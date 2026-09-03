<!-- PDF_PAGE: 1 -->

Fuel 290 (2021) 120019
Available online 29 December 2020
0016-2361/© 2020 Elsevier Ltd. All rights reserved.
Full Length Article 
Large-eddy simulation of methane direct injection using the full 
injector geometry 
M.R. Yosri
a , *
, J.Z. Ho
a
, M. Meulemans
a
, M. Talei
a
, R.L. Gordon
a
, M.J. Brear
a
, D. Cosby
b
, J. 
S. Lacey
c 
a
Department of Mechanical Engineering, University of Melbourne, Parkville, VIC 3010, Australia 
b
Continental, Newport News, VA, USA 
c
Department of Mechanical Engineering, KU Leuven, 3001 Leuven, Belgium   
ARTICLE INFO  
Keywords: 
Large-Eddy Simulation (LES) 
Constant Volume Chamber (CVC) 
Schlieren 
Under-expanded gaseous jet 
Direct Injection (DI) 
ABSTRACT  
Understanding the mixing process of under-expanded gaseous-fuel jets from an outward opening injector is 
essential for developing Direct Injection (DI) internal combustion engines. This paper presents a Large-Eddy 
Simulation (LES) study of the DI of methane into a Constant Volume Chamber (CVC), considering the full, in -
ternal geometry of a prototype injector. Four cases at conditions relevant to Compressed Natural Gas (CNG) DI 
engines are investigated, with methane as a surrogate for CNG. A new post-processing method permits the 3D 
LES field to be projected into a 2D density gradient field that can be compared to a schlieren image. The LES 
results are then validated against high-speed, schlieren imaging experiments, demonstrating that the simulations 
are able to reproduce experimental trends. Three main regions of the external flow are observed: a recirculation 
zone just downstream of the injector tip, a stagnation zone and a far-mixing zone. The location of the stagnation 
zone increases as the CVC pressure decreases, consistent with a theory presented in the literature. The modelling 
of the full internal geometry of the injector leads to a determination of the injector pressure losses. Once the 
pressure loss within the injector is considered, a short version of the injector can reasonably represent the full 
injector for prediction of the external flow.   
1. Introduction 
Internal Combustion (IC) engines dominate the transport sector. One 
pathway to reduce their emissions is through the use of low carbon, 
alternative fuels such as Compressed Natural Gas (CNG). This fuel has 
significant potential as a long-term solution because of its favourable 
properties when compared to conventional fuels, including low Partic -
ulate Matter (PM), nitrogen oxide ( NO
x
), and CO
2 
emissions, and high 
antiknock resistance [1 – 6] . An in-depth understanding of CNG injection 
processes is required in order to optimise fuel mass flow and air/fuel 
mixing to obtain these benefits. 
The most common fuel injection methods for natural gas Spark 
Ignition (SI) engines are Port Fuel Injection (PFI) and Direct Injection 
(DI). In Port Fuel Injection, CNG and air are mixed before entering the 
cylinder, whereas for Direct Injection CNG is injected directly into the 
cylinder. CNG DI leads to higher volumetric efficiency and power output 
than PFI for a given engine displacement [7 – 10] . To achieve sufficient 
mass flow rate and fast air/fuel mixing, CNG DI requires higher rail 
pressures [11] , typically from 16 to 20 bar compared to 2 to 10 bar for 
PFI [12,13] . 
In the DI system, the Nozzle Pressure Ratio (NPR) is defined as the 
ratio of rail pressure to cylinder or chamber pressure. The NPR is one of 
the critical parameters affecting the fuel mass flow rate and air/fuel 
mixing. Donaldson and Snedeker showed that by increasing the NPR, the 
gas jet transitions from a subsonic jet to moderately under-expanded 
(1 . 1 < NPR < 2) and eventually to a highly under-expanded jet 
(2 < NPR ) [14] . With DI rail pressures of 20 bar and chamber pressures 
from 0.4 – 4 bar at the start of the injection, moderately to highly under- 
expanded jets are expected to be present in CNG DI. These jets display 
complex flow phenomena such as shock waves and expansion fans 
which affect the mass flow rate and air/fuel mixing [15] . 
In addition to NPR, the geometrical features of the gas injector can 
have an impact on the mass flow rate and air/fuel mixing. Early gen -
erations of CNG direct injectors had a similar design to gasoline direct 
injectors, featuring an inward opening valve. This kind of gas injector 
suffers from issues such as fuel leakage. The newest generation of CNG 
* Corresponding author. 
E-mail address: mysori@student.unimelb.edu.au (M.R. Yosri).  
Contents lists available at ScienceDirect 
Fuel 
journal homepag e: www.else vier.com/loc ate/fuel 
https://doi.org/10.1016/j.fuel.2020.120019 
Received 19 August 2020; Received in revised form 23 November 2020; Accepted 14 December 2020

<!-- PDF_PAGE: 2 -->

