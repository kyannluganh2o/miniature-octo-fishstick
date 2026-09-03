# Changelog

## 2026-08-30 — Frozen literature registration and PDF inventory

- Registered the 115-paper frozen literature library: A=30, B=30, C=36, D=19.
- Assigned and locked Paper IDs A001–A030, B001–B030, C001–C036, and D001–D019.
- Created the complete `source_record_id` to canonical Paper ID mapping.
- Created the read-only PDF inventory and recorded missing-PDF status.
- Confirmed 95 downloaded PDFs and 20 missing PDFs against the frozen expectation.
- No PDF was modified, renamed, moved, or copied.

## 2026-08-30 — Reading-tier and parameter-schema initialization

- Locked reading tiers for all 115 canonical papers: Tier 1 = 31, Tier 2 = 46, Tier 3 = 38.
- Corrected the approved upstream Tier input typo `C-SD-14` to the existing record `C-SD-13`.
- Upgraded the literature-library schema from 1.0 to 1.1 by adding `reading_tier`; no existing field, scientific record, Paper ID, or mapping changed.
- Created the reading-tier manifest and scientific reading protocol; PDF availability remains independent of tier.
- Initialized cross-scale Parameter schema 1.0 with status `Pilot-ready`, SI normalization rules, provenance requirements, and a header-only long-format master table.
- No paper parameter values were extracted; no paper notes or evidence records were created.

## 2026-08-30 — Phase 6 Pilot Scientific Reading

Phase 6 Pilot Scientific Reading completed.

Pilot papers = 12.

Batches:
P1 = B011, C014, C016, D003
P2 = B013, B029, C031, D017
P3 = A020, A022, A016, D009

Pilot generated:
machine-readable full text
structured paper notes
per-paper parameter extraction
candidate evidence cards
schema-gap log
Pilot validation report

Extraction status: complete = 6; partial = 6; failed = 0.
Critical schema gaps proposed = 5. Tier 1 bulk processing is not ready until those gaps are reviewed.

No bulk corpus processing started.

## 2026-08-30 — Phase 6.1 Parameter Schema 1.1 upgrade

- Archived the complete pre-migration Schema 1.0/Pilot extraction state under `99_Archive/old_versions/Phase6_1_pre_schema_1_1/`.
- Upgraded the parameter schema from 1.0 to 1.1 and resolved all 17 logged schema gaps: critical = 5, high = 9, medium = 2, low = 1.
- Preserved all 286 Phase 6 parameter observations and added 73 atomic or explicit missing-component records, producing 359 parameter records.
- Migrated exactly 12 Pilot per-paper JSON files and created normalized tables for provenance locators, ratio definitions, dimensionless-number definitions, events, intervals, time-history registration, process relations, and Pilot mechanism relations.
- Re-validated all 12 Pilot records; no migration failure, duplicate parameter identifier, orphan foreign key, lost observation, or blocking schema gap remained.
- Source-limited unknowns remain explicitly represented as `NV`/`NR`; no numeric value was inferred or derived during migration.
- Raw PDFs, Paper IDs, reading tiers, library identity tables, original Pilot notes, original Pilot evidence cards, and global evidence matrices were not modified.
- Schema 1.1 passed the Pilot readiness gate. Phase 7 was not started.

## 2026-08-31 — Phase 7

Phase 7 Tier 1 Bulk Scientific Processing completed.

```text
Tier 1:
total = 31
Pilot processed previously = 12
Bulk processed in Phase 7 = 14
Blocked missing PDF = 5

Parameter Schema:
1.1 unchanged

No semantic Schema migration performed.
No Paper ID changed.
No reading tier changed.
No raw PDF modified.
No global evidence synthesis started.
```

QC: all 26 available Tier 1 PDFs are processed; foreign-key integrity PASS; blocking schema gaps = 0; one non-blocking candidate recorded; A030 noncanonical master title flagged for later bibliographic maintenance. Master-table growth: parameters +353, locators +93, ratios +35, dimensionless definitions +20, events +28, intervals +4, histories +13, explicit points +0, process relations +38.

## 2026-08-31 — Phase 7.1 Tier 1 housekeeping

Phase 7.1 Tier 1 housekeeping completed.

- A030 canonical bibliographic title corrected from the verified local PDF first-page publisher front matter.
- B028 `projected_spray_area` retained as a deferred non-blocking schema candidate.
- Five missing Tier 1 records audited; all remain missing and status-consistent, with no late PDF detected.
- An incomplete A030 author list was recorded as an additional non-blocking bibliographic issue and was not modified in this phase.
- Paper IDs unchanged.
- Reading tiers unchanged.
- Parameter Schema 1.1 unchanged.
- Scientific extraction unchanged.
- No Tier 2 processing started.

## 2026-08-31 — Phase 8 Tier 2 chapter-core scientific processing

Phase 8 Tier 2 Chapter-Core Scientific Processing completed.

