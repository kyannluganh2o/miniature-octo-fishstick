<!-- PDF_PAGE: 1 -->

Francesco Bonelli1
e-mail: francesco.bonelli@unibas.it
Annarita Viggiano
e-mail: annarita.viggiano@unibas.it
Vinicio Magi
e-mail: vinicio.magi@unibas.it
School of Engineering,
University of Basilicata,
Potenza 85100, Italy
A Numerical Analysis of
Hydrogen Underexpanded Jets
Under Real Gas Assumption
This work examines the ﬂuid dynamic structure of underexpanded gas jets by using a
high-performance computing (HPC) methodology in order to untangle the question of
whether it is necessary to include the real gas assumption dealing with hydrogen jets.
The answer to this question is needed in order to guarantee accurate numerical simula-
tions of such jets in practical engineering applications, such as direct-injection hydrogen
engines. An axial symmetric turbulent ﬂow model, which solves the Favre-averaged
Navier–Stokes equations for a multicomponent gas mixture, has been implemented and
validated. The ﬂow model has been assessed by comparing spreading and centerline
property decay rates of subsonic jets at different Mach numbers with those obtained by
both theoretical considerations and experimental measurements. Besides, the Mach disk
structure of underexpanded jets has been recovered, thus conﬁrming the suitability and
reliability of the computational model. To take into account the effects of real gases, both
van der Waals and Redlich–Kwong equations of state have been implemented. The analy-
sis of a highly underexpanded hydrogen jet with total pressure equal to 75 MPa, issuing
into nitrogen at 5 MPa, shows that the use of real gas equations of state affects signiﬁ-
cantly the jet structure in terms of temperature, pressure, and Mach number proﬁles
along the jet centerline and also in terms of jet exit conditions, with differences up to
38%. [DOI: 10.1115/1.4025253]
1 Introduction
The investigation of sonic and supersonic gas jets is a relevant
subject for both gas dynamics and engineering applications, such
as engines, combustors, etc. Speciﬁcally, a comprehensive analy-
sis of such jets can provide guidance for the development of new
strategies both to improve the performance and efﬁciency of
direct-injection engines and to verify the feasibility of new
propulsion systems. In addition, this subject is important also for
safety issues, such as the sudden release of gas from a high-
pressure tube or pipe in the case of failure.
In this scenario, this work is aimed to study the ﬂuid dynamic
behavior of underexpanded hydrogen jets, using pressure condi-
tions similar to those encountered in direct-injection hydrogen
engines.
Hydrogen is a very attractive fuel for internal combustion
engines (ICEs), since hydrogen-fueled ICEs can work with near-
zero emissions and higher efﬁciencies than conventional
hydrocarbon-fueled ICEs [ 1]. These capabilities are due to the
unique features of hydrogen compared to conventional fossil
fuels. The wide ﬂammability limits allow stable combustion with
very lean mixtures, thus resulting in lower maximum gas tempera-
tures and, consequently, in lower nitrogen oxides (NOx) produc-
tion. Moreover, the engine can operate unthrottled at low loads
with an improvement of engine efﬁciency. However, hydrogen is
responsible for some inconvenience at high engine loads. Speciﬁ-
cally, the low ignition energy can cause undesirable combustion
events, such as preignition, knock, and backﬁre, whereas the small
quenching distance leads to narrow thermal boundary layer with
higher thermal losses. Moreover, the low density causes a reduc-
tion of volumetric efﬁciencies.
One of the most promising strategies in order to overcome these
problems is the direct injection strategy. This approach requires
high pressure and high ﬂow rate injections to ensure a good mix-
ing in the available short time, which goes from 20 ms down to
4 ms when rpm increases from 1000 to 5000 [ 1]. Thus, hydrogen
injection is designed to be sonic with injection pressure higher
than 8 MPa and mass ﬂow rate between 1 and 10 g/s [ 1]. This
results in an underexpanded jet issuing into the cylinder.
The structure of underexpanded jets, as depicted in Fig. 1,i s
well documented [ 2,3]. In such a jet, wedge-shaped waves of
expansion occur at the edge of the injector. The expansion waves
cross one another and are reﬂected from the opposite boundaries
of the jet as waves of compression. These waves again cross
one another and are reﬂected as expansion waves from the jet
boundaries [ 2]. When the pressure difference between the jet and
the surroundings is relatively large, the compression waves
coalesce in an oblique shock, named barrel shock. If the jet-to-
ambient pressure ratio is greater than two [ 4], the reﬂection of the
barrel shock cannot be regular anymore, so that a disk-shaped
Fig. 1 Schematic of underexpanded sonic jet
1Corresponding author.
Contributed by the Fluids Engineering Division of ASME for publication in the
JOURNAL OF FLUIDS ENGINEERING. Manuscript received October 12, 2012; ﬁnal
manuscript received August 6, 2013; published online September 12, 2013. Assoc.
Editor: John Abraham.
Journal of Fluids Engineering DECEMBER 2013, Vol. 135 / 121101-1Copyright VC 2013 by ASME
Downloaded from asmedigitalcollection.​asme.​org/​fluidsengineering/​article-pdf/​135/​12/​121101/​6189348/​fe_135_12_121101.​pdf by Dalian University Of Technology user on 31 August 2026

<!-- PDF_PAGE: 2 -->

