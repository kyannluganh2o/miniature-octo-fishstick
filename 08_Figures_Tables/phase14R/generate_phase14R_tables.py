from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "08_Figures_Tables" / "phase14R"
TABLES = OUT / "tables"
TABLES.mkdir(parents=True, exist_ok=True)


def write_table(name: str, headers: list[str], rows: list[list[str]]):
    with (TABLES / f"{name}.csv").open("w", encoding="utf-8-sig", newline="") as stream:
        writer = csv.writer(stream)
        writer.writerow(headers)
        writer.writerows(rows)


write_table(
    "TAB-01",
    ["Parameter", "Physical role", "Required definition", "Common ambiguity", "Comparison rule"],
    [
        ["NPR", "Underexpansion and momentum-flux control", "Upstream/downstream pressures; locations; total/static; absolute basis; time", "Rail/chamber vs plenum/ambient; nominal vs instantaneous", "Match pressure roles, gas, nozzle, ambient state, and transient stage"],
        ["Mach number", "Compressibility and wave strength", "Object; frame; sound-speed state; location; time", "M_s vs post-wave M vs M_rel vs detonation-front Mach", "Separate incident, post-wave, droplet-relative, and front values"],
        ["Weber number", "Aerodynamic stress relative to surface tension", "rho_g; relative velocity; length; sigma; thermodynamic state", "Pre/post-wave density; parent/fragment diameter; velocity frame", "Compare only definition-complete, state-matched values"],
        ["Reynolds number", "Inertial transport relative to viscous transport", "rho; velocity; length; viscosity; phase; state; frame", "Gas vs liquid viscosity; freestream vs post-wave state", "Use as a companion condition to the loading history"],
        ["Ohnesorge number", "Liquid viscous resistance to capillary-inertial response", "Liquid viscosity, density, sigma, length, and temperature", "Parent vs fragment scale; temperature-dependent properties", "Match liquid state and characteristic length"],
        ["Loading duration", "Exposure to pressure and slip forcing", "Start/end events; front passage, post-wave residence, or full forcing", "Shock transit vs compressed-gas residence", "Retain event definitions; avoid universal pooling"],
        ["Breakup time", "Response clock", "Onset, first shedding, rupture, or completion; normalization", "Onset vs completion; dimensional vs normalized time", "Compare the same event and normalization"],
        ["Signed ΔSOI", "Pilot/main chronology", "Target event minus reference event; fuel order; event type; unit", "Opposite sign; electronic vs hydraulic vs actual SOI", "State named events, sign convention, speed, and operating point"],
        ["L_E/L_D", "Liquid-survival distance relative to a device scale", "Evaporation endpoint and denominator length", "Front height vs cell, induction, or refill scale", "Use within the reported strong-wave domain"],
    ],
)

write_table(
    "TAB-02",
    ["Study", "Gas / nozzle", "Pressure definition", "NPR / pressure range", "Ambient state", "Transient stage", "Mach-disk / topology metric", "Comparison scope"],
    [
        ["[[CITE:B009]] H2 series", "H2; converging exit D=1.5 mm", "Nozzle total / ambient static", "NPR 8.5, 10, 30, 70", "98.37 kPa; 296 K", "Semi-steady after transient overshoot", "x_MD/D = 1.85, 2.06, 3.77, 5.81; derived from reported x_MD and D", "Within-study NPR trend"],
        ["[[CITE:B009]] CH4 case", "CH4; same D=1.5 mm nozzle", "Same total/static roles", "NPR 8.5", "98.37 kPa; 296 K", "Semi-steady", "x_MD/D = 1.90; derived", "Gas-species contrast within one setup"],
        ["[[CITE:B021]] steady/unsteady case", "H2; convergent exit D=1 mm", "Plenum total / chamber static", "NPR 12.7 representative comparison", "Case-specific chamber state", "Steady and unsteady", "Mach-disk position and H2 radial profiles", "Instantaneous vs steady topology"],
        ["[[CITE:B029]] pressure-build cases", "H2 injector; internal restriction and volume case-specific", "Injector-internal p_inj(t); measurement location retained", "Time-dependent histories", "Transient test state", "Opening to stabilization", "Pressure, penetration, velocity, and Mach-contour evolution", "Event alignment across pressure-build histories"],
    ],
)

