<!-- PDF_PAGE: 1 -->

Pressure-based large-eddy simulation of
under-expanded hydrogen jets for engine
applications
A. Ballatore *, J.A. van Oijen
Eindhoven University of Technology, Department of Mechanical Engineering, Power & Flow, Building 15, Groene
Loper 5, 5612 AE, Eindhoven, the Netherlands
highlights
/C15 Our model correctly describes the mixing of H2 jets for DI-CI engine applications.
/C15 Pressure-based solvers can be used with reasonable accuracy for under-expanded ﬂows.
/C15 Under-relaxation factors help such p-based algorithm improving the shock resolution.
/C15 The WALE model with 4th-order cubic convective schemes delivers the most accurate results.
article info
Article history:
Received 26 June 2023
Received in revised form
31 August 2023
Accepted 6 September 2023
Available online 22 September 2023
Keywords:
Under-expanded jets
Large-eddy simulation
Pressure-based
OpenFOAM
Compressible effects
abstract
An assessment of Large-Eddy Simulations (LES) of non-reactive under-expanded hydrogen
jets by using a pressure-based algorithm is presented. Such jets feature strong
compressible discontinuities often considered to be best dealt with by a density-based
solver. The crucial contribution of this work is to evaluate the suitability of the pressure-
based solver to correctly describe the ﬂow ﬁeld of gaseous hydrogen jets for engine ap-
plications, despite the presence of shock waves in the under-expanded near-oriﬁce region.
Inherently, the paper aims at providing guidance on the corresponding numerical aspects
to simulate these ﬂows. Hydrogen jets in an argon atmosphere at three different injection
pressures are simulated and the results are compared to experiments in literature. Jet tip
penetration and cone angle are the main investigated parameters. A good match is found,
conﬁrming the solidity of the proposed model. Different LES sub-grid scale models and
discretisation schemes are then investigated in order to ﬁnd the best approach in terms of
accuracy and required computational cost. In particular, it is found that the WALE model
coupled with a 4th-order cubic scheme for the convective terms yields the most suitable
conﬁguration.
© 2023 The Author(s). Published by Elsevier Ltd on behalf of Hydrogen Energy Publications
LLC. This is an open access article under the CC BY license ( http://creativecommons.org/
licenses/by/4.0/).
* Corresponding author .
E-mail address: a.ballatore@tue.nl (A. Ballatore).
Available online at www.sciencedirect.com
ScienceDirect
journal homepage: www.elsevier.com/locate/he
international journal of hydrogen energy 49 (2024) 771 e783
https://doi.org/10.1016/j.ijhydene.2023.09.062
0360-3199/© 2023 The Author(s). Published by Elsevier Ltd on behalf of Hydrogen Energy Publications LLC. This is an open access article under the CC BY
license ( http://creativecommons.org/licenses/by/4.0/).

<!-- PDF_PAGE: 2 -->

1. Introduction
Hydrogen has been labeled for a long time as the fuel of the
future [1e4], due to its carbon-free combustion and the ability
to achieve high energy efﬁciency. Moreover, it can be produced
from renewable energy sources, enabling efﬁcient large-scale
storage and transport of renewable energy. The unique
thermo-physical properties of hydrogen can facilitate the
design of a highly efﬁcient internal combustion engine (ICE) [5].
The high diffusivity of hydrogen, for instance, may enhance in-
cylinder fuel-air mixing. Furthermore, the wide ﬂammability
limit from 4 to 76 vol% hydrogen in air, alongside with the high
ﬂame speed, indicates that hydrogen ICE can operate consid-
erably lean, thus improving thermal efﬁciency [6e9]. In partic-
ular, direct injection of hydrogen, aside from enabling high
volumetric efﬁciency, avoids possibly undesired combustion-
related phenomena such as engine knock [ 10,11]. However,
due to its low density, H
2 requires high injection pressures to
fully penetrate in the cylinder [ 12]. This typically leads to a
turbulent under-expanded jet, as explained in the following.
Let us consider a converging nozzle, like the ones normally
involved in engine applications. With respect to the pressure
proﬁles shown in Fig. 1 , the most trivial case is when the in-
jection pressure P
0 and the ambient pressure P∞ are the same.
In this case (curve a), there is no ﬂow. When the ratio between
the total pressure in the nozzle P
0 and the ambient pressure
P∞, namely the Nozzle Pressure Ratio (NPR), increases, the
ﬂow becomes subsonic. This trend (curve b) holds until the
outlet velocity reaches sonic conditions, i.e. the Mach number
is Ma ¼ 1 (curve c). The exit pressure P
e and the ambient
pressure are still equal, and the ﬂow is said to be choked. The
value of NPR where this chocked condition occurs, is labeled
as the critical pressure ratio. Increasing the injection pressure
further will not have any additional effect on the ﬂow velocity
within the nozzle, as the maximum Mach number in the
minimum-area section is 1. The local speed of sound c will
also remain the same at the exit. In fact, c ¼ ﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃgRT
e
p , with g
being the speciﬁc heat ratio, R the speciﬁc gas constant and Te
the exit temperature. For an ideal gas, Te, at ﬁxed g and Ma,
depends solely on the injection temperature T0, that is kept
ﬁxed when increasing the injection pressure P0. If the injection
pressure P0 increases further, an under-expanded condition
occurs (curve d). At ﬁrst, this is moderately under-expanded:
the outlet velocity cannot go beyond Ma ¼ 1, and so the exit
pressure becomes higher than the ambient one; as a conse-
quence, a further expansion occurs in the near-oriﬁce region,
in order to let the pressure reduce to the ambient one. A very
weak normal shock forms at the exit of the nozzle, together
with a pattern of oblique reﬂected shock waves. As P
0 is
further increased, the ﬂow reaches a point where eventually it
becomes highly under-expanded: at the nozzle exit, an inﬁnite
number of rarefaction waves (the so-called Prandtl-Mayer fan)
spreads onto the jet boundary and collapse into a slightly-
curved oblique shock wave named Mach disk.
In-depth understanding of both the aforementioned
under-expansion process and the related turbulent mixing
past the nozzle oriﬁce is therefore required for the design of an
efﬁcient gaseous injection system and for the analysis of the
most suitable associated injection strategies aimed at better
mixture quality and clean combustion [ 13], by improving the
jet penetration and the mixing of the fuel with the sur-
rounding environment.
From a computational point of view, the near-nozzle re-
gion is the most challenging aspect in an under-expanded
ﬂow. It has mostly been studied using density-based solvers,
in which the primitive variable is the density, directly
computed from mass conservation with pressure being
updated through an equation of state. For instance, Ham-
zehloo [13], Vuorinen et al. [14], and Li et al. [15] used a density-
based approach to tackle, by means of LES, the resolution of
the shock cells pattern of the near-nozzle region. Duronio
et al. [ 16] and Bonelli et al. [ 17] did the same but with RANS
(Reynolds-averaged Navier Stokes) simulations. While this is
the most natural approach for the resolution of shock waves,
since the governing equations are solved for the conservative
variables, density-based solvers on the other hand experience
stiffness problems as well as a loss of accuracy when
approaching the low Mach number limit. Moreover, the time
step is limited by the most rapidly propagating wave, which
becomes restrictive for low Mach number ﬂows [ 18]. Lai et al.
[19] showed, in RANS, the performance of the pressure-based
numerical method to resolve shocks and other discontinuities
to rival those of the density-based methods. Moreover, in in-
jection for ICE where the ﬂow in the largest part of the
computational domain is at a low Mach number but in some
parts supersonic ﬂow exists, a pressure-based solver may be
an attractive as well as efﬁcient choice [ 20]. For instance, Li
et al. [ 21] investigated under-expanded hydrogen jets with
RANS by ﬁrst computing the near-nozzle ﬂow ﬁeld in a smaller
domain using a density-based solver, and then use that
Fig. 1 e Schematic pressure distributions in a converging
nozzle.
international journal of hydrogen energy 49 (2024) 771 e783772

<!-- PDF_PAGE: 3 -->

solution to compute the ﬂow further downstream through a
pressure-based solver. Babayev et al. [ 22] conducted their
computational study by means of a pressure-based PISO al-
gorithm coupled with RANS modelling to assess the charac-
teristics of a H
2 direct-injection compression-ignition
combustion concept.
In H 2-ICE, the aforementioned supersonic region covers
indeed only a small part of the domain, and the main focus is
correctly describing the fuel/oxidizer mixing on a larger scale,
the whole combustion chamber, in view of an engine appli-
cation. Solving the largest turbulent structures, rather than
time-averaging like in RANS, helps capturing accurately this
phenomenon, hence the use of LES is crucial [ 23]. Moreover,
the mixing process occurs mostly downstream of the under-
expanded region, where the local Mach number is low and
the ﬂow can be deemed incompressible, and where conse-
quently density-based solver could fail in accuracy and efﬁ-
ciency. Therefore, we aim to study for the ﬁrst time such
under-expanded jets with LES through a pressure-based
solver, and compare the results against experimental litera-
ture to validate such an approach. In the next sections, after a
brief review of the mathematical background of the problem,
the computational setup will be introduced, and the results
will be discussed.
2. Numerical problem
The dynamics of a ﬂuid is governed by mass, momentum, and
energy conservation, namely the (compressible) Navier-
Stokes equations. For a non-reactive ﬂow they read [ 24]:
vr
vt þ v
vxi
ðruiÞ¼ 0 (1)
vðruj Þ
vt þ v
vxi
ðruiuj Þ¼/C0 vp
vxj
þ vtij
vxi
(2)
vrhs
vt þ v
vxi
ðruihs Þ¼ Dp
Dt þ v
vxi
/C18
l vT
vxi
/C19
þ tij
vui
vxj
/C0 v
vxi
 
r
XN
k¼1
Vk;iYk hs;k
!
þ _uT
(3)
with:
Dp
Dt ¼ vp
vt þ ui
vp
vxi
; (4)
where r is the density, ui the ith component of the velocity
vector, p the pressure, hs is the sensible enthalpy, Vk,i is the
diffusion velocity of the ith species, qi ¼/C0 l vT
vxi
is the heat ﬂux
vector, with T the ﬂuid temperature and l the thermal con-
ductivity. The chemical heat release rate _uT is zero for the
non-reacting ﬂows considered in this work. The total stress
tensor tij is given by:
tij ¼ m
/C20 vui
vxj
þ vuj
vxi
/C21
/C0
/C18 2
3 m vuk
vxk
/C19
dij; (5)
with dij the Kronecker delta. If the ﬂuid is assumed to be an
ideal gas (acceptable assumption for hydrogen jets [ 25]), then
pressure and density can be linked by the well-known ideal
gas law p ¼ rRT, with R being the speciﬁc gas constant. In total,
ﬁve equations are needed: one for the density, three for the
components of the velocity, one for the energy.
If the gas consists of more than one species, then another
set of transport equations adds up to the ﬁve above, namely:
vrYk
vt þ v
vxi
ðrui YkÞ¼ v
vxi
/C18
rDk
vYk
vxi
/C19
þ _uk; (6)
where Yk indicates the mass fraction of species k ¼ 1, …, N, Dk
the corresponding molecular diffusion coefﬁcient, and uk the
net chemical production rate, which is null for the non-
reactive ﬂows considered in this study. Since for the conser-
vation of mass, the sum of all the species fractions must be
equal to 1, these transport equations constitute N /C0 1 addi-
tional relations to be solved together with the aforementioned
ﬁve.
2.1. LES modelling
Denoting Reynolds-averaged quantities by a bar f and Favre-
averaged quantities by a tilde ef ¼ rf =r, the ﬁltered
compressible Navier-Stokes equations can be written as [ 24]:
vr
vt þ v
vxi
ðreuiÞ¼ 0 (7)
v
vt ðreui Þþ v
vxi
ðreuieuj Þ¼/C0 vp
vxj
þ v
vxi
½tij /C0 rðguiuj /C0 euieujÞ/C138 (8)
vrehs
vt
þ v
vxi
ðreuiehs Þ¼ Dp
Dt þ v
vxi
/C20
l vT
vxi
/C0 rðgui hs /C0 euiehs Þ
/C21
þ tij
vui
vxj
/C0 v
vxi
 
r
XN
k¼1
Vk;iYkhs;k
!
þ _uT
(9)
vðrfYk Þ
vt þ v
vxi
ðreuifYkÞ¼ v
vxi
/C2
Vk;iYk /C0 rðguiYk /C0 euifYkÞ
/C3
þ _uk (10)
where
Dp
Dt ¼ vp
vt þ ui
vp
vxi
(11)
The ﬁrst right-hand side term of Eq. (10) needs closure,
typically done as:
Vk;i Yk /C0 rðguiYk /C0 euifYkÞ¼
/C18
/C0 rDk þ mt
Sck
/C19 veYk
vxi
(12)
where mt is the turbulent viscosity and Sck is the sub-grid scale
Schmidt number for species k. The ideal gas equation of state
reads p ¼ rReT.
In OpenFOAM, the ﬁltering operation is performed by the
grid itself, so only the ﬁlter width is speciﬁed and not its shape.
It is crucial to avoid low-order numerical schemes, as any
artiﬁcial viscosity that would be added would increase the
error and smear out the turbulence [ 26]. The present study is
therefore based on the highest order numerical schemes
available within OpenFOAM, namely 2nd-order implicit
backward Euler for time derivatives, 2nd-order linear scheme
international journal of hydrogen energy 49 (2024) 771 e783 773

<!-- PDF_PAGE: 4 -->

for the gradient terms, and either 2nd-order linear or 4th-
order cubic interpolation for the divergences. Note that the
formal spatial accuracy of the cubic interpolation is only
second-order. This is due to the treatment of the viscous term
that is limited to a linear interpolation. However, since the
instabilities in the mixing layer at the ﬂanks of the jet are
convective instabilities, the convective terms deliver a higher
contribution than the viscous ones. Therefore, it could be
expected to obtain an accurate method just by treating only
the convective terms with a higher order of accuracy.
There are also many blended schemes available that
switch on-the-ﬂy from a high-order to a ﬁrst-order scheme
when the computation encounters strong gradients in the
variables, adding numerical viscosity to better deal with the
discontinuity and help stability. Indeed, this would be bene-
ﬁcial in resolving shock waves within the near-nozzle. How-
ever, for the same aforementioned reason, these methods
would not be beneﬁcial in the region further downstream, as
they would damp turbulent velocity ﬂuctuations.
The residual or sub-grid scale (SGS) Reynolds stresses
gu
iuj /C0 euieuj in Eq. (8) require modelling to get the closure of the
system. The residual stress tensor reads:
tR
ij ¼ rðguiuj /C0 euieujÞ (13)
with r being the ﬁltered density. The anisotropic part of the
residual stress tensor is deﬁned as [ 27]:
tr
ij ¼ tR
ij /C0 2
3krdij (14)
where kr denotes the residual kinetic energy kr ¼ 1
2tR
ii . Using a
Boussinesq-like hypothesis, the anisotropic contribution of
the residual stress tensor is assumed to be directly propor-
tional to the (ﬁltered) strain rate tensor by means of a sub-grid
kinematic viscosity n
sgs, namely:
tr
ij ¼/C0 2rnsgseSij (15)
whereeSij ¼ 1
2
/C16
veui
vxj
þ
veuj
vxi
/C17
. In this study, three different sub-grid
viscosity models will be compared. Smagorinsky was the
ﬁrst to propose an expression for the sub-grid viscosity [ 28] as:
nsgs ¼ C2
SD2
ﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ
2eSije
S
ij
q
(16)
with a model constant CS z 0.18 and the ﬁlter width D ¼
ðDx DyDzÞ
1
3 . The wall-adapting local eddy-viscosity (WALE)
method is another SGS model developed based on the Sma-
gorinsky model [29], where the sub-grid kinematic viscosity is
deﬁned as:
nsgs ¼ C2
W D2 ðSd
ijSd
ij
Þ
3
2
ðeSije
S
ijÞ
5
2 þð Sd
ijSd
ij
Þ
5
4
(17)
where Sd
ij is the traceless symmetric part of the square of the
velocity gradient tensor. Differently from the Smagorinsky
model, this model accounts for both strain and rotational rate
of the smallest resolved turbulent scales. As a consequence,
most of the turbulent transitional processes and structures
relevant for the kinetic energy dissipation are reproduced. The
WALE model retains null eddy viscosity in case of a pure
shear, which can occur in free jets. It is then possible to
reproduce the laminar to turbulent transition process through
the growth of linear unstable modes.
There are also models that compute the coefﬁcient
appearing in the sub-grid scale viscosity expression on-the-ﬂy
as the simulation progresses. While this could improve the
accuracy, it certainly increases the computational cost. For
instance, the model proposed in Ref. [ 30] solves an additional
transport equation for the sub-grid scale turbulent kinetic
energy k
sgs:
vrksgs
vt
þ v
vxi
ðreui ksgsÞ/C0 v
vxi
/C20
rðn þ nsgsÞ vksgs
vxj
/C21
¼ 2rnsgs
/C20 veui
vxj
: 1
2
/C18 veui
vxj
þ veuj
vxi
/C19/C21
/C0 2
3
v
vxi
ðreuiksgsÞ/C0 Cer
k3=2
sgs
D (18)
where the operator “:” denotes the double inner products of
two tensors and Ce is a model coefﬁcient derived from local
ﬂow properties. The sub-grid scale viscosity is then obtained
as
n
sgs ¼ CkksgsD (19)
with Ck being another model coefﬁcient, whose value again is
computed according to local ﬂow attributes. These types of
LES models are usually labeled as “one-equation” models. The
ability of these eddy-viscosity models to reproduce the near-
nozzle region will be investigated in section 4.
2.2. PIMPLE algorithm features for compressible ﬂows
A pressure-based approach within the OpenFOAM framework
is used. The solver herein treated is PIMPLE-based, which is a
merged PISO-SIMPLE (pressure implicit split operator - semi-
implicit method for pressure-linked equations) algorithm. It
computes the pressure from momentum and mass conser-
vation, iteratively corrects it, and then updates the density
through an equation of state, linking it to the pressure by
means of a compressibility factor j (for a perfect gas, j ¼ 1/
RT). This is a segregated solver: as pressure and velocity are
highly coupled in the Nanvier-Stokes equations due to the
presence of Vp in the momentum equations, the mass and
momentum equations are solved sequentially in order to
decouple them. One way of proceeding in an efﬁcient manner
was introduced by Chorin, whose projection method is a
fractional step technique in which the velocity is linearised by
decomposing it into a solenoidal and an irrotational contri-
bution. The detailed steps of Chorin 's method can be found in
Ref. [31].
The PIMPLE algorithm [ 32] is summarised in Fig. 2 ,w h e r e
the inner loop refers to the iterations performed to correct
the pressure, whereas the outer one denotes how many
times the system of equation is solved for a time step. In
general, the time step Dt must be set according to a Courant
number below 1 to ensure stability, Co ¼ uDt/Dx < 1, with Dx
the grid cell size. This is especially true for PISO-type
solvers. PIMPLE algorithms can achieve convergence even
for Co > 1[ 33]. However, such values correspond to a time
step whose solution, for highly turbulent LES ﬂows, is far
from reality because phenomena with high characteristic
velocity are not captured. Accordingly, decreasing the time
international journal of hydrogen energy 49 (2024) 771 e783774

<!-- PDF_PAGE: 5 -->

step can help capturing more and more turbulent ﬂuctua-
tions. In this sense, a good trade-off between quality of the
results and run-time has been found in the present work at
Co ¼ 0.5.
2.3. Transonic correction and under-relaxation
Originally, pressure-based solvers were developed for
incompressible and mildly compressible ﬂows, but nowadays
they have been extended to account for a broad range of sit-
uations, including transonic ﬂows [ 18,34,35]. The key devel-
opment has been the reformulation of the pressure equation
to include density and velocity correction, ensuring that the
type of the equation changed from purely elliptic for incom-
pressible ﬂows to hyperbolic in transonic and supersonic
compressible ﬂows [ 34]. In this way, the pressure plays the
dual role of affecting density (through the equation of state) in
the limit of high-Mach compressible ﬂow, and velocity
(through the gradient in the momentum equation) in the limit
of incompressible ﬂow, in order to enforce mass conservation.
In particular, the pressure contribution to the density when
the ﬂow is compressible reads:
r
transz
/C18 vr
vp
/C19
T
ptrans ¼ jptrans (20)
with respect to Fig. 2 , within the outer iteration, the sudden
change of a certain variable at a certain point in the domain
can cause numerical instability. A possible solution is issued
by allowing the variable to change only by a fraction a
4,
namely the under-relaxation factor. This factor a4 can be cho-
sen between 0 and 1, where 1 means that no under-relaxation
is used.
Fig. 2 e Iteration scheme for a single time-step of the PIMPLE algorithm.
international journal of hydrogen energy 49 (2024) 771 e783 775

<!-- PDF_PAGE: 6 -->

3. Computational setup
Simulations of the experimental hydrogen injections in the
work of Mansor et al. [36] are performed, in which the jet ﬂows
into an argon atmosphere within a cylindrical constant-
volume chamber of 8 cm in diameter and 3 cm in depth. For
the sake of simplicity, the present domain has been scaled
onto a 3 /C2 3 /C2 7.5 cm
3 cuboid. In the present work, the nozzle
has been placed on the outside and simply shaped as a conical
converging body with the same exit diameter of D ¼ 0.8 mm as
in the experiment. The same is true for the volume of the
chamber and the nozzle-wall distance. The boundaries of the
geometry (see Fig. 3 ) consist only of the injection area of the
nozzle (the “inlet”) and the walls of the injector and combus-
tion chamber (the “walls”).
The mesh was inspired by Ref. [ 13], in which a similar case
of injection is investigated, but here adapted in order to ach-
ieve a good balance between accuracy and computational
speed. After progressive reﬁnements, we came up with the
lightest mesh that could convey both stable and reliable
computations. It resulted in an almost fully orthogonal grid of
(roughly) 5 million cells. However, it has to be noted that it is
questionable whether a mesh sensitivity study, in its stricter
deﬁnition, can be carried out on a large-eddy simulation, since
both the discretisation schemes and the sub-grid scale models
introduce errors interacting in a non-linear way when
changing the grid spacing [ 37,38].
The largest part of the domain has a cell size of 0.26 mm ( D/
3). The near-nozzle ﬁeld features two reﬁnement regions, with
cell size of respectively 0.13 mm ( D/6) and 0.067 mm ( D/12), as
depicted in Fig. 3. Smaller cell sizes allow to better capture the
thin shock wave discontinuities. Moreover, they reduce the
sub-grid scale contribution in the highly shear-generated
turbulence zone.
The boundary conditions are summarised in Table 1 . The
ﬂow is initialized by prescribing a pressure ratio, namely an
injection pressure P
0 and an ambient pressure P∞. The ﬂuid in
the domain initially consists of argon and is stagnant every-
where. Following [39], no-slip boundary conditions are applied
to all solid walls. The temperature at which the hydrogen is
injected is kept ﬁxed at 300 K. The same value sets the initial
temperature ﬁeld in the rest of the domain. The ambient
pressure is P
∞ ¼ 1.2 MPa as in the experiments. The injection
pressure P0 is varied among 4, 8 and 14 MPa, leading to three
different cases with, respectively, NPR ¼ 3.3, 6.7, and 11.7. The
computational cost of such simulations translates into
approximately 0.02 ms of simulated physical time for every
hour of computation, performed on one node and 64 cores,
when using static SGS models. When using the dynamic k-
equation model, the computational cost increases roughly by
10%.
4. Results
A ﬁrst overview of the development of the resulting jet in
space and time can be found in Fig. 4, where density contours
are shown on the two-dimensional mid-plane of the whole
chamber. The WALE model has been chosen for the sub-grid
scale modelling, together with a 4th-order convective
scheme. This combination yields the most reliable results, as
will be shown in section 4.4. The hydrogen ﬂow expands
f r o mt h eo r i ﬁ c ei n t ot h ec h a m b e r .D u et ot h es t r o n ga n d
sudden injection of gas into a quiescent atmosphere,
compression waves surround the jet, reﬂecting on the walls
and then crossing each other. As the injection pressure in-
creases, the jet has a higher H
2 concentration (as indicated by
the different colour gradation), a larger width, and a faster
penetration.
4.1. Compressible effects
As compressibility effects are most challenging for a
pressure-based solver, we have a closer look at the near-
nozzle ﬁeld where these phenomena are the strongest. In
particular, the effect of under-relaxation on shock resolution
has been investigated. In Fig. 5 , the simulation results of two
identical under-expanded jets at NPR ¼ 3.3, with and without
under-relaxation ( a ¼ 0.7 and a ¼ 1, respectively), are
compared to Schlieren imaging of a compressed air jet
recorded experimentally [ 40] with a similar pressure ratio
(NPR ¼ 5). When under-relaxation is not employed, the
Fig. 3 e Schematic of the computational domain (left) and of the mesh (right, cross section mid-plane) and corresponding
boundary conditions (green: inlet, red: walls). (For interpretation of the references to colour in this ﬁgure legend, the reader
is referred to the Web version of this article.)
Table 1 e Boundary and initial conditions.
Inlet Walls Initial ﬁeld
P [MPa] rowhead 4 - 8 - 14 Zero gradient 1.2
u [m/s] rowhead - No-slip 0
T [K] rowhead 300 Zero gradient 300
Y
H2 rowhead 1 Zero gradient 0
YAr rowhead 0 Zero gradient 1
international journal of hydrogen energy 49 (2024) 771 e783776

<!-- PDF_PAGE: 7 -->

characteristic shock wave structure is dramatically blurred.
Some spurious compression waves can be observed in the
nozzle. Taking instead under-relaxation into account allows
the pressure-based algorithm at hand to reveal the charac-
teristic diamond pattern at the correct place. The use of high-
order discretisation schemes, in particular the 4th-order
cubic interpolation that has been applied in our studies, may
suffer from spurious oscillations that prevent the
convergence of the computations. Even when numerical
stability is ensured, under-relaxation factors can help in
increasing the accuracy. In Fig. 6 the dependency of the major
ﬂow variables on the magnitude of the under-relaxation
factor is presented. It is clear that the lower the under-
relaxation factor a, the more accurate the shock resolution
is. The drawback of a lower a is a slower convergence due to
an increased number of required inner iterations [ 41]. In view
of this, one should avoid using too small values of a. A good
trade-off between accuracy and efﬁciency has been found, for
the present study, in a ¼ 0.7.
4.2. Mass ﬂow
The faster jet penetration is a direct consequence of the mass
ﬂow exiting the nozzle. The mass ﬂow issued by an injector is
the amount of fuel per unit of time that passes through the
cross-section area of its nozzle. It is an important quantity as
its integral over time denotes how much fuel has been intro-
duced during the injection time. A theoretical estimate of the
mass ﬂow exiting a convergent nozzle is provided by the
following expression [ 42]:
_m ¼ A
nozzleP0
ﬃﬃﬃﬃﬃﬃﬃﬃg
RT0
r /C18 g þ 1
2
/C19 /C0 gþ1
2ðg/C0 1Þ
(21)
where Anozzle is the area of the oriﬁce issuing the jet and
g ¼ 1.4 is the speciﬁc heat ratio. It should be noted that, at ﬁxed
temperature, _m depends linearly on the injection pressure
only. This behaviour, despite of the isentropic approximation
of Eq. (21), is quite well matched by the numerical results in
which the mass ﬂow is directly computed from the density
Fig. 4 e Instantaneous density contours (kg/m 3) at the mid-plane at, from left to right respectively, NPR ¼ 3.3, 6.7, and 11.7.
Size of the reported area is 30 mm £ 75 mm.
Fig. 5 e Comparison of under-relaxation inﬂuence on
shock resolution. Left: a ¼ 1, middle: a ¼ 0.7, right:
Schlieren image of air jet at NPR ¼ 5 from Ref. [ 40].
international journal of hydrogen energy 49 (2024) 771 e783 777

<!-- PDF_PAGE: 8 -->

and velocity ﬁeld, as shown in Fig. 7 . Not only is the trend of
mass ﬂow versus injection pressure linear, but also the
computed mass ﬂow values resemble with good accuracy the
ones estimated by Eq. (21). This means that the discharge
coefﬁcient of the simulation is approximately 1, i.e. an ideal
situation where no pressure head losses occur within the
nozzle. Unfortunately, the experimental mass ﬂows are not
reported in Ref. [ 36].
4.3. Cone angle
As well as the penetration, the radial spreading of the jet gets
larger with increasing NPR. These two aspects are connected
by mass and momentum conservation. Simply speaking, the
more the jet diffuses laterally, the less mass and momentum
is available to penetrate in the axial direction, and vice versa.
From an experimental point of view, this is typically measured
by means of the cone angle, i.e. the angle between the jet
boundaries. There are various methods to measure it [ 43].
Here, we choose to compute the angle from the jet 's equiva-
lent area [ 44e46], and compare them to the ones measured
Fig. 6 e Near-oriﬁce pressure, temperature, density and Mach number as function of the axial distance along the centerline
at different under-relaxation factors.
Fig. 7 e Computed and theoretical nozzle mass ﬂows for
different injection pressures.
international journal of hydrogen energy 49 (2024) 771 e783778

<!-- PDF_PAGE: 9 -->

experimentally by Ref. [36]. In order to do so, the ﬂow has been
ﬁrst circumferentially averaged. The corresponding results
are shown in Fig. 8 and in Table 2 . The ﬁrst thing to notice is
that, in the same fashion as for the experimental reference,
the computed angles increase with increasing NPR. This cor-
rect trend conﬁrms the solidity of the numerical approach.
When the individual cases are compared, there is a discrep-
ancy of 3 e6
/C14 . These differences may be attributed to the un-
certainty in the angle measurements. In fact, locating the jet
boundaries is challenging. It depends strongly on the
threshold used to identify it [ 47], and it can reach an uncer-
tainty up to 24% [ 48]. Here, we decided to represent the jet by
the isocontour corresponding to the 0.1% H
2 mass fraction (i.e.
YH2 ¼ 0:001, using the same deﬁnition used for the jet tip
penetration in 4.4), but a unique deﬁnition on where to mea-
sure the jet angle is not present in literature. To underline the
sensitivity of the angle computation, we report also in Table 2
the angle calculated when taking the hydrogen mass fraction
equal to 0.2%. Indeed, when 0.2 is chosen as threshold, the
computed angles are 2 e3
/C14 smaller, and closer to the ones
predicted experimentally.
4.4. Jet penetration
The jet tip penetration is one of the key parameters that
characterise under-expanded jets with regards to air-fuel
mixing and mixture formation in direct injection engines
[49]. The penetration has been determined in this study by
recording the axial distance from the nozzle exit to the po-
sition where the mass fraction of hydrogen falls below a
threshold of 0.1%, as introduced by Ref. [ 44]. In under-
expanded ﬂows with Reynolds number in the order of 10
5 /C0
106, as in the present work, such measure of penetration
length was found to be a linear function of the square root of
time [50]. This behaviour is encountered as well in our study,
as can be observed in Fig. 9 , where the experimental data
from Ref. [ 36] are compared to the theoretical trend and to
the results coming from our simulations for three different
injection pressures. The trends of the numerical simulations
follow the experimental ones and ﬁt the linear trend, con-
ﬁrming the validity of the present numerical model. The jet
has a high velocity immediately after the nozzle, then it
starts decelerating and spreading radially due to loss of
momentum. As the NPR increases, the jet tip penetration
rate increases due to higher momentum, hence resulting in a
faster ﬂow.
Fig. 8 e Cone angle of hydrogen jets at, from above to bottom, NPR ¼ 3.3, 6.7, 11.7. The measurements have been performed
by computing the angle swept by the equivalent jet triangle area at y ¼ L/2 and YH2 ¼ 0:001
Table 2 e Computed cone angles 4 and comparison with
the experimental values of [ 36] for different injection
pressures. Two different threshold criteria, 0.1% and 0.2%
hydrogen mass fraction, have been used to highlight the
sensitivity of the measurement.
P0 NPR Y H2 ¼ 0.1% Y H2 ¼ 0.2% Exp [ 36].
4 MPa 3.3 29.4 /C14 27.3/C14 22.9/C14
8 MPa 6.7 32.0 /C14 28.8/C14 26.4/C14
14 MPa 11.7 35.2 /C14 33.0/C14 31.0/C14
international journal of hydrogen energy 49 (2024) 771 e783 779

<!-- PDF_PAGE: 10 -->

The penetration lengths of hydrogen are reported for the
three different injection pressures, computed with different
combinations of LES models and convective discretisation
schemes. First, the static Smagorinsky and WALE models and
the dynamic k-equation model are compared in Fig. 10. It can
be seen that the penetration curves on overall are quite
similar. One thing worth underlining is that the error accu-
mulates in time. This is why the differences among the LES
models are larger when the NPR is lower, i.e. when the jet is
slower. In the initial development of the jet the Smagorinsky
model predicts a deeper penetration in time. Indeed, the
Smagorinsky model is not suitable for high shear ﬂows, since
the SGS dissipation is too high to correctly predict the tran-
sition to turbulence during the initial evolution of the jet,
resulting in a substantial underprediction of jet width [ 51] and
over-prediction of jet penetration. The dynamic K-equation
model appears most accurate for high NPR values but lacks
precision with respect to the expected trend in the case with
NPR ¼ 3.3. On the contrary, the static WALE model matches
the experimental data on average better.
In Fig. 11 , the WALE model is then compared to the dy-
namic K-equation model with different discretisation
schemes. When coupled with the linear scheme, the results
get closer to the reference data when NPR ¼ 11.7, and the same
is true with cubic interpolation when NPR ¼ 6.7, whereas for
NPR ¼ 3.3 there is little difference between the two dis-
cretisation schemes. In general, one would prefer the cubic
scheme over the linear interpolation due to the higher order of
accuracy in the convective terms, and hence improved
description of the turbulence.
In order to reduce the statistical uncertainty, one should
in principle average an ensemble of as many different tur-
bulent realisations as possible [ 52]. Simulation has to be
repeated many times, requiring a high computational effort.
However, there could be cases in which this operation would
add little information, for instance, in high-velocity strong
shear ﬂows where most of the turbulence is generated by the
development of the jet rather than inﬂuenced by the initial
turbulent conditions. In order to investigate this, additional
Fig. 9 e Jet penetration length as a function of the square
root of time. Blue: NPR ¼ 3.3, red: NPR ¼ 6.7, green:
NPR ¼ 11.7. Circles: experimental data, dashed lines:
present study, solid lines: theoretical trend. (For
interpretation of the references to colour in this ﬁgure
legend, the reader is referred to the Web version of this
article.)
Fig. 10 e H2 penetration length at different NPR values (top:
NPR ¼ 3.3, middle: NPR ¼ 6.7, bottom: NPR ¼ 11.7) with
different SGS models.
international journal of hydrogen energy 49 (2024) 771 e783780

<!-- PDF_PAGE: 11 -->

simulations of the NPR ¼ 6.7 case have been performed, for
which some turbulent white noise has been prescribed
constantly in time at the inlet of the nozzle, in order to
introduce a certain amount of random ﬂuctuations to the
ﬂow along the three directions in space. More precisely, a
digital-ﬁlter based inlet boundary condition for velocity is
used to generate synthetic turbulence-alike time-series,
where the root mean squared (RMS) ﬂuctuation scale is 10%
of the mean ﬂow in every direction in space. The bottom-
right panel of Fig. 11 shows the jet penetration in time for
three different realisations: one with no added turbulence at
the inlet, and two additional simulations with the same
turbulence intensity prescribed at the inlet but with different
randomness. It can be noted that the jet penetration length
does not differ too much from one simulation to the other, at
most 5%, compared to the maximum difference that char-
acterises the single realisations with different LES models
and numerical schemes, that can reach values up to 20%. We
can then conclude that differences much bigger than 5% are
not due to a particular realisation but rather to the method
used. Hence, one single realisation is deemed here sufﬁcient
to fully characterise the jet.
5. Conclusions
In the present paper, the suitability of a pressure-based
PIMPLE-solver for large-eddy simulation of non-reactive,
under-expanded, highly turbulent H
2 jets for engine applica-
tions has been investigated for the ﬁrst time. The advantage of
using such a solver is to keep a high accuracy in describing the
low-Mach turbulence occurring in most of the domain,
meanwhile being still able to capture fairly well, through a
proper transonic correction, the strong compressible discon-
tinuities that arise in the near-oriﬁce ﬁeld. To this end, it is
shown that the use of under-relaxation factors improves the
shock resolution, especially when oscillatory high-order
interpolation schemes are employed. Different LES models
and numerical schemes have then been assessed. The static
Smagorinsky model appears to be unsuitable for the investi-
gated ﬂows. The dynamic K-equation model looks to be more
accurate for high injection pressure but lacks precision for the
case with low NPR. In the end, the WALE model with 4th-order
convective schemes has been found to be the best trade-off
between accuracy and computational time, and hence it is
Fig. 11 e H2 penetration length at different NPR values with different LES models and convective schemes. Top left:
NPR ¼ 3.3, top right: NPR ¼ 6.7, bottom left: NPR ¼ 11.7. The bottom right panel shows results for different turbulent
realisations (NPR ¼ 11.7).
international journal of hydrogen energy 49 (2024) 771 e783 781

<!-- PDF_PAGE: 12 -->

the recommended choice for this speciﬁc case. Since the re-
sults coming from different turbulent realisations are very
similar, it is shown that one realisation is sufﬁcient to fully
characterise the jet.
Describing the fuel mixing with the surrounding environ-
ment in a correct way is fundamental in view of incorporating
combustion modelling. Hence, such a study is of importance
from a practical perspective, constituting a solid step towards
clean combustion of hydrogen for DI-CI engine applications.
The pressure-based model investigated in the present
manuscript has the advantage of describing both the high-Ma
compressible discontinuities and low-Ma turbulence, in
particular the ones arising in high-pressure hydrogen jets,
with acceptable accuracy and a high computational efﬁciency.
Declaration of competing interest
The authors declare that they have no known competing
ﬁnancial interests or personal relationships that could have
appeared to inﬂuence the work reported in this paper.
Acknowledgements
This publication is part of the Argon Power Cycle project
(project number 17868) ﬁnanced by the Dutch Research
Council (NWO).
references
[1] Pugazhendhi A, Chen W-H. Hydrogen energy technology for
future. Int J Hydrogen Energy 2022;47:37153 .
[2] Marchenko O, Solomin S. The future energy: hydrogen
versus electricity. Int J Hydrogen Energy 2015;40:3801 e5.
[3] Adeel A, Abul A-A, Angelina A, Saidur R. Hydrogen fuel and
transport system: a sustainable and environmental future.
Int J Hydrogen Energy 2016;41:1369 e80.
[4] Rana K, N DS, Jilakara S. Potential of hydrogen fuelled ic
engine to achieve the future performance and emission
norms. SAE Technical Papers; 2015 .
[5] Yip HL, Srna A, Yuen ACY, Kook S, Taylor RA, Yeoh GH,
Medwell PR, Chan QN. A review of hydrogen direct injection
for internal combustion engines: towards carbon-free
combustion. Appl Sci 2019;9 .
[6] Onorati A, Payri R, Vaglieco B, Agarwal A, Bae C, Bruneaux G,
Canakci M, Gavaises M, Gu¨ nthner M, Hasse C, Kokjohn S,
Kong S-C, Moriyoshi Y, Novella R, Pesyridis A, Reitz R,
Ryan T, Wagner R, Zhao H. The role of hydrogen for future
internal combustion engines. Int J Engine Res 2022:529 e40.
[7] Ogden JM. Hydrogen: the fuel of the future? Phys Today
2002;55:69e75.
[8] Oh S, Kim C, Lee Y, Yoon S, Lee J, Kim J. Experimental
investigation of the hydrogen-rich offgas spark ignition
engine under the various compression ratios. Energy
Conversion and Management; 2019 .
[9] Kim J, Chun KM, Song S, Baek H-K, Lee SW. Hydrogen effects
on the combustion stability, performance and emissions of a
turbo gasoline direct injection engine in various air/fuel
ratios. Applied Energy; 2018 .
[10] Kee S-S, Shioji M, Mohammadi A, Nishi M, Inoue Y. Knock
characteristics and their control with hydrogen injection
using a rapid compression/expansion machine. SAE Trans
2007;116:217e26.
[11] Song J, Park S. Combustion characteristics of a methane
engine with air- and n2-assisted direct injection. Fuel; 2017 .
[12] Lee S, Kim G, Bae C. Behavior of hydrogen hollow-cone spray
depending on the ambient pressure. Int J Hydrogen Energy
2021;46:4538e54.
[13] Hamzehloo A, Aleiferis P. Computational study of hydrogen
direct injection for internal combustion engines. SAE
Technical Papers 2013;11 .
[14] Vuorinen V, Yu J, Tirunagari S, Kaario O, Larmi M, Duwig C,
et al. Large-eddy simulation of highly underexpanded
transient gas jets. Phys Fluids 2013;25:016101 .
[15] Li X, Wu K, Yao W, Fan X. A comparative study of highly
underexpanded nitrogen and hydrogen jets using large eddy
simulation. Int J Hydrogen Energy 2016;41:5151 e61.
[16] Duronio F, Montanaro A, Ranieri S, Allocca L, De Vita A.
Under-expanded jets characterization by means of cfd
numerical simulation using an open foam density-based
solver. In: 15th international conference on engines &
vehicles. SAE International; 2021 .
[17] Bonelli F, Viggiano A, Magi V. A numerical analysis of
hydrogen underexpanded jets under real gas assumption. J
Fluid Eng 2013;135 .
[18] Zhang L, Kumbaro A, Ghidaglia J-M. A conservative pressure
based solver with collo- cated variables on unstructured
grids for two-ﬂuid ﬂows with phase change. J Comput Phys
2019:265e89.
[19] Lai Y, So R, Przekwas A. Turbulent transonic ﬂow simulation
using a pressure-based method. Int J Eng Sci 1995;33:469 e83.
[20] Miettinen A, Siikonen T. Application of pressure- and
density-based methods for different ﬂow speeds. Int J Numer
Methods Fluid 2015;79:243 e67.
[21] Li X, Chen Q, Chen M, He Q, Christopher DM, Cheng X,
Chowdhury BR, Hecht ES. Modeling of underexpanded
hydrogen jets through square and rectangular slot nozzles.
Int J Hydrogen Energy 2019;44:6353 e65.
[22] Babayev R, Andersson A, Dalmau AS, Im HG, Johansson B.
Computational optimization of a hydrogen
direct-injection compression-ignition engine for jet mixing
dominated nonpremixed combustion. Int J Engine Res
2022;23:754e68.
[23] Rutland CJ. Large-eddy simulations for internal combustion
engines e a review. Int J Engine Res 2011;12:421 e51.
[24] Poinsot T, Veynante D. Theoretical and numerical
combustion. R.T. Edwards; 2005 .
[25] Khaksarfard R, Kameshki M, Paraschivoiu M. Numerical
simulation of high pressure release and dispersion of
hydrogen into air with real gas model. Shock Waves
2010:205e16.
[26] Roos Launchbury D. Recommendations for LES simulations.
Wiesbaden: Springer Fachmedien Wiesbaden; 2016. p. 63 e8.
[27] Pope SB. Turbulent ﬂows. Cambridge University Press; 2000 .
[28] Smagorinsky J. General circulation experiments with the
primitive equations. i. the basic experiment. Mon Weath
1963;91:99e164.
[29] Franck N, Ducros F. Subgrid-scale stress modelling based on
the square of the velocity gradient tensor. Flow, Turbul
Combust 1999;62:183 e200.
[30] Kim W-W, Menon S. A new dynamic one-equation subgrid-
scale model for large eddy simulations. 33rd Aerospace
Sciences Meeting and Exhibit; 1995 .
[31] Chorin AJ. Numerical solution of the Navier-Stokes
equations. Math Comput 1968;22:745 e62.
international journal of hydrogen energy 49 (2024) 771 e783782

<!-- PDF_PAGE: 13 -->

[32] Ferziger JH, Peri /C19c M. Computational methods for ﬂuid
dynamics. 2nd ed. Berlin: Springer; 1999 .
[33] Aravind Karthik M, Srinivas G, Naik N. Implementation of
higher-order pimple algorithm for time marching analysis of
transonic wing compressibility effects with high mach pre-
conditioning. Engineered Science 2022;20:218 e35.
[34] Karki KC, Patankar SV. Pressure based calculation procedure
for viscous ﬂows at all speedsin arbitrary conﬁgurations.
AIAA Journal 1989;27:1167 e74.
[35] Harlow FH, Amsden AA. A numerical ﬂuid dynamics
calculation method for all ﬂow speeds. J Comput Phys
1971;8:197e213.
[36] Mansor MRA, Nakao S, Nakagami K, Shioji M. Study on
hydrogen-jet development in the argon atmosphere. Green
Energy and Technology Zero-Carbon Energy Kyoto; 2012.
p. 177 e84.
[37] Kempf A, Geurts B, Oefelein J. Error analysis of large-eddy
simulation of the turbulent non-premixed sydney bluff-body
ﬂame. Combustion and Flame; 2011 .
[38] Salvetti M, Meldi M, Luca B, Sagaut P. Reliability of large-eddy
simulations: benchmarking and uncertainty quantiﬁcation.
ERCOFTAC Series 2018:15 e23.
[39] Gad-el Hak M. The ﬂuid mechanics of microdevices dthe
freeman scholar lecture. J Fluid Eng 1999;121:5 e33.
[40] Wei X, Mariani R, Chua L, Lim H, Lu Z, Cui Y, New T.
Mitigation of under-expanded supersonic jet noise through
stepped nozzles. J Sound Vib 2019;459:114875 .
[41] Barron RM, Salehi Neyshabouri AA. Effects of under-
relaxation factors on turbulent ﬂow simulations. Int J Numer
Methods Fluid 2003;42:923 e8.
[42] Dong C, Cui X, Liu S, Jiang Z, Wu Y. Investigation on the
choked mass-ﬂow characteristics of the helium ﬂuid during
the joule-thomson process in micro-oriﬁce under different
high pressures. Cryogenics 2022;122:103416 .
[43] Ruiz-Rodriguez I, Pos R, Megaritis T, Ganippa L. Investigation
of spray angle measurement techniques. IEEE Access; 2019.
p. 1. 1 .
[44] Naber JD, Siebers DL. Effects of gas density and vaporization
on penetration and dispersion of diesel sprays. SAE
Technical Paper; 1996 .
[45] Payri F, Payri R, Bardi M, Carreres M. Engine combustion
network: inﬂuence of the gas properties on the spray
penetration and spreading angle. Exp Therm Fluid Sci
2014;53:236e43.
[46] Emberson D, Ihracska B, Imran S, Diez A. Optical
characterization of diesel and water emulsion fuel injection
sprays using shadowgraphy. Fuel 2016;172:253 e62.
[47] Canny J. A variational approach to edge detection. In:
Proceedings of the third AAAI conference on artiﬁcial
intelligence, AAAI’83. AAAI Press; 1983. p. 54 e8.
[48] Macian V, Payri R, Garcia A, Bardi M. Experimental
evaluation of the best approach for diesel spray images
segmentation. Exp Tech 2012;36:26 e34.
[49] Yu J, Vuorinen V, Kaario O, Sarjovaara T, Larmi M.
Characteristics of high pressure jets for direct injection gas
engine. SAE Int J Fuels Lubricants 2013;6:149 e56.
[50] Petersen B, Ghandhi J. Transie nt high-pressure hydrogen jet
measurements. SAE 2006 World Congress & Exhibition;
2006.
[51] Le Ribault C, Sarkar S, Stanley SA. Large eddy simulation of a
plane jet. Phys Fluids 1999;11:3069 e83.
[52] Farrace D, Panier R, Schmitt M, Boulouchos K, Wright YM.
Analysis of averaging methods for large eddy simulations of
diesel sprays. SAE Int J Fuels Lubricants 2015;8:568 e80.
international journal of hydrogen energy 49 (2024) 771 e783 783
