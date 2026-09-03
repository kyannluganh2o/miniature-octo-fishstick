<!-- PDF_PAGE: 1 -->

Investigations of diesel and natural gas injection interaction on combustion 
characteristics of a high-pressure direct-injection dual-fuel engine based on 
large eddy simulation
Zifan Lian
a
, Wei Li
b
, Yanbin Cai
c
, Houchang Chen
a
, Junxin Jiang
a
, Guoxiang Li
a
,  
Feiyang Zhao
a , *
, Wenbin Yu
a , *
a
School of energy and power engineering, Shandong University, Jinan, China
b
State Key Laboratory of Engine and Powertrain System, Weichai Power Co., Ltd., Weifang 261061, China
c
Weichai Lovol Intelligent Agricultural Technology CO., LTD, Weifang, China
HIGHLIGHTS
• DMD algorithm was introduced to study the flow field structure induced by diesel and natural gas jet in HPDI engine.
• The chemical kinetics of CH
4
/air ignition with additions of OH was elucidated by reaction pathway analysis.
• The synergies of vortex mixing and chemical reaction on the ignition of low reactivity natural gas is elucidated.
ARTICLE INFO
Keywords:
Natural gas jet
Flow field structure
Combustion and emission
Dual fuel diesel engine
ABSTRACT
HPDI (high-pressure direct-injection) with pilot ignition is modern technology developed for heavy-duty natural 
gas engines. The dynamics of coherent flow structures due to diesel and natural gas jet play a significant role on 
ignition characteristics. In this study, a large eddy simulation (LES) framework coupled with chemistry solver is 
conducted for three-dimensional modelling of the thermal process of a HPDI engine. By integrating the Dynamic 
Mode Decomposition (DMD) algorithm, the break-up and attenuation process of unstable flow structures 
accompanied by different scale vortex formation and dissipation is able to be effectively demonstrated from fuel 
jet. The prime in-cylinder flow field structures from natural gas injection to its ignition is characterized by the 
vortex entrainment phenomenon resulting from the impingement between the natural gas jet and active products 
from diesel combustion. This phenomenon leads to enhanced heat transfer and exchange of active radicals by 
which the ignition of the natural gas is therefore facilitated, especially when angle β (the intersection angle 
between diesel and nature gas jet) is decreased. Moreover, the present study extends the ability of reaction-rate 
based global pathway analysis to evaluate the reactivity of OH additions to CH
4
/air mixture. In summary, the 
interactive dual fuel turbulent combustion process of the HPDI engine is theoretically elucidated, wherein the 
synergetic kinetics of vortex entrainment-mixing and chemical reaction facilitate the ignition of low reactivity 
natural gas.
1. Introduction
With the increasing concern on the depletion of fossil fuels and 
environmental issues, the adoption of diesel/natural gas dual-fuel mode 
is a promising way for traditional compression ignition (CI) engines to 
comply with the increasingly stringent emission regulations and reduce 
fossil fuels dependence [ 1 , 2 ]. Currently, the diesel/natural gas dual-fuel 
engines are classified as the low-pressure gas engines with the tech -
nology of intake port injection or the natural gas high-pressure direct 
injection (HPDI) engines according to the fuel injection pressure [ 3 ]. 
Although low-pressure injection dual-fuel engines with approximately 5 
% share of diesel energy offer lower NOx and soot emissions, the engine 
load expansion capability is limited due to knock issues, meanwhile 
particular attention is still paid to the high HC emissions at low loads 
* Corresponding authors.
E-mail addresses: fyzhao@sdu.edu.cn (F. Zhao), wbyu@sdu.edu.cn (W. Yu). 
Contents lists available at ScienceDirect
Applied Energy
journal homepag e: www.else vier.com/loc ate/apene rgy
https://doi.org/10.1016/j.apenergy.2024.124807
Received 10 February 2024; Received in revised form 20 September 2024; Accepted 27 October 2024  
Applied Energy 378 (2025) 124807 
Available online 4 November 2024 
0306-2619/© 2024 Elsevier Ltd. All rights are reserved, including those for text and data mining, AI training, and similar technologies.

<!-- PDF_PAGE: 2 -->

