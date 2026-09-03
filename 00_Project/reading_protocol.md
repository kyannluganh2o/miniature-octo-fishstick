# Scientific Reading Protocol

## 1. Purpose

This protocol governs scientific reading after Phase 5. It fixes reading depth, evidence provenance, and completion standards without changing literature classification or Paper IDs. A/B/C/D remain topic libraries; `reading_tier` records analysis depth only.

## 2. Tier Definitions

- **Tier 1 — Full pillar papers:** full-text pillar evidence for the mechanism-oriented review.
- **Tier 2 — Chapter-core papers:** targeted full-text reading of every section relevant to the assigned scientific questions.
- **Tier 3 — Supporting evidence papers:** claim-targeted reading for a specific claim, comparison, background statement, or knowledge gap.

Tier is independent of `must_read`, `reading_priority`, chapter assignment, citation count, and PDF availability. Only an explicit user/ChatGPT decision may reclassify a paper.

## 3. Source Hierarchy

Use the original PDF as the authority for scientific facts, followed by `library_master`, structured extraction, paper notes, the evidence base, chapter synthesis, and manuscript prose. Downstream content never overrides an upstream source. Important conclusions should remain traceable as `claim → paper_id → confirmed source location → original PDF`.

## 4. Full-text Availability Rules

Missing full text blocks reading but never lowers a tier or excludes a paper. Use `blocked_missing_pdf` until the canonical PDF is available and identity-matched. Do not substitute an abstract, search snippet, or secondary citation for unavailable full text when the requested evidence requires the original paper.

## 5. Tier 1 Reading Requirements

Read the complete scientific paper. Extract all relevant reported parameters, operating conditions, key quantitative results, confirmed figure/table/equation locations, claim-level evidence, mechanisms, limitations, contradictions, cross-paper links, and chapter relevance. Record what is not reported without filling gaps from memory.

## 6. Tier 2 Reading Requirements

Read the full text selectively but completely across all sections relevant to the assigned scientific questions. Extract key operating conditions, chapter-relevant parameters, principal quantitative results, important claims and evidence, mechanism relevance, limitations that affect use, and confirmed source locations. Unrelated sections need not receive line-by-line treatment.

## 7. Tier 3 Reading Requirements

Validate bibliographic identity, locate the relevant section, and extract only the information needed for a specific claim, comparison, background statement, or gap. Full cover-to-cover reading is not required by default. If a Tier 3 paper appears essential to a core argument, flag it and request user/ChatGPT reclassification; do not upgrade it autonomously.

## 8. Source-location Requirements

For material Tier 1 and Tier 2 information, record confirmed page, section, figure, table, or equation locators whenever available. Use only locators actually observed in the source. Never invent or infer a page, figure, table, or equation number. If localization is not confirmed, record `NV` or explain the limitation in `notes`.

## 9. Reported vs Derived vs Inferred

- `reported`: explicitly stated, tabulated, plotted, or otherwise shown by the paper.
- `derived`: calculated by the project workflow from reported inputs; record formula, inputs, units, and basis.
- `inferred`: a project scientific interpretation not directly stated by the paper; never present it as an author-reported result.

These states are mutually distinguishable. Author interpretation should also be identified as such in evidence records.

## 10. Parameter Extraction Rules

Use `05_Data_Extraction/schema/parameter_dictionary.yaml`, `units.yaml`, and `extraction_rules.md`. Preserve reported values and units alongside normalized values and units. Record definitions, reference scales, physical locations, reference frames, and context (`case_id`, `condition_id`, time/stage, spatial location) whenever they affect meaning. Do not perform external property lookup or estimate unreported properties during the current workflow.

## 11. Figure/Table/Equation Localization

When a value is obtained from a figure, table, or equation, record its identifier and page/section if confirmed, plus extraction method in `notes`. Digitized or equation-derived values are `derived` unless the source provides the exact number. Preserve uncertainty and do not imply greater precision than the source.

## 12. Mechanism Interpretation

Separate observation, author interpretation, project synthesis, and hypothesis. Do not rewrite correlation as causation. Preserve qualifiers such as “may,” “suggested,” or “possible.” Link mechanisms across scales only through supported definitions and evidence: wave/jet structure → local forcing → droplet/spray response → transport/phase change/mixing → ignition/combustion.

## 13. Contradiction Handling

Do not force conflicting results into agreement. Check definitions, gauge versus absolute pressure, gas/liquid properties, geometry, temperature, ambient density, reference scales for Mach/Re/We/Oh, droplet size and spacing, methods, resolution, regime, and measurement definitions. Record unresolved conflicts for later entry in `06_Evidence_Base/contradiction_matrix.csv` rather than resolving them by assumption.

## 14. Missing Information

Use `NR` when a relevant parameter is not reported, `NA` when it does not apply, and `NV` when a candidate value or locator is not verified. Never use numeric zero for missing information. Do not infer density, viscosity, surface tension, latent heat, or other properties from model memory.

## 15. Quality Control

Before marking work complete, verify paper identity, tier, context, controlled parameter name, value status, units, definition, source location, extraction status, and notes. Check that derived values are reproducible, inferred statements are labeled, dimensionless-number definitions are compatible before comparison, and no downstream record contradicts the PDF without an explicit conflict flag.

## 16. Completion Criteria

Tier 1 is complete only when the entire paper and all relevant evidence categories have been assessed. Tier 2 is complete only when all question-relevant sections and key evidence have been assessed. Tier 3 is complete only when the target claim or information need has been resolved or explicitly recorded as unavailable. `verified` additionally requires independent source-location and transcription checks. A blocked or unresolved item remains `blocked_missing_pdf` or `needs_review`; it is not complete.
