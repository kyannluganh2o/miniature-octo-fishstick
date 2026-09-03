<!-- PDF_PAGE: 1 -->

Contents lists available atScienceDirect
Fuel
journal homepage: www.elsevier.com/locate/fuel
Full Length Article
Gas jet flow characteristic of high-pressure methane pulsed injection of
single-hole cylindrical nozzle
Yan Leia, Jiaxing Liua, Tao Qiua,⁎
, Yunqiang Lib, Yupeng Wangb, Bo Wana, Xianwu Liua
aCollege of Energy and Environmental Engineering, Beijing University of Technology, Beijing 100124, China
bState Key Laboratory of Engine Reliability, Weichai Power Co., Ltd., Weifang 261061, China
ARTICLE INFO
Keywords:
Direct injection
Gas jet
Pulsed injection
Constant Volume Bomb (CVB)
Methane
ABSTRACT
For a direct injection natural gas engine, the fuel jets into the cylinder in cycles, and this gas pulsed injection
process causes crucial effects on the combustion. This study presents an experimental investigation on the
methane direct injection. An optical test rig is designed to observe the high-pressure methane jet into a constant-
volume bomb (CVB), and a numerical model is built to analyze the gas flow. The methane jet has a two-stage
feature. The gas jet characteristic parameters (the tip penetration, penetration speed, jet cone cover area) change
rapidly in dynamic stage I, and become stable in stable stage II. The dynamic process inside the nozzle induces
this two-stage gas jet flow. The inner methane flow experiences a time delay from the inlet to the outlet, and the
gas jet undergoes the same time delay to maintain stable. Furthermore, the injection pressure has great effects on
the gas jet. As the injection pressure rises high enough, the gas jet saturation behavior occurs, and it is caused by
inner flow saturation of Mach number, Reynolds number and gas velocity inside the nozzle. It is not necessary to
increase injection pressure as high as possible for improving the gas jet characteristics.
1. Introduction
Nowadays, the gas fuel as one kind of clean energy is applied in
many engineering fields. For the application in the internal combustion
engine, the gaseous fuel such as natural gas (NG) is more and more
adopted as the combustion fuel to produce less harmful emissions.
There are generally two kinds of natural gas injection methods: one is
the intake pipe injection and the other is the direct injection (DI) in the
cylinder. Gas direct injection provides the possibility of gas direct in-
jection engine as it can increase the volumetric efficiency, generating
the turbulence and increase thermal efficiency of gas engine. In the
natural gas engine applications, the gas-fuel direction injection offers
advantages in engine efficiency[1], and direct-injection natural gas
combustion can achieve the stable lean combustion and low NOx
emissions along with low cyclic variations[2,3]. In natural gas engine
applications, direct injection compression ignition (DICI) engines are
regarded as promising technology focus due to high thermal efficiency
and low emission[4–6]. For the natural gas direct injection compres-
sion ignition (DICI) engines, the gas fuel jets into the cylinder just be-
fore the top dead center when the cylinder pressure is extremely high
due to the compression of the piston. For a direct injection engine, the
gas fuel injection timing is critical for engine combustion, which com-
pletely distinguishes from traditional intake pipe injection. Zeng et al.
[7]tested a direct-injection natural gas engine under various fuel in-
jection timings and reported that the fuel injection timing had a large
influence on the engine performance, combustion and emissions. Huang
et al.[8,9]investigated a direct-injection engine fueled with natural
gas-hydrogen blends under different ignition timings, and they found
that the time intervals between the end of fuel injection and ignition
timing are very sensitive to direct-injection gas engine combustion.
Furthermore, for the internal combustion engine, the fuel injection
occurs once a cycle, and this gas injection repeats in cycles as the engine
runs. Thus, this fuel supply process a pulsed injection. The gas fuel NG
directly jets into the cylinder in very short time, and the gas injection
process generally lasts within several milliseconds (about 2–3ms). For
this short-time gas pulsed injection, the air and the gas fuel mix with
each other within this limit time just before combustion, thus the
control of the natural gas jet is important for the formation of the air-
fuel mixture as well as the combustion stability. It is crucial for NG
engine to control the pulse injection process for better engine output.
In a practical DI natural gas engine, this high background pressure
requires the gas fuel direct injection should maintain high enough
pressure to guarantee the gas injection[10]. Thus, the high-pressure gas
direct injection is necessary for better efficiency and output power.
Goudie et al.[11]tested a directly injected natural gas heavy-duty
engine over the ESC 13-mode test cycle, and reported that the engine
https://doi.org/10.1016/j.fuel.2019.116081
Received 12 July 2019; Received in revised form 19 August 2019; Accepted 22 August 2019
⁎ Corresponding author.
E-mail address:qiutao@bjut.edu.cn(T. Qiu).
Fuel 257 (2019) 116081
Available online 28 August 2019
0016-2361/ © 2019 Elsevier Ltd. All rights reserved.
T

