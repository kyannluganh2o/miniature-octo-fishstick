from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "09_Manuscript" / "phase14R_harmonized_draft.md"
TARGET = ROOT / "09_Manuscript" / "phase14S_integrated_draft.md"


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected one match, found {count}")
    return text.replace(old, new, 1)


text = SOURCE.read_text(encoding="utf-8")
text = replace_once(text, "# Phase 14R Physics-Led Harmonized Draft", "# Phase 14S Scientifically Integrated Draft", "title")
text = replace_once(text, "Status: reconstructed working manuscript", "Status: figure/table–manuscript scientifically integrated working manuscript", "status")

# CH01: keep the physical-chain role and move the research-gap burden to FIG-09.
old = """FIG-01 follows the physical sequence from injector opening to combustion while marking the quantities transmitted between stages. Injector motion and (p_{inj}(t)) create a developing underexpanded jet. The shock and vortex field supplies local pressure, density, velocity, and loading duration. These variables drive internal liquid waves, acceleration, deformation, and instability; breakup then creates a population whose size, velocity, and temperature govern transport and evaporation. Vapor and pilot products finally enter the mixture and chemical induction processes that form an ignition kernel.

Chapters 2 and 3 develop the gas dynamics and the load sampled by a moving droplet. Chapters 4 and 5 follow single-droplet response and the redistribution of loading by neighbors and clouds. Chapter 6 tracks fragments, phase change, and vapor transport. Chapter 7 examines the directly observed roles of chronology, jet interaction, pilot products, and mixture state in ignition and heat release. Chapter 8 compares reacting strong-wave systems, and Chapter 9 integrates the competing time scales and measurement requirements.

The sequence is physically continuous, but several connecting quantities have not been measured under one HPDI condition. FIG-01 uses these missing variables to prevent a schematic arrow from implying a completed causal chain. The discussion begins with the upstream boundary: the pressure, nozzle, gas, ambient, and opening history that determine how an underexpanded shock system forms."""
new = """FIG-01 defines the physical chain examined in this review. Injector motion and \(p_{\mathrm{inj}}(t)\) create a developing underexpanded jet; the moving wave and vortex field supplies pressure, density, relative velocity, direction, and duration to the liquid. Liquid response produces a fragment population whose size, velocity, and temperature condition transport and phase change, after which vapor and pilot products enter mixture preparation and chemical induction. The open connectors do not add a second gap map; they simply mark that the state passed between adjacent stages has not been measured continuously under one HPDI condition.

Chapters 2 and 3 develop the gas dynamics and the load sampled by a moving droplet. Chapters 4 and 5 follow single-droplet response and the redistribution of loading by neighbors and clouds. Chapter 6 tracks fragments, phase change, and vapor transport. Chapter 7 examines the directly observed roles of chronology, jet interaction, pilot products, and mixture state in ignition and heat release. Chapter 8 compares reacting strong-wave systems, and Chapter 9 aligns the still-unclosed interfaces with their competing clocks.

The discussion begins at the upstream boundary: the pressure, nozzle, gas, ambient, and opening history that determine how an underexpanded shock system forms."""
text = replace_once(text, old, new, "CH01 FIG01 integration")

