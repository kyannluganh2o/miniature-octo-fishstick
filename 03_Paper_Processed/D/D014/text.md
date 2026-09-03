<!-- PDF_PAGE: 1 -->

Characterization of droplet kinematics and spatial distribution in a 
two-phase ethanol-fueled rotating detonation flow field
Jianghong Li
a , b
, Songbai Yao
a , c , *
, Ying Lei
a , c
, Jingtian Yu
a , c
, Wenwu Zhang
a , c
a
Ningbo Institute of Materials Technology and Engineering, Chinese Academy of Sciences, Ningbo, 315201, China
b
Faculty of Mechanical Engineering and Mechanics, Ningbo University, Ningbo, 315211, China
c
University of Chinese Academy of Sciences, Beijing, 100049, China
ARTICLE INFO
Handling Editor: Dr M Djukic
Keywords:
Rotating detonation
Two-phase flow
Droplet distribution
Droplet kinematics
Hydrogen carrier
Ethanol
ABSTRACT
We investigate the behavior of evaporating droplets in a two-phase rotating detonation engine (RDE) fueled by 
liquid ethanol, a renewable energy source and hydrogen carrier with relatively high energy density. In the 
present study, we conduct an Eulerian-Lagrangian simulation to examine the spatial distribution and kinematic 
motion of ethanol droplets within a rotating detonation flow field over a wide range of equivalence ratios of 
0.9 – 1.6. The droplets are tracked as they are injected into the flow field, with important droplet parameters 
analyzed comprehensively and correlatively as they evaporate and move downstream. The ethanol droplets are 
then classified into three main categories: leading-edge droplets near the detonation front, trailing-edge droplets 
in the post-detonation region that are newly injected, and the remaining droplets that occupy the majority of the 
fuel refill zone. The droplet distribution patterns are found to shift as the equivalence ratio changes. Specifically, 
as the equivalence ratio increases, droplet clusters accumulate and gradually move downstream. Under the fuel- 
rich conditions, particularly at the equivalence ratios between 1.5 and 1.6, excess droplets near the detonation 
front result in prolonged evaporation, which intensifies and tilts the detonation front, causing localized explo -
sions that disrupt the flow field and droplet injection.
Nomenclature
RDE Rotating detonation engine
RDC Rotating detonation combustor
RDW Rotating detonation wave
OSW Oblique shock wave
SMD Sauter mean diameter
C-J Chapman – Jouguet
1. Introduction
The rotating detonation engine (RDE) is one of the potential new 
propulsion technologies to improve the thermodynamical efficiency of 
existing combustion engines [ 1 , 2 ]. A significant number of RDE studies 
have utilized gaseous fuels, particularly hydrogen, such as Refs. [ 3 – 9 ]. 
To broaden the possibilities for diverse engine architectures, including 
air-breathing engines, gas turbines, and rockets, there has been a 
gradual shift toward using more practical liquid propellants.
However, as noted by Harroun and Heister [ 10 ], liquid propellants 
traditionally used in combustion engines cannot be directly adapted for 
use in an RDE, and it also adds complexity to liquid-fueled RDE systems. 
In the early work of Bykovskii et al. [ 11 ], they conducted RDE experi -
ments involving various liquid propellants such as kerosene, gasoline, 
and diesel. Fine atomization and rapid mixing were found to be crucial 
for achieving stable liquid-fueled rotating detonations. Kindracki [ 12 ] 
and Bykovskii et al. [ 13 ] successfully achieved sustained rotating det -
onations by introducing gaseous hydrogen into a kerosene-air mixture. 
Kindracki et al. [ 14 ] also examined the role of hydrogen addition in 
kerosene-fueled RDEs, highlighting its environmental benefits and 
suitability for liquid-fueled RDE applications. Ishihara et al. [ 15 ] 
investigated the thrust performance of a cylindrical RDE using ethanol 
and liquid nitrous oxide as propellants, achieving a maximum thrust of 
294 N, with a maximum specific impulse of 148 s. Han et al. [ 16 ] 
explored the characteristics and combustion efficiency of the liquid 
kerosene/oxygen-enriched air RDE in various modes. Zhao et al. [ 17 ] 
found that increasing the exit convergent ratio in a kerosene-fueled RDE 
with oxygen-enriched air prolonged the time required for the 
* Corresponding author. Ningbo Institute of Materials Technology and Engineering, Chinese Academy of Sciences, Ningbo 315201, China.
E-mail address: yaosongbai@nimte.ac.cn (S. Yao). 
Contents lists available at ScienceDirect
International Journal of Hydrogen Energy
journal homepage: www.else vier.com/loc ate/he
https://doi.org/10.1016/j.ijhydene.2025.01.004
Received 11 October 2024; Received in revised form 7 December 2024; Accepted 1 January 2025  
International Journal of Hydrogen Energy 102 (2025) 260–273 
Available online 11 January 2025 
0360-3199/© 2025 Hydrogen Energy Publications LLC. Published by Elsevier Ltd. All rights are reserved, including those for text and data mining, AI training, and 
similar technologies.

<!-- PDF_PAGE: 2 -->

