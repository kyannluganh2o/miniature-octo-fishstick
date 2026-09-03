#!/usr/bin/env python3
"""Create the read-only-derived machine-readable layer for eligible Tier 2 PDFs.

The script accepts only locked Tier 2 records whose inventory entry says that
the canonical local PDF exists, is readable, and identity-matched.  It refuses
to overwrite outputs and never writes below ``02_PDF_Raw``.
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


ROOT = Path(__file__).resolve().parents[2]
RAW_ROOT = (ROOT / "02_PDF_Raw").resolve()
OUTPUT_ROOT = ROOT / "03_Paper_Processed"


def index(path: Path, key: str) -> dict[str, dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    if len({row[key] for row in rows}) != len(rows):
        raise ValueError(f"duplicate {key} in {path}")
    return {row[key]: row for row in rows}


def tokens(value: str) -> list[str]:
    stop = {"a", "an", "and", "at", "for", "in", "of", "on", "the", "to", "with"}
    return [w for w in re.findall(r"[a-z0-9]+", value.lower()) if len(w) > 1 and w not in stop]


def title_coverage(title: str, page: str) -> float:
    expected = tokens(title)
    observed = set(tokens(page))
    return sum(word in observed for word in expected) / len(expected) if expected else 0.0


def headings(pages: list[str]) -> list[dict[str, object]]:
    pattern = re.compile(
        r"^(?:(\d+(?:\.\d+)*)\.?\s+)?(abstract|introduction|background|method(?:s|ology)?|"
        r"experimental(?:\s+setup|\s+method(?:s)?)?|numerical(?:\s+method(?:s)?|\s+model)?|"
        r"model(?:ing|ling)?|results?(?:\s+and\s+discussion)?|discussion|conclusions?|summary|"
        r"outlook|references|appendix(?:\s+[A-Z])?)(?:\s*[:.-].*)?$", re.I
    )
    found: list[tuple[int, str]] = []
    for page_no, text in enumerate(pages, 1):
        for raw in text.splitlines():
            line = re.sub(r"\s+", " ", raw).strip()
            if len(line) <= 100 and pattern.match(line):
                item = (page_no, line.rstrip(" .:"))
                if item not in found:
                    found.append(item)
    if not found or found[0][0] != 1:
        found.insert(0, (1, "Front matter and abstract"))
    result = []
    for pos, (start, title) in enumerate(found):
        next_start = found[pos + 1][0] if pos + 1 < len(found) else len(pages) + 1
        result.append({
            "section_id": f"S{pos + 1:02d}", "section_title": title,
            "pdf_page_start": start, "pdf_page_end": max(start, next_start - 1),
            "boundary_status": "best_effort",
        })
    return result


def process(paper_id: str, master: dict[str, dict[str, str]], inventory: dict[str, dict[str, str]], tiers: dict[str, dict[str, str]]) -> dict[str, object]:
    if paper_id not in master or paper_id not in inventory or paper_id not in tiers:
        raise ValueError(f"{paper_id}: canonical record missing")
    m, inv, tier = master[paper_id], inventory[paper_id], tiers[paper_id]
    if tier["reading_tier"] != "tier2" or tier["reading_status"] != "not_started":
        raise ValueError(f"{paper_id}: not an unprocessed Tier 2 paper")
    if not (inv["file_exists"] == "yes" and inv["pdf_readable"] == "yes" and inv["pdf_match_status"] == "matched"):
        raise ValueError(f"{paper_id}: PDF is not exists/readable/matched")
    if inv["source_record_id"] != m["source_record_id"]:
        raise ValueError(f"{paper_id}: source_record_id mismatch")
    pdf = (ROOT / inv["current_relpath"]).resolve()
    if not pdf.is_relative_to(RAW_ROOT) or not pdf.is_file():
        raise ValueError(f"{paper_id}: PDF path invalid")
    destination = OUTPUT_ROOT / m["library_primary"] / paper_id
    if destination.exists():
        raise FileExistsError(f"refusing to overwrite {destination}")

    started = datetime.now(timezone.utc).isoformat(timespec="seconds")
    reader = PdfReader(str(pdf))
    pages: list[str] = []
    unreadable: list[int] = []
    for page_no, page in enumerate(reader.pages, 1):
        try:
            text = (page.extract_text() or "").replace("\x00", "").strip()
        except Exception:
            text = ""
        if not text:
            unreadable.append(page_no)
        pages.append(text)
    if not pages or unreadable:
        raise ValueError(f"{paper_id}: unreadable pages {unreadable}")
    if inv.get("page_count", "").strip() and int(inv["page_count"]) != len(pages):
        raise ValueError(f"{paper_id}: page count mismatch")
    coverage = title_coverage(m["title"], pages[0])
    fallback = m["first_author"].lower() in pages[0].lower() and m["year"] in pages[0]
    if coverage < 0.70 and not fallback:
        raise ValueError(f"{paper_id}: identity coverage {coverage:.3f}, fallback failed")
    identity_basis = "title token coverage >= 0.70" if coverage >= 0.70 else "inventory match plus first author and year on first page"
    sections = headings(pages)
    completed = datetime.now(timezone.utc).isoformat(timespec="seconds")
    sha256 = hashlib.sha256(pdf.read_bytes()).hexdigest()

    with tempfile.TemporaryDirectory(prefix=f"phase8_{paper_id}_") as temp:
        out = Path(temp) / paper_id
        out.mkdir()
        metadata = {
            "paper_id": paper_id, "source_record_id": m["source_record_id"], "title": m["title"],
            "authors": m["authors"], "year": m["year"], "journal": m["journal"] or "NV",
            "doi": m["doi"] or "NV", "pdf_filename": inv["current_filename"],
            "pdf_relpath": inv["current_relpath"], "page_count": len(pages),
            "processing_date": completed[:10], "pdf_sha256": sha256,
        }
        (out / "metadata.json").write_text(json.dumps(metadata, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        (out / "text.md").write_text("\n".join(f"<!-- PDF_PAGE: {i} -->\n\n{text}\n" for i, text in enumerate(pages, 1)), encoding="utf-8")
        (out / "sections.json").write_text(json.dumps(sections, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        with (out / "page_map.csv").open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=["paper_id", "pdf_page", "printed_page", "section", "notes"])
            writer.writeheader()
            for page_no in range(1, len(pages) + 1):
                labels = [str(s["section_title"]) for s in sections if int(s["pdf_page_start"]) <= page_no <= int(s["pdf_page_end"])]
                writer.writerow({"paper_id": paper_id, "pdf_page": page_no, "printed_page": "", "section": labels[-1] if labels else "Unclassified", "notes": "Printed page not independently verified."})
        log = {
            "paper_id": paper_id, "input_pdf": inv["current_relpath"], "processing_started": started,
            "processing_completed": completed, "parser_method": "pypdf page-by-page text extraction",
            "identity_title_token_coverage": round(coverage, 4), "identity_confirmation_basis": identity_basis,
            "warnings": [], "unreadable_pages": [],
            "extraction_limitations": ["Multi-column order, equations, and glyphs may require PDF cross-check.", "Section boundaries are best-effort.", "No figure digitization was performed."],
        }
        (out / "processing_log.json").write_text(json.dumps(log, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(out, destination)
    return {"paper_id": paper_id, "pages": len(pages), "sections": len(sections), "identity_coverage": round(coverage, 4), "pdf_sha256": sha256}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("paper_ids", nargs="+")
    args = parser.parse_args()
    master = index(ROOT / "01_Library/master/library_master.csv", "paper_id")
    inventory = index(ROOT / "11_QC/missing_pdf/pdf_inventory.csv", "paper_id")
    tiers = index(ROOT / "00_Project/reading_tiers.csv", "paper_id")
    print(json.dumps([process(pid, master, inventory, tiers) for pid in args.paper_ids], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