<!-- PDF_PAGE: 2 -->

produces low NOx emissions. Jones et al.[12]reported that the high-
pressure directly injected natural gas engine has lower particulate
matters emissions without increasing nitrogen oxide (NOx) emissions or
fuel consumption. McTaggart et al.[13]tested the natural gas DI engine
and analyzed the engine performance under condition of varied gas
injection pressure based on a numerical model, and reported that the
engine efficiency may increases 7% and the output power rises 20% as
the natural gas injection pressure increases from 30MPa to 60MPa.
However, they did not explain the reason in details. Moreover, the DI
technique requires higher injection pressure. However, higher injection
pressure results in stringent requirement of the injector materials and
the machining process levels with higher costs. It is necessary to re-
search further the effects caused by the high injection pressure.
Recently many researchers focus on investigating the high-pressure
gas injection. Optical observing the gas injection process has been one
effective and useful research method. Many literatures report the vi-
sualization investigation on the gas injection, and demonstrate that the
high-pressure gas jet process is possible to be visually observed by aids
of optical technology. Ishibashi et al.[14]succeeded to investigate the
gas jet combustion in the rapid compression and expansion machine
(RCEM) by means of shadowgraph method. Dong et al.[15]adopted
the Schlieren imaging method to examine the gas jet process and shock
wave structure evolution law under different nozzle pressure ratio, and
they found that long injection duration exists in gas injection process
after the end of the injection. Kuensch et al.[16]investigated the be-
havior of a hollow cone gas jet generated by a piezoelectric injector by
means of tracer-based planar laser-induced fluorescence (PLIF), and
reported that the investigated gas jets undergo two different stages
during the injection. Erfan et al.[17]used Z-type Schlieren and high-
speed camera to observe the structure of Compressed Natural Gas
(CNG) jet directly injected into an optical constant volume chamber
(CVC), and reported that the jet tip penetration of CNG increases for
higher injection pressure and decreases for the higher pressure of the
chamber. Yu et al.[18–20]completed optical experiments and ob-
served the gas jet flow structure and turbulent mixing of pulsed gas jet,
and they reported that shock waves with barrel structure appear im-
mediately near the nozzle exit. Dong et al.[21]investigated experi-
mentally the macroscopic structure of natural gas jets, and reported
that increasing the gas injection pressure is unable to improve the jet tip
penetration obviously.
These above literatures focus on the gas jet process, and reveal that
the higher injection pressure causes effects on gas jet penetration
characteristic. In addition, most literatures investigate the jet tip pe-
netration and the shock wave structure, but there are few literatures
focusing on the dynamic process of the gas pulsed injection. Moreover,
the complex natural gas jet process and its energy transfer process are
unrevealed totally, and the reasons of the jet characteristics are still not
clear.
Furthermore, the gas jet’s source, i.e. the gas injector, may cause
influence on the gas jet characteristics. Vera-Tudela et al.[22] re-
searched the dynamic effects of the needle of a single-hole injector on
the high-pressure methane jet penetration, and they found that a strong
dependency of the needle dynamics on the injection pressure and the
control pressure. These results reveal that the inner operation process of
the injector may cause influence on the high-pressure gas jet, but they
did not explain the reasons in details.Fig. 1illustrates the scheme of the
high-pressure gas injector nozzle. The nozzle hole has a diameter ofd,
and its thickness isl. In a practical high-pressure injector nozzle, gen-
erallyd=0.1mm–0.3mm, and l=1mm, and thus this nozzle has a
diameter/length ratio about 3.3–10 that is greater than 2. This means
that this nozzle is a thick wall hole, and its inner flow is not ignored.
Therefore, it is essential to understand thoroughly the complex
high-pressure natural gas jet flow characteristic by considering the
Fig.1.High-pressure gas injector nozzle.
Fig. 2.Schematics of optical CVB test rig.
Y. Lei, et al. Fuel 257 (2019) 116081
2

<!-- PDF_PAGE: 3 -->

