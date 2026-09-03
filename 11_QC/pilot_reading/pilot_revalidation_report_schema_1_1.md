# Pilot Re-validation Report — Schema 1.1

## Result

**READY with source-limited unknowns.** All 12 Pilot papers migrated successfully; no schema blocker remains. `PASS_WITH_LIMITATION` below means the schema is adequate but the source does not provide every desired numeric component.

| Validation question | Result | Basis |
|---|---|---|
| 1. Can steady NPR be stored without losing its definition? | PASS | Ratio operands, pressure basis, context, and provenance are explicit. |
| 2. Can transient injector pressure and NPR history be represented? | PASS_WITH_LIMITATION | Histories and temporal basis are modeled; no source-unverified time-series points were digitized. |
| 3. Can Mach and shock Mach number be distinguished? | PASS_WITH_LIMITATION | Quantity context and frame are explicit; unstated frames remain `NV`. |
| 4. Can Mach-disk formation and state be represented? | PASS | State, position, and chronology are separable. |
| 5. Can We, Re, and Oh definitions be audited? | PASS_WITH_LIMITATION | Reference components are linked; unreported components remain explicit unknowns. |
| 6. Can loading duration be represented without mixing definitions? | PASS_WITH_LIMITATION | Typed intervals and endpoints are explicit; some durations are not numerically reported. |
| 7. Can shock geometry and curvature context be preserved? | PASS | Geometry is independent of Mach and uses explicit categorical context. |
| 8. Can phase change and breakup coupling be represented? | PASS | Events, intervals, and supported process relations are available. |
| 9. Can mixing, ignition, and detonation chronology be represented? | PASS | Event types, references, offsets, and process relations preserve order and support type. |
| 10. Can RDE characteristic scales and ratios be represented? | PASS_WITH_LIMITATION | Named scales and linked operands are available; some standalone operand values remain `NV`. |
| 11. Is claim-to-source provenance machine-auditable? | PASS | Source-locator identifiers are unique and foreign keys resolve. |

## Per-Paper Migration Status

| Paper ID | Migration | Parameter reconciliation | Foreign keys | Blocking issue |
|---|---|---|---|---|
| A016 | PASS | PASS | PASS | None |
| A020 | PASS | PASS | PASS | None |
| A022 | PASS | PASS | PASS | None |
| B011 | PASS | PASS | PASS | None |
| B013 | PASS | PASS | PASS | None |
| B029 | PASS | PASS | PASS | None |
| C014 | PASS | PASS | PASS | None |
| C016 | PASS | PASS | PASS | None |
| C031 | PASS | PASS | PASS | None |
| D003 | PASS | PASS | PASS | None |
| D009 | PASS | PASS | PASS | None |
| D017 | PASS | PASS | PASS | None |

## Gate Decision

The Schema 1.1 Pilot readiness gate passes. Phase 7 remains unstarted and requires a separate explicit instruction.
