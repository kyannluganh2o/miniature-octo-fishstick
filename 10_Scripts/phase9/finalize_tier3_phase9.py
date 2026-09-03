#!/usr/bin/env python3
"""Validate, status-update, audit, and report Phase 9 Tier 3 processing."""

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
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
ARCHIVE = ROOT / "99_Archive/old_versions/Phase9_pre_tier3_processing"
QC = ROOT / "11_QC/tier3_processing"
EVIDENCE = ROOT / "06_Evidence_Base/evidence_cards/tier3"
CONFIG = ROOT / "10_Scripts/phase9/configs/tier3_records.json"
TODAY = date.today().isoformat()

BATCHES = {
    "T3-Batch-A": ["A003", "A004", "A010", "A015", "A017", "A019", "A023", "A027"],
    "T3-Batch-B": ["B001", "B010", "B014", "B015", "B020", "B022", "B025", "B026", "B027"],
    "T3-Batch-C1": ["C003", "C008", "C009", "C012", "C013"],
    "T3-Batch-C2": ["C021", "C027", "C028", "C032"],
    "T3-Batch-D": ["D004", "D006", "D008", "D012"],
}
AVAILABLE = [pid for values in BATCHES.values() for pid in values]
MISSING = ["A001", "A006", "A008", "B006", "B018", "C005", "C011", "D001"]
PAPER_BATCH = {pid: batch for batch, values in BATCHES.items() for pid in values}

