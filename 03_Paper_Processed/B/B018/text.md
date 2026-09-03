<!-- PDF_PAGE: 1 -->

2020-01-0325 Published 14 Apr 20 20
Under-Expanded Gaseous Jets Characterization 
for Application in Direct Injection Engines: 
Experimental and Numerical Approach
Luigi Allocca, Alessandro Montanaro, and Giovanni Meccariello Istituto Motori CNR
Francesco Duronio and Stefano Ranieri Università degli Studi de L'Aquila
Angelo De Vita Università degli Studi de L'Aquila, Istituto Motori CNR
Citation: Allocca, L., Montanaro, A., Meccariello, G., Duronio, F. et al., “Under-Expanded Gaseous Jets Characterization for Application in 
Direct Injection Engines: Experimental and Numerical Approach,” SAE Technical Paper 2020-01-0325, 2020, doi:10.4271/2020-01-0325.
Abstract
I
n the last years, increasing concerns about environmental 
pollution and fossil sources depletion led transport sectors 
research and development towards the study of new tech-
nologies capable to reduce vehicles emissions and fuel 
consumption. Direct-injection systems (DI) for internal 
combustion engines propose as an effective way to achieve 
these goals. This technology has already been adopted in 
Gasoline Direct Injection (GDI) engines and, lately, a great 
interest is growing for its use in natural gas fueling, so 
increasing efficiency with respect to port-fuel injection ones. 
Alone or in combination with other fuels, compressed natural 
gas (CNG) represents an attractive way to reduce exhaust 
emission (high H/C ratio), can be produced in renewable ways, 
and is more widespread and cheaper than gasoline or diesel 
fuels. Gas direct-injection process involves the occurrence of 
under-expanded jets in the combustion chamber. An accurate 
characterization of such phenomena is crucial for a conse -
quent application in DI-CNG engines.
In this paper an experimental and numerical analysis of 
methane under-expanded jets (as surrogate of CNG) has been 
carried out. The fuel has been injected into an optically-acces-
sible constant-volume chamber by using a modified commer-
cial injector at pressures up to 1.2 MPa. Schlieren imaging 
technique has been employed to evaluate the effects of the 
injection pressure and chamber thermodynamic conditions 
on jet macroscopic characteristics. Proper image post-
processing has been performed to evaluate jet tip penetration, 
Mach disk position and spray cone-angle. Further, a numerical 
CFD model of the injection process has been developed using 
a large eddy simulation (LES) turbulence framework. The 
simulation reproduces both the fuels flow inside and outside 
the injector providing a better knowledge of the air-fuel 
mixing process.
Introduction
T
he constant and continuous growth of world popula -
tion and the improvements in the standard of living 
are leading to an increase in fossil fuels consumption, 
to which are related issues of environmental pollution and 
greenhouse gas emissions. Transport sector significantly 
contributes to CO
2 and pollutant emissions, since most 
internal combustion engines (ICE) burns oil derivatives. For 
this reason, the main goal of ICE research is to develop novel 
technologies in order to achieve a more sustainable mobility 
with a reduced environmental impact and capable to satisfy 
the increasingly stringent regulations on emissions and 
consumption. In order to pursue this task, a solution could 
be to take advantage of the progress made in the field of direct 
injection, together with the use of alternative fuels, such as 
natural gas.
Compressed natural gas (CNG) is regarded as a promising 
alternative fuel to improve engine thermal efficiency and 
reduce both carbon dioxide and pollutant emissions [ 1]. 
Compared to other hydrocarbon fuels, CNG presents wide -
spread and abundant reserves. Furthermore, it can be produced 
in renewable ways, for example, by anaerobic digestion of 
organic wastes. Due to the high H/C ratio, burning natural 
gas can effectively reduce CO
2 emissions compared to gasoline 
and diesel. Its high-octane number also allows high compres-
sion ratios to be  achieved without knocking. Finally, its 
gaseous nature makes it intrinsically free from particulate 
emission problems.
Natural gas can be used both in spark ignition (SI) and 
compression ignition (CI) engines. Most light duty vehicles 
powered by NG are bi-fuel refitted from gasoline engines in 
which gas is always indirectly injected into the intake manifold 
and this causes a reduction in volumetric efficiency, therefore 
in power output. Moreover, due to the slow burning rate of 
gas, to achieve adequate combustion efficiency an advance of 
the spark timings is necessary with a consequent increase in 
the combustion temperature and higher NO
x formation. On 
the other hand, bi-fuel engines show an average reduction in 
Downloaded from SAE International by Dalian Univ of Technology, Monday, August 31, 2026

<!-- PDF_PAGE: 2 -->