Fuel 290 (2021) 120019
2
direct injectors feature an outward opening poppet valve which can be 
sealed by the cylinder pressure [16] . However, the geometry of outward 
opening injectors is complex. Phenomena such as choking, shock waves 
and boundary layer separation can occur as compressible gas flows 
through the small passages [17] . 
Swanteka et al. investigated the quasi-steady-state behaviour of CNG 
DI by varying the fuel rail pressure from 10 bar to 15 bar [18] . They 
showed that for an outward opening injector, the external flow could be 
divided into recirculation, stagnation, and mixing regions. Keskinen 
et al. showed that the shape of the jet of the outward-opening injector is 
strongly affected by changes of the injection timing, NPR, and the pro -
trusion angle of the injector ’ s poppet valve [19] . Vuorinen et al. and 
Hamzehloo et al. carried out LES to investigate the transient develop -
ment of highly under-expanded gaseous jets of methane ( CH
4
), nitrogen 
( N
2
) and hydrogen ( H
2
) in a wall-bounded closed system with a single 
hole nozzle [15,20 – 23] . They showed that increasing NPR can increase 
the Mach disk location and width, the penetration length and the 
volumetric growth of the jet. They also found that increasing the 
chamber temperature at a given NPR results in an increase of both the jet 
penetration and volume. Recently, Bartolucci et al. used LES to inves -
tigate mixing and turbulent characteristics of direct injection of argon 
into nitrogen using an outward opening injector [24] . They demon -
strated that a higher NPR leads to formation of complex eddy structures 
at the tip of the gaseous jet whereas a lower NPR features a more 
compact jet with smaller eddies. A comprehensive transient simulation 
of CNG DI through a realistic injector geometry has not yet been 
reported. 
One key parameter in the modelling of these types of injectors is 
considering the valve lift at the start of injection. Baratta et al. compared 
the jet shape of the CNG DI qualitatively with schlieren images with and 
without considering the needle valve movement [25 – 27] . They showed 
that the movement of the injector ’ s needle valve causes pressure waves 
to propagate within the injector, affecting the injector mass flow rate. 
Deshmukh et al. used LES to study the transient development of an 
outward opening injector in an open ambient condition without 
considering the poppet valve motion [17,28,29] . The transient injector 
movement was shown to have a significant impact on the gaseous jet 
formation and air/fuel mixing parameters such as penetration length, 
maximum width and volumetric growth of the jet. Up to 30% over- 
prediction compared with experimental results can be observed if the 
valve lift movement is not considered. 
This study therefore undertakes LES of methane direct injection with 
simulation of the full internal geometry and valve lift of an outward 
opening, prototype injector. The simulation results are compared with 
experimental results from a Constant Volume Chamber (CVC) [30] . 
Different conditions are considered by varying the chamber pressure and 
temperature. The flow field inside the injector and the external jet 
characteristics are studied in detail to determine the requirements for 
high-fidelity simulation of CNG injection. 
2. Experimental setup 
2.1. DI CNG injector 
The injection hardware is a prototype DI CNG injector provided by 
Continental [31] . A cross-section of this injector is shown in Fig. 1 . It 
consists of two main sections, which are intended to reduce gas leakage. 
There is an internal, inward opening “ cold ” valve that is actuated by a 
solenoid, and an outward opening “ hot ” valve that is spring actuated and 
is driven by the gas pressure force. The gas delivered by this injector is in 
a hollow cone configuration with a 50
◦
angle poppet valve. The cold 
valve has an asymmetric geometry, with two holes downstream of the 
valve whose axes are in the y-direction. 
2.2. Constant Volume Chamber (CVC) and operating conditions 
The Constant Volume Chamber (CVC) was recently used in a series of 
experimental studies performed by the group [30,32 – 35] . The CVC is a 
stainless steel cube with the intersection of three 90 mm diameter holes 
and fused silica windows, providing optical access to the chamber. 
In the study by Lacey et al., methane (a surrogate for CNG) was 
injected into quiescent, non-reacting nitrogen to examine the funda -
mental mechanisms governing the development of methane jets [30] . 
They investigated several thermodynamic states relevant to modern DI 
engines by varying the CVC temperature and pressure, and the fuel 
temperature. The two temperatures are intended to emulate a cold en -
gine at 298 K, and a fully warmed up engine at 360 K. The pressures used 
in their study represent a range of in-cylinder pressures that the fuel jet 
could encounter, based upon different levels of boosting or different 
injection timings. The rail pressure was kept constant at 20 bar , as this 
value is relevant to what would be expected in DI CNG engines. The 
experimental and numerical test conditions, shown in Table 1 , will be 
investigated in this work. 
2.3. Valve lift profile 
The valve lift profile is required as a boundary condition in the LES 
injection modelling. A set of experiments were carried out using high- 
speed imaging with a Photron SA1.1 Fastcam and a 150 mm focal 
length macro lens to obtain this profile for different CVC conditions. The 
injector was pulsed for 2 ms and movies were recorded at 30,000 frame 
per second (fps) with a physical scaling of approximately 25 μ m per 
Fig. 1. Sectional view of the prototype Continental DI CNG injector, indicating 
the flow passage in blue, and the inward ( “ hot ” ) and outward opening ( “ cold ” ) 
valves [31] . 
Table 1 
Operating conditions of cases considered.  
Case No. Condition CVC Pressure CVC Temperature 
1 Changing CVC Pressure 0.4 bar 298 K 
2 1 bar 298 K 
3 3 bar 298 K 
4 Changing Temperature 1 bar 360 K  
Fig. 2. Experimental valve lift profile for P
CVC 
= 1 bar (solid black line) and 
P
CVC 
= 3 bar (dashed blue line) with P
rail 
= 20 bar . 
M.R. Yosri et al.

<!-- PDF_PAGE: 3 -->

Fuel 290 (2021) 120019
3
pixel. The edge of the poppet valve is determined in each image through 
a post-processing routine, and valve lift profile versus time can then be 
determined. 
The valve lift profiles are shown for two cases in Fig. 2 . There is a 700 
μ s delay between sending the “ open ” signal to the solenoid and the 
opening of the valve. The valve opens over approximately 300 μ s until it 
reaches its maximum height. The injector ’ s hot, inward opening valve 
then fluctuates until it reaches a stable condition after approximately a 
further 500 μ s . When the signal is turned off, the valve gradually closes 
and experiences a bounce before completely closing. There are small 
differences between the valve lift profiles across the range of tested 
chamber pressures ( P
CVC
). With increasing chamber pressure, the 
amplitude and duration of the fluctuations increases. This may affect the 
injector mass flow rate, particularly for the case with the highest 
chamber pressure. 
2.4. Validation mass flow rate measurement 
Validation data for the mass flow rate through the injector was ob -
tained by measuring a long-duration static mass flow rate of a nitrogen 
injection into air at ambient conditions. The rail pressure was kept 
constant at 20 bar by using a bottle of pressurised nitrogen connected to 
a pressure regulator. The gas is then stored in an accumulator to provide 
enough gas during the time of injection. A Coriolis mass flow meter 
(Micro Motion CMF010M) was used to measure the mass flow rate, and a 
pressure transducer was installed before the injector to record the 
pressure during the injection. The injector was pulsed for 1 s to ensure 
the Coriolis mass flow meter could record a steady-state measurement. 
At each tested condition, the injection event was repeated five times to 
ensure the data were repeatable. The results of this experiment will be 
discussed in Section 4.1 . 
3. Numerical methods 
LES was performed using the CONVERGE CFD software package 
[36] . CONVERGE uses a finite volume method to discretise the conser -
vation equations with a second-order-accurate spatial discretisation 
scheme. The Pressure Implicit with the Splitting of Operators (PISO) 
algorithm was then used to solve the governing equations [37] . Shock 
treatment was undertaken with a step flux limiter [36] . A variable time 
step, calculated based on the maximum of the Courant Friedrich Lewy 
(CFL) number was used. The time step varied from 1 e
 9
s to 5 e
 8
s with 
the total injection duration of 2 ms . 
3.1. Governing equations 
LES decomposition is based on spatial filtering, accomplished by 
Favre density-weighted filtering, defined as: 
̃
ϕ
(
x , t
)
=
ρ ϕ
ρ
. (1) 
The quantity ϕ can then be decomposed into its filtered and sub-grid 
terms: 
ϕ =
̃
ϕ + ϕ
′
, (2)  
where 
̃
ϕ is the filtered (or resolved) variable and ϕ
′
is the Sub-Grid Scale 
(SGS) variable. The momentum equation is used here to explain the LES 
decomposition: 
∂ ρ ̃u
i
∂ t
+
∂ ρ ̃u
i
̃u
j
∂ x
j
= 
∂ P
∂ x
i
+
∂ σ
ij
∂ x
j

ρ∂τ
ij
∂ x
j
, (3)  
where ρ is the density of the mixture, u is the velocity, P denotes the 
pressure and σ
ij 
is the resolved shear stress tensor. The sub-grid stress 
term ( τ
ij
) is as follows: 
τ
ij
=

̃u
i
u
j
 ̃u
i
̃u
j
)
. (4) 
The term τ
ij 
cannot be computed directly and needs to be modelled. 
The one equation, non-viscosity based Dynamic Structure model was 
used to model τ
ij 
[38] . In this method, a transport equation for the sub- 
grid kinetic energy is additionally solved, 
∂ ρ k
∂ t
+
∂ ρ ̃u
j
k
∂ x
j
=
∂
(
μ
Pr sgs
∂ k
∂ x
j
)
∂ x
j
+ ρτ
ij
S
ij
 ρ ∊ , (5)  