performance of the gas injector. This work aims at investigating the
high-pressure natural gas jet flow from a single-hole injector nozzle,
and here methane (CH4) is adopted as high-pressure injection gas since
methane is the principal component of natural gas. An optical test rig is
built to observe the high-pressure methane gas jet inside a constant
volume bomb (CVB). The high-pressure methane jet performance is
tested under conditions of varied injection and background pressures.
The details of the methane jet flow is observed by a schlieren system
together with a digital high-speed camera. A three-dimension numer-
ical model is built according to the optical CVB gas jet system, and the
details of the methane jet flow are further discussed based on the si-
mulation results.
2. Experimentalinvestigation
2.1. Gas jet optical test
This work builds an optical test rig based on a constant volume
bomb (CVB) system to visually observe the methane (CH
4) gas jet
process. An optical CVB test rig is designed to observe the high-pressure
gas jet under the condition of varied injection pressurepinjectionand
back pressurepb, as shown inFig. 2. A BOSCH gasoline injector is
adopted as the high-pressure gas injector with the injection pressure up
to 30MPa. A matching nozzle cover is connected with the injector so
that the gas injector becomes single hole with a diameter of 0.3mm.
The gas injector is on the top head of the CVB which is supplied high-
pressure methane gas boosted by a gas pressure boosting device. In
addition, a high-pressure steel cylinder provided the CVB with air as the
background gas. To observe the jet process of the gas injection, a
schlieren system together with a digital high-speed camera is adopted.
The light comes from the lighting source, a halogen tungsten lamp.
Through the schlieren system, the light (changing to the parallel light)
goes into the CVB, and finally reaches the camera, which has a Z-shape
optical path. The main optical path is between two concave mirrors
which lay symmetrically opposed on the each side of the CVB. As the
parallel light transfers through the high-pressure gas jet inside the CVB,
the gas density gradient in the measure field changes, resulting in dif-
ferent refractive indexes on the incident light. A high speed camera
finally catches the information of the methane gas jet characteristics.
The images from the camera are sent to the computer for further data
post-processing.
During the test, first the CVB is supplied with background air with
back pressurepb, and the CVB system is maintained stable for 5min. In
addition, an electronically controlled unit (ECU) is developed to syn-
chronously trigger both the injector and the camera. ECU triggers the
gas injector to emit the high-pressure methane gas into the CVB, at the
Fig.3.Optical image and post process image.
Fig. 4.Numerical model of gas jet flow in CVB.
Table1
Test Apparatus.
Type Specification
Camera Photron
FASTCAM Mini
AX200
Image sensor
Sensor resolution
Frame rate
CMOS image
sensor
1024×1024
pixels
6400 fps max
Pressure gauge R01.4311 Range
Accuracy
Operating temperature
0–10MPa
1% full scale
−40 to 60°C
Air pump W0.9/8 Rated outlet pressure
Rated rotation
Volume flow
0.8MPa
930r/min
900L/min
Gas pressure
booster pump
OLF-2530 Rated outlet pressure
Rated rotation
Volume flow
Boost ratio
Gas inlet pressure
Driving gas pressure
0.7MPa
1400r/min
165L/min
60:1
0.01–1MPa
≤0.8MPa
Y. Lei, et al.
Fuel 257 (2019) 116081
3

<!-- PDF_PAGE: 4 -->

same time the camera records the gas jet process. During the experi-
ments, the methane inject pressurepinjectionvaries within the range of
0–30MPa, and the back pressurepb is adjusted range in 0–5MPa. All
the specifications of the test apparatus are described inTable 1.
2.2. Test data post process
The test results of the images of methane gas jet are transmitted to
the computer, need to be post processed.Fig. 3(a) shows one original
image from the camera. It illustrates the gas fuel jet inside the CVB. The
images are post processed based on a program developed in commercial
code Matlab by the authors. First, the image prior the injection (i.e.
t=0ms, no injection) is regarded as the reference background image,
and all other pictures are compared with this reference image to re-
move the background, as shown inFig. 3(b). Then, the image edge is
identified according to an edge detection algorithms based on Robert
operator.Fig. 3(c) shows clearly the edge of the methane gas jet flow.
Based on the edge image of the gas jet, the gas jet tip penetrationSis
defined as the maximum vertical distance of the jet flow contour profile
to the nozzle outlet. The jet cone cover area is defined the total area of
the jet cone. At last, the image is colored, as shown inFig. 3(d).
2.3. Uncertainty analysis of the optical experiment
For each test condition, the gas jet repeats five times. Based on the
five-time test data, the method of standard deviation (SD) is adopted to
Fig.6.Grid independency result.
Fig. 5.Build-up process of the pressure inlet.
Y. Lei, et al. Fuel 257 (2019) 116081
4

<!-- PDF_PAGE: 5 -->

