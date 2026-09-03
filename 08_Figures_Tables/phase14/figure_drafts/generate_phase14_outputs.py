from __future__ import annotations

import csv
import math
import re
from pathlib import Path
from textwrap import wrap

from PIL import Image, ImageDraw, ImageFont


# This generator is stored under 08_Figures_Tables/phase14/figure_drafts/.
ROOT = Path(__file__).resolve().parents[3]
P14 = ROOT / "08_Figures_Tables" / "phase14"
QDIR = P14 / "quantitative"
REGDIR = QDIR / "case_registry"
SPECDIR = P14 / "figure_specs"
DRAFTDIR = P14 / "figure_drafts"
PREVIEWDIR = P14 / "figure_previews"
SOURCEDIR = P14 / "figure_sources"
TABLEDIR = P14 / "tables"
SUPPORTDIR = ROOT / "07_Chapters" / "draft_support"
MANUSCRIPTDIR = ROOT / "09_Manuscript"
QCDIR = ROOT / "11_QC"

for directory in (P14, QDIR, REGDIR, SPECDIR, DRAFTDIR, PREVIEWDIR, SOURCEDIR, TABLEDIR, SUPPORTDIR, QCDIR):
    directory.mkdir(parents=True, exist_ok=True)


def write_csv(path: Path, fields: list[str], rows: list[dict[str, object]]) -> None:
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def write_text(path: Path, text: str) -> None:
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def md_table(fields: list[str], rows: list[dict[str, object]]) -> str:
    def clean(value: object) -> str:
        return str(value if value is not None else "").replace("|", "\\|").replace("\n", " ")

    lines = ["| " + " | ".join(fields) + " |", "| " + " | ".join("---" for _ in fields) + " |"]
    lines.extend("| " + " | ".join(clean(row.get(field, "")) for field in fields) + " |" for row in rows)
    return "\n".join(lines)


FIGURE_SOURCE_FIELDS = [
    "source_panel_id", "figure_id", "paper_id", "source_pdf", "page_number",
    "source_figure_number", "source_panel_label", "source_type", "phenomenon",
    "scientific_role", "why_selected", "condition_summary", "source_locator_id",
    "candidate_reuse_mode", "license_status", "priority", "notes",
]

figure_sources = [
    dict(source_panel_id="FSP-02-01", figure_id="FIG-02", paper_id="B009", source_pdf="02_PDF_Raw/B/B-H2-04_2014_Hamzehloo_LES_Underexpanded_Hydrogen_MethaneJets.pdf", page_number="9", source_figure_number="5–8", source_panel_label="NR", source_type="simulation_contour", phenomenon="transient jet development and Mach-disk emergence", scientific_role="connect developing nozzle flow to successive external wave states", why_selected="verified locator; direct transient sequence; condition definitions available", condition_summary="H2/CH4; converging nozzle D=1.5 mm; semi-steady comparison follows transient development", source_locator_id="LOC-B009-0005", candidate_reuse_mode="reuse_permission_required", license_status="all_rights_reserved", priority="high", notes="Use exact source only with permission; otherwise retain labelled placeholder and cite physical facts."),
    dict(source_panel_id="FSP-02-02", figure_id="FIG-02", paper_id="B021", source_pdf="02_PDF_Raw/B/B-E-01_2023_Anaclerio_Numerical_Underexpanded_HydrogenJets_ICE.pdf", page_number="11–12", source_figure_number="18–19", source_panel_label="NR", source_type="simulation_contour", phenomenon="unsteady one-jet Mach-disk evolution", scientific_role="show that instantaneous shock topology differs from the steady NPR state", why_selected="verified unsteady section and figure locator", condition_summary="hydrogen; one-jet unsteady calculation; pressure and chamber state remain case-specific", source_locator_id="LOC-B021-0006", candidate_reuse_mode="reuse_permission_required", license_status="unknown", priority="medium", notes="License not confirmed in frozen project files."),
    dict(source_panel_id="FSP-02-03", figure_id="FIG-02", paper_id="B029", source_pdf="02_PDF_Raw/B/B-E-09_2026_Sang_InjectorPressureBuildUp_Underexpanded_HydrogenJet.pdf", page_number="9", source_figure_number="8–12", source_panel_label="NR", source_type="graph", phenomenon="injector pressure build-up and transient underexpanded-jet response", scientific_role="align injector pressure history with Mach-disk formation, motion, and stabilization", why_selected="most direct pressure-build-up/transient-wave pairing in frozen corpus", condition_summary="hydrogen injector transient; event alignment and pressure location must be retained", source_locator_id="LOC-B029-0008", candidate_reuse_mode="internal_preview_only", license_status="CC BY-NC-ND 4.0", priority="high", notes="ND and NC restrictions make journal reuse conditional; do not crop or adapt until venue and rights route are confirmed."),
    dict(source_panel_id="FSP-04-01", figure_id="FIG-04", paper_id="C016", source_pdf="02_PDF_Raw/C/C-SD-09_2021_Sharma_ShockInduced_DropletAerobreakup.pdf", page_number="13", source_figure_number="6", source_panel_label="NR", source_type="shadowgraph", phenomenon="shock-induced droplet aerobreakup morphologies", scientific_role="anchor representative SIE and RTP response sequences", why_selected="direct high-speed observation; cases have incident Mach, We, Re, diameter, and author regime label", condition_summary="water; incident-shock Mach 1.12–1.45; d0=0.5–2.9 mm; author labels SIE/RTP", source_locator_id="LOC-C016-0004", candidate_reuse_mode="reuse_open_license", license_status="CC BY 4.0", priority="critical", notes="Preserve image meaning, time labels, and scale information; attribution required."),
    dict(source_panel_id="FSP-04-02", figure_id="FIG-04", paper_id="C025", source_pdf="02_PDF_Raw/C/C-ST-05_2025_Ullman_ShockInduced_DropletBreakup_TimescalesStatistics.pdf", page_number="5", source_figure_number="4–6", source_panel_label="NR", source_type="simulation_contour", phenomenon="droplet displacement and deformation under shock loading", scientific_role="support the transition from early compression to deformation and sheet/rim evolution", why_selected="verified source sequence with definition-rich case configuration", condition_summary="water; d0=100 µm; incident Mach 2 and 3 cases; We=822 and 3760 as reported", source_locator_id="LOC-C025-0003", candidate_reuse_mode="reuse_permission_required", license_status="unknown", priority="high", notes="Use only after permission or replace by fact-based mechanism redraw."),
    dict(source_panel_id="FSP-04-03", figure_id="FIG-04", paper_id="D018", source_pdf="02_PDF_Raw/D/D-DW-03_2026_Yang_RP3_Droplet_DeformationBreakup_Detonation.pdf", page_number="10", source_figure_number="15–16", source_panel_label="NR", source_type="experiment_image", phenomenon="complete breakup in detonation-driven loading", scientific_role="show ligament and fragment formation under a reacting strong wave", why_selected="direct observation with liquid-specific breakup-time scaling", condition_summary="water and RP-3; detonation Mach about 6–7; high We; reacting strong-wave comparison only", source_locator_id="LOC-D018-0008", candidate_reuse_mode="reuse_permission_required", license_status="all_rights_reserved", priority="medium", notes="Strong-wave analogue, not HPDI evidence."),
    dict(source_panel_id="FSP-05-01", figure_id="FIG-05", paper_id="C035", source_pdf="02_PDF_Raw/C/C-MD-03_2021_Wang_ShockInduced_TandemDroplet_Breakup.pdf", page_number="5", source_figure_number="4", source_panel_label="NR", source_type="shadowgraph", phenomenon="tandem-droplet wake shielding and spacing-dependent response", scientific_role="represent ordered streamwise collective effects", why_selected="verified direct tandem observation with S/D and We ranges", condition_summary="water; d0≈2 mm; S/D=1.2–10.5; We=13–180", source_locator_id="LOC-C035-0004", candidate_reuse_mode="reuse_permission_required", license_status="publisher_license_unknown", priority="critical", notes="AIP publication; reuse permission not established."),
    dict(source_panel_id="FSP-05-02", figure_id="FIG-05", paper_id="C036", source_pdf="02_PDF_Raw/C/C-MD-04_2026_Guo_ShockInduced_ParallelDroplets_Aerobreakup.pdf", page_number="8–11", source_figure_number="5–7", source_panel_label="NR", source_type="experiment_image", phenomenon="parallel-droplet channel opening and closure", scientific_role="represent transverse arrangement and squeeze/channel-flow effects", why_selected="verified phase-diagram figures; distinct mechanism from tandem shielding", condition_summary="parallel droplets; D=230–430 µm; L/D below 0.1 to above 2; We O(10)–O(100)", source_locator_id="LOC-C036-0003", candidate_reuse_mode="reuse_permission_required", license_status="all_rights_reserved", priority="critical", notes="Do not generalize the phase boundary to dense sprays."),
    dict(source_panel_id="FSP-06-01", figure_id="FIG-06", paper_id="C024", source_pdf="02_PDF_Raw/C/C-ST-04_2023_DukeWalker_SmallDroplet_BreakupEvaporation_HighWeber.pdf", page_number="7", source_figure_number="7–8", source_panel_label="NR", source_type="shadowgraph", phenomenon="small-droplet breakup, cloud persistence, and disappearance", scientific_role="anchor the fragment-survival/evaporation branch", why_selected="direct observation linking high-We breakup to a finite disappearance interval", condition_summary="small droplets; high Weber loading; final discernible clouds disappear at 250–300 µs", source_locator_id="LOC-C024-0005", candidate_reuse_mode="reuse_permission_required", license_status="all_rights_reserved", priority="high", notes="Observation cannot by itself establish HPDI mixture improvement."),
    dict(source_panel_id="FSP-07-01", figure_id="FIG-07", paper_id="A022", source_pdf="02_PDF_Raw/A/A-H2-05_2024_Rorimpandey_JetInteractionAngle_H2DDI.pdf", page_number="3", source_figure_number="2", source_panel_label="NR", source_type="schematic", phenomenon="pilot–hydrogen jet geometry and interaction angle", scientific_role="define spatial intersection geometry for the chronology schematic", why_selected="direct application geometry; open license; exact locator", condition_summary="H2 dual-direct-injection configuration; pilot SOI 0.6 ms after H2 SOI in extracted timing record", source_locator_id="LOC-A022-0006", candidate_reuse_mode="redraw_from_scientific_facts", license_status="CC BY 4.0", priority="high", notes="Prefer an original geometry redraw even though reuse is licensed; cite A022."),
    dict(source_panel_id="FSP-07-02", figure_id="FIG-07", paper_id="A026", source_pdf="02_PDF_Raw/A/A-H2-09_2025_Heaton_HydrogenInjectionTiming_EnergyProportion_Flame.pdf", page_number="7–11", source_figure_number="9–13", source_panel_label="NR", source_type="other", phenomenon="hydrogen injection timing and flame/heat-release response", scientific_role="represent chronology-conditioned combustion response", why_selected="direct engine-domain timing series with explicit electronic SOI events", condition_summary="hydrogen SOI varied 0–30 CA bTDC; pilot electronic SOI 6 CA bTDC; energy share remains case-specific", source_locator_id="LOC-A026-0005", candidate_reuse_mode="internal_preview_only", license_status="CC BY-NC", priority="medium", notes="Noncommercial restriction requires venue check before final reuse."),
    dict(source_panel_id="FSP-07-03", figure_id="FIG-07", paper_id="A007", source_pdf="02_PDF_Raw/A/A-NG-07_2018_Fink_DieselPilot_NGJet_SpatialTemporalInteraction.pdf", page_number="6", source_figure_number="10", source_panel_label="NR", source_type="graph", phenomenon="pilot/main timing and ignition delay", scientific_role="show direct timing-to-ignition evidence without attributing it to shock", why_selected="typed gas-SOI minus pilot-SOI interval and explicit ignition definitions", condition_summary="RCEM; gas SOI minus pilot SOI from −2.5 to +1.5 ms; paper-specific HRR thresholds", source_locator_id="LOC-A007-0005", candidate_reuse_mode="reuse_permission_required", license_status="all_rights_reserved", priority="high", notes="Graph is a data expression; do not imitate visually without permission or independent replot data."),
    dict(source_panel_id="FSP-08-01", figure_id="FIG-08", paper_id="D018", source_pdf="02_PDF_Raw/D/D-DW-03_2026_Yang_RP3_Droplet_DeformationBreakup_Detonation.pdf", page_number="4–6", source_figure_number="4–6", source_panel_label="NR", source_type="experiment_image", phenomenon="reacting strong-wave droplet deformation and breakup", scientific_role="represent detonation-domain observation", why_selected="direct reacting-wave observation with water/RP-3 comparison", condition_summary="detonation Mach about 6–7; water and RP-3; d0≈0.25–1.27 mm", source_locator_id="LOC-D018-0005", candidate_reuse_mode="reuse_permission_required", license_status="all_rights_reserved", priority="high", notes="Comparison domain only."),
    dict(source_panel_id="FSP-08-02", figure_id="FIG-08", paper_id="D019", source_pdf="02_PDF_Raw/D/D-DW-04_2026_Zou_DetonationShock_DropletInteraction_Mechanisms.pdf", page_number="10–15", source_figure_number="8–15", source_panel_label="NR", source_type="simulation_contour", phenomenon="reacting detonation versus matched-leading-Mach inert shock loading", scientific_role="separate heat-release effects from leading-wave Mach", why_selected="direct reacting/inert comparison at matched incident Mach", condition_summary="water d0=4.8 mm; incident Mach 4.8; detonation and inert-shock cases have different post-wave We/Re", source_locator_id="LOC-D019-0006", candidate_reuse_mode="reuse_permission_required", license_status="all_rights_reserved", priority="critical", notes="Use to emphasize post-wave state, not leading Mach equivalence."),
]

write_csv(P14 / "figure_source_inventory.csv", FIGURE_SOURCE_FIELDS, figure_sources)


REUSE_FIELDS = ["source_panel_id", "figure_id", "paper_id", "source_figure_number", "license_status", "copyright_notice_found", "reuse_action", "attribution_required", "permission_status", "final_use_allowed_now", "recommended_alternative", "notes"]
reuse_rows = []
for row in figure_sources:
    license_status = row["license_status"]
    if row["candidate_reuse_mode"] == "reuse_open_license":
        action, final_now, permission = "reuse_open_license", "yes_with_attribution", "license_confirmed"
    elif row["candidate_reuse_mode"] == "redraw_from_scientific_facts":
        action, final_now, permission = "redraw_from_scientific_facts", "yes_as_original_redraw", "not_required_for_new_visual_expression"
    elif row["candidate_reuse_mode"] == "internal_preview_only":
        action, final_now, permission = "internal_preview_only", "no", "venue_or_permission_check_pending"
    else:
        action, final_now, permission = "reuse_permission_required", "no", "not_requested_phase14"
    reuse_rows.append(dict(source_panel_id=row["source_panel_id"], figure_id=row["figure_id"], paper_id=row["paper_id"], source_figure_number=row["source_figure_number"], license_status=license_status, copyright_notice_found="yes" if license_status not in ("unknown", "publisher_license_unknown") else "not_confirmed", reuse_action=action, attribution_required="yes", permission_status=permission, final_use_allowed_now=final_now, recommended_alternative="retain provenance-labelled placeholder; use author synthesis for mechanism" if final_now == "no" else "use with exact attribution and unaltered data meaning", notes=row["notes"]))

