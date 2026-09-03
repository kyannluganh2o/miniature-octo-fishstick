# Parameter Extraction Rules — Schema 1.1

Schema version: 1.1  
Status: Pilot-validated revision  
Previous version: 1.0

## 1. Scope

These rules govern extraction into the long-format parameter database and its normalized relational extensions. They define how to transcribe, normalize, qualify, migrate, and verify data. They do not authorize processing additional literature or starting a later workflow phase.

## 2. Source Priority

The original PDF is authoritative. Prefer the paper's main text, tables, figures, equations, and supplementary material over metadata, notes, or secondary citations. If downstream content conflicts with the PDF, preserve the conflict and follow the PDF.

## 3. Reported Values

Mark `reported` only when a value or qualitative result is explicitly stated or shown. Preserve wording, value, unit, uncertainty, context, definition, and confirmed source location. Do not add precision or reinterpret an author's variable as a project variable without evidence.

## 4. Derived Values

Mark project-calculated values `derived`. Retain the reported inputs, formula, assumptions, unit conversions, and calculation basis in `definition` or `notes`. Do not derive a value when a required input, property, definition, or unit is missing or unverified.

## 5. Inferred Values

Mark a scientific interpretation not directly stated by the paper `inferred`. An inferred value or mechanism is never presented as an author-reported result. Preserve uncertainty and distinguish project synthesis from author interpretation.

## 6. Unit Normalization

Preserve `reported_value` and `reported_unit`; store SI conversions separately as `normalized_value` and `normalized_unit`. Use `units.yaml`. Convert only when units and physical definitions are confirmed. Never use a unit conversion to reconcile different variable definitions.

## 7. Dimensionless Numbers

Record reported and derived values separately. For We, Re, Oh, Mach, density ratio, viscosity ratio, and pressure ratio, retain the original definition and all applicable reference velocity, length, density, viscosity, surface tension, pressure points, frame, and physical location. Equal values with incompatible definitions are not equivalent; flag `definition_mismatch` in `notes` or QC.

## 8. NPR

Do not map an unspecified “pressure ratio” automatically to `NPR`. Record `NPR_reported`, `NPR_definition`, numerator, denominator, and whether pressures are absolute or gauge. Populate `NPR_derived` only from verified, definition-compatible pressures and record the formula.

## 9. Shock Mach Number

Identify the physical wave, measurement/derivation method, location, and reference frame. Keep incident, transmitted, reflected, and other wave Mach numbers separate. Populate `M_s` only with an explicit `M_s_definition` and `M_s_reference_frame`; never collapse distinct waves into one value.

## 10. Mach Disk

Confirm whether a Mach disk is present and record the position/diameter definition and nozzle reference diameter. Distinguish steady position, transient position, maximum position, and time-resolved position using context and `time_or_stage`. Do not compare normalized positions when the reference diameter differs or is unknown.

## 11. Shock Curvature

Preserve reported geometry and curvature definitions. Allowed geometry categories are `planar`, `cylindrical`, `spherical`, `divergent`, `curved_local`, and `unknown`. Do not assign `shock_curvature = 0` to planar shocks unless a later approved project convention explicitly defines that representation; use category plus `NA` or `NR` as appropriate.

## 12. Loading Duration

Record start, end, definition, and time scale. Shock-passage duration, high-speed-gas exposure, pressure loading, aerodynamic forcing, and wave residence time are not assumed equivalent. Normalize only when the endpoints and physical basis are compatible.

## 13. Droplet Parameters

Record initial versus evolving diameter, radius, temperature, velocity, and properties separately in context. Do not supply unreported density, viscosity, surface tension, specific heat, or latent heat from memory. Current policy permits no external property lookup; a future external source must be separately cited and labeled.

## 14. Multi-droplet S/D

For `S_over_D`, record `spacing`, `spacing_definition`, and the meanings of both S and D, including direction, center-to-center or surface gap, droplet diameter choice, and arrangement when reported. A dimensionless S/D without these definitions is not sufficient for cross-paper equivalence.

## 15. Breakup Regimes

Preserve the author's original regime terminology and classification basis. A project taxonomy may be recorded separately but must not overwrite the source terminology. Do not force ambiguous observations into bag, multimode, shear-stripping, catastrophic, KH, or RT categories.

## 16. Phase Change

Distinguish observed vaporization from modeled evaporation and from inferred mass loss. Record phase-change model, conditions, mass-loss definition, and transcritical state when supported. Do not infer vaporization merely from droplet-size reduction if deformation, imaging limits, or breakup could explain it.

## 17. Mixing and Ignition

Qualitative mixing or combustion evidence is valid when labeled qualitative. Record definitions for mixture fraction, equivalence ratio, mixing/ignition time, lift-off length, and heat-release metrics. Preserve the relationship among jet, pilot, droplet, ignition, and flame locations without converting proximity into causality.

## 18. Source Location

Record only confirmed page, section, figure, table, or equation identifiers. Never invent a locator. If a value is digitized from a plot, record the figure and method and mark the value `derived`; if localization is not verified, use `NV` and explain.

## 19. Missing Values

Use `NR` when the checked source does not report a relevant value, `NA` when the parameter does not apply, and `NV` when a candidate value or locator is unverified. Never use numeric zero, blank-space conventions, or an estimated physical property to represent missing information.

## 20. Conflicting Values

Preserve all source-supported values as separate contextual rows. Check condition, definition, unit, pressure basis, reference frame, location, time, and method. Do not choose a preferred value without evidence; flag unresolved conflicts for QC and later contradiction handling.

## 21. Tables/Figures

