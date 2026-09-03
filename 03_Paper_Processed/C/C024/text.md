<!-- PDF_PAGE: 1 -->

International Journal of Multiphase Flow 161 (2023) 104389
Available online 18 January 2023
0301-9322/© 2023 Elsevier Ltd. All rights reserved.
Contents lists available at ScienceDirect
International Journal of Multiphase Flow
journal homepage: www.elsevier.com/locate/ijmulflow
Experiments on the breakup and evaporation of small droplets at high Weber
number
Vasco Duke-Walker, Benjamin J. Musick, Jacob A. McFarland∗
Mechanical Engineering, Texas A&M University, College Station, 77840, TX, USA
A R T I C L E I N F O
Keywords:
Breakup
Evaporation
Deformation
Parent droplet
Child droplet
Droplet cloud
A B S T R A C T
Shock-driven multiphase mixing is present in numerous physical systems such as detonation-driven propulsion
engines, liquid–vapor cloud explosions, and hypersonic flight droplet impacts. At the microscale, droplets
experience deformation, breakup, and evaporation under extreme conditions (high Weber and Reynolds
regimes). For small droplets, these phenomena are simultaneous and highly transient, making their interactions
and interdependencies warrant further investigation. In this study, experiments are conducted in a shock
tube facility to investigate these simultaneous droplet-scale phenomena. An interface consisting of small
acetone droplets ( ⌀ 10–40 [μm]) is impulsively accelerated by a strong planar shock wave (Mach ∼ 2 .09).
The droplet size distribution is well-characterized in-situ utilizing a Phase Doppler Particle Analyzer (PDPA)
and shadowgraphy. The development of child droplet clouds is captured through an ensemble of Mie scattering
images. A simplified model is developed to interpret the experimental results, combining deformation, breakup,
and evaporation models. The results indicate that the breakup of small droplets at high Weber numbers is likely
dominated by the Rayleigh–Taylor (RT) mechanism, aligning with previous empirical models for low Weber
numbers.
1. Introduction
Many extreme environments exist where droplets will encounter
high-speed impulsive acceleration resulting in droplet deformation,
breakup, and evaporation due to aerodynamic forces and strong tem-
perature gradients. Such environments can be as varied as droplet
impact on hypersonic flight vehicles, blast and detonation mitigation
in process safety, explosive dispersal of chemical compounds, and high-
speed combustion in detonation-cycle engines. In order to model and
thoroughly understand the relevant physics of an evolving droplet, an
understanding of the broader field of shock-driven multiphase mixing
is needed, from the cloud-scale (macroscale) down to the individual
droplet dynamics (microscale). In this discussion, note that the term
particle is used when referring to physics applicable to any discrete
phase, while the term droplet is used when discussing physics unique
to liquid particles.
Shock-driven multiphase mixing can be divided into two regimes:
the macroscale (motions of droplet groups) and the microscale (in-
dividual droplets). On the macroscale, the evolution of multiphase
fluid mixture interfaces is considered in the SDMI, including hydro-
dynamic mixing, vorticity deposition, and particle lag effects (velocity
equilibration time). Further, evaporation can be limited by large-scale
∗ Corresponding author.
E-mail addresses: vascoduke@tamu.edu (V. Duke-Walker), mcfarlandja@tamu.edu (J.A. McFarland).
URL: https://fmecl.engr.tamu.edu (V. Duke-Walker).
mixing of the particle and vapor phase, introducing particles to new
dry gas. More importantly, understanding the macroscale can be further
improved by exploring critical physical phenomena on the microscale,
such as breakup and evaporation, which drive the behaviors at larger
scales. Breakup and evaporation are relevant because they alter particle
response times and limit vapor mixing rates.
High-speed single droplet breakup has mostly been considered with-
out evaporation; however, as the size of the droplets becomes smaller,
evaporation becomes more dominant. Goossens et al. ( 1988) studied
experimentally shock strength effects on evaporation with small stable
water droplets, 0.5 < 𝑑 𝑝 < 2 [μm], showing good agreement with simple
evaporation models. Paudel et al. (2018) performed full 3D simulations
at Mach 1.65 and droplet size 𝑑𝑝 < 10 [μ m], and showed disparities
in the case of evaporating and non-evaporating droplets. Paudel et al.
(2018) suggested that evaporation and droplet size play a strong role
in the hydrodynamic development of the SDMI, with time scales for
momentum equilibration and evaporation being strongly dependent on
droplet size. It was observed that large droplets start to lag behind the
flow, inducing small-scale perturbations and reducing hydrodynamic
growth. In contrast, small droplets would equilibrate and evaporate
quickly, producing more classic Richtmyer–Meshkov instability (RMI)
https://doi.org/10.1016/j.ijmultiphaseflow.2023.104389
Received 12 October 2022; Received in revised form 15 December 2022; Accepted 9 January 2023

<!-- PDF_PAGE: 2 -->

International Journal of Multiphase Flow 161 (2023) 104389
2
V. Duke-Walker et al.
behavior (Dahal and McFarland, 2017; Black et al., 2017). These were
further investigated and presented experimentally at Mach 1.65, and
2 < 𝑑 𝑝 < 11 [μ m] by Middlebrooks et al. (2019), in which a sec-
ond droplet breakup event occurred at re-shock (second acceleration
by reflected shock wave), evaporating the droplets nearly instanta-
neously. Further experimental work by Duke-Walker et al. (2020) was
performed to understand the coupled effect on droplet breakup and
evaporation using acetone droplets at Mach 1.65 and 𝑑𝑝 = 10 [μ m].
This work showed that droplet breakup contributed significantly to the
evaporation process at early time; however, evaporation was limited by
hydrodynamic mixing at late times.
At the microscale, small droplets subjected to sudden acceleration
from a shock will experience aerodynamic forces leading to droplet
deformation, breakup, and finally evaporation. The Momentum equili-
bration rate, which is the rate at which particles adjust to changes in the
flow field velocity, is the most significant factor affecting macroscale
shock-driven multiphase mixing and is primarily controlled by breakup
rates and final child droplet sizes.
Droplet breakup phenomena are divided into various regimes de-
scribed by the Weber number, 𝑊 𝑒 = 𝜌𝑔𝑣2
𝑝𝑔𝑑𝑝∕𝜎, the ratio of inertial
to surface tension effects, Reynold’s number, 𝑅𝑒 = 𝜌𝑔𝑑𝑝𝑣𝑝𝑔∕𝜇, inertial
to viscous effects, and Ohnesorge number, 𝑂ℎ = 𝜇∕√𝜌𝜎𝑑𝑝, relating
viscous to inertial and surface tensions forces. Here 𝜌𝑔 is the density
of the gas, 𝑣𝑝𝑔 = |𝑣𝑔 − 𝑣𝑝| the relative droplet to gas velocity, 𝑑𝑝 the
initial parent droplet diameter, and 𝜎 the surface tension of the liquid
droplet. The critical Weber number is determined when 𝑂ℎ < 0.1 from
𝑊 𝑒𝑐 = 12 ⋅ (1 + 𝑂ℎ1.6) from Pilch and Erdman (1987), indicating that
breakup will occur for low viscosity fluids at a 𝑊 𝑒 ∼ 12 . At low
𝑊 𝑒, various breakup regimes exist that result from the combination of
Rayleigh–Taylor and capillary instabilities (Kirar et al., 2022). For the
flow conditions considered in this paper, the droplet breakup process is
expected to be in the high 𝑊 𝑒, shear stripping or catastrophic regimes,
depending on the reference source for breakup regimes.
Several empirical models have been analyzed for low 𝑊 𝑒 in the
bag and stamen breakup regimes, providing accurate results of the
breakup time and the representative Sauter mean diameter of the child
droplets (Hsiang and Faeth, 1992; Wert, 1995). Hsiang and Faeth
(1992) proposed that child droplet sizes are based on the growth of
the liquid boundary layer thickness. Their proposed size correlation is
valid for 𝑊 𝑒 < 103 and 𝑂ℎ < 0.1. Wert (1995) proposed a model based
on linear stability theory for capillary waves in the toroidal ring of the
bag breakup regime, tuned with experimental data from Hsiang and
Faeth (1992) for large droplets 𝑑𝑝 > 500 [μ m]. Furthermore, the same
breakup model (Wert, 1995), was tuned by Duke-Walker et al. (2021)
in simulation efforts to match experimental data for small droplet
𝑑𝑝 = 10 [μ m] at moderate Mach numbers (Mach 1.65) (Middlebrooks
et al., 2019). A review of previous breakup models applied to similar
experiments as those presented here can be found in Duke-Walker et al.
(2021).
Theoretical breakup models (e.g. TAB and KHRT) have provided a
deeper understanding of the deformation process and hydrodynamic
instabilities occurring on the droplet surface. The TAB model has been
shown to greatly underpredict the mean drop size after breakup for
a jet (Tanner, 1997) and shock-driven droplets (Duke-Walker et al.,
2021), while the ETAB model (Tanner, 1997) produces droplet sizes
much larger than experiments show for low 𝑊 𝑒. Thus, the TAB and
ETAB models were not considered in this work. The KHRT model has
been advanced by various authors (Liu et al., 1993; Beale and Reitz,
1999), describing the breakup process through the Kelvin–Helmholtz
(KH) and Rayleigh–Taylor (RT) instabilities. The model estimates the
most unstable, fastest growing wavelengths, 𝛬, and respective growth
rate, 𝛺, for each mechanism to determine the breakup time and child
droplet sizes.
Both KH and RT instabilities can occur simultaneously with the RT
instability terminating the KH as seen here. In other cases, the KH in-
stability finishes the breakup process before the RT breakup completes
or the KH may be prevented altogether when its wavelength is too large
relative to the parent droplet diameter (at low 𝑊 𝑒). Generally, the RT
mechanism is considered to dominate the breakup process at lower𝑊 𝑒,
while the KH mechanism dominates at higher 𝑊 𝑒 (Theofanous et al.,
2012). The KHRT model has shown satisfactory results in predicting
the child droplet sizes in the primary breakup of a diesel jet (Liu
et al., 1993). Unfortunately, there are still some uncertainties in the
model since it strongly depends on the choice of coefficients and must
be tuned to experimental work, becoming an open challenge (Sharma
et al., 2022).
Empirical and theoretical breakup models have been widely de-
veloped, tested, tuned, and reiterated to make their application more
general for different breakup regimes. Studies such as Stefanitsis et al.
(2019) show how different experimental conditions may require a dif-
ferent application of zero-dimensional models or coefficients for good
numerical replication of the deformation process. Full 3D simulations
of droplet breakup are non-trivial tasks requiring modeling aspects that
make their validity difficult to determine. However, studies attempting
to match experimental conditions using Euler (Meng and Colonius,
2018) or coupled Euler–Lagrange methods (Stefanitsis et al., 2021)
have shown relatively good agreement with their respective study.
Notably, many previous experiments have been for relatively larger
droplets (order of millimeters). Widdecke et al. (1995) conducted a
study with isopropanol droplets with 50–200 [μm] diameters at shock
Mach numbers of 2–6, with 𝑊 𝑒 ∼ 10 4 and 𝑅𝑒 ∼ 10 4, observing breakup
and cloud formation, however, no efforts were made towards modeling
the phenomena. Kobiera et al. (2009) performed similar studies with
hexane droplets of 0.6–2.0 [mm] in diameter at 𝑊 𝑒 ∼ 10 3–105 and
𝑅𝑒 ∼ 10 4–105, subjected to shocks strength 𝑀 = 2, 2.9. It was observed
that the time for acceleration and dispersion of a droplet into a cloud
was dependent on the diameter and incident shock strength, with the
dispersed cloud diameter being 𝑊 𝑒 dependent and dispersion time
a function of droplet size. Park et al. (2017) studied water droplets
with diameters of 2.0–3.6 [mm] at shock wave Mach numbers of 1.4–
2.2, producing 𝑊 𝑒 ∼ 10 3–104, and 𝑅𝑒 ∼ 10 4. This work observed a
deficiency in predicted droplet acceleration by the available models. It
is worthwhile to note that, in the studies surveyed, little attention was
given to small droplets 𝑑 < 50 [μm] under similar 𝑊 𝑒 regimes.
In this study, a series of shock-droplet experiments were undertaken
with relatively small droplet sizes ( 10–40 [μm]) to provide insight into
the coupled behavior of the shock-droplet breakup and evaporation.
As stated previously, droplet breakup for large droplets has been con-
sidered mostly without evaporation. However, evaporation becomes
significant as the droplet size is made smaller. The experiments con-
ducted here provide metrics of droplet cloud development at various
post-shock times, from shock interaction to droplet extinction. Laser
Mie scattering and Planar Laser Induced Fluorescence (PLIF) imagery
were utilized to track the development of the liquid and vapor species
of acetone, respectively. Special attention was placed on creating an
interface that would be insensitive to mixing and a thorough char-
acterization of the initial conditions was conducted, specifically the
distribution of droplet sizes in the interface. Several existing models
are considered, and their predictions are compared to experimental
data. Additional data points were drawn from published data (Kobiera
et al., 2009) for comparison to model predictions. A simple model for
concurrent breakup and evaporation that most accurately predicts the
experimental results is thus proposed.
2. Experimental facility
The following section will familiarize the reader with the equip-
ment used to conduct the experiments reported in this article, namely
the shock tube facility, diagnostics, data acquisition system, and the
particle–gas curtain shaping device.

