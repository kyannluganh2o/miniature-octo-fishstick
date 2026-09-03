<!-- PDF_PAGE: 1 -->

Available online at www.sciencedirect.com 
Proceedings of the Combustion Institute 36 (2017) 2417–2424 
www.elsevier.com/locate/proci 
Simulation of drop deformation and breakup in 
supersonic flow 
F. Xiao ∗, Z.G. Wang , M.B. Sun ∗, N. Liu , X. Yang 
Science and Technology on Scramjet Laboratory, National University of Defense Technology, Changsha 410073, China 
Received 4 December 2015; accepted 9 September 2016 
Available online 13 October 2016 
Abstract 
The deformation and breakup process of a liquid drop in supersonic flow is numerically studied with 
a coupled Level Set and Volume of Fluid method as the interface tracking approach. The Navier–Stokes 
equation s in the liquid phase are solved by an incompressible flow solver using a finite volume method, and 
the governing equations in the gas phase are solved by a compressible flow solver using a finite difference 
method. Proper boundary conditions are specified at the interface for both liquid and gas flow solvers in order 
to correctly capture the interaction between the liquid and gas flows. It is demonstrated that the simulation 
cost can be significantly reduced by reducing liquid/gas density ratio while keeping the same Weber number 
and Ohnesorge number. Drop breakup at different Weber numbers is simulated. Bag breakup, bag stamen 
breakup, and multimode breakup modes are reproduced by the present two-phase flow solver. The physical 
mechanism for drop breakup in supersonic flow is investigated, and Rayleigh–Taylor instability is found to 
determine the breakup morphology for the studied Weber number range. 
© 2016 The Combustion Institute. Published by Elsevier Inc. All rights reserved. 
Keywords: Drop deformation; Drop breakup; Supersonic flow; Interface tracking; Rayleigh–Taylor instability 
1. Introduction 
In order to achieve high combustion perfor- 
mance in a supersonic combustion ramjet (Scram- 
jet) engine, the liquid fuel must mix well with the 
supersonic air flow. The understanding of the at- 
omization process in a supersonic flow is required 
to design a superior fuel injection scheme. Compu- 
tational Fluid Dynamics (CFD) in two-phase flow 
has made significant progress and furthered our un- 
derstanding of the atomization mechanism [1–7] . 
∗ Corresponding authors. 
E-mail addresses: xiaof03@aliyun.com (F. Xiao), 
wind_flowcfd@163.com (M.B. Sun). 
As the liquid fuel is injected into the supersonic air 
flow, the liquid jet first undergoes primary breakup, 
producing both small and large drops, and then 
the large drops further undergo secondary breakup 
in the downstream, producing ever smaller drops. 
For primary breakup, the liquid jet disintegration 
process can be directly resolved using an inter- 
face tracking method [1] . For secondary breakup, 
a lot of work has been done to develop models 
for secondary atomization [8] . However, no single 
model can describe all aspects of secondary atom- 
ization accurately [8] . Interface tracking methods 
have been used in [9–15] to directly resolve the drop 
deformation and breakup process to elucidate the 
physical mechanism, which may help improve the 
models of secondary atomization. 
http://dx.doi.org/10.1016/j.proci.2016.09.016 
1540-7489 © 2016 The Combustion Institute. Published by Elsevier Inc. All rights reserved.

<!-- PDF_PAGE: 2 -->

