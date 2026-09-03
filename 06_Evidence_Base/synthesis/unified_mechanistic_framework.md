# Unified Mechanistic Framework

## 1. Framework Scope

This framework converts the 53 frozen Phase 10 Global Claims into an evidence-weighted physical architecture. It is a synthesis layer, not manuscript prose and not a claim that the full HPDI shock–droplet chain has been observed. Each retained arrow is classified in `mechanism_pathways.csv` as direct, mixed/indirect, cross-scale inference, or evidence gap. Application distance is kept explicit.

The principal chain is:

```text
injection boundary and chronology
→ injector pressure build-up / valve state
→ transient underexpanded-jet state
→ Mach-disk and shock-cell topology
→ local gas pressure / density / velocity state
→ loading magnitude and duration
→ droplet nondimensional response state
→ deformation and instability competition
→ secondary breakup
→ fragment state and transport
→ phase change / evaporation
→ mixture redistribution
→ ignition and combustion response
```

The chain is well supported in components but is not closed end-to-end under a common HPDI condition. The main discontinuities are M03, M08, and M11.

## 2. Injection Boundary Conditions

The upstream state is not a single pressure. It comprises time-resolved injector or supply pressure, valve-opening state, ambient/chamber pressure, nozzle geometry, gas species and thermodynamic state, and injection chronology. NPR is usable only when numerator and denominator pressure roles, pressure types, locations, and time bases are compatible (GC-0006, GC-0007, GC-0009, GC-0010).

Direct support is strongest for the proposition that pressure build-up and opening history create a developing stage before a quasi-steady stage. In HPDI/H2DDI, pilot/main timing and overlap are independently well supported as mixture and ignition controls (GC-0001, GC-0002), but this does not itself show a shock-mediated droplet mechanism.

## 3. Transient Underexpanded-Jet Development

The underexpanded-jet state evolves during injector opening. Formation, instantaneous position, overshoot, and stabilized behavior must be treated as different observables (GC-0007). Compatible pressure ratio, nozzle, ambient, and gas conditions govern momentum, penetration, lateral growth, entrainment, and shock development, but these responses are not universally monotonic across geometries or transient stages (GC-0008 to GC-0011).

Evidence status: direct and strong within gas-jet studies; moderate at the HPDI application boundary because engine-local transient gas states are less completely resolved.

## 4. Shock Structure and Local Loading

Mach-disk position and motion are the best-constrained shock-structure observables. Shock-cell spacing, Mach-disk diameter/curvature, appearance threshold, and potential-core length are less consistently defined or measured (GC-0015). The shock-dominated near field and weaker-shock far-mixing region should remain separate, and any notional-nozzle initialization requires a validated placement and decay assumption (GC-0012).

Shock topology can generate local pressure, density, velocity, and vorticity changes. Canonical shock-droplet and spray-shock studies show that such changes can load droplets or sprays (GC-0020, GC-0036, GC-0037). However, the corpus contains no co-located, time-resolved HPDI measurement that maps a gas-jet Mach disk or shock cell to the pressure/velocity history experienced by pilot droplets (GC-0052). Thus:

```text
B: underexpanded-jet topology → local gas-state variation        supported
C: specified gas-state jump → canonical droplet loading          supported
B/C → A: topology → actual HPDI pilot loading                     not validated
```

The last arrow is the central M03/M11 evidence gap, not an implied conclusion.

## 5. Loading-to-Droplet Response

Droplet loading requires both magnitude and history. Magnitude includes pressure jump, density change, local gas–droplet relative velocity, and spatial nonuniformity. History requires a typed interval: shock-front passage, shocked-state exposure, expansion-wave-limited loading, or total forcing. These intervals cannot be substituted for each other (GC-0016).

The comparison-ready response state is multivariable: Mach context, Weber number with explicit velocity/density/length/surface-tension references, Reynolds number, Ohnesorge number, density ratio, droplet size, liquid/thermal state, and loading duration. Comparable Weber number alone does not guarantee comparable morphology or timing (GC-0017, GC-0018).

