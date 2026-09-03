<!-- PDF_PAGE: 1 -->

Combustion and Flame 231 (2021) 111484 
Contents lists available at ScienceDirect 
Combustion and Flame 
journal homepage: www.elsevier.com/locate/combustflame 
Numerical study on rotating detonation stability in two-phase 
kerosene-air mixture 
Zhaoxin Ren, Longxi Zheng ∗
School of Power and Energy, Northwestern Polytechnical University, Xi’an 710072, China 
a r t i c l e i n f o 
Article history: 
Received 23 June 2020 
Revised 24 April 2021 
Accepted 26 April 2021 
Available online 24 May 2021 
Keywords: 
Rotating detonation 
Two-phase 
Kerosene 
Stability 
Total pressure 
Total temperature 
a b s t r a c t 
Kerosene/air two-phase rotating detonation is numerically investigated to ﬁnd out the limits of detona- 
tion stability as a function of total pressure and total temperature considering the operation conditions of 
the detonation engine. The Eulerian-Lagrangian two-phase governing system is used and the kerosene/air 
two-step reaction mechanism is applied to simulate the unsteady features, such as self-sustained prop- 
agation and quenching. The ﬁndings from the parametric study show that stable rotating detonation is 
achieved in a limited range of total pressure and the increasing total temperature contributes to deto- 
nation stability. The bifurcated wave structure is formed in the two-phase rotating detonation and the 
promotion of droplet evaporation tends to weaken this near-inlet complex wave feature. The reaction- 
dominated quenching and the evaporation-dominated quenching are two mechanisms for the breakdown 
of the detonation front, which is due to the interaction among ﬂuid dynamics, droplet evaporation, and 
exothermic reaction. 
©2 0 2 1 The Combustion Institute. Published by Elsevier Inc. All rights reserved. 
1. Introduction 
Rotating detonation engine (RDE) has been studied widely in 
recent years [1–5] owing to its advantages of fast reaction rate, low 
entropy production, and high eﬃciency of thermodynamic cycle. 
The rotating detonation wave (RDW) propagates in the combus- 
tion chamber of RDE with cylinder or concentric cylinder shapes to 
produce combustion products with high temperature and pressure, 
which generates thrust continuously. The combination of RDE with 
a turbine engine or rocket engine has the advantage from a wide 
range of application conditions, such as ﬂight Mach numbers, mass 
ﬂow rates, and the associated thrusts. The detailed features of RDE 
have been investigated on the fuel injection, fuel-oxygen mixing, 
ignition, stable/unstable propagation of RDW, and thrust/impulse 
performance by theoretical analysis, experiment, and numerical 
simulation since 1994 [6] . 
Most of the previous research on RDE focused on hydrogen 
and hydrocarbon gaseous fuels with low density. Hydrogen is the 
most studied fuel for RDE due to the low activation energy of 
hydrogen-air chemical reaction and high speciﬁc impulse. Anand 
et al. [7] experimentally investigated the effects of fuel injection 
patterns on the operability and performance of hydrogen-air rotat- 
ing detonation in a rotating detonation combustor (RDC). They di- 
∗ Corresponding author. 
E-mail address: zhenglx@nwpu.edu.cn (L. Zheng). 
vided the three basic modes of RDW propagation and found that 
the length-to-diameter ratio of the fuel injection nozzle decides 
the number of RDWs. The RDC operability depends on the air- 
ﬂow rate as well as the equivalence ratio. Xie et al. [8] studied 
the operating diagram of hydrogen-air RDC under fuel-lean condi- 
tions by experiments and they classiﬁed four combustion modes 
with the variation of equivalence ratios and mass ﬂow rates of air. 
They [9] also analyzed the oxygen-enriched hydrogen-air rotating 
detonation and considered the effects of equivalent ratios, mass 
ﬂow rates, and oxygen volume fractions. The increase of air mass 
ﬂow rate and oxygen volume fraction is expected to broaden the 
stability limit of RDW. The US Air Force Research Lab [10] used 
OH chemiluminescence imaging to investigate the propagation of 
hydrogen-air RDW and observed the size and shape of RDW struc- 
ture in an optically accessible RDC for the ﬁrst time. They found 
that the wave numbers in RDC are affected by airﬂow rates and 
the non-ideal fuel-air mixing results in the unsteady dynamics of 
RDWs. Frolov et al. [11] tested a large-scale RDC fueled by hy- 
drogen and measured the maximum net thrust (6 kN) and spe- 
ciﬁc impulse (~30 0 0 s). Researchers also focused on ethylene and 
acetylene fuels. Ishihara et al. [12] experimentally studied the ro- 
tating detonation rocket engine (RDRE) with the ethylene-oxygen 
mixtures and carried out the operation for a long time (maxi- 
mum 10 s) by applying heat resistant material. They measured 
the maximum thrust (301 N) and the maximum speciﬁc impulse 
(144 s). The ethylene-air RDW in the hollow combustor was stud- 
https://doi.org/10.1016/j.combustﬂame.2021.111484 
0010-2180/© 2021 The Combustion Institute. Published by Elsevier Inc. All rights reserved. 
i An update to this article is included at the end

<!-- PDF_PAGE: 2 -->

Z. Ren and L. Zheng Combustion and Flame 231 (2021) 1114 8 4 
Nomenclature 
B M mass transfer number (–) 
c L speciﬁc heat of liquid fuel (J kg −1 K −1 ) 
c p speciﬁc heat of mixture gas (J kg −1 K −1 ) 
d d droplet diameter (m) 
D k diffusion coeﬃcient of k th species (m 2 s −1 ) 
e t speciﬁc total energy (J kg −1 ) 
h speciﬁc enthalpy (J kg −1 ) 
h V,sf evaporated vapor enthalpy (J kg −1 ) 
L k Knudsen layer thickness (m) 
L V latent heat of droplet evaporation (J kg −1 ) 
m mass (kg) 
Nu Nusselt number (–) 
N c Number of droplets in one computation cell 
P static pressure (Pa) 
P 0 total pressure (Pa) 
Pr Prandtl number (–) 
q heat ﬂux (J m −2 s −1 ) 
R universal gas constant (J K −1 mol −1 ) 
Re d droplet Reynolds number (–) 
S i source term 
Sc Schmit number (–) 
Sh Sherwood number (–) 
T static temperature (K) 
T 0 total temperature (K) 
T B, L liquid boiling temperature (K) 
t a droplet acceleration time (s) 
u velocity (m s −1 ) 
W molecular weight of mixture gas (kg/mol) 
Y k mass fraction of kth species (–) 
λ thermal conductivity (W m −1 K −1 ) 
μ dynamic viscosity (Pa s) 
ρ density (kg m −3 ) 
/Phi1s spray equivalence ratio (–) 
ied [13] and the contraction ratio of the Laval nozzle was found 
to affect the operability of RDW. Anand et al. [14] investigated the 
performance of the hollow RDC with ethylene-air mixtures by ex- 
periments and illustrated the high-frequency instability of deto- 
nation that occurred in the RDRE. Bykovskii [15] et al. analyzed 
the acetylene-oxygen RDC in annular combustors and valued the 
total pressure loss from the injectors. Zhong et al. [16] studied 
the effects of ethylene-acetylene-hydrogen mixtures on the RDW 
and found that the increase of acetylene and hydrogen in the 
mixture extends the stable operating regime of RDC. The prop- 
agation features of RDW with hydrogen-ethylene-acetylene mix- 
tures [17] were experimentally analyzed in the annular combus- 
tion chamber and the velocity and pressure are found to be less 
than those of hydrogen fuel. 
Most of the previous research investigated the rotating deto- 
nation with gaseous fuels and relatively fewer studies focused on 
liquid fuel. Liquid hydrocarbon fuel is advantageous because of 
its easy storage, convenient application, and engine coolant ser- 
vices. From the point of view of engineering application, it is re- 
quired to carry out the research on liquid fuel RDE. Kindracki 
[18] applied experiments on the RDW of liquid kerosene and air 
mixtures with hydrogen addition and a detonation initiator with 
acetylene-oxygen mixtures were used to initiate the RDW. The ve- 
locity of RDW has a 20–25% reduction than the Chapman-Jouguet 
(C-J) value. Hayashi et al. [19] numerically studied the JP-10/air ro- 
tating detonation by the Eulerian-Eulerian method and they dis- 
cussed the effects of droplet diameter and pre-vaporization on the 
operability of RDE. The liquid hydrocarbon fuel, such as kerosene, 
has a higher density as well as speciﬁc heating values than the 
gaseous fuel. However, in combustors, the liquid fuel needs to be 
atomized for evaporation and then mixes with oxygen to form a 
reactive mixture. The two-phase reacting ﬂows and detonation in 
RDC with liquid fuel are expected to be more complex than those 
of gaseous fuel and the underlying physics need to be revealed 
since the knowledge regarding the initiation and stabilization of 
RDW formed in the two-phase mixture is still lacking. In partic- 
ular, the counterbalance between the evaporative cooling of fuel 
droplets and the heat release from the chemical reaction for the 
two-phase RDW is quite different from the RDW using gaseous 
fuel. 
Based on a ramjet engine, the rotating denotation of the two- 
phase kerosene-air mixture is numerically analyzed in the present 
study. The two-phase reacting ﬂow is modeled by the two-way 
coupling Eulerian-Lagrangian method. The effects of total pressure 
and total temperature for the combustor inlet are studied, consid- 
ering the variations of ﬂight Mach numbers and ﬂight altitudes. 
The remainder of this paper is organized as follows. The govern- 
ing equations and numerical methods are introduced in Section 2 . 
The main results are presented in Sections 3 –5 , including the self- 
sustained propagation and extinction of RDW. Finally, concluding 
remarks and discussions are drawn in Section 6 . 
2. Numerical formulation 
2.1. Governing equations and numerical methods 
In this study, the two-dimensional Navier-Stokes equations, in- 
cluding the transport equations of six species (C 10 H 20 , O 2 , CO 2 , CO, 
H 2 O, N 2 ), are solved, and the state equation for an ideal gas with 
multi-species is used to close the gas-phase equations. The equa- 
tions for evaporating fuel droplets are solved individually in a La- 
grangian manner. The coupling between the gaseous and dispersed 
droplets phases is calculated using the classical point-source in cell 
(PSIC) method [20] . The equations for gas-phase, droplet-phase and 
the inter-phase coupling terms are as follows, 
gas − phase equations 
⎧ 
⎪ ⎪ ⎪ ⎪ ⎪ ⎪ ⎪ ⎪ ⎨ 
⎪ ⎪ ⎪ ⎪ ⎪ ⎪ ⎪ ⎪ ⎩ 
∂ 
∂t 
(ρ) + 
∂ 
∂ x j 
(ρu j 
)
= S m 
∂ 
∂t 
( ρu i ) + 
∂ 
∂ x j 
(ρu i u j + P δij − τij 
)
= S F , i 
∂ 
∂t 
( ρe t ) + 
∂ 
∂ x j 
(
( ρe t + P ) u j − u i τij − q j 
)
= S Q 
∂ 
∂t 
( ρY k ) + 
∂ 
∂ x j 
(ρY k u j 
)
+ 
∂ 
∂ x j 
(ρY k 
(
V k, j + V c 
j 
))
= S combustion ,k + S Y k 
(1) 
droplet − phase equations 
⎧ 
⎪ ⎪ ⎪ ⎪ ⎪ ⎪ ⎪ ⎨ 
⎪ ⎪ ⎪ ⎪ ⎪ ⎪ ⎪ ⎩ 
d x d ,i 
d t = u d ,i 
d u d ,i 
d t 
= 
F d , i 
m d 
= 
F sg , i + F qs , i + F am , i + F vu , i 
m d 
d T d 
d t 
= 
Q d + ˙ m d L V 
m d c L 
= 
(
f Q ( Re d ) 
τa 
) ( Nu 
3 Pr 
)( c p 
c L 
)
( T @d − T d ) + 
(
˙ m d 
m d 
)
L V 
c L 
d m d 
d t 
= ˙ m d = − m d 
( 1 
τa 
)(
Sh 
3Sc 
)
In ( 1 + B M ) 
(2) 
inter − phase coupling terms 
2