2
UNDER-EXPANDED GASEOUS JETS CHARACTERIZATION FOR APPLICATION IN DIRECT INJECTION ENGINES
brake specific fuel consumption and lower CO, CO2 and HC 
emissions compared to gasoline conventional engines [ 2]. 
Thermal efficiency and power could be improved by increasing 
engine compression ratio, taking advantage of the high anti-
knocking property of natural gas. However, since bi-fuel 
engines work with gasoline, too, there is a limit to the 
maximum compression ratio that can be achieved without 
incurring in detonation problems. In other words, bi-fuel 
engines cannot fully benefit from the advantages offered by 
natural gas.
Due to the high autoignition temperature (low cetane 
rating), natural gas in CI engines is commonly used in dual 
fuel mode for heavy duty vehicles [3]. In such engines, natural 
gas is premixed with air into the intake manifold, introduced 
into the combustion chamber and then ignited by injecting 
small amount of pilot diesel fuel, late in the compression 
stroke. As NG is introduced outside from the cylinder, a reduc-
tion in volumetric efficiency is produced implying lower 
engine powers compared to traditional diesel engines. 
However, extremely lean mixtures burned in dual fuel mode 
combined with low flame speed of natural gas significantly 
reduce NO
x emissions [4].
To overcome the problem of power reduction occurring 
in both bi fuel and dual fuel technologies, the solution lies in 
development of dedicated natural gas direct injection engines 
(CNG-DI), thus increasing volumetric efficiency [ 5]. Before 
than CNG engines, the direct injection systems have been 
originally tested on gasoline engines. Indeed, the GDI engines 
are a relevant research topic since various years but still very 
actual and prominent [ 6]. The direct injection technologies 
are capable of performing stratified and homogeneous 
combustion, allowing the engine downsizing and the reduc -
tion of CO
2 emissions [7]. Now, with the increasing environ-
mental concerns, direct injection would be applied also on 
CNG engines. However, direct injection technology, has some 
issues still unsolved that require further research and develop-
ment. As example, in order to inject a sufficient amount of gas 
for every engine condition and to ensure an efficient air/gas 
mixing, large flow areas and/or high injection pressures are 
required to achieve the right combustible flow rates. Previous 
studies [8, 9] have shown that for CNG-DI in spark ignition 
engines an optimal solution consists in the use of outwardly-
opening injectors to maximize flow area with injection pres -
sures between 16 and 30 bar to ensure enough fuel quantity 
for each load condition. Higher pressure values, almost twice, 
are instead required for NG direct injection in CI engines [10], 
due to the higher compression ratio of diesel engines coupled 
with the late gas injection, during compression stroke. For 
such high pressure values, a compressible fluid flowing 
through a convergent nozzle could accelerate to supersonic 
velocity and reach chocking condition. The jet flow becomes 
under-expanded and shock waves appear at nozzle exit. The 
presence of these shock waves can significantly influence 
downstream flow structure and air/fuel mixing process [ 11].
A relevant issue for development of CNG-DI engines is 
the accurate knowledge of gaseous jet flow and the effects on 
mixing process of injection pressure and in-cylinder thermo-
dynamic conditions which are both responsible for the under-
expanded structure occurrence. It is worth noting that the 
presence of under-expanded jets is closely related to the ratio 
between the pressure upstream of injector nozzle and 
in-cylinder pressure [ 12], often referred to as net pressure 
ratio (NPR).
Another issue is that a quantitative measurement of air/
fuel mixing is not always available by experimental investiga-
tions. In this regard, the improvement in the computing 
power has allowed the use of computational fluid dynamics 
(CFD) as a helpful diagnostic tool for investigating under-
expanded jets. The CFD simulations allow not only to obtain 
information otherwise not available with certain experi -
mental optical techniques, but also to reduce costs associated 
with variations in test rigs. In the last years, there have been 
several numerical studies of under-expanded jets. The meth-
odology broadly adopted by researchers involves the usage 
of both density-based [13, 14, 15] and Pressure Implicit Split 
Operator (PISO) algorithms [16, 17, 18, 19] in order to capture 
the jet structure and the shock waves. As verified by Yosri 
et al. [17] and Hamzehloo et al. [ 20, 21] such model, featuring 
a LES turbulence framework, is capable to capture the initial 
vortex ring, formed at the beginning of the injection, the 
Mach disks location and dimensions, the macroscopic char -
acteristics such as penetration length and volumetric growth. 
Banholzer et  al. [ 16] have investigated under-expanded 
methane jets taking into account the condensation 
phenomena that may occur at nozzle exit after the expansion 
of a very high-pressure jets. They have combined a pressure-
based solver with a vapor-liquid equilibrium model and a 
moving mesh methodology, and have carried out several 
RANS simulations in order to investigate the injection of 
methane at 30 MPa pressure into air at different pressure 
levels. Also, they have considered the effect of the fuel 
changing and the temperatures of the air. Furthermore, for 
the lower gas and air temperatures two additional simulations 
were performed including the needle opening process. They 
found that a decrease in fuel temperature such as an increase 
in NPR leads to a more significant phase separation. The 
numerical results have been then compared with experi -
mental measurements obtained from Schlieren (for vapor 
phase) and Mie-scattering (for liquid phase) images. This 
comparison has shown a very good agreement between the 
experimental and numerical results both in length and width 
of the potential core and in their structures. A comparison 
between RANS and LES turbulence models results has been 
performed by Hamzehloo et al. [ 14]. It has been found that 
using the same spatial resolution, the LES model leads to a 
wider subsonic region after each shock compared to those of 
RANS. Moreover, both RANS and LES models predicted 
similar penetration and spreading rate results. Deshmukh 
et al. [ 18] have characterized a hollow-cone helium jet in 
terms of several macroscopic parameters such as axial pene -
tration length and volume of jet, by LES and URANS simula-
tions with both a fixed needle lift and a moving needle 
approach. They also have investigated the air/helium mixing 
in terms of mass-weighted probability density function (PDF) 
of the injected gas within the jet volume. They found that the 
transient needle opening law strongly influences the initial 
stages of the gas jet formation.
This paper considers a commercial injector, suitable for 
gaseous direct injection, and presents a broad experimental 
campaign of jet characterization and a numerical 
Downloaded from SAE International by Dalian Univ of Technology, Monday, August 31, 2026

<!-- PDF_PAGE: 3 -->

UNDER-EXPANDED GASEOUS JETS CHARACTERIZATION FOR APPLICATION IN DIRECT INJECTION ENGINES
 3
reconstruction of the injection process. The main goal is to 
properly characterize the nature of a gaseous injection by 
investigating the effects of injection pressure and in-cylinder 
thermodynamic conditions on macroscopic characteristics 
and mixing process of a gaseous jet. In order to ensure the 
presence of under-expanded structures, a maximum injection 
pressure of 1.2 MPa has been chosen. As a first step of this 
work, methane has been injected into a Constant Volume 
Chamber (CVC) filled with nitrogen. schlieren technique has 
been used to visualize the gaseous jet and to measure penetra-
tion length, cone-angle and Mach disk height (X
disk). Further 
information about the injection process, not available from 
the schlieren images, have been obtained from a numerical 
CFD model developed and validated through the experi -
mental measures. To properly simulate the injection process, 
the model features the complete modelling of the injector’s 
internal flow, a mesh motion for the pintle’s lift transient, an 
adaptive mesh refinement algorithm (AMR) and the imple -
mentation of two species (methane and nitrogen).
Investigation Methodology
The investigations carried out in this paper are finalized to 
characterize a gaseous injection in a constant volume, opti -
cally-accessible chamber at different thermo-dynamic condi-
tions. The jet studied has a transient evolution indeed, accord-
ingly to up to downstream pressure ratio, there are different 
jet’s structures:
 • s
ubsonic jet: the jet is characterized by the presence of a 
potential core region extending for a few nozzle 
diameters, surrounded by the turbulent mixing layer 
induced by the Kelvin-Helmotz instability. In the 
potential core there is no turbulent mixing between gas 
and air.
 • u
nder-expanded jet (NPR > 2): if critical sonic conditions 
have been reached, formation of oblique shocks occurs. 
The shock lines converges towards the jet’s axis and 
merges creating an intercepting shock. Once the jet’s 
axis is reached the waves are reflected and the structure 
is repeated;
 • s
trongly under-expanded jet (NPR > 3.85): at higher 
pressure ratios, a normal shock occurs; it is called Mach 
disk. A highly under-expanded jet is easily recognizable 
by the presence of “barrel shock” in the structure of the 
jet itself close to the nozzle exit.
The physics of under-expanded jets are fundamental for 
engine application because the phenomena influence the air/
fuel mixing process and so, obviously the combustion. A deep 
knowledge of such processes can be achieved only through 
proper theoretical and experimental activities. In this optic, 
an experimental campaign has been conducted at the Istituto 
Motori-CNR-laboratories by the schlieren imaging tech -
nique. A commercial injector, with injection pressure up to 
1.2 MPa, has been modified to been used as a direct injection 
device. Different operating condition have been investigated 
changing injection pressure, ambient pressure and tempera -
ture. The initial conditions for the experimental analysis are 
reported in Table 1. The jet has been characterized in terms 
of penetration length, cone angle and Mach disk height - the 
latter measured only for the highest pressure ratios.
Penetration length represents the distance between the 
nozzle exit and the furthest point on the contour of jet, 
measured along the axis of the spray. The acquisition of the 
penetration length end off as the jet overcomes the vessel 
window acceptance. In this work, cone angle is defined as the 
angle between the tangents to the outside edge of the spray. 
The lines are drawn on the spray contour, from 1% up to 50% 
of the axial penetration: their intersection determines the 
origin of the angle itself [ 22]. Finally, Mach disk height, is 
measured as the maximum displacement of the disk in the 
direction of the jet evolution, with respect to the injector tip 
(Figure 1). The measure error of Mach disk height is half of 
pixel’s height, 166
 μm