where Pr
sgs 
is set to be 0.87 and μ is the dynamic viscosity [38] . The term 
S
ij 
denotes the filtered strain rate tensor, k is the sub-grid kinetic energy 
and ∊ is the sub-grid dissipation rate, defined as follows, respectively: 
S
ij
=
1
2
(
∂ ̃u
i
∂ x
j
+
∂ ̃u
j
∂ x
i
)
, (6)  
k =
1
2
(
̃u
i
u
i
 ̃u
i
̃u
i
)
, and (7)  
∊ = C
∊
k
1 . 5
Δ
. (8) 
The variable C
∊ 
is a model constant and Δ is the grid size. In this 
study, C
∊
= 1 following the approach of [39] . 
Dynamic LES models require a second filtering operation using a test 
filter, which is twice the grid size ( Δ
⌢
). The test level filtered stress 
tensor, T
ij 
is defined as: 
T
ij
=
(
̃u
i
u
j
⌢
 ̃u
i
⌢
̃u
j
⌢
)
. (9) 
Germano ’ s identity [40] relates the grid level tensor to the test level 
tensor by: 
L
ij
= T
ij
 τ
ij
⌢
=
(
̃u
i
̃u
j
⌢
 ̃u
i
⌢
̃u
j
⌢
)
, (10)  
where L
ij 
is the Leonard stress term [40] . In the dynamic structure 
model, the SGS stress tensor is modelled as a function of SGS kinetic 
energy which are given by: 
τ
ij
= c
ij
k , (11)  
T
ij
= c
ij
K , (12)  
where c
ij 
is the coefficient tensor and K denotes the test level kinetic 
energy which is defined by: 
K =
1
2
(
̃u
i
u
i
⌢
 ̃u
i
⌢
̃u
i
⌢
)
. (13) 
The trace of the Leonard term relates the test and grid level kinetic 
energies by: 
K = k
⌢
+
1
2
L
ii
. (14) 
Using Eqs. (14), (11) and (12) , Germano ’ s identity (Eq. 10 ) can be 
written as: 
L
ij
=
1
2
c
ij
L
ii
. (15) 
The tensor coefficient c
ij 
can now be obtained from Eq. 15 and be 
substituted into Eq. 11 to calculate τ
ij
: 
τ
ij
= 2 k
L
ij
L
ii
, (16)  
M.R. Yosri et al.

<!-- PDF_PAGE: 4 -->

Fuel 290 (2021) 120019
4
3.2. Computational domain and grid parameters 
Fig. 3 shows the computational domain, including the internal ge -
ometry of the injector, a portion of the CVC, and the boundary condi -
tions. In order to reduce the computational cost, Adaptive Mesh 
Refinement (AMR) was employed [36] . AMR was activated based on 
thresholds on velocity and methane mass fraction ( Y
CH
4
) fields. The base 
grid-size of this study is 1 mm , and the smallest grid size is 0.03 mm . 
Further details on the AMR algorithm can be found in Ref [36] . The 
minimum grid size was chosen following Baratta et al., who propose that 
to obtain an accurate mass flow rate, the critical section of the injector 
should have at least 10 – 15 grid points [26] . In this geometry, this 
location is taken to be the throat at the choking location, which has 12 
grid points. Moreover, for Case 1 (highest NPR), a simulation with a 
finer grid was performed, which resulted in negligible difference (5 – 7%) 
compared to the penetration and cone angle results achieved with the 
original grid. 
3.3. Boundary conditions 
A fuel rail pressure of 20 bar , methane mass fraction of 1 and tem -
perature of 298 K or 360 K were used as the inlet condition. Depending 
on the operating regime, different wall boundary conditions can be used. 
The maximum Knudsen number was less than 0.1 for this injector, 
therefore the velocity slip boundary condition was applied to the walls, 
as proposed by [41] . At the tip of the poppet wall, as the boundary layer 
separation is essential, the no-slip boundary condition was applied [17] . 
All walls were adiabatic. 
3.4. Initial conditions 
The initial conditions were imposed in three different regions. The 
flow path in the cold valve was initialised using the conditions at the 
injector inlet. As it takes more than 500 μ s to completely close the 
injector after the closing of the cold valve (see Fig. 2 ), the flow path in 
the hot valve was initialised with the pressure and temperature of the 
CVC, but with a mass fraction of methane, Y
CH
4
= 1. The third region is 
the chamber itself, which is initialised with the pressure and tempera -
ture of the selected case and pure nitrogen as a mass fraction Y
N
2
= 1. 
3.5. Post-processing method 
3.5.1. Numerical representation of schlieren images 
Lacey et al. reported the results for the axial penetration of the jet 
and the jet spreading angle, which is defined as the cone angle 5 mm 
downstream of the injector [30] . These two values characterise the jet 
development. The axial penetration was recorded for 500 μ s After the 
Start Of Injection (ASOI), where the fuel exits from the injector (0 ASOI 
μ s ≈ 700 μ s in Fig. 2 ) up until the jet leaves the imaging window at 37 
mm . The cone angle is calculated from 500 μ s to 2000 μ s ASOI, which is 
the period when the jet operates in a quasi-steady state condition. 
To find these two parameters from the LES results, a new post- 
processing technique is required. The experimental schlieren images 
visualise the volumetric inhomogeneities in the gas by showing the 
variations in the refractive index projected onto a two-dimensional 
plane. The two-dimensional schlieren images are a set of lighter and 
darker regions representing the positive and negative density gradients 
in the direction normal to the knife-edge [42] . The z-type schlieren 
imaging configuration used in Lacey et al. images the projected density 
gradient corresponding to the z-direction in the computational domain. 
In order to find the density gradient from the LES results, the three- 
dimensional data must first be projected onto the same two- 
dimensional plane as the focal plane of the schlieren imaging system. 
A post-processing code was written to approximate the density gradient 
in each grid point as: 
∂ρ
∂ x
i
=
ρ
x i + d
 ρ
x i
d
, (17)  
where ρ is the density, x
i 
is the Cartesian coordinates and d denotes the 
mesh size. The values on the original grid were linearly interpolated 
onto a grid of uniform spacing to determine the density gradients 
because AMR was used to generate the original grid. The linear Delau -
nay triangulation method was employed for this interpolation [43] . The 
density gradient values were then spatially ensemble-averaged in the y- 
direction with a number of planes. The distance between each two 
planes, Δ , was equal to the smallest grid size. 
3.5.2. Cone angle and penetration length 
For the LES results, the projected density gradient field was analysed 
to determine the jet boundary. A fluid element with a density gradient 
greater than 0.1% of the maximum value in the domain was considered 
to be inside the jet, provided that the mass fraction of methane is also 
greater than 0.1%. These threshold values were found appropriate based 
on visual inspection of the jet, and conditioning with the fuel mass 
fraction avoids identification of density gradients from pressure waves. 
After determining the jet boundary, two lines were plotted from the 
injector tip corners to the edge of the jet boundary 5 mm downstream. 
The jet spreading angle is the angle between these lines. The maximum 
axial penetration is the maximum axial distance from the tip of the 
injector to the jet boundary. The experimental post-processing methods 
and results for the jet spreading angle and penetration results are 
documented in the study of Lacey et al. [30] . 
4. Results and discussions 
Validation results are presented for the injector mass flow rate, 
penetration length, jet spreading angle and location of the Mach disk 
using both experimental results and empirical correlations for all cases. 
Then, for Case 2 ( P
CVC
= 1 bar and T = 298 K) as a reference case, the 
flow within the injector and its effect on the external flow features such 
as penetration length and jet spreading angle is investigated. Finally, for 
Case 2, the transient development of the external flow and the mixing 
process is discussed. 
Fig. 3. Sectional view of the computational domain.  
M.R. Yosri et al.

