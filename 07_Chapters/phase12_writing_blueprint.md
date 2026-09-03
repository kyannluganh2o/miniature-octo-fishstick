# Phase 12 Writing Blueprint

## 1. Article Scientific Thesis

Internal working thesis:

> The reviewed literature strongly resolves transient underexpanded-wave formation, definition-complete canonical compressible droplet response, collective mechanisms in bounded configurations, and injection-timing-controlled HPDI ignition as component problems. It does not yet directly close the full underexpanded-shock → pilot-droplet loading → dense-spray breakup/evaporation → mixture redistribution → ignition/combustion chain under a common HPDI condition. The review's scientific contribution is therefore an evidence-weighted framework that unifies the resolved local physics, identifies the four transfer discontinuities, and specifies the parameter definitions and synchronized evidence needed to close them.

This is an internal synthesis thesis, not final Abstract text.

## 2. Article Narrative Logic

The article follows physical causality while refusing to imply equal evidence for every arrow:

```text
injection boundary and chronology
→ transient underexpanded-wave formation
→ shock topology and local gas state
→ droplet loading magnitude and duration
→ deformation and instability
→ secondary breakup
→ collective and fragment-population effects
→ transport and conditional phase change
→ mixture redistribution
→ ignition and combustion
```

The main narrative pauses at four explicit discontinuities:

- MP-033: shock topology → actual HPDI pilot-droplet loading;
- MP-032: canonical single/ordered droplets → dense polydisperse reacting HPDI spray;
- MP-028: shock-mediated breakup/evaporation → measured HPDI mixture field; and
- MP-029: shock-caused mixture change → measurable HPDI ignition/combustion response.

Detonation and RDE evidence enters after the direct HPDI application chain, as a bounded strong-wave analogue rather than a substitute evidence base.

## 3. Chapter Architecture

The fixed architecture contains nine chapters and 31 stable sections:

1. Introduction and Review Scope
2. High-Pressure Injection and Transient Underexpanded-Wave Formation
3. From Shock Topology to Local Multiphase Loading
4. Compressible Droplet Deformation, Instability, and Secondary Breakup
5. Collective Droplet Effects and Canonical-to-Spray Transfer
6. Fragment Populations, Phase Change, and the Mixture-Formation Bridge
7. HPDI Mixture Formation, Ignition, and Combustion Coupling
8. Strong-Wave Analogues: Detonation and Rotating Detonation Engines
9. Integrated Mechanistic Framework, Evidence Gaps, and Research Priorities

The complete chapter-level contract is in `chapter_architecture.csv`; the stable manuscript structure is in `00_Project/chapter_structure.md`.

## 4. Section-by-Section Argument Flow

Each Section Blueprint records its scientific question, opening problem, mechanism logic, boundaries, evidence anchors, intended takeaway, and transition. The central argument sequence is:

- S04–S06 establish definition-complete, time-dependent injection and shock states.
- S07–S09 convert topology into local loading variables and expose MP-033.
- S10–S13 build the multivariable canonical droplet-response argument.
- S14–S16 introduce collective corrections and expose MP-032.
- S17–S20 define fragment and phase-change states and expose MP-028.
- S21–S25 separate directly supported timing/mixture/ignition physics from MP-029.
- S26–S28 define the value and boundary of the detonation/RDE analogue.
- S29–S31 reassemble the chain by evidence status and derive research priorities.

No section carries more than four primary Global Claims. Framing, transfer-audit, and synthesis sections may have no primary GC when they are explicitly anchored by frozen SP/MP/KG relations.

## 5. Synthesis Proposition Deployment

- SP-001 anchors CH02 and the time-resolved injection boundary.
- SP-002 anchors CH03 and the MP-033 discontinuity.
- SP-003 anchors loading, comparison discipline, and CH04.
- SP-004 anchors CH05 and the MP-032 transfer boundary.
- SP-005 anchors the conditional breakup–phase-change argument in CH06.
- SP-006 anchors the separation between direct HPDI chronology evidence and MP-028/MP-029.
- SP-007 anchors the bounded detonation/RDE analogue in CH08.
- SP-008 anchors fragment-population state from CH04 through CH06.

All eight frozen SP IDs are deployed without renumbering or scientific rewriting.

## 6. Global Claim Deployment

All 53 Global Claims receive one primary section in `claim_section_map.csv`. Later reuse is limited to conceptual cross-reference unless a claim is needed as boundary or corroborating evidence. GC-0052 is fully discussed in S08; GC-0053 is fully discussed in S20 and then cross-referenced in S25 and CH09.

Paper-conditioned claims GC-0038–GC-0051 are kept localized. Secondary-only claims provide field framing or evidence-coverage context and do not replace primary sources.

## 7. Evidence Deployment Strategy

For each Global Claim, `evidence_deployment_map.csv` specifies:

- strongest primary anchors;
- selected supporting or boundary papers;
- contrasting/qualifying evidence;
- review-secondary context; and
- condition-compatibility requirements.

Default citation pattern: one to three strongest primary anchors plus only the boundary or corroborating papers that materially change interpretation. Avoid sentence-level citation dumps. Reviews support terminology, history, and field framing; they do not replace available primary evidence.

Evidence strength and application directness must both be stated. Strong canonical evidence can still have low directness for HPDI transfer.

## 8. Figure Architecture

Nine stable core figure IDs are planned:

