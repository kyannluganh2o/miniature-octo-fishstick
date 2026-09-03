<!-- PDF_PAGE: 1 -->

Full Length Article
Effects of injector structural parameters coupled with injection pressure on 
the combustion and emission performance of commercial HPDI natural 
gas engine
Kaiqiang Yang , Zhongshu Wang
*
, Yiran Chen , Mengjian Li , Yandong Wang , Lan Yang ,  
Dan Wang , Yaodong Du
State Key Laboratory of Automotive Chassis Integration and Bionics, Jilin University, Changchun 130025, China
ARTICLE INFO
Keywords:
HPDI natural gas engine
Injecctor structural parameters
Injection pressure
Combustion
Emissions
ABSTRACT
High-pressure direct injection (HPDI) natural gas engines are a next-generation powertrain technology. They 
provide high efficiency and low emissions for future clean transportation. However, limited in-cylinder mixing 
restricts combustion speed and overall performance. Improving mixture formation is crucial for enhancing 
thermal efficiency and emission control. This study addresses this challenge through coordinated optimization of 
injector geometry and injection pressure. Five injectors with different structural designs were tested on a six- 
cylinder 11.59 L heavy-duty HPDI engine. Experiments were conducted under a medium-to-high load condi -
tion (BMEP ≈ 10.8 bar). The natural-gas injection pressure ranged from 200 to 300 bar with 10 bar intervals. The 
effects of nozzle geometry and injection pressure on combustion and emissions were analyzed. Results show that 
increasing the injector flow area strengthens turbulence and accelerates mixture formation. Moderate dispersion 
improves combustion and reduces HC and CO emissions. Excessive dispersion, however, increases wall 
impingement and unburned hydrocarbons. A narrow spray cone at high pressure enhances heat-release con -
centration and shortens combustion duration. With optimized injector design and higher injection pressure, the 
engine achieved a brake thermal efficiency of 46.85 %, 3.28 % higher than the original engine. HC and CO 
emissions decreased by 0.314 and 0.5 g/kW ⋅ h, while NOx emissions increased by 6.3 g/kW ⋅ h. The results confirm 
that coordinated design and pressure control effectively improve HPDI engine performance.
1. Introduction
The escalating severity of environmental issues, such as global 
warming, has underscored the critical importance of conserving energy 
and reducing carbon emissions [ 1 , 2 ]. Internal combustion engines, 
being the primary power source for road transportation, face stringent 
emission regulations. Natural gas, recognized for its clean combustion, 
high efficiency, and wide availability, is extensively used in commercial 
vehicle engines and demonstrates significant potential for technological 
advancement [ 3 – 7 ]. Most current natural gas engines adopt a port fuel 
injection configuration, where natural gas is thoroughly mixed with air 
in the intake manifold before entering the cylinder and is ignited by a 
spark plug near top dead center, operating in a premixed combustion 
mode. This approach offers notable advantages: combining stoichio -
metric combustion with exhaust gas recirculation (EGR) and a three-way 
catalyst enables compliance with emission standards, while also 
benefiting from relatively low costs and rapid flame propagation [ 5 ]. 
However, it also suffers from significant drawbacks, including high 
pumping losses, elevated thermal loads, and a strong tendency to knock 
under high-load conditions, which constrain further improvements in 
efficiency, power output, and operational stability.
Currently, diesel-ignited high-pressure direct injection (HPDI) nat -
ural gas engines, utilizing in-cylinder high-pressure direct injection 
technology, have achieved breakthroughs in efficiency and significant 
optimization in emission performance while maintaining power output 
comparable to that of diesel engines. Additionally, their transient 
response capability has been markedly improved [ 8 , 9 ]. The key 
distinction in their operational process lies in the intake stroke, where 
only fresh air is introduced, effectively avoiding pumping losses. Near 
the end of the compression stroke, a dual-fuel coaxial injector first de -
livers a pilot amount of diesel into the cylinder. This diesel ignites 
autonomously via compression before top dead center, forming ignition 
nuclei. Subsequently, high-pressure natural gas (typically injected at 
* Corresponding author.
E-mail address: wangzhongshu@jlu.edu.cn (Z. Wang). 
Contents lists available at ScienceDirect
Fuel
journal homepag e: www.else vier.com/loc ate/fuel
https://doi.org/10.1016/j.fuel.2025.138211
Received 9 November 2025; Received in revised form 10 December 2025; Accepted 28 December 2025  
Fuel 413 (2026) 138211 
Available online 30 December 2025 
0016-2361/© 2026 Elsevier Ltd. All rights are reserved, including those for text and data mining, AI training, and similar technologies.

<!-- PDF_PAGE: 2 -->

180 – 300 bar) is injected and ignited by these nuclei, completing the 
combustion process primarily in a diffusion-controlled mode. Major 
advantages include high volumetric efficiency, a diffusion-dominated 
combustion mode that largely avoids knock tendency, and the poten -
tial for further efficiency gains via conventional methods such as 
increasing the compression ratio. By leveraging the flexible control of 
both diesel and natural gas enabled by the dual-fuel coaxial injector, 
HPDI natural gas engines can actively implement multiple advanced 
combustion modes — such as Homogeneous Charge Direct Ignition 
(HCDI), Direct Injection Natural Gas-Diesel Reactivity Combustion (DI- 
NG), and Slightly Premixed Combustion (SPC) — to meet diverse opera -
tional demands [ 10 – 14 ]. This capability fully demonstrates the consid -
erable technological potential and scope for further development of 
HPDI natural gas engines in commercial vehicle applications.
In HPDI natural gas engines, both natural gas and diesel are injected 
into the cylinder in the form of high-pressure jets, which significantly 
enhances in-cylinder turbulent intensity. Therefore, rational design of 
the injector can directly influence the mixture formation process, 
thereby determining the combustion rate and emission levels [ 15 – 17 ]. 
Dong et al. [ 18 ] conducted experiments using port-injected ethanol and 
direct-injected diesel in a single-cylinder diesel engine. Under fixed total 
orifice area and spray angle conditions, they observed that increasing 
the number of holes reduced the peak in-cylinder pressure and pressure 
rise rate while prolonging the combustion duration; however, advancing 
the injection timing mitigated the influence of holes count. Raghu et al. 
[ 19 ] compared the effects of different holes numbers on engine perfor -
mance in a single-cylinder direct-injection diesel engine fueled with 
biodiesel/hydrogen. Their results indicated that hydrogen supplemen -
tation compensated for the combustion deficiencies of biodiesel, while 
the injector structural directly affected key combustion characteristics 
such as spray penetration, droplet size, and mixture formation. Within 
their operating conditions, the 4-holes injector demonstrated the best 
overall performance. Zareei et al. [ 20 ] used simulation software to study 
the influence of holes number on heat transfer coefficient and in- 
cylinder pressure in a diesel/hydrogen engine. Their key conclusion 
revealed that the heat transfer coefficient peaked concurrently with 
maximum in-cylinder pressure, and an increase in the number of holes 
influenced fuel penetration and evaporation rates, leading to a reduction 
in both heat transfer coefficient and in-cylinder pressure. Lu et al. [ 21 ] 
employed simulation tools to investigate the impact of holes number and 
pilot injection timing on a diesel/methanol dual-fuel engine. Their 
findings highlighted that the number of holes significantly affected the 
development of high-temperature zones during combustion. In their 
study, the 9-holes injector achieved the highest combustion efficiency, 
and when combined with an appropriate pilot injection strategy, it 
enabled comprehensive optimization of combustion and emission 
performance.
Increasing the injection angle can effectively mitigate jet deflection 
and the associated Coanda effect; however, an excessively large injec -
tion angle may also adversely affect the mixture formation process 
[ 22 , 23 ]. Drawing on the structural of a dual-fuel coaxial injector, Li et al. 
[ 24 ] developed a simplified simulation model of a four-cylinder diesel- 
ignited methanol dual-fuel engine. Using a three-dimensional simula -
tion model coupled with chemical reaction kinetics, they investigated 
the influence of the number of holes and the injection angle of the dual- 
fuel injector on engine performance. Their results indicated that, within 
the scope of the study, a higher number of holes with smaller diameters 
was more beneficial for fuel economy and emissions, though it corre -
spondingly increased knock intensity and NOx emissions. The influence 
of in-cylinder flow on the injection angle necessitated comprehensive 
consideration of multiple factors. In their study, an injection angle of 10
◦
yielded the best economic and emission performance. Wang et al. [ 25 ] 
studied the effect of injection angle combined with pilot diesel injection 
strategy on the performance of an ammonia/diesel dual-fuel engine. 
Their main conclusions showed that a larger injection angle combined 
with a medium proportion of delayed pilot diesel injection achieved 
optimal economy, while a larger injection angle paired with a higher 
proportion of advanced pilot diesel injection significantly improved 
emission performance. Tian et al. [ 26 ] conducted a simulation study on 
the injection angle in an equivalence-ratio combustion methanol engine. 
Their key results demonstrated that an injection angle of 35
◦
effectively 
formed a stepped stratified mixture, enhancing peak cylinder pressure 
and combustion speed, thereby improving flame propagation and 
combustion efficiency while reducing overall emissions. Zhan et al. [ 27 ] 
used simulation software to model the effect of injection angle on an 
ammonia/diesel dual-fuel engine. Their main findings indicated that 
increasing the injection angle promoted the combustion of residual 
ammonia in the cylinder. In their study, an injection angle of 77.5
◦
with 
60 % ammonia energy share achieved the best economy and signifi -
cantly reduced greenhouse gas emissions. Javad et al. [ 28 ] experimen -
tally investigated the effects of the number of holes, injection angle, and 
injection pressure in a single-cylinder direct-injection diesel engine 
fueled with diesel/hydrogen. Their results revealed a clear positive 
correlation between the number of holes and brake thermal efficiency 
(BTE). Increasing the number of holes and injection pressure led to 
higher NOx emissions but reduced soot emissions. Within the experi -
mental range, the three-holes injector, combined with a 400 bar- in -
jection pressure and a 15
◦
injection angle, delivered the best overall 
performance.
For direct-injection engines, elevated injection pressure directly in -
fluences the penetration distance and turbulent kinetic energy of 
gaseous fuel jets, thereby significantly affecting mixture formation, 
combustion, and emission performance [ 29 – 31 ]. McTaggart-Cowan 
et al. [ 32 ] investigated the effect of injection pressure on the perfor -
mance of a pilot-ignited direct-injection natural gas engine in a single- 
cylinder setup. Their findings indicated that higher natural gas injec -
tion pressure markedly reduced PM and CO emissions under high-load 
conditions, with only a marginal increase in NOx emissions, while 
exhibiting negligible effects at low loads. Through bench testing, Larson 
[ 33 ] examined the influence of injection pressure on a diesel-piloted 
Nomenclature
NO
X
Nitrogen oxides
CO Carbon monoxide
HC Hydrocarbon
CO
2
Carbon dioxide
HPDI High pressure direct injection
HCDI Homogenous charge direct injection
DI-NG Direct injection natural gas and diesel reactivity 
combustion
SPC Slightly premixed combustion
BTE Brake thermal efficiency
HRR Heat release rate
T
DINJ
Injection timing of diesel
T
GINJ
Injection timing of natural gas
BSNO
X
Brake specific nitrogen oxides
BSHC Brake specific hydrocarbon
BSCO Brake specific carbon monoxide
P
NGinj
Natural gas injection pressure
BMEP Brake mean effective pressure
CA Crank angle
CA50 Crank angle at which 50 % of cumulative heat release
CA90 Crank angle at which 90 % of cumulative heat release
COV Cycle-to-cycle variation
K. Yang et al.                                                                                                                                                                                                                                    Fuel 413 (2026) 138211 
2

