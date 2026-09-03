# Phase 13 Evidence-Grounded Working Draft

Status: working manuscript draft

Abstract: pending later phase

# CH01 — Introduction and Review Scope

## Review problem and internal scientific thesis

High-pressure gas injection, compressible wave formation, liquid breakup, mixture preparation, and pilot-assisted ignition are often studied as separate problems. Each domain has a mature local vocabulary and a substantial evidence base, yet the interfaces between them are less secure. Underexpanded-jet studies resolve shock topology; canonical shock–droplet studies resolve response to a prescribed load; spray and engine studies resolve mixture and ignition behavior. The existence of these adjacent bodies of evidence does not mean that the entire pathway has been observed under one HPDI condition.

The central review problem is therefore one of evidence-weighted mechanism transfer. Gas-jet studies support relations between definition-compatible boundary states and transient shock structure [[CITE:B009]] [[CITE:B021]]. Canonical studies support relations between specified compressible loading and droplet response [[CITE:C007]]. HPDI-relevant studies support timing-, geometry-, and mixture-dependent ignition [[CITE:A007]] [[CITE:A011]]. The missing evidence lies at the joins: topology has not been mapped to actual pilot-droplet loading; canonical mechanisms have not been validated for a dense reacting spray; shock-created fragments have not been followed into a measured HPDI mixture field; and a shock-caused mixture change has not been linked to ignition or combustion.

This review accordingly follows physical causality while refusing to give every arrow equal status. Its working thesis is that component physics is relatively well resolved but cross-scale closure remains incomplete. The contribution is not a free-form synthesis of paper summaries. It is a mechanism framework in which claims retain source identity, condition boundaries, evidence strength, and application directness.

FIG-01 introduces the progression from injection boundary through wave, loading, liquid response, collective and fragment states, mixture, and ignition. Solid, conditioned, inferred, and open connectors distinguish what is directly supported from what is transferred or missing. The framework makes a continuous research question visible without presenting a continuous observed mechanism.

The immediate need is therefore methodological as well as physical: terms and dimensionless numbers must be comparable before evidence can be joined. The next section defines the scope, terminology, and evidence-status discipline used throughout the review.

## Scope, terminology, and evidence-status discipline

[TAB-01 ABOUT HERE]

The review covers pilot-ignited high-pressure direct injection, transient underexpanded gaseous jets, shock and vortex structure, compressible droplet and cloud response, fragment transport and phase change, and HPDI mixture, ignition, and combustion coupling. Detonation and rotating-detonation studies are included only as bounded strong-wave analogues. Literature-library labels are management categories rather than physical stages or manuscript chapters.

Comparability begins with definitions. NPR must identify numerator and denominator roles, absolute or gauge basis, locations, and time state. Mach must distinguish jet, incident-shock, post-shock, relative, and detonation contexts. Weber, Reynolds, and Ohnesorge numbers must retain all component references. Loading duration must distinguish front passage, shocked-state exposure, expansion-limited forcing, and total history; breakup time and signed injection timing likewise require named start and end events. TAB-01 summarizes this definition discipline. Secondary synthesis shows that even commonly reported observables have unequal maturity—for example, Mach-disk position is better constrained than several other topology metrics [[CITE:B004]], while breakup regime boundaries remain sensitive to their defining state [[CITE:C002]] [[CITE:C003]].

Scientific statements are separated by evidence mode. Reported primary evidence describes observations or simulations within the source domain. Conditioned generalization combines compatible sources while retaining boundaries. Review-secondary context supplies terminology or field framing. Cross-scale inference connects adjacent domains only with cautious language. Evidence-gap statements identify an unmeasured link, and project hypotheses are labeled as such. Evidence strength is reported separately from HPDI application directness.

This discipline prevents normalization from manufacturing similarity. Two identical symbols may represent different physical states, and a strong canonical result may remain a low-directness application analogue. Correlation and author interpretation are not upgraded to causation. Numerical values are used only when source-linked and material to the argument; qualitative figure trends are not digitized or guessed.

The resulting method treats definitions as scientific boundaries rather than editorial detail. With those boundaries fixed, the article can follow a causal narrative without implying that every transition has been measured.

## Article framework and narrative route

[FIG-01 ABOUT HERE]

The article progresses from upstream boundary to downstream application. Chapter 2 defines the time-dependent injection state and the formation of underexpanded waves. Chapter 3 translates gas topology into local loading variables and exposes the missing measurement between that topology and actual pilot droplets. Chapter 4 examines canonical internal response, deformation, instability, and fragmentation. Chapter 5 introduces collective corrections and audits transfer to a dense spray. Chapter 6 follows fragments through transport and conditional phase change to the open mixture bridge. Chapter 7 establishes the direct HPDI chronology–mixture–ignition evidence before isolating the missing shock cause. Chapter 8 treats detonation and RDE evidence as an analogue. Chapter 9 reorganizes the results by closure status and derives research priorities.

This order is a mechanism route, not a claim that the full route is observed. Four discontinuities are introduced where they first become physically relevant and remain open in the final synthesis: shock topology to pilot-droplet loading, canonical response to dense reacting spray, shock-created fragments to measured mixture, and shock-caused mixture change to ignition. Evidence downstream of a gap is not used to fill it rhetorically.

FIG-01 provides the single article-level framework. Later figures expand individual segments without duplicating the full schematic, and planned tables preserve definition and condition constraints. Direct, mixed or indirect, cross-scale, and gap encodings are used consistently. The strong-wave analogue is placed after direct HPDI evidence so that it cannot silently substitute for application measurements.

The narrative begins, therefore, with the boundary state that can be established most defensibly: pressure role and history, valve and injector chronology, nozzle geometry, gas properties, and ambient thermodynamics. Only after that state is typed can the underexpanded wave field—and eventually its possible interaction with liquid—be interpreted.

# CH02 — High-Pressure Injection and Transient Underexpanded-Wave Formation

## Definition-complete injection and ambient boundary state

[TAB-02 ABOUT HERE]

An underexpanded jet is not specified by a nominal injection pressure alone. The physically relevant upstream boundary includes the pressure role and reference state, the time at which it is evaluated, nozzle geometry, gas thermodynamic state, and the ambient pressure, temperature, and density. A storage pressure, a rail pressure, a nozzle-inlet stagnation pressure, and a reconstructed exit pressure are not interchangeable numerators for a pressure ratio. Gauge and absolute pressures are likewise not interchangeable. The denominator must be identified as the local ambient or chamber pressure at the relevant event. These requirements make the nozzle pressure ratio contextual rather than self-defining. TAB-01 summarizes the minimum definitions needed before ratios or dimensionless groups can be compared.

Within definition-compatible conditions, pressure ratio changes jet momentum, penetration, occupied volume, and entrainment, but it does not impose a geometry-independent monotonic penetration law. Experiments and simulations show that penetration and dispersion depend on ambient density, nozzle configuration, and the transient stage used for measurement; in one modeled geometry, increasing the reported pressure ratio did not monotonically increase hydrogen penetration [[CITE:B006]] [[CITE:B009]] [[CITE:B015]]. Ambient pressure, density, and temperature also alter formation time, diffusion, penetration, and lateral growth. Their effect on a settled Mach-disk position can be more regular when the contextual pressure ratio is held fixed, but fixed-NPR and fixed-injection-pressure comparisons describe different experiments [[CITE:B021]] [[CITE:B028]] [[CITE:B011]]. The defensible statement is therefore conditional: pressure ratio is an important part of the boundary state, not a sufficient similarity coordinate.

Nozzle size, exit shape, and inter-jet spacing add independent structure to that boundary. They reorganize expansion waves, shear-layer growth, coherent vortices, and jet interaction, producing nonlinear changes in dispersion and mixing [[CITE:B022]] [[CITE:B028]]. The evidence does not span a common factorial matrix of diameter, shape, spacing, gas species, and pressure ratio, so these effects cannot be collapsed into a universal geometry correction. A comparison-ready record must retain the diameter basis, passage length and shape, discharge configuration, number and orientation of holes, gas composition, and ambient state. The boundary variables and their permissible comparisons are organized in TAB-02 and represented as the upstream block of FIG-02.

