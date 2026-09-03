<!-- PDF_PAGE: 1 -->

Renewable and Sustainable Energy Reviews 119 (2020) 109653
Available online 9 December 2019
1364-0321/© 2019 Elsevier Ltd. All rights reserved.
A comprehensive review of pilot ignited high pressure direct injection 
natural gas engines: Factors affecting combustion, emissions 
and performance 
Menghan Li
a , b , c
, Hanming Wu
c
, Tiechen Zhang
a
, Boxiong Shen
a
, Qiang Zhang
d , *
, 
Zhenguo Li
c , ** 
a
School of Energy and Environmental Engineering, Hebei University of Technology, No. 5340 Xiping Road, Beichen District, Tianjin, 300401, China 
b
School of Civil and Transportation Engineering, Hebei University of Technology, No. 5340 Xiping Road, Beichen District, Tianjin, 300401, China 
c
National Engineering Laboratory for Mobile Source Emission Control Technology, China Automotive Technology & Research Center, Co., Ltd., No. 68 Xianfeng East 
Road, Dongli District, Tianjin, 300300, China 
d
School of Energy and Power Engineering, Shandong University, No. 17923 Jingshi Road, Lixia District, Jinan, 250061, China   
ARTICLE INFO  
Keywords: 
Natural gas 
Pilot ignited 
High pressure direct injection 
Performance 
Emissions 
Injection strategy 
ABSTRACT  
With the increasing concern on environmental pollution originated from diesel engines, natural gas, which is 
widely accepted as a promising alternative fuel for diesel owing to its wide availability and low emissions, has 
brought into focus. Spark ignition natural gas engines are the most widely used type of natural gas engines. 
Nevertheless, the thermal efficiency and power output of this type of engines are lower than equivalent diesel 
engines while HC emissions are relatively higher. It is generally agreed that the drawback of the lower thermal 
efficiency can be mitigated by using diesel as the pilot fuel instead of using spark plug, however, if natural gas is 
premixed with air before introduced into the cylinder, the flaw of higher HC emissions still exists. Pilot ignited 
high pressure direct injection natural gas engines are capable of reaching thermal efficiency equivalent to diesel 
engines and maintain all the advantages in emissions, thus, have been become a research hotspot. In this paper, 
the effects of injection parameters (including injection timing, injection pressure and injection interval between 
pilot diesel and natural gas) on combustion, emissions and performance are presented based on the related 
published documents. Furthermore, the adaptable load range, the emission reducing effects and the corre -
sponding drawbacks are discussed for different injection strategies. Finally, the effects of injector design and 
gaseous fuel composition are collected and critically analyzed.   
1. Introduction 
Diesel, which is a conventional fossil fuel derived from petroleum 
sources, consists of hundreds of compounds with carbon number 
ranging from 10 to 22 and an average carbon number of 14 or 15. The 
most predominant chemical classes are n-alkanes, iso-alkanes, cyclo -
alkanes, and aromatics [ 1 ]. In the past decades, diesel has been 
considered as one of the most widely used fuels in the transportation 
sector owing to its high combustion efficiency, lower running cost and 
suitability for engine design [ 2 , 3 ]. Though diesel engines have obvious 
superiority in practical application, the emissions accompanied cannot 
be ignored. The primary emissions of diesel engines are carbon mon -
oxide (CO), nitrogen oxides (NOx), sulphur oxides (SOx), particulate 
matter (PM) and green house gas (GHG) emissions. NOx emissions in -
crease tropospheric ozone and hydroxyl-radical concentrations, 
contributing to the formation of photochemical smog [ 4 ]. SOx emissions 
are the precursors for sulphuric acid, which could cause adverse effects 
on respiratory health of human [ 5 ]. CO is a poisonous gas, which could 
reduce the oxygen carrying capacity of blood and block the transport of 
oxygen to vital organs in human body, leading to tissue hypoxia along 
with the subsequent nausea, headache and even death [ 6 ]. Among all 
the emissions from diesel engines, PM is considered as the most harmful 
one owing to its significant adverse effects on climate and human health; 
* Corresponding author. School of Energy and Power Engineering, Shandong University, No. 17923 Jingshi Road, Lixia District, Jinan, Shandong Province, 
250061, China. 
** Corresponding author. National Engineering Laboratory for Mobile Source Emission Control Technology, China Automotive Technology & Research Center, Co., 
Ltd., No. 68 Xianfeng East Road, Dongli District, Tianjin 300300, China. 
E-mail addresses: sduzhangqiang@sdu.edu.cn (Q. Zhang), lizhenguo@catarc.ac.cn (Z. Li).  
Contents lists available at ScienceDirect 
Renewable and Sustainable Energy Reviews 
journal homepage: http://www. elsevier.co m/locate/rs er 
https://doi.org/10.1016/j.rser.2019.109653 
Received 17 June 2019; Received in revised form 2 December 2019; Accepted 3 December 2019

<!-- PDF_PAGE: 2 -->

Renewable and Sustainable Energy Reviews 119 (2020) 109653
2
PM is made up of small particles and liquid droplets, which can be 
inhaled in the respiratory system, causing respiratory morbidity as well 
as cardiovascular and cerebrovascular diseases [7]. With the implement 
of the more stringent standards to limit these harmful emissions, natural 
gas have been increasing concerned owing to its low carbon content, low 
adiabatic flame temperature and the subsequent lower green house gas 
emissions, PM emissions, NOx emissions and SOx emissions when 
adopted as the fuel for the engines of automobiles and marines [8–11]. 
In the on-road transportation sector, the number of natural gas ve -
hicles reached 27.8 million in 2019, nearly tripled the number of 2008 
[12]; in the past ten years, growth in the population of on-road natural 
gas vehicles is most noticeable in Asia-Pacific region, followed by Latin 
American and Europe; three countries, China, Iran and India account for 
more than 50% of total vehicle population. During 2005 to 2017, the 
proportion of natural gas vehicles in total vehicles has increased from 
0.5% to 1.5%, whereas the penetration rate varies from country to 
country; the top three countries with the highest penetration rates are 
Uzbekistan, Iran and Pakistan, with penetration rates of 40.8%, 31.9% 
and 14.0%, respectively [13]. In the marine sector, the use of natural gas 
is of great importance due to the emission limitations for SOx and NOx. 
According to the data in 2019, most of the global natural gas fuelled 
fleets are operating in Norway and the rest are operating in North 
Sea/Baltic Sea region due to the regulation of SOx or NOx in these re -
gions; statistics showed that the share of liquefied natural gas (LNG) 
fuelled vessels has increased from 5.6% in 2010 to 13.5% in 2018 from 
the aspect of gross tonnage delivered; among all the LNG vessels, ferry 
has the largest population and cruise ship has the highest penetration 
rate [14]. As illustrated in the word energy review of British Petroleum 
(BP) in 2019 [15], though natural gas consumption has been increased 
largely from 1993 to 2018, the production of natural gas is in equilib -
rium with the consumption of natural gas. The production capability 
could meet the demand of consumption due to the following reasons 
[16]: (1) the volume for the remaining gas reserves is large enough, 
meanwhile, the amount of proved gas reserves increase by 50% in the 
past twenty years; (2) the yields of the unconventional natural gases, 
such as shale gas, tight gas and coalbed gas, have been remarkably 
increased owing to the “Unconventional Oil and Gas Revolution”; (3) the 
discovery of conventional and unconventional natural gas fields is still 
on-going. 
When natural gas is applied to engines in the manner of the con -
ventional spark ignition technology, the corresponding PM, NOx and CO 
emissions would be significantly reduced compared to equivalent diesel 
engines owing to the fuel properties; however, the power output will be 
reduced due to the limitation of compression ratio and the reduced 
volumetric efficiency caused by the throttling losses [17]. Adopting 
diesel as the pilot fuel for natural gas is another method for natural gas 
usage in engines; in this case, there are two ways for introducing natural 
gas into the cylinder, i.e. premixed and direct injection [18]. With re -
gard to pilot ignited premixed dual fuel engine, the compression ratio 
can be raised owing to the faster flame propagation and most emissions 
could also be controlled in a level obvious lower than equivalent diesel 
engines [19–21]. However, the thermal efficiency is still lower than 
diesel engines attributed to the possibility of knocking caused by the 
premixed end gas and the essential throttling to ensure the flammability 
of the premixed charge at part load conditions. Moreover, for both spark 
ignition natural gas engine and pilot ignited premixed dual fuel engine, 
the shortcomings of the higher HC emissions and the lower volumetric 
efficiency could not be eliminated as natural gas is premixed with air in 
the intake system, leading to the escaping of unburnt fuel during the 
overlapping period and the partial oxidation products originated from 
wall quenching [22]. With regard to pilot ignited direct injection natural 
gas engine, both natural gas and diesel are introduced into the cylinder 
by a concentric-needle dual fuel injector in a direct injection pattern [23, 
24]. Subsequently, only fresh air is inhaled into the cylinder during the 
intake stroke. Thus, less fuel/air mixture will be formed near the cyl -
inder wall or in the crevices and fuel will not escape into the exhaust 
List of abbreviations including units and nomenclature 
ATDC after top dead center 
BP British petroleum 
BTDC before top dead center 
BMEP brake mean effective pressure 
CA crank angle 
CA10 10% heat release combustion phase angle 
CA50 50% heat release combustion phase angle 
CA90 90% heat release combustion phase angle 
CO carbon monoxide 
CR compression ratio 
DI-NG direct injection natural gas and diesel reactivity 
combustion 
DNI diesel and natural gas injection interval 
DRGEP direct relationship graph with error propagation 
DRGEPSA direct relationship graph with error propagation and 
sensitivity analysis 
DRP diesel rail pressure 
ECU electric control unit 
EGR exhaust gas recirculation 
EE energy equivalent 
ETS end of the diesel injection to the start of natural gas 
injection 
GHG green house gas 
GID gaseous fuel ignition delay 
GISFC gross indicated specific fuel consumption 
GSEP separation between natural gas injections 
HC hydrocarbon 
HCCI homogenous charge compression ignition 
HCDI homogenous charge direct injection 
HPDI high pressure direct injection 
IHR integrated heat release 
ITE indicated thermal efficiency 
IMEP indicated mean effective pressure 
mm millimeter 
ms millisecond 
NOx nitrogen oxides 
NGSI natural gas single injection 
NPP proportion of natural gas post injection 
NPSOI injection timing of natural gas pre-injection 
NSOI start of the injection of natural gas 
Pi orifice inlet pressure 
Pe orifice exit pressure 
Pb ambient pressure 
PCP peak cylinder pressure 
PM particulate matter 
PRR pressure rise rate 
RCD rapid combustion duration 
RNG renormalization group 
PNPI proportion of natural gas pre-injection 
SOx sulphur oxides 
STS start of the diesel injection to the start of natural gas 
injection 
SPC slightly premixed combustion 
THC total hydrocarbons 
VE volumetric equivalent  
M. Li et al.