`tau_loading / tau_response` is retained only as a candidate project metric. It is physically motivated by finite-duration evidence but is not literature-established and is not added to Parameter Master.

## 6. Deformation and Secondary Breakup

Definition-complete loading directly supports deformation in isolated and ordered droplets. Internal shock transmission, refraction, focusing, pressure extrema, and circulation can imprint later deformation, but their relevance depends on wave-speed ratio, phase state, geometry, and omitted physics (GC-0020).

Secondary breakup emerges from competing RT, KH/shear, capillary-retraction, sheet-rupture, wake, and ligament processes rather than a Weber-only taxonomy (GC-0019, GC-0021). Strong evidence supports the deformation/instability-to-breakup segment within canonical conditions. Critical Weber values are condition- and definition-specific observed ranges unless the source or cross-paper evidence establishes a mechanistic boundary. Broad taxonomy retains the explicit missing-C004 limitation.

## 7. Fragment Transport and Collective Effects

Breakup creates evolving fragment-size, velocity, spacing, and mass distributions (GC-0023). These products, rather than a breakup label alone, govern cloud transport and provide the initial state for evaporation. The evidence is direct but diagnostically sparse, so M06 remains moderate.

Multidroplet evidence adds mechanisms absent from an isolated-droplet picture. Tandem wake shielding, parallel squeeze flow/channel closure, and cloud-scale shock attenuation are directly supported (GC-0022, GC-0028). Arrangement matters: tandem and parallel systems cannot share a universal critical spacing. Dilute-cloud attenuation and ordered-droplet behavior demonstrate why collective corrections are needed, but they do not quantitatively validate a dense, disordered, polydisperse, evaporating, reacting HPDI spray.

## 8. Phase Change and Evaporation

Breakup and evaporation can overlap for small droplets or strong-wave conditions (GC-0024). The interaction direction is not universal. Vapor layers and Stefan flow can reduce interfacial shear and oppose deformation, whereas heating-induced surface-tension reduction can promote breakup in other conditions (GC-0025, GC-0026). Experiments on tested droplets above 100 micrometres found negligible evaporation influence on deformation over the observation interval, which does not extend to smaller droplets or later phase-change stages (GC-0027).

The controlling boundary includes droplet/fragment size, liquid volatility and properties, gas temperature, density ratio, Stefan-related state, post-wave history, and the observation interval. The transition between phase-change-suppressed and thermally promoted breakup is not yet condition-matched.

## 9. Mixture Formation

Transport, dispersion, entrainment, evaporation, wall interaction, and injection geometry all contribute to mixture redistribution. Direct HPDI evidence strongly supports the role of injection chronology, overlap, and geometry in premixing and stratification (GC-0001, GC-0002, GC-0004). General atomization and evaporation physics supports a possible fragment-to-vapor-to-mixture bridge.

What is not supported is the isolated contribution of shock-generated pilot fragments to the actual HPDI mixture field. M08 is therefore limited. The framework keeps `general transport/evaporation → mixture redistribution` distinct from `shock-induced breakup/evaporation → measured HPDI mixture change`.

## 10. Ignition and Combustion Coupling

Mixture state and pilot-product interaction directly govern ignition timing, reaction-front development, heat-release mode, stability, and operating-point-dependent emissions (GC-0001 to GC-0004, GC-0038, GC-0040, GC-0041). Overlap can assist main-fuel ignition through reacting pilot products or disrupt/delay pilot ignition; chronology and geometry determine the direction (GC-0002).

This directly supported A-library chain is:

```text
injection chronology / geometry
→ premixing and pilot-product distribution
→ ignition behavior
→ combustion response
```

It does not establish the separate proposed chain:

```text
gas-jet shock
→ pilot breakup / evaporation
→ mixture change
→ ignition / combustion change
```

The latter remains an evidence gap (GC-0053).

## 11. RDE / Detonation Strong-Wave Analogues