<!-- PDF_PAGE: 3 -->

International Journal of Multiphase Flow 161 (2023) 104389
3
V. Duke-Walker et al.
Fig. 1. Experimental facility. (A) Hydraulic diaphragm loading mechanism. (B) Ultrasonic atomizing nozzle. (C) Test sections with laser table and aerosol containment vessel, (D)
Nd: Yag Laser 532 [nm] and 266 [nm].
2.1. Shock tube facility
Experiments were conducted in the fluids mixing shock tube facility
shown in Fig. 1. The shock tube is divided into three main sections: a
driver (high-pressure), driven (low-pressure), and test section housing
the interface and diagnostics. A 24 gauge (0.51 [mm]) galvanized
steel sheet-metal diaphragm is placed between the driver and driven
sections and the two sections are clamped together with two 50 kip dual
actuating hydraulic rams, sealing the system. The hydraulic clamping
mechanism allows for quick turnaround time (under 60 [s] to replace
diaphragms) as well as the ability to use diaphragms sufficiently strong
enough to obtain shock strengths up to Mach 2.75. The driver section
is pressurized to just below the diaphragm breaking pressure, and the
experiment is initiated by a pulse of high-pressure gas, at which point
the diaphragm is instantaneously ruptured by an x-shaped knife. This
method has proved to provide repeatable and reliable experiments. The
driven section is long enough to allow for a stable planar shock to
fully develop before reaching the test section at atmospheric conditions.
The test section is equipped with multiple acrylic windows that were
positioned to visualize the droplet field from the sides and above. The
laser beam enters through a Sapphire window positioned in the end
wall of the test section.
2.2. Diagnostics and data acquisition
The firing sequence and signals are automated through a LabVIEW
code and NI data acquisition hardware acquiring dynamic data at 1
[MHz]. Two dynamic pressure transducers are utilized to measure the
shock velocity from the recorded pressure jump times, and used for
timing of the trigger signals to the diagnostics in the test section. The
laser pulses and synchronized camera imaging are initiated by the
Insight 4G program at a precise time after the shock passes, as measured
by the pressure transducer trigger signal. A Litron NanoPIV 200 laser is
utilized, providing 200 [mJ] and 40 [mJ] of laser energy at 532 [nm]
and 266 [nm] wavelengths, respectively. The laser output is focused
with a plano-convex, concave lens and transformed into a sheet with a
cylindrical lens. The cylindrical lens is rotated 90 degrees to allow for
planar-imaging from any of the window ports in the test sections, as
seen in Figs. 1, and 6.
Two 29 [MP] cameras were utilized to capture the morphological
behavior of the gas and droplets. One camera was filtered to see only
the fluorescence emission from acetone vapor excited by the 266 [nm]
laser emissions, while the other was filtered to see only the 532 [nm]
Mie-scattered light. Neutral density filters were applied to the camera
receiving Mie-scattered light as needed to reduce overexposure. A
Phase Doppler Particle Analyzer (PDPA) system from TSI inc. was used
to measure droplet sizes in-situ, before shock initiation. This system
used a continuous wave laser at 561 [nm] to measure droplet sizes
via FlowSizer64 software. A high-speed shadowgraphy system was also
implemented, consisting of an 880 [mW] LED white light source with
collimating optics, a high-speed camera (Phantom T3610, resolution
1280 × 800, 8-bit pixel size 18 [ μm]), and a long-distance microscope
(K2 Distamax) lens with a 44 [mm] extension tube. Further details
about the shock tube facility are provided in Duke-Walker et al. (2020).
2.3. Multiphase interface shaping apparatus
In this work, the acetone droplets were generated using a focused
ultrasonic (oscillating at 120 [kHz]) spray nozzle designed by Mi-
crospray ( Leiby, 2021 ). This device has the advantage of being able
to produce consistent droplet size with a low relative Span Factor
(uniformity of the drop size distribution) and a low spray dispersion
angle. This device generates droplets via periodic capillary waves in-
duced in a liquid film on the flat nozzle tip. The waves are induced
by a piezo-electric actuator at the base of the nozzle. The frequency
at which the nozzle vibrates dictates the droplet diameter produced.
The ultrasonic nozzle is driven by a broadband ultrasonic generator of
a 20-W tracking driver power and a 25–120 [kHz] output frequency
range. The droplet median diameter of the nozzle can be estimated from
ultrasonic atomizing theory (Lang, 1962), as 𝐷0.5 = 0.34 8𝜋𝜎
𝜌𝑙 𝑓 2 , in which,
𝜎 is the surface tension [N/m], 𝜌𝑙 is the density of the liquid [kg/m 3]
and 𝑓 the operating frequency [Hz].
The acetone droplets were mixed into pre-saturated carrier gas
(nitrogen gas saturated with acetone vapor) in a containment vessel
shown in Fig. 1 before flowing into the test section. A stable rectangular
interface was achieved between the droplet-laden carrier gas and the
surrounding test section gas via an interface shaping device (ISD).
This device directs the droplet-laden gas into the test section in a
controlled manner creating a stable rectangular interface at various
flow concentrations. Compared to our previous work ( Duke-Walker
et al., 2020; Middlebrooks et al., 2019), this device increases the cross-
sectional interface area and delays any hydrodynamic mixing during

<!-- PDF_PAGE: 4 -->

International Journal of Multiphase Flow 161 (2023) 104389
4
V. Duke-Walker et al.
Fig. 2. (A) Multiphase droplet-gas curtain system, Phase Doppler Particle Analyzer
(PDPA): (B) Inside the shock tube test section and (C) Outside free-handle sample.
the droplets’ deformation, break up, and evaporation process. The ISD
is composed of hollow rectangular aluminum housing 127 [ mm] ×
50.8 [mm] with inserts made of solid 3D-printed nylon. As shown in Bal-
akumar et al. (2008) and Orlicz (2007), a dramatic improvement in the
interface stability can be achieved by tuning the 3D flow-straightening
geometry.
Two main flow stabilization sections were constructed to control
the multiphase interface’s shape and stabilization, one at the entrance
(upstream flow stabilization P.1) and one at the exit (downstream flow
stabilization P.2) of the test section ( Figs. 1 –2). The main goal of
the upstream flow stabilization device is to shape and straighten the
multiphase droplet–vapor–gas flow before entering the test section. It
is composed of three subsections; a circular section to allow the flow
to develop and smoothly transition, a honeycomb to straighten the
incoming flow and reduce possible vortex growth, and a contraction to
smoothly shape the interface. Similarly, the downstream flow stabiliza-
tion device P.2 is composed of a secondary honeycomb and contraction,
allowing for a smooth transition as the interface exits the tube. The
downstream device also shields the curtain from any flow disturbances
from the outside air. Design parameters for the honeycomb dimensions
and contraction limitations designs were obtained from Mauro et al.
(2017).
3. Experimental methodology
This section expands on the methodologies and techniques uti-
lized to characterize the multiphase droplet field, initial experimental
conditions, and experimental variation.
3.1. Droplet characterization
Acetone is an ideal fluid for studying droplet breakup and vaporiza-
tion due to its thermophysical properties, which results in high𝑊 𝑒 (low
surface tension) with rapid evaporation (high vapor pressure). Acetone
is also similar to fuels such as ethanol and methanol, having similar
surface tension, density, and low viscosity ( 𝑂ℎ < 0.1). Additionally, at
the droplet sizes and shock conditions in this work, the thermophysical
properties of acetone allow for similar evaporation and breakup mech-
anisms to those of fluids with lower vapor pressures and higher surface
tensions at stronger shock conditions, such as (𝐶10 − 𝐶12) hydrocarbons
in a detonation environment. Furthermore, acetone vapor pressure is
high enough at standard pressure and temperature to produce concen-
trations sufficient to allow fluorescence imagery in atmospheric air.
More detail on the behavior of acetone droplet–vapor–gas systems can
be found in Duke-Walker et al. (2020).
The size distribution of acetone droplets produced was extensively
characterized via two different measurement techniques, Phase Doppler
Particle Analyzer (PDPA) and high-speed microscopy shadowgraph.
The concurrent methodologies aided in reducing uncertainty in the size
distribution, both from the nozzle and inside the multiphase interface.
The optical method compensated for the PDPA’s limitations (volume
and spatial resolution), while the PDPA compensated for diffraction-
limits on measurable droplet sizes in the optical method, comple-
menting each other well. The PDPA method, while having a limited
measurement volume, is superior at resolving small droplet sizes when
compared to current direct imaging methods such as shadowgraphy and
digital in-line holography (Guildenbecher et al., 2017).
3.1.1. Phase doppler particle analyzer measurements
The PDPA system provides an accurate and reliable droplet size
distribution and droplet velocity ( TSI, 2022) via the use of measured
diffraction patterns from droplets illuminated by intersecting lasers.
The PDPA system requires frequent and careful calibration since a
slight misalignment of the laser beams could alter the phase measure-
ments and size results. Because of this, an initial parametric study
was conducted to determine the most accurate and efficient operating
conditions for the device and measured conditions. The optimum beam
intersection position was determined by obtaining a high data rate [Hz]
and burst efficiency ( 𝐵𝑟 > 70 [%] ). Then a study of the photomul-
tiplier tube (PMTs) voltage setting was performed to determine the
best settings, based on the PDPA manual from TSI ( 2022). The PMT
transforms the scattered light and converts it to an electrical signal,
where the PMT voltage increases its sensitivity. PMT voltage is one of
the most critical parameters that effects the measurable particle sizes.
As the PDPA system acquires data, the sizes measured will fluctuate
over time (number of measurements) and the best settings are indicated
when the variation in 𝑑10 is minimized. The study found that the
optimum laser power was 10–30 [%] , PMT voltage 425 [V], and Burst
threshold 30 [%] . Furthermore, the PDPA system was calibrated at the
beginning of every experimental session and collected data analyzed
against system intensity validation metrics (max diameter difference
10 [%], the slope of upper intensity curve 0.6 [mV∕μm2]), ensuring the
validity of the measurements. A total of thirty measurements of the
spray characterization were conducted outside and inside the shock
tube test section to ensure that the droplet size distribution was well
characterized and had no considerable variation. The total number
of valid droplet size measurements collected ex-situ and in-situ were
828,475 and 32,307.
A representation of the setup utilized for collecting the statistical
data can be seen in Figs. 2 - 4 . The system was used ex-situ and in-
situ with a refraction scatter angle of 32.5 degrees between the laser
beam (PowerSight Module PS-TM-2D-R) and the Fiber Optic Transmit-
ting Probes with a lens focal length lens of 70 [mm]. The laser was
integrated with a lens of 300 [mm] focal length, allowing us to measure
droplet diameters between 0.5–125 [ μm].
3.1.2. High speed microscope shadowgraphy
The high-speed microscope shadowgraphy setup was utilized to
verify the measurements of the PDPA system. The shadowgraphy lens
was set to produce a 7.25X magnification, with a pixel size of∼2.5 [μm]
and the high-speed camera system was set to a 1 [μs] exposure time.
Calibration images at this magnification were captured with a target
(R1L3S2P) with a 1 [mm] long scale with 10 [μm] divisions with low
reflectivity. A 532 [nm] (10 [nm] FWHM) filter was placed in front
of the LED source to provide monochromatic illumination resulting in
higher sensitivity and contrast as droplets passed through the illumi-
nated region (see Fig. 3). A MATLAB routine was developed to identify
individual droplets to create a statistical representation of the droplet
size distribution.

<!-- PDF_PAGE: 5 -->

