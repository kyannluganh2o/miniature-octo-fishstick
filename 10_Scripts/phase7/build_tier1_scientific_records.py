#!/usr/bin/env python3
"""Build Phase 7 per-paper scientific records from reviewed JSON configs.

Configs contain only information confirmed during full-text reading. The builder
assigns stable paper-local IDs, resolves aliases, validates controlled links,
refuses overwrite/duplicate append, writes per-paper notes and evidence cards,
and appends the Schema 1.1 normalized master tables.
"""

from __future__ import annotations

import argparse
import copy
import csv
import json
import os
import tempfile
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
MASTER_LIBRARY = ROOT / "01_Library/master/library_master.csv"
TIERS = ROOT / "00_Project/reading_tiers.csv"
PER_PAPER = ROOT / "05_Data_Extraction/per_paper"
NOTES_ROOT = ROOT / "04_Paper_Notes"
EVIDENCE_ROOT = ROOT / "06_Evidence_Base/evidence_cards/tier1"

TABLES = {
    "parameters": ROOT / "05_Data_Extraction/master_tables/parameter_master.csv",
    "source_locators": ROOT / "05_Data_Extraction/master_tables/source_locators.csv",
    "ratios": ROOT / "05_Data_Extraction/master_tables/ratio_definitions.csv",
    "dimensionless_definitions": ROOT / "05_Data_Extraction/master_tables/dimensionless_definitions.csv",
    "events": ROOT / "05_Data_Extraction/master_tables/events.csv",
    "intervals": ROOT / "05_Data_Extraction/master_tables/intervals.csv",
    "histories": ROOT / "05_Data_Extraction/master_tables/time_history_registry.csv",
    "time_series_points": ROOT / "05_Data_Extraction/master_tables/time_series_points.csv",
    "process_relations": ROOT / "05_Data_Extraction/master_tables/process_relations.csv",
}

MECHANISM_TABLE = EVIDENCE_ROOT / "tier1_mechanism_relations.csv"

NOTE_HEADINGS = [
    "Bibliographic Identity",
    "Tier 1 Role",
    "Research Question",
    "Study Type and Configuration",
    "Geometry and Operating Conditions",
    "Injection / Ambient Conditions",
    "Wave / Jet Structure",
    "Droplet / Spray Initial Conditions",
    "Dimensionless Parameters",
    "Time Scales",
    "Main Physical Observations",
    "Quantitative Results",
    "Mechanism Proposed by Authors",
    "Wave → Droplet/Spray Response Chain",
    "Mixing / Ignition / Combustion Consequences",
    "Key Figures, Tables, and Equations",
    "Reported vs Derived vs Inferred",
    "Limitations",
    "Evidence Candidates",
    "Contradictions / Comparison Hooks",
    "Parameter-Schema Gaps",
    "Relevance to Review Mainline",
    "Reading Completion Checklist",
]


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        return list(reader.fieldnames or []), list(reader)


def index_csv(path: Path, key: str) -> dict[str, dict[str, str]]:
    _, rows = read_csv(path)
    result: dict[str, dict[str, str]] = {}
    for row in rows:
        if row[key] in result:
            raise ValueError(f"Duplicate {key}={row[key]} in {path}")
        result[row[key]] = row
    return result


def blank_row(header: list[str]) -> dict[str, str]:
    return {field: "" for field in header}


def expand_repeated_items(paper: dict[str, Any]) -> None:
    """Expand compact config entries that contain a ``for_each`` list.

    String fields may use ``{suffix}``, ``{case_id}``, or any other variant
    key. This is a configuration convenience only; expanded records pass the
    same validations as ordinary explicit records.
    """
    repeatable = (
        "parameters", "ratios", "dimensionless_definitions", "events",
        "intervals", "histories", "process_relations", "mechanism_relations",
    )
    for field in repeatable:
        expanded: list[dict[str, Any]] = []
        for raw_item in paper.get(field, []):
            variants = raw_item.get("for_each")
            if not variants:
                expanded.append(raw_item)
                continue
            base = {key: copy.deepcopy(value) for key, value in raw_item.items() if key != "for_each"}
            for variant in variants:
                item = copy.deepcopy(base)
                item.update(copy.deepcopy(variant))
                for key, value in list(item.items()):
                    if isinstance(value, str):
                        item[key] = value.format(**variant)
                expanded.append(item)
        paper[field] = expanded


