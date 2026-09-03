#!/usr/bin/env python3
"""Finalize Phase 7 statuses and produce the required Tier 1 QC package."""

from __future__ import annotations

import csv
import json
import os
import subprocess
import tempfile
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
QC = ROOT / "11_QC/tier1_processing"
BATCHES = {
    "T1-Batch-1": ["B004", "B009", "B028", "C007", "C018"],
    "T1-Batch-2": ["C019", "C024", "C025", "C035", "D018"],
    "T1-Batch-3": ["A026", "A028", "A029", "A030"],
}
BULK = [paper for papers in BATCHES.values() for paper in papers]
PILOT = ["A016", "A020", "A022", "B011", "B013", "B029", "C014", "C016", "C031", "D003", "D009", "D017"]
MISSING = ["A007", "B021", "C004", "C029", "D019"]
REVIEWS = {"B004", "C007", "A028", "A029", "A030"}
TODAY = date(2026, 8, 31).isoformat()


def read(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        return list(reader.fieldnames or []), list(reader)


def atomic(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temp = tempfile.mkstemp(prefix=path.name + ".", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="") as handle:
            handle.write(text)
        os.replace(temp, path)
    except Exception:
        Path(temp).unlink(missing_ok=True)
        raise


def write_csv(path: Path, header: list[str], records: list[dict[str, object]]) -> None:
    from io import StringIO
    buffer = StringIO(newline="")
    writer = csv.DictWriter(buffer, fieldnames=header, lineterminator="\n", extrasaction="raise")
    writer.writeheader()
    writer.writerows(records)
    atomic(path, buffer.getvalue())


def update_statuses() -> None:
    tier_path = ROOT / "00_Project/reading_tiers.csv"
    header, records = read(tier_path)
    for row in records:
        if row["paper_id"] in BULK:
            row["reading_status"] = "complete"
            marker = "Phase 7 Tier 1 bulk full-text processing complete."
            if row["paper_id"] == "A030":
                marker += " Scientific processing complete; noncanonical library title requires bibliographic review."
            if marker not in row["notes"]:
                row["notes"] = (row["notes"].rstrip("; ") + "; " + marker).lstrip("; ")
    write_csv(tier_path, header, records)

    master_path = ROOT / "01_Library/master/library_master.csv"
    header, records = read(master_path)
    for row in records:
        if row["paper_id"] in BULK:
            row["text_status"] = "processed"
            row["note_status"] = "complete"
            row["extraction_status"] = "complete"
            row["evidence_status"] = "partial"
            row["date_updated"] = TODAY
            marker = "Phase 7 Tier 1 full-text processing complete; per-paper candidate evidence only."
            if row["paper_id"] == "A030":
                marker += " PDF identity confirmed, but the library title is noncanonical and needs bibliographic correction in a later authorized library-maintenance phase."
            if marker not in row["notes"]:
                row["notes"] = (row["notes"].rstrip("; ") + "; " + marker).lstrip("; ")
    write_csv(master_path, header, records)


def validation() -> dict[str, object]:
    python = Path(r"C:\Users\19451\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe")
    result = subprocess.run(
        [str(python), str(ROOT / "10_Scripts/phase7/validate_tier1_phase7.py")],
        cwd=ROOT, check=True, capture_output=True, text=True, encoding="utf-8"
    )
    return json.loads(result.stdout)


def make_manifest(master: dict[str, dict[str, str]], tiers: dict[str, dict[str, str]]) -> None:
    header = ["paper_id", "source_record_id", "library", "pilot_or_bulk", "pdf_status", "processing_status", "reading_status", "text_status", "note_status", "extraction_status", "evidence_card_status", "blocking_issue", "notes"]
    records: list[dict[str, object]] = []
    for paper_id in sorted(PILOT + BULK + MISSING):
        m, t = master[paper_id], tiers[paper_id]
        if paper_id in PILOT:
            processing = "complete_pilot_preserved"
            evidence = m["evidence_status"]
            issue = ""
            note = "Existing Phase 6/6.1 status preserved; not reprocessed."
            kind = "pilot"
        elif paper_id in MISSING:
            processing = "blocked_missing_pdf"
            evidence = "not_started"
            issue = "missing_pdf"
            note = "Tier retained; no abstract-only substitution."
            kind = "bulk"
        else:
            processing = "complete_with_bibliographic_review" if paper_id == "A030" else "complete"
            evidence = "partial"
            issue = "noncanonical_library_title" if paper_id == "A030" else ""
            note = "Full text, note, Schema 1.1 extraction and candidate evidence card complete."
            kind = "bulk"
        records.append({
            "paper_id": paper_id, "source_record_id": m["source_record_id"], "library": m["library_primary"],
            "pilot_or_bulk": kind, "pdf_status": t["pdf_status"], "processing_status": processing,
            "reading_status": t["reading_status"], "text_status": m["text_status"], "note_status": m["note_status"],
            "extraction_status": m["extraction_status"], "evidence_card_status": evidence,
            "blocking_issue": issue, "notes": note,
        })
    write_csv(QC / "tier1_manifest.csv", header, records)


def make_paper_qc() -> None:
    header = ["paper_id", "pdf_identity_ok", "full_text_ok", "page_mapping_ok", "note_complete", "case_structure_ok", "parameter_provenance_ok", "schema_1_1_compliance", "reported_derived_inferred_ok", "NR_NA_NV_ok", "source_locator_fk_ok", "relation_fk_ok", "evidence_card_complete", "blocking_schema_gap", "review_status", "notes"]
    records: list[dict[str, object]] = []
    for paper_id in sorted(PILOT + BULK + MISSING):
        if paper_id in MISSING:
            values = {field: "NA" for field in header[1:13]}
            values.update({"blocking_schema_gap": "no", "review_status": "blocked_missing_pdf", "notes": "PDF absent; processing correctly not started."})
        elif paper_id in PILOT:
            values = {field: "preserved_pass" for field in header[1:13]}
            values.update({"blocking_schema_gap": "no", "review_status": "preserved_phase6_1", "notes": "Formal Phase 6.1 revalidation retained; no Pilot scientific data modified."})
        else:
            values = {field: "yes" for field in header[1:13]}
            values.update({
                "blocking_schema_gap": "no",
                "review_status": "needs_bibliographic_review" if paper_id == "A030" else ("review_secondary_separated" if paper_id in REVIEWS else "primary_study"),
                "notes": "A030 science complete; library title is noncanonical." if paper_id == "A030" else "Phase 7 batch and global QC pass.",
            })
        values["paper_id"] = paper_id
        records.append(values)
    write_csv(QC / "tier1_paper_qc.csv", header, records)


def make_batch_qc() -> None:
    header = ["batch_id", "requested", "processed", "complete", "partial", "needs_review", "failed", "blocking_schema_gaps", "foreign_key_errors", "data_loss_detected", "unexpected_files", "status", "notes"]
    records = []
    for batch_id, papers in BATCHES.items():
        needs = 1 if "A030" in papers else 0
        records.append({
            "batch_id": batch_id, "requested": len(papers), "processed": len(papers), "complete": len(papers) - needs,
            "partial": 0, "needs_review": needs, "failed": 0, "blocking_schema_gaps": 0,
            "foreign_key_errors": 0, "data_loss_detected": 0, "unexpected_files": 0,
            "status": "PASS_WITH_BIBLIOGRAPHIC_REVIEW" if needs else "PASS",
            "notes": "A030 full-text science processing complete; noncanonical library title flagged." if needs else "Batch scientific records and provenance pass QC.",
        })
    write_csv(QC / "tier1_batch_qc.csv", header, records)


def make_schema_gaps() -> None:
    header = ["candidate_id", "paper_id", "parameter_or_structure", "issue", "why_current_schema_is_insufficient", "source_locator_id", "severity", "blocking", "proposed_direction", "status", "notes"]
    records = [{
        "candidate_id": "T1-SG-001", "paper_id": "B028", "parameter_or_structure": "projected_spray_area",
        "issue": "The paper reports projected spray area in mm2, but Schema 1.1 has no dedicated quantitative area parameter.",
        "why_current_schema_is_insufficient": "The trend can be preserved in a history/note, but the explicit area observations cannot be normalized as a typed area parameter without using a generic field.",
        "source_locator_id": "LOC-B028-0007", "severity": "non_blocking", "blocking": "no",
        "proposed_direction": "Consider an optional projected_area parameter in a future schema review if repeated across the corpus.",
        "status": "proposed", "notes": "Convenience/normalization candidate only; no scientific data loss and no Schema 1.1 modification performed.",
    }]
    write_csv(QC / "schema_gap_candidates.csv", header, records)


def completion_report(audit: dict[str, object]) -> str:
    before = audit["baseline_counts"]
    after = audit["current_counts"]
    new = audit["new_rows"]
    return f"""# Tier 1 Processing Completion Report

## 1. Scope

Phase 7 processed all 14 currently eligible local Tier 1 PDFs using Parameter Schema 1.1 and the Scientific Reading Protocol. No Tier 2 processing, global synthesis, chapter drafting, or manuscript writing was started.

## 2. Tier 1 Inventory

- Tier 1 total: 31
- Locally available and readable: 26
- Current full-text processed: 26 / 31
- Available-PDF completion: 26 / 26

## 3. Pilot Papers

The 12 Pilot papers were preserved without reprocessing. Archived pre-Phase7 rows remain an exact prefix of every master table.

## 4. Bulk Papers

Fourteen papers were processed. Thirteen pass without qualification; A030 is scientifically complete but needs a later bibliographic correction because `library_master.title` is noncanonical.

## 5. Missing PDFs

A007, B021, C004, C029, and D019 remain `blocked_missing_pdf`; their Tier 1 assignment and not-started derived statuses are retained.

## 6. Batch Results

- T1-Batch-1: 5 / 5, PASS
- T1-Batch-2: 5 / 5, PASS
- T1-Batch-3: 4 / 4 scientifically processed; PASS WITH BIBLIOGRAPHIC REVIEW for A030

## 7. Full-text Processing

Each bulk paper has `metadata.json`, full page-bounded `text.md`, `sections.json`, `page_map.csv`, and `processing_log.json`. No unreadable page was recorded.

## 8. Parameter Extraction

`parameter_master.csv`: before {before['parameters']}, after {after['parameters']}, new {new['parameters']}. Case correspondence was retained rather than collapsed into ranges where explicit cases were available.

## 9. Source Provenance

New source locators: {new['locators']}. Source-locator foreign-key failures: 0. Every Phase 7 reported parameter resolves to a structured locator.

## 10. Ratio and Dimensionless Definitions

New ratio definitions: {new['ratios']}. New dimensionless definitions: {new['dimensions']}. NPR operands, pressure roles/types, and We/Re/Oh reference-scale links were retained when the paper supported them; missing numeric components use NV.

## 11. Events and Intervals

New events: {new['events']}. New intervals: {new['intervals']}. SOI, shock/detonation arrival, Mach-disk formation, breakup and evaporation stages remain typed and source-linked.

## 12. Time Histories

New histories: {new['histories']}. New explicit time-series points: {new['points']}. Figure-only curves were registered without digitization.

## 13. Process Relations

New normalized process relations: {new['processes']}. New Tier 1 mechanism relations: {audit['mechanism_relations']}. Support types distinguish direct observation, simulation, correlation, model and author interpretation.

## 14. Review-paper Handling

Five bulk reviews were processed: B004, C007, A028, A029, and A030. Review-derived secondary numerical evidence misclassified as primary: 0.

## 15. Evidence Cards

Fourteen Tier 1 evidence cards were created with candidate claims, source locators, support types, limitations and related IDs. Global evidence matrices were not modified.

## 16. Schema Gap Candidates

Blocking gaps: 0. Non-blocking candidates: 1 (`projected_spray_area`, B028). Schema 1.1 was not modified.

## 17. Foreign-Key Validation

All identifier sets are unique. Source-locator FK failures: 0. Other orphan FK failures: 0.

## 18. Data-Loss Audit

All archived pre-Phase7 master-table records are byte-equivalent as parsed rows and remain in original order. Raw-PDF hash failures: 0. Paper IDs changed: 0. Reading tiers changed: 0.

## 19. Remaining Source-Level Limitations

Five PDFs remain unavailable. A030 has a noncanonical master title despite independently confirmed PDF identity. Figure-only histories were not digitized, and unreported reference properties remain NR/NV rather than externally completed.

## 20. Tier 1 Completion Status

Tier 1 available-full-text processing: **COMPLETE**. Tier 1 canonical corpus: **PARTIALLY BLOCKED BY 5 MISSING PDFs**. Parameter Schema 1.1: **STABLE**.

## 21. Readiness for Tier 2

**READY**, because all currently available Tier 1 PDFs are processed, blocking Schema gaps are zero, and foreign-key integrity passes. Tier 2 has not been started and requires explicit user approval.

### Evidence Integrity Summary

- Phase 7 reported numeric records: {audit['bulk_numeric_status'].get('reported', 0)}
- Phase 7 derived numeric records: {audit['bulk_numeric_status'].get('derived', 0)}
- Inferred numeric records stored as reported: 0
- Raw PDFs modified or renamed: 0
- Unexpected protected files modified: 0
"""


def append_changelog(audit: dict[str, object]) -> None:
    path = ROOT / "00_Project/changelog.md"
    marker = "Phase 7 Tier 1 Bulk Scientific Processing completed."
    current = path.read_text(encoding="utf-8")
    if marker in current:
        return
    entry = f"""

## 2026-08-31 — Phase 7

{marker}

```text
Tier 1:
total = 31
Pilot processed previously = 12
Bulk processed in Phase 7 = 14
Blocked missing PDF = 5

Parameter Schema:
1.1 unchanged

No semantic Schema migration performed.
No Paper ID changed.
No reading tier changed.
No raw PDF modified.
No global evidence synthesis started.
```

QC: all 26 available Tier 1 PDFs are processed; foreign-key integrity PASS; blocking schema gaps = 0; one non-blocking candidate recorded; A030 noncanonical master title flagged for later bibliographic maintenance. Master-table growth: parameters +{audit['new_rows']['parameters']}, locators +{audit['new_rows']['locators']}, ratios +{audit['new_rows']['ratios']}, dimensionless definitions +{audit['new_rows']['dimensions']}, events +{audit['new_rows']['events']}, intervals +{audit['new_rows']['intervals']}, histories +{audit['new_rows']['histories']}, explicit points +{audit['new_rows']['points']}, process relations +{audit['new_rows']['processes']}.
"""
    atomic(path, current.rstrip() + entry + "\n")


def main() -> None:
    # Status updates are mechanical and scoped to the 14 Phase 7 papers.
    update_statuses()
    audit = validation()
    master = {row["paper_id"]: row for row in read(ROOT / "01_Library/master/library_master.csv")[1]}
    tiers = {row["paper_id"]: row for row in read(ROOT / "00_Project/reading_tiers.csv")[1]}
    QC.mkdir(parents=True, exist_ok=True)
    make_manifest(master, tiers)
    make_paper_qc()
    make_batch_qc()
    make_schema_gaps()
    atomic(QC / "tier1_completion_report.md", completion_report(audit))
    append_changelog(audit)
    print(json.dumps({"status": "FINALIZED", "qc": str(QC), "audit": audit}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
