<!-- PDF_PAGE: 1 -->

ViewOnline
ExportCitation
RESEARCH ARTICLE |  MARCH 18 2025
Three-dimensional numerical simulations of phase change
effects on shock-droplet interactions
Special Collection: Recent Fluid Mechanics: Celebrating the 100th Anniversary of the ICTAM (International Congress of
Theoretical and Applied Mechanics)
Jiaxi Song (宋家喜) 
  ; Tian Long (龙天); Shucheng Pan (潘书诚)  
Physics of Fluids 37, 033358 (2025)
https://doi.org/10.1063/5.0255860
Articles You May Be Interested In
A phenomenological analysis of droplet shock-induced cavitation using a multiphase modeling approach
Physics of Fluids (January 2023)
Analysis of pressure variation within multiple water columns induced by shock wave
Physics of Fluids (August 2025)
A numerical assessment of shock–droplet interaction modeling including cavitation
Physics of Fluids (February 2023)
 29 August 2026 09:54:09

<!-- PDF_PAGE: 2 -->

Three-dimensional numerical simulations of phase
change effects on shock-droplet interactions
Cite as: Phys. Fluids 37, 033358 (2025); doi: 10.1063/5.0255860
Submitted: 31 December 2024 . Accepted: 22 February 2025 .
Published Online: 18 March 2025
Jiaxi Song (宋家喜),1,2,3
 Tian Long (龙天),1,2,3 and Shucheng Pan (潘书诚)1,2,3,a)
AFFILIATIONS
1School of Aeronautics, Northwestern Polytechnical University, Xi ’an 710072, China
2Institute of Extreme Mechanics, Northwestern Polytechnical University, Xi ’an 710072, China
3National Key Laboratory of Aircraft Configuration Design, Xi ’an 710072, China
Note: This paper is part of the Special Topic, Recent Fluid Mechanics: Celebrating the 100th Anniversary of the ICTAM (International
Congress of Theoretical and Applied Mechanics).
a)Author to whom correspondence should be addressed: shucheng.pan@nwpu.edu.cn
ABSTRACT
In real propulsion systems, phase change often accompanies shock-droplet interactions, significantly affecting droplet deformation and frag-
mentation. However, the influence of phase change on shock-droplet interactions, especially considering real fluid effects, remains rarely
investigated. In this study, with three-dimensional high-fidelity numerical simulations, we conduct a comprehensive investigation of an n-
dodecane droplet embedded in its high-temperature vapor environment under shock wave impacting both with and without phase change.
We investigate the effects of phase change on the shock-droplet interactions, including the early-stage wave dynamics, the surface instability
development, the droplet deformation and movement, as well as the vortical structure. Under the influence of evaporation, the low-
temperature vapor layer formed on the droplet surface reduces the shear forces induced by the high-speed airflow, thereby suppressing the
growth of Kelvin-Helmholtz instability waves. In contrast, the vorticity analysis shows that condensation effects promote the generation of
negative Q-values, corresponding to an increase in the shear force on the droplet surface, thereby enhancing the development of surface insta-
bilities. The phase-change effects of surface instabilities subsequently alter the dynamics of droplet deformation and movement. Finally, we
investigated the effect of Mach number on droplet phase change. As the Mach number decreases, the reduced vapor pressure around the
droplet enhances the evaporation rate, leading to a transition from condensation-dominated to evaporation-dominated phase-change
conditions.
Published under an exclusive license by AIP Publishing. https://doi.org/10.1063/5.0255860
I. INTRODUCTION
Shock-droplet interaction is a fundamental problem with a broad
range of engineering applications, including raindrop damage during
supersonic flight,
1 sprays dynamics,2 shock wave lithotripsy,3 and sec-
ondary atomization of liquid jets in supersonic combustion systems. 4
For instance, the evaporation, deformation, and fragmentation of fuel
droplets driven by shock waves in high-temperature environments play
a significant role in the performance of supersonic combustion ramjet
engines and liquid-fueled rotating detonation systems.
5,6 The atomiza-
tion and evaporation of liquid fuel enhance the mixing between air and
vaporized fuel, thereby improving the fuel utilization efficiency.
7
Therefore, understanding the interaction mechanism between the
shock waves and the fuel droplets in such a high-temperature environ-
ment is of significance. In addition, shock-droplet interactions are often
accompanied by phase changes in real propulsion systems due to (1)
the increased temperature of the surrounding environment leading to
evaporation of the droplet surface and (2) the impact of the shock wave
alters the pressure and temperature conditions around the droplet,
which potentially causes evaporation or condensation on its surface.
The deformation and fragmentation of single droplets driven
by shock waves have been extensively studied over the past few deca-
des.
8–23 However, due to limitations in experimental conditions and
numerical models, most studies have not accounted for the effects of
phase change. Pilch and Erdman
12 proposed five breakup mechanisms
for different Weber number ranges, i.e., the vibrational, bag, bag-and-
stamen, stripping, and catastrophic mechanisms. Later, Theofanous
and Li14 reclassified the breakup mechanisms by using laser-induced
fluorescence visualization, suggesting that the Rayleigh-Taylor piercing
(RTP) mechanism dominates at low Weber numbers, while shear-
induced entrainment (SIE) becomes the terminal breakup mechanism
Phys. Fluids 37, 033358 (2025); doi: 10.1063/5.0255860 37, 033358-1
Published under an exclusive license by AIP Publishing
Physics of Fluids ARTICLE pubs.aip.org/aip/pof
 29 August 2026 09:54:09

<!-- PDF_PAGE: 3 -->

at high Weber numbers, based on the surface instabilities during the
droplet deformation and breakup process. Furthermore, they pointed
out that the catastrophic breakup mechanism does not exist but is
merely a mirage of the shadowgraphs used to visualize waves. 14
Recently, Sharma et al.15,16 conducted experimental studies on water
and metal droplets under shock wave impact, showing that the RTP
mode can still occur in small droplets (diameter 0.5 mm) at Weber
numbers up to 800, while the SIE mode can be present in large drop-
lets (diameter 2.5 mm) at Weber numbers as low as 200. This suggests
that the droplet breakup modes are not only correlated with the
Weber number but also depend on the droplet size.
Several recent studies have suggested that phase change effects
can significantly influence the droplet deformation and breakup mech-
anisms, such as cavitation and vaporization. For instance, regarding
cavitation, Sembian et al.
24 experimentally observed that the focusing
of an expansion wave, which was caused by the reflection of the trans-
mitted wave at the downstream interface, generated negative pressures
for initiating the cavitation, especially for large droplets in the high
Mach number regime. Later, Xiang and Wang 25 numerically investi-
gated the interaction between a planar shock wave and a water column
embedded with a cavity at high Weber numbers. It was found that,
under the same shock strength, increasing the cavity radius led to an
increase in the momentum of the transverse jet. Meanwhile, Liang
et al.
26 conducted a similar experiment and found that both the relative
size and eccentricity of the vapor cavity significantly affected the move-
ment and deformation of the hollow droplet. In addition, Jiao et al.27
conducted a three-dimensional (3D) numerical simulation of the
deformation and breakup of cavity-embedded droplets under critical
conditions and analyzed the effects of the vapor cavity and real fluid
effects on the droplet dynamics. However, it is worth noting that the
above studies did not consider the effects of phase change or the incep-
tion of cavitation inside the droplet, which are difficult to numerically
model or experimentally measure.
With respect to vaporization, most studies have focused on the
breakup of vaporizing droplets under the incompressible flow assump-
tion at low Weber numbers. Haywood et al.
28,29 used non-orthogonal
adaptive grids to predict the evaporation and deformation of n-
heptane droplets within high-temperature air. The prediction based on
existing Nusselt and Sherwood number correlations shows a good
agreement with the numerical result. Nevertheless, their numerical
simulations are unable to accurately represent the fragmentation of
droplets due to the limited grid resolution. Strotos et al.30 coupled the
volume of fluid (VOF) method with a local evaporation model and the
adaptive grid refinement to study the effect of heating and evaporation
on the breakup of the volatile n-heptane droplets embedded in a high-
temperature gas. They concluded that heating has a minor impact on
droplet breakup, except at low Weber numbers, due to the short dura-
tion of the heating effect. In contrast, droplet deformation and breakup
could enhance heat transfer and evaporation. Furthermore, a recent
numerical study
31 focused on the vaporization of a freely moving and
deforming droplet, specifically investigating the influence of droplet
deformation on the vaporization rate at low to moderate Weber num-
bers. For high-speed compressible flows, Goossenset al.32 were among
the first to examine droplet evaporation induced by shock waves.
Their results indicated that, for weak shock waves and relatively small
droplet sizes, the evaporation rate could be governed by heat conduc-
tion and vapor diffusion. Recently, Das and Udaykumar
33 developed a
sharp-interface method to calculate the vaporization of droplets in
high-speed flows. Based on the simulation-based data, they developed
a surrogate model for the temporally averaged Sherwood number and
Nusselt number34 cast as functions of the shock Mach number and
Reynolds number, to investigate the vaporization rate of aluminum
droplets. Subsequently, they simulated the interaction between
shocked flows and reacting aluminum droplets35 to study the effects of
Mach number and Reynolds number on reacting aluminum droplets.
Additionally, Zhu et al.
36 adopted the coupled level-set and VOF
method to simulate the n-decane droplet and shock wave interaction
without phase change. They specifically focused on the impact of shock
Mach number on the droplet size distribution. Xionget al.37 employ a
high-fidelity compressible numerical approach to investigate the early-
stage shock–droplet interaction, focusing on the relationship between
negative peak pressure and the reflected expansion wave, while
addressing the challenges posed by varying gas –liquid wave velocity
ratios.
Until now, there is still a lack of experimental data on the interac-
tion between shock waves and evaporating droplets in high-
temperature environments. Recently, Redding and Khare 38 investi-
gated the deformation, fragmentation, and vaporization of n-dodecane
droplets impacted by normal shock waves, using the VOF method
coupled with a diffuse-interface method. They modeled phase change
effects based on solving a thermal-mechanical-chemical equilibrium
relaxation procedure. The results showed that, unlike inert droplets,
the vaporization suppressed the interfacial instabilities when consider-
ing the phase-change effects. Additionally, the rate of vaporization is
dependent on the shock strength, with lower Mach numbers leading to
higher vaporization rates. However, due to the limitations of their
numerical method, the study used the stiffened gas equations of state
for n-dodecane, which did not account for the thermodynamic effects
of real fluids, and only a two-dimensional cylindrical configuration
was discussed. Additionally, Tareyet al.
39 conducted detailed numeri-
cal simulations of the deformation and breakup behavior of n-
dodecane droplets under shock waves at Mach 5, focusing on the
phase change effects induced by chemical reactions and evaporation.
The study showed that in the presence of evaporation, a recondensed
vapor layer forms around the droplet surface, which helps suppress the
growth of surface Kelvin-Helmholtz (KH) instability waves. By altering
the fuel ’s reactivity, they also investigated the influence of the
Damkohler number on droplet evolution. As the fuel ’s reactivity
increased, the flame thickness decreased, which is consistent with the
trend observed in laminar diffusion flame theory. It is worth noting
that most of the studies on shock-droplet interactions involving phase
change are limited to 2D and axisymmetric simulations. Due to the
substantial computational cost associated with considering phase
change effects, to our knowledge, 3D numerical simulations of com-
pressible flows with phase change have not yet been reported. Also, a
comprehensive study that combines the effect of phase change, 3D
configurations, and the real fluid effect is not achieved.
Based on the reasons mentioned above, a fully conservative
sharp-interface method for compressible multiphase flows with phase
change
40 is used to solve the gas-liquid n-dodecane interface interac-
tion under phase change conditions. The numerical simulations in this
study were conducted using an in-house compressible multiphase
code, which has been extensively tested and validated in previous
research.
41,42 The thermophysical properties of n-dodecane are close
Physics of Fluids ARTICLE pubs.aip.org/aip/pof
Phys. Fluids 37, 033358 (2025); doi: 10.1063/5.0255860 37, 033358-2
Published under an exclusive license by AIP Publishing
 29 August 2026 09:54:09