- FIG-01 — evidence-weighted unified framework;
- FIG-02 — transient injection and underexpanded-wave evolution;
- FIG-03 — gas-wave state to droplet-loading bridge, including MP-033;
- FIG-04 — multivariable compressible droplet-response framework;
- FIG-05 — isolated-to-dense-spray collective corrections, including MP-032;
- FIG-06 — fragment transport and conditional phase change, including MP-028;
- FIG-07 — direct HPDI chronology-to-ignition chain plus MP-029;
- FIG-08 — detonation/RDE analogue and transfer boundary; and
- FIG-09 — closed-versus-unclosed evidence and research-priority map.

Every mechanism figure must distinguish directly supported, mixed/indirect, cross-scale inference, and evidence-gap arrows. Phase 12 specifies messages and encodings only; it does not draw figures.

## 9. Table Architecture

Eight stable core table IDs are planned:

- TAB-01 — parameter definitions and comparability;
- TAB-02 — underexpanded-jet/shock comparison domains;
- TAB-03 — compressible droplet-response conditions and regimes;
- TAB-04 — collective effects and transfer limits;
- TAB-05 — fragment/phase-change coupling boundaries;
- TAB-06 — HPDI timing, mixture, ignition, and combustion evidence;
- TAB-07 — RDE/detonation-to-HPDI transfer matrix; and
- TAB-08 — knowledge gaps and required evidence.

These are comparison, definition, boundary, and transfer tables—not full-corpus paper inventories.

## 10. Quantitative Synthesis Opportunities

Twelve candidates are recorded. None is designated high feasibility before a case-level definition audit.

- Moderate: contextual NPR versus x_MD/D; Mach/definition-complete We versus response; d0 versus conditioned breakup/evaporation response; signed ΔSOI versus conditioned mixture/ignition response.
- Low: p_inj(t) versus transient Mach-disk history; typed loading duration versus response; spacing/cloud descriptors versus collective response; typed L_E/L_D versus RDE behavior.
- Not recommended: generic NPR pooling; generic Mach/We regime pooling; generic breakup-time pooling; cross-domain L_E/L_D-to-HPDI mapping.

Where compatible data are insufficient, use a condition-domain table, categorical mechanism map, evidence heatmap, or conceptual regime map. Do not lower definition standards to obtain plot density. `tau_loading / tau_response` remains a project hypothesis only.

## 11. Knowledge-Gap Deployment

KGs appear where the relevant mechanism first arises and return in S30:

- KG-001 begins in S07 and is centered in S08.
- KG-002 begins in S10 and is centered in S16.
- KG-003 begins in S18 and is centered across S20/S25.
- KG-004 begins in S04.
- KG-005 begins in S09.
- KG-006 begins in S15 and is centered in S17.
- KG-007 begins in S18 and is centered in S19.
- KG-008 begins in S26 and is centered in S28.
- KG-009 begins in S20 and continues through CH07.
- KG-010 begins in S12 as the C004 source limitation.

## 12. Cross-Scale Transfer Narrative

The transfer narrative uses a hierarchy:

1. Within-domain direct evidence establishes gas-jet, canonical droplet, collective, HPDI chronology, and RDE component relations.
2. Shared local variables provide physically plausible qualitative bridges.
3. Population, thermochemical, geometry, and chronology differences limit quantitative transfer.
4. Direct application claims stop at MP-033, MP-032, MP-028, and MP-029 unless future synchronized evidence closes them.

Cross-scale language must use terms such as “physically plausible,” “bounded analogue,” “component-supported,” or “not validated,” matching the frozen Phase 11 classifications.

## 13. Required Writing Cautions

The 12-item `writing_caution_map.csv` controls Phase 13. The dominant cautions are:

- do not write “shock improves HPDI ignition” as a reported or established result;
- do not compare NPR without pressure roles, types, locations, and time bases;
- do not treat We or Mach as context-free variables;
- do not transfer isolated-droplet regimes directly to dense HPDI spray;
- do not state one universal direction for breakup–phase-change coupling;
- do not use RDE/detonation as proof of HPDI behavior;
- do not generalize paper-conditioned timing or heat-release claims; and
- retain the explicit C004 / C-F-04 source limitation.

## 14. Expected Article Contributions

1. Unify transient underexpanded-jet, compressible droplet, collective spray, phase-change, and HPDI ignition literature in one mechanism progression.
2. Establish definition discipline for NPR, Mach, We/Re/Oh, loading duration, breakup time, ΔSOI, and characteristic-scale comparisons.
3. Separate domain-bounded direct evidence from mixed evidence, cross-scale inference, and application-level evidence gaps.
4. Identify and structurally deploy the four central unclosed pathways MP-033, MP-032, MP-028, and MP-029.
5. Treat fragment population and collective effects as required mediators between canonical breakup and engine-relevant mixture formation.
6. Convert frozen evidence gaps into section-specific diagnostic, modelling, and reporting priorities.

## 15. Phase 13 Writing Order

Recommended evidence-driven drafting order:

1. CH02 — injection and underexpanded-wave formation;
2. CH03 — topology-to-loading bridge;
3. CH04 — canonical droplet deformation and breakup;
4. CH05 — collective effects and transfer;
5. CH06 — fragment state and phase change;
6. CH07 — HPDI mixture, ignition, and combustion;
7. CH08 — bounded strong-wave analogue;
8. CH09 — integrated framework, gaps, and conclusions;
9. CH01 — Introduction and scope;
10. Abstract, only after the complete manuscript is internally consistent.

Phase 13 must use the Section Blueprints and evidence-deployment records rather than reopen a free-form 114-paper summary process.
