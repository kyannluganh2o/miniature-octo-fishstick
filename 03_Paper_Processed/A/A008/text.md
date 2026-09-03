<!-- PDF_PAGE: 1 -->

NUMERICAL ANAL YSIS OF THE COMBUSTION PROCESS IN DUAL-FUEL
ENGINES WITH DIRECT INJECTION OF NATURAL GAS
Michael Jud∗, Christoph Wieland, Georg Fink, Thomas Sattelmayer
Lehrstuhl f ¨ur Thermodynamik
T echnische Universit¨at M ¨unchen
85748 Garching, Germany
jud@td.mw.tum.de
ABSTRACT
An efﬁcient computational ﬂuid dynamics model for predict-
ing high pressure dual-fuel combustion is one of the most essen-
tial steps in order to improve the concept, to reduce the number
of experiments and to make the development process more cost-
efﬁcient. For Diesel and natural gas such a model developed
by the authors is ﬁrst used to analyze the combustion process
with respect to turbulence chemistry interaction and to clarify the
question whether the combustion process is limited by chemistry
or the mixing process. On the basis of these ﬁndings a reduced
reaction mechanism is developed in order to save up to 35% of
computing time. The prediction capability of the modiﬁed com-
bustion model is tested for different gas injection timings repre-
senting different degrees of premixing before ignition. Compared
to experimental results from a rapid compression expansion ma-
chine, the shape of heat release rate, the ignition timing of the
gas jet and the burnout are well predicted. Finally, misﬁring
observed at different geometric conﬁgurations in the experiment
are analyzed with the model. It is identiﬁed that in these geomet-
ric conﬁgurations at low temperature levels the gas jet covers
the preferred ignition region of the diesel jet. Since the model is
based on the detailed chemistry approach, it can in future also
be used for other fuel combinations or for predicting emissions.
INTRODUCTION AND MOTIVATION
In recent years, research activity in the ﬁeld of alternative
fuels for heavy-duty internal combustion engines has increased.
∗Address all correspondence to this author.
Due to the low C/H-ratio of methane, a signiﬁcant CO 2 reduc-
tion can be achieved by using natural gas. The use of classical
lean burn engines for natural gas combustion however, leads to
a considerable methane slip due to ﬂame quenching at the wall
and overlap in valve timing. Because of the considerably strong
global warming potential of methane this needs to be avoided.
By using a methane direct injection concept instead of premix-
ing, this slip can be avoided and a signiﬁcant reduction potential
for greenhouse gas emissions results. Since in this concept a
small quantity of Diesel pilot fuel can act as an ignition source
for different main fuels, a ﬂexible combustion system for differ-
ent alternative fuels is provided.
Nowadays, numerical simulation is an essential part of the
development process of new combustion systems. A simulation
concept for high pressure dual-fuel (HPDF) combustion based
on detailed chemistry calculation was ﬁrst shown by Zoldak et
al. [1]. Zoldak used an unvalidated model to investigate the emis-
sion behavior at different engine operating modes. A similar con-
cept was proposed in [2] and validated using measurements per-
formed on a rapid compression expansion machine (RCEM). The
validation experiments were performed at a temperature level of
780 K and at a pressure level of 75 bar using a ﬁxed arrangement
of a single gas and single Diesel jet. The simulations showed
good qualitative agreement with the measurements for partially
premixed and mainly diffusive natural gas combustion. This
model will be used as starting point for further investigations in
this paper.
The goal of this paper is to present a numerical combus-
tion model for a wide temperature and pressure range, variation
Proceedings of the ASME 2018 
Internal Combustion Engine Division Fall Technical Conference 
ICEF2018 
November 4-7, 2018, San Diego, CA, USA 
ICEF2018-9579
1
Copyright © 2018 ASME
Downloaded from asmedigitalcollection.​asme.​org/​ICEF/​proceedings-pdf/​ICEF2018/​51999/​V002T06A008/​2444299/​v002t06a008-icef2018-9579.​pdf by Dalian University Of Technology user on 31 August 2026

<!-- PDF_PAGE: 2 -->

of the geometrical arrangements of gas and Diesel jet as well as
variation in injection timing. Since the two most critical points of
the simulation concept presented in [2] are the disregard of direct
coupling of turbulence and chemistry and the high computational
effort of detailed chemistry calculation, these will be the main fo-
cus for model improvement. In this context, the question will be
clariﬁed whether the mixing process or reaction chemistry limits
the combustion at different injection strategies. Finally, the im-
proved model is used to make predictions for different operating
conditions. To reduce the number of possible different valida-
tion conﬁgurations, all investigations are limited to ﬁnal com-
pression temperatures of 780 K (at 75 bar) or 920 K (at 125 bar)
and angles of −20◦ or +10◦ between gas and Diesel jet (see Fig.
1). The low temperature and pressure case represents a low load
engine operating point, cold start operation or the use of miller
valve timings. The high temperature and pressure case represents
a mid or full load engine operating point.
NUMERICAL MODEL DESCRIPTION AND EXPERIMEN-
TAL SETUP
The CONVERGE [3] solver for Reynolds-Averaged
Navier–Stokes equations (RANS) is used for computational ﬂuid
dynamics (CFD) analysis presented below. Automated mesh
generation is used including adaptive mesh reﬁnement (AMR).
Turbulence modeling is based on the renormalization group
(RNG) k-ε model [4] with adjusted turbulent kinetic energy dis-
sipation rate coefﬁcient. For gas direct injection, real gas ef-
fects are considered using the model proposed by Redlich and
Kwong in [5]. For Diesel injection and breakup, the blob injec-
tion model of Reitz and Diwakar [6] and the Kelvin-Helmholtz
Rayleigh-Taylor (KH-RT) model [7] are applied. To account for
droplet collision during spray breakup, the model of Schmidt
and Rutland [8] is used. Combustion modeling is based on de-
tailed chemistry calculation in each computational cell, assum-
ing uniform species and temperature distribution within this cell.
Detailed chemistry calculations are performed using the SAGE
solver, which is included in CONVERGE and based on SUN-
DIALS (SUite of Nonlinear and DIfferential/Algebraic Equation
Solver) [9] CVODES solver for stiff and nonstiff ODE systems.
In order to reduce the chemical complexity in computational
combustion analysis, hydrocarbon mixtures like Diesel and nat-
ural gas are generally replaced by reference fuels. That is why
n-heptane is used instead of Diesel and natural gas is represented
by its main component methane in all simulations. Detailed ki-
netic mechanisms for n-heptane and methane are available to pre-
dict chemistry well over a wide range of initial conditions [10].
The computational effort for these mechanisms is unfortunately
too large, even for RANS CFD calculations. Therefore, skele-
tal and reduced mechanisms were developed for speciﬁc prob-
lems and conditions. Numerical studies related to dual-fuel
combustion of n-heptane/methane/air mixtures [11, 12] demon-
strated a good performance of a skeletal mechanism developed
by the Chalmers University in collaboration with the University
of Wisconsin-Madison. This mechanism is hereafter referred as
the Chalmers mechanism [13]. In a previous study, this mech-
anism was shown to perform well for high pressure dual-fuel
(HPDF) combustion at a low ﬁnal compression temperature of
780 K and a ﬁnal compression pressure of 75 bar [2].
The validation experiments are performed using a Rapid
Compression Expansion Machine (RCEM) equipped with a glass
piston, which provides optical access to the combustion cham-
ber. The pressure in the combustion chamber, used for pressure
trace analysis to obtain experimental heat release rates (HRR),
is measured using a pressure transducer. Two single hole nozzle
injectors, one for natural gas direct injection and one for Diesel
injection, are integrated in the cylinder head. The basic geomet-
ric arrangement of the injectors in a plane parallel to the ﬂat
piston is illustrated in Fig. 1. The angle between natural gas
and Diesel jet as well as relative injection timings can be varied
over a wide range of parameters. By default, the angle α is set
to +10◦. For the investigations presented in this paper, the in-
jection parameters of Diesel and natural gas injection were kept
constant (0.11mm/2000bar/3mg, 0.9mm/330bar/80mg). The op-
erating conditions and physical dimensions of the RCEM and the
injectors are summarized in Tab. 1. A detailed description of the
setup can be found in [14,15]. In comparison to the setup in prior
studies, the volume at top dead center (TDC) was reduced to
achieve higher compression ratios and higher ﬁnal compression
temperatures of up to 920 K. This extended setup provides max-
imum ﬂexibility regarding ﬁnal compression temperature and ﬁ-
nal compression pressure.
5 mm
pilot injector natural gas
injector
10 mm
α
FIGURE 1: GEOMETRIC
ARRANGEMENT OF GAS AND
DIESEL INJECTOR IN A PLANE PARALLEL TO THE FLAT
PISTON.
2
Copyright © 2018 ASME
Downloaded from asmedigitalcollection.​asme.​org/​ICEF/​proceedings-pdf/​ICEF2018/​51999/​V002T06A008/​2444299/​v002t06a008-icef2018-9579.​pdf by Dalian University Of Technology user on 31 August 2026

