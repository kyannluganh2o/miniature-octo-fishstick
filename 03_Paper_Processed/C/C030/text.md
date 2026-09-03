<!-- PDF_PAGE: 1 -->

J. Fluid Mech. (2024), vol. 1000, A33, doi:10.1017/jfm.2024.1035
Impact of vaporization on drop aerobreakup
B. Boyd1,†,S .B e c k e r1 and Y . Ling2,†
1Department of Mechanical Engineering, University of Canterbury, Christchurch 8140, New Zealand
2Department of Mechanical Engineering, University of South Carolina, Columbia, SC 29208, USA
(Received 15 May 2024; revised 16 October 2024; accepted 23 October 2024)
Aerodynamic breakup of vaporizing drops is commonly seen in many spray applications.
While it is well known that vaporization can modulate interfacial instabilities,
the impact of vaporization on drop aerobreakup is poorly understood. Detailed
interface-resolved simulations were performed to systematically study the effect of
vaporization, characterized by the Stefan number, on the drop breakup and acceleration for
different Weber numbers and density ratios. It is observed that the resulting asymmetric
vaporization rates and strengths of Stefan ﬂow on the windward and leeward sides of
the drop hinder bag development and prevent drop breakup. The critical Weber number
thus generally increases with the Stefan number. The modulation of the boundary layer
also contributes to a signiﬁcant increase of drag coefﬁcient. Numerical experiments were
performed to afﬁrm that the drop volume reduction plays a negligible role and the Stefan
ﬂow is the dominant reason for the breakup suppression and drag enhancement observed.
Key words: breakup/coalescence, drops, condensation/evaporation
1. Introduction
Aerodynamic breakup of drops is a classical multiphase ﬂow problem commonly
encountered in various spray applications such as liquid fuel injection and spray cooling.
When the relative velocity between the drop and the surrounding gas is sufﬁciently high,
the drop deforms and may even break as it accelerates. In many atomization problems,
bulk liquids ﬁrst break into larger drops, which then undergo secondary atomization into
even smaller child droplets. In the present study, the term aerobreakup refers to any
scenario in which the drop undergoes a topology change, such as forming a hole. For
cases near the critical breakup condition, the drop may not fully atomize into a large
number of smaller droplets. For theoretical and numerical studies, drop aerobreakup is
often formulated in an idealized conﬁguration, i.e. a stationary drop suddenly exposed to
a uniform gaseous stream (O’Rourke & Amsden 1987;J a i net al. 2015, 2019; Marcotte &
Zaleski 2019;R i m b e r tet al. 2020). Experimentally, this sudden change in relative velocity
† Email addresses for correspondence: bradley.boyd@canterbury.ac.nz, stanley_ling@sc.edu
1000 A33-1
© The Author(s), 2024. Published by Cambridge University Press. This is an Open Access article,
distributed under the terms of the Creative Commons Attribution licence ( https://creativecommons.org/
licenses/by/4.0/), which permits unrestricted re-use, distribution and reproduction, provided the original
article is properly cited.
https://doi.org/10.1017/jfm.2024.1035
 Published online by Cambridge University Press

<!-- PDF_PAGE: 2 -->

B. Boyd, S. Becker and Y. Ling
is achieved using a shock wave (Hsiang & Faeth 1995; Theofanous, Li & Dinh 2004)o r
aj e t( F l o c ket al. 2012; Opfer et al. 2014; Jackiw & Ashgriz 2021). The shape evolution
and acceleration of the drop are governed by key dimensionless parameters, including the
Weber (We), Ohnesorge ( Oh) and Reynolds ( Re) numbers, and the liquid-to-gas density
ratio (η). Extensive experimental, theoretical and numerical studies have been dedicated to
investigating drop aerobreakup (Guildenbecher, López-Rivera & Sojka 2009; Theofanous
2011). In recent years, high-ﬁdelity experimental diagnostics and large-scale numerical
simulations have emerged (Jackiw & Ashgriz 2021;C h i r c oet al. 2022;L i n g&M a h m o o d
2023; Tang, Adcock & Mostert 2023), providing important details to understand the
underlying physics of interfacial multiphase ﬂow. While We is often used to characterize
different breakup modes, the effects of η (Jain et al. 2019; Marcotte & Zaleski 2019), Re
(Aalburg, Van Leer & Faeth 2003;S t r o t o set al. 2016b) and heating (Strotos et al. 2016a)
may also be important for low- We scenarios.
In applications where drop aerobreakup occurs in high-temperature environments,
such as injection of liquid fuel into combustion chambers, drop vaporization occurs
simultaneously as the drop accelerates and deforms (Strotos et al. 2016a). Phase
change is known to signiﬁcantly inﬂuence canonical interfacial instabilities, such as
Rayleigh–Taylor and Kelvin–Helmholtz instabilities (Hsieh 1978; Pillai & Narayanan
2018). Since interfacial instability plays a signiﬁcant role in drop deformation and breakup,
it is expected that vaporization can also have a substantial inﬂuence on drop aerobreakup.
However, a detailed characterization of the vaporization effect is lacking in the literature.
The vaporization of drop liquid on the surface can be driven by heat transfer as a result
of the temperature gradient or by mass transfer due to the
vapour concentration gradient.
This study focuses on the former scenario, where the rate of vaporization is determined by
the imbalance of heat ﬂuxes across the interface. This introduces additional parameters,
such as the Prandtl ( Pr)a n d Stefan ( St) numbers. Experimentally, the vaporization of a
spherical drop in high-temperature environments has been studied, resulting in commonly
used empirical relations for the drop vaporization rate (Renksizbulut & Yuen 1983;
Abramzon & Sirignano 1989). These correlations are strictly valid in the zero- We limit
and will signiﬁcantly underestimate the vaporization rate for deformable drops with ﬁnite
We (Boyd, Becker & Ling 2023; Setiya & Palmore 2023). For drops with ﬁnite We and
St, the strong coupling between drop shape deformation and vaporization complicates
the problem. On the one hand, signiﬁcant drop deformation will change the gas ﬂow
around the drop and the temperature distribution in the thermal boundary layer near
the surface, which leads to the time-varying and non-uniform distribution of the local
vaporization rate on the drop surface. However, vaporization, in particular, the asymmetric
vaporization rate on the windward and leeward sides of the drop, modulates the interfacial
dynamics and drop acceleration, which in turn change the drop deformation and the
breakup criteria. The goal of this study is to comprehensively investigate these complex
interactions between drop aerobreakup and vaporization through detailed parametric
numerical simulations. Beyond the commonly considered We, we will systematically vary
two other key dimensionless parameters, i.e. St and η, to fully characterize the vaporization
effect.
2. Methodology
To accurately predict the aerobreakup of vaporizing drops, two-phase interfacial ﬂows with
phase change must be resolved faithfully with the proper physical models and numerical
methods. The simulation approach used for the present simulations has been presented
in recent work of the authors (Boyd & Ling 2023;B o y d et al. 2023), therefore only a
1000 A33-2
https://doi.org/10.1017/jfm.2024.1035
 Published online by Cambridge University Press

