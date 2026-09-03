# Phase 11 Cross-Paper Mechanistic Synthesis Report

## Outcome

Phase 11 is complete. The frozen Phase 10 Global Claims, Claim–Evidence Matrix, mechanism edges, coverage segments, contradiction adjudications, and knowledge gaps have been consolidated into a traceable scientific synthesis architecture. No Phase 10 claim was renumbered or scientifically rewritten, and no chapter, figure, or manuscript content was created.

## Synthesis Scale

- Mechanism nodes: 22
- Mechanism pathways: 34
- Directly supported pathways: 17
- Indirect/mixed pathways: 12
- Cross-scale-inference pathways: 2
- Evidence-gap pathways: 3
- Cross-scale transfer relations assessed: 9
- Synthesis propositions: 8

Pathway counts classify `direct` separately, combine `mixed` and `indirect` as indirectly supported for the progress summary, and retain cross-scale inference and evidence gap as separate states.

## Cross-Scale Transfer Status

- Directly validated: 0
- Partially validated: 2
- Physically plausible or analogue-only: 4
- Not validated: 3

The two partially validated transfers are B gas-jet evidence to engine-relevant underexpanded-jet formation and C inert-shock response to D detonation loading under controlled leading-wave comparison. Neither closes the B/C-to-A pilot-loading chain.

The four plausible/analogue relations are B → C local-state/loading mapping, ordered/cloud C → A collective corrections, D → A strong-wave analogy, and C/D → A small-droplet breakup/evaporation scale overlap. The three unvalidated transfers are underexpanded shock topology → HPDI pilot loading, isolated canonical droplets → dense HPDI spray, and breakup/phase change → measured HPDI mixture formation.

## Synthesis Proposition Status

- Established: 0
- Well-supported: 2
- Supported with boundaries: 3
- Cross-scale supported: 1
- Plausible but indirect: 2
- Unresolved: 0

`Established` was deliberately not assigned. The highest-confidence propositions remain condition-bounded rather than universal.

### Retained Propositions

- **SP-001 — well-supported:** Transient injector pressure build-up, valve opening, and chronology define the developing underexpanded-jet environment; a nominal pressure or steady NPR is insufficient. Main GCs: GC-0006, GC-0007, GC-0009, GC-0010, GC-0036. Cross-scale: no. Main limitation: direct HPDI-resolved formation evidence is less complete than vessel/free-jet evidence.
- **SP-002 — plausible but indirect:** Mach-disk/shock-cell topology is a physical source of transient gas-state variation, but its mapping to actual HPDI pilot loading is unvalidated. Main GCs: GC-0012, GC-0013, GC-0014, GC-0036, GC-0052. Cross-scale: yes. Main limitation: no co-located HPDI shock/gas-state/droplet measurement.
- **SP-003 — well-supported:** Compressible droplet response requires Mach context, typed loading duration, d0, liquid properties, and definition-complete We/Re/Oh rather than Weber number alone. Main GCs: GC-0016, GC-0017, GC-0018, GC-0020, GC-0021, GC-0030, GC-0034, GC-0039. Cross-scale: no. Main limitation: dimensionless definitions remain incomplete in many source condition sets.
- **SP-004 — cross-scale supported:** Collective mechanisms demonstrate why isolated-droplet physics requires shielding, spacing, attenuation, and population corrections before transfer to dense HPDI sprays. Main GCs: GC-0022, GC-0028, GC-0052. Cross-scale: yes. Main limitation: ordered/dilute systems are not direct dense reacting-spray validation.
- **SP-005 — supported with boundaries:** Breakup–phase-change coupling can suppress or promote deformation depending on size, volatility, Stefan/vapor-layer effects, thermal property change, and forcing history. Main GCs: GC-0024 to GC-0027 and GC-0031. Cross-scale: no. Main limitation: the direction-change boundary lacks matched-condition evidence.
- **SP-006 — supported with boundaries:** Injection timing/overlap directly controls HPDI mixture and ignition/combustion response; shock-enhanced pilot-breakup contribution remains a separate unclosed inference. Main GCs: GC-0001 to GC-0004, GC-0038, GC-0040, GC-0041, GC-0053. Cross-scale: yes. Main limitation: no continuous shock-to-ignition measurement.
- **SP-007 — plausible but indirect:** RDE/detonation work supplies bounded strong-wave and characteristic-scale analogues, not substitute HPDI evidence. Main GCs: GC-0024, GC-0032 to GC-0035. Cross-scale: yes. Main limitation: no validated application-scale mapping.
- **SP-008 — supported with boundaries:** Fragment population state mediates transport, attenuation, and evaporation, but cannot be represented universally by a breakup label or single mean size. Main GCs: GC-0019, GC-0023, GC-0024, GC-0028, GC-0029. Cross-scale: no. Main limitation: fragment distributions and velocities are sparse.

