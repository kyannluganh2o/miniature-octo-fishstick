<!-- PDF_PAGE: 1 -->

A comparative study of highly underexpanded
nitrogen and hydrogen jets using large eddy
simulation
Xiaopeng Li *, Kun Wu, Wei Yao, Xuejun Fan
State Key Laboratory of High Temperature Gas Dynamics, Institute of Mechanics, Chinese Academy of Sciences,
Beijing, 100190, PR China
article info
Article history:
Received 8 November 2015
Received in revised form
21 January 2016
Accepted 21 January 2016
Available online 17 February 2016
Keywords:
Scramjet
Hydrogen
Highly underexpanded jet
Large eddy simulation
abstract
Three-dimensional large eddy simulations (LES) of highly underexpanded hydrogen and
nitrogen jets at the same nozzle pressure ratio (NPR) of 5.60 and at a Reynolds number
around 10
5 are performed. The classical near-ﬁeld structures of highly underexpanded jets
are well captured by LES, especially the shape and size of Mach barrel for both jets are very
similar and agree well with the available literature data. However, the ﬂow ﬁeld and the
shock structures after the Mach disk differ signiﬁcantly. The density in the annular shear
layer of H
2 jet is much lower because of its smaller molecular weight. Meanwhile, the H 2 jet
has a much longer jet core and more shock cells. The dominant instability mode is helical for
the N
2 jet, but is axisymmetric for the H 2 jet. There are two discrete peaks of fs ¼ 37.086 kHz
and f2s ¼ 45.695 kHz in the spectrum of the N 2 jet, while the spectrum of the H 2 jet is
characterized by a fundamental screech frequency of fs ¼ 47.020 kHz and its high-order
harmonics. The H 2 jet mixes more rapidly with the ambient air but has a much smaller
mixing area on cross-section planes. Mixing between the ambient air and fuel still takes
places at the jet boundary deﬁned according to the mixture fraction of Z ¼ 0.02, and the area
of fully turbulent region of the highly underexpanded jets seems to be less predicted based
on the traditional vorticity T/NT (turbulent/non-turbulent) interface for both jets.
Copyright © 2016, Hydrogen Energy Publications, LLC. Published by Elsevier Ltd. All rights
reserved.
Introduction
Scramjet engine is one of the most promising propulsive
systems for future hypersonic vehicles because of its high
performance at large Mach number. Usually air entering the
combustor is supersonic at ﬂight speeds beyond Mach 5, thus
the residence time of the air in a scramjet engine is on the
order of milliseconds [1]. The mixing and diffusive
combustion of fuel and air in a conventional scramjet engine
take place simultaneously in the combustor. Therefore,
ensuring fuel-air mixing and subsequently combustion in
such a short time is critical to the design of scramjet engine
[2e4].
In spite of the high price in production and storage,
hydrogen is a very attractive fuel that may help to resolve the
problem because of its higher combustion efﬁciency than
conventional hydrocarbon fuels. Hydrogen gives the highest
* Corresponding author . Tel.: þ86 10 82544053.
E-mail address: lxpyfy@163.com (X. Li).
Available online at www.sciencedirect.com
ScienceDirect
journal homepage: www.elsevier.com/locate/he
international journal of hydrogen energy 41 (2016) 5151 e5161
http://dx.doi.org/10.1016/j.ijhydene.2016.01.120
0360-3199/Copyright © 2016, Hydrogen Energy Publications, LLC. Published by Elsevier Ltd. All rights reserved.

<!-- PDF_PAGE: 2 -->