<!-- PDF_PAGE: 3 -->

TABLE 1: OPERATING CONDITIONS AND PHYSICAL DI-
MENSIONS OF THE RCEM TEST RIG, THE DIESEL AND
THE GAS INJECTOR.
Dimension Value
Bore (mm) 220
Compression ratio up to 24
Final compression temperature (K) up to 920
Diesel injection pressure (bar) 2000
Diesel nozzle diameter (mm) 0.11
Diesel mass (mg) 3
Gas injection pressure (bar) 330
Gas nozzle diameter (mm) 0.9
Gas mass (mg) 80
COMBUSTION CHARACTERIZATION FOR MODEL IM-
PROVEMENT
When using detailed chemistry calculation in combination
with RANS or LES, the disregard of direct coupling of the tur-
bulent ﬂow ﬁeld and chemical reaction rates is often criticized.
At this point it should be made clear again that the model based
on the SAGE solver described above does not include a direct
coupling either. That’s why the ﬁrst part of this section is a
short digression to evaluate the effects of turbulence chemistry
interaction (TCI) on dual-fuel combustion with natural gas di-
rect injection. The second part discusses the inﬂuence of natural
gas chemistry on the combustion process depending on injection
strategies and operating conditions. These two investigations can
give an indication of whether combustion is limited by the mix-
ing process or by chemistry. In case of limitation by the mixing
process, chemistry becomes less important and a potential for
reaction mechanism reduction results.
Turbulence Chemistry Interaction
According to Bray [16], there is no a priori reason why a
chemical reaction mechanism for a turbulent ﬂame should be
different from a mechanism for a laminar ﬂame under similar
thermodynamic conditions. Turbulence as well as chemistry in-
volve a broad range of length and timescales. In a turbulent ﬂow,
the largest scales are associated with the geometrical dimensions
while the smallest represent dissipation of turbulent energy by
viscosity [16]. According to Pope [17], the smallest turbulent
timescales are normally not smaller than 1 × 10−4 s. Chemical
scales can comprise a range from 1 × 10−10 s up to over 1 s [18]
and thus can overlap the turbulent timescale range. The intensity
of turbulence chemistry interaction (TCI) is mainly dependent on
this overlap. A direct and complete consideration of the interac-
tion mechanisms can only be achieved by resolving all turbulent
and chemical scales, which is still limited to simple cases due to
the great computational effort [16].
The main inﬂuence of the turbulent ﬂow ﬁeld on chemical
reaction rates is given by the large-scale motions of turbulence.
In the case of non-premixed combustion, zones of fuel-rich and
fuel-lean mixture are formed, while in the case of premixed com-
bustion, turbulent mixing creates zones of cold reactants and hot
products [19]. In both cases, the result is incomplete mixing,
considering that for chemical reactions mixing on a molecular
level is necessary [16]. Therefore, a direct evaluation of reac-
tion rates from the averaged values of species composition and
temperature should always be evaluated with caution. In addi-
tion, in the case of premixed or partially premixed combustion,
the change of the ﬂame surface area due to TCI affects chemical
reaction rates. This effect is known as stretch and is negligible
when diffusive combustion dominates.
The main effect of chemical reaction on the turbulent ﬂow
ﬁeld is due to heat release. The resulting large density gradients
increase vorticity production and thus the intensity of turbulence.
However, heat release also leads to local expansion, which re-
duces vorticity and thus the intensity of turbulence. It can not be
universally stated which of these effects dominates.
In the case of high pressure dual-fuel (HPDF) combustion,
the injection of Diesel and natural gas will lead to temperature
and mixture inhomogeneities in the combustion chamber, which
may inﬂuence the reaction rates. To account for this effect, a re-
action rate multiplier model proposed by Kong et al. [20], based
on the Partially-Stirred Reactor (PaSR) model of Golovitchev
[21], was implemented in CONVERGE. Using this model, the
chemical reaction rates are scaled based on a chemical timescale
and the turbulent mixing time. The chemical timescale is de-
ﬁned as the time, n-heptane, methane or carbon monoxide need
to reach their equilibrium state. The calculation of the turbulent
mixing time is based on the turbulent kinetic energy and its dis-
sipation rate. By applying this model, only the direct inﬂuence
of the turbulent ﬂow ﬁeld on chemistry and not vice versa is con-
sidered.
For a partially premixed setup with gas start of injection
(SOI) 1 ms before Diesel SOI and a ﬁnal compression temper-
ature of 920 K the inﬂuence of the TCI model was found to be
small compared to changes in grid resolution and boundary con-
ditions. The maximum short-term deviation for the integral heat
release rate is less than 7%, while the total burnout is not ef-
fected at all (< 0.1%). For a diffusive setup with gas SOI 1 ms
after Diesel SOI, the changes due to the TCI model are of the
same magnitude.
The observed effect is maybe smaller than expected, but co-
incides with the results predicted by Pomraning et al. [22]. Pom-
3
Copyright © 2018 ASME
Downloaded from asmedigitalcollection.​asme.​org/​ICEF/​proceedings-pdf/​ICEF2018/​51999/​V002T06A008/​2444299/​v002t06a008-icef2018-9579.​pdf by Dalian University Of Technology user on 31 August 2026