<!-- PDF_PAGE: 3 -->

Impact of vaporization on drop aerobreakup
brief summary will be given here. The Navier–Stokes equations with surface tension are
solved for two-phase ﬂows using the one-ﬂuid approach. The momentum and continuity
equations are given as
ρ
(∂u
∂t + u ·∇ u
)
=− ∇ p + ∇· (2μD) + ρg + σκδγnγ, (2.1)
∇· u = sγ
( 1
ρg
− 1
ρl
)
, (2.2)
where u, p, μ, ρ, σ and κ are the velocity, pressure, dynamic viscosity, density, surface
tension coefﬁcient and interfacial curvature. The deformation tensor is deﬁned as D =
(∇ u + ∇ uT)/2. The interface normal and the interface Dirac distribution function are
denoted by nγ and δγ, respectively. The subscripts l and g refer to the liquid and gas
properties, respectively, while the subscript γ denotes properties related to the surface.
The two different phases are distinguished by the liquid volumefraction f , which follows
the advection equation with the phase-change-induced source term, i.e.
∂f
∂t + ∇· ( f u) = − sγ
ρl
. (2.3)
In (2.2)a n d( 2.3), sγ is the mass ﬂow rate per unit volume, which in turn depends on the
mass ﬂux at the interface ( jγ) and the interfacial area density ( φγ)a s
sγ = jγφγ, (2.4)
where φγ = Aγ/Vc, with Aγ the liquid–gas interface area in a cell with volume Vc. The
source term on the right-hand side of (2.2) is responsible for the generation of the Stefan
ﬂow; while the counterpart on the right-hand side of ( 2.3) accounts for the additional
change in the interface location due to phase change.
The phase change at the interface is driven by heat transfer, so jγ is determined by the
gas temperature gradient at the interface,
jγ = 1
hl,g
(kl ∇ T|l,γ · nγ − kg ∇ T|g,γ · nγ), (2.5)
where T, k and hl,g are the temperature, thermal conductivity and speciﬁc latent heat of
vaporization, respectively. The gas and liquid temperature ﬁelds required to calculatejγ are
obtained by solving the energy conservation equation for both the liquid and gas phases :
ρgCp,g
(∂Tg
∂t + u ·∇ Tg
)
= ∇· (kg ∇ Tg), (2.6)
ρlCp,l
(∂Tl
∂t + u ·∇ Tl
)
= ∇· (kl ∇ Tl), (2.7)
where Cp is the isobaric-speciﬁc heat. Since Tg and Tl are solved only in the gas and
liquid regions, the gas–liquid interface is treated as an embedded boundary where the
temperature remains as the saturation temperature Tsat.
To rigorously resolve the sharp and vaporizing interface, a novel volume-of-ﬂuid (VOF)
method was used (Boyd & Ling 2023;B o y det al. 2023). As the projection method is
1000 A33-3
https://doi.org/10.1017/jfm.2024.1035
 Published online by Cambridge University Press

<!-- PDF_PAGE: 4 -->

B. Boyd, S. Becker and Y. Ling
used to incorporate the continuity equation, the pressure Poisson equation is solved. The
volumetric source due to vaporization was added to the pressure equation to account
for the non-zero divergence of the velocity near the interface and the resulting Stefan
ﬂow. To avoid contaminating the velocity at the interfacial cells, the vaporization-induced
volumetric source is distributed to the pure gas and liquid cells adjacent to the interface
in a conservative manner. This treatment will guarantee that the velocities at the interface
cells are correctly represented and can be used directly in VOF advection. The energy
equations for both phases are solved with the Dirichlet boundary condition at the interface.
To avoid calculating the gradient across the interface, we estimate the temperature gradient
for each phase by extrapolating the
neighbouring pure cells for the corresponding phase.
The contribution of vaporization to the motion of the interface towards the liquid side is
accounted for by geometrically shifting the planar VOF interface.
The physical model and numerical methods were implemented in the open source
Basilisk solver, and the solver has been thoroughly validated to accurately simulate
two-phase interfacial ﬂows, including the aerobreakup of drops without and with phase
change (Zhang, Popinet & Ling 2020; Boyd & Ling 2023;B o y d et al. 2023;L i n g&
Mahmood 2023). A key feature of the Basilisk solver is that the quadtree/octree mesh is
used to discretize the domains, providing important ﬂexibility to dynamically reﬁne the
mesh in user-deﬁned regions. The adaptation criterion for the present study is based on
the wavelet estimate of the discretization errors of the volume fraction,
temperature and
velocity.
3. Results
3.1. Problem set-up
We consider a freely moving drop with diameter D0, initially stationary and at saturation
temperature in an unbounded domain, suddenly exposed to a uniform superheated stream
of vapour of the drop liquid with temperature T∞ and velocity U∞ ;s e eﬁgure 1(a). Using
the free-stream velocity U∞ , the initial drop radius R0 = D0/2, where D0 is the initial drop
diameter, the liquid density ρl, and the difference between the free-stream and saturation
temperatures (T∞ − Tsat) as the characteristic scales, the dimensionless variables can be
deﬁned as
u∗ = u/U∞ , x∗ = x/R0,ρ ∗ = ρ/ρl, T∗ = (T − Tsat)/(T∞ − Tsat). (3.1a–d)
Following previous works on aerobreakup, time is non-dimensionalized by the drop
breakup time (Ranger & Nicholls 1969)
t∗ = tU∞ /(D0
√
ρl/ρg). (3.2)
The deﬁnitions and values of the key dimensionless parameters, including the Weber
(We), Stefan ( St), Ohnesorge ( Oh) and Reynolds ( Re) numbers, and the liquid-to-gas
density ( η) and viscosity ( m) ratios, are provided in table 1 . The ﬂuid properties are
similar to those of acetone: the saturation temperature is Tsat = 359 K, the surface tension
is σ = 0.0153 N m− 1, the latent heat is hl,g = 4.88 × 105 Jk g − 1, and the gas density,
viscosity and thermal conductivity are ρg = 5.11 kg m− 3, μg = 9.59 × 10− 6 Pa s and
kg = 0.0166 W m− 1 K− 1, respectively. In the present study, Re = 1000, Pr = 0.84 and
m = 19.29 are kept constant, while η, We and St are varied for parametric studies. We
vary η by changing ρl, and three values, i.e. η= 139, 453 and 766, are considered,
which correspond to the density ratios from acetone ( η= 139) to ammonia ( η= 766).
1000 A33-4
https://doi.org/10.1017/jfm.2024.1035
 Published online by Cambridge University Press

