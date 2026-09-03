# Phase 13R Physics-Led Working Draft

Status: reconstructed working manuscript

Abstract: pending later phase

# CH01 — Introduction and Review Scope

## High-pressure injection, pilot sprays, and ignition coupling

High-pressure gaseous injection can produce a transient underexpanded jet on a time scale comparable to pilot-spray development and ignition preparation. Expansion waves, a barrel shock, a Mach disk, reflected shocks, and vortical shear layers create strongly nonuniform pressure, density, and velocity in the same region where liquid droplets accelerate, deform, fragment, evaporate, and mix. If these processes overlap, wave-induced changes in the pilot may alter the local mixture presented to the ignition chemistry.

Each part of this sequence has been studied in depth, but usually in a different physical configuration. Gas-jet experiments and simulations resolve shock cells, penetration, and mixing without liquid droplets [[CITE:B009]] [[CITE:B021]]. Shock-tube studies impose planar waves on isolated droplets or dilute clouds and reveal internal-wave motion, instability, fragmentation, and evaporation [[CITE:C007]] [[CITE:C016]] [[CITE:C024]]. Engine and constant-volume studies vary pilot/main timing, jet angle, pressure, and operating state to identify mixture and ignition responses [[CITE:A007]] [[CITE:A011]]. The variables at the interfaces between these configurations are less often measured together.

The coupling matters because time-scale ordering can change the role of the pilot. A short compression may accelerate small droplets but end before larger droplets deform. Breakup may increase area, yet the fragments must heat, evaporate, and mix before the ignition delay expires. Pilot products can promote gaseous-fuel ignition through heat and radicals, while early gas-jet interaction can dilute or displace the pilot. The same nominal increase in injection pressure can therefore change shock structure, gas momentum, mixing rate, and ignition chronology simultaneously.

Four scientific questions organize the unresolved coupling. What pressure and relative-velocity history does a pilot droplet experience while crossing the moving shock system? Which isolated-droplet mechanisms survive inside a dense, polydisperse spray whose wakes and fragments modify the load? Under what conditions do shock-created fragments change the vapor and equivalence-ratio field before ignition? Can that change be separated from the effects of injection timing, momentum, geometry, and chamber state?

This review connects high-pressure injection, compressible multiphase loading, secondary breakup, phase change, mixture formation, and pilot-assisted ignition through their governing variables and time scales. Detonation and rotating-detonation studies are used as a separate strong-wave comparison domain. The aim is to identify the mechanisms that can already be connected physically, the conditions under which those connections change, and the measurements needed to determine whether wave–droplet coupling materially affects HPDI ignition.

## Scope and physical comparison framework

[TAB-01 ABOUT HERE]

The review spans transient high-pressure gas injection, underexpanded shock structures, shock–droplet and shock–cloud interaction, secondary breakup, fragment transport, phase change, HPDI mixture preparation, and pilot-assisted ignition and combustion. Single droplets, ordered pairs, dilute clouds, dense sprays, engines, and detonation devices are treated as distinct physical configurations rather than interchangeable realizations of one flow.

Several familiar parameters require explicit physical definitions. NPR identifies the upstream and downstream pressure roles, their absolute or gauge basis, and the transient state. Mach number may describe a jet, incident shock, post-shock stream, droplet-relative flow, or detonation front. Weber, Reynolds, and Ohnesorge numbers retain their density, velocity, length, viscosity, and surface-tension references. Loading duration distinguishes front passage from residence in the post-wave stream, and injection timing retains fuel order and the events used to define start of injection. TAB-01 concentrates these definitions so that later comparisons repeat them only when they change the interpretation.

Primary experiments and simulations are used to describe mechanisms within their tested geometry and state. Review articles provide terminology and broader context, while detonation and RDE studies inform strong-wave physics without replacing HPDI measurements. Cross-domain comparisons are made through shared local variables—pressure, density, relative velocity, size, thermal state, residence time, mixture composition, and ignition delay—rather than through identical symbols alone.

This approach permits strong physical synthesis without assigning causality beyond the measured sequence. A canonical droplet experiment can reveal how instability develops under a specified load; an engine experiment can reveal how timing changes ignition. Connecting the two requires the local loading, fragment, vapor, and mixture histories that both experiments do not individually provide.

## From injector dynamics to ignition

[FIG-01 ABOUT HERE]

FIG-01 follows the physical sequence from injector opening to combustion while marking the quantities transmitted between stages. Injector motion and (p_{inj}(t)) create a developing underexpanded jet. The shock and vortex field supplies local pressure, density, velocity, and loading duration. These variables drive internal liquid waves, acceleration, deformation, and instability; breakup then creates a population whose size, velocity, and temperature govern transport and evaporation. Vapor and pilot products finally enter the mixture and chemical induction processes that form an ignition kernel.

Chapters 2 and 3 develop the gas dynamics and the load sampled by a moving droplet. Chapters 4 and 5 follow single-droplet response and the redistribution of loading by neighbors and clouds. Chapter 6 tracks fragments, phase change, and vapor transport. Chapter 7 examines the directly observed roles of chronology, jet interaction, pilot products, and mixture state in ignition and heat release. Chapter 8 compares reacting strong-wave systems, and Chapter 9 integrates the competing time scales and measurement requirements.

The sequence is physically continuous, but several connecting quantities have not been measured under one HPDI condition. FIG-01 uses these missing variables to prevent a schematic arrow from implying a completed causal chain. The discussion begins with the upstream boundary: the pressure, nozzle, gas, ambient, and opening history that determine how an underexpanded shock system forms.

# CH02 — High-Pressure Injection and Transient Underexpanded-Wave Formation

## Injection and ambient conditions governing underexpansion

Underexpansion begins when the gas leaving a nozzle must continue expanding after the exit to approach the surrounding pressure. The upstream state that drives this process is not a single pressure label. It includes the stagnation or nozzle-inlet pressure available to accelerate the gas, the chamber pressure opposing the discharge, the gas temperature and thermodynamic model, and the losses and geometry that determine the exit state. Once the flow chokes, downstream pressure disturbances can no longer communicate through the throat to regulate the mass flux. Expansion waves then turn and accelerate the gas outside the nozzle, while recompression organizes the barrel shock, Mach disk, reflected shocks, slip lines, and subsequent cells.

The nozzle pressure ratio is useful only when its two pressures describe the same physical roles. A storage-to-ambient ratio, a rail-to-chamber ratio, and a reconstructed stagnation-to-static ratio can have equal numerical values while producing different nozzle-exit states. The absolute or gauge basis and the instant at which each pressure is sampled are equally important during an injection event. TAB-01 collects these definitions so that later sections can focus on the physics rather than repeat the bookkeeping.

Pressure ratio changes both the rate at which momentum enters the chamber and the degree of external expansion. Within a fixed nozzle and a consistent pressure definition, stronger underexpansion generally enlarges the shock-containing near field. Penetration and entrainment are less simply ordered because they also respond to ambient density, jet spreading, transient development, and nozzle geometry. Experiments and simulations consequently show pressure-driven changes in penetration and occupied volume without a geometry-independent monotonic law [[CITE:B006]] [[CITE:B009]] [[CITE:B015]]. At fixed contextual NPR, changing chamber pressure, density, or temperature alters the jet's acceleration, diffusion, and lateral growth; holding injection pressure fixed instead changes NPR at the same time and creates a different comparison [[CITE:B021]] [[CITE:B028]] [[CITE:B011]].

Nozzle diameter, passage shape, and the arrangement of neighboring holes determine where expansion fans meet the shear layer and how rapidly coherent structures grow. Non-circular exits and closely spaced jets can redistribute pressure and entrainment, bend adjacent jets, or merge their outer shear layers [[CITE:B022]] [[CITE:B028]]. These geometric changes act together with gas density, speed of sound, viscosity, and real-gas behavior. A recognizable barrel shock can therefore persist while the exit velocity, centerline density, and mixing field shift appreciably with the equation of state or nozzle representation [[CITE:B008]] [[CITE:A028]].

The initial condition for transient jet development is thus a coupled thermofluid state: nozzle geometry and opening area, gas composition and temperature, upstream pressure history, and chamber pressure and density. Once the injector begins to open, each of these quantities can evolve on the same time scale as the shock system itself.

## Injector opening and transient jet formation

[FIG-02 ABOUT HERE]

The first shock cells form while the injector is still changing its effective flow area and upstream pressure. Needle or valve motion first admits a small mass flow, after which the nozzle accelerates toward a choked state and the external jet passes through developing subsonic, shock-cell, and Mach-disk configurations. The resulting wave pattern is therefore tied to the history of valve lift, pressure build-up, and chamber pressure rather than to the final rail-pressure plateau.