heat release with the shortest kinetic time [5,6], and is already
used as fuel in space propulsion [7,8]. In addition, hydrogen is
generally considered to be more environment-friendly since it
does not produce any harmful pollutants like carbon mon-
oxide (CO), carbon dioxide (CO
2), or particulate matter during
the combustion process except the minor NOx formation due
to its high-adiabatic ﬂame temperatures. The fuel is usually
injected into the combustor at a pressure much higher than
the ambient pressure to ensure a good mixing, which will
result in a highly underexpanded jet [9e12]. For the design
beneﬁt, revealing the ﬂow characteristics and understanding
the physical mechanism of a highly underexpanded hydrogen
jet are conducive to the development of scramjet engine.
The highly underexpanded jet is characterized by the
presence of a Mach disk in the near-ﬁeld region and deﬁned by
a nozzle pressure ratio (NPR) beyond 3.85 [12]. Adamson and
Nicholls (1959) [9] presented the structure of a highly under-
expanded jet into quiescent air ﬁrstly. Ashkenas and Sherman
(1965) [10] indicated that the near-ﬁeld structures of highly
underexpanded jets are dominated by NPR and obtained an
empirical formula to predict the Mach disk height according to
NPR. Over the years, several more experimental [11e19] and
numerical [20e24] studies have been conducted, which have
resulted in a good understanding of the ﬂow characteristics of
highly underexpanded jets today. One may refer to the recent
review of Franquet et al. (2015)[25] for further details. However,
the knowledge on a highly underexpanded hydrogen jet is still
limited since most of the injected gases used in previous
studies are air or nitrogen. Hydrogen has higher diffusivity and
larger nozzle exit speed due to its low molecular weight, which
may result in a much different ﬂow ﬁeld even at the same NPR.
In addition, the previous experimental and numerical studies
on highly underexpanded jets mainly provide the time-
averaged ﬂow characteristics in the near-ﬁeld region of jets
by using schlieren photographs and Reynolds averaged
NaviereStokes (RANS) methodology respectively. The instan-
taneous unsteady ﬂow features of a highly underexpanded jet
that dominate the mixing processes are still not well revealed.
Large eddy simulation (LES), which resolves the large scales
directly while models the effects of small scales, is turbulence-
well-represented yet computationally affordable for the
simulation of supersonic shear ﬂows with high compress-
ibility. In recent years, LES researches [26e30] on under-
expaned jets have emerged thanking to the advances in
numerical methods and computation technology. In partic-
ular, Gorle et al. (2010) [28] conducted a computational study of
highly underexpanded hydrogen jet at NPR ¼ 30.0, and found
that the near-ﬁeld structures captured by the LES have a good
agreement with the experiments. However, their main goal
was to verify the jet injection modeling and an in-depth anal-
ysis on the instantaneous ﬂow features was not performed.
Recently, Hamzehloo and Aleiferis (2015) [30] performed a
numerical analysis of underexpaned hydrogen jets with
different NPRs using LES, where the transient ﬂow develop-
ment upstream of the nozzle exit was investigated, as well as
the effect of NPR on the mixing characteristics and near nozzle
shock structures were analyzed. Besides the near-ﬁeld shock
structures, screech tone of underexpanded supersonic jets is
another important subject of many experimental and theo-
retical studies [26,27,31e36] since its ﬁrst experimentally
observation by Powell (1953) [31]. However, the working gases
are usually air/nitrogen as well in those studies, whereas the
data on the screech characteristics of highly underexpaned
hydrogen jets are rather lacking in the literature.
In the present study, a three-dimensional LES of high
pressure hydrogen jet through a convergent nozzle with an
exit diameter of D ¼ 2.0 mm and an exit Reynolds number
around 10
5 was carried out. A test case of nitrogen injection at
the same NPR of 5.60 was also simulated for comparison. A
well-designed, hexahedral and block-structured grid con-
taining about 27.3 M computational cells is applied. The
compressible ﬂow solver, astroFoam, which is developed
based on the OpenFOAM C þþ library, is used to perform the
simulations. The time evolution, averaged jet structures,
shock structures, dominant instability modes, and mixing
characteristics of the H
2 jet are analyzed and discussed in
comparison with the N 2 jet.
Computational methodology
Three-dimensional, Favre-ﬁltered Navier eStokes equations
for the unsteady compressible Newtonian ﬂuids with heat and
species transfer are solved using a density-based compress-
ible solver, astroFoam, which is developed based on the
standard rhoCentralFoam solver distributed with OpenFOAM
v2.3.0. The rhoCentralFoam solver [37] has been proved to be
able to capture the ﬂow discontinuities (e.g. shock waves) with
non-oscillatory and low dissipation by solving the convection-
diffusion equation using the semi-discrete K-T central
scheme [38]. However, the rhoCentralFoam solver is limited to
single species non-reacting ﬂows in its standard form. The
multiple species transport and multi-component diffusion are
added to create the astroFoam solver to investigate the gases
mixing and reacting ﬂow. In addition, the astroFoam solver
solves for sensible enthalpy equation instead of the transport
of total energy in rhoCentralFoam solver in order to easily
include the chemical reaction and species transport terms.
Similar OpenFOAM solvers have been developed to study the
incompressible turbulent ﬂows by Vuorinen et al. (2011) [39]
and Baba and Tabor (2009) [40] as well as the supersonic
compressible turbulent ﬂows by Vuorinen et al. (2013) [29] and
Fureby et al. (2011, 2013) [41,42]. The ﬁltered sub-grid terms are
modeled with the sub-grid scale turbulent kinetic energy one-
equation model, which is integrated in OpenFOAM in the
standard form.
Computational domain and grid
Previous studies [31e36] indicated that the sound waves
originated in the downstream will propagate upstream to
change the initial shear layer structures at the nozzle exit,
which will inﬂuence the development of jet shear layer in the
downstream further. However, A priori knowledge of nozzle
exit conditions is usually difﬁcult to be obtained in many
practical applications. Therefore, the numerical investigation
of underexpanded jets requires implementing the practical
nozzle geometries to capture the self-sustained acoustic loop
correctly. Some example of such endeavors can be found in
international journal of hydrogen energy 41 (2016) 5151 e51615152

<!-- PDF_PAGE: 3 -->

the LES of supersonic jets by Liu et al. (2009) [27] and Dauptain
et al. (2010) [43].
The computational domain used in the current LES
modeling of underexpanded jets is shown in Fig. 1 (a). The
computational domain mainly consists of a box of size
50 /C2 100 /C2 50 mm respectively in x, y, and z Cartesian coor-
dinate directions. The hydrogen or nitrogen jet in the high
pressure nozzle (with total pressure P
0 and total temperature
T0) is injected into the quiescent air (with static pressure P ∞
and static temperature T ∞) from a convergent nozzle of
20.0 mm in height. The entrance and exit diameters of the
nozzle are d ¼ 8.0 mm and D ¼ 2.0 mm respectively.
The spatial resolution in LES of supersonic jets needs to be
rather high indicated by the previous studies [27e30,43e46].
The hexahedral, block-structured grid presented in Fig. 1(b) is
applied in the present LES. Altogether the mesh contains
27.3 M computational cells. The jet core is meshed with high
resolution by adding a reﬁnement region which covers the jet
core and the jet shear layers. With those careful arrange-
ments, the grid resolution in the main region of interest in this
study is similar as those used in the previous LES of super-
sonic jets, which are summarized in Table 1. In addition, very
coarse cell sizes with a resolution of 1.0 mm in the far ﬁeld and
0.5 mm at outﬂow boundaries are used to introduce additional
dissipation and avoid wave reﬂections from these boundaries.
The computational time step Dt is respectively 5.63 /C2 10
/C0 9 s for
H2 jet and 1.37 /C2 10/C0 8 s for N2 jet, both of which are limited by a
maximum Courant-Friedrichs-Lewy (CFL) number of 0.6. This
time step is on the same order of magnitude as that Kawai and
Lele (2010) [44] and G /C19enin and Menon (2010) [45] used in the
LES modeling of a sonic jet in supersonic cross ﬂow (JISC).
Initialization and boundary conditions
The quiescent air is the mixture of nitrogen in 0.76699 and
oxygen in 0.23301 by mass fraction, and initially the
temperature, pressure, density, and velocity are respectively
set as uniform, i.e. T
∞ ¼ 300 K, P ∞ ¼ 101,325 Pa, r∞ ¼ 1.17 kg/
m3,U ∞ ¼ 0. The hydrogen and nitrogen jets are injected into
the quiescent air with the same total pressure and tempera-
ture at NPR of 5.60. The ﬂow conditions at the nozzle exit are
close to the sonic condition, and are summarized in Table 2
marked with subscript 1. The ﬂow at the nozzle inlet is sub-
sonic, thus the stagnation condition for temperature and
pressure is employed, while a zero-gradient condition for ve-
locity is used. All walls including the sides of nozzle and the
round tube outside the nozzle are treated as no-slip adiabatic
walls. At the top of the computational domain together with
the four free surfaces of the box, open boundary condition is
applied, i.e. all ﬂow parameters are treated as zero-gradient
for outﬂow and set as ambient values when the backﬂow oc-
curs. The integral time scale is deﬁned using D and the
maximum velocities in the near ﬁeld of the jets as t
0 ¼ D/(2U1),
and takes a value of 2.83 ms for N 2 jet and 0.76 ms for H 2 jet.
Thus a simpliﬁed time value of t0 ¼ 2.5 ms, which is close to the
integral time scale of N 2 jet, is selected as the reference time.
The ﬂow-through time (FTT) for the jet washing out the whole
computational domain in streamwise direction is about
t
total z 0.5 ms ¼ 200t0 for both jets, thus the total simulation
duration is set as 4t total ¼ 2.0 ms ¼ 800t0, which is four times
the value used by Vuorinen et al. (2013) [29] to ensure statis-
tical steady. The instantaneous results are saved every 2t 0,
then turbulent statistics are collected for the last three ﬂow-
through times (200t
0~800t0, total 300 time steps).
Results and discussion
Flow evolution
The temporal evolution of mass fraction for H 2 and N2 jets at
the same NPR of 5.60 is presented in Fig. 2. As can be seen, the
main ﬂow structures at different times for the hydrogen jet
are similar to those of the nitrogen jet. For example, the initial
tip vortex ring which is usually visible in subsonic jets and the
undulating vortex ring are noted for both the H
2 and N 2 jets.
The turbulent transition of the jets is both characterized by
the breakdown of recirculation zones, the loss of ﬂow sym-
metry, and the generation of streamwise vortexes. Mean-
while, the large-scale turbulent vortices along the jet shear
layer are also observed when the jets are fully developed.
However, there is a vortex ring near the nozzle exit for the
hydrogen jet, which differs from the nitrogen jet.
The sonic conditions for H
2 and N 2 jets under the same
total pressure and total temperature differ signiﬁcantly due to
the differences in the molecular weight. In particular, Table 2
indicates that velocity at nozzle exit for hydrogen jet is
1321.3 m/s, which is much larger than the 353.1 m/s for ni-
trogen jet. Thereby, the H
2 jet penetrates faster than the N2 jet.
The jet penetration z(t) and maximum width W(t) are two
important overall parameters to characterize the ﬂow evolu-
tion characteristics, and are closely related to the overall
mixing and entrainment. In the present study, the jet pene-
tration and maximum width are deﬁned according to the
outer limit of mass fraction Y
s on the midline plane. In other
words, the jet penetration z(t) is deﬁned as the maximum axial
Fig. 1 e (a) Computational model employed for the LES of
highly underexpanded jets (units: mm). (b) Computational
grid.
international journal of hydrogen energy 41 (2016) 5151 e5161 5153

