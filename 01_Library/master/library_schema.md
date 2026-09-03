# Literature Database Schema

Schema version: 1.1  
Status: Active frozen-library schema

## 1. Purpose

This document defines the machine-readable data contract for frozen A/B/C/D literature-library records, the global literature master, exclusion audit logs, source-to-Paper-ID mapping, and search provenance. It defines structure and validation only; it contains no real or example literature records.

## 2. Responsibility Boundary

User + ChatGPT perform scientific curation and semantic deduplication. This includes literature searching, scope screening, scientific relevance judgment, A/B/C/D classification, intra-library and cross-library deduplication, relevance grading, must-read decisions, chapter relevance, parameter-extraction planning, and Keep/Exclude decisions.

Codex performs engineering processing and deterministic integrity validation. Codex may normalize data representation, validate controlled vocabularies and identifiers, report conflicts, generate approved file paths, assign Paper IDs after approval, and track processing status. Codex does not make semantic duplicate decisions and must not change upstream curated decisions.

## 3. Data Model

The data model separates five concerns:

1. Frozen library inputs: `A_fixed.csv`, `B_fixed.csv`, `C_fixed.csv`, and `D_fixed.csv`.
2. Canonical global index: `library_master.csv`.
3. Historical identity mapping: `paper_id_map.csv`.
4. Exclusion and duplicate-decision audit logs under `01_Library/excluded/`.
5. Search provenance: `search_log.csv`.

The target invariant after approved Paper ID assignment is:

```text
one paper = one final Paper ID = one master record = one canonical PDF
```

## 4. Source Record vs Final Paper ID

`source_record_id` is the persistent upstream working identifier. It must remain available after final Paper ID assignment because it is part of the audit trail.

`paper_id` is the final canonical identifier. It may be empty during curation and validation. Its required format after assignment is `^[ABCD][0-9]{3}$`. Once explicitly approved and locked, it is immutable.

The valid pre-assignment state is therefore: populated `source_record_id` and empty `paper_id`.

## 5. Literature Libraries

`library_primary` is one of `A`, `B`, `C`, or `D` and is supplied by user + ChatGPT. Codex must preserve it. `library_secondary` is optional and may contain multiple explicitly approved library codes separated by `;`.

A/B/C/D are literature topic libraries. They are not manuscript chapters and must never be hard-mapped to chapter numbers. Chapter mapping uses separate chapter fields.

## 6. library_master.csv

The canonical header, in fixed order, is:

```text
paper_id,source_record_id,library_primary,library_secondary,record_status,title,authors,first_author,year,journal,volume,issue,pages_or_article_number,doi,doi_status,publication_type,language,bibtex_key,relevance_grade,relevance_score,relevance_reason,must_read,reading_tier,reading_priority,final_decision,exclusion_reason,chapter_primary,chapter_secondary,chapter_role,topic_tags,parameter_groups,pdf_status,pdf_filename,pdf_relpath,pdf_match_status,text_status,note_status,extraction_status,evidence_status,citation_status,source_database,source_url,search_batch_id,verification_flags,date_added,date_updated,notes
```

`duplicate_of` is intentionally absent. Confirmed duplicate history belongs in `duplicates.csv` and `paper_id_map.csv`.

## 7. Field Definitions

Legend: **R** = required for an imported master record; **O** = optional; **C** = conditionally required. “Mutable” describes changes after initial population; locked identifiers remain immutable.