<!-- PDF_PAGE: 4 -->

raning showed that for a RANS turbulence model the sub-grid
term of turbulence, resulting from under resolved RANS grids,
is signiﬁcantly more important than TCI. He identiﬁed the grid
resolution and the chemistry model as the most important param-
eters inﬂuencing combustion.
Natural Gas Chemistry
The observation that the TCI model has only little inﬂuence
on combustion originates from the limitation of turbulent mixing
and not by chemical reaction rates. To prove this hypothesis, the
effect of a slower methane chemistry on heat release rate has to
be evaluated. In a perfectly premixed natural gas combustion, the
chemical reaction rates signiﬁcantly inﬂuence the heat release.
However, in the case of mixture-limited combustion, in which
the chemistry is considerably faster than the mixing process, the
chemical reaction rates have no inﬂuence on heat release. This is
the case, for example, in a completely non-premixed combustion
setup. Consequently, if two reaction mechanisms with different
chemical reaction rates for methane show the same heat release
rates, the combustion is limited by the mixing process. Based on
this fact, the idea is to slow the chemical reaction rate of methane
in the reaction mechanism. Thus, a reaction mechanisms has to
be found providing identical chemistry for n-heptane combus-
tion but different chemistry for natural gas combustion. Using
the Chalmers mechanism as reference, a mechanism with slower
methane chemistry is needed. This allows to shift the mixture
limitation boundary towards chemistry limitation.
Rahimi et al. [23] published a mechanism based on a
prior version of the Chalmers mechanism used in this paper.
They combined the Chalmers n-heptane mechanism [24] with
the GRI3.0 mechanism [25] for methane combustion. For
n-heptane/air mixtures it was shown in [2] that ignition delays
are very similar for Chalmers and Rahimi over a wide range of
temperature and equivalence ratio. For methane/air mixtures a
comparison of ignition delays and laminar ﬂame speed is pre-
sented in Fig. 2 and plotted against experimental data. It is
clearly shown that the methane kinetics of the Rahimi mecha-
nism is signiﬁcantly slower compared to the methane kinetics of
the Chalmers mechanism. Ignition delays for methane/air mix-
tures differ about factor four to ﬁve and laminar ﬂame speeds
about factor two. Compared to experimental data, none of the
mechanisms shows an exact match.
Using these two mechanisms without TCI model, it can now
be investigated if a much slower methane chemistry will delay
the combustion process. Therefore, the partially premixed setup
with gas start of injection (SOI) 1ms before Diesel SOI and the
diffusive setup with gas SOI 1 ms after Diesel SOI are investi-
gated for the ﬁnal compression temperatures of 920 K and 780 K.
The results are represented in terms of heat release rates (HRR)
in Fig. 3.
For the high temperature and highly diffusive case (920 K,
800 1000 120010−1
100
101
102
103
Temperature T [K]
Ignition delay τ [ms]
[Huang et al.]
[Hashemi et al.]
Chalmers
Rahimi
0.5 1 1.5 2 2.50
0.05
0.1
0.5
Equivalence ratio Φ [-]
Laminar ﬂame speed sl [m/s]
[Rozen et al.]
Chalmers
Rahimi
FIGURE 2: COMPARISON OF IGNITION DELAYS AND
LAMINAR FLAME SPEEDS FOR CHALMERS AND
RAHIMI MECHANISM. IGNITION DELAYS ARE CAL-
CULATED AT A PRESSURE LEVEL OF 40 BAR AND
FOR EQUIV ALENCE RATIO OF 1.0 AND COMPARED TO
EXPERIMENTAL DATA MEASURED BY HUANG [26] AND
HASHEMI [27]. LAMINAR FLAME SPEEDS ARE CALCU-
LATED AT A PRESSURE LEVEL OF 20 BAR AND FOR AN
INITIAL TEMPERATURE OF 300 K AND COMPARED TO
EXPERIMENTAL DATA MEASURED BY ROZEN [28].
gas +1 ms), the HRR for Chalmers and Rahimi are almost iden-
tical. Also in the partially premixed case (920 K, gas -1 ms),
the HRR show the same behavior. Since the slower chemistry
does not inﬂuence the combustion process, combustion in these
cases is clearly limited by the mixing process. For the low tem-
perature cases the Rahimi mechanism predicts a slightly faster
Diesel ignition than the Chalmers mechanism. Compared to
other n-heptane mechanisms from literature, however, this dif-
ference is negligible. The described small difference leads to
a slightly earlier expansion of the Diesel cloud, which does not
4
Copyright © 2018 ASME
Downloaded from asmedigitalcollection.​asme.​org/​ICEF/​proceedings-pdf/​ICEF2018/​51999/​V002T06A008/​2444299/​v002t06a008-icef2018-9579.​pdf by Dalian University Of Technology user on 31 August 2026

<!-- PDF_PAGE: 5 -->

