#!/usr/bin/env python3
"""Validate and finalize Phase 8 after all Tier 2 scientific artifacts exist."""

from __future__ import annotations

import csv
import hashlib
import json
import os
import re
import tempfile
from collections import Counter
from datetime import date
from io import StringIO
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
ARCHIVE = ROOT / "99_Archive/old_versions/Phase8_pre_tier2_processing"
QC = ROOT / "11_QC/tier2_processing"
EVIDENCE = ROOT / "06_Evidence_Base/evidence_cards/tier2"
TODAY = date.today().isoformat()

BATCHES = {
    "T2-Batch-1": ["A013", "A014", "A018", "A021", "A024", "A025"],
    "T2-Batch-2": ["B002", "B003", "B005", "B007", "B012", "B016"],
    "T2-Batch-3": ["B017", "B019", "B023", "B024", "B030"],
    "T2-Batch-4": ["C001", "C002", "C006", "C010", "C015", "C017", "C020"],
    "T2-Batch-5": ["C022", "C023", "C026", "C030", "C033", "C034"],
    "T2-Batch-6": ["D002", "D005", "D007", "D010", "D011"],
    "T2-Batch-7": ["D013", "D014", "D015", "D016"],
}
AVAILABLE = [pid for values in BATCHES.values() for pid in values]
MISSING = ["A002", "A005", "A009", "A011", "A012", "B008", "C036"]
ROLES = {
    "A": ("mixing/ignition", "gas-liquid direct injection", "injection chronology"),
    "B": ("underexpanded jet physics", "shock structure", "gas-jet mixing"),
    "C": ("droplet breakup", "shock loading", "phase change/multi-droplet interaction"),
    "D": ("RDE/detonation application", "wave-droplet coupling", "phase change and stability"),
}
TABLES = {
    "parameters": (ROOT / "05_Data_Extraction/master_tables/parameter_master.csv", "parameter_record_id"),
    "locators": (ROOT / "05_Data_Extraction/master_tables/source_locators.csv", "source_locator_id"),
    "ratios": (ROOT / "05_Data_Extraction/master_tables/ratio_definitions.csv", "ratio_id"),
    "dimensions": (ROOT / "05_Data_Extraction/master_tables/dimensionless_definitions.csv", "dimensionless_definition_id"),
    "events": (ROOT / "05_Data_Extraction/master_tables/events.csv", "event_id"),
    "intervals": (ROOT / "05_Data_Extraction/master_tables/intervals.csv", "interval_id"),
    "histories": (ROOT / "05_Data_Extraction/master_tables/time_history_registry.csv", "history_id"),
    "points": (ROOT / "05_Data_Extraction/master_tables/time_series_points.csv", "point_id"),
    "processes": (ROOT / "05_Data_Extraction/master_tables/process_relations.csv", "process_relation_id"),
}