complete the uncertainty analysis of the gas jet characteristics.
The average of the tested gas jet penetration distance is defined as:
=X X
n
¯ i
n
i
(1)
wherenis the number of the measurements, andXiis the measurement
result.
The Standard deviationSDis defined as following:
= =SD
X X
n
( ¯ )i
n
i1
2
(2)
3. Numericalsimulation
This paper presents both the numerical simulation and the experi-
mental investigation on the high-pressure methane gas direct injection
in a newly designed constant volume bomb (CVB) system. The high-
pressure methane is delivered to the gas injector and then jets into the
low-pressure air in the CVB system. In order to clarify the details of the
methane gas jet flow inside the space-limited CVB, a three-dimension
(3D) numerical model is built based on a commercial code ANSYS CFX.
3.1. Geometry and mesh modelling
Fig. 4shows the 3D model mesh based on the gas jet CVB system. In
this CVB model, an orifice with diameter of 0.3mm and length of 5mm
is in the middle. The zone around the cylindrical orifice entrance/outlet
corners should be paid the most attention due to the complicated flow
caused by variable cross section and great gradients. Hence, the meshes
of these zones are particularly refined.
3.2. Physical setups
To simulate the gas jet, an unsteady model is built based on basic N-
S equations. For the high-pressure natural gas injection of a single-hole
cylindrical nozzle in this model, the gas flows inside the tiny orifice at a
high speed, and the gas jet is turbulent flow with high Reynolds
number. To model turbulence in the injector outlet, the two-equation
realizablek-ɛmodel is adopted. For the single-hole cylindrical nozzle
gas injection in this work, for example, when the gas injection pressure
is 20MPa, according to preliminary estimation Reynolds number of gas
jet flow is above 8000, which is a high Reynolds number flow. The two-
equation realizablek-ɛmodel assumes that the flow in the whole model
field is turbulent, and it is suitable for simulation of turbulent flow with
Fig. 7.Model validation.
Y. Lei, et al. Fuel 257 (2019) 116081
5

<!-- PDF_PAGE: 6 -->

high Reynolds number. In addition, this realizablek-ɛmodel has a new
transmission equation for the turbulent dissipation rate, and it is good
for accurately predicting the divergence ratio of flat and cylindrical jets.
In this model, there are several hypotheses: the heat transfer model
is assumed to be isothermal, and the interaction viscosity forces among
the molecules and gravity are all ignored. The solver type is set to be
density-based. For the setting of the spatial discretization, gradient is
defined as Least Square Cell Based, and a second-order upwind scheme
is selected for the turbulence. The mixture model is adopted to define
the injected methane and the background air, and the hybrid in-
itialization is used. The boundary condition is set as the pressure con-
dition. The pressure inlet, i.e. the injection pressurepinjectionof the
methane gas jet, is set by a UDF file that is edited by the authors. The
build-up process of the pressure inlet is set to experience two stages:
first the pressure rises, then maintains stable as shown inFig. 5, which
exactly simulates the injection pressure building-up process in the
practical injector. In the model, the injection methane gas is set as ideal
gas, and the high-pressure methane jets into the CVB system full of low-
pressure air with constant back pressurep
b.
3.3. Grid independence analysis
The preliminary requirement of the numerical simulation is
choosing the optimum mesh fineness for calculation. The numerical
model is simulated with different grid number.Fig. 6shows the grid
independence analysis results at the condition of the injection pressure
p
injection=10MPa and the back pressurepb=1MPa. It shows the gas
mass flow rate increases slightly as the grid number becomes greater.
This gas mass flow rate curve remains stable for different grid density,
demonstrating that the model solution is relatively independent on the
grid density. Hence, for better simulation accuracy, in this simulation
the model grid with the amount of 4.25E+06 is acceptable.
3.4. Model validation
The numerical model is validated by the optical experimental re-
sults.Fig. 7shows the comparison between the model simulation and
the test results under the methane gas injection pressure
p
injection=20MPa and back pressurepb=2MPa. Fig. 7(a) is the jet tip
penetration of methane. It shows that as the injection time increases,
the methane gas jet tip penetrationSrises, and both the experimental
and model simulation curves show the same tendency. During the total
gas jet stage, the standard deviations of the CH
4gas jet tip penetration
distance between the simulation and the test data are almost below 5%.
Fig. 7(b) gives the comparison of the methane jet cone profile between
the model and test result, and it shows that both jet cones have the
similar profiles. The results reveal that the model simulation results
approach the test data, and show good consistency with the test data.
Thus, the result demonstrates that this model is available to analyse the
CH
4jet flow characteristic of the nozzle.
4. Resultsanddiscussion
Fig. 8shows a whole jet process of the methane gas jet. For this
research, the back pressure is constant, i.e. 2MPa. All the optical results
are based on the data of this constant back pressure. To better illustrate
the methane gas jet characteristic, here only presents the optical test
results of one pressure condition (p
injection=20MPa, pb=2MPa) since
all the methane jet images have the similar process. The results clearly
reveals the high-pressure methane gas jet penetration process in CVB.
The high-pressure methane gas emits from the nozzle on the CVB head
and then penetrates towards to the bottom with the increase in the
injection time. The front of the gas jet continues to expand and the tail
end becomes fuzzy. The shape of the gas jet flow profile is almost a
cone. The jet cone develops quickly, and it almost reach the bottom
limit of the optical window at time=15.5ms.
To view the details of the jet penetration process, here presents the
jet penetration characteristic under condition ofp
injection=20MPa,
pb=2MPa. Fig. 9(a) presents the test results of both the gas jet tip
penetration distance and the gas jet cone cover area. The test results
show that both the jet tip penetration and the jet cone area increase
with the increase in the injection time.Fig. 9(b) is the methane gas jet
penetration speed. Note that the gas jet tip penetration is as the mea-
sured distance of the gas jet tip to the injector nozzle outlet, while the
Fig.8.Methane jet flow developing process.
Y. Lei, et al. Fuel 257 (2019) 116081
6

