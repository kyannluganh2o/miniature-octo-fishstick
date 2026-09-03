<!-- PDF_PAGE: 1 -->

ViewOnline
ExportCitation
RESEARCH ARTICLE |  JUNE 14 2022
Numerical investigations on the deformation and breakup of
an n-decane droplet induced by a shock wave
Wanli Zhu (朱万里) 
  ; Hongtao Zheng (郑洪涛) 
  ; Ningbo Zhao (赵宁波)  
Physics of Fluids 34, 063306 (2022)
https://doi.org/10.1063/5.0093291
Articles You May Be Interested In
Effect of airflow pressure on the droplet breakup in the shear breakup regime
Physics of Fluids (May 2021)
An experimental study on the influence of airflow temperature on the different silicone oil droplet breakup
regimes
Physics of Fluids (September 2022)
Decane under shear: A molecular dynamics study using reversible NVT ‐ SLLOD and NPT ‐ SLLOD
algorithms
J. Chem. Phys. (December 1995)
 29 August 2026 09:14:55

<!-- PDF_PAGE: 2 -->

Numerical investigations on the deformation
and breakup of an n-decane droplet induced
by a shock wave
Cite as: Phys. Fluids 34, 063306 (2022); doi: 10.1063/5.0093291
Submitted: 28 March 2022 . Accepted: 29 May 2022 .
Published Online: 14 June 2022
Wanli Zhu (朱万里),
 Hongtao Zheng (郑洪涛),
 and Ningbo Zhao (赵宁波)a)
AFFILIATIONS
College of Power and Energy Engineering, Harbin Engineering University, Harbin 150001, China
a)Author to whom correspondence should be addressed: zhaoningboheu@126.com
ABSTRACT
This paper adopts the coupled level-set and volume-of-fluid and the large eddy simulation methods to simulate the deformation and breakup
of an n-decane droplet under the action of a shock wave. We aim to investigate the effects of the shock Mach number and droplet diameter
on temporary deformation and breakup characteristics at high Weber numbers from 5813 to 22 380. Additionally, special attention is paid to
subsequent sub-droplet size distributions, which many researchers generally ignore. The results indicate that the evolution of droplet defor-
mation and breakup in the shear breakup regime generally agrees with the obtained experimental data. Based on the present methods, the
physical mechanisms for variations of multiple recirculation zones and the development of Kelvin –Helmholtz instability in wave formation
are discussed. Larger shock Mach number and smaller droplet diameter can significantly increase the cross-stream and stream-wise deforma-
tions. Moreover, both relaxation and breakup times are directly proportional to the initial droplet diameters but inversely proportional to the
shock Mach numbers. Eventually, as the shock Mach number increases, the superficial area and mass ratios of sub-droplets to parent droplets
all increase from 5.596 to 8.278 and from 23.38% to 38.38%, while the ratios increase from 2.652 to 18.523 and from 4.63% to 92.7%, respec-
tively, as the droplet diameter decreases.
Published under an exclusive license by AIP Publishing. https://doi.org/10.1063/5.0093291
I. INTRODUCTION
The secondary breakup of a droplet is a fundamental process of
atomization and sprays, which is a complicated two-phase flow prob-
lem. Extensive studies have been conducted on the problem for more
than half a century due to its scientific and industrial applications,
such as raindrops,
1 inkjet printing, 2 sprays,3–5 and liquid jets. 6,7
Unfortunately, most preceding investigations are conducted in sub-
sonic airflows8,9 where the effect of the airflow compressibility is mar-
ginal. With the recent development of supersonic combustion systems,
including detonation engines,
10,11 scramjet engines,12 and supersonic gas
atomizers,13 the shock wave-induced secondary breakup of fuel droplets
has increased importance in high-speed flow scenarios. The current
study is mainly motivated by an interest in liquid-fueled detonation
engines, including rotating detonation engines (RDEs),
14,15 pulse deto-
nation engines (PDEs),16,17 and oblique detonation engines (ODEs),18,19
where the fuel droplet interacts with a shock wave and undergoes defor-
mation, breakup, atomization, and vaporization before it mixes with air
and subsequently enhances the detonation and deflagration. However,
the droplet breakup is commonly associated with more uncertainty in
practical applications as the shock Mach numberM
s increases, leading
to more complicated problems. For this purpose, it is necessary to inves-
tigate droplet breakup under highly unstable conditions.
According to previous research, the onset of droplet breakup is
usually determined by the Weber numberWe. Classically, the breakup
has been categorized into five modes. In addition to the vibrational
regime (We /C20 12), four major breakup regimes are bag, multimode,
shear or stripping, and catastrophic, with the correspondingWe being
12–50, 50–10, 100–350, and >350, respectively.
20 Also, Xu et al.21 iden-
tified the butterfly breakup regime for the first time, considering the
effect of the shear layer of airflow. Many arguments can be synthesized
into the above classifications, including classical works
22,23 and recent
investigations.24,25 Besides, the mechanisms for the shear breakup have
significantly been debated. Jalaal and Mehravaran26 captured different
wave instabilities on the windward surface of droplets. Besides the
Kelvin–Helmholtz instability (KHI), they also captured the presence of
the transverse azimuthal modulation or the Rayleigh–Taylor instability
(RTI). Zhu et al.
27 concluded that the RTI waves play a critical role in
flattening deformation and stripping breakup. While Guanet al.28 and
Phys. Fluids 34, 063306 (2022); doi: 10.1063/5.0093291 34, 063306-1
Published under an exclusive license by AIP Publishing
Physics of Fluids ARTICLE scitation.org/journal/phf
 29 August 2026 09:14:55

<!-- PDF_PAGE: 3 -->

Wang et al.29 believed that the KHI waves dominated the shear breakup
in their work. Consequently, there is still much uncertainty about the
mechanisms of shear breakup.
In addition to the breakup mechanisms above, the breakup char-
acteristics of a droplet impacted by a shock wave have been examined.
Recently, using the high-speed shadowgraph technique, Shen et al.30
studied the transient deformation and breakup of a water droplet
affected by shock waves. They showed that the initiation time
decreases with increasing We numbers due to enhanced disruptive
inertia. Poplavski et al. 31 investigated the droplet deformation and
breakup in a horizontal shock tube. Comparison of simulation results
with experimental data indicated good agreements with the temporal
characteristics, i.e., morphology, dynamics, and induction time of the
breakup. Kaiser et al.32 investigated the shock-induced breakup of a
water column. They indicated that capillary and viscous forces have a
minor effect on integral parameters at the early breakup stage. Sharma
et al.
33 carried out the water droplet–shock wave interaction in a verti-
cal shock tube based on the exploding wire technique. They mentioned
that the breakup process could be recurrent until the complete droplet
disintegrates or external drag acting on the droplet was insufficient for
further disintegration. Overall, studies of the shock-induced shear
breakup in the literature focus on the early stages of droplet breakup
and the shock wave dynamics without investigating the later stages of
atomization and mist development.
Current numerical approaches for simulating the breakup pro-
cess can be primarily divided into the Euler–Lagrange and Euler–Euler
methods.34 For the Euler–Lagrange approach, the strategy for the liq-
uid phase is usually tracked by the Lagrangian Particle Tracking (LPT)
technology, such as the Discrete Phase Model (DPM),6,13 especially for
liquid jets concerned with the breakup process. Since breakup mecha-
nisms are determined by processes on both sides of the phase interface,
such problems with the resolution of the small-scale process are avail-
a b l ef o rt h eE u l e r–Euler method. There are two popular models for
predicting complex interfaces. One is the interface-capturing model,
such as the five-equation model, 28,35 and the other is the interface-
tracking model, such as the volume of fluid (VOF),31,36 level set (LS),37
and coupled Level Set and Volume of Fluid (CLSVOF) models. 7,34
Moreover, the CLSVOF model takes advantage of both the mass con-
servation of the VOF model and the sharp interface capturing of the
LS model. Many studies of droplet breakup have been reported in the
literature by the CLSVOF model. Zhu et al.
7 and Zhao et al.34 focused
on the primary atomization morphology and droplet dynamics, while
the details of the droplet deformation cannot be obtained. To accu-
rately capture the deformation morphology and sub-droplet distribu-
tions, we adopted the CLSVOF model to simulate the droplet
deformation and breakup induced by shock waves.
Although the existing experimental and numerical works have
made explicit progress, a limited number of publications utilize a fuel
droplet rather than a water droplet as the test fluid. Thus, we focus on
an n-decane (n-C 10H22) droplet as the subject mainly motivated by
practical interest. Furthermore, to the author ’s best knowledge, the
data on the entire evolution of the stripping breakup regime, including
fast deformation, subsequent shear breakup, and even the complete
atomization of the parent droplet, are still lacking. Based on the
reasons mentioned above, the objective of this work is to investigate
the effects exerted by the shock Mach number and droplet diameter
on the breakup mechanism and temporal characteristics, including
cross-stream and stream-wise deformations, breakup times, and so on.
Moreover, this paper pays more attention to the sub-droplet distribu-
tions. The rest of the manuscript is organized as below. Governing
equations and numerical implementation are specified in Sec. II.T h e
physical model and numerical validation are introduced in Sec. III.
Numerical results and discussions are presented in Sec. IV,a n dt h e
vital conclusions are summarized in Sec.V.
II. GOVERNING EQUATION AND NUMERICAL
IMPLEMENTATION
A. Governing equations
The droplet deformation and breakup induced by shock waves
are numerically simulated with two models. Estimates show that the
Reynolds numbers Re during the flow around a droplet vary from
about 39 679 to 62 774. Therefore, a turbulence model is used to calcu-
late the turbulent flow conditions of the droplet and shock in each
phase. Additionally, a two-phase tracking model is used to capture the
gas-liquid interface.
1. The turbulence modeling based on the LES model
The large eddy simulation (LES) model is an advanced method
for fundamental research on turbulent flows, and it has been widely
used to calculate the problem of droplet deformation and breakup.27,31
Therefore, the LES model is used for turbulence modeling in this
paper. The mesh size is used as the filter, and the scale that is smaller
than the filter width, also termed the sub-grid scale (SGS), is removed
from the variables. Then, the governing equations for the LES are the
filtered continuity and momentum conservation equations in the fol-
lowing forms:
@q
@t þ @ q~uiðÞ
@xi
¼ 0; (1)
@ q~uiðÞ
@t þ
@ q~ui~uj
/C0/C1
@xj
"#
¼/C0 @~p
@xi
þ @
@xj
l @rij
@xj
 !