for fid in ("FIG-01", "FIG-03", "FIG-06", "FIG-09"):
    reuse_rows.append(dict(source_panel_id=f"AUTH-{fid}", figure_id=fid, paper_id="NA", source_figure_number="NA", license_status="author_generated", copyright_notice_found="NA", reuse_action="author_synthesis", attribution_required="cite scientific sources in caption", permission_status="not_required", final_use_allowed_now="yes", recommended_alternative="NA", notes="Original Phase 14 vector schematic; no literature image copied."))

write_csv(P14 / "figure_reuse_strategy.csv", REUSE_FIELDS, reuse_rows)


figure_specs = {
    "FIG-01": dict(title="Unified injector-to-ignition mechanism framework", question="Which physical variables are transported from injector opening to ignition, and where do four cross-scale couplings remain unmeasured?", message="The chain is physically continuous, but its causal closure depends on Lagrangian load, dense-spray transfer, fragment-to-mixture transport, and mixture-to-ignition measurements.", panels="Single author-synthesis canvas: boundary history → wave field → liquid loading → deformation/breakup → fragment population → transport/phase change → mixture → ignition/heat release.", sources="No literature image panels. Scientific facts: [[CITE:B009]] [[CITE:B021]] [[CITE:C016]] [[CITE:C035]] [[CITE:C024]] [[CITE:A007]] [[CITE:A022]].", components="All boxes, arrows, transported-variable labels, and four open coupling gates are author generated.", variables="needle/valve state; p_inj(t); NPR(t); p, rho, u; x_d(t); u_rel(t); d0; Mach; We; Oh; fragment d/v/T distributions; vapor/species; ignition delay.", arrows="Solid arrows for physical progression within native domains; dashed arrows at unresolved cross-scale transfers; no arrow from visible Mach disk directly to known pilot load.", takeaway="A useful experiment must measure the transported variables on one clock rather than infer the full chain from isolated component studies.", caption="Define the mechanism sequence and explicitly name the four unresolved quantities without project IDs.", rights="Author synthesis; cite the physical sources.", limitation="Does not assign magnitudes or universal time ordering."),
    "FIG-02": dict(title="Transient injection and underexpanded-wave evolution", question="How do valve/needle motion and p_inj(t) organize choking, Mach-disk appearance, overshoot, motion, and stabilization?", message="Mach-disk state is event-aligned and transient; nominal rail pressure cannot substitute for the nozzle boundary history.", panels="A: author timeline. B–D: provenance-labelled placeholders FSP-02-01 to FSP-02-03.", sources="FSP-02-01 [[CITE:B009]]; FSP-02-02 [[CITE:B021]]; FSP-02-03 [[CITE:B029]].", components="Timeline, event markers, normalized conceptual traces, and state labels are author generated.", variables="valve lift; p_inj(t); effective area; choking; x_MD(t)/D; formation/overshoot/stabilized state.", arrows="Time-directed arrows; dotted conceptual traces; literature observations remain separate and condition labelled.", takeaway="Compare transient jets only after aligning pressure location, event zero, gas, nozzle, ambient state, and wave stage.", caption="State that source images are placeholders unless rights allow final reuse.", rights="B009 permission required; B021 unknown; B029 CC BY-NC-ND internal preview only.", limitation="No machine-readable time histories exist in the extracted time-series table."),
    "FIG-03": dict(title="Eulerian wave field to Lagrangian pilot-droplet forcing", question="How are p(x,t), rho(x,t), and u(x,t) sampled along moving pilot droplets?", message="Droplet response requires p[x_d(t),t], rho[x_d(t),t], u_rel(t), load direction, and duration; actual HPDI histories are unresolved.", panels="Author synthesis only: Eulerian field, moving trajectory, sampling operator, load history, response clocks, open HPDI measurement gate.", sources="Scientific basis: [[CITE:B009]] [[CITE:B021]] [[CITE:C007]] [[CITE:C016]].", components="All visual elements author generated.", variables="p(x,t); rho(x,t); u(x,t); x_d(t); u_d(t); u_rel(t); Δp; impulse; tau_loading; tau_response.", arrows="Field-to-trajectory sampling is solid as a mathematical operation; the actual HPDI data path ends in an open dashed measurement gate.", takeaway="A shock topology image cannot be converted to a unique droplet We or impulse without trajectory-resolved gas and liquid data.", caption="Retain the unresolved state in reader-facing physical language.", rights="Author synthesis.", limitation="tau_loading/tau_response is an organizing hypothesis, not a universal correlation."),
    "FIG-04": dict(title="Compressible droplet deformation and breakup", question="How do internal response and competing RT/KH/capillary processes create sheets, ligaments, and fragments?", message="We alone does not determine morphology; Mach frame, material state, d0, Oh, and load duration organize competing paths.", panels="A: C016 open-license observation placeholder. B: C025 permission-pending placeholder. C: D018 strong-wave comparison placeholder. D: author mechanism cascade.", sources="FSP-04-01 [[CITE:C016]]; FSP-04-02 [[CITE:C025]]; FSP-04-03 [[CITE:D018]].", components="Mechanism cascade and parameter perimeter author generated.", variables="M_s/M_rel; We components; Re; Oh; d0; density ratio; loading duration; internal pressure/circulation.", arrows="Compression → flattening; branching RT piercing and KH/shear stripping; capillary competition; sheet/rim → ligament → fragments.", takeaway="Use condition-faceted morphology, not a universal two-axis breakup map.", caption="Identify observation source and reuse state for every panel.", rights="Only C016 is immediately reusable under CC BY 4.0; others remain placeholders.", limitation="Reacting detonation panels are analogues and do not validate HPDI breakup."),
    "FIG-05": dict(title="From isolated droplets to collective spray response", question="How do arrangement, shielding, channel flow, and wave attenuation modify canonical response before dense-spray transfer?", message="Collective mechanisms are directly observed in ordered pairs and clouds, but no universal mapping to dense reacting HPDI spray is validated.", panels="Isolated reference schematic; tandem placeholder FSP-05-01; parallel placeholder FSP-05-02; cloud synthesis; dense-polydisperse target behind an open transfer gate.", sources="[[CITE:C016]]; FSP-05-01 [[CITE:C035]]; FSP-05-02 [[CITE:C036]]; cloud facts [[CITE:C033]] [[CITE:C034]].", components="Configuration progression, mechanism labels, cloud and dense-spray symbols author generated.", variables="S/D; orientation; volume fraction; polydispersity; transmitted pressure/impulse; wake slip.", arrows="Solid within configuration; dashed and open at dense-HPDI transfer.", takeaway="Spacing laws are arrangement- and loading-specific; dense spray requires population statistics and two-way coupling.", caption="Do not label canonical results as dense-spray validation.", rights="Tandem and parallel observations require permission; layout placeholders only.", limitation="No direct dense-HPDI validation in the frozen corpus."),
    "FIG-06": dict(title="Fragment population to transport, evaporation, and mixture redistribution", question="Which fragment variables control transport and conditional phase change before any mixture effect?", message="Breakup creates distributions, not a single smaller diameter; phase change may be promoted or suppressed, and mixture influence requires residence before ignition.", panels="Author-synthesis dominant canvas plus one permission-pending observation placeholder FSP-06-01.", sources="FSP-06-01 [[CITE:C024]]; mechanism and survival facts [[CITE:D017]] [[CITE:C031]] [[CITE:C032]].", components="Fragment distributions, two thermal branches, residence/transport network, and open HPDI mixture gate author generated.", variables="n(d); mass-weighted d; velocity; surface area; fragment temperature; gas temperature; volatility; residence; vapor fraction.", arrows="Separate shear-suppression and surface-tension-reduction branches; neither is universal. Open arrow to HPDI mixture contribution.", takeaway="Breakup is not equivalent to faster evaporation or improved mixing.", caption="State the conditional branches and the unmeasured fragment-to-mixture contribution.", rights="Author synthesis; C024 observation requires permission and remains placeholder.", limitation="Detection loss and fragment statistics are not interchangeable with evaporation."),
    "FIG-07": dict(title="HPDI chronology, mixture preparation, and ignition", question="How do signed pilot/main timing and jet geometry condition mixture, ignition, and heat release?", message="Chronology and geometry have direct application evidence; shock-mediated improvement is not isolated.", panels="Author signed-timeline and intersection schematic; placeholders/redraw for FSP-07-01 to FSP-07-03.", sources="FSP-07-01 [[CITE:A022]]; FSP-07-02 [[CITE:A026]]; FSP-07-03 [[CITE:A007]].", components="Signed ΔSOI convention, pilot-product states, mixture stratification, ignition-kernel sequence author generated.", variables="pilot SOI; gas SOI; signed ΔSOI; intersection distance; pilot state; mixture fraction; temperature; radicals; ignition delay.", arrows="Solid chronology-to-observed response; dashed wave-mediated branch ending before ignition causality.", takeaway="A timing response cannot be assigned to shock-induced atomization without synchronized fragment/species measurements.", caption="Preserve sign convention, fuel order, event definitions, geometry, and operating condition.", rights="A022 physical geometry will be redrawn; A026 internal preview only; A007 permission required.", limitation="No condition-compatible pooled timing-response metric was available."),
    "FIG-08": dict(title="Strong-wave droplet analogues", question="Which local variables are shared between detonation/RDE and HPDI, and which scales remain device-specific?", message="Strong-wave studies clarify local loading and residence competition but cannot substitute for HPDI evidence.", panels="D018 and D019 observation placeholders; author two-layer shared-variable/domain-specific comparison schematic.", sources="FSP-08-01 [[CITE:D018]]; FSP-08-02 [[CITE:D019]]; RDE scale relation [[CITE:D009]].", components="Shared-variable layer and domain-specific scale layer author generated.", variables="post-wave p/rho/u; d0; fragment distribution; residence; detonation reaction zone; RDE refill scale; HPDI geometry and ignition time.", arrows="Solid within strong-wave domain; dashed transfer to HPDI measurement questions.", takeaway="Leading Mach equality does not preserve post-wave thermochemistry or application scale.", caption="Label detonation/RDE as comparison domain only.", rights="Observation panels require permission and remain placeholders.", limitation="L_E/L_D has no validated quantitative mapping to HPDI ignition."),
    "FIG-09": dict(title="Integrated multiscale coupling and research priorities", question="Which clocks and transported variables determine whether upstream wave processes can influence ignition?", message="Influence depends on time ordering and four missing synchronized measurements, not a generic direct/indirect evidence ladder.", panels="Author synthesis only: competing clocks, transported variables, and four reader-facing measurement questions.", sources="Synthesis basis: [[CITE:B009]] [[CITE:C016]] [[CITE:C035]] [[CITE:C024]] [[CITE:A007]] [[CITE:D009]].", components="All visual elements author generated.", variables="injector time; wave time; droplet acoustic/acceleration time; instability time; fragment response; evaporation; mixing; ignition; p/rho/u; d/v/T; species.", arrows="Clock sequence is not fixed; arrows show possible ordering. Four open measurement gates remain explicit.", takeaway="The research priority is synchronized gas–liquid–species–combustion measurement on a common clock.", caption="Use physical quantities and missing measurements; no internal MP/KG identifiers.", rights="Author synthesis.", limitation="Conceptual ordering only; no universal tau_loading/tau_response curve."),
}

for fid, spec in figure_specs.items():
    body = f"""# {fid} — {spec['title']}

## Scientific question

{spec['question']}

## Scientific message

{spec['message']}

## Panel structure

{spec['panels']}

## Source panels

{spec['sources']}

## Author-generated components

{spec['components']}

## Variables shown

{spec['variables']}

## Mechanism arrows

{spec['arrows']}

## Reader takeaway

{spec['takeaway']}

## Caption logic

{spec['caption']}

## Rights status

{spec['rights']}

## Known limitation

{spec['limitation']}
"""
    write_text(SPECDIR / f"{fid}_spec.md", body)


# Reader-facing tables. Values are restricted to extracted records or explicit author synthesis.
tables: dict[str, tuple[list[str], list[dict[str, object]]]] = {}

tables["TAB-01"] = (["Parameter", "Physical meaning", "Required definition", "Common incompatible definitions", "Minimum information for comparison", "Recommended use"], [
    {"Parameter":"NPR", "Physical meaning":"Upstream-to-downstream pressure ratio controlling underexpansion", "Required definition":"Numerator and denominator roles, locations, total/static type, absolute/gauge basis, and time/stage", "Common incompatible definitions":"Rail/chamber; plenum/ambient; instantaneous/nominal; gauge/absolute", "Minimum information for comparison":"Both pressures plus nozzle state, gas, ambient state, and transient stage", "Recommended use":"Only definition-complete, condition-faceted jet comparisons"},
    {"Parameter":"Mach number", "Physical meaning":"Speed relative to a specified acoustic state", "Required definition":"Object (jet, incident shock, post-wave flow, relative flow, detonation front), reference frame, and sound-speed state", "Common incompatible definitions":"Incident-shock M_s; post-shock M; droplet-relative M_rel; detonation-front Mach", "Minimum information for comparison":"Velocity, sound-speed state, frame, location, and time", "Recommended use":"Keep separate axes/facets for different frames"},
    {"Parameter":"Weber number", "Physical meaning":"Aerodynamic/inertial stress relative to surface tension", "Required definition":"Density, velocity, length, and surface tension with state and frame", "Common incompatible definitions":"Pre/post-wave density; gas/droplet-relative velocity; parent/fragment diameter", "Minimum information for comparison":"All four components and loading stage", "Recommended use":"Conditioned response map; never a universal threshold alone"},
    {"Parameter":"Reynolds number", "Physical meaning":"Inertial transport relative to viscous transport", "Required definition":"Density, velocity, length, viscosity, phase, state, and frame", "Common incompatible definitions":"Gas or liquid viscosity; post-wave or freestream state", "Minimum information for comparison":"All components and thermodynamic state", "Recommended use":"Companion condition, not a substitute for the load history"},
    {"Parameter":"Ohnesorge number", "Physical meaning":"Liquid viscous resistance relative to capillary–inertial response", "Required definition":"Liquid viscosity/density, surface tension, and length scale", "Common incompatible definitions":"Parent versus fragment scale; temperature-dependent properties", "Minimum information for comparison":"Liquid identity, temperature/state, and d definition", "Recommended use":"Material/scale facet for breakup comparisons"},
    {"Parameter":"Loading duration", "Physical meaning":"Time over which a specified pressure/slip load acts", "Required definition":"Start/end events and whether interval is front passage, post-wave residence, or full forcing", "Common incompatible definitions":"Shock transit; compressed-gas residence; time to expansion arrival", "Minimum information for comparison":"Both events, time reference, and load variable", "Recommended use":"Conceptual or within-compatible-case only"},
    {"Parameter":"Breakup time", "Physical meaning":"Interval to a specified deformation or fragmentation event", "Required definition":"Onset, first shedding, sheet rupture, or complete breakup plus normalization", "Common incompatible definitions":"Onset versus completion; dimensional time versus t*", "Minimum information for comparison":"Event definition, scale, imaging/model criterion", "Recommended use":"Event-specific values only"},
    {"Parameter":"Signed ΔSOI", "Physical meaning":"Ordered separation between pilot and main-fuel injection events", "Required definition":"Target SOI minus reference SOI, fuel order, actual/electronic/hydraulic event, and unit", "Common incompatible definitions":"Opposite sign; crank angle versus time; command versus actual SOI", "Minimum information for comparison":"Both named events, sign convention, engine speed for conversions, operating point", "Recommended use":"Condition-faceted chronology tables/plots"},
    {"Parameter":"L_E/L_D", "Physical meaning":"Evaporation distance relative to a named detonation/reaction/refill scale", "Required definition":"Evaporation endpoint and denominator physical length", "Common incompatible definitions":"Front height, cell width, induction length, refill length", "Minimum information for comparison":"Both lengths, chemistry, geometry, wave number, and residence definition", "Recommended use":"Within the reported strong-wave domain only"},
])