<!-- PDF_PAGE: 4 -->

position, and the jet maximum width is deﬁned as the
maximum span in the radial direction. The jet penetration z(t)
and maximum width W(t) for H 2 and N 2 jets as a function of
time are compared quantitatively in Fig. 3 . Fig. 3(a) further
conﬁrms the conclusion that the H 2 jet penetrates faster than
the N2 jet. In particular, the FTT time for H 2 jet is around 160t0,
which is about 40t 0 shorter than that of N 2 jet. This observa-
tion implies that the H 2 jet mixes more rapidly with the
ambient air than the respective N 2 jet. However, Fig. 3(b) in-
dicates that the jet maximum width for H 2 jet is generally
smaller than that of N 2 jet, which will result in a smaller
mixing area and is not favorable for fuel-air mixing.
Time-averaged jet ﬁeld
Fig. 4 shows the time-averaged streamwise velocities on the
centerline plane for H 2 and N 2 jets. As can be seen, the jets
expand rapidly after being injected from the high pressure
nozzle, and reach the highest velocity when approaching the
Mach disk. The maximum velocity for H
2 jet is around 2600 m/
s, which is much larger than the 700 m/s for N 2 jet. Those peak
velocities nearly double of the nozzle exit velocities U 1 for
both jets. Downstream from the Mach disk, the general ve-
locity patterns are similar and high-momentum region dis-
tributes along the annular regions for both jets. However, the
potential core of H
2 jet seems to be much longer than that of
N2 jet, which implies that there is more shock cells in H 2 jet
under the same NPR.
Fig. 5 shows the effect of fuel properties on the density
contours insides the jets. In particular, signiﬁcant differences
are observed in the annular shear layer where the N
2 jet has
much higher density values than the H 2 jet. This is under-
standable since the density of H2 jet is lower than that of N2 jet
at fully expanded conditions with the same initial pressure
and temperature, as indicated by Table 2 . The density at the
nozzle exit for N
2 jet is 3.37 kg/m 3, which is higher than the
ambient value r∞ ¼ 1.17 kg/m 3. On the contrary, the lower
molecular weight of H2 leads to a less dense jet with density of
0.24 kg/m 3 at the nozzle exit, which is much lower than the
ambient value r∞. The large differences in density for H 2 jet
with the ambient air will result in the intense ﬂow disconti-
nuities along the jet shear layer as seen in Fig. 6(a). In contrast,
the peak values of density gradient in N
2 jet are corresponding
to the shock structures in the ﬂow ﬁeld, which is shown in
Fig. 6(b).
In addition, the axial density values for N 2 jet after the
shock-containing ﬁeld (around y/D ¼ 10) remain higher than
the ambient values, so the density along the jet centerline
decrease to r
∞ gradually after the breakdown of the jet core,
which is shown in Fig. 7. On the other hand, the axial density
of H 2 jet increases almost linearly from around y/D ¼ 15,
which is near the end of jet core.
Shock structures
Fig. 8 presents the time-averaged near-ﬁeld shock structures
of N 2 jet predicted by LES in comparison with the available
literature data. As can be seen, the classical wave structures in
the near ﬁeld of a highly underexpanded jet including the
Mach disk, barrel shock, triple point, reﬂected shock and slip
lines which have been conﬁrmed by previous experimental
studies [9e12,16e19] and numerical work [20e25,28e30] are
all well captured by the present LES. In addition, the predicted
shock structures are in good agreement with the schlieren
photography shown in Fig. 8(b) measured by Yang (2012) [47]
at the same NPR of 5.60 over an exposure time of 0.6 ms.
The present LES result also compares reasonably with the
time-averaged concentration distribution shown in Fig. 8(c)
and (d) obtained in LES and PLIF at a similar NPR of 5.5 in
Ref. [29] in terms of the Mach disk height. Franquet et al. (2015)
[25] reviewed the available experimental data and indicated
that the Mach disk position of a highly underexpanded jet is
mainly governed by NPR and is independent of ﬂuid, while the
Mach disk diameter is strongly dependent on the nozzle ge-
ometry and shape. Therefore, the ﬁnding from Fig. 8(a) and (c)
that the LES performed in Ref. [29] predicts a much wider
Mach diameter than the present LES is mainly attributed to
the difference in nozzle geometry design and simulation set-
Table 1 e Grid resolution comparison in the near ﬁeld (r/D: ¡1.5 ~ 1.5; y/D: 0 e5D) of jets in the present and previous LES
modeling of supersonic jets.
Grid D (mm) Drmin Drmax Dymin Dymax Re Total ( /C2 106)
Present work 2.0 D/200 D/52 D/67 D/25 ~10 5 27.3
Liu et al. (2009) [27] 72.8 D/29 D/29 D/29 D/29 ~10 5 11.0
Dauptain et al. (2010) [43] 25.4 D/35 D/30 D/35 D/30 ~10 6 22.0
Rana et al. (2011) [46] 4.0 D/33 D/33 D/33 D/33 ~10 4 9.2
Vuorinen et al. (2013) [29] 1.4 D/70 D/50 D/35 D/25 ~10 5 12.0
Table 2 e Jet exit ﬂow conditions at the sonic oriﬁce.
Property Symbol Case Units
N2 H2
Mach number M 1 1.0 1.0 e
Static pressure P 1 0.3 0.3 MPa
Stagnation pressure P 0 0.57 0.57 MPa
Stagnation temperature T 0 360.0 360.0 K
Nozzle pressure
ratio (NPR)
P0/P∞ 5.60 5.60 e
Static pressure ratio P 1/P∞ 2.96 2.96 e
Ratio of speciﬁc heats r 1.4 1.4 e
Molecular Weight W 28 2 g/mol
Velocity at nozzle exit U 1 353.1 1321.3 m/s
Density r1 3.37 0.24 kg/m 3
Reynolds number
at nozzle exit
Re1 1.36 0.72 /C2 105
Nozzle density ratio
(NDR)
r1/r∞ 2.87 0.21 e
Ideal mass ﬂow rate _m 3.734 0.998 g/s
international journal of hydrogen energy 41 (2016) 5151 e51615154

