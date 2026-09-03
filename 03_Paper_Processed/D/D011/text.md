<!-- PDF_PAGE: 1 -->

Effects of droplet evaporation on the ﬂow ﬁeld of
hydrogen-enhanced rotating detonation engines
with liquid kerosene
Songbai Yao a,b,*, Chunhai Guo a,b, Wenwu Zhang a,b
a Zhejiang Key Laboratory of Aero-Engine Extreme Manufacturing Technology, Ningbo Institute of Materials
Technology and Engineering, Chinese Academy of Sciences, Ningbo 315201, China
b University of Chinese Academy of Sciences, Beijing 100049, China
highlights
/C15 Rotating detonation engines (RDEs) with a heterogenous kerosene-hydrogen-air mixture are investigated.
/C15 Numerical simulations based on an Eulerian-Lagrangian two-way coupled framework are conducted.
/C15 A dual-front rotating detonation wave (RDW) caused by droplet evaporation is explained.
/C15 Micro-explosions and secondary RDWs are captured at higher kerosene mass ﬂow rates.
article info
Article history:
Received 5 March 2023
Received in revised form
24 April 2023
Accepted 26 April 2023
Available online 27 May 2023
Keywords:
Rotating detonation
Hydrogen-enhanced combustion
Kerosene fuel
Two-phase ﬂow
Eulerian-Lagrangian model
abstract
In this study, numerical simulations based on an Eulerian-Lagrangian framework are
conducted to investigate the liquid-fueled rotating detonation engine (RDE) with hetero-
geneous kerosene-hydrogen-air mixtures. The hydrogen addition is implemented for
combustion enhancement of the liquid kerosene and helps to ignite and achieve a self-
sustained two-phase rotating detonation wave (RDW). The effects of droplet evaporation
at various initial droplet sizes and kerosene mass ﬂow rates on the structure and propa-
gation of the two-phase RDW are analyzed. Results suggest that with smaller droplet sizes,
the structure of the RDW is analogous to that of a gaseous RDW, and a comparison with
experimental data suggests that the estimated detonation speed and thrust performance
(fuel-based speciﬁc impulse) are within the reasonable ranges. However, as the droplet size
or the mass ﬂow rate of kerosene increases, the two-phase RDW exhibits characteristic
features such as the dual-front laminated structure, micro-explosions and secondary
transverse waves.
© 2023 Hydrogen Energy Publications LLC. Published by Elsevier Ltd. All rights reserved.
* Corresponding author . Zhejiang Key Laboratory of Aero-Engine Extreme Manufacturing Technology, Ningbo Institute of Materials
Technology and Engineering, Chinese Academy of Sciences, Ningbo 315201, China.
E-mail address: yaosongbai@nimte.ac.cn (S. Yao).
Available online at www.sciencedirect.com
ScienceDirect
journal homepage: www.elsevier.com/locate/he
international journal of hydrogen energy 48 (2023) 33335 e33345
https://doi.org/10.1016/j.ijhydene.2023.04.314
0360-3199/© 2023 Hydrogen Energy Publications LLC. Published by Elsevier Ltd. All rights reserved.

<!-- PDF_PAGE: 2 -->

Introduction
The rapid global energy demand requires new power pro-
duction systems and advanced combustion technologies with
improved fuel efﬁciency and reduced emissions. The focus on
utilizing detonation for propulsion, characterized by a more
thermodynamically-efﬁcient cycle [ 1e3], has led to the prac-
tical development of detonation engines such as the pulsed
detonation engine (PDE), oblique detonation engine (ODE) and
rotating detonation engine (RDE). Recently, there have been
growing interest in the applications of RDEs to conventional
gas turbines, ramjets, and rocket engines. The RDE differs
from the other types of detonation engines in that reactants
are fed continuously from the head surface of the combustion
chamber and one or multiple rotating detonation waves
(RDWs) will propagate along the circumferential direction
continuously (see Fig. 1 ), which is why the RDE is also called
the continuous detonation engine (CDE) or continuously
rotating detonation engine (CRDE) in literature. The recent
development of RDEs was well summarized in some review
articles such as refs. [ 4,5].
E a r l ys t u d i e so nR D E sm a i n l yf o c u s e do ng a s e o u sf u e l s
such hydrogen [ 7e12], methane [ 13e16] and ethylene
[17e19], yet the advance of RDEs toward engineering ap-
plications demand liquid fuels that are more practically
used. Kindracki [ 20]a c h i e v e dc o n t i n u o u s l yr o t a t i n gd e t o -
nations by adding gaseous hydrogen to the kerosene-air
mixture. It was reported that they could not achieved
rotating detonations if kerosene and air were injected at the
ambient temperature and hot air was needed. They also
discussed the inﬂuence of hydrogen addition to kerosene-
fueled RDEs and stated that hydrogen addition was
environmentally-friendly and applicable to liquid-fueled
RDEs [ 21], though the additional supply of hydrogen might
complicate the fuel lines. In the same manner, kerosene-
fueled rotating detonations were obtained in a large-sized
RDE with a diameter of 503 mm by Bykovskii et al. [ 22],
where it was found that without hydrogen addition there
could only be turbulent combustion. The feasibility of
kerosene-fueled RDEs with hydrogen addition using a real-
istic geometry was demonstrated in the simulations by
Salvadori et al. [ 23]. Another route to achieve rotating det-
onations in kerosene-fueled RDEs was by replacing the air
oxidizer with pure oxygen or oxygen-enriched air. For
example, in the study of Ref. [ 24], rotating detonations were
achieved in oxygen-enriched kerosene-air mixture, but it
was found that kerosene-fueled detonations were difﬁcult
to be initialized and the issue was solved by using high
explosive materials. In the work of refs. [ 25,26], oxygen-
enriched air was supplied in order to obtain self-sustained
RDWs, while some used pre-heated hot air [ 27,28]. Xu
et al. [ 29] used an air-alcohol-oxygen heater to supply
oxygen-enriched air at the temperatures of 535 K e545 K in
their experimental research on kerosene-fueled RDEs.
Additionally, Ren and Zheng [ 30] studied the main structure
of kerosene-fueled RDEs in which premixed kerosene-air
mixture was supplied at the total temperatures of
900e1200 K, below which self-sustained RDWs could not be
obtained. Cracked kerosene-air mixtures have also been
taken into consideration [ 31].
Each combustion enhancement approach has its own pros
and cons and here we focus on the strategy of hydrogen
addition, which has also been used for the ammonia-fueled
RDE [ 32]. In this study, the effects of droplet evaporation on
the characteristics and structure of the two-phase RDW with a
heterogenous kerosene-hydrogen-air mixture are analyzed,
and the thrust performance of the RDE is estimated and
compared with experimental data under similar conditions.
Simulations at different mass ﬂow rates of kerosene are also
conducted to reveal the interactions between liquid droplets
and the two-phase RDWs.
The remainder of this paper is organized as follows: ﬁrst,
we present the numerical methods of our simulations based
on an Eulerian-Lagrangian framework for the two-phase ﬂow,
such as the governing equations, density-based solver,
chemical kinetics, boundary conditions, and mesh dis-
cretization. The next section is the main part of this paper
where we discuss and summarize the results obtained from
our simulations. Finally, we conclude the major ﬁndings in the
last section.
Methods
Gas phase
The compressible reactive Navier-Stokes equations of the
carrier phase (gas and vapor) are solved, which are coupled
with the transport equations for the reacting species,
vr
vt þ V,ðrUÞ ¼ Sm; (1)
Fig. 1 e Schematic of the RDE. Diagram redrawn from Yao
et al. [ 6]. RDW d Rotating detonation wave.
international journal of hydrogen energy 48 (2023) 33335 e3334533336

