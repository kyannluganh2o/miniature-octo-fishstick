<!-- PDF_PAGE: 1 -->

Fuel 290 (2021) 119808
Available online 4 December 2020
0016-2361/© 2020 Elsevier Ltd. All rights reserved.
Full Length Article 
Eulerian  Lagrangian modelling of rotating detonative combustion in 
partially pre-vaporized n -heptane sprays with hydrogen addition 
Qingyang Meng
a , b
, Majie Zhao
b
, Hongtao Zheng
a
, Huangwei Zhang
b , * 
a
College of Power and Energy Engineering, Harbin Engineering University, Harbin 150001, China 
b
Department of Mechanical Engineering, National University of Singapore, 9 Engineering Drive 1, Singapore 117576, Republic of Singapore   
ARTICLE INFO  
Keywords: 
Rotating detonation combustion 
n -Heptane 
Hydrogen 
Fuel spray 
Pre-vaporization 
Eulerian – Lagrangian modelling 
ABSTRACT  
Rotating detonation combustion (RDC) fuelled with partially pre-vaporized n -heptane sprays and gaseous 
hydrogen is studied with an Eulerian  Lagrangian method and a simplified two-dimensional model. Our focus is 
the effects of various pre-vaporized n -heptane equivalence ratios and droplet diameters on detonation wave 
propagation and droplet dynamics in two-phase RDC. The results show that when the droplets are small, they are 
fully vaporized by the detonation wave. However, when the droplet diameter is relatively large and/or the 
detonation wave number is bifurcated, liquid droplets are observable beyond the refill zone. Moreover, the 
detonation speed is considerably influenced by the droplet pre-vaporization and diameter. The velocity deficits 
from our simulated two-phase RDC vary between 5% and 30%. Over 70% n -heptane is detonated in the simu -
lated cases, and it is found that there exists a critical droplet diameter (about 20 µ m), around which the deto -
nated fuel fraction is minimal. Four droplet trajectories in RDC are identified, which are differentiated by various 
evaporation times, residence times and interactions between droplets and the basic RDC flow structures. Inside 
the refill zone, three droplet categories are qualitatively identified. Droplets injected at the right end of the refill 
zone directly interact with the deflagration surface and meanwhile have relatively long residence time. However, 
droplets injected closer to the travelling detonation front have insufficient time to be heated and vaporized. 
Novel technologies and implementations may be needed to enhance the in-situ droplet evaporation during the 
refill period in practical liquid fuelled RDE ’ s. Our results also demonstrate that when pre-vaporization level is 
low and initial droplet diameter is large, the liquid fuel droplets may disperse towards the combustor exit. 
Furthermore, the droplet dispersion height decreases with liquid fuel pre-vaporization, while increases with 
droplet diameter.   
1. Introduction 
Propulsive devices based on detonation combustion have attracted 
increased interests from the scientific and engineering communities in 
recent years, due to their higher thermodynamic efficiencies than those 
of deflagration-dominated engines [1,2] . Among the different detona -
tion engines, Rotating Detonation Engines (RDE) have numerous ad -
vantages, including simple ignition process, compact engine geometry 
and steady thrust output. Extensive studies have been conducted on 
RDE ’ s by means of experiments [3 – 5] , numerical simulations [6 – 13] 
and theoretical analysis [14 – 17] . 
Most of the existing RDE studies use gaseous fuels (e.g. hydrogen or 
ethylene) [1,2] . However, for practical applications, liquid fuels are 
more desirable, due to their small storage space, high energy density and 
extensive supply source. Early interests in liquid fuelled RDE ’ s date back 
to 1960s  70s [16] , which was mainly motivated by rocket propulsion 
technology development for space exploration in that era. In recent 
years, they have been revived, to develop novel pressure-gain combus -
tion technology, and a series of laboratory-scale RDE experiments have 
been successfully realized with various liquid fuels. For instance, 
Bykovskii et al. [18 – 20] achieved two-phase Rotating Detonation 
Combustion (RDC) by spraying liquid kerosene. In their tests with an 
annular cylindrical combustor (diameter 306 mm), the oxygen-enriched 
air should be used as the oxidant to initiate the detonation [18] . More 
recently, hydrogen or syngas is added in their experiments with a larger 
combustor (diameter 503 mm) using standard air and kerosene sprays 
[19,20] . In this combustor, Rotating Detonation Waves (RDW ’ s) cannot 
be initiated without gaseous hydrogen or syngas. They systematically 
* Corresponding author. 
E-mail address: huangwei.zhang@nus.edu.sg (H. Zhang).  
Contents lists available at ScienceDirect 
Fuel 
journal homepag e: www.else vier.com/loc ate/fuel 
https://doi.org/10.1016/j.fuel.2020.119808 
Received 9 July 2020; Received in revised form 5 November 2020; Accepted 18 November 2020

<!-- PDF_PAGE: 2 -->

Fuel 290 (2021) 119808
2
discussed the RDW propagation characteristics and propulsive perfor -
mance of liquid kerosene fuelled RDE ’ s [19,20] . 
In addition, Kindracki [21] investigated kerosene atomization 
characteristics in cold nitrogen flows by changing nitrogen velocity and 
fuel injection pattern of a model detonation chamber. They found that 
most of the droplets in their experiments have diameters of 20  40 µ m , 
which can quickly evaporate and form a combustible mixture in the 
chamber. Kindracki [22] used liquid kerosene and gaseous air to study 
initiation and propagation of RDW ’ s. In his work, continuous propaga -
tion of detonation wave was successfully achieved for a mixture of liquid 
kerosene and air and a small addition of hydrogen. Velocity deficits of 
20  25% are observed for his studied heterogeneous mixtures. 
Li et al. [23] investigated the RDW behaviours in both premixed and 
non-premixed injection schemes by using vaporized Jet A-1 and pre- 
heated air. The RDW ’ s stabilize with both injection methods. They 
also tested the RDC at cold starting, i.e. without air pre-heating, and it 
turns out that the detonation initiation is not successful, characterized 
by non-periodic pressure signals within the operating period. Further -
more, based on a rocket-type combustor, Xue et al. [24] used liquid 
nitrogen TetrOxide (NTO) and liquid MonomethylHydrazine (MMH) as 
the propellants to study the RDW propagation mode under different 
mass flow rates and outlet structures. This experiment is a preliminary 
demonstration of the feasibility of RDE ’ s with liquid hypergolic 
propellants. 
The foregoing experimental studies have provided significant sci -
entific insights about the two-phase RDC. However, detailed informa -
tion about detonation and flow fields (e.g. droplet evaporation and fuel 
vapour distributions) inside the channel are difficult to be measured. 
Alternatively, numerical simulation based on reacting two-phase flows 
is a promising tool for understanding fundamental physics and assisting 
practical design of liquid fuelled RDE ’ s. For instance, based on Euler -
ian  Lagrangian method, Sun and Ma [9] used octane and air as the 
reactants to numerically investigate the effects of air total temperature 
and fuel inlet spacing on the two-phase RDW. They found that increasing 
the fuel inlet spacing results in reduction of RDW propagation speed. 
They also explored the upper limit of fuel inlet spacing (beyond which 
the RDW cannot propagate stably) and found that increasing air total 
temperature would increase the foregoing limit. 
More recently, Hayashi et al. [25] used two-fluid method to simulate 
the JP-10/air RDE ’ s with different droplet sizes (i.e. 1  10 μ m) and pre- 
evaporation factors (i.e. 0  100%). From their work, high liquid droplet 
densities are found along the contact surface between the fresh and 
burned gas. They also observed that the non-reactive fuel pockets behind 
the detonation wave and highlighted the possible detonation quenching 
mechanisms caused by the interactions between the detonation front 
and fuel droplets. Furthermore, we studied the rotating detonation 
combustion fueled by partially pre-vaporized n -heptane sprays [26] and 
found that the detonation speed decreases with droplet sizes and tends 
to be constant when the diameter is greater than 30 µ m. Meanwhile, the 
percentage of detonated n -heptane first decreases and then increases as 
the droplet diameter varies from 5 to 80 µ m . 
The objective of our work is to further clarify the physics of deto -
nation propagation and droplet dynamics in liquid n -heptane fuelled 
RDE ’ s. Specifically, we aim to work on the following three questions 
which are not answered in the previous work (e.g. [9,25,26] ): (1) How 
do the droplet size and pre-evaporation affect the detonation propaga -
tion? (2) What are the percentages of the detonated fuels? (3) How are 
the droplets distributed in the RDE combustor? To this end, two- 
dimensional rotating detonative combustion is simulated based on a 
simplified RDC model and a hybrid Eulerian  Lanrangian approach. The 
reactants are partially pre-vaporized liquid n -heptane sprays with 
addition of stoichiometric hydrogen/air gas. The n -heptane droplet sizes 
and pre-vaporized gas equivalence ratios are varied to study their effects 
on the RDW characteristics and the droplet behaviours in the RDE 
chamber. Besides the above novel efforts, the droplet trajectories in the 
RDE chamber and the various timescales will also be discussed in this 
work. 
The structure of the manuscript is organized as below. The governing 
equation and computational method are detailed in Section 2 . The 
physical model and simulated cases are introduced in Section 3 . The 
mesh sensitivity and simulation results will be discussed in Sections 4 
and 5 , respectively. Section 6 closes the manuscript with the main 
conclusions. 
2. Governing equation and computational method 
2.1. Governing equation for gas phase 
The governing equations of mass, momentum, energy, and species 
mass fraction, with the ideal gas equation of state, for the compressible 
reacting two-phase flows are solved in this work. They respectively read 
∂ρ
∂ t
+ ∇ ∙ [ ρ u ] = S
mass
, (1)  
∂ ( ρ u )
∂ t
+ ∇ ∙ [ u ( ρ u ) ] + ∇ p + ∇ ∙ T = S
mom
, (2)  
∂ ( ρ E )
∂ t
+ ∇ ∙ [ u ( ρ E + p ) ] + ∇ ∙ [ T ∙ u ] + ∇ ∙ j = ˙ω
T
+ S
energy
, (3)  
∂ ( ρ Y
m
)
∂ t
+ ∇ ∙ [ u ( ρ Y
m
) ] + ∇ ∙ s
m
= ˙ω
m
+ S
species , m
, ( m = 1 , ⋯ M  1 ) , (4)  
p = ρ RT . (5) 
In above equations, t is time, ∇ ∙ ( ∙ ) is the divergence operator. ρ is 
the density, u is the velocity vector, T is the gas temperature, p is the 
pressure and updated from the equation of state, i.e. Eq. (5) . Y
m 
is the 
mass fraction of m -th species, M is the total species number. Only ( M  1) 
equations are solved in Eq. (4) and the mass fraction of the inert species 
(e.g. nitrogen) can be recovered from 
∑
M
m = 1
Y
m
= 1. E is the total energy, 
defined as E = e +| u |
2
/ 2 with e being the specific internal energy. R in 
Eq. (5) is specific gas constant and is calculated from R =
R
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
=
8 . 314 J/(mol ∙ K) is universal gas constant. The source terms in Eqs. (1) 
(4) , i.e. S
mass
, S
mom
, S
energy 
and S
species , m
, account for the exchanges of mass, 
momentum, energy and species. Their corresponding expressions are 
given in Eqs. (26)  (29) , respectively. 
The viscous stress tensor T in Eq. (2) modelled by 
T =  2 μ dev ( D ) . (6) 
Here μ is dynamic viscosity and is dependent on gas temperature 
following the Sutherland ’ s law [27] . Moreover, D ≡
[
∇ u +(∇ u )
T
]/
2 is 
the deformation gradient tensor and its deviatoric component in Eq. (6) , 
i.e. dev ( D ) , is defined as dev ( D ) ≡ D  tr ( D ) I / 3 with I being the unit 
tensor. 
In addition, j in Eq. (3) is the diffusive heat flux and can be repre -
sented by Fourier ’ s law, i.e. 
j =  k ∇ T . (7) 
Thermal conductivity k is calculated using the Eucken approxima -
tion [28] , i.e. k = μ C
v
( 1 . 32 + 1 . 37 ∙ R / C
v
) , where C
v 
is the heat capacity 
at constant volume and derived from C
v
= C
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
is the heat capacity at constant pressure, and C
p , m 
is the heat 
capacity at constant pressure of m -th species, which is estimated from 
JANAF polynomials [29] . 
In Eq. (4) , s
m
=  D
m
∇( ρ Y
m
) is the species mass flux. The mass 
diffusivity D
m 
can be derived from heat diffusivity α = k / ρ C
p 
through 
D
m
= α / Le
m
. With the unity Lewis number assumption (i.e. Le
m
= 1), 
the mass diffusivity D
m 
is calculated through D
m
= k / ρ C
p
. Moreover, ˙ω
m 
is the production or consumption rate of m -th species by all N reactions, 
Q. Meng et al.

