<!-- PDF_PAGE: 1 -->

Numerical study of the near-ﬁeld of highly underexpanded
turbulent gas jets
Alexey Velikorodny *, Sergey Kudriakov 1
CEA-Saclay, DEN, DANS, STMF, LATF, F-91191 Gif-sur-Yvette, France.
article info
Article history:
Received 7 December 2011
Received in revised form
3 May 2012
Accepted 27 May 2012
Available online 9 July 2012
Keywords:
Underexpanded jets
Mach disk
Turbulence
Notional nozzle
LES
Hydrogen safety
abstract
For safety issues related to the storage of gases (e.g. hydrogen) under high pressure, it is
necessary to determine how the gas is released in the case of failure. In particular, there exist
limited quantitative information on the near-ﬁeld properties of gas jets, which are important
for establishing proper decay laws in the far-ﬁeld. Simulations of the near-ﬁeld of highly
underexpanded (high pressure) gas jets have been performed using Finite-Volume solver of
the CAST3M code and validated using several sources available in the literature. The
numerical model solves the 3D Compressible Multi-Component Navier eStokes equations
directly without relying on the compressibility-corrected turbulence models. It provides
sufﬁciently fair mean predictions both in the case of one-component air eair and two-
component helium-air releases. Possible initial conditions for the far-ﬁeld simulations are
suggested in terms of distance from the source, as well as the turbulence characteristics and
gas-dynamic parameters at this location. In addition, these results are used to evaluate
several notional nozzle concepts in order to determine the one physically consistent.
Copyright ª 2012, Hydrogen Energy Publications, LLC. Published by Elsevier Ltd. All rights
reserved.
1. Introduction
In aerospace and industrial applications, sonic and supersonic
jets are often encountered. In particular, an accidental
discharge of a high-pressure gas (e.g. hydrogen) to atmosphere
from a small opening in a reservoir can result in under-
expanded sonic/supesonic jet (pressure at the exit is much
greater than atmospheric). In these cases, knowledge of the
temperature and ﬂammable gas concentration are important
in order to suggest the appropriate safety standards. However,
there exist very limited quantitative information on the near-
ﬁeld properties of gas jets, as a result of great challenges of ﬂow
measurements and simulation in the supersonic/subsonic
shock-structured regions. Therefore, in literature currently
there exist various simplifying approaches.
The group of authors, including Birch et al. [1], [2], Ewan
and Moodie [3], Yuceil and Otugen [4], among others, provided
several types of scaling laws for velocity, temperature and/or
concentration irrespective of the particulars in the initial
expansion of the underexpanded jet by using the notional
nozzle concept. Birch et al. [1] developed this concept based on
the ideal gas law, the equation of conservation of mass
between the choked ﬂow through the actual nozzle and
a sonic ﬂow through the notional nozzle. In addition,
a uniform velocity proﬁle and atmospheric temperature were
assumed after the jet expansion region. Yuceil and Otugen [4],
among others, attempted to advance the original concept by
introducing the momentum and energy equations. This
analysis provides the gas properties such as temperature and
density at the notional location.
* Corresponding author . Tel.: þ33 (0) 1 69 08 10 81; fax.: þ33 (0) 1 69 08 82 29.
E-mail addresses: alexey.velikorodny@cea.fr (A. Velikorodny), sergey.kudriakov@cea.fr (S. Kudriakov).
1 Tel.: þ33 (0) 1 69 08 52 85.
Available online at www.sciencedirect.com
journal homepage: www.elsevier.com/locate/he
international journal of hydrogen energy 37 (2012) 17390 e17399
0360-3199/$ e see front matter Copyright ª 2012, Hydrogen Energy Publications, LLC. Published by Elsevier Ltd. All rights reserved.
http://dx.doi.org/10.1016/j.ijhydene.2012.05.142

<!-- PDF_PAGE: 2 -->