| Field | Type | Req. | Allowed values / format | Multi-value | Purpose | Population and change rule |
|---|---|---:|---|---|---|---|
| `paper_id` | string | C | `^[ABCD][0-9]{3}$` or empty before assignment | No | Final canonical key | Assigned only after the approval gate; immutable after lock |
| `source_record_id` | string | R | Non-empty upstream identifier | No | Preserves source identity | Imported from curated input; retained permanently |
| `library_primary` | enum | R | `A`, `B`, `C`, `D` | No | Primary topic library | Set upstream; Codex must not reclassify it |
| `library_secondary` | enum list | O | `A`, `B`, `C`, `D` | `;` | Explicit cross-library relevance | Set or changed only by user/ChatGPT instruction |
| `record_status` | enum | R | `candidate`, `screened`, `retained`, `excluded`, `pending_verification` | No | Curation/identity state | Imported or updated from approved workflow state |
| `title` | string | R | Verbatim verified title or unverified supplied title | No | Primary identity metadata | Never guessed; corrections require evidence |
| `authors` | string | O | Source-reported author list | No | Full authorship metadata | Never guessed; normalize formatting without changing identity |
| `first_author` | string | O | Source-supported first author | No | Naming and lookup support | Derived only from verified `authors` or source metadata |
| `year` | integer/string | O | Four-digit year when verified | No | Publication year | Never inferred from incomplete evidence |
| `journal` | string | O | Source-supported publication venue | No | Bibliographic metadata | Never guessed |
| `volume` | string | O | Source-supported value | No | Bibliographic metadata | Never guessed |
| `issue` | string | O | Source-supported value | No | Bibliographic metadata | Never guessed |
| `pages_or_article_number` | string | O | Source-supported pages or article number | No | Bibliographic locator | Never guessed |
| `doi` | string | O | Bare `10.` DOI form without URL prefix | No | Persistent publication identifier | Trim and remove DOI URL prefix only; never alter DOI content or infer it |
| `doi_status` | enum | R | `verified`, `unverified`, `missing`, `conflict` | No | DOI confidence state | Updated only from evidence or detected conflict |
| `publication_type` | enum | O | `journal_article`, `review_article`, `conference_paper`, `book_chapter`, `thesis`, `report`, `other` | No | Stable publication category | Leave empty if incomplete information prevents classification |
| `language` | string | O | Language code or approved label | No | Publication language | Populate from verified metadata |
| `bibtex_key` | string | O | Project-approved unique key | No | Link to bibliography record | Populate when bibliography is constructed; must be unique |
| `relevance_grade` | enum | O | `S+`, `S`, `A`, `B`, `C` | No | Upstream scientific relevance grade | Codex validates but never rerates |
| `relevance_score` | integer | O | `1`–`5` | No | Numeric relevance score | Upstream decision; Codex only validates mapping |
| `relevance_reason` | string | O | Curated scientific rationale | No | Explains relevance judgment | Preserve meaning; only whitespace/encoding cleanup allowed |
| `must_read` | enum | O | `yes`, `no`, `pending` | No | Full-reading requirement | Upstream decision only |
| `reading_tier` | enum | R | `tier1`, `tier2`, `tier3` | No | Frozen reading-depth assignment | Imported from the approved 115-paper tier plan; change only by explicit user/ChatGPT reclassification |
| `reading_priority` | enum | O | `critical`, `high`, `medium`, `low`, `pending` | No | Reading order | Upstream decision only |
| `final_decision` | enum | R | `keep`, `exclude`, `pending` | No | Final curation disposition | Change only by explicit user/ChatGPT decision |
| `exclusion_reason` | enum | C | `duplicate`, `low_relevance`, `outside_scope`, `insufficient_scientific_value`, `non_primary_source`, `metadata_problem`, `unavailable_full_text`, `other` | No | Structured reason for exclusion | Required when excluded where an approved reason exists; missing PDF alone does not trigger exclusion |
| `chapter_primary` | string | O | Approved chapter identifier | No | Primary manuscript relevance | Empty until chapter structure is locked; upstream assignment only |
| `chapter_secondary` | string list | O | Approved chapter identifiers | `;` | Additional chapter relevance | Empty until approved; do not use comma separators |
| `chapter_role` | enum | O | `core_evidence`, `supporting_evidence`, `methodological_reference`, `background`, `contradictory_evidence`, `mechanism_support`, `review_context` | No | Function within chapter synthesis | Upstream assignment; not mandatory for every record |
| `topic_tags` | string list | O | Future approved taxonomy | `;` | Mechanism/topic descriptors | Populate after taxonomy approval; Codex must not invent a competing taxonomy |
| `parameter_groups` | string list | O | Future schema-defined groups | `;` | Planned parameter extraction | Populate from upstream plan and later parameter dictionary |
| `pdf_status` | enum | O | `not_requested`, `missing`, `downloaded`, `verified`, `unavailable` | No | PDF acquisition state | Engineering status; do not auto-exclude on missing PDF |
| `pdf_filename` | string | O | `{paper_id}_{year}_{first_author}_{short_title}.pdf` after assignment | No | Canonical PDF filename | Generate only when required identity fields are verified |
| `pdf_relpath` | string | O | Project-relative path under `02_PDF_Raw/` | No | Portable PDF location | Never store a machine-specific absolute path |
| `pdf_match_status` | enum | O | `not_checked`, `matched`, `mismatch`, `ambiguous` | No | PDF-to-record identity state | Set `matched` only after deterministic identity verification |
| `text_status` | enum | O | `not_started`, `processed`, `failed`, `needs_review` | No | Machine-readable text status | Updated by processing workflow |
| `note_status` | enum | O | `not_started`, `draft`, `complete`, `verified`, `needs_review` | No | Paper-note status | Updated by note workflow |
| `extraction_status` | enum | O | `not_started`, `partial`, `complete`, `verified`, `needs_review` | No | Parameter-extraction status | Updated by extraction workflow |
| `evidence_status` | enum | O | `not_started`, `partial`, `complete`, `verified`, `needs_review` | No | Evidence-base integration status | Updated by evidence workflow |
| `citation_status` | enum | O | `unverified`, `verified`, `issue` | No | Citation verification state | Updated by citation audit |
| `source_database` | string | O | Database/source name | No | Search provenance | Imported from search records |
| `source_url` | string | O | Source URL | No | Record provenance | Preserve supplied source; do not fabricate |
| `search_batch_id` | string | O | Existing batch identifier | No | Links record to search log | Imported from search workflow |
| `verification_flags` | enum/string list | O | Approved flags including `doi_conflict`, `year_conflict`, `title_conflict`, `author_conflict`, `possible_duplicate`, `library_conflict`, `rating_conflict`, `pdf_identity_conflict` | `;` | Records unresolved issues | Codex may add deterministic flags; a flag is not a semantic decision |
| `date_added` | date | O | `YYYY-MM-DD` | No | Record creation date | Set on controlled import; preserve thereafter |
| `date_updated` | date | O | `YYYY-MM-DD` | No | Last approved record update | Update when the record changes |
| `notes` | string | O | Free text | No | Supplemental context | Do not hide information here when a structured field exists |