# CH02: establish the question before the figure, then read the panels.
text = replace_once(text, "## Injector opening and transient jet formation\n\n[FIG-02 ABOUT HERE]\n\nThe first shock cells form", "## Injector opening and transient jet formation\n\nThe first shock cells form", "move FIG02 lead")
anchor = "The resulting wave pattern is therefore tied to the history of valve lift, pressure build-up, and chamber pressure rather than to the final rail-pressure plateau."
text = replace_once(text, anchor, anchor + "\n\n[FIG-02 ABOUT HERE]\n\nThe three panels expose different parts of that adjustment. In Fig. 2a, the axial-Mach profiles first rise locally, develop repeated shock-associated peaks, and then relax toward a later distribution; the early near field is therefore not a scaled copy of the semi-steady jet [[CITE:B009]]. Figure 2b compares steady and unsteady Mach-disk positions at the reported operating points and shows that an instantaneous topology can remain close to, but is not identical with, its steady counterpart [[CITE:B021]]. Figure 2c adds the missing injector-side chronology: the velocity contours evolve from the first shocks to joined shock cells while the internal pressure/area history is still developing [[CITE:B029]]. Read together, the panels show one coupled adjustment viewed through axial Mach, topology, and injector-conditioned velocity fields; they cannot be collapsed onto a single nominal-pressure coordinate.", "FIG02 analysis")
old = """FIG-02 summarizes this event-aligned evolution from injector motion and (p_{inj}(t)) to choking, shock formation, overshoot, and stabilization. The key consequence for downstream multiphase physics is that a droplet or pilot jet entering during formation can encounter a different pressure and velocity field from one entering after the shock cells have settled.

## Mach-disk and shock-cell evolution

[TAB-02 ABOUT HERE]

Once a strongly underexpanded jet forms, Prandtl–Meyer expansion at the nozzle lip accelerates the gas and lowers its static pressure."""
new = """The key downstream consequence is temporal: a droplet or pilot jet entering during formation can encounter a different pressure and velocity field from one entering after the shock cells have settled.

## Mach-disk and shock-cell evolution

Once a strongly underexpanded jet forms, Prandtl–Meyer expansion at the nozzle lip accelerates the gas and lowers its static pressure."""
text = replace_once(text, old, new, "remove generic FIG02 and move TAB02")
anchor = "Their location controls where pressure, density, velocity, and turbulent shear change most abruptly."
tab02 = """Their location controls where pressure, density, velocity, and turbulent shear change most abruptly.

[TAB-02 ABOUT HERE]

Table 2 separates three valid forms of comparison. B009 uses one nozzle, common pressure roles, and a semi-steady state across its hydrogen NPR series, so the increasing \(x_{\mathrm{MD}}/D\) values support a within-study NPR trend [[CITE:B009]]. B021 supplies a steady/unsteady topology contrast and radial information, but its nozzle, chamber state, and reported metric do not reproduce the B009 sequence [[CITE:B021]]. B029 primarily constrains event alignment because \(p_{\mathrm{inj}}(t)\), opening-to-stabilization history, penetration, and contour evolution are reported together [[CITE:B029]]. The scientific distinction is between a controlled parameter trend, a state/topology comparison, and a transient boundary-condition history—not between three interchangeable NPR points."""
text = replace_once(text, anchor, tab02, "TAB02 synthesis")

# CH03: retain the mature Eulerian-to-Lagrangian argument and sharpen the paired clocks.
old = "FIG-03 summarizes the conversion from wave geometry to the fields that act on liquid: (p(x,t)), ρ(x,t), (u(x,t)), vorticity, and their gradients. The relevant input for droplet dynamics is obtained only after these Eulerian fields are sampled along a liquid trajectory. That Lagrangian conversion is the central problem of the next section."
new = "The visible wave geometry identifies candidate compression, expansion, and vortex events, but it does not specify their magnitude or duration along moving liquid. Figure 3 therefore separates the Eulerian field from the trajectory-sampled load developed in the next section."
text = replace_once(text, old, new, "FIG03 lead-in")
anchor = "A pilot droplet crossing a transient underexpanded jet encounters a history rather than a single shock strength."
addition = "FIG-03 makes the non-equivalence explicit: visible wave topology is not trajectory-resolved droplet load. The Eulerian field becomes physically relevant only after it is sampled as \\(p[\\mathbf{x}_d(t),t]\\), \\(\\rho_g[\\mathbf{x}_d(t),t]\\), and \\(\\mathbf{u}_{\\mathrm{rel}}(t)\\) along the moving liquid. That sampled history defines \\(\\tau_{\\mathrm{load}}\\), whereas deformation or breakup defines the separately specified \\(\\tau_{\\mathrm{response}}\\). Their ratio is useful as an organizing hypothesis, not as a universal criterion and not as a substitute for the missing HPDI trajectory history.\n\n" + anchor
text = replace_once(text, anchor, addition, "FIG03 analysis")