RDE and detonation studies directly support strong-wave droplet deformation/breakup and show that droplet or evaporation scales relative to reaction/refill/wave scales can change unburned pockets, wave speed, multiplicity, stability, or extinction (GC-0032 to GC-0035). They also show why equal leading-shock Mach does not guarantee equal later droplet response: reacting post-wave velocity, sound speed, pressure gradient, chemistry, and loading duration differ from inert-shock conditions.

These studies provide strong-wave and characteristic-scale analogues. They do not prove HPDI behavior. `L_E/L_D` and related ratios are comparison candidates within their defined RDE systems; no validated mapping to HPDI injection/ignition scales exists.

## 12. Cross-Scale Transfer to HPDI

The transfer audit yields the following hierarchy:

- B → C: physically plausible qualitative bridge through local pressure, density, velocity, Mach context, and loading duration; not a closed universal formula.
- B → A: underexpanded-jet formation is partially validated at engine relevance, but topology-to-pilot-loading is not validated.
- C → A: isolated-droplet mechanisms provide foundations; dense-spray transfer is not validated.
- ordered/cloud C → A: analogue-only evidence demonstrates collective corrections that must be represented.
- C/D → A: overlapping breakup/evaporation scales are physically plausible, but the mixture/ignition consequence is not validated.
- D → A: detonation/RDE evidence is analogue-only.

Application directness must therefore be read with every pathway.

## 13. Directly Supported Mechanism Links

The strongest closed links are:

1. Compatible transient injector boundary → developing underexpanded-jet state → Mach-disk/shock-cell topology.
2. Definition-complete local loading state → canonical droplet deformation → instability-mediated secondary breakup.
3. HPDI injection chronology/overlap → mixture and pilot-product redistribution → ignition and combustion response.
4. Multidroplet/cloud arrangement → shielding, squeeze-flow/channel-closure, and shock-attenuation changes.

These closures are domain-bounded and should not be interpreted as one fully observed end-to-end chain.

## 14. Indirect / Cross-Scale Links

Indirect links include shock-cell topology to a droplet-specific loading history, fragment products to engine mixture fields, and strong-wave characteristic-scale evidence to HPDI. Each is physically motivated by supported component relations, but condition matching and application directness are incomplete.

## 15. Unclosed Mechanism Links

The highest-priority unclosed links are:

1. Underexpanded gas-jet shock topology → actual HPDI pilot-droplet local loading (KG-001).
2. Canonical isolated/ordered droplet response → dense polydisperse reacting pilot spray (KG-002).
3. Shock-induced breakup → evaporation → measured HPDI mixture redistribution → ignition/combustion change (KG-003).

Closing them requires synchronized, co-located shock/gas-state, droplet/fragment, species/mixture, and ignition/heat-release diagnostics or condition-matched validated simulation.

## 16. Synthesis Propositions

Eight propositions are retained in `synthesis_propositions.csv`:

- SP-001: transient injector boundary and chronology, not nominal pressure alone, define jet development.
- SP-002: shock topology is a plausible loading source, but HPDI pilot-loading mapping is unvalidated.
- SP-003: compressible droplet response requires a multivariable state beyond We alone.
- SP-004: collective effects bound isolated-droplet transfer to dense sprays.
- SP-005: breakup–phase-change coupling is directionally conditional.
- SP-006: direct timing/mixture/ignition evidence is distinct from the unclosed shock-mediated path.
- SP-007: RDE/detonation evidence is a bounded analogue.
- SP-008: fragment population state mediates transport, attenuation, and evaporation.

No proposition is labelled proven or universally true.

## 17. Highest-Priority Knowledge Gaps

The existing KG IDs are retained. High-priority integration centers on KG-001 through KG-005: gas-shock-to-pilot-loading closure, dense-spray transfer, continuous shock-to-ignition closure, NPR definition compatibility, and We/Mach/loading standardization. Medium-priority integration uses KG-006 through KG-009 for fragment products, conditional phase change, RDE scaling, and synchronized diagnostics. KG-010 remains a low-priority but explicit source-availability limitation associated with C004.

Uncertainty does not prevent Phase 12 planning because every open edge is explicitly classified and traceable. It must remain visible in future chapter and figure architecture.