write_table(
    "TAB-03",
    ["Source / case", "Loading", "Mach", "We", "Re / Oh", "d0 / liquid", "Loading duration", "Response", "Boundary"],
    [
        ["[[CITE:C016]] C01", "Incident shock + post-shock airflow", "M_s=1.12", "219; post-shock airflow definition", "Re=13,000; Oh=NR", "2.5 mm water", "NR", "SIE", "Source taxonomy; no universal threshold"],
        ["[[CITE:C016]] C02", "Incident shock + post-shock airflow", "M_s=1.30", "1600; same definition", "Re=40,000; Oh=NR", "2.9 mm water", "NR", "SIE", "Mach and We vary together"],
        ["[[CITE:C016]] C03", "Incident shock + post-shock airflow", "M_s=1.12", "44; same definition", "Re=2500; Oh=NR", "0.5 mm water", "NR", "RTP", "Diameter and Re vary with We"],
        ["[[CITE:C016]] C04", "Incident shock + post-shock airflow", "M_s=1.45", "795; same definition", "Re=12,000; Oh=NR", "0.5 mm water", "NR", "RTP", "Mach and We vary together"],
        ["[[CITE:C025]] M2", "Analytic post-shock gas load", "M_s=2", "822; post-shock rho_g |u_rel|^2 d0/sigma", "NR", "100 µm water", "NR", "Deformation and atomized-mass statistics", "Numerical case; source-defined response"],
        ["[[CITE:C025]] M3", "Analytic post-shock gas load", "M_s=3", "3760; same definition", "NR", "100 µm water", "NR", "Piercing and atomized-mass transfer", "Two-case numerical comparison"],
        ["[[CITE:C014]] C01-C08", "Uniform post-shock freestream", "M_infinity=0.30-1.19", "1050-1160; post-shock rho_g |u_g|^2 d0/sigma", "Re=2600-24,000; Oh=0.002-0.044", "NR; water or ethylene glycol", "NR", "Peripheral mist, multiple bags, leeward ligaments", "Matched-We morphology remains Mach- and material-dependent"],
        ["[[CITE:D018]] water / RP-3", "Reacting detonation products", "Front Mach about 6.03-7.07", "3.10×10^4-5.67×10^5; averaged post-detonation state", "Oh=0.0039-0.0223", "0.25-1.27 mm water / RP-3", "Reacting-wave history", "Complete-breakup t*=10.06 water; 7.90 RP-3", "Reacting strong-wave analogue"],
        ["[[CITE:D019]] reacting / inert pair", "Matched-leading-Mach detonation and inert shock", "Incident Mach 4.8", "5.42×10^4 detonation; 3.18×10^5 inert", "Re=4.80×10^4 / 2.00×10^5; Oh=NR", "4.8 mm water", "O(10^-4 s) deformation scale", "Distinct deformation and cavitation histories", "Equal leading Mach does not imply equal post-wave load"],
    ],
)

write_table(
    "TAB-04",
    ["Configuration", "Source", "Spacing / population descriptor", "Loading", "Collective mechanism", "Response", "Dense-spray implication"],
    [
        ["Isolated droplet", "[[CITE:C016]]", "NA", "Incident shock + post-shock airflow", "Single-body response", "SIE / RTP under case-specific M_s, We, Re, d0", "No shielding, attenuation, vaporization, or reaction"],
        ["Tandem pair", "[[CITE:C035]]", "Streamwise S/D=1.2-10.5", "Post-shock gas; We=13-180", "Wake shielding; altered trailing-droplet slip", "Spacing-dependent differential deformation", "Ordered pair; orientation-specific"],
        ["Parallel pair", "[[CITE:C036]]", "Transverse L/D<0.1 to >2", "Post-wave gas; We O(10)-O(100)", "Squeeze flow; channel opening / closure", "Bag, trailing, shuttlecock, open, and closed modes", "Pair-scale phase boundaries"],
        ["Dilute cloud", "[[CITE:C033]] [[CITE:C034]]", "Cloud height, volume fraction, number density", "Shock transmission through water-droplet cloud", "Wave attenuation; fragmentation feedback", "Pressure attenuation and broadened transmitted load", "Cloud descriptor not convertible to pair spacing"],
        ["Dense polydisperse reacting HPDI spray", "Direct dense-HPDI validation absent", "Joint size, spacing, volume fraction, velocity, temperature, vapor", "Transient two-way gas-liquid coupling", "Combined shielding, channel flow, attenuation, phase change", "Unresolved population response", "Direct measurement and validation required"],
    ],
)