<!-- PDF_PAGE: 7 -->

penetration speed is calculated by the penetration distance divided by
the related time. It is obvious that the penetration speed curve has a
two-stage feature, and has a turning pointtturning(here
tturning=1.4ms). During stage I, the gas penetration speed decreases
sharply, which means that this is an unstable stage due the varying gas
penetration speed. During stage II, the gas penetration speed tends to be
constant that it is a stable stage. The gas jet penetrates at a higher speed
during the earlier stage I than that during later stage II. For the total
injection stage, the gas jet penetration distance increases with the
injection time, however the jet penetration distance rises more rapidly
in stage I (t=0–tturning) than that in stage II (t> tturning). As for the jet
cone area, it increases at a greater slope during stage II.
This methane jet flow’s two-stage behavior also occurs for different
conditions of varied pressures.Fig. 9shows the optical test results of the
methane gas jet penetration characteristics under the conditions of
various gas injection pressure with constant back pressure of
pb=2MPa. Fig. 10(a) shows the jet penetration speed, and these speed
curves have similarly two-stage behaviors.Fig. 10(b) shows the gas jet
Fig.9.Two-stage behavior of gas jet penetration (optical test results).
Y. Lei, et al. Fuel 257 (2019) 116081
7

<!-- PDF_PAGE: 8 -->

tip penetration distanceS i.e. the total length of the gas jet, and the
results show that it increases with the increase in the injection time, and
so does the jet cone area as shown inFig. 10(c). These curves reveal that
the methane gas jet has a two-stage behavior even for varied pressure
conditions. The differences among the curves of varied injection pres-
sures are small during the initial jet stage, and increase during the jet
process, especially in the later injection. During the early time of stage I
(here time≤0.5ms), those parameters have a few differences for
varied injection pressures. The injection pressure causes greater effects
during stage II. As the injection pressure rises, all the jet penetration
parameters, i.e. the tip penetration, the jet cone area, and the gas pe-
netration speed, increase accordingly. However, the increasing
Fig.10.Methane gas jet penetration characteristics (optical test results).
Y. Lei, et al. Fuel 257 (2019) 116081
8

<!-- PDF_PAGE: 9 -->

tendency induced by the rising injection pressure weakens as the in-
jection pressure becomes high enough (here injection pressure
pinjection≥20MPa). Once the gas injection pressure is higher enough
(pinjection≥20), the gas jet penetration distance, the jet cone area and
the jet penetration speed all tend to be constant even aspinjectionrises.
To see the details of this two-stage behavior of the methane gas jet
flow, the model simulation is used to further analyze the methane gas
flow process.Fig. 11presents the model results of the methane gas jet
process.Fig. 11(a) is the methane density contour of the total jet pro-
cess, and it shows the methane density decreases along the flow di-
rection from the nozzle to the CVB background. At the beginning of the
jet process (0–0.8ms), the methane almost locates inside the nozzle,
and it penetrates from the nozzle outlet into the background. The shape
of the jet flow has a fork tail due to the background air resistance. This
fork tail shrinks as the jet continues. About 1.4ms, the fork tail almost
disappears and the central methane core appears. After that, this central
methane core becomes stable.Fig. 11(b) is the methane velocity con-
tour. It also reveals that the methane flow velocity gradually rises as the
jet time increases. During the early jet process (<0.8ms), the gas flow
velocity is relatively small, lower than the local sonic speed. As the gas
jet continues (≥0.8ms), the methane gas speeds up to the local sonic
speed (450m/s). This jet flow from the nozzle is an underexpanded jet
that induces the expansion shock wave, and a shock cell appears at
time=1.4ms. The shock cell appears in the center of the jet flow,
where the gas velocity is up to the maximum. The shock cell becomes
stable when time=1.6ms with the continuous developing of the gas
jet, and the barrel shock with Mach disk appears in the area near the
nozzle outlet at 2.6ms. The Mach disk maintains during the late jet
process. Therefore, these results reveal that the methane gas jet is a
dynamic process, and it needs a delay time to become stable after it
emits out of the nozzle outlet the jet begins. For this operation condi-
tion, this delay time is about 1.4ms.
Fig. 12shows the turbulence kinetic energy of the methane jet flow.
It shows at the gas jet beginning, the turbulence kinetic energy is quite
small both inside and outside the nozzle, and it slightly rises at
t=0.4ms outside the nozzle. For the gas jet flow, the turbulence ki-
netic energy has an axisymmetric distribution. This axisymmetric tur-
bulence kinetic energy has a core that has relatively greater value. The
core length tends to change as the gas jet continues. The turbulence
kinetic energy becomes stronger as the jet time increases, and its core
area becomes larger, as shown inFig. 12(a). However, it is notable that
the core length at the beginning increases, and it tends to maintain
constant, just at time=1.4ms, as shown inFig. 12(b). There results in
Figs. 11 and 12reveal that the gas jet after the nozzle needs time to
become stable, and this time delay is 1.4ms here.
Fig. 13shows the mass distribution of methane in the jet flow along
xaxis i.e. the jet directon, and herex=0 is the nozzle outlet.Fig. 13(a)
is the methane mass fraction contour, andFig. 13(b) gives the details of
the methane mass fraction at the planex
0 =10mm. Here, the location
of the methane gas jet flow starting point is exactly the nozzle outlet,
and the observing plane alone the jet axis direction has a location ofx
0.
At the planex0, the jet flow has a jet circle where the methane mass
fraction is investigated. In this work, three different jet planes are
given, and these curves at the constant planes illustrate that the me-
thane mass fraction varies against injection time. At the very beginning
of the gas injection, the methane mass fractions of different plane lo-
cations increase sharply, and then they tend to become change slightly
as time is about 1ms, which reveals that the methane mass distribution
in the same position along the jet direction is also a dynamic process.
The methane jet flow outside the nozzle origins from the inner flow
inside the nozzle. It is necessary to analyze the inner flow character-
istics inside the nozzle.Fig. 14illustrates the details of the inner gas
flow of the injector under condition ofpinjection=20MPa, pb=2MPa.
Here presents the flow parameters in the central planes respectively
Fig.10.(continued)
Y. Lei, et al. Fuel 257 (2019) 116081
9