tables["TAB-02"] = (["Study/case", "Gas and nozzle", "Pressure definition", "NPR", "Ambient/state", "Transient stage", "x_MD/D or topology metric", "Comparability role"], [
    {"Study/case":"[[CITE:B009]] H2 semi-steady sweep", "Gas and nozzle":"H2; converging exit D=1.5 mm", "Pressure definition":"Nozzle total pressure / ambient static pressure", "NPR":"8.5, 10, 30, 70", "Ambient/state":"98.37 kPa, 296 K", "Transient stage":"semi-steady", "x_MD/D or topology metric":"1.85, 2.06, 3.77, 5.81 (derived from reported x_MD and D)", "Comparability role":"Only numeric series retained for the QSA-01 within-study plot"},
    {"Study/case":"[[CITE:B009]] CH4 case", "Gas and nozzle":"CH4; same D=1.5 mm nozzle", "Pressure definition":"Same total/static definition", "NPR":"8.5", "Ambient/state":"98.37 kPa, 296 K", "Transient stage":"semi-steady", "x_MD/D or topology metric":"1.90 (derived)", "Comparability role":"Gas-species contrast within one setup"},
    {"Study/case":"[[CITE:B021]] steady NPR endpoints", "Gas and nozzle":"H2; convergent exit D=1 mm", "Pressure definition":"Plenum total / chamber static is verified for validation case", "NPR":"Endpoint values appear only in case labels in extracted records", "Ambient/state":"chamber state case-specific", "Transient stage":"steady", "x_MD/D or topology metric":"1.299 and 5.362 reported mm for named endpoint cases", "Comparability role":"Table context only; excluded from QSA-01 because paired ratio records are missing"},
    {"Study/case":"[[CITE:B029]] pressure-build history", "Gas and nozzle":"H2 injector; case-specific internal volume and restriction", "Pressure definition":"Injector-internal p_in(t); location must be retained", "NPR":"time dependent; not digitized", "Ambient/state":"transient test condition", "Transient stage":"opening → formation → motion → stabilization", "x_MD/D or topology metric":"figure-only history", "Comparability role":"FIG-02 event alignment; no pooled numeric entry"},
])

tables["TAB-03"] = (["Paper/case", "Loading type", "Mach definition/value", "We definition/value", "Re / Oh", "d0 and liquid", "Loading duration", "Reported response", "Comparison boundary"], [
    {"Paper/case":"[[CITE:C016]] C01", "Loading type":"incident shock + post-shock airflow", "Mach definition/value":"M_s=1.12, incident shock / preshock sound speed", "We definition/value":"219; rho_a V_i² D_i/sigma, post-shock airflow", "Re / Oh":"Re=13000; Oh=NR", "d0 and liquid":"2.5 mm water", "Loading duration":"NR", "Reported response":"SIE", "Comparison boundary":"Author taxonomy; We definition record remains incomplete at component-ID level"},
    {"Paper/case":"[[CITE:C016]] C02", "Loading type":"incident shock + post-shock airflow", "Mach definition/value":"M_s=1.30", "We definition/value":"1600; same source definition", "Re / Oh":"Re=40000; Oh=NR", "d0 and liquid":"2.9 mm water", "Loading duration":"NR", "Reported response":"SIE", "Comparison boundary":"Not a universal regime threshold"},
    {"Paper/case":"[[CITE:C016]] C03", "Loading type":"incident shock + post-shock airflow", "Mach definition/value":"M_s=1.12", "We definition/value":"44; same source definition", "Re / Oh":"Re=2500; Oh=NR", "d0 and liquid":"0.5 mm water", "Loading duration":"NR", "Reported response":"RTP", "Comparison boundary":"Diameter and Re change with We"},
    {"Paper/case":"[[CITE:C016]] C04", "Loading type":"incident shock + post-shock airflow", "Mach definition/value":"M_s=1.45", "We definition/value":"795; same source definition", "Re / Oh":"Re=12000; Oh=NR", "d0 and liquid":"0.5 mm water", "Loading duration":"NR", "Reported response":"RTP", "Comparison boundary":"Mach and We change together"},
    {"Paper/case":"[[CITE:C025]] M2", "Loading type":"analytic post-shock gas load", "Mach definition/value":"M_s=2", "We definition/value":"822; post-shock rho_g U_r² d0/sigma", "Re / Oh":"NR", "d0 and liquid":"100 µm water", "Loading duration":"NR", "Reported response":"deformation/size/time statistics reported", "Comparison boundary":"Numerical case; response metric must remain source-typed"},
    {"Paper/case":"[[CITE:C025]] M3", "Loading type":"analytic post-shock gas load", "Mach definition/value":"M_s=3", "We definition/value":"3760; same definition", "Re / Oh":"NR", "d0 and liquid":"100 µm water", "Loading duration":"NR", "Reported response":"deformation/size/time statistics reported", "Comparison boundary":"No universal pooling with detonation cases"},
    {"Paper/case":"[[CITE:C014]] C01–C08", "Loading type":"uniform post-shock freestream", "Mach definition/value":"M∞=0.30–1.19, post-shock freestream", "We definition/value":"1050–1160; post-shock rho_g u_g² d0/sigma", "Re / Oh":"Re=2600–24000; Oh=0.002–0.044", "d0 and liquid":"d0=NV in current extraction", "Loading duration":"NR", "Reported response":"numeric response not paired in master table", "Comparison boundary":"Condition context only; excluded from quantitative map"},
    {"Paper/case":"[[CITE:D018]] water/RP-3 sets", "Loading type":"reacting detonation products", "Mach definition/value":"detonation-front Mach about 6.03–7.07", "We definition/value":"3.10×10^4–5.67×10^5; averaged post-detonation state", "Re / Oh":"Oh=0.0039–0.0223", "d0 and liquid":"0.25–1.27 mm water/RP-3", "Loading duration":"reacting-wave history; not reduced to one duration", "Reported response":"complete-breakup t*=10.06 water; 7.90 RP-3", "Comparison boundary":"Reacting strong-wave analogue"},
    {"Paper/case":"[[CITE:D019]] detonation/inert pair", "Loading type":"matched-leading-Mach reacting vs inert", "Mach definition/value":"incident Mach 4.8", "We definition/value":"5.42×10^4 detonation; 3.18×10^5 inert; components not reported in Table I", "Re / Oh":"Re=4.80×10^4 / 2.00×10^5; Oh=NR", "d0 and liquid":"4.8 mm water", "Loading duration":"deformation scale O(10^-4 s)", "Reported response":"different post-wave deformation/cavitation histories", "Comparison boundary":"Equal leading Mach does not imply equal load"},
])

tables["TAB-04"] = (["Configuration", "Paper", "Spacing/cloud descriptor", "Loading", "Main collective mechanism", "Reported response", "Limit for dense spray transfer"], [
    {"Configuration":"isolated droplet", "Paper":"[[CITE:C016]]", "Spacing/cloud descriptor":"NA", "Loading":"incident shock + post-shock airflow", "Main collective mechanism":"none; canonical local response", "Reported response":"SIE/RTP labels under case-specific M_s, We, Re, d0", "Limit for dense spray transfer":"No shielding, attenuation, polydispersity, vaporization, or reaction"},
    {"Configuration":"tandem", "Paper":"[[CITE:C035]]", "Spacing/cloud descriptor":"streamwise S/D=1.2–10.5; critical spacing depends on We", "Loading":"post-shock gas; We=13–180", "Main collective mechanism":"wake shielding and altered trailing-droplet load", "Reported response":"spacing-dependent deformation/breakup; critical S/D decreases with We", "Limit for dense spray transfer":"Ordered pair and one orientation; no universal spacing law"},
    {"Configuration":"parallel", "Paper":"[[CITE:C036]]", "Spacing/cloud descriptor":"transverse L/D below 0.1 to above 2", "Loading":"post-wave gas; We O(10)–O(100)", "Main collective mechanism":"squeeze flow, channel opening/closure, mutual deformation", "Reported response":"bag/trailing/shuttlecock/open/closed author modes", "Limit for dense spray transfer":"Pair-scale phase boundaries depend on orientation and size"},
    {"Configuration":"dilute cloud", "Paper":"[[CITE:C033]] [[CITE:C034]]", "Spacing/cloud descriptor":"cloud volume fraction/surface descriptors; S/D not reported", "Loading":"shock transmission through droplet cloud", "Main collective mechanism":"shock attenuation and fragmentation feedback", "Reported response":"transmitted pressure depends on cloud state; neglecting fragmentation can overpredict pressure", "Limit for dense spray transfer":"Descriptor is not convertible to pair S/D; cloud remains dilute/model-specific"},
    {"Configuration":"dense polydisperse reacting spray target", "Paper":"No direct validation in frozen corpus", "Spacing/cloud descriptor":"requires joint size, spacing, volume fraction, velocity, temperature, and vapor statistics", "Loading":"transient HPDI gas–liquid two-way coupling", "Main collective mechanism":"combined shielding, channel flow, attenuation, vaporization, population feedback", "Reported response":"unresolved", "Limit for dense spray transfer":"Must be measured or validated directly; canonical rows are not a closure"},
])

tables["TAB-05"] = (["Paper", "Liquid / size", "Thermal state", "Loading", "Phase-change state/model", "Dominant physical effect", "Breakup consequence", "Evaporation consequence", "Boundary"], [
    {"Paper":"[[CITE:C024]]", "Liquid / size":"small droplets; exact d0 case-specific", "Thermal state":"high-We heated post-wave flow", "Loading":"shock/post-wave aerodynamic load", "Phase-change state/model":"direct optical disappearance interval", "Dominant physical effect":"fragment cloud formation plus finite heating/evaporation", "Breakup consequence":"high-We fragmentation", "Evaporation consequence":"last discernible clouds disappear at 250–300 µs", "Boundary":"Optical loss is not automatically vapor mass or HPDI mixture gain"},
    {"Paper":"[[CITE:D017]] d0=1–120 µm", "Liquid / size":"modeled parent-size series", "Thermal state":"post-detonation products", "Loading":"detonation-front/post-front history", "Phase-change state/model":"deformation+evaporation; KH-RT; WERT49 branches", "Dominant physical effect":"breakup closure changes surface-area production", "Breakup consequence":"model-dependent child production", "Evaporation consequence":"extinction distance differs by orders of magnitude", "Boundary":"Within-study model comparison only"},
    {"Paper":"[[CITE:D018]] water", "Liquid / size":"d0=0.25–1.20 mm", "Thermal state":"reacting detonation products", "Loading":"high-We reacting wave", "Phase-change state/model":"deformation/breakup observation", "Dominant physical effect":"KHI-dominated growth and complete breakup", "Breakup consequence":"complete-breakup time t*=10.06", "Evaporation consequence":"not paired as a common numeric endpoint", "Boundary":"Strong-wave analogue"},
    {"Paper":"[[CITE:D018]] RP-3", "Liquid / size":"d0=0.27–1.27 mm", "Thermal state":"reacting detonation products", "Loading":"high-We reacting wave", "Phase-change state/model":"deformation/breakup observation", "Dominant physical effect":"liquid-property-dependent breakup", "Breakup consequence":"complete-breakup time t*=7.90", "Evaporation consequence":"not paired as a common numeric endpoint", "Boundary":"Do not convert liquid difference to an HPDI threshold"},
    {"Paper":"[[CITE:D019]]", "Liquid / size":"water d0=4.8 mm", "Thermal state":"reacting detonation versus inert shock", "Loading":"same leading Mach 4.8; different post-wave state", "Phase-change state/model":"resolved thermal/cavitation response", "Dominant physical effect":"reaction heat release changes pressure/velocity-gradient history", "Breakup consequence":"different deformation/cavitation paths", "Evaporation consequence":"thermal history differs despite equal leading Mach", "Boundary":"Leading Mach cannot stand in for post-wave thermochemistry"},
    {"Paper":"[[CITE:D009]]", "Liquid / size":"kerosene d0=2–5 µm", "Thermal state":"RDE refill/reaction environment", "Loading":"rotating detonation", "Phase-change state/model":"L_E/L_D=0.13–0.84", "Dominant physical effect":"liquid persistence changes upstream mixture and wave support", "Breakup consequence":"not isolated from model system", "Evaporation consequence":"larger d0 gives longer normalized evaporation distance", "Boundary":"RDE device scale; no HPDI ignition mapping"},
])

tables["TAB-06"] = (["Paper", "Fuel pair / platform", "Pilot/main order and signed timing", "Geometry / operating condition", "Mixture observation", "Ignition observation", "Heat-release response", "Scope/boundary"], [
    {"Paper":"[[CITE:A007]]", "Fuel pair / platform":"diesel pilot + natural gas; RCEM", "Pilot/main order and signed timing":"gas SOI − pilot SOI = −2.5 to +1.5 ms", "Geometry / operating condition":"paper-specific RCEM state", "Mixture observation":"spatial/temporal jet interaction", "Ignition observation":"pilot and gas ignition use distinct HRR thresholds", "Heat-release response":"timing-dependent HRR characterization", "Scope/boundary":"Do not convert to another sign convention or attribute to shock"},
    {"Paper":"[[CITE:A020]]", "Fuel pair / platform":"diesel pilot + H2; case family", "Pilot/main order and signed timing":"both H2-first and pilot-first; separations 0.07–3.07 ms", "Geometry / operating condition":"case-specific interaction/ambient state", "Mixture observation":"chronology changes encounter state", "Ignition observation":"qualitative/case-conditioned in current extracted record", "Heat-release response":"not paired as one common numeric y metric", "Scope/boundary":"Useful chronology domain; not eligible for pooled timing-response plot"},
    {"Paper":"[[CITE:A022]]", "Fuel pair / platform":"pilot diesel + H2 direct injection", "Pilot/main order and signed timing":"pilot SOI 0.6 ms after H2 SOI", "Geometry / operating condition":"interaction-angle study", "Mixture observation":"angle controls jet intersection/entrainment", "Ignition observation":"geometry-conditioned response", "Heat-release response":"application result remains case-specific", "Scope/boundary":"Geometry and chronology cannot be pooled independently"},
    {"Paper":"[[CITE:A026]]", "Fuel pair / platform":"pilot diesel + H2 engine", "Pilot/main order and signed timing":"H2 electronic SOI 0–30 CA bTDC; pilot electronic SOI 6 CA bTDC", "Geometry / operating condition":"energy share and injection timing varied", "Mixture observation":"timing changes mixture preparation/flame development", "Ignition observation":"timing-conditioned", "Heat-release response":"flame and heat-release behavior changes with timing/energy share", "Scope/boundary":"Electronic events; CA-to-time conversion requires speed and matching events"},
    {"Paper":"[[CITE:A018]]", "Fuel pair / platform":"pilot/main HPDI context", "Pilot/main order and signed timing":"typed SOI separation retained but numeric value NV", "Geometry / operating condition":"paper-specific", "Mixture observation":"chronology-sensitive", "Ignition observation":"injection-to-ignition interval defined", "Heat-release response":"conditioned qualitative evidence", "Scope/boundary":"No numeric timing entry without verified events"},
])