<!-- PDF_PAGE: 4 -->

to those of aviation kerosene, making it suitable for studying the inter-
action between fuel droplets and shock waves. It is noteworthy that a
real-fluid equation of state based on Helmholtz energy is employed for
n-dodecane in this paper to ensure high accuracy on thermodynamics.
Additionally, the shock-droplet interactions under different shock
intensities are studied at the end of the paper. The rest of this paper is
organized as follows. The governing equations and numerical imple-
mentation are specified in Sec.II, while the physical model and numer-
ical validation are introduced in Sec. III. Numerical results and
discussions are presented in Sec.IV, followed by the main conclusions
in Sec. V.
II. NUMERICAL METHODOLOGY
A. Governing equations
The governing equations for two-phase viscous flows with phase
change and surface tension force can be written as
@U
@t þr T /C1FþrT /C1Fv ¼ S; (1)
where
U ¼ q; qu; qv; qw; E½/C138 T; (2)
F ¼
qu qv qw
qu2 þ p quv quw
qvu qv2 þ p qvw
qwu qwv qw2 þ p
ðE þ pÞu ðE þ pÞv ðE þ pÞw
8
>>
>
>
>
>
<
>>
>
>
>
>:
9
>>
>
>
>
>
=
>>
>
>
>
>;
; (3)
F
v ¼/C0
000
sxx sxy sxz
syx syy syz
szx szy szz
usxx þ vsxy þ wsxz usyx þ vsyy þ wsyz uszx þ vszy þ wszz
8
>>
>
>
>
>
<
>>
>
>
>
>
:
9
>>
>
>
>
>
=
>>
>
>
>
>
;
;
(4)
denote the conservative variables, convective fluxes, and viscous fluxes,
respectively. Here, q represents the density, u, v,a n d w denote the
velocity components in thex, y,a n dz directions, respectively.E repre-
sents the total energy, p is the pressure, s is the viscous stress tensor. It
is worth noting that the vector S represents the exchange terms
between the liquid and gaseous phase, encompassing effects from
phase change, surface tension, and viscosity. For further details on
these terms, see Sec. II E below. Notably, although heat conduction
and vapor diffusion may play significant roles in low-speed convective
environments
43 or the long-term evaporation of droplets,32 their influ-
ence under high-speed, short-duration shock conditions, particularly
during the early stages of droplet deformation and breakup, is negligi-
ble
44,45 here, considering the timescales of the diffusion and heat con-
duction are usually much larger than that of the shock impacting. In
real-world applications, particularly in engines or systems where drop-
let exposure to shocks is coupled with prolonged high-temperature
environments, the impact of these processes becomes more important,
which may require the coupling of these effects with our current
models.
B. Equations of state
To close the system of governing equations, specific equations of
state (EOS) are required. In this paper, we consider three types of flu-
ids: air, water, and n-dodecane. The equations of state for air and water
are described by the stiffened-gas EOS,
46,47 which is given by
eðp; qÞ¼ p þ cp
qðc /C0 1Þ þ q; Tðp; qÞ¼ p þ p
Cvqðc /C0 1Þ ; (5)
where e and T represent the internal energy and temperature, which
depend on the pressure p and density q. Here, c, p, q, Cv denote the
adiabatic coefficient, the parameter accounting for fluid pre-
compression, the reference internal energy, and the heat capacity at
constant volume, respectively. According to Refs. 46 and 47,t h e
parameters for the stiffened-gas EOS for air, vapor, and liquid water
are provided in Table I.N o t a b l y ,w h e np ¼ 0, the stiffened-gas EOS
reduces to the ideal-gas EOS, which is applicable for air and water
vapor. For n-dodecane, a real-fluid EOS based on Helmholtz energy
48
is utilized to obtain thermodynamic variables with higher physical
accuracy. This EOS reduces the prediction error in thermodynamic
parameters of n-dodecane to less than 1%.
49
C. Numerical discretization
The governing equations in Eq. (1) are discretized using a finite-
volume approach on Cartesian meshes. Applying Gauss’s theorem and
the first-order forward Euler time marching method, the governing
equations can be written as
a
nþ1
i;j;k Unþ1
i;j;k /C0 an
i;j;kUn
i;j;k ¼ Dt
DxDyDz XðDCi;j;kÞ
þ Dt
Dx ½Ai/C0 1=2;j;kðFi/C0 1=2;j;kþFv;i/C0 1=2;j;kÞ
/C0 Aiþ1=2;j;kðFiþ1=2;jþFv;iþ1=2;j;kÞ/C138
þ Dt
Dy ½Ai;j/C0 1=2;kðFi;j/C0 1=2;k þ Fv;i;j/C0 1=2;kÞ
/C0 Ai;jþ1=2;kðFi;jþ1=2;k þ Fv;i;jþ1=2;kÞ/C138
þ Dt
Dz ½Ai;j;k/C0 1=2ðFi;j;k/C0 1=2 þ Fv;i;j;k/C0 1=2Þ
/C0 Ai;j;kþ1=2ðFi;j;kþ1=2 þ Fv;i;j;kþ1=2Þ/C138; (6)
where an
i;j;kUn
i;j;k is the vector of conservative states at the center of
the cell ði; j; kÞ at the time step n for each material. ai;j;k is the volume
fraction of the corresponding phase in the cell ði; j; kÞ,a n dUi;j;k is the
vector of cell-averaged states,Dt i st h et i m es t e p ,Dx, Dy,a n dDz repre-
sent the grid spacing in the x, y,a n d z directions, respectively.
TABLE I. The parameters of the stiffened-gas EOS for air and water.
Fluid types cp ðPaÞ q ðJ=kgÞ Cv ðJ=kg=KÞ
Air 1.4 0 0 0.718 /C2 103
Water vapor 1.33 0 1.99 /C2 106 1.399 /C2 103
Water liquid 2.35 10 9 /C0 1.167 /C2 106 1.816 /C2 106
Physics of Fluids ARTICLE pubs.aip.org/aip/pof
Phys. Fluids 37, 033358 (2025); doi: 10.1063/5.0255860 37, 033358-3
Published under an exclusive license by AIP Publishing
 29 August 2026 09:54:09

<!-- PDF_PAGE: 5 -->

