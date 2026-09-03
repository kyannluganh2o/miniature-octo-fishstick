<!-- PDF_PAGE: 1 -->

Research Paper
Investigation of hydrogen jet formation for direct injection engines: a 
dual-scale framework from shock reflection to spray evolution
Fangxi Xie
a , b
, Zhendong Liang
a , b
, Bo Cui
c
, Wenjun Guo
c
, Xiaoping Li
a , b
, Beiping Jiang
a , b
,  
Zhe Zhao
a , b
, Xiangyang Wang
a , b , *
a
College of Automotive Engineering, Jilin University, Changchun 130025, China
b
National Key Laboratory of Automotive Chassis Integration and Bionics, Jilin University, Changchun 130025, China
c
China Automotive Engineering Research Institute Co., Ltd, Chongqing 401122, China
ARTICLE INFO
Keywords:
Hydrogen direct injection engine
Jet characteristics
Shock reflection
Spray evolution
ABSTRACT
Understanding hydrogen jet formation in hydrogen-fueled direct injection engines is essential for optimizing in- 
cylinder mixture preparation and achieving high-efficiency, low-emission combustion. This study introduces a 
dual-scale analytical framework that links near-field shock dynamics with far-field spray evolution, providing a 
more comprehensive perspective compared to previous studies that primarily focused on either experimental 
observations or numerical simulations alone. Constant volume combustion vessel experiments were combined 
with high-fidelity numerical simulations to systematically evaluate the effects of nozzle pressure ratio, nozzle 
hole diameter, and ambient temperature on hydrogen jet development. The results demonstrate that the nozzle 
pressure ratio is the dominant factor governing jet momentum, morphology, and entrainment, while nozzle hole 
diameter controls shear layer growth and dispersion scale, and ambient temperature plays a secondary role by 
promoting instabilities and lateral expansion. The proposed framework effectively captures the coupling between 
compressible shock – vortex interactions in the near field and large-scale dispersion in the far field. These findings 
provide new insights into hydrogen mixture formation and offer theoretical guidance for developing more 
efficient and controllable injection strategies in hydrogen direct injection engines.
1. Introduction
Hydrogen-fueled internal combustion engines have emerged as a key 
technology in the global pursuit of carbon neutrality [ 1 ]. With zero 
carbon emissions at the point of use and favorable combustion charac -
teristics such as high flame speed [ 2 ] and wide flammability limits [ 3 ], 
hydrogen offers a promising alternative to conventional fossil fuels. 
Among various hydrogen utilization strategies, HDI has garnered 
increasing attention due to its potential to enhance thermal efficiency 
[ 4 , 5 ] , suppress abnormal combustion phenomena (e.g., knock and pre- 
ignition) [ 6 , 7 ], and enable lean burn by precisely controlling the in- 
cylinder mixture formation [ 8 ].
In direct injection engines, the dynamics of fuel jet formation play a 
critical role in determining the spatial and temporal evolution of the 
mixture[ 9 , 10 ], which directly affects combustion quality and emissions 
[ 11 , 12 ]. Numerous studies have investigated gaseous and liquid jets to 
better understand penetration and mixing behaviors. For instance, Dong 
et al. reported that for natural gas jets, higher injection pressures do not 
yield proportionally longer penetrations because of choked-flow con -
straints at the nozzle exit [ 13 ], while Lei et al. showed numerically that 
methane jet development proceeds in two stages, with rapid early evo -
lution followed by a quasi-stationary phase [ 14 ]. Additionally, Ni et al., 
based on schlieren imaging and planar laser-induced fluorescence, re -
ported that the rate of increase in jet penetration distance gradually 
diminishes as NPR rises [ 15 ]. For liquid sprays, Lu et al. explained that 
increasing the injection pressure enhances the penetration velocity of 
the spray and the spreading extent of the liquid film after impingement, 
whereas an increase in ambient pressure produces the opposite effect 
[ 16 ].
Other liquid fuels, such as alcohols and liquid ammonia, have been 
extensively studied. For methanol, higher injection pressures enhance 
penetration and dispersion, with the initial cone angle decreasing 
rapidly and strong sensitivity to ambient temperature [ 17 ]. Ethanol 
spray penetration is mainly influenced by ambient temperature, while 
ambient pressure governs overall spray characteristics; predictive 
models such as Response Surface Methodology and Artificial Neural 
Networks can accurately estimate penetration [ 18 , 19 ]. For liquid 
* Corresponding author at: College of Automotive Engineering, Jilin University, Changchun 130025, China.
E-mail address: 753403128@qq.com (X. Wang). 
Contents lists available at ScienceDirect
Applied Thermal Engineering
journal homepag e: www.el sevier.com/loc ate/aptherm eng
https://doi.org/10.1016/j.applthermaleng.2025.128523
Received 9 July 2025; Received in revised form 21 September 2025; Accepted 25 September 2025  
Applied Thermal Engineering 280 (2025) 128523 
Available online 27 September 2025 
1359-4311/© 2025 Elsevier Ltd. All rights are reserved, including those for text and data mining, AI training, and similar technologies.

<!-- PDF_PAGE: 2 -->

ammonia, high temperatures reduce penetration sensitivity to injection 
pressure and reveal three axial temperature regions along the spray 
centerline: isothermal, logarithmic growth, and linear growth zones 
[ 20 ]. These findings indicate that spray penetration and distribution are 
strongly dependent on ambient conditions and injection parameters, 
and predictive modeling provides effective characterization tools.
Although such works have established valuable empirical and semi- 
empirical correlations, many remain descriptive in nature and fuel- 
specific, making cross-comparison difficult. Moreover, liquid sprays 
are dominated by breakup and atomization, whereas gaseous jet -
s — especially hydrogen — are governed by compressible flow physics. 
The unique properties of hydrogen, including low molecular weight [ 21 ] 
and high diffusivity [ 22 ], lead to distinctive under-expanded jet 
behavior with near-field features such as Mach disks, barrel shocks, and 
shear layers [ 23,24 ]. These structures strongly influence penetration, 
entrainment, and subsequent mixture distribution [ 25,26 ]. Recent 
studies have highlighted the role of reflected shocks in secondary vortex 
generation [ 27 ] and confirmed NPR as the primary determinant of Mach 
disk characteristics [ 28 ]. Wang et al. modified empirical correlations for 
specific injector designs [ 29 ]. Comparative works have further revealed 
that hydrogen jets mix more intensively downstream of the Mach disk 
than methane jets [ 30 ], and that elevated ambient temperature and 
pressure enhances hydrogen jet spreading through diffusion effects 
[ 31,32 ]. Further research also indicated that the transient tip vortex in 
hydrogen jets may destabilize the oblique shock boundaries during the 
early injection phase [ 33 ].
More recent contributions, including Chen et al. [ 34 ], Kirchweger 
et al. [ 35 ], Lee et al. [ 36 ] and Coratella et al.[ 37 ], have underscored the 
importance of turbulence – shock interactions in shaping hydrogen jet 
mixing, but a consistent framework for linking near-field compressible 
structures with far-field spray dynamics remains incomplete.
Despite growing interest, most prior investigations emphasize global 
spray parameters (penetration distance, spray angle, jet volume), with 
limited attention to the near-field physics where shock – vortex in -
teractions and velocity gradients dominate. This simplification over -
looks the decisive role of the initial jet core in shaping far-field 
morphology and mixture formation under realistic engine conditions. As 
a result, there is still a critical gap in understanding how near-field 
structures (e.g., Mach disks and shear layers) couple with far-field 
dispersion, especially under varying NPR, NHD, and AT.
To address this gap, the present study proposes a dual-scale analyt -
ical framework that separates hydrogen jet evolution into two inter -
connected regimes: (i) a near-field core dominated by compressible 
shock – shear interactions, and (ii) a far-field region governed by large- 
scale dispersion and turbulent mixing. By combining constant-volume 
vessel experiments with high-fidelity simulations, this work systemati -
cally quantifies the influence of NPR, NHD, and AT on jet formation, 
transition, and evolution. The contributions are twofold: (i) establishing 
a unified framework that directly captures the coupling between near- 
field shock physics and far-field spray development, and (ii) providing 
new physical insights and design guidance for optimizing injection 
strategies and mixture preparation in HDI engines.
2. Experimental setup
To investigate the influence of spraying and mixing behavior on HDI 
engine performance in a comprehensive manner, a combined approach 
involving both CVCC experiments and CFD simulations was adopted. 
These two platforms were designed to capture complementary physical 
processes under either controlled or engine-representative conditions, 
enabling a multi-scale and cross-validated understanding of hydrogen 
spray dynamics.
2.1. CVCC platform
The CVCC platform utilized in this study, as schematically illustrated 
in Fig. 1 , integrates multiple subsystems for safe and precise experi -
mental operation [ 38 ]. The hydrogen fuel delivery system consists of a 
high-pressure cylinder (maximum working pressure of 120 bar), pres -
sure regulator (0 – 150 bar), flame arrestor, and fuel injector, which 
collectively ensure controlled and reliable hydrogen injection into the 
chamber. Ambient gas conditions are established using a compressed 
dry air supply system with intake and exhaust valves, allowing homo -
geneous filling and controlled evacuation after each test. A dedicated 
top-mounted ventilation system is employed to prevent hydrogen 
accumulation and ensure operational safety.
Spray visualization is achieved using a Z-type Schlieren imaging 
system, composed of ( Fig. 2 ) a high-power LED light source (55 W), 
optical diaphragms, reflective plane and concave mirrors (diameter 38 
mm and 101.6 mm; focal length 1500 mm), a vertically aligned knife- 
edge with 50 % cutoff, and a high-speed Phantom V7.3 camera equip -
ped with a Nikon AF 80 – 200 mm f/2.8D lens set at 200 mm. The entire 
optical path uses UV-grade quartz aluminum components with a 
reflective wavelength range of 200 – 1100 nm, providing high-fidelity 
visualization of the hydrogen jet [ 39 ].
System control and data acquisition are managed through a 
LabVIEW-based interface, which coordinates the microcontroller unit, 
pressure and temperature sensors, and the high-speed camera system. 
Injection timing and image acquisition are synchronized via digital 
triggers. Internal chamber temperature is regulated by a flexible silicone 
heater and insulation mat, with an insulation mat and controlled 
through a PID feedback loop. Prior to testing, the temperature setting 
was calibrated using a reference K-type thermocouple placed at the 
nozzle exit plane. To verify spatial uniformity, three additional ther -
mocouples were distributed inside the optical chamber, and the 
measured variation across the field of view was within ± 2 K of the 
setpoint both before and after injection. During tests, images are 
captured at a frequency of 10,000 Hz and a resolution of 512 × 512 
pixels, with a fixed exposure time of 10 μ s to ensure accurate capture of 
fast-evolving spray structures. The CVCC chamber itself is cuboid in 
shape and fitted with three optical-grade quartz windows (JGS2, 130 
mm diameter, 50 mm thickness) to facilitate optical access. The injector 
is mounted vertically through a threaded port at the top center of the 
chamber and sealed using a combination of nitrile O-rings and copper 
gaskets to withstand high internal pressures. The chamber temperature 
was monitored with calibrated K-type thermocouples (accuracy ± 1 K), 
the pressure was measured using piezoelectric pressure transducers 
(accuracy ± 0.2 % of full scale), and the injection timing was controlled 
by a high-speed electronic driver with an accuracy of ± 0.05 ms. The 
overall uncertainty in derived macroscopic spray parameters was esti -
mated to be within 3 – 5 %, consistent with values reported in previous 
studies using the same CVCC facility and Schlieren imaging system 
[ 38,39 ].
The selected experimental ranges of nozzle pressure ratio (5 – 100), 
nozzle hole diameters (0.75 – 2.0 mm), and ambient temperatures 
(300 – 800 K) were chosen to be representative of in-cylinder conditions 
Nomenclature
AT Ambient Temperature
CFD Computational Fluid Dynamics
CVCC Constant Volume Combustion Chamber
CFL Courant – Friedrichs – Lewy
HDI Hydrogen Direct Injection
LES Large Eddy Simulation
NHD Nozzle Hole Diameter
NIST National Research of Standards and Technology
NPR Nozzle Pressure Ratio
RANS Reynolds-Averaged Navier – Stokes
F. Xie et al.                                                                                                                                                                                                                                       Applied Thermal Engineering 280 (2025) 128523 
2

