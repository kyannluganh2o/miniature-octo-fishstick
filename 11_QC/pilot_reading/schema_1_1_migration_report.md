# Schema 1.1 Migration Report

## 1. Scope

Phase 6.1 upgraded the parameter data contract from Schema 1.0 to 1.1 and migrated exactly 12 Pilot papers: A016, A020, A022, B011, B013, B029, C014, C016, C031, D003, D009, and D017. No literature was added and no bulk Tier 1 processing was started.

## 2. Pre-Migration State

The Phase 6 baseline contained 286 parameter observations across 12 per-paper JSON files. Value status was reported = 281, NA = 4, NR = 1, derived = 0, and inferred = 0.

## 3. Archive Snapshot

Twenty pre-migration files were copied to `99_Archive/old_versions/Phase6_1_pre_schema_1_1/`: four schema files, `parameter_master.csv`, 12 per-paper JSON files, the schema-gap log, Pilot extraction QC, and the Pilot validation report. Source and archive hashes matched.

## 4. Gap Inventory

The authoritative Pilot gap log contained 17 gaps: critical = 5, high = 9, medium = 2, and low = 1. Resolution status is recorded separately in `schema_gap_resolution.csv`; the original gap log was preserved.

## 5. Critical Gap Resolution

G001 NPR context, G002 Mach-disk state, G003 transient injector-pressure/NPR history, and G005 Weber reference scales were resolved by new explicit fields and relational tables. G007 loading duration was resolved by the typed-interval convention. No critical gap remains open or partial.

## 6. High Gap Resolution

All nine high-priority gaps were resolved through explicit source locators, case/condition scoping, Mach context and frame, dimensionless-number references, event chronology, process relations, or named characteristic-scale operands. No high-priority blocker remains.

## 7. Medium/Low Gap Resolution

One medium gap and the low gap were resolved directly; one medium gap was resolved by a documented machine-executable convention. No medium or low gap blocks migration.

## 8. Schema Architecture Changes

Schema 1.1 keeps the long-format parameter observation table and adds stable relational identifiers for provenance, ratio operands, dimensionless definitions, events, intervals, histories, and process/mechanism relations. Migration is additive and retains legacy fields.

## 9. New Tables

The migration created `source_locators.csv` (93 rows), `ratio_definitions.csv` (11), `dimensionless_definitions.csv` (56), `events.csv` (32), `intervals.csv` (14), `time_history_registry.csv` (12), header-only `time_series_points.csv`, `process_relations.csv` (16), and `pilot_mechanism_relations.csv` (24).

## 10. parameter_master Changes

All 286 original observations were preserved in their original order and values. Seventy-three new atomic or explicit missing-component records were appended, producing 359 unique parameter records. Post-migration value status is reported = 294, NA = 4, NR = 2, NV = 59, derived = 0, and inferred = 0.

## 11. Pilot Data Migration

All 12 per-paper JSON files now declare Schema 1.1 and contain additive relational arrays. Existing parameter content was retained, and per-paper parameters reconcile with the master table.

## 12. NPR Validation

Pressure ratios now record numerator, denominator, pressure basis, temporal basis, spatial basis, case/condition context, and source locator. Transient NPR is linked to an explicit history registry rather than being collapsed into a steady scalar.

## 13. Mach and M_s Validation

Mach records distinguish quantity meaning, local/reference state, spatial location, temporal state, frame, and source provenance. Where a source did not establish a frame, the uncertainty remains explicit rather than assumed.

## 14. Mach-Disk Validation

Mach-disk existence, formation, stabilization, position, and state are representable as separate parameters/events. Absence, non-applicability, and non-verification are not conflated.

## 15. We, Re, and Oh Validation

Dimensionless records link velocity, length, density, viscosity, surface-tension, and other applicable reference components. When a paper reports a dimensionless result without independently verified component values, the component records remain `NV` with reasons.

## 16. Loading-Duration Validation

Loading duration is represented by typed intervals with explicit endpoints. Shock-front passage, shocked state, pressure pulse, post-shock exposure, expansion-limited loading, and total forcing are not merged merely because their durations are similar.

## 17. Event Chronology

Events use stable identifiers, event types, reported/normalized time, reference events, and signed offsets. The convention preserves whether an event occurs before or after its reference.

## 18. Phase Change and Breakup

Evaporation, phase-change, deformation, and breakup processes are separated and may be linked by supported process relations. Correlation and author interpretation are not promoted to causality.

## 19. Mixing and Ignition

Mixing, ignition, flame transition, and detonation-related events can be ordered and related without forcing incompatible definitions into a single scalar chronology.

## 20. RDE Characteristic Scales

Evaporation length, detonation characteristic length, reaction-zone length, refill-zone length, wave height, and related ratios have named parameter identities. A reported ratio may coexist with `NV` standalone operands when the latter are not source-verified.

## 21. Provenance

Ninety-three normalized source locators connect reported and explicitly missing observations to verified document locations or retained legacy locator text. Locator identifiers are unique and all populated locator foreign keys resolve.

## 22. Data-Loss Audit

The 286 pre-migration observations were compared field by field with the archived master table and per-paper JSON records. No observation, reported value, unit, definition, source locator, Paper ID, or case/condition association was lost or rewritten.

## 23. Remaining Limitations

Remaining limitations are source-level, not schema-level: several Weber reference components are not independently reported; B029 histories remain figure-level without digitization; D003 has only one source-verified numeric interval; D009 standalone ratio operands are not verified; and several Mach frames are unstated. These are represented as `NV` or `NR` with explicit reasons, not guessed values.

## 24. Readiness

Schema 1.1 is **READY** for a separately authorized Phase 7 Tier 1 run: all critical gaps are resolved or convention-resolved, blocking high gaps are zero, all 12 migrations pass, identifiers and foreign keys validate, provenance is explicit, and no Pilot observation was lost. This report does not start Phase 7.
