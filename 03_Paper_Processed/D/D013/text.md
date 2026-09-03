<!-- PDF_PAGE: 1 -->

Acta Astronautica 223 (2024) 108–118
Available online 5 July 2024
0094-5765/© 2024 IAA. Published by Elsevier Ltd. All rights are reserved, including those for text and data mining, AI training, and similar technologies.
Effects of the droplet size and engine size on two-phase kerosene/air 
rotating detonation engines in flight operation conditions 
Wenbo Cao , Qiuyue Liu , Fang Wang
*
, Chunsheng Weng 
National Key Laboratory of Transient Physics, Nanjing University of Science and Technology, 210094, Nanjing, People ’ s Republic of China   
ARTICLE INFO  
Keywords: 
Rotating detonation 
Engine size 
Flight operation condition 
ABSTRACT  
The numerical and experimental research of rotating detonation engines is usually conducted in ground envi -
ronmental conditions. Although many breakthroughs have been made, there are still deficiencies in under -
standing engines operating in real flight conditions. In order to reveal the effect of engine size and initial 
kerosene droplet size on the rotating detonation engines in flight conditions, the Eulerian-Lagrangian model is 
adopted, and a series of two-phase kerosene/air rotating detonation cases are simulated in the conditions of 
Mach 5 and 24 km altitude. When 5 μ m and 10 μ m droplets are adopted, the RDE behaves like gaseous rotating 
detonations with clear cellular structures. When the 20 μ m and 30 μ m droplets are adopted, the rotating deto -
nation waves tend to be divided into two layers and form the λ -shaped shock structure. The results indicate that 
droplet size and engine size influence detonation wave propagation and flow field mainly through droplet heat 
absorption and evaporation height. Increasing the engine sizes can promote the two-phase rotating detonation 
and broaden the initial diameter range capable of obtaining rotating detonation waves. However, as droplet size 
increases, the fresh mixture layer becomes stratified, with an upper layer predominantly comprising fuel vapor 
and a lower layer of fuel droplets, which results in an λ -shaped shock structure at the detonation front. The flight 
operation condition brings in differences in features such as detonation wave height and velocity deficit. The 
detonation height in flight conditions is higher than that in ground conditions. The most velocity deficit in flight 
conditions observed in our study is below 15 %, which is lower than the results (22.5 %) in ground operating 
conditions. These results indicate that the optimal design of the rotating detonation engine must consider the real 
operation conditions and the effect of engine sizes and droplet sizes.   
1. Introduction 
Rotating detonation engine (RDE) is an innovative engine that 
operates on detonation combustion [ 1 – 4 ]. Compared to 
deflagration-based devices, engines utilizing detonation have higher 
thermal efficiency, greater specific impulse, and a more compact 
structure. The RDE configuration typically consists of an annular with 
one end open and the other equipped with a pneumatic injection system. 
In this setup, fuel and oxidizer are injected axially through the pneu -
matic injection end, while combustion products are predominantly 
discharged in the axial direction from the open end. RDE exhibits 
extensive potential for various applications aimed at overcoming ther -
mal efficiency limitations, such as rocket engines [ 5 – 7 ], turbine engines 
[ 8 , 9 ], and ramjet engines [ 10 – 12 ]. 
In recent years, a large amount of research has been conducted on the 
working characteristics and performance of rotating detonation engines. 
Detonation engines can choose different types of fuel according to the 
need, such as gas [ 13 – 17 ], liquid [ 18 – 22 ], and solid [ 23 – 25 ] fuel. Meng 
et al. [ 19 ] studied the propagation modes of rotating detonation waves 
supplied with liquid kerosene and oxygen-enriched air. Ding et al. [ 21 ] 
established an experimental model of a liquid kerosene-fueled rotating 
detonation combustor. The propagation modes of detonation waves 
were investigated, and the effects of the oxygen mass fraction and the 
equivalence ratio were analyzed. Zhao et al. [ 22 ] analyzed the effects of 
the exit convergent ratio on the propagation behavior of rotating deto -
nations utilizing liquid kerosene. Peng et al. [ 26 ] conducted a series of 
experiments on hydrogen/air, ethylene/air, and methane/air. They 
found that the equivalence ratio is an essential factor affecting the sta -
bility of detonation wave propagation. Ma et al. [ 27 ] studied the igni -
tion, quenching, reinitiation, and stable propagation process of a 
rotating detonation engine by the hydrogen/air propellant combination. 
It was found that the stable process of rotating detonation wave can be 
* Corresponding author. 
E-mail address: wfnjust@126.com (F. Wang).  
Contents lists available at ScienceDirect 
Acta Astronautica 
journal homepag e: www.else vier.com/loc ate/actaastro 
https://doi.org/10.1016/j.actaastro.2024.07.002 
Received 27 May 2024; Received in revised form 26 June 2024; Accepted 1 July 2024

<!-- PDF_PAGE: 2 -->