# CH04: place TAB03 after the first Mach/We/d0 comparison and FIG04 after the governing discussion.
text = replace_once(text, "## Governing parameters of compressible droplet response\n\n[FIG-04 ABOUT HERE]\n\n[TAB-03 ABOUT HERE]\n\nWhen a shock passes", "## Governing parameters of compressible droplet response\n\nWhen a shock passes", "remove early FIG04 TAB03")
anchor = "The ratio of droplet diameter to the preferred Kelvin–Helmholtz wavelength helps explain why a scalar We threshold shifts with size."
addition = """The ratio of droplet diameter to the preferred Kelvin–Helmholtz wavelength helps explain why a scalar We threshold shifts with size.

[TAB-03 ABOUT HERE]

Across Table 3, Weber number repeatedly co-varies with diameter, Reynolds number, and Mach: the C016 SIE/RTP cases change \(d_0\), \(Re\), and \(M_s\) together, while the C025 pair changes the incident Mach and resulting post-shock Weber number together [[CITE:C016]] [[CITE:C025]]. The Mach descriptor also changes physical frame—from incident-shock Mach to post-wave freestream or detonation-front context—and the response endpoint ranges from a named morphology to deformation statistics, piercing, cavitation, or complete breakup [[CITE:C014]] [[CITE:D018]] [[CITE:D019]]. These rows support a state-conditioned response, not a universal We-only or Mach-only regime map."""
text = replace_once(text, anchor, addition, "TAB03 synthesis")
old = """FIG-04 organizes these variables around a sequence rather than a universal regime axis: pressure transmission and acceleration lead to deformation; deformation establishes interfacial geometry; and shear, acceleration, capillarity, and viscosity determine which disturbances grow. TAB-03 retains the Mach frame, reference density and velocity, diameter, liquid state, and loading interval needed to compare those stages."""
new = """[FIG-04 ABOUT HERE]

The morphology comparison makes those state dependencies visible. Figure 4a shows an acceleration-dominated RTP form: the windward body has flattened and the liquid is penetrated into bag-like structures rather than being removed as a uniformly thin edge mist [[CITE:C016]]. Figure 4b instead shows a broad shear-induced entrainment layer with fine peripheral liquid, consistent with strong interfacial shear and stripping [[CITE:C016]]. In Fig. 4c, distinct first and second ligament-shedding events remain visible after the initial fragment release; first shedding therefore cannot be equated with breakup completion [[CITE:C013]]. Figure 4d resolves a KHI-dominant stage followed by coupled KHI–RTI breakup, but the reacting detonation products, front strength, and post-wave history make it a strong-wave analogue rather than a transferable HPDI regime boundary [[CITE:D018]]. The common conclusion is mechanistic competition on an evolving interface, not a single monotonic progression with We."""
text = replace_once(text, old, new, "FIG04 panel analysis")

anchor = "Increasing shock strength then alters both the circulation and the pressure-gradient-driven deformation. These early mechanisms occur before a mature breakup cloud forms."
addition = """Increasing shock strength then alters both the circulation and the pressure-gradient-driven deformation. These early mechanisms occur before a mature breakup cloud forms.

[FIG-04A ABOUT HERE]

Figure 4A shows why the thermodynamic state belongs in that initial condition. In the 500 K case (Fig. 4A(a–c)), the refracted shock advances through the droplet and subsequent internal reflections remain on a diverging branch. In the 650 K case (Fig. 4A(d–f)), the lower internal sound speed makes the refracted shock lag, converge, and emit a transmitted wave after focusing [[CITE:C029]]. The visual contrast supports the source interpretation that crossing a sound-speed ratio near unity reverses the refraction behavior. It does not establish a late-breakup map: the calculation is two-dimensional and its role here is to connect thermodynamic state to early pressure and circulation histories."""
text = replace_once(text, anchor, addition, "FIG04A integration")