def make_id(prefix: str, paper_id: str, number: int, width: int) -> str:
    return f"{prefix}-{paper_id}-{number:0{width}d}"


def ensure_allowed_paper(paper: dict[str, Any], master: dict[str, dict[str, str]], tiers: dict[str, dict[str, str]]) -> None:
    paper_id = paper["paper_id"]
    if paper_id not in master or paper_id not in tiers:
        raise ValueError(f"{paper_id}: missing canonical records")
    if master[paper_id]["source_record_id"] != paper["source_record_id"]:
        raise ValueError(f"{paper_id}: source_record_id mismatch")
    if master[paper_id]["library_primary"] != paper["library"]:
        raise ValueError(f"{paper_id}: library mismatch")
    if tiers[paper_id]["reading_tier"] != "tier1" or tiers[paper_id]["reading_status"] != "not_started":
        raise ValueError(f"{paper_id}: not an unprocessed Tier 1 paper")
    processed_dir = ROOT / "03_Paper_Processed" / paper["library"] / paper_id
    required = {"metadata.json", "text.md", "sections.json", "page_map.csv", "processing_log.json"}
    if not processed_dir.is_dir() or not required.issubset({item.name for item in processed_dir.iterdir()}):
        raise ValueError(f"{paper_id}: incomplete machine-readable layer")


