# Phase 10 Global Evidence Consolidation Report

## Outcome

Phase 10 Global Evidence Consolidation is complete. The evidence base now operates at claim, mechanism, condition, contradiction, coverage, and knowledge-gap level. No chapter or manuscript prose was created.

## Evidence Scale

- Candidate claims inventoried: 239
- Pilot / Tier 1 / Tier 2 / Tier 3: 24 / 46 / 131 / 38
- Retained for active consolidation: 181
- Inventory-only / non-retained: 58
- Normalized Global Claims: 53
- Claim-Evidence links: 189
- Unique supporting papers represented: 106
- Mechanism edges: 182
- Knowledge gaps: 10

### Candidate Distribution

- Mainline/library roles — A injection-to-combustion: 57; B underexpanded-jet/shock: 63; C droplet response/phase change: 75; D strong-wave/RDE application: 44
- Support types — author_interpretation: 87; direct: 13; direct_observation: 23; experimental_correlation: 18; indirect: 2; model_based: 56; project_inference: 3; review_secondary: 5; simulation_resolved: 32

## Claim Strength

- strong: 18
- moderate: 15
- limited: 20
- insufficient: 0
- contested: 0
- normalization_status = needs_scientific_review: 0

Evidence strength is assigned to the evidence-to-claim relationship and then consolidated. Review evidence remains secondary; Tier alone is not used as a grade.

## Mainline Coverage

- M01 high-pressure injection -> underexpanded-jet formation: **MODERATE** — Direct HPDI-resolved formation evidence is less complete than vessel/free-jet evidence.
- M02 underexpanded jet -> Mach disk / shock-cell structure: **STRONG** — NPR definition, nozzle geometry, gas species, and transient state require explicit compatibility.
- M03 shock structure -> local pressure / velocity loading: **LIMITED** — No direct time-resolved mapping from an HPDI gas-jet shock field to pilot-spray droplet loading.
- M04 local loading -> droplet deformation: **STRONG** — Most evidence concerns isolated or ordered droplets rather than dense pilot sprays.
- M05 deformation / instability -> secondary breakup: **STRONG** — Regime boundaries depend on We/Mach/loading definitions; C004 remains missing.
- M06 breakup -> fragment transport / dispersion: **MODERATE** — Fragment distributions, cloud transport, and dense-spray interactions are not uniformly measured.
- M07 breakup / thermal loading -> evaporation / phase change: **MODERATE** — Heating, Stefan flow, volatility, and size can reverse the apparent phase-change effect on breakup.
- M08 transport / evaporation -> mixture formation: **LIMITED** — The shock-breakup/evaporation contribution to actual HPDI mixture fields is not directly isolated.
- M09 mixture formation -> ignition / combustion: **MODERATE** — Injection chronology is well supported, but the upstream shock-droplet causal path is not closed.
- M10 droplet response <-> detonation / RDE wave behavior: **MODERATE** — Mostly numerical and application-scale; chemistry, geometry, and characteristic scales vary.
- M11 canonical shock-droplet physics -> HPDI application transfer: **INDIRECT_ONLY** — No direct HPDI experiment closes shock structure -> pilot loading -> breakup -> ignition.

Strongly covered segments: 3; moderately covered: 5; limited or indirect-only: 3; missing: 0.

## Top Strong Global Claims