. Then, for further information, not 
available by the images measurement, a CFD model has 
been developed.
Experimental Activities
The experimental setup includes a fuel supply system, an injec-
tion apparatus for a CNG Direct Injection and an optically 
accessible constant volume chamber (Figure 2).
TABLE 1  Experimental parameters
Parameter Value
Ambient Temperature (K) 293.15, 363.15
Ambient Pressure (MPa) 0.1, 0.4
Gas Injection Pressure (MPa) 0.6, 0.9, 1.2
Injection Duration(ms) 5
© SAE International.
 FIGURE 1   Definitions of measured parameters.
© SAE International.
Downloaded from SAE International by Dalian Univ of Technology, Monday, August 31, 2026

<!-- PDF_PAGE: 4 -->

4
UNDER-EXPANDED GASEOUS JETS CHARACTERIZATION FOR APPLICATION IN DIRECT INJECTION ENGINES
The fuel supply system consists of a tank filled with 
methane gas (99.95%) up to 17.5 MPa. A pressure regulator is 
used to realize the desired value per each condition. A trans -
ducer ensures an accurate reading of the gas pressure just 
upstream the injector connection.
The fuel was delivered using an inwardly opening single-
hole commercial injector, suitably modified to inject gas 
directly into the constant volume chamber. The same injector 
was adopted in a revised PFI engine for research purpose at 
the CNR laboratory. To provide the direct injection of the gas, 
both the engine and the injector were suitable modified. For 
this reason, a special adapter 1 mm in diameter orifice has been 
designed and mounted both in engine and CVC investigations. 
Further details of the adapter are shown in Figure 3, while the 
geometrical parameters of the adapter are reported in Table 2.
The injection process was controlled by a programmable 
Electronic Control Unit (PECU) for energizing the current 
necessary to activate the needle lift. The injection duration 
was set at 5.0 ms for all the experimental conditions. Five 
repetitions were carried out to ensure repeatability of the 
measurements and define a minimum of records. The injec -
tion and acquisition process started in synchronous mode by 
a TTL triggering signal generated by a pulse generator.
The tests were performed in the CVC, optically accessible 
through three quartz window, 80 mm in diameter, permitting 
the access to a wide area of the spray under investigation. The 
injector was located at the top of the vessel in a customized 
holder. Gas pressure conditions in the vessel (N
2) has been 
varied by gas adduction, while the temperature has been set 
through a system of electrical resistances integrated in 
the chamber.
The structure of gaseous spray was investigated by the 
schlieren technique, sensible to the gradient densities gener -
ated by the fluids flow along the optical path and resulting in 
variations of the refractive index of the gas. Schlieren setup 
(Figure 2) was realized according to the traditional Z-type 
configuration, and further details are reported in [23]. A high-
power LED lamp (Omicron LED MOD V2) emits a light radia-
tion at the wavelength of 455 nm. The beam is collimated 
through a 15° off-axis mirror, with a focal length of 500 mm. 
The generated collimated beam passes through the spray in 
the chamber and is deflected and focused by a second off-axis 
mirror, with analogues characteristics. A knife-edge, mounted 
orthogonally to the spray propagation direction, is placed at 
the focus of the second mirror. Finally, a biconvex lens converts 
the images in the camera through its objective.
The detector is a high-speed C-Mos camera (Photron 
FASTCAM SA4), working at a rate of 27,000 frames per second 
(fps) and realizing an image window of 256x432 pixels. The 
camera was equipped with a 90 mm focal lens realizing a 
spatial resolution of 6 pixel/mm.
Image Processing 
Procedure
As stated above, the schlieren technique is sensitive to the 
gradients of density of the media under examination. Due to 
the expansion of a gas into a surrounding ambient made of 
gas, comparable density gradients realize between methane 
and nitrogen making the methane jet boundary difficult to 
detect. For this reason, a customized procedure was imple -
mented to process the images and ensure a proper contrast 
in order to allow the measurement of macroscopic charac -
teristics of the jet. The thread of this process can be found 
in [24].
 FIGURE 2   Experimental Setup.
© SAE International.
 FIGURE 3   Sketch of the gas injection system.
© SAE International.
TABLE 2  Adapter nozzle geometrical parameters
Parameter Value
Adapter Length (mm) 42.6
Nozzle Length (mm) 0.9
Nozzle Angle (degree) 130
Nozzle Diameter (mm) 1
© SAE International.
Downloaded from SAE International by Dalian Univ of Technology, Monday, August 31, 2026

<!-- PDF_PAGE: 5 -->

UNDER-EXPANDED GASEOUS JETS CHARACTERIZATION FOR APPLICATION IN DIRECT INJECTION ENGINES
 5
Figure 4  reports the steps of the processing algorithm 
applied to the schlieren images.
The routine begins with the extraction of the background, 
through an average of its images, caught just before the start 
of the fuel injection (Figure 4a). Once injected in the chamber, 
the methane jet looks very feeble against the background 
(Figure 4b); to attenuate undesirable noise, the background is 
removed (Figure 4 c). Subsequently, in an iterative way, a 
subtraction of one image and the previous one is carried out, 
to highlight differences in two consecutive steps during the 
evolution of the jet (Figure 4d); images 4c and 4d are super -
imposed obtaining a better contrast with respect to the back-
ground ( Figure 4 e). In the next step, an improvement in 
brightness and contrast ( Figure 4 f) has been obtained, 
followed by a blurring of the image, according to a Gaussian 
function (Figure 4 g). Then, the image has been binarized, 
through the “OTSU threshold” operator (Figure 4h) [25]. The 
spray outline has been extracted from the binarized image by 
means of a contour recognition filter (edge detector, Figure 
4i), through which the measure of the spray penetration was 
possible. Figure 4 l shows an overlay of images “a” and “i”, 
where the two lines determine the axial penetration.
Numerical Approaches
The numerical activities carried out in this study consist in a set 
of CFD simulations performed by CONVERGE software suite. 
It is a general purpose CFD tool that features also mesh movement, 
forced embedding, and an adaptive mesh refinement algorithm 
(AMR). AMR refine mesh where high specific field gradients are 
calculated without significantly increasing the total number of 
computational cells. The injected mass from the injector is 
unknown. The known parameters are the injection pressure, the 
injector’s internal geometry and the pintle lift (Figure 5). The 
pintle lift law has been provided by the manufacturer.
In this way the simulation involves both inside and 
outside’s flows. The pintle lift has been simulated thanks to a 
mesh movement. The injector’s exiting flow is free to expand 
in a constant volume cylinder of diameter and height respec-
tively of 30 mm and 70 mm. The operating conditions reported 
in Table 3 have been simulated and then validated using the 
data from the experimental campaign.
The dynamics of the gaseous injection have been described 
solving the typical equations of a fluid-dynamic problem: 
 FIGURE 4   Image Processing Procedure.
© SAE International.
 FIGURE 5   Pintle Lift.
© SAE International.
Downloaded from SAE International by Dalian Univ of Technology, Monday, August 31, 2026

