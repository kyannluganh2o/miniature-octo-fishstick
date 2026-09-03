from __future__ import annotations

from pathlib import Path


HERE = Path(__file__).resolve().parent
SOURCE = HERE / "phase14_figtable_informed_draft.md"
TARGET = HERE / "phase14R_harmonized_draft.md"

text = SOURCE.read_text(encoding="utf-8")
text = text.replace("# Phase 13R Physics-Led Working Draft", "# Phase 14R Physics-Led Harmonized Draft", 1)

replacements = {
    "For a fixed nozzle and consistent pressure roles, increasing NPR moves the Mach disk downstream and usually enlarges it [[CITE:B003]] [[CITE:B009]] [[CITE:B021]]. The square-root-type position scalings often used for steady jets capture this direction, but transient overshoot and injector-specific exit conditions change the instantaneous coefficient. Disk diameter, curvature, appearance threshold, and cell wavelength are less consistently constrained than axial position [[CITE:B004]]. TAB-02 therefore separates the geometric feature, nozzle-diameter basis, and developing or settled state for every comparison. The case-level audit retained one definition-complete numerical sequence for plotting: within the B009 semi-steady hydrogen series, NPR values of 8.5, 10, 30, and 70 correspond to derived `x_MD/D` values of 1.85, 2.06, 3.77, and 5.81, respectively; the methane case at NPR 8.5 gives 1.90 under the same nozzle and ambient state [[CITE:B009]]. This is a within-study trend, not a cross-paper coefficient.":
    "For a fixed nozzle and consistent pressure roles, increasing NPR moves the Mach disk downstream and usually enlarges it [[CITE:B003]] [[CITE:B009]] [[CITE:B021]]. The square-root-type position scalings often used for steady jets capture this direction, but transient overshoot and injector-specific exit conditions change the instantaneous coefficient. Disk diameter, curvature, appearance threshold, and cell wavelength are less consistently constrained than axial position [[CITE:B004]]. TAB-02 therefore separates the geometric feature, nozzle-diameter basis, and developing or settled state for every comparison. Within the B009 semi-steady hydrogen series, NPR values of 8.5, 10, 30, and 70 correspond to derived \(x_{\mathrm{MD}}/D\) values of 1.85, 2.06, 3.77, and 5.81; the methane case at NPR 8.5 gives 1.90 under the same nozzle and ambient state [[CITE:B009]]. This within-study sequence establishes the expected pressure-ratio trend without defining a cross-paper coefficient.",

    "The unavailable C004 source limits a broad treatment of Newtonian and viscoelastic taxonomy, so its primary conclusions are not reconstructed here from secondary descriptions. The available studies nevertheless define the central modeling requirement: downstream spray and combustion calculations need a time-dependent product state, not merely a parent-droplet regime label. Once multiple droplets are present, even the imposed load changes through wakes and wave attenuation, adding a second level of closure beyond single-droplet breakup.":
    "The available studies define the central modeling requirement: downstream spray and combustion calculations need a time-dependent product state, not merely a parent-droplet regime label. Once multiple droplets are present, even the imposed load changes through wakes and wave attenuation, adding a second level of closure beyond single-droplet breakup.",

    "FIG-05 summarizes the progression from isolated response to pair interaction and population feedback. Dilute clouds reveal the mechanism cleanly, but dense pilot sprays add rapid vaporization, broad size and velocity distributions, turbulence, collisions, and possible reaction. These features determine which pair- and cloud-scale processes remain recognizable in an injector spray.":
    "FIG-05 compares isolated, tandem, parallel, and cloud configurations rather than presenting a temporal progression. Each configuration introduces a different collective mechanism: wake shielding for streamwise pairs, squeeze flow and channel closure for transverse pairs, and attenuation with population feedback for clouds. Dense pilot sprays additionally contain polydispersity, rapid vaporization, turbulence, collisions, and possible reaction, so transfer from these canonical configurations remains open.",

    "FIG-07 follows the physical chronology from injection events and jet trajectories to mixture stratification. TAB-06 retains the fuel order, event definition, angle, operating point, and ignition metric needed to compare different configurations. Once overlap occurs, the next process is thermochemical: pilot products can heat and seed the main mixture, while the main jet can dilute or displace the pilot.":
    "FIG-07 uses relative chronology: signed \(\Delta\mathrm{SOI}\) is defined from named pilot and main-fuel events, with fuel order, event type, and geometry retained. TAB-06 preserves the operating point and ignition metric needed to compare configurations. Once overlap occurs, the next process is thermochemical: pilot products can heat and seed the main mixture, while the main jet can dilute or displace the pilot. The direct timing/geometry pathway is therefore separated from the hypothesized wave-mediated fragment pathway.",

    "Rotating-detonation calculations define one such ratio as the evaporation distance divided by detonation-front height. In a simulated kerosene family with no pre-evaporated fuel, increasing initial diameter lengthened evaporation distance, enlarged fuel-lean or unburned pockets, reduced wave speed, and eventually produced shock–flame decoupling [[CITE:D009]]. Adding pre-vaporized fuel restored a more reactive upstream mixture. The ratio organizes those cases because its numerator and denominator describe the same refill and wave geometry. In the paired D009 cases, increasing `L_E/L_D` from 0.13 to 0.55 as `d0` increases from 2 to 4 µm accompanies a decrease in mean rotating-wave velocity from 1728 to 1618 m/s [[CITE:D009]]. The 5 µm case reports `L_E/L_D = 0.84` but lacks a paired wave-velocity value in the current extraction, so it is retained in the registry but excluded from the plot. This remains a within-study RDE relation.":
    "Rotating-detonation calculations define one such ratio as the evaporation distance divided by detonation-front height. In a simulated kerosene family with no pre-evaporated fuel, increasing initial diameter lengthened evaporation distance, enlarged fuel-lean or unburned pockets, reduced wave speed, and eventually produced shock–flame decoupling [[CITE:D009]]. Adding pre-vaporized fuel restored a more reactive upstream mixture. The ratio organizes those cases because its numerator and denominator describe the same refill and wave geometry. In the paired D009 cases, increasing \(L_E/L_D\) from 0.13 to 0.55 as \(d_0\) increases from 2 to 4 µm accompanies a decrease in mean rotating-wave velocity from 1728 to 1618 m/s [[CITE:D009]]. The 5 µm case reports \(L_E/L_D=0.84\), but no paired wave-velocity value is available. This remains a within-study RDE relation.",

    "Breakup can shorten the liquid-survival scale by generating small, rapidly heated children. Detonation experiments with micrometre-scale fuel droplets show a finite survival region that evaporation-only calculations greatly overpredict for larger droplets; breakup models reduce the distance by increasing surface area [[CITE:D017]]. The variable post-front velocity and pressure history, however, causes different breakup closures to bracket rather than reproduce all observations. At `d0 = 10 µm` in the D017 model family, the reported extinction distance is 37.05 mm without breakup, 0.32 mm with KH–RT breakup, and 0.93 mm with WERT49 breakup [[CITE:D017]]. The order-of-magnitude spread at fixed diameter shows that a diameter trend cannot be separated from the product-generation closure.":
    "Breakup can shorten the liquid-survival scale by generating small, rapidly heated children. Detonation experiments with micrometre-scale fuel droplets show a finite survival region that evaporation-only calculations greatly overpredict for larger droplets; breakup models reduce the distance by increasing surface area [[CITE:D017]]. Across the reported model family, including breakup reduces predicted survival by roughly one to two orders of magnitude, while the KH-RT and WERT49 closures remain distinct. At \(d_0=10\) µm, the reported extinction distance is 37.05 mm without breakup, 0.32 mm with KH-RT breakup, and 0.93 mm with WERT49 breakup [[CITE:D017]]. The spread at fixed diameter shows that parent-size trends cannot be separated from the product-generation closure or from the variable post-front history.",

    "Detonation and RDE calculations can test sensitivity to post-wave thermochemistry and characteristic scales, but any use in HPDI requires an explicit mapping of load, residence, population, and reaction times. The missing C004 PDF remains a narrower source limitation on breakup-taxonomy coverage rather than a missing physical coupling. TAB-08 organizes these measurements and models by the variable that crosses each interface and the observable needed for validation.":
    "Detonation and RDE calculations can test sensitivity to post-wave thermochemistry and characteristic scales, but any use in HPDI requires an explicit mapping of load, residence, population, and reaction times. TAB-08 organizes these measurements and models by the variable that crosses each interface and the observable needed for validation.",
}

