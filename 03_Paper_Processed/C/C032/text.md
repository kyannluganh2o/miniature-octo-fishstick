<!-- PDF_PAGE: 1 -->

Full Length Article
Aerodynamic breakup of an n-decane droplet in a high temperature gas
environment
George Strotos a,b,⇑, Ilias Malgarinos a, Nikos Nikolopoulos a,c, Manolis Gavaises a
a School of Engineering and Mathematical Sciences, City University London, Northampton Square, EC1V 0HB London, UK
b Technological Education Institute of Piraeus, Mechanical Engineering Department, Fluid Mechanics Laboratory, 250 Thivon and P. Ralli str., Aigal eo 12244, Greece
c Centre for Research and Technology Hellas/Chemical Process and Energy Resources Institute (CERTH/CPERI), Egialeias 52, Marousi, Greece
article info
Article history:
Received 7 May 2016
Received in revised form 29 July 2016
Accepted 1 August 2016
Available online 6 August 2016
Keywords:
Droplet breakup
VOF
Heating
Evaporation
abstract
The aerodynamic droplet breakup under the inﬂuence of heating and evaporation is studied numerically
by solving the Navier-Stokes, energy and transport of species conservation equations; the VOF
methodology is utilized in order to capture the liquid-air interphase. The conditions examined refer to
an n-decane droplet with Weber numbers in the range 15–90 and gas phase temperatures in the range
600–1000 K at atmospheric pressure. To assess the effect of heating, the same cases are also examined
under isothermal conditions and assuming constant physical properties of the liquid and surrounding
air. Under non-isothermal conditions, the surface tension coefﬁcient decreases due to the droplet heat-
up and promotes breakup. This is more evident for the cases of lower Weber number and higher gas
phase temperature. The present results are also compared against previously published ones for a more
volatile n-heptane droplet and reveal that fuels with a lower volatility are more prone to breakup. A 0-D
model accounting for the temporal variation of the heat/mass transfer numbers is proposed, able to
predict with sufﬁcient accuracy the thermal behavior of the deformed droplet.
/C2112016 Elsevier Ltd. All rights reserved.
1. Introduction
The efﬁciency of spray combustion systems is determined by
the dispersion of the spray droplets which increase the surface area
and subsequently the rates of heat and mass transfer. Following
the primary jet breakup, the produced droplets are subjected to
secondary breakup which further enhances the heat/mass transfer
rates. The coupled problem of secondary droplet breakup under
the inﬂuence of heating and evaporation is of major engineering
interest, but due to its complexity has not been yet addressed in
detail and the vast majority of relevant works examine these two
phenomena independently.
Droplets under the inﬂuence of aerodynamic forces are sub-
jected to different breakup modes, namely the bag breakup, the
transitional breakup, the sheet-thinning breakup and the catas-
trophic breakup; for details see Guildenbecher et al. [1] among
many others. The outcome of the breakup is determined by the rel-
ative strength of the aerodynamic, surface tension, viscous and
external body forces acting on the droplet. These are grouped into
dimensionless numbers, forming the Weber number ( We), the Rey-
nolds number ( Re), the Ohnesorge number ( Oh), the density ratio
(e) and the viscosity ratio ( N), as shown in Eq. (1), while under cer-
tain ﬂow conditions other parameters such as the Froude number,
the Mach number and the turbulence levels may become
important.
We ¼ qg U2
rel;0D0
r Re ¼ qg Urel;0D0
lg
Oh ¼ llﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ ﬃ
qlrD0
p
e ¼ ql
qg
N ¼ ll
lg
ð1Þ
The phenomena observed during droplet breakup have been
addressed in review studies such as those of [1–5] among others;
it is generally considered that the We number is the most inﬂuen-
tial parameter, while viscous effects become important when
Oh > 0.1. The breakup process requires some ﬁnite time to be
established and the duration of the phenomenon is in the order
of the shear breakup timescale t
sh proposed by Nicholls and Ranger
[6]:
tsh ¼ D0
Urel;0
ﬃﬃ ﬃ
e
p
ð2Þ
http://dx.doi.org/10.1016/j.fuel.2016.08.014
0016-2361//C2112016 Elsevier Ltd. All rights reserved.
⇑ Corresponding author at: School of Engineering and Mathematical Sciences,
City University London, Northampton Square, EC1V 0HB London, UK.
E-mail addresses: George.Strotos.1@city.ac.uk, gstrot@teipir.gr (G. Strotos),
Ilias.Malgarinos.1@city.ac.uk (I. Malgarinos), Nikolaos.Nikolopoulos.1@city.ac.uk,
n.nikolopoulos@certh.gr (N. Nikolopoulos), M.Gavaises@city.ac.uk (M. Gavaises).
Fuel 185 (2016) 370–380
Contents lists available at ScienceDirect
Fuel
journal homepage: www.else vier.com/locate/fuel

<!-- PDF_PAGE: 2 -->

