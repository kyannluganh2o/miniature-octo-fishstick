<!-- PDF_PAGE: 1 -->

Shock Waves (2016) 26:403–415
DOI 10.1007/s00193-015-0593-0
ORIGINAL ARTICLE
Shock waves in sprays: numerical study of secondary atomization
and experimental comparison
A. Chauvin1 · E. Daniel1 · A. Chinnayya2 · J. Massoni1 · G. Jourdan1
Received: 9 July 2014 / Revised: 30 June 2015 / Accepted: 4 August 2015 / Published online: 29 August 2015
© Springer-V erlag Berlin Heidelberg 2015
Abstract Numerical modeling of the interaction between
a cloud of water droplets and a planar shock wave is com-
pared with experimental data. The mathematical model relies
on an Eulerian description of the dispersed phase with the
assumption of dilute ﬂows. It is shown that the secondary
atomization of the droplets strongly inﬂuences the structure
of both the shock wave and the induced ﬂow. After shock
loading, the individual liquid components generate daughter
droplets, and the overall interphase surface per unit volume
undergoes strong variations which modify the pressure relax-
ation process towards a dynamic and thermal equilibrium
state. The experimental data enable one to determine the
best analytical formulation of the droplet number production
rate. Models of droplet number production rate are compared
in order to highlight this feature. The model based on the
assumption of linear variation of droplet diameter with time
gives the best agreement between the numerical results and
the experimental data.
Keywords Two-phase ﬂow · Shock wave · Spray ·
Secondary atomization · Fragmentation
Communicated by A. Hadjadj.
B E. Daniel
eric.daniel@univ-amu.fr
1 Aix-Marseille Université, CNRS, UMR IUSTI 7343, 5 rue E.
Fermi, 13013 Marseille, France
2 ENSMA, CNRS, Institut PRIME, UPR 3346, 1, Av. Clément
Ader, 86961 Futuroscope, France
1 Introduction
Dilute two-phase ﬂows appear in a wide range of engineering
and scientiﬁc applications, from safety up to energy produc-
tion. One key issue is the relaxation of a shock wave by
non-equilibrium phenomena in two-phase ﬂows, which has
been studied for more than 50 years. Carrier [ 1], Marble
[2], and Rudinger [ 3] investigated shock wave propagation
through particle-laden ﬂows. The dusty gas was composed
of solid particles immersed in a gaseous carrier phase. The
gas-particle mixture is considered as a continuous medium:
each phase is described by its own physical properties assum-
ing that the volume occupied by solid particles is negligibly
small. This assumption greatly simpliﬁes the mathematical
model and leads to the so-called dilute ﬂow model which is
used in the present work.
When a shock wave propagates through a two-phase
medium containing solid particles, the induced post-shock
pressure is not constant. The induced pressure jump decreases
as the shock wave propagates downstream the air-particle
mixture because of momentum and heat transfer [ 4,5]. The
overall structure of a shocked two-phase ﬂow is composed of
a precursor shock wave and a relaxation zone, where momen-
tum and heat transfer between the two phases take place until
the two-phase ﬂow reaches a new equilibrium. In such a case,
a ﬁxed pressure gauge would record a sudden pressure jump
induced by the transmitted shock wave followed by a pres-
sure increase to its equilibrium value.
However, if the dispersed phase is a low-viscosity liq-
uid such as water, it was shown in [ 6] that the shock wave
propagation differs greatly from the one observed in a solid
particle cloud. For a measurement station located inside the
two-phase medium, just after the pressure jump induced by
the transmitted shock wave, a pressure drop is observed. This
phenomenon was attributed to the breakup of the droplets [6].
123

<!-- PDF_PAGE: 2 -->

404 A. Chauvin et al.
The present study assesses to what extent atomization of
drops modiﬁes the two-phase post-shock ﬂow. Several mod-
els of secondary atomization are tested and are included in
a two-phase dilute ﬂow model solved in a one-dimensional
conﬁguration. Numerical and experimental results are com-
pared.
In this paper, two major points are emphasized. First, the
breakup phenomenon must be included in the model in order
to observe the pressure drop observed in experiments. The
second point is related to the modeling of the fragmenta-
tion process. V arious models were suggested [ 7,8]. They
depend on the main characteristics of the secondary atom-
ization, such as the total duration of the phenomenon and
the equilibrium diameter, and are generally deduced from
analyses carried out for a single droplet. In this study, mod-
els are extrapolated to a cloud of droplets and introduced in
an Eulerian/Eulerian approach. The importance of the formu-
lation of the droplet number production rate as source term is
pointed out before testing various estimations of secondary
atomization characteristic parameters. Eventually, this analy-
sis allows selecting the best breakup formulation and the best
associated correlations for two-phase ﬂow models based on
comparison with experimental pressure histories.
2 Experimental set-up
The interaction between a shock wave and a cloud of water
droplets was obtained experimentally in a 3795-mm-long
shock tube with a 8 × 8 cm square cross section, placed in a
vertical position as shown in Fig.1. Liquid water columns are
injected through a perforated plate located at the top of the
shock tube driven section. Then, Rayleigh–Plateau instabili-
ties act to break the column into droplets of known diameter,
linked to the jet diameter [ 9]. A cloud of droplets having
a mean diameter of 500 μm is generated. This two-phase
medium is released downwards from the shock tube top.
The shock wave, propagating upwards from the diaphragm,
encounters the cloud in the 880-mm-long visualization ﬁeld
composed of plexiglass windows. In the present case, the
interaction between the incident shock wave (Mach number
M
is = 1.49) impinging a 751 mm high cloud at the location
xint = 2959 mm is used for comparison with computational
results [6].
For each experiment, high speed visualization provided
the initial cloud position and quantitative displacements of
the downward moving cloud front. Pressure probes were
located at different stations starting from S
8 to S 1 and
recorded the pressure history. The pressure signals were then
used to observe the inﬂuence of the cloud of droplets on the
shock wave propagation.
The pressure sensors S
1 to S6 were covered with a 0.5-mm
layer of silicone, and their calibration was done by measuring
S1=3630 mm
S2=3520 mm
S3=3410 mm
S4=3190 mm
S5=3080 mm
S6=2970 mm
x0=0
Diaphragm x=750 mm
S7=2630 mm
S8=1770 mm
xt=3795 mm
S9=900 mm
S10=615 mm
S11=415 mm
S12=225 mm
S13=115 mm
rebmahclatnemirepxErebmahcerusserpwoLrebmahCerusserphgiH
Droplet generator
Shock wave
Cloud of droplets
xint
1025 mm2020mm750 mm
Fig. 1 Experimental apparatus of the shock tube used in [ 6]. xinit cor-
responds to the initial position of the droplet cloud before its interaction
with shock wave
the shock wave velocity between station S 8 and S7. Further
description of the experiment can be found in [ 6] and [10].
3 Mathematical model
Numerical investigations were carried out by solving the
unsteady one-dimensional two-phase ﬂow conservation equa-
tions. An Eulerian/Eulerian approach is used, leading to a
classical set of partial differential equations describing the
dynamics of dilute ﬂows given in ( 1a) and (1b)[ 11,12]. The
gaseous and the dispersed phases are described by conserva-
tion equations which are only coupled by the source terms
123