def prepare_paper(paper: dict[str, Any], headers: dict[str, list[str]]) -> dict[str, Any]:
    paper_id = paper["paper_id"]
    source_id = paper["source_record_id"]
    aliases: dict[str, dict[str, str]] = {
        "locator": {}, "parameter": {}, "event": {}, "interval": {},
        "history": {}, "ratio": {}, "dimensionless": {}, "process": {},
    }

    locators: list[dict[str, str]] = []
    for number, item in enumerate(paper.get("source_locators", []), start=1):
        row = blank_row(headers["source_locators"])
        row.update({field: str(value) for field, value in item.items() if field in row and field != "key"})
        row["source_locator_id"] = make_id("LOC", paper_id, number, 4)
        row["paper_id"] = paper_id
        row["source_file"] = paper["pdf_relpath"]
        row.setdefault("locator_status", "complete")
        if not row["locator_status"]:
            row["locator_status"] = "complete"
        if not row["verification_status"]:
            row["verification_status"] = "verified"
        aliases["locator"][item["key"]] = row["source_locator_id"]
        locators.append(row)

    events: list[dict[str, str]] = []
    for number, item in enumerate(paper.get("events", []), start=1):
        row = blank_row(headers["events"])
        row.update({field: str(value) for field, value in item.items() if field in row and field != "key"})
        row["event_id"] = make_id("EVT", paper_id, number, 3)
        row["paper_id"] = paper_id
        aliases["event"][item["key"]] = row["event_id"]
        events.append(row)
    for row, item in zip(events, paper.get("events", [])):
        row["reference_event_id"] = aliases["event"].get(item.get("reference_event", ""), "")
        row["source_locator_id"] = aliases["locator"][item["locator"]]

    intervals: list[dict[str, str]] = []
    for number, item in enumerate(paper.get("intervals", []), start=1):
        row = blank_row(headers["intervals"])
        row.update({field: str(value) for field, value in item.items() if field in row and field != "key"})
        row["interval_id"] = make_id("INT", paper_id, number, 3)
        row["paper_id"] = paper_id
        row["start_event_id"] = aliases["event"].get(item.get("start_event", ""), "")
        row["end_event_id"] = aliases["event"].get(item.get("end_event", ""), "")
        row["source_locator_id"] = aliases["locator"][item["locator"]]
        aliases["interval"][item["key"]] = row["interval_id"]
        intervals.append(row)

    histories: list[dict[str, str]] = []
    for number, item in enumerate(paper.get("histories", []), start=1):
        row = blank_row(headers["histories"])
        row.update({field: str(value) for field, value in item.items() if field in row and field != "key"})
        row["history_id"] = make_id("HIST", paper_id, number, 3)
        row["paper_id"] = paper_id
        row["time_reference_event_id"] = aliases["event"].get(item.get("reference_event", ""), "")
        row["source_locator_id"] = aliases["locator"][item["locator"]]
        aliases["history"][item["key"]] = row["history_id"]
        histories.append(row)

    parameters: list[dict[str, str]] = []
    for number, item in enumerate(paper.get("parameters", []), start=1):
        row = blank_row(headers["parameters"])
        row.update({field: str(value) for field, value in item.items() if field in row and field != "key"})
        row["parameter_record_id"] = make_id("PAR", paper_id, number, 4)
        row["paper_id"] = paper_id
        row["source_record_id"] = source_id
        row["reading_tier"] = "tier1"
        row["case_id"] = item.get("case_id", "ALL")
        row["condition_id"] = item.get("condition_id", row["case_id"])
        row["context_id"] = f"CTX-{paper_id}-{row['case_id']}-{row['condition_id']}"
        row["reported_value"] = str(item.get("reported_value", ""))
        row["source_locator_id"] = aliases["locator"][item["locator"]]
        locator = next(loc for loc in locators if loc["source_locator_id"] == row["source_locator_id"])
        row["source_location"] = locator["raw_locator"]
        row["schema_version"] = "1.1"
        row["extraction_status"] = item.get("extraction_status", "complete")
        row["verification_status"] = item.get("verification_status", "verified")
        aliases["parameter"][item["key"]] = row["parameter_record_id"]
        parameters.append(row)

    ratios: list[dict[str, str]] = []
    for number, item in enumerate(paper.get("ratios", []), start=1):
        row = blank_row(headers["ratios"])
        row.update({field: str(value) for field, value in item.items() if field in row and field != "key"})
        row["ratio_id"] = make_id("RATIO", paper_id, number, 3)
        row["paper_id"] = paper_id
        row["numerator_parameter_record_id"] = aliases["parameter"].get(item.get("numerator_parameter", ""), "")
        row["denominator_parameter_record_id"] = aliases["parameter"].get(item.get("denominator_parameter", ""), "")
        row["source_locator_id"] = aliases["locator"][item["locator"]]
        aliases["ratio"][item["key"]] = row["ratio_id"]
        ratios.append(row)

    dimensions: list[dict[str, str]] = []
    for number, item in enumerate(paper.get("dimensionless_definitions", []), start=1):
        row = blank_row(headers["dimensionless_definitions"])
        row.update({field: str(value) for field, value in item.items() if field in row and field != "key"})
        row["dimensionless_definition_id"] = make_id("DIM", paper_id, number, 3)
        row["paper_id"] = paper_id
        row["parameter_record_id"] = aliases["parameter"][item["parameter"]]
        for config_name, field_name in (
            ("reference_velocity", "reference_velocity_parameter_id"),
            ("reference_density", "reference_density_parameter_id"),
            ("reference_length", "reference_length_parameter_id"),
            ("reference_viscosity", "reference_viscosity_parameter_id"),
            ("reference_surface_tension", "reference_surface_tension_parameter_id"),
        ):
            row[field_name] = aliases["parameter"].get(item.get(config_name, ""), "")
        other = item.get("other_components", [])
        row["other_component_ids"] = ";".join(aliases["parameter"][key] for key in other)
        row["source_locator_id"] = aliases["locator"][item["locator"]]
        aliases["dimensionless"][item["key"]] = row["dimensionless_definition_id"]
        dimensions.append(row)

    processes: list[dict[str, str]] = []
    for number, item in enumerate(paper.get("process_relations", []), start=1):
        row = blank_row(headers["process_relations"])
        row.update({field: str(value) for field, value in item.items() if field in row and field != "key"})
        row["process_relation_id"] = make_id("PROC", paper_id, number, 3)
        row["paper_id"] = paper_id
        row["source_locator_id"] = aliases["locator"][item["locator"]]
        aliases["process"][item["key"]] = row["process_relation_id"]
        processes.append(row)

    # Resolve relational links stored on parameter observations.
    for row, item in zip(parameters, paper.get("parameters", [])):
        for config_name, field_name, namespace in (
            ("event", "event_id", "event"), ("interval", "interval_id", "interval"),
            ("history", "history_id", "history"), ("ratio", "ratio_id", "ratio"),
            ("dimensionless", "dimensionless_definition_id", "dimensionless"),
            ("process", "process_relation_id", "process"),
        ):
            row[field_name] = aliases[namespace].get(item.get(config_name, ""), "")

    contexts = []
    seen_contexts: set[tuple[str, str]] = set()
    for row in parameters:
        key = (row["case_id"], row["condition_id"])
        if key not in seen_contexts:
            contexts.append({"context_id": row["context_id"], "case_id": key[0], "condition_id": key[1]})
            seen_contexts.add(key)

    mechanisms: list[dict[str, str]] = []
    mechanism_header = [
        "mechanism_relation_id", "paper_id", "case_id", "source_node", "relation_type",
        "target_node", "support_type", "candidate_claim_id", "source_locator_id",
        "verification_status", "notes",
    ]
    for number, item in enumerate(paper.get("mechanism_relations", []), start=1):
        row = blank_row(mechanism_header)
        row.update({field: str(value) for field, value in item.items() if field in row})
        row["mechanism_relation_id"] = make_id("MECH", paper_id, number, 3)
        row["paper_id"] = paper_id
        row["source_locator_id"] = aliases["locator"][item["locator"]]
        mechanisms.append(row)

    for claim in paper.get("evidence_candidates", []):
        claim["source_locator_id"] = aliases["locator"][claim["locator"]]
        claim["relevant_parameter_ids"] = [aliases["parameter"][key] for key in claim.get("parameters", [])]
        claim["relevant_process_event_ids"] = [
            aliases[namespace][key]
            for namespace, key in claim.get("relations_events", [])
        ]

    return {
        "paper": paper,
        "aliases": aliases,
        "contexts": contexts,
        "parameters": parameters,
        "source_locators": locators,
        "events": events,
        "intervals": intervals,
        "histories": histories,
        "ratios": ratios,
        "dimensionless_definitions": dimensions,
        "process_relations": processes,
        "mechanism_relations": mechanisms,
    }