<!-- PDF_PAGE: 3 -->

direct-injection natural gas engine. The results demonstrated that 
increasing the natural gas injection pressure from 190 bar to 230 bar 
considerably accelerated mixture formation, thus shortening the com -
bustion duration and advancing the combustion phasing. Moreover, 
coupling high injection pressure with a high equivalence ratio further 
optimized emission performance. Xie et al. [ 34 ] employed a combined 
approach using constant-volume combustion cylinder experiments, en -
gine bench tests, and CFD simulations to study the effects of injection 
pressure and injector design on direct-injection engines. Their results 
revealed that matching injection pressure with injector geometry 
effectively balanced spray morphology and mixture quality, leading to 
improved combustion stability and performance. Silviu et al. [ 35 ] con -
ducted experimental research on a single-cylinder diesel-piloted direct- 
injection natural gas engine to evaluate the impact of injection pressure 
and injector configuration. Their key conclusions highlighted that 
gaseous fuel injection pressure substantially influenced dual-fuel engine 
performance: within the 100 – 160 bar range, increasing pressure 
enhanced the combustion rate and brake thermal efficiency (BTE), 
though it also raised NOx emissions. By co-optimizing the injector 
configuration — using a layout with 6 diesel holes and 7 uniformly 
distributed gas holes — combustion stability was improved, achieving a 
30 % reduction in NOx emissions along with controlled methane emis -
sions and a 25 % increase in load capacity. When pressure was optimally 
matched with nozzle geometry, HPDI technology demonstrated the 
potential to reduce NOx emissions by up to 60 % while maintaining 
diesel-like efficiency.
In summary, existing studies have primarily explored the feasibility 
of enhancing combustion through injection-related strategies using 
single liquid or gaseous fuels. Various technical approaches — including 
adjustments to nozzle number, spray angle, injection pressure, 
ultrasonic-assisted supply, injectors spatial modification and combus -
tion chamber optimization — have demonstrated notable improvements 
in combustion performance and emission levels[ 36 – 38 ]. However, these 
investigations have been almost exclusively conducted on single- 
cylinder or four-cylinder passenger car engines. In contrast, commer -
cial heavy-duty HPDI natural gas engines employ a coaxial injector 
capable of delivering high-pressure diesel and natural gas jets simulta -
neously from a single device. Validating and applying these techniques 
within this dual-fuel, high-pressure injection architecture is therefore a 
critical step toward enabling further optimization and fully realizing the 
economic advantages of HPDI engines in heavy-duty applications 
[ 39 – 41 ]. However, experimental studies focusing on these aspects 
remain relatively scarce. Therefore, this work investigates the influence 
of the number of holes and the injection angle of a diesel – natural gas 
coaxial injector, synergized with injection pressure, on the combustion 
and emission characteristics of a high-compression-ratio HPDI engine. 
The findings aim to provide guidance for the design and development of 
dual-fuel coaxial injectors and support the application of HPDI natural 
gas engines.
2. Experimental set-up and scheme
2.1. Exprimental set-up
The test engine was a heavy-duty, diesel-ignited HPDI natural gas 
engine. The main engine parameters are summarized in Table 1 .
Fig. 1 shows a photograph of the engine test bench, which includes 
the test engine, an electric dynamometer, an air flow meter, a natural 
gas flow meter, an in-cylinder pressure sensor, a combustion analyzer, 
an emission analyzer, and multiple temperature and pressure sensors. 
The detailed layout is provided in Fig. 2 , and the specific parameters of 
the test equipment are listed in Table 2 . This study utilizes five sets of 
coaxial dual-fuel injectors with different nozzle geometric parameters. 
For each comparative test, all six cylinders of the engine are equipped 
with injectors of the same configuration, while other boundary condi -
tions are kept consistent. The injector parameters and physical 
photographs are presented in Table 3 . Signals including engine torque, 
speed, power, intake air temperature and pressure, exhaust temperature 
and pressure, temperatures and pressures before and after the inter -
cooler, lubricating oil temperature and pressure, and coolant tempera -
ture and pressure are all acquired by the dynamometer's data acquisition 
system. The in-cylinder pressure data represents the average value of 
200 consecutive working cycles. The pressure signal is measured using a 
Kistler piezoelectric pressure sensor, conditioned through a charge 
amplifier, and subsequently transmitted to the combustion analyzer for 
data acquisition and processing. HC, CO, and NOx emissions are 
measured using a HORIBA MEXA-7100DEGR emission analyzer. The 
measurement principles and accuracies of the analyzers are summarized 
in Table 4 . All test results are based on averaged values from three 
repeated experiments.
2.2. Calculation of combustion parameters
The natural gas energy substitution percentage (PES) is a critical 
boundary condition for dual-fuel engines [ 42 , 43 ]. It is defined as the 
proportion of energy released by natural gas combustion relative to the 
total energy released by all fuels. The calculation formula is as follows: 
PES =
˙m
naturalgas
× H
u
naturalgas
˙m
naturalgas
× H
u
naturalgas
+ ˙m
diesel
× H
u
diesel
(1) 
In the euqation, ˙m
naturalgas 
and ˙m
diesel 
represent the mass flow rates of 
natural gas and diesel, respectively, in kg/h; H
u
naturalgas 
and H
u
diesel 
and 
denote the lower heating values of natural gas and diesel, respectively, 
in MJ/kg. The composition of the LNG used in the experiments has a 
significant influence on engine performance and is essential for ensuring 
Table 1 
Specifications of the test engine.
Specification Value
Engine type In-line-6-cylinder four-stroke water-cooled turbocharged 
inter-cooled type
Bore × stroke/mm 126 × 155
Displacement/L 11.59
Compression ratio 19.5
Rated power/(kW) 353
Rated speed/(r/min) 1900
Maximum torque/ 
(N ⋅ m)
2100
Combustion chamber 
shape
ω
Injection Dual-direct injection
Fig. 1. The engine test bench.
K. Yang et al.                                                                                                                                                                                                                                    Fuel 413 (2026) 138211 
3