establishment of the detonation wave. Perkowski et al. [ 18 ] presented 
experimental results for an RDE using liquid kerosene and pre-heated 
air, observing various combustion modes, including deflagration, 
pulsed combustion, high-frequency instabilities, and stable detonation. 
Zhou et al. [ 19 ] investigated the pressure gain characteristics of a 
kerosene/pre-heated air RDE, measuring total pressure gains for 
different configurations using Equivalent Available Pressure (EAP). 
Similarly, He et al. [ 20 ] analyzed the total pressure gain in rotating 
detonation combustors (RDCs) with dilution holes, examining the effects 
of pressure ratios and equivalence ratios across four different models. Li 
et al. [ 21 ] conducted a long-term test on a kerosene-fueled rotating 
detonation engine using incoming air at a total temperature of 620 K. 
Huang et al. [ 22 ] conducted an analysis of an RDE fueled by ammonia, 
successfully demonstrating ammonia-oxygen rotating detonations in a 
cylindrical chamber with a Laval nozzle.
Numerical simulations have become an invaluable tool for studying 
the multi-scale physics of the rotating detonation waves (RDW) [ 23 , 24 ], 
providing critical insights into achieving and sustaining stable detona -
tion waves, as well as maximizing the thrust performance of 
liquid-fueled RDEs. For example, the feasibility of kerosene-fueled RDEs 
with hydrogen addition using a realistic geometry was demonstrated in 
the simulations by Salvadori et al. [ 25 ]. Yao et al. [ 26 ] evaluated the 
effects of droplet evaporation on the structure and thrust performance of 
the hydrogen-enhanced RDE with liquid kerosene. Prakash et al. [ 27 ] 
investigated the performance of an RDE fueled by liquid RP-2 and 
gaseous oxygen through high-fidelity numerical simulations. Malik et al. 
[ 28 ] examined the dynamics of detonation waves driven by aerosolized 
RP-2 fuel sprays. Their study employed an unlike-doublet impinging-jet 
injector to atomize RP-2 and water into aerosolized droplets, focusing on 
how these droplets interact with the detonation wave. Meng et al. [ 29 ] 
explored two-phase RDE physics using partially pre-vaporized n-hep -
tane and hydrogen. They observed that smaller droplets fully vaporized 
in the detonation wave, while larger droplets persisted beyond the refill 
zone, affecting the overall detonation dynamics. In our previous studies 
[ 26 , 30 ], we demonstrated that the evaporation process of larger drop -
lets could alter the detonation front structure, sometimes resulting in a 
dual reacting front in two-phase RDWs. Salvadori et al. [ 31 ] analyzed 
the sustainability of kerosene-fueled detonation waves when the injec -
tion of the hydrogen-enriched fuel is reduced. Their research illumi -
nated the roles of hydrogen and kerosene in sustaining rotating 
detonations. Gao et al. [ 32 ] investigated the role of the forward shock 
wave in a non-premixed RDE with a gaseous kerosene-air mixture. Wang 
et al. [ 33 ] investigated pre-heated kerosene injection in a rotating 
detonation scramjet engine, focusing on the atomization and evapora -
tion of kerosene in a supersonic air intake at Mach 2. Upon examining 
the stability and propagation of kerosene-fueled rotating detonation 
waves, Wen et al. [ 34 ] proposed a stability criterion to establish a sta -
bility regime.
Ethanol, as a rocket engine propellant, has performance slightly 
inferior to kerosene but has garnered renewed attention due to its 
environmental advantages as a renewable fuel with low emissions. For 
instance, liquid ethanol has been utilized in rocket engines for launch 
vehicles [ 35 , 36 ]; also, studies have explored the combustion charac -
teristics of scramjets fueled by liquid ethanol [ 37 ]. Recently, Sato and 
collaborators [ 38 , 39 ] conducted a series of experiments on RDEs using 
liquid ethanol and achieved stable rotating detonations. In our previous 
investigations [ 30 , 40 , 41 ], we focused on the behavior of a liquid 
ethanol-fueled RDE using pre-heated air or hydrogen addition for 
combustion enhancement. We examined the shock interactions, the 
re-initiation mechanism, and the effects of incomplete evaporation of 
ethanol droplets on the structure of the two-phase RDW under varying 
fuel conditions. However, previous studies, including our own, have 
predominantly focused on the evaporation characteristics of droplet 
ensembles under varying working conditions, without adequately 
exploring the kinematics of individual droplets in the distributed space, 
including their motion, distribution, and changes in physical state over 
time. In this study, we address this gap by tracking and analyzing 
grouped droplets, with a specific focus on how their physical states and 
distributions evolve after injection, which is expected to provide a more 
comprehensive understanding of the diverse behaviors of droplets 
throughout the entire fuel refill zone.
2. Numerical methods
2.1. Mathematical formulations
In this study, the three-dimensional RDC is reduced to a two- 
dimensional domain with a circumferential length of 192 mm, i.e., D 
≈ 61.2 mm, and a height of 120 mm, as shown in Fig. 1 . This assumption 
is justified by the fact that the thickness of the RDC is typically an order 
of magnitude smaller than its diameter and length, such as Ref. [ 42 ]. The 
two-phase rotating detonation flow field is described using a 
Lagrangian-Eulerian approach, where the Navier-Stokes equations are 
solved for the continuous carrier phase, i.e.,
Continuity equation: 
∂ ρ
∂ t
+ ∇ • [ ρ V ] = S
m
, (1) 
where ρ is the gaseous density, V is the velocity vector.
Momentum equation: 
∂ ( ρ V )
∂ t
+ ∇ • [( ρ V V )] + ∇ p  ∇ • τ = S
u
, (2) 
where p is the pressure, τ is the viscous stress tensor and τ = μ
(
(∇ V ) 
(∇ V )
T

2
3
(∇ ⋅ V ) I
)
, and μ = A
s
̅̅̅
T
√
/
(
1 +
T
s
T
)
is the dynamic viscosity 
fitted by Sutherland ’ s formula, with A
s
= 1 . 672 × 10
 6
kg /

m ⋅ s ⋅
̅̅̅ ̅
K
√ )
and T
s
= 170 . 672 K.
Energy equation: 
∂ ( ρ E )
∂ t
+ ∇ • [( ρ E + p ) V ] = ∇ • [ τ • V ]  ∇ • q + S
e
, (3) 
where E = e +
| V |
2
2 
is the total energy, and e is the specific internal en -
ergy.
Species transport equation: 
∂ ( ρ Y
m
)
∂ t
+ ∇ • [( ρ Y
m
V )] =  ∇ • s
m
+ ˙ω
m
+ S
Y
, (4) 
where Y
m 
is the mass fraction of the m-th species, s
m 
is the mass flux and 
˙ω
m 
is the net production rate of the m-th species. In Eqs. (1) – (4), S
m
, S
u
, 
S
e
, and S
Y 
denote the exchange of mass, momentum, energy, and spe -
cies, respectively, between the gas phase and the dispersed phase. The 
simulation does not implement subgrid-scale turbulence models, 
adhering to the methodologies of Refs. [ 27 , 29 , 43 , 44 ], as conventional 
turbulence models suitable for low-speed flows may not directly apply to 
the rotating detonation flow field [ 45 ]. The limitations of the lack of a 
suitable turbulence model in the simulation are noted here, and this is an 
open topic that requires further exploration.
The dispersed particles are tracked using a point-particle assump -
tion, which means that particle boundary layers and inter-particle in -
teractions are not resolved. Assuming a dilute regime for the droplets, 
primary atomization and secondary break-up are not considered. The 
Lagrangian system for dispersed particles is described by 
dm
d
dt
= ˙ m
d
, (5) 
dV
d
dt
=
F
d
m
d
, (6) 
J. Li et al.                                                                                                                                                                                                                                         International Journal of Hydrogen Energy 102 (2025) 260–273 
261

<!-- PDF_PAGE: 3 -->