Many works have studied either experimentally or numerically
the droplet breakup, aiming to enlighten the conditions leading to
the different breakup regimes and the underlying physics. Selective
experimental studies on droplet breakup are those of [7–22] but
generally, there is a scattering of the experimental ﬁndings which
is probably due to the variety of the experimental techniques used
and the experimental uncertainties. Numerical works aiming to ﬁll
the gap in knowledge such as those of [23–32]; they have examined
the isothermal droplet breakup in 2-D and 3-D computational
domains and they have provided useful information into the
detailed processes inside and in the vicinity of the droplets during
droplet breakup, which are difﬁcult to be determined with experi-
mental techniques. More speciﬁcally, [7–10] provided breakup
maps in the We-Oh plane, [11–13,16] further clariﬁed the bound-
aries between different breakup regimes, [14,15,20,23,25,30,31]
clariﬁed the physical mechanisms behind the breakup regimes,
[13,18] examined the size distribution of the child droplets after
the parent droplet disintegration, [22] identiﬁed experimentally
the gas ﬂow structure during droplet breakup, [15,24,26,32]
examined the effect of density ratio and [26,27,29,31] examined
the droplet drag coefﬁcient. For a detailed presentation of the works
referring to droplet breakup, see Strotos et al. [33].
Regarding the evaporation studies, in addition to 0-D or 1-D
models (see details in the review articles of [34–37] among others),
detailed CFD works solving the complete Navier-Stokes and
heat/mass transfer equations have also been published. Selectively,
the works of [38–47] refer to single component evaporation and
[48–53] refer to multicomponent droplet evaporation, providing
detailed information in the transport processes between the liquid
and the gas phase. More speciﬁcally, [39,40] were the ﬁrst who
solved the complete set of the governing equations, [42,47]
modelled the presence of the suspender, [43] examined the effect
of thermocapillary ﬂow, [44] studied the effect of turbulence and
[46] proposed numerical improvements for the evaporation mod-
elling. Similarly, in multicomponent studies the ﬁrst ones were those
of [48,49], followed by [50] who included variable thermophysical
properties and [52,53] which conducted parametric studies. The
aforementioned studies were restricted to the modelling of isolated
spherical droplets and a detailed presentation of the works referring
to droplet evaporation, was given in Strotos et al. [54].
Regarding the coupled problem of droplet breakup and evapo-
ration, this has not yet been studied in detail except in the CFD
works of [55–60]. Haywood et al. [55,56] showed that for droplets
under steady or unsteady (oscillatory) deformation, the quasi-
steady correlations for Nusselt ( Nu) and Sherwood ( Sh) numbers
are still valid when a volume-equivalent diameter is used, Mao
et al. [57] showed that the mass transfer from deformed droplets
is mainly controlled by the Peclet ( Pe) number, while the We
num-
ber has a small impact only at high Pe numbers. Hase and Weigand
[58] studied the effect of droplet deformation on the heat transfer
enhancement and they found that this increases due to the oscilla-
tory droplet motion and the increased surface area of the deformed
droplets; moreover, the steady-state classical correlations for the
Nu number, under-predict the heat transfer at the beginning of
the simulation. Later, Schlottke et al. [59] included the evaporation
in their model and they found that the droplet heating is affected
by the ﬂow ﬁeld inside the droplet which transfers hotter ﬂuid
from the droplet surface towards inside. Cerqueira et al. [60] stud-
ied spherical and deformed rising bubbles and proposed new cor-
relations for the Nu and Sh numbers.
Nomenclature
Roman symbols
BM mass transfer Spalding number [–]
BT heat transfer Spalding number [–]
cp heat capacity [J/kg K]
D diameter [m]
DAB vapor diffusion coefﬁcient [m 2/s]
Fheat heating factor [–]
Oh Ohnesorge number Oh ¼ ll=
ﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ ﬃ
qlrD0
p
[–]
k thermal conductivity [W/mK]
L latent heat of vaporization [J/kg]
m mass [kg]
_m00 evaporation rate per unit area [kg/m 2 s]
Nu Nusselt number [–]
Pr Prandtl number [–]
R radius [m]
Re Reynolds number Re ¼ qg Urel;0D0=lg [–]
S surface area [m 2]
Sc Schmidt number [–]
Sh Sherwood number [–]
t time [s]
tsh shear breakup timescale tsh ¼ D ﬃﬃ ﬃep =U [–]
T temperature [K]
U reference velocity [m/s]
u instantaneous droplet velocity [m/s]
V volume [m 3]
We Weber number We ¼ qg U2
rel;0D0=r [–]
Wet instantaneous We number [–]
Y vapor concentration [kg/kg]
Greek symbols
a thermal diffusivity [m 2/s]
c thermal effusivity c ¼
ﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ ﬃ
kqcp
p
[J/m2 Ks 0.5]
e density ratio e ¼ ql=qg [–]
l viscosity [kg/ms]
N viscosity ratio N ¼ ll=lg [–]
v kinematic viscosity [m 2/s]
q density [kg/m 3]
r surface tension coefﬁcient [N/m]
Subscripts
0 initial
c cross-stream
cr critical
g gas
l liquid
rel relative
s at surface
t instantaneous magnitude
x, y, z coordinates
1 free-stream conditions
Abbreviations
C07 n-heptane C
7H16
C10 n-decane C 10H22
CFD Computational Fluid Dynamics
cpR Cells per Radius
CSS Continuum Surface Stress
UDF User Deﬁned Function
VOF Volume of Fluid
G. Strotos et al. / Fuel 185 (2016) 370–380 371

<!-- PDF_PAGE: 3 -->

The aforementioned studies were restricted to We number
below 10, which limits the results to small droplet deformation
without breakup. Recently, Strotos et al. [61] examined the effect
of heating and evaporation in cases undergoing breakup for
We = 15–90. They examined volatile n-heptane droplets and they
showed that the droplet heating becomes increasingly inﬂuential
during breakup for lower We number and higher gas temperature.
The present numerical work is a continuation of this work and
examines an n-decane droplet with substantially lower volatility
than the n-heptane; this promotes the higher heating of the droplet.
This work is the ﬁrst examining the combined effect of heating and
breakup solving the Navier-Stokes, energy and transport of species
equations coupled with interface capturing, for a wide range of We
numbers, gas phase temperatures for this particular fuel while it
compares it with the less volatile one for similar ﬂow conditions.
The structure of the paper includes a brief description of the numer-
ical model and the cases examined, followed by the results, while
the most important conclusions are summarized at the end.
2. Numerical model and methodology
The continuous ﬁeld representation of the two-phase ﬂow with
the VOF methodology is used to study the droplet breakup. The
problem is assumed to be 2-D axisymmetric and an automatic local
grid reﬁnement technique [62,63] enhances the accuracy of the
computations at the interface region, while achieving low computa-
tional cost compared to a simulation with a uniform grid of the same
density. The droplet heating and evaporation are accounted for by
solving the energy and vapor transport equations, while the local
evaporation rate is obtained by using a model based on Fick’s law,
which is independent of the droplet shape. The species properties
depend on the local temperature [64,65] and mass averaging rules
are used for the gaseous mixture assuming incompressible ideal
gas. For the complete presentation of the equations solved, the
reader is referred to Strotos et al. [54]. The simulations were per-
formed with the commercial CFD tool ANSYS FLUENT v14.5 [66]
and the numerical settings adopted as also the User Deﬁned Func-
tions (UDFs) are identical to those used in Strotos et al. [61].
The model has been successfully validated in[33,54,63,67,68] for
cases including the motion of a free falling droplet, droplet breakup,
droplet evaporation and droplet impact onto a solid substrate.
3. Results and discussion
3.1. Cases examined and numerical setup
The cases examined are similar to those presented in Strotos
et al. [61] for a volatile n-heptane droplet (C07), but this time an
n-decane (C10) droplet is examined which has a much lower
volatility (i.e. vapor pressure) than the n-heptane. The cases exam-
ined refer to a small 100
lm diameter droplet with an initial tem-
perature of T0 = 300 K, corresponding to Oh = 0.02 which is low
enough to guarantee breakup process almost independent from
the Oh number. The droplet is assumed to be initially motionless
and it is subjected to a step change of the gas phase velocity lead-
ing to We numbers in the range 15–90. The ambient air has a high
temperature in the range 600–1000 K ( Tcr,C10 = 617.7 K) which cor-
respond to high density and viscosity ratios ( e > 1200 and N >2 0
respectively) and thus the breakup outcome is not affected by
them since e >3 2 [24]. The aforementioned combination of We
numbers and gas phase temperatures corresponds to gas phase
velocities in the range 77–243 m/s; these in turn correspond to
Re numbers in the range 84–367 which ensures that the ﬂow
remains laminar and axisymmetric [69,70]; the Mach numbers
are below 0.38, which implies that the compressibility effects can
be ignored. For all cases examined, the ambient pressure is
atmospheric; thus no modiﬁcations capturing high pressure effects
are required in the evaporation model. A graphical representation
of the cases examined is shown in Fig. 1 on the We-Re map. These
cases were examined both for evaporating and isothermal condi-
tions. For the latter, the energy equation and the evaporation
source terms were not accounted for, while the species properties
were kept constant at their reference temperature values, i.e. at
T0 = 300 K for the liquid droplet and at T1 for the surrounding
air; the isothermal runs correspond to a parametric study for the
effect of We and Re numbers.
Regarding the computational domain and the boundary condi-
tions, these are the same as in Strotos et al. [33,61,68], in which
a step change of the gas phase velocity is applied around the ini-
tially motionless droplet; the 2-D axisymmetric computational
domain is moving with the average translational droplet velocity.
Upwind the droplet, Dirichlet boundary conditions were applied
(i.e. ﬁxed velocity and temperature for the non-isothermal cases)
and downwind Neumann boundary conditions (i.e. zero ﬁrst gradi-
ent for all variables) were used. A locally reﬁned grid with 192 cells
per radius was used, able to resolve the boundary layers at the
interface region as explained in Strotos et al. [61]. It has to be noted
that the 2D simulations performed in this work are considered reli-
able up to the breakup instant, since after that, three-dimensional
phenomena appear.
In an effort to relate and also distinguish the simulations per-
formed in Strotos et al. [61] for the volatile n-heptane droplet, from
the present simulations referring to n-decane, the heat and mass
transfer Spalding numbers ( BT and BM respectively) are considered
(Eqs. (3) and (4) ). These are calculated by using the initial surface
temperature Ts,0 (Eq. (5)) which corresponds to the contact temper-
ature between semi-inﬁnite solids [71]; this concept was also used
in [72–74] for droplet impact on hot substrates and agrees well
with the CFD predictions at the ﬁrst time-step.
BT;1 ¼ cp;g;1ðT1 /C0 T0Þ
LðTs;0Þ ð3Þ
BM;0 ¼ YsðTs;0Þ/C0 Y1
1 /C0 YsðTs;0Þ ð4Þ
Ts;0 ¼ clT0 þ cg T1
cl þ cg
ð5Þ
Fheat ¼ 1 þ BT;1
1 þ BM;0
ð6Þ
Fig. 1. Cases examined on the We-Re plane.
372 G. Strotos et al. / Fuel 185 (2016) 370–380