During this developing interval, expansion and recompression fronts propagate through gas that was injected under earlier boundary conditions. The Mach disk can appear, move downstream, overshoot its later location, and then retreat or stabilize as the nozzle flow and surrounding jet adjust. LES of a small hydrogen nozzle, for example, resolved the first disk tens of microseconds after injection began and a later semi-steady structure, with early disk dimensions exceeding their settled values [[CITE:B009]]. Transient experiments and simulations with different injector designs likewise separate formation, instantaneous, and stabilized shock positions [[CITE:B014]] [[CITE:B018]] [[CITE:B021]].

The time origin matters because a command signal, initial needle lift, first detectable mass flow, and first optical appearance are not simultaneous. Aligning data to different events shifts the apparent formation time and can make two otherwise similar jets seem dynamically different. Pressure also needs a location: rail pressure may remain nearly constant while the nozzle-inlet pressure rises or oscillates, particularly when internal volumes and valve restrictions are important [[CITE:B013]] [[CITE:B017]] [[CITE:B029]]. The shock system responds to the pressure and area actually presented to the nozzle, not to the nominal set point.

Choking marks the transition to an underexpanded discharge when the pressure ratio exceeds the critical value for the specified gas and stagnation state. A hydrogen-release study describes the associated nonuniform exit velocity and complex shock structure above its reported critical ratio [[CITE:B007]]. The numerical threshold from that configuration should remain attached to its gas model and pressure definition; real injectors add internal losses and a continuously changing area. What carries across configurations is the sequence: opening increases mass flux, the throat reaches a sonic state, external expansion strengthens, and the barrel-shock/Mach-disk system grows toward a state determined by the instantaneous boundary.

FIG-02 summarizes this event-aligned evolution from injector motion and (p_{inj}(t)) to choking, shock formation, overshoot, and stabilization. The key consequence for downstream multiphase physics is that a droplet or pilot jet entering during formation can encounter a different pressure and velocity field from one entering after the shock cells have settled.

## Mach-disk and shock-cell evolution

[TAB-02 ABOUT HERE]

Once a strongly underexpanded jet forms, Prandtl–Meyer expansion at the nozzle lip accelerates the gas and lowers its static pressure. The surrounding barrel shock turns the expanding stream back toward the axis, and sufficiently strong compression produces a Mach disk that decelerates the core through a near-normal shock. Reflected shocks, triple points, slip lines, and repeated expansion–compression cells then structure the near field. Their location controls where pressure, density, velocity, and turbulent shear change most abruptly.

For a fixed nozzle and consistent pressure roles, increasing NPR moves the Mach disk downstream and usually enlarges it [[CITE:B003]] [[CITE:B009]] [[CITE:B021]]. The square-root-type position scalings often used for steady jets capture this direction, but transient overshoot and injector-specific exit conditions change the instantaneous coefficient. Disk diameter, curvature, appearance threshold, and cell wavelength are less consistently constrained than axial position [[CITE:B004]]. TAB-02 therefore separates the geometric feature, nozzle-diameter basis, and developing or settled state for every comparison. The case-level audit retained one definition-complete numerical sequence for plotting: within the B009 semi-steady hydrogen series, NPR values of 8.5, 10, 30, and 70 correspond to derived `x_MD/D` values of 1.85, 2.06, 3.77, and 5.81, respectively; the methane case at NPR 8.5 gives 1.90 under the same nozzle and ambient state [[CITE:B009]]. This is a within-study trend, not a cross-paper coefficient.

Gas species changes more than molecular diffusion. At matched NPR, hydrogen and methane can produce similar gross first-cell dimensions while differing in local density, speed of sound, specific-heat ratio, exit turbulence, and downstream instability. Simulations report hydrogen mixing upstream or near the Mach disk under conditions where methane remains more sharply segregated, followed by different potential-core and shock-cell development [[CITE:B009]] [[CITE:B010]] [[CITE:B011]]. These coupled property changes explain why equal NPR does not create identical velocity or scalar fields.

Farther downstream, repeated shocks weaken and turbulent mixing progressively erases the cell structure. Equivalent-jet or notional-nozzle models attempt to replace the unresolved shock-containing region with an effective source for the far field. Their utility depends on where the source is placed and whether mass, momentum, enthalpy, and the relevant decay behavior survive the replacement [[CITE:B001]] [[CITE:B019]] [[CITE:B020]]. A model calibrated for a sonic exit or one gas can misplace the transition between the shock-dominated near field and the mixing-dominated far field.

The gas-dynamic sequence is therefore well defined within a specified injector and ambient state: expansion builds a supersonic core, recompression creates the Mach disk and cells, and turbulent shear eventually dominates downstream. The next physical question is no longer where these structures appear, but what pressure and relative-velocity history they impose on liquid moving through them.

# CH03 — From Shock Topology to Local Multiphase Loading

## Wave and vortex structures as sources of local forcing

The barrel shock, Mach disk, reflected shocks, slip lines, and coherent vortices divide an underexpanded jet into regions with different pressure, density, velocity, and flow direction. A liquid element entering this field does not respond to the visible topology itself; it responds to the sequence of gas states encountered along its trajectory. Compression raises pressure and density abruptly, expansion lowers them, and shear layers and vortices continuously rotate and modulate the relative velocity. The aerodynamic load therefore varies in both magnitude and direction even when the global jet boundary is steady.

Near the Mach disk, a supersonic core is decelerated and compressed over a short axial distance. A droplet crossing this region can experience a rapid pressure impulse followed by a large velocity slip with the post-shock gas. A droplet travelling outside the disk may instead cross an oblique barrel shock or a shear layer, producing a weaker compression but a longer transverse-velocity history. Downstream reflected shocks and vortex rings can repeat or redirect the loading. Numerical studies link these structures to cone-angle and mixing changes, while also showing that nozzle geometry, gas species, and baroclinic vorticity alter the local field [[CITE:B027]].

Waves generated by a spray have a different origin. If the nozzle-exit or near-tip motion outruns the local acoustic speed during the injection-rate ramp, compression waves can coalesce into attached or detached shocks. Raising ambient temperature increases the sound speed, while increasing ambient density decelerates the spray; both effects can suppress shock formation under hot, dense engine conditions [[CITE:D001]] [[CITE:D002]] [[CITE:D005]]. Nozzle-exit velocity, spray-tip velocity, and the velocity of individual droplets must remain separate because each enters a different part of this sequence.

Reflected-wave experiments reveal how strongly the direction and timing of a wave matter. A reflected shock that intersects an already-developed spray reduces radial growth, cone angle, volume, and entrainment while changing axial tip penetration much less [[CITE:D004]]. The wave compresses and redirects the surrounding gas after the spray has acquired its own momentum and internal structure. This behavior cannot be reproduced simply by assigning the same Mach number to an injector-generated near-nozzle shock, because the direction of propagation and the age of the spray are different.

FIG-03 summarizes the conversion from wave geometry to the fields that act on liquid: (p(x,t)), ρ(x,t), (u(x,t)), vorticity, and their gradients. The relevant input for droplet dynamics is obtained only after these Eulerian fields are sampled along a liquid trajectory. That Lagrangian conversion is the central problem of the next section.

## From transient shock structures to pilot-spray forcing

[FIG-03 ABOUT HERE]

A pilot droplet crossing a transient underexpanded jet encounters a history rather than a single shock strength. Its path may intersect an expansion fan, barrel shock, Mach disk, slip line, or vortex-dominated shear layer while both the wave system and the droplet are moving. At each instant, the aerodynamic slip is `u_rel(t) = u_g[x_d(t),t] - u_d(t)`, and the associated dynamic load scales with `ρ_g u_rel²`. The pressure acting on the windward surface also changes discontinuously across compression waves. Droplet inertia then feeds back into the history: small droplets accelerate toward the local gas velocity more quickly, whereas large droplets preserve slip for longer.

Gas-jet calculations resolve the motion and size of Mach disks and shock cells under changing pressure ratio [[CITE:B009]] [[CITE:B021]]. Canonical shock–droplet experiments prescribe an incident wave and then image the transmitted wave, early pressure redistribution, and airflow-driven deformation [[CITE:C007]] [[CITE:C016]]. These two experimental designs isolate different parts of the same physical sequence. The first gives an Eulerian gas field without liquid trajectories; the second gives liquid response to a comparatively controlled load without the evolving injector geometry and wave topology of HPDI.

Reconstructing pilot-spray forcing requires both descriptions in one coordinate system. Time-resolved density or pressure imaging must locate the moving wave surfaces; velocimetry or validated compressible-flow calculations must recover the post-wave velocity; and droplet or ligament tracking must provide (x_d(t)), (u_d(t)), and size. The resulting histories should distinguish pressure impulse from aerodynamic drag, because the shock front can traverse the droplet long before the post-wave slip decays. They should also preserve the direction of the load: crossing a barrel shock obliquely produces a different deformation tendency from passing through the near-normal Mach disk.