[ 4 ]. By comparison, the technical scheme of a HPDI engine involves 
using a concentric biaxial needle injector that injects diesel into the 
cylinder at the late stage of compression stroke to form an ignition 
source, followed by high-pressure natural gas that ignites combustion 
within this flame core formed by diesel. Due to the advantage of in- 
cylinder natural gas direct injection technology, combustion within a 
HPDI engine primarily occurs through diffusion combustion, which 
enables engine to adapt well to larger compression ratios and overcome 
knock issue and low volumetric efficiency, while maintaining similar 
thermal efficiency and power output as diesel engines of comparable 
size [ 5 ]. Therefore, the HPDI engines are considered to be the most 
competitive natural gas engines at present.
The impact of fuel injection strategy on the performance and emis -
sion characteristics of HPDI engines has garnered significant attention 
from researchers in recent years. Zhang Q et al. [ 6 ] studied the influence 
of the fuel injection modulation on knocking behaviors of a pilot ignited 
direct injection natural gas engine. It was revealed that retarded diesel 
injection timing or advanced natural gas timing along with increased 
fuel injection pressure could result in higher knock intensity. Mean -
while, the cycle to cycle variation of the brake mean effective pressure 
was aggravated with earlier fuel injection timing. Khosravi M et al. [ 7 ] 
experimentally investigated the formation and oxidation of the soot 
exhausts from a HPDI engine using both the high-speed two-color py -
rometry and the OH* chemiluminescence imaging. It was indicated that 
the peak of apparent heat release rate was basically related with the 
onset of detectable soot formation, while the peak of soot concentration 
and the end of injection timing for natural gas were also highly corre -
lated. It was noteworthy that the injection interval between the diesel 
and the natural gas was able to affect the peak of apparent heat release 
rate and soot concentration by regulating the premixed intensity of the 
natural gas. Rochussen J et al. [ 8 ] analyzed the combustion process of a 
HPDI engine based on a single-cylinder optical engine and it was found 
that the combustion processes went through five typical stages: diesel 
auto-ignition, natural gas ignition, partially premixed combustion of 
natural gas, non-premixed combustion, and late cycle oxidation. In 
addition, the ignition of natural gas was more sensitive to the injection 
interval between diesel and natural gas than injection pressure. 
Recently, the homogenous charge direct injection (HCDI) strategy was 
investigated experimentally in a pilot ignition direct injection natural 
gas engine by Li M et al. [ 9 ]. This HCDI strategy involves two natural gas 
injections, with the first occurring prior to pilot diesel injection and the 
second following it. The results indicate that at low loads, this strategy 
led to increased NOx, CO, and HC emissions while providing modest 
improvement on soot emission and thermal efficiency. At high loads, 
this strategy exhibited significant improvements in CO and soot emis -
sions as well as greatly improved thermal efficiency despite increases in 
NOx and HC emissions.
In recent years, with the significant progress in the combustion 
microscopic kinetic reaction, complex reaction mechanism and numer -
ical simulation of turbulent combustion, the research methods for 
combustion modes of Internal Combustion Engines (ICEs) are gradually 
enriched, among which Computational Fluid Dynamics (CFD) is an 
efficient method to study the combustion characteristics. So far, the 
numerical studies of the HPDI engines are absorbed in the optimization 
of injection parameters and the synergetic combustion characteristics of 
diesel/natural gas. CFD code KIVA-3 V coupled with multi-objective 
genetic algorithm NSGA-II was utilized to optimize the injection strat -
egy of a HPDI engine by Liu J et al. [ 10 ]. It was presented that an 
adoption of diesel injection timing at   15.2 
◦
CA After Top Dead Center 
(ATDC) and natural gas injection timing at   6.0 
◦
CA ATDC combined 
with the nozzle hole circumferential deviation angle of 8.8
◦
could 
decrease NOx and soot emissions simultaneously. Li M et al. [ 11 ] studied 
the effects of N-butanol addition, natural gas post injection, and Exhaust 
Gas Recirculation (EGR) to the diesel natural gas direct injection engine. 
It was reported that the diesel mixed with N-butanol was favorable to 
improve thermal efficiency by 2.3 % and 6.5 % at low and medium 
loads, respectively. Moreover, the natural gas post injection combined 
with moderate EGR rate was able to decrease CO, NOx, and soot emis -
sions. The synergetic effects of EGR rate and diesel quality on combus -
tion and emission for a HPDI engine were numerically investigated by 
Yu S et al. [ 12 ], and it was illustrated that the increasing of EGR rate was 
capable to smooth the peak combustion pressure, improve indicated 
thermal efficiency with acceptable NOx emission when the amount of 
diesel was constant. To further investigate the underlying combustion 
mechanism induced by the advantage of HPDI engines, many re -
searchers have carried out the numerical studies to discover the 
fundamental reaction kinetics on diesel /naturel gas mixtures. Zhou L 
et al. [ 13 ] employed a large eddy simulation (LES) model coupled with a 
detailed chemical kinetics solver to study the ignited process and flame 
stability in a HPDI engine. When the injection duration of natural gas 
(CH
4
) was prolonged, more activated radicals were generated, among 
which CH
3 
was the improver to facilitate the chain reaction of CH
4 
high- 
temperature reaction. Li J et al. [ 14 ] evaluated the effect of mixture 
stratification on the n-heptane/methane mixtures combustion process 
under HPDI conditions. It was revealed that H + CH
4 
= CH
3 
+ H
2 
and 
OH + CH
4 
= CH
3 
+ H
2
O were the main consumption reactions of CH
4
, 
and the representative exothermic reaction was CH
3 
+ O2 = CH
3
O
2 
at 
low heat release region. Furthermore, with an advanced methane in -
jection timing, the reaction paths of CH
2
, CH
2
O, and HCO were signif -
icant changed through premixed-combustion to the mixing-controlled 
combustion.
As summarized above, in the field of diesel/natural duel fuel engine, 
most of previous studies focus on the fuel injection strategy and diesel/ 
natural gas mixtures combustion kinetics, research regarding to the 
interaction mechanism between diesel and direct natural gas jet is still 
rare. Nemati A et al. [ 15 ] numerically studied the interaction between 
diesel and methane flame jet in a two-stroke dual-fuel marine engine. 
According to their results, increased penetration of methane jet was 
conducive to CH
4
/air mixing, so as to improve combustion intensity at 
low engine load. Fink G et al. [ 16 ] investigated the influence of spatial 
and temporal interaction between diesel pilot and directly injected 
natural gas jet on ignition and combustion characteristics in a rapid 
compression expansion machine. A strong interaction led to the retarded 
ignition of diesel even caused misfire, meanwhile the ignition delay of 
natural gas significantly affected the heat release rate. It was obvious to 
see that the interaction between diesel and natural gas jet has marked 
impact on ignition delay and heat release rate. Therefore, it is essential 
to clarify the effect of the transient flow field structure induced by diesel 
and natural gas jet on HPDI engine combustion characteristics in deep. 
The dynamics of coherent flow structures has a significant impact on the 
mixing of the fuel and the oxidizer.
As an effective flow field analysis theory, the Dynamic Mode 
Decomposition (DMD) algorithm decomposes the transient flow field 
into discrete dynamic modes according to the frequency, and then ex -
tracts the flow field structure and dynamics corresponding to different 
frequency modes [ 17 ]. Sakowitz A et al. [ 18 ] successfully investigated 
the fluid flow and EGR mixing in the manifold of a six-cylinder engine by 
integrating the DMD algorithm to LES model. It was indicated that the 
DMD could visualize velocity field and the exhaust concentration field 
caused by EGR pulsation, which was conducive to optimize the EGR 
inhomogeneity in the engine manifold. The DMD algorithm was also 
used to detect the unsteady pressure behavior in the combustion 
chamber of a CI engine by Torregrosa AJ et al. [ 19 ], and it was proven 
that the modal unsteady characterization was feasible to guide the 
setting up of fuel spray angle to optimize the acoustic signature of the 
combustion process. In addition, the DMD algorithm was utilized to 
showcase the cycle to cycle variation features of in-cylinder flow under 
varying swirl conditions by Liu M et al. [ 20 ]. It was indicated that the 
cyclic variation of engine flow field at compression stroke could be 
suppressed by inducing a higher swirl ratio. Qin W et al. [ 21 ] depicted 
the in-cylinder flow characteristics by integrating the mode decompo -
sition approach with the LES simulation. The results revealed that the 
Z. Lian et al.                                                                                                                                                                                                                                     Applied Energy 378 (2025) 124807 
2

<!-- PDF_PAGE: 3 -->