write_table(
    "TAB-05",
    ["Source / domain", "Liquid / size", "Thermal state", "Loading", "Phase-change mechanism", "Aerodynamic effect", "Liquid-property effect", "Observed response", "Applicability boundary"],
    [
        ["[[CITE:C024]] shock tube", "Acetone; 14.16-37.3 µm parent distribution", "Heated post-shock flow", "M about 2.09; high We", "Fragmentation-evaporation overlap", "Fragment-cloud growth", "Volatile liquid; temperature-dependent loss", "Cloud disappearance about 250-300 µs", "Optical disappearance not equal to vapor mass"],
        ["[[CITE:C026]] shock tube", "Acetone / water; about 55-200 µm", "Case-specific post-shock heating", "Mach and We combinations", "Evaporation weak for deformation above about 100 µm", "Early deformation and acceleration", "Size and volatility condition thermal influence", "Breakup-initiation morphology; large-drop response weakly altered by evaporation", "Short early-time window"],
        ["[[CITE:C027]] locally supersonic flow", "2-propanol, Hex-Pen, TGDE", "Bow-shock pressure rise vs vapor pressure", "Droplet-relative supersonic flow", "Superheating and vaporization bounded by local pressure", "Breakup across accelerating flow", "Higher volatility favors superheating response", "Liquid-dependent disruption and fluorescence field", "Facility-specific pressure and residence history"],
        ["[[CITE:C031]] 3-D simulation", "n-dodecane; modeled droplet", "No phase change / evaporation / condensation", "Planar shock; Mach-family cases", "Cool vapor layer / blowing", "Reduced interfacial shear; KH suppression", "Evaporation smooths interface; condensation strengthens shear", "Distinct deformation and vorticity histories", "Coefficient-dependent phase-change model"],
        ["[[CITE:C032]] high-temperature gas", "n-decane; modeled droplet", "600-1000 K", "We=15-90", "Heating and evaporation", "Breakup promoted at lower We and higher T", "Reduced surface tension; volatility dependence", "Temperature-dependent shape and breakup-time response", "Single-droplet numerical domain"],
        ["[[CITE:D017]] liquid-fueled detonation", "Fuel droplets; d0=1-120 µm", "Post-detonation products", "Variable post-front history", "Breakup-evaporation overlap", "Child production raises surface area", "Model-specific heat/mass transfer", "Breakup reduces predicted survival by about 1-2 orders; closures differ", "Within-study model comparison; detonation domain"],
    ],
)

