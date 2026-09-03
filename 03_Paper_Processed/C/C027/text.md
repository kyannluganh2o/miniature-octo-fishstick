<!-- PDF_PAGE: 1 -->

ViewOnline
ExportCitation
RESEARCH ARTICLE |  JULY 20 2012
Breakup and vaporization of droplets under locally
supersonic conditions
YoungJun Kim; James C. Hermanson
Physics of Fluids 24, 076102 (2012)
https://doi.org/10.1063/1.4733459
Articles You May Be Interested In
Temporal properties of secondary drop breakup in the bag-stamen breakup regime
Physics of Fluids (May 2013)
Instability mechanisms of the bag-stamen breakup
Physics of Fluids (February 2026)
Numerical investigations on the deformation and breakup of an n-decane droplet induced by a shock wave
Physics of Fluids (June 2022)
 29 August 2026 09:45:45

<!-- PDF_PAGE: 2 -->

PHYSICS OF FLUIDS 24, 076102 (2012)
Breakup and vaporization of droplets under locally
supersonic conditions
Y oungJun Kima) and James C. Hermanson b)
Department of Aeronautics and Astronautics, University of Washington, Seattle, Washington
98195, USA
(Received 30 April 2012; accepted 19 June 2012; published online 20 July 2012)
The disruption and vaporization of simulated fuel droplets in an accelerating super-
sonic ﬂow was examined experimentally in a draw-down supersonic wind tunnel.
The droplets achieved supersonic velocities relative to the surrounding air to give
relative Mach numbers of up to 1.8 and Weber numbers of up to 300. Mono-disperse,
100 μm-diameter ﬂuid droplets were generated using a droplet-on-demand generator
upstream of the tunnel entrance. Direct close-up single- and multiple-exposure imag-
ing was used to examine the features of droplet breakup and to determine the droplet
velocities. Laser-induced ﬂuorescence (LIF) imaging of the disrupting droplets was
performed using acetone ﬂuorescence to determine the dispersion of the expelled va-
por. Three test liquids were employed: 2-propanol and tetraethylene glycol dimethyl
ether as non-volatile ﬂuids and a 50/50 hexanol-pentane mixture (Hex-Pen 50/50).
The vapor pressure of the Hex-Pen 50/50 was sufﬁciently high to cause the droplet
ﬂuid to potentially become superheated in the decreased static pressure of the super-
sonic stream. The dynamics for 2-propanol and Hex-Pen 50/50 droplets were similar
up to the point of disruption, which occurred more rapidly for the more volatile
Hex-Pen 50/50. A 1D dynamic droplet model was developed to provide a ﬁrst esti-
mate of the expected droplet acceleration and velocity. The actual droplet velocities
were in reasonable agreement with the model up to the point at which signiﬁcant
droplet disruption and mass loss commenced. The droplet deformation and breakup
patterns for these supersonic ﬂow conditions can be classiﬁed into four different ﬂow
regions characterized by changes in the Weber number with downstream distance
as the droplets accelerate, however, those ﬂow regimes and Weber number ranges
were different than those seen for droplets disrupting in shock tubes. The disruption
patterns were seen to be generally similar for the different ﬂuids, though droplet
disruption occurred more rapidly for the more volatile ﬂuid. LIF imaging established
the extent of the dispersion of the expelled vapor. Examination of the vapor clouds
surrounding the droplets suggests that Hex-Pen 50/50 droplets had a greater rate of
vaporization than 2-propanol droplets starting at approximately 2 mm downstream
of the nozzle throat, where the air static pressure became lower than the liquid vapor
pressure. This suggests that droplet superheating can have an effect on the extent
and rate of droplet vaporization under locally supersonic conditions. The degree of
vaporization for Hex-Pen 50/50 was approximately 1.3 times greater than that of
the non-volatile ﬂuids over all downstream distances in the supersonic ﬂow.
C⃝ 2012
American Institute of Physics .[ http://dx.doi.org/10.1063/1.4733459]
I. INTRODUCTION
The breakup and vaporization of liquid droplets in supersonic ﬂow is an interesting research
problem with potentially important implications for supersonic combustion ramjets (scramjets) that
a)Postdoctoral Research Scientist.
b)Professor and Chair.
1070-6631/2012/24(7)/076102/24/$30.00 C⃝ 2012 American Institute of Physics24, 076102-1
 29 August 2026 09:45:45

<!-- PDF_PAGE: 3 -->

076102-2 Y . Kim and J. C. Hermanson Phys. Fluids 24, 076102 (2012)
utilize liquid hydrocarbon fuels. Non-cryogenic, liquid hydrocarbons have substantial beneﬁts as
scramjet fuel,1, 18, 19 including higher energy density, lower cost, and ease of handling compared to
liquid hydrogen fuel. The fuel in scramjets is typically injected in a pre-vaporized state. In a “cold
start” situation, however, some hydrocarbon fuel may be injected while still in liquid phase. In the
situation where some or all of the fuel is injected as liquid, the rates and physical mechanisms
associated with the disruption and vaporization of liquid droplets under supersonic ﬂow conditions
become critical issues to scramjet combustor performance.
The disruption of droplets in high-speed ﬂow has often been studied by the sudden application
of aerodynamic loads though the use of shock tubes.3, 5, 7–9 Though this technique can produce liquid
droplets under locally supersonic conditions, this is accomplished only after the passage of a shock
wave through the droplets, which may differ from the case of liquid fuels injected into scramjets.
Other droplet disruption studies have been conducted at subsonic speeds,
10, 11 for example, by
droplets falling across a high-speed gas jet, 12 droplet-bearing jets in cross ﬂow, 13 and drop tubes. 14
Most of the previous studies have used macroscopic droplet size on the mm to cm scale.
The disruption of droplets due to aerodynamic forces is typically characterized in terms of
the Weber number, We = ρ∞ v2
r di /σ, where ρ∞ is the static density of the air, vr = v∞ − vd the
velocity of air relative to the droplet, di the initial diameter of the droplet, and σ the surface tension
of the liquid. In compressible ﬂow, the discussion also must consider the effects of the Mach number
of the droplet relative to the surrounding supersonic air ﬂow, Mr = (v∞ − vd )/a∞ , where a∞ is the
local speed of sound at the droplet location, on the disruption behavior of the droplets. The evolution
of this relative Mach number would be expected to be fundamentally different for droplets in an
accelerating, supersonic ﬂow compared to the ﬂow conﬁguration in shock tubes.
V arious characterizations of droplet disruption vs. Weber number are available in the literature
for subsonic, and in a few cases supersonic, ﬂow relative to the droplets. A sketch extracted from one
such study of the disruption behavior of droplets for different Weber numbers in impulsively applied
supersonic ﬂow (i.e., a shock tube) is presented in Fig. 1. The most commonly observed droplet
disruption modes are vibrational, bag, piercing, stripping, and catastrophic, depending on the Weber
number.
11, 12 It should be stressed that the actual breakup modes can vary considerably depending
upon experimental method and facility used (for example, shock-tubes versus the direct-injection,
continuously accelerating technique employed in this research), the ﬂow conditions (i.e., compress-
ible versus incompressible ﬂow), and the presence of possible liquid superheating. Establishing the
droplet disruption and vaporization behavior as a function of Weber and Mach numbers number for
the case of droplets moving supersonically relative to an accelerating supersonic ﬂow, in the possible
presence of droplet superheating, is a primary focus of the current work.
One possible technique to increase the dispersion of liquid fuels is to exploit the accelerated va-
porization made possible by superheating the liquid. Investigation of the vaporization of superheated
droplets and sprays have to date been largely conﬁned to incompressible ﬂows,
1, 2 with the physics
of superheated liquid droplet disruption and vaporization in supersonic ﬂow not yet well established.
Previous research16 in supersonic ﬂow has suggested that, for the case of subsonic Mach numbers
relative to droplets, droplet superheating has some impact on the droplet velocity and lifetime due to
the possible superheating effects within the bulk of the droplet due to the decreased static pressure
in supersonic ﬂow. The extent to which this is also the case for droplets at supersonic relative Mach
numbers is not yet clearly established. In one investigation, superheat effects were not reported 17
in droplets at relative Mach numbers as high as 3.4. On the other hand, droplet superheating does
appear to play some role in droplet lifetime at lower Mach relative numbers (up to 1.8). 22 This
points to the need for further study of the effects of ﬂuid superheating on droplet disruption and
vaporization under locally supersonic conditions, which is one focus of the research reported here.
This research investigates the dynamics and disruption behavior of droplets consisting of volatile
and non-volatile ﬂuid accelerated smoothly and continuously to supersonic Mach numbers relative to
the droplets without the passage of shock waves through the droplet. This problem is fundamentally
different from the more commonly studied conﬁguration of droplets in shock tubes, where the rise
in static pressure would not be expected to result in superheating of the bulk liquid within the
droplet. The smooth acceleration in the current study is accomplished over a range of liquid vapor
pressures using a compact, under-expanded supersonic jet formed in a draw-down wind tunnel. The
 29 August 2026 09:45:45