−2 0 2 4 6
0
1
2
3
Time after TDC t [ms]
HRR [MJ/s]
920K, +1ms
−2 0 2 4 6
Time after TDC t [ms]
920K, -1ms
−2 0 2 4 6
0
1
2
3
Time after TDC t [ms]
HRR [MJ/s]
780K, +1ms
−2 0 2 4 6
Time after TDC t [ms]
780K, -1ms
Chalmers
Rahimi
FIGURE 3: HEAT RELEASE RATES CALCULATED USING
THE CHALMERS AND THE RAHIMI MECHANISM FOR
TWO DIFFERENT TEMPERATURE LEVELS AND TWO
DIFFERENT INJECTION TIMINGS. THE ANGLE α BE-
TWEEN THE JETS IS 10◦.
signiﬁcantly inﬂuence the geometric interaction between gas and
Diesel jet. Compared to the high temperature cases, the degree
of gas premixing has further increased with the same injection
timing due to the considerably longer Diesel ignition delay. De-
spite the additional increase of the premixing degree at the same
gas SOI timing, the ignition timing and the HRR of the gas in the
highly diffuse case (780 K, gas +1 ms) are not affected by the
slower gas chemistry. In order to push the limit of the mixture
limitation further towards chemical limitation, the gas injection
was postponed further towards early (780 K, gas -1 ms). In this
case, the ignition of the gas jet takes slightly longer using the
Rahimi mechanism and the burnout is slower compared to the
Chalmers mechanism. The reason for this observation is that the
slower methane chemistry of the Rahimi mechanism inﬂuences
and limits combustion.
The results of Fig. 3 show that in three of the four inves-
tigated cases combustion is entirely limited by the mixing pro-
cess. The methane chemistry has no signiﬁcant inﬂuence on
HRR when the temperature is high and the degree of premix-
ing is low. Thus, for each temperature level there is a maximum
degree of premixing up to which the HRR can be controlled by
the injection mass ﬂow.
Reaction Mechanism Reduction
This section is motivated by the high computational effort of
detailed chemistry based combustion models compared to clas-
sical combustion models using one- or two-step chemistry. In
the previous section it was shown that the inﬂuence of reaction
kinetics is small for high temperatures, since methane chemistry
is fast compared to the mixing process. As a result, the modeling
accuracy of the methane kinetics can be reduced without penalty.
For n-heptane reaction kinetics Curran et al. [10] described
all important reactions. They found that the oxidation process is
more complex for temperatures below 700 K - 800 K (depend-
ing on pressure and composition), compared to higher temper-
atures. Thus, models for low temperature kinetics involve ad-
ditional species and reactions not needed for high temperature
kinetics modeling. The Chalmers mechanism includes low and
high temperature kinetics and is validated down to 650 K. Con-
sequently, there is a signiﬁcant reduction potential for n-heptane
as well as for methane kinetics. Based on these ﬁndings, a re-
duced mechanism for high temperature combustion is derived
from the Chalmers mechanism in the following paragraph in or-
der to reduce the computational effort.
Mechanism reduction is performed using the direct re-
lation graph with error propagation and sensitivity analysis
(DRGEPSA) method introduced by Niedermayer et al. [29].
DRGEPSA is implemented in the CONVERGE software pack-
age [3]. The reduction is based on ignition delays which are
calculated using homogeneous constant volume reactors under
adiabatic conditions. The maximum reduction potential results
from the maximum permissible deviation of the reduced mecha-
nism from the base mechanism at deﬁned sampling points. Sam-
pling points for temperature are chosen to range from 700 K to
1200 K in steps of 50 K. A lower limit of 700 K is selected be-
cause mixing zones of cold Diesel and natural gas with hot air
can be much colder compared to the ﬁnal compression tempera-
ture. Regarding pressure, three sampling points are speciﬁed in
the range of 40 bar up to 120 bar. Values for equivalence ratio
range from lean (0.4) to rich (2.5) for mixture compositions of
n-heptane/air and methane/air. In addition, a set of target species
is deﬁned. Target species are forced to be part of the reduced
mechanism and thus can not be eliminated during the reduction
process. Apart from fuel and air, CH 3, CH 2O, OH, H 2O and
H2O2 are included in the target species set. Schiffner et al. [12]
found that these species play an important role during the ig-
nition process of n-heptane/methane/air mixtures. To retain the
capability of the base mechanism for CO and NO x prediction,
all relevant species for these sub-mechanisms are included in the
target species list too. The parameters for mechanism reduction
are summarized in Tab. 2.
The reduced mechanism consists of 53 species and 244 reac-
tions. Fig. 4 shows a comparison of ignition delays for the base
mechanism (referred as Chalmers-83 from now on) and the re-
duced mechanism (referred as Chalmers-53). Results are almost
5
Copyright © 2018 ASME
Downloaded from asmedigitalcollection.​asme.​org/​ICEF/​proceedings-pdf/​ICEF2018/​51999/​V002T06A008/​2444299/​v002t06a008-icef2018-9579.​pdf by Dalian University Of Technology user on 31 August 2026

<!-- PDF_PAGE: 6 -->

TABLE 2: SUMMARY OF MECHANISM REDUCTION PA-
RAMETERS.
Parameter Value
Base mechanism name Chalmers-83
Base mechanism
(species/reactions)
83/433
Pressure range (bar) 40, 80, 120
Temperature range (K) 700 - 1200 (in steps of 50)
Equivalence ratio range (-) 0.4, 0.6, 0.8, 1.0, 1.5, 2.0, 2.5
Fuel fraction range
(mn−heptane /mFuel )
0, 0.5, 1
Ignition delay error
tolerance (%)
2
Target species C7H16, CH 4, CH 3, CH 2O,
H2O2, H 2O, OH, CO, CO 2,
N, N2, N2O, NO2, O2, N2
Reduced mechanism name Chalmers-53
Reduced mechanism
(species/reactions)
53/244
identical and the curves overlap. To test the performance of the
reduced mechanism under engine conditions, results of a CFD
calculation using the base mechanism are compared with results
obtained using the reduced mechanism. For the test case, gas
SOI is chosen to be 0.5 ms after Diesel SOI. Final compression
temperature and pressure are at 920 K and 125 bar respectively.
The results for the two mechanisms hardly differ (the difference
is below 1% at all times) and HRR are not shown in this case be-
cause the lines would completely overlap like in ﬁg. 4. Thus, the
Chalmers-83 mechanism can be replaced by the reduced mech-
anism for high temperature and pressure conditions without ex-
pecting signiﬁcant differences. In the case of Chalmers-83, 70%
of the total computing time was spend for the combustion model.
Using the reduced mechanism, this share was reduced and the to-
tal computing time could be reduced by about 35% while keeping
all other simulation parameters constant.
The range of application of the reduced mechanism
(Chalmers-53) covers the thermodynamic conditions of all rel-
evant previous publications, since Diesel like compression ratios
are used in for HPDF concept (e.g. [1, 30–33]). High compres-
sion ratios in combination with slightly premixed or non pre-
mixed natural gas combustion can gain Diesel like efﬁciencies
while keeping hydrocarbon emissions low [30,32,33]. This oper-
800 1000 120010−1
100
101
102
103
104
Temperature T [K]
Ignition delay τ [ms]
Chalmers-83
Chalmers-53
800 1000 120010−2
10−1
100
101
Temperature T [K]
Ignition delay τ [ms]
FIGURE 4: COMP
ARISON OF IGNITION DELAYS FOR
METHANE/AIR (TOP) AND N-HEPTANE/AIR MIXTURES
(BOTTOM) USING CHALMERS-83 AND CHALMERS-53.
IGNITION DELAYS ARE CALCULATED AT A PRESSURE
LEVEL OF 40 BAR AND FOR EQUIV ALENCE RATIO OF
1.0.
ating strategy is in accord with the statement that methane chem-
istry is unimportant when there is no strong premixing.
RESULTS AND DISCUSSION
In this section, the numerical model is used to predict cases
with different level of gas premixing and to investigate the spa-
tial interaction of gas and Diesel jet. Two different operating
points are selected for these investigations. The ﬁrst operating
point is chosen to have a ﬁnal compression temperature of 920 K
and a ﬁnal compression pressure of 125 bar (high temperature
case). The conditions represent a mid or full load engine operat-
ing point. Based on the results shown in the previous chapter, the
prediction quality is not expected to change at even higher tem-
6
Copyright © 2018 ASME
Downloaded from asmedigitalcollection.​asme.​org/​ICEF/​proceedings-pdf/​ICEF2018/​51999/​V002T06A008/​2444299/​v002t06a008-icef2018-9579.​pdf by Dalian University Of Technology user on 31 August 2026

