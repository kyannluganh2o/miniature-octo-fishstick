# Literature Library Curation and Engineering Workflow

## Purpose

This workflow separates upstream scientific judgment from downstream database engineering. A/B/C/D are literature topic libraries, not manuscript chapters. The current phase defines the data contract only; it does not import papers or assign final Paper IDs.

## Responsibility Boundary

User + ChatGPT perform scientific curation and semantic deduplication. Their screening, classification, grading, chapter-relevance, parameter-planning, and Keep/Exclude decisions are upstream curated decisions.

Codex performs engineering processing and deterministic integrity validation. Codex does not make semantic duplicate decisions and must not independently change an upstream scientific decision.

## Phase A — User + ChatGPT Scientific Curation

1. Literature search
2. Scope screening
3. Intra-library deduplication
4. Cross-library deduplication
5. Relevance grading
6. Preliminary chapter mapping
7. Must-read decision
8. Parameter-extraction planning
9. Keep/exclude decision
10. Library freeze

Phase A owns scientific relevance judgment, A/B/C/D classification, semantic duplicate identification, canonical-paper selection, and all decisions about whether a record should be retained or excluded.

## Phase B — Codex Engineering Processing

1. Import frozen library records
2. Normalize metadata format
3. Validate controlled vocabularies
4. Validate identifiers
5. Run deterministic integrity checks
6. Flag conflicts
7. Report unresolved issues
8. Assign Paper IDs only after approval
9. Lock Paper IDs
10. Build `library_master`
11. Track PDF acquisition
12. Continue downstream processing

Codex may normalize whitespace, remove a DOI URL prefix without changing the DOI content, validate formats, create approved relative paths, and update engineering statuses. Codex must not reinterpret scientific content to change a library, relevance grade, must-read status, reading priority, chapter mapping, parameter plan, or Keep/Exclude decision.

## Literature Deduplication Responsibility

Literature screening, semantic duplicate identification, and cross-library deduplication are performed upstream by the user with ChatGPT. Frozen A/B/C/D inputs are treated as curated literature records intended to be mutually unique.

Codex MUST NOT:

- decide that records are duplicates from similar titles, authors, topics, abstracts, or semantic similarity;
- merge or delete a suspected duplicate;
- select a canonical winner without an explicit upstream decision;
- change `library_primary` or reassign a record between libraries;
- change a user/ChatGPT Keep/Exclude decision; or
- write a final duplicate audit decision with Codex as the decision source.

Codex MAY check identical normalized DOI values, duplicate `paper_id`, duplicate `source_record_id`, exact normalized-title collisions, conflicting DOI mappings, malformed identifiers, invalid enum values, and missing mandatory identity fields. These checks are quality control, not semantic deduplication.

When a deterministic identity conflict is found:

```text
preserve all affected records
→ add a verification flag
→ do not merge
→ do not delete
→ do not reclassify
→ do not select a canonical winner
→ report the exact conflicting fields
→ wait for user/ChatGPT review
```

## Library Freeze

A library freeze means that the current round of searching, screening, scientific relevance judgment, deduplication, rating, classification, and Keep/Exclude decisions has produced a stable version for engineering processing. It does not mean the library can never receive another paper. Future additions must use an explicit incremental update process and must not silently rewrite prior records.

## Paper ID Assignment Gate

Paper IDs are not generated during schema initialization. Formal assignment requires this sequence:

```text
A library frozen
→ B library frozen
→ C library frozen
→ D library frozen
→ all upstream deduplication decisions confirmed
→ Codex deterministic integrity validation passed
→ all conflicts resolved by user/ChatGPT
→ Paper ID assignment
→ Paper ID lock
→ library_master construction
```

The approved `library_primary` determines the Paper ID prefix. Codex must not change the primary library to simplify numbering. After approval and lock, a Paper ID is immutable and does not change with chapter assignment, topic tags, PDF status, or reading status.

## Source Record and Canonical Record

`source_record_id` preserves the upstream working identity and remains in the audit trail after final assignment. `paper_id` is allowed to be empty until the assignment gate is passed. The final invariant is:

```text
one paper = one final Paper ID = one master record = one canonical PDF
```

## Chapter and Parameter Boundaries

Library assignment and chapter assignment are independent. Do not create chapter numbers or infer chapter mappings from A/B/C/D. `chapter_primary`, `chapter_secondary`, and `chapter_role` may remain empty until the manuscript structure is locked.