<!-- PDF_PAGE: 4 -->

076102-3 Y . Kim and J. C. Hermanson Phys. Fluids 24, 076102 (2012)
FIG. 1. Droplet breakup mode based on Weber number for non-volatile droplets (from Pilch and Erdman 14).
continuously accelerating droplets studied here allow for the study of features of fuel injection into
a supersonic ﬂow not possible in shock tubes, where the velocity relative to the droplet is relatively
constant.10, 12, 22 Furthermore, the current technique allows for the investigation of potential superheat
effects due to the reduction in static pressure that is not possible in shock tubes due to the static
pressure rise after shock passage. Of speciﬁc interest are the droplet disruption patterns, the droplet
acceleration, the rates of vaporization, and how all of these behaviors might be impacted by the
superheating that can potentially occur when droplets consisting of volatile liquids experience a
decrease in static pressure in the supersonic ﬂow.
II. APPROACH
A. Flow conﬁguration and diagnostics
Tests of liquid droplet disruption were conducted using the under-expanded supersonic jet
conﬁguration shown schematically in Fig. 2. The 2D under-expanded jet was discharged into a
draw-down wind tunnel with 63.5 × 63.5 mm borosilicate glass walls to allow for ﬂow visualization
throughout the contraction, nozzle throat, and test section as shown in Fig. 3. The test section was
connected to a vacuum tank with a volume of 2.8 m 3. The nozzle consisted of a convex convergent
section 15 mm long with 4.8 × 3.9 mm throat area. To prevent premature droplet breakup before
the droplets reach supersonic conditions ( Mr > 1), the Weber number was kept as low as possible
in the subsonic region. To achieve this, the wind tunnel contraction was optimized to produce low
droplet relative velocities in the subsonic section. Schlieren imaging indicated that the Mach disk
was situated approximately 11.2 mm downstream of throat for a back pressure of 16.7 kPa.
 29 August 2026 09:45:45

<!-- PDF_PAGE: 5 -->

076102-4 Y . Kim and J. C. Hermanson Phys. Fluids 24, 076102 (2012)
FIG. 2. Schematic diagram of droplet injection and acceleration process using an under-expanded jet.
Flow conditions on the tunnel centerline were determined by wall static pressure measurements
and a pitot probe inserted from the bottom of the tunnel, which together gave an uncertainty in the
measured ﬂow velocity of approximately 5%. The air ﬂow reached a measured Mach number of
Mair = 2.3 near the location of the Mach disk (all droplets were completely disrupted and vaporized
upstream of that location). A 3D computational ﬂuid dynamics (CFD) analysis Fluent25 of the air
ﬂow in this conﬁguration indicated that the air ﬂow properties was essentially uniform (to within
5%) over a distance approximately 1.5 mm from the centerline in both the x and y directions. The
issues of ﬂow uniformity are discussed in Sec. IV in greater detail.
B. Droplet generation and size
A MicroFab piezoelectric droplet-on-demand generator with a MicroJet III controller gener-
ated mono-disperse 100 ± 5 μm diameter droplets of each test ﬂuid at nominal frequencies of
3300 Hz. This droplet size resulted in a sufﬁciently low Weber number in the subsonic region of
the wind tunnel to prevent early droplet breakup. At the same time, the droplets were sufﬁciently
large to effectively “lag” the ﬂow and to reach supersonic relative velocities in supersonic ﬂow
that occurred in the under-expanded jet test section. The droplet “lag” can be characterized by the
FIG. 3. 2D supersonic wind tunnel conﬁguration (dimensions in mm) and coordinate system.
 29 August 2026 09:45:45

<!-- PDF_PAGE: 6 -->

076102-5 Y . Kim and J. C. Hermanson Phys. Fluids 24, 076102 (2012)
FIG. 4. Mono-disperse droplets at injection.
Stokes number, St = τ· U
D , where τ is the momentum response time, U is the ﬂow velocity, and D
is a characteristic dimension. 23, 24 The characteristic momentum response time, τ, was determined
by integrating the equation of motion using Stokes-law drag for a spherical particle in a gas. The
Stokes number for a droplet size 100 μm in the supersonic ﬂow of this work was approximately
49–86 in the test section downstream of the throat. A Stokes number much greater than unity
(St ≫ 1) is consistent with the signiﬁcant droplet “lag” that leads to the desired supersonic ﬂow
relative to the droplets.
The droplet separation distances at injection were typically approximately three droplet diam-
eters as shown in Fig. 4, which also conﬁrms that the droplets were initially spherical. The chosen
droplet injection frequency did not result in droplet-droplet interaction due to the signiﬁcant acceler-
ation that accompanies the droplet injection into the supersonic ﬂow. The droplet generator tip was
positioned 5 mm above the entrance of the convergent nozzle entrance, and was aligned with 3-axis
micro-stagers to ensure that the droplets were injected on the tunnel centerline.
C. Test ﬂuids and droplet superheating
The properties of the test liquids employed here are summarized in Table I. 2-propanol
and tetraethylene glycol dimethyl ether (TGDE), both of which have low vapor pressures
(P
vapor < 10 kPa), served as non-volatile, control liquids. For the case of a more volatile liquid,
the static air pressure for supersonic conditions can become signiﬁcantly lower than the vapor pres-
sure of the droplet, with the potential to give rise to superheating effects not present for the case
of the nonvolatile liquids.
6 A hexanol/n-pentane 50%–50% mixture by volume (denoted here as
Hex-Pen 50/50) was formulated to serve as a volatile ﬂuid ( Pvapor = 30.7 kPa) while approximately
matching the mechanical properties of the non-volatile 2-propanol. The higher vapor pressure of
Hex-Pen 50/50 exceeds the minimum static pressure in the supersonic ﬂow, as shown in Fig. 5.I ti s
challenging to identify test liquids with different vapor pressures that keep other, key ﬂuid properties
similar. The effectiveness in matching the mechanical properties can be characterized in terms of the
TABLE I. Test liquid properties (temperature: 294 K).
Test liquid P vapor (kPa) m (g/mol) ρ (kg/m3) μ (Pa s) α (m2/s) σ (N/m) Oh
TGDE 0.0013 222.27 1384.66 0.003939 5.687 × 10− 8 0.0339 0.0575
2-propanol 4.404 60.10 785.16 0.002311 6.726 × 10− 8 0.0213 0.0565
Hexanol-pentane 50/50 30.67 86.52 781.08 0.001345 7.245 × 10− 8 0.0209 0.0333
Hexanol 0.067 102.18 818.96 0.005191 7.837 × 10− 8 0.0262 0.1120
Pentane 58.77 72.15 625.33 0.000232 7.943 × 10− 8 0.0159 0.0074
 29 August 2026 09:45:45

<!-- PDF_PAGE: 7 -->

076102-6 Y . Kim and J. C. Hermanson Phys. Fluids 24, 076102 (2012)
FIG. 5. Static pressures along the tunnel centerline with vapor pressures of the test liquids shown for reference. The nominal
back pressure was 16.7 kPa.
Ohnesorge number, Oh = μ/(ρσ di)1/2. The values of Ohnesorge number for the ﬂuids considered
here are included in Table I. For all test liquids employed here Oh < 0.1, under which conditions
the effect of viscosity on droplet disruption has been seen to be negligible. 8
The droplet ﬂuids were not heated prior to their injection into the supersonic ﬂow. The calculated
maximum Fourier number of the droplets was Fo = 4αt/d2
i ≈ 0.027 for the test ﬂuids, where α is
the thermal diffusivity and t is the total time for which droplets were subjected to static temperatures
in the contraction at least 1 K below ambient and in the under-expanded jet up to the Mach disk.
The low value of the Fourier number suggests that while there may be some cooling very near the
droplet surface, cooling of the bulk droplet ﬂuid was negligible in the supersonic ﬂow owing to the
very short droplet lifetimes. It has been suggested that, in fact, the liquid temperature can increase
due to the viscous heating resulting from rapid droplet deformation in high-speed ﬂow.
6, 17
D. Imaging systems
Droplets were imaged in the test section using direct close-up imaging, double-exposure imag-
ing, and laser-induced ﬂuorescence (LIF). Illumination for the direct imaging was provided by a
Xenon Corporation N-787B nano-pulse system generating 500 mJ pulses of 10 ns duration. During
each light pulse a droplet or droplet fragment moved a maximum of approximately 2% of the initial
droplet diameter of 100 μm; thus the droplets were effectively “frozen” at a given position and state
of deformation and fragmentation. Images were captured with a Princeton Instruments PI Max 2
ICCD camera coupled with a VZM 300 video microscope lens shown in Fig. 6. One challenge is
capturing close-up images of disrupting droplets as they move at high speed through the imaging
volume. This was accomplished by detecting droplets as they passed through a helium-neon laser
beam incident on a photodiode.
20 The output signal from the photodiode was then conditioned into
a standard 5V TTL signal and used to trigger the PI MAX2 camera after a suitable delay time. Upon
receiving this trigger signal, the PI MAX2 camera controller initiated the exposure by opening the
electronic shutter (gates open). The controller then sent a trigger signal to the nano-pulse system to
produce a 10 ns light pulse to illuminate the detected droplet. The camera controller subsequently
terminated the exposure (gates closed). The image was then recorded on a PC for post-processing
to account for interlacing, CCD array defects, background signal, imperfections in the window and
optics, and to increase image contrast. The camera was repositioned at various locations along the
 29 August 2026 09:45:45