<!-- PDF_PAGE: 3 -->

Renewable and Sustainable Energy Reviews 119 (2020) 109653
3
pipe during valve overlapping, resulting in extremely low HC emissions. 
In addition, the knocking tendency will be mitigated as a result of the 
leaner end-gas and the corresponding reduced possibility of 
auto-ignition at the near wall regions, which makes the engine more 
adaptable to higher compression ratio. Moreover, throttling device is 
not essential to maintain the normal operation at part load conditions; 
therefore, this type of engines are capable of reaching diesel-like thermal 
efficiency and power output [25–27]. As can be summarized from the 
comparison of the current technologies for natural gas engines, pilot 
ignited direct injection natural gas engines can obtain higher power 
output, better fuel economy and fewer HC emissions; besides, it has been 
proven that pilot ignited direct injection natural gas engines could meet 
the Euro VI emission standards with power output equivalent to diesel 
engines and improved transient response [28]. Consequently, usage of 
natural gas in the pattern of direct injection and pilot ignition has been 
considered as the most promising choice for the employment of natural 
gas in engines. 
During the evolution of the technologies used in pilot ignited direct 
injection natural gas engines, the knowledge for the effects of different 
design and calibration parameters could help to shorten the develop -
ment cycle of this type of engines. In fact, researchers and engineers 
should first obtain an acquaintance with the possible parameters which 
could improve the emissions and performance of the engine. Then, 
schemes and calibration procedures would be proposed according to the 
design objectives. Finally, the proposed design schemes would be 
assessed by numerical simulations and experiments. In this case, it is 
considered that the assessment for the effects of the key parameters on 
combustion, emissions and performance would make a review work 
more constructive and meaningful from both theoretical and engineer -
ing aspects. Up to now, there is only one published review paper 
regarding pilot ignited high pressure direct injection natural gas en -
gines, i.e. the paper by Ouellette P et al., in 2016 [28]. The work of 
Ouellette P et al. [28] gives a general review for the progresses in the 
fuel system of pilot ignited high pressure direct injection natural gas 
engines and summarized the technologies used to reach the re -
quirements of Euro VI emissions standard. However, limited informa -
tion on the influence of the specific parameters, such as injection 
parameters, injector geometric parameters and gaseous fuel composi -
tions, are provided in their study. Thus, a review paper regarding the 
evaluation of the influencing factors involved in the design process of 
pilot ignited high pressure direct injection natural gas engines is still in 
need. 
The purpose of this paper is to provide guidelines for the design and 
calibration of pilot ignited natural gas engines. In section 2, a compre -
hensive review of the literatures concerning the effects of injection pa -
rameters, including injection timing, injection pressure and injection 
interval between diesel and natural gas on the combustion characteris -
tics (including cylinder pressure, heat release rate and combustion pa -
rameters), emission characteristics (including CO, NOx, HC, soot and PM 
if available) and performance (including thermal efficiency and fuel 
economy) of pilot ignited direct injection natural gas engines is pre -
sented. In section 3, the impacts of different injection strategies, such as 
High Pressure Direct Injection (HPDI) with post injection, Homogenous 
Charge Direct Injection (HCDI), Homogenous Charge Compression 
Ignition (HCCI), Slightly Premixed Combustion (SPC) as well as Direct 
Injection Natural Gas and Diesel Reactivity Combustion (DI-NG) are 
discussed critically to give further guidelines for the optimization of 
emissions and thermal efficiency. Besides, the effects of injector designs 
(including the diameter and number of gas nozzle holes, gas included 
angle, diesel included angle, injector tip height and the internal struc -
ture of co-injectors) are assessed to identify the role of injector design in 
the development of pilot ignited direct injection natural gas engines. In 
section 4, the effects of gaseous fuel composition (including the addition 
of hydrogen, nitrogen, ethane and propane) are summarized to elucidate 
the importance of energy source selection. In section 5, the key con -
clusions for all the above sections are presented. 
2. Effects of injection parameters 
Injection timing, injection pressure along with injection interval 
between pilot diesel and natural gas are the most basic parameters for 
pilot ignited direct injection natural gas engines. In engine calibration, 
the optimization of these parameters is vital for the improvements of 
thermal efficiency, combustion and emissions [28]. Injection timing can 
be separated into the injection timing of natural gas and the injection 
timing of diesel; at fixed injection interval, either of them can be referred 
to as the injection timing of pilot ignited direct injection natural gas 
engine. Injection pressure involves the injection pressure of natural gas 
and the injection pressure of diesel; the injection pressure of diesel is 
always higher than the injection pressure of natural gas in order to avoid 
leakage of natural gas into diesel and the differences between the in -
jection pressure of diesel and natural gas is a fixed value (generally 
lower than 20 bar), thus, either of them can be used to represent the 
injection pressure of the engine injection system. Injection interval be -
tween pilot diesel and natural gas has two different definitions, the first 
one is the time duration from the start of the diesel injection to the start 
of natural gas injection (STS), the other one is the time duration from the 
end of the diesel injection to the start of natural gas injection (ETS). In 
the previous studies, either of these two definitions are adopted. It 
should also be noted that as the effects of these parameters are highly 
dependent on the precise control of the injection system; hence, in this 
section, all the studies are based on the electric controlled injection 
system rather than mechanical ones. 
2.1. Injection timing 
Injection timing, which has profound effects on the combustion and 
emissions of pilot ignited direct injection natural gas engines (Table 1), 
is the most basic injection parameter for direct injection engines. When 
evaluating the effects of injection timing, the injection interval between 
diesel and natural gas should be kept constant while the injection tim -
ings of diesel and natural gas should be changed simultaneously. For 
experimental studies discussed in this section, the injection timings are 
electric command signals rather than the actual injection timings when 
fuel is introduced into the cylinder. The time duration between the 
electric command and the actual injection timing is called injection 
delay. There are two contributors for the whole injection delay, the first 
one is the electric delay caused by the response of the electric driver and 
solenoids; the second one is the mechanical delay induced by the hy -
draulic elements of the injector. Normally, the injection delay is ranging 
from 0.5ms to 0.7 ms [29], but the specific value changes with injection 
pressure and operation condition. 
Douville [30] studied the combustion and emission characteristics in 
a single cylinder, naturally aspirated two-stroke engine and a 
six-cylinder, turbo-charged two-stroke engine at medium to high speeds 
and low loads. As can be found by the experiment results of Douville 
[30], peak cylinder pressure and NOx emissions increase with the 
advancement of injection timing due to the associated compression ef -
fects and higher in-cylinder temperature; CO emission first decrease and 
then flatten out with advancing injection timing attributed to the 
improved oxidation with earlier fuel introduction, albeit the trends of 
HC emissions, soot emissions and thermal efficiency are dependent on 
engine type and operation parameters (engine load and engine speed). 
Dumitrescu [31] and Trusca [32] also conducted experiments on the 
single cylinder, naturally aspirated engine with retrofitted electric 
control system for the injector at medium speed and low loads; the 
conclusions of Dumitrescu [31] and Trusca [32] are consistent with 
those of Douville [30] in view of NOx and CO emissions while contro -
versies exist in terms of thermal efficiency and HC emissions due to the 
modifications in the injector system. 
Harrington et al. [33] performed studies on a six cylinder, 
turbo-charged four-stroke engine at an operating condition with me -
dium speed and high load; their results showed that thermal efficiency 
M. Li et al.

<!-- PDF_PAGE: 4 -->