<!-- PDF_PAGE: 5 -->

Fuel 290 (2021) 120019
5
4.1. Injector mass flow rate 
The injector mass flow rate under steady state conditions was 
measured experimentally in Subsection 2.4 , and compared with those 
obtained from analytical and LES results. In this injector, the flow is 
choked when the downstream pressure (i.e. P
CVC
) falls below a critical 
pressure, P
*
, determined by: 
P
*
P
t
=
(
2
γ + 1
) γ
γ  1
, (18)  
where γ is the specific heat ratio of the gaseous jet and p
t 
indicates the 
upstream static pressure (i.e. the fuel rail pressure). At a 20 bar fuel rail 
pressure, the value of p
* 
is 10.56 bar for a nitrogen jet and 10.88 bar for a 
methane jet. The maximum CVC pressure is 3 bar in this study, hence the 
flow is choked for all cases. Therefore, the mass flow rate ( ˙m ) can be 
calculated using the following formula [44] : 
˙m =
P
t
̅̅̅̅̅̅̅ ̅
RT
t
√ A
*
̅̅ ̅
γ
√
(
1 +
γ  1
2
) γ + 1
2 ( 1  γ )
, (19)  
where T
t 
is the upstream static temperature ( T
t
= 298 K ), R is the gas 
constant and A
* 
is the choked cross-sectional area. The mass flow rate 
was calculated analytically using Eq. (19) , and numerically from the LES 
results. For the analytical solution, A
* 
was determined from the LES 
results. These values are compared with the measured data in Table 2 . 
The time-averaged steady-state Mach number field obtained from 
LES is shown in Fig. 4 . In order to illustrate the choking area within the 
injector, the iso-surface of Mach = 1 is used. The flow is choked inside 
the injector just upstream of the nozzle exit when the valve is fully open. 
As can be seen from Table 2 , both analytical and numerical results show 
a very good agreement (less than 5% difference) with the experimental 
data. 
4.2. Pressure loss inside the injector 
Fig. 5 a shows the area-averaged pressure at various streamwise lo -
cations through the injector under quasi-steady state conditions (500 μ s 
to 2000 μ s ASOI) for Case 2. A significant pressure loss within the 
injector is observed from 20 bar in the rail to 10 bar at the nozzle exit. 
The variable Z
* 
is the axial distance from the injector inlet, non- 
dimensionalised by the total length (See Fig. 4 ). Fig. 5 b shows the 
area-averaged pressure at Z
*
= 0 . 45 obtained from the simulation of the 
entire injector under transient conditions. The pressure is initialised at 1 
bar and then increases to 12 bar at 300 μ s . After that, it reaches a quasi- 
Table 2 
The injector mass flow rate obtained from experimental, numerical and 
analytical results; P
rail 
= 20 bar , T = 298 K.  
Approach Mass flow rate ( g / s )  Difference % 
Experiments 11.07 – 
Analytical 11.38 2.8% 
Numerical 10.57 4.5%  
Fig. 4. Time-averaged steady-state Mach field within the injector for nitrogen P
CVC 
= 1 bar , Prail = 20 bar and T = 298 K, Z
* 
is the non-dimensionalised 
injector length. 
Fig. 5. a) Area averaged pressure with respect to non-dimensionalised injector length ( Z
*
), b) Area averaged pressure at Z
*
= 0 . 45 with respect to time P
CVC 
= 1 bar , 
T = 298 K. 
M.R. Yosri et al.

<!-- PDF_PAGE: 6 -->

Fuel 290 (2021) 120019
6
steady-state condition (see Fig. 5 b). The observed fluctuations are due to 
the pressure waves travelling inside the injector. 
In order to investigate the impact of the injector internal geometry on 
global external flow parameters, a short version of the injector is 
modelled from Z
*
= 0 . 45 for Case 2. Two additional simulations with 
input pressures of 20 and 12 bar and a CVC pressure of 1 bar are per -
formed for comparison. Fig. 6 shows the penetration length and the jet 
spreading angle for all simulations and the experimental results. When 
the full injector geometry is considered, a very good agreement with the 
experimental penetration length is achieved. For the short injector with 
the 20 bar input pressure, an over-prediction of at least 25% at each 
instant is observed for both the penetration length and cone angle. The 
penetration length for the 12 bar case shows a slight over-prediction 
(around 7%) at the beginning of the injection. This is because the 
pressure in the hot valve is still below 12 bar before approximately 300 
μ s ASOI. Once the injector is fully open, the difference between the re -
sults with the full injector and the short version is less than 5% for the 
penetration length. A better agreement between the results of the full 
injector and the short version is observed for the cone angle in this case. 
4.3. Injector internal flow 
Fig. 7 illustrates the pressure and Mach development within the 
injector for different instants during injection for Case 2. At 5 μ s , the gas 
from the cold valve at 20 bar is entering the hot valve at 1 bar . At 90 μ s , 
the Prandtl – Meyer expansion fans can be observed just upstream of the 
Fig. 6. Experimental vs. numerical a) penetration length and b) jet spreading angle for the long and short injector with different rail pressure as labelled, P
CVC 
= 1, T 
= 298 K, methane. 
Fig. 7. Mach and pressure fields within the injector at different instants as 
labelled, Case 2: P
CVC
= 1 bar , T = 298 K. 
1
0.8
0.6
0.01
0.2
0.4
Fig. 8. Instantaneous external flow features for Case 2 during the injection, shown with schlieren imaging (first row) and simulation results using the density 
gradient method (second row). 
M.R. Yosri et al.

<!-- PDF_PAGE: 7 -->