<!-- PDF_PAGE: 6 -->

6
UNDER-EXPANDED GASEOUS JETS CHARACTERIZATION FOR APPLICATION IN DIRECT INJECTION ENGINES
conservation of mass, momentum, energy and the specie’s 
transport equations. These are the equations just mentioned:
 ∂
∂ + ∂
∂ =ρρ
t
u
x Si
i
 (1)
 ∂
∂ + ∂
∂ =− ∂
∂ + ∂
∂ +ρ ρσu
t
uu
x
P
xx Si ij
ji
ij
j
i ( 2)
 
∂
∂ + ∂
∂ =− ∂
∂ + ∂
∂ + ∂
∂
∂
∂






+ ∂
∂
ρ ρσ
ρ
e
t
ue
x
Pu
x
u
xx
KT
x
x D
j
j
j
j
ij i
jj j
j
t
m m
mm
j
e
hY
x S∑
∂
∂






 +
 (3)
 ∂
∂ + ∂
∂ = ∂
∂
∂
∂





 +ρ ρ ρm mj
jj
tm
j
m
t
u
xx
DY
x S  (4)
 ∂
∂ + ∂
∂ = ∂
∂ + ∂
∂
∂
∂ −+ρρ σ µ ρεk
t
uk
x
u
xx Prt
k
x si
i
ij i
jj j
k (5)
W
here ρ is the density, u is the velocity, P is the pressure and 
σij is the shear stress tensor. Ym is the mass fraction of the species 
m. T is the temperature and hm is the specific enthalpy of species 
m. Dt is the turbulent mass diffusion coefficient and it is constant 
for each component. To couple density, pressure and tempera-
ture the Redlich Kwong (RK) cubic equation has been used:
 P RT
vb
a
vb v= − − +2  (6)
W
ith a and b:
 
a pv
T
bv
rk cc
r
rk c
rk rk
=
=
==
α
β
αβ
2
0 42748 0 08664., .
 (7 )
where α represents the attractive forces between molecules β 
represents the molecules volume while vc is the critical volume, 
given by the critical temperature, the critical pressure and the 
universal gas constant. The equations have been discretized 
using a central differencing scheme which Taylor series trun-
cation errors is second-order [ 26]. The solution algorithm 
relies on the PISO method with converge criteria based on 
density, being the flow compressible [19, 27].
The grid dimensions have been selected relying on bibli-
ography references [28, 13, 18]. Specifically, the base mesh’s 
dimension is of 4 mm with a local embedding of level 4 for 
the internal flow and for the flow just outside the nozzle. The 
AMR level has been set to 6 based on the density and pressure 
gradients (minimum grid size = 62.5 μ m). In this way, the 
model’s computational weight has been lowered and the cell 
usage optimized as shown in Figure 6 .
The turbulence model selected is a LES-Viscous One 
Equation model in order to solve the flow field till to the 
smallest computable vortices. This is unavoidable to make 
qualitatively and quantitatively considerations concerning 
air-fuel mixing process that is fundamental in a possible 
subsequent engine application. The point-wise successive over-
relaxation (SOR) algorithm, with relaxation factor, has been 
adopted to integrate solution over time [ 27]. The used time 
step was varied accordingly to the CFL convective and diffu-
sion numbers so as not to exceed the unity in first case and 
two in the second one.
Three fluid regions have been identified ( Figure 7). The 
initial conditions at each region are the follow:
TABLE 3  Operating conditions numerically simulated
Case
Ambient 
Temperature (K)
Ambient 
Pressure (MPa)
Gas Injection 
Pressure (MPa)
Case 1 293.15 0.1 1.2
Case 2 293.15 0.4 1.2
© SAE International.
 FIGURE 6   Computational cells over time.
© SAE International.
 FIGURE 7   Sectional view of the computational domain and 
assignment of initialization regions.
© SAE International.
Downloaded from SAE International by Dalian Univ of Technology, Monday, August 31, 2026

<!-- PDF_PAGE: 7 -->

UNDER-EXPANDED GASEOUS JETS CHARACTERIZATION FOR APPLICATION IN DIRECT INJECTION ENGINES
 7
 • H igh Pressure Region (Region 2): this is the high pressure 
zone filled with fuel at the injection pressure (methane). It 
is delimited by injector’s internal surfaces and the pintle. 
However, when the pintle lifts, this region is connected to 
the Low Pressure Region and the methane flow.
 • L
ow Pressure Region (Region 3): this zone belongs to 
the cylinder connecting the high pressure region to the 
bulk one. Its pressure and temperature are equal to the 
ambient ones. The species present are unknown. 
Indeed, after some cycles of injection, a fraction of 
methane, added to the nitrogen, is present in this region 
and there are no ways to estimate the relative fractions.
 • B
ulk Region (Region 1): this zone represents the 
injection volume, likely it is filled by nitrogen N 2 at the 
ambient pressure and temperature.
The boundary conditions are the follows (Figure 8):
 • H
igh Pressure Inlets: these are the four holes where the 
combustible is supplied to the injector; their surfaces are 
treated as fixed pressure inlets;
 • M
oving Pintle Surface: this surface reproduce the 
movement of the pintle through a mesh movement;
 • I
njector Wall Surfaces: they consist of some internal faces of 
the injector and the bulk faces. Their boundaries conditions 
are velocity and temperature law of wall functions [27].
All the simulations have been performed on 36 cores of 
a Fujitsu Siemens Workstation equipped with two Intel Xeon 
Gold 6140. Numerical results have been post-processed by 
Paraview software. In particular, methane mass fraction and 
density gradient fields have been plotted with proper color 
maps in order to compare them with the experimental images.
Experimental Results
The analysis of schlieren images has provided information 
regarding evolution and structure of the gaseous jet, tip pene-
tration, cone angle, and Mach disk height allowing to measure 
them. A comparison of the experimental results was conducted 
in order to evaluate:
 • e ffect of injection pressure variation at constant pressure 
and temperature in the chamber;
 • e
ffect of chamber back-pressure fixed the injection 
pressure and chamber temperature;
 • e
ffect of chamber temperature at fixed injection pressure 
and density of nitrogen in the vessel.
Effect of Injection 
Pressure
The effects of injection pressure on the evolution of the gaseous 
jet are shown in Figure 9 , where the chamber pressure and 
temperature are maintained constant. Each sequence starts 
at the instant t
SOI, i.e. the time-frame just before the gaseous 
jet exits from the nozzle and appears in the chamber; the next 
images of the sequences are collected at a predetermined time 
interval from t
SOI function of the camera acquisition rate.
Once fixed the solenoid excitation duration at 5.0 ms, the 
total injection durations up to 11 ms has been measured. This 
is attributed to the compressibility of gas, despite being the 
pintle in the closed position, due to the continues flowing 
toward the chamber of the gas located in the adapter pipe.
For each of the injection pressure, the jet undergoes an 
evolution of its structure passing from subsonic to moderately 
under-expanded up to strongly under-expanded with appear-
ance of Mach disk. As the pintle begins closing, the jet returns 
subsonic. Since Mach disk appearance and its length are corre-
lated to NPR, it can be inferred that the pressure upstream the 
nozzle varies due the pintle lift transitory and gas compressibility.
Figure 10 shows the variation of the Mach disk height 
during the injection process, as the injection pressure varies.
Mach disk height increases in time, up to about 1 ms; 
then assumes a constant value up to about 5 ms, indicating 
 FIGURE 8   Detail of injector’s upper part with related 
