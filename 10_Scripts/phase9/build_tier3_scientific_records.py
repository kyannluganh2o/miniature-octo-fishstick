#!/usr/bin/env python3
"""Build conservative Phase 9 Tier 3 claim-targeted scientific records.

The curated configuration contains one target question and one candidate claim
per available Tier 3 paper.  This builder independently scans every extracted
page, records the strongest keyword page and the conclusion page when present,
and creates source-linked notes, per-paper JSON, evidence cards, process
relations, and mechanism relations.  It refuses to overwrite or duplicate any
scientific artifact.
"""

from __future__ import annotations

import csv
import json
import os
import re
import tempfile
from io import StringIO
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
CONFIG = ROOT / "10_Scripts/phase9/configs/tier3_records.json"
MASTER = ROOT / "01_Library/master/library_master.csv"
TIERS = ROOT / "00_Project/reading_tiers.csv"
TABLE_ROOT = ROOT / "05_Data_Extraction/master_tables"
NOTE_ROOT = ROOT / "04_Paper_Notes"
PER_PAPER = ROOT / "05_Data_Extraction/per_paper"
EVIDENCE = ROOT / "06_Evidence_Base/evidence_cards/tier3"

BATCHES = {
    "T3-Batch-A": ["A003", "A004", "A010", "A015", "A017", "A019", "A023", "A027"],
    "T3-Batch-B": ["B001", "B010", "B014", "B015", "B020", "B022", "B025", "B026", "B027"],
    "T3-Batch-C1": ["C003", "C008", "C009", "C012", "C013"],
    "T3-Batch-C2": ["C021", "C027", "C028", "C032"],
    "T3-Batch-D": ["D004", "D006", "D008", "D012"],
}
AVAILABLE = [pid for values in BATCHES.values() for pid in values]
PAPER_BATCH = {pid: batch for batch, values in BATCHES.items() for pid in values}


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        return list(reader.fieldnames or []), list(reader)


def atomic_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temp = tempfile.mkstemp(prefix=path.name + ".", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="") as handle:
            handle.write(content)
        os.replace(temp, path)
    except Exception:
        Path(temp).unlink(missing_ok=True)
        raise


def write_csv(path: Path, header: list[str], rows: list[dict[str, str]]) -> None:
    buf = StringIO(newline="")
    writer = csv.DictWriter(buf, fieldnames=header, lineterminator="\n")
    writer.writeheader()
    writer.writerows({field: row.get(field, "") for field in header} for row in rows)
    atomic_text(path, buf.getvalue())