The aperture A denotes the cell face after segmentation by the
interface C at the current time step. The inviscid numerical flux F
is computed by the fifth-order Weighted Essentially Non-
Oscillatory scheme 50 and the global Lax-Friedrichs scheme. 51 The
viscous numerical flux Fv is approximated by the fourth-order
central finite-difference scheme. The term XðDCi;jÞ represents the
momentum and energy exchange between the liquid and gaseous
phases within a cut cell. Additionally, a second-order strong
stability-preserving Runge –Kutta scheme 52 is employed for time
marching. The maximum admissible time step size, considering
the maximum wave speed, viscous diffusion, and propagation of
capillary waves at the interface, is determined by
Dt ¼ CFL /C1min DxP jui6cj1
; 3
14
qDx2
l ;
ﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃql þ qg
8pr Dx3
r !
; (7)
where c is the speed of sound, l and r represent the viscosity and sur-
face tension coefficients, respectively.qg and ql are the densities of the
gas phase and the liquid phase, respectively. CFL ¼ 0:8i se m p l o y e d
for all the simulations in this paper.
D. Interface capturing
In this paper, the level-set method 53 is employed to capture the
two-phase interface during the shock wave and droplet interaction.
The two-phase domain is represented by a level-set function /ðxÞ.
The liquid-phase and the gaseous-phase regions are represented by
/ðxÞ < 0a n d /ðxÞ > 0, respectively, with the two-phase interface
being /ðxÞ¼ 0. The level-set function/ðxÞ is evolved over time by an
advection equation:
@/
@t þ u/nC /C1r/ ¼ 0; (8)
where u/ denotes the level-set advection velocity, which is determined
by solving a two-material Riemann problem,54 as detailed in the next
subsection. The interface normal nC and interface curvature j can be
computed by
nC ¼ r/
jr/j ; j ¼r/C1 r/
jr/j : (9)
After the advection step, the level-set function is reinitialized to main-
tain the signed distance property jr/j¼ 1 using the re-initialization
equation:55
@/
@s þ signð/0Þðjr/j/C0 1Þ¼ 0: (10)
To handle the discontinuities of fluid states across the interface, our
sharp interface method employs a two-fluid formulation, i.e., solving
the vapor and liquid separately. The ghost point values required by the
high-order discretization near the interface are extended from the
respective fluid by using the extending algorithm. 56 This treatment
allows the liquid and vapor states to be numerically interpolated or
reconstructed separately on either side of the interface, ensuring that
no unphysical oscillations are generated due to discontinuities of fluid
states.
E. Interface interactions
To improve numerical stability while guaranteeing strict con-
servation and sharp interfacial properties for each fluid, the inter-
action term XðDC
i;j;kÞ is obtained by solving a two-material
Riemann problem with phase change, 40 which can be written as
four terms:
XðDCi;j;kÞ¼ XvðDCi;j;kÞþ XcðDCi;j;kÞþ XsðDCi;j;kÞþ XpðDCi;j;kÞ;
(11)
where the appropriate terms denote viscous, inertial, and surface-
tension forces and effects of phase change, respectively. The viscous
flux across the two-phase interfaceDC
i;j;k is
XvðDCi;j;kÞ¼ð 0; sDCi;j;knC; sDCi;j;knC /C1uÞT ; (12)
with an interface viscous stress tensor of
s ¼ lð/C0 2
3 r/C1uI þð ru þr uT ÞÞ: (13)
The combination of the inertial term and the surface tension term can
be written as
Xc;mðDCi;j;kÞþ Xs;mðDCi;j;kÞ¼ð 0;DCi;j;kpC;mnC;DCi;j;kpC;mnC /C1uCÞT ;
(14)
where the subscript m stands for the liquid phase or gaseous phase.
The pressure jump across the interface, induced by surface tension and
mechanical equilibrium, is given by
Dp ¼ pC;1 /C0 pC;2 ¼ rj; (15)
where r is the surface tension coefficient. As in Longet al.,40 the phase
change term XpðDCi;j;kÞ can be obtained by
Xp;mðDCi;j;kÞ¼ 6
/C16
jDCi;j;k; jDCi;j;knC /C1uC; jDCi;j;k
/C16
eC þ 1
2 juCj2
/C17/C17
;
(16)
where eC is the internal energy of the phase interface, þ and – are
applied for the gaseous phase and liquid phase, respectively. In
3D, the interface segment DC
i;j;k in the cut cell ði; j; kÞ can be
approximated by
DCi;j;k ¼
ﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ
ðAiþ1=2;j;k /C0 Ai/C0 1=2;j;kÞ2 þð Ai;jþ1=2;k /C0 Ai;j/C0 1=2;kÞ2 þð Ai;j;kþ1=2 /C0 Ai;j;k/C0 1=2Þ2
q
: (17)
Here, an additional phase change model is required to evaluate the mass flux j.I nt h i sp a p e r ,w ee m p l o yt h eH e r t z–Knudsen (HK)
relation: 57
Physics of Fluids ARTICLE pubs.aip.org/aip/pof
Phys. Fluids 37, 033358 (2025); doi: 10.1063/5.0255860 37, 033358-4
Published under an exclusive license by AIP Publishing
 29 August 2026 09:54:09

<!-- PDF_PAGE: 6 -->

j ¼
ﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ
1
2pRg
s
ke
psat /C1TlﬃﬃﬃﬃﬃTl
p /C0 kc
pgﬃﬃﬃﬃﬃTg
p
 !
; (18)
where Rg denotes the specific gas constant, which is set to
461:52 J=ðkg /C1KÞ for water and 48 :81 J=ðkg /C1KÞ for n-dodecane. Tl
and Tg are the temperatures of the phase interface for the liquid
and the gas, pg is the pressure of the gaseous phase at the phase
interface, psat is the saturation pressure. In our simulations, the
saturation pressure of water and n-dodecane is calculated accord-
ing to Ref. 57 and the OpenSource library CoolProp, 58 respec-
tively. ke and kc are the evaporation and condensation coefficients,
respectively. In previous studies, 33,39 many investigators have
assumed
ke ¼ kc ¼ 2a
2 /C0 a ; (19)
when using the HK relation, wherea can be calculated by
a 1 /C0 qg
ql
/C18/C191=3
 !
exp /C0 1
2 ql
qg
/C16/C171=3
/C0 2
0
@
1
A (20)
However, the above assumptions may introduce substantial errors, as
reported by previous evaporation experiments. 57 The model coeffi-
cients require rigorous experimental calibration to accurately model
the complex phase change process. Unfortunately, the phase change
statistical data for the shock-droplet interactions experiment have not
been sufficiently provided in previous literature. Therefore, this study
directly specifies the model coefficients to consider the phase change
effects dominated by evaporation and condensation, i.e.,k
e ¼ 0:4a n d
kc ¼ 0:03 for the evaporation-dominated cases,ke ¼ 1:0a n dkc ¼ 0:6
for the condensation-dominated cases. The selected coefficients of ke
and kc are chosen manually based on extensive testing simulations to
ensure that the droplet remains in a representative evaporation-
dominated or condensation-dominated state, respectively.
F. Multi-resolution mesh refinement
For shock-droplet interaction, as we incorporate both the real-
fluid EOS and phase-change model, the time cost of our numerical
simulation is several times larger than that using a simple EOS. To
enhance computational efficiency, we employ a block-structured adap-
tive multi-resolution mesh refinement technique.
59,60 As shown in
Fig. 1, the domain is divided into several square blocks. Blocks near the
droplet interface or regions with strong fluid field variations, such as
shock waves, are refined. It is important to note that all blocks contain
a fixed number of internal cells, and adaptive refinement is achieved
by applying different refinement levels to the blocks. In this paper, we
set the number of blocks to 1 initially, with the number of internal cells
per block being 16 in each coordinate direction (i.e., x, y, and z). The
effective resolution is determined by the maximum refinement level
L
max, indicating the maximum number of cells Nmax in each coordi-
nate direction being
Nmax ¼ 16 /C2 2Lmax : (21)
For more details on the adaptive multi-resolution method, please refer
to Ref. 60.
III. PHYSICAL MODEL AND NUMERICAL VALIDATION
A. Problem description and simulation setup
Deformation and breakup of droplets typically occur under the
impact of high-speed airflow, often generated by a planar shock wave
due to its simplicity.22 In this paper, we focus primarily on the droplets’
dynamics at high Weber numbers, under the phase change effect.
Figure 1 illustrates the initial parameters, including the droplet position
and diameter, boundary conditions, and the computational domain
with adaptive mesh refinement. The simulations are performed in a
3D geometry to capture the full complexity of the shock-droplet inter-
action. To reduce computational costs, a quarter of the physical
computational domain is chosen for numerical simulations, as shown
by the red dashed box in Fig. 1. The current choice of computational
domain size is sufficient to balance the influence of domain boundary
conditions and computational costs. In addition to the symmetric
boundary conditions applied at the symmetry axis, the inflow
FIG. 1. Schematic of the initial conditions and computational domain for 3D shock-
droplet interactions, showing two subfigures (a) and (b) from different views, includ-
ing the multi-resolution block edges and the initial positions of droplet and the
shock. The red dashed lines represent a quarter of the computational domain.
Physics of Fluids ARTICLE pubs.aip.org/aip/pof
Phys. Fluids 37, 033358 (2025); doi: 10.1063/5.0255860 37, 033358-5
Published under an exclusive license by AIP Publishing
 29 August 2026 09:54:09

<!-- PDF_PAGE: 7 -->

