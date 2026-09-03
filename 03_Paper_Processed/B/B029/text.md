<!-- PDF_PAGE: 1 -->

Effect of the Injector Pressure-Building Process on Dynamic Gas
Flow Characteristics of a Highly Turbulent Underexpanded
Hydrogen Jet from a Single-Hole Cylindrical Injector
Hailang Sang, Yu Ye, Yan Lei,* Zhenru Zhu, Chuanfu Kou, Xing Liu, and Tao Qiu
Cite This: ACS Omega 2026, 11, 24028−24040
 Read Online
ACCESS
Metrics & More
 Article Recommendations
ABSTRACT: High-pressure hydrogen direct injection (DI)
technology demonstrates significant potential for high thermal
efficiency and ultralow emissions in engines. The hydrogen gas jet
at an elevated nozzle pressure ratio (NPR) exhibits turbulent
underexpanded jet behavior, manifesting shock wave formations
and sequential shock cell structures in the near-nozzle zone. This
work investigated transient shock cell evolution and Mach disk
parameters during high-pressure hydrogen injection through a
single-hole cylindrical injector. The injector inner pressure
building-up process was tested, and a three-dimensional large-
eddy simulation (LES) model was used to investigate the
underexpanded jet. The results show that the inner pressure
declines from the hydrogen tank to the injector, undergoing a
pressure-building transient process, causing a delay in achieving stabilization. Moreover, shock cell development exhibits distinct
transient characteristics. The Mach disk dimension parameters, i.e., cell core length L
c
, Mach disk width W
disk
, and Mach disk height
H
disk
, demonstrate phased evolution: an initial growth phase followed by asymptotic stabilization. The turning points of L
c
, W
disk
, and
H
disk
depend on the inner pressure-building process. Notably, the constant coefficient C
H
for H
disk
estimation requires empirical
correction due to transient shock cell behavior. For NPR ≥ 90 of a single-hole injector, our data recommend C
H
= 0.85−0.9. The
shock waves of the underexpanded gas flow induce a lower entrainment ratio within the near-nozzle region (Z/D < 8), resulting in
minimal entrainment. Furthermore, this dynamic delay phenomenon becomes particularly pronounced when injection cycles are
shorter. It is necessary to consider the dynamic hydrogen jet characteristic for better design and optimization.
1. INTRODUCTION
Hydrogen has emerged as a carbon-neutral gaseous fuel with
significant potential for decarbonizing energy systems, finding
widespread applications across power generation and trans-
portation sectors.
1,2
Its unique combustion properties,
including minimal ignition energy, rapid flame propagation,
and ultralean combustion capability, position it as an optimal
fuel candidate for next-generation propulsion devices. Con-
temporary energy conversion devices, particularly internal
combustion engines (ICE), gas turbines, and fuel cells,
increasingly adopt hydrogen to achieve carbon neutrality
targets.
3−5
Hydrogen is a high-quality fuel suitable for use in
internal combustion engines (ICE) due to its low ignition
energy and high flame speed. In ICE applications, hydrogen’s
distinctive combustion characteristics enable stable ultralean
combustion regimes, translating to 15−25% thermal efficiency
gains coupled with near-zero COx emissions compared to
conventional hydrocarbons.
6,7
Internal combustion engines
play a dominant role in transportation, and the use of
hydrogen as a fuel for internal combustion engines has
attracted increasing attention. Hydrogen as an engine fuel
offers advantages, such as improved flame propagation speed,
low lean burn limit, and high energy density. Recent techno-
economic analyses, including a 2045 roadmap by Delorme et
al. at the Argonne National Laboratory, project 40−60%
efficiency improvements in hydrogen-ICE hybrid systems
through advanced direct injection and turbocharging strat-
egies.
8
Consequently, conventional internal combustion
engines fueled with hydrogen have been the focus of research
and development because of their low ignition energy, lack of
carbon atoms, and high combustion efficiency. Hence, carbon-
free hydrogen is a critical enabler for decarbonizing hard-to-
Received: November 16, 2025
Revised: February 28, 2026
Accepted: April 1, 2026
Published: April 13, 2026
Articlehttp://pubs.acs.org/journal/acsodf
© 2026 The Authors. Published by
American Chemical Society
24028
https://doi.org/10.1021/acsomega.5c12077
ACS Omega 2026, 11, 24028−24040
This article is licensed under CC-BY-NC-ND 4.0
Downloaded from pubs.​acs.​org/​acsodf/​article-pdf/​11/​16/​24028/​64924359/​ao5c12077.​pdf by guest on 29 August 2026

<!-- PDF_PAGE: 2 -->