- GC-0001 — Within the tested pilot-ignited direct-injection configurations, relative pilot/main timing and main-fuel injection timing set the achieved premixing and shift combustion between mixing-controlled and premixed regimes, with operating-point-dependent stability and emissions tradeoffs. Primary evidence: 10; condition domain: HPDI/H2DDI engine, vessel, and validated-model conditions.
- GC-0002 — Pilot/main jet overlap and dwell can accelerate main-fuel ignition through interaction with reacting pilot products while delaying or suppressing pilot ignition when the interaction disrupts the pilot; the direction therefore depends on chronology and geometry. Primary evidence: 9; condition domain: pilot-ignited gaseous direct injection.
- GC-0007 — Injector pressure build-up and valve-opening history drive a developing underexpanded-jet stage before a stable or quasi-steady stage; formation, instantaneous, overshoot, and stabilized shock positions are distinct observables. Primary evidence: 8; condition domain: transient high-pressure gas injection.
- GC-0009 — Pressure ratio strongly influences underexpanded-jet momentum, penetration, volume, and entrainment, but penetration and entrainment need not vary monotonically across nozzle geometries or transient states. Primary evidence: 7; condition domain: transient and quasi-steady underexpanded gas jets.
- GC-0022 — Neighboring droplets alter shock-driven breakup through wake shielding, squeeze flow, and channel closure; spacing effects depend on tandem versus parallel geometry and Weber number. Primary evidence: 6; condition domain: ordered multi-droplet shock interaction.
- GC-0036 — Spray-generated shocks depend on nozzle-exit velocity, injection-rate ramp, ambient sound speed and density, and injection timing; when present they can change spray penetration and angle, but typical hot dense engine conditions may suppress their formation. Primary evidence: 6; condition domain: high-pressure diesel spray and vessel/engine-relevant conditions.
- GC-0003 — Higher gaseous-fuel injection pressure generally intensifies post-ignition mixing and can shorten mixing-controlled combustion at higher load, while ignition sensitivity and emissions or pressure-rise penalties remain operating-point dependent. Primary evidence: 5; condition domain: pilot-ignited natural-gas engine conditions.
- GC-0028 — Shock propagation through a dilute droplet cloud is attenuated by exchange area, volume fraction, droplet size, shock strength, and breakup; neglecting fragmentation can overpredict transmitted pressure. Primary evidence: 5; condition domain: planar shock interaction with dilute droplet clouds.
- GC-0017 — Droplet deformation and breakup timing or morphology depend jointly on aerodynamic loading, droplet size, and Mach context; comparable Weber number alone does not ensure comparable response. Primary evidence: 4; condition domain: post-shock and supersonic-flow droplet loading.
- GC-0034 — Under detonation-wave loading, smaller droplets and stronger waves accelerate instability and breakup, while liquid properties and the transition from stripping to coupled KHI-RTI piercing alter the collapsed breakup time. Primary evidence: 4; condition domain: water and hydrocarbon droplets under detonation waves.

## Weak or Indirect Mechanism Connections

- M03: underexpanded-jet shock structure -> actual HPDI pilot-spray local loading remains limited.
- M08: breakup/evaporation and fragment transport -> actual HPDI mixture formation remains limited.
- M11: canonical shock-droplet physics -> HPDI application transfer is indirect-only.
- The full shock -> breakup -> evaporation -> mixture -> ignition chain is not directly closed by one condition-matched source.

## Mechanism Architecture

- Directly supported source edges: 76
- Indirectly supported source edges: 102
- Cross-scale inference edges: 1
- Explicit non-retained evidence-gap edges: 3

The project mainline is not treated as proof. Cross-scale and evidence-gap edges remain explicitly labelled.

## Contradiction Adjudication

- True unresolved contradictions: 0
- Apparent condition differences: 4
- Apparent definition differences: 2
- Different physical stage: 2
- Method-dependent differences: 0
- Scale-dependent differences: 1
- Complementary, not contradictory: 1
- Insufficient comparability: 0

No true unresolved contradiction was promoted from differences that can be explained by definition, condition, physical stage, method, or scale.

## Priority Knowledge Gaps