Fuel 290 (2021) 120019
7
hot valve. The total pressure in the hot valve increases to around 6 bar at 
150 μ s . The jet features diamond shape structures due to the reflection of 
compression waves from the walls and a formation of oblique shock 
waves [23] . These structures are present up to the point that the flow 
reaches subsonic conditions. At later times up to 300 μ s , the supersonic 
region in the hot valve increases in length while the total pressure in the 
hot valve increases as well. After that, the boundary between the su -
personic and subsonic regions retreats back as the pressure ratio be -
tween the hot and cold valves decreases. At 350 μ s , this ratio is below 
two, and therefore the shock waves dissipate quickly within the injector. 
As demonstrated in Fig. 6 , neglecting these complex dynamics during 
the injection process can lead to inaccurate results at the early stages of 
injection. 
4.4. Injector external flow 
4.4.1. Comparison with experimental results 
Fig. 8 shows a comparison between schlieren images and the LES 
results using the projected density gradient method (see Section 3.5.1 ) at 
different instants for Case 2. Jet features such as the penetration length 
and cone angle are shown. Qualitatively, the experiments and simula -
tions appear consistent. A region featuring high density gradients with 
shock structures such as Mach disks, shown as vertical lines, are present 
close to the poppet valve. Further downstream much smaller values of 
density gradients are observed. 
Quantitative comparison between experimental and simulation re -
sults is performed using the Mach disk location, the penetration length 
and the cone angle. The Mach disk location, H
disk
, the distance from the 
Mach disk to the nozzle exit, is presented in Table 3 for Cases 1,2 and 4. 
Case 3 with P
CVC
= 3 bar has a lower NPR and is in the moderately 
under-expanded jet regime ( NPR = 3 . 34 < 4 . 05), which does not 
feature a Mach disk. The variable H
disk 
can also be obtained empirically 
from the correlation proposed by Crist et al. [45] : 
H
disk
/
D
eq
= 0 . 67
̅̅̅̅̅̅̅̅̅ ̅
NPR
√
, (20)  
where D
eq 
denotes the equivalent diameter of the annulus flow pathway. 
The difference between H
disk
/ D
eq
obtained from the LES and experi -
mental results is less than 5%. The agreement with the empirical cor -
relation is slightly higher for Case 4 with a higher CVC temperature. 
The results for the jet spreading angle are compared with the 
experimental results in Fig. 9 . The jet spreading angle was measured 500 
μ s ASOI when the jet had a sharp edge. An agreement to within 2% at 
each instant was observed for all cases. 
Fig. 10 shows the comparison between LES, experimental and 
analytical results for the penetration length. An updated version of the 
Table 3 
Location of the Mach Disk.  
Case H
disk
/ D 
Numerical  
H
disk
/ D 
Experiment  
Difference to 
Experiment 
Difference to 
Empirical 
Correlation 
1) P
CVC
= 0.4 
bar T =
298 K  
3.05 3.15 4.12% 2.00% 
2) P
CVC
= 1 
bar T =
298 K  
1.98 2.02 4.01% 2.90% 
4) P
CVC
= 1 
bar T =
360 K  
2.06 2.15 4.87% 8.01%  
Fig. 9. Experimental (circle) vs. numerical jet spreading angle (solid line) for 
case 1 to 4 as labelled. 
Fig. 10. Experiment (red circle with error bars) compare with numerical (black 
solid line) and analytical penetration length (blue solid line) for Case 1 to 4, top 
to bottom. (For interpretation of the references to color in this figure legend, the 
reader is referred to the web version of this article.) 
M.R. Yosri et al.

<!-- PDF_PAGE: 8 -->

Fuel 290 (2021) 120019
8
Hill and Ouellette correlation by Hajialimohammadi et al. was used to 
calculate the analytical penetration length [46,47] . The analytical so -
lution was developed for a single hole injector considering the conser -
vation of momentum, and can be described as: 
Z
t
= Γ D
1
2
eq
[
γ
a
π
4
P
eff
P
a
R
a
T
a
(
2
γ
a
+ 1
)
(
γ
a
γ
a
 1
)
]
1
4
t
1
2
, (21)  
where Z
t 
is penetration length, t denotes time, Γ = 3 and the subscript 
“ a ” corresponds to the ambient chamber pressure [46] . The variable P
eff 
Fig. 11. Numerical jet spreading angle for a) different CVC pressures b) different CVC temperatures as labelled.  
Fig. 12. Jet penetration results of a) numerical at different CVC pressures b) numerical at different CVC temperatures c) analytical at different CVC pressures c) 
analytical at different CVC temperatures labelled. 
M.R. Yosri et al.

<!-- PDF_PAGE: 9 -->

Fuel 290 (2021) 120019
9
is the effective pressure at the nozzle exit, which is less than the fuel rail 
pressure. 
As shown in Fig. 10 , the analytical solution predicts much higher 
penetration at the early stages. This is not surprising given that this 
solution is developed for a fully open single hole injector. While there is 
a good agreement with the experimental results for Cases 2 and 4 with 
chamber pressure of 1 bar , the agreement is not as good for Cases 1 and 3 
at 250 μ s ASOI. 
Several factors contribute to this. For Case 1, with the highest NPR, 
the experimental uncertainty is largest (see Fig. 10 ). Further, the 
simulation results are expected to be more sensitive to the geometrical 
features of the injector and boundary conditions for such a high NPR. 
Therefore, any small discrepancy is expected to have a large impact on 
the results. This is also observed in the level of uncertainty in the 
experimental results. For Case 3, although the bouncing of the valve at 
the early stages of the opening is considered in the simulations, the valve 
lift profile is an ensemble average, and the raw profiles show notable 
fluctuations. 
Fig. 11 shows the simulation results, highlighting the effect of 
changing the CVC pressure and temperature on the jet spreading angle. 
Increasing the chamber pressure from 0.4 to 3 bar changes the time- 
averaged cone angle from 115
◦
to 66
◦
. Increasing the CVC tempera -
ture by about 60 K does not have much impact on the jet spreading 
angle. Increased amplitude of fluctuations are observed for higher NPRs. 
Fig. 12 depicts the effect of changing the chamber pressure and 
temperature on the penetration length using both simulation and 
analytical results. Increasing the chamber pressure from 0.4 to 3 bar , 
changes the penetration length by about 50% at 500 μ s ASOI. Changing 
the fuel and chamber temperature changes the penetration length by 
14% at 500 μ s ASOI. LES results show that the penetration rate results up 
to 800 μ s ASOI have an almost linear dependency with time. Previous 
studies using a similar injector showed that the penetration length has a 
0.8 power-law dependency with time after approximately 500 μ s ASOI 
[17,48] . The constants A
1 
to A
3 
have an inverse relation with CVC 
pressure to the power of 0.25. Eq. (21) also shows that Z
t
∝ 1 / P
0 . 25
CVC
. 
Collectively, the results of Figs. 11 and 12 show that the penetration 
length and the cone angle both have an inverse relationship with the 
chamber pressure, and a direct relationship with temperature, consistent 
with the theoretical argument of Lacey et al. [30] . 
4.4.2. Analysis of the jet development 
Fig. 13 shows the iso-surfaces of Y
CH
4
= 0 . 01 at different instants for 
Case 1. 20 μ s ASOI, a three dimensional toroidal vortex ring initiates at 
the tip of the jet. A toroidal vortex ring was also observed at the initial 
development of the hollow cone jet in Bartolucci et al. [24] . In the 
present study, the vortex ring is not axisymmetric, due to asymmetric 
holes downstream of injector. At later times, as the hollow cone jet in -
creases in size, it collapses into a single jet (250 μ s ASOI). 
Fig. 14 shows the transient development of the hollow-cone jet for 
the under-expanded jet ( P
CVC 
= 1 bar ) in the Y  Z plane. At the start of 
injection, boundary layer separation occurs as the flow passes over the 
poppet valve at the tip of the injector. The annular bow shock is formed 
close to the tip, and initial annular tip vortices at 20 μ s ASOI are 
observed. At later times, as the high-speed methane enters the CVC, the 
jet entrains the quiescent nitrogen, both from inside and outside the 
hollow cone. This causes the development of a low-pressure zone in 
front of the poppet valve. The tip vortices in the inner region grow in 
size, forming large scale eddies, impinging onto the poppet valve. This 
creates a recirculation zone, enhancing methane/nitrogen mixing. At 
120 μ s ASOI, the Mach disk is formed when the poppet valve is partially 
open. The presence of the Mach disk and shock cells region postpones 
mixing. Downstream of these features, viscous forces become dominant 
and the shock cells region disappear [15] . By 350 μ s ASOI, the hollow 
cone jet has collapsed into a single jet. A stagnation zone is formed 
downstream of the recirculation zones, and a far-mixing region is pre -
sent, as seen at 450 μ s ASOI [18] . At this time, the injector is fully open, 
with the far-mixing region featuring subsonic turbulent mixing. 
Fig. 15 shows a comparison between all cases in terms of the mean 
and standard deviation of the methane mass fraction under quasi-steady 
state conditions at the mid Y-Z plane of the jet. Both inner and outer 
mixing layers are formed downstream of the injector tip with their 
thickness increasing up to the point that they merge into a one mixing 
layer. After this point, high fluctuations of Y
CH
4 
are observed, consistent 
with the results presented in [17] . The CVC pressure has an impact on 
Fig. 13. Iso-surface of Y
CH 4
= 0 . 01 at different instants for Case 2.  
M.R. Yosri et al.