C
p , d
dT
d
dt
=
h
c
A
d
( T
∞
 T
d
) ˙ m
d
˙
Q
L
m
d
, (7) 
where m
d
, V
d
, T
d
, C
p , d 
denote the droplet ’ s mass, velocity, temperature 
and heat capacity, respectively. h
c 
is the convective heat transfer coef -
ficient, and 
˙
Q
L 
is the latent heat. F
d 
is the Stokesian drag force for 
spherical droplets where the drag coefficient is computed according to 
Ref. [ 46 ].
2.2. Two-way coupling and boundary conditions
Two-way exchange between the gas and dispersed phases is achieved 
through the source terms in Eqs. (1) – (4). For the dispersed particles, the 
mass transfer rate of evaporation ˙m
d 
is given by the Abramzon and 
Sirignano model 
46 
˙m
d
= π D
d
Sh D
vap
ρ
f
ln ( 1 + B
m
) , (8) 
where B
m
, D
vap
, ρ
f 
are the Spalding mass transfer number, vapor mass 
diffusivity, and film density, respectively. The Sherwood number Sh =
2 . 0 + 0 . 6Re
1
2
d
S
1
3
c 
is calculated based on Refs. [ 47 , 48 ]. A full description of 
the governing equations can be found in our previous work [ 40 ]; 
therefore, they are only briefly summarized above to keep the paper 
self-contained. The accuracy of the implemented evaporation model was 
validated in previous research [ 29 , 33 , 49 , 50 ] and corroborated by our 
previous study [ 40 ], where evaporation rates were compared with 
experimental measurements and analytical solutions.
Across the inlet surface, each mesh cell is treated as a micro-nozzle 
controlled by the inlet total pressure p
0
. The flow through each micro- 
nozzle is then determined by the relationship between the local pres -
sure p
w 
in each mesh cell and the inlet total pressure: 
(1) p
w
≥ p
0
, no injection occurs.
(2) p
0
> p
w
> p
cr
, the subsonic inlet flow is calculated as follows:
p = p
w
, T = T
0
(
p
p
0
)
γ  1
γ
, v =
̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅ ̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅ ̅̅̅̅ ̅
2 γ
γ  1
R T
0
[
1 
(
p
p
0
)
γ  1
γ
]
√
√
√
√
; (9) 
where T
0 
is the inlet total temperature. 
(3) p
w
≤ p
cr
< p
0
, the sonic inlet flow is calculated as follows:
p = p
cr
, T = T
cr
, v =
̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅ ̅
2 γ
γ + 1
RT
0
√
. (10) 
where R is the gas constant. p
cr 
and T
cr 
are the critical values of pressure 
and temperature, respectively, at which the inlet flow becomes choked: 
p
cr
= p
0
(
2
γ + 1
)
γ
γ  1
, T
cr
= T
0
(
2
γ + 1
)
. (11) 
This injection setup has also been employed in other studies, such as 
Refs. [ 26 , 29 , 30 , 40 , 51 ]. Ethanol droplets are injected from the inlet at 
the same local velocity as the gas phase, with a fixed initial diameter of 
4 μ m and temperature of 300 K. It was noted in Ref. [ 52 ] that in the 
liquid spray-air detonation experiments, the size of the small droplets 
could be on the order of 5 μ m. Besides, the implemented droplet size is 
sufficiently small to satisfy both the requirement of being much smaller 
than the mesh cell for the point-particle assumption and to show mini -
mal difference compared with the results using a droplet break-up model 
[ 50 ]. The simulation is conducted using the finite volume method based 
on the OpenFOAM libraries [ 53 ]. An in-house solver, based on rho -
CentralFoam, is used, which implements the second-order central-up -
wind Kurganov-Tadmor scheme [ 54 ]. The species transport equations 
are coupled to the generic solver to solve the chemical processes. The 
OpenFOAM-based framework has been widely utilized in studies of 
hypersonic engines, as shown in Refs. [ 55 – 58 ], and has been extended to 
detonation process simulations [ 9 , 29 , 50 , 59 , 60 ].
A structured grid is employed for the two-dimensional computa -
tional domain, with a fixed grid size of 0.2 mm in the circumferential 
direction. To meet the resolution requirements for capturing the deto -
nation front structure, a stretched grid is used in the axial direction, with 
a ratio of Δ y
max
= 10 × Δ y
min
. The resulting grid consists of 5.7 × 10
5 
cells. In our previous study [ 40 ], the solutions were compared with 
those obtained using three other coarser and finer meshes — 2 . 8 × 10
5
, 
1 . 1 × 10
6
, and 2 . 3 × 10
6 
cells — and showed good convergence. A 
second-order backward Euler scheme is used for time discretization with 
a maximum CFL (Courant – Friedrichs – Lewy) number of 0.1.
For the chemical reaction model, this paper adopts a two-step 
mechanism for the ethanol-air combustion, 
C
2
H
5
OH + 2O
2
⇒
k
1
2CO + 3H
2
O (12) 
2CO + O
2
⇔
k
2
2CO
2
(13) 
The reaction parameters for the ethanol oxidation and CO – CO
2 
equilibrium are given by Westbrook and Dryer [ 61 ] and Franzelli et al. 
[ 62 ], respectively. We validated this two-step mechanism in our previ -
ous study by comparing the ignition delay times of stoichiometric 
ethanol-air mixtures with experimental data from Nativel et al. [ 63 ] and 
Heufer et al. [ 64 ]. The calculated ignition delay times were found to 
agree well with the experimental measurements.
For additional validation, a numerical experiment of ethanol-air 
detonation in a two-dimensional channel, as illustrated in Fig. 2 , is 
Fig. 1. Computational domain of the rotating detonation flow field.
J. Li et al.                                                                                                                                                                                                                                         International Journal of Hydrogen Energy 102 (2025) 260–273 
262

<!-- PDF_PAGE: 4 -->

conducted to demonstrate the cellular detonation structure of premixed 
ethanol-air vapor mixtures at varying equivalence ratios. The two- 
dimensional detonation tube has a length of 300 mm and a width of 
60 mm. It is initially filled with an ethanol-air mixture at equivalence 
ratios ranging from 0.8 to 1.2. The tube is ignited at the left end by three 
equidistant hot spots. The computation domain is discretized using a 
refined mesh with a cell size of Δ x = 0.1 mm. The results in Fig. 3 show 
small variation in the cellular detonation cell sizes across the different 
cases, with cell sizes approximately ranging from 25 to 30 mm. This is 
close to the 30 – 40 mm scales observed in the experiments reported by 
Diakow et al. [ 65 ]. Overall, the implemented two-step mechanism 
demonstrates satisfactory accuracy as a reduced chemistry for simu -
lating ethanol-air detonations.
3. Results and discussion
3.1. Characteristics of fuel refill zone at varying equivalence ratios
Fig. 4 depicts the flow field of a stably propagating two-phase RDW 
at ϕ = 1.0 and T
0 
= 1200 K. The propagation velocity of the detonation 
wave is approximately 1394 m/s, showing a 22% deficit compared to 
the theoretical Chapman – Jouguet (C-J) value, as discussed in our pre -
vious study [ 40 ]. Specifically, Fig. 4 (a) shows the distributions of 
ethanol vapor and droplets in the flow field, whereas Fig. 4 (b) shows the 
contour of the local equivalence ratios based on ethanol vapor and air. 
The two-phase detonation is achieved by injecting liquid fuel into a 
previously established gaseous detonation flow field to overcome the 
challenge that liquid fuels are difficult to directly ignite and establish 
detonation [ 66 ]. The fuel refill zone in front of the reacting front of the 
RDW, where liquid ethanol droplets and air are injected and distributed, 
generally appears triangular in shape. Along the upstream and down -
stream directions, this zone can be broadly divided into two parts. In the 
near-bottom region, denoted as Region 1, freshly injected droplets move 
downstream in the flow field and begin to evaporate after mixing with 
the hot air. In Fig. 4 (a), colors represent the temperatures of the droplets 
as they travel downstream. The droplet surface delineates the boundary 
between Region 1 and Region 2, where the droplets nearly complete 
their vaporization. Droplet evaporation causes inhomogeneities in 
Region 2, as indicated by the scattered distribution of local equivalence 
ratios. Another interface, referred to as the deflagration surface, sepa -
rates the fuel refill zone from the downstream exhaust products. Here, 
the fuel vapor, under high local temperatures, initiates deflagrative 
combustion. Additionally, a shear layer forms between the newly 
generated detonation products and those from earlier detonations. 
Previous studies [ 26 , 30 ] have noted that, unlike in gaseous RDWs, un -
burned liquid fuel vapor often accumulates along the shear layer.
In Fig. 5 , the fuel refill zones across different equivalence ratios are 
shown. For near-stoichiometric conditions ( ϕ = 0.9 – 1.1), the RDW 
structures generally remain the same, although the accumulation of 
unburned ethanol vapor over the shear layer becomes more prominent. 
As ϕ increases to ϕ ≥ 1 . 2, the excessive injection of droplets into the 
post-detonation zone, which is expected to relieve pressure due to 
expansion and injection recovery, causes fluctuations in local pressures 
near the inlet. This disrupts the triangular shape of the fuel refill zone 
and the shear layer. At ϕ > 1.5, the tail of the shear layer extends to the 
fuel refill zone, leading to significant irregularities in the two-phase 
RDW structure.
Fig. 6 illustrates the temperature distribution of the flow fields at 
identical snapshots. Under various equivalence ratios, unburned regions 
are visible near the shear layer. At higher equivalence ratios, these re -
gions expand due to the presence of significant ethanol vapor, causing 
local quenching of the detonation wave along the shear layer, a phe -
nomenon also reported by Ref. [ 67 ] for the kerosene-air RDW. As the 
detonation wave sweeps through the fuel refill zone, the ethanol vapor is 
not completely ignited or consumed. Instead, the unburned fuel vapor 
lowers the local temperature in the post-detonation region. Despite this, 
a stable two-phase RDW can still be achieved across the investigated 
equivalence range of 0.9 – 1.6. In our previous study [ 40 ], we provided a 
comprehensive analysis of the structure of the two-phase ethanol-air 
RDW, as well as the mechanisms of quenching and re-initiation pro -
cesses. Therefore, these aspects are not the focus of the current study. 
Instead, in the following section, we will use the case with ϕ = 1 as the 
benchmark and focus on the kinematics and spatial statistical aspects of 
the droplets in the flow field.
Fig. 2. Two-dimensional channel filled with ethanol-air mixtures for the simulation of cellular detonation.
Fig. 3. Numerical soot foils (maximum pressure traces) illustrating the cellular structure of the ethanol-air detonation.
J. Li et al.                                                                                                                                                                                                                                         International Journal of Hydrogen Energy 102 (2025) 260–273 
263