Thermodynamic and numerical definitions are part of the scientific boundary rather than implementation details. Real-gas treatment and nozzle representation can materially change exit and centerline states even when a recognizable barrel-shock and Mach-disk topology remains. Turbulence closure, spatial resolution, and dimensionality similarly affect quantitative mixing and shock metrics; the present evidence does not establish a universal ranking of model families [[CITE:B008]] [[CITE:A028]]. Consequently, qualitative topological agreement cannot be used as proof that two calculations impose the same local density, velocity, or pressure history.

The upstream state should therefore be reported as a typed, multivariable boundary: pressure role, pressure type, location and time basis; nozzle geometry; gas properties; and ambient thermodynamic state. This discipline prevents nominally identical NPR values from concealing different physical problems. It also exposes the next requirement: even a complete static boundary cannot reconstruct the formation, overshoot, and stabilization created by valve opening and injector pressure build-up.

## Injector pressure build-up and developing underexpanded state

[FIG-02 ABOUT HERE]

The early underexpanded jet is an event-driven flow, not a steady jet observed at shorter elapsed time. Valve motion and the pressure history at the injector or nozzle inlet determine when choking begins, how rapidly the exit state develops, and whether the shock system overshoots before approaching a quasi-steady configuration. A plateau rail pressure or a single NPR therefore cannot reconstruct the developing interval. Time must be referenced to a defined event—command, needle lift, start of mass flow, or optical appearance—and the pressure must be attached to a known location and reference type.

Transient studies consistently distinguish formation, instantaneous, overshoot, and stabilized Mach-disk positions. Pressure build-up and valve opening produce a developing state in which the barrel shock and Mach disk move while the mass-flow and exit conditions are still changing; only later may a quasi-steady relation become meaningful [[CITE:B014]] [[CITE:B018]] [[CITE:B021]]. Supporting injector studies show that the relevant chronology depends on the hydraulic or pneumatic actuation and on how the internal pressure communicates with the nozzle [[CITE:B013]] [[CITE:B017]] [[CITE:B029]]. The observable called “Mach-disk position” must therefore carry a state qualifier. Mixing an early maximum, a time-resolved position, and a settled value in one scaling relation would manufacture disagreement or agreement from different stages.

Choking supplies a useful physical transition, but a threshold reported for one release configuration is not a universal injector constant. One source describes hydrogen releases above its stated critical pressure ratio as choked and underexpanded, with a shock-bearing, nonuniform exit flow [[CITE:B007]]. That statement is retained as paper-conditioned evidence: the critical ratio depends on the gas model and the precise stagnation-to-back-pressure definition, while real injectors add losses, internal dynamics, and time-dependent upstream states. The safer cross-paper procedure is to identify whether and when the local nozzle state becomes choked under each source's definitions, rather than transfer a single numerical threshold.

FIG-02 should therefore represent the boundary as trajectories, not isolated values: valve state, local injector pressure, contextual NPR, shock appearance, shock motion, and the interval over which a stabilized state is claimed. TAB-02 provides the associated event and state qualifiers. This treatment also separates a pressure overshoot from a spatial overshoot of a shock feature; the two may be related, but they are not the same observable and need not be synchronous.

The practical implication is that injector history remains upstream of every later loading argument. A droplet exposed during shock formation does not experience the field inferred from a plateau NPR, and a diagnostic triggered by command timing may sample a different physical stage from one aligned to actual mass flow. Once event alignment and state qualification are retained, the developing and quasi-steady evidence can coexist without being forced into one curve. The next question is then narrower: among the shock features formed under compatible states, which topology measures are sufficiently constrained for comparison?

## Mach-disk and shock-cell organization under compatible states

Shock topology becomes comparison-ready only after the pressure definition, nozzle basis, gas, ambient state, and transient qualifier have been matched. Under those constraints, the most robust directional result is that increasing contextual NPR moves the Mach disk downstream for a fixed nozzle and generally increases its size; transient dimensions may overshoot their quasi-steady values [[CITE:B003]] [[CITE:B009]] [[CITE:B021]]. The claim is not that one universal correlation applies across facilities. It is that Mach-disk position has a reproducible direction within compatible gas-jet conditions, whereas the coefficient and even the appropriate diameter normalization remain configuration dependent.

Gas species illustrates why matching NPR is necessary but insufficient. At a matched reported ratio, the gross near-field barrel-shock and Mach-disk scale can remain similar in some calculations, while downstream shock cells, instability, potential-core length, and mixing develop differently [[CITE:B010]] [[CITE:B009]] [[CITE:B011]]. Density, speed of sound, real-gas thermodynamics, and nozzle-exit turbulence are coupled in these comparisons. Species should therefore not be treated as a label on an otherwise identical flow unless these properties and the numerical treatment have also been controlled.

The topology also changes with axial region. The near field is organized by expansion, recompression, the barrel shock, Mach disk, and successive shock cells; farther downstream, shocks weaken and turbulent mixing dominates. Equivalent-jet or notional-nozzle formulations can bridge these regions, but only after the initialization location, decay assumptions, and exit-state definition have been validated for the condition of interest [[CITE:B001]] [[CITE:B019]] [[CITE:B020]]. Experimental qualification of zone boundaries shows why a force-based or optical transition in one gas and nozzle cannot simply be relabeled as another source's potential-core length. A secondary synthesis likewise identifies Mach-disk position as better constrained than disk diameter, curvature, appearance threshold, cell wavelength, or potential-core length [[CITE:B004]].

This evidence hierarchy defines how FIG-02 and TAB-02 should be read. Mach-disk position may support a definition-matched comparison; diameter and cell spacing require stronger configuration controls; qualitative topology supports mechanism identification but not identical local states. No universal diameter, shock-cell-spacing, or potential-core relation is implied. Near-field and far-field observables should remain separate, and every distance must retain its feature definition and nozzle-diameter basis.

Chapter 2 therefore closes a bounded component problem: a complete, time-resolved injection boundary produces an evolving underexpanded jet, and compatible conditions support a well-constrained directional relation for Mach-disk position. It does not yet say what a liquid element experiences. A mapped shock surface, vortex, or cell pattern must still be translated into local pressure, density, velocity, relative Mach number, and forcing duration. That translation—from known gas-phase topology to the loading of actual pilot droplets—is the subject of the next chapter.

# CH03 — From Shock Topology to Local Multiphase Loading

## Shock, vortex, and wave topology as local gas-state sources

Gas-phase topology is the source of local multiphase loading, but an image of a shock or vortex is not itself a droplet-loading history. Barrel shocks, a Mach disk, reflected waves, spray-generated shocks, and coherent vortices change pressure, density, velocity, and their gradients in different spatial regions and over different intervals. The required bridge therefore begins with a typed wave origin and a local state pair, (p(x,t)), ρ(x,t), and (u(x,t)), rather than with a generic label such as “shock intensity.”

Near-field shock and vortex organization can alter jet or spray cone angle and downstream mixing. Numerical evidence links baroclinic and coherent-vortex structures to changes in the developing field, while also showing that pressure ratio, species, and nozzle geometry remain coupled [[CITE:B027]]. Such results establish that topology can reorganize a local gas state; they do not directly measure the loading of an HPDI pilot spray. The distinction matters because two cases with similar global cone angles can contain different local pressure jumps, relative velocities, and residence times.

Spray-generated shocks form another wave family. Their appearance depends on nozzle-exit velocity, injection-rate ramp, ambient sound speed and density, and injection timing. Where present, they can change penetration and spray angle; under typical hot, dense engine conditions, higher sound speed and stronger spray deceleration can suppress their formation [[CITE:D001]] [[CITE:D002]] [[CITE:D005]]. Nozzle-exit velocity must not be replaced with spray-tip velocity in this argument. The former participates in the wave-formation condition, whereas the latter is an evolving response of the dispersed system.

Reflected shocks demonstrate a different coupling. Schlieren experiments show reduced radial spray growth, cone angle, volume, and entrainment after reflected-wave interaction, while axial tip penetration changed comparatively little [[CITE:D004]]. This is direct evidence that a wave can redistribute spray development anisotropically. It is not evidence that an injector-generated near-nozzle shock produces the same response: wave origin, direction, interaction stage, ambient gas, and prior spray history differ. Those boundaries prevent the reflected-shock result from being used as a surrogate loading map for HPDI.

FIG-03 therefore begins with separate topology classes and converts each into candidate local state changes before any droplet-response arrow is drawn. The gas-side evidence supports spatial and temporal variation in pressure, density, and velocity. What remains absent is a synchronized measurement that follows those variations into the frame of actual pilot droplets. That absence is not a weakness of topology studies; it identifies the precise transfer that must be audited next.