<!-- PDF_PAGE: 5 -->

Impact of vaporization on drop aerobreakup
U∞ ,T∞
Inflow Outflow
L0
D0
x0
0.4t∗ = 0 0.8 1.2 1.6 2.0
0.4t∗ = 0 0.8 1.2 1.6 2.0
(b)(a)
(c)
Figure 1. ( a) Computational domain for the 3-D simulations. Morphological evolutions for ( b)
non-vaporizing (St = 0) and (c) vaporizing (St = 2) drops. The results are for η= 139 and We = 10.5.
We St Oh Re Pr η m
ρgU2
∞ D0/σ Cp,g(T∞ − Tsat)/hl,g μl/√ ρlσD0 ρgU∞ D0/μg cp,gμg/kg ρl/ρg μl/μg
1–40 0–2 0.0007–0.01 1000 0.84 139–766 19.29
Table 1. Key dimensionless parameters for the present simulations.
By varying the free-stream temperature T∞ , St changes from 0 to 2. The range of We
considered is from 1 to 40, which covers the non-breakup and bag-breakup regimes ,a n d
is sufﬁcient to identify the critical Weber number Wecr.T ov a r yWe but keep Re ﬁxed, U∞
and D0 are varied simultaneously ; as a result, Oh will vary from 7 × 10− 4 to 0.01, which
is generally small and is not expected to inﬂuence the critical Weber number (Hsiang &
Faeth 1995).
Under the non-zero relative velocity between the drop and the vapour free stream, the
drop is accelerated along the streamwise direction, while in the meantime it deforms
and vaporizes. Both two-dimensional (2-D) axisymmetric and three-dimensional (3-D)
simulations were performed, in which adaptive quadtree/octree meshes were used. The
resolution of the mesh is controlled by the level of reﬁnement, L, which corresponds to 2L
cells in a coordinate direction. For 2-D axisymmetric simulations, we have used L = 13,
and the length of the computational domain is L0 = 32D0, which gives a minimum cell
size equivalent to Δ = D0/512. For 3-D simulations, we have used a coarser mesh,
i.e. Δ = D0/256, due to the high computational cost. Grid reﬁnement studies were
conducted by varying L = 11, 12 and 13 (Δ = D0/128, D0/256 and D0/512). The results,
presented in the Appendix, conﬁrm that the mesh resolution used is sufﬁcient to accurately
resolve the vaporization of a drop undergoing signiﬁcant deformation.
3.2. Vaporization-induced breakup suppression
The key observation from the simulation results is that drop vaporization tends to stabilize
aerodynamic deformation and can suppress drop breakup. The strength of vaporization
is characterized by St, and the vaporization rate increases with St. The 3-D simulation
results for non-vaporizing (St = 0) and vaporizing (St = 2) drops are shown in ﬁgures 1(b)
1000 A33-5
https://doi.org/10.1017/jfm.2024.1035
 Published online by Cambridge University Press

<!-- PDF_PAGE: 6 -->

B. Boyd, S. Becker and Y. Ling
St = 0
St = 1
St = 2
–2
3
2
1
0
1
2
3
Rim formation
Disk
bending
forwards
t∗ = 1.2
02 0
0.14
0.290.43
0.570.71
0.86
1.00
0
75
150
(×10–6)
0.36t∗ = 0 z∗
T∗
jγ∗
r∗
η = 766
η = 453
η = 139
0.72 1.08 1.44 1.80
(b)(a)
Figure 2. ( a) Temporal evolution of the drop surfaces for different η and St. The results for η= 139, 453
and 766 correspond to We = 10.5, 12 and 12, respectively. ( b) The ﬂow ﬁeld and vaporization mass ﬂux j∗
γ =
jγ/(ρlU∞ ) (upper half) and temperature ﬁeld T∗ = (T − Tsat)/(T∞ − Tsat) (lower half) at t∗ = 1.2f o r η=
139, We = 10.5a n d St = 1.
and 1(c), respectively, with all other parameters, including η= 139 and We = 10.5, kept
unchanged. It can be observed that the non-vaporizing drop breaks at the centre, while
the vaporizing counterpart does not. The early-time shape evolutions for both drops are
quite similar. The initially spherical drop expands radially into a disk shape ( t∗ = 0.8)
due to the pressure difference between the windward pole and the periphery of the drop
(Rimbert et al. 2020). The internal radial ﬂow within the liquid causes the axial thickness
of the disk to reduce in time. The difference between the two cases arises at approximately
t∗ = 1.2, when the periphery edge of the disk starts to retract towards the centre, driven
by surface tension. The radial retraction of the vaporizing drop is faster, and due to mass
conservation, the thinning at the disk’s centre slows down, preventing the disk thickness
from diminishing to zero. As a consequence, the two surfaces of the disk do not pinch
to form a hole. In contrast, the non-vaporizing drop eventually undergoes a bag-mode
breakup, characterized by the formation of a central hole, whereas the vaporizing drop
maintains its initial topology without undergoing topological change.
We have performed the same cases using
2-D axisymmetric simulations, which yield
similar results for the present case, mainly due to the moderate Re = 1000. The less
expensive 2-D simulations will then be performed for parametric simulations varying We,
St,a n dη.
3.3. Modulation of drop surface
To conﬁrm that the vaporization-induced suppression of bag breakup is not a coincidence
for the speciﬁc density ratio η= 139 considered, additional cases η= 453 and 766 are
simulated. The time evolutions of the drop surfaces for different St and η are shown in
ﬁgure 2(a). When η increases, the dynamics of drop deformation changes, and the critical
Weber number that characterizes the onset of drop breakup, Wecr, decreases. The decrease
in Wecr with η is signiﬁcant when η ≳ 100 (Marcotte & Zaleski 2019). For the three
different η considered here, we have used We = 12 for η= 453 and 766, and We = 10.5
for η= 139, which are slightly over the corresponding Wecr. If there is no vaporization
(St = 0), then drops of all η will break in the bag mode.
1000 A33-6
https://doi.org/10.1017/jfm.2024.1035
 Published online by Cambridge University Press