Multiphase feedback complicates the reconstruction. A dense pilot spray can attenuate a wave, alter local density through vaporization, and create wakes that redistribute velocity. The gas field measured without liquid may therefore differ from the field that loads the liquid. Hot chamber conditions can additionally weaken or remove spray-generated shocks even when a cold-vessel experiment displays them [[CITE:D001]].

No current HPDI measurement combines these quantities with sufficient spatial and temporal resolution to recover the complete Lagrangian load. The unresolved scientific quantity is consequently precise: `p[x_d(t),t]`, `ρ_g[x_d(t),t]`, `u_rel(t)`, and the duration of each compression, expansion, and shear-dominated interval for the actual pilot-droplet population. This missing history, rather than the existence of shock cells, limits predictions of wave-driven pilot breakup.

## Loading magnitude, duration, and liquid response scales

A pressure jump initiates droplet motion, but continued deformation depends on how long the post-wave gas maintains a velocity relative to the liquid. Four intervals must be distinguished: passage of the compression front, residence in the compressed gas, termination or reversal by an expansion wave, and the longer period over which the droplet accelerates and deforms. These intervals can differ by orders of magnitude and excite different responses.

Jet-induced-wave measurements provide a clear example. The compression front is followed closely by an expansion wave, leaving a thin shocked region with only a finite time to transfer momentum. In the associated model, small droplets accelerate appreciably during this interval, whereas 50 μm droplets have a response time much longer than the roughly 60–100 μs shocked-state exposure [[CITE:D003]]. The front can therefore be detected optically without producing the sustained slip needed for large deformation of every droplet in the cloud.

Loading magnitude also requires a reference state. Incident-shock Mach controls the jump generated by the wave, while post-shock or droplet-relative Mach controls the subsequent gas–liquid motion. Weber number formed from post-wave density, relative velocity, initial diameter, and surface tension measures the ratio of aerodynamic to capillary stress, but it does not contain the duration of that stress. Reynolds number describes viscous transport in the gas, and Ohnesorge number measures the importance of liquid viscosity relative to inertia and capillarity. Equal Weber numbers can thus accompany different compressibility, viscous damping, and exposure histories.

The liquid introduces its own clocks: acoustic transit and internal-wave focusing occur first, followed by acceleration, global deformation, instability growth, sheet or ligament formation, and final fragmentation. A short impulse may move the center of mass while ending before an interfacial instability grows appreciably; a longer post-wave stream can sustain shear until stripping or piercing begins. TAB-01 defines the time and dimensionless quantities used in these comparisons.

The comparison suggests that the ratio between the duration of an imposed aerodynamic load and a characteristic liquid response time may provide a useful organizing concept. The numerator could be expansion-limited exposure or another explicitly bounded forcing interval, while the denominator must match the process of interest—acceleration, deformation, capillary response, or instability growth. This ratio has not been established as a universal dimensionless parameter.

With pressure, velocity, density, and duration specified, the analysis can move from the gas field to the liquid. The first response occurs inside the droplet, where compression waves refract, focus, and generate circulation before the external flow has produced mature sheets or ligaments.

# CH04 — Compressible Droplet Deformation, Instability, and Secondary Breakup

## Governing parameters of compressible droplet response

[FIG-04 ABOUT HERE]

[TAB-03 ABOUT HERE]

When a shock passes a droplet, the liquid first receives a pressure impulse and then experiences aerodynamic loading from the post-shock stream. The latter scales with gas density, relative velocity, and droplet diameter, but the response also depends on liquid inertia, viscosity, surface tension, and the time available for deformation. Weber number captures the ratio of aerodynamic to capillary stress; Reynolds number measures gas-side viscous transport; Ohnesorge number measures liquid viscous damping; and the density ratio controls how quickly the liquid accelerates relative to the gas. None of these quantities contains the entire compressible history.

Mach number introduces an independent influence because it changes shock jumps, pressure distribution around the deformed body, and the development of the surrounding bow shock and shear layer. At approximately fixed Weber number near 1100, experiments found substantial changes in morphology and breakup time as the post-shock freestream Mach number increased: peripheral mist, multiple bags, and leeward ligament structures appeared under different cases, while flattening and sheet growth weakened at higher Mach [[CITE:C014]]. Gas identity, Reynolds number, and density ratio also varied, so the comparison isolates a strong Mach-context dependence without reducing it to a single compressibility coefficient.

Droplet diameter changes both the capillary response time and the interfacial wavelengths that can grow on the deformed surface. Shock-tube observations show that small and large droplets can select different breakup modes at overlapping Weber numbers; Rayleigh–Taylor piercing persisted near a reported We of 800 for smaller droplets, whereas shear-induced entrainment appeared near We of 200 for larger droplets [[CITE:C016]]. The ratio of droplet diameter to the preferred Kelvin–Helmholtz wavelength helps explain why a scalar We threshold shifts with size.

Compressibility also acts differently at different stages. Numerical and experimental comparisons report altered transverse spreading and morphology across supersonic conditions, while early normalized acceleration or drift may remain closer across a narrower sonic transition [[CITE:C008]] [[CITE:C007]]. Mach 2 and Mach 3 simulations likewise produced similar early displacement and spreading but different later piercing and ligament structures, which ties the apparent similarity to response stage rather than to the full breakup history [[CITE:C025]]. Early center-of-mass motion, global flattening, sheet formation, and final fragmentation are therefore not interchangeable response metrics.

Regime maps remain useful for naming recurrent morphologies, provided that their Weber, Mach, liquid, and observation definitions remain attached to each boundary [[CITE:C002]]. They describe how a particular loading state develops; they do not replace that state with a context-free threshold.

FIG-04 organizes these variables around a sequence rather than a universal regime axis: pressure transmission and acceleration lead to deformation; deformation establishes interfacial geometry; and shear, acceleration, capillarity, and viscosity determine which disturbances grow. TAB-03 retains the Mach frame, reference density and velocity, diameter, liquid state, and loading interval needed to compare those stages.

## Internal wave motion and early deformation

The incident shock does not simply apply an external pressure step. Part of the wave reflects into the gas, while a transmitted compression enters the liquid and refracts over the curved interface. Subsequent reflections and rarefactions create an internal wave envelope whose geometry depends on acoustic impedance, the ratio of sound speeds, droplet curvature, and incident-shock strength. The windward and leeward surfaces can therefore experience different pressure extrema before appreciable bulk deformation occurs.

High-fidelity calculations show that internal expansion-wave focusing contributes to a negative-pressure region, but the total pressure history also includes relaxation, fluctuation, and Mach-stem effects [[CITE:C018]]. At low wave-speed ratios, the predicted focus and minimum-pressure location can be close; at higher ratios they separate, so focusing alone no longer locates the pressure minimum or a potential cavitation site. This distinction is important because a localized tensile region may seed internal damage even while the external gas begins to flatten the droplet.

Near transcritical conditions, thermodynamic state changes the liquid sound speed and hence the direction of refraction. Calculations of n-dodecane in nitrogen show a transition between diverging and converging transmitted shocks as the sound-speed ratio crosses unity. Strong convergence creates a focal pressure peak and an axial jet, while baroclinic torque deposits circulation where pressure and density gradients are misaligned [[CITE:C029]]. Increasing shock strength then alters both the circulation and the pressure-gradient-driven deformation. These early mechanisms occur before a mature breakup cloud forms.

The curvature of the imposed wave adds another geometric control. A divergent shock changes the normal and tangential components of loading over the interface and moves the point at which internal and external structures interact. In two-dimensional calculations, this shift moved ligament inception toward the windward side and sustained greater spanwise extension than a planar shock [[CITE:C019]]. Because viscosity, capillarity, phase change, and three-dimensional curvature were omitted, the result identifies how wave geometry redirects early deformation rather than predicting final fragments.

Internal pressure and circulation set the initial condition for the slower aerodynamic stage. Once the post-wave gas maintains a velocity relative to the liquid, the droplet flattens, its rim and sheets are stretched, and disturbances grow on surfaces already shaped by the internal-wave history. The transition from wave-controlled response to airflow-controlled instability is therefore continuous even though the dominant time scales differ.

## Competing instabilities and the breakup cascade