- **HIGH — KG-001 (M03;M11)**: Direct spatially and temporally resolved evidence linking underexpanded gas-jet shock structure to actual pilot-spray droplet loading in HPDI is absent. Current evidence: Component relations are supported in underexpanded-jet and canonical shock-droplet studies, but the transfer edge is indirect. Missing: Co-located gas pressure/velocity/shock diagnostics and pilot-droplet response under HPDI-relevant timing and geometry. Why it matters: This is the central unclosed arrow between gas-jet physics and pilot-droplet breakup.
- **HIGH — KG-002 (M04;M05;M11)**: Transfer from isolated or ordered canonical droplets to dense, polydisperse, reacting HPDI pilot sprays is not validated. Current evidence: Canonical deformation and breakup mechanisms are strong; application directness is low. Missing: Dense-spray experiments or validated simulations with realistic HPDI pilot size distributions, spacing, turbulence, and reacting ambient state. Why it matters: Single-droplet mechanisms may change through shielding, collective shock attenuation, and phase change.
- **HIGH — KG-003 (M07;M08;M09;M11)**: The continuous chain shock-induced breakup -> evaporation -> mixture formation -> HPDI ignition is supported mainly by cross-domain stitching rather than a direct experiment. Current evidence: Breakup/evaporation coupling and mixture-controlled ignition each have evidence, but their causal connection is not directly measured. Missing: A single condition-matched study resolving shock loading, fragment/evaporation evolution, mixture field, and ignition response. Why it matters: Without the link, claimed ignition benefits of shock-enhanced atomization remain a hypothesis.
- **HIGH — KG-004 (M01;M02;M03)**: NPR comparisons remain vulnerable to incompatible numerator roles, pressure reference types, and transient versus quasi-steady time bases. Current evidence: Schema 1.1 records ratio roles and histories, but many source claims remain only partially comparison-ready. Missing: Uniform reporting of storage/nozzle-inlet/stagnation pressure, ambient pressure, gauge/absolute basis, and time history. Why it matters: Definition mismatch can create false scaling agreement or disagreement.
- **HIGH — KG-005 (M04;M05)**: Weber and Mach definitions, reference frames, and loading intervals are not standardized across shock-droplet studies. Current evidence: Several claims explicitly show comparable We does not ensure comparable morphology. Missing: Condition sets reporting every We/Re/Oh/Mach component and typed loading duration. Why it matters: Uncontrolled definitions obscure regime boundaries and cross-paper contradictions.
- **MEDIUM — KG-006 (M06)**: Fragment-size, velocity, spacing, and cloud-transport statistics are sparse under finite shock loading. Current evidence: Selected studies report fragment PDFs, mist images, or cloud extent, but coverage is not systematic. Missing: Time-resolved, uncertainty-qualified fragment distributions and velocities across We, Mach, size, and droplet population. Why it matters: Transport and evaporation models require product distributions, not only regime labels.
- **MEDIUM — KG-007 (M07)**: Phase change can suppress or promote deformation depending on thermal and interfacial conditions, but the transition boundary is poorly constrained. Current evidence: Model and experimental results cover separated droplet-size, Stefan-number, volatility, and temperature domains. Missing: Matched-condition studies separating vapor-layer shear reduction from thermal property changes. Why it matters: The sign of breakup-evaporation coupling cannot be generalized without this boundary.
- **MEDIUM — KG-008 (M10)**: RDE/detonation evidence strongly demonstrates characteristic-scale sensitivity but remains weakly transferable to HPDI engines. Current evidence: Droplet size and evaporation scales control wave stability in strong-wave applications. Missing: A validated nondimensional mapping between RDE characteristic scales and engine injection/ignition scales. Why it matters: Strong-wave analogues should inform, not substitute for, HPDI evidence.
- **MEDIUM — KG-009 (M08;M09)**: Realistic multispecies, high-speed diagnostics and validated high-fidelity models remain insufficient under engine pressure, swirl, wall, and turbulence conditions. Current evidence: Timing/overlap effects are well represented, but local radicals, mixture fields, and transient shocks are rarely measured together. Missing: Synchronized species, velocity, pressure/shock, droplet, and heat-release diagnostics with quantified model validation. Why it matters: Current mechanism attribution often relies on correlations or model-resolved fields.
- **LOW — KG-010 (M04;M05;M06)**: The missing Tier 1 source C004 limits broad review-level coverage of Newtonian and viscoelastic aerobreakup taxonomy. Current evidence: The remaining 114-paper corpus contains strong Newtonian shock-droplet evidence but cannot verify C004 locally. Missing: The original local PDF for C004 / C-F-04; no abstract or secondary reconstruction is used. Why it matters: Broad taxonomy claims should retain an explicit source-availability limitation.

## Source Limitation

C004 / C-F-04 remains the only missing PDF. No online text, abstract substitute, or review-based reconstruction was used. Broad aerobreakup-regime claims carry the limitation `missing Tier 1 source C004` where applicable.

## Minimal Integrity Check

1. Active Global Claims without source-linked evidence or explicit insufficiency: 0.
2. Missing source locators in active evidence: 0.
3. Orphan Claim-Evidence links: 0.
4. Retained mechanism edges without an evidence source: 0.
5. True contradictions lacking condition/definition compatibility: 0.
6. Knowledge gaps without a coverage-segment reference: 0.
7. Existing Paper IDs changed: 0; reading tiers changed: 0; Parameter Schema changed: NO.
8. C004 status: missing.

## Phase 11 Readiness

Global Claims, Claim-Evidence Matrix, Mechanism Matrix, Coverage Map, contradiction adjudication, and knowledge-gap mapping are populated. Low-confidence normalization items are isolated and do not define an otherwise uncovered core mechanism segment.

**Readiness for Phase 11 Cross-Paper Mechanistic Synthesis: READY**
