# HPDI Shock–Droplet Review

## Project Overview

This repository supports a mechanism-oriented academic review of high-pressure gas–liquid direct injection, underexpanded compressible jets, shock structures, spray and droplet breakup, and shock–droplet interaction. The planned evidence base is expected to retain approximately 120 core and supporting references, but the literature set is still being finalized.

## Research Scope

The project covers HPDI and pilot-ignited high-pressure direct injection, underexpanded jets, shock-cell structures, barrel shocks, Mach disks, gas–liquid interaction, atomization, droplet breakup, shock-induced secondary breakup, and multiphase compressible-flow mechanisms.

## Research Objective

The objective is not merely to summarize publications. The workflow compares experimental, numerical, and theoretical findings; extracts controlling parameters; constructs a cross-paper evidence base; identifies consistent trends and contradictory results; examines differences in operating conditions and definitions; develops mechanism-level relationships; and identifies knowledge gaps.

## Literature Library System

`A`, `B`, `C`, and `D` are thematic literature-library classifications. They are not manuscript chapters. A paper may support multiple chapters while retaining one canonical Paper ID and one canonical PDF. After the literature libraries are finalized and an ID is locked, the Paper ID remains immutable.

## Repository Structure

```text
00_Project/             Review scope, questions, terminology, workflow, and planning
01_Library/             Canonical literature index, thematic libraries, and search records
02_PDF_Raw/             Immutable original PDFs and no derived content
03_Paper_Processed/     Reproducible machine-readable paper outputs
04_Paper_Notes/         Structured close-reading notes for individual papers
05_Data_Extraction/     Parameter schemas, per-paper extraction, and master tables
06_Evidence_Base/       Claims, mechanisms, contradictions, gaps, and evidence cards
07_Chapters/            Future chapter synthesis; chapter structure is not yet locked
08_Figures_Tables/      Figures, tables, source data, and permissions records
09_Manuscript/          Working manuscript, clean manuscript, references, and submission files
10_Scripts/             Processing, metadata, extraction, citation, and QC scripts
11_QC/                  Citation, parameter, PDF, duplicate, and consistency audits
99_Archive/             Retained old, rejected, or deprecated outputs
```

## Core Data Flow

```text
PDF
↓
machine-readable extraction
↓
paper note
↓
parameter extraction
↓
evidence matrix
↓
cross-paper synthesis
↓
chapter draft
↓
manuscript
```

## Source-of-Truth Rules

`02_PDF_Raw/` is the immutable primary source for paper content. `01_Library/master/` contains the canonical literature index for identity and management status. Derived records must not overwrite upstream evidence; when a derived record conflicts with an original paper, the original PDF wins.

## Paper ID Convention

Expected Paper IDs have forms such as `A001`, `B014`, `C027`, and `D006`. The letter identifies the thematic library, not a manuscript chapter. Once finalized, a Paper ID is immutable and serves as the stable key across project directories.

## PDF Management

The recommended canonical filename is:

```text
{PaperID}_{Year}_{FirstAuthor}_{ShortTitle}.pdf
```

Each paper should have one canonical PDF. Original PDFs must not be overwritten, converted in place, or mixed with derived TXT, Markdown, JSON, image, or analysis files.

## Evidence-Based Review Workflow

Important scientific claims should be traceable whenever possible to a Paper ID plus a confirmed source location such as a page, section, figure, table, or equation. Evidence matrices must distinguish reported results, author interpretations, agent synthesis, hypotheses, and uncertainty. Cross-paper synthesis should be based on project evidence rather than model memory.

## Current Project Status

- Directory initialization completed.
- Project-level configuration established.
- A/B/C/D literature libraries are still being finalized.
- Final chapter structure has not yet been locked.
- PDF batch processing has not yet started.

This status does not imply that all planned references have been acquired.

## Working with Codex

Codex and other agents must read `AGENTS.md` before project work. They must not modify raw PDFs, invent bibliography or citations, or overwrite existing research data without confirmation. Batch-processing scripts should be deterministic and idempotent where practical. Scientific synthesis must use verified project evidence rather than model memory.

## Important Restrictions

- Do not fabricate bibliographic metadata, citations, source locations, or parameters.
- Do not use `0` for missing data; use the project missing-value codes.
- Do not duplicate PDFs to represent chapter assignment.
- Do not assume that the final literature set, chapter structure, or parameter schema is already locked.
- Do not silently overwrite, rename, move, or delete research assets.