```text
Tier 2:
total = 46
available local PDFs = 39
processed in Phase 8 = 39
blocked_missing_pdf = 7

Parameter Schema:
1.1 unchanged

Tier 2 evidence cards created = 39
Tier 2 -> Tier 1 candidate links created = 39

No Tier 3 processing started.
No global evidence synthesis started.
No Paper ID changed.
No reading tier changed.
No raw PDF modified.
```

## 2026-08-31 — Phase 9 Tier 3 Claim-Targeted Supporting Evidence Processing

Phase 9 Tier 3 Claim-Targeted Supporting Evidence Processing completed.

Tier 3: total = 38; available local PDFs = 30; claim-targeted processed = 30; blocked_missing_pdf = 8.

Tier 3 supporting evidence cards = 30; Tier 3 → core candidate links = 26; retained evidence candidates = 26.

Parameter Schema 1.1 unchanged. No Tier 1/2 scientific data modified. No global evidence consolidation started. No Paper ID changed. No reading tier changed. No raw PDF modified.

## 2026-09-01 — Phase 9.1 — Late-PDF Backfill

- Reconciled the PDF inventory: 19 recovered PDFs matched/readable; C004 remains the only missing PDF.
- Processed recovered papers in frozen-tier order: Tier 1 (4), Tier 2 (7), Tier 3 (8).
- Added only per-paper machine-readable artifacts, notes, structured extraction, tier-local candidate evidence, cross-tier candidate links, QC/status updates, and completion-report addenda.
- Confirmed Schema 1.1 remains stable; global evidence matrices, chapters, synthesis, and manuscript files were unchanged.
- Phase 10 remains not started.

## 2026-09-01 — Phase 10 — Global Evidence Consolidation

- Inventoried all 239 Pilot/Tier 1/Tier 2/Tier 3 candidate claims while preserving original candidate IDs and evidence-card history.
- Retained 181 evidence-worthy candidates for active consolidation and kept 58 method, background, extraction-fragment, schema-observation, low-incremental-value, or historically non-retained candidates as inventory-only records.
- Created 53 conservative Global Claims and 189 long-format Claim-Evidence links representing 106 papers.
- Consolidated 182 mechanism edges: 76 directly supported, 102 indirectly supported, 1 cross-scale inference, and 3 explicit non-retained evidence-gap edges.
- Adjudicated 10 apparent-conflict candidates: true unresolved = 0; condition-related = 4; definition-related = 2; different physical stage = 2; scale-dependent = 1; complementary = 1.
- Completed the 11-segment evidence coverage map and mapped 10 evidence-derived knowledge gaps (high = 5; medium = 4; low = 1).
- Preserved C004 / C-F-04 as the sole missing PDF and added explicit coverage limitations where its absent Tier 1 review evidence matters.
- Minimal integrity checks passed with zero missing source locators in active evidence, zero orphan evidence links, and zero retained source-free mechanism edges.
- Paper IDs, reading tiers, Parameter Schema 1.1, raw PDFs, existing notes/extractions/evidence cards, chapters, and manuscript files were unchanged.
- Phase 11 readiness = READY. Phase 11 was not started.

## 2026-09-01 — Phase 11 — Cross-Paper Mechanistic Synthesis

- Consolidated the frozen Phase 10 evidence into 22 stable high-level mechanism nodes and 34 evidence-weighted mechanism pathways.
- Classified pathways as 17 direct, 12 indirect/mixed, 2 cross-scale inference, and 3 explicit evidence gaps.
- Assessed 9 cross-scale transfer relations: directly validated = 0; partially validated = 2; physically plausible/analogue-only = 4; not validated = 3.
- Created 26 parameter-to-mechanism bridges, 27 boundary-condition records, an M01–M11 mainline synthesis map, and a 29-entry parameter-priority table.
- Retained 8 higher-order Synthesis Propositions: well-supported = 2; supported with boundaries = 3; cross-scale supported = 1; plausible but indirect = 2.
- Recorded one candidate synthesis metric (`tau_loading / tau_response`) as a project hypothesis only; Parameter Master and Schema 1.1 were unchanged.
- Integrated all existing KG-001 through KG-010 without renumbering or creating a duplicate gap system.
- Preserved M03, M08, and M11 as limited/indirect at their application boundaries; no cross-scale inference was promoted to direct HPDI evidence.
- Minimal integrity passed with zero unsupported active propositions, zero unsupported retained pathways, and zero orphan MN/MP/SP/GC/KG references.
- Existing Global Claims, Phase 10 evidence matrices, raw PDFs, paper notes, per-paper JSON, evidence cards, chapter structure, chapters, figures, and manuscript files were not modified.
- C004 remains the sole missing PDF.
- Phase 12 readiness = READY; Phase 12 was not started.

## 2026-09-01 — Phase 12 — Chapter Architecture + Figure/Table Planning + Writing Blueprint

