<!-- PDF_PAGE: 1 -->

Fuel 314 (2022) 123087
Available online 10 January 2022
0016-2361/© 2021 Elsevier Ltd. All rights reserved.
Full Length Article 
Simulations of rotating detonation combustion with in-situ evaporating 
bi-disperse n -heptane sprays 
Shan Jin
a , b
, Huangwei Zhang
b , *
, Ningbo Zhao
a
, Hongtao Zheng
a 
a
College of Power and Energy Engineering, Harbin Engineering University, Harbin 150001, China 
b
Department of Mechanical Engineering, National University of Singapore, 9 Engineering Drive 1, Singapore 117576, Republic of Singapore   
ARTICLE INFO  
Keywords: 
Rotating detonation combustion 
N -heptane spray 
Reactant mixing 
Equivalence ratio 
Velocity deficit 
Propulsion performance 
ABSTRACT  
Eulerian-Lagrangian simulations are conducted for two-dimensional Rotating Detonative Combustion fueled by 
bi-disperse n -heptane sprays without any fuel pre-vaporization. Parametric studies are performed to study the 
influences of droplet diameter and droplet distribution on the rotating detonation wave. The extinction process of 
the detonation wave is also been analyzed. It is found that small n -heptane droplets (e.g., 2 µ m) are completely 
vaporized in the fuel refilling area. Increasing the droplet diameter causes the droplet to fail to evaporate 
completely within the fuel refilling area and exist after the detonation wave. A reflected shock can be observed 
after the detonation wave. When the droplet diameter is larger than 10 μ m, the higher pressure after the 
detonation wave leads to the reactants cannot be sprayed into the combustor, eventually leading to extinction of 
the detonation wave. In bi-disperse n -heptane sprays, presence of droplets with small diameter stabilizes the 
detonation wave. The average equivalence ratio (up to 0.66 only) in the fuel refilling area is lower than total 
equivalence ratio (1.0 in this work), and the average equivalence ratio decreases with increased droplet diameter 
in the bi-disperse n -heptane sprays. The increase in droplet diameter decreases the detonated fuel fraction and 
detonation wave speed. The detonation speeds in bi-disperse n -heptane sprays are 3 – 9% lower than the 
respective gaseous cases. Moreover, the results also show that propulsion performance of rotating detonation 
combustor, such as thrust and specific impulse, decreases with the droplet diameter.   
1. Introduction 
Rotating Detonation Engine (RDE) is deemed one of the most 
promising pressure-gain combustion technologies due to the high ther -
modynamic cycle efficiency [1,2] . In previous studies, gaseous fuels are 
mainly tested, including hydrogen and simple hydrocarbons [1-5] . 
However, liquid fuels typically have a higher energy density and are 
more convenient to be stored and transported. Utilization of liquid fuels 
is of utmost importance to commercialize rotating detonation technol -
ogy to engineering practice. 
The first liquid fuel RDE test was carried out in 1960s [6] , and in 
recent years a lot of research progress has been available for liquid fuel 
RDEs. For instance, Bykovskii et al. [5,7,8] used liquid kerosene sprays 
and oxygen-enriched air in experimental research on two-phase rotating 
detonation. The diameter of outer combustor wall in their test was 306 
mm. They found that addition of hydrogen to the mixture can reduce the 
critical diameter of the RDE combustor. After that, they increased the 
diameter to 503 mm [7,8] , and found that the Rotating Detonation Wave 
(RDW) cannot continuously propagate without hydrogen or syngas 
added. 
In addition, Kindracki [9] investigated kerosene atomization char -
acteristics under different carrier gas (nitrogen) velocities and fuel in -
jection patterns in a RDE combustor. They measured the droplet 
diameters and found that when the sprayed droplet diameters are 
20  40 μ m, the droplets can quickly evaporate in the combustor. Sub -
sequently, they used kerosene with hydrogen addition to conduct a two- 
phase rotating detonation experiment [10] . They successfully obtained a 
rotating detonation wave that propagates stably, with a velocity deficit 
of the detonation wave propagation being 20%  25%. More recently, 
Wola ´nski and his co-workers [11] partially mixed the preheated liquid 
Jet-A and hot air, leading to a composition higher than the rich flam -
mability limit. With that, they achieved a rotating detonation without 
hydrogen addition. They also found that heat losses, momentum losses, 
and pre-combustion of the fuel are the main reasons for the speed deficit 
(up to 35%). 
To obtain more detailed structures of rotating detonations in liquid 
fuel sprays, RDE modelers also carried out a series of numerical studies. 
* Corresponding author. 
E-mail address: huangwei.zhang@nus.edu.sg (H. Zhang).  
Contents lists available at ScienceDirect 
Fuel 
journal homepag e: www.else vier.com/loc ate/fuel 
https://doi.org/10.1016/j.fuel.2021.123087 
Received 27 September 2021; Received in revised form 26 December 2021; Accepted 28 December 2021

<!-- PDF_PAGE: 2 -->

Fuel 314 (2022) 123087
2
For instance, Sun and Ma [12] investigated the effects of air total tem -
perature and fuel inlet spacing on the two-phase RDW in liquid octane 
and air. They found that increasing the fuel inlet spacing decreases the 
wave speed. Moreover, Hayashi et al. [13] investigated the effects of JP- 
10 droplet diameter and pre-evaporation on two-phase rotating deto -
nation waves. They found that there are liquid droplets along the contact 
surface between the fresh and burned gas. Ren and Zheng [14] studied 
the limit of kerosene/air two-phase detonation stability as a function of 
total pressure and total temperature, mimicking the operating condi -
tions of ramjet detonation engine. They found that stable rotating 
detonation can be achieved in a limited range of total pressure and 
increased total temperature is conducive to RDW stability. 
Moreover, Meng et al. [15] used n -heptane/air as the reactants to 
systematically study the influences of initial droplet diameter (5 – 50 μ m) 
and the n -heptane pre-evaporation degree on detonation characteristics 
(e.g., detonation velocity, detonated fuel fraction, droplet evaporation 
height). Meng et al. [16] also investigated the rotating detonation 
combustion with partially pre-vaporised n -heptane spray without 
hydrogen addition. They analyzed the detailed RDE flow field and 
droplet distribution inside the fuel refilling zone and found that a layer 
with high vapor concentration exists between the droplet-laden area and 
deflagration surface. Besides, Zhao and Zhang [17] investigated the 
influences of droplet diameter and equivalence ratio on rotating deto -
nations. The propagation speed increases as the total equivalence ratio 
Nomenclature 
C
p 
Heat capacity at constant pressure [J/kg/K] 
D Deformation gradient tensor 
D
f 
Vapour mass diffusivity in the gas phase [m
2
/s] 
D
m 
Mass diffusivity [m
2
/s] 
d
0
s 
Initial droplet diameter of small droplet [ μ m] 
d
0
l 
Initial droplet diameter of large droplet [ μ m] 
E Total non-chemical energy [J/kg] 
e Specific sensible internal energy [J/kg] 
F
d 
Drag force on the droplet [N] 
Δ h
o
f , m 
Formation enthalpy of m -th species [J/mol] 
h ( T
d
) Heat of vaporization at the droplet temperature [J/kg] 
I Unit tensor 
j Diffusive heat flux [W/m
2
] 
k Thermal conductivity coefficient [W/m/K] 
k
c 
Mass transfer coefficient [m/s] 
Le
m 
Lewis number of m -th species 
M Total species number 
m
d 
Mass of a single droplet [kg] 
˙m
d 
Evaporation rate [kg/s] 
˙m
f 
Vapor mass flux [kg/m
2
/s] 
c
p,d 
droplet heat capacity [J/kg/K] 
Nu Nusselt number 
n
p 
Droplet number per parcel 
T
S 
Droplet surface temperature [K] 
V
d 
Volume of a single fuel droplet [m
3
] 
B
T 
Spalding heat transfer number 
Pr Prandtl number 
Re
d 
Droplet Reynolds number 
˙
Q
c 
Convective heat transfer rate [J/s] 
R Specific gas constant [J/kg/K] 
R
u 
Universal gas constant [J/mol/K] 
Sc Schmidt number 
Sh Sherwood number 
s
m 
Species mass flux [kg/m
2
/s] 
S
mass 
Mass transfer rate [kg/m
3
/s] 
S
mom 
Momentum transfer rate [N/m
3
] 
S
energy 
Energy transfer rate [J/m
3
/s] 
S
species , m 
Species transfer rate [kg/m
3
/s] 
T Gas temperature [K] 
T Viscous stress tensor [kg/m/s
2
] 
T
d 
Droplet temperature [K] 
t Time [s] 
u Velocity vector [m/s] 
u
d 
Droplet velocity vector [m/s] 
V
c 
CFD cell volume [m
3
] 
W
d 
Molar weight of the vapor [kg/mol] 
W
m 
Molar weight of m -th species [kg/mol] 
Y
m 
Mass fraction of m -th species 
p Pressure [Pa] 
X
S 
Fuel vapor mole fraction 
F
d 
Drag force on the droplet [N] 
F
p 
Pressure gradient force [N] 
F
u 
Thrust from kinetic energy [N] 
F
p 
Thrust from pressure gain [N] 
A
0 
Surface of outlet [m
2
] 
v
g 
velocity of gaseous detonation [m/s] 
v
d 
velocity of two-phase detonations [m/s] 
˙
Q
lat 
Latent heat transfer rate [J/s] 
Greek letters 
α Thermal diffusivity coefficient [m
2
/s] 
μ Dynamic viscosity [kg/m/s] 
ρ Gas density [kg/m
3
] 
ρ
d 
Droplet material density [kg/m
3
] 
˙ω
m 
Production or consumption rate of m -th species [kg/m
3
/s] 
˙ω
T 
Heat release from chemical reactions [J/m
3
/s] 
ϕ Equivalence ratio 
ψ detonated fuel fraction 
Superscript 
0 Initial value 
Subscripts 
c CFD cell 
d Droplet 
energy Energy 
f Droplet surface 
i i -th condensed species vapor 
m Mass, m -th species 
mass Mass 
mom Momentum 
p Pressure gain 
s Small droplet 
species Species 
l Large droplet 
eff Effective value 
u kinetic energy 
Acronym 
RDE Rotating detonation engine 
RDW Rotating detonation wave 
HRR Heat release rate [J/m
3
/s] 
ER Evaporation rate [kg/ m
3
/s) 
FI Flame index 
I
sp 
Specific impulse [s] 
CFD Computational fluid dynamics  
S. Jin et al.