## The unclosed shock-topology-to-HPDI-pilot-loading bridge

[FIG-03 ABOUT HERE]

The present corpus supports two adjacent relations but not their application-scale connection. Underexpanded-jet studies resolve how compatible boundary states organize Mach disks, shock cells, and transient wave motion [[CITE:B009]] [[CITE:B021]]. Canonical shock–droplet studies resolve how specified aerodynamic or shock loading produces deformation and breakup [[CITE:C007]] [[CITE:C016]]. No current study co-locates these measurements in an HPDI configuration so that the gas-jet shock field can be mapped onto the pressure, density, relative velocity, and exposure duration experienced by the actual pilot-droplet population.

This is the first major cross-scale discontinuity in the review. A topology map can identify candidate regions of compression, expansion, shear, and vorticity, but it cannot determine a droplet's trajectory through those regions without synchronized liquid-phase information. Conversely, a canonical experiment with a prescribed incident shock provides a definition-complete loading state but does not reproduce the evolving geometry, chronology, polydispersity, or thermochemistry of a pilot spray embedded in a high-pressure gaseous jet. Stitching the two component literatures produces a physically plausible bridge, not a measured HPDI mechanism.

Closing the bridge requires more than simultaneous pictures of a jet and a spray. The gas diagnostics must resolve local pressure or density and velocity with an event-aligned time base; the liquid diagnostics must provide droplet or ligament positions, sizes, and velocities in the same coordinate system. The analysis must then compute a relative rather than incident or jet Mach context, retain the definition of every Weber-number component, and distinguish shock-front passage from the duration of the shocked or accelerated state. Injector geometry, pilot/main chronology, ambient thermodynamic state, and measurement volume must also be common to both data streams. These requirements are summarized in FIG-03 and TAB-08.

The absence of this information means that strong component evidence can coexist with low application directness. It is scientifically defensible to state that underexpanded topology supplies candidate sources of local loading and that droplets respond to such loading. It is not defensible to state that a measured Mach-disk position establishes the load on an HPDI pilot droplet, or that canonical breakup evidence fills the missing measurement. The shock-topology-to-pilot-loading pathway therefore remains open.

The practical value of making the gap explicit is that later chapters can use canonical droplet evidence without silently upgrading it. They must treat the loading state as imposed and definition-complete, and any return to HPDI must remain conditional until the co-located measurement exists. The next step is to define that loading state in terms that preserve both magnitude and duration.

## Loading magnitude, duration, and response-time compatibility

Finite compressible loading cannot be represented by a pressure jump or Weber number alone. A liquid structure responds to the local gas-state change, relative velocity, density, and the interval over which that state acts. Shock-front passage, residence in the shocked gas, exposure before a following expansion wave, and the total observation time are different intervals. Combining them under a generic “exposure time” removes the physical event that starts and ends the forcing.

Jet-induced shock measurements illustrate the consequence. A shock can produce a push-away impulse, while a following expansion wave shortens the effective shocked-state duration; small droplets can approach the gas response during that interval whereas larger droplets respond much more slowly [[CITE:D003]]. The evidence therefore supports a compatibility argument: nonuniform or finite-duration forcing changes deformation and motion according to the relation between the loading history and the liquid response time. It does not establish a single universal duration or length scale across shock tubes, jets, sprays, and engines.

A comparison-ready load should retain the pre- and post-wave pressure, density, temperature, and velocity; the reference frame for incident, post-shock, or relative Mach number; and explicit start and end events for each interval. Weber, Reynolds, and Ohnesorge numbers must retain their density, velocity, length, viscosity, and surface-tension references. The response time must likewise be named: acceleration, deformation, capillary, instability-growth, or breakup time. TAB-01 collects these definitions, while FIG-03 shows why topology must pass through them before a droplet-response claim is made.

The ratio τ_loading/τ_response can be useful as a possible organizing metric suggested by this synthesis. It is not an established nondimensional parameter in the reviewed literature. Its numerator and denominator would have to be typed for each mechanism, and alternative choices may reverse the apparent ordering of cases. At present it should be used to formulate a measurement or modeling test, not to collapse heterogeneous published data.

This magnitude–duration formulation provides the interface between Chapters 3 and 4. It preserves what is known on the gas side while avoiding a false HPDI closure: the local loading variables are physically specified, but their values for actual pilot droplets remain unmeasured. Canonical response evidence can now be organized by a multivariable state rather than by a universal Weber-number taxonomy.

# CH04 — Compressible Droplet Deformation, Instability, and Secondary Breakup

## Multivariable compressible droplet-response state

[FIG-04 ABOUT HERE]

[TAB-03 ABOUT HERE]

Equal reported Weber numbers do not define equal compressible droplet loads. The result depends on which gas density and relative velocity enter the number, whether the Mach value describes the incident shock, post-shock stream, or droplet-relative flow, and how droplet size, liquid properties, and forcing duration are specified. Weber number is therefore one component of a loading state whose interpretation also requires Reynolds and Ohnesorge context, density ratio, initial diameter, thermal state, and a typed observation interval. TAB-03 organizes these comparison requirements.

Direct experiments and high-fidelity simulations show that deformation and breakup timing or morphology change jointly with aerodynamic loading, droplet size, and Mach context [[CITE:C014]] [[CITE:C025]]. Compressibility can alter transverse spreading and breakup morphology at supersonic conditions, while narrower numerical comparisons find similar early scaled drift, acceleration, or drag across the sonic transition [[CITE:C008]] [[CITE:C007]]. These results describe different response stages and metrics rather than a simple conflict. They show why a single regime boundary cannot be transferred across differing Mach frames and loading histories.

Reported breakup ranges illustrate the same limitation. A condition-specific data set found Rayleigh–Taylor piercing persisting near a reported Weber number of 800 for small droplets while shear-induced entrainment occurred near 200 for larger droplets [[CITE:C016]]. The observation is strong within the tested sizes and shocks, but it is not a universal critical-We reversal. It demonstrates that diameter relative to instability scales and the compressible forcing history can change mode selection even when a scalar loading number appears to suggest otherwise.

Regime maps remain valuable if their definitions travel with them. Morphological categories organize observations and downstream product states, yet each boundary must retain velocity, density, length, surface-tension, Mach, and time references [[CITE:C002]] [[CITE:C003]]. Coverage of broad taxonomy is also limited because the primary source C004 is unavailable in the frozen corpus. Secondary material is not used here to reconstruct that missing contribution.

FIG-04 therefore represents response as a multivariable state leading to possible deformation and breakup paths, not as a one-axis Weber ladder. This formulation reconciles apparently different trends through their physical stage and boundary conditions. It also prepares the next question: before surface instability dominates, what internal wave and circulation structures are created inside the liquid?

## Internal wave dynamics and deformation topology

The earliest liquid response contains dynamics that a bulk aerodynamic number cannot describe. An incident compression is transmitted and refracted at the curved interface; reflected and internal waves move through a medium whose acoustic properties and thermodynamic state may differ sharply from the gas. Their focusing, expansion, and interaction create localized pressure extrema, baroclinic circulation, and internal velocity structures that can precondition later flattening, jetting, or asymmetric deformation.

Model-resolved studies show that shock transmission, refraction, Mach-stem motion, and internal-flow topology depend on the wave-speed ratio, phase state, and shock strength [[CITE:C018]] [[CITE:C029]]. In transcritical calculations, changing the liquidlike or gaslike state changes the speed-of-sound ratio and hence the refracted-wave topology; stronger convergence can generate a focal pressure peak and an axial jet. Shock-strength changes also modify circulation and the balance between radial flattening and pressure-gradient-driven deformation. These mechanisms are direct within the modeled early-time domain but remain bounded by two-dimensional or axisymmetric geometry and by omitted viscosity, capillarity, heat transfer, cavitation, or chemistry.

Wave curvature supplies an additional condition. For one modeled divergent shock, curvature shifted ligament formation upstream and sustained greater spanwise extension relative to a planar comparison [[CITE:C019]]. The result is useful because it shows that the spatial history of loading can alter deformation topology even when a nominal shock strength is held similar. It must remain localized: the study used a two-dimensional cylindrical droplet and omitted several interfacial and phase-transition processes.

