# Cross-Scale Parameter Schema

Schema version: 1.1  
Status: Pilot-validated revision  
Previous version: 1.0  
Migration source: Phase 6 Pilot

## 1. Purpose and Scope

Schema 1.1 preserves the heterogeneous, auditable, long-format parameter database established in version 1.0 and adds normalized relational structures for parameter context, time/event semantics, process relations, and machine-readable provenance. It resolves the structural gaps identified during the 12-paper Phase 6 Pilot without redefining or deleting the original observations.

The governing chain remains:

```text
injection and ambient conditions
→ jet and wave structure
→ local forcing and characteristic scales
→ droplet/spray response and phase change
→ transport, mixing, ignition, combustion, and detonation consequences
```

Equal symbols or equal numerical values are not assumed physically equivalent across papers.

## 2. Long-Format Parameter Master

`05_Data_Extraction/master_tables/parameter_master.csv` retains one paper × one case/context × one parameter observation per row. All version 1.0 fields remain. Version 1.1 adds:

```text
parameter_record_id
context_id
parameter_role
parameter_context
reference_frame
state_qualifier
event_id
interval_id
history_id
ratio_id
dimensionless_definition_id
process_relation_id
source_locator_id
sign_convention
missing_reason
schema_version
```

`parameter_record_id` is the immutable row key. Existing Pilot rows use `PAR-{paper_id}-{NNNN}` in their original per-paper row order. New rows receive later unused numbers and IDs are never regenerated because of sorting.

`context_id` is a stable paper-local context label derived from the preserved case and condition identifiers. It does not replace `case_id` or `condition_id`.

## 3. Parameter Roles

`parameter_role` distinguishes how a value functions in the source:

```text
experimental_control
boundary_condition
initial_condition
operating_condition
material_property
measured_input
model_input
calibrated_coefficient
measured_output
simulated_output
derived_metric
reported_correlation
classification
descriptive_state
unknown
```

Model inputs and calibrated coefficients must not be presented as experimentally measured physical properties. `derived_metric` requires `value_status=derived`; migration itself does not create derived numeric values.

## 4. Parameter Context and Reference Frame

`parameter_context` describes the physical object or process represented by a record. Allowed values are defined by parameter family in `parameter_dictionary.yaml`. Mach-family values include `incident_shock`, `post_shock_freestream`, `local_jet`, `jet_exit`, `relative_gas_droplet`, `droplet_relative`, `detonation_front`, `transmitted_shock`, `reflected_shock`, `other`, and `unknown`.

Frame-dependent values use:

```text
laboratory
shock_fixed
droplet_fixed
jet_axis
injector_fixed
wave_fixed
rotating_frame
other
unknown
NV
```

`NV` is used when the source context exists but the reference frame cannot be verified. A bare `Mach = X` without context is invalid for core extraction.

## 5. State Semantics

Mach-disk distance, diameter, position, and motion records use `state_qualifier`:

```text
formation
growth
instantaneous
motion
maximum_excursion
minimum_excursion
oscillation
stabilization
stabilized
quasi_steady
time_averaged
reported_unspecified
```

Formation, instantaneous position, excursion, motion, oscillation, and stabilized position are separate observations. A steady study is not automatically labeled `stabilized`; use the source-supported state.

## 6. Structured Provenance

`source_location` remains as the legacy human-readable locator. `source_locator_id` is the canonical machine-readable link to `source_locators.csv`:

```text
source_locator_id,paper_id,source_file,pdf_page,printed_page,section,subsection,figure,figure_panel,table,equation,appendix,raw_locator,locator_status,verification_status,notes
```

Safe parsing preserves the original locator in `raw_locator`. Unclear components remain blank; they are never guessed. `locator_status` is `complete`, `partial`, or `unparsed`. Structured locators use stable IDs `LOC-{paper_id}-{NNNN}`.

## 7. Contextual Ratios

NPR, `L_E/L_D`, S/D, and other defined ratios use `ratio_definitions.csv`. The required base header is:

```text
ratio_id,paper_id,case_id,condition_id,ratio_name,ratio_symbol,reported_ratio_value,normalized_ratio_value,value_status,numerator_parameter_record_id,numerator_name,numerator_role,numerator_type,numerator_location,numerator_time_basis,denominator_parameter_record_id,denominator_name,denominator_role,denominator_type,denominator_location,denominator_time_basis,ratio_definition,source_locator_id,verification_status,notes
```

Schema 1.1 additionally separates thermodynamic pressure type from gauge/absolute reference through:

```text
numerator_thermodynamic_pressure_type
numerator_pressure_reference_type
denominator_thermodynamic_pressure_type
denominator_pressure_reference_type
```

Pressure roles include `storage_pressure`, `rail_pressure`, `injector_internal_pressure`, `nozzle_inlet_pressure`, `stagnation_pressure`, `total_pressure`, `static_pressure`, `ambient_pressure`, `back_pressure`, `chamber_pressure`, `other`, and `unknown`.

NPR time bases include `instantaneous`, `initial`, `peak`, `storage_based`, `inlet_based`, `plateau`, `quasi_steady`, `time_averaged`, `time_resolved`, and `reported_unspecified`. A scalar NPR record remains preserved but is not considered comparison-ready without a linked contextual ratio definition.

## 8. Time Histories

`time_history_registry.csv` registers histories without digitizing plots:

```text
history_id,paper_id,case_id,condition_id,variable_name,variable_role,parameter_context,time_reference_event_id,history_type,data_availability,start_time,end_time,time_unit,source_locator_id,reported_or_derived,verification_status,notes
```

History types include pressure, NPR, Mach-disk position/diameter, velocity, temperature, mass, evaporation, heat release, and `other`. Data availability is one of `explicit_tabulated`, `explicit_text_values`, `figure_only`, `qualitative_only`, `formula_based`, or `not_available`.

`time_series_points.csv` is reserved for explicitly tabulated or explicitly labelled points. Figure-only curves are registered but not digitized.

## 9. Dimensionless Definitions

`dimensionless_definitions.csv` links each core We/Re/Oh/Mach record to its definition components:

```text
dimensionless_definition_id,paper_id,case_id,condition_id,parameter_record_id,dimensionless_name,symbol,formula_reported,definition_status,reference_velocity_parameter_id,reference_density_parameter_id,reference_length_parameter_id,reference_viscosity_parameter_id,reference_surface_tension_parameter_id,other_component_ids,parameter_context,reference_frame,source_locator_id,verification_status,notes
```

For breakup-relevant We, velocity, density, length, and surface-tension references must be linked when reported. Missing components are represented by explicit `NV` parameter records with `missing_reason`; they are not filled from model memory. `definition_status` may be `complete_reported`, `incomplete_reported`, `formula_only`, or `not_verified`.

Re and Oh use the same component-link architecture. A reported dimensionless value may be retained when its definition is incomplete, but it is not treated as definition-compatible for cross-paper comparison.

## 10. Events and Signed Chronology

`events.csv` stores typed events and signed offsets:

```text
event_id,paper_id,case_id,condition_id,event_type,event_label,event_domain,reported_time,reported_time_unit,normalized_time,normalized_time_unit,reference_event_id,signed_offset,offset_unit,event_status,source_locator_id,verification_status,notes
```

Event types cover SOI/EOI, ignition and flame transition, shock and pressure-pulse events, Mach-disk formation/stabilization, breakup and evaporation events, detonation arrival, and `other`. A signed offset preserves event direction; `-0.4 ms` and `+0.4 ms` are not equivalent.

## 11. Intervals and Loading Duration

`intervals.csv` stores typed intervals:

```text
interval_id,paper_id,case_id,condition_id,interval_type,start_event_id,end_event_id,reported_duration,reported_unit,normalized_duration,normalized_unit,value_status,definition,source_locator_id,verification_status,notes
```

Allowed interval types include `shock_front_passage`, `pressure_pulse`, `shocked_state`, `post_shock_aerodynamic_exposure`, `expansion_wave_limited_loading`, `total_forcing`, `wave_residence`, `injection_duration`, `SOI_separation`, `ignition_delay`, `deformation_interval`, `breakup_interval`, `evaporation_interval`, and `other_reported`.