Renewable and Sustainable Energy Reviews 119 (2020) 109653
4
and NOx emissions increase monotonously, HC decrease continuously 
with the advance of injection timing, whereas CO exhibits a first 
decrease and then increase trend. Zhang et al. [ 34 ] carried out experi -
ments on a six cylinder, turbo-charged four-stroke engine at idle con -
ditions. As revealed by their results, the time duration for the initial of 
combustion would be extended at more advanced injection timing 
owing to the lower pressure and temperature during fuel injections, 
resulting in prolonged ignition delay and increased proportion of the 
premixed combustion; variations in these combustion characteristics, 
however, would further lead to advanced 50% heat release combustion 
phase angle (CA50) and 90% heat release combustion phase angle 
(CA90); in view of emissions, it was demonstrated that NOx and CO 
emissions are relatively higher at earlier injection timing while HC 
seems to be insensitive to injection timing ( Fig. 1 ). They also performed 
experiments at medium speeds and loads on the same engine, the engine 
test bed is shown in Fig. 2 [ 35 , 36 ]. The test bed used in these studies has 
a typical arrangement for the experiments of multiple-cylinder pilot 
ignited direct injection natural gas engines; for this kind of engines, 
natural gas and diesel are pressurized before delivered to the integrated 
pressure regulating module, and then supplied to the gas rail and diesel 
rail; the concentric-needle injectors receive fuels from both rails and 
introduce the fuels into the cylinder according to the electric signals. In 
their studies, the cylinder pressure of pilot ignited direct injection nat -
ural gas was divided into four stages, i.e. stage of pure compression, 
stage of mixture preparation, stage of pilot diesel combustion and stage 
of natural gas combustion; though advancing the injection timing has 
negative effects on exhaust energy and boost ratio, the positive effects on 
pressure rise rate are more pronounced, leading to higher peak cylinder 
pressure, advanced CA50 and higher NOx emissions; with regard to 
ignition delay, rapid combustion duration as well as HC and CO emis -
sions, the changing rules with injection timing are uncertain due to the 
differences in operation conditions and the corresponding discrepancies 
in in-cylinder temperature, pressure and flow field ( Fig. 3 ). It should be 
noted that if single-cylinder engines are used in the experiments, the gas 
rail and the diesel rail should be removed; moreover, if LNG is used 
instead of pipeline natural gas, the pump module for gas pressurization 
should be removed and a LNG tank integrated with hydraulically driven 
linear pump and vaporizing device should be added. 
2.2. Injection pressure 
The injection pressures of pilot ignited high pressure direct injection 
natural gas engines are ranging from 100 bar to 300 bar in most ex -
periments ( Table 2 ). In view of the pilot fuel, the pressure of diesel liquid 
is established by high pressure diesel pump; in view of natural gas, the 
pressure is established by a compressor if pipe line gas is supplied while 
by a hydraulic pump if LNG is supplied. Generally, pipe-line natural gas 
is supplied during experimental studies and LNG tank is equipped with 
heavy-duty trucks and marines. In pilot ignited direct injection engines, 
the pressure at nozzle exit is higher than the pressure in the combustion 
chamber, forming unexpanded gas jets [ 37 – 39 ]. As indicated by the 
previous studies, different from liquid fuel, the injection pressure of 
natural gas affects the jet characteristics by pressure ratio rather than the 
absolute pressure [ 40 ]. The schematic diagrams of high-pressure gas jets 
are shown in Fig. 4 . As shown, the high-pressure gas jets could be 
classified as subsonic jets, moderately under-expanded jets and highly 
under-expanded jets by the range of pressure ratio. In pilot ignited direct 
injection natural gas engines, the pressure ratio is generally higher than 
1.85. Therefore, moderately and highly under-expanded jets are more 
frequent encountered during engine operation, leading to the formation 
of shock wave structures. As investigated, pressure ratio has substantial 
effects on wave structure; for moderately under-expanded jets, the 
Table 1 
Effects of injection timing.  
Type of engine CR Engine speed, 
BMEP 
Injection timing 
(
�
BTDC) 
PCP Combustion 
parameters 
Thermal 
efficiency 
NOx CO HC Soot 
single cylinder, 
naturally aspirated, 
two stroke (Douville 
1994) 
16:1 1250 rpm, 1 
bar 
7-17
�
BTDC 
(Diesel) 
↑ – ↓ ↑ first ↓ 
then 
↔ 
first ↓ then 
↔ 
– 
single cylinder, 
naturally aspirated, 
two stroke (Douville 
1994) 
16:1 1250 rpm, 3 
bar 
3-21
�
BTDC 
(Diesel) 
↑ – first ↑ then ↓ ↑ first ↓ 
then 
↔ 
↑ first ↓ then ↔ t 
six-cylinder, turbo- 
charged, two stroke 
(Douville 1994) 
17:1 1200 
rpm & 1800 
rpm, 3 bar 
1-19
�
BTDC 
(Diesel) 
↑ – first ↑ then 
↔ (1200 rpm), 
↑ (1800 rpm) 
↑ first ↓ 
then 
↔ 
↑ – (1200 rpm), 
first ↑ then ↓ and 
finally ↔ (1800 
rpm) 
single cylinder, 
naturally aspirated, 
two stroke 
(Dumitrescu 1999) 
16:1 1200 rpm, 1 
bar && 3 bar 
0-18
�
BTDC 
(Diesel) 
– – first ↑ then ↔ ↑ first ↓ 
then 
↔ 
first ↓ then 
↔ 
– 
six cylinder, turbo- 
charged, four stroke 
(Harrington 2002) 
19:1 1668 rpm, 16 
bar 
14.5 – 28
�
BTDC 
(Diesel) 
– – ↑ ↑ first ↓ 
then ↑ 
↓ – 
six cylinder, turbo- 
charged, four stroke 
(Zhang 2015) 
17:1 600 rpm, 0.03 
BMEP (idle) 
4-13
�
BTDC (NG) ↑ ignition delay ↑ , RCD 
↑ , CA50 ← , CA90 ← 
– ↑ ↑ ↔ – 
six cylinder, turbo- 
charged, four stroke 
(Zhang 2015) 
17:1 1275 
rpm & 1550 
rpm, 10.5 bar 
1-19
�
BTDC (NG) ↑ ignition delay ↓ , RCD ↑ 
or first ↑ then ↓ , CA50 
← , CA10-50 first ↑ then 
↓ 
first ↑ then ↓ ↑ first ↑ 
then ↓ 
↔ (1275 
rpm), 
↓ (1550 
rpm) 
– 
six cylinder, turbo- 
charged, four stroke 
(Li 2015) 
17:1 1200 rpm, 13 
bar 
4-22
�
BTDC (NG) ↑ ignition delay ↓ , RCD 
first ↑ then ↓ and 
finally ↔ , CA50 ← 
– – – – – 
↑ indicates that an increasing trend with the advancement of injection timing is illustrated. 
↓ indicates that a decreasing trend with the advancement of injection timing is illustrated. 
↔ indicates that this parameter is insensitive to injection timing. 
← indicates that an advancing trend with the advancement of injection timing is illustrated. 
– indicates that the data are not available. 
M. Li et al.

<!-- PDF_PAGE: 5 -->

Renewable and Sustainable Energy Reviews 119 (2020) 109653
5
oblique shocks could be observed while for highly under-expanded jets, 
Mach disk would appear at the nozzle exit; these macroscopic jet 
structures could affect the evolution of the jet flow and thus influence 
the mixing quality. In view of jet flow characteristics in a chamber with 
constant volume and pressure, a general trend is that increases in 
pressure ratio could result in larger Mach disk, increased jet velocity and 
turbulence intensity, longer penetration as well as enhanced mixing 
[41]. 
In pilot ignited direct injection natural gas engines, since the back 
pressure is changing continuously with the piston movement and the 
variations in combustion induced pressure, the pressure ratio is a tran -
sient value rather than a constant one. The transient pressure ratio is 
highly dominated by injection pressure when operating condition is 
fixed. In this case, injection pressure could affect the jet penetration and 
Fig. 1. Effects of injection parameters on (a) CO emissions, (b) THC emissions, (c) CH
4 
emissions and (d) NOx emissions at idle conditions [34].  
Fig. 2. The schematic diagram of the test bed [36].  
M. Li et al.

<!-- PDF_PAGE: 6 -->

Renewable and Sustainable Energy Reviews 119 (2020) 109653
6
turbulence intensity, which will further affect the fuel/air mixing, the 
combustion and the emission formation processes in the combustion 
chamber evidently [ 42 ]. Earlier studies concerning the effects of injec -
tion pressure were performed on naturally aspirated, two stroke engines. 
According to Douville ’ s results at medium speed [ 30 ], increasing in -
jection pressure has negative effects on NOx emissions, CO emissions 
and CH
4 
emissions while has minor effects on thermal efficiency. As can 
be summarized from Dumitrescu ’ s results [ 31 ], increases in injection 
pressure would lead to increases in NOx and CH
4 
emissions, whereas the 
changing rule for CO emissions is load dependent; at BMEP of 0 – 3 bar, 
the effects of injection pressure on CO emissions could be neglected 
while at BMEP of 4 bar, CO emissions reach the highest value at the 
lowest injection pressure; when it comes to thermal efficiency, the 
changing trend with injection pressure is first increase and then decrease 
in the whole range of load tested; as also indicated by Douville ’ s and 
Dumitrescu ’ s results, the effects of injection pressure on NOx and CH
4 
emissions are not injector design dependent; however, the trends for CO 
emissions and thermal efficiency with the variation of injection pressure 
rely on the specific design of injector. As can be found from the results of 
Trusca [ 32 ], increases in injection pressure would bring about increases 
in NOx and CO emissions, however, thermal efficiency could be 
improved; the differences in the trend of CO emissions from the previous 
studies are mainly due to the modifications in the cylinder head, which 
could influence the intake process. For the naturally aspirated 
two-stroke engines discussed above, the requirements for injection 
pressure are generally at a low level (lower than 200 bar) due to the 
lower in-cylinder pressure. When it comes to turbo-charged four-stroke 
engines, injection pressures higher than 200 bar are more frequently 
adopted due to the raised intake pressure and the subsequent higher 
in-cylinder pressure. 
Larson [ 43 ] was the first one to evaluate the effects of injection 
pressure in a turbo-charged four-stroke engine; from the experimental 
results, he found that injection pressure doesn ’ t have evident effects on 
NOx emissions when compared against CA50, which means that the 
increases in NOx emissions caused by injection pressure are mainly 
induced by the advanced combustion phasing; when it comes to CO and 
HC emissions, it could be concluded from his results that the trends with 
the increase of injection pressure are different at different speeds and 
loads; in terms of PM emissions, the reducing effects of the increased 
injection are only evident at higher loads. The test engine of 
McTaggart-Cowan et al. [ 44 , 45 ] was similar to that of Larson [ 43 ], 
however, the intake and exhaust systems were modified to achieve 
in-cylinder conditions with Exhaust Gas Recirculation (EGR) added; 
hence, in their study, the effects of injection pressure were assessed at 
conditions with different EGR fractions; as demonstrated by their re -
sults, without EGR addition, NOx emissions illustrate an increasing 
trend at low and medium speeds and tend to be independent of injection 
pressure when EGR is added; at low and medium speeds, CO emissions 
prone to be lower at higher injection pressure while show an opposite 
trend at relatively higher speed; the formation of HC is depending on 
rather complicated mechanisms, thus, HC emissions are affected by not 
only speed and load, but also EGR fraction; PM emissions are strongly 
affected by injection pressure and are lower at higher injection pressures 
owing to the improved atomization and higher in-cylinder temperature. 
Brown [ 29 ] performed experiments at high and low pilot mass flows to 
evaluate the effects of injection pressure; as the results for high pilot 
Fig. 3. Emissions of (a) THC emissions, (b) CO emissions and (c) NOx emissions at different injection timings (A_180: engine speed ¼ 1275 rpm, DRP ¼ 180 bar; 
A_240: engine speed ¼ 1275 rpm, DRP ¼ 240 bar; A_300: engine speed ¼ 1275 rpm, DRP ¼ 300 bar; B_18: engine speed ¼ 1550 rpm, DRP ¼ 180 bar; B_240: engine 
speed ¼ 1550 rpm, DRP ¼ 240 bar; B_300: engine speed ¼ 1550 rpm, DRP ¼ 300 bar) [ 35 ]. 
M. Li et al.

<!-- PDF_PAGE: 7 -->