write_table(
    "TAB-06",
    ["Source", "Fuel / platform", "Injection order / ΔSOI", "Geometry / condition", "Mixture response", "Ignition response", "Heat-release response", "Scope"],
    [
        ["[[CITE:A001]]", "Diesel pilot / natural gas engine", "Engine-program timing", "Load and speed map; gas-pressure sweep", "High-pressure mixing benefit strongest at high load", "NR", "Shorter combustion duration; weaker speed effect", "Engine-specific operating map"],
        ["[[CITE:A002]]", "Diesel pilot / natural gas HPDI engine", "Engine-program timing", "Gas rail 300-600 bar; load/speed sweep", "Higher injection rate; improved late-cycle mixing", "Ignition comparatively less pressure-sensitive", "Shorter mixing-controlled burn; higher harshness / NOx", "Pressure benefit and penalty depend on operating point"],
        ["[[CITE:A005]]", "Diesel pilot / natural gas engine", "Paired-hole configuration; case-specific timing", "Nearby gas-hole pairs", "Greater early entrainment; rich moderate-temperature residence", "NR", "Higher particulate matter despite entrainment gain", "Geometry-specific soot interpretation"],
        ["[[CITE:A007]]", "Diesel pilot / natural gas RCEM", "Gas SOI - pilot SOI = -2.5 to +1.5 ms", "Jet angle and overlap sweep", "Spatial-temporal interaction sets premixing", "Pilot/gas ignition trade-off", "Ignition-relative-to-SOI organizes HRR", "No shock attribution; RCEM boundary"],
        ["[[CITE:A009]]", "Diesel pilot / natural gas RCM", "Relative pilot/gas timing", "Ambient pressure and temperature sweep", "Timing controls natural-gas premixing", "Lower-state pilot ignition more vulnerable to adjacent jet", "Premixed / mixing-controlled response shifts", "Free-jet configuration"],
        ["[[CITE:A011]]", "Diesel pilot / natural gas optical engine", "Relative pilot/gas timing", "Injection-pressure and timing sweep", "NG stratification and premixing vary with chronology", "NG ignition weakly sensitive to pressure", "Non-premixed to partially premixed to stratified premixed modes", "Optical-engine geometry and line-of-sight imaging"],
        ["[[CITE:A013]]", "Pilot-ignited direct-injected natural gas engine", "Relative injection timing sweep", "140-220 bar; gas fraction and timing varied", "Timing domains represent NG stratification", "Pilot and NG combustion phasing vary by regime", "Six stratified-combustion regimes", "Paper-specific RIT definition"],
        ["[[CITE:A020]]", "n-heptane pilot / H2 CVCC", "H2-first and pilot-first; 0.07-3.07 ms separation", "Converging single-hole jets; temperature sweep", "Finite interaction with reacting pilot products", "Distinct pilot and H2 ignition events", "Long-delay cases show slower propagation and variability", "Quiescent chamber; paper-specific ignition thresholds"],
        ["[[CITE:A022]]", "Diesel pilot / H2 CVCC", "Pilot SOI 0.6 ms after H2 SOI", "12, 15, and 19 deg interaction geometries", "Angle changes jet overlap and entrainment", "Greater overlap shortens pilot-to-main transition in tested cases", "Geometry-conditioned stabilization / AHRR", "No universal angle scalar"],
        ["[[CITE:A026]]", "Diesel pilot / H2 optical engine", "H2 SOI 0-30 CA bTDC; pilot SOI 6 CA bTDC", "H2 energy share 70-95%", "Timing changes preignition dilution and premixing", "Advanced H2 timing can delay pilot ignition", "Pilot energy strengthens early H2 reaction; late phase similar", "Electronic SOI; line-of-sight flame imaging"],
    ],
)

write_table(
    "TAB-07",
    ["Source", "Domain", "Liquid / d0", "Wave descriptor", "Post-wave / residence scale", "Breakup / evaporation scale", "Observed response", "HPDI-relevant variable", "Transfer boundary"],
    [
        ["[[CITE:D009]]", "Two-phase RDE simulation", "Kerosene; 2-5 µm", "Mean rotating-wave speed by case", "RDE refill and front height", "L_E/L_D=0.13-0.84", "Larger d0 increases liquid persistence; 2-4 µm paired cases show lower wave speed", "Liquid-survival / residence ratio", "RDE-specific denominator and chemistry"],
        ["[[CITE:D013]]", "Two-phase RDE", "Reported 20 and 30 µm cases", "Rotating-wave structure", "Device refill layer", "NR", "Liquid persistence reorganizes wave structure", "Population residence and wave feedback", "Device-level feedback"],
        ["[[CITE:D014]]", "Two-phase ethanol RDE", "Ethanol droplet population", "Wave-relative droplet grouping", "Leading, trailing, and downstream histories", "Thermal impulse and evaporation history", "Near-front droplets heat and evaporate rapidly; downstream groups respond gradually", "Wave-relative position; temperature; residence", "RDE kinematics and thermochemistry"],
        ["[[CITE:D017]]", "Liquid-fueled detonation experiment / model", "Fuel droplets; 1-120 µm", "Post-detonation survival region", "Measured cloud persistence", "Extinction distance by breakup closure", "Breakup branches shorten survival relative to no-breakup; closures bracket observations", "Fragment size and survival distance", "Reduced breakup models; detonation products"],
        ["[[CITE:D018]]", "Planar detonation experiment", "Water / RP-3; 0.25-1.27 mm", "Front Mach about 6-7", "Reacting post-wave history", "Complete-breakup t*=10.06 / 7.90", "Liquid-dependent KHI-RTI sequence", "Material state and local slip", "High-We reacting strong wave"],
        ["[[CITE:D019]]", "Reacting detonation vs inert shock simulation", "Water; d0=4.8 mm", "Matched incident Mach 4.8", "Distinct post-wave We/Re and pressure gradients", "O(10^-4 s) deformation scale", "Wave topology, deformation, and cavitation diverge", "Post-wave state beyond leading Mach", "2-D geometry; surface tension / viscosity omitted"],
    ],
)