<!-- PDF_PAGE: 4 -->

The droplet’s tendency to increase its temperature is propor-
tional to BT and inversely proportional to BM, since the evaporation
absorbs heat and tends to decrease the droplet temperature.
An indicator of the droplet heat-up is the heating factor Fheat
(Eq. (6)); large values imply a high tendency to increase the tem-
perature. A comparison of the heating factor for the n-heptane
(C07) and the n-decane (C10) is shown in Fig. 2 as a function of
the gas phase temperature for T0 = 300 K (note that this is indepen-
dent of the ﬂow conditions). It is evident that the n-decane has a
higher possibility to heat-up due to its lower vapor pressure; the
heating factor increases with the gas phase temperature and
decreases with increasing initial fuel temperature (not shown in
Fig. 2 ). It has to be noted that the heating factor has a qualitative
character and for the isothermal cases it was assumed that Fheat =1 ,
which corresponds to inﬁnite latent heat and zero vapor pressure.
Note that the deﬁnition of the heating factor adopted here is suit-
able for the present conditions, but might not be suitable for low
ambient temperatures close to the droplet temperature in which
Fheat <1 .
Finally, prior to the presentation of the results of the present
work, it has to be noted that the isothermal simulations conducted
in Strotos et al. [61] for an n-heptane and the present simulations
for an n-decane are in close agreement between them since they
both have low Oh numbers (0.01 and 0.02 respectively) and
similar Re number ranges (77–337 and 84–367 respectively for
T1 = 600–1000 K). On the other hand, the evaporating simulations
for these two fuels are exhibiting large variations due to the
species thermal properties.
3.2. Hydrodynamic effect of heating
The results obtained for the droplet shapes are shown in Figs. 3
and 4 for the cases with free stream temperature 800 and 1000 K
respectively. In these ﬁgures the left part corresponds to the
isothermal predictions and the right part to the evaporating simu-
lations; the cases with T1 = 600 K are not presented since the dif-
ferences between isothermal and evaporating simulations were
small. The droplet shapes drawn in black correspond to time inter-
vals of 0.5 tsh (i.e. 0.0, 0.5, 1.0, 1.5, 2.0 tsh) and the droplet shapes
drawn in red correspond to intermediate instances i.e. 0.75, 1.25,
1.75, 2.25tsh (the time instant of 0.25 tsh has been omitted); the last
droplet shape corresponds to the instant of breakup. From ﬁgures
Figs. 3 and 4 it is evident that the We number is the most inﬂuen-
tial parameter leading to different breakup regimes as the We
number increases, namely the bag breakup for low We numbers,
the transitional breakup for intermediate We numbers and the
sheet-thinning breakup for the highest We number examined. Nev-
ertheless, the sheet-thinning breakup is not clear due to the low Re
number and the continuous transition between the different
breakup regimes; the effect of Re number and the existence of a
critical Re number leading to bag breakup at We = 15 was in detail
discussed in Strotos et al. [61] and similar comments were also
made in Han and Tryggvason [23] and Guildenbecher et al. [1].
Apart from the dominant role of We number, the droplet heating
is playing an important role for the low We number cases. Under
isothermal conditions, droplets with We = 15 and T1 > 800 K are
not breaking up due to the low Re number. At the same We number
when heating is accounted for with T1 = 800 K ( Fig. 3), a clear bag
breakup is predicted; this is even more emphatic for the case of
T1 = 1000 K ( Fig. 4 ) in which the droplet not only breaks up, but
the breakup regime predicted is the transitional breakup. To the
authors best knowledge, no previous study has reported transi-
tional break-up at such a low We number; this is purely due to
the droplet heating which reduces the surface tension coefﬁcient
and subsequently the forces tending to resist the droplet deforma-
tion. Note that the effect of heating was not so profound in the high
volatility n-heptane examined in Strotos et al. [61].
The predicted onset of breakup tbr (termed also as ‘‘initiation
time”) for all cases examined is shown in Fig. 5 , along with the
corresponding experimental correlations given by Pilch and
Erdman [2] and Dai and Faeth [13], abbreviated as ‘‘P-E 1987”
and ‘‘D-F 2001” respectively; the present data for the breakup time
are subjected to error of the order of 0.05 tsh (2.5–5%) due to the
estimation of the breakup time by examining post-processed
images. The experimental correlations differ between them due
to several experimental uncertainties [25]. The trends are correctly
captured by predicting faster breakup with increasing We number.
The isothermal cases exhibit a weak dependency on Re number
when the We is kept constant, while in the evaporating cases the
reduction of the surface tension coefﬁcient acts as if the We num-
ber was higher; subsequently the droplet breaks up is faster. A best
ﬁt curve of the breakup time for both evaporating and isothermal
cases is given in Eq. (7) valid for the entire range of conditions
examined, i.e. n-decane fuel, Oh = 0.02, We = 15–90, Re = 84–367
and T1 = 600–1000 K.
tbr =tsh ¼ 8:628We/C0 0:352Re/C0 0:086F/C0 0:116
heat ð7Þ
One of the most important magnitudes determining the combustion
efﬁciency is the droplet surface area ( S) which deviates signiﬁcantly
from the corresponding of the initial spherical shape ( S0) during the
droplet deformation and breakup and it is difﬁcult to be measured
experimentally. The temporal evolution of this quantity is pre-
sented in Fig. 6 for selected cases ( T1 = 800 K and We = 15, 30,
90); note that for the isothermal case with We = 15, the droplet is
not breaking up. In all cases, after an initial non-deforming period
of /C24 0.3tsh, the droplet surface area starts to increase with a fast rate
(1.6–5.7 in terms of non-dimensional units) proportional to the We
number, which is in accordance with the ﬁndings of Han and Tryg-
gvason [23].U pt o t = tsh the variation of the surface area is smooth,
but at subsequent times the rate of deformation may change due to
surface instabilities appearing even in the isothermal cases. For that
reason, the maximum surface area at the instant of breakup is not
following a smooth variation as the We number is changing and a
local maximum is observed at We = 30 (as it was also shown in
[61]) reaching values of 12 S0. This point needs further investigation
by performing 3-D simulations since 3-D phenomena may appear
before the breakup instant and alter both the rate of deformation
Fig. 2. Heating factor as a function of the gas phase temperature for two different
fuels ( T0 = 300 K).
G. Strotos et al. / Fuel 185 (2016) 370–380 373