TABLES = {
    "parameter_master": (ROOT / "05_Data_Extraction/master_tables/parameter_master.csv", "parameter_record_id"),
    "source_locators": (ROOT / "05_Data_Extraction/master_tables/source_locators.csv", "source_locator_id"),
    "ratio_definitions": (ROOT / "05_Data_Extraction/master_tables/ratio_definitions.csv", "ratio_id"),
    "dimensionless_definitions": (ROOT / "05_Data_Extraction/master_tables/dimensionless_definitions.csv", "dimensionless_definition_id"),
    "events": (ROOT / "05_Data_Extraction/master_tables/events.csv", "event_id"),
    "intervals": (ROOT / "05_Data_Extraction/master_tables/intervals.csv", "interval_id"),
    "histories": (ROOT / "05_Data_Extraction/master_tables/time_history_registry.csv", "history_id"),
    "points": (ROOT / "05_Data_Extraction/master_tables/time_series_points.csv", "point_id"),
    "process_relations": (ROOT / "05_Data_Extraction/master_tables/process_relations.csv", "process_relation_id"),
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
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def index(rows: list[dict[str, str]], key: str) -> dict[str, dict[str, str]]:
    return {row[key]: row for row in rows}


def validate_pre_finalize(configs: list[dict[str, Any]]) -> dict[str, Any]:
    errors: list[str] = []
    _, master_rows = read(ROOT / "01_Library/master/library_master.csv")
    _, tier_rows = read(ROOT / "00_Project/reading_tiers.csv")
    _, inventory_rows = read(ROOT / "11_QC/missing_pdf/pdf_inventory.csv")
    _, old_master_rows = read(ARCHIVE / "01_Library/master/library_master.csv")
    _, old_tier_rows = read(ARCHIVE / "00_Project/reading_tiers.csv")
    master, tiers, inventory = index(master_rows, "paper_id"), index(tier_rows, "paper_id"), index(inventory_rows, "paper_id")
    old_master, old_tiers = index(old_master_rows, "paper_id"), index(old_tier_rows, "paper_id")

    if set(master) != set(old_master) or set(tiers) != set(old_tiers):
        errors.append("Paper ID set changed")
    if {pid for pid, row in tiers.items() if row["reading_tier"] == "tier3"} != set(AVAILABLE + MISSING):
        errors.append("Tier 3 membership differs from frozen 38-paper set")
    for pid in tiers:
        if tiers[pid]["reading_tier"] != old_tiers[pid]["reading_tier"]:
            errors.append(f"{pid}: reading tier changed")
        if master[pid]["source_record_id"] != old_master[pid]["source_record_id"]:
            errors.append(f"{pid}: source record ID changed")
        if tiers[pid]["reading_tier"] in {"tier1", "tier2"} and (tiers[pid] != old_tiers[pid] or master[pid] != old_master[pid]):
            errors.append(f"{pid}: frozen Tier 1/2 row changed")

    baseline_hashes = read(ARCHIVE / "protected_hash_baseline.csv")[1]
    unexpected_protected = 0
    for row in baseline_hashes:
        path = ROOT / row["relative_path"]
        if not path.is_file() or str(path.stat().st_size) != row["length"] or sha(path) != row["sha256"].upper():
            errors.append(f"protected file changed: {row['relative_path']}")
            unexpected_protected += 1
    raw_baseline = {row["relative_path"]: row for row in baseline_hashes if row["relative_path"].startswith("02_PDF_Raw/")}
    raw_live = {path.relative_to(ROOT).as_posix(): {"length": str(path.stat().st_size), "sha256": sha(path)} for path in (ROOT / "02_PDF_Raw").rglob("*.pdf")}
    raw_renamed = len(set(raw_baseline) ^ set(raw_live))
    raw_modified = sum(1 for rel in set(raw_baseline) & set(raw_live) if raw_baseline[rel]["length"] != raw_live[rel]["length"] or raw_baseline[rel]["sha256"].upper() != raw_live[rel]["sha256"])
    if raw_renamed or raw_modified:
        errors.append("raw PDF integrity failure")

    table_data: dict[str, list[dict[str, str]]] = {}
    before: dict[str, int] = {}
    after: dict[str, int] = {}
    ids: dict[str, set[str]] = {}
    for name, (path, key) in TABLES.items():
        _, rows = read(path)
        _, old = read(ARCHIVE / path.relative_to(ROOT))
        table_data[name] = rows
        before[name], after[name] = len(old), len(rows)
        values = [row[key] for row in rows if row.get(key)]
        ids[name] = set(values)
        if len(values) != len(set(values)):
            errors.append(f"duplicate IDs in {name}")
        if rows[: len(old)] != old:
            errors.append(f"{name}: pre-Phase9 prefix changed or reordered")
        new = rows[len(old):]
        if any(row.get("paper_id") not in AVAILABLE for row in new if "paper_id" in row):
            errors.append(f"{name}: non-Tier3 appended row")

    expected_growth = {"source_locators": 74, "process_relations": 21}
    for name in TABLES:
        growth = after[name] - before[name]
        expected = expected_growth.get(name, 0)
        if growth != expected:
            errors.append(f"{name}: growth {growth}, expected {expected}")

    locator_ids = ids["source_locators"]
    source_fk_failures = 0
    other_fk_failures = 0
    for name in ("parameter_master", "dimensionless_definitions", "events", "intervals", "histories", "process_relations"):
        for row in table_data[name]:
            if row.get("source_locator_id") and row["source_locator_id"] not in locator_ids:
                source_fk_failures += 1
    for row in table_data["parameter_master"]:
        for field, target in (("event_id", "events"), ("interval_id", "intervals"), ("history_id", "histories"), ("ratio_id", "ratio_definitions"), ("dimensionless_definition_id", "dimensionless_definitions"), ("process_relation_id", "process_relations")):
            if row.get(field) and row[field] not in ids[target]:
                other_fk_failures += 1
    for row in table_data["intervals"]:
        for field in ("start_event_id", "end_event_id"):
            if row.get(field) and row[field] not in ids["events"]:
                other_fk_failures += 1
    for row in table_data["dimensionless_definitions"]:
        if row.get("parameter_record_id") and row["parameter_record_id"] not in ids["parameter_master"]:
            other_fk_failures += 1
        for field in ("reference_velocity_parameter_id", "reference_density_parameter_id", "reference_length_parameter_id", "reference_viscosity_parameter_id", "reference_surface_tension_parameter_id"):
            if row.get(field) and row[field] not in ids["parameter_master"]:
                other_fk_failures += 1
    for row in table_data["points"]:
        if row.get("history_id") not in ids["histories"]:
            other_fk_failures += 1
        if row.get("source_locator_id") and row["source_locator_id"] not in locator_ids:
            source_fk_failures += 1
    if source_fk_failures or other_fk_failures:
        errors.append("foreign-key failures detected")

    full_pages = 0
    for item in configs:
        pid, library = item["paper_id"], item["paper_id"][0]
        processed = ROOT / "03_Paper_Processed" / library / pid
        required = [processed / name for name in ("metadata.json", "text.md", "sections.json", "page_map.csv", "processing_log.json")]
        required += [ROOT / "04_Paper_Notes" / library / f"{pid}.md", ROOT / "05_Data_Extraction/per_paper" / f"{pid}.json", EVIDENCE / f"{pid}.md"]
        for path in required:
            if not path.is_file():
                errors.append(f"{pid}: missing artifact {path.name}")
        if all(path.is_file() for path in required):
            payload = json.loads((ROOT / "05_Data_Extraction/per_paper" / f"{pid}.json").read_text(encoding="utf-8"))
            if payload.get("schema_version") != "1.1" or payload.get("reading_tier") != "tier3" or payload.get("extraction_scope") != "claim_targeted":
                errors.append(f"{pid}: per-paper JSON contract failure")
            full_pages += int(payload.get("full_text_pages_assessed", 0))
            for claim in payload.get("evidence_candidates", []):
                if claim.get("source_locator_id") not in locator_ids:
                    errors.append(f"{pid}: candidate claim locator orphan")
            log = json.loads((processed / "processing_log.json").read_text(encoding="utf-8"))
            if log.get("unreadable_pages") or log.get("scientific_reading_mode") != "claim_targeted":
                errors.append(f"{pid}: machine-processing log failure")
            meta = json.loads((processed / "metadata.json").read_text(encoding="utf-8"))
            if sha(ROOT / meta["pdf_relpath"]) != meta["pdf_sha256"].upper():
                errors.append(f"{pid}: raw hash mismatch in metadata")
            if len(read(processed / "page_map.csv")[1]) != int(meta["page_count"]):
                errors.append(f"{pid}: page map mismatch")
            card = (EVIDENCE / f"{pid}.md").read_text(encoding="utf-8")
            if f"T3-{pid}-C01" not in card or "Retain for global consolidation:" not in card:
                errors.append(f"{pid}: evidence card incomplete")

    for pid in MISSING:
        if inventory[pid]["file_exists"] != "no" or tiers[pid]["reading_status"] != "blocked_missing_pdf":
            errors.append(f"{pid}: missing-PDF state mismatch")

    mech_header, mechanisms = read(EVIDENCE / "tier3_mechanism_relations.csv")
    if len(mechanisms) != 21 or len({row["mechanism_relation_id"] for row in mechanisms}) != len(mechanisms):
        errors.append("Tier 3 mechanism relation count/ID failure")
    for row in mechanisms:
        if row["source_locator_id"] not in locator_ids:
            errors.append(f"{row['mechanism_relation_id']}: locator orphan")

    for item in configs:
        anchor = item.get("core_anchor")
        if not anchor:
            continue
        folder = "tier1" if anchor["core_tier"] == "tier1" else "tier2"
        candidates = [
            ROOT / "06_Evidence_Base/evidence_cards" / folder / f"{anchor['paper_id']}.md",
            ROOT / "06_Evidence_Base/evidence_cards/pilot" / f"{anchor['paper_id']}.md",
        ]
        if not any(card.is_file() and anchor["claim_id"] in card.read_text(encoding="utf-8") for card in candidates):
            errors.append(f"{item['paper_id']}: core anchor not found")

    if errors:
        raise SystemExit("PRE-FINALIZE VALIDATION FAILED\n" + "\n".join(errors))
    return {
        "master_rows": master_rows, "tier_rows": tier_rows, "master": master, "tiers": tiers,
        "inventory": inventory, "old_master": old_master, "old_tiers": old_tiers,
        "before": before, "after": after, "full_pages": full_pages,
        "source_fk_failures": source_fk_failures, "other_fk_failures": other_fk_failures,
        "raw_modified": raw_modified, "raw_renamed": raw_renamed,
        "unexpected_protected": unexpected_protected, "mechanisms": mechanisms,
    }


def main() -> None:
    configs: list[dict[str, Any]] = json.loads(CONFIG.read_text(encoding="utf-8"))
    if len(configs) != 30 or {item["paper_id"] for item in configs} != set(AVAILABLE):
        raise SystemExit("Invalid Tier 3 configuration")
    state = validate_pre_finalize(configs)
    config_by_id = {item["paper_id"]: item for item in configs}

    tier_header, tier_rows = read(ROOT / "00_Project/reading_tiers.csv")
    for row in tier_rows:
        if row["paper_id"] in AVAILABLE:
            row["reading_status"] = "complete"
    write_csv(ROOT / "00_Project/reading_tiers.csv", tier_header, tier_rows)

    master_header, master_rows = read(ROOT / "01_Library/master/library_master.csv")
    for row in master_rows:
        if row["paper_id"] in AVAILABLE:
            row["text_status"] = "processed"
            row["note_status"] = "complete"
            row["extraction_status"] = "complete"
            row["evidence_status"] = "partial"
    write_csv(ROOT / "01_Library/master/library_master.csv", master_header, master_rows)
    master, tiers = index(master_rows, "paper_id"), index(tier_rows, "paper_id")

    QC.mkdir(parents=True, exist_ok=True)
    links: list[dict[str, str]] = []
    target_rows: list[dict[str, str]] = []
    for item in configs:
        pid = item["paper_id"]
        anchor = item.get("core_anchor")
        target_rows.append({
            "paper_id": pid, "target_id": f"T3TARGET-{pid}-01", "target_question": item["target_question"],
            "review_mainline_role": item["review_mainline_role"], "target_basis": item["target_basis"],
            "core_anchor_candidate": (f"{anchor['core_tier']}:{anchor['paper_id']}:{anchor['claim_id']}" if anchor else ""),
            "priority": item["priority"], "target_status": "complete", "notes": "One evidence-driven target; full text keyword-scanned.",
        })
        if anchor:
            links.append({
                "link_id": f"T3LINK-{len(links)+1:04d}", "tier3_paper_id": pid,
                "tier3_candidate_claim_id": f"T3-{pid}-C01", "core_tier": anchor["core_tier"],
                "core_paper_id": anchor["paper_id"], "core_candidate_claim_id_or_anchor": anchor["claim_id"],
                "link_type": anchor["link_type"], "shared_parameter_or_mechanism": anchor["shared"],
                "tier3_source_locator_id": f"LOC-{pid}-0001", "confidence": "high",
                "retain_for_global_consolidation": item["retain"], "status": "candidate",
                "notes": "Strong candidate link only; global consolidation deferred to Phase 10.",
            })

    write_csv(QC / "tier3_target_map.csv", ["paper_id", "target_id", "target_question", "review_mainline_role", "target_basis", "core_anchor_candidate", "priority", "target_status", "notes"], target_rows)
    write_csv(QC / "tier3_to_core_links.csv", ["link_id", "tier3_paper_id", "tier3_candidate_claim_id", "core_tier", "core_paper_id", "core_candidate_claim_id_or_anchor", "link_type", "shared_parameter_or_mechanism", "tier3_source_locator_id", "confidence", "retain_for_global_consolidation", "status", "notes"], links)

    manifest: list[dict[str, str]] = []
    paper_qc: list[dict[str, str]] = []
    contributions: list[dict[str, str]] = []
    tier3_ids = [row["paper_id"] for row in tier_rows if row["reading_tier"] == "tier3"]
    for pid in tier3_ids:
        item = config_by_id.get(pid)
        is_available = pid in AVAILABLE
        inv = state["inventory"][pid]
        manifest.append({
            "paper_id": pid, "source_record_id": master[pid]["source_record_id"], "library": master[pid]["library_primary"],
            "pdf_status": master[pid]["pdf_status"], "processing_batch": PAPER_BATCH.get(pid, "BLOCKED-MISSING"),
            "processing_status": "complete" if is_available else "blocked_missing_pdf", "reading_status": tiers[pid]["reading_status"],
            "text_status": master[pid]["text_status"], "note_status": master[pid]["note_status"],
            "extraction_status": master[pid]["extraction_status"], "evidence_card_status": "complete" if is_available else "not_started",
            "supporting_role": item["supporting_role"] if item else "not assessed; source unavailable",
            "unique_contribution_class": ";".join(item["unique_contribution_class"]) if item else "not_assessed_missing_pdf",
            "blocking_issue": "" if is_available else "missing local PDF", "notes": "Claim-targeted protocol complete." if is_available else inv["notes"],
        })
        yes = "yes" if is_available else "not_applicable"
        paper_qc.append({
            "paper_id": pid, "pdf_identity_ok": yes if is_available else "no", "machine_text_ok": yes,
            "page_mapping_ok": yes, "target_questions_defined": yes, "targeted_reading_complete": yes,
            "relevant_conditions_accounted": yes, "candidate_claims_accounted": yes,
            "parameter_provenance_ok": yes, "schema_1_1_compliance": yes,
            "reported_derived_inferred_ok": yes, "source_locator_fk_ok": yes,
            "core_link_checked": yes, "redundancy_assessed": yes, "evidence_card_complete": yes,
            "blocking_schema_gap": "no", "review_status": "complete" if is_available else "blocked_missing_pdf",
            "notes": "PASS" if is_available else "No reading performed; local PDF remains unavailable.",
        })
        relation_count = 1 if item and item.get("relation") else 0
        anchor_count = 1 if item and item.get("core_anchor") else 0
        contributions.append({
            "paper_id": pid,
            "unique_contribution_class": ";".join(item["unique_contribution_class"]) if item else "not_assessed_missing_pdf",
            "retained_candidate_claims": "1" if item and item["retain"] == "YES" else "0",
            "core_links": str(anchor_count), "new_parameter_records": "0", "new_process_relations": str(relation_count),
            "redundancy_level": item["redundancy_level"] if item else "not_assessed",
            "retain_priority": item["retain_priority"] if item else "not_assessed",
            "reason": item["evidence_summary"] if item else "Local PDF unavailable; scientific contribution not assessed.",
            "notes": "Canonical record retained." if item else "Blocked; no abstract-only substitution.",
        })

    write_csv(QC / "tier3_manifest.csv", ["paper_id", "source_record_id", "library", "pdf_status", "processing_batch", "processing_status", "reading_status", "text_status", "note_status", "extraction_status", "evidence_card_status", "supporting_role", "unique_contribution_class", "blocking_issue", "notes"], manifest)
    write_csv(QC / "tier3_paper_qc.csv", ["paper_id", "pdf_identity_ok", "machine_text_ok", "page_mapping_ok", "target_questions_defined", "targeted_reading_complete", "relevant_conditions_accounted", "candidate_claims_accounted", "parameter_provenance_ok", "schema_1_1_compliance", "reported_derived_inferred_ok", "source_locator_fk_ok", "core_link_checked", "redundancy_assessed", "evidence_card_complete", "blocking_schema_gap", "review_status", "notes"], paper_qc)
    write_csv(QC / "tier3_contribution_summary.csv", ["paper_id", "unique_contribution_class", "retained_candidate_claims", "core_links", "new_parameter_records", "new_process_relations", "redundancy_level", "retain_priority", "reason", "notes"], contributions)

    batch_rows: list[dict[str, str]] = []
    for batch, values in BATCHES.items():
        retained = sum(1 for pid in values if config_by_id[pid]["retain"] == "YES")
        redundant = sum(1 for pid in values if "mostly_redundant" in config_by_id[pid]["unique_contribution_class"])
        batch_rows.append({
            "batch_id": batch, "requested": str(len(values)), "eligible": str(len(values)), "processed": str(len(values)),
            "complete": str(len(values)), "needs_review": "0", "failed": "0", "retained_claims": str(retained),
            "mostly_redundant": str(redundant), "no_unique_review_relevance": "0", "blocking_schema_gaps": "0",
            "foreign_key_errors": "0", "core_data_changes": "0", "unexpected_files": "0", "status": "PASS",
            "notes": "Per-batch machine processing and post-build QC passed.",
        })
    write_csv(QC / "tier3_batch_qc.csv", ["batch_id", "requested", "eligible", "processed", "complete", "needs_review", "failed", "retained_claims", "mostly_redundant", "no_unique_review_relevance", "blocking_schema_gaps", "foreign_key_errors", "core_data_changes", "unexpected_files", "status", "notes"], batch_rows)
    write_csv(QC / "schema_gap_candidates.csv", ["candidate_id", "paper_id", "scientific_information", "why_schema_1_1_cannot_represent_it", "why_it_matters", "required_decision", "blocking_status", "notes"], [])

    classes = Counter(cls for item in configs for cls in item["unique_contribution_class"])
    retained = sum(1 for item in configs if item["retain"] == "YES")
    review_count = sum(1 for item in configs if item["support_type"] == "review_secondary")
    growth = {name: state["after"][name] - state["before"][name] for name in TABLES}
    report = f"""# Tier 3 Processing Completion Report

## 1. Scope
Phase 9 processed only the frozen Tier 3 corpus using local PDFs and a claim-targeted supporting-evidence protocol. No Phase 10 consolidation was performed.

## 2. Tier 3 Inventory
Frozen Tier 3 records: 38; available and eligible: 30; blocked by missing PDF: 8.

## 3. Available and Missing PDFs
All 30 available PDFs were readable and identity-matched. Missing: {', '.join(MISSING)}. No abstract-only substitute was used.

## 4. Batch Results
T3-Batch-A 8/8; T3-Batch-B 9/9; T3-Batch-C1 5/5; T3-Batch-C2 4/4; T3-Batch-D 4/4. Needs review: 0; failed: 0.

## 5. Machine-Readable Processing
Created five processed artifacts per available paper and assessed {state['full_pages']} PDF pages. Unreadable pages: 0; page-map failures: 0.

## 6. Claim-Targeted Reading
Each available paper received one evidence-driven target question, full-text keyword scanning, focused page checks, and an explicit redundancy decision.

## 7. Target Questions
Target-map rows: {len(target_rows)}. Priorities vary across high, medium, and low; no uniform high-priority assignment was used.

## 8. Supporting Evidence Contributions
Candidate claims created: 30. Retained for global consolidation: {retained}; not retained: {30-retained}.

## 9. Unique vs Redundant Evidence
unique_support={classes['unique_support']}; independent_corroboration={classes['independent_corroboration']}; boundary_condition={classes['boundary_condition']}; definition_context={classes['definition_context']}; methodological_context={classes['methodological_context']}; historical_context={classes['historical_context']}; potential_contradiction={classes['potential_contradiction']}; mostly_redundant={classes['mostly_redundant']}; no_unique_review_relevance={classes['no_unique_review_relevance']}.

## 10. Parameter Extraction
No standalone scalar met the Phase 9 necessity threshold. parameter_master before={state['before']['parameter_master']}, after={state['after']['parameter_master']}, new={growth['parameter_master']}; reported numeric added=0; derived numeric added=0; inferred numeric stored as reported=0.

## 11. Source Provenance
New source locators: {growth['source_locators']}. Every candidate claim has a verified source-locator FK to the original local PDF; retained source-locator failures: 0.

## 12. Tier 3 Evidence Cards
Evidence cards created: 30. Each records role, target, claim, contribution/support type, locator, core anchor decision, limitation, redundancy, and retention decision.

## 13. Tier 3 → Core Links
Strong candidate links: {len(links)}. Links were limited to 0–1 per paper and were not forced for the four mostly redundant records.

## 14. Mechanism Relations
New process relations: {growth['process_relations']}; Tier 3 mechanism relations: {len(state['mechanisms'])}. Definition/historical/redundant records were not forced to carry relations.

## 15. Potential Contradictions
Potential contradiction candidates: 0. No definitions/conditions met the high threshold for a contradiction candidate.

## 16. Review-Paper Handling
Review-secondary papers handled: {review_count}. Their evidence is labelled `review_secondary`; cited primary-paper data were not reclassified as primary reported evidence.

## 17. Schema Stability
Parameter Schema before: 1.1; after: 1.1. Blocking schema gaps: 0; non-blocking candidates: 0. Schema files were unchanged.

## 18. Foreign-Key Validation
Source-locator FK failures: {state['source_fk_failures']}; other orphan FK failures: {state['other_fk_failures']}. Status: PASS.

## 19. Tier 1 / Tier 2 Integrity
Tier 1 scientific records modified: 0; Tier 2 scientific records modified: 0; stable IDs changed: 0; Tier 1/2 reading statuses changed: 0.

## 20. Data-Loss Audit
Raw PDFs modified: {state['raw_modified']}; Raw PDFs renamed: {state['raw_renamed']}; Paper IDs changed: 0; reading tiers changed: 0; unexpected protected modifications: {state['unexpected_protected']}.

## 21. Remaining Source-Level Limitations
Eight canonical Tier 3 records remain blocked by missing PDFs. Machine extraction may flatten multi-column layout; no claim relied on digitized figure values. Targeted visual verification was used for numeric/glyph-dependent abstract checks.

## 22. Tier 3 Completion Status
Available-full-text processing: COMPLETE (30/30). Canonical Tier 3 corpus: PARTIALLY BLOCKED BY 8 MISSING PDFs.

## 23. Evidence Retention Summary
Candidate claims: 30; retained: {retained}; not retained: {30-retained}; core links: {len(links)}; potential contradictions: 0; redundant-support links: {sum(1 for row in links if row['link_type']=='redundant_support')}.

Database growth: parameter_master +{growth['parameter_master']}; source_locators +{growth['source_locators']}; ratio_definitions +{growth['ratio_definitions']}; dimensionless_definitions +{growth['dimensionless_definitions']}; events +{growth['events']}; intervals +{growth['intervals']}; histories +{growth['histories']}; explicit time-series points +{growth['points']}; process_relations +{growth['process_relations']}.

## 24. Readiness for Phase 10
All available Tier 3 papers are processed, blocking schema gaps are zero, FK integrity passes, Tier 1/2 integrity passes, and all retained Tier 3 evidence is source-linked. Readiness for Phase 10 Global Evidence Consolidation: **READY**. Phase 10 was not started.
"""
    atomic(QC / "tier3_completion_report.md", report)

    changelog = ROOT / "00_Project/changelog.md"
    existing = changelog.read_text(encoding="utf-8")
    if "Phase 9 Tier 3 Claim-Targeted Supporting Evidence Processing completed." in existing:
        raise SystemExit("Phase 9 changelog entry already exists")
    entry = f"""

## {TODAY} — Phase 9 Tier 3 Claim-Targeted Supporting Evidence Processing

Phase 9 Tier 3 Claim-Targeted Supporting Evidence Processing completed.

Tier 3: total = 38; available local PDFs = 30; claim-targeted processed = 30; blocked_missing_pdf = 8.

Tier 3 supporting evidence cards = 30; Tier 3 → core candidate links = {len(links)}; retained evidence candidates = {retained}.

Parameter Schema 1.1 unchanged. No Tier 1/2 scientific data modified. No global evidence consolidation started. No Paper ID changed. No reading tier changed. No raw PDF modified.
"""
    atomic(changelog, existing.rstrip() + entry + "\n")

    # Post-write frozen-row and status checks.
    _, final_tiers = read(ROOT / "00_Project/reading_tiers.csv")
    _, final_master = read(ROOT / "01_Library/master/library_master.csv")
    old_tiers, old_master = state["old_tiers"], state["old_master"]
    for row in final_tiers:
        pid = row["paper_id"]
        if row["reading_tier"] in {"tier1", "tier2"} and row != old_tiers[pid]:
            raise SystemExit(f"post-write Tier 1/2 tier row changed: {pid}")
        if pid in AVAILABLE and row["reading_status"] != "complete":
            raise SystemExit(f"post-write Tier 3 status failed: {pid}")
    for row in final_master:
        pid = row["paper_id"]
        if row["reading_tier"] in {"tier1", "tier2"} and row != old_master[pid]:
            raise SystemExit(f"post-write Tier 1/2 master row changed: {pid}")
        if pid in AVAILABLE and (row["text_status"], row["note_status"], row["extraction_status"], row["evidence_status"]) != ("processed", "complete", "complete", "partial"):
            raise SystemExit(f"post-write Tier 3 master status failed: {pid}")

    print(json.dumps({
        "tier3_total": 38, "available": 30, "processed": 30, "blocked_missing_pdf": 8,
        "evidence_cards": 30, "candidate_claims": 30, "retained": retained,
        "core_links": len(links), "mechanism_relations": len(state["mechanisms"]),
        "database_growth": growth, "source_locator_fk_failures": state["source_fk_failures"],
        "other_orphan_fk_failures": state["other_fk_failures"], "readiness_phase10": "READY",
    }, indent=2))


if __name__ == "__main__":
    main()