The mechanistic implication is not that internal waves uniquely determine the final breakup mode. Rather, their pressure and circulation imprint sets the initial deformation field on which external shear, wake dynamics, capillary retraction, and interfacial instabilities subsequently act. A model that matches only late projected width may conceal an incorrect early internal mechanism, while a model that resolves focusing accurately may still lack the physics needed for final fragmentation.

FIG-04 separates this internal-wave branch from the external aerodynamic branch and reconnects them at deformation. That separation preserves evidence status and prevents an idealized focusing result from being generalized to a hot, phase-changing, three-dimensional droplet. The next stage is the competition among interfacial instabilities and the multiscale structures they generate.

## Instability competition and multiscale breakup cascade

Secondary breakup is a staged competition among mechanisms, not the instantaneous assignment of a Weber-number label. The deformed parent liquid develops sheets, rims, surface waves, ligaments, and wake-coupled structures. Rayleigh–Taylor growth can amplify acceleration-driven disturbances; Kelvin–Helmholtz or shear processes strip and roll interfaces; capillarity retracts sheets and rims; wake pressure and recirculation redirect deformation. Which process dominates changes with Mach context, loading history, Ohnesorge number, geometry, and the event chosen to define breakup.

High-resolution experiments and interface-resolved calculations show recurrent sheet, wave, and ligament formation across extreme aerobreakup, including distinct first and later shedding events [[CITE:C012]] [[CITE:C013]]. This evidence supports a multiscale cascade: a parent-scale deformation produces intermediate liquid structures whose own instability and capillary times determine fragments. A single breakup time or final mode label therefore discards the sequence needed to predict fragment sizes and velocities.

Mechanism studies further show that morphology can emerge from different combinations of acceleration-driven, shear-driven, capillary, rupture, and wake processes [[CITE:C005]] [[CITE:C009]]. The labels are useful when attached to observations, but they should not be treated as mutually exclusive universal regimes. For example, early stripping and later piercing may occur in one history, and the sensitivity of later ligament shedding need not match that of the first event. Condition-specific overlap of nominal mode ranges reinforces this interpretation rather than creating a contradiction.

The source boundary is important. The unavailable C004 paper limits broad primary coverage of breakup taxonomy. The review retains that limitation and does not reconstruct the missing contribution from secondary accounts. The remaining evidence is sufficient to establish multistage instability competition, but not to declare a complete universal map. FIG-04 consequently uses branching and converging mechanisms, while TAB-03 requires that every regime statement carry its forcing and event definitions.

The downstream consequence is that breakup prediction must describe products, not only classifications. Sheets and ligaments determine an evolving fragment population, and recurrent shedding determines when mass enters that population. Whether current reduced models can reproduce those outputs across conditions is therefore a stricter question than whether they match one projected deformation curve.

## Regime and model predictive limits

A model validated against one observable is not thereby validated for the full breakup cascade. Projected width, center-of-mass acceleration, a first-breakup time, mode label, fragment distribution, cloud length, evaporation time, and phase-change coupling are distinct targets. They respond to different omitted physics and often use different measurement definitions. The reviewed comparisons therefore do not support a single reduced model that predicts all of them across the shock–droplet condition space [[CITE:C006]].

Reduced-order formulations can still be useful within a declared domain. A source-specific statement reports successful deformation prediction with the Taylor Analogy Breakup model, which represents the droplet through a spring–mass–damper analogy [[CITE:C020]]. That result remains paper-conditioned. It does not establish that the same closure predicts compressible internal waves, multistage ligament shedding, fragment statistics, or phase change, and it cannot be promoted into full-condition coverage.

The appropriate validation hierarchy follows the intended use. A model for momentum exchange may be assessed against acceleration and drag; a model for atomization must also predict event timing and product statistics; a model used for evaporation or ignition must preserve mass, surface area, fragment temperature, and residence history. Agreement in an upstream quantity is necessary but not sufficient for a downstream application. The missing C004 source additionally constrains any claim of comprehensive taxonomy coverage, but it does not invalidate the resolved mechanism evidence from the available corpus.

FIG-04 marks model-conditioned paths separately from directly observed mechanisms. TAB-03 should record the validation observable, event definition, dimensionality, interface treatment, and condition range alongside any model result. This prevents a regime map from being read as a product-state closure and makes disagreement traceable to the metric that was actually tested.

Chapter 4 thus establishes a bounded canonical result: definition-complete compressible loading produces internal wave response, deformation, competing instabilities, and staged fragmentation. It does not supply a universal Weber-only taxonomy or a universal reduced closure. More importantly for HPDI, the chapter has treated a single idealized target. Neighboring droplets and clouds can redistribute the load itself, so the next chapter introduces the collective mechanisms absent from isolated-droplet response.

# CH05 — Collective Droplet Effects and Canonical-to-Spray Transfer

## Ordered-droplet shielding, squeeze flow, and channel closure

The response of neighboring droplets depends on arrangement as well as spacing. A tandem pair introduces a wake and load-shadowing problem, whereas a parallel pair introduces squeeze flow, lateral pressure redistribution, and possible closure of the gas channel between interfaces. These mechanisms can change deformation and breakup in opposite directions, so a universal critical spacing would erase the geometry that produces the effect.

Tandem experiments show that the leading droplet can remain close to isolated behavior while its wake delays and weakens the trailing droplet's response. The effect increases at smaller normalized spacing and lower Weber number in the tested domain; the reported transition spacing itself varies with Weber number [[CITE:C035]]. This is direct evidence of wake shielding, not a general attenuation law for arbitrary clouds. The spacing is defined by the experimental arrangement and initial diameter, and the finite post-shock window limits later low-We rupture observations.

Parallel droplets exhibit a different topology. At lower Weber number, decreasing spacing changes post-flattening bending and can shift the observed breakup mode. At higher loading, a sufficiently small gap promotes equatorial filaments and closure of the channel between droplets, with repeated closure and reopening in some cases [[CITE:C036]]. The pressure and velocity field between the droplets is therefore not the isolated solution sampled twice; the interfaces jointly reshape the flow.

These findings support a direct collective correction: arrangement and (S/D) redistribute effective loading through shielding, squeeze flow, and channel closure. They do not support averaging tandem and parallel results into one spacing curve. Weber and Mach context, diameter basis, alignment uncertainty, and shock history must remain attached to the configuration. TAB-04 therefore separates isolated, tandem, parallel, cloud, and dense-spray states rather than treating “multiple droplets” as a single category.

FIG-05 uses these ordered systems to identify mechanisms that must be considered when moving beyond a single droplet. The next step is not to assume that an HPDI spray behaves like an array of pairs, but to examine a population-scale feedback already visible in dilute clouds: the dispersed phase can attenuate and reshape the wave that loads downstream droplets.

## Cloud-scale shock attenuation and feedback

A droplet population is not only a passive recipient of a shock. Momentum and energy exchange, interface area, and fragmentation modify the transmitted wave, so the population changes the subsequent loading environment of its downstream members. This feedback is already measurable in dilute clouds and introduces a mechanism absent from isolated- and ordered-droplet descriptions.

Cloud experiments and coupled models show that attenuation of peak overpressure and impulse depends on volume fraction, droplet size, exchange area, shock strength, and breakup [[CITE:C033]]. When fragmentation is omitted, the transmitted pressure can be overpredicted; including a breakup-dependent exchange-area evolution better reproduces the characteristic transient pressure [[CITE:C034]]. This evidence directly supports the direction of the feedback within the tested dilute-cloud configurations: breakup changes area and interphase coupling, which changes shock propagation.

The variables must nevertheless be typed. Volume fraction alone does not specify number density, size distribution, or exchange area, and transmitted peak pressure is not interchangeable with impulse or a downstream local velocity history. A closure based on one assumed diameter evolution is model-conditioned even when it matches one pressure trace. Cloud statistics, breakup law, wave strength, and sensor location therefore belong to the scientific statement.

The result also changes the interpretation of downstream breakup. Droplets deeper in a cloud may see a weaker and temporally reshaped wave than upstream droplets, while the fragments produced upstream can strengthen interphase exchange. Consequently, an externally imposed shock history cannot be applied uniformly to the population. FIG-05 represents this two-way relation between population state and gas loading; TAB-04 records which collective descriptors are available.