<!-- PDF_PAGE: 3 -->

Fuel 314 (2022) 123087
3
increases for the same droplet diameter. Furthermore, they observed 
that when the droplet diameter is less than 5 μ m, the thrust force from 
pressure gain and kinetic energy decreases significantly with the droplet 
diameter. However, for initial droplet diameter d
0 
> 5 μ m, the thrust 
force from the kinetic energy first increases and then decreases with the 
droplet diameter, while the thrust force from pressure gain is shown to 
have limited change. 
In this work, the effects of initial droplet diameter on wave speed, 
detonated fuel fraction and specific impulse in two-phase rotating 
detonation combustor without pre-vaporization (only in-situ gasifica -
tion) will be further studied with Eulerian – Lagrangian method. In pre -
vious studies on two-phase detonation, mono-sized or polydispersed 
droplets have been considered, such as in Refs. [13,14,18 – 21] . It is well 
known that the droplets of various sizes can behave differently in terms 
of evaporation, heating and velocity relaxation with the gas phase. 
When we consider the mono-sized droplets, it is possible to clearly un -
derstand how the droplets of a particular size evolve in a detonated flow 
field. However, this is idealized, because polydisperse droplets are 
ubiquitous in practical spray combustion because atomizers are used 
[9 – 11] . Nonetheless, a real droplet size distribution (i.e., diameter range 
and distribution shape) is still full of uncertainties (difficult to be 
characterized) and it is challenging to be accurately modelled in CFD. If 
we use some presumed distributions for the droplets, this will make our 
research results lack of generality. Therefore, we will consider bi- 
disperse droplets in this study. Two-dimensional flatten domain is 
used to model the practical rotating detonation combustor, and liquid n - 
heptane and air are selected as the reactants. The rest of the manuscript 
is structured as below. In Section 2 the computational method and the 
physical model are introduced. Results are presented and discussed in 
Section 3 , whereas conclusions are made in Section 4 . 
2. Mathematical and physical models 
2.1. Governing equation 
The Eulerian – Lagrangian method is used to investigate the two- 
phase rotating detonation combustion in this work. The gas phase is 
described with the Eulerian method, whilst the sprayed liquid fuel 
droplets are tracked by the Lagrangian method. For the gas phase, the 
governing equations for unsteady compressible multi-species reacting 
flows read 
∂ρ
∂ t
+ ∇ ∙ [ ρ u ] = S
m
(1)  
∂ ( ρ u )
∂ t
+ ∇ ∙ [ u ( ρ u ) ] + ∇ p + ∇ ∙ T = S
F
(2)  
∂ ( ρ E )
∂ t
+ ∇ ∙ [ u ( ρ E ) ] + ∇ ∙ [ u p ] + ∇ ∙ [ T ∙ u ] + ∇ ∙ j = _ω
T
+ S
e
(3)  
∂ ( ρ Y
m
)
∂ t
+ ∇ ∙ [ u ( ρ Y
m
) ] + ∇ ∙ s
m
= _ω
m
+ S
Y m
, ( m = 1 , ⋯ M  1 ) (4)  
p = ρ RT (5)  
here t is time and ∇ ∙ ( ∙ ) is the divergence operator. ρ is the gas density, u 
is the gas velocity vector, T is the gas temperature, and p is the pressure. 
Y
m 
is the mass fraction of m -th species, and M is the total species number. 
E is the total non-chemical energy, i.e., E ≡ e
s
+ | u |
2
/ 2. e
s
= h
s
 p / ρ is 
the sensible internal energy and h
s 
is sensible enthalpy. R in Eq. (5) is the 
specific gas constant and is calculated from R = R
u
∑
M
m = 1
Y
m
MW
 1
m
. MW
m 
is the molar weight of m -th species and R
u
= 8 . 314 J/(mol ∙ K) is the 
universal gas constant. The viscous stress tensor T in Eq. (2) modelled by 
T =  2 μ dev ( D ) . Here μ is the dynamic viscosity and is dependent on gas 
temperature following the Sutherland ’ s law. Moreover, 
D ≡
[
∇ u +(∇ u )
T
]/
2 is the deformation gradient tensor and its devia -
toric component, dev ( D ) , is defined as dev ( D ) ≡ D  tr ( D ) I / 3 with I being 
the unit tensor. j in Eq. (3) is the diffusive heat flux and can be modelled 
by Fourier ’ s law, i.e. j =  k ∇ T . Thermal conductivity k is calculated 
using the Eucken approximation [22] , i.e. k = μ C
v
( 1 . 32 + 1 . 37 ∙ R / C
v
) , 
where C
v 
is the heat capacity at constant volume and derived from C
v
=
C
p
 R . Here C
p
=
∑
M
m = 1
Y
m
C
p , m 
is the heat capacity at constant pressure, 
and C
p , m 
is the heat capacity of m -th species, which is estimated from 
JANAF polynomials [23] . Particle-source-in-cell (PSI-CELL) approach is 
used [24] and the source terms in Eqs. (1) – (4) , i.e., S
m
, S
F
, S
e 
and S
Y
m
, 
account for the exchanges of mass (fuel species), momentum, and en -
ergy, respectively. 
In Eq. (4) , s
m
=  D
m
∇( ρ Y
m
) is the species mass flux. With unity 
Lewis number assumption, the mass diffusivity D
m 
is calculated through 
D
m
= k / ρ C
p
. Moreover, ˙ω
m 
is the production or consumption rate of m - 
th species by all N reactions, and can be calculated from the reaction rate 
of each reaction ω
o
m , j
, i.e. 
˙ω
m
= MW
m
∑
N
j = 1
ω
o
m , j
. (6) 
Also, the term ˙ω
T 
in Eq. (3) accounts for the heat release from 
chemical reactions and is estimated as ˙ω
T
= 
∑
M
m = 1
˙ω
m
Δ h
o
f , m
. Here Δ h
o
f , m 
is the formation enthalpy of m -th species. 
The Lagrangian method is used to track the liquid fuel droplets. The 
equations of mass, momentum, and energy for single droplets are 
dm
d
dt
=  ˙m
d
, (7)  
d u
d
dt
=
F
d
+ F
p
m
d
, (8)  
c
p , d
dT
d
dt
=
˙
Q
c
+
˙
Q
lat
m
d
, (9)  
where m
d
= π ρ
d
d
3
/ 6 is the mass of a single droplet, where ρ
d 
and d are 
the droplet material density and diameter, respectively. u
d 
is the droplet 
velocity vector, c
p,d 
is the droplet heat capacity, and T
d 
is the droplet 
temperature. Uniform temperature inside the droplet is assumed, since 
the droplet Biot number is small in our simulations. 
Phase change of the liquid fuel droplets, i.e., evaporation, is 
considered in our studies. The phase transition can be described with the 
help of an equilibrium, or non-equilibrium model or a generalized model 
[25-27] . In this study, the evaporation rate of the droplet ˙m
d 
is calcu -
lated with Abramzon and Sirignano model [28] . Its accuracy in pre -
diction of droplet evaporation in elevated ambient pressures and 
temperatures has been validated in our recent work [17] . The droplet 
evaporation rate reads 
˙m
d
= π d ρ
f
D
f
Shln ( 1 + B
M
) (10)  
where ρ
f
= p
S
MW
m
/ RT
S 
and D
f
= 3 . 6059 × 10
 3
∙ ( 1 . 8T
s
)
1 . 75
∙ ( α / p
s
β ) are 
the density and mass diffusivity at the film over the droplet, respectively 
[17] . α and β are the constants related to specific species [29] . 
p
S
= p ∙ exp

c
1
+ c
2
/ T
s
+ c
3
lnT
s
+ c
4
T
c
5
s
)
is the surface vapor pressure, with 
T
S
= ( T + 2 T
d
) / 3 being the droplet surface temperature. In Eq. (10) , B
M 
is the Spalding mass transfer number and defined as 
B
M
≡ ( Y
Fs
 Y
F ∞
) / ( 1  Y
Fs
) . Y
Fs
= MW
d
X
s
/ [ MW
d
X
s
+ MW
ed
( 1  X
s
) ]
and Y
F ∞ 
are the vapor mass fractions at the droplet surface and in the gas 
phase, respectively. MW
d 
is the molecular weight of the vapor, MW
ed 
is 
the averaged molecular weight of the mixture excluding the fuel vapor, 
and X
S
= X
m
p
sat
/ p is the mole fraction of the vapor at the droplet surface. 
Here p
sat 
is the saturated pressure and X
m 
is the molar fraction of the 
condensed species in the gas phase. 
In Eq. (8) , F
d 
is the Stokes drag, which is modelled as 
S. Jin et al.