computed flow fields could be divided into four reconstructed parts 
using the proper orthogonal decomposition algorithm: namely mean 
part, coherent part, transition part and turbulent part. The dominant 
frequencies and equilibrium flow field structures in every reconstructed 
flow part were therefore found by the DMD method. On the whole, via 
employing DMD algorithm, the break-up and attenuation process of 
unstable flow structures accompanied by different scale vortex forma -
tion and dissipation is able to be effectively demonstrated. The analysis 
of turbulent jet structures is crucial for comprehending the fundamental 
principles of fluid dynamics.
Therefore, the most effective approach to accurately depict the 
turbulent-induced thermal process of HPDI engines is by employing a 
numerical combustion method combined with an LES turbulence model 
to solve the governing equation. The present research on HPDI engines 
reveals a lack of investigation into the interaction mechanism between 
diesel and direct injection of natural gas. Hence, this study aims to uti -
lize the DMD algorithm and LES model for decomposing the transient in- 
cylinder flow field and visualizing the primary flow field structure, 
thereby comprehending the potential interaction effect between diesel 
and natural gas jets in HPDI engines. The impact of chemical kinetic 
mechanism of diesel active combustion products on natural gas ignition 
is typically elucidated through global path analysis based on reaction 
rate. Consequently, the current article is organized as follows: Section 2
presents construction of the three-dimensional CFD model for HPDI 
engine. Section 3 describes the DMD method used for decomposing the 
in-cylinder density field. The simulation results of DMD under different 
intersection angle between diesel and natural gas jet, followed by the 
discussion and comparation against reaction pathway analysis are pre -
sented in Section 4 . Finally, the conclusions are summarized in section 5 .
2. Construction of the 3D CFD model
In this study, the 3D engine combustion model was constructed 
based on the CFD software CONVERGE. Besides, a mixture of decalin, n- 
dodecane, isocetane, isooctane, and toluene is selected as the surrogate 
for diesel rather than single component to accurately reproduce the 
physicochemical property of practical diesel [ 22 ], while methane (CH
4
) 
is selected as the surrogate for natural gas. The compositions of five 
components in diesel fuel surrogate models are presented in Table 1 . 
This diesel/natural gas dual fuel chemical kinetic mechanism includes 
101 species and 344 elements reactions, and its predictions of ignition 
delay and species mole fraction for methane and diesel have been fully 
validated in previous study [ 23 ]. In-cylinder fuel injection and the 
subsequent spray dynamics play a key role in fuel-air mixing and the 
spray-guided combustion in engines. The interaction between jet ve -
locity and turbulence intensity results in a more pronounced energy 
exchange between fuel and air, thus the phenomenon of fuel spray and 
break-up became more significant for diesel to ignite natural gas in HPDI 
engine. So that, the spray models should be primarily calibrated in CFD 
modelling.
2.1. Numerical model for diesel spray
The objective of this section is to establish an accurate spray model 
for diesel fuel. Therefore, the modelling of evaporative diesel spray is 
carried out based on the LES dynamic structure model [ 24 ]. The 
experimental results from Du W et al. [ 25 ] is used to validate the diesel 
spray penetration. The relevant parameters are presented in Table 2 , and 
the spray mass flow rate for the validation case is plotted in Fig. 1 .
In order to accurately simulate diesel spray, the Frossling model [ 26 ] 
is adopted as evaporation model, the NTC model [ 26 , 27 ] is used as the 
droplet collision model. The Wall film model is selected for spray-wall 
interaction [ 28 ]. The crucial droplet break up of diesel spray is formu -
lated by the Kelvin-Helmholtz and Rayleigh-Taylor (KH-RT) model [ 29 ]. 
The comparison between measured data and simulation results of liquid 
and gas penetration of diesel spray is shown in Fig. 2 . In general, model 
predictions of liquid and gas penetration are consistent with experi -
mental results. The model accurately predicts the overall liquid phase 
penetration distance at 40 MPa but still performs discrepancy over the 
gas phase penetration distance. The diesel liquid penetration at 160 MPa 
from 0.2 ms to 0.6 ms could be precisely captured by current spray 
model. Moreover, spray model gives slight overpredictions for gas 
penetration in overall, but a bit underpredictions for liquid penetration 
from spray onset. The penetration discrepancies between model pre -
dictions and experimental results might be attributed to the capability of 
LES model in capturing vortices within the spray field and a refined grid 
that facilitates better resolution of small-scale vortices. The presence of 
vortex structures in the spray field leads to non-uniform fuel distribution 
and consequently results in deviations between predicted penetration 
and experimental results.
2.2. Numerical model for natural gas jet
In the present study, the INFLOW boundary based on mass flow rate 
is applied for predicting high-pressure natural gas spray [ 30 ] while the 
LES dynamic structure turbulence model [ 24 ] is used. In addition, the 
experimental results of methane jet from reference [ 31 ] is used to 
validate the accuracy of natural gas jet model, the experimental condi -
tions are given in Table 3 . Fig. 3 shows the comparative result of 
methane jet penetration between experimental images [ 31 ] and model 
predictions. With the development of CH
4 
jet, both the penetration 
distance and jet area have been continuously increasing. However, it has 
been observed that the size of the jet head at 500us is smaller than what 
have found in experiment. This discrepancy might be attributed to the 
ability of LES model to capture vortex structures within the flow field. 
These vortices introduce additional fluctuations in the jet head, resulting 
in a more dispersed distribution of CH
4 
within this region and conse -
quently causing a narrowing jet head.
2.3. CFD combustion model for HPDI engine
In the present study, the three-dimensional CFD model is constructed 
based on a six-cylinder four-stroke HPDI engine. Since there are nine 
diesel and natural gas injection holes of the injector evenly distributed 
along the circumference, the scheme of combining 1/9 sector and pe -
riodic boundary is selected to save the computational expense. The LES 
dynamic structure model [ 24 ] is employed for prediction of in-cylinder 
flow field. The combustion process is simulated utilizing the SAGE 
detailed chemical kinetics solver [ 32 ] coupled with the diesel/natural 
gas duel-fuel chemical kinetic mechanism [ 23 ] including 101 species 
and 325 elementary reactions. Besides, the O’Rourke and Amsden model 
[ 33 ] is adopted to simulate wall heat transfer process. The above cali -
brated spray models are applied to simulate diesel and nature gas 
Table 1 
Compositions of five components in diesel fuel surrogate models [ 22 ].
n- 
dodecane
isooctane toluene isocetane decalin
Diesel fuel 
surrogate
0.3602 0.0750 0.1950 0.3149 0.0549
Table 2 
Experimental setting of diesel spray.
Parameter Value
Injection pressure/MPa 40,160
Ambient pressure/MPa 4
Injection mass/mg 25
Ambient temperature/K 723
Fuel temperature/K 288
Z. Lian et al.                                                                                                                                                                                                                                     Applied Energy 378 (2025) 124807 
3

<!-- PDF_PAGE: 4 -->

injection, the Frossling model [ 26 ] is employed as diesel droplet evap -
oration model, the NTC model [ 26 , 27 ] is adopted as the droplet collision 
model. The Wall film model is adopted for spray-wall interaction [ 28 ]. 
The droplet break up of diesel spray is formulated by the KH-RH model 
[ 29 ]. The natural gas (CH
4
) is injected into cylinder at late stage of 
compression stroke based on INFLOW boundary. In this HPDI engine, 
the diesel and natural gas are directly injected into cylinder using a dual- 
fuel injector. As the ignition source, the diesel is injected into cylinder 
before natural gas, and the injection pressures of diesel and natural gas 
are 30 MPa and 28 MPa, respectively. The temperature boundaries for 
piston, cylinder head, and cylinder wall are set to 553 K, 523 K, and 420 
K. In order to capture the emissions of HPDI engine, the Extended Zel -
dovich model [ 34 , 35 ] and Hiroyasu model [ 36 ] are used for the 
description of the NOx and soot emissions. Since the mesh size within 
transition area in computational domain are critical to simulation sta -
bility and convergence, this study refers to the grids scheme in literature 
[ 37 ]. The base grid size of the HPDI engine model is 2 mm, and a four- 
level fixed embedding area has been added to refine the grid for both the 
diesel spray and natural gas jet regions. Additionally, a two-level fixed 
embedding area has been applied to refine the grid near the cylinder 
head, piston, and cylinder wall boundaries. Furthermore, the adaptive 
mesh refinement methodology based on velocity and temperature 
gradient has been enabled during calculations, refining it to 1/4 and 1/2 
relative to the base grid size respectively. The graphical meshes 
depicting the refined diesel spray and natural gas jet regions are shown 
in Fig. 4 (a) and (b). As a consequence, the 3D CFD model for HPDI 
engine combustion has been delicately constructed, then the operation 
conditions at full load (IMEP = 25.21 bar) with 1200 rpm and 1300 rpm 
are used to validate the CFD model.
The numerically predicted in-cylinder pressure and heat release rate 
(HRR), depicted in Fig. 5 , are compared to the HPDI engine experi -
mental results. Although there is a slight deviation between the calcu -
lated curves and measured ones, the overall trend of both cases is 
consistent. In order to quantitatively compare the difference between 
numerical simulation results and experimental results of HPDI engine 
combustion, Eq. (1) is used to calculate the relative errors of indicated 
power, indicated thermal efficiency and maximum cylinder pressure. 
The comparison results of key engine performance indicators are pre -
sented in Table 4 , demonstrating that all indicators exhibit a prediction 
Fig. 1. Diesel injection rate at 40 MPa and 160 MPa injection pressure [ 25 ].
Fig. 2. The comparison between experimental results [ 25 ] (symbols) and model predictions (solid lines) of liquid and gas penetration for diesel spray at 40 MPa (left) 
and 160 MPa (right).
Table 3 
The experimental conditions of methane jet.
Parameter Value
Nozzle diameter/mm 0.4
Ambient temperature/K 293
Ambient pressure/atm 1
Methane temperature/K 336
Ambient gas air
Fig. 3. Comparison between experimental images [ 31 ] and model predictions 
of methane jet.
Z. Lian et al.                                                                                                                                                                                                                                     Applied Energy 378 (2025) 124807 
4

<!-- PDF_PAGE: 5 -->

deviation within the range of 1 %. In general, the present HPDI engine 
combustion model is able to accurately predict the direct-injected nat -
ural gas combustion induced by pilot diesel under HPDI test 
circumstance. 
Er =
| p
exp
  p