International Journal of Multiphase Flow 161 (2023) 104389
5
V. Duke-Walker et al.
Fig. 3. Microscopy shadowgraph: (A) Calibration target, (B) Example of the droplet
field, (C) Sample droplets diameter, (D) System configuration.
Table 1
Breakup initial conditions.
𝑑𝑝 [μm] 𝑂ℎ 𝑊 𝑒 𝑅𝑒
14.16 0.02 662 ± 19 1647 ± 21
37.3 0.01 1743 ± 49 4338 ± 56
3.2. Initial conditions
A thorough understanding of the initial conditions is necessary
to validate and compare the performance of existing breakup and
evaporation models. For this work, the focus was placed on control-
ling the multiphase interface, and characterizing the droplet and gas
mixture (see Table 1). The shock tube was initially filled with dry (no
acetone vapor) atmospheric air at standard temperature and pressure
(approximately 1 [atm] and 293 [K]). The multiphase interface fluid
is composed of liquid acetone droplets and nitrogen gas saturated with
acetone vapor (40.69 [%] by mass) at 1 [atm] and 293 [K]. The stability
of the multiphase interface, droplet-gas curtain created by the ISD, was
analyzed utilizing a time sequence Mie-scattering and PLIF images of
the X-Y plane. Various gas flow rates were tested to find the most stable
regime, and atomized liquid droplet flow rates adjusted accordingly.
A combination of images of the curtain on the X-Z and X-Y planes
were captured and post-processed to quantify the interface shape. These
measurements showed that the rectangular shape measured to be a
width of 𝑋 ∼ 12 .19 [mm], length of 𝑍 ∼ 48 .26 [mm], and height of
𝑌 ∼ 139.7 [mm], as can be seen in Fig. 2 .
Concentration and statistical droplet size distribution measurements
were collected and analyzed to validate the multiphase curtain char-
acteristics. For this work, the droplet concentration was controlled
via liquid mass flow rate, set by a syringe pump at ∼1.5 [ ml
min ] and
gas mass flow rate, set via mass controller to ∼10[𝑆𝐿𝑀 ]. The droplet
concentration was measured via a filtration retention device ( Duke-
Walker et al. , 2020 ) and the mixture was found to be >99.99[%] by
volume gas, leaving <0.01[%] for the droplet field, indicating negligible
droplet-to-droplet interactions in the initial conditions.
The statistical size distribution of droplets ex-situ and in-situ was
measured with PDPA and shadowgraphy (as detailed in Sections 3.1.1
and 3.1.2 ) to be compared with theoretical droplet size predictions
based on acoustic theory as shown in Section 2.3 . Taking the droplet
median diameter from theory as 𝑑0.5 = 13.02 [μm], PDPA measurements
ex-situ showed 𝑑0.5 = 12 .05 [μ m] and in-situ 𝑑0.5 = 13 .93 [μ m], while
shadowgraphy ex-situ found 𝑑0.5 = 17.92 [μm]. PDPA results and theory
Fig. 4. Phase Doppler Particle Analyzer (PDPA) outside and inside the shock tube test
section.
Fig. 5. Shadowgraph outside, PDPA outside and inside the shock tube test section.
showed excellent agreement. The shadowgraph numerically disagreed;
however, it is understandable since it is limited to measuring droplets
larger than 12.5 [μm] for the current setup, which is the bulk of
droplets within the distribution. When the shadowgraphy droplet size
probability distribution was scaled to show similar probability above
the detectable diameter, it showed excellent agreement with the PDPA
data sample, as seen in Fig. 5 .
While PDPA accuracy and sample rate are high, it is limited by the
maximum droplet size detected with the lens and sampling volume of
our current configuration. The sample volume of the shadowgraphy
system is higher than the PDPA system and allowed for measurement
of larger droplets, though the sample rate was lower and limited at
small droplet sizes by diffraction. Finally, the shadowgraph showed that
droplet diameters beyond 𝑑 > 125 [μ m] do not play a significant role,
which is the maximum droplet diameter that the PDPA can detect with
the currently equipped lens.
The size statistics of the droplets, which are considered the initial
conditions in our modeling section, are taken to be those of the ex-situ
PDPA data, 𝑑10 = 14 .16 [μ m] and 𝑑32 = 37 .3 [μ m], as these have the
highest statistical confidence. The statistical droplet distribution from
the PDPA can be seen in Fig. 4 .

<!-- PDF_PAGE: 6 -->

International Journal of Multiphase Flow 161 (2023) 104389
6
V. Duke-Walker et al.
Table 2
Experimental camera setting.
t [ μs] 0–25 0–125 125–300
Aperture 22 16 5.6–2.8
Filter [nm] 532 – –
Neutral density 4 – –
Fig. 6. Angular distortion: (A) location 1 at two angles ( 𝛽 = 0 and 𝛽 = 45) (B) location
2 at the top of the window 𝛽 = 0 , (C) original distorted image, and (D) corrected
distorted image.
3.3. Experimental diagnostics
Before every experiment, the laser alignment and its optics in
conjunction with the camera lens must be checked and secured, and all-
optical equipment and windows must be cleaned to guarantee optimal
performance. A calibration target is positioned at the center of the test
section window to indicate the center of the interface with respect to
the cameras. An example is shown in Fig. 6 . Once the optical system
is ready, calibration and background images are acquired to account
for the changes in the experimental setup as cameras get re-positioned.
The camera focus is set at the mid-range of the hyper-focal distance
and further adjusted to the droplet (Mie-scattering signal) or gas (flu-
orescence signal) field. The cameras, depending on the experimental
times, as shown in Table 2 , were adjusted not to overexpose or over-
saturate the CCD sensor. Three primary camera settings were utilized to
account for the variation in scattered light intensity from the resulting
breakup process, child droplet cloud growth, and evaporation, as shown
in Table 2.
For the first 0–25 [ μs], the camera is set on window 1 (W1 in
Figs. 1 and 6 ), perpendicular to the shock tube at 𝜃 = 0 with a
0.41X magnification, to capture droplets at their initial conditions and
during early breakup times. Due to the excess scattered light during
breakup, the camera aperture, and neutral density filters were adjusted
accordingly, as presented in Table 2 . The second camera position, set
for window 1 with 𝜃 = 45 and a magnification of ∼0.3X, allowed
an experimental visualization from 0–125 [ μs]; however, the highest
quality images were obtained after 25 [ μs]. This setting captured the
initial conditions and droplet cloud growth. The cameras were inclined
to extend the field of view and bridge the gap between windows. Lastly,
the third camera position, at the top of the test section in window 3
(W3 in Figs. 1 and 6) with a 𝛽 = 0 and a magnification of ∼0.3X, was
selected to capture the late time evolution and evaporation of the child
droplet cloud. Calibration images were captured for each camera setup,
allowing droplet and gas field images to be overlaid, obtaining a ratio
to transform from [pixel] to [mm], and providing an image map for
correcting optical distortion due to camera inclination angle.
Table 3
Experimental post-shock conditions and breakup initial conditions.
Mach V [m/s] P [kPa] T [K]
2.09 ± 0.01 461 .3 ± 4.6 493 .6 ± 6.4 516 .6 ± 3.2
The oblique image projection was adjusted to correct for the camera
inclination angle by following the transformation proposed by Loomis
(2022) This method takes four cardinal points from the original calibra-
tion target to warp, transform, and remap the image plane. Once the
distorted calibration images are corrected, the experimental images are
rectified following the same approach, as seen in Fig. 6 C and D. These
steps ensure that the experimental results will replicate the correct
[pixel] to the [mm] ratio when detecting and calculating the actual
size of the child droplet cloud, as will be demonstrated in Section 4.2 .
Having described all experimental equipment calibration and char-
acterized the multiphase interface, we move now to the experimental
procedures for initiating (firing) a shock wave. The firing procedures
begin by replacing the diaphragm and filling the shock tube with clean
ambient air. This must be performed to remove any residual acetone
vapor from previous runs and eliminate dust or debris in the shock tube.
An automatic shock firing sequence (ASFS) was developed with the
LabVIEW control program, following the procedure described by Duke-
Walker et al. ( 2020) with slight variations, to gain repeatability and
reduce the procedure complexity. In the ASFS, the driver pressure
was set to reach a target static pressure of 460 [psi] by filling slowly
through a small solenoid valve. Once this pressure was reached, a large
solenoid valve was actuated to raise the pressure quickly (within∼1 [s])
to the diaphragm breaking pressure, approximately ∼500 [psig]. The
supply gas pressure was maintained within a gas tank at a pressure of
1000 [psig]. During the ASFS, the interface was introduced whenever
the pressure in the driver reached 375 [psig], followed immediately
by the carrier gas at 385 [psig]. This increase in the boost valve
pressure allowed a reliable and instantaneous break of the diaphragm.
The voltage threshold was set to 0.4 [V] inside LabVIEW ensuring
that the dynamic pressure transducers (DPT) captured the shock and
the timing was repeatable. Once the first DPT detects the shock, two
laser pulses are triggered, capturing two frames (i.e., A & B) on each
camera. Frame A contains the initial droplet location just before shock
interaction, and frame B shows the child droplet cloud development.
These procedures were repeated for each experimental trial until the
complete morphological interface development was obtained.
Another important factor to be considered in modeling the experi-
mental results is the run-to-tun variation of the shock strength. One of
the primary causes of this variation was found to be variations in the
diaphragm; the deviation in thickness was up to ±0.00075 [in.] from the
nominal value of 0.025 [ in.], enough to cause a variation in bursting
pressure and shock strength between experiments. Other factors that
could have contributed to the variations between experiments were
dulling of the knife edge, and variation in metallurgical properties of
the diaphragm. In practice, the shocks were still within a close range
of Mach numbers, between 2.09 ± 0.01. At these Mach strengths, it can
be estimated that the jump from atmospheric to post-shock conditions
will vary in pressure, temperature, and velocity as shown in Table 3 .
4. Experimental results
This section will discuss the experimental results from a qualitative
and quantitative point of view, giving a more detailed insight into the
temporal and morphological evolution of the multiphase interface.
4.1. Qualitative description of droplet cloud evolution and evaporation
All experimental images have been corrected and converted from
[px] to [mm] with their respective size calibration image. The droplet
and gas contributions are overlaid to describe the droplet development

<!-- PDF_PAGE: 7 -->

International Journal of Multiphase Flow 161 (2023) 104389
7
V. Duke-Walker et al.
Fig. 7. Time series ensemble images of experimental results: (A) initial conditions prior shock arrival, (B) droplet break up, (C) onset of cloud growth, (D) PLIF signal at a later
time, (E) cloud growth stagnation and evaporation Images captured from 0–125 [μs] were taken in plane X-Y and 125–300 [μs] in plane X-Z. (For interpretation of the references
to color in this figure legend, the reader is referred to the web version of this article.)
qualitatively. The overlay was performed by taking four coordinate
points from the corrected calibration image from both 29 [MP] cameras
and applying them to the experimental images. For further details, the
reader is encouraged to see Duke-Walker et al. ( 2020). Specifically, a
MATLAB algorithm was implemented to provide a quantitative mea-
surement of cloud growth, relative position, velocity, and trajectory
and is detailed in Section 4.2 . Subsequently, once all experimental
images were processed, a time series evolution of the particle cloud
was assembled as shown in Figs. 7 and 9 . Fig. 7 shows the droplet
field (Mie-scattered 532 [nm] light) in yellow, while the vapor field
(laser-induced fluorescence) is shown in blue at 𝑡 = 0 [μ s]. At all other
times, 𝑡 = 0 .4 [μ s] through 𝑡 = 253 [μ s], the X locations, upstream and
downstream edges, of the vapor field are indicated by dashed white
lines for clarity. The dotted lines represent the predicted location of the
acetone vapor interface, based on 1D gas dynamics calculations. Images
of acetone fluorescence are shown at two times to verify the position
predicted by 1D gas dynamics, though the images were not calibrated
for quantitative purposes.
Generally, the development can be outlined as an initial compres-
sion of the gas/vapor within the multiphase interface ( 𝑡 = 0 .4 [μ s])
followed by breakup of the parent droplets forming child droplets ( 𝑡 =
0.4–8.4 [μ s]), then growth of the child droplet cloud ( 𝑡 = 8 .4–98 [μ s]),
and lastly evaporation of the child droplets (𝑡 = 98–253 [μs]). The image
at 𝑡 = 0.4 [μs] shows the breakup process and early cloud development
as particles on the downstream side of the interface remain intact while
those on the upstream side are already showing child droplet cloud
growth. Droplet breakup initiates at different times depending on when
the shock wave intersects it, and occurs at different rates, dependent
upon the parent droplet’s size. As the shock traverses the droplet-gas
curtain, the gas responds instantaneously, jumping to the post-shock
conditions. At the same time, the droplets begin equilibrating with the
gas through mass, energy, and momentum transfer. The momentum
equilibration time is responsible for the droplets falling behind the
gas interface, even before breakup occurs. Parent droplet deformation
occurs before breakup, over a relatively short time, but could not be
visualized as the droplet sizes under consideration were close to or
under the diffraction limit of our optics.
Within the child droplet cloud, the smallest droplets equilibrate in
speed with the post-shock gas near instantaneously. In contrast, the
larger droplets lag behind and stretch the cloud (in the X direction),
dropping further behind the gas/vapor interface. The cloud growth in
the X direction can be attributed to the different equilibration times
from the child droplet size distribution. The droplet cloud growth in
the X-Y and X-Z directions can be attributed to the deformation rate
of parent droplets, creating a radial velocity that transitions the child
droplets outward. The growth in the X-Y and Y-Z planes is assumed to
be symmetric for analysis purposes. Once growth ceases, it can be taken
that the system has equilibrated in velocity.
Additionally, the intensity of scattered light from the droplets de-
creases significantly from the initial droplet clouds, near the initial
breakup event, to the evolved and evaporating clouds at later times, as
seen in Fig. 8. In this figure the sum of the image intensity is divided by
the total area of droplet clouds, as identified by the algorithm discussed
in Section 4.2. Then, after finding the average intensity corresponding
to a group of clouds at a specific time, all average cloud intensity
values were normalized against the maximum average intensity of the
complete data set. The initial increase in average intensity is due to
the increased area for light scattering as single large parent droplets
are converted into many small child droplets, as explained from Mie-
theory ( Crowe et al. , 1998). The initial sudden decrease in intensity
can be explained by the stretching of the droplet clouds, as the cloud
area increases greatly from the region before ∼10 [μ s] to that after. A
slow decrease in average intensity occurs then as clouds are stretched,
and the smaller child droplets begin to completely evaporate, marking
a second decrease in intensity at about 150 [μs].
Lastly, the particle survival time can be measured as the time when
the intensity of scattered light for a droplet cloud drops to zero. The
size of the parent droplet largely influences the evaporation time and
the cloud conditions. The bigger the parent droplet, the larger the child
droplets produced, leading to a longer survival time. From the exper-
imental results, no droplet clouds were observed past 300 [μ s], while
clouds were observed only intermittently from 250–300 [μs], indicating
that the evaporation time of the larger parent droplets (resulting child
droplet clouds) should be in this range.