As the post-shock stream accelerates around the liquid, the windward surface flattens and the equatorial region stretches into a rim or sheet. Acceleration of the dense liquid by the lighter gas promotes Rayleigh–Taylor growth, while velocity discontinuity along the interface drives Kelvin–Helmholtz waves and shear stripping. Capillary pressure resists the creation of area and retracts thin sheets; liquid viscosity damps small-scale motion; and the wake changes both pressure and the direction of shear. Breakup morphology emerges from the competition among these processes rather than from a single instability acting everywhere.

At moderate loading, capillary rim retraction can preserve a bag-like structure, whereas stronger downstream shearing promotes multibag or shear-dominated breakup [[CITE:C005]]. Supersonic calculations reproduce bag, bag-stamen, and multimode structures and relate their development to acceleration-driven instability within the simulated Weber range [[CITE:C009]]. These mode names describe the dominant visible topology, but the liquid can pass through several local mechanisms during one event.

At higher loading, the cascade becomes explicitly multiscale. Global flattening produces a thin sheet; waves corrugate that sheet; holes and rims form; rims stretch into ligaments; and ligaments retract and fragment into daughter droplets. High-magnification shadowgraphy resolves sheets, ligaments, and small droplets that conventional imaging merges into a diffuse cloud [[CITE:C012]]. Three-dimensional simulations and experiments further show recurrent ligament formation after sheet rupture. The first shedding event is only weakly sensitive to Weber number over the studied range, whereas later events are increasingly governed by liquid inertia and wake-vortex dynamics [[CITE:C013]].

This staged behavior explains why “breakup time” depends on the chosen event. Time to first sheet rupture, first ligament shedding, windward piercing, loss of the parent core, and optical disappearance are different clocks. Simulations at two shock Mach numbers show similar early normalized deformation but different piercing and atomization histories, with the resulting fragment distributions changing as the cascade proceeds [[CITE:C025]].

The useful organizing picture is therefore a sequence of coupled scales: parent acceleration and flattening establish the geometry; RT and KH disturbances amplify on that geometry; capillary retraction and wake motion select sheet and ligament evolution; and secondary fragmentation creates the population transported downstream. A universal We-only boundary would collapse these distinct stages and their Mach, size, viscosity, and loading-duration dependence.

## Predictive limits of breakup regimes and reduced models

Breakup models differ mainly in which part of the sequence they approximate. Spring–mass–damper analogies represent global deformation; instability models estimate growth or stripping rates; stochastic or population models prescribe daughter sizes; and interface-resolved methods calculate sheets and ligaments directly at much higher cost. A model that predicts projected width can therefore fail to predict the onset of piercing, and a model that assigns the correct regime can still produce an incorrect surface-area history.

This distinction becomes critical downstream. Momentum exchange depends on acceleration and projected area, evaporation depends on fragment size, temperature, and total surface area, and cloud attenuation depends on the evolving spatial distribution. Validation against only one of these quantities leaves the others unconstrained. Existing comparisons show that no single reduced formulation has reproduced deformation history, intermediate morphology, daughter-size statistics, cloud length, evaporation, and phase coupling over the full aerodynamic-breakup range [[CITE:C006]].

The Taylor Analogy Breakup model has reproduced deformation in a source-specific calculation by treating the droplet as a damped oscillator [[CITE:C020]]. That success is physically consistent with a global restoring-force picture, but the same degrees of freedom cannot resolve internal shock focusing, local sheet rupture, recurrent ligaments, or a multimodal fragment distribution. Reduced models remain most useful when their output matches the question being asked and when the calibration range includes the relevant Mach, We, Oh, liquid, and forcing duration.

Regime maps have a similar role. They compress complex sequences into useful categories, but their boundaries inherit the velocity and density used in We, the Mach frame, initial diameter, liquid properties, and the observed breakup event. A map based on continuous airflow does not automatically apply to an expansion-limited shock pulse. Likewise, projected images and three-dimensional fragment statistics can assign different completion times to the same event.

The unavailable C004 source limits a broad treatment of Newtonian and viscoelastic taxonomy, so its primary conclusions are not reconstructed here from secondary descriptions. The available studies nevertheless define the central modeling requirement: downstream spray and combustion calculations need a time-dependent product state, not merely a parent-droplet regime label. Once multiple droplets are present, even the imposed load changes through wakes and wave attenuation, adding a second level of closure beyond single-droplet breakup.

# CH05 — Collective Droplet Effects and Canonical-to-Spray Transfer

## Wake shielding, squeeze flow, and channel closure

Two droplets exposed to the same incident shock need not experience the same aerodynamic history. Their relative position determines how the gas accelerated around one interface reaches the other. Tandem alignment places the downstream droplet inside the upstream wake; parallel alignment forces the gas through the narrowing channel between adjacent interfaces. Spacing therefore changes both the magnitude and direction of the local load, but by different mechanisms in the two geometries.

For tandem droplets, the lead droplet forms a wake with reduced mean velocity and altered pressure. A trailing droplet inside this region develops less slip, lower drag, and weaker cross-stream deformation. Experiments show delayed initial deformation and a smaller maximum width for the downstream droplet as normalized spacing decreases, while the leading droplet remains close to isolated behavior [[CITE:C035]]. The spacing over which this shielding persists also changes with Weber number because stronger loading shortens the time required for deformation and wake evolution.

Parallel droplets instead accelerate gas between their facing surfaces. At moderate separation, this squeeze flow changes the pressure distribution and can reverse the direction in which a flattened droplet bends. At smaller gaps and higher loading, equatorial filaments grow into the channel and can meet, temporarily closing the gas passage. Imaging shows closed and repeatedly reopening modes as the gap is reduced [[CITE:C036]]. The pair then behaves as a coupled obstacle whose effective shape evolves with both interfaces.

The contrast between these arrangements rules out a single universal spacing threshold. Reducing tandem spacing strengthens shielding and weakens the downstream load; reducing parallel spacing can intensify local channel flow before closure reorganizes it. Initial diameter, (S/D), alignment error, Weber number, and the duration of post-shock flow all determine which interaction develops. TAB-04 therefore keeps tandem, parallel, cloud, and dense-spray configurations separate.

These ordered systems reveal a general principle: neighboring liquid structures redistribute the gas field before they alter one another's breakup. In a cloud, the same feedback extends beyond a pair because the population extracts momentum from the wave and changes the forcing seen deeper downstream.

## Shock attenuation and feedback in droplet clouds

A shock entering a droplet cloud transfers momentum and energy to a large interfacial area. Pressure and velocity disturbances are scattered around droplets, while drag accelerates the liquid and reduces the gas momentum available to sustain the transmitted wave. If droplets deform or fragment, their total surface area grows and the coupling intensifies. The downstream population therefore experiences a wave that has already been modified by the upstream population.

Cloud experiments show that attenuation of peak overpressure and impulse varies with liquid volume fraction, droplet size, exchange area, shock strength, and breakup [[CITE:C033]]. These variables are not redundant. Equal volume fractions can be composed of many small droplets or fewer large ones, producing very different area per unit volume. A peak-pressure metric emphasizes the compression front, whereas impulse integrates the longer pressure history that drives acceleration.

Coupled calculations reproduce the characteristic transmitted-pressure history more accurately when fragmentation changes the effective exchange area. When breakup is omitted, the transmitted pressure is overpredicted under the tested dilute-cloud conditions [[CITE:C034]]. The mechanism is a feedback loop: shock loading creates fragments; fragments increase area and shorten aerodynamic response times; stronger interphase exchange then attenuates and reshapes the wave that loads the rest of the cloud.

Spatial heterogeneity follows naturally. Droplets at the front of a cloud see the strongest initial compression and generate wakes and fragments. Droplets farther downstream encounter a weaker, temporally broadened wave and a gas stream altered by upstream momentum extraction. Their breakup cannot be predicted by assigning one incident shock to every droplet. Local volume fraction, size distribution, cloud thickness, and sensor or droplet position must accompany any attenuation measurement.

FIG-05 summarizes the progression from isolated response to pair interaction and population feedback. Dilute clouds reveal the mechanism cleanly, but dense pilot sprays add rapid vaporization, broad size and velocity distributions, turbulence, collisions, and possible reaction. These features determine which pair- and cloud-scale processes remain recognizable in an injector spray.

## From canonical droplets to dense pilot sprays

[FIG-05 ABOUT HERE]

[TAB-04 ABOUT HERE]

An isolated droplet converts a specified gas history into one deformation and breakup history. A dense pilot spray contains a distribution of sizes, velocities, temperatures, spacings, and trajectories, so both the load and the response vary across the population. Small droplets accelerate rapidly and reduce their slip; large droplets preserve high relative velocity. Upstream structures create wakes, downstream structures are shielded, and adjacent interfaces can generate squeeze flow or channel closure. At the same time, collective momentum exchange attenuates the incident wave.