<!-- PDF_PAGE: 3 -->

Fuel 290 (2021) 119808
3
and can be calculated from the reaction rate of each reaction ω
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
. (8) 
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
2.2. Governing equation for liquid phase 
The Lagrangian method is used to model the dispersed liquid phase, 
which is composed of a large number of spherical droplets [30] . The 
interactions between the droplets are neglected because we only study 
the dilute sprays with the droplet volume fraction being generally less 
than 1 ‰ [31] . The droplet break-up is not considered in this work. 
Therefore, the governing equations of mass, momentum and energy for 
the individual droplets are 
dm
d
dt
=  ˙m
d
, (9)  
d u
d
dt
=
F
d
m
d
, (10)  
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
, (11)  
where m
d 
is the mass of a single droplet and it is calculated by m
d
=
π ρ
d
d
3
d
/ 6 ( ρ
d 
and d
d 
are the material density and diameter of a single 
droplet, respectively). u
d 
is the droplet velocity vector, F
d 
is the force 
exerting on the droplet and here we only consider the Stokes drag [32] . 
c
p,d 
is the droplet heat capacity at constant pressure, and T
d 
is the droplet 
temperature. In this work, both ρ
d 
and c
p,d 
are functions of droplet 
temperature T
d 
[33] , i.e. 
ρ
d
( T
d
) =
a
1
a
1 +( 1  T
d
/ a
3
)
a
4
2
, (12)  
c
p , d
( T
d
) =
b
2
1
τ
+ b
2
 τ
{
2 . 0 b
1
b
3
+ τ
{
b
1
b
4
+ τ
[
1
3
b
2
3
+ τ
(
1
2
b
3
b
4
+
1
5
τ b
2
4
) ] } }
, (13)  
where a
i 
and b
i 
denote the species-specific constants and can be found 
from Ref. [33] . In Eq. (13) , τ = 1 . 0  min ( T
d
, T
c
) / T
c
, where T
c 
is the 
critical temperature (i.e. the temperature at and above which vapor of 
the substance cannot be liquefied, irrespective of the pressure) and 
min ( ∙ , ∙ ) is the minimum function. 
The evaporation rate, ˙m
d
, in Eq. (9) is modelled through 
˙m
d
= π d
d
ShD
ab
ρ
S
ln ( 1 + X
r
) , (14)  
where X
r 
is the molar ratio, and estimated from 
X
r
=
X
S
 X
C
1  X
S
. (15) 
Here X
C 
is the condensed species molar fraction in the surrounding 
gas, and X
S 
is the fuel species molar fraction at the droplet surface. Note 
that estimation of the molar ratio in Eq. (15) does not account for the 
actual chemical reaction effects in the bulk gas. X
S 
can be calculated 
using Raoult ’ s Law 
X
S
= X
m
p
sat
p
, (16)  
with which it has been assumed the inter-molecular force difference in 
the mixture is neglected. This is expected to be acceptable for high-speed 
flows. p
sat 
is the saturated pressure and is a function of droplet tem -
perature T
d 
[33] , i.e. 
p
sat
= p ∙ exp
(
c
1
+
c
2
T
d
+ c
3
lnT
d
+ c
4
T
c
5
d
)
, (17)  
where c
i 
are constants and can be found from Ref. [33] . Variations of p
sat 
with T
d 
is expected to accurately reflect the liquid droplet evaporation in 
high-speed hot atmosphere. Moreover, in Eq. (16) , X
m 
is the molar 
fraction of the condensed species in the gas phase. Moreover, in Eq. (14), 
ρ
S
= p
S
MW
m
/ RT
S 
is vapor density at the droplet surface, where p
S 
is 
surface vapor pressure and T
S
= ( T + 2 T
d
) / 3 is droplet surface temper -
ature. D
ab 
is the vapor diffusivity in the gaseous mixture [27] , i.e. 
D
ab
= 3 . 605910
 3
×( 1 . 8 T
S
)
1 . 75
×
α
l
p
S
β
l
, (18)  
where α
l 
and β
l 
are constants related to different species. 
The Sherwood number in Eq. (14) is modelled as [34] 
Sh = 2 . 0 + 0 . 6 Re
1 / 2
d
Sc
1 / 3
, (19)  
where Sc is the Schmidt number of gas phase and its value is assumed to 
be 1.0. The droplet Reynolds number in Eq. (19) , Re
d
, is defined based on 
the velocity difference between the two phases, i.e. 
Re
d
≡
ρ
d
d
d
| u
d
 u |
μ
. (20) 
The Stokes drag in Eq. (10) is modeled as (assuming that the droplet 
is spherical) [32] 
F
d
=
18 μ
ρ
d
d
2
d
C
d
Re
d
24
m
d
( u  u
d
) . (21) 
The drag coefficient in Eq. (21) , C
d
, is estimated as [32] 
C
d
=
⎧
⎪
⎨
⎪
⎩
0 . 424 , Re
d
> 1000 ,
24
Re
d
(
1 +
1
6
Re
2 / 3
d
)
, Re
d
< 1000 .
(22) 
The convective heat transfer rate 
˙
Q
c 
in Eq. (11) is calculated by 
˙
Q
c
= h
c
A
d
( T  T
d
) , (23)  
where A
d 
is the surface area of a single droplet. h
c 
is the convective heat 
transfer coefficient, and computed using the correlation by Ranz and 
Marshall [34] , i.e. 
Nu = h
c
d
d
k
= 2 . 0 + 0 . 6 Re
1 / 2
d
Pr
1 / 3
, (24)  
where Nu and Pr are Nusselt and Prandtl numbers of gas phase, 
respectively. 
The latent heat of vaporization 
˙
Q
lat 
in Eq. (11) is calculated by 
˙
Q
lat
= h
g , boil
 h
l , boil
, (25)  
where h
g , boil 
and h
l , boil 
are the enthalpies for carrier gas phase and liquid 
phase respectively under boiling temperature. 
Two-way coupling between the gas and liquid phases is taken into 
consideration. The corresponding terms, S
mass
, S
mom
, S
energy 
and S
species , m 
in Eqs. (1)  (4) , are calculated based on the contributions from each 
droplet in the host CFD cells, which read ( V
c 
is the cell volume, N
d 
is the 
droplet number in the cell) 
S
mass
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
, (26)  
S
mom
= 
1
V
c
∑
N
d
1
F
d
, (27)  
Q. Meng et al.

<!-- PDF_PAGE: 4 -->