# CH05: introduce the configuration question, then read panels and use TAB04 for condition space.
text = replace_once(text, "## Wake shielding, squeeze flow, and channel closure\n\nTwo droplets exposed", "## Wake shielding, squeeze flow, and channel closure\n\nTwo droplets exposed", "CH05 anchor")
anchor = "Spacing therefore changes both the magnitude and direction of the local load, but by different mechanisms in the two geometries."
addition = """Spacing therefore changes both the magnitude and direction of the local load, but by different mechanisms in the two geometries.

[FIG-05 ABOUT HERE]

Figure 5 compares configurations rather than successive times. Relative to the isolated reference in Fig. 5a, the downstream member of the tandem pair in Fig. 5b deforms less strongly than the lead droplet as the pair evolves; this differential response is consistent with wake shielding and reduced local slip [[CITE:C035]]. In Fig. 5c, the transverse gap narrows and the facing interfaces develop channel-directed structures, making squeeze flow and closure—not wake sheltering—the relevant interaction [[CITE:C036]]. Figure 5d moves to population scale: the image sequence and station pressure traces show a transmitted compression that is attenuated and broadened through the cloud [[CITE:C033]]. These are three distinct ways that neighboring liquid modifies the gas load, not one universal spacing law."""
text = replace_once(text, anchor, addition, "FIG05 panel analysis")
text = replace_once(text, "FIG-05 compares isolated, tandem, parallel, and cloud configurations rather than presenting a temporal progression. Each configuration introduces a different collective mechanism: wake shielding for streamwise pairs, squeeze flow and channel closure for transverse pairs, and attenuation with population feedback for clouds. Dense pilot sprays additionally contain polydispersity, rapid vaporization, turbulence, collisions, and possible reaction, so transfer from these canonical configurations remains open.\n\n", "", "remove generic FIG05")
text = replace_once(text, "## From canonical droplets to dense pilot sprays\n\n[FIG-05 ABOUT HERE]\n\n[TAB-04 ABOUT HERE]", "## From canonical droplets to dense pilot sprays\n\n[TAB-04 ABOUT HERE]", "remove moved FIG05")
anchor = "An isolated droplet converts a specified gas history into one deformation and breakup history."
addition = """Figure 5 shows the distinct forms of collective interaction, while Table 4 places them in their respective geometric and loading ranges. Pair coordinates such as streamwise \(S/D\) or transverse \(L/D\) retain orientation and define one or two neighbors; cloud descriptors such as volume fraction, number density, and thickness define a population and its integrated exchange area. They cannot be converted directly without a size distribution and spatial-correlation model. Consequently, the C035 shielding and C036 closure boundaries constrain ordered geometries, whereas C033/C034 constrain attenuation for a cloud-level loading and sensor arrangement [[CITE:C035]] [[CITE:C036]] [[CITE:C033]] [[CITE:C034]].

An isolated droplet converts a specified gas history into one deformation and breakup history."""
text = replace_once(text, anchor, addition, "TAB04 synthesis")