<!-- PDF_PAGE: 10 -->

Fuel 290 (2021) 120019
10
the formation and the shape of these mixing layers. By increasing the 
CVC pressure, the mixing layers merge closer to the nozzle exit. This is 
expected because when the CVC pressure is increased, the NPR is 
decreased and consequently, the shock affected region is reduced in size 
[15] . 
To further examine the jet development, Fig. 16 shows the flow 
streamlines and the field of Y
CH
4 
for different cases at t = 600 μ s ASOI 
when the quasi-steady state is reached. While the recirculation zone 
enhances mixing in the inner region, mixing dominantly occurs in the 
outer region for the far-mixing zone. The recirculation zone evidently 
increases in size as the CVC pressure decreases, pushing the far mixing 
zone further downstream. Similar trends were observed by Bartolucci 
et al. where increasing the NPR increased the recirculation zone length 
[24] . 
Considering the stagnation point as the streamwise location on the 
jet axis at the which the streamwise velocity is zero, a recirculation zone 
length ( L
R
) can be obtained. The mean value of L
R 
is reported in Table 4 
showing that the size of the recirculation zone is strongly dependant on 
the CVC pressure. 
Massey et al. developed a scaling law for the recirculation zone 
length behind the bluff body using the equation for the conservation of 
momentum [49] . For a fixed geometry, this scaling can be written as 
follows: 
L
R
∝
U
b
P
, (22)  
where U
b 
is the nozzle exit bulk velocity in the direction normal to the 
bluff body and P is the chamber pressure. For our cases, the nozzle is 
choked and therefore the resulting velocity is constant. Therefore, Eq. 23 
can be rearranged as, 
L
R
∝
cos ( θ / 2 )
P
, (23)  
where θ is the spreading angle. Fig. 17 shows that the scaling has a 
reasonable performance for the cases studied here. Once again, these 
results highlight the impact of the CVC pressure on the external flow 
dynamics. 
5. Conclusions 
Large-eddy simulations (LESs) of methane direct injection into a 
Constant Volume Chamber (CVC) considering the full internal geometry 
of a prototype, hollow-cone injector were performed. Three cases with 
different CVC pressures of 3, 1 and 0.4 bar at 298 K were considered with 
fourth case featuring a gas and CVC temperature of 360 K with a CVC 
pressure of 1 bar . All cases had the same rail pressure of 20 bar . These 
conditions were all relevant to CNG DI engines considering different 
injection strategies. The results were validated against high-speed 
schlieren imaging from Lacey et al. ’ s experimental work [30] using a 
new post-processing concept. The key findings of the study are sum -
marised below.  
1. An excellent agreement between simulation and experimental results 
was achieved for the jet spreading angle.  
2. A varying degree of agreement was observed for the jet penetration 
length. This was attributed to the higher sensitivity of the results to 
the input parameters, modelling assumptions for the highest NPR 
case and the fluctuations of the poppet valve in the lowest NPR case.  
3. A short version of the injector featuring a part of the hot valve was 
simulated. The inlet boundary conditions for the short injector were 
set using the information of the pressure loss obtained from the full 
injector simulation. The results of the short injector simulation 
showed a good agreement with the experimental results. 
Fig. 14. Transient development of the under-expanded jet (Case 2), shown 
using a) methane mass fraction field superimposed with velocity vectors b) 
Mach field and c) pressure field. 
Fig. 15. Mean (Top) and standard deviation (bottom) of the fuel mass fraction 
at the mid Y  Z plane at quasi steady state condition (500 to 2000 μ s ), 
as labelled. 
M.R. Yosri et al.

<!-- PDF_PAGE: 11 -->

Fuel 290 (2021) 120019
11
4. The external flow consisted of three main regions: A “ recirculation ” 
zone where mixing is dominant and is present just downstream of the 
injector tip. This is followed by a “ stagnation zone ” where the axial 
velocity is almost zero. Downstream of this region is a “ far-mixing ” 
zone with a strong mixing occurring outside the jet. This observation 
was consistent with previous studies of under-expanded jets.  
5. The length of the recirculation zone increased as the CVC pressure 
decreased. This could be explained using a theory recently developed 
in the literature for flow behind a bluff body, highlighting the 
importance of the CVC pressure on the jet dynamics. 
CRediT authorship contribution statement 
M.R. Yosri: Conceptualization, Software, Validation, Formal anal -
ysis, Investigation, Data curation, Writing - original draft, Visualization. 
J.Z. Ho: Methodology, Visualization. M. Meulemans: Methodology, 
Visualization. M. Talei: Conceptualization, Funding acquisition, Re -
sources, Supervision, Writing - review & editing. R.L. Gordon: Funding 
acquisition, Resources, Supervision, Writing - review & editing. M.J. 
Brear: Funding acquisition, Resources, Supervision, Writing - review & 
editing. D. Cosby: Resources. J.S. Lacey: Investigation, Writing - review 
& editing. 
Declaration of Competing Interest 
The authors declare that they have no known competing financial 
interests or personal relationships that could have appeared to influence 
the work reported in this paper. 
Fig. 16. Stream plot of the velocity vector field for different cases superimposed on the mass fraction field, 500 μ s ASOI, as labelled.  
Table 4 
Size of re-circulation zone ( L
R
) for different cases.  
No. CVC pressure 
( bar ) 
Temperature 
(K) 
Mean size of the re-circulation zone 
L
R 
(mm)  
1 0.4 298 18.39 
2 1 298 12.23 
3 3 298 6.94 
4 1 360 12.33  
Fig. 17. Variation of L
R 
for different cases, markers are LES results and the 
trend-line as labelled. 
M.R. Yosri et al.