<!-- PDF_PAGE: 8 -->

International Journal of Multiphase Flow 161 (2023) 104389
8
V. Duke-Walker et al.
Fig. 8. Average child droplet cloud intensity versus time, mean intensity is average
maximum cloud intensity.
Fig. 9. MATLAB algorithm for detecting cloud metrics.
4.2. Particle cloud detection
The algorithm for child droplet cloud size detection consists of
three main routines: image pre-processing and background correction,
cloud boundary detection, and detected cloud acceptance/rejection.
Once images are loaded, background subtraction is performed from
the mean value of the background image before the shock. Image
noise reduction is performed to improve the image restoration process,
followed by an image median filter square of 5 [px] by 5 [px] to smooth
droplet intensity within the cloud, and finally a 2-D Gaussian smoothing
kernel filter to slightly blur the droplet cloud. A 2D gradient filter
was then applied to the image to identify the cloud boundary quickly
and reliably. The algorithm extracts from the detected droplet cloud
boundary the length 𝛥𝑋, width 𝛥𝑌 , mean intensity, and X distance
traveled post-shock, and plots the results.
After the droplet clouds were detected, a mean of the cloud length
and width were obtained for each image. Cloud length and widths
beyond ±1 standard deviation were rejected. These rejected cloud
Fig. 10. Cloud downstream and upstream positions versus time.
lengths were most often due to overlap with neighboring clouds. An
example of the detected droplet cloud found with the algorithm can
be seen in Fig. 9. A subsequent routine in the algorithm calculates the
upstream and downstream locations matching droplet cloud locations
in frame B, with the initial parent droplet location from frame A.
From the center of the detected cloud in frame B, we traced the pixel
location of the most likely parent droplet in frame A by matching the Y
position. Lastly, the algorithm’s detection is limited by the proximity of
child droplets to one another in that droplets with spacing larger than
the filter size will result in a discontinuous intensity contour. Thus,
large trailing droplets may not be included in the cloud dimensions,
producing a possible error on the order of 5 [%] for some clouds. On
average, 15 ± 5 clouds are detected per experimental run, providing
some statistical certainty and minimizing the effect of small random
errors in our could dimensions.
4.3. Quantitative description of droplet cloud dynamics
Once the cloud boundary is detected in frame B, the droplet position
is measured from the center of the interface in frame A to estimate the
relative position (distance traveled) of the cloud head (downstream)
and tail (upstream) over time, shown in Fig. 9. Generally, more parent
droplets were detected in frame A than child droplet clouds in frame
B as time progressed. This is because the smallest parent droplets will
change phase relatively quickly and are no longer detected in frame B,
while the largest will persist much longer.
As seen in Fig. 10 at time 0 [μs], the parent droplets are immediately
accelerated by the shock wave passage, breaking up and quickly equi-
librating with the gas velocity ( ∼461.3 [m/s]). It could be inferred that
the smallest child droplets tend to accelerate faster and quickly reach
equilibrium with the flow at the head (downstream edge) of the droplet
cloud. Inversely, the largest child droplets within the distribution tend
to fall behind, stretching out the droplet cloud and showing more
significant cloud growth. Figs. 11 and 12 display the average cloud
length and width, shown as orange points, with error bars giving the
bounds of lengths or widths of droplet clouds observed at that time. The
cloud length and width increase in the first 70 [μs] and starts to plateau
at late times as all child droplet sizes come to velocity equilibrium with
the gas.
It must be emphasized that child droplet cloud growth is correlated
with the parent droplet size distribution shown in Section 3.2 . The
smallest parent droplets (below 6 [ μm]) will have deformation, break

<!-- PDF_PAGE: 9 -->

International Journal of Multiphase Flow 161 (2023) 104389
9
V. Duke-Walker et al.
Fig. 11. Cloud length 𝐿𝑥 versus time. (For interpretation of the references to color
in this figure legend, the reader is referred to the web version of this article.)
Fig. 12. Cloud width 𝐿𝑦 versus time. (For interpretation of the references to color in
this figure legend, the reader is referred to the web version of this article.)
up and phase change on similar time scales. However, as the parent
droplet diameter increases, there is an increase in the breakup time and
more considerably the evaporation time, leaving more time for child
droplet cloud growth before complete evaporation. Observations of the
droplet clouds at 𝑡 > 300 [μ s] do not show discernible droplet clouds
indicating that complete evaporation occurs at 300 > 𝑡 > 250 [μs].
5. Modeling of experimental results
In this section, a simplified model, the Child Droplet Cloud (CDC)
model (see Fig. 13), is developed to explain the observed evaporation
times and cloud growth (see Fig. 14 ). It was hypothesized in the
previous sections that the child droplet cloud length resulted from
a difference in equilibration times resulting from the child droplet
size distribution. As such, this model predicts the trajectory of the
parent droplet, and representative small and large child droplets to
Fig. 13. Modeling algorithm.
predict the cloud development in X and Y. Various breakup models,
providing predicted breakup times and child droplet sizes, are tested
to determine their fit to the experimental measurements. Further, the
evaporation time is estimated based on the 𝐷2 law modified to account
for significant local vapor fractions when necessary. The use of these
simplified models accounts for shock conditions, droplet breakup, and
psychrometrics and allows the direct calculation of final child droplet
cloud size and evaporation time without the need for numerical in-
tegration. The detailed equations of this model may be found in the
Appendix while the following sections provide a mostly qualitative
description of its functioning and its results.
5.1. Predicted gas properties
First, the gas conditions must be predicted based on the initial gas
properties and shock strength. Two initial conditions were considered;
one for the surrounding dry air and one for the acetone-vapor-saturated
nitrogen within the multiphase interface. The post-shock conditions
were solved using 1D gas dynamics. The surrounding air was calculated
to have a post-shock pressure of 493.6 [kPa] , temperature of 516.6 [ K],
and velocity of 461.3 [ m/s], at the mean shock Mach number of 2.09.
For simplicity, the shock refraction problem is not solved at the gas
interface (air and acetone–nitrogen mixture) since the interface is lim-
ited in size in the shock (Y-Z) plane (∼50 [mm] interface width vs. 140
[mm] tube width). Instead, the interface gas is assumed to achieve the
same velocity as the post-shock air, and the transmitted shock strength
predicted. Note this assumption will result in a mismatch in predicted
pressure between the interface and surrounding gas, but eliminates
the need for 2D gas dynamics simulations. With this assumption, the
interface carrier gas is estimated to have a post-shock temperature of
461.1 [K]. The droplets are assumed to fall behind the interface carrier
gas and into the surrounding dry air after initiation of the breakup
process. It is then assumed that the child droplets and surrounding
air reached the wet bulb temperature rapidly (see Duke-Walker et al. ,
2020; Paudel et al. , 2018). The wet bulb temperature was calculated
based on psychrometric equilibrium conditions to be 𝑇𝑤𝑏 = 328.3 [K].
5.2. Droplet trajectories
The simple scenario of rigid spherical, non-deforming/breaking ace-
tone droplet will be considered first to explain the effect of drag on
droplet trajectories in the CDC model. The CDC model assumes that
droplet-to-droplet interactions are negligible (interface droplet volume
fractions were <1 [%] ) even within the child droplet cloud (droplet
volume fractions quickly drop below 1 [%] during cloud evolution).
Additionally, the droplet was assumed to begin accelerating when the
incident shock has completely transited the droplet, and unsteady drag
effects were not considered. A simple drag model was used (Eq. (A.1)),

<!-- PDF_PAGE: 10 -->

International Journal of Multiphase Flow 161 (2023) 104389
10
V. Duke-Walker et al.
Fig. 14. Schematic of the deformation and breakup process: (A) Initial parent droplet
of diameter 𝑑𝑝, (B) Maximum deformation 𝑑𝑎, (C) Representative Sauter mean child
droplet diameter 𝑑𝑐, (D) cloud development trajectory, and (E) Nearly evaporated
particle.
where the coefficient of drag was taken to follow the ( Klyachko,
1934) drag model, shown in Eq. ( A.2). Cloutman (1988) provided an
analytical solution for the droplet velocity ( Eqs. (A.4) and (A.8)) and
position (Eqs. (A.5) and (A.9)) over time (see Dahal and McFarland ,
2017 for more) for both 𝑅𝑒 > 1000 and 𝑅𝑒 ≤ 1000 regimes. For our
conditions, the acetone droplet will start on the high 𝑅𝑒 solution if it
is larger than ∼8 [μ m] in diameter and then transition to the low 𝑅𝑒
solution as its velocity increases, 𝑅𝑒 decreases. Its final lag distance
can then be estimated as the distance traveled relative to the gas once
the droplet reaches 99 [%] of the gas velocity.
5.3. Deformation model
Deformation effects are now added to the simple rigid droplet accel-
eration scenario as a necessary precondition for breakup. The effect of
deformation is to increase both the drag coefficient and cross-sectional
area of the droplet as it takes on an oblate form. Deformation was taken
to occur as described by the TAB model (O’Rourke and Amsden, 1987)
where the droplet’s dynamics are considered as a forced mass–spring–
damper system. The deformation process is taken to begin immediately
when the shock wave completely transits the droplet and will end at the
onset of breakup, if the breakup criteria are met.
The parent droplet will begin to oscillate from a sphere to a oblate-
disk of equal volume, altering the drag forces experienced by the
droplet. If the windward and leeward points are taken as the poles,
then the diameter at the equator, 𝑑𝑎, will increase initially. The non-
dimensional displacement of the equator is taken as 𝑦∗ = 2(𝑑𝑎 − 𝑑𝑝)∕𝑑𝑝,
where 𝑑𝑝 is the initial diameter of the parent droplet. The equatorial
diameter 𝑑𝑎 will continue oscillating as 𝑦∗ follows a decaying sine wave.
If 𝑦∗ exceeds a critical value of 1, meaning that the droplet has reached
150 [%] of its original equatorial diameter, then breakup will occur,
ending the oscillation of the parent droplet.
Rather than track the parent droplet diameter as a function of time,
its drag properties were derived from a weighting of the initial spherical
and its fully deformed oblate spheroid shapes. Since it is known that
the parent droplet will experience more time acting as a sphere than
a disk ( Chou and Faeth , 1998 ), when breakup is eminent, the drag
properties are weighted to be 1∕3 of a sphere, and 2∕3 the final oblate
spheroid. The drag acceleration term is weighted by the deformed
area ratio (Eq. ( A.3)) and modifies the drag coefficient (Eq. ( A.11)),
providing a closer representation of the drag forces experienced by the
parent droplet before breakup. A representation of this process can be
seen in Fig. 14B. At the onset of the breakup process, the child droplet
outward radial velocity, 𝑣𝑐,𝑦, is set based on the deformation rate from
the TAB model (Tanner, 1997) as seen in Eq. ( A.16).
Fig. 15. Breakup initiation versus parent diameter at Mach ∼2.1 flow conditions.
Fig. 16. Breakup completion versus parent diameter at Mach ∼2.1 flow conditions.
5.4. Breakup models
Adding to the model for a deforming droplet, breakup is now consid-
ered. Many models exist for breakup, providing breakup times and child
droplet sizes. A combination of theoretical, the KHRT model (Beale and
Reitz, 1999), and empirical models such as those of Wert (1995), Duke-
Walker et al. ( 2021), and Hsiang and Faeth ( 1992) have been imple-
mented to predict the child droplet parameters. Since breakup parame-
ters (e.g. 𝑊 𝑒, 𝑅𝑒, and 𝑂ℎ) for these models are set at the time of shock
interaction, the properties of the post-shock acetone saturated interface
gas are used. The breakup times for each of these models are based on
the characteristic breakup time, 𝑡𝑐 in Eq. (A.17), proposed by Nicholls
and Ranger (1969). Breakup times can be nondimensionalized as 𝜏𝑏 =
𝑡∕𝑡𝑐.
The KHRT model predicts that breakup occurs through two hy-
drodynamic instabilities on the droplet surface, the Kelvin–Helmholtz
(KH) and Rayleigh–Taylor (RT) instabilities. For each instability the
most unstable, fastest growing ( Eqs. (A.19) and (A.21)) wavelength is
calculated (Eqs. (A.20) and (A.22)). The child droplet sizes are taken
to scale with this wavelength for each mechanism (Eq. ( A.24)). The
rate of production is taken as a function of the instability growth
rate with parameters tuned to agree with the characteristic breakup
time, 𝑡𝑐. The KH mechanism is taken to begin immediately after shock
interaction, 𝜏𝑖 = 0 , and to precede deformation. The KH mechanism
then continues at a sufficient rate to consume all droplet mass at the