<!-- PDF_PAGE: 5 -->

3.2. Temporal and spatial evolution of droplets in detonation front 
proximity and fuel refill region
Each droplet is assigned an original ID when it is first created or 
injected into the domain. We then track and analyze the droplets 
throughout the simulation. The variation of droplet parameters with the 
circumferential position is shown in Fig. 7 . At this moment, the deto -
nation wave is located near the circumferential position of 110 mm, and 
Fig. 4. Structure of a stable two-phase ethanol-air RDW at ϕ = 1.0 and T
0 
= 1200 K. (a) Ethanol vapor and droplet temperature and (b) local equivalence ratio.
Fig. 5. Ethanol vapor distribution in the flow field at different equivalence ratios.
Fig. 6. Gas phase temperature and evaporation rate distributions in the flow field at different equivalence ratios.
J. Li et al.                                                                                                                                                                                                                                         International Journal of Hydrogen Energy 102 (2025) 260–273 
264

<!-- PDF_PAGE: 6 -->

the droplets near the wave front are highlighted in red. It can be seen 
that the y-direction (axial) velocity of droplets U
y , d 
changes notably 
before and after interaction with the detonation wave. Initially, the 
injected droplets have low y-direction velocity in the post-detonation 
region with a high local pressure. As the burned products are exhaus -
ted toward the exit, the droplet ’ s velocity increases, reaching its peak 
just before being overtaken by the detonation wave. On the other hand, 
other droplet properties remain mostly stable along the circumferential 
position before being swept by the detonation wave.
As the diagram reveals, the majority of droplets initially display 
almost no velocity along the x-direction (circumferential) as they are 
injected axially. Upon interacting with the forward-propagating deto -
nation wave, however, they quickly acquire forward momentum and the 
temperature of the droplets T
d 
also rises rapidly. Near the detonation 
wave, the elevated pressure and temperature enhance compression and 
evaporation, thereby increasing the evaporation rate ˙m
d
. Despite this 
increased evaporation, the x-direction velocity remains relatively un -
changed, indicating that the droplets experience limited circumferential 
motion. The droplet diameter D
d 
is fairly uniform across the circum -
ferential positions, although larger droplets tend to be observed near the 
detonation wave. These larger droplets are typically those that have just 
been injected into the combustion chamber, where the high gas tem -
perature causes their expansion. The droplet ’ s age is counted from the 
moment it is introduced into the combustor. The distribution of droplet 
ages resembles the triangular shape of the fuel refill zone, as droplets 
injected earlier travel further downstream and persist longer. A few 
droplets exist near the front of the detonation wave, as they are rapidly 
consumed shortly after being introduced, resulting in a short lifespan. In 
summary, the variation in droplet behavior is primarily driven by their 
proximity to the detonation wave. Significant changes are observed in 
droplets located near the wave front, where rapid momentum gain, 
evaporation, and temperature changes occur.
The distance between the position of the droplet and the intake wall 
is defined as the droplet ’ s longitudinal distance y
d
, which is analogous to 
Fig. 7. Variations of droplet parameters with circumferential position in the flow field (color in red represents droplets near the detonation wave front). (For 
interpretation of the references to color in this figure legend, the reader is referred to the Web version of this article.)
Fig. 8. Variations of droplet velocities (axial and circumferential) and age with longitudinal distance.
J. Li et al.                                                                                                                                                                                                                                         International Journal of Hydrogen Energy 102 (2025) 260–273 
265

<!-- PDF_PAGE: 7 -->

