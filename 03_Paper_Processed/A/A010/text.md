<!-- PDF_PAGE: 1 -->

Contents lists available at ScienceDirect
Fuel
journal homepage: www.elsevier.com/locate/fuel
Full Length Article
The e ﬀects of partially premixed combustion mode on the performance and
emissions of a direct injection natural gas engine
Menghan Li a,b, Xuelong Zheng b, Qiang Zhang c,⁎
, Zhenguo Li b,⁎
, Boxiong Shen a, Xiaori Liu a
a School of Energy and Environmental Engineering, Hebei University of Technology, Tianjin 300401, China
b National Engineering Laboratory for Mobile Source Emission Control Technology, China Automotive Technology & Research Center Co., Ltd., Tianjin 300300, China
c School of Energy and Power Engineering, Shandong University, Jinan 250061, China
ARTICLE INFO
Keywords:
Direct injection natural gas engine
n-Heptane
Methane
Partially premixed combustion mode
ABSTRACT
Direct injection natural gas engines have been widely recognized as a promising alternative for conventional
diesel or natural gas engines attributed to their advantages in both eﬃciency and emissions. However, with the
promulgation of the more stringent emission regulations, the control of soot and CO (carbon monoxide) emis-
sions becomes a major issue for the investigation of direct injection natural gas engines. In this paper, partially
premixed combustion mode is applied to a direct injection natural gas engine based on a 3D model coupled with
dual fuel chemical kinetic mechanism. The eﬀ ects of the proportion of the natural gas pre-injection and the
injection timing of the natural gas pre-injection are analyzed based on the combustion and emission results. In
order to further optimize the partially premixed combustion mode, the combined use of partially premixed
combustion mode and EGR (exhaust gas recirculation) was also assessed. The results indicate that soot and CO
emissions could be substantially reduced without penalties in NOx and thermal eﬃciency by the coordination of
PNPI (proportion of natural gas pre-injection), NPSOI (injection timing of natural gas pre-injection) and EGR.
1. Introduction
It is widely accepted that internal combustion engines are one of the
most predominant contributors to atmospheric pollution [1]. Owing to
the advantages in emission reduction and reserves, natural gas engines
are more and more concerned [2–4]. Currently, the more stringent
emission standards call for more advanced technologies of emission
control in natural gas engines. In high pressure direct injection natural
gas engines, the combustion mode can be ﬂexibly changed by adjusting
injection parameters to achieve optimum generally performance,
making it a favorable choice for the development of future natural gas
engine.
Many studies are focused on the emission characteristics, emission
control methods and emission prediction methods in direct injection
natural gas engines. Most of the earlier studies are focused on the tra-
ditional di ﬀusion-dominated combustion mode. Hill et al. [5] tracked
the formation of NO in a high pressure direct injection natural gas
engine by thermodynamic analysis and found that NOx emissions could
be reduced by delaying injection timing. Harrington et al. [6] con-
ﬁrmed that 45% reduction in NOx emissions could be achieved by using
direct injection natural gas instead of direct injection diesel; they also
found that NOx emission characteristics could be optimized by ad-
justing injection pressure and injection timing. McTaggart-Cowan et al.
[7] tried to reduce NOx emissions by adding EGR, changing relatively
injection timing between diesel and natural gas as well as varying in-
jection pressure; as can be concluded from their results, NOx emissions
could be considerably reduced by using later injection timing, lower
injection pressure and higher EGR fraction while PM, CO and HC
emissions would increase when the same measures are taken; at high
EGR fractions, the use of shorter relative injection timing between
diesel and natural gas could mitigate the negative e ﬀects of EGR on PM
and CO emissions, however, increases in NOx emissions and HC emis-
sions might be accompanied; they also attempted to reduce emissions
by adopting fuels with di ﬀerent compositions [8]; it is found that
https://doi.org/10.1016/j.fuel.2019.04.009
Received 10 December 2018; Received in revised form 2 March 2019; Accepted 3 April 2019
Abbreviations: BTDC, before top dead center; CO, carbon monoxide; CA50, 50% heat release combustion phase angle; DI-CNG, direction injection of compressed
natural gas; DRGEP, directed relation graph with error propagation; DRGEPSA, directed relation graph with error propagation and sensitivity analysis; EGR, exhaust
gas recirculation; HC, hydrocarbon; ITE, indicated thermal eﬃciency; NGSI, natural gas single injection; NOx, nitrogen oxides; NPP, proportion of natural gas post
injection; PAH, polycyclic aromatic hydrocarbon; PM, particulate matter; PNPI, proportion of natural gas pre-injection; NPSOI, injection timing of natural gas pre-
injection
⁎ Corresponding authors.
E-mail addresses: sduzhangqiang@sdu.edu.cn (Q. Zhang), lizhenguo@catarc.ac.cn (Z. Li).
Fuel 250 (2019) 218–234
Available online 06 April 2019
0016-2361/ © 2019 Elsevier Ltd. All rights reserved.
T

<!-- PDF_PAGE: 2 -->

unburned fuel emissions and black carbon emissions could be reduced
by increasing the proportion of nitrogen and hydrogen while NOx
emissions showed no de ﬁnite trend with the increase of nitrogen pro-
portion in the gaseous fuels. In recent years, with the purpose of
emission reduction, some new combustion strategies and new designs
of the injection system in direct injection natural gas engines are
evaluated and elaborated by numerical methods. Munshi et al. [9] ex-
plored the combined use of di ﬀusion-dominated combustion, partially
Fig. 1. Main oxidation paths for natural gas surrogate fuels (a) and diesel surrogate fuel (b).
100
1000
10000Ignition delay(μs)
1000/T(K
-1
)
=0.5,P=20atm
=3.0,P=40atm
=0.4,P=100atm
 detailed mech
 current mech