sim
|
p
exp
× 100% (1) 
Where, p
exp 
represents the experimental value of indicated power, 
indicated thermal efficiency and maximum cylinder pressure, and p
sim 
represents the corresponding simulated value.
3. Interaction mechanism of pilot diesel fuel and natural gas jet
Since the natural gas is the primary exothermic fuel in HPDI engine 
while the diesel only acts as the ignited source, the oxidation of natural 
gas determines the combustion process in HPDI mode. It is inferred that 
the interactive effect of the transient flow field structure induced by 
diesel and natural gas jet promotes the turbulent mixing as well as the 
mass and heat transfer. The underlying interaction mechanism of break- 
up and attenuation process of jet vortex will be discovered in the 
following sections via DMD methodology.
3.1. Dynamic mode decomposition algorithm
DMD is a data driven method that offers a novel perspective for 
comprehending fluid flow by extracting dynamic patterns from time 
series data. The input data for DMD consists of flow field measurements 
obtained at equal time-interval through experiments or numerical sim -
ulations. By decomposing these time series data, the vortex structures 
with different frequencies could be extracted, thereby revealing key 
dynamic characteristics inherent in the flow field. DMD is an approxi -
mation to the Koopman operator mode, and the dissipation rate and 
frequency of the flow field structure could be reflected by the complex 
eigenvalue of the Koopman mode [ 38 ]. The diagram of DMD algorithm 
has been depicted in Fig. 6 and its input is a set of flow field sequence 
snapshots, such as a set of density flow field data, arranged according to 
time interval Δ t obtained from numerical simulation, as shown in Eq. 
(2) : 
v
N
1
=
{
v
1
, v
2 ,
v
3
, … , v
N
}
(2) 
where, v
i 
represents the flow field data at each moment, v
N
1 
denotes the 
flow field set from the 1st to the N th time.
When the time interval is small enough, the nonlinear system could 
be approximated as a linear system, and the coefficient matrix A satisfies 
Eq. (3) : 
v
i + 1
= A v
i
(3) 
The Krylov form of the original flow field sequence could be obtained 
by substituting Eq. (3) into Eq. (2) : 
v
N
1
=
{
v
1
, A v
1
, A
2
v
1
, … , A
N   1
v
1
}
(4) 
The information of flow field sequence v
N
1 
could be represented by 
the eigenvalues, eigenvectors and amplitudes of coefficient matrix A , 
and the Eq. (5) could be derived from Eq. (4) as: 
v
N
2
= Av
N   1
1
(5) 
Fig. 4. Graphical mesh refinement at diesel spray and natural gas jet regions.
Fig. 5. The comparison between predicted HRR and in-cylinder pressure against experiment results.
Table 4 
The comparative results of HPDI engine performance indicators.
Engine 
operation
Indicated 
power/ 
kW
Indicated 
thermal 
efficiency
Maximum 
cylinder 
pressure /MPa
1200 rpm, 
100%load
Experiment 347.9 45.74 22.56
Simulation 345.1 45.37 22.41
Relative 
error
0.8 % 0.8 % 0.7 %
1300 rpm, 
100%load
Experiment 388.9 46.01 22.70
Simulation 388.6 45.97 22.71
Relative 
error
0.08 % 0.09 % 0.04 %
Z. Lian et al.                                                                                                                                                                                                                                     Applied Energy 378 (2025) 124807 
5

<!-- PDF_PAGE: 6 -->

where, v
N
2 
represents the flow field set from the 2nd to the N th time, and 
v
N   1
1 
is the flow field set from the 1st to the N-1 th time.
The data set v
N   1
1 
is decomposed by singular value decomposition 
(SVD) method [ 37 ] to get the Eq. (6) : 
v
N   1
1
= U
∑
W
T
(6) 
where U and W are orthogonal matrices and 
∑
is a diagonal matrix.
Then, the Eq. (5) could be rewritten as Eq. (7) : 
v
N
2
= А U
∑
W
T
(7) 
The similar matrix 
̃
S of coefficient matrix A could be formulated by 
Eq. (7)
̃
S ≜ U
T
v
N
2
W
∑
  1
= U
T
AU (8) 
In this case, the DMD mode ϕ
i 
could be expressed as: 
ϕ
i
= U y
i
(9) 
where, y
i
is the eigenvector of the similar matrix 
̃
S . Through the above 
derivation, the original flow field could be decomposed into: 
v
i
≈
∑
N   1
i = 1
ϕ
i
λ
i   1
i
α
i
, i ∈ { 1 , … , N   1 } (10) 
where, the eigenvalue λ
i 
represents the flow field intensity of the DMD 
mode, and α
i 
represents the amplitude of the DMD mode.
The relative error of DMD algorithm is calculated by the norm of 
reconstructed flow field v
ʹ
i 
and original flow field v
i
, as shown in Eq. (11) : 
RE =
l
2
 
v
ʹ
i
)
  l
2
( v
i
)
l
2
( v
i
)
(11) 
where, v
ʹ
i 
and v
i 
represent DMD reconstructed flow field and original 
flow field data, respectively.
The frequency f
i 
associated with each spatial mode could be obtained 
by calculating the imaginary part of the complex eigenvalue λ
i 
and the 
time step Δ t between the snapshots: 
f
i
=
ω
i
2 π
=
Im { ln ( λ
i
) }
2 π Δ t
(12) 
3.2. Mode decomposition of in-cylinder density flow field
The DMD algorithm requires a set of in-cylinder flow field data with 
equal time intervals, and each flow field should contain the same 
number of mesh. However, in the combustion simulation of HPDI en -
gine, the number and location of mesh in the computing domain 
constantly change at each time step due to the Adaptive Mesh Refine -
ment (AMR) algorithm, which continuously adjusts the mesh based on 
temperature and velocity gradient during computation. As a result, the 
mesh generated by CFD software CONVERGE is not satisfied with the 
requirement of DMD algorithm. To rebuild the flow field mesh including 
the same number and location, the original flow field mesh is needed to 
be linearly interpolated into the orthogonal mesh using post-processing 
TECPLOT tool. In this study, each interpolated flow field contains 
17,616 orthogonal grids, which could save computation time while 
ensuring sufficient resolution.
In the current section, the input snapshots of the DMD algorithm are 
a set of density flow fields at full load of 1200 rpm. These snapshots 
cover the period from natural gas jet start to natural gas and diesel 
interaction, and continue until the time when the natural gas is ignited 
by pilot diesel. The start timings of diesel spray and natural gas jet are 
  10 
◦
CA ATDC and   5.5 
◦
CA ATDC at full load of 1200 rpm, respec -
tively. The time interval of the density flow field snapshots is set to 
0.1 
◦
CA. Because the nonlinear flow field system is approximated as a 
linear system by DMD, the relative error of the reconstructed density 
flow field and original density flow field has been evaluated according to 
Eq. (11) . The relative error is decreased with the increase of the number 
of snapshots participating in DMD algorithm, as shown in Fig. 7 . The 
relative error from   3 
◦
CA ATDC backward is basically less than 1 %, 
indicating that the DMD reconstructed density flow field could replace 
Fig. 6. The diagram of DMD algorithm.
Fig. 7. The change in relative error of DMD reconstructed flow field and 
input field.
Z. Lian et al.                                                                                                                                                                                                                                     Applied Energy 378 (2025) 124807 
6

<!-- PDF_PAGE: 7 -->

