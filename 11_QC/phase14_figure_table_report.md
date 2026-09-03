# Phase 14 Scientific Figure/Table Production Report

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
- Candidate source panels: 14
- Open-license reusable now: 1
- Permission required: 10
- Redraw from scientific facts: 1
- Internal-preview-only because of license restrictions: 2
- Rejected/fabricated observation panels: 0 created

Tables:
- Populated: 8 / 8
- Main-table rows: 49
- Unique papers represented: 21
- Supplementary tables proposed: 0
```

All nine figure drafts exist as editable SVG plus PNG preview. Literature observations whose rights are not cleared remain provenance-labelled placeholders; no experimental, schlieren, PLIF, optical, or simulation data were imitated or altered.

## Quantitative eligibility

```text
12 candidate analyses

ready_cross_paper = 0
ready_conditioned = 0
within_study_only = 3
qualitative_only = 5
not_recommended = 4
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
Net manuscript word change = 196

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