Dilute-cloud attenuation is not a validated law for a dense, polydisperse, evaporating, reacting HPDI pilot spray. Collisions, turbulence modulation, broad size and spacing distributions, vapor generation, walls, and chemistry add interactions not resolved in the canonical cloud evidence. The data establish the need for collective correction before transfer, not the correctness of a particular dense-spray correction. That transfer boundary is audited explicitly next.

## Canonical-to-dense-spray transfer audit

[FIG-05 ABOUT HERE]

[TAB-04 ABOUT HERE]

Single droplets, ordered pairs, dilute clouds, and dense reacting sprays are distinct physical systems. Canonical studies establish mechanisms cleanly: local compressible loading produces deformation and instability; tandem wakes shield; parallel gaps generate squeeze flow and channel closure; and droplet clouds attenuate transmitted waves [[CITE:C035]] [[CITE:C036]] [[CITE:C033]] [[CITE:C034]]. The evidence supports the necessity of collective corrections before these mechanisms are transferred to HPDI. It does not validate the dense-spray transfer itself.

An actual pilot spray adds polydispersity, irregular spacing, a distribution of velocities, droplet–droplet and droplet–ligament interaction, turbulence, wall proximity, phase change, and possibly reaction. Each addition can alter both the local load and the product population. An isolated regime map cannot represent shielding; an ordered spacing criterion cannot represent a disordered distribution; and a dilute-cloud attenuation closure may fail when interface area and vapor evolve rapidly. Population descriptors—size and velocity distributions, number or volume density, spatial correlations, thermochemical state, and their time evolution—are therefore required inputs rather than optional refinements.

The gas-side boundary is equally important. Underexpanded-jet studies provide strong topology evidence [[CITE:B009]] [[CITE:B021]], while canonical droplet studies provide strong response evidence [[CITE:C007]]. Because the topology-to-pilot-loading bridge remains open, adding collective mechanisms does not repair the missing load. A dense-spray validation must measure the evolving gas state and the population response together under synchronized HPDI-relevant conditions.

FIG-05 marks this canonical-to-dense-spray pathway as unclosed, and TAB-04 identifies the state variables that cannot be merged across configurations. The permitted inference is qualitative: shielding, squeeze flow, channel closure, and attenuation provide physically grounded mechanisms likely to matter when local arrangements reproduce their conditions. Quantitative prediction of an HPDI pilot spray requires an explicit collective-state model and validation. Applying a single-droplet breakup regime directly would overstate both evidence strength and application directness.

This second discontinuity defines the output required from future spray models. They must predict not only a mean response but an evolving fragment population under redistributed loading. Chapter 6 therefore follows that population into transport and phase change, while keeping the dense-spray transfer boundary visible.

# CH06 — Fragment Populations, Phase Change, and the Mixture-Formation Bridge

## Fragment population state and transport

Breakup mode is not a sufficient initial condition for downstream transport. Once the parent liquid forms sheets, rims, and ligaments, the relevant state becomes a population: fragment sizes, velocities, positions, temperatures, spacings, mass fractions, and their evolution with time. A single arithmetic mean can conceal the small fragments that dominate area and the large remnants that dominate mass and survival.

Measurements show that fragment-size distributions and inter-fragment spacing evolve with breakup stage and acceleration [[CITE:C025]]. The population sampled after the first shedding event is not equivalent to one sampled after later ligament rupture. Detection thresholds and line-of-sight overlap can remove small products, while number-, area-, and mass-weighted statistics answer different questions. Reporting a D10 or D32 without its weighting, sampling time, and resolved range therefore does not fully specify transport or evaporation input.

The same distinction applies to velocity. Fragments inherit different parts of the parent deformation field and experience size-dependent acceleration and wake interaction. Their relative velocity determines later aerodynamic loading, while spatial correlations determine collision, shielding, and cloud expansion. Parent center-of-mass motion cannot replace the joint size–velocity distribution. High-resolution sheet and ligament evidence [[CITE:C012]] [[CITE:C013]] and reduced-model limitations [[CITE:C006]] reinforce why downstream prediction requires product-state validation.

FIG-06 places the evolving fragment population between breakup and transport. TAB-05 records the distribution definition, weighting, threshold, sampling event, and gas-history interval. The purpose is not to demand every statistic from every paper; it is to prevent a regime label or one mean diameter from being interpreted as a complete downstream state.

Fragment state also mediates the next coupling. It changes exchange area, response time, residence, and thermal history, but those changes do not automatically imply faster evaporation or improved mixture formation. Whether breakup and phase change materially overlap depends on size, volatility, gas state, and the duration of exposure.

## Overlap of breakup, evaporation, and droplet survival scales

[TAB-05 ABOUT HERE]

Breakup and evaporation are concurrent only when their characteristic histories overlap under the same state. Fragmentation increases area and changes acceleration, but evaporation also depends on temperature, pressure, volatility, vapor accumulation, and residence. The correct question is therefore not whether breakup “enhances evaporation” in general, but which parent or fragment sizes experience significant mass loss during the relevant forcing and observation intervals.

Small-droplet and strong-wave studies show cases in which breakup, cloud growth, and evaporation occur on comparable scales. Evaporation-only calculations can substantially overpredict observed droplet survival, whereas adding breakup shortens the modeled survival region toward the experiment [[CITE:C024]] [[CITE:D017]]. The agreement remains model-conditioned because post-wave gas histories, optical thresholds, and breakup closures differ. It nevertheless establishes that an evaporation-only representation may be inadequate when fragmentation rapidly changes size and area.

The opposite-looking result is also direct within its boundary: for tested droplets larger than 100 μm, evaporation had negligible influence on measured deformation over the reported early observation interval [[CITE:C026]]. This does not contradict later or smaller-scale overlap. It isolates a stage in which aerodynamic deformation was faster than measurable phase-change influence. Extending the statement to later breakup, fragments, or smaller droplets would remove the size and time boundaries that make it valid.

Locally supersonic vaporization adds a compressible constraint. Relative Mach number and the bow-shock pressure rise modify the local saturation margin; weaker pressure rise and higher liquid volatility can favor superheating effects [[CITE:C027]]. These tests differ from high-pressure engine environments, so the result supplies a mechanism and a comparison requirement rather than an HPDI prediction.

FIG-06 therefore shows overlapping but separately defined breakup, transport, and phase-change intervals. TAB-05 requires initial and fragment size, liquid, gas thermal history, pressure state, volatility, detection threshold, and time basis. With those boundaries preserved, the literature supports conditional overlap rather than a universal diameter threshold. The remaining question is why phase change can oppose deformation in one regime and promote it in another.

## Conditional direction of phase-change coupling

Phase change has no universal sign in droplet breakup. Different studies isolate different interfacial and thermal mechanisms, so apparently opposing trends can be conditionally consistent. Vapor production may build a low-temperature layer and Stefan flow that reduce gas–liquid shear; heating may instead lower surface tension and make deformation or rupture easier. Which effect dominates depends on size, volatility, thermal state, density ratio, surface tension, model coefficients, and forcing history.

In selected phase-change simulations, evaporation or a vapor layer reduced interfacial shear and opposed deformation or bag development [[CITE:C031]]. The inferred mechanism is consistent with temperature, vorticity, and interface fields, but it depends on the chosen phase-change coefficients and modeled thermodynamic family. It supports a possible suppressing pathway under those conditions, not the statement that vaporization suppresses breakup generally.

A different numerical framework found that heating-induced surface-tension reduction promoted breakup in non-isothermal hydrocarbon cases, especially at lower reported Weber number and higher gas temperature [[CITE:C032]]. That pathway is also condition-specific and is not directly equivalent to vapor-layer shear reduction. The two results emphasize different parts of the coupled balance: one changes the effective aerodynamic coupling near the interface, while the other changes liquid resistance through temperature-dependent properties.

The proper synthesis is a branching relation. Thermal and phase-change processes alter both the applied interfacial stress and the resisting liquid properties, and their relative rates determine direction. A defensible comparison must retain Stefan or vaporization state, density ratio, volatility, gas temperature, surface tension model, diameter, and observation interval. FIG-06 encodes both branches; TAB-05 records their boundary variables rather than forcing them into a single trend.

This conditional result narrows what can be carried toward HPDI. Fragment and phase-change physics provides mechanisms for changing transport and survival, but it does not demonstrate that a shock has measurably changed an engine mixture field. That application bridge remains to be evaluated directly.

## The unclosed shock-fragment-to-mixture bridge