boundary conditions.© SAE International.
 FIGURE 9   Evolution of the gaseous jet structure at the 
varying of the injection pressure© SAE International.
Downloaded from SAE International by Dalian Univ of Technology, Monday, August 31, 2026

<!-- PDF_PAGE: 8 -->

8
UNDER-EXPANDED GASEOUS JETS CHARACTERIZATION FOR APPLICATION IN DIRECT INJECTION ENGINES
that the pressure upstream the nozzle stabilized. For longer 
times, the disk height gradually decreases, following the 
closure of the injector. Furthermore, the maximum Mach disk 
height increases for higher injection pressure.
Figure 11  and Figure 12  show the effects of injection 
pressure on the jet tip penetration being constant the back 
pressure in the chamber (0.1 and 0.4 MPa respectively) and 
the temperature (293.15 K).
The graphs show values of axial penetration averaged on 
five successive injections per each test. Error bars reported on 
the graphs give the filling of the standard deviation in the 
complete measurements cycle.
Increase of the tip penetrations correspond to higher 
injection pressures. This effect is stronger for higher back-
pressures. At 0.1 MPa pressure condition in the chamber 
(Figure 11)) and injection pressure of 1.2 MPa, the jet takes 
1.33 ms to cover the window clearance; as the pressure 
decreases down to 0.6 MPa, the flying time of the jet increases 
up to 1.48 ms. The growth in axial penetration is marginal 
within the analyzed time window.
Jet cone-angle is weakly influenced by the injection 
pressure. On one side, the increase in injection pressure deter-
mines a greater quantity of injected fuel, with a consequent 
widening of the cone-angle. On the other hand, the spray would 
tend to penetrate more quickly, causing a self-narrowing. These 
two aspects tend to compensate each other, producing a negli-
gible influence of the injection pressure, as shown in Figure 13.
Effect of Pressure in the 
Vessel
The effects of ambient pressure on the evolution of gaseous jet 
are shown in Figure 14 , where the injection pressure and 
chamber temperature were kept constant.
 FIGURE 10   Effect of injection pressure on Mach disk height
© SAE International.
 FIGURE 11   Axial jet penetration over time for pch = 0.1 MPa.
© SAE International.
 FIGURE 12   Axial jet penetration vs. time at pch = 0.4 MPa.
© SAE International.
 FIGURE 13   Variation of jet cone angle vs. injection pressure 
at pch = 0.4 MPa.
© SAE International.
Downloaded from SAE International by Dalian Univ of Technology, Monday, August 31, 2026

<!-- PDF_PAGE: 9 -->

UNDER-EXPANDED GASEOUS JETS CHARACTERIZATION FOR APPLICATION IN DIRECT INJECTION ENGINES
 9
The figure shows that, for the injection pressure of 
1.2 MPa and the chamber pressure of 0.4 MPa, the Mach 
disks do not occur. The jet, initially subsonic, becomes 
moderately under expanded, with the appearance of shock 
diamonds figures. Then, the evolution again 
becomes subsonic.
Figure 15 shows the effects of vessel back-pressure on the 
tip penetrations for pinj 1.2 MPa and the gas temperature of 
293.15 K. At higher pressure of the gas in the vessel, the tip 
penetration decreases due to its brake action on the methane 
propagation. The vessel pressure of 0.1 MPa determines a tip 
elongation of 54.1 mm at 1.0 ms from the SOI while, at the 
same instant, the jet has covered 39 mm at the chamber 
pressure of 0.4 MPa. Similar trends are registered for the two 
other injection pressures.
Summarizing, the tip penetration of methane jet is more 
sensitive to changes in the vessel pressure than to the variation 
of the injection pressure. In the same way, jet cone-angle is 
mostly affected by the variations in chamber pressure, as 
pictured in Figure 16.
Effect of the Gas 
Temperature in the 
Chamber
The effects of the N2 temperature in the vessel on the evolution 
of gaseous jet are shown in Figure 17 , where the injection 
pressure is kept constant, against a fixed ambient back-density 
obtained acting on the pressure and temperature of N 2. This 
condition realizes a constant resistance of the gas vs. the jet 
motion, regardless of the temperature values. Figure 17 high-
lights that, for the injection pressure of 0.6 MPa and the 
nitrogen density of 1.12 kg/m
3, Mach disks still occur for both 
temperature values. This is due to the fact that the occurrence 
of Mach disks depends mainly on the pressure ratio, rather 
than on the temperature [ 29]. In both cases, the thermody -
namic conditions are such that the ratio between the pressure, 
upstream of the nozzle, and the chamber pressure is such that 
the jet becomes under-expanded. For the same reason, no 
 FIGURE 14   Evolution of the gaseous jet structure at the 
varying of the chamber pressure.© SAE International.
 FIGURE 15   Axial jet penetration vs. time for pinj = 1.2 MPa.
© SAE International.
 FIGURE 16   Variation of jet cone angle vs. chamber 
pressure at pinj = 1.2 MPa.
© SAE International.
 FIGURE 17   Evolution of the gaseous jet structure at the 
varying of the temperature of the gas in the chamber© SAE International.
Downloaded from SAE International by Dalian Univ of Technology, Monday, August 31, 2026

<!-- PDF_PAGE: 10 -->

10
UNDER-EXPANDED GASEOUS JETS CHARACTERIZATION FOR APPLICATION IN DIRECT INJECTION ENGINES
substantial differences on disk height were observed by 
varying chamber temperature.
Figure 18 shows the effects of the gas temperature in the 
chamber on the tip penetration of the jets for the injection 
pressure of 0.6 MPa, at constant back-density of the gas. 
Variation in chamber temperature does not seem significantly 
affecting the axial penetration. Error bars are significantly 
larger at the chamber temperature of 363.15 K where the 
convective motions in the gas produce complex background 
figures making the image processing complex and hard for 
distinguishing the actual methane contours.
Numerical Results
The results obtained by the developed numerical model have 
been compared with the experimental data previously exposed.
Figure 19 represents a 3D visualization of the simulated 
jet aiming to highlight the capacity of the numerical recon -
struction to reproduce qualitatively the jet morphology.
In the numerical investigation, the axial penetration 
length has been computed as the distance between the farthest 
point on the contour of the jet and the top of the wall region, 
by using a threshold for the mass fraction of methane of 0.001, 
similarly to the definition of Deshmukh et al. [ 18].
Figures 20  and 21  show the comparisons between the 
numerical and experimental jet penetrations plotted as 
function of the time for the selected cases ( Table 3  for 
further details).
The results between the experimental and numerical 
datasets catch the trends in both cases and highlight a good 
agreement toward the last part of the simulated time-frames 
while, at the beginning of the injection, small differences are 
registered. A possible motivation could be imputable to the 
uncertainty on the transient of the injector opening.
The adopted model is capable to reproduce qualitatively 
the jet morphology and its temporal evolution. Its character-
istic normal shock is clearly visible plotting the density 
gradient, shown in Figure 22 . At the first stage of the 
injection, the jet exits from the nozzle creating a tip vortex 
structure, Figure 22a. The pressure ratio is relatively low and 
the flow is subsonic Figure 22 b. Then, at increasing of the 
NPR, critical conditions are reached: the jet becomes under-
expanded and shock cells grow ( Figure 22 c). A further 
increase of the pressure brings to the formation of the Mach 
disk (Figure 22d).
 FIGURE 18   Axial jet penetration vs. time for pinj = 0.6 MPa.
