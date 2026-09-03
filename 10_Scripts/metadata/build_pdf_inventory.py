#!/usr/bin/env python3
"""Build the frozen-library PDF inventory without modifying raw PDFs.

The script is deterministic and idempotent. It reads only from 02_PDF_Raw and
the canonical library tables, then rewrites the three approved inventory outputs
under 11_QC/missing_pdf. It never renames, moves, deletes, or edits a PDF.
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import re
import tempfile
from collections import Counter
from datetime import date
from pathlib import Path
from typing import Any, Iterable


INVENTORY_FIELDS = [
    "paper_id",
    "source_record_id",
    "library",
    "expected_record",
    "current_filename",
    "current_relpath",
    "file_exists",
    "file_size_bytes",
    "page_count",
    "pdf_readable",
    "pdf_status",
    "pdf_match_status",
    "identity_basis",
    "verification_flags",
    "notes",
]

MISSING_FIELDS = [
    "paper_id",
    "source_record_id",
    "library",
    "year",
    "first_author",
    "title",
    "doi",
    "doi_status",
    "pdf_status",
    "retry_priority",
    "notes",
]

DOI_RE = re.compile(r"10\.\d{4,9}/[^\s<>\"']+", re.IGNORECASE)
YEAR_RE = re.compile(r"\b(?:19|20)\d{2}\b")
STOPWORDS = {
    "about",
    "analysis",
    "and",
    "application",
    "direct",
    "effect",
    "experimental",
    "for",
    "from",
    "high",
    "injection",
    "investigation",
    "numerical",
    "of",
    "on",
    "pressure",
    "study",
    "the",
    "under",
    "using",
    "with",
}


def frozen_mapping() -> list[dict[str, str]]:
    """Return the user-approved frozen order and immutable Paper ID mapping."""

    source_ids: list[tuple[str, str]] = []
    source_ids.extend(("A", f"A-NG-{index:02d}") for index in range(1, 18))
    source_ids.extend(("A", f"A-H2-{index:02d}") for index in range(1, 10))
    source_ids.extend(("A", f"A-R-{index:02d}") for index in range(1, 5))

    source_ids.extend(("B", f"B-T-{index:02d}") for index in range(1, 6))
    source_ids.extend(("B", f"B-H2-{index:02d}") for index in range(1, 11))
    source_ids.extend(("B", f"B-NG-{index:02d}") for index in range(1, 6))
    source_ids.extend(("B", f"B-E-{index:02d}") for index in range(1, 11))

    source_ids.extend(("C", f"C-F-{index:02d}") for index in range(1, 8))
    source_ids.extend(("C", f"C-SD-{index:02d}") for index in range(1, 14))
    source_ids.extend(("C", f"C-ST-{index:02d}") for index in range(1, 7))
    source_ids.extend(("C", f"C-PC-{index:02d}") for index in range(1, 7))
    source_ids.extend(("C", f"C-MD-{index:02d}") for index in range(1, 5))

    source_ids.extend(("D", f"D-IC-{index:02d}") for index in range(1, 6))
    source_ids.extend(("D", f"D-RDE-{index:02d}") for index in range(1, 11))
    source_ids.extend(("D", f"D-DW-{index:02d}") for index in range(1, 5))

    counters: Counter[str] = Counter()
    records: list[dict[str, str]] = []
    for library, source_record_id in source_ids:
        counters[library] += 1
        records.append(
            {
                "library": library,
                "source_record_id": source_record_id,
                "paper_id": f"{library}{counters[library]:03d}",
            }
        )

    expected = {"A": 30, "B": 30, "C": 36, "D": 19}
    if dict(counters) != expected or len(records) != 115:
        raise RuntimeError(f"Frozen mapping construction failed: {dict(counters)}")
    return records


USER_SUPPLIED_MISSING: dict[str, dict[str, str]] = {
    "A001": {"doi": "10.1115/1.2432894"},
    "A002": {"doi": "10.4271/2015-01-0865"},
    "A005": {"doi": "10.4271/2016-01-0807"},
    "A006": {"doi": "10.4271/2017-01-0763"},
    "A007": {"doi": "10.1115/1.4039934"},
    "A008": {"doi": "10.1115/ICEF2018-9579"},
    "A009": {"doi": "10.1115/1.4043643"},
    "A011": {"doi": "10.1177/1468087419836877"},
    "A012": {"doi": "10.1115/ICEF2021-74466"},
    "B006": {
        "title": "Transient High-Pressure Hydrogen Jet Measurements",
        "doi": "10.4271/2006-01-0652",
    },
    "B008": {
        "title": "A Numerical Analysis of Hydrogen Underexpanded Jets Under Real Gas Assumption",
        "doi": "10.1115/1.4025253",
    },
    "B018": {
        "title": "Under-Expanded Gaseous Jets Characterization for Application in Direct Injection Engines: Experimental and Numerical Approach",
        "doi": "10.4271/2020-01-0325",
    },
    "B021": {
        "title": "Numerical characterization of hydrogen under-expanded jets with a focus on Internal Combustion Engines applications",
        "doi": "10.1177/14680874221148789",
    },
    "C004": {
        "title": "Aerobreakup of Newtonian and Viscoelastic Liquids",
        "doi": "10.1146/annurev-fluid-122109-160638",
    },
    "C005": {
        "title": "Secondary breakup of a drop at moderate Weber numbers",
        "doi": "10.1098/rspa.2014.0930",
    },
    "C011": {
        "title": "Numerical Study on Liquid Droplet Internal Flow Under Shock Impact",
        "doi": "10.2514/1.J057134",
    },
    "C029": {
        "title": "Numerical study of the transcritical shock-droplet interaction",
        "doi": "10.1103/PhysRevFluids.6.113601",
    },
    "C036": {
        "title": "Shock-induced aerobreakup of parallel-arranged droplets",
        "doi": "10.1103/5398-z2gf",
    },
    "D001": {
        "title": "Effect of Ambient Temperature and Density on Shock Wave Generation in a Diesel Engine",
        "doi": "10.1615/AtomizSpr.v20.i2.50",
    },
    "D019": {
        "title": "Comparative analysis of detonation and shock waves interacting with droplets: Characteristics and mechanisms",
        "doi": "10.1103/mp9z-tlk3",
    },
}


def normalize_compact(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", value.casefold())


def author_name_matches(text: str, expected_author: str) -> bool:
    expected = normalize_compact(expected_author)
    if not expected:
        return False
    if len(expected) <= 3:
        tokens = [normalize_compact(token) for token in re.findall(r"[A-Za-z0-9]+", text)]
        return expected in tokens
    return expected in normalize_compact(text)


def normalized_words(value: str) -> set[str]:
    value = re.sub(r"(?<=[a-z])(?=[A-Z])", " ", value)
    words = re.findall(r"[a-z0-9]+", value.casefold())
    return {word for word in words if len(word) >= 4 and word not in STOPWORDS}


def clean_doi(value: str) -> str:
    value = re.sub(
        r"^https?://(?:dx\.)?doi\.org/", "", value.strip(), flags=re.IGNORECASE
    )
    return value.rstrip(".,;:)]}>")


def first_doi(text: str) -> str:
    match = DOI_RE.search(text)
    return clean_doi(match.group(0)) if match else ""


def parse_filename(path: Path, source_record_id: str) -> dict[str, str]:
    name_without_pdf = re.sub(r"(?i)\.pdf$", "", path.name)
    remainder = name_without_pdf[len(source_record_id) + 1 :]
    parts = remainder.split("_")
    year = parts[0] if parts and re.fullmatch(r"(?:19|20)\d{2}", parts[0]) else ""
    first_author = parts[1] if len(parts) > 1 else ""
    short_title = " ".join(parts[2:]) if len(parts) > 2 else ""
    return {"year": year, "first_author": first_author, "short_title": short_title}


def plausible_metadata_title(value: str, filename: str) -> bool:
    compact = normalize_compact(value)
    return (
        len(value.strip()) >= 15
        and compact not in {"untitled", "title", "document", "microsoftword"}
        and compact != normalize_compact(filename)
        and not compact.startswith("microsoftword")
    )


def title_from_front(front_text: str, first_author: str, short_title: str) -> str:
    """Extract a conservative title only when the author line anchors it."""

    if not normalize_compact(first_author):
        return ""
    lines = [re.sub(r"\s+", " ", line).strip() for line in front_text.splitlines()]
    lines = [line for line in lines if line]
    author_index = next(
        (
            index
            for index, line in enumerate(lines[:30])
            if author_name_matches(line, first_author)
        ),
        None,
    )
    if author_index is None or author_index == 0:
        return ""

    candidates: list[str] = []
    for line in lines[max(0, author_index - 5) : author_index]:
        lower = line.casefold()
        if (
            DOI_RE.search(line)
            or re.fullmatch(r"\d+", line)
            or lower.startswith(("http", "www.", "doi:", "copyright", "contents list"))
            or "available online" in lower
            or "printed in" in lower
        ):
            continue
        if re.search(r"\bvol\.?\s*\d+", lower) and len(line) < 100:
            continue
        candidates.append(line)

    candidate = " ".join(candidates[-3:]).strip(" -")
    if not 15 <= len(candidate) <= 400:
        return ""
    descriptor_words = normalized_words(short_title)
    candidate_words = normalized_words(candidate)
    if descriptor_words and len(descriptor_words & candidate_words) < 2:
        return ""
    return candidate


def author_line_from_front(front_text: str, first_author: str) -> str:
    if not normalize_compact(first_author):
        return ""
    lines = [re.sub(r"\s+", " ", line).strip() for line in front_text.splitlines()]
    for line in lines[:35]:
        if author_name_matches(line, first_author) and 3 <= len(line) <= 350:
            lower = line.casefold()
            if not any(token in lower for token in ("university", "institute", "journal", "doi")):
                return line
    return ""


def journal_from_metadata(subject: str) -> str:
    subject = re.sub(r"\s+", " ", subject).strip()
    if not subject:
        return ""
    if "journal" in subject.casefold():
        return subject.split(",", 1)[0].strip()
    return ""


def inspect_pdf(path: Path, source_record_id: str) -> dict[str, Any]:
    filename_parts = parse_filename(path, source_record_id)
    result: dict[str, Any] = {
        "page_count": "",
        "pdf_readable": "no",
        "title": "",
        "authors": "",
        "first_author": "",
        "year": filename_parts["year"],
        "journal": "",
        "volume": "",
        "issue": "",
        "pages_or_article_number": "",
        "doi": "",
        "doi_status": "missing",
        "publication_type": "",
        "language": "",
        "pdf_match_status": "ambiguous",
        "identity_basis": [],
        "verification_flags": [],
        "notes": "",
    }

    try:
        from pypdf import PdfReader

        reader = PdfReader(str(path), strict=False)
        if reader.is_encrypted:
            try:
                reader.decrypt("")
            except Exception:
                pass
        result["page_count"] = len(reader.pages)
        metadata = dict(reader.metadata or {})
        front_text = "\n".join(
            (reader.pages[index].extract_text() or "")
            for index in range(min(2, len(reader.pages)))
        )
        result["pdf_readable"] = "yes"

        meta_title = str(metadata.get("/Title", "")).strip()
        meta_author = str(metadata.get("/Author", "")).strip()
        meta_subject = str(metadata.get("/Subject", "")).strip()
        metadata_text = "\n".join(str(value) for value in metadata.values())

        if plausible_metadata_title(meta_title, path.name):
            result["title"] = re.sub(r"\s+", " ", meta_title)
            result["identity_basis"].append("embedded_title")
        else:
            result["title"] = title_from_front(
                front_text,
                filename_parts["first_author"],
                filename_parts["short_title"],
            )
            if result["title"]:
                result["identity_basis"].append("front_matter_title")

        expected_author = normalize_compact(filename_parts["first_author"])
        if (
            meta_author
            and len(meta_author) <= 500
            and expected_author
            and author_name_matches(meta_author, filename_parts["first_author"])
        ):
            result["authors"] = re.sub(r"\s+", " ", meta_author)
            result["identity_basis"].append("embedded_authors")
        else:
            result["authors"] = author_line_from_front(
                front_text, filename_parts["first_author"]
            )
            if result["authors"]:
                result["identity_basis"].append("front_matter_authors")

        author_match = author_name_matches(
            front_text[:12000] + "\n" + meta_author,
            filename_parts["first_author"],
        )
        year_match = bool(
            filename_parts["year"] and filename_parts["year"] in front_text[:12000]
        )
        if author_match:
            result["first_author"] = filename_parts["first_author"]
            result["identity_basis"].append("first_author_front_matter")
        if year_match:
            result["identity_basis"].append("year_front_matter")

        doi = first_doi(metadata_text) or first_doi(front_text[:20000])
        if doi:
            result["doi"] = doi
            result["doi_status"] = "verified"
            result["identity_basis"].append("doi_pdf")

        result["journal"] = journal_from_metadata(meta_subject)

        short_words = normalized_words(filename_parts["short_title"])
        title_words = normalized_words(result["title"])
        title_match = bool(short_words and len(short_words & title_words) >= 2)
        if title_match:
            result["identity_basis"].append("title_descriptor_consistent")

        identity_features = sum((author_match, year_match, title_match))
        if identity_features >= 2:
            result["pdf_match_status"] = "matched"
        else:
            result["pdf_match_status"] = "ambiguous"
            result["verification_flags"].append("pdf_identity_unverified")

        if not result["title"]:
            result["verification_flags"].append("title_not_verified")
        if not result["first_author"]:
            result["verification_flags"].append("author_not_verified")
    except Exception as exc:
        result["pdf_readable"] = "no"
        result["pdf_match_status"] = "ambiguous"
        result["verification_flags"].append("unreadable_pdf")
        result["notes"] = f"PDF read failed: {type(exc).__name__}"

    result["identity_basis"] = list(dict.fromkeys(result["identity_basis"]))
    result["verification_flags"] = list(dict.fromkeys(result["verification_flags"]))
    return result


def load_master(master_path: Path) -> dict[str, dict[str, str]]:
    if not master_path.exists() or master_path.stat().st_size == 0:
        return {}
    with master_path.open("r", encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    return {
        row.get("source_record_id", ""): row
        for row in rows
        if row.get("source_record_id", "")
    }


def atomic_write_csv(path: Path, fields: list[str], rows: Iterable[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temp_name = tempfile.mkstemp(prefix=path.name + ".", suffix=".tmp", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
            writer.writeheader()
            writer.writerows(rows)
        os.replace(temp_name, path)
    except Exception:
        try:
            os.unlink(temp_name)
        except FileNotFoundError:
            pass
        raise


def atomic_write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temp_name = tempfile.mkstemp(prefix=path.name + ".", suffix=".tmp", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="") as handle:
            handle.write(content)
        os.replace(temp_name, path)
    except Exception:
        try:
            os.unlink(temp_name)
        except FileNotFoundError:
            pass
        raise


def scan(project_root: Path) -> dict[str, Any]:
    mapping = frozen_mapping()
    raw_root = project_root / "02_PDF_Raw"
    master = load_master(project_root / "01_Library" / "master" / "library_master.csv")

    expected_by_source = {row["source_record_id"]: row for row in mapping}
    pdfs = sorted(raw_root.glob("*/*.pdf"), key=lambda path: path.as_posix().casefold())
    candidates: dict[str, list[Path]] = {source: [] for source in expected_by_source}
    unexpected: list[Path] = []

    source_ids_longest_first = sorted(expected_by_source, key=len, reverse=True)
    for pdf_path in pdfs:
        source = next(
            (
                candidate
                for candidate in source_ids_longest_first
                if pdf_path.name.casefold().startswith((candidate + "_").casefold())
            ),
            None,
        )
        if source is None:
            unexpected.append(pdf_path)
        else:
            candidates[source].append(pdf_path)

    inventory_rows: list[dict[str, Any]] = []
    metadata_rows: list[dict[str, Any]] = []
    missing_rows: list[dict[str, Any]] = []

    for record in mapping:
        source_id = record["source_record_id"]
        paper_id = record["paper_id"]
        library = record["library"]
        paths = candidates[source_id]
        current_master = master.get(source_id, {})

        if current_master.get("paper_id") and current_master["paper_id"] != paper_id:
            raise RuntimeError(
                f"Locked mapping conflict for {source_id}: "
                f"{current_master['paper_id']} != {paper_id}"
            )

        if len(paths) == 0:
            supplied = USER_SUPPLIED_MISSING.get(paper_id, {})
            title = current_master.get("title", "") or supplied.get("title", "")
            doi = current_master.get("doi", "") or supplied.get("doi", "")
            year = current_master.get("year", "")
            first_author = current_master.get("first_author", "")
            metadata = {
                **record,
                "title": title,
                "authors": current_master.get("authors", ""),
                "first_author": first_author,
                "year": year,
                "journal": current_master.get("journal", ""),
                "volume": current_master.get("volume", ""),
                "issue": current_master.get("issue", ""),
                "pages_or_article_number": current_master.get(
                    "pages_or_article_number", ""
                ),
                "doi": doi,
                "doi_status": "unverified" if doi else "missing",
                "publication_type": current_master.get("publication_type", ""),
                "language": current_master.get("language", ""),
                "pdf_status": "missing",
                "pdf_filename": "",
                "pdf_relpath": "",
                "pdf_match_status": "not_checked",
                "page_count": "",
                "pdf_readable": "",
                "identity_basis": [],
                "verification_flags": ["pdf_missing"],
                "notes": "User-supplied DOI/title retained as unverified metadata."
                if doi or title
                else "PDF missing; bibliographic metadata not available locally.",
            }
            inventory_rows.append(
                {
                    **record,
                    "expected_record": "yes",
                    "current_filename": "",
                    "current_relpath": "",
                    "file_exists": "no",
                    "file_size_bytes": "",
                    "page_count": "",
                    "pdf_readable": "",
                    "pdf_status": "missing",
                    "pdf_match_status": "not_checked",
                    "identity_basis": "",
                    "verification_flags": "pdf_missing",
                    "notes": metadata["notes"],
                }
            )
            missing_rows.append(
                {
                    **record,
                    "year": year,
                    "first_author": first_author,
                    "title": title,
                    "doi": doi,
                    "doi_status": "unverified" if doi else "missing",
                    "pdf_status": "missing",
                    "retry_priority": "",
                    "notes": metadata["notes"],
                }
            )
            metadata_rows.append(metadata)
            continue

        if len(paths) > 1:
            joined_names = ";".join(path.name for path in paths)
            joined_relpaths = ";".join(
                path.relative_to(project_root).as_posix() for path in paths
            )
            metadata = {
                **record,
                "title": "",
                "authors": "",
                "first_author": "",
                "year": "",
                "journal": "",
                "volume": "",
                "issue": "",
                "pages_or_article_number": "",
                "doi": "",
                "doi_status": "missing",
                "publication_type": "",
                "language": "",
                "pdf_status": "downloaded",
                "pdf_filename": joined_names,
                "pdf_relpath": joined_relpaths,
                "pdf_match_status": "ambiguous",
                "page_count": "",
                "pdf_readable": "",
                "identity_basis": ["source_record_id_filename"],
                "verification_flags": ["multiple_pdf_candidates"],
                "notes": "Multiple PDF candidates preserved; no candidate selected.",
            }
            inventory_rows.append(
                {
                    **record,
                    "expected_record": "yes",
                    "current_filename": joined_names,
                    "current_relpath": joined_relpaths,
                    "file_exists": "yes",
                    "file_size_bytes": "",
                    "page_count": "",
                    "pdf_readable": "",
                    "pdf_status": "downloaded",
                    "pdf_match_status": "ambiguous",
                    "identity_basis": "source_record_id_filename",
                    "verification_flags": "multiple_pdf_candidates",
                    "notes": metadata["notes"],
                }
            )
            metadata_rows.append(metadata)
            continue

        pdf_path = paths[0]
        inspected = inspect_pdf(pdf_path, source_id)
        relpath = pdf_path.relative_to(project_root).as_posix()
        identity_basis = ["source_record_id_filename", *inspected["identity_basis"]]
        metadata = {
            **record,
            **inspected,
            "pdf_status": "downloaded",
            "pdf_filename": pdf_path.name,
            "pdf_relpath": relpath,
            "identity_basis": list(dict.fromkeys(identity_basis)),
        }
        inventory_rows.append(
            {
                **record,
                "expected_record": "yes",
                "current_filename": pdf_path.name,
                "current_relpath": relpath,
                "file_exists": "yes",
                "file_size_bytes": pdf_path.stat().st_size,
                "page_count": inspected["page_count"],
                "pdf_readable": inspected["pdf_readable"],
                "pdf_status": "downloaded",
                "pdf_match_status": inspected["pdf_match_status"],
                "identity_basis": ";".join(metadata["identity_basis"]),
                "verification_flags": ";".join(inspected["verification_flags"]),
                "notes": inspected["notes"],
            }
        )
        metadata_rows.append(metadata)

    stats = {
        "total_records": len(mapping),
        "library_counts": dict(Counter(row["library"] for row in mapping)),
        "downloaded": sum(row["file_exists"] == "yes" for row in inventory_rows),
        "missing": sum(row["file_exists"] == "no" for row in inventory_rows),
        "readable": sum(row["pdf_readable"] == "yes" for row in inventory_rows),
        "unreadable": sum(row["pdf_readable"] == "no" for row in inventory_rows),
        "matched": sum(
            row["pdf_match_status"] == "matched" for row in inventory_rows
        ),
        "ambiguous": sum(
            row["pdf_match_status"] == "ambiguous" for row in inventory_rows
        ),
        "mismatch": sum(
            row["pdf_match_status"] == "mismatch" for row in inventory_rows
        ),
        "not_checked": sum(
            row["pdf_match_status"] == "not_checked" for row in inventory_rows
        ),
        "unexpected": len(unexpected),
        "unexpected_files": [
            path.relative_to(project_root).as_posix() for path in unexpected
        ],
        "multiple_candidates": sum(
            "multiple_pdf_candidates" in row["verification_flags"]
            for row in inventory_rows
        ),
    }
    return {
        "mapping": mapping,
        "inventory": inventory_rows,
        "missing": missing_rows,
        "metadata": metadata_rows,
        "stats": stats,
    }


def report_markdown(stats: dict[str, Any]) -> str:
    counts = stats["library_counts"]
    return f"""# PDF Inventory Report