boundary conditions at the shock inlet, and outflow boundary condi-
tions for the remaining domain boundaries are specified to prevent
numerical contamination from shock wave reflections. 40 The initial
droplet is placed in a high-temperature vapor environment with the
same material as the droplet. Two different liquids are used in the pre-
sent study: water for validation and n-dodecane for our investigation.
In conventional shock-droplet interactions, the Weber number
and Ohnesorge number are the two primary parameters governing
droplet deformation and breakup. The Weber number, defined as the
ratio of inertial forces to capillary forces, is given by
We ¼
qg u2
g D0
r ; (22)
where qg and ug indicate the post-shock density and velocity of the
gaseous phase, respectively.D0 and r denote the initial droplet diame-
ter and the surface-tension coefficient, respectively. The Ohnesorge
number is defined as the ratio of viscous forces to capillary forces,
Oh ¼
llﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃql D0rp ; (23)
with the dynamic viscosity of the liquid droplet phase ll and the den-
sity of the liquid droplet phase ql . Another important parameter is the
Mach number, defined as the ratio of the flow velocity us to the speed
of sound c in the gaseous phase:
Ma ¼ us
c : (24)
Additionally, it is worth noting that the time in this paper is non-
dimensionalized using a scaling from Ref.10:
t/C3 ¼ t ug
D0
ﬃﬃﬃﬃﬃqg
ql
r
: (25)
B. Grid convergence study
Here, the grid convergence study refers to the spatial resolution
of the finest layer of the multi-resolution adaptive mesh. Five different
mesh resolutions are employed to simulate the interactions between
the shock wave and the n-dodecane droplet with a phase change, cor-
responding to resolutions of 64, 128, 192, 256, and 320 cells per initial
droplet diameter.Figure 2 illustrates the evolution of droplet mass due
to phase change for five different mesh resolutions. It can be observed
that as the mesh resolution increases, the droplet mass evolution
curves gradually converge, indicating that the droplet phase change
becomes nearly independent of the mesh size when the number of cells
per initial droplet diameter exceeds 256. We note that as the mesh res-
olution increases, additional small-scale vortex structures in the flow
FIG. 2. Droplet mass evolution for an n-dodecane droplet under a 1.47 Mach shock
impact. Grid convergence study using 5 different mesh resolutions, i.e., 64, 128,
192, 256, and 320 cells per initial droplet diameter.
FIG. 3. Comparison between the numerical schlieren images (top) and the experimental visualizations (bottom) of the interaction of a planar shock wave with a water column.
Reprinted from Sembian et al., Phys. Fluids 28, 056102 (2016), with the permission of AIP Publishing.
Physics of Fluids ARTICLE pubs.aip.org/aip/pof
Phys. Fluids 37, 033358 (2025); doi: 10.1063/5.0255860 37, 033358-6
Published under an exclusive license by AIP Publishing
 29 August 2026 09:54:09

<!-- PDF_PAGE: 8 -->

field are resolved. Nonetheless, their influence on the macroscopic pro-
cesses of droplet evaporation, propulsion, and deformation can be
insignificant. Moreover, finer grids may capture additional small-scale
liquid fragments during the later stages of droplet breakup. Although
this aspect is beyond the scope of the present study; the current mesh
resolution is deemed sufficient to investigate the impact of phase
change on the early-stage shock-droplet interaction.
C. Numerical verification and validation
Numerical verification is conducted by comparing the numerical
results with existing well-known experiment results or benchmark
numerical solutions. Due to a lack of experimental studies on n-
dodecane droplets with phase change, we select the water droplets
under shock wave impact to validate the accuracy of the numerical
method. The interaction between a shock wave and a water column is
considered the first test case. Following the experimental setup of
Sembian et al.,
24 the initial water column diameter is 22 mm, and the
shock wave Mach number is 2.4. The initial conditions are
q ¼ 1:2k g=m3; p ¼ 1:01325 /C2 105 Pa; T ¼ 293:0K ;
pre /C0 shocked vapor;
q ¼ 3:87 kg=m3; p ¼ 6:64 /C2 105 Pa; T ¼ 597:8K ;
u ¼ 567:1m =s; post /C0 shocked vapor;
q ¼ 1000:0k g=m3; p ¼ 1:01325 /C2 105 Pa; T ¼ 293:0K ;
water droplet:
8
>>
>
>
>>>
>
>
>
>
>
>
<
>>
>
>
>
>
>
>
>
>>>
>
:
(26)
In this case, the computational domain is identical to the 2D cross
section in Fig. 1 . The simulation employs a 6-level adaptive mesh,
with the finest resolution being 512 cells along the droplet diameter.
Figure 3 shows the comparison between our numerical results and pre-
vious experimental data.
24 The reflected shock wave, transmitted wave,
and reflected expansion wave show good qualitative agreement with
the experiment. Next, we change the initial water column diameter to
4.8 mm and the shock wave Mach number to 1.47. The initial condi-
tions are given by
q ¼ 1:2k g=m
3; p ¼ 1:01325 /C2 105 Pa; T ¼ 293:0K ;
pre /C0 shocked vapor;
q ¼ 2:18 kg=m3; p ¼ 2:38 /C2 105 Pa; T ¼ 381:0K ;
u ¼ 225:8m =s; post /C0 shocked vapor;
q ¼ 1000:0k g=m3; p ¼ 1:01325 /C2 105 Pa; T ¼ 293:0K ;
water droplet:
8
>>
>
>
>
>
>
>
>
>
>>>
<
>>
>
>
>
>
>
>
>
>
>
>
>
:
(27)
We compare the normalized upstream stagnation point
movement between the present results, the experiment of Igra
and Takayama,
61 and previous numerical results.18,23 As in Fig. 4,o u r
results fit the numerical results and experimental data very well.
IV. RESULTS AND DISCUSSION
A. The effects of phase change
To investigate the effects of phase change on the shock wave
interaction with an n-dodecane droplet, we perform simulations with
and without the phase change model. Two different conditions are
considered for phase-change simulations: the evaporation-dominated
and the condensation-dominated cases, which are achieved by specify-
ing different model coefficients,k
e and kc. The evaporation-dominated
case usually occurs for droplet interaction with shock inside a
low-concentration vapor-air mixture, 38,39 while the condensation-
dominated case can be encountered when the surrounding gas mixture
has a high fuel vapor fraction.
Following previous studies,
18,21 we consider the evolution of a
4.8 mm diameter n-dodecane droplet in its vapor environment under
a shock wave with a Mach number of 1.47. The computational domain
is shown in Fig. 1, and the initial conditions and fluid properties are
given in Table II. The Weber number and Ohnesorge number for this
benchmark case are 8.25/C2 10
4 and 1.23 /C2 10/C0 3, respectively. Next, we
analyze the effect of phase change on shock-droplet interactions from
FIG. 4. Comparison of the normalized upstream stagnation point drift between the
present results and previous studies (the experimental data of Igra et al.,61 and the
numerical data of Meng and Colonius 23 and Kaiser et al.18)
TABLE II. The initial conditions for n-dodecane droplet, pre-shock vapor, and post-shock vapor.
qðkg=m3Þ pðPaÞ uðm=sÞ TðKÞ lðPa /C1sÞ rðN=mÞ
n-Dodecane droplet 593.5 1.0 /C2 105 0.0 490.0 1.96 /C2 10–4 0.009
Pre-shock n-dodecane vapor 4.38 1.0 /C2 105 0.0 500.0 7.59 /C2 10–6 /C1/C1/C1
Post-shock n-dodecane vapor 10.15 2.17 /C2 105 123.45 510.49 /C1/C1/C1 /C1/C1/C1
Physics of Fluids ARTICLE pubs.aip.org/aip/pof
Phys. Fluids 37, 033358 (2025); doi: 10.1063/5.0255860 37, 033358-7
Published under an exclusive license by AIP Publishing
 29 August 2026 09:54:09

<!-- PDF_PAGE: 9 -->

3 aspects: the early-stage wave pattern and flow structure, the droplet
acceleration and deformation, and the vorticity evolution.
1. Early-stage wave pattern evolution and flow field
structure
Due to the acoustic impedance mismatch between the vapor and
the droplet, the interaction between the incident shock wave and the
droplet leads to the formation of a series of wave structures. Figure 5
depicts the influence of phase change on the evolution of wave patterns
under 3 different situations: no-phase-change, evaporation-dominated
phase change, and condensation-dominated phase change. In all cases,
the interaction of the incident shock wave with the droplet surface gen-
erates a reflected wave and a transmitted shock wave.62 The transmit-
ted shock then reflects at the downstream side of the droplet, forming
a reflected expansion wave. Additionally, the incident shock wave
FIG. 5. Early-stage evolution of the wave patterns in shock-droplet interactions for (a) no-phase-change, (b) evaporation, and (c) condensation cases.
Physics of Fluids ARTICLE pubs.aip.org/aip/pof
Phys. Fluids 37, 033358 (2025); doi: 10.1063/5.0255860 37, 033358-8
Published under an exclusive license by AIP Publishing
 29 August 2026 09:54:09

<!-- PDF_PAGE: 10 -->

undergoes Mach reflection, leading to a Mach stem. When phase
change is considered, additional wave structures are induced. For both
two-phase change situations, the droplet initially undergoes evapora-
tion. As shown in the first column (t/C3 ¼ 0.0033) of Figs. 5(b) and 5(c),
the vapor phase induces an additional evaporation shock wave, while
the liquid phase generates an extra evaporation rarefaction wave,
which are both absent in the classic shock-droplet interactions of
Fig. 5(a). When the superheated liquid vaporizes, a large amount of
vapor is suddenly generated, which in turn results in a local, abrupt
increase in pressure and density. Because vapor is highly compressible
FIG. 6. Temperature and pressure contours for (a) no-phase-change, (b) evaporation, and (c) condensation cases.
Physics of Fluids ARTICLE pubs.aip.org/aip/pof
Phys. Fluids 37, 033358 (2025); doi: 10.1063/5.0255860 37, 033358-9
Published under an exclusive license by AIP Publishing
 29 August 2026 09:54:09