<!-- PDF_PAGE: 8 -->

076102-7 Y . Kim and J. C. Hermanson Phys. Fluids 24, 076102 (2012)
FIG. 6. Direct imaging system layout schematic (top view of test section shown).
length of the test section to capture images of droplets from the point of their injection into supersonic
ﬂow to the location where complete disruption occurred.
Studies to date of droplet dynamics in high-speed ﬂow have largely relied on some form of
high-speed imaging to measure drop displacement vs. time. 15 Double-exposure imaging with a
continuous light source were employed in this work for this purpose. Illumination was provided by
Oriel 68806 arc-lamp. The PI MAX2 camera allowed for double-exposure images to be captured
by an electronic shuttering technique called gating; in this work a typical gate delay of /Delta1t ≈ 12 μs
was employed, representing the time between two exposures on a single image frame in Fig. 7.T h e
droplet velocities were determined directly from the measured droplet displacement and the pulse
separation time, i.e., Vd = /Delta1z//Delta1t. The technique resulted in calculated velocities with an estimated
error of approximately 2%.
The characteristics of the vapor cloud surrounding the disrupting droplets were examined
using LIF as shown in Fig. 8. The ﬂuorescent seed was acetone, blended with each test ﬂuid
at a concentration of 5% by volume. 25, 26 The laser-induced ﬂuorescence technique allowed the
determination of the distribution of the vapor concentration surrounding a droplet at each stage of
FIG. 7. Measurement of droplet displacement via double-exposure imaging.
 29 August 2026 09:45:45

<!-- PDF_PAGE: 9 -->

076102-8 Y . Kim and J. C. Hermanson Phys. Fluids 24, 076102 (2012)
Camera
Nd:YAG laser at 266 nm 
with 10 Hz
UV ﬁlter
Mirror
Beam 
stopper
Test 
sec/g415on
Lenses
aperture
Controller
Nd:YAG laser at 266 nm
with 10 Hz
Nd:YAG Laser 
(266 nm at 10Hz) 
FIG. 8. LIF Imaging and optical layout. Photograph of setup (top) and schematic layout diagram (bottom).
droplet breakup in supersonic ﬂow. Due to the very violent and rapid droplet disruption that occurs
in supersonic ﬂow, the acetone tracer was expected to provide a reasonable indication of the total
amount and extent of the vaporized ﬂuid.23 Laser illumination for the LIF visualization was generated
using the fourth harmonic of a pulsed Nd:Y AG laser (266 nm) at a pulse frequency of 10 Hz and
with a pulse energy of approximately 60 mJ/pulse. The laser beam was formed into a relatively
thick sheet approximately 20 mm high and 1 mm wide. This beam thickness contrasted with the
thinner laser sheets normally employed in planar laser-induced ﬂuorescence (PLIF) imaging – the
much larger laser-light volume employed here being sufﬁciently large to facilitate droplet capture
and to ensure the illumination of the entire vapor cloud surrounding each disrupting droplet.
28–31 LIF
imaging was performed in the supersonic regions of the ﬂow (the contraction blocks prevented LIF
imaging in the subsonic regions of the ﬂow). The laser was synchronized with the PI MAX2 camera
in the same way as that used for the nano-pulse light source. To capture only the ﬂuorescence signal
of interest and eliminate spurious 266 nm laser light within the wind tunnel, a UV ﬁlter ahead of
the camera passed all light except in the range of 150–300 nm. Image processing was employed for
background subtraction and to correct for variations in the laser intensity within the imaging volume
to determine the contours of the vapor concentration. Calibration LIF images performed using a
laminar, subsonic jet with known acetone concentration allowed for the estimation of the acetone
vapor concentration in the vicinity of the disrupting droplets.
23
III. DROPLET DYNAMIC MODEL
A simple, 1D computational model was developed to give a ﬁrst estimate of the expected trends
in droplet velocities and acceleration along the centerline of the tunnel and the corresponding droplet
relative Mach and Weber numbers. This dynamic model, by comparison with experiments, facilitated
the assessment of the effects of droplet disruption and vaporization on the droplet dynamics. The
 29 August 2026 09:45:45

<!-- PDF_PAGE: 10 -->

076102-9 Y . Kim and J. C. Hermanson Phys. Fluids 24, 076102 (2012)
modeling domain encompassed a region beginning at the contraction inlet, and ending upstream of
the Mach disk. In both subsonic and supersonic air ﬂow regimes, stagnation quantities were taken to
be equal to those of the laboratory atmospheric conditions, neglecting any viscous or shock losses.
Modeling of the subsonic air ﬂow ﬁeld was treated separately from the modeling of the super-
sonic, under-expanded jet. Predictions of the droplet dynamic model for the subsonic region of the
air ﬂow were based on isentropic ﬂow of air through a contraction with subsonic stagnation losses
assumed to be minimal (the stagnation pressure losses at the throat are on the order of 3%–5% of
the inlet stagnation pressure, as determined by pitot probe measurements).
Supersonic air ﬂow predictions along the tunnel centerline to support the simple, 1D dynamic
model, were made via the standard method of characteristics for 2D planar ﬂow.
23 The supersonic,
under-expanded jet was taken to emerge unconstrained into a chamber of quiescent air with constant
nominal backpressure of 16.7 kPa everywhere outside of the jet. A MA TLAB code developed for
this purpose predicted a shape for the under-expanded jet that agreed well with observations made
of the jet using schlieren photography.
The droplet dynamic model neglected any transverse droplet acceleration due to ﬂow turbulence
and took the droplet acceleration to be affected primarily by drag in the air ﬂow direction from the
smoothly accelerating subsonic and supersonic ﬂow. Double exposure images conﬁrmed that the
droplet velocity transverse to the air ﬂow was minimal in comparison to velocity in the air ﬂow
direction (less than 5%).
Utilizing theoretical air ﬂow properties calculated using the aforementioned method, the
idealized droplet velocity and position through the tunnel were calculated in one dimension via inte-
gration of the equations of motion by using assumed drag coefﬁcients. The drag coefﬁcient data for
solid spheres, C
Dsp, for Reynolds numbers similar to those expected for this experiment as reported
by Bailey and Hiatt21 were employed as a baseline in the dynamic droplet model. Such a rigid-sphere
approach does not consider deformation or mass loss due to droplet disruption and vaporization.
The solid sphere drag data can, in principle, be corrected by empirical correlations to account
for mass loss and droplet shape changes occurring during breakup. Those corrections, however,
have generally been developed for situations in which droplets breakup under essentially constant
supersonic velocities, such as those induced by shock tubes. In the current research it was possible,
using the droplet imaging employed, to get an estimate for the change in the droplet cross-sectional
area based on the observed change in droplet diameter during the early stages of droplet deformation.
The visual imaging was useful for this purpose up to a downstream distance of approximately
z =+ 2 mm, by which point the ratio of the deformed droplet diameter to the initial value, d/d
0
increased to approximately 1.8. Downstream of that location, the droplet fragmentation no longer
allowed an effective estimate of droplet cross sectional area; in this case the modeled droplet area
was taken to be the value at z =+ 2 mm.
The drag force was calculated via Eq. (1), which is based upon theoretical free stream air
properties, relative velocity, ν∞ − νd, and the droplet cross sectional area Ad,
FD = 1
2ρ∞ v2
r Ad CDsp = 1
2ρ∞ Ad CDsp (v∞ − vd )2. (1)
Using Newton’s law, Eq. (1) can be reformulated to solve for droplet acceleration as
z1 = z
z2 = ˙z
[ ˙z1
˙z2
]
=
⎡
⎣
z2
1
2
ρ∞ Ad CDsp
ρd Vd
(v∞ (z1) − z2)2 + g
⎤
⎦ . (2)
Numerical time integration of the droplet acceleration for the spherical, solid-sphere case was
achieved by a ﬁrst order Euler’s method code written in MA TLAB. Comparisons of these simpliﬁed
model results, which include the droplet velocity and position versus time, the Weber and Mach
numbers, and the static pressure, can be made with direct measurements of droplet velocities and air
ﬂow characteristics.
 29 August 2026 09:45:45