<!-- PDF_PAGE: 4 -->

the reproducibility of the results. Accordingly, the compositional anal -
ysis of the LNG fuel employed in this study has been provided, as shown 
in Table 4 . Based on the test report issued by the inspection agency, the 
values adopted in this study are 48.387 MJ/kg and 42.552 MJ/kg, 
respectively.
Using the acquired in-cylinder pressure data from 200 consecutive 
working cycles, the corresponding heat release rate can be derived by 
the following equation [ 44 – 47 ]: 
dQ
net
d θ
=
γ
γ  1
p
dV
d θ
+
1
γ  1
V
dp
d θ
(2) 
γ =
C
p
C
V
(3) 
T =
pV
mR
(4) 
In the equation, 
dQ net
d θ 
represents the heat release rate, p denotes the 
cylinder pressure value, V signifies the cylinder volume where work is 
performed, C
V 
and C
p 
denote the specific heat capacities at constant 
volume and constant pressure respectively, γ is the polytropic exponent, 
and T represents the instantaneous temperature within the cylinder. 
Since the mass of natural gas was much higher than diesel, the physical 
properties of the fuel could be approximated by those of natural gas in 
the calculation process. This study calculates combustion phase angle, 
and other combustion parameters using the aforementioned formula.
2.3. Test conditions
During the experimental investigation, critical boundary conditions 
summarized in Table 5 were selected based on typical heavy-duty 
commercial vehicle operating profiles to systematically elucidate the 
influence of injector structural parameters and natural gas injection 
pressure on combustion and emission characteristics of the HPDI natural 
Fig. 2. Schematic diagram of the engine test bench.
Table 2 
Test equipment.
Equipment Type Precision
Electric dynamometer FCD-1300 Torque: ± 0.2 %F.S 
Speed: ± 5r/min
Air flow meter 20 N150 ± 0.1 %
Natural gas flow meter CMF050 ± 0.35 %
In-cylinder pressure sensor 6052B & 6054C ± 0.6 %F.S
Diesel flow meter CMFG010-S ± 1.25 %
Combustion analyzer AVL BD0331 
Emission analyzer MEXA-7100DEGR 
Table 3 
Emission test method and accuracies.
Parameter Measuring Accuracy
HC emissions Flame ionization detector (FID) ± 1%FS
CO emissions Nondispersive infrared (NDIR) ± 1%FS
NO
X 
emissions Chemiluminescent detector (CLD) ± 1%FS
Table 4 
LNG component detection report.
Component Unit Test results
Methane % 94.7
Ethane % 4.07
Propane % 0.30
Isobutane % 0.03
N-butane % 0.07
Neopentane % 0.04
Isopentane % 0.03
N-pentane % 0.01
Heavier hydrocarbons % 0.10
Oxygen % 0.12
Nitrogen % 0.53
K. Yang et al.                                                                                                                                                                                                                                    Fuel 413 (2026) 138211 
4

<!-- PDF_PAGE: 5 -->

