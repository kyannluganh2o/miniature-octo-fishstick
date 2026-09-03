# Phase 14R Source-Image / Figure-Table Harmonization Report

Status: **COMPLETE** on 2026-09-02.

## Scope and operating boundaries

Phase 14R integrated source images, reconstructed reader-facing figures and tables, and harmonized the Phase 14 manuscript locally. It did not perform a new literature search, create Paper IDs, expand the library, redefine the mechanism architecture, or initiate Phase 15. Targeted PDF inspection was limited to questions raised by specific figures, tables, and manuscript passages. No write operation targeted `02_PDF_Raw/`.

## Actual production

```text
Final working figure count = 9
Existing figures retained and simplified = 3
Figures substantially reconstructed = 6
New figures added = 0
Figures removed / merged = 0

Direct literature panels used = 21
Unique Paper IDs represented visually = 19
Source panels with complete registry fields = 21 / 21
Source panels linked to an existing local PDF = 21 / 21
Source-panel image files present = 21 / 21

Author-synthesis figures = 3
Hybrid figures = 4
Source-image-dominant figures = 2
Quantitative figures = 0

Editable SVG figures = 9 / 9
PNG figure previews = 9 / 9
Unreadable or zero-dimension PNG files = 0

Reader-facing tables = 8 / 8
Table data rows = 55
Unique Paper IDs represented in tables = 31
Workbook audit sheets = 8 / 8
```

The Phase 14 actions resolve as three `retain and simplify`, three `replace`, and three `major redesign` decisions.

## Figure results

### FIG-01

- **Type:** author synthesis.
- **Scientific message:** compact injector-to-ignition physical sequence with four open couplings.
- **Source panels:** none; citations supply the synthesis basis.
- **Main change from Phase 14:** retained and simplified; workflow and evidence-gap framing removed.

### FIG-02

- **Type:** hybrid.
- **Scientific message:** injector opening and pressure build-up precede choking, shock-cell formation, Mach-disk motion, overshoot, and semi-steady behavior on a qualitative event line.
- **Source panels:** B009, B021, B029; 3 panels.
- **Main change from Phase 14:** placeholder layout replaced by direct transient-jet observations and a compact event timeline.

### FIG-03

- **Type:** author synthesis.
- **Scientific message:** visible Eulerian topology is not the Lagrangian pressure and relative-velocity history sampled by a moving pilot droplet.
- **Source panels:** none.
- **Main change from Phase 14:** retained and simplified; vector notation and loading magnitude normalized.

### FIG-04

- **Type:** source-image dominant.
- **Scientific message:** source observations distinguish early deformation, sheet/rim/ligament development, piercing, stripping, and fragment production without imposing a universal regime boundary.
- **Source panels:** C012, C013, C016, D018; 4 panels.
- **Main change from Phase 14:** mechanism-flow layout replaced by a literature-observation montage with compact mechanism annotations.

### FIG-05

- **Type:** hybrid.
- **Scientific message:** isolated, tandem, parallel, and cloud configurations introduce different collective mechanisms and do not form a temporal progression.
- **Source panels:** C035, C036, C033; 3 panels.
- **Main change from Phase 14:** major redesign as a configuration comparison; the dense reacting HPDI-spray connection remains open.

### FIG-06

- **Type:** hybrid.
- **Scientific message:** vapor-layer or blowing effects can suppress interfacial shear, whereas heating-induced surface-tension reduction can promote deformation; downstream transport and vapor redistribution remain conditional.
- **Source panels:** C024, C026, C031, C032; 4 panels.
- **Main change from Phase 14:** major redesign with direct observations and two explicitly separate phase-change branches.

### FIG-07

- **Type:** hybrid.
- **Scientific message:** relative injection chronology requires signed `Delta SOI`, named events, fuel order, and geometry; the direct timing/geometry pathway is distinct from the hypothesized wave-mediated fragment pathway.
- **Source panels:** A022, A026, A007; 3 panels.
- **Main change from Phase 14:** major redesign; the fixed pilot-to-gas sequence was removed.

### FIG-08

- **Type:** source-image dominant.
- **Scientific message:** strong-wave studies share local pressure, density, slip, size, fragment-state, and residence variables with HPDI, while their thermochemistry and device scales remain domain-specific.
- **Source panels:** D018, D019, D014; 4 panels.
- **Main change from Phase 14:** full-flow schematic replaced by a source-observation comparison and a compact transfer-boundary block.

### FIG-09

- **Type:** author synthesis.
- **Scientific message:** competing injection, wave, liquid-response, evaporation, mixing, and ignition clocks organize the unresolved measurements.
- **Source panels:** none.
- **Main change from Phase 14:** retained and simplified; separated from FIG-01 by focusing on clocks and transported quantities rather than the article-level sequence.

## Table results

### TAB-01

Nine compact parameter-definition rows separate physical role, required definition, common ambiguity, and comparison rule.

### TAB-02

Four representative underexpanded-jet studies compare gas/nozzle state, pressure definition, NPR, transient stage, and Mach-disk or topology metrics without library-inventory or plotting language.

### TAB-03