the penetration depth of the droplets and has been found to be important 
for the stability of the two-phase RDW [ 27 ]. Fig. 8 shows the variation of 
droplet parameters with the longitudinal distance. Generally, the num -
ber of droplets decreases from upstream to downstream, meaning that 
most droplets evaporate into vapor during their downstream movement. 
Under the current condition, the furthest distance droplets can move 
from the intake wall is approximately 14 . 6 mm.
The longitudinal velocity U
y , d 
refers to the velocity component cor -
responding to the longitudinal movement of droplets in the flow field. 
Under the current condition, the maximum longitudinal velocity of 
droplets is about 480 m/s. At different longitudinal distances, the min -
imum longitudinal velocity that droplets can achieve varies. In the up -
stream part of the flow field, where newly injected droplets accumulate 
with an initial velocity equal to the gas phase velocity, the longitudinal 
velocity of the droplets ranges from zero to a maximum value of around 
480 m/s. In the downstream part of the flow field, the minimum lon -
gitudinal velocity of droplets is higher and shows an increasing trend. 
The droplets that can travel and remain in regions more than 10 mm 
away in longitudinal distance have a minimum velocity of approxi -
mately 300 m/s.
The transversal velocity U
x , d 
represents the velocity component of 
the droplet that is aligned with the movement direction of the detona -
tion wave. As shown in Fig. 8 , in contrast to the longitudinal velocity 
U
x , d
, which spans a wide range throughout the flow field, only a small 
number of droplets exhibit significant positive transverse velocities. 
These droplets are located near the detonation wave, gaining their speed 
from its forward motion. The majority of droplets maintain a relatively 
constant transverse speed at different longitudinal distances. Some 
droplets indicate a transverse velocity in the opposite direction to the 
detonation wave, which is caused by the post-detonation expansion ef -
fect. Regarding the residence time of the droplets, they primarily 
accumulate predominantly below y
d 
= 7 mm, with some droplets 
remaining unevaporated and migrating to regions beyond this 
threshold. A small number of droplets continue to move beyond y
d 
= 14 
mm in the fuel refill zone. Closer to approximately y
d 
= 3 mm, accu -
mulated droplets show longer lifetimes. According to the statistical 
frequency diagram in Fig. 9 , the majority of droplets exhibit lifespans 
shorter than 40 μ s.
The droplet density ρ
d
, illustrated in Fig. 10 demonstrates a distri -
bution pattern that is opposite to that of the droplet temperature as the 
droplets move downstream. The heating of droplets as they move 
downstream results in a right-angled triangular pattern in the distribu -
tion of droplet temperatures T
d
, as Fig. 10 shows. Conversely, the 
droplet density tends to decrease due to substantial mass transfer due to 
evaporation, following a left-angled triangular distribution. Most drop -
lets evaporate before reaching the droplet temperature of 450 K, which 
is near the critical temperature of ethanol droplets under the given 
conditions. Fig. 11 indicates that approximately 6% of the droplets 
exhibit temperatures between 420 and 425 K, over 50% fall within the 
425 – 440 K range, and about 1.5% of droplets exceed 450 K. Regarding 
the distribution of droplet diameters D
d
, Fig. 10 shows that for droplets 
at y
d 
> 7 mm, few have diameters larger than their initial size, indicating 
that these droplets have passed through the thermal expansion phase. 
Droplets near their initial size of 4 μ m tend to gather below y
d 
= 7 mm, 
suggesting that they have just entered the flow field, where the heating 
process is still in its early stages. As suggested in the statistical frequency 
diagram ( Fig. 11 ), more than 44% of the droplets are heated slowly by 
the ambient gas and experience thermal expansion.
Fig. 12 illustrates how the specific heat capacity C
p , d 
varies with 
longitudinal distance, and the corresponding statistical frequency dia -
gram is presented in Fig. 13 . When the droplets are heated downstream, 
their specific heat capacities increase, and thus, the specific heat ca -
pacity exhibits a similar trend to the droplet temperature along the 
longitudinal distance. In contrast, both the droplet surface tension σ
d 
and viscosity μ
d 
diminish. As noted by Tolman et al. [ 68 ], the surface 
tension of droplets tended to decrease as their size diminishes, with this 
effect becoming more pronounced for very small droplets. Conse -
quently, the surface tension of downstream droplets is reduced due to 
both their elevated temperature and smaller sized. Also, the droplet 
viscosity is found to be temperature-dependent and generally decreases 
with increasing temperature, as confirmed by Ref. [ 69 ].
3.3. Temporal and spatial evolution of droplets in post-detonation region
Droplets in the flow field can be generally categorized into three 
groups based on their positions. The first group, consisting of droplets 
located ahead of the detonation wave — referred to as the leading-edge 
droplets — is mainly discussed in the previous section. These droplets 
are marked in red in Fig. 14 , a snapshot ( T = 1250 μ s) of the stabilized 
flow field. Considering the angle between the detonation front and the 
intake wall, a perpendicular line can be drawn from the contact point 
between the detonation wave and the most downstream droplet in the 
combustion chamber, extending to the front edge of the detonation 
wave. Droplets within this region are classified as leading-edge droplets 
and are on the verge of experiencing significant changes once the 
detonation wave passes. The second group consists of droplets situated 
immediately behind the high-pressure blockage zone, referred to as the 
trailing-edge droplets and are colored in green in Fig. 14 . All remaining 
droplets fall under the third category. These droplets dominate the fuel 
refill zone and are indicated in black. The distinction between these two 
sets is determined from the deflection point indicated by the arrow. The 
evaporation processes of these three types of droplets will be analyzed in 
greater detail in the following discussion.
The evaporation of the leading-edge droplets with time is visualized 
in Fig. 15 , including the temperature, diameter, and evaporation rate of 
these droplets evolve over time. When directly swept by the detonation 
wave, the evaporation process occurs over a very short period. Initially, 
before the arrival of the detonation wave, the droplets evaporate 
steadily in the high-temperature and high-pressure flow field, with their 
properties changing gradually. Once the detonation wave reaches the 
droplets, a sharp rise in temperature and pressure occurs. The droplets 
absorb significant heat, resulting in a rapid temperature increase. 
Fig. 9. Statistical histograms illustrating the distributions of droplet velocities (axial and circumferential) and age.
J. Li et al.                                                                                                                                                                                                                                         International Journal of Hydrogen Energy 102 (2025) 260–273 
266

<!-- PDF_PAGE: 8 -->

Fig. 10. Variations of droplet density, temperature and size (diameter) with longitudinal distance.
Fig. 11. Statistical histograms illustrating the distributions of droplet density, temperature and size (diameter).
Fig. 12. Variations of droplet specific heat capacity, viscosity, and surface tension with longitudinal distance.
J. Li et al.                                                                                                                                                                                                                                         International Journal of Hydrogen Energy 102 (2025) 260–273 
267

<!-- PDF_PAGE: 9 -->

Consequently, the droplets expand, leading to a surge in diameter and an 
acceleration of their evaporation rate. Most droplets are fully evapo -
rated after the detonation wave passes, while a few remain — represen -
ted by dashed lines and hollow symbols in Fig. 15 . Despite a decrease in 
their evaporation rate over time, the remaining droplets continue to 
evaporate in the high-temperature post-detonation environment, even -
tually leading to their complete evaporation.
The evaporation process of the trailing-edge droplets in the post- 
detonation zone, along with the remaining droplets, is primarily unaf -
fected by the detonation wave itself. In order to quantitatively assess this 
process, we introduce the Sauter Mean Diameter (SMD), the average 
evaporation rate ˙m
d
, and the average temperature T
d 
are of the groups of 
the trailing-edge droplets and remaining droplets are analyzed in groups 
with time. The SMD is calculated at each time step using the following 
formula: 
SMD =
∑
n
i
× D
3
d , i
∑
n
i
× D
2
d , i
(14) 
where n
i 
is the quantity of droplets with diameter D
d , i
. The trailing-edge 
droplets evaporate completely within 49.1 μ s (see Fig. 16 (a)). Initially, 
before 1.255 ms, these droplets absorb heat from the surrounding high- 
temperature environment, leading to a steady increase in their tem -
perature until it stabilizes at 430 K. The evaporation rate reaches its peak 
at approximately 1 . 2e
 9
kg / s, resulting in a corresponding decrease in 
droplet diameter. From 1.255 ms to 1.286 ms, as the droplets move 
downstream, they experience a slight temperature increase. However, 
the evaporation rate begins to decline during this period. Despite the 
continuous decreasing of the droplet sizes, their temperatures eventually 
rise to about 435 K before it starts to decrease slightly again. This 
reduction occurs due to the loss of mass from the evaporating droplets 
and the latent heat required for evaporation. The average droplet tem -
perature decreases to approximately 420 K at 1.286 ms and then rises 
again as the cooler droplets continue to absorb heat from the higher 
temperature surrounding gas. This process continues until all the 
trailing-edge droplets in this group eventually evaporate.
The remaining droplets take around 25.6 μ s to fully evaporate 
( Fig. 16 (b)). After being in the flow field for some time after injection, 
their average temperature reaches 410 K, their diameter decreases to 
3.7 μ m, and their evaporation rate is 1e
 9 
kg/s. During the evaporation 
process, the droplets travel downstream, with their average diameter 
continuously decreasing, indicating ongoing evaporation. Before 1.258 
ms, the temperature of the downstream droplets rises steadily to 435 K, 
and the evaporation rate increases to 1 . 6e
 9 