Inventory date: {date.today().isoformat()}

## Literature Records

- Total: {stats['total_records']}
- A: {counts.get('A', 0)}
- B: {counts.get('B', 0)}
- C: {counts.get('C', 0)}
- D: {counts.get('D', 0)}

## PDF Availability

- Downloaded: {stats['downloaded']}
- Missing: {stats['missing']}
- Unexpected PDFs: {stats['unexpected']}

## PDF Readability and Identity

- Readable PDFs: {stats['readable']}
- Unreadable PDFs: {stats['unreadable']}
- Identity matched: {stats['matched']}
- Identity ambiguous / not fully verified: {stats['ambiguous']}
- Identity mismatch: {stats['mismatch']}
- Identity not checked because PDF is missing: {stats['not_checked']}
- Multiple PDF candidates: {stats['multiple_candidates']}

## Paper ID Mapping

- Assigned mappings: {stats['total_records']}
- Unique Paper IDs expected: {stats['total_records']}
- Mapping status: LOCKED
"""


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--project-root",
        type=Path,
        default=Path(__file__).resolve().parents[2],
        help="Project root; defaults to the repository root derived from this script.",
    )
    parser.add_argument(
        "--metadata-json",
        type=Path,
        default=None,
        help="Optional diagnostic metadata output outside the project data contract.",
    )
    args = parser.parse_args()
    project_root = args.project_root.resolve()
    result = scan(project_root)

    output_dir = project_root / "11_QC" / "missing_pdf"
    atomic_write_csv(
        output_dir / "pdf_inventory.csv", INVENTORY_FIELDS, result["inventory"]
    )
    atomic_write_csv(
        output_dir / "missing_pdfs.csv", MISSING_FIELDS, result["missing"]
    )
    atomic_write_text(
        output_dir / "pdf_inventory_report.md", report_markdown(result["stats"])
    )

    if args.metadata_json is not None:
        args.metadata_json.parent.mkdir(parents=True, exist_ok=True)
        atomic_write_text(
            args.metadata_json,
            json.dumps(result, ensure_ascii=False, indent=2) + "\n",
        )

    print(json.dumps(result["stats"], ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
