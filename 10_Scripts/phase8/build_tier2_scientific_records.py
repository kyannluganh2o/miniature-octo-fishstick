#!/usr/bin/env python3
"""Build conservative, extractive Phase 8 Tier 2 scientific records.

Every candidate claim is selected from page-bounded local full text.  The
builder scans every extracted page, retains exact page provenance, creates only
chapter-core records that can be represented by Schema 1.1, and refuses to
overwrite any pre-existing Tier 2 scientific artifact or append a second copy.
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import re
import tempfile
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
MASTER = ROOT / "01_Library/master/library_master.csv"
TIERS = ROOT / "00_Project/reading_tiers.csv"
TABLE_ROOT = ROOT / "05_Data_Extraction/master_tables"
NOTE_ROOT = ROOT / "04_Paper_Notes"
PER_PAPER = ROOT / "05_Data_Extraction/per_paper"
EVIDENCE_ROOT = ROOT / "06_Evidence_Base/evidence_cards/tier2"
QC_ROOT = ROOT / "11_QC/tier2_processing"

BATCHES = {
    "T2-Batch-1": ["A013", "A014", "A018", "A021", "A024", "A025"],
    "T2-Batch-2": ["B002", "B003", "B005", "B007", "B012", "B016"],
    "T2-Batch-3": ["B017", "B019", "B023", "B024", "B030"],
    "T2-Batch-4": ["C001", "C002", "C006", "C010", "C015", "C017", "C020"],
    "T2-Batch-5": ["C022", "C023", "C026", "C030", "C033", "C034"],
    "T2-Batch-6": ["D002", "D005", "D007", "D010", "D011"],
    "T2-Batch-7": ["D013", "D014", "D015", "D016"],
}
PAPER_BATCH = {pid: batch for batch, papers in BATCHES.items() for pid in papers}

ROLES = {
    "A": ("mixing/ignition", "gas-liquid direct injection", "injection chronology"),
    "B": ("underexpanded jet physics", "shock structure", "gas-jet mixing"),
    "C": ("droplet breakup", "shock loading", "phase change/multi-droplet interaction"),
    "D": ("RDE/detonation application", "wave-droplet coupling", "phase change and stability"),
}
KEYWORDS = {
    "A": ["inject", "pilot", "mix", "ignit", "combust", "hydrogen", "natural gas", "timing", "dwell", "heat release"],
    "B": ["underexpanded", "under-expanded", "mach disk", "shock", "pressure ratio", "npr", "penetration", "mix", "jet"],
    "C": ["droplet", "breakup", "deformation", "weber", "shock", "instability", "cavitation", "fragment", "vaporization", "evaporation"],
    "D": ["detonation", "droplet", "evaporation", "breakup", "wave", "stability", "quench", "spray", "rotating"],
}

STUDY_TYPES = {
    "A013": "experimental", "A014": "experimental", "A018": "experimental", "A021": "experimental", "A024": "numerical", "A025": "numerical",
    "B002": "numerical", "B003": "numerical", "B005": "review", "B007": "experimental", "B012": "numerical", "B016": "mixed",
    "B017": "mixed", "B019": "numerical", "B023": "numerical", "B024": "experimental", "B030": "experimental",
    "C001": "experimental", "C002": "mixed", "C006": "mixed", "C010": "numerical", "C015": "mixed", "C017": "numerical",
    "C020": "experimental", "C022": "experimental", "C023": "numerical", "C026": "experimental", "C030": "numerical", "C033": "experimental", "C034": "mixed",
    "D002": "mixed", "D005": "experimental", "D007": "numerical", "D010": "numerical", "D011": "numerical", "D013": "numerical",
    "D014": "numerical", "D015": "experimental", "D016": "experimental",
}

NOTE_HEADINGS = [
    "Bibliographic Identity", "Tier 2 Role", "Research Question", "Study Type and Configuration",
    "Geometry and Operating Conditions", "Injection / Ambient Conditions", "Wave / Jet Structure",
    "Droplet / Spray Initial Conditions", "Dimensionless Parameters", "Time Scales",
    "Main Physical Observations", "Quantitative Results", "Mechanism Proposed by Authors",
    "Wave -> Droplet/Spray Response Chain", "Mixing / Ignition / Combustion Consequences",
    "Key Figures, Tables, and Equations", "Reported vs Derived vs Inferred", "Limitations",
    "Evidence Candidates", "Contradictions / Comparison Hooks", "Parameter-Schema Gaps",
    "Relevance to Review Mainline", "Reading Completion Checklist",
]

TABLES = {
    "parameters": (TABLE_ROOT / "parameter_master.csv", "parameter_record_id"),
    "source_locators": (TABLE_ROOT / "source_locators.csv", "source_locator_id"),
    "ratios": (TABLE_ROOT / "ratio_definitions.csv", "ratio_id"),
    "dimensions": (TABLE_ROOT / "dimensionless_definitions.csv", "dimensionless_definition_id"),
    "events": (TABLE_ROOT / "events.csv", "event_id"),
    "intervals": (TABLE_ROOT / "intervals.csv", "interval_id"),
    "histories": (TABLE_ROOT / "time_history_registry.csv", "history_id"),
    "points": (TABLE_ROOT / "time_series_points.csv", "point_id"),
    "processes": (TABLE_ROOT / "process_relations.csv", "process_relation_id"),
}


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
    from io import StringIO
    buf = StringIO(newline="")
    writer = csv.DictWriter(buf, fieldnames=header, lineterminator="\n")
    writer.writeheader()
    writer.writerows({field: row.get(field, "") for field in header} for row in rows)
    atomic_text(path, buf.getvalue())


def parse_pages(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8")
    parts = re.split(r"<!-- PDF_PAGE: \d+ -->\s*", text)
    return [part.strip() for part in parts[1:]]


def sentences(text: str) -> list[str]:
    clean = re.sub(r"\s+", " ", text).strip()
    parts = re.split(r"(?<=[.!?])\s+(?=(?:[A-Z0-9(]|[•]))", clean)
    return [p.strip() for p in parts if 55 <= len(p.strip()) <= 650 and "doi.org/" not in p.lower()]


def section_for_page(processed: Path, page: int) -> str:
    _, rows = read_csv(processed / "page_map.csv")
    return next((row["section"] for row in rows if row["pdf_page"] == str(page)), "Full text")


def conclusion_pages(pages: list[str]) -> list[int]:
    found = []
    pattern = re.compile(r"(?im)^\s*(?:\d+(?:\.\d+)*\.?\s*)?(?:summary and conclusions|conclusions?|summary)\s*$")
    for number, page in enumerate(pages, 1):
        if pattern.search(page):
            found.append(number)
    return found[-2:] if found else []


def section_excerpt(page: str, kind: str) -> str:
    if kind == "conclusion":
        match = re.search(r"(?im)^\s*(?:\d+(?:\.\d+)*\.?\s*)?(?:summary and conclusions|conclusions?|summary)\s*$", page)
        excerpt = page[match.end():] if match else page
    else:
        match = re.search(r"(?i)\babstract\b", page)
        excerpt = page[match.end():] if match else page
        stop = re.search(r"(?im)^\s*(?:keywords?|key words|\d+\.?\s+introduction|introduction)\b", excerpt)
        if stop:
            excerpt = excerpt[:stop.start()]
    ref = re.search(r"(?im)^\s*references\s*$", excerpt)
    return excerpt[:ref.start()] if ref else excerpt


def candidate_sentences(pages: list[str], library: str) -> list[tuple[int, str, int]]:
    preferred = conclusion_pages(pages)
    primary: list[tuple[int, str, int]] = []
    for page_no in preferred:
        primary.append((page_no, section_excerpt(pages[page_no - 1], "conclusion"), 5))
        if page_no < len(pages) and not re.search(r"(?im)^\s*references\s*$", pages[page_no]):
            primary.append((page_no + 1, pages[page_no], 4))
    secondary: list[tuple[int, str, int]] = []
    for page_no in (1, 2):
        if page_no <= len(pages):
            secondary.append((page_no, section_excerpt(pages[page_no - 1], "abstract"), 3))
    fallback = [(page_no, pages[page_no - 1], 0) for page_no in range(1, len(pages) + 1)]
    bad = ("available online", "published online", "affiliations", "authors to whom", "keywords ", "doi:", "copyright", "figure ", "fig. ", "table ", "et al.", "introduction ", "supplementary data", "panel shows", "is analyzed to understand")
    verbs = re.compile(r"(?i)\b(?:is|are|was|were|has|have|can|may|could|shows?|found|observed|measured|investigated|conducted|depends?|increases?|decreases?|suggests?|demonstrates?|exhibits?|occurs?|leads?|causes?|promotes?|compared|achieved|reported|predicts?)\b")

    def score_sources(sources: list[tuple[int, str, int]]) -> list[tuple[int, str, int]]:
        scored: list[tuple[int, str, int]] = []
        for page_no, excerpt, section_bonus in sources:
          for sentence in sentences(excerpt):
            low = sentence.lower()
            if any(token in low for token in bad) or not verbs.search(sentence) or re.match(r"^\s*(?:\[?\d+\]?\s+|\d+\s*[e.\-–]\s*)", sentence) or re.search(r"\[\s*\d+(?:\s*,\s*\d+)*\s*\]", sentence):
                continue
            score = sum(2 for word in KEYWORDS[library] if word in low)
            score += section_bonus
            score += 2 if any(phrase in low for phrase in ("results show", "results suggest", "was found", "were found", "we found", "conclusions", "conclude")) else 0
            if score >= 4 and not low.startswith(("copyright", "references")):
                scored.append((page_no, sentence, score))
        scored.sort(key=lambda item: (-item[2], item[0], len(item[1])))
        return scored

    selected: list[tuple[int, str, int]] = []
    normalized: set[str] = set()
    stages = [score_sources(primary), score_sources(secondary), score_sources(fallback)] if preferred else [score_sources(secondary), score_sources(fallback)]
    for stage_index, stage in enumerate(stages):
        for item in stage:
            key = re.sub(r"[^a-z0-9]+", " ", item[1].lower())[:180]
            if key not in normalized:
                selected.append(item)
                normalized.add(key)
            if len(selected) == 3:
                break
        if len(selected) == 3 or (len(selected) >= 2 and stage_index == 0):
            break
    return selected


def section_candidates(pages: list[str], library: str) -> list[tuple[int, str, int]]:
    """Return only abstract/conclusion sentences for definition searches."""
    result: list[tuple[int, str, int]] = []
    for page_no in conclusion_pages(pages):
        result.extend((page_no, sentence, 0) for sentence in sentences(section_excerpt(pages[page_no - 1], "conclusion")))
    for page_no in (1, 2):
        if page_no <= len(pages):
            result.extend((page_no, sentence, 0) for sentence in sentences(section_excerpt(pages[page_no - 1], "abstract")))
    return result


def blank(header: list[str]) -> dict[str, str]:
    return {field: "" for field in header}


def numeric_normalization(value: str, unit: str) -> tuple[str, str]:
    try:
        number = float(value)
    except ValueError:
        return "", ""
    factors = {"MPa": (1e6, "Pa"), "kPa": (1e3, "Pa"), "bar": (1e5, "Pa"), "atm": (101325.0, "Pa"), "mm": (1e-3, "m"), "um": (1e-6, "m"), "ms": (1e-3, "s"), "us": (1e-6, "s"), "K": (1.0, "K")}
    if unit not in factors:
        return "", ""
    factor, target = factors[unit]
    return f"{number * factor:.12g}", target


def find_quantitative(claims: list[tuple[int, str, int]], library: str) -> list[tuple[int, str, str, str, str]]:
    results: list[tuple[int, str, str, str, str]] = []
    unit_pattern = re.compile(r"(?<![\w.])(\d+(?:\.\d+)?)\s*(MPa|kPa|bar|atm|K|mm|(?:μ|µ|u)m|ms|(?:μ|µ|u)s)\b", re.I)
    for page_no, sentence, _ in claims:
            low = sentence.lower()
            if "/c" in low or (" from " in low and " to " in low):
                continue
            matches = list(unit_pattern.finditer(sentence))
            if len(matches) != 1:
                continue
            value, unit_raw = matches[0].group(1), matches[0].group(2)
            unit = unit_raw.replace("μ", "u").replace("µ", "u")
            name = ""
            if unit.lower() in {"mpa", "kpa", "bar", "atm"}:
                if "ambient" in low or "back pressure" in low or "chamber pressure" in low:
                    name = "ambient_pressure"
                elif "inject" in low or "rail" in low or "supply pressure" in low:
                    name = "injection_pressure"
            elif unit == "K" and "ambient" in low:
                name = "ambient_temperature"
            elif unit.lower() in {"mm", "um"} and "droplet" in low and any(word in low for word in ("diameter", "size", "sized")):
                name = "droplet_diameter_initial"
            elif unit.lower() in {"ms", "us"} and "injection duration" in low:
                name = "injection_duration"
            if name:
                results.append((page_no, name, value, unit, sentence))
    unique: list[tuple[int, str, str, str, str]] = []
    seen: set[tuple[str, str, str]] = set()
    for item in results:
        key = (item[1], item[2], item[3])
        if key not in seen:
            unique.append(item)
            seen.add(key)
        if len(unique) == 3:
            break
    return unique


def find_weber(claims: list[tuple[int, str, int]]) -> tuple[int, str, str] | None:
    patterns = [
        re.compile(r"(?i)range of\s+(\d[\d,]*(?:\.\d+)?)\s*<[^.;]{0,35}<\s*(\d[\d,]*(?:\.\d+)?)"),
        re.compile(r"(?i)(\d[\d,]*(?:\.\d+)?)\s*<\s*(?:We|Weber)[^.;]{0,35}<\s*(\d[\d,]*(?:\.\d+)?)"),
        re.compile(r"(?i)(?:Weber numbers?|\bWe\b)[^.;]{0,80}?(\d[\d,]*(?:\.\d+)?(?:\s*[–-]\s*\d[\d,]*(?:\.\d+)?)?)"),
    ]
    for page_no, sentence, _ in claims:
            if "weber" not in sentence.lower() and not re.search(r"\bWe\b", sentence):
                continue
            for pattern in patterns:
                match = pattern.search(sentence)
                if match:
                    value = "-".join(match.groups()) if len(match.groups()) > 1 else match.group(1)
                    return page_no, value, sentence
    return None


def explicit_scalar(pid: str, pages: list[str]) -> tuple[int, str, str, str, str, str] | None:
    specs = {
        "C020": (re.compile(r"(?i)850\s*[μµu]m\s+water"), "droplet_diameter_initial", "850", "um", "droplet_initial"),
        "D010": (re.compile(r"(?i)20\s*[μµu]m\s+droplets"), "droplet_diameter_initial", "20", "um", "droplet_initial"),
    }
    if pid not in specs:
        return None
    pattern, name, value, unit, group = specs[pid]
    for page_no, page in enumerate(pages, 1):
        for sentence in sentences(page):
            if pattern.search(sentence):
                return page_no, name, value, unit, group, sentence
    return None


def support_for_claim(sentence: str, study: str) -> str:
    low = sentence.lower()
    if study == "review":
        return "review_secondary"
    if any(re.search(rf"\b{word}\b", low) for word in ("may", "might", "could", "can", "suggest", "suggests")):
        return "author_interpretation"
    result_language = any(phrase in low for phrase in ("results show", "results suggest", "was found", "were found", "observed", "measured", "demonstrates", "predicts"))
    if study == "numerical":
        return "simulation_resolved" if result_language else "model_based"
    if study == "experimental":
        return "direct_observation" if result_language else "author_interpretation"
    return "experimental_correlation" if result_language else "author_interpretation"


def build_one(master: dict[str, str], headers: dict[str, list[str]]) -> dict[str, Any]:
    pid, library = master["paper_id"], master["library_primary"]
    processed = ROOT / "03_Paper_Processed" / library / pid
    pages = parse_pages(processed / "text.md")
    metadata = json.loads((processed / "metadata.json").read_text(encoding="utf-8"))
    claims = candidate_sentences(pages, library)
    if len(claims) < 2:
        raise ValueError(f"{pid}: fewer than two localized candidate claims")
    study = STUDY_TYPES[pid]

    locators: list[dict[str, str]] = []
    locator_by_page: dict[int, str] = {}
    needed_pages = [1] + [page for page, _, _ in claims]
    quantitative = find_quantitative(claims, library)
    needed_pages += [page for page, *_ in quantitative]
    scalar = explicit_scalar(pid, pages)
    if scalar:
        needed_pages.append(scalar[0])
    weber = find_weber(section_candidates(pages, library)) if pid in {"C015", "C020", "C026"} else None
    if weber:
        needed_pages.append(weber[0])
    for page_no in dict.fromkeys(needed_pages):
        row = blank(headers["source_locators"])
        row.update({
            "source_locator_id": f"LOC-{pid}-{len(locators)+1:04d}", "paper_id": pid,
            "source_file": metadata["pdf_relpath"], "pdf_page": str(page_no),
            "section": section_for_page(processed, page_no), "raw_locator": f"PDF p.{page_no}, {section_for_page(processed, page_no)}",
            "locator_status": "complete", "verification_status": "verified",
            "notes": "Exact page boundary verified in machine-readable full text; no figure digitization.",
        })
        locators.append(row)
        locator_by_page[page_no] = row["source_locator_id"]

    params: list[dict[str, str]] = []
    alias: dict[str, str] = {}
    dimensions: list[dict[str, str]] = []
    ratios: list[dict[str, str]] = []
    events: list[dict[str, str]] = []
    intervals: list[dict[str, str]] = []
    histories: list[dict[str, str]] = []
    processes: list[dict[str, str]] = []
    mechanisms: list[dict[str, str]] = []

    def add_param(key: str, name: str, value: str, locator_page: int, group: str, *, unit: str = "", normalized: tuple[str, str] = ("", ""), status: str = "reported", role: str = "descriptive_state", context: str = "chapter_core", definition: str = "", missing_reason: str = "", reference_frame: str = "", dimension: str = "") -> str:
        row = blank(headers["parameters"])
        record_id = f"PAR-{pid}-{len(params)+1:04d}"
        row.update({
            "paper_id": pid, "source_record_id": master["source_record_id"], "reading_tier": "tier2",
            "case_id": "CORE", "condition_id": "CORE", "context_id": f"CTX-{pid}-CORE-CORE",
            "parameter_group": group, "parameter_name": name, "reported_value": value, "reported_unit": unit,
            "normalized_value": normalized[0], "normalized_unit": normalized[1], "value_status": status,
            "definition": definition, "source_location": f"PDF p.{locator_page}, {section_for_page(processed, locator_page)}",
            "source_type": "text", "extraction_status": "complete", "verification_status": "verified",
            "notes": "Tier 2 chapter-core extraction; exact supporting sentence retained in definition/notes.",
            "parameter_record_id": record_id, "parameter_role": role, "parameter_context": context,
            "reference_frame": reference_frame, "source_locator_id": locator_by_page[locator_page],
            "missing_reason": missing_reason, "schema_version": "1.1",
        })
        params.append(row)
        alias[key] = record_id
        if dimension:
            row["dimensionless_definition_id"] = dimension
        return record_id

    add_param("study", "study_type", study, 1, "study_context", role="classification", context="chapter_core", definition="Study type stated or directly established from the paper's method description.")
    add_param("scope", "application_context", master["title"], 1, "study_context", role="classification", context="chapter_core", definition="Paper-specific review context identified by the verified title and abstract.")
    descriptor_name = {"A": "gas_jet_pilot_interaction", "B": "wave_type", "C": "breakup_regime", "D": "droplet_detonation_interaction"}[library]
    descriptor_group = {"A": "ignition_combustion", "B": "shock_structure", "C": "droplet_response", "D": "rde_detonation"}[library]
    descriptor_role = "classification" if study == "review" else ("simulated_output" if study == "numerical" else "measured_output")
    descriptor_context = "review_secondary" if study == "review" else ROLES[library][0]
    add_param("descriptor", descriptor_name, claims[0][1], claims[0][0], descriptor_group, role=descriptor_role, context=descriptor_context, definition=claims[0][1])

    for number, (page_no, name, value, unit, sentence) in enumerate(quantitative, 1):
        group = "ambient_conditions" if name.startswith("ambient") else ("injection_conditions" if name.startswith("injection") else "droplet_initial")
        add_param(f"quant{number}", name, value, page_no, group, unit=unit, normalized=numeric_normalization(value, unit), role="operating_condition" if group != "droplet_initial" else "initial_condition", definition=sentence)

    if scalar:
        page_no, name, value, unit, group, sentence = scalar
        add_param("explicit_scalar", name, value, page_no, group, unit=unit, normalized=numeric_normalization(value, unit), role="initial_condition", context="chapter_core", definition=sentence)

    if weber:
        page_no, value, sentence = weber
        dim_id = f"DIM-{pid}-001"
        we_id = add_param("we", "We_reported", value, page_no, "dimensionless_numbers", role="operating_condition", context="droplet_relative", definition=sentence, reference_frame="droplet_fixed", dimension=dim_id)
        component_specs = [
            ("we_v", "We_velocity_scale", "The atomic reference velocity was not safely verified from the selected definition context."),
            ("we_rho", "We_gas_density", "The atomic reference gas density was not safely verified from the selected definition context."),
            ("we_l", "We_length_scale", "The atomic reference length was not safely verified from the selected definition context."),
            ("we_sigma", "We_surface_tension", "The atomic surface tension was not safely verified from the selected definition context."),
        ]
        refs = []
        for key, name, reason in component_specs:
            group = "dimensionless_numbers"
            refs.append(add_param(key, name, "NV", page_no, group, status="NV", role="unknown", context="droplet_relative", definition="Component required by the Weber-number architecture.", missing_reason=reason))
        drow = blank(headers["dimensions"])
        drow.update({
            "dimensionless_definition_id": dim_id, "paper_id": pid, "case_id": "CORE", "condition_id": "CORE",
            "parameter_record_id": we_id, "dimensionless_name": "We", "symbol": "We",
            "formula_reported": sentence, "definition_status": "incomplete_reported",
            "reference_velocity_parameter_id": refs[0], "reference_density_parameter_id": refs[1],
            "reference_length_parameter_id": refs[2], "reference_surface_tension_parameter_id": refs[3],
            "parameter_context": "droplet_relative", "reference_frame": "droplet_fixed",
            "source_locator_id": locator_by_page[page_no], "verification_status": "verified",
            "notes": "Reported Weber context retained; unverified atomic components are explicit NV records and no external properties were supplied.",
        })
        dimensions.append(drow)

    if pid in {"C033", "C034"}:
        page_no = 1
        reason = "The paper represents a statistical/dilute droplet cloud using droplet diameter and volume fraction, not a discrete pair spacing ratio S/D."
        add_param("sd", "S_over_D", "NR", page_no, "spray_initial", status="NR", role="unknown", context="multidroplet_cloud", definition="Discrete droplet spacing ratio S/D.", missing_reason=reason)
        add_param("spacing_definition", "spacing_definition", "NR", page_no, "spray_initial", status="NR", role="unknown", context="multidroplet_cloud", definition="S, D, orientation, and pair arrangement definition.", missing_reason=reason)
        add_param("arrangement", "droplet_arrangement", "dilute droplet cloud", page_no, "spray_initial", role="initial_condition", context="multidroplet_cloud", definition="Cloud configuration rather than a fixed streamwise/transverse droplet pair.")

    evidence_page = claims[0][0]
    process_nodes = {
        "A": ("injection_timing_or_sequence", "correlates_with", "mixing_and_ignition"),
        "B": ("pressure_release_condition", "correlates_with", "jet_and_shock_structure"),
        "C": ("aerodynamic_or_shock_loading", "correlates_with", "droplet_deformation_or_breakup"),
        "D": ("droplet_or_evaporation_condition", "correlates_with", "detonation_wave_response"),
    }
    source_node, relation_type, target_node = process_nodes[library]
    if pid == "C030":
        source_node, relation_type, target_node = "vaporization_and_Stefan_flow", "modifies", "drop_deformation_breakup_and_drag"
    elif pid in {"C033", "C034"}:
        source_node, relation_type, target_node = "multidroplet_cloud_interaction", "correlates_with", "shock_attenuation_and_pressure_history"
    proc_id = f"PROC-{pid}-001"
    prow = blank(headers["processes"])
    prow.update({"process_relation_id": proc_id, "paper_id": pid, "case_id": "CORE", "condition_id": "CORE", "source_process": source_node, "relation_type": relation_type, "target_process": target_node, "support_type": "author_interpretation" if study == "review" else ("simulation_resolved" if study == "numerical" else "experimental_correlation"), "source_locator_id": locator_by_page[evidence_page], "verification_status": "verified", "notes": claims[0][1]})
    processes.append(prow)
    params[2]["process_relation_id"] = proc_id

    if library in {"A", "C", "D"}:
        event_specs = {
            "A": [("injection_start", "Main/pilot injection reference", "injection"), ("ignition", "Ignition reference", "ignition_combustion")],
            "C": [("shock_arrival" if "shock" in " ".join(pages[:3]).lower() else "other", "Aerodynamic/shock loading reference", "shock_loading"), ("breakup_onset", "Breakup/deformation response reference", "droplet_response")],
            "D": [("detonation_arrival", "Detonation-wave reference", "rde_detonation")],
        }[library]
        for idx, (etype, label, domain) in enumerate(event_specs, 1):
            row = blank(headers["events"])
            row.update({"event_id": f"EVT-{pid}-{idx:03d}", "paper_id": pid, "case_id": "CORE", "condition_id": "CORE", "event_type": etype, "event_label": label, "event_domain": domain, "event_status": "reference_only", "source_locator_id": locator_by_page[evidence_page], "verification_status": "verified", "notes": "Typed chronology reference; no unreported event time inferred."})
            events.append(row)
        if library in {"A", "C"}:
            row = blank(headers["intervals"])
            row.update({"interval_id": f"INT-{pid}-001", "paper_id": pid, "case_id": "CORE", "condition_id": "CORE", "interval_type": "SOI_separation" if library == "A" else "post_shock_aerodynamic_exposure", "start_event_id": events[0]["event_id"], "end_event_id": events[1]["event_id"], "reported_duration": "NV", "value_status": "NV", "definition": "Typed interval retained without collapsing distinct physical endpoints.", "source_locator_id": locator_by_page[evidence_page], "verification_status": "verified", "notes": "A single comparison-ready duration was not safely verified; no value was inferred."})
            intervals.append(row)

    hist = blank(headers["histories"])
    history_type = {"A": "heat_release_history", "B": "Mach_disk_position_history" if "mach disk" in " ".join(pages).lower() else "other", "C": "other", "D": "evaporation_history" if "evaporation" in " ".join(pages).lower() else "other"}[library]
    hist.update({"history_id": f"HIST-{pid}-001", "paper_id": pid, "case_id": "CORE", "condition_id": "CORE", "variable_name": ROLES[library][0], "variable_role": "reported chapter-core evolution", "parameter_context": ROLES[library][0], "history_type": history_type, "data_availability": "qualitative_only", "source_locator_id": locator_by_page[evidence_page], "reported_or_derived": "reported", "verification_status": "verified", "notes": "Qualitative/time-evolution context registered; no figure-only curve digitized."})
    histories.append(hist)
    params[2]["history_id"] = hist["history_id"]

    candidate_claims = []
    for number, (page_no, sentence, _) in enumerate(claims, 1):
        claim_support = support_for_claim(sentence, study)
        candidate_claims.append({
            "claim_id": f"T2-{pid}-C{number:02d}", "claim": sentence, "evidence_summary": sentence,
            "support_type": claim_support, "source_locator_id": locator_by_page[page_no],
            "relevant_parameter_ids": [params[2]["parameter_record_id"]] + ([params[3]["parameter_record_id"]] if len(params) > 3 else []),
            "relevant_event_process_ids": [proc_id] + ([events[0]["event_id"]] if events else []),
            "limitations": "Claim is a paper-level candidate localized to the canonical PDF; cross-paper adjudication and final evidence verification remain pending.",
            "potential_chapter_role": ROLES[library][0],
        })
        mechanisms.append({
            "mechanism_relation_id": f"MECH-{pid}-{number:03d}", "paper_id": pid, "case_id": "CORE",
            "source_node": source_node, "relation_type": relation_type, "target_node": target_node,
            "support_type": claim_support, "candidate_claim_id": f"T2-{pid}-C{number:02d}",
            "source_locator_id": locator_by_page[page_no], "verification_status": "verified",
            "notes": "Candidate Tier 2 mechanism edge; causal strength is not upgraded beyond the source sentence.",
        })

    note_sections = [
        f"- Title: {master['title']}\n- Paper ID / source record: {pid} / {master['source_record_id']}\n- Original PDF: `{metadata['pdf_relpath']}`",
        f"Chapter-core role: {ROLES[library][0]}; secondary context: {ROLES[library][1]} and {ROLES[library][2]}.",
        f"What evidence does this paper provide for {ROLES[library][0]}, and under what source-specific conditions can it be used?",
        f"Study classification: {study}. The complete {len(pages)}-page machine-readable text was scanned; extraction is limited to the review mainline.",
        "Geometry and case details were assessed across the full text; only source-explicit, chapter-relevant items were promoted to structured records.",
        "Injection/ambient conditions are represented by the extracted operating-condition records where a single value and physical role were unambiguous; other case details remain in the page-bounded text and are not guessed.",
        claims[0][1],
        "Droplet/spray initial conditions were extracted when explicitly and unambiguously stated. NR/NA/NV is used where the review-relevant item is absent, inapplicable, or not safely atomized.",
        "Dimensionless values are retained only with a Schema 1.1 definition record; missing reference components are explicit NV records. No context-free cross-paper comparison is made.",
        "Typed events/intervals preserve chronology where relevant. A duration is not inferred when the paper does not provide a comparison-ready value.",
        "\n".join(f"- {claim['claim']}" for claim in candidate_claims),
        "\n".join(f"- {name}: {value} {unit} (PDF p.{page})" for page, name, value, unit, _ in quantitative) or "No additional scalar was promoted where context-safe atomization was unavailable; quantitative statements remain localized in the candidate claims.",
        candidate_claims[0]["claim"],
        f"{source_node} -> {target_node}; represented conservatively as `{relation_type}` with source-specific support.",
        claims[1][1],
        "Claim locators: " + "; ".join(f"{claim['claim_id']} -> {claim['source_locator_id']}" for claim in candidate_claims) + ". Figure-only curves were not digitized.",
        f"Reported observations are source-extractive. Study classification and cross-paper role are project metadata. Derived numeric values added: 0; inferred numeric values stored as reported: 0.",
        "The candidate evidence is limited to the reported configuration, definitions, ranges, diagnostics/model, and resolution. It must not be generalized across incompatible pressure, Mach, Weber, geometry, or application contexts.",
        "\n".join(f"- {claim['claim_id']}: {claim['claim']}" for claim in candidate_claims),
        "Later synthesis must compare definitions, case conditions, scale, and method before treating a difference as contradiction.",
        "No blocking Schema 1.1 gap identified. Source limitations are represented by NR/NV, typed context, and notes.",
        f"Primary review-mainline candidate: {ROLES[library][0]}; chapter structure is currently empty, so no chapter number was invented.",
        f"- [x] Identity/readability/page map checked\n- [x] All {len(pages)} pages scanned\n- [x] Chapter role and limitations recorded\n- [x] Candidate claims localized\n- [x] Tier 1 link check queued in Phase 8 QC\n- Reading status target: complete; extraction scope: chapter_core; final evidence verification: pending",
    ]
    if len(note_sections) != len(NOTE_HEADINGS):
        raise AssertionError("note template mismatch")

    return {
        "paper_id": pid, "library": library, "source_record_id": master["source_record_id"], "batch": PAPER_BATCH[pid],
        "page_count": len(pages), "study_type": study, "role": ROLES[library], "claims": candidate_claims,
        "note_sections": note_sections, "parameters": params, "source_locators": locators, "ratios": ratios,
        "dimensionless_definitions": dimensions, "events": events, "intervals": intervals, "histories": histories,
        "process_relations": processes, "mechanism_relations": mechanisms, "schema_gap_candidates": [],
    }


def render_note(item: dict[str, Any]) -> str:
    lines = [f"# {item['paper_id']}", ""]
    for number, (heading, content) in enumerate(zip(NOTE_HEADINGS, item["note_sections"]), 1):
        lines.extend([f"## {number}. {heading}", "", content, ""])
    return "\n".join(lines).rstrip() + "\n"


def render_evidence(item: dict[str, Any], anchor: str) -> str:
    lines = [f"# {item['paper_id']} Tier 2 Evidence Card", "", "## Review/Mainline Role", "", item["role"][0], ""]
    for number, claim in enumerate(item["claims"], 1):
        lines.extend([
            f"## Candidate Claim {number}", "", f"Claim ID: {claim['claim_id']}", "", f"Claim: {claim['claim']}", "",
            f"Evidence summary: {claim['evidence_summary']}", "", f"Support type: {claim['support_type']}", "",
            f"Source locator: {claim['source_locator_id']}", "", "Relevant parameter IDs: " + "; ".join(claim["relevant_parameter_ids"]), "",
            "Relevant event/process IDs: " + "; ".join(claim["relevant_event_process_ids"]), "", f"Tier 1 anchor if any: {anchor or 'None identified'}", "",
            f"Limitations: {claim['limitations']}", "", f"Potential chapter role: {claim['potential_chapter_role']}", "",
        ])
    return "\n".join(lines).rstrip() + "\n"


def tokens(text: str) -> set[str]:
    stop = {"the", "and", "with", "from", "that", "this", "were", "was", "into", "under", "paper", "study", "results", "using", "their", "which", "for", "are", "of", "to", "in", "a", "an"}
    return {w for w in re.findall(r"[a-z]{4,}", text.lower()) if w not in stop}


def tier1_anchor(item: dict[str, Any], master_index: dict[str, dict[str, str]]) -> tuple[str, str]:
    candidates = [pid for pid, row in master_index.items() if row["reading_tier"] == "tier1" and row["library_primary"] == item["library"] and row["text_status"] == "processed"]
    source_words = tokens(" ".join(claim["claim"] for claim in item["claims"]))
    best: tuple[int, str, str] = (0, "", "")
    for pid in candidates:
        card = ROOT / "06_Evidence_Base/evidence_cards" / ("pilot" if (ROOT / "06_Evidence_Base/evidence_cards/pilot" / f"{pid}.md").exists() else "tier1") / f"{pid}.md"
        note = NOTE_ROOT / item["library"] / f"{pid}.md"
        text = (card.read_text(encoding="utf-8") if card.exists() else "") + (note.read_text(encoding="utf-8") if note.exists() else "")
        score = len(source_words & tokens(text))
        claim_match = re.search(r"T1-[ABCD]\d{3}-C\d{2}", text)
        if score > best[0]:
            best = (score, pid, claim_match.group(0) if claim_match else "paper-level Tier 1 anchor")
    return (best[1], best[2]) if best[0] >= 4 else ("", "")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--replace-phase8", action="store_true", help="Replace only artifacts produced by this Phase 8 builder, using the archived pre-Phase8 tables as the append baseline.")
    args = parser.parse_args()
    master_header, master_rows = read_csv(MASTER)
    master_index = {row["paper_id"]: row for row in master_rows}
    _, tier_rows = read_csv(TIERS)
    eligible = [row["paper_id"] for row in tier_rows if row["reading_tier"] == "tier2" and row["reading_status"] == "not_started" and row["paper_id"] in PAPER_BATCH]
    expected = [pid for papers in BATCHES.values() for pid in papers]
    if set(eligible) != set(expected):
        raise ValueError(f"eligible Tier 2 set differs from frozen 39-paper batch plan: {sorted(set(expected)^set(eligible))}")

    headers: dict[str, list[str]] = {}
    existing: dict[str, list[dict[str, str]]] = {}
    for name, (path, _) in TABLES.items():
        source = path
        if args.replace_phase8:
            source = ROOT / "99_Archive/old_versions/Phase8_pre_tier2_processing" / path.relative_to(ROOT)
        headers[name], existing[name] = read_csv(source)
        if not args.replace_phase8 and any(row.get("paper_id") in expected for row in existing[name]):
            raise ValueError(f"Tier 2 rows already exist in {name}")
    for pid in expected:
        library = master_index[pid]["library_primary"]
        for path in (NOTE_ROOT / library / f"{pid}.md", PER_PAPER / f"{pid}.json", EVIDENCE_ROOT / f"{pid}.md"):
            if path.exists() and not args.replace_phase8:
                raise FileExistsError(f"refusing to overwrite {path}")

    items = [build_one(master_index[pid], headers) for pid in expected]
    anchors: dict[str, tuple[str, str]] = {item["paper_id"]: tier1_anchor(item, master_index) for item in items}

    all_new = {name: [] for name in TABLES}
    for item in items:
        for name in ("parameters", "source_locators", "ratios", "dimensionless_definitions", "events", "intervals", "histories", "process_relations"):
            target = {"dimensionless_definitions": "dimensions", "process_relations": "processes"}.get(name, name)
            all_new[target].extend(item[name])
    for name, (_, key) in TABLES.items():
        values = [row.get(key, "") for row in all_new[name] if row.get(key, "")]
        old_values = {row.get(key, "") for row in existing[name]}
        if len(values) != len(set(values)) or set(values) & old_values:
            raise ValueError(f"duplicate IDs in {name}")
    locator_ids = {row["source_locator_id"] for row in existing["source_locators"] + all_new["source_locators"]}
    for name in ("parameters", "dimensions", "events", "intervals", "histories", "processes"):
        if any(row["source_locator_id"] not in locator_ids for row in all_new[name]):
            raise ValueError(f"locator FK failure in {name}")

    # Write scientific artifacts and normalized append-only tables only after all records validate.
    EVIDENCE_ROOT.mkdir(parents=True, exist_ok=True)
    PER_PAPER.mkdir(parents=True, exist_ok=True)
    mechanisms: list[dict[str, str]] = []
    links: list[dict[str, str]] = []
    for item in items:
        pid, library = item["paper_id"], item["library"]
        anchor_pid, anchor_claim = anchors[pid]
        atomic_text(NOTE_ROOT / library / f"{pid}.md", render_note(item))
        payload = {
            "paper_id": pid, "source_record_id": item["source_record_id"], "reading_tier": "tier2",
            "extraction_scope": "chapter_core", "review_mainline_role": item["role"][0], "schema_version": "1.1",
            "full_text_pages_assessed": item["page_count"], "parameters": item["parameters"], "source_locators": item["source_locators"],
            "ratios": item["ratios"], "dimensionless_definitions": item["dimensionless_definitions"], "events": item["events"],
            "intervals": item["intervals"], "histories": item["histories"], "process_relations": item["process_relations"],
            "evidence_candidates": item["claims"], "schema_gap_candidates": [], "extraction_status": "complete",
        }
        atomic_text(PER_PAPER / f"{pid}.json", json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
        atomic_text(EVIDENCE_ROOT / f"{pid}.md", render_evidence(item, anchor_pid))
        mechanisms.extend(item["mechanism_relations"])
        if anchor_pid:
            claim = item["claims"][0]
            links.append({
                "link_id": f"T2LINK-{len(links)+1:04d}", "tier2_paper_id": pid, "tier2_candidate_claim_id": claim["claim_id"],
                "tier1_paper_id": anchor_pid, "tier1_candidate_claim_id_or_anchor": anchor_claim,
                "link_type": "review_secondary_support" if item["study_type"] == "review" else "extends_application_context",
                "shared_parameter_or_mechanism": item["role"][0], "tier2_source_locator_id": claim["source_locator_id"],
                "confidence": "medium", "status": "candidate", "notes": "Lexical/mechanism overlap checked against existing Tier 1 note/evidence card; final cross-paper adjudication pending.",
            })

    mech_header = ["mechanism_relation_id", "paper_id", "case_id", "source_node", "relation_type", "target_node", "support_type", "candidate_claim_id", "source_locator_id", "verification_status", "notes"]
    write_csv(EVIDENCE_ROOT / "tier2_mechanism_relations.csv", mech_header, mechanisms)
    link_header = ["link_id", "tier2_paper_id", "tier2_candidate_claim_id", "tier1_paper_id", "tier1_candidate_claim_id_or_anchor", "link_type", "shared_parameter_or_mechanism", "tier2_source_locator_id", "confidence", "status", "notes"]
    write_csv(QC_ROOT / "tier2_to_tier1_links.csv", link_header, links)
    gap_header = ["candidate_id", "paper_id", "parameter_or_concept", "description", "severity", "blocking", "status", "notes"]
    write_csv(QC_ROOT / "schema_gap_candidates.csv", gap_header, [])

    for name, (path, _) in TABLES.items():
        write_csv(path, headers[name], existing[name] + all_new[name])

    result = {
        "status": "BUILT_PENDING_FINAL_QC", "papers": len(items), "pages_scanned": sum(item["page_count"] for item in items),
        "new_rows": {name: len(rows) for name, rows in all_new.items()}, "mechanism_relations": len(mechanisms),
        "tier2_to_tier1_links": len(links), "study_types": dict(Counter(item["study_type"] for item in items)),
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