kg/s. Beyond this point, the 
droplet temperature declines for the same reasons outlined above, which 
leads to a reduction in the evaporation rate until the droplets completely 
evaporate.
Fig. 13. Statistical histograms illustrating the distributions of droplet specific heat capacity, viscosity, and surface tension.
Fig. 14. Droplet distribution at a stable time snapshot ( T = 1250 μ s). 
Benchmark case at ϕ = 1.0 and T
0 
= 1200 K. Axes are not scaled equally.
Fig. 15. Evaporation process of leading-edge droplets. Hollow shapes and dashed lines indicate droplets that did not fully evaporate after being impacted by the 
detonation wave.
J. Li et al.                                                                                                                                                                                                                                         International Journal of Hydrogen Energy 102 (2025) 260–273 
268

<!-- PDF_PAGE: 10 -->

3.4. Effects of equivalence ratios on droplets kinematics and distribution
Fig. 17 illustrates that the temperature, evaporation rate, and size 
distributions of the droplets across different equivalence ratios. Mean -
while, Fig. 18 computes the centroids of the scatter plots in Fig. 17 using 
the Euclidean norm. As the equivalence ratio increases, more droplets 
are observed moving downstream in the flow field. Specifically, for 
equivalence ratios of ϕ = 0.9 to 1.2, the maximum longitudinal distance 
droplets can travel is approximately 11 mm. At ϕ = 1.3 to 1.4, droplets 
can reach up to 15 mm, while at ϕ = 1.5 to 1.6, the movement distance 
extends to 20 mm. Besides, for ϕ = 0.9 to 1.4, the droplets with high 
temperatures of 420 – 450 K tend to accumulate between 4 mm and 11 
mm. As ϕ increases to 1.5 to 1.6, local quenching disrupts the fuel refill 
zone significantly, as shown in Fig. 17 . Particularly at ϕ = 1.6, the dis -
tribution pattern of high-temperature droplets shifts towards down -
stream with only a few droplets reaching a temperature of 450 K, and the 
mean temperature of the droplet cluster also decreases, as can be seen in 
Fig. 18 . In terms of the evaporation rate, upstream droplets evaporate 
more rapidly with increasing height, whereas downstream droplets 
experience a slower evaporation rate at higher longitudinal distances. 
This phenomenon occurs because downstream droplets, having been in 
the flow field longer, exhibit smaller diameters and reduced surface 
areas. Additionally, the heated droplets display smaller temperature and 
velocity differences compared to the surrounding gas, all of which 
contribute to decreased evaporation rates of the downstream droplets. 
At ϕ = 0.9 – 1.1, Fig. 18 shows that the mean evaporation rates of droplet 
clusters tend to decrease as the equivalence ratio increases. This decline 
becomes less pronounced when ϕ is between 1.2 and 1.4. However, a 
further decrease is observed at ϕ = 1.5, followed by a significant in -
crease at ϕ = 1.6. Similarly, the mean sizes of the droplet clusters show a 
steady decrease with the equivalence ratio from ϕ = 1.1 to 1.4. There are 
minor fluctuations observed at ϕ = 0.9 and 1.0, while larger fluctuations 
occur at ϕ = 1.5 and 1.6.
The significant variations in droplet evaporation near the fuel-rich 
condition of ϕ ≈ 1.6 is explained. Fig. 19 shows the evolution of the 
two-phase RDW over time, which can be sustained but is highly unsta -
ble. Under the fuel-rich condition, the accumulation of an excessive 
number of droplets near the detonation front causes the upstream 
portion of the front to lag, as observed in the zoom-in window at 1285 μ 
s. As the bow-shaped detonation front develops, it will collide with the 
inlet wall, leading to localized high pressures and explosions that rapidly 
consume the nearby newly injected droplets and hinder further droplet 
injection.
4. Conclusion
This numerical study provides a comprehensive analysis of ethanol 
droplet behavior in a two-phase RDW, offering some insight into the 
distinct dynamics of droplets based on their spatial position and inter -
action with the detonation wave. The main findings are as follows. 
(1) The proximity to the detonation wave and the longitudinal po -
sition are key factors influencing droplet kinematics and spatial 
distribution. Droplets close to the detonation wave undergo rapid 
evaporation and experience temperature spikes, while those 
further downstream encounter gradual temperature increases 
and slower evaporation rates. As the droplets move downstream 
after injection, corresponding parameters ( U
y , d
, U
x , d
, T
d
, ρ
d
, D
d
, 
C
p , d
, μ
d
, σ
d
) vary differently. Notably, droplet temperature and 
size play crucial roles in this variation.
(2) The liquid droplets are classified into three main categories: the 
leading-edge droplets near the detonation front, the trailing-edge 
droplets in the post-detonation region that are immediately 
injected, and the remaining fuel droplets that occupy the majority 
of the fuel refill zone. Most leading-edge droplets evaporate 
rapidly as the detonation wave passes. In contrast, the evapora -
tion of trailing-edge droplets and the remaining droplets in the 
post-detonation zone is largely unaffected by the detonation 
wave. After injection, these droplets exhibit a steady temperature 
rise, an increase in longitudinal velocity, and minimal changes in 
transversal velocity.
(3) As the equivalence ratio increases, a greater number of droplets 
are observed moving downstream, leading to different distribu -
tion patterns of the clusters of droplets and variations in their 
longitudinal distance, mean evaporation rate, mean droplet 
temperature, and mean droplet size. Significant changes in 
droplet distribution and behavior near the fuel-rich condition ( ϕ 
= 1.6) result from the accumulation of excessive droplets near the 
detonation front, which will disturb the local pressure 
Fig. 16. Evaporation process of (a) trailing-edge droplets and (b) remaining droplets. Average properties of the grouped droplets over time are presented.
J. Li et al.                                                                                                                                                                                                                                         International Journal of Hydrogen Energy 102 (2025) 260–273 
269

<!-- PDF_PAGE: 11 -->

Fig. 17. Temperature, evaporation rate and size distributions of droplets at different equivalence ratios.
J. Li et al.                                                                                                                                                                                                                                         International Journal of Hydrogen Energy 102 (2025) 260–273 
270

<!-- PDF_PAGE: 12 -->

distribution over the injection surface, induce shock waves, and 
promote localized explosions.
CRediT authorship contribution statement
Jianghong Li: Writing – review & editing, Writing – original draft, 
Investigation, Formal analysis, Data curation, Conceptualization. 
Songbai Yao: Writing – review & editing, Writing – original draft, Su -
pervision, Project administration, Methodology, Funding acquisition, 
Conceptualization. Ying Lei: Writing – review & editing, Software, Data 
curation. Jingtian Yu: Writing – review & editing, Software, Data 
curation. Wenwu Zhang: Supervision, Project administration, Funding 
acquisition.
Declaration of competing interest
The authors declare that they have no known competing financial 
interests or personal relationships that could have appeared to influence 
the work reported in this paper.
Acknowledgment
This work was supported by the National Natural Science Foundation 
of China (No. 52306175), the Ningbo Natural Science Foundation (No. 
2023J413), and the Ningbo Yongjiang Talent Introduction Programme 
(No. 2022A-210-G).
Fig. 18. Centroids of the temperature distribution of droplets at different equivalence ratios.
Fig. 19. Evolution of the two-phase RDW at the fuel-rich condition of ϕ = 1.6.
J. Li et al.                                                                                                                                                                                                                                         International Journal of Hydrogen Energy 102 (2025) 260–273 
271

<!-- PDF_PAGE: 13 -->