## Mainline Mechanistic Status

| Segment | Mechanistic interpretation | Strength / directness | Application directness | Main variables | Main condition boundary | Main limitation |
|---|---|---|---|---|---|---|
| M01 | Pressure build-up, valve state, boundary conditions, and chronology establish a developing underexpanded jet. | moderate / mixed | engine-relevant | p_inj(t), contextual NPR(t), ambient state, nozzle, gas properties | pressure role/type and event alignment | incomplete direct HPDI-resolved formation |
| M02 | Compatible underexpanded state organizes Mach-disk and shock-cell topology. | strong / direct | canonical/vessel gas jet | NPR definition, x_MD/D, cell spacing, geometry, species | transient state and near/far field | dimensions beyond x_MD are less constrained |
| M03 | Shock topology produces local gas-state changes, but pilot-droplet loading is not mapped in HPDI. | limited / indirect | analogue before application | p(x,t), rho(x,t), u(x,t), jumps, duration | wave origin, location, frame, chronology | direct support ends before the B/C-to-A edge |
| M04 | Multivariable loading state and internal/collective mechanisms govern deformation. | strong / direct | canonical droplets | M_s, M_rel, We, Re, Oh, d0, duration, S/D | definition and population matching | dense reacting spray not validated |
| M05 | Deformation and RT/KH/shear/capillary competition produce secondary breakup. | strong / direct | canonical droplets | We, Mach context, Oh, d0, duration, breakup event | forcing history and taxonomy | no universal We boundary; C004 missing |
| M06 | Breakup products govern fragment transport and cloud response. | moderate / mixed | canonical/analogue | fragment PDF, velocity, spacing, volume fraction | time, detection, weighting, population | sparse product-state data |
| M07 | Breakup and evaporation overlap; thermal effects can reverse the apparent coupling. | moderate / mixed | selected canonical/RDE conditions | d0, fragment size, volatility, gas T, Stefan/density ratios | liquid/thermal/post-wave state | transition boundary not matched |
| M08 | Transport and evaporation contribute to mixture redistribution, but the shock-fragment contribution is not isolated in HPDI. | limited / indirect | engine-relevant but stitched | fragments, evaporation scale, timing, overlap, geometry | hot dense ambient, walls, turbulence | general physics is not direct mixture-field evidence |
| M09 | Mixture and pilot-product distribution directly govern ignition/combustion; shock-mediated upstream cause is open. | moderate / direct for timing | direct HPDI | DeltaSOI, ignition delay, overlap, temperature/oxygen | event definitions, fuel pair, load, geometry | shock-caused mixture-to-ignition arrow unmeasured |
| M10 | Droplet/evaporation scales couple to detonation/RDE waves; reacting post-wave history matters. | moderate / mixed | strong-wave application analogue | detonation Mach, post-wave state, d0, L_E/L_D | chemistry, geometry, wave number, scale definition | not directly transferable to HPDI |
| M11 | Canonical mechanisms form a basis, but the full HPDI application chain is not validated. | indirect-only / cross-scale | cross-domain only | definition-complete NPR/Mach/We, duration, size distribution, collective and phase-change descriptors | geometry, polydispersity, reaction state | no direct end-to-end HPDI experiment |