2418 F. Xiao et al. / Proceedings of the Combustion Institute 36 (2017) 2417–2424 
All the simulations in [9–15] are for a drop in 
the subsonic flow, and both liquid and gas phases 
are assumed to be incompressible. For a drop in the 
supersonic air flows as in a Scramjet engine, two ap- 
proaches can be used: the first approach is to treat 
both liquid and gas phases as compressible flows 
[16–20] ; the second is to treat the liquid phase as 
incompressible and the gas phase as compressible 
[21] . Since the sound speed is much higher in the 
liquid than in the gas, the constraint of the CFL 
condition requests the time step to be very small in 
the first approach, resulting in high computational 
cost. Simulations of drop breakup in [16–20] are 
carried out in two-dimensional or axisymmetric co- 
ordinates. Furthermore, the equation of state is sig- 
nificantly different between gas and liquid, which 
may induce oscillations in numerical solutions near 
the interface. In order to avoid these two problems, 
the second approach is applied here to simulate the 
drop breakup in the supersonic flow. Furthermore, 
the total pressure in the combustor of a SCRAM- 
JET engine is several MPa, and the corresponding 
compressibility of the liquid fuel (e.g., kerosene) 
is in the order of 0.1%. Therefore, it is appropri- 
ate to assume that the liquid is incompressible. The 
method in [21] solves Euler equations by neglect- 
ing the effect of viscosity, and the tangential veloc- 
ities are assumed to be discontinuous across the in- 
terface, resulting in considerable errors in the shear 
stress on the drop. In order to resolve well the shear 
forces acting on the interface, the effects of viscos- 
ity are taken into account, and the Navier–Stokes 
equations are solved in the current methodology. 
In this study, the deformation and breakup mor- 
phology of liquid drop in supersonic flow at dif- 
ferent Weber numbers is numerically investigated. 
The difference between the drop breakup in super- 
sonic and subsonic flows is examined. The paper is 
to provide physical insight on the drop breakup in 
supersonic flow with some characteristic quantities, 
which can be useful in building secondary atomiza- 
tion models in supersonic flow. 
2. Numerical methods 
In the present formulation, the interface is 
tracked using the CLSVOF method where two 
functions are used to represent the interface. VOF 
function F is defined as the volume fraction of 
liquid in a cell. Level set (LS) function φis defined 
as the signed distance from the interface, with the 
contour φ = 0 representing the interface, φ>  0 
in the liquid, and φ< 0 in the gas. The CLSVOF 
algorithm is detailed in [13] . The usual spatially 
filtered LES formulation is employed in the single- 
phase flow regions. The governing equations for 
the incompressible liquid phase and compressible 
gas phase are detailed in [13] and [22] respectively. 
The governing equations are solved on a Carte- 
sian grid, with the gas flow calculated by a finite 
Fig. 1. Variable arrangement. Green-shaded region is 
pressure control volume (CV); grey-shaded region is x - 
momentum CV; yellow-shaded region is y -momentum 
CV. 
difference method and the liquid flow by a finite 
volume method. For simplicity, the numerical 
methods are described on a two-dimensional grid 
for illustration; extension to 3D is straightforward. 
The arrangement of flow variables on the grid is 
demonstrated in Fig. 1 . The variables solved by the 
liquid flow solver (liquid variables) are arranged 
in a staggered manner: pressure p is located at 
cell centres; velocity components u ( u L ) and v 
( v L ) are located at the corresponding cell faces. 
The variables solved by the gas flow solver (gas 
variables: pressure P , velocity components U and 
V , temperature T , and density ρ) are all located at 
cell corners. LS function φ and VOF function F 
are located at cell centres. 
2.1. Numerical methods for the gas flow solver 
The supersonic gas flow is solved by the LES 
code developed by Sun et al. [22,23] . A second 
order TVD (total-variation-diminishing) Runge–
Kutta method proposed by Shu [24] is used for 
temporal discretization of the compressible flow 
governing equation. A fifth-order WENO scheme 
developed by Jiang and Shu [25] is used here 
for spatial discretization of inviscid fluxes. A 
second-order central difference scheme is applied 
to discretize the viscous terms. 
In order to solve the gas flow, boundary condi- 
tions should be specified at the interface. This can 
be achieved by specifying gas variables in the liquid 
region. The velocity in the liquid region ( φi + 1/2, j −1/2 
> 0) is given by the liquid velocity field constructed 
in the liquid flow solver: 
U i+1 / 2 ,j−1 / 2 = 
u L 
i+1 / 2 ,j−1 /Delta1y j + u L 
i+1 / 2 ,j /Delta1y j−1 
/Delta1y j + /Delta1y j−1 
(1) 
V i+1 / 2 ,j−1 / 2 = 
v L 
i+1 ,j−1 / 2 /Delta1x i + v L 
i,j−1 / 2 /Delta1x i+1 
/Delta1x i + /Delta1x i+1 
(2) 
Eqs. (1) and (2) are interpolation of cell face val- 
ues to cell corners, and the operation is done for all

<!-- PDF_PAGE: 3 -->