gas engine. The engine was operated steadily at 1200 rpm and 1000 N ⋅ m 
using an electric dynamometer in constant-speed and constant-torque 
mode. The operating speed of 1200 r/min selected in this study corre -
sponds to the most frequently used condition in real-world applications. 
Therefore, this operating point was chosen to better reflect practical 
usage and to highlight the advantages of HPDI natural gas engines in 
terms of fuel economy and emissions performance. A load of 1000 N ⋅ m 
was selected primarily due to the constraints associated with the test 
engine. The engine used on the test bench has a compression ratio of 
19.5, which results in relatively high in-cylinder peak pressures under 
high-load conditions. The steel piston is designed for a maximum 
permissible pressure of 180 bar, and mild knock phenomena were 
observed near this limit. Thus, to ensure operational safety during 
testing, a load of 1000 N ⋅ m was chosen as it remains within the safe 
operating range while still providing representative high-load charac -
teristics. The PES serves as a key boundary parameter for fuel supply in 
HPDI engines. According to China VI emission regulations for com -
mercial vehicles, the energy substitution ratio of the primary fuel must 
not fall below 95 %. Since diesel, as the pilot fuel, has a decisive influ -
ence on engine stability, maintaining PES at 95 % ensures the reliability, 
validity, and reproducibility of the research conclusions.Owing to the 
high compression ratio of the test engine, which increased knock pro -
pensity and peak in-cylinder pressure approaching the mechanical limits 
of the piston, the conventional diffusion-dominated combustion mode 
was adopted to ensure operational safety and accuracy, with diesel in -
jection timing (T
DINJ
) set at 17
◦
CA BTDC and natural gas injection 
(T
GINJ
) at 12
◦
CA BTDC.
To ensure rapid in-cylinder injection and sufficient combustion of 
natural gas, the lower limit of natural gas injection pressure was set at 
200 bar based on experimental results, while the upper limit was 
determined as 300 bar considering the safety constraints of the natural 
gas supply system and connecting pipelines; moreover, a pressure 
adjustment step size of 10 bar was adopted to guarantee precise control 
during testing. Five coaxial injectors with different configurations were 
fabricated for the experiments, as summarized in Table 5 : the 8-hole -
s – 72
◦
, 9-holes – 72
◦
, 9-holes – 73.5
◦
, 9-holes – 75
◦
, and 10-holes – 72
◦
in -
jectors. Table 6 presents the detailed structural parameters of the five 
injectors, together with the main view and sectional view of the in- 
cylinder configuration visualized using three-dimensional modeling 
software.
3. Results and discussion
3.1. Effect of injector structural parameters coordinate injection pressure 
on engine economy
Fig. 3 illustrates the combined influence of injector structural pa -
rameters and injection pressure on the engine ’ s economic performance 
under the tested operating conditions. As shown, the number of holes 
has a considerable impact on BTE. The 9-holes injector exhibits superior 
BTE across various injection pressures. The BTE values of the 8- and 10- 
holes injectors are comparable; however, the 8-holes injector shows 
higher sensitivity to injection pressure and achieves relatively high BTE 
at elevated injection pressure. The injection angle has a relatively minor 
effect on BTE. Nevertheless, the 72
◦
coaxial injector demonstrates better 
compatibility under high natural gas injection pressure, yielding the 
optimal thermal efficiency of approximately 46.85 %. For all injector 
configurations, increasing the natural gas injection pressure consistently 
improves BTE. This trend can be attributed to the synergistic effect of 
injector design and injection pressure, which alters the dynamic char -
acteristics of the fuel jet — directly increasing the fuel – air contact area 
and jet interaction intensity — and indirectly enhances in-cylinder tur -
bulence through the penetration and breakup of large-scale vortices and 
shear layer instability induced by high-momentum fuel jets [ 27 – 33 , 48 ]. 
These results confirm that optimizing injector design coupled with high 
Table 5 
Test conditions.
Speed 
(rpm)
Load 
(N ⋅ m)
BMEP 
(bar)
T
DINJ 
(
◦
CA BTDC)
T
GINJ 
(
◦
CA BTDC)
PES 
(%)
1200 1000 10.8 17 12 95
Table 6 
Injector parameters.
Case type Case 1 Case 2 Case 3 Case 4 Case 5(original)
Parameters Nozzle holes = 8 
Injection angle = 72
◦
Nozzle holes = 9 
Injection angle = 72
◦
Nozzle holes = 9 
Injection angle = 73.5
◦
Nozzle holes = 9 
Injection angle = 75
◦
Nozzle holes = 10 
Injection angle = 72
◦
Main view
Sectional view
Fig. 3. BTE of different injectors and natural gas injection pressures.
K. Yang et al.                                                                                                                                                                                                                                    Fuel 413 (2026) 138211 
5

<!-- PDF_PAGE: 6 -->

injection pressure can effectively improve engine economic 
performance.
3.2. Effect of injector structural parameters coordinate injection pressure 
on engine emissions
Fig. 4 illustrates the synergistic effects of injector structural param -
eters and natural gas injection pressure on emission performance. 
Overall, the influence of injection angle exhibits differentiated charac -
teristics: for BSNOx, the 72
◦
injectors yields significantly higher NOx 
emissions across all pressure levels compared to the 73.5
◦
and 75
◦
configurations; for BSHC emissions, within the 200 – 230 bar range, all 
three injection angles result in similar BSHC levels, with the 75
◦
in -
jectors showing relatively lower values, while at 240 – 270 bar discern -
ible differences emerge with BSHC increasing in the order 75
◦
< 72
◦
<
73.5
◦
, and at 280 – 300 bar the order becomes 72
◦
< 75
◦
< 73.5
◦
; for 
BSCO emissions, the 72
◦
injectors generally produce lower BSCO across 
all pressures compared to the 73.5
◦
and 75
◦
injectors. When using in -
jectors with different injection angles, the influence of injection pressure 
remains broadly consistent: with increasing pressure, BSNOx and BSHC 
show a clear upward trend, while BSCO decreases correspondingly.
Overall, the influence of holes number on emission performance 
exhibits distinct differentiated characteristics: for BSNOx, the 9-holes 
injectors produce significantly higher emissions across all pressure 
levels compared to the 8-holes and 10-holes injectors, with the 8-holes 
and 10-holes configurations showing similar BSNOx levels — though 
the 8-holes injectors are relatively higher; for BSHC, emissions increase 
in the order 9-holes < 8-holes < 10-holes, and the BSHC generated by 
the 10-holes injectors are markedly higher than that of the 8-holes and 9- 
holes injectors; for BSCO, the 9-holes injectors achieves significantly 
lower emissions than the 8-holes and 10-holes injectors. Furthermore, 
the impact of injection pressure on emission performance varies slightly 
with different holes numbers: as injection pressure gradually increases, 
BSNOx shows a pronounced upward trend, and BSHC rises slightly; 
Fig. 4. Emissions of different injectors and natural gas injection pressures.
K. Yang et al.                                                                                                                                                                                                                                    Fuel 413 (2026) 138211 
6

<!-- PDF_PAGE: 7 -->