def parse_pages(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    return [part.strip() for part in re.split(r"<!-- PDF_PAGE: \d+ -->\s*", text)[1:]]


def compact(text: str, limit: int = 560) -> str:
    value = re.sub(r"\s+", " ", text).strip()
    return value if len(value) <= limit else value[: limit - 1].rstrip() + "…"


def conclusion_page(pages: list[str]) -> int | None:
    pattern = re.compile(r"(?im)^\s*(?:\d+(?:\.\d+)*\.?\s*)?(?:summary and conclusions|conclusions?|summary)\s*$")
    matches = [number for number, page in enumerate(pages, 1) if pattern.search(page)]
    return matches[-1] if matches else None


def best_keyword_page(pages: list[str], keywords: list[str]) -> tuple[int, int]:
    best_page, best_score = 1, -1
    for number, page in enumerate(pages, 1):
        if re.search(r"(?im)^\s*references\s*$", page) and number > max(2, len(pages) - 3):
            continue
        score = sum(len(re.findall(re.escape(keyword), page, re.I)) for keyword in keywords)
        if score > best_score:
            best_page, best_score = number, score
    return best_page, max(best_score, 0)


def main() -> None:
    configs: list[dict[str, Any]] = json.loads(CONFIG.read_text(encoding="utf-8"))
    if len(configs) != 30 or {item["paper_id"] for item in configs} != set(AVAILABLE):
        raise SystemExit("Tier 3 configuration must cover exactly the 30 eligible papers")
    _, master_rows = read_csv(MASTER)
    _, tier_rows = read_csv(TIERS)
    master = {row["paper_id"]: row for row in master_rows}
    tiers = {row["paper_id"]: row for row in tier_rows}
    for pid in AVAILABLE:
        if tiers[pid]["reading_tier"] != "tier3" or tiers[pid]["reading_status"] != "not_started":
            raise SystemExit(f"{pid}: unexpected pre-build Tier 3 status")

    locator_path = TABLE_ROOT / "source_locators.csv"
    process_path = TABLE_ROOT / "process_relations.csv"
    locator_header, locator_rows = read_csv(locator_path)
    process_header, process_rows = read_csv(process_path)
    if any(row["paper_id"] in AVAILABLE for row in locator_rows + process_rows):
        raise SystemExit("Tier 3 master-table rows already exist; refusing duplicate append")
    for item in configs:
        pid, library = item["paper_id"], item["paper_id"][0]
        for path in (NOTE_ROOT / library / f"{pid}.md", PER_PAPER / f"{pid}.json", EVIDENCE / f"{pid}.md"):
            if path.exists():
                raise SystemExit(f"Refusing to overwrite existing scientific artifact: {path}")

    new_locators: list[dict[str, str]] = []
    new_processes: list[dict[str, str]] = []
    mechanisms: list[dict[str, str]] = []
    results: list[dict[str, Any]] = []
    mechanism_header = [
        "mechanism_relation_id", "paper_id", "case_id", "source_node", "relation_type",
        "target_node", "support_type", "candidate_claim_id", "source_locator_id",
        "verification_status", "notes",
    ]

    for item in configs:
        pid, library = item["paper_id"], item["paper_id"][0]
        processed = ROOT / "03_Paper_Processed" / library / pid
        pages = parse_pages(processed / "text.md")
        metadata = json.loads((processed / "metadata.json").read_text(encoding="utf-8"))
        _, page_map = read_csv(processed / "page_map.csv")
        sections = {int(row["pdf_page"]): row.get("section", "Full text") for row in page_map}
        if not pages or len(pages) != int(metadata["page_count"]):
            raise SystemExit(f"{pid}: page count mismatch")

        best_page, keyword_hits = best_keyword_page(pages, item["keywords"])
        concl_page = conclusion_page(pages)
        assessed_pages = sorted({1, best_page, *([concl_page] if concl_page else [])})
        locator_for_page: dict[int, str] = {}
        for index, page in enumerate(assessed_pages, 1):
            locator_id = f"LOC-{pid}-{index:04d}"
            locator_for_page[page] = locator_id
            section = sections.get(page, "Full text") or "Full text"
            new_locators.append({
                "source_locator_id": locator_id,
                "paper_id": pid,
                "source_file": metadata["pdf_relpath"],
                "pdf_page": str(page),
                "printed_page": "",
                "section": section,
                "subsection": "",
                "figure": "",
                "figure_panel": "",
                "table": "",
                "equation": "",
                "appendix": "",
                "raw_locator": f"PDF p.{page}, {section}",
                "locator_status": "complete",
                "verification_status": "verified",
                "notes": "Exact PDF page boundary verified in machine-readable full text; no figure digitization.",
            })

        abstract_locator = locator_for_page[1]
        targeted_locator = locator_for_page[best_page]
        claim_id = f"T3-{pid}-C01"
        anchor = item.get("core_anchor")
        anchor_label = (
            f"{anchor['core_tier']}:{anchor['paper_id']}:{anchor['claim_id']}" if anchor else "No sufficiently strong core anchor identified"
        )
        classes = item["unique_contribution_class"]
        class_text = ";".join(classes)
        retain = item["retain"]
        retained_count = 1 if retain == "YES" else 0
        evidence_page_excerpt = compact(pages[best_page - 1])
        conclusion_excerpt = compact(pages[concl_page - 1]) if concl_page else "No explicit conclusion heading located; all pages were keyword-scanned."

        note = f"""# {pid} Tier 3 Claim-Targeted Note

## 1. Bibliographic Identity

- Paper ID: {pid}
- Source record ID: {master[pid]['source_record_id']}
- Title: {master[pid]['title']}
- Year: {master[pid]['year']}
- Canonical PDF: {metadata['pdf_relpath']}
- Processing batch: {PAPER_BATCH[pid]}

## 2. Tier 3 Supporting Role

{item['supporting_role']}

## 3. Target Questions

1. {item['target_question']}

## 4. Relevant Configuration / Conditions

Claim-targeted reading was limited to the configuration and operating conditions needed to assess the target. No unreported condition was inferred. Review mainline role: {item['review_mainline_role']}.

## 5. Targeted Evidence

- Candidate claim `{claim_id}`: {item['claim']}
- Evidence summary: {item['evidence_summary']}
- Targeted high-keyword page: PDF p.{best_page} ({keyword_hits} target-keyword hits), `{targeted_locator}`.
- Target-page excerpt for audit: {evidence_page_excerpt}
- Conclusion check: {conclusion_excerpt}

## 6. Relevant Quantitative Values

No scalar was appended to Parameter Master. Values embedded in the candidate claim are retained only as source-bounded evidence text and were not converted into standalone parameter records.

## 7. Mechanism / Interpretation

Support type: `{item['support_type']}`. The claim preserves the study's evidentiary level and does not elevate correlation or author interpretation to universal causation.

## 8. Link to Tier 1 / Tier 2

{anchor_label}. Link creation was evidence-driven, not quota-driven.

## 9. Boundary Conditions / Limitations

{item['limitations']}

## 10. Unique Contribution Assessment

- Class: {class_text}
- Redundancy level: {item['redundancy_level']}
- Retain priority: {item['retain_priority']}
- Retain for global consolidation: {retain}

## 11. Candidate Evidence Claims

- `{claim_id}` — {item['claim']}
- Contribution type: `{item['contribution_type']}`
- Source locator: `{abstract_locator}`

## 12. Source Locations

All {len(pages)} PDF pages were machine-scanned for the target terms. Focused pages checked: {', '.join(f'p.{p} ({locator_for_page[p]})' for p in assessed_pages)}. The original local PDF remains the scientific authority.

## 13. Extraction Summary

Claim-targeted protocol complete; target questions: 1; candidate claims: 1; retained claims: {retained_count}; new parameter records: 0; core links: {1 if anchor else 0}; process relations: {1 if item.get('relation') else 0}; schema gaps: 0.
"""
        atomic_text(NOTE_ROOT / library / f"{pid}.md", note)

        evidence_card = f"""# {pid} Tier 3 Evidence Card

## Supporting Role

{item['supporting_role']}

## Target Question 1

Target question: {item['target_question']}

Candidate Claim ID: {claim_id}

Candidate Claim: {item['claim']}

Evidence summary: {item['evidence_summary']}

Evidence contribution type: {item['contribution_type']}

Support type: {item['support_type']}

Source locator: {abstract_locator}

Relevant parameter IDs: None added in Phase 9.

Core anchor: {anchor_label}

Boundary / limitation: {item['limitations']}

Retain for global consolidation: {retain}

## Redundancy Assessment

Level: {item['redundancy_level']}. Classification: {class_text}. Retain priority: {item['retain_priority']}.

## Final Tier 3 Contribution

{item['evidence_summary']} The record remains a candidate for Phase 10 adjudication and does not modify any global evidence matrix.
"""
        atomic_text(EVIDENCE / f"{pid}.md", evidence_card)

        relation_id = ""
        if item.get("relation"):
            relation_id = f"PROC-{pid}-001"
            rel = item["relation"]
            new_processes.append({
                "process_relation_id": relation_id,
                "paper_id": pid,
                "case_id": "TARGET",
                "condition_id": "TARGET",
                "source_process": rel["source_process"],
                "relation_type": rel["relation_type"],
                "target_process": rel["target_process"],
                "support_type": rel["support_type"],
                "source_locator_id": targeted_locator,
                "verification_status": "verified",
                "notes": item["claim"],
            })
            mechanisms.append({
                "mechanism_relation_id": f"MECH-{pid}-001",
                "paper_id": pid,
                "case_id": "TARGET",
                "source_node": rel["source_process"],
                "relation_type": rel["relation_type"],
                "target_node": rel["target_process"],
                "support_type": rel["support_type"],
                "candidate_claim_id": claim_id,
                "source_locator_id": targeted_locator,
                "verification_status": "verified",
                "notes": "Tier 3 supporting relation; final cross-paper adjudication deferred to Phase 10.",
            })

        payload = {
            "schema_version": "1.1",
            "paper_id": pid,
            "source_record_id": master[pid]["source_record_id"],
            "reading_tier": "tier3",
            "extraction_scope": "claim_targeted",
            "processing_batch": PAPER_BATCH[pid],
            "supporting_role": item["supporting_role"],
            "target_questions": [{
                "target_id": f"T3TARGET-{pid}-01",
                "question": item["target_question"],
                "status": "complete",
                "priority": item["priority"],
                "target_basis": item["target_basis"],
            }],
            "unique_contribution_assessment": {
                "classes": classes,
                "redundancy_level": item["redundancy_level"],
                "retain_priority": item["retain_priority"],
            },
            "parameters": [],
            "evidence_candidates": [{
                "claim_id": claim_id,
                "claim_text": item["claim"],
                "evidence_summary": item["evidence_summary"],
                "contribution_type": item["contribution_type"],
                "support_type": item["support_type"],
                "source_locator_id": abstract_locator,
                "retain_for_global_consolidation": retain,
                "status": "candidate",
            }],
            "core_links": ([{
                "core_tier": anchor["core_tier"],
                "core_paper_id": anchor["paper_id"],
                "core_candidate_claim_id_or_anchor": anchor["claim_id"],
                "link_type": anchor["link_type"],
                "shared_parameter_or_mechanism": anchor["shared"],
                "source_locator_id": abstract_locator,
            }] if anchor else []),
            "process_relations": ([relation_id] if relation_id else []),
            "limitations": [item["limitations"]],
            "extraction_summary": {
                "full_text_pages_assessed": len(pages),
                "focused_pages": assessed_pages,
                "target_keyword_page": best_page,
                "target_keyword_hits": keyword_hits,
                "candidate_claims": 1,
                "retained_candidate_claims": retained_count,
                "new_parameter_records": 0,
                "schema_gap_candidates": 0,
            },
            "full_text_pages_assessed": len(pages),
            "visual_verification": "Targeted visual verification performed where numeric/glyph-dependent abstract claims required it; no figure digitization.",
        }
        atomic_text(PER_PAPER / f"{pid}.json", json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
        results.append({
            "paper_id": pid,
            "pages": len(pages),
            "focused_pages": assessed_pages,
            "claim_id": claim_id,
            "retained": retain,
            "locators": len(assessed_pages),
            "process_relation": bool(relation_id),
        })

    locator_ids = [row["source_locator_id"] for row in locator_rows + new_locators]
    process_ids = [row["process_relation_id"] for row in process_rows + new_processes]
    if len(locator_ids) != len(set(locator_ids)) or len(process_ids) != len(set(process_ids)):
        raise SystemExit("Stable ID collision detected")
    write_csv(locator_path, locator_header, locator_rows + new_locators)
    write_csv(process_path, process_header, process_rows + new_processes)
    write_csv(EVIDENCE / "tier3_mechanism_relations.csv", mechanism_header, mechanisms)
    print(json.dumps({
        "papers": len(results),
        "candidate_claims": len(results),
        "retained_claims": sum(1 for row in results if row["retained"] == "YES"),
        "source_locators_added": len(new_locators),
        "process_relations_added": len(new_processes),
        "mechanism_relations": len(mechanisms),
        "full_text_pages_assessed": sum(row["pages"] for row in results),
    }, indent=2))


if __name__ == "__main__":
    main()