[FIG-06 ABOUT HERE]

General breakup and phase-change physics does not by itself establish a shock-generated HPDI mixture change. The corpus supports an evolving fragment population, conditional overlap of breakup and evaporation, and mixture-controlled ignition as separate relations [[CITE:C024]] [[CITE:C031]] [[CITE:A007]] [[CITE:A011]]. It does not contain a synchronized application measurement that follows a specified shock load through pilot fragmentation and evaporation into a resolved HPDI mixture-fraction or species field.

The missing link is broader than a measurement of smaller droplets. To attribute a mixture change to shock-mediated fragmentation, the experiment or simulation must identify the upstream wave and local load, resolve the parent-to-fragment population, retain vaporization and transport histories, and measure the resulting gas-phase composition before ignition. Hot dense gas, turbulence, walls, polydispersity, pilot/main chronology, and fuel volatility must be represented in the same condition. Otherwise a correlation between injection settings and mixture state cannot isolate the shock contribution.

Existing HPDI studies provide direct mixture and ignition information, and canonical studies provide strong component mechanisms. Combining them supports a physically plausible research hypothesis, not a continuous causal claim. The full sequence—shock, breakup, evaporation, mixture redistribution, and ignition—remains insufficiently evidenced across the incompatible scales and histories represented by canonical droplets, clouds, vessels, engines, and strong-wave devices [[CITE:A007]] [[CITE:A011]] [[CITE:C024]]. FIG-06 leaves the shock-fragment-to-mixture connector open; TAB-08 states the diagnostics required to close it.

This third discontinuity is distinct from the earlier canonical-to-dense-spray gap. Even a validated dense-spray breakup model would still need to show that the resulting fragment and vapor fields materially alter the HPDI mixture at the relevant time and location. Conversely, a measured mixture change would not identify a shock cause unless the upstream wave and fragment history were co-resolved.

Chapter 6 therefore concludes with bounded component knowledge: fragment state mediates transport; breakup and evaporation can overlap; and phase-change direction is conditional. The contribution of shock-created fragments to a measured HPDI mixture field remains open. Chapter 7 now turns to what is directly known in the application domain—chronology, overlap, mixture preparation, ignition, and heat release—before returning to the untested shock-mediated cause.

# CH07 — HPDI Mixture Formation, Ignition, and Combustion Coupling

## Injection chronology, geometry, and mixture preparation

[FIG-07 ABOUT HERE]

[TAB-06 ABOUT HERE]

In pilot-ignited direct injection, timing is a signed sequence rather than an unsigned interval. The identities of the first and second fuels, the event used for start of injection, and the sign convention for relative timing determine whether a positive shift means more premixing, more overlap, or a reversal of fuel order. Geometry then determines where the two jets entrain, intersect, encounter the wall, and form stratified or premixed regions. TAB-06 therefore treats chronology and injector arrangement as coupled application variables.

Across tested configurations, relative pilot/main timing and gaseous-fuel timing directly control the achieved premixing and shift heat release between mixing-controlled and more premixed behavior [[CITE:A006]] [[CITE:A011]] [[CITE:A018]]. The direction and preferred interval are not universal: dwell definition, fuel pair, ambient state, chamber geometry, and operating point change the ignition and stability tradeoffs. Timing should thus be interpreted through the mixture state it produces, not as a transferable optimum.

Injector-hole arrangement and relative jet angle reorganize entrainment, overlap, vortex transport, wall interaction, and stratification. More local mixing does not guarantee lower emissions. One configuration increased early entrainment at equal penetration yet produced higher particulate matter, which the authors associated with residence in a rich, moderate-temperature region [[CITE:A005]]. Other studies report angle- and flow-area-dependent changes in overlap, combustion, and wall interaction [[CITE:A016]] [[CITE:A017]]. These results are direct or model-resolved within particular chambers; they demonstrate mechanism sensitivity to geometry rather than a universal “more mixing is better” rule.

Review-secondary evidence identifies independent timing, quantity, and interval control as a defining opportunity of dual-fuel direct injection, but it does not replace primary confirmation under standardized conditions [[CITE:A027]] [[CITE:A029]]. A further paper-conditioned observation reports natural-gas premixing near the piston-bowl wall before ignition across its tested conditions, including a sequence in which gas injection follows pilot combustion [[CITE:A014]]. That statement remains localized to its source and is not generalized to all HPDI geometry.

FIG-07 begins with this directly supported application chain: signed chronology and geometry reorganize overlap, entrainment, wall interaction, and mixture stratification. It does not yet assign an upstream shock cause. The next section follows the measured mixture and pilot-product state into ignition, where overlap can assist the main fuel while simultaneously disturbing the pilot.

## Pilot-product interaction and ignition response

Pilot/main overlap has stage-dependent effects. Interaction with hot, reacting pilot products can accelerate main-fuel ignition, while the same gas jet can dilute, displace, or disrupt the pilot before it establishes a robust ignition kernel. Chronology and geometry therefore determine not only how much the jets overlap, but which chemical and fluid-mechanical stage is being perturbed.

Optical vessel, rapid-compression, engine, and simulation studies support this conditional direction. Stronger overlap or an appropriate dwell can shorten the pilot-to-main transition and accelerate gaseous-fuel ignition, yet excessive or early interaction can delay or suppress pilot ignition [[CITE:A009]] [[CITE:A022]] [[CITE:A007]]. The configurations use different ambient reactivity, angle definitions, and overlap metrics, so the evidence supports a mechanism class rather than one optimal dwell. The safest statement is that the mixture and pilot-product distributions directly govern the ignition response within their chronology and geometry.

Conditioned hydrogen evidence shows why the end-of-injection event must be retained. In one tested sequence, ignition after hydrogen end of injection produced slower propagation and persistent lean unburned regions [[CITE:A020]]. Another study found that sufficiently advanced hydrogen injection delayed diesel pilot ignition and attributed the effect to pre-ignition dilution, while noting that the pre-ignition fuel distributions were not directly visualized [[CITE:A026]]. The first is a reported condition-specific observation; the second mechanism remains an author interpretation rather than direct measurement of dilution.

Chemical state supplies an additional but bounded explanation. Homogeneous-reactor calculations found temperature to dominate methane ignition above about 1100 K, while realistic H/OH radicals shortened delay mainly over the reported 950–1100 K interval [[CITE:A012]]. Because this zero-dimensional analysis omits turbulent transport, it isolates kinetic sensitivity rather than reproducing a jet interaction. It is best used to interpret why hot products and radicals may affect ignition differently across local thermal states.

FIG-07 encodes these evidence levels separately: observed chronology and overlap lead to measured ignition responses, while dilution or radical pathways retain their experimental or model-based status. The resulting ignition chronology sets the initial conditions for heat release, but combustion benefits and penalties remain coupled to injection pressure, pilot energy, load, and operating point.

## Heat-release mode, injection pressure, and operating response

Injection pressure and pilot energy influence different stages of combustion. Higher gaseous-fuel pressure can increase injection rate and post-ignition mixing, shortening a mixing-controlled event at higher load, while ignition itself may be comparatively insensitive in a particular optical engine [[CITE:A001]] [[CITE:A002]] [[CITE:A011]]. The benefits diminish or change with speed, load, nozzle flow area, and timing, and can be accompanied by NOx, pressure-rise, noise, or stability penalties. A pressure trend is therefore meaningful only with its pressure definition and operating point.

Pilot energy changes the initial reacting field. In one optical study, increasing diesel energy share strengthened and spatially extended the pilot flame and accelerated the initial hydrogen response, whereas the later mixing-controlled phase remained similar across the tested shares [[CITE:A026]]. This separates an ignition/early-reaction effect from late gaseous-fuel mixing control. Natural-luminosity thresholds and different imaging arrangements limit quantitative intensity comparisons, but the stage-specific direction is directly supported.

Other combustion classifications remain paper-conditioned. One engine study organized pilot-ignited direct-injection natural-gas behavior into relative-injection-timing domains in which pilot and gas apparent heat release and emissions varied consistently with gas fraction and injection pressure [[CITE:A013]]. Another reported feasible controlled-phasing hydrogen dual-direct-injection operation up to its tested hydrogen energy share without pre-ignition or knock [[CITE:A018]]. Neither result defines a universal operating map; each carries its engine, speed, load, timing, and diagnostic boundaries.