electrify transport sectors while maintaining power density
requirements.
Hydrogen can be utilized as an engine fuel through two
primary approaches. One is by utilizing hydrogen as a single-
gas fuel, and the other is by using it combined with other fuels,
such as gasoline, diesel, biodiesel, natural gas, and so on.
9−11
A
critical advancement in both methods is direct injection (DI)
technology. Direct injection of hydrogen is a useful practical
technology which overcomes many of the limitations of port
fuel injection and has been demonstrated to produce excellent
engine brake thermal efficiency and reduce high-load NOx
emissions.
12−14
Lee et al.
15
investigated the effects of hydrogen
direct injection (HDI) on the efficiency and emission
characteristics of an HDI engine, and reported that HDI can
achieve various combustion models to maximize engine
performance, and higher injection pressure improves hydrogen
stratification and efficiency. For HDI technology, in order to
ensure the flow rate of the nozzle, the injection pressure range
is usually 1.5−30 MPa.
16
Lai et al.
17
conducted a test of a DI
hydrogen engine with an H
2
injection pressure of 12 MPa, and
they found that a maximum power of 124.8 kW at an engine
speed of 4500 rpm, together with a BTE of 42.57%, is
achieved, and NOx emissions are controlled to under 20 ppm.
Yamane et al.
18
used high-pressure injectors for the direct
hydrogen injection engines, and the hydrogen injection
pressure can be up to 20 MPa, with a maximum H
2
injection
volume of 400 mL/injection at 3000 rpm. In addition, as the
engine runs, the high-pressure hydrogen fuel is injected during
the compression stroke, and the injection is repeated cycle by
cycle. The HDI is carried out periodically, and hydrogen
injection is completed once per cycle, which is a pulse
injection. Such high engine speeds require short fuel injection
durations, resulting in high fuel injection pressures. Further-
more, modern engines operate at high speeds to increase the
power and efficiency. For higher engine speeds (more than
6000 rpm), the period of each hydrogen injection is shortened,
which enhances its pulse characteristics. The hydrogen directly
jets into the cylinder in a very short time, and the gas injection
process generally lasts for a few milliseconds (about 1−4 ms).
For this short-time gas pulsed injection, the air and the gas fuel
mix with each other within this limited time just before
combustion. When hydrogen is released from the injector
nozzle of a millimeter-size diameter, high-pressure and high-
speed hydrogen jets generate shockwaves, and this complex jet
flow process occurs periodically. Moreover, the periodical
pulse underexpanded hydrogen jet flow has a great influence
on the entrainment of the environmental air, which determines
the mixing process of the air-fuel mixture. Therefore, it is
necessary and crucial to investigate the pulse jet characteristics
of high-pressure hydrogen gas injection from the millimeter-
size nozzle holes for a fundamental understanding of the gas
dynamics and sonic/mixing characteristics of underexpanded
jets, which will enable the development of new, more efficient
high-pressure DI gas fuel engines.
For a great nozzel pressure ratio (NPR, the hydrogen jet
inside the combustion chamber becomes an underexpanded
gas flow because hydrogen jets with NPR ≥ 4 are considered
to be highly underexpanded.
19
This underexpanded hydrogen
jet induces shockwaves to cause supersonic and sonic flow in
the jet. White et al.
20
reported that for hydrogen-fueled
internal combustion engines, gas fuel injection is typically
designed to achieve sonic speed to allow for high mass flow
rates and short injection durations. Yip et al.
21
investigated the
hydrogen jet and flame by optical experiments under simulated
DI engine conditions, and the optical test results showed that
the shockwave structure appeared in the nozzle near field.
Zhang et al.
22
performed a numerical simulation of high-
pressure hydrogen jets and found that high injection pressure
results in shockwaves and turbulent underexpanded fuel jets
near the nozzle exit. Zhang et al.
23
reported that the flow
characteristics of a supersonic jet stemming from a circular
nozzle are highly dependent on the Mach number, and the
Mach disc forms and induces a primary vortex ring. Asahara et
al.
24
conducted a numerical study of an unsteady high-pressure
hydrogen jet and observed the supersonic flow-like Mach disk
structures, and they reported that jet-base flapping resulted in
periodic high-concentration hydrogen clouds within the range
of the Mach disk.
Many studies have investigated the Mach disk dimensions,
such as the Mach disk height H
disk
and the Mach disk width
W
disk
. These Mach disk dimension parameters can indicate the
location and size of annular shear layers and mixing
characteristics. Crist et al.
25
studied the near-nozzle shock
wave structure and measured the H
disk
for a variety of gases,
including nitrogen, argon, helium, and CO
2
, and they proposed
an equation to calculate Mach disk height based on the NPR.
As suggested by Crist, H
disk
shows a linear relation with the
square root of NPR. Many researchers estimated the linear
constant coefficient C
H
between H
disk
and NPR. Velikorodny
and Kudriakov
26
conducted a 3D simulation to investigate the
near-field of highly underexpanded gas jets, and suggested that
the linear constant coefficient C
H
is 0.63. Vuorinen et al.
27
studied the large-eddy simulations (LES) model of the highly
underexpanded transient gas jets, and they reported that the
nozzle pressure ratio has an influence on the Mach disk
dimensions and suggested C
H
values of 0.62. Hamzehloo and
Aleiferis
28
found that for hydrogen jets with values of NPR up
to 10, C
H
had a value of 0.65; for hydrogen jets with NPR in
the range 8.5−70, an average value of C
H
was suggested to be
0.71.
The above literature on the Mach disk dimensions
considered the condition that the underexpanded feature
becomes stable. In addition, for the NPR, the injection
pressure of the injector is adopted to substitute the total
pressure near the nozzle outlet. Furthermore, many literature
reports considered the injection pressure or total pressure
inside the nozzle as constant. For practical application in the
hydrogen DI engine, the pressure inside the injector needs
time to build up as the injection is triggered. However, few
studies considered the inner pressure-building process of the
injector. A previous work
29
experimentally investigated the
macroscopic structure of gas jets using the Schlieren imaging
technique and found that high-pressure gas jet flow is a
dynamic process inside the injector nozzle. Yin et al.
30
conducted a modeling investigation on gas jet flow with direct
injection and found that the gas jet process exhibits a three-
stage transient behavior. Thus, the dynamic pressure-building
process inside the DI injector may have a great influence on
the jet flow out from the nozzle. In order to mitigate the
impact of excessive boundary conditions, this article focuses on
the study of the gas jet flow from a structurally simple single-
hole circular nozzle. This work conducts both experimental
and numerical simulation research on the pressure-building
process and its effect on the underexpanded jet flow of
hydrogen direct injection.
ACS Omega http://pubs.acs.org/journal/acsodf Article
https://doi.org/10.1021/acsomega.5c12077
ACS Omega 2026, 11, 24028−24040
24029
Downloaded from pubs.​acs.​org/​acsodf/​article-pdf/​11/​16/​24028/​64924359/​ao5c12077.​pdf by guest on 29 August 2026

<!-- PDF_PAGE: 3 -->

2. METHODOLOGY
2.1. High-Pressure Gas Jet from a Single-Hole Cylindrical
Injector
For high-pressure gas fuel direct injection, the injector is
usually designed with a multihole nozzle. For the purpose of
studying the gas jet flow characteristics from the injector, a
single-hole nozzle is necessary. Generally, the single-hole
injector is formed by adopting a modified cover to cope with
the multihole injector. The injector cover is designed such that
there is a cylindrical nozzle. Figure 1 presents the high-pressure
gas injector with a 6-hole nozzle used in this research. There is
a chamber inside the cover, and at the bottom of the cover is a
single-hole circular nozzle with a diameter of 0.5 mm. The
hydrogen gas first enters the injector from the high-pressure
fuel tank, flows out of the injector through the six holes into
the inner chamber of the cover, and finally jets into the
background atmosphere through the single-hole nozzle.
The hydrogen gas experiences different pressures during this
injection process. The high-pressure hydrogen gas with
pressure p
injection
from the tank first enters the internal chamber
of the cover, and the gas pressure inside the chamber changes
to pressure p
in
. Finally, the hydrogen gas jets out of the circular
nozzle with pressure p
jet
, and into the background with
pressure p
b
. The characteristics of the hydrogen gas jet from a
single-hole circular nozzle highly depend on the ratio of the
upstream nozzle total pressure p
in
to the background ambient
static pressure p
b
. This NPR is defined as the ratio of the
upstream total pressure p
in
to ambient static pressure p
b
, i.e.,
NPR = p
in
/p
b
. Based on NPR, gas jets can be characterized as
subsonic, moderately underexpanded, and highly under-
expanded. For a hydrogen gas-free jet, it is considered that
the gas jet is highly underexpanded as NPR ≥ 4. Figure 2
shows an underexpanded gas jet near the nozzle. For the
underexpanded gas jet, the gas flow velocity at the nozzle
outlet can reach sound speed, i.e., the gas flow is choked and
the local Mach number Ma = 1. The high-pressure injection
induces oblique and expansion shock waves to form a barrel
shock. Prandtl−Meyer shock waves appear at the nozzle outlet
due to the high NPR, and the triple point forms. Mach disks
form due to the complex near-nozzle shock wave structure, and
the local Mach number Ma changes due to Mach disks. The
flow velocity before the Mach disk is supersonic (Ma ≫ 1),
and it becomes subsonic after the Mach disk (Ma < 1). For the
underexpanded gas jet with a high NPR, a series of shock cells
form within the jet core. The shock cells are formed by
reflection of radially propagating oblique shocks and expansion
fans from the jet boundary. The shock cells lead the static
pressure inside the jet to decrease gradually to that of the
surrounding ambient pressure.
Generally, the dimensions of the Mach disk in under-
expanded gas jets are described by two parameters, i.e., the
Figure 1. High-pressure gas injector (photograph courtesy: Yan Lei. Copyright 2024).
Figure 2. Near-nozzle shock wave structure of underexpanded gas jets.
ACS Omega http://pubs.acs.org/journal/acsodf Article
https://doi.org/10.1021/acsomega.5c12077
ACS Omega 2026, 11, 24028−24040
24030
Downloaded from pubs.​acs.​org/​acsodf/​article-pdf/​11/​16/​24028/​64924359/​ao5c12077.​pdf by guest on 29 August 2026

<!-- PDF_PAGE: 4 -->

Mach disk height H
disk
and the Mach disk width W
disk
. The
Mach disk width is defined as the distance between two triple
points, and the Mach disk height is defined as the distance
between the disk and the nozzle outlet.
Based on H
disk
, the first Mach disk location can be predicted
by eq 1.
19,25
=
H
 D
C
p
 p
disk
H
in
 b
(1)
Here, D is the nozzle diameter and C
H
is the coefficient of
H
disk
.
The coefficient C
H
is estimated as the constant. For
hydrogen gas jets with a value of NPR up to 10, C
H
has a
value of 0.65.
19
An average value of C
H
= 0.71 has been
recommended with the NPR in the range of 8.5−70.
28
The underexpanded gas flow developing process has a great
influence on the entrainment of the gas jet. The entrainment
ratio ψ
E
is adopted to characterize jet entrainment. The
entrainment ratio is defined as the ratio of the entrained air
mass m
air
to the hydrogen mass m
H2
, or the ratio of the
entrained air mole n
air
to the hydrogen mole n
H2
, as shown in
eq 2.
= =
m
 m
n
 n
E
air
 H2
air
 H2
(2)
2.2. Experimental Investigation
2.2.1. Test Rig Set-Up. To research the performance of
the high-pressure hydrogen gas jet sourced from the single-
hole injector, an injector from BOSCH with a pressure up to
30 MPa was adopted as the hydrogen gas injector. To achieve
single-hole injection, an injector cover is provided. The cover
was designed with a single hole with a diameter d = 0.5 mm to
match the injector, as shown in Figure 1. Because the cover is
connected to the injector, the gas injector has only one outlet;
hence, a single-hole injector is fabricated.
Based on the single-hole gas injector, a test rig based on a
constant volume vessel (CVV) was set up to investigate the
hydrogen gas injection performance, as shown in Figure 3. The
inner chamber of CVV was first full of atmosphere air with a
pressure of 0.1 MPa and a temperature of 300 K. During the
experiment, the gas injector was supplied with hydrogen from
the tank at a pressure of 15 MPa. There were two optical
windows made of transparent quartz glass with a diameter of
100 mm at both sides of the CVV. The single-hole gas injector
was mounted directly above the center of the CVV top head.
The gas injector was supplied with high-pressure hydrogen by
a booster pump. The hydrogen gas jet process was recorded by
a high-speed camera, together with a schlieren set-up. The
injector and the camera were synchronously triggered by a
synchronous controller developed by the authors. Figure 3b
presents the synchronous control timing sequence of the
Figure 3. Hydrogen jet test system (created by Yan Lei. Copyright 2024).
ACS Omega http://pubs.acs.org/journal/acsodf Article
https://doi.org/10.1021/acsomega.5c12077
ACS Omega 2026, 11, 24028−24040
24031
Downloaded from pubs.​acs.​org/​acsodf/​article-pdf/​11/​16/​24028/​64924359/​ao5c12077.​pdf by guest on 29 August 2026

<!-- PDF_PAGE: 5 -->

camera and the gas injector. The details of the test rig can be
found in our published papers.
29
During the optical test, first the CVV was supplied with
background air with back pressure p
b
, and the CVV system was
maintained stable for 5 min. Then, the gas injector was
triggered to begin the hydrogen injection under conditions of
different injection pressures p
injection
. At the same time, the
camera was synchronously triggered to record the jet
penetration process. The inner pressure of the gas injector
p
in
was examined by a Kistler pressure sensor, which was
mounted on the injector cover in Figure 1. Table 1 gives the
specifications of the test devices.
Figure 4 shows the tested inner pressure, p
in
, inside the
injector. The hydrogen pressure drops from the fuel tank to the
injector. The hydrogen pressure from the tank is set to 15
MPa, and the pressure inside the injector decreases, i.e., p
in
= 9
MPa. Meanwhile, the pressure-building process inside the
injector is dynamic. It reveals that the inner pressure gradually
rises to its peak value of 9 MPa and then remains stable as the
injector control valve opens. It takes time for the inner pressure
to peak. For this injector, the time required for the inner
pressure increase is 4 ms.
2.2.2. Image Postprocessing. The images of the jet
process were transmitted to the computer for further
postprocessing. All the test images were postprocessed based
on a program developed in commercial code Matlab by the
authors.
29,31
The image postprocessing procedure is shown in
Figure 5. First, the image prior to injection (i.e., t = 0 ms, no
injection) was regarded as the reference background image,
and all other pictures were compared with this reference image
to remove the background. Then, the image edge was
identified according to an edge detection algorithm based on
the Canny operator. In this study, the center of the injector
outlet was set to the zero point (O point) of this system. For
this test system, the mechanical base for installing the gas
injector, with a fixed-sized hypotenuse projection in the
images, was used as the calculation basis for pixel points, as
shown in Figure 6. Therefore, the position of each pixel point
within the image boundary relative to the origin O point can be
calculated.
Moreover, Figure 6 gives the original test image and the
postprocessed result, which clearly shows the outline edge of
the hydrogen jet flow. According to the outline of the jet, the
hydrogen jet tip penetration, Z
tip
, is defined as the maximum
vertical distance of the jet contour profile to the nozzle outlet.
For each test condition, the hydrogen jet test was repeated five
times. The average of the five measurements was set as the jet
tip penetration, and the standard deviation was used to
evaluate uncertainty.
2.3. Numerical Model Simulation
2.3.1. Numerical Model Set-Up. To research the
performance of a high-pressure hydrogen gas jet sourced
from the single-hole injector, a three-dimensional (3D) LES
numerical model of the hydrogen gas jet was further completed
based on the commercial code CONVERGE. This 3D
hydrogen jet model adopted a dynamic structure (DS)
approach in LES modeling applying a subgrid scale (SGS).
The 3D LES model simulation adopted a fully wall-bounded
system comprising a CVV filled with low-pressure air and a
single-hole nozzle. Figure 7 presents the 3D numerical model
and the grids. For the high-pressure-ratio gas jet, the near-
nozzle field of the gas jet, such as the field around the
cylindrical orifice entrance/outlet corners, should receive the
most attention due to the complicated underexpanded gas
flow. Hence, the grids of the near-nozzle field are particularly
refined. To ensure accuracy of the calculation, considering the
size of the spacing between grids, this study used the adaptive
mesh refinement (AMR) method to build the model grids to
record all flow details in LES simulation without an obvious
improvement in computational loads. The present AMR-
subgrid scale (AMR-SGS) modeling is based on the algorithm
coupling temperature, velocity, and species. The computational
grid resolution adapts in response to small changes in these
parameters with a maximum refinement level of 6. The refined
grids are shown in Figure 6, and they clearly show the
complicated vortex rings. For a clear interpretation of the
numerical method employed, the key parameters used in the
simulations are listed in Table 2.
For the single-nozzle cylindrical injector, the gas flow
through the nozzle is assumed to be isentropic because
Table 1. Test Devices
type specification
camera Photron FASTCAM
SA-X2
image sensor CMOS image
sensor
sensor resolution 1024 × 1024
pixels
frame rate 200,000 fps max
pressure
sensor
KISTLER 4011A range 0−500 bar
max. deviation %FSO < ±0.5
linearity at (T
ref
)
(LSQ)
%FSO < ±0.1
Figure 4. Inner pressure.
Figure 5. Image processing procedure.
ACS Omega http://pubs.acs.org/journal/acsodf Article
https://doi.org/10.1021/acsomega.5c12077
ACS Omega 2026, 11, 24028−24040
24032
Downloaded from pubs.​acs.​org/​acsodf/​article-pdf/​11/​16/​24028/​64924359/​ao5c12077.​pdf by guest on 29 August 2026

<!-- PDF_PAGE: 6 -->

hydrogen is considered as an ideal gas. To maintain the
injection pressure, the nozzle’s top boundary was set as a
pressure inlet, while the CVV chamber’s bottom boundary was
designated as the pressure outlet. The back pressure of the
model was set to be constant atmosphere pressure, i.e., p
b
= 0.1
MPa. The inlet pressure was set to the hydrogen injection
pressure p
injection
. The model was adopted varied inlet pressure,
as shown in Table 3. In this research, there were a total of 3
cases of different injection pressures, and lastly, the pressure
values were all up to 9 MPa. For cases 1# and 2#, the injection
pressures rise dynamically with different rising slopes, and both
reach the peak value of 9 MPa at the end. The pressure
maintains a constant value of 9 MPa in case 3#.
2.3.2. Modeling Validation. In the high-pressure hydro-
gen gas jet, the central axis pressure of the gas jet can reflect
the underexpanded region and shock waves generated by the
Figure 6. Optical test image and postprocessed image.
Figure 7. Hydrogen jet model and grids.
Table 2. Basic Method of the Numerical Model
category specification/description
turbulence model LES (Dynamie Smagorinsky)
base solver PISO, density-based
time control 1 × 10
−8
−1 × 10
−7
s
ACS Omega http://pubs.acs.org/journal/acsodf Article
https://doi.org/10.1021/acsomega.5c12077
ACS Omega 2026, 11, 24028−24040
24033
Downloaded from pubs.​acs.​org/​acsodf/​article-pdf/​11/​16/​24028/​64924359/​ao5c12077.​pdf by guest on 29 August 2026

<!-- PDF_PAGE: 7 -->

compressible fluid high-pressure jet, which can reflect the
accuracy of the model simulation to capture the high-pressure
supersonic flow. Therefore, in the research, the model grid
independence was done by checking the central axis pressure
of the hydrogen jet flow. Here, the author adopted three
different gridding standards, ranging from coarse and middle to
fine. The overall grid size and the AMR scale differ from one
another, as shown in Table 4.
In this study, the root mean square error (RMSE) was used
to characterize the accuracy of the simulation model. RMSE
can be calculated as shown in the following equation.
=
y y
 n
RMSE
( )
i ref
2
(3)
where y
i
represents the values obtained by the model
simulation, and y
ref
represents the corresponding reference
values. Here, n is the number of values.
Figure 8 gives the results of the grid independence
verification under the condition of injection pressure = 9
MPa, while the jet time is 1 ms. It shows that the pressure
curve shows the fluctuation, and improving grid density (from
coarse to fine) may reduce the fluctuation. Furthermore, the
pressure curves of medium and coarse grids coincide, which
means that the deviation of the simulation for both medium
and fine mesh resolutions is minimal. However, the fine grid
has a great cell number, and the simulation solving time
becomes longer than the medium one, despite the simulations
yielding a more explicit and precise representation of the near-
nozzle shock structure. Therefore, the medium grid was
adopted for this model simulation.
To quantitatively evaluate the grid independence, the RMSE
was calculated according to eq 3. Here, y
i
denotes the reference
pressure values obtained along the central axis with the finest
mesh, and y
ref
represents the corresponding predicted pressure
values from the medium mesh. In this work, the calculated
RMSE is 0.01, which is significantly small, relative to the
pressure magnitude. This indicates that the medium mesh
provides sufficient numerical accuracy and was therefore
adopted for all subsequent simulations to balance precision
and computational efficiency.
Figure 9 presents the model simulation verification result
compared to the optical test data. Figure 9a shows the
hydrogen jet zip penetration of model results and test data.
Both the model results and the test data show that the
hydrogen jet tip penetration Z
tip
increases as the jet begins.
The deviation was calculated based on relative errors, which
may be used to measure the proportional deviation of the
predicted value from the actual value, and it is particularly
suitable for data with significant differences in magnitude.
Here, y
i
was set to be the model results of Z
tip
, while y
ref
was set
to the test data. It reveals that the model results are consistent
with the test data and have good followability. The deviation
between the model and test data is less than 10%. Figure 9b
shows the hydrogen jet morphology of both the model and test
results. It shows that the shape of the jet closely matches the
test results, with a high degree of overlap. Therefore, the model
is good for analyzing the hydrogen jet characteristics.
Table 3. Pressure Boundary of the LES Model
Table 4. Grid Settings for Grid Independence Verification
grid
density
base size
(regular
hexahedron)
AMR
maximum
cell number grid embedding type
solving
time
coarse 4.0 mm 0.53 × 10
6
SGS (based on
velocity,
temperature, and
species)
20 h
medium 2.0 mm 4.05 × 10
6
50 h
fine 1.5 mm 9.53 × 10
6
90 h
Figure 8. Grid independence verification (p
in
= 9 MPa).
ACS Omega http://pubs.acs.org/journal/acsodf Article
https://doi.org/10.1021/acsomega.5c12077
ACS Omega 2026, 11, 24028−24040
24034
Downloaded from pubs.​acs.​org/​acsodf/​article-pdf/​11/​16/​24028/​64924359/​ao5c12077.​pdf by guest on 29 August 2026

<!-- PDF_PAGE: 8 -->

3. RESULTS AND DISCUSSION
Figure 10 gives the hydrogen mass fraction during the jet
development process. It shows that hydrogen continues
penetrating from the nozzle outlet. The hydrogen gas
accumulates in the central region of the near-nozzle jet area
with the greatest hydrogen mass fraction. The hydrogen mass
fraction gradually decreases from the nozzle outlet to the jet
front. The jet front diffuses and sucks environmental air to mix
with each other.
The high-pressure hydrogen jet with NPR = 90 is highly
underexpanded, and the jet characteristics, especially in the
near-nozzle area, are important, which determine the
developing jet penetration and entrainment. Figure 11 presents
the velocity of the underexpanded hydrogen jet. As the jet
begins, the sonic speed appears near the nozzle area due to
shock waves. The Mach disk appears at 0.2 ms, and the first
shock cell is completely shaped by the Mach disk, together
with shock waves. As the jet continues, the first shock cell
develops, and more shock cells form. A total of 8 cells appeared
for case 1# at 0.9 ms. At first, there is a space between these
shock cells. However, the shock cell space gradually decreases
and the cells join with each other at 1.1 ms. The area of
supersonic velocity continues expanding and tends to become
stable in the last period of the jet. This result reveals that the
shock cells experience a dynamic developing process.
Figure 12 presents the Mach number Ma along the direction
of the jet center line. The zero point is the nozzle outlet. It
shows that Ma is greater than 1 just at the nozzle outlet. This
result means that the hydrogen jet flow becomes supersonic at
the nozzle outlet, which is the typical underexpanded jet due to
a high nozzle pressure ratio NPR. Ma sharply reaches its peak,
Ma = 4.6, at the near-nozzle area, which is the first shock cell
region. Then, Ma gradually decreases along the jet direction,
and finally falls below 1 after Z/D > 50. The hydrogen jet flow
becomes subsonic in the downstream area of the jet. In the
near-nozzle area Z/D < 20, Ma maintains a high value, Ma > 2.
In this near-nozzle area, the hydrogen jet becomes supersonic.
For the supersonic jet flow, shock waves happen and form a
series of shock cells. The shock cell structure and the
developing characteristic cause great effects on jet penetration
and entrainment. Figure 13 shows the cell core length L
c
of
these three cases with different pressure inlets. The cell core is
Figure 9. Model verification (p
in
= 9 MPa).
Figure 10. Mass fraction contour of hydrogen during injection (case
1#, p
in
= 9 MPa).
Figure 11. Velocity contour of the hydrogen jet (case 1#, p
in
= 9
MPa).
ACS Omega http://pubs.acs.org/journal/acsodf Article
https://doi.org/10.1021/acsomega.5c12077
ACS Omega 2026, 11, 24028−24040
24035
Downloaded from pubs.​acs.​org/​acsodf/​article-pdf/​11/​16/​24028/​64924359/​ao5c12077.​pdf by guest on 29 August 2026

<!-- PDF_PAGE: 9 -->

the area covering the shock cells, and the velocity in this cell
core is sonic and even supersonic. In this study, the value of L
c
is derived based on the velocity results of the model
simulation. In the central cross-section, including the center-
line of the nozzle, the overall shape of the hydrogen jet can be
clearly seen. The areas of sonic and supersonic speeds
constitute the core region. For this, the outer contour line of
the core area, the distance from the nozzle outlet to the
farthest outer contour within the core area along the jet flow
direction, is the cell core length L
c
. It reveals that for all cases,
the cell core length L
c
rises rapidly at the beginning of the jet,
and then it tends to reach its peak and become stable. The
stable peak values for different cases are within the same range,
marked in gray, which has an average value of 19.5 mm.
Furthermore, the L
c
curve turning point varies for different
cases. For case 1#, the turning point of the cell core length L
c
occurs at 1.1 ms when the shock cells join with each other, as
shown in Figure 10. Similarly, for case 2#, the turning point
happens at 0.4 ms. For case 3#, the cell core length L
c
sharply
reaches its peak without delay. These results show that the
pressure-building process inside the injector has a huge
influence on the cell core length L
c
. The shorter the
pressure-building process, the faster the stable characteristic
of the shock cells.
Figure 14 gives the Mach disk width of three different
pressure inlets. It shows that the Mach disk width W
disk
has a
similar developing trend with the cell core length L
c
. W
disk
increases first and then maintains its peak stably. The stable
peak values for different cases are almost equal to the average
value of 0.67 mm. Similarly, the curves of W
disk
of cases 1# and
2# show a delay in reaching the stable value compared with
that of case 3#.
Figure 15 shows the Mach disk height of three different
pressure inlets. The Mach disk height H
disk
has a similar
developing trend with both L
c
and W
disk
as well as the delay
characteristics. All Mach disk height H
disk
curves become stable
with an average of H
disk
= 4.21 mm. As for H
disk
, it can be
derived by eq 1. The constant coefficient C
H
in eq 1 is
estimated in many literatures. For hydrogen gas jets with a
value of NPR up to 10, Hamzehloo
28
suggested that C
H
has a
value of 0.65. Meanwhile, an average value of C
H
= 0.71 has
been recommended with NPR in the range of 8.5−70.
19
With
the different values of C
H
, the Mach disk height H
disk
is
calculated, as shown in Table 5. It shows that for the same
nozzle structure and pressure boundary, H
disk
increases as C
H
becomes higher. For different cases of the pressure p
in
changing, the pressure p
in
of case 1# is set according to the
experimental data. Thus, the C
H
should be set to 0.85. In this
work, the injector is a single-hole cylindrical nozzle, and the
analysis is derived from the specific injector geometry and
operating condition. Therefore, for the single-hole cylindrical
injector of high NPR ≥ 90, C
H
is suggested to be set to C
H
=
0.85−0.9. Compared with the suggested C
H
of 0.65 by
Hamzehloo, C
H
in this work is higher (0.85−0.9). This is
because the larger C
H
is derived under the condition of a
dynamic pressure boundary. The dynamic pressure-building
process inside the injector may cause more fluctuations
compared to constant pressure boundaries. These dynamic
fluctuations tend to induce pressure waves that influence the
Mach disk H
disk
.
The shock waves of the underexpanded gas flow developing
process greatly influence the entrainment of the gas jet and
finally the mixing of air and hydrogen. Along the jet direction,
the hydrogen jet has a different entrainment ratio. Figure 16
shows the entrainment ratio under conditions of different Z/D
positions for different pressure boundary cases. The smaller Z/
D = 1.4 represents a position close to the nozzle outlet, while
the higher Z/D = 29.4 is far from the nozzle, which is out of
the shock wave core. It shows that the entrainment ratios are
almost the same for different cases as Z/D is higher. For the
smaller Z/D, which is close to the nozzle outlet, there are a few
differences for the three cases. Furthermore, in the early stage
of the jet of Z/D = 1.9, the entrainment ratio of case 1# is
slightly greater than that of the other two cases. It reveals that
the dynamic pressure boundary mainly affects the entrainment
Figure 12. Mach number Ma (case 1#, p
in
= 9 MPa).
Figure 13. Cell core length.
ACS Omega http://pubs.acs.org/journal/acsodf Article
https://doi.org/10.1021/acsomega.5c12077
ACS Omega 2026, 11, 24028−24040
24036
Downloaded from pubs.​acs.​org/​acsodf/​article-pdf/​11/​16/​24028/​64924359/​ao5c12077.​pdf by guest on 29 August 2026

<!-- PDF_PAGE: 10 -->

ratio in the area close to the nozzle outlet during the early stage
of the jet.
Here, the details of the hydrogen mass fraction and
entrainment ratio under the condition of different Z/D along
the jet direction based on the results of case 1# are presented,
because those parameters have a similar tendency among the
three cases. According to the model simulation results of case
1#, which follow the test data, the hydrogen entrainment
characteristics are investigated. Figure 17 shows the developing
process of the average hydrogen mass fraction on the sections
along the jet boundary. Z/D represents the section location
along the jet direction. The smaller the Z/D value, the closer it
is to the nozzle outlet. The results show that the hydrogen
mass fraction decreases with the increase of Z/D. Especially,
the near-nozzle zone (Z/D < 8) has the highest hydrogen mass
fraction, and there are few differences for different Z/D in this
Figure 14. Mach disk width.
Figure 15. Mach disk height.
Table 5. Mach Disk Height H
disk
with Different C
H
C
H
nozzle diameter D [mm] p
in
[MPa] p
b
[MPa] H
disk
0.65 0.5 9 0.1 3.083
0.71 3.368
0.8 3.795
0.85 4.032
0.9 4.269
Figure 16. Entrainment ratio of different cases.
ACS Omega http://pubs.acs.org/journal/acsodf Article
https://doi.org/10.1021/acsomega.5c12077
ACS Omega 2026, 11, 24028−24040
24037
Downloaded from pubs.​acs.​org/​acsodf/​article-pdf/​11/​16/​24028/​64924359/​ao5c12077.​pdf by guest on 29 August 2026

<!-- PDF_PAGE: 11 -->

zone. Moreover, this zone is just within the range of Mach disk
height, i.e., H
disk
= 4.0, Z/D = 8. This near-nozzle area is the
supersonic flow area with shock waves; thus, the hydrogen
mass fraction is more than 50%. Few entrainments occur in
this near-nozzle zone. As the jet begins, the hydrogen mass
fraction of the near-nozzle zone sharply increases up to a high
value with a maximum of 75%. Then, at time = 1.1 ms, the
hydrogen mass fraction of the near-nozzle zone declines to
about 50% and becomes stable. This turning point coincides
with the time of the cell core length L
c
in Figure 13. As the
shock wave develops coving the core area, the shock wave
induces turbulence and enhances the gas flow. The enhanced
flow results in hydrogen diffusion; thus, the hydrogen mass
fraction tends to decrease, and a turning point appears. As for
the regions far away from the nozzle (Z/D > 8), the hydrogen
mass fraction gradually decreases with the increase in Z/D, and
its value is no more than 50%. In addition, the turning point
(time = 1.1 ms) exists for a high Z/D. Therefore, the
developing process of the shock waves in the near-nozzle zone
has a great influence on the subsequent jets.
Figure 18 presents the entrainment ratio of the hydrogen jet.
Here, the entrainment ratio ψ
E
is adopted to characterize the
jet entrainment. Figure 18a illustrates the developing process
of the entrainment ratio ψ
E
. It shows that ψ
E
is low, close to
zero, for small Z/D (near-nozzle zone). For a high Z/D (far
zone), ψ
E
increases sharply with the increase in Z/D. There are
double peaks during the total jet process. One occurs in the
initial jet stage (0.1−0.5 ms), and the other happens in the late
stage (1.6−2 ms). During these two peak stages, the value of
ψ
E
remains high and relatively stable in the peak, which forms
the peak region. Figure 18b presents, respectively, the average
value of entrainment ratio ψ
E
of these two peak regions against
Z/D. The results show that the entrainment ratio ψ
E
of two
peak regions has a linear increasing tendency with the increase
in Z/D. This reveals that the jet flow has greater entrainment
capacity in the far zone than in the near-nozzle zone.
Furthermore, the entrainment ratio ψ
E
of the late jet stage
has a greater linear rising rate compared to the initial stage.
4. CONCLUSION
The high-pressure hydrogen gas jet with a high NPR is the
typical underexpanded jet, which experiences shock waves and
a series of shock cells. For great NPR, the hydrogen jet flow
becomes supersonic at the nozzle outlet. Furthermore, the
underexpanded hydrogen jet exhibits a dynamic process due to
the pressure-building process inside the injector. The inner
pressure inside the hydrogen injector decreases from the fuel
tank to the injector, and the injector experiences a dynamic
pressure-building process. The inner pressure-building process
of the injector causes a delay in the pressure rising to peak and
becoming stable, which greatly influences gas jet penetration
and entrainment.
For a high NPR hydrogen jet, the development of shock
cells is also a dynamic process. The cell core length L
c
, Mach
disk width W
disk
, and Mach disk height H
disk
first increase and
then remain stable at the peak value; the turning point of cell
core length L
c
, W
disk
, and H
disk
depends on the inner pressure-
building process. Moreover, the constant coefficient C
H
for
deriving the Mach disk height H
disk
should be corrected due to
the dynamic characteristic of the shock cells. For the single-
hole cylindrical injector of NPR ≥ 90, C
H
is suggested to be set
to 0.85−0.9.
The shock waves of the underexpanded gas flow developing
process greatly influence the entrainment of the gas jet. The
hydrogen mass fraction decreases with the increase in Z/D. In
the near-nozzle zone (Z/D < 8), the highest hydrogen mass
fraction occurs together with a lower entrainment ratio ψ
E,
which reveals that few entrainments occur in the near-nozzle
zone. The entrainment ratio ψ
E
has a linear increasing
tendency with the increase in Z/D, which means the jet flow
has a greater entrainment capacity in the far zone than in the
near-nozzle zone. Furthermore, the entrainment ratio ψ
E
of the
late jet stage has a greater linear rising rate compared to the
initial stage.
These dynamic hydrogen jet characteristics demonstrate that
there is a delay in stable jet penetration and entrainment. This
dynamic delay of the jet characteristics may become serious if
the changing cycle of the hydrogen injection is shorter. As for
modern HDI power engines, the injection cycle tends to be
Figure 17. Hydrogen mass fraction (Case 1#).
Figure 18. Entrainment ratio (Case 1#).
ACS Omega http://pubs.acs.org/journal/acsodf Article
https://doi.org/10.1021/acsomega.5c12077
ACS Omega 2026, 11, 24028−24040
24038
Downloaded from pubs.​acs.​org/​acsodf/​article-pdf/​11/​16/​24028/​64924359/​ao5c12077.​pdf by guest on 29 August 2026

<!-- PDF_PAGE: 12 -->

shorter as the engine speed becomes higher for better output
power. Thus, it is necessary and significant to consider the
dynamic underexpanded hydrogen jet characteristic for better
design and performance optimization.
■
AUTHOR INFORMATION
Corresponding Author
Yan Lei − College of Mechanical and Energy Engineering,
Beijing University of Technology, Beijing 100124, China;
orcid.org/0000-0003-1732-2703; Email: leiyan@
bjut.edu.cn
Authors
Hailang Sang − Institute of Energy Storage Science and
Engineering, Tianjin University, Tianjin 300072, China;
Guangxi Yuchai Machinery Co., Ltd., Yulin 537000, China
Yu Ye − Guangxi Yuchai Machinery Co., Ltd., Yulin 537000,
China
Zhenru Zhu − College of Mechanical and Energy Engineering,
Beijing University of Technology, Beijing 100124, China
Chuanfu Kou − Guangxi Yuchai Machinery Co., Ltd., Yulin
537000, China
Xing Liu − Guangxi Yuchai Machinery Co., Ltd., Yulin
537000, China
Tao Qiu − College of Mechanical and Energy Engineering,
Beijing University of Technology, Beijing 100124, China;
orcid.org/0000-0002-6508-1396
Complete contact information is available at:
https://pubs.acs.org/10.1021/acsomega.5c12077
Notes
The authors declare no competing financial interest.
■
ACKNOWLEDGMENTS
We gratefully acknowledge the financial support provided by
the National Natural Science Foundation of China
(52371302) and the Guangxi Science and Technology Major
Program (AA24206013).
■
NOMENCLATURE
C
H
, coefficient of Mach disk height; D, diameter; H
disk
, Mach
disk height; Ma, Mach number; m
air
, air mass; M
H2
, hydrogen
mass; n
air
, air mole; n
H2
, hydrogen mole; p
b
, background
pressure; p
in
, gas pressure inside the injector chamber; p
injection
,
gas pressure from the tank; p
jet
, jet pressure at the nozzle
outlet; W
disk
, Mach disk width; Z, hydrogen jet penetration
distance; Z
tip
, hydrogen jet tip penetration; ψ
E
, entrainment
ratio
■
ABBREVIATIONS
AMR, adaptive mesh refinement; BTE, brake thermal
efficiency; CVV, constant volume vessel; DI, direct injection;
DS, dynamic structure; HDI, hydrogen direct injection; ICE,
internal combustion engine; LES, large-eddy simulation; NPR,
nozzle pressure ratio; SGS, subgrid scale
■
REFERENCES
(1) Tasleem, S.; Alsharaeh, E. H. Role of green, yellow, blue, white
and gold hydrogen in fuelling the path to net zero and sustainable
future- A review. Energy Conversion and Management 2025, 326,
No. 119500.
(2) Cho, H. H.; Strezov, V.; Evans, T. J. Life cycle assessment of
renewable hydrogen transport by liquid organic hydrogen carriers.
Journal of Cleaner Production 2024, 469, No. 143130.
(3) Dimitriou, P.; Tsujimura, T. A review of hydrogen as a
compression ignition engine fuel. Int. J. Hydrogen Energy 2017, 42,
24470−22486.
(4) Meng, H.; Zhan, Q.; Ji, C.; Yang, J.; Wang, S. Comprehensive
multi-performance research of hydrogen-fueled Wankel rotary engine
by experimental and data-driven methods. Energy 2025, 319,
No. 134971.
(5) Saaudua, R.; Hamdi, F.; Krotli, M.; Bouabid, A.; Cuce, E.; Koten,
H.; Miraoui, I. Performance and emission characteristics of hydrogen
enriched CNG in a dual fuel diesel engine: An experimental and
numerical research. Renewable Energy 2025, 241, No. 122387.
(6) Verhelst, S. Recent progress in the use of hydrogen as a fuel for
internal combustion engines. Int. J. Hydrogen Energy 2014, 39, 1071−
1085.
(7) Shalid, M. I.; Farhan, M.; Anas, R.; Salam, H. A.; Chen, T.; Xiao,
Q.; Li, X.; Ma, F. Optimization of hydrogen production and system
efficiency enhancement through exhaust heat utilization in hydrogen-
enriched internal combustion engine. Energy 2025, 319, No. 135051.
(8) Delorme, A.; Rousseau, A.; Sharer, P.; Pagerit, S.; Wallner, T.
Evolution of hydrogen fueled vehicles compared to conventional
vehicles from 2010 to 2045. SAE Paper No. 2009-01-1008, 2009.
(9) Manigandan, S.; Ryu, J. I.; Praveen Kumar, T. R.; Elgendi, M.
Hydrogen and ammonia as a primary fuel − A critical review of
production technologies, diesel engine applications, and challenges.
Fuel 2023, 352, No. 129100.
(10) Zhang, W.; Wei, W.; Liu, X.; Zhou, Y.; Li, N. Hydrogen
enrichment of diesel fuel for combustion improvement and emission
reduction in a diesel engine. Int. J. Hydrogen Energy 2023, 48 (23),
15848−15859.
(11) Farhan, M.; Chen, T.; Rao, A.; Shahid, M. I.; Xiao, Q.; Liu, Y.;
et al. Performance, emissions and combustion analysis of hydrogen-
enriched compressed natural gas spark ignition engine by optimized
Gaussian process regression and neural network at low speed on
different loads. Energy 2024, 302, No. 131857.
(12) Matthias, N.; Wallner, T.; Scarcelli, R. A hydrogen direct
injection engine concept that exceeds US DOE light-duty efficiency
targets. SAE Int. J. Engines 2012, 5, 838−849.
(13) Sharma, S.; Goyal, P.; Tyagi, R. Hydrogen-fueled internal
combustion engine: A review of technical feasibility. Int. J.
Performability Eng. 2015, 11 (5), 491−501.
(14) Antunes, J. G.; Mikalsen, R.; Roskilly, A. An experimental study
of a direct injection compression ignition hydrogen engine. Int. J.
Hydrogen Energy 2009, 34 (15), 6516−6522.
(15) Lee, S.; Kim, G.; Bae, C. Effect of mixture formation mode on
the combustion and emission characteristics in a hydrogen direct-
injection engine under different load conditions. Appl. Therm. Eng.
2022, 209, No. 118276.
(16) Verhelst, S.; Demuynck, J.; Sierens, R.; Scarcelli, R.; Wallner, T.
Update on the Progress of Hydrogen-Fueled Internal Combustion
Engines. Belgium 2013, 381−400.
(17) Fy, Lai; Sun, B. G.; Zhang, S. W.; Wang, K. D.; Luo, Q. H.;
Bao, L. Z.; Leach, F. Experimental analysis and optimization of the
variable valve timing on attaining high efficiency with low NOx
emission of a direct-injected hydrogen engine. Energy 2025, 381,
No. 133199.
(18) Yamane, K.; Nogami, M.; Umemura, Y.; Oikawa, M.; Sato, Y.;
Goto, Y. Development of high pressure H
2
gas injectors, capable of
injection at large injection rate and high response using a common-rail
type actuating system for a 4-cylinder, 4.7-liter total displacement,
spark ignition hydrogen engine. SAE Technical Paper, 2011.
(19) Hamzehloo, A.; Aleiferis, P. G. Gas dynamics and flow
characteristics of highly turbulent under-expanded hydrogen and
methane jets under various nozzle pressure ratios and ambient
pressures. Int. J. Hydrogen Energy 2016, 41, 6544−6566.
ACS Omega http://pubs.acs.org/journal/acsodf Article
https://doi.org/10.1021/acsomega.5c12077
ACS Omega 2026, 11, 24028−24040
24039
Downloaded from pubs.​acs.​org/​acsodf/​article-pdf/​11/​16/​24028/​64924359/​ao5c12077.​pdf by guest on 29 August 2026

<!-- PDF_PAGE: 13 -->

(20) White, C. M.; Steeper, R.; Lutz, A. E. The hydrogen-fueled
internal combustion engine: a technical review. Int. J. Hydrogen Energy
2006, 31, 1292−1305.
(21) Yip, H. L.; Srna, A.; Liu, X.; Kook, S.; Hawkes, E. R.; Chan, Q.
N. Visualization of hydrogen jet evolution and combustion under
simulated direct-injection compression-ignition engine conditions. Int.
J. Hydrogen Energy 2020, 45, 32562−32578.
(22) Zhang, J.; Zhang, X.; Huang, W.; Dong, H.; Wang, T.
Isentropic analysis and numerical investigation on high-pressure
hydrogen jets with real gas effects. Int. J. Hydrogen Energy 2020, 45,
20256−20265.
(23) Zhang, H. H.; Aubry, C. Z. H.; Wu, W. T.; Sha, S. The
evolution of the initial flow structures of a highly under-expanded
circular jet. J. Fluid Mech. 2019, 871, 305−331.
(24) Asahara, M.; Ieasa, T.; Tsuboi, N.; Koichi, H. A Numerical
study on unsteady characteristics of high-pressure hydrogen jet
ejected from a pinhole. Int. J. Hydrogen Energy 2022, 47, 31709−
31728.
(25) Crist, S.; Glass, D. R.; Sherman, P. M. Study of the highly
underexpanded sonic jet. AIAA J. 1966, 4 (1), 68−71.
(26) Velikorodny, A.; Kudriakov, S. Numerical study of the nearfield
of highly underexpanded turbulent gas jets. Int. J. Hydrog Energy 2012,
37, 17390−173999.
(27) Vuorinen, V.; Yu, J.; Tirunagari, S.; Kaario, O.; Larmi, M.;
Duwig, C.; Boersma, B. J. Large-eddy simulation of highly
underexpanded transient gas jets. Phys. Fluids 2013, 25, No. 016101.
(28) Hamzehloo, A.; Aleiferis, P. G. Large eddy simulation of highly
turbulent under expanded hydrogen and methane jets for gaseous-
fuelled internal combustion engines. Int. J. Hydrog Energy 2014, 39,
21275−21296.
(29) Lei, Y.; Liu, J. X.; Qiu, T.; Li, Y. Q.; Wang, Y. P.; Wan, B.; Liu,
X. W. Gas jet flow characteristic of high-pressure methane pulsed
injection of single-hole cylindrical nozzle. Fuel 2019, 257,
No. 116081.
(30) Yin, Y.; Lei, Y.; Shen, H.; Yi, Y.; Zhao, T.; Qiu, T. Modeling
investigation on transient behaviors of gaseous ammonia jet flow with
direct injection. Fuel 2024, 358, No. 129997.
(31) Lei, Y.; Liu, J.; Qiu, T.; Mi, J.; Liu, X.; Zhao, N. Effect of
injection dynamic behavior on fuel spray penetration of common-rail
injector. Energy 2019, 188, No. 116060.
ACS Omega http://pubs.acs.org/journal/acsodf Article
https://doi.org/10.1021/acsomega.5c12077
ACS Omega 2026, 11, 24028−24040
24040
Downloaded from pubs.​acs.​org/​acsodf/​article-pdf/​11/​16/​24028/​64924359/​ao5c12077.​pdf by guest on 29 August 2026