BSCO remains essentially unchanged with the 8-holes injectors, in -
creases marginally with the 10-holes injectors, and decreases slightly 
with the 9-holes injectors.
3.3. Effect of injector structural parameters coordinate injection pressure 
on combustion process
Comparative analysis of Fig. 5 -(b), 5-(c), and 5-(d) reveals the in -
fluence of injection angle coupled with injection pressure on in-cylinder 
pressure and heat release rate during the engine combustion process. 
Regarding in-cylinder pressure, the 72
◦
injectors consistently yield 
higher overall pressure levels compared to the 73.5
◦
and 75
◦
injectors, 
with the latter two exhibiting similar pressure characteristics. As natural 
gas injection pressure increases from 200 bar to 300 bar, in-cylinder 
pressure demonstrates a corresponding upward trend, with peak com -
bustion pressures rising from 152.71 bar, 141.17 bar, and 141.02 bar to 
165.95 bar, 160.20 bar, and 160.98 bar for the 72
◦
, 73.5
◦
, and 75
◦
in -
jectors, respectively. Local magnification details indicate that the 72
◦
injectors ’ pressure response to increasing injection pressure is slightly 
less pronounced than that of the 73.5
◦
and 75
◦
configurations. In terms 
of heat release rate, the 72
◦
and 73.5
◦
injectors achieve similar peak 
values, both exceeding that of the 75
◦
injectors, while the 72
◦
injectors 
produce a more concentrated heat release curve and significantly faster 
combustion velocity. With injection pressure elevated from 200 bar to 
300 bar, the heat release rates intensify markedly — peak values increase 
from 216.00 J/
◦
CA, 198.46 J/
◦
CA, and 202.77 J/
◦
CA to 320.27 J/
◦
CA, 
317.54 J/
◦
CA, and 308.73 J/
◦
CA for the 72
◦
, 73.5
◦
, and 75
◦
injectors, 
respectively.
Comparative analysis of Fig. 5 -(a), 5-(b), and 5-(e) reveals the in -
fluence of holes number coupled with injection pressure on in-cylinder 
pressure and heat release rate during the combustion process. 
Regarding in-cylinder pressure, the 9-holes injectors yield higher overall 
pressure levels compared to the 8-holes and 10-holes configurations, 
with the latter two exhibiting similar pressure characteristics. As natural 
gas injection pressure increases from 200 bar to 300 bar, the peak 
combustion pressure for the 8-holes, 9-holes, and 10-holes injectors rises 
Fig. 5. In-cylinder pressure and HRR of different injectors and natural gas injection pressures.
K. Yang et al.                                                                                                                                                                                                                                    Fuel 413 (2026) 138211 
7

<!-- PDF_PAGE: 8 -->

from 143.01 bar, 152.71 bar, and 143.10 bar to 157.85 bar, 165.95 bar, 
and 158.66 bar, respectively. In terms of heat release rate, the 8-holes 
and 9-holes injectors achieve similar peak values, both significantly 
higher than that of the 10-holes injectors, while the heat release curve of 
the 9-holes injectors is more concentrated with a faster combustion rate. 
With injection pressure elevated from 200 bar to 300 bar, the peak heat 
release rates increase markedly from 201.38 J/
◦
CA, 216.00J/
◦
CA, and 
200.89 J/
◦
CA to 318.76 J/
◦
CA, 320.27 J/
◦
CA, and 281.75 J/
◦
CA for the 
8-, 9-, and 10-holes injectors, respectively.
3.4. Effect of injector structural parameters coordinate injection pressure 
on in-cylinder temperature
Fig. 6 presents the variation of in-cylinder temperature histories of 
different injector configurations and injection pressures. The influence 
of injection cone angle shows a comparable trend: narrower cone angles 
concentrate the gas jets toward the cylinder center, generating higher 
localized temperatures and stronger turbulent kinetic energy. At 300 
bar, the 72
◦
injector yields a peak temperature about 70 – 100 K higher 
than the 73.5
◦
and 75
◦
cases, confirming that an appropriate narrowing 
of the injection angle strengthens the core reaction zone and promotes 
complete oxidation. However, excessive temperature concentration in 
the main combustion zone also corresponds to increased thermal NOx 
formation, consistent with the BSNOx trends observed earlier.
The comparison of in-cylinder temperature histories of different 
injector-holes numbers and injection pressures reveals that the struc -
tural configuration exerts a significant influence on the thermal evolu -
tion within the combustion cylinder. Generally, the 9-holes injectors 
Fig. 6. In-cylinder temperature of different injectors and natural gas injection pressures.
K. Yang et al.                                                                                                                                                                                                                                    Fuel 413 (2026) 138211 
8

<!-- PDF_PAGE: 9 -->

exhibit the highest in-cylinder temperature throughout the combustion 
process, while the 8-holes and 10-holes injectors show comparatively 
lower peak values. This indicates that the 9-holes configuration provides 
an optimal balance between jet momentum and spatial fuel distribution, 
facilitating stronger turbulence and more complete combustion. With 
increasing injection pressure, all injector configurations experience a 
noticeable rise in temperature and an earlier occurrence of the tem -
perature peak, reflecting accelerated mixture formation and intensified 
heat release.
3.5. Effect of injector structural parameters coordinate injection pressure 
on combustion phase
Comparative analysis of Fig. 7 -(b), 7-(c), and 7-(d) reveals the in -
fluence of injection angle coupled with injection pressure on combustion 
phasing in the engine cylinder. As shown, the combustion initiation 
remains largely consistent across different injection angles due to the 
HPDI combustion mode, where ignition is primarily governed by in -
jection timing. Specifically, at the injection pressure of 300 bar, the 
combustion initiation points for the 72
◦
, 73.5
◦
, and 75
◦
injectors are 
2.2
◦
CA ATDC,  1.9
◦
CA ATDC, and  2.35
◦
CA ATDC, respectively. 
Owing to the intense in-cylinder turbulence during early combustion 
that dominates mixture homogenization, the corresponding combustion 
Fig. 7. Combustion phases of different injectors and natural gas injection pressures.
K. Yang et al.                                                                                                                                                                                                                                    Fuel 413 (2026) 138211 
9

<!-- PDF_PAGE: 10 -->

