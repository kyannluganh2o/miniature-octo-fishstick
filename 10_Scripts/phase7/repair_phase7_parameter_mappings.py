#!/usr/bin/env python3
"""One-time Phase 7 mapping repair; stable IDs and scientific values are unchanged."""

from __future__ import annotations

import csv
import json
import os
import tempfile
from io import StringIO
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
UPDATES = {
    "PAR-B004-0006": ("dimensionless_numbers", "definition"),
    "PAR-B004-0007": ("dimensionless_numbers", "definition"),
    "PAR-B004-0009": ("dimensionless_numbers", "definition"),
    "PAR-B009-0027": ("dimensionless_numbers", "definition"),
    "PAR-B009-0028": ("dimensionless_numbers", "definition"),
    "PAR-B009-0029": ("dimensionless_numbers", "definition"),
    "PAR-B009-0030": ("dimensionless_numbers", "definition"),
    "PAR-B028-0035": ("dimensionless_numbers", "definition"),
    "PAR-B028-0036": ("dimensionless_numbers", "definition"),
    "PAR-C024-0015": ("droplet_response", "evaporation_time"),
    "PAR-A026-0005": ("dimensionless_numbers", "definition"),
    "PAR-A030-0003": ("interaction_geometry", "jet_overlap_description"),
    "PAR-A030-0005": ("process_context", "model_applicability_note"),
}


def atomic(path: Path, text: str) -> None:
    fd, temp = tempfile.mkstemp(prefix=path.name + ".", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="") as handle:
            handle.write(text)
        os.replace(temp, path)
    except Exception:
        Path(temp).unlink(missing_ok=True)
        raise


def update_parameter_list(records: list[dict[str, object]], changes: dict[str, tuple[str, str]]) -> set[str]:
    found: set[str] = set()
    for row in records:
        record_id = str(row["parameter_record_id"])
        if record_id in changes:
            row["parameter_group"], row["parameter_name"] = changes[record_id]
            found.add(record_id)
    return found


def main() -> None:
    master = ROOT / "05_Data_Extraction/master_tables/parameter_master.csv"
    with master.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        header = list(reader.fieldnames or [])
        records = list(reader)
    found = update_parameter_list(records, UPDATES)
    if found != set(UPDATES):
        raise ValueError(f"master mapping targets missing: {sorted(set(UPDATES) - found)}")
    buffer = StringIO(newline="")
    writer = csv.DictWriter(buffer, fieldnames=header, lineterminator="\n")
    writer.writeheader()
    writer.writerows(records)
    atomic(master, buffer.getvalue())

    by_paper: dict[str, dict[str, tuple[str, str]]] = {}
    for record_id, update in UPDATES.items():
        paper_id = record_id.split("-")[1]
        by_paper.setdefault(paper_id, {})[record_id] = update
    for paper_id, changes in by_paper.items():
        path = ROOT / "05_Data_Extraction/per_paper" / f"{paper_id}.json"
        payload = json.loads(path.read_text(encoding="utf-8"))
        found = update_parameter_list(payload["parameters"], changes)
        if found != set(changes):
            raise ValueError(f"{paper_id}: per-paper mapping targets missing")
        atomic(path, json.dumps(payload, ensure_ascii=False, indent=2) + "\n")

    # Keep source configs reproducible by matching records on their stable
    # post-expansion order (the builder's documented ID convention).
    for config_name in ("batch1.json", "batch2.json", "batch3.json"):
        path = ROOT / "10_Scripts/phase7/configs" / config_name
        payload = json.loads(path.read_text(encoding="utf-8"))
        changed = 0
        for paper in payload["papers"]:
            expanded: list[dict[str, object]] = []
            for raw in paper.get("parameters", []):
                variants = raw.get("for_each")
                if variants:
                    expanded.extend([raw] * len(variants))
                else:
                    expanded.append(raw)
            for number, raw in enumerate(expanded, start=1):
                record_id = f"PAR-{paper['paper_id']}-{number:04d}"
                if record_id in UPDATES:
                    raw["parameter_group"], raw["parameter_name"] = UPDATES[record_id]
                    changed += 1
        if changed:
            atomic(path, json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"updated_stable_ids": sorted(UPDATES), "scientific_values_changed": 0}, indent=2))


if __name__ == "__main__":
    main()