<!-- PDF_PAGE: 5 -->

up (a slip condition for velocity is used inside the nozzle in
Ref. [29]).
Ashkenas and Sherman (1965) [10] developed an empirical
formula as Hdisk=D ¼ CH,
ﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ
NPR
p
to predict the Mach disk height
at NPR from 20 to 200. CH is a constant of 0.67. Ewan and
Moodie (1986) [13] observed experimentally a much smaller
value of CH z 0.55 for NPR <10. Fig. 9(a) presents the time-
averaged proﬁles of pressure along the jet centerline for H 2
and N2 jets, from which it can be seen that the locations of the
ﬁrst normal shock, i.e. the Mach disk, for both jets are highly
overlapped. This conﬁrms the conclusion proposed by Fran-
quet et al. (2015) [25] that the Mach disk position of a highly
underexpanded jet is independent of ﬂuid quantitatively. In
addition, the corresponding C
H value for both jets is 0.61,
which is between 0.55 and 0.67 yet close to 0.62 obtained by
Vuorinen et al. (2013) [29] at the similar NPR of 5.5 using LES
technique.
The mean proﬁle of fuel mass fraction shown in Fig. 9(b)
indicates that the H
2 jet has a much longer jet core of about
15D than the around 9D for N 2 jet. This is consistent with the
previous observations based on streamwise velocity and
density ﬁeld. More interestingly, Fig. 9 demonstrates that the
shock structures differ greatly in the jet core for H
2 and N2 jets
although the locations of the Mach disk are highly overlapped.
In particular, the locations of shocks for both jets are not
matched anymore after the Mach disk, and there are also
more shock cells in the H
2 jet. Nine shock cells can be
identiﬁed in the H 2 jet from Fig. 9(a), while there are only ﬁve
shock cells in the N 2 jet. It is also observed that the strength of
quasi-periodic shocks after the Mach disk is weaker in the H 2
jet than in the N 2 jet. This ﬁnding implies that the Mach disk
height of a highly underexpanded jet is mainly dominated by
the NPR as indicated by Ashkenas and Sherman (1965) [10] and
Franquet et al. (2015) [25] previously. However, the ﬂow ﬁeld
and shock structures after the Mach disk in a highly under-
expanded jet may also be affected strongly by the injected fuel
properties.
Dominant instability modes
Powell (1953) [31] observed experimentally that the supersonic
underexpanded jets will produce screech tone that dominates
all the other noise sources in the forward direction. This
behavior was attributed to the establishment of an acoustic
feedback formed of sound waves that were originated in the
downstream due to shock/shear layer interaction, and then
propagated upstream to force the initial shear layer at the
nozzle lip to generate new structures in the shear layer [31].
Gutmark et al. (1989) [33] and Powell et al. (1992) [34] observed
experimentally that the dominant instability modes of su-
personic screeching jets were affected strongly by NPR. In
particular, Powell et al. (1992) [34] indicated that the screech
tone of underexpanded circular jets changes successively
from an axially symmetric one to a ﬂapping one, a helical one,
t/t0
z(t)/D
0 50 100 150 200 250
5
10
15
20
25
30
35
40
H2
N2
(a)
z(t)/D
W(t)/D
0 5 10 15 20 25 30 35 400
2
4
6
8
10
12
H2
N2
(b)
Fig. 3 e (a) Non-dimensional jet penetration rate, (b) jet maximum width.
Fig. 2 e Time evolution of mass fraction Ys on the midline plane for H 2 and N2 jets. The instants are successively: (a) t/t 0 ¼ 36,
(b) t/t0 ¼ 64, and (c) t/t 0 ¼ 128, and respectively correspond to the initial phase, the transition phase, and the fully developed
ﬂow.
international journal of hydrogen energy 41 (2016) 5151 e5161 5155