The synthesis is therefore a conditioned operating chain: injection settings and chronology shape mixture and ignition; ignition phasing and mixing then shape heat-release mode; performance and emissions emerge from the complete operating point. More intense mixing can shorten late combustion while increasing another penalty, and no single response can stand for overall improvement. FIG-07 and TAB-06 preserve this separation.

The remaining hydrogen-specific heat-release observations are narrower still. They are included because they constrain interpretation within their sources, not because they support a general HPDI scaling law.

## Condition-specific hydrogen heat-release behavior

Hydrogen heat-release profiles depend on injection duration, ignition timing, fuel comparison, and the interval used to define combustion. In one dual-fuel study, a peak in apparent heat release immediately after hydrogen-jet ignition was followed by a steadier interval until the end of hydrogen injection when hydrogen injection and combustion outlasted the diesel surrogate; the profile changed when the surrogate's injection and combustion duration altered that ordering [[CITE:A021]]. The same source attributed most of the dual-fuel apparent heat release to hydrogen under its conditions. These statements remain localized because their source-specific diagnostics and timing do not establish a universal profile.

A numerical comparison reported generally higher hydrogen heat-release rate than methane and attributed the difference to coupled fuel and jet properties; late combustion began after injection ended and heat release then declined rapidly [[CITE:A024]]. This is model-based comparative evidence, not a general ranking across injectors and operating states. Momentum, quenching, flammability, mixture formation, and injection duration are coupled in the comparison.

These observations add context to the directly supported timing–mixture–ignition framework, but they should not be merged into a cross-paper AHRR law. TAB-06 retains the fuel, timing, diagnostic, and operating boundaries. The application argument can now return to its central unresolved question: whether any of the measured ignition and heat-release changes were caused by an upstream shock-mediated change in the pilot spray or mixture.

## The unclosed shock-caused mixture-to-ignition link

The application corpus strongly supports a chronology-to-mixture-to-ignition relation. Relative timing, geometry, overlap, and pilot-product distribution change mixture preparation and ignition under tested HPDI-relevant conditions [[CITE:A006]] [[CITE:A011]] [[CITE:A018]] [[CITE:A009]] [[CITE:A022]] [[CITE:A007]]. None of this evidence identifies an upstream shock as the cause of the mixture change.

The distinction separates two pathways. The direct pathway begins with controlled injection chronology and geometry, continues through measured or model-resolved mixture and pilot-product states, and ends in observed ignition or heat release. The open pathway begins with an underexpanded or spray-generated wave, proceeds through local droplet loading, dense-spray fragmentation and phase change, and would then require a measured mixture redistribution that changes ignition. Strong support for the direct pathway cannot close the open one.

Closing the shock-caused mixture-to-ignition link requires synchronized diagnostics spanning all relevant events. The wave field and local gas state must be measured with the pilot population; fragment and vapor evolution must be resolved; the pre-ignition species or mixture field must be quantified; and ignition location, delay, and heat release must be aligned to the same injection chronology. A comparison in which only injector pressure changes would remain confounded by mass flow, momentum, mixing, and timing unless the shock-mediated branch were isolated.

The corpus therefore makes a shock-mediated pathway physically plausible through component evidence, but it does not demonstrate that shock-induced pilot breakup improves ignition. FIG-07 leaves the causal connector open, and FIG-09/TAB-08 carry the required evidence into the final synthesis. This fourth discontinuity remains distinct from ordinary uncertainty in the direct timing chain.

With the direct HPDI evidence established first, the review can now use detonation and rotating-detonation studies for a narrower purpose: to examine droplet response under strong reacting waves. Those systems provide a bounded analogue, not proof of HPDI behavior.

# CH08 — Strong-Wave Analogues: Detonation and Rotating Detonation Engines

## Droplet and evaporation scales in detonation and RDE wave response

Two-phase detonation and rotating-detonation systems expose liquid droplets to strong reacting waves, but their characteristic ratios are meaningful only within the definitions used to construct them. Initial diameter and evaporation length or time may be compared with refill, reaction-zone, detonation-height, or wave-transit scales. These denominators represent different physical clocks and lengths; a symbol such as (L_E/L_D) cannot be moved between studies without preserving both definitions.

Within the rotating-detonation domain, droplet size and evaporation scale affect vaporization completeness, unburned pockets, wave structure, multiplicity, speed deficit, stabilization, and extinction [[CITE:D009]]. One study defines an evaporation-distance to detonation-front-height ratio and, within its no-pre-evaporation family, relates increasing scale mismatch to larger unburned pockets and eventual shock–flame decoupling. The result is direct within the simulated inlet, chemistry, geometry, and scale definition; its numerical thresholds are not transferred outside that system.

Position relative to the wave adds a trajectory-dependent history. Modeling shows that droplets close to the detonation front experience a sharper thermal impulse and faster vaporization, while some farther downstream are weakly affected; longitudinal position also changes kinematics and spatial distribution [[CITE:D014]]. A population cannot therefore be described by diameter alone. Wave-relative position, pre-vaporized fraction, local thermochemical state, and residence through refill and post-wave regions must accompany it.

The broader literature contains differing fuels, chemistries, geometries, initial vapor fractions, wave numbers, and characteristic-length definitions. These differences bound quantitative aggregation and explain why the planned synthesis remains qualitative or condition-faceted. FIG-08 maps the strong-wave mechanism within its own domain; TAB-07 retains both numerator and denominator of every scale ratio.

The supported conclusion is that characteristic-scale coupling controls whether liquid persists into dynamically important regions of an RDE or detonation flow. It is not that an RDE evaporation ratio predicts HPDI mixture preparation. The next section sharpens this boundary by comparing reacting and inert waves at a matched leading-shock Mach.

## Reacting versus inert strong-wave droplet loading

Equal leading-shock Mach numbers do not guarantee equal droplet loading. Incident or detonation Mach describes the leading wave, while later deformation depends on post-wave velocity, density, sound speed, pressure gradients, chemistry, and the duration of those states. A matched leading Mach can therefore produce similar early wave topology and divergent subsequent cavitation, drag, deformation, and breakup.

Detonation experiments show that smaller droplets and stronger waves accelerate instability and breakup, with an early shear-stripping stage transitioning toward coupled Kelvin–Helmholtz/Rayleigh–Taylor piercing and catastrophic breakup [[CITE:D018]]. Collapsed breakup time also differs by liquid in the tested facility, consistent with a role for liquid properties. These are strong within-domain observations, not an inert-shock correlation or an engine-spray closure.

Matched modeling directly demonstrates the post-wave distinction. At equal leading-shock Mach, detonation and inert-shock cases can share early topology, but heat release changes post-wave velocity and sound speed, pressure-gradient history, and the duration of low-pressure or accelerated states [[CITE:D019]]. The modeled detonation case consequently differs in cavitation collapse, forward-jet formation, leeward deformation, and drag. The calculation is idealized and two-dimensional, so it establishes a mechanism and transfer warning rather than quantitative universal behavior.

These results also clarify apparent disagreement between shock-derived and detonation-derived breakup descriptions. The cases are not definition-compatible simply because their leading Mach values match. The reacting post-wave state is part of the load. Inert-shock correlations should be transferred only after matching the Mach definition and retaining chemistry, post-wave kinematics, pressure gradients, liquid, diameter, and event definitions.

FIG-08 therefore separates early leading-wave similarity from later history divergence. TAB-07 records the thermochemical state and all characteristic scales. This bounded comparison identifies valuable strong-wave physics while setting the conditions for the final transfer audit to HPDI.

## Bounded transfer from strong-wave analogues to HPDI

[FIG-08 ABOUT HERE]

[TAB-07 ABOUT HERE]

Detonation and RDE evidence is a bounded strong-wave analogue for HPDI, not application proof. The domains share useful physical variables—compressible pressure and velocity histories, relative Mach context, droplet size, aerodynamic loading, evaporation, and finite residence—but differ in chemistry, geometry, wave scale, post-wave state, population state, and characteristic-length definitions [[CITE:D009]] [[CITE:D018]] [[CITE:D019]]. Shared terminology does not establish dynamic similarity.

The most defensible transfer is mechanistic. Strong reacting waves show that post-wave thermochemistry and pressure-gradient history can make leading Mach an incomplete descriptor; droplet position relative to a wave changes thermal and kinematic impulse; and evaporation-to-wave scale ratios can influence wave stability within their defined device. These results identify variables and failure modes that HPDI measurements or models should retain.

