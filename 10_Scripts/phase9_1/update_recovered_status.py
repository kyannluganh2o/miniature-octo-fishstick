#!/usr/bin/env python3
"""Reconcile recovered Phase 9.1 PDFs before tier-conformant processing.

The script updates only explicitly approved recovered records. It requires the
live inventory to report one readable, identity-matched PDF and never touches
02_PDF_Raw. Existing non-target rows are preserved byte-for-byte as parsed CSV
records and remain in their original order.
"""

from __future__ import annotations

import argparse
import csv
import os
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
MASTER_PATH = ROOT / "01_Library/master/library_master.csv"
TIERS_PATH = ROOT / "00_Project/reading_tiers.csv"
INVENTORY_PATH = ROOT / "11_QC/missing_pdf/pdf_inventory.csv"
SNAPSHOT = ROOT / "99_Archive/old_versions/Phase9_1_pre_late_pdf_backfill"


RECOVERED = {
    "A001": dict(title="The Effects of High-Pressure Injection on a Compression-Ignition, Direct Injection of Natural Gas Engine", authors="G. P. McTaggart-Cowan; H. L. Jones; S. N. Rogak; W. K. Bushe; P. G. Hill; S. R. Munshi", first_author="McTaggart-Cowan", year="2007", journal="Journal of Engineering for Gas Turbines and Power", doi_status="verified"),
    "A002": dict(title="Direct Injection of Natural Gas at up to 600 Bar in a Pilot-Ignited Heavy-Duty Engine", authors="Gordon McTaggart-Cowan; Ken Mann; Jian Huang; Ashish Singh; Bronson Patychuk; Zheng Xiong Zheng; Sandeep Munshi", first_author="McTaggart-Cowan", year="2015", journal="SAE International Journal of Engines", doi_status="verified"),
    "A005": dict(title="Combustion and Emissions of Paired-Nozzle Jets in a Pilot-Ignited Direct-Injection Natural Gas Engine", authors="Christopher W. J. Mabson; Ehsan Faghani; Pooyan Kheirkhah; Patrick Kirchen; Steven N. Rogak; Gordon McTaggart-Cowan", first_author="Mabson", year="2016", journal="SAE Technical Paper", doi_status="verified"),
    "A006": dict(title="Effect of Injection Strategies on Emissions from a Pilot-Ignited Direct-Injection Natural-Gas Engine - Part II: Slightly Premixed Combustion", authors="Ehsan Faghani; Pooyan Kheirkhah; Christopher W. J. Mabson; Gordon McTaggart-Cowan; Patrick Kirchen; Steve Rogak", first_author="Faghani", year="2017", journal="SAE Technical Paper", doi_status="verified"),
    "A007": dict(title="Influence of the Spatial and Temporal Interaction Between Diesel Pilot and Directly Injected Natural Gas Jet on Ignition and Combustion Characteristics", authors="Georg Fink; Michael Jud; Thomas Sattelmayer", first_author="Fink", year="2018", journal="Journal of Engineering for Gas Turbines and Power", doi_status="verified"),
    "A008": dict(title="Numerical Analysis of the Combustion Process in Dual-Fuel Engines With Direct Injection of Natural Gas", authors="Michael Jud; Christoph Wieland; Georg Fink; Thomas Sattelmayer", first_author="Jud", year="2018", journal="", doi_status="unverified"),
    "A009": dict(title="Fundamental Study of Diesel-Piloted Natural Gas Direct Injection Under Different Operating Conditions", authors="Georg Fink; Michael Jud; Thomas Sattelmayer", first_author="Fink", year="2019", journal="Journal of Engineering for Gas Turbines and Power", doi_status="verified"),
    "A011": dict(title="Parametric study of pilot-ignited direct-injection natural gas combustion in an optically accessible heavy-duty engine", authors="Jeremy Rochussen; Gordon McTaggart-Cowan; Patrick Kirchen", first_author="Rochussen", year="2020", journal="International Journal of Engine Research", doi_status="verified"),
    "A012": dict(title="The Interaction Between the Pilot Diesel and Main NG Injection in an HPDI Engine", authors="N. Diepstraten; X. L. J. Seykens; L. M. T. Somers", first_author="Diepstraten", year="2021", journal="", doi_status="unverified"),
    "B006": dict(title="Transient High-Pressure Hydrogen Jet Measurements", authors="B. R. Petersen; J. B. Ghandhi", first_author="Petersen", year="2006", journal="SAE Technical Paper", doi_status="unverified"),
    "B008": dict(title="A Numerical Analysis of Hydrogen Underexpanded Jets Under Real Gas Assumption", authors="Francesco Bonelli; Annarita Viggiano; Vinicio Magi", first_author="Bonelli", year="2013", journal="Journal of Fluids Engineering", doi_status="verified"),
    "B018": dict(title="Under-Expanded Gaseous Jets Characterization for Application in Direct Injection Engines: Experimental and Numerical Approach", authors="Luigi Allocca; Alessandro Montanaro; Giovanni Meccariello", first_author="Allocca", year="2020", journal="SAE Technical Paper", doi_status="verified"),
    "B021": dict(title="Numerical characterization of hydrogen under-expanded jets with a focus on Internal Combustion Engines applications", authors="Giuseppe Anaclerio; Tommaso Capurso; Marco Torresi; Sergio Mario Camporeale", first_author="Anaclerio", year="2023", journal="International Journal of Engine Research", doi_status="verified"),
    "C005": dict(title="Secondary breakup of a drop at moderate Weber numbers", authors="Mohit Jain; R. Surya Prakash; Gaurav Tomar; R. V. Ravikrishna", first_author="Jain", year="2015", journal="Proceedings of the Royal Society A", doi_status="verified"),
    "C011": dict(title="Numerical Study on Liquid Droplet Internal Flow Under Shock Impact", authors="Ben Guan; Yao Liu; Chih-Yung Wen; Hua Shen", first_author="Guan", year="2018", journal="AIAA Journal", doi_status="verified"),
    "C029": dict(title="Numerical study of the transcritical shock-droplet interaction", authors="Bradley Boyd; Dorrin Jarrahbashi", first_author="Boyd", year="2021", journal="Physical Review Fluids", doi_status="verified"),
    "C036": dict(title="Shock-induced aerobreakup of parallel-arranged droplets", authors="Jianfeng Guo; Peng Kang; Kai Mu; Ting Si", first_author="Guo", year="2026", journal="Physical Review Fluids", doi_status="verified"),
    "D001": dict(title="Effect of Ambient Temperature and Density on Shock Wave Generation in a Diesel Engine", authors="Sanghoon Kook; Lyle M. Pickett", first_author="Kook", year="2010", journal="Atomization and Sprays", doi_status="unverified"),
    "D019": dict(title="Comparative analysis of detonation and shock waves interacting with droplets: Characteristics and mechanisms", authors="Hanbing Zou; Xin Jin; Haotian Chen; Wei Wang; Sheng Xu; Bing Wang", first_author="Zou", year="2026", journal="Physical Review Fluids", doi_status="verified"),
}