<!-- PDF_PAGE: 6 -->

and ﬁnally a sinuous one as NPR increases from 2.0 to 5.84.
Tam et al. (1986) [32,35] derived the following formula to pre-
dict the shock screech frequency for a underexpanded jet of
Mach number Mj:
St ¼ fsDj
Uj
¼ 0:67
/C16
M2
j /C0 1
/C17 1=2
"
1 þ 0:7Mj
h
1 þð g /C0 1ÞM2
j
.
2
i1=2
/C18 T0
T∞
/C19 1=2
#/C0 1
(1)
where St is the Strouhal number, fs is the fundamental screech
frequency. Mj is the fully expanded jet Mach number, and Uj is
the fully expanded jet velocity, both of which can be calcu-
lated based on NPR according to the one-dimensional isen-
tropic equations. Dj is the fully expanded jet diameter [32,35].
The instantaneous density gradient on different cross-
section planes of N 2 jet shown in Fig. 10 presents an obvious
helical distribution, which implies that the N2 jet is dominated
by the helical mode. However, it is very interesting to ﬁnd that
the density gradient pattern looks like axisymmetric for H
2 jet,
which indicates that the dominant screech tone of H 2 jet is an
axisymmetric one.
Fast Fourier Transformation (FFT) of pressure ﬂuctuation
on either side of the jets at x/D ¼ 1, z/D ¼ 0 and x/D ¼/C0 1, z/
D ¼ 0 near the jet shear layer for different streamwise posi-
tions at y/D ¼ 2, 4, 6, 8, 10, 15 are implemented, and Fig. 11
shows the spectrum and relative phase at y/D ¼ 6a sa n
example. As can be seen, the N 2 jet has two discrete peaks.
One is fs ¼ 37.086 kHz, and the other is f2s ¼ 45.695 kHz. The
phase angles 4 for these two peak frequencies are /C0 177/C14 and
/C0 178/C14 respectively, and are both close to p and corresponding
to the helical modes. This is consistent with the previous
observation based on the instantaneous density gradient
shown in Fig. 10 . However, the spectrum for H 2 jet differs
greatly. The H 2 jet has a much high peak frequency of
fs ¼ 47.020 kHz. It is also found that there is some harmonics in
the spectrum of H 2 jet. In particular, the ﬁrst harmonics (2 fs),
the second harmonics (3 fs), and the third harmonics (4 fs)a ty /
D ¼ 6 can be clearly identiﬁed in H 2 jet. The longer jet core and
the more shock-cell structures in H 2 jet are believed to be the
main reason to cause the harmonics. But note that the phase
angles for the fundamental screech frequency f
s and the high-
order harmonics in H 2 jet are rather irregular, neither close to
0/C14 nor close to 180 /C14 .
In addition, the Strouhal number based on the second peak
frequency f2s ¼ 45.695 kHz for N 2 jet is 0.202, which is 8.2%
smaller than the prediction of 0.220 by Equation (1).I n
contrast, the Strouhal number based on the fundamental
screech frequency f
s ¼ 47.020 kHz for H2 jet is 0.208, and is 5.4%
smaller than the empirical prediction by Equation (1).
Mixing characteristics
The contour lines of fuel mass fraction (Y H2 or Y N2)i n Fig. 10
show that the N 2 jet has a much larger mixing area in the
downstream than the H 2 jet. To evaluate the jet mixing
properties quantitatively, the mixing area on cross-section
planes are computed based on the isoline of instantaneous
mass fraction, i.e. Y
H2 ¼ 0.02 for H2 jet and YN2 ¼ 0.77165 for N2
jet, both of which indicate the same mixture fraction level of
Z ¼ 0.02. The resulted mixing area is normalized by the nozzle
exit area A 1 and plotted as a function of streamwise positions
in Fig. 12 (a), while Fig. 12 (b) presents the ratio of mixing area
between the two jets.
Fig. 4 e Time averaged contours of streamwise velocities of
underexpanded jets on the centerline plane. (a) H 2 jet,
(b) N 2 jet.
Fig. 5 e Time-averaged contours of density on the jet
centerline plane. (a) H 2 jet, (b) N 2 jet.
Fig. 6 e Time-averaged density gradient on the jet
centerline plane. (a) H 2 jet, (b) N 2 jet.
y/D
ρ (kg/m
3
)[ N 2 ]
ρ (kg/m
3
)[ H 2 ]
0 5 10 15 20 25 300.0
1.0
2.0
3.0
4.0
0
0.1
0.2
0.3
0.4
H2
N2
Fig. 7 e Mean proﬁles of density along the jet centerline.
international journal of hydrogen energy 41 (2016) 5151 e51615156

<!-- PDF_PAGE: 7 -->