# CH06: move FIG06 and TAB05 after both thermal branches are established.
text = text.replace("\n[TAB-05 ABOUT HERE]\n", "\n", 1)
text = replace_once(text, "FIG-06 follows these product variables from breakup into transport and phase change. The next question is temporal: do fragments survive long enough to travel as liquid, or do breakup and evaporation overlap before the mixture reaches ignition conditions?", "The next question is temporal: do fragments survive long enough to travel as liquid, or do breakup and evaporation overlap before the mixture reaches ignition conditions?", "remove generic FIG06")
text = replace_once(text, "TAB-05 organizes the required initial size, fragment distribution, gas temperature and pressure history, volatility, and observation interval. These variables determine whether breakup mainly changes liquid transport or materially changes vapor availability before ignition.\n\n", "", "remove early TAB05 callout")
old = """FIG-06 therefore shows phase change as a branch that alters both aerodynamic coupling and liquid resistance. Assigning one universal sign—promotion or suppression—would merge different thermal histories. What matters for HPDI is the resulting fragment, vapor, and temperature field at the time when the gaseous fuel and pilot products begin to interact.

## Fragment transport, vaporization, and mixture redistribution

[FIG-06 ABOUT HERE]"""
new = """[FIG-06 ABOUT HERE]

The four source panels separate the required clocks and mechanisms. Figure 6a shows fragmentation and optical disappearance overlapping over hundreds of microseconds, but the fading signal does not by itself measure vapor mass [[CITE:C024]]. Figure 6b shows that, over the early interval of the larger-droplet cases, substantial deformation can develop while evaporation remains a weak influence on shape [[CITE:C026]]. Figure 6c isolates the vapor-layer route: evaporation smooths the interface and suppresses shear-driven structure relative to the no-phase-change and condensation branches [[CITE:C031]]. Figure 6d isolates the competing liquid-property route: hotter n-decane cases exhibit deformation changes consistent with temperature-dependent capillary resistance [[CITE:C032]]. The diagram therefore keeps vapor-layer shear suppression and heating-induced capillary weakening as parallel conditional branches before they rejoin in the downstream fragment, transport, and evaporation state.

[TAB-05 ABOUT HERE]

Five cross-row patterns follow from Table 5. C026 constrains a weak early-time phase-change influence for sufficiently large droplets; C027 makes pressure and volatility part of the vaporization condition; C031 demonstrates vapor-layer-mediated shear suppression; C032 shows heating-induced capillary weakening; and C024/D017 show fragmentation and evaporation overlapping through daughter-product generation [[CITE:C026]] [[CITE:C027]] [[CITE:C031]] [[CITE:C032]] [[CITE:C024]] [[CITE:D017]]. Because these mechanisms act on different states and clocks, phase change has no universal positive or negative effect on breakup. The quantity carried forward is the conditional fragment-size, velocity, temperature, and vapor state—not the binary fact that breakup occurred.

## Fragment transport, vaporization, and mixture redistribution"""
text = replace_once(text, old, new, "FIG06 TAB05 integration")

# CH07: establish chronology and geometry before FIG07; broaden into TAB06 classes.
text = text.replace("\n[FIG-07 ABOUT HERE]\n\n[TAB-06 ABOUT HERE]\n", "\n", 1)
anchor = "Simulations and engine studies similarly show angle- and flow-area-dependent changes in vortex entrainment, overlap, combustion phasing, and unburned fuel [[CITE:A016]] [[CITE:A017]]."
addition = """Simulations and engine studies similarly show angle- and flow-area-dependent changes in vortex entrainment, overlap, combustion phasing, and unburned fuel [[CITE:A016]] [[CITE:A017]].

[FIG-07 ABOUT HERE]

The panels show why chronology and geometry must be read together. Figure 7a makes geometry explicit: changing injector angle moves the intersection zone and therefore changes where hydrogen can contact pilot spray or products [[CITE:A022]]. Figure 7b adds relative timing: at the same optical location, the pilot-flame state and early hydrogen-flame footprint differ with the hydrogen start of injection and energy split [[CITE:A026]]. Figure 7c then maps ignition response over both gas-delay and jet-angle coordinates, demonstrating that neither coordinate alone orders the result [[CITE:A007]]. Geometry sets where the streams meet; relative timing sets the pilot state when they meet; ignition depends on both. None of these panels isolates a wave-created fragment contribution."""
text = replace_once(text, anchor, addition, "FIG07 panel analysis")
old = "FIG-07 uses relative chronology: signed \\(\\Delta\\mathrm{SOI}\\) is defined from named pilot and main-fuel events, with fuel order, event type, and geometry retained. TAB-06 preserves the operating point and ignition metric needed to compare configurations. Once overlap occurs, the next process is thermochemical: pilot products can heat and seed the main mixture, while the main jet can dilute or displace the pilot. The direct timing/geometry pathway is therefore separated from the hypothesized wave-mediated fragment pathway."
new = """[TAB-06 ABOUT HERE]

Table 6 broadens the panel comparison into three application-control classes. The A007/A009/A011/A013/A020/A022/A026 rows use chronology and geometry to alter premixing, overlap, pilot state, and ignition timing. A001/A002 instead emphasize injection pressure and momentum, whose clearest effect is stronger entrainment and a shorter later mixing-controlled burn. A005 shows a third class—local hole arrangement and rich-zone residence—in which greater early entrainment does not guarantee improved downstream combustion. No single signed \(\Delta\mathrm{SOI}\) or mixing-intensity coordinate organizes these classes: chronology fixes the reactive state at first contact, geometry fixes its location, momentum governs subsequent transport, and pilot energy and oxygen set chemical robustness. Once overlap occurs, the next process is thermochemical: pilot products can heat and seed the main mixture, while the main jet can dilute or displace the pilot."""
text = replace_once(text, old, new, "TAB06 synthesis")