## Most Strongly Closed Mechanism Pathways

1. **MP-001/MP-003/MP-005:** injector pressure build-up and opening → transient underexpanded state → Mach-disk formation, motion, and stabilized location under compatible boundary definitions.
2. **MP-010/MP-012/MP-015/MP-016:** definition-complete loading state → deformation → instability competition → secondary breakup in canonical droplet conditions.
3. **MP-025/MP-026/MP-027:** HPDI injection chronology and overlap → mixture/pilot-product redistribution → ignition behavior → combustion response.

Collective shock attenuation (MP-014/MP-019) is also directly supported, but its transfer to dense HPDI spray is not closed.

## Most Important Unclosed Mechanism Pathways

1. **MP-033:** underexpanded-jet Mach-disk/shock-cell topology → actual local loading history of HPDI pilot droplets.
2. **MP-028:** shock-mediated breakup/evaporation → measured HPDI mixture-field redistribution.
3. **MP-029:** shock-caused mixture change → measurable HPDI ignition or combustion change.

MP-032, canonical single/ordered droplet response → dense polydisperse reacting HPDI spray, is the main scale-transfer limitation that cuts across all three.

## Parameter Synthesis

- Core comparison parameters/groups: 12
- High-priority supporting parameters/groups: 9
- Supporting/context parameters/groups: 4
- Entries requiring strict definition matching: 22
- Not recommended for direct cross-paper comparison: 4

The core set comprises p_inj(t), definition-complete NPR(t), Mach-disk x/D, incident-shock M_s, local M_rel, pressure jump, velocity jump/local relative velocity, typed loading duration, definition-complete We, droplet diameter/distribution, signed DeltaSOI, and typed L_E/L_D.

Direct comparison is recommended only after definition matching. Generic NPR, generic Mach, We without component references, and generic breakup time are explicitly not recommended. Re, Oh, density ratio, S/D/cloud descriptors, fragment distributions, evaporation scales, and ignition delay remain high-value when their phase, frame, event, and statistic definitions are complete.

One candidate synthesis metric, `tau_loading / tau_response`, is retained as a project hypothesis only. It is not literature-established, is not a universal group, and was not added to Parameter Master.

## Knowledge-Gap Integration

- High-priority KGs linked to synthesis: 5 (KG-001 to KG-005)
- Medium-priority KGs linked to synthesis: 4 (KG-006 to KG-009)
- Low-priority KGs linked to synthesis: 1 (KG-010)

The highest-impact gap cluster is KG-001/KG-002/KG-003: local shock-to-pilot loading, canonical-to-dense-spray transfer, and the continuous shock-to-mixture-to-ignition chain. KG-004/KG-005 define the comparison discipline needed to prevent false cross-paper scaling.

## Minimal Integrity Check

1. Unsupported active synthesis propositions: 0.
2. Unsupported retained pathways: 0; all retained pathways link to Phase 10 Global Claims, and three missing arrows are explicitly `evidence_gap`.
3. Orphan MN/MP/SP/GC/KG references in Phase 11 tables: 0.
4. Existing Global Claims remain 53 with existing IDs unchanged; Phase 10 evidence files were not scientifically rewritten.
5. Existing knowledge gaps remain KG-001 through KG-010 with IDs unchanged.
6. Parameter Schema remains version 1.1 and was not modified.
7. C004 remains the sole missing PDF.

## Phase 12 Readiness

The required synthesis propositions, mechanism pathways, transfer matrix, parameter bridge, boundary conditions, mainline map, parameter priorities, and unified framework are complete. The major uncertainties are explicit as indirect, analogue-only, cross-scale inference, or evidence gap, and do not prevent architecture planning.

**Readiness for Phase 12 Chapter Architecture + Figure/Table Planning + Writing Blueprint: READY**