<!-- PDF_PAGE: 3 -->

vðrUÞ
vt þ V,ðrUUÞþ Vp ¼ V,bt þ Su; (2)
vðrEÞ
vt þ V,ððrE þ pÞUÞ¼ V,ðU,btÞþ V,ðKVTÞ/C0 _Q þ SE; (3)
vðrYiÞ
vt þ V,ðrYi UÞþ V,ðrDVYiÞ¼ r _ui þ SY : (4)
The density, velocity vector, pressure and temperature of the
carrier phase are denoted as r, U, p and T, respectively. The
speciﬁc total energy E is composed of the sensible internal
energy of the carrier phase and the kinetics energy of the gas-
vapor mixture. In the transport equations of species, _u
i is the
chemical reaction rate, _Q is the heat release of chemical re-
actions, Yi is the mass fraction of the species. The thermal
conductivity and mass diffusivity are deﬁned as K and D,
respectively. The viscous stress tensor is deﬁned as
bt ¼ m
/C18
ðVUÞ/C0ð VUÞT /C0 2
3 ðV,UÞI
/C19
; (5)
where g is the speciﬁc ratio, m is the dynamic viscosity given by
Sutherland's law [33]. The thermal conductivity K is computed
according to the Eucken correlation [ 34] and the mass diffu-
sivity D is obtained under the relation of D ¼ K=rCp at unity
Lewis number.
Thus far, there are not appropriate turbulence models for
supersonic reactive ﬂows like detonations, and the conven-
tionally used models for low-speed ﬂows may not be validate.
Therefore, it is still very common to directly solve the
NaviereStokes equations in the simulations of detonation
waves [ 35,36] as well as RDEs [ 11,16,37e39] under the
assumption that the effect of viscosity might not be as sig-
niﬁcant as it appears in incompressible low-speed ﬂows; but it
should not be regarded as the direct numerical simulation
(DNS) approach since the smallest scale is not resolved. Given
that the treatment of turbulence is still an open question to
the research of detonation simulations, it is beyond the scope
of the current study.
The implemented Eulerian-Lagrangian framework is a
two-way coupling model and there will be exchange of mass,
momentum, energy and transport of species between the
carrier phase and Lagrangian droplets through the source
terms of S
m, Su, SE, SY , which are formulated as
Sm ¼ 1
V
dmd
k
dt ; (6)
Su ¼/C0 1
V
d
/C0
md
kVd
k/C1
dt ; (7)
SE ¼/C0 1
V
d
/C0
md
kTd
k/C1
Cp;d
k
dt : (8)
SY ¼
(
Sm; fuel species
0; other species
(9)
The dynamics of the Lagrangian droplets under the
point-source assumption are described by the following
equations,
dXd
k
dt ¼ Vd; (10)
dVk
d
dt ¼
3CDrg
/C16
Vg /C0 Vk
d
/C17 /C12/C12 Vg /C0 Vk
d
/C12/C12
4rd
kDd
k ; (11)
dmd
k
dt ¼ pms
k Dd
k
Sc Sh ln
/C18 YF;s
k /C0 YF;g
1 /C0 YF;s
k þ 1
/C19
; (12)
dTd
k
dt ¼ pDd
k ms
kCp;s
k Nu
md
kCp;d
k Pr /C0 dmd
k
dt
hfg
k
md
kCp;d
k ; (13)
where Xd and Dd are the position and diameter of the droplet.
The Stokesian drag force is computed according to Ref. [ 40]
and the convective heat transfer is given by the model of Ranz
and Marshall [ 41,42]. Similar to previous studies such as refs.
[43,44], the liquid droplets in the dilute regime are considered,
i.e., inter-droplet interactions and droplet break-up are
neglected. The effects of droplet break-up were found to be
negligible with d
0 /C20 20 m m[ 44], whereas the inﬂuence of inter-
droplet interactions may require further investigation.
The chemical reaction of kerosene/air is modeled by a reduced
two-step mechanism (2S_KERO_BFER) [45], and hydrogen oxi-
dization is described by Marinov's one-step mechanism [46], as
summarized in Table 1. The reaction rates ki are computed ac-
cording to the Arrhenius law using the pre-exponential factors,
activation energy, and reaction exponents from the references.
Both mechanisms have been validated in the numerical simu-
lations of detonation waves. For example, in Ref. [ 47], the two-
step mechanism for kerosene-a ir combustion was validated
with experimental data [48,49] w.r.t the ignition delay time and
detonation cell, and the hydrogen oxidation mechanism was
used and validated in Ref. [50] for RDE simulations.
The simulations are performed using the ﬁnite volume
method based on the open-source OpenFOAM library (v2206)
[51]. We developed a compressible solver using the original
rhoCentralFoam which implements the central-upwind Kur-
ganov and Tadmor (KT) schemes for shock capturing. The
capability of the KT schemes to resolve the detonation wave
with sufﬁcient accuracy has been extensively validated in
numerical studies [ 38,47,52,53]. As we aim to simulate two-
phase RDWs, the Lagrangian particle tracking library is
coupled with rhoCentralFoam and the transport equations for
reacting species are solved. The inlet conditions are assumed
to be uniformly-distributed micro nozzle ﬂows, which is a
very common treatment to approximate the fuel inlet for RDE
simulations [ 38,47,50]. It will produce an injection ﬂow
depending on the inlet total pressure of the reservoir p
0 and
local pressure of the computation cell on the headwall pw.
Table 1 e Chemical kinetics of kerosene-hydrogen-air
reactions.
Reactants Chemical equations
Kerosene [ 45] KERO þ 10O20
k1
10CO þ 10H2O
CO þ 0:5O2⇔
k2
CO2
Hydrogen [ 46] H2 þ 0:5O20
k3
H2O
international journal of hydrogen energy 48 (2023) 33335 e33345 33337

<!-- PDF_PAGE: 4 -->

(1) pw /C21 p0, no injection. The inlet ﬂow properties are given by,
p ¼ pw; T ¼ T0
/C18 p
p0
/C19 g/C0 1
g
; v ¼ 0; (14)
(2) p0 > pw > pcr, subsonic inlet ﬂow. The pressure, temperature
and velocity are given by:
p ¼ pw; T ¼ T0
/C18 p
p0
/C19
g/C0 1
g ; v ¼
ﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ ﬃ
2g
g /C0 1 RT0
"
1 /C0
/C18 p
p0
/C19
g/C0 1
g
#vuut ; (15)
(3) pw /C20 pcr < p0, sonic inlet ﬂow. The pressure, temperature
and velocity are given by:
p ¼ pcr; T ¼ Tcr; v ¼
ﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ ﬃ
2g
g þ 1 RT0
s
; (16)
where T0 is the inlet total temperature, and pcr and Tcr are the
critical pressure and temperature when the inlet ﬂow is
choked
pcr ¼ p0
/C18 2
g þ 1
/C19 g
g/C0 1
; Tcr ¼ T0
/C18 2
g þ 1
/C19
: (17)
The droplets will be injected from the inlet in parcels at the
same velocity of the gaseous phase. A wave transmissive non-
reﬂecting boundary is applied to the outlet where the far-ﬁeld
condition is set to the ambient pressure and temperature of
p
∞ ¼ 0.1 MPa and T∞ ¼ 300 K, respectively.
The RDEs usually have a channel width (radial direction)
that is one order of magnitude smaller than the circumfer-
ential and axial lengths. And thus, for computational efﬁ-
ciency, it is common to treat the rotating detonation chamber
(RDC) as a two-dimensional domain where the radial direction
is neglected. To this end, the RDC is unwrapped along the
circumferential direction into a computational domain of
160 mm /C2 100 mm (see Fig. 2 ), which is equivalent to a
diameter of 50.95 mm and a chamber length of 100 mm.
Separate injectors of the fuel and oxidizer are not imple-
mented in the simulations. In the case of non-premixed in-
jection [16,54], the nonuniformity of the fuel-reﬁll zone could
lead to different combustion modes of the RDE and the phe-
nomenon of wave multiplicity.
The mesh is equally spaced along the circumferential di-
rection at Dx ¼ 100 mm. The mesh cells are stretched along the
axial direction by a constant factor, i.e. d ¼
Dymax
Dymin
¼ 10, leading
to a minimum size of Dymin ¼ 50 mm on the bottom of the RDC
for sufﬁcient resolution of the RDW. An implicit backward
scheme is implemented for time integration with an initial
time step of Dt ¼ 1e
/C0 9 s and will be automatically adjusted to
ensure CFL ¼ Dt
/C16 Pn
i¼1
uxi
Dxi
/C17
/C20 0:1.
The cell size is closely related to the existence of self-
sustained detonation wave [ 55]. Unlike gaseous hydrogen-air
detonations, there are limited data on the cell size of
kerosene-fueled detonations under wide working condition
and, what 's more, different from the working conditions of
detonation tubes, the liquid fuel is usually injected into the
RDE at high temperatures and pressures. The study of Wang &
Weng [ 56], for example, implemented a very similar working
condition to that of our study and the cell size of kerosene-air
detonations was estimated to be less than 1 mm. According to
Liu et al. [ 47], the cell size of kerosene (vapor) e air at high
temperatures (i.e. 1000 K) was about 2.86 mm. Therefore, the
dimensions of the geometry in our study, both the axial
(100 mm) and circumferential (160 mm) directions, are large
enough to allow for a sufﬁcient number of detonation cells and
to maintain the propagation of the two-phase RDW. It may be
not practical to use such kind of relatively small-sized conﬁg-
urations in the experiments, but here we focus on the physics
of the two-phase RDW and a sub-scale computation domain
should sufﬁce.
For grid sensitivity validation, the simulation of the RDE
with a premixed mixture of high-temperature kerosene vapor
and air is veriﬁed under the current resolution (Mesh-2), and is
compared with the solutions using ﬁner and coarser meshes,
i.e., Mesh-1 and Mesh-3. The results are shown in Fig. 3. It can
be seen that the main features of the RDW structure are
approximately the same, such as the wave front, the oblique
shock wave and the triangular-shaped fuel-reﬁll zone, and the
heights of the RDWs are also found to be close. In Mesh-2 and
Mesh-3, details such as the wavy structure of the shear layer
can be more clearly captured. Therefore, in consideration of
both computational efﬁciency and accuracy, Mesh-2 is used in
the remainder of this study. The total number of grid nodes in
Mesh-2 is 0.8 million and the simulation is decomposed and
parallelized on 128 cores.
Results and discussion
Operating conditions
Different from gaseous hydrogen-fueled RDEs, it is difﬁcult to
initialize the two-phase RDW by directly igniting the liquid
fuel. In the experiments, for example, the kerosene-fueled
RDEs were ignited by pre-detonators ﬁlled with hydrogen-
oxygen mixtures [ 57] or hot jets [ 29]. In the same manner,
here the RDE is ignited by a premixed stoichiometric
hydrogen-air mixture to ﬁrst obtain a gaseous rotating deto-
nation before the supply of kerosene.
A fuel mass fraction of 4
H2 ¼ _uH2 = _ufuel ¼ 27% is selected,
which falls within the range of 4H2 in the experimental study
[58]. In some previous study [ 30], the droplet size (diameter) of
the kerosene fuel is d0 ¼ 4 m m, whereas in this study we in-
crease it to 5e20 m m to account for more broad scenarios. The
hot air is supplied at a mass ﬂow rate of 0.493 kg/s at the total
temperatures of T
0 ¼ 600 K. A relatively higher T0 is needed
because according to the inlet condition Eqs. 13e16, the initial
temperature of the inlet ﬂow is pressure-dependent and will
be smaller than T0. For example, at the choking condition, T ¼
T0
/C16
p
p0
/C17 g/C0 1
g
with p < p0. The liquid droplets will be injected at an
ambient temperature of 300 K and a mass ﬂow rates of 0.02 kg/
s, corresponding to the (near) stoichiometric condition and a
global fuel-air equivalence ratio 4z 1.
Main structure
A benchmark case is ﬁrst selected to analyze the main struc-
ture of the two-phase RDW, which is Case A1 from Table 2 .
The ﬂow ﬁeld is shown in Fig. 4 where the evolution of the
international journal of hydrogen energy 48 (2023) 33335 e3334533338

<!-- PDF_PAGE: 5 -->

droplet diameter and temperature are also illustrated. The
kerosene droplets are injected at an initial diameter of 5 m m
and as they ﬂow downstream and evaporate, the droplet size
gradually decreases; however, the variation of the droplet size
in the triangular-shaped fuel-reﬁll zone is not signiﬁcant
while they are heated by the surrounding hot air stream.
Though the majority of kerosene droplets are instantly deto-
nated after being swept by the RDW, Fig. 4 a indicates that a
small portion of unburned kerosene vapor will spread along
the shear layer, which in the gaseous RDW is an interface
separating the burned products from current and the previous
cycles. Meanwhile, downstream in the fuel-reﬁll zone, a thin
layer of kerosene vapor will be deﬂagrated (non-detonation
burning) by the hot products on the deﬂagration surface
(Fig. 4 d). Overall, the main characteristics of the two-phase
RDW are analogous to those of the gaseous RDW.
As the initial droplet size increases, however, considerable
differences appear and phenomena related to droplet evapo-
ration become pronounced. It can be seen in Fig. 5a that as d
0
increases to 10 m m, a small amounts of kerosene droplets start
to permeate through the RDW front rather than being instantly
Fig. 2 e The computation domain. Unwrapped 2D view of an RDC.
Fig. 3 e Flow ﬁelds of the RDWs with a premixed kerosene (vapor)-air mixture at 4 ¼ 1 and T0 ¼ 1200 K under various
resolutions.
Table 2 e Parameters of the simulation cases.
Case T0 (K) d0 (m m) _ufuel (kg/s) 4H2 4
A1 600 5 0.027 27% z 1.0
A2 10
A3 20
international journal of hydrogen energy 48 (2023) 33335 e33345 33339

<!-- PDF_PAGE: 6 -->

detonated. At d0 ¼ 20 m m, the two-phase RDW exhibits an
evident coupled structure that has been reported in our pre-
vious study [ 6] for RDWs fueled by a heterogenous ethanol-
hydrogen-air mixture, i.e., a laminated structure caused by
droplet evaporation was revealed. As Fig. 5 shows, the coupled
structure is comprised of two reacting fronts: the ﬁrst one will
provide the ﬁrst-stage latent heat source to pre-heat the
injected liquid droplets at lower temperatures, and the second
one is maintained by the reactions of the kerosene vapor-air
mixture, which in turn will support the reacting front ahead.
Fig. 6 shows the heat release rates ( _Q) of the coupled reacting
fronts. A narrow triangle-shaped evaporation zone will exist
between the coupled reacting fronts, which is tilted in the di-
rection of the RDW because the liquid droplets downstream
are already heated by hot air and vaporize more rapidly in the
evaporation zone. In view of this and our previous study, it can
be stated that this double-reacting-front laminated structure is
a general feature of two-phase RDWs fueled by heterogenous
gas-liquid fuel mixtures, regardless of the type of fuels (kero-
sene or ethanol), and the laminated structure becomes pro-
nounced when large-size liquid droplets are injected.
Pressure-time proﬁles are obtained from the probes located
at a distance of 0.04 m from the bottom to calculate the
detonation speeds V
D of the RDWs (see Fig. 7). There is a clear
trend of detonation speed deﬁcit with the increase of the
initial droplet size, which is consistent with the experimental
observations [59,60]. Compared with the theoretical C-J values
[61], the detonation speeds of the RDWs indicate a deﬁcit
ranging from 6% to 17%. In the experimental study of Kin-
dracki [20], a detonation speed deﬁcit of 20 e25% was reported
for the two-phase RDWs fueled also by kerosene-hydrogen-air
mixtures. In view of the fact that the simulations are con-
ducted in more idealized conditions (e.g., improved mixing)
than the experiments, it is reasonable to get a smaller deto-
nation speed deﬁcit.
The fuel-based speciﬁc impulse for the two-phase RDEs is
also computed using the following formula,
I
f
spðtÞ¼ FðtÞ
_mfuel /C2 g (17)
where the thrust is determined by
FðtÞ¼
Z
outlet
/C2
rv2
e þ pout /C0 p∞
/C3
dAc (18)
and _mfuel is the sum of the fuel mass ﬂow rates of both kero-
sene _mKERO and hydrogen _mH2 [62]
_mf ¼ _mKERO þ _mH2 : (19)
Fig. 4 e Flow ﬁeld of the two-phase RDW. Case A1 (benchmark).
international journal of hydrogen energy 48 (2023) 33335 e3334533340

<!-- PDF_PAGE: 7 -->

Fig. 5 e Contours of the temperature and pressure gradient (Case A2 and A3). The formation of a coupled laminated
structure as the droplet size increases.
Fig. 6 e Heat release rates of the coupled reacting fronts (zoomed).
Fig. 7 e Variation of the detonation speed and thrust performance with droplet sizes. Theoretical C-J values computed using
Shock and Detonation Toolbox [ 61], experimental data from Bykovskii et al. [ 58].
international journal of hydrogen energy 48 (2023) 33335 e33345 33341

<!-- PDF_PAGE: 8 -->

The average fuel-based speciﬁc impulses If
sp at different d0
are shown together with the experimental results from
Bykovskii et al. [ 58]i n Fig. 7 . In the experimental research,
Bykovskii et al. estimated If
sp of kerosene-air RDEs with
different amount of hydrogen addition, i.e.,4H2 ¼ 9%, 21%, 40%,
and 100%. It was reported that the fuel-based speciﬁc impulse
increased with 4H2 ,a si ss h o w ni nFig. 7 (b). Our simulations are
conducted at 4H2 ¼ 27% with different droplet sizes, but the
Table 3 e Parameters of the simulation cases (kerosene-
rich).
Case T0 (K) d0 (m m) _ufuel (kg/s) 4H2 4
B1 700 5 0.057 13% z 1.95
B2 10
B3 12
B4 14
Fig. 8 e Contours of the temperature and pressure gradient. Occurrence of micro-explosions.
Fig. 9 e Pressure distributions of Case B2 with d0 ¼ 10 m m. The evolution of micro-explosions.
Fig. 10 e Distributions of CO during the evolution of micro-explosions (Case B2).
international journal of hydrogen energy 48 (2023) 33335 e3334533342

<!-- PDF_PAGE: 9 -->

values of If
sp fall well within the range of the experimental data,
and are very close to the measurement at 4H2 ¼ 21%. Overall,
the thrust performance of the kerosene-air RDEs agrees well
with the experimental values under similar conditions.
Kerosene-rich condition and the occurrence of micro-
explosions
Additional simulation cases are conducted for the investiga-
tion of the two-phase RDWs at kerosene-rich conditions, as
summarized in Table 3 . The mass ﬂow rate of kerosene is
doubled, whereas that of hydrogen remains the same, which
will provide a total fuel mass ﬂow rate of _u
fuel ¼ 0.057 kg/s and
4H2 ¼ 13%. Our results indicate that to achieve a stable
rotating detonation at such a high mass ﬂow rate of kerosene,
a relatively large inlet total temperature is required, i.e.,
T
0 ¼ 700 K, so that the injected droplets can be sufﬁciently pre-
heated before passing through the RDW.
At d0 ¼ 5 m m, the main features of the RDW are found to be
similar to those of Case A series except that there are un-
burned hydrogen pockets along the shear layer. As the droplet
size increases to 10 m m, the liquid droplets have a longer life
time and the structure of the two-phase RDW is signiﬁcantly
affected. The two-phase RDW starts to bend outward and
presents a bowed shape. A larger droplet size requires more
latent heat for vaporization, thus when the RDW sweeps the
droplets ahead, a portion of them are not instantly heated up
and vaporized. These droplets will ﬂow further downstream
and permeate the shear layer from the contacting point, as is
marked in Fig. 8 a. As the RDW continues to propagate, these
droplets will vaporize in the shear layer region and start to
react rapidly. This will not only interrupt the structure of the
RDW but also lead to occurrence of micro-explosions. Fig. 9
shows how the permeating droplets cause collisions of
shock waves and local explosions near the contacting point.
To clarify the induction of the micro-explosions, the evo-
lution of the intermediate species, i.e. CO, is shown in Fig. 10.
It is revealed that the formation of the intermediate CO is
closely related to the evolution of the micro-explosions, con-
ﬁrming that the penetrated droplets are herein vaporized and
reacted. The distributions of H
2 and CO2 are also plotted at the
snapshot of t 0 þ 580 m s (see Fig. 11). Prior to the occurrence of
the micro-explosions, there are unburned hydrogen streaks
origination from the contacting point and extending into the
shear layer. When the micro-explosions occur, the local
hydrogen and kerosene vapor start to react rapidly and the
reaction product of CO
2 can be observed. The occurrence of
the micro-explosions will accompany the RDW continuously
during propagation.
However, as the initial droplet size increase to 12 m m and
14 m m (Cases B3 and B4), a noticeable phenomenon is that the
micro-explosions have now developed into secondary deto-
nation waves and the transverse waves can also be observed
(see Fig. 12 ). This is because larger initial droplet sizes will
have a longer life time and the volume of unevaporated
droplets after the passage of the RDW will increase, providing
sufﬁcient chemical heat release to support a secondary deto-
nation wave near the contacting point.
Concluding remarks
Numerical simulations of the RDE fueled by liquid kerosene
with hydrogen addition a are conducted to expound the ef-
fects of droplet evaporation on the propagation and structure
of the two-phase RDW. Results suggest that with a droplet size
smaller than 10 m m, the two-phase RDW at the stoichiometric
condition reveals a structure similar to that of the gaseous
RDW; however, a laminated structure composed of coupled
detonation fronts appears when the droplet size increases
Fig. 11 e Contours of H 2 and CO 2 at t þ 580 m s when micro-explosions occur (Case B2).
Fig. 12 e Formation of secondary detonation waves with
larger droplet sizes at the fuel-rich condition (Cases B3 and B4).
international journal of hydrogen energy 48 (2023) 33335 e33345 33343

<!-- PDF_PAGE: 10 -->

further, indicating a two-stage evaporation of the droplets
after being swept by the RDW. The detonation speed of the
RDW and the thrust performance show an evident decreasing
trend with larger droplet sizes, but the estimations fall within
the reasonable ranges of the experimental data. On the other
hand, as the mass ﬂow rate of kerosene increases, a charac-
teristic micro-explosion phenomenon caused by permeating
droplets is captured. The non-fully vaporized liquid droplets
will move downstream to the contacting point of the wave
front and shear layer, and accompany the propagation of the
RDW; under the kerosene-rich condition, the micro-
explosions can develop into secondary detonation waves on
top of the primary RDW as the droplet size gets larger.
Declaration of competing interest
The authors declare that they have no known competing
ﬁnancial interests or personal relationships that could have
appeared to inﬂuence the work reported in this paper.
Acknowledgement
This work is supported by the Chinese Academy of Sciences,
Ningbo Yongjiang Talent Introduction Programme (No. 2022A-
210-G).
references
[1] Wolanski P. Detonative propulsion. Proc Combust Inst
2013;34:125e58.
[2] Raman V, Prakash S, Gamba M. Nonidealities in rotating
detonation engines. Annu Rev Fluid Mech 2023;55:639 e74.
[3] Kailasanath K, Schwer DA. High-ﬁdelity simulations of
pressure-gain combustion devices based on detonations. J
Propul Power 2017;33:153 e62.
[4] Anand V, Gutmark E. Rotating detonation combustors and
their similarities to rocket instabilities. Prog Energy Combust
Sci 2019;73:182 e234.
[5] M aJ Z ,L u a nM Y ,X i aZ J ,W a n gJ P ,Z h a n gS J ,Y a oS B ,e ta l .
Recent progress, development trends, and consideration
of continuous detonation engines. AIAA J
2020;58:4976 e5035.
[6] Yao S, Tang X, Zhang W. Structure of a heterogeneous two-
phase rotating detonation wave with ethanol ehydrogeneair
mixture. Phys Fluids 2023;35:031712 .
[7] Fotia ML, Hoke J, Schauer F. Experimental performance
scaling of rotating detonation engines operated on gaseous
fuels. J Propul Power 2017;33:1187 e96.
[8] Pal P, Kumar G, Drennan SA, Rankin BA, Som S.
Multidimensional numerical modeling of combustion
dynamics in a non-premixed rotating detonation engine
with adaptive mesh reﬁnement. J Energy Resour Technol
2021;143:112308.
[9] Sousa J, Paniagua G, Collado Morata E. Thermodynamic
analysis of a gas turbine engine with a rotating detonation
combustor. Appl Energy 2017;195:247 e56.
[10] Xia ZJ, Ma H, He Y, Ge GY, Zhou CS. Low frequency instability
in a H-2/air plane-radial rotating detonation engine. Int J
Hydrogen Energy 2022;47:5663 e76.
[11] Sato T, Chacon F, White L, Raman V, Gamba M. Mixing and
detonation structure in a rotating detonation engine with an
axial air inlet. Proc Combust Inst 2020;38:3769 e76.
[12] Zhao T, Zhu J, Ling M, Yan C, You Y. Coupling characteristic
analysis and propagation direction control in hydrogen eair
rotating detonation combustor with turbine. Int J Hydrogen
Energy 2023;48:22250 e63.
[13] Walters IV, Gejji RM, Heister SD, Slabaugh CD. Flow and
performance analysis of a natural gas-air rotating detonation
engine with high-speed velocimetry. Combust Flame
2021;232:111549.
[14] Liu S-J, Huang S-Y, Peng H-Y, Yuan X-Q. Characteristics of
methane-air continuous rotating detonation wave in hollow
chambers with different diameters. Acta Astronaut
2021;183:1e10.
[15] Peng H-Y, Liu W-D, Liu S-J, Zhang H-L, Zhou W-Y. Realization
of methane-air continuous rotating detonation wave. Acta
Astronaut 2019;164:1
e8.
[16] Prakash S, Raman V, Lietz CF, Hargus WA, Schumaker SA.
Numerical simulation of a methane-oxygen rotating
detonation rocket engine. Proc Combust Inst
2021;38:3777e86.
[17] Kumar DS, Ivin K, Singh AV. Sensitizing gaseous detonations
for hydrogen/ethylene-air mixtures using ozone and H2O2 as
dopants for application in rotating detonation engines. Proc
Combust Inst 2021;38:3825 e34.
[18] Yokoo R, Goto K, Kasahara J, Athmanathan V, Braun J,
Paniagua G, et al. Experimental study of internal ﬂow
structures in cylindrical rotating detonation engines. Proc
Combust Inst 2021;38:3759 e68.
[19] Shamshin IO, Kazachenko MV, Frolov SM, Basevich VY.
Transition of deﬂagration to detonation in
ethyleneehydrogeneair mixtures. Int J Hydrogen Energy
2022;47:16676e85.
[20] Kindracki J. Experimental research on rotating detonation in
liquid fuel-gaseous air mixtures. Aero Sci Technol
2015;43:445e53.
[21] Kindracki J, Wacko K, Wozniak P, Siatkowski S, Mezyk Ł.
Inﬂuence of gaseous hydrogen addition on initiation of
rotating detonation in liquid fuel eair mixtures. Energies
2020;13:5101.
[22] Bykovskii FA, Zhdan SA, Vedernikov EF. Continuous spin
detonation of a heterogeneous kerosene-air mixture with
addition of hydrogen. Combust Explos Shock Waves
2016;52:371e3.
[23] Salvadori M, Panchal A, Menon S. Simulation of liquid
droplets combustion in a rotating detonation engine. Proc
Combust Inst 2023;39:3063 e72.
[24] Bykovskii FA, Zhdan SA, Vedernikov EF. Continuous spin
detonation of fuel-air mixtures. Combust Explos Shock
Waves 2006;42:463 e71.
[25] Zheng Q, Meng H, Weng C, Wu Y, Feng W, Wu M.
Experimental research on the instability propagation
characteristics of liquid kerosene rotating detonation wave.
Defence Technology 2020;16:1106 e15.
[26] Zhao MH, Wang K, Zhu YY, Wang ZC, Yan Y, Wang YJ, et al.
Effects of the exit convergent ratio on the propagation
behavior of rotating detonations utilizing liquid kerosene.
Acta Astronaut 2022;193:35 e43.
[27] Zhou J, Song F, Wu Y, Xu S, Yang X, Cheng P, et al.
Investigation of pressure gain characteristics for kerosene-
hot air RDE. Combust Flame 2023;247:126102 .
[28] Meng HL, Xiao Q, Feng WK, Wu ML, Han XP, Wang F, et al.
Air-breathing rotating detonation fueled by liquid kerosene
in cavity-based annular combustor. Aero Sci Technol
2022;122:107407.
[29] Xu S, Song F, Wu Y, Zhou J, Cheng P, Yang X, et al.
Experimental investigation on combustion efﬁciency of a
international journal of hydrogen energy 48 (2023) 33335 e3334533344

<!-- PDF_PAGE: 11 -->

partially premixed kerosene-air rotating detonation
combustor. Fuel 2022;329:125418 .
[30] Ren Z, Zheng L. Numerical study on rotating detonation
stability in two-phase kerosene-air mixture. Combust Flame
2021;231:111484.
[31] Han J, Bai Q, Zhang S, Weng C. Experimental study on
propagation mode of rotating detonation wave with cracked
kerosene gas and ambient temperature air. Phys Fluids
2022;34:075127.
[32] Sun Z, Huang Y, Luan Z, Gao S, You Y. Three-dimensional
simulation of a rotating detonation engine in ammonia/
hydrogen mixtures and oxygen-enriched air. Int J Hydrogen
Energy 2022;48:4891 e905.
[33] Sutherland WLII. The viscosity of gases and molecular force.
London, Edinburgh Dublin Phil Mag J Sci 1893;36:507 e31.
[34] Svehla RA. Estimated viscosities and thermal conductivities
of gases at high temperatures. NASA; 1962 .
[35] Zhu R, Fang X, Xu C, Zhao M, Zhang H, Davy M. Pulsating
one-dimensional detonation in ammonia-hydrogen eair
mixtures. Int J Hydrogen Energy 2022;47:21517 e36.
[36] Heidari A, Wen JX. Numerical simulation of ﬂame
acceleration and deﬂagration to detonation transition in
hydrogen-air mixture. Int J Hydrogen Energy
2014;39:21317e27.
[37] Huang S, Li Y, Zhou J, Liu S, Peng H. Effects of the pintle
injector on H2/air continuous rotating detonation wave in a
hollow chamber. Int J Hydrogen Energy 2019;44:14044 e54.
[38] Zhao M, Cleary MJ, Zhang H. Combustion mode and wave
multiplicity in rotating detonative combustion with separate
reactant injection. Combust Flame 2021;225:291 e304.
[39] Meng Q, Zhao M, Zheng H, Zhang H. Eulerian-Lagrangian
modelling of rotating detonative combustion in partially pre-
vaporized n-heptane sprays with hydrogen addition. Fuel
2021;290.
[40] White FM, Majdalani J. Viscous ﬂuid ﬂow. New York:
McGraw-Hill; 2006 .
[41] Ranz WE, Marshall WR. Evaporation from drops: Part 1.
Chem Eng Prog 1952;48:141 e6.
[42] Ranz WE, Marshall WR. Evaporation from drops: Part 2.
Chem Eng Prog 1952;48:173 e80.
[43] Meng Q, Zhao N, Zhang H. On the distributions of fuel
droplets and in situ vapor in rotating detonation combustion
with prevaporized n -heptane sprays. Phys Fluids
2021;33:043307.
[44] Zhao M, Zhang H. Modelling rotating detonative combustion
fueled by partially pre-vaporized n-heptane sprays. arXiv
2020. preprint arXiv:200908617 .
[45] Franzelli B, Riber E, Sanjos /C19e M, Poinsot T. A two-step
chemical scheme for kerosene-air premixed ﬂames.
Combust Flame 2010;157:1364 e73.
[46] Marinov NM, Westbrook CK, Pitz WJ. Detailed and global
chemical kinetics model for hydrogen. In: 8th international
symposium on transport properties. Lawrence Livermore
National Laboratory; 1995
.
[47] Liu X-Y, Luan M-Y, Chen Y-L, Wang J-P. Propagation behavior
of rotating detonation waves with premixed kerosene/air
mixtures. Fuel 2021;294 .
[48] Zhukov VP, Sechenov VA, Starikovskiy AY. Autoignition of
kerosene (Jet-A)/air mixtures behind reﬂected shock waves.
Fuel 2014;126:169 e76.
[49] Zhang C, Li B, Rao F, Li P, Li X. A shock tube study of the
autoignition characteristics of RP-3 jet fuel. Proc Combust
Inst 2015;35:3151 e8.
[50] Zhao M, Li JM, Teo CJ, Khoo BC, Zhang H. Effects of variable
total pressures on instability and extinction of rotating
detonation combustion. Flow, Turbul Combust
2020;104:261e90.
[51] Weller HG, Tabor G, Jasak H, Fureby C. A tensorial approach
to computational continuum mechanics using object-
oriented techniques. Comput Phys 1998;12 .
[52] Huang X, Lin Z. Analysis of coupled-waves structure and
propagation characteristics in hydrogen-assisted kerosene-
air two-phase rotating detonation wave. Int J Hydrogen
Energy 2022;47:4868 e84.
[53] Zhu M, Jin K, Duan Q, Zeng Q, Sun J. Numerical simulation on
the spontaneous ignition of high-pressure hydrogen release
through a tube at different burst pressures. Int J Hydrogen
Energy 2022;47:10431 e40.
[54] Sato T, Raman V. Detonation structure in ethylene/air-based
non-premixed rotating detonation engine. J Propul Power
2020;36:752e62.
[55] Ciccarelli G, Dorofeev S. Flame acceleration and transition to
detonation in ducts. Prog Energy Combust Sci
2008;34:499e550.
[56] Wang F, Weng CS. Effects of divergence inlet on kerosene/air
rotating detonation engines. AIAA J 2022;60:4578 e600.
[57] Xu G, Wu YW, Xiao Q, Ding CW, Xia YQ, Li Q, et al.
Characterization of wave modes in a kerosene-fueled
rotating detonation combustor with varied injection area
ratios. Appl Therm Eng 2022;212:118607 .
[58] Bykovskii FA, Zhdan SA, Vedernikov EF. Continuous
detonation of the liquid kerosene-air mixture with addition
of hydrogen or syngas. Combust Explos Shock Waves
2019;55:589e98.
[59] Gubin SA, Sichel M. Calculation of the detonation velocity of
a mixture of liquid fuel droplets and a gaseous oxidizer.
Combust Sci Technol 2007;17:109 e17.
[60] Kailasanath K. Liquid-fueled detonations in tubes. J Propul
Power 2006;22:1261 e8.
[61] Browne S, Ziegler J, Shepherd JE. Numerical solution
methods for shock and detonation jump conditions. 2015 .
[62] Bykovskii FA, Zhdan SA, Vedernikov EF. Continuous detonation
of the liquid kerosenedair mixture with addition of hydrogen
or syngas. Combust Explos Shock Waves 2019;55:589
e98.
international journal of hydrogen energy 48 (2023) 33335 e33345 33345
