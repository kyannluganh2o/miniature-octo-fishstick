# Pilot Scientific Reading Validation Report

## 1. Pilot Scope

Phase 6 processed exactly the 12 user-designated Tier 1 Pilot papers in batches P1–P3. All scientific extraction used the local canonical PDFs. No web lookup, figure digitization, non-Pilot processing, global evidence-matrix update, or manuscript drafting was performed.

## 2. Papers Processed

- P1: B011, C014, C016, D003
- P2: B013, B029, C031, D017
- P3: A020, A022, A016, D009

## 3. Processing Success

- PDF identity/readability confirmed: 12/12
- Machine-readable full text and page maps: 12/12
- Standard 23-section paper notes: 12/12
- Per-paper extraction JSON: 12/12
- Pilot evidence cards: 12/12
- Reading self-QC passed: 12/12
- Extraction status: 6 complete, 6 partial
- Needs review / failed: 0 / 0

The six partial records are D003, B013, B029, C031, D017, and A022. Their Pilot-role questions were answered, but important definitions, graphical time histories, model-input semantics, or missing-schema fields prevent a fully normalized extraction.

## 4. Parameter-Schema Coverage

The long-format parameter master contains 286 Pilot rows: 281 reported, 4 NA, 1 NR, 0 derived, and 0 inferred numeric records. Case IDs retain changes in NPR, Mach, droplet size, injection timing, angle, oxygen level, phase-change state, and detonation condition. No figure curves were digitized.

## 5. NPR Findings

B011 explicitly defines NPR as upstream/nozzle total pressure divided by ambient static pressure. B013 reports a storage-pressure-based NPR while also specifying a lower sonic-inlet pressure. B029 defines NPR from time-dependent injector-internal pressure and background pressure. A single scalar NPR field therefore cannot safely preserve all three contexts.

Assessment: **NEEDS REVISION**. Required additions are pressure role, spatial location, pressure type, numerator/denominator source, and time basis.

## 6. Mach / M_s Definition Findings

C014 uses post-shock freestream Mach, C016 uses incident-shock Mach, C031 varies incident-shock Mach, B011/B013 report jet/local Mach, and D017 concerns a detonation front. These are not interchangeable.

Assessment: **NEEDS REVISION**. Every Mach record needs a required context and reference frame.

## 7. Mach Disk and Shock-Cell Findings

B011 provides quasi-steady geometry at fixed NPR. B013 separates formation near 20 μs from later position/oscillation near 3.8 mm. B029 links turning/stable behavior to injector pressure history. Current time/stage fields are useful but do not enforce formation, motion, maximum excursion, and stabilization as separate states.

Assessment: **NEEDS REVISION**.

## 8. Weber/Reynolds/Ohnesorge Definition Findings

C014, C016, C031, and D017 define We using post-shock gas density and a post-shock or droplet-relative velocity, but their Mach contexts and forcing histories differ. C014 and C016 also demonstrate that breakup mode is not safely organized by scalar We alone. Reference velocity, density, length, and surface tension must be mandatory linked fields for core We records.

Assessment: **NEEDS REVISION**.

## 9. S/D Findings

No Pilot paper reports a core multi-droplet S/D case. The existing rule requiring S, D, arrangement, and direction remains appropriate, but this field was not empirically stress-tested by the selected Pilot corpus.

Assessment: no change demonstrated by this Pilot; retain as an untested item for later validation.

## 10. Shock Curvature Findings

The corpus includes planar incident shocks, jet-induced divergent/compression waves, underexpanded-jet shock structures, and detonation fronts. The existing geometry vocabulary and rule against encoding planar curvature as numeric zero can represent the observed cases without inventing curvature.

Assessment: **PASS**, provided wave geometry remains distinct from Mach context and no unreported numeric curvature is derived.

## 11. Loading Duration Findings

D003 shows that shock-front passage, pressure/shocked-state pulse, expansion-wave termination, post-wave exposure, and the total forcing interval are physically different. A single loading-duration scalar is ambiguous.

Assessment: **NEEDS REVISION**. Split loading intervals and require start/end event definitions.

## 12. Time-Scale Findings

The Pilot requires event-relative timing across several domains: Mach-disk formation and stabilization, shock exposure and droplet response, aerodynamic nondimensional time, injection SOI/EOI chronology, ignition delay, evaporation distance/time, and RDE refill-zone scales. `time_or_stage` is useful but insufficient without typed event relationships and signed reference-event semantics.

## 13. Phase-Change Schema Findings

C031 supplies real-fluid model inputs, manually selected Hertz–Knudsen coefficients, interface mass flux, and simulation outputs. D017 combines measured survival/cloud morphology with reduced breakup–evaporation models. These need parameter-role and process-coupling fields so model inputs are not mistaken for measured properties and concurrent breakup/phase change remains reconstructable.

Assessment: **NEEDS REVISION**.

## 14. Mixing/Ignition Schema Findings

A020 and A022 require explicit event chronology and geometry/overlap context. A016 adds a linked mechanism chain from vortex entrainment through heat/OH transport to methane ignition and combustion response. Independent scalar rows cannot preserve the evidential support of each link.

Assessment: **NEEDS REVISION**.

## 15. RDE/Detonation Schema Findings

D009 defines `Δ = L_E/L_D`, with numerator and denominator carrying distinct physical meanings. The ratio organizes the paper's stability criterion and cannot be stored safely as an unlabeled generic dimensionless number.

Assessment: **NEEDS REVISION**. Add named characteristic scales and explicit ratio operands.

## 16. Provenance and Source-Location Quality

Every Pilot parameter has a local-PDF source location, source type, and verification state. Free-text locators are human-readable but do not separately encode PDF page, printed page, section, figure, table, or equation, limiting future automated citation audit.

Assessment: **NEEDS REVISION**.

## 17. Critical Schema Gaps

Five critical gaps were recorded:

1. G001 — contextual/composite NPR pressure roles.
2. G002 — Mach-disk state and observation-time semantics.
3. G003 — time-dependent injector pressure and NPR histories.
4. G005 — mandatory We reference-scale records.
5. G007 — split loading-duration taxonomy.

The full log contains 17 proposed gaps: 5 critical, 9 high, 2 medium, and 1 low.

## 18. Proposed Schema Changes

### Critical before bulk processing

- Represent NPR as a contextual pressure-ratio record with roles, types, locations, and time basis.
- Add Mach-disk state qualifiers for formation, growth, motion, excursion, and stabilization.
- Add time-series/history references for injector pressure and transient NPR.
- Require We reference velocity, density, length, and surface tension.
- Split loading duration into typed intervals with explicit start/end events.

### Recommended before bulk processing

- Require Mach context/reference frame.
- Add parameter-role and phase-change/breakup process links.
- Add event/reference-event chronology for injection and ignition.
- Add mechanism-chain records with support type.
- Add RDE characteristic-scale operands and structured source locators.

### Optional

- Add mass-flux sign convention, dedicated interaction-angle/overlap fields, and required missing-value rationale.

### No change required

- Preserve the existing long-format master-table model.
- Preserve reported/derived/inferred and NR/NA/NV controls.
- Preserve the current no-unreported-curvature rule.

## 19. Readiness for Tier 1 Bulk Processing

**NOT READY.** The five critical gaps above should be reviewed and either incorporated into Parameter Schema 1.1 or explicitly resolved by an approved extraction convention before Tier 1 bulk processing. This Pilot report proposes changes only; no formal schema file was modified.