<!-- PDF_PAGE: 10 -->

locating at the nozzle inlet, the middle, and the nozzle outlet. All the
parameters are derived based on the area integral of the central plane
for different locations. The results show that both the gas pressure and
the density decrease in order from the nozzle inlet to the outlet, but the
gas velocity rises on the contrary. For the nozzle inlet, when the in-
jection time increases, the gas pressure and the density decline, but the
velocity increases. For the nozzle outlet, the gas pressure and the
density increase as time goes by, but the velocity slightly decreases. For
the nozzle middle plane, all these parameters change slightly. For all
the locations, these gas parameters such the pressure, the density, and
the velocity, tend to be stable at 1.4ms. This shows that the inner flow
experiences a dynamic process. At the beginning, all the gas parameters
vary from the nozzle inlet to the outlet. At time=1.4ms, the gas inner
flow tends to maintain stable. Therefore, there is a buffering time
(about 1.4ms) for the high-pressure methane gas to maintain stable
from the inlet to the outlet.
This dynamic flow process of the nozzle causes directly effects on
the jet flow out of the nozzle. Thus, similarly, the gas jet flow also
experiences a dynamic process. At the jet beginning, the methane gas
velocity and the density change, and then the jet flow becomes stable at
1.4ms, which is induced by the inner nozzle flow dynamic character-
istic. As a result, this dynamic flow process of the injector nozzle causes
the two-stage methane jet flow.
Fig. 15presents the inner methane gas flow Mach number char-
acteristics insider the injector nozzle under condition of constant back
pressurepb=2MPa while the injection pressure varies. It illustrates
the Mach numberMa alongx-axis exactly the gas flow direction. The
zero point of thex-axis is the nozzle inlet, and the nozzle outlet locates
atx=5mm. The results show that for a given operation condition of
constant injection pressure and back pressure, Mach numberMa
Fig.11.Methane gas jet flow parameters (model simulation results).
Y. Lei, et al. Fuel 257 (2019) 116081
10

<!-- PDF_PAGE: 11 -->

increases from the nozzle inlet to the outlet. As for the constant back
pressure 2MPa,Ma is below 1 when the injection pressure is lower than
15MPa. When the injection pressure continues rising up to 15MPa,
Mach number rising up to 1 at the outlet, which means the methane gas
flow becomes a sonic flow. Moreover,Ma curves tend to be coincident
even the injection pressure continues to rise. The curve of 20MPa co-
incides with that of 25MPa, which meansMa maintains stable, named
Mach number saturation, even the injection pressure increases enough.
Thus, this saturation ofMa inside the nozzle means the constant velo-
city at the nozzle outlet even the injection pressure increases
Fig. 12.Turbulence kinetic energy of methane jet flow (model simulation results).
Y. Lei, et al. Fuel 257 (2019) 116081
11

<!-- PDF_PAGE: 12 -->