Despite this progress, the notional nozzle does not neces-
sarily exist in the physical sense and, thus, the aforemen-
tioned models are to be further validated and/or reﬁned. In
particular, it has been shown (e.g. Chenoweth [5]) that the
ideal gas law overestimates the hydrogen/helium mass
release by a signiﬁcant amount for a very high pressure
storage. Another problem rises from the assumption that
there is no entrainment of the stationary ﬂuid into the shear
layer during the expansion. Therefore, an approach alterna-
tive to the notional nozzle, was recently suggested by Xu et al.
[6]. In this work axisymmetric Navier eStokes equations with
k /C0 u model were solved in the near-ﬁeld of the highly
underexpanded hydrogen jet. The results of this computation
were analyzed to ﬁnd a critical distance from the nozzle,
where they considered to be suitable for the subsequent
simulations of the far-ﬁeld. However, neither attempt to
deﬁne a criteria for this distance, nor validation of the
computation have been performed.
Previous numerical studies of the unsteady highly under-
expanded gas jets were two-dimensional in their nature in
order to provide high-ﬁdelity transient computations of the
shock waves and ﬂow structures in the near-ﬁeld (e.g. Ishii
et al. [7],P e` neau et al. [8], among others). Pe ` neau et al. [8]
studied both the one-component and two-component
(hydrogen-air) releases. However, a total time of these
computations was rather limited and thus a quasi steady state
has not been reached. In the case of Reynolds-averaged
NaviereStokes equations (RANS) simulations some of the
authors (Chauveau et al. [9], Lehnasch [10]) utilized turbulence
models with compressibility correction of Sarkar et al. [11],
which is limited to isotropic turbulence scenario.
Taking into account the outlined limitation of the previous
studies, it was attempted in this paper to solve 3 D
Compressible Multi-Component Navier eStokes equations in
the near-ﬁeld of highly underexpanded gas jets with the
particular emphasis on experimental validation of the
numerical model. The following background section gives
a short review of theoretical and experimental studies, as well
as lists the major objectives of the present work.
2. Background
2.1. Shock-wave structure
The major parameter utilized in the past to classify free
underexpanded jet, discharging to atmosphere is the pressure
ratio P
0=PN, where P0 is a stagnation pressure in the tank and
PN is an ambient pressure (Ashkenas and Sherman [12]).
However, it has been also shown (see Bier and Schmidt [13],
Crist et al. [14]), that the shock-wave structure in these jets
also depends on a geometry of the nozzle and the nature of
gas. As the ﬂow leaves the nozzle the high pressure mismatch
causes it to expand and accelerate. Expansion waves originate
near the expansion point, propagate and meet the outer
boundary of the jet, where they are reﬂected as compression
waves. Coalescence of these waves results in a curved barrel
shock surrounding the immediate supersonic region (a sche-
matic describing the process can be found in the studies cited
above). For higher values of P
0=PN ð> 15Þ, which are
considered herein, the shock structure is rather complex. The
reﬂection of the incident shock is not regular anymore, and
a so-called Mach disk pattern appears a few diameters
downstream the oriﬁce. The ﬂow is subsonic just after the
Mach disk, while it remains supersonic downstream of the
barrel shock. The triple point connects various discontinuities
and becomes the origin of a new slip line, which gives rise to
a supersonic shear layer. The lengths of the shock cell and
subsonic zone are increasing functions of pressure ratio
and exit Mach number, while the diameter of the Mach
disk depends signiﬁcantly on g (Bier and Schmidt [13],
Crist et al. [14]).
In view of the latter, and in the context of an accidental
discharge of high-pressure hydrogen (or helium), a theoretical
analysis based on dimensional groups has been developed in
Ref. [15]. It was shown, in particular, that
Xm
De
¼ 1
2
ﬃﬃﬃgp
ﬃﬃﬃﬃﬃﬃ ﬃ
Pe
PN
s
/C2
/C18 g þ 1
g /C0 1
/C19 1=4
(1)
Dm
De
¼ a Xm
De
ﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ
1 /C0 g þ 1
g /C2
/C18 g þ 1
g /C0 1
/C19 /C0 1=2
s
(2)
where Xm and Dm are location and diameter of the Mach
disk, Pe is a static pressure at the exit section, and a is an
empirical constant, which accounts for the growth of the
mixing layer. The latter can be for instance approximated, at
the location of the Mach disk, using experimental measure-
ments of Bier and Schmidt [13] provided for various gases,
including hydrogen. It should be also noted, that the Mach
disk location, X
m as given by Eqn. (1), is in fact weakly
dependent on g, and is well approximated by a commonly
used experimental correlation of Ashkenas and Sherman [12]:
Xm
De
¼ 0:67 /C2
ﬃﬃﬃﬃﬃﬃ ﬃ
P0
PN
s
.
2.2. Quantitative measurements and validation
techniques
Quantitative measurements in the near-ﬁeld of under-
expanded jets are scarce due to the highly complex nature of
the ﬂow. Most of the early experimental data in the near-ﬁeld
was obtained using impact techniques. For example, Glotov
[16] utilized probes immediately after the Mach disk to
determine the length of the subsonic core ðL
sÞ. Correlation (3),
thus obtained, can be used for Pe=PN /C20 30.
Ls
Dm
¼ 1:96 /C2
/C18 Pe
PN
/C19 /C0 0:16
(3)
The essentially non-intrusive methods such as particle
image velocimetry (PIV) show some promise for the quanti-
tative characterization of supersonic jets as it has been
demonstrated by Chauveau et al. [9] and Yuceil et al. [17].
However, a dramatic particle inertia effect was found to exist
just downstream of the Mach disk. For example, recent PIV
measurements of a hydrogen jet release of Veser et al. [18]
provide velocity data only beyond the shock-structured
region (i.e. > 25D
e in the case of P0 ¼ 19:2 -bar).
international journal of hydrogen energy 37 (2012) 17390 e17399 17391

<!-- PDF_PAGE: 3 -->

Planar laser-induced ﬂuorescence (PLIF) was used in the
experiments designed by Wilke et al. [19]. Although, the PLIF
images provide only qualitative spatial information regarding
the structure of supersonic jets, it was demonstrated that
supersonic shear layers exhibit relatively low growth rates
and appear parallel many diameters downstream.
Recently, a large set of density/concentration measure-
ments of the vertical turbulent subsonic and supersonic
helium jets was performed by Dubois [20] using Background
Oriented Schlieren (BOS) technique. The covered ﬁeld from
the nozzle exit up to 200 D
e and stagnation-to-ambient pres-
sure ratios as large as 120 were considered. Several ﬁelds-of-
view (FOV) and physical resolutions (PR) were employed,
which allowed for high resolution of both the near and far-
ﬁelds. These parameters are given in Table 1 and will be
referred as such henceforward.
One of the particular ﬁndings of this work, which is in line
with the results of e.g. Wilke [19], is that the potential core
length ( X
p - position at the centerline, where mixing layers
merge) of the highly underexpanded jet is relatively large
compared to the ones ideally expanded. An empirical corre-
lation provided by this study approximates the length of the
potential core as follows:
X
p ¼ 8 /C2 Xm (4)
It should be noted, however, that this expression was ob-
tained based on density measurements only, while both the
pressure and temperature were assumed to be atmospheric
throughout the development region.
2.3. Unresolved issues and objectives
Current industrial standard is to store hydrogen under pres-
sure as high as 700-bar and, apparently, it would be an ideal
case to consider numerically as an accidental release scenario.
However, several fundamental issues exist to date and are
listed below:
1) to the best knowledge of the authors, insofar, there exist no
quantitative measurements in the near-ﬁeld (starting from
the nozzle exit) of such a very high-pressure hydrogen/
helium release to be used for validation of numerical models.
2) Unsteady high-resolution 3 D simulations on a sufﬁciently
large domain of jets issuing from very high-pressure sources
require a prohibitive amount of computational resources.
3) the notional nozzle concepts, which might have been
a useful simpliﬁcation for these type of releases, them-
selves require further validation and/or reﬁnement.
The aim of the present paper is, insofar, to avoid or try to
resolve these issues. The list of objectives is, thus, summa-
rized as follows:
1) The high-resolution quantitative BOS measurements in the
near-ﬁeld of highly underexpanded gas jets are going to be
utilized for validation of the numerical model. The high-
pressure helium jet measurements of Dubois [20] in the
range from 0 D
e up to 200 De were found to be appropriate. It
should be noted, that although helium can not fully replace
hydrogen in the experiments or simulations, it has rather
similar physical and dynamical properties, and might be
reasonably applied especially in those situations, where
their great chemical difference is not a concern.
2) The purpose of this work is to perform the high-resolution
3D unsteady simulations of the near-ﬁeld of highly under-
expanded jet in order to develop a methodology, which
deﬁnes the location and boundary conditions for the
subsequent far-ﬁeld modeling. A validation case of 30-bar
has been, therefore, chosen, because it provides a reason-
able balance between the order of pressurization and the
size of the computational domain to be considered (i.e. for
pressures as high as 700-bar the Mach disk position, as well
as the potential and development zones might be prohibi-
tively great for a typical test case).
3) These results are used to evaluate several notional nozzle
concepts by associating them with a physical location in
space. This work provides further insight into application
of these laws to model high-pressure jets corresponding to
the industrial standards.
4) Moreover, the results of such simulations might be utilized
in future in order to improve relations for the potential core
length and consequently the virtual origin of a typical high-
pressure jet.
3. Governing equations and numerical
modeling
3.1. Compressible multi-component Navier eStokes
equations
The viscous ﬂow of a Newtonian multi-component ﬂuid of N
species is governed by the Navier eStokes equations which
express the conservation of total mass (without source of
mass), the mass conservation for species k ðk ¼ 1; .; N /C0 1Þ,
conservation of momentum and energy [21],
vr
vt þ V
/
$ðr u!Þ¼ 0 (5)
vrYk
vt þ V
/
$ðrð u! þ V!
kÞYkÞ¼ 0 (6)
vr u!
vt þ V
/
$ðr u!5 u! þ PIÞ¼ V
/
$ s þr g! (7)
vret
vt þ V
/
$ðr u!htÞ¼ V
/
$ð s $ u! /C0 q!Þþ r g!$ u! (8)
The gas jet is considered to be either helium or air, with the
pressure, temperature and density being coupled using the
ideal gas law. The mass fractions Y
k, ðk ¼ 1; .; NÞ, the species
density rk and the mixture density are related by: Yk ¼ rk=r
and Fick’s law is used for the diffusion velocity V!
k of species k
Table 1 e Deﬁnition of the FOVs and corresponding
resolutions of BOS experiments [20].
12 3
FOV, mm 11 /C2 9.8 70 /C2 30 200 /C2 112
PR, mm/pix 21.3 108.2 201.5
international journal of hydrogen energy 37 (2012) 17390 e1739917392