© SAE International.
 FIGURE 19   3D visualization of the simulated jet.
© SAE International.
 FIGURE 20   Experimental and numerical axial jet 
penetration vs. time for Case 1 (pinj = 1.2 MPa and  
pch = 0.1 MPa).
© SAE International.
Downloaded from SAE International by Dalian Univ of Technology, Monday, August 31, 2026

<!-- PDF_PAGE: 11 -->

UNDER-EXPANDED GASEOUS JETS CHARACTERIZATION FOR APPLICATION IN DIRECT INJECTION ENGINES
 11
As further confirmation of the model reliability, the Mach 
disk height has been measured from numerical data for the 
Case 1 and compared with the experimental one. Again, 
numerical and experimental results are in a quite-good agree-
ment. Just small differences appear during the first phase of 
the injection (Figure 23).
The Case 2 is not suitable for such analysis due to the 
NPR  ≪ 3.85 [ 28] (Figure 24). Indeed, the model reveals the 
presence of shock cells as it is expected from the theory and 
observed from the experimental images.
The value of the Mach disk height, X
disk, is related to the 
upstream pressure ( pi in Figure 25 ) through the empirical 
relationship [29]:
 FIGURE 21   Experimental and numerical axial jet 
penetration vs. time for Case 2 (pinj = 1.2 MPa and 
pch = 0.4 MPa).
© SAE International.
 FIGURE 22   Gaseous jet structure’s evolution at different 
time-step for Case 1 (pinj = 1.2 MPa and p ch = 0.1 MPa) obtained 
plotting the density gradient.© SAE International.
 FIGURE 23   Experimental and Numerical Mach Disk Height 
vs. time for pinj = 1.2 MPa and p ch = 0.1 MPa
© SAE International.
 FIGURE 24   Gaseous jet structure’s evolution at different 
time-step for Case 1 (pinj = 1.2 MPa and p ch = 0.4 MPa) obtained 
plotting the density gradient.© SAE International.
 FIGURE 25   Nozzle Pressure Definition
© SAE International.
Downloaded from SAE International by Dalian Univ of Technology, Monday, August 31, 2026

<!-- PDF_PAGE: 12 -->

12
UNDER-EXPANDED GASEOUS JETS CHARACTERIZATION FOR APPLICATION IN DIRECT INJECTION ENGINES
 X
D
p
p
idisk =
∞
06 7 .  (8)
w
ith:
 • D o
rifice diameter;
 • p∞  downstream pressure;
Handling Eq. 8, it is possible to compute pi, as:
 pp X
D
i =⋅ 
 
∞
1
06 7
2
.
disk  (9)
Xdisk can be measured from the numerical results as shown in 
Figure 26 and whose precision is related to the mesh size.
For example, at 0.81 ms the computed Mach disk height 
is equal to 2.05  mm. Inserting the ambient pressure of 
0.101325 MPa and the diameter of the nozzle (1 mm) into the 
Eq. 8, p
i,emp is equal to:
 pie mp, . .
.
. .=⋅ 




 =0 101325 1
06 7
20 5
1 000 09 4
2
MPa mm
mm MPa (10)
Th
is value can be compared with that obtained from CFD 
model, at the position illustrated in Figure 25, computing the 
average value over the axial section ( p
i,cfd):
 pic fd, .= 09 7M Pa (11)
Th
e two results are in good accordance with differences 
around 3%. The behaviour of both pi,cfd and pi,emp as function 
of the simulation time can also be easily computed. Figure 27 
shows the comparison between the pressure p i,emp =  pi,emp(t) 
calculated with the empirical relation (Eq. 8) and the one 
estimated from the CFD model p i,cfd = p i,cfd(t).
From the analysis of Eq. 9, a quadratic relationship is 
recognizable between p i and X disk . This is indicative of how 
strong the impact of the pi computation is against small uncer-
tainness on the X disk . The precision measurement of X disk is 
clearly related to the mesh dimension that in our case is 62.5μm.
Evaluation of the methane/air mixing process is a relevant 
topic especially in terms of the effects on the combustion in 
engine applications.
The image sequence reported in Figure 28  shows the 
methane mass fraction ( y
CH4) at different instants from 
the SOI.
The analysis of the images makes clearly recognizable a 
zone, around the jet axis, composed predominantly by 
methane (y
CH4  ≈ 1) called potential core. As the injection goes 
on, the length of such zone grows in a first phase but, then, it 
begins to recede at the end of the simulation. This methane 
 FIGURE 26   2D-map of Density Gradient - Mach 
Disk particular
© SAE International.
 FIGURE 27   2D-map of Density Gradient - Mach 
Disk particular
© SAE International.
 FIGURE 28   Evolution of the gaseous jet structure in term 
of yCH4 2D-map - p inj = 1.2 MPa and p ch = 0.1 MPa
© SAE International.
Downloaded from SAE International by Dalian Univ of Technology, Monday, August 31, 2026

<!-- PDF_PAGE: 13 -->

UNDER-EXPANDED GASEOUS JETS CHARACTERIZATION FOR APPLICATION IN DIRECT INJECTION ENGINES
 13
core is surrounded by a mixing layer of the two species 
(methane and nitrogen) on both the sides.
Downstream the potential core, the jet is characterized 
by a zone where the methane’s mass fraction is significantly 
lower than the one present within the potential core.
Besides, to quantitatively estimate the mixing character-
istics of the gaseous jet, an already established statistical 
approach has been adopted [13, 15, 18]. The probability density 
function (PDF) of mass weighted methane fraction has been 
computed within the jet volume (ρ
iYCH4,Vi), obtained using a 
threshold value for the mass fraction of Y CH4, i > 0.001. The 
influence of the injected specie and the injection pressure on 
mixture formation in gaseous jets have been analysed by 
Vourinen et al. [ 13] while, in this study, attention has been 
focused on the effects of varying chamber counter-pressure. 
The probability density function allows to obtain the distribu-
tion of instantaneous methane concentration in each cell, thus 
providing information about global air/gas mixture. In 
Figure  29  the mass-weighted PDFs of the methane mass 
fraction, for Case 1 and Case 2, at t
ASOI = 0.75 ms after the start 
of the injection, are shown.
The two vertical grey lines delimit the flammable zone 
defined by a methane mass fraction between 0.044 and 0.15. 
In both considered cases, the most probable value, greater of 
about the 24 % for Case 1 than Case 2, belongs to the flam -
mable zone. Furthermore, the probability of finding methane 
mass with a y
CH4 in the flammable zone is greater for the 
counter-pressure of 0.1 MPa. Finally, for the selected time -
frame, it can be observed another peak value for a y CH4  ≈ 1 
representatives of the potential core zone where almost only 
methane is present.
Conclusions
In this work, the gas flow from a single-hole commercial 
injector has been experimentally and numerically investi -
gated. The experimental study has been carried out by 
injecting methane into a constant-volume vessel under 
different injection pressures and different chamber counter-
pressures and temperatures. The images have been acquired 
by schlieren imaging technique; proper image post-processing 
has been performed to evaluate jet tip penetration, Mach disk 
position and spray cone-angle.
Further investigations regarding air/gas mixing process 
have been performed developing a CFD model of the injection 
process for different operating conditions. Such model allows 
a broader understanding of the jet’s characteristic and, espe-
cially, provides further informations concerning the air/fuel 
mixing. The main findings of experimental and numerical 
investigations are summarized as follow:
 • t