continuously. As a result, the methane gas jet flow that origins from the
nozzle outlet is affected by this velocity saturation, thus the jet pene-
tration characteristic also has a saturation behavior as illustrated in
Fig. 10.
Fig. 16shows Reynolds numberReof the methane gas flow alongx-
axis under condition of constant back pressurepb=2MPa while the
injection pressure varies. Herex=5mm is just the nozzle outlet. It
clearly illustrates thatReinside the nozzle differs from that outside the
nozzle. Inside the nozzle, Reynolds number increases sharply from the
nozzle inlet to the outlet, and Re is over 3800, which means the inner
methane gas flow is turbulent. However, Reynolds number tends to
decline quickly after the gas jets out of the nozzle, and it sharply de-
creases to below the critical Reynolds number, which means the outside
jet flow is laminar flow. The high gas velocity and Mach number mainly
Fig.13.Methane mass fraction of jet flow (model simulation results).
Y. Lei, et al. Fuel 257 (2019) 116081
12

<!-- PDF_PAGE: 13 -->

induce this inner turbulence gas flow, and the resistance of the back-
ground air dissipates the gas jet energy to cause the outside laminar
flow.
In addition, the results ofFigs. 15 and 16show that as the injection
pressure rises, both Mach number and Reynolds number increase. As
the injection pressure is high enough (here≥20MPa), both Mach
number and Reynolds number become constant.
5. Conclusion
This study presents an investigation on the high-pressure methane
gas direct injection under conditions of varied pressures, and the high-
pressure methane gas jet flow characteristics is further discussed. A
three-dimension numerical model is verified by the optical test results.
The main conclusions are summarized as the following.
Under condition of constant injection pressure and back pressure, as
the injection time increases, the methane gas penetration speed first
decreases and then maintains constant, which shows the methane gas
jet penetration has a two-stage feature during the jet process. Stage I is
a dynamic stage: the methane penetration velocity declines sharply,
and both the methane tip penetration and the jet cone cover area rise.
Stage II is a stable stage: the methane penetration speed becomes
constant, while both the methane jet tip penetration and the jet cone
cover area continue rising but the curves’ slopes become slightly
smoother.
The dynamic flow process inside the injector nozzle induces this
Fig.14.Flow characteristics of central plane inside nozzle (model simulation results).
Y. Lei, et al. Fuel 257 (2019) 116081
13

<!-- PDF_PAGE: 14 -->

two-stage feature of the methane gas jet flow. The inner flow experi-
ences a dynamic process, and there is a time delay from the inlet to the
outlet for the high-pressure methane gas maintain stable characteristics
such as the gas velocity, pressure, density, turbulence kinetic energy.
This dynamic flow process of the inner nozzle flow causes directly ef-
fects on the gas jet flow out of the nozzle. The methane gas jet also
experiences a same time delay to maintain stable flow.
The injection pressure has great effects on the methane gas jet
characteristic. When the injection pressure increases, the jet parameters
such as the methane jet tip penetration, the jet cone cover area and the
penetration speed increase. However, the saturation behavior of the
methane jet occurs as the injection pressure rises high enough. The jet
parameters become constant even the injection pressure increases. This
jet saturation behavior is caused by inner flow saturation of Mach
number, Reynolds number, and gas velocity inside the nozzle.
Therefore, for the practical engineering application, it is not necessary
to increase gas injection pressure as high as possible for improving the
gas jet characteristics.
For the practical direct injection technology in internal combustion
engines, the gas injection is a dynamic jet that should be not be ignored
for engine electronically control. In addition, the structure design of the
injector nozzle is important since the inner flow of the injector nozzle
causes influence on the dynamic gas jet. More work of the influence of
the dynamic natural gas jet on the gas fuel turbulent combustion should
be further done in the future.
Fig.14.(continued)
Fig. 15.Mach number of methane gas flow inside the nozzle (model simulation results).
Y. Lei, et al. Fuel 257 (2019) 116081
14

<!-- PDF_PAGE: 15 -->