<!-- PDF_PAGE: 3 -->

Shock waves in sprays: numerical study of secondary atomization ... 405
as a consequence of the assumption of dilute ﬂows. These
source terms represent the main exchanges between the two
phases: the drag force and the convective heat transfer. The
mass transfer due to evaporation is assumed to have little
inﬂuence because the interaction is studied over a very short
time. The water cloud is assumed to be mono-disperse, the
droplets are taken as spherical with the same initial temper-
ature and velocity before their interactions with the shock
wave.
As secondary atomization can occur, a supplemental equa-
tion is required to model the droplet breakup phenomenon.
To be consistent with the global set of conservative equa-
tions, an equation for the number of droplets per unit volume
(n
d) is added. The fragmentation process is modeled as a
source term ˙n of the added equation, which represents the
droplet number production rate per time and volume unit. It
may contain terms due to collision, agglomeration, or frag-
mentation of droplets [7]. The initial volume fraction, which
compares the volume of water to the total volume of the
cloud, is around 1 %, hence the medium can be assumed to
be diluted. Therefore, the initial distance between droplets
is large enough to allow ignoring interaction between the
droplets. Indeed, during the time interval of interest, the
volume fraction goes from about 1 % to less than 10 %. Refer-
ring to Gelfand [ 13], the distance λ between droplets can be
estimated to be 2.7 and 0.7 diameters, respectively. Conse-
quently, the droplet coalescence or collisions were neglected
in the present study.
Gaseous phase
∂ρ
g
∂t + ∂
∂x
(
ρg ug
)
= 0
∂ρg ug
∂t + ∂
∂x
(
ρg u2
g + Pg
)
=− Fdrag
∂ρg Eg
∂t + ∂
∂x
(
ug
(
ρg Eg + Pg
))
=− Q − Fdragud (1a)
Dispersed phase
∂ρd
∂t + ∂
∂x (ρd ud) = 0
∂ρd ud
∂t + ∂
∂x
(
ρd u2
d
)
= Fdrag
∂ρd Ed
∂t + ∂
∂x (ρd ud Ed) = Q + Fdragud
∂nd
∂t + ∂
∂x (nd ud) =˙n (1b)
In this system of equation, the subscript g indicates the
gaseous phase and the subscript d signiﬁes the dispersed
medium; u and E are, respectively, the velocity and the total
speciﬁc energy of the phases, E = e + u2
2 with e being the
speciﬁc internal energy. Pg is the gas pressure andρg its den-
sity. The equation of state of the gaseous phase is the perfect
gas law Pg = ρg RTg . The apparent density of the dispersed
phase is deﬁned as ρd = αdρ∗ where ρ∗, the density of the
droplet material, is assumed constant and αd is the volume
fraction of the liquid phase. Note that the pressure in the
dispersed medium is neglected due to its level of dilution.
The source terms F
drag, Q, and ˙n are the drag force, the
convective heat transfer, and the droplet production rate due
to the breakup, respectively. The drag force obeys the fol-
lowing relation:
F
drag = π
8 ndρgφ2
d Cd
⏐⏐ug − ud
⏐⏐(
ug − ud
)
(2)
The drag coefﬁcient Cd used is an empirical relation from
Jourdan et al. [ 14] for a solid sphere suspended in a shock
tube. In this relation, φd deﬁnes the droplet diameter. This
correlation is pertinent because it was determined, thanks to
the acceleration of a single particle after the passage of the
shock wave, which is very similar to the conﬁguration of the
present study [ 6]:
log
10 (Cd) =− 0.695 + 1.259
(
log10
(
Rep
))
− 0.464
(
log10
(
Rep
)) 2
+ 0.045
(
log10
(
Rep
)) 3 (3)
Rep is the particulate Reynolds number deﬁned as Re p =
ρgφd|ug− ud|
μg . μg is the viscosity of the gas. The convective
heat term obeys the relation:
Q = ndπφd Nu λg(Tg − Td), (4)
where Tg and Td are the temperature of the gas and of the
droplet, respectively. λg is the air thermal conductivity. The
Nusselt number, Nu, is estimated from the Ranz-Marshall
correlation [15]:
Nu = 2 + 0.6Re1/2
p Pr1/3 (5)
The Prandtl number, Pr = 0.7, and the thermal conductivity
of the gas, λg are assumed to be constant.
The system of partial differential equations is solved by
the means of a Godunov scheme extended to high order
according to the MUSCL-Hancock method combined with a
minmod ﬂux limiter. The ﬂuxes are computed by using exact
Riemann solvers for both phases. The temporal stability is
ensured by choosing a CFL number equal to 0.9. A regular
mesh is employed with 1-mm length cells (a study of the grid
independence can be found in the Appendix). Details of the
numerical scheme can be found in [ 16].
123

<!-- PDF_PAGE: 4 -->