/C0 @sij
@xj
; (2)
rij ¼ l @~ui
@xj
þ @~uj
@xi
 !"#
/C0 2
3 l @~ui
@xi
dij; (3)
where ~/C1ðÞ denotes a filtered quantity, ui is the velocity component in
the direction xi, t is the time, p is the pressure, l is the kinematic vis-
cosity, rij is the viscous stress tensor,dij is the Kronecker delta that is 1
only when i ¼ j, and otherwise is 0, sij and skk are sub-grid scale
(SGS) stress tensors, the model used to provide closure is often called
the SGS model, which usually follows the Boussinesq hypothesis:
sij /C0 1
3 skkdij ¼/C0 2lt~Sij; (4)
where lt is called the sub-grid viscosity, ~Sij is a strain rate tensor, and
~Sij ¼ @~ui=@xj þ @~uj=@xi
/C0/C1 =2. According to the Smagorinsky
model,38 the SGS turbulent viscositylt can be expressed as
lt ¼ q CsDðÞ 2 ~Sjj ; (5)
where Sjj is the magnitude of the strain rate defined as ~Sjj ¼
ﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ
2~Sij~Sij
q
,
CS is the Smagorinsky constant, andD is the filter width.
Physics of Fluids ARTICLE scitation.org/journal/phf
Phys. Fluids 34, 063306 (2022); doi: 10.1063/5.0093291 34, 063306-2
Published under an exclusive license by AIP Publishing
 29 August 2026 09:14:55

<!-- PDF_PAGE: 4 -->

2. Interface tracking based on the CLSVOF model
The VOF model 39 is simple and can maintain the conservation
of the fluid volume, while the LS model 40 is suitable for solving
the problem of interface curvature. The VOF model can avoid the
non-conservation of mass of the LS model, while the LS model can
optimize the solution for the normal direction and precision of the
curvature. Therefore, the CLSVOF model, introduced recently by
many researchers,
41,42 takes advantage of the two models. For the
VOF model, the volume fraction is introduced because gas and liquid
are not interpenetrating. In each volume, volume fractions of gas and
liquid phases sum to 1,
a
g þ al ¼ 1; (6)
where g and l represent the gas and liquid phases, respectively,a is the
volume fraction in a computational cell where is located in the liquid if
a ¼ 1, in the gas if a ¼ 0, and at the gas –liquid interface if 0 < a < 1.
The VOF equation is solved to ensure mass conservative. Therefore,
the following continuous equation for the volume fraction of each
phase is solved to track the interface between phases:
@ aqðÞ
@t þr/C1 aquðÞ ¼ 0; (7)
where u is the velocity vector and the local fluid density q and
dynamic viscosity l are governed by the following equations,
respectively,
qaðÞ ¼ ql al þ qg 1 /C0 alðÞ ; (8)
laðÞ ¼ ll al þ lg 1 /C0 alðÞ : (9)
The LS model describes the interface using a signed distance
function /, the value is zero at the interface, positive and negative in
the liquid and gas phases, respectively. An initial value of the LS func-
tion is defined from the VOF equation, and then, a re-initialization is
performed to obtain the newly signed distance function /. The level-
set function can be rewritten as a function similar to the VOF
equation,
@ /ðÞ
@t þr/C1 u/ðÞ ¼ 0: (10)
Moreover, smoothed Heaviside function H /ðÞ ensures the con-
tinuous variation of physical properties. The phase properties are typi-
cally interpolated across the interface as
q/ðÞ ¼ q
l H /ðÞ þ qg 1 /C0 H /ðÞðÞ ; (11)
l/ðÞ ¼ ll H /ðÞ þ lg 1 /C0 H /ðÞðÞ : (12)
In Eqs.(11) and (12), the Heaviside functionH /ðÞ is expressed as
H /ðÞ ¼
0; / < /C0 e;
1
2 1 þ /
e þ 1
p sin p/
e
/C18/C19/C20/C21
; /jj /C20 e;
1; / > e;
8
>>
>
>
<
>>>>
:
(13)
where this function is defined as a positive or negative distancee from
the interface where the value ofe is a small parameter of the mesh ele-
ment size typically taken to be 1.5 times the mesh size.
43,44
The surface tensionFr is corrected by/ as
Fr ¼ rj /ðÞ d/ðÞ r /ðÞ ; (14)
where j/ðÞ is the interface curvature withj/ðÞ ¼r/C1 n. n is the nor-
mal vector on the interface,n ¼r /ðÞ = r /ðÞ
/C12/C12 /C12/C12 , which can be accurate
due to the continuous LS function. d/ðÞ is the Dirac function to limit
the influence of surface tension within the interface,
d/ðÞ ¼ dH /ðÞ
d/ ¼
0; /jj > e;
1
2e 1 þ cos p/
e
/C18/C19/C20/C21
; /jj /C20 e:
8
><
>:
(15)
B. Numerical implementation
The ANSYS Fluent 18.0 is adopted in the numerical simulations,
where the finite volume method45 is used to solve the governing equa-
tion discretely. The coupling of pressure and velocity is implemented
by the pressure implicit with the splitting of operators (PISOs) algo-
rithm,46 which is performed through predictor and corrector of the
velocity and pressure field. The pressure staggering option (PRESTO!)
scheme27,31 is used for pressure discretization, especially for these sim-
ulations’ problems with strong body forces and high-density ratios.
This discretization gives more accurate results since interpolation
errors and pressure gradients for the boundaries are avoided. The
explicit solver with the geo-reconstruct discretization scheme 27,31 is
used to solve the volume fraction equations. The second-order upwind
discretization is adopted for the continuity, energy equations, and
level-set function and the bounded-central differencing discretization
is used for the momentum equation.47 Numerical stability conditions
should also limit the computational time step since the developed solu-
tion procedure is explicit. Advection on arbitrary small mesh could
require minimal time steps to satisfy the Courant –Friedrichs–Lewy
(CFL) condition.
42 T h et i m es t e pa d o p t e df o re a c hc a s ei s0 . 0 4lsw i t h
t h em a x i m u mC F Ln u m b e rb e l o w0 . 5i nt h i sp a p e r .
III. PHYSICAL MODEL AND NUMERICAL VALIDATION
A. Problem description and simulation setup
Deformation and subsequent breakup occur when a droplet is
suddenly exposed to high-speed and high-pressure airflows, which are
usually generated in shock tubes due to their simplicity and repeatabil-
ity. According to the two-dimensional (2D) approach, the geometry of
the shock tube is schematically depicted by the rectangular domain, as
sketched in Fig. 1, where the stream-wise and cross-stream directions
are denoted by the x and y directions, respectively. As shown inFig. 1
(a), the domain is divided into the driver section ( L
x1 ¼ 200 mm) and
driven section ( Lx2 ¼ 1300 mm) using a virtual cross diaphragm,
which corresponds to the position of x ¼ 0 between the two different
pressure and density zones. The parent droplet with initial diameter
D0 is set at the center of the driven section. By referring to the compu-
tational domains from the works of Jalaal and Mehravaran26 and Zhu
et al.,27 the cross-stream size of L y ¼ 20 mm> 5 D0 is considered to
minimize the influence of the domain boundary conditions on the
droplet dynamics. Figure 1(b) schematically describes the formation
and propagation of the shock and expansion waves, and the x, t coor-
dinates represent the position and time, respectively. The driver and
driven sections are initially filled with high- and low-pressure air. At
Physics of Fluids ARTICLE scitation.org/journal/phf
Phys. Fluids 34, 063306 (2022); doi: 10.1063/5.0093291 34, 063306-3
Published under an exclusive license by AIP Publishing
 29 August 2026 09:14:55