<!-- PDF_PAGE: 11 -->

076102-10 Y . Kim and J. C. Hermanson Phys. Fluids 24, 076102 (2012)
(b)(a)
z, Distance from throat [mm]
Mach number
-12 -10 -8 -6 -4 -2 0 2 4 6 8 10 120
0.5
1
1.5
2
2.5
3
x=- 2m m
x=- 1m m
x=0m m
x=1m m
x=2m m
z, Distance from throat [mm]
Mach number
-12 -10 -8 -6 -4 -2 0 2 4 6 8 10 120
0.5
1
1.5
2
2.5
3
y=0m m
y=0 . 5m m
y=1m m
y=1 . 5m m
y=2m m
y=2 . 2m m
FIG. 9. (a) Air ﬂow Mach number as a function of z at different x-locations (b) Air ﬂow Mach number as a function of z at
different y-locations.
IV. FLOW UNIFORMITY
The droplets in this ﬂow conﬁguration ideally travel exactly along the wind tunnel centerline.
However, the trajectory of a given droplet may be perturbed slightly off-center due to the injection
technique and the existence of turbulence in the incoming ﬂow. Therefore, it was important to
ascertain the deviation of the ﬂow conditions from those on the centerline, to establish the area over
which the ﬂow can be approximated as being uniform. ANSYS FLUENT was employed to solve
this compressible ﬂow problem in all three dimensions using a ﬁnite volume method.
23 FLUENT
was employed to model the air ﬂow only. In order to investigate the ﬂow ﬁeld near the centerline,
the Mach number distribution was obtained from the ANSYS 3D CFD simulation in different cross
sections (where the coordinates x = spanwise; y = out of plane; and z = downstream indicate the
principal directions).
The Mach number is shown as a function of z and x for y = 0i nF i g .9(a). It can be seen that, for
a given downstream location z, the Mach numbers were similar up to x =± 1 mm off of center with
less than 5% deviation. Therefore, the ﬂow can be considered to effectively be uniform inx-direction
within this range of x =± 1 mm from the centerline. Similarly, the Mach number uniformity in
the y direction for x = 0 is shown in Fig. 9(b). It is seen that the Mach number was similar up to
y = 1.5 mm, indicating that the region over which the approximation uniform ﬂow is valid in
the y-direction up to y =± 1.5. From these observations, it can be concluded that the ﬂow can
be approximated as being essentially uniform in both the transverse x and y directions near the
centerline (speciﬁcally, within y < ±1.5 and x < ±1). All droplets considered here were within this
region.
V. RESULTS AND DISCUSSION
A. Droplet dynamics and disruption
The measured absolute droplet velocities (i.e., relative to lab-ﬁxed coordinates) using the double-
exposure imaging technique are shown in Fig. 10(a) for all three test ﬂuids. All droplets entered the
tunnel inlet under subsonic conditions at a measured velocity of 6.5 m/s at the location z =− 16 mm.
The droplet velocities increased to approximately 55 m/s at the nozzle throat for 2-propanol and
Hex-Pen 50/50 and 40 m/s for TGDE droplets, respectively. TGDE droplets had lower acceleration
and lower velocity largely due to the higher density of that ﬂuid compared to 2-propanol and Hex-Pen
 29 August 2026 09:45:45

<!-- PDF_PAGE: 12 -->

076102-11 Y . Kim and J. C. Hermanson Phys. Fluids 24, 076102 (2012)
(a) (b)
z, Distance from throat [mm]
Vdroplet [m/s]
-8 -6 -4 -2 0 2 4 6 80
20
40
60
80
100
120
140
160
180
200
2-propanol
Hex-Pen 50/50
TGDE
2-propanol - model
Hex-Pen 50/50 - model
TGDE - model
z, Distance from throat [mm]
Mach number
-8 -6 -4 -2 0 2 4 6 80
0.5
1
1.5
2
2.5
3
Mair-experiment
Mrel-2-propanol (model)
Mrel-Hex-Pen 50/50 (model)
Mrel-TGDE (model)
Mrel-2-propanol
Mrel-Hex-Pen 50/50
Mrel-TGDE
FIG. 10. (a) Measured absolute (lab-ﬁxed coordinates) droplet velocities and (b) relative Mach number in supersonic
ﬂow. The dashed lines correspond to the droplet dynamic model; the solid line in (b) represents the measured air Mach
number.
50/50. The droplet velocity reached a value as high as 135 m/s, 105 m/s, and 100 m/s for 2-propanol,
Hex-Pen 50/50 and TGDE, respectively, before complete breakup occurred. The droplet dynamics
up to the point of droplet disruption appeared to be similar for the 2-propanol and Hex-Pen 50/50,
which might be expected given that the ﬂuid properties were speciﬁcally selected to be similar. The
more volatile Hex-Pen 50/50 droplets, however, exhibit a shorter droplet lifetime due presumably
to more rapid vaporization expected to commence at approximately z = 2 mm, where superheating
may have started, as suggested by Fig. 5. The non-volatile TGDE droplets had similar dynamics
to that of 2-propanol showing a similar trend, but with somewhat lower values of velocity. The
droplet accelerations were of the order of 10
5 m/s2; such high levels of droplet acceleration have
been observed previously in compressible ﬂow. 5–7
The droplet dynamic model, corrected to take into account the observed deformed droplet di-
ameter, predicts that the droplet velocity at the throat for 2-propanol and Hex-Pen 50/50 would
be approximately 55 m/s and gradually increase to approximately 90 m/s at the point where
droplets have completely disrupted and vaporized. The model follows the same trend as the
experimental velocity measurements, as seen in Fig. 10(a), but indicates a value at the throat
(z = 0) that is approximately 5% lower. At a downstream distance of z = 6 mm the model droplet
velocity is roughly 11% lower than the observed values, given that the droplet signiﬁcant distor-
tion/disruption, as well as mass loss, by that point was expected. It should be noted that although
the simpliﬁed dynamic model takes into account the expected change in droplet drag due to defor-
mation, it does not consider droplet breakup and fragmentation, and the associated mass loss due to
evaporation.
During the initial droplet deformation the reasonable agreement between the simple dynamic
model and the actual droplet velocities suggests that the drag is impacted primarily by the change
in the cross-sectional area of droplet, combined with the changes in the ﬂow conditions. Further
downstream, the droplet drag, however, appears to be affected by a combination of the cross-sectional
area change due to the deformation, plus mass shedding due to the disruption. Beyond a downstream
distance of approximately z =+ 2 mm, the droplet cross-sectional area increases beyond that which
can be measured by the visual imaging. This further increase in droplet cross section would be
expected to contribute to a higher droplet drag and more rapid acceleration, consistent with the
observed deviation of the measured velocities from those predicted by the simple dynamic model.
The scatter in the supersonic droplet velocity data shown in Fig. 10(a) is believed to be primarily
due to the ﬂuctuations in droplet locations relative to the wind tunnel centerline.
 29 August 2026 09:45:45

<!-- PDF_PAGE: 13 -->