def validate_prepared(item: dict[str, Any], existing_ids: dict[str, set[str]]) -> None:
    paper_id = item["paper"]["paper_id"]
    specs = (
        ("parameters", "parameter_record_id"), ("source_locators", "source_locator_id"),
        ("events", "event_id"), ("intervals", "interval_id"), ("histories", "history_id"),
        ("ratios", "ratio_id"), ("dimensionless_definitions", "dimensionless_definition_id"),
        ("process_relations", "process_relation_id"),
    )
    for table_name, key in specs:
        ids = [row[key] for row in item[table_name]]
        if len(ids) != len(set(ids)) or set(ids) & existing_ids[table_name]:
            raise ValueError(f"{paper_id}: duplicate IDs in {table_name}")
    locator_ids = {row["source_locator_id"] for row in item["source_locators"]}
    parameter_ids = {row["parameter_record_id"] for row in item["parameters"]}
    event_ids = {row["event_id"] for row in item["events"]}
    for row in item["parameters"]:
        if row["source_locator_id"] not in locator_ids:
            raise ValueError(f"{paper_id}: parameter locator orphan")
        if row["value_status"] in {"NR", "NA", "NV"} and not row["missing_reason"]:
            raise ValueError(f"{paper_id}: missing rationale on {row['parameter_record_id']}")
        if row["value_status"] == "reported" and not row["source_locator_id"]:
            raise ValueError(f"{paper_id}: reported parameter without locator")
    for row in item["intervals"]:
        if row["start_event_id"] and row["start_event_id"] not in event_ids:
            raise ValueError(f"{paper_id}: interval start orphan")
        if row["end_event_id"] and row["end_event_id"] not in event_ids:
            raise ValueError(f"{paper_id}: interval end orphan")
    for row in item["dimensionless_definitions"]:
        if row["parameter_record_id"] not in parameter_ids:
            raise ValueError(f"{paper_id}: dimensionless parameter orphan")