Renewable and Sustainable Energy Reviews 119 (2020) 109653
7
Table 2 
Effects of injection pressure.  
Type of engine CR Engine speed, 
BMEP or IMEP 
Injection 
pressure 
PCP Combustion 
parameters 
Thermal 
efficiency 
NOx CO HC Soot or 
PM 
single 
cylinder, 
naturally 
aspirated, 
two stroke 
(Douville 
1994) 
16:1 1250 rpm, 0–4 
bar (BMEP) 
100 bar, 120 
bar, 140 bar 
(NG) 
– – ↔ ↑ ↑ ↑(CH
4
), load 
and gas 
nozzle 
diameter 
dependent 
(NMHC) 
– 
single 
cylinder, 
naturally 
aspirated, 
two stroke 
(Dumitrescu 
1999) 
16:1 1200 rpm, 0–4 
bar (BMEP) 
100 bar, 130 
bar, 160 bar 
(NG) 
↑ – first ↑ 
then ↓ 
↑ ↔(0–3 bar), 
↓(4 bar) 
↑(CH
4
), load 
dependent 
(NMHC) 
– 
single 
cylinder, 
naturally 
aspirated, 
two stroke 
(Trusca 
2001) 
16:1 1200 rpm, 1 
bar&3 bar&5 bar 
(BMEP) 
130 bar, 150 
bar, 170 bar 
(NG) 
– – ↑ ↑ ↑(3 bar) – – 
single 
cylinder, 
turbo- 
charged, 
four stroke 
(Larson 
2003) 
19:1 800 rpm&1200 
rpm&1600 rpm, 
6.5 bar&9 
bar&10.5 bar 
(IMEP) 
190 bar, 230 
bar (NG) 
– RCD ↓, CA50 
← 
↔ ↔ load and 
speed 
dependent 
load and 
speed 
dependent 
↔(6.5 
bar&& 
9 bar), 
↓(10.8 
bar) 
single 
cylinder, 
turbo- 
charged, 
four stroke 
(McTaggart- 
Cowan 
2003) 
19:1 1200 rpm, 10.5 
bar (IMEP) 
170–250 bar 
(NG) 
↑ ignition delay 
↓, RCD ↓ 
– ↑ ↓ – ↓ 
single 
cylinder, 
turbo- 
charged, 
four stroke 
(McTaggart- 
Cowan 
2007) 
19:1 800 rpm&1200 
rpm&1600 rpm, 
3 bar&8.5 
bar&13.5 bar 
(IMEP) 
200–300 bar 
(NG) 
↑ ignition delay 
↓ 
↔ ↑(800 
rpm&1200 
rpm without 
EGR), ↓(1600 
rpm without 
EGR), ↔(with 
EGR) 
↓(800 
rpm&1200 
rpm), 
↑(1600 rpm) 
Load, speed 
and EGR ratio 
dependent 
↓ 
single 
cylinder, 
turbo- 
charged, 
four stroke 
(Brown 
2008) 
16.7:1 800 rpm, 8.5 bar 
(IMEP) 
165 bar, 225 
bar, 275 bar 
(NG) 
– – – ↔(165–225 
bar), 
↑(225–275 
bar) 
– ↓ – 
single 
cylinder, 
turbo- 
charged, 
four stroke 
(Patychuk 
2013) 
17:1 1493 rpm, 
16.0–16.7 bar 
(IMEP) 
230–280 bar 
(NG) 
– – – ↓ ↓ ↑ ↓ 
six cylinder, 
turbo- 
charged, 
four stroke 
(Zhang 
2015) 
17:1 600 rpm, 0.03 
BMEP (idle) 
150 bar, 180 
bar, 240 bar 
(Diesel) 
↔(150–180 
bar), 
↑(180–240 
bar) 
ignition delay 
↓, RCD ↓, 
CA50 ←, CA90 
← 
– ↑ ↑ ↔(150–180 
bar), 
↑(180–240 
bar) 
– 
Six cylinder, 
turbo- 
charged, 
four stroke 
(Zhang 
2015) 
17:1 1275 rpm&1550 
rpm, 10.5 bar 
(BMEP) 
180 bar, 240 
bar, 300 bar 
(Diesel) 
↑ ignition delay 
↓, RCD 
(injection 
timing 
dependent), 
CA50 ←, 
CA10-50 ↓ 
↑ ↑ injection 
timing 
dependent 
↑(1275 rpm), 
injection 
timing 
dependent 
(1550 rpm) 
– 
Six cylinder, 
turbo- 
17:1 180bar–300 
bar (Diesel) 
↑ – – – – – 
(continued on next page) 
M. Li et al.

<!-- PDF_PAGE: 8 -->

Renewable and Sustainable Energy Reviews 119 (2020) 109653
8
mass flow are less representative for the modern concept of pilot ignited 
direct injection natural gas engines, only the results for low pilot mass 
flow are described in this paper; it can be seen from their results that 
NOx emissions are the highest at the highest injection pressure, never -
theless, no significant differences could be observed between those of 
the low and medium injection pressures; in terms of CO emissions, a 
decreasing trend with the increasing injection pressure could be 
observed. Patychuk [46] made a comprehensive data analysis regarding 
the effects of injection pressure and found that rising the injection 
pressure would result in slightly reduced NOx and CO, evidently reduced 
PM with penalties in HC emissions at fixed combustion phasing and EGR 
rate. 
The results of Zhang et al. [34–36] are consistent with the previous 
studies in view of combustion parameters, i.e. increases in injection 
pressure could lead to shortened ignition delay, reduced rapid com -
bustion duration (RCD) and advanced combustion phasing (Fig. 5); with 
regard to emissions, the increasing of NOx emissions with rising injec -
tion pressure is a relatively definite characteristic at conditions without 
EGR; however, the changing rules for CO and HC emissions are not only 
dependent on engine speed or engine load but also affected by other 
injection parameters. In the above mentioned studies concerning the 
effects of injection pressure, the upper limits of injection pressure are 
within 300 bar; in the study of McTaggart-Cowan et al., in 2015 [47], 
Table 2 (continued ) 
Type of engine CR Engine speed, 
BMEP or IMEP 
Injection 
pressure 
PCP Combustion 
parameters 
Thermal 
efficiency 
NOx CO HC Soot or 
PM 
charged, 
four stroke 
(Li 2015) 
1200 rpm, 13 
bar&18.5 bar 
(BMEP) 
ignition delay 
↓, RCD ↓, 
CA50 ← 
six cylinder, 
turbo- 
charged, 
four stroke 
(McTaggart- 
Cowan 
2015) 
17:1 1220rpm–1680 
rpm, 
20.1bar–24.5 bar 
(BMEP) 
270bar–600 
bar (NG) 
↑ – ↑ ↑ ↓ ↓ ↓ 
↑ indicates that an increasing trend with the rising of injection pressure is illustrated. 
↓ indicates that a decreasing trend with the rising of injection pressure is illustrated. 
↔ indicates that this parameter is insensitive to injection pressure. 
← indicates that an advancing trend with the advancement of injection pressure is illustrated. 
– indicates that the data are not available. 
Fig. 4. Schematic diagrams of the three flow states of high-pressure gas jet [39].  
Fig. 5. Effects of injection pressure on combustion parameters [36].  
M. Li et al.

<!-- PDF_PAGE: 9 -->

Renewable and Sustainable Energy Reviews 119 (2020) 109653
9
the injection pressure was raised to 600 bar. Though injection pressure 
was raised from 270 bar to 600 bar, the trends are similar to those at 
injection pressure in the range from 100 bar to 300 bar, i.e. increases in 
injection pressure could yield improved efficiency, reduced PM, CO and 
HC emissions with penalties in NOx emissions. It should be noted that 
the natural gas supply system with injection pressure higher than 300 
bar has not been commercialized until now due to the high demand for 
the manufacture quality and the increased combustion noise accompa -
nied. From all the published studies focused on the effects of injection 
pressure, it can be summarized that the trends of NOx emissions, peak 
cylinder pressure and combustion parameter are in good agreement 
attributed to the improved diffusion speed and enhanced combustion of 
the fuel jets. However, excessive high pressure may lead to 
over-penetration, the competing effects of improved mixing and the 
over-penetration behavior would result in the uncertain trends of CO 
and HC emissions. 
2.3. Injection interval between pilot diesel and natural gas 
In pilot ignited high pressure direct injection natural gas engines, 
injection interval between pilot diesel and natural gas (DNI) is generally 
shorter than 1.5 ms (shorter than 15 
�
C A at medium engine speeds) to 
ensure the reliable ignition, but negative values are also permitted 
( Table 3 ). The injection interval between pilot diesel and natural gas 
dominates the interaction between diesel sprays and natural gas jets, 
namely, the in-cylinder mixing process; it also affects the interactions 
between combustion of both fuels, which in turn influences the gener -
ation of emissions. Dumitrescu [ 31 ] conducted one of the earliest re -
searches focused on the effects of injection interval and found that 
longer injection interval could reduce NOx emissions to a lower level 
attributed to the more split combustion process and the subsequent 
reduced combustion temperature; additionally, longer injection interval 
could result in reduced interactions between the pilot diesel and natural 
gas flame, leading to decreased HC emissions, more sufficient combus -
tion and higher thermal efficiency. Larson [ 43 ] evaluated the effects of 
injection interval in a relatively wider range; as displays by his results, 
CA10 is more sensitive to injection interval than CA50 and CA90, 
revealing a trend of first advance then delay with the extending injection 
interval; rapid combustion duration is mainly affected by the proportion 
of mixing-controlled combustion and exhibits a trend of first increase 
and then decrease; in views of emissions, high NOx emissions appear at 
shorter injection intervals owing to the higher in-cylinder temperature, 
CO and THC emissions have optimized values in the whole range of 
injection interval tested. McTaggart-Cowan et al. [ 44 , 48 ] pointed out 
that at negative and short injection intervals, the ignition of pilot diesel 
occurs in a richer atmosphere, leading to increased intensity of the 
combustion event; this could further promote the production of NOx 
emissions at all CA50 tested and result in improved thermal efficiency at 
CA50 of 0
�
BTDC and 10
�
BTDC; when injection interval is prolonged, 
possibility for the formation of over-leaning natural gas/air mixture 
would be increased and the phase for pilot diesel combustion would be 
more distinctive, resulting in increased HC at CA50 of 10
�
BTDC and 
20
�
BTDC. It can also be concluded from their results that CO emissions 
are not sensitive to injection interval with EGR fraction ranging from 
0 to 40%; however, at EGR fraction up to 50%, CO emissions could be 
effectively controlled by adopting shorter injection interval; PM emis -
sions are generally higher at relatively longer injection intervals at late 
combustion phasing and high EGR fraction. 
As could be summarized from the above studies concerning the ef -
fects of injection interval, all the researches before 2010 were performed 
at low to medium loads. In the recent years, McTaggart-Cowan et al. 
[ 49 ] conducted experiments at relatively higher load; as demonstrated 
by their results, the trends for NOx emissions and HC emissions are 
consistent with the previous studies while CO and PM show an 
increasing trend at different EGR fractions; the trends for CO and PM at 
higher load are different from those at low and medium loads because 
more fuel is introduced into the cylinder at high load conditions, thus 
increasing the sensitivity to local equivalence ratio. Owing to the simi -
larity in the test conditions and engine design, the results of Faghani 
et al. [ 50 ] are in accordance with those of McTaggart-Cowan et al. [ 49 ]. 
The variations of emissions with injection interval at idle conditions, as 
investigated by Zhang et al. [ 33 ], are not consistent with the above 
mentioned results; this can be explained by the increased sensitivity of 
cylinder pressure to pilot injection timing, resulting in earlier rapid 
pressure rise, higher peak cylinder pressure and increased NOx emis -
sions at extended injection interval; CO and HC emissions, however, 
show different trends with the extension of injection interval at different 
injection pressures. In the study of Li et al. [ 36 ], the effects of injection 
interval on combustion parameters at relatively high loads were pointed 
out, i.e. extension of injection interval could result in increased ignition 
delay, extended rapid combustion duration as well as delayed CA50 
( Fig. 6 ); these trends are similar to those found in the study of Zhang 
et al. at idle conditions [ 34 ], albeit different from those given by Larson 
[ 43 ] attributed to the differences in the range of injection interval and 
engine load. 
3. Effects of injection strategies and injector design 
3.1. Injection strategies 
Due to the flexibility of the concentric-needle dual fuel injector, the 
injection strategies can be freely adjusted to obtain different combustion 
modes, which in turn influences the engine performance and emission 
characteristics. In general, the injection strategies of pilot ignited direct 
injection natural gas engines could be classified as the following five 
common types, i.e. conventional HPDI, HCDI, HCCI, SPC and DI-NG. In 
light of the conventional HPDI injection strategies, all the natural gas is 
introduced into the cylinder after the end of pilot diesel injection by a 
single injection and the injection timings for both fuels are close to the 
Top Dead Center (TDC), thus, forming a predominantly mixing- 
controlled combustion pattern. If the single natural gas injection is 
separated into two injections, both injections are injected after the end 
of pilot diesel injection and the second injection accounts for smaller 
percentage of all the natural gas, the transformation from HPDI injection 
strategy to HPDI with post injection is achieved. For HCDI injection 
strategy, the injection of natural gas should also be split into two parts, 
one before pilot diesel injection and one after pilot diesel injection; in 
this case, the proportion of premixed combustion is enlarged. For HCCI 
injection strategy, all the natural gas is injected prior to pilot diesel in -
jection and only single injection of natural gas is adopted, forming a 
stratified mixture before diesel injection; the proportions of premixed 
and mixing-controlled combustion are dependent on the injection 
timing of both fuels. For SPC injection strategy, the start of natural gas 
injection is prior to the start of pilot diesel injection and the end of 
natural gas injection is delayed than the start of pilot diesel injection, 
which means the injections of natural gas and diesel are partly over -
lapped and the in-cylinder charge obtains a slightly premixed state. 
Extensive studies have been conducted to compare various injection 
strategies with the conventional HPDI injection strategy, all of which are 
concentrated on four stroke turbo-charged engines with the capability of 
EGR addition. As pointed out by Munshi et al. [ 51 ], who were the first 
ones to apply HCCI and HCDI combustion strategies in a pilot ignited 
direct injection natural gas engine, at idle and very low load conditions 
(lower than 25%), only conventional HPDI injection strategy could be 
applied to ensure the reliable ignition and stable operation. Subse -
quently, all the other advanced injection strategies are only meaningful 
at medium and high loads. HCDI injection strategy is more adaptable to 
conditions with engine loads higher than 50% of the full load while 
HCCI is more adaptable to conditions with engine loads ranging from 
25% to 50%. HCCI injection strategy is promising to achieve nearly zero 
NOx and soot emissions with improvements in thermal efficiency when 
appropriate proportion of EGR is added; however, the excessive high 
M. Li et al.

