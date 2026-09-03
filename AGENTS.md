# AGENTS.md — Project Operating Rules

This file defines the highest-level operating rules for coding and research agents working in this repository. These rules apply to all project operations unless the user gives a specific, explicit instruction that overrides them.

## 1. Project Mission

This project builds an auditable, traceable, mechanism-oriented academic review workflow. It is not a pipeline for producing isolated paper summaries.

```text
raw paper
→ machine-readable paper
→ structured paper note
→ parameter extraction
→ evidence base
→ cross-paper synthesis
→ manuscript chapter
```

Important scientific conclusions should be traceable whenever possible through:

```text
Claim → Paper ID → source location → original PDF
```

## 2. Source-of-Truth Hierarchy

Use this authority order:

1. Original PDF
2. `library_master`
3. Structured extraction
4. Paper notes
5. Evidence base
6. Chapter synthesis
7. Manuscript prose

The original paper is the final authority for scientific facts. `01_Library/master/library_master.csv` is the sole master index for literature identity and management status. Downstream derived information must never overwrite or redefine upstream evidence. If downstream content conflicts with the original PDF, the original PDF wins.

## 3. Immutable Raw Data Rule

`02_PDF_Raw/` is immutable raw data. Agents must not modify, overwrite, recompress and replace, or otherwise transform PDFs in place. Do not rename a PDF whose Paper ID has been formally locked unless the user explicitly instructs it. Do not create TXT, Markdown, JSON, images, logs, temporary files, or analytical output under `02_PDF_Raw/`. Write every derived output to `03_Paper_Processed/` or a later workflow directory.

**Never modify files under `02_PDF_Raw` unless the user explicitly instructs otherwise.**

## 4. Paper ID Policy

A finalized Paper ID is immutable. Expected forms include `A001`, `A002`, `B001`, `C001`, and `D001`.

- An ID does not change with chapter assignment or secondary topic.
- The same DOI or paper must not have multiple canonical IDs.
- Deduplication must identify one canonical Paper ID.
- Cross-directory records must use `paper_id` as the relational key.
- A paper such as `A023` remains `A023` even when it supports several chapters.

Stop and report any Paper ID conflict instead of resolving it by assumption.

## 5. Canonical PDF Naming

Use this recommended naming pattern for canonical PDFs:

```text
[PaperID]_[Year]_[FirstAuthor]_[ShortTitle].pdf
```

Example: `A023_2021_Wang_UnderexpandedJet.pdf`.

The filename is a human-readable label. The stable database association key is `paper_id`.

## 6. Literature Classification versus Chapter Assignment

The literature library (`A/B/C/D`) and manuscript chapter assignment are independent dimensions. **A/B/C/D are not manuscript chapters.** Do not express chapter assignment by copying PDFs into chapter folders. Record chapter relevance in `library_master`, chapter paper lists, and evidence matrices. One canonical paper and one canonical PDF may support multiple chapters.

## 7. Bibliographic Integrity

Bibliographic integrity is a highest-priority rule.

```text
Never invent bibliographic information.
Never generate a citation from memory.
Never fabricate a DOI.
Never fabricate a title.
Never fabricate authors.
Never fabricate journal information.
Never fabricate volume, issue, pages, article number, or publication year.
```

Use `unknown`, `not verified`, `needs verification`, or the project-defined missing-value representation when information is unavailable. Never make a plausible guess.

## 8. Evidence and Scientific Claim Policy

Classify each core scientific claim as one of the following:

- Reported result
- Author interpretation
- Agent synthesis
- Hypothesis
- Uncertainty

Do not rewrite correlation as causation unless the source and evidence support causality. Do not turn phrases such as “possible mechanism,” “suggested mechanism,” or “may be attributed to” into established facts.

For important mechanism claims, record the Paper ID and any source location that is actually confirmed: page, section, figure, table, or equation. Never fabricate a page number, figure number, or other source location.

## 9. Claim–Evidence Traceability

The evidence matrix must support at least these fields:

```text
claim_id
claim_text
paper_id
source_location
evidence_type
evidence_summary
evidence_strength
notes
```

Before writing chapters, use structured evidence in `06_Evidence_Base/` rather than model memory. Every material claim should have appropriate evidence and source location when available.

## 10. Contradictory Literature

Do not hide disagreement to make the narrative smoother. When results conflict, inspect differences in:

- pressure-ratio definition;
- absolute versus gauge pressure;
- injection and ambient pressure;
- gas composition and liquid properties;
- nozzle geometry and diameter;
- temperature and ambient density;
- Mach, Reynolds, Weber, and Ohnesorge number definitions;
- droplet size;
- experimental versus numerical methodology;
- spatial and temporal resolution;
- breakup regime; and
- measurement definition.

Record unresolved contradictions in `06_Evidence_Base/contradiction_matrix.csv`; do not force them into artificial agreement.