<!-- PDF_PAGE: 7 -->

Impact of vaporization on drop aerobreakup
Figure 2(a) clearly shows that the vaporization-induced breakup suppression is present
for all η. The difference between the interface shapes for different St is actually larger
when η increases. As a result, the detailed mechanisms behind the stabilizing effect of
vaporization are better revealed in the cases with higher η= 453 and 766. After the
drop deforms from a sphere to a disk, a rim is formed at the periphery ;s e e t∗ = 1.08
in ﬁgure 2 (a). It is observed that the rim moves downstream faster, causing the disk to
bend forwards, and the level of bending increases with St and η. This modulation of the
drop shape is due to the asymmetric vaporization rates on the windward and leeward
sides of the rim ;s e e ﬁgure 2 (b). Since the local vaporization mass ﬂux jγ is non-zero
only in the interfacial cells (cells with fractional values of VOF), we have graphically
‘thickened’ the non-zero j
γ region in the top half of ﬁgure 2 (b) for better visualization,
from which different vaporization rates on the two sides of the rim can be clearly seen.
The vaporization rate depends on the temperature gradient near the interface, which is
in turn inversely proportional to the thickness of the thermal boundary layer near the
interface, given
that T∞ − Tsat is ﬁxed. Due to the stagnation ﬂow on the windward side,
the boundary layer thickness is much smaller than that on the leeward side where the ﬂow
separates;s e e ﬁgure 2 (b). As a result, the vaporization is signiﬁcantly stronger on the
windward side of the rim. Due to the density difference between the liquid and the vapour,
Stefan ﬂow is induced at the interface, which repels the interface in the opposite normal
direction. The higher vaporization rate on the windward side of the rim leads to a stronger
repelling force, which causes the disk to bend
forwards.
The excessive forward bending of the disk hinders bag formation and development.
As shown in previous studies on bag breakup (Ling & Mahmood 2023;T a n g et al.
2023), the bag forms when the centre of the disk becomes sufﬁciently thin, as seen at
t∗ = 1.44 for η= 766 and St = 1i n ﬁgure 2(a). The centre of the disk moves downstream
faster than the periphery, forming a bag with an upstream-facing opening, as observed at
t∗ = 1.80 for η= 766 and St = 1. Vaporization, however, modulates the drop shape in the
opposite manner, causing the edge to move downstream faster than the centre, forming
a ‘reverse bag’ with a downstream-facing opening, as seen at t∗ = 1.08 for η= 766 and
St = 2. This modulation hinders bag development. NearWecr, the force driving bag growth
(the pressure difference across the drop) is only slightly higher than the resisting force
(the surface tension on the periphery). This
unfavourable modulation by vaporization is
sufﬁcient to suppress bag development and prevent hole formation in the bag.
As the Stefan ﬂow is related to the density difference between vapour and liquid, Stefan
ﬂow and the resultant repelling force are enhanced when η increases. For the highest η=
766, vaporization results in a more signiﬁcant modulation of the shape and drag of the
drop. As a result, even a smaller St = 1 is sufﬁcient to suppress drop breakup, in contrast
to the cases for η= 139 where suppression is not observed until St = 2.
3.4. Modulation on gas ﬂow and drag
Another important effect of vaporization is the enhancement of drag and drop acceleration,
which can be observed qualitatively in ﬁgure 2(a). Detailed quantitative measurements of
the drag coefﬁcient ( Cd)a r eg i v e ni nﬁgure 3 (d). Here, the drag coefﬁcient is deﬁned
based on the instantaneous drop frontal area,
Cd = Fd
1
2ρg(U∞ − ud)2πR2
= F∗
d
1
2η(1 − u∗
d)2π(R∗)2
, (3.3)
1000 A33-7
https://doi.org/10.1017/jfm.2024.1035
 Published online by Cambridge University Press

<!-- PDF_PAGE: 8 -->