centers occur at 3.5
◦
CA ATDC, 4
◦
CA ATDC, and 3.8
◦
CA ATDC, while the 
combustion endpoints are 29.5
◦
CA ATDC, 32.75
◦
CA ATDC, and 
36.75
◦
CA ATDC, respectively. This behavior is attributed to the nar -
rower injection angle under high injection pressure, which helps 
maintain high penetration of the natural gas jet, concentrating fuel in 
core regions of tumble flow such as the combustion cylinder center. This 
promotes the conversion of kinetic energy of the jet into turbulent en -
ergy, thereby accelerating the combustion rate. As injection pressure 
increases from 200 bar to 300 bar, all combustion phases advance 
significantly: the combustion initiation for the 72
◦
, 73.5
◦
, and 75
◦
in -
jectors shifts from  0.65
◦
CA ATDC to  2.2
◦
CA ATDC, from  0.75
◦
CA 
ATDC to  1.9
◦
CA ATDC, and from  0.7
◦
CA ATDC to  2.35
◦
CA ATDC, 
respectively; the combustion centers advance from 7.35
◦
CA ATDC to 
3.5
◦
CA ATDC, from 7.45
◦
CA ATDC to 4
◦
CA ATDC, and from 7.5
◦
CA 
ATDC to 3.8
◦
CA ATDC; and the combustion endpoints advance from 
35.3
◦
CA ATDC to 29.5
◦
CA ATDC, from 37.95
◦
CA ATDC to 32.75
◦
CA 
ATDC, and from 40.2
◦
CA ATDC to 36.75
◦
CA ATDC.
Comparative analysis of Fig. 7 -(a), 7-(b), and 7-(e) reveals the in -
fluence of holes number coupled with injection pressure on in-cylinder 
combustion phasing. As shown, increasing the number of nozzle holes 
enhances spray atomization and accelerates mixture formation and 
ignition kernel development, resulting in slightly advanced combustion 
initiation. At the injection pressure of 300 bar, the combustion initiation 
points for the 8-holes, 9-holes, and 10-holes injectors are  1.65
◦
CA 
ATDC,  2.2
◦
CA ATDC, and  2.55
◦
CA ATDC, respectively; the corre -
sponding combustion centers occur at 4.75
◦
CA ATDC, 3.5
◦
CA ATDC, 
and 3.9
◦
CA ATDC; and the combustion endpoints are 34.25
◦
CA ATDC, 
29.5
◦
CA ATDC, and 34.25
◦
CA ATDC. This behavior is primarily attrib -
uted to the strong influence of turbulent intensity on the main com -
bustion phase velocity. The 9-holes injectors achieve a more balanced 
mixture formation and concentration distribution, maximizing the tur -
bulent flame area and resulting in faster combustion. As injection 
pressure increases from 200 bar to 300 bar, all combustion phases 
advance significantly: combustion initiation shifts from  0.55
◦
CA 
ATDC to  1.65
◦
CA ATDC for the 8-holes injectors, from  0.65
◦
CA 
ATDC to  2.2
◦
CA ATDC for the 9-holes injectors, and from  0.8
◦
CA 
ATDC to  2.55
◦
CA ATDC for the 10-holes injectors; combustion centers 
advance from 7.9
◦
CA ATDC to 4.75
◦
CA ATDC, from 7.35
◦
CA ATDC to 
3.5
◦
CA ATDC, and from 7.6
◦
CA ATDC to 3.9
◦
CA ATDC, respectively; 
and combustion endpoints advance from 38.85
◦
CA ATDC to 34.25
◦
CA 
ATDC, from 35.3
◦
CA ATDC to 29.5
◦
CA ATDC, and from 40.95
◦
CA ATDC 
to 34.25
◦
CA ATDC.
3.6. Effect of injector structural parameters coordinate injection pressure 
on combustion stability
COV is a key metric for evaluating combustion stability and overall 
engine performance. Fig. 8 illustrates the COV of different injector 
configurations and injection pressures. For all injectors, the COV re -
mains below 3 %, indicating stable combustion across the entire test 
matrix; nevertheless, clear differentiation exists among the configura -
tions. As injection pressure increases, the COV IMEP initially decreases 
and then slightly rises beyond 280 bar. The initial decline reflects 
improved penetration and atomization, which reduce cycle-to-cycle 
variations in the early combustion phase. With respect to spray cone 
angle, the 72
◦
configuration achieves the lowest mean COV, confirming 
its superior compatibility between penetration and mixture uniformity. 
In contrast, the 75
◦
injector produces slightly higher fluctuations due to 
weaker in-cylinder entrainment near the ignition region.
The 9-holes injector demonstrates the best overall stability, with 
COV IMEP values of 1.2 – 1.5 % across 200 – 300 bar, while the 8-holes 
and 10-holes injectors exhibit relatively higher fluctuation levels of 
1.8 – 2.4 % and 2.1 – 2.6 %, respectively. The superior stability of the 9- 
holes injector originates from its well-balanced jet momentum distri -
bution, which enhances mixture homogeneity and ensures consistent 
ignition kernel development cycle-to-cycle. However, at excessively 
high pressures, intensified jet impingement and local over-lean regions 
induce marginal instability, particularly for the 10-holes injector.
4. Conclusion and outlook
4.1. Conclusion
This study investigates the influence of injector structural parame -
ters coupled with injection pressure on a six-cylinder heavy-duty HPDI 
natural gas engine under a typical operating condition of 1200 r/min- 
10.8 bar with the PES of 95 %. Five injector configurations — 8-hole -
s – 72
◦
, 9-holes – 72
◦
, 9-holes – 73.5
◦
, 9-holes – 75
◦
, and 10-hole -
s – 72
◦
— were tested; the main findings are summarized as follows:
1.The economic performance of the HPDI natural gas engine is 
strongly affected by the injector orifice number, with the 9-hole 
configuration showing clear superiority. Increasing injection pressure 
enhanced combustion for all injectors, and the 9-holes – 72
◦
– 30 MPa 
combination achieved the BTE above 46.8 %, demonstrating excellent 
efficiency. These results confirm the feasibility of improving gas-fueled 
engine performance through coordinated optimization of injector 
structure and injection pressure.
2 Emission characteristics corresponded closely to the in-cylinder 
thermal environment. Because NOx formation depends on temperature 
and pressure, injection pressure governed its positive correlation with 
combustion intensity, and the 9-holes-72
◦
injector consistently pro -
duced higher NOx, HC and CO remained low and were largely unaf -
fected by injection pressure, except for the 10-hole 72
◦
injector, whose 
higher emissions were attributed to reduced jet penetration and 
increased wall-quenching.
4.2. Outlook
The aforementioned findings demonstrate that injector configuration 
parameters and injection pressure exert considerable influence on the 
combustion and emission characteristics of HPDI natural gas engines. 
Subsequent research should employ simulation analysis to conduct an 
in-depth investigation of in-cylinder flow field evolution, thereby 
elucidating the synergistic mechanisms through which injector design 
and injection pressure collectively enhance combustion performance in 
such engines.
Fig. 8. COV of different injectors and natural gas injection pressures.
K. Yang et al.                                                                                                                                                                                                                                    Fuel 413 (2026) 138211 
10

<!-- PDF_PAGE: 11 -->