<!-- PDF_PAGE: 5 -->

t ¼ 0, the airflow in the undisturbed driver section and the driven sec-
tion is marked as zones (4) and (1). At t > 0, the shock wave and a set
of expansion waves are synchronously generated but propagate in the
opposite direction due to the appropriate pressure differential. The air-
flows behind the shock wave and expansion wave are marked as zones
(2) and (3). In the following, the initial airflow parameters at different
zones are indicated by subscripts 1 –4. There would be a contact sur-
face where p
2 ¼ p3 between zones (2) and (3) at different densities
and temperatures. Note that the sustainable time of airflows in the
zone (2) is also known as the test time, during which the shock wave
can purely compress the uniform airflow.
Based on the problem description above, boundary and initial
conditions should be set to fit with the computational conditions, and
thus, the pressure outlet boundary condition is imposed at the right
end of the computational domain, and no-slip boundary conditions
are applied at the other walls. Furthermore, the two sections were ini-
tialized with the same temperature ( T
4=T1 ¼ 298.15 K) and very dif-
ferent pressures (p4=p1 /C29 1; p1 ¼ 1 atm), with the ideal gas air being
at rest on either side (V4 ¼ V1 ¼ 0). Based on the initial conditions, a
normal shock forms and travels toward the right side (driven section),
while a set of expansion waves propagate toward the left one (driver
section). Given the parameters of high-pressure p4 and low-pressure
p1 on the left- and right-hand sides of the tube, as well as the thermo-
dynamic parameters, the prescribed shock Mach number Ms can be
initially derived from analytical expression48 as below
b ¼ 2c1
c1 þ 1 M2
s /C0 c1 /C0 1
c1 þ 1
/C18/C19
1 /C0 c4 /C0 1
c1 þ 1
c1
c4
Ms /C0 1
Ms
/C18/C19/C20/C21 /C0 2c4
c4 /C0 1
;
(16)
where the compression ratiob ¼ p4=p1, c is the speed of sound, and c
is the specific heat ratio. The test fuel droplet is an isolated n-C 10H22
droplet suggested by many researchers as a major component in the
surrogates for jet and diesel fuels.49,50 The following properties of the
n-C10H22 droplet are employed: density ql ¼ 730 kg/m3, viscosity
ll ¼ 0.0024 kg/m s, and surface tension coefficient r ¼ 0.026 N/m.
Moreover, the droplet deformation and breakup induced by shock
waves can be determined by the following dimensionless parameters:
the Weber number (We ¼ q2 V2ðÞ 2D0=r)i st h er a t i oo fa i r f l o w’s iner-
tia force to droplet ’s surface tension force, the Ohnesorge number
[Oh¼ ll = ql D0rðÞ 1=2] is the ratio of the viscous force to the surface
tension force, the Reynolds number (Re¼ q2V2D0=l2) is the ratio of
the inertial force to the viscous force, and the density ratio
(e ¼ q
l =q2), where the subscript l represents the liquid droplet and p,
q, V, r; and l are the pressure, density, velocity, surface tension coeffi-
cient, and dynamic viscosity of fluids, respectively. The test conditions
are obtained by varying shock Mach numbers M
s and droplet diame-
ters D0. The calculated Ohnesorge numbers are less than 0.1, so the
viscous effects can be negligible.20,23 The initial parameters in the cur-
rent simulation cases are mainly summarized inTable I.
B. Mesh sensitivity analysis
The adaptive mesh refinement (AMR) maintains a nested hierar-
chy of higher-resolution subgrids whose distribution is updated
dynamically during the calculation to enhance spatial resolution and
accuracy in regions of interest.
27 A mesh independence study is per-
formed with the mesh sizes of h ¼ 10, 20, and 40 lm, corresponding
to three kinds of mesh resolutions of D0=h ¼ 67.5, 135, and 270,
where h is the mesh size after refinement. Figure 2 shows the numeri-
cal results of the dimensionless cross-stream and stream-wise diame-
ters, Dcro=D0 and Dstr=D0, which are typically used to quantify the
time-dependent droplet morphology.51 I tc a nb es e e nt h a tt h e r ei sa
noteworthy deviation of the above dimensionless diameters between
the mesh resolution of D0=h ¼ 67.5 and the mesh resolution of
D0=h ¼ 135, while the dimensionless diameters almost overlap
between D0=h ¼ 135 and D0=h ¼ 270, indicating that the droplet
deformation and breakup are nearly independent of the mesh size
when D
0=h ¼ 135. Therefore, a resolution of D0=h ¼ 135 is used in
the following simulations in consideration of the computational accu-
racy and cost.
In addition, it is necessary to evaluate the accumulation of errors,
which is dependent on the computation strategies, mesh resolution,
and the number of time steps. By referring to Smirnov et al.,52,53 the
accumulated errors can be calculated by
Serr ¼ ﬃﬃﬃnp /C1
Xz
i¼1
h
Li
/C18/C19 kþ1
; (17)
where Serr is the total accumulated error which should not exceed 5%.
h and Li are the mesh size and domain size in i direction, respectively.
k ¼ 2i st h eo r d e ro fa c c u r a c yo fn u m e r i c a ls c h e m e ,z ¼ 2i st h e
FIG. 1. A schematic of wave propagation in the 2D computational domain used for
the simulation setup.
TABLE I. Detailed parameters of the current simulations under initial conditions.
Cases b Ms D0/mm We Oh Re e
1 4.98 1.4 2.2 6 549 0.011 672 39 679 365
2 7.04 1.5 2.2 10 657 0.011 672 51 149 331
3 9.82 1.6 2.2 15 916 0.011 672 62 919 304
4 13.56 1.7 2.2 22 380 0.011 672 74 831 281
5 7.04 1.5 1.2 5 813 0.015 804 27 900 331
6 7.04 1.5 1.7 8 235 0.013 278 39 525 331
7 7.04 1.5 2.7 13 080 0.010 536 62 774 331
Physics of Fluids ARTICLE scitation.org/journal/phf
Phys. Fluids 34, 063306 (2022); doi: 10.1063/5.0093291 34, 063306-4
Published under an exclusive license by AIP Publishing
 29 August 2026 09:14:55

<!-- PDF_PAGE: 6 -->