- Fixed a nine-chapter, 31-section mechanism-oriented review architecture in `00_Project/chapter_structure.md`.
- Assigned all 53 frozen Global Claims to one primary section and deployed all 8 Synthesis Propositions, 34 Mechanism Pathways, and 10 Knowledge Gaps.
- Created section-level argument, evidence-deployment, repetition-control, gap-deployment, writing-caution, and long-format article-traceability plans under `07_Chapters/`.
- Planned 9 stable core figures and 8 stable core tables under the configured `08_Figures_Tables/` directory; no figure or final table was produced.
- Evaluated 12 quantitative-synthesis candidates: moderate = 4, low = 4, not recommended = 4, high = 0. Definition matching was retained as a hard gate.
- Explicitly deployed MP-033, MP-032, MP-028, and MP-029 as unclosed pathways rather than narrative conclusions.
- Preserved C004 / C-F-04 as the sole missing source and retained its taxonomy-coverage limitation.
- Existing SP/GC/MP/KG IDs, Phase 10/11 evidence and synthesis, Parameter Schema 1.1, raw PDFs, paper notes, per-paper extraction, evidence cards, and `09_Manuscript/` were unchanged.
- Phase 13 Evidence-Grounded Chapter Drafting readiness = READY; Phase 13 was not started.

## 2026-09-02 — Phase 13 — Evidence-Grounded Chapter Drafting

- Drafted S01–S31 in the frozen nine-chapter architecture and prescribed CH02–CH09 then CH01 order.
- Created 31 traceable section files, nine coherent chapter files, and `09_Manuscript/phase13_evidence_grounded_draft.md` (11,094 words; Abstract deferred).
- Deployed all 53 primary Global Claims in their primary sections and represented all eight Synthesis Propositions in a 63-row argument ledger.
- Used 77 canonical Paper IDs across 133 citation-placeholder occurrences; unknown citations = 0. `library_master.bib` was empty, so no BibTeX key was invented.
- Placed FIG-01–FIG-09 and TAB-01–TAB-08 exactly once as draft placeholders; no figure, final table, or quantitative plot was produced.
- Retained MP-033, MP-032, MP-028, and MP-029 as open; retained C004 as missing, RDE/detonation as analogue-only, and `tau_loading/tau_response` as a project hypothesis.
- Recorded two non-blocking issues (citation-key resolution and C004 source availability); blocking issues = 0 and architecture revision candidates = 0.
- Frozen Phase 10/11 evidence, Phase 12 architecture, raw PDFs, notes, per-paper extraction, evidence cards, schemas, Paper IDs, and literature corpus were not modified.
- Phase 14 readiness = READY; Phase 14 was not started.

## 2026-09-02 — Phase 13R — Physics-Led Manuscript Reconstruction

- Reconstructed 31 reader-facing sections and nine coherent chapters from scientific questions, physical variables, mechanism sequences, targeted paper-level evidence, and frozen boundary conditions.
- Created `09_Manuscript/phase13R_physics_led_draft.md` (11,516 words) without overwriting the Phase 13 manuscript.
- Fully reconstructed S01–S03 and S29–S31; deeply rewrote 24 sections; retained S24 as one compact moderate rewrite.
- Refined 30 of 31 section titles and lightly naturalized the CH09 title without changing section IDs, chapter order, or scientific scope.
- Retained 76 canonical Paper IDs across 140 citation-placeholder occurrences; unknown citations = 0 and all 53 primary deployment anchors are present in their assigned sections.
- Created `phase13R_title_map.csv` and a 31-row post-prose `phase13R_section_evidence_ledger.csv` for traceability only.
- Reduced the specified evidence-engineering and closure-audit phrases to zero manuscript occurrences while preserving condition limits in physical sentences.
- Placed FIG-01–FIG-09 and TAB-01–TAB-08 exactly once as placeholders; no final figure, table, Abstract, bibliography reconstruction, or journal formatting was produced.
- Retained MP-033, MP-032, MP-028, and MP-029 as open; retained C004 as missing, RDE/detonation as a bounded analogue, and the loading-duration/response-time ratio as a hypothesis rather than a universal parameter.
- Frozen evidence/synthesis inputs, raw PDFs, Paper IDs, and the original Phase 13 manuscript were not modified.
- Phase 14 readiness = READY; Phase 14 was not started.

## Phase 14 completed (2026-09-02)

- Created `08_Figures_Tables/phase14/` scientific figure/table production assets.
- Completed exact provenance and reuse/redraw classification for candidate literature panels.
- Audited all twelve quantitative candidates; produced only three within-study plots.
- Populated TAB-01–TAB-08 and created the table source map.
- Created `09_Manuscript/phase14_figtable_informed_draft.md` with three local, source-backed additions; Phase 13R was not overwritten.
- Recorded Phase 15 readiness and outstanding rights blockers in the Phase 14 QC report.