The canonical mechanisms remain physically relevant, but they operate locally and intermittently. A droplet that is momentarily exposed at the edge of a spray may resemble the isolated configuration. One in the core may travel in a low-slip wake; a close parallel neighbor may intensify lateral pressure gradients; and a fragment cloud may remove enough gas momentum to weaken the load downstream [[CITE:C035]] [[CITE:C036]] [[CITE:C033]] [[CITE:C034]]. A dense spray model must determine how often and where each local state occurs rather than select one canonical regime for the entire population.

Polydispersity couples these mechanisms across time. Large parent droplets deform slowly and shed ligaments, while small fragments accelerate, evaporate, and leave the region more rapidly. Their relative positions change, so a spacing distribution measured at injection is not the distribution present when the shock arrives. Turbulence broadens the trajectory and velocity distributions, and vaporization changes local density and temperature. In reacting surroundings, heat release and radical transport can alter the gas state before all liquid has fragmented.

The gas field must also be measured in the presence of liquid. Shock topology calculated for a gas-only jet [[CITE:B009]] [[CITE:B021]] cannot be sampled along a pilot trajectory without accounting for attenuation and vapor production. Conversely, applying an isolated-droplet correlation independently to every parcel suppresses the collective changes in pressure and velocity that create the local load.

The principal modeling state is therefore a joint distribution: droplet and fragment size, velocity, temperature, position, and liquid mass together with the local gas pressure, density, velocity, and composition. Existing ordered-pair and dilute-cloud studies identify the terms that must enter this state, but they do not yet determine their statistical weight in a dense, polydisperse, reacting HPDI spray. Following the population downstream requires the fragment distribution produced by breakup, which becomes the starting point for transport and evaporation.

# CH06 — Fragment Populations, Phase Change, and the Mixture-Formation Bridge

## Fragment populations and downstream transport

The output of secondary breakup is not a regime name but an evolving population of liquid structures. A parent droplet first produces sheets, rims, ligaments, and residual cores; these structures then fragment into droplets with different sizes, velocities, and positions. Number-weighted statistics emphasize the smallest products, area-weighted statistics emphasize structures important to heat and mass transfer, and mass-weighted statistics remain dominated by the largest remnants. A single mean diameter cannot describe all three roles.

Fragment velocity is coupled to size. Small droplets have short aerodynamic response times and rapidly approach the gas velocity, whereas large fragments preserve relative motion and continue to deform. This size-dependent acceleration stretches the cloud in the streamwise direction. Lateral velocity inherited from sheet and ligament motion broadens it transversely, while wakes and collisions change local spacing. Three-dimensional calculations show that size distributions and inter-fragment distances continue evolving after primary piercing and ligament shedding [[CITE:C025]].

Sampling time therefore changes the apparent product state. A distribution measured immediately after first rupture contains many connected or marginally resolved structures; later sampling includes capillary retraction, secondary ligament breakup, acceleration, and loss of small droplets through evaporation or diagnostic threshold. High-magnification studies resolve structures that coarser shadowgraphy records only as a diffuse edge [[CITE:C012]] [[CITE:C013]]. Detection limit, depth of field, and the definition of an independent fragment must accompany any comparison.

Transport models require at least the joint size–velocity distribution and its mass weighting. Evaporation models additionally need fragment temperature and surface area; cloud-interaction models need number density and spatial correlation. A model that reproduces parent flattening but assigns an incorrect daughter distribution can still predict the wrong cloud length, vapor release, and wave attenuation [[CITE:C006]].

FIG-06 follows these product variables from breakup into transport and phase change. The next question is temporal: do fragments survive long enough to travel as liquid, or do breakup and evaporation overlap before the mixture reaches ignition conditions?

## Coupled breakup, evaporation, and droplet survival

[TAB-05 ABOUT HERE]

Fragmentation changes evaporation primarily by redistributing liquid mass toward smaller length scales. For a fixed liquid volume, smaller droplets expose more surface area and have shorter thermal and momentum response times. They heat and accelerate rapidly, while larger remnants retain liquid mass and can survive far downstream. Whether this area growth matters before ignition depends on the ordering of breakup time, heating and evaporation time, residence time, and ignition delay.

Shock-tube measurements of a dilute acetone curtain resolve a sequence in which breakup occurs first, size-dependent acceleration stretches the cloud, and evaporation subsequently removes the dispersed children [[CITE:C024]]. Initial droplets in the micrometre range equilibrate much faster than the larger members of the distribution, so the cloud length reflects both parent drag and daughter sizes. An evaporation-only description cannot reproduce a cloud whose surface area and velocity distribution are being reset by fragmentation.

Liquid-fueled detonation experiments provide a reacting strong-wave example. The measured droplet-survival region is far shorter than evaporation-only calculations for the larger initial droplets, while breakup models create small children that vaporize rapidly [[CITE:D017]]. Some models remove liquid faster than observed because the actual post-wave acceleration varies and larger RT-scale fragments persist. The comparison shows why breakup and evaporation must be integrated over the same gas history rather than calculated as sequential equilibrium events.

Large-droplet early deformation can occupy a different ordering. For droplets larger than 100 μm observed over the early high-speed deformation interval, evaporation produced little measurable change in shape [[CITE:C026]]. The liquid had time to accelerate and deform but not to lose enough mass or alter its properties substantially. Smaller fragments or later stages from the same parent could still enter an evaporation-sensitive regime.

Locally supersonic relative motion adds a pressure effect. A bow shock raises the gas pressure at the windward side and changes the difference between liquid vapor pressure and surrounding pressure. Lower bow-shock pressure rise and higher volatility favor superheating and vaporization in the tested configurations [[CITE:C027]]. Relative Mach, thermal state, and liquid properties must therefore accompany any diameter-based survival argument.

TAB-05 organizes the required initial size, fragment distribution, gas temperature and pressure history, volatility, and observation interval. These variables determine whether breakup mainly changes liquid transport or materially changes vapor availability before ignition.

## Thermal and phase-change control of deformation

Phase change modifies droplet breakup through two competing routes. Vaporization creates mass flux away from the interface and can form a cool, vapor-rich layer that reduces gas-side shear. Heating simultaneously lowers surface tension for many hydrocarbons and can reduce the capillary stress resisting deformation. The observed direction depends on which route develops faster than the aerodynamic and instability time scales.

Three-dimensional shock–droplet simulations resolve the first route. In evaporation-dominated cases, a low-temperature vapor layer weakens near-interface velocity gradients and suppresses Kelvin–Helmholtz wave growth; condensation-dominated cases sustain stronger shear, greater flattening, sheet stretching, and ligament formation [[CITE:C031]]. Phase change also introduces additional compression or rarefaction structures in the coupled Riemann response. The result depends on manually selected evaporation and condensation coefficients, but it shows how mass and heat flux can alter the stress applied to the interface rather than merely remove liquid.

Non-isothermal hydrocarbon calculations isolate the second route. Heating decreases surface tension and promotes breakup for modeled n-decane droplets, particularly at lower Weber number and higher gas temperature; the more volatile comparison liquid heats differently because evaporation removes energy [[CITE:C032]]. These cases use continuous high-temperature flow rather than a shock pulse, so they describe property evolution during aerodynamic breakup, not the same interface state as the vapor-layer simulations.

Volatility links the two mechanisms. Rapid vaporization can cool the interface and shield it from shear, but it can also shrink the liquid and increase the fraction of mass carried by small fragments. A less volatile liquid may retain more mass while heating enough to reduce surface tension. Density ratio, Stefan or mass-transfer state, initial diameter, gas temperature, and exposure duration determine which balance dominates.

FIG-06 therefore shows phase change as a branch that alters both aerodynamic coupling and liquid resistance. Assigning one universal sign—promotion or suppression—would merge different thermal histories. What matters for HPDI is the resulting fragment, vapor, and temperature field at the time when the gaseous fuel and pilot products begin to interact.

## Fragment transport, vaporization, and mixture redistribution

[FIG-06 ABOUT HERE]

Fragments alter a pre-ignition mixture only if they evaporate and their vapor is transported into chemically relevant regions before ignition begins. The controlling state includes fragment size and temperature, relative velocity, local gas temperature and pressure, vapor saturation, residence time, and the surrounding turbulent flow. Increased surface area can accelerate mass transfer, but a fragment that is swept away from the ignition zone or remains cold may contribute little to the local equivalence ratio.

Size-dependent acceleration couples vapor release to spatial redistribution. Small fragments quickly follow the gas and can be carried along shear layers or into recirculation zones; larger remnants cross streamlines more slowly and retain inertia. Their vapor is then entrained and diffused on a mixing time that may be longer than the liquid evaporation time. Walls, jet–jet interaction, and the main gaseous-fuel momentum field can dominate where that vapor accumulates. The relevant output is therefore a time-resolved mixture or species field, not simply the disappearance of liquid.