he analysis of the schlieren images revealed that, at 
sufficiently high-pressure ratios, the jet has a transient 
nature and involves three flow patterns: subsonic, 
moderately under-expanded, with its characteristic 
shock cells structure, and highly under-expanded with 
Mach disk formation and typical barrel shock 
configuration. The same flow patterns have been 
captured by developing a LES numerical model;
 • h
igher injection pressures correspond to a slightly 
increase in jet tip penetration and to an increment of 
maximum Mach disk height. Moreover, due to the 
transient pintle motion and gas compressibility, Mach 
disk height varies with time;
 • c
hanging in injection pressure does not seem to affect 
the jet cone angle;
 • h
igher chamber pressures correspond to a decrease of jet 
tip penetration and to an increase of jet cone angle;
 • t
he variation chamber of the temperature does not seem 
to significantly affect axial penetration;
 • t
he results of the numerical model have been compared 
against the experimental measures. This evaluation 
highlights a good agreement between the datasets in 
terms of jet tip penetration and Mach disk position;
 • s
ome differences between numerical and experimental 
results can be noticed at the beginning stages of jet 
evolution; this is attributed to the uncertainties on the 
injectors opening transient;
 • t
he pressure upstream the nozzle was determined from 
the numerical results; this value is related to Mach disk 
height through an empirical correlation (Eq. 9). A 
comparison between this numerically measured pressure 
and the calculated one has been conducted to further 
validate numerical model;
 • 2-
D maps of methane mass fraction highlight the 
presence of zones composed almost uniquely by methane 
(potential core) surrounded at both side by nitrogen 
mixed layers. Downstream the potential core, methane 
fraction assumes lower values. It can be conclude that 
higher NPR imply better mixing;
In conclusion, the numerical model provides informa -
tion, not available from schlieren images, on the flow field 
of fuel-jet. These results can be exploited to deepen the 
knowledge of under-expanded jets evolution in engines 
 FIGURE 29   Probability distribution of mass fraction yCH4 
for Case 1 and Case 2 at tASOI = 0.75 ms.
© SAE International.
Downloaded from SAE International by Dalian Univ of Technology, Monday, August 31, 2026

<!-- PDF_PAGE: 14 -->

14
UNDER-EXPANDED GASEOUS JETS CHARACTERIZATION FOR APPLICATION IN DIRECT INJECTION ENGINES
fueled by direct injection of the gas and, therefore, to 
optimize of the mixture formation process. Future studies 
could involves tests of the developed model against other 
experimental datasets.
References
 1 .  C hala, G., Aziz, A., and Hagos, F., “Natural Gas Engine 
Technologies: Challenges and Energy Sustainability Issue,” 
Energies 11:2934, 2018, doi:10.3390/en11112934.
 2
.
 C
hen, H., He, J., and Zhong, X., “Engine Combustion and 
Emission Fuelled with Natural Gas: A Review,” Journal of the 
Energy Institute  92:1123-1136, 2019, doi:10.1016/j.
joei.2018.06.005.
 3
.
 B
oretti, A., Lappas, P., Zhang, B., Mazlan, S.K., “Cng Fueling 
Strategies for Commercial Vehicles Engines - A Literature 
Review,” in 8th SAEINDIA International Mobility Conference 
and Exposition and Commercial Vehicle Engineering 
Congress 2013 (SIMCOMVEC), SAE International, 2013, 
doi:10.4271/2013-01-2812.
 4
.
 W
ahbi, A., Tsolakis, A., and Herreros, J., Emissions Control 
Technologies for Natural Gas Engines: For Transportation and 
Power Generation (2019), 359-379, doi:10.1007/978-981-13-
3307-113”.
 5
.
 K
orakianitis, T., Namasivayam, A., and Crookes, R., 
“Natural-Gas Fueled Spark-Ignition (si) and Compression-
Ignition (ci) Engine Performance and Emissions,” Progress in 
Energy and Combustion Science  37:89-112, 2011, 
doi:10.1016/j.pecs.2010.04.002.
 6
.
 D
uronio, F., De Vita, A., Allocca, L., and Anatone, M., 
“Gasoline Direct Injection Engines - A Review of Latest 
Technologies and Trends. Part 1: Spray Breakup Process,” 
Fuel 265:116948, 2020a, doi:10.1016/J.FUEL.2019.116948.
 7
.
 D
uronio, F., De Vita, A., Montanaro, A., and Villante, C., 
“Gasoline Direct Injection Engines-A Review of Latest 
Technologies and Trends. Part 2,” Fuel 265:116947, 2020b, 
doi:10.1016/J.FUEL.2019.116947.
 8
.
 D
ouailler, B., Ravet, F., Delpech, V., Soleri, D. et al., “Direct 
Injection of cng on High Compression Ratio Spark Ignition 
Engine: Numerical and Experimental Investigation,” SAE 
Technical Papers 2011-01-0923, 2011, https://doi.
org/10.4271/2011-01-0923.
 9
.
 B
aratta, M., Misul, D., Xu, J., Fuerhapter, A., Heindl, R., 
Peletto, C., Preuhs, J., Salemi, P., “Development of a High 
Performance Natural Gas Engine with Direct Gas Injection 
and Variable Valve Actuation,” 2017, 
doi:h/10.4271/2017-24-0152.
 1
0.
 T
aha, Z., Rahim, M.A., and Mamat, R., “Injection 
characteristics Study of High-Pressure Direct Injector for 
Compressed Natural Gas (cng) Using Experimental and 
Analytical Method,” IOP Conference Series: Materials 
Science and Engineering  257:012057, 2017, doi:10.1088/1757-
899X/257/1/012057.
 1
1.
 Y
u, J., Vuorinen, V., Hillamo, H., Sarjovaara, T., Kaario, O., 
and Larmi, M., “An Experimental Study on High Pressure 
Pulsed Jets for Di gas Engine Using Planar Laser-Induced 
Fluorescence,” in SAE 2012 International Powertrains, Fuels 
and Lubricants Meeting , SAE International, 2012, https://doi.
org/10.4271/2012-01-1655.
 1
2.
 D
onaldson, C.D. and Snedeker, R.S., “A Study of Free Jet 
Impingement. Part 1. Mean Properties of Free and 
Impinging Jets,” Journal of Fluid Mechanics 45:281-319, 1971, 
doi:10.1017/S0022112071000053.
 1
3.
 V