<!-- PDF_PAGE: 4 -->

Vk;i Yk ¼/C0 Dk
vYk
vxi
(9)
with Dk being the diffusion coefﬁcient of species k into the
mixture. Following Stokes’ hypothesis, the viscous shear
stress tensor
s is given by:
sij ¼ m
/C18 vui
vxj
þ vuj
vxi
/C0 2
3dij V
/
$ u!
/C19
(10)
and the energy ﬂux is
qi ¼/C0 l vT
vxi
/C0 r
XN
k¼1
hkDk
vYk
vxi
(11)
This ﬂux includes a heat diffusion term expressed by
Fourier’s law and a second term associated with the diffusion
of species with different enthalpies. The standard notations
are used for the speciﬁc total energy, e
t, speciﬁc total
enthalpy, ht and speciﬁc internal enthalpy for the species k
ðk ¼ 1; .; NÞ, hk.
3.2. Numerical discretization and turbulence treatment
The system of Eqns (5)e(8) is solved using Finite Volume
approach developed in the CAST3M code. The approximate
Riemann-type methods are used for convective ﬂuxes, which
are either the van Leer splitting [22] or the advection upstream
splitting “AUSM þ” [23] methods. The “diamond”- type
approach is employed for approximation of the diffusive
ﬂuxes [24]. Overall, these explicit schemes have a second
order accuracy both in time and space.
Although a few eddy viscosity-type turbulence models are
realized in the CAST3M, an alternative approach is employed
in view of complexity of the problem, as well as thanks to
monotonicity of the numerical schemes used. Present
numerical model directly solves the governing equations
without relying onto the subgrid-scale (SGS) turbulence
models. Thus, the largely controversial SGS models, especially
those with compressibility-corrected terms [11] (with more
calibrating constants), can be avoided. However, the numeri-
cally generated dissipation inherent with a numerical algo-
rithm has been shown to be rather effective SGS turbulence
model for high-resolution simulations in many other inves-
tigations, including the work of Boris et al. [25], where the so-
called MILES (Monotonically Integrated LES) approach has
been described in detail.
3.3. Computational domain and grid
Gas release from a 30-bar pressure tank has been considered.
The corresponding release velocities at the exit ðM
e ¼ 1Þ were
322 m=s and 892 m/s for air and helium, respectively. The ﬂow
ﬁeld was initialized with an air at 1 atm and the temperature
of 300 K. The diameter of the opening ðD
eÞ was ﬁxed to be
1 mm, which gives the Reynolds numbers well beyond 10 5 for
both considered cases and, thus, the mixing layer is expected
to become turbulent shortly after the release. However,
a laminar velocity proﬁle is assumed at the inﬂow. All gas-
dynamic parameters at the oriﬁce, where the ﬂow is
prescribed to be choked, were calculated from the stagnation
pressure and temperature using the ideal gas law (e.g.
Ref. [26]), because 30-bar is considered to be insufﬁcient for
real gas effects to take place [5].
In order to test the numerical model, including the size of
the domain, boundary conditions and numerical schemes,
ﬁrst a relatively simple scenario of a one-component air eair
jet release was considered. In addition, this case permits to
compare results with the interferometric Rayleigh scattering
(IRS) measurements of Yuceil et al. [17] and the axisymmetric
simulations of Lehnasch [10], where compressibility-corrected
turbulence models were used. The position X
m and diameter
Dm of the Mach disk are compared in Table 2 to the values
given in Ref. [10], obtained from Schlieren visualization in
Ref. [17], as well as with the early experimental correlations
from various sources (see Section 2.1). Fig. 1 shows centerline
values of axial streamwise velocity and Mach number. After
exiting the oriﬁce, the air jet undergoes great acceleration and
cooling; as a result the Mach number increases up to 5.36,
which is in good agreement with a semi-empirical formula
given in [12]. Moreover, the Mach number of 0.4 just after the
Mach disk has been predicted by Harstad and Bellan [27]. It can
be also seen that the streamwise velocity increase behind the
Mach disk correlates well both with measured IRS values [17],
and those obtained numerically [10]. However, the latter
axisymmetric simulation could not capture a convex shape of
the Mach disk and thus its axial position was slightly
overestimated.
This set of initial simulations resulted in a computational
domain, which has the following dimensions of “base”,
vertical and “top” sections: 10 D
e,3 5De and 48De,r e s p e c t i v e l y .
As it is shown in Fig. 2 the no-slip boundary condition was
set for the base, while the pressure conditions (atmospheric)
were prescribed at the outer boundaries to allow modeling
of entrainment. The latter was also improved by concen-
trating computational volumes in the vicinity of the shear
layers, where the highest turbulence production rate is
expected.
T h ec o a r s e( 5 0/C2 50 /C2 100) and ﬁne (64 /C2 64 /C2 176) grids
were used in the present work with the respective X /C2 q /C2 Z
resolution (with q being an azimuthal coordinate). Both
grids had 36 elements on the exit diameter, and cells of the
order of D
e=128 in the mixing region. Boris et al. [25] suggests
the grid spacing to be well smaller than a critical value of
D
e=16 in order for numerical dissipation to become insig-
niﬁcant compared to the eddy diffusivity from all unre-
solved scales.
The computations were performed until the ﬂow reached
a quasi steady state with the time steps being as small as
approximately 2 :5 /C3 10
/C0 9 and 10 /C0 9 for air and helium,
respectively. In the course of this work, it was found simi-
larly to the experimental work of Lacerda [28] (see Fig. 4.5 e6
in Ref. [28]), that a helium jet takes much more time to
Table 2 e Comparison of the position and diameter of the
Mach disk (from various sources). A minimum Z=De
coordinate for Xm is used for present data.
Yuceil Present Lehnasch Correlations
Xm =De 3.6 3.65 3.86 3.56 e3.67
Dm =De 1.85 1.88 2.14 1.82 e2.23
international journal of hydrogen energy 37 (2012) 17390 e17399 17393