B. Boyd, S. Becker and Y. Ling
2.5
2.0
1.5
1.0
0.5
r∗
r∗
r∗
r∗
r∗
r∗
R∗
Cd
R∗
z∗
0
3
2
0
3.0
2.5
2.0
1.5
1.0
0.5
0
2.0
1.8
1.6
1.4
0.5
0.4
0.3
0.2
0.5
0.4
0.3
0.2
0.5
0.4
0.3
0.2
St = 0
St = 1
St = 2
St = 0
St = 1
St = 2
η = 139
η = 139
η = 453
η = 453
η = 766
η = 766
1.2
1.0
2.0
1.8
1.6
1.4
1.2
1.0
2.0
1.8
1.6
1.4
1.2
1.0
3.0
2.5
2.0
1.5
1.0
0.5
0
3.0
2.5
2.0
1.5
1.0
0.5
0
3.0
2.5
2.0
1.5
1.0
0.5
0
0 12
0 12 0 12 0 12
012 012 012
0 1 2 0 12 0 12 3
01 2 01 2
1
3
2
0
1
3
2
0
1
3
2
0
1
2.5
–32
ωg∗ pg∗
03 2
η = 139, St = 0
η = 453, St = 0
η = 766, St = 0 η = 766, St = 2
η = 453, St = 2
η = 139, St = 2 η = 139, St = 0
η = 453, St = 0 η = 453, St = 2
η = 766, St = 2η = 766, St = 0
η = 139, St = 2
2.0
1.5
1.0
0.5
0
2.5
–1.1 0 1.1
2.0
1.5
1.0
0.5
0
2.5
2.0
1.5
1.0
0.5
0012
z∗ z∗
t∗ t∗ t∗
t∗ t∗ t∗
z∗
012 012 012
0 1 20 1 2
(b)(a)
(d)
(c)
Figure 3. The gas ( a) vorticity ( ω∗
g = ωgR0/U∞ )a n d( b) pressure ( p∗
g = pg/(ρgU2
∞ )) ﬁelds at t∗ = 1.2f o r
different density ratios η= 139, 453, 766, and Stefan numbers St = 0 and 2. The temporal evolutions of the
drop lateral radius R∗ and the drag coefﬁcient Cd for different η and St are shown in ( c,d), respectively. The
dashed lines in ( a,b) indicate the lateral radius of the wake ( r∗
w) estimated based on vorticity.
where F∗
d = Fd/(ρlU2
∞ R2
0). While Cd varies over time, it is observed that Cd generally
increases with St; however, the detailed mechanisms behind this trend remain to be
investigated.
Since vaporization on the two sides of the rim is asymmetric, the Stefan ﬂow and the
resulting repelling force are stronger on the upstream side of the rim, leading to a net force
in the
streamwise direction, which contributes to an increase in drag in the rim region.
However, this contribution to the overall drag is expected to be minor, as vaporization on
the drop surfaces away from the edge rim is approximately symmetric ;s e e ﬁgure 2 (b).
1000 A33-8
https://doi.org/10.1017/jfm.2024.1035
 Published online by Cambridge University Press

<!-- PDF_PAGE: 9 -->

Impact of vaporization on drop aerobreakup
Another possible reason for the higher drag coefﬁcient is the larger lateral drop radius
when vaporization is present, as seen in the results for η= 453 in ﬁgure 3 (c). While
the drag on the drop will increase with R∗ and the frontal area, the drag coefﬁcient
Cd (see ( 3.3)) will not. Interestingly, for η= 139, R∗ actually decreases slightly with St
(see t∗ = 1), while Cd remains higher for larger St. Therefore, the increase in Cd when St
increases, as observed in ﬁgure 3(d), cannot be explained by the modulation of R∗ alone.
The key mechanism for drag enhancement is the modulation of the wake structure by
the Stefan ﬂow. It can be clearly observed from the vorticity ﬁelds ( ﬁgure 3 a) that the
maximum lateral radius of the wake, r∗
w, increases when vaporization is present. Near the
ﬂow separation point, the Stefan ﬂow pushes the vorticity layer away from the interface,
resulting in a larger slope of the wake boundary and eventually in a larger r∗
w. The pressure
in the wake is generally low, as shown in ﬁgure 3 (b), thus the enlargement of the wake
radius contributes to the increase of the low-pressure region area and the net drag acting
on the drop. This mechanism is similar to the drag crisis for a solid sphere, in which the
drag is reduced when the wake lateral radius decreases due to the delay of the turbulent
boundary layer separation (Tiwari et al. 2020).
Since the strength of the Stefan ﬂow is
enhanced as η increases, its modulation of the wake becomes more signiﬁcant for higher
η, as shown in ﬁgures 3(a)a n d3(b). As depicted in ﬁgure 3(a), when St increases from 0 to
2, r∗
w for η= 139 increases from 2.4 to 2.5, while for η= 453 and 766, r∗
w increases from
2.7 to 3.0 and from 2.8 to 3.3, respectively. Correspondingly, the vaporization-induced
enlargement of the low-pressure region for η= 766 is more pronounced than for η= 139;
see ﬁgure 3(b). Consequently, the increase in Cd with St is more signiﬁcant for higher η.
When St increases from 0 to 2, Cd at t∗ = 1f o rη= 766 increases by approximately 67 %,
whereas the increases for η= 453 and 139 are approximately 40 % and 5 %, respectively;
see ﬁgure 3(d).
3.5. Effects of Stefan ﬂow and interface receding
The drop vaporization results in two key modulations in interfacial dynamics: (1) the
interface receding towards the liquid, reducing the drop volume ; and (2) the Stefan ﬂow
induced by the ﬂuid volume generated near the interface that occurs when a high-density
liquid turns into a low-density vapour. While the previous discussions are focused on the
effect of the Stefan ﬂow, it remains to afﬁrm that it indeed dominates the other contribution
in the breakup suppression and drag enhancement. For this purpose, additional numerical
‘experiments’
are performed to investigate the individual effects on these two features.
Four numerical tests are performed , and the results are shown in ﬁgure 4 :( 1 ) St = 0,
where there is no vaporization; (2) St = 2-IR ( interface receding), where the interface
recedes but Stefan ﬂow is turned off; (3) St = 2-SF ( Stefan ﬂow), where Stefan ﬂow is
produced but the interface receding is turned off, so the drop volume remains unchanged;
and ﬁnally, (4) St = 2, where the full vaporization effect is incorporated. In the simulation
for St = 2-IR, the source term on the right-hand side of (2.2) is set to zero, while the source
term on the right-hand side of ( 2.3) remains unchanged. As a result, the VOF interface
recedes towards the liquid side due to vaporization, but Stefan ﬂow is not produced. For
St = 2-SF, the opposite is done: the source term on the right-hand side of ( 2.3)i ss e t
to zero , while the counterpart for ( 2.2) remains unchanged. Consequently, Stefan ﬂow
is induced, but the interface does not recede due to vaporization, and the drop volume
remains constant. It should be noted that these two cases are ‘unphysical’ and can be
examined in a numerical study only by switching vaporization-related source terms on
1000 A33-9
https://doi.org/10.1017/jfm.2024.1035
 Published online by Cambridge University Press

<!-- PDF_PAGE: 10 -->