normal shock, called “Mach disk,” together with a reﬂected shock
take place. Downstream of the reﬂected shock, the ﬂow remains
supersonic, whereas downstream of the Mach disk, it becomes
subsonic.
The study of this ﬂuid structure has been addressed by several
authors [ 5–8] by using both experimental measurements and nu-
merical simulations. Panda and Seasholtz [ 5] have measured the
density ﬁeld of underexpanded supersonic free jets issuing from a
choked circular nozzle using a Rayleigh scattering–based tech-
nique. They have shown that the shear layer grows faster than an
equivalent fully expanded jet. Moreover, they have found some
relations between the pressure ﬂuctuation occurring outside the jet
and the density ﬂuctuation occurring inside. Woodmansee et al.
[6] have performed nonintrusive pressure and temperature meas-
urements using coherent anti-Stokes Raman scattering (CARS)
and have compared their experimental results with those obtained
from a Reynolds-averaged Navier–Stokes simulation. They have
found a good agreement between the two data sets. Large eddy
simulation (LES) and Schlieren imaging experiments of an under-
expanded hydrogen jet have been carried out by Gorl /C19e et al. [ 7].
They were able to get good agreement in terms of both the evolu-
tion of the Mach disk height over time and the prediction of the
mixing region. The solution of the Favre-averaged Navier–Stokes
equations along with the standard k/C0 e turbulence model carried
out by Birkby and Page [ 8] has shown good capability in predict-
ing Mach disk location and its distinctive features, such as the
triple point, the slip line, and the curved jet boundary, although
they found a decay rate of the cell wavelength greater than the
real one.
A signiﬁcant issue in modeling turbulent free jets at high Mach
number is the inﬂuence of gas compressibility. It is recognized
that compressibility has a relatively small inﬂuence on turbulent
eddies in wall-bounded ﬂows for Mach number up to about 5.
This appears not to be true for free shear layers, where signiﬁcant
density variations occur, even with small pressure changes and
sonic Mach number. It has been veriﬁed that both the k/C0 e and
k/C0 x models, developed for incompressible ﬂows, are not able to
predict the observed decrease in spreading rate with increasing
Mach number for free shear layers [ 9].
The Favre-averaged turbulent kinetic energy equation for com-
pressible ﬂows includes three additional terms (i.e., pressure
work, pressure dilatation, and dilatation-dissipation). Over the last
two decades, several researchers have proposed models for each
of these additional terms. Sarkar et al. [ 10], Zeman [ 11], and
Wilcox [ 12] have developed models for the dilatation-dissipation
term, as a function of turbulent Mach number, in order to predict
the correct spreading rate for the compressible mixing layer.
Blaisdell et al. [ 13] have carried out direct numerical simulations
(DNSs) in order to improve a fundamental understanding of
compressible turbulence and to contribute to the development of
turbulence models for compressible ﬂows.
The present work has been carried out by means of an in-house
axial symmetric ﬂow model [ 14], which solves the Favre-
averaged Navier–Stokes equations for a multicomponent mixture
of gases and is able to take into account real gas effects by
employing either van der Waals or Redlich–Kwong equations of
state (EoS). The solver is written in
FORTRAN 90 and is fully paral-
lelized by using the message-passing interface (MPI) libraries.
The validation of the mathematical and numerical models has
been assessed by comparing spreading and centerline property
decay rates with those obtained by both theoretical considerations
and experimental measurements [ 9,15–17]. The effect of gas com-
pressibility and density ratio on the dynamic of the jet has been
analyzed, and the Mach disk structure of an underexpanded air jet
has been compared with results available in the literature [ 6].
Finally, the code has been used to investigate the inﬂuence of real
gas effects on the structure of underexpanded hydrogen jets.
The analysis of real gas effects is a relevant concern addressed
by several researchers in the case of high-pressure injection proc-
esses, at ﬁrst in the context of liquid rockets [ 18–21] and then
extended to the ﬁeld of ICEs [ 22–24]. Cheng et al. [ 18] and Cheng
and Farmer [ 19] have developed a spray combustion model in
order to understand the effects on wall erosion. They have used a
ﬁnite difference Navier–Stokes solver with a k/C0 e model and real-
ﬂuid models for the multiphase ﬂow. The model predicts the
shear layer growth and gives a good agreement with experimental
measurements in terms of velocity and species proﬁles. Disagree-
ment in the H
2O species proﬁle was attributed to experimental
measurement error. Zong et al. [ 20] have performed an LES anal-
ysis of cryogenic ﬂuid injection and mixing under supercritical
conditions. They have devised a uniﬁed theoretical framework
capable of treating ﬂuid ﬂows, transcritical property variations,
and real-ﬂuid thermodynamics. The results from an investigation
of unsteady combustion inside small-scale, multi-injectors liquid
rocket engine carried out by Masquelet [ 21] by using LES have
shown the strong inﬂuence of real gas EoS on the overall chamber
behavior. Lim et al. [ 22] have performed 3D simulations of the
combustion process for a dimethyl ether-fueled (DME) diesel
engine. They have incorporated a spray impingement and nonpre-
mixed combustion models with a Peng–Robinson EoS, used to
calculate the evaporation rate of DME droplets, into the
STAR-CD
commercial computational ﬂuid dynamics code, and they have
found good agreement with experimental data. An interesting
analysis, which deals with the numerical simulation of fuel sprays
and a model that properly take into account the effects of high
pressure and temperature, has been carried out by Hohmann and
Renz [23], who have shown that the use of real models is manda-
tory for single droplets, whereas for droplet sprays, the difference
with respect to the ideal model becomes not appreciable. Lapuerta
et al. [ 24] have performed a study in order to select the most suita-
ble EoS for the estimation of instantaneous temperature and heat
release rate along the compression and expansion stroke of ICEs.
They have proven that the Soave equation provides the best pre-
dictions. The results show small differences with those obtained
under the ideal assumptions; however, the authors claim that such
differences may become important dealing with the estimation of
highly temperature-dependent phenomena.
The contribution of this work is to extend the use of real gas
equations for the simulation of hydrogen underexpanded jets. To
the authors’ knowledge, this work can be considered as a ﬁrst
attempt to systematically include the inﬂuence of real gas effects
on underexpanded jets of hydrogen. In Ref. [ 25], a preliminary
study of real gas effects on underexpanded hydrogen jets has been
carried out by the authors, thus showing that the use of real gas
models can be relevant under high pressure and temperature.
These ﬁndings can be explained by considering the low inversion
temperature of hydrogen, which is a speciﬁc property of such a
gas. Since, with the increase of pressure, the inversion tempera-
ture decreases, the gas operating conditions may fall outside of
the Joule–Thomson inversion curve.
In a recent work [ 26], the release of hydrogen from a high-
pressure tank into ambient air has been numerically studied by
solving the Euler equations with the Abel–Noble EoS, thus show-
ing differences up to 20% in terms of release velocity with respect
to the ideal gas assumption.
In this work, two-parameters real gas equations of state (i.e.,
the van der Waals and the Redlich–Kwong EoS) have been used,
together with the ideal gas assumption. The main objective of this
study is to assess how the real gas conditions inﬂuence the direct
injection of hydrogen in ICEs. Computations of a highly underex-
panded hydrogen jet, issued from a tank with total pressure equal
to 75 MPa into high-pressure (i.e., 5 MPa) environment has been
performed, thus showing that the use of real gas equations of
state substantially affects the results. The results, in terms of bar-
rel shock length under the ideal and the real gas assumptions,
have been compared with the empirical correlation proposed by
Ashkenas and Sherman [ 27].
This work is organized as follows: in Sec. 2, the governing
equations and the mathematical model are given. Then, the accu-
racy and reliability of the computational model are assessed by
121101-2 / Vol. 135, DECEMBER 2013 Transactions of the ASME
Downloaded from asmedigitalcollection.​asme.​org/​fluidsengineering/​article-pdf/​135/​12/​121101/​6189348/​fe_135_12_121101.​pdf by Dalian University Of Technology user on 31 August 2026

<!-- PDF_PAGE: 3 -->