the original flow field satisfactorily.
The DMD algorithm decomposes the density flow fields into char -
acterized eigenvectors, eigenvalues, and amplitudes, as given in Eq. 
(10) . The real parts and imaginary parts of the eigenvalues represent the 
dissipation rates of the flow field energy and the moving frequencies of 
the flow field structures, respectively. The energy of the flow field 
structure corresponding to the eigenvalues located outside, above, and 
inside the unit circle is representative of an increase, stabilization, and 
decay, respectively. Among the 32 DMD modes studied, the largest 
number of decay modes can be found, while the growth modes and 
quasi-steady state modes are less common, as shown in Fig. 8 (a). In 
addition, the real and imaginary parts of the logarithmic eigenvalues are 
plotted in Fig. 8 (b), with color bar showing initial amplitude intensity. It 
is found that the mode frequencies calculated by DMD algorithm are 
symmetrically distributed. The logarithmic eigenvalue of most modes is 
less than 0, which indicates the flow field energy of these modes grad -
ually decays. There are six modes in which the energy of the flow field 
increases with time because the real parts of the logarithmic eigenvalues 
of these six modes are positive. The initial amplitudes of the two red 
modes, as seen from Fig. 8 , are 3887.97 kg ⋅ m
  3
, which is much higher 
than the rest where the initial amplitudes are less than 1000 kg ⋅ m
  3
.
Since the amplitudes of DMD modes can reflect the energy content of 
flow field structures, four modes with maximum initial amplitudes are 
selected to study the primary structure of the density flow field. As 
depicted in Fig. 9 , the initial amplitudes of pair modes 0 and 1 are the 
largest among all DMD modes, reaching 3887.97 kg ⋅ m
  3
, followed by 
pair modes 26 and 27 with initial amplitudes of 354.31 kg ⋅ m
  3
. 
Therefore, the modes 0, 1, 26 and 27 are considered observable rich in 
capturing the intrinsic dynamics of fluid structure interactions between 
diesel and natural gas jet.
Fig. 10 (a) and (b) present the dynamics and flow field structures 
corresponding to modes 0 and 1 based on density flow field decompo -
sition. Since the real parts of the logarithmic eigenvalues of the modes 
0 and 1 are positive, as shown in Fig. 8 (b), their flow field energies are 
enhanced with a time-varying natural gas jet, and rise from 3887.97 
kg ⋅ m
  3 
to 4020 kg ⋅ m
  3 
gradually, which indicates that the flow field 
structures captured by the modes 0 and 1 are the primary in-cylinder 
flow field structures from natural gas injection to its ignition. Since 
the eigenvectors and time-varying amplitudes of modes 0 and 1 are 
equal, the flow field structure and dynamics of these two modes are 
identical, as depicted in Fig. 10 . The eigenvectors ϕ
i 
in Eq. (10) are 
dimensionless. Therefore, the color levels in Fig. 10 (b) are also 
dimensionless. The cloud image represents the relative density distri -
bution within each region of the cylinder. From Fig. 10 (b), the density 
within natural gas jet area is the highest, while there is the lowest 
density at active products area of diesel combustion with an obvious 
density gradient between the core region and the peripheral region. The 
density of ambient gas area is uniformly distributed far from the inter -
ference between diesel and natural gas jet. Specifically, the flow field 
structures captured by modes 0 and 1 reflect the vortex entrainment 
phenomenon caused by the impingement of high momentum natural gas 
jet to the active products of diesel combustion. The heat transfer and 
exchange of active radical will be enhanced by such vortex entrainment 
process, so as to accelerate the ignition of natural gas.
The pair modes 26 and 27 have the second largest initial amplitudes, 
their dynamics and flow field structures are shown in Fig. 11 (a) and (b). 
Similar to pair modes 0 and 1, the eigenvectors and time-varying am -
plitudes of modes 26 and 27 are identical, they exhibit the same dy -
namics and flow field structure. As shown in Fig. 8 (b), the real parts of 
the logarithmic eigenvalues of modes 26 and 27 are negative, indicating 
that the energies of the flow field captured by them gradually decreases 
from the initial 354.31 kg ⋅ m
  3 
to 0, as shown in Fig. 11 (a). The mass 
transfer phenomenon of the natural gas jet entrains with the ambient air 
is reappeared by the uneven local density from flow field structures of 
modes 26 and 27, as illustrated in Fig. 11 (b).
So far, the dynamics and flow field structures of the primary modes 
resulting from direct injected natural gas jet interfering with diesel have 
been analyzed using DMD algorithm. In general, whether it is the vortex 
entrainment phenomenon generated by the impingement of natural gas 
jet on active products of diesel combustion or the uneven density dis -
tribution in natural gas jet entrained with ambient air, the processes of 
vortex break-up and decay facilitate both the entrainment of natural gas 
Fig. 8. Distribution of the DMD mode eigenvalues in the complex plane.
Fig. 9. The energy spectrum of DMD modes.
Z. Lian et al.                                                                                                                                                                                                                                     Applied Energy 378 (2025) 124807 
7

<!-- PDF_PAGE: 8 -->

with the surrounding air and the entrainment of active products 
resulting from diesel combustion. As a result, the natural gas jet is more 
prone to undergo chemical oxidation reaction, thus facilitating its 
ignition. Furthermore, it is inferred that the impingement phenomenon 
of natural gas jet on active products of diesel combustion should be the 
key factor to natural gas ignition, and the impact strength strongly 
depends on the intersection angle between the axis of the diesel spray 
and the natural gas jet. From this point of view, the next section will 
focus on the exploring how varying injection intersection angle between 
diesel and natural gas injection affect HPDI engine combustion 
characteristics.
Fig. 10. Analysis of the dynamics and flow field structures of modes 0 and 1 based on density field decomposition.
Fig. 11. Analysis of the dynamics and flow field structures of modes 26 and 27 based on density field decomposition.
Z. Lian et al.                                                                                                                                                                                                                                     Applied Energy 378 (2025) 124807 
8

<!-- PDF_PAGE: 9 -->