<!-- PDF_PAGE: 7 -->

peratures and/or pressures. This means, if the model performs
well at the high temperature case, it is also expected to perform
well even at, for example, 1000 K. A second operating point is
chosen to have a ﬁnal compression temperature of 780 K and a ﬁ-
nal compression pressure of 125 bar (low temperature case). The
conditions represent a low load engine operating point or the low
temperature operating condition characteristic for Miller cycles.
In order to change the degree of premixing, the temporal
variation of gas start of injection (SOI) is between -1.5 ms and
+1.5 ms relative to Diesel SOI. The jet interaction is investigated
using an impinging jet conﬁguration with an angle α = −20◦
between the jets. Experimental results published by Fink et al.
( [14] and [15]) are used for validation of the computational re-
sults.
Prediction of combustion at different gas mixing states
In order to change the characteristics of HRR, which is nec-
essary to meet emission limits and to optimize engine efﬁciency
at different engine load levels, the level of premixing of gas can
be varied. To limit the number of possible variations, Diesel SOI
is kept constant relative to top dead center (TDC), while gas SOI
is varied in order to change the level of premixing before igni-
tion. This strategy ensures constant conditions for Diesel ignition
in all different cases. All variations for the high and the low tem-
perature case are performed with an angle α of +10◦ between
the jets.
Fig. 5a shows the predicted HRR for gas SOI 1.5 ms and
0.5 ms before and 0.5 ms and 1.5 ms after Diesel SOI for the high
temperature case. Chalmers-53 was used to perform these simu-
lations. The Diesel ignition characteristic is nearly constant for
all cases. Small deviations mainly result from pressure and tem-
perature ﬂuctuations from case to case at TDC which are within
±2 bar and ±4 K. For high levels of premixing, the Diesel igni-
tion determines the start of gas combustion and an earlier gas SOI
does not cause a shift of the start of heat release. The level of pre-
mixing determines the height and width of the premix peak but
does not signiﬁcantly affect the rate of pressure rise. The burnout
can be directly correlated to the gas SOI relative to Diesel SOI.
A qualitative and quantitative comparison between predicted and
measured HRR (Fig. 5b) in general shows good agreement. It is
worth mentioning that the case with the lowest degree of premix-
ing shows the least quantitative agreement. Since it was shown
in the previous chapter that in this case the combustion is lim-
ited by mixing, this is probably due to the quality of the mixture
between gas and air.
Fig. 6a shows the predicted HRR for gas SOI 1.5 ms and
0.5 ms before and 0.5 ms and 1.5 ms after Diesel SOI for the
low temperature case. Chalmers-83 was used to perform these
simulations. As shown in the section on the general characteri-
zation of the combustion process, predicting combustion is more
challenging the lower the temperature levels are. In contrast to
−2 0 2 4 6 8 10
0
1
2
3
Time after TDC t [ms]
HRR [MJ/s]
-1.5 ms
-0.5 ms
+0.5 ms
+1.5 ms
(a) CFD calculations
−2 0 2 4 6 8 10
0
1
2
3
Time after TDC
t [ms]
HRR [MJ/s]
(b) RCEM measurements
FIGURE 5
: NUMERICAL PREDICTION OF HRR FOR
GAS SOI 1.5 MS AND 0.5 MS BEFORE AND 0.5 MS AND
1.5 MS AFTER DIESEL SOI (a) IN COMPARISON WITH EX-
PERIMENTAL HRR OBTAINED FROM PRESSURE TRACE
ANALYSIS (b). FINAL COMPRESSION CONDITIONS ARE
920 K AND 125 BAR. THE ANGLE α BETWEEN THE JETS
IS 10◦.
mainly mixing driven combustion in the high temperature case,
chemistry is gaining in importance in this case. The Diesel ig-
nition characteristic is again nearly constant for all considered
cases. Compared to the high temperature case, the peak of Diesel
HRR (ﬁrst sharp peak) is much higher now. This is due to longer
ignition delay times for Diesel at low temperatures and thus due
to more time to mix with air. The change in shape of the main
HRR follows the same behavior as in the high temperature case,
however, the rate of pressure rise is smaller. A qualitative and
quantitative comparison between predicted and measured HRR
7
Copyright © 2018 ASME
Downloaded from asmedigitalcollection.​asme.​org/​ICEF/​proceedings-pdf/​ICEF2018/​51999/​V002T06A008/​2444299/​v002t06a008-icef2018-9579.​pdf by Dalian University Of Technology user on 31 August 2026

<!-- PDF_PAGE: 8 -->