Nine compressible-droplet cases retain loading, Mach, dimensionless groups, size, duration, response, and boundary. Targeted verification of C014 confirmed that the relevant initial diameter is not reported, so the cell is `NR`. SIE, RTP, and NR are defined in the table caption.

### TAB-04

Five rows compare isolated, tandem, parallel, and cloud configurations using spacing/population descriptors, collective loading mechanisms, response, and the dense-spray implication.

### TAB-05

Six source rows reconstruct the phase-change competition around C024, C026, C027, C031, C032, and D017. Vapor-layer shear reduction, heating-driven liquid-property change, early large-droplet behavior, and fragmentation-evaporation overlap are represented separately.

### TAB-06

Ten representative A-library studies cover relative timing, geometry, mixture preparation, ignition, heat-release response, injection pressure, pilot energy, and hydrogen-specific behavior without becoming a full library inventory.

### TAB-07

Six strong-wave studies include D014 wave-relative position and thermal-history information alongside breakup, evaporation, residence, and transfer boundaries.

### TAB-08

Six coupling problems are expressed as technical noun phrases with established physics, missing quantity, diagnostics, model requirement, and scientific significance.

```text
TAB-05 phase-change competition represented = yes
TAB-06 HPDI mechanism coverage improved = yes
TAB-08 question-form wording removed = yes
Question-form table cells = 0
Reader-facing project-language cells = 0
```

## Manuscript harmonization

The Phase 14R manuscript was generated from `phase14_figtable_informed_draft.md` through explicit paragraph and notation replacements rather than chapter regeneration.

```text
Scientific subsections modified = 8
Phase 14 word count = 11,694
Phase 14R word count = 11,653
Net word change = -41
Global rewrite = no
Reader-facing C004 occurrences = 0
```

The eight locally affected subsections cover the B009 Mach-disk trend, Lagrangian loading notation, breakup-model limits, configuration comparison, relative injection chronology, D009/D017 strong-wave interpretation, strong-wave transfer limits, and final measurement requirements. The B009, D009, and D017 numerical statements remain within-study or model-branch comparisons.

Required manuscript term counts:

```text
case-level audit = 0
current extraction = 0
registry = 0
excluded from plot = 0
QSA- = 0
frozen corpus = 0
C004 = 0
permission pending = 0
```

## Notation normalization

The notation map defines pressure history, transient NPR, Mach-disk position, droplet position and velocities, gas density, shock and relative Mach numbers, We/Re/Oh, loading and response times, the strong-wave length ratio, and signed injection timing. Vector position and velocity are distinguished from scalar magnitudes. Dynamic loading uses `rho_g |u_rel|^2`, while reader-facing mathematical text uses bold vector notation. A byte-level check found no embedded control-character corruption after regeneration.

```text
Manuscript / figure / table / caption notation synchronized = PASS
Extra carriage-return control bytes in Phase 14R manuscript = 0
```

## Traceability and reader-facing QC

- Every direct panel records Paper ID, canonical local PDF path, PDF page, original figure, original panel or combined sequence, physical phenomenon, condition summary, manuscript section, new figure ID, crop note, and source locator.
- Scientific content in direct panels was cropped and proportionally resized only; panel labels and Paper-ID provenance are external to the source image.
- Figures carry compact Paper-ID/original-figure provenance; captions carry citation markers.
- Twenty-one reader-facing text files were scanned across SVG figures, CSV tables, captions, manuscript, and notation map.
- Forbidden production, rights, eligibility, and internal-audit terms found: 0.
- Question marks in reader-facing tables: 0.
- Reader-facing `C004` occurrences: 0.
- All 21 source-panel PNGs and 9 preview PNGs opened with valid positive dimensions.
- All eight workbook sheets were rendered and visually inspected; formula-error scan: 0.
- The generated page-render cache was removed from the deliverable directory; reproducible PDF scratch remains outside the Phase 14R output tree.

## Scientific boundary check

```text
Actual HPDI pilot-droplet Lagrangian loading = unresolved
Canonical single/ordered-droplet physics to dense reacting HPDI pilot spray = unresolved
Shock-generated fragments to measured HPDI pre-ignition mixture redistribution = unresolved
Wave-induced mixture change to ignition / combustion response = unresolved
RDE / detonation = strong-wave comparison domain only
tau_load / tau_response = organizing hypothesis only
```

No figure, table, caption, or manuscript edit closes these relationships visually or verbally.

## Highest-priority human review

1. Verify every composite crop against the cited PDF page and original figure at full resolution, especially multi-figure or sequence crops.
2. Review the working captions for venue-specific wording and confirm that each panel-level description remains no stronger than the source observation.
3. Check final figure typography, panel balance, and legibility at the intended journal column width.
4. Resolve publisher reuse and permission requirements before submission; these administrative notes are intentionally absent from reader-facing figures.
5. Complete final citation rendering and bibliography reconciliation in Phase 15 without changing frozen scientific boundaries.

## Phase 15 readiness

**READY.** Phase 14R completion criteria are met. Venue-specific image permissions, final citation rendering, and journal formatting remain expected Phase 15 or pre-submission tasks rather than Phase 14R blockers.