Fig. 13 illustrates the instantaneous snapshots of fuel mass
fraction on the jet centerline plane, visually showing the
mixing characteristics of highly underexpanded jets near the
jet boundary. As seen in Fig. 12(a), the non-dimensional mix-
ing area A* for N 2 jet in the near-ﬁeld region is rather small,
and jumps suddenly at y/D ¼ 6 because of the existence of
undulating vortex ring (see Fig. 2), then increases quickly from
around the end of jet core (i.e. at about y/D ¼ 8) as the jet
spreads toward the radial direction (see Fig. 13 ). The overall
trend of mixing area for H 2 jet is similar as that of N 2 jet, i.e. A*
is relatively small in the near-ﬁeld region and increases
gradually from the end of jet core. As indicated previously by
Fig. 9 , the jet core for H
2 jet is as long as about 15D, thus the
notable increase in the mixing area of H 2 jet can be observed
from y/D ¼ 16. Subsequently, the mixing area ratio between
the N2 jet and H2 jet increases from y/D ¼ 8 to y/D ¼ 16 mainly
due to the increase in mixing area of N 2 jet, and reaches to a
maximum value of about 9.0 at y/D ¼ 16, then decreases
gradually because of the increase in the mixing area of H 2 jet,
as shown in Fig. 12(b).
Besides the isoline of mixture faction level Z ¼ 0.02 marked
by the white lines to represent the jet boundary, the isoline of
vorticity magnitude equal to u ¼ 0.7U
1/D is also included in
Fig. 13 . In jet ﬂows, different ﬂow regimes are observed,
namely a fully turbulent region and a laminar outer ﬂow, the
two being separated by the so-called turbulent/non-turbulent
(T/NT) interface [48e51]. The interaction between the two
ﬂows at the interface leads to an exchange of mass, mo-
mentum, and scale quantities, thus the region of the T/NT
interface layer is of major importance for the mixing process
in a non-premixed combustion system.
The fully turbulent region is associated with vertical ﬂow,
while irrotational velocity ﬂuctuations are found in the non-
turbulent ﬂow outside the interface. As a result, the absolute
value of the vorticity is usually used to determine the T/NT
interface in the previous work [48e51]. For example, Bisset
et al. (2002) [48], Silva and Pereira (2008) [49], and Gampert
et al. (2014) [50] have employed the threshold of u ¼ 0.7U
1/D as
a T/NT interface detection criterion. In particular, Silva and
Pereira (2008) [49] examined the vorticity dynamics close to
this vorticity T/NT interface in a turbulent plane jet at
Rel z 120 using direct numerical simulation (DNS). Recently
Gampert et al. (2014) [51] studied the T/NT interface of a sub-
sonic free jet using LES and found that the agreement between
the experiments and simulation was more satisfactory for the
mixture fraction p.d.f (probability density function) with the
ﬁner LES. Generally the T/NT interface of a highly under-
expanded jet has been rarely investigated in the previous
work. Fig. 13 (a) and (b) show that isoline of Z ¼ 0.02 is very
close to the isoline of u ¼ 0.7U
1/D in the near-ﬁeld region for
both N2 and H2 jets. However, the T/NT interface identiﬁed by
u ¼ 0.7U1/D seems much narrower than the jet boundary
Fig. 8 e Comparison of time-averaged near-ﬁeld properties of highly underexpanded nitrogen jets at similar NPR between
the present LES prediction and the available literature data. (a) Density gradient (log 10ðjVrjÞ) obtained by the present LES,
NPR ¼ 5.60; (b) Schlieren photography [47], NPR ¼ 5.60; (c) Average concentration ( rYN2 ) obtained by LES [29], NPR ¼ 5.5;
(d) Average concentration ( rYN2 ) obtained using PLIF (Planar Laser Induced Fluorescence) technique [29], NPR ¼ 5.5.
y/D
P/P∞
0 5 10 15 20 25 300.0
0.5
1.0
1.5
2.0
2.5
3.0
H2
N2
(a)
y/D
Ys
0 5 10 15 20 25 300.0
0.2
0.4
0.6
0.8
1.0
1.2
H2
N2
(b)
Fig. 9 e Mean proﬁles of pressure and fuel mass fraction Ys
along the jet centerline. (a) pressure, (b) mass fraction Ys.
international journal of hydrogen energy 41 (2016) 5151 e5161 5157

<!-- PDF_PAGE: 8 -->

deﬁned according to Z ¼ 0.02 in the downstream of the jets. A
small region of N2 jet is shown in Fig. 13(c) in more detail, with
arrows representing the local velocity vector. As it can be
seen, the ambient air change its direction from the cross-
section direction to the streamwise direction when it is
transported across the jet boundary, which implies that the
ambient air is being entrained by the jet ﬂow and mixed with
the injection gas. It is also suggested that the fully turbulent
ﬂow region of jets is larger than that deﬁned based on the
traditional vorticity T/NT interface.
In addition, the second invariant Q [52] of the velocity
gradient tensor, deﬁned as Q ¼ (U
ijUij/C0 SijSij)/2 with Sij and Uij
representing the strain and rotation tensor respectively, is
often used to identify the coherent structures in turbulent
ﬂows. The three iso-surface of Q-criterion at 10 8 s/C0 2 is
compared with the iso-surface of vorticity for both jets in
Fig. 14 . As it can be seen, the iso-surface of Q-criterion is
characterized by lots of large scale coherent structures and
generally envelops the iso-surface of vorticity after the end of
jet core, which intuitively illustrates that the fully turbulent
region of the highly underexpanded jets is less predicted
based on the vorticity T/NT interface. These also indicates
that the traditional vorticity T/NT interface detection for
incompressible turbulent ﬂows, i.e. u ¼ 0.7U
1/D, may not be
suitable for underexpanded supersonic jets, and more effort
need to be devoted into this subject further.
Conclusion
In this study, large eddy simulations of highly underexpanded
hydrogen and nitrogen jets at the same NPR of 5.60 are carried
Fig. 11 e The cross spectrum and relative phase of pressure ﬂuctuation on either side of the jets at x/D ¼ 1, y/D ¼ 6, z/D ¼ 0
and x/D ¼¡ 1, y/D ¼ 6, z/D ¼ 0. The red lines indicate the amplitude while the green lines indicate the relative phase 4. (a) H2
jet, (b) N 2 jet. (For interpretation of the references to color in this ﬁgure legend, the reader is referred to the web version of
this article.)
Fig. 10 e Instantaneous snapshots of density gradient magnitude and contour lines of fuel mass fraction Ys on the cross-
section planes at different streamwise positions.
international journal of hydrogen energy 41 (2016) 5151 e51615158

<!-- PDF_PAGE: 9 -->