−2 0 2 4 6 8 10
0
1
2
3
Time after TDC t [ms]
HRR [MJ/s]
-1.5 ms
-0.5 ms
+0.5 ms
+1.5 ms
(a) CFD calculations
−2 0 2 4 6 8 10
0
1
2
3
Time after TDC t [ms]
HRR [MJ/s]
(b) RCEM measurements
FIGURE 6
: NUMERICAL PREDICTION OF HRR FOR
GAS SOI 1.5 MS AND 0.5 MS BEFORE AND 0.5 MS AND
1.5 MS AFTER DIESEL SOI (a) IN COMPARISON WITH EX-
PERIMENTAL HRR OBTAINED FROM PRESSURE TRACE
ANALYSIS (b). FINAL COMPRESSION CONDITIONS ARE
780 K AND 75 BAR. THE ANGLE α BETWEEN THE JETS
IS 10◦.
(Fig. 6b) shows good agreement again. The sharp peak dur-
ing Diesel combustion can not be captured by the pressure trace
analysis.
Finally, a qualitative comparison of the results between the
high and low temperature cases is presented. The quality of the
prediction is identical for cases. The timing of gas ignition is
well predicted in all cases. This primarily indicates a good pre-
diction of the spatial interaction of the jets and the mixing state.
Considering in addition the ﬁndings from the section of natu-
ral gas chemistry, too slow methane kinetics would delay the
heat release for low temperature cases with early gas injection.
Since this is not the case, it seems that the methane kinetics in
Chalmers-83 mechanism can reproduce the reality well even in
cases where chemistry limits combustion.
Prediction of gas and Diesel jet interaction
In addition to the variations in mixing state shown in the
previous section, Fink et al. [14, 15] investigated a variation of
geometrical arrangements of gas and Diesel jet. For the geomet-
rical variation, the origin of gas and Diesel jet was held constant
while the angle α between the jets was varied between+20◦ and
−30◦ (Fig. 1). The main experimental results of this study can be
summarized as follows: in the high temperature case, Diesel ig-
nition occurs for all investigated cases withα between +20◦ and
−30◦, no matter what timing is chosen between gas and Diesel
SOI. Low temperature cases show the same behavior in case of
diverging jets (α > 0◦). In case of crossing jets ( α < 0◦) how-
ever, Diesel ignition and main combustion occur only if Diesel
injection starts before gas injection. Thus, a region in which ig-
nition is not possible was experimentally found.
To study the reasons for misﬁring in case of Diesel SOI af-
ter gas SOI and crossing jets, an arrangement of the jets with
α = −20◦ and gas SOI 1 ms before Diesel SOI is chosen and
numerically investigated for the high and the low temperature
case. For the high temperature case the Chalmers-53 and for
the low tempreature case the Chalmers-83 mechanism is used.
Fig. 7 shows the jet interaction for both cases at two different
states for each case. The ﬁrst state represents the ﬁrst stage ig-
nition, while the second state represents the main ignition. For
each state, the distribution of hydrogen peroxide mass fraction
(yH2O2) and the density ﬁeld in a slice parallel to the ﬂat pis-
ton are shown. They are compared to a superposition of OH*
and shadowgraph (SG) measurements. The hydrogen peroxide
distribution is scaled from 0.00 to 0.01 for all cases and states,
while the color map of the density distribution is scaled relative
to the background density (ref) at Diesel SOI. In the hydrogen
peroxide distribution as well as in the density distribution con-
tours indicate the mass fraction of 1% Diesel and 1% methane.
The density ﬁeld has been selected for plotting in order to show
the mixing between fuel and air as well as to show strong tem-
perature changes during the ignition process.
The ﬁrst state shows the ﬁrst stage ignition of Diesel in both
cases. Schiffner et al. [12] demonstrated that a massive hydro-
gen peroxide pool is formed during ﬁrst stage ignition of Diesel.
They also showed that this pool decreases with increasing substi-
tution of Diesel by methane. As a result, the ignition process is
delayed. The high temperature case at the time of ﬁrst stage ig-
nition at the top of Fig. 7 shows that the hydrogen peroxide pool
is only formed in the region of pure Diesel/air mixtures even if
Diesel is already mixed into the gas jet. In the low temperature
case the hydrogen peroxide concentration is much lower com-
8
Copyright © 2018 ASME
Downloaded from asmedigitalcollection.​asme.​org/​ICEF/​proceedings-pdf/​ICEF2018/​51999/​V002T06A008/​2444299/​v002t06a008-icef2018-9579.​pdf by Dalian University Of Technology user on 31 August 2026

<!-- PDF_PAGE: 9 -->

yH2O2 density
0.00 ref+y 0.01 ref ref-x
SG
OH*
second stateﬁrst state ﬁrst statesecond state
low temperature high temperature
20
◦
FIGURE 7: INTERA
CTION OF GAS AND DIESEL JET AT TWO DIFFERENT STATES FOR A HIGH AND A LOW TEMPERA-
TURE CASE. FROM LEFT TO RIGHT ARE SHOWN THE DISTRIBUTION OF HYDROGEN PEROXIDE, THE DENSITY DIS-
TRIBUTION AND A SUPERPOSITION OF OH* AND SHADOWGRAPH (SG) MEASUREMENTS.
pared to the high temperature case. Nevertheless, a part of the
Diesel fuel is in the ﬁrst stage ignition state as well, since prior
to the ﬁrst temperature rise no hydrogen peroxide is produced.
In this state no OH* signal is detected by the measurement sys-
tem in both cases since OH production starts at main ignition
only [12]. The temperature rise during this state does not result
in a signiﬁcant density change.
If the temperature rise during ﬁrst stage ignition is strong
enough, a second rapid and much stronger temperature rise fol-
lows after a delay time. This process is referred as main ignition
or just ignition. The strong temperature rise is initiated by the
consumption of hydrogen peroxide. OH radicals are formed dur-
ing this process. Having a look at the second state of the high
temperature case, this process can clearly be observed. The hy-
drogen peroxide pool has strongly decreased compared to the
ﬁrst state while OH* is detected by the measurement system in
the corresponding region and in the ignited region of the gas jet.
A strong density reduction can be observed caused by locally
9
Copyright © 2018 ASME
Downloaded from asmedigitalcollection.​asme.​org/​ICEF/​proceedings-pdf/​ICEF2018/​51999/​V002T06A008/​2444299/​v002t06a008-icef2018-9579.​pdf by Dalian University Of Technology user on 31 August 2026

<!-- PDF_PAGE: 10 -->