076102-12 Y . Kim and J. C. Hermanson Phys. Fluids 24, 076102 (2012)
TABLE II. Breakup regions.
Downstream distance, z(mm)
Fluids Region I Region II Region III Region IV
2-propanol − 12 to − 2 − 2t o0 0t o3 3t o6 . 5
TGDE − 12 to − 1.3 − 1 . 3t o0 . 5 0 . 5t o3 . 5 3 . 5t o7 . 3
Hex-Pen 50/50 − 12 to − 2.5 − 2.5 to − 0.5 − 0 . 5t o2 . 7 2 . 7t o4
The Mach numbers relative to the droplet are shown in Fig. 10(b). The Mach number for the air
ﬂow (solid line), Mair, downstream of the throat reached a maximum value of 2.3. The relative Mach
numbers were similar for the all three ﬂuids largely due to the fact that the ﬂow velocity signiﬁcantly
exceeded the droplet velocity, so that the variations in droplet velocity had a relatively small impact
on the relative Mach number. The tunnel is capable of producing a maximum droplet relative Mach
number of approximately 1.8, demonstrating the capability of this under-expanded-jet technique to
produce supersonic velocities relative to the droplet, while avoiding the impulsive loading and shock
passage that occurs in shock tube experiments.
3–5, 8, 10 The droplet dynamic model (dashed lines)
exhibits similar qualitative trends to the experimental results up to the location where all droplet
disruption is complete. The relative velocities determined from these experiments indicate a Weber
number near the nozzle throat of approximately We = 150 for 2-propanol and Hex-Pen 50/50 and
We= 120 for TGDE.
Representative images of 2-propanol and TGDE droplets undergoing deformation and disruption
in supersonic ﬂow are shown in Fig. 11 (additional direct images of disrupting droplets are provided
in the Appendix). The droplets are seen to exhibit aerodynamic breakup, including deformation of
the droplet and the shedding of droplet ﬂuid. Signiﬁcant droplet deformation and disruption generally
occurred downstream of the nozzle throat and well upstream of the Mach disk. Previous research
13, 14
in shock tubes suggests that the values of Weber number seen in this investigation would be expected
to lead to a sheet stripping disruption mode. The stripping, as well as catastrophic, breakup modes
were observed in this investigation. Unlike the bulk of previous droplet-disruption studies, the
ﬂow conditions in the vicinity of the droplet in this work, including the Weber number, change
continuously as the droplet is accelerated into the supersonic ﬂow ﬁeld.
The droplet deformation and breakup patterns for these conditions can evidently be
classiﬁed into four different ﬂow regimes by considering the changes in the Weber number with
downstream distance as the droplet accelerates.
23 Although each case contained some variation
in the patterns of droplet deformation and breakup, it was generally possible to identify a dis-
tinct, most prominent pattern. In Region I (termed “deformation”), droplets in the nozzle entrance
transformed from spherical to semi-ellipsoidal in shape before the actual breakup started. Signif-
icant mass loss commenced in the “initial breakup” seen in Region II, while the droplets showed
semi-ellipsoidal shapes with thin tails on the leeward sides. In Region III, “primary breakup”
was observed with surface undulation and deformation on the windward side and chaotic sheet
stripping on the leeward side of the droplet. The signiﬁcant mass loss in Region III would rea-
sonably be expected to impact the droplet drag/acceleration, as discussed previously and shown
in Fig. 10(a). Finally, Region IV was characterized by “catastrophic breakup” with signiﬁcant
droplet fragmentation. Beyond Region IV , the droplet remnants consisted of either a tenuous
vapor with interspersed smaller droplets or fragments no longer visible using the direct imag-
ing technique. The physical extent of each region varied somewhat for the different test ﬂuids,
reﬂecting the differences in vapor pressure and Weber number. These differences are shown in
Table II.
In the case of Hex-Pen 50/50, superheating may have occurred as the static pressure in the
vicinity of the droplets decreased in the supersonic ﬂow. Consistent with this, the disruption patterns
were observed to be generally similar up to approximately z = 2 mm but the rapid vaporization
caused the Hex-Pen droplets to disappear by approximately z = 4 mm. This suggests that although
superheating can serve to decrease the droplet lifetime, superheating does not appear to impact
 29 August 2026 09:45:45

<!-- PDF_PAGE: 14 -->

076102-13 Y . Kim and J. C. Hermanson Phys. Fluids 24, 076102 (2012)
 
z = -8.75 mm, t = 0.6ms 
 Mr = 0.12, We = 10.5 
 
z = -3.85 mm, t = 0.9ms 
Mr = 0.26, We = 39.6 
 
 z = -1.00 mm, t = 0.98ms 
Mr = 0.51, We = 115.3 
 z = -0.49 mm, t = 0.992ms 
Mr = 0.60, We = 143.8 
 z = 0.57 mm, t = 1.01ms 
Mr = 0.88, We = 217.2 
 z = 2.44 mm, t = 1.03ms 
Mr = 1.45, We = 278.9 
 z = 3.11 mm, t = 1.04ms 
Mr = 1.53, We = 254.9 
 z = 5.05 mm, t = 1.061ms 
Mr = 1.77, We = 197.6 
 
z = -9.37 mm, t = 0.558 ms 
Mr = 0.129, We = 6.87 
 
z = -1.882 mm, t = 1.1 ms 
Mr = 0.407, We = 65 
 
 
 
z = -1.1 mm, t = 1.19 ms 
Mr = 0.486, We = 78 
 
 
 
z = 0.467 mm, t = 1.22 ms 
Mr = 0.805, We = 145 
  
z = 0.978 mm, t = 1.235 ms 
Mr = 1.01, We = 172 
  
z = 2.29 mm, t = 1.26 ms 
Mr = 1.42, We = 203 
 
 
z = 2.62 mm, t = 1.26 ms 
Mr = 1.45, We = 184 
  
z = 4.1 mm, t = 1.282 ms 
Mr = 1.68, We = 160 
FIG. 11. Droplet breakup Regions I-IV for 2-propanol (left) and TGDE (right).
the nature of the instability/deformation/disruption mechanisms. The TGDE droplets displayed
generally similar disruption behaviors as observed for 2-propanol, with the exception that the
ﬁnal disruption phases (Regions III and IV) occurred over somewhat larger ranges of downstream
distance,
23 consistent with the relatively lower values of Weber number in that case.
The droplet Weber numbers for 2-propanol and Hex-Pen 50/50 of 115 and TGDE are 78 at the
location where initial droplet breakup occurs at approximately z =− 1 mm, as seen in Fig. 12. These
values of Weber number would be expected near the transition from bag-and-stamen breakup to
sheet stripping in shock tube experiments; 11 sheet stripping appears to occur under these conditions
in the current study, as seen in Fig. 11. The highest Weber number is approximately 316 at a location
approximately 2 mm downstream of the throat in the supersonic region. The TGDE droplets showed
a similar trend in Weber number that of 2-propanol and Hex-Pen 50/50 droplets, but with somewhat
lower values due to its higher surface tension. The Weber number for all ﬂuids then decreases due to
the rapid decrease in static air density; this decrease continues until the droplet breaks up completely
and vaporizes.
The average droplet time-of-ﬂight to droplet disruption can be readily determined from the
variation in the average droplet velocity with downstream distance. The droplet breakup time from
the start of Region II to the end of Region IV was found to be approximately 86, 67, and 123 μsf o r
 29 August 2026 09:45:45

<!-- PDF_PAGE: 15 -->

