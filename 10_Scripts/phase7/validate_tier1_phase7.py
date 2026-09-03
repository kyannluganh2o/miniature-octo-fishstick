#!/usr/bin/env python3
"""Read-only integrity audit for Phase 7 Tier 1 bulk outputs."""

from __future__ import annotations

import csv
import hashlib
import json
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
ARCHIVE = ROOT / "99_Archive/old_versions/Phase7_pre_tier1_bulk"
BULK = ["B004", "B009", "B028", "C007", "C018", "C019", "C024", "C025", "C035", "D018", "A026", "A028", "A029", "A030"]
PILOT = ["A016", "A020", "A022", "B011", "B013", "B029", "C014", "C016", "C031", "D003", "D009", "D017"]
MISSING = ["A007", "B021", "C004", "C029", "D019"]

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


def rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def ensure(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def main() -> None:
    errors: list[str] = []
    warnings: list[str] = []
    data = {name: rows(path) for name, (path, _) in TABLES.items()}
    ids: dict[str, set[str]] = {}
    for name, (_, key) in TABLES.items():
        values = [row[key] for row in data[name] if row[key]]
        ensure(len(values) == len(set(values)), f"duplicate IDs in {name}", errors)
        ids[name] = set(values)

    # Schema dictionary parameter-name/group mapping and controlled vocabularies.
    dictionary = (ROOT / "05_Data_Extraction/schema/parameter_dictionary.yaml").read_text(encoding="utf-8")
    parameter_map = dict(re.findall(r"^  ([A-Za-z_][A-Za-z0-9_]*): \{group: ([A-Za-z_][A-Za-z0-9_]*)", dictionary, re.M))
    vocab: dict[str, set[str]] = {}
    for match in re.finditer(r"^  ([A-Za-z_][A-Za-z0-9_]*): \[([^\]]*)\]", dictionary, re.M):
        vocab[match.group(1)] = {part.strip().strip('"') for part in match.group(2).split(",")}

    for row in data["parameters"]:
        pid = row["paper_id"]
        # Pilot names were formally accepted by Phase 6.1 and are immutable in
        # Phase 7. Apply strict dictionary mapping to newly appended rows.
        if pid in BULK:
            ensure(row["parameter_name"] in parameter_map, f"{row['parameter_record_id']}: unknown parameter_name", errors)
            if row["parameter_name"] in parameter_map:
                ensure(parameter_map[row["parameter_name"]] == row["parameter_group"], f"{row['parameter_record_id']}: name/group mismatch", errors)
        for field in ("value_status", "source_type", "extraction_status", "verification_status", "parameter_role"):
            ensure(row[field] in vocab[field], f"{row['parameter_record_id']}: invalid {field}={row[field]}", errors)
        if row["reference_frame"]:
            ensure(row["reference_frame"] in vocab["reference_frame"], f"{row['parameter_record_id']}: invalid reference_frame", errors)
        if row["state_qualifier"]:
            ensure(row["state_qualifier"] in vocab["mach_disk_state"], f"{row['parameter_record_id']}: invalid state_qualifier", errors)
        if row["parameter_name"] == "shock_geometry":
            ensure(row["reported_value"] in vocab["shock_geometry"], f"{row['parameter_record_id']}: invalid shock geometry", errors)
        ensure(row["source_locator_id"] in ids["locators"], f"{row['parameter_record_id']}: locator FK orphan", errors)
        if row["value_status"] in {"NR", "NA", "NV"}:
            ensure(bool(row["missing_reason"]), f"{row['parameter_record_id']}: missing reason absent", errors)
        for field, target in (("event_id", "events"), ("interval_id", "intervals"), ("history_id", "histories"), ("ratio_id", "ratios"), ("dimensionless_definition_id", "dimensions"), ("process_relation_id", "processes")):
            if row[field]:
                ensure(row[field] in ids[target], f"{row['parameter_record_id']}: {field} orphan", errors)

    for name in ("events", "intervals", "histories", "ratios", "dimensions", "processes"):
        for row in data[name]:
            ensure(row["source_locator_id"] in ids["locators"], f"{row[TABLES[name][1]]}: locator FK orphan", errors)
    for row in data["intervals"]:
        for field in ("start_event_id", "end_event_id"):
            if row[field]:
                ensure(row[field] in ids["events"], f"{row['interval_id']}: {field} orphan", errors)
    for row in data["histories"]:
        if row["time_reference_event_id"]:
            ensure(row["time_reference_event_id"] in ids["events"], f"{row['history_id']}: event orphan", errors)
    for row in data["dimensions"]:
        ensure(row["parameter_record_id"] in ids["parameters"], f"{row['dimensionless_definition_id']}: observation orphan", errors)
        for field in ("reference_velocity_parameter_id", "reference_density_parameter_id", "reference_length_parameter_id", "reference_viscosity_parameter_id", "reference_surface_tension_parameter_id"):
            if row[field]:
                ensure(row[field] in ids["parameters"], f"{row['dimensionless_definition_id']}: {field} orphan", errors)
        for component in filter(None, row["other_component_ids"].split(";")):
            ensure(component in ids["parameters"], f"{row['dimensionless_definition_id']}: other component orphan", errors)
    for row in data["ratios"]:
        for field in ("numerator_parameter_record_id", "denominator_parameter_record_id"):
            if row[field]:
                ensure(row[field] in ids["parameters"], f"{row['ratio_id']}: {field} orphan", errors)

    mechanisms_path = ROOT / "06_Evidence_Base/evidence_cards/tier1/tier1_mechanism_relations.csv"
    mechanisms = rows(mechanisms_path)
    mech_ids = [row["mechanism_relation_id"] for row in mechanisms]
    ensure(len(mech_ids) == len(set(mech_ids)), "duplicate Tier 1 mechanism IDs", errors)
    for row in mechanisms:
        ensure(row["source_locator_id"] in ids["locators"], f"{row['mechanism_relation_id']}: locator orphan", errors)
        ensure(row["relation_type"] in vocab["relation_type"], f"{row['mechanism_relation_id']}: invalid relation_type", errors)
        ensure(row["support_type"] in vocab["support_type"], f"{row['mechanism_relation_id']}: invalid support_type", errors)

    # Required artifacts and local-PDF integrity.
    inventory = {row["paper_id"]: row for row in rows(ROOT / "11_QC/missing_pdf/pdf_inventory.csv")}
    master = {row["paper_id"]: row for row in rows(ROOT / "01_Library/master/library_master.csv")}
    tiers = {row["paper_id"]: row for row in rows(ROOT / "00_Project/reading_tiers.csv")}
    for paper_id in BULK:
        library = master[paper_id]["library_primary"]
        processed = ROOT / "03_Paper_Processed" / library / paper_id
        for filename in ("metadata.json", "text.md", "sections.json", "page_map.csv", "processing_log.json"):
            ensure((processed / filename).is_file(), f"{paper_id}: missing processed {filename}", errors)
        ensure((ROOT / "04_Paper_Notes" / library / f"{paper_id}.md").is_file(), f"{paper_id}: missing note", errors)
        ensure((ROOT / "05_Data_Extraction/per_paper" / f"{paper_id}.json").is_file(), f"{paper_id}: missing per-paper JSON", errors)
        ensure((ROOT / "06_Evidence_Base/evidence_cards/tier1" / f"{paper_id}.md").is_file(), f"{paper_id}: missing evidence card", errors)
        log = json.loads((processed / "processing_log.json").read_text(encoding="utf-8"))
        raw = ROOT / inventory[paper_id]["current_relpath"]
        ensure(sha(raw) == json.loads((processed / "metadata.json").read_text(encoding="utf-8"))["pdf_sha256"], f"{paper_id}: raw PDF hash changed", errors)
        ensure(not log["unreadable_pages"], f"{paper_id}: unreadable page recorded", errors)
        ensure(tiers[paper_id]["reading_tier"] == "tier1", f"{paper_id}: tier changed", errors)

    ensure(set(PILOT + BULK + MISSING) == {pid for pid, row in tiers.items() if row["reading_tier"] == "tier1"}, "Tier 1 membership differs from locked 31-paper set", errors)

    # Data-loss audit: archived table rows must be an exact prefix of current tables.
    baseline_counts: dict[str, int] = {}
    current_counts: dict[str, int] = {}
    for name, (path, _) in TABLES.items():
        archived_path = ARCHIVE / path.relative_to(ROOT)
        old = rows(archived_path)
        current = data[name]
        baseline_counts[name] = len(old)
        current_counts[name] = len(current)
        ensure(current[: len(old)] == old, f"{name}: pre-Phase7 rows changed or reordered", errors)

    bulk_params = [row for row in data["parameters"] if row["paper_id"] in BULK]
    numeric = [row for row in bulk_params if row["reported_value"] not in {"", "NR", "NA", "NV"} and re.fullmatch(r"[-+]?\d+(?:\.\d+)?(?:[Ee][-+]?\d+)?", row["reported_value"].strip())]
    numeric_status = Counter(row["value_status"] for row in numeric)
    ensure(numeric_status.get("inferred", 0) == 0, "inferred numeric records stored", errors)

    result = {
        "status": "PASS" if not errors else "FAIL",
        "errors": errors,
        "warnings": warnings,
        "bulk_papers": BULK,
        "pilot_papers": PILOT,
        "missing_papers": MISSING,
        "baseline_counts": baseline_counts,
        "current_counts": current_counts,
        "new_rows": {name: current_counts[name] - baseline_counts[name] for name in TABLES},
        "mechanism_relations": len(mechanisms),
        "bulk_parameter_rows": len(bulk_params),
        "bulk_numeric_status": dict(numeric_status),
        "source_locator_fk_failures": sum("locator" in item and "orphan" in item for item in errors),
        "other_fk_failures": sum("orphan" in item and "locator" not in item for item in errors),
        "raw_pdf_hash_failures": sum("raw PDF hash" in item for item in errors),
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    if errors:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