<!-- PDF_PAGE: 11 -->

compared to liquid, these sudden changes steepen into an evaporation
shock wave in the vapor region. For the liquid side, this sudden genera-
tion of the evaporation shock wave at the interface should maintain
the mechanical equilibrium (or jump conditions), whose exact solution
is a rarefaction wave in the liquid region. This has also been reported
by the exact solutions of an n-dodecane evaporation Riemann prob-
lem.40 In addition, a contact discontinuity forms between the
evaporation-induced low-temperature vapor and the original high-
FIG. 7. The droplet deformation morphologies rendered using the ray tracing technique for (a) no-phase-change, (b) evaporation, and (c) condensation case s.
FIG. 8. The mass flux distribution on the droplet surface in the condensation-dominated case, with a schematic of the physical quantities describing drople t interface
deformation.
Physics of Fluids ARTICLE pubs.aip.org/aip/pof
Phys. Fluids 37, 033358 (2025); doi: 10.1063/5.0255860 37, 033358-10
Published under an exclusive license by AIP Publishing
 29 August 2026 09:54:09

<!-- PDF_PAGE: 12 -->

temperature vapor (t/C3 ¼ 0.0168). These wave structures have also been
observed in previous studies.33,34 In the evaporation-dominated case,
although the shock wave impact reduces the evaporation rate on the
droplet’s windward side, the droplet itself remains in an evaporation
state. Both the windward and leeward sides exhibit evaporation-
induced surface waves ( Fig. 5(b), t/C3 ¼ 0.0673). In the condensation-
dominated case, upon the shock impacting, condensation occurs on
the windward side of the droplet and therefore prevents the
FIG. 9. Time evolution of the normalized cross-stream diameter (a), streamwise diameter (b), upstream stagnation point drift (c), downstream stagnation p oint drift (d), upstream
stagnation point pressure (e), and downstream stagnation point pressure (f) for no-phase-change, evaporation, and condensation cases.
Physics of Fluids ARTICLE pubs.aip.org/aip/pof
Phys. Fluids 37, 033358 (2025); doi: 10.1063/5.0255860 37, 033358-11
Published under an exclusive license by AIP Publishing
 29 August 2026 09:54:09

<!-- PDF_PAGE: 13 -->

propagation of the evaporation-induced contact wave in these areas. A
condensation-dominated contact wave is observed in the interior of
the droplet ( Fig. 5(c), t/C3 ¼ 0.1347). Notably, the interaction between
the shock wave and the low-temperature vapor layer causes the vapor
layer to separate from the droplet surface ( Fig. 5(b), t
/C3 ¼ 0.1347). In
the condensation-dominated case, the formation of extra vortex struc-
tures is observed.
Figure 6 shows the temperature and pressure contours under 3
different conditions. First, we observe that the pressure distributions
are roughly consistent for all cases. The incident shock wave reflects at
the windward side, forming a high-pressure region, while the recircu-
lating zones develop at the leeward side of the droplet, where the pres-
sure is relatively low. The pressure difference between the windward
and leeward sides induces a horizontal force that drives the movement
and the flattening of the droplet.
63 Next, unlike the pressure contours,
the 3 cases show significantly different temperature fields. As shown in
Fig. 6(b) , the evaporated vapor has a lower temperature than that
behind the shock wave. In the evaporation-dominated case, the entire
droplet is surrounded by a low-temperature vapor layer, which is gen-
erated by evaporating the liquid of the droplet. The thickness of such a
vapor layer is much smaller on the windward side, indicating a rela-
tively smaller evaporation rate there, which is consistent with previous
studies,
38 primarily due to the increase in the vapor pressure by shock
impacting. Meanwhile, the condensation-dominated case only exhibits
evaporation in a small region near the droplet ’s equator, while in the
rest region the condensation effect prevents the formation of a low-
temperature vapor layer.
2. Droplet morphology and center of mass motion
To highlight the effect of phase change on the droplet interface
evolution, we employ the ray tracing technique to render the droplet
interface, as shown in Fig. 7 . When phase change is neglected,
the shear force of the airflow induces KH instability waves on the
droplet surface.
63 These waves first form on the windward side
(Fig. 7(a) , t/C3 ¼ 0.135) and then propagate toward the leeward
side ( Fig. 7(a), t/C3 ¼ 0.135–0.269), eventually coalescing into a liquid
film ( Fig. 7(a) , t/C3 ¼ 0.421). In the evaporation-dominated case, the
entire droplet is surrounded by an evaporated vapor layer, which pre-
vents the shear between the high-speed airflow and droplet surface. As
FIG. 10. The time evolution of the normalized center-of-mass drift (a), velocity (b), acceleration (c), and unsteady drag coefficient (d) for no-phase-chan ge, evaporation, and
condensation cases.
Physics of Fluids ARTICLE pubs.aip.org/aip/pof
Phys. Fluids 37, 033358 (2025); doi: 10.1063/5.0255860 37, 033358-12
Published under an exclusive license by AIP Publishing
 29 August 2026 09:54:09

<!-- PDF_PAGE: 14 -->

a result, the KH waves on the windward side of the droplet are sup-
pressed, leading to a smoother droplet surface [ Fig. 7(b) ]. In the
condensation-dominated case inFig. 7(c), the wrinkles on the droplet’s
windward side become significantly more pronounced during the early
stages (t/C3 ¼ 0.135), indicating a notable enhancement of the KH insta-
bility waves. In contrast, the leeward side of the droplet remains rela-
tively smooth, suggesting that the KH waves do not propagate toward
the leeward side and are instead suppressed by the local evaporation
there [see Fig. 6(c)].
The mass flux distribution on the droplet surface provides a clear
visualization of which regions are undergoing evaporation or conden-
sation. When the mass flux is positive, it indicates evaporation, while a
negative mass flux corresponds to condensation. As shown in Fig. 8,
the higher pressure on the windward side [see Fig. 6(c)] leads to a
condensation-dominated phase change on the droplet surface, while
the lower pressure in the equatorial region results in an evaporation-
dominated phase change. According to our previous study,
64 the evap-
oration effect tends to suppress the development of interface instabil-
ity, while the condensation effect promotes the development of
interface instability, which is consistent with the surface roughness in
Fig. 8. It is worth noting that due to the focusing of the Mach stem, the
pressure in the droplet’s downstream stagnation region experiences a
sudden increase, leading to a condensation-dominated phase change.
As a result, the leeward side of the droplet is subjected to strong shear
forces, leading to the formation of a lip (t
/C3 ¼ 0.269).
In the following, we focus on the quantitative result of the phase-
change effect on the droplet deformation. As shown inFig. 8,t h ei n t e r -
face deformation quantities are normalized by
FIG. 11. The contours of Y-vorticity on the plane Y ¼ 0 and the Q-criterion on the plane Z ¼ 0 for (a) no-phase-change, (b) evaporation, and (c) condensation cases.
Physics of Fluids ARTICLE pubs.aip.org/aip/pof
Phys. Fluids 37, 033358 (2025); doi: 10.1063/5.0255860 37, 033358-13
Published under an exclusive license by AIP Publishing
 29 August 2026 09:54:09

<!-- PDF_PAGE: 15 -->