<!-- PDF_PAGE: 5 -->

as also the breakup instant. Regarding the effect of heating (see the
solid lines in Fig. 6), it is evident that it is important for low to med-
ium We numbers and t > tsh by further increasing the rate of
deformation.
As explained in Strotos et al. [61] it is difﬁcult to ﬁnd a mathe-
matical expression predicting the temporal evolution of the surface
area for the entire phenomenon up to the breakup instant and cov-
ering the entire range of We numbers leading to different breakup
regimes. This becomes even more complex when heating is
included since the surface area evolution is implicitly coupled with
the variation of the surface tension coefﬁcient due to heating. On
the other hand, the evolution of the surface area can be predicted
for t < tsh with Eq. (8a), which has been slightly modiﬁed relative to
the one used in [61] by using in the denominator on the right hand
side of Eq. (8a) the term sin h(c2). Now, the coefﬁcient c1 expresses
the surface area at t = tsh and c2 characterizes the form of the curve
connecting the initial and the ‘‘ﬁnal” state at t = 0 and t=t sh respec-
tively; a low c2 value implies a smoother (closer to the linear)
Fig. 4. Droplet shapes for the cases with T1 = 1000 K. The droplet shapes drawn black (see the online version) correspond to time intervals of 0.5 tsh and the drawn red
correspond to representative intermediate instances of 0.25 tsh. The last droplet shape corresponds to the instant of breakup. Differences are observed at the lower We number
case. (For interpretation of the references to colour in this ﬁgure legend, the reader is referred to the web version of this article.)
Fig. 3. Droplet shape evolution for the cases with T1 = 800 K. The droplet shapes drawn black (see the online version) correspond to time intervals of 0.5 tsh and the droplet
shapes drawn red correspond to representative intermediate instances of 0.25 tsh. The last droplet shape corresponds to the instant of breakup. Differences are observed at the
lower We number case. (For interpretation of the references to colour in this ﬁgure legend, the reader is referred to the web version of this article.)
374 G. Strotos et al. / Fuel 185 (2016) 370–380

<!-- PDF_PAGE: 6 -->

variation. An important improvement of the present ﬁtting curve
relative to the one in [61], is the inclusion of the effect of heating
by using the correction factor fcorr in the adjustable coefﬁcients c1
and c2 (see Eqs. (8b) and (8c) ). Eqs. (8a)–(8c) is valid for the entire
range of conditions examined in the present work, the correlation
coefﬁcient for the ﬁtting of the surface area evolution is above 0.98
and the prediction of the surface area at t = tsh is within the 15%
error for most of the cases examined; nevertheless this can reach
values of 30% for speciﬁc cases at the highest temperature of
1000 K.
S
S0
/C0 1 ¼ c1
sin hðc2 /C1t=tshÞ
sin hðc2 Þ ; t < tsh ð8aÞ
c1 ¼ 0:1484We1:092 Re/C0 0:284f corr ; f corr ¼ 1 þ 4:152We/C0 1:06ðFheat /C0 1Þ0:84 ð8bÞ
c2 ¼ 4:5234We0:294Re/C0 0:198 f corr ; f corr ¼ 1 /C0 0:013We/C0 0:50 ðFheat /C0 1Þ0:289 ð8cÞ
For the isothermal cases ( fcorr = 1) the surface area increases
with increasing We number and decreasing Re number; this is
clearly derived from the sign of the exponents of c1 (Eq. (8b)).
When heating is included, the phenomenon becomes more compli-
cated and the correction factor fcorr depends both on the We num-
ber and the heating factor Fheat. The correction factor for the
coefﬁcient c1 is always fcorr > 1 which means that heating tends
to increase the surface area at t = tsh. As stated in [61], the extrap-
olation of this curve up to tbr should be done with caution and limit
the maximum value not to exceed 10–12 S0, otherwise unphysical
values may be obtained.
The droplet breakup is governed by the relative strength of the
forces acting on the droplet, which vary dynamically as the droplet
shape, dimensions and velocity change during the whole process.
The instantaneous deforming forces scale with qg u2
rel;t D2
c;t where
urel;t is the instantaneous relative drop-gas velocity (obtained by
subtracting the average droplet velocity from the free-stream
velocity) and Dc,t is the instantaneous cross-stream diameter, while
the instantaneous restorative forces scale with rDc,t in which the
viscous forces have been ignored since Oh < 0.1. The ratio of these
forces represents an instantaneous We number (see Eq. (9)) which
changes during the breakup process and includes the effects of
heating, deformation and velocity change:
Wet ¼
qg u2
rel;t Dc;t
r ¼ We0
r0
r
/C16/C17 Dc;t
D0
/C18/C19 urel;t
U0
/C18/C19 2
ð9Þ
The predicted transient We number based on Eq. (9) is plotted
in Fig. 7 for selected isothermal and evaporating cases with
T1 = 800 K. The transient We number increases in time implying
that the deforming forces become progressively stronger, except
of the isothermal case with We = 15. In this case the droplet is
not breaking up and after reaching a maximum, the instantaneous
We number decreases, implying that the restorative forces become
stronger. Generally, the instantaneous We number (as deﬁned in
Eq. (9)) increases by a factor of 2–3 relative to the initial We num-
ber which is mainly ought to the increase of the cross sectional
diameter; the reduction of the relative drop-gas velocity (no more
than 10% for the cases examined) and the reduction of the surface
tension coefﬁcient play a secondary role. In Fig. 7 the curves
derived from Eq. (9) by using either the experimental breakup time
of Dai and Faeth [13] or that of Pilch and Erdman [2] for Oh = 0.02
Fig. 7. Predicted instant We number for selected isothermal (dashed lines) and
evaporating (solid lines) cases with T1 = 800 K.
Fig. 6. Temporal evolution of the dimensionless droplet surface area for selected
cases with T1 = 800 K. The dashed lines correspond to the isothermal cases and the
solid lines to the evaporating cases.
Fig. 5. Predicted dimensionless breakup time for the isothermal and the evaporat-
ing n-decane cases.
G. Strotos et al. / Fuel 185 (2016) 370–380 375