high ﬂame temperatures. At the second state of the low tem-
perature case, the already small hydrogen peroxide pool has de-
creased only slightly compared to the ﬁrst state. This decrease
is mainly caused by convection and diffusion but not by con-
sumption. That is why there is no temperature rise and no main
ignition in the second state. Obviously, the temperature rise dur-
ing ﬁrst stage ignition was not strong enough to ignite the Diesel
fuel.
Finally the question arises, why only in the case of crossing
jets and late Diesel injection no ignition occurs. A ﬁrst expla-
nation can be found in [34]. The authors showed that at ﬁxed
injection duration Diesel ignition starts at the core of the Diesel
jet in case of low temperature levels, while it starts in the shear
layer at high temperature levels. In addition, at high tempera-
ture levels ignition starts closer to the injector and thus the lift
off length is much shorter. This is due to wider self ignition and
burning limits at higher temperatures for a given mixture. In im-
pinging jet conﬁgurations and at low temperatures, the preferred
ignition range of the Diesel jet is therefore covered by the gas jet
and can no longer contribute to ignition.
The reliable prediction of ignition and misﬁring by the nu-
merical model conﬁrms the good performance of the mixing
model and the reaction mechanism. This is very important for
future investigations of multi hole injectors.
SUMMARY AND CONCLUSIONS
A numerical model previously developed by the authors was
extended for investigations of the combustion process in a dual-
fuel engine application:
• The existing model was extended by a reaction rate multi-
plier model to take into account TCI effects. It has been
shown that this model has no signiﬁcant inﬂuence on the
combustion process, neither for partially premixed, nor for
diffusive methane combustion. This indicated the limitation
of combustion by turbulent mixing in the studied cases.
• As a consequence, two different reaction mechanisms have
been used to study a high and a low temperature case in
terms of combustion limitation by mixing or chemistry. The
Chalmers and the Rahimi reaction mechanism show similar
results for n-Heptane combustion but totally different behav-
ior for methane combustion. It could be shown that depend-
ing on temperature and degree of premixing there is a limit at
which mixture limited combustion turns into predominantly
chemically limited combustion.
• As a result of these ﬁndings it can be concluded that a pre-
cise prediction of the complex chemistry is unimportant for
high temperatures. Therefore, a reduced mechanism was de-
rived from the Chalmers mechanism, which leads to 35%
reduction in computation time for high temperature cases.
The second part of the study was focused on the prediction ca-
pability of the model. For veriﬁcation, experimental results from
the RCEM were used:
• For different gas start of injection (SOI) timings relative to
Diesel SOI the model was able to predict Diesel and gas
ignition well. The change in shape of HRR as well as the
burnout characteristics match with experimental results. In
addition, the prediction quality was found to be independent
of the ﬁnal compression temperature level.
• Misﬁring in case of low temperature levels and crossing jets
was predicted and analyzed numerically. The reason for
misﬁring is that the temperature rise by the ﬁrst stage ig-
nition of the Diesel is not sufﬁcient to dissociate the hydro-
gen peroxide radicals and thus to ignite the mixture. This
is because the preferred ignition region of the Diesel at low
temperatures is covered by the gas jet.
The numerical model has performed excellently when applied to
ﬂexible dual-fuel combustion systems based on direct gas injec-
tion. It will be used in the future to investigate different levels
of premixing, different main fuels and to better understand the
combustion process. It can be further used to investigate different
dual-fuel multi hole injector conﬁgurations. Since the model is
based on detailed chemistry calculations, it has the additional ca-
pability for the prediction of emissions (e.g. NOx, CO2, CH4,...).
ACKNOWLEDGMENT
This research has been funded by the Federal Ministry of
Economics and Technology of Germany in the framework of
Maritime Technologien der n ¨achsten Generation. The project
was carried out in collaboration with L’Orange GmbH and MTU
Friedrichtshafen GmbH, which is gratefully acknowledged.
REFERENCES
[1] Zoldak, P., Sobiesiak, A., Wickman, D., and Bergin, M.,
2015. “Combustion Simulation of Dual Fuel CNG Engine
Using Direct Injection of Natural Gas and Diesel”. SAE
International Journal of Engines, 8(2), pp. 846–858.
[2] Jud, M., Fink, G., and Sattelmayer, T., 2017. “Predict-
ing Ignition and Combustion of a Pilot Ignited Natural Gas
Jet Using Numerical Simulation Based on Detailed Chem-
istry”. In ASME 2017 Internal Combustion Engine Divi-
sion Fall Technical Conference.
[3] Richards, K. J., Senecal, P. K., and Pomraning, E., 2016.
CONVERGE (v2.3) Manual.
[4] Yakhot, V ., and Orszag, S. A., 1986. “Renormalization
Group Analysis of Turbulence. I. Basic Theory”. Journal
of Scientiﬁc Computing, 1(1), pp. 3–51.
[5] Redlich, O., and Kwong, J. N. S., 1949. “On the Thermody-
namics of Solutions. V . An Equation of State. Fugacities of
10
Copyright © 2018 ASME
Downloaded from asmedigitalcollection.​asme.​org/​ICEF/​proceedings-pdf/​ICEF2018/​51999/​V002T06A008/​2444299/​v002t06a008-icef2018-9579.​pdf by Dalian University Of Technology user on 31 August 2026

<!-- PDF_PAGE: 11 -->