<!-- PDF_PAGE: 5 -->

“stabilize”. More speciﬁcally, for a helium-air jet computa-
tions at least until t/C3 ¼ 360 were required, while for an air eair
jet t/C3 ¼ 90 was sufﬁcient (where t/C3 is deﬁned in the next
section).
Although, both a full domain and a one-quarter of the
domain (using symmetry conditions) calculations were
considered, only the latter have ﬁnally reached a quasi steady
state regime, in view of the small time-step restriction and the
need to continue simulations for a sufﬁciently long period of
time. Moreover, since no signiﬁcant differences were observed
(at least in the present numerical framework) in the inter-
mediate results, this paper reports only the one-quarter of the
domain simulations. Nevertheless, these are expected to be
sufﬁciently accurate due to several speciﬁc features of the
highly underexpanded jet, including its large potential core
length and signiﬁcantly low growth rates when compared to
the subsonic ones (i.e. typical 3 D instabilities do not start their
development prior the X
p). In addition, this sacriﬁce allowed to
continue simulations beyond the quasi steady state in order to
acquire turbulence statistics.
4. Numerical results and analysis
It must be noted, that throughout this section the following
non-dimensional quantities are used for streamwise velocity,
density, pressure and temperature: U
/C3 ¼ < U >
Ue
, r/C3 ¼ < r >
rhe
,
P/C3 ¼ < P >
Pa
, T/C3 ¼ < T >
Ta
, where subscripts and symbols <>,
e, rhe, a, denote Reynolds average, exit value, helium density at
ambient conditions and atmospheric value, respectively. In
addition, following usual practice, time is made dimension-
less as follows: t
/C3 ¼ tUe=De. It is also interesting to note, that in
the present numerical framework a difference between the
Reynolds and Favre averages has been quantitatively shown
to be negligible (see below).
4.1. Initial transient gas jet ﬁeld
Since the two-component (helium-air) gas jet took more
time to reach quasi steady state its initial transient behavior
 0.4
 0.6
 0.8