<!-- PDF_PAGE: 7 -->

are also shown; these were derived by processing the experimental
data of [13] and more details can be found in [61]. These curves
represent the critical instantaneous condition for breakup and
when crossed, breakup occurs. The present simulations qualita-
tively agree with these curves.
3.3. Thermal behavior of the droplet
The temporal evolution of the mean volume averaged droplet
temperature Tm and the spatially averaged surface temperature Ts
are shown in Fig. 8 a with the solid and dashed lines respectively,
for two cases combining different We numbers and gas phase tem-
peratures; these are indicated inside the parentheses as ( We, T1).
Both the mean droplet temperature and the surface temperature
increase with increasing ambient temperature, as expected. The
mean droplet temperature Tm increases continuously in time and
may reach a heat-up of 15 K by the onset of breakup, while the
average surface temperature Ts exhibits a quite transient behavior;
during the ﬂattening phase ( t < 0.6–0.8tsh) the surface temperature
increases until reaching a maximum, followed by a decrease until
coming closer to the volume averaged temperature. This behavior
is mainly attributed to the ﬂow patterns induced by the shape dis-
tortion which exchange hotter ﬂuid from the droplet surface with
the colder ﬂuid from the droplet interior (see also Schlottke et al.
[59]). Additional to that, the increased surface temperature results
in a high evaporation rate which tends to further suppress the sur-
face heating.
In Fig. 8 b the dimensionless droplet mass and droplet volume
(solid and dashed lines, respectively) are shown for the cases
(We, T1) = (15, 600) and (15, 1000). Up to the breakup instant,
the evaporated mass is less than 0.5%, while the droplet volume
increases up to 0.1% due to the thermal expansion effect. Note that
in the corresponding cases with n-heptane presented in [61], the
maximum heat-up was 7 K, the evaporated mass was reaching
2% and the thermal expansion effect was absent. The aforemen-
tioned differences are mainly affected by the different volatility
between the n-heptane and n-decane.
The heat and mass transfer processes are usually characterized
by the dimensionless Nusselt ( Nu) and Sherwood ( Sh) numbers
respectively, which express the heat/mass transfer enhancement
relative to a purely diffusive process. These are deﬁned as the
dimensionless temperature/concentration gradient at the droplet
interface, but their calculation is not applicable with the VOF
methodology due to the continuous variation of the ﬁeld magni-
tudes across the interface as explained in [60]. Inspired by Hase
and Weigand [58] an indirect method is used to estimate them,
through Eqs. (10)–(12):
qlV dðcp;lTmÞ
dt ¼ S Nu /C1kg;1
D0
ðT1 /C0 TsÞ/C0 _m00L
/C18/C19
ð10Þ
_m ¼ S Sh /C1qg;1DAB;1
D0
lnð1 þ BM Þð 11Þ
Nul /C1kl;0
Ts /C0 Tm
D0
¼ Nu /C1kg;1
T1 /C0 Ts
D0
/C0 _m00L ð12Þ
Eq. (10) is the droplet energy balance, Eq. (11) is a widely used rela-
tionship for the evaporation rate of spherical droplets and Eq. (12)
represents the heat ﬂux continuity at the droplet’s surface, in which
Nul is the dimensionless temperature gradient inside the liquid; this
equation connects the average droplet temperature Tm with the sur-
face temperature Ts. The set of Eqs. (10)–(12) also forms a variant of
the 0-D model for spherical droplet evaporation proposed by Renk-
sizbulut et al. [75]. Solving Eqs. (10)–(12) for Nu, Sh and Nuliq and
Fig. 8. (a) Temporal evolution of mean droplet temperature Tm (solid lines) and spatially averaged surface temperature Ts (dashed lines). In (b) temporal evolution of
dimensionless droplet mass (solid lines) and dimensionless droplet volume (dashed lines). The cases shown in parentheses correspond to ( We, T1).
Fig. 9. Temporal variation of Nu, Sh and Nul for the case of ( We, T1) = (15, 600).
376 G. Strotos et al. / Fuel 185 (2016) 370–380

<!-- PDF_PAGE: 8 -->

using the CFD data for the mean droplet temperature Tm, the space
averaged surface temperature Ts and the evaporation rate dm/dt, the
temporal variation of the dimensionless transfer numbers is
obtained; this is shown in Fig. 9 for the case ( We, T1) = (15, 600),
which can be regarded as representative, since the qualitative
behavior observed is similar in all cases examined. For the Nu and
Sh numbers, there is a short initial transitional period as the one
observed in [39,40,58]; after that, they exhibit small ﬂuctuations
in time. The Sh number seems to oscillate around a steady-state
Fig. 10. Predictions of the 0-D model for (a) the spatially averaged surface temperature and (b) the droplet mass for the case of We = 45. The solid lines are the CFD data and
the dashed lines are the 0-D model predictions.
Fig. 11. Spatial distribution of (a) surface temperature, (b) droplet temperature and (c) vapor concentration for the case ( We, T1) = (15, 800). The time instances presented are
0.5, 1.0, 1.5 and 2.0 tsh. In (a) characteristic streamlines are also shown. For color interpretation, see the online version.
Table 1
Transient Nu and Nuliq numbers. The time t corresponds to the dimensionless time
t/tsh.
Nu ¼ c0 /C0 c1 t þ c2 expð/C0 c3 tÞ Nul ¼ c0 þ c1 expð/C0 c2 tÞþ c3 cosð2pt=c4 Þ
c0 1:326Re0:3647
1 ð1 þ BT;1 Þ/C0 0:236 56:47 þ 7:65 /C110/C0 4 Re1:707
l ð1 þ BT;1 Þ/C0 0:432
c1 3 /C110/C0 6 Re2:212
1 ð1 þ BT;1 Þ2:226 201 þ 1:99 /C110/C0 4 Re2:25
l ð1 þ BT;1 Þ/C0 0:5285
c2 3 15:59 þ 1:65 /C110/C0 6 Re2:64
l ð1 þ BT;1 Þ/C0 0:623
c3 60 5:786 /C110/C0 5 Re2:226
l ð1 þ BT;1 Þ/C0 0:825
c4 – 1.2
G. Strotos et al. / Fuel 185 (2016) 370–380 377

<!-- PDF_PAGE: 9 -->