Acknowledgments
We gratefully acknowledge financial support for this work by the
National Natural Science Foundation (91641106), the Beijing Natural
Science Foundation (3172007), the Key Laboratory of High Efficiency
and Low Emission Engine Technology, Ministry of Industry and
Information Technology, Beijing Institute of Technology
(2017CX02015). In addition, we acknowledge Beijing University of
Technology for their financial support of this work.
References
[1]Moon S. Potential of direct-injection for the improvement of homogeneous-charge
combustion in spark-ignition natural gas engines. Appl Therm Eng 2018;136:41–8.
[2] Wang JH, Huang ZH, Miao HY, Wang XB, Jiang DM. Study of cyclic variations of
direct-injection combustion fueled with natural gas–hydrogen blends using a con-
stant volume vessel. Int J Hydrogen Energy 2008;33(24):7580–91.
[3] Wang JH, Huang ZH. Effect of partially premixed and hydrogen addition on natural
gas direct injection lean combustion. Int J Hydrogen Energy 2009;34(22):9239–47.
[4] Faghani E, Kheirkhah P, Mabson CWJ, McTaggart-Cowan G, Kirchen P, Rogak S.
Effect of injection strategies on emissions from a pilot-ignited direct-injection nat-
ural-gas engine-Part I: late post injection, SAE technical paper; 2017-01-0774.
[5]Gogolev IM, Wallace JS. Performance and emissions of a compression-ignition di-
rect-injected natural gas engine with shielded glow plug ignition assist. Energy
Convers Manage 2018;164:70–82.
[6] Baratta M, Rapetto N. Mixture formation analysis in a direct-injection NG SI engine
under different injection timings. Fuel 2015;159:675–88.
[7]Zeng K, Huang ZH, Liu B, Liu LX, Jiang DM, Ren Y, et al. Combustion characteristics
of a direct-injection natural gas engine under various injection timings. Appl Therm
Eng 2006;26(8–9):806–13.
[8]Huang ZH, Wang JH, Liu B, Zeng K, Yu JR, Jiang DM. Combustion characteristics of
a direct-injection engine fueled with natural gas-hydrogen blends under different
ignition timings. Fuel 2007;86(3):381–7.
[9] Zheng JJ, Hu EJ, Huang ZH, Ning DZ, Wang JH. Combustion and emission char-
acteristics of a spray guided direct-injection spark-ignition engine fueled with
natural gas-hydrogen blends. Int J Hydrogen Energy 2011;36(17):11155–63.
[10]Gogolev IM, Wallace JS. Study of assisted compression ignition in a direct injected
natural gas engine. J Eng Gas Turbines Power 2017;139:122802.
[11] Goudie D, Dunn M, Munshi SR, Lyford PE, Wright J, Duggal V, Frailey M.
Development of a compression ignition heavy duty pilot-ignited natural gas fueled
engine for low NOx emissions, SAE technical paper; 2004-01-2954.
[12] Jones HL, McTaggart-Cowan GP, Rogak SN, Bushe WK, Munshi SR, Buchholz BA.
Source apportionment of particulate matter from a diesel pilot-ignited natural gas
fueled heavy duty DI engine, SAE technical paper; 2005-01-2149.
[13]McTaggart-Cowan G, Mann K, Huang J, Singh A, Patychuk B, Zheng XZ, Munshi S.
Direct injection of natural gas at up to 600 bar in a pilot-ignited heavy-duty engine.
SAE Int J Engines 2015;8(3). 2015–01-0865.
[14]Ishibashi R, Tsuru D. An optical investigation of combustion process of a direct
high-pressure injection of natural gas. J Mar Sci Technol 2017;22:447–58.
[15]Dong Q, Li Y, Song EZ, Yao C, Fan LY, Sun J. The characteristic analysis of high-
pressure gas jets for natural gas engine based on shock wave structure. Energy
Convers Manage 2017;149:26–38.
[16] Kuensch ZA, Schlatter S, Keskinen K, Hulkkonen T, Larmi M, Boulouchos K.
Experimental investigation on the gas jet behavior for a hollow cone piezoelectric
injector, SAE technical paper; 2014-01-2749.
[17]Erfan I, Chitsaz I, Ziabasharhagh M, Hajialimohammadi A, Fleck B. Injection
characteristics of gaseous jet injected by a single-hole nozzle direct injector. Fuel
2015;160:24–34.
[18]Yu JZ, Vuorinen V, Kaario O, Sarjovaara T, Larmi M. Visualization and analysis of
the characteristics of transitional underexpanded jets. Int J Heat Fluid Flow
2013;44:140–54.
[19] Yu Jingzhou, Vuorinen Ville, Kaario Ossi, Sarjovaara Teemu, Larmi Martti.
Characteristics of high pressure jets for direct injection gas engine. SAE Int J Fuels
Lubr 2013;6(1):149–56.https://doi.org/10.4271/2013-01-1619.
[20] Yu JZ, Vuorinen V, Hillamo H, Sarjovaara T, Kaario O, Larmi M. An experimental
study on high pressure pulsed jets for DI gas engine using planar laser-induced
fluorescence, SAE technical paper; 2012-01-1655.
[21]Dong Q, Li Y, Song EZ, Fan LY, Yao C, Sun J. Visualization research on injection
characteristics of high-pressure gas jets for natural gas engine. Appl Therm Eng
2018;132:165–73.
[22] Vera-Tudela W, Kyrtatos P, Schneider B, Boulouchos K, Willmann M. An experi-
mental study on the effects of needle dynamics on the penetration of a high-pressure
methane jet. Fuel 2019;253:79–89.
Fig. 16.Reynolds number of methane gas flow (model simulation results).
Y. Lei, et al. Fuel 257 (2019) 116081
15