<!-- PDF_PAGE: 11 -->

International Journal of Multiphase Flow 161 (2023) 104389
11
V. Duke-Walker et al.
Fig. 17. SMD ratio ( 𝑑𝑐 ∕𝑑𝑝) vs. We predicted by different breakup models.
predicted final breakup time, 𝜏𝑏𝑡,𝐾𝐻 . The RT mechanism was taken to
occur instantaneously at 𝜏𝑏𝑡,𝑅𝑇 and may occur before the KH instability
consumes the entirety of the parent droplet mass ( Fig. 16 ). The KH
mechanism may be prevented when the most unstable wavelength
becomes larger than the droplet diameter. Sharma et al. (2022) suggests
that 𝜆𝑘ℎ∕𝑑𝑝 < 0.1, while Theofanous et al. (2012) suggests 𝜆𝑘ℎ∕𝑑𝑝 < 0.2
and that RT instability cannot be dominant if this condition is met.
The empirical models are derived based on experimental observa-
tions of breakup driven by a shock interaction for droplet diameters on
the order of 1 [mm]. For this work, the models of Wert (1995) (referred
to as Wert model), Duke-Walker et al. (2021), a modification of Wert’s
model (referred to as Wert49 model), and Hsiang and Faeth ( 1992)
(referred to as Hsiang model) have been tested against our experimental
observations. These models predict that breakup will initiate at some
time after shock interaction, 𝑡𝑏𝑖, and end at 𝑡𝑏𝑡, where these values are
found as functions 𝑊 𝑒 and 𝑂ℎ (Eqs. (A.18) and (A.23)). The functions
used for each time may change with 𝑊 𝑒, breakup regime. Since all
cases presented are in the high Weber number regime, 𝑊𝑒 > 600, there
is only one applicable time correlation for each model. The breakup
initiation time is constant at 𝜏𝑏𝑖 ∼ 1 .6 for Hsiang model, while it
decreases with increasing 𝑊 𝑒 for both the Wert and Wert49 models
taking on values of 𝜏𝑏𝑖 ∼ 0 .35 and 𝜏𝑏𝑖 ∼ 1 .2, respectively, in the 𝑊 𝑒
range of interest here ( Fig. 15 ). The total breakup time again takes
on a constant value of 𝜏𝑏𝑡 ∼ 5 for the Hsiang model, and a constant
value of 𝜏𝑏𝑡 = 6 for the Wert 49 model, while for the Wert model
the breakup time decreases with 𝑊 𝑒 approaching a value 𝜏𝑏𝑡 ∼ 2 for
the 𝑊 𝑒 numbers considered here. Fig. 16 shows that the KH and RT
mechanisms are much faster than the empirical models for the gas
conditions considered here, though the Wert model approaches the
KHRT times for large droplets 𝑑𝑃 > 70.
The child droplet sizes produced are predicted as a function of the
initial breakup parameters and times. While a range of sizes is produced
during breakup, these models predict a single characteristic size for
the child droplets, the Sauter mean diameter or 𝑑32 (Eq. (A.24)). This
droplet size is predicted as ratio of the parent drop size,𝑑𝑐∕𝑑𝑝. For each
empirical model, the child droplet size ratio, 𝑑𝑐 ∕𝑑𝑝, asymptotes to a
low value as 𝑊 𝑒 increases, 𝑑𝑐 ∕𝑑𝑝 ∼ 0 .1 for the Wert49 and Hsiang
models and 𝑑𝑐 ∕𝑑𝑝 ∼ 0 .05 for the Wert model as seen on Fig. 17 . A
comparison of the child droplet sizes produced at our gas conditions is
shown for each model in Fig. 18. This figure shows that both Wert and
RT models produced a similar particle diameter. Similarly, Wert49 and
Hsiang are relatively close for small droplets, 𝑑𝑝 < 40 [μm]. Conversely,
the KH child droplet sizes were an order of magnitude smaller than
other models.
These small KH droplets will equilibrate with the surrounding gas
nearly instantaneously due to their small size. Similar behavior has
Fig. 18. Parent vs. Child droplet diameters predicted by different breakup models.
been observed in work related to the empirical models, and Chou and
Faeth (1998) found that small droplets were observed at early times
traveling near the gas velocity. The model proposed here, thus assumes
that the smallest child droplet produced occurs at early time and is
sufficiently small to equilibrate with the gas nearly instantaneously. For
the KHRT model this droplet is produced at 𝜏 = 0 and for the empirical
models at 𝜏 = 𝜏𝑏𝑖. Breakup ceases at 𝜏 = 𝜏𝑏𝑡, whether by onset of the RT
mechanism or by completion of the KH or empirical breakup models.
At this time, the child droplets produced are taken to have a diameter
𝑑𝑐 (Eq. (A.24)), given by the empirical models, or RT mechanism (for
our conditions RT breakup precedes KH completion).
With the child droplet production timing and sizes determined, the
droplet trajectory model can be implemented to determine the path
of two exemplar child droplets, the characteristic smallest and largest
sizes (or KH and RT child droplets). The small droplet trajectory will
track the downstream edge of the child droplet cloud, and for both the
KH and empirical models the droplet is assumed to travel at the gas
velocity from the moment of production. For the large droplets, the
parent droplet trajectory must be tracked until 𝜏 = 𝜏𝑏𝑡 as in Section 5.3.
This provides its velocity and lag distance from𝜏𝑏𝑖, when the small child
droplet is produced and begins traveling with the gas, to 𝜏𝑏𝑡, when the
large droplet is produced and takes on its own trajectory. The child
droplet trajectory starts at the parent droplet’s position and velocity,
including the radial velocity predicted by the deformation model. It is
tracked using the equations presented in Section 5.2 for both the 𝑥 and
𝑦 components of velocity. The final cloud dimensions may be estimated
when 𝑣𝑐,𝑥 = 0.99𝑣𝑔,𝑥, which allows an estimate of the maximum volume
of the individual cloud to predict its evaporation time.
5.5. Evaporation models
Up to this point, droplet deformation and breakup have been consid-
ered to be independent of phase change. We now add evaporation to the
deforming and breaking droplet case to determine when the resulting
child droplets should completely evaporate. A simple estimation of
evaporation rates can be provided from the 𝐷2 law ( Crowe et al. ,
1998) and the instantaneous droplet vaporization rate provided by the
Spalding model, ̇ 𝑚𝐵 (Eq. (A.31)), Abramzon and Sirignano (1989). The
evaporation rate of the parent droplet is considered to be negligible
and the 𝐷2 lifetime of the largest child droplet, after formation at 𝜏𝑏𝑡,
is taken to predict when the child droplet cloud should no longer be
visible in experimental Mie-scattering images.
The effect of cloud gas saturation by vapor is considered when sig-
nificant. The cloud total volume 𝑉𝑐𝑙𝑜𝑢𝑑 is calculated as the volume of an
ellipsoid, where the child droplet maximum radial displacement 𝐿𝑐,𝑦 is

<!-- PDF_PAGE: 12 -->