tables["TAB-07"] = (["Paper", "Device/domain", "Fuel/liquid", "Wave descriptor", "d0 / evaporation-breakup scale", "L_E and L_D definition", "Reported behavior", "HPDI-relevant insight", "Transfer limitation"], [
    {"Paper":"[[CITE:D009]]", "Device/domain":"RDE numerical case family", "Fuel/liquid":"kerosene droplets", "Wave descriptor":"mean rotating-wave speed reported by case", "d0 / evaporation-breakup scale":"2–5 µm; L_E/L_D=0.13–0.84", "L_E and L_D definition":"evaporation distance / detonation-front height", "Reported behavior":"larger d0 increases liquid persistence; wave speed decreases in paired 2–4 µm cases", "HPDI-relevant insight":"compare liquid survival with residence/reaction scale", "Transfer limitation":"denominator is RDE-specific"},
    {"Paper":"[[CITE:D017]]", "Device/domain":"detonation experiment/model comparison", "Fuel/liquid":"micrometre fuel droplets", "Wave descriptor":"post-detonation survival region", "d0 / evaporation-breakup scale":"1–120 µm; extinction distance strongly model dependent", "L_E and L_D definition":"not the D009 ratio", "Reported behavior":"breakup closures shorten survival relative to no-breakup branch", "HPDI-relevant insight":"fragment model controls downstream liquid persistence", "Transfer limitation":"reacting post-front state and model closures differ from HPDI"},
    {"Paper":"[[CITE:D018]]", "Device/domain":"planar detonation experiment", "Fuel/liquid":"water and RP-3", "Wave descriptor":"detonation Mach about 6–7", "d0 / evaporation-breakup scale":"0.25–1.27 mm; complete breakup t*=10.06 water, 7.90 RP-3", "L_E and L_D definition":"NA", "Reported behavior":"liquid-dependent KHI-dominated deformation and breakup", "HPDI-relevant insight":"material state and post-wave history matter", "Transfer limitation":"detonation thermochemistry"},
    {"Paper":"[[CITE:D019]]", "Device/domain":"reacting detonation vs inert shock simulation", "Fuel/liquid":"water, d0=4.8 mm", "Wave descriptor":"matched incident Mach 4.8", "d0 / evaporation-breakup scale":"deformation scale O(10^-4 s)", "L_E and L_D definition":"NA", "Reported behavior":"post-wave We/Re and deformation differ strongly", "HPDI-relevant insight":"leading-wave Mach is insufficient", "Transfer limitation":"geometry, chemistry, and size far from HPDI"},
    {"Paper":"[[CITE:D013]]", "Device/domain":"two-phase RDE", "Fuel/liquid":"reported liquid-fuel droplet cases", "Wave descriptor":"rotating-wave structure", "d0 / evaporation-breakup scale":"20 and 30 µm cases reported", "L_E and L_D definition":"NR in current extracted record", "Reported behavior":"lambda-shaped/two-layer wave tendency", "HPDI-relevant insight":"droplet persistence can reorganize wave structure", "Transfer limitation":"device-level feedback has no direct HPDI counterpart"},
])

tables["TAB-08"] = (["Scientific question", "Known physics", "Missing variable/measurement", "Required synchronized diagnostics", "Model requirement", "Why it matters"], [
    {"Scientific question":"What load do actual pilot droplets experience while crossing a transient underexpanded jet?", "Known physics":"Injector transients move shock cells; imposed shocks deform droplets", "Missing variable/measurement":"p[x_d(t),t], rho[x_d(t),t], u_rel(t), direction and duration for the pilot population", "Required synchronized diagnostics":"needle/pressure, density-gradient or pressure field, gas velocity, droplet/ligament tracking", "Model requirement":"validated transient injector flow sampled along measured liquid trajectories", "Why it matters":"A visible Mach disk does not define a unique droplet We or impulse"},
    {"Scientific question":"Which canonical breakup mechanisms survive in dense reacting sprays?", "Known physics":"Wake shielding, squeeze flow, channel closure, and cloud attenuation alter loading", "Missing variable/measurement":"joint size–spacing–velocity–temperature statistics and gas feedback", "Required synchronized diagnostics":"3D/high-speed liquid imaging plus gas pressure/velocity and transmitted-wave measurements", "Model requirement":"population/two-way-coupled model with polydispersity, vaporization, and reaction", "Why it matters":"Ordered-pair laws cannot close dense-spray response"},
    {"Scientific question":"Do wave-created fragments change the pre-ignition HPDI mixture?", "Known physics":"Fragment size, velocity, temperature, and residence control evaporation and transport", "Missing variable/measurement":"mass-resolved fragment field, vapor/species field, thermal state, and time to ignition", "Required synchronized diagnostics":"fragment sizing/tracking, temperature, vapor/species imaging, common event clock", "Model requirement":"product-distribution model coupled to evaporation and turbulent transport", "Why it matters":"Breakup alone does not imply more vapor in the ignition region"},
    {"Scientific question":"Does a wave-induced mixture change alter ignition independently of chronology and momentum?", "Known physics":"SOI order, dwell, geometry, oxygen, temperature, and pilot products control ignition", "Missing variable/measurement":"isolated wave-induced delta-mixture and its overlap with the ignition kernel", "Required synchronized diagnostics":"wave, liquid, species, temperature/radical proxy, ignition location, and heat release", "Model requirement":"uncertainty propagation from load to fragments to mixture to chemistry", "Why it matters":"A shorter ignition delay after pressure increase is not causal proof of wave-mediated breakup"},
    {"Scientific question":"Can loading duration organize response across configurations?", "Known physics":"Front passage, post-wave residence, and deformation clocks are distinct", "Missing variable/measurement":"explicit start/end events for tau_loading and a source-defined response clock", "Required synchronized diagnostics":"event-resolved load history and response morphology", "Model requirement":"test competing clocks without assuming a universal ratio", "Why it matters":"Undefined time ratios create false correlations"},
    {"Scientific question":"Which strong-wave quantities transfer from detonation/RDE to HPDI?", "Known physics":"Local post-wave pressure, density, slip, size, and residence affect droplets", "Missing variable/measurement":"validated mapping of thermochemistry, geometry, residence, population, and reaction scale", "Required synchronized diagnostics":"domain-specific post-wave state and liquid-survival measurements", "Model requirement":"explicit dimensional mapping with failure bounds", "Why it matters":"RDE L_E/L_D is a comparison scale, not an HPDI ignition predictor"},
])

for tid, (fields, rows) in tables.items():
    write_csv(TABLEDIR / f"{tid}.csv", fields, rows)
    write_text(TABLEDIR / f"{tid}.md", f"# {tid}\n\n{md_table(fields, rows)}")


# Table source map expands each reader row into one provenance record per cited Paper ID.
TABLE_SOURCE_FIELDS = ["table_id", "row_id", "paper_id", "case_id", "source_location", "parameter_group", "reported_value_or_category", "definition_status", "condition_summary", "reader_role", "notes"]
table_source_rows: list[dict[str, object]] = []
for tid, (fields, rows) in tables.items():
    for idx, row in enumerate(rows, 1):
        joined = " ".join(str(v) for v in row.values())
        ids = re.findall(r"\[\[CITE:([ABCD]\d{3})\]\]", joined) or ["NA"]
        for paper_id in ids:
            locator = "author synthesis from project definitions"
            if paper_id != "NA":
                locator = "see figure/table row citations and 05_Data_Extraction/master_tables/source_locators.csv"
            table_source_rows.append(dict(table_id=tid, row_id=f"{tid}-R{idx:02d}", paper_id=paper_id, case_id="grouped_or_named_in_row", source_location=locator, parameter_group="definition" if tid == "TAB-01" else "cross-study comparison", reported_value_or_category="; ".join(str(row.get(k, "")) for k in fields[-3:]), definition_status="explicit or limitation stated", condition_summary="; ".join(str(row.get(k, "")) for k in fields[:3]), reader_role="representative comparison; not inventory", notes="Derived values are labelled in the reader row; missing values use NR/NV/NA."))

write_csv(P14 / "table_source_map.csv", TABLE_SOURCE_FIELDS, table_source_rows)


AUDIT_FIELDS = ["analysis_id", "scientific_question", "candidate_x", "candidate_y", "independent_papers", "eligible_cases", "definition_compatibility", "condition_compatibility", "normalization_validity", "dominance_by_single_study", "cross_paper_value", "status", "plot_recommendation", "main_reason", "notes"]
audit_rows = [
    dict(analysis_id="QSA-01", scientific_question="Can definition-complete NPR explain x_MD/D across compatible underexpanded-jet conditions?", candidate_x="contextual NPR", candidate_y="x_MD/D", independent_papers=1, eligible_cases=5, definition_compatibility="pass within B009 only", condition_compatibility="same nozzle/ambient; gas facet retained", normalization_validity="pass; reported x_MD divided by reported D=1.5 mm", dominance_by_single_study="100%", cross_paper_value="none", status="within_study_only", plot_recommendation="B009 H2 line plus CH4 same-NPR marker; label as within-study", main_reason="B021 endpoints lack paired explicit ratio records; other candidate papers lack usable pairs", notes="No cross-paper correlation or fit."),
    dict(analysis_id="QSA-02", scientific_question="Can event-aligned p_inj(t) be related to Mach-disk formation/motion/stabilization?", candidate_x="p_inj(t) or NPR(t)", candidate_y="Mach-disk state/time or x_MD(t)/D", independent_papers=6, eligible_cases=0, definition_compatibility="partial", condition_compatibility="heterogeneous event zeros and pressure locations", normalization_validity="not testable; time_series_points.csv has zero rows", dominance_by_single_study="NA", cross_paper_value="qualitative event sequence", status="qualitative_only", plot_recommendation="FIG-02 conceptual timeline and source-labelled placeholders", main_reason="registered histories are figure-only and were not digitized", notes="No curve digitization undertaken."),
    dict(analysis_id="QSA-03", scientific_question="How do Mach context and definition-complete We relate to deformation/breakup response?", candidate_x="M_s or M_rel plus We", candidate_y="response metric or author breakup mode", independent_papers=0, eligible_cases=0, definition_compatibility="fails strict complete-component requirement", condition_compatibility="inert/reacting, size, liquid, and response definitions differ", normalization_validity="not valid for pooled numeric map", dominance_by_single_study="NA", cross_paper_value="condition table only", status="qualitative_only", plot_recommendation="TAB-03 plus FIG-04 mechanism/observation layout", main_reason="candidate We records are incomplete_reported or lack matched response metrics", notes="C016 and C025 cases remain useful qualitative anchors."),
    dict(analysis_id="QSA-04", scientific_question="Does typed loading duration relative to response time organize breakup?", candidate_x="tau_loading or tau_loading/tau_response", candidate_y="event-specific response", independent_papers=0, eligible_cases=0, definition_compatibility="insufficient typed start/end event pairs", condition_compatibility="heterogeneous loading histories", normalization_validity="not established", dominance_by_single_study="NA", cross_paper_value="hypothesis only", status="qualitative_only", plot_recommendation="conceptual clocks in FIG-03/FIG-09", main_reason="both time definitions are not jointly complete", notes="No plot, fit, or universal correlation."),
    dict(analysis_id="QSA-05", scientific_question="How does d0 condition breakup/evaporation response under matched wave and thermal states?", candidate_x="d0", candidate_y="extinction distance or typed response", independent_papers=1, eligible_cases=21, definition_compatibility="pass within D017 model branches", condition_compatibility="same study; model branch retained", normalization_validity="reported d0 and reported extinction distance; censored >500 values marked", dominance_by_single_study="100%", cross_paper_value="none", status="within_study_only", plot_recommendation="D017 model-branch small multiple/line; no cross-domain pooling", main_reason="other studies use incompatible response endpoints or lack paired case values", notes="Plot demonstrates model sensitivity, not a universal diameter law."),
    dict(analysis_id="QSA-06", scientific_question="How do spacing/cloud descriptors affect collective response?", candidate_x="S/D or typed cloud descriptor", candidate_y="breakup/attenuation response", independent_papers=0, eligible_cases=0, definition_compatibility="descriptor types non-equivalent", condition_compatibility="tandem, parallel, and cloud configurations differ", normalization_validity="S/D cannot be converted to volume fraction/cloud statistic", dominance_by_single_study="NA", cross_paper_value="mechanism comparison", status="qualitative_only", plot_recommendation="FIG-05 and TAB-04", main_reason="no common x/y definition across configurations", notes="No universal critical spacing."),
    dict(analysis_id="QSA-07", scientific_question="How does signed pilot/main chronology relate to mixture/ignition response?", candidate_x="signed ΔSOI", candidate_y="mixture/ignition/combustion response", independent_papers=0, eligible_cases=0, definition_compatibility="timing definitions available for selected studies, but y metrics are not paired", condition_compatibility="fuel order, geometry, event type, and operating point differ", normalization_validity="no valid cross-engine conversion", dominance_by_single_study="NA", cross_paper_value="conditioned chronology table", status="qualitative_only", plot_recommendation="FIG-07 timeline plus TAB-06", main_reason="no condition-compatible paired numeric response registry", notes="Direct timing evidence remains distinct from shock causality."),
    dict(analysis_id="QSA-08", scientific_question="Does typed L_E/L_D organize RDE behavior?", candidate_x="L_E/L_D", candidate_y="mean rotating-wave velocity", independent_papers=1, eligible_cases=3, definition_compatibility="pass within D009", condition_compatibility="same case family; d0 changes; B5 lacks paired wave velocity", normalization_validity="source-typed ratio retained", dominance_by_single_study="100%", cross_paper_value="none", status="within_study_only", plot_recommendation="D009 three-point within-study plot", main_reason="typed ratios are model/device-specific and other studies lack compatible scales", notes="Analogue only; no HPDI mapping."),
    dict(analysis_id="QSA-09", scientific_question="Can generic NPR be pooled against shock metrics?", candidate_x="generic NPR", candidate_y="shock metric", independent_papers=0, eligible_cases=0, definition_compatibility="fail by design", condition_compatibility="not applicable", normalization_validity="invalid", dominance_by_single_study="NA", cross_paper_value="none", status="not_recommended", plot_recommendation="none", main_reason="pressure roles/types/time basis are missing or incompatible", notes="Use QSA-01 only."),
    dict(analysis_id="QSA-10", scientific_question="Can generic Mach/We be pooled into a universal breakup map?", candidate_x="generic Mach/We", candidate_y="breakup regime", independent_papers=0, eligible_cases=0, definition_compatibility="fail by design", condition_compatibility="inert shock, detonation, continuous flow mixed", normalization_validity="invalid", dominance_by_single_study="NA", cross_paper_value="none", status="not_recommended", plot_recommendation="none", main_reason="identical numbers do not represent identical physical states", notes="No universal regime boundary."),
    dict(analysis_id="QSA-11", scientific_question="Can generic breakup time be pooled?", candidate_x="generic breakup time", candidate_y="Mach/We/d0", independent_papers=0, eligible_cases=0, definition_compatibility="fail by design", condition_compatibility="onset/shedding/completion differ", normalization_validity="invalid", dominance_by_single_study="NA", cross_paper_value="none", status="not_recommended", plot_recommendation="none", main_reason="event and time normalization are not common", notes="Retain event-specific times."),
    dict(analysis_id="QSA-12", scientific_question="Can RDE L_E/L_D be mapped quantitatively to HPDI ignition?", candidate_x="RDE L_E/L_D", candidate_y="HPDI ignition/combustion response", independent_papers=0, eligible_cases=0, definition_compatibility="no validated mapping", condition_compatibility="cross-domain mismatch", normalization_validity="invalid", dominance_by_single_study="NA", cross_paper_value="none", status="not_recommended", plot_recommendation="none", main_reason="chemistry, residence, geometry, and denominator scales do not correspond", notes="Use FIG-08/TAB-07 comparison boundary only."),
]
write_csv(QDIR / "quantitative_eligibility_audit.csv", AUDIT_FIELDS, audit_rows)