B. Boyd, S. Becker and Y. Ling
St = 0
St = 2-IR
St = 2-SF
St = 2
St = 0
St = 2-IR
St = 2-SF
St = 2
η = 139
η = 453
η = 139 η = 139
η = 453
η = 766
η = 766
η = 453
η = 766
0.36t∗ = 0 0.72 1.08 1.44 1.80
2.0 0.5
0.4
0.3
0.2012 012
012 012
01 2 012
1.8
1.6
1.4
1.2
1.0
R
∗ Cd
0.5
0.4
0.3
0.2
Cd
0.5
0.4
0.3
0.2
Cd
2.0
1.8
1.6
1.4
1.2
1.0
R∗
2.0
1.8
1.6
1.4
1.2
1.0
R
∗
(b)(a)( c)
t∗ t∗
Figure 4. Temporal evolutions of ( a) drop surfaces, ( b) drop lateral radius R∗,a n d( c) drag coefﬁcient Cd
for different numerical tests: St = 0 represents cases without vaporization; St = 2-IR represents the numerical
tests where the interface recedes due to vaporization but the source term on the right-hand side of ( 2.2)i s
turned off to avoid the production of the Stefan ﬂow; St = 2-SF represents the numerical tests where the Stefan
ﬂow is generated due to vaporization, but the source term on the right-hand side of ( 2.3) is set to zero to avoid
interface receding towards the liquid phase due to vaporization; St = 2 represents a full simulation with both
interface-receding and Stefan ﬂow effects accounted for.
and off in different equations. However, these cases are very helpful for understanding the
individual effects of vaporization and identifying the dominant one.
For both η, the drop surfaces for St = 2-IR are very similar to those for St = 0
throughout the drop evolution ;s e e ﬁgure 4 (a). Holes are formed for both cases, leading
to a change in the drop topology. This indicates that vaporization-induced recession of
the interface and resulting volume change have minimal impact on drop deformation. In
contrast, the drop surfaces for the case St = 2-SF, with Stefan ﬂow turned on but with
the interface receding turned off , are close to the full simulation results for St = 2f o ra l l
times, and eventually the breakup is suppressed for both cases. The results for the drop
lateral radius shown in ﬁgure 4(b) are consistent, and the evolutions of R∗ for St = 0a n d
St = 2-IR are similar, while the results for St = 2-SF agree well with those for St = 2.
Therefore, we can conclude that the Stefan ﬂow is the primary effect of vaporization that
inﬂuences the drop deformation.
The drag coefﬁcient for the numerical tests is presented in ﬁgure 4 (c). The good
agreement between the results for St = 2-SF and St = 2 conﬁrms that the Stefan ﬂow
is responsible for the drag enhancement. Without incorporating the Stefan ﬂow, as in the
test St = 2-IR, one will signiﬁcantly underestimate the drag and drop acceleration.
1000 A33-10
https://doi.org/10.1017/jfm.2024.1035
 Published online by Cambridge University Press

<!-- PDF_PAGE: 11 -->

Impact of vaporization on drop aerobreakup
9
10
11
12
13
14
0 0.5 1.0 1.5 2.0
η = 139
η = 453
η = 766
Wecr
St
Breakup location
Figure 5. The critical Weber number Wecr for the aerodynamic breakup of a vaporizing drop as a function of
the Stefan number St, for different liquid-to-vapour density ratios ( η= 139, 453 and 766). The corresponding
drop surfaces upon breakup are also shown.
3.6. Impact on breakup criteria
The drop breakup criteria are often deﬁned based on the critical Weber number Wecr.
When We is lower than Wecr, the drop will remain unbroken throughout the acceleration.
Parametric 2-D axisymmetric simulations have been performed to identify Wecr for
different η and St. We have considered three values of η, and ﬁve values of St,s ot h e r ea r e
15 cases with different η–St combinations. For each case, simulations of different We are
run to ﬁnd Wecr iteratively, using a bisection method with minimum and maximum limits
We = 1 and 40, respectively. The tolerance for iteration convergence is 0.2, that is, the root
ﬁnding error for Wecr is less than 0.2. For each case, approximately 5–7 simulations are
needed to reach the desired tolerance. For all 15 cases, more than 100 runs were performed.
For some cases just above Wecr, the drop lateral radius R∗ is decreasing when the
drop breaks at the centre. Those drops will eventually return to the ellipsoidal shape and
will not atomize into a large number of child droplets. Such a near- Wecr behaviour has
been identiﬁed in previous studies as well (Ling & Mahmood 2023). We considered the
formation of a hole in the drop bag to also be a breakup case to give a robust criterion for
determining Wecr.
The results of Wecr for differentηand St are summarized in ﬁgure 5. For non-vaporizing
drops ( St = 0), Wecr = 9.8, 10. 9 and 11.4 for liquid-to-gas density ratios η= 139, 453
and 766, respectively. Experimental measurements for Wecr available in the literature
are mainly for non-vaporizing drops with large η,a n d Wecr ≈ 11 for water drops in air
(η= 831) (Guildenbecher et al. 2009). Therefore, our results for Wecr agree well with
the experimental data in the literature. Furthermore, the present results show that Wecr
decreases slightly with η, which is also consistent with previous studies on the density
ratio effect (Jain et al. 2019; Marcotte & Zaleski 2019). To the best knowledge of the
authors, there are no experimental measurements for Wecr for vaporizing drops. Since
vaporization tends to stabilize the drop, Wecr generally increases with St, meaning that a
higher gas dynamic pressure is required to break the drop. It was found that Wecr increases
by approximately 13 % for η= 766 when St increases from 0 to 2.
1000 A33-11
https://doi.org/10.1017/jfm.2024.1035
 Published online by Cambridge University Press

<!-- PDF_PAGE: 12 -->