def render_note(item: dict[str, Any], master_row: dict[str, str]) -> str:
    paper = item["paper"]
    sections = paper["note_sections"]
    if len(sections) != 23:
        raise ValueError(f"{paper['paper_id']}: note must contain exactly 23 sections")
    lines = [f"# {paper['paper_id']}", ""]
    for number, (heading, content) in enumerate(zip(NOTE_HEADINGS, sections), start=1):
        lines.extend([f"## {number}. {heading}", "", str(content).strip(), ""])
    return "\n".join(lines).rstrip() + "\n"


def render_evidence(item: dict[str, Any]) -> str:
    paper = item["paper"]
    lines = [f"# {paper['paper_id']} Tier 1 Evidence Card", ""]
    for number, claim in enumerate(paper.get("evidence_candidates", []), start=1):
        lines.extend(
            [
                f"## Candidate Claim {number}", "",
                f"Claim ID: {claim['claim_id']}", "",
                f"Candidate claim: {claim['claim']}", "",
                f"Evidence type: {claim['evidence_type']}", "",
                f"Evidence summary: {claim['evidence_summary']}", "",
                f"Source locator: {claim['source_locator_id']}", "",
                f"Support type: {claim['support_type']}", "",
                f"Limitations: {claim['limitations']}", "",
                "Relevant parameter IDs: " + ("; ".join(claim["relevant_parameter_ids"]) or "None"), "",
                "Relevant process/event IDs: " + ("; ".join(claim["relevant_process_event_ids"]) or "None"), "",
                f"Potential chapter role: {claim['potential_chapter_role']}", "",
            ]
        )
    return "\n".join(lines).rstrip() + "\n"


def per_paper_payload(item: dict[str, Any]) -> dict[str, Any]:
    paper = item["paper"]
    return {
        "paper_id": paper["paper_id"],
        "source_record_id": paper["source_record_id"],
        "reading_tier": "tier1",
        "tier1_role": paper["tier1_role"],
        "study_context": paper["study_context"],
        "cases": paper.get("cases", []),
        "parameters": item["parameters"],
        "key_results": paper.get("key_results", []),
        "mechanisms": paper.get("mechanisms", []),
        "evidence_candidates": paper.get("evidence_candidates", []),
        "schema_gap_candidates": paper.get("schema_gap_candidates", []),
        "extraction_notes": paper.get("extraction_notes", []),
        "extraction_status": paper.get("extraction_status", "complete"),
        "schema_version": "1.1",
        "contexts": item["contexts"],
        "events": item["events"],
        "intervals": item["intervals"],
        "histories": item["histories"],
        "ratios": item["ratios"],
        "dimensionless_definitions": item["dimensionless_definitions"],
        "process_relations": item["process_relations"],
        "source_locators": item["source_locators"],
    }