REG_FIELDS = ["paper_id", "case_id", "x_value", "x_definition", "y_value", "y_definition", "conditions", "normalization", "source_locator", "reported_or_derived", "include_exclude", "exclusion_reason"]
qsa01 = [
    dict(paper_id="B009", case_id="B009-H2-NPR8.5", x_value=8.5, x_definition="P0/P_infinity; total/static", y_value=1.853, y_definition="x_MD/D", conditions="H2; D=1.5 mm; 98.37 kPa; 296 K; semi-steady", normalization="2.78 mm / 1.5 mm", source_locator="LOC-B009-0001;LOC-B009-0003;LOC-B009-0006", reported_or_derived="x reported; y derived", include_exclude="include", exclusion_reason=""),
    dict(paper_id="B009", case_id="B009-H2-NPR10", x_value=10, x_definition="P0/P_infinity; total/static", y_value=2.060, y_definition="x_MD/D", conditions="H2; same setup; semi-steady", normalization="3.09/1.5", source_locator="LOC-B009-0001;LOC-B009-0003;LOC-B009-0006", reported_or_derived="x reported; y derived", include_exclude="include", exclusion_reason=""),
    dict(paper_id="B009", case_id="B009-H2-NPR30", x_value=30, x_definition="P0/P_infinity; total/static", y_value=3.767, y_definition="x_MD/D", conditions="H2; same setup; semi-steady", normalization="5.65/1.5", source_locator="LOC-B009-0001;LOC-B009-0003;LOC-B009-0006", reported_or_derived="x reported; y derived", include_exclude="include", exclusion_reason=""),
    dict(paper_id="B009", case_id="B009-H2-NPR70", x_value=70, x_definition="P0/P_infinity; total/static", y_value=5.813, y_definition="x_MD/D", conditions="H2; same setup; semi-steady", normalization="8.72/1.5", source_locator="LOC-B009-0001;LOC-B009-0003;LOC-B009-0006", reported_or_derived="x reported; y derived", include_exclude="include", exclusion_reason=""),
    dict(paper_id="B009", case_id="B009-CH4-NPR8.5", x_value=8.5, x_definition="P0/P_infinity; total/static", y_value=1.900, y_definition="x_MD/D", conditions="CH4; same nozzle/ambient; semi-steady", normalization="2.85/1.5", source_locator="LOC-B009-0001;LOC-B009-0003;LOC-B009-0006", reported_or_derived="x reported; y derived", include_exclude="include", exclusion_reason=""),
    dict(paper_id="B021", case_id="B021-NPR5", x_value="NV", x_definition="NPR only encoded in case label; no paired ratio row", y_value=1.299, y_definition="reported x_MD in mm; D=1 mm", conditions="steady H2 numerical endpoint", normalization="not accepted for registry plot", source_locator="LOC-B021-0002;LOC-B021-0004", reported_or_derived="y reported", include_exclude="exclude", exclusion_reason="missing explicit paired NPR record"),
    dict(paper_id="B021", case_id="B021-NPR60", x_value="NV", x_definition="NPR only encoded in case label; no paired ratio row", y_value=5.362, y_definition="reported x_MD in mm; D=1 mm", conditions="steady H2 numerical endpoint", normalization="not accepted for registry plot", source_locator="LOC-B021-0002;LOC-B021-0004", reported_or_derived="y reported", include_exclude="exclude", exclusion_reason="missing explicit paired NPR record"),
    dict(paper_id="B003", case_id="ALL", x_value="NV", x_definition="candidate study", y_value="NV", y_definition="no paired case values in master table", conditions="NR", normalization="NA", source_locator="NV", reported_or_derived="NV", include_exclude="exclude", exclusion_reason="no eligible paired records"),
    dict(paper_id="B025", case_id="ALL", x_value="NV", x_definition="candidate study", y_value="NV", y_definition="no paired case values in master table", conditions="NR", normalization="NA", source_locator="NV", reported_or_derived="NV", include_exclude="exclude", exclusion_reason="no eligible paired records"),
    dict(paper_id="B030", case_id="ALL", x_value="NV", x_definition="candidate study", y_value="NV", y_definition="no paired case values in master table", conditions="NR", normalization="NA", source_locator="NV", reported_or_derived="NV", include_exclude="exclude", exclusion_reason="no eligible paired records"),
]
write_csv(REGDIR / "QSA-01.csv", REG_FIELDS, qsa01)

diameters = [1, 5, 10, 15, 40, 90, 120]
branches = {
    "no_breakup": [0.84, 13.32, 37.05, 71.25, ">500", ">500", ">500"],
    "KH-RT": [0.04, 0.12, 0.32, 0.46, 0.98, 2.25, 2.97],
    "WERT49": [0.075, 0.41, 0.93, 1.29, 3.78, 8.76, 11.96],
}
qsa05 = []
for branch, vals in branches.items():
    for d, val in zip(diameters, vals):
        qsa05.append(dict(paper_id="D017", case_id=f"D017-D{d}-{branch}", x_value=d, x_definition="modeled parent diameter in µm", y_value=val, y_definition="predicted extinction distance in mm", conditions="same detonation-study model family; branch retained", normalization="none", source_locator="LOC-D017-0006;LOC-D017-0007", reported_or_derived="reported", include_exclude="include_censored" if isinstance(val, str) and val.startswith(">") else "include", exclusion_reason=""))
for pid, reason in [("C024", "evaporation interval not paired to d0 cases"), ("C026", "qualitative response only"), ("C027", "no compatible paired response"), ("D009", "response is RDE device scale; audited separately in QSA-08"), ("D014", "trajectory/location response not paired to common d0 metric"), ("D018", "breakup time grouped by liquid rather than individual d0 case")]:
    qsa05.append(dict(paper_id=pid, case_id="ALL", x_value="NV", x_definition="candidate d0", y_value="NV", y_definition="candidate response", conditions="study-specific", normalization="NA", source_locator="NV", reported_or_derived="NV", include_exclude="exclude", exclusion_reason=reason))
write_csv(REGDIR / "QSA-05.csv", REG_FIELDS, qsa05)

qsa08 = [
    dict(paper_id="D009", case_id="D009-B2", x_value=0.13, x_definition="evaporation distance / detonation-front height", y_value=1728, y_definition="mean rotating-detonation wave velocity, m/s", conditions="kerosene; d0=2 µm; same model family", normalization="source ratio retained", source_locator="LOC-D009-0005;LOC-D009-0006;LOC-D009-0007", reported_or_derived="reported", include_exclude="include", exclusion_reason=""),
    dict(paper_id="D009", case_id="D009-B3", x_value=0.31, x_definition="same", y_value=1696, y_definition="mean wave velocity, m/s", conditions="kerosene; d0=3 µm", normalization="source ratio retained", source_locator="LOC-D009-0005;LOC-D009-0006;LOC-D009-0007", reported_or_derived="reported", include_exclude="include", exclusion_reason=""),
    dict(paper_id="D009", case_id="D009-B4", x_value=0.55, x_definition="same", y_value=1618, y_definition="mean wave velocity, m/s", conditions="kerosene; d0=4 µm", normalization="source ratio retained", source_locator="LOC-D009-0005;LOC-D009-0006;LOC-D009-0007", reported_or_derived="reported", include_exclude="include", exclusion_reason=""),
    dict(paper_id="D009", case_id="D009-B5", x_value=0.84, x_definition="same", y_value="NV", y_definition="mean wave velocity absent in current paired record", conditions="kerosene; d0=5 µm", normalization="source ratio retained", source_locator="LOC-D009-0005;LOC-D009-0006", reported_or_derived="reported x", include_exclude="exclude", exclusion_reason="missing paired y value"),
]
for pid in ("D006", "D007", "D008", "D010", "D011", "D012", "D013", "D015"):
    qsa08.append(dict(paper_id=pid, case_id="ALL", x_value="NV", x_definition="typed L_E/L_D unavailable or incompatible", y_value="NV", y_definition="device response not paired", conditions="RDE/detonation study-specific", normalization="NA", source_locator="NV", reported_or_derived="NV", include_exclude="exclude", exclusion_reason="missing or incompatible ratio/response definition"))
write_csv(REGDIR / "QSA-08.csv", REG_FIELDS, qsa08)


# Captions
figure_caption_lines = ["# Phase 14 Working Figure Captions", ""]
caption_texts = {
    "FIG-01":"Unified injector-to-ignition mechanism framework. Injector motion and p_inj(t) create a transient underexpanded wave field; local p, rho, u and trajectory sampling determine liquid loading; deformation and breakup create fragment populations whose transport, thermal state and residence condition phase change and mixture redistribution. Four dashed measurement gates retain the unresolved actual pilot load, dense-spray transfer, fragment-to-mixture contribution and mixture-to-ignition contribution. Author synthesis based on [[CITE:B009]] [[CITE:B021]] [[CITE:C016]] [[CITE:C035]] [[CITE:C024]] [[CITE:A007]] [[CITE:A022]].",
    "FIG-02":"Event-aligned injector and underexpanded-wave evolution from valve/needle opening through pressure build-up, choking, Mach-disk appearance, overshoot and stabilization. Literature placeholders: B009 Figs. 5–8 [[CITE:B009]]; B021 Figs. 18–19 [[CITE:B021]]; B029 Figs. 8–12 [[CITE:B029]]. Reuse status pending except as noted in the reuse strategy; timing traces are conceptual because no machine-readable time-series points were available.",
    "FIG-03":"Eulerian wave field to Lagrangian pilot-droplet forcing. The relevant histories are p[x_d(t),t], rho[x_d(t),t], u_rel(t), load direction and duration, not the visible shock topology alone. Author synthesis based on gas-jet and canonical shock–droplet studies [[CITE:B009]] [[CITE:B021]] [[CITE:C007]] [[CITE:C016]]. Actual HPDI pilot-droplet histories remain unresolved.",
    "FIG-04":"Compressible droplet deformation and breakup. Representative observation placeholders identify early shock response, deformation and fragment formation; the author mechanism synthesis separates internal pressure/circulation, flattening, RT-type piercing, KH/shear stripping, capillary competition, sheet/rim formation and ligaments. Sources: C016 Fig. 6 [[CITE:C016]] (CC BY 4.0); C025 Figs. 4–6 [[CITE:C025]] and D018 Figs. 15–16 [[CITE:D018]] (reuse status pending).",
    "FIG-05":"Progression from isolated droplets to tandem, parallel and cloud configurations, followed by an open transfer gate to dense polydisperse reacting spray. Tandem and parallel placeholders are C035 Fig. 4 [[CITE:C035]] and C036 Figs. 5–7 [[CITE:C036]]; cloud mechanisms are synthesized from [[CITE:C033]] [[CITE:C034]]. Pair/cloud observations do not establish a universal dense-HPDI scaling.",
    "FIG-06":"Fragment population, transport, conditional phase change and mixture redistribution. The author synthesis tracks size, velocity, surface area and thermal distributions and separates vapor-layer shear suppression from heating/surface-tension promotion. C024 Figs. 7–8 [[CITE:C024]] are retained as a permission-pending observation placeholder. Breakup is not treated as a necessary increase in HPDI vapor or mixing.",
    "FIG-07":"Signed pilot/main chronology, jet intersection, pilot-product state, mixture stratification, ignition kernel and heat release. Geometry is redrawn from physical facts in A022 [[CITE:A022]]; A026 timing/flame panels [[CITE:A026]] and A007 ignition-delay graph [[CITE:A007]] remain rights-conditioned placeholders. Direct timing effects are not attributed to shock-mediated atomization.",
    "FIG-08":"Strong-wave droplet analogues. D018 reacting-wave observations [[CITE:D018]] and D019 reacting/inert contours [[CITE:D019]] remain permission-pending placeholders. The author comparison separates shared local p/rho/u, size and residence variables from detonation reaction-zone, RDE refill and HPDI geometry/ignition scales. Strong-wave results are a comparison domain only.",
    "FIG-09":"Integrated competing clocks and transported variables from injector opening to ignition. The figure organizes wave, droplet, instability, fragment, evaporation, mixing and ignition times and identifies four missing synchronized measurements in physical language. Author synthesis based on [[CITE:B009]] [[CITE:C016]] [[CITE:C035]] [[CITE:C024]] [[CITE:A007]] [[CITE:D009]].",
}
for fid in sorted(caption_texts):
    figure_caption_lines.extend([f"## {fid}", "", caption_texts[fid], ""])
write_text(P14 / "working_figure_captions.md", "\n".join(figure_caption_lines))