The parameter taxonomy is also not locked. This phase defines only the `parameter_groups` field and its semicolon-delimited format. Future parameter definitions must come from `05_Data_Extraction/schema/` in a separate approved phase.

## Incremental Updates

After a freeze, each addition or correction must identify its source, preserve prior identities, pass the same controlled-vocabulary and integrity checks, and document unresolved conflicts. Never replace an existing frozen record merely because a new record appears similar.

## Phase Roadmap After Frozen-Library Registration

```text
Phase 5: Tier registration
         → reading protocol
         → parameter schema

Phase 6: Pilot scientific reading

Phase 6.1: Parameter Schema 1.1 upgrade
           → additive Pilot migration
           → Pilot re-validation

Phase 7: Tier 1 corpus processing

Phase 8: Tier 2 chapter-focused processing

Phase 9: Tier 3 claim-targeted processing

Phase 10: Evidence-base construction

Phase 11: Cross-paper synthesis

Phase 12: Chapter Architecture + Figure/Table Planning + Writing Blueprint

Phase 13: Evidence-Grounded Chapter Drafting
```

Phase 5 establishes analysis depth and a Pilot-ready data contract only. It does not authorize paper processing, paper-note generation, evidence synthesis, chapter-directory creation, or manuscript drafting. Each later phase starts only by explicit instruction and must preserve the source hierarchy and immutable raw-PDF rule.

Phase 6.1 upgrades the parameter data contract and migrates only the 12 Phase 6 Pilot records. It does not start Phase 7, add literature, alter reading tiers or Paper IDs, or authorize bulk corpus processing. Phase 7 requires a separate explicit instruction after the Schema 1.1 readiness gate is accepted.

## Phase 10 — Global Evidence Consolidation

Status: completed on 2026-09-01.

Phase 10 consolidated the Pilot and Tier 1/2/3 candidate-evidence layers without reprocessing papers or modifying historical evidence cards. The completed evidence layer contains:

```text
candidate claims inventoried = 239
active consolidation candidates = 181
inventory-only / non-retained candidates = 58
normalized Global Claims = 53
Claim-Evidence links = 189
papers represented in active evidence = 106
global mechanism edges = 182
contradiction candidates adjudicated = 10
knowledge gaps mapped = 10
```

The coverage map rates M02, M04, and M05 strong; M01, M06, M07, M09, and M10 moderate; M03 and M08 limited; and M11 indirect-only. C004 / C-F-04 remains the sole missing PDF and is carried as an explicit coverage limitation rather than reconstructed from secondary material.

Minimal integrity checks passed with zero missing active source locators, zero orphan Claim-Evidence links, zero retained mechanism edges without source evidence, and zero knowledge gaps lacking a coverage-segment reference. Paper IDs, reading tiers, raw PDFs, and Parameter Schema 1.1 were unchanged.

Readiness for Phase 11 Cross-Paper Mechanistic Synthesis: READY. Phase 11 has not started and requires a separate explicit instruction.

## Phase 11 — Cross-Paper Mechanistic Synthesis

Status: completed on 2026-09-01.

Phase 11 consolidated the 53 frozen Global Claims and the Phase 10 evidence matrices into a mechanism-oriented synthesis layer under `06_Evidence_Base/synthesis/`:

```text
mechanism nodes = 22
mechanism pathways = 34
cross-scale transfer relations = 9
synthesis propositions = 8
mainline segments retained = M01–M11
candidate synthesis metrics = 1 (project hypothesis only)
```

The direct, indirect/mixed, cross-scale, and evidence-gap pathway classes remain separate. M03, M08, and M11 were not upgraded beyond the Phase 10 evidence. The central unclosed relations remain gas-jet shock topology to actual HPDI pilot loading, shock-mediated breakup/evaporation to measured HPDI mixture formation, and shock-caused mixture change to ignition/combustion response.

Global Claim IDs, Knowledge Gap IDs, Paper IDs, Parameter Schema 1.1, raw PDFs, Phase 10 evidence files, chapter structure, chapters, and manuscript files were unchanged. C004 remains missing.

Readiness for Phase 12 Chapter Architecture + Figure/Table Planning + Writing Blueprint: READY. Phase 12 has not started and requires separate explicit instruction.