Acta Astronautica 223 (2024) 108–118
109
divided into deflagration, deflagration to detonation transition (DDT), 
and coexistence of detonation and deflagration. The phenomenon of 
single-double-single wave transition was found and analyzed for the first 
time in the experiment. 
The experiment provides a basis for the study of rotating detonation 
engines. To better understand the complex variations of two-phase 
rotating detonation waves in the flow field, many researchers have 
conducted numerical simulation studies. Zhang et al. [ 28 ] developed a 
two-phase detonation solver called RYrhoCentralFoam for multi-phase, 
multi-component, compressible, and reacting flows. Yao et al. [ 29 ] 
explored the adaptive mode switching process of rotating detonation 
waves in response to the change in inlet conditions. Meng et al. [ 30 ] 
discussed the effects of fuel hole numbers on detonation waves. Smirnov 
et al. [ 31 ] studied the effects of different mixture compositions on the 
onset of rotating detonation wave mode and the mean thrust is under 
consideration. 
With the breakthrough at ground environmental conditions, the 
development direction will be focused on the operation at real flight 
conditions. Understanding the working characteristics and performance 
of RDE in real flight conditions is increasingly urgent. Our previous 
study [ 32 , 33 ] reported the achievement of direct-connect RDE experi -
ments in a cavity-based annular combustor to approach the Mach 4 
flight condition at an altitude of 20 km. Liquid kerosene was directly 
injected into the combustor, resulting in the observation of rotating 
detonation waves that achieved approximately 60 % of the Chap -
man – Jouguet velocity. Li et al. [ 34 ] studied the multi-column film 
cooled hydrogen-enriched kerosene-fueled rotating detonation engine. 
Bell et al. [ 35 ] profiled the cross-sectional area of the RDE for improving 
the operability and effective integration of downstream hardware. Wen 
et al. [ 36 ] studied the propagation characteristics and stability of 
droplet-laden two-phase rotating detonation waves by theoretical 
analysis and numerical simulations. While these simulations involve 
prominent aspects of the ground operation of two-phase RDE, there 
remains insufficient research on RDE performance in real flight 
conditions. 
This study conducts numerical simulations on a two-phase kerosene/ 
air rotating detonation engine operating at Mach 5 and 24 km to explore 
the effects of engine size and droplet size at real flight conditions. The 
rest sections are structured as follows. Section 2 introduces the gov -
erning equations and numerical method, Section 3 presents the results 
and discussion, and Section 4 outlines the conclusions drawn from this 
study. 
2. Governing equations and numerical method 
2.1. Governing equations 
The two-phase rotating detonation phenomenon using droplets in -
volves multiphase flow, evaporation, combustion, and complex shock 
wave systems. The Navier-Stokes equations are solved for compressible, 
multi-component, and reactive flows. The droplet volume fraction ef -
fects on the gas phase are neglected since dilute sprays are considered 
[ 37 ]. The equations of mass, momentum, energy, and species mass 
fraction read 
∂ ρ
∂ t
+ ∇ • [ ρ u ] = S
mass
, (1)  
∂ ( ρ u )
∂ t
+ ∇ • [ u • ( ρ u )] + ∇ p + ∇ • T = S
mom ,
(2)  
∂ ( ρ E )
∂ t
+ ∇ • [ u ( ρ E + p )] + ∇ • [ T • u ] + ∇ • j = ˙ω
T
+ S
energy ,
(3)  
∂ ( ρ Y
m
)
∂ t
+ ∇ • [ u ( ρ Y
m
)] + ∇ • s
m
= ˙ω
m
+ S
species , m ,
( m = 1 , … M  1 ) , (4)  
p = ρ RT . (5)  
Where t is time, ρ is the gas density, u is the gas velocity vector, T is the 
gas temperature, p is the pressure, Y
m 
is the mass fraction of m- th species. 
E = e + | u |
2
/2 is the total non-chemical energy with e being the specific 
internal energy. R in Eq. (5) is the specific gas constant. M is the total 
species number. Only ( M - 1) species mass fractions are solved, and the 
inert species, i.e., nitrogen, is calculated from 
∑
M
m = 1
Y
m 
= 1. The source 
terms, S
mass
, S
mom
, S
energy
, and S
species , m
, denote the inter-phase exchanges 
of mass, momentum, energy, and species, respectively. T represents the 
viscous stress tensor, while j is the diffusive heat flux. Moreover, S
m 
is 
the species mass flux. ˙ω
m 
and ˙ω
T 
are the net reaction rate of m -th species 
and combustion heat release rate, respectively. 
The atomization and droplet interaction processes will increase the 
surface area of droplets, thus promoting the mass transfer and mo -
mentum transfer between droplets and gas [ 38 – 40 ]. To increase the 
combustion efficiency, atomizers should inject droplets with high ve -
locity into the combustor [ 41 ]. Although the results obtained will be 
more accurate and more authentic when the atomization and droplet 
interaction processes are simulated in detail, it becomes challenging to 
account for the atomization and droplet interaction processes of each 
droplet in large-scale numerical simulations, due to the significant in -
crease in computational requirements. This can potentially exceed the 
acceptable limits for computational resources. On one hand, the droplet 
size used in this study ranges from 5 μ m to 30 μ m, which can be 
considered to finish the effect of atomization. On the other hand, this 
study focuses on the size effect of droplets and engine combustors. 
Therefore, based on the consideration of calculation time and economic 
cost, the atomization and droplet interaction processes are ignored in 
this study. 
The sprayed fuel is assumed as droplet particles, and each droplet 
particle may contain dozens of droplets. The representative droplet 
particles are tracked by the Lagrangian method with point- 
approximation assumption. The evolutions of mass, velocity, and tem -
perature of individual fuel droplets are governed by 
dm
d
dt
=  ˙m
d
(6)  
d u
d
dt
=
F
d
m
d
, (7)  
c
p , d
dT
d
dt
=
˙
Q
C
+
˙
Q
lat
m
d
(8)  
where m
d 
is the droplet mass, u
d 
is the droplet velocity vector, and T
d 
is 
the droplet temperature. 
The phase transition of the liquid fuel droplet, i.e., evaporation, is 
crucial in two-phase detonations. This transition can be characterized 
using an equilibrium model, a non-equilibrium model, or a generalized 
model [ 42 , 43 ]. In this study, the phase change model employed is the 
non-equilibrium model of liquid evaporation boiling. The droplet 
evaporation rate ˙m
d 
is calculated from 
˙m
d
= π dShD
ab
ρ
s
ln ( 1 + X
r
) , (9)  
where d is the droplet diameter, D
ab 
the vapor diffusivity in the gaseous 
mixture, and ρ
s 
the density on the droplet surface. Sh = 2 . 0 +
0 . 6 Re
1 / 2
d
Sc
1 / 3 
is the Sherwood number, and Sc is the Schmidt number of 
the gas phase. The droplet Reynolds number, Re
d
, is calculated based on 
the velocity difference between two phases, i.e., Re
d
≡ ρ
d
d | u  u
d
| / μ . ρ
d 
represents the droplet material density and μ is the dynamic viscosity of 
the gaseous mixture. In Eq. (9) , X
r
≡ ( X
S
 X
C
) / ( 1  X
S
) is the concen -
tration difference between the gas flow and droplet surface, scaled by 
that between the droplet surface and interior. X
C 
is the fuel species molar 
fraction in the surrounding gas, while X
S 
is the fuel species molar 
W. Cao et al.

<!-- PDF_PAGE: 3 -->

Acta Astronautica 223 (2024) 108–118
110
fraction at the droplet surface. Note that the estimation of the molar 
ratio in Eq. X
r
≡ ( X
S
 X
C
) / ( 1  X
S
) does not account for the actual 
chemical reaction effects in the bulk gas. X
S 
can be calculated using 
Raoult ’ s Law X
S
= X
m
p
sat
p
, with which it has been assumed the inter- 
molecular force difference in the mixture is neglected. The p
sat 
is the 
saturated pressure and X
m 
is the molar fraction of the condensed species 
in the gas phase. 
In Eq. (7) , F
d 
is the force acting on the droplets, including the Stokes 
drag force (i.e., part I in Eq. (10) ) and pressure gradient force (i.e., part II 
in Eq. (10) ) [ 37 ] 
F
d
=
18 μ
ρ
d
d
2
C
d
Re
d
24
m
d
( u  u
d
)
⏟̅̅̅̅̅̅̅̅̅̅̅̅̅̅ ̅̅̅̅ ̅⏞⏞̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅ ̅ ̅⏟
І

1
6
π d
3
∇ p
⏟̅̅̅̅ ̅⏞⏞̅̅̅̅ ̅⏟
II
, (10)  
where C
d 
is the drag coefficient [ 44 ] 
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
≥ 1000
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
< 1000
, (11) 
The convective heat transfer rate 
˙
Q
C 
in Eq. (8) is 
˙
Q
C
= h
c
A
d
( T  T
d
) , (12)  
where A
d 
represents the surface area of a single droplet, and T
d 
is the 
droplet temperature. h
c 
is the convective heat transfer coefficient esti -
mated following Ranz and Marshall [ 45 ] 
Nu = 2 . 0 + 0 . 6 Re
1 / 2
d
Pr
1 / 3
, (13)  
where Nu and Pr are Nusselt and Prandtl numbers of the gas phase, 
respectively. Furthermore, heat transfer due to latent heat of vapor -
ization 
˙
Q
lat 
is 
˙
Q
lat
= h
g , boil
 h
l , boil
, (14)  
where h
g , boil 
and h
l , boil 
are the enthalpies of the gas phase and liquid phase 
at the droplet boiling temperature. 
The source terms in Eqs. (1) – (4) account for the influence of 
dispersed droplets on the gas phase and are estimated according to the 
droplets in individual cells 
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
, (15)  
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
(  ˙m
d
u
d
+ F
d
) , (16)  
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

Q
c
 ˙m