B. Boyd, S. Becker and Y. Ling
The drop shapes upon breakup at the corresponding Wecr are also shown in ﬁgure 5 ,
where it can be observed that vaporization modiﬁes the drop shape at the point of breakup.
As expected, the breakup outcomes, including the velocity and size distributions of the
resulting child droplets, will also change. However, a detailed study of the child droplet
statistics is beyond the scope of the present work.
Although the general increasing trend of We
cr with St holds for all density ratios, a closer
examination reveals that the variations in Wecr depend on η.F o rη= 139, Wecr increases
approximately linearly as St increases, and the drop shapes remain similar. In contrast, the
variation of Wecr for higher ηis more complex. Speciﬁcally, forη= 453, Wecr shows little
change within the searching tolerance 0.2 for St values between 0.5 and 1.5. In these cases,
vaporization delays the breakup and modiﬁes the drop shape at the point of breakup, but
it is not sufﬁcient to suppress the breakup. For η= 453, the breakup time for St = 1.0i s
t∗ = 1.907, which increases to 1.925 for St = 1.5, while Wecr for these two cases remains
almost the same.
For η= 766, although Wecr increases monotonically with St, similar to the trend
observed for η= 139, the drop shape upon breakup varies more signiﬁcantly with changes
in St. While the shape for the non-vaporizing case ( St = 0) at η= 766 closely resembles
that of its lower- η counterparts, the drop experiencing strong vaporization, such as at
St = 2, displays a very different breakup shape, deforming into a long bag along the
streamwise direction. For low St values, the drop at η= 766 breaks in a typical bag mode
by pinching the two interfaces and forming a hole near the axis, similar to what occurs for
lowerηvalues, which is expected when We ≈ We
cr.H o w e v e r ,a sSt increases, the pinching
location shifts away from the axis, and the breakup morphology appears to shift towards
a bag-stem mode, though a more detailed investigation would be required to conﬁrm this
observation.
Finally, it is noted that the
variations of Wecr discussed above are strictly valid for
the current range of parameters considered, namely 139 ⩽ η ⩽ 766 and 0 ⩽ St ⩽ 2.
Extension of the present study to higher St and ambient temperature will be relegated
to our future work.
4. Conclusions
Parametric 3-D and 2-D axisymmetric interface-resolved simulations are conducted in
the present study to investigate the aerobreakup of vaporizing drops. The Weber and
Stefan numbers, and the liquid-to-gas density ratio, are varied to systematically study the
effect of vaporization on the drop deformation/breakup and drag. For a wide range of
liquid-to-density ratios, vaporization contributes to hindering the drop deformation
, and
if the Stefan number is sufﬁciently high, can suppress bag breakup. The vaporization
also contributes to enhancement of the drag: it is shown that the drag coefﬁcient for
a vaporizing drop can be 84 % higher than its non-vaporizing counterpart. The Stefan
ﬂow induced by the interface vaporization plays the dominant role in modulations of the
drop deformation stabilization and drag enhancement. The asymmetric vaporization rates
on the windward and leeward sides of the edge rim and the resulting different strength
of Stefan ﬂow cause the disk to deform in
an opposite manner compared to the bag,
which hinders the bag development and breakup. The Stefan ﬂow modiﬁes the boundary
layer dynamics near the separation point, leading to a wider wake and a large drag. More
than
100 simulations were run to identify the critical Weber number for different Stefan
numbers and density ratios. When the Stefan number increases from 0 to 2, the critical
Weber number can increase up to 13 %.
1000 A33-12
https://doi.org/10.1017/jfm.2024.1035
 Published online by Cambridge University Press

<!-- PDF_PAGE: 13 -->

Impact of vaporization on drop aerobreakup
L = 11
L = 12
L = 13
0
50
jγ∗ × 106
100
150
200
250
300
350
400
0
50
100
150
200
250
300
350
400
–1.0 –0.5 0
cos(θ)
0.5 1.0 –1.0 –0.5 0
cos(θ)
0.5 1.0
t∗ = 0.72 t∗ = 1.08
0.36t∗ = 0 0.72 1.08 1.44 1.80
θ
(b)
(a)
(c)
Figure 6. ( a) Temporal evolution of the drop surfaces for different mesh reﬁnement levels L = 11, 12 and 13,
for the case η= 139, We = 10.5a n d St = 2. ( b,c) Distribution of the vaporization mass ﬂux jγ on the drop
surface for t∗ = 0.72 and 1.08, respectively.
Funding. This research was supported by ACS-PRF (no. 62481-ND9) and NSF (no. 1942324). We also
acknowledge the ACCESS program for providing the computational resources that have contributed to the
research results reported in this paper. The code used for the present simulations is an extension of the
open-source multiphase ﬂow solver Basilisk, which is made available by S. Popinet and other collaborators.
Declaration of interests. The authors report no conﬂict of interest.
Author ORCID.
Y . Linghttps://orcid.org/0000-0002-0601-0272.
Appendix. Grid reﬁnement studies
Grid reﬁnement studies for non-vaporizing drops can be found in our previous paper
(Ling & Mahmood 2023). The results of grid reﬁnement studies for a vaporizing drop
(η= 139, We = 10.5 and St = 2) are shown in ﬁgure 6. This case represents a drop with
strong vaporization and high St in the present study. Three different reﬁnement levels,
L = 11, 12 and 13, corresponding to 128, 256 and 512 cells per initial drop diameter, are
used. The time evolution of the drop surface for different meshes is shown in ﬁgure 6(a),
where it can be observed that the results for different meshes are almost indistinguishable
until t
∗ = 1.08. At later times, the results for L = 12 and 13 remain very close. The
distribution of vaporization mass ﬂux j∗
γ on the drop surface at t∗ = 0.7 2a n d1 . 0 8i ss h o w n
in ﬁgures 6(b)a n d6(c). Here, j∗
γ is plotted as a function of cos θ, where θ is the colatitude
on the drop surface with respect to the origin, which is in the middle between the windward
and leeward poles (see t
∗ = 0.72 in ﬁgure 6a). Again, the results for L = 1 2a n d1 3a g r e e
very well, conﬁrming that the mesh resolution (L = 13 or D0/Δ = 512) used in the present
study is sufﬁcient to resolve the interfacial dynamics when vaporization is present.
1000 A33-13
https://doi.org/10.1017/jfm.2024.1035
 Published online by Cambridge University Press

<!-- PDF_PAGE: 14 -->