<!-- PDF_PAGE: 3 -->

in HDI engines. In particular, these values correspond to injection 
pressure ratios, nozzle geometries, and thermodynamic states typically 
encountered during the intake and compression strokes. The relevance 
of these parameter ranges has been confirmed in our previous HDI en -
gine study [ 40 – 42 ], where in-cylinder measurements demonstrated that 
NPR, NHD, and AT values fall within the practical operating window of a 
prototype hydrogen engine.
To quantitatively analyze the evolution of the hydrogen spray, a 
MATLAB-based image processing script was developed. This script au -
tomates the batch processing of schlieren image sequences captured in 
TIFF format and performs several key preprocessing steps. The images 
are first cropped based on the nozzle and spray location, and then 
resized for consistency. Edge-preserving MCF filtering is applied to 
reduce noise while maintaining contour sharpness. Histogram stretching 
and grayscale normalization are used to enhance the contrast between 
the spray and background.
To ensure the accuracy and repeatability of Schlieren measurements, 
the optical system was carefully calibrated prior to experiments. A 
reference calibration grid with 1 mm spacing was positioned at the 
nozzle exit plane to establish the pixel-to-length conversion, yielding a 
scaling factor. The optical path was aligned by adjusting the reflective 
mirrors until the calibration grid produced sharp and distortion-free 
edges on the imaging sensor. The knife-edge cutoff ratio was verified 
by using a uniform background light source and adjusting the vertical 
blade to achieve a 50 % light cutoff. Prior to each experimental 
sequence, the stability of the optical setup was rechecked to minimize 
Fig. 1. Schematic diagram of CVCC bench.
Fig. 2. Control interface of CVCC.
F. Xie et al.                                                                                                                                                                                                                                       Applied Thermal Engineering 280 (2025) 128523 
3

<!-- PDF_PAGE: 4 -->

alignment errors. These procedures ensured that both the spatial di -
mensions and density gradient visualization from the Schlieren images 
were reliable and reproducible.
2.2. CFD modelling
In this study, CFD simulations were conducted using the CONVERGE 
software. Detailed descriptions of the CONVERGE platform, governing 
equations, and turbulence models are provided in the supplementary 
materials . Hydrogen injection was modeled as a gaseous inflow under 
choked-flow conditions, with the instantaneous mass flow rate deter -
mined by the upstream pressure and nozzle diameter. Boundary condi -
tions included a prescribed total pressure at the nozzle inlet, ambient 
pressure and temperature at the chamber walls, and no-slip adiabatic 
wall conditions. Thermodynamic and transport properties of hydrogen 
were obtained from the NIST database and implemented in CONVERGE. 
The investigation of hydrogen jet characteristics is divided into two 
parts: the near-field core region and the far-field macroscopic region. 
Due to the differing focuses of these two regions, separate computational 
strategies were employed. Specifically, the near-field core region pri -
marily addresses the evolution of shock structures during the early stage 
of the under-expanded supersonic hydrogen jet, as well as the formation 
and development of transient vortices. In contrast, the far-field region 
focuses on the macroscopic features of the jet, including penetration 
distance, spray cone angle, projected area, and self-similarity behavior, 
where detailed vortex structures are of less concern. Accordingly, 
different geometrical models and turbulence models were adopted for 
each region.
For the simulation of the near-field core region, a simplified geom -
etry and high-resolution mesh were used to ensure accurate capture of 
early-stage shock structures and transient vortex dynamics. As illus -
trated in Fig. 3(a) , the injector was simplified to a small cylindrical 
nozzle with a diameter D , matching that of the actual injector. The 
computational domain was set as a cylinder with a height and diameter 
of 20 mm, sufficient to encompass the main flow structures during early 
jet development. The base mesh size was set to 2 mm, with up to six 
levels of adaptive mesh refinement. Three fixed mesh refinement regions 
were defined within the main cylinder, with refinement levels of 2, 5, 
and 6, corresponding to initial cell sizes of D /4, D /16, and D /32, 
respectively. The total number of computational cells reached approxi -
mately 13,600,000. In the near-field LES simulations, an adaptive time- 
stepping strategy was employed based on the CFL condition to ensure 
accurate resolution of shock and vortex dynamics while maintaining 
computational efficiency. Prior to the production runs, short conver -
gence tests were performed to determine stable bounds for the time step: 
if the time step is chosen too large the solution fails to converge or 
under-resolves rapid shock – shear interactions. Therefore, the solver was 
configured with an adaptive time-step controlled by a target CFL num -
ber between 0.5 – 1. To maintain numerical stability, the maximum and 
minimum time steps were set to 1 × 10
– 9 
and 1 × 10
– 10 
s, respectively. 
Due to the computational cost being close to the limits of available re -
sources, mesh and time-step independence studies were not further 
conducted for this case.
For the simulation of the far-field macroscopic characteristics of the 
hydrogen jet, the full geometry of the constant-volume combustion 
chamber was used, and mesh independence was verified. The geometry 
and mesh configuration are shown in Fig. 3(b) . To balance simulation 
accuracy and computational efficiency, several base mesh sizes were 
tested. As shown in Fig. 4 , the comparison of axial penetration distances 
under different mesh resolutions demonstrated that a base mesh size of 
4 mm provides sufficient accuracy in capturing the axial jet penetration 
while avoiding excessive computational cost. In addition, Fig. 5 further 
confirms that the selected mesh and time step settings effectively 
reproduce the macroscopic behavior of the hydrogen jet. As can be seen 
from the figure, the spray morphologies of the experimental and simu -
lated hydrogen free jet schlieren images at each development time are 
highly similar, with the difference in axial penetration distance being 
less than 5 %.
In terms of temporal resolution, the time step in CFD simulations 
governs the rate of energy and momentum transfer. If the time step is too 
Fig. 3. 3D geometry model and mesh settings.
8mm
6mm
5mm
4mm
3mm
Fig. 4. Comparison of axial penetration distance with different basic grids.
F. Xie et al.                                                                                                                                                                                                                                       Applied Thermal Engineering 280 (2025) 128523 
4

<!-- PDF_PAGE: 5 -->

large, the transfer rate within fine mesh regions may be overestimated, 
potentially leading to deviations from the actual physical process, 
instability in the flow field, and increased numerical errors. To match 
the 4 mm base mesh in the far-field simulations, an initial time step of 1 
× 10
 9 