<!-- PDF_PAGE: 3 -->

Z. Ren and L. Zheng Combustion and Flame 231 (2021) 1114 8 4 
⎧ 
⎪ ⎪ ⎪ ⎪ ⎪ ⎪ ⎪ ⎪ ⎪ ⎪ ⎨ 
⎪ ⎪ ⎪ ⎪ ⎪ ⎪ ⎪ ⎪ ⎪ ⎪ ⎩ 
S m = − 1 
/Delta1V 
∑ 
N c 
( ˙ m d ) 
S F , i = − 1 
/Delta1V 
∑ 
N c 
(
F d , i + ˙ m d u d , i 
)
S Q = − 1 
/Delta1V 
∑ 
N c 
(
Q d + ˙ m d ( 
u d ,i u d ,i 
2 
+ h V , sf ) 
)
S Y k = 
{ 
− 1 
/Delta1V 
∑ 
N c 
( ˙ m d ) for fuel 
0 for other species 
(3) 
ρ, u i , P, T are the density, velocity, pressure, and temperature of the 
gas mixture, respectively. In this paper, pressure refers to the static 
pressure and static temperature. The total pressure and total tem- 
perature will be pointed out. Y k is the mass fraction of the species 
k. R is the universal gas constant. The assumption of the Fourier 
heat conduction and Fickian mass diffusion is utilized to consider 
the molecular contributions in the viscous terms. The Soret and 
Dufour effects are neglected. δij is the Kronecker delta function and 
τij is the Newtonian viscous stress tensor, 
τij = 2 μ
(
S ij − S ii δij 
3 
)
(4) 
S ij = 
1 
2 
( ∂ u i 
∂ x j 
+ 
∂ u j 
∂ x i 
)
(5) 
S ij is the strain tensor. μ is the shear viscosity. V k is the diffusion 
velocity of the species k and is approximated by, 
V k X k = − D k ∇ X k (6) 
A correction velocity V c j is added in the species transport 
equations to ensure global mass conservation, 
V c 
j = 
N S ∑ 
k =1 
D k 
W k 
W 
∂ X k 
∂ x i 
(7) 
N S is the total number of species. D k and W k are the molecule 
weight and the mass diffusion coeﬃcient of the k th species. e t is 
the total energy, i.e., kinetic energy and internal (containing chem- 
ical) energy, which is deﬁned as, 
e t = 
N S ∑ 
k =1 
Y k 
( ∫ T 
T ref 
c p,k d T + h 0 
f,k 
)
− P 
ρ + 
u i u i 
2 
(8) 
where c p , k is the speciﬁc heat capacity at constant pressure, and 
h 0 f,k is the speciﬁc chemical formation enthalpy at the reference 
temperature, T ref . The heat ﬂux q j is, 
q j = λ∂T 
∂ x j 
−
N S ∑ 
k =1 
ρh k Y k V k, j (9) 
where λis the thermal conductivity of the gas mixture. The ther- 
modynamic properties of gas-phase are computed from the ﬁfth- 
order polynomials [21] . The transport properties including the vis- 
cosity, μk , the heat conductivity, λk , and the binary diffusion co- 
eﬃcient, D k , of each chemical species are obtained based on the 
kinetic theory [22] . In particular, the heat conductivity of each 
species is calculated by using the modiﬁed Eucken model. The dy- 
namic viscosity and the binary diffusion coeﬃcient are computed 
according to the Chapman-Enskog theory, and the semi-empirical 
expressions proposed by Wake and Wassiljewa are used to calcu- 
late the dynamic viscosity and heat conductivity of the mixture. 
The source terms, S m , S F, i and S Q , describe the two-way cou- 
plings of mass, momentum, and energy, respectively. S combustion, k is 
the source term from combustion. The droplet-phase is described 
by a large quality of discrete computational parcels that represent 
droplets dispersed in the background ﬂows. The spray of droplets 
is assumed to be sparsely dispersed. Droplet collision and dense 
particle effects are neglected as the mass loading of droplet-phase 
is small. An inﬁnite heat conduction coeﬃcient is assumed and the 
inner temperature distribution of each droplet remains uniform. 
The overall force on the droplet due to ﬂuid-droplet coupling is de- 
noted by F d, i , while the overall convective heat transfer between 
the ﬂuid and droplets is denoted by Q d . For the two-phase det- 
onation, the droplets could interact with the shock or detonation 
waves, and the unsteady forces on the droplet should be consid- 
ered [23] . F sg, i , F qs, i , F am, i , and F vu, i represent the stress-gradient, 
quasi-steady, added-mass, and viscous-unsteady forces. The quasi- 
steady force, F qs, i , is as, 
F qs ,i = m d 
(
f F ( Re d , M d ) 
t a 
) (
u i @d − u d ,i 
)
(10) 
In the quasi-steady force formulation, the correction function 
that accounts for the effect of droplet Reynolds number and 
droplet relative Mach number is denoted by f F (Re d , M d ), and em- 
pirical correlations of this correction function are given in Ref. [24] . 
The droplet Reynolds number, Re d , is deﬁned based on the rel- 
ative velocity between the ﬂuid and the droplet as Re d = | u i @d 
– u d, i | d d / ν and the droplet relative Mach number is M d = | u i @d 
– u d, i |/ a @d . u i @d and T @d are the velocity and temperature of the 
gas seen by the droplet at its position. c p is the speciﬁc heat of 
the mixture gas and c L is the speciﬁc heat of the liquid. τa is the 
droplet acceleration time. f Q (Re d ) is the corrections of heat trans- 
fer for an evaporating droplet. The non-equilibrium effect on the 
droplet evaporation is considered via the Langmuir-Knudsen evap- 
oration law [25] . The evaporation rate is controlled by the mass 
transfer number, B M = ( Y sf − Y V )/(1 − Y sf ). Here Y V is the mass frac- 
tion of vapor on the far-ﬁeld condition for the droplets and Y sf is 
the vapor surface mass fraction calculated from the surface molar 
fraction. 
The reaction of kerosene and oxygen is selected as a two-step 
reduced scheme considering the computational costs, which can 
predict the reaction rate, adiabatic ﬂame temperature, CO levels at 
equilibrium, and ignition delay for a wide range of pressure [26] , 
as follows, 
KERO + 10 O 2 ⇒  10 CO + 10 H 2 O (11a) 
CO + 0 . 5 O 2 ⇔  C O 2 (11b) 
Here KERO is short for kerosene. Eq. (11a) is the kerosene oxi- 
dation and Eq. (11b) is the CO –CO 2 equilibrium reaction. The for- 
ward reaction rates for reactions (12a) and (12b) are written as, 
k 1 = A 1 f 1 (φ) exp (− E 1 /RT ) [ KERO ] n KERO [ O 2 ] n O 2 , 1 (12a) 
k 2 = A 2 f 2 (φ) exp (− E 2 /RT ) [ CO ] n CO [ O 2 ] n O 2 , 2 (12b) 
where A i is the pre-exponential factor, E i is the activation energy of 
reaction i and n j , i is the reaction exponent for species j in reaction 
i . The subscripts 1 and 2 denote the two reactions of Eqs. (11a) and 
( 11b ), respectively. f 1 and f 2 are the correction functions based on 
the equivalence ratio φ. The detailed descriptions are given in Ref. 
[26] . 
The governing equations of the multi-phase reacting ﬂow are 
solved by utilizing our in-house codes, which have been previously 
applied to study a variety of compressible reacting ﬂow and deto- 
nation problems [27 , 28] . The adaptive central-upwind sixth-order 
weighted essentially non-oscillatory (WENO –CU6) scheme [29] is 
applied for the convection terms. This scheme ensures that the 
simulations for the main ﬂow with a low dissipation and achieves 
a proper resolution of the ﬂow properties around the shock and 
detonation waves. A sixth-order symmetric compact difference 
scheme is applied for the viscous diffusion terms. Time-integration 
3

<!-- PDF_PAGE: 4 -->

Z. Ren and L. Zheng Combustion and Flame 231 (2021) 1114 8 4 
Fig. 1. Schematic of rotating detonation formed in two-phase mixture. 
is realized by the explicit third-order Runge-Kutta method. In gas- 
to-droplet coupling, the physical quantities of the gas for a speciﬁc 
droplet is obtained by using a fourth-order Lagrangian polynomial 
interpolation method from the Eulerian velocity ﬁeld. A third-order 
Adams-Bashforth time integration is used to obtain the position, 
velocity, and temperature of the droplet. 
2.2. Computational set-up 
Two-dimensional numerical simulation for the two-phase rotat- 
ing detonation is applied, as shown in Fig. 1 . Previous studies have 
shown that the essential characteristics of RDW are not obvious 
between two-dimensional and three-dimensional simulations [19] . 
The three-dimensional annular combustion chamber is unwrapped 
into two dimensions and the computation domain is scaled by the 
dashed lines in Fig. 1 . In particular, the streamwise length of the 
domain from left to right is L x and the transverse length from up 
to down is L y . For the present study, L x equals 0.04 m and L y is 
0.06 m. For the upper and lower boundaries, the periodic boundary 
condition is utilized. The mixture of dispersed droplets, depicted 
by the black dots, and air is injected from the left boundary, which 
is assumed to include many micro nozzles and the inlet velocity is 
calculated from the local pressure, as proposed by Fievisohn et al. 
[30] . The nozzle area ratio from the throat to the exit is set as 1/3. 
For the outlet conditions at the right boundary in Fig. 1 , the gas 
pressure is extrapolated from the values inside the computational 
domain as the gas velocity is supersonic, and the outlet pressure is 
set as the ambient pressure when the gas velocity is subsonic. The 
other parameters are interpolated by assuming ﬁrst-order deriva- 
tives. The initiation of detonation should be properly set to achieve 
the one-way propagation of rotating detonation wave, and the ini- 
tiation method in the present study is the same with that in Ref. 
[31] . 
For the inﬂow conditions of an air-breathing aircraft with a 
ﬂight altitude of 25 km and a ﬂight Mach number of 4.5, the re- 
sulting total pressure, P 0 , for the inﬂow air of combustion chamber 
is 7 atm and the total temperature, T 0 , is 10 0 0 K. The liquid fuel 
is considered as pre-atomized. Therefore, for the laden droplets, 
the initial droplet velocity is identical to the velocity of the lo- 
cal carrier gas, and the initial droplet temperature is T d = 298 K. 
The density of droplets is 642 kg m −3 and the initial droplet size 
is uniform with an initial diameter of 2 μm. The main physi- 
cal and chemical characteristics of a kerosene droplet can be re- 
ferred to in Ref. [32] . The droplets are considered without any 
further breakup processes since the Weber number based on the 
slip velocity (for the initial velocity between two phases equal- 
ing zero) is small. The spray equivalence ratio, /Phi1s , is represented 
Table 1 
Summary of inﬂow parameters for Case RD. 
Gas-phase 
Total pressure, P 0 (atm) 
7 
Total temperature, T 0 (K) 
10 0 0 
Droplet-phase Diameter, d d (μm) 
2 
Temperature, T d (K) 
298 
Table 2 
Simulation cases for the effects of total pressure. 
Case # RDP1 RDP2 RDP3 
Total pressure, P 0 (atm) 3 5 9 
Table 3 
Simulation cases for the effects of total temperature. 
Case # RDT1 RDT2 RDT3 
Total temperature, T 0 (K) 900 1100 1200 
by /Phi1s · ( F / O ) st = ˙ m fuel / ( ˙ m air Y O 2 ) . (F/O) st is the stoichiometric fuel- 
to-oxidizer ratio and equals to 3.42. ˙ m fuel and ˙ m air are the mass 
ﬂow rates of fuel and air from the incoming ﬂow, respectively. Y O 2 
( = 0.23) is the mass fraction of the oxygen in the air. The spray 
equivalence ratio for the base case, Case RD, is /Phi1s = 1.0. The in- 
ﬂow parameters are listed in Table 1 . 
The RDWs formed in the stoichiometric mixture of fuel vapors 
and air are simulated to make a comparison, named as Case R. In 
addition, the Case RD0.5 with the pre-evaporation factor β = 50% 
is applied. The β is deﬁned as, 
β= 
˙ m vapor 
˙ m vapor + ˙ m droplet 
(13) 
where ˙ m vapor and ˙ m droplet are the mass ﬂow rates of fuel vapors 
and fuel droplets at the inlet of the combustion chamber, respec- 
tively. The total pressure and total temperature of Case R and Case 
RD0.5 are the same as those of Case RD. 
The aircraft will change its altitude during the ﬂight and the 
total pressure for the combustor inlet will be varied accordingly. 
It is important and necessary to analyze the effects of total pres- 
sure on the stable operation of two-phase rotating detonation. In 
the present research, the total pressure increases from 3 atm to 9 
atm, corresponding to the ﬂight altitudes decreasing from 30 km 
to 20 km, and Table 2 summarizes the simulation cases. The other 
inﬂow parameters are kept the same with those of Case RD. The 
variation of total pressure is expected to inﬂuence chemical re- 
action as well as droplet evaporation, and the effects on the sta- 
bility of two-phase RDW will be discussed in the following part. 
A series of simulations for the rotating detonation formed in the 
gaseous fuel-air mixture is applied for the comparison study. The 
total pressure for cases RP1, RP2, and RP3 are 3, 5, and 9 atm, re- 
spectively. Other inﬂow parameters are kept the same as those of 
Case RD. 
The aircraft will also alter its speed during the ﬂight and the 
total temperature of the combustor inlet will be changed accord- 
ingly. It is then important to discuss the inﬂuence of total temper- 
ature on the two-phase rotating detonation. In the present study, 
the total temperature increases from 900 K to 1200 K, which cor- 
responds to the ﬂight Mach numbers from 4.0 to 5.0, and Table 3 
summarizes the simulation cases. The other inﬂow parameters are 
kept the same with those of Case RD. The variation of total temper- 
ature is expected to inﬂuence chemical reaction as well as droplet 
evaporation, and the effects on the stability of two-phase rotating 
detonation are discussed in the following part. A series of numer- 
ical simulations for the rotating detonation formed in the gaseous 
fuel-air mixture is applied for the comparison study. The total tem- 
perature, T 0 , of the premixing ﬂow for cases RT1, RT2, and RT3 are 
4

<!-- PDF_PAGE: 5 -->

Z. Ren and L. Zheng Combustion and Flame 231 (2021) 1114 8 4 
Fig. 2. The results of the Sod’s shock tube problems: (a) density and (b) pressure. 
90 0, 110 0, and 120 0 K, respectively. Other inﬂow parameters are 
kept the same as those of Case RD. 
2.3. Model validation 
Since the experiments for the rotating detonation formed in 
multi-phase ﬂows have rarely been reported, we attempted to val- 
idate our numerical procedures based on the available experimen- 
tal data. The computation ability for compressible ﬂow has been 
achieved through the comparison with the experiments of the 
compressible shear layer [27] and the results are in good agree- 
ment with the experimental measurements. The validations for the 
shock-capturing scheme, droplet evaporation model, and chemical 
scheme are applied. The resolution study for the computational 
grids is analyzed. 
2.3.1. Shock-capturing scheme 
The calculation of Sod’s shock tube problems [33] is applied to 
validate the computation ability of complex waves and expansion 
waves for the rotating detonation. The initial conditions and the 
associated distributions of parameters are, 
(ρ, u, p) = 
{
(1 , 0 , 1) , 0 ≤ x < 0 . 5 
(0 . 125 , 0 , 0 . 1) , 0 . 5 ≤ x ≤ 1 
(14) 
As shown in Fig. 2 , the numerical results are in good agree- 
ment with the analytical result. In particular, it is found that the 
two curves from the present calculation and exact solution almost 
overlap and there is no oscillation of pressure and density around 
the shock discontinuity. 
2.3.2. Droplet evaporation model 
For the droplet evaporation in the sparse spray, and the evap- 
oration of a single droplet is slightly affected by the surrounding 
droplets. The numerical simulation is applied for the experiments 
[34] . As shown in Fig. 3 , the numerical predictions of the squared 
droplet diameter, d 2 , monotonously decrease with increasing time, 
and the predictions are found to be in good agreement with the 
experimental measurements. The comparisons between numerical 
simulations and experiments show that the non-equilibrium evap- 
oration model used in the present study can reproduce the tempo- 
ral evolution of the squared droplet diameter. 
2.3.3. Chemical scheme 
A two-step reaction model for the chemical reaction of 
kerosene gas and oxygen in high ambient temperature is used. This 
model is suitable for a wide range of ambient pressure from 1.0 to 
12.0 atm, which can be used for the present pressure in this pa- 
per. The one-dimensional numerical simulation is then used to val- 
idate the chemical scheme for detonation features of the kerosene- 
air mixture. The propagations of the detonation wave, U D , under 
different equivalent ratios are calculated. The initial pressure is 
Fig. 3. Temporal evolution of the squared droplet diameter between numerical sim- 
ulations and experiments. 
Fig. 4. Comparison of the detonation velocity, U D , predicted by numerical simula- 
tions and experiments. 
0.1 MPa and the initial temperature is 373 K. The velocity of the 
detonation wave is compared with the results from STANJAN code 
[35] and the experiment [36] , as shown in Fig. 4 . The wave veloc- 
ity calculated by the present in-house code with the two-step reac- 
tion scheme is in good agreement with that calculated by STANJAN 
code. Although the experimental measurement has a wide uncer- 
tainty, the numerical and experimental results also show good con- 
sistency. Therefore, we can obtain a reasonable detonation wave by 
utilizing the present chemical scheme. 
The chemical reaction rate and sensitivity are important to the 
numerical simulation of the detonation problem. Therefore, the cell 
sizes of the mixture of kerosene vapor and air with different equiv- 
alence ratios are predicted based on the two-dimensional deto- 
nation simulation to compare with the experiment data. Accord- 
ing to the experiment conducted by Austin and Shepherd [37] , the 
initial pressure of the kerosene/air mixture is 1 atm and the ini- 
tial temperature is 353 K. The range of the equivalence ratio is 
5

<!-- PDF_PAGE: 6 -->

Z. Ren and L. Zheng Combustion and Flame 231 (2021) 1114 8 4 
Fig. 5. Comparison of cell size measurements of kerosene/air detonation between 
the present numerical results and the experimental data. 
from 0.7 to 1.4. Figure 5 shows a comparison between the nu- 
merical results of the detonation cell size and the experimen- 
tal results [37] under different equivalence ratios. It can be seen 
that the two results are relatively consistent. However, the chem- 
ical reaction rate cannot be well predicted by the two-step re- 
duced reaction model, and the cell size obtained from the nu- 
merical simulation has a certain deviation with the experimental 
measurement. 
2.3.4. Grid-independence study 
The grid scale should be carefully designed to satisfy the re- 
quirements from both the resolution of detonation waves and 
the particle-in-cell model describing point-mass droplets. First, the 
grid size should be small enough for capturing the physics of RDW. 
The mesh scales are varied for the grid independence study for the 
simulation of RDW formed in a stoichiometric mixture of kerosene 
vapor and air. Three sets of computational meshes are applied for 
the initial conditions of Case R, and the grid sizes, /Delta1, are chosen as 
20 0, 10 0, and 50 μm, respectively. The transverse distributions of 
pressure and temperature crossing the RDW are plotted in Fig. 6 . 
The pressure and temperature from different grid scales are found 
to be almost overlapped together except for the coarsest one of 
/Delta1= 200 μm. Therefore, the mesh size is ﬁnally taken as 50 μm 
and the grid independence is achieved, which guarantees reliabil- 
ity. In addition, the grid spacing has to be large enough for the 
point-source assumption to be valid and the grid size has to be 10 
times larger than the droplet size to get correct droplet dynam- 
ics, and the computation mesh ( /Delta1= 50 μm) is suitable or the fuel 
droplet ( d d = 2 μm). 
Figure 7 shows the local enlargements of the numerical 
schlieren around the rotating detonation waves with the grid sizes 
decreasing from 20 0 μm, 10 0 μm to 50 μm. It is found that all the 
computational grids can predict the basic wave structures of rotat- 
ing detonation, such as detonation front, oblique shock wave, and 
slip line. The front of the detonation wave is smooth without cel- 
lular structures. 
Furthermore, the grid-independence study is applied for Case 
RP3 with the total pressure P 0 = 9 atm and total temperature 
T 0 = 10 0 0 K. The three computation grids, /Delta1, increase from 50 μm, 
100 μm to 200 μm. It is observed that the three chosen grids can 
capture the wave structures, as depicted in Fig. 8 . With the in- 
crease of the total pressure, the detonation front of RDW is found 
to be smooth. In addition, the minimum cell size of the kerosene- 
air detonation is less than 50 mm [19] and the 50 μm grid applied 
in the present study is small enough (around 10 0 0 grids per cell). 
Based on the above model validation and resolution study, the 
Eulerian-Lagrangian approach is further applied to mimic the ro- 
tating detonation of evaporating fuel droplets in the compressible 
ﬂows. 
3. Basic features of two-phase RDW 
The rotating detonation formed in a stoichiometric kerosene- 
air mixture, namely Case RD, is analyzed at ﬁrst and the instan- 
taneous distributions of temperature, pressure, fuel mass fraction, 
and droplets are shown in Fig. 9 . The stable self-sustained prop- 
agation of the detonation wave is achieved after several rotation 
cycles. As shown in Fig. 9 (a), RDW refers to the rotating detona- 
tion wave, which propagates from the bottom to the top in the 
domain and OSW is the oblique shock wave. The slip line sepa- 
rates the fresh products from the detonation and the former com- 
bustion products. The shearing vortices are formed along the slip 
line due to the velocity difference of the combustion products. The 
main features of the ﬂow and wave structure are consistent with 
previous results of gaseous rotating detonation. However, for the 
two-phase rotating detonation, it is found that there is another 
slip line close to the boundary which separates the fresh unreacted 
mixture and combustion products. This is because that another ro- 
tating detonation wave, named RDW-2, with a decreased height of 
detonation front is formed near the inlet, as shown in Fig. 9 (b). The 
second oblique shock wave, referred to OSW-2, is also observed. 
The RDW is bifurcated into two detonation waves in the two-phase 
ﬂow and the bifurcated wave structure with two detonation fronts 
leads to a more complicated ﬂow ﬁeld. In particular, the upstream 
RDW is found to be curved near the inlet with decreased pressure. 
This is due to the interaction between evaporating droplets and 
chemical reactions, which will be discussed later. From the distri- 
bution of fuel mass fraction, it can be observed that there are un- 
reactive pockets in the downstream region from RDW-2, which ad- 
vect downstream associated with the shear vortices. From Fig. 9 (d) 
it is found that the fuel spray completes the evaporation quickly as 
they are injected into the airﬂow with high temperature, but the 
penetration length along the transverse direction is non-uniform, 
which is mainly due to the spatial distribution of temperature and 
Fig. 6. Transverse distributions of pressure (a) and temperature (b) with different grid sizes for the initial conditions of Case R. 
6

<!-- PDF_PAGE: 7 -->

Z. Ren and L. Zheng Combustion and Flame 231 (2021) 1114 8 4 
Fig. 7. Local enlargements of the numerical schlieren with different grid resolutions for Case R: (a) /Delta1= 50 μm, (b) /Delta1= 100 μm and (c) /Delta1= 200 μm. 
Fig. 8. Local enlargements of the numerical schlieren with different grid resolutions for Case RP3: (a) /Delta1= 50 μm, (b) /Delta1= 100 μm and (c) /Delta1= 200 μm. 
Fig. 9. Instantaneous distributions of (a) temperature (K), (b) pressure (atm), (c) fuel mass fraction and (d) dispersed fuel droplets with diameters (μm) for Case RD. 
pressure from rotating detonation as well as the non-uniform local 
injection velocity. 
The local enlargements of the bifurcated wave structure near 
the inlet are shown in Fig. 10 . Figure 10 (a) gives the distributions 
of dispersed droplets with the pressure iso-lines to indicate the 
detonation fronts and Fig. 10 (b) shows the local temperature 
contours. A λshape wave structure occurs around the inlet, which 
is bifurcated into RDW and RDW-2, and is found to be stable 
during the detonation propagation. In particular, the head of RDW 
near the inlet becomes a curved shock wave, referred to SW in 
Fig. 10 (b). This is due to the fact that the fuel droplets near the 
inlet cannot evaporate to form enough vapors for chemical reac- 
tion and the leading shock wave decouples with the post-shock 
ﬂame, as shown in Fig. 10 (b). The corrugation of the post-shock 
ﬂame is attributed to the inhomogeneous fuel concentration. As 
the RDW propagates upward and traverses the droplet cluster, 
7

<!-- PDF_PAGE: 8 -->

Z. Ren and L. Zheng Combustion and Flame 231 (2021) 1114 8 4 
Fig. 10. Enlarged snapshots of (a) dispersed fuel droplets with diameters (μm) and (b) temperature (K) around the bifurcated RDW for Case RD. 
Fig. 11. Transverse proﬁles of (a) pressure (solid line) and temperature (dashed line), and (b) mass fractions of fuel (solid line) and oxygen (dashed line) along x = 0.5 mm 
for Case RD. 
it is observed that the penetration length of droplets decreases 
due to the acceleration of evaporation in the post-RDW ﬂow with 
higher temperatures. Although the fuel injection is uniform, the 
spatial segregation of droplets becomes inhomogeneous, which 
is attributed to the velocity variation after the RDW. The heating 
from the curved SW promotes the droplet evaporation and results 
in more fuel vapors to form reactive mixtures. The second rotating 
detonation wave, RDW-2, is formed in the downstream region. The 
detonation front of RDW-2 is along the streamwise direction but 
the height is much shorter than that of RDW due to the lack of 
fuel for the chemical reaction. 
In order to illustrate the detailed features of the bifurcated 
RDW, Figure 11 shows the transverse proﬁles of pressure, tem- 
perature, and mass fractions of fuel and oxygen, which cross the 
curved SW and RDW-2. The propagating SW from the right side 
compresses the incoming air and leads to the high-temperature of 
the post-shock ﬂow, as depicted in Fig. 11 (a). The distribution of 
fuel mass fraction, Y F , in Fig. 11 (b) demonstrates that the near- 
inlet part of the RDW is a non-reacting shock wave due to the 
lack of fuel vapors. The heating from the SW contributes to the 
droplet evaporation and it is found that the fuel mass fraction has 
a quick increase in the downstream region from the SW. In partic- 
ular, the temperature, T , decreases as the Y F increases and it is be- 
cause of the evaporative cooling. In the further downstream area, a 
strong detonation wave, RDW-2, is formed in the fuel-lean reactive 
mixture, associated with the coupling of pressure and temperature 
peaks. Then the mass fractions of fuel and oxygen have a sudden 
reduction due to the fast reaction rate of detonation. 
The distributions of the pressure and temperature across the bi- 
furcated RDW are compared with the curves of the fuel mass frac- 
tion, as shown in Fig. 12 . The propagation direction of the waves 
is from the left to right. As the curved SW traverses the droplets 
curtain injected from the inlet, the fuel mass fraction increases 
quickly due to the heating of the shock wave and there is a pre- 
evaporation (PreEvap) zone between the leading shock wave and 
the RDW-2, as scaled in Fig. 12 (b). When the Y F increases to the 
maximum, the RDW-2 is formed and results in a sudden decrease 
of the Y F . The chemical reaction (React) regime follows the PreEvap 
region. 
As the bifurcated RDW propagates downstream, the instanta- 
neous distributions of pressure are shown in Fig. 13 (a). It is found 
that the bifurcated wave structure is stable during wave propaga- 
tion. Fig. 13 (b) and (c) show the transverse distributions of pres- 
sure, temperature, and fuel mass fraction across the waves. The 
heating from the leading shock wave, SW, on the local ﬂow con- 
tributes to the evaporation of the fuel droplets, associated with the 
fast increases of Y F . The second rotating detonation wave, RDW- 
2, is formed downstream and it consumes the reactive mixtures 
rapidly. 
The bifurcated wave structure of two-phase rotating detonation 
is attributed to the complex interaction among shock waves, evap- 
orating droplets, and chemical reaction. Figure 14 qualitatively de- 
picts the effects of droplets on the rotating detonation. The grey 
dots represent the fuel droplets. The blue lines refer to the shock 
wave, SW, and the red lines are for the detonation wave, DW. 
Generally, there are four regimes for the wave structure of two- 
phase RDW. Regime 1 contains a fresh mixture of evaporating fuel 
droplets and air. The detonation wave cannot be formed in regime 
1. It is because of the local insuﬃcient reactive mixture due to the 
ﬁnite droplet evaporation rates for exothermic reaction and then 
the local SW decouples with the ﬂame. The pre-heating of SW on 
droplets occurs in Regime 2 and accelerates the evaporation, which 
results in the formation of the reactive mixtures for detonation. Fi- 
nally, a second DW is formed in the downstream region, namely 
8

<!-- PDF_PAGE: 9 -->

Z. Ren and L. Zheng Combustion and Flame 231 (2021) 1114 8 4 
Fig. 12. Transverse proﬁles of (a) pressure (solid line) and fuel mass fraction (dashed line), and (b) temperature (solid line) and fuel mass fraction (dashed line) along 
x = 0.5 mm for Case RD. 
Fig. 13. Instantaneous distributions of pressure (atm) for Case RD (a). Transverse proﬁles of (b) pressure (solid line) and fuel mass fraction (dashed line), and (c) temperature 
(solid line) and fuel mass fraction (dashed line) along x = 0.5 mm. 
Fig. 14. Schematic diagram of the bifurcated wave structure. 
regime 3. In regime 4, the main detonation wave generates due 
to the completion of droplets and the associated suﬃcient fuel-air 
mixtures for the chemical reaction. 
To further analyze the inﬂuence of the droplet evaporation on 
the RDWs, Case R using pre-evaporated fuel vapors and Case RD0.5 
with a mixture of droplets and vapors are applied. The instanta- 
neous pressure distributions for Case R are shown in Fig. 15 (a). It 
is found that the RDW displays a single wave with a smooth front, 
which is different from the two-phase rotating detonation with the 
bifurcated wave structure. The fuel for Case RD0.5 is a mixture of 
droplets and vapors, and the pre-evaporation factor, β, equals 50%. 
Figure 15 (b) and (c) provide the distributions of temperature and 
pressure for Case RD0.5. As the droplets are injected from the inlet, 
it is observed that the front of the RDW tends to be unstable with 
the ﬁne cellular wave structures. The temperature distribution of 
the combustion products becomes inhomogeneous due to the non- 
uniform chemical reaction intensity on the detonation front. 
The variations of the pressure at two observation points 
( x = 2 mm, y = 50 mm) and ( x = 5 mm, y = 50 mm) near the in- 
let are shown in Figs. 16 (a) and 17 (a). From the pressure signals, it 
is observed that the pressure peak of the RDW formed in the two- 
phase mixtures is higher than that of the gaseous RDW, but the 
peak values ﬂuctuate with time, indicating a more unstable propa- 
gation feature. The pressure peak indicates the current position of 
the detonation front, and the propagation velocity of the RDW is 
calculated by using the time interval between two neighbor deto- 
nation waves, as shown in Figs. 16 (b) and 17 (b). The C-J velocity of 
detonation using the ambient conditions of the present simulation 
is calculated as 1.9 km/s. It is found that the propagation veloc- 
ity of the gaseous RDW is higher than that of the two-phase RDW, 
and it is mainly due to the fact that for two-phase detonation the 
droplets need to evaporate to form fuel vapors for the chemical 
reaction. The decrease of pre-evaporation factor from Case RD0.5 
to Case RD results in the decrease of the detonation velocity since 
fewer droplets are pre-evaporated to form reactive mixtures for the 
exothermic reaction. The pressure peaks recorded at x = 5 mm and 
y = 50 mm are found to be slightly lower than those observed at 
x = 2 mm and y = 50 mm, which is closer to the inlet. 
4. Effects of total pressure 
The RDWs formed in the gaseous mixture of fuel vapors and air 
are simulated at ﬁrst and the results are shown in Fig. 18 . The to- 
tal pressure increases from 3 atm to 9 atm. It is found that a single 
9

<!-- PDF_PAGE: 10 -->

Z. Ren and L. Zheng Combustion and Flame 231 (2021) 1114 8 4 
Fig. 15. Instantaneous distributions of pressure (atm) for Case R (a). Instantaneous distributions of (b) temperature (K) and (c) pressure (atm) for Case RD0.5. 
Fig. 16. Variation of pressure (a) and propagation velocity of the rotating detonation wave (b) at the observation point ( x = 2 mm, y = 50 mm) for Case RD, Case RD0.5 and 
Case R. 
Fig. 17. Variation of pressure (a) and propagation velocity of the rotating detonation wave (b) at the observation point ( x = 5 mm, y = 50 mm) for Case RD, Case RD0.5 and 
Case R. 
Fig. 18. Instantaneous distributions of pressure for (a) Case RP1, (b) Case RP2, and (c) Case RP3. 
10

<!-- PDF_PAGE: 11 -->

Z. Ren and L. Zheng Combustion and Flame 231 (2021) 1114 8 4 
Fig. 19. Variation of pressure at the observation point ( x = 2 mm, y = 50 mm) for the effects of total pressure: (a) ﬁve rotating circles and (b) local enlargement. 
Fig. 20. Variation of pressure (a) and propagation velocity of the rotating detonation wave (b) at the observation point ( x = 2 mm, y = 50 mm) for Case RD and Case RDP2. 
rotating detonation propagates in the combustion chamber and the 
wave pressure increases with the increasing total pressure. In par- 
ticular, for Case RP1 with low total pressure ( P 0 = 3 atm), the ro- 
tating detonation tends to be unstable with the ﬁne cellular wave 
structures on the detonation front. As P 0 increases, the detonation 
front becomes smooth and the cellular structures disappear, indi- 
cating a more stable RDW. 
The effects of total pressure on the propagation features of RDW 
are then analyzed. The variation of pressure at the observation 
point ( x = 2 mm, y = 50 mm) near the inlet is shown in Fig. 19 . 
As the total pressure, P 0 , increases from 3 atm to 9 atm, it is found 
that the stable rotating detonation is only formed for the medium 
P 0 equaling to 5 atm and 7 atm in the present study. For the low 
P 0 , the RDW in Case RDP1 is found to quench during the second 
rotating circle. For the high P 0 equaling to 9 atm, the pressure vari- 
ation for Case RDP3 indicates that the initial detonation wave can- 
not achieve the self-sustained propagation during the ﬁrst rotating 
circle. Although both the low and high total pressures result in the 
quenching of detonation, the mechanisms are different. In general, 
the decrease in pressure reduces the chemical reaction rate and 
results in the decoupling between the shock wave and post-shock 
ﬂame. The pressure increase suppresses the droplet evaporation 
and the RDW quenches due to the lack of reactive mixtures. The 
detailed analysis of the quenching mechanisms will be given in the 
following part by analyzing the quenching dynamics. The local en- 
largement of the pressure evolution in Fig. 19 (b) shows that there 
is a slight difference in the detonation velocity between the cases 
RDP2 and RD and the increasing P 0 from cases RDP2 to RD results 
in a much stronger detonation wave, associated with the fast heat 
release rates. 
For Case RDP2 with stable RDW, the pressure signals at the two 
observation points are shown in Figs. 20 (a) and 21 (a), respectively. 
The Case RD is used to make a comparison. With the decrease 
of total pressure from Case RD to Case RDP2, it is found that the 
pressure of the rotating detonation wave decreases, as seen by the 
decreasing pressure peaks. Figures 20 (b) and 21 (b) show that the 
propagation velocity of the RDW for Case RDP2 is slightly slower 
than that of Case RD. In addition, the RDW formed in the low- 
pressure ﬂow has a higher ﬂuctuation level of the detonation ve- 
locity. 
4.1. Self-sustained RDW 
Figure 22 shows the instantaneous distributions of the dis- 
persed fuel droplets with their diameters in colors. For Case RDP2 
with the stable RDW, it is found that the penetration length of fuel 
droplets has a non-uniform distribution along the transverse direc- 
tion, and the length becomes the shortest in the downstream re- 
gion from the RDW. For Case RDP1, the self-sustained propagating 
detonation wave is not formed and the penetration length has a 
uniform distribution. As the total pressure increases to 9 atm, the 
overall penetration length of droplets tends to be longer, as shown 
in Fig. 22 (c). This is because the increasing ambient pressure re- 
duces the evaporation rates. Generally, the increasing pressure ac- 
celerates the combustion rates, but for the two-phase reacting ﬂow 
this pressure increase impedes the liquid evaporation, and thus the 
lack of reactive mixture results in the quenching of rotating deto- 
nation. 
Among the three cases with various total pressure, the instan- 
taneous ﬂow ﬁelds of Case RDP2 with the stable rotating deto- 
nation are shown in Fig. 23 . The decrease of total pressure from 
Case RD to Case RDP2 is found to have a slight inﬂuence on the 
temperature of the detonation front and the combustion products, 
as shown in Fig. 23 (a). The distribution of fuel mass fraction dis- 
plays that the unreacted mixtures in the downstream region from 
RDW-2 in Case RD disappear under the low-pressure condition in 
Case RDP2. This is due to the fact that the decrease in pressure 
accelerates the local evaporation rates of droplets near the inlet 
and the detonation wave is formed with suﬃcient reactive mix- 
11

<!-- PDF_PAGE: 12 -->

Z. Ren and L. Zheng Combustion and Flame 231 (2021) 1114 8 4 
Fig. 21. Variation of pressure (a) and propagation velocity of the rotating detonation wave (b) at the observation point ( x = 5 mm, y = 50 mm) for Case RD and Case RDP2. 
Fig. 22. Instantaneous distributions of dispersed fuel droplets with diameters (μm) for (a) Case RDP1, (b) Case RDP2 and (c) RDP3. 
Fig. 23. Instantaneous distributions of (a) temperature (K), (b) pressure (atm) and (c) fuel mass fraction for Case RDP2. 
tures. From the pressure ﬁelds, it is found that the wave struc- 
ture of rotating detonation, which displays a single curved detona- 
tion front, is different from that in Case RD, and the detailed fea- 
ture will be discussed later. The pressure peak of detonation is re- 
duced due to the decrease in total pressure. In particular. the wave 
front of RDW tends to be corrugated with the unstable cellular ﬁne 
structures. 
Figure 24 shows the local enlargements near the inlet to illus- 
trate the wave structure of RDW for Case RDP2. The dashed lines 
in Fig. 24 (a) are the pressure iso-lines and refer to the detonation 
front. The unsteady transverse waves, referred to TW, are formed 
on the wave front. It is found that the distribution of fuel droplets 
becomes non-uniform as the RDW traverses the droplet curtain, 
and the penetration length is shortened, which are attributed to 
the variation in velocity and temperature of the carrier gas after 
the RDW. It is interesting to observe that the near-inlet wave struc- 
ture of RDW is changed from the bifurcated waves to a curved 
single wave as the ambient pressure decreases. However, local de- 
coupling of the shock and post-shock ﬂame occurs in the droplet 
curtain, as shown in Fig. 24 (b). From the distributions of pressure 
iso-lines in Fig. 24 (a), the detonation front is found to be broken 
down near the inlet. This is mainly attributed to the complex inter- 
action between the shock wave, droplet evaporation, and chemical 
reaction. 
12

<!-- PDF_PAGE: 13 -->

Z. Ren and L. Zheng Combustion and Flame 231 (2021) 1114 8 4 
Fig. 24. Enlarged snapshots of (a) dispersed fuel droplets with diameters (μm) and (b) temperature (K) around inlet for Case RDP2. 
Fig. 25. Temporal evolution of temperature distribution for Case RDP1. The time interval between two neighbor graphs is 6 μs. 
4.2. Quenching of RDW 
For either low-pressure or high-pressure conditions in the 
present investigation, the RDW cannot achieve the self-sustained 
propagation and the quenching occurs, as shown by the pressure 
signals in Fig. 19 (a). In general, the variation of ambient pressure 
not only affects the chemical reaction for heat release but also 
inﬂuences the droplet evaporation, which contributes to the for- 
mation of reactive mixtures. The following part will analyze the 
quenching phenomena of rotating detonation by detailing the dy- 
namic process. 
As the total pressure decreases to 3 atm, the temporal dis- 
tributions of temperature and pressure are given in Figs. 25 and 
26 , respectively. The typical RDW is formed by recognizing the 
detonation front separating the cold fresh reactive mixtures and 
the hot combustion products in Fig. 25 (a) as well as the front with 
unsteady transverse waves in Fig. 26 (a). The height of RDW is 
found to decrease continuously from Fig. 26 (a) to (d) and the slip 
line between the fresh unburnt gas and the detonated products 
tends to be curved, as shown in Fig 25 (b). In particular, the multi- 
wave point connecting the RDW and the OSW moves towards 
the inlet and the detonation front displays a concave to convex 
shape, as shown in Fig. 26 (c). It is found that the transverse waves 
propagate along the left direction and the right part of the deto- 
nation front tends to be smooth, as scaled by the red solid line in 
Fig. 26 (c). It indicates that there is an absence of transverse waves 
that are generated from the right edge of the detonation front. Fur- 
thermore, the transverse waves disappear on the detonation front 
and the RDW surface becomes completely smooth, as depicted in 
Fig. 26 (d). In addition, the wave pressure is reduced and the rotat- 
ing detonation tends to be weak. As the RDW propagates towards 
the fresh mixture, the detonation pressure decreases, and the 
wave surface is further convex towards the propagation direction, 
as shown in Fig. 26 (e).This is due to the absence of the transverse 
waves and associated their compression effects for accelerating 
the chemical reaction. From Fig. 26 (f) (i), the iso-lines of fuel mass 
fraction with Y F = 0.03 are scaled by the black dashed lines and 
are used to distinguish the unreacted mixture and the combustion 
products. It is found that the local quenching is generated around 
the multi-wave point, as shown in Fig. 25 (f), and the local shock 
wave decouples with the post-shock ﬂame, which leads to the un- 
reacted mixtures in the post-shock ﬂow ( Fig. 26 (f)). The decoupling 
regime on the detonation front expands further. The incoming new 
fresh reactive mixture can not be burnt and are found to traverse 
the detonation front, which weakens the rotating detonation in 
turn, as depicted by a large amount of unreacted mixture with 
a low temperature in Fig. 25 (g). The height of RDW decreases 
continuously and ﬁnally the detonation breaks down completely, 
which is seen from the distribution of pressure in Fig. 26 (i). 
The quenching of rotating detonation also occurs in the high- 
pressure ﬂow with total pressure P 0 = 9 atm (Case RDP3). 
Figures 27 and 28 provide the temporal proﬁles of temperature and 
pressure, respectively. As the initial detonation wave propagates to- 
wards the fresh reactive mixture, the droplets are injected from the 
inlet to evaporate. It is found that a low-temperature regime oc- 
curs in the post-RDW ﬂow, as scaled by the green dashed lines 
in Fig. 27 (b). This is mainly attributed to two facts, namely the 
weak heat release from exothermic reaction and the heat loss from 
droplet evaporation. The ﬁrst mechanism is due to the insuﬃcient 
reactive mixtures from the limited evaporation rates of droplets 
13

<!-- PDF_PAGE: 14 -->

Z. Ren and L. Zheng Combustion and Flame 231 (2021) 1114 8 4 
Fig. 26. Temporal evolution of pressure distribution for Case RDP1. The time interval between two neighbor graphs is 6 μs. The black dashed lines refer to the fuel mass 
fraction Y F = 0.03. 
Fig. 27. Temporal evolution of temperature distribution for Case RDP3. The time interval between two neighbor graphs is 6 μs. 
Fig. 28. Temporal evolution of pressure distribution for Case RDP3. The time interval between two neighbor graphs is 6 μs. 
in the high-pressure ﬂow. The second one is from the evapora- 
tive cooling that reduces the local gaseous temperature, which in 
turn suppresses the droplet evaporation. From the pressure distri- 
bution in Fig. 28 (b), the rotating detonation front is curved near 
the inlet and the wave strength becomes weak, associated with 
the decreasing propagating speed. The local quenching then oc- 
curs near the inlet and the leading shock wave decouples with 
the ﬂame, as shown by the green dashed lines in Fig. 27 (c). The 
low-temperature regime further expands due to the weak chemical 
reaction, which impedes the droplet evaporation to form reactive 
mixtures. The height of RDW is found to decrease continuously. Fi- 
nally, the detonation front disappears. In Fig. 28 (g) only a V-shaped 
curved shock wave exits in the ﬂow ﬁeld and the unreacted fuel- 
air mixtures with low temperature ﬁll in the combustion chamber, 
as shown in Fig. 27 (g) ( Fig. 29 ). 
The reason for the quenching of RDW is complex due to the in- 
teractions among compressible ﬂow, chemical reaction, and heat 
transfer, which also includes the droplet dynamics for the two- 
phase detonation. Considering the initial conditions in the present 
study, two mechanisms account for the quenching phenomena as 
the total pressure varies in the rotating detonation chamber. As the 
total pressure decreases, the detonation is not strong with the re- 
duction of chemical reaction rates. There are no transverse waves 
that are generated from the triple point and the transverse waves 
on the RDW surface disappear gradually, which further weakens 
the detonation front. The fresh mixtures are not consumed and 
14

<!-- PDF_PAGE: 15 -->

Z. Ren and L. Zheng Combustion and Flame 231 (2021) 1114 8 4 
Fig. 29. Instantaneous distributions of pressure for (a) Case RT1, (b) Case RT2, and (c) Case RT3. 
Fig. 30. Variation of pressure at the observation point for the effects of total temperature: (a) ﬁve rotating circles and (b) local enlargement. 
they traverse the RDW, which in turn suppresses the detonation. 
The local quenching initiates from the right edge of the detona- 
tion front and develops towards the inlet. Finally, the leading shock 
completely decouples with the ﬂame and the rotating detonation 
front breaks down. It is referred to a reaction-dominated quench- 
ing for the low-pressure ﬂow due to the absence of transverse 
waves from the suppression of chemical reaction. For the RDWs 
formed in the gaseous mixtures with the low total pressure, it is 
found that the rotating detonation is unstable with the ﬁne cel- 
lular structures on the detonation front, which is due to the low 
chemical reaction rate under the low-pressure conditions. As the 
total pressure increases, the gaseous rotating detonation becomes 
stable with a smooth detonation front. When the total pressure in- 
creases, the droplet evaporation rate decreases and the propagation 
of RDW cannot be sustained due to the lack of reactive mixtures 
for the exothermic reaction. The quenching initiates near the inlet 
where the droplets evaporate. The local cooling from the evapo- 
ration further weakens the chemical reaction and hence the deto- 
nation front. The shock and ﬂame decoupling regime develops to- 
wards the outlet and the detonation front disappears at last. For 
the inﬂow with high total pressure, the quenching is attributed 
to the limited evaporation rates of fuel droplets and is referred to 
evaporation-dominated quenching. 
5. Effects of total temperature 
The rotating detonation waves formed in the gaseous mixture 
of fuel vapors and air are simulated with the variation of the to- 
tal temperature. The gaseous reactive mixture is found to result 
in a single rotating detonation wave and the detonation front be- 
comes smooth with the increasing total temperature. In particular, 
for Case RT1 with T 0 = 900 K, the cellular wave structures appear 
on the detonation front. In addition, the wave pressure decreases 
with the increase of the total temperature, and the rotating deto- 
nation tends to be stable. 
The effects of total temperature on the propagation of RDW are 
studied by analyzing the variation of pressure at the observation 
point ( x = 2 mm, y = 50 mm), as shown in Fig. 30 . As the to- 
tal temperature increases from 900 K to 1200 K, it is found that 
the stable rotating detonation is only formed for the T 0 higher 
than 10 0 0 K. For the low total temperature, the RDW for Case 
RDT1 is found to quench during the ﬁrst rotating circle and the 
initial detonation wave cannot achieve the self-sustained propa- 
gation. It is because that the temperature decrease reduces not 
only the droplet evaporation rates but also the chemical reaction 
rates, which weaken the detonation and result in the decoupling 
of shock and ﬂame. The local enlargement of the pressure evolu- 
tion in Fig. 30 (b) shows that there is a slight difference in the det- 
onation velocity among the cases RD, RDT2, and RDT3. It is also 
observed that the increasing total temperature from cases RD to 
RDT3 results in the weaker detonation wave, as seen by the reduc- 
tion of the pressure peaks. 
The RDW achieves stable propagation for Case RDT2 and Case 
RDT3. The pressures at the two observation points are recorded 
in Figs. 31 (a) and 32 (a), respectively. The data of Case RD is used 
to make a comparison. With the decrease of the total tempera- 
ture from Case RDT3 to Case RD, it is found that the detonation 
pressure decreases, as shown by the decreasing pressure peaks. 
Figures 31 (b) and 32 (b) show that the effects of the total tempera- 
ture on the propagation velocity of RDW is unobvious. 
The reacting ﬂow ﬁelds with the variation of total tempera- 
ture, T 0 , are shown in Fig. 33 . From the temperature distribution, 
it is found that the increase of T 0 from cases RD to RDT3 results 
in the higher temperature of the combustion products after the 
15

<!-- PDF_PAGE: 16 -->

Z. Ren and L. Zheng Combustion and Flame 231 (2021) 1114 8 4 
Fig. 31. Variation of pressure (a) and propagation velocity of the rotating detonation wave (b) at the observation point ( x = 2 mm, y = 50 mm) for Case RD, Cased RDT2 
and Case RDT3. 
Fig. 32. Variation of pressure (a) and propagation velocity of the rotating detonation wave (b) at the observation point ( x = 5 mm, y = 50 mm) for Case RD, Cased RDT2 
and Case RDT3. 
Fig. 33. Instantaneous distributions of (a) temperature (K), (b) pressure (atm) and (c) fuel mass fraction for Case RDT2. Instantaneous distributions of (d) temperature (K), 
(e) pressure (atm) and (f) fuel mass fraction for Case RDT3. 
16

<!-- PDF_PAGE: 17 -->

Z. Ren and L. Zheng Combustion and Flame 231 (2021) 1114 8 4 
Fig. 34. Enlarged snapshots of temperature (K) around inlet for (a) Case RDT2 and (b) Case RDT3. Here, the black dashed lines refer to the pressure P = 11 atm to indicate 
the detonation fronts. 
Fig. 35. Temporal evolution of temperature distribution for Case RDT1. The time interval between two neighbor graphs is 6 μs. 
Fig. 36. Temporal evolution of pressure distribution for Case RDT1. The time interval between two neighbor graphs is 6 μs. 
RDW. The gas temperature along the slip line which separates the 
ﬂows after the oblique shock and the detonation wave is also in- 
creased. This is due to the complete combustion of the reactive 
mixtures in the high-temperature ﬂow, as seen by the disappear- 
ance of the unreacted fuel gas in the downstream region from the 
triple point in Fig. 33 (f). The effects on the wave structure of the 
two-phase rotating detonation are unapparent. From the distribu- 
tions of pressure, the λ-shaped bifurcated wave structure is found 
to be formed. Only the distance between the two detonation fronts 
becomes close with the increase of total temperature, and the det- 
onation front tends to be smooth by the comparison of Fig. 33 (b) 
and (e). It is mainly because that the increasing temperature pro- 
motes the droplet evaporation as well as the chemical reaction. 
The combustion is then completed in a shorter time (acceleration 
of chemical reaction) with more reactive mixtures (droplet evapo- 
ration), which results in the earlier formation of the second RDW. 
The local enlargements of the near-inlet wave structure for 
cases RDT2 and RDT3 are shown in Fig. 34 . With the increase 
of total temperature, it is found that the height of the curved 
shock wave, SW, decreases, and the initiation position of the 
RDW approaches to the inlet from Case RDT2 to Case RDT3. This 
is mainly due to the acceleration of droplet evaporation in the 
ﬂow with higher temperatures, and the shock wave couples with 
the ﬂame with enhanced chemical reaction. It is also observed 
17

<!-- PDF_PAGE: 18 -->

Z. Ren and L. Zheng Combustion and Flame 231 (2021) 1114 8 4 
that the height of the second rotating detonation wave, RDW-2, 
decreases. The bifurcated features of the two-phase RDW wave 
structure tend to be unobvious as the RDW-2 becomes weak with 
the increase of the total temperature, since the droplet evaporation 
can be achieved in a shorter length and has less inﬂuence on the 
initiation of RDW. 
As the total temperature decreases to 900 K in the present 
study, the self-sustained propagation of RDW cannot be achieved 
and the quenching occurs. The temporal distributions of tempera- 
ture and pressure are given in Figs. 35 and 36 , respectively. The 
proﬁles of Case RDT1 are found to be similar to those of Case 
RDP3. In particular, the local quenching occurs near the inlet, as 
shown by the decoupling of the shock wave and ﬂame in Fig. 35 (b). 
The quenching area propagates along the right direction and the 
height of the detonation front decreases continuously. In partic- 
ular, there are strong shear ﬂow between the unreacted and re- 
acted mixtures. Finlay the left part of the combustion chamber is 
ﬁlled with the fresh fuel-air mixture with low temperature and the 
detonation front breaks down. In Fig. 36 (f), only a curved shock 
wave with a V shape exists. The quenching dynamics are the same 
as those in the high-pressure ﬂow, in which the decoupling of 
shock and ﬂame is mainly due to the limited evaporation rates 
of droplets, and the local heat release from the chemical reaction 
cannot sustain the shock-ﬂame coupling in the fuel-lean mixtures. 
Therefore the interaction between droplet evaporation and chemi- 
cal reaction leads to the unsteady quenching of RDW in the two- 
phase ﬂow. 
6. Conclusions 
A fundamental investigation on the stability of kerosene/air 
two-phase rotating detonation, focusing on the self-sustained 
propagation and quenching, is performed based on the hybrid 
Eulerian-Lagrangian two-phase ﬂow model with a simpliﬁed two- 
step reaction mechanism. The rotating detonations formed in the 
gaseous fuel-air mixtures are analyzed for the comparative study. 
Considering a ramjet-based rotating detonation engine, the in- 
ﬂow parameters in the present study are set to meet the operation 
conditions of the combustion chamber. The total pressure and total 
temperature are varied according to different ﬂight Mach numbers 
and ﬂight altitudes to investigate the inﬂuence of these parame- 
ters on the rotating detonation features from the perspective of 
optimizing the RDC stability and the performance. For the ranges 
of rotating detonation stability considering the combustor size, the 
total pressure should be conﬁned among 3 atm and 7 atm, and the 
total temperature should be higher than 900 K. 
The self-sustained propagation RDW in two-phase ﬂows has 
a bifurcated wave structure near the inlet, which is due to 
the interaction among ﬂuid dynamics, dispersed droplets, chem- 
ical reaction, and shock wave. The RDW quenching is mainly 
due to two mechanisms, namely a reaction-dominated quenching 
and an evaporation-dominated quenching. The reaction-dominated 
quenching occurs in the ﬂows with low total pressure and initiates 
from the triple point, which is due to the weak chemical reaction 
rate and hence the non-generation of transverse waves at the deto- 
nation front. The evaporation-dominated quenching generates from 
the inlet and propagates to the outlet, and this is from the limited 
droplet evaporation rates in the ﬂows with high total pressure or 
low total temperature. 
The inﬂow conditions for a stable kerosene/air two-phase ro- 
tating detonation are wide for total temperature but are found to 
be narrow for total pressure, which is different from the gaseous 
RDW. This information will provide a plan for developing two- 
phase RDE using liquid fuel. 
Declaration of Competing Interest 
The authors declare that they have no known competing ﬁnan- 
cial interests or personal relationships that could have appeared to 
inﬂuence the work reported in this paper. 
Acknowledgments 
This work is partially supported by the Basic Research Plan of 
Natural Science in Shaanxi Province (Grant No. 2020JQ-159), NSFC 
under the Grant No. 51806179 , the project funded by China Post- 
doctoral Science Foundation, and the Fundamental Research Funds 
for the Central Universities. 
References 
[1] Q. Meng , N. Zhao , H. Zheng , et al. , A numerical study of rotating detonation 
wave with different numbers of fuel holes, Aerosp. Sci. Technol. 93 (2019) 
105301 . 
[2] Y. Zhong , Y. Wu , D. Jin , et al. , Investigation of rotating detonation fueled by the 
pre-combustion cracked kerosene, Aerosp. Sci. Technol. 95 (2019) 105480 . 
[3] Z. Ji , H. Zhang , B. Wang , Performance analysis of dual-duct rotating detonation 
aero-turbine engine, Aerosp. Sci. Technol. 92 (2019) 806–819 . 
[4] L. Deng , H. Ma , X. Liu , et al. , Secondary shock wave in rotating detonation com- 
bustor, Aerosp. Sci. Technol. 95 (2019) 105517 . 
[5] N. Zhao , Q. Meng , H. Zheng , et al. , Numerical study of the inﬂuence of annular 
width on the rotating detonation wave in a non-premixed combustor, Aerosp. 
Sci. Technol. (2020) 105825 . 
[6] F.A . Bykovskii , A .A . Vasil’ev , E.F. Vedernikov , et al. , Explosive combustion of a 
gas mixture in radial annular chambers, Combust. Explos. Shock Waves 30 (4) 
(1994) 510–516 . 
[7] V. Anand , A.S. George , R. Driscoll , et al. , Investigation of rotating detonation 
combustor operation with H2-Air mixtures, Int. J. Hydrogen Energy 41 (2) 
(2016) 1281–1292 . 
[8] Q. Xie , H. Wen , W. Li , et al. , Analysis of operating diagram for H2/Air rotating 
detonation combustors under lean fuel condition, Energy 151 (2018) 408–419 . 
[9] Q. Xie , B. Wang , H. Wen , et al. , Enhancement of continuously rotating detona- 
tion in hydrogen and oxygen-enriched air, Proc. Combust. Inst. 37 (3) (2019) 
3425–3432 . 
[10] B.A. Rankin , D.R. Richardson , A.W. Caswell , et al. , Chemiluminescence imaging 
of an optically accessible non-premixed rotating detonation engine, Combust. 
Flame 176 (2017) 12–22 . 
[11] S.M. Frolov , V.S. Aksenov , V.S. Ivanov , et al. , Large-scale hydrogen–air continu- 
ous detonation combustor, Int. J. Hydrogen Energy 40 (3) (2015) 1616–1623 . 
[12] K. Ishihara , J. Nishimura , K. Goto , et al. ,S t u d y on a long-time operation 
towards rotating detonation rocket engine ﬂight demonstration, 55th AIAA 
Aerospace Sciences Meeting (2017), p. 1062 . 
[13] H. Peng , W. Liu , S. Liu , et al. , Experimental investigations on ethylene-air Con- 
tinuous Rotating Detonation wave in the hollow chamber with Laval nozzle, 
Acta Astronaut. 151 (2018) 137–145 . 
[14] V. Anand , A.S. George , C.F. de Luzan , et al. , Rotating detonation wave me- 
chanics through ethylene-air mixtures in hollow combustors, and implications 
to high frequency combustion instabilities, Exp. Therm. Fluid Sci. 92 (2018) 
314–325 . 
[15] F.A . Bykovskii , S.A . Zhdan , E.F. Vedernikov , Continuous spin detonation in an- 
nular combustors, Combust. Explos. Shock Waves 41 (4) (2005) 449–459 . 
[16] Y. Zhong , D. Jin , Y. Wu , et al. , Investigation of rotating detonation wave fu- 
eled by “ethylene-acetylene-hydrogen” mixture, Int. J. Hydrogen Energy 43 (31) 
(2018) 14787–14797 . 
[17] S. Zhou , H. Ma , S. Chen , et al. , Experimental investigation on propagation 
characteristics of rotating detonation wave with a hydrogen-ethylene-acetylene 
fuel, Acta Astronaut. 157 (2019) 310–320 . 
[18] J. Kindracki , Experimental research on rotating detonation in liquid fuel—
gaseous air mixtures, Aerosp. Sci. Technol. 43 (2015) 445–453 . 
[19] A.K. Hayashi , N. Tsuboi , E. Dzieminska , Numerical study on JP-10/air detonation 
and rotating detonation engine, AIAA J. (2020) 1–17 . 
[20] C.T. Crowe , M.P. Sharma , D.E Stock , The particle-source-in cell (PSI-CELL) model 
for gas-droplet ﬂows, J. Fluids Eng. 99 (2) (1977) 325–332 . 
[21] A. Burcat , B. Ruscic , Third Millenium Ideal Gas and Condensed Phase Thermo- 
chemical Database For Combustion With Updates from Active Thermochemical 
tables, Argonne National Laboratory, Argonne, IL, 2005 . 
[22] B.E. Poling , J.M. Prausnitz , J.P O’connell , The Properties of Gases and Liquids, 
Mcgraw-hill, New York, 2001 . 
[23] Y. Ling , S. Balachandar , M. Parmar , Inter-phase heat transfer and energy cou- 
pling in turbulent dispersed multiphase ﬂows, Phys. Fluids 28 (3) (2016) 
033304 . 
[24] E. Loth , Compressibility and rarefaction effects on drag of a spherical particle, 
AIAA J. 46 (9) (2008) 2219–2228 . 
[25] R.S. Miller , K. Harstad , J. Bellan , Evaluation of equilibrium and non-equilibrium 
evaporation models for many-droplet gas-liquid ﬂow simulations, Int. J. Mul- 
tiph. Flow 24 (6) (1998) 1025–1055 . 
18

<!-- PDF_PAGE: 19 -->

Z. Ren and L. Zheng Combustion and Flame 231 (2021) 1114 8 4 
[26] B. Franzelli , E. Riber , M. Sanjosé, et al. , A two-step chemical scheme for 
kerosene–air premixed ﬂames, Combust. Flame 157 (7) (2010) 1364–1373 . 
[27] Z. Ren , B. Wang , L. Zheng , Numerical analysis on interactions of vortex, shock 
wave, and exothermal reaction in a supersonic planar shear layer laden with 
droplets, Phys. Fluids 30 (3) (2018) 036101 . 
[28] Z. Ren , B. Wang , G. Xiang , et al. , Effect of the multiphase composition in a 
premixed fuel–air stream on wedge-induced oblique detonation stabilisation, 
J. Fluid Mech. 846 (2018) 411–427 . 
[29] X.Y. Hu , Q. Wang , N.A Adams , An adaptive central-upwind weighted essentially 
non-oscillatory scheme, J. Comput. Phys. 229 (23) (2010) 8952–8965 . 
[30] R.T. Fievisohn , K.H. Yu , Steady-state analysis of rotating detonation engine 
ﬂowﬁelds with the method of characteristics, J. Propul. Power (2017) 89–99 . 
[31] Y. Uemura , A.K. Hayashi , M. Asahara , et al. , Transverse wave generation 
mechanism in rotating detonation, Proc. Combust. Inst. 34 (2) (2013) 
1981–1989 . 
[32] Z. Ren , B. Wang , G. Xiang , et al. , Numerical analysis of wedge-induced oblique 
detonations in two-phase kerosene–air mixtures, Proc. Combust. Inst. 37 (3) 
(2019) 3627–3635 . 
[33] G.A Sod , A survey of several ﬁnite difference methods for systems of nonlinear 
hyperbolic conservation laws, J. Comput. Phys. 27 (1) (1978) 1–31 . 
[34] G. Xu , M. Ikegami , S. Honma , et al. , Inverse inﬂuence of initial diameter on 
droplet burning rate in cold and hot ambiences: a thermal action of ﬂame in 
balance with heat loss, Int. J. Heat Mass Transf. 46 (7) (2003) 1155–1169 . 
[35] W.C Reynolds , STANJAN Chemical Equilibrium Solver. V3.89 IBM PC, Stanford 
University, Stanford, 1981 . 
[36] F. Schauer , C. Miser , C. Tucker , et al. , Detonation initiation of hydrocarbon-air 
mixtures in a pulsed detonation engine, 43rd AIAA Aerospace Sciences Meeting 
and Exhibit (2005), p. 1343 . 
[37] J.M. Austin , J.E Shepherd , Detonations in hydrocarbon fuel blends, Combust. 
Flame 132 (1–2) (2003) 73–90 . 
19

<!-- PDF_PAGE: 20 -->

Update 1 of 2
Combustion and Flame
Volume 242, Issue , August 2022, Page 
 https://doi.org/10.1016/j.combustflame.2022.112048DOI:

<!-- PDF_PAGE: 21 -->

Combustion and Flame 242 (2022) 112 0 4 8 
Contents lists available at ScienceDirect 
Combustion and Flame 
journal homepage: www.elsevier.com/locate/combustflame 
Erratum to “Numerical study on rotating detonation stability in 
two-phase kerosene-air mixture” [Combust. Flame 231 (2021) 1114 8 4 ] 
Zhaoxin Ren, Longxi Zheng ∗
School of Power and Energy, Northwestern Polytechnical University, Xi’an, 710072, China 
The Publisher regrets that within the abovementioned article, the Figure 5 had been duplicated was published as Figure 4 . The ﬁgure has 
been corrected online, and has been printed below: 
Figure 4. 
The Publisher apologizes for any inconvenience caused. 
DOI of original article: 10.1016/j.combustﬂame.2021.1 1 1484 
∗ Corresponding author. 
E-mail address: zhenglx@nwpu.edu.cn (L. Zheng). 
https://doi.org/10.1016/j.combustﬂame.2022.1 12048 
0010-2180/© 2022 The Combustion Institute. Published by Elsevier Inc. All rights reserved.

<!-- PDF_PAGE: 22 -->

Update 2 of 2
Combustion and Flame
Volume 252, Issue , June 2023, Page 
 https://doi.org/10.1016/j.combustflame.2022.112266DOI:

<!-- PDF_PAGE: 23 -->

Combustion and Flame 252 (2023) 1 12266 
Contents lists available at ScienceDirect 
Combustion and Flame 
journal homepage: www.elsevier.com/locate/combustflame 
Corrigendum 
Corrigendum to ‘Numerical study on rotating detonation stability in 
two-phase kerosene-air mixture’ [Combust. Flame 231 (2021) 1114 8 4 ] 
Zhaoxin Ren, Longxi Zheng ∗
School of Power and Energy, Northwestern Polytechnical University, Xi’an 710072, China 
The Authors regret that the Acknowledgements section was incomplete. The Acknowledgements have been corrected online, and can 
be found below: 
Acknowledgments 
This work is partially supported by the Basic Research Plan of Natural Science in Shaanxi Province (Grant No. 2020JQ-159), NSFC under 
the Grant No. 51806179, the project funded by China Postdoctoral Science Foundation, and the Fundamental Research Funds for the Central 
Universities. 
The Authors apologize for any inconvenience caused. 
DOI of original article: 10.1016/j.combustﬂame.2021.1 1 1484 
∗ Corresponding author. 
E-mail address: zhenglx@nwpu.edu.cn (L. Zheng) . 
https://doi.org/10.1016/j.combustﬂame.2022.1 12266 
0010-2180/© 2022 The Combustion Institute. Published by Elsevier Inc. All rights reserved.