comparing the results with those obtained experimentally by
Wang and Andreopoulos [ 16] and Narayanan et al. [ 17] (Sec. 3.1)
and by Woodmansee et al. [ 6] (Sec. 3.2). In Sec. 3.3, simulations
of an underexpanded hydrogen jet are performed by employing
the van der Waals and the Redlich–Kwong EoS, in addition to the
ideal gas assumption. Finally, conclusions are summarized.
2 The Governing Equations and the Numerical
Method
The ﬂow ﬁeld has been simulated by solving the Favre-
averaged Navier–Stokes equations for a multicomponent mixture
of nonreacting gases, which can be treated either as thermally per-
fect or as real gases, in an axial symmetric conﬁguration. The set
of governing equations, fully coupled with the standard k/C0 e turbu-
lence model, are
@
@t
ð
S
WdS þ
þ
@S
F /C1nds ¼
ð
S
HdS (1)
The vector of unknowns and the sum of the inviscid and viscous
ﬂuxes are deﬁned as follows:
W ¼½ /C22qq; /C22q~u; /C22q~v; /C22qE; /C22qk; /C22qes/C138T (2)
F ¼ð FE /C0 FV ; GE /C0 GV Þ (3)
FE ¼½ /C22qq ~u; /C22q~u2 þ /C22p; /C22q~u~v; /C22q~uH; /C22q~uk; /C22q~ues/C138T (4)
GE ¼½ /C22qq ~v; /C22q~u~v; /C22q~v2 þ /C22p; /C22q~vH; /C22q~vk; /C22q~ves/C138T (5)
H ¼½ 0; 0; 0; 0; Hk ; He/C138T (6)
ðFV ; GV Þ¼ /C0 /C22qq ~uq; r; ~u /C1r /C0 q; ll þ lt
rk
/C18/C19
rk; ll þ lt
re
/C18/C19
res
/C20/C21 T
(7)
Hk ¼ ltP /C0 2
3 /C22qk ~S /C0 /C22qesð1 þ PÞ (8)
He ¼ ce1 ltP /C0 2
3 /C22qk ~S
/C18/C19 es
k /C0 ce2f2 /C22q e2
s
k (9)
/C22q ¼
XN
q¼1
/C22qq (10)
E ¼
XN
q¼1
~Yq ~eq þð ~u2 þ ~v2Þ=2 þ k (11)
H ¼ E þ /C22p=/C22q (12)
where q is the density; u and v are velocity components; E is the
speciﬁc total energy; k the turbulent kinetic energy; e the dissipa-
tion of turbulent kinetic energy; H the speciﬁc total enthalpy; H
the source term vector; ce1, ce2, rk, and re the turbulence model
constants; P the turbulence production based on velocity gradient;
S the velocity divergence; e the speciﬁc internal energy; and P
the compressibility correction. Under the thermally perfect
assumption, the pressure is evaluated from the equation of state,
/C22p ¼ ~T
X
N
q¼1
/C22qqRq (13)
where T is the temperature and R is the speciﬁc gas constant. The
species diffusion velocity, the stress tensor, and the heat ﬂux vec-
tor are given, respectively, by
/C22qq ~uq ¼/C0 /C22qDqr ~Yq (14)
r ¼ l½r~u þð r~uÞT /C138/C0 2
3 ½lr/C1~u þ /C22qk/C138I (15)
q ¼/C0 kr ~T þ
XN
q¼1
~hq /C22qq ~uq (16)
where Yq is the mass fraction of the qth species and l, k, and Dq
represent the sum of the molecular and turbulent viscosity, the
thermal conductivity, and the species diffusion coefﬁcient,
respectively.
The thermodynamic properties for the thermally perfect gas
have been expressed by means of a polynomial temperature curve
ﬁt. The molecular transport properties have been determined
from a model based on the Chapman–Enskog theory, which
amounts to solve the Boltzmann equation for the singlet-velocity
distribution function. The mixture viscosity and thermal conduc-
tivity have been computed by means of Wilke’s [ 28] law and of
Waassiljewa’s [29] formula.
The governing equations are solved by a cell-centered ﬁnite
volume approach by using an implicit treatment of the source
terms. The solver uses a high-order total variation diminishing
(TVD) method, which is a generalization of the Harten–Yee
upwind TVD scheme [ 30] extended to multispecies turbulent gas
mixture. Moreover, the model has been extended to include the
effects of turbulence on the transport mechanism of momentum,
energy, and mass. The numerical viscous ﬂuxes are evaluated by
applying Gauss theorem, and the equations are advanced in time
by means of a third-order Runge–Kutta scheme.
As far as the boundary conditions concern, the inﬂow is speci-
ﬁed by setting the values of velocity, pressure, and temperature
and by assuming a zero normal gradient for k and e. In the case of
open boundaries, either freestream conditions or ﬁrst order extrap-
olation conditions are imposed, depending on the ﬂow direction.
At walls, no-slip condition is enforced on the velocity, the pres-
sure is obtained by assuming a zero normal gradient and adiabatic
conditions, and the normal species diffusion ﬂuxes are set to zero.
Moreover, the turbulent kinetic energy and the normal derivative
of e are also set equal to zero at walls.
The code is written in
FORTRAN 90 and is fully parallelized by
using the message-passing interface (MPI) libraries. More details
of the model are reported in Ref. [ 14].
2.1 Turbulent Diffusion Model. In the present work, the
standard k/C0 e model for turbulence, which accounts for low
Reynolds effects by means of wall damping functions suggested
by Speziale et al. [ 31], has been used.
The turbulent viscosity and the wall damping functions are
deﬁned as
lt ¼ clfl /C22q k2
ðes þ ed Þ (17)
f2 ¼½ 1 /C0 expð/C0 yþ=4:9Þ/C1382 (18)
fl ¼ 1 þ 3:45ﬃﬃﬃﬃﬃﬃﬃRet
p
/C18/C19
tanh yþ
70
/C18/C19
(19)
where cl is equal to 0.09 and the viscous coordinate and the
turbulent Reynolds number are deﬁned as yþ ¼ usy=/C23 and
Ret ¼ /C22qðk2=ðllesÞÞ, respectively.
Pope’s correction [ 32] to the e equation has been included to
overcome the well-known round-jet/plane-jet anomaly, so that ce2
becomes
ce2 ¼ 1:92½1 /C0ð 2=9Þexpð/C0 Re2
t =36Þ/C138 /C0 0:79v (20)
where v is a nondimensional measure of the vortex stretching [ 32]
and the dependence on the turbulent Reynolds number is that sug-
gested by Hanjalic and Launder [ 33].
Journal of Fluids Engineering DECEMBER 2013, Vol. 135 / 121101-3
Downloaded from asmedigitalcollection.​asme.​org/​fluidsengineering/​article-pdf/​135/​12/​121101/​6189348/​fe_135_12_121101.​pdf by Dalian University Of Technology user on 31 August 2026

<!-- PDF_PAGE: 4 -->