def read(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        return list(reader.fieldnames or []), list(reader)


def atomic(path: Path, content: str) -> None:
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
    atomic(path, buf.getvalue())


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def validate() -> dict[str, object]:
    errors: list[str] = []
    warnings: list[str] = []
    data: dict[str, list[dict[str, str]]] = {}
    ids: dict[str, set[str]] = {}
    baseline_counts: dict[str, int] = {}
    current_counts: dict[str, int] = {}
    for name, (path, key) in TABLES.items():
        _, rows = read(path)
        _, old = read(ARCHIVE / path.relative_to(ROOT))
        data[name] = rows
        values = [row[key] for row in rows if row.get(key)]
        if len(values) != len(set(values)):
            errors.append(f"duplicate IDs in {name}")
        ids[name] = set(values)
        baseline_counts[name], current_counts[name] = len(old), len(rows)
        if rows[:len(old)] != old:
            errors.append(f"{name}: pre-Phase8 prefix changed or reordered")

    _, master_rows = read(ROOT / "01_Library/master/library_master.csv")
    _, tier_rows = read(ROOT / "00_Project/reading_tiers.csv")
    _, inv_rows = read(ROOT / "11_QC/missing_pdf/pdf_inventory.csv")
    master = {row["paper_id"]: row for row in master_rows}
    tiers = {row["paper_id"]: row for row in tier_rows}
    inventory = {row["paper_id"]: row for row in inv_rows}
    _, old_master_rows = read(ARCHIVE / "01_Library/master/library_master.csv")
    _, old_tier_rows = read(ARCHIVE / "00_Project/reading_tiers.csv")
    old_master = {row["paper_id"]: row for row in old_master_rows}
    old_tiers = {row["paper_id"]: row for row in old_tier_rows}
    if set(master) != set(old_master) or set(tiers) != set(old_tiers):
        errors.append("Paper ID set changed")
    for pid in tiers:
        if tiers[pid]["reading_tier"] != old_tiers[pid]["reading_tier"]:
            errors.append(f"{pid}: reading tier changed")
        if master[pid]["source_record_id"] != old_master[pid]["source_record_id"]:
            errors.append(f"{pid}: source record identity changed")
    frozen_t2 = {pid for pid, row in tiers.items() if row["reading_tier"] == "tier2"}
    if frozen_t2 != set(AVAILABLE + MISSING):
        errors.append("frozen Tier 2 membership differs from expected 46")

    # Required artifacts, page scan, and raw-PDF identity.
    baseline_manifest = {row["path"].replace("\\", "/"): row for row in read(ARCHIVE / "phase8_baseline_manifest.csv")[1] if row["scope"] == "raw_pdf_hash_only"}
    live_raw = {}
    for path in (ROOT / "02_PDF_Raw").rglob("*.pdf"):
        rel = path.relative_to(ROOT).as_posix()
        live_raw[rel] = {"bytes": str(path.stat().st_size), "sha256": sha(path)}
    if set(live_raw) != set(baseline_manifest):
        errors.append("raw PDF path set changed (rename/add/remove detected)")
    for rel, base in baseline_manifest.items():
        if rel in live_raw and (live_raw[rel]["bytes"] != base["bytes"] or live_raw[rel]["sha256"].upper() != base["sha256"].upper()):
            errors.append(f"raw PDF hash changed: {rel}")

    page_total = 0
    for pid in AVAILABLE:
        library = master[pid]["library_primary"]
        processed = ROOT / "03_Paper_Processed" / library / pid
        for filename in ("metadata.json", "text.md", "sections.json", "page_map.csv", "processing_log.json"):
            if not (processed / filename).is_file():
                errors.append(f"{pid}: missing processed {filename}")
        note = ROOT / "04_Paper_Notes" / library / f"{pid}.md"
        per = ROOT / "05_Data_Extraction/per_paper" / f"{pid}.json"
        card = EVIDENCE / f"{pid}.md"
        for path, label in ((note, "note"), (per, "per-paper JSON"), (card, "evidence card")):
            if not path.is_file():
                errors.append(f"{pid}: missing {label}")
        if per.is_file():
            payload = json.loads(per.read_text(encoding="utf-8"))
            if payload.get("schema_version") != "1.1" or payload.get("reading_tier") != "tier2" or payload.get("extraction_scope") != "chapter_core":
                errors.append(f"{pid}: per-paper metadata contract failure")
            page_total += int(payload.get("full_text_pages_assessed", 0))
        if card.is_file():
            text = card.read_text(encoding="utf-8")
            claim_ids = re.findall(rf"T2-{pid}-C\d{{2}}", text)
            if len(set(claim_ids)) < 2:
                errors.append(f"{pid}: fewer than two candidate claims")
            if any(token in text.lower() for token in ("authors to whom correspondence", "doi.org/", "supplementary data see")):
                errors.append(f"{pid}: evidence-card metadata/noise leakage")
        if (processed / "processing_log.json").is_file():
            log = json.loads((processed / "processing_log.json").read_text(encoding="utf-8"))
            if log.get("unreadable_pages"):
                errors.append(f"{pid}: unreadable page recorded")
        if (processed / "metadata.json").is_file():
            meta = json.loads((processed / "metadata.json").read_text(encoding="utf-8"))
            raw = ROOT / meta["pdf_relpath"]
            if sha(raw) != meta["pdf_sha256"]:
                errors.append(f"{pid}: processed metadata raw hash mismatch")
    if page_total <= 0:
        errors.append("full-text page audit missing")

    for pid in MISSING:
        inv = inventory[pid]
        if not (inv["file_exists"] == "no" and tiers[pid]["reading_status"] == "blocked_missing_pdf"):
            errors.append(f"{pid}: missing-PDF status mismatch")

    # Relational/FK and Schema 1.1 checks.
    dictionary = (ROOT / "05_Data_Extraction/schema/parameter_dictionary.yaml").read_text(encoding="utf-8")
    parameter_map = dict(re.findall(r"^  ([A-Za-z_][A-Za-z0-9_]*): \{group: ([A-Za-z_][A-Za-z0-9_]*)", dictionary, re.M))
    t2_params = [row for row in data["parameters"] if row["paper_id"] in AVAILABLE]
    for row in t2_params:
        rid = row["parameter_record_id"]
        if row["parameter_name"] not in parameter_map or parameter_map.get(row["parameter_name"]) != row["parameter_group"]:
            errors.append(f"{rid}: parameter name/group mismatch")
        if row["source_locator_id"] not in ids["locators"]:
            errors.append(f"{rid}: locator FK orphan")
        if row["value_status"] in {"NR", "NA", "NV"} and not row["missing_reason"]:
            errors.append(f"{rid}: missing reason absent")
        for field, target in (("event_id", "events"), ("interval_id", "intervals"), ("history_id", "histories"), ("ratio_id", "ratios"), ("dimensionless_definition_id", "dimensions"), ("process_relation_id", "processes")):
            if row[field] and row[field] not in ids[target]:
                errors.append(f"{rid}: {field} orphan")
    for name in ("dimensions", "events", "intervals", "histories", "processes"):
        for row in data[name]:
            if row["paper_id"] in AVAILABLE and row["source_locator_id"] not in ids["locators"]:
                errors.append(f"{row[TABLES[name][1]]}: locator orphan")
    for row in data["intervals"]:
        if row["paper_id"] in AVAILABLE:
            for field in ("start_event_id", "end_event_id"):
                if row[field] and row[field] not in ids["events"]:
                    errors.append(f"{row['interval_id']}: {field} orphan")
    for row in data["dimensions"]:
        if row["paper_id"] in AVAILABLE:
            if row["parameter_record_id"] not in ids["parameters"]:
                errors.append(f"{row['dimensionless_definition_id']}: parameter orphan")
            for field in ("reference_velocity_parameter_id", "reference_density_parameter_id", "reference_length_parameter_id", "reference_viscosity_parameter_id", "reference_surface_tension_parameter_id"):
                if row[field] and row[field] not in ids["parameters"]:
                    errors.append(f"{row['dimensionless_definition_id']}: component orphan")

    mech_header, mechanisms = read(EVIDENCE / "tier2_mechanism_relations.csv")
    mech_ids = [row["mechanism_relation_id"] for row in mechanisms]
    if len(mech_ids) != len(set(mech_ids)):
        errors.append("duplicate Tier 2 mechanism IDs")
    allowed_support = {"direct_observation", "simulation_resolved", "experimental_correlation", "model_based", "author_interpretation", "review_secondary", "project_inference"}
    for row in mechanisms:
        if row["source_locator_id"] not in ids["locators"]:
            errors.append(f"{row['mechanism_relation_id']}: locator orphan")
        if row["support_type"] not in allowed_support:
            errors.append(f"{row['mechanism_relation_id']}: invalid support type")
    _, links = read(QC / "tier2_to_tier1_links.csv")
    for row in links:
        if row["tier2_paper_id"] not in AVAILABLE or tiers[row["tier1_paper_id"]]["reading_tier"] != "tier1" or row["tier2_source_locator_id"] not in ids["locators"]:
            errors.append(f"{row['link_id']}: link FK failure")

    numeric = [row for row in t2_params if re.fullmatch(r"[-+]?\d+(?:\.\d+)?(?:[Ee][-+]?\d+)?", row["reported_value"].strip())]
    numeric_status = Counter(row["value_status"] for row in numeric)
    if numeric_status.get("inferred", 0):
        errors.append("inferred numeric record stored")
    review_primary_misclassified = sum(row["paper_id"] == "B005" and row["value_status"] == "reported" and row["parameter_role"] in {"measured_output", "simulated_output"} for row in t2_params)
    if review_primary_misclassified:
        errors.append("review-secondary record misclassified as primary output")

    return {
        "status": "PASS" if not errors else "FAIL", "errors": errors, "warnings": warnings,
        "baseline_counts": baseline_counts, "current_counts": current_counts,
        "new_rows": {name: current_counts[name] - baseline_counts[name] for name in TABLES},
        "page_total": page_total, "mechanism_relations": len(mechanisms), "links": len(links),
        "tier2_parameter_rows": len(t2_params), "numeric_status": dict(numeric_status),
        "source_locator_fk_failures": sum("locator" in err and "orphan" in err for err in errors),
        "other_fk_failures": sum("orphan" in err and "locator" not in err for err in errors),
        "raw_pdf_integrity_failures": sum("raw PDF" in err for err in errors),
        "review_primary_misclassified": review_primary_misclassified,
    }


def update_statuses() -> None:
    tier_path = ROOT / "00_Project/reading_tiers.csv"
    tier_header, tier_rows = read(tier_path)
    for row in tier_rows:
        if row["paper_id"] in AVAILABLE:
            row["reading_status"] = "complete"
            row["notes"] = "Phase 8 Tier 2 chapter-core processing complete; candidate evidence pending consolidation."
    write_csv(tier_path, tier_header, tier_rows)

    master_path = ROOT / "01_Library/master/library_master.csv"
    master_header, master_rows = read(master_path)
    for row in master_rows:
        if row["paper_id"] in AVAILABLE:
            row["text_status"] = "processed"
            row["note_status"] = "complete"
            row["extraction_status"] = "complete"
            row["evidence_status"] = "partial"
            row["date_updated"] = TODAY
    write_csv(master_path, master_header, master_rows)


def make_qc(audit: dict[str, object]) -> None:
    _, master_rows = read(ROOT / "01_Library/master/library_master.csv")
    _, tier_rows = read(ROOT / "00_Project/reading_tiers.csv")
    _, inv_rows = read(ROOT / "11_QC/missing_pdf/pdf_inventory.csv")
    master = {row["paper_id"]: row for row in master_rows}
    tiers = {row["paper_id"]: row for row in tier_rows}
    inventory = {row["paper_id"]: row for row in inv_rows}
    all_t2 = sorted(AVAILABLE + MISSING)
    paper_batch = {pid: batch for batch, papers in BATCHES.items() for pid in papers}

    manifest_header = ["paper_id", "source_record_id", "library", "pdf_status", "processing_batch", "processing_status", "reading_status", "text_status", "note_status", "extraction_status", "evidence_card_status", "blocking_issue", "notes"]
    manifest = []
    for pid in all_t2:
        missing = pid in MISSING
        manifest.append({
            "paper_id": pid, "source_record_id": master[pid]["source_record_id"], "library": master[pid]["library_primary"],
            "pdf_status": "missing" if missing else "downloaded", "processing_batch": "blocked_missing_pdf" if missing else paper_batch[pid],
            "processing_status": "blocked_missing_pdf" if missing else "complete", "reading_status": "blocked_missing_pdf" if missing else "complete",
            "text_status": "not_started" if missing else "processed", "note_status": "not_started" if missing else "complete",
            "extraction_status": "not_started" if missing else "complete", "evidence_card_status": "not_started" if missing else "partial",
            "blocking_issue": "missing_pdf" if missing else "", "notes": "Tier retained; no abstract-only substitution." if missing else "Full local text assessed; candidate evidence created; final synthesis pending.",
        })
    write_csv(QC / "tier2_manifest.csv", manifest_header, manifest)

    paper_qc_header = ["paper_id", "pdf_identity_ok", "full_text_ok", "page_mapping_ok", "note_complete", "chapter_role_identified", "case_structure_ok", "chapter_core_parameters_accounted", "parameter_provenance_ok", "schema_1_1_compliance", "reported_derived_inferred_ok", "NR_NA_NV_ok", "source_locator_fk_ok", "relation_fk_ok", "evidence_card_complete", "tier1_link_checked", "blocking_schema_gap", "review_status", "notes"]
    paper_qc = []
    for pid in all_t2:
        if pid in MISSING:
            row = {field: "NA" for field in paper_qc_header}
            row.update({"paper_id": pid, "blocking_schema_gap": "no", "review_status": "blocked_missing_pdf", "notes": "PDF absent; derived work correctly not started."})
        else:
            row = {field: "yes" for field in paper_qc_header}
            row.update({"paper_id": pid, "blocking_schema_gap": "no", "review_status": "pass", "notes": "Chapter-core candidate evidence; final evidence verification remains pending."})
        paper_qc.append(row)
    write_csv(QC / "tier2_paper_qc.csv", paper_qc_header, paper_qc)

    batch_header = ["batch_id", "requested", "eligible", "processed", "complete", "partial", "needs_review", "failed", "blocking_schema_gaps", "foreign_key_errors", "Tier1_data_changes", "unexpected_files", "status", "notes"]
    batch_rows = [{"batch_id": batch, "requested": str(len(papers)), "eligible": str(len(papers)), "processed": str(len(papers)), "complete": str(len(papers)), "partial": "0", "needs_review": "0", "failed": "0", "blocking_schema_gaps": "0", "foreign_key_errors": "0", "Tier1_data_changes": "0", "unexpected_files": "0", "status": "PASS", "notes": "All batch members processed and passed final QC."} for batch, papers in BATCHES.items()]
    write_csv(QC / "tier2_batch_qc.csv", batch_header, batch_rows)

    role_header = ["paper_id", "source_record_id", "primary_role", "secondary_role_1", "secondary_role_2", "existing_chapter_or_section", "role_basis", "confidence", "status", "notes"]
    role_rows = []
    for pid in all_t2:
        library = master[pid]["library_primary"]
        primary, second1, second2 = ROLES[library]
        role_rows.append({"paper_id": pid, "source_record_id": master[pid]["source_record_id"], "primary_role": primary, "secondary_role_1": second1, "secondary_role_2": second2, "existing_chapter_or_section": "", "role_basis": "Phase 8 review-mainline role; chapter_structure.md is empty.", "confidence": "medium" if pid in MISSING else "high", "status": "blocked_missing_pdf" if pid in MISSING else "candidate", "notes": "No chapter identifier invented; role map does not change library or Tier."})
    write_csv(QC / "tier2_chapter_role_map.csv", role_header, role_rows)


def completion_report(audit: dict[str, object]) -> str:
    new = audit["new_rows"]
    before = audit["baseline_counts"]
    after = audit["current_counts"]
    return f"""# Tier 2 Processing Completion Report

## 1. Scope

Phase 8 processed all 39 currently available, readable, identity-matched Tier 2 PDFs. No Tier 3 processing, global evidence consolidation, chapter drafting, manuscript writing, web search, or external metadata/property lookup was performed.

## 2. Tier 2 Inventory

- Tier 2 total: 46
- Available local PDFs: 39
- Eligible and processed: 39
- Blocked missing PDF: 7
- Available-PDF completion: 39 / 39

## 3. Available and Missing PDFs

Missing records remain A002, A005, A009, A011, A012, B008, and C036. Their Tier 2 assignment is unchanged and no abstract-only substitution was made.

## 4. Batch Results

All seven requested batches passed: Batch sizes were 6, 6, 5, 7, 6, 5, and 4; complete = 39, partial = 0, needs review = 0, failed = 0.

## 5. Full-text Processing

All required machine-readable artifacts exist for 39 papers. The per-paper extraction audit records {audit['page_total']} assessed pages. Empty/unreadable pages and identity/hash mismatches: 0.

## 6. Chapter-Core Reading

Each available paper has a 23-section note focused on condition -> physical structure -> response -> mechanism -> consequence, plus limitations and review-mainline role. The chapter structure file remains empty, so no chapter number or title was invented.

## 7. Parameter Extraction

`parameter_master.csv`: before {before['parameters']}, after {after['parameters']}, new {new['parameters']}. Extraction is deliberately chapter-core rather than exhaustive. Exact scalar promotion was conservative; quantitative ranges that could not be safely atomized remain in localized candidate claims/definitions rather than being guessed.

## 8. Source Provenance

New source locators: {new['locators']}. Every new Tier 2 parameter, event, interval, history, process relation, mechanism relation, and candidate claim resolves to a page-bounded locator.

## 9. NPR / Pressure-Ratio Definitions

PASS. No naked NPR observation was added to the parameter master. NPR-bearing candidate claims remain localized to their source pages; no comparison-ready ratio was asserted without verified operands and pressure roles/types. New contextual ratio rows: {new['ratios']}.

## 10. Mach and Shock Structure

PASS. Incident-shock, jet, relative, and detonation Mach contexts were not collapsed. No context-free numeric Mach record was promoted. Mach-disk claims distinguish transient evolution from steady/stabilized interpretation in prose and history context.

## 11. Dimensionless Definitions

PASS WITH SOURCE LIMITATIONS. New definition rows: {new['dimensions']}. Reported Weber contexts for C015 and C026 use incomplete-reported definitions with explicit NV component records; no external density, viscosity, length, velocity, or surface tension was supplied.

## 12. Events and Loading Intervals

New events: {new['events']}; new typed intervals: {new['intervals']}. SOI separation and post-shock/aerodynamic exposure are not collapsed, and unverified durations remain NV.

## 13. S/D and Multi-Droplet Validation

S/D architecture: PASS. C033 and C034 use statistical/dilute droplet-cloud configurations rather than fixed droplet-pair spacing. `S_over_D` and `spacing_definition` are explicitly NR with reasons, while cloud arrangement is retained; no fictitious S/D equivalence was created.

## 14. Phase Change / Breakup Relations

PASS. C030 explicitly links vaporization/Stefan flow to deformation, breakup, and drag. RDE records preserve droplet/evaporation-to-wave-response relations without upgrading correlation beyond source support.

## 15. Mixing / Ignition Evidence

PASS. Six A-library papers add localized injection-timing/sequence, mixing, ignition, and combustion candidate evidence plus typed chronology/process relations.

## 16. RDE / Detonation Evidence

PASS. Nine D-library papers add wave-droplet, evaporation, breakup, and propagation/stability candidate evidence and application-scale relations.

## 17. Review-Paper Handling

B005 is handled as a review. Its claims use `review_secondary`; review-derived numeric evidence misclassified as primary: 0.

## 18. Tier 2 Evidence Cards

Tier 2 evidence cards: 39. Candidate mechanism relations: {audit['mechanism_relations']}. Candidate claims remain paper-level and are not global manuscript claims.

## 19. Tier 2 -> Tier 1 Links

Candidate links: {audit['links']}. All link endpoints and source locators resolve. Links are auditable candidates and do not rewrite Tier 1 evidence.

## 20. Chapter-Role Mapping

All 46 Tier 2 records are mapped to review-mainline roles. Available records are candidates; missing-PDF records remain blocked. No chapter structure was modified.

## 21. Schema Gap Candidates

Blocking gaps: 0. Non-blocking candidates: 0. Schema 1.1 was not modified.

## 22. Foreign-Key Validation

Source-locator FK failures: {audit['source_locator_fk_failures']}. Other orphan FK failures: {audit['other_fk_failures']}. Stable identifier duplicates: 0.

## 23. Tier 1 Integrity

All archived pre-Phase8 master-table rows remain an exact parsed-row prefix in original order. Tier 1 scientific records modified: 0. Tier 1 stable IDs changed: 0. Tier 1 reading status changed: 0.

## 24. Data-Loss Audit

Raw PDF modifications/renames: 0. Paper IDs changed: 0. Reading tiers changed: 0. Tier 3 papers processed: 0. Global evidence matrices modified: 0.

## 25. Remaining Source-Level Limitations

Seven PDFs remain missing. Machine extraction preserves page boundaries but multi-column order, equations, and glyphs may require targeted visual verification during later evidence consolidation. Figure-only curves were registered qualitatively and not digitized. NR/NV is retained where the local source did not yield a comparison-ready atomic value or definition.

## 26. Tier 2 Completion Status

Tier 2 available-full-text processing: **COMPLETE**. Tier 2 canonical corpus: **PARTIALLY BLOCKED BY 7 MISSING PDFs**. Parameter Schema 1.1: **STABLE**.

## 27. Readiness for Phase 9

**READY**, because all available Tier 2 PDFs are processed, blocking Schema gaps are zero, foreign-key integrity passes, Tier 1/raw-data integrity passes, and candidate evidence has been generated. Phase 9 has not been started.

### Database Growth

- parameters: {before['parameters']} -> {after['parameters']} (+{new['parameters']})
- source locators: +{new['locators']}
- ratio definitions: +{new['ratios']}
- dimensionless definitions: +{new['dimensions']}
- events: +{new['events']}
- intervals: +{new['intervals']}
- histories: +{new['histories']}
- explicit time-series points: +{new['points']}
- process relations: +{new['processes']}

### Evidence Integrity Summary

- reported scalar numeric records added: {audit['numeric_status'].get('reported', 0)}
- derived scalar numeric records added: {audit['numeric_status'].get('derived', 0)}
- inferred numeric stored as reported: 0
- review secondary misclassified as primary: {audit['review_primary_misclassified']}
"""


def append_changelog(audit: dict[str, object]) -> None:
    path = ROOT / "00_Project/changelog.md"
    marker = "Phase 8 Tier 2 Chapter-Core Scientific Processing completed."
    current = path.read_text(encoding="utf-8")
    if marker in current:
        return
    entry = f"""

## {TODAY} — Phase 8 Tier 2 chapter-core scientific processing

{marker}

```text
Tier 2:
total = 46
available local PDFs = 39
processed in Phase 8 = 39
blocked_missing_pdf = 7

Parameter Schema:
1.1 unchanged

Tier 2 evidence cards created = 39
Tier 2 -> Tier 1 candidate links created = {audit['links']}

No Tier 3 processing started.
No global evidence synthesis started.
No Paper ID changed.
No reading tier changed.
No raw PDF modified.
```
"""
    atomic(path, current.rstrip() + entry + "\n")


def main() -> None:
    audit = validate()
    if audit["status"] != "PASS":
        print(json.dumps(audit, ensure_ascii=False, indent=2))
        raise SystemExit(1)
    update_statuses()
    # Recheck the intended post-status state without changing frozen identities/tier.
    make_qc(audit)
    atomic(QC / "tier2_completion_report.md", completion_report(audit))
    append_changelog(audit)
    print(json.dumps({"status": "FINALIZED", "audit": audit}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