4. Interference effects of diesel/natural gas injection on engine 
combustion
Fig. 12 plots the diagram of diesel and natural gas dual-fuel injection 
in a HPDI engine with a coaxial dual-fuel injector. The engine operation 
of 1300 rpm and full load (IMEP = 26.35 bar) is selected as the baseline. 
Angle β is defined as the intersection angle between diesel and natural 
gas, and its baseline value is 0
◦
. In this section, the diesel injection angle 
is expected to vary from 67
◦
to 75
◦
while the natural gas injection angle 
keeps unchanged, to investigate the corresponding prime flow field 
structures in-cylinder and their influence on HPDI engine combustion 
performance with different intersection angles β . The specific case setup 
is presented in Table 5 . A negative intersection angle β indicates that the 
diesel spray axis is close to the natural gas jet axis, and vice versa.
4.1. Effects of intersection angle of direct diesel and natural gas injection 
on HPDI engine combustion
Fig. 13 (a) and (b) plot the effects of intersection angle β of direct 
injected diesel and natural gas on in-cylinder pressure, HRR, and com -
bustion phase. With the intersection angle β decreases, the HRR phase is 
dramatically advanced, and the first small peak of low-temperature 
exothermic reactions has no obvious change but the second peak of 
HRR is significantly reduced, which indicated that the varying inter -
section angle β has great influence to natural gas ignition rather than 
diesel compression ignition. When the intersection angle β ≤ 0
◦
, the 
smaller the intersection angle β , the faster the pressure rises near TDC, 
but there is little difference in the maximum pressure. Compared to β ≤
0
◦
, the phase of maximum pressure is retarded when β = 4
◦
. As shown in 
Fig. 13 (b), the combustion phases defined as CA10-CA50 or CA50-CA90 
have slight difference among the cases of β =   4
◦
to   2
◦
. However, when 
β = 4
◦
, both CA10 and CA90 experience significant delays. Based on the 
in-cylinder temperature and OH distribution cloud diagrams shown in 
Figs. 16 and 17 , it can be observed that β = 4
◦
hinders the efficient 
exchange of heat and active radicals between diesel combustion active 
products and natural gas jet, resulting in suboptimal ignition effective -
ness and slow natural gas combustion rate. This ultimately undermines 
engine performance.
Effects of β on CO, NOx, indicated thermal efficiency, and indicated 
power are illustrated in Fig. 14 . The predicted values of CO and NOx 
closely align with the experimental values. NOx emissions remained 
consistent with the baseline in all cases, while CO emissions were 
minimized at the case of β = 2
◦
. The reduction of CO emissions by 44.9 % 
at β = 2
◦
indicates a significant increase in the oxidation of CO to CO
2
. 
This oxidation heat release process leads to higher thermal efficiency 
and indicated power of the engine under β = 2
◦
compared to other 
conditions, as illustrated in Fig. 14 (b). Therefore, the β = 2
◦
angle is 
considered as the optimal intersection angle between diesel and natural 
gas in the HPDI engine.
The DMD algorithm is employed to extract the prime flow field 
structures with varying β in order to further investigate the impact of 
intersection angle β on the combustion process of HPDI engine, as 
illustrated in Fig. 15 . When β is set at 4
◦
, the natural gas jet remains 
separated from the majority of active products generated during diesel 
combustion, with the exception of the region near the jet hole. This 
phenomenon of separation poses difficulties in igniting natural gas and 
consequently contributes to the ignition delay observed in CA10 at β =
4
◦
. As the β decreases, the combustion products of diesel are in complete 
contact with the natural gas jet. When β is set to   2
◦
and   4
◦
, the 
natural gas jet passes through the active product region, resulting in a 
further increase in the contact area between them. Consequently, as β 
decreases, there is a gradual increase in the contact area between the 
active products of diesel combustion and the natural gas jet, the contact 
between both jets is more intense.
To provide a direct representation of combustion process in cham -
ber, Fig. 16 plots the distribution of in-cylinder temperature and the 
contour of CH
4 
mole fraction (with concentration of 0.005) at β = 4
◦
, 0
◦
, 
and   4
◦
. In the present study, jet downstream is specified as the area 
where the natural gas jet and the high temperature area are spatially 
separated from the Y direction. The temperature in the vicinity of the 
natural gas jet, as depicted in Fig. 16 , remains below 800 K while the 
high-temperature area resulting from diesel combustion is situated just 
beneath it. With the advancement of the natural gas jet, there is an in -
crease in the contact area between the natural gas jet and the high 
temperature region. Moreover, a smaller β corresponds to a larger con -
tact area between the natural gas jet and the high temperature region, 
which aligns with the findings from results of DMD decomposition. As 
more natural gas gets involved into the high-temperature area, the 
cooling effect of the low-temperature natural gas jet results in the 
gradual fading of the high-temperature area. Since the diesel/air 
mixture gradually burns out at high-temperature area downstream, 
while the natural gas/air mixture cannot be supplemented to this area 
owing to a large spatial gap in the case of larger β , the temperature of 
this area drops. However, the high-temperature area downstream of β =
  4
◦
can maintain higher temperature until   2.5 
◦
CA ATDC. It can be 
inferred from the overlap between high-temperature area and the con -
tour of CH
4 
that the natural gas/air mixture continuously reaches at the 
high-temperature area downstream, while its combustion provides en -
ergy to sustain such high temperature. Therefore, the presence of a 
smaller β is advantageous in maintaining an elevated temperature re -
gion downstream, thereby facilitating the ignition of the natural gas/air 
mixture.
The OH radical acts as an active product of diesel combustion, its 
distribution is similar with field of in-cylinder high-temperature, as 
plotted in Fig. 17 . The decreased β could enhance the cooling effect from 
low-temperature natural gas jet to high-temperature area, thereby the 
high-temperature reactions of diesel are suppressed, resulting in shrink 
area of OH radical distribution. Moreover, more natural gas/air mixture 
enters the downstream of high-temperature area with the decreased β , 
this mixture blends with the OH radical produced by the high- 
Fig. 12. The diagram of intersection angle of diesel and natural gas injection.
Table 5 
The cases setup of varied intersection angles.
Parameter baseline 
(1300 rpm, 100 % 
load)
Case1 Case2 Case3 Case4
Diesel injection angle 
α
1
71
◦
67
◦
69
◦
73
◦
75
◦
Natural gas injection 
angle α
2
71
◦
71
◦
71
◦
71
◦
71
◦
Intersection angle β =
α
2
- α
1
0
◦
4
◦
2
◦
  2
◦
  4
◦
Z. Lian et al.                                                                                                                                                                                                                                     Applied Energy 378 (2025) 124807 
9

<!-- PDF_PAGE: 10 -->

temperature reaction of diesel, and therefore accelerate the ignition of 
natural gas/air mixture. As a consequence, the combustion of natural 
gas/air mixture provides energy to sustain the high-temperature in this 
region and continuously generates a large amount of OH radical. This is 
why the downstream area could maintain high-temperature and high 
OH radical concentration at β =   4
◦
. However, for the case of β = 4
◦
and 
0
◦
, the amount natural gas/air mixture entering the downstream of high- 
temperature area is lower. After the original diesel/air mixture in the 
area is consumed, the high-temperature reaction could not be continued, 
resulting in a decrease of the OH radical concentration. Therefore, the 
effective collision of natural gas/air mixture with active products of 
diesel combustion is a principal factor to the ignition of natural gas/air 
mixture in HPDI engines. From this point of view, the intrinsic chemical 
kinetics mechanism of OH radical promoting the ignition process and 
the reaction path of natural gas oxidation is deserved to further 
investigated.
4.2. Effects of OH radical on ignition and reaction path of natural gas 
oxidation
In this section, the software CHEMKIN-Pro is used to investigate the 
influence of the varying mole fraction of OH radical on the ignition 
characteristics of natural gas. The simulated condition encompasses a 
temperature range of 800-1200 K, an equivalence ratio range of 0.5 – 2, 
and the pressure up to 17 MPa to accommodate the HPDI engine in- 
cylinder environment at   5
◦
CA ATDC. The initial mole fraction of 
OH radical is set to be 0 and 5E-5, respectively. The simulated results of 
ignition delays for CH
4
/air mixture are depicted in Fig. 18 . The 
increased concentration of OH radical is able to shorten the ignition 
delays when Ф is unchanged, and the accelerating effect is more pro -
nounced at lower temperature conditions compared to high- 
temperature cases. In order to explore the intensified reaction path of 
CH
4 
oxidation process with addition of OH radical, a reaction-rate based 
global pathway analysis is conducted under the conditions of T = 1000 
K, P = 17 MPa, Ф = 0.5 and 1, with varying levels of added OH radicals.
The prime reaction path of CH
4 
oxidation at T = 1000 K, P = 17 MPa, 
and Ф = 0.5 and 1 is obtained by integrating the reaction rate of the 
elementary reactions of CH
4 
from reaction beginning to the time of CH
4
/ 
air mixture ignition, as shown in Fig. 19 . The green font indicates a 
reaction path with an OH concentration of 5E-5, while the blue font 
represents a reaction path with an OH concentration of 0. In the CH
4 
oxidation path, the CH
3 
is firstly generated by dehydrogenation reaction 
of CH
4
, and there are three prime reaction paths for the oxidation of CH
3 
at T = 1000 K, P = 17 MPa, and Ф = 0.5, which are represented by the 
blue, purple, and the black color solid lines, respectively. It is appre -
ciable that there are distinct differences in the reaction path of CH
3 
at 
varying OH radical additions, as highlighted by the red rectangle. On the 
one hand, the 92.6 % of CH
3 
is produced by CH
4 
+ OH = CH
3 
+ H
2
O, and 
the reaction CH
4 
+ HO
2 
= CH
3 
+ H
2
O
2 
contributes 4.1 % of CH
3 
pro -
duction. By comparison, when the added OH radical concentration is 5E- 
5, the CH
3 
generated by the reaction CH
4 
+ OH = CH
3 
+ H
2
O is dominant 
by 99.6 %, which is higher than the sum of CH
4 
+ OH = CH
3 
+ H
2
O and 
Fig. 13. Effects of intersection angle β on in-cylinder pressure and combustion phase.
Fig. 14. Effects of β on CO, NOx, indicated thermal efficiency and indicated power.
Z. Lian et al.                                                                                                                                                                                                                                     Applied Energy 378 (2025) 124807 
10