Intervals with different physical endpoints are never merged merely because they share a duration. A source-unreported duration is stored as `NV` with an explicit reason.

## 12. Process Relations

`process_relations.csv` represents coupling and chronology between physical processes:

```text
process_relation_id,paper_id,case_id,condition_id,source_process,relation_type,target_process,support_type,source_locator_id,verification_status,notes
```

Relation types are `precedes`, `follows`, `promotes`, `suppresses`, `modifies`, `couples_with`, `concurrent_with`, `correlates_with`, `author_attributes_to`, and `other`. Causal verbs require source support. Support types are `direct_observation`, `simulation_resolved`, `experimental_correlation`, `model_based`, `author_interpretation`, and `project_inference`.

Pilot claim-level mechanism chains remain separate in `pilot_mechanism_relations.csv`; formal global evidence matrices are unchanged.

## 13. Interaction Geometry

Schema 1.1 supports `interaction_angle`, `jet_axis_angle`, `relative_injection_angle`, `jet_overlap_description`, `overlap_start_distance`, `interaction_geometry`, and `interaction_region`. Explicit numeric values may be atomized from existing composite Pilot records while preserving the original row. Relative momentum is never calculated unless every required input and an approved formula are available; otherwise it is `NR` or `NV` with rationale.

## 14. Characteristic Scales

Named characteristic scales include `evaporation_length`, `detonation_characteristic_length`, `reaction_zone_length`, `refill_zone_length`, `wave_height`, `characteristic_response_length`, and `other_reported_characteristic_scale`. Ratios such as `Δ=L_E/L_D` must link explicit numerator and denominator parameter records, including `NV` operand records where the ratio is reported but standalone operand values are not verified.

## 15. Missing Values and Sign Conventions

`NR`, `NA`, and `NV` require `missing_reason`. Blank is not an acceptable substitute for a missing code. Numeric zero remains a valid reported value when the source explicitly reports zero and must never be treated as missing.

`sign_convention` is required when the meaning of mass flux, heat flux, interface flux, or signed relative timing depends on direction. Unverified direction is `NV`, not an assumed positive convention.

## 16. Shock Curvature

The version 1.0 geometry architecture is retained. Planar, cylindrical, spherical, divergent, curved-local, and unknown wave geometries remain separate from Mach context. Planar geometry is not encoded as numeric zero curvature unless the paper or an explicitly approved project convention defines it that way.

## 17. Foreign-Key Integrity

All populated foreign keys must resolve to their corresponding table:

```text
parameter_record_id → parameter_master.csv
source_locator_id → source_locators.csv
event_id/reference_event_id → events.csv
interval_id → intervals.csv
history_id → time_history_registry.csv
ratio_id → ratio_definitions.csv
dimensionless_definition_id → dimensionless_definitions.csv
process_relation_id → process_relations.csv
mechanism_relation_id → pilot_mechanism_relations.csv
```

Orphan keys are errors. Semantic uncertainty is retained as `needs_review` or an explicit missing code rather than being silently deleted.

## 18. Backward Compatibility and Migration

Migration is additive:

- all 286 Phase 6 parameter observations remain;
- reported values, units, definitions, and legacy source locations are preserved;
- no migration-generated numeric value is marked `derived` or `reported`;
- new atomic records are limited to source-explicit components or explicit missing-component records;
- 12 per-paper JSON files retain all version 1.0 keys and add version 1.1 relational arrays;
- original Pilot notes, evidence-card prose, global evidence matrices, Paper IDs, reading tiers, and raw PDFs remain unchanged.

## 19. Readiness Gate

Tier 1 bulk processing is ready only when critical gaps are resolved or resolved by a machine-executable convention; blocking high gaps are zero; all Pilot migrations pass; no observation is lost; identifiers and foreign keys are unique; provenance and missing rationales validate; and the ten Pilot core questions pass or pass with source-only limitations.
