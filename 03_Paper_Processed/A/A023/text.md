<!-- PDF_PAGE: 1 -->

International Journal of Hydrogen Energy 57 (2024) 904–917
Available online 13 January 2024
0360-3199/© 2024 The Authors. Published by Elsevier Ltd on behalf of Hydrogen Energy Publications LLC. This is an open access article under the CC BY-NC-ND
license (http://creativecommons.org/licenses/by-nc-nd/4.0/).
Split injection strategies for a high-pressure hydrogen direct injection in a 
small-bore dual-fuel diesel engine 
Xinyu Liu, Lynette Yang, Qing Nian Chan, Sanghoon Kook
* 
School of Mechanical and Manufacturing Engineering, The University of New South Wales, Sydney, NSW, 2052, Australia   
ARTICLE INFO  
Handling Editor: Dr Mehran Rezaei  
Keywords: 
Hydrogen direct injection 
Split injection 
Injection timing 
Dual-fuel combustion 
CO
2 
reduction 
Diesel engine 
ABSTRACT  
Hydrogen-diesel dual direct-injection (H2DDI) engines present a promising pathway towards cleaner and more 
efficient transportation. In this study, hydrogen split injection strategies were explored in an automotive-size 
single-cylinder compression ignition (CI) engine, with a focus on varying the injection timings and energy 
fractions. The engine was operated at an intermediate load with fixed combustion phasing through adjustments 
of pilot diesel injection timing. An energy substitution principle guided the variation in energy fraction between 
the two hydrogen injections and then diesel injection while keeping the total energy input constant. The findings 
demonstrate that early first hydrogen injection timings lead to characteristics indicative of premixed combustion, 
reflecting a high homogeneity of the hydrogen-air mixture. In contrast, hydrogen stratification levels were 
predominantly influenced by later second injection timings, with mixing-controlled combustion behaviour 
apparent for very late injections near top dead centre or when the second hydrogen injection held high energy 
fractions, which led to decreased nitrogen oxides (NO
x
: NO and NO
2
) emissions. The carbon dioxide (CO
2
) 
emissions did not show high sensitivity to the hydrogen split injection strategies, exhibiting about 77 % reduction 
compared to the diesel baseline due primarily to increased hydrogen energy fraction of up to 90 %.   
1. Introduction 
Hydrogen has recently gained attention as an alternative for fossil 
fuels to reach the carbon neutrality. It can be produced from electrolysis 
of purified water using renewable electricity sources such as solar and 
wind energy. For its usage, the hydrogen-fuelled internal combustion 
engine (H2ICE) avoids the production of carbon emissions such as un -
burnt hydrocarbons, carbon monoxide and most importantly, carbon 
dioxide (CO
2
). Compared to hydrogen fuel cell, H2ICE offers many 
benefits including a relatively straightforward transition from the 
existing engines and current manufacturing infrastructure, as well as a 
high tolerance to hydrogen impurity and a flexibility to run with other 
fuels [ 1 – 3 ]. 
Earlier studies into H2ICE primarily focused on spark-ignition (SI) 
engines, with the goal of enhancing engine performance and stability by 
utlising the high laminar flame speed and the broad flammability range 
of hydrogen [ 4 ]. These early studies yielded significant improvements in 
engine performance [ 5 – 7 ], where the conventional fuel supply system 
was replaced with a hydrogen fumigation or port injection system to 
generate a premixed hydrogen in the intake manifold before the air 
passes through the intake valves to the combustion chamber [ 8 , 9 ]. The 
port injection was also widely implemented in CI engines using a range 
of alternative fuels such as ammonia [ 10 , 11 ] and methane [ 12 , 13 ] in a 
diesel-piloted dual-fuel mode. However, the use of port injection for 
hydrogen was limited, as backfire, pre-ignition and knock occurred due 
to the low minimum ignition energy and short quenching distance of 
hydrogen [ 14 ]. Additionally, hydrogen displaces air during the intake 
stroke, which results in reduced oxygen intake and an increased work of 
compression. This ultimately leads to a reduction in volumetric effi -
ciency and thus lower engine efficiency/power output [ 1 , 15 ]. 
One way for avoiding the aforementioned limitations of using 
hydrogen in internal combustion engines is direct injection (DI) of 
hydrogen [ 16 ]. Injecting hydrogen after the intake valve closure can 
eliminate backfire and significantly reduce the occurrence of 
pre-ignition [ 1 , 17 – 20 ]. Furthermore, the volumetric efficiency loss that 
occurs from the displacement of air by hydrogen is eliminated. High 
pressure direct injection in SI engines has shown that hydrogen DI en -
ables mixture stratification control via injection timing, which therefore 
achieves high-efficiency at fuel-lean engine operation without deterio -
rating combustion stability [ 21 , 22 ]. Hydrogen DI was also attempted in 
* Corresponding author. 
E-mail address: s.kook@unsw.edu.au (S. Kook).  
Contents lists available at ScienceDirect 
International Journal of Hydrogen Energy 
journal homepage: www.else vier.com/loc ate/he 
https://doi.org/10.1016/j.ijhydene.2024.01.065 
Received 22 August 2023; Received in revised form 22 December 2023; Accepted 6 January 2024

<!-- PDF_PAGE: 2 -->

International Journal of Hydrogen Energy 57 (2024) 904–917
905
a compression-ignition engine in a form of hydrogen-diesel dual direct 
injection [ 23 ]. Using a DI system for hydrogen, it was possible to take 
advantage of the flexibility in hydrogen injection timing, which enabled 
control over the stratification of the hydrogen charge and thus nitrogen 
oxides (NO
x
) emissions – one outstanding air-polluting emission of 
H2ICE. A follow-up study using computational simulations [ 24 ] found 
that earlier hydrogen injection resulted in an almost homogenous 
mixture, leading to dominantly fuel-lean conditions and a largely pre -
mixed combustion process of the fuel. Intermediate injection timings 
were found to cause a moderately stratified mixture with much of the 
hydrogen at near-stoichiometric conditions; this condition resulted in 
the highest engine efficiency, with a corresponding trade-off of 
increased NO
x 
emissions. Finally, late injection timings were found to 
form a highly stratified charge, with fuel-rich mixtures that resulted in 
mixing-controlled combustion. The hydrogen DI was further improved 
by adding a newly designed single-hole nozzle cap to the original 
multi-hole injector [ 25 ], by targeting the hydrogen jet towards the 
piston bowl rather than allowing the fuel to enter in a diffuse cloud. The 
new injection approach reduced combustion near the cylinder walls and 
thus, the associated wall heat losses, achieve 90 % hydrogen combustion 
with only 10 % energy supplied from conventional diesel as pilot. 
Previous studies emphasised the importance of hydrogen mixture 
formation for the control of combustion and NO
x
, which is directly 
related to hydrogen injection strategies. Split injection - where the total 
fuel supplied to the cylinder is split across multiple injections is one 
suggested alternative to single injection, has emerged as a potential 
parameter that may be investigated to optimise engine performance and 
emissions. From previous research performed for various liquid fuels or 
natural gas [ 26 – 30 ], split injection has demonstrated many benefits. For 
example, in the case of split ethanol direct injection in a compression 
ignition engine [ 29 ], an increase in first injection proportion was found 
to cause higher in-cylinder pressure and heat release rate, effectively 
increasing the indicated engine efficiency and reducing the indicated 
specific fuel consumption. Split injection strategies were also 
investigated in a dual-fuel SI engine with gasoline port injection and 
hydrogen direct injection [ 31 ]. With varied hydrogen direct injection 
proportions and second injection timings, the split injection method was 
found to achieve a more controlled stratification of hydrogen compared 
to the single injection counterpart. 
Despite many expected benefits, to date, the literature does not 
provide a detailed understanding of the use of split injection in a direct 
injection compression ignition engine using gaseous hydrogen as the 
fuel supply. In particular, no studies have been performed on the use of 
split injection in a hydrogen-diesel dual direct injection CI engine; thus, 
this study seeks to fill that gap and investigate the impact of split in -
jection on the emissions and performance. While keeping the diesel 
direct injection timing near top dead centre (TDC), hydrogen injection is 
split into two, with first hydrogen injection in the range of 180 to 60 
◦
CA 
before top dead centre (bTDC) and second hydrogen injection between 
90 
◦
CA bTDC and TDC. The hydrogen energy split is also varied. 
Depending on the hydrogen injector type, the diesel injection is maxi -
mised at 30 % or 10 % of the total energy input. For the remaining 70 % 
or 90 % of the hydrogen energy, the first and second injection is equally 
split or varied for their energy fractions. The study measured the in- 
cylinder pressure and engine-out emissions, including NO
x
, smoke, un -
burnt hydrocarbon (uHC), and carbon monoxide (CO), and compared 
them to a reference case of conventional diesel-only operation. 
2. Engine test facility and operation strategy 
2.1. Hydrogen-diesel dual direct injection (H2DDI) engine setup 
A single-cylinder engine modified from a production inline four- 
cylinder diesel engine (Hyundai D4EA series) was used for the H2DDI 
research as illustrated in Fig. 1 a. Only the second cylinder block was 
kept, and the rest was removed while adding needed counter-balance 
mass to the crank shaft to accommodate single-cylinder operation. The 
single-cylinder engine experiments offer an excellent degree of freedom 
Fig. 1a. Schematic diagram of hydrogen-diesel dual direct injection engine setup.  
X. Liu et al.

<!-- PDF_PAGE: 3 -->

International Journal of Hydrogen Energy 57 (2024) 904–917
906
for independent injection control in a wide range of timings and com -
binations of hydrogen and diesel direct injection before new injection 
strategies are tested in multi-cylinder engines. The resulting single- 
cylinder displacement volume is 497.78 cm
3 
with an 83 mm bore and 
92 mm stroke. For the cylinder head, the original four-cylinder head was 
used with only minor modifications such as blocked water jacket holes 
for cylinder 1, 3 and 4. The second cylinder is fitted with the conven -
tional diesel injector and a new hydrogen direct injector, as well as an in- 
cylinder pressure transducer. The engine has no throttle valves and is 
naturally aspirated. The cylinder head has a nominal swirl ratio of 1.4, 
as measured on a steady flow rig. To reduce the pressure oscillations 
from the single-cylinder operation, the intake and exhaust pipes are 
connected to two 60 dm
3 
surge tanks. 
Fig. 1 b shows the engine setup pictures and hydrogen/diesel injector 
arrangements. For diesel direct injection, the engine is equipped with a 
conventional common-rail injection system (Bosch CP3 pump and CRI2 
injector). The nozzle holes have a nominal diameter of 134 μ m, a 
discharge coefficient of 0.86, and a Bosch K-factor of 1.5, with a stan -
dard hydraulic flow rate of 400 cm
3
. This injector was used for a con -
ventional ultra-low sulphur diesel fuel with a minimum cetane number 
of 51. For hydrogen direct injection, a conventional spray-guided gas -
oline direct injector (GDI) with six 160- μ m holes and an included angle 
of 70
◦
was used. The steady flow rate of hydrogen through the GDI 
injector was 1.37 g/s at 20 MPa pressure. The hydrogen injection 
pressure was controlled using a boost pump system (Zenobalti, ZB-1301) 
based on a single-stage, single-acting pneumatic hydrogen pump (Has -
kel, AG-62-86979). No injector failure occurred during the entire testing 
period, suggesting commercial GDI injectors are capable of sealing the 
hydrogen at this high pressure. However, the lubrication of the injector 
needle was needed as it operates without gasoline. This was addressed 
by adding a droplet of engine oil into the injector inlet, which typically 
lasted for a day. No impact of this subtle engine oil addition was 
measured either on combustion or engine-out emissions. 
Detailed illustrations of the two hydrogen injector arrangements are 
shown in Fig. 1 b. One type of injector kept the original nozzle but had a 
ducted channel at the exit of the multi-hole nozzle tip. This cylindrical 
channel is 7.5 mm in diameter and 15.5 mm long. It was expected the 
high-pressure gas jets merge and plume flows into the cylinder before 
making hydrogen-air mixtures as proven in the computational simula -
tions [ 22 ]. Another nozzle type of the present study is a single-hole 
capped nozzle. While using the same conventional GDI, it had a 1-mm 
hole cap welded on the original nozzle. This was to maintain the 
hydrogen gas momentum with a single hydrogen jet directed towards 
the cylindrical-shape piston bowl. From the previous tests, the 
single-hole capped nozzle performed much better with 90 % hydrogen 
energy operation [ 25 ] compared to 50 % hydrogen operation with the 
ducted channel multi-hole injector [ 23 ]. For both injectors, the 
hydrogen injection mass was measured using the Zeuch method; the 
pressure increment resulting from hydrogen injection into a vessel with 
a constant volume of 1.29 dm
3 
was measured using a high-precision 
pressure sensor (Sensys, model PSH, 1 MPa full scale, 0.15 % preci -
sion). Finally and importantly, as hydrogen was injected in a 
high-pressure gaseous state, the flow through the nozzle was choked as 
the pressure ratio across the injector exceeded two [30,32] . Further 
information about the used hydrogen injection system and its applica -
tion to engines is found in a published international patent [ 33 ]. 
2.2. Instruments for engine control and data acquisition 
The engine was equipped with a piezoelectric in-cylinder pressure 
transducer (Kistler 6056A with amplifier 5015A) mounted on the cyl -
inder head to monitor the in-cylinder pressure. The crankshaft position 
was monitored using a high-precision encoder (Autonics, 1800 pulses 
per revolution) and the engine speed was controlled by an eddy current 
Fig. 1b. Engine setup pictures and drawings of the ducted channel multi-hole injector and the single-hole nozzle capped injector installation.  
X. Liu et al.

<!-- PDF_PAGE: 4 -->

International Journal of Hydrogen Energy 57 (2024) 904–917
907
dynamometer (FroudeHoffmann, AG-30HS). A universal engine control 
unit (Zenobalti, ZB-9013P) was used to control the diesel common-rail 
pressure, as well as to adjust the injection timing and duration for 
both diesel and hydrogen direct injectors. Throughout the experiments, 
the engine coolant temperature was maintained at a constant tempera -
ture of 363 K (90 
◦
C) to replicate a warmed-up engine operation. 
The four engine-out emissions, including NO
x 
(NO and NO
2
), smoke, 
carbon monoxide (CO), and unburnt hydrocarbon (uHC) were measured 
during the experiments. A non-dispersive infrared analyser (Testo 
350XL), with an accuracy of 5 %, is used to measure NO
x
, while another 
gas analyser (Horiba Mexa-584L) with 1.7 % accuracy was used to 
measure CO and uHC. To detect the level of exhaust smoke, an 
opacimeter (Horiba Mexa-600L) with an accuracy of 0.15 m
-1 
absorp -
tion was used. 
2.3. Engine operation strategy 
The engine was operated at a constant speed of 2000 revolutions per 
minute (rpm), which corresponds to the maximum torque output of the 
production engine (see Table 1 ). Due to the additional degrees of 
freedom associated with the two fuel injectors, a fuel-substitution 
strategy was implemented for this study. The total energy injected per 
cycle, was maintained at 820 J. As the amount of injected hydrogen was 
increased, the injection duration of diesel fuel was reduced in proportion 
to the energy, and the injection timing was adjusted to ensure that the 
mid-point combustion phasing was kept constant such that the crank- 
angle degree at 50 % chemical energy conversion, denoted as CA50, 
was fixed at 10 ± 0.5 
◦
CA after the top dead center (aTDC). The details 
of the operation strategy are listed in Table 2 . The hydrogen split in -
jection, a main topic of the present study, was performed with varied 
energy fraction of the first and second hydrogen injection. Timings of the 
first and second injections were also varied to evaluate their impact on 
the mixture formation and combustion. 
3. Results and discussion 
3.1. Ducted channel multi-hole hydrogen injector 
The ensemble-averaged in-cylinder pressure and derived apparent 
heat release rate (aHRR) traces are shown in Fig. 2 for varied hydrogen 
split ratios and second injection timings. The first hydrogen injection 
was fixed at early timing of 180 
◦
CA bTDC. In each plot, the results for 
the diesel baseline (black solid lines) are also shown as a reference point. 
With the fixed first injection timing, the varied second hydrogen injec -
tion timing was expected to influence hydrogen mixture stratifications 
significantly. The energy share for the first and second injections are the 
same as noted in the legend. For example, 15/15/70d represents the 
energy share for each of the two hydrogen injections are equal 15 % and 
the remaining 70 % are supplied from diesel. The arrows shown on the 
aHRR traces (bottom left) indicate the diesel injection timing and 
duration chosen for a constant combustion phasing, i.e. CA50 at 10 
◦
CA 
aTDC, as well as a constant energy input of 820 J/cycle. For all three 
tested second hydrogen injection timings, up to 70 % total hydrogen 
energy substitution was achieved without knocking. It is noted the 
previously examined single injection approach using the same ducted 
channel multi-hole hydrogen injector was limited at 50 % total 
hydrogen energy fraction [ 23 ]. The split injection strategy using 
hydrogen direct injection at overall lean hydrogen charge demonstrates 
a significant benefit of increased hydrogen energy fraction via mixture 
control; that is, a blend of more homogenous charge from the first in -
jection and more stratified charge from the second injection led to 
increased use of hydrogen. It is important to mention that the pressure 
fluctuations on some of the pressure traces are caused by the natural 
frequency of the combustion chamber amplified by the recessed pressure 
sensor mount channel, rather than pressure ringing due to knocking. 
For each of the second injection timings, the in-cylinder pressure 
traces show a consistent increase in the end of compression (TDC) 
pressure at a higher hydrogen energy fraction. This higher pressure was 
a result of the increased compression work from the higher amount of 
gaseous hydrogen that was injected during the compression stroke. With 
a 30 % hydrogen energy fraction and the remaining 70 % of energy 
supplied by diesel, the in-cylinder pressure traces of all three hydrogen 
second injection timings are very similar with the diesel baseline. 
However, the peak aHRR is higher than the diesel, which was likely due 
to higher adiabatic flame temperature of hydrogen. Upon further 
increasing the hydrogen fraction to 40 and 50 %, a shorter ignition delay 
was needed to maintain CA50, from a progressively retarded diesel in -
jection for higher hydrogen fraction. Although the peak aHRR for 40 % 
and 50 % hydrogen fractions were expected to be higher than 30 %, they 
are held constant due to this retarded diesel injection. While comparing 
the second hydrogen injection timings at the same energy fraction, it is 
interesting to note that the switch of second hydrogen injection does not 
show a significant change of the magnitude as well as the phasing. 
To evaluate the varied hydrogen energy fraction and second injec -
tion timing altogether, the in-cylinder pressure was further processed for 
engine power output, combustion phasing, and burn duration parame -
ters. Fig. 3 shows net indicated mean effective pressure (IMEP) that was 
calculated from in-cylinder pressure over the complete engine cycle 
including both the power loop and pumping loop, and indicated effi -
ciency which was calculated using known lower heating values of 
Table 1 
Engine and injection system specifications.  
Displacement 497.8 cm
3 
Bore 83 mm 
Stroke 92 mm 
Compression 
ratio 
17.4 (ducted channel injector) and 17.7 (single-hole injector) 
Swirl ratio 1.4 
Piston Top-hat cylindrical bowl (55 mm in diameter) 
Number of 
valves 
2 intake and 2 exhaust 
Injection system Hydrogen direct injector Diesel direct injector 
Pumping system (Zenobalti) 
Boost pump (Haskel AG-62-86979) 
Original injector (Bosch spray- 
guided GDI) 
Number of original holes: 6 
Nominal hole diameter: 160 μ m 
Ducted channel diameter: 6 mm 
Ducted channel length: 12.3 mm 
Nozzle cap single-hole diameter: 1 
mm 
Steady flow rate: 1.37 g/s at 20 
MPa H
2 
pressure 
Common-rail pump 
(Bosch CP3) 
Number of injector holes: 
7 
Nominal hole diameter: 
134 μ m 
Included angle: 150
◦
K-factor: 1.5 
Discharge coefficient: 
0.86 
HFR: 400 cm
3 
for 30 s at 
10 MPa  
Table 2 
Engine operating and fuel injection conditions.  
Engine speed [rpm] 2000 
Intake air pressure [kPa] 101.3 (Natural aspiration) 
Intake air temperature [
◦
C] 27 
Coolant (water) temperature [
◦
C] 90 
Net IMEP [kPa] 500 – 930 kPa 
Fuel Hydrogen Diesel 
Cetane number – 51 
Fuel density at 15 
◦
C [kg/m3] 0.089 848 
Lower heating value [MJ/kg] 119.7 43.4 
Fuel injection pressure [MPa] 20 100 
Combustion phasing [CA50, 
◦
CA aTDC] 10 
Total energy input [J/cycle] 820 
Injection timing [
◦
CA 
bTDC] 
First 180 – 60 12 – 3 
Second 90 – 0 – 
Energy fraction [%] Ducted channel multi-hole 
injector 
60 – 30 10 – 40 30 
Single-hole nozzle capped 
injector 
80 – 10 10 – 80 10  
X. Liu et al.

<!-- PDF_PAGE: 5 -->

International Journal of Hydrogen Energy 57 (2024) 904–917
908
Fig. 2. Effect of equal split H2 energy fraction on in-cylinder pressure and heat release. The results are shown for three selected second H2 injection timings at fixed 
first H2 injection of 180
◦
CA bTDC. The diesel injection duration and timing selected for fixed CA50. SOI = start of injection. 
Fig. 3. Effect of equal split H2 energy fraction on engine performance parameters for varied second H2 injection timings at fixed first H2 injection of 180
◦
CA bTDC.  
X. Liu et al.

<!-- PDF_PAGE: 6 -->

International Journal of Hydrogen Energy 57 (2024) 904–917
909
hydrogen and diesel fuel and measured injected mass per cycle. The 
combustion stability was evaluated using the coefficient of variation of 
IMEP (CoV of IMEP), which was below 3.5 % for all tested conditions. As 
the fuelling rate was constant, the net indicated efficiency simply fol -
lows the net IMEP trends. Combustion phasing including CA10, CA50, 
and CA90 (the crank position corresponding to 10 %, 50 %, and 90 % of 
total heat release, marked by circle, cross, and square, respectively) and 
burn durations including early-phase burn (CA10 – CA50), late-cycle 
burn and total burn duration represented by circle, cross, and square 
are shown on the right side of Fig. 3 . 
Fig. 3 exhibits a consistent decreasing trend in IMEP for higher 
hydrogen energy fractions regardless of the second injection timing. This 
trend was supported by the in-cylinder pressure data, which revealed 
reduced peak and late-cycle pressures, as well as diminished peak aHRR. 
Regarding the second injection timings, the variations are not significant 
with all three injection timings exhibiting the same trend. The com -
bustion phasing, represented by CA50, was optimised at 10 
◦
CA bTDC 
through adjustments in the timing of diesel injection, resulting in similar 
start and end of combustion ( i.e. CA10 and CA90). Therefore, it was 
explained that controlled combustion phasing using the adjusted diesel 
injection timing made a more significant impact than the possible 
mixture stratification variations due to the second hydrogen injection 
timing change. This is consistent with minimal differences noticed from 
the in-cylinder pressure and aHRR profiles in Fig. 2 ; that is, the hydrogen 
energy fraction leads to measurable differences but not the hydrogen 
second injection timing. 
Similar with the in-cylinder pressure/aHRR profiles and power 
output parameters, engine-out emissions shown in Fig. 4 suggest higher 
sensitivity to the hydrogen energy fraction than the second hydrogen 
injection timing. The most significant change in engine-out emissions is 
observed for increased hydrogen energy fraction with continuously 
decreasing CO
2 
and increasing NO
x
. The trade-off characteristics is clear 
that increased use of hydrogen significantly reduces CO
2 
emissions, but 
the higher hydrogen mass aggravates the thermal NO formation. Inter -
estingly, CO shows a similar increasing trend for higher hydrogen en -
ergy fraction. It is noted there are still 30 – 70 % of combustion from 
diesel, which might undergo increased CO due to reaction quenching 
occurring in hydrogen trapped local regions ( e.g. crevice volume). The 
influence of varied second hydrogen injection timing becomes evident 
when engine-out emissions of unburnt hydrocarbon (uHC) is evaluated. 
The overall increasing trend stays the same as CO emissions for 
increased hydrogen fraction, but it is 60 
◦
CA bTDC second injection 
leading to the highest uHC emissions. This was unexpected as NO
x 
emissions show the highest amount among the 3 s injection timings 
tested, albeit the difference is not significant. The cause for the observed 
trend is not entirely clear but it was thought the close interaction of 
second injected hydrogen and diesel pilot fuel led to reaction quenching, 
which could be avoided when the second injection timing was early at 
90 
◦
CA bTDC. When the second injection was further retarded to 40 
◦
CA 
bTDC, the hydrogen was directed into the piston-bowl where the diesel 
pilot flame induced combustion was more complete. Further investiga -
tion is required to better understand complex uHC trends, for example 
using computational simulations [ 24 ]. 
The combustion noise in Fig. 4 was estimated from the in-cylinder 
pressure using the method developed by Shahlari et al. [ 34 , 35 ] with 
respect to engine structure and frequency response in human hearing. 
The results show an overall reduced noise level at a higher hydrogen 
fraction. For diesel dominated combustion (hydrogen fraction less than 
50 % of the total energy), the three different second hydrogen injection 
timings show a similar noise level. However, when the hydrogen frac -
tion is higher than 50 %, a later second hydrogen injection exhibits 
decreased noise. This benefit was due to the increased mixing-limited 
hydrogen combustion as a higher portion of hydrogen was injected at 
a later timing. In other words, the extended combustion period helped 
reduce noise while hydrogen diffusion flames were maintained for later 
crank angles. 
Fig. 4. Effect of equal split H2 energy fraction on engine-out emissions for 
varied second H2 injection timings at fixed first H2 injection of 180
◦
CA bTDC. 
X. Liu et al.

<!-- PDF_PAGE: 7 -->

International Journal of Hydrogen Energy 57 (2024) 904–917
910
From Figs. 1 – 4 where the equal split hydrogen injection methods 
were applied, it was found that the energy fraction from each injection 
plays a more significant role than the injection timings. To examine this 
further, the energy split ratio between two hydrogen injections was 
varied. As shown in Fig. 5 , the first hydrogen injection timing was again 
fixed at 180 
◦
CA bTDC while 90 and 60 
◦
CA bTDC were selected for the 
second injection timing. The second injection of 40 
◦
CA bTDC was 
eliminated for this split ratio variation test, as the long injection dura -
tion for a high hydrogen fraction duration would leave a trapped 
hydrogen in the ducted channel of the injector [ 23 ]. 
As depicted in Fig. 5 , the energy fraction from diesel was fixed at 30 
% while the remaining 70 % are supplied by hydrogen. The energy 
fraction for the first hydrogen injection was varied between 60 % and 30 
% of the total energy. This is noted in the figure legend – e.g. 60/10/30d 
indicates 60 % hydrogen first injection, 10 % hydrogen second injection 
and 30 % diesel injection by energy. For each timing of the second in -
jection, an increased first hydrogen fraction consistently results in a 
higher pressure at the end of compression. Given fixed hydrogen total 
mass, this increased pressure at TDC is a result of compressing more 
hydrogen mass. Compared to the diesel baseline, the pilot diesel injec -
tion had to be delayed to maintain CA50 at 10 
◦
CA aTDC. This once 
again attributes to the high flame speed of hydrogen. With a higher first 
injection fraction, a more premixed hydrogen charge leads to a higher 
peak in-cylinder pressure. For the hydrogen injection timing of 180/90 
◦
CA, the peak aHRR is lower than the diesel baseline, but a broader 
shaped and lower magnitude aHRR profile is measured, meaning that 
the combustion was dominated by a more homogeneous hydrogen 
charge due to higher first injection fraction. When the second hydrogen 
injection timing was delayed to 60 
◦
CA bTDC, the overall magnitudes of 
both the in-cylinder pressure and aHRR increase. This increase is due to 
a shorter mixing time resulting from the second injection, leading to a 
more stratified charge. This is evidenced by a narrower, diesel-like aHRR 
profile. 
For varied first and second hydrogen fraction conditions of Fig. 5 , the 
engine power output, combustion phasing and burn duration results are 
plotted in Fig. 6 . At a higher first hydrogen injection fraction, it was 
expected that a more premixed hydrogen charge would generate a 
higher net IMEP (and higher indicated efficiency) as the in-cylinder peak 
was increased. This is shown clearly in Fig. 6 . Between the two hydrogen 
second injection timings, the later 60 
◦
CA bTDC injection shows higher 
IMEP than the 90 
◦
CA bTDC, which is also consistent with increased in- 
cylinder pressure conditions. This suggests making a homogenous lean 
hydrogen charge made from the early first injection could be mixed with 
a stratified charge with locally rich mixtures to produce higher power 
output. The CoV of IMEP indicates that all the tested conditions produce 
stable combustion with less than 3.3 % variance. Interestingly, the 
combustion phasing and burn duration do not exhibit significant dif -
ferences due either to the varied first/second hydrogen injection fraction 
or the second injection timing, which was primarily due to pilot diesel 
injection timing adjusted to match CA50. However, a trend is observed 
that the burn duration of hydrogen-diesel combustion is much shorter, 
which is due to increased premixed combustion. The higher premixed 
combustion is also evident from an increase in the first hydrogen in -
jection fraction, which tends to decrease the overall burn duration 
(CA10-CA90) to be shortest at 60 % first hydrogen injection fraction. 
Fig. 7 presents the engine-out emissions of CO
2
, NO
x
, CO, and uHC, 
alongside the estimated combustion noise for varied first/second 
hydrogen fraction conditions delineated in Figs. 5 and 6 . For a fixed ratio 
of 70 % hydrogen and 30 % diesel energy feed, it is discerned that an 
increased fraction of the first hydrogen injection corresponds to 
decreased CO
2 
emissions and, conversely, an overall increase in NO
x 
emissions for both tested second hydrogen injection timings. The most 
significant reductions in CO
2 
emissions occur when the first hydrogen 
fraction is maximised to 60 %. With an early injection at 180 
◦
CA aTDC, 
Fig. 5. Effect of H
2 
split ratio on in-cylinder pressure and heat release rate. The results are shown for two selected second H
2 
injection timings at fixed first H
2 
injection of 180
◦
CA bTDC. The total H
2 
energy fraction is held constant at 70 %. 
X. Liu et al.

<!-- PDF_PAGE: 8 -->

International Journal of Hydrogen Energy 57 (2024) 904–917
911
the hydrogen charge was allotted ample time for mixture formation. 
This more premixed charge condition resulted in a higher burning rate 
and thus higher flame temperature to cause increased thermal NO for -
mation; however, higher efficiency engine operation achieved lower 
CO
2 
emissions at fixed total energy input. This is consistent with the 
shortest overall burn duration measured for 60 % first hydrogen injec -
tion in Fig. 6 . It is also corroborated by the observed higher pressure 
( Fig. 5 ) and IMEP ( Fig. 6 ). Remarkably, compared to the diesel baseline, 
the hydrogen injection configuration of 180/60 
◦
CA aTDC with a 60 % 
first injection fraction culminates in a 60 % reduction in CO
2 
emissions. 
Both CO and uHC emissions exhibit a common decreasing trend 
when the fraction of first hydrogen injection increases, suggesting a 
more complete burn due to an increase in charge premixing. The com -
bustion noise also shows the same trend that higher premixed com -
bustion due to higher first hydrogen injection fraction caused increased 
noise. Between the two tested second injection timings of 90 and 60 
◦
CA 
bTDC, the later injection timing resulted in higher noise, which is 
consistent with higher net IMEP and pressure shown previously. The 
mixture formation with a blend of lean homogeneous charge (first in -
jection) and more stratified charge with locally rich mixtures (second 
injection) achieved the highest power output with increased noise as a 
drawback; however, the estimated noise was still below the diesel 
baseline. 
3.2. Single-hole nozzle capped hydrogen injector 
The previous section highlighted the advantages of split hydrogen 
injection to enhance mixture control for the optimised use of hydrogen 
in a hydrogen diesel direct injection compression ignition engine. These 
advantages became more pronounced with a modified design of the 
hydrogen injector, which incorporated a 1 mm single-hole cap to the 
previous 6-hole injector. This improvement effectively prevented 
hydrogen clustering within the ducted channel and enabled the engine 
to derive 90 % of its energy from hydrogen [ 25 ]. The results in this 
section maintain a constant energy input of 820 J/cycle with 90 % en -
ergy fraction from hydrogen, supplemented by 10 % from diesel as pilot 
fuel. It further examines the impacts of hydrogen split injection strate -
gies on hydrogen mixture control using the new injector. 
The results presented in Fig. 8 include the in-cylinder pressure and 
aHRR profiles for varied split ratios between the first and second 
hydrogen injections. For this test, the timing of the first injection was 
consistently set at 180 
◦
CA bTDC to establish a homogeneous hydrogen 
mixture, similar with Fig. 5 in the case of a ducted channel multi-hole 
injector. Conversely, the second injection was varied between 20 and 
0 
◦
CA bTDC to generate different levels of stratification for hydrogen. As 
illustrated in the lower left, the diesel injection timing was adjusted to 
maintain CA50 at 10 ± 0.5 
◦
CA aTDC. 
For the in-cylinder pressure trends, it is evident that an increase in 
Fig. 6. Effect of H
2 
split ratio on engine performance parameters for two selected second H2 injection timings at fixed first H2 injection timing of 180
◦
CA bTDC. The 
total H
2 
energy fraction is held constant at 70 %. 
X. Liu et al.

<!-- PDF_PAGE: 9 -->

International Journal of Hydrogen Energy 57 (2024) 904–917
912
the first hydrogen injection proportion leads to a higher TDC and sub -
sequently a higher peak pressure across all three injection timings. This 
heightened TDC pressure, resulted from a more substantial hydrogen 
mass undergone compression work. Consequently, the larger hydrogen 
mass forms a charge with a higher level of premixing, leading to the 
elevated peak pressure. Specifically, the very early first hydrogen in -
jection timing of 180 
◦
CA bTDC allows a homogeneous hydrogen charge 
to form, due to the prolonged mixing duration. Higher late-cycle in- 
cylinder pressure (occurring after the pressure peak) at greater first in -
jection proportions further supports the evidence of enhanced premixed 
combustion with higher hydrogen homogeneity. As a consequence of 
these factors, the overall aHRR trace displays a higher peak and a 
slightly broader shape as the proportion of the first hydrogen injection 
increases. 
When comparing the injection timings, it becomes evident that an 
earlier second injection timing results in marginally higher peak pres -
sure. For cases where the first injection contains a high hydrogen frac -
tion ( e.g. 80 %), this rise in peak pressure can be attributed to a shift in 
the combustion mode from hydrogen mixing-controlled combustion to a 
more premixed combustion. The aHRR traces in Fig. 8 provide as 
additional evidence for the transition between the combustion modes. 
With an earlier second hydrogen injection timing, the peak aHRR in -
creases due to the extended mixing duration. This contrasts with the 
situation where the second injection occurs very late ( e.g. , at TDC), in 
which case overall lower peak is measured with extended aHRR profile. 
These observations are indicative of the prevalence of mixing-controlled 
combustion when the second injection is delayed. 
Fig. 9 presents results of net IMEP, CoV of IMEP, net indicated effi -
ciency; combustion phasing parameters including CA10, CA50, CA90, as 
well as burn durations for early (CA10 to CA50), late (CA50 to CA90), 
and overall (CA10 to CA90) phases. A positive correlation is observed 
between net IMEP and the first hydrogen injection proportion, indi -
cating that as the initial injection of hydrogen increases, the engine 
power output similarly escalates. This is because of enhanced premixing 
that is evident from the higher in-cylinder pressure. Additionally, the 
IMEP tends to follow an upward trend as the second injection advances, 
until the first hydrogen injection proportion surpasses 60 %. Beyond this 
point, the second injection timing at 10 
◦
CA bTDC results in higher IMEP 
compared to both the earliest and latest timings. Again, this trend is 
attributed to the higher degree of premixing achieved with earlier in -
jection at 180 
◦
CA bTDC. The expedited burn duration and accelerated 
combustion rate supported by an earlier injection of a larger hydrogen 
proportion culminate in a more thorough and rapid premixed combus -
tion process, thereby increasing engine power output. The net indicated 
efficiency under each condition parallels the trend observed with net 
IMEP, owing to the constant fuel rate upheld throughout the experi -
ments, which ensures a linear relationship between these parameters. 
The consistently low CoV of IMEP, which is even lower than that of the 
baseline diesel case, denotes the stability of combustion across all tested 
conditions. 
As mentioned previously, the diesel injection timing was adjusted to 
fix CA50 at 10 
◦
CA aTDC, which was successful for any first hydrogen 
injection proportions of 30 % and higher at 20 
◦
CA bTDC second in -
jection. However, for later second injection timing of 10 
◦
CA bTDC, 
maintaining CA50 required a minimum first injection proportion of 40 
%. Similarly, a minimum proportion of 50 % was needed for 180/0 
◦
CA 
bTDC injection. For the first injection proportions falling below these 
values, attaining a fixed CA50 value became unfeasible due to delayed 
second injection timings and the prolonged injection event. In such in -
stances, CA50 invariably lagged, despite varied diesel injection timings 
intended to counterbalance the hydrogen injection. For all the second 
injection timings tested, an increased first hydrogen proportion consis -
tently advanced both CA50 and CA90, indicating a hastened rate of 
combustion facilitated by the enhanced premixing of hydrogen and air. 
As a result, the burn durations demonstrate a similarly diminishing trend 
for higher first hydrogen injection proportions, a phenomenon ascribed 
Fig. 7. Effect of H2 split ratio on engine-out emissions for two selected second 
H2 injection timings at fixed first H2 injection timing of 180
◦
CA bTDC. The 
total H2 energy fraction is held constant at 70 %. 
X. Liu et al.

<!-- PDF_PAGE: 10 -->

International Journal of Hydrogen Energy 57 (2024) 904–917
913
Fig. 8. Effect of H2 split ratio on in-cylinder pressure and heat release. The results are shown for three selected second H2 injection timings at fixed first H2 injection 
of 180
◦
CA bTDC. The diesel injection duration and timing selected for fixed CA50. 
Fig. 9. Effect of H2 split ratio on engine performance parameters for three selected second H2 injection timings at fixed first H2 injection timing of 180
◦
CA bTDC. 
The total H2 energy fraction is held constant at 90 %. 
X. Liu et al.

<!-- PDF_PAGE: 11 -->

International Journal of Hydrogen Energy 57 (2024) 904–917
914
to the augmentation of premixed combustion. Particularly noteworthy is 
the observation that for hydrogen first injection proportions below 50 %, 
the ensuing diffusion flames ignited by the high second injection pro -
portion serve to extend the burn duration. This extension becomes 
progressively more evident as the delay of the second injection in -
creases. This is especially apparent for the latest second injection timing 
at 0 
◦
CA bTDC, where a pronounced deceleration in late combustion 
duration (CA50 - CA90) occurs as the first injection fraction rises. This 
effect can be attributed to the shift in combustion mode, unlike all other 
test conditions where both hydrogen injections precede the final diesel 
injection; that is, the diesel injection occurs before the second hydrogen 
injection, which extends beyond TDC and the start of combustion. As a 
result, the combustion process is partially premixed and predominantly 
mixing-controlled. 
Emissions results for CO
2 
and NO
x 
are presented in Fig. 10 . All in -
jection timings and proportions yield low levels of CO
2
, with emissions 
falling substantially below the diesel baseline case. Its sensitivity to the 
variation of hydrogen injection split ratios and the second injection 
timing appears to be minimal. All measured CO
2 
emissions of combus -
tion with hydrogen as a 90 % energy input were reduced to less than a 
third of the diesel baseline. However, the NO
x 
emission results reveal a 
steady increasing trend corresponding to the rise in the proportion of the 
first hydrogen injection from 10 % to 80 %. This trend aligns with ex -
pectations, as larger proportions in the first injection contribute to a 
more premixed combustion with a higher burning rate. When consid -
ering the injection timings, it is evident that a delayed second injection 
consistently results in reduction of NO
x 
emissions, irrespective of the 
hydrogen split ratio. This is likely attributable to the prolonged diffusion 
burning phase associated with such late hydrogen injection, where the 
hydrogen continues to be introduced beyond TDC, thus resulting in a 
combustion process more influenced by mixing-controlled combustion, 
rather than being primarily premixed. It is notable such NO
x 
sensitivity 
to hydrogen second injection timing was not evident with the ducted 
channel multi-hole injection ( Fig. 7 ), indicating the single-hole capped 
injector led to much more effective control of hydrogen mixtures. 
Since the level of hydrogen charge premixing was found to affect the 
power output and NO
x 
emissions directly, further experiments were 
performed with varied first hydrogen injection timing. As shown in 
Fig. 11 , the first hydrogen injection timing was set for 180, 90 and 60 
◦
CA bTDC while the proportion of first hydrogen injection was varied 
between 10 and 80 % of the total energy input. The second hydrogen 
injection was fixed at 10 
◦
CA bTDC for all the test conditions. The results 
of hydrogen injection timing of 180/10 
◦
CA bTDC was simply replotted 
from Fig. 8 . 
Fig. 11 shows that, for 180/10 
◦
CA bTDC hydrogen injections, 
increasing the portion of first hydrogen injection results in higher TDC 
from higher hydrogen proportion undergoing compression as previously 
discussed. The higher peak in-cylinder pressures, and corresponding rise 
in aHRR is attributed to the longer mixing, and consequently more 
premixed hydrogen charge and higher in-cylinder pressure. This trend is 
also observed for 90/10 
◦
CA bTDC hydrogen injections. When the same 
split conditions across these two timings are compared, the peak pres -
sure appears largely unchanged when the first injection is delayed but 
the peak aHRR shows a decreasing trend. This aHRR reduction is 
ascribed to a shift towards mixing-controlled combustion from premixed 
combustion as the first hydrogen injection was implemented at a later 
timing. In the case of the most delayed first injection timing of 60 
◦
CA 
bTDC, a positive correlation between the increase in the first injection 
proportion with the in-cylinder pressure and aHRR is observed until a 
split of 60 % and 30 %. However, beyond this point, with split ratios of 
70 %/20 % and 80 %/10 %, the trend inverts due to the insufficient 
mixing time for the first injection before the remaining hydrogen is 
introduced. This assertion is corroborated by wider aHRR profile shapes 
associated with higher first injection proportions. 
Fig. 12 presents the net IMEP, CoV of IMEP, indicated efficiency; 
combustion phasing, and burn durations for the hydrogen first injection 
timing and fraction variations as in Fig. 11 . A direct relationship is 
observed between the net IMEP and the proportion of hydrogen in the 
first injection, which is evident across all combinations of injection 
timings. The observed trend suggests that the IMEP increase predomi -
nantly depends on the hydrogen split ratio. It is because that a larger 
proportion of injected hydrogen leads to a more premixed charge, 
thereby enhancing combustion and subsequently the power output. 
However, it is worth noting that for later first injection timings at 90 and 
60 
◦
CA bTDC, the IMEP exceeds the value for the advanced injection 
timing of 180 
◦
CA. This inversion can be accounted for the distribution 
of the main combustion event: while CA50 remained constant, the heat 
release from the mixing-limited stratified hydrogen, as well as the 
diffusion flames during the later injections extends and persists into the 
expansion stroke, thereby contributing to a higher total work output. It 
is also apparent that as the proportion of hydrogen in the first injection 
increases, the injection timing becomes a more significant factor in 
determining the net IMEP and engine efficiency. This is particularly 
noticeable in the wider spread at a first proportion of 80 % compared to 
10 %. This growing difference as the first injection proportion increases 
indicates that for higher engine power output and efficiency, hydrogen 
charge premixing should be increased with higher proportion of first 
injected hydrogen; however, more stratified hydrogen mixture distri -
bution is required by delaying the first hydrogen injection timing. 
For combustion phasing, the CA50 was successfully maintained for 
first hydrogen injection proportions of 40 % and above, accomplished 
through the control of diesel injection timing. Specifically, irrespective 
of diesel injection timing, the CA50 for low proportion first injection was 
persistently retarded. This is attributed to the formation of hydrogen 
diffusion flames incited by the delayed second injection at 10 
◦
CA bTDC. 
Here, due to the substantial proportion of hydrogen injected close to 
TDC and the consequent insufficient mixing time, a shift towards a 
diffusion flame occurs. Furthermore, the burn durations indicate 
Fig. 10. Effect of H2 split ratio on engine-out NOx and CO2 emissions for three 
selected second H2 injection timings at fixed first H2 injection timing of 180
◦
CA bTDC. The total H2 energy fraction is held constant at 90 %. 
X. Liu et al.

<!-- PDF_PAGE: 12 -->

International Journal of Hydrogen Energy 57 (2024) 904–917
915
Fig. 11. Effect of H2 split ratio on in-cylinder pressure and heat release. The results are shown for three selected first H2 injection timings at fixed second H2 
injection of 10
◦
CA bTDC. The diesel injection duration and timing selected for fixed CA50. 
Fig. 12. Effect of H2 split ratio on engine performance parameters for three selected first H2 injection timings at fixed second H2 injection timing of 10
◦
CA bTDC. 
The total H2 energy fraction is held constant at 90 %. 
X. Liu et al.

<!-- PDF_PAGE: 13 -->

International Journal of Hydrogen Energy 57 (2024) 904–917
916
expedited combustion when a higher proportion of hydrogen is initially 
injected. When comparing different injection timings for a fixed second 
hydrogen injection proportion, it appears that the injection timing does 
not significantly influence the rate of combustion for each scenario, as 
the burn durations exhibit considerable similarity across varying first 
injection timings. This indicates that combustion phasing and burn 
duration are primarily governed by the proportion of first hydrogen 
injection. However, for hydrogen first injection proportions less than 40 
%, the burn duration substantially lengthens, showing an almost twofold 
increase from the highest to the lowest first injection proportions across 
all injection timings tested. This elongation suggests the optimal strati -
fication of the charge was exceeded, leading to combustion being 
dominated by diffusion flames. Nevertheless, a slight increase in burn 
duration is observed for later injection timings, a trend that intensifies as 
the first injection fraction escalates. This can once again be explained by 
the slower burn of diffusion flames formed during later injections, as 
opposed to the premixed combustion observed in earlier injection tim -
ings. These observations align with the recorded in-cylinder pressure 
and aHRR data, with the higher peak pressure and aHRR observed for 
earlier timings implying more rapid combustion. Intriguingly, a first 
injection timing at 90 
◦
CA consistently resulted in the shortest burn 
duration. This suggests that this intermediate timing allowed for optimal 
charge stratification, which in turn increased the combustion rate as the 
ignition of locally rich mixtures facilitated flame propagation 
throughout the remaining pre-entrained mixtures. 
The emissions CO
2 
and NO
x 
are presented in Fig. 13 . At a high ratio 
of 90 % hydrogen and 10 % diesel, the measured CO
2 
emission levels 
were very low, averaged at around 2 % of the total exhaust volume. This 
value remained remarkably consistent, regardless of the variation in the 
first hydrogen injection proportion or the injection timing. By contrast, 
NO
x 
emissions show high sensitivity to the first hydrogen injection 
proportion with increased premixed hydrogen charge causing higher 
NO
x 
emissions. This can be mitigated to a certain extend by delaying the 
first hydrogen injection timing to 60 
◦
CA bTDC, a positive effect of 
hydrogen charge stratification leading to diffusion flames with a lower 
burning rate. However, to maintain NO
x 
emissions at the same level of 
the baseline diesel, the first hydrogen injection should be kept lower 
than 20 %, indicating an important IMEP/efficiency – NO
x 
trade-off 
characteristics. 
4. Conclusions 
The performance and emissions resulting from varied split injection 
strategies have been systematically studied in a hydrogen-diesel dual 
direct-injection engine. Two different hydrogen injector geometries 
were used in the same automotive-size single-cylinder diesel engine. 
Varied hydrogen injection timings during the compression stroke 
allowed control over hydrogen charge premixing as well as a level of 
stratification. The engine performance was assessed through measure -
ments of in-cylinder pressure and derived metrics such as apparent heat 
release rate (aHRR), combustion phasing, indicated mean effective 
pressure (IMEP), and efficiency. The analysis of engine-out emissions 
was centred around carbon dioxide (CO
2
) and nitrogen oxides (NO
x
). 
The key findings from this experimental study are summarised as 
follows:  
1. Utilising a multi-hole hydrogen injector with equal split injection 
strategies, a 20%-point higher hydrogen substitution ratio of 70 % 
was achieved compared to the previous single injection approach 
[ 23 ]. However, the limited mixture making capability of this injector 
led to only minor differences in overall engine performance and 
emissions despite the change of hydrogen second injection timing.  
2. With increased hydrogen first injection proportion, the ducted- 
channel multi-hole injector showed decreased CO
2 
but increased 
NO
x 
emissions in response to increased charge premixing. However, 
its expected sensitivity to the second injection timing was not 
measured even for higher hydrogen second injection proportions.  
3. A single-hole capped injector permitted a 90 % hydrogen energy 
substitution ratio for all split injection cases, as the design enabling 
hydrogen delivery more directly towards the piston bowl compared 
to the dispersed hydrogen mixtures of ducted-channel multi-hole 
injector. 
4. Utilising the single-hole capped injector, the second hydrogen in -
jection timing, ranging from 20 to 0 
◦
CA bTDC, demonstrated a more 
distinct effect on mixture stratification control. Notably, the very late 
injection at TDC revealed mixing-controlled hydrogen combustion, 
achieving diesel-comparable or superior power output with sub -
stantial CO
2 
reduction.  
5. By varying the split ratio at three specific first hydrogen injection 
timings, the single-hole capped injector showed discernible transi -
tions between combustion modes. Specifically, a high fraction of 
hydrogen in the first injection facilitated premixed combustion due 
to increased mixing time. Conversely, a high fraction of hydrogen in 
the second injection favoured mixing-controlled combustion, char -
acterised by the shift towards late-cycle combustion for lower NO
x 
emissions. From the results of hydrogen split injection strategies, it is 
indicated that the timing of hydrogen injection plays a crucial role. 
Therefore, it is recommended to find the balance between early and 
late hydrogen injection timings so that the combustion is further 
enhanced and engine-out emissions are optimised  
6. The hydrogen split injection strategies do not make a significant 
impact on CO
2 
emissions. It is the high total energy fraction of 
hydrogen of up to 90 %, which achieves about 77 % CO
2 
reduction 
compared to the diesel baseline. 
Declaration of competing interest 
The authors declare that they have no known competing financial 
Fig. 13. Effect of H2 split ratio on engine-out NOx and CO2 emissions for three 
selected first H2 injection timings at fixed second H2 injection timing of 10
◦
CA 
bTDC. The total H2 energy fraction is held constant at 90 %. 
X. Liu et al.

<!-- PDF_PAGE: 14 -->

International Journal of Hydrogen Energy 57 (2024) 904–917
917
interests or personal relationships that could have appeared to influence 
the work reported in this paper. 
Acknowledgements 
The experiments pertinent to this study were conducted at the UNSW 
Engine Research Laboratory, Sydney, Australia. The authors acknowl -
edge the financial support provided by the Australian Renewable Energy 
Agency (ARENA) for this research project. 
References 
[1] Yip H, Srna A, Yuen A, Kook S, Taylor R, Yeoh G, Medwell P, Chan Q. A review of 
hydrogen direct injection for internal combustion engines: towards carbon-free 
combustion. Appl Sci 2019;9(22):4842. https://doi.org/10.3390/app9224842 . 
[2] Verhelst S. Recent progress in the use of hydrogen as a fuel for internal combustion 
engines. Int J Hydrogen Energy 2014;39(2):1071 – 85. https://doi.org/10.1016/j. 
ijhydene.2013.10.102 . 
[3] Simio LD, Iannaccone S, Guido C, Napolitano P, Maiello A. Natural gas/hydrogen 
blends for heavy-duty spark ignition engines: performance and emissions analysis. 
Int J Hydrogen Energy 2024;50(B):743 – 57. https://doi.org/10.1016/j. 
ijhydene.2023.06.194 . 
[4] Das LM. Hydrogen-oxygen reaction mechanism and its implication to hydrogen 
engine combustion. Int J Hydrogen Energy 1996;21:703 – 15. https://doi.org/ 
10.1016/0360-3199(95)00138-7 . 
[5] Mathur H, Das LM. Performance characteristics of a hydrogen fuelled S.I. engine 
using timed manifold injection. Int J Hydrogen Energy 1991;16:115 – 27. https:// 
doi.org/10.1016/0360-3199(91)90038-K . 
[6] Wang S, Ji C. Cyclic variation in a hydrogen-enriched spark-ignition gasoline 
engine under various operating conditions. Int J Hydrogen Energy 2012;37: 
1112 – 9. https://doi.org/10.1016/j.ijhydene.2011.02.079 . 
[7] Dimitriou P, Tsujimura T. A review of hydrogen as a compression ignition engine 
fuel. Int J Hydrogen Energy 2017;42(38):24470 – 86. https://doi.org/10.1016/j. 
ijhydene.2017.07.232 . 
[8] Lee J, Park C, Bae J, Kim Y, Choi Y, Lim B. Effect of different excess air ratio values 
and spark advance timing on combustion and emission characteristics of hydrogen- 
fueled spark ignition engine. Int J Hydrogen Energy 2019;44(45):25021 – 30. 
https://doi.org/10.1016/j.ijhydene.2019.07.181 . 
[9] Sandalci T, karagoz Y. Experimental investigation of the combustion 
characteristics, emissions and performance of hydrogen port fuel injection in a 
diesel engine. Int J Hydrogen Energy 2014;39(32):18480 – 9. https://doi.org/ 
10.1016/j.ijhydene.2014.09.044 . 
[10] Li T, Zhou X, Wang N, Wang X, Chen R, Li S, Yi P. A comparison between low-and 
high-pressure injection dual-fuel modes of diesel-pilot-ignition ammonia 
combustion engines. J Energy Inst 2022;102:362 – 73. https://doi.org/10.1016/j. 
joei.2022.04.009 . 
[11] Zhou X, Li T, Wang N, Wang X, Chen R, Li S. Pilot diesel-ignited ammonia dual fuel 
low-speed marine engines: a comparative analysis of ammonia premixed and high- 
pressure spray combustion modes with CFD simulation. Renew Sustain Energy Rev 
2023;173:113108. https://doi.org/10.1016/j.rser.2022.113108 . 
[12] Berenjestanaki AV, Kawahara N, Tsuboi K, Tomita E. Performance, emissions and 
end-gas autoignition characteristics of PREMIER combustion in a pilot fuel-ignited 
dual-fuel biogas engine with various CO
2 
ratios. Fuel 2021;286(2):119330. https:// 
doi.org/10.1016/j.fuel.2020.119330 . 
[13] Imamoto T, Kawahara N, Tomita E. PREMIER combustion characteristics of a pilot 
fuel-ignited dual-fuel biogas engine with consideration of cycle-to-cycle cariations. 
Fuel 2022;314:123049. https://doi.org/10.1016/j.fuel.2021.123049 . 
[14] Verhelst S, Wallner T, Sierens R. Hydrogen-Fueled internal combustion engines. 
Handb. Hydrogen Energy 2014:821 – 902. https://doi.org/10.1201/b17226 . 
[15] Saravanan N, Nagarajan G. An experimental investigation of hydrogen-enriched air 
induction in a diesel engine system. Int J Hydrogen Energy 2008;33(6):1769 – 75. 
https://doi.org/10.1016/j.ijhydene.2007.12.065 . 
[16] Naber JD, Siebers DL. Hydrogen combustion under diesel engine conditions. Int J 
Hydrogen Energy 1998;23(5):363 – 71. https://doi.org/10.1016/S0360-3199(97) 
00083-9 . 
[17] Wimmer A, Wallner T, Ringler J, Gerbig F. H2-direct injection – a highly promising 
combustion concept. SAE Technical Paper, 2005-01-0108; 2005. https://doi.org/ 
10.4271/2005-01-0108 . 
[18] Mohammadi A, Shioji M, Nakai Y, Ishikura W, Tabo E. Performance and 
combustion characteristics of a direct injection SI hydrogen engine. Int J Hydrogen 
Energy 2007;32(2):296 – 304. https://doi.org/10.1016/j.ijhydene.2006.06.005 . 
[19] Li Y, Gao W, Zhang P, Ye Y, Wei Z. Effects study of injection strategies on 
hydrogen-air formation and performance of hydrogen direct injection internal 
combustion engine. Int J Hydrogen Energy 2019;44(47):26000 – 11. https://doi. 
org/10.1016/j.ijhydene.2019.08.055 . 
[20] Rorimpandey P, Yip H, Srna A, Zhai G, Wehrfritz A, Kook S, Hawkes E, Chan Q. 
Hydrogen-diesel dual-fuel direct-injection (H2DDI) combustion under 
compression-ignition engine conditions. Int J Hydrogen Energy 2023;48(2): 
766 – 83. https://doi.org/10.1016/j.ijhydene.2022.09.241 . 
[21] Huang S, Li T, Wang X, Chen R, Yang R, Qing Z. Effects of various discharge 
strategies on ignition and combustion of lean natural gas mixture under the static 
and turbulent conditions. Exp Therm Fluid Sci 2022;133:110581. https://doi.org/ 
10.1016/j.expthermflusci.2021.110581 . 
[22] Park C, Kim Y, Oh J, Choi J, Choi Y. Effect of fuel injection timing on performance 
and emissions with a dedicated direct injector in a hydrogen engine. Energy 
Convers Manag X 2023;18:100379. https://doi.org/10.1016/j.ecmx.2023.100379 . 
[23] Liu X, Srna A, Yip H, Kook S, Chan Q, Hawkes E. Performance and emissions of 
hydrogen-diesel dual direct injection (H2DDI) in a single-cylinder compression- 
ignition engine. Int J Hydrogen Energy 2021;46(1):1302 – 14. https://doi.org/ 
10.1016/j.ijhydene.2020.10.006 . 
[24] Wang Y, Evans A, Srna A, Wehrfritz A, Hawkes E, Liu X, Kook S, Chan Q. 
A numerical investigation of mixture formation and combustion characteristics of a 
hydrogen-diesel dual direct injection engine. SAE Technical Paper, 2021-01-0526; 
2021. https://doi.org/10.4271/2021-01-0526 . 
[25] Liu X, Seberry G, Kook S, Chan Q, Hawkes E. Direct injection of hydrogen main fuel 
and diesel pilot fuel in a retrofitted single-cylinder compression ignition engine. Int 
J Hydrogen Energy 2022;47(85):35864 – 76. https://doi.org/10.1016/j. 
ijhydene.2022.08.149 . 
[26] H ¨anggi S, Moretto G, Albin T, Onder C. The potential of heat release rate and 
cylinder pressure feedback control for conventional and premixed charge 
compression ignition combustion. Int J Engine Res 2020;22(9):3080 – 100. https:// 
doi.org/10.1177/1468087420948314 . 
[27] Moretto G, H ¨anggi S, Onder C. Optimal combustion calibration for direct-injection 
compression-ignition engines using multiple injections. Int J Engine Res 2023;24 
(4):1273 – 784. https://doi.org/10.1177/14680874221087969 . 
[28] Li Z, Wang Y, Wang Y, Yin Z, Gao Z, Ye Z, Zhen X. Effects of fuel injection timings 
and methanol split ratio in m/d/m strategy on a diesel/methanol dual-fuel direct 
injection engine. Fuel 2022;325:124970. https://doi.org/10.1016/j. 
fuel.2022.124970 . 
[29] Woo C, Goyal H, Kook S, Hawkes E, Chan Q. Double injection strategies for 
ethanol-fuelled gasoline compression ignition (gci) combustion in a single-cylinder 
light-duty diesel engine. SAE Technical Paper, 2016-01-2303; 2016. https://doi. 
org/10.4271/2016-01-2303 . 
[30] How H, Masjuki H, Kalam M, Teoh Y. Influence of injection timing and split 
injection strategies on performance, emissions, and combustion characteristics of 
diesel engine fueled with biodiesel blended fuels. Fuel 2018;213:106 – 14. https:// 
doi.org/10.1016/j.fuel.2017.10.102 . 
[31] Li G, Yu X, Shi W, Yao C, Wang S, Shen Q. Effects of split injection proportion and 
the second injection timings on the combustion and emissions of a dual fuel SI 
engine with split hydrogen direct injection. Int J Hydrogen Energy 2019;44(21): 
11194 – 204. https://doi.org/10.1016/j.ijhydene.2019.02.222 . 
[32] Yip H, Srna A, Liu X, Kook S, Hawkes ER, Chan Q. Visualization of hydrogen jet 
evolution and combustion under simulated direct-injection compression-ignition 
engine conditions. Int J Hydrogen Energy 2020;45(56):32562 – 78. https://doi.org/ 
10.1016/j.ijhydene.2020.08.220 . 
[33] Kook S, Liu X, Edmonds B. Hydrogen-diesel direct injection dual-fuel system for 
internal combustion engines. In: Australian patent provisional application No. 
2022900118, filed 21 Jan 2022, international application No. PCT/AU2023/ 
050019. International publication; 27 Jul 2023 . 
[34] Shahlari A, Kurtz E, Hocking C, Antonov S. Correlation of cylinder pressure-based 
engine noise metrics to measured microphone data. Int J Engine Res 2015;16(7): 
829 – 50. 10.1177%2F1468087414552831 . 
[35] Shahlari A, Hocking C, Kurtz E, Ghandhi J. Comparison of compression ignition 
engine noise metrics in low-temperature combustion egimes. SAE Int. J. Engines 
2013;6(1):541 – 52. https://doi.org/10.4271/2013-01-1659 . 
X. Liu et al.