406 A. Chauvin et al.
4 Comparison of numerical and experimental
results in the absence of a fragmentation model
4.1 One-phase ﬂow
For checking the reliability of the numerical scheme, it was
compared with recorded pressures obtained at different sta-
tions in the shock tube in the absence of droplets.
Numerical and experimental tests were conducted corre-
sponding to the following initial conditions: incident shock
wave Mach number of Mach = 1.49, test gas air at 293 K.
The driver pressure is equal to 6.8 bar, and the driven section
pressure was kept at 1 bar. The time is set to zero when the
incident shock wave reaches station S
8 (Fig. 1) for both the
experimental and numerical cases.
In Fig. 2, the pressure signals measured at stations S 5 and
S2 are plotted for a relatively long time range. These stations
were chosen because in the studied two-phase ﬂow cases
these pressure gauges are placed inside the cloud of droplets,
near the lower and upper fronts, respectively. At station S
5,
the incident shock wave is very well reproduced both with
respect to its arrival time as well as the pressure jump. There is
a small difference between the two signals when the reﬂected
expansion wave reaches this location from the driver chamber
end-wall.
Moreover, the propagation of the reﬂected shock wave is
a bit faster in the numerical case. This may be explained by
the complex geometry due to the presence of the multi-holes
injectors. This fact is not modeled in the present study, in
which the bottom is taken as a perfectly ﬂat plate.
Finally, the largest discrepancy between the numerical and
the experimental arrival times of the incident shock waves is
about 30 μs, which is low in comparison to the studied time
(plateau duration). Concerning the reﬂected shock wave, the
maximum difference is about 0.1 ms.
4.2 Mandatory fragmentation modeling
The numerical solution computed for a two-phase system is
compared with experimental data [ 6]i nF i g .3. The droplet
production rate ˙n is set to 0. The analysis of pressure signals
obtained at measuring stations S
5 and S2, located inside the
two-phase medium, leads to three observations.
First, at the upper front, station S 2, the incident shock
wave arrival time is in good agreement with experiments.
The pressure behind the shock wave is overestimated in the
computation. Second, at stations S
5 and S2, the pressure jump
recorded in the experiment is followed immediately by a pres-
sure drop, which is not observed in the computational results.
Finally, the reﬂected shock wave from the driven section end-
wall arrives earlier in the numerical results, at about 6.5 ms
instead of 8 ms at S
5 and at nearly 5 ms instead of 6.5 ms
at S2. These discrepancies are signiﬁcantly greater than the
time accuracy observed in the one-phase case (0.1 ms). These
differences are most probably caused by the changes in the
droplet diameter observed in the experiments due to sec-
ondary atomization of droplets. In the present computations,
the droplets are not able to fragment: their diameter does
not change, and therefore, they have larger diameters than
those present in the experimental case where secondary atom-
ization occurs. The total interface surface is smaller. The
exchanges between the gas and the dispersed phase are not
enhanced by the increase of the total exchange surface of the
droplets. This induces, numerically, ﬁrst a greater pressure
jump in station S
2 and secondly the absence of a pressure
drop due to a regular increase of surface area because of
02468 1 0
Station 2 (3520 mm)
 Exp
 Num
t (ms)
02468 1 0
0
1
2
3
4
P (bar)
t (ms)
Station 5 (3080 mm)
 Exp
 Num
(a) (b)
Fig. 2 Comparison of experimental overpressure history and computation obtained in the absence of a droplet cloud
123

<!-- PDF_PAGE: 5 -->

Shock waves in sprays: numerical study of secondary atomization ... 407
02468 1 0
t (ms)
T80#665
 Exp
 Num
Station 2 (3520 mm)
02468 1 0
0
1
2
3
4
t (ms)
P (bar)
T80#665
 Exp
 Num
Station 5 (3080 mm) (a) (b)
Fig. 3 Comparison of experimental overpressures [ 6] and computational results in the absence of drop fragmentation
secondary atomization. It is therefore necessary to take into
account the droplet fragmentation in order to improve the
agreement between numerical and experimental results.
5 Fragmentation model for Eulerian approach
Droplets immersed in a ﬂow are exposed to shear forces
which tend to stretch the liquid, whereas the surface ten-
sion acts to maintain their shape and coherence. A stability
criterion of the droplet cohesion is deﬁned by a comparison
of these two forces based on the Weber number deﬁned by
[17]:
We = ρ
g
(
ug − ud
)2 φd
σ (6)
where σ is the surface tension of the droplet.
If the Weber number is greater than a critical value,
Wec, drop atomization occurs. According to various studies
reviewed by Guildenbecher et al. [ 18], Wec is about 11 ± 2
for an Ohnesorge number (Oh) lower than 0.1. This value
increases for Oh greater than 0.1, due to the increase of liquid
viscous forces. Hsiang and Faeth [19] reported that below this
value, the breakup regimes occur for constant Weber number,
which is the case in the present study.
The Ohnesorge number, deﬁned in the following equation,
compares the viscous forces with the surface tension and
inertia forces:
Oh = μ
d√ σρdφd
(7)
In an Eulerian approach, the individual characteristics of
droplets are replaced by averaged quantities for the dispersed
phase (1b). Consequently, the diameter of the droplets φd ,a s
any non-conservative quantity like temperature, is not strictly
an unknown of the system of equations. It can be deduced
from the apparent density, ρ
d , and the number per unit vol-
ume, nd , solved in the system of partial differential equations
using the following relation:
φd =
( 6ρd
πρ∗nd
) 1/3
. (8)
As the fragmentation is a constant mass process, it cannot
modify the dispersed phase continuity equation. The only
remaining possibility is to introduce the fragmentation model
in the number density conservation equation as˙n. Two points
of view are then possible in order to quantify the value of the
droplet number production rate ˙n.
The relaxation process depicting the breakup phenomenon
can be summarized as explained in the following scenario.
At the beginning, n
d droplets of diameter φd and mass m
undergo fragmentation because of a large velocity differ-
ence between them and the surrounding gas, a situation that
the capillary force cannot withstand. The diameter of the
daughter droplets tends toward the equilibrium value φ
c as
the number of droplets approaches the equilibrium value nc.
This relaxation phenomenon occurs during a characteristic
breakup time τbr. From this scenario, supported by experi-
mental evidence [13,18], two models can be formulated.
5.1 Linear variation of droplet diameter: LVDD model
The ﬁrst point of view consists of a linear decrease in the
diameter toφc, during the characteristic breakup time process
τbr. Then, the rate of diameter variation can be written as
[8,20]
123