table_caption_titles = {
    "TAB-01":"Parameter definitions and cross-study comparability. The table states the minimum physical definition required before NPR, Mach, We, Re, Oh, duration, breakup time, signed ΔSOI or L_E/L_D can be compared.",
    "TAB-02":"Representative underexpanded-jet comparison domains. Reported conditions and derived x_MD/D values are separated from figure-only transient histories; the table is not a gas-jet paper inventory.",
    "TAB-03":"Compressible droplet-response conditions and regimes. Mach frame, We definition, d0, liquid, duration and response taxonomy remain visible; no universal Weber threshold is inferred.",
    "TAB-04":"Collective effects and transfer limits from isolated droplets through tandem, parallel and cloud configurations to the unresolved dense-spray target.",
    "TAB-05":"Fragment and phase-change coupling across size, thermal state, loading and model conditions, allowing promotion, suppression, negligible or mixed behavior.",
    "TAB-06":"HPDI chronology, mixture, ignition and combustion cases with explicit fuel order, timing definition, geometry and operating boundary.",
    "TAB-07":"Detonation/RDE strong-wave comparison with source-typed evaporation/breakup scales and explicit limits on HPDI transfer.",
    "TAB-08":"Unresolved physical couplings and the synchronized measurements and model outputs required to resolve them; internal project identifiers are omitted from reader-facing content.",
}
table_caption_lines = ["# Phase 14 Working Table Captions", ""]
for tid in sorted(table_caption_titles):
    table_caption_lines.extend([f"## {tid}", "", table_caption_titles[tid], ""])
write_text(P14 / "working_table_captions.md", "\n".join(table_caption_lines))


# Vector and PNG working figures.
W, H = 1600, 1000
COLORS = {"ink":"#17324D", "blue":"#2F6690", "cyan":"#D9EEF4", "orange":"#E69F00", "gold":"#F6D55C", "green":"#4C956C", "mint":"#DCEFE3", "red":"#C4493D", "pink":"#F5DFDC", "gray":"#66717E", "light":"#F5F7F8", "line":"#A9B4BE", "white":"#FFFFFF"}

try:
    FONT_REG = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 25)
    FONT_SMALL = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 20)
    FONT_BOLD = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 31)
    FONT_TITLE = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 42)
except OSError:
    FONT_REG = FONT_SMALL = FONT_BOLD = FONT_TITLE = ImageFont.load_default()