CH4 in AR/O2
0.5 0.6 0.7 0.8 0.9 0.60 0.65 0.70 0.75 0.80 0.85 0.90
100
1000
CH4 in N2/O2
Ignition delay(μ s)
1000/T(K
-1
)
=3.0,P=40atm
=3.0,P=75atm
=3.0,P=115atm
 detailed mech
 current mech
) b () a (
Fig. 2. Validation for the ignition delay of methane in Ar/O 2 (the experiment data of 20 atm are from Ref. [16], the experiment data of 40 atm and 100 atm are from
Ref. [17]) (a) and methane in N 2/O2 (the experiment data of all the pressures are from Ref. [17]) (b).
Fig. 3. Validation for the ignition delay of ethane (the experiment data are from Ref. [18]), methane/ethane mixtures (the experiment data are from Ref. [19]),
propane (the experiment data are from Ref. [20]) and methane/propane mixtures (the experiment data are from Ref. [21]).
M. Li, et al. Fuel 250 (2019) 218–234
219

<!-- PDF_PAGE: 3 -->

premixed combustion and homogenous charge combustion modes in a
direct injection natural gas engine; the results demonstrated that
homogenous charge combustion mode could attain extremely low NOx
and Soot emissions without reductions in thermal e ﬃ ciency, however,
the high peak pressure and pressure rise rate limit its use at high load
conditions; di ﬀusion-dominated combustion mode has higher soot and
NOx emissions compared to the other two operating modes, whereas it
can obtain the most steady operation at low loads; partially premixed
combustion strategy is a compromise between di ﬀusion-dominated
combustion and homogenous charge combustion modes, which means
it could be applied to high load conditions with relatively low soot and
NOx emissions. Zoldak et al. [10] applied DI-CNG operating mode in a
direct injection natural gas engine by numerical methods; their results
indicated that DI-CNG operating mode, which adopts two diesel injec-
tions, one before the injection of natural gas and one after the injection
of natural gas, could achieve fuel economy and soot emissions
equivalent to the conventional premixed natural gas combustion mode
without causing excessively high peak cylinder pressure and pressure
rise rate; however, for this combustion mode, the CO emissions are
extremely high and the fuel economy needs further improvement.
Mabson et al. [11] designed a new type of injectors with paired nozzles
for direct injection natural gas engine; their results indicated that NOx
emissions could be slightly reduced by the adoption of the new in-
jectors, however, obvious increases in soot and CO emissions would
occur. Faghani et al. [12] attempted to reduce the PM emissions in
direct injection natural gas engine by injecting natural gas earlier than
the end of pilot diesel injection; although only one natural gas injection
is applied, the proportion of premixed natural gas is increased as a
result of the negative injection separation between the pilot diesel in-
jection and the natural gas injection, leading to substantially reduced
PM emissions without penalties in NOx and unburned fuel emissions if
overall equivalence ratio and EGR ratio are appropriately selected; the
main drawback of this strategy is the higher cyclic variation caused by
the interference between the pilot diesel and natural gas injections. It
can be concluded from the previous studies that partially premixed
combustion mode is a promising way to reduce PM and CO emissions of
direct injection natural gas engines owing to its low knocking tendency
and high control ﬂexibility. Nevertheless, the CFD model used in the
previous study was based on very detailed mechanisms, which means
the calculations have high demand for computational resources;
moreover, they didn ’t provide detailed analysis of the e ﬀects of the
injection parameters and how the partially premixed combustion mode
can be optimized.
The object of this paper is to assess the potential of partially pre-
mixed combustion mode in achieving higher thermal e ﬃ ciency and
lower emissions. First, a more e ﬃ cient chemical kinetic mechanism
with high accuracy for diesel/natural gas dual fuel combustion was
constructed. The mechanism was not only used for ignition and oxi-
dation process prediction but also for the prediction of soot precursor
concentrations. Based on the constructed mechanism and the actual
parameters of the combustion chamber, a 3D model was built for the
direct injection natural gas engine. After veri ﬁcation, the 3D model was
applied to investigate the engine performance with di ﬀerent partially
premixed combustion strategies based on the analysis of combustion
parameters and emission characteristics. Finally, the combined appli-
cation of partially premixed combustion mode and EGR addition was
numerically evaluated to further optimize the engine performance.
2. Chemical mechanism construction
In pilot ignition direct injection natural gas engines, at least two
fuels, i.e. natural gas and diesel, should be taken into consideration.
Regarding the speci ﬁc combustion and emission formation process in
the research engine, natural gas is the main emissions source and diesel
acts as the ignition source. In this case, the mechanism of natural gas
should obtain high oxidation and ﬂame propagation accuracies while
for the mechanism of diesel, the ignition characteristic plays a key role.
Subsequently, a reduced mechanism is used for natural gas while a
skeleton mechanism is used for diesel to achieve the accuracy demand
and also the computational e ﬃ ciency. A decoupling method is used for
the mechanism construction, implying that the mechanisms of natural
gas and diesel were constructed separately and then merged together.
For direct injection natural gas engines with partially premixed com-
bustion
mode, the importance of premixed combustion increases, which
means the minor components in natural gas will take more e ﬀects.
Fig. 4. Validation for the ignition delay of n-heptane (the experiment data are
from Ref. [22]).
02468 1 0 1 2 1 4 1 6
0.00
0.05
0.10
0.15
0.20
0.25
0.30
C2H2
O2
Mole fraction
HAB(mm)
CH4
CO
H2O
CH4 in Ar/O2, =2.6, P=1atm
900 950 1000 1050 1100 1150 1200 1250
0.0000
0.0005
0.0010
0.0015
0.0020
C2H6 in N2/O2, =1.5, P=1atm 
C2H2×2
C2H4
CO2
CO
Mole fraction
Temperature(K)
C2H6
(a) (b)
Fig. 5. Validation for the mole fraction traces of methane and ethane [23].
M. Li, et al. Fuel 250 (2019) 218–234
220

<!-- PDF_PAGE: 4 -->

Thus, it is essential to take methane, ethane and propane into con-
sideration and select the mixture of these three fuels as the surrogate
fuel for natural gas. When constructing the sub-mechanism for natural
gas, the detailed mechanism for natural gas, i.e. AramcoMech 1.3 [13],
is selected as the basic mechanism as this mechanism has been widely
validated for the prediction of the oxidation process of methane, ethane
and propane. AramcoMech 1.3, which consists of 253 species and 1542
reactions, is reduced to a mechanism with 69 species and 403 reactions
by DRGEP (Directed Relation Graph with Error Propagation) and
DRGEPSA (Directed Relation Graph with Error Propagation and Sen-
sitivity Analysis). When constructing the sub-mechanism for diesel, n-
heptane is selected as the surrogate fuel for diesel since its ignition and
emission characteristics are similar to diesel. To simplify the
computation process without sacri ﬁces in the accuracies of ignition and
emission prediction, the large molecule reactions for n-heptane oxida-
tion is extracted from the skeletal mechanism developed by Pang et al.
[14] and corporated into the natural gas mechanism with modi ﬁcations
of reaction rate coe ﬃ cients and several reaction steps, forming an in-
tegrated dual fuel mechanism. The main oxidation paths for diesel and
natural gas surrogate fuels are shown in Fig. 1. The construction of the
ﬁnal mechanism used for the 3D simulation, which consists of 81 spe-
cies and 427 reactions, is completed after adding the 12-step NOx
Fig. 6. Validation for the mole fraction traces of propane (the experiment data are from Ref. [24]) and n-heptane (the experiment data are from Ref. [25].
Table 1
Engine speci ﬁcations.
Item Speciﬁcations
Number of cylinder 6
Engine type Turbocharged, water cooled
Combustion chamber bowl
Bore × Stroke/mm 150 × 150
Displacement/L 15.9
Compression ratio 15.7
Rated power/kW 353
Rated speed/rpm 2100
Idle speed/rpm 600
Fig. 7. Diagrams for the structure (a) and location (b) of the dual fuel injector.
Fig. 8. Validation of cylinder pressure.
M. Li, et al. Fuel 250 (2019) 218–234
221

<!-- PDF_PAGE: 5 -->

mechanism into the integrated mechanism.
3. Chemical mechanism validation
The mechanism has been validated for di ﬀerent surrogate fuels
against experiment data of shock tube ignition delays and mole fraction
traces for key species. All the simulations for the validations of the
mechanism were done with the Chemkin packages [15]. As shown in
Fig. 2, the simulation results for the ignition delay of methane ﬁt well
with those of the detailed mechanism and also are in good agreement
with the experiment results. As can be observed from Fig. 3, the si-
mulation results for the ignition delay of ethane, propane as well as
methane/ethane and methane/propane mixtures are generally con-
sistent with those of the detailed mechanism and are in good agreement
with the experiment results at most conditions. However, at pressure of
20 atm and equivalence ratio of 1.0, the deviations between the simu-
lation results for the ignition delay of ethane and the experiment results
are relatively larger at high temperatures. These deviations would not
cause large errors in 3D engine simulations because at high tempera-
tures, the errors are lower than 30 μs, which is smaller than 0.5°CA at
most engine speeds; in addition, the simulation results of the current
mechanism for methane/ethane mixture are of high accuracy and the
surrogate fuel of natural gas used for 3D simulations has lower than 5%
ethane in it, implying that the current mechanism is reliable enough for
the ignition delay prediction of natural gas in 3D simulations. In view of
diesel surrogate fuel, as illustrated in Fig. 4, the ignition delay of n-
heptane can be accurately reproduced by the current mechanism, im-
plying that the ignition of the 3D simulation can be predicted by the
current mechanism.
It is demonstrated in Figs. 5 and 6 that the predicted mole fraction
traces of the current mechanism ﬁt well with the experiment results,
indicating that the current mechanism can be applied to predicting the
oxidation process of surrogate fuels as well as the formation of CO and
C
2H2.
4. 3D model construction and case setup
4.1. 3D model construction
CFD simulations of the direct injection natural gas engine were
carried out using the commercial Converge code software [26]. The
computational mesh of the 3D model is constructed based on the real
geometry of the engine. The main speci ﬁcations of engines are given in
Table 1. The base size for the grid is 2 mm, re ﬁnements have been
conducted at locations with high velocity and high temperature to raise
the accuracy for the prediction of ﬂow and temperature ﬁelds. When
constructing the 3D model, the Redlich-Kwong equation is used to
couple density, pressure, and temperature. The RNG k-e model is used
for the simulation of the in-cylinder ﬂow ﬁeld. In views of the predic-
tion of the diesel spray, the Frossling model and the O ’Rourke model are
adopted for the prediction of the evaporation and collision of the diesel
droplets. The mechanism constructed in this paper is coupled with the
SAGE detailed chemistry solver to calculate the heat release process and
mole fractions of the related species. Based on the 3D model, simula-
tions were conducted at three di ﬀerent pressures and compared with
the experiment results. The detailed information of the experiment
setup were provided in Ref. [27]. In the experiment, a concentric dual-
fuel injector is used for both diesel and natural gas injection. Thus,
there is only one injector per cylinder. Diagrams for the structure and
location of the injector are shown in Fig. 7. It is demonstrated in Figs. 8
and 9 that the simulation results of three di ﬀerent cylinder pressures ﬁt
well with the experiment results, implying that the combustion process
of the engine can be well reproduced by the 3D model constructed in
this paper. Meanwhile, the simulation results of NOx, CO and soot
emissions agree well with the experiment results, indicating that the
accuracy for the predication of the emissions is high enough for the 3D
0
400
800
1200
1600
2000
2400
2800
240bar210bar
 NOx exp.
 NOx sim.
 CO exp.
 CO sim.
 Soot exp.
 Soot sim.
180bar
NOx(ppm)
0.000
0.003
0.006
0.009
0.012
0.015
Soot emissions(mg/cycle)
Fig. 9. Validation of emissions.
Table 2
Parameters of the simulation cases.
Case set NPSOI PNPI EGR
NGSI – – 0%
Partially Premixed 30°BTDC –130°BTDC (every 20°BTDC) 10%, 30%, 50%,
70%, 100%
0%
30°BTDC, 50°BTDC, 70°BTDC, 90°BTDC, 110°BTDC, 125°BTDC (Interference between two natural gas
injections will occur when more advanced NPSOI is applied)
90%
Partially Premixed+EGR 50°BTDC 30% 5%–25% (every
5%)50°BTDC 50%
110°BTDC 70%
130°BTDC 90%
130°BTDC 100%
-80 -60 -40 -20 0 20
0.000
0.001
0.002
0.003
0.004
0.005
0.006
Natural gas main-injection
Mass flow rate(kg/s)
Crank angle(°CA)
 NGSI
 HCDI
Natural gas pre-injection
Pilot diesel injection
NSOI
NPSOI
Fig. 10. Schematic diagram of the injection strategy for di ﬀerent combustion
mode.
M. Li, et al. Fuel 250 (2019) 218–234
222

<!-- PDF_PAGE: 6 -->

simulation.
4.2. Uncertainty analysis
Though the accuracy of the prediction for the combustion and
emission formation processes has been proved to be su ﬃ cient for 3D
simulations. The simulation results cannot be perfectly ﬁtted with the
experiment results, especially near the TDC and during the combustion
process, resulting in errors in cylinder pressure and emissions. The
uncertainty analysis is as follows:
 Errors caused by the blow-by and heat transfer process: In the
experiments, the blow-by and heat loss phenomena are inevitable.
However, the blow-by gas cannot be accounted for in 3D simula-
tions, thus, the simulated gas mass near the TDC is higher than the
actual value. Besides, the accurate simulation of heat loss
Fig. 11. Cylinder pressure of di ﬀerent NPSOI at di ﬀerent PNPI.
Fig. 12. Peak cylinder pressure (a) and maximum pressure rise rate (b) at di ﬀerent NPSOI and PNPI.
M. Li, et al. Fuel 250 (2019) 218–234
223

<!-- PDF_PAGE: 7 -->

phenomena is highly dependent on the heat transfer and the local
temperature distribution of the wall boundaries, which means li-
quid-solid coupling is in need; nevertheless, the implement of liquid-
solid coupling will consume extremely large computational re-
sources and is not adaptable for the 3D transient simulation of the
engine working process. Thus, there are biases between the simu-
lated heat loss and experimental heat loss. The errors caused by the
blow-by and heat transfer simulation, however, will lead to higher
cylinder pressure near the TDC as shown in Fig. 7. Actually, the
stage of pilot fuel heat release also exists in the experiment. But it is
less obvious due to the reduction in cylinder pressure caused by heat
loss and blow-by gas.
 Errors caused by the ﬂow ﬁeld simulation: In this paper, RNG k-e
turbulence model is applied to the simulation of the in-cylinder ﬂow
ﬁeld and the development of the natural gas jets. Though RNG k-e
model is e ﬃ cient for 3D simulation, especially when the detailed
injection and combustion processes are considered, it is unavoidable
that errors may exist in the detailed ﬂow ﬁeld description, especially
during the high speed injection of natural gas, where shock waves
and Mach disk may appear. In this case, disparities between
Fig. 13. Heat release rate at di ﬀerent NPSOI and PNPI.
Fig. 14. Temperature distribution of di ﬀerent NPSOI at PNPI of 50%(5°BTDC).
M. Li, et al. Fuel 250 (2019) 218–234
224

<!-- PDF_PAGE: 8 -->

simulation and experiment in the di ﬀusion process of natural gas as
well as the mixing process of fuel and air may be arisen, which will
lead to the errors during the combustion process.
 Errors caused by the ignorance of the crevices: In the actual
geometry of an engine, there are crevices between piston, piston
rings and liner. The detailed structures of these crevices are hard to
be considered in the 3D simulation due to the tiny sizes and the
dynamic changes during the working process. In the 3D simulation
of the current study, the volume of the crevices is considered
whereas the detailed geometry is neglected. Though the
Fig. 15. Local equivalence ratio distribution of di ﬀerent NPSOI at PNPI of 50% (5°BTDC).
Fig. 16. CA50 and ITE at di ﬀerent NPSOI and PNPI.
20 40 60 80 100 120 140
800
1600
2400
3200
4000
4800NOx emissions(ppm)
NPSOI(°BTDC)
PNPI       NGSI
 10%  30%
 50%  70%
 90%  100%
) b () a (
Fig. 17. NOx emissions at di ﬀerent NPSOI and di ﬀerent PNPI (a), cell data of NO mole fraction (b).
M. Li, et al. Fuel 250 (2019) 218–234
225

<!-- PDF_PAGE: 9 -->

simpliﬁcation of crevices is reasonable for 3D simulations, it may
bring about errors in emission prediction.
 Errors caused by the selection of the surrogate fuels: When se-
lecting the surrogate fuels for natural gas, C1 –C3 fuels, i.e. methane,
ethane and propane, are selected as the surrogate fuels to ensure the
accuracies of the oxidation and emission formation process. Larger
hydrocarbons are not considered owing to their low contents in
natural gas. With regard to diesel, n-heptane, which has the similar
900
1800
2700
3600
4500
NPSOI 30°BTDC 
NO(ppm)
Crank angle(°CA)
PNPI
 NGSI  10%
 30%    50%
 70%    100%
0 2 04 06 08 0 1 0 0 0 2 04 06 08 0 1 0 0
400
800
1200
1600
2000
PNPI 50%
NO(ppm)
Crank angle(°CA)
NPSOI
 NGSI     30°BTDC
 50°BTDC  70°BTDC
 90°BTDC  130°BTDC
) b () a (
Fig. 18. NO mole fraction traces at di ﬀerent NPSOI and di ﬀerent PNPI.
20 40 60 80 100 120 140
0
500
1000
1500
2000
2500
3000
CO emissions(ppm)
NPSOI(°BTDC)
PNPI       NGSI
 10%  30%
 50%  70%
 90%  100%
(a) (b)
Fig. 19. CO emissions at di ﬀerent NPSOI and di ﬀerent PNPI (a) and cell data of CO mole fraction (b).
NGSI PNPI 10%, NPSOI 30°BTDC PNPI 10%, NPSOI 90°BTDC 
PNPI 50%, NPSOI 30°BTDC PNPI 50%, NPSOI 90°BTDC PNPI 100%, NPSOI 30°BTDC 
Fig. 20. Local CO mole fraction distribution (15°ATDC).
M. Li, et al. Fuel 250 (2019) 218–234
226

<!-- PDF_PAGE: 10 -->

characteristics as diesel, has chosen as the surrogate fuels. For the
speciﬁc combustion and emission formation process in the research
engine, natural gas is the main emission source and diesel acts as the
ignition source, which means most of the related emissions, in-
cluding CO, NOx and soot, are coming from the combustion of
natural gas. Besides, most of the reliable detailed kinetic mechan-
isms and database available for validation are focused on n-heptane.
In this case, though potential uncertainties do exist, the ignorance of
heavier fuel molecules and aromatics will not lead to signi ﬁcant
errors in emission predictions.
Ideally, all the situations and structures in the experiments should
be taken into consideration when developing the 3D model. However,
limited by the simulation technique, computational source and e ﬃ -
ciency, only the most important models are integrated in the ﬁnal code.
Besides, simpli ﬁcation of the geometry and reduction of the kinetic
mechanism are essential. These will deﬁ nitely lead to uncertainties in
simulation. Nevertheless, in view of the combustion mode investiga-
tion, the accuracies are acceptable after the validation of cylinder
pressure and emissions.
0 2 04 06 08 0 1 0 0
10
100
1000
10000
 PNPI 10%
CO mole fraction(ppm)
Crank angle(°CA)
NPSOI
 NGSI
 30°BTDC
 50°BTDC
 70°BTDC
 90°BTDC
 110°BTDC
 130°BTDC
0 2 04 06 08 0 1 0 0
10
100
1000
10000
 PNPI 50%
CO mole fraction(ppm)
Crank angle(°CA)
NPSOI
 NGSI
 30°BTDC
 50°BTDC
 70°BTDC
 90°BTDC
 110°BTDC
 130°BTDC
) b () a (
0 2 04 06 08 0 1 0 0
10
100
1000
10000
 PNPI 70%
CO mole fraction(ppm)
Crank angle(°CA)
NPSOI
 NGSI
 30°BTDC
 50°BTDC
 70°BTDC
 90°BTDC
 110°BTDC
 130°BTDC
0 2 04 06 08 0 1 0 0
10
100
1000
10000
 PNPI 100%
CO mole fraction(ppm)
Crank angle(°CA)
NPSOI
 NGSI
 30°BTDC  50°BTDC  70°BTDC
 90°BTDC  110°BTDC  130°BTDC
) d () c (
Fig. 21. CO mole fraction traces at di ﬀerent NPSOI and PNPI.
20 40 60 80 100 120 140
1E-6
1E-5
1E-4
0.001
0.01
Soot emissions(mg/cycle)
NPSOI(°BTDC)
PNPI       NGSI
 10%  30%
 50%  70%
 90%  100%
(a) (b)
Fig. 22. Soot emissions at di ﬀerent NPSOI and PNPI (a), cell data of soot mass fraction (b).
M. Li, et al. Fuel 250 (2019) 218–234
227

<!-- PDF_PAGE: 11 -->

4.3. Case setup
A set of simulation cases were designed to evaluate the performance
of partially premixed combustion mode. Additional cases were also
designed to evaluate the e ﬀects of EGR to further optimize the partially
premixed combustion mode. All the simulations were done at injection
pressure of 180 bar, NSOI of 11°BTDC, DSOI of 18°BTDC and DPW of
5.5° because this is an optimized combination of parameters based on
the previous experiments. Other details of the simulation cases are
provided in Table 2. The schematic diagram of the injection strategy for
diﬀerent combustion mode is shown in Fig. 10.
5. Results and discussion
5.1. E ﬀects of PNPI and NPSOI
The cylinder pressures of di ﬀerent PNPI at di ﬀerent NPSOI are il-
lustrated in Fig. 11. As shown by the Figure, the peak cylinder pressure
is the highest at NPSOI of 30°BTDC for di ﬀerent PNPI, which can be
conﬁrmed by the peak cylinder pressure data in Fig. 12. This can be
explained by the distribution of equivalence ratio in Fig. 14, and the
temperature distribution in Fig. 15. As can be seen from Fig. 14,a t
NPSOI of 30°BTDC, the equivalence ratio is higher near the ﬂame front
and the distribution of the fuel is more concentrated around the corners
of the combustion chamber, which is more bene ﬁcial for the fast pro-
pagation of the natural gas ﬂame, leading to obvious higher heat release
rate ( Fig. 13) and thus higher peak cylinder pressure and higher max-
imum pressure rise rate( Fig. 12 ). It can also be summarized from
Figs. 11 and 12 that at PNPI from 10% to 50%, the peak cylinder
pressure changes in a very small range when NPSOI varies from
50°BTDC to 130°BTDC; at PNPI of 10% and 30%, this phenomenon is
caused by the smaller di ﬀerences in heat release rate( Fig. 13) while at
PNPI of 50%, the competing e ﬀect between the combustion phasing and
the peak heat release rate is the main contributor. When PNPI increases
to 70% or higher, the peak cylinder pressure is relatively higher at
NPSOI in the range of 70°BTDC to 110°BTDC due to the earlier com-
bustion phasing. It should also be noted that when partially premixed
combustion mode is adopted, the peak cylinder pressures are generally
higher than the combustion mode with NGSI strategy, except the peak
cylinder pressure at PNPI of 100% and NPSOI of 130°BTDC, which is
much lower than that of the NGSI combustion mode due to the less
stratiﬁed mixture formed in the cylinder.
NGSI PNPI 10%, NPSOI 30°BTDC PNPI 10%, NPSOI 90°BTDC 
PNPI 50%, NPSOI 30°BTDC PNPI 50%, NPSOI 90°BTDC PNPI 100%, NPSOI 30°BTDC 
Fig. 23. Local soot mass fraction distribution (15°ATDC).
NGSI PNPI 10%, NPSOI 30°BTDC PNPI 10%, NPSOI 90°BTDC 
PNPI 50%, NPSOI 30°BTDC PNPI 50%, NPSOI 90°BTDC PNPI 100%, NPSOI 30°BTDC 
Fig. 24. Local OH mole fraction distribution (15°ATDC).
M. Li, et al. Fuel 250 (2019) 218–234
228

<!-- PDF_PAGE: 12 -->

As shown in the heat release rates in Fig. 13, at most conditions of
partially premixed combustion mode, the heat release rate can be di-
vided into two main stages, i.e. the stage of pilot diesel combustion and
the stage of natural gas combustion. At PNPI from 10% to 50%, the
peak heat release during pilot diesel combustion changes slightly with
PNPI and NPSOI. However, at PNPI higher than 50%, the ignition of
pilot diesel will be delayed at NPSOI of 30°BTDC. This can be explained
by the enhanced competition between natural gas and pilot diesel at the
most advanced NPSOI and longer injection duration of the natural gas
pre-injection. Additionally, the ignition of natural gas shows an ad-
vancing trend with the increase of PNPI. At PNPI lower than 70%, the
combustion of natural gas can be splitted to the premixed combustion
phase and the di ﬀusion combustion phase, meanwhile, the two com-
bustion phases can be clearly distinguished. When PNPI increases to
70% or more, the borderline between the premixed and di ﬀusion
combustion of natural gas becomes indistinct due to the signi ﬁcant
increased amount of premixed natural gas. In addition, it should be
noticed that the peak heat release rate witnesses a reduction when
NPSOI increases to 70°BTDC or more. This is because the strati ﬁcation
is weakened and the ﬂame propagation gets slower at relatively ad-
vanced NPSOI.
Fig. 16 gives the CA50 and ITE at di ﬀerent NPSOI and PNPI. As
illustrated, ITE rises with the increase of PNPI at PNPI lower than 90%
attributed to the advanced CA50 and raised cylinder pressure. When
PNPI changes from 70% to 90%, the variation of ITE with PNPI is un-
certain due to the e ﬀects of lower ﬂame propagation. At PNPI of 10%,
the variation of ITE with NPSOI is relatively small, the values for ITE of
diﬀerent NPSOI are close to that of the NGSI combustion mode at
NPSOI of 130°BTDC owing to the combined e ﬀects of combustion
phasing and combustion completeness. However, at PNPI of 90% and
100%, the ITE is highly a ﬀected by the combustion phasing, i.e. ITE is
generally higher at advanced CA50.
Fig. 17 provides the NOx emissions at di ﬀerent NPSOI and PNPI. It
can be seen from the Figure that when partially premixed combustion
mode is applied, the NOx emissions will increase accordingly. Gen-
erally, NOx emissions increase with the increase of PNPI. This can be
explained by the cell data of NO mole fraction shown in Fig. 17b and
NO mole fraction traces in Fig. 18a. As can be seen, high values of NO
concentration generally appear at cells with temperature in the range of
2400 K–2800 K and equivalence ratio in the range from 0.75 to 0.97.
Though the highest temperature distributes near the stoichiometric
condition, NOx emissions are a ﬀected by the combined e ﬀects of tem-
perature and oxygen concentration and tend to get higher at leaner
conditions. When PNPI rises, more cells distribute in leaner and high-
temperature regions, leading to higher peak values of NO mole fraction
and the subsequent higher NOx emissions. Meanwhile, at PNPI lower
than 50%, NOx emissions change in a smaller magnitude with NPSOI.
When PNPI increases to 50% or more, the NOx emissions vary in a
larger range, however, the variation of NOx emissions with NPSOI is
uncertain attributed to the randomness of the local equivalence ratio
distribution of the natural gas/air mixture during the combustion pro-
cess and the subsequent uncertainties in the production of NOx
Fig. 25. General equivalence ratio distribution of di ﬀerent NPSOI and di ﬀerent PNPI.
M. Li, et al. Fuel 250 (2019) 218–234
229

<!-- PDF_PAGE: 13 -->

(Fig. 18 ). As can also be observed form Fig. 17, at PNPI of 50% and
70%, NOx emissions are lowest at 110°BTDC while reach the smallest
value at 130°BTDC at PNPI of 90% and 100%; the peak values of NOx
emissions appear at 30°BTDC at di ﬀerent PNPI and the highest value of
NOx emissions appears at PNPI of 90%.
In view of CO emissions ( Fig. 19), with the partially premixed
combustion mode adopted, CO emissions could witness considerable
reductions even at PNPI of 10%. At PNPI of 10%, the lowest CO
emissions can be found at 70°BTDC; at PNPI of 30% and 50%, the
lowest CO emissions can be found at 50°BTDC; at PNPI of 70%, the
lowest CO emissions can be found at 30°BTDC; at PNPI of 90% and
100%, the lowest CO emissions can be found at 30°BTDC. These phe-
nomena can be explained by the cell data, local distribution and mole
fraction traces of CO in Figs. 19b, 20 and 21. It is demonstrated in
Fig. 19b that there is a speci ﬁc range of equivalence ratio for high CO
emissions, i.e. from 1.5 to 2.4. At PNPI of 10%, 50% and 100%, the
equivalence ratios in most cells are lower than 3.3, 1.8 and 1.5 re-
spectively, indicating that the conditions for CO accumulation are
avoided at higher PNPI; therefore, the CO emissions will be reduced
accordingly. As can be seen in Fig. 20, with the increase of PNPI, the
regions with high CO concentration decrease obviously, however, the
locations are generally the same expect those for PNPI of 100%. At PNPI
of 0%, 10% and 50%, regions with high CO concentration distribute
near the corner opposite the natural gas jets, whereas at PNPI of 100%,
few CO molecules still exist at 15°BTDC, most of which appear at the
bottom of the cylinder head. As shown in Fig. 21, at PNPI of 10%, the
peak value of CO mole fraction changes slightly with NPSOI, the lower
value for CO emissions at PNPI of 70°BTDC is mainly caused by the
quicker oxidation at the later combustion stages( Fig. 21a). At PNPI of
50%, the peak values for the traces of CO mole fraction are much lower
than those of the NGSI combustion mode owing to the more premixed
distribution of the fuel/air mixture; meanwhile, the peak value of the
CO mole fraction trace is the lowest and the oxidation rate is relatively
high at NPSOI of 70°BTDC, leading to the fewest CO emissions emitted
(Fig. 21b). At PNPI of 70%, the di ﬀerences between the values for CO
mole fraction traces of di ﬀerent NPSOI are enlarged, indicating that the
mixing of the natural gas is more in ﬂuenced by NPSOI at larger PNPI;
moreover, though the peak in-cylinder CO mole fraction at NPSOI of
30°BTDC has the highest value, the oxidation rate is much quicker than
those of other NPSOI due to the signi ﬁcantly advanced combustion
phasing, resulting in lower CO emissions ( Fig. 21c). At PNPI of 100%,
the decreased CO formation plays a more important role; at NPSOI of
90°BTDC, both lower CO formation and higher oxidation rate can be
achieved, CO emissions can obtain an extremely low value ( Fig. 21d).
The soot emissions at di ﬀerent NPSOI and PNPI are demonstrated in
Fig. 22a. In this Figure, it is obvious that soot emissions will be sig-
niﬁcantly reduced with the increase of PNPI. This can be explained by
the cell data and mass fraction traces of soot in Figs. 22b and 26. As can
be deduced from Fig. 22b, the concentration of soot is mainly related
with equivalence ratio, i.e. higher soot mass fractions could be observed
with equivalence ratio higher than 1.2; when equivalence ratio rises
from 1.6, soot mass fraction changes in a smaller magnitude. These
behaviors indicate that if more cells have equivalence ratio higher than
1.2, soot emissions will be higher correspondingly. At higher PNPI,
proportion of cells with equivalence ratio higher than 1.2 increases
markedly, leading to reduced soot generation. The soot distribution in
Fig.
23 reveals the same trend of soot with the increase of PNPI. As
shown in the Figure, the regions with high soot concentrations are si-
milar to those with high CO concentrations due to the similar re-
lationship with equivalence ratio. It is generally agreed that soot oxi-
dation is associated with OH concentration, indicating that regions with
high OH are not prone to soot accumulation. This can be con ﬁrmed by
Fig. 26. Soot mass traces at di ﬀerent NPSOI and di ﬀerent PNPI.
M. Li, et al. Fuel 250 (2019) 218–234
230

<!-- PDF_PAGE: 14 -->

the comparison between Figs. 23 and 24, regions with high soot con-
centrations only appear at those with low OH concentrations. Ad-
ditionally, at higher PNPI, the more adequate di ﬀusion of natural will
result in more su ﬃ cient use of oxygen, subsequently, the oxygen in the
regions below the cylinder head and at the bottom of the combustion
chamber could participate in the combustion process, leading to lower
possibility of soot formation.
As also shown in Fig. 22a, soot emissions illustrate relatively smaller
variations with NPSOI at relatively small PNPI while experienced ob-
viously larger variations at larger PNPI. This is because at relatively
smaller PNPI, the local rich regions are less a ﬀected by NPSOI; as can be
seen in Fig. 25a, the mass fraction with equivalence ratio higher than
1.2 di ﬀers slightly with each other at PNPI of 10%, leading to smaller
variations of soot emissions with the change of NPSOI. This can be
conﬁrmed by the soot mass traces at PNPI of 10% in Fig. 26a, in which
the peak values for the traces of soot mass changes in a smaller range
with NPSOI. As PNPI increases to 50%, the mass fraction with
equivalence ratio of 0– 0.4 and 1.6 –2.0 decreases while the mass frac-
tion with equivalence ratio of 0.4 –1.2 increases ( Fig. 25b); moreover, as
also demonstrated by Fig. 25b, at 50°BTDC, the mass fraction with
equivalence ratio higher than 1.2 is the lowest, resulting in the least
soot formation and consequently the lowest soot emission. When PNPI
rises to 70%, the mass fraction with equivalence ratio of 0.4 –0.8 is the
highest and the di ﬀerences of equivalence ratio distribution between
diﬀerent NPSOI are enlarged ( Fig. 25c); moreover, the peak value of in-
cylinder soot mass varies in a wider range ( Fig. 26c), causing obvious
distinctions between soot emissions of di ﬀerent NPSOI; at 50°BTDC, the
formation of soot is mitigated attributed to the lowest mass fraction
with equivalence ratio higher than 1.2, resulting in the lowest peak
value of soot mass and the ﬁnal soot emissions. If all natural gas is
introduced into the cylinder before the pilot fuel injection (i.e. at PNPI
of 100%), the mass fraction with equivalence ratio higher than 1.2
reduces to very low values ( Fig. 25d), suggesting that soot formation at
this condition is abated. Besides, it can be seen from Fig. 26 that at PNPI
of 10%, 50% and 70%, the peak values of soot mass appear at the
combustion process of natural gas, indicating that natural gas is the
main source of soot emissions; however, when PNPI rises to very high
value, such as 100%, the peak values of in-cylinder soot mass appear at
the combustion process of pilot diesel; at this condition, the oxidation of
soot after 10°BTDC is vital for the elimination of soot emission
(Fig. 26d); at NPSOI of 90°BTDC and 110°BTDC, the mass fraction with
equivalence ratio of 0.4 –0.8 is higher than 90%, which means the
natural gas/air mixture is highly homogenous and not favorable for
soot production( Fig. 25d). In addition, it can be found that soot emis-
sions are generally lower at higher PNPI due to the more su ﬃ cient
mixing of natural gas and air, only at 30°BTDC and 50°BTDC, soot
emissions of 100% PNPI are larger than those of 90% PNPI as a result of
the much delayed combustion phasing, the subsequent slower oxida-
tion.
5.2.
Eﬀects of EGR
When evaluating the e ﬀects of EGR in this section, the intake
pressure was raised to maintain the total amount of oxygen. The se-
lection of the cases at di ﬀerent PNPI is based on the results in Section
5.1, which means the combinations of PNPI and NPSOI in this section is
30
45
60
75
90
105Cylinder pressure(bar)
Crank angle(°CA)
EGR fraction
 0%
 5%
 10%
 15%
 20%
 25%
PNPI 30%, NPSOI 50°BTDC 30
45
60
75
90
105
Cylinder pressure(bar)
Crank angle(°CA)
PNPI 50%,NPSOI 50°BTDC
EGR fraction
 0%
 5%
 10%
 15%
 20%
 25%
) b () a (
30
45
60
75
90
105
120Cylinder pressure(bar)
Crank angle(°CA)
PNPI 70%,NPSOI 110°BTDC
EGR fraction
 0%
 5%
 10%
 15%
 20%
 25%
-20 -10 0 10 20 30 40 -20 -10 0 10 20 30 40
- 2 0 - 1 00 1 02 03 04 0 - 2 0 - 1 00 1 02 03 04 0
30
40
50
60
70
80
90
Cylinder pressure(bar)
Crank angle(°CA)
PNPI 100%,NPSOI 130°BTDC
EGR fraction
 0%
 5%
 10%
 15%
 20%
 25%
(c) (d)
Fig. 27. Eﬀects of EGR on cylinder pressure.
M. Li, et al. Fuel 250 (2019) 218–234
231

<!-- PDF_PAGE: 15 -->

the optimized ones with better general performance of ITE and emis-
sions. As can be seen from Fig. 27, the pressure before the ignition of
pilot fuel raises with the increase of EGR fraction. However, the peak
cylinder pressure rises with the increase of EGR fraction at PNPI of 30%
and 100% while decreases with the increase of EGR fraction at PNPI of
50% and 70%. This can be explained by the competing e ﬀects between
the increased compression pressure and the slowed down heat release
(Fig. 28 ). It should also be noted that at smaller PNPI, the cylinder
pressure during the late combustion stage di ﬀers slightly from each
other; nevertheless, at PNPI of 100%, the cylinder pressure exhibits
much smaller values during the late combustion stage attributed to the
deteriorated ﬂame propagation and the subsequent incomplete com-
bustion.
Fig. 29 provides the variation of NOx emissions with EGR fraction at
0
80
160
240
320
400
PNPI 30%, NPSOI 50°BTDC
Heat release rate(J/°CA)
Crank angle(°CA)
EGR fraction
 0%
 5%
 10%
 15%
 20%
 25%
0
80
160
240
320
400
480
560
PNPI 50%, NPSOI 50°BTDC
Heat release rate(J/°CA)
Crank angle(°CA)
EGR fraction
 0%
 5%
 10%
 15%
 20%
 25%
) b () a (
0
60
120
180
240
300
360
420 PNPI 70%, NPSOI 110°BTDC
Heat release rate(J/°CA)
Crank angle(°CA)
EGR fraction
 0%
 5%
 10%
 15%
 20%
 25%
- 2 0 - 1 00 1 02 03 04 0 -20 -10 0 10 20 30 40
- 2 0 - 1 00 1 02 03 04 0 -20 -10 0 10 20 30 40
0
50
100
150
200
250
300
PNPI 100%, NPSOI 130°BTDC
Heat release rate(J/°CA)
Crank angle(°CA)
EGR fraction
 0%
 5%
 10%
 15%
 20%
 25%
(c) (d)
Fig. 28. Eﬀects of EGR on heat release rate.
0% 5% 10% 15% 20% 25%
0
500
1000
1500
2000
2500
NOx emissions(ppm)
EGR fraction
PNPI/NPSOI
 30%/50°BTDC
 50%/50°BTDC
 70%/110°BTDC
 90%/130°BTDC
 100%/130°BTDC
 NGSI
Fig. 29. Eﬀects of EGR on NOx emissions.
0% 5% 10% 15% 20% 25%
0
500
1000
1500
2000
2500CO emissions(ppm)
EGR fraction
PNPI/NPSOI
 30%/50°BTDC
 50%/50°BTDC
 70%/110°BTDC
 90%/130°BTDC
 100%/130°BTDC
 NGSI
Fig. 30. Eﬀects of EGR on CO emissions.
M. Li, et al. Fuel 250 (2019) 218–234
232

<!-- PDF_PAGE: 16 -->

diﬀerent partially premixed combustion strategies. As can be seen from
the Figure, NOx emissions decreases continuously with the increase of
EGR fraction owing to the lower combustion temperature caused by the
increase proportion of in-cylinder charge with high heat capacity. The
decrease of NOx emissions is more prominent at relatively higher PNPI,
especially at PNPI of 90%. It is also demonstrated in Fig. 29 that the
NOx emissions will be lower than natural gas single injection (NGSI)
combustion mode if EGR fraction reaches 5% at PNPI of 100%, 10% at
PNPI of 30%, 15% at PNPI of 50% and 90%, 20% at PNPI of 70%.
Figs. 30 and 31 give the variation of NOx emissions with EGR
fraction at di ﬀerent partially premixed strategies. As illustrated, CO and
soot emissions tend to be higher at higher EGR fraction. Meanwhile, CO
and soot emissions both increase by a greater percentage with EGR
fraction at PNPI of 90% and 100%. For CO emissions, the values at PNPI
of 90% and 100% will exceed those of PNPI of 50% and 70% due to the
lowered ﬂame temperature and the consequently deteriorated com-
bustion completeness. For soot emissions, the values at PNPI of 90%
and 100% will not reach a level higher than that of the relatively lower
PNPI when EGR fraction changes from 0% to 25% as a result of the
obvious lower initial values at EGR fraction of 0%. Additionally, as can
be deduced from Figs. 30 and 31, the CO and soot emissions of the
selected partially premixed strategies at di ﬀerent EGR fractions main-
tained lower than those of the NGSI combustion strategy due to the
more homogenous fuel/air mixture.
Fig. 32 gives the variation of ITE with EGR fraction at di ﬀerent
partially premixed strategies. As shown in the Figure, ITE decreases
monotonously with the increase of EGR fraction owing to the delayed
combustion phasing and the increased formation of partial oxidation
products. At PNPI of 90% and 100%, the ITE is more sensitive to EGR
fraction due to the smaller concentration gradient of the natural gas/air
mixture, which means the ﬂame propagation of natural gas is more
aﬀected by the EGR fraction. In general, at PNPI of 30% and 90%, ITE
will be lower than that of NGSI combustion mode when EGR fraction
reaches 20%; at PNPI of 50% and 70%, ITE keeps higher than that of
NGSI combustion mode; at PNPI of 100%, ITE will be lower than that of
NGSI combustion mode when EGR fraction reaches 10%. It can be
concluded from the results that partially premixed combustion strate-
gies with small PNPI or excessively high PNPI are not adaptable to high
EGR rates.
6. Conclusion
This paper investigates the application of partially premixed com-
bustion mode and also the combined use of partially premixed and EGR
in a direct injection natural gas engine by a 3D model based on a va-
lidated n-heptane/natural gas mechanism. The main conclusions are as
follows:
1. A mechanism for n-heptane/methane/ethane/propane mixtures was
constructed for the chemical kinetic study of direct injection natural
gas engines and validated for its prediction of ignition delay, oxi-
dation process and soot precursor mole fraction. Coupled with this
mechanism, a 3D model was built for a direct injection natural gas
engine and the model is veri ﬁed for the reliable prediction of the
combustion and emission formation process.
2. When partially premixed combustion mode is applied, pressure rise
rate is higher and ITE is improved at most cases, implying that the
appropriate use of partially premixed combustion mode can obtain
better fuel economy, however, higher combustion noise may be
accompanied. The variation of ITE with NPSOI is uncertain at dif-
ferent PNPI while ITE is relatively higher at higher PNPI.
3. Based on the analysis of cell data, contour maps and species fraction
traces, it can be summarized that the application of partially pre-
mixed combustion mode will lead to more su ﬃ cient mixing of the
natural gas and air; consequently, the regions with low equivalence
ratio, high OH concentration and high temperature will be enlarged
with the increase of PNPI; meanwhile, during the combustion pro-
cess, the peak values of the CO and soot fraction traces will be re-
duced along with increases in the peak values of NOx mole fraction
at higher PNPI, resulting in reduced CO and soot emissions with
sacriﬁces in NOx emissions. NPSOI has di ﬀerent
 optimized values
for the control of CO, soot and NOx emissions at di ﬀerent PNPI
owing to the coordination between natural gas injection and in-cy-
linder mixing.
4. The combined use of partially premixed combustion mode and EGR
addition is applied to eliminate the higher NOx emissions of par-
tially premixed combustion mode. It can be summarized from the
results that NOx emissions can be e ﬀectively controlled with in-
evitable increases in CO emissions and soot emissions when EGR is
added. Besides, ITE may become lower than that of NGSI combus-
tion mode if EGR is excessively added at PNPI of 30%, 90% and
100%. Generally, best compromise between fuel economy and
emissions can be achieve at 50% or 70% PNPI with EGR fraction of
25% and 90% PNPI with EGR fraction of 15%.
Acknowledgements
This work was supported by the Science and Technology Research
Project of Colleges and Universities in Hebei Province (QN2016041).
And it was also Supported by National Engineering Laboratory for
Mobile Source Emission Control Technology (NELMS2018A10) and
0% 5% 10% 15% 20% 25%
1E-6
1E-5
1E-4
0.001
0.01
Soot emissions(mg/cycle)
EGR fraction
PNPI/NPSOI
 30%/50°BTDC    50%/50°BTDC
 70%/110°BTDC  90%/130°BTDC
 100%/130°BTDC  NGSI
Fig. 31. Eﬀects of EGR on Soot emissions.
0% 5% 10% 15% 20% 25%
20
25
30
35
40
45
50ITE(%)
EGR fraction
PNPI/NPSOI
 30%/50°BTDC    50%/50°BTDC
 70%/110°BTDC  90%/130°BTDC
 100%/130°BTDC  NGSI
Fig. 32. Eﬀects of EGR on ITE.
M. Li, et al. Fuel 250 (2019) 218–234
233

<!-- PDF_PAGE: 17 -->

Science and Technology Program of Hebei Province (17274006D).
References
[1] Zhang SF, Lee TH, Wu H, Pei JY, Wu W, Liu FS, Zhang CH. Experimental and kinetic
studies on laminar ﬂame characteristics of acetone-butanol-ethanol (ABE) and to-
luene reference fuel (TRF) blends at atmospheric pressure. Fuel 2018;232:755 –68.
[2] Weaver CS. Natural gas vehicles – a review of the state of the art SAE technical
paper 892133 1989 .
[3] Liu SH, Zhou LB, Wang ZY, Ren J. Combustion characteristics of compressed natural
gas/diesel dual-fuel turbocharged compressed ignition engine. Proc Inst Mech Eng
D: J Automob Eng 2003;217(9):833 –8.
[4] Cho Haeng Muk, He Bangquan. Spark ignition natural gas engines – a review.
Energy Convers Manage 2007;48:608 –18. https://doi.org/10.1016/j.enconman.
2006.05.023.
[5] Hill PG, Douville B. Analysis of combustion in diesel engines fueled by directly
injected natural gas. J Eng Gas Turbines Power 2000;122(1):141 –6.
[6] Harrington J, Munshi S, Nedelcu C, et al. Direct injection of natural gas in a heavy-
duty diesel engine. Spring fuels & lubricants meeting & exhibition. Reno: Nevada;
2002.
[7] McTaggart-Cowan GP, Bushe WK, Rogak SN, Hill PG, Munshi SR. PM and NOx
reduction by injection parameter alterations in a direct injected, pilot ignited, heavy
duty natural gas engine with EGR at various operating conditions SAE technical
paper 2005-01-1733 2005 .
[8] McTaggart-Cowan GP, Rogak SN, Munshi SR, Hill PG, Bushe WK. The in ﬂuence of
fuel composition on a heavy-duty, natural-gas direct-injection engine. Fuel
2010;89(3):752–9.
[9] Munshi SR, McTaggart-Cowan GP, Huang J, Hill PG. Development of a partially-
premixed combustion strategy for a low-emission, direct injection high e ﬃ ciency
natural gas engine. ASME 2011 internal combustion engine division fall technical
conference. West Virginia, USA: Morgantown; 2011 .
[10] Zoldak P, Sobiesiak A, Wickman D, Bergin M. Combustion simulation of dual fuel
CNG engine using direct injection of natural gas and diesel. SAE Int J Engines
2015;8(2):846–58.
[11] Mabson CWJ, Faghani E, Kheirkhah P, Kirchen P, Rogak SN, McTaggart-Cowan GP.
Combustion and emissions of paired-nozzle jets in a pilot-ignited direct-injection
natural gas engine. 2016. SAE technical paper 2016-01-0807 .
[12] Faghani E, Kheirkhah P, Mabson CWJ, Mctaggart-Cowan GP, Kirchen P, Rogak S.
Eﬀect of injection strategies on emissions from a pilot-ignited direct-injection nat-
ural-gas engine-Part II: slightly premixed combustion. 2017. SAE technical paper
2017-01-0763.
[13] Metcalfe WK, Burke SM, Ahmed SS, Curran HJ. A hierarchical and comparative
kinetic modeling study of C1 –C2 hydrocarbon and oxygenated fuels. Int J Chem
Kinet 2013;45:638 –75.
[14] Pang B, Xie MZ, Jia M, Liu YD. Development of a phenomenological soot model
coupled with a skeletal PAH mechanism for practical engine simulation. Energy
Fuels 2013;27(3):1699 –711.
[15] Kee RJ, Rupley FM, Miller JA. Chemkin-II: a Fortran chemical kinetics package for
the analysis of gas-phase chemical kinetics (No. SAND-89-8009). Livermore, CA
(USA):
Sandia National Labs.; 1989 .
[16] Zhang Y, Huang Z, Wei L, et al. Experimental and modeling study on ignition delays
of lean mixtures of methane, hydrogen, oxygen, and argon at elevated pressures.
Combust Flame 2012;159(3):918 –31.
[17] Petersen EL, Davidson DF, Hanson RK. Ignition delay times of Ram accelerator CH/
O/diluent mixtures. J Propul Power 1999;15(1):82 –91.
[18] Hu E, Chen Y, Zhang Z, et al. Experimental study on ethane ignition delay times and
evaluation of chemical kinetic models. Energy Fuels 2015;29(7):4557 –66.
[19] Aul CJ, Metcalfe WK, Burke SM, Curran HJ, Petersen EL. Ignition and kinetic
modeling of methane and ethane fuel blends with oxygen: a design of experiments
approach. Combust Flame 2013;160(7):1153 –67.
[20] Lam KY, Hong Z, Davidson DF, Hanson RK. Shock tube ignition delay time mea-
surements in propane/O/argon mixtures at near-constant-volume conditions. Proc
Combust Inst 2011;33(1):251 –8.
[21] Petersen EL, Kalitan DM, Simmons S, Bourque G, Curran HJ, Simmie JM. Methane/
propane oxidation at high pressures: experimental and detailed chemical kinetic
modeling. Proc Combust Inst 2007;31(1):447 –54.
[22] Hartmann M, Gushterova I, Fikri M, Schulz C, Schießl R, Maas U. Auto-ignition of
toluene-doped n-heptane and iso-octane/air mixtures: high-pressure shock-tube
experiments and kinetics modeling. Combust Flame 2011;158(1):172 –8.
[23] Dagaut P, Cathonnet M, Boettner JC. Kinetics of ethane oxidation. Int J Chem Kinet
1991;23(5):437–55.
[24] Marinov NM, Castaldi MJ, Melius CF, Tsang W. Aromatic and polycyclic aromatic
hydrocarbon formation in a premixed propane ﬂame. Combust Sci Technol
1997;128(1–6):295–342.
[25] Bakali AE, Delfau JL, Vovelle C. Experimental study of 1 atmosphere, rich, pre-
mixed n-heptane and iso-octane ﬂames. Combust Sci Technol
1998;140(1–6):69–91.
[26] Richards KJ, Senecal PK, Pomraning E. CONVERGE (v2.4). Madison, WI:
Convergent Science, Inc.; 2017 .
[27] Li MH, Zhang Q, Li GX, Li PX. E ﬀects of hydrogen addition on the performance of a
pilot-ignition direct-injection natural gas engine: a numerical study. Energy Fuels
2017;31(4):4407–23.
M. Li, et al.
Fuel 250 (2019) 218–234
234