## Phase 12 — Chapter Architecture + Figure/Table Planning + Writing Blueprint

Status: completed on 2026-09-01.

Phase 12 converted the frozen Phase 10/11 evidence and synthesis layers into a stable article construction plan without rereading the full corpus, changing scientific IDs, producing final figures/tables, or writing manuscript prose.

```text
chapters = 9
stable sections = 31
Global Claims with one primary section = 53 / 53
Synthesis Propositions deployed = 8 / 8
Mechanism Pathways represented = 34 / 34
Knowledge Gaps deployed = 10 / 10
core figures planned = 9
core tables planned = 8
quantitative candidates assessed = 12
writing cautions = 12
```

The stable architecture is recorded in `00_Project/chapter_structure.md`. The detailed section, claim, evidence, gap, caution, and traceability plans are under `07_Chapters/`; figure, table, and quantitative-synthesis plans are under the configured `08_Figures_Tables/` directory.

MP-033, MP-032, MP-028, and MP-029 are explicitly deployed as unclosed pathways. C004 / C-F-04 remains missing. Existing SP/GC/MP/KG IDs, Phase 10/11 scientific content, Parameter Schema 1.1, raw PDFs, per-paper assets, and `09_Manuscript/` were unchanged.

Readiness for Phase 13 Evidence-Grounded Chapter Drafting: READY. Phase 13 has not started and requires separate explicit instruction.

## Phase 13 — Evidence-Grounded Chapter Drafting

Status: completed on 2026-09-02.

Phase 13 drafted all 31 stable sections in the Phase 12 batch order, completed chapter-level and cross-chapter coherence passes, compiled nine chapter reading units and one full working manuscript, and created citation, evidence-ledger, section-status, and unresolved-issue support files.

```text
chapters drafted = 9 / 9
sections drafted = 31 / 31
working-draft words = 11094
Synthesis Propositions represented = 8 / 8
primary Global Claims deployed = 53 / 53
unique canonical papers cited = 77
unknown citations = 0
blocking drafting issues = 0
```

Because `library_master.bib` is empty, citations remain canonical `[[CITE:PaperID]]` placeholders; no bibliographic key or metadata was invented. MP-033, MP-032, MP-028, and MP-029 remain open, C004 remains missing, detonation/RDE evidence remains analogue-only for HPDI transfer, and `tau_loading/tau_response` remains a project hypothesis.

Readiness for Phase 14 Figure/Table Production + Quantitative Eligibility Audit + Manuscript Integration: READY. Phase 14 has not started and requires separate explicit instruction.

## Phase 13R — Physics-Led Manuscript Reconstruction

Status: completed on 2026-09-02.

Phase 13R reconstructed the Phase 13 scientific content as a reader-facing, mechanism-led review while retaining the frozen scientific architecture and canonical Paper-ID citation system. All 31 sections and nine chapters were rewritten in the prescribed physics-first order and compiled into `09_Manuscript/phase13R_physics_led_draft.md` without overwriting the Phase 13 manuscript.

```text
chapters reconstructed = 9 / 9
sections reconstructed = 31 / 31
working-manuscript words = 11516
full reconstructions = 6
deep rewrites = 24
moderate rewrites = 1
reader-facing section titles refined = 30 / 31
primary Global Claim deployment anchors present = 53 / 53
unique canonical papers cited = 76
citation-placeholder occurrences = 140
unknown citations = 0
```

CH01 and CH09 were fully reconstructed; CH03, S20, and S25 received major reconstruction. Internal evidence-ontology language no longer structures the prose. MP-033, MP-032, MP-028, and MP-029 remain open; C004 remains missing; detonation/RDE evidence remains a bounded strong-wave analogue; and the loading-duration/response-time ratio remains a non-universal project hypothesis.

Readiness for Phase 14 Figure/Table Production + Quantitative Eligibility Audit + Manuscript Integration: READY. Phase 14 has not started and requires separate explicit instruction.

## Phase 14 — Scientific Figure/Table Production (completed)

Completed 2026-09-02. Nine figure specifications, nine SVG/PNG working drafts, eight populated reader tables, a rights-aware source/reuse inventory, twelve case-level quantitative eligibility decisions, three within-study plots, and a targeted Phase 14 manuscript draft were produced. No new literature was introduced. Phase 15 readiness is recorded in `11_QC/phase14_figure_table_report.md`.