## 11. Parameter Extraction Rules

Parameter extraction must follow the future definitions in:

- `05_Data_Extraction/schema/parameter_dictionary.yaml`
- `05_Data_Extraction/schema/units.yaml`
- `05_Data_Extraction/schema/extraction_rules.md`

Agents must not independently redefine parameters. Where applicable, preserve `reported_value`, `reported_unit`, `normalized_value`, `normalized_unit`, `source_location`, and `extraction_notes`.

Strictly distinguish `reported`, `derived`, `estimated`, and `inferred`. Any agent-calculated value must be marked `derived` and accompanied by the formula or basis used.

## 12. Units and Definitions

- Prefer SI units in master tables.
- Preserve original reported units where needed for auditability.
- A unit conversion must not change the physical definition.
- State every pressure-ratio definition explicitly.
- Distinguish gauge pressure from absolute pressure.
- State the physical location or definition of every Mach number.
- For Weber number, record the characteristic velocity, length scale, and density definition whenever possible.
- Never assume that identical symbols imply identical definitions across papers.

## 13. Missing Data Policy

Never infer an unreported parameter. Use these codes:

- `NR` — Not Reported: the source does not report the value.
- `NA` — Not Applicable: the parameter does not apply to the configuration or analysis.
- `NV` — Not Verified: a candidate value exists but has not been verified against an authoritative source.

Never use numeric `0` to represent missing data.

## 14. Derived Files

`03_Paper_Processed/` is the reproducible machine-processing layer. A future per-paper layout may be:

```text
03_Paper_Processed/A/A023/
    text.md
    metadata.json
    sections.json
    references.json
    tables/
    figures/
    processing_log.json
```

Do not create this structure until the relevant processing task explicitly requires it.

## 15. Paper Notes

`04_Paper_Notes/` stores structured close-reading records produced by humans or agents. A paper note must go beyond an abstract and address, where supported: research question, configuration, operating conditions, methods, observations, quantitative results, mechanism, limitations, chapter relevance, and evidence value.

## 16. Evidence Base

`06_Evidence_Base/` supports cross-paper synthesis, not single-paper summaries. Its assets include:

- `claim_evidence_matrix.csv`
- `mechanism_matrix.csv`
- `contradiction_matrix.csv`
- `knowledge_gaps.csv`
- `evidence_cards/`

## 17. Manuscript Writing Rules

Do not jump directly from a large set of PDFs to final prose. Use:

```text
paper → extraction → evidence → synthesis → chapter draft
```

Core chapter claims require literature support. Do not pad citations, dump citations, merely list papers by author and year without synthesis, invent citations, hide uncertainty for fluency, or present agent inference as a published conclusion.

## 18. Chapter Writing Source Priority

Use this reading priority for chapter work:

1. `00_Project/`
2. `01_Library/master/`
3. `06_Evidence_Base/`
4. `05_Data_Extraction/`
5. `04_Paper_Notes/`
6. `03_Paper_Processed/`
7. `02_PDF_Raw/`

This is a workflow priority, not an authority reversal. If downstream content conflicts with the PDF, the original PDF wins.

## 19. File Modification Discipline

Before any batch operation, define the input directory, output directory, and file-matching rule. Avoid overwrites, add explicit overwrite protection, retain processing logs, and make scripts idempotent where practical.

Do not perform `rename all`, `delete all`, `move all`, or `overwrite all` operations without explicit user instruction. Preserve unrelated existing work.

## 20. Scripts

Scripts under `10_Scripts/` must be deterministic and idempotent where practical, use project-relative paths, avoid machine-specific temporary paths, emit error logs, give explicit errors for missing inputs, never silently skip failures, and never automatically delete source files.

## 21. Quality Control

`11_QC/` is used for citation audit, parameter audit, missing-PDF detection, duplicate detection, chapter consistency, and source traceability. Quality-control output must not overwrite source data.

## 22. Archive Rule

Use `99_Archive/` for superseded, rejected, or deprecated outputs that must be retained. Prefer archiving recoverable research material to permanent deletion.

## 23. Agent Stop Conditions

Stop the affected operation and report rather than guess when any of the following occurs:

- Paper ID conflict;
- one DOI maps to multiple canonical records;
- PDF and metadata clearly do not match;
- pressure definition cannot be confirmed;
- unit cannot be confirmed;
- page, figure, table, or equation location cannot be confirmed;
- CSV schema is incompatible;
- a target contains important content and the operation may overwrite it; or
- missing input makes data reliability unacceptable.

## 24. Current Project Phase

Current phase: **Project initialization and literature-library finalization.**

The complete A/B/C/D libraries, final `library_master`, final chapter structure, and final parameter schema are not yet locked. Agents must not assume that any of these items has been finalized.