s was used to ensure numerical stability and physical accuracy.
Since the far-field simulation focuses on time-averaged flow featur -
es — such as penetration distance, cone angle, and spray area — rather 
than capturing transient vortex structures, the RANS SST k – ω turbulence 
model was employed to maintain a balance between accuracy and 
computational cost. In contrast, the near-field core region required 
detailed resolution of unsteady flow features such as shock evolution 
and vortex dynamics in the initial jet stage. Therefore, the Dynamic 
Structure subgrid-scale model within the LES framework was used to 
improve fidelity and capture the fine-scale flow structures.
2.3. Calculation of spray index
In the analysis of hydrogen jet characteristics, the definitions and 
calculation methods of key parameters are as follows. The Mach disk 
marks the location where the jet transitions from supersonic to subsonic 
flow, typically accompanied by abrupt changes in pressure, tempera -
ture, and density. The position of the Mach disk is closely related to 
nozzle design and the jet ’ s pressure ratio. The Mach disk diameter refers 
to the actual transverse extent of the shock region originating from the 
nozzle, indicating the lateral expansion of the Mach structure. In this 
study, the position and diameter of the Mach disk are calculated based 
on Equations (1) and (2) , respectively [ 28 ]. 
L
MD
D
e
= 0 . 69 M
e
̅̅̅̅̅̅ ̅
γ η
e
√
(1) 
Where L
MD 
is the length (position) of the Mach disk, D
e 
is the 
diameter at the outlet, γ is the specific heat ratio of hydrogen, and η
e 
is 
the injection pressure ratio at the outlet. 
D
MD
D
e
=
{
0 . 36
̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅ ̅
η
0
 3 . 9
√
For contour nozzles
0 . 31
̅̅̅̅̅̅̅̅̅̅̅̅ ̅
η
0
 5
√
For cone or hole nozzles
(2) 
where D
MD 
is the diameter of the Mach disk.
Jet penetration distance is primarily determined by the injection 
pressure ratio, velocity, temperature, and interactions with the ambient 
medium. The jet cone angle defines the expansion rate of the jet and the 
strength of interaction between the jet flow and the surrounding gas. 
The jet area refers to the cross-sectional area of the jet at a given axial 
location and is often used to characterize flow rate and mixing behavior.
Fig. 6 provides a detailed illustration of the definitions of penetration 
distances and cone angle. The axial penetration distance is defined as the 
maximum distance from the nozzle exit to the leading edge of the spray 
along the jet axis, as captured in the Schlieren images. The radial 
penetration distance is defined as the maximum spray width in the di -
rection perpendicular to the jet axis. If the spray is asymmetric, the 
radial expansion is recorded separately on both sides, and the total 
radial width is represented as a + b. The spray cone angle refers to the 
total included angle between the left and right boundary lines of the jet 
spray relative to the centerline extending from the nozzle exit. The cone 
Fig. 5. Comparison of experimental and simulated through jet images.
Fig. 6. Definition of jet penetration distance, spay cone angle and area.
F. Xie et al.                                                                                                                                                                                                                                       Applied Thermal Engineering 280 (2025) 128523 
5

<!-- PDF_PAGE: 6 -->

angle is calculated based on Equation (3) . 
θ = tan
 1
(
d
1
L
)
+ tan
 1
(
d
2
L
)
(3) 
When the axial penetration distance of the spray is less than a 
specified length L , the spray cone angle is defined as the angle between 
the central axis of the nozzle and the lines extending to the widest part of 
the jet. The spray area is defined as the projected area of the spray jet on 
the image plane, which is used to quantify the spatial coverage of the 
spray. The spray area is calculated according to Equation (4) . 
A =
∑
( x , y )∈ R
s
p
(4) 
where R represents the identified spray region and s
p 
denotes the 
physical area corresponding to a single pixel. The spray region area is 
computed using the regionprops function in MATLAB, which performs 
area statistics on the binary image.
3. Result and discussion
Fig. 7 illustrates the Schlieren images of under-expanded hydrogen 
jets captured at various time intervals under three different NPRs (16/2, 
40/3, and 60/2). Despite inherent limitations in optical resolution, 
characteristic flow features such as the shock boundaries and supersonic 
core can still be discerned. At the earliest stages of injection (e.g., 0.4 
ms), all three conditions show clear evidence of a high-speed jet issuing 
from the nozzle, accompanied by density gradients typical of under- 
expanded jet flows.
As the injection continues, the formation of Mach disks becomes 
progressively more visible. With increasing NPR, both the location and 
the diameter of the Mach disk exhibit noticeable growth. This suggests 
that higher NPR extend the supersonic core length and intensify the 
momentum exchange within the jet. For instance, at NPR = 60/2, the 
Mach structure appears more extended and pronounced compared to the 
16/2 condition, indicating a stronger expansion and recompression 
process downstream of the nozzle. However, due to the unsteady nature 
of the hydrogen jet and the optical distortion caused by turbulent mixing 
and density fluctuations, the precise contours of the Mach disks remain 
blurry, and quantitative interpretation from these experimental images 
is limited.
To address these limitations and gain a deeper understanding of the 
shock structure evolution, especially in the jet core region, numerical 
simulations were conducted in the subsequent section. The simulation 
results offer improved spatial and temporal resolution and provide a 
complementary means to analyze jet characteristics that cannot be fully 
resolved by optical diagnostics alone. The combination of experimental 
and numerical methods allows for a more comprehensive evaluation of 
the near-field jet behavior under various injection conditions.
3.1. The impact of NPR
The NPR conditions configured in this study cover the typical oper -
ating range of HDI engines. The evolution and characteristics of the gas 
jet are not strongly dependent on the absolute injection pressure or 
background pressure alone, but rather on the injection pressure ratio. 
The corresponding parameter settings are summarized in Table 1 .
Fig. 8 presents the mass fraction contours of hydrogen jets in the 
near-field region during the initial injection stage (8 – 20 μ s) under 
various NPRs. Overall, as the NPR increases, the jet morphology tran -
sitions from a relatively confined and momentum-deficient gas plume to 
a high-velocity, structurally complex, and clearly stratified under- 
expanded jet ( Table 2 ).
At an NPR of 5, the hydrogen jet exhibits weak expansion and high 
diffusion characteristics. The mass fraction near the nozzle exit is rela -
tively low, with blurred boundaries and the absence of well-defined 
shear layer structures. Due to insufficient momentum, no prominent 
Fig. 7. Comparison of experimental Schlieren images under different NPR.
Table 1 
NPR simulation condition setting.
Parameter Value
Injection pressure/Ambient pressure (bar) 20/4, 50/5, 90/6, 60/3, 80/2, 100/1
NHD (mm) 1
AT (K) 300
F. Xie et al.                                                                                                                                                                                                                                       Applied Thermal Engineering 280 (2025) 128523 
6

<!-- PDF_PAGE: 7 -->

recirculation or stabilized jet contour is observed at this stage. As the 
NPR increases to 10 – 20, the jet boundary begins to exhibit clear con -
centration gradients and shear layers. The mass fraction contours 
become more defined and saturated, with the outer edges forming 
distinct “ mushroom-cap ” structures. This indicates the onset of shear 
instabilities and the development of small-scale vortical structures. At 
NPRs of 15 and above, secondary vortex structures become apparent, 
particularly at 16 μ s and 20 μ s. Ear-like vortices emerge on both sides of 
the jet front, a typical feature of high-pressure under-expanded jets. 
These structures enhance hydrogen – air mixing by promoting entrain -
ment and instability near the shear layers.
Under even higher NPR conditions (e.g., 40 and 100), the jet exhibits 
typical features of high-Mach-number supersonic flows. The core region 
downstream of the nozzle displays a concentrated mass fraction 
distribution with values exceeding 0.9, indicating near-saturation. 
Intense asymmetric disturbances appear along the jet boundary, 
reflecting vigorous shear layer development and enhanced turbulence. 
Additionally, distinct recirculation vortex rings form in the jet tail, 
driven by the strong momentum injection. These structures entrain 
surrounding low-concentration gas into the high-speed core flow, 
thereby significantly enhancing the mixing efficiency in the near-nozzle 
region.
Fig. 9 illustrates the evolution of Mach number distributions in the 
near-field region of hydrogen jets during the initial injection stage under 
various NPRs. The figure reveals that as NPR increases, significant 
changes occur in the Mach number distribution near the nozzle exit, as 
well as in the shock structures and shear layer development. ( Fig. 10 ).
At NPR = 5, the flow field initially (at 12 μ s) exhibits an axisym -
metric diamond-shaped shock pattern, without a clearly defined normal 
shock (Mach disk), indicating a moderately under-expanded jet state. As 
the jet evolves to 16 – 20 μ s, a weak Mach disk gradually forms, and the 
jet continues downstream along reflected shock waves. Mild distur -
bances arise in the shear layer, inducing weak recirculation structures. 
However, the extent of the mixing region remains limited, and second -
ary vortices do not exhibit strong entrainment behavior.
As NPR increases to the range of 10 – 20, the jet structure transitions 
Fig. 8. Distribution of hydrogen near-field jet mass fraction under different NPRs.
Table 2 
NHD simulation condition setting.
Parameter Value
Injection pressure/Ambient pressure (bar) 50/5
NHD (mm) 0.75, 1, 1.25, 1.5, 2
AT (K) 300
F. Xie et al.                                                                                                                                                                                                                                       Applied Thermal Engineering 280 (2025) 128523 
7

<!-- PDF_PAGE: 8 -->

into a typical highly under-expanded regime. During the 16 – 20 μ s in -
terval, an axisymmetric normal shock (Mach disk) clearly forms down -
stream of the nozzle exit. Upstream of the Mach disk, prominent 
expansion waves develop, and alternating interactions between shocks 
and expansion waves near the jet axis form a characteristic barrel- 
shaped shock structure. Reflected shocks downstream of the Mach 
disk are also observed. At the interface between the main jet and the 
ambient gas, distinct bow shocks are induced [ 33 ], becoming more 
prominent at higher NPRs. Meanwhile, the shear layers develop rapidly, 
accompanied by boundary layer roll-up and the growth of secondary 
vortices triggered by Kelvin – Helmholtz-type instabilities [ 43 ], which 
promote mixing between the high-speed jet and the stationary sur -
rounding gas.
At even higher NPRs (40 and 100), large regions of high Mach 
number flow (Ma > 2.5) emerge immediately during the early injection 
phase. A well-defined Mach disk appears downstream of the nozzle, 
gradually shifting downstream over time. A complete internal shock 
system forms between the nozzle exit and the Mach disk, featuring 
repeated interactions between expansion and compression waves. 
Strong shear shocks are observed along the outer edge of the barrel 
structure, where intensified velocity gradients result in highly developed 
shear layers. Vortex structures rapidly grow and evolve into multi-scale 
vortices, creating strong entrainment interfaces and enhancing mixing. 
In addition, interactions between shock structures and unstable shear 
layers lead to more complex flow patterns, such as shock interaction 
zones formed by collisions between shear shocks and reflected shocks, 
which cause abrupt local variations in the Mach number field. 
Furthermore, at high NPRs, a prominent bow shock envelope forms 
around the entire jet cone during the initial stage and gradually expands 
over time. This structure acts as a wide leading shock front, exerting a 
precursor compression effect on the far-field ambient gas. The fitting 
results of the Mach disk height with respect to nozzle pressure ratio 
(NPR) indicate that its evolution can be well approximated by a power- 
law function of the form L
m
/ D = aPr
b
, where L
m 
is the Mach disk 
location, D is the nozzle diameter, and Pr is the NPR. According to the 
study by Franquet et al. [ 28 ], when the fitting constants a = 0.6454 and 
b ¼ 0.5, the empirical correlation effectively describes the evolution of 
Mach disk position in under-expanded gas jets. In the present study, the 
best-fit values of a = 0.6361 and b ¼ 0.5076 yielded a close approxi -
mation of the near-field Mach disk position for hydrogen jets, showing 
excellent agreement in both accuracy and trend with the literature, 
thereby confirming that the proposed model reliably captures the NPR- 
Fig. 9. Mach number distribution of hydrogen near-field jet at different NPRs.
R2=0.9993
R2=0.9962
y=0.2631x0.6126
Mach disk location
y=0.6361x0.5076
Fit curve
Mach disk diameter
Fit curve
Fig. 10. The position and diameter of the Mach disk at 20 μ s and its fitting 
curve under different NPRs.
F. Xie et al.                                                                                                                                                                                                                                       Applied Thermal Engineering 280 (2025) 128523 
8

<!-- PDF_PAGE: 9 -->

dependent behavior of Mach disk location in under-expanded hydrogen 
jets. This demonstrates the applicability and reference value of the 
empirical formula in representing near-field hydrogen jet characteris -
tics. In contrast, the relationship between the Mach disk diameter and 
NPR shows a notable deviation from Franquet ’ s empirical model. In this 
work, fitting constants of a = 0.2631 and b ¼ 0.6126 provided an ac -
curate representation of the Mach disk diameter under different NPR 
conditions.
Additionally, comparisons between the fitted curves and the 
measured data reveal that at high NPRs, the actual values of both Mach 
disk position and diameter deviate slightly from the fitted results. This 
discrepancy may stem from the complex coupling effects of intense 
shock interactions, the development of secondary vortices, and the 
growth of mixing layers. Therefore, further investigation integrating 
Mach number distributions, turbulence parameters, and velocity fields is 
necessary to reveal the underlying mechanisms governing the nonlinear 
interactions between shock structure evolution and mixing behavior.
Fig. 11 illustrates the mass fraction contours of hydrogen jets at 
representative time instants under different NPRs, ranging from 5 to 
100. It is evident that NPR significantly influences the jet ’ s penetration 
capability, spreading characteristics, and mixing behavior. At the initial 
stage (0.1 ms), jets under high NPR conditions (40 and 100) exhibit 
Fig. 11. Distribution of hydrogen macro jet mass fraction under different NPRs.
F. Xie et al.                                                                                                                                                                                                                                       Applied Thermal Engineering 280 (2025) 128523 
9

<!-- PDF_PAGE: 10 -->

typical features of strongly under-expanded structures. Prominent 
expansion waves and shock patterns are observed near the nozzle exit, 
and complex reflected shocks and shear layer disturbances develop 
throughout the flow field, resulting in highly non-uniform local mass 
fraction distributions. Notably, at NPR = 100, the jet front displays a 
clear “ umbrella-shaped ” spreading pattern, suggesting intense lateral 
diffusion and recirculation. In contrast, jets at lower NPRs show more 
stable morphologies with compact mass fraction iso -contours, forming a 
typical slender conical structure.
As time progresses, the jet continues to propagate downstream. In 
the mid-to-late stages (0.4 – 1.0 ms), high-NPR jets maintain strong axial 
momentum, generating a broader jet region with a noticeably larger 
spreading angle compared to low-NPR conditions. The mass fraction 
contours reveal the formation of a pronounced low-concentration en -
velope around the jet tail under high NPRs, indicating enhanced mixing 
between the hydrogen jet and the surrounding ambient gas.
Fig. 12 presents a quantitative comparison and trend analysis of axial 
penetration distance, radial penetration distance, spray cone angle, and 
spray area of hydrogen jets under six different NPR conditions. In terms 
of axial penetration distance, a significant overall increase is observed 
with rising NPR. Particularly after 0.2 ms, distinct divergence among jets 
with different NPRs becomes evident. Under high NPR conditions, the 
jet front advances rapidly, indicating stronger penetration capability. 
For instance, at NPR = 100, the jet approaches the wall-impingement 
limit by 0.8 ms. For NPRs between 5 and 20, the penetration length 
exhibits a nearly linear growth, while at NPRs of 40 and above, a 
nonlinear acceleration trend is observed.
Radial penetration distance also increases with NPR, with higher 
NPRs leading to more pronounced lateral expansion of the jet. This is 
primarily attributed to the intensified secondary vortex structures 
around the triple point region at higher NPRs, which induce stronger 
entrainment effects and enhance momentum exchange with the sur -
rounding air. After 0.6 ms, jets under high NPR conditions exhibit 
significantly larger radial widths, indicating more developed shear 
layers and enhanced lateral momentum diffusion. For example, at NPR 
= 100, the radial penetration distance exceeds 40 mm at 1.0 ms, which is 
substantially greater than that observed under lower NPRs.
The evolution of spray cone angle exhibits more complexity. In the 
early stage (0.02 ms), flow expansion at the nozzle exit leads to a large 
cone angle due to rapid expansion. This is followed by a sharp 
contraction and stabilization, reflecting the typical “ initial over- 
expansion – shear-induced narrowing – stabilized spreading ” behavior 
of under-expanded jets. After 0.1 ms, the cone angle gradually stabilizes 
over time, with a slight increase under higher NPRs. Notably, NPRs of 40 
and 100 maintain relatively large cone angles even at 1.0 ms. Spray area 
increases significantly with NPR and exhibits a characteristic exponen -
tial growth trend over time. At 1.0 ms, the spray area for NPR = 5 is only 
552 mm
2
, whereas for NPR = 100, it reaches 2907 mm
2 
by 0.8 ms, 
indicating a much stronger jet spreading capability and mixing poten -
tial. Moreover, the growth slope of the area data also increases with 
NPR. For NPRs above 20, the effect becomes particularly pronounced, 
suggesting that the intensified aerodynamic structure associated with 
deeper under-expansion markedly enhances mixing behavior.
Fig. 13(a) presents the evolution of the axial-to-radial penetration 
ratio ( L
z
/ L
r
) as a function of NPR at different time instants. This ratio 
serves as an important parameter for evaluating the jet morphology — -
specifically, its “ slenderness ” or “ expansion capacity ”— and reflects the 
relative dominance of axial penetration versus radial spreading. As 
shown in the figure, the value of L
z
/ L
r 
decreases progressively over time, 
indicating a transition from a jet dominated by strong axial penetration 
to one characterized by enhanced lateral expansion. This trend becomes 
more pronounced after 0.4 ms. Significant differences are also observed 
among the various NPR conditions.
At the initial stage (0.1 ms), all NPR cases exhibit relatively high L
z
/
L
r 
values, suggesting that early jet development is primarily driven by 
injection momentum, resulting in strong axial advancement. As time 
5
10
15
20
40
100
5
10
15
20
40
100
5
10
15
20
40
100
5
10
15
20
40
100
Fig. 12. Evolution of hydrogen jet penetration distance, cone angle and area under different NPRs.
F. Xie et al.                                                                                                                                                                                                                                       Applied Thermal Engineering 280 (2025) 128523 
10

<!-- PDF_PAGE: 11 -->

progresses, the decrease in L
z
/ L
r 
is more rapid under lower NPR con -
ditions. For example, at 1.0 ms, the ratio drops to 3.42 for NPR = 5, 
whereas it remains above 3.1 for NPR = 15 and 20. Additionally, it is 
worth noting that for NPRs of 40 and 100, the L
z
/ L
r 
values are relatively 
low even at 0.1 ms, indicating a local jet behavior characterized by 
diminished axial penetration and enhanced radial spreading. This 
observation is consistent with the rapid broadening of jet boundaries at 
high NPRs.
To further elucidate the macroscopic expansion behavior of 
hydrogen jets under varying NPRs and assess their geometric similarity, 
the axial penetration distances were normalized using a self-similar 
scaling approach in this section. The normalization follows the power- 
law form defined by equation (5) : 
L
z
a
= C
(
t
τ
) n
(5) 
where L
z 
is the axial penetration distance, a is the characteristic length 
scale, t is the jet development time, τ is the characteristic time scale, C 
and n are fitting coefficients representing the growth rate exponent of 
the jet evolution. The characteristic length scale a can be selected as the 
nozzle diameter, the momentum flux characteristic length ( M
n
/ p
b
)
m
, or 
another reference scale. Unlike the nozzle diameter, which represents 
only a geometric feature, the momentum-flux scale integrates the 
combined effects of nozzle diameter, injection pressure, and density, 
thus reflecting the true driving force of the under-expanded jet. In this 
study, a is chosen as the momentum flux characteristic length. The ex -
ponents m and n are taken as 0.267 and 0.474, respectively, which 
closely align with the findings of Ouellette et al.
As shown in Fig. 13(b) , after normalizing the axial penetration dis -
tance by the momentum flux characteristic length, the data from 
different NPR cases exhibit good collapse, indicating strong geometric 
similarity of hydrogen jets across varying NPRs. Within the normalized 
time range of 0.2 to 1.0 ms, the normalized axial distance L
z
/ a grows 
consistently following a power-law trend t
n 
for all cases, with minimal 
deviation between the fitted curves. This demonstrates the effectiveness 
of the chosen normalization scale in describing the jet evolution under 
different NPR conditions. Closer inspection reveals minor discrepancies 
at the initial stage ( t
n 
< 0.4), where jets at lower NPRs (e.g., 5 and 10) 
lag slightly behind those at higher NPRs (e.g., 40 and 100). This is 
attributed to the lower initial momentum in low NPR jets, resulting in 
slower development rates. However, as time progresses, the curves 
converge, indicating that the influence of NPR on the normalized evo -
lution mainly occurs in the early phase. Beyond t
n 
> 0.5, the normalized 
curves for all NPRs nearly overlap, revealing strong self-similarity in the 
jet evolution dynamics.
For the near-field jet structures, the observed growth of Mach disk 
height with NPR follows the classical scaling laws reported by Franquet 
et al. [ 28 ], although our results show slight deviations at very high NPRs 
due to intensified secondary vortex formation and shock – shear in -
teractions unique to hydrogen. This suggests that while the empirical 
correlations developed for generic under-expanded jets remain broadly 
valid, hydrogen-specific instabilities must be considered at engine- 
relevant conditions. Regarding macroscopic penetration behavior, the 
nearly linear growth of axial penetration at moderate NPRs agrees with 
the self-similarity correlations of Ouellette et al. [ 44 ], whereas the 
nonlinear acceleration observed at NPR ≥ 40 highlights the stronger 
expansion and mixing potential of hydrogen compared to methane or 
natural gas jets [15,30] .
3.2. The impact of NHD
This section is based on the simulation results under different NHD 
conditions, combined with key characteristic parameters, to deeply 
analyze the influence of NHD changes on the near-field core area 
structure and far-field macroscopic characteristics of the hydrogen jet. 
The specific working conditions are set as follows:
Fig. 14 illustrates the evolution of near-field mass fraction distribu -
tions of hydrogen jets from 8 to 20 µ s under different NHDs, ranging 
from 0.75 mm to 2 mm, highlighting the significant influence of NHD on 
the initial jet expansion, mixture distribution, and shear layer develop -
ment. As the NHD increases, the hydrogen jets exhibit a stronger 
diffusion tendency, larger lateral envelope, and more pronounced vortex 
structures within the early injection stage. The overall jet morphology 
transitions from a slender column to a mushroom-shaped structure.
Under small NHD conditions (e.g., 0.75 mm), the jet remains rela -
tively narrow throughout the 8 – 20 µ s period. The mixing layer is thin, 
axial penetration is strong, but radial spreading is limited. The under -
developed shear layer hampers the formation of stable recirculation 
zones. In the mass fraction contours, the high-concentration region ap -
pears more concentrated and columnar, with a sharp gradient at the 
outer boundary, indicating a thinner mixing layer and restricted inter -
action between the jet and the ambient gas.
In contrast, jets with moderate NHDs (1.25 – 1.5 mm) exhibit clearly 
distinguishable double-sided vortex roll-up structures by 12 – 16 µ s. The 
jet front shows a symmetrical bulging pattern, and the hydrogen-rich 
core expands significantly. Surrounding this core is a thicker diluted 
5
10
15
20
40
100
5
10
15
20
40
100
Fig. 13. The ratio of axial/radial penetration and self-similarity of axial penetration under different NPRs.
F. Xie et al.                                                                                                                                                                                                                                       Applied Thermal Engineering 280 (2025) 128523 
11

<!-- PDF_PAGE: 12 -->

Fig. 14. Distribution of hydrogen near-field jet mass fraction under different NHDs.
Fig. 15. Mach number distribution cloud of hydrogen near-field jet under different NHDs.
F. Xie et al.                                                                                                                                                                                                                                       Applied Thermal Engineering 280 (2025) 128523 
12

<!-- PDF_PAGE: 13 -->

layer with blurred boundaries, indicating intensified momentum ex -
change and vortex-induced mixing with the surrounding medium. When 
the NHD further increases to 2 mm, the jet undergoes substantial lateral 
expansion, occupying a larger spatial volume. The high-concentration 
hydrogen region becomes the most extensive among the cases, and 
vortex structures appear at an earlier stage.
Fig. 15 presents the Mach number distributions of near-field 
hydrogen jets under different NHDs. The comparison clearly illustrates 
that NHD significantly influences the near-field flow structures, partic -
ularly in terms of Mach disk morphology, shock wave system configu -
ration, shear layer evolution, and the formation of secondary vortex 
structures. Under the smallest NHD condition (0.75 mm), the Mach 
structure exhibits a sharp and compact profile. The shock waves are 
relatively weak, showing only a near-axial bow shock, while the re -
flected waves and shear layers remain underdeveloped. This suggests 
that although the axial velocity of the jet is high, the energy associated 
with compressive wave fluctuations is low, and secondary flow struc -
tures have not yet formed a closed system.
As the NHD increases to 1.0 mm, the barrel-shaped structure begins 
to emerge. The bow shocks expand laterally, and initial reflected shock 
structures form during the 16 – 20 µ s period. The shear layer develops 
further, showing a distinct Mach number discontinuity at the interface. 
With further increases in NHD to 1.25 mm and 1.5 mm, the Mach disk 
shifts forward and becomes more stable. The outer edge of the barrel 
shock becomes more defined, and the bow shocks appear earlier and 
expand over a wider range. At the intersection of the reflected shocks 
and the shear layer, large-scale annular secondary vortices begin to 
form, inducing periodic instability streaks along the jet boundary and 
significantly enhancing turbulence intensity.
Under the largest NHD condition (2.0 mm), the Mach disk expands 
substantially, with a broader high-Mach region and a more complex 
reflected shock system developing along the downstream edge. The 
strongly entrained shear layers cause outward bow shock deflection, 
forming a thick, stable jet structure. Moreover, the larger orifice diam -
eter promotes the generation of multiple annular secondary vortex 
systems, facilitating faster lateral dispersion and recirculating mixing of 
the jet.
In comparison with varying NPR conditions, changes in NHD pri -
marily modulate the spatial configuration of the shock system and the 
morphology of induced vortices. In contrast, NPR more directly in -
fluences the overall jet momentum and shock strength. Specifically, 
increasing NPR enhances the intensity of the Mach disk and broadens 
the high-Mach region. Specifically, increasing the NPR enhances the 
strength of the Mach disk and broadens the high-Mach region. The 
enhancement effect of larger NHDs is mainly reflected in the expansion 
of near-field jet structure volume, increased shear layer thickness, and 
intensified secondary vortices. Therefore, precise matching of NHD and 
NPR is crucial for effective control of the shock system to prevent jet 
instability and uneven mixture formation.
Fig. 16 illustrates the variation in Mach disk position and diameter at 
20 μ s after injection under different NHD conditions. It is evident that 
both the axial position and diameter of the Mach disk increase signifi -
cantly with rising NHD, each following a well-fitted quadratic trend. The 
polynomial fitting equation for the Mach disk position is given by y =
 0 . 61 x
2
+ 3 . 33 x  0 . 66, with a coefficient of determination (R
2
) 
exceeding 0.99, indicating excellent fitting accuracy. For the Mach disk 
diameter, the fitting equation is y =  0 . 39 x
2
+ 1 . 83 x  0 . 51, and while 
the R
2 
value is slightly lower, it still reflects a good level of correlation.
As NHD increases, the mass flow rate and jet momentum rise 
markedly, allowing the shock structure to develop further. Conse -
quently, the Mach disk shifts noticeably downstream, while the shear 
layer intensifies and the location of reflected shock waves extends, 
leading to a concurrent increase in Mach disk diameter. Specifically, 
when NHD increases from 0.75 mm to 2.0 mm, the Mach disk position 
moves from approximately 1.54 mm to 3.62 mm — an increase of over 
135 %. Simultaneously, the diameter expands from about 0.58 mm to 
1.57 mm, reflecting a growth of over 170 %. This trend highlights that 
the injector ’ s geometric configuration directly governs the scale and 
intensity of internal shock structures within the hydrogen jet. It is worth 
noting that, in comparison to the effect of nozzle pressure ratio (NPR), 
the influence of NHD on Mach disk morphology exhibits a smoother and 
more controllable trend. This structural evolution primarily stems from 
the continuous increase in momentum flux, rather than abrupt flow 
regime transitions.
Fig. 17 presents the temporal evolution of hydrogen mass fraction 
distributions from 0.1 ms to 1.0 ms under varying NHD conditions. The 
results clearly demonstrate that the overall penetration capability of the 
hydrogen jet is significantly enhanced with increasing NHD. The 
hydrogen plume extends rapidly in the axial direction, while the radial 
dispersion also becomes more pronounced, indicating a stronger pene -
tration capacity. At the initial stage (0.1 ms), smaller NHDs (0.75 mm 
and 1.0 mm) produce relatively compact hydrogen plumes with local -
ized diffusion characteristics, and the jet structure has not yet stabilized. 
In contrast, when the NHD reaches 1.5 mm or larger, the jet quickly 
develops into a typical plume shape with a distinct high-velocity core 
region. Barrel-shaped shock structures form beneath the injector outlet, 
and the hydrogen mass fraction rapidly reaches its peak value. As the 
injection progresses into the 0.4 ms stage and beyond, jets with larger 
NHDs display a more prominent axial core structure, accompanied by 
well-developed shear layers along the jet boundary. These shear layers 
induce substantial entrainment of ambient gases, thereby significantly 
enhancing the development of the mixing zone. Notably, under the 2.0 
mm NHD condition, the jet exhibits a strong expansion tendency, with 
clearly defined turbulent plume regions forming on both sides of the 
main jet stream. These regions show a wide mixing interface and com -
plex flow structures, indicative of intensified fuel – air mixing processes.
Fig. 18 illustrates the temporal evolution of key macroscopic 
hydrogen jet parameters — including axial penetration distance, radial 
penetration distance, spray cone angle, and spray area — under different 
NHDs of 0.75 mm, 1.0 mm, 1.25 mm, 1.5 mm, and 2.0 mm. For axial 
penetration, all NHD conditions exhibit a rapid increase over time. 
However, larger NHDs (e.g., 1.5 mm and 2.0 mm) consistently result in 
much greater axial penetration at each time step, indicating that NHD 
directly amplifies jet momentum, thereby driving the jet front deeper 
into the chamber. At 1.0 ms, the jet from the 2.0 mm nozzle already 
surpasses the far-wall boundary, showing signs of wall impingement, 
whereas the 0.75 mm case remains in a free-expansion stage. A similar 
trend is observed for radial penetration: as NHD increases, the lateral 
spread becomes broader, particularly when the diameter exceeds 1.5 
mm. This can be attributed to the higher initial mass flow rate and 
momentum flux under larger NHDs, which intensify entrainment and 
mixing with ambient gases.
Mach disk location
Fit curve
y=-0.61x2+3.33x-0.66
R2=0.99067
y=-0.39x2+1.83x-0.51
Mach disk diameter
Fit curve
R2=0.93469
Fig. 16. The position and diameter of the Mach disk at 20 μ s and its fitting 
curve under different NHDs.
F. Xie et al.                                                                                                                                                                                                                                       Applied Thermal Engineering 280 (2025) 128523 
13

<!-- PDF_PAGE: 14 -->

Spray cone angle dynamics show a distinct contraction pattern. In 
the early stages (0.02 – 0.1 ms), all nozzles exhibit relatively large cone 
angles, indicating strong initial expansion. However, as time progresses, 
the cone angles gradually stabilize around 26
◦
, suggesting a transition 
from a free-expansion regime to a quasi-steady state. Notably, for NHDs 
ranging from 1.25 mm to 2.0 mm, the cone angles converge during the 
later stages. Regarding spray area, the jet cross-sectional area increases 
exponentially across all NHDs, especially during the 0.4 – 1.0 ms interval. 
For larger nozzle diameters (e.g., 2.0 mm), the growth rate is particu -
larly pronounced. At 1.0 ms, the spray area for the 2.0 mm NHD exceeds 
1300 mm
2
, while that for 0.75 mm remains around 625 mm
2
— more 
than a twofold difference — highlighting the significant amplification 
effect of NHD on the available fuel – air mixing volume.
As shown in Fig. 19(a) , with increasing time, the ratio of axial to 
radial penetration distance of the hydrogen jet exhibits an overall trend 
of initially high values followed by gradual stabilization. During the 
early stage (t = 0.1 ms), this ratio exceeds 3.6 across all NHDs, reflecting 
a characteristic slender jet structure. As the injection progresses, the 
axial-to-radial ratio gradually declines and stabilizes. For NHDs ranging 
from 0.75 mm to 1.25 mm, the ratio stabilizes between 3.0 and 3.4, 
indicating a relatively stable jet geometry with good geometric self- 
similarity. However, under larger diameters of 1.5 mm and above, the 
ratio decreases more markedly. In particular, the ratio drops to 
approximately 2.64 for the 2.0 mm case at t = 0.8 ms, indicating that 
larger NHDs are more prone to enhanced radial expansion, leading to a 
shift in jet structure from “ axial-dominated ” to a more isotropic 
Fig. 17. Hydrogen macro jet mass fraction distribution under different NHDs.
F. Xie et al.                                                                                                                                                                                                                                       Applied Thermal Engineering 280 (2025) 128523 
14

<!-- PDF_PAGE: 15 -->

expansion mode.
To further investigate the influence of NHD on the axial evolution of 
hydrogen jets, the axial penetration distance at 1.0 ms under each NHD 
condition (denoted as L
z 1
) is selected as the reference length scale. The 
raw data are then normalized using empirical constants C = 0.99 and n =
0.43. Fig. 19(b) presents the normalized penetration distance curves for 
different NHDs. The results show that when NHD is less than 1.5 mm, the 
normalized curves exhibit strong self-similar behavior, particularly for 
t
n 
> 0.66, where all curves converge into a smooth and continuous 
growth trend.
In contrast, for larger NHDs (1.5 mm and 2.0 mm), the normalized 
curves deviate markedly from the smaller-diameter trends after t
n 
> 0.5, 
displaying accelerated axial penetration and increased scatter in the 
normalized profiles. This deviation arises from the interplay of several 
coupled mechanisms: the larger nozzle area increases mass flow rate and 
injection momentum, elevating kinetic energy density in the near-field 
region and amplifying Reynolds stress fluctuations; thicker shear 
layers and enhanced lateral expansion modify entrainment dynamics 
and disrupt classical scaling; stronger interactions between near-field 
shock structures and secondary vortices further alter the axial growth 
pattern; and the longer transition distance from structured near-field jets 
to far-field dispersion introduces temporal nonlinearity. Quantitative 
analysis of axial velocity variance, shear layer thickness, and vortex- 
induced velocity fluctuations supports these observations, confirming 
a “ non-classical ” self-similar behavior for large-diameter jets. These 
findings indicate that self-similarity scaling valid for small and moderate 
NHDs cannot be directly applied to larger diameters, highlighting the 
importance of carefully considering NHD-dependent effects for accurate 
jet modeling and hydrogen injector design, as well as for guiding sub -
sequent experimental and numerical investigations.
With respect to NHD, the finding that larger diameters promote 
stronger lateral dispersion and annular vortex formation is consistent 
with the numerical results of Hamzehloo et al. [ 33 ] and the comparative 
hydrogen – methane study by Duronio et al. [ 30 ]. However, the smoother 
quadratic trend of Mach disk position with NHD observed here differs 
from the more abrupt transitions reported for NPR variation, indicating 
0.75 mm
1 mm
1.25 mm
1.5 mm
2 mm
0.75 mm
1 mm
1.25 mm
1.5 mm
2 mm
0.75 mm
1 mm
1.25 mm
1.5 mm
2 mm
0.75 mm
1 mm
1.25 mm
1.5 mm
2 mm
Fig. 18. Evolution of hydrogen jet penetration distance, cone angle and area under different NHDs.
0.75 mm
1 mm
1.25 mm
1.5 mm
2 mm
0.75 mm
1 mm
1.25 mm
1.5 mm
2 mm
Fig. 19. The ratio of axial/radial penetration and self-similarity of axial penetration under different NHDs.
F. Xie et al.                                                                                                                                                                                                                                       Applied Thermal Engineering 280 (2025) 128523 
15

<!-- PDF_PAGE: 16 -->

that geometric scaling provides a more predictable means of controlling 
hydrogen jet morphology.
3.3. The impact of AT
Studying the mechanism of the effect of AT on the structure and 
diffusion behavior of hydrogen jet is of great significance for revealing 
the law of mixture formation and guiding the optimization of actual in- 
cylinder direct injection strategy. The specific AT condition settings of 
this section are shown in Table 3 .
Fig. 20 presents the evolution of hydrogen jet mass fraction distri -
bution in the near-field region (8–20 µs) under different AT conditions 
ranging from 300 K to 800 K. Overall, the jets at the initial stage (8 µs) 
exhibit strong consistency across all AT cases: the flow structures are 
typically axisymmetric, with high hydrogen mass fraction concentrated 
in the core region. The jet boundaries appear relatively distinct, indi -
cating that in the early stage of injection, AT has not yet exerted a sig -
nificant influence on the jet structure or mixing characteristics. The 
primary differences lie in the magnitude of the concentration distribu -
tion rather than in the morphological features.
As injection time progresses, the influence of AT becomes increas -
ingly evident, primarily reflected in the formation and evolution of 
secondary vortical structures, axial development capacity of the jet, and 
the morphology of the mass fraction distribution. Specifically, under 
lower AT conditions (300–400 K), the jet exhibits relatively slow axial 
propagation, while maintaining strong lateral dispersion. The core re -
gion shows high mass fraction but broader overall contours, with pro -
nounced boundary disturbances—indicative of active instability 
characteristics. As AT increases to 500–600 K, the irregular boundary 
disturbances tend to weaken, and the jet structure transitions toward a 
more elongated shape. During 12–16 µs, large and symmetric secondary 
vortices appear, suggesting that elevated AT enhances shear-layer dis -
turbances, thereby promoting the more complete development of the 
near-field mixing layer. In this stage, the high-concentration region re -
mains axially dominant, and the jet exhibits stronger structural 
coherence.
At high AT conditions (700–800 K), the mixing intensity is further 
enhanced. Especially in the 16–20 µs phase, vortex structures become 
more prominent, with boundaries showing characteristic entrainment 
and roll-up features. Localized structural disturbances become more 
intense, indicating that under high-temperature conditions, both the 
growth rate and amplitude of shear instabilities increase markedly. 
Additionally, the axial growth rate of high mass fraction zones is 
significantly accelerated, with an enlarged axial coverage for the same 
concentration thresholds.
It is worth noting that, compared with the pronounced influence of 
injection pressure on jet structure and evolution, the modulation effect 
of AT is relatively limited. Although elevated AT facilitates the forma -
tion of unstable boundary structures and promotes mixing layer devel -
opment, its impact on the momentum propagation path and velocity 
field structure in the core jet region is comparatively minor—far less 
significant than the enhancements in jet momentum and shock structure 
evolution induced by variations in injection pressure.
Fig. 21 displays the evolution of Mach number distributions in the 
near-field region (8–20 µs) of hydrogen jets under AT conditions ranging 
from 300 K to 800 K. The figure reveals the influence of thermal envi -
ronment on the flow field structure, shock wave system, and the 
development of shear layer instabilities in high-pressure gas jets. 
Overall, hydrogen jets under all AT conditions exhibit typical under- 
expanded characteristics, and rising AT influences both the scale and 
evolution rate of shock structures to a certain extent. At the initial stage 
(8 µs), distinct Mach disk structures are observed along the jet centerline 
for all AT levels, accompanied downstream by bow shocks and classic 
barrel-shaped shock systems in an axisymmetric layout. At this phase, 
the peak Mach number regions are highly concentrated, the jet mo -
mentum has not yet dissipated significantly, and the shock boundaries 
remain smooth—indicating that inertial effects dominate in early in -
jection, with AT exerting only a limited influence on shock formation. 
Notably, in the low-temperature group (300–400 K), the Mach disks 
appear shorter with weaker shock strength, and the main jet shows a 
larger expansion angle. The velocity gradient across the shear layer is 
relatively small, and asymmetric instability structures have not yet 
developed.
As the jet progresses to 12–16 µs, shear layer disturbances gradually 
intensify. Particularly in the medium-to-high AT group (500–700 K), the 
Mach disk extends further downstream, the bow shock becomes less 
distinct, and secondary expansion waves as well as interference patterns 
from reflected shocks appear. Additionally, across all AT conditions, 
vortex structures begin to emerge outside the barrel shock, aligned along 
the shear layer. These vortices display a relatively symmetric distribu -
tion at the jet boundary, forming secondary vortical structures. Espe -
cially at 600–700 K, the shear layer experiences stronger perturbations, 
and the scale of secondary vortices increases. By 20 µs, in the high- 
temperature group (700–800 K), the jet’s shock system has evolved 
into a highly complex structure. Regions beyond the main Mach zone 
undergo structural disintegration, generating multiple high-Mach- 
number “entrainment structures” and disturbance waves. The bound -
aries exhibit irregular rolling patterns, reflecting the intensification of 
shock–vortex interactions. Furthermore, the axial high-Mach region 
continues to extend, the velocity gradient along the centerline remains 
high, and the shear layers are strongly perturbed and entrained into the 
vortex region. In contrast, under low-temperature conditions, the shock 
system retains a relatively regular structure at the same time scale, and 
the development of secondary structures is more delayed.
Fig. 22 presents the quantitative variation trends of the Mach disk 
position and diameter in hydrogen jets at 20 µs under different AT 
conditions. Overall, although both the axial position and radial diameter 
of the Mach disk exhibit slight fluctuations with changing AT, the 
magnitude of variation remains small and confined within a narrow 
range, indicating pronounced stability. This outcome suggests that, 
under fixed injection pressure and nozzle geometry, the influence of AT 
on the geometric characteristics of the near-field Mach disk is relatively 
limited.
Specifically, the Mach disk position (left axis) fluctuates within a 
range of approximately 2.04–2.10 mm as AT increases from 300 K to 
800 K, showing a non-monotonic trend: it first increases gradually to a 
peak (around 2.10 mm), then slightly declines and stabilizes. In contrast, 
the Mach disk diameter (right axis) decreases slightly with increasing 
AT, with a maximum variation of about 0.25 mm, remaining consis -
tently within the range of 0.85–1.10 mm. This phenomenon can be 
attributed to the fact that while AT may alter the density and viscosity 
characteristics of the surrounding gas, thus affecting the development of 
boundary shear layers and the interference of shock structures, its in -
fluence on the axial momentum transport of the main jet and the spatial 
confinement of shock structures is relatively weak. Consequently, it does 
not significantly drive dimensional changes in the core Mach disk 
structure.
Fig. 23 illustrates the hydrogen mass fraction distribution contours at 
representative time points under various AT conditions. It can be 
observed that, at the same stage of jet development, hydrogen jets 
exhibit stronger axial expansion with increasing AT, as evidenced by the 
extended leading-edge propagation distance and an overall outward- 
spreading jet morphology. Under lower AT conditions (300–400 K), 
the hydrogen jet appears concentrated and relatively slender, with a 
Table 3 
AT simulation condition setting.
Parameter Value
Injection pressure/Ambient pressure (bar) 50/5
NHD (mm) 1
AT (K) 300, 400, 500, 600, 700, 800
F. Xie et al.                                                                                                                                                                                                                                       Applied Thermal Engineering 280 (2025) 128523 
16

<!-- PDF_PAGE: 17 -->

compact main jet structure and limited axial penetration distance. The 
jet boundary remains well-defined, and radial expansion is restricted, 
with hydrogen primarily distributed along a narrow region close to the 
nozzle axis. As AT rises to 500 – 800 K, the jet front becomes increasingly 
diffuse, and both axial and radial expansion become more pronounced. 
The jet structure broadens significantly, resulting in a more uniform 
distribution of hydrogen over a larger spatial domain. This shift in -
dicates that high-temperature environments markedly enhance hydro -
gen ’ s transport and mixing capabilities with the ambient gas. The 
underlying mechanisms are as follows: first, elevated temperatures 
reduce the background gas density, thereby decreasing resistance during 
jet penetration and allowing higher flow velocities to be maintained. 
Second, the binary diffusion coefficient increases with temperature, 
accelerating the migration rate of hydrogen molecules in the ambient 
medium and leading to a smoother concentration gradient. Additionally, 
high temperatures increase the viscosity of the background gas, which 
enhances the turbulence intensity induced by the jet, further promoting 
radial dispersion and mixing.
To comprehensively analyze the influence of AT on the injection 
characteristics of hydrogen jets, macroscopic parameters including axial 
penetration distance, radial penetration distance, spray cone angle, and 
jet area were extracted under various AT conditions ranging from 300 K 
to 800 K. The results are shown in Fig. 24 . Overall, the penetration 
distances increased rapidly with jet development time, exhibiting a clear 
nonlinear growth trend. It can be observed that, at the same develop -
ment time, the jet front propagation distance increases gradually with 
Fig. 20. Distribution of hydrogen near-field jet mass fraction under different ATs.
F. Xie et al.                                                                                                                                                                                                                                       Applied Thermal Engineering 280 (2025) 128523 
17

<!-- PDF_PAGE: 18 -->

rising AT, indicating enhanced penetration capability along the jet axis. 
For example, at 1 ms, the axial penetration distance increases from 
77.65 mm (300 K) to 90.21 mm (800 K), corresponding to a growth of 
approximately 16 %. Similarly, the radial penetration distance also in -
creases with time, with more pronounced radial expansion under higher 
AT conditions. At 300 K, the radial expansion is relatively slow, limited 
by weaker molecular diffusion and lower turbulence intensity; whereas 
at 800 K, the radial extent significantly enlarges, reflecting the strong 
diffusion and good mixing characteristics of hydrogen in a high-AT 
background gas.
It is also observed that the spray cone angle is relatively large during 
the initial injection period (0 – 0.1 ms), then tends to stabilize. Across 
different time points, the spray cone angle does not show a strong reg -
ular pattern with increasing AT. This complexity may result from 
changes in turbulence shear effects induced by the variation of back -
ground gas viscosity with AT, leading to a complicated response of the 
spray cone angle. Regarding the spray area, the results indicate that in 
the early stage of jet development (t ≤ 0.2 ms), differences in spray area 
among different AT conditions are not significant. This is mainly because 
the jet is still in the initial development phase, with hydrogen not yet 
forming a distinct diffusive pattern and momentum not fully developed. 
However, in the subsequent middle and late stages (t ≥ 0.4 ms), the 
spray area increases at a faster rate with time, and the growth magnitude 
is larger at higher AT. Notably, under the 800 K high-AT condition, the 
spray area at 1.0 ms reaches 1.5 times that under room temperature 
(300 K), demonstrating the strong promotion effect of a high-AT envi -
ronment on the lateral expansion and outward spreading capability of 
the hydrogen jet.
Fig. 25(a) shows the variation of the ratio of axial to radial pene -
tration distances ( L
z
/ L
r
) of the hydrogen jet at different injection times 
as a function of AT. From the data, it is evident that under all AT con -
ditions, the L
z
/ L
r 
ratio gradually decreases with increasing injection 
Fig. 21. Mach number distribution cloud of hydrogen near-field jet under different ATs.
Mach disk location
Mach disk diameter
Fig. 22. The position and diameter of the Mach disk at 20 μ s and its fitting 
curve under different ATs.
F. Xie et al.                                                                                                                                                                                                                                       Applied Thermal Engineering 280 (2025) 128523 
18

<!-- PDF_PAGE: 19 -->

time. This indicates that during the early injection stage (t ≤ 0.2 ms), the 
hydrogen jet predominantly propagates axially at high velocity, exhib -
iting a “ slender columnar ” structure. In the later injection stage (t ≥ 0.6 
ms), due to the reduction in jet velocity, enhanced turbulence devel -
opment, and intensified gas mixing, the radial expansion becomes more 
pronounced, leading to a decline in L
z
/ L
r 
and resulting in a more 
expanded and stabilized jet morphology.
In this section, the reference scale is chosen as the axial penetration 
distance at 1 ms, L
z 1
, with constants C = 1.02 and n = 0.44 providing 
good self-similarity. Fig. 25(b) presents the normalized axial penetration 
distance evolution over time. It can be observed that under different AT 
conditions (300 – 800 K), the normalized curves show a high degree of 
consistency throughout the injection process. Especially for normalized 
times t
n 
≥ 0.4, the curves nearly overlap across all temperatures, 
forming a smooth and continuous growth trend. This demonstrates that 
although significant differences exist in the absolute values of L
z 
at 
various ATs, their growth trends and expansion rates exhibit good self- 
similar characteristics.
During the early injection period ( t
n 
≤ 0.2), slight dispersion exists 
among the curves, with the 300 – 400 K cases showing somewhat slower 
growth compared to higher AT conditions, indicating that high AT fa -
vors increased initial jet velocity and slightly faster axial propagation. As 
injection proceeds, jet morphology under all conditions stabilizes, and 
the L
z 
growth curves rapidly converge, enhancing self-similarity. This 
phenomenon suggests that after normalization, despite the significant 
impact of AT on absolute penetration distances, the axial propagation of 
hydrogen jets displays good geometric similarity with a unified scaling 
evolution law. It implies that the macroscopic evolution process of this 
Fig. 23. Hydrogen macro jet mass fraction distribution under different ATs.
F. Xie et al.                                                                                                                                                                                                                                       Applied Thermal Engineering 280 (2025) 128523 
19

<!-- PDF_PAGE: 20 -->

type of under-expanded, high-speed hydrogen jet is governed by 
consistent mechanisms such as momentum transport under different 
thermodynamic conditions, with temperature primarily affecting the 
velocity magnitude rather than the propagation mode.
Although the present study provides detailed insights into the 
coupling between near-field shock structures and far-field spray devel -
opment of under-expanded hydrogen jets, several limitations should be 
acknowledged. First, the near-field LES resolution, while sufficiently 
fine to resolve major shock and vortex interactions, may not fully cap -
ture all small-scale turbulent structures. Second, chemical reactions 
were not considered, and the analysis therefore focuses solely on 
mixture formation rather than reactive combustion processes. Third, the 
assumption of axisymmetric boundary conditions may introduce un -
certainties at very late jet development stages, where three-dimensional 
flow interactions could become more pronounced. These limitations will 
be addressed in future work through higher-resolution simulations and 
coupled combustion modeling.
4. Conclusion
This study systematically investigated the under-expanded hydrogen 
jet behavior relevant to HDI engines by employing a dual-scale analyt -
ical framework that combined constant-volume vessel experiments with 
high-fidelity numerical simulations. The effects of NPR, NHD, and AT on 
both near-field shock structures and far-field spray evolution were 
comprehensively analyzed. The key conclusions are summarized as 
follows: 
(1) Near-field shock structures under high NPR: Experiments 
demonstrated that hydrogen jets at elevated NPR conditions 
exhibit pronounced under-expanded features. Compared with 
low-NPR jets, the Mach disk becomes more elongated and 
distinct, reflecting stronger expansion and recompression down -
stream of the nozzle. Nevertheless, due to the inherent unstead -
iness of hydrogen jets and optical distortion induced by turbulent 
300 K
400 K
500 K
600 K
700 K
800 K
300 K
400 K
500 K
600 K
700 K
800 K
300 K
400 K
500 K
600 K
700 K
800 K 300 K
400 K
500 K
600 K
700 K
800 K
Fig. 24. Evolution of hydrogen jet penetration distance, cone angle and area under different ATs.
300 K
400 K
500 K
600 K
700 K
800 K
300 K
400 K
500 K
600 K
700 K
800 K
Fig. 25. The ratio of axial/radial penetration and self-similarity of axial penetration under different ATs.
F. Xie et al.                                                                                                                                                                                                                                       Applied Thermal Engineering 280 (2025) 128523 
20

<!-- PDF_PAGE: 21 -->

mixing, precise identification of fine shock structures in experi -
ments remains challenging.
(2) NPR as the dominant factor: NPR strongly governs jet momentum 
and morphology. Higher NPR results in significantly increased jet 
velocity, intensified shock structures, an extended potential core, 
and enhanced entrainment driven by recirculating vortices near 
the jet tail. Consequently, axial velocity decays more slowly, 
radial dispersion is reinforced, and the overall spray assumes a 
broader, more expanded structure.
(3) Role of nozzle hole diameter: NHD critically regulates shear 
characteristics and dispersion. Larger orifices increase near-field 
jet volume, thicken shear layers, and promote secondary vortex 
formation, thereby enhancing turbulent mixing. Both axial and 
radial penetration, as well as spray area, increase with NHD, 
although a saturation tendency appears at larger diameters, 
indicating nonlinear effects and edge limitations.
(4) Effect of ambient temperature: AT exerts a secondary yet non- 
negligible influence. Higher AT promotes boundary-layer insta -
bility, accelerates shock evolution, and strengthens shear-layer 
growth, leading to increased spray angle and area. However, 
the modulation of jet momentum and axial velocity profiles by AT 
is limited compared to the pronounced effects of NPR and NHD.
(5) Interplay of NPR, NHD, and AT: The combined influence of these 
parameters governs the overall jet evolution. NPR primarily 
dictates momentum and shock structures, NHD controls shear 
instabilities and dispersion scale, while AT modulates boundary 
instabilities. Their interplay shapes hydrogen jet behavior across 
both near-field and far-field regions.
(6) Implications for HDI engines: The proposed dual-scale framework 
effectively links near-field dynamics (shock structures and shear 
instabilities) with far-field spray development, offering new in -
sights into hydrogen mixture formation. The findings highlight 
that (i) high NPR enhances penetration and promotes mixing but 
requires careful control to avoid excessive jet impingement; (ii) 
appropriate nozzle sizing balances penetration depth with lateral 
dispersion; and (iii) elevated ambient temperature supports faster 
mixing without fundamentally altering jet momentum. These 
insights provide theoretical guidance for tailoring injection stra -
tegies and optimizing mixture distribution in HDI engines, ulti -
mately contributing to improved combustion stability and 
efficiency.
CRediT authorship contribution statement
Fangxi Xie: Resources, Project administration. Zhendong Liang: 
Writing – review & editing, Writing – original draft. Bo Cui: Formal 
analysis, Data curation. Wenjun Guo: Funding acquisition, Conceptu -
alization. Xiaoping Li: Validation, Software. Beiping Jiang: Funding 
acquisition, Formal analysis. Zhe Zhao: Resources, Project administra -
tion. Xiangyang Wang: Resources, Project administration.
Declaration of competing interest
The authors declare that they have no known competing financial 
interests or personal relationships that could have appeared to influence 
the work reported in this paper.
Acknowledgments
This work is supported financially by the National Natural Science 
Foundation of China (Grant No. 52476117), the Scientific and Techno -
logical Developing Scheme of Jilin Province (Grant No. 
20240101140JC), and the Changchun Scientific and Technological 
Development Program (Grant No. 23GZZ20).
Appendix A. Supplementary data
Supplementary data to this article can be found online at https://doi. 
org/10.1016/j.applthermaleng.2025.128523 .
Data availability
The data that has been used is confidential.
References
[1] W. Chen, C. Lu, Q. Zuo, C. Kou, R. Shi, H. Wang, et al., Combustion characteristics 
analysis and performance evaluation of a hydrogen engine under direct injection 
plus lean burn mode, J. Clean. Prod. 470 (2024), https://doi.org/10.1016/j. 
jclepro.2024.143323.
[2] Z. Liang, F. Xie, B. Jiang, X. Li, Y. Su, Z. Wang, Evaluating the potential of mixture 
formation methods to achieve efficient combustion and near-zero emissions on a 
hydrogen direct injection engine, J. Clean. Prod. 439 (2024) 140930, https://doi. 
org/10.1016/j.jclepro.2024.140930.
[3] S. Guo, H. Meng, Q. Zhan, C. Ji, D. Wang, In-depth analysis of the key combustion 
parameters in the hydrogen-fueled Wankel rotary engine, Int. J. Hydrogen Energy 
100 (2025) 58–66, https://doi.org/10.1016/j.ijhydene.2024.12.325.
[4] Z. Liang, F. Xie, K. Lai, H. Chen, J. Du, X. Li, Study of single and split injection 
strategies on combustion and emissions of hydrogen DISI engine, Int. J. Hydrogen 
Energy 49 (2023) 1087–1099, https://doi.org/10.1016/j.ijhydene.2023.10.060.
[5] B. Sun, L. Bao, Q. Luo, Development and trends of direct injection hydrogen 
internal combustion engine technology, J Automot. Saf. Energy 12 (2021) 
265–278, https://doi.org/10.3969/j.issn.1674-8484.2021.03.001.
[6] Zhang S wei, Sun B gang, Luo Q he, Bao L zhi. Experimental evaluation of pre- 
ignition and multi-objective optimal controlling of turbocharged direct injection 
hydrogen engines under high-load and high-speed conditions using Taguchi and 
TOPSIS methods. Energy Convers. Manag. 2025;325. Doi: 10.1016/j. 
enconman.2024.119378.
[7] Z. Liang, F. Xie, Z. Wang, C. Lu, Y. Su, X. Li, et al., Suppressing pre-ignition and 
knock in hydrogen direct injection spark ignition engines with variable valve 
timing and split injection, Energy Convers. Manag. 327 (2025) 119570, https:// 
doi.org/10.1016/j.enconman.2025.119570.
[8] Z. Wang, Y. Chen, Q. Li, X. Tang, Z. Yang, D. Wang, et al., Impact of hydrogen- 
injected parameters on the stratified air-fuel mixture formation and combustion of 
the direct injection hydrogen engine, Energy Convers. Manag. 321 (2024) 119083, 
https://doi.org/10.1016/j.enconman.2024.119083.
[9] M. Hafis, K. Balaji, N. Tamilarasan, D. Senthilkumar, R. Sakthivel, A review on 
alternative fuels: spray characteristics, engine performance and emissions effect, 
Sustain Futur. 9 (2025), https://doi.org/10.1016/j.sftr.2025.100456.
[10] Y. Ki, H. Yang, J.J. Kim, Lee S. young, J. Hwang, C. Bae, Stratified hydrogen 
combustion with various mixing processes, Int. J. Hydrogen Energy 169 (2025) 
151170, https://doi.org/10.1016/j.ijhydene.2025.151170.
[11] S. Liu, J. Zhang, J. Xue, M. Chen, L. Dai, Z. Yin, Optical test devices and methods 
for internal combustion engines and optical studies on spray combustion 
characteristics for three different alternative fuels : a review, J. Energy Inst. 117 
(2024) 101845, https://doi.org/10.1016/j.joei.2024.101845.
[12] E. Hu, S. Huang, J. Ku, Z. Huang, Combustion characteristics of natural gas injected 
into a constant volume vessel, Fuel 235 (2019) 1146–1158, https://doi.org/ 
10.1016/j.fuel.2018.08.101.
[13] Q. Dong, Y. Li, E. Song, L. Fan, C. Yao, J. Sun, Visualization research on injection 
characteristics of high-pressure gas jets for natural gas engine 2018,132, pp. 
165–73.
[14] Y. Lei, J. Liu, T. Qiu, Y. Li, Y. Wang, B. Wan, et al., Gas jet flow characteristic of 
high-pressure methane pulsed injection of single-hole cylindrical nozzle, Fuel 257 
(2019) 116081, https://doi.org/10.1016/j.fuel.2019.116081.
[15] Z. Ni, Q. Dong, D. Wang, X. Yang, Visualization research of natural gas jet 
characteristics with ultra-high injection pressure, Int. J. Hydrogen Energy 47 
(2022) 32473–32492, https://doi.org/10.1016/j.ijhydene.2022.07.132.
[16] L. Lu, Y. Pei, J. Qin, Z. Peng, Y. Wang, K. Zhong, Experimental study on spatial 
distribution characteristics of cylinder-wall oil films under fuel spray impinging 
condition of GDI engine, Energy 254 (2022), https://doi.org/10.1016/j. 
energy.2022.124381.
[17] X. Wang, X. Chang, J. Liu, J. Gao, J. Wu, H. He, Experimental investigation of high- 
pressure methanol spray characteristics for engines, Appl. Therm. Eng. 271 (2025), 
https://doi.org/10.1016/j.applthermaleng.2025.126388.
[18] Y. Zhang, Y. Su, X. Li, F. Xie, H. Yu, B. Shen, et al., Study and prediction on 
macroscopic characteristics of free spray of typical alcohol fuels through 
experimentation and the artificial neural network, Energy 316 (2025), https://doi. 
org/10.1016/j.energy.2025.134610.
[19] Y. Zhang, Y. Su, X. Li, F. Xie, Y. Wang, B. Shen, et al., Modeling of spray 
characteristics of alcohol fuels using response surface methodology and artificial 
neural networks, Fuel 392 (2025), https://doi.org/10.1016/j.fuel.2025.134936.
[20] X. Chen, W. Long, C. Ma, P. Dong, Z. Zhang, J. Tian, et al., Experimental and 
modeling study on liquid phase ammonia spray characteristics under high-pressure 
injection and engine-like ambient conditions. Int Commun, Heat Mass Transf. 164 
(2025), https://doi.org/10.1016/j.icheatmasstransfer.2025.108853.
F. Xie et al.                                                                                                                                                                                                                                       Applied Thermal Engineering 280 (2025) 128523 
21

<!-- PDF_PAGE: 22 -->

[21] S. Verhelst, T. Wallner, Hydrogen-fueled internal combustion engines, Prog. 
Energy Combust. Sci. 35 (2009) 490–527, https://doi.org/10.1016/j. 
pecs.2009.08.001.
[22] H. Meng, Q. Zhan, C. Ji, J. Yang, S. Wang, Identification, prediction and 
classification of hydrogen-fueled Wankel rotary engine knock by data-driven based 
on combustion parameters, Energy 308 (2024), https://doi.org/10.1016/j. 
energy.2024.133029.
[23] K. Wang, C. Li, W. Jia, Y. Chen, J. Wang, Under-expanded jet and diffusion 
characteristics for small-hole leakage of hydrogen-blended natural gas in high- 
pressure pipelines, Process Saf. Environ. Prot. 190 (2024) 195–211, https://doi. 
org/10.1016/j.psep.2024.07.045.
[24] A. Ballatore, J.A. van Oijen, Pressure-based large-eddy simulation of under- 
expanded hydrogen jets for engine applications, Int. J. Hydrogen Energy 49 (2024) 
771–783, https://doi.org/10.1016/j.ijhydene.2023.09.062.
[25] G. Caramia, R. Amirante, P. De Palma, Unsteady RANS simulations of under- 
expanded hydrogen jets for internal combustion engines, Int. J. Hydrogen Energy 
96 (2024) 849–859, https://doi.org/10.1016/j.ijhydene.2024.11.242.
[26] B.R. Petersen, J.B. Ghandhi, Transient high-pressure hydrogen jet measurements, 
SAE Tech Pap (2006), https://doi.org/10.4271/2006-01-0652.
[27] A. Hamzehloo, P.G. Aleiferis, Numerical modelling of transient under-expanded 
jets under different ambient thermodynamic conditions with adaptive mesh 
refinement, Int. J. Heat Fluid Flow 61 (2016) 711–729, https://doi.org/10.1016/j. 
ijheatfluidflow.2016.07.015.
[28] E. Franquet, V. Perrier, S. Gibout, P. Bruel, Free underexpanded jets in a quiescent 
medium: a review, Prog. Aerosp. Sci. 77 (2015) 25–53, https://doi.org/10.1016/j. 
paerosci.2015.06.006.
[29] X. Wang, Sun B. gang, Luo Q. he, Bao L. zhi, Su J. ye, J. Liu, et al., Visualization 
research on hydrogen jet characteristics of an outward-opening injector for direct 
injection hydrogen engines, Fuel 280 (2020) 118710, https://doi.org/10.1016/j. 
fuel.2020.118710.
[30] F. Duronio, A. De Vita, CFD analysis of hydrogen and methane turbulent 
transitional under-expanded jets, Int. J. Heat Fluid Flow 107 (2024) 109381, 
https://doi.org/10.1016/j.ijheatfluidflow.2024.109381.
[31] A. Hamzehloo, P. Aleiferis, Numerical modelling of mixture formation and 
combustion in DISI hydrogen engines with various injection strategies, SAE Tech 
Pap. 2014 (2014), https://doi.org/10.4271/2014-01-2577.
[32] A. Hamzehloo, P.G. Aleiferis, Large eddy simulation of highly turbulent under- 
expanded hydrogen and methane jets for gaseous-fuelled internal combustion 
engines, Int. J. Hydrogen Energy 39 (2014) 21275–21296, https://doi.org/ 
10.1016/j.ijhydene.2014.10.016.
[33] A. Hamzehloo, P.G. Aleiferis, Gas dynamics and flow characteristics of highly 
turbulent under-expanded hydrogen and methane jets under various nozzle 
pressure ratios and ambient pressures, Int. J. Hydrogen Energy 41 (2016) 
6544–6566, https://doi.org/10.1016/j.ijhydene.2016.02.017.
[34] F. Chen, A. Allou, Q. Douasbin, L. Selle, J.D. Parisse, Influence of straight nozzle 
geometry on the supersonic under-expanded gas jets, Nucl. Eng. Des. 339 (2018) 
92–104, https://doi.org/10.1016/j.nucengdes.2018.09.003.
[35] W. Kirchweger, R. Haslacher, M. Hallmannsegger, U. Gerke, Applications of the LIF 
method for the diagnostics of the combustion process of gas-IC-engines, Exp. Fluids 
43 (2007) 329–340, https://doi.org/10.1007/s00348-007-0287-1.
[36] S. Lee, G. Kim, C. Bae, Behavior of hydrogen hollow-cone spray depending on the 
ambient pressure, Int. J. Hydrogen Energy 46 (2021) 4538–4554, https://doi.org/ 
10.1016/j.ijhydene.2020.11.001.
[37] C. Coratella, A. Tinchon, R. Oung, L. Doradoux, G. Dober, C. Hespel, et al., 
Experimental characterization of a hydrogen hollow cone jet at under-expanded 
conditions via schlieren technique, Int. J. Hydrogen Energy 72 (2024) 730–743, 
https://doi.org/10.1016/j.ijhydene.2024.05.411.
[38] B. Wang, F. Xie, W. Hong, J. Du, H. Chen, Y. Su, The effect of structural parameters 
of pre-chamber with turbulent jet ignition system on combustion characteristics of 
methanol-air pre-mixture, Energy Convers Manag 274 (2022) 116473, https://doi. 
org/10.1016/j.enconman.2022.116473.
[39] Y. Liu, Y. Liu, F. Xie, Y. Su, Z. Wang, B. Wang, et al., Optical investigation of the 
influence of high-reactivity iso-octane turbulent jet ignition on the combustion 
characteristics of ammonia/air mixtures, Appl. Therm. Eng. 242 (2024) 122489, 
https://doi.org/10.1016/j.applthermaleng.2024.122489.
[40] Z. Liang, F. Xie, Z. Guo, Z. Wang, H. Dou, B. Wang, et al., Optimization and 
prediction of a novel preignition in hydrogen direct injection engines through 
experimentation and the Random forest algorithms, Energy Convers Manag 313 
(2024) 118602, https://doi.org/10.1016/j.enconman.2024.118602.
[41] F. Xie, Z. Liang, B. Cui, W. Guo, X. Li, B. Jiang, et al., Spray-to-combustion 
interaction in hydrogen direct injection engines: effects of injector structure and 
injection pressure, Energy 333 (2025) 137514, https://doi.org/10.1016/j. 
energy.2025.137514.
[42] Z. Liang, F. Xie, Q. Li, Y. Su, Z. Wang, H. Dou, et al., Co-optimization and 
prediction of high-efficiency combustion and zero-carbon emission at part load in 
the hydrogen direct injection engine based on VVT, split injection and ANN, 
Energy 308 (2024) 133038, https://doi.org/10.1016/j.energy.2024.133038.
[43] M. Kumar, R. Asthana, Z. Uddin. Nonlinear Study of Kelvin-Helmholtz instability of 
cylindrical flow with mass and heat transfer, 2016, 71, pp. 216–24.
[44] Hill PG, Ouellette P. Transient Turbulent Gaseous Fuel Jets for Diesel Engines 
1999;121:93–101.
F. Xie et al.                                                                                                                                                                                                                                       Applied Thermal Engineering 280 (2025) 128523 
22
