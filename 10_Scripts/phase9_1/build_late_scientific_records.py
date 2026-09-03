#!/usr/bin/env python3
"""Run the validated Phase-7 record builder for late Tier-2/Tier-3 PDFs.

The underlying builder owns the Schema 1.1 row construction and FK checks.
This adapter changes only tier-specific eligibility, labels, and output paths.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import tempfile
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "10_Scripts/phase7/build_tier1_scientific_records.py"


def load_base():
    spec = importlib.util.spec_from_file_location("phase7_record_builder", BASE)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load {BASE}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("tier", choices=("tier2", "tier3"))
    parser.add_argument("config", type=Path)
    parser.add_argument("--validate-only", action="store_true")
    args = parser.parse_args()

    config = json.loads(args.config.read_text(encoding="utf-8"))
    if config.get("reading_tier") != args.tier:
        raise ValueError("Config reading_tier does not match command tier")

    base = load_base()
    base.EVIDENCE_ROOT = ROOT / f"06_Evidence_Base/evidence_cards/{args.tier}"
    base.MECHANISM_TABLE = base.EVIDENCE_ROOT / f"{args.tier}_mechanism_relations.csv"
    base.NOTE_HEADINGS[1] = f"{args.tier.title()} Role"

    # Late-backfill configs use named note fields to remain auditable without
    # duplicating the 23-heading protocol boilerplate in every JSON record.
    generic = {
        "Bibliographic Identity": "Identity verified against the local PDF and canonical library record.",
        f"{args.tier.title()} Role": f"Late-PDF backfill; frozen {args.tier} assignment retained.",
        "Reported vs Derived vs Inferred": "Only source-reported values and explicitly labelled author interpretations are recorded; no project-side numerical inference was added.",
        "Parameter-Schema Gaps": "No schema change proposed during late backfill.",
        "Reading Completion Checklist": "Local PDF identity, machine-readable layer, targeted scientific reading, source locators, structured extraction, note, and evidence card completed.",
    }
    for paper in config["papers"]:
        fields = {**generic, **paper.pop("note_fields", {})}
        paper["note_sections"] = [fields.get(heading, "NR for this paper or outside the tier-specific extraction scope.") for heading in base.NOTE_HEADINGS]

    original_prepare = base.prepare_paper
    original_payload = base.per_paper_payload
    original_render_evidence = base.render_evidence

    def ensure_allowed(paper, master, tiers):
        paper_id = paper["paper_id"]
        if paper_id not in master or paper_id not in tiers:
            raise ValueError(f"{paper_id}: missing canonical records")
        if master[paper_id]["source_record_id"] != paper["source_record_id"]:
            raise ValueError(f"{paper_id}: source_record_id mismatch")
        if master[paper_id]["library_primary"] != paper["library"]:
            raise ValueError(f"{paper_id}: library mismatch")
        if tiers[paper_id]["reading_tier"] != args.tier or tiers[paper_id]["reading_status"] != "not_started":
            raise ValueError(f"{paper_id}: not an unprocessed {args.tier} paper")
        processed = ROOT / "03_Paper_Processed" / paper["library"] / paper_id
        required = {"metadata.json", "text.md", "sections.json", "page_map.csv", "processing_log.json"}
        if not processed.is_dir() or not required.issubset({p.name for p in processed.iterdir()}):
            raise ValueError(f"{paper_id}: incomplete machine-readable layer")

    def prepare(paper, headers):
        item = original_prepare(paper, headers)
        for row in item["parameters"]:
            row["reading_tier"] = args.tier
        return item

    def payload(item):
        result = original_payload(item)
        result["reading_tier"] = args.tier
        result[f"{args.tier}_role"] = result.pop("tier1_role")
        return result

    def render_evidence(item):
        return original_render_evidence(item).replace("Tier 1 Evidence Card", f"{args.tier.title()} Evidence Card", 1)

    base.ensure_allowed_paper = ensure_allowed
    base.prepare_paper = prepare
    base.per_paper_payload = payload
    base.render_evidence = render_evidence
    temp_path = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w", encoding="utf-8", suffix=".json", prefix="expanded_",
            dir=args.config.parent, delete=False,
        ) as handle:
            json.dump(config, handle, ensure_ascii=False, indent=2)
            temp_path = Path(handle.name)
        sys.argv = [str(BASE), str(temp_path)] + (["--validate-only"] if args.validate_only else [])
        base.main()
    finally:
        if temp_path is not None:
            temp_path.unlink(missing_ok=True)


if __name__ == "__main__":
    main()