CRediT authorship contribution statement
Kaiqiang Yang: Writing – original draft. Zhongshu Wang: 
Conceptualization. Yiran Chen: Data curation. Mengjian Li: Method -
ology. Yandong Wang: Conceptualization. Lan Yang: Project admin -
istration. Dan Wang: Investigation. Yaodong Du: Conceptualization.
Declaration of competing interest
The authors declare that they have no known competing financial 
interests or personal relationships that could have appeared to influence 
the work reported in this paper.
Acknowledgement
This research was supported by the National Natural Science Foun -
dation of China (NO. 52372383), China; Jilin Province Budget Basic 
Construction Fund (Innovation Capacity Building) Plan (2024C006-4), 
Jilin Province, China.
Data availability
Data will be made available on request.
References
[1] Wang H, Wang X, Ge Y, Wang S, Yang J, Ji C. Analyzing the impact of hydrogen 
direct injection parameters on flow field and combustion characteristics in Wankel 
rotary engines. Energy 2025;319:135004. https://doi.org/10.1016/j. 
energy.2025.135004.
[2] Wang H, Yan G, Jiao H, Liu D, Liu L, Liu M, et al. Effects of spark ignition chamber 
arrangement on combustion characteristics in a hydrogen rotary engine. Energy 
2025;138280. https://doi.org/10.1016/j.energy.2025.138280.
[3] Algayyim SJM, Saleh K, Wandel AP, et al. Influence of natural gas and hydrogen 
properties on internal combustion engine performance, combustion, and emissions: 
a review. Fuel 2024;362(000):25. https://doi.org/10.1016/j.fuel.2023.130844.
[4] Wang Z, Su X, Wang X,et al. Impact of ignition energy on the combustion 
performance of an SI heavy-duty stoichiometric operation natural gas engine. Fuel: 
A journal of fuel science, 2022(Apr.1):313. Doi: 10.1016/j.fuel.2021.122857.
[5] Zhang Q, Xu Z, Li M, et al. Combustion and emissions of a Euro VI heavy-duty 
natural gas engine using EGR and TWC. Journal of Natural Gas Science & 
Engineering 2016:660–71. https://doi.org/10.1016/j.jngse.2015.12.015.
[6] Wang D, Kuang M, Wang Z, et al. Experimental study on the impact of Miller cycle 
coupled EGR on a natural gas engine. Energy 2024;294. https://doi.org/10.1016/j. 
energy.2024.130911.
[7] Khan MI, Yasmeen T, Khan MI, et al. Research progress in the development of 
natural gas as fuel for road vehicles: a bibliographic review (1991–2016). Renew 
Sustain Energy Rev 2016;66:702–41. https://doi.org/10.1016/j.rser.2016.08.041.
[8] Li M, Wu H, Zhang T, et al. A comprehensive review of pilot ignited high pressure 
direct injection natural gas engines: Factors affecting combustion, emissions and 
performance. Renew Sustain Energy Rev 2020;119. https://doi.org/10.1016/j. 
rser.2019.109653.
[9] Ouelette P, Goudie D, Mctaggart-Cowan G. Progress in the development of natural 
gas high pressure direct injection for Euro VI heavy-duty trucks. Springer 
Fachmedien Wiesbaden 2016. https://doi.org/10.1007/978-3-658-12918-7_45.
[10] Munshi SR, Mctaggartcowan GP, Huang J, et al. Development of a Partially- 
Premixed Combustion Strategy for a Low-Emission, Direct Injection High 
Efficiency Natural Gas Engine. Am Soc Mech Eng 2011:515–28. https://doi.org/ 
10.1115/ICEF2011-60181.
[11] Zoldak P, Sobiesiak A, Wickman D,et al. Combustion Simulation of Dual Fuel CNG 
Engine Using Direct Injection of Natural Gas and Diesel.SAE 2015 world congress 
& exhibition: April 21-23, 2015, Detroit, Michigan, USA .2015. Doi: 10.4271/ 
2015-01-0851.
[12] Mctaggart-Cowan GP, Mann K, Huang J, et al. Particulate Matter Reduction from a 
Pilot-Ignited. Direct Injection of Natural Gas Engine 2012. https://doi.org/ 
10.1115/ICEF2012-92162.
[13] Li MH, Zheng XL, Zhang Q, Li ZG, Shen BX, Liu XR. The effects of partially 
premixed combustion mode on the performance and emissions of a direct injection 
natural gas engine. Fuel 2019;250:218–34. https://doi.org/10.1016/j. 
fuel.2019.04.009.
[14] Florea R, Neely GD, Abidin Z,et al.Efficiency and Emissions Characteristics of 
Partially Premixed Dual-Fuel Combustion by Co-Direct Injection of NG and Diesel 
Fuel (DI 2).SAE report, 2016, 000(4):14.Doi: 10.4271/2016-01-0779.
[15] Wang Z, Chen Y, Wang D, et al. Impact of hydrogen-injected parameters on the 
stratified air-fuel mixture formation and combustion of the direct injection 
hydrogen engine. Energy conversion & management 2024(Dec.):321.. https://doi. 
org/10.1016/j.enconman.2024.119083.
[16] Ouellette P. Direct injection of natural gas for diesel engine fueling. 1961.http:// 
hdl.handle.net/2429/4772.
[17] Wei D, Dong Q, Ju C,et al. Simultaneous measurement and analysis of gas needle 
lift and injected rate for HPDI fuel injector. Measurement, 2024:231. Doi: 10.1016/ 
j.measurement.2024.114493.
[18] Dong S, Yang C, Ou B, et al. Experimental investigation on the effects of nozzle- 
hole number on combustion and emission characteristics of ethanol/diesel dual- 
fuel engine. Fuel 2018;217(APR.1):1–10. https://doi.org/10.1016/j. 
fuel.2017.12.024.
[19] Palani R, Subramanian V. Effect of nozzle hole number on performance and 
emissions of dual-fuel diesel engines with juliflora biodiesel blends and hydrogen 
additive. Int J Hydrogen Energy 2025;146:149990. https://doi.org/10.1016/j. 
ijhydene.2025.06.180.
[20] Zareei J, Alvarez JRN. Dataset of the effect of the number of injector holes on the 
heat transfer coefficient and the pressure in the combustion chamber of a 
hydrogen-diesel engine. Data Brief 2024;55:110597. https://doi.org/10.1016/j. 
dib.2024.110597.
[21] Lu Y, Wei M, Wang X,et al. Numerical study of nozzle hole number and pre- 
injection timing effect on combustion and emissions of methanol/diesel dual-fuel 
engine. International Communications in Heat and Mass Transfer, 2025(Feb.):161. 
Doi: 10.1016/j.icheatmasstransfer.2024.108512.
[22] Trusca B. High pressure direct injection of natural gas and hydrogen fuel in a diesel 
engine.2009. http://hdl.handle.net/2429/11481.
[23] Jennings MJ, Jeske FR. Analysis of the Injection Process in Direct Injected Natural 
Gas Engines: Part II—Effects of Injector and Combustion Chamber Design. Journal 
of Engineering for Gas Turbines & Power 1994;116(4):806–13. https://doi.org/ 
10.1115/1.2906889.
[24] Li Z, Wang Y, Yin Z, et al. An exploratory numerical study of a diesel/methanol 
dual-fuel injector: Effects of nozzle number, nozzle diameter and spray spacial 
angle on a diesel/methanol dual-fuel direct injection engine. Fuel 2022;318: 
123700. https://doi.org/10.1016/j.fuel.2022.123700.
[25] Wang Z, Yang C, Zhang F, et al. Effects of diesel injector nozzle angle and split 
diesel injection strategy on combustion and emission characteristics of an 
ammonia/diesel dual-fuel engine. Energy 2024;307. https://doi.org/10.1016/j. 
energy.2024.132686.
[26] Tian Y, Zhu J, Li W, Li W, **ng. Effect of injection angle on combustion and 
emission performance of spark ignition M100 methanol engine in equivalent 
combustion. Energy 2025;324:135876. https://doi.org/10.1016/j. 
energy.2025.135876.
[27] Zhao Z, Miao X, Chen X, et al. Simulation Study of Diesel Spray Tilt Angle and 
Ammonia Energy Ratio effect on Ammonia-Diesel Dual-fuel Engine Performance. 
Energy Eng 2024;121(9). https://doi.org/10.32604/ee.2024.051237.
[28] Zareei J, Prasad KDV, Kareem AK, Chandra S, Shavkatov N, Rodriguez-Benites C, 
et al. Optimizing diesel engine performance and emissions with diesel-hydrogen 
mixtures: Impact of injector configuration, angle, and pressure. Energy Convers 
Manage: X 2024;23:100678. https://doi.org/10.1016/j.ecmx.2024.100678.
[29] Douville, B. (1994). Performance, emissions and combustion characteristics of 
natural gas fueling of diesel engines (Doctoral dissertation, University of British 
Columbia). 1994.https://dx.doi.org/10.14288/1.0080855.
[30] Dumitrescu, S. (1999). Pilot ignited high pressure direct injection of natural gas 
fueling of diesel engines (Doctoral dissertation, University of British Columbia). 
1999.https://dx.doi.org/10.14288/1.0099404.
[31] Ouellette, P. (1992). High pressure injection of natural gas for diesel engine 
fueling (Doctoral dissertation, University of British Columbia). 1992.https://dx. 
doi.org/10.14288/1.0080922.
[32] Mctaggart-Cowan GP, Jones HL, Rogak SN, et al. The Effects of High-pressure 
Injection on a Compression-Ignition, Direct Injection of Natural Gas Engine.ASME 
2005. Internal Combustion Engine Division Fall Technical Conference 2005. 
https://doi.org/10.1115/1.2432894.
[33] Larson, C. R. (2003). Injection study of a diesel engine fueled with pilot-ignited, 
directly-injected natural gas (Doctoral dissertation, University of British 
Columbia). 2003.https://dx.doi.org/10.14288/1.0080985.
[34] Xie, F.,Liang, Z.,Cui, B., Guo,W.,Li,X.,&Jiang,B.,et al. Spray-to-combustion 
interaction in hydrogen direct injection engines: effects of injector structural and 
injection pressure. Energy. Doi: 10.1016/j.energy.2025.137514.
[35] Dumitrescu S, Hill PG, Li G, et al. Effects of injection changes on efficiency and 
emissions of a diesel engine fueled by direct injection of natural gas//SAE. 
International Fuels and Lubricants Meeting and Exposition. 2001 .
[36] Duan R, Zhu Y, Wang H, et al. Evaluating the combustion process of a dual-fuel 
direct-injection engine considering ammonia injectors spatial modification. Appl 
Therm Eng 2025;128971. https://doi.org/10.1016/j. 
applthermaleng.2025.128971.
[37] Zhu J, Niu J, Tian G, et al. Potential improvement in hydrogen spherical flame 
propagation by ultrasonic-fed implementation under lean-burn conditions. Fuel 
2026;405:136816. https://doi.org/10.1016/j.fuel.2025.136816.
[38] Bao J, Wang X, Tian G, et al. Comparative analysis of chamber dimension and 
recess location on combustion behavior in a rotary engine with hydrogen addition. 
Fuel 2026;404:136392. https://doi.org/10.1016/j.fuel.2025.136392.
[39] Yang X, Wang X, Dong Q, Ni Z, Song J, Zhou T. Experimental study on the two- 
phase fuel transient injection characteristics of the high-pressure natural gas and 
diesel co-direct injection engine. Energy 2022;243:123114. https://doi.org/ 
10.1016/j.energy.2022.123114.
[40] Chen G, Wei F, Zhang K, et al. Investigation on combustion characteristics and gas 
emissions of a high-pressure direct-injection natural gas engine at different 
combustion modes. Energ Conver Manage 2023;277:116617. https://doi.org/ 
10.1016/j.enconman.2022.116617.
K. Yang et al.                                                                                                                                                                                                                                    Fuel 413 (2026) 138211 
11