Fuel 290 (2021) 119808
4
S
energy
= 
1
V
c
∑
N
d
1
(
˙
Q
c
+
˙
Q
lat
)
, (28)  
S
species , m
=
{
S
mass
, for condensed species
0 , for other species .
(29)  
2.3. Computational method 
The gas phase governing equations, i.e. Eqs. (1)  (4) , are discretized 
with cell-centred finite volume method and solved by a density-based 
solver, RYrhoCentralFoam , which is developed from the fully 
compressible flow solver rhoCentralFoam in the framework of Open -
FOAM 5.0 [35] . This solver can simulate compressible reactive flows 
and capture shock wave accurately in a collocated, polyhedral, finite- 
volume framework using non-oscillatory upwind-central schemes. The 
solver rhoCentralFoam is validated by Greenshields et al. [36] using 
various benchmark tests, including the Sod ’ s problem, two-dimensional 
forward-facing step and supersonic jet. It is found that the central- 
upwind scheme in rhoCentralFoam (i.e. Kurganov, Noelle and Petrova 
(KNP) scheme [37] ) is competitive with the state-of-the-art schemes, 
such as Roe scheme, in shock capturing [36] . The RYrhoCentralFoam 
solver has been systematically validated by a series of benchmark tests, 
including two-phase gas-droplet mixture [40] . The results show that the 
RYrhoCentralFoam solver can accurately predict the shock wave, mo -
lecular diffusion, auto-ignition and shock-induced ignition. Moreover, 
the sub-models of this solver related to the dispersed droplet phase are 
verified and validated against analytical and experimental data. It is also 
found that the RYrhoCentralFoam solver is able to model the gas  droplet 
two-phase detonations, including detonation propagation speed, inter -
phase interactions and detonation frontal structures. The RYrhoCen -
tralFoam solver has been applied for various detonative or RDC 
problems, including instability and wave bifurcation in RDC [10,38] , as 
well as two-phase RDC with liquid n -heptane [26] . Besides, the similar 
solver developed from rhoCentralFoam has also been validated and used 
in one- and two-dimensional detonations by Gutierrez Marcantoni et al. 
[39] . 
A second-order implicit backward method is employed for temporal 
discretization and the time step is about 10
-9 
s (maximum Courant 
number less than 0.1). Second-order Godunov-type upwind-central KNP 
scheme [37] is used for discretizing the convective terms in momentum 
equation, i.e. Eq. (2) . To ensure the numerical stability, van Leer limiter 
is adopted for flux calculations with KNP scheme. Total Variation 
Diminishing (TVD) scheme is used for the convective terms in the energy 
and species mass fraction equations. Also, second-order central differ -
encing scheme is applied for the diffusion terms. 
The chemical source terms, ˙ω
m 
and ˙ω
T 
in Eqs. (3) and (4) respec -
tively, are integrated with a Euler implicit method. One-step irreversible 
mechanisms for H
2 
[41] and n -C
7
H
16 
[42] combustion are used to esti -
mate the reaction rates through 
ω
o
m , j
= AT
n
exp
(

E
a
RT
)
[ F ]
a
[ O ]
b
, (30) 
where A is the pre-exponential factor and n is the temperature 
exponent. [ F ] and [ O ] are the concentrations of the fuel and oxidizer, 
respectively, E
a 
is the activation energy, a and b are the fuel and oxidizer 
reaction orders, respectively. The kinetic parameters of the chemical 
reactions for H
2
/O
2 
and n -C
7
H
16
/O
2 
are listed in Table 1 . 
The kinetic parameters of Reaction I in Table 1 are validated by Ma 
et al. [41] with one-dimensional detonation initiation / propagation, 
and successfully used in their simulations of pulse detonation engines. It 
is also used by Meng et al. [43] for modelling rotating detonation 
combustion and reasonable results of RDC propagation are achieved. 
Reaction II has been used for modelling spray RDC by Zhao and Zhang 
[26] and the results with Reaction II demonstrate good agreements with 
those from a skeletal n -C
7
H
16 
mechanism [44] . Since this study is 
focused on the RDW propagation and droplet dynamics, instead of 
detailed gaseous reactions, the foregoing mechanisms are sufficient. 
One-step or simplified mechanisms are also used for two-phase RDC 
modelling [9,25] and general two-phase detonation problems [45,46] . 
For the liquid phase, their equations, i.e. Eqs. (9)  (11) , are solved by 
first-order implicit Euler method. Meanwhile, the gas properties at the 
droplet location are estimated based on linear interpolation. The two- 
way coupling terms, i.e. Eqs. (26)  (29) , are calculated explicitly, as 
the source terms of the gas phase equations, i.e. Eqs. (1)  (4) . 
3. Physical model and simulation case 
3.1. RDC model with liquid fuel sprays 
Fig. 1 shows a two-dimensional rectangular domain which is used 
here as a simplified model of a flattened RDE combustor. The length (i.e. 
x (mm)
y (mm)
2880 ...
Periodic 
boundary
Periodic 
boundary
Non-reflective boundary
Nozzle injection
n-C7H16(g)/air(g)/n-C7H16(l)H2+air
...
H2 Inlet  n-C7H16 Inlet  Wall 
Detonation wave front
Oblique shock wave
Slip line
Deflagration surface
Fuel refill zone
Product
RDW propagating direction
99
Hot spot
Contact triple 
pointp
Fig. 1. Two-dimensional RDC model: computational domain and boundary condition. The gas temperature (250  3,000 K) is shown as the background.  
Table 1 
Chemical reactions for H
2
/O
2 
and n -C
7
H
16
/O
2 
(units in cm-sec-mole-cal- 
Kelvins).  
Index Reaction A n E
a 
a b Ref. 
I 2H
2 
+ O
2 
⇒ 2H
2
O  1.03 ×
10
9  
0.0  29,841.0  1.0  1.0 [41] 
II n -C
7
H
16 
+ 11O
2 
⇒ 
7CO
2 
+ 8H
2
O  
5.10 ×
10
11  
0.0  30,000.0  0.25  1.5 [42]  
Q. Meng et al.

<!-- PDF_PAGE: 5 -->

Fuel 290 (2021) 119808
5
x -direction) of the computational domain in Fig. 1 is 288 mm, while the 
height ( y -direction) is 99 mm. This domain has been used in our pre -
vious work by Zhao and Zhang [26] , in which successful rotating 
detonation wave propagation in liquid n -C
7
H
16 
sprays is achieved. The 
corresponding nominal diameter is approximately 92 mm, similar to 
that of a small-scale RDE combustors (e.g. by Bohon et al. [47] and also 
Deng et al. [48,49] ). It should be highlighted that, to obtain physically 
sound results on RDC ’ s with droplet evaporation and reactant mixing, it 
is significant to use a practically relevant dimensions for the simplified 
RDC model, in which the timescale relations between droplet evapora -
tion, reactant mixing and periodic RDW propagation can be reasonably 
reproduced. In addition, turbulence effects on RDW is not considered 
here. 
The boundary conditions of the RDC model are marked in Fig. 1 . The 
outlet is assumed to be non-reflective, to avoid the interference from 
upstream-propagating pressure waves on the detonation wave and 
deflagration surface near the head end. The detonation waves can 
propagate continuously via periodic boundaries at the left and right 
sides of the domain, as indicated in Fig. 1 . The modelled propellant 
injectors lie at the entire lower boundary in Fig. 1 , which will be 
introduced in Section 3.2 . 
The RDW is initiated forcibly using a rectangular hot spot (20 atm 
and 2,000 K) near the left boundary with height and width being 12.2 
mm × 1 mm (see Fig. 1 ), respectively. Additionally, a fresh fuel layer 
(12.2 mm × 288 mm) with premixed stoichiometric n -C
7
H
16
/air is 
initialized near the lower boundary (i.e. the fuel injectors) in Fig. 1 to 
promote the propagation of the newly ignited RDW. The rest region in 
the domain is initialized with air, corresponding to pressure of 1 atm and 
temperature of 300 K. Stable propagation of RDW is identified through 
examining the pressure history from probes and instantaneous wave 
propagation speed. 
3.2. Gaseous / liquid reactants and injection model 
In this work, the fuels are partially pre-vaporized n -C
7
H
16 
sprays 
with separate injection of stoichiometric hydrogen/air gas. The latter is 
used for stabilizing the continuous detonations, as implemented in the 
liquid fuel RDE experiments by Bykovskii et al. [19,20] and Kindracki 
[22] . The reactant injector system is modelled as 32 sets of abreast and 
continuously arranged n -C
7
H
16 
and H
2 
inlet jets at the head end (see 
Fig. 1 ). A set of these two inlets are discretized with solid walls to mimic 
the discrete injection of propellants in practical RDE ’ s. The area ratio θ 
(length ratio in 2D cases) between H
2
, n -C
7
H
16 
inlets and the solid wall is 
fixed to be 1:6:2. Although it is shown that the injector spacing may 
affect the RDW propagation [9,25] , however, this effect is not studied in 
this work. 
Heterogeneous mixtures of n -C
7
H
16 
droplets and vapour are injected 
through the n -C
7
H
16 
inlet. The droplets are assumed to be spherical and 
mono-sized, with diameters being 5 – 50 μ m, which are close to those 
measured in detonation combustor by Kindracki [21] . It is acknowl -
edged that polydispersity of fuel droplets is not considered. Computa -
tional parcel method is used in our simulations, in which droplets with 
identical properties are denoted by one parcel. In addition, different 
levels of pre-vaporization in the n -C
7
H
16 
stream are parameterized by 
the equivalence ratio ϕ
g 
of premixed vapour/air mixture through the n - 
C
7
H
16 
inlet. Both gaseous n -C
7
H
16 
and H
2 
streams have identical total 
temperature and pressure, i.e. T
0 
= 300 K and p
0 
= 20 atm respectively. 
Similar to the gaseous fuel RDE modelling [11,50 – 54] , injections of 
n -C
7
H
16 
and H
2 
are determined by the relation between injector total 
pressure and local pressure near the inlet in the domain. For the liquid 
phase, the interphase kinematic equilibrium is assumed, and hence the 
droplet injection velocity follows that of the gas phase issued from the 
same inlets. This assumption is acceptable when the droplets disperse 
sufficiently long in the carrier gas from the upstream plenum of practical 
RDE ’ s. Therefore, in our studies the n -C
7
H
16 
spray injection is activated 
if, and only if, the top head gas pressure is lower than p
o
. With the above 
assumptions and simplifications, there are three situations for n -C
7
H
16 
inlets, i.e. 
(1) If p ≥ p
o
, then there are no reactants injected through the inlets, 
which are treated as solid walls and hence no flashback can occur. The 
local pressure p
i
, gas temperature T
i
, droplet temperature T
i , d
, gas ve -
locity v and droplet velocity v
d 
respectively satisfy the following con -
ditions ( T is the local temperature near the inlet) 
p
i
= p , T
i
= T and v = 0 , no droplets ; (31) 
(2) If p
cr 
< p < p
o
, then the flows at the inlet are not choked, and 
therefore 
p
i
= p , T
i
= T
o
(
p
i
P
o
)
γ
R
 1
γ
R
, T
i , d
= T
o
, and v = v
d
=
̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅ ̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅ ̅̅̅̅̅̅̅̅̅̅̅ ̅
2 γ
R
γ
R
 1
RT
o
[
1 
(
p
i
P
o
)
γ
R
 1
γ
R
]
√
√
√
√
; (32) 
(3) If p ≤ p
cr
, then the flows at the inlet are choked, and therefore 
p
i
= p
cr
, T
i
= T
o
(
p
i
P
o
)
γ
R
 1
γ
R
, T
i , d
= T
o
, and v = v
d
=
̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅ ̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅ ̅̅̅̅̅̅̅̅̅̅̅ ̅
2 γ
R
γ
R
 1
RT
o
[
1 
(
p
i
P
o
)
γ
R
 1
γ
R
]
√
√
√
√
(33) 
The critical pressure p
cr 
is calculated from the choking condition, 
based on the total pressure and reactant specific heat ratio, p
cr
=
p
o
(
2
γ
R
+ 1
)
γ
R
γ
R
 1
. γ
R 
is the specific heat capacity ratio of the mixture. For H
2 
inlets, same correlations as Eqs. (31)  (33) are used, without specifica -
tions of T
i , d 
and v
d
. A posterior examination of our results show that this 
droplet injection model can accurately reproduce the specified droplet 
mass flow rates (with errors less than 2%), and it has been successfully 
applied in our recent simulations of two-phase RDE ’ s [26] . 
3.3. Simulation case 
Table 2 shows five case groups, i.e. A  E, simulated in this work. 
They are characterized by the different equivalence ratios of gas and 
Table 2 
Information of liquid and pre-vaporized n -heptane (stoichiometric H
2
/air from H
2 
inlet).  
Case 
group 
n -Heptane equivalence ratio Hydrogen Liquid Droplet property 
Liquid n -heptane 
phase ϕ
l  
Pre-vaporized n -heptane gas 
phase ϕ
g  
Global n -heptane Equivalence 
ratio † ϕ
t  
Mass flow rate (kg/ 
s) 
Mass flow rate 
(kg/s) 
Initial diameter d
0
d 
( μ m)  
A  0.134  0.35  0.446  0.037  0.107 5 – 50 
B  0.129  0.4  0.485  0.036  0.097 5 – 50 
C  0.126  0.6  0.650  0.036  0.092 5 – 50 
D  0.123  0.8  0.813  0.035  0.087 5 – 50 
E  0.123  1.0  0.976  0.035  0.087 5 – 50 
† ϕ
t 
is estimated based on liquid / gaseous n -C
7
H
16 
and oxygen from both n -C
7
H
16 
and H
2 
inlets. 
Q. Meng et al.

<!-- PDF_PAGE: 6 -->

Fuel 290 (2021) 119808
6
liquid phases in the n -C
7
H
16 
stream, i.e. ϕ
g 
and ϕ
l
. They are respectively 
estimated based on the mass of the gaseous and liquid n -heptane and the 
air injected from the n -heptane inlet. As shown in Table 2 , the global n - 
C
7
H
16 
equivalence ratio ϕ
t 
gradually increases, from Case A with ϕ
t 
=
0.446 to Case E with ϕ
t 
= 0.976. In each group, the droplet diameters 
considered are d
0
d 
= 5, 10, 15, 20, 30, 40 and 50 μ m. Readers should be 
reminded that in all the cases, the hydrogen/air stream is stoichiometric. 
For ease of reference, individual cases are named as, e.g. A15. Here the 
letter A denotes case group A with ϕ
l 
= 0.134 and ϕ
g 
= 0.35, whereas the 
number indicates the initial droplet diameter, i.e. d
0
d 
= 15 μ m. For each 
group, the corresponding droplet-free RDC cases are also simulated for 
comparisons. For instance, A00 denotes the purely gaseous n -heptane/ 
air mixture with ϕ
g 
= 0.35. 
4. Mesh sensitivity analysis 
The computational domain in Fig. 1 is discretized with uniform 
Cartesian cells. It should be highlighted that resolving the detailed 
detonation structure is beyond the objective of this work; instead, 
detonation propagation in two-phase fuels are concentrated. Mean -
while, in Lagrangian tracking of the sub-grid droplets, a mesh resolution 
larger than the droplet diameter is desirable, to ensure that the gas phase 
quantities at the droplet surface (critical for estimating the two-phase 
coupling, e.g. evaporation) can be accurately approximated using the 
interpolated ones at the droplet centre [56] . Therefore, three mesh sizes 
are tested, i.e. 0.1, 0.2 and 0.4 mm, termed as M1, M2 and M3, 
respectively. 
Fig. 2 shows the pressure history at a probe near the inlet end with 
M1, M2 and M3. The results are from Case B15. It is found that variations 
of the mesh resolutions do not change the RDW number and propagation 
direction. Also, from Fig. 2 , the pressure histories predicted with M1 and 
M2 are close, in terms of the peak pressure instants and values. However, 
pressure history from M3 slightly lags behind those from M1 and M2 and 
the peak value is also slightly lower than those from M1 and M2. The 
higher pressure from M1 at t = 7.9 s may result from the non-uniform 
instantaneous pressure distribution along the detonation wave. More -
over, the pressure peaks from M1 and M2 are closer to the maximum 
pressure (4.09 × 10
7 
Pa, predicted by SD Toolbox [55] with 250 K and 
15 atm). 
Table 3 shows the RDW propagation speed D
det 
predicted with the 
three meshes. D
CJ 
is also calculated with SD Toolbox based on the 
assumption that all the n -C
7
H
16 
droplets are vaporized and perfectly 
mixed with the n -C
7
H
16 
and H
2 
gaseous mixtures. The deficits of the 
calculated detonation speed relative to Chapman – Jouguet (C – J) speed 
are all around 15%, which may stem from the dual-fuel and two-phase 
injections, and hence non-uniform reactant distributions. Moreover, 
the deviations of RDW propagation speed relative to the finest case M1 
increase with increased mesh size, 1.5% for M3 and 0.5% for M2. 
Fig. 4. Contours of (a) temperature (lower limit clipped to 310 K), (b) pressure, 
(c) averaged evaporation rate, (d) vaporized n -C
7
H
16 
from droplets, (e) pre- 
vaporized n -C
7
H
16
, (f) H
2
. Results from Case B05. Unit for x- and y -axis in m. 
0 20 40 60 80 100
0
2
4
6
8
10
12
14
16
d10 (μm)
y (mm)
M3
M2
M1
Fig. 3. Distributions of mean droplet diameter along the RDE height, Case B15.  
7.6 7.8 8.0 8.2
0
1x107
2x107
3x107
4x107
p (Pa)
t (ms)
Max pressure
 M3
 M2
 M1
Fig. 2. Pressure history from a location near the head end, Case B15. Dashed 
line: maximum pressure from SD Toolbox [55] . 
Table 3 
RDW propagation speeds predicted with different meshes.  
Mesh Δ
x , y
(mm)  D
det
(m/ 
s)  
D
CJ
(m/ 
s)  
Deficit (C – J, 
%) 
Deviation (M1, 
%) 
M1  0.1 1379 1615  14.6  
M2  0.2 1386 1615  14.2  0.5 
M3  0.4 1359 1615  15.8  1.5  
Q. Meng et al.

<!-- PDF_PAGE: 7 -->

Fuel 290 (2021) 119808
7
Two-way interphase coupling is considered in this work and there -
fore it is also important to examine how mesh resolutions for Eulerian 
gas phase influence the Lagrangian droplet calculations. Fig. 3 shows the 
variations of droplet arithmetic mean diameter ( d
10
) along the height ( y ) 
direction in Case B15. Here d
10 
is estimated based on the droplets in the 
entire domain from about 50 instants. The droplet diameters from M3 
are consistently higher than the results in M1 and M2. Meanwhile, the 
droplet distributions in M1 and M2 are generally similar along the entire 
RDE height direction. Based on the results in Figs. 2 and 3 as well as 
Table 3 , the resolution of 0.2 mm will be selected, in terms of the 
acceptable computational accuracy and cost. Similar resolutions are also 
used by Schwer et al. [45,57] for their Eulerian  Lagrangian modelling 
of two-phase detonation. 
5. Results and discussion 
5.1. General characteristics of liquid-fuelled rotating detonation 
combustion 
Fig. 4 respectively demonstrate the distributions of Lagrangian 
droplets, gas temperature (color cut off over 310 K), pressure, averaged 
evaporation rate, mass fractions of n -heptane and hydrogen from a 
single-waved case, i.e. B05. Note that the averaged evaporation rate is 
calculated using Eq. (26) . Fig. 4 (d) and 4(e) respectively visualize the 
mass fractions of n -C
7
H
16 
vaporized in the chamber and pre-vaporized 
before injection. The details of the droplets inside the dashed box in 
Fig. 4 (a) are enlarged in Fig. 5 . 
It can be found from Fig. 4 (a) and 4(b) that the RDC structure in -
cludes detonation wave, deflagration surface and oblique shock wave, 
similar to the previously results of two-phase [9,25,26] and gaseous RDC 
[10,52] . The detonation wave height ( y -direction) h
d 
is 0.03 m, whilst 
the refill zone length ( x -direction) l
f 
is about 0.193 m. Their ratio, K =
l
f
/ h
d
, is 6.4, which is within the range (i.e. 5  9) suggested by Bykovskii 
et al. [58] for gaseous reactants. The discrete inlets result in the ribbon- 
like distributions of n -heptane and hydrogen fuels in the refill zone. As 
mentioned in Section 3.2 , the injections of liquid n -C
7
H
16 
droplets at the 
individual inlets are synchronized with that of the carrier gas. Therefore, 
droplet injection only occurs in the triangular fuel refill zone and leads 
to a series of parallelly spray jets, as shown by the Lagrangian droplets in 
Fig. 4 (a) and 5(a). Behind the RDW, due to the higher local pressure than 
the total pressure (i.e. 20 atm), the droplet injection is suppressed. 
Droplet evaporation is limited inside the refill zone as shown from 
the distribution of averaged evaporation rate in Fig. 4 (c). This can also 
be confirmed by negligible decrease of droplet diameters (see Fig. 4 a and 
5a). On the contrary, high evaporation rates are observable in Fig. 4 (c) 
near the deflagration surface. Due to small diameters ( d
0
d 
= 5 µ m ) and 
Fig. 6. Contours of (a) temperature (lower limit clipped to 310 K), (b) pressure, 
(c) evaporation rate, (d) vaporized n -C
7
H
16 
from droplets, (e) pre-vaporized n - 
C
7
H
16
, (f) H
2
. Results from Case C40. Unit for x- and y -axis in m. 
Fig. 5. Distributions of droplets coloured by (a) diameter and (b) y -direction 
velocity. The region corresponds to the dashed box in Fig. 4 (a). Unit for x- and 
y -axis in m. 
Fig. 7. Distributions of droplets coloured by (a) diameter and (b) y -direction 
velocity. The region corresponds to the dashed box in Fig. 6 (a). Unit for x- and 
y -axis in m. 
Q. Meng et al.

<!-- PDF_PAGE: 8 -->

Fuel 290 (2021) 119808
8
large y -direction velocity (see Fig. 5 b), the droplets are transported by 
the carrier gas, traversing the refill zone. For those droplets at the tips of 
the spray jets, they have direct contact with the wrinkled deflagration 
surface and evaporation occurs due to the local high temperature, which 
can be found in Fig. 5 . Nevertheless, through comparisons between 
Fig. 4 (d) and 4(e), one can see that the concentration of the pre- 
vaporized n -C
7
H
16 
is much higher than that of n -C
7
H
16 
vaporized in 
the chamber. Interestingly, the droplets do not penetrate into the burned 
side of the deflagration surface, since they have small velocity differ -
ences with the local surrounding gas and are engulfed and trapped by 
the eddies resulting from Kelvin – Helmholtz and Richtmyer – Meshkov 
instabilities [10,53,59] (see Fig. 5 ). However, a pocket of the vapour is 
occasionally transported into the burned gas side (pointed by the arrow 
in Fig. 4 d) and then deflagrated there. 
Plotted in Figs. 6 and 7 are the counterpart results from Case C40. 
Different from the results in Figs. 4 and 5 , three RDW ’ s are stabilized in 
this case. The bifurcation of the RDW number results from the sponta -
neous ignition of detonation wavelets along the deflagration surface of 
the refill zone. Three RDWs ’ have nearly the same height, i.e. h
d
≈ 0.01 
m, about one third of that in Fig. 4 . Accordingly, the length of the 
triangular fuel refill zone is reduced to l
f
≈ 0.055 m, leading to K = 5 . 5. 
In this case, a large number of liquid droplets can be seen behind the 
detonation waves. This may be caused by the shorter refill zone and 
increased initial droplet diameter ( d
0
d 
= 40 µ m). These escaping droplets 
are accelerated by expanded post-detonation gas (characterized by the 
high velocity in the post-detonation areas in Fig. 7 ). Moreover, contin -
uous evaporation occurs there due to the high gas temperature and/or 
gradually reduced pressure, as seen from the distributions of high 
evaporation rates in Fig. 6 (c). This is consistent with the gradual 
0 10 20 30 40 50
1200
1400
1600
1800
2000Ddet (m/s)
Case Group A
B
C
D
E
Solid symbols: droplet-laden case
Open symbols: gaseous case
(a)
0 10 20 30 40 50
0
5
10
15
20
25
30
35
40Df (%)
d0 (μm)
Case Group A
B
C
D
E
Solid symbols: droplet-laden case
Open symbols: gaseous case
(b)
(μm)
Fig. 8. (a) Detonation propagation speed and (b) velocity deficit as functions of 
initial droplet diameter under different pre-vaporized gas equivalence ratios. 
Open symbols: gaseous (i.e. n -C
7
H
16 
vapour and H
2
) case without droplets in -
jection. The number in the legend indicates the RDW number, which also ap -
plies for Figs. 9 and 21 . 
0 10 20 30 40 50
0.75
0.80
0.85
0.90
0.95
1.00
1.05
fdet
d0 (μm)
A Case  Group  
B
C
D
E
Solid symbols: droplet-laden cas e
Open symbols: gase ous cas e
(μm)
Fig. 9. Detonated fuel fraction as a function of initial droplet diameter under 
different pre-vaporized gas equivalence ratios. 
84.1
75.1 71.3 70.7 70.8 72.3 74.2 74.2
11.9
12.2
10.5 9.48 10.7 10.6 9.84 10.2
3.22
11.3 16.7 18.3 17 15.7 14.6 14.2
0.74 1.38 1.46 1.51 1.52 1.38 1.32 1.38
0 5 10 15 20 30 40 50
0
20
40
60
80
100fdet, fdef (%)
d0 (μm)
 Detonated n-C7H16  Defagrated n-C7H16
 Detonated H2  Defagrated H2
(μm)
Fig. 10. Detonated and deflagrated fuel fractions. Results from case group B 
( ϕ
g 
= 0.4). 
(μm)
0        1         2          3          4          5
50       800       1500        2300        3000
(K)
t = 10.57 ms(a)
t = 10.594 ms(b)
t = 10.61 ms(c)
t = 10.612 ms(d)
Fig. 11. Droplet trajectory I: be fully vaporized around the detonation front. 
Results from case B05. Arrows indicate the droplet locations. Image size: 288 
mm × 40 mm. 
Q. Meng et al.

<!-- PDF_PAGE: 9 -->

Fuel 290 (2021) 119808
9
reduction of the droplet diameters when the distance between the 
droplet and the detonation wave increases (see Fig. 7 ). It should be 
emphasized that droplets at two sides of the deflagration surfaces are 
originally different: they are newly injected in the refill zone and escape 
from the preceding detonation front, respectively. This is apparent by 
their distinct droplet diameters (see Fig. 7 a). 
It is noteworthy to further discuss the interactions between liquid 
droplets and the characteristic structures (e.g. detonation wave, def -
lagrative surface and oblique shock wave) in rotating detonation com -
bustion, through the droplet distributions in Figs. 5 and 7 . For small 
droplets, e.g. 5 µ m in Fig. 5 , the droplets around the approaching 
detonation wave are completely vaporized and the vapours are deto -
nated. Meanwhile, the hot burned gas near the deflagrative surface 
promotes the evaporation there, leading to high vapour concentration 
and subsequent deflagrative combustion. The above phenomena are 
qualitatively consistent with the observations by Hayashi et al. [25] and 
Sun and Ma [9] in their RDC modelling with liquid JP-10 ( d
0
d 
= 1, 5, and 
10 μ m) and octane sprays ( d
0
d 
= 20 μ m), respectively. However, for 
relatively large droplets (e.g. 40 µ m in Fig. 7 b), they stagnate slightly 
away from the deflagration surface due to the local kinematic equilib -
rium effects. For those escaping droplets, when they cross the oblique 
shock wave extending from the next RDW ’ s, most of them are depleted 
due to the high temperature in the post-shock area, as observed in Fig. 6 
0.0
4.0x10-9
8.0x10-9
1.2x10-8
1.6x10-8
2.0x10-8
mdot,d (kg/s)
(b)
a
-200
0
200
400
600
800
1000 (c)
Ux (m/s)
a
0
100
200
300
400 (d)
Uy (m/s)
a
10.57 10.58 10.59 10.60 10.61 10.62
0
200
400
600
800
1000 (e)
Uc (m/s)
t (ms)
a
10.57 10.58 10.59 10.60 10.61 10.62
-100
0
100
200
300
400
500
600 (f)
Uc-Ud (m/s)
t (ms)
a
0
5
10
15
20
25
30
d2
d (μm2)
(a)
a
Fig. 12. Time histories of (a) diameter squared, (b) evaporation rate, (c) x -direction velocity, (d) y -direction velocity, (e) local gas velocity magnitude, (f) velocity 
difference in trajectory I. 
(μm)
0        1         2          3          4          5
50       800       1500        2300        3000
(K)
t = 10.51 ms(a)
t = 10.54 ms(b)
t = 10.59 ms(c)
t = 10.622 ms(d)
Fig. 13. Droplet trajectory II: be fully vaporized around the deflagrative sur -
face. Results from case B05. Arrows indicate the droplet locations. Image size: 
288 mm × 40 mm. 
Q. Meng et al.

<!-- PDF_PAGE: 10 -->

Fuel 290 (2021) 119808
10
(a). Representative droplet trajectories in an RDE chamber will be 
further studied in Section 5.4 . 
5.2. Detonation propagation speed 
Fig. 8 shows the detonation propagation speed D
det 
and velocity 
deficit D
f 
as functions of initial droplet size d
0
d 
under various pre- 
vaporized gas equivalence ratios ϕ
g
. The solid lines are fitted from our 
simulation results marked as symbols. Note that each case group has a 
constant pre-vaporized gas equivalence ratio ϕ
g 
as tabulated in Table 2 . 
It is seen that with increased ϕ
g 
from 0.35 to 1.0, D
det 
increases. It is 
observed that for the relatively small ϕ
g 
(e.g. 0.35 and 0.4 in groups A 
and B), D
det 
first increases as the droplet size increases, and when d
0
d 
is 
beyond 5 µ m , it gradually decreases and almost is constant (close to the 
corresponding gaseous D
det 
values when their RDW numbers are the 
same) when d
0
d
> 30 µ m . The speed enhancement for small droplets is 
probably due to their fast evaporation, kinetically contributing towards 
the overall stoichiometric gas composition. However, when ϕ
g 
further 
increases, e.g. 0.8 and 1.0 in groups C and D, such non-monotonicity 
becomes not obvious. 
It is also seen from Fig. 8 (a) that bifurcation of the RDW number 
occurs when ϕ
g 
is high, e.g. in groups C  E. Multiply RDW ’ s are also 
observed by Bykovskii et al. [19] from the experimental studies of RDE 
with liquid kerosene  hydrogen  air mixtures, in which the RDW ’ s in -
crease from one to five with increased overall reactant mass flow rate. It 
is shown from Fig. 8 (a) that the number of RDW ’ s also affects the 
propagation speed of the two-phase detonation. This is particularly 
obvious in case group E. For example, detonation propagation speeds in 
Cases E20 and E50 (four-wave mode) are higher than those in adjacent 
cases (Cases E15 and E30, five- and six-wave modes respectively). 
Similar tendencies can also be observed among Cases D30, D20, D15. 
This is because as the RDW number increases, the width of the fuel refill 
zone decreases accordingly, the time for droplet evaporation and/or 
reactant mixing is reduced. 
Fig. 8 (b) further shows the corresponding velocity deficits, which are 
relative to the respective C  J velocities calculated assuming that all the 
liquid n -C
7
H
16 
are fully vaporized and the gaseous mixture is perfectly 
mixed. Compared to the gaseous cases, the sprayed fuels lead to higher 
velocity deficits, and the differences are more striking when the pre- 
vaporization level is relatively small (e.g. ϕ
g 
= 0.35, 0.4 and 0.6). 
Meanwhile, for the same ϕ
g
, the velocity deficit D
f 
generally rises when 
the initial droplet size increases, consistent with the tendencies from 
liquid-fuelled detonation in tubes [60,61] . However, as ϕ
g 
increases, D
f 
consistently decreases. For example, the velocity deficits of group E vary 
between 4%  10%, whilst those of group A 21%  28%. The exceptions 
are groups B and C. D
f 
in these two groups are close because generally 
0.0
1.0x10-9
2.0x10-9
3.0x10-9
4.0x10-9
5.0x10-9
6.0x10-9
(b)
mdot,d (kg/s)
b
-40
-20
0
20Ux (m/s)
(c) b
10.50 10.53 10.56 10.59 10.62
80
100
120
140
160
180
200Uc (m/s)
t (ms)
(e)
b
10.50 10.53 10.56 10.59 10.62
-40
-20
0
20
40
Uc-Ud (m/s)
t (ms)
(f)
b
60
80
100
120
140
160
180
200
Uy (m/s)
(d)
b
0
5
10
15
20
25
30 (a)
d2
d (μm2)
b
Fig. 14. Time histories of (a) diameter squared, (b) evaporation rate, (c) x -direction velocity, (d) y -direction velocity, (e) local gas velocity magnitude, (f) interphase 
velocity difference in trajectory II. 
Q. Meng et al.

<!-- PDF_PAGE: 11 -->

Fuel 290 (2021) 119808
11
higher RDW number in group C than in group B, which to some degree 
offset the deficit reduction caused by increased pre-vaporization gas 
equivalence ratio. Similar velocity deficit level, i.e. 20%  25%, are re -
ported by Kindracki [22] in his liquid kerosene RDE experiments. It is 
well known that there are diverse factors for velocity deficits in RDE ’ s 
[1] , and in our cases, they may be caused by droplet evaporation, gas 
reactant mixing and/or RDW number multiplicity. 
5.3. Detonated fuel fraction 
Fig. 9 shows the fraction of detonated fuels (including n -C
7
H
16 
and 
H
2
), f
det
, as a function of initial droplet diameter d
0
d 
under different gas 
equivalence ratios ϕ
g
. f
det 
is estimated based on the volume averaged 
detonation consumption rates of individual fuel conditioning on heat 
release rate 
˙
Q greater than 10
13 
J/m
3
/s, approximately deem to be 
detonative combustion [10] , i.e. 
f
det
=
˙ω
det , n  C 7 H 16
+ ˙ω
det , H 2
˙ω
n  C 7 H 16
+ ˙ω
H 2
, (34)  
where ˙ω
n  C 7 H 16 
and ˙ω
H 2 
are the n -C
7
H
16 
and H
2 
overall consumption 
rates, respectively. ˙ω
det , n  C 7 H 16 
and ˙ω
det , H 2 
are the n -C
7
H
16 
and H
2 
con -
sumption rates, respectively, conditioning on 
˙
Q > 10
13 
J/m
3
/s. In gen -
eral, for a fixed droplet diameter d
0
d
, f
det 
increases from groups A to E. 
This is because n -C
7
H
16 
concentration in the gas phase is increased with 
ϕ
g
. Meanwhile, this enhancement effect on detonative combustion are 
more pronounced when ϕ
g 
is relatively low, for instance, in groups A, B 
and C. There exists a critical droplet diameter, i.e. about 20 µ m , corre -
sponding to minimum f
det
. When d
0
d
< 20 μ m, f
det 
decreases with d
0
d
. This 
is because larger droplets have less propensity to be fully vaporized at 
the detonation wave (hence smaller ˙ω
det , n  C 7 H 16
). Meanwhile, the 
escaping droplets can continue evaporation immediately behind the 
RDW, and the vapour is consumed by the deflagration (larger ˙ω
n  C 7 H 16
). 
These two processes result in smaller f
det
. However, when d
0
d
> 20 μ m, 
droplets are vaporized in a broader zone, i.e. between the slip line and 
deflagration surface behind the RDW, as seen from Fig. 6 (a) and 7. 
Limited deflagrative combustion is observed there, due to low oxygen 
concentration under initial fuel-lean n -C
7
H
16
/air conditions (e.g. groups 
A and B). As such, f
det 
increases with further increased d
0
d
, because 
˙ω
n  C 7 H 16 
is reduced. Due to the deflagrative combustion of part of the 
vaporized n -C
7
H
16
, f
det 
in the two-phase cases is generally lower than 
that in the corresponding gaseous cases. When the equivalence ratio of 
the initial n -C
7
H
16
/air gas becomes higher (e.g. groups C  E), the 
dependence of f
det 
on d
0
d 
tends to be weak. This can be justified by the 
limited evaporation time in the reduced refill zone due to wave bifur -
cation, and low oxygen concentration in the detonated gas due to the 
near-stoichiometric condition (see Fig. 10 ). 
The fractions of detonated ( f
det
) and deflagrated ( f
def
) fuels are 
further examined, based on the cases of ϕ
g 
= 0.4 (group B). The deto -
nated (deflagrated) fuel fraction is the fuel consumption rate of deto -
native (deflagrative) combustion, normalized by the sum of the overall 
fuel consumption rates, i.e. ˙ω
n  C 7 H 16
+ ˙ω
H 2
. Here the deflagration is 
identified based on 
˙
Q ≤ 10
13 
J/m
3
/s. It is seen that over 70% n -heptane 
is detonated under different droplet diameter conditions. The detonated 
n -heptane fraction first decreases until d
0
d 
= 15 µ m and then slightly 
increases. The fractions of deflagrated n -heptane have similar tendency 
but are much lower (less than 18%). Also, the detonated and deflagrated 
hydrogen fractions show limited variations when the droplet diameter is 
increased. 
5.4. Typical droplet trajectory in rotating detonative combustion 
Four representative droplet trajectories in rotating detonation com -
bustion are identified through screening the fates of a large number of 
droplets after they are injected into the domain. The first trajectory 
( “ trajectory I ” for reference hereafter) is shown in Fig. 11 (a)  (d), which 
shows the time sequence of the instantaneous location of one liquid fuel 
droplet in case B05 ( ϕ
g 
= 0.4 and d
0
d
= 5 μ m), and the gas temperature is 
overlaid to demonstrate the detonation wave location. Meanwhile, for 
this droplet, its time histories of diameter squared ( d
2
d
), evaporation rate 
( ˙m
d
), x - and y -direction velocities ( U
x 
and U
y
), magnitude of gas velocity 
( U
c
) at the droplet location, and interphase velocity magnitude differ -
ence ( U
c
 U
d
) are demonstrated in Fig. 12 . 
It is seen from Fig. 11 (a) that this droplet moves mainly along the 
RDE height direction in the refill zone after it is injected at t = 10.567 
ms. This can be confirmed by relatively small x -direction and dominant 
y -direction velocities, as shown in Fig. 12 (c) and 12(d) respectively. The 
y -direction velocity is around 200 m/s at the inlet, decreases due to the 
drag effects and then increases towards 120 m/s before the detonation 
arrives. The increased velocity results from the recirculating flows near 
the walls, which can be observed in Fig. 5 . The interphase velocity dif -
ference is small before the detonation front as shown in Fig. 12 (f), 
implying the interphase kinematic quasi-equilibrium in the refill zone. 
Then the droplet stagnates some distance below the deflagrative surface, 
as seen in Fig. 11 (b). During this period, its diameter d
d 
almost keeps 
constant (see Fig. 12 a) and the droplet temperature is relaxed to local 
gas temperature (about 250 K) due to the convective heat transfer. 
Limited evaporation happens and therefore almost zero ˙m
d 
is observed 
in Fig. 12 (b). At t = 10.61 ms (marked with a in Fig. 12 ), the droplet is 
swept by the approaching detonation wave (see Fig. 11 c), and therefore 
rapidly heated to the boiling temperature (about 540 K, see the col -
ouring of Fig. 12 a and 12b). Strong evaporation proceeds (with high ˙m
d 
in Fig. 12 b) and the droplet is fully vaporized (with quickly decaying 
size in Fig. 12 a) when it crosses the detonation wave. 
Likewise, Figs. 13 and 14 show the counterpart results of droplet 
trajectory II in rotating detonation field. The results are from the same 
case B05 as shown in Figs. 11 and 12 . Different from trajectory I, this 
droplet is injected at t = 10.5 ms, from an inlet at the right end of the fuel 
(μm)
0             5                10                  15
(K)
t = 4.916 ms(a)
(b)
(c)
(d)
t = 5.03 ms
t = 5.04 ms
t = 5.05 ms
(e) t = 5.07 ms
(f) t = 5.084 ms
Fig. 15. Droplet trajectory III: leak through the triple point. Results from Case 
B15. Arrows indicate the droplet location. Image size: 288 mm × 40 mm. 
Q. Meng et al.

<!-- PDF_PAGE: 12 -->

Fuel 290 (2021) 119808
12
refill zone and hence relatively far away from detonation wave front. 
Before t = 10.605 ms (marked as b in Fig. 14 ), the droplet temperature is 
gradually reduced from the initial value of 300 K towards the local gas 
temperature (i.e. about 250 K) in the fill zone and then slightly increases 
when it approaches the hot deflagration surface. This trend is also seen 
from trajectory I in Fig. 12 . Meanwhile, the droplet size and evaporation 
rate do not show pronounced changes (see Fig. 14 a and 14b) in this 
period. However, considerable variations of droplet and gas velocities, 
as well as their difference, can be observed in Fig. 14 (c)  14(f). These are 
different from the results in Fig. 12 . This is caused by its interactions 
with the eddies arising from the local deflagrative front instabilities. 
After t = 10.605 ms, droplet temperature and evaporation rate ˙m
d 
in -
crease quickly (see Fig. 14 b). This stems from the close interactions 
between the droplet and hot deflagrative surface, as indicated in Fig. 13 
(c) and 13(d). However, the droplet temperature stays around 500 K. 
After t = 10.605 ms, droplet evaporation rate decreases because of the 
reduced droplet size, as demonstrated in Fig. 14 (a) and 14(b). 
Different from droplet trajectories I and II, Figs. 15 and 16 show the 
time evolutions of trajectory III, in which the droplet first interacts with 
the deflagrative surface and then leaves the refill zone through the triple 
point. The results are from case B15 and the initial droplet diameter is 
d
0
d
= 15 μ m, larger than those in trajectories I and II. Similar to the 
droplet in trajectory II, this droplet is also injected far from the 
propagating detonation wave. At its early stage ( t ≤ 5.03 ms), the 
droplet temperature decreases gradually towards local gas temperature, 
and the evaporation rate ˙m
d 
is almost zero (see Fig. 16 b), as observed in 
trajectories I and II. Nevertheless, when the droplet approaches the 
triple point (e.g. at t = 5.04 ms, marked as c in Fig. 16 ), its temperature, 
velocity and evaporation rate abruptly increase, as seen from Fig. 16 . 
Considerable interphase velocity difference is observed from Fig. 16 (f) 
at that instant. When it enters the burned area, like at t = 5.05 ms and 
5.07 ms in Fig. 15 (d) and 15(e), the evaporation is greatly enhanced, 
leading to considerably reduced droplet size. This can be seen from 
Fig. 16 (a) and 16(b). The oscillation of ˙m
d 
results from the spatially non- 
uniform thermo-chemical compositions (e.g. temperature) behind the 
detonation wave. Meanwhile, the droplet velocities are generally high, 
in line with the local gas flows near the slip line (hence low interphase 
velocity difference). Finally, the droplet is completely vaporized at t =
5.084 ms in Fig. 15 (f). 
The last type of droplet trajectory observed from our results is shown 
in Figs. 17 and 18 , termed as droplet trajectory IV. The results are from 
the three-waved case C40 with ϕ
g 
= 0.6 and d
0
= 40 μ m. After the 
droplet is injected from inlet at t = 11.58 ms, it travels through the 
detonation front immediately (see Fig. 17 a and 17b), which marked as 
d in Fig. 18 . In the detonated gas, the droplet temperature quickly rea -
ches the boiling point and evaporation rate increases accordingly, 
0.0
2.0x10-8
4.0x10-8
6.0x10-8
mdot,d (kg/s)
(b)
c
0
200
400
600
800
Uy (m/s)
(d)
c
0
200
400
600
Ux (m/s)
(c)
c
4.92 4.96 5.00 5.04 5.08
0
200
400
600
800
1000
Uc (m/s)
t (ms)
(e)
c
4.92 4.96 5.00 5.04 5.08
-200
0
200
400
600
800
Uc-Ud (m/s)
t (ms)
(f)
c
0
50
100
150
200
250
300
d2
d (μm2)
(a)
c
Fig. 16. Time histories of (a) diameter squared, (b) evaporation rate, (c) x -direction velocity, (d) y -direction velocity, (e) local gas velocity magnitude, (f) interphase 
velocity difference in trajectory III. 
Q. Meng et al.

<!-- PDF_PAGE: 13 -->

Fuel 290 (2021) 119808
13
peaking at about t = 11.60 ms. This can be clearly seen from Fig. 18 (a) 
and 18(b). Between t = 11.59 ms and 11.65 ms, the droplet diameter and 
x -direction velocity continuously decrease. However, the y -direction 
velocity increases due to the expansion of the detonation product gas. 
The second milestone of this droplet is to cross the oblique shock wave 
connecting with the next detonation wave, and this instant is marked as 
e in Fig. 18 . This is manifested by abruptly increased droplet and gas 
velocities, evaporation rate ˙m
d 
also slightly increases, due to the high 
temperature in the post-shock zone, but decays quickly due to the 
quickly reduced droplet diameter. 
Table 4 summarizes the key time and length scales of droplet and 
rotating detonation wave in the foregoing four trajectories. Several 
interesting phenomena merit further discussion here. Firstly, the 
computed evaporation time of trajectory I is τ
sim
ev
≈ 2 μ s , much shorter 
than the theoretical value, i.e. τ
est
ev
≈ 5 μ s , calculated from droplet evap -
oration in stagnant flows and therefore Sh ≈ 2 . 0 [62] 
τ
est
ev
=
ρ
d
d
0
d
2
8 ρ
s
D
ab
ln ( 1 + X
r
)
, (35)  
where ρ
s
, X
r 
and D
ab 
are estimated with the droplet evaporation tem -
perature. Moreover, in trajectory II, τ
sim
ev
= 20 μ s is close to τ
est
ev 
from Eq. 
(35) . This is justifiable since the droplet has relatively low interphase 
velocity difference (low Re
d 
and therefore a good approximation of 
Sh ≈ 2). However, in trajectories III and IV, τ
sim
ev 
are 33% and 13% higher 
than τ
est
ev
, respectively. Different from the droplets in trajectories I and II, 
those in trajectories III and IV mainly travel beyond the refill zone. This 
may be affected by the variable surrounding gas atmosphere behind the 
detonation wave as illustrated in Figs. 15 and 17 . However, Eq. (35) still 
provides good estimates for droplet evaporation time in rotation deto -
nation combustion. 
Secondly, it is of great relevance to enhance the droplet residence 
time in the fuel refill zone in order to increase the liquid fuel utilization 
and detonated fuel fraction in RDE ’ s. As listed in Table 4 , the total 
residence times τ
tot
res 
of droplets in the four trajectories are 48, 123, 149 
and 82 μ s respectively, and the refill zone residence time τ
ref
res 
respectively 
accounts for about 96%, 100%, 72% and 5% of them. Note that if τ
ref
res
<
τ
tot
res 
(the droplet does not fully vaporize in the refill zone), then τ
ref
res 
can be 
approximated from τ
res
, i.e. 
τ
ref
res
≈ τ
res
=
l
i
D
det
, (36)  
where l
i 
is the distance between the droplet injector and the instanta -
neous detonation wave and l
i 
is always less than the refill zone length, i. 
e. l
i
≤ l
f
. Equation (36) holds when the y -direction velocity component is 
low and its validity can be confirmed from close values of τ
res 
and τ
ref
res 
in 
Table 4 . Fig. 19 schematically shows the distribution of liquid fuel 
droplets in the triangular refill zone, and three categories of droplets can 
be loosely grouped, marked with 1, 2 and 3. The first category of 
droplets (in yellow in Fig. 19 ) generally have high τ
ref
res
, which lies at the 
tips of the spray jets and are injected near the right end of the instan -
taneous refill zone (hence with large l
i
). Two extremes, the oldest and 
youngest droplets (in pink and blue respectively), are near the triple 
point and at the rightmost end of the zone, respectively. The duration 
with which they interact with, or affected by, the deflagration surface 
can be approximated as τ
ref
res
. These droplets may be fully vaporized in -
side the refill zone (e.g. trajectory II), or escape near the triple point (e.g. 
trajectory III), and have significant influence on detonated fuel fraction 
as discussed in Section 5.3 . Either fate is expected to have small kinetic 
contributions for detonative combustion, and therefore should be 
avoided in practical liquid RDE technologies. 
For the third droplet category (in green), they are just injected into 
the refill zone and featured by small l
i 
and τ
ref
res 
(e.g. trajectory IV). 
Accordingly, unless they are perfectly atomized and sprayed with small 
d
0
d
, they would have limited time to be heated and vaporized, leading to 
negligible vapour addition and subsequent mixing with oxidant for the 
encroaching RDW. On the contrary, the evaporative cooling and inter -
phase momentum exchange may adversely affect the stable propagation 
of detonation wave base near the injector. The second category of 
droplets with intermediate l
i 
have longer τ
ref
res 
(compared to the second 
category) and do not directly interact with deflagration surface 
(compared to the first category). It is expected to play a major role in 
providing vaporized fuel before or on RDW arrival. Therefore, how to 
implement and optimize in-situ droplet evaporation inside the refill zone 
of practical RDE combustors deserves further investigations using both 
computational and experimental methods. 
5.5. Droplet dispersion height in rotating detonation combustor 
Fig. 20 shows the variations of Sauter Mean Diameter (SMD, d
32
) 
along the RDE height direction ( y -direction) for different pre-vaporized 
gas equivalence ratios and initial droplet diameters. Here SMD is 
calculated based on the ratio of the volume to surface area of the 
droplets distributed along the entire x -direction at a fixed height. Note 
that the mean detonation wave height is marked by a rectangle and the 
entire RDE height is y = 99 mm. It is seen that the droplet SMD are 
almost unchanged initially when the axial distance is less than the RDW 
height. This is because most of these droplets are within the fuel refill 
zone and limited droplet vaporization occurs due to the low gas tem -
perature. The SMD decreases rapidly when the droplets are beyond the 
detonation wave height. This can be justified by the fact that the droplets 
are surrounded by hot detonation product and the droplets keep evap -
orating there. Small-sized droplets are completely vaporized before 
arriving the outlet ( y = 99 mm). However, larger droplets escape from 
outlet and this would weaken the fuel utilization. It is also found that all 
the droplets are vaporized within the RDE combustor for high ϕ
g 
is 0.6 
and above (see Fig. 20 c – e). Therefore, increasing droplet pre- 
evaporation in the liquid fuel supply can promote the in-situ 
(μm)
0           10          20            30          40
50       800       1500        2300        3000
(K)
t = 11.582 ms(a)
(b)
(c)
(d)
(e)
(f)
t = 11.59 ms
t = 11.61 ms
t = 11.63 ms
t = 11.65 ms
t = 11.66 ms
Fig. 17. Droplet trajectory IV: cross the detonation wave and interact with the 
shock wave. Results from case C40. Arrows indicate the droplet location. Image 
size: 288 mm × 40 mm. 
Q. Meng et al.

<!-- PDF_PAGE: 14 -->

Fuel 290 (2021) 119808
14
vaporization of the liquid droplets inside the chamber. 
Fig. 21 further shows the variations of the droplet dispersion height 
( H ) for all the simulated cases. H is defined as the y -direction distance 
between the RDE head end and the critical axial height beyond which no 
droplets are dispersed (i.e. d
32
= 0 in Fig. 20 ). We can find that H in -
creases monotonically as the initial droplet size d
0
d 
increases for a fixed 
pre-vaporized equivalence ratio ϕ
g 
(i.e. within the same group). In 
addition, with increased ϕ
g 
from groups A to E, H decreases gradually. If 
the droplets cannot be completely vaporized before the RDE exit, then 
we assume H = 99 mm, which may occur when d
0
d 
is large and/or ϕ
g 
is 
small, e.g. cases A50, A40, B50 and B40 as shown in Fig. 21 . This does 
not only deteriorate the fuel utilization but also adversely affects or even 
damages the downstream structures, e.g. exit nozzle or turbine blades 
when the detonation combustor is integrated with turbomachinery. 
Therefore, from RDE design perspective, besides the general re -
quirements of the detonation wave height discussed by Bykovskii et al. 
[58] , optimal chamber height of liquid fuelled RDE should be deter -
mined, by considering the fuel atomization and evaporation character -
istics. This topic merits further studies in the future work. 
0.0
4.0x10-7
8.0x10-7
1.2x10-6
1.6x10-6
(b)
mdot,d (kg/s)
d e
-400
-200
0
200
400
e
(c)
Ux (m/s)
d
200
400
600
800
(d)
Uy (m/s)
d
e
11.58 11.60 11.62 11.64 11.66
200
400
600
800
1000 (e)
Uc (m/s)
t (ms)
d
e
11.58 11.60 11.62 11.64 11.66
-200
0
200
400
600 (f)
Uc-Ud (m/s)
t (ms)
d e
0
400
800
1200
1600
2000
(a)
d2
d (μm2)
d
e
Fig. 18. Time histories of (a) diameter squared, (b) evaporation rate, (c) x -direction velocity, (d) y -direction velocity, (e) local gas velocity magnitude, (f) interphase 
velocity difference in trajectory IV. 
Table 4 
Time and length scales in various droplet trajectories.  
Trajectory Droplet evaporation time ( µ s) Droplet residence time ( µ s) RDW speed D
det 
(m/ 
s)  
Refill zone length l
f 
(m)  
Injection distance l
i 
(m)  
Present simulation 
τ
sim
ev  
Theoretical 
Estimation τ
est
ev  
Whole 
domain τ
tot
res  
Refill zone 
τ
ref
res  
I (5 µ m) 2 5 48 46 1390  0.193  0.064 
II (5 µ m) 20 22 123 123 1390  0.193  0.193 
III (15 µ m) 40 30 149 107 1376  0.200  0.158 
IV (40 µ m) 76 67 82 4 1516  0.060  0.004  
Q. Meng et al.

<!-- PDF_PAGE: 15 -->

Fuel 290 (2021) 119808
15
6. Conclusions 
Eulerian  Lagrangian modelling of two-dimensional rotating deto -
native combustion fuelled with partially pre-vaporized n -heptane sprays 
and gaseous hydrogen is performed. Our emphasis is laid on detonation 
wave propagation in heterogeneous mixtures and droplet dynamics in 
rotating detonation combustion. Different pre-vaporized n -heptane 
equivalence ratios ( ϕ
g
) and droplet diameters ( d
0
d
) are investigated. 
The results show that when the droplets are small, they are fully 
vaporized by the detonation wave. However, when the diameter is 
relatively large and/or the detonation wave number is bifurcated, liquid 
droplets are observable beyond the refill zone. They continue evapo -
rating in the post-detonated gas and the vapour is deflagrated. More -
over, the detonation propagation speed is increased with ϕ
g
. When ϕ
g 
is 
Oblique 
shock wave
Deﬂagration 
surfaceDetonation 
wave
①
②
③
Oldest droplet (largest )
Youngest droplet (smallest )
Fig. 19. Schematic of droplet distribution in the fuel refill zone of rotating 
detonation combustion. 
0 20 40 60 80 100 120
0
10
20
30
40
50
d32 (μm)
y (mm)
5μm
10μm
15μm
20μm
30μm
40μm
50μm
(c) Φg=0.6
0 20 40 60 80 100 120
0
10
20
30
40
50
d32 (μm)
y (mm)
5μm
10μm
15μm
20μm
30μm
40μm
50μm
(a) Φg=0.35
0 20 40 60 80 100 120
0
10
20
30
40
50
d32 (μm)
y (mm)
5μm
10μm
15μm
20μm
30μm
40μm
50μm
(d) Φg=0.8
0 20 40 60 80 100 120
0
10
20
30
40
50
d32 (μm)
y (mm)
5μm
10μm
15μm
20μm
30μm
40μm
50μm
(e) Φg=1.0
0 20 40 60 80 100 120
0
10
20
30
40
50
d32 (μm)
y (mm)
5μm
10μm
15μm
20μm
30μm
40μm
50μm
(b) Φg=0.4
Fig. 20. Profiles of Sauter mean diameter along the RDE height direction.  
Q. Meng et al.

<!-- PDF_PAGE: 16 -->

Fuel 290 (2021) 119808
16
low (e.g. 0.35 and 0.4), the propagation speed is enhanced in small-sized 
sprays, compared to the purely gaseous detonation. The velocity deficit 
increases with d
0
d 
and/or ϕ
g
, and varies from 5% to 30% in our studied 
cases. 
It is also found that the detonated fuel fraction increases with ϕ
g
. 
However, there exists a critical droplet diameter (about 20 µ m), with 
which the detonated fuel fraction is lowest. Over 70% n -heptane is 
detonated in the simulated cases. Four typical droplet trajectories in 
rotating detonation combustion are identified, and they are character -
ized by various evaporation times, residence times and their interactions 
with the basic structures in the detonation combustion field. Inside the 
refill zone, three droplet categories are qualitatively identified. Droplets 
injected at the right end of the refill zone directly interact with the 
deflagration surface and have relatively long residence time. However, 
droplets injected closer to the detonation front have insufficient time to 
be heated and vaporized in the refill zone. Further studies are needed to 
develop efficient technologies to enhance the in-situ droplet evaporation 
during the refill period for practical RDE implementations. 
Our results also demonstrate that when ϕ
g 
is low (0.35 and 0.4) and 
d
0
d 
is large (40 and 50 µ m), the liquid fuel droplets may disperse toward 
the domain exit. When ϕ
g 
is high, they can be fully evaporated inside the 
chamber. Furthermore, the droplet dispersion height is reduced when 
the pre-evaporation degree becomes high, whilst it increases when d
0
d 
is 
increased. 
CRediT authorship contribution statement 
Qingyang Meng: Conceptualization, Methodology, Writing - orig -
inal draft, Visualization, Investigation. Majie Zhao: Software. Hongtao 
Zheng: Supervision, Funding acquisition. Huangwei Zhang: Writing - 
review & editing, Supervision, Project administration, Funding 
acquisition. 
Declaration of Competing Interest 
The authors declare that they have no known competing financial 
interests or personal relationships that could have appeared to influence 
the work reported in this paper. 
Acknowledgments 
This work used the computational resources of the National Super -
computing Centre, Singapore (https://www.nscc.sg). QM is supported 
by the China Scholarship Council (No. 201906680008). 
References 
[1] Anand V, Gutmark E. Rotating detonation combustors and their similarities to 
rocket instabilities. Prog Energy Combust 2019;73:182 – 234 . 
[2] Wola ´nski P. Detonative propulsion. Proc Combust Inst 2013;34:125 – 58 . 
[3] Rankin BA, Richardson DR, Caswell AW, Naples AG, Hoke JL, Schauer FR. 
Chemiluminescence imaging of an optically accessible non-premixed rotating 
detonation engine. Combust Flame 2017;176:12 – 22 . 
[4] Kawasaki A, Inakawa T, Kasahara J, Goto K, Matsuoka K, Matsuo A, et al. Critical 
condition of inner cylinder radius for sustaining rotating detonation waves in 
rotating detonation engine thruster. Proc Combust Inst 2019;37:3461 – 9 . 
[5] Bluemner R, Bohon MD, Paschereit CO, Gutmark EJ. Effect of inlet and outlet 
boundary conditions on rotating detonation combustion. Combust Flame 2020; 
216:300 – 15 . 
[6] Zheng Y, Wang C, Wang Y, Liu Y, Yan Z. Numerical research of rotating detonation 
initiation processes with different injection patterns. Int J Hydrogen Energy 2019; 
44:15536 – 52 . 
[7] Driscoll R, Aghasi P, St George A, Gutmark EJ. Three-dimensional, numerical 
investigation of reactant injection variation in a h2/air rotating detonation engine. 
Int J Hydrogen Energy 2016;41:5162 – 75 . 
[8] Schwer DA, Kailasanath K, Towards non-premixed injection modeling of rotating 
detonation engines, 51st AIAA/SAE/ASEE Joint Propulsion Conference (2015), 
paper 3782. 
[9] Sun B, Ma H. Two-dimensional numerical study of two-phase rotating detonation 
wave with different injections. AIP Adv 2019;9:115307 . 
[10] Zhao M, Li JM, Teo CJ, Khoo BC, Zhang H. Effects of variable total pressures on 
instability and extinction of rotating detonation combustion. Flow Turbul Combust 
2020;104:261 – 90 . 
[11] Yi TH, Lou J, Turangan C, Choi JY, Wolanski P. Propulsive performance of a 
continuously rotating detonation engine. J Propuls Power 2011;27:171 – 81 . 
[12] Jourdaine N, Tsuboi N, Ozawa K, Kojima T, Hayashi AK. Three-dimensional 
numerical thrust performance analysis of hydrogen fuel mixture rotating 
detonation engine with aerospike nozzle. Proc Combust Inst 2019;37:3443 – 51 . 
[13] Katta VR, Cho KY, Hoke JL, Codoni JR, Schauer FR, Roquemore WM. Effect of 
increasing channel width on the structure of rotating detonation wave. Proc 
Combust Inst 2019;37:3575 – 83 . 
[14] Kaemming T, Fotia ML, Hoke J, Schauer F. Thermodynamic modeling of a rotating 
detonation engine through a reduced-order approach. J Propuls Power 2017;33: 
1170 – 8 . 
[15] Nordeen CA, Schwer D, Schauer F, Hoke J, Barber T, Cetegen B. Thermodynamic 
model of a rotating detonation engine. Combust Explos Shock 2014;50:568 – 77 . 
[16] Shen PW, Adamson Jr T. Theoretical analysis of a rotating two-phase detonation in 
liquid rocket motors. Astronaut Acta 1972;17:715 – 28 . 
[17] Zhou R, Wang JP. Numerical investigation of flow particle paths and 
thermodynamic performance of continuously rotating detonation engines. 
Combust Flame 2012;159:3632 – 45 . 
[18] Bykovskii FA, Zhdan SA, Vedernikov EF. Continuous spin detonation of fuel-air 
mixtures. Explos Shock Waves 2006;42:463 – 71 . 
[19] Bykovskii FA, Zhdan SA, Vedernikov EF. Continuous detonation of the liquid 
kerosene — air mixture with addition of hydrogen or syngas. Combust Explos Shock 
2019;55:589 – 98 . 
[20] Bykovskii FA, Zhdan SA, Vedernikov EF. Continuous spin detonation of a 
heterogeneous kerosene – air mixture with addition of hydrogen. Combust Explos 
Shock 2016;52:371 – 3 . 
[21] Kindracki J. Experimental studies of kerosene injection into a model of a 
detonation chamber. J Power Technol 2012;92:80 – 9 . 
[22] Kindracki J. Experimental research on rotating detonation in liquid fuel – gaseous 
air mixtures. Aerosp Sci Technol 2015;43:445 – 53 . 
[23] Li JM, Chang, Li L, Yang Y, Teo CJ, Khoo BC. Investigation of injection strategy for 
liquid-fuel rotating detonation engine, AIAA Aerospace Sciences Meeting (2018), 
paper 0403. 
[24] Xue S, Liu H, Zhou L, Yang W, Hu H, Yan Y. Experimental research on rotating 
detonation with liquid hypergolic propellants. Chin J Aeronaut 2018;31:2199 – 205 . 
[25] Hayashi AK, Tsuboi N, Dzieminska E. Numerical study on JP-10/air detonation and 
rotating detonation engine. AIAA J 2020:1 – 17 . 
[26] Zhao M, Zhang H. Modelling rotating detonative combustion fueled by partially 
pre-vaporized n-heptane sprays, Accepted by 38th International Symposium on 
Combustion, under reviewed by Proc. Combust. Inst. (2021). 
[27] W. Sutherland, LII. The viscosity of gases and molecular force, The London, 
Edinburgh, and Dublin Philosophical Magazine and Journal of Science 36 (2009) 
507-531. 
[28] Reid RC, Prausnitz JM, Poling BE. The properties of gases and liquids, McGraw- 
Hill. New York: U.S.A; 2007 . 
[29] McBride BJ, Coefficients for calculating thermodynamic and transport properties of 
individual species, Report No. NASA-TM-4513, NASA Lewis Research Center, 
Cleveland, OH, USA, 1993. 
[30] Macpherson GB, Nordin N, Weller HG. Particle tracking in unstructured, arbitrary 
polyhedral meshes for use in cfd and molecular dynamics. Commu Numer Mechods 
Eng 2009;25:263 – 73 . 
[31] Crowe CT, Schwarzkopf JD, Sommerfeld M, Tsuji Y. Multiphase flows with droplets 
and particles. Boca Raton, USA: CRC Press; 2011 . 
[32] Liu AB, Mather D, Reitz RD, Modeling the effects of drop drag and breakup on fuel 
sprays, 102 (1993) 83-95. 
[33] Doble M. Perry ’ s chemical engineers ’ handbook. New York, U.S.A.: McGraw-Hill; 
2007 . 
[34] Ranz W, Marshall WR, Evaporation from drops, 48 (1952) 141-146. 
0 10 20 30 40 50
0
10
20
30
40
50
60
70
80
90
100
H (mm)
d0
d (μm)
Outlet Height
Case Group A
B
C D
E
RDW number
Fig. 21. Change of droplet dispersion height with initial droplet diameter .  
Q. Meng et al.

<!-- PDF_PAGE: 17 -->

Fuel 290 (2021) 119808
17
[35] Weller HG, Tabor G, Jasak H, Fureby C. A tensorial approach to computational 
continuum mechanics using object-oriented techniques, 12 (1998) 620-631. 
[36] Greenshields CJ, Weller HG, Gasparini L, Reese JM. Implementation of semi- 
discrete, non-staggered central schemes in a colocated, polyhedral, finite volume 
framework, for high-speed viscous flows. Int J Numer Meth Fluids 2010;63:1–21. 
[37] Kurganov A, Noelle S, Petrova G. Semidiscrete central-upwind schemes for 
hyperbolic conservation laws and hamilton–jacobi equations, 23 (2001) 707-740. 
[38] Zhao M, Zhang H. Origin and chaotic propagation of multiple rotating detonation 
waves in hydrogen/air mixtures. Fuel 2020;275:117986. 
[39] Marcantoni LG, Tamagno J, Elaskar S, Rhocentralrffoam: An openfoam solver for 
high speed chemically active flows–simulation of planar detonations–, 219 (2017) 
209-222. 
[40] Huang Z, Zhao M, Xu Y, Li G, Zhang H. Eulerian-Lagrangian modelling of 
detonative combustion in two-phase gas-droplet mixtures with OpenFOAM: 
Validations and verifications. Fuel 2021;286:119402. 
[41] Ma F, Choi JY, Yang V. Propulsive performance of airbreathing pulse detonation 
engines. J Propuls Power 2006;22:1188–203. 
[42] Westbrook CK, Dryer FL. Simplified reaction mechanisms for the oxidation of 
hydrocarbon fuels in flames. Combust Sci Technol 2007;27:31–43. 
[43] Meng Q, Zhao N, Zheng H, Yang J, Li Z, Deng F. A numerical study of rotating 
detonation wave with different numbers of fuel holes. Aerosp Sci Technol 2019;93: 
105301. 
[44] Liu S, Hewson JC, Chen JH, Pitsch H. Effects of strain rate on high-pressure 
nonpremixed n-heptane autoignition in counterflow. Combust Flame 2004;137: 
320–39. 
[45] Schwer DA. Multi-dimensional simulations of liquid-fueled JP10/oxygen 
detonations, AIAA Propulsion and Energy 2019 Forum (2019), paper 4042. 
[46] Ren Z, Wang B, Xiang G, Zheng L. Effect of the multiphase composition in a 
premixed fuel–air stream on wedge-induced oblique detonation stabilisation. 
J Fluid Mech 2018;846:411–27. 
[47] Bohon MD, Bluemner R, Paschereit CO, Gutmark EJ. High-speed imaging of wave 
modes in an rdc. Exp Therm Fluid Sci 2019;102:28–37. 
[48] Deng L, Ma H, Xu C, Liu X, Zhou C. The feasibility of mode control in rotating 
detonation engine. Appl Therm Eng 2018;129:1538–50. 
[49] Deng L, Ma H, Xu C, Zhou C, Liu X. Investigation on the propagation process of 
rotating detonation wave. Acta Astronaut 2017;139:278–87. 
[50] Yao S, Wang J. Multiple ignitions and the stability of rotating detonation waves. 
Appl Therm Eng 2016;108:927–36. 
[51] Yao S, Liu M, Wang J. Numerical investigation of spontaneous formation of 
multiple detonation wave fronts in rotating detonation engine. Combust Sci 
Technol 2015;187:1867–78. 
[52] Schwer D, Kailasanath K. Numerical investigation of the physics of rotating- 
detonation-engines. Proc Combust Inst 2011;33:2195–202. 
[53] Hishida M, Fujiwara T, Wolanski P. Fundamentals of rotating detonations. Shock 
Waves 2009;19:1–10. 
[54] Tsuboi N, Watanabe Y, Kojima T, Hayashi AK. Numerical estimation of the thrust 
performance on a rotating detonation engine for a hydrogen–oxygen mixture. Proc 
Combust Inst 2015;35:2005–13. 
[55] J. Shepherd, Copyright © 1993-2020 by California Institute of Technology, https:// 
shepherd.Caltech. Edu/edl/publicresources/sdt/. 
[56] Watanabe H, Matsuo A, Matsuoka K, Kawasaki A, Kasahara J. Numerical 
investigation on propagation behavior of gaseous detonation in water spray. Proc 
Combust Inst 2019;37:3617–26. 
[57] D.A. Schwer, E. O’Fallon Jr, D. Kessler. Liquid-fueled detonation modeling at the us 
naval research laboratory, Report No. NRL/MR/6041–18-9816, Naval Research 
Laboratory, Washington, D.C., USA, 2018. 
[58] Bykovskii FA, Zhdan SA, Vedernikov EF. Continuous spin detonations. J Propuls 
Power 2006;22:1204–16. 
[59] Li Q, Liu P, Zhang H. Further investigations on the interface instability between 
fresh injections and burnt products in 2-d rotating detonation. Comput Fluids 
2018;170:261–72. 
[60] Kailasanath K. Liquid-fueled detonations in tubes. J Propuls Power 2006;22: 
1261–8. 
[61] Gubin SA, Sichel M. Calculation of the detonation velocity of a mixture of liquid 
fuel droplets and a gaseous oxidizer. Combust Sci Technol 2007;17:109–17. 
[62] Rochette B, Riber E, Cuenot B. Effect of non-zero relative velocity on the flame 
speed of two-phase laminar flames. Proc Combust Inst 2019;37:3393–400. 
Q. Meng et al.