Quantitative transfer would require a validated mapping of pressure, density, velocity, chemistry, loading duration, droplet and fragment distributions, and residence scales. RDE (L_E/L_D) cannot be mapped directly to HPDI ignition because its detonation-height or reaction-scale denominator has no demonstrated engine-equivalent. Similarly, a detonation breakup time cannot substitute for a pilot-spray response when the post-wave flow and collective state differ.

FIG-08 encodes all within-domain strong-wave arrows as direct or model-resolved and places an analogue-only boundary before HPDI. TAB-07 provides the definition audit, while FIG-09 and TAB-08 retain the resulting research need. The existing component evidence supports qualitative hypothesis generation and model stress-testing, but direct HPDI validation is absent.

Chapter 8 therefore contributes a constrained comparison rather than an additional closure. Its evidence strengthens the argument that loading history and thermochemical state matter, while leaving the four HPDI discontinuities untouched. The final chapter can now reassemble the full chain by evidence status, specify what is missing at each break, and derive targeted priorities.

# CH09 — Integrated Mechanistic Framework, Evidence Gaps, and Research Priorities

## Closed components and unclosed cross-scale pathways

[FIG-09 ABOUT HERE]

The reviewed mechanism chain is coherent but not closed end to end. Several components are strongly or moderately supported within declared domains. Definition-complete injector history organizes transient underexpanded-wave formation; compatible states support Mach-disk and topology trends [[CITE:B009]] [[CITE:B021]]. Specified compressible loading produces internal wave response, deformation, instability, and staged fragmentation [[CITE:C007]]. Ordered droplets and dilute clouds directly demonstrate shielding, channel interaction, and shock attenuation. Fragment and thermal states condition transport and phase change. In HPDI-relevant systems, chronology, geometry, mixture preparation, and pilot-product interaction directly govern ignition and heat-release behavior [[CITE:A007]] [[CITE:A011]].

Four discontinuities prevent these components from becoming one measured causal chain. First, gas-phase shock topology has not been mapped to the local loading history of actual HPDI pilot droplets. Second, isolated and ordered canonical mechanisms have not been quantitatively validated for a dense, polydisperse, evaporating, reacting pilot spray. Third, shock-created fragment and vapor populations have not been followed into a measured HPDI mixture field. Fourth, a shock-caused mixture change has not been shown to produce a measurable ignition or combustion response. These are separate missing links: evidence downstream of one gap cannot close its upstream neighbor.

The distinction between evidence strength and application directness is central. A canonical experiment may offer strong direct evidence for a local mechanism and still have low HPDI directness. Conversely, an engine correlation may be highly application-relevant while offering limited causal isolation. RDE and detonation studies add strong-wave insight but remain analogue-only. FIG-01 summarizes the physical progression once; FIG-09 reorganizes it by direct, mixed/indirect, cross-scale, and missing support.

This map also prevents two common overclosures. Breakup is not equivalent to evaporation or mixture improvement, and timing-controlled ignition is not evidence of an upstream shock cause. The corpus supports these neighboring relations separately, but not the continuous shock-induced breakup–evaporation–mixture–ignition sequence [[CITE:A007]] [[CITE:A011]] [[CITE:C024]].

The synthesis contribution is therefore not a claim that one universal mechanism has been proved. It is an auditable separation of resolved local physics, bounded transfer, and unmeasured application arrows. That structure converts the gaps into specific diagnostic requirements rather than a generic request for more data.

## Evidence-derived research priorities and diagnostic requirements

[TAB-08 ABOUT HERE]

The highest-priority experiment is a co-located topology-to-loading measurement under HPDI-relevant chronology and geometry. Time-resolved injector or nozzle pressure, contextual NPR, shock position or density-gradient fields, local gas velocity, and pilot-droplet size and velocity must share one event clock and coordinate system. This would close the first discontinuity by replacing inferred loading with the pressure, relative velocity, and duration actually experienced by the liquid. Reporting storage, inlet or stagnation pressure, ambient pressure, absolute/gauge basis, and transient state is part of the experiment, not metadata.

The dense-spray transfer requires population-resolved validation. Experiments or high-fidelity simulations should retain realistic size and spacing distributions, turbulence, ambient thermodynamic state, phase change, and reaction where relevant. Outputs must include time-resolved fragment size, velocity, spacing, and mass distributions with uncertainty and detection limits. Such data would test which canonical shielding, squeeze-flow, channel-closure, and attenuation mechanisms survive in a disordered pilot spray and would provide the product state needed by transport models.

Closing the two downstream application links requires synchronized species and combustion diagnostics. The same case should follow local shock loading through fragmentation and evaporation into a pre-ignition mixture or species field, then resolve ignition location and delay and subsequent heat release. A controlled comparison must separate shock-mediated changes from mass-flow, momentum, timing, and geometry effects. Without this isolation, a faster ignition event remains a correlation with the injection setting rather than proof of shock-enhanced atomization.

Definition standardization supports all three priorities. Weber, Reynolds, and Ohnesorge numbers should report every component; Mach must be assigned to the incident wave, post-wave gas, jet, or relative motion; and loading intervals must name their start and end events. The possible τ_loading/τ_response ratio is a project hypothesis that may help design such comparisons, but its time scales require mechanism-specific definition and validation before it can be treated as an organizing parameter.

Secondary priorities address boundaries rather than new mechanism arrows. Matched thermal studies should separate vapor-layer or Stefan-flow shear reduction from heating-induced surface-tension change. RDE comparisons require a validated nondimensional mapping before their characteristic scales can inform HPDI quantitatively. Realistic engine work needs synchronized pressure, velocity, species, droplet, and heat-release diagnostics and model validation under swirl, wall, and turbulence conditions. The unavailable C004 source remains a source-availability limitation on broad breakup taxonomy; acquiring and processing the original PDF would improve coverage but does not constitute a new physical gap.

TAB-08 links each need to a discontinuity, measurement set, and validation target, while FIG-09 shows the order in which the measurements close the chain. This staging makes the research program falsifiable: each study is designed to resolve a named arrow or definition, not merely to add another operating point.

## Conclusions and review contributions

The literature provides a strong basis for several component mechanisms. Injector pressure build-up and chronology create a transient underexpanded-wave environment that cannot be represented by nominal pressure or steady NPR alone. Definition-complete compressible loading organizes droplet deformation and breakup through internal waves, aerodynamic forcing, and competing instabilities. Ordered droplets and clouds show direct collective effects, while fragment populations and thermal state mediate transport and phase change. HPDI studies directly establish that injection chronology, geometry, mixture preparation, and pilot-product interaction control ignition and combustion within condition-specific boundaries.

These results do not validate the complete application chain. The shock-topology-to-pilot-loading, canonical-to-dense-spray, shock-fragment-to-mixture, and shock-caused-mixture-to-ignition pathways remain open. The review therefore does not conclude that an underexpanded shock breaks the pilot, improves evaporation and mixing, and shortens ignition. It concludes that component evidence makes parts of that sequence physically plausible and defines the measurements required to test it.

The review's first contribution is mechanism unification without evidence flattening: injection, strong-wave gas dynamics, liquid response, collective effects, fragments, phase change, mixture preparation, and ignition are placed in one progression while each arrow retains its support level and application distance. The second is definition discipline for NPR, Mach context, Weber/Reynolds/Ohnesorge components, loading duration, breakup events, signed injection timing, and characteristic-scale ratios. The third is explicit separation of direct evidence, mixed or indirect support, cross-scale inference, and absence.

The fourth contribution is to identify collective and fragment-population state as necessary mediators between canonical breakup and engine mixture formation. A regime label or mean diameter cannot substitute for an evolving population, and a dilute-cloud mechanism cannot be transferred to a dense reacting spray without validation. The fifth is an evidence-derived research program centered on synchronized, definition-complete diagnostics rather than generic data accumulation.

Detonation and RDE evidence remains a bounded analogue whose value lies in strong-wave mechanisms and transfer warnings, not HPDI proof. C004 remains unavailable, and the project-level τ_loading/τ_response concept remains a possible organizing metric rather than an established nondimensional parameter. With those boundaries retained, the synthesis resolves what the corpus can support and makes its most important absences scientifically usable. Final abstract formulation, figure production, table population, quantitative eligibility auditing, and publication-level integration remain for later phases.