<!-- PDF_PAGE: 6 -->

408 A. Chauvin et al.
˙φ = φc − φd
τbr
. (9)
Assuming the droplets are spherical, the mass conservation
implies
nd = nc
( φc
φd
) 3
. (10)
Taking the time derivative of (10) yields
dn d
dt = − 3nc
φd
( φc
φd
) 3
˙φ, (11)
which with ( 9) becomes
dn d
dt = 3nd
τbr
(
1 − φc
φd
)
(12)
This last expression is a way to estimate the source term ˙n.I n
the following, this model, based on the assumption of linear
variation of droplet diameter, is named the L VDD model.
5.2 Linear variation of droplet number model: LVDN
model
The second point of view assumes that during the character-
istic time τbr, the number of droplets nd decreases linearly
toward an equilibrium value nc [7,21]:
˙n = nc − nd
τbr
(13)
Note that this classical and frequently used formulation is
equivalent to that in Kolev [ 7] for a linear diminution of the
mother drop mass. Together with the mass conservation (10),
the above equation leads to
dn
dt = nd
(φd/φc)3 − 1
τbr
(14)
This model, based on the assumption of linear variation of
droplet number, is named the L VDN model in subsequent
sections.
Regardless of the model used, only the values of φc and
τbr have to be estimated in order to determine ˙n. Compar-
isons of results obtained from these two models are shown in
the following sections together with experimental ﬁndings.
The inﬂuence of the assumptions used, L VDN or L VDD, on
the production rate is shown as well as the inﬂuence of the
correlations of φ
c and τbr.
5.3 Maximum stable diameter
The maximum stable diameter φc is deﬁned as the diameter
of the largest drop created when fragmentation is completed.
The end of this process is indicated by a stability criterion
based on the critical Weber number We
c, deﬁned by Brodkey
[22]a s
Wec = 12
(
1 + 1.077 Oh1.6
)
. (15)
The maximum stable diameter φc can be deduced from the
stability criterion, using the Weber number deﬁnition and the
critical value. It is deﬁned as the maximum diameter below
which no atomization occurs by
φc = Wec
σ
ρg
(
ug − ud
)2 (16)
Note that in the range We ≤ Wec the droplets are in a stable
state.
Kolev [ 7] used an approximation of the ﬁnal diameter
based on the correlation of Hsiang and Faeth [ 23], for high
velocity ﬂows leading to
φc = 7.44√ Red
( ρd
ρg
) 0.25
φd 350
< We ≤ 1000 and 300 < Re ≤ 16,000 (17)
These two estimations forφc are implemented and compared
in the numerical L VDD model.
5.4 Total breakup time
The elapsed time from the beginning of the atomization of
a drop until the end of its fragmentation is deﬁned as the
total breakup time, τbr. Characteristic breakup times may be
given in a dimensionless form, T , as described by Ranger
and Nicholls [24]:
T = τ
⏐⏐ug − ud
⏐⏐
φd
√ρg
ρd
, (18)
where τ is the physical time.
Pilch and Erdman [ 25] offered approximations for the
dimensionless total breakup time, Tbr, based on experimental
observations at low Ohnesorge numbers:
Tbr = 6(We− 12)− 0.25 12 < We ≤ 18
Tbr = 2.45(We− 12)0.25 18 < We ≤ 45
Tbr = 14.1(We− 12)− 0.25 45 < We ≤ 351
Tbr = 0.766(We− 12)0.25 351 < We ≤ 2670
Tbr = 5.5W e > 2670 (19)
123

<!-- PDF_PAGE: 7 -->

Shock waves in sprays: numerical study of secondary atomization ... 409
Hsiang and Faeth [ 23] obtained the following correlation:
Tbr = 5
1 − Oh/7 We < 103 Oh < 3.5( 2 0 )
Nigmatulin [26] proposed
Tbr = 6
(
1 + 1.2Oh0.74)
ln(We)0.25 (21)
In Gelfand’s review [13], the total breakup time varies in the
following range (for Oh < 0.1):
4 < Tbr < 6( 2 2 )
6 Comparison of droplet production rate models
The inﬂuence of the two models proposed for droplet number
fragmentation rate ˙n is studied on the respective numerical
solutions of the ﬂow. In both models, the total atomization
time is estimated by ( 19), and the maximal stable diame-
ter is given in ( 16). A numerical Lagrangian probe, initially
located at 2962 mm upstream of the initial air/water interface,
allows recording the variation in the diameter of droplets (this
sensor moves with the gas velocity). The diameter evolution
with time measured by this Lagrangian sensor is presented in
Fig. 4, for both the L VDN and L VDD models. These two for-
mulations lead to signiﬁcantly different atomization features.
With the L VDN model, the equilibrium state of the droplet is
reached in 7μs instead of 250μs for the L VDD model. These
values have to be compared with the total breakup time range
165μs <τ
br < 265μs given by Gelfand [13] and presented
2.2 2.3 2.4 2.5 2.6 2.7 2.8 2.9 3.0
0
100
200
300
400
500
d ( m)
t (ms)
 LVDD model
 LVDN model