Moreover, the effect of density ﬂuctuations on turbulence have
been taken into account, since, although applications are limited
to transonic and supersonic ﬂows, such effect is not negligible for
free shear layers, even for sonic Mach number [ 9]. Following the
work of Blaisdell et al. [ 13], two additional terms have been
considered for the turbulent kinetic energy equation (i.e., the
dilatation-dissipation and the pressure-dilatation terms). For the
dilatation-dissipation term, the Sarkar’s model [ 10] has been
implemented, whereas the pressure-dilatation term has been
assumed to be of the same order of the ﬁrst term [ 34]. Sarkar et al.
[10] and Zeman [ 11] have modeled the dilatation-dissipation term
as a function of the turbulence Mach number, M
t, deﬁned as
M2
t ¼ 2k=c2, where c is the speed of sound. They considered that
the equation for the solenoidal dissipation, es, is not inﬂuenced by
compressibility and assumed the dilatation-dissipation, ed, propor-
tional to es, ed ¼ nesFðMtÞ, where n is a closure coefﬁcient and
F(Mt) is a complex function of Mt. In Sarkar’s model, the relation
used is ed ¼ esM2
t . By assuming that the pressure-dilatation and
the dilatation-dissipation terms are of the same order of magnitude
[34], the compressibility correction, P, in the turbulent kinetic
energy equation is P ¼ 3:0M2
t .
However, Blaisdell et al. [ 13] have compared DNS results with
Sarkar’s model and have shown that, beyond Mt ’ 0:3, the ratio
ed/es becomes nearly constant and equal to 0.09. Therefore, fol-
lowing the work of Gross et al. [ 35], the compressibility correc-
tion becomes
P ¼ 3:0 M2
t ; if 0 /C20 Mt /C20
ﬃﬃﬃﬃﬃﬃﬃ
0:1
p
0:1; if Mt >
ﬃﬃﬃﬃﬃﬃﬃ
0:1
p
(
(21)
2.2 Real Gas Model. In order to investigate real gas effects
on the jet structure, both van der Waals and Redlich–Kwong equa-
tions of state have been implemented. The former is probably the
most known EoS, whereas the latter has been chosen as it provides
a very good agreement with the National Institute of Standards
and Technology (NIST) Standard Reference Database [ 36]i n
terms of hydrogen compressibility factor, as shown in Fig. 2. The
ﬁgure shows the compressibility factor versus pressure for
the Redlich–Kwong EoS and for different values of temperature.
The data of NIST [ 36] are also reported for comparison.
The van der Waals and Redlich–Kwong equations for a single
pure gas read
p ¼
RT
v /C0 b /C0 a
v2 (22)
p ¼ RT
v /C0 b /C0 aﬃﬃﬃ
T
p
vðv þ bÞ
(23)
respectively, where v is the speciﬁc volume and a and b are model
constants. Speciﬁcally, the expressions of the speciﬁc heats are
obtained as follows. The total differentiation of the speciﬁc
enthalpy h(p,T)i s
dh ¼
@h
@T
/C18/C19
p
dT þ @h
@p
/C18/C19
T
dp (24)
and from the deﬁnition of the speciﬁc heats and enthalpy
cp ¼ cv /C0 @h
@p
/C18/C19
T
dp
dT þ @e
@v
/C18/C19
T
dv
dT þ dðpvÞ
dT (25)
By writing dh as dh ¼ Tds þ vdp and considering the derivative
with respect to p,
@h
@p
/C18/C19
T
¼ v þ T @s
@p
/C18/C19
T
(26)
By taking into account the Maxwell relationship
@s
@p
/C18/C19
T
¼/C0 @v
@T
/C18/C19
p
(27)
and the following relation:
@v
@T
/C18/C19
p
¼/C0 @p
@T
/C18/C19
v
/C30 @p
@v
/C18/C19
T
(28)
Eq. (25) can be written as
cp ¼ cv /C0 T @p
@T
/C18/C19 2
v
/C30 @p
@v
/C18/C19
T
(29)
where cv is expressed as
cv ¼ cref
v þ
ðv
1
@cv
@v
/C18/C19
T
dv (30)
where the superscript ref indicates the low-pressure reference con-
dition [ 37], corresponding to a reference pressure equal to 100
kPa. From the ﬁrst Gibbs equation and from the deﬁnition of c v,
@cv
@v
/C18/C19
T
¼ T @2p
@T2
/C18/C19
v
(31)
Therefore, the constant pressure–speciﬁc heat can be written as
cp ¼ cref
p /C0 R /C0 T
ð1
v
@2p
@T2
/C18/C19
v
dv /C0 T @p
@T
/C18/C19 2
v
/C30 @p
@v
/C18/C19
T
(32)
Speciﬁc internal energy and speciﬁc enthalpy for real gases have
been computed as follows:
e ¼ eref /C0 RT
ð1
v
T @z
@T
/C18/C19
v
dv
v (33)
h ¼ href /C0 RT
ð1
v
T @z
@T
/C18/C19
v
dv
v /C0 RTð1 /C0 zÞ (34)
where z is the compressibility factor. The extension to a multi-
component gas mixture of N species is obtained by employing the
mixing rules proposed by Reid et al. [ 38], which provide speciﬁc
expressions of the model constants a and b. As regards the speed
of sound, the expression for a gas mixture is given by
Fig. 2 Hydrogen compressibility factor versus pressure for dif-
ferent values of temperature: Redlich–Kwong EoS and NIST
data [36]
121101-4 / Vol. 135, DECEMBER 2013 Transactions of the ASME
Downloaded from asmedigitalcollection.​asme.​org/​fluidsengineering/​article-pdf/​135/​12/​121101/​6189348/​fe_135_12_121101.​pdf by Dalian University Of Technology user on 31 August 2026

<!-- PDF_PAGE: 5 -->

c2 ¼ @p
@q
/C18/C19
s
¼ Kh þ
XN
q¼1
YqXq (35)
where K and Xq are expressed as follows:
K ¼
@p
@T
/C18/C19
qj;j¼1;N
XN
q¼1
qqcref
vq þ @F
@T
/C18/C19
qj;j¼1;N
(36)
Xq ¼ @p
@qq
 !
T;qj;j6¼q
/C0 Keref
q /C0 K @F
@qq
 !
T;qj;j6¼q
(37)
where F is the departure function [ 38].
3 Results
The accuracy and reliability of the computational model has
been assessed by comparing the results with those obtained exper-
imentally by Wang and Andreopoulos [ 16] and Narayanan et al.
[17], who have studied the inﬂuence of the density ratio and com-
pressibility effects of turbulent subsonic jets, and by Woodmansee
et al. [ 6], who have analyzed the ﬂow ﬁeld of an underexpanded
sonic jet. Finally, the model has been used to investigate how the
real gas assumption inﬂuences the structure of underexpanded
hydrogen jets.
3.1 Compressibility Effects in Turbulent Subsonic Jets.
The analysis of the compressibility effects in turbulent jets
has been carried out by considering two test cases, which are
experimentally investigated by Wang and Andreopoulos [ 16] and
Narayanan et al. [ 17].
In Ref. [ 16], free circular jets have been studied that originate
from an initially turbulent pipe, with an inner diameter ( Din)o f
7.0 mm and an outer diameter ( Dout) of 9.5 mm, issuing in ambient
air (pa ¼ 1 atm, Ta ¼ 288 K) at three different subsonic Mach num-
bers (i.e., 0.3, 0.6, and 0.9). Three different gases (i.e., helium,
nitrogen, and krypton) have been used to investigate the inﬂuence
of the density ratio on the ﬂow structure.
In the present work, the computed spreading and centerline
property decay rates have been compared with those obtained
experimentally for the nitrogen injection at Mach number equal to
0.6 and 0.9.
Figure 3 shows the computational domain by plotting every
16th grid point (at the top) and the blow up of the oriﬁce with the
grid plotted every eighth grid point (at the bottom). The two-
dimensional computational domain has been speciﬁed as an open
environment of dimension 0.35 m by 0.175 m in the axial and
radial directions, respectively.
The oriﬁce, shown at the bottom of the left boundary, is set up
as an inﬂow boundary, whereas the boundary between the inner
and outer diameter of the pipe is set up as no slip wall. A low-
velocity coﬂow is considered at the remaining portions of the left
boundary, while open conditions are set at the top and right boun-
daries. By taking advantage of the axial symmetry of the jet, only
half plane of the domain has been considered and axial symmetry
conditions are implemented along the bottom boundary.
The grid is structured and has a uniform spacing in the radial
direction in the oriﬁce up to the outer diameter, whereas it is
stretched elsewhere. Three different grids have been considered
that hereafter will be referred to as COARSE, MEDIUM, and
FINE grids. The COARSE grid includes 1024 cells axially and
512 radially, 28 of which are in the oriﬁce and 10 are along the
wall. The minimum grid spacing is in the oriﬁce and is equal
to 0.125 mm in both the axial and radial direction, whereas the
maximum grid spacing is at the outer boundaries and it is
approximately 1.17 mm and 0.56 mm in the axial and radial direc-
tions, respectively. The MEDIUM and FINE grids have been
obtained by halving the grid spacing of the COARSE grid once
and twice, respectively, in both the axial and radial directions. In
Fig. 3, the MEDIUM grid is shown.
The jet exit temperature has been set up equal to 246.44 K and
264.73 K for the cases with Mach number equal to 0.9 and 0.6,
respectively, whereas in both cases, the jet exit pressure is equal
to 1 atm. In order to include the boundary layer at the exit of the
pipe, a hyperbolic tangent velocity proﬁle has been used,
UðrÞ¼ Uð0Þtanh
r0 /C0 r
2dh
/C18/C19
(38)
where r0 is the inner radius and dh is the momentum thickness. By
considering the formula suggested by Zapryagaev and Solotchin
[39] for the displacement thickness,
d/C3 ¼ 1:73½1 þ 0:5ðc /C0 1ÞM2/C138
ﬃﬃﬃﬃﬃﬃﬃﬃﬃ
LDin
Re
r
(39)
where L is the converging or run-up distance of the nozzle, and
the deﬁnition of the displacement thickness
Uð0Þ½r2
0 /C0ð r0 /C0 d/C3 Þ2/C138¼
ðr0
0
2½Uð0Þ/C0 UðrÞ/C138rdr (40)
a momentum thickness to jet radius dh/r0 equal to 0.0342 and 0.04
has been computed for the cases with Mach number equal to 0.9
and 0.6, respectively.
A limit on the time step has been imposed by using a Courant
number equal to 0.9.
In order to verify the grid independence of the results, the simu-
lation of the jet with Mach number equal to 0.9 has been carried
out by using the three different grids and the results, in terms of
centerline velocity normalized by the exit velocity as a function of
the axial distance normalized by the inner diameter of the pipe,
are shown in Fig. 4. The ﬁgure shows that the proﬁles obtained
Fig. 3 Computational domain for subsonic nitrogen jets. The
grid lines are shown every 16th and 8th grid point in the compu-
tational domain (at the top) and in the blow up (at the bottom),
respectively.
Journal of Fluids Engineering DECEMBER 2013, Vol. 135 / 121101-5
Downloaded from asmedigitalcollection.​asme.​org/​fluidsengineering/​article-pdf/​135/​12/​121101/​6189348/​fe_135_12_121101.​pdf by Dalian University Of Technology user on 31 August 2026

<!-- PDF_PAGE: 6 -->

with the two ﬁner grids are on top of each other; therefore, the
MEDIUM grid is used hereafter.
Figure 5 shows the centerline velocity proﬁles obtained with
both Mach numbers equal to 0.6 and 0.9 together with the
experimental data. As physically expected and in agreement with
experimental measurements [ 9,15,16], the potential core is longer
and the velocity decades slower with increasing Mach number.
The ﬁgure shows that a very good agreement is found between
the numerical results and the experimental data, except in the ﬁrst
5–6 diameters distance, where experiments show that the ﬂow
accelerates before it starts to decay. Wang and Andreopoulos give
an explanation based on the pipe frictional effects, which cause
further gas acceleration along the centerline towards a Mach 1
state if the length were unlimited and a deceleration in the near
wall region. This experimental outcome is not possible to be
reproduced in the simulations, because subsonic jet conditions
have been considered in the full section of the oriﬁce. However,
this discrepancy does not inﬂuence the reliability and accuracy of
the model, which is able to correctly predict the velocity decay, as
shown in the ﬁgure.
To conﬁrm the solver reliability and accuracy, the jet experi-
mental setup of Ref. [ 17] (i.e., an isothermal air jet at Mach num-
ber equal to 0.6) has been considered. This case does not show
any gas acceleration in the centerline at the jet exit. The jet is
issued in still air from a nozzle with an exit diameter equal to
82.27 mm.
The jet exit temperature is equal to 299.82 K, whereas the am-
bient temperature is equal to 301.48 K. The jet and the ambient
pressure has been set up equal to 1 atm.
The computational domain is of dimension 4.9362 m by
4.9856 m in the axial and radial directions, respectively. The
boundary conditions are the same as in the previous case. By con-
sidering a converging distance of the nozzle equal to three diame-
ters, a momentum thickness to jet radius equal to 0.0436 has been
obtained by using Eqs. (38) and (39).
In order to verify the grid independence of the results, two dif-
ferent meshes have been considered. Table 1 summarizes the
number of computational cells and the grid resolution in terms of
maximum/minimum grid spacing in the axial/radial direction,
Dx/r
max/min, for both meshes. A Courant number equal to 0.9 has
been used.
Figure 6 shows the centerline velocity normalized by the exit
velocity as a function of the axial distance normalized by the noz-
zle diameter for both grids, thus showing a good grid conver-
gence. Experimental results are also reported, thus showing a very
good agreement in terms of both potential core length and center-
line velocity decay rate.
The two nitrogen subsonic jets with different Mach numbers
have been further analyzed to get their spreading rates in the self-
similar region. As far as the self-similar condition regards, the
axial velocity normalized by centerline velocity has been plotted
as a function of radial distance normalized by the half-width, r
1/2,
which is the radial distance at which the velocity is half of the
centerline velocity, at different axial locations. The self-similar
region has been deﬁned as the region where the proﬁles are on top
of each other.
Figure 7 shows the velocity radial proﬁles for both Mach num-
bers in the self-similar region at two axial locations downstream
of the injector exit (i.e., 11.86 and 20 diameters for the case with
Mach number equal to 0.9 and 12.57 and 17.86 for the case with
Mach number equal to 0.6). In Ref. [ 16], the authors found self-
similar conditions between 14 and 20 diameters downstream of
the tube exit for both Mach numbers.
Fig. 4 Subsonic nitrogen jets: grid independence analysis in
terms of normalized centerline velocity proﬁle
Fig. 5 Subsonic nitrogen jets: comparison of numerical
results (lines) and experimental data [16] (symbols) in terms of
normalized centerline velocity proﬁles
Table 1 Subsonic air jet: details of the grids resolution
COARSE FINE
Oriﬁce cells 80 120
Wall cells 16 24
Radial cells 1024 1536
Axial cells 2048 3072
Dx
max (m) 1.19 /C2 10–2 7.93 /C2 10–3
Dxmin (m) 5.14 /C2 10–4 3.43 /C2 10–4
Drmax (m) 1.23 /C2 10–2 8.23 /C2 10–2
Drmin (m) 5.14 /C2 10–4 3.43 /C2 10–4
Fig. 6 Subsonic air jet: comparison of numerical results (lines)
and experimental data [ 17] (symbols) in terms of normalized
centerline velocity proﬁles and grid independence analysis
121101-6 / Vol. 135, DECEMBER 2013 Transactions of the ASME
Downloaded from asmedigitalcollection.​asme.​org/​fluidsengineering/​article-pdf/​135/​12/​121101/​6189348/​fe_135_12_121101.​pdf by Dalian University Of Technology user on 31 August 2026

<!-- PDF_PAGE: 7 -->

Figure 8 shows the half-width, r1/2, for both cases as a function
of the axial distance. The spreading rate, which is the slope of the
two straight lines, is equal to 0.057 and 0.072 for Mach number
0.9 and 0.6, respectively. This ﬁnding conﬁrms lower values of
the decay rates at higher Mach number. The decrease of spreading
rate with increasing Mach number is also observed in Ref. [ 16],
where a spreading rate of 0.058 and 0.071 was measured for Mach
number 0.9 and 0.6, respectively.
3.2 Underexpanded Air Jet. The case of an underexpanded
air jet issuing into air has been analyzed by using the same test
speciﬁcations employed by Woodmansee et al. [ 6], in order to val-
idate the computational model against measurements. In Ref. [ 6],
nonintrusive pressure and temperature measurements in the ﬂow
ﬁeld of the underexpanded sonic jet have been performed by using
the high-resolution nitrogen CARS technique.
The jet is originated from a convergent nozzle with an exit
diameter of 5 mm, issuing in still air with pressure equal to
p
a ¼ 0.98 atm and temperature equal to Ta ¼ 294 K. The jet exit
conditions, in terms of pressure and temperature, are those shown
in the experimental radial proﬁles [ 6] measured at the exit of the
nozzle. Therefore, the jet exit pressure has been imposed equal to
316 kPa, whereas a hyperbolic tangent proﬁle has been used to
model the thermal boundary layer as follows:
TðrÞ¼ Tðr
0Þþ½ Tð0Þ/C0 Tðr0Þ/C138tanh r0 /C0 r
2dt
/C18/C19
(41)
where the axial and the wall temperatures have been set up equal
to 252 K and 189 K, respectively, as shown in Ref. [ 6]. In this
case, the ratio dt/r0 has been assumed equal to 0.0238 by assuming
that the thermal boundary layer thickness is dT ¼ d=Pr1=3, as indi-
cated in Ref. [ 40], where d is the velocity boundary layer thick-
ness and Pr is the Prandtl number, assumed equal to 0.72.
As regards the jet exit velocity proﬁle, Eq. (38) has been
employed, where the momentum thickness to jet radius, computed
on the basis of Eq. (39), has been imposed equal to 0.0208.
The computational domain is of dimensions 0.25 m by 0.125 m
in the axial and radial directions, respectively. The boundary con-
ditions are the same as in the previous cases. A Courant number
equal to 0.9 has been used.
The grid independence has been assessed by using three differ-
ent grid resolutions. The details of each grid are summarized in
Table 2. The pressure proﬁles along the jet centerline, by using
the three different grids, are plotted in Fig. 9, thus showing that
the grid independence is already reached with the MEDIUM grid.
Hereafter, the results obtained with the FINE grid are shown.
In Fig. 10, the computational shadowgraph is given, thus show-
ing that the computational model accurately resolves the distinc-
tive features of the underexpanded jet, such as the Mach disk
location, the triple point, the slip line, and the curved jet boundary,
and that the computational results are in good agreement with the
experimental shadowgraph in Ref. [ 6].
A comparison between the CARS measurements and the nu-
merical results, in terms of temperature and pressure along the jet
centerline, is shown in Figs. 11(a) and 11(b), respectively. In this
ﬁgure and also in the others of this section, the CARS data are
mean values determined from ten time-averaged spectra acquired
at each measurement location. The uncertainty bars represent the
standard deviation of the ten values. Where the bars are missing,
it means that the uncertainty of the CARS measurements falls
within the size of the data symbols. Both temperature and pressure
proﬁles are in very good agreement with measurements. Both
temperature and pressure decrease quickly before increasing
suddenly passing through the Mach disk. Downstream of the
Mach disk location, a regular pattern occurs, due to the periodicity
of expansion and compression waves, in which the frequency is
Fig. 7 Subsonic nitrogen jets: velocity proﬁles in similarity
coordinates
Fig. 8 Subsonic nitrogen jets: spreading rates for the sub-
sonic jets
Table 2 Under expanded air jet: details of the grids resolution
COARSE MEDIUM FINE
Oriﬁce cells 20 30 45
Wall cells 8 12 18
Radial cells 256 384 576
Axial cells 512 768 1152
Dx
max (m) 18.70 /C2 10–4 12.47 /C2 10–4 8.31 /C2 10–4
Dxmin (m) 1.25 /C2 10–4 8.33 /C2 10–5 5.56 /C2 10–5
Drmax (m) 9.59 /C2 10–4 6.39 /C2 10–4 4.26 /C2 10–4
Drmin (m) 1.25 /C2 10–4 8.33 /C2 10–5 5.56 /C2 10–5
Fig. 9 Underexpanded air jet: grid independence analysis in
terms of centerline pressure
Journal of Fluids Engineering DECEMBER 2013, Vol. 135 / 121101-7
Downloaded from asmedigitalcollection.​asme.​org/​fluidsengineering/​article-pdf/​135/​12/​121101/​6189348/​fe_135_12_121101.​pdf by Dalian University Of Technology user on 31 August 2026

<!-- PDF_PAGE: 8 -->

correctly captured by the numerical simulations with respect to
experiments.
Figures 12(a) and 12(b) show the radial proﬁles of temperature
and pressure at x/Din ¼ 1.28, respectively. The results are in very
good agreement with measurements for both temperature and
pressure proﬁles.
From this study, it can be concluded that the computational
model provides good results that are in agreement with the physi-
cal structure of the jets in the entire domain.
3.3 Real Gas Effects in Hydrogen Underexpanded Jets. In
order to evaluate the inﬂuence of real gas assumption on the
behavior of underexpanded hydrogen jets, simulations have been
performed by employing the ideal gas assumption, the van der
Waals, and the Redlich–Kwong equations of state. A highly
underexpanded hydrogen sonic jet, issuing into still nitrogen from
a nozzle with an inner and outer diameter equal to 0.3 mm and
0.6 mm, respectively, has been considered. The total pressure and
temperature in the injector are set up equal to 75 MPa and 300 K,
respectively, whereas the ambient pressure and temperature are
equal to 5 MPa and 300 K, respectively.
The computational domain is of dimensions 0.015 m by
0.012 m in the axial and radial directions, respectively.
Two grids have been used, a ﬁne mesh with 1200 cells axially
and 600 radially, 30 of which are located in the oriﬁce and 30
along the wall, and a coarse one with 800 cells axially and 400
radially, 20 of which are in the oriﬁce and 20 along the wall. In
the ﬁne mesh, the minimum grid spacing is in the oriﬁce and is
equal to 0.005 mm in both the axial and radial direction, whereas
the maximum grid spacing is at the outer boundaries and is
approximately 0.05 mm and 0.039 mm in the axial and radial
directions, respectively.
The boundary conditions are the same as in the previous cases.
As regards the jet exit velocity proﬁle, Eq. (38) has been
employed, where the momentum thickness to jet radius has been
imposed equal to 0.03. The Courant number is equal to 0.1.
The jet exit properties, computed by considering an isentropic
expansion through the nozzle under the ideal assumption (a) and
with the van der Waals (b) and Redlich–Kwong (c) EoS, are sum-
marized in Table 3, thus showing large differences between the
ideal and real gas EoS, especially in terms of gas velocity and
gas density. Moreover, the use of the van der Waals and
Redlich–Kwong EoS provides a mass ﬂow rate that is 10.1% and
8.7% smaller, respectively, than that computed with the ideal
assumption.
Figure 13 shows the pressure centerline proﬁles under the ideal
gas assumption, obtained by using the two different computational
grids. The proﬁles are in very good agreement up to the Mach
disk location, whereas there are slight differences downstream the
region where the periodic structure takes place. However, the use
of a ﬁner mesh than the ones employed in this work would require
Fig. 10 Shadowgraph ﬁeld of the air underexpanded jet
Fig. 11 Temperature ( a) and pressure ( b) along the air under-
expanded jet centerline
Fig. 12 Radial temperature ( a) and radial pressure (b) distribu-
tion of the air underexpanded jet atx/Din 5 1.28
Table 3 Hydrogen jet exit properties: ideal ( a), van der Waals
(b), Redlich–Kwong (c)
ab (diff. %) c (diff. %)
p (MPa) 39.98 33.26 (16.8%) 35.08 (12.3%)
T (K) 253.37 241.70 (4.6%) 244.89 (3.3%)
q (kg/m3) 38.25 24.95 (34.8%) 27.13 (29.1%)
u (m/s) 1197.05 1652.71 (38.1%) 1540.57 (28.7%)
_m (g/s) 2.98 2.68 (10.1%) 2.72 (8.7%)
121101-8 / Vol. 135, DECEMBER 2013 Transactions of the ASME
Downloaded from asmedigitalcollection.​asme.​org/​fluidsengineering/​article-pdf/​135/​12/​121101/​6189348/​fe_135_12_121101.​pdf by Dalian University Of Technology user on 31 August 2026

<!-- PDF_PAGE: 9 -->

a prohibitive amount of computational resources. On the other
hand, the grid analysis, performed for the case of the underex-
panded air jet, has shown that the use of 30 computational cells in
the injector provides accurate results. Therefore, the results with
the ﬁner grid will be shown in what follows in order to assess the
effects of real gas.
Figure 14 shows the contour plots of temperature, pressure, and
Mach number, respectively, obtained by considering ideal and
both real gas assumptions. In all cases, the typical structure of
underexpanded jets is recovered. The normalized barrel length is
equal to 2.50, 2.64, and 2.57 when the ideal assumption, the van
der Waals, and the Redlich–Kwong EoS are employed, respec-
tively. These values are in good agreement with the empirical cor-
relation of Ashkenas and Sherman [ 27], L
b=Din ¼ 0:67
ﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ
p0=pa
p
,
which gives a normalized barrel length equal to 2.59. The ideal
gas assumption slightly underestimates the barrel length, whereas
a better agreement is achieved by using the Redlich–Kwong EoS.
Fig. 13 Underexpanded hydrogen jet: grid independence anal-
ysis in terms of centerline pressure
Fig. 14 Temperature, pressure, and Mach number contour
plots for the hydrogen jet: ideal ( a), van der Waals (b), Redlich-
Kwong (c)
Fig. 15 Temperature, pressure, and Mach number along the
hydrogen underexpanded jet centerline
Journal of Fluids Engineering DECEMBER 2013, Vol. 135 / 121101-9
Downloaded from asmedigitalcollection.​asme.​org/​fluidsengineering/​article-pdf/​135/​12/​121101/​6189348/​fe_135_12_121101.​pdf by Dalian University Of Technology user on 31 August 2026

<!-- PDF_PAGE: 10 -->

Besides, Fig. 14 shows a Mach disk diameter slightly smaller
when the real gas assumption is employed.
The centerline proﬁles of temperature, pressure, and Mach
number of Fig. 15 show that the results are strongly affected by
the EoS. As regards temperature, the proﬁles are on the top of
each other up to the Mach disk location, whereas downstream of
the Mach disk, the van der Waals and the Redlich–Kwong
EoS give a higher value of the maximum temperature (equal to
335.90 K and 326.90 K, respectively) than the ideal gas assump-
tion (292.81 K). In the region where periodic ﬂow structures take
place, the real gas EoS temperature proﬁles are below the ideal
one. Similarly, the pressure proﬁles show large differences
among the three different EoS, with the maximum pressures equal
to 7.95 MPa, 7.60 MPa, and 6.26 MPa when the ideal assumption,
the van der Waals, and the Redlich–Kwong EoS are employed,
respectively. As regard the Mach number proﬁles, the van der
Waals and the Redlich–Kwong EoS provide a maximum Mach
number equal to 4.95 and 4.82 and a minimum Mach number
equal to 0.25 and 0.30, respectively, whereas the maximum and
minimum Mach number predicted by the ideal assumption are
equal to 4.45 and 0.39, respectively. Finally, large differences, in
terms of Mach number, among the real and the ideal assumptions
are also found in the periodic ﬂow structure.
4 Conclusions
In this work, an accurate, high-performance computational
model has been implemented and validated in order to analyze the
structure of hydrogen underexpanded jets. A comprehensive
understanding of the jet structure is important dealing with hydro-
gen injection in engineering devices, such as internal combustion
engines, in order to develop new strategies and to improve the per-
formance and efﬁciency of hydrogen propulsion systems. Besides,
this subject is important also for safety issues dealing with the
sudden release of hydrogen from a high-pressure tube or pipe in
the case of failure.
In order to validate the computational model and compare the
numerical results with available measurements, different test
cases have been considered based on some experimental studies
available in the literature. These studies are concerned with
nitrogen and air turbulent subsonic jets, with different exit Mach
number, and air underexpanded jets. In all cases, the results show
a very good agreement with the experimental data, thus conﬁrm-
ing the suitability and accuracy of the computational model to
provide the velocity centerline decay, the Mach disk structure,
and its axial location.
Then, the computational model has been used to study the inﬂu-
ence of real gas effects on the structure of a highly underexpanded
hydrogen jet, issued from a tank with total pressure equal to
75 MPa into still nitrogen at pressure equal to 5 MPa. In this case,
two equations of state have been used, other than the ideal gas
EoS (i.e., the van der Waals and the Redlich–Kwong EoS). The
real gas EoS provides different jet exit conditions with respect to
those computed with the ideal assumption, with differences up to
38.1% and 34.1% in terms of gas velocity and gas density, respec-
tively. Moreover, the mass ﬂow rates computed with the van der
Waals and the Redlich–Kwong EoS are lower than that computed
under the ideal assumption, with differences of 10.1% and
8.7%, respectively. In all three cases, the typical structure of an
underexpanded jet is well recovered, with the barrel length in
good agreement with the empirical correlation of Ref. [ 27]. Slight
differences in terms of barrel length and Mach disk diameter
occur when the ideal and the real gas EoS are employed. As far as
the centerline proﬁles are concerned, the use of the van der Waals
and the Redlich–Kwong EoS provides an increase of the maxi-
mum temperature of about 14.7% and 11.64%, an increase of the
pressure downstream of the Mach disk of about 27.0% and 21.4%,
and an increase of the maximum Mach number of about 11.2%
and 8.3%, respectively, with respect to the ideal assumption.
Lower values of the minimum Mach number (i.e., 35.9% and
23.1%, respectively) than those computed under the ideal assump-
tion are obtained with the van der Waals and the Redlich–Kwong
EoS.
Acknowledgment
Most of the computations have been performed by employing
the HPC resources of the IBM PLX-GPU located at CINECA
(Italy) and of the Supernova Linux Cluster located at WCSS
(Poland), made available within the Distributed European Com-
puting Initiative by the PRACE-2IP, receiving funding from
the European Community’s Seventh Framework Programme
(FP7/2007-2013) under grant agreement No. RI-283493. Some
computations were performed under the HPC-EUROPA2 project
(project number 228398) with the support of the European Com-
mission Capacities Area Research Infrastructures Initiative and by
using CASPUR-Italy resources (Consorzio Interuniversitario per
le Applicazioni di Supercalcolo Per Universit /C19a e Ricerca) under
the Standard HPC Grant 2012.
Nomenclature
a,b ¼ EoS constants
c ¼ speed of sound
cp, cv ¼ constant pressure and constant volume speciﬁc heats
ce1, ce2, cl ¼ turbulence model constants
D ¼ diffusion coefﬁcient
Din, Dout ¼ inner and outer diameter
e ¼ speciﬁc internal energy
E ¼ total energy
f2, fl ¼ wall damping function
F ¼ departure function
F ¼ sum of inviscid and viscous ﬂuxes
h ¼ speciﬁc enthalpy
H ¼ total enthalpy
H ¼ source term vector
k ¼ turbulent kinetic energy
L ¼ converging or run-up distance
Lb ¼ barrel length
_m ¼ mass ﬂow rate
M ¼ Mach number
N ¼ number of species
p ¼ static pressure
P ¼ turbulence production by mean velocity gradient
q ¼ total heat ﬂux
r0 ¼ inner radius
R ¼ speciﬁc gas constant
Re ¼ Reynolds number
s ¼ speciﬁc entropy; face length
S ¼ velocity divergence; cell area
T ¼ temperature
u,v ¼ velocity components
ls ¼ friction velocity
v ¼ speciﬁc volume
yþ ¼ viscous coordinate
Y ¼ mass fraction
W ¼ vector unknown
z ¼ compressibility factor
Greek Symbols
c ¼ speciﬁc heats ratio
d ¼ velocity boundary layer thickness
dt ¼ thermal thickness
dT ¼ thermal boundary layer
dh ¼ momentum thickness
d* ¼ displacement thickness
e ¼ dissipation of turbulent kinetic energy
k ¼ thermal conductivity
l ¼ viscosity
121101-10 / Vol. 135, DECEMBER 2013 Transactions of the ASME
Downloaded from asmedigitalcollection.​asme.​org/​fluidsengineering/​article-pdf/​135/​12/​121101/​6189348/​fe_135_12_121101.​pdf by Dalian University Of Technology user on 31 August 2026

<!-- PDF_PAGE: 11 -->

n ¼ closure coefﬁcient for the dilatation dissipation
model
P ¼ compressibility correction
q ¼ density
r ¼ total stress tensor
rk,re ¼ turbulence model constants
v ¼ nondimensional measure of the vortex stretching
Subscripts
0 ¼ total condition
a ¼ ambient condition
d ¼ dilatation
E ¼ inviscid contribution
l ¼ laminar
s ¼ solenoidal
t ¼ turbulent
V ¼ viscous contribution
Superscripts
/C0¼ Reynolds-averaged
/C24¼ Favre-averaged
ref ¼ reference conditions
References
[1] White, C. M., Steeper, R. R., and Lutz, A. E., 2006, “The Hydrogen-Fueled
Internal Combustion Engine: A Technical Review,” Int. J. Hydrogen Energy ,
31(10), pp. 1292–1305.
[2] Pay, S. I., 1954, Fluid Dynamics of Jets , Van Nostrand, Toronto.
[3] Crist, S., Sherman, P., and Glass, D., 1966, “Study of the Highly Underex-
panded Sonic Jet,” AIAA J., 4(1), pp. 68–71.
[4] Owston, R., Magi, V., and Abraham, J., 2008, “Fuel-Air Mixing Characteristics
of DI Hydrogen Jets,” SAE Paper No. 2008-01-1041.
[5] Panda, J., and Seasholtz, R. G., 1999, “Measurement of Shock Structure and
Shock-Vortex Interaction in Underexpanded Jets Using Rayleigh Scattering,”
Phys. Fluids, 11(12), pp. 3761–3777.
[6] Woodmansee, M. A., Iyer, V., Dutton, J. C., and Lucht, R. P., 2004,
“Nonintrusive Pressure and Temperature Measurements in an Underexpanded
Sonic Jet Flowﬁeld,” AIAA J., 42(6), pp. 1170–1180.
[7] Gorl /C19e, C., Gamba, M., and Ham, F., 2010, “Investigation of an Underexpanded
Hydrogen Jet in Quiescent Air Using Numerical Simulations and Experiments,”
Center for Turbulence Research Annual Research Briefs , Center for Turbulence
Research, Stanford, CA.
[8] Birkby, P., and Page, G. J., 2001, “Numerical Prediction of Turbulent Underex-
panded Sonic Jets Using a Pressure-Based Methodology,” J. Aerosp. Eng.,
215(3), pp. 165–173.
[9] Wilcox, D. C., 1994, Turbulence Modeling for CFD , DCW Industries, Inc., La
Ca~nada, CA.
[10] Sarkar, S., Erlebacher, G., Hussaini, M. Y., and Kreiss, H. O., 1989, “The
Analysis and Modeling of Dilatational Terms in Compressible Turbulence,”
Univ. Space Research Assoc. ICASE Report No. 89-79.
[11] Zeman, O., 1990, “Dilatation Dissipation: The Concept and Application in
Modeling Compressible Mixing Layers,” Phys. Fluids A , 2(2), pp. 178–188.
[12] Wilcox, D. C., 1992, “Dilatation-Dissipation Corrections for Advanced Turbu-
lence Models,” AIAA J., 30(11), pp. 2639–2646.
[13] Blaisdell, G. A., Mansour, N. M., and Reynolds, W. C., 1993, “Compressibility
Effects on the Growth and Structure of Homogeneous Turbulent Shear Flow,”
J. Fluid Mech. , 256, pp. 443–485.
[14] Grasso, F., and Magi, V., 1995, “Simulation of Transverse Gas Injection in
Turbulent Supersonic Air Flows,” AIAA J., 33(1), pp. 56–62.
[15] Abramovich, G. N., 1963, The Theory of Turbulent Jets , MIT, Cambridge, MA.
[16] Wang, Z., and Andreopoulos, Y., 2010, “Density and Compressibility Effects in
Turbulent Subsonic Jets Part 1: Mean Velocity Field,” Exp. Fluids , 48(2), pp.
327–343.
[17] Narayanan, S., Barber, T. J., and Polak, D. R., 2002, “High Subsonic Jet Experi-
ments: Turbulence and Noise Generation Studies,” AIAA J. , 40(3), pp.
430–437.
[18] Cheng, G., Anderson, P., and Farmer, R., 1997, “Development of CFD Model
for Simulating Gas/Liquid Injectors in Rocket Engine Design,” 33rd AIAA/
ASME/SAE/ASEE Joint Propulsion Conference and Exhibit, American Insti-
tute of Aeronautics and Astronautics (AIAA).
[19] Cheng, G., and Farmer, R., 2003, “Development of Efﬁcient Real-Fluid Model
in Simulating Liquid Rocket Injector Flows,” 39th AIAA/ASME/SAE/ASEE
Joint Propulsion Conference and Exhibit, American Institute of Aeronautics
and Astronautics (AIAA).
[20] Zong, N., Meng, H., and Hsieh, S. Y., 2004, “A Numerical Study of Cryogenic
Fluid Injection and Mixing Under Supercritical Conditions,” Phys. Fluids ,
16(12), pp. 4248–4261.
[21] Masquelet, M. M., 2006, “Simulations of a Sub-Scale Liquid Rocket Engine:
Transient Heat Transfer in a Real Gas Environment,” M.S. thesis, Georgia Insti-
tute of Technology, Atlanta, GA.
[22] Lim, J., Kim, Y., Lee, S., Chung, J., Kang, W., and Min, K., 2010, “3-D Simu-
lation of the Combustion Process for Di-Methyl Ether-Fueled Diesel Engine,”
J. Mech. Sci. Technol. , 24(12), pp. 2597–2604.
[23] Hohmann, S., and Renz, U., 2003, “Numerical Simulation of Fuel Sprays at
High Ambient Pressure: The Inﬂuence of Real Gas Effects and Gas Solubility
on Droplet Vaporisation,” Int. J. Heat Mass Transfer , 46(16), pp. 3017–3028.
[24] Lapuerta, M., Ballesteros, R., and Agudelo, J. R., 2006, “Effect of the Gas State
Equation on the Thermodynamic Diagnostic of Diesel Combustion,” Appl.
Therm. Eng., 26, pp. 1492–1499.
[25] Perrone, A., Viggiano, A., and Magi, V., 2011, “Investigation of Real Gas
Effects on Hydrogen Underexpanded Jets,” XX International Symposium on
Air Breathing Engines 2011 (ISABE 2011), American Institute of Aeronautics
and Astronautics (AIAA), Curran, pp. 1903–1912.
[26] Khaksarfard, R., Kameshki, M. R., and Paraschivoiu, M., 2010, “Numerical
Simulation of High Pressure Release and Dispersion of Hydrogen Into Air With
Real Gas Model,” Shock Waves, 20(3), pp. 205–216.
[27] Ashkenas, H., and Sherman, F., 1965, “Structure and Utilization of Supersonic
Free Jets in Low Density Wind Tunnels,” NASA Technical Report No.
CR-60423.
[28] Wilke, C. R., 1950, “A Viscosity Equation for Gas Mixture,” J. Chem. Phys. ,
18(4), pp. 517–519.
[29] Berman, H. A., Anderson, J. D., and Drummond, J. P., 1983, “Supersonic Flow
Over a Rearward Facing Step With Transverse Nonreacting Hydrogen
Injection,” AIAA J., 21(12), pp. 1707–1713.
[30] Yee, H. C., and Harten, A., 1987, “Implicit TVD Schemes for Hyperbolic Con-
servation Laws in Curvilinear Coordinates,” AIAA J., 25(2), pp. 266–274.
[31] Speziale, C. G., Abid, R., and Anderson, E. C., 1990, “A Critical Evaluation of
Two-Equation Models for Near Wall Turbulence,” AIAA Paper No. 90-1481.
[32] Pope, S. B., 1978, “An Explanation of the Turbulent Round-Jet/Plane Jet
Anomaly,” AIAA J., 16(3), pp. 279–281.
[33] Hanjalic, K., and Launder, B. E., 1976, “Contribution Towards a Reynolds
Stress Closure for Low-Reynolds-Number Turbulence,” J. Fluid Mech. , 74(4),
pp. 593–610.
[34] Erlebacher, G., Hussaini, M. Y., Kreiss, O., and Sarkar, S., 1990, “The Analysis
and Simulation of Compressible Turbulence,” NASA Technical Report No.
CR-181997.
[35] Gross, N., Blaisdell, G. A., and Lyrintzis, A. S., 2011, “Analysis of Modiﬁed
Compressibility Corrections for Turbulence Models,” 49th AIAA Aerospace
Sciences Meeting including the New Horizons Forum and Aerospace Exposi-
tion, American Institute of Aeronautics and Astronautics (AIAA), Curran.
[36] Lemmon, E. W., McLinden, M. O., and Friend, D. G., 2013, “Thermophysical
Properties of Fluid Systems,” NIST Chemistry WebBook , NIST Standard Refer-
ence Database Number 69, P. J. Linstrom and W. G. Mallard, eds., National
Institute of Standards and Technology, Gaithersburg MD.
[37] Prausnitz, D., Lichtenthaler, R., and Azevedo, E. D., 1986, Molecular Thermo-
dynamics for Fluid Phase Equilibrium , Prentice-Hall, Englewood Cliffs, NJ.
[38] Reid, R., Prausnitz, J., and Poling, B., 1987, The Properties of Gases and
Liquids, 4th ed., McGraw-Hill, New York.
[39] Zapryagaev, V. I., and Solotchin, A. V., 1997, “An Experimental Investigation
of the Nozzle Roughness Effect on Streamwise Vortices in a Supersonic Jet,”
J. Appl. Mech. Tech. Phys. , 38(1), pp. 78–86.
[40] Schlichting, H., 1979, Boundary Layer Theory , 7th ed., McGraw-Hill, New
York.
Journal of Fluids Engineering DECEMBER 2013, Vol. 135 / 121101-11
Downloaded from asmedigitalcollection.​asme.​org/​fluidsengineering/​article-pdf/​135/​12/​121101/​6189348/​fe_135_12_121101.​pdf by Dalian University Of Technology user on 31 August 2026