Canonical experiments establish the upstream elements of this sequence. Fragment populations evolve after breakup [[CITE:C025]], and micrometre-scale clouds can undergo overlapping fragmentation, transport, and evaporation [[CITE:C024]] [[CITE:D017]]. HPDI experiments separately show that premixing and local pilot-product distributions strongly influence ignition [[CITE:A007]] [[CITE:A011]]. These observations make a shock-mediated contribution physically possible, particularly if breakup creates fragments whose evaporation time is shorter than the remaining ignition delay.

The magnitude of that contribution has not been isolated in an HPDI condition. Doing so would require the same experiment to measure the local wave and gas velocity, the parent-to-fragment population, vapor or mixture fraction, and the subsequent ignition field with one event clock. A smaller optical liquid signal alone would be ambiguous because breakup, evaporation, out-of-plane motion, and detection threshold can all reduce it. Similarly, a changed ignition delay could arise from injection timing, gaseous-fuel momentum, pilot displacement, or chamber temperature without any shock-induced liquid pathway.

The central physical question is consequently whether the fragment evaporation and vapor-mixing times are short relative to the interval between wave interaction and ignition, and whether the vapor enters the region where an ignition kernel forms. Current measurements do not yet provide this joint history. The next chapter examines the mixture and ignition variables that are measured directly in HPDI systems, beginning with injection chronology and jet geometry.

# CH07 — HPDI Mixture Formation, Ignition, and Combustion Coupling

## Injection chronology, jet geometry, and mixture preparation

[FIG-07 ABOUT HERE]

[TAB-06 ABOUT HERE]

Pilot-ignited direct injection creates mixture structure through the relative motion of two fuel streams. The liquid pilot must atomize, evaporate, and begin reacting, while the gaseous main jet entrains air and penetrates toward or through the pilot products. Their signed start-of-injection separation determines which stream arrives first, how far each has travelled at intersection, and whether the pilot is unreacted, igniting, or already burned when the main jet reaches it.

Increasing the dwell before main-fuel injection gives the pilot more time to mix and react, but it can also allow hot products to dilute and cool before contact. Advancing the main gas injection increases its premixing time and penetration, yet may place a high-momentum gas jet through the pilot before the pilot establishes a kernel. Experiments across engine, rapid-compression, and vessel configurations show transitions from mixing-controlled burning toward distributed or stratified premixed behavior as relative timing changes [[CITE:A006]] [[CITE:A011]] [[CITE:A018]]. The same timing magnitude can describe the opposite physical sequence if the fuel order or sign convention is reversed.

Jet geometry determines the spatial counterpart of this chronology. Converging jets intersect earlier and can entrain pilot products into the gas jet, while diverging jets preserve more independent pilot development. Hole spacing, angle, and flow area also change wall impingement and the residence of rich mixtures. A paired-hole arrangement increased early entrainment but also increased particulate matter in the tested engine, consistent with longer residence in a rich, moderate-temperature region [[CITE:A005]]. Simulations and engine studies similarly show angle- and flow-area-dependent changes in vortex entrainment, overlap, combustion phasing, and unburned fuel [[CITE:A016]] [[CITE:A017]].

Dual-fuel injection independently varies fuel quantity, sequence, and interval, but the resulting reactivity stratification still depends on oxygen level and injector arrangement [[CITE:A027]] [[CITE:A029]]. These controls are therefore useful only when the fuel order and local mixture state are specified.

Mixture preparation is therefore controlled by where and when the jets meet, not by timing or momentum alone. Local equivalence ratio, scalar dissipation, temperature, and pilot-product concentration evolve along each jet and near the wall. A source-specific study found natural-gas premixing near the bowl wall before ignition across its tested timing range, including a case in which gaseous fuel followed pilot combustion [[CITE:A014]]. Such behavior reflects that chamber and injector geometry rather than a universal ignition location.

FIG-07 follows the physical chronology from injection events and jet trajectories to mixture stratification. TAB-06 retains the fuel order, event definition, angle, operating point, and ignition metric needed to compare different configurations. Once overlap occurs, the next process is thermochemical: pilot products can heat and seed the main mixture, while the main jet can dilute or displace the pilot.

## Pilot-product entrainment and ignition

The pilot creates a localized source of temperature, radicals, and partially oxidized products. Main-fuel ignition begins when entrainment and molecular mixing bring a sufficiently reactive gas mixture into contact with that source for long enough to form a self-sustaining kernel. Too little overlap leaves the main jet cold and chemically isolated; too much or too-early overlap can dilute, cool, or aerodynamically disrupt the pilot before it ignites.

Optical experiments show both directions within the same physical framework. Greater spatial overlap and an appropriate dwell shorten the transition from pilot ignition to gaseous-fuel ignition, while a strong gas–pilot interaction before pilot ignition can delay or suppress the pilot [[CITE:A009]] [[CITE:A022]] [[CITE:A007]]. The transition depends on the overlap location relative to pilot lift-off and ignition, the momentum of each jet, ambient oxygen, and charge temperature. A larger converging angle moves the intersection upstream, but the resulting ignition change depends on whether the pilot has reacted by the time the gas arrives.

The main jet can interact with hot products in several ways. Entrainment raises temperature and transports H, O, and OH-containing products toward the gas jet; local dilution lowers oxygen and can reduce pilot reactivity; gas-jet momentum can move the pilot plume away from its preferred air-entrainment path. In a homogeneous-reactor analysis, temperature dominated methane ignition above about 1100 K, whereas realistic H/OH radicals shortened ignition delay mainly between 950 and 1100 K [[CITE:A012]]. These calculations isolate kinetics; actual jets add turbulent mixing and spatial gradients.

Hydrogen timing studies illustrate the mixture consequence. Advancing hydrogen injection increases premixing, but one early case substantially delayed diesel-pilot ignition, which the authors attributed to pre-ignition dilution [[CITE:A026]]. Because the fuel distribution before ignition was not directly imaged, dilution remains a physically consistent interpretation rather than a measured equivalence-ratio field. In a vessel experiment, hydrogen ignition after its end of injection propagated more slowly and left persistent lean unburned regions [[CITE:A020]]. By that time the jet had mixed beyond the composition and temperature range most favorable for rapid propagation.

Ignition is thus controlled by a coupled residence problem: pilot products, oxygen, fuel, and heat must coexist at the correct composition for a finite chemical induction time. Changes in timing and geometry act by moving that reactive overlap through space and time.

## Heat-release modes and operating-condition tradeoffs

Once ignition occurs, the heat-release rate reflects how much fuel was premixed before ignition and how rapidly fresh fuel and air continue to mix. A strongly premixed fraction burns rapidly near ignition and can increase pressure-rise rate. A mixing-controlled flame releases heat as gaseous fuel and air are entrained across the reaction zone. Relative injection timing determines the initial balance, while injection pressure, nozzle area, pilot energy, load, and chamber motion govern the later supply and mixing rates.

Raising gaseous-fuel injection pressure increases mass flux and jet momentum for a fixed nozzle and command, strengthening entrainment and shortening the late mixing-controlled phase under high-load conditions [[CITE:A001]] [[CITE:A002]] [[CITE:A011]]. The influence is weaker at some low-load or high-speed points, where available residence time, background turbulence, and ignition sensitivity differ. Faster mixing can reduce particulate matter and improve fuel conversion, but may also increase NOx, combustion noise, or pressure-rise severity. These outcomes arise from the same accelerated heat-release process rather than independent pressure effects.

Pilot energy controls the spatial extent and duration of the initial reacting region. Increasing the diesel share in an optical hydrogen engine strengthened and spread the pilot flame and accelerated the early hydrogen reaction, while the later mixing-controlled phase changed less [[CITE:A026]]. A larger pilot can improve ignition robustness but also changes local dilution, emissions, and the fraction of total heat release attributable to the pilot.

Relative-injection-timing sweeps identify distinct domains of apparent heat-release and emissions behavior as gas stratification, gas fraction, and injection pressure change [[CITE:A013]]. Hydrogen dual-direct-injection tests likewise report feasible controlled-phasing operation over the tested timing and energy-share range without pre-ignition or knock [[CITE:A018]]. These operating maps depend on engine speed, load, geometry, fuel fraction, and phasing control; they are most useful for identifying which stage—premixed ignition, early pilot-assisted reaction, or late mixing-controlled burn—responds to a control variable.

The application-level picture is consequently stage specific. Timing and geometry prepare the mixture, pilot energy establishes an ignition source, and gaseous-fuel momentum governs much of the subsequent mixing-controlled burn. Improving one stage can create a penalty in another, so heat-release shape and operating constraints must be interpreted together.