<!-- PDF_PAGE: 10 -->

Renewable and Sustainable Energy Reviews 119 (2020) 109653
10
Table 3 
Effects of injection interval between diesel and natural gas.  
Type of engine CR Engine speed 
(BMEP) 
Injection 
interval (
�
CA) 
PCP Combustion parameters Thermal efficiency NOx CO HC Soot or PM 
single cylinder, naturally 
aspirated, two stroke 
(Dumitrescu 1999) 
16:1 1200 rpm, 
0 – 4 bar 
(BMEP) 
3.7 – 5.9 
�
C A 
(STS) 
↓ – ↑ ↓ – ↓ – 
single cylinder, turbo-charged, 
four stroke (Larson 2003) 
19:1 1200 
rpm & 800 
rpm, 9 bar 
(IMEP) 
-4-32 
�
C A 
(STS) 
– RCD (first ↑ then ↓ ), CA10 
(first ← then → ), CA50 
( ↔ ), CA90 ( ↔ ) 
↔ First ↓ 
and 
then ↔ 
First ↓ then ↑ First ↓ then ↑ – 
single cylinder, turbo-charged, 
four stroke (McTaggart- 
Cowan 2003 & McTaggart- 
Cowan 2005) 
19:1 1200 rpm, 10 
bar (IMEP) 
 2.9-13 
�
C A 
(STS) 
↓ – ↓ (CA50 ¼
0
�
ATDC & 10
�
ATDC), 
↔ (CA50 ¼ 20
�
ATDC) 
↓ EGR and CA50 
dependent 
↔ (CA50 ¼ 0
�
ATDC), 
↓ (CA50 ¼
10
�
ATDC & 20
�
ATDC) 
↔ (CA50 ¼ 0
�
ATDC), 
↑ (CA50 ¼ 10
�
ATDC), 
EGR dependent (CA50 
¼ 20
�
ATDC) 
single cylinder, turbo-charged, 
four stroke (McTaggart- 
Cowan 2012) 
17:1 1500 rpm, 
16.6 bar 
(IMEP) 
 25.2 – 7.2 
�
C 
A (STS) 
– – ↓ ↓ ↑ ↓ (CH
4
) ↑ 
six cylinder, turbo-charged, four 
stroke (Zhang 2015) 
17:1 600 rpm, 0.03 
BMEP (idle) 
5.3 
�
C A, 7.5 
�
C A (ETS) 
↑ ignition delay ↑ , RCD ↑ , 
CA50 → , CA90 (injection 
pressure and injection 
timing dependent) 
– ↑ ↑ (DRP ¼ 150 bar 
& 180 bar), 
↓ (DRP ¼ 240 
bar) 
↔ (DRP ¼ 150 bar), ↓ (DRP 
¼ 180 bar & 240 bar) 
– 
six cylinder, turbo-charged, four 
stroke (Li 2015) 
17:1 1200 rpm, 
18.5 bar 
(BMEP) 
2.3 – 6.8 
�
C A 
(ETS) 
↓ ignition delay ↑ , RCD ↑ , 
CA50 → 
↓ – – – – 
single cylinder, turbo-charged, 
four stroke (Faghani 2017) 
17:1 1500 rpm, 
16.5 bar 
(IMEP) 
 13.5 – 13.5 
�
C A (STS) 
– – ↓ ↓ ↑ ↓ (CH
4
) ↑ 
↑ indicates that an increasing trend with the increase of injection interval is illustrated. 
↓ indicates that a decreasing trend with the increase of injection interval is illustrated. 
↔ indicates that this parameter is insensitive to injection interval. 
← indicates that an advancing trend with the advancement of injection interval is illustrated. 
→ indicates that a delaying trend with the advancement of injection interval is illustrated. 
– indicates that the data are not available. 
M. Li et al.

<!-- PDF_PAGE: 11 -->

Renewable and Sustainable Energy Reviews 119 (2020) 109653
11
peak cylinder pressure and pressure rise rate limit its use at high engine 
loads; meanwhile, the drawbacks of high CO and HC emissions may be 
encountered. HCDI injection strategy is a compromise between HPDI 
and HCCI injection strategies because the peak pressure and knock 
tendency of HCDI injection strategy are lower than those of HCCI in -
jection strategy; however, the benefits in soot emissions will be miti -
gated. Different from the study of Munshi et al. in which the comparison 
among the optimized performance of different injection strategies is the 
key point, the numerical study of Li et al. [52] mainly focused on the 
evaluation of the effects of pre-natural gas injection parameters when 
HCDI injection strategy is applied; their results suggested that once 
HCDI injection strategy is adopted, the indicated thermal efficiency 
could be improved compared with that of the natural gas single injection 
(NGSI) strategy, higher indicated thermal efficiency could be obtained 
at higher proportion of natural gas pre-injection under conditions 
without EGR while at conditions with EGR, excessive high proportion of 
natural gas could lead to impaired thermal efficiency; besides, at con -
ditions both with and without EGR, soot and CO could be reduced, 
whereas NOx will be raised by using higher proportion of natural gas 
pre-injection (Fig. 7); the variations of thermal efficiency and emissions 
with the injection timing of natural gas pre-injection, however, are 
different at different proportions of natural gas pre-injection attributed 
to the coordination between natural gas jet characteristics and 
in-cylinder flow field. 
Florea et al. [53] compared HCCI injection strategy to conventional 
HPDI injection strategy and operation mode with pilot ignition and 
premixed natural gas on a test engine same to Munshi et al. [51]; they 
found that when HCCI injection strategy is implied, the operating range 
for engine load is from 5 to 12 bar (BMEP) at 1205 rpm; the brake 
thermal efficiency could be improved up to 2% at BMEP of 12 bar while 
the improvements in thermal efficiency will be canceled at low load 
conditions; at conditions without EGR, reduced PM could be achieved 
with penalties in NOx emission, however, this problem can be mitigated 
by adding EGR; in addition, when compared to operation mode with 
pilot ignition and premixed natural gas, the primary advantage of HCCI 
Fig. 6. Effects of injection interval on combustion parameters at high load 
conditions [36]. 
Fig. 7. Effects of proportion of natural gas pre-injection (PNPI) and injection timing of natural gas pre-injection (NPSOI) for HCDI injection strategy: the red dash 
lines indicate the results of the single natural gas injection (NGSI) strategy [52]. (For interpretation of the references to colour in this figure legend, the reader is 
referred to the Web version of this article.) 
M. Li et al.

<!-- PDF_PAGE: 12 -->