TIER_IDS = {
    "tier1": ["A007", "B021", "C029", "D019"],
    "tier2": ["A002", "A005", "A009", "A011", "A012", "B008", "C036"],
    "tier3": ["A001", "A006", "A008", "B006", "B018", "C005", "C011", "D001"],
}


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        return list(reader.fieldnames or []), list(reader)


def atomic_write(path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    fd, name = tempfile.mkstemp(prefix=path.name + ".", suffix=".tmp", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=fields)
            writer.writeheader()
            writer.writerows(rows)
        os.replace(name, path)
    except Exception:
        try:
            os.unlink(name)
        except FileNotFoundError:
            pass
        raise


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("tier", choices=sorted(TIER_IDS))
    args = parser.parse_args()
    if not SNAPSHOT.is_dir():
        raise RuntimeError("Required Phase 9.1 pre-backfill snapshot is missing")

    inv_fields, inv_rows = read_csv(INVENTORY_PATH)
    del inv_fields
    inventory = {row["paper_id"]: row for row in inv_rows}
    master_fields, master_rows = read_csv(MASTER_PATH)
    tier_fields, tier_rows = read_csv(TIERS_PATH)
    master = {row["paper_id"]: row for row in master_rows}
    tiers = {row["paper_id"]: row for row in tier_rows}

    for paper_id in TIER_IDS[args.tier]:
        inv = inventory[paper_id]
        row = master[paper_id]
        tier = tiers[paper_id]
        if tier["reading_tier"] != args.tier or row["reading_tier"] != args.tier:
            raise RuntimeError(f"{paper_id}: frozen tier conflict")
        if not (inv["file_exists"] == "yes" and inv["pdf_readable"] == "yes" and inv["pdf_match_status"] == "matched"):
            raise RuntimeError(f"{paper_id}: live PDF is not readable and identity-matched")
        if tier["reading_status"] not in {"blocked_missing_pdf", "not_started"}:
            raise RuntimeError(f"{paper_id}: unexpected pre-processing status {tier['reading_status']}")

        row.update(RECOVERED[paper_id])
        row.update({
            "pdf_status": "downloaded",
            "pdf_filename": inv["current_filename"],
            "pdf_relpath": inv["current_relpath"],
            "pdf_match_status": "matched",
            "verification_flags": "local_pdf_identity_verified",
            "date_updated": "2026-09-01",
        })
        marker = "Phase 9.1 late PDF recovered and identity-verified from the local original PDF."
        if marker not in row.get("notes", ""):
            row["notes"] = (row.get("notes", "").rstrip() + " " + marker).strip()
        tier.update({
            "pdf_status": "downloaded",
            "reading_status": "not_started",
            "notes": "Phase 9.1 late-PDF identity verification passed; tier-conformant processing not started.",
        })

    atomic_write(MASTER_PATH, master_fields, master_rows)
    atomic_write(TIERS_PATH, tier_fields, tier_rows)
    print(f"Prepared {len(TIER_IDS[args.tier])} recovered {args.tier} records")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