uorinen, V., Wehrfritz, A., Duwig, C., and Boersma, B.J., 
“Large-Eddy Simulation on the Effect of Injection Pressure 
and Density on Fuel Jet Mixing in Gas Engines,” Fuel 
130:241-250, 2014, doi:10.1016/j.fuel.2014.04.045.
 1
4.
 H
amzehloo, A. and Aleiferis, P.G., “LES and RANS 
Modelling of Under-Expanded Jets with Application to 
Gaseous Fuel Direct Injection for Advanced Propulsion 
Systems,” International Journal of Heat and Fluid Flow 
76:309-334, 2019, doi:10.1016/j.ijheatfluidflow.2019.01.017.
 1
5.
 V
uorinen, V., Yu, J., Tirunagari, S., Kaario, O. et al., “Large-
Eddy Simulation of Highly Underexpanded Transient Gas 
Jets,” Physics of Fluids 25:016101, 2013, doi:10.1063/1.4772192.
 1
6.
 B
anholzer, M., Vera-Tudela, W., Traxinger, C., Pfitzner, M.  
et al., “Numerical Investigation of the Flow Characteristics 
of Underexpanded Methane Jets,” Physics of Fluids 
31:056105, 2019, doi:10.1063/1.5092776.
 1
7.
 Y
osri, M., Lacey, J., Talei, M., Gordon, R., and Brear, M., 
“Development of a Verification Methodology for Large-Eddy 
Simulation of Underexpanded Natural Gas Jets,” 
Development 10:13, 2018.
 1
8.
 D
eshmukh, A.Y., Vishwanathan, G., Bode, M., Pitsch, H., 
Khosravi, M., and Bebber, D.V., “Characterization of Hollow 
Cone Gas Jets in the Context of Direct Gas Injection in 
Internal Combustion Engines,” 2018, doi:10.4271/2018-01-
0296.
 1
9.
 B
artolucci, L., Scarcelli, R., Wallner, T., Swantek, A., Powell, 
C.F., Kastengren, A., and Duke, D., “CFD and X-Ray 
Analysis of Gaseous Direct Injection from an Outward 
Opening Injector,” Technical Report,” 2016, 
doi:10.4271/2016-01-0850.
 2
0.
 H
amzehloo, A. and Aleiferis, P.G., “Gas Dynamics and Flow 
Characteristics of Highly Turbulent Under-Expanded 
Hydrogen and Methane Jets under Various Nozzle Pressure 
Ratios and Ambient Pressures,” International Journal of 
Hydrogen Energy 41:6544-6566, 2016a, doi:10.1016/j.
ijhydene.2016.02.017.
 2
1.
 H
amzehloo, A. and Aleiferis, P., “Numerical Modelling of 
Transient Under-Expanded Jets under Different Ambient 
Thermodynamic Conditions with Adaptive Mesh 
Refinement,” International Journal of Heat and Fluid Flow 
61:711-729, 2016b, doi:10.1016/J.
IJHEATFLUIDFLOW.2016.07.015.
 2
2.
 H
ung, D.L., Harrington, D.L., Gandhi, A.H., Markle, 
L.E., Parrish, S.E., Shakal, J.S., Sayar, H., Cummings, 
S.D., Kramer, J.L., “Gasoline Fuel Injector Spray 
Measurement and Characterization - A New SAE j2715 
Recommended Practice,” 2008, https://doi.
org/10.4271/2008-01-1068 .
 2
3.
 M
ontanaro, A., Allocca, L., and Lazzaro, M., “Iso-Octane 
Spray from a gdi Multi-Hole Injector under Non- and Flash 
Boiling Conditions,” in International Powertrains, Fuels and 
Lubricants Meeting , SAE International, 2017, https://doi.
org/10.4271/2017-01-2319.
Downloaded from SAE International by Dalian Univ of Technology, Monday, August 31, 2026

<!-- PDF_PAGE: 15 -->

© 2020 SAE International. All rights reserved. No part of this publication may be reproduced, stored in a retrieval system, or transmitted, in any form or by any means, 
electronic, mechanical, photocopying, recording, or otherwise, without the prior written permission of SAE International.
Positions and opinions advanced in this work are those of the author(s) and not necessarily those of SAE International. Responsibility for the content of the work lies 
solely with the author(s).
ISSN 0148-7191
 15
UNDER-EXPANDED GASEOUS JETS CHARACTERIZATION FOR APPLICATION IN DIRECT INJECTION ENGINES
 24. V era-Tudela, W., Kyrtatos, P., Schneider, B., Boulouchos, K., 
and Willmann, M., “An Experimental Study on the Effects of 
Needle Dynamics on the Penetration of a High-Pressure 
Methane Jet,” Fuel 253:79-89, 2019, doi:10.1016/j.
fuel.2019.04.171.
 2
5.
 S
tockman, G. and Shapiro, L.G., Computer Vision  First 
Edition (Upper Saddle River, NJ: Prentice Hall PTR, 2001).
 2
6.
 V
eersteg, H., Malalasekera, W., “An Introduction to 
Computational Fluid Dynamics ,” 1995.
 2
7.
 R
ichards, K., Senecal, P., and Pomraning, E., Converge 
Manual (Version 2.4) (Madison, WI-USA: Convergent 
Science Inc., 2016).
 2
8.
 Y
u, J., Vuorinen, V., Kaario, O., Sarjovaara, T., and Larmi, 
M., “Visualization and Analysis of the Characteristics of 
Transitional Underexpanded Jets,” International Journal of 
Heat and Fluid Flow 44:140-154, 2013, doi:10.1016/J.
IJHEATFLUIDFLOW.2013.05.015.
 2
9.
 F
ranquet, E., Perrier, V., Gibout, S., and Bruel, P., “Review on 
the Underexpanded Jets,” 2015, doi:10.13140/
RG.2.1.2640.6883 .
Contact Information
Luigi Allocca
Istituto Motori CNR
l.allocca@im.cnr.it
Viale Marconi, 4 - 80125 Napoli - ITALY
Phone +39 081 7177223 Fax +39 081 2396097
Definitions/Abbreviations
AMR - Adaptive Mesh Refinement
CFD - Computational Fluid Dynamics
CFL - Courant-Friedrichs-Lewy number
CI - Compression Ignition
CNG - Compressed Natural Gas
CVC - Constant Volume Chamber
DI - Direct Injection
DI-CNG - Compressed Natural Gas Direct Injection
fps - frame per second
GDI - Gasoline Direct Injection
ICE - Internal Combustion Engines
LED - Light Emitting Diode
LES - Large Eddy Simulation
NG - Natural Gas
NPR - Net Pressure Ratio
p
ch - nitrogen chamber pressure
PDF - Probability Density Function
PECU - Programmable Electronic Control Unit
PFI - Port Fuel Injected
pinj - gas injection pressure
PISO - Pressure Implicit Split Operator
RANS - Reynolds-Averaged Navier-Stokes
SI - Spark Ignition
SOI - Start of Injection
T
ch - chamber temperature
TTL - Transistor-Transistor Logic
URANS - Unsteady Reynolds-Averaged Navier-Stokes
X
disk - Mach disk height
yCH4 - methane mass fraction
Downloaded from SAE International by Dalian Univ of Technology, Monday, August 31, 2026
