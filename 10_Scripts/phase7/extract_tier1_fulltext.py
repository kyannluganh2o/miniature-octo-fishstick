#!/usr/bin/env python3
"""Create the Phase 7 machine-readable layer for approved Tier 1 PDFs.

The script is intentionally conservative: it reads only canonical PDFs named by
the current inventory, validates paper identity against library_master, refuses
to overwrite an existing per-paper directory, and never writes under
02_PDF_Raw.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import shutil
import tempfile
from datetime import datetime, timezone
from pathlib import Path

from pypdf import PdfReader


PROJECT_ROOT = Path(__file__).resolve().parents[2]
MASTER_PATH = PROJECT_ROOT / "01_Library/master/library_master.csv"
INVENTORY_PATH = PROJECT_ROOT / "11_QC/missing_pdf/pdf_inventory.csv"
TIERS_PATH = PROJECT_ROOT / "00_Project/reading_tiers.csv"
RAW_ROOT = (PROJECT_ROOT / "02_PDF_Raw").resolve()
OUTPUT_ROOT = PROJECT_ROOT / "03_Paper_Processed"

HEADING_RE = re.compile(
    r"^(?:(\d+(?:\.\d+)*)\.?\s+)?"
    r"(abstract|introduction|background|method(?:s|ology)?|experimental(?:\s+setup|\s+method(?:s)?)?|"
    r"numerical(?:\s+method(?:s)?|\s+model)?|theoretical(?:\s+model)?|model(?:ing|ling)?|"
    r"results?(?:\s+and\s+discussion)?|discussion|conclusions?|summary|outlook|references|appendix(?:\s+[A-Z])?)"
    r"(?:\s*[:.-].*)?$",
    re.IGNORECASE,
)


def read_csv_index(path: Path, key: str) -> dict[str, dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    result: dict[str, dict[str, str]] = {}
    for row in rows:
        value = row[key]
        if value in result:
            raise ValueError(f"Duplicate {key}={value} in {path}")
        result[value] = row
    return result


def normalize_identity(text: str) -> list[str]:
    words = re.findall(r"[a-z0-9]+", text.lower())
    stop = {"a", "an", "and", "at", "for", "in", "of", "on", "the", "to", "with"}
    return [word for word in words if word not in stop and len(word) > 1]


def identity_coverage(title: str, first_page_text: str) -> float:
    title_words = normalize_identity(title)
    page_words = set(normalize_identity(first_page_text))
    if not title_words:
        return 0.0
    return sum(word in page_words for word in title_words) / len(title_words)


def extract_pages(reader: PdfReader) -> tuple[list[str], list[int]]:
    pages: list[str] = []
    unreadable: list[int] = []
    for page_number, page in enumerate(reader.pages, start=1):
        try:
            text = page.extract_text() or ""
        except Exception:
            text = ""
        text = text.replace("\x00", "").strip()
        if not text:
            unreadable.append(page_number)
        pages.append(text)
    return pages, unreadable


def detect_headings(pages: list[str]) -> list[dict[str, object]]:
    candidates: list[tuple[int, str]] = []
    for page_number, text in enumerate(pages, start=1):
        for raw_line in text.splitlines():
            line = re.sub(r"\s+", " ", raw_line).strip()
            if len(line) > 100:
                continue
            match = HEADING_RE.match(line)
            if match:
                title = line.rstrip(" .:")
                if not candidates or candidates[-1] != (page_number, title):
                    candidates.append((page_number, title))

    if not candidates or candidates[0][0] != 1:
        candidates.insert(0, (1, "Front matter and abstract"))

    deduplicated: list[tuple[int, str]] = []
    seen_per_page: set[tuple[int, str]] = set()
    for page_number, title in candidates:
        key = (page_number, title.lower())
        if key not in seen_per_page:
            deduplicated.append((page_number, title))
            seen_per_page.add(key)

    sections: list[dict[str, object]] = []
    for index, (start_page, title) in enumerate(deduplicated, start=1):
        next_start = deduplicated[index][0] if index < len(deduplicated) else len(pages) + 1
        end_page = max(start_page, next_start - 1)
        sections.append(
            {
                "section_id": f"S{index:02d}",
                "section_title": title,
                "pdf_page_start": start_page,
                "pdf_page_end": end_page,
                "boundary_status": "best_effort",
            }
        )
    return sections


def page_sections(page_count: int, sections: list[dict[str, object]]) -> list[str]:
    labels: list[str] = []
    for page in range(1, page_count + 1):
        covering = [
            str(section["section_title"])
            for section in sections
            if int(section["pdf_page_start"]) <= page <= int(section["pdf_page_end"])
        ]
        labels.append(covering[-1] if covering else "Unclassified")
    return labels


def write_outputs(
    destination: Path,
    paper_id: str,
    master: dict[str, str],
    inventory: dict[str, str],
    pages: list[str],
    sections: list[dict[str, object]],
    pdf_sha256: str,
    started: str,
    completed: str,
    unreadable_pages: list[int],
    identity_score: float,
    identity_basis: str,
) -> None:
    metadata = {
        "paper_id": paper_id,
        "source_record_id": master["source_record_id"],
        "title": master["title"],
        "authors": master["authors"],
        "year": master["year"],
        "journal": master["journal"] or "NV",
        "doi": master["doi"] or "NV",
        "pdf_filename": inventory["current_filename"],
        "pdf_relpath": inventory["current_relpath"],
        "page_count": len(pages),
        "processing_date": completed[:10],
        "pdf_sha256": pdf_sha256,
    }
    (destination / "metadata.json").write_text(
        json.dumps(metadata, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    text_chunks = []
    for page_number, text in enumerate(pages, start=1):
        text_chunks.append(f"<!-- PDF_PAGE: {page_number} -->\n\n{text}\n")
    (destination / "text.md").write_text("\n".join(text_chunks), encoding="utf-8")

    (destination / "sections.json").write_text(
        json.dumps(sections, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    labels = page_sections(len(pages), sections)
    with (destination / "page_map.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle, fieldnames=["paper_id", "pdf_page", "printed_page", "section", "notes"]
        )
        writer.writeheader()
        for page_number, label in enumerate(labels, start=1):
            writer.writerow(
                {
                    "paper_id": paper_id,
                    "pdf_page": page_number,
                    "printed_page": "",
                    "section": label,
                    "notes": "Printed page not independently verified.",
                }
            )

    log = {
        "paper_id": paper_id,
        "input_pdf": inventory["current_relpath"],
        "processing_started": started,
        "processing_completed": completed,
        "parser_method": "pypdf page-by-page text extraction; identity checked against library_master",
        "identity_title_token_coverage": round(identity_score, 4),
        "identity_confirmation_basis": identity_basis,
        "warnings": [] if not unreadable_pages else ["One or more pages yielded no extractable text."],
        "unreadable_pages": unreadable_pages,
        "extraction_limitations": [
            "Multi-column order, equations and embedded glyphs may require PDF cross-check.",
            "Section boundaries are best-effort and require scientific-reading review.",
            "No figure digitization or bulk image extraction was performed.",
        ],
    }
    (destination / "processing_log.json").write_text(
        json.dumps(log, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


def process_paper(
    paper_id: str,
    master_index: dict[str, dict[str, str]],
    inventory_index: dict[str, dict[str, str]],
    tier_index: dict[str, dict[str, str]],
) -> dict[str, object]:
    if paper_id not in master_index or paper_id not in inventory_index or paper_id not in tier_index:
        raise ValueError(f"{paper_id}: missing master, inventory, or tier record")
    master = master_index[paper_id]
    inventory = inventory_index[paper_id]
    tier = tier_index[paper_id]
    if tier["reading_tier"] != "tier1" or tier["reading_status"] != "not_started":
        raise ValueError(f"{paper_id}: not an unprocessed Tier 1 record")
    if not (
        inventory["file_exists"] == "yes"
        and inventory["pdf_readable"] == "yes"
        and inventory["pdf_match_status"] == "matched"
    ):
        raise ValueError(f"{paper_id}: PDF is not exists/readable/matched")
    if inventory["source_record_id"] != master["source_record_id"]:
        raise ValueError(f"{paper_id}: source_record_id mismatch")

    pdf_path = (PROJECT_ROOT / inventory["current_relpath"]).resolve()
    if not pdf_path.is_relative_to(RAW_ROOT):
        raise ValueError(f"{paper_id}: PDF path escaped immutable raw root")
    if not pdf_path.is_file():
        raise FileNotFoundError(pdf_path)

    destination = OUTPUT_ROOT / master["library_primary"] / paper_id
    if destination.exists():
        raise FileExistsError(f"Refusing to overwrite existing output: {destination}")

    started = datetime.now(timezone.utc).isoformat(timespec="seconds")
    reader = PdfReader(str(pdf_path))
    pages, unreadable_pages = extract_pages(reader)
    if not pages or unreadable_pages:
        raise ValueError(f"{paper_id}: unreadable PDF pages {unreadable_pages}")
    score = identity_coverage(master["title"], pages[0])
    identity_basis = "library_master title token coverage >= 0.70"
    if score < 0.70:
        first_page_lower = pages[0].lower()
        author_ok = bool(master.get("first_author", "").strip()) and master["first_author"].lower() in first_page_lower
        year_ok = bool(master.get("year", "").strip()) and master["year"] in pages[0]
        if not (author_ok and year_ok and inventory["pdf_match_status"] == "matched"):
            raise ValueError(
                f"{paper_id}: identity token coverage {score:.3f} below 0.70 and "
                "author/year fallback failed"
            )
        identity_basis = (
            "inventory matched plus first-author and year confirmed on first PDF page; "
            "library_master title is malformed or noncanonical"
        )
    inventory_pages = inventory.get("page_count", "").strip()
    if inventory_pages and int(inventory_pages) != len(pages):
        raise ValueError(
            f"{paper_id}: page-count mismatch inventory={inventory_pages} extracted={len(pages)}"
        )

    sections = detect_headings(pages)
    pdf_sha256 = hashlib.sha256(pdf_path.read_bytes()).hexdigest()
    completed = datetime.now(timezone.utc).isoformat(timespec="seconds")
    with tempfile.TemporaryDirectory(prefix=f"phase7_{paper_id}_") as temp_dir:
        temporary = Path(temp_dir) / paper_id
        temporary.mkdir()
        write_outputs(
            temporary,
            paper_id,
            master,
            inventory,
            pages,
            sections,
            pdf_sha256,
            started,
            completed,
            unreadable_pages,
            score,
            identity_basis,
        )
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(temporary, destination)

    return {
        "paper_id": paper_id,
        "pages": len(pages),
        "sections": len(sections),
        "identity_coverage": round(score, 4),
        "pdf_sha256": pdf_sha256,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("paper_ids", nargs="+", help="Locked Paper IDs to process")
    args = parser.parse_args()

    master_index = read_csv_index(MASTER_PATH, "paper_id")
    inventory_index = read_csv_index(INVENTORY_PATH, "paper_id")
    tier_index = read_csv_index(TIERS_PATH, "paper_id")

    results = [
        process_paper(paper_id, master_index, inventory_index, tier_index)
        for paper_id in args.paper_ids
    ]
    print(json.dumps(results, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