## Condition-specific hydrogen heat-release behavior

Hydrogen heat release follows the relative durations of injection, ignition delay, and mixing. In one dual-fuel study, hydrogen ignition produced an initial apparent-heat-release peak followed by a steadier interval while hydrogen injection continued; the profile became more transient when the diesel-surrogate injection and combustion duration altered the ordering of premixed and injection-controlled burning [[CITE:A021]]. Hydrogen dominated the apparent heat release under those tested conditions.

A three-dimensional engine calculation reported higher hydrogen heat-release rate than methane through much of the event and attributed the difference to coupled jet momentum, flammability, and quenching behavior. After the end of injection, the late heat-release rate fell rapidly [[CITE:A024]]. Because injection duration, mixture distribution, and the numerical combustion model differ from other studies, this comparison describes that engine configuration rather than a universal hydrogen–methane ranking.

These observations reinforce the role of event ordering. The interval between ignition and end of injection determines how long heat release is supplied by an actively injected jet, while the late phase depends on the mixture left behind after injection stops.

## From mixture preparation to ignition

Ignition begins in a local mixture whose equivalence ratio, temperature, oxygen concentration, and radical pool have been shaped by jet entrainment and pilot chemistry. A rich pocket may contain ample fuel but insufficient oxygen; a very lean pocket may be too cool or too weakly reactive; and a pilot plume diluted before autoignition can lose both temperature and radical production. The ignition kernel forms where turbulent transport creates a composition that can complete its chemical induction before the flow carries it away.

Injection chronology presently explains most observed variation in this state. Pilot-first sequences control how long the liquid spray can evaporate and react before the gas arrives. Gas-first sequences control how dilute and spatially extended the gaseous mixture becomes before contact with the pilot. Jet angle and momentum set the overlap location, while chamber temperature and oxygen set the chemical time. Across engine and vessel studies, these variables consistently shift pilot robustness, main-fuel delay, flame propagation, and heat-release mode [[CITE:A007]] [[CITE:A009]] [[CITE:A011]] [[CITE:A020]] [[CITE:A022]].

A wave-induced change in pilot fragments could enter this sequence by changing vapor release, local equivalence ratio, or the temperature history of the pilot mixture. To separate that contribution, the wave interaction would need to occur early enough for fragments to evaporate and mix before the ignition kernel forms. The resulting species field would then have to be distinguished from changes caused directly by injection pressure, mass flux, dwell, or jet geometry. These direct controls are strong: changing gaseous-fuel pressure alters momentum and late mixing, while changing dwell repositions both jets and the pilot products.

The necessary experiment must therefore synchronize pressure or density-gradient imaging, gas and droplet velocities, fragment or vapor diagnostics, local composition, and ignition. A shorter ignition delay after raising injection pressure would not by itself isolate wave-induced breakup, because the same change also increases gas momentum and entrainment. A reduction in liquid optical signal would likewise mix fragmentation, evaporation, deflection, and detection effects.

At present, no condition-matched HPDI study separates a wave-induced liquid or vapor change from the larger chronology, momentum, geometry, and thermochemical controls. The physical route remains credible only as a hypothesis: a wave changes fragment state, fragments alter vapor distribution, and that distribution reaches an ignition-sensitive region before chemical induction ends. The strong-wave literature considered next is a separate comparison domain that helps clarify wave–droplet time scales; it is not the next causal stage of an HPDI cycle.

# CH08 — Strong-Wave Analogues: Detonation and Rotating Detonation Engines

## Droplet and evaporation scales in detonation-wave systems

A droplet-laden detonation couples liquid response to a propagating reaction zone. Droplets ahead of or near the front are compressed, accelerated, heated, and fragmented; vapor released behind the front changes local equivalence ratio and can feed or starve the reaction. The decisive comparison is between the time or distance required for liquid to vaporize and the characteristic residence, refill, or wave scale of the device.

Rotating-detonation calculations define one such ratio as the evaporation distance divided by detonation-front height. In a simulated kerosene family with no pre-evaporated fuel, increasing initial diameter lengthened evaporation distance, enlarged fuel-lean or unburned pockets, reduced wave speed, and eventually produced shock–flame decoupling [[CITE:D009]]. Adding pre-vaporized fuel restored a more reactive upstream mixture. The ratio organizes those cases because its numerator and denominator describe the same refill and wave geometry. In the paired D009 cases, increasing `L_E/L_D` from 0.13 to 0.55 as `d0` increases from 2 to 4 µm accompanies a decrease in mean rotating-wave velocity from 1728 to 1618 m/s [[CITE:D009]]. The 5 µm case reports `L_E/L_D = 0.84` but lacks a paired wave-velocity value in the current extraction, so it is retained in the registry but excluded from the plot. This remains a within-study RDE relation.

Wave-relative position creates a second scale. Droplets close to the front receive a sharp temperature and pressure impulse and vaporize rapidly; droplets released or transported farther downstream heat more gradually, and some trailing droplets are only weakly affected by the front [[CITE:D014]]. Their longitudinal position determines both the peak thermal load and the time spent in hot products. A distribution of trajectories therefore produces a distribution of evaporation histories even at one initial diameter.

Breakup can shorten the liquid-survival scale by generating small, rapidly heated children. Detonation experiments with micrometre-scale fuel droplets show a finite survival region that evaporation-only calculations greatly overpredict for larger droplets; breakup models reduce the distance by increasing surface area [[CITE:D017]]. The variable post-front velocity and pressure history, however, causes different breakup closures to bracket rather than reproduce all observations. At `d0 = 10 µm` in the D017 model family, the reported extinction distance is 37.05 mm without breakup, 0.32 mm with KH–RT breakup, and 0.93 mm with WERT49 breakup [[CITE:D017]]. The order-of-magnitude spread at fixed diameter shows that a diameter trend cannot be separated from the product-generation closure.

These studies show that droplet size matters through its relation to a device-specific wave and residence scale, not as an isolated diameter threshold. The definitions of evaporation completion, reaction-zone or detonation height, pre-vaporized fraction, fuel chemistry, and wave multiplicity must remain attached to any scale ratio.

## Reacting and inert strong-wave loading

Matching the leading-shock Mach number does not match the gas history behind the wave. An inert shock establishes a post-shock state that relaxes through fluid motion and expansion. A detonation adds rapid heat release, changing pressure, temperature, sound speed, flow velocity, and their gradients. The droplet may see similar early transmitted and reflected wave patterns but very different subsequent slip, cavitation, and deformation.

Detonation-tube experiments show an early Kelvin–Helmholtz-dominated stripping stage followed by coupled KH and Rayleigh–Taylor piercing and catastrophic breakup for water and RP-3 droplets [[CITE:D018]]. Smaller droplets and stronger waves reach these stages sooner. Liquid properties alter the collapsed breakup time, while the adverse post-detonation pressure gradient reduces average acceleration relative to some uniform post-shock comparisons.

A controlled numerical comparison at equal leading Mach isolates the role of reaction heat release. Early wave topology remains similar, but the detonation changes reflected-shock propagation and shortens the persistence of the low-pressure region responsible for cavitation. Lower post-wave relative velocity suppresses the inert-shock forward jet and promotes leeward flattening through recirculation [[CITE:D019]]. Equal leading Mach thus coexists with different We/Re states and different loading duration.

This comparison clarifies why compressible droplet correlations require both a wave descriptor and a post-wave descriptor. Incident Mach sets the initial jump, whereas post-wave velocity and density set aerodynamic stress; pressure-gradient history governs acceleration; chemistry and sound speed control later wave motion. Ignoring these variables can attribute a reacting–inert difference to Mach when it actually arises from the state behind the front.

The strong-wave domain therefore provides a stringent test of loading-history models. It shows that early shock transmission can be similar while later instability and phase response diverge, a behavior directly relevant to any attempt to organize breakup by a single leading-wave parameter.

## What strong-wave analogues reveal for HPDI

[FIG-08 ABOUT HERE]

[TAB-07 ABOUT HERE]

Detonation and rotating-detonation systems share several local processes with high-pressure injection: rapid compression, large gas–liquid slip, finite wave exposure, fragmentation, heating, and vapor transport. They show especially clearly that the post-wave state and residence history matter as much as the leading wave. They also provide conditions in which liquid persistence feeds back on a propagating reaction zone.

The most useful physical lessons are local. A droplet's position relative to a moving wave controls its thermal impulse; breakup competes with evaporation over a finite survival distance; and heat release changes the velocity and pressure-gradient history that drives later deformation [[CITE:D009]] [[CITE:D014]] [[CITE:D018]] [[CITE:D019]]. These results guide which variables should be measured in HPDI: relative velocity rather than leading Mach alone, fragment size rather than parent diameter alone, and time to ignition relative to breakup and evaporation times.