Renewable and Sustainable Energy Reviews 119 (2020) 109653
12
injection strategy is the reductions in HC emissions. McTaggart-Cowan 
et al. [49] proposed the concept of SPC injection strategy for the sake 
of PM reduction; they found that increases in NOx and CH
4 
emissions 
will be accompanied when SPC injection strategy is adopted. Patychuk 
[46] focused on the PM reducing effects of SPC injection strategy in their 
study; they found that at conditions with EGR, the trade-off relationship 
between NOx and PM emissions could be broken at relatively higher 
level of premixed combustion while at conditions without EGR, the 
trade-off between NOx and PM still exists. Zoldak et al. [54] was the first 
ones to conceive the DI-NG injection strategy; the main purpose of this 
injection strategy is also the achievement of both low PM and NOx 
emissions; the main difference from the HCCI injection strategy is that 
two pilot diesel injections are adopted to obtain better control of the 
spatial reactivity, however, the drawbacks of higher peak cylinder, 
pressure rise rate and HC emissions remain; it should also be noted that 
DI-NG injection strategy has another drawback, i.e. the percentage of 
pilot diesel cannot be lower than 5% owing to the increased number of 
pilot fuel injection and the demand of stable ignition. Moreover, it 
should be noticed that only numerical results focused on the attempt of 
DI-NG injection strategy were reported, no experiment data regarding 
this injection strategy has been published until now. HPDI with post 
injection was put forward by Faghani et al. [55,56] to realize PM 
reduction; as pointed out by their studies, when CA50 and EGR fraction 
is fixed, the PM and CO emissions could be reduced by 80% percent 
without obvious variations in NOx emissions; nevertheless, these sig -
nificant reducing effects on PM and CO emissions could only be obtained 
when separation between gas injection is in the range of 1.5 ms–2.5 ms 
and proportion of natural gas post injection in the range of 15%–20%; 
meanwhile, peak cylinder pressure and fuel consumptions would in -
crease slightly; these results suggested that adopting sufficient separa -
tion between two natural gas injections and shifting enough natural gas 
in the post injection could separate the two combustion events intro -
duced by the main and post natural gas injections, leading to better 
utilization of the air in the combustion chamber; however, when the 
natural gas injections are excessively separated, the interaction between 
the combustion products produced by the two combustion events will be 
weakened, thus the temperature rise caused by the post-combustion 
event could not promote the oxidation of PM emissions. Most results 
of Li et al. [57] aligns with the results of Faghani et al. [55,56], addi -
tional findings are that at conditions without EGR, NOx emissions will 
witness an increasing trend when post injection strategy is applied; 
however, at conditions with EGR, the advantages of lower PM and CO 
emissions could be maintained without sacrifices in NOx emissions 
(Fig. 8). 
3.2. Injector design 
For the injector design of pilot ignited direct injection natural gas 
engines, though great efforts have put into the improvement of 
compactness and reliability, these modifications would not affect the 
general performance of engines [28]. For the optimization of combus -
tion and emissions, the design of injector primarily focused on the 
optimization of gas nozzles in the earlier studies. In order to evaluate the 
effects of the gas hole diameter and the design of the injector nozzle 
schematic, Douville [30] performed experiments with gas hole diameter 
of 0.41 mm and 0.51 mm; as can be summarized from his results, gas 
hole diameter has minor effects on thermal efficiency, however, NOx, 
CO and HC would get a higher value when larger gas hole diameter is 
adopted. The numerical results of Jennings and Jeske [58] related to the 
effects of gas hole diameter are consistent with those of Douville’s, i.e. 
adopting smaller hole diameter could promote the in-cylinder mixing 
process; except for the effects of gas hole diameter, Jennings and Jeske 
[58] also examined the effects of gas hole number, nozzle angle and 
injector tip height; they pointed out that excessive large number of holes 
has negative effects on natural gas/air mixing quality because plume 
merging may occur; though increasing the jet angle of natural gas could 
eliminate jet deflection and the corresponding Coanda effect, adverse 
effects on jet mixing would be induced when excessive large jet angle is 
applied; furthermore, compared with adjusting jet angle, adopting an 
appropriate injector tip height seems to be a more effective method of 
eliminating jet deflection. Dumitrescu [31] experimentally investigated 
the effects of gas nozzle number on emissions and found that when 
selecting the appropriate gas hole number, the dynamic interlace angle 
between diesel and natural gas jets should be taken into consideration as 
relative motion is permitted for a concentric-needle injector; when the 
appropriate hole number is chosen, the interlace angle should maintain 
a stable value during engine operation; as also shown by his investiga -
tion, THC at the whole range of load tested and CO at low load condi -
tions are not significantly affected by gas hole number; CO emissions at 
high load conditions increase with gas hole number and NOx emissions 
could be effectively reduced by choosing appropriate gas hole number. 
Later, some researchers sought to reduce the cost of the HPDI injector 
by simplifying the schematic of the injector. Brown et al. [29,59] was the 
first researcher to conduct a comprehensive research concerning this 
issue and proposed the design of the co-injector. For the co-injector, 
diesel is injected into the gas reservoir rather than the in-cylinder 
charge; thus, diesel could atomize and partially mix with natural gas 
before the mixture of both fuels injected into the cylinder in a pattern of 
two-phase flow; under this circumstance, the contact around the gas 
needle with the injector body could be redesigned to avoid tight toler -
ances and the consequent high manufacturing cost; apart from the lower 
cost, the co-injector also has other advantages, such as the generally 
lower PM emissions and lower low-load NOx emissions compared to the 
conventional concentric-needle injector. The major drawback of the 
co-injector, as pointed out by Brown [29], is the high demand for pilot 
fuel amount to maintain stable operation, generally twice the amount of 
the pilot fuel needed by conventional concentric-needle injectors; other 
drawbacks include the poor control at conditions with short pulse width, 
the higher CH
4 
emissions at low load conditions and the slightly higher 
cyclic variations. To resolve the main drawback of the original 
co-injectors and further reduce the cost of the injector, Laforet [60], 
Birger and Rogak [61] replaced the diesel needle with a flow restrictor; 
in this case, diesel will continuously leak into the gas reservoir instead of 
controlled by the injection signal; thereby, the actuator of diesel injec -
tion could be removed along with the diesel needle, achieving a 
simplified design; in views of CO and THC emissions, though co-injector 
with flow restrictor has similar performance as that of the original 
co-injector, reduced amount of pilot diesel is required to achieve stable 
operation; however, the problem of the poor control at low pulse width 
range still remains and an additional problem of the excessive diesel 
accumulation during braking conditions, when the injector is not firing 
Fig. 8. Comparison of different post injection strategies for HCDI injection 
strategy [57]. 
M. Li et al.

<!-- PDF_PAGE: 13 -->

Renewable and Sustainable Energy Reviews 119 (2020) 109653
13
for long period, appears unexpectedly; Birger [[62]61] further reduce 
the volume of the gas reservoir by adding sleeves outside the gas needle 
to reduce the discharge coefficient and obtain a more controllable gas 
flow rate at low load conditions; they pointed out that though the con -
trol flexibility could be improved by the optimization of the volume for 
the gas reservoir, the defection of diesel accumulation still exists, which 
leads to the possibility of pure diesel injection and deterioration of en -
gine performance after braking; solutions for this problem was also 
proposed by Birger [61[62]], i.e. adding a check value upstream in the 
gas line; nevertheless, this will undoubtedly result in increased efforts in 
design and raised cost in manufacturing, thus, has not been further 
investigated since then. 
Recent investigations on injector design are mainly focused on the 
alignment of diesel and natural gas holes. In a numerical research of Lee 
and Montgomery [63], an injector with two non-concentric needles 
were used in replacement of the conventional concentric-needle 
injector; therefore, all of their research work were based on the 
injector with two non-concentric needles; their numerical results indi -
cated that diesel included angle, gas included angle, diesel nozzle dis -
tribution and gas nozzle distribution have limited effects on thermal 
efficiency and NOx emissions; these design parameters, however, have 
evident effects on jet-wall impingement, air utilization and the subse -
quent CO emissions; generally, CO emissions will be lower with smaller 
diesel included angle and appropriate number of diesel nozzle holes 
(five holes) with evenly distributed design; in light of gas nozzles, 
optimized gas included angle and appropriate number of nozzle holes 
with properly designed uneven distribution has beneficial effects on CO 
reduction. Mabson et al. [64] evaluated the effects of the paired-hole 
design on the emissions of pilot ignited direct injection natural gas en -
gine; as can be seen from their results, all the designs with paired-hole 
nozzles have much higher PM and CO emissions than the conventional 
design at high and medium loads while have PM and CO emissions 
similar to those of the original design at low load conditions; NOx and 
CH
4 
emissions tend to be less sensitive to the paired-nozzle design; in 
general, NOx emissions of paired-hole design are slightly lower than the 
conventional design, albeit the variations in CH
4 
emissions are 
injector-design dependent; among all the paired-nozzle designs, the 
design with larger holes and small angle between gas jets seems to be the 
best one from the prospect of PM emissions and stable operation. 
4. Effects of gaseous fuel composition 
It is generally accepted that the composition of natural gas varies 
significantly with gas sources. In addition, blending natural gas with 
hydrogen has the potential to reduce emissions and achieve higher ef -
ficiency. Thus, the previous studies mainly focused on the effects for the 
proportion of commercial natural gas compositions (ethane, propane 
and nitrogen) as well as the blend ratio of hydrogen. As demonstrated by 
the results of Trusca [32], McTaggart-Cowan et al. [65,66] and Li et al. 
[67], adding hydrogen into natural gas would lead to shortened gas 
ignition delay owing to the increased activity of the gaseous fuels; at 
operating condition with low load and low speed, the effects of 
hydrogen addition on rapid combustion duration and fuel economy are 
relatively small [65], whereas at medium and high load conditions with 
medium speed, the reduced ignition delay caused by hydrogen addition 
would have a stronger impact on the combustion process, resulting in 
smaller proportion of premixed combustion, reduced rapid combustion 
duration and deteriorated thermal efficiency [66,67]; with regard to 
emissions, it was observed that at most conditions, significantly reduced 
HC, soot, PM, CO and CO
2 
emissions could be obtained by blending 
hydrogen with penalties in NOx emissions due to the lower carbon 
content, higher concentrations of free active radicals and increased 
combustion intensity (Fig. 9). 
The effects of adding ethane, propane and nitrogen into natural gas 
were mainly investigated by McTaggart-Cowan GP et al.[66, 68]; when 
the proportions of ethane and propane are increased in the gaseous fuels, 
the ignition delay of gaseous fuels would be reduced due to the lower 
octane number, leading to reduced premixed combustion and extended 
rapid combustion duration (Fig. 10); fuel economy, however, seems to 
be insensitive to the proportion of these two species; in light of emissions 
(Fig. 11), addition of ethane and propane is prone to increase the gen -
eration of PM, CO and NOx emissions owing to the higher carbon con -
tent and in-cylinder temperature while reduces HC emissions attributed 
to the delayed onset of bulk quenching. McTaggart-Cowan GP et al.[66, 
68] also examined the effects of nitrogen dilution; different from heavier 
hydrocarbons and hydrogen, nitrogen will not increase the fuel reac -
tivity but could increase the momentum of the gas jets, which in turn 
will promote the fuel/air mixing process, shorten the ignition delay and 
reduce combustion duration; these effects on mixing and combustion 
could further result in reduced HC, CO emissions at most combustion 
phasing and smaller tendency of PM generation at late combustion 
phasing; the trend for rapid combustion duration, however, is opposite 
to conditions with heavier hydrocarbons and hydrogen addition, 
showing a decreasing trend due to the improved late-cycle mixing and 
the accordingly accelerated oxidation in the post-combustion stages; it 
can also be noticed that when relatively high percentage of nitrogen is 
blended in natural gas, NOx emissions can be mitigated due to the 
reduced adiabatic flame temperature and fuel consumption could be 
reduced by a considerable percentage (Fig. 11). 
5. Conclusions 
After summarizing plenty of the published literatures on pilot ignited 
high pressure direct injection natural gas engines. The following 
Fig. 9. OH mole fraction traces of different hydrogen blend ratios (a) at DRP of 180 bar and hydrogen is added at a volumetric equivalent (VE) pattern (b) at DRP of 
180 bar and hydrogen is added at an energy equivalent (EE) pattern [67]. 
M. Li et al.

<!-- PDF_PAGE: 14 -->

Renewable and Sustainable Energy Reviews 119 (2020) 109653
14
Fig. 10. Effect of fuel on the combustion event (relative to equivalent natural-gas fuelled timing condition, all four timings are shown for each fuel composition: 50% 
IHR at 0, 5, 10, and 15 
�
ATDC) [ 66 ]. 
Fig. 11. Effect of fuel composition on emissions (relative to equivalent natural-gas fuelled timing condition, all four timings are shown for each fuel composition: 
50% IHR at 0, 5, 10, and 15 
�
ATDC) [ 66 ]. 
M. Li et al.