1
 1.2
 1.4
 1.6
 1.8
2
 2.2
 2.4
0 1 2 3 4 5 6 7 8 9
U / Ue
Z/De
Lehnasch
Present
Yuceil IRS
0
 0.5
1
 1.5
2
 2.5
3
 3.5
4
 4.5
5
 5.5
0 1 2 3 4 5 6 7 8 9
M
Z/De
Present
Fig. 1 e Centerline values of streamwise velocity and Mach number.
x
y
x
z
Solid boundary
Pressure boundaries
Fig. 2 e Grid cross sections at y [ 0 and z [ 0. Red lines correspond to the inﬂow/outﬂow pressure boundaries, while the
black one to the wall condition. Note: Only half of the vertical cut is shown. (For interpretation of the references to colour in
this ﬁgure legend, the reader is referred to the web version of this article.)
international journal of hydrogen energy 37 (2012) 17390 e1739917394

<!-- PDF_PAGE: 6 -->

is brieﬂy described below. The Mach number contours cor-
responding to t/C3 ¼ 270 and 225 are shown in Fig. 3 in order to
demonstrate that the shock-wave structure was indeed
highly unsteady (see also Ref. [28]). It can be seen, that the
thickness of the shear layer prior to a triple point changes
with time together with the position, diameter of the Mach
disk and a curvature of the barrel shock. Convective insta-
bilities appear to be generated around the triple point,
propagating and growing in the supersonic region along the
potential core. The compressions and subsequent rarefac-
tions, potentially produced by these vortex structures, are
manifested in the oscillations of the supersonic shear layer
along the potential core, which can be seen in the top image.
In addition, these pulsations are as well observed in the RMS
data, which is discussed in the end of this section. It should
be noted, that unsteady behavior of the supersonic gas jets
has been observed in context of the aerodynamic jet noise.
Being more close to the objectives of the present paper,
Peneau et al. [8] reported the position of the Mach disk to
vary signiﬁcantly during the release of hydrogen from
a high-pressure tank ð100 atm Þ up to t
/C3 ¼ 80 (corresponds to
an end of the simulation). However, the measurements of
Lacerda [28] demonstrated that for light gases Mach disk
takes relatively longer time to stabilize around the location
predicted by a steady theory [12] or [15]. It was also argued in
Ref. [28] that it afterward oscillates with a low amplitude
around this location at a resonant frequency of the reservoir.
Investigation of the unsteady phenomena in the near-ﬁeld
of underexpanded jets is, however, out of scope of this
paper.
4.2. Mean and RMS gas jet ﬁelds
Present simulations were carried out until t/C3 ¼ 540 and the
quasi steady state solution was conﬁrmed to be reached at
t
/C3 ¼ 360. The calculated mean position Xm and diameter Dm of
the Mach disk for the two-component (helium-air) jet are
compared in Table 3 with the values obtained from BOS
visualizations of Dubois [20] and with the scaling laws given in
Section 2.1. Eqn. (2) appear to slightly underestimate the
diameter of the Mach disk due to uncertainty in the empirical
constant a, as well as assumption, that the normal shock
substantially exceeds dimensions of the exit section, which
work better for higher initial pressure ratios. It is, however,
apparent that both the simulated and theoretical mean
dimensions of the shock-wave structure are in general
agreement with the experiments.
Fig. 4 shows comparison of BOS data for three ﬁeld-of-view
(see Table 1 ) with both coarse and ﬁne grid computations.
Good agreement between FOV1 measurements and compu-
tations is observed for the initial sharp density decrease up to
the position of Mack disk. However, in the proximity of this
strong normal shock resolution seems to be inadequate,
which results in certain errors in measuring its position and
diameter ( Table 3 ). Although, correspondence with FOV2 is
ﬁne for the ﬁrst few diameters behind the Mach disk, in
general, computations overestimate experimental data. In the
end of the computational domain, however, ﬁne grid results
show better agreement with the BOS data.
Fig. 5 shows centerline values of the gas jet velocity, Mach
number, temperature and pressure calculated using both
coarse and ﬁne grids. From the point of view of validation, the
Mach number is observed to reach 94% of unity at Z ¼ 6:2D
e for
the ﬁne grid, which is in good agreement with the value of
6:5D
e (with Xm being added) predicted by Eqn. (3). According to
this plot the jet oscillates around a sonic point up to Z ¼ 20De
and becomes well supersonic afterward. The pressure distri-
bution beyond the Mach disk deviates from atmospheric also
up to the axial location of 20 De. Temperature drops below
30 K in the proximity of the Mach disk and quickly returns to
the ambient value behind it. After about 12 D
e from the oriﬁce
temperature rapidly decreases and reaches its exit value
approximately at Z ¼ 20 D
e. It can be seen that the tempera-
ture distribution is being far apart from the atmospheric
throughout the domain. The centerline velocity, likewise,
reaches its exit value at the same streamwise distance and
continues to grow afterward.
While Dubois [20] estimated the length of the potential core
for this release scenario to be equal about 29 D
e (see Eqn. (4)),
present computations do not show any signiﬁcant deviation
of the centerline mass fraction from unity on the entire
domain of 35 D
e. Intermediate results of the far-ﬁeld simula-
tions demonstrate that when the numerically obtained
temperature is used to calculate the helium mass fraction
instead of the atmospheric one (as it was done in the experi-
ments) the estimate of the potential core length increases
beyond 35 D
e.
It is now important to examine the gas dynamic parame-
ters provided by various notional nozzle models against the
simulated data. Table 4 shows such a comparison in the
assumption that a discharge coefﬁcient equals unity, which is
reasonable in this range of Reynolds numbers. The axial data
given e.g. by Figs. 4 and 5 at 20 D
e from the nozzle exit is in very
good agreement with all the parameters provided by the
model of Ewan and Moodie [3]. The notional nozzle diameter
ðD
f Þ, which was calculated based on the transverse velocity
Fig. 3 e Mach number contours at t/C3 [270: top image,
t/C3 [225: bottom image; x and z coordinates are non-
dimensionalized by De.
Table 3 e Comparison of the position and diameter of the
Mach disk with BOS and scaling laws. A minimum Z=De
coordinate for Xm is used for present data.
Dubois (BOS) Present Eqns. (1) and (2)
Xm =De 3.5e3.8 3.63 3.58
Dm =De 1.25e1.75 1.54 1.35
international journal of hydrogen energy 37 (2012) 17390 e17399 17395

<!-- PDF_PAGE: 7 -->

and mass fraction at this location (to the point where they
become negligible, see Fig. 6), is slightly larger when compared
to this model. Such a deviation is insigniﬁcant and can be,
apparently, ﬁxed by shifting the position of interest a little
upstream.
Although, the notional nozzle model of Birch et al. [1] gives
a good value for D
f , it underestimates the axial density and
substantially overestimates the value of temperature at this
location. The other two concepts as described by Birch et al. [2]
and Yuceil and Otugen [4], suggest the notional nozzle diam-
eter to be almost twice as small as the one found in simula-
tions. This is not consistent with the fact, that all the gas
dynamic parameters given or assumed by these models are
expected to exist much further downstream, where the extent
of the gas jet must be greater (i.e. beyond the potential core
length).
Therefore, the model of Ewan and Moodie [3] not only
provides the best ﬁt to the simulated data ( Table 4 ), but also
deﬁnes these gas-dynamic and thermodynamic parameters
at the point located well before the end of the potential core
and at the same time rather far from the major shock cells
(i.e. isobaric section of the jet). Since any notional nozzle
model insofar assumes a 100% gas concentration at the
notional diameter this framework will give the smallest error
in mass fraction at least in the proximity to the centerline.
This can be observed, in particular, by looking at helium
concentration in Fig. 6 . However, it can be also seen, that all
the transverse gas dynamic parameters at this location
(besides pressure) exhibit large gradients between 0 and 2 D
e.
Thus, although, the model given by Ref. [3] could provide
reasonable boundary conditions for the subsequent simula-
tions, further validation and reﬁnement of this law is needed
to be able to model the near-ﬁeld entrainment into the high-
pressure jet.
 0
 1
 2
 3
 4
 5
 6
 0  5  10  15  20  25  30  35  40  45
ρ*
Z/De
Coarse
Fine
BOS FOV1
BOS FOV2
BOS FOV3
Fig. 4 e Mean centerline values of simulated and measured
density. BOS experiments using three ﬁelds-of-view.
 0.2
 0.4
 0.6
 0.8
 1
 1.2
 1.4
 1.6
 1.8
 2
 0  5  10  15  20  25  30  35
U*
Z/De
Coarse
Fine
 0
 1
 2
 3
 4
 5
 6
 7
 8
 0  5  10  15  20  25  30  35
M
Z/De
M = 0.94 at Z/De = 6.2
Coarse
Fine
 0
 0.1
 0.2
 0.3
 0.4
 0.5
 0.6
 0.7
 0.8
 0.9
 1
 0  5  10  15  20  25  30  35
T*
Z/De
Coarse
Fine
 0
 0.5
 1
 1.5
 2
 2.5
 3
 0  5  10  15  20  25  30  35
P*
Z/De
Coarse
Fine
Fig. 5 e Mean centerline values of streamwise velocity, Mach number, temperature and pressure.
international journal of hydrogen energy 37 (2012) 17390 e1739917396

<!-- PDF_PAGE: 8 -->

The turbulence intensities were calculated based on the
100 collected data ﬁelds and are shown in Fig. 7 both
for axial and transverse streamwise velocity. It must be
noted, that in such a highly compressible multi-component
regime Favre averaging is usually preferred to the Reynolds
one (i.e. < ru >¼ < r >< u > þ < r
0u0 >). However, in the
present numerical framework the density/velocity cross-
correlation has been shown to be negligible. More speciﬁ-
cally, a maximum value of the quantity < r
0u0 >= < r >< u >
did not exceed 5 /C3 10/C0 3 both for axial and transverse
locations.
It can be seen in the axial plots of Fig. 7 , that initially,
inside the barrel shock, the ﬂow is indeed potential and there
exist no ﬂuctuations (see e.g. Ref. [12]). Peak RMS velocity
values are observed in the proximity of the Mach disk
location, where a normal shock wave interacts with a large
density gradient. For a similar scenario turbulent energy
production across a shock wave has been described in a 1 D
case by Gavrilyuk and Saurel [29]. It is not clear, however,
whether these peak values are a direct result of such inter-
actions or the Mach disk unsteadiness is also driven by the
Kelvin-Helmholtz instability as it was described above.
Nevertheless, beyond the Mach disk and after a few minor
shock cells (e.g. beyond Z=D
e ¼ 20) the turbulence intensity
starts to approach a constant value of about 7%. The trans-
verse values of ﬂuctuating velocity are also shown in Fig. 7
at Z=D
e ¼ 20. The maximum value of RMS velocity can
be observed at the periphery of the supersonic shear
layer. Thus, turbulence characteristics at this location,
and turbulent kinetic energy in particular, could be also
Table 4 e Table of boundary conditions given by various notional nozzle models and the data from present simulations at
Z[20 De.
Model Birch [1] Ewan [3] Birch [2] Yuceil [4] Present
Temperature, K 300 224.97 300 117.81 214.27
Mach number 1.0 1.0 1.28 2.15 1.06
Velocity, m=s 1019.17 882.57 1308.22 1375.29 913.11
Density, kg=m3 0.162 0.216 0.162 0.414 0.218
Df =De 4.08 3.79 2.68 2.2 4.06
0
 0.2
 0.4
 0.6
 0.8
1
 1.2
 1.4
 1.6
0 1 2 3 4 5
U*
X/De
0
 0.2
 0.4
 0.6
 0.8
1
 1.2
 1.4
 1.6
 1.8
2
0 1 2 3 4 5
M
X/De
0
 0.1
 0.2
 0.3
 0.4
 0.5
 0.6
 0.7
 0.8
 0.9
1
0 1 2 3 4 5
Yhe
X/De
 0.4
 0.5
 0.6
 0.7
 0.8
 0.9
1
 1.1
 1.2
0 1 2 3 4 5
X/De
T*
Fig. 6 e Mean transverse values of streamwise velocity, Mach number, temperature and helium mass fraction at Z=De[20.
international journal of hydrogen energy 37 (2012) 17390 e17399 17397

<!-- PDF_PAGE: 9 -->

provided as boundary conditions for the far-ﬁeld
computations.
5. Conclusions
Simulations of the highly underexpanded turbulent gas jets
were performed and compared with available experimental
data sets and correlations. Present numerical model provides
relatively fair mean predictions both in the case of the one-
component air eair and two-component helium-air
scenarios. In particular, the position and diameter of the Mach
disk, and most importantly, characteristic lengths of the
subsonic and potential cores were found to be in good agree-
ment with experimental measurements and Eqns. (1) and (2) .
The latter demonstrates that present numerical model seems
to achieve largely correct growth rates without any contro-
versial SGS models with compressibility-corrected terms.
Potential initial conditions for the far-ﬁeld simulations of
the high-pressure gas jets were suggested in terms of the
distance from the source, which is beyond all the near-ﬁeld
shock-cells, while at the same time well before the end of
the potential core. The turbulence characteristics and gas-
dynamic parameters at this location were provided as well.
The latter have been shown to be well predicted by the
notional nozzle model of Ewan and Moodie [3], which was
demonstrated to exist in physical sense. Future work will be
directed toward the far-ﬁeld simulations of the high-pressure
hydrogen/helium releases with the boundary conditions given
by the present methodology, as well as toward the validation
and/or reﬁnement of the notional nozzle models.
Acknowledgments
This work has been supported by French Research National
Agency (ANR) through Plan d’Action National sur l’Hydrogne et
les piles combustible program (projet DIMITRHY no. ANR -08-
PANH-006). IRPHE group (AiX Marseille), kindly provided the
BOS experimental data in electronic form.
references
[1] Birch AD, Brown DR, Dodson MG, Swafﬁeld F. The structure
and concentration decay of high pressure jets of natural gas.
Combustion Science and Technology 1984;36:249 e61.
[2] Birch AD, Huches DJ, Swafﬁeld F. Velocity decay of high pressure
jets. Combustion Science and Technology 1987;52:161e71.
[3] Ewan BCR, Moodie K. Structure and velocity measurements
in underexpanded jets. Combustion Science and Technology
1986;45:275e88.
[4] Yuceil KB, Otugen MV. Scaling parameters for
underexpanded supersonic jets. Physics of Fluids December
2002;14(12):4206e15.
[5] Chenoweth DR. Gas-transfer analysis section H-real gas
results via the van der Waals equation of state and virial
expansion extensions of its limiting Abel-Noble form, Sandia
report, SAND83 e8229, June 1983.
[6] Xu BP, Zhang JP, Wen JX, Dembele S, Karwatzki J. Numerical
study of a highly under-expanded hydrogen jet,
International Conference on Hydrogen Safety, Pisa, Italy,
8e10 September 2005.
[7] Ishii R, Fujimoto H, Hatta N, Umeda Y. Experimental and
numerical analysis of circular pulse jets. Journal of Fluid
Mechanics 1999;392:129 e53.
[8] Peneau F, Pedro G, Oshkai P, Djilali N. Transient supersonic
release of hydrogen from a high pressure vessel:
a computational analysis. International Journal of Hydrogen
Energy 2009;34(14):5817 e27.
[9] Chauveau, C., Davidenko, D.M., Sarh, B., Go ¨ kalp, I.,
Avrashkov, V., Fabre, C., PIV measurements in an
underexpanded hot free jet, 10th international symposium
on application of laser techniques to ﬂuid mechanics, Lisbon,
Portugal, 26 e29 June 2006.
[10] Lehnasch G. Contribution a ` L’e´ tude nume´ rique des jets
supersoniques sous-de` tendus, PhD The` se, L’Universite´ de
Poitiers, 2005.
[11] Sarkar S, Erlebach G, Hussaini MY, Kreiss HO. The analysis
and modelling of dilatational terms in compressible
turbulence. Journal of Fluid Mechanics 1991;227:473 e93.
[12] Ashkenas H, Sherman FS. Structure and utilization of
supersonic free jets in low density wind tunnels. Rareﬁed
Gas Dyn 1966;2:84 e105.
[13] Bier K, Shcmidt B. Zur Form der Verdichtungsstibe in frei
expandierenden Gasstrahlen. Z.f.angew. Physik 1961;13:
493e500.
 0
 0.1
 0.2
 0.3
 0.4
 0.5
 0.6
 0  5  10  15  20  25  30  35
U’ / <U>
Z/De
 0
 0.02
 0.04
 0.06
 0.08
 0.1
 0.12
 0.14
 0.16
 0.18
 0.2
 0.22
 0  1  2  3  4  5
U’/ <U>
X/De
Fig. 7 e Centerline and transverse (at Z=De[20) values of RMS velocity ðu0[<u2>1=2Þ.
international journal of hydrogen energy 37 (2012) 17390 e1739917398

<!-- PDF_PAGE: 10 -->

[14] Crist S, Sherman PM, Glass DR. Study of the highly
underexpanded sonic jet. AIAA Journal 1965;4(1):68 e71.
[15] Velikorodny A. Overview of highly underexpanded jets:
application to the accidental release of gas from a high-
pressure reservoir, CEA Rapport DEN/DANS, SFME/LTMF/RT/
10e016/A, January 2011.
[16] Glotov GF. Local subsonic zones in supersonic jets ﬂows.
Fluid Dynamics 1998;33(1):117 e23.
[17] Yuceil KB, Otugen MV, Aric E. Interferometric Rayleigh
Scattering and PIV Measurements in the Near-Field
of Underexpanded Sonic Jets, 41st Aerospace
Sciences Meeting and Exhibit, Reno, Nevada, 6 e9
January 2003.
[18] Veser A, Kuznetsov M, Fast G, Friedrich A, Kotchourko N,
Stern G, et al. The structure and ﬂame propagation regimes
in turbulent hydrogen jets. International Journal of Hydrogen
Energy 2011;36:2351 e9.
[19] Wilke JA, Danehy PM, Nowak RJ, Alberfert DW. Fluorescence
Imaging Study of Impinging Underexpanded Jets, 46th AIAA
Aerospace Sciences Meeting and Exhibit, Reno, NV, 7 e10
January 2008.
[20] Dubois J. E ´ tude expe´ rimentale de jets libres, compressibles
ou en pre´ sence d’un obstacle, PhD the ` se, Aix Marseille
Universite´ , June 2010.
[21] Poinsot T, Veynante D. Theoretical and numerical
combustion. Edwards; 2001.
[22] Hanel D, Schwane R, Seider G. On the accuracy of upwind
schemes for the solution of the Euler and Navier-stokes
equations. AIAA Conference 1987:87 e1105.
[23] Liou MS. A Sequel to AUSM: AUSM
þ. Journal of
Computational Physics 1996;129:364 e82.
[24] Beccantini A, Gounand S. Evaluation of the diffusive terms of
the Navier-Stokes equations via a cell-centered ﬁnite volume
approach, CEA Rapport DEN/DANS, SFME/LTMF/RT02 e024/B,
2002.
[25] Boris JP, Grinstein FF, Oran ES, Kolbe RJ. New insights into
large eddy simulation. Fluid Dynamic Research 1992.
[26] Landau LD, Lifshitz EM. Fluid mechanics (Course of
Theoretical Physics). 2nd ed. Pergamon Press; July 1987.
[27] Harstad K, Bellan J. Global analysis and parametric
dependencies for potential unintended hydrogen-fuel
releases. Combustion and Flame 2006;144:89 e102.
[28] Lacerda NL. On the start up of supersonic underexpanded
jets, PhD thesis, California Institute of Technology,
Pasadena, 1986.
[29] Gavrilyuk SL, Saurel R. Estimation of the turbulent energy
production across a shock wave. Journal of Fluid Mechanics
2006;549:131e9.
international journal of hydrogen energy 37 (2012) 17390 e17399 17399