The device scales are nevertheless different. An RDE front repeatedly traverses an annular or unrolled combustor, while HPDI injection occurs in a chamber with moving boundaries, a pilot spray, a separate gaseous jet, and engine-scale swirl and wall interaction. Detonation chemistry creates post-wave temperatures and radicals absent from an inert underexpanded shock. The characteristic denominator in `L_E/L_D` is a detonation-front or reaction/refill length, not an HPDI ignition length.

Quantitative use would require a mapping that preserves wave strength, post-wave density and velocity, liquid properties, loading duration, droplet population, thermal state, and the competing residence and reaction scales. No such mapping has been validated. FIG-08 therefore places the shared local mechanisms and the domain-specific scales in separate layers, and TAB-07 retains both definitions in every characteristic ratio.

Strong-wave studies thus sharpen the physics without supplying an engine prediction. The final chapter returns to HPDI and connects the relevant time scales from injector opening to ignition, identifying which couplings can be calculated from existing measurements and which require new synchronized diagnostics.

# CH09 — Multiscale Coupling and Research Priorities

## Integrated multiscale mechanism and unresolved couplings

[FIG-09 ABOUT HERE]

The coupled problem begins with competing clocks. Injector opening and pressure build-up determine when the gas chokes and how rapidly the Mach disk and shock cells move. A droplet then experiences shock-front passage, a finite post-wave slip, internal acoustic motion, acceleration, deformation, instability growth, and fragmentation. The resulting children have their own acceleration and evaporation times, while turbulent mixing and chemical induction determine whether their vapor reaches an ignition-sensitive region. The ordering of these times, rather than any single pressure or Weber number, controls which parts of the sequence can influence combustion.

Across the gas–liquid interface, only a small set of variables carries the wave into the liquid mechanics: local pressure history, gas density, relative velocity, load direction, and duration. Underexpanded-jet studies describe these quantities in an Eulerian frame around shocks and vortices [[CITE:B009]] [[CITE:B021]]. Droplet studies describe the response to imposed versions of the same variables [[CITE:C007]] [[CITE:C016]]. The missing step is their evaluation along actual pilot trajectories in a transient injector field. Without that history, a visible Mach disk cannot be converted into a unique droplet Weber number, impulse, or instability time.

Once liquid structures interact, the load becomes collective. Tandem wakes reduce downstream slip, parallel gaps intensify or close channel flow, and clouds attenuate the transmitted compression [[CITE:C035]] [[CITE:C036]] [[CITE:C033]] [[CITE:C034]]. A dense pilot spray combines all of these effects across a changing distribution of sizes and spacings. Consequently, canonical breakup physics remains locally useful, but the population response requires joint gas and liquid statistics rather than independent-droplet calculations.

Fragmentation can affect mixture preparation when it creates enough surface area early enough for vapor to be released and transported before ignition. Small fragments accelerate and evaporate quickly; large remnants preserve mass and inertia; vapor then mixes on a separate turbulent time [[CITE:C024]] [[CITE:D017]]. Thermal state can either weaken interfacial shear through a vapor layer or promote deformation through reduced surface tension [[CITE:C031]] [[CITE:C032]]. The net change in mixture fraction therefore depends on fragment distribution, residence, volatility, and gas history, not simply on whether breakup occurred.

In HPDI experiments, injection chronology and jet geometry exert the clearest control over ignition. They set overlap, pilot dilution, access to hot products and radicals, local equivalence ratio, and the interval available for chemical induction [[CITE:A007]] [[CITE:A011]] [[CITE:A020]] [[CITE:A022]]. A wave-mediated liquid contribution must be separated from these stronger controls by measuring the fragment and vapor field directly. No current experiment follows the entire chain from transient wave, through pilot fragments and vapor, to the ignition kernel under one condition.

FIG-09 summarizes this multiscale sequence. Solid physical blocks denote processes measured within their native configurations; the connecting questions identify quantities still absent at HPDI scale. The central challenge is not to invent a universal scaling, but to measure the same pressure, velocity, population, mixture, and ignition history on a common clock.

## Measurements and models needed to resolve the coupling

[TAB-08 ABOUT HERE]

The most important unresolved measurement is the aerodynamic history of pilot droplets inside a transient underexpanded jet. A useful experiment would synchronize injector pressure and needle motion with density-gradient or pressure-field imaging, gas velocity, and droplet or ligament tracking. These measurements would provide `p[x_d(t),t]`, `ρ_g[x_d(t),t]`, `u_rel(t)`, and the arrival of expansion or reflected waves. Reporting the pressure roles, nozzle state, and event time would allow the resulting load to be compared across injectors.

The next requirement is a population-resolved account of collective breakup. High-speed three-dimensional diagnostics or validated interface-resolved calculations should measure size–velocity distributions, spatial correlations, and liquid mass through the shock interaction. The gas response must be recorded at the same time to capture wake shielding and wave attenuation. Dense-spray experiments should vary polydispersity, volume fraction, turbulence, and thermal state independently where possible, rather than infer all collective behavior from one mean spacing.

Fragment transport and vaporization require simultaneous area, temperature, and composition information. Measurements should distinguish connected ligaments from independent droplets, preserve number- and mass-weighted distributions, and quantify detection loss. Laser-based vapor or species diagnostics aligned with the fragment field could determine whether smaller products actually raise local vapor concentration or are transported away. Matched thermal studies are also needed to separate vapor-layer shear reduction from heating-induced surface-tension change.

The final coupling to ignition demands a common chronology for wave interaction, mixture preparation, and chemical response. Pressure and velocity fields, pilot and main-fuel species, temperature-sensitive markers, radical-sensitive diagnostics where feasible, ignition location, and heat release should be measured in one geometry. Controlled changes must isolate wave interaction from simultaneous changes in injection momentum, dwell, and mass flow. Only then can a change in ignition delay be assigned to a wave-induced liquid or vapor process.

Model development should follow the same hierarchy. Gas dynamics must reproduce injector transients and local wave motion; liquid models must predict product distributions rather than only regime labels; population models must include shielding and attenuation; and combustion calculations must propagate uncertainty in vapor and mixture fields to ignition. Validation at each interface prevents compensation errors in which an incorrect fragment field still produces a plausible heat-release trace.

Detonation and RDE calculations can test sensitivity to post-wave thermochemistry and characteristic scales, but any use in HPDI requires an explicit mapping of load, residence, population, and reaction times. The missing C004 PDF remains a narrower source limitation on breakup-taxonomy coverage rather than a missing physical coupling. TAB-08 organizes these measurements and models by the variable that crosses each interface and the observable needed for validation.

## Conclusions

High-pressure gaseous injection creates a transient compressible flow whose wave structure evolves with injector opening, pressure build-up, nozzle geometry, gas properties, and chamber state. Mach-disk position follows pressure ratio under compatible conditions, but the local load on liquid depends on the pressure, density, velocity, direction, and duration sampled along each droplet trajectory.

Shock-loaded droplets respond through a sequence of internal wave motion, acceleration, flattening, interfacial instability, sheet and ligament formation, and fragmentation. Weber number alone cannot order this sequence because Mach context, loading duration, initial size, viscosity, surface tension, and thermodynamic state alter both the imposed stress and the liquid response time. Reduced models must therefore be judged against the output they are expected to predict, especially fragment size and velocity distributions needed downstream.

Neighboring droplets modify the load through wake shielding, squeeze flow, channel closure, and wave attenuation. Dense pilot sprays add polydispersity, turbulence, vaporization, and reaction to these interactions. Fragment populations then govern liquid transport and surface-area growth, while the direction and rate of phase-change coupling depend on thermal state, volatility, vapor-layer dynamics, and temperature-dependent surface tension.

HPDI ignition is controlled most directly by injection chronology, jet geometry, mixture stratification, pilot-product entrainment, temperature, oxygen, and radicals. Shock-induced fragmentation may alter the vapor field when fragment evaporation and mixing are fast relative to ignition delay, but this contribution has not been isolated from injection momentum, timing, and geometry. Detonation and RDE studies clarify strong-wave loading and residence-scale effects while remaining a separate thermochemical and geometric domain.

The review links these fields through the variables that cross their interfaces and through the competing time scales that decide whether one stage can affect the next. Four experimental questions remain decisive: the load experienced by actual pilot droplets, the survival of canonical mechanisms in dense sprays, the influence of fragments on the pre-ignition mixture, and the effect of any wave-induced mixture change on ignition. Resolving them requires synchronized gas, liquid, species, and combustion diagnostics rather than additional isolated correlations.