Transcribe exact tabulated values when unambiguous. Treat visually digitized figure values as `derived`, retain estimated uncertainty and tool/method notes, and avoid false precision. Equation outputs are `derived` unless the resulting number is explicitly reported. Preserve captions and footnote qualifications through concise notes.

## 22. Quality Control

Verify identity, tier, case/condition, controlled parameter name and group, value status, units, definition, source type/location, and extraction/verification status. Recalculate conversions and derived values independently. Confirm no unreported property was supplied, no incompatible definitions were merged, no locator was invented, and no missing code was misused before setting `verified`.

## 23. Stable Record IDs

Every parameter observation requires an immutable `parameter_record_id`. Assign the next unused paper-local number when a record is first created and never regenerate identifiers because of sorting, filtering, or export order. Preserve the existing ID when correcting metadata or adding relational links.

## 24. Contextual NPR Extraction

Retain the scalar NPR observation and create a linked `ratio_definitions.csv` record. Record numerator and denominator names, roles, thermodynamic pressure types, absolute/gauge reference types, spatial locations, time bases, component parameter IDs when present, formula, and source locator. Storage-, injector-internal-, nozzle-inlet-, stagnation-, total-, and ambient-pressure ratios are not equivalent.

If the source reports a time-dependent injector pressure, use a `time_history_registry.csv` record and `time_resolved` ratio time basis. Do not compress a history into a single plateau NPR unless the paper explicitly reports that quantity as a separate observation.

## 25. Transient Pressure and History Registration

Register every source-supported pressure, NPR, Mach-disk, mass, evaporation, velocity, temperature, or heat-release history. Mark whether data are tabulated, explicitly stated, figure-only, qualitative, formula-based, or unavailable. Figure-only histories are not digitized. `time_series_points.csv` accepts only explicitly tabulated or explicitly labelled points.

## 26. Mach Context and Reference Frame

Every core Mach record requires a physical context and reference frame. Keep incident-shock, post-shock freestream, local-jet, jet-exit, gas–droplet-relative, and detonation-front Mach numbers separate. Use `M_s` only for an explicitly defined shock-propagation Mach. If the frame cannot be verified, use `NV`; do not guess.

## 27. Mach-Disk State Handling

Every Mach-disk position, distance, diameter, formation-time, or motion record requires a state qualifier. Formation, growth, instantaneous position, excursion, oscillation, stabilization, stabilized position, quasi-steady position, and time-average are distinct. Link event and history records when the paper provides chronology or a trajectory.

## 28. Dimensionless-Number Components

Create a `dimensionless_definitions.csv` record for every core We/Re/Oh/Mach observation. For We, link velocity, density, length, and surface-tension parameter records. Re links velocity, density, length, and viscosity. Oh links liquid viscosity, density, length, and surface tension. When a component is required by the reported formula but not verified in the Pilot extraction, create an `NV` component record with `missing_reason`; never fill it from memory.

## 29. Event Chronology

Use typed events and signed offsets for SOI, EOI, ignition, flame transition, shock arrival/departure, expansion-wave arrival, Mach-disk formation/stabilization, breakup, evaporation, and detonation events. Preserve the reference event and sign. An absolute dwell without event direction is incomplete.

## 30. Loading-Duration Taxonomy

Use `intervals.csv` to separate shock-front passage, pressure pulse, shocked-state duration, post-shock aerodynamic exposure, expansion-wave-limited loading, total forcing, wave residence, injection duration, SOI separation, ignition delay, breakup, deformation, and evaporation intervals. Require typed start and end events. If a duration is not reported, store `NV` and explain which interval could not be verified.

## 31. Parameter Role and Model Inputs

Classify each parameter as an experimental control, boundary/initial/operating condition, material property, measured/model input, calibrated coefficient, measured/simulated output, derived metric, reported correlation, classification, descriptive state, or unknown. A model property or coefficient is not a measured material property merely because it has physical units.

## 32. Process and Mechanism Relations

Use `process_relations.csv` for source-supported process coupling and chronology. Use `pilot_mechanism_relations.csv` for claim-linked Pilot mechanism chains. Each edge requires a relation type, support type, source locator, and verification state. Use causal verbs only when supported; otherwise prefer `correlates_with` or `author_attributes_to`. Project inference remains explicitly labeled.

## 33. Interaction Geometry and Relative Momentum

Store interaction angle, axis angle, relative injection angle, overlap distance/description, geometry, and interaction region in dedicated records when explicitly reported. Do not calculate relative momentum from angle alone. A momentum ratio may be derived only from verified reported inputs and an approved formula; otherwise use `NR` or `NV` with rationale.

## 34. RDE Characteristic Scales

Store `L_E`, `L_D`, and other named scales as distinct parameter records. A reported ratio such as `Δ=L_E/L_D` requires a ratio record linked to both operands, including explicit `NV` operand records when standalone numeric values are unavailable. Do not flatten named physical scales into a generic dimensionless value.

## 35. Structured Provenance, Missing Rationale, and Sign Convention

Every reported parameter requires a nonblank `source_locator_id` that resolves to `source_locators.csv`; preserve the original `source_location` as `raw_locator`. Parse only unambiguous page, section, figure, table, equation, or appendix components. `NR`, `NA`, and `NV` require `missing_reason`. Direction-dependent fluxes and signed offsets require `sign_convention`; use `NV` when the source direction cannot be verified.

## 36. Migration Controls

Schema migration is additive. Preserve original values, units, definitions, locators, value status, and verification state. Do not generate derived values merely because the new schema can express a formula. Do not store project inference as reported numeric data. Validate unique identifiers, controlled vocabularies, missing rationales, structured provenance, and every foreign key before declaring migration complete.