out using a supersonic compressible OpenFOAM solver,
astroFoam. The effects of fuel properties on the ﬂow charac-
teristic of the jets are examined in detail. The main ﬁndings of
the study are summarized as follows.
(1) The ﬂow evolution of H
2 jet at different time is similar
with that of N 2 jet. Quantitatively speaking, the H 2 jet
penetrates faster than the respective N 2 jet, but the
maximum width in radial direction for H 2 jet is much
smaller.
(2) The present LES results reproduce the classical near-
ﬁeld structures of highly underexpanded jets. Particu-
larly the Mach disk height of both jets is highly
matched, and is also similar to those presented in pre-
vious studies.
(3) At the given NPR, the ﬂow ﬁeld and the shock structures
after the Mach disk are strongly affected by the injected
fuel. The H
2 jet has much lower density values in the
annular shear layer than the N 2 jet because of the
smaller molecular weight. Meanwhile, the H 2 jet has a
much longer jet core and more shock cells.
(4) The screech tone of underexpanded jets is affected by
the injected fuel. The dominant instability mode is
Fig. 13 e Instantaneous snapshots of fuel mass fraction on
the jet centerline plane. (a) H 2 jet, Y H2 ¼ 0.02,
u ≈ 4.62 £ 105 s¡1, (b) N 2 jet, Y N2 ¼ 0.77165,
u ≈ 1.24 £ 105 s¡1, (c) The detail of N 2 jet showing the
mixing characteristics near the jet boundary. The arrows
in (c) represent the local velocity vector.
Fig. 14 e Three-dimensional iso-surfaces of the vorticity
(green, u ¼ 0.7U1/D) and Q-criterion (yellow, Q ¼ 108 s¡2). (a)
H2 jet, u ≈ 4.62 £ 105 s¡1, (b) N 2 jet, u ≈ 1.24 £ 105 s¡1. (For
interpretation of the references to color in this ﬁgure legend,
the reader is referred to the web version of this article.)
y/D
A*
0 5 10 15 20 25 30 35 400
30
60
90
120
150
180
210
240
H2
N2
(a)
y/D
AN2/AH2
0 5 10 15 20 25 30 35 400
2
4
6
8
10
(b)
Fig. 12 e (a) Time-averaged non-dimensional mixing area on cross-section planes at different streamwise positions.
(b) Mixing area ratio between the N 2 and H 2 jet.
international journal of hydrogen energy 41 (2016) 5151 e5161 5159

<!-- PDF_PAGE: 10 -->

helical for the N 2 jet, but is axisymmetric for the H 2 jet.
Two discrete peaks of fs ¼ 37.086 kHz and
f2s ¼ 45.695 kHz that correspond to the helical mode
both exist in the spectrum of the N 2 jet. The spectrum of
the H 2 jet is characterized by a fundamental screech
frequency of fs ¼ 47.020 kHz and its high-order
harmonics.
(5) The injected fuel has a relatively large inﬂuence on the
mixing properties of jets. The H 2 jet mixes more rapidly
with the ambient air than the N 2 jet, but has a much
smaller mixing area on cross-section planes. The mix-
ing area ratio between the N
2 jet and H 2 jet reaches a
maximum value of about 9.0 at around the end of jet
core of H 2 jet, then decreases gradually due to an in-
crease in the mixing area of H 2 jet. Mixing between the
ambient air and injection gas still takes places at the jet
boundary deﬁned according to mixture fraction
Z ¼ 0.02, and the fully turbulent region of the highly
underexpanded jets seems to be less predicted based on
the traditional vorticity T/NT interface for both N
2 and
H2 jets.
Acknowledgments
The Project was supported by the Foundation for Innovative
Research Groups of the National Natural Science Foundation
of China (Grant No. 10621202) and National Natural Science
Foundation of China (Grant No. 11502270).
references
[1] Segal C. The scramjet engine: processes and characteristics.
Cambridge University Press; 2009 .
[2] Keistler PG, Hassan HA, Xiao X. Simulation of supersonic
combustion in three-dimensional conﬁgurations. J Propuls
Power 2009;25(6):1233 e9.
[3] Won SH, Jeung IS, Parent B, Choi JY. Numerical investigation
of transverse hydrogen jet into supersonic crossﬂow using
detached-eddy simulation. AIAA J 2010;48(6):1047 e58.
[4] Cecere D, Ingenito A, Giacomazzi E, Romagnosi L, Bruno C.
Hydrogen/air supersonic combustion for future hypersonic
vehicles. Int J Hydrogen Energy 2011;36(18):11969 e84.
[5] Contreras A, Yi /C21git S, €Ozay K, Veziro /C21glu TN. Hydrogen as
aviation fuel: a comparison with hydrocarbon fuels. Int J
Hydrogen Energy 1997;22(10):1053 e60.
[6] White CM, Steeper RR, Lutz AE. The hydrogen-fueled internal
combustion engine: a technical review. Int J Hydrogen
Energy 2006;31(10):1292 e305.
[7] Brewer GD. Hydrogen usage in air transportation. Int J
Hydrogen Energy 1978;3(2):217 e29.
[8] Winter CJ. Hydrogen in high-speed air transportation. Int J
Hydrogen Energy 1990;15(8):579 e95.
[9] Adamson Jr TC, Nicholls JA. On the structure of jets from
highly underexpanded nozzles into still air. J Aerosp Sci
1959;26(1):16e24.
[10] Ashkenas H, Sherman F. Structures and utilization of
supersonic free jets in low density wind tunnels. NASA
Technical Report. 1965. No. CR-60423 .
[11] Crist S, Glass DR, Sherman PM. Study of the highly
underexpanded sonic jet. AIAA J 1966;4(1):68 e71.
[12] Donaldson CD, Snedeker RS. A study of free jet impingement.
Part 1. Mean properties of free and impinging jets. J Fluid
Mech 1971;45(2):281 e319.
[13] Ewan BCR, Moodie K. Structures and velocity measurements
in underexpanded jets. Combust Sci Technol
1986;45(5e6):275e88.
[14] Hill PG, Ouellette P. Transient turbulent gaseous fuel jets for
diesel engines. J Fluids Eng 1999;121:93 e101.
[15] Ouellette P, Hill PG. Turbulent transient gas injections. J
Fluids Eng 2000;122(4):743 e52.
[16] Bu¨ lent Yu
¨ ceil K, Volkan €Otu¨ gen M, Arik Engin.
Interferometric Rayleigh scattering and PIV measurements
in the near ﬁeld of underexpanded sonic jets. In: 41st
Aerospace Sciences Meeting and Exhibit, AIAA 2003-917.
[17] Andr/C19e B, Castelain T, Bailly C. Experimental exploration of
underexpanded supersonic jets. Shock Waves
2013;24(1):21e32.
[18] Mitchell D, Honnery D, Soria J. The underexpanded jet Mach
disk and its associated shear layer. Phys Fluids
2014;26(9):1e18.
[19] Rogers T, Petersen P, Koopmans L, Lappas P, Boretti A.
Structural characteristics of hydrogen and compressed
natural gas fuel jets. Int J Hydrogen Energy
2015;40(3):1584e97.
[20] Otobe Y, Kashimura H, Matsuo S. Inﬂuence of nozzle
geometry on the near-ﬁeld structures of a highly
underexpanded sonic jet. J Fluids Struct
2008;24(2):281 e93.
[21] Menon N, Skews BW. Shock wave conﬁgurations and ﬂow
structures in non-axisymmetric underexpanded sonic jets.
Shock Waves 2010;20(3):175 e90.
[22] Hatanaka K, Saito T. Inﬂuence of nozzle geometry on
underexpanded axisymmetric free jet characteristics. Shock
Waves 2012;22(5):427 e34.
[23] Velikorodny Alexey, Kudriakov Sergey. . Numerical study of
the near-ﬁeld of highly underexpanded turbulent gas jets. Int
J Hydrogen Energy 2012;37(22):17390 e9.
[24] Bonelli F, Viggiano A, Magi V. A numerical analysis of
hydrogen underexpanded jets under real gas assumption. J
Fluids Eng 2013;135(12):121101 .
[25] Franquet E, Perrier V, Gibout S, Bruel P. Free underexpanded
jets in a quiescent medium: a review. Prog Aerosp Sci
2015;77:25e53.
[26] Berland J, Bogey C, Bailly C. Numerical study of screech
generation in a planar supersonic jet. Phys Fluids
2007;19(7):075105.
[27] Liu JH, Kailasanath K, Ramamurti R, Munday D, Gutmark E,
Lohner R. Large-eddy simulations of a supersonic jet and
its near-ﬁeld acoustic properties. AIAA J
2009;47(8):1849 e65.
[28] Gorle C, Gamba M, Ham F. Investigation of an
underexpanded hydrogen jet in quiescent air using
numerical simulations and experiments. Stanford, CA:
Center for Turbulence Research Annual Research Briefs,
Center for Turbulence Research; 2010 .
[29] Vuorinen V, Yu JZ, Tirunagari S, Kaario O, Larmi M,
Duwig C, et al. Large-eddy simulation of highly
underexpanded transient gas jets. Phys Fluids
2013;25(1):016101 .
[30] Hamzehloo A, Aleiferis PG. Large eddy simulation of highly
turbulent under-expanded hydrogen and methane jets for
gaseous-fuelled internal combustion engines. Int J Hydrogen
Energy 2014;39(36):21275 e96.
[31] Powell A. On the mechanism of choked jet noise. Proc Phys
Soc Sect B 1953;66(12):1039 .
international journal of hydrogen energy 41 (2016) 5151 e51615160