076102-14 Y . Kim and J. C. Hermanson Phys. Fluids 24, 076102 (2012)
z, Distance from throat [mm]
Weber number
-8 -6 -4 -2 0 2 4 6 80
50
100
150
200
250
300
350
400
2-propanol
Hex-Pen 50/50
TGDE
FIG. 12. V ariation in Weber number with downstream distance.
2-propanol, Hex-Pen 50/50 and TGDE, respectively, as shown in Fig. 13. The Weber numbers for
the three liquids varied from 115 to 316. Pilch and Erdman 14 correlated the Weber number with the
droplet breakup time in shock tubes in terms of the “initiation of breakup” and “total breakup.” In
order to compare the breakup times seen in shock tube experiments to those seen in the continuously
accelerating ﬂow of the current work, the correlation given in Eq. (3) was used. Here, the reference
Weber number was taken to be the value at which droplet breakup commenced (roughly 1 mm
t[
[
 s]
z, Distance from throat [mm]
10
1
10
2
10
3
10
4-14
-12
-10
-8
-6
-4
-2
0
2
4
6
8
10
2-propanol
Hex-Pen 50/50
TGDE
 tb = 123 μs 
tb = 67 μs 
t
btb = 86 μs 
FIG. 13. Droplet breakup time ( tb) for three test liquids. Each time difference is referenced to the observed beginning of
droplet breakup in Region II.
 29 August 2026 09:45:45

<!-- PDF_PAGE: 16 -->

076102-15 Y . Kim and J. C. Hermanson Phys. Fluids 24, 076102 (2012)
upstream of the throat),
t = di
vd
ρd
ρ∞
[
14.1(We − 12)0.25 − 2
]
for 45 ≤ We ≤ 351. (3)
The breakup time indicated in Eq. (3) is the difference between the time to total breakup (as
seen in Region IV) and the initiation of breakup (consistent with the initial breakup observed in
Region II).14 The correlation suggests a breakup time of 770μs for a Weber number of 115. This time
is an order of magnitude larger than the disruption time seen for the continuously accelerating ﬂow
of this experiment, where the Weber number continuously and rapidly increases with downstream
distance.
Historically, the mode of droplet breakup has been characterized by the Weber number for the
case where the ﬂow velocity is relatively constant over the lifetime of a droplet (such as is the case in
shock-tube studies). The breakup modes have been described as “pulling” (by viscous drag), “bag”
(by Rayleigh-Taylor instability), and “stripping” (by shear) according to their corresponding Weber
number range,
6–8, 13–15, 20 as depicted, for example, in Fig. 1. Although the continuously accelerating
air ﬂow in this work is fundamentally different than the constant-velocity cases frequently reported
in the literature,
13, 14 sheet-stripping, pulling and catastrophic modes of droplet disruption are still
observed. The disruption due to sheet-stripping and pulling appears to precede the signiﬁcant
deformation of the windward surface of the droplet.
The Weber numbers at which these various disruption modes occur are, however, generally
higher than those reported previously in shock-tube experiments where the Weber numbers are
approximately constant. 6–8, 13–15 This is especially apparent for the “pulling” mode, which Theo-
fanous et al. 33 suggest occurs for Weber numbers less than approximately 26, but are seen to be
present in the current investigation at Weber numbers as high as 200. That the Weber numbers
observed here to be associated with each disruption mode are somewhat different than those re-
ported previously is not unexpected, given that the Weber number experienced by the droplets in
these experiments continuously changes with downstream distance and is therefore not constant in
time, in contrast to shock tube studies where the ﬂow velocity following the shock wave is nearly
constant.
The inertial stability of droplets under conditions of high acceleration can be characterized
in terms of the Bond number, Bo = ρ a
d ri2/σ, where ad is the droplet acceleration and ri the
initial droplet radius. The Bond numbers for the droplets in this investigation ( di = 100 μm) were
approximately Bo = 50 for both 2-propanol and Hex-Pen 50/50 and Bo = 40 for TGDE at the
nozzle throat. These values of Bond number are expected to be too low to result in droplet shattering
due to inertial instability (Rayleigh-Taylor instability) at the windward front surface. The growth
of the unstable modes due to the inertial instability is rather small compared with the aerodynamic
deformation until the Bond number reaches the rather large value of approximately 10
5.32 This
suggests that inertial instability does not play a signiﬁcant role in the deformation and disruption of
the droplets under conditions of this investigation, pointing instead to aero deformation and shedding
of droplet ﬂuid as the primary disruption mechanisms in this case.
B. Droplet vaporization
Sample acquired LIF images of undisrupted droplets, and the corresponding images following
background subtraction, ﬁltering, normalization, laser calibration, and vapor contours are shown
in Fig. 14. Representative LIF images of disrupting 2-propanol and Hex-Pen 50/50 droplets are
shown in Fig. 15 (additional LIF images are shown in the Appendix) for several downstream
distances. These representative results correspond to each of the four breakup regions described
above. 2-propanol images are on the left of Fig. 15; Hex-Pen 50/50, on the right. Three contours
of estimated acetone vapor concentration, C = 0.8 × 10
− 5 mol/cc, 1.6 × 10− 5 mol/cc, and 2.6
× 10− 5 mol/cc, are overlaid in the ﬁgures. The measured vapor ﬂuorescence intensities shown
in Fig. 15 were normalized by the peak recorded intensity for all images. These results al-
low for comparison of the relative vapor concentration distributions between the 2-propanol and
 29 August 2026 09:45:45

<!-- PDF_PAGE: 17 -->

076102-16 Y . Kim and J. C. Hermanson Phys. Fluids 24, 076102 (2012)
FIG. 14. LIF images of undisrupted (top pair) and supersonically disrupted droplets (bottom pair). (Left) Acquired images;
(right) processed images. The white contours, from outermost to innermost, correspond, respectively, to the reference vapor
concentrations of 0.8 × 10
5,1 . 6× 105, and 2.6 × 105 mol/cc.
Hex-Pen 50/50 droplets. The absolute concentrations above correspond directly to the calibration
sample, but may not correspond exactly to the actual absolute concentration of expelled vapor
from each of the two test liquids due to the limitations associated with the calibration tech-
nique. Nonetheless, a direct, quantitative comparison between the degrees of vaporization asso-
ciated with the two different ﬂuids is realizable here because all ﬂow and imaging conditions
(experiment setup, acetone concentration, laser illumination, camera, and optics) for 2-propanol
and Hex-Pen 50/50 were kept identical between the two cases.
27 All vapor-concentration contours
rendered were sufﬁciently removed from the surface of the disrupting droplet to ensure that es-
sentially only vapor was imaged in each case. To extract a general trend in the fashion in which
droplet vaporization occurs, a statistical sample of 80 droplet LIF images was taken in order to
take into account the droplet-to-droplet variations in the shape and extent of the imaged vapor
clouds.
The similarity in the ﬂuorescence intensity ﬁeld images in Fig. 15 (z < 2.5 mm) suggests that
the superheating was not present, to any signiﬁcant extent, in either the 2-propanol or Hex-Pen 50/50
droplets in that region. For either liquid, inside the apparent droplet liquid boundary the mass of
liquid appears consolidated in a single continuous drop and not fragmenting to any great degree. By
contrast, there is evidently a difference in the degree of vaporization for the Hex-Pen 50/50 droplets
compared to 2-propanol farther downstream, as seen in the intensity ﬁeld images shown in Fig. 15
(z > 2.5 mm). These results suggest an effect of superheating on the more volatile Hex-Pen 50/50
droplet, which exhibits a vapor cloud somewhat different in structure and extent than seen for 2-
propanol. Note that the non-volatile, 2-propanol liquid was not superheated at this location because
the vapor pressure of the injected liquid was still below the static pressure of the surrounding air,
resulting in the boundary of the mass of the droplet liquid being relatively distinct. On the other
hand, for the Hex-Pen 50/50 droplets, the liquid mass was no longer consistently lumped in a drop-
like shape at that location, but shows clear signs of enhanced fragmentation as seen in Fig. 15 for
z > 2.5 mm, which would also be consistent with the effects of droplet superheating. All of this
 29 August 2026 09:45:45

<!-- PDF_PAGE: 18 -->

076102-17 Y . Kim and J. C. Hermanson Phys. Fluids 24, 076102 (2012)
   0 < z < 1.3 mm  
    1.3 < z < 2.5 mm  
    2.5 < z < 3.8 mm  
     3.8 < z < 5.1 mm
m
m
FIG. 15. Representative LIF images: 2-propanol (left) and Hex-Pen 50/50 (right). The white contours, from outermost to
innermost, correspond, respectively, to the reference vapor concentrations of 0.8 × 105,1 . 6× 105, and 2.6 × 105 mol/cc.
is consistent with the more rapid disruption of the Hex-Pen 50/50 droplets compared to those of
2-propanol, as discussed previously.
The Hex-Pen 50/50 droplets consistently showed larger vapor cloud areas than 2-propanol
droplets for all concentration contour levels and at all downstream locations. In general, the Hex-
Pen 50/50 droplets also exhibited a larger number of detached vapor fragments from the main
cloud. Based on these LIF images, the more volatile Hex-Pen 50/50 appears to have had a higher
vaporization rate than 2-propanol at all downstream locations in this supersonic ﬂow, suggesting
 29 August 2026 09:45:45

<!-- PDF_PAGE: 19 -->

076102-18 Y . Kim and J. C. Hermanson Phys. Fluids 24, 076102 (2012)
(a) (b)
z, Distance from throat [mm]
A, Vapor area [mm
2
]
0 1 2 3 4 5 6 7 8 9 10 11 120
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.8e-5 mol/cc
1.6e-5 mol/cc
2.6e-5 mol/cc
z, Distance from throat [mm]
A,V apor area [mm
2
]
0 1 2 3 4 5 6 7 80
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.8e-5 mol/cc
1.6e-5 mol/cc
2.6e-5 mol/cc
FIG. 16. V apor contour area for (a) 2-propanol and (b) Hex-Pen 50/50.
that droplet superheating does play some role in accelerating the vaporization of supersonic droplets
under these conditions.
At peak Weber numbers corresponding to those in this investigation, droplets in shock tubes
generally undergo sheet stripping breakup characterized by surface liquid mass being sheared
off by surrounding air ﬂow. This phenomenon did not appear to be dominant for the Hex-Pen
50/50 droplets. Instead, the fragmentation in the presence of possible superheating seen in Fig. 15
(z > 2.5 mm) might be better described as a shattering phenomenon normally seen only in Weber
number regimes above 350.
14 It is concluded that superheating of the liquid contributes to the
increase in droplet vaporization rate as the location at which the apparent signiﬁcant increase in
the size of the vapor cloud surrounding the droplet is ﬁrst noted roughly corresponds to the point
at which the vapor pressure of the liquid exceeds the static pressure of the surrounding air.
The impact of droplet superheating on the vaporization rate can be assessed by considering
the area enclosed by each of the three selected vapor concentration contours plotted versus the
downstream distance in Fig. 16(a) for 2-propanol and Fig. 16(b) for Hex-Pen 50/50 droplets, respec-
tively. The data scatter in each ﬁgure reﬂects the droplet-to-droplet variation in the individual vapor
concentrations of interest. Also shown in the ﬁgures are second-order polynomial curve ﬁts applied
to the measured contour areas. Comparison of these curve ﬁts suggests that the vaporization rate of
the Hex-Pen 50/50 droplets exceeds that of the 2-propanol droplets by a factor of approximately 1.3
over all downstream distances in this supersonic ﬂow.
The observation of accelerated droplet vaporization suggests a possible effect of droplet su-
perheating that is different than reported previously,
17 where no apparent superheating effect was
apparent for volatile droplets injected into an under-expanded supersonic jet at higher relative Mach
numbers than those of the current work. The different conclusions may be partially explained by
recognizing the differences between both the ﬂow conditions and the test liquids employed in those
previous experiments versus those of the current work. The ﬂow conditions employed in the pre-
vious experiment resulted in considerably higher droplet relative Mach numbers (up to M
r = 3.5),
which would be expected to result in a signiﬁcantly higher static pressure rise behind the bow shock
that presumably resides upstream of the supersonic droplets than for the conditions reported here
(Mr up to 1.7). The peak pressure rise P2/P1, across the bow shock on the droplet centerline was
approximately 10–15 for that previous study, which is almost 5 times higher than the expected static
pressure rise in current work ( P
2/P1 = 3.2). Therefore, the static pressure experienced in the imme-
diate vicinity of the droplet was likely higher in those experiments than in the current study, which
may have led to a partial or complete suppression of any droplet superheating effects. In addition,
 29 August 2026 09:45:45

<!-- PDF_PAGE: 20 -->

076102-19 Y . Kim and J. C. Hermanson Phys. Fluids 24, 076102 (2012)
the test liquids employed in the previous research were ethanol, 1-propanol and hexanol, all of which
have lower vapor pressures than Hex-Pen 50/50 employed in this work. In summary, the combination
of an expected lower static pressure rise across the bow shock at the lower relative Mach numbers
of the current study, combined with the use of a test liquid with higher vapor pressure, appear to
at least partially account for the effects of liquid superheating on droplet vaporization observed
here.
VI. SUMMARY
1. A draw-down supersonic wind tunnel was constructed with an optimal contraction proﬁle to
create droplets at supersonic relative Mach numbers (Mr > 1) within a rapidly and continuously
accelerating air ﬂow. The optimal wind tunnel contour suppresses early droplet breakup by
maintaining a low Weber number in the subsonic section.
2. Droplet disruption and vaporization patterns were captured using a close-up direct and laser-
induced ﬂuorescence imaging system. The velocities of droplets were measured via a multiple
exposure imaging technique. Any effects of superheat appeared to have a minor effect on droplet
dynamics, in that volatile droplets had similar velocity and acceleration proﬁles to non-volatile
droplets. However, the lifetimes of volatile droplets were observed to be signiﬁcantly shortened
in the presence of the superheating that may occur when the air static pressure drops below
the vapor pressure of the droplet ﬂuid.
3. The droplets in this continuously accelerating ﬂow, where Weber number continuously and
rapidly increases with downstream distances were observed to disrupt an order of magnitude
faster than would be expected in shock-tube-like ﬂows with constant air velocity for similar
values of the Weber number at which the disruption commences.
4. Generally, similar patterns of droplet breakup (initial deformation, sheet stripping, primary
breakup, and catastrophic breakup) were observed for the different test ﬂuids, but over some-
what different downstream distances, depending on the vapor pressure and Weber number.
Consideration of the relevant droplet Bond number suggests that the disruption is due to
aerodynamic deformation and ﬂuid shedding, rather than inertial instability.
5. The Weber numbers at which these various disruption modes occur are, however, generally
higher than those reported previously in shock-tube experiments where the Weber numbers
are approximately constant.
6. The more volatile droplets exhibited a higher vaporization rate than that seen for non-volatile
droplets in supersonic ﬂow at all downstream locations, suggesting that droplet superheating
does play some role in accelerating the vaporization of supersonic droplets under for the test
conditions employed here.
ACKNOWLEDGMENTS
The authors would like to acknowledge the help of Mr. Robert Cerff in conducting the exper-
iments reported here. This work was supported by that National Science Foundation (NSF) under
Grant No. FA42883/A42648.
APPENDIX: DETAILS OF DROPLET BREAKUP AND VAPORIZATION
This appendix provides more detailed images of close-up droplet disruption and LIF in super-
sonic ﬂow. Figures 17 and 18 show droplet disruption for 2-propanol and TGDE by each region,
which represents Region I (deformation), Region II (initial breakup), Region III (primary breakup),
and Region IV (total breakup). In supersonic ﬂow, the detailed images of droplet fragmentation and
vaporization were captured as shown in Figs. 19 and 20.
 29 August 2026 09:45:45

<!-- PDF_PAGE: 21 -->

076102-20 Y . Kim and J. C. Hermanson Phys. Fluids 24, 076102 (2012)
 
 
 
 
 
 
 z = -8.75 mm, t = 0.6ms 
Mr = 0.12, We = 10.5 
 z = -8.51 mm, t = 0.62ms 
Mr = 0.12, We = 10.9 
 z = -6.37 mm, t = 0.77ms 
Mr = 0.17, We = 18.25 
 z = -6.74 mm, t = 0.75ms 
Mr = 0.16, We = 16.64 
 z = -3.85 mm, t = 0.9ms 
Mr = 0.26, We = 39.6 
 z = -2.21 mm, t = 0.95ms 
Mr = 0.37, We = 68.4 
Region I 
 
z = -0.77 mm, t = 0.99ms 
Mr = 0.55, We = 128.2 
 
z = -1.00 mm, t = 0.98ms 
Mr = 0.51, We = 115.3 
 
z = -0.49 mm, t = 0.992ms 
Mr = 0.60, We = 143.8 
 
z = -1.35 mm, t = 0.97ms 
Mr = 0.46, We = 97.8 
 
z = -0.97 mm, t = 0.982ms 
Mr = 0.52, We = 114.8 
 
z = -0.93 mm, t = 0.984ms 
Mr = 0.52, We = 120.3 
Region II 
 z = 0.57 mm, t = 1.01ms 
Mr = 0.88, We = 217.2 
 z = 0.81 mm, t = 1.02ms 
Mr = 0.97, We = 234.3 
 z = 0.48 mm, t = 1.009ms 
Mr = 0.85, We = 208.2 
 z = 2.44 mm, t = 1.03ms 
Mr = 1.45, We = 278.9 
 z = 1.1 mm, t = 1.018ms 
Mr = 1.07, We = 263.3 
 z = 1.00 mm, t = 1.016ms 
Mr = 1.04, We = 250.7 
Region III 
 z = 3.11 mm, t = 1.04ms 
Mr = 1.53, We = 254.9 
 z = 3.22 mm, t = 1.043ms 
Mr = 1.56, We = 256.2 
 z = 5.05 mm, t = 1.061ms 
Mr = 1.77, We = 197.6 
 z = 5.00 mm, t = 1.06ms 
Mr = 1.76, We = 188.8 
 z = 4.30 mm, t = 1.05ms 
Mr = 1.71, We = 219.9 
 z = 4.47 mm, t = 1.055ms 
Mr = 1.72, We = 210.8 
Region IV 
100 μm 
Air ﬂow and Droplet direc/g415on 
FIG. 17. Droplet breakup regions for 2-propanol.
 29 August 2026 09:45:45

<!-- PDF_PAGE: 22 -->

076102-21 Y . Kim and J. C. Hermanson Phys. Fluids 24, 076102 (2012)
 
 
 
 
 
 
z = -9.54 mm, t = 0.534 ms 
Mr = 0.127, We = 6.71 
 
z = -9.37 mm, t = 0.558 ms 
Mr = 0.129, We = 6.87 
 
z = -6.43 mm, t = 0.899 ms 
Mr = 0.18, We = 13.1 
 
z = -6.89 mm, t = 0.857 ms 
Mr = 0.168, We = 11.9 
 
z = -1.882 mm, t = 1.1 ms 
Mr = 0.407, We = 65 
 
z = -1.38 mm, t = 1.18 ms 
Mr = 0.418, We = 68.7 
Region I 
 
z = -1.31 mm, t = 1.17 ms 
Mr = 0.451, We = 69.6 
 
z = -1.32 mm, t = 1.18 ms 
Mr = 0.456, We = 70.5 
 
 
z = -1.1 mm, t = 1.19 ms 
Mr = 0.486, We = 78 
 
 
z = -0.089 mm, t = 1.21 ms 
Mr = 0.649, We = 117 
 
 
z = -0.494 mm, t = 1.2 ms 
Mr = 0.579, We = 101 
 
 
z = 0.467 mm, t = 1.22 ms 
Mr = 0.805, We = 145 
Region II 
  
z = 0.877 mm, t = 1.233 ms 
Mr = 0.955, We = 169 
 
 
z = 0.887 mm, t = 1.234 ms 
Mr = 0.953, We = 168 
  
z = 0.978 mm, t = 1.235 ms 
Mr = 1.01, We = 172 
  
z = 1.08 mm, t = 1.24 ms 
Mr = 1.03, We = 177 
  
z = 2.29 mm, t = 1.26 ms 
Mr = 1.42, We = 203 
  
z = 2.93 mm, t = 1.27 ms 
Mr = 1.5, We = 177 
Region III 
 
 
z = 2.62 mm, t = 1.26 ms 
Mr = 1.45, We = 184 
 
 
z = 3.16 mm, t = 1.27 ms 
Mr = 1.51, We = 169 
  
z = 3.85 mm, t = 1.278 ms 
Mr = 1.65, We = 164 
  
z = 3.93 mm, t = 1.28 ms 
Mr = 1.648, We = 160.4 
  
z = 4.1 mm, t = 1.282 ms 
Mr = 1.68, We = 160 
  
z = 4.3 mm, t = 1.284 ms 
Mr = 1.7, We = 156 
Region IV 
Air ﬂow and Droplet direc/g415on 
100 μm 
FIG. 18. Droplet breakup regions for TGDE.
 29 August 2026 09:45:45

<!-- PDF_PAGE: 23 -->

076102-22 Y . Kim and J. C. Hermanson Phys. Fluids 24, 076102 (2012)
FIG. 19. Representative LIF images: 2-propanol (left) and Hex-Pen 50/50 (right). The white contours, from outermost to
innermost, correspond, respectively, to the reference vapor concentrations of 0.8 × 105,1 . 6× 105, and 2.6 × 105 mol/cc.
 29 August 2026 09:45:45

<!-- PDF_PAGE: 24 -->

076102-23 Y . Kim and J. C. Hermanson Phys. Fluids 24, 076102 (2012)
FIG. 20. Representative LIF images: 2-propanol (left) and Hex-Pen 50/50 (right). The white contours, from outermost to
innermost, correspond, respectively, to the reference vapor concentrations of 0.8 × 105,1 . 6× 105, and 2.6 × 105 mol/cc.
 29 August 2026 09:45:45

<!-- PDF_PAGE: 25 -->

076102-24 Y . Kim and J. C. Hermanson Phys. Fluids 24, 076102 (2012)
1 I. W. Kay, W. T. Peschke, and R. N. Guile, “Hydrocarbon-fueled scramjet combustor investigation,” J. Propul. Power 8(2),
507–512 (1992).
2 E. M Peter, A. Takimoto, and Y . Hayashi, “Flashing and shattering phenomena of superheated liquid jets,” JSME Int. J.,
Ser. B 37(2), 313–321 (1994).
3 T. Y oshida and K. Takayama, “Interaction of liquid droplets with planar shock waves,”ASME J. Fluids Eng. 112, 481–486
(1990).
4 O. G. Engel, “Fragmentation of waterdrops in the zone behind an air shock,” J. Res. Natl. Bur. Stand. 60(3), 245–280
(1958).
5 P . G. Simpkins and E. L. Bales, “Water-drop response to sudden accelerations,” J. Fluid Mech. 55(4), 629–639 (1972).
6 D. D. Joseph, A. Huang, and G. V . Candler, “V aporization of a liquid drop suddenly exposed to a high-speed airstream,”
J. Fluid Mech. 318, 223–236 (1996).
7 D. D. Joseph, J. Bellanger, and G. S. Beavers, “Breakup of a liquid drop suddenly exposed to a high-speed airstream,” Int.
J. Multiphase Flow 25, 1263–1303 (1999).
8 H. Hirahara and M. Kawahashi, “Experimental investigation of viscous effects upon a breakup of droplets in high-speed
air ﬂow,” Exp. Fluids 13(6), 423–428 (1992).
9 A. R. Hanson, E. G. Domich, and H. S. Adams, “Shock tube investigation of the breakup of drops by air blasts,” Phys.
Fluids 6(8), 1070–1080 (1963).
10 A. A. Shraiber, A. M. Podvysotsky, and V . V . Dubrovsky, “Deformation and breakup of drops by aerodynamic forces,”
Atomization Sprays 6, 667–692 (1996).
11 Z. Liu and R. D. Reitz, “An analysis of the distortion and breakup mechanisms of high speed liquid drops,”Int. J. Multiphase
Flow 23(4), 631–650 (1997).
12 S. S. Hwang, Z. Liu, and R. D. Reitz, “Breakup mechanisms and drag coefﬁcients of high-speed vaporizing liquid drops,”
Atomization Sprays 6, 353–376 (1996).
13 B. E. Gelfand, “Droplet breakup phenomena in ﬂows with velocity lag,” Prog. Enegry Combust. Sci. 22, 201–265 (1996).
14 M. Pilch and C. A. Erdman, “Use of breakup time data and velocity history date to predict the maximum size of stable
fragments for acceleration-induced breakup of a liquid drop,” Int. J. Multiphase Flow 13(6), 741–757 (1987).
15 C. Ortiz, D. D. Joseph, and G. S. Beavers, “Acceleration of a liquid drop suddenly exposed to a high-speed airstream,” Int.
J. Multiphase Flow 30, 217–224 (2004).
16 L. M. Y anson, M. R. Phariss, and J. C. Hermanson, “Effects of liquid superheat on droplet disruption in a supersonic
stream,” AIAA Paper 2005-0351, 2005.
17 J. C. Hermanson, “Dynamics of supersonic droplets of volatile liquids,” AIAA J. 45(3), 730–733 (2007).
18 O. A. Powell, J. T. Ewards, R. B. Norris, and K. E. Numbers, “Development of hydrocarbon-fuels scramjet engines: The
hypersonic technology (HyTech) program,” J. Propul. Power 17(6), 1170–1176 (2001).
19 M. B. Colket and L. J. Spadaccini, “Scramjet fuels autoignition study,” J. Propul. Power 17(2), 315–323 (2001).
20 G. J. Li, T. N. Dinh, and T. G. Theofanous, “An experimental study of droplet breakup in supersonic ﬂow: The effect of
long-range interactions,” 42nd AIAA Aerospace Sciences Meeting and Exhibit , AIAA Paper No. 2004-968, 2004.
21 A. B. Bailey and J. Hiatt, “Free-ﬂight measurements of sphere drag at subsonic, transonic, supersonic, and hypersonic
speeds for continuum, transition, and near-molecular ﬂow conditions,” Arnold Engineering Development Center, Arnold
Air Force Station, TN, Report No. AEDC-TR-70-291.
22 Y . J. Kim, R. G. Cerff, and J. C. Hermanson, “Injection and disruption of supersonic droplets,” 48th AIAA Aerospace
Sciences Meeting and Exhibit , AIAA Paper No. 2010-752, 2010.
23 Y . J. Kim, “An experiment study of the disruption and vaporization or non-volatile and volatile droplets under locally
supersonic conditions,” Ph.D. dissertation, University of Washington, 2011.
24 C. T. Crowe, M. Sommerfeld, and Y . Tsuji, Multiphase Flows with Droplets and Particles (CRC, 1998), p. 24.
25 D. S. Shringi, B. D. Shaw, and H. A. Dwyer, “Laser-induced ﬂuorescence imaging of acetone inside evaporating and
burning fuel droplets,” Opt. Lasers Eng. 47(1), 51–56 (2009).
26 T. Tran, Y . Kochar, and J. Seitzman, “Measurements of liquid acetone ﬂuorescence and phosphorescence for two-phase
fuel imaging,” 43rd AIAA Aerospace Sciences Meeting and Exhibit , AIAA Paper 2005-0827, 2005.
27 H. Takahashi, S. Ikegami, H. Oso, G. Masuya, and M. Hirota, “Quantitative imaging of injectant mole fraction and density
in supersonic mixing,” AIAA J. 46(11), 2935–2943 (2008).
28 B. D. Ritchi and J. M. Seitzman, “Quantitative acetone PLIF in two-phase ﬂows,” 39th Aerospace Sciences Meeting and
Exhibit, AIAA Paper 2001-0414, 2001.
29 A. Lozano, B. Yip, and R. K. Hanson, “Acetone: A tracer for concentration measurements in gaseous ﬂows by planar
laser-induced ﬂuorescence,” Exp. Fluids 13(6), 369–376 (1992).
30 K. Ammigan and H. L. Clack, “Planar laser-induced ﬂuorescence imaging of the spatial vapor distribution around a
monodisperse acetone droplet stream exposed to asymmetric radiant heating,” Proc. Combust. Inst. 32(2), 2179–2186
(2009).
31 M. Orain, X. Mercier, and F. Grisch, “PLIF imaging of fuel-vapor spatial distribution around a monodisperse stream of
acetone droplets: Comparison with modeling,” Combust. Sci. Technol. 177(2), 249–278 (2005).
32 E. Y . Harper, G. W. Grube, and I. Chang, “On the breakup of accelerating liquid drops,” J. Fluid Mech. 52(3), 565–591
(1972).
33 T. G. Theofanous, G. J. Li, and T. N. Dihn, “Aerobreakup in rareﬁed supersonic gas ﬂows,” ASME J. Fluids Eng. 126,
516–527 (2004).
 29 August 2026 09:45:45