## 8. Controlled Vocabularies

Controlled values are case-sensitive and must match Section 7. Invalid values are flagged, not silently coerced. Empty is distinct from every enum value.

`record_status` meanings:

- `candidate`: upstream screening is incomplete.
- `screened`: preliminary screening is complete but the library is not frozen.
- `retained`: upstream decision is to retain.
- `excluded`: upstream decision is to exclude.
- `pending_verification`: metadata or identity requires review.

`doi_status` meanings:

- `verified`: confirmed through a reliable source or original paper.
- `unverified`: a DOI string exists but is not reliably verified.
- `missing`: no DOI is currently available.
- `conflict`: sources provide inconsistent DOI values.

## 9. Relevance Rating

Relevance is an upstream scientific judgment. The meanings are:

- `S+`: indispensable/core paper; default score `5`.
- `S`: highly important core paper; default score `4`.
- `A`: strongly relevant; default score `3`.
- `B`: useful supporting paper; default score `2`.
- `C`: peripheral or weak relevance; default score `1`.

Relevance grades A/B/C are entirely different from literature libraries A/B/C/D. A grade/score mismatch is flagged as `rating_conflict` and reported; Codex must not correct either value independently.

## 10. Must-read Classification

- `yes`: full-text close reading is required.
- `no`: usable as background/support but not a priority full-text reading target.
- `pending`: no final decision.

Reading priority is `critical`, `high`, `medium`, `low`, or `pending`. Both fields are upstream decisions. Codex must not upgrade or downgrade them.

## 11. Chapter Mapping

`chapter_primary`, `chapter_secondary`, and `chapter_role` are independent of A/B/C/D. All may remain empty while the chapter structure is unlocked. Multiple secondary chapters use `;`, never commas. Codex must not create chapter identifiers or infer chapters from library membership.

## 12. Parameter Extraction Mapping

`parameter_groups` records planned extraction groups and uses `;` for multiple values. The definitive taxonomy will be governed by `05_Data_Extraction/schema/parameter_dictionary.yaml` in a later phase. Codex must not create or substitute an independent taxonomy.

## 13. Status Fields

Processing status fields are engineering state, not scientific value judgments. Their controlled values are defined in Section 7. A failed or missing PDF state does not authorize exclusion. Status changes must reflect actual completed operations and must not be used to imply verification that did not occur.