number of directions in integration, and n ¼ 40 000 is the number of
time steps. In the current simulations, to ensure the calculation accu-
racy, the accumulated errors Serr are not exceed 0.0013% within the
acceptable range.
C. Numerical verification and validation
By comparing the numerical results obtained with the well-
known exact analytical solution or benchmark numerical solutions for
the purpose of the numerical verification. To validate the
discontinuity-capturing capability of including the shock wave, contact
discontinuity and expansion wave, the modified version of the Sod ’s
shock tube problem,54 first introduced by Fedkiwet al.,55 is considered
as our test case. The shock tube is initially filled with mixtures of
H2/O2/Ar (20%: 10%: 70% by volume fraction). Additionally, the
length of the shock tube is 0.1 m, and the position of the diaphragm is
x ¼ 0.05 m. The initial conditions for the left and right states are
T; u; pðÞ ¼
400K; 0; 8000 PaðÞ ;
1200K; 0; 80 000 PaðÞ ;
x /C20 0:05 m;
x > 0:05 m:
(
(18)
In the simulation case, the computational domain is discretized
with 400 uniform cells and the CFL number is 0.02. Figure 3 shows
our numerical results compared with the analytical data55 at t ¼ 40 ls.
Since the analytical data on the specific heat ratio are lacking, instead,
we compare the numerical results with simulation data by Huang
et al.56 Under the initial condition, the strong shock wave and contact
discontinuity would propagate to the left while the expansion wave
would propagate in the opposite direction. As shown in Fig. 3 ,t h e
shock front, contact surface, and rarefaction waves are sharply cap-
tured, indicating the present numerical results are in good qualitative
agreement with exact analytic and benchmark simulation data.
For the problem of droplet deformation and breakup, the quanti-
tative validation of the numerical method is performed by examining
characteristic parameters of the deformed droplet vs time compared
with the experimental data of Poplavski et al.31 The initial test condi-
tion is consistent with the available experimental data, which were car-
ried out in a horizontal shock tube. In their work, experimental data of
droplet morphology were visualized and measured based on the shad-
owgraph method, by which the interval between frames is 306 0.1 ls.
The shadowgraph images provided a quasi-2D interface, data are from
a center slice of the interface, and, thus, 2D simulations are appropriate
for comparison. Figure 4 compares the dimensionless cross-stream
diameter (D
cro=D0) between the experimental and numerical data at
different time instants. In particular, the complex structures of the
shear breakup mode with small scales are captured in both the experi-
ment and simulation, as shown by the image inFig. 4. There is a devia-
tion interval at a late breakup and atomization stage ( t ¼ 390 ls).
Actually, the sub-droplets are stripped from the radial periphery of the
parent droplet, which may reduce the value of D
cro=D0. That is, the
Dcro=D0 would reach a maximum and minimum value when the dis-
tinguished sub-droplets are taken into account into the statistical data
or not. However, the mist is generated as a dark shadow in the experi-
ment, which would significantly obscure the parent droplet and look
larger than the numerical results. Here, for facilitating comparison
under different conditions, the instantaneous data of D
cro=D0 in the
current simulations are determined without the extra sub-droplets
from the previous work.
20,27 Therefore, the maximum error in any of
the Dcro=D0 measurements is estimated at no more than 6.5%, which
shows a relatively good agreement between the numerical simulation
and the experimental data. In summary, the present numerical meth-
odology is proven to reveal the droplet deformation and breakup
induced by the shock wave reasonably.
IV. RESULTS AND DISCUSSIONS
A. Deformation and breakup process
The features of the airflow field surrounding a droplet are condu-
cive to understanding the droplet deformation and breakup mecha-
nism.
57 Figure 5 shows the shock dynamics in the temporal evolution
of the airflow’s pressure, temperature, and velocity fields coupled with
different wave patterns for case 5 at the early breakup stage, where the
white outline clearly illustrates the droplet morphology. As shown in
Fig. 5 , the parent droplet shows no shape change immediately after
being struck by the shock wave for nearly 3.16 ls. It is mainly because
the shock-passage time is much shorter than the relaxation time tr
observed by Kaiser,32 during which the initial droplet would retain its
coherent structure. However, after the relaxation timetr, there existed
a slight corrugation on the windward surface of the droplet att ¼ 4 ls.
The corrugation is also an evidence that the droplet should not be
quiescent. Moreover, WS is the windward stagnation point, LS is the
leeward stagnation point, and EQ is the equator of the parent droplet.
Typical wave patterns include the incident shock (IS), reflected shock
(RS), diffracted shock (DS), and transmitted shock (TS) waves. More
specifically, the RS wave is formed and propagates upstream, and the
DS wave encloses the droplet, whereas the TS wave, much faster than
the IS wave, propagates inside the droplet. As is shown in Fig. 5(b),a
triple point (TP) is formed at the intersection of the IS wave, RS wave,
and Mach stem (MS) att ¼ 2 ls. As observed by the temperature field,
the impacted wave reflection becomes a Mach reflection at a certain
angle, as observed by the temperature field, the dashed box att ¼ 6 ls
represents an enlarged MS area. Additionally, the uniform airflow
FIG. 2. Evolution of the dimensionless cross-stream and stream-wise diameters,
Dcro=D0 and Dstr =D0, with different mesh resolutions (case 7).
Physics of Fluids ARTICLE scitation.org/journal/phf
Phys. Fluids 34, 063306 (2022); doi: 10.1063/5.0093291 34, 063306-5
Published under an exclusive license by AIP Publishing
 29 August 2026 09:14:55

<!-- PDF_PAGE: 7 -->

with high velocity, pressure, and temperature parameters follows the
IS wave before the shock –droplet interaction. In contrast, the formed
RS wave deflects the uniform airflow as it passes through it. A low-
pressure region is formed near the EQ, where the external flow velocity
is comparatively higher. As illustrated in Fig. 5(a), the high-pressure
differences established between the windward and leeward sides of the
parent droplet, leading to the droplet deformation and subsequent
shear breakup. The Mach–Mach collision occurs at LS, which would
create a local high-pressure and high-temperature region and also pro-
mote droplet deformation. Moreover, external airflows with different
velocities in the wake of the parent droplet further form the multiple
recirculation zones (RZs) discussed below.
There are a series of complex flow phenomena in the airflow field
due to the shock–droplet interaction, such as the generation and evo-
lution of vortices. Here, we focus on the vortex structures near the fuel
droplet and the effect that the shock wave has on the development of
vortices. The Q-criterion or Q-value is used to highlight the vortex
cores, which is one of the most popular vortex identification methods
proposed by Huntet al.
58 Recently, detailed descriptions ofQ-criterion
have been introduced by Buren et al.59 and Gao and Liu.60 More spe-
cifically, based on the eigenvalues of the velocity gradient tensorru or
the related invariants, theQ is equal to the residual of rotation rate ten-
sor norm squared subtracted from the strain rate tensor norm squared,
and, thus, Q can be expressed as
FIG. 3. Comparisons of present numerical results with analytical data 55 and simulation data 56 for the Sod ’s shock tube problem: (a) density, (b) temperature, (c) velocity, and
(d) specific heat ratio.
Physics of Fluids ARTICLE scitation.org/journal/phf
Phys. Fluids 34, 063306 (2022); doi: 10.1063/5.0093291 34, 063306-6
Published under an exclusive license by AIP Publishing
 29 August 2026 09:14:55

<!-- PDF_PAGE: 8 -->

Q ¼ 1
2 kXk2 /C0k Sk2/C0/C1
; (19)
where X ¼ 1=2ðru /C0r uðÞ TÞ and S ¼ 1=2ðru þr uðÞ TÞ are rota-
tion rate and strain rate tensors, respectively. Thus, Q represents the
local balance between shear strain rate and vorticity magnitude.
Positive Q-values give prominence to regions of high swirl in compari-
son to shear to represent coherent vortices. And, the larger theQ-value
is, the greater the vortex intensity is. Figure 6 shows different intensi-
ties of vortex structures visualized by the Q-criterion and their evolu-
tions at different time instants. Unsteady vortex shedding after the
shock passage forms multiple recirculation zones (RZs). Typical fea-
tures of RZs, including windward RZ, wake RZ, and sheet RZ, are
identified in different locations, as shown inFig. 6.
At t ¼ 0 ls, there is no vortex in the potential flow. The wind-
ward RZ primarily appears at the windward surface of the droplet
once the velocity field is established and induced by the IS wave.
Gradually, the windward RZ becomes larger and successively moves
from the center to the equator when the shock wave completely passes
through the droplet (0 < t < 4 ls). The larger the windward RZ, the
stronger the shearing force of airflows. At t ¼ 6 ls, due to the flow
separation, the wake RZ is formed near the LS with the development
FIG. 4. Quantitative comparison of the dimensionless cross-stream diameter
Dcro=D0 between the present numerical results and experimental data. 31
FIG. 5. Evolutions of the airflow (a) pressure, (b) temperature, and (c) velocity coupled with different wave patterns at an early stage of droplet deformati on.
Physics of Fluids ARTICLE scitation.org/journal/phf
Phys. Fluids 34, 063306 (2022); doi: 10.1063/5.0093291 34, 063306-7
Published under an exclusive license by AIP Publishing
 29 August 2026 09:14:55

<!-- PDF_PAGE: 9 -->

of external airflow surrounding the droplet periphery. The increasing
flow separation makes the wake RZ become more marked over time
after the shock-droplet collision, leading to a flattened droplet in the
leeward side (6 < t < 14 ls). By inspection of the droplet morphology
at t ¼ 19 ls, due to the expanding region of windward RZ, the KHI
waves on the windward surface, similar to the observations of Jalaal
and Mehravaran,
26 tend to be unstable and become more evident
when there is a divergent velocity difference between two fluids sepa-
rated by a perturbed interface. At the same time, the huge pressure dif-
ference between WS and LS makes the parent droplet distort from its
undisturbed circular shape and then become flattened to form an
oblate ellipsoid. Especially, on the one hand, the direct stripping pro-
cess of KHI waves can promote the shear breakup with fine mist dis-
tributed on the windward surface along with the droplet deformation,
which is different from the phenomenon that breakup always occurs
after the parent droplet deformation in subsonic flow conditions. On
the other hand, the fragmentation of the KHI waves makes the parent
droplet more prone to distortion and deformation, in turn. The KHI
waves continuously grow with the time elapsed, merge, and finally
turn into sheets or ligaments near the EQ point at t ¼ 28 ls. As a
result, the stretching of sheets and ligaments accompanied by the KHI
waves stripping will increase the cross-stream deformation of the par-
ent droplet. At the same time, the vortices shedding in the wake RZ
become weak and produce the secondary vortices and many more.
And these vortices are also combined to form another sheet RZ located
between the sheet and wake RZs. Therefore, the sheet at each EQ point
can be enlarged due to the combined effect of the windward and sheet
RZs. When the aerodynamic shearing force of the airflow is strong
enough to break the sheets into fragments, ligaments, and sub-
droplets, which could reduce the cross-stream deformation of the par-
ent droplet. Moreover, there is a rollback structure of the peripheral lip
generated at the leeward side of the droplet due to conjunct interac-
tions of the sheet and wake RZs. The sub-droplets are mainly stripped
f r o mt h er a d i a lp e r i p h e r yo ft h ep a r e n td r o p l e t ,w h i c hu n d e r g o e s
deformation, instability wave stripping, ligament, and lip fragmenta-
tions until completely stripped and atomized. As discussed above, the
larger sub-droplets of shear breakup are largely attributed to fragmen-
tations of the sheets, ligaments, and lips rather than the direct KHI
wave stripping. However, the initial generation and development of
the KHI waves on the windward surface still play an important role
during the deformation and shear breakup processes.
B. Deformation extents and breakup times
The study of droplet deformation is essential for understanding
the subsequent droplet breakup. Figure 7 shows the time-resolved
droplet morphologies at different Mach number ( M
s ¼ 1.4–1.7) and
droplet diameter (D0 ¼ 1.2–2.7 mm) conditions. As shown in Fig. 7,
similar shear breakup regimes occur at the early breakup stage
(t ¼ 20–100 ls), and the time interval for each image is 20 ls.
However, the droplet morphology varies accordingly at different M
s
and D0 numbers. As shown inFig. 7(a),a t t ¼ 20 ls, due to the shear-
ing force of the airflow, the inconspicuous KHI waves have already
been generated on the windward surface for all cases. Nevertheless, the
initial parent droplets still keep round with smooth windward surfaces
owing to their relatively strong surface tension forces. As time goes on,
the KHI waves become more evident with increasing M
s.B yc o n t r a s t ,
as shown in Fig. 7(b), the KHI waves on the windward surface become
more prominent with decreasingD0. Overall, it may also be concluded
that the generations of KHI waves are prominent and unstable at
higher shock Mach numbers and lower droplet diameters. Moreover,
the extents of the deformation and breakup are significantly different
We conditions. In the following discussion, we mainly focus on the
FIG. 6. The vortices interact and form multiple recirculation zones at various time instants based on the Q-criterion.
Physics of Fluids ARTICLE scitation.org/journal/phf
Phys. Fluids 34, 063306 (2022); doi: 10.1063/5.0093291 34, 063306-8
Published under an exclusive license by AIP Publishing
 29 August 2026 09:14:55

<!-- PDF_PAGE: 10 -->

FIG. 7. Effects of (a) shock Mach number Ms and (b) droplet diameter D0 on the evolutions of droplet morphology at early stage of droplet breakup.
Physics of Fluids ARTICLE scitation.org/journal/phf
Phys. Fluids 34, 063306 (2022); doi: 10.1063/5.0093291 34, 063306-9
Published under an exclusive license by AIP Publishing
 29 August 2026 09:14:55

<!-- PDF_PAGE: 11 -->

quantitative effects of the shock Mach number and droplet diameter
on the dimensionless cross-stream and stream-wise diameters,
Dcro=D0 and Dstr=D0, at the early breakup stage.
Figures 8 and 9 show the effects of the two factors on temporal
characteristics of Dcro=D0 and Dstr=D0 growing with time at different
shock Mach numbers and droplet diameters. As shown in Fig. 8,f o u r
kinds of shock Mach numbers ( Ms ¼ 1.4–1.7) and a fixed droplet
diameter (D0 ¼ 2.2 mm) are selected, corresponding to We numbers
in the range of 6549 –22 380. As shown in Fig. 8 , the evolution of
Dcro=D0 shows a nearly exponential increasing trend with time, while
Dstr=D0 shows an opposite downward trend. As the Mach number
increases, the increasing differential pressure may promote overall
deformation and make the parent droplet unstable, and the enhance-
ment of shearing force of airflow with larger differential velocity may
enhance the generations of ligaments and sheets. Due to the stretching
of sheets and ligaments at the radial edge of the parent droplet, there is
a continuous expansion of D
cro=D0 even accompanied with ligament
and sheet fragmentations. At the same time, the parent droplet is
FIG. 8. Temporal variations of (a) the dimensionless cross-stream diameterDcro=D0 and (b) the dimensionless stream-wise diameterDstr=D0 at different shock Mach numbersMs.
FIG. 9. Temporal variations of (a) the dimensionless cross-stream diameter Dcro=D0 and (b) the dimensionless stream-wise diameter Dstr =D0 at different droplet diameters D0.
Physics of Fluids ARTICLE scitation.org/journal/phf
Phys. Fluids 34, 063306 (2022); doi: 10.1063/5.0093291 34, 063306-10
Published under an exclusive license by AIP Publishing
 29 August 2026 09:14:55

<!-- PDF_PAGE: 12 -->

continuously compressed and becomes thinner in the stream-wise
direction. Therefore, as Ms increases, the growth rate of Dcro=D0 and
Dstr=D0 is larger at higher We numbers due to the increasing aerody-
namic force of airflow behind the shock wave.
As shown in Fig. 9 , four kinds of droplet diameters
(D0 ¼ 1.2–2.7 mm) and a fixed shock Mach number ( Ms ¼ 1.5) are
selected, corresponding to We numbers in the range of 5813 –13 080.
Contrary to the conditions of changingMs above, the growing slope of
curves of Dcro=D0 and Dstr=D0 all decreases as droplet diameter D0
increases, resulting in a reduced growth rate of the droplet deforma-
tion. The We numbers of droplet become larger with the increase of
D0; however, the critical Weber numbersWecri are positively related to
initial droplet diameters D0. Also, to a large extent, the droplet defor-
mation depends not only on the resistance between the aerodynamic
force of airflow force and surface tension force but also on energy
transfer.7 When Ms is fixed in advance, the airflow aerodynamic
energy acting on the droplet is reduced in the unit surface area of the
droplet, restraining the growth rate of droplet deformation. Therefore,
increasing D
0 would inhibit the overall deformation of the parent
droplet. The results obtained above further show that shock Mach
number plays a positive role, but droplet diameter plays a negative role
i nt h eg r o w t hr a t eo fd r o p l e td e f o r m a t i o n .
As the discussions mentioned above, the parent droplets have sig-
nificantly different characteristics of the maximum dimensionless cross-
stream and stream-wise diameters, D
cro=D0ðÞ max and Dstr=D0ðÞ min,a t
t h ee n ds t a g eo fd r o p l e td e f o r m a t i o n .Figure 10 shows the effects of
shock Mach numberMs and droplet diameterD0 on Dcro=D0ðÞ max and
Dstr=D0ðÞ min.A ss h o w ni n Fig. 10(a),a s Ms increases, the values of
Dcro=D0ðÞ max and Dstr=D0ðÞ min turn into approximately 1.50–2.12 and
0.41–0.65, respectively. Besides, Dcro=D0ðÞ max increases on the whole,
but the evolution of Dstr=D0ðÞ min shows the opposite trend. In addition,
t h el a r g e rt h ev a l u eo fDcro=D0ðÞ max and the smaller the value of
Dstr=D0ðÞ min, the greater the extent of droplet deformation. As the
shock Mach numberMs increases, the parent droplet becomes longer in
the cross-stream direction and thinner in the stream-wise direction. It is
because the aerodynamic force is stronger enough to push the parent
droplet to move quickly from the center to the edge, making the liga-
ment and sheet larger and the body thinner. Different from the factor of
M
s,a ss h o w ni nFig. 10(b),a st h ed r o p l e td i a m e t e rD0 increases, the
evolutions of Dcro=D0ðÞ max and Dstr=D0ðÞ min show the opposite trend.
The values of Dcro=D0ðÞ max and Dstr=D0ðÞ min turn into approximately
1.52–3.23 and 0.25–0.63, respectively. As a consequence, the values of
Dcro=D0ðÞ max increase while the values of Dstr=D0ðÞ min decrease with
decreasing D0, indicating that cross-stream and stream-wise deforma-
tion extents are relatively larger at smaller droplet diameter.
It is instructive to examine the characteristics of the relaxation
time tr and total breakup time tb. Figures 11(a) and 11(b) show the
evolution of parent droplets’ tr and tb under different conditions. As
discussed above, the n-C 10H22 droplet showed no visible change in
shape immediately after the shock wave struck it at early stage of
shock–droplet interaction. This behavior agrees that relaxation time is
associated with every conceivable movement of matter. During the
relaxation time t
r, the signal for action is received, and the movement
mechanism is set into operation. As shown inFig. 11,a s Ms decreases,
the values of tr and tb range from 3.28 to 4.88 ls, and from 185 to 329
ls, respectively. While the values of tr and tb, respectively, range from
3.16 to 5.16 lsa n df r o m1 3 4t o2 7 6lsa s D0 increases. In the present
simulations, the relaxation time is relatively shorter and notr occupies
more than 2.36% of the total breakup times tb,i n d i c a t i n gt h a tt h es u s -
tainable times of the uniform airflows induced by the shock wave play
a more critical role in the entire shear breakup process. And, the relax-
ation and total breakup times are shorter, the smaller the mass of the
FIG. 10. Effects of (a) shock Mach number Ms and (b) droplet diameter D0 on the maximum dimensionless cross-stream diameter Dcro=D0ðÞ max and (c) the minimum dimen-
sionless stream-wise diameter Dstr =D0ðÞ min.
Physics of Fluids ARTICLE scitation.org/journal/phf
Phys. Fluids 34, 063306 (2022); doi: 10.1063/5.0093291 34, 063306-11
Published under an exclusive license by AIP Publishing
 29 August 2026 09:14:55

<!-- PDF_PAGE: 13 -->

parent droplet that is involved D0 and the stronger the signal for air-
flow that is given by the velocity of both the shock wave and airflow
behind it.
C. Sub-droplet distributions
The sub-droplets initially occur when the KHI waves, sheets, liga-
ments, and lips are disintegrated from the parent droplets in the shear
breakup regime. The sub-droplet breakup characteristics, including the
numbers and sizes, are processed with MATLAB ’s post-processing
tool.27 Figure 12shows the sub-droplets stripped from the parent droplet
at different shock Mach numbers and droplet diameters att ¼ 215 ls.
As shown in Fig. 12(a), the atomization extents of the parent droplet are
qualitatively larger at high-shock Mach numbersMs due to the high-
frequency wave crest stripping as well as fragmentations of ligaments,
sheets, and lips. Additionally, the parent droplets for cases 3–4 are disap-
peared and ultimately atomized into a fine mist, while the parent droplet
cores for cases 1–2 are still exist. In comparison, as shown inFig. 12(b),
the atomization extents of the parent droplet are lower at higher droplet
diametersD0 mainly due to the slower deformation rates and extents. In
particular, the parent droplet cores for cases 5–6 are disappeared, and
the parent droplet for case 5 thoroughly atomized into the dense mist.
However, the parent droplet for cases 2 and 7 is still not atomized, and
there are a few sub-droplets stripped from the parent droplet for case 7.
Figure 13 shows the numerical results of the final sub-droplet
size percentages under different conditions. The sub-droplet sizes
intensively range from 10 to 255lm, and the numbers of sub-droplets
primarily increase as the shock Mach number increases and the drop-
let diameter decreases. As previously mentioned, the sub-droplet sizes
from the direct stripping of the KHI waves are commonly smaller
than those of the sheets, ligaments, and lips stripped from the periph-
ery and leeward side of the parent droplet. At the onset of the breakup,
the aerodynamic force is relatively strong enough to tear the larger
sizes of sheets and ligaments apart, producing many larger sub-
droplets. As time goes by, fragmentations of sheet and ligament can be
further atomized into smaller sub-droplets. Therefore, to a large
extent, the sub-droplet size distributions may look nonmonotonic due
to the uncertainty of multi-scale sub-droplets developed from sheets,
ligaments, lips, and wave stripping during the shear breakup process.
More specifically, with increasing shock Mach numbers and decreas-
ing droplet diameters, the size ratios of the initial parent droplets to
the mean sub-droplets fluctuate from 10 to 25. As a result, the mean
sub-droplet sizes tend to be smaller at higher shock Mach numbers
and lower droplet diameters.
Figure 14 shows the superficial area ratios S
1=S0 and the mass
ratios m1=m0 of the sub-droplets to the initial parent droplet at differ-
ent Ms and D0.A ss h o w ni nFig. 14, the subscripts 0 and 1 represent
the parent droplet and the sub-droplets, respectively. Both curves of
S1=S0 and m1=m0 show an increasing linear trend with the increase of
Ms but with the decrease of D0.T h ev a l u e so fS1=S0 and m1=m0
obtained are higher mainly because more sub-droplets tend to be
stripped from the parent droplet at higher Ms and lower D0 condi-
tions. More specifically, as Ms increases, there are growths of m1=m0
and S1=S0 that concretely increase from 23.38% to 38.38% and from
5.6 to 8.28, respectively. On the contrary, as D0 decreases, there are
growths of m1=m0 and S1=S0 that concretely increase from 4.63% to
92.7% and from 2.65 to 18.52, respectively. As mentioned above, it can
also be illustrated that increasing theM
s and decreasingD0 would pro-
mote the deformation, subsequent shear breakup, the complete atomi-
zation of the parent droplet, and thereby increase the specific surface
area of the fuel droplets, which is critical to enhance the secondary
atomization induced by shock waves.
V. SUMMARY AND CONCLUSIONS
We have conducted 2D numerical simulations on droplet defor-
mation and the breakup of an n-C
10H22 droplet induced by the shock
FIG. 11. Effects of (a) shock Mach number Ms and (b) droplet diameter D0 on the relaxation time tr and total breakup time tb.
Physics of Fluids ARTICLE scitation.org/journal/phf
Phys. Fluids 34, 063306 (2022); doi: 10.1063/5.0093291 34, 063306-12
Published under an exclusive license by AIP Publishing
 29 August 2026 09:14:55

<!-- PDF_PAGE: 14 -->

FIG. 12. Effects of (a) shock Mach number Ms and (b) droplet diameter D0 on the sub-droplet distributions.
Physics of Fluids ARTICLE scitation.org/journal/phf
Phys. Fluids 34, 063306 (2022); doi: 10.1063/5.0093291 34, 063306-13
Published under an exclusive license by AIP Publishing
 29 August 2026 09:14:55

<!-- PDF_PAGE: 15 -->

wave, emphasizing the effects of the Mach numbers ( Ms ¼ 1.4–1.7)
and droplet diameters (D0 ¼ 1.2–2.7 mm) on the physical mechanism
and temporal characteristics in the shear breakup regime. The main
conclusions are as follows:
(1) The CLSVOF-LES methodology based on AMR technology can
reveal the airflow field patterns and shear breakup mechanisms
reasonably at high Weber conditions. The fuel droplet shows
no change in shape immediately after being struck during the
relaxation time and KHI waves start to appear after the relaxa-
tion time elapsed. Moreover, droplet deformation and shear
breakup occur almost simultaneously and promote each other.
Furthermore, the huge pressure difference between the wind-
ward side and the leeward side makes the cross-stream and
stream-wise deformation of the parent droplet. The generation
and stripping of KHI waves are mainly due to shearing forces
FIG. 13. Effects of (a) shock Mach number Ms and (b) droplet diameter D0 on the percentage of the sub-droplet sizes.
FIG. 14. Effects of (a) shock Mach number Ms and (b) droplet diameter D0 on the superficial area ratios S1=S0 and the mass ratios m1=m0.
Physics of Fluids ARTICLE scitation.org/journal/phf
Phys. Fluids 34, 063306 (2022); doi: 10.1063/5.0093291 34, 063306-14
Published under an exclusive license by AIP Publishing
 29 August 2026 09:14:55

<!-- PDF_PAGE: 16 -->

in the windward recirculation zone, while the shearing forces in
wake and sheet recirculation zones may lead to the fragmenta-
tions of sheets, ligaments, and lips.
(2) Shear breakup regimes occur in all the present simulations, and
the generations of KHI waves are prominent and unstable at
higher shock Mach numbers and lower droplet diameters. The
parent droplet is continuously stretched and compressed in the
cross-stream and stream-wise directions under different We
number conditions. The growth rates and extents of cross-
stream and stream-wise deformation are relatively larger at
higher shock Mach number and smaller droplet diameter con-
ditions. Furthermore, the relaxation time and total breakup
time should be shorter, the smaller the mass of the parent drop-
let that is involved in droplet diameter and the stronger the
strength for shock Mach number.
(3) The atomization extents including the sub-droplet numbers of
the parent droplet are larger at higher shock Mach number and
lower droplet diameter conditions, while the mean sub-droplet
sizes tend to be smaller and the size ratios of the initial parent
droplets to the mean sub-droplet fluctuate from 10 to 25. More
specifically, the superficial area and the mass ratios increase
from 23.38% to 38.38% and from 5.6 to 8.28, respectively. By
contrast, as the droplet diameter decreases, the superficial area
and the mass ratios increase from 4.63% to 92.7% and from
2.65 to 18.52, respectively.
The data focus on the variation of deformation and breakup with
the droplet diameters and shock Mach numbers in this paper.
However, with increases in gas temperature instantaneously behind
the shock wave, breakup interaction with evaporation and explosion
would make the atomization process more complicated. And, the
information available for deducing the breakup mechanism by which
evaporation and explosion occurred is still limited. Moreover, the
shock-droplet interaction is three-dimensional (3D). Therefore, to fur-
ther develop the liquid-fueled detonation engines, we will perform 3D
numerical simulations to investigate the shock–droplet interaction in a
wider range of practical applications.
ACKNOWLEDGMENTS
The authors would like to acknowledge the National Natural
Science Foundation of China (Grant No. 52071103) for supporting
this work.
AUTHOR DECLARATIONS
Conflict of Interest
The authors have no conflicts to disclose.
Author Contributions
Wanli Zhu: Investigation (lead); methodology (lead); writing –
original draft (lead). Hongtao Zheng: Writing – review and editing
(equal). Ningbo Zhao: Conceptualization (equal); project administra-
tion (lead).
DATA AVAILABILITY
The data that support the findings of this study are available
within the article.
REFERENCES
1A. P. Lebanoff and A. K. Dickerson, “Drop impact onto pine needle fibers with
non-circular cross section, ” Phys. Fluids 32(9), 092113 (2020).
2Y. Liu and B. Derby, “Experimental study of the parameters for stable drop-
on-demand inkjet performance, ” Phys. Fluids 31(3), 032004 (2019).
3S. Patil and S. Sahu, “Air swirl effect on spray characteristics and droplet dis-
persion in a twin-jet crossflow airblast injector, ” Phys. Fluids 33(7), 073314
(2021).
4S. Ke, P. Jin, S. Xu, X. Yin, X. Yin, and F. Li, “Transient radial spray from elec-
trified viscous jets, ” Phys. Fluids 33(12), 121704 (2021).
5S. Jeong and Y. Yoon, “Sheet-breakup characteristics of a closed-type swirl
injector considering internal flow instability, ” Acta Astronaut. 186, 363 –371
(2021).
6P. B. Li, Z. G. Wang, M. B. Sun, and H. B. Wang, “Numerical simulation of the
gas-liquid interaction of a liquid jet in supersonic crossflow, ” Acta Astronaut.
134, 333–344 (2017).
7Y. H. Zhu, F. Xiao, Q. L. Li, R. Mo, C. Li, and S. Lin, “LES of primary breakup
of pulsed liquid jet in supersonic crossflow, ” Acta Astronaut. 154, 119 –132
(2019).
8D. V. Antonov, G. V. Kuznetsov, and P. A. Strizhak, “Comparison of the char-
acteristics of micro-explosion and ignition of two-fluid water-based droplets,
emulsions and suspensions, moving in the high-temperature oxidizer
medium,” Acta Astronaut. 160, 258–269 (2019).
9D. V. Antonov, R. M. Fedorenko, G. V. Kuznetsov, and P. A. Strizhak,
“Modeling the micro-explosion of miscible and immiscible liquid droplets, ”
Acta Astronaut. 171,6 9–82 (2020).
10K. Kailasanath, “Recent developments in the research on pulse detonation
engines,” AIAA J. 41(2), 145–159 (2003).
11K. Alhussan, M. Assad, and O. Penazkov, “Analysis of the actual thermody-
namic cycle of the detonation engine, ” Appl. Therm. Eng. 107, 339–344 (2016).
12A. Oamjee and R. Sadanandan, “Effects of fuel injection angle on mixing per-
formance of scramjet pylon-cavity flameholder, ” Phys. Fluids 32(11), 116108
(2020).
13M. S. Almanzalawy, L. H. Rabie, and M. H. Mansour, “Modeling of an efficient
airblast atomizer for liquid jet into a supersonic crossflow, ” Acta Astronaut.
177, 142–157 (2020).
14J. Koch and J. N. Kutz, “Modeling thermodynamic trends of rotating detona-
tion engines,” Phys. Fluids 32(12), 126102 (2020).
15Q. Y. Meng, N. B. Zhao, and H. W. Zhang, “On the distributions of fuel drop-
lets and in situ vapor in rotating detonation combustion with prevaporized n-
heptane sprays,” Phys. Fluids 33(4), 043307 (2021).
16P. Debnath and K. M. Pandey, “Numerical investigation of detonation combustion
wave in pulse detonation combustor with ejector, ” J. Appl. Fluid Mech. 10(2),
725–733 (2017).
17J. L. Li, W. Fan, W. Chen, K. Wang, and C. J. Yan, “Propulsive performance of
a liquid kerosene/oxygen pulse detonation rocket engine, ” Exp. Therm. Fluid
Sci. 35(1), 265–271 (2011).
18P. F. Yang, H. D. Ng, and H. H. Teng, “Unsteady dynamics of wedge-induced
oblique detonations under periodic inflows, ” Phys. Fluids 33(1), 016107 (2021).
19P .F .Y a n g ,H .D .N g ,H .H .T e n g ,a n dZ .L .J i a n g ,“Initiation structure of oblique
detonation waves behind conical shocks,” Phys. Fluids29(8), 086104 (2017).
20M. Pilch and C. A. Erdman, “Use of breakup time data and velocity history
data to predict the maximum size of stable fragments for acceleration-induced
breakup of a liquid drop, ” Int. J. Multiphase Flow 13(6), 741–757 (1987).
21Z. Xu, T. Wang, and Z. Che, “Droplet deformation and breakup in shear flow
of air,” Phys. Fluids 32, 052109 (2020).
22E. Y. Harper, G. W. Grube, and I. D. Chang, “On the breakup of accelerating
liquid drops,” J. Fluid Mech. 52(3), 565–591 (1972).
23T. G. Theofanous and G. J. Li, “On the physics of aerobreakup, ” Phys. Fluids
20(5), 052103 (2008).
24H. Zhao, Z. Wu, W. Li, J. Xu, and H. Liu, “Interaction of two drops in the bag
breakup regime by a continuous air jet, ” Fuel 236(15), 843–850 (2019).
25I. M. Jackiw and N. Ashgriz, “On aerodynamic droplet breakup, ” J. Fluid
Mech. 913, A33 (2021).
26M. Jalaal and K. Mehravaran, “Transient growth of droplet instabilities in a
stream,” Phys. Fluids 26(1), 012101 (2014).
Physics of Fluids ARTICLE scitation.org/journal/phf
Phys. Fluids 34, 063306 (2022); doi: 10.1063/5.0093291 34, 063306-15
Published under an exclusive license by AIP Publishing
 29 August 2026 09:14:55

<!-- PDF_PAGE: 17 -->

27W. Zhu, N. Zhao, X. Jia, X. Chen, and H. Zheng, “Effect of airflow pressure on
the droplet breakup in the shear breakup regime, ” Phys. Fluids 33(5), 053309
(2021).
28B. Guan, Y. Liu, C. Wen, and H. Shen, “Numerical study on liquid droplet
internal flow under shock impact, ” AIAA J. 56(9), 3382–3387 (2018).
29Z. Wang, T. Hopfes, M. Giglmaier, and N. A. Adams, “Effect of Mach number
on droplet aerobreakup in shear stripping regime, ” Exp. Fluids 61(9), 193–210
(2020).
30S. Shen, J. Li, C. Tang, J. Liu, X. Ma, and W. Fan, “The viscous effect on the
transient droplet deformation process under the action of shock wave, ”
Atomization Sprays 29(2), 105–121 (2019).
31S. V. Poplavski, A. V. Minakov, and A. A. Shebeleva, “On the interaction of
water droplet with a shock wave: Experiment and numerical simulation, ” Int. J.
Multiphase Flow 127, 103273 (2020).
32J. Kaiser, J. M. Winter, S. Adami, and N. A. Adams, “Investigation of interface
deformation dynamics during high-Weber number cylindrical droplet
breakup,” Int. J. Multiphase Flow 132, 103409 (2020).
33S. Sharma, A. P. Singh, S. S. Rao, A. Kumar, and S. Basu, “Shock induced aero-
breakup of a droplet, ” J. Fluid Mech. 929, A27 (2021).
34J. F. Zhao, W. Lin, P. B. Li, W. Chu, Y. H. Tong, and W. S. Nie, “Simulation of
a liquid jet in supersonic crossflow by a hybrid CLSVOF-LPT method, ” Acta
Astronaut. 183,2 3–28 (2021).
35N. Liu, Z. G. Wang, M. B. Sun, H. B. Wang, and B. Wang, “Numerical simula-
tion of liquid droplet breakup in supersonic flows, ” Acta Astronaut. 145,
116–130 (2018).
36W. Zhu, N. Zhao, X. Jia, C. Sun, and H. Zheng, “Effects of airflow velocity and
droplet diameter on the secondary breakup characteristics, ” AIAA J. 59(8), 1–9
(2021).
37K. Luo, C. X. Shao, M. Chai, and J. R. Fan, “Level set method for atomization
and evaporation simulations, ” Prog. Energy Combust. 73,6 5–94 (2019).
38J. Smagorinsky, “General circulation experiments with the primitive equa-
tions,” Mon. Weather Rev. 91(3), 99–165 (1963).
39C. W. Hirt and B. D. Nichols, “Volume of fluid (VOF) method for the dynam-
ics of free boundaries, ” J. Comput. Phys. 39, 201–225 (1981).
40J. J. Xu and W. Ren, “A level-set method for two-phase flows with moving con-
tact line and insoluble surfactant, ” J. Comput. Phys. 263,7 1–90 (2014).
41W. Chu, X. Li, Y. Tong, and Y. Ren, “Numerical investigation of the effects of
gas-liquid ratio on the spray characteristics of liquid-centered swirl coaxial
injectors,” Acta Astronaut. 175(9), 204–215 (2020).
42A. Liu, D. Sun, B. Yu, J. Wei, and Z. Cao, “An adaptive coupled volume-of-fluid
and level set method based on unstructured grids, ” Phys. Fluids 33(1), 012102
(2021).
43K. Luo, C. Shao, Y. Yang, and J. Fan, “A mass conserving level set method for
detailed numerical simulation of liquid atomization, ” J. Comput. Phys. 298,
495–519 (2015).
44Z. Wang, S. Li, R. Chen, Z. Xun, Q. Liao, D. Ye, and B. Zhang, “Numerical
study on dynamic behaviors of the coalescence between the advancing liquid
meniscus and multi-droplets in a microchannel using CLSVOF method, ”
Comput. Fluids 170(3), 341–348 (2018).
45H. Jiang and L. Cheng, “Large-eddy simulation of flow past a circular cylinder
for Reynolds numbers 400 to 3900, ” Phys. Fluids 33(3), 034119 (2021).
46R. Issa, B. A. Befrui, K. R. Beshay, and A. D. Gosman, “Solution of the implic-
itly discretized reacting flow equations by operator-splitting, ” J. Comput. Phys.
93(2), 388–410 (1991).
47Y. Li, C. Ma, X. Zhang, K. Wang, and D. Jiang, “Three-dimensional numerical
simulation of violent free surface deformation based on a coupled level set and
volume of fluid method, ” Ocean Eng. 210(2), 106794 (2020).
48V. Rossano, A. Cittadini, and G. D. Stefano, “Computational evaluation of
shock wave interaction with a liquid droplet, ” Appl. Sci. 12(3), 1349 (2022).
49A. Moghaddas, K. E. Far, and H. Metghalchi, “Laminar burning speed mea-
surement of premixed n-decane/air mixtures using spherically expanding
flames at high temperatures and pressures, ” Combust. Flame 159, 1437 –1443
(2012).
50H. Quintens, C. Strozzi, R. Zitoun, and M. Bellenoue, “Deflagration-autoigni-
tion-detonation transition induced by flame propagation in an N-decane/O 2/
Ar mixture,” Flow, Turbul. Combust. 102, 735–755 (2019).
51W.-H. Chou, L.-P. Hsiang, and G. M. Faeth, “Temporal properties of drop
breakup in the shear breakup regime, ” Int. J. Multiphase Flow 23(4), 651 –669
(1997).
52N. N. Smirnov, V. B. Betelin, V. F. Nikitin, L. I. Stamov, and D. I. Altoukhov,
“Accumulation of errors in numerical simulations of chemically reacting gas
dynamics,” Acta Astronaut. 117, 338–355 (2015).
53N. N. Smirnov, V. B. Betelin, R. M. Shagaliev, V. F. Nikitin, I. M. Belyakov, Y.
N. Deryuguin, S. V. Aksenov, and D. A. Korchazhkin, “Hydrogen fuel rocket
engines simulation using LOGOS code, ” Int J Hydrogen Energy 39(20),
10748–10756 (2014).
54G. A. Sod, “A survey of several finite difference methods for systems of nonlin-
ear hyperbolic conservation laws, ” J. Comput. Phys. 27(1), 1–31 (1978).
55R. P. Fedkiw, B. Merriman, and S. Osher, “High accuracy numerical methods
for thermally perfect gas flows with chemistry, ” J. Comput. Phys. 132(2),
175–190 (1997).
56Z. W. Huang, M. J. Zhao, Y. Xu, G. Z. Li, and H. W. Zhang, “Eulerian-
Lagrangian modelling of detonative combustion in two-phase gas-droplet mix-
tures with OpenFOAM: Validations and verifications, ” Fuel 286(2), 119402
(2021).
57T. G. Theofanous, “Aerobreakup of Newtonian and viscoelastic liquids, ” Annu.
Rev. Fluid Mech. 43(1), 661–690 (2011).
58J. C. R. Hunt, A. A. Wray, and P. Moin, “Eddies, stream, and convergence
zones in turbulent flows, ” in Proceedings of the CTR Summer Program (Center
for Turbulence Research, Stanford University, 1988), Vol. 2, pp. 193 –208.
59T. V. Buren, E. Whalen, and M. Amitay, “Vortex formation of a finite-span
synthetic jet: High Reynolds numbers, ” Phys. Fluids 26(1), 014101 (2014).
60Y. Gao and C. Liu, “Rortex and comparison with eigenvalue-based vortex
identification criteria,” Phys. Fluids 30(8), 085107 (2018).
Physics of Fluids ARTICLE scitation.org/journal/phf
Phys. Fluids 34, 063306 (2022); doi: 10.1063/5.0093291 34, 063306-16
Published under an exclusive license by AIP Publishing
 29 August 2026 09:14:55