B. Boyd, S. Becker and Y. Ling
REFERENCES
AALBURG ,C . ,V AN LEER ,B .&F AETH , G.M. 2003 Deformation and drag properties of round drops
subjected to shock-wave disturbances. AIAA J. 41 (12), 2371–2378.
ABRAMZON ,B .&S IRIGNANO , W.A. 1989 Droplet vaporization model for spray combustion calculations.
Intl J. Heat Mass Transfer 32 (9), 1605–1618.
BOYD ,B . ,B ECKER ,S .&L ING , Y. 2023 Simulation and modeling of the vaporization of a freely moving and
deforming drop at low to moderate Weber numbers. Intl J. Heat Mass Transfer 218, 124735.
BOYD ,B .&L ING , Y. 2023 A consistent volume-of-ﬂuid approach for direct numerical simulation of the
aerodynamic breakup of a vaporizing drop. Comput. Fluids 254, 105807.
CHIRCO , L., M AAREK ,J . ,P OPINET ,S .&Z ALESKI , S. 2022 Manifold death: a volume of ﬂuid
implementation of controlled topological changes in thin sheets by the signature method. J. Comput. Phys.
467, 111468.
FLOCK , A.K., G UILDENBECHER , D.R., C HEN ,J . ,S OJKA , P .E. & B AUER , H.-J. 2012 Experimental
statistics of droplet trajectory and air ﬂow during aerodynamic fragmentation of liquid drops. Intl J.
Multiphase Flow 47, 37–49.
GUILDENBECHER , D.R., L ÓPEZ -RIVERA ,C .&S OJKA , P.E. 2009 Secondary atomization. Exp. Fluids
46 (3), 371.
HSIANG , L.-P . & F AETH , G.M. 1995 Drop deformation and breakup due to shock wave and steady
disturbances. Intl J. Multiphase Flow 21, 545–560.
HSIEH , D.Y. 1978 Interfacial stability with mass and heat transfer. Phys. Fluids 21, 745–748.
JACKIW ,I . M .&A SHGRIZ , N. 2021 On aerodynamic droplet breakup. J. Fluid Mech. 913, A33.
JAIN ,M . ,P RAKASH , R.S., T OMAR ,G .&R AV I K R I S H N A, R.V. 2015 Secondary breakup of a drop at
moderate Weber numbers. Proc. R. Soc. Lond. A 471 (2177), 20140930.
JAIN , S.S., T YAGI ,N . ,P RAKASH , R.S., R AV I K R I S H N A,R . V .&T OMAR , G. 2019 Secondary breakup of
drops at moderate Weber numbers: effect of density ratio and Reynolds number. Intl J. Multiphase Flow
117, 25–41.
LING ,Y .&M AHMOOD , T. 2023 Detailed numerical investigation of the drop aerobreakup in the bag breakup
regime. J. Fluid Mech. 972, A28.
MARCOTTE ,F .&Z ALESKI , S. 2019 Density contrast matters for drop fragmentation thresholds at low
Ohnesorge number. Phys. Rev. Fluids 4 (10), 103604.
OPFER , L., R OISMAN , I.V ., V ENZMER ,J . ,K LOSTERMANN ,M .&T ROPEA , C. 2014 Droplet–air collision
dynamics: evolution of the ﬁlm thickness. Phys. Rev. E 89, 013023.
O’R OURKE ,P . J .&A MSDEN , A.A. 1987 The TAB method for numerical calculation of spray droplet breakup.
Tech. Rep. LA-UR-2105. Los Alamos National Laboratory.
PILLAI ,D . S .&N ARAYANAN , R. 2018 Rayleigh–Taylor stability in an evaporating binary mixture. J. Fluid
Mech. 848,R 1 .
RANGER ,A . A .&N ICHOLLS , J.A. 1969 Aerodynamic shattering of liquid drops. AIAA J. 7, 285–290.
RENKSIZBULUT ,M .&Y UEN , M.C. 1983 Experimental study of droplet evaporation in a high-temperature
air stream. Trans. ASME J. Heat Transfer 105, 384–388.
RIMBERT ,N . ,C ASTRILLON ESCOBAR ,S . ,M EIGNEN ,R . ,H ADJ -ACHOUR ,M .&G RADECK , M. 2020
Spheroidal droplet deformation, oscillation and breakup in uniform outer ﬂow. J. Fluid Mech. 904,A 1 5 .
SETIYA ,M .&P ALMORE ,J . A .J R 2023 Quasi-steady evaporation of deformable liquid fuel droplets. Intl J.
Multiphase Flow 164, 104455.
STROTOS ,G . ,M ALGARINOS ,I . ,N IKOLOPOULOS ,N .&G AVA I S E S,M .2 0 1 6a Aerodynamic breakup of an
n-decane droplet in a high temperature gas environment. Fuel 185, 370–380.
STROTOS ,G . ,M ALGARINOS ,I . ,N IKOLOPOULOS ,N .&G AVA I S E S,M .2 0 1 6b Numerical investigation of
aerodynamic droplet breakup in a high temperature gas environment. Fuel 181, 450–462.
TANG ,K . ,A DCOCK ,T .&M OSTERT , W. 2023 Bag ﬁlm breakup of droplets in uniform airﬂows. J. Fluid
Mech. 970,A 9 .
THEOFANOUS , T.G. 2011 Aerobreakup of Newtonian and viscoelastic liquids. Annu. Rev. Fluid Mech.
43, 661–690.
THEOFANOUS , T.G., L I,G . J .&D INH , T.-N. 2004 Aerobreakup in rareﬁed supersonic gas ﬂows. Trans.
ASME J. Fluid Engng 126, 516–527.
TIW ARI, S.S., P AL , E., B ALE ,S . ,M INOCHA ,N . ,P ATW ARDHAN , A.W ., NANDAKUMAR ,K .&J OSHI ,J . B .
2020 Flow past a single stationary sphere, 2. Regime mapping and effect of external disturbances. Powder
Technol. 365, 215–243.
ZHANG ,B . ,P OPINET ,S .&L ING , Y. 2020 Modeling and detailed numerical simulation of the primary
breakup of a gasoline surrogate jet under non-evaporative operating conditions. Intl J. Multiphase Flow
130, 103362.
1000 A33-14
https://doi.org/10.1017/jfm.2024.1035
 Published online by Cambridge University Press