<!-- PDF_PAGE: 4 -->

Fuel 314 (2022) 123087
4
F
d
=
(
18 μ / ρ
d
d
2
)
∙ ( C
d
Re
d
/ 24 ) ∙ m
d
( u  u
d
) [30] . Here C
d 
is the drag co -
efficient and estimated using the Schiller and Naumann model [31] . 
Re
d
≡ ρ d | u
d
 u | / μ is the droplet Reynolds number. Also, F
p 
is the pres -
sure gradient force and is calculated from F
p
=  V
d
∇ p . Here V
d 
is the 
volume of a single fuel droplet. 
In Eq. (9) , 
˙
Q
c
= h
c
A
d
( T  T
d
) denotes the convective heat transfer 
between the gas and liquid phases. Here A
d 
is surface area of a single 
droplet. h
c 
is the convective heat transfer coefficient, and estimated 
using the correlation of Ranz and Marshall [32] through the modified 
Nusselt number, i.e. Nu = 2 +
[
( 1 + Re
d
Pr )
1 / 3
max ( 1 , Re
d
)
0 . 077
 1
]/
F ( B
T
) [28] . Pr is the gas Prandtl number, and B
T 
is the Spalding heat 
transfer number. Furthermore, 
˙
Q
lat 
in Eq. (9) denotes the heat transfer 
caused by the latent heat of evaporation. 
Two-way coupling between the gas and liquid phases are considered 
based on PSI-CELL method, in terms of mass, momentum, energy and 
species exchanges. Specifically, we consider the transfer of the fuel 
species between liquid droplets and the gas due to liquid evaporation. 
We also include the convective heat transfer between the gas and liquid 
phases and the heat transfer caused by the enthalpy carried by the fuel 
vapour. Besides, the drag force and momentum transfer due to droplet 
evaporation are taken into consideration, and the gravitational force is 
neglected since we only study small droplets. Therefore, the source 
terms for the gas phase equations read ( V
c 
is cell volume and N
d 
is the 
droplet number in a CFD cell) 
S
m
=
1
V
c
∑
N
d
1
˙m
d
, (11)  
S
F
= 
1
V
c
∑
N
d
1
(
 ˙m
d
u
d
+ F
d
)
, (12)  
S
e
= 
1
V
c
∑
N
d
1
[
 ˙m
d
h ( T
d
) +
˙
Q
c
]
, (13)  
S
Y m
=
{
S
m
f or the liquid f uel species ,
0f or other species ,
(14) 
In Eq. (13) , h ( T
d
) is the fuel vapor enthalpy at the droplet tempera -
ture. Note that the energy exchange caused by the hydrodynamic force is 
not included since it is of secondary importance for dilute spray deto -
nations [33] . This has also been confirmed from our a posterior com -
parisons of the hydrodynamic force work and convective heat transfer 
from our simulations, which shows that the former is much (2 – 3 orders 
of magnitude) smaller than the latter in dilute and fine sprays. 
2.2. Physical model 
Fig. 1 shows the schematic of rotating detonation in a two- 
dimensional (2D) unrolled model RDE chamber. Although three- 
dimensional (3D) geometry effects do play an essential role in rotating 
detonations [4,34 – 37] , however, the objective of this paper is to 
investigate the effects of dispersed phase properties (such as droplet size 
and loading) on rotating detonations, and it is sufficient if we can well 
predict the key flow field characteristics in the modelled RDE 
combustor. Previous studies using 2D domain have confirmed that 2D 
simulations can accurately reproduce the flow and combustion features 
in RDEs, e.g., in Refs. [38,39] . In light of these considerations, in this 
paper, a 2D computational domain will be adopted. The lengths ( x -di -
rection) and width ( y -direction) of the domain are 153 mm and 50 mm, 
respectively. This extent ensures that the rotating detonation wave and 
accompanied flow features can be correctly captured. 
The boundary conditions of the model RDE chamber are also marked 
in Fig. 1 . Specifically, the outlet is assumed to be non-reflective, which is 
reasonable since the local flows are supersonic. Periodic boundaries at 
the left and right sides are enforced, such that the RDW can continuously 
propagate across the flattened domain. 
Through the continuous injectors at the bottom of the domain in 
Fig. 1 , the spherical droplets of liquid n -heptane sprays are injected into 
the domain with carrier gas, heated air, with the same strategy used by 
Meng et al. [15,16] . The initial temperature of the n -heptane droplets is 
323 K to promote rapid evaporation of the droplet. The initial material 
density of the n -heptane droplets is 680 kg/m
3
. The initial temperature 
and pressure of the carrier gas air are 700 K and 30 atm, respectively. 
The liquid equivalence ratio can be varied by changing volume fractions 
of the liquid fuel droplets in the carrier gas. Moreover, a high- 
temperature and high-pressure spot (2,000 K and 20 atm) of 1 mm ×
12 mm is used in the lower left corner of the combustor, as shown in 
Fig. 1 , to initiate the detonation wave. 
It is well known that in practical RDEs [9-11] , liquid fuel sprays are 
always polydispersed, and the size of the fuel droplets are therefore 
distributed. Different from our previous work [15 – 17] , the effects of the 
initial droplet diameters of a polydisperse sprays on RDW propagation, 
in-chamber reactant mixing and propulsion performance are studied. 
However, to pinpoint the foregoing effects, bi-dispersed droplets with a 
specified mass ratio are considered in the current study, i.e., one class of 
fuel droplets with smaller diameter d
0
s
, whilst the other class with larger 
sizes d
0
l
. Their mass ratios are parameterized by liquid equivalence ra -
tios, i.e., ϕ
s 
and ϕ
l
, respectively. They are defined as the mass ratio of the 
liquid droplets (with d
0
s 
and d
0
l
) to the carrier gas air from the injector. In 
all the simulations, the total liquid fuel equivalence ratios, i.e., ϕ
t
= ϕ
s
+
ϕ
l
, are fixed to be unity. As such, varying either of the equivalence ratio, 
ϕ
s 
or ϕ
l
, would lead to change of the other. The initial diameter of the 
Fig. 1. Computational domain and boundary condition in two-dimensional RDE.  
S. Jin et al.

<!-- PDF_PAGE: 5 -->

Fuel 314 (2022) 123087
5
smaller droplet class d
0
s 
is fixed to be 2 µ m in all our cases, whereas d
0
l 
varies from 5 to 20 µ m . 
Moreover, in this study, pure n -heptane sprays with in-situ evapo -
ration in the RDE model combustor will be considered, i.e., no pre- 
vaporization effects. Therefore, this is closer to the practical RDE 
implementations. In published literature, very limited work has been 
reported on modelling of pure spray RDE, except the recent one by Ren 
and Zheng [14] , where pure kerosene is used as the propellant. 
2.3. Numerical implementation 
The governing equations for both gas and liquid phases are solved by 
a multiphase reacting flow code RYrhoCentralFoam [40] , which is 
developed based on a density-based compressible flow solver rhoCen -
tralFoam in OpenFOAM 6.0 [41] . Detailed validations and verifications 
have been made for RYrhoCentralFoam [42,43] , including: (1) shock 
capturing, (2) molecular diffusion, (3) shock-chemistry interactions, (4) 
chemistry integration schemes, (5) detonation propagation speed and 
cellular structure, and (6) gas – liquid two-phase models (such as droplet 
evaporation, two-phase coupling). All the validations are demonstrated 
collectively through Ref. [44] . It has been successfully used for model -
ling detonative combustion with gaseous and liquid fuels [15,17,39,44] . 
The cell-centered finite volume method is used to discretize the gas 
phase equations, i.e., Eqs. (1) – (4) . The second-order implicit backward 
scheme is used for time marching of the gas phase variables. The time 
step is about 10
 9 
s, which leads to a maximum Courant number of 0.1. 
Moreover, second-order Godunov-type upwind-central scheme is used 
to calculate the convection terms in the momentum equations. The total 
variation diminishing scheme is applied for the convection terms in the 
energy and species mass fraction equations. 
Two-step chemical mechanism for n -heptane is used in this work, 
which includes six species (i.e., n -C
7
H
16
, CO, CO
2
, H
2
O, O
2
, N
2
) and two 
reactions. The chemical mechanisms are listed in Table 1 with their 
respective parameters for Arrhenius kinetics. This mechanism has been 
validated against a detailed mechanism [45] and the results show that it 
can correctly reproduce the detonation propagation speed, pressure, and 
temperature at both von Neumann and Chapman – Jouguet (C-J) points 
in the ZND (Zeldovich  von Neumann  D ¨oring) structures corre -
sponding to a wide range of operating conditions [16] . The two-step 
chemistry is deemed sufficient in this work since detailed gaseous 
chemistry is not focused on here; instead, we are more interested in 
detonation propagation speed, overall propulsion performance and 
droplet dynamics in liquid fueled RDE. 
For the liquid phase, the Lagrangian equations, i.e., Eqs. (7) – (9) , are 
solved with the first-order Euler method. With the PSI-CELL imple -
mentations, two-way coupling between the gas and liquid phases about 
species, mass, momentum, and energy exchanges is performed for each 
time step, through Eqs. (11) – (14) . The droplet breakup model by Reitz 
[46] is used, which can accurately simulate the droplet breakup under 
engine relevant conditions and also successfully used for spray detona -
tion modelling [17] . We use computational parcel method in our sim -
ulations, and one parcel contain many droplets having the same 
velocity, size, temperature, and thermodynamic parameters. The drop -
lets in each parcel will be solved from the same set of Lagrangian 
equations, i.e., Eqs. (7) – (9) . The actual initial number of the droplets in a 
parcel are determined from the loading and diameter of the droplets. 
The computational domain in Fig. 1 is discretized with uniform 
496,000 Cartesian cells for the Eulerian flow field calculations and the 
cell spacing size is 125 µ m . Mesh sensitivity analysis is also performed, 
which demonstrates that further refinement of the mesh would not 
change the predicted detonation speed and key features of the rotating 
detonative flow fields. Additionally, in the hybrid Eulerian  Lagrangian 
method with point-force approximation, the Lagrangian droplet diam -
eter should be smaller than the Eulerian cell size [47] . This is because 
the gas phase quantities near the droplet surfaces (critical for estimating 
the two-phase coupling, e.g. evaporation) can be well approximated 
using the interpolated ones at the location of the sub-grid droplet [48] . 
In our simulations, the ratio of the Eulerian cell size and Lagrangian 
droplets, θ , range from 6.25 to 62.5, which is well above or close to the 
criterion, θ > 10, as suggested by Sontheimer et al. [49] and Luo et al. 
[50] . As such, the current Eulerian mesh resolution is expected to be 
sufficient for capturing the flow field, droplet dynamic behaviors and 
gas  liquid bi-directional coupling in liquid fuel rotating detonations. 
The accumulation error in numerical simulations depends on the 
accuracy of algorithm and grid, and the number of time integration 
steps. Some methods for error estimations in simulations of a combustor 
are provided in Refs. [51] and [52] . Based on their methods, the cu -
mulative error in our simulations is about 0.3%, estimated with the 
numerical scheme accuracy (second-order), mesh size (0.125 mm), and 
time step (2 × 10
 9 
μ s) used in this work. This confirms the accuracy of 
the numerical methods in RYrhoCentralFoam solver and simulation setup 
for the spray RDE modelling. 
Note that the operating time of an RDE test can be, e.g., 0.1 s or 4 s 
[10,11] . Considering the computational cost, the simulated physical 
time of the rotating detonations in this paper are about 1,500 μ s, which 
is indeed lower than the reported time in the actual experiments. 
Nonetheless, this roughly corresponds to 10 cycles of rotating detona -
tions and the detonation wave has propagated steadily. Therefore, the 
long-term behaviors of the detonation wave can be well confirmed in our 
simulations. 
3. Results and discussion 
3.1. RDW propagation in fuel sprays 
The features of rotating detonations in sprayed n -heptane fuels will 
be demonstrated in this section. Three cases are considered: (1) mono- 
sized sprays with initial droplet diameter d
0 
= 2 µ m; (2) mono-sized 
sprays with d
0 
= 10 µ m ; and (3) bi-disperse sprays with 50% droplets 
of d
0
s 
= 2 μ m and 50% large droplets of d
0
l 
= 10 μ m. Be reminded that the 
(total) liquid fuel equivalence ratios in these three cases are identical, i. 
e. ϕ
t 
= 1.0. The key information about the gas phase and liquid phase is 
listed in Table 2 . 
Fig. 2 shows the contours of pressure and gas temperature corre -
sponding to case 1. The results are extracted after the RDW runs over ten 
cycles. In this work, one cycle means that the RDW propagates from the 
left periodic boundary to the right one. The key features of rotating 
Table 1 
Chemical mechanism for n -C
7
H
16 
combustion (units in cm-sec-mole-cal-Kelvin). 
A is the pre-exponential factor, n is the temperature exponent, E
a 
is the activa -
tion energy, a and b are the fuel and oxidizer reaction orders, respectively.   
Reaction A n E
a 
a b 
I 2 n -C
7
H
16 
+ 15O
2 
⇒ 14CO +
16H
2
O  
6.3 ×
10
11  
0.0  30,000.0  0.25  1.5 
II 2CO + O
2 
⇔ 2CO
2 
4.5 ×
10
10  
0.0  20,000.0  1.0  0.5  
Table 2 
Information about the gas phase and liquid phase in cases 1  3. T
0 
and p
0 
are 
total temperature and total pressure of carrier air, ϕ
t 
is total liquid fuel equiv -
alence ratio, T
0
d 
is temperature of droplets, d
0 
is mono-sized sprays with initial 
droplet diameter, d
0
s 
and d
0
l 
are initial droplet diameter of small droplets and 
large droplets in bi-disperse sprays.  
Case Gas phase Liquid phase  
T
0
(K)  p
0
(atm)  ϕ
t  
T
0
d
(K)  d
0
( μ m)  d
0
s
( μ m)  d
0
l
( μ m)  
1 700 30 1 323 2 – – 
2 10 – – 
3 – 2 10  
S. Jin et al.

<!-- PDF_PAGE: 6 -->

Fuel 314 (2022) 123087
6
detonation flow field, including detonation wave, oblique shock wave, 
slip line and deflagration surface, are well predicted, as marked in Fig. 2 
(b). The triangular fuel refilling area is generally regular, and thereby 
liquid fuel evaporation and fuel vapor / oxidizer mixing can proceed 
therein. The average detonation propagation velocity of the detonation 
wave under the current condition is about 1760 m/s, which is lower than 
the purely gaseous RDW speed (1830 m/s) under the same pressure and 
total temperature conditions. The C-J speed in the corresponding 
gaseous conditions is 1835.7 m/s. As such, the velocity deficits are 3.8% 
and 4.1%, respectively. 
Fig. 3 further shows the enlarged views about the distributions of 
Heat Release Rate (HRR), Evaporation Rate (ER), n -C
7
H
16 
vapor mass 
fraction, pressure gradient magnitude, Lagrangian droplet temperature 
and diameter near the detonation wave in Fig. 2 . Note that in Fig. 3 (b) 
the evaporation rate is the volumetric source term S
m 
in Eq. (11) and 
therefore it is a Eulerian quantity. One can see from Fig. 3 (a) that high 
heat release rate can be found along the detonation wave, except near 
the triple point. There, the leading shock (solid line) and reaction front 
(with high HRR) are decoupled. This is because the fuel vapor ahead of it 
has been consumed by the deflagration surface. 
After being injected into the combustor, the n -heptane droplets are 
quickly heated close to the saturation temperature (see Fig. 3 e, about 
540 K) and then start to vaporize quickly and therefore considerable 
evaporation can be observed near the injector with fast reduction of the 
droplet size, demonstrated in Fig. 3 (b) and 3(f). The height of the 
evaporating droplet layer is small, about 1.5 mm, beyond which no 
droplets exist. In the fuel filling area, the resultant n -heptane vapor mass 
fraction is close to stoichiometry (about 6.02%, see Fig. 3 c), indicating 
the complete evaporation of the liquid fuels. One can also see from Fig. 3 
(c) that the fuel vapor mass fraction is relatively uniform ahead of the 
RDW, which implies the efficient mixing of the fuel vapor and oxidizer 
inside the refilling area. Moreover, it is shown from Fig. 3 (c), 3(e) and 3 
(f) that there are no n -heptane droplets behind the detonation wave, and 
therefore all the fuels have been consumed by the rotating detonation 
wave or deflagration surface. 
Fig. 4 shows the contours of pressure and gas temperature in case 2, 
in which the initial droplet diameter d
0 
is increased to 10 μ m. In this 
case, the detonation wave is quenched after propagating after about 5 
cycles. The transient extinction process will be discussed in detail in 
Section 3.2 . Briefly, the fuel refilling area becomes less organized, 
compared to that in case 1. No pronounced temperature rise is observed 
along the interface between the fuel refilling area and burned product 
gas. This indicates that less deflagrative combustion occurs due to 
insufficient fuel vapor. Moreover, the leading shock wave becomes 
oblique and is reflected at the inlet. Since the pressure immediately 
behind the RDW is higher than the total pressure, based on our gas in -
jection method [15,16] , it is assumed to be a solid wall. This reflected 
shock is almost parallel to the oblique shock connected with the leading 
shock. 
Fig. 2. Contours of (a) pressure and (b) gas temperature. d
0 
= 2 µ m and ϕ
t 
= 1.0. 
Fig. 3. Contours of (a) heat release rate, (b) evaporation rate, (c) n -heptane 
vapor mass fraction, (d) pressure gradient magnitude, (e) droplet temperature 
and (f) diameter. d
0 
= 2 µ m and ϕ
t 
= 1.0. Solid line: detonation and oblique 
shock waves. 
Fig. 4. Contours of (a) pressure and (b) gas temperature. d
0 
= 10 µ m and ϕ
t 
= 1.0. 
S. Jin et al.

<!-- PDF_PAGE: 7 -->

Fuel 314 (2022) 123087
7
Fig. 5 shows the distributions of HRR, ER, n -C
7
H
16 
vapor mass 
fraction, pressure gradient magnitude, Lagrangian droplet temperature 
and diameter around the detonation wave corresponding to the same 
instant in Fig. 4 . The HRR contour in Fig. 5 (a) shows that the detonative 
combustion only proceeds behind a small fraction of the leading shock, 
roughly corresponding to the downstream ( y > 0.006 m) of the fuel 
refilling area. When y < 0.006 m, finite distance between the leading 
shock wave and reaction front can be seen, and therefore no detonations 
occur there. However, one can find that a Secondary Rotating Detona -
tion Wave (SRDW) exists near the injector. This phenomenon is also 
reported by Ren and Zheng [14] in liquid kerosene RDE. The formation 
of SRDW can be attributed to: (1) existence of the reflected shock wave; 
(2) sufficient n -heptane vapor ahead of the reflected shock wave (behind 
the leading shock). The second reason can be more clearly shown in 
Fig. 5 (b) and 5(c), through which high evaporation rate and fuel vapor 
concentration can be found between the reflected and leading shocks. 
How the secondary rotating detonation wave evolves during a detona -
tion extinction process will be further interpreted in Section 3.2 . In this 
case, the height of the evaporating droplet distribution zone is much 
higher than that in case 1, because larger droplets may have longer 
heating and evaporation timescales. 
Plotted in Fig. 6 are the contours of pressure and gas temperature in 
the bidisperse sprays, i.e., case 3. Similar to the results of case 2 in Fig. 5 , 
the leading shock wave is inclined, and a reflected shock wave is present. 
However, different from case 2, case 3 is characterized by continuously 
rotating detonation propagation across the model RDE chamber. 
Although the RDW are stable both in cases 1 and 3, nevertheless, the 
morphology of the RDW is different, which can be more clearly seen in 
Fig. 7 . 
Fig. 7 shows zoomed contours of the HRR, ER, n -C
7
H
16 
vapor mass 
fraction, pressure gradient magnitude, Lagrangian droplet temperature 
and diameter near the detonation wave in Fig. 6 . More heat release 
behind the leading shock wave can be found in Fig. 7 (a), compared to 
the counterpart results in Fig. 5 (a). This can confirm the effects of the 
small droplets in fuel vapor supply and hence sustain the detonative 
combustion. Likewise, local extinctions of the detonation wave can be 
also observed near the injector in Fig. 7 (a). A SRDW along the reflected 
Fig. 5. Contours of (a) heat release rate, (b) evaporation rate, (c) n -heptane 
vapor mass fraction, (d) pressure gradient magnitude, (e) droplet temperature 
and (f) diameter. d
0 
= 10 µ m and ϕ
t 
= 1.0. Solid line: detonation and oblique 
shock waves. 
Fig. 6. Contours of (a) pressure and (b) gas temperature. d
0
s 
= 2 μ m (50%), d
0
l 
= 10 μ m (50%), and ϕ
t 
= 1.0. 
Fig. 7. Contours of (a) heat release rate, (b) evaporation rate, (c) n -heptane 
vapor mass fraction, (d) pressure gradient magnitude, (e) droplet temperature 
and (f) diameter. d
0
s 
= 2 μ m (50%), d
0
l 
= 10 μ m (50%) and ϕ
t 
= 1.0. Solid line: 
detonation and oblique shock waves. 
S. Jin et al.

<!-- PDF_PAGE: 8 -->

Fuel 314 (2022) 123087
8
shock wave is also present, which is the same as that in Fig. 5 (a). The 
average detonation propagation speed is about 1750 m/s, slightly lower 
than that in Fig. 2 . In Fig. 7 , one can also see that the fuel droplets are 
dispersed almost in the entire fuel refilling area, and this is because 50% 
of the fuel sprays have larger diameter (10 μ m), which have longer 
heating and evaporation time in the fuel refilling area. 
3.2. RDW extinction in fuel sprays 
It has been shown from case 2 that the rotating detonative com -
bustion fueled with n -heptane sprays are quenched after propagating 
about five cycles. Their transient will be further discussed in this section, 
about how the main and secondary rotating detonation wave evolve. 
Fig. 8 demonstrates the time sequences of pressure and gas temperature 
during the detonation extinction process. At 1340 μ s (same as that in 
Fig. 4 ), the RDW still exists. From 1360 μ s to 1380 μ s, the height of the 
detonation wave gradually decreases. Moreover, since the pressure 
behind the detonation wave is higher than the total pressure of the inlet 
air, the fuel sprays cannot be injected into the combustor, which leads to 
a gradually reduced fuel filling area. From 1400 μ s to 1440 μ s, the RDW 
gradually becomes weak, which can be confirmed by the decreased 
temperature and pressure near the detonation wave. Eventually, the 
detonation wave is extinguished. 
Fig. 9 shows the evolutions of the HRR and ER corresponding to the 
above detonation extinction process. Fig. 9 (a) 9(f)  correspond to six 
instants in Fig. 8 (1340 μ s – 1440 μ s). It can be found that the detonation 
wave undergoes an extinction and re-ignition process. Specifically, at 
1340 μ s, due to the large droplet diameter, the droplets are unable to 
evaporate completely in the fuel refilling area and a large amount of 
evaporating droplets exist after the detonation wave. Existence of these 
droplets result in a high volumetric evaporation rate in this region. 
There is a significant discontinuity in the heat release rate on the 
detonation wave. The detonation wave experiences the first instanta -
neous extinction. 
From Fig. 9 (a) to 9(b), although the detonation wave is extinguished, 
the higher temperature after the wave allows the droplets to continue to 
evaporate and eventually cause the detonation wave to re-ignite. After 
that, the heat release behind the leading shock is more distributed, 
indicating the enhanced detonative combustion, as shown in Fig. 9 (b)- 
(d). Meanwhile, the number of evaporating droplets after the detonation 
wave gradually increases during this process and eventually leads 
another severe localized extinction of detonation combustion behind the 
Fig. 8. Extinction process of a detonation wave in n -heptane sprays. d
0 
= 10 µ m and ϕ
t 
= 1.0.  
S. Jin et al.

<!-- PDF_PAGE: 9 -->

Fuel 314 (2022) 123087
9
leading shock, as shown in Fig. 9 (e). Another extinction at 1440 μ s can 
be found in Fig. 9 (f). Eventually, the pressure wave is fully decoupled 
from the combustion wave and the detonation wave is extinguished. 
Moreover, the height of the secondary detonation wave from the re -
flected shock wave is low at 1340 μ s, about 2 mm (see Fig. 9 a). From 
1360 to 1380 μ s, as the detonation wave is reignited and gradually de -
velops, the height of the secondary detonation wave increases to 5 mm. 
The secondary detonation wave from the reflected shock also becomes 
quenched and at 1420 μ s, it is no longer observable in Fig. 9 (f). 
Comparing Fig. 5 and Fig. 7 , one can find that when the proportion of 
large droplets ϕ
l 
increases from 50% to 100%, number of the remaining 
droplets after the detonation wave increases significantly. These resid -
ual droplets can continue evaporate behind the detonation wave and the 
fuel vapour can burn locally with deflagration mode. In these cases, 
since the total equivalence ratio is the same (1.0), less fuel can be 
detonated if more fuel is deflagrated. Indeed, we can also see the 
evaporating droplets behind the detonation wave. However, their per -
centage is relatively low, and therefore the RDW can still maintain. 
3.3. Reactant mixing and detonated fuel fraction 
The structure and extinction process of RDW with mono-sized sprays 
have been discussed in Sections 3.1 and 3.2 . In Section 3.3 , the effects of 
larger droplet diameter ( d
0
l
) in the bi-disperse sprays on reactant mixing, 
effective equivalence ratio and detonated fuel fraction will be investi -
gated. Fig. 10 shows the contours of n -heptane vapor mass fraction and 
equivalence ratio from the cases of d
0
l 
= 5, 7.5 and 10 μ m, respectively. 
ϕ
l 
= 0.5 and d
0
s 
= 2 μ m. In this analysis, the effective equivalence ratio 
ϕ
eff 
is defined as the ratio of required stoichiometric oxygen atoms to the 
available oxygen atoms [53] . The former is defined as the minimum 
number of oxygen atoms demanded to convert all carbon and hydrogen 
atoms to CO
2 
and H
2
O, respectively [53] , i.e., 
ϕ
eff
=
n
C
+ n
H
/ 4
n
O
/ 2
, (15)  
where n
C
, n
H
, and n
O 
denote the number of available carbon, hydrogen 
and oxygen atoms, respectively. The reader should be reminded that 
since it is based on element conservation, ϕ
eff 
is also well defined in the 
detonation product area. However, the ones in the un-detonated mix -
tures (such as triangular fuel refilling area) are most relevant for our 
analysis. Also, only the atoms in the gas phase are considered and no 
contribution (such as hydrogen or carbon atoms) from the liquid fuels is 
included. 
One can see from Fig. 10 that, as d
0
l 
increases from 2 to 10 µ m, less 
vapor is released from the sprayed droplets intermediately after they are 
injected into the RDE chamber, resulting in less distributions of n -C
7
H
16 
vapor near the injectors. As the droplets gradually evaporate down -
stream of the fuel refilling area, gradual increase of the mass fraction of 
n -C
7
H
16 
vapor can be observed. This is particularly true for d
0
l 
≥ 5 µ m in 
Fig. 9. Time sequence of heat release rate (left column) and evaporation rate 
(right column) in a detonation extinction process in case 2. Solid line: deto -
nation and oblique shock waves. 
Fig. 10. Contours of (left column) n -heptane vapor mass fraction and (right column) effective equivalence ratio: (a) d
0
l 
= 2 μ m, (b) d
0
l 
= 5 μ m, (c) d
0
l 
= 7.5 μ m and (d) 
d
0
l 
= 10 μ m. ϕ
l 
= 0.5 and d
0
s 
= 2 μ m. Solid line: detonation and oblique shock waves. 
S. Jin et al.

<!-- PDF_PAGE: 10 -->

Fuel 314 (2022) 123087
10
Fig. 10 (b) – (d). The difference in droplet diameter can lead to a signifi -
cant difference in the time required for complete evaporation of the 
droplet. The difference in the distribution of n -C
7
H
16 
vapor in the fuel 
refilling area further results in a change of the angle of the detonation 
wave. As shown in Fig. 10 , the detonation wave propagates in a strati -
fied reactant mixtures along the detonation wave height direction, from 
fuel-lean, to stoichiometric, to spotty fuel-rich compositions along the 
deflagrative contact surface. Furthermore, in the fuel refilling area, the 
distance in the y -direction where the equivalence ratio reaches unity 
increases with the d
0
l
, which ultimately leads to an increase in the angle 
of the detonation wave with the size of the larger droplet class d
0
l
. n - 
Heptane vapor is accumulated near the contact surface between the 
refilled fuel and detonated product, particularly obvious in Fig. 10 (b) – 
(d). The reason for this peculiar phenomenon and its effects on rotating 
detonations have been explained in Ref. [16] . 
As shown in Fig. 10 , the similar tendencies of the n -heptane vapor 
inside the fuel refilling area can also been observed from the distribu -
tions of the effective equivalence ratio. For d
0
l 
= 2 µ m , overall unity 
equivalence ratio in the fuel refilling area is found, indicating the fast 
evaporation and efficient vapor/oxidizer mixing before the detonation 
wave arrives. However, for the rest cases, the equivalence ratio is almost 
zero near the top head, and gradually increases towards unity along the 
y -direction. This is consistent with the results of fuel vapor distributions 
discussed above. At the fuel-product contact surface, locally rich pockets 
can be found, with ϕ > 2.0. 
Fig. 11 further quantifies the average equivalence ratio as a function 
of the diameter d
0
l 
of the larger fuel droplet class. Different liquid fuel 
equivalence ratios 〈 ϕ
eff
〉 for larger droplet class are considered, i.e., ϕ
l 
=
0.2  1.0. Here the averaging is performed based on the fuel refilling 
area based on ten uncorrelated time instants. Since the droplet evapo -
ration is very limited when they are first injected into the combustor, 
equivalence ratio around the inlet is almost zero. This makes the average 
equivalence ratio 〈 ϕ
eff
〉 in the fuel filling area well below 1, with a 
maximum value of 0.66. As d
0
l 
increases, the evaporation rate of the 
droplets decreases and the area near the inlet with an equivalence ratio 
close to zero gradually increases. This makes the average equivalence 
ratio in the fuel filling area gradually decrease. 
In the calculation under different proportions of large droplets ϕ
l
, 
when the initial diameter of the larger droplet d
0
l 
increases to a certain 
value, the detonation wave cannot maintain stable propagation. The 
maximum droplet diameter before the extinction of the detonation wave 
is defined as the critical diameter in the following description. The 
extinction curve is obtained by marking the critical diameters at 
different ϕ
l
. Note that this curve is approximated and in our work we 
have not performed detailed trail-and-error method to get the accurate 
results for the extinction conditions. The extinction curve shows that the 
critical diameter gradually increases as the proportion of large droplets 
ϕ
l 
gradually decreases which indicates that decreasing the initial 
diameter of the droplet is conducive to maintain stable propagation of 
the detonation wave. 
To further interpret the premixedness of the reactants in liquid fueled 
rotating detonative combustion, the Flame Index ( FI ) is used here to 
identify the local combustion regimes, i.e., premixed ( FI = + 1) or non- 
premixed ( FI =  1) condition [54] . It is defined as 
FI =
∇ Y
F
∙ ∇ Y
O
|∇ Y
F
||∇ Y
O
|
(16)  
where Y
F 
and Y
O 
represent the mass fractions of gaseous n -heptane and 
oxygen, respectively. Fig. 12 shows the contours of flame index in the 
RDE combustor corresponding to the foregoing four cases. As shown in 
Fig. 12 (a) to 12(d), a value of  1 for FI is found in the fuel refilling area, 
which implies that the fuel and oxidizer mixing proceeds there. This is in 
line with the findings from Ref. [17] , although the inter-injector spacing 
is considered therein. However, the deflagration surface and detonation 
wave are dominated by premixed combustion ( FI = + 1). 
The detonated fuel fraction ψ [15,39] is further adopted to measure 
the percentage of the n -heptane fuel burned by the rotating detonation. 
It can be estimated from 
ψ =
∫
V
ω t
C
7
H
16
dv
∫
V
ω t
C
7
H
16
dv +
∫
V
ω f
C
7
H
16
dv
(17)  
where ω t
C
7
H
16 
and ω f
C
7
H
16 
are the volumetric consumption rates of 
detonated and deflagrated n -C
7
H
16
, respectively. V represents the 
computational domain. Note that the n -heptane fuel is deemed denoted 
(deflagrated) when the corresponding heat release rate is greater than or 
approximately equal to (less than) 10
13 
J/m
3
/s [55] . This value is 
determined from a stand-alone C-J n -heptane detonation calculation 
with The Shock & Detonation Toolbox [56] . When we slightly adjust the 
foregoing criterion around this numerical value, the obtained detonated 
fuel fraction is almost not affected. This shows the limited sensitivity of 
Fig. 11. Average equivalence ratio in the fuel refilling area as a function of the diameter of larger droplet class. d
0
s 
= 2 μ m and ϕ
t 
= 1.0.  
S. Jin et al.

<!-- PDF_PAGE: 11 -->

Fuel 314 (2022) 123087
11
ψ to the HRR criterion. 
Fig. 13 shows the change of detonated fuel fraction ψ as a function of 
the diameter d
0
l 
of the larger fuel droplet class. For comparison, the 
result of gaseous RDC with ϕ = 1.0 (i.e., full vaporization before injec -
tion) is also shown. The detonated fuel fraction ψ in the simulated liquid 
fuel RDE are 6%  18% lower than that (0.9) of the corresponding 
gaseous RDE. Overall, regardless of the larger droplet equivalence ratio 
ϕ
l
, the detonated fuel fraction ψ monotonically decreases with increased 
d
0
l
. This is because as the diameter d
0
l 
increases, the droplets do not 
evaporate quickly after being injected into the combustor. There are 
large amount of fuel droplets crossing the detonation wave and 
continuing evaporating there. The released vapor mixes with the local 
oxidizer and is deflagrated (HRR is below 10
13 
J/m
3
/s). As d
0
l 
increases, 
the droplets behind the detonation wave increases, which would lead to 
reduced detonated fuel fraction ψ . This trend is observed all the larger 
droplet equivalence ratio ϕ
l
. 
Moreover, as ϕ
l 
increases, from instance, from 0.2 to 1.0, the diam -
eter of the largest droplets with which a stable detonation wave can be 
sustained gradually decreases. Besides, under the same d
0
l 
( < 7.5 μ m), ψ 
increases as ϕ
l 
decreases. Decreased ϕ
l 
indicates increased fraction of 
small droplets ( d
0
s 
= 2 μ m) that can be fully evaporated and which can 
contribute towards the detonative combustion, which will increase ψ . 
3.4. Detonation wave propagation speed 
Fig. 14 shows the change of the detonation propagation speed with 
the diameter of the larger droplets d
0
l 
in bi-dispersed sprays. The total 
liquid fuel equivalence ratio ϕ
t 
is 1 for all considered cases. For com -
parison, the result of gaseous RDC with ϕ
t 
= 1.0 (i.e., full vaporization 
before injection) is also added. It is found that the detonation propa -
gation speeds from liquid fueled RDC are 4%-10% lower than that of the 
corresponding gaseous RDC. There may be different reasons for the 
speed deficits, such as nonuniform mixing of oxidizer and fuel in the fuel 
filling area, and heat or momentum exchange due to the droplets near 
the detonation front [17] . As d
0
l 
increases, the detonation propagation 
speed gradually decreases in all the cases with various ϕ
l
. This is because 
the larger the size of the fuel droplet, the lower the average equivalence 
ratio in the fuel filling area, and the propagation velocity of the deto -
nation wave decreases as the equivalence ratio decreases. Under the 
same equivalence ratio ϕ
l
, the small droplets can release more vapor 
than the large size droplets, and therefore the detonation propagation 
speed is higher. 
The RDW velocity deficit at different d
0
l 
is given in Fig. 15 . The ve -
locity deficit is calculated as δ v = ( v
g
 v
d
) / v
g
, where v
g 
is the velocity of 
gaseous detonation at the same total pressure and temperature, whist v
d 
is that of two-phase detonations at different d
0
l
. As shown in Fig. 15 , the 
Fig. 12. Contours of flame index in the combustor: (a) d
0
l 
= 2 μ m, (b) 5 μ m, (c) 7.5 μ m and (d) 10 μ m. ϕ
l 
= 0.5 and d
0
s 
= 2 μ m.  
Fig. 13. Detonated fuel fraction as a function of the diameter of larger droplets. d
0
s 
= 2 μ m and ϕ
t 
= 1.0.  
S. Jin et al.

<!-- PDF_PAGE: 12 -->

Fuel 314 (2022) 123087
12
droplets need to evaporate into gaseous n -heptane mixing with air in the 
fuel refilling area, which makes the distribution of the equivalence ratio 
in the fuel refilling area non-uniform, as shown in Fig. 10 . This non- 
uniform distribution makes the speed of the detonation wave lower 
than that of the gaseous detonation under the same conditions. As d
0
l 
increases, n -heptane vapor yield in the fuel refilling area decreases, and 
accordingly the equivalence ratio in the fuel-refilling area decreases, 
which makes the detonation wave speed decrease and the velocity 
deficit increases. Moreover, as the equivalence ratio of lager droplet 
classes ϕ
l 
increases, the number of droplets increases, the equivalence 
ratio in the fuel-refilling area decreases, and hence the velocity deficit 
gradually increases. 
3.5. Propulsion performance 
The droplet diameter and spatial distribution in the RDE chamber 
not only affect the detonation wave propagation, but also the propulsion 
performance resulting from the detonation combustion. To this end, the 
specific impulse I
sp 
is calculated 
I
sp
=
∫
A o
[
ρ u
2
+ ( p  p
b
)
]
dA
o
/ g ˙m
F
(18)  
in which A
o 
is the area of the outlet, u is the gas velocity at the outlet, ˙m
F 
is the mass flow rate of the fuel, g is gravity acceleration, p is the local 
pressure at the outlet, and p
b 
is the backpressure. Fig. 16 shows the effect 
of diameter d
0
l 
and equivalence ratio ϕ
l 
of the larger droplet class on the 
specific impulse I
sp
. Specifically, for a given equivalence ratio (such as ϕ
l 
= 0.5), as d
0
l 
increases, the specific impulse gradually decreases. This is 
because as d
0
l 
increases, when the droplets are sprayed into the 
combustor, they cannot quickly evaporate into a gaseous state. This 
further affects the overall ratio of detonation combustion and hence 
reduces specific impulse. For a fixed diameter of larger droplet class 
(such as d
0
l 
= 5 μ m), as ϕ
l 
increases, the number of droplets with a 
diameter of 2 μ m decreases, which means that the number of droplets 
that can completely evaporate into fuel vapor in the fuel refilling area 
decreases. The decrease in the number of droplets decreases the average 
equivalence ratio in the fuel refilling area, which leads to a decrease in 
specific impulse. 
The thrust force from the kinetic energy and pressure gain in rotating 
Fig. 14. Detonation wave speed as a function of the droplet diameter. d
0
s 
= 2 μ m and ϕ
t 
= 1.0.  
Fig. 15. Velocity deficit as a function of the droplet diameter. d
0
s 
= 2 μ m and ϕ
t 
= 1.0.  
S. Jin et al.

<!-- PDF_PAGE: 13 -->

Fuel 314 (2022) 123087
13
detonations are also shown in Fig. 17 . The thrust from kinetic energy is 
defined as F
u
=
∫
A
o
ρ u
2
dA
o
, whilst the thrust from pressure gain is F
p
=
∫
A
o
( p  p
b
) dA
o
. The thrust from kinetic energy includes the thrust 
generated by combustion products as well as by the propellant itself. The 
thrust generated by combustion products is the thrust from the pressure 
gain and it is the more important one in the two types of thrust described 
above, which can be clearly observed in the Fig. 17 . The thrust force 
from pressure gain F
p 
decreases significantly with the droplet diameter 
d
0
l
. As d
0
l 
increases, the droplet evaporation rate decreases, and the un -
burned droplets after the detonation wave gradually increases, resulting 
in deflagration combustion of n -heptane vapor near the slip line. This 
reduces the detonated fuel fraction ψ (see Eq. (17) ) and eventually leads 
to a decrease in thrust. For a fixed diameter of larger droplet class (such 
as d
0
l 
= 5 μ m), as ϕ
l 
increases, the average equivalence ratio 〈 ϕ
eff
〉 in the 
fuel refilling area decreases, which leads to a decrease in the detonated 
fuel fraction and ultimately to a decrease in thrust from pressure gain. 
Since the propellant flow rate is not changed in the calculations of this 
study, this means that the kinetic energy of the propellant produces 
almost no change in thrust for different operating conditions, so the 
trend of F
u 
is the same as F
p
. 
From the above results, we can see that droplet diameter and the 
mass ratio of the larger droplet class are important factors for droplet 
evaporation and heating, thereby stabilizing the two-phase rotating 
detonations. Specifically, if both d
0
l 
and ϕ
l 
are high (such as case 2 in 
Section 3.1 ), the detonation wave would extinguish due to relatively 
slow evaporation rate. If both d
0
l 
and ϕ
l 
are small (such as case 1), the 
detonation wave can propagate stably due to sufficient fuel vapour 
supply from the liquid fuels and the propagation and propulsion char -
acteristics of the detonation wave are higher than other conditions (the 
d
0
l 
is small but ϕ
l 
is high or d
0
l 
is high but ϕ
l 
is small, as will be shown 
later). If the d
0
l 
is small but ϕ
l 
is high or d
0
l 
is high but ϕ
l 
is small, 
although the remaining droplets can be observed after the detonation 
wave, the propagation of the detonation wave is still stable from our 
simulated case. This, to some degree, corroborates the role of the fine 
droplet class in stabilizing the detonation wave. However, the propa -
gation and propulsion characteristics of the detonation wave are lower 
than those of case 1 in which both d
0
l 
and ϕ
l 
are small. 
Fig. 16. Specific impulse as a function of droplet diameter. d
0
s 
= 2 μ m and ϕ
t 
= 1.0.  
Fig. 17. Thrust force from (a) kinetic energy and (b) pressure gain. d
0
s 
= 2 μ m and ϕ
t 
= 1.0.  
S. Jin et al.

<!-- PDF_PAGE: 14 -->

Fuel 314 (2022) 123087
14
4. Conclusions 
Two-dimensional rotating detonations fueled by liquid n -heptane 
sprays are simulated with Eulerian  Lagrangian method. Bi-disperse 
fuel droplets without any fuel pre-vaporization are considered in our 
work and paramettric studies are performed to clarify the influences of 
liquid fuel droplet diameter and equivlance ratio on rotating detonation 
wave propagation, reactant mixing and propulsion performance. 
In mono-sized sprays, when the droplet diameter is small (2 μ m), the 
n -heptane droplets can completely evaporate in the fuel refilling area. 
While droplet diameter increases, a reflected shock can be obsevered 
after the detonation wave and the larger droplets can not completely 
evaporate in the fuel refilling area and exist behind the detonation wave. 
When the droplet diameter is > 10 μ m, the higher pressure after the 
detonation wave leads to the reactants can not be sprayed into the 
combustor eventually leading to the extinction of the detonation wave. 
In bi-disperse sprays with 50% droplets of d
0
s 
= 2 μ m and 50% large 
droplets of d
0
l 
= 10 μ m, the presence of droplets with small diameter 
maintains the stable propagation of the detonation wave, while reflected 
shock is also observed. 
The incomplete evaporation of droplets in the fuel filling area near 
the inlet of the RDC leads to an average equivalence ratio in the fuel 
refilling area ( ϕ
eff
) lower than ϕ
t
. ϕ
eff 
decreases with increasing d
0
l 
and 
the decreasing ϕ
eff 
leads to a decrease in the detonated fuel fraction with 
increased d
0
l
. The detonation propagation speeds from liquid fueled RDC 
are lower than that of the corresponding gaseous RDC. The increase in d
0
l 
and ϕ
l 
raise the velocity deficit. Finally, d
0
l 
and ϕ
l 
also affect the thrust 
and specific impulse of the RDC. The propulsive performance decreases 
with increased d
0
l 
and ϕ
l
. 
CRediT authorship contribution statement 
Shan Jin: Conceptualization, Methodology, Writing – original draft, 
Visualization, Investigation. Huangwei Zhang: Writing – review & 
editing, Supervision, Project administration, Funding acquisition. 
Ningbo Zhao: Supervision. Hongtao Zheng: Supervision. 
Declaration of Competing Interest 
The authors declare that they have no known competing financial 
interests or personal relationships that could have appeared to influence 
the work reported in this paper. 
Acknowledgements 
The simulations used the ASPIRE 1 Cluster from National Super -
computing Centre, Singapore (NSCC) (https://www.nscc.sg/). SJ is 
supported by China Scholarship Council (No. 202006680045). HZ is 
supported by MOE Tier 1 grant (R-265-000-653-114). Discussion with 
Dr Majie Zhao from Beijing Institute of Technology is gratefully 
acknowledged. 
References 
[1] Wola ´nski P. Detonative propulsion. Proc Combust Inst 2013;34(1):125 – 58 . 
[2] Anand V, Gutmark E. Rotating detonation combustors and their similarities to 
rocket instabilities. Prog Energy Combust Sci 2019;73:182 – 234 . 
[3] Bykovskii FA, Zhdan SA, Vedernikov EF. Continuous spin detonations. J Propuls 
Power 2006;22(6):1204 – 16. https://doi.org/10.2514/1.17656 . 
[4] Rankin BA, Richardson DR, Caswell AW, Naples AG, Hoke JL, Schauer FR. 
Chemiluminescence imaging of an optically accessible non-premixed rotating 
detonation engine. Combust Flame 2017;176:12 – 22. https://doi.org/10.1016/j. 
combustflame.2016.09.020 . 
[5] Bykovskii FA, Zhdan SA, Vedernikov EF. Continuous spin detonation of fuel-air 
mixtures. Combust Explos Shock Waves 2006;42(4):463 – 71. https://doi.org/ 
10.1007/s10573-006-0076-9 . 
[6] Shen P-W, Adamson Jr TC. Theoretical analysis of a rotating two-phase detonation 
in liquid rocket motors. NASA 1972 . 
[7] Bykovskii FA, Zhdan SA, Vedernikov EF. Continuous spin detonation of a 
heterogeneous kerosene – air mixture with addition of hydrogen. Combust Explos 
Shock Waves 2016;52(3):371 – 3 . 
[8] Bykovskii FA, Zhdan SA, Vedernikov EF. Continuous detonation of the liquid 
kerosene — air mixture with addition of hydrogen or syngas. Combust Explos Shock 
Waves 2019;55(5):589 – 98 . 
[9] Kindracki J. Experimental studies of kerosene injection into a model of a 
detonation chamber. J Power Technol 2012;92:80 – 9 . 
[10] Kindracki J. Experimental research on rotating detonation in liquid fuel – gaseous 
air mixtures. Aerosp Sci Technol 2015;43:445 – 53 . 
[11] Wola ´nski P, Balicki W, Perkowski W, Bilar A. Experimental research of liquid- 
fueled continuously rotating detonation chamber. Shock Waves 2021;31(7): 
807 – 12 . 
[12] Sun Bo, Ma Hu. Two-dimensional numerical study of two-phase rotating 
detonation wave with different injections. AIP Adv 2019;9(11):115307 . 
[13] Hayashi AK, Tsuboi N, Dzieminska E. Numerical study on JP-10/air detonation and 
rotating detonation engine. AIAA J 2020;58(12):5078 – 94 . 
[14] Ren Z, Zheng L. Numerical study on rotating detonation stability in two-phase 
kerosene-air mixture. Combust Flame 2021;231:111484 . 
[15] Meng Q, Zhao M, Zheng H, Zhang H. Eulerian-Lagrangian modelling of rotating 
detonative combustion in partially pre-vaporized n-heptane sprays with hydrogen 
addition. Fuel 2021;290:119808 . 
[16] Meng Q, Zhao N, Zhang H. On the distributions of fuel droplets and in situ vapor in 
rotating detonation combustion with prevaporized n-heptane sprays. Phys Fluids 
2021;33(4):043307 . 
[17] Zhao M, Zhang H. Rotating detonative combustion in partially pre-vaporized dilute 
n-heptane sprays: droplet size and equivalence ratio effects. Fuel 2021;304: 
121481 . 
[18] Smirnov NN, Nikitin VF, Dushin VR, Filippov YG, Nerchenko VA, Khadem J. 
Combustion onset in non-uniform dispersed mixtures. Acta Astronaut 2015;115: 
94 – 101 . 
[19] Smirnov NN, Betelin VB, Kushnirenko AG, Nikitin VF, Dushin VR, Nerchenko VA. 
Ignition of fuel sprays by shock wave mathematical modeling and numerical 
simulation. Acta Astronaut 2013;87:14 – 29 . 
[20] Betelin VB, Smirnov NN, Nikitin VF, Dushin VR, Kushnirenko AG, Nerchenko VA. 
Evaporation and ignition of droplets in combustion chambers modeling and 
simulation. Acta Astronaut 2012;70:23 – 35 . 
[21] Smirnov NN, Nikitin VF, Khadem J, Alyari-Shourekhdeli Sh. Onset of detonation in 
polydispersed fuel – air mixtures. Proc Combust Inst 2007;31(2):2195 – 204 . 
[22] Reid RC, Prausnitz JM, Poling BE. The properties of gases and liquids. McGraw Hill 
Book; 1987 . 
[23] McBride BJ. Coefficients for calculating thermodynamic and transport properties of 
individual species. Natl Aeron Space Administr 1993;4513 . 
[24] Crowe CT, Sharma MP, Stock DE. The particle-source-in cell (PSI-CELL) model for 
gas-droplet flows 1977;99:325 – 32. 
[25] Sazhin SS. Advanced models of fuel droplet heating and evaporation. Prog Energy 
Combust Sci 2006;32(2):162 – 214 . 
[26] Tyurenkova VV. Non-equilibrium diffusion combustion of a fuel droplet. Acta 
Astronaut 2012;75:78 – 84 . 
[27] Tyurenkova V. Two regimes of a single n-heptane droplet combustion. Acta 
Astronaut 2019;163:25 – 32 . 
[28] Abramzon B, Sirignano WA. Droplet vaporization model for spray combustion 
calculations. Int J Heat Mass Transf 1989;32(9):1605 – 18 . 
[29] Fuller EN, Schettler PD, Giddings JC. A new method for prediction of binary gas- 
phase diffusion coefficients. Ind Eng Chem 1966;58(5):18 – 27 . 
[30] Liu AB, Mather D, Reitz RD. Modeling the effects of drop drag and breakup on fuel 
sprays. SAE Trans 1993:83 – 95 . 
[31] Naumann Z, Schiller L. A drag coefficient correlation. Z Ver Deutsch Ing 1935;77: 
318 – 23 . 
[32] Ranz WE, W. R. Marshall J. Evaporation from Drops, Part I. Chem Eng Prog 1952; 
48:141 – 6. 
[33] Xu Y, Zhao M, Zhang H. Extinction of incident hydrogen/air detonation in fine 
water sprays. Phys Fluids 2021;33(11):116109 . 
[34] Sato T, Chacon F, White L, Raman V, Gamba M. Mixing and detonation structure in 
a rotating detonation engine with an axial air inlet. Proc Combust Inst 2021;38(3): 
3769 – 76 . 
[35] Betelin VB, Nikitin VF, Mikhalchenko EV. 3D numerical modeling of a cylindrical 
RDE with an inner body extending out of the nozzle. Acta Astronaut 2020;176: 
628 – 46 . 
[36] Smirnov NN, Nikitin VF, Stamov LI, Mikhalchenko EV, Tyurenkova VV. Three- 
dimensional modeling of rotating detonation in a ramjet engine. Acta Astronaut 
2019;163:168 – 76 . 
[37] Smirnov NN, Nikitin VF, Stamov LI, Mikhalchenko EV, Tyurenkova VV. Rotating 
detonation in a ramjet engine three-dimensional modeling. Aerosp Sci Technol 
2018;81:213 – 24 . 
[38] Hishida M, Fujiwara T, Wolanski P. Fundamentals of rotating detonations. Shock 
Waves 2009;19(1):1 – 10 . 
[39] Zhao M, Cleary MJ, Zhang H. Combustion mode and wave multiplicity in rotating 
detonative combustion with separate reactant injection. Combust Flame 2021;225: 
291 – 304 . 
[40] Zhang H, RYrhoCentralFOAM, https://blog.nus.edu.sg/huangwei/nus- 
ryrhocentralfoam-solver/, National University of Singapore. 
[41] Greenshields CJ, Weller HG, Gasparini L, Reese JM. Implementation of semi- 
discrete, non-staggered central schemes in a colocated, polyhedral, finite volume 
framework, for high-speed viscous flows. Int J Numer Methods Fluids 2010;63: 
1 – 21 . 
S. Jin et al.

<!-- PDF_PAGE: 15 -->

Fuel 314 (2022) 123087
15
[42] Huang Z, Zhao M, Xu Y, Li G, Zhang H. Eulerian-Lagrangian modelling of 
detonative combustion in two-phase gas-droplet mixtures with OpenFOAM: 
Validations and verifications. Fuel 2021;286:119402. 
[43] Zhang H, Zhao M, Huang Z. Large eddy simulation of turbulent supersonic 
hydrogen flames with OpenFOAM. Fuel 2020;282:118812. 
[44] Zhao M, Ren Z, Zhang H. Pulsating detonative combustion in n-heptane/air 
mixtures under off-stoichiometric conditions. Combust Flame 2021;226:285–301. 
[45] Liu S, Hewson JC, Chen JH, Pitsch H. Effects of strain rate on high-pressure 
nonpremixed n-heptane autoignition in counterflow. Combust Flame 2004;137(3): 
320–39. 
[46] Reitz RD. Modeling atomization processes in high-pressure vaporizing sprays. At 
Spray Technol 1987;3:309–37. 
[47] Crowe CT, Sommerfeld M, Tsuji Y. Multiphase flows with particles and droplets. 
New York: CRC Press; 1998. 
[48] Watanabe H, Matsuo A, Matsuoka K, Kawasaki A, Kasahara J. Numerical 
investigation on propagation behavior of gaseous detonation in water spray. Proc 
Combust Inst 2019;37(3):3617–26. 
[49] Sontheimer M, Kronenburg A, Stein OT. Grid dependence of evaporation rates in 
Euler-Lagrange simulations of dilute sprays. Combust Flame 2021;232:111515. 
[50] Luo K, Desjardins O, Pitsch H. DNS of droplet evaporation and combustion in a 
swirling combustor. Cent Turbul Res Annu Res Briefs 2008:253–65. 
[51] Smirnov NN, Betelin VB, Nikitin VF, Stamov LI, Altoukhov DI. Accumulation of 
errors in numerical simulations of chemically reacting gas dynamics. Acta 
Astronaut 2015;117:338–55. 
[52] Smirnov NN, Betelin VB, Shagaliev RM, Nikitin VF, Belyakov IM, Deryuguin YN, 
et al. Hydrogen fuel rocket engines simulation using LOGOS code. Int J Hydrogen 
Energy 2014;39(20):10748–56. 
[53] Zhou R, Hochgreb S. The behaviour of laminar stratified methane/air flames in 
counterflow. Combust Flame 2013;160(6):1070–82. 
[54] Yamashita H, Shimada M, Takeno T. A numerical study on flame stability at the 
transition point of jet diffusion flames. Symp Combust 1996;26(1):27–34. 
[55] Zhao M, Li J-M, Teo CJ, Khoo BC, Zhang H. Effects of variable total pressures on 
instability and extinction of rotating detonation combustion. Flow, Turbul 
Combust 2020;104(1):261–90. 
[56] Shepherd J. Shock and Detonation Toolbox. https://shepherd.caltech.edu/EDL/ 
Public Resources/sdt/. 
S. Jin et al.