<!-- PDF_PAGE: 11 -->

CH
4 
+ HO
2 
= CH
3 
+ H
2
O
2 
in the absence of OH radical. It has been 
proven that the reaction CH
4 
+ OH = CH
3 
+ H
2
O is one of the main 
consumption reactions of CH
4 
as concluded in Ref. [ 14 ] at the relevant 
conditions of dual fuel engine. This leads to a shorter ignition delay of 
CH
4
/air mixture due to the participation of OH radicals. On the other 
hand, the addition of OH radicals also promotes the CH
3 
consumption 
via CH
3 
+ OH( + M) = CH
3
OH( + M) from 2.3 % to 6.4 %. The rapid 
consumption of CH
3 
is therefore conducive to the ignition of CH
4
. The 
ignition reaction path of CH
4
/air mixture at T = 1000 K, P = 17 MPa, 
and Ф = 1 is displayed in Fig. 19 (b). In this condition, CH
4 
dehydrogenates to produce CH
3 
first, and then CH
3 
only generates CH
3
O 
and CH
2
O via CH
3 
+ HO
2 
= CH
3
O + OH and CH
3 
+ O
2 
= CH
2
O + OH. As 
the same condition of Ф = 0.5, the addition of OH radical also promotes 
the ignition by strengthening the CH
4 
consumption reaction CH
4 
+
OH = CH
3 
+ H
2
O, and its CH
4 
consumption rises from 92.1 % to 99.5 %.
So far, the DMD algorithm is utilized to decompose the in-cylinder 
density field of an HPDI engine. The in-cylinder primary flow field 
structure, from natural gas injection to its ignition, is characterized by 
the vortex entrainment caused by the impingement between the natural 
gas jet and the active products of diesel combustion. The processes of 
Fig. 15. The primary flow field structures with varying β .
Fig. 16. In-cylinder temperature distribution (Color level represents temperature, solid line is CH
4 
contour line with mole fraction of 0.005).
Z. Lian et al.                                                                                                                                                                                                                                     Applied Energy 378 (2025) 124807 
11

<!-- PDF_PAGE: 12 -->

vortex break-up and decay, accompanied by the formation and dissi -
pation of vortices at various scales, facilitate the entrainment of natural 
gas with surrounding air as well as the active radicals from pilot diesel 
combustion. Moreover, a reaction-rate based global pathway analysis is 
conducted to elucidate underlying chemical kinetics mechanism for 
assisted CH
4
/air ignition with varying OH radical additions. Such 
investigation provides theoretical basis for further optimization of HPDI 
injection strategies.
5. Conclusion
In this study, the 3D combustion model of an HPDI engine is estab -
lished by integrating the diesel/natural gas dual-fuel chemical kinetics 
mechanism with LES dynamic structure model in CFD software 
CONVERGE. The DMD algorithm is employed to decompose the density 
flow field within the HPDI engine cylinder to deeply explore the vortex 
interference effects of diesel and natural gas injection. Moreover, the 
underlying synergetic dynamics is further disclosed from view of 
chemical kinetics. The main conclusions of this study are summarized as 
follows: 
1. Modal decomposition results reveal that during the period from 
natural gas injection to its ignition, the in-cylinder primary flow field 
structure is characterized by vortex entrainment phenomenon pro -
duced by the impingement between natural gas jets and diesel 
combustion active products, thereby intensifying heat and active 
radicals exchange between the natural gas jet and the active products 
of diesel combustion.
2. HPDI engine numerical simulation with different β is carried out to 
investigate the effects of diesel/natural gas injection on engine 
combustion. Numerical simulation results show that there is an 
optimized β ( β = 2
◦
under full load of 1300 rpm in this study) that 
reduces CO emissions by 44.9 %. The reason is that when β = 2
◦
, the 
overlap between the natural gas jet region and the active product 
region of diesel combustion effectively initiates ignition of the nat -
ural gas jet, resulting in a more optimal combustion phase for natural 
gas. This leads to increased oxidation of CO to CO
2
, thereby reducing 
CO emissions.
3. The reaction-rate based global pathway analysis is introduced as an 
auxiliary means to explain the chemistry mechanism of natural gas 
ignition surrounded by active radicals. Varied OH concentrations are 
added to CH
4
/air mixture, and ignition delay times are compared. It 
Fig. 17. The in-cylinder distribution of OH radical.
Fig. 18. The effect of OH radical addition on the ignition delay of CH
4
/air mixture.
Z. Lian et al.                                                                                                                                                                                                                                     Applied Energy 378 (2025) 124807 
12

<!-- PDF_PAGE: 13 -->

is indicated that OH exhibits a more pronounced promoting effect on 
CH
4
/air ignition, especially at low initial temperatures. The reaction 
path analysis reveals that the addition of OH radical accelerates the 
ignition of CH
4
/air mixture by increasing CH
4 
consumption of CH
4 
+
OH = CH
3 
+ H
2
O to 99.6 % and 99.5 % when Ф = 0.5 and 1, 
respectively. Moreover, the addition of OH radicals also increased 
the CH
3 
consumption of CH
3 
+ OH( + M) = CH
3
OH( + M) by 4.1 % 
when Ф = 0.5.
CRediT authorship contribution statement
Zifan Lian: Writing – original draft, Visualization, Validation, Soft -
ware, Methodology, Investigation, Data curation, Conceptualization. 
Wei Li: Investigation, Data curation. Yanbin Cai: Data curation. Hou -
chang Chen: Visualization. Junxin Jiang: Visualization. Guoxiang Li: 
Supervision, Funding acquisition. Feiyang Zhao: Writing – review & 
editing, Supervision, Investigation, Funding acquisition, Conceptuali -
zation. Wenbin Yu: Supervision, Methodology, Funding acquisition, 
Conceptualization.
Declaration of competing interest
The authors declare that they have no known competing financial 
interests or personal relationships that could have appeared to influence 
the work reported in this paper.
Acknowledgements
The authors greatly acknowledge the support of National Key 
Research and Development Program of China (No. 2021YFD2000302), 
Key R & D plan of Shandong Province (No. 2021CXGC010812-2) and 
Shandong Provincial Natural Science Foundation (NO. ZR2021ME212 
and No. 2022HWYQ-061).
The authors would like to express their sincere gratitude to 
CONVERGE SCIENCE Inc. and their engineering team for their invalu -
able support.
Data availability
Data will be made available on request. 
Fig. 19. Reaction path of CH
4
/air mixture at different OH radical additions (T = 1000 K, P = 17 MPa, Ф = 0.5 and 1).
Z. Lian et al.                                                                                                                                                                                                                                     Applied Energy 378 (2025) 124807 
13

<!-- PDF_PAGE: 14 -->