Fig. 4 Evolution of the diameter of the droplets with time for a
Lagrangian probe initially located at 2962 mm. Comparison between
the L VDD and the L VDN models
in (22). Consequently, the L VDD model yields a better agree-
ment with experimental results in terms of the secondary
atomization duration. As a consequence, the relaxation zone
is drastically reduced for the L VDN model, in comparison to
the one computed using the L VDD model.
Concerning the ﬁnal diameter, the L VDN model leads to
droplets of 22μm in diameter, whereas the L VDD model pre-
dicts a larger value: 46 μm. A droplet of 500 μm in diameter
exposed to a ﬂow ﬁeld induced by a shock wave with Mach
number 1.5 would generate droplets of maximum diameter
about 7 μm, using the estimate in ( 16) and the physical val-
ues given in Table 1. This critical diameter is estimated for
single droplet and constant ﬂow ﬁeld velocity. This assump-
tion is no longer valid when other droplets are present in the
surrounding. This environment change explains the discrep-
ancies observed in the ﬁnal diameter.
In Fig. 5, the evolution of both gas and droplet velocity is
presented for the two models. It is noticeable that dynamic
equilibrium is reached at the same time with the same velocity
in both cases but the unsteady stages are quite different (time
shorter than 2.8 ms).
The experimental and numerical pressure signals are com-
pared in Fig. 6,a ts t a t i o n sS
5 and S2. At station S 5, for both
models, the arrival time of the transmitted shock wave agrees
well with experimental results. Nevertheless, the L VDN
model leads to an underestimation of the pressure jump
which is not followed by a pressure drop. On the other hand,
the computational pressure signals obtained with the L VDD
model show good agreement with experimental ﬁndings for
both the arrival time of the transmitted shock wave and the
peak overpressure level.
The importance of using correct estimation of the source
term used for the droplet number production rate ˙n is thus
highlighted and is found to be crucial: an overestimation of
this term as calculated using the L VDN model leads to dif-
ferences between computational and experimental behavior
especially at short times.
Thus, the use of the L VDD model is highly recommended.
7 Inﬂuence of the total breakup time and
maximum stable diameter correlations
The inﬂuence of the correlations employed for the ﬁnal stable
diameter, φc, and the total breakup time, τbr, is studied using
the L VDD model.
7.1 Total breakup time
In this section, the critical diameter, φc, is computed using
(16) and τbr is deﬁned by three different approximations
offered by Pilch and Erdmann [ 25], Hsiang and Faeth [ 23],
and Nigmatulin [ 26].
123

<!-- PDF_PAGE: 8 -->

410 A. Chauvin et al.
Table 1 Main parameters and dimensionless numbers corresponding to the experiment [ 6]
Φd (μm)σ ( N.s− 1)ϱ d (kg.m− 3) Mis ug (m.s− 1)ϱ g (kg.m− 3) Re We Oh
500 7 .12 × 10− 2 10.5 1.49 238 2.2 14,000 824 4 .5 × 10− 3
2.5 3.0 3.5 4.0 4.5 5.0 5.5 6.0
0
50
100
150
200
250
u (m.s
-1
)
t (ms)
LVDN model
 ug
 ud
2 . 53 . 03 . 54 . 04 . 55 . 05 . 56 . 0
0
50
100
150
200
250u (m.s
-1
)
t (ms)
LVDD model
 ug
 ud