<!-- PDF_PAGE: 12 -->

Fuel 290 (2021) 120019
12
Acknowledgement 
This research was supported by the Australian Research Council 
(ARC) [LP160100339] and the Ford Motor Company. Mohsen Talei also 
acknowledges the support of the ARC through the DECRA Fellowship 
(DE180100416). We also would like to thank Continental for providing 
the prototype DI CNG injector hardware. 
References 
[1] Engerer H, Horn M. Natural gas vehicles: an option for Europe. Energy Policy 2010; 
38(2):1017 – 29. https://doi.org/10.1016/j.enpol.2009.10.054 . 
[2] Semin R, Bakar A. A Technical review of compressed natural gas as an alternative 
fuel for internal combustion engines; 2008. doi: 10.3844/ajeassp.2008.302.311. 
[3] Khan MI, Yasmin T, Shakoor A. Technical overview of Compressed Natural Gas 
(CNG) as a transportation fuel. Renew Sustain Energy Rev 2015;51:785 – 97. 
https://doi.org/10.1016/j.rser.2015.06.053 . 
[4] Kosmadakis G, Rakopoulos D, Rakopoulos C. Performance and emissions of a 
methane-fueled spark-ignition engine under consideration of its cyclic variability 
by using a computational fluid dynamics code. Fuel 2019;258:116 – 54. https://doi. 
org/10.1016/j.fuel.2019.116154 . 
[5] Wallner T, Pamminger M, Scarcelli R, Powell C, Simeu SK, Wooldridge S, Boyer B, 
Iqbal A, Reese R. Performance, fuel economy, and economic assessment of a 
combustion concept employing in-cylinder gasoline/natural gas blending for light- 
duty vehicle applications. United States: N. p., 2019. doi:10.4271/03-12-03-0019. 
[6] Singh AP, Pal A, Agarwal AK. Comparative particulate characteristics of hydrogen, 
CNG, HCNG, gasoline and diesel fueled engines. Fuel 2016;185:491 – 9. https://doi. 
org/10.1016/j.fuel.2016.08.018 . 
[7] Ferrera M. Highly efficient natural gas engines. In: 13th International conference 
on engines and vehicles, SAE International, Paper No. 2017 – 04-0059; 2017. doi: 
10.4271/2017-24-0059. 
[8] Erfan I, Chitsaz I, Ziabasharhagh M, Hajialimohammadi A, Fleck B. Injection 
characteristics of gaseous jet injected by a single-hole nozzle direct injector. Fuel 
2015;160:24 – 34. https://doi.org/10.1016/j.fuel.2015.07.037 . 
[9] Erfan I, Hajialimohammadi A, Chitsaz I, Ziabasharhagh M, Martinuzzi RJ. 
Influence of chamber pressure on CNG jet characteristics of a multi-hole high 
pressure injector. Fuel 2017;197:186 – 93. https://doi.org/10.1016/j. 
fuel.2017.02.018 . 
[10] Song J, Choi M, Kim D, Park S. Combustion characteristics of methane direct 
injection engine under various injection timings and injection pressures. J Eng Gas 
Turb Power 2017;139(8). https://doi.org/10.1115/1.4035817 . 
[11] Bartolucci L, Scarcelli R, Wallner T, Swantek A, Powell CF, Kastengren A, Duke D. 
CFD and x-ray analysis of gaseous direct injection from an outward opening 
injector. In: SAE 2016 World Congress and Exhibition, SAE International, Paper 
No. 2016-01-0850; 2016. doi:10.4271/2016-01-0850. 
[12] Hall J, Hibberd B, Streng S, Bassett M. Compressed-natural-gas optimised 
downsized demonstrator engine. Proc Inst Mech Eng Part D J Autom Eng 2018;232 
(1):75 – 89. https://doi.org/10.1177/0954407017707552 . 
[13] Choi M, Lee S, Park S. Numerical and experimental study of gaseous fuel injection 
for CNG direct injection. Fuel 2015;140:693 – 700. https://doi.org/10.1016/j. 
fuel.2014.10.018 . 
[14] Donaldson RS, Snedeker C. A study of free jet impingement. Part 1. Mean 
properties of free and impinging jets. J Fluid Mech 1971;45(2)281 – 319. doi: 
10.1017/S0022112071000053. 
[15] Hamzehloo A, Aleiferis P. Large eddy simulation of highly turbulent under- 
expanded hydrogen and methane jets for gaseous-fuelled internal combustion 
engines. Int J Hydrogen Energy 2014;39(36):21275 – 96. https://doi.org/10.1016/ 
j.ijhydene.2014.10.016 . 
[16] Husted HL, Karl G, Schilling S, Weber C. Direct Injection of CNG for Driving 
performance with Low CO
2
. In: 23rd Aachen colloquium automobile and engine 
technology, Aachen; 2014. p. 829 – 50. 
[17] Deshmukh AY, Bode M, Falkenstein T, Khosravi M, van Bebber D, Klaas M, 
Schr ¨oder W, Pitsch H. Simulation and modeling of direct gas injection through 
poppet-type outwardly-opening injectors in internal combustion engines. Springer 
Singapore, Singapore 2019:65 – 115. https://doi.org/10.1007/978-981-13-3307-1_ 
4 . 
[18] Swantek AB, Duke DJ, Kastengren AL, Sovis N, Powell CF, Bartolucci L, Scarcelli R, 
Waller T. An experimental investigation of gas fuel injection with X-ray 
radiography. Exp Therm Fluid Sci 2017;87:15 – 29. https://doi.org/10.1016/j. 
expthermflusci.2017.04.016 . 
[19] Keskinen K, Kaario O, Nuutinen M, Vuorinen V, Künsch Z, Liavåg LO, Larmi M. 
Mixture formation in a direct injection gas engine: numerical study on nozzle type, 
injection pressure and injection timing effects. Energy 2016;94(Suppl. C):542 – 56. 
https://doi.org/10.1016/j.energy.2015.09.121 . 
[20] Vuorinen V, Yu J, Tirunagari S, Kaario O, Larmi M, Duwig C, Boersma BJ. Large- 
eddy simulation of highly underexpanded transient gas jets. Phys Fluids 2013;25 
(1):1 – 22. https://doi.org/10.1063/1.4772192 . 
[21] Vuorinen V, Wehrfritz A, Duwig C, Boersma BJ. Large-eddy simulation on the 
effect of injection pressure and density on fuel jet mixing in gas engines. Fuel 2014; 
130:241 – 50 . 
[22] Hamzehloo A, Aleiferis P. Computational study of hydrogen direct injection for 
internal combustion engines. SAE International, Paper No. 2013-01-2524; 2013. 
doi:10.4271/2013-01-2524. 
[23] Hamzehloo A, Aleiferis PG. Numerical modelling of transient under-expanded jets 
under different ambient thermodynamic conditions with adaptive mesh 
refinement. Int J Heat Fluid Flow 2016;61(Part B):711 – 29. https://doi.org/ 
10.1016/j.ijheatfluidflow.2016.07.015 . 
[24] Bartolucci L, Cordiner S, Mulone V, Scarcelli R, Wallner T, Swantek AB, Powell CF, 
Kastengren AL. Gaseous jet through an outward opening injector: Details of mixing 
characteristic and turbulence scales. Int J Heat Fluid Flow 2020;85:108660. 
https://doi.org/10.1016/j.ijheatfluidflow.2020.108660 . 
[25] Baratta M, Catania AE, Pesce FC. CNG injector nozzle design and flow prediction. 
In: ASME internal combustion engine division fall technical conference; 2010. 
p. 795 – 800. https://doi.org/10.1115/ICEF2010-35104 . 
[26] Baratta M, Catania AE, Pesce FC. Multidimensional modelling of natural gas jet and 
mixture formation in direct injection spark ignition engines – development and 
validation of a virtual injector model. J Fluids Eng 2011;133(4):41304 – 14. https:// 
doi.org/10.1115/1.4003877 . 
[27] Baratta M, Rapetto N. Mixture formation analysis in a direct-injection NG SI engine 
under different injection timings. Fuel 2015;159:675 – 88. https://doi.org/ 
10.1016/j.fuel.2015.07.027 . 
[28] Deshmukh AY, Vishwanathan G, Bode M, Pitsch H, Khosravi M, van Bebber D. 
Characterization of hollow cone gas jets in the context of direct gas injection in 
internal combustion engines. In: WCX world congress experience, SAE 
International, Paper No. 2018-01-0296; 2018. doi:10.4271/2018-01-0296. 
[29] Deshmukh AY, Falkenstein T, Pitsch H, Khosravi M, van Bebber D, Klaas M, 
Schroeder W. Numerical investigation of direct gas injection in an optical internal 
combustion engine. In: WCX world congress experience, SAE International, Paper 
No. 2018-01-0171; 2018. doi:10.4271/2018-01-0171. 
[30] Lacey J, Meulemans M, Poursadegh F, Brear M, Petersen P, Kramer U, Smith A, 
Hornby M, Cosby D, Czimmek P. An optical and numerical characterization of 
directly injected compressed natural gas jet development at engine-relevant 
conditions. In: WCX SAE world congress experience, SAE International, Paper No. 
2019-01-0294; 2019. doi:10.4271/2019-01-0294. 
[31] Hornby M, Husslein K, Schüle H, Heukenroth C, Klemp W, Komischke T, Gerlach T. 
Gas direct injector with reduced leakage. USA Patent No. US9453486B1; 2015. 
[32] Lacey J, Poursadegh F, Brear MJ, Gordon R, Petersen P, Lakey C, Butcher B, 
Ryan S. Generalizing the behavior of flash-boiling, plume interaction and spray 
collapse for multi-hole, direct injection. Fuel 2017;200:345 – 56. https://doi.org/ 
10.1016/j.fuel.2017.03.057 . 
[33] Poursadegh F, Lacey JS, Brear MJ, Gordon RL. On the fuel spray transition to dense 
fluid mixing at reciprocating engine conditions. Energy Fuels 2017;31(6):6445 – 54. 
https://doi.org/10.1021/acs.energyfuels.7b00050 . 
[34] Poursadegh F, Lacey JS, Brear MJ, Gordon RL, Petersen P, Lakey C, Butcher B, 
Ryan S, Kramer U. On the phase and structural variability of directly injected 
propane at spark ignition engine conditions. Fuel 2018;222:294 – 306. https://doi. 
org/10.1016/j.fuel.2018.02.137 . 
[35] Poursadegh F, Lacey J, Brear M, Gordon R. The direct transition of fuel sprays to 
the dense-fluid mixing regime in the context of modern compression ignition 
engines. In: WCX world congress experience, SAE International, Paper No. 2018- 
01-0298; 2018. doi:10.4271/2018-01-0298. 
[36] Richardson KJ, Senecal P, Pomraning E. Converge 2.4, Convergent Science, 
Madison, WI; 2017. 
[37] Issa RI, Gosman AD, Watkins AP. The computation of compressible and 
incompressible recirculating flows by a non-iterative implicit scheme. J Comput 
Phys 1986;62(1):66 – 82. https://doi.org/10.1016/0021-9991(86)90100-2 . 
[38] Pomraning E, Rutland CJ. Dynamic one-equation nonviscosity large-eddy 
simulation model. AIAA J 2002;40(4):689 – 701. https://doi.org/10.2514/2.1701 . 
[39] Akira Y, Kiyosi H. A statistically-derived subgrid-scale kinetic energy model for the 
large-eddy simulation of turbulent flows. J Phys Soc Jpn 1985;54(8):2834 – 9. 
https://doi.org/10.1143/JPSJ.54.2834 . 
[40] Germano M, Piomelli U, Moin P, Cabot WH. A dynamic subgrid-scale eddy 
viscosity model. Phys Fluids A Fluid Dyn 1991;3(7):1760 – 5. https://doi.org/ 
10.1063/1.857955 . 
[41] Gad-el Hak M. The fluid mechanics of microdevices-The freeman scholar lecture. 
J Fluids Eng 1999;121(1):5 – 33. https://doi.org/10.1115/1.2822013 . 
[42] Settles GS. Schlieren and shadowgraph techniques. Springer, Berlin, Heidelberg; 
2001. doi:10.1007/978-3-642-56640-0. 
[43] Seidel R. The upper bound theorem for polytopes: an easy proof of its asymptotic 
version. Comput Geom 1995;5(2):115 – 6. https://doi.org/10.1016/0925-7721(95) 
00013-Y . 
[44] Lumley JL. Engines: an introduction. Cambridge University Press; 1999. URL: 
https://books.google.com.au/books?id = it1BggypJ2oC . 
[45] Crist S, Glass DR, Sherman PM. Study of the highly underexpanded sonic jet. Am 
Inst Aeronaut Astronaut 1966;4(1):68 – 71. https://doi.org/10.2514/3.3386 . 
[46] Hill PG, Ouellette P. Transient turbulent gaseous fuel jets for diesel engines. 
J Fluids Eng 1999;121(1):93 – 101. https://doi.org/10.1115/1.2822018 . 
[47] Hajialimohammadi A, Edgington-Mitchell D, Honnery D, Montazerin N, 
Abdullah A, Agha Mirsalim M. Ultra high speed investigation of gaseous jet 
injected by a single-hole injector and proposing of an analytical method for 
pressure loss prediction during transient injection. Fuel 2016;184:100 – 9. https:// 
doi.org/10.1016/j.fuel.2016.06.112 . 
[48] Kuensch ZA, Schlatter S, Keskinen K, Hulkkonen T, Larmi M, Boulouchos K. 
Experimental investigation on the gas jet behavior for a hollow cone piezoelectric 
injector. SAE International, Paper No. 2014-01-2749; 2014. doi:10.4271/2014-01- 
2749. 
[49] Massey JC, Langella I, Swaminathan N. A scaling law for the recirculation zone 
length behind a bluff body in reacting flows. J Fluid Mech 2019;875:699 – 724. 
https://doi.org/10.1017/jfm.2019.475 . 
M.R. Yosri et al.