## 14. CSV Rules

All project CSV files governed here are UTF-8 and comma-delimited.

1. The first and only initial row is the header.
2. Do not add blank title rows or example data.
3. Use standard CSV quoting for fields containing commas, quotes, or line breaks.
4. Use `;` for multi-value fields; do not use commas or locale punctuation as internal multi-value delimiters.
5. Leave currently missing values empty; never use numeric `0` as a missing-value marker.
6. Column names use `snake_case` and must remain in the defined order.
7. No header may contain duplicate column names.
8. Spreadsheet merged cells have no place in CSV data.

The four fixed-library files have the identical header:

```text
source_record_id,paper_id,title,authors,year,journal,doi,doi_status,relevance_grade,relevance_score,relevance_reason,must_read,reading_tier,reading_priority,chapter_primary,chapter_secondary,chapter_role,topic_tags,parameter_groups,final_decision,exclusion_reason,verification_flags,notes
```

Their library is determined by their approved file/library context. These files receive only records already screened and deduplicated upstream.

## 15. Upstream Deduplication Policy

Semantic duplicate identification and cross-library deduplication belong to user + ChatGPT. Codex MUST NOT decide duplicates from similar titles, authors, topics, abstracts, or meaning; merge records; delete suspected duplicates; select a canonical paper; move a record between libraries; or change Keep/Exclude decisions.

Retained frozen records are intended to be mutually unique. That expectation does not remove the requirement for deterministic quality checks.

## 16. Codex Integrity Validation

Codex may detect and flag:

- identical normalized DOI values;
- duplicate `source_record_id`;
- duplicate final `paper_id`;
- exact normalized-title collisions;
- invalid ID or DOI format;
- enum mismatch;
- grade/score mismatch;
- conflicting mappings; and
- missing mandatory identity fields.

Integrity validation is not deduplication. Similar title, similar authors, similar topic, or similar abstract is insufficient for a duplicate decision.

For every potential conflict, Codex must preserve all records, add an appropriate verification flag, refrain from deletion/merge/reclassification/canonical selection, report the exact conflicting fields, and stop automated handling of that conflict pending user/ChatGPT review.

## 17. Duplicate Audit Log

`duplicates.csv` is the audit log for confirmed upstream duplicate decisions, not an output table for Codex semantic judgments. Its fixed header is:

```text
duplicate_record_id,duplicate_library,canonical_record_id,canonical_paper_id,duplicate_type,matching_basis,doi,title,decision_source,decision_date,notes
```

| Field | Type | Req. | Allowed / purpose |
|---|---|---:|---|
| `duplicate_record_id` | string | R | Upstream identifier of confirmed duplicate record |
| `duplicate_library` | enum | R | `A`, `B`, `C`, `D`; original library |
| `canonical_record_id` | string | R | Upstream identifier selected as canonical by user/ChatGPT |
| `canonical_paper_id` | string | O | Locked final ID when available; empty before assignment |
| `duplicate_type` | enum | R | `exact_duplicate`, `cross_library_duplicate`, `metadata_variant`, `other` |
| `matching_basis` | enum | R | `same_doi`, `same_title`, `same_title_and_authors`, `manual_verification`, `user_chatgpt_decision`, `other` |
| `doi` | string | O | Normalized DOI retained for audit |
| `title` | string | O | Supplied title retained for audit |
| `decision_source` | enum | R | `user`, `chatgpt`, `user_and_chatgpt`, `manual_review`; never `codex` |
| `decision_date` | date | O | `YYYY-MM-DD` |
| `notes` | string | O | Supplemental audit context |

Codex may write a confirmed decision only when the decision has been explicitly supplied upstream.

## 18. Paper ID Mapping

`paper_id_map.csv` preserves historical source identity to final Paper ID. Its fixed header is:

```text
source_record_id,source_library,canonical_paper_id,mapping_status,mapping_basis,doi,title,notes
```