for old, new in replacements.items():
    if old not in text:
        raise RuntimeError(f"Expected paragraph not found: {old[:100]}")
    text = text.replace(old, new, 1)

notation_replacements = {
    "At each instant, the aerodynamic slip is `u_rel(t) = u_g[x_d(t),t] - u_d(t)`, and the associated dynamic load scales with `ρ_g u_rel²`.":
    "At each instant, the aerodynamic slip is \(\mathbf{u}_{\mathrm{rel}}(t)=\mathbf{u}_g[\mathbf{x}_d(t),t]-\mathbf{u}_d(t)\), and the associated dynamic load scales with \(\\rho_g|\mathbf{u}_{\mathrm{rel}}|^2\).",
    "droplet or ligament tracking must provide (x_d(t)), (u_d(t)), and size.":
    "droplet or ligament tracking must provide \(\mathbf{x}_d(t)\), \(\mathbf{u}_d(t)\), and size.",
    "`p[x_d(t),t]`, `ρ_g[x_d(t),t]`, `u_rel(t)`":
    "\(p[\mathbf{x}_d(t),t]\), \(\\rho_g[\mathbf{x}_d(t),t]\), \(\mathbf{u}_{\mathrm{rel}}(t)\)",
    "The characteristic denominator in `L_E/L_D`":
    "The characteristic denominator in \(L_E/L_D\)",
}
for old, new in notation_replacements.items():
    if old not in text:
        raise RuntimeError(f"Expected notation string not found: {old}")
    text = text.replace(old, new)

for forbidden in ("C004", "current extraction", "retained in the registry", "excluded from the plot", "case-level audit"):
    if forbidden.lower() in text.lower():
        raise RuntimeError(f"Forbidden reader-facing term remains: {forbidden}")

TARGET.write_text(text, encoding="utf-8")
print(TARGET)