write_table(
    "TAB-08",
    ["Coupling problem", "Established physics", "Missing quantity", "Required diagnostics", "Model requirement", "Scientific significance"],
    [
        ["Pilot-droplet loading in transient underexpanded jets", "Injector transients move shock cells; imposed shocks deform droplets", "p[x_d,t], rho_g[x_d,t], vector u_rel(t), direction, duration", "Needle / pressure; density-gradient field; gas velocity; droplet tracking", "Transient injector flow sampled along measured liquid trajectories", "Mach-disk visibility does not define droplet We or impulse"],
        ["Canonical breakup in dense reacting sprays", "Shielding, squeeze flow, channel closure, and attenuation alter loading", "Joint size-spacing-velocity-temperature statistics and gas feedback", "3-D liquid imaging; gas pressure / velocity; transmitted-wave measurements", "Polydisperse two-way coupling with phase change and reaction", "Ordered-pair laws cannot close dense-spray response"],
        ["Fragment contribution to pre-ignition mixture", "Fragment state and residence control evaporation and transport", "Mass-resolved fragments, vapor/species field, thermal state, ignition time", "Fragment sizing / tracking; temperature; species imaging; common event clock", "Product distribution coupled to evaporation and turbulent transport", "Breakup alone does not imply vapor in the ignition region"],
        ["Wave-induced mixture change and ignition", "Chronology, geometry, oxygen, temperature, and pilot products control ignition", "Wave-induced mixture increment and ignition-kernel overlap", "Wave, liquid, species, temperature/radical proxy, ignition, heat release", "Uncertainty propagation from load to fragments to chemistry", "Ignition-delay change is not causal proof of wave-mediated breakup"],
        ["Loading / response timescale competition", "Front passage, post-wave residence, and deformation clocks differ", "Explicit tau_load endpoints and source-defined tau_response", "Event-resolved load history and morphology", "Test competing clocks without universal-ratio assumption", "Undefined time ratios create false correlations"],
        ["Strong-wave transfer to HPDI", "Local post-wave pressure, density, slip, size, and residence affect droplets", "Mapping of thermochemistry, geometry, residence, population, reaction scale", "Domain-specific post-wave state and liquid-survival measurements", "Dimensional mapping with failure bounds", "RDE L_E/L_D is a comparison scale, not an HPDI ignition predictor"],
    ],
)

captions = r"""# Phase 14R Working Table Captions

## TAB-01

Physical definitions and comparison rules for pressure ratio, Mach number, dimensionless loading groups, timing, and characteristic lengths.

## TAB-02

Representative underexpanded-jet conditions and Mach-disk or topology comparison scope. Derived \(x_{\mathrm{MD}}/D\) values are identified explicitly and remain within-study comparisons.

## TAB-03

Compressible droplet-response conditions and source-defined morphologies. SIE = shear-induced entrainment; RTP = Rayleigh-Taylor piercing; NR = not reported.

## TAB-04

Collective mechanisms across isolated, tandem, parallel, and cloud configurations, with the direct dense-HPDI validation boundary retained.

## TAB-05

Phase-change competition across liquid size, thermal state, loading, interfacial aerodynamics, and temperature-dependent liquid properties.

## TAB-06

Representative HPDI and dual-direct-injection cases linking relative timing and geometry to mixture preparation, ignition, and heat-release response. ΔSOI retains each source's named events and sign convention.

## TAB-07

Strong-wave comparison cases organized by post-wave state, residence, breakup, and evaporation scales, with explicit limits on transfer to HPDI.

## TAB-08

Unresolved physical couplings, missing quantities, synchronized diagnostics, and model requirements for connecting transient loading to ignition response.
"""
(OUT / "working_table_captions.md").write_text(captions, encoding="utf-8")

print(f"Generated eight Phase 14R tables under {TABLES}")