International Journal of Multiphase Flow 161 (2023) 104389
12
V. Duke-Walker et al.
used for the 𝑌 and 𝑍 dimensions and the cloud trajectory parallel to the
shock wave 𝐿𝑐,𝑥 is used for the 𝑋 dimension. The maximum vapor mass
fraction achievable in the child droplet cloud, 𝑌𝑚𝑎𝑥, is predicted using
the cloud volume, parent droplet mass, and thermodynamic functions.
This value was found to be negligible, <1%, for the Wert49 and Hsiang
breakup models, but in excess of the saturation mass fraction for the
Wert and KHRT models at the parent droplet sizes considered. Thus,
complete evaporation of the child droplet cloud would not be predicted
to occur for the KHRT and Wert model, as seen in Fig. 19, though
mixing and diffusion effects not included in the CDC model would result
in complete evaporation at much greater times.
To calculate the droplet vaporization rate of the child droplet ̇ 𝑚𝐵 =
𝑓 (𝑣@𝑇𝑓 , 𝑑𝑐 , 𝜌𝑓 , 𝑆ℎ, 𝐵𝑀 ), child droplets were considered to lag into the
surrounding dry gas at the post-shock conditions (as observed in our
experimental measurements). Since velocity equilibrium is achieved at
early times relative to the complete evaporation time, we take that
evaporation occurs primarily in the free convection regime, setting
the Sherwood number to 2. The Spalding mass transfer number, 𝐵𝑀
(Eq. (A.27)), is calculated assuming that the vapor mass fraction in
the cloud gas is at its maximum value, 𝑌∞ = 𝑌𝑚𝑎𝑥. This assumption
works well as this value is exceeding low ( <1 [%]) for the Wert49 and
Hsiang models, meaning that it has little effect even though its variation
with time is not observed. For the Wert and KHRT models, saturation is
achieved and the variation of 𝑌∞ with time will not alter the outcome,
that complete evaporation will not occur. A time-varying model for
the vapor fraction can be implemented using the approach outlined
here but was unnecessary at this time. The surface vapor fraction, 𝑌𝑆,
is found by assuming that the surface layer of gas is at the droplet
temperature and is saturated with vapor.
Mass transport properties (e.g. Sh and 𝑣) were evaluated at the
film temperature 𝑇𝑓 and density 𝜌𝑓 . The film properties are estimated
as being 1/3 the free stream value (post shock dry gas conditions)
and 2/3 the surface values, e.g. film weighting factor 𝐴𝑟 = 1∕3 in
Eq. (A.28) (Abramzon and Sirignano, 1989). The temperature at the
surface of the droplet was taken to be the uniform droplet temperature
set to the wet bulb value 𝑇𝑝 = 𝑇𝑤𝑏. The surface gas density was
evaluated for the saturated mix of gas and vapor at 𝑌𝑆 and 𝑇𝑆. A
total evaporation time was computed using the initial steady-state mass
transfer rate, ̇ 𝑚𝐵, to find the time rate of change of the diameter
squared, 𝑑
𝑑𝑡
(𝑑2
𝑐
). The 𝐷2 law assumes that this value is constant over
the life of the droplet, thus we can predict the total evaporation time
by predicting when 𝑑2
𝑐 = 0 (see Eqs. (A.32) and (A.33)).
5.6. Comparison of models to experimental data
The results of the CDC model are plotted for each model for two
parent droplet sizes, 𝑑10 ∼ 14 .16 [μ m] and 𝑑32 ∼ 37 .3 [μ m], in Fig. 19.
The performance of the CDC model is strongly dependent on droplet
acceleration during deformation, the breakup time, and child droplet
size. The droplet trajectory was modified, as the deforming parent
droplet is accelerated and child droplets are produced. The parent
droplet will experience its highest acceleration as the shape deforms to
an oblate disk, resulting in a shorter velocity equilibration time. This
effect modifies the parent droplet trajectory and child droplet cloud
length at early times, from 𝜏𝑏𝑖 to 𝜏𝑏𝑡, and may be observed clearly in the
Wert49 and Hsiang droplet model results. Even though the Wert49 and
Hsiang models create similar child droplet sizes for a 37.3 [ μm] parent
droplet, the Hsiang model breakup times, being shorter, reduce the
parent droplet lag and thus the child droplet cloud length. Further, the
larger the parent droplet, the greater the parent droplet lag distance,
despite the lower acceleration rate.
The KHRT model considers the droplet to immediately break up,
producing small child droplets that equilibrate rapidly with the shocked
gas. Since the KH time is longer than the RT time, the droplet will
be stripped of mass by the KH initially; however, RT breakup will
terminate the breakup process. The RT mechanism produces slightly
larger child droplets, but still possesses short equilibration times. The
parent droplet lag, over the short time between KH onset and RT final
breakup, contributes significantly to the cloud length. The Wert model,
having only slightly larger breakup times and similar child droplet
sizes, produces slightly large cloud lengths (Fig. 19). Both the KHRT
and Wert models have cloud volumes that are sufficiently small that
the cloud gas will be saturated, thus evaporation will not consume all
the liquid droplet mass unless additional cloud mixing effects are in-
cluded. This evaporation effect is, in essence, a particle–particle effect,
sometimes referred to as three-way coupling and typically limited to
high volume fractions.
The Wert49 and Hsiang models produce longer breakup times and
larger child droplet sizes, resulting in larger child droplet clouds. As
discussed in the previous section, vapor fractions were much smaller
as the cloud volume increased with cloud length and by the square of
the cloud width. Thus, the child droplets evaporate as if they are in the
free stream gas, without affecting one another, with no particle–particle
effects. Predictions from the Wert49 and Hsiang models show better
agreement when compared with the experimental measurements in
terms of the child droplet cloud size, the transient acceleration response
during deformation, and the predicted evaporation times. The varying
evaporation times between the 𝑑32 and 𝑑10 droplet sizes help to explain
the slight upward trend in cloud length at late times. As clouds from
small parent droplets evaporate, the mean cloud size trends towards
the larger clouds produced by larger parent droplets.
Overall, the Wert49 model produced the best match to the experi-
mental data, though it still under predicts the largest cloud lengths. One
reason for this may be that child droplet sizes are certainly produced in
excess of the 𝑑32 size as it is only a statistical representation of the size
distribution tail. The trajectory of the small parent droplet cloud sizes
predicted is also somewhat smaller than experimental measurements.
One possible reason is that the parent droplet experiences a stronger
drag than our model predicts; recall that the current model uses an
average of drag properties estimated for a deforming parent droplet.
With this in mind, the data of Kobiera et al. (2009) was con-
sidered for further validation of the proposed CDC model. These ex-
periments measured the child droplet cloud lengths over time for
various millimeter-sized ( 0.6–2.0 [mm]) n-hexane droplets. Owing to
their larger size, these droplets will have longer evaporation times
relative to their velocity equilibration times. This data serves then to
test the CDC model on larger parent droplets, in a different 𝑊 𝑒 regime
with little evaporation effects. Both the Wert49 and Hsiang breakup
mechanisms showed some agreement, while the KHRT and original
Wert model had poor agreement, and thus, are not shown. Fig. 20,
shows the data of Kobiera et al. (2009), reproduced by digitization of
figures 15 and 18 in the cited paper.
Overall, agreement is good for the Wert49 model at late times for
the 1–2 [mm] droplets (within ∼9 [%] error). The early time trajectories
of the droplets show less agreement as the experimental data for the
0.6–1.3 [mm] droplets show an inflection that cannot be reproduced
by the CDC model, and is not consistent with the 2 [mm] droplet data.
The 1 and 1.3 [mm] experimental data also show a sudden decrease
in cloud length at 𝑡 ∼ 300 [μ s] that cannot be explained by the physics
considered in this paper. The 0.6 [mm] droplet data aligns closely with
the 1 [mm] data and thus does not agree well with the Wert49 CDC
model predictions. The Hsiang model matched the results well for the
1.3 [mm] size, due in part to the anomalous drop at 𝑡 ∼ 300 [μ s],
but the Wert 49 model showed overall better agreement. Without
further information on the experimental conditions of this work, we
cannot provide further insight as to the sources of disagreement. Other
breakup models showed poorer agreement, with the Wert and KHRT
models having greater than ∼80 [%] error. The Wert49 model fit can
be improved by increasing the parent droplet acceleration considering
a higher weighting of the oblate versus sphere properties over the
breakup time (see Appendix A.4, a weighting of 1/2 worked well).

<!-- PDF_PAGE: 13 -->

International Journal of Multiphase Flow 161 (2023) 104389
13
V. Duke-Walker et al.
Fig. 19. Cloud length 𝐿𝑥 versus time comparison between model and experimental results.
Fig. 20. Cloud length 𝐿𝑥 results: utilizing the empirical Wert49 and Hsiang breakup
model.
6. Conclusion
Experiments were performed to examine the shock-driven simul-
taneous breakup and evaporation of small droplets. The droplet sizes
(14.16 < 𝑑 𝑝 < 37.3 [μ m]) and shock wave Mach number ( 𝑀 ∼ 2 .09)
produced Weber numbers in the range of 600 < 𝑊 𝑒 < 1800 and
Reynolds numbers in the range of 1600 < 𝑅𝑒 < 4400, resulting in rapid
velocity equilibration times and droplet evaporation. A simple model,
the child droplet cloud (CDC) model, was developed to provide further
insight into the experimental data and the physics of small droplet
breakup and evaporation. Four breakup models were considered, one
analytical model (KHRT model) and three empirical models (Wert,
Hsiang, and Wert49) based on experimental observations of larger
droplets at lower shock wave Mach numbers. Evaporation times were
estimated using the 𝐷2 law for characteristic large child droplets,
accounting for the saturation of the cloud gas. Child droplet cloud
lengths and evaporation times were estimated for both the 𝑑10 and 𝑑32
sizes measured in experiments.
The empirical models considered provided the best prediction of the
child droplet cloud length and evaporation time. The Wert49 model,
a modified version of the Wert model ( Wert, 1995) developed in our
previous work ( Duke-Walker et al. , 2021), was found to most closely
predicted child droplet trajectories and evaporation time. The model
deficiencies are likely due to the underprediction of the parent droplet
drag force during breakup or possibly due to the presence of larger
child droplets than predicted. The Hsiang breakup model ( Hsiang and
Faeth, 1992 ) produced similar results but predicted slightly smaller
droplet cloud lengths than measured. The CDC model, with the Wert49
breakup mechanism, also compared well to previously published data
for millimeter-sized droplets accelerated by a 𝑀 = 2 shock wave
(21,000 < 𝑊 𝑒 < 70,000) ( Kobiera et al. , 2009 ). Both models found
that child droplet clouds were large enough that the vapor content
remained low and droplet evaporation was not effected by neighboring
child droplets.
The KHRT model predicted rapid production of very small KH child
droplets followed by an RT breakup event terminating the breakup
process. The RT droplet sizes predicted were larger than the KH
droplets and similar in size to the droplet sizes predicted by the original
Wert model. While the Wert and KHRT models produced similar child
droplet sizes, the Wert model predicted larger cloud lengths due to
its greater breakup times and resulting increase in parent droplet lag
distance. Both models produced sufficiently small cloud volumes that
vapor saturation was achieved, thus evaporation could not completely
consume the liquid mass. The KHRT model resulted in the smallest
child cloud lengths.
The CDC model results indicate that cloud lengths are largely driven
by overall breakup times, parent droplet drag forces during breakup,
and child droplet size distributions, resulting in varying lag distances.
Overall, the empirical models derived from experiments at low 𝑊 𝑒
produce better agreement with our observations at high 𝑊 𝑒. An ex-
planation for this might be found in the KHRT model, as it predicts
breakup as a function of surface hydrodynamic instabilities, rather
than a function of 𝑊 𝑒. For our case, the KHRT model predicted that
RT growth rates would be significant, preempting the KH breakup
process, due to the rapid acceleration of small droplets at high velocity.
The KHRT model also predicts RT breakup for large droplets at low
𝑊 𝑒, similar to the experimental conditions used for the empirical
model. Further, the KHRT model predicts the early formation of very

<!-- PDF_PAGE: 14 -->