| Field | Type | Req. | Allowed / purpose |
|---|---|---:|---|
| `source_record_id` | string | R | Historical upstream identity |
| `source_library` | enum | R | `A`, `B`, `C`, `D` |
| `canonical_paper_id` | string | C | Locked canonical ID; empty while unassigned |
| `mapping_status` | enum | R | `unassigned`, `canonical`, `mapped_duplicate`, `excluded`, `pending` |
| `mapping_basis` | enum | O | `direct_assignment`, `user_chatgpt_deduplication`, `manual_verification`, `other` |
| `doi` | string | O | Normalized DOI used for audit, never guessed |
| `title` | string | O | Source title used for audit |
| `notes` | string | O | Supplemental mapping context |

Codex must not set `mapped_duplicate` from semantic similarity.

The remaining governed audit/provenance headers and their table-specific fields are:

### low_relevance.csv

```text
source_record_id,library,title,authors,year,journal,doi,relevance_grade,relevance_score,exclusion_reason,decision_source,decision_date,notes
```

`library` is enum A/B/C/D. `decision_source` is `user`, `chatgpt`, `user_and_chatgpt`, or `manual_review`. `decision_date` is `YYYY-MM-DD`. All shared bibliographic and relevance fields follow Section 7. This table records confirmed low-relevance decisions only.

### excluded_other.csv

```text
source_record_id,library,title,authors,year,journal,doi,exclusion_category,exclusion_reason,decision_source,decision_date,notes
```

`library`, `decision_source`, and `decision_date` follow the preceding definitions. `exclusion_category` is an approved structured category; `exclusion_reason` stores the upstream rationale. This table must not be populated from an autonomous Codex scientific judgment.

### search_log.csv

```text
search_batch_id,search_date,database,query,filters,result_count,records_added,operator,notes
```

`search_batch_id` is the unique batch key; `search_date` is `YYYY-MM-DD`; `database`, `query`, and `filters` preserve search provenance; `result_count` and `records_added` are non-negative integers when reported; `operator` identifies the human or approved system performing the search; `notes` contains supplemental context. The current schema stage adds no search rows.

## 19. Paper ID Assignment and Lock

No Paper ID is assigned during schema initialization. Assignment requires all four libraries to be frozen, all upstream deduplication decisions to be confirmed, deterministic integrity validation to pass, and every conflict to be resolved by user/ChatGPT.

After approval, the Paper ID prefix follows locked `library_primary`. Codex must not reclassify a paper for numbering convenience. Once locked, the ID cannot change because of chapter, topic, PDF, reading, note, or extraction status.

## 20. Library Freeze

A library freeze means that the current searching, screening, relevance judgment, semantic deduplication, rating, classification, and Keep/Exclude decisions form a stable engineering input. Freeze does not prohibit later additions; every addition must follow an explicit incremental update process with provenance and validation.

## 21. Global Master Construction

Construct `library_master.csv` only after the Paper ID assignment gate is satisfied. Import approved frozen records without altering their scientific decisions. The master is the sole canonical literature identity and management index. A confirmed retained paper receives one master row and one canonical PDF association.

## 22. Validation Rules

Before import or master construction, validate:

- exact header and column order;
- unique column names;
- UTF-8 comma-delimited encoding;
- controlled vocabulary membership;
- Paper ID regex when populated;
- unique `source_record_id` and populated `paper_id`;
- bare DOI representation and deterministic duplicate DOI collisions;
- exact normalized-title collisions;
- relevance grade/score consistency;
- semicolon use in multi-value fields;
- `YYYY-MM-DD` dates;
- relative, not absolute, PDF paths;
- required identity fields; and
- absence of silent record deletion or merging.

Failures must be preserved, flagged, and reported. Validation never authorizes semantic decisions.

## 23. Schema 1.1 Migration

Schema 1.1 adds the required controlled field `reading_tier` immediately after `must_read` in `library_master.csv` and all four fixed-library tables. Existing rows were migrated using the approved 115-paper tier plan.

- No field was removed or renamed.
- No scientific record was added, deleted, merged, or reclassified.
- No Paper ID or source-to-Paper-ID mapping was changed.
- All pre-existing cell values were preserved; only `reading_tier` was added and populated.

## 24. Change Control

After real data entry begins, do not casually rename or delete columns, change column order, alter enum meanings, change delimiter rules, change the Paper ID format, redefine relevance grades, or revise controlled vocabularies.

Any necessary schema change must:

1. document the reason;
2. increment the schema version;
3. describe the migration;
4. identify affected files and records;
5. preserve auditability; and
6. receive explicit approval before data migration.