value, while the Nu number decreases continuously in time with a
slow rate. On the other hand, the Nuliq number exhibits a more
unsteady behavior. The initial transitional period is longer com-
pared to the other numbers and its magnitude exhibits almost
one order of magnitude larger variations with time.
It is of engineering interest to ﬁnd expressions for the Nu, Sh and
Nuliq numbers and use them in 0-D or 1-D models aiming to predict
the droplet temperature and the evaporation rate. Earlier CFD
works on spherical droplets (see [39,40] among many others) pro-
vided such expressions as a function of the instantaneous Re, BT and
BM numbers. Nevertheless, this is not applicable in the case of dro-
plet breakup due to the short duration of the phenomenon and
more importantly due to shape distortion from the spherical one.
In [61] time-averaged transfer numbers (being a function of the ini-
tial reference conditions) were used and they could adequately cap-
ture the thermal behavior of droplets undergoing breakup.
Following this approach, the time-averaged transfer numbers ﬁt-
ting the present data are given in Eqs. (13)–(15); the Rel appearing
in Eq. (15) (Rel ¼ Re1e2=3N/C0 4=3Þ was taken from [38] and it is derived
by equating the tangential shear stresses at the droplet surface:
Nu ¼
2 þ 6:83Re0:07
1 Pr1=3
g;1
ð1 þ BT;1Þ0:75 ð13Þ
Sh ¼ 2 þ 1:608We0:591
0 Sc1=3
g;1
/C16/C17
ð1 þ BT;1Þð 14Þ
Nul ¼ 55:95 þ RelPr1:6
l =1429 ð15Þ
The set of Eqs. (10)–(15) forms a 0-D model which can be used
to predict the average droplet heating and evaporation, but not the
transient variation of the surface temperature, which decreases
after reaching a maximum (see Fig. 8 a). The reason for that dis-
crepancy is that the time-averaged expressions ignore the tran-
sient behavior of the transfer numbers. In the present work, the
Nu and Nuliq numbers are expressed as a function of the non-
dimensional time and this is an improvement of the model used
in [61]; the correlations used are shown in Table 1 and they are
valid for the conditions examined in the present work.
The results of the 0-D model by using the transient correlations
for Nu and Nuliq are shown in Fig. 10 for the case of We = 45 and
three different gas phase temperatures; the solid and the dashed
lines correspond to the CFD and the 0-D model predictions, respec-
tively. As seen, the time dependent expressions for the transfer
number can adequately predict the transient behavior of the sur-
face temperature, with a less than 4 K error. The model predictions
presented in Fig. 10 have assumed that the temporal evolution of
the surface area is known and this is a limitation of the proposed
model. On the other hand, Eqs. (8a)–(8c) for the surface area evo-
lution can be used to predict the thermal behavior for t<t sh; in this
case, the errors are mainly determined by the effectiveness of the
curve reproducing the surface area evolution.
In Strotos et al. [61] it was shown that droplet breakup is
affected by heating when the We number is low and the ambient
temperature is high. This conclusion was drawn both by consider-
ing the associated timescales (either in a macroscopic or a micro-
scopic level) and by implementing the aforementioned 0-D
model with the time-averaged expressions for the transfer num-
bers. These comments are also veriﬁed by the present simulations
for an n-decane droplet. Relating the n-heptane CFD simulations
performed in [61] and the present ones for the n-decane, the sur-
face temperature at t = tsh is well represented by Eq. (16). This
Fig. 12. Spatial distribution of (a) surface temperature, (b) droplet temperature and (c) vapor concentration for the case ( We, T1) = (30, 800). The time instances presented are
0.5, 1.0, 1.25 and 1.5 tsh. In (a) characteristic streamlines are also shown. For color interpretation, see the online version.
378 G. Strotos et al. / Fuel 185 (2016) 370–380

<!-- PDF_PAGE: 10 -->

equation clearly demonstrates the effect of We number, gas phase
temperature and species volatility through the heating factor Fheat:
TsðtshÞ¼ T0 1 þ 0:0195We/C0 0:2532F2:053
heat
/C16/C17
ð16Þ
3.4. Spatial distribution of the ﬂow variables
The spatial distribution of surface temperature, inner droplet
temperature and vapor concentration ﬁeld are shown in Figs. 11
and 12 for the cases with T1 = 800 K and We number 15 and 30,
respectively. The surface temperature (denoted with a thick line
colored with the corresponding temperature values) is not spa-
tially uniform; along the droplet surface differences of 15 K can
be observed. In the initial ﬂattening phase, hot spots are observed
on the front side of the droplet in an off-axis location; at subse-
quent instances hot spots are observed at the rear of the droplet.
In a spherical droplet case these temperature differences along
the surface could induce secondary ﬂow (due to surface tension
gradients) and form cellular vortices. The present work has
included the effect of surface tension variation along the interface
through the CSS surface tension model [76]. Nevertheless, no sec-
ondary ﬂow was observed in the present cases (see characteristic
streamlines in the left column), since the ﬂow patterns are deter-
mined by the droplet shape. Regarding the inner temperature ﬁeld
and the vapor concentration ﬁeld in the gas phase, these follow
similar patterns to the ones observed in [61], as affected by the
local velocity ﬁeld and the droplet deformation.
4. Conclusions
The Navier-Stokes, energy and transport of species conservation
equations together with the VOF methodology have been utilized
to study the coupled problem of aerodynamic droplet breakup
under the inﬂuence of heating and evaporation for We numbers
in the range 15–90 and gas phase temperatures 600–1000 K. To
quantify the effect of heating, the same cases were also studied
under isothermal conditions assuming constant species properties.
Combining the results obtained from the present work for an
n-decane fuel droplet with those for a more volatile n-heptane
droplet presented in Strotos et al. [61], it seems that droplet heat-
ing affects the overall breakup performance for low We numbers,
high gas phase temperatures and low volatility fuels. For a non-
breaking-up case with constant properties, heating may decrease
the surface tension coefﬁcient in such a way, that droplet not only
breaks up in the bag breakup regime, but also in the transitional
breakup regime. Nevertheless, at high We numbers the surface ten-
sion still decreases but without altering the breakup performance.
During droplet breakup, despite the fact that the liquid evaporated
mass is very low (especially for low volatility fuels), one has to con-
sider the evaporation source terms since they play an important
role by suppressing the droplet heat-up; this is evident for high
volatility fuels which seem to be less affected by heating.
The concept of ‘‘heating factor” was introduced which provides
an indication of the droplet tendency to heat-up by combining the
terms tending to increase and decrease the droplet temperature.
Useful correlations were provided for an a priori estimation of
the breakup instant, surface area evolution and droplet heat-up.
Additional to them, an enhanced 0-D model able to predict the
thermal behavior of the droplet is proposed. In relevance to our
previous work [61], it uses time-dependent transfer numbers
instead of time-averaged and it is able to capture the transient
behavior of the spatially average surface temperature. The latter
is not spatially uniform and peak values are observed in the front
of the droplet in the initial ﬂattening phase and at the rear of the
droplet in the subsequent stages.
Acknowledgements
The research leading to these results has received funding from
the People Programme (Marie Curie Actions) of the European
Union’s Seventh Framework Programme FP7-PEOPLE-2012-IEF
under REA grant Agreement No. 329116.
References
[1] Guildenbecher DR, López-Rivera C, Sojka PE. Secondary atomization. Exp Fluids
2009;46:371–402.
[2] Pilch M, Erdman C. Use of breakup time data and velocity history data to
predict the maximum size of stable fragments for acceleration-induced
breakup of a liquid drop. Int J Multiph Flow 1987;13:741–57 .
[3] Faeth GM, Hsiang LP, Wu PK. Structure and breakup properties of sprays. Int J
Multiph Flow 1995;21(Supplement):99–127 .
[4] Gelfand BE. Droplet breakup phenomena in ﬂows with velocity lag. Prog
Energy Combust Sci 1996;22:201–65 .
[5] Theofanous TG. Aerobreakup of newtonian and viscoelastic liquids. Annu Rev
Fluid Mech 2011;43:661–90 .
[6] Nicholls JA, Ranger AA. Aerodynamic shattering of liquid drops. AIAA J
1969;7:285–90
.
[7] Krzeczkowski SA. Measurement of liquid droplet disintegration mechanisms.
Int J Multiph Flow 1980;6:227–39 .
[8] Hsiang LP, Faeth GM. Near-limit drop deformation and secondary breakup. Int J
Multiph Flow 1992;18:635–52 .
[9] Hsiang LP, Faeth GM. Drop properties after secondary breakup. Int J Multiph
Flow 1993;19:721–35 .
[10] Hsiang LP, Faeth GM. Drop deformation and breakup due to shock wave and
steady disturbances. Int J Multiph Flow 1995;21:545–60 .
[11] Chou WH, Hsiang LP, Faeth GM. Temporal properties of drop breakup in the
shear breakup regime. Int J Multiph Flow 1997;23:651–69 .
[12] Chou WH, Faeth GM. Temporal properties of secondary drop breakup in the
bag breakup regime. Int J Multiph Flow 1998;24:889–912
.
[13] Dai Z, Faeth GM. Temporal properties of secondary drop breakup in the
multimode breakup regime. Int J Multiph Flow 2001;27:217–36 .
[14] Liu Z, Reitz RD. An analysis of the distortion and breakup mechanisms of high
speed liquid drops. Int J Multiph Flow 1997;23:631–50 .
[15] Lee CH, Reitz RD. An experimental study of the effect of gas density on the
distortion and breakup mechanism of drops in high speed gas stream. Int J
Multiph Flow 2000;26:229–44 .
[16] Cao X-K, Sun Z-G, Li W-F, Liu H-F, Yu Z-H. A new breakup regime of liquid
drops identiﬁed in a continuous and uniform air jet ﬂow. Phys Fluids
2007;19:057103.
[17] Zhao H, Liu H-F, Li W-F, Xu J-L. Morphological classiﬁcation of low viscosity
drop bag breakup in a continuous air jet stream. Phys Fluids 2010;22:114103
.
[18] Zhao H, Liu H-F, Xu J-L, Li W-F, Lin K-F. Temporal properties of secondary drop
breakup in the bag-stamen breakup regime. Phys Fluids 2013;25:054102 .
[19] Opfer L, Roisman IV, Tropea C. Aerodynamic fragmentation of drops: dynamics
of the liquid bag. In: ICLASS 2012, Heidelberg, Germany; 2012.
[20] Opfer L, Roisman IV, Venzmer J, Klostermann M, Tropea C. Droplet-air collision
dynamics: evolution of the ﬁlm thickness. Phys Rev E 2014;89:013023 .
[21] Guildenbecher DR, Sojka PE. Experimental investigation of aerodynamic
fragmentation of liquid drops modiﬁed by electrostatic surface charge. Atom
Sprays 2011;21:139–47 .
[22] Flock AK, Guildenbecher DR, Chen J, Sojka PE, Bauer HJ. Experimental statistics
of droplet trajectory and air ﬂow during aerodynamic fragmentation of liquid
drops. Int J Multiph Flow 2012;47:37–49
.
[23] Han J, Tryggvason G. Secondary breakup of axisymmetric liquid drops. II.
Impulsive acceleration. Phys Fluids 2001;13:1554–65 .
[24] Aalburg C. Deformation and breakup of round drop and nonturbulent liquid
jets in uniform crossﬂows. In: Aerospace Engineering and Scientiﬁc
Computing. University of Michigan; 2002
.
[25] Khosla S, Smith CE. Detailed understanding of drop atomization by gas
crossﬂow using the volume of ﬂuid method. In: ILASS Americas, Toronto,
Canada, 2006 .
[26] Quan S, Schmidt DP. Direct numerical study of a liquid droplet impulsively
accelerated by gaseous ﬂow. Phys Fluids 2006;18:103103 .
[27] Wadhwa AR, Magi V, Abraham J. Transient deformation and drag of
decelerating drops in axisymmetric ﬂows. Phys Fluids 2007;19:113301
.
[28] Xiao F, Dianat M, McGuirk JJ. LES of single droplet and liquid jet primary break-
up using a coupled level set/volume of ﬂuid method. In: 12th ICLASS,
Heidelberg, Germany, 2012 .
[29] Khare P, Yang V. Drag coefﬁcients of deforming and fragmenting liquid
droplets. In: ILASS Americas, 2013
.
[30] Jalaal M, Mehravaran K. Transient growth of droplet instabilities in a stream.
Phys Fluids 2014;26:012101 .
[31] Jain M, Prakash RS, Tomar G, Ravikrishna RV. Secondary breakup of a drop at
moderate Weber numbers. Proceed Roy Soc Lond A: Math, Phys Eng Sci
2015;471
.
[32] Yang W, Jia M, Sun K, Wang T. Inﬂuence of density ratio on the secondary
atomization of liquid droplets under highly unstable conditions. Fuel
2016;174:25–35.
G. Strotos et al. / Fuel 185 (2016) 370–380 379

<!-- PDF_PAGE: 11 -->

[33] Strotos G, Malgarinos I, Nikolopoulos N, Gavaises M. Predicting droplet
deformation and breakup for moderate Weber numbers. Int J Multiph Flow
2016;85:96–109.
[34] Givler SD, Abraham J. Supercritical droplet vaporization and combustion
studies. Prog Energy Combust Sci 1996;22:1–28 .
[35] Bellan J. Supercritical (and subcritical) ﬂuid behavior and modeling: drops,
streams, shear and mixing layers, jets and sprays. Prog Energy Combust Sci
2000;26:329–66
.
[36] Sazhin SS. Advanced models of fuel droplet heating and evaporation. Prog
Energy Combust Sci 2006;32:162–214 .
[37] Erbil HY. Evaporation of pure liquid sessile and spherical suspended drops: a
review. Adv Colloid Interface Sci 2012;170:67–86
.
[38] Renksizbulut M, Haywood RJ. Transient droplet evaporation with variable
properties and internal circulation at intermediate Reynolds numbers. Int J
Multiph Flow 1988;14:189–202 .
[39] Haywood RJ, Nafziger R, Renksizbulut M. Detailed examination of gas and
liquid phase transient processes in convective droplet evaporation. J Heat
Transfer 1989;111:495–502 .
[40] Chiang CH, Raju MS, Sirignano WA. Numerical analysis of convecting,
vaporizing fuel droplet with variable properties. Int J Heat Mass Transf
1992;35:1307–24.
[41] Megaridis CM. Comparison between experimental measurements and
numerical predictions of internal temperature distributions of a droplet
vaporizing under high-temperature convective conditions. Combust Flame
1993;93:287–302
.
[42] Shih AT, Megaridis CM. Suspended droplet evaporation modeling in a laminar
convective environment. Combust Flame 1995;102:256–70 .
[43] Shih AT, Megaridis CM. Thermocapillary ﬂow effects on convective droplet
evaporation. Int J Heat Mass Transf 1996;39:247–57
.
[44] Abou Al-Sood MM, Birouk M. A numerical study of the effect of turbulence on
mass transfer from a single fuel droplet evaporating in a hot convective ﬂow.
Int J Therm Sci 2007;46:779–89 .
[45] Raghuram S, Raghavan V, Pope DN, Gogos G. Two-phase modeling of
evaporation characteristics of blended methanol–ethanol droplets. Int J
Multiph Flow 2013;52:46–59 .
[46] Schlottke J, Weigand B. Direct numerical simulation of evaporating droplets. J
Comput Phys 2008;227:5215–37 .
[47] Ghata N, Shaw BD. Computational modeling of the effects of support ﬁbers on
evaporation of ﬁber-supported droplets in reduced gravity. Int J Heat Mass
Transf 2014;77:22–36 .
[48] Megaridis CM, Sirignano WA. Numerical modeling of a vaporizing
multicomponent droplet. Symp (Int) Combust 1990;23:1413–21 .
[49] Megaridis CM, Sirignano WA. Multicomponent droplet vaporization in a
laminar convective environment. Combust Sci Technol 1992;87:27–44 .
[50] Megaridis CM. Liquid-phase variable property effects in multicomponent
droplet convective evaporation. Combust Sci Technol 1993;92:291–311 .
[51] Renksizbulut M, Bussmann M. Multicomponent droplet evaporation at
intermediate Reynolds numbers. Int J Heat Mass Transf 1993;36:2827–35
.
[52] Strotos G, Gavaises M, Theodorakakos A, Bergeles G. Numerical investigation
of the evaporation of two-component droplets. Fuel 2011;90:1492–507 .
[53] Banerjee R. Numerical investigation of evaporation of a single ethanol/iso-
octane droplet. Fuel 2013;107:724–39 .
[54] Strotos G, Malgarinos I, Nikolopoulos N, Gavaises M. Predicting the
evaporation rate of stationary droplets with the VOF methodology for a
wide range of ambient temperature conditions. Int J Therm Sci
2016;109:253–62.
[55] Haywood RJ, Renksizbulut M, Raithby GD. Numerical solution of deforming
evaporating droplets at intermediate Reynolds numbers. Numer Heat Transf;
A: Appl 1994;26:253–72 .
[56] Haywood RJ, Renksizbulut M, Raithby GD. Transient deformation and
evaporation of droplets at intermediate Reynolds numbers. Int J Heat Mass
Transf 1994;37:1401–9 .
[57] Mao ZS, Li T, Chen J. Numerical simulation of steady and transient mass
transfer to a single drop dominated by external resistance. Int J Heat Mass
Transf 2001;44:1235–47 .
[58] Hase M, Weigand B. Transient heat transfer of deforming droplets at high
Reynolds numbers. Int J Numer Meth Heat Fluid Flow 2003;14:85–97 .
[59] Schlottke J, Dulger E, Weigand B. A VOF-based 3D numerical investigation of
evaporating, deformed droplets. Progr Comput Fluid Dyn, Int J 2009;9:426–35 .
[60] Cerqueira RFL, Paladino EE, Maliska CR. A computational study of the
interfacial heat or mass transfer in spherical and deformed ﬂuid particles
ﬂowing at moderate Re numbers. Chem Eng Sci 2015;138:741–59
.
[61] Strotos G, Malgarinos I, Nikolopoulos N, Gavaises M. Numerical investigation
of aerodynamic droplet breakup in a high temperature gas environment. Fuel
2016;181:450–62.
[62] Theodorakakos A, Bergeles G. Simulation of sharp gas–liquid interface using
VOF method and adaptive grid local reﬁnement around the interface. Int J
Numer Meth Fluids 2004;45:421–39
.
[63] Malgarinos I, Nikolopoulos N, Marengo M, Antonini C, Gavaises M. VOF
simulations of the contact angle dynamics during the drop spreading:
standard models and a new wetting force model. Adv Colloid Interface Sci
2014;212:1–20.
[64] Perry RH, Green DW. Perry’s chemical engineers’ handbook. 7th ed. McGraw-
Hill; 1997 .
[65] Poling BE, Prausnitz JM, O’Connell JP. Properties of Gases and Liquids. 5th
ed. McGraw-Hill; 2001 .
[66] ANSYS /C210FLUENT, Release 14.5, Theory Guide; 2012.
[67] Malgarinos I, Nikolopoulos N, Gavaises M. Coupling a local adaptive grid
reﬁnement technique with an interface sharpening scheme for the simulation
of two-phase ﬂow and free-surface ﬂows using VOF methodology. J Comput
Phys 2015;300:732–53 .
[68] Strotos G, Malgarinos I, Nikolopoulos N, Papadopoulos K, Theodorakakos A,
Gavaises M. Performance of VOF methodology in predicting the deformation
and breakup of impulsively accelerated droplets. In: 13th ICLASS, Tainan,
Taiwan, 2015
.
[69] Clift R, Grace JR, Weber ME. Bubbles, drops and particles. New York: Academic
Press; 1978 .
[70] Michaelides EE. Particles, bubbles & drops: their motion, heat and mass
transfer. World Scientiﬁc; 2006 .
[71] Incropera FP, de Witt DP. Fundamentals of heat and mass transfer. 3rd ed. New
York: Wiley; 1990 .
[72] Seki M, Kawamura H, Sanokawa K. Transient temperature proﬁle of a hot wall
due to an impinging liquid droplet. J Heat Transfer 1978;100:167–9 .
[73] Strotos G, Aleksis G, Gavaises M, Nikas K-S, Nikolopoulos N, Theodorakakos A.
Non-dimensionalisation parameters for predicting the cooling effectiveness of
droplets impinging on moderate temperature solid surfaces. Int J Therm Sci
2011;50:698–711
.
[74] Strotos G, Nikolopoulos N, Nikas K-S, Moustris K. Cooling effectiveness of
droplets at low Weber numbers: effect of temperature. Int J Therm Sci
2013;72:60–72.
[75] Renksizbulut M, Bussmann M, Li X. Droplet vaporization model for spray
calculations. Part Part Syst Charact 1992;9:59–65
.
[76] Lafaurie B, Nardone C, Scardovelli R, Zaleski S, Zanetti G. Modelling merging
and fragmentation in multiphase ﬂows with SURFER. J Comput Phys
1994;113:134–47.
380 G. Strotos et al. / Fuel 185 (2016) 370–380