d
h
g , boil
)
, (17)  
S
species , m
=
{
S
mass
0
for condensed species
for other species .
, (18)  
where V
c 
is the CFD cell volume and N
d 
is the droplet number in a cell. 
Note that  ˙m
d
u
d 
in Eq. (16) denotes the evaporation-induced mo -
mentum exchange between the gas and liquid phases. 
2.2. Numerical method 
The governing equations for gas and droplet phases are solved by a 
hybrid Eulerian-Lagrangian solver RYrhoCentralFoam [ 28 ]. The solver 
has been validated through extensive benchmark tests including the 
RDE modelling with gaseous and liquid fuels [ 46 , 47 ]. The results show 
that the solver can accurately predict the response of fuel droplets to 
flows with shock waves and chemical reactions. For the gas phase 
equations, the second-order implicit backward scheme is applied for 
time discretization. For the liquid phase, the equations are solved by the 
implicit Euler method. Two-way coupling between the gas and liquid 
phases is implemented for each time step. 
A two-step kerosene/air reaction mechanism [ 48 ] is used in the 
current study. The chemical model contains six species (Kerosene, O
2
, 
CO, CO
2
, H
2
O, and N
2
), and two reactions, namely 
Kerosene + O
2
⇒ CO + H
2
O ,
CO + O
2
⇔ CO
2
. (19) 
Kerosene is defined by the literature [ 48 ], which is a combination of 
76.7 % C
10
H
22 
+ 13.2 % C
9
H
12 
+ 10.1 % C
9
H
18
. It used the thermo -
physical parameters provided in the literature [ 48 ]. The reaction rates 
are 
k
f 1
= A
1
f
1
( ϕ ) e
(

E
a , 1
RT
)
[ Kerosene ]
n
Kerosene
[ O
2
]
n
O
2 ,
1  
k
f 2
= A
2
f
2
( ϕ ) e
(

E
a , 2
RT
)
[ CO ]
n
CO
[ O
2
]
n
O
2 ,
2
. (20)  
where A
i 
is the pre-exponential factor, and E
a, i 
is the activation energy of 
the reactions. The reaction rates are given in Table 1 . f
1
( ϕ ) and f
2
( ϕ ) are 
the correction functions based on the equivalence ratio ϕ . The detailed 
descriptions are given in Table 2 [ 48 ]. 
The reliability of the two-step mechanism in detonation simulations 
has been well confirmed in Refs. [ 49 – 51 ] by comparing with a detailed 
mechanism JetSurF 2.0 [ 52 ] for detonation ZND (Zel ’ dovich-von Neu -
mann-D ¨oring) properties and ignition delay time with different equiv -
alence ratios and pressures. 
2.3. Physical model 
In this study, the rotating detonation engine size and droplet size 
were selected as key variables to explore their influence on the RDE 
performance. Typically, to simplify the three-dimensional physical 
model in an annular RDE [ 31 ], the curvature effects can be ignored and a 
two-dimensional physical model [ 47 ] can be adopted. As this method 
has been proven reliable, it was also adopted in the present study. 
Fig. 1 shows the simplified two-dimensional physical model. Here, l
a 
is the axial height, l
c 
is the circumferential length, and h
D 
is the deto -
nation height. The kerosene droplets gradually absorb heat and evapo -
rate into kerosene vapor as it moves downstream. Therefore, the 
detonation height is composed of the droplet heat absorption height h
A
, 
the evaporation height h
E
, and the vapor height h
V
. The lower boundary 
is the inlet of the fuel and oxidant, in which the gas is injected at an 
isentropic flow inlet condition [ 53 ]. The upper boundary is the outlet of 
the combustion product, and the left and right boundaries are periodic. 
In this study, air was used as the oxidant, and kerosene droplets were 
used as fuel. Table 2 lists the main injection and outlet parameters 
adopted in this study. Different from most simulations with the ground 
conditions [ 18 , 20 , 54 – 56 ], this study was performed at Mach 5 and 24 
km altitude, which can further reveal the rotating detonation behavior 
at flight operation conditions. 
2.4. Grid independence analysis 
The grid independence is verified by comparing the employed grid 
Table 1 
Reaction rate coefficients (mol, s, cm
3
, K, Cal) [ 48 ].   
Kerosene oxidation CO – CO
2 
equilibrium 
Activation energy 4.15 × 10
4 
2.0 × 10
4 
Pre-exponential factor 8.00 × 10
11 
4.5 × 10
10 
Reaction exponents n
Kerosene 
0.55 n
CO 
1.00 
n
O 2 , 1 
0.90 n
O 2 , 2 
0.50  
W. Cao et al.

<!-- PDF_PAGE: 4 -->

Acta Astronautica 223 (2024) 108–118
111
and refined grid. The employed grid in this study is 0.1 mm, and the 
refined grid size is 0.05 mm. The cases with 5 μ m and 30 μ m droplets are 
simulated using the employed grid and refined grid, respectively. The 
comparison of the two simulation results is listed in Table 3 . It can be 
found that the simulation results by the two girds are generally close, 
and the error is within 5 % for detonation velocity. Accumulation error 
estimation [ 57 ] is made, and the cumulative error of our simulations is 
less than 1.4E-5. This confirms the accuracy of our numerical 
simulations. 
Fig. 2 shows the temperature contours of the cases. The detonation 
waves have propagated for multiple cycles and become fully developed. 
It can be found that the detonation propagation velocity and the flow 
field structure of the two meshes are consistent. The propagation modes 
with different droplets are also not affected by the grids. Based on the 
acceptable computational cost and accuracy, the grid size of 0.1 mm can 
be adopted. The grid number is within 0.25 – 4 million for different cases 
in this study. 
3. Results and discussion 
This study focuses on the influence of the engine size and droplet 
diameter effects on the flow field and performance of the RDE in flight 
conditions. To investigate the engine size effects, four geometries ( l
c 
×
l
a
) are adopted, i.e., G1(0.1 × 0.03), G2(0.2 × 0.06), G3(0.3 × 0.09), and 
G4(0.4 × 0.12). Furthermore, in each geometry, four droplet sizes are 
simulated, i.e., 5 μ m, 10 μ m, 20 μ m, and 30 μ m. The equivalence ratio 
remains around 1.1. 
Table 4 lists the operation conditions for each case and displays the 
summary of the initiation results. Overall, most cases obtained self- 
sustained single wave (SW) rotating detonation waves, except for 
cases 3 and 4. Recently, Zhu et al. [ 58 ] used a 0.15 × 0.05 m model to 
simulate the two-dimensional non-premixed coal/hydrogen/air rotating 
detonation with a particle size of 1, 5, 10, and 20 μ m at an environ -
mental pressure of 0.1 MPa. In their research, sustainable rotating 
detonation waves were obtained. In this study, the 0.1 × 0.03 m model 
cannot obtain the detonation wave above 20 μ m (case 3 and case 4), 
while the 0.2 × 0.06 m model can obtain the detonation wave above 20 
μ m. This indicates that increasing the engine sizes can promote the 
two-phase rotating detonation, broadening the initial diameter range 
capable of obtaining rotating detonation waves. Three sub-studies are 
presented in this section to explore the effects of engine size and droplet 
diameter. The flow field structure is first presented. Then, the effect of 
the droplet size is analyzed, followed by the analysis of the engine size 
effect. 
3.1. The flow field structure 
Fig. 3 illustrates the temperature contour of the fully developed two- 
phase rotating detonation flow field in case 12. A stable single-wave 
propagation mode occurs in the RDE combustor, and the direction of 
the detonation wave propagation is from left to right. In the temperature 
contour, the typical flow field structure inside the RDE, including the 
detonation front (DF), oblique shock wave, slip line, fresh mixture layer 
(FML), and deflagration surface between the detonation product and 
FML, can be clearly captured. The main characteristics of the rotating 
detonation wave structures are similar to the previous research results 
on two-phase rotating detonation [ 59 ]. It can be found that rotating 
detonation waves can be obtained in both ground environmental con -
ditions and flight conditions. The droplets are mainly distributed in the 
FML after injection. The flow field of the RDE is critical for directly 
reflecting the complex combustion process and energy release. 
3.2. The effect of the droplet size 
Droplet evaporation can be affected by many factors, including the 
diameter, temperature, ambient temperature and pressure, and the 
shear speed of droplets and gas. In this section, the influence of droplet 
diameter on the rotating detonation will be analyzed. The contents 
include the kerosene vapor and droplet distribution, the influence of 
droplet size, the relationship between evaporation height and size, and 
the influence of evaporation behavior on RDE. 
Fig. 4 shows the temperature contours overlaid with droplet di -
ameters and smoke foils with different d
0 
(cases 9 – 12) in larger engine 
sizes (0.3 × 0.09). It can be seen from Fig. 4 that due to the small droplet 
size in case 9, the droplets can evaporate at a very short height (0.005 
m), and the h
E 
is much lower than the h
D
. The evaporation heights of 
cases 10, 11, and 12 are 0.014 m, 0.039 m and 0.047 m, respectively. 
Because of the small droplet size and high total injection temperature, 
the droplets in case 9 evaporate rapidly with injection, while the drop -
lets in case 12 almost reach the detonation height. With the increase of 
droplet sizes, the evaporation height gradually becomes higher, while 
the flow field structure does not change significantly. When d
0 
further 
increases to 20 μ m and 30 μ m, the evaporation and reaction rate near the 
inlet are too slow to be coupled with the leading shock, thereby forming 
a λ -shaped shock structure shown in Fig. 4 . From this figure, we also 
observe that this structure begins to appear above 20 μ m in the white 
box area of the pressure gradient contours. However, it did not appear 
when d
0 
is below 10 μ m, consistent with our previous research [ 60 ] in 
ground environmental conditions. 
With the increase in droplet diameter, it is observed that the deto -
nation front tends to be unstable. Due to the uneven chemical reaction 
intensity on the detonation front, the temperature distribution of the 
combustion products becomes uneven. More details can be seen through 
the locally enlarged pressure gradient contour. For example, as the 
droplet size increases, the cell structure near the inlet becomes irregular 
and gradually blurred. The cell structure in case 11 and case 12 is 
divided into two layers, as shown in the red box in Fig. 4 . The lower layer 
is blurred and difficult to identify, while the upper layer has a clear cell 
structure. At the same time, the formation of a λ -shaped shock structure 
was observed in the entrance region. This is because the droplets absorb 
Table 2 
Simulation conditions in this study.  
Mach Altitude 
/km 
Recovery 
coefficient 
Total 
pressure 
/MPa 
Total 
temperature 
/K 
Ambient 
pressure 
/Pa 
5 24 0.54 0.86 1242 2972  
Fig. 1. Schematic of two-phase rotating detonation physical model.  
Table 3 
Grid independence analysis results.   
Grid name Grid size Speed(m/s) Error
V
(%) 
Case5 Employed 0.1 mm 1687 0.17 
Refined 0.05 mm 1684 
Case8 Employed 0.1 mm 1401 4.56 
Refined 0.05 mm 1337  
W. Cao et al.

<!-- PDF_PAGE: 5 -->

Acta Astronautica 223 (2024) 108–118
112
heat from the high-temperature gas, and its temperature rises to the 
boiling point. Once the droplet temperature reaches the boiling point, 
the evaporation becomes violent and can be quickly consumed by the 
detonation front. Smaller droplets have a faster evaporation time and 
shorter evaporation height. In the lower layer of the FML, the liquid 
kerosene is more, whereas the evaporated kerosene vapor is very little 
when droplets are larger. This leads to the separation of the leading 
shock wave and the reaction zone. Thus, a λ -shaped shock structure is 
formed. With the increase in droplet size, this separation trend becomes 
more evident. Due to the droplet evaporation and detonation reaction 
coinciding, there is a significant velocity difference between the upper 
and lower parts of the detonation wave. The apparent difference in the 
propagation velocity causes the increase of the inclination angle, which 
is the key factor in forming the λ -shaped shock structure. Therefore, the 
different droplet sizes significantly influence the formation of the 
λ -shaped shock structure in the combustor. 
Fig. 5 shows the axial distributions of the kerosene vapor mass 
fraction and kerosene droplet volume fraction. The solid line is the mass 
fraction, and the dotted line is the volume fraction. The average h
D 
of 
cases 9, 10, 11, and 12 is 0.048 m, marked by an orange dotted line in 
the figure. When the fuel just enters the combustor, the droplet size is 
large, and the mass fraction of the kerosene vapor is extremely low. As 
the droplets move downstream, they gradually evaporate, and the 
change in volume fraction and vapor mass fraction conforms to the 
evaporation process. As the kerosene droplets reach the detonation 
height, it can be seen that the kerosene droplets have completely 
evaporated. The mass fraction is the lowest due to the intense con -
sumption. In the downstream of the detonation wave, the mass fraction 
is the highest, indicating unburned kerosene vapor. In the study of Yao 
et al. [ 18 ], it was also found that as the liquid fuel is injected at an 
ambient temperature and after the droplets mix with the hot air, the 
evaporation starts to progress gradually. When the droplets pass through 
the preceding detonation wave, they are instantly heated by the wave 
front, which results in a significant rise in temperature and fast 
evaporation. 
The effective equivalence ratio ( ϕ
eff
) is the minimum number of 
oxygen atoms required to convert all carbon atoms and hydrogen atoms 
into CO
2 
and H
2
O using the definition ϕ
eff
= ( n
C
+ n
H
/ 4 ) / ( n
O
/ 2 ) , 
where n
C
, n
H 
, and n
O 
denote the number of available carbon, hydrogen, 
and oxygen atoms, respectively. Fig. 6 shows the temperature and 
effective equivalence ratio distribution against the HRR in cases 9 – 12. 
As can be seen, the temperature and ϕ
eff 
are significantly affected by 
HRR. Specifically, the larger HRR results in a smaller ϕ
eff 
distribution 
and higher temperature. In addition, with the increased droplet size, the 
HRR scatters are clustered, and more HRR above 10
12 
J/m
3
/s can be 
observed. In case 12 (with the largest d
0
), the HRR above 10
14 
J/m
3
/s 
reaches the most, indicating the highest detonation intensity. The 
smallest ϕ
eff 
focuses on 2000 – 2500 K because the droplets absorb heat 
from the high-temperature gas to evaporation. Therefore, a low- 
temperature region is formed where the evaporation is the greatest 
and the HRR is low. When the droplet diameter is small, local fuel-rich 
regions occur in the low-temperature regions. This is because small 
droplets have a larger surface area to volume ratio, which increases the 
evaporation rate. The droplets absorb a lot of heat during evaporation, 
forming locally high ϕ
eff 
and low HRR regions. On the contrary, due to 
the slow evaporation rate of the larger diameter droplets, the evapora -
tion amount is smaller under the same conditions, reducing the ϕ
eff
. 
The droplet evaporation behavior has a significant effect on the 
droplet distribution in the RDE [ 54 ]. Fig. 7 shows the ratio of h
A
, h
E
, h
V 
Fig. 2. Grid independence validation (left: d
0 
= 5 μ m, right: d
0 
= 30 μ m), propagating after six cycles.  
Table 4 
Simulation case information and propagation results.  
Case No. l
c 
× l
a
, 
m × m 
d
0
, 
μ m 
Kerosene mass flow rate (kg/s) Phenomenon 
Case 1 0.1 × 0.03 5 0.09 SW 
Case 2 10 SW 
Case 3 20 Failure 
Case 4 30 Failure 
Case 5 0.2 × 0.06 5 0.18 SW 
Case 6 10 SW 
Case 7 20 SW 
Case 8 30 SW 
Case 9 0.3 × 0.09 5 0.27 SW 
Case 10 10 SW 
Case 11 20 SW 
Case 12 30 SW 
Case 13 0.4 × 0.12 5 0.36 SW 
Case 14 10 SW 
Case 15 20 SW 
Case 16 30 SW  
Fig. 3. Temperature contour overlaid with the droplet distribution in case 12.  
W. Cao et al.

<!-- PDF_PAGE: 6 -->

Acta Astronautica 223 (2024) 108–118
113
to h
D 
as a function of d
0 
in cases with l
c 
= 0.3 m. As shown in the figure, 
as the droplet size increases, the proportion of heat absorption and 
evaporation height gradually increases, while the proportion of vapor 
height decreases. This phenomenon can also be observed intuitively in 
Fig. 4 . This is because when the droplet size increases, the droplets need 
to absorb enough heat and gradually begin to evaporate after reaching 
the boiling point. Within the height from the inlet to the detonation 
height, small kerosene droplets quickly evaporate into vapor. However, 
larger-size kerosene droplets (such as d
0 
= 20 μ m and 30 μ m) exhibit 
obvious endothermic processes during evaporation and require a higher 
height to evaporate into vapor completely. 
Fig. 8 shows the variation trends of detonation wave height h
D 
and 
vapor height h
V
. Although the detonation height increases with the 
increased combustor length, the ratio of detonation height to the 
combustor is almost constant. From the research results of Yao et al. 
[ 18 ], the detonation height only accounts for 25 % of the length of the 
combustor at ground environment conditions. However, it can be seen 
that the detonation height accounts for nearly 55 % of the combustor 
length in this study. This indicates that the detonation height in flight 
conditions is higher than that in ground environmental conditions. In 
addition, as shown in Fig. 8 b, the vapor height h
V 
is significantly reduced 
with increased d
0 
and decreased l
c
. When the d
0 
is increased to 30 μ m, 
the h
V 
approaches 0 despite the l
c 
variation. This indicates the required 
heat absorbing and evaporation height exceeds the detonation height. 
The rotating detonation wave is mainly propagating through two-phase 
mixtures. These results reveal the variation of droplet evaporation in 
RDEs and further illustrate the influence of droplet size on the evapo -
ration process and combustion performance. 
Fig. 9 shows the ratio of evaporation height to combustor length, 
which reflects the proportion of fuel evaporation height through the 
combustor. The ratio of evaporation height increases with the increase 
in droplet size. This is because the larger the droplet size, the higher 
absorption heat height is required for complete evaporation. Further -
more, it can be seen from Figs. 8 and 9 that at the same droplet size, the 
detonation height and vapor height increase, and h
E
/ l
c 
decreases as 
engine size increases. This is because the evaporation rate is the same at 
the same droplet size and evaporation environment. Therefore, with the 
increase of the detonation combustor size, the corresponding proportion 
will decrease. From the perspective of height ratio, the injection heights 
of cases 2, 6, 10, and 14 accounts for 41.7 %, 21.7 %, 15.9 % and 13.0 % 
of the combustor height, respectively. These results indicate that with 
the increase in engine size, the evaporated fuel height ( h
V
) gradually 
increases (i.e., h
E 
gradually decreases), and thus, the rotating detonation 
wave in the large-size engine is more stable. 
Fig. 10 shows the detonation velocity and detonated fuel fraction 
( f
det
) at different droplet sizes and engine sizes. The f
det 
means that the 
detonation reaction of kerosene fuel in the combustor accounts for the 
proportion of the whole chemical reaction. The f
det 
is estimated based on 
the volume averaged detonation consumption rates of individual fuel 
conditioning on HRR greater than 10
13 
J/(m
3
⋅ s), approximately deemed 
to be detonative combustion [ 47 ]. 
f
det , Kerosene
= ˙ω
det , Kerosene
/
˙ω
Kerosene
(21)  
where ˙ω
det , Kero 
is the Kerosene consumption rate, conditioning on HRR >
10
13 
J/(m
3
⋅ s). It can be seen from Fig. 10 that the detonation wave 
velocity increases with the increase of engine size. The large engine size 
Fig. 4. Temperature contours overlaid with droplet diameters and smoke foils of cases 9 – 12.  
Fig. 5. Droplet mass fraction and vapor volume fraction distribution along the 
axial direction. Note that the solid line is the mass fraction, and the dotted line 
is the volume fraction. 
W. Cao et al.

<!-- PDF_PAGE: 7 -->

Acta Astronautica 223 (2024) 108–118
114
provides enough space for the droplets to absorb heat, evaporate, and 
mix. This can promote the fuel combustion heat release rate, thereby 
increasing the propagation velocity of detonation waves. In addition, 
from Figs. 8 and 10 , it can be seen that the variation trend of evaporation 
height and the detonation reaction is consistent. Compared with kero -
sene droplets, kerosene vapor is conducive to the detonation reaction. 
As the droplet size increases, the propagation velocity and the 
detonation reaction gradually decrease. When the droplet size increases 
from 20 μ m to 30 μ m, the decrease becomes significant. This phenom -
enon is consistent with the study of Wang [ 51 ]. This is due to the 
inconsistency between the height of heat absorption and evaporation 
required for different droplet sizes and the height provided by different 
engine sizes. The maximum velocity deficit of this study is 25 %, 
compared with the theoretical Chapman – Jouguet value. However, with 
the same droplet size, the velocity deficits in the current study (~15 %) 
are significantly lower than the simulations at ground operation con -
ditions (~22.5 %) [ 18 ]. Due to the lower environmental pressure and 
higher injection total temperature at flight conditions, the detonation 
height is higher ( Fig. 8 ). Therefore, the kerosene droplets have enough 
space to absorb heat, evaporate, and mix with the oxidant, which 
significantly enhances the intensity of the detonation wave. Thus, the 
velocity deficit is reduced. These results indicate that the flight condi -
tions resulted in more efficient combustion and reduced velocity deficits 
compared to ground environmental conditions. 
3.3. The effect of the engine size 
RDE has been widely studied, but there are few studies on the min -
imum size and operation limit of RDE. In this section, the influence of 
the size of RDE on the flow field is explored. When d
0 
is 20 and 30 μ m, 
the rotating detonation waves fail to be self-sustained. Thus, the case 
with d
0 
= 10 μ m was selected first to discuss the influence of engine size. 
Fig. 11 shows the temperature contours with different engine sizes. It 
can be seen that the λ -shaped shock structure only occurred in the en -
gine of 0.1 × 0.03 m size, but not in the larger size engine. From Figs. 4, 
9 and 11 , it can be found that the λ -shaped shock structure depends on 
h
E
/ l
c, 
with a critical value of 40 %. Exceeds the critical value, the 
λ -shaped shock structure is formed at the entrance. Hence, large-size 
engines provide a more stable propagation environment. The evapora -
tion height of fuel at different engine sizes is marked in Fig. 11 . It can be 
found that h
E 
is almost equal in Figs. 9 and 11 . However, the larger the l
c
, 
the smaller the h
E
/ l
c
. In the case with the same droplet size, the h
E
/ l
c 
in 
case 2 (i.e., the smallest engine size) is the largest, forming the λ -shaped 
shock structure. In the smaller combustor, the droplets are quickly flown 
away by the high-velocity airflow after the injection, and the droplets 
move to the contact surface between the FML and the combustion 
product before complete evaporation. In the larger combustor, the 
airflow velocity inside the combustor is slower. Compared with the 
small-size combustor, the droplets have enough time and space to absorb 
heat and evaporation. Therefore, in a larger combustor, the droplets can 
be completely evaporated within a short height and mixed with the 
oxidant. 
Fig. 12 shows the temperature and effective equivalence ratio dis -
tribution against the HRR in cases 2, 6, 10, and 14. As can be seen, the 
temperature and HRR are significantly affected by l
c
. Specifically, a 
larger l
c 
results in a higher ϕ
eff 
distribution and temperature. In addition, 
with the increased l
c
, the scatter points accumulate in the high HRR area. 
The large ϕ
eff 
accumulates in the region of low HRR. This is because, in 
the low HRR area, the droplets cannot absorb heat effectively and 
quickly evaporate into vapor, which leads to the local fuel-rich state. In 
Fig. 6. Temperature versus heat release rate in cases 9 – 12. Scatters are colored by the ϕ
eff
.  
Fig. 7. h
A
, h
E
, h
V 
account for h
D 
as a function of d
0 
in cases with l
c 
= 0.3 m.  
W. Cao et al.

<!-- PDF_PAGE: 8 -->

Acta Astronautica 223 (2024) 108–118
115
case 14 (with the largest l
c
), HRR above 10
13 
J/m
3
/s can be seen the 
most, indicating the highest detonation intensity. These results reveal 
that combustor sizes affect the detonation propagation by increasing the 
ϕ
eff 
and the HRR. 
Fig. 13 shows the ratio of h
A
, h
E
, and h
V 
to h
D 
as a function of l
c 
in 
cases with d
0 
= 10 μ m. As shown in the figure, as the combustor size 
increases, the heat absorption and evaporation proportion decrease 
while the vapor proportion gradually increases. This phenomenon can 
also be observed intuitively in Fig. 11 . When the droplet size is consis -
tent, the droplet evaporation process remains the same. However, when 
the combustor size increases, the height that the droplets can pass 
through is relatively short, and thus the proportion of vapor increases. 
The effective equivalence ratio at HRR > 10
12 
J/m
3
/s ( ϕ
eff, HRR > 1e12
) 
is calculated by a time-averaged method and a non-dimensional 
parameter droplet contribution efficiency [ 61 ] ( η
d
) is calculated by 
η
d
=
ϕ
eff , HRR > 1 e 12
 ϕ
g
ϕ
d
× 100% , (22)  
where ϕ
d 
and ϕ
g 
are the initially injected droplet equivalence ratio and 
fuel vapor equivalence ratio, and they are respectively equal to the 
global equivalence ratio and zero in this study. Fig. 14 shows the vari -
ation of ϕ
eff, HRR > 1e12, 
and η
d 
as a function of the droplet diameter d
0 
and 
engine length l
c
. It can be seen that the ϕ
eff, HRR > 1e12 
decreases with the 
increase of droplet size and increases with the increase of combustor 
size. This is consistent with the conclusion obtained above. When the 
droplet size increases, the droplet evaporation absorbs more heat, thus 
lowering the heat release rate. When the combustor size is increased, the 
height between heat absorption and evaporation is high enough for 
droplet evaporation, thereby reducing the heat release rate. As shown in 
Fig. 14 , at l
c 
= 0.4 m and d
0 
= 30 μ m, the ϕ
eff, HRR > 1e12 
is only 62.21 %. 
However, at l
c 
= 0.4 m and d
0 
= 5 μ m, the ϕ
eff, HRR > 1e12 
can rise to 
around 76.05 %. For the droplet contribution efficiency, the overall 
trend is consistent, and the variation range is within 50% – 75 %. 
As mentioned above, the detonation wave cannot be obtained when 
the combustor size is 0.1 × 0.03 m and d
0 
is larger than 10 μ m (i.e., case 
Fig. 8. Detonation wave height h
D 
and vapor height h
V 
as a function of d
0 
and l
c
.  
Fig. 9. h
E
/ l
c 
as a function of d
0 
and l
c
.  
Fig. 10. Detonation velocity and detonated fuel fraction as a function of d
0 
and l
c
.  
W. Cao et al.

<!-- PDF_PAGE: 9 -->

Acta Astronautica 223 (2024) 108–118
116
3, case 4). However, as the engine size increases, the rotating detonation 
can be self-sustained at d
0 
= 20 μ m and d
0 
= 30 μ m. The larger engine 
size provides a sufficiently high height to absorb heat and evaporate. 
Therefore, the heat absorption and evaporation height provided to the 
Fig. 11. Temperature contours overlaid by droplet diameters in different engine sizes.  
Fig. 12. Temperature versus heat release rate in cases 2, 6, 10, and 14. The scatters are colored by the ϕ
eff
.  
Fig. 13. h
A
, h
E
, and h
V 
account for h
D 
as a function of l
c 
in cases with d
0 
=
10 μ m. 
Fig. 14. ϕ
eff, HRR > 1e12 
and η
d 
as a function of d
0 
and l
c
.  
W. Cao et al.

<!-- PDF_PAGE: 10 -->

Acta Astronautica 223 (2024) 108–118
117
droplets by different engine sizes determine whether the detonation 
wave can be self-sustained. 
4. Conclusion 
This study used a two-step reaction mechanism of kerosene to 
simulate two-phase rotating detonations and obtained reliable results. 
The numerical simulations were conducted to study the detonation en -
gines operating in Mach 5 and 24 km conditions. The engine sizes and 
droplet diameters are investigated. The velocity performance, flow field 
structure in the FML, and RDE performance were analyzed. The main 
conclusions are as follows.  
1) The results found that all cases obtained the single wave propagation 
mode except for case 3 and case 4 (i.e., l
c 
= 0.1 m, d
0 
= 20, 30 μ m). 
The reason for the failure is that there is not enough endothermic 
evaporation height in cases 3 and 4. When 5 μ m and 10 μ m droplets 
are adopted, the RDE behaves like gaseous rotating detonations with 
clear cellular structures. When the 20 μ m and 30 μ m droplets are 
adopted, the rotating detonation waves tend to be divided into two 
layers and form the λ -shaped shock structure.  
2) The flight operation condition brings in differences in the features of 
detonation wave height and vapor height. The detonation height in 
flight conditions is higher than that in ground conditions. The vapor 
height significantly increases with increased engine size and 
decreased droplet size. The vapor height fraction h
V 
is only 24 % at l
c 
= 0.1 m with a fixed d
0 
of 10 μ m, while it can reach 76 % when l
c 
is 
increased to 0.4 m. When the d
0 
is increased to 30 μ m, the h
V 
ap -
proaches 0 despite the l
c 
variation. The rotating detonation wave is 
mainly propagating through two-phase mixtures. These results 
indicate that the design of the rotating detonation combustor must 
consider the real operation conditions and the effects of l
c 
and d
0
.  
3) Larger engine sizes and smaller droplet sizes lead to better mixing 
and dispersion of fuel, which promotes complete combustion and 
improves fuel utilization efficiency. These effects lead to higher 
propagation velocities. The velocity deficits in the current study 
(~15 %) are significantly lower than the simulations at ground 
environmental conditions (~22.5 %). This indicates that the flight 
conditions resulted in more efficient combustion and reduced ve -
locity deficits compared to ground environmental conditions. The 
maximum velocity deficit of this study is 25 % in cases with a large 
droplet diameter and small engine size. 
CRediT authorship contribution statement 
Wenbo Cao: Writing – original draft, Visualization, Investigation. 
Qiuyue Liu: Writing – original draft, Formal analysis. Fang Wang: 
Writing – review & editing, Writing – original draft, Funding acquisition, 
Conceptualization. Chunsheng Weng: Resources. 
Declaration of competing interest 
The authors declare that they have no known competing financial 
interests or personal relationships that could have appeared to influence 
the work reported in this paper. 
Acknowledgment 
This work is supported by the National Natural Science Foundation 
of China (No. 12202204), the China Postdoctoral Science Foundation 
(Nos. 2022M711622, 2023T160321), the Natural Science Foundation of 
Jiangsu Province (No. BK20220953), and the Fundamental Research 
Funds for the Central Universities. Numerical computations were per -
formed on Hefei advanced computing center. 
References 
[1] V. Raman, S. Prakash, M. Gamba, Nonidealities in rotating detonation engines, 
Annu. Rev. Fluid Mech. 55 (2023) 639 – 674 . 
[2] X.-p. Han, Q. Zheng, B.-x. Li, Q. Xiao, H. Xu, F. Wang, H.-l. Meng, W.-k. Feng, C.- 
s. Weng, Numerical simulation of flow field characteristics and the improvement of 
pressure oscillation of rotating detonation engine, Defence Technology 26 (2023) 
191 – 202 . 
[3] F. Wang, C.-s. Weng, Y.-w. Wu, Q.-d. Bai, Q. Zheng, H. Xu, Effects of total pressures 
and equivalence ratios on kerosene/air rotating detonation engines using a 
paralleling CE/SE method, Defence Technology 17 (2021) 1805 – 1816 . 
[4] Q. Zheng, H.-l. Meng, C.-s. Weng, Y.-w. Wu, W.-k. Feng, M.-l. Wu, Experimental 
research on the instability propagation characteristics of liquid kerosene rotating 
detonation wave, Defence Technology 16 (2020) 1106 – 1115 . 
[5] A. Batista, M. Ross, C. Lietz, W.A. Hargus, Detonation wave interaction 
classifications in a rotating detonation rocket engine, in: AIAA Propulsion and, 
Energy 2020 Forum, 2020 . 
[6] S.M. Frolov, I.O. Shamshin, V.S. Aksenov, P.A. Gusev, V.A. Zelensky, E. 
V. Evstratov, M.I. Alymov, Rocket engine with continuously rotating liquid-film 
detonation, Combust. Sci. Technol. 192 (2018) 144 – 165 . 
[7] S. Prakash, V. Raman, C.F. Lietz, W.A. Hargus, S.A. Schumaker, Numerical 
simulation of a methane-oxygen rotating detonation rocket engine, Proc. Combust. 
Inst. 38 (2021) 3777 – 3786 . 
[8] M. Ilbas, O. Kumuk, S. Karyeyen, Numerical study of a swirl gas turbine combustor 
for turbulent air and oxy-combustion of ammonia/kerosene fuels, Fuel 304 (2021) 
121359 . 
[9] J. Tellefsen, P. King, F. Schauer, J. Hoke, Analysis of an RDE with convergent 
nozzle in preparation for turbine integration, in: 50th AIAA Aerospace Sciences 
Meeting Including the New Horizons Forum and Aerospace Exposition, 2012 . 
[10] N.N. Smirnov, V.F. Nikitin, L.I. Stamov, E.V. Mikhalchenko, V.V. Tyurenkova, 
Three-dimensional modeling of rotating detonation in a ramjet engine, Acta 
Astronaut. 163 (2019) 168 – 176 . 
[11] V.S. Ivanov, S.M. Frolov, A.E. Zangiev, V.I. Zvegintsev, I.O. Shamshin, Hydrogen 
fueled detonation ramjet: conceptual design and test fires at Mach 1.5 and 2.0, 
Aero. Sci. Technol. (2021) 109 . 
[12] S.M. Frolov, V.I. Zvegintsev, V.S. Ivanov, V.S. Aksenov, I.O. Shamshin, D. 
A. Vnuchkov, D.G. Nalivaichenko, A.A. Berlin, V.M. Fomin, Wind tunnel tests of a 
hydrogen-fueled detonation ramjet model at approach air stream Mach numbers 
from 4 to 8, Int. J. Hydrogen Energy 42 (2017) 25401 – 25413 . 
[13] J. Wilhite, R.B. Driscoll, A.C. St George, V. Anand, E.J. Gutmark, Investigation of a 
rotating detonation engine using ethylene-air mixtures, in: 54th AIAA Aerospace 
Sciences Meeting, 2016. San Diego, California, USA . 
[14] K. Wu, S.-j. Zhang, D.-w. She, J.-p. Wang, Analysis of flow-field characteristics and 
pressure gain in air-breathing rotating detonation combustor, Phys. Fluids 33 
(2021) . 
[15] F. Wang, Q.Y. Liu, C.S. Weng, On the feasibility and performance of the ammonia/ 
hydrogen/air rotating detonation engines, Phys. Fluids 35 (2023) . 
[16] S.-J. Liu, S.-Y. Huang, H.-Y. Peng, X.-Q. Yuan, Characteristics of methane-air 
continuous rotating detonation wave in hollow chambers with different diameters, 
Acta Astronaut. 183 (2021) 1 – 10 . 
[17] G. Wang, W. Liu, S. Liu, H. Zhang, H. Peng, Y. Zhou, Experimental verification of 
cylindrical air-breathing continuous rotating detonation engine fueled by non- 
premixed ethylene, Acta Astronaut. 189 (2021) 722 – 732 . 
[18] S. Yao, X. Tang, W. Zhang, Structure of a heterogeneous two-phase rotating 
detonation wave with ethanol – hydrogen – air mixture, Phys. Fluids 35 (2023) . 
[19] H. Meng, Q. Zheng, C. Weng, Y. Wu, W. Feng, G. Xu, F. Wang, Propagation mode 
analysis of rotating detonation waves fueled by liquid kerosene, Acta Astronaut. 
187 (2021) 248 – 258 . 
[20] Q. Meng, N. Zhao, H. Zhang, On the distributions of fuel droplets and in situ vapor 
in rotating detonation combustion with prevaporized n-heptane sprays, Phys. 
Fluids 33 (2021) 043307 . 
[21] C. Ding, Y. Wu, G. Xu, Y. Xia, Q. Li, C. Weng, Effects of the oxygen mass fraction on 
the wave propagation modes in a kerosene-fueled rotating detonation combustor, 
Acta Astronaut. 195 (2022) 204 – 214 . 
[22] M. Zhao, K. Wang, Y. Zhu, Z. Wang, Y. Yan, Y. Wang, W. Fan, Effects of the exit 
convergent ratio on the propagation behavior of rotating detonations utilizing 
liquid kerosene, Acta Astronaut. 193 (2022) 35 – 43 . 
[23] I.B. Dunn, V. Malik, W. Flores, A. Morales, K.A. Ahmed, Experimental and 
theoretical analysis of carbon driven detonation waves in a heterogeneously 
premixed Rotating Detonation Engine, Fuel 302 (2021) . 
[24] H. Xu, X. Ni, X. Su, B. Xiao, Y. Luo, F. Zhang, C. Weng, Q. Zheng, Experimental 
investigation on the application of the coal powder as fuel in a rotating detonation 
combustor, Appl. Therm. Eng. 213 (2022) . 
[25] W. Wu, Y. Wang, W. Han, G. Wang, M. Zhang, J. Wang, Experimental research on 
solid fuel pre-combustion rotating detonation engine, Acta Astronaut 205 (2023) 
258 – 266 . 
[26] H.-Y. Peng, W.-D. Liu, S.-J. Liu, H.-L. Zhang, L.-X. Jiang, Hydrogen-air, ethylene- 
air, and methane-air continuous rotating detonation in the hollow chamber, Energy 
211 (2020) 118598 . 
[27] Z. Ma, S. Zhang, M. Luan, S. Yao, Z. Xia, J. Wang, Experimental research on 
ignition, quenching, reinitiation and the stabilization process in rotating 
detonation engine, Int. J. Hydrogen Energy 43 (2018) 18521 – 18529 . 
[28] Z. Huang, M. Zhao, Y. Xu, G. Li, H. Zhang, Eulerian-Lagrangian modelling of 
detonative combustion in two-phase gas-droplet mixtures with OpenFOAM: 
validations and verifications, Fuel 286 (2021) . 
W. Cao et al.