(a) (b)
Fig. 5 Evolution of gas and droplet velocities versus time for Lagrangian probe initially located at 2962 mm
2345678
t (ms)
Station 2 (3520 mm)
 Exp (T80#665)
 LVDD model
 LVDN model
2345678
0.0
0.5
1.0
1.5
2.0
2.5
3.0
3.5
P (bar)
t (ms)
Station 5 (3080 mm)
 Exp (T80#665)
 LVDD model
 LVDN model
(a) (b)
Fig. 6 Comparison of experimental overpressure history [ 6] and computation obtained for the two droplet numbers production rate models
As seen in Fig. 7, it appears that these approximations
do not present a signiﬁcant inﬂuence on the pressure signal
for a pressure probe located far from the interaction location
(station S 2). Moreover, the equilibrium pressure observed
at station S 5 is the same for the three formulae. Actually,
the approximation chosen has mainly an inﬂuence on the
transitory pressure near the location of the interaction, i.e.,
for short times as can be seen at S 5.
It is noticeable that no pressure drop is observed when
using Nigmatulin’s correlation.
Figure 8 shows the evolution of the droplet diameter versus
the time for the Lagrangian probe. No signiﬁcant differences
are observed regarding the ﬁnal diameter reached whatever
the approximation used and the Nigmatulin approximation
leads to the largest total breakup time.
Regarding the fragmentation times related to Fig. 8, Pilch
and Erdmann provide a numerical total breakup time of
around 230 μs, whereas for Hsiang and Faeth, it is near
290 μs and for Nigmatulin close to 360 μs. Recall that the
values estimated by Gelfand [ 13] suggested 165 μs <τ
br <
123

<!-- PDF_PAGE: 9 -->

Shock waves in sprays: numerical study of secondary atomization ... 411
2.0 2.5 3.0 3.5 4.0 4.5 5.0
0.0
0.5
1.0
1.5
2.0
2.5
3.0
P (bar)
t (ms)
Station 5 (3080 mm)
 Exp (T80#665)
 Pilch and Erdman (1987)
 Hsiang and Faeth  (1992)
 Nigmatulin (1991) 
(a)
2.0 2.5 3.0 3.5 4.0 4.5 5.0
(b)
t (ms)
Station 2 (3520 mm)
 Exp (T80#665)
 Pilch and Erdman (1987)
 Hsiang and Faeth  (1992)
 Nigmatulin (1991) 
Fig. 7 Comparison of experimental pressure history [ 6] and computation obtained with three different total breakup times τbr
2.2 2.3 2.4 2.5 2.6 2.7 2.8 2.9 3.0
0
100
200
300
400
500
d ( m)
t (ms)
 Pilch and Erdmann (1987)
 Hsiang and Faeth (1992)
 Nigmatulin (1991)
Fig. 8 Evolution of diameter of the droplets with time for a Lagrangian
probe initially located at 2962 mm for three correlations of total breakup
time
265μs. The Nigmatulin breakup time is signiﬁcantly higher
than Gelfand’s upper value. Consequently, one may think
that if the droplet secondary atomization takes longer time,
as suggested in the Nigmatulin results, the exchange between
the gas and the droplets is increased slowly. Therefore, the
numerical pressure drop seems to be related to the growth of
the interfacial surface in time.
7.2 Maximum stable diameter
In this section, the total breakup time τ
br is computed using
Pilch and Erdman’s correlation presented in ( 19). The inﬂu-
ence of the correlations for φc given in ( 16) and ( 17)i s
studied.
In Fig. 9, the computed pressure signals show that what-
ever is the correlation used for φc, a similar equilibrium
pressure is reached and so is the arrival of the transmitted
shock wave. Nevertheless, the pressure drop which was found
to be characteristic of the secondary atomization is not repro-
duced when using the correlation by Hsiang and Faeth [ 19].
The evolution in time of the droplet diameter for the
Lagrangian probe, presented in Fig. 10, provides an insight
into the absence of this pressure drop. The ﬁnal diameter
reached using the Hsiang and Faeth correlation is about
108 μm, whereas for the other correlation, it is about 47 μm.
The slope related to the diameter variation over time obtained
with the Hsiang and Faeth correlation is lower than the one
obtained when using the other ﬁnal diameter correlation.
It appears that in order to observe the characteristic pres-
sure drop, the numerical estimation of the droplet production
rate and more speciﬁcally the estimation of the diameter
variation over time, which corresponds to the variation of
interfacial surface, is crucial. If the slope of the diameter
variation with respect to time is too high, as with the L VDN
model, or too low, as with the Hsiang and Faeth approxima-
tion for φ
c, the pressure drop will not be observed.
The better the estimation of the variation of exchange sur-
face, the closer the numerical results for the pressure behavior
will be to the experimental ones. The L VDD model is rec-
ommended to be used with the total breakup time given by
Pilch and Erdmann [25]( 19) and the ﬁnal diameter obtained
with the critical Weber number deﬁnition ( 16).
8 Deformation stage
When a droplet is subjected to a ﬂow ﬁeld, two stages are
observed before complete atomization of the droplet occurs,
a deformation stage followed by a fragmentation stage [ 13].
123

<!-- PDF_PAGE: 10 -->

412 A. Chauvin et al.
2.0 2.5 3.0 3.5 4.0 4.5 5.0
0.0
0.5
1.0
1.5
2.0
2.5
3.0
(a)
P (bar)
t (ms)
Station 5 (3080 mm)
 Exp (T80#665)
 Definition Eq.16
 Hsiang and Faeth  (1992) 
2 . 02 . 53 . 03 . 54 . 04 . 55 . 0
(b)
t (ms)
Station 2 (3520 mm)
 Exp (T80#665)
 Definition Eq.16
 Hsiang and Faeth  (1992) 
Fig. 9 Comparison of experimental pressure history [ 6] and computation obtained with two different critical diameter
2.2 2.3 2.4 2.5 2.6 2.7 2.8 2.9 3.0
0
200
400
600
d (m)
t (ms)
 Definition Eq.16
 Hsiang and Faeth (1992)
Fig. 10 Evolution of diameter of droplets with time for a Lagrangian
probe initially located at 2962 mm for two approximations of critical
diameter
In the ﬁrst stage, the initial drop is ﬂattened to a lens shape
and expands in a transverse direction to the main ﬂow due to
a strong pressure gradient between the upstream and down-
stream stagnation points [27]. In previous studies [28,29], the
deformation stage of the droplet has been taken into account
in order to improve the L VDN model. It was shown that tak-
ing into account this stage with the L VDN model leads to the
observation of a pressure drop following the pressure peak,
as observed experimentally [ 6]. The inﬂuence of deforma-
tion time on the computed pressure history when using the
L VDD model is considered in the following.
8.1 Deformation stage model
During the deformation stage, the droplets are only ﬂattened
and no new droplets are created. Consequently, from the time
0n
0
brdef
d
c
0n
1
0n
t
0
Fig. 11 Schematic temporal evolution of fragmentation model includ-
ing a deformation stage
when the droplet is exposed to an unstable state(We > Wec)
until the end of its deformation period, no atomization occurs:
˙n is set to 0.
After this time, ˙n is computed with the L VDD model using
the Pilch and Erdmann approximation of τbr (19), and the
ﬁnal diameter is calculated using the Weber number deﬁni-
tion (16). In order to determine the elapsed time τ since the
drops are subjected to unstable conditions, another partial
differential equation is solved:
∂τ
∂t + ud
∂τ
∂x =˙τ, (23)
where ˙τ i ss e tt o0w h e nW e < Wec and equal to 1 when
fragmentation occurs, We > Wec.
This equation allows taking into account a delay in the
secondary atomization process, which corresponds to the
deformation phase. The scheme of the deformation stage
model is presented in Fig. 11.
Pilch and Erdman [25] presented a correlation of the char-
acteristic deformation time as
123

<!-- PDF_PAGE: 11 -->

Shock waves in sprays: numerical study of secondary atomization ... 413
Tdef = 1.9
(We− Wec)0.25
(
1 + 2.2Oh1.6
)
We < 104 Oh < 1.5( 2 4 )
Hsiang and Faeth [ 23] proposed
Tdef = 1.6
1 − Oh
7
We < 103 Oh < 3.5 (25)
Nigmatulin [26] suggested
Tdef = 2.6
(
1 + 1.5Oh0.74)
ln(We)0.25 (26)
2.4 2.5 2.6 2.7
0
200
400
d ( m)
t (ms)
 No delay
 Pilch Delay (1987)
 Hsiang Delay (1992)
 Nigmatulin Delay (1991)
Fig. 12 Evolution of droplet diameter with time for a Lagrangian probe
initially located at 2962 mm for three deformation time τdef approxi-
mations
8.2 Deformation stage results at constant diameter
The droplet diameter variation with time calculated by the
Lagrangian probe is presented in Fig. 12, when no delay is
considered and for the three deformation times presented in
(24)t o( 26). For times lower than the deformation time, the
droplet diameter is constant. Then, for the three approxima-
tions of the deformation time, the diameter evolution follows
the same tendency, until reaching the same equilibrium value,
but not at the same ﬁnal time.
The corresponding pressure signals are presented in
Fig. 13 at stations S
5 and S 2. For both stations, the delay
computed using the Pilch and Erdmann approximation is not
signiﬁcantly affected by the pressure evolution as compared
with the case when no delay was present. This deformation
time obtained by ( 24) being quite low as shown in Fig. 12
has no signiﬁcant inﬂuence on the pressure history. Never-
theless, at station S
5, for other correlations, the differences
are signiﬁcant: the pressure drop is reached later in the cases
of greater deformation times. At station S
2, far from the air/
cloud front, the pressure peak increases with the increase of
deformation time, and eventually, the results are worse than
those obtained with no delay.
As it can be seen with Nigmatulin’s deformation time
approximation, during the deformation phase, the cloud
behaves as if it was composed of solid particles: the pres-
sure jump induced by the transmitted shock wave is followed
by a pressure increase. Then, the secondary atomization of
the drops occurs (τ > τ
def). Thus, the interfacial surface
of exchanges between the gas and the drops is increased
which leads to a pressure decrease. Consequently, adding
a delay in the secondary atomization induces a pressure drop
with a delay in the range of the chosen deformation time.
Then, the pressure reaches an equilibrium value which is the
same value for allτ
def approximations. Far from the air-cloud
2.0 2.5 3.0 3.5 4.0 4.5 5.0
0.0
0.5
1.0
1.5
2.0
2.5
3.0
Station 5 (3080 mm)
 Exp T80#665
 No delay
 Pilch delay (1987)
 Hsiang delay (1992)
 Niglatulin delay (1991)
(a)
P (bar)
t (ms)
2.0 2.5 3.0 3.5 4.0 4.5 5.0
(b)Station 2 (3520 mm)
 Exp T80#665
 No delay
 Pilch delay (1987)
 Hsiang delay (1992)
 Niglatulin delay (1991)
t (ms)
Fig. 13 Inﬂuence on the pressure history of the deformation time correlations used
123

<!-- PDF_PAGE: 12 -->

414 A. Chauvin et al.
3.0 3.5 4.0 4.5 5.0 5.5 6.0
0.0
0.5
1.0
1.5
2.0
2.5
3.0
Station 2  (3520 mm)
T80#753        
  Exp      
  Num
P (bar)
t (ms)
Fig. 14 Comparison between the experimental overpressure history
and computation using the L VDD model. The shock wave Mach number
is 1.3. The spray is made of droplets of 500 μm in diameter, the volume
fraction is 0.25 %. The cloud is 739 mm high and x
int = 2945 mm
(T80#753).
interface, at S2, the pressure peak increases with deformation
time.
Taking into account the deformation stage leads to add
another parameter τdef . Its inclusion does not signiﬁcantly
improve the results. It leads to the creation of an evolution
in the exchange area. This stage may be of interest when
the L VDN model is used. When using the L VDD model, it
is recommended not to use the deformation stage. This last
model provides better agreement with experiments for all the
measurement stations than the L VDN model even when the
latter includes a deformation stage.
The L VDD model with the suggested approximations (16,
19) was computed for other conﬁgurations of shock/cloud
interactions. The experimental pressure signal of a planar
shock wave of Mach number 1.3 interacting at 2945 mm
with a two-phase medium with a volume fraction of 0.25
%, composed of droplets of 500 μm diameter, is presented
in Fig. 14. Good agreement is obtained between the experi-
mental and numerical pressure signals. The transmitted shock
wave and the pressure peak exhibit similar values in both
experimental and computational results. The pressure drop
is also observed in the computations, which demonstrates
a good prediction of the variation of the droplet diameter
with time. The use of the L VDD model is thus validated for
a shock wave interaction with a low volume fraction cloud
(α
d < 1%).
9 Conclusion
Computations of the interaction between a dilute two-phase
ﬂow and a planar shock wave were compared with experi-
mental results. The need to take into account the secondary
atomization of the droplets composing the cloud was ﬁrstly
highlighted. When the fragmentation of the droplets is not
considered, the pressure induced by the transmitted shock
wave was found to be overestimated. A new model for droplet
production rate was presented. It is based on the assumption
of linear variation of the droplet diameter (L VDD model).
This model was compared to a classical model based on the
assumption of linear variation of the droplet number. The
choice of the model for the secondary atomization produc-
tion rate was found to greatly inﬂuence the characteristic
pressure history. The L VDD model shows the best agreement
with experimental ﬁndings. Indeed, it is able to reproduce
the characteristic transient pressure observed experimentally
during the interaction between a planar shock wave and a
dilute cloud of droplets, which is undergoing the process of
atomization. The pressure jump is then followed by a pres-
sure drop. A study of the inﬂuence of the total breakup time
and an expression for the maximum stable diameter, required
to compute the droplet number production rate, emphasized
the need of a good prediction by computation of the droplet
number variation in time and by unit volume. It highlighted
the major inﬂuence of the estimation of the evolution of
interfacial area in time during the secondary atomization
process. If the variation of droplet diameter in time is too
slow, the characteristic pressure drop which follows the pres-
sure jump may not be observable. Moreover, if the droplet
production rate is too high, the droplets reach their ﬁnal diam-
eter in a very short time, which leads to an underestimated
pressure jump. Consequently, the observation of the charac-
teristic pressure history with a pressure drop related to the
secondary atomization of the drop is not possible. In order
to obtain computational results which are in good agreement
with experiments done for planar shock waves interacting
with a dilute medium, the use of the L VDD model is rec-
ommended with the estimation of the total breakup time as
given by Pilch and Erdman [ 25] and the maximum stable
diameter estimated by the stability criterion. Nevertheless,
some discrepancies can be seen at longer times between the
experimental and numerical pressure signals. These may be
due to the pressure gauges used which seem to be unable
to record the pressure at the correct level for a long time.
The physical model of the droplet phase may be improved
by taking into account a more accurate thermodynamical
behavior for the droplets via a speciﬁc equation of state.
The droplet phase density would be changed because of the
sudden variation of the pressure, leading to a change in the
droplet diameter. The second important point to be improved
is a better representation of the diameter distribution of the
droplet cloud.
Acknowledgments The authors would like to thank DGA-Tn for sup-
porting this study and Robert Tosello for valuable discussions.
123

<!-- PDF_PAGE: 13 -->

Shock waves in sprays: numerical study of secondary atomization ... 415
Appendix
Although the numerical method is detailed in [16], it is impor-
tant for this speciﬁc unsteady application to verify the grid
independence of the solutions. V arious meshes are tested on
the simulations presented in Sect. 7. Mesh 1 corresponds to
the one used in the present study (dx = 1 mm), the cell is then
divided by two (Mesh 2), and the third mesh d x = 0.25 mm
(Mesh 3). The pressure evolution along the shock tube axis
is plotted at time t = 4.5 ms for these different meshes.
This pressure evolution shows that each wave pattern (expan-
sion fan, shock wave, interaction with the droplet cloud) is
computed in the same way regardless of the mesh used. The
differences are quite negligible and cannot be seen on this
ﬁgure (Fig. 15), and one can state that the results are inde-
pendent of the grid.
Fig. 15 Inﬂuence of the mesh size on the pressure evolution along the
shock tube axis
References
1. Carrier, G.F.: Shock waves in a dusty gas. J. Fluid Mech.4, 376–385
(1958)
2. Marble, F.E.: Dynamics of a gas containing small solid particles.
Comb. Propuls. Fifth AGARD Colloq. 7, 175–213 (1963)
3. Rudinger, G.: Some properties of shock relaxation in gas ﬂows
carrying small particles. Phys. Fluids 7, 658–663 (1964)
4. Sommerfeld, M.: The unsteadiness of shock waves propagating
through gas-particle mixtures. Exp. Fluids 3, 197–206 (1985)
5. Outa, E., Tajima, K., Morii, H.: Experiments and analyses on shock
waves propagating through a gas-particle mixture. Bull. Jpn. Soc.
Mech. Eng. 19(130), 384–394 (1976)
6. Chauvin, A., Jourdan, G., Daniel, E., Houas, L., Tosello, R.: Exper-
imental investigation of the propagation of a planar shock wave
through a two-phase gas-liquid medium. Phys. Fluids 23, 113301
(2011)
7. Kolev, N.I.: Multiphase Flow Dynamics 2. Mechanical and Ther-
mal Interactions, Springer, 2 (2002)
8. V erhagean, J.: Modélisation multiphasique d’écoulements et de
phénomènes de dispersion issus d’explosion (2011), PhD manu-
script, Aix-Marseille University, France
9. Tyler, E.: Instability of liquid jets. Philos. Magazine Series 7
16(105), 504–518 (1933)
10. Jourdan, G., Daniel, E., Houas, L., Tosello, R.: Attenuation of a
shock wave passing through a cloud of water droplets. Shock Waves
20, 285–296 (2010)
11. Daniel, E., Saurel, R., Loraud, J.C., Larini, M.: A multiphase for-
mulation for two phase ﬂows. Int. J. Num. Methods Fluid Flows 4,
269–280 (1994)
12. Saurel, R., Daniel, E., Loraud, J.C.: Two phase ﬂows: second
order schemes and boundary conditions. AIAA J. 32(6), 1214–
1221 (1994)
13. Gelfand, B.E.: Droplet breakup phenomena in ﬂows with velocity
lag. Prog. Energy. Combust. Sci. 22, 201–265 (1996)
14. Jourdan, G., Houas, L., Igra, O., Estivalezes, J.L., Devals, C.,
Meshkov, E.E.: Drag coefﬁcient of a sphere in a non-stationary
ﬂow: new results. Proc. R. Soc. A 463(2088), 3323–3345 (2007)
15. Ranz, W.E., Marshall, W.R.: Spray simulation—evaporation from
drop. Chem. Eng. Prog. 48, 141–173 (1952)
16. Thevand, N., Daniel, E., Loraud, J.C.: On high resolution schemes
for compressible viscous two-phase dilute ﬂows. Int. J. Numer.
Meth. Fluids 31, 681–702 (1999)
17. Weber, C.: Zum zerfall eines ﬂüssigkeitsstrahles. Z. Angew. Math.
Mech. 11, 136–154 (1931)
18. Guildenbecher, D.R., Lopez-Rivera, C., Sojka, P .E.: Secondary
atomization. Exp. Fluids 46, 371–402 (2009)
19. Hsiang, L.P ., Faeth, G.M.: Drop deformation and breakup due to
shock wave and steady disturbances. Int. J. Multiph. Flow21, 545–
560 (1995)
20. Zeoli, N., Gu, S.: Numerical modelling of droplet break-up for gas
atomization. Comput. Mat. Sci. 38(2), 282–292 (2006)
21. Utheza, F., Saurel, R., Daniel, E., Loraud, J.C.: Multiphase ﬂow
dynamics 2. Droplet break-up through an oblique shock wave.
Shock Waves 5, 265–273 (1996)
22. Brodkey, R.S.: The Phenomena of Fluid Motions. Addison-Wesley,
Reading Mass (1967)
23. Hsiang, L.P ., Faeth, G.M.: Near-limit drop deformation and sec-
ondary breakup. Int. J. Multiph. Flow 18, 635–652 (1992)
24. Ranger, A.A., Nicholls, J.A.: Aerodynamic shattering of liquid
drops. AIAA 7, 285–290 (1969)
25. Pilch, M., Erdman, C.A.: Use of break-up time data to predict the
maximum size of stable fragment for acceleration induced breakup
of a liquid drop. Int. J. Multiph. Flow 16, 741–757 (1987)
26. Nigmatulin, R.I.: Dynamics of Multiphase Media. Hemisphere
Publishing Company, New york (1991)
27. Joseph, D.D., Belanger, J., Beavers, G.S.: Breakup of a liquid drop
suddenly exposed to a high-speed airstream. Int. J. Multiph. Flow
25, 1263–1303 (1999)
28. Chauvin, A., Jourdan, G., Daniel, E., Houas, L., Tosello, R.: Study
of the interaction between a shock wave and a cloud of droplets,
28th International Symposium on Shock Waves,2, 39-44, Springer
Berlin Heidelberg (2012)
29. Del Prete, E., Haas, J.-F., Chauvin, A., Jourdan, G., Chinnayya,
A., Hadjadj, A.: Secondary atomization on two-phase shock wave
structure, 28th International Symposium on Shock Waves, 2, 95-
100, Springer Berlin Heidelberg (2012)
30. Wierzba, A., Takayama, K.: Experimental investigation of the aero-
dynamic breakup of liquid drops. AIAA J. 26, 1329–1335 (1988)
123