References
[1] Ma JZ, Luan MY, Xia ZJ, Wang JP, Zhang SJ, Yao SB, et al. Recent progress, 
development trends, and consideration of continuous detonation engines. AIAA J 
2020;58:4976 – 5035 .
[2] Wola ´nski P. Detonative propulsion. Proc Combust Inst 2013;34:125 – 58 .
[3] Bennewitz JW, Burr JR, Bigler BR, Burke RF, Lemcherfi A, Mundt T, et al. 
Experimental validation of rotating detonation for rocket propulsion. Sci Rep 2023; 
13:14204 .
[4] Zhou S, Ma Y, Liu F, Hu N. Experimental investigation on pulse operation 
characteristics of rotating detonation rocket engine. Fuel 2023;354:129408 .
[5] Yu J, Yao S, Li J, Li J, Lei Y, Wang R, et al. Experimental investigation of the 
hydrogen-air rotating detonation engine with cat-ear-shaped film cooling holes. Int 
J Hydrogen Energy 2024;89:1454 – 65 .
[6] Bai Q, Han J, Qiu H, Zhang S, Weng C. Study on initiation characteristics of 
rotating detonation by auto-initiation and pre-detonation method with high- 
temperature hydrogen gas. Int J Hydrogen Energy 2024;49:450 – 61 .
[7] Fan W, Peng H, Liu S, Sun M, Yuan X, Zhang H, et al. Initiation process of non- 
premixed continuous rotating detonation wave through schlieren visualization. 
Combust Flame 2024;265:113437 .
[8] Dille KJ, Frederick MD, Slabaugh CD, Heister SD. Rotating detonation combustor 
performance informed through a novel megahertz-rate stagnation pressure 
measurement. Phys Fluids 2024;36:026127 .
[9] Fan LZ, Shi Q, Zhi Y, Nie WS, Lin W. Experimental and numerical study on multi- 
wavemodes of H
2
/O
2 
rotating detonation combustor. Int J Hydrogen Energy 2022; 
47:13121 – 33 .
[10] Harroun A, Heister SD. Liquid fuel survey for rotating detonation rocket engines. 
In: AIAA SCITECH 2022 Forum; 2022 .
[11] Bykovskii FA, Zhdan SA, Vedernikov EF. Continuous spin detonations. J Propul 
Power 2006;22:1204 – 16 .
[12] Kindracki J. Experimental research on rotating detonation in liquid fuel-gaseous air 
mixtures. Aero Sci Technol 2015;43:445 – 53 .
[13] Bykovskii FA, Zhdan SA, Vedernikov EF. Continuous detonation of the liquid 
kerosene-air mixture with addition of hydrogen or syngas. Combust Explos Shock 
Waves 2019;55:589 – 98 .
[14] Kindracki J, Wacko K, Wo ´zniak P, Siatkowski S, M ę ˙zyk Ł . Influence of gaseous 
hydrogen addition on initiation of rotating detonation in liquid fuel – air mixtures. 
Energies 2020;13:5101 .
[15] Ishihara K, Sato T, Kimura T, Nakajima K, Nakata K, Itouyama N, et al. Nitrous 
oxide/ethanol cylindrical rotating detonation engine for sounding rocket space 
flight. J Spacecraft Rockets 2024. https://doi.org/10.2514/1.A35824 .
[16] Han X, Huang Y, Zheng Q, Xiao Q, Xu H, Wang F, et al. Study of the characteristics 
and combustion efficiency of liquid kerosene/oxygen-enriched air rotating 
detonation wave with different modes. Fuel 2024;355:129424 .
[17] Zhao MH, Wang K, Zhu YY, Wang ZC, Yan Y, Wang YJ, et al. Effects of the exit 
convergent ratio on the propagation behavior of rotating detonations utilizing 
liquid kerosene. Acta Astronaut 2022;193:35 – 43 .
[18] Perkowski W, Bilar A, Augustyn M, Kawalec M. Air-breathing rotating detonation 
engine supplied with liquid kerosene: propulsive performance and combustion 
stability. Shock Waves 2024;34:181 – 92 .
[19] Zhou J, Song F, Wu Y, Xu S, Yang X, Cheng P, et al. Investigation of pressure gain 
characteristics for kerosene-hot air RDE. Combust Flame 2023;247:126102 .
[20] He X-J, Gong X-P, Wang J-P, Ma JZ. Investigation of the total pressure gain in 
rotating detonation combustors with dilution holes. Phys Fluids 2024;36:045103 .
[21] Li X, Li J, Qin Q, Jin W, Yuan L. Experimental study on detonation characteristics 
of liquid kerosene/air rotating detonation engine. Acta Astronaut 2024;215: 
124 – 34 .
[22] Huang SY, Zhou J, Liu SJ, Peng HY, Yuan XQ. Continuous rotating detonation 
engine fueled by ammonia. Energy 2022;252:123911 .
[23] Raman V, Prakash S, Gamba M. Nonidealities in rotating detonation engines. Annu 
Rev Fluid Mech 2023;55:639 – 74 .
[24] Pal P, Kumar G, Drennan SA, Rankin BA, Som S. Multidimensional numerical 
modeling of combustion dynamics in a non-premixed rotating detonation engine 
with adaptive mesh refinement. J Energy Resour Technol 2021;143:112308 .
[25] Salvadori M, Panchal A, Menon S. Simulation of liquid droplets combustion in a 
rotating detonation engine. Proceedings of the combustion institute. 2022. 
p. 3063 – 72 .
[26] Yao S, Guo C, Zhang W. Effects of droplet evaporation on the flow field of 
hydrogen-enhanced rotating detonation engines with liquid kerosene. Int J 
Hydrogen Energy 2023;48:33335 – 45 .
[27] Prakash S, Bielawski R, Raman V, Ahmed K, Bennewitz J. Three-dimensional 
numerical simulations of a liquid RP-2/O2 based rotating detonation engine. 
Combust Flame 2024;259:113097 .
[28] Malik V, Salauddin S, Hytovick R, Bielawski R, Raman V, Bennewitz J, et al. 
Detonation wave driven by aerosolized liquid RP-2 spray. Proc Combust Inst 2023; 
39:2807 – 15 .
[29] Meng Q, Zhao M, Zheng H, Zhang H. Eulerian-Lagrangian modelling of rotating 
detonative combustion in partially pre-vaporized n-heptane sprays with hydrogen 
addition. Fuel 2021;290:119808 .
[30] Li J, Lei Y, Yao S, Yu J, Li J, Zhang W. Investigation of multi-stage evaporation and 
wave multiplicity of two-phase rotating detonation waves fueled by ethanol. Acta 
Astronaut 2023;213:418 – 30 .
[31] Salvadori M, Panchal A, Menon S. Numerical study of spray combustion effects on 
detonation propagation. AIAA J 2023;61:5347 – 64 .
[32] Gao S, Peng H, Huang Y, Sun Z, You Y. Numerical simulations and theoretical 
analysis of the forward shock wave in a non-premixed air-breathing rotating 
detonation combustor. Phys Fluids 2024;36:066101 .
[33] Wang J, Lin W, Huang W, Shi Q, Zhao J. Numerical study on atomization and 
evaporation characteristics of preheated kerosene jet in a rotating detonation 
scramjet combustor. Appl Therm Eng 2022;203:117920 .
[34] Wen H, Wei W, Fan W, Xie Q, Wang B. On the propagation stability of droplet- 
laden two-phase rotating detonation waves. Combust Flame 2022;244:112271 .
[35] Suzuki L, Nakayama S, Sakai K. ZERO by interstellar technologies inc.: lowering 
the cost of access to space from Japan. In: Small satellite conference; 2024 .
[36] Sakaki K, Kakudo H, Nakaya S, Tsue M, Kanai R, Suzuki K, et al. Performance 
evaluation of rocket engine combustors using ethanol/liquid oxygen pintle 
injector. In: 52nd AIAA/SAE/ASEE joint propulsion conference; 2016 .
[37] Nakaya S, Hikichi Y, Nakazawa Y, Sakaki K, Choi M, Tsue M, et al. Ignition and 
supersonic combustion behavior of liquid ethanol in a scramjet model combustor 
with cavity flame holder. Proc Combust Inst 2015;35:2091 – 9 .
[38] Yoneyama K, Ishihara K, Ito S, Watanabe H, Itouyama N, Kawasaki A, et al. 
Experimental clarification on detonation phenomena of liquid ethanol rotating 
detonation combustor. In: AIAA SCITECH 2022 forum; 2022 .
[39] Sato T, Ishihara K, Yoneyama K, Ito S, Itouyama N, Watanabe H, et al. 
Experimental research on thrust performance of rotating detonation engine with 
liquid ethanol and gaseous oxygen. In: AIAA AVIATION 2022 forum; 2022 .
[40] Li J, Yao S, Yu J, Li J, Lei Y, Zhang W. Shock interactions and re-initiation 
mechanism of liquid ethanol-fueled rotating detonation wave. Phys Fluids 2024; 
36:096106 .
[41] Yao S, Tang X, Zhang W. Structure of a heterogeneous two-phase rotating 
detonation wave with ethanol – hydrogen – air mixture. Phys Fluids 2023;35: 
031712 .
[42] Bykovskii FA, Zhdan SA, Vedernikov EF. Continuous multifront detonation of 
kerosene-air mixture in an annular combustor with variations of its geometry. 
Shock Waves 2021;31:829 – 39 .
[43] Sun J, Yang P, Chen Z. Dynamic interaction patterns of oblique detonation waves 
with boundary layers in hypersonic reactive flows. Combust Flame 2025;271: 
113832 .
[44] Tian C, Teng H, Shi B, Yang P, Wang K, Zhao M. Propagation instabilities of the 
oblique detonation wave in partially prevaporized n-heptane sprays. J Fluid Mech 
2024;984:A16 .
[45] Prakash S. Computational modeling of non-idealities in gaseous and multiphase 
detonating flows [ph.D. Thesis]. University of Michigan; 2022 .
[46] Kuo KK, Acharya R. Fundamentals of turbulent and multiphase combustion. John 
Wiley & Sons; 2012 .
[47] Ranz WE, Marshall WR. Evaporation from drops: Part 1. Chem Eng Prog 1952;48: 
141 – 6 .
[48] Ranz WE, Marshall WR. Evaporation from drops: Part 2. Chem Eng Prog 1952;48: 
173 – 80 .
[49] Chen H, Li R, Wu Y, Hu H, Zhu Y. Numerical study on rotating detonation 
combustion with the discrete distribution of partially pre-vaporized n-heptane 
sprays. Fuel 2024;356:129650 .
[50] Zhao M, Zhang H. Modelling rotating detonative combustion fueled by partially 
pre-vaporized n-heptane sprays. arXiv preprint arXiv:200908617 2020 .
[51] Hu J, Zhang B. Time/frequency domain analysis of detonation wave propagation 
mechanism in a linear rotating detonation combustor. Appl Therm Eng 2024;255: 
124014 .
[52] Papavassiliou J, Makris A, Knystautas R, Lee JHS, Westbrook CK, Pitz WJ. 
Measurements of cellular structure in spray detonation. Dynamic Aspects of 
Explosion Phenomena; 1993. p. 148 – 69 .
[53] Weller HG, Tabor G, Jasak H, Fureby C. A tensorial approach to computational 
continuum mechanics using object-oriented techniques. Comput Phys 1998;12: 
620 – 31 .
[54] Kurganov A, Tadmor E. New high-resolution central schemes for nonlinear 
conservation laws and convection – diffusion equations. J Comput Phys 2000;160: 
241 – 82 .
[55] Chapuis M, Fedina E, Fureby C, Hannemann K, Karl S, Martinez Schramm J. 
A computational study of the HyShot II combustor performance, vol. 34. 
Proceedings of the Combustion Institute; 2013. p. 2101 – 9 .
[56] Fureby C, Nordin-Bates K, Petterson K, Bresson A, Sabelnikov V. A computational 
study of supersonic combustion in strut injector and hypermixer flow fields. Proc 
Combust Inst 2015;35:2127 – 35 .
[57] Yao W, Wang J, Lu Y, Li X, Fan X. Full-scale Detached Eddy Simulation of kerosene 
fueled scramjet combustor based on skeletal mechanism. In: 20th AIAA 
international space planes and hypersonic systems and technologies conference; 
2015 .
[58] Zhou D, Zou S, Yang S. An OpenFOAM-based fully compressible reacting flow 
solver with detailed transport and chemistry for high-speed combustion 
simulations. AIAA Scitech 2020 Forum; 2020 .
[59] Sun J, Wang Y, Tian B, Chen Z. detonationFoam: an open-source solver for 
simulation of gaseous detonation based on OpenFOAM. Comput Phys Commun 
2023;292:108859 .
[60] Chen H, Si C, Wu Y, Hu H, Zhu Y. Numerical investigation of the effect of 
equivalence ratio on the propagation characteristics and performance of rotating 
detonation engine. Int J Hydrogen Energy 2023;48:24074 – 88 .
[61] Westbrook CK, Dryer FL. Simplified reaction mechanisms for the oxidation of 
hydrocarbon fuels in flames. Combust Sci Technol 1981;27:31 – 43 .
[62] Franzelli B, Riber E, Sanjos ´e M, Poinsot T. A two-step chemical scheme for 
kerosene-air premixed flames. Combust Flame 2010;157:1364 – 73 .
J. Li et al.                                                                                                                                                                                                                                         International Journal of Hydrogen Energy 102 (2025) 260–273 
272

<!-- PDF_PAGE: 14 -->

[63] Nativel D, Niegemann P, Herzler J, Fikri M, Schulz C. Ethanol ignition in a high- 
pressure shock tube: ignition delay time and high-repetition-rate imaging 
measurements. Proc Combust Inst 2021;38:901–9 .
[64] Heufer KA, Olivier H. Determination of ignition delay times of different 
hydrocarbons in a new high pressure shock tube. Shock Waves 2010;20:307–16 .
[65] Diakow P, Cross M, Ciccarelli G. Detonation characteristics of dimethyl ether and 
ethanol–air mixtures. Shock Waves 2015;25:231–8 .
[66] Kailasanath K. Liquid-fueled detonations in tubes. J Propul Power 2006;22:1261–8 .
[67] Ren Z, Zheng L. Numerical study on rotating detonation stability in two-phase 
kerosene-air mixture. Combust Flame 2021;231:111484 .
[68] Tolman RC. The effect of droplet size on surface tension. J Chem Phys 1949;17: 
333–7 .
[69] Khare P. Dynamics of a liquid droplet. Am Chem Soc; 2024 .
J. Li et al.                                                                                                                                                                                                                                         International Journal of Hydrogen Energy 102 (2025) 260–273 
273