def xml_escape(text: str) -> str:
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def text_lines(text: str, width: int) -> list[str]:
    return wrap(text, max(8, width // 13), break_long_words=False) or [""]


def add_box_svg(parts: list[str], box: tuple[int,int,int,int], text: str, fill: str, stroke: str, dashed: bool=False, font_size: int=24) -> None:
    x,y,w,h = box
    dash = ' stroke-dasharray="10 7"' if dashed else ""
    parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="18" fill="{fill}" stroke="{stroke}" stroke-width="3"{dash}/>' )
    lines = text_lines(text, w-30)
    start_y = y + h/2 - (len(lines)-1)*font_size*0.58
    for i,line in enumerate(lines):
        parts.append(f'<text x="{x+w/2}" y="{start_y+i*font_size*1.18:.1f}" text-anchor="middle" font-family="Arial" font-size="{font_size}" fill="{COLORS["ink"]}">{xml_escape(line)}</text>')


def add_arrow_svg(parts: list[str], a: tuple[int,int], b: tuple[int,int], dashed: bool=False, color: str|None=None) -> None:
    color = color or COLORS["blue"]
    dash = ' stroke-dasharray="10 8"' if dashed else ""
    parts.append(f'<line x1="{a[0]}" y1="{a[1]}" x2="{b[0]}" y2="{b[1]}" stroke="{color}" stroke-width="4" marker-end="url(#arrow)"{dash}/>' )


def add_box_png(draw: ImageDraw.ImageDraw, box: tuple[int,int,int,int], text: str, fill: str, stroke: str, dashed: bool=False) -> None:
    x,y,w,h=box
    draw.rounded_rectangle((x,y,x+w,y+h), radius=18, fill=fill, outline=stroke, width=3)
    if dashed:
        for xx in range(x+8, x+w-8, 22):
            draw.line((xx,y, min(xx+12,x+w),y), fill=stroke, width=4)
            draw.line((xx,y+h, min(xx+12,x+w),y+h), fill=stroke, width=4)
    lines=text_lines(text,w-30)
    bbox=[draw.textbbox((0,0),line,font=FONT_REG) for line in lines]
    total=len(lines)*31
    yy=y+h/2-total/2
    for line,b in zip(lines,bbox):
        tw=b[2]-b[0]
        draw.text((x+w/2-tw/2,yy),line,font=FONT_REG,fill=COLORS["ink"])
        yy+=31


def add_arrow_png(draw: ImageDraw.ImageDraw, a: tuple[int,int], b: tuple[int,int], dashed: bool=False, color: str|None=None) -> None:
    color=color or COLORS["blue"]
    if dashed:
        segments=12
        for i in range(0,segments,2):
            t1=i/segments; t2=min(1,(i+1)/segments)
            draw.line((a[0]+(b[0]-a[0])*t1,a[1]+(b[1]-a[1])*t1,a[0]+(b[0]-a[0])*t2,a[1]+(b[1]-a[1])*t2),fill=color,width=4)
    else:
        draw.line((a,b),fill=color,width=4)
    angle=math.atan2(b[1]-a[1],b[0]-a[0])
    s=15
    p1=(b[0]-s*math.cos(angle-0.55),b[1]-s*math.sin(angle-0.55))
    p2=(b[0]-s*math.cos(angle+0.55),b[1]-s*math.sin(angle+0.55))
    draw.polygon((b,p1,p2),fill=color)


def build_figure(fid: str, title: str, boxes: list[tuple[tuple[int,int,int,int],str,str,str,bool]], arrows: list[tuple[tuple[int,int],tuple[int,int],bool,str]], notes: list[tuple[int,int,str,str]], footer: str) -> None:
    parts=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">', f'<rect width="{W}" height="{H}" fill="{COLORS["white"]}"/>', '<defs><marker id="arrow" markerWidth="12" markerHeight="12" refX="10" refY="6" orient="auto"><path d="M0,0 L12,6 L0,12 z" fill="#2F6690"/></marker></defs>', f'<text x="70" y="70" font-family="Arial" font-weight="700" font-size="42" fill="{COLORS["ink"]}">{xml_escape(fid + "  " + title)}</text>']
    image=Image.new("RGB",(W,H),"white")
    draw=ImageDraw.Draw(image)
    draw.text((70,28),f"{fid}  {title}",font=FONT_TITLE,fill=COLORS["ink"])
    for box,text,fill,stroke,dashed in boxes:
        add_box_svg(parts,box,text,fill,stroke,dashed)
        add_box_png(draw,box,text,fill,stroke,dashed)
    for a,b,dashed,color in arrows:
        add_arrow_svg(parts,a,b,dashed,color)
        add_arrow_png(draw,a,b,dashed,color)
    for x,y,text,color in notes:
        for j,line in enumerate(text_lines(text,500)):
            parts.append(f'<text x="{x}" y="{y+j*27}" font-family="Arial" font-size="22" fill="{color}">{xml_escape(line)}</text>')
            draw.text((x,y-22+j*27),line,font=FONT_SMALL,fill=color)
    parts.append(f'<line x1="70" y1="930" x2="1530" y2="930" stroke="{COLORS["line"]}" stroke-width="2"/>')
    parts.append(f'<text x="70" y="968" font-family="Arial" font-size="20" fill="{COLORS["gray"]}">{xml_escape(footer)}</text>')
    draw.line((70,930,1530,930),fill=COLORS["line"],width=2)
    draw.text((70,946),footer,font=FONT_SMALL,fill=COLORS["gray"])
    parts.append('</svg>')
    write_text(DRAFTDIR/f"{fid}.svg","\n".join(parts))
    image.save(PREVIEWDIR/f"{fid}.png")


fig_defs = {
"FIG-01": (
    "Unified injector-to-ignition mechanism framework",
    [((70,130,250,120),"Injector opening\nneedle/valve, A_eff",COLORS["cyan"],COLORS["blue"],False),((380,130,250,120),"Boundary history\np_inj(t), NPR(t)",COLORS["cyan"],COLORS["blue"],False),((690,130,250,120),"Underexpanded field\nMach disk, shocks, vortices",COLORS["cyan"],COLORS["blue"],False),((1000,130,250,120),"Local gas state\np(x,t), rho(x,t), u(x,t)",COLORS["cyan"],COLORS["blue"],False),((1280,130,250,120),"Trajectory sampling\nx_d(t), u_rel(t), duration",COLORS["pink"],COLORS["red"],True),((70,430,250,120),"Liquid response\ninternal wave, deformation",COLORS["mint"],COLORS["green"],False),((380,430,250,120),"Instability competition\nRT ↔ KH/shear ↔ capillary",COLORS["mint"],COLORS["green"],False),((690,430,250,120),"Fragment population\nd, v, T distributions",COLORS["pink"],COLORS["red"],True),((1000,430,250,120),"Transport & phase change\nresidence, evaporation",COLORS["mint"],COLORS["green"],False),((1280,430,250,120),"Mixture → ignition\nspecies, kernel, heat release",COLORS["pink"],COLORS["red"],True)],
    [((320,190),(380,190),False,COLORS["blue"]),((630,190),(690,190),False,COLORS["blue"]),((940,190),(1000,190),False,COLORS["blue"]),((1250,190),(1280,190),True,COLORS["red"]),((1405,250),(195,430),True,COLORS["red"]),((320,490),(380,490),False,COLORS["green"]),((630,490),(690,490),True,COLORS["red"]),((940,490),(1000,490),False,COLORS["green"]),((1250,490),(1280,490),True,COLORS["red"])],
    [(90,650,"Open measurements: actual pilot load • dense-spray transfer • fragment-to-mixture transport • mixture-to-ignition attribution",COLORS["red"]),(90,835,"Solid = physical progression within native configurations; dashed = unresolved cross-scale quantity.",COLORS["gray"])],
    "Author synthesis. No literature image copied. Citations and boundary conditions are listed in FIG-01_spec.md."),
"FIG-02": (
    "Transient injection and underexpanded-wave evolution",
    [((80,130,220,100),"Valve/needle opening",COLORS["cyan"],COLORS["blue"],False),((350,130,220,100),"p_inj(t) rises\nA_eff changes",COLORS["cyan"],COLORS["blue"],False),((620,130,220,100),"Choking",COLORS["cyan"],COLORS["blue"],False),((890,130,220,100),"Mach disk appears\nand moves",COLORS["cyan"],COLORS["blue"],False),((1160,130,220,100),"Overshoot",COLORS["cyan"],COLORS["blue"],False),((1380,130,160,100),"Stabilized",COLORS["cyan"],COLORS["blue"],False),((90,420,430,260),"Panel B placeholder\nB009 Figs. 5–8\ntransient simulation contours\npermission required",COLORS["light"],COLORS["gray"],True),((585,420,430,260),"Panel C placeholder\nB021 Figs. 18–19\nunsteady one-jet topology\nlicense unknown",COLORS["light"],COLORS["gray"],True),((1080,420,430,260),"Panel D placeholder\nB029 Figs. 8–12\npressure build-up / wave evolution\nCC BY-NC-ND: internal preview",COLORS["light"],COLORS["gray"],True)],
    [((300,180),(350,180),False,COLORS["blue"]),((570,180),(620,180),False,COLORS["blue"]),((840,180),(890,180),False,COLORS["blue"]),((1110,180),(1160,180),False,COLORS["blue"]),((1380,180),(1380,180),False,COLORS["blue"])],
    [(100,315,"Conceptual event alignment only: pressure location and time zero remain study specific.",COLORS["gray"]),(100,760,"QSA-01 inset is within B009 only; no cross-paper fit.",COLORS["red"])],
    "Hybrid layout draft. Literature panels are provenance-labelled placeholders pending final rights decisions."),
"FIG-03": (
    "Eulerian wave field → Lagrangian pilot-droplet forcing",
    [((80,150,350,230),"Eulerian gas field\np(x,t)\nrho(x,t)\nu(x,t)\nshocks + vortices",COLORS["cyan"],COLORS["blue"],False),((600,150,360,230),"Moving liquid trajectory\nx_d(t), u_d(t)\nsample the gas field\nalong each droplet",COLORS["mint"],COLORS["green"],False),((1130,150,380,230),"Lagrangian load\np[x_d(t),t]\nrho[x_d(t),t]\nu_rel(t), direction, duration",COLORS["pink"],COLORS["red"],True),((170,530,330,160),"Pressure impulse\nfront passage",COLORS["light"],COLORS["blue"],False),((635,530,330,160),"Post-wave slip\naerodynamic work",COLORS["light"],COLORS["blue"],False),((1100,530,330,160),"Liquid response clocks\nacoustic, acceleration, instability",COLORS["light"],COLORS["green"],False)],
    [((430,265),(600,265),False,COLORS["blue"]),((960,265),(1130,265),True,COLORS["red"]),((1330,380),(1330,530),True,COLORS["red"]),((500,610),(635,610),False,COLORS["blue"]),((965,610),(1100,610),False,COLORS["green"])],
    [(110,790,"Actual HPDI pilot histories are not measured together; tau_loading/tau_response remains an organizing hypothesis.",COLORS["red"])],
    "Author synthesis. Open dashed gate prevents Mach-disk topology from being read as a known pilot-droplet load."),
"FIG-04": (
    "Compressible droplet deformation and breakup",
    [((80,130,420,220),"Panel A placeholder\nC016 Fig. 6\nshadowgraph: SIE / RTP\nCC BY 4.0",COLORS["light"],COLORS["gray"],True),((590,130,420,220),"Panel B placeholder\nC025 Figs. 4–6\ndeformation contours\npermission pending",COLORS["light"],COLORS["gray"],True),((1100,130,420,220),"Panel C placeholder\nD018 Figs. 15–16\nreacting-wave breakup\ncomparison domain",COLORS["light"],COLORS["gray"],True),((80,520,250,120),"Shock arrival\ninternal pressure",COLORS["cyan"],COLORS["blue"],False),((390,520,250,120),"Flattening\ninternal circulation",COLORS["mint"],COLORS["green"],False),((700,450,250,100),"RT-type piercing",COLORS["pink"],COLORS["red"],False),((700,590,250,100),"KH / shear stripping",COLORS["mint"],COLORS["green"],False),((1020,520,220,120),"Sheet / rim",COLORS["cyan"],COLORS["blue"],False),((1300,520,220,120),"Ligaments → fragments",COLORS["mint"],COLORS["green"],False)],
    [((330,580),(390,580),False,COLORS["blue"]),((640,580),(700,500),False,COLORS["red"]),((640,580),(700,640),False,COLORS["green"]),((950,500),(1020,580),False,COLORS["red"]),((950,640),(1020,580),False,COLORS["green"]),((1240,580),(1300,580),False,COLORS["blue"])],
    [(100,770,"Condition perimeter: Mach frame • We components • Re • Oh • d0 • density ratio • loading duration",COLORS["gray"])],
    "Hybrid layout draft. Observation panels remain source data; mechanism cascade is an original synthesis."),
"FIG-05": (
    "From isolated droplets to collective spray response",
    [((50,160,230,180),"Isolated\ncanonical local load",COLORS["cyan"],COLORS["blue"],False),((340,160,260,180),"Tandem placeholder\nC035 Fig. 4\nwake shielding",COLORS["light"],COLORS["gray"],True),((660,160,260,180),"Parallel placeholder\nC036 Figs. 5–7\nchannel flow",COLORS["light"],COLORS["gray"],True),((980,160,250,180),"Cloud\nshock attenuation\nfragment feedback",COLORS["mint"],COLORS["green"],False),((1300,160,250,180),"Dense HPDI target\npolydisperse, vaporizing, reacting",COLORS["pink"],COLORS["red"],True),((170,520,260,130),"Wake shielding\nreduced trailing slip",COLORS["light"],COLORS["blue"],False),((510,520,260,130),"Squeeze flow\nchannel closure",COLORS["light"],COLORS["blue"],False),((850,520,260,130),"Wave attenuation\ntransmitted impulse",COLORS["light"],COLORS["green"],False),((1190,520,260,130),"Population feedback\nsize–spacing–vapor",COLORS["pink"],COLORS["red"],True)],
    [((280,250),(340,250),False,COLORS["blue"]),((600,250),(660,250),False,COLORS["blue"]),((920,250),(980,250),False,COLORS["green"]),((1230,250),(1300,250),True,COLORS["red"]),((430,585),(510,585),False,COLORS["blue"]),((770,585),(850,585),False,COLORS["green"]),((1110,585),(1190,585),True,COLORS["red"])],
    [(120,780,"No universal S/D or cloud-descriptor scaling closes the dense reacting spray target.",COLORS["red"])],
    "Hybrid layout draft. Ordered-pair and cloud observations are not labelled as dense-spray validation."),
"FIG-06": (
    "Fragment state to mixture redistribution",
    [((70,150,330,220),"Fragment population\nnumber/mass size distributions\nvelocity + temperature\nsurface area",COLORS["mint"],COLORS["green"],False),((500,110,330,170),"Branch 1\nvapor-layer / blowing\nreduces interfacial shear",COLORS["cyan"],COLORS["blue"],False),((500,330,330,170),"Branch 2\nheating lowers surface tension\nand may promote deformation",COLORS["pink"],COLORS["red"],False),((930,150,280,220),"Transport clocks\nacceleration\nresidence\nturbulent dispersion",COLORS["cyan"],COLORS["blue"],False),((1310,150,240,220),"Evaporation / vapor\nconditional rate",COLORS["mint"],COLORS["green"],False),((270,620,420,190),"Observation placeholder\nC024 Figs. 7–8\nfragment cloud and disappearance\npermission pending",COLORS["light"],COLORS["gray"],True),((930,620,420,190),"HPDI mixture contribution\nspecies + equivalence ratio\nat ignition-sensitive location",COLORS["pink"],COLORS["red"],True)],
    [((400,260),(500,195),False,COLORS["blue"]),((400,260),(500,415),False,COLORS["red"]),((830,195),(930,260),False,COLORS["blue"]),((830,415),(930,260),False,COLORS["red"]),((1210,260),(1310,260),False,COLORS["green"]),((1430,370),(1140,620),True,COLORS["red"])],
    [(90,835,"Breakup ≠ necessarily faster evaporation ≠ necessarily improved HPDI mixing.",COLORS["red"])],
    "Author-synthesis dominant hybrid. The open gate requires fragment transport before ignition, not a one-way benefit arrow."),
"FIG-07": (
    "HPDI chronology, mixture preparation, and ignition",
    [((70,130,240,110),"Pilot SOI",COLORS["cyan"],COLORS["blue"],False),((360,130,240,110),"Gas SOI",COLORS["cyan"],COLORS["blue"],False),((650,130,240,110),"Jet intersection",COLORS["mint"],COLORS["green"],False),((940,130,240,110),"Pilot products +\nmixture stratification",COLORS["mint"],COLORS["green"],False),((1230,130,300,110),"Ignition kernel →\nheat release",COLORS["pink"],COLORS["red"],False),((80,420,430,240),"Panel B redraw/placeholder\nA022 Fig. 2\njet geometry\nCC BY 4.0; redraw preferred",COLORS["light"],COLORS["gray"],True),((585,420,430,240),"Panel C placeholder\nA026 Figs. 9–13\ntiming/flame response\nCC BY-NC: venue check",COLORS["light"],COLORS["gray"],True),((1090,420,430,240),"Panel D placeholder\nA007 Fig. 10\ntiming/ignition delay\npermission required",COLORS["light"],COLORS["gray"],True)],
    [((310,185),(360,185),False,COLORS["blue"]),((600,185),(650,185),False,COLORS["blue"]),((890,185),(940,185),False,COLORS["green"]),((1180,185),(1230,185),False,COLORS["green"])],
    [(100,315,"Signed ΔSOI must retain fuel order and event definitions.",COLORS["gray"]),(100,770,"Wave-mediated fragment → mixture → ignition path remains unisolated (dashed scientific hypothesis only).",COLORS["red"])],
    "Hybrid layout draft. Direct chronology evidence is separated from any shock-to-ignition claim."),
"FIG-08": (
    "Strong-wave droplet analogues",
    [((80,140,580,260),"Panel A placeholder\nD018 Figs. 4–6\nreacting-wave droplet response\npermission required",COLORS["light"],COLORS["gray"],True),((940,140,580,260),"Panel B placeholder\nD019 Figs. 8–15\nreacting vs inert at matched leading Mach\npermission required",COLORS["light"],COLORS["gray"],True),((120,560,580,180),"Shared local variables\npost-wave p, rho, u\nd0 and fragment population\nresidence / survival",COLORS["mint"],COLORS["green"],False),((900,560,580,180),"Domain-specific scales\ndetonation reaction zone\nRDE refill/front height\nHPDI geometry + ignition clock",COLORS["pink"],COLORS["red"],True)],
    [((700,650),(900,650),True,COLORS["red"])],
    [(140,835,"Leading Mach equality does not preserve post-wave thermochemistry; L_E/L_D has no validated HPDI mapping.",COLORS["red"])],
    "Hybrid layout draft. Detonation/RDE are comparison domains, not HPDI evidence."),
"FIG-09": (
    "Integrated multiscale coupling and research priorities",
    [((50,150,170,120),"Injector time",COLORS["cyan"],COLORS["blue"],False),((245,150,170,120),"Wave time",COLORS["cyan"],COLORS["blue"],False),((440,150,170,120),"Droplet response",COLORS["mint"],COLORS["green"],False),((635,150,170,120),"Instability",COLORS["mint"],COLORS["green"],False),((830,150,170,120),"Fragment response",COLORS["mint"],COLORS["green"],False),((1025,150,170,120),"Evaporation",COLORS["cyan"],COLORS["blue"],False),((1220,150,170,120),"Mixing",COLORS["cyan"],COLORS["blue"],False),((1415,150,140,120),"Ignition",COLORS["pink"],COLORS["red"],False),((80,430,330,170),"Missing: trajectory load\np, rho, u_rel, duration",COLORS["pink"],COLORS["red"],True),((460,430,330,170),"Missing: dense population\nsize–spacing–gas feedback",COLORS["pink"],COLORS["red"],True),((840,430,330,170),"Missing: fragment → vapor\nmass, T, residence, species",COLORS["pink"],COLORS["red"],True),((1220,430,330,170),"Missing: mixture → ignition\nseparate timing/momentum",COLORS["pink"],COLORS["red"],True),((300,720,1000,110),"Transported variables: boundary history → local p/rho/u → liquid d/v/T distributions → vapor/species → ignition state",COLORS["light"],COLORS["gray"],False)],
    [((220,210),(245,210),False,COLORS["blue"]),((415,210),(440,210),False,COLORS["green"]),((610,210),(635,210),False,COLORS["green"]),((805,210),(830,210),False,COLORS["green"]),((1000,210),(1025,210),False,COLORS["blue"]),((1195,210),(1220,210),False,COLORS["blue"]),((1390,210),(1415,210),True,COLORS["red"])],
    [(100,350,"Clock ordering is condition dependent; no universal tau_loading/tau_response correlation is claimed.",COLORS["gray"])],
    "Author synthesis. Research priorities are expressed as measurable physical quantities, not internal project IDs."),
}

for fid,(title,boxes,arrows,notes,footer) in fig_defs.items():
    build_figure(fid,title,boxes,arrows,notes,footer)


def build_plot(fid: str, title: str, x_label: str, y_label: str, series: list[tuple[str,list[tuple[float,float]],str]], x_log: bool=False, y_log: bool=False, note: str="") -> None:
    svg=[f'<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="800" viewBox="0 0 1200 800">', '<rect width="1200" height="800" fill="white"/>', '<defs><marker id="arrow" markerWidth="10" markerHeight="10" refX="9" refY="5" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#2F6690"/></marker></defs>', f'<text x="70" y="60" font-family="Arial" font-size="34" font-weight="700" fill="{COLORS["ink"]}">{xml_escape(title)}</text>']
    img=Image.new("RGB",(1200,800),"white"); d=ImageDraw.Draw(img); d.text((70,25),title,font=FONT_BOLD,fill=COLORS["ink"])
    left,top,right,bottom=130,110,1100,650
    all_pts=[p for _,pts,_ in series for p in pts]
    tx=lambda v: math.log10(v) if x_log else v
    ty=lambda v: math.log10(v) if y_log else v
    xs=[tx(p[0]) for p in all_pts]; ys=[ty(p[1]) for p in all_pts]
    xmin,xmax=min(xs),max(xs); ymin,ymax=min(ys),max(ys)
    xpad=(xmax-xmin)*0.08 or 1; ypad=(ymax-ymin)*0.12 or 1
    xmin-=xpad; xmax+=xpad; ymin-=ypad; ymax+=ypad
    sx=lambda v:left+(tx(v)-xmin)/(xmax-xmin)*(right-left)
    sy=lambda v:bottom-(ty(v)-ymin)/(ymax-ymin)*(bottom-top)
    svg.append(f'<line x1="{left}" y1="{bottom}" x2="{right}" y2="{bottom}" stroke="{COLORS["ink"]}" stroke-width="3"/><line x1="{left}" y1="{top}" x2="{left}" y2="{bottom}" stroke="{COLORS["ink"]}" stroke-width="3"/>')
    d.line((left,bottom,right,bottom),fill=COLORS["ink"],width=3); d.line((left,top,left,bottom),fill=COLORS["ink"],width=3)
    for k in range(6):
        xx=left+k*(right-left)/5; yy=bottom-k*(bottom-top)/5
        svg.append(f'<line x1="{xx}" y1="{top}" x2="{xx}" y2="{bottom}" stroke="#E3E8EC" stroke-width="1"/><line x1="{left}" y1="{yy}" x2="{right}" y2="{yy}" stroke="#E3E8EC" stroke-width="1"/>')
        d.line((xx,top,xx,bottom),fill="#E3E8EC",width=1); d.line((left,yy,right,yy),fill="#E3E8EC",width=1)
        xv_t=xmin+k*(xmax-xmin)/5; yv_t=ymin+k*(ymax-ymin)/5
        xv=10**xv_t if x_log else xv_t; yv=10**yv_t if y_log else yv_t
        xtext=f"{xv:.3g}"; ytext=f"{yv:.3g}"
        svg.append(f'<text x="{xx:.1f}" y="{bottom+30}" text-anchor="middle" font-family="Arial" font-size="18" fill="{COLORS["gray"]}">{xtext}</text><text x="{left-14}" y="{yy+6:.1f}" text-anchor="end" font-family="Arial" font-size="18" fill="{COLORS["gray"]}">{ytext}</text>')
        xb=d.textbbox((0,0),xtext,font=FONT_SMALL); yb=d.textbbox((0,0),ytext,font=FONT_SMALL)
        d.text((xx-(xb[2]-xb[0])/2,bottom+8),xtext,font=FONT_SMALL,fill=COLORS["gray"])
        d.text((left-18-(yb[2]-yb[0]),yy-12),ytext,font=FONT_SMALL,fill=COLORS["gray"])
    for si,(name,pts,color) in enumerate(series):
        coords=[(sx(x),sy(y)) for x,y in pts]
        if len(coords)>1:
            svg.append('<polyline points="'+' '.join(f'{x:.1f},{y:.1f}' for x,y in coords)+f'" fill="none" stroke="{color}" stroke-width="4"/>')
            d.line(coords,fill=color,width=4)
        for x,y in coords:
            svg.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="8" fill="white" stroke="{color}" stroke-width="4"/>')
            d.ellipse((x-8,y-8,x+8,y+8),fill="white",outline=color,width=4)
        ly=125+si*40
        svg.append(f'<line x1="820" y1="{ly}" x2="870" y2="{ly}" stroke="{color}" stroke-width="4"/><text x="885" y="{ly+7}" font-family="Arial" font-size="21" fill="{COLORS["ink"]}">{xml_escape(name)}</text>')
        d.line((820,ly,870,ly),fill=color,width=4); d.text((885,ly-14),name,font=FONT_SMALL,fill=COLORS["ink"])
    svg.append(f'<text x="{(left+right)/2}" y="715" text-anchor="middle" font-family="Arial" font-size="24" fill="{COLORS["ink"]}">{xml_escape(x_label)}</text><text transform="translate(35 {(top+bottom)/2}) rotate(-90)" text-anchor="middle" font-family="Arial" font-size="24" fill="{COLORS["ink"]}">{xml_escape(y_label)}</text>')
    d.text(((left+right)/2-170,690),x_label,font=FONT_REG,fill=COLORS["ink"]); d.text((20,360),y_label,font=FONT_SMALL,fill=COLORS["ink"])
    if note:
        svg.append(f'<text x="130" y="765" font-family="Arial" font-size="19" fill="{COLORS["red"]}">{xml_escape(note)}</text>')
        d.text((130,742),note,font=FONT_SMALL,fill=COLORS["red"])
    svg.append('</svg>')
    write_text(QDIR/f"{fid}.svg","\n".join(svg)); img.save(QDIR/f"{fid}.png")


build_plot("QSA-01_B009_within_study", "B009 within-study Mach-disk position", "NPR = P0/P∞", "x_MD / D (derived)", [("H2",[(8.5,1.853),(10,2.060),(30,3.767),(70,5.813)],COLORS["blue"]),("CH4",[(8.5,1.900)],COLORS["orange"])], note="Within one study/setup; no cross-paper fit or universal coefficient.")
build_plot("QSA-05_D017_within_study", "D017 within-study extinction distance", "parent d0 (µm; log axis)", "extinction distance (mm; log axis)", [("KH-RT",list(zip(diameters,[0.04,0.12,0.32,0.46,0.98,2.25,2.97])),COLORS["blue"]),("WERT49",list(zip(diameters,[0.075,0.41,0.93,1.29,3.78,8.76,11.96])),COLORS["orange"]),("no breakup (uncensored)",list(zip(diameters[:4],[0.84,13.32,37.05,71.25])),COLORS["green"])],x_log=True,y_log=True,note=">500 mm lower bounds remain in the registry; exact points are not invented.")
build_plot("QSA-08_D009_within_study", "QSA-08 — D009 RDE case-family response", "L_E / L_D (source definition)", "mean rotating-wave velocity (m/s)", [("D009 B2–B4",[(0.13,1728),(0.31,1696),(0.55,1618)],COLORS["blue"])],note="Three paired cases in one RDE model family; analogue only and not mapped to HPDI.")


# Targeted deepening map and integrated draft.
DEEP_FIELDS = ["edit_id", "section_id", "trigger_figure_or_table", "edit_type", "scientific_reason", "proposed_content", "paper_ids", "priority", "apply_now", "notes"]
deep_rows = [
    dict(edit_id="P14-E01", section_id="S06", trigger_figure_or_table="TAB-02;QSA-01", edit_type="add_quantitative_comparison", scientific_reason="Case audit produced a definition-complete within-study x_MD/D series while rejecting cross-paper pooling.", proposed_content="Add B009 NPR and derived x_MD/D values; explicitly state within-study-only status.", paper_ids="B009", priority="high", apply_now="yes", notes="No correlation fit."),
    dict(edit_id="P14-E02", section_id="S18", trigger_figure_or_table="TAB-05;QSA-05", edit_type="add_condition_comparison", scientific_reason="D017 registry quantifies model sensitivity at fixed d0.", proposed_content="Add the 10 µm extinction-distance spread across no-breakup, KH-RT and WERT49 branches.", paper_ids="D017", priority="medium", apply_now="yes", notes="Within-study model comparison."),
    dict(edit_id="P14-E03", section_id="S26", trigger_figure_or_table="TAB-07;QSA-08", edit_type="add_quantitative_comparison", scientific_reason="D009 has three paired L_E/L_D–wave-speed cases and one unpaired ratio case.", proposed_content="Add the 2–4 µm paired range and retain the 5 µm exclusion transparently.", paper_ids="D009", priority="high", apply_now="yes", notes="RDE-only; no HPDI mapping."),
    dict(edit_id="P14-E04", section_id="S08", trigger_figure_or_table="FIG-03;TAB-08", edit_type="no_change", scientific_reason="Current prose already states the exact unresolved Lagrangian variables and diagnostics.", proposed_content="No change.", paper_ids="B009;B021;C007;C016", priority="high", apply_now="no", notes="Boundary preserved."),
    dict(edit_id="P14-E05", section_id="S16", trigger_figure_or_table="FIG-05;TAB-04", edit_type="no_change", scientific_reason="Current prose already separates ordered/cloud mechanisms from dense HPDI spray.", proposed_content="No change.", paper_ids="C033;C034;C035;C036", priority="high", apply_now="no", notes="Dense-spray transfer remains unresolved."),
    dict(edit_id="P14-E06", section_id="S25", trigger_figure_or_table="FIG-07;TAB-06", edit_type="no_change", scientific_reason="No eligible timing-response pooling emerged; existing boundary is scientifically sufficient.", proposed_content="No change.", paper_ids="A007;A020;A022", priority="high", apply_now="no", notes="Wave-to-ignition causality remains open."),
]
write_csv(SUPPORTDIR / "phase14_targeted_deepening_map.csv", DEEP_FIELDS, deep_rows)

source_manuscript = MANUSCRIPTDIR / "phase13R_physics_led_draft.md"
target_manuscript = MANUSCRIPTDIR / "phase14_figtable_informed_draft.md"
manuscript = source_manuscript.read_text(encoding="utf-8")
insertions = [
    ("TAB-02 therefore separates the geometric feature, nozzle-diameter basis, and developing or settled state for every comparison.", "TAB-02 therefore separates the geometric feature, nozzle-diameter basis, and developing or settled state for every comparison. The case-level audit retained one definition-complete numerical sequence for plotting: within the B009 semi-steady hydrogen series, NPR values of 8.5, 10, 30, and 70 correspond to derived `x_MD/D` values of 1.85, 2.06, 3.77, and 5.81, respectively; the methane case at NPR 8.5 gives 1.90 under the same nozzle and ambient state [[CITE:B009]]. This is a within-study trend, not a cross-paper coefficient."),
    ("The variable post-front velocity and pressure history, however, causes different breakup closures to bracket rather than reproduce all observations.", "The variable post-front velocity and pressure history, however, causes different breakup closures to bracket rather than reproduce all observations. At `d0 = 10 µm` in the D017 model family, the reported extinction distance is 37.05 mm without breakup, 0.32 mm with KH–RT breakup, and 0.93 mm with WERT49 breakup [[CITE:D017]]. The order-of-magnitude spread at fixed diameter shows that a diameter trend cannot be separated from the product-generation closure."),
    ("The ratio organizes those cases because its numerator and denominator describe the same refill and wave geometry.", "The ratio organizes those cases because its numerator and denominator describe the same refill and wave geometry. In the paired D009 cases, increasing `L_E/L_D` from 0.13 to 0.55 as `d0` increases from 2 to 4 µm accompanies a decrease in mean rotating-wave velocity from 1728 to 1618 m/s [[CITE:D009]]. The 5 µm case reports `L_E/L_D = 0.84` but lacks a paired wave-velocity value in the current extraction, so it is retained in the registry but excluded from the plot. This remains a within-study RDE relation."),
]
for old, new in insertions:
    if old not in manuscript:
        raise RuntimeError(f"Manuscript anchor missing: {old[:80]}")
    manuscript = manuscript.replace(old, new, 1)
write_text(target_manuscript, manuscript)


def word_count(text: str) -> int:
    return len(re.findall(r"\b[\wµρΔ]+(?:[-–][\wµρΔ]+)*\b", text))

original_words = word_count(source_manuscript.read_text(encoding="utf-8"))
new_words = word_count(manuscript)
net_words = new_words - original_words


# Figure source/readme and Phase 14 report.
write_text(SOURCEDIR / "README.md", """# Figure source handling

This directory intentionally contains provenance records and rights-aware placeholders rather than copied literature panels. Original PDFs remain immutable under `02_PDF_Raw/`. A literature image enters a publication composite only after its exact locator and reuse route are confirmed. Open-license status does not relax attribution, scale-bar, or data-meaning requirements.
""")

statuses = {s: sum(1 for r in audit_rows if r["status"] == s) for s in ("ready_cross_paper", "ready_conditioned", "within_study_only", "qualitative_only", "not_recommended")}
open_panels = sum(1 for r in reuse_rows if r["reuse_action"] == "reuse_open_license")
permission_panels = sum(1 for r in reuse_rows if r["reuse_action"] == "reuse_permission_required")
redraw_panels = sum(1 for r in reuse_rows if r["reuse_action"] == "redraw_from_scientific_facts")
internal_panels = sum(1 for r in reuse_rows if r["reuse_action"] == "internal_preview_only")
table_rows_count = sum(len(rows) for _, rows in tables.values())
unique_papers = sorted(set(re.findall(r"\[\[CITE:([ABCD]\d{3})\]\]", " ".join(" ".join(str(v) for v in row.values()) for _, rows in tables.values() for row in rows))))

report = f"""# Phase 14 Scientific Figure/Table Production Report

Status: **COMPLETE** on 2026-09-02.

## Actual production

```text
Figures:
- Planned: 9
- Scientific specs complete: 9 / 9
- Author-synthesis figures produced: 4 (FIG-01, FIG-03, FIG-06, FIG-09)
- Hybrid figures drafted: 5 (FIG-02, FIG-04, FIG-05, FIG-07, FIG-08)
- Quantitative figures produced: 3, all within-study only
- Figures blocked from publication-ready literature-panel reuse: 5 hybrid layouts

Literature panels:
- Candidate source panels: {len(figure_sources)}
- Open-license reusable now: {open_panels}
- Permission required: {permission_panels}
- Redraw from scientific facts: {redraw_panels}
- Internal-preview-only because of license restrictions: {internal_panels}
- Rejected/fabricated observation panels: 0 created

Tables:
- Populated: 8 / 8
- Main-table rows: {table_rows_count}
- Unique papers represented: {len(unique_papers)}
- Supplementary tables proposed: 0
```

All nine figure drafts exist as editable SVG plus PNG preview. Literature observations whose rights are not cleared remain provenance-labelled placeholders; no experimental, schlieren, PLIF, optical, or simulation data were imitated or altered.

## Quantitative eligibility

```text
12 candidate analyses

ready_cross_paper = {statuses['ready_cross_paper']}
ready_conditioned = {statuses['ready_conditioned']}
within_study_only = {statuses['within_study_only']}
qualitative_only = {statuses['qualitative_only']}
not_recommended = {statuses['not_recommended']}
```

### Candidate decisions

1. **QSA-01 — NPR versus x_MD/D:** `within_study_only`. Five B009 cases pass; B021 endpoint cases are excluded because the extracted x_MD records are not paired with explicit ratio records. A B009-only plot was produced without regression.
2. **QSA-02 — p_inj(t) versus Mach-disk transient:** `qualitative_only`. The history registry is figure-only and `time_series_points.csv` contains zero points.
3. **QSA-03 — Mach/We versus droplet response:** `qualitative_only`. Strict definition-complete We plus a common response metric is absent; TAB-03 and FIG-04 retain condition facets.
4. **QSA-04 — typed loading duration versus response:** `qualitative_only`. Joint start/end and response-time definitions are insufficient; the ratio remains conceptual.
5. **QSA-05 — d0 versus breakup/evaporation response:** `within_study_only`. D017 supplies 21 branch-conditioned records; a model-specific plot was produced, with censored `>500 mm` values retained in the registry.
6. **QSA-06 — S/D or cloud descriptor versus collective response:** `qualitative_only`. Pair spacing and cloud descriptors are not convertible.
7. **QSA-07 — signed ΔSOI versus mixture/ignition:** `qualitative_only`. Timing records exist, but no condition-compatible paired y metric supports plotting.
8. **QSA-08 — L_E/L_D versus RDE behavior:** `within_study_only`. Three paired D009 cases pass; the 5 µm case is excluded from plotting because wave velocity is NV.
9. **QSA-09 — generic NPR pooling:** `not_recommended`.
10. **QSA-10 — generic Mach/We universal breakup map:** `not_recommended`.
11. **QSA-11 — generic breakup-time pooling:** `not_recommended`.
12. **QSA-12 — RDE L_E/L_D to HPDI ignition mapping:** `not_recommended`.

The four Phase 12 moderate candidates therefore resolve as QSA-01 `within_study_only`, QSA-03 `qualitative_only`, QSA-05 `within_study_only`, and QSA-07 `qualitative_only`. No cross-paper quantitative synthesis survived the case-level audit.

## Figure decisions

- **FIG-01:** author synthesis. A variable-led mechanism sequence with four open measurement gates replaces the former evidence-audit emphasis.
- **FIG-02:** hybrid layout. The author timeline supplies the scientific comparison; three literature panels remain rights-aware placeholders.
- **FIG-03:** author synthesis. The actual HPDI Lagrangian load ends at an open measurement gate.
- **FIG-04:** hybrid layout. C016 is reusable under CC BY 4.0; C025 and D018 remain placeholders; the mechanism cascade is original.
- **FIG-05:** hybrid layout. Tandem/parallel observations are separated from the unvalidated dense-spray target.
- **FIG-06:** author-synthesis dominant hybrid. Promotion and suppression branches are separate, and the mixture contribution remains open.
- **FIG-07:** hybrid layout. Signed chronology and geometry are direct; the wave-mediated ignition path is not closed.
- **FIG-08:** hybrid layout. Shared local variables and device-specific scales are separated.
- **FIG-09:** author synthesis. Competing clocks and transported variables drive the research priorities.

## Rights blockers

- B009, C025, C035, C036, C024, D018, D019, and A007 observation panels require permission or a confirmed publisher route.
- B021 license status is unknown in frozen project files.
- B029 is CC BY-NC-ND 4.0 and remains internal-preview-only pending venue review.
- A026 is CC BY-NC and remains internal-preview-only pending venue review.
- A022 is CC BY 4.0, but its geometry is redrawn from scientific facts to keep a unified visual language.

Action: retain source-labelled placeholders in the hybrid drafts; use the author synthesis as the working scientific figure until rights are resolved.

## Targeted manuscript deepening

```text
Sections reviewed after figure/table synthesis = 31
Sections scientifically deepened = 3 (S06, S18, S26)
Sections shortened due to figure/table replacement = 0
Net manuscript word change = {net_words}

No global prose rewrite performed = confirmed
```

The added material is limited to the B009 within-study NPR–x_MD/D sequence, D017 fixed-diameter model spread, and D009 within-study L_E/L_D–wave-speed sequence. All additions are source-backed and explicitly bounded.

## Scientific boundary check

```text
actual HPDI pilot Lagrangian load = unresolved
canonical droplet to dense reacting pilot spray = unresolved
fragment population to HPDI pre-ignition mixture = unresolved
wave-induced mixture change to ignition = unresolved
RDE/detonation = strong-wave comparison domain only
tau_loading/tau_response = hypothesis only
```

No new literature, Paper IDs, claims, pathways, or mechanism architecture were introduced. `02_PDF_Raw/`, extraction schemas, paper notes, evidence cards, global claims, claim-evidence matrix, and Phase 13R manuscript remain unchanged.

## Minimal QC

- FIG-01–FIG-09 scientific messages and specs: PASS.
- TAB-01–TAB-08 populated: PASS.
- Literature panels trace to Paper ID, PDF, page, original figure, and source locator: PASS.
- Rights status assigned or explicitly unknown: PASS.
- Quantitative plots have eligibility status and case registry: PASS.
- Plotted points trace to Paper ID, case, source locator, and reported/derived status: PASS.
- Forbidden generic pooling: absent.
- Four causal boundaries: open.
- New scientific literature: none.

## Phase 15 readiness

**READY**, with literature-panel permissions and final venue-specific reuse decisions carried forward as known blockers rather than Phase 14 completion blockers.
"""
write_text(QCDIR / "phase14_figure_table_report.md", report)


def append_once(path: Path, marker: str, block: str) -> None:
    text = path.read_text(encoding="utf-8")
    if marker not in text:
        write_text(path, text.rstrip() + "\n\n" + block.rstrip())


append_once(ROOT / "00_Project" / "workflow.md", "Phase 14 — Scientific Figure/Table Production (completed)", """## Phase 14 — Scientific Figure/Table Production (completed)

Completed 2026-09-02. Nine figure specifications, nine SVG/PNG working drafts, eight populated reader tables, a rights-aware source/reuse inventory, twelve case-level quantitative eligibility decisions, three within-study plots, and a targeted Phase 14 manuscript draft were produced. No new literature was introduced. Phase 15 readiness is recorded in `11_QC/phase14_figure_table_report.md`.
""")
append_once(ROOT / "00_Project" / "changelog.md", "Phase 14 completed (2026-09-02)", """## Phase 14 completed (2026-09-02)

- Created `08_Figures_Tables/phase14/` scientific figure/table production assets.
- Completed exact provenance and reuse/redraw classification for candidate literature panels.
- Audited all twelve quantitative candidates; produced only three within-study plots.
- Populated TAB-01–TAB-08 and created the table source map.
- Created `09_Manuscript/phase14_figtable_informed_draft.md` with three local, source-backed additions; Phase 13R was not overwritten.
- Recorded Phase 15 readiness and outstanding rights blockers in the Phase 14 QC report.
""")

print(f"Generated Phase 14 assets under {P14}")
print(f"Tables: {len(tables)}; main rows: {table_rows_count}; unique papers: {len(unique_papers)}")
print(f"Net manuscript word change: {net_words}")