F. Xiao et al. / Proceedings of the Combustion Institute 36 (2017) 2417–2424 2419 
cell corners in the liquid region. The extension of 
the interpolation operation to 3D is given below by 
taking Eq. (1) for example: 
U i+1 / 2 ,j−1 / 2 ,k−1 / 2 = 
u L 
i+1 / 2 ,j−1 ,k−1 /Delta1y j /Delta1z k + u L 
i+1 / 2 ,j,k−1 /Delta1y j−1 /Delta1z k + u L 
i+1 / 2 ,j−1 ,k /Delta1y j /Delta1z k−1 + u L 
i+1 / 2 ,j,k /Delta1y j−1 /Delta1z k−1 
(
/Delta1y j + /Delta1y j−1 
)
( /Delta1z k + /Delta1z k−1 ) 
(3) 
The pressure P in the liquid region is calculated 
by a linear extrapolation from the gas to the liquid 
along the interface normal [14,26] . 
2.2. Numerical methods for the liquid flow solver 
A first order forward-Euler projection method 
was used for temporal discretization of the liq- 
uid flow governing equations [7,14] . In order to 
numerically reproduce the pressure discontinuity 
across the interface arising from the surface ten- 
sion, Ghost Fluid Method [26,27] is used. 
Boundary conditions should be provided for the 
liquid flow, which can be achieved by specifying liq- 
uid variables in the gas region. In order to solve 
the pressure Poisson equation in the liquid region, 
the pressure in the neighbouring gas cell must be 
given: 
if φi,j < 0 , 
p i,j = 
∑ i+1 
m = i 
∑ j+1 
n = j P m −1 / 2 ,n −1 / 2 /Theta1
(
φm −1 / 2 ,n −1 / 2 
)
∑ i+1 
m = i 
∑ j+1 
n = j /Theta1
(
φm −1 / 2 ,n −1 / 2 
)
/Theta1(φ) = 
{ 
1 if φ ≤ 0 
0 if φ> 0 
(4) 
φi−1 / 2 ,j−1 / 2 = 
φi−1 ,j−1 /Delta1x i /Delta1y j + φi,j−1 /Delta1x i−1 /Delta1y j + φi−1 ,j /Delta1x i /Delta1y j−1 + φi,j /Delta1x i−1 /Delta1y j−1 
(/Delta1x i−1 + /Delta1x i )(/Delta1y j−1 + /Delta1y j ) 
(5) 
Equation (4) is interpolation of pressure from 
cell corners to cell centre, and is done for all cell 
centres in the gas region. Equation (5) is used to 
calculate the LS value at every cell corner by inter- 
polation of cell centre LS values. 
Note that the pressure in the gas has physical 
meaning. Since the pressure at the gas cell centres 
adjacent to the interface is specified as in Eq. (4) , 
the Dirichlet boundary condition is enforced when 
solving the pressure Poisson equation in the liq- 
uid region. Therefore, the pressure resolved in the 
liquid reproduces its physical value in some sense. 
In the Ghost Fluid Method, the surface tension 
on the interface is incorporated in the discretiza- 
tion of pressure gradient (( p i −[ p ] −p i −1 )/ δx , [ p ] is 
the pressure jump across the interface due to sur- 
face tension, (see [13,14] for more details) where 
one (e.g., p i −1 ) is at the gas cell centre adjacent to 
the interface and the other (e.g., p i ) is in the liquid. 
Since the pressure boundary condition is specified 
at the gas cell centres adjacent to the interface, the 
pressure jump due to the surface tension can be 
captured when solving the pressure Poisson equa- 
tion in the liquid. 
In order to calculate the shear stress on the in- 
terface exerted by the gas flow, the velocity in the 
adjacent gas momentum control volumes should be 
specified for the liquid flow solver: 
if φi−1 / 2 ,j < 0 , u i−1 / 2 ,j = 
U i−1 / 2 ,j−1 / 2 + U i−1 / 2 ,j+1 / 2 
2 
(6) 
if φi,j+1 / 2 < 0 , v i,j+1 / 2 = 
V i−1 / 2 ,j+1 / 2 + V i+1 / 2 ,j+1 / 2 
2 
(7) 
Equations (6) and (7) are used to compute veloc- 
ity at the cell faces in the gas region by interpolation 
of cell corner values. 
After the pressure and velocity components are 
specified in the gas region, the incompressible flow 
solver developed in [13,14] can be used to compute 
the liquid flow. 
2.3. Solution algorithm 
The solution algorithm for one time step is de- 
scribed as follows: 
(a) Provide boundary conditions for the gas flow 
at the interface by specifying the gas variables 
in the liquid region. 
(b) Solve the gas flow to next time step. 
(c) Provide boundary conditions for the liquid 
flow. 
(d) Compute the liquid flow to next time step. 
(e) Construct the liquid velocity field u L 
i using an 
extrapolation technique [13] . 
(f) Advect the LS and VOF functions using u L 
i to 
next time step by the CLSVOF method. (N.B. 
The VOF field can inherently conserve the 
liquid mass enclosed by the captured inter- 
face, and the level set field is adjusted basing 
on the VOF to satisfy the liquid mass conser- 
vation. The interface position captured by 
the level set and VOF determines the region

<!-- PDF_PAGE: 4 -->

2420 F. Xiao et al. / Proceedings of the Combustion Institute 36 (2017) 2417–2424 
solved by the incompressible/compressible 
solver at the next time step.) 
3. Results and discussions 
3.1. The effect of liquid/gas density ratio 
The test case from [28,29] is simulated here. The 
diameter D of tributylphosphate (TBP) drop is 3.6 
mm. The density and viscosity of TBP are ρL = 
978 kg/m 3 and μL = 4 ×10 −3 Pa ·s . The tempera- 
ture and pressure of the freestream air flow are T ∞  
= 107 K and P ∞  = 45 Pa, with a low air density of 
ρ∞  = 0.001464 kg/m 3 . The freestream air velocity 
U ∞  is 622 m/s, with a Mach number ( Ma = U ∞  / a, a 
is the sound speed in air) of 3. The surface tension 
coefficient σ is 0.0273 N/m. Thus, the Weber num- 
ber ( W e = ρ∞  U 2 
∞  D/σ) is 75, and the Ohnesorge 
number ( Oh = μL /( ρL σD ) 1/2 ) is 0.013. 
A characteristic time scale is defined as t C = 
( ρL / ρ∞  ) 1 / 2 D/ U ∞  ; the dimensionless time is thus 
defined as t ∗= t / t C . The time step is constrained 
by the CFL (Courant–Friedrichs–Lewy) number. 
Assuming that a uniform mesh with a cell size 
of D / N is used, the time step is /Delta1t = αD / U ∞  , 
α= CFL /[ N (1 + 3/ Ma )] (which is derived from: 
CFL = ( U ∞  + a ) /Delta1t / /Delta1x + a /Delta1t / /Delta1y + a /Delta1t / /Delta1z for the 
initial flow, /Delta1x = /Delta1y = /Delta1z = D/N , Ma = U ∞  /a ). 
Therefore, the required time steps for one simula- 
tion are in the order of t C / /Delta1t = ( ρL / ρ∞  ) 1/2 / α. It is 
attractive to reduce the liquid/gas density ratio in 
order to reduce the computational cost. Two simu- 
lations are run to investigate the effect of reducing 
the liquid/gas density ratio while keeping the same 
We and Oh . The first is to use the above flow con- 
ditions and parameters, resulting in a density ratio 
of 667577. In the second, the freestream gas pres- 
sure and density increase by 36 times, resulting in 
ρ∞  = 0.05274 kg/m 3 and a density ratio of 18544; 
the drop diameter is reduced to 0.1 mm to pro- 
duce the same Weber number; the liquid viscosity 
is reduced to 0.6667 ×10 −3 Pa to recover the same 
Oh . Since the freestream gas velocity U ∞  , tempera- 
ture T ∞  , and thus viscosity μG according to Suther- 
land’s law are the same in the two simulations, the 
Reynolds number ( Re = ρ∞  U ∞  D / μG ) is the same. 
The simulation domain size is [0, 10 D ] ×[ −4 D , 
4 D ] ×[ −4 D , 4 D ] in x, y , and z directions re- 
spectively. The centre of the initially static drop 
was located at the position (2 D , 0, 0). In order 
to resolve well the drop deformation and breakup 
process, a uniform mesh was used in the region 
[0, 5 D ] ×[ −D , D ] ×[ −D , D ] with a cell size of 
0.033 D . In other regions, a coarser mesh was used 
to reduce the computational cost. The domain and 
mesh nondimensionalized by D is the same in the 
two simulations. The initial flow condition is spec- 
ified as follows: in the gas region, the velocity, 
pressure, and density are set to be those of the 
freestream gas flow; in the liquid region, the veloc- 
Fig. 2. Deformed drop predicted by simulations with dif- 
ferent density ratios at t ∗=0.97. (The initial drop is also 
plotted. Results are nondimensionalized by D ). 
Fig. 3. Predicted deformed drop on two meshes at 
t ∗=0.78. 
ity is set to be 0, and the pressure is set to be that of 
the freestream gas flow. CFL number is 0.4 in both 
simulations. The first simulation runs 120,000 time 
steps, the second runs 20,000 time steps, and both 
simulations produce the deformed drop at t ∗= 0.97 
shown in Fig. 2 . The position and shape of the 
deformed drop predicted by the two simulations 
nearly collapsed, with a cross-stream diameter dif- 
ference of 0.1%. Therefore, the freestream gas den- 
sity 0.05274 kg/m 3 and the drop diameter 0.1 mm 
are used in all following simulations, which can pro- 
duce nearly the same results and significantly re- 
duce the computational time by six times. 
3.2. Resolution study and preliminary validation 
For resolution study, one more simulation is 
run on a fine mesh. For the fine mesh, the simula- 
tion domain size is [0, 18 D ] ×[ −4 D , 4 D ] ×[ −4 D , 
4 D ]. A uniform mesh was used in the region [0, 
8.25 D ] ×[ −1.2 D , 1.2 D ] ×[ −1.2 D , 1.2 D ] with a 
cell size of 0.025 D . Figure 3 shows the predicted 
deformed drop at t ∗= 0.78. The morphology of the 
deformed drop obtained on the fine mesh is anal- 
ogous to that on the coarse mesh, with the cross- 
stream diameter slightly larger (by 2.5%) than on

<!-- PDF_PAGE: 5 -->

F. Xiao et al. / Proceedings of the Combustion Institute 36 (2017) 2417–2424 2421 
Fig. 4. Shock standoff distance at different Ma in the 
early stage. 
Fig. 5. Drop morphology at t ∗=0.48, 0.97, 1.45, 1.70, 
1.94, 2.42, 2.67 for We = 19.5, Ma = 3 (the initial drop is 
represented by the circle). 
the coarse mesh. This indicates that the simulation 
on the fine mesh could present meaningful results. 
Figure 4 demonstrates that the shock standoff 
distance in the early simulation stage when the drop 
is still spherical is well captured at different Ma 
numbers in comparison with the experimental mea- 
surements [35] . This implies that the boundary con- 
ditions specified at the interface are appropriate. 
3.3. Drop breakup at different We 
Ten simulations with We of 15, 16, 17, 19.5, 24, 
28, 40, 50, 60, 75 are run to study the effect of We 
on the drop breakup morphology. The flow condi- 
tions and parameters for the We = 75 test case are 
the same as the second simulation in Subsection 
3.1 . For the cases with We = 15, 16, 17, 19.5, 24, 
28, 40, 50, 60, the surface tension coefficients are 
respectively increased to 0.136, 0.128, 0.12, 0.105, 
0.0853, 0.0731, 0.0512, 0.041, 0.0341 N/m; liquid 
viscosity is increased correspondingly to keep the 
same Oh as the We = 75 test case. All simulations 
are run on the fine mesh on 48 CPU cores for 80 
h ours to obtain the results up to t ∗= 2.9. The CFL 
number is 0.4 with the corresponding time step 
/Delta1t = 5 ×10 −3 D / U ∞  . Figures 5 –7 demonstrate the 
predicted drop deformation and breakup process 
for We = 19.5, 28, 75. A bag breakup mode is 
observed in the simulation with the We of 19.5. At 
Fig. 6. Drop morphology at t ∗=0.44, 0.92, 1.4, 1.70, 
1.89, 2.37 for We = 28, Ma = 3 (top: front view, bottom: 
oblique view by an angle of 30 °, experimental photo from 
[30] ). 
Fig. 7. Drop morphology at t ∗=0.48, 0.97, 1.21, 1.45, 
1.70, 1.94, 2.42 for We = 75, Ma = 3 (experimental photos 
from [29] ). 
the higher We of 28, a bag-stamen breakup mode 
is reproduced. From the oblique view by an angle 
of 30 °as shownin Fig.6 , itcan beclearly observed 
that a small liquid stamen forms in the centre of 
the bag and the stamen is located in the down- 
stream of the bag rim as in the experiment. As 
We grows to 75, the simulated droplet undergoes 
multimode breakup: the drop deformation process 
up to t ∗= 0.97 agrees well with the experimental 
observations in [29] , and then a wave of liquid 
sheet form at the periphery of the liquid disk. The 
liquid sheet then bends downstream and disinte- 
grates into tiny ligaments and droplets, which is 
underresolved in the current simulation. 
In summary, a pure drop deformation mode 
is predicted by current LES for We = 15; a bag 
breakup mode for We = 16, 17, 19.5, 24; a bag- 
stamen breakup mode for We = 28, 40; a multi- 
mode breakup mode for We = 50, 60, 75. Table 1 . 
compares the We number ranges for different 
breakup modes in subsonic and supersonic flows. 
In subsonic flows, the correct breakup modes were 
well reproduced by LES at corresponding We in 
comparison with experiments. LES of drop in su- 
personic flows demonstrates that the critical We 
number between different breakup modes is signifi- 
cantly higher than that in subsonic flow. This is con- 
sistent with the experimental observation [28] that

<!-- PDF_PAGE: 6 -->

2422 F. Xiao et al. / Proceedings of the Combustion Institute 36 (2017) 2417–2424 
Table 1 
Drop breakup regimes ( Oh < 0.1). 
Breakup mode Deformation Bag Bag-stamen Multimode 
Subsonic expt. [31] We < 12 12 < We < 16 16 < We < 28 28 < We < 80 
Subsonic LES [36] 3.4, 11.5 12.5, 13.5 22, 25 50 
Supersonic LES We ≤ 15 16 ≤We ≤ 24 28 ≤We ≤ 40 40 ≤We ≤ 75 
Fig. 8. Initiation time versus We in subsonic and super- 
sonic flows. (LES data in subsonic flow is from [36] ). 
the critical We for bag breakup in supersonic flow 
is higher than in subsonic air. 
The drop breakup process consists of two 
stages: (1) drop deforms into a liquid disk; (2) dis- 
integration of the liquid disk. The elapsed time of 
the deformation period is defined as the initiation 
time t ∗
I , and the cross-stream diameter of the liquid 
disk at t ∗
I is defined as maximum cross-stream di- 
mension D max [31] . t ∗
I is indicated at the first sign 
of instability wave which determines the breakup 
mode (e.g. bag formation for the bag breakup as 
in Zhao et al. [31] ). Figures 8 and 9 compares t ∗
I 
and D max predicted for drop breakup in supersonic 
flow with the available experimental measurements 
[31–34] and LES results [14] in subsonic flows. It 
is observed that t ∗
I obtained from LES of drop in 
supersonic flow is higher than that from LES of 
drop in subsonic flow. It has been demonstrated 
by experiments [31] and LES [14] that D max grows 
from a small value (around 1.6) in the bag regime 
to 2 in the bag-stamen and multimode regimes in 
the subsonic flow. The present simulation s confirm 
the same trend in the supersonic flow as shown in 
Fig. 9. 
Figures 10 and 12 show the pressure (nondimen- 
sionalized by ρ∞  U 2 
∞  ) and velocity vector at plane 
z = 0. A strong bow shock forms ahead of the drop, 
and the shock structure and position change as 
the drop moves and deforms, indicating that the 
boundary conditions for the gas flow solver on the 
drop surface are properly provided. In the down- 
Fig. 9. D max versus We in subsonic and supersonic flows. 
(LES data in subsonic flow is from [36] ). 
Fig. 10. Pressure (nondimensionalized by ρ∞  U 2 
∞  ) con- 
tour and velocity vector at t ∗=0.48 for We = 19.5, 
Ma = 3. 
stream of the shock, the gas flow goes around the 
drop, resulting in high pressure on the windward 
side of the drop and low pressure on the down- 
stream side and periphery. The pressure difference 
between the windward side and the drop periphery 
drives the liquid to move laterally, deforming the 
drop into a disk shape as shown in Fig. 10 . Since 
the Reynolds number is low, the vortex in the wake 
of the drop is axisymmetric. 
Figure 11 compares the drag coefficient and 
drop cross-stream dimension during drop deforma- 
tion in subsonic ( We = 13.5 [36] ) and supersonic

<!-- PDF_PAGE: 7 -->

F. Xiao et al. / Proceedings of the Combustion Institute 36 (2017) 2417–2424 2423 
Fig. 11. Comparison of drag coefficient C D and cross- 
stream dimension D c of drop in subsonic and supersonic 
flows. (LES data in subsonic flow is from [36] . Experimen- 
tal data of C D for sphere in subsonic and supersonic flows 
are respectively from [37] and [38] ). 
Fig. 12. Pressure (nondimensionalized by ρ∞  U 2 
∞  ) con- 
tour and velocity vector at t ∗=1.45 for We=19.5, Ma=3. 
( We = 17) flows. C D is well predicted at the start 
when the drop is almost spherical in comparison 
with the experimental data for a solid sphere. It 
can be observed that as the drop deforms from 
a sphere to a liquid disk, the drag coefficient C D 
grows moderately from 1.05 to 1.35 in supersonic 
flow while C D more than doubles in the deforma- 
tion period in subsonic flow. The predicted C D is 
always higher in supersonic flow than in subsonic 
flow. The predicted drop cross-stream dimension 
D c grows slower in supersonic flow than in subsonic 
flow. This arises from the different behaviours be- 
tween the subsonic and supersonic flows round an 
obstacle. In subsonic flow, the region with lowest 
pressure is the drop periphery, and the high pres- 
sure on both drop windward side and leeward side 
drives the liquid to move laterally [36] . In super- 
sonic flow, the lowest pressure region is the drop 
leeward side, and thus the pressure driving force 
in the lateral direction is weaker. Furthermore, the 
aerodynamic force can be weakened after the shock 
compression ahead of the drop (total pressure loss 
across shocks is well known). Therefore, it requires 
a longer initiation time for the drop to deform into a 
liquid disk in supersonic flow, and also a higher crit- 
ical We number to achieve corresponding breakup 
mode than in subsonic flow. 
Figure 12 shows that the huge pressure differ- 
ence between the upstream and downstream sides 
of the liquid disk makes the low-density gas sig- 
nificantly accelerate the high-density liquid phase, 
which can induce Rayleigh–Taylor (RT) instability. 
The drop acceleration a D is derived from the sim- 
ulation results as in [13] , which are 588, 064 m/s 2 , 
766, 030 m/s 2 , 812, 456 m/s 2 at t ∗
I for We = 19.5, 
28, 75 test cases respectively. The wavelengths 
of the most unstable RT wave calculated from 
λmax = 2 π(3 σ/ (ρL a D )) 1 / 2 are1.47 D ,1.07 D ,0.64 D 
for the three test cases respectively. After t ∗
I , the 
instability wave develops on the simulated liquid 
disk as shown in Figs. 5 –7 , and the wavelengths are 
1.68 D, D , 0.6 D for the three test cases respectively 
which are consistent with the RT instability. 
4. Conclusions 
The deformation and breakup of drop in super- 
sonic flow is simulated using a CLSVOF interface 
tracking method. The shock waves ahead of the 
drop are well reproduced. The drop deformation 
and breakup morphology at different Weber num- 
bers is well predicted, indicating that the interaction 
between the gas flow and liquid flow at the interface 
is properly captured by the proposed method. The 
critical Weber number between different breakup 
modes and the initiation time are higher in super- 
sonic flow than in subsonic flow. 
Acknowledgements 
This project was supported by National Nat- 
ural Science Foundation of China (Project Nos. 
11402298 , 51406233 and 11472303 ). Simulations 
were run on Tianhe-1A of National Supercomput- 
ing Center in Changsha. 
References 
[1] M. Gorokhovski , M. Hermann , Ann. Rev. Fluid 
Mech. 40 (2008) 343–366 . 
[2] O. Desjardins , J.O. McCaslin , M. Owkes , P. Brady , 
Atomization Sprays 23 (2013) 1001–1048 . 
[3] J. Shinjo , A. Umemura , Int. J. Multiphase Flow 36 
(2010) 513–532 . 
[4] J. Shinjo , A. Umemura , Proc. Combust. Inst. 33 
(2011) 2089–2097 . 
[5] J. Shinjo , A. Umemura , Proc. Combust. Inst. 35 
(2015) 1595–1602 .

<!-- PDF_PAGE: 8 -->

2424 F. Xiao et al. / Proceedings of the Combustion Institute 36 (2017) 2417–2424 
[6] F. Xiao , M. Dianat , J.J. McGuirk , AIAA J. 51 (2013) 
2878–2893 . 
[7] F. Xiao , M. Dianat , J.J. McGuirk , Int. J. Multiphase 
Flow 60 (2014) 103–118 . 
[8] D.R. Guildenbecher , C. López-Rivera , P.E. Sojka , 
Exp. Fluids 46 (2009) 371–402 . 
[9] M. Jalaal , K. Mehravaran , Int. J. Multiphase Flow 47 
(2012) 115–132 . 
[10] M. Jalaal , K. Mehravaran , Phys. Fluids 26 (2014) 
012101 . 
[11] T. Kékesi , G. Amberg , L. Prahl Wittberg , Int. J. Mul- 
tiphase Flow 66 (2014) 1–10 . 
[12] M. Jain , R.S. Prakash , G. Tomar , R.V. Ravikrishna , 
Proc. R. Soc. A 471 (2015) 20140930 . 
[13] F. Xiao , Large eddy simulation of liquid jet primary 
breakup , 2012 Ph.D. thesis . Loughborough Univer- 
sity, Loughborough, United Kingdom 
[14] F. Xiao , M. Dianat , J.J. McGuirk , Atomization 
Sprays 24 (2014) 281–302 . 
[15] D. Fuster , G. Agbaglah , C. Josserand , S. Popinet , 
S. Zaleski , Fluid Dyn. Res. 41 (2009) 065001 . 
[16] H. Terashima , G. Tryggvason , J. Comp. Phys. 228 
(2009) 4012–4037 . 
[17] H. Terashima , G. Tryggvason , Comput. Fluids 39 
(2010) 1804–1814 . 
[18] R.K. Shukla , C. Pantano , J.B. Freund , J. Comp. 
Phys. 229 (2010) 7411–7439 . 
[19] T.G. Theofanous , Annu. Rev. Fluid Mech. 43 (2011) 
661–690 . 
[20] C.H. Chang , X.L Deng , T.G. Theofanous , J. Comp. 
Phys. 242 (2013) 946–990 . 
[21] R. Caiden , R.P. Fedkiw , C. Anderson , J. Comp. Phys. 
166 (2001) 1–27 . 
[22] M.B. Sun , H. Geng , J.H. Liang , Z.G. Wang , Flow 
Turbul. Combust. 82 (2009) 271–286 . 
[23] M.B. Sun , Z.G. Wang , J.H. Liang , H. Geng , J. 
Propul. Power 24 (2009) 688–696 . 
[24] C.W. Shu , High-Order Methods for Computa- 
tional Physics, Eds., Springer-Verlag, Berlin, 1999, 
pp. 439–582 . 
[25] G.S. Jiang , C.W. Shu , J. Comput. Phys. 126 (1996) 
202–228 . 
[26] R. Fedkiw , T. Aslam , B. Merriman , S. Osher , J. Com- 
put. Phys. 152 (1999) 457–492 . 
[27] M. Kang , R. Fedkiw , X.D. Liu , J. Sci. Comput. 15 
(2000) 323–360 . 
[28] T.G. Theofanous , G.J. Li , T.N. Dinh , J. Fluids Eng. 
126 (2004) 516–527 . 
[29] T.G. Theofanous , G.J. Li , Phys. Fluids 20 (2008) 
052103 . 
[30] H. Zhao , H.F. Liu , J..L. Xu , W.F. Li , K.F. Lin , Phys. 
Fluids 25 (2013) 054102 . 
[31] H. Zhao , H.F. Liu , W.F. Li , J.L. Xu , Phys. Fluids 22 
(2010) 114103 . 
[32] L.P. Hsiang , G.M. Faeth , Int. J. Multiphase Flow 18 
(1992) 635–652 . 
[33] M. Pilch , C.A. Erdman , Int. J. Multiphase Flow 13 
(1987) 741–757 . 
[34] Z. Dai , G.M. Faeth , Int. J. Multiphase Flow 27 (2001) 
217–236 . 
[35] H.W. Liepmann , A. Roshko , Elements of Gasdy- 
namics, John Wiley and Sons, New York, 1957, 
p. 105 . 
[36] F. Xiao , M. Dianat , J.J. McGuirk , Comput. Fluids 
136 (2016) 402–420 . 
[37] B.R. Munson , D.F. Young , T.H. Okiishi , Fundamen- 
tals of Fluid Mechanics , New York, 1990 . 
[38] D.J. Carlson , R.F. Hoglund , AIAA J. 2 (1964) 
1980–1984 .