<!-- PDF_PAGE: 12 -->

[41] Dong Q, Li Y, Song E, Yao C, Fan L, Sun J. The characteristic analysis of high- 
pressure gas jets for natural gas engine based on shock wave structural. Energ 
Conver Manage 2017;149:26–38. https://doi.org/10.1016/j. 
enconman.2017.06.015.
[42] Abdelaal MM, Hegab AH. Combustion and emission characteristics of a natural gas- 
fueled diesel engine with EGR. Energ Conver Manage 2012;64:301–12. https://doi. 
org/10.1016/j.enconman.2012.05.021.
[43] Li W, Liu Z, Wang Z. Experimental and theoretical analysis of the combustion 
process at low loads of a diesel natural gas dual-fuel engine. Energy 2016;94: 
728–41. https://doi.org/10.1016/j.energy.2015.11.052.
[44] Li M, Zhang Q, Li G, Shao S. Experimental investigation on performance and heat 
release analysis of a pilot ignited direct injection natural gas engine. Energy 2015; 
90:1251–60. https://doi.org/10.1016/j.energy.2015.06.089.
[45] Li M, Liu G, Liu X, Li Z, Zhang Q, Shen B. Performance of a direct-injection natural 
gas engine with multiple injection strategies. Energy 2019;189:116363. https:// 
doi.org/10.1016/j.energy.2019.116363.
[46] Wang Z, Su X, Wang X, Jia D, Wang D, Li J. Impact of ignition energy on the 
combustion performance of an SI heavy-duty stoichiometric operation natural gas 
engine. Fuel 2022;313:122857. https://doi.org/10.1016/j.fuel.2021.122857.
[47] Sahoo BB, Sahoo N, Saha UK. Effect of engine parameters and type of gaseous fuel 
on the performance of dual-fuel gas diesel engines—A critical review. Renew 
Sustain Energy Rev 2009;13(6–7):1151–84. https://doi.org/10.1016/j. 
rser.2008.08.003.
[48] Wang, B., Xie, F., Li, X.,et al. Optical and simulation investigation of effect of jet- 
wall interaction on combustion performance of methanol pre-chamber turbulent 
jet ignition system. Applied Energy, 385, 125533.Doi: 10.1016/j. 
apenergy.2025.125533.
K. Yang et al.                                                                                                                                                                                                                                    Fuel 413 (2026) 138211 
12