<!-- PDF_PAGE: 11 -->

[32] Tam CKW, Seiner JM, Yu JC. Proposed relationship between
broadband shock associated noise and screech tones. J
Sound Vib 1986;110(2):309 e21.
[33] Gutmark E, Schadow KC, Bicker CJ. Mode switching in
supersonic circular jets. Phys Fluids 1989;1(5):868 e73.
[34] Powell A, Umeda Y, Ishii R. Observations of the oscillation
modes of choked circular jets. J Acoust Soc Am
1992;92(5):2823e36.
[35] Tam CKW. Supersonic jet noise. Annu Rev Fluid Mech
1995;27:17e43.
[36] Li XD, Gao JH. Numerical simulation of the three-
dimensional screech phenomenon from a circular jet. Phys
Fluids 2008;20(3):035101 .
[37] Greenshields CJ, Weller HG, Gasparini L, Reese JM.
Implementation of semi-discrete, non-staggered central
schemes in a colocated, polyhedral, ﬁnite volume
framework, for high-speed viscous ﬂows. Int J Numer
Methods Fluids 2010;63(1):1 e21.
[38] Kurganov A, Tadmor E. New high-resolution central schemes
for nonlinear conservation laws and convection-diffusion
equations. J Comput Phys 2000;160(1):241 e82.
[39] Vuorinen V, Wehrfritz A, Yu JZ, Kaario O, Larmi M,
Boersma BJ. Large-eddy simulation of subsonic jets. J Phys
Conf Ser IOP Publ 2011;318(3):032052 .
[40] Baba-Ahmadi MH, Tabor G. Inlet conditions for LES using
mapping and feedback control. Comput Fluids
2009;38(6):1299e311.
[41] Fureby C, Chapuis M, Fedina E, Karl S. CFD analysis of the
HyShot II scramjet combustor. Proc Combust Inst
2011;33(2):2399e405.
[42] Chapuis M, Fedina E, Fureby C. A computational study of the
HyShot II combustor performance. Proc Combust Inst
2013;34(2):2101e9.
[43] Dauptain A, Cuenot B, Gicquel LYM. Large eddy simulation of
stable supersonic jet impinging on ﬂat plate. AIAA J
2010;48(10):2325e38.
[44] Kawai S, Lele SK. Large-eddy simulation of jet mixing in
supersonic crossﬂows. AIAA J 2010;48(9):2063 e83.
[45] G/C19enin F, Menon S. Dynamics of sonic jet injection into
supersonic crossﬂow. J Turbul 2010;11(4):1 e30.
[46] Rana ZA, Thornber B, Drikakis D. Transverse jet injection
into a supersonic turbulent cross-ﬂow. Phys Fluids
2011;23(4):046103.
[47] Meng Yang. High speed pulsed schlieren technology and its
application to ﬂow visualization in supersonic combustion
[Master's Thesis]. Institute of Mechanics, Chinese Academy
of Science; 2012 [in Chinese] .
[48]
Bisset DK, Hunt JCR, Rogers M. The turbulent/non-turbulent
interface bounding a far wake. J Fluid Mech
2002;451:383e410.
[49] Da Silva CB, Pereira JCF. Invariants of the velocity-gradient,
rate-of-strain, and rate-of-rotation tensors across the
turbulent/nonturbulent interface in jets. Phys ﬂuids
2008;20(5):55101.
[50] Gampert M, Boschung J, Hennig F, Gauding M, Peters N. The
vorticity versus the scalar criterion for the detection of the
turbulent/non-turbulent interface. J Fluid Mech
2014;750:578e96.
[51] Gampert M, Kleinheinz K, Peters N, Pitsch H. Experimental
and numerical study of the scalar turbulent/non-turbulent
interface layer in a jet ﬂow. Flow Turbul Combust
2014;92(1e2):429e49.
[52] Dubief Y, Delcayre F. On coherent-vortex identiﬁcation in
turbulence. J Turbul 2000;1(1). 011 e011.
international journal of hydrogen energy 41 (2016) 5151 e5161 5161