# CH08: read the panels first, then separate local transfer variables from device scales in TAB07.
text = text.replace("\n[FIG-08 ABOUT HERE]\n\n[TAB-07 ABOUT HERE]\n", "\n", 1)
anchor = "Detonation and rotating-detonation systems share several local processes with high-pressure injection: rapid compression, large gas–liquid slip, finite wave exposure, fragmentation, heating, and vapor transport. They show especially clearly that the post-wave state and residence history matter as much as the leading wave. They also provide conditions in which liquid persistence feeds back on a propagating reaction zone."
addition = """Detonation and rotating-detonation systems share several local processes with high-pressure injection: rapid compression, large gas–liquid slip, finite wave exposure, fragmentation, heating, and vapor transport. They show especially clearly that the post-wave state and residence history matter as much as the leading wave. They also provide conditions in which liquid persistence feeds back on a propagating reaction zone.

[FIG-08 ABOUT HERE]

The source panels resolve the distinction between leading-wave label and experienced load. Figure 8a shows liquid-dependent breakup chronology and morphology under a detonation front, including different times to the KHI-dominant and coupled KHI–RTI stages [[CITE:D018]]. In Fig. 8b, reacting and inert cases share the reported leading Mach number and similar early wave geometry, yet their pressure fields are already not identical [[CITE:D019]]. Figure 8c shows that droplets grouped by wave-relative position acquire different temperature, evaporation-rate, and size histories [[CITE:D014]]. By the later states in Fig. 8d, the reacting and inert pressure fields have diverged further [[CITE:D019]]. Thus \(M_{\mathrm{leading}}\) alone does not define droplet loading: post-wave \(p\), \(\rho_g\), \(\mathbf{u}_{\mathrm{rel}}\), pressure gradient, thermal history, chemistry, and residence remain independent state variables."""
text = replace_once(text, anchor, addition, "FIG08 panel analysis")
anchor = "The device scales are nevertheless different. An RDE front repeatedly traverses an annular or unrolled combustor, while HPDI injection occurs in a chamber with moving boundaries, a pilot spray, a separate gaseous jet, and engine-scale swirl and wall interaction. Detonation chemistry creates post-wave temperatures and radicals absent from an inert underexpanded shock. The characteristic denominator in \\(L_E/L_D\\) is a detonation-front or reaction/refill length, not an HPDI ignition length."
addition = anchor + "\n\n[TAB-07 ABOUT HERE]\n\nTable 7 separates locally transferable variables—post-wave pressure, density, relative velocity, droplet size, fragment state, and residence—from domain-specific reaction-zone, refill/front, thermochemical, and device-kinematic scales. The D009 and D017 rows are complementary rather than redundant: D009 normalizes liquid persistence by an RDE device scale, whereas D017 shows that the predicted survival distance changes by roughly one to two orders of magnitude when breakup-generated products are included and still depends on closure choice [[CITE:D009]] [[CITE:D017]]. Together they show that survival is a competition between product-generation physics and a device-specific residence scale. Neither the numerical ratio nor the breakup closure is an HPDI ignition predictor without an explicit mapping."
text = replace_once(text, anchor, addition, "TAB07 synthesis")
text = replace_once(text, "Quantitative use would require a mapping that preserves wave strength, post-wave density and velocity, liquid properties, loading duration, droplet population, thermal state, and the competing residence and reaction scales. No such mapping has been validated. FIG-08 therefore places the shared local mechanisms and the domain-specific scales in separate layers, and TAB-07 retains both definitions in every characteristic ratio.", "Quantitative use would require a mapping that preserves wave strength, post-wave density and velocity, liquid properties, loading duration, droplet population, thermal state, and the competing residence and reaction scales. No such mapping has been validated.", "remove generic FIG08 TAB07")