<!-- PDF_PAGE: 11 -->

Acta Astronautica 223 (2024) 108–118
118
[29] S. Yao, X. Tang, W. Zhang, Adaptive operating mode switching process in rotating 
detonation engines, Acta Astronaut. 205 (2023) 239 – 246 . 
[30] Q. Meng, N. Zhao, H. Zheng, J. Yang, Z. Li, F. Deng, A numerical study of rotating 
detonation wave with different numbers of fuel holes, Aero. Sci. Technol. 93 
(2019) 105301 . 
[31] N.N. Smirnov, V.F. Nikitin, L.I. Stamov, E.V. Mikhalchenko, V.V. Tyurenkova, 
Rotating detonation in a ramjet engine three-dimensional modeling, Aero. Sci. 
Technol. 81 (2018) 213 – 224 . 
[32] H.L. Meng, Q. Xiao, W.K. Feng, M.L. Wu, X.P. Han, F. Wang, C.S. Weng, Q. Zheng, 
Air-breathing rotating detonation fueled by liquid kerosene in cavity-based annular 
combustor, Aero. Sci. Technol. 122 (2022) 1 – 11 . 
[33] W. Feng, Q. Zheng, Q. Xiao, H. Meng, X. Han, Q. Cao, H. Huang, B. Wu, H. Xu, 
C. Weng, Effects of cavity length on operating characteristics of a ramjet rotating 
detonation engine fueled by liquid kerosene, Fuel 332 (2023) . 
[34] J. Li, J. Yu, J. Li, Y. Lei, S. Yao, W. Zhang, Investigation of hydrogen-enriched 
kerosene-fueled rotating detonation engine with multi-column film cooling, Phys. 
Fluids 36 (2024) . 
[35] K. Bell, D. Schwer, A.K. Agrawal, Profiling cross-sectional area of a radial rotating 
detonation combustor to increase pressure gain, Aero. Sci. Technol. 133 (2023) . 
[36] H. Wen, W. Wei, W. Fan, Q. Xie, B. Wang, On the propagation stability of droplet- 
laden two-phase rotating detonation waves, Combust. Flame 244 (2022) 112271 . 
[37] C.T. Crowe, J.D. Schwarzkopf, M. Sommerfeld, Y. Tsuji, Multiphase Flows with 
Droplets and Particles, second ed., CRC Press, 2011, p. 509 . 
[38] V.B. Betelin, N.N. Smirnov, V.F. Nikitin, V.R. Dushin, A.G. Kushnirenko, V. 
A. Nerchenko, Evaporation and ignition of droplets in combustion chambers 
modeling and simulation, Acta Astronaut. 70 (2012) 23 – 35 . 
[39] N.N. Smirnov, V.B. Betelin, A.G. Kushnirenko, V.F. Nikitin, V.R. Dushin, V. 
A. Nerchenko, Ignition of fuel sprays by shock wave mathematical modeling and 
numerical simulation, Acta Astronaut. 87 (2013) 14 – 29 . 
[40] N.N. Smirnov, V.F. Nikitin, V.R. Dushin, Y.G. Filippov, V.A. Nerchenko, J. Khadem, 
Combustion onset in non-uniform dispersed mixtures, Acta Astronaut. 115 (2015) 
94 – 101 . 
[41] V.V. Tyurenkova, M.N. Smirnova, L.I. Stamov, N.N. Smirnov, Mathematical 
modeling of droplet collisions in sprays under microgravity conditions, Acta 
Astronaut. 219 (2024) 459 – 466 . 
[42] V.V. Tyurenkova, Non-equilibrium diffusion combustion of a fuel droplet, Acta 
Astronaut. 75 (2012) 78 – 84 . 
[43] V. Tyurenkova, Two regimes of a single n-heptane droplet combustion, Acta 
Astronaut. 163 (2019) 25 – 32 . 
[44] A.B. Liu, D. Mather, R.D. Reitz, Modeling the effects of drop drag and breakup on 
fuel sprays, SAE Trans. 102 (1993) 83 – 95 . 
[45] M. Zhao, H. Zhang, Origin and chaotic propagation of multiple rotating detonation 
waves in hydrogen/air mixtures, Fuel 275 (2020) 117986 . 
[46] M. Zhao, Z. Ren, H. Zhang, Pulsating detonative combustion in n-heptane/air 
mixtures under off-stoichiometric conditions, Combust. Flame 226 (2021) 
285 – 301 . 
[47] Q. Meng, M. Zhao, H. Zheng, H. Zhang, Eulerian-Lagrangian modelling of rotating 
detonative combustion in partially pre-vaporized n-heptane sprays with hydrogen 
addition, Fuel 290 (2021) 119808 . 
[48] B. Franzelli, E. Riber, M. Sanjos ´e, T. Poinsot, A two-step chemical scheme for 
kerosene – air premixed flames, Combust. Flame 157 (2010) 1364 – 1373 . 
[49] F. Wang, C. Weng, Effects of divergence inlet on kerosene/air rotating detonation 
engines, AIAA J. 60 (2022) 4578 – 4600 . 
[50] F. Wang, C. Weng, Preliminary criterion for positive total pressure gain in 
kerosene/air rotating detonation combustor, AIAA J. 60 (2022) 6548 – 6556 . 
[51] F. Wang, C. Weng, Numerical research on two-phase kerosene/air rotating 
detonation engines, Acta Astronaut. 192 (2022) 199 – 209 . 
[52] H. Wang, E. Dames, B. Sirjean, D. Sheen, R. Tangko, A. Violi, J. Lai, 
F. Egolfopoulos, D. Davidson, R. Hanson, A high-temperature chemical kinetic 
model of n-alkane (up to n-dodecane), cyclohexane, and methyl-, ethyl-, n-propyl 
and n-butyl-cyclohexane oxidation at high temperatures, JetSurF version 2 (2010) 
19 . 
[53] Z. Luan, Y. Huang, S. Gao, Y. You, Formation of multiple detonation waves in 
rotating detonation engines with inhomogeneous methane/oxygen mixtures under 
different equivalence ratios, Combust. Flame 241 (2022) 112091 . 
[54] M. Zhao, H. Zhang, Rotating detonative combustion in partially pre-vaporized 
dilute n-heptane sprays: droplet size and equivalence ratio effects, Fuel 304 (2021) 
121481 . 
[55] H. Chen, R. Li, Y. Wu, H. Hu, Y. Zhu, Numerical study on rotating detonation 
combustion with the discrete distribution of partially pre-vaporized n-heptane 
sprays, Fuel 356 (2024) 129650 . 
[56] D.-W. Zhai, N.-B. Zhao, S. Jin, X.-F. Shao, H.-T. Zheng, Numerical study on the 
characteristics of rotating detonation wave with multicomponent mixtures, Int. J. 
Hydrogen Energy 48 (2023) 29786 – 29797 . 
[57] N.N. Smirnov, V.B. Betelin, V.F. Nikitin, L.I. Stamov, D.I. Altoukhov, Accumulation 
of errors in numerical simulations of chemically reacting gas dynamics, Acta 
Astronaut. 117 (2015) 338 – 355 . 
[58] W. Zhu, Y. Wang, Effect of hydrogen flow rate and particle diameter on coal- 
hydrogen-air rotating detonation engines, Int. J. Hydrogen Energy 47 (2022) 
1328 – 1342 . 
[59] Z. Ren, L. Zheng, Numerical study on rotating detonation stability in two-phase 
kerosene-air mixture, Combust. Flame 231 (2021) 111484 . 
[60] F. Wang, W. Cao, C. Weng, Numerical research on kerosene/hydrogen/air rotating 
detonation engines with discrete injection strategies, Phys. Fluids 35 (2023) . 
[61] F. Wang, C. Weng, H. Zhang, Semi-confined layered kerosene/air two-phase 
detonations bounded by nitrogen gas, Combust. Flame 258 (2023) . 
W. Cao et al.