<!-- PDF_PAGE: 15 -->

Renewable and Sustainable Energy Reviews 119 (2020) 109653
15
conclusions could be drawn from different aspects: 
(1) Advancing injection timing could gain improved thermal effi -
ciency and advanced CA50 at most conditions; other combustion 
parameters, such as ignition delay and rapid combustion dura -
tion, have no general changing rules with variations in injection 
timing. The effects of injection timing on CO, HC and soot are not 
monotonous; CO emissions first decrease then flatten out with the 
advancement of injection timing at low load conditions and the 
tendency of deteriorated CO emissions at earlier injection timings 
may appear at high load conditions; The changing regularities of 
HC emissions with injection timing are different at different load 
and speed while soot could be reduced by advancing injection 
timing in a certain range. The effects of injection timing on NOx 
emissions are relative definite, i.e. increases in NOx emissions 
could be observed at earlier injection timings under all test 
conditions.  
(2) Some discrepancies exist in the effects of injection pressure on 
thermal efficiency; in the earlier studies, injection pressure has 
minor effects on thermal efficiency; in the recent studies, injec -
tion pressure has proved to raise thermal efficiency attributed to 
the improvements in the injection system. The effects of injection 
pressure on combustion parameters are consistent in most pre -
vious studies, i.e. raised injection pressure could result in short -
ened ignition delay, reduced rapid combustion duration and 
advanced CA50. The advanced combustion phasing and 
improved mixing could cause increased NOx emissions along 
with decreased soot and PM emissions. Since the formation 
mechanisms of CO and HC turn out to be more complex, the 
changing rules of these two emissions vary with engine load and 
speed.  
(3) Prolonged injection interval tends to have beneficial effects on 
thermal efficiency at low load conditions; at high load conditions, 
deteriorated thermal efficiency could be induced by extending 
injection interval. Regarding combustion characteristics, 
extending injection interval could lead to prolonged ignition 
delay and extended combustion duration, the effects on CA50 and 
CA90, however, are different at different operating conditions. 
From the perspective of emissions, NOx could be reduced by 
extending injection interval except for idle conditions; CO, PM 
and soot are higher while HC are lower at larger injection interval 
under most operation conditions.  
(4) All the injection strategies, including HPDI with post injection, 
HCDI, HCCI, SPC and DI-NG, are designed to further reduce the 
PM emissions of pilot ignited high pressure direct injection nat -
ural gas engines without sacrificing NOx emissions. As can be 
summarized from the published studies, all these injection stra -
tegies have the capability to realize PM control. The injection 
strategy of HPDI with post injection could reduce PM without 
impairing NOx emissions; however, all the other injection stra -
tegies would lead to raised NOx emissions; this problem could be 
easily resolved by adding EGR, thus, would not limit their 
application. Among all the injection strategies, DI-NG is less 
investigated as the substitution of diesel cannot meet the future 
requirements. HCCI is limited to low and medium load conditions 
due to the apparently higher pressure rise rate. Though HCDI and 
SPC injection strategies could extend the load range to a higher 
level, the PM reducing effects are weaker than that of HCCI in -
jection strategy. At extremely low load conditions, HPDI injection 
strategy is the only choice in order to maintain stable operation. 
Overall, optimized general performance could be gained by the 
combined use of various injection strategies.  
(5) For conventional concentric-needle dual fuel injector, it can be 
found that using relatively smaller diameter of nozzle hole could 
obtain lower emissions. For a specific nozzle diameter, there exist 
optimized values for the number of nozzle holes, the jet included 
angle and injector tip height. Even if the paired-nozzle design is 
proposed for PM emission reduction, the result is not as expected, 
the resulted PM emissions would be worse rather than improved. 
The concept of co-injector has the capability of PM reduction, 
however, the difficulties in the electric control at low load con -
ditions and the misfiring behavior during braking conditions are 
two flaws of this type of injector, which limit its commercial use.  
(6) Adding hydrogen into natural gas could achieve obvious lower 
HC, CO, CO
2 
and PM emissions, whereas NOx emissions would 
increase at conditions without EGR addition; besides, ignition 
delay would reduce due to the increased concentration of active 
radicals and thermal efficiency could be improved at relatively 
high loads with sufficient addition of hydrogen. Increasing the 
proportion of ethane and propane in natural gas has no signifi -
cant effects on fuel economy while has negative effects on all 
emissions except HC. Diluting natural gas with nitrogen is a 
feasible method for the emission control of CO and HC, PM 
emissions also witness reductions at certain combustion timings. 
Different from blending other compositions, adding sufficient 
nitrogen could achieve both NOx reduction and considerable 
improvements in fuel economy. 
Acknowledgement 
This work was supported by the National Natural Science Foundation 
of China (No.51906057), the Science and Technology Research Project 
of Colleges and Universities in Hebei Province (No.QN2019056), the 
Science Fund for Young Scholars of Natural Science Fund in Hebei 
Province(No.E2019202198), National Engineering Laboratory for Mo -
bile Source Emission Control Technology(No.NELMS2018A10), Science 
and Technology Directorate Project of Tianjin City(No.18ZXSZSF00060) 
and Science and Technology Program of Hebei Province 
(No.17274006D), Tianjin Key Laboratory of Power Transmission and 
Safety Technology for New Energy Vehicles and Hebei Engineering 
Research Center of Pollution Control in Power System. It should also be 
noted that the reuse permission for all the figures cited in this paper has 
been obtained by the authors. 
Appendix A. Supplementary data 
Supplementary data to this article can be found online at https://doi. 
org/10.1016/j.rser.2019.109653. 
References 
[1] Wei LJ, Yao CD, Wang QG, Pan W, Han GP. Combustion and emission 
characteristics of a turbocharged diesel engine using high premixed ratio of 
methanol and diesel fuel. Fuel 2015;140:156–63. 
[2] Farrell JT, Cernansky NP, Dryer FL, Friend DG, Hergart CA, Law CR, McDavid R, 
Mueller CJ, Pitsch H. Development of an experimental database and kinetic models 
for surrogate diesel fuels. Technical Paper No. 2007-01-0201. SAE; 2007. 
[3] Bayraktar H. An experimental study on the performance parameters of an 
experimental CI engine fueled with diesel–methanol–dodecanol blends. Fuel 2008; 
87(2):158–64. 
[4] Lawrence MG, Crutzen PJ. Influence of NOx emissions from ships on tropospheric 
photochemistry and climate. Nature 1999;402(11):167–70. 
[5] Koenig JQ. Health effects of sulfur oxides: sulfur dioxide and sulfuric acid. In: 
Koenig JQ, editor. Health effects of ambient air pollution. Boston: Springer; 2000. 
p. 99–114. 
[6] Raub JA, Mathieu-Nolf M, Hampson NB, Thom SR. Carbon monoxide poisoning—a 
public health perspective. Toxicology 2000;145(1):1–14. 
[7] Anderson JO, Thundiyil JG, Stolbach A. Clearing the air: a review of the effects of 
particulate matter air pollution on human health. J Med Toxicol 2012;8(2):166–75. 
[8] Weaver CS. Natural gas vehicles–a review of the state of the art. Technical Paper 
No. 892133. SAE; 1989. 
[9] Liu SH, Zhou LB, Wang ZY, Ren J. Combustion characteristics of compressed 
natural gas/diesel dual-fuel turbocharged compressed ignition engine. P I Mech 
Eng D-J Automot 2003;217(9):833–8. 
[10] Cho HM, He BQ. Spark ignition natural gas engines—a review. Energy Convers 
Manag 2007;48:608–18. https://doi.org/10.1016/j.enconman.2006.05.023. 
M. Li et al.

<!-- PDF_PAGE: 16 -->