International Journal of Multiphase Flow 161 (2023) 104389
14
V. Duke-Walker et al.
small droplets, as assumed by the CDC model. Thus, the underlying
interpretation of the breakup process in the KHRT model has merit.
Further analysis of the KH and RT mechanisms should be undertaken
to provide better timing for the onset of the RT mechanism and better
representative child droplet sizes. For now, the CDC model with the
Wert49 breakup model provides the best match for child droplet cloud
sizes and evaporation times for parent drops in the range of700 < 𝑊 𝑒 <
70,000 and 𝑂ℎ < 0.1.
Our future experimental work will focus on understanding the
behavior of the acceleration term and breakup times on an interface
composed of monodisperse droplets, in order to better determine the
effects of droplet diameter on breakup and evaporation. Future the-
oretical work should focus on deriving more accurate parameters for
the KH and RT instabilities on a breaking droplet. The CDC model will
be implemented in our particle-in-cell simulations with more advanced
time-varying deformation, drag, and evaporation models. Experimen-
tal observations of surface instabilities are needed for small droplets
at high velocities. High-resolution simulations may also yield much
needed insight into the interface physics.
CRediT authorship contribution statement
Vasco Duke-Walker: Conceptualization, Writing – original draft,
Writing – review & editing, Investigation, Methodology, Visualization.
Benjamin J. Musick: Writing – review & editing, Writing – original
draft. Jacob A. McFarland: Supervision, Writing – review & editing,
Funding acquisition, Methodology.
Declaration of competing interest
The authors declare the following financial interests/personal rela-
tionships which may be considered as potential competing interests:
Jacob A. McFarland reports financial support was provided by National
Science Foundation. Jacob A. McFarland reports financial support was
provided by Office of Naval Research.
Data availability
Data will be made available on request.
Acknowledgments
This work was supported by the National Science Foundation,
United States through award number 2053154 and the Office of Naval
Research, United States through contract number N00014-20-1-2796.
Appendix. Child droplet cloud model details
A.1. Predicted gas properties
Post-shock properties (pressure, temperature, and velocity) were
calculated using the ideal gas shock-jump equations. Phase change
properties (e.g. saturation pressure and latent heat) and transport prop-
erties (e.g. viscosity) were taken from Engineering Equation Solver
(EES). Gas mixture properties were calculated assuming ideal gas mix-
tures and psychrometric equilibrium. EES iteratively solved the system
of equations of the CDC model using a forward Euler time marching
method (1st order accuracy in space and time).
A.2. Drag model
The simple drag force for a spherical rigid particle is calculated as
𝐹𝐷 = 𝑎𝑝𝑚𝑝, where 𝑚𝑝 is the mass of the particle and 𝑎𝑝 is the particle
acceleration shown in Eq. (A.1), where 𝑣𝑝 is the particle velocity, 𝐶𝐷,𝑠
is the drag coefficient of a sphere, and 𝜌𝑔 and 𝜌𝑝 the gas and particle
densities.
𝑎𝑝 = 𝐶𝐷,𝑠
3
4
𝜌𝑔
𝜌𝑝
|𝑣𝑔 − 𝑣𝑝|
𝑑𝑝
(𝑣𝑔 − 𝑣𝑝
) (A.1)
The drag coefficient for a simple spherical droplet is taken to follow
the Kliatchko drag model (Klyachko, 1934), shown in Eq. (A.2), where
𝜇𝑔 is the gas kinematic viscosity.
𝐶𝐷,𝑠 =
{ 24∕𝑅𝑒 + 4∕𝑅𝑒1∕3 𝑅𝑒 ≤ 1000
0.424 𝑅𝑒 > 1000 (A.2)
A.3. Droplet trajectories
Analytical solutions to Eq. (A.1) with 𝐶𝐷,𝑠 from Eq. (A.2) were pre-
sented by Cloutman (1988) and used to model the particle dynamics.
The cloud length is imagined as the distance between a small child
droplet created at 𝑡 = 𝑡𝑏,𝑖 traveling at the gas velocity and the location
of a characteristic large child droplet created at 𝑡 = 𝑡𝑏𝑡. It is tracked as a
function of the lag distance of the largest child droplet from the moment
the first small droplet is created, 𝑡 = 𝑡𝑏𝑖. The lag distance is defined
as the distance between a particle and the gas it was initialized in,
𝐿𝑥(𝑡) = |𝑣𝑔,𝑗 𝑡 − 𝑥𝑝,𝑗 (𝑡)| where 𝑗 is the index 𝑥 or 𝑦, 𝑣𝑔,𝑗 is the gas velocity
component and 𝑥𝑝,𝑗 (𝑡) is the instantaneous coordinate of a particle with
𝑥𝑝,𝑗 (𝑡 = 0) = 0 .
The total lag distance of the large child droplet is found as the
sum of the parent droplet lag distance from 𝑡 = 𝑡𝑏𝑖 to 𝑡 = 𝑡𝑏𝑡 and the
large child droplet thereafter, 𝑡 > 𝑡 𝑏𝑡. This distance is taken to be the
cloud length, 𝐿𝑗 (𝑡) = 𝐿𝑝,𝑗 (𝑡𝑏𝑡) + 𝐿𝑐,𝑗 (𝑡). The process for calculating the
individual lag distances is outlined in the steps below. It is assumed
that the shock acceleration occurs only in the 𝑥 direction.
(1) The drag acceleration coefficient of the parent droplet, 𝐴𝑝,𝑥, is
calculated assuming constant drag properties produced by a weighted
average of a sphere and an oblate disk (see Section 5.3). The weighted
properties are assigned a subscript of 𝑑. Since all parent droplets had
𝑅𝑒 > 1000, the velocity and trajectory were computed following the
high-speed solution (Eq. (A.3)).
𝐴𝑝,𝑥 = 3
4 𝐶𝐷,𝑑
𝜌𝑔
𝜌𝑝
[
𝑑𝑝𝑑
2
𝑑3
𝑝
]
(A.3)
(2) The parent droplet velocity, 𝑣𝑝,𝑥(𝑡), is calculated as
𝑣𝑝,𝑥(𝑡) = 𝑣𝑔,𝑥∕ [1 + 𝐴𝑝,𝑥𝑣𝑔,𝑥𝑡] if 𝑡 ≤ 𝑡𝑏𝑡 (A.4)
(3) The parent droplet lag distance, 𝐿𝑝,𝑥 is calculated from breakup
initiation to completion, 𝑡𝑏𝑖 ≤ 𝑡 ≤ 𝑡𝑏𝑡, starting with a position 𝑥𝑝,𝑥(𝑡𝑏𝑖) =
0. Since the shock acceleration is only in the 𝑥 direction, 𝐿𝑝,𝑦 = 0 and
𝑣𝑔,𝑦 = 0.
𝐿𝑝,𝑥(𝑡) = 𝑥𝑝,𝑥(𝑡𝑏𝑖) + 𝐴−1
𝑝,𝑥𝑙𝑛[1 + 𝐴𝑝,𝑥𝑣𝑔,𝑥(𝑡 − 𝑡𝑏,𝑖)]
if 𝑡𝑏𝑖 ≤ 𝑡 ≤ 𝑡𝑏𝑡
(A.5)
(4) A large child droplet is produced at 𝑡 = 𝑡𝑏𝑡 with initial 𝑥 velocity
of the parent droplet, 𝑣𝑐,𝑗 (𝑡𝑏𝑡) = 𝑣𝑝,𝑗 (𝑡𝑏𝑡) and 𝑦 velocity given by the
TAB model (see Appendix A.4). The velocity of the child droplets is
small enough, low 𝑅𝑒 < 1000, such that they follow the low-speed
solution from (Cloutman, 1988) with constants 𝐵𝑐, and 𝐶𝑐 presented
in Eqs. (A.6) and (A.7), where 𝑑𝑐 is the large child droplet diameter.
The velocity is then calculated as shown in Eq. (A.8).
𝐵𝑐 = 4.5
[
4𝜇𝑔
𝑑𝑐
2𝜌𝑝
]
(A.6)
𝐶𝑐 = 3−1
21∕3
[𝑑𝑐 𝜌𝑔
2𝜇𝑔
]2∕3
(A.7)

<!-- PDF_PAGE: 15 -->

International Journal of Multiphase Flow 161 (2023) 104389
15
V. Duke-Walker et al.
𝑣𝑐,𝑗 (𝑡) =
[(
𝑣𝑐,𝑗 (𝑡𝑏𝑡)− 2
3 + 𝐶𝑐
)
𝑒
2𝐵𝑐 (𝑡−𝑡𝑏𝑡)
3 − 𝐶𝑐
]−1.5
(A.8)
if 𝑡 > 𝑡 𝑏𝑡
(5) The lag distance of the large child droplet is defined with respect
to its origin as 𝐿𝑐,𝑗 (𝑡𝑏𝑡) = 0 . The child drop lag distance is shown in
Eq. (A.9).
𝐿𝑐,𝑗 (𝑡) = 3
𝐵𝑐 𝐶𝑐
|||||||
𝑣𝑐,𝑗 (𝑡𝑏𝑡)1∕3 − 𝑣𝑐,𝑗 (𝑡)1∕3+
𝐶 −1∕2
𝑐 𝑡𝑎𝑛−1 (𝐶𝑐
−1∕2𝑣𝑐,𝑗 (𝑡𝑏𝑡)−1∕3)−
𝐶 −1∕2
𝑐 𝑡𝑎𝑛−1 (𝐶𝑐
−1∕2𝑣𝑐,𝑗 (𝑡)−1∕3)
|||||||
if 𝑡 > 𝑡 𝑏𝑡
(A.9)
(6) The total child droplet cloud length and width can now be
calculated as a function of 𝑡. The maximum cloud size is calculated
when velocity equilibrium is achieved, 𝑣𝑐,𝑖 = 0 .01𝑣𝑔,𝑖. By substituting
these values into Eq. (A.9), and adding the total parent drop lag
distance, the maximum cloud dimension are obtained. It is assumed
that the 𝑧 cloud dimension is the same as the 𝑦 dimension.
(7) Droplet trajectory were calculated until 𝑡 = 𝑡𝑒𝑣𝑝, as show in
Appendix A.6.
A.4. Deformation model
The parent droplet drag properties were calculated by taking a
weighted average between a sphere and an oblate disk properties. This
approach follows the results of Chou and Faeth (1998). The average
deformation drag coefficient 𝐶𝐷,𝑑 and an effective particle deformed
diameter 𝑑𝑝𝑑 were calculated below where the maximum distortion 𝑑𝑎
was taken when 𝑦∗ = 2(𝑑𝑎 − 𝑑𝑝)∕𝑑𝑝 = 1.
𝑑𝑝𝑑 =
√
𝑑𝑝
2 ⋅ (1 − 𝑦∗) + 𝑑𝑎
2 ⋅ 𝑦∗ (A.10)
𝐶𝐷,𝑑 = 𝐶𝐷,𝑠 ⋅ (2∕3) + 𝐶𝐷,𝑑𝑠𝑘 ⋅ (1∕3) (A.11)
The parent droplet deformation rate was computed using the TAB
model (O’Rourke and Amsden, 1987) to provide a predicted initial
child droplet radial velocity. It should be noted that the TAB model
deformation rate would also indicate the breakup initiation time, 𝑡𝑏𝑖,
but this time is supplanted by the prescribed breakup models for cloud
length predictions. While these 𝑡𝑏𝑖 values are similar, this does create a
small inconsistency in this approach. Nevertheless, the TAB model was
used to provide an estimate for the child droplet radial velocities as
outlined below.
(1) The oscillation frequency for droplet oscillations, 𝜔 is calculated
using Eq. (A.12) where 𝐶𝑘 = 8 , 𝐶𝑏 = 0 .5 and 𝐶𝐹 = 1∕3 are
the fundamental oscillation frequency, north and south amplitude of
oscillation described by O’Rourke and Amsden (1987). This equation
assumes that the viscosity of the liquid has a negligible effect on the
oscillation frequency as is true for our case (acetone).
𝜔 =
[
𝐶𝑘𝜎
𝜌𝑝(𝑑𝑝∕2)3
]1∕2
(A.12)
(2) The surface velocity of the droplet is calculated from the defor-
mation rate.
̇ 𝑦(𝑡) = 𝑊𝑒
[ 𝐶𝐹
𝐶𝑘𝐶𝑏
]
⋅ 𝜔 ⋅ 𝑠𝑖𝑛(𝜔 ⋅ 𝑡) (A.13)
(3) The surface velocity is assumed to reach a maximum at the time
of maximum distortion, 𝑡𝑑.
𝑡𝑑 = 𝑐𝑜𝑠−1
(
1 − 12
𝑊𝑒
)
∕𝜔 (A.14)
(4) The child droplet velocity does take on the full value of the
surface velocity but is instead reduced by a surface energy balance
factor, 𝛼, as explained by Tanner (1997).
𝛼2 = 5
4 𝐶𝐷,𝑠 + 18
𝑊 𝑒 (1 − 𝑑𝑝∕𝑑𝑐 ) (A.15)
𝑣𝑐,𝑦(𝑡𝑏𝑡) = 𝛼 ̇ 𝑦(𝑡𝑑 ) (A.16)
A.5. Breakup models
The breakup times and child droplet sizes are set by one of the four
models discussed in the main text (KHRT, Wert, Hsiang, and Wert49)
as follows:
(1) The breakup parameters ( 𝑊 𝑒, 𝑅𝑒, and 𝑂ℎ) are calculated for
the post-shock interface gas condition as described in the main text.
The characteristic breakup time 𝑡𝑐 is calculated in Eq. (A.17).
𝑡𝑐 = 𝑑
𝑣𝑔
( 𝜌𝑝
𝜌𝑔
)0.5
(A.17)
(2) The breakup initiation times, 𝑡𝑏𝑖,𝑡 = 𝜏𝑏𝑖,𝑡 ⋅ 𝑡𝑐, are calculated
from the non-dimensional breakup times as given in Eq. (A.18), where
𝑊 𝑒𝛿 = (𝑊 𝑒 − 12). The KH initiation time is by definition 0.
𝜏𝑏𝑖 =
⎧
⎪
⎪
⎨
⎪
⎪⎩
1.9𝑊 𝑒−0.25
𝛿 Wert
𝑚𝑖𝑛(3, 3.3284𝑊 𝑒−0.131
𝛿 ) Wert49
1.6
1−(𝑂ℎ∕7) Hsiang
0 KH
(A.18)
(3) For the KHRT model, the growth rate (Eqs. (A.19) and (A.21))
and wavelength (Eqs. (A.20) and (A.22)) are calculated for the most
unstable mode for both the KH and RT instabilities. In these equations,
𝑇𝑎 = 𝑂ℎ
√
𝑊 𝑒 is the Taylor number and 𝐵0 = 0.61, 𝐵1 =
√
3, 𝐶𝑅𝑇 = 0.1
and 𝐶𝜏 = 1 are constants (Beale and Reitz, 1999).
𝛺𝐾𝐻 = 0.34 + 0.38𝑊 𝑒1.5
(1 + 𝑂ℎ)(1 + 1.4𝑇 𝑎0.6)
√ 𝜎
𝜌𝑔(𝑑𝑝∕2)3 (A.19)
𝛬𝐾𝐻 =
9.02𝑟𝑝(1 + 0.45
√
𝑂ℎ)(1 + 0.4𝑇 𝑎0.7)
(1 + 0.865𝑊 𝑒1.67)0.6 (A.20)
𝛺𝑅𝑇 =
√√√√ 2
3
√
3𝜎
[𝑎𝑝(𝜌𝑝 − 𝜌𝑔)]1.5
𝜌𝑝 + 𝜌𝑔
(A.21)
𝐾𝑅𝑇 =
√
𝑎𝑝(𝜌𝑝−𝜌𝑔 )
3𝜎
𝛬𝑅𝑇 = 2𝜋𝐶𝑅𝑇 ∕𝐾𝑅𝑇
(A.22)
(4) The total breakup time is computed from the empirical and
theoretical models.
𝜏𝑏𝑡 =
⎧
⎪
⎪
⎪
⎨
⎪
⎪
⎪⎩
14.1𝑊 𝑒−0.25
𝛿 Wert
6 Wert49
5
1−(𝑂ℎ∕7) Hsiang
3.726𝐵1𝑑𝑝
2𝑡𝑐 𝛺𝐾𝐻
KH
𝐶𝜏
𝑡𝑐 𝛺𝑅𝑇
RT
(A.23)
(5) The representative child drop sizes for the different breakup of
models are calculated as follows.
𝑑𝑐 =
⎧
⎪
⎪
⎪
⎪
⎨
⎪
⎪
⎪
⎪⎩
0.32 [𝑊 𝑒(𝜏𝑏,𝑡 − 𝜏𝑏,𝑖)]2∕3 𝜎
𝑣2𝑔 𝜌𝑔
Wert
0.49 [𝑊 𝑒(𝜏𝑏,𝑡 − 𝜏𝑏,𝑖)]2∕3 𝜎
𝑣2𝑔 𝜌𝑔
Wert49
6.2𝑑𝑝
(
𝜌𝑝
𝜌𝑔
)0.25(
𝜇𝑝
𝜌𝑝𝑑𝑝𝑣𝑔
)0.5
Hsiang
2𝐵0𝛬𝐾𝐻 KH
𝛬𝑅𝑇 RT
(A.24)
A.6. Evaporation models
The evaporation time is derived from the 𝐷2 law (Crowe et al.,
1998) and the instantaneous droplet vaporization rate ̇ 𝑚𝐵 proposed
by Abramzon and Sirignano (1989). The evaporation time is calculated
as follows:
(1) The maximum volume (when velocity equilibrium is achieved)
occupied by the cloud is calculated as an ellipsoid.
𝑉𝑐𝑙𝑜𝑢𝑑 = 4
3 𝜋(𝐿𝑦
)2 (𝐿𝑥∕2) (A.25)

<!-- PDF_PAGE: 16 -->

International Journal of Multiphase Flow 161 (2023) 104389
16
V. Duke-Walker et al.
(2) The maximum vapor mass fraction possible is calculated for
the droplet mass and cloud dry gas mass, 𝑚𝑔, using the wet bulb
temperature 𝑇𝑤𝑏, post-shock pressure 𝑃𝑔, and cloud volume 𝑉𝑐𝑙𝑜𝑢𝑑 . In
Eq. (A.26), the subscript 𝑔 denotes properties of the dry gas,𝑣 the vapor
species, and 𝑚 the mixture of gas and vapor. 𝑅𝑢 is the universal gas
constant The wet bulb temperature is found by solving the adiabatic
saturation problem (conservation of energy at saturation).
𝑚𝑚 = 𝑚𝑔 + 𝑚𝑝
𝑌𝑣𝑚𝑎𝑥 =
𝑚𝑝
𝑚𝑚
𝑅𝑚 = 𝑅𝑢 ⋅
[
1−𝑌𝑣𝑚𝑎𝑥
𝑀𝑊 𝑔
+ 𝑌𝑣 𝑚𝑎𝑥
𝑀𝑊 𝑣
]
𝑃𝑔 ⋅ 𝑉𝑐𝑙𝑜𝑢𝑑 = 𝑚𝑚𝑅𝑚𝑇𝑤𝑏
(A.26)
(3) The vapor fraction in the cloud is set to the lower of 𝑌𝑣𝑚𝑎𝑥
and 𝑌𝑠𝑎𝑡 the equilibrium saturation mass fraction. The Spalding mass
transfer number 𝐵𝑀 is then calculated with 𝑌𝑠, the droplet surface
vapor mass fraction.
𝐵𝑀 = 𝑌𝑠 − 𝑌∞
1 − 𝑌𝑠
(A.27)
(4) The film conditions for temperature and density are taken as a
weighting between the free stream gas and the droplet surface condi-
tions, where 𝐴𝑟 is a film weighting factor taken to be 1/3 (Abramzon
and Sirignano, 1989). In Eqs. (A.28) and (A.29), the subscript𝑔 denotes
the post-shock, free stream, and dry gas conditions, as before.
𝑇𝑓 = 𝐴𝑟𝑇𝑔 + (1 − 𝐴𝑟) ⋅ 𝑇𝑝 (A.28)
𝜌𝑓 = 𝐴𝑟𝜌𝑔 + (1 − 𝐴𝑟) ⋅ 𝜌𝑠 (A.29)
(5) From these conditions, we proceed to calculate the mass transfer
rate ̇ 𝑚𝐵, where the Sherwood number 𝑆ℎ = 2, and 𝑣 is the diffusivity
calculated from the Gililland model, Eq. (A.30) where ∕𝑛𝑢 is the atomic
diffusion volume for each species (see Dahal and McFarland (2017) for
more).
𝑀𝑊 𝑣 = (1∕𝑀𝑊 𝑔 + 1∕𝑀𝑊 𝑣)
𝑣 = 0.0043
𝑇𝑓 [𝐾]1.5
𝑃𝑔 [𝑎𝑡𝑚](𝜈1∕3
𝑔 +𝜈1∕3
𝑣 )
2
√
𝑀𝑊 𝑣
1002
(A.30)
̇ 𝑚𝐵 = 𝑆ℎ𝜋𝑑 𝑐 𝜌𝑓 𝑣𝑙𝑛(1 + 𝐵𝑀 ) (A.31)
(6) The evaporation time is estimated following the 𝐷2 law (Abram-
zon and Sirignano, 1989; Crowe et al., 1998).
𝜆 = 4
𝜋
̇ 𝑚𝐵
𝜌𝑝𝑑𝑐
(A.32)
𝑡𝑒𝑣𝑝 = 𝑑𝑐
2
𝜆 (A.33)
References
Abramzon, B., Sirignano, W.A., 1989. Droplet vaporization model for spray combustion
calculations. Int. J. Heat Mass Transfer 32 (9), 1605–1618.
Balakumar, B., Orlicz, G., Tomkins, C., Prestridge, K., 2008. Simultaneous particle-
image velocimetry–planar laser-induced fluorescence measurements of Richtmyer–
Meshkov instability growth in a gas curtain with and without reshock. Phys. Fluids
20 (12), 124103.
Beale, J.C., Reitz, R.D., 1999. Modeling spray atomization with the Kelvin-
Helmholtz/Rayleigh-Taylor hybrid model. At. Spray. 9 (6).
Black, W.J., Denissen, N.A., McFarland, J.A., 2017. Evaporation effects in shock-driven
multiphase instabilities. J. Fluids Eng. 139 (7), 071204. http://dx.doi.org/10.1115/
1.4036162.
Chou, W.-H., Faeth, G., 1998. Temporal properties of secondary drop breakup in the
bag breakup regime. Int. J. Multiph. Flow. 24 (6), 889–912.
Cloutman, L.D., 1988. Analytical solutions for the trajectories and thermal histories of
unforced particulates. Amer. J. Phys. 56 (7), 643–645.
Crowe, C., Sommerfeld, M., Tsuji, Y., et al., 1998. Multiphase Flows with. CRC Press.
Dahal, J., McFarland, J.A., 2017. A numerical method for shock driven multiphase
flow with evaporating particles. J. Comput. Phys. 344, 210–233. http://dx.doi.
org/10.1016/j.jcp.2017.04.074, URL: https://linkinghub.elsevier.com/retrieve/pii/
S0021999117303625.
Duke-Walker, V., Allen, R., Maxon, W.C., McFarland, J.A., 2020. A method for
measuring droplet evaporation in a shock-driven multiphase instability. Int. J.
Multiph. Flow. 133, 103464.
Duke-Walker, V., Maxon, W.C., Almuhna, S.R., McFarland, J.A., 2021. Evaporation and
breakup effects in the shock-driven multiphase instability. J. Fluid Mech. 908.
Goossens, H., Cleijne, J., Smolders, H., Van Dongen, M., 1988. Shock wave induced
evaporation of water droplets in a gas-droplet mixture. Exp. Fluids 6 (8), 561–568.
Guildenbecher, D.R., Gao, J., Chen, J., Sojka, P.E., 2017. Characterization of drop
aerodynamic fragmentation in the bag and sheet-thinning regimes by crossed-beam,
two-view, digital in-line holography. Int. J. Multiph. Flow. 94, 107–122.
Hsiang, L.-P., Faeth, G., 1992. Near-limit drop deformation and secondary breakup.
Int. J. Multiph. Flow. 18 (5), 635–652. http://dx.doi.org/10.1016/0301-9322(92)
90036-G, URL: https://linkinghub.elsevier.com/retrieve/pii/030193229290036G.
Kirar, P.K., Soni, S.K., Kolhe, P.S., Sahu, K.C., 2022. An experimental investigation of
droplet morphology in swirl flow. J. Fluid Mech. 938.
Klyachko, L., 1934. Heating and ventilation. USSR J. Otopl. I Ventil (4).
Kobiera, A., Szymczyk, J., Wolański, P., Kuhl, A., 2009. Study of the shock-induced
acceleration of hexane droplets. Shock Waves 18 (6), 475–485.
Lang, R.J., 1962. Ultrasonic atomization of liquids. J. Acoust. Soc. Am. 34 (1), 6–8.
Leiby, M., 2021. Ultrasonic spray nozzles. URL: https://microspray.com/nozzles/.
Liu, A.B., Mather, D., Reitz, R.D., 1993. Modeling the effects of drop drag and breakup
on fuel sprays. SAE Trans. 83–95.
Loomis, D.J.S., 2022. Produce orthonormal view from oblique projective image, URL:
https://johnloomis.org/ece564/notes/tform/planar/html/planar2.html.
Mauro, S., Brusca, S., Lanzafame, R., Famoso, F., Galvagno, A., Messina, M., 2017.
Small-scale open-circuit wind tunnel: Design criteria, construction and calibration.
Int. J. Appl. Eng. Res. 12 (23), 13649–13662.
Meng, J., Colonius, T., 2018. Numerical simulation of the aerobreakup of a water
droplet. J. Fluid Mech. 835, 1108–1135. http://dx.doi.org/10.1017/jfm.2017.804.
Middlebrooks, J.B., et al., 2019. Shock Tube Experimentation Utilizing Advance
Diagnostics for the Study of an Impulsively Accelerated Multiphase Cylinder (Ph.D.
thesis). University of Missouri–Columbia.
Nicholls, J., Ranger, A., 1969. Aerodynamic shattering of liquid drops. AIAA J. 7 (2),
285–290.
Orlicz, G.C., 2007. Shock Driven Instabilities in a Varicose, Heavy-Gas Curtain: mach
Number Effects (Ph.D. thesis). University of New Mexico.
O’Rourke, P.J., Amsden, A.A., 1987. The TAB Method for Numerical Calculation of
Spray Droplet Breakup. Technical Report, Los Alamos National Lab.(LANL), Los
Alamos, NM (United States).
Park, G., Yeom, G.-S., Hong, Y.K., Moon, K.H., 2017. Experimental study of time-
dependent evolution of water droplet breakup in high-speed air flows. Int. J.
Aeronaut. Space Sci. 18 (1), 38–47.
Paudel, M., Dahal, J., McFarland, J., 2018. Particle evaporation and hydrodynamics in a
shock driven multiphase instability. Int. J. Multiph. Flow. 101, 137–151. http://dx.
doi.org/10.1016/j.ijmultiphaseflow.2018.01.008, URL: https://www.sciencedirect.
com/science/article/pii/S0301932217306523.
Pilch, M., Erdman, C.A., 1987. Use of breakup time data and velocity history data to
predict the maximum size of stable fragments for acceleration-induced breakup of
a liquid drop. Int. J. Multiph. Flow. 13 (6), 741–757.
Sharma, S., Chandra, N.K., Basu, S., Kumar, A., 2022. Advances in droplet aerobreakup.
Eur. Phys. J. Spec. Top. 1–15.
Stefanitsis, D., Koukouvinis, P., Nikolopoulos, N., Gavaises, M., 2021. Nu-
merical investigation of the aerodynamic droplet breakup at mach num-
bers greater than 1. J. Energy Eng. 147 (1), 04020077. http://dx.doi.org/
10.1061/(ASCE)EY.1943-7897.0000720, arXiv:https://ascelibrary.org/doi/pdf/10.
1061/%28ASCE%29EY.1943-7897.0000720, URL: https://ascelibrary.org/doi/abs/
10.1061/%28ASCE%29EY.1943-7897.0000720.
Stefanitsis, D., Strotos, G., Nikolopoulos, N., Kakaras, E., Gavaises, M., 2019. Improved
droplet breakup models for spray applications. Int. J. Heat Fluid Flow 76, 274–
286. http://dx.doi.org/10.1016/j.ijheatfluidflow.2019.02.010, URL: https://www.
sciencedirect.com/science/article/pii/S0142727X18309007.
Tanner, F.X., 1997. Liquid jet atomization and droplet breakup modeling of
non-evaporating diesel fuel sprays. SAE Trans. 127–140.
Theofanous, T., Mitkin, V., Ng, C., Chang, C., Deng, X., Sushchikh, S., 2012. The physics
of aerobreakup. II. Viscous liquids. Phys. Fluids 24 (2), 022104.
TSI, 2022. Phase Doppler Particle Analyzer Manual, URL: https://tsi.com/products/
fluid-mechanics-systems/phase-doppler-particle-analyzer-(pdpa)-systems/.
Wert, K., 1995. A rationally-based correlation of mean fragment size for drop secondary
breakup. Int. J. Multiph. Flow. 21 (6), 1063–1071.
Widdecke, N., Klenk, W., Frohn, A., 1995. Impact of strong shock waves on monodis-
perse isopropanol droplet streams. In: Shock Waves@ Marseille III. Springer, pp.
89–94.