def atomic_write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        raise FileExistsError(f"Refusing to overwrite {path}")
    fd, temp_name = tempfile.mkstemp(prefix=path.name + ".", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="") as handle:
            handle.write(content)
        os.replace(temp_name, path)
    except Exception:
        Path(temp_name).unlink(missing_ok=True)
        raise


def append_rows(path: Path, header: list[str], rows: list[dict[str, str]]) -> None:
    if not rows:
        return
    with path.open("a", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=header, extrasaction="raise")
        writer.writerows(rows)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("config", type=Path)
    parser.add_argument(
        "--validate-only",
        action="store_true",
        help="Validate and render all payloads in memory without writing files or tables.",
    )
    args = parser.parse_args()
    config = json.loads(args.config.read_text(encoding="utf-8"))
    papers = config["papers"]
    for paper in papers:
        expand_repeated_items(paper)

    master = index_csv(MASTER_LIBRARY, "paper_id")
    tiers = index_csv(TIERS, "paper_id")
    headers: dict[str, list[str]] = {}
    existing_rows: dict[str, list[dict[str, str]]] = {}
    existing_ids: dict[str, set[str]] = {}
    key_fields = {
        "parameters": "parameter_record_id", "source_locators": "source_locator_id",
        "ratios": "ratio_id", "dimensionless_definitions": "dimensionless_definition_id",
        "events": "event_id", "intervals": "interval_id", "histories": "history_id",
        "process_relations": "process_relation_id", "time_series_points": "point_id",
    }
    for name, path in TABLES.items():
        headers[name], existing_rows[name] = read_csv(path)
        existing_ids[name] = {row[key_fields[name]] for row in existing_rows[name] if row[key_fields[name]]}

    for paper in papers:
        ensure_allowed_paper(paper, master, tiers)
        if (PER_PAPER / f"{paper['paper_id']}.json").exists():
            raise FileExistsError(f"Per-paper JSON already exists for {paper['paper_id']}")

    prepared = [prepare_paper(paper, headers) for paper in papers]
    for item in prepared:
        validate_prepared(item, existing_ids)

    # Build all text payloads before the first write.
    payloads = []
    for item in prepared:
        paper_id = item["paper"]["paper_id"]
        library = item["paper"]["library"]
        payloads.append(
            (
                PER_PAPER / f"{paper_id}.json",
                json.dumps(per_paper_payload(item), ensure_ascii=False, indent=2) + "\n",
            )
        )
        payloads.append((NOTES_ROOT / library / f"{paper_id}.md", render_note(item, master[paper_id])))
        payloads.append((EVIDENCE_ROOT / f"{paper_id}.md", render_evidence(item)))

    result = {
        "mode": "validate-only" if args.validate_only else "write",
        "papers": [item["paper"]["paper_id"] for item in prepared],
        "new_rows": {
            name: sum(len(item[name]) for item in prepared)
            for name in (
                "parameters", "source_locators", "ratios", "dimensionless_definitions",
                "events", "intervals", "histories", "process_relations", "mechanism_relations",
            )
        },
    }
    if args.validate_only:
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return

    for path, content in payloads:
        atomic_write_text(path, content)

    for name in (
        "parameters", "source_locators", "ratios", "dimensionless_definitions",
        "events", "intervals", "histories", "process_relations",
    ):
        rows = [row for item in prepared for row in item[name]]
        append_rows(TABLES[name], headers[name], rows)

    mechanism_header = [
        "mechanism_relation_id", "paper_id", "case_id", "source_node", "relation_type",
        "target_node", "support_type", "candidate_claim_id", "source_locator_id",
        "verification_status", "notes",
    ]
    mechanism_rows = [row for item in prepared for row in item["mechanism_relations"]]
    EVIDENCE_ROOT.mkdir(parents=True, exist_ok=True)
    if mechanism_rows:
        new_file = not MECHANISM_TABLE.exists()
        with MECHANISM_TABLE.open("a", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=mechanism_header)
            if new_file:
                writer.writeheader()
            writer.writerows(mechanism_rows)

    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