Renewable and Sustainable Energy Reviews 119 (2020) 109653
16
[11] Korakianitis T, Namasivayam AM, Crookes RJ. Natural-gas fueled spark-ignition 
(SI) and compression-ignition (CI) engine performance and emissions. Prog Energy 
Combust 2011;37:89 – 112 . 
[12] NGV Global.Current natural gas vehicle statistics, http://www.iangv.org/curren 
t-ngv-stats/ . 
[13] the Oxford Institute for Energy. A review of prospects for natural gas as a fuel in 
road transport. https://www.oxfordenergy.org/wpcms/wp-content/uploads/2 
019/04/A-review-of-prospects-for-natural-gas-as-a-fuel-in-road-transport-Insight- 
50.pdf?v ¼ 1c2903397d88 . 
[14] A review of demand prospects for LNG as a marine transport fuel. https://www. 
oxfordenergy.org/wpcms/wp-content/uploads/2018/07/A-review-of-demand-pr 
ospects-for-LNG-as-a-marine-fuel-NG-133.pdf . 
[15] British Petroleum. Statistical review of world energy, https://www.bp.com/en/gl 
obal/corporate/energy-economics/statistical-review-of-world-energy/natural-gas. 
html . 
[16] Zou CN, Yang Z, He DB, Wei YS, Li J, Jia A, Chen JJ, Zhao Q, Li Y, Li J, Yang S. 
Theory, technology and prospects of conventional and unconventional natural gas. 
Pet Explor Dev 2018;45(4):604 – 18 . 
[17] Assefa HD, Ahlgren EO. Well-to-wheel assessment of natural gas vehicles and their 
fuel supply infrastructures-Perspectives on gas in transport in Denmark. Trans Res 
D-Tr E 2018;65:14 – 35 . 
[18] Sahoo BB, Sahoo N, Saha UK. Effect of engine parameters and type of gaseous fuel 
on the performance of dual-fuel gas diesel engines — a critical review. Renew 
Sustain Energy Rev 2009;13(6):1151 – 84 . 
[19] Abagnale C, Cameretti MC, De Simio L, Gambino M, Iannaccone S, Tuccillo R. 
Numerical simulation and experimental test of dual fuel operated diesel engines. 
Appl Therm Eng 2014;65(1 – 2):403 – 17 . 
[20] Lounici MS, Loubar K, Tarabet L, Balistrou M, Niculescu DC, Tazerout M. Towards 
improvement of natural gas-diesel dual fuel mode: an experimental investigation 
on performance and exhaust emissions. Energy 2014;64:200 – 11 . 
[21] Yang B, Xi C, Wei X, Zeng K, Lai MC. Parametric investigation of natural gas port 
injection and diesel pilot injection on the combustion and emissions of a 
turbocharged common rail dual-fuel engine at low load. Appl Energy 2015;143: 
130 – 7 . 
[22] Liu J, Yang F, Wang H, Ouyang M, Hao S. Effects of pilot fuel quantity on the 
emissions characteristics of a CNG/diesel dual fuel engine with optimized pilot 
injection timing. Appl Energy 2013;110:201 – 6 . 
[23] Goudie D, Dunn M, Munshi SR, Lyford-Pike E, Wright Jo, Duggal V, Frailey M. 
Development of a compression ignition heavy duty pilot-ignited natural gas fuelled 
engine for low NOx emissions. Technical Paper No. 2004-01-2954. SAE; 2004 . 
[24] Jones HL. Source and characterization of particulate matter from a pilot-ignited 
natural gas fuelled engine. Master Thesis. Vancouver: University of British 
Columbia; 2004 . 
[25] Zhao H. Direct injection natural gas engines. In: Zhao H, editor. Advanced direct 
injection combustion engine technologies and development. Cambridge: 
Woodhead Publishing Ltd.; 2010. p. 199 – 228 . 
[26] Hill PG, Douville B. Analysis of combustion in diesel engines fueled by directly 
injected natural gas. J Eng Gas Turbines Power 2000;122(1):141 – 9 . 
[27] Faghani E, Kirchen P, Rogak SN. Application of fuel momentum measurement 
device for direct injection natural gas engines. Technical Paper 2015-01-0915. 
SAE; 2015 . 
[28] Ouellette P, Goudie D, McTaggart-Cowan G. Progress in the development of natural 
gas high pressure direct injection for Euro VI heavy-duty trucks. In: Liebl J, Beidl C, 
editors. Internationaler motorenkongress 2016. Wiesbaden: Springer Vieweg; 
2016. p. 591 – 607 . 
[29] Brown BS. High-pressure direct-injection of natural gas with entrained diesel into a 
compression-ignition engine. Master Thesis. Vancouver: University of British 
Columbia; 2008 . 
[30] Douville B. Performance, emissions and combustion characteristics of natural gas 
fueling of diesel engines. Master Thesis. Vancouver: University of British Columbia; 
1994 . 
[31] Dumitrescu S. Pilot ignited high pressure direct injection of natural gas fueling of 
diesel engines. Master Thesis. Vancouver: University of British Columbia; 1999 . 
[32] Trusca B. High pressure direct injection of natural gas and hydrogen fuel in a diesel 
engine. Master Thesis. Vancouver: University of British Columbia; 2001 . 
[33] Harrington J, Munshi S, Nedelcu C, Ouellette P, Thompson J, Whitfield S. Direct 
injection of natural gas in a heavy-duty diesel engine. Technical Paper 2002-01- 
1630. SAE; 2002 . 
[34] Zhang Q, Li MH, Li GX, Shao SD. Emission effects of injection parameters on the 
combustion and emission characteristics of diesel-piloted direct-injection natural 
gas engine during idle conditions. J Energy Eng 2015;141(4):04014043 . 
[35] Zhang Q, Li MH, Shao SD. Combustion process and emissions of a heavy-duty 
engine fueled with directly injected natural gas and pilot diesel. Appl Energy 2015; 
157:217 – 28 . 
[36] Li M, Zhang Q, Li GX, Shao SD. Experimental investigation on performance and 
heat release analysis of a pilot ignited direct injection natural gas engine. Energy 
2015;90:1251 – 60 . 
[37] Vuorinen V, Wehrfritz A, Duwig C, Boersma BJ. Large-eddy simulation on the 
effect of injection pressure and density on fuel jet mixing in gas engines. Fuel 2014; 
130:241 – 50 . 
[38] Yu J, Vuorinen V, Kaario O, Sarjovaara T, Larmi M. Visualization and analysis of 
the characteristics of transitional underexpanded jets. Int J Heat Fluid Flow 2013; 
44:140 – 54 . 
[39] Dong Q, Li Y, Song EZ, Yao C, Fan LY, Sun J. The characteristic analysis of high- 
pressure gas jets for natural gas engine based on shock wave structure. Energy 
Convers Manag 2017;149:26 – 38 . 
[40] Mtui P. Pilot-ignited natural gas combustion in diesel engines. Doctoral thesis. 
Vancouver: University of British Columbia; 1996 . 
[41] Yu JZ, Vuorinen V, Kaario O, Sarjovaara T, Larmi M. Characteristics of high 
pressure jets for direct injection gas engine. technical paper No.2013-01-1619. 
SAE; 2013 . 
[42] Ouellette P. High pressure injection of natural gas for diesel engine fueling. Master 
Thesis. Vancouver: University of British Columbia; 1992 . 
[43] Larson CR. Injection study of a diesel engine fueled with pilot-ignited, directly- 
injected natural gas. Master Thesis. Vancouver: University of British Columbia; 
2003 . 
[44] McTaggart-Cowan GP, Bushe WK, Rogak SN, Hill PG, Mushi SR. Injection 
parameter effects on a direct injected, pilot ignited, heavy duty natural gas engine 
with EGR. technical paper No. 2003-01-3089. SAE; 2003 . 
[45] McTaggart-Cowan GP, Jones HL, Bushe WK, Rogak SN, Hill PG. The effects of high- 
pressure injection on a compression – ignition, direct injection of natural gas engine. 
J Eng Gas Turbines Power 2007;129(2):579 – 88 . 
[46] Patychuk BD. Particulate matter emission characterization from a natural-gas high- 
pressure direct-injection engine. Master Thesis. Vancouver: University of British 
Columbia; 2013 . 
[47] McTaggart-Cowan GP, Mann K, Huang J, Singh A, Patychuk B, Zheng ZX, 
Munshi S. Direct injection of natural gas at up to 600 Bar in a pilot-ignited heavy- 
duty engine. Technical Paper No. 2015-01-0865. SAE; 2015 . 
[48] McTaggart-Cowan GP, Bushe WK, Rogak SN, Hill PG, Mushi SR. PM and NOx 
reduction by injection parameter alterations in a direct injected, pilot ignited, 
heavy duty natural gas engine with EGR at various operating conditions. Technical 
Paper No.2005-01-1733. SAE; 2015 . 
[49] McTaggart-Cowan GP, Mann K, Huang J, Wu N, Munshi SR. Particulate matter 
reduction from a pilot-ignited, direct injection of natural gas Engine. Proc ASME 
2012 Int Combust Eng Div Fall Tech Conf 2012:ICEF2012-92162 . 
[50] Faghani E, Kheirkhah P, Mabson CWJ, McTaggart-Cowan G, Kirchen P, Rogak S. 
Effect of Injection Strategies on Emissions from a pilot-ignited direct-injection 
natural-gas engine- Part II: slightly premixed combustion. Technical Paper No. 
2017-01-0763. SAE; 2017 . 
[51] Munshi SR, McTaggart-Cowan GP, Huang J, Hill PG. Development of a partially- 
premixed combustion strategy for a low-emission, direct injection high efficiency 
natural gas engine. Proc ASME 2011 Int Combust Eng Divi Fall Tech Conf 2011: 
ICEF2011-60181 . 
[52] Li MH, Zheng XL, Zhang Q, Li ZG, Shen BX, Liu XR. The effects of partially 
premixed combustion mode on the performance and emissions of a direct injection 
natural gas engine. Fuel 2019;250:218 – 34 . 
[53] Florea R, Neely GD, Abidin Z, Miwaj J. Efficiency and emissions characteristics of 
partially premixed dual-fuel combustion by co-direct injection of NG and diesel 
fuel (DI2). Technical Paper No. 2016-01-0779. SAE; 2016 . 
[54] Zoldak P, Sobiesiak A, Wickman D, Bergin M. Combustion simulation of dual fuel 
CNG engine using direct injection of natural gas and diesel. Technical Paper No. 
2015-01-0851. SAE; 2015 . 
[55] Faghani E, Patychuk B, McTaggart-Cowan G, Rogak S. Soot emission reduction 
from post injection strategies in a high pressure direct-injection natural gas engine. 
Technical Paper No. 2013-24-0114. SAE; 2013 . 
[56] Faghani E, Kheirkhah P, Mabson CWJ, McTaggart-Cowan GP, Kirchen P, Rogak S. 
Effect of injection strategies on emissions from a pilot-ignited direct-injection 
natural-gas engine- Part I: late post injection. Technical Paper No. 2017-01-0774. 
SAE; 2017 . 
[57] Li MH, Zhang Q, Liu XR, Ma YX, Zheng QP. Soot emission prediction in pilot 
ignited direct injection natural gas engine based on n-heptane/toluene/methane/ 
PAH mechanism. Energy 2018;163:660 – 81 . 
[58] Jennings MJ, Jeske FR. Analysis of the injection process in direct injected natural 
gas engines: Part II — effects of injector and combustion chamber design. J Eng Gas 
Turbines Power 1994;116:806 – 13 . 
[59] Brown BS, Rogak SN, Munshi S. Multiple injection strategy in a direct-injection 
natural gas engine with entrained diesel. Technical Paper No. 2009-01-1954. SAE; 
2009 . 
[60] Laforet CA. Combustion of natural gas with entrained diesel in a heavy-duty 
compression-ignition engine. Master Thesis. Vancouver: University of British 
Columbia; 2009 . 
[61] Birger NJ, Rogak SN. Flow characteristics of a gas-blast fuel injector for direct- 
injection compression-ignition engines. Technical Paper No. 2009-01-1857. SAE; 
2009 . 
[62] Birger NJ. Flow characteristics of gas-blast fuel injectors for direct-injection 
compression-ignition engine. Master Thesis. Vancouver: University of British 
Columbia; 2010 . 
[63] Lee WG, Montgomery D. Numerical investigation of the performance of a high 
pressure direct injection (HPDI) natural gas engine. ICEF2014-5681 Proc ASME 
2014 Int Combust Eng Div Fall Tech Conf 2014:ICEF2014-5681 . 
[64] Mabson CWJ, Faghani E, Kheirkhah P, Kirchen P, Rogak SN, McTaggart-Cowan GP. 
Combustion and emissions of paired-nozzle jets in a pilot-ignited direct-injection 
natural gas engine. Technical paper No. 2016-01-0807. SAE; 2016 . 
[65] McTaggart-Cowan GP, Jones HL, Rogak SN, Bushe WK, Hill PG, Munshi SR. Direct- 
injected hydrogen-methane mixtures in a heavy-duty compression ignition engine. 
Technical paper No. 2006-01-0653. SAE; 2006 . 
M. Li et al.

<!-- PDF_PAGE: 17 -->

Renewable and Sustainable Energy Reviews 119 (2020) 109653
17
[66] McTaggart-Cowan GP, Rogak SN, Munshi SR, Hill PG, Bushe WK. The influence of 
fuel composition on a heavy-duty, natural-gas direct-injection engine. Fuel 2010; 
89:752–9. 
[67] Li MH, Zhang Q, Li GX, Li PX. Effects of hydrogen addition on the performance of a 
pilot-ignition direct-injection natural gas engine: a numerical study. Energy Fuel 
2017;31(4):4407–23. 
[68] McTaggart-Cowan GP, Wu N, Jin B, Rogak SN, Davy MH, Bushe WK. Effects of fuel 
composition on high-pressure non-premixed natural gas combustion. Combust Sci 
Technol 2009;181(3):397–416. 
M. Li et al.