References
[1] Shenghua L, Longbao Z, Ziyan W, Jiang R. Combustion characteristics of 
compressed natural gas/diesel dual-fuel turbocharged compressed ignition engine. 
Proceedings Inst Mech Engineers, Part D: J Automobile Eng 2016;217(9):833–8 .
[2] Poompipatpong C, Cheenkachorn K. A modified diesel engine for natural gas 
operation: performance and emission tests. Energy 2011;36(12):6862–6 .
[3] Li M, Zhang Q, Li G, Shao S. Experimental investigation on performance and heat 
release analysis of a pilot ignited direct injection natural gas engine. Energy 2015; 
90:1251–60 .
[4] Mousavi SM, Saray RK, Bahlouli K, Poorghasemi K, Maghbouli A, Sadeghlu A. 
Effects of pilot diesel injection strategies on combustion and emission 
characteristics of dual-fuel engines at part load conditions. Fuel 2019;258 .
[5] McTaggart-Cowan GP, Rogak SN, Munshi SR, Hill PG, Bushe WK. The influence of 
fuel composition on a heavy-duty, natural-gas direct-injection engine. Fuel 2010; 
89(3):752–9 .
[6] Zhang Q, Song G, Wang X, Li M. Effects of injection strategy on the knocking 
behavior of a pilot ignited direct injection natural gas engine. Fuel 2022;308 .
[7] Khosravi M, McTaggart-Cowan G, Kirchen P. Pyrometric imaging of soot processes 
in a pilot ignited direct injected natural gas engine. Int J Engine Res 2020;22(5): 
1605–23 .
[8] Rochussen J, McTaggart-Cowan G, Kirchen P. Parametric study of pilot-ignited 
direct-injection natural gas combustion in an optically accessible heavy-duty 
engine. Int J Engine Res 2019;21(3):497–513 .
[9] Li M, Wang X, Jia D, Wang C, Wang R, Zhang Q, et al. Experimental investigation 
on the combustion and emissions in a pilot ignited direct injection natural gas 
engine using HCDI strategy. Fuel Process Technol 2021;222 .
[10] Liu J, Zhao HB, Wang JL, Zhang N. Optimization of the injection parameters of a 
diesel/natural gas dual fuel engine with multi-objective evolutionary algorithms. 
Appl Therm Eng 2019;150:70–9 .
[11] Li M, Li C, Wei Z, Zhang Q, Rao Z. Numerical study on the combustion and 
emission characteristics of a direct injection natural gas engine ignited by diesel/n- 
butanol blends. Appl Therm Eng 2023;226 .
[12] Yu S, Wei L, Zhou S, Lu X, Huang W. Numerical study on the effects of pilot diesel 
quantity coupling EGR in a high pressure direct injected natural gas engine. 
Combust Sci Technol 2022:1–18 .
[13] Zhou L, Liu Z, Zhao W, Jiang X, Wei H. Large Eddy simulation of combustion 
characteristics of non-premixed methane jet with pilot diesel in high-pressure 
direct injection mode. SAE Int J Fuels Lubricants 2022;15(1):99–118 .
[14] Li J, Liu H, Liu X, Ye Y, Wang H, Yao M. Investigation of the combustion kinetics 
process in a high-pressure direct injection natural gas marine engine. Energy Fuel 
2021;35(8):6785–97 .
[15] Nemati A, Ong JC, Pang KM, Mayer S, Walther JH. A numerical study of the 
influence of pilot fuel injection timing on combustion and emission formation 
under two-stroke dual-fuel marine engine-like conditions. Fuel 2022;312 .
[16] Fink G, Jud M, Sattelmayer T. Influence of the spatial and temporal interaction 
between diesel pilot and directly injected natural gas jet on ignition and 
combustion characteristics. J Eng Gas Turbines Power 2018;140(10) .
[17] Luong HT, Wang Y, Sung H-G, Sohn CH. A comparative study of dynamic mode 
decomposition methods for mode identification in a cryogenic swirl injector. 
J Sound Vib 2021;503 .
[18] Sakowitz A, Mihaescu M, Fuchs L. Flow decomposition methods applied to the flow 
in an IC engine manifold. Appl Therm Eng 2014;65(1–2):57–65 .
[19] Torregrosa AJ, Broatch A, García-Tíscar J, Gomez-Soriano J. Modal decomposition 
of the unsteady flow field in compression-ignited combustion chambers. Combust 
Flame 2018;188:469–82 .
[20] Liu M, Zhao F, Hung DLS. A coupled phase-invariant POD and DMD analysis for the 
characterization of in-cylinder cycle-to-cycle flow variations under different swirl 
conditions. Flow, Turbulence Combust 2022;110(1):31–57 .
[21] Qin W, Zhou L, Liu D, Jia M, Xie M. Investigation of in-cylinder engine flow 
quadruple decomposition dynamical behavior using proper orthogonal 
decomposition and dynamic mode decomposition methods. J Eng Gas Turbines 
Power 2019;141(8) .
[22] Yu W, Zhao F, Yang W, Tay K, Xu H. Development of an optimization methodology 
for formulating both jet fuel and diesel fuel surrogates and their associated skeletal 
oxidation mechanisms. Fuel 2018;231:361–72 .
[23] Lian Z, Zhang J, Zhao F, Yu W. Optimization of methane simplified chemical 
kinetic mechanism based on uncertainty quantitation analysis by sparse 
polynomial chaos expansions. Fuel 2023;339 .
[24] Pomraning E. Development of large Eddy simulation turbulence models. 2000 .
[25] Du W, Lou J, Yan Y, Bao W, Liu F. Effects of injection pressure on diesel sprays in 
constant injection mass condition. Appl Therm Eng 2017;121:234–41 .
[26] Reitz RD. Mechanism of atomization of a liquid jet. Phys Fluids 1982;25(10) .
[27] Taskiran OO, Ergeneman M. Trajectory based droplet collision model for spray 
modeling. Fuel 2014;115:896–900 .
[28] O’Rourke PJ, Amsden AA. A spray/wall interaction submodel for the KIVA-3 wall 
film model. SAE Int 2000;109:281–98 .
[29] Beale JC, Reitz RD. Modeling spray atomization with the kelvin-helmholtz/ 
rayleigh-taylor hybrid model9; 1999. p. 623–50 (6) .
[30] Le Moine J, Senecal PK, Kaiser SA, Salazar VM, Anders JW, Svensson KI, et al. 
A Computational Study of the Mixture Preparation in a Direct–Injection Hydrogen 
Engine. J Eng Gas Turbines Power 2015;137(11) .
[31] White TR. Simultaneous diesel and natural gas injection for dual-fuelling 
compression-ignition engines. UNSW, Sydney. In: PhD. Mechanical & 
Manufacturing Engineering, Faculty of Engineering. UNSW: UNSW; 2006 .
[32] Senecal PK, Pomraning E, Richards KJ, Briggs TE, Choi CY, McDavid RM, et al. 
Multi-dimensional modeling of direct-injection diesel spray liquid length and flame 
lift-off length using CFD and parallel detailed chemistry. SAE International; 2003 .
[33] Amsden A. KIVA3V. A block-structured KIVA program for engines with vertical or 
canted valves. United States; 1997:medium: CM; quantity: 1 CD rom; OS: UNICOS, 
UNIX (adaptable). HP-UX; Compatibility: MLT-PLTFM 2024 .
[34] Yang J, Golovitchev VI, Redon P, Sanchez Javier Lopez, J.. Numerical analysis of 
NOx formation trends in biodiesel combustion using dynamic ϕ-T parametric maps. 
SAE Technical Paper Series. SAE International; 2011 .
[35] Saario A, Rebola A, Coelho P, Costa M, Oksanen A. Heavy fuel oil combustion in a 
cylindrical laboratory furnace: measurements and modeling. Fuel 2005;84(4): 
359–69 .
[36] Rao V, Honnery D. Application of a multi-step soot model in a thermodynamic 
diesel engine model. Fuel 2014;135:269–78 .
[37] Li M, Zhang Q, Li G, Li P. Effects of hydrogen addition on the performance of a 
pilot-ignition direct-injection natural gas engine: a numerical study. Energy Fuel 
2017;31(4):4407–23 .
[38] Schmid PJ. Dynamic mode decomposition of numerical and experimental data. 
J Fluid Mech 2010;656:5–28 .
Z. Lian et al.                                                                                                                                                                                                                                     Applied Energy 378 (2025) 124807 
14