# CH09: align the gap map with research actions and compress priorities into three tiers.
text = text.replace("\n[FIG-09 ABOUT HERE]\n", "\n", 1)
anchor = "The ordering of these times, rather than any single pressure or Weber number, controls which parts of the sequence can influence combustion."
addition = """The ordering of these times, rather than any single pressure or Weber number, controls which parts of the sequence can influence combustion.

[FIG-09 ABOUT HERE]

Figure 9 aligns each physical stage with both a clock and the state transmitted downstream. The load row carries \(p\), \(\rho_g\), and \(\mathbf{u}_{\mathrm{rel}}\) into liquid response; the fragment row carries size, velocity, and temperature toward evaporation and transport; the mixture row carries composition and thermal state toward radicals and heat release. The four open interfaces occur where one row cannot yet be connected to the next under a common HPDI event clock. This division of labor differs from Fig. 1: Fig. 1 defines the reviewed physical chain, whereas Fig. 9 explains why that chain is not quantitatively closed."""
text = replace_once(text, anchor, addition, "FIG09 integration")
text = replace_once(text, "FIG-09 summarizes this multiscale sequence. Solid physical blocks denote processes measured within their native configurations; the connecting questions identify quantities still absent at HPDI scale. The central challenge is not to invent a universal scaling, but to measure the same pressure, velocity, population, mixture, and ignition history on a common clock.\n\n", "The central challenge is not to invent a universal scaling, but to measure pressure, velocity, population, mixture, and ignition histories on a common clock.\n\n", "remove generic FIG09")
text = text.replace("\n[TAB-08 ABOUT HERE]\n", "\n", 1)
anchor = "Reporting the pressure roles, nozzle state, and event time would allow the resulting load to be compared across injectors."
priority = """Reporting the pressure roles, nozzle state, and event time would allow the resulting load to be compared across injectors.

[TAB-08 ABOUT HERE]

Table 8 converts the four physical gaps in Fig. 9 into research actions. Priority 1 is trajectory-resolved loading: synchronize injector pressure and motion, the density-gradient or pressure field, gas velocity, and liquid tracking to recover the vector load history. Priority 2 is the population bridge: measure mass-resolved fragment size, velocity, temperature, spatial correlation, and vapor/species fields while also resolving gas feedback. Priority 3 is causal isolation at ignition: acquire mixture, temperature or radical proxies, ignition location, and heat release under controlled changes that separate wave interaction from momentum, dwell, and mass flow. Explicit timescale endpoints and bounded strong-wave mappings support these three tiers but do not replace them."""
text = replace_once(text, anchor, priority, "TAB08 priority synthesis")
text = replace_once(text, "Detonation and RDE calculations can test sensitivity to post-wave thermochemistry and characteristic scales, but any use in HPDI requires an explicit mapping of load, residence, population, and reaction times. TAB-08 organizes these measurements and models by the variable that crosses each interface and the observable needed for validation.", "Detonation and RDE calculations can test sensitivity to post-wave thermochemistry and characteristic scales, but any use in HPDI requires an explicit mapping of load, residence, population, and reaction times.", "remove generic TAB08")

# Repair Python control-character escapes in LaTeX sequences introduced above.
text = text.replace("\r" + "ho", r"\rho")
text = text.replace("\t" + "au", r"\tau")
text = text.replace("\b" + "mathbf", r"\mathbf")
TARGET.write_text(text, encoding="utf-8")
print(f"Created {TARGET}")