D/C3
cro=wise ¼ Dcro=wise=D0;
x/C3
usp=dsp ¼ð xusp=dsp /C0 xusp0 =dsp0 Þ=D0;
(
(28)
where xusp0 =dsp0 represents the initial positions of the droplet ’s
upstream and downstream stagnation points. As shown in Figs. 9(a)
and 9(b),t h ee v o l u t i o no fD/C3
cro exhibits a nearly exponential increase
with time due to the stretching of liquid sheets, while D/C3
wise shows a
smoothly decreasing tendency. In the evaporation-dominated case, the
reduction in airflow shear force suppresses the growth of surface KH
instabilities, thereby inhibiting the generation of liquid ligaments and
sheets, which are promoted in the condensation-dominated case. The
significant enhancement of the growth of ligaments and liquid sheets
by the condensation is clearly illustrated in Fig. 9(a) for t
/C3 ¼ 0.269–
0.421. As the evolution ofD/C3
wise is influenced by both the degree of flat-
tening and the leeward crater depth, we additionally choose the drift of
the droplet’s upstream and downstream stagnation points x
/C3
usp=dsp in
Figs. 9(c) and 9(d) to comprehensively evaluate the horizontal defor-
mation of the droplet. Compared to the no-phase-change case, both
D
/C3
wise and x/C3
dsp show smaller reductions in the evaporation case, indicat-
ing a weaker flattening. While in the condensation-dominated case,
the decrease tendency in x
/C3
dsp is enhanced, indicating a greater
flattening. In addition, the reduction inD/C3
wise slowing down in the later
stages can be attributed to the growth of the leeward crater. Since the
droplet flattening is mainly influenced by the pressure difference
between the windward and leeward sides, we show the time evolution
of the pressure at the droplet’ss t a g n a t i o np o i n t si nFigs. 9(e) and 9(f).
The agreement in the pressure distribution at the upstream stagnation
point for the 3 cases is consistent with the distribution of x
/C3
usp.
Moreover, the sudden increase in pressure at t/C3 ¼ 0.1 is attributed to
the focusing of the Mach stem, which results in crater development.
To quantify the droplet motion, following Meng and Colonius,23
the calculation of the center-of-mass drift, velocity, acceleration, and
unsteady drag coefficient in a non-dimensional form is given by
FIG. 12. Time evolution of the (a) positive circulation Cþ
xz on the x-z plane, (b) negative circulation C/C0
xz on the x-z plane, (c) total absolute circulation jCxz j on the x-z plane, and
(d) interface circulation jCi j for the no-phase-change, evaporation, and condensation cases.
TABLE III. The initial conditions for post-shock n-dodecane vapor at various Mach
numbers.
Mach number qðkg=m3Þ pðPaÞ uðm=sÞ TðKÞ
1.27 7.33 1.62 /C2 105 75.38 505.99
1.37 8.66 1.89 /C2 105 100.01 508.21
1.47 10.15 2.17 /C2 105 123.45 510.49
Physics of Fluids ARTICLE pubs.aip.org/aip/pof
Phys. Fluids 37, 033358 (2025); doi: 10.1063/5.0255860 37, 033358-14
Published under an exclusive license by AIP Publishing
 29 August 2026 09:54:09

<!-- PDF_PAGE: 16 -->

xc ¼
ð
X
xal ql dV
ð
X
al ql dV
; x/C3
c ¼ Dx
D0
¼ xc /C0 x0
D0
;
uc ¼
ð
X
ual ql dV
ð
X
al ql dV
; u/C3
c ¼ uc
ug
;
ac ¼ d
dt
ð
X
ual ql dV
ð
X
al ql dV
0
BBB@
1
CCCA; a/C3
c ¼ acD0
u2
g
;
Cd ¼ 2Fd
qu2S ¼ 2Ml ac
qg ðug /C0 ucÞ2D0
:
8
>>>>
>
>
>
>
>
>
>
>
>
>
>
>
>
>
>>>
>
>
>
>
>
>
>
>
>
>
<
>>
>
>
>
>>>
>
>
>
>
>
>
>
>
>
>
>
>
>
>>>
>
>
>
>
>
>
>
:
(29)
The term a
l ql denotes the liquid phase density, Ml represents
the time-dependent droplet mass, and x0 is the initial position of the
droplet’sm a s sc e n t r o i d .Figure 10 compares the center-of-mass
motion between the no-phase-change, evaporation-dominated, and
condensation-dominated cases. The droplet ’s acceleration peaks at
t
/C3 ¼ 0.04, corresponding to the transition from a regular reflection to a
Mach reflection. 23 Then, the Mach stem focuses on the droplet ’s
downstream stagnation point and increases the pressure on the lee-
ward side. As a result, the pressure difference between the windward
and leeward sides decreases, leading to a rapid reduction in droplet
acceleration. Subsequently, the acceleration begins to increase again
due to the expansion of the droplet in its cross-stream direction and
the development of recirculating zones with relatively low pressure on
the leeward side of the droplet.
63 Compared to the no-phase-change
case, the evaporation-dominated case experiences weaker shear forces
of the airflow, resulting in a smaller cross-stream diameter. As the
aerodynamic force acting on the droplet is positively correlated with its
cross-stream diameter, the drag force and acceleration are therefore
smaller in Figs. 10(c)–10(d). In contrast, the condensation-dominated
FIG. 13. Temperature and pressure con-
tours for (a) 1.27 Ma, (b) 1.37 Ma, and (c)
1.47 Ma cases. The color maps do not
represent the actual minimum and maxi-
mum values but are chosen to best illus-
trate all relevant features.
Physics of Fluids ARTICLE pubs.aip.org/aip/pof
Phys. Fluids 37, 033358 (2025); doi: 10.1063/5.0255860 37, 033358-15
Published under an exclusive license by AIP Publishing
 29 August 2026 09:54:09

<!-- PDF_PAGE: 17 -->

case shows the opposite trend, with a larger cross-stream diameter and
consequently stronger aerodynamic forces. The evolution of the cen-
ter-of-mass velocity exhibits a similar difference for the 3 cases.
Additionally, as the center-of-mass drift of the droplet is relatively
small, there is a minor difference among the three cases.
3. Analysis of vorticity dynamics
In this section, we analyze the effect of phase change on vortex
generation during the droplet evolution, with particular focus on its
influence on surface instabilities. As shown inFig. 11, for the Y-vortic-
ity on the plane Y ¼ 0, when the incident shock wave passes through
the droplet (t/C3 ¼ 0.0673), the vorticity production occurs on the drop-
let surface due to the baroclinic mechanism (misalignment of the
density gradient and the pressure gradients). Compared to the no-
phase-change case, the evaporation-dominated and condensation-
dominated scenarios show an increased magnitude of the negative vor-
ticity and the positive vorticity, respectively.Figure 11 also presents the
Q-criterion on the plane Z ¼ 0. The evaporation-dominated droplet
surface generates larger positive Q-values, indicating that vorticity
deposition on the droplet surface under evaporation effects is primarily
rotation-dominated. In contrast, distinct negative Q-values are found
near the droplet surface for the condensation-dominated case, imply-
ing a shear effect
36 for vorticity deposition. Consequently, compared to
Fig. 11(a), this stronger shear effect on the windward side enhances the
growth of KH instability waves, leading to an onset location closer to
the droplet ’s upstream stagnation point ( Figs. 11(a) and 11(c),
t
/C3 ¼ 0.1347). As mentioned above, the vapor layer in the evaporation-
dominated case inhibits the generation of KH instability waves, corre-
sponding to a smooth interface in Fig. 11(b). Additionally, to quantify
the vortical structure evolution in Fig. 11, we also illustrate the time
evolution of positive, negative, and interface circulation (Cþ, C/C0 , Ci)
in Fig. 12 . Circulation is defined as the line integral of the velocity
along a closed path,
C ¼
ð
(
C
u /C1dl ¼
ðð
S
ðr /C2 uÞ/C1dS ¼
ðð
S
x /C1dS; (30)
where u is the velocity vector of the fluid and x is the vorticity. In
Fig. 12, the vapor phase circulation on the x-z planeC6
xz, and the circu-
lation at the interface can be calculated by
C6
xz ¼
ðð
S
x6
y Hð/ÞdS;
C6
i ¼
ðð
S
dð/ÞðDutiÞ6dS;
(31)
where Hð/Þ and dð/Þ represent the Heaviside function and its deriva-
tive (i.e., the Dirac delta function), respectively. The term Du ¼
u1 /C0 u2 is the difference between the two fluids andti denotes the tan-
gential component of the interface, which is normal to the gradient of
the level-set function. As expected,Figs. 12(a)–12(c) indicate the mag-
nitudes of the positive, the negative, and the absolute circulation in the
condensation-dominated condition are significantly larger than those
FIG. 14. Droplet deformation morphologies rendered using the ray tracing technique for (a) 1.27 Ma, (b) 1.37 Ma, and (c) 1.47 Ma cases.
Physics of Fluids ARTICLE pubs.aip.org/aip/pof
Phys. Fluids 37, 033358 (2025); doi: 10.1063/5.0255860 37, 033358-16
Published under an exclusive license by AIP Publishing
 29 August 2026 09:54:09

<!-- PDF_PAGE: 18 -->

in the no-phase-change case. However, in the evaporation-dominated
case, compared to the no-phase-change case, the increase in the total
circulation (t/C3 < 0.1) in the early stage is attributed to the enhancement
of the negative circulation. While the decrease in the total circulation
in the later stage (t
/C3 > 0.3) is mainly due to the significant reduction of
the positive circulation.Figure 12(d)shows the magnitude of the circu-
lation on the interface. The circulation exhibits a significant decrease
under evaporation-dominated conditions, which further suggests a
substantial reduction in the shear forces exerted by the airflow, as
encapsulated by the evaporation layer.
B. Effects of Mach number
In shock-droplet interactions involving phase change, the shock
intensity plays a critical role in altering both the phase change and defor-
mation dynamics. This section evaluates the effects of shock intensity on
droplet phase change by 3 different shock Mach numbers. Under
condensation-dominated conditions, the phase change behavior of the
droplet becomes more complex, with simultaneous evaporation and con-
densation occurring on its surface. Therefore, this section merely focuses
on condensation-dominated cases to analyze the effects of Mach number
on droplet dynamics. The initial conditions of n-dodecane vapor behind
t h es h o c kw a v ef o rt h e3M a c hn u m b e r sa r el i s t e di nTable III.
T h ee v o l u t i o no ft h ew a v es t r u c t u r ei nt h ee a r l ys t a g eo ft h ef l o w
field is similar for different Mach numbers and therefore will not be
elaborated here.Figure 13 shows the pressure and temperature contour
plots for the selected 3 Mach numbers. As the Mach number decreases,
both the pressure and temperature surrounding the droplet signifi-
cantly decrease. According to a previous study,
38 lower pressure indi-
cates that the liquid molecules on the droplet ’s surface require less
kinetic energy to overcome the vapor pressure, thereby increasing the
evaporation rate of the droplet. As shown in Fig. 13(a),t h ea r e ao ft h e
low-temperature vapor layer on the droplet surface increases signifi-
cantly at lower Mach numbers.
The intensity of the shock wave affects the phase change of the
droplet, which in turn influences the droplet deformation. As the
FIG. 15. Q-criterion and zero level-set isosurface for (a) no-phase-change, (b) evaporation, and (c) condensation cases. The computed Q-criterion isosurface is colored by
velocity magnitude, and the zero level-set isosurface is colored by mass flux.
Physics of Fluids ARTICLE pubs.aip.org/aip/pof
Phys. Fluids 37, 033358 (2025); doi: 10.1063/5.0255860 37, 033358-17
Published under an exclusive license by AIP Publishing
 29 August 2026 09:54:09

<!-- PDF_PAGE: 19 -->

Mach number decreases, the increased surface evaporation rate sup-
presses the development of surface instabilities, resulting in a smoother
droplet surface, as illustrated in Fig. 14(a). Meanwhile, at lower Mach
numbers, the stretching and rupture of the liquid film are also sup-
pressed; see Figs. 14(a)–14(c).T h er e a s o nf o rt h i sb e h a v i o ri st w o f o l d ,
i.e., (1) the reduction in post-shock airflow velocity diminishes the
shear force acting on the droplet’s equator, and (2) the weakened con-
densation effect on the droplet’s windward side further reduces shear
forces.
To gain a deeper understanding of the effect of Mach number,
Fig. 15 shows the mass flux distribution on the droplet surface and the
Q-criterion for the three different Mach numbers. As the Mach num-
ber decreases, the positive and negative Q-criterion isosurfaces in
Fig. 15 reveal that more vortex structures are generated around the
droplet, while the shear-dominant regions diminish. In this situation,
the generation of KH waves on the droplet surface is suppressed,
resulting in a smoother surface. This conclusion is consistent with
the vorticity analysis for the evaporation-dominated case in Sec. IV A.
For the mass flux distribution in Fig. 15 , as the Mach number
decreases, the condensation effect on the windward side of the droplet
is significantly reduced. Finally, the Mach number effect on the vortic-
ity is demonstrated by Fig. 16. The interface circulation magnitude in
Fig. 16(a) increases with the Mach number. When decreasing the
Mach number, both the positive and negative circulation magnitudes
become smaller, corresponding to the enhanced evaporation and con-
densation rates; see Fig. 16(b). Additionally, we observe that the peak
of the negative circulation, which is induced by the shock impact,
becomes significantly smaller for weaker shocks at lower Mach num-
bers. We note that the total mass flux in Fig. 16(c) indicates that the
droplet undergoes an overall evaporation process for the 2 low Mach
numbers (1.27 and 1.37), corresponding to a monotonic decrease in
the droplet mass in Fig. 16(d).H o w e v e r ,w h e nt h es h o c ki n t e n s i t yi s
large enough, e.g., at a Mach number of 1.47, the total mass flux
changes from positive to negative in the late stage, which is caused by
the transition from evaporation to condensation, as demonstrated by
the non-monotonic evolution of the droplet mass inFig. 16(d).
V. CONCLUSION
In this study, we have performed the first 3D numerical simula-
tions of shock interactions with an n-dodecane fuel droplet in a
FIG. 16. Time evolution of the interface circulation (a), the average positive and negative mass fluxes (b), the average total mass flux (c), and normalized dr oplet mass for the
Ma 1.27, Ma 1.37, and Ma 1.47 cases. The average positive and negative mass fluxes are indicated by þ and /C0 , respectively.
Physics of Fluids ARTICLE pubs.aip.org/aip/pof
Phys. Fluids 37, 033358 (2025); doi: 10.1063/5.0255860 37, 033358-18
Published under an exclusive license by AIP Publishing
 29 August 2026 09:54:09

<!-- PDF_PAGE: 20 -->

high-temperature vapor environment, accounting for both phase
change and real fluid effects. After validating the numerical meth-
ods and physical models by comparing numerical and experimen-
tal data of shock interaction with water droplets without phase
change, we numerically study an n-dodecane droplet (initial tem-
perature 490 K) inside a 500 K n-dodecane vapor, impacted by a
Mach 1.47 shock wave. To evaluate the phase change effects, three
cases were considered: no-phase-change, evaporation-dominated,
and condensation-dominated phase change. In the evaporation-
dominated case, a low-temperature vapor layer forms on the drop-
let surface, reducing shear forces exerted by the surrounding
airflow, thereby suppressing the development of KH instability
waves on its surface. This leads to weaker droplet deformation, a
smaller windward area, and lower acceleration and drag coeffi-
cients, compared to the no-phase-change case. In the
condensation-dominated case, evaporation occurs only in the low-
pressure region near the droplet ’s equator, while condensation
occurs elsewhere. Such condensation increases shear forces, pro-
moting KH instability growth, which promotes droplet flattening,
sheet stretching, and ligament formation. Consequently, the
increased cross-stream diameter results in higher acceleration and
drag coefficients. Finally, as the shock intensity influences the
droplet phase change process, we investigated the condensation-
dominated droplet phase change scenarios under 3 different Mach
numbers. The decrease in the Mach numbers reduces the vapor
pressure around the droplet, resulting in an increased evaporation
rate and a transition from condensation-dominated to
evaporation-dominated phase change. This transition suppresses
the development of surface instability waves and significantly
reduces the circulation at the gas –liquid interface. Our future
research is subject to numerical simulation of shock-impacted
reactive droplets in multi-component vapor environments.
ACKNOWLEDGMENTS
We thank the organization of the 26th International
Conference on Theoretical and Applied Mechanics (ICTAM 2024)
of the International Union of Theoretical and Applied Mechanics
(IUTAM) in Daegu, Korea, held on August 25, 2024, for creating
the platform at which, and for bringing together the audience to
which, this work was first presented. This work was supported by
the National Natural Science Foundation of China (Grant Nos.
1247021811 and 11902271).
AUTHOR DECLARATIONS
Conflict of Interest
The authors have no conflicts to disclose.
Author Contributions
Jiaxi Song: Conceptualization (equal); Data curation (lead); Formal
analysis (equal); Investigation (equal); Methodology (equal); Software
(equal); Validation (lead); Visualization (lead); Writing– original draft
(lead). Tian Long: Formal analysis (equal); Investigation (equal);
Methodology (equal); Software (equal). Shucheng Pan:
Conceptualization (equal); Funding acquisition (lead); Project adminis-
tration (lead); Supervision (lead); Writing– review & editing (lead).
DATA AVAILABILITY
The data that support the findings of this study are available from
the corresponding author upon reasonable request.
REFERENCES
1G. D. Waldman and W. Reinecke, “Raindrop breakup in the shock layer of a
high-speed vehicle,” AIAA J. 10, 1200–1204 (1972).
2S. Patil and S. Sahu, “Air swirl effect on spray characteristics and droplet dis-
persion in a twin-jet crossflow airblast injector, ” Phys. Fluids 33, 073314
(2021).
3E. Johnson and T. Colonius, “Numerical simulations of non-spherical bubble
collapse,” J. Fluid Mech. 629, 231–262 (2009).
4Y. Yang, T. Kubota, and E. E. Zukoski, “Applications of shock-induced mixing
to supersonic combustion, ” AIAA J. 31, 854–862 (1993).
5J. C. Hermanson, “Dynamics of supersonic droplets of volatile liquids, ” AIAA
J. 45(3), 730–733 (2007).
6J. Urzay, “Supersonic combustion in air-breathing propulsion systems for
hypersonic flight,” Annu. Rev. Fluid Mech. 50, 593–627 (2018).
7J. Redding, “Deformation, fragmentation and vaporization of volatile liquid drop-
lets in Shock-Laden environments,” M.S. thesis (University of Cincinnati, 2020).
8J. O. Hinze, “Critical speeds and sizes of liquid globules, ” Appl. Sci. Res. 1,2 7 3
(1949).
9A. R. Hanson, E. G. Domich, and H. S. Adams, “Shock tube investigation of
the breakup of drops by air blasts, ” Phys. Fluids 6, 1070 (1963).
10A. A. Ranger and J. A. Nicholls, “Aerodynamic shattering of liquid drops, ”
AIAA J. 7, 285 (1969).
11P. D. Patel and T. G. Theofanous, “Hydrodynamic fragmentation of drops, ”
J. Fluid Mech. 103, 207–223 (1981).
12M. Pilch and C. A. Erdman, “Use of breakup time data and velocity history data
to predict the maximum size of stable fragments for acceleration-induced
breakup of a liquid drop, ” Int. J. Multiphase Flow 13,7 4 1–757 (1987).
13T. G. Theofanous, “Aerobreakup of Newtonian and viscoelastic liquids, ” Annu.
Rev. Fluid Mech. 43, 661 (2011).
14T. G. Theofanous and G. J. Li, “On the physics of aerobreakup, ” Phys. Fluids
20, 052103 (2008).
15S. Sharma, A. P. Singh, S. S. Rao, A. Kumar, and S. Basu, “Shock induced aero-
breakup of a droplet, ” J. Fluid Mech. 929, A27 (2021).
16S. Sharma, N. K. Chandra, A. Kumar, and S. Basu, “Shock-induced atomisation
of a liquid metal droplet, ” J. Fluid Mech. 972, A7 (2023).
17H. Chen, “Two-dimensional simulation of stripping breakup of a water drop-
let,” AIAA J. 46, 1135–1143 (2008).
18J. W. J. Kaiser et al. , “Investigation of interface deformation dynamics during
high-Weber number cylindrical droplet breakup, ” Int. J. Multiphase Flow 132,
103409 (2020).
19C. H. Chang, X. Deng, and T. G. Theofanous, “Direct numerical simulation of
interfacial instabilities: A consistent, conservative, all-speed, sharp-interface
method,” J. Comput. Phys. 242, 946–990 (2013).
20J. Han and G. Tryggvason, “Secondary breakup of axisymmetric liquid drops.
II. Impulsive acceleration, ” Phys. Fluids 13, 1554 (2001).
21J. C. Meng and T. Colonius, “Numerical simulation of the aerobreakup of a
water droplet,” J. Fluid Mech. 835, 1108–1135 (2018).
22B. Dorschner, L. Biasiori-Poulanges, K. Schmidmayer, H. El-Rabii, and T.
Colonius, “On the formation and recurrent shedding of ligaments in droplet
aerobreakup,” J. Fluid Mech. 904, A20 (2020).
23J. C. Meng and T. Colonius, “Numerical simulations of the early stages of high-
speed droplet breakup, ” Shock Waves 25, 399–414 (2015).
24S. Sembian, M. Liverts, N. Tillmark, and N. Apazidis, “Plane shock wave inter-
action with a cylindrical water column, ” Phys. Fluids 28, 056102 (2016).
25G. Xiang and B. Wang,“Numerical study of a planar shock interacting with a cylin-
drical water column embedded with an air cavity,” J. Fluid Mech.825, 825 (2017).
26Y. Liang, Y. Jiang, C.-Y. Wen, and Y. Liu, “Interaction of a planar shock wave and
a water droplet embedded with a vapour cavity,” J. Fluid Mech. 885, R6 (2020).
27Y. Jiao, S. J. Schmidt, and N. A. Adams, “Simulating shock interaction with a
cavity-embedded cylinder/droplet using a real-fluid hybrid scheme at near-
critical conditions,” Phys. Rev. Fluids 9(7), 074002 (2024).
Physics of Fluids ARTICLE pubs.aip.org/aip/pof
Phys. Fluids 37, 033358 (2025); doi: 10.1063/5.0255860 37, 033358-19
Published under an exclusive license by AIP Publishing
 29 August 2026 09:54:09

<!-- PDF_PAGE: 21 -->

28R. J. Haywood, M. Renksizbulut, and G. D. Raithby, “Numerical solution of
deforming evaporating droplets at intermediate Reynolds numbers, ” Numer.
Heat Transfer 26(3), 253–272 (1994).
29R. J. Haywood, M. Renksizbulut, and G. D. Raithby, “Transient deformation
and evaporation of droplets at intermediate Reynolds numbers, ” Int. J. Heat
Mass Transfer 37(9), 1401–1409 (1994).
30G. Strotos, I. Malgarinos, N. Nikolopoulos, and M. Gavaises, “Numerical inves-
tigation of aerodynamic droplet breakup in a high temperature gas environ-
ment,” Fuel 181, 450–462 (2016).
31B. Boyd, S. Becker, and Y. Ling, “Simulation and modeling of the vaporization
of a freely moving and deforming drop at low to moderate Weber numbers, ”
Int. J. Heat Mass Transfer 218, 124735 (2024).
32H. W. J. Goossens, J. W. Cleijne, H. J. Smolders, and M. E. H. van Dongen,
“Shock wave induced evaporation of water droplets in a gas-droplet mixture, ”
Exp. Fluids 6, 561–568 (1988).
33P. Das and H. S. Udaykumar, “A sharp-interface method for the simulation of
shock-induced vaporization of droplets, ” J. Comput. Phys. 405, 109005 (2020).
34P. Das and H. S. Udaykumar, “A simulation-derived surrogate model for the
vaporization rate of aluminum droplets heated by a passing shock wave, ” Int. J.
Multiphase Flow 130, 103299 (2020).
35P. Das and H. S. Udaykumar, “Sharp-interface calculations of the vaporization
rate of reacting aluminum droplets in shocked flows, ” Int. J. Multiphase Flow
134, 103442 (2021).
36W. Zhu, H. Zheng, and N. Zhao, “Numerical investigations on the deformation
and breakup of an n-decane droplet induced by a shock wave, ” Phys. Fluids
34(6), 063306 (2022).
37T. Xiong, C. Shao, and K. Luo, “Exploration of shock –droplet interaction based
on high-fidelity simulation and improved theoretical model, ” J. Fluid Mech.
988, A46 (2024).
38J. P. Redding and P. Khare, “A computational study on shock induced defor-
mation, fragmentation and vaporization of volatile liquid fuel droplets, ” Int. J.
Heat Mass Transfer 184, 122345 (2022).
39P. Tarey, P. Ramaprabhu, and J. A. McFarland, “Evolution of a shock-impacted
reactive liquid fuel droplet with evaporation effects: A numerical study, ” Int. J.
Multiphase Flow 174, 104744 (2024).
40T. Long, J. Cai, and S. Pan, “A fully conservative sharp-interface method for
compressible multiphase flows with phase change, ” J. Comput. Phys. 493,
112501 (2023).
41T. Long, J. Cai, and S. Pan, “An accelerated conservative sharp-interface method
for multiphase flows simulations, ” J. Comput. Phys. 429, 110021 (2021).
42S. Pan, L. Han, X. Hu, and N. A. Adams, “A conservative interface-interaction
method for compressible multi-material flows, ” J. Comput. Phys. 371, 870–895
(2018).
43J. W. Chae, H. S. Yang, and W. S. Yoon,“Supercritical droplet dynamics and emis-
sion in low speed cross-flows,” J. Mech. Sci. Technol.22(8), 1586–1601 (2008).
44Y. Jiao, S. J. Schmidt, and N. A. Adams, “Effect of gas cavity size and eccentric-
ity on shock interaction with a cylinder at near-critical conditions, ” Phys.
Fluids 36(9), 096108 (2024).
45B. Boyd and D. Jarrahbashi, “Numerical study of the transcritical shock-droplet
interaction,” Phys. Rev. Fluids 6(11), 113601 (2021).
46A. Zein, M. Hantke, and G. Warnecke, “Modeling phase transition for com-
pressible two-phase flows applied to metastable liquids, ” J. Comput. Phys. 229,
2964–2998 (2010).
47T. Paula, S. Adami, and N. A. Adams, “Analysis of the early stages of liquid-
water-drop explosion by numerical simulation, ” Phys. Rev. Fluids 4(4), 044003
(2019).
48E. W. Lemmon and M. L. Huber, “Thermodynamic properties of n-dodecane, ”
Energy Fuels 18, 960–967 (2004).
49E. W. Lemmon and R. Span, “Short fundamental equations of state for 20
industrial fluids,” J. Chem. Eng. Data 51, 785 (2006).
50G. S. Jiang and C. W. Shu, “Efficient implementation of weighted ENO
schemes,” J. Comput. Phys. 126, 202 (1996).
51P. L. Roe, “Approximate Riemann solvers, parameter vectors, and difference
schemes,” J. Comput. Phys. 43, 357–372 (1981).
52C. W. Shu and S. Osher, “Efficient implementation of essentially non-
oscillatory shock capturing schemes, ” J. Comput. Phys. 77, 439–471 (1988).
53S. Osher and J. A. Sethian, “Fronts propagating with curvature-dependent
speed: Algorithms based on Hamilton-Jacobi formulations, ” J. Comput. Phys.
79,1 2–49 (1988).
54X. Hu, B. Khoo, N. A. Adams, and F. Huang, “A conservative interface method
for compressible flows, ” J. Comput. Phys. 219(2), 553–578 (2006).
55M. Sussman, P. Smereka, and S. Osher, “A level set approach for computing
solutions to incompressible two-phase flow, ” J. Comput. Phys. 114,1 4 6–159
(1994).
56R. P. Fedkiw, T. D. Aslam, B. Merriman, and S. Osher, “A non-oscillatory
Eulerian approach to interfaces in multimaterial flows (the ghost fluid
method),” J. Comput. Phys. 152, 457–492 (1999).
57A. H. Persad and C. A. Ward, “Expressions for the evaporation and condensa-
tion coefficients in the Hertz-Knudsen relation, ” Chem. Rev. 116, 7727 (2016).
58I. H. Bell, J. Wronski, S. Quoilin, and V. Lemort, “Pure and pseudo-pure fluid
thermophysical property evaluation and the open-source thermophysical prop-
erty library CoolProp, ” Ind. Eng. Chem. Res. 53(6), 2498–2508 (2014).
59A. Harten, “Adaptive multiresolution schemes for shock computations, ”
J. Comput. Phys. 115(2), 319–338 (1994).
60L. H. Han, X. Y. Hu, and N. A. Adams, “Adaptive multi-resolution method for
compressible multi-phase flows with sharp interface model and pyramid data
structure,” J. Comput. Phys. 262, 131–152 (2014).
61D. Igra and K. Takayama, “Numerical simulation of shock wave interaction
with a water column, ” Shock Waves 11(3), 219–228 (2001).
62D. Ranjan, J. Oakley, and R. Bonazza, “Shock-bubble interactions, ” Annu. Rev.
Fluid Mech. 43(1), 117–140 (2011).
63N. Liu, Z. Wang, M. Sun, H. Wang, and B. Wang, “Numerical simulation of
liquid droplet breakup in supersonic flows, ” Acta Astronaut. 145,1 1 6–130
(2018).
64J. Song and S. Pan, “Numerical investigation of the Richtmyer-Meshkov insta-
bility for the vapor-liquid interface with phase change, ” Sci. Sin-Phys. Mech.
Astron. 54(10), 104710 (2024).
Physics of Fluids ARTICLE pubs.aip.org/aip/pof
Phys. Fluids 37, 033358 (2025); doi: 10.1063/5.0255860 37, 033358-20
Published under an exclusive license by AIP Publishing
 29 August 2026 09:54:09