Gaseous Solutions”. Chemical Reviews, 44(1), pp. 233–
244.
[6] Reitz, R. D., and Diwakar, R., 1987. “Structure of High-
Pressure Fuel Sprays”. In SAE International Congress and
Exposition, SAE Technical Paper Series.
[7] Reitz, R. D., and Beale, J. C., 1999. “Modelling Spray At-
omization with the Kelvin-Helmholtz/Rayleigh-Taylor Hy-
brid Model”. Atomization and Sprays, 9(6), pp. 623–650.
[8] Schmidt, D. P., and Rutland, C. J., 2000. “A New Droplet
Collision Algorithm”. Journal of Computational Physics,
164(1), pp. 62–80.
[9] Hindmarsh, A. C., Brown, P. N., Grant, K. E., Lee,
S. L., Serban, R., Shumaker, D. E., and Woodward, C. S.,
2005. “SUNDIALS: Suite of Nonlinear and Differen-
tial/Algebraic Equation Solvers”. ACM Transactions on
Mathematical Software, 31(3), pp. 363–396.
[10] Curran, H. J., Gaffuri, P., Pitz, W. J., and Westbrook, C. K.,
1998. “A Comprehensive Modeling Study of n-Heptane
Oxidation”. Combustion and Flame, 114(1-2), pp. 149–
177.
[11] Aggarwal, S. K., Awomolo, O., and Akber, K., 2011. “Ig-
nition Characteristics of Heptane–Hydrogen and Heptane–
Methane Fuel Blends at Elevated Pressures”. International
Journal of Hydrogen Energy, 36(23), pp. 15392–15402.
[12] Schiffner, M., Grochowina, M., and Sattelmayer, T., 2017.
“Development of a Numerical Model for Ignition Phenom-
ena in a Micro Pilot Ignited Dual Fuel Engine With External
Mixture Formation”. In ASME 2017 Internal Combustion
Engine Division Fall Technical Conference.
[13] Tao, F., Reitz, R. D., and Foster, D. E., 2007. “Revisit
of Diesel Reference Fuel (n-Heptane) Mechanism Applied
to Multidimensional Diesel Ignition and Combustion Sim-
ulations”. In Seventeenth International Multidimensional
Engine Modeling User’s Group Meeting, SAE Technical
Paper Series.
[14] Fink, G., Jud, M., and Sattelmayer, T., 2017. “Inﬂuence of
the Spatial and Temporal Interaction Between Diesel Pilot
and Directly Injected Natural Gas Jet on Ignition and Com-
bustion Characteristics”. Journal of Engineering for Gas
Turbines and Power, 139(18):1096.
[15] Fink, G., Jud, M., and Sattelmayer, T., 2018. “Fundamental
Study of Diesel-Piloted Natural Gas Direct Iinjection under
Different Operating Conditions”. In ASME 2018 Internal
Combustion Engine Division Fall Technical Conference.
[16] Bray, K., 1996. “The challenge of turbulent combustion”.
Symposium (International) on Combustion, 26(1), pp. 1–
26.
[17] Pope, S. B., 1997. “Computationally efﬁcient implementa-
tion of combustion chemistry using in situ adaptive tabula-
tion”. Combustion Theory and Modelling, 1(1), pp. 41–63.
[18] Warnatz, J., Maas, U., and Dibble, R. W., 1999. Com-
bustion: Physical and Chemical Fundamentals, Modeling
and Simulation, Experiments, Pollutant Formation, second
edition ed. Springer Berlin Heidelberg, Berlin, Heidelberg.
[19] Veynante, D., and Vervisch, L., 2002. “Turbulent combus-
tion modeling”. Progress in Energy and Combustion Sci-
ence, 28(3), pp. 193–266.
[20] Kong, S.-C., Marriott, C. D., Reitz, R. D., and Christensen,
M., 2001. “Modeling and Experiments of HCCI Engine
Combustion Using Detailed Chemical Kinetics with Multi-
dimensional CFD”. In SAE 2001 World Congress, SAE
Technical Paper Series, SAE International400 Common-
wealth Drive, Warrendale, PA, United States.
[21] Golovitchev, V . I., Nordin, N., Jarnicki, R., and Chomiak,
J., 2000. “3-D Diesel Spray Simulations Using a New
Detailed Chemistry Turbulent Combustion Model”. In
CEC/SAE Spring Fuels & Lubricants Meeting & Exposi-
tion, SAE Technical Paper Series, SAE International400
Commonwealth Drive, Warrendale, PA, United States.
[22] Pomraning, E., Richards, K., and Senecal, P. K., 2014.
“Modeling Turbulent Combustion Using a RANS Model,
Detailed Chemistry, and Adaptive Mesh Reﬁnement”. In
SAE 2014 World Congress & Exhibition, SAE Technical
Paper Series, SAE International400 Commonwealth Drive,
Warrendale, PA, United States.
[23] Rahimi, A., Fatehifar, E., and Saray, R. K., 2010. “De-
velopment of an Optimized Chemical Kinetic Mechanism
for Homogeneous Charge Compression Ignition Combus-
tion of a Fuel Blend of n-Heptane and Natural Gas Using
a Genetic Algorithm”. Proceedings of the Institution of
Mechanical Engineers, Part D: Journal of Automobile En-
gineering, 224(9), pp. 1141–1159.
[24] Tao, F., Golovitchev, V . I., and Chomiak, J., 2000.
“Self-Ignition and Early Combustion Process of n-Heptane
Sprays Under Diluted Air Conditions: Numerical Studies
Based on Detailed Chemistry”. In International Fuels &
Lubricants Meeting & Exposition, SAE Technical Paper
Series, SAE International400 Commonwealth Drive, War-
rendale, PA, United States.
[25] Smith, G. P., Golden, D. M., Frenklach, M., Moriarty,
N. W., Eiteneer, B., Goldenberg, M., Bowman, C. T., Han-
son, R. K., Song, S., Gardiner, Jr., William C., Lissianski,
V . V ., and Qin, Z.
[26] Huang, J., Hill, P. G., Bushe, W. K., and Munshi, S. R.,
2004. “Shock-Tube Study of Methane Ignition Under
Engine-Relevant Conditions: Experiments and modeling”.
Combustion and Flame, 136(1-2), pp. 25–42.
[27] Hashemi, H., Christensen, J. M., Gersen, S., Levinsky, H.,
Klippenstein, S. J., and Glarborg, P., 2016. “High-Pressure
Oxidation of Methane”. Combustion and Flame, 172,
pp. 349–364.
[28] Rozenchan, G., Zhu, D. L., Law, C. K., and Tse, S. D.,
2002. “Outward propagation, burning velocities, and chem-
ical effects of methane ﬂames up to 60 ATM”. Proceedings
11
Copyright © 2018 ASME
Downloaded from asmedigitalcollection.​asme.​org/​ICEF/​proceedings-pdf/​ICEF2018/​51999/​V002T06A008/​2444299/​v002t06a008-icef2018-9579.​pdf by Dalian University Of Technology user on 31 August 2026

<!-- PDF_PAGE: 12 -->

of the Combustion Institute, 29(2), pp. 1461–1470.
[29] Niemeyer, K. E., Sung, C.-J., and Raju, M. P., 2010.
“Skeletal mechanism generation for surrogate fuels using
directed relation graph with error propagation and sensitiv-
ity analysis”. Combustion and Flame, 157(9), pp. 1760–
1770.
[30] McTaggart-Cowan, G. P., Jones, H. L., Rogak, S. N.,
Bushe, W. K., Hill, P. G., and Munshi, S. R., 2007.
“The Effects of High-Pressure Injection on a Compression–
Ignition, Direct Injection of Natural Gas Engine”. Journal
of Engineering for Gas Turbines and Power, 129(2), p. 579.
[31] McTaggart-Cowan, G., Mann, K., Huang, J., Singh, A.,
Patychuk, B., Zheng, Z. X., and Munshi, S., 2015. “Di-
rect Injection of Natural Gas at up to 600 Bar in a Pilot-
Ignited Heavy-Duty Engine”. SAE International Journal
of Engines, 8(3).
[32] Faghani, E., Kheirkhah, P., Mabson, C. W., McTaggart-
Cowan, G., Kirchen, P., and Rogak, S., 2017. “Effect
of Injection Strategies on Emissions from a Pilot-Ignited
Direct-Injection Natural-Gas Engine- Part I: Late Post In-
jection”. In WCXTM 17: SAE World Congress Experience,
SAE Technical Paper Series, SAE International400 Com-
monwealth Drive, Warrendale, PA, United States.
[33] Faghani, E., Kheirkhah, P., Mabson, C. W., McTaggart-
Cowan, G., Kirchen, P., and Rogak, S., 2017. “Effect of In-
jection Strategies on Emissions from a Pilot-Ignited Direct-
Injection Natural-Gas Engine- Part II: Slightly Premixed
Combustion”. In WCX TM 17: SAE World Congress Expe-
rience, SAE Technical Paper Series, SAE International400
Commonwealth Drive, Warrendale, PA, United States.
[34] Schiffner, M., Jud, M., and Sattelmayer, T., 2017. “Re-
action Kinetics Analysis of Dual Fuel Internal Combus-
tion Engines Based on Ignition Delay Times Using n-
Heptane/Methane Fuel Blends”. In Proceedings of the Eu-
ropean Combustion Meetning.
12
Copyright © 2018 ASME
Downloaded from asmedigitalcollection.​asme.​org/​ICEF/​proceedings-pdf/​ICEF2018/​51999/​V002T06A008/​2444299/​v002t06a008-icef2018-9579.​pdf by Dalian University Of Technology user on 31 August 2026
