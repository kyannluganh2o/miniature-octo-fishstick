<!-- PDF_PAGE: 1 -->

Dual-fuel dual-direct injection: An efficient and clean combustion
technology for diesel engines
Tao Li
a
, Pengyun Zhao
b
, Haibin He
c
, Chunguang Wang
a
, Haitao Zhang
b
,
Zhanming Chen
b , c , *
, Hao Chen
b
a
School of Energy and Power Engineering, Xi ’ an Jiaotong University, Xi ’ an, 710049, PR China
b
Shaanxi Key Laboratory of New Transportation Energy and Automotive Energy Saving, School of Energy and Electrical Engineering, Chang ’ an University, Xi ’ an,
710064, PR China
c
Ningbo C.S.I. Power & Machinery Group Co., Ltd, Ningbo, 315020, PR China
ARTICLE INFO
Handling Editor: Dr. Paul Williams
Keywords:
Diesel engine
Dual-fuel direct injection
Renewable fuels
Combustion characteristics
Emission characteristics
ABSTRACT
The reduction of pollutant emissions from diesel engines and achievement of a carbon-neutral transportation
sector requires the improvement of traditional diesel engine combustion. Dual-fuel combustion modes have been
introduced to promote the application of renewable fuels in diesel engines accordingly. However, traditional
dual-fuel combustion is limited by poor stability, low renewable fuel substitution rate, narrow operating con-
ditions, and high pollutant emissions. Dual-fuel direct injection (DFDI) has been proposed to address these
problems. This paper critically reviews the latest research on and compares the advantages of DFDI combustion
with those of other combustion modes and evaluates the performance, combustion, and emissions characteristics
of diesel – gasoline, diesel – natural gas, diesel – methanol, diesel – ammonia, and diesel – hydrogen DFDI engines.
When using DFDI, the fuel injection strategy is more flexible, the concentration and activity distributions of the
different fuels in the cylinder can be effectively controlled, and there is considerable potential for combustion
optimization. Furthermore, the DFDI engine exhibits a higher power output, better thermal efficiency, and
significantly improved combustion stability compared to the conventional diesel engine. These advantages
broaden the engine working conditions, increase the replacement rate of diesel with renewable fuels, and reduce
the emissions of carbon monoxide, hydrocarbons, nitrogen oxides, particulate matter, soot, and other pollutants.
Nomenclature
ICE internal combustion engine CO
2
carbon dioxide
HC hydrocarbons NOx nitrogen oxide
PM particulate matter CI compression ignition
UHCs unburned hydrocarbons CO carbon monoxide
NG natural gas DME dimethyl ether
HCCI homogeneous charge
compression ignition
DFDI dual fuel direct injection
RCCI reactivity controlled
compression ignition
LHV latent heat of vaporization
DGDFDI diesel/gasoline dual fuel
direct injection
PCCI premixed charge
compression ignition
DNGDFDI diesel/natural gas dual fuel
direct injection
DMDFDI diesel/methanol dual fuel
direct injection
CVCC constant volume
combustion chamber
DHDFDI diesel/hydrogen dual fuel
direct injection
( continued on next column )
( continued )
Nomenclature
DMCC diesel/methanol combined
combustion
DADFDI diesel/ammonia dual fuel
direct injection
EGR exhaust gas recirculation ITE indicated thermal
efficiency
ICCI intelligent charge
compression ignition
SOI
g
start of gasoline injection
IMEP indicated mean effective
pressure
SOI
d
start of diesel injection
STP spray tip penetration E
g
gasoline DI energy fraction
SPA spray projected area HPDI high pressure direct
injection
SMOI start of methanol injection CDI conventional direct
injection
E
d
diesel DI energy fraction DI2 dual direct injection
( continued on next page )
* Corresponding author. Shaanxi Key Laboratory of New Transportation Energy and Automotive Energy Saving, School of Energy and Electrical Engineering,
Chang ’ an University, Xi ’ an, 710064, PR China.
E-mail address: ZM_Chen@chd.edu.cn (Z. Chen).
Contents lists available at ScienceDirect
Journal of the Energy Institute
journal homepag e: www.el sevier.com/loc ate/joei
https://doi.org/10.1016/j.joei.2025.102006
Received 30 November 2024; Received in revised form 14 January 2025; Accepted 15 January 2025
Journal of the Energy Institute 119 (2025) 102006 
Available online 20 January 2025 
1743-9671/© 2025 The Energy Institute. Published by Elsevier Ltd. All rights are reserved, including those for text and data mining, AI training, and similar 
technologies.

<!-- PDF_PAGE: 2 -->

( continued )
Nomenclature
ATDC after top dead center BTDC before top dead center
CA crank angle No
z
nozzle number
SINL spatial integrated natural
luminosity
Ro
t
rotation angle
MESR methanol energy
substitution ratio
CAD crank angle degree
P
inj
injection pressure BTE brake thermal efficiency
Δ t injection interval FLOL flame lifted-off length
SA spray angle RON research octane number
1. Introduction
1.1. Overview
The internal combustion engine (ICE) is the primary power device
used in transportation, construction machinery, agricultural machinery,
fishing vessels, and defensive equipment [ 1 ]. In China, 44.7012 million
ICEs were sold in 2023 (5,116,500 diesel and 39,584,700 gasoline) [ 2 ].
The enormous quantity of ICEs in China consumes more than 60 % of the
petroleum in the country every year and produces more than 9.8 % of
national carbon dioxide (CO
2
) emissions. Indeed, the transportation
sector, particularly road transportation, is among the largest consumers
of energy and producers of pollutants worldwide. In 2023, the emissions
of carbon monoxide (CO), hydrocarbons (HC), nitrogen oxides (NO
x
)
and particulate matter (PM) from motor vehicles in China were 7.43
million tons, 1.912 million tons, 5.267 million tons and 53,000 tons,
respectively; vehicles are responsible for more than 90 % of these
emissions. Furthermore, diesel vehicles accounted for more than 80 %
and 90 % of the total NO
x
and PM, respectively, emitted by automobiles,
while gasoline vehicles accounted for 80 % of the total CO and HC
emissions [ 2 ]. These pollutants cause significant harm to the global
environment, climate, and human health. as shown in Fig. 1 , global
greenhouse gas emissions are still at high levels. Excessive CO
2
emis-
sions have created a serious greenhouse effect that has resulted in a
global increase in temperatures and extreme weather frequency [ 3 ].
Therefore, various countries have established carbon neutrality targets
in line with national conditions [ 4 ], as shown in Figs. 1 and 2 , with the
goal of achieving global carbon neutrality by 2060 [ 5 ]. As a result,
emissions and fuel efficiency regulations are becoming increasingly
stringent in the transportation sector [ 6 ].
The depletion of fossil fuel resources and growing demand for eco-
friendly vehicles require the development of power sources with high
thermal efficiencies and ultra-low emissions. In response to the dual
stresses exerted by energy and environmental constraints, considerable
progress has been made in improving and supplementing the fuel supply
systems, air management systems, post-processing technologies, and
other internal mechanisms of ICEs [ 7 – 11 ] using advanced electronic
control technologies [ 12 – 15 ]. Indeed, ICEs have shown significant po-
tential for combustion optimization and emissions improvement.
Recently, researchers have attempted to meet stringent emissions re-
quirements by developing cleaner alternative fuels and improving
advanced combustion modes [ 16 – 18 ]. The development of clean fuels
and the application of such combustion modes have gradually shifted
the focus of the diesel-fueled vehicle market from “ high performance ” to
“ low fuel consumption ” and “ low CO
2
emissions ” accordingly.
1.2. Advanced ICE technologies
Compared to gasoline engines, diesel engines have a higher thermal
efficiency that can reach 40 – 55 % [ 19 ]. However, diesel engines also
generate more pollutants such as CO, unburned hydrocarbons (UHCs),
NO
x
, and PM [ 20,22 ]. In addition, traditional diesel engine combustion
is controlled by spray diffusion [ 23 ]. The diesel spray burns simulta-
neously as it spreads, inevitably forming local over concentration and
high-temperature areas [ 24 , 25 ]. Critically, NO
x
is generated in
high-temperature oxygen-enriched conditions, whereas soot is gener-
ated in high-temperature oxygen poverty conditions [ 168 ]. These con-
trasting conditions cause one type of emissions to rise as the other falls.
Consequently, realizing the simultaneous reduction of NO
x
and soot
emissions from traditional diesel ICEs is quite difficult [ 27 ]. Combustion
optimization is at the core of ICE research, and researchers and engi-
neers in the ICE industry have accordingly proposed the homogeneous
charge compression ignition (HCCI) [ 28 – 30 ], premixed charge
compression ignition (PCCI) [ 31 – 33 ], reactivity-controlled compression
ignition (RCCI) [ 34 – 36 ], and dual-fuel direct injection (DFDI) [ 37 , 38 ]
combustion modes to solve the problem of high emissions from diesel
ICEs. Fig. 3 compares the fuel equivalent ratio ( φ ) vs ambient temper-
ature ( T ) curves for these different combustion modes, among which the
most interesting and promising is DFDI.
As shown in Fig. 3 , HCCI combustion completely avoids the soot
generation region and occupies only a small part of the NO
x
generation
region; however, the associated ignition and combustion rates are
extremely fast [ 39 ] and the pressure increase rate and mechanical load
are quite high [ 40 ]. In addition, HCCI is a homogeneous combustion
process controlled by chemical reaction dynamics, making it extremely
sensitive to boundary conditions such as temperature, pressure, and
equivalence ratio in the cylinder [ 41 ]. Furthermore, HCCI combustion is
difficult to effectively control under variable operating conditions and
engine loads, making its effective operation area extremely narrow
[ 42 – 44 ]. Researchers developed PCCI combustion to expand the load
range for low-temperature combustion [ 45 ] using multiple injections
Fig. 1. Greenhouse gas emissions over the years.
T. Li et al. Journal of the Energy Institute 119 (2025) 102006 
2

<!-- PDF_PAGE: 3 -->

Fig. 2. Exhaust gas regulations and future fuel economy target [ 6 ].
T. Li et al. Journal of the Energy Institute 119 (2025) 102006 
3

<!-- PDF_PAGE: 4 -->

combined with exhaust gas recirculation (EGR) to control fuel com-
bustion in the partially homogeneous state formed by early injection and
the concentration stratification state formed in late injection [ 46 ]. The
concentration stratification of the fuel in PCCI can effectively slow the
combustion heat release rate to increase the engine load. Notably, PCCI
exhibits a wider range of temperatures and equivalence ratios than HCCI
while avoiding the soot generation region and occupying only a small
portion of the NO
x
generation region [ 47 ]. However, neither HCCI nor
PCCI can be easily ignited at small load, resulting in a narrow operating
range and high emission of pollutants (CO and HC). Indeed, different
engine loads require different injection activities to achieve efficient and
clean combustion [ 48 ].
Reitz et al. [ 49 – 51 ] proposed an RCCI combustion mode that
included the injection of a low-activity fuel with a high octane number
(such as gasoline or methanol) at the inlet and the direct injection of a
high-activity fuel with a high cetane number (such as diesel, biodiesel,
or dimethyl ether) in the cylinder. This system allows different degrees
of activity and concentration stratification to be obtained by adjusting
the injection ratio between the two fuels and the injection strategy for
the high-activity fuel, achieving efficient and clean combustion over a
wide range of engine loads. Indeed, Kokjohn [ 50 ] reported that RCCI
combustion can operate over a wide range of engine loads with
near-zero levels of NO
x
and soot emissions. Furthermore, the RCCI en-
gine has an acceptable rate of pressure increase and ringing intensity as
well as an extremely high indicated efficiency, as shown in Fig. 4 . A
comparison between RCCI and conventional diesel combustion
indicated a reduction in NO
x
emissions by three orders of magnitude, a
six-fold reduction in soot emissions, and a 16.4 % increase in gross
indicated efficiency. Compared to HCCI and PCCI, the load range of
RCCI combustion is extended to a 24 bar brake mean effective pressure
[ 52 ]. However, while NO
x
and PM can be maintained at lower levels
when using RCCI, these levels do not fully cover the actual operating
load range of the engine [ 53 ]. In addition, while the use of port injection
creates a generally homogeneous environment in the cylinder, local
regions can exhibit low reactivity and equivalence ratios, leading to
incomplete combustion and significantly increased CO and HC emis-
sions. Furthermore, port injection leads to pumping and volumetric
losses that reduce the effective power of the engine. Therefore, re-
searchers developed dual-fuel direct injection (DFDI) combustion mode
[ 54 – 56 ] to overcome the inefficiencies of the port-injection RCCI mode.
The lower pumping loss and more precise fuel control provided by the
use of direct injection considerably improves thermal efficiency and
engine performance compared to the use of port injection.
Wissink et al. [ 57 ] proposed a novel injection strategy for DFDI
combustion by comparing the characteristics of RCCI, PPCI, and DFDI
combustion at a nominal gross mean effective pressure of 0.9 MPa.
Notably, DFDI allowed combustion phasing near the top dead center
(TDC) with reduced combustion noise, and the cyclic combustion
instability was significantly reduced. Furthermore, DFDI combustion
exhibited less noise and required less EGR than RCCI combustion to
achieve a similar efficiency, and exhibited less noise and greater effi-
ciency than PPCI combustion. Indeed, DFDI can be considered to
combine the efficiency advantage of RCCI with the engine load advan-
tage of PPCI while reducing the need for EGR and the occurrence of
combustion instability. In contrast to RCCI, the two different fuels used
in DFDI are controlled by two independent injection systems, allowing
the distribution of reactivity and equivalence ratio, as well as the
different combustion modes, to be adapted to different working condi-
tions. As a result, the DFDI combustion is expected to cover the entire
operating region with satisfactory performance.
Recently, the University of Wisconsin [ 58 ], Lund University [ 59 ],
Dalian University of Technology [ 60 ] and Shanghai Jiao Tong Univer-
sity [ 61 ] have successively conducted research on efficient and clean
compression-ignition combustion engines using DFDI. In these engines,
two sets of direct fuel injection systems are used to realize dual-fuel
multi-pulse in-cylinder injection. The injection phase and duration of
each pulse can be changed by co-regulating the two fuel injection stra-
tegies to achieve flexible control of the fuel reactivity as well as the
distribution of the mixture in the cylinder. This realizes the accurate
control of ignition and heat release in each cycle as well as the com-
bustion phase and rate, peak cylinder pressure, and pressure increase
rate to improve thermal efficiency, reduce pollutant emissions, and
expand the available engine load. Clearly, DFDI represents a promising
combustion mode for achieving satisfactory engine performance with
effective control of the ignition and combustion processes.
1.3. Clean alternative fuels for dual-fuel engines
Achieving efficient and clean combustion using a single fuel under a
wide range of operating conditions is difficult owing to the limitations of
its physical and chemical properties [ 62 ]. A notable advantage of
dual-fuel combustion is that fuels with different activities can be used to
adapt to different engine operating conditions and loads [ 63 – 65 ].
Currently, dual-fuel combustion predominantly uses a combination of
diesel and a zero-carbon or low-carbon fuel [ 66 ]. Fig. 5 shows the
transition pathways from primary energy sources to a selection of sus-
tainable, renewable fuels [ 67 ] used in dual-fuel diesel combustion,
including alcohols, biogas, ethers, esters, and hydrogen [ 68 ]. These fuels
represent effective alternatives for reducing NO
x
, greenhouse gas, and
PM emissions [ 69 – 72 ]. Researchers have identified alcohols, natural
gas, biodiesel, dimethyl ether (DME), ammonia, and hydrogen as
promising candidates for alternative fuels to reduce the operating costs
Fig. 3. Operating range of various combustion concepts [ 154 ].
Fig. 4. Equivalence ratio versus temperature plot comparing conventional
diesel (circles) and RCCI combustion (triangles) at 5
◦
ATDC [ 50 ].
T. Li et al. Journal of the Energy Institute 119 (2025) 102006 
4

<!-- PDF_PAGE: 5 -->

and harmful emissions of diesel engines [ 16 , 73,74,169 ]. For DME,
methanol, ammonia and hydrogen, they all have flash boiling properties
[ 76 , 77 ]. Flash boiling spray, recognized as a promising atomization
technique, has been proven to achieve superior atomization [ 75 , 78 , 79 ].
Table 1 shows the physical, chemical, and thermal properties of these
various fuels. The parameters applied with each fuel determine its per-
formance in a compression-ignition combustion engine in terms of
aeration cooling effect, volatility, spray, ignition, combustion dynamics,
and pollutant emission characteristics.
In particular, oxygen-containing fuels, such as alcohols and ethers,
can significantly reduce CO and HC emissions [ 80 ]. Meanwhile, these
fuels can also decrease the flame temperature in the combustion
chamber, thereby reducing NO
x
emissions [ 81 ]. However, oxygenated
fuels have a smaller lower heating value (LHV), a lower octane number,
and higher evaporation enthalpy, which can cause engine cold-start
problems. In contrast, some oxygen-containing fuels (such as alcohols)
exhibit a high LHV and low cetane number that reduces the maximum
combustion pressure in the cylinder at a low engine load and decreases
the temperature of the combustion starting point, worsening the
combustion conditions and even causing engine misfire [ 82 ]. Typically,
employing an oxygenated fuel with a high cetane number or comple-
mentary dual fuel can solve the above problems.
Among the potential zero-carbon fuels, ammonia and hydrogen have
higher octane numbers and exhibit excellent anti-knock performance.
Hydrogen has the unique advantages of high calorific value, fast flame
propagation speed, high diffusion coefficient, and wide combustion
range. Indeed, hydrogen can easily achieve lean combustion, reduce
NO
x
emissions and improve thermal efficiency [ 83 ]. Ammonia has a low
adiabatic flame temperature and small heat transfer loss, which are of
considerable benefit to the power and economy of an ICE. In particu-
larly, a low flame temperature is beneficial for reducing thermal NO
x
generation. However, the final NO
x
emission level must be balanced
considering the specific fuel characteristics. Additionally, as the LHV of
liquid ammonia is extremely large, full application of the
heat-absorption characteristics of ammonia vaporization can help to
improve ICE combustion efficiency [ 84 , 85 ]. Dual-fuel combustion mode
is quite feasible when using hydrogen- and ammonia-based ICEs owing
to the high spontaneous combustion temperature and low combustion
Fig. 5. Main creation and conversion process of energy source [ 67 ].
Table 1
Physical and chemical properties and thermal properties of clean alternative fuels[ 155 – 166 ]
Properties Diesel Gasoline NG DME methanol Ethanol n-Butanol ammonia hydrogen
Chemical formula C
10
-C
22
C
4
-C
12
CH4 CH
3
OCH
3
CH
3
OH C
2
H
5
OH C
4
H
9
OH NH
3
H
2
Molar mass(g/mol) 122 – 324 58 – 170 16 46 32 46 74 17 2
H/C ratio 2.1 – 2.2 1.7-1.9 4 3 4 3 2.5 – –
Oxygen content (%w) 0 0 0 34.8 50 34.8 21.6 0 0
Density @ 20
◦
C (g/cm3) 0.82-0.86 0.72-0.78 0.72 0.666 0.796 0.798 0.810 0.718 0.0013
Dynamic viscosity (mPa ⋅ s) – 0.37-0.44 0.01 8.75 0.6 1.5 3.6 0.01 0.009
Boiling point (
◦
C) – 20 – 210  162  85.9 65 78 118  33.5  253
Latent heat of vaporization (MJ/kg) 45 41 – 44 50 28.8 19.7 26.8 33.2 18.8 120
Auto-ignition temperature (
◦
C) 205 257 540 238 385 363 343 660 572
Flammability limits (%) 0.6 – 7.5 1.4 – 7.6 5 – 15 3.4 – 18.6 7.3 – 36 4.3 – 19 1.4 – 11.2 15 – 28 4 – 75
Laminar flame speed(m/s) 0.86 0.37-0.43 0.38 0.51 0.56 0.39 0.48 0.07 1.85
Adiabatic flame temperature 2300 2346 2222 2250 2216 2310 2388 1800 2377
RON – 90 – 98 107 55 – 60 109 109 98 110 > 130
T. Li et al. Journal of the Energy Institute 119 (2025) 102006 
5

<!-- PDF_PAGE: 6 -->

speeds of these fuels.
High-activity fuels suitable for dual-fuel combustion include diesel,
biodiesel, and DME, whereas suitable low-activity fuels include hydro-
carbons, alcohols, and zero-carbon fuels. Hydrocarbon fuels primarily
include gasoline (or the gasoline reference fuel isooctane) and natural
gas (or methane); alcohol fuels primarily include methanol, ethanol, n-
butanol, and other low-carbon alcohols; and zero-carbon fuels primarily
include ammonia and hydrogen. The remainder of this review describes
diesel – gasoline, diesel – natural gas, diesel – alcohol, diesel – hydrogen,
and diesel – ammonia DFDI combustion accordingly.
2. Diesel – gasoline DFDI combustion
Gasoline has a low boiling point, high octane number, suitable
volatility, and ready ignition and is widely used in spark-ignition en-
gines accordingly. However, owing to gasoline knock limitations, its
compression ratio is relatively low and the associated fuel economy is
poor [ 86 ]. Therefore, an increasing number of researchers have begun
using gasoline in compression-ignition combustion engines. The com-
bustion mode of gasoline ignited by a high-cetane-number fuel has been
extensively studied. By the beginning of the 21st century, the diesel-
– gasoline dual-fuel direct injection (DGDFDI) combustion engine had
received most of the research attention.
Wissink et al. [ 87 ] first proposed the DGDFDI engine and compared
DGDFDI and RCCI combustion using a single-cylinder direct-injection
diesel engine. The results indicated that DGDFDI combustion perfor-
mance was superior to that of airway-injected gasoline combustion and
the cycle combustion instability was significantly reduced. Furthermore,
DGDFDI combustion exhibited reduced noise and improved efficiency
compared to PPCI combustion [ 57 ]. DGDFDI combustion was shown to
combine the efficiency benefits of RCCI with the engine load benefits of
PPCI, while reducing the need for EGR and the occurrence of combus-
tion instability [ 88 ]. Furthermore, the NO
x
emissions produced by
DGDFDI combustion were lower and the CO and HC emission levels
were close to those realized using RCCI combustion.
Subsequently, Lv et al. [ 61 , 89 – 91 ] proposed an intelligent charge
compression ignition (ICCI) combustion engine using dual direct injec-
tion (DI2) of diesel and gasoline to fully exploit the advantages of
DGDFDI combustion, as shown in Fig. 6 . They reported that under the
optimal gasoline ratio, the ICCI-based multi-injection strategy improved
the thermal efficiency and emissions of combustion. They also compared
the performance of ICCI combustion with that of other combustion
modes, including RCCI, G85 DI2, and G85 and G70 single direct injec-
tion, under similar operating conditions. The ICCI combustion mode
performed best with an improvement in thermal efficiency of approxi-
mately 2 % compared to the RCCI or dual direct-injection combustion
modes. Furthermore, the NO
x
emissions of ICCI combustion were much
closer to zero than those of the direct injection modes.
Qian et al. [ 92 ] found that under low-load conditions, DGDFDI
combustion can be expanded to an indicated mean effective pressure
(IMEP) of 2 bar by reducing the proportion of gasoline, as shown in
Fig. 7 . Furthermore, after reducing the intake pressure and increasing
the intake temperature, the indicated thermal efficiency (ITE) reached
approximately 46 %, representing a significant improvement in engine
efficiency under low-load conditions. They also reported that the octane
number had a quantifiable impact on DGDFDI combustion and emission
characteristics Subsequently, they investigated the effects of #75, #80,
#85, and #95 research octane number (RON) gasoline on DGDFDI
combustion, reporting that the reactivity of the mixture increased as the
gasoline RON decreased, leading to earlier combustion. This also caused
the peak heat release rate and cylinder pressure to advance as the RON
decreased. As shown in Fig. 8 , #85 gasoline was determined to achieve
ultra-low NO
x
and PM emissions as well as an excellent ITE (close to 50
%) when adjusting the injection timings of the diesel and gasoline in
DGDFDI combustion.
The aforementioned literatures extensively studied diesel – gasoline
combustion under medium and low engine loads. However, the com-
bustion and emission characteristics of diesel and gasoline DFDI under
high engine loads are poorly understood. Zhu et al. [ 93 ] conducted a
comprehensive study on DGDFDI combustion in heavy-duty engines
under high loads, reporting that DGDFDI still exhibited a thermal effi-
ciency comparable to that of RCCI. They also reported that DGDFDI
Fig. 6. Schematic diagrams of two direct injectors setup and ICCI injection strategies [ 61 ].
T. Li et al. Journal of the Energy Institute 119 (2025) 102006 
6

<!-- PDF_PAGE: 7 -->

provided an approach for the control of the combustion rate and the
diesel fraction played a leading role in controlling the combustion phase,
whereas the gasoline fraction played a larger role in controlling the
combustion duration. Furthermore, the start of gasoline injection ( SOI
g
)
and the start of diesel injection ( SOI
d
) had more significant effects on
DFDI performance as the DI gasoline energy fraction ( E
g
) and DI diesel
energy fraction ( E
d
) increased, respectively. To this end, Shirvani et al.
[ 94 ] used artificial neural networks to predict the optimal injection
scheme for DGDFDI engines and thereby obtain the optimal parameter
settings. As shown in Fig. 9 , the optimal ranges to reduce NO
x
, soot, and
indicated specific fuel consumption were 4 % < E
d
< 8 %, 23 % < E
g
<
25 %,  110
◦
after top dead center (aTDC) < SOI
d
<  70
◦
aTDC,  5.5
◦
aTDC < SOI
g
<  2
◦
aTDC, and gasoline injection pressure ≃ 900 bar.
In summary, mixed diesel – gasoline fuels can fully utilizing the ad-
vantages associated with the physical and chemical properties of each
fuel to reduce NO
x
and PM emissions while achieving efficient and clean
combustion. Notably, the thermal efficiency of a DGDFDI engine can
reach 50 % when using an 85 % gasoline, 15 % diesel mix. Furthermore,
the combined combustion of gasoline and diesel can extend the fuel
Fig. 7. Extending ICCI ITE to low loads by modulating engine control strategies [ 92 ].
Fig. 8. ITE of ICCI mode under IMEP of 4 bar fueled with low-octane gasoline/
diesel [ 92 ].
T. Li et al. Journal of the Energy Institute 119 (2025) 102006 
7

<!-- PDF_PAGE: 8 -->

combustion delay, shorten the combustion duration, increase the
amount of premixed combustion, and reduce soot and NO
x
emissions
under steady state conditions. Finally, both CO and HC emissions of the
DGDFDI engine gradually decrease during the process of transient load
increase. Clearly, engine combustion can be improved by burning a
gasoline – diesel blend using direct injection.
3. Diesel – natural gas DFDI combustion
The primary component of natural gas is methane, which is the
simplest hydrocarbon fuel because it contains no C-C bonds. Natural gas
(NG) is used as a vehicle fuel worldwide owing to its mature production
process and complete infrastructure [ 95 ]. However, the high sponta-
neous ignition temperature of NG and the difficulty of
compression-ignition combustion in the cylinder limit its efficient and
clean use as an engine fuel [ 96 – 98 ]. Therefore, researchers have adapted
the operating modes of engines powered by diesel and other active fuels
to achieve stable and efficient combustion in cylinders when combined
with NG. Currently, diesel – NG dual-fuel engines typically adopt one of
two injection methods: RCCI and DFDI. When using RCCI, premixed NG
formed by port injection is used as a low-reactivity fuel while
direct-injected diesel is used as a high-activity fuel. The combustion and
emission characteristics of diesel – NG RCCI engines have been studied in
detail [ 97 , 99 – 102 ], indicating high fuel efficiency and low emissions.
However, RCCI diesel – NG engines also exhibit disadvantages including
high CO and HC emissions [ 75 ]. Because NG itself can be compressed in
the inlet injection mode, gas expansion occurs during the injection
process, reducing the engine charge coefficient and resulting in an
approximately 15 % reduction in engine power compared to pure gas-
oline engines. Besides, NG contains trace amounts of sulfide, which can
lead to the wear and corrosion of cylinder walls, valves and valve seats.
To address these problems, researchers have proposed the diesel – NG
dual-fuel direct injection (DNGDFDI) engine.
The idea of directly injecting diesel and NG was first proposed by
professor Hill of the University of British Columbia over 30 years ago
[ 104 ]. Westport subsequently modified several heavy-duty diesel trucks
to run on both diesel and NG using a single injector for both fuels [ 104 ].
Koseki et al. [ 105 ] introduced the DNGDFDI concept and identified the
effect of NG – air mixture formation on thermal efficiency and exhaust
emissions through comparison with a diesel – NG RCCI engine. They re-
ported that the DGDFDI engine exhibited a higher thermal efficiency
and power with lower NO
x
and soot emissions. However, little research
has been conducted on DNGDFDI engines using engine benches; most
studies have focused on the numerical simulation of DNGDFDI engines
instead. In the 2010s, Zoldak [ 106 ] investigated the potential of
DNGDFDI combustion for improving efficiency and reduce emissions
compared to fumigated dual-fuel combustion by conducting a
three-dimensional computational fluid dynamics analysis in KIVA 3V
version 2. The results indicated that the engine load limit for dual-fuel
operation could be extended with a slight penalty in the indicated fuel
efficiency. However, because of the large number of injection parame-
ters, the characteristics of DNGDFDI combustion are highly dependent
on the specific injection strategy applied.
Fig. 9. Solution approach for optimizing injection strategy of a DDFS engine using two direct injectors [ 94 ].
Fig. 10. Diesel/NG dual-fuel combustion strategies [ 111 ].
T. Li et al. Journal of the Energy Institute 119 (2025) 102006 
8

<!-- PDF_PAGE: 9 -->

Critically, these studies were all based on numerical simulations and
lacked corresponding experimental support. The University of British
Columbia and Westport investigated the influence of the injection
strategy on a DNGDFDI engine using an engine bench test system for the
first time by injecting diesel for a short time before TDC and NG for a
short time after TDC. Appropriate adjustment of the diesel injection time
was shown to significantly improve fuel efficiency and emissions output
[ 107 ]. Furthermore, they also found that increasing the fuel injection
pressure could effectively reduce PM and CO emissions under high en-
gine loads [ 108 ].
However, all of these DNGDFDI methods used low-pressure in-
jections. Few studies have been conducted on the characteristics and
emissions of NG combustion under high injection pressures. Li et al.
[ 109 , 110 ] studied the effects of the injection parameters on the com-
bustion characteristics, emissions, economy, and noise of a
high-pressure DNGDFDI engine. Their experimental results showed that
increasing the NG injection advance angle, increasing the injection
pressure, shortening the injection interval between the two fuels, and
decreasing the diesel injection pulse width were conducive to advancing
the combustion phase and improving efficiency. Furthermore, they
reported that the primary measures for reducing NO
x
emissions included
delaying NG injection, reducing the injection pressure, extending the
injection interval between the two fuels, and increasing the diesel in-
jection pulse width. The primary measures for controlling UHCs emis-
sions included reducing the NG injection advance angle, increasing the
injection pressure, and increasing the diesel injection pulse width.
Notably, providing a smaller NG injection advance angle with a lower
injection pressure, shortening the injection interval between the two
fuels, and shortening the diesel injection pulse width effectively
controlled the CO and soot emissions. The combustion noise produced
by the high-pressure DNGDFDI engine was primarily generated by the
combustion of the NG. Therefore, combustion noise can be reduced by
delaying the timing of NG injection, reducing the injection pressure,
extending the injection interval between the two fuels, and increasing
the diesel injection pulse width.
Neely et al. [ 111 ] conducted a comparative study on Pilot-DF, RCCI,
HPDI, DI2, and different diesel combustion modes using an HPDI die-
sel – NG dual-fuel engine platform and a three-dimensional numerical
simulation to verify that DI2 was the best combustion mode, as shown in
Figs. 10 and 11 . The results indicated that using a diffusion-controlled
combustion strategy increased the thermal efficiency of the HPDI en-
gine by more than 2 % and reduced methane emissions by 75 %
compared to an HPDI engine using the same combustion mode.
Furthermore, soot emissions were the same as those of the HPDI engine
when using a partially premixed combustion strategy, though NO
x
emissions increased slightly. However, considering that soot emissions
were lower, NO
x
emissions could be better controlled by employing
EGR, which slightly decreased the combustion efficiency of DI2 at a
small engine load. Liu et al. [ 112 ] studied and obtained an optimal in-
jection strategy for a DNGDFDI engine using CFD simulations showing
that both the diesel and NG injection timing were optimal at  15.2
◦
CA
(aTDC) and  6.0
◦
CA (aTDC).
This previous research indicated that DNGDFDI combustion can
eliminate the knocking phenomenon observed in premixed NG engines
and overcome their low charging efficiency. Indeed, this combustion
mode allows for a higher compression ratio and engine thermal effi-
ciency. Furthermore, the DNGDFDI engine exhibits excellent flexibility
in fuel injection control using common injection strategies such as pilot-
DF, RCCI, HPDI, HCDI, and DI2, among which DI2 is considered one of
the most promising because of its outstanding power and economy.
Finally, the emissions of CO, UHC, NO
x
, soot, and other pollutants can be
effectively reduced by adjusting the diesel and NG injection interval and
pulse width.
Fig. 11. Combustion characteristic of Pilot-DF, RCCI, HPDI, DI2 [ 111 ].
Fig. 12. The change of rate of pressure rise rate for different combustion modes
and engine loads [ 121 ].
T. Li et al. Journal of the Energy Institute 119 (2025) 102006 
9

<!-- PDF_PAGE: 10 -->

4. Diesel – alcohol DFDI combustion
Alcohol-based fuels have clear advantages over gasoline and NG
[ 113 , 114 ]. Firstly, alcohol-based fuels are in liquid form at room tem-
perature and pressure, enabling easy storage and transportation. Sec-
ondly, they are a form of renewable energy that can be obtained from a
wide range of sources, such as biomass. Thirdly, alcohol-based fuels,
particularly methanol and ethanol, have low carbon contents. Alcohol
fuels also contain a great deal of oxygen, which is beneficial for com-
bustion and reduces soot. Fourthly, alcohol-based fuels have a larger
latent heat of vaporization, which is conducive to extending the ignition
delay period and reducing the incidence of local overconcentrated areas
in the cylinder. Besides, the heat absorption of alcohol fuel vaporization
lowers the initial temperature in the cylinder, which is conducive for
reducing the combustion temperature and thereby reducing NO
x
gen-
eration. Finally, alcohol fuels have higher octane ratings (methanol
RON114, ethanol RON108, n-butanol RON96) [ 115 ], which is condu-
cive to the expansion of dual-fuel combustion to large engine loads. In
the remainder of this section, methanol, a representative alcohol-based
fuel, is considered to discuss the performance of diesel – alcohol DFDI
engines [ 116 ].
Yao et al. [ 117 , 118 ] first proposed a diesel – methanol compound
combustion (DMCC) engine that adopted a pure diesel mode under
starting and idling conditions and inlet methanol injection with
in-cylinder direct injection of diesel after the engine was warmed, in
which the methanol premix was ignited using the diesel. In contrast to
RCCI combustion, which relies solely on fuel activity to control the
ignition and combustion processes. DMCC combustion uses highly active
diesel fuel to ignite low-activity methanol, providing superior control
and flexibility. Therefore, the DMCC engine can be expanded to small
and large loads alike to realize efficient combustion and ultra-low
emissions by controlling the methanol substitution rate and fuel injec-
tion strategy. Furthermore, Fang et al. [ 119 ] and Yin et al. [ 120 ] studied
the combustion and emissions characteristics of diesel – methanol
dual-fuel dual-direct-injection (DMDFDI) engines, reporting that they
exhibited notable advantages in terms of combustion characteristics and
combustion rate control. Indeed, the combustion duration provided by
DMDFDI was shorter than that provided by DMCC, and the combustion
stage of the former was more advanced. Additionally, the maximum soot
emitted by the DMDFDI engine at full load was 66 % smaller than that
emitted by a conventional combustion engine, and the NO
x
emissions
were approximately 60 – 70 % smaller across the entire load range.
Fig. 13. The change of CO, uTHC, NOx and soot emissions for different combustion modes and engine loads [ 121 ].
T. Li et al. Journal of the Energy Institute 119 (2025) 102006 
10

<!-- PDF_PAGE: 11 -->

However, CO and HC emissions of the DMDFDI engine were signifi-
cantly higher, indicating that the mixture of fuel and air in this engine
must be improved. Altun et al. [ 121 ] compared DMDFDI and RCCI en-
gines, as shown in Figs. 12 and 13 , reporting that the former exhibited a
higher brake thermal efficiency (BTE) with 63 % and 22 % reductions in
unburned HC and CO emissions, respectively. They also found that the
lower injection pressure employed in DFDI resulted in slightly higher
NO
x
and soot emissions from DMDFDI combustion than from RCCI
combustion.
Clearly, the fuel injection strategy must be adjusted to improve the
degree of fuel – air mixing in the DMDFDI engine and reduce the resulting
NO
x
and soot emissions. Long et al. [ 122 ] accordingly studied the
characteristics of high pressure DMDFDI combustion in a constant vol-
ume combustion chamber (CVCC). They found that the methanol in
some areas of the cylinder did not burn completely, resulting in
increased UHC emissions. As shown in Figs. 14 and 15 , under
low-pressure conditions, the inhibitory effect of methanol on diesel
self-ignition was weakened owing to poor methanol – diesel mixing. As
the fuel injection pressure increased, the ignition delay first decreased,
then increased, and the flame floating length consistently increased. In
addition, the flame area and spatially integrated natural luminosity
(SINL) of DMDFDI combustion were smaller than those of direct injec-
tion combustion, and the SINL for DMDFDI decreased faster after
reaching its maximum value. This implies that the soot oxidized faster
and more completely during DMDFDI combustion. Long et al. [ 123 ]
subsequently mixed methanol with water in different proportions to
further investigate the spray and characteristics of diesel – aqueous
methanol DFDI combustion. The results indicated that the water content
of the methanol and the interval between diesel and methanol injection
were two most critical parameters affecting the ignition and combustion
processes. Under diesel pilot injection, the collision time and position of
the spray plume can be changed by adjusting the injection interval to
realize appropriate intersection of the two spray plumes, which
promotes the mixing of the diesel and methanol sprays and is conducive
to the ignition and combustion of the latter. The longer the injection
interval, the weaker the ignition inhibition effect of the methanol on the
diesel, the shorter the ignition delay, the smaller the flame lift-off length
(FLOL), and the higher the SINL of the flame, indicating greater soot
generation. Furthermore, the higher the water content of the methanol
fuel, the greater the heat absorption during water evaporation, resulting
in a longer ignition delay, larger FLOL, and lower SINL.
Chen et al. [ 63 , 124 ] used visualization technology to conduct a
detailed study of the spray mixing and combustion process of DMDFDI in
a CVCC with the diesel injector placed at 90
◦
to the methanol injector.
They improved the fuel mixture stratification and combustion flame
characteristics by applying high injection pressures ( > 60 MPa) and
delaying the diesel injection time. As shown in Figs. 16 and 17 , the
collision and interference of the diesel spray plume with the methanol
spray plume effectively promoted diesel – methanol, methanol – air, and
diesel – air mixing. Additionally, under high-injection pressure condi-
tions, the strength of impacts between the diesel and methanol
increased, resulting in a larger spray area. When the collision times and
locations of the methanol and diesel spray plumes were changed by
adjusting the diesel injection time, the combination of high pressure and
appropriate injection timing effectively improved the formation of the
diesel – methanol – air mixture, increasing the spray area by up to 62.5 %
after diesel – methanol impact. However, as shown in Figs. 18 and 19 , the
flame shape and light intensity changed with the applied injection
pressure ( P
inj
) and interval ( Δ t ), with higher pressures shortening the
combustion ignition delay, increasing the FLOL, and reducing soot
production, and longer injection intervals resulting in longer ignition
delay, larger FLOL, and lower soot production. Chen et al. concluded
that the combustion and emission characteristics of DMDFDI can be
effectively improved by proper regulation of Δ t and P
inj
, and the pro-
duction of soot can be reduced by up to 33.33 %.
Yin et al. [ 120 ] compared the operating range and combustion
Fig. 14. Flame images for DMDFDI and CDI [ 122 ].
T. Li et al. Journal of the Energy Institute 119 (2025) 102006 
11

<!-- PDF_PAGE: 12 -->

characteristics of a DMDFDI engine using different methanol injection
timings. As shown in Figs. 20 and 21 , the operating range of the DMDFDI
engine was limited by incomplete and roaring combustion. The engine
exhibited the widest operating range when the methanol injection time
was  300
◦
CA aTDC and its narrowest operating range when the
methanol injection time was  60
◦
CA aTDC. However, at  60
◦
CA
aTDC, the methanol energy substitution ratio (MESR) reached its
maximum of 62.7 %, reflecting the best fuel economy, and the maximum
ITE reached 43.4 %. In addition, when methanol was injected directly in
the compression stroke at  180
◦
CA aTDC, HC and CO emissions were
the lowest among the considered methanol injection times. The lowest
NO
x
emissions are observed at  60
◦
CA aTDC. Yin et al. [ 125 ] also
investigated the effects of different loads and MESRs on the combustion
in and emissions from a DMDFDI engine. As shown in Fig. 22 , the sta-
bility of DMDFDI combustion was significantly reduced when the engine
was under a low load, leading to a deterioration in the fuel economy.
When the engine was under medium to high loads, its combustion sta-
bility and fuel economy were significantly improved by adjusting the
load and MESR. When the engine load was 79.5 %, the MESR was 52.4 %
and the ITE reached a maximum of 43.4 %. Furthermore, NO
x
emissions
decreased significantly with increasing MESR, whereas CO and HC
emissions increased significantly. However, CO and HC emissions
decreased significantly as the engine load increased. The combination of
a high MESR and high engine load resulted in lower HC emissions than
observed for conventional pure diesel combustion.
Li et al. [ 167 ] reported that the arrangement of injectors and the
number, diameter, and angle of nozzles affected the combustion and
emission characteristics of DMDFDI engines: the larger the number of
nozzles, the smaller the nozzle-hole diameter, which was conducive to
fuel atomization and spontaneous combustion. These results can be
applied to shorten the ignition delay period of the DMDFDI engine,
increase the flame area and methanol diffusion combustion rate within,
and improve its heat release rate and combustion efficiency. Further-
more, more nozzles resulted in lower soot, UHCs, CO, and CH2 emis-
sions. However, an increase in combustion temperature led to higher
NO
x
emissions. Combining these findings, eight nozzles were deter-
mined to be the most suitable for DMDFDI injectors. Finally, they pro-
posed that the diesel – methanol injection angle could be adjusted to
more accurately target the injected methanol at the diesel flame to
achieve a higher combustion speed and heat release, which is beneficial
for improving fuel economy and lowering emissions. In addition, Feng
et al. [ 127 ] found that increasing the nozzle length effectively improved
the combustion stability of a DMDFDI engine and inhibited the gener-
ation of pollutants such as NO
x
. Li et al. [ 128 , 129 ] used a fast
non-dominated sorting genetic algorithm (NSGA-II) to co-optimize the
injection parameters and layouts for two fuels. The resulting optimal
parameters of the DMDFDI engine under low-load operation are sum-
marized in Table 2 , in which the methanol fraction, injection timing,
injection pressure, injection angle, nozzle diameter, and injector loca-
tion can be observed to have exerted significant effects on engine per-
formance. Notably, the methanol-related parameters had more
significant effects than the diesel-related parameters.
In summary, the use of DMDFDI combustion can avoid incomplete
combustion of the fuel under a small engine load and avoid rough
combustion under heavy engine load. Furthermore, a DMDFDI engine
can precisely control the quantity of methanol injected into each cyl-
inder such that there is no uneven combustion, as observed when
injecting different quantities of methanol into each cylinder using the
airway injection method. This prevents fuel deposition at the injector
inlet owing to poor atomization, which has been identified when
employing the airway injection method and avoids the corresponding
decrease in the aeration efficiency. In addition, the DMDFDI engine can
Fig. 15. Flame images of CDI and DMDFDI with different injection pressures [ 122 ].
T. Li et al. Journal of the Energy Institute 119 (2025) 102006 
12

<!-- PDF_PAGE: 13 -->

also realize the flexible regulation of injection strategies for diesel and
methanol. In these strategies, methanol is injected into the engine when
the diesel ignites, the methanol is still in the process of diffusion,
evaporation, and atomization to form a mixture, thereby achieving a
diffusion combustion mode. Notably, the diesel ignition preparation
process during the combustion delay period is unaffected by the airflow
and temperature drop in the cylinder owing to methanol injection,
evaporation, and atomization, allowing the diesel to be successfully
ignited. Meanwhile, the larger latent heat of methanol vaporization and
the oxygen-carrying ability of methanol reduces the temperature in the
combustion area and inhibits soot generation, which is conducive to
reducing NO
x
and carbon soot emissions. Therefore, a high substitution
rate of methanol fuel corresponds to lower pollutant emissions.
5. Diesel – hydrogen DFDI combustion
Hydrogen is an excellent fuel for ICEs because of its high calorific
value, fast flame propagation speed, high diffusion coefficient, and wide
combustion range. Indeed, the use of hydrogen as an ICE fuel offers
several specific advantages: 1) a wide combustion concentration range
[ 130 , 131 ]; 2) a rapid flame propagation speed with highly efficient
combustion as well as a high spontaneous combustion temperature and
octane number, which can achieve a high compression ratio to improve
thermal efficiency [ 132 ]; 3) low ignition energy and suitable starting
performance [ 133 ]; 4) a rapid diffusion rate in air, which facilitates the
formation of a homogeneous mixture to achieve lean combustion,
reduce harmful emissions (particularly NO
x
), and improve thermal ef-
ficiency [ 134 , 135 ].
Boretti et al. [ 136 ] proposed a diesel – hydrogen dual-fuel direct in-
jection (DHDFDI) engine and employed the KAVA model to evaluate its
performance, reporting that the conversion efficiency and power output
of the DHDFDI engine were higher than those of a conventional diesel
engine, and that its thermal efficiency was approximately 40 %. Liu et al.
[ 26 ] applied the DHDFDI model to CI engines to verify the accuracy of
the numerical simulation of DHDFDI engine performance, reporting that
DHDFDI could effectively improve the preignition and detonation owing
to hydrogen inlet injection to achieve higher thermal efficiency and
lower pollutant emissions than possible in conventional diesel engines.
As shown in Fig. 23 , an optimal thermal efficiency of 47 % and low
emissions were simultaneously achieved at a 50 % hydrogen substitu-
tion rate and 40
◦
CA before top dead center (bTDC) hydrogen injection.
Furthermore, the noise created by combustion was reduced by 6 dB, the
engine output NO
x
emissions were maintained below 11 g/kWh, and
while the UHC and CO emissions were constant, soot emissions were
reduced by a factor of 10. In addition, Rorimpandey et al. [ 137 ] deter-
mined that a higher hydrogen energy fraction can effectively improve
the thermal efficiency of a DHDFDI engine but will inevitably increase
NO
x
emissions; when the hydrogen energy fraction reached 90 %, the
thermal efficiency was 57.2 %. By adjusting the injection timing, they
concluded that a bTDC hydrogen injection time of 40
◦
CA provided the
optimal results with suitable in-cylinder mixture reactivity and con-
centration stratifications to achieve a 85.9 % reduction in CO
2
emissions
and 13.3 % improvement in IMEP/efficiency. Finally, Liu et al. [ 138 ]
changed the hydrogen injector to employ a porous structure in a
split-injection strategy that increased the hydrogen replacement rate by
20 – 70 % compared to a single-injection strategy. The stratification of
the mixture was effectively improved using this setup by adjusting the
timing of the first and second hydrogen injections, thereby improving
the effective thermal efficiency of the DHDFDI engine and significantly
reducing its CO
2
and NO
x
emissions.
Most of the above DHDFDI studies focused on the entire engine or
evaluated a test bench engine, and the research objectives were
Fig. 16. Spray morphology of diesel/methanol DI2 at different injection pressure and injection interval [ 124 ].
T. Li et al. Journal of the Energy Institute 119 (2025) 102006 
13

<!-- PDF_PAGE: 14 -->

primarily concerned with macro-scale combustion and emissions char-
acteristics. However, many factors influencing engine operation, such as
the thermal environment, operating state, and structure of the cylinder,
are coupled, making the role of each factor difficult to determine
accurately. Therefore, the influences of single factors such as the initial
temperature, pressure, oxygen concentration, fuel equivalence ratio,
and fuel injection strategy on the ignition and combustion processes
have been studied individually. Rorimpandey et al. [ 139 ] used a CVCC
to investigate the effects of injector configuration, injection timing, and
ambient temperature on DHDFDI spray and combustion characteristics.
As shown in Figs. 24 and 25 , spontaneous diesel combustion occurred in
the head of a DHDFDI engine using diesel pilot injection, and diesel
combustion become more complete as the interval for the hydrogen
injected following ignition increased. As the injection interval between
the two fuels increases, diesel combustion quickly ignited the hydrogen
after contact to realize a higher flame propagation speed, longer flame
penetration distance, and a larger flame area. In contrast, DHDFDI using
hydrogen pilot injection exhibited a longer ignition delay than DHDFDI
using diesel pilot injection. Under hydrogen pilot injection, the ignition
delay was extended, the hydrogen spray penetration distance increased,
and the mixing effect with air improved as the injection interval
increased. The hydrogen was ignited soon after the spontaneous com-
bustion of the diesel, allowing the flame to quickly develop into a
hydrogen spray head that improved the combustion effect.
Rorimpandey et al. [ 137 ] also investigated the effects of the energy
share and ambient oxygen concentration on DHDFDI combustion using a
CVCC. As shown in Figs. 26 and 27 , they found that the ignition of diesel
was unaffected by the interaction with the hydrogen jet, and the diesel
always caught fire at the edge of the hydrogen spray, where it ignited the
hydrogen. Furthermore, they reported that a decrease in oxygen con-
centration extended the interaction time between hydrogen and diesel
too long, prolonging the ignition delay. Note that environmental con-
ditions can also affect the FLOL: at 21 vol% O
2
, the flame was observed
to attach to the nozzle, but became increasingly lifted at lower ambient
oxygen concentrations; at 15 vol% O
2
, the flame lifted approximately 5
mm from the hydrogen nozzle, and this distance increased to 7 mm for
cases with short diesel injection duration. Finally, an increase in the
hydrogen substitution rate and oxygen concentration effectively
reduced the quantity of carbon smoke generated during DHDFDI
combustion.
In summary, the wide combustion limit and rapid flame propagation
speed associated with hydrogen facilitate its use as a combustion
accelerator in diesel engines to improve combustion and reduce emis-
sion concentrations. Compared to a conventional diesel engine, a
DHDFDI engine can increase the peak combustion pressure, heat release
rate, and indicated power while reducing the engine combustion noise,
fuel consumption rate, average combustion temperature in the cylinder,
and UHC, CO, PM, and soot emissions. It is worth noting that DHDFDI
Fig. 17. Integrated effects of injection pressure and injection interval on the maximum SPA [ 124 ].
T. Li et al. Journal of the Energy Institute 119 (2025) 102006 
14

<!-- PDF_PAGE: 15 -->

effectively increases the hydrogen substitution rate to 70 %. However,
DHDFDI engines have the disadvantage of significantly increasing NO
x
emissions under high loads. Future studies should accordingly focus on
preventing knock combustion in and reducing NO
x
emissions from
DHDFDI engines.
6. Diesel – ammonia DFDI combustion
Ammonia fuel, which consists of nitrogen and hydrogen, produces
only nitrogen and water when fully burned and does not emit green-
house gases such as CO
2
, helping to reduce the greenhouse effect and
achieve carbon neutrality goals. Therefore, the application of ammonia
fuel in ICE has great potential. However, there are still many problems
with ammonia engines. For example, (1) high ignition energy: ammonia
has a high spontaneous combustion temperature and a large minimum
ignition energy, which makes it difficult to ignite in the engine [ 140 ].
(2) Slow combustion speed: the laminar flame speed of ammonia is low,
and the combustion process is slow, which affects the power output and
efficiency of the engine [ 141 ]. (3) NO
X
emissions: NO
x
is easily produced
during ammonia combustion, especially N
2
O, which has a high global
warming potential [ 140 ]. (4) Unburned ammonia emissions: Due to
inadequate combustion, ammonia engines are prone to produce un-
burned ammonia in the start-up stage or under low load conditions
[ 142 ]. (5) Cold start difficulty: Ammonia engines require higher tem-
peratures during cold starts to promote the decomposition and com-
bustion of ammonia, often requiring additional heating devices [ 140 ].
(6) Complex fuel supply system: In order to improve combustion per-
formance, it is usually necessary to mix with hydrogen and other ac-
celerants, which increases the complexity and cost of the fuel supply
system. International efforts to improve ammonia CI engines have pur-
sued four methods: providing a high compression ratio, designing an
ignition system dedicated to ammonia fuel, using ammonia with a
certain proportion of mixed fuel to provide strong combustion
performance, and using high cetane-number fuel pilot injection to ignite
ammonia [ 143 ]. Gray et al. [ 144 ] first evaluated the use of diesel as an
ignition source for ammonia engines in 1966. They found that the full
combustion of diesel – ammonia fuel was achieved at a compression ratio
of 15.2:1, which is much lower than that of pure ammonia. In 1977, Bro
et al. [ 145 ] adopted a dual-fuel strategy employing airway injection of
ammonia and in-cylinder direct injection of diesel to achieve ammonia
combustion in a compression ICE. However, the combustion phase of the
engine was excessively delayed, the combustion rate was slow, and the
efficiency of the entire machine was low owing to the limitations of
manufacturing and control levels. Reiter et al. [ 146 , 147 ] studied the
influence of the ammonia ratio on the injection of ammonia into the
airway and the corresponding compression-ignition combustion mode
of in-cylinder direct-injected diesel. They reported that increasing the
proportion of ammonia effectively reduced carbon smoke emissions, but
increased NO
x
emissions when the ammonia energy replacement ratio
exceeded 60 %. Similarly, Nadimi et al. [ 148 ] found that 84.2 % of input
energy can be provided by ammonia meanwhile indicated ITE is
increased by increasing the diesel substitution.
In summary, ammonia fuel can be applied in CI combustion engines
using port injection of ammonia and direct injection of diesel. However,
this approach is associated with several disadvantages such as a low
ammonia substitution rate and narrow operating conditions. In addition,
the port injection of ammonia causes part of the ammonia fuel to enter
the boundary layer, where it does not readily participate in-cylinder
combustion, resulting in higher-than-anticipated ammonia emissions.
Furthermore, high NO
x
emissions are generated in the combustion core
area owing to thin burning at high temperatures. Therefore, diesel-
– ammonia dual-fuel direct injection (DADFDI) combustion has been
proposed in recent years to address these problems.
Indeed, the need to develop a new ammonia fuel supply and injection
system for direct injection into the combustion cylinder is urgent. Sasaki
et al. [ 149 ] proposed a direct liquid injector that can simultaneously
Fig. 18. Combustion morphologies produced by diesel – methanol DI2 at different injection pressures and intervals [ 124 ].
T. Li et al. Journal of the Energy Institute 119 (2025) 102006 
15

<!-- PDF_PAGE: 16 -->

Fig. 19. Change in the sum of KL factors during diesel – methanol DI2 combustion at different injection pressures and intervals [ 124 ].
Fig. 20. Experimental operating range and ITE contours for methanol injection timings of  300,  180, and  60
◦
CA aTDC [ 120 ].
T. Li et al. Journal of the Energy Institute 119 (2025) 102006 
16

<!-- PDF_PAGE: 17 -->

inject diesel and ammonia using the airway injection of gaseous
ammonia, direct injection of gaseous ammonia into the cylinder, and
direct injection of liquid ammonia into the cylinder. Gaseous ammonia
injection provided advantageously simple operation. However, this in-
jection strategy had few adjustable parameters and reduced the inflation
efficiency of the ICE. Although the direct injection of gaseous ammonia
into the cylinder overcame some of the shortcomings associated with
airway injection, the thermal efficiency of the ICE was also reduced
under this method. Finally, the direct injection of liquid ammonia into
the cylinder was governed by parameters (duration, phase, and fre-
quency of injection) that can be adjusted according to the engine load,
making it the most efficient injection method. Notably, the high heat
absorption of liquid ammonia vaporization can be used to improve the
combustion efficiency of an ICE.
In the early stages of DADFDI research, liquid ammonia was difficult
to directly apply using in-cylinder direct injection technology; therefore,
researchers primarily studied the combustion and emissions character-
istics of DADFDI engines using numerical simulations. Boretti [ 103 , 104 ]
simulated the full load range of an DADFDI engine, demonstrating that
the efficient combustion of ammonia can be achieved by increasing the
ammonia injection pressure and that DADFDI is superior to the airway
injection of ammonia with in-cylinder direct injection of diesel. Lamas
[ 150 ] explored hydrogen – ammonia – diesel compression-ignition com-
bustion using numerical simulations and effectively inhibited NO
x
emissions by reasonably controlling the timing of direct ammonia in-
jection. The results of numerical analyses conducted by Li et al. [ 126 ]
indicated that the direct injection of liquid ammonia can significantly
reduce the emissions of unburned ammonia, NO
x
, and other greenhouse
gases. In addition, the high-pressure direct injection of liquid ammonia
can accommodate an ammonia replacement rate of up to 97 %.
Additional research has been conducted since to verify the accuracy
of these numerical simulations. Long et al. [ 21 , 22 ] used a DADFDI in-
jection strategy in a low-speed two-stroke engine to study engine per-
formance and emission characteristics under different ammonia
injection quantities, ammonia injection timings, and diesel injection
timings. The results indicated that soot emissions decreased significantly
with increasing injected ammonia, whereas NO
x
emissions increased
significantly. In addition, they reported that diesel injection timing
realized more accurate control of the combustion phase than ammonia
injection timing and was more conducive to improving the thermal ef-
ficiency of the engine and shortening the combustion duration. Notably,
delaying the timing of diesel injection or extending the total combustion
Fig. 21. Effects of methanol injection timings on regular gaseous emissions [ 120 ].
Fig. 22. Left: experimental operating range and ITE contours. Right: effects of ESR on emissions at different engine loads [ 125 ].
T. Li et al. Journal of the Energy Institute 119 (2025) 102006 
17

<!-- PDF_PAGE: 18 -->

time can regulate NOx emissions but may worsen the ITE in some cases.
An injection timing of  8
◦
CA aTDC was reported to represent the best
choice for realizing the best ITE and emission performance of diesel-
– liquid phase ammonia balanced engines (as shown in Figs. 28 and 29 ).
Bj ø rgen et al. [ 151 ] concluded that the optimal injection strategy was to
temporarily close the ammonia and diesel oil injectors and avoid the
injection of ammonia after diesel combustion. In addition, they sug-
gested that the optimal injection strategy largely depends on the inter-
action between the ammonia and diesel spray.
To study the effects of the single injection strategy and environ-
mental conditions on the DADFDI spray, combustion, and emission
characteristics under steady state conditions, Chen et al. [ 152 ] observed
the interaction between the diesel and ammonia spray in a CVCC with
the diesel and liquid ammonia injectors arranged at 90
◦
to one another.
As shown in Figs. 30 and 31 , they found that the impact of the two spray
plumes after cross-injection promoted the diesel – air, liquid ammonia-
– air and diesel – liquid ammonia mixing. Moreover, an increase in the
diesel injection delay weakened the impact intensity of the two spray
plumes, reducing the momentum loss owing to spray collision. This not
only allowed the spray to more easily mix with air, accelerating the
spray diffusion rate and increasing the spray area, but also resulted in an
extremely short ignition delay with a longer diesel injection delay as
well as a higher FLOL. Thus, a more intense combustion process that
emitted less soot. Therefore, the interaction between the diesel and
ammonia sprays can be promoted by reasonably adjusting the injection
timing of the two fuels to improve the combustion and emissions char-
acteristics of DADFDI. Similarly, Zhang et al. [ 153 ] studied the inter-
action between two sprays with different ammonia injection quantities
Table 2
Optimal operating parameters of a DMDFDI engine at low loads [ 129 ].
Parameters Optimal
Strategy
Effect Benefit
Methanol
fraction
Around 78 % Split two
combustion stages
Compromise between
combustion efficiency and
heat transfer losses
SOI Advanced
SOI
d
+ SOI
m
near TDC
Control
combustion
phasing and fuel/
air mixing
Reduce the local
equivalence ratio, retard
combustion phasing, and
improve NO
x
and fuel
efficiency
Spray angle
(SA)
SA
d
= 60 – 80
+ SA
m
=
70 – 80
Determine spray
target
Enhance fuel/air mixing
and reduce heat transfer
losses
Injector
position
Central-
mounted
methanol
injector
Dominate fuel
distributions and
interactions
Improve combustion
efficiency and accelerate
combustion rate
Injection
pressure
High P
inj d
+
High P
inj m
Determine
injection duration
and fuel/air mixing
Increase fuel/air mixture
homogeneity
Nozzle
number
(No
z)
No
z d
= 5 +
No
z m
= 6
Affect injection
duration and fuel/
air mixing
Shorten combustion
duration and lengthen
injection penetration
Rotation
angle
(Ro
t
)
Rot
d
= 53 +
Rot
m
= 38
Affect two fuels
interaction
Improve combustion
efficiency
Fig. 23. Combustion and emission characteristics of a DHDFDI engine according to hydrogen energy fraction and hydrogen injection timing [ 26 ].
T. Li et al. Journal of the Energy Institute 119 (2025) 102006 
18

<!-- PDF_PAGE: 19 -->

and observed the impact on the combustion flame in a CVCC. They re-
ported that the liquid ammonia spray volume produced by high-pressure
injection could be divided into gas entrainment and ejection zones. The
effective ignition of ammonia in the diesel spray occurred in the gas
entrainment zone, except for the liquid ammonia volume under evap-
oration, indicating reliable ammonia ignition and subsequent diffusion
combustion with a 74.4 % ammonia energy replacement. As sufficient
ammonia must be mixed with an appropriate quantity of lead diesel in
diffusion combustion mode, the ammonia injection rate must be
increased or the diesel flame suspension time extended. In summary, the
nozzle and spray arrangements of the two fuels and the reasonable
choice of injection strategy are extremely critical factors influencing the
spray, combustion, and emissions characteristics of the DADFDI engine.
Shin [ 55 ] reached the same conclusion as Li [ 126 ] through a nu-
merical analysis and obtained the optimal strategy for DADFDI. When
97 % of diesel was substituted with ammonia, the timing of ammonia
injection had the most significant effect on the combustion phase and
thermal efficiency and the maximum thermal efficiency occurred be-
tween combustion stages 2 and 10 CAD. Though the change in CO
2
emissions with injection time was insignificant, the emissions of nitrous
oxide and greenhouse gasses increased with the delay in ammonia in-
jection. Indeed, greenhouse gas emissions from DADFDI combustion
were at least 50.1 % and up to 97.0 % smaller than those from con-
ventional diesel combustion. Comprehensively considering the com-
bustion and emissions characteristics of the DADFDI engine, when the
ammonia injection rate was set to  7 CAD and the diesel injection rate
was set between  15 and  10 CAD, the IMEP, greenhouse gas emis-
sions, and NO emissions produced by DADFDI combustion were all
improved compared to those of conventional diesel combustion. Under
these conditions, the efficiency was increased by approximately 8 %, NO
emissions were reduced by 12.2 – 13.5 %, and greenhouse gas emissions
were reduced by approximately 91 %, while the emission range of un-
burned ammonia remained within 36.2 – 58.4 ppm. These results indi-
cate the advantages of using ammonia as a fuel substitute for diesel in
the development of heavy-duty engines.
In summary, the combination of diesel and ammonia is particularly
suitable for application in DFDI engines because of the considerable
difference between the reactivities of the two fuels, particularly when
directly injecting of ammonia into the cylinder. Indeed, DADFDI can
effectively regulate the distribution of ammonia in the cylinder and
optimize the reactivity distribution of the mixture, thereby improving
efficiency and inhibiting emissions while achieving efficient engine
combustion over a wide load range. Furthermore, the emissions of NO
and unburned ammonia can be effectively reduced by adjusting the
diesel and ammonia injection strategies. The use of high ammonia in-
jection pressure diffusion combustion technology to expand the oper-
ating load of the engine can effectively increase the potential diesel
replacement with ammonia as high as 97 % according to the proportion
of fuel energy. However, the most significant problem faced by DADFDI
engines is their high NO
x
emissions. Future research should evaluate the
combination of DADFDI with exhaust gas recirculation to control NO
x
emissions accordingly.
Fig. 24. DHDFDI combustion flame development process under different injection timings (hydrogen first injection) [ 139 ].
T. Li et al. Journal of the Energy Institute 119 (2025) 102006 
19

<!-- PDF_PAGE: 20 -->

Fig. 25. DHDFDI combustion flame development process under different injection timings (diesel first injection) [ 139 ].
T. Li et al. Journal of the Energy Institute 119 (2025) 102006 
20

<!-- PDF_PAGE: 21 -->

7. Conclusion and further recommendations
This paper critically reviewed the application of dual-fuel in-cylinder
direct injection technology in diesel engines. The use of DFDI was shown
to provide a technical solution to realize the efficient and clean com-
bustion of low-activity renewable fuels (such as alcohol, ammonia, and
hydrogen) in diesel engines. Indeed, the use of DFDI can:
1. flexibly adjust the injection time, volume, and interval of each fuel
and regulate the formation of mixtures, reactivity stratification, and
concentration stratification;
2. effectively improve upon the power and thermal efficiency of con-
ventional diesel engines while flexibly regulating the combustion
process; as a result, the combustion optimization potential is large;
3. address shortcomings associated with the limited low-activity fuel
replacement rate, low combustion stability, low combustion effi-
ciency at medium engine loads, and low flexible combustion at high
engine loads owing to the injection of low-activity fuel at the inlet
and high-activity fuel in the cylinder to broaden the operating con-
ditions of dual-fuel engines;
4. reduce the emissions of CO, UHC, NO
x
, and other pollutants by
conventional diesel engines through the use of diesel to ignite a low-
carbon and zero-carbon fuel, thereby achieving the efficient and
clean combustion of renewable fuels.
At present, the typical low-activity fuels used in DFDI diesel engines
include gasoline, NG, methanol, hydrogen, and ammonia. Each of these
fuels has its own advantages. Diesel – gasoline DFDI exhibits the highest
thermal efficiency of approximately 50 % at a gasoline ratio of 85 %.
Diesel – NG DFDI eliminates knocking. Diesel – methanol DFDI utilizes the
high latent heat of methanol gasification to effectively reduce the in-
cylinder temperature, inhibit diesel combustion, and significantly
reduce NO
x
and soot emissions. Diesel – hydrogen DFDI employs the low
ignition energy, wide flammability limit, and high flame speed of
hydrogen to provide a greater thin burning limit and improve the
thermal efficiency of the diesel engine while reducing the fuel con-
sumption rate. Notably, because hydrogen is a zero-carbon fuel, it pro-
motes the homogenization of the air – fuel mixture to effectively mitigate
CO, CO
2
, HC, PM, and soot emissions. Finally, diesel – ammonia DFDI
accommodates a maximum diesel replacement rate with ammonia of 97
% and significantly reduces the emissions of greenhouse gases such as
CO, UHC, NO
x
, and nitrous oxide while considerably broadening the
operating conditions of dual-fuel engines.
The highly active fuel used in the DFDI diesel engines in this review
was diesel. Owing to the high carbon content of diesel, its combustion
flame temperature is high, which leads to a sharp increase in CO, CO
2
,
NO
x
, and PM emissions. A vital future development trend is to find a
diesel fuel with a high cetane number to serve as a high-activity fuel in
DFDI combustion. Notably, the cetane numbers of carbon-neutral fuels
Fig. 26. DHDFDI combustion flame development process images depicting energy share under ambient 21 vol% O
2
[ 137 ].
T. Li et al. Journal of the Energy Institute 119 (2025) 102006 
21

<!-- PDF_PAGE: 22 -->

such as DME and polymethoxy-dimethyl ether are higher than that of
diesel, and their reactivities are better. Most importantly, low boiling
point fuels such as methanol, DME, ammonia, and hydrogen have flash
boiling properties. Flash boiling has been regarded as a promising
method to improve the atomization of fuel sprays and to reduce emis-
sions without a high-pressure injection system. Therefore, they have
excellent prospects for application in DFDI diesel engines. In future
research, the spray, combustion, and emission characteristics of DFDI
combustion of these carbon-neutral fuels with low-carbon or zero-
carbon fuels should be studied in detail.
In addition, current research results indicate that DFDI combustion is
superior to conventional diesel combustion in all respects. However,
previous studies have employed engine bench experiments in which the
operating conditions were stable. This type of setup cannot represent the
operating characteristics of an actual DFDI engine under the instanta-
neous conditions present in a working vehicle. Therefore, actual vehicle
road tests should be conducted using DFDI diesel engines to evaluate
their operating performance and provide basic data, optimization
schemes, and a technical path for combustion control in high-efficiency
and low-emission DFDI engines under different road conditions.
Finally, DFDI-based engines have the potential for widespread
application in the automobile market. A DFDI engine suitable for
different vehicle models should be designed accordingly by adjusting
the shape of the combustion chamber, varying the placement of the two
injectors, designing special dual-fuel injectors, further optimization of
injection strategies, and studies on the combined effects of flash boiling
and EGR to effectively broaden the proportion of DFDI engines in the
automobile market.
CRediT authorship contribution statement
Tao Li: Writing – original draft, Writing – review & editing. Pengyun
Zhao: Writing – review & editing, Writing – original draft, Data cura-
tion. Haibin He: Visualization, Funding acquisition. Chunguang
Wang: Funding acquisition, Writing – review & editing. Haitao Zhang:
Writing – original draft, Methodology. Zhanming Chen: Writing – re-
view & editing, Writing – original draft, Investigation. Hao Chen:
Validation, Methodology.
Declaration of competing interest
The authors declare that they have no known competing financial
interests or personal relationships that could have appeared to influence
the work reported in this paper.
Fig. 27. DHDFDI combustion flame development process images depicting energy share under ambient 15 vol% O
2
[ 137 ].
T. Li et al. Journal of the Energy Institute 119 (2025) 102006 
22

<!-- PDF_PAGE: 23 -->

Fig. 28. Combustion duration and ITE according to ammonia and diesel injection timing [ 21 , 22 ]
T. Li et al. Journal of the Energy Institute 119 (2025) 102006 
23

<!-- PDF_PAGE: 24 -->

Fig. 29. CO, UHC, soot, NO
x
emissions according to diesel injection timing [ 21 , 22 ]
T. Li et al. Journal of the Energy Institute 119 (2025) 102006 
24

<!-- PDF_PAGE: 25 -->

Fig. 30. Spray morphologies of cross-injected diesel – ammonia according to injection interval [ 152 ].
Fig. 31. Combustion processes of diesel – ammonia cross-injection according to Δ t [ 152 ].
T. Li et al. Journal of the Energy Institute 119 (2025) 102006 
25

<!-- PDF_PAGE: 26 -->

Acknowledgments
This project was funded by China Postdoctoral Science Foundation
(2023M741840), China; Shaanxi Science and technology Nova (2024
ZC-KJXX-026), China; Research Funds for the Interdisciplinary Projects,
CHU(300104240913), China; and Fundamental Research Funds for the
Central Universities, CHU (300102383201), China. Our deepest grati-
tude goes to the editors and reviewers for their careful work and
thoughtful suggestions, which have helped us to improve this paper
substantially.
References
[1] G. Kalghatgi, Is it really the end of internal combustion engines and petroleum in
transport? Appl. Energy 225 (2018) 965 – 974 .
[2] Ministry of Ecology and. Environment of the People ’ s Republic of China, China
Mobile Source Environmental Management Annual Report, 2023 .
[3] G. Grolleau, C. Weber, The effect of inflation on CO2 emissions: an analysis over
the period 1970 – 2020, Ecol. Econ. 217 (2024) 108029 .
[4] H. Song, C. Wang, K. Sun, H. Geng, L. Zuo, Material efficiency strategies across
the industrial chain to secure indium availability for global carbon neutrality,
Resour. Pol. 85 (2023) 103895 .
[5] X. Gu, M. Wang, J. Wu, An empirical study on the green effects of new energy
vehicle promotion in the context of global carbon neutrality, Chin J Populat
Resour Environ 20 (4) (2022) 332 – 340 .
[6] Z. Lee, T. Kim, S. Park, S. Park, Review on spray, combustion, and emission
characteristics of recent developed direct-injection spark ignition (DISI) engine
system with multi-hole type injector, Fuel 259 (2020) 116209 .
[7] M. Abdullah, M. Zoynal Abedin, Recent development of combined heat transfer
performance for engine systems: a comprehensive review, Res Surf Interf 15
(2024) 100212 .
[8] X. Chen, Y. Shi, Y. Cai, J. Xie, Y. Yang, D. Hou, Y. Fan, Effect of non-thermal
plasma injection flow rate on diesel particulate filter regeneration at room
temperature, Carbon Lett 34 (3) (2024) 1075 – 1089 .
[9] J. Galindo, H. Climent, J. de la Morena, D. Gonz ´alez-Domínguez, S. Guilain,
Assessment of air management strategies to improve the transient response of
advanced gasoline engines operating under high EGR conditions, Energy 262
(2023) 125586 .
[10] J.C. Puoza, T. Zhang, F. Uba, Y. Kuusana, A. Ibrahim, Optimization of post-
treatment honing parameters of laser textured engine cylinder bore and engine
performance, J Eng Res 11 (4) (2023) 478 – 487 .
[11] B. Tesfa, R. Mishra, F. Gu, N. Powles, Prediction models for density and viscosity
of biodiesel and their effects on fuel supply system in CI engines, Renew. Energy
35 (12) (2010) 2752 – 2760 .
[12] V. Ayhan, Investigation of electronic controlled direct water injection for
performance and emissions of a diesel engine running on sunflower oil methyl
ester, Fuel 275 (2020) 117992 .
[13] Y. Qian, S. Sun, D. Ju, X. Shan, X. Lu, Review of the state-of-the-art of biogas
combustion mechanisms and applications in internal combustion engines, Renew.
Sustain. Energy Rev. 69 (2017) 50 – 58 .
[14] A. Thawko, L. Tartakovsky, The mechanism of particle formation in non-
premixed hydrogen combustion in a direct-injection internal combustion engine,
Fuel 327 (2022) 125187 .
[15] J. Xu, Q. Lan, L. Fan, Y. Wu, Y. Wei, Y. Gu, Research on injection performance of
the double-lift electronically controlled injector for marine diesel engine, Fuel
337 (2023) 126878 .
[16] G. Ergen, Comprehensive analysis of the effects of alternative fuels on diesel
engine performance combustion and exhaust emissions: role of biodiesel, diethyl
ether, and EGR, Therm. Sci. Eng. Prog. 47 (2024) 102307 .
[17] Y. Hua, Research progress of higher alcohols as alternative fuels for compression
ignition engines, Fuel 357 (2024) 129749 .
[18] F. Zhou, J. Yu, C. Wu, J. Fu, J. Liu, X. Duan, The application prospect and
challenge of the alternative methanol fuel in the internal combustion engine, Sci.
Total Environ. 913 (2024) 169708 .
[19] T. Wang, Y. Zhang, J. Zhang, Z. Peng, G. Shu, Comparisons of system benefits and
thermo-economics for exhaust energy recovery applied on a heavy-duty diesel
engine and a light-duty vehicle gasoline engine, Energy Convers. Manag. 84
(2014) 97 – 107 .
[20] A.G.M.B. Mustayen, M.G. Rasul, X. Wang, M. Negnevitsky, J.M. Hamilton,
Remote areas and islands power generation: a review on diesel engine
performance and emission improvement techniques, Energy Convers. Manag. 260
(2022) 115614 .
[21] Z. Zhang, W. Long, P. Dong, H. Tian, J. Tian, B. Li, Y. Wang, Performance
characteristics of a two-stroke low speed engine applying ammonia/diesel dual
direct injection strategy, Fuel 332 (2023) 126086 .
[22] Z. Zhang, C. Zhang, P. Cai, Z. Jing, J. Wen, Y. Li, H. Wang, L. An, J. Zhang, The
potential of coal-to-liquid as an alternative fuel for diesel engines: a review,
J. Energy Inst. 109 (2023) 101306 .
[23] C. Zhai, E. Liu, G. Zhang, W. Xing, F. Chang, Y. Jin, H. Luo, K. Nishida, Y. Ogata,
Similarity and normalization study of fuel spray and combustion under ultra-high
injection pressure and micro-hole diameter conditions – spray characteristics,
Energy 288 (2024) 129684 .
[24] L. Geng, Y. Zhao, S. Shan, B. Kang, N. Gao, H. Chen, Study on spray and
combustion characteristics of Fischer-Tropsch diesel/biodiesel blends in a
constant volume chamber, J. Energy Inst. 111 (2023) 101422 .
[25] C. Zhang, K. Yang, G. Li, J. Dai, T.H. Lee, Spray evaporation characteristics of
isopropanol-butanol-ethanol (IBE)/diesel blends in a constant volume chamber,
Fuel 330 (2022) 125659 .
[26] X. Liu, A. Srna, H.L. Yip, S. Kook, Q.N. Chan, E.R. Hawkes, Performance and
emissions of hydrogen-diesel dual direct injection (H2DDI) in a single-cylinder
compression-ignition engine, Int. J. Hydrogen Energy 46 (1) (2021) 1302 – 1314 .
[27] F. Chang, H. Luo, C. Zhai, Y. Jin, P. Xiong, J. Wang, B. Song, J. Zhang, K. Nishida,
Experimental investigation of fuel adhesion from wall-impinging spray with
various injection mass ratios, Exp. Therm. Fluid Sci. 163 (2025) 111403 .
[28] M. Fathi, O. Jahanian, M. Shahbakhti, Modeling and controller design
architecture for cycle-by-cycle combustion control of homogeneous charge
compression ignition (HCCI) engines – a comprehensive review, Energy Convers.
Manag. 139 (2017) 1 – 19 .
[29] R.K. Maurya, M.R. Saxena, Characterization of ringing intensity in a hydrogen-
fueled HCCI engine, Int. J. Hydrogen Energy 43 (19) (2018) 9423 – 9437 .
[30] T.W.B. Riyadi, M. Spraggon, S.G. Herawan, M. Idris, P.A. Paristiawan, N.R. Putra,
M.F. R, R. Silambarasan, I. Veza, Biodiesel for HCCI engine: prospects and
challenges of sustainability biodiesel for energy transition, Res. Eng. 17 (2023)
100916 .
[31] S. Bhurat, S. Pandey, V. Chintala, M. Jaiswal, C. Kurien, Effect of novel fuel
vaporiser technology on engine characteristics of partially premixed charge
compression ignition (PCCI) engine with toroidal combustion chamber, Fuel 315
(2022) 123197 .
[32] M. Nibin, J.B. Raj, V.E. Geo, Experimental studies to improve the performance,
emission and combustion characteristics of wheat germ oil fuelled CI engine using
bioethanol injection in PCCI mode, Fuel 285 (2021) 119196 .
[33] A.P. Singh, V. Kumar, A.K. Agarwal, Evaluation of comparative engine
combustion, performance and emission characteristics of low temperature
combustion (PCCI and RCCI) modes, Appl. Energy 278 (2020) 115644 .
[34] M. Elkelawy, E.A. El Shenawy, S.A. Mohamed, M.M. Elarabi, H. Alm-Eldin
Bastawissi, Impacts of EGR on RCCI engines management: a comprehensive
review, Energy Convers. Manag. X 14 (2022) 100216 .
[35] J. Li, W. Yang, D. Zhou, Review on the management of RCCI engines, Renew.
Sustain. Energy Rev. 69 (2017) 65 – 79 .
[36] R.D. Reitz, G. Duraisamy, Review of high efficiency and clean reactivity
controlled compression ignition (RCCI) combustion in internal combustion
engines, Prog. Energy Combust. Sci. 46 (2015) 12 – 71 .
[37] Y. Bai, Y. Wang, L. Hao, Experimental study on the effects of injection timing and
n-butanol energy ratio on combustion and emissions of n-butanol/diesel DFDI
engine, Fuel 324 (2022) 124654 .
[38] W. Yang, Y. Wang, Y. Bai, L. Hao, X. Liu, Experimental study of the bioethanol
substitution rate and the diesel injection strategies on combustion and emission
characteristics of dual-fuel-direct-injection (DFDI) engine, J. Energy Inst. 106
(2023) 101153 .
[39] L.M. Olesky, G.A. Lavoie, D.N. Assanis, M.S. Wooldridge, J.B. Martz, The effects
of diluent composition on the rates of HCCI and spark assisted compression
ignition combustion, Appl. Energy 124 (2014) 186 – 198 .
[40] J. Hunicz, M. Mikulski, M.S. Geca, A. Rybak, An applicable approach to mitigate
pressure rise rate in an HCCI engine with negative valve overlap, Appl. Energy
257 (2020) 114018 .
[41] X. Duan, M.-C. Lai, M. Jansons, G. Guo, J. Liu, A review of controlling strategies
of the ignition timing and combustion phase in homogeneous charge compression
ignition (HCCI) engine, Fuel 285 (2021) 119142 .
[42] H. Bendu, S. Murugan, Homogeneous charge compression ignition (HCCI)
combustion: mixture preparation and control strategies in diesel engines, Renew.
Sustain. Energy Rev. 38 (2014) 732 – 746 .
[43] A.A. Hairuddin, T. Yusaf, A.P. Wandel, A review of hydrogen and natural gas
addition in diesel HCCI engines, Renew. Sustain. Energy Rev. 32 (2014) 739 – 761 .
[44] P. Kumar, A. Rehman, Bio-diesel in homogeneous charge compression ignition
(HCCI) combustion, Renew. Sustain. Energy Rev. 56 (2016) 536 – 550 .
[45] P. Drews, T. Albin, F.J. He ß eler, N. Peters, D. Abel, Fuel-efficient model-based
optimal MIMO control for PCCI engines, IFAC Proc. Vol. 44 (1) (2011)
12998 – 13003 .
[46] S.K. Pandey, S.R. Sarma Akella, R.V. Ravikrishna, Novel fuel injection strategies
for PCCI operation of a heavy-duty turbocharged diesel engine, Appl. Therm. Eng.
143 (2018) 883 – 898 .
[47] J. Lee, S. Chu, J. Cha, H. Choi, K. Min, Effect of the diesel injection strategy on the
combustion and emissions of propane/diesel dual fuel premixed charge
compression ignition engines, Energy 93 (2015) 1041 – 1052 .
[48] E. Shim, H. Park, C. Bae, Comparisons of advanced combustion technologies
(HCCI, PCCI, and dual-fuel PCCI) on engine performance and emission
characteristics in a heavy-duty diesel engine, Fuel 262 (2020) 116436 .
[49] R.M. Hanson, S.L. Kokjohn, D.A. Splitter, R.D. Reitz, An Experimental
Investigation of Fuel Reactivity Controlled PCCI Combustion in a Heavy-Duty
Engine, vol. 3, 2010, pp. 700 – 716 .
[50] S.L. Kokjohn, R.M. Hanson, D.A. Splitter, R.D. Reitz, Fuel reactivity controlled
compression ignition (RCCI): a pathway to controlled high-efficiency clean
combustion 12 (3) (2011) 209 – 226 .
[51] A. Paykani, A. Garcia, M. Shahbakhti, P. Rahnama, R.D. Reitz, Reactivity
controlled compression ignition engine: pathways towards commercial viability,
Appl. Energy 282 (2021) 116174 .
T. Li et al. Journal of the Energy Institute 119 (2025) 102006 
26

<!-- PDF_PAGE: 27 -->

[52] S. Molina, A. García, J.M. Pastor, E. Belarte, I.J.A.E. Balloul, Operating Range
Extension of RCCI Combustion Concept from Low to Full Load in a Heavy-Duty
Engine, vol. 143, 2015, pp. 211 – 227 .
[53] D.A. Splitter, M.L. Wissink, D.A. DelVescovo, R. Reitz, RCCI Engine Operation
towards 60% Thermal Efficiency, 2013 .
[54] L. Ning, Q. Duan, H. Kou, K. Zeng, Parametric study on effects of methanol
injection timing and methanol substitution percentage on combustion and
emissions of methanol/diesel dual-fuel direct injection engine at full load, Fuel
279 (2020) 118424 .
[55] J. Shin, S. Park, Numerical analysis and optimization of combustion and
emissions in an ammonia-diesel dual-fuel engine using an ammonia direct
injection strategy, Energy 289 (2024) 130014 .
[56] M. Taghi Zarrinkolah, V. Hosseini, Methane slip reduction of conventional dual-
fuel natural gas diesel engine using direct fuel injection management and
alternative combustion modes, Fuel 331 (2023) 125775 .
[57] M. Wissink, R. Reitz, Direct dual fuel stratification, a path to combine the benefits
of RCCI and PPC, SAE Int. J. Eng. 8 (2015) 878 – 889 .
[58] J. Lim, R. Reitz, High Load (21 Bar IMEP) Dual Fuel RCCI Combustion Using Dual
Direct Injection, 2013 .
[59] Y. Li, M. Jia, L. Xu, X.-S. Bai, Multiple-objective optimization of methanol/diesel
dual-fuel engine at low loads: a comparison of reactivity controlled compression
ignition (RCCI) and direct dual fuel stratification (DDFS) strategies, Fuel 262
(2020) 116673 .
[60] W. Long, B. Li, J. Cao, X. Meng, J. Tian, J. Cui, H. Tian, Effects of dual-direct
injection parameters on performance of fuel Jet Controlled Compression Ignition
mode on a high-speed light duty engine, Fuel 235 (2019) 658 – 669 .
[61] Z. Li, G. Huang, Y. Zhang, W. Zhao, J. Li, Z. He, Y. Qian, X. Lu, Dual fuel
intelligent charge compression ignition (ICCI) combustion: efficient and clean
combustion technology for compression ignition engines, Fuel 279 (2020)
118565 .
[62] B. Wu, Z. Zi, X. Zou, J. Li, S. Jin, Effect of diesel and gasoline blending fuel
coordinate with in-cylinder charge conditions on efficient and clean combustion
based heavy-duty diesel engine, Fuel 297 (2021) 120790 .
[63] Z. Chen, P. Zhao, T. Wang, H. He, H. Chen, P. Zhang, Y. Li, L. Geng, D. Qi,
Visualization study the cross spray and combustion characteristics of diesel and
methanol in a constant volume combustion chamber at cold and flare flash
boiling regions, Energy 301 (2024) 131654 .
[64] P. Dong, K. Liu, L. Zhang, Z. Zhang, W. Long, H. Tian, Study on the synergistic
control of nitrogenous emissions and greenhouse gas of ammonia/diesel dual
direct injection two-stroke engine, Energy 307 (2024) 132657 .
[65] X. Yin, Y. Yan, X. Ren, L. Yu, H. Duan, E. Hu, K. Zeng, Effects of methanol energy
substitution ratio and diesel injection timing on a methanol/diesel dual-fuel
direct injection engine, Fuel 382 (2025) 133773 .
[66] S. Nithya, A. Chinnathambi, S. Ali Alharbi, B. Minofar, Carbon neutrality with
ammonia: an analysis of its feasibility as a fuel for diesel engines fuelled with
spirulina microalgae and oxygenated additives, Fuel 361 (2024) 130628 .
[67] Q. Pham, S. Park, A.K. Agarwal, S. Park, Review of dual-fuel combustion in the
compression-ignition engine: spray, combustion, and emission, Energy 250
(2022) 123778 .
[68] H. Luo, L. Liu, K. Nishida, W. Zhou, Development and utilization on green energy
in marine powertrain: challenges and opportunities, Green Energy Resour. 2 (2)
(2024) 100076 .
[69] D. Goyal, T. Goyal, S.K. Mahla, G. Goga, A. Dhir, D. Balasubramanian, A.
T. Hoang, M. Wae-Hayee, J.S.F. Josephin, A. Sonthalia, E.G. Varuvel,
K. Brindhadevi, Application of Taguchi design in optimization of performance
and emissions characteristics of n-butanol/diesel/biogas under dual fuel mode,
Fuel 338 (2023) 127246 .
[70] M. Gurusamy, C. Ponnusamy, The influence of hydrogen induction on the
characteristics of a CI engine fueled with blend of camphor oil and diesel with
diethyl ether additive, Int. J. Hydrogen Energy 48 (62) (2023) 24054 – 24073 .
[71] S. Kumar, G. Goga, Emission characteristics & performance analysis of a diesel
engine fuelled with various alternative fuels – a review, Mater. Today: Proc.
(2023) .
[72] S.K. Mahla, S.M. Safieddin Ardebili, H. Sharma, A. Dhir, G. Goga, H. Solmaz,
Determination and utilization of optimal diesel/n-butanol/biogas derivation for
small utility dual fuel diesel engine, Fuel 289 (2021) 119913 .
[73] P. Soltic, T. Hilfiker, Y. Wright, G. Hardy, B. Fr ¨ohlich, D. Klein, The potential of
dimethyl ether (DME) to meet current and future emissions standards in heavy-
duty compression-ignition engines, Fuel 355 (2024) 129357 .
[74] J. Tian, L. Wang, Y. Xiong, Y. Wang, W. Yin, G. Tian, Z. Wang, Y. Cheng, S. Ji,
Enhancing combustion efficiency and reducing nitrogen oxide emissions from
ammonia combustion: a comprehensive review, Process Saf. Environ. Protect.
183 (2024) 514 – 543 .
[75] S. Wang, S. Qiu, X. Li, P. Zhang, Modeling non-monotonic variation of plume
angle with superheat index of flash boiling spray, Energy 306 (2024) 132515 .
[76] M. Cui, W. Zhang, J. Fu, X. Luo, D.L.S. Hung, M. Xu, X. Li, Impact of flash boiling
spray on soot generation of a rich fuel – air mixture under various ambient
pressures, Combust. Flame 263 (2024) 113388 .
[77] S. Qiu, S. Wang, Y. Zhang, Y. Li, M. Xu, X. Li, Dynamics and mechanisms of spray
plume interference under flash boiling conditions, Energy 314 (2025) 134121 .
[78] Z. Jin, H. Wu, S. Xu, D. Zhou, S. Mi, Y. Qian, X. Lu, A unified spray model for large
eddy simulations under non-flashing and flash boiling conditions: effects of in-
nozzle flow and external thermal breakup in liquid ammonia injection, Int. J.
Multiphas. Flow 184 (2025) 105116 .
[79] H. Wu, S. Mi, Y. Qian, T. Zhang, J. Zhang, C. Pan, L. Shi, X. Lu, Spray and
evaporation characteristics of high-pressure liquid ammonia injection under
flash-boiling and evaporating conditions, Fuel 381 (2025) 133627 .
[80] R. Behçet, A. Yakin, Evaluation of hydrogen-containing NaBH4 and oxygen-
containing alcohols (CH3OH, C2H5OH) as fuel additives in a gasoline engine, Int.
J. Hydrogen Energy 47 (53) (2022) 22316 – 22327 .
[81] D.A.R. Kay, W.G. Wilson, V. Jalan, High temperature thermodynamics and
applications of rare earth compounds containing oxygen and sulphur in fuel gas
desulphurization and SOx and NOx removal, J. Alloys Compd. 193 (1) (1993)
11 – 16 .
[82] R.J. Murray, Methanol and Methanol/Diesel Fuel Modes in Compression Ignition
Engines, Reference Module in Chemistry, Molecular Sciences and Chemical
Engineering, Elsevier, 2024 .
[83] S.H. Hosseini, A. Tsolakis, A. Alagumalai, O. Mahian, S.S. Lam, J. Pan, W. Peng,
M. Tabatabaei, M. Aghbashlo, Use of hydrogen in dual-fuel diesel engines, Prog.
Energy Combust. Sci. 98 (2023) 101100 .
[84] M.-C. Chiong, C.T. Chong, J.-H. Ng, S. Mashruk, W.W.F. Chong, N.A. Samiran, G.
R. Mong, A. Valera-Medina, Advancements of combustion technologies in the
ammonia-fuelled engines, Energy Convers. Manag. 244 (2021) 114460 .
[85] C. Kurien, M. Mittal, Review on the production and utilization of green ammonia
as an alternate fuel in dual-fuel compression ignition engines, Energy Convers.
Manag. 251 (2022) 114990 .
[86] Z. S ¸ ahin, O. Durgun, C. Bayram, Experimental investigation of gasoline
fumigation in a single cylinder direct injection (DI) diesel engine, Energy 33 (8)
(2008) 1298 – 1310 .
[87] M. Wissink, J. Lim, D. Splitter, R. Hanson, R. Reitz, Investigation of injection
strategies to improve high efficiency RCCI combustion with diesel and gasoline
direct injection, in: ASME 2012 Internal Combustion Engine Division Fall
Technical Conference, 2012 .
[88] M. Wissink, R. Reitz, Exploring the role of reactivity gradients in direct dual fuel
stratification, SAE Int. J. Eng. 9 (2016) .
[89] Z. Li, J. Li, G. Huang, Y. Zhang, Z. He, Y. Qian, X. Lu, A methodology for
stratified-charge preparation via low-reactivity fuel multi-injection strategy in
intelligent charge compression ignition (ICCI) mode, Fuel 289 (2021) 119751 .
[90] Z. Li, Y. Zhang, G. Huang, W. Zhao, Z. He, Y. Qian, X. Lu, Control of intake
boundary conditions for enabling clean combustion in variable engine conditions
under intelligent charge compression ignition (ICCI) mode, Appl. Energy 274
(2020) 115297 .
[91] W. Zhao, Y. Zhang, G. Huang, Z. He, Y. Qian, X. Lu, Experimental study of
butanol/biodiesel dual-fuel combustion in intelligent charge compression ignition
(ICCI) mode: a systematic analysis at low load, Fuel 287 (2021) 119523 .
[92] S. Mi, Y. Zhang, H. Wu, W. Zhao, X. Lu, Y. Qian, Effects of research octane
number of gasoline and dual direct injection strategies on combustion and
emission performance of intelligent charge compression ignition (ICCI) mode,
Fuel Process. Technol. 238 (2022) 107508 .
[93] Y. Zhu, Y. Zhang, Z. He, Q. Wang, W. Li, A numerical investigation of gasoline/
diesel direct dual fuel stratification (DDFS) combustion at high loads, Fuel 312
(2022) 122751 .
[94] S. Shirvani, S. Shirvani, A.H. Shamekhi, R. Reitz, F. Salehi, Meeting EURO6
emission regulations by multi-objective optimization of the injection strategy of
two direct injectors in a DDFS engine, Energy 229 (2021) 120737 .
[95] H. Luo, B. Zhou, Y. Liu, Y. Jin, C. Zhai, K. Nishida, J. Ge, Characteristics of
hydrogen enrichment on RNG combustion under various engine speeds in a
retrofitted gas engine, Process Saf. Environ. Protect. 188 (2024) 629 – 642 .
[96] B. Liu, R.E. Hayes, M.D. Checkel, M. Zheng, E. Mirosh, Reversing flow catalytic
converter for a natural gas/diesel dual fuel engine, Chem. Eng. Sci. 56 (8) (2001)
2641 – 2658 .
[97] J. Liu, Y. Liu, Q. Ji, P. Sun, X. Zhang, X. Wang, H. Ma, Effects of split injection
strategy on combustion stability and GHG emissions characteristics of natural
gas/diesel RCCI engine under high load, Energy 266 (2023) 126542 .
[98] X. Sun, H. Liu, X. Duan, H. Guo, Y. Li, J. Qiao, Q. Liu, J. Liu, Effect of hydrogen
enrichment on the flame propagation, emissions formation and energy balance of
the natural gas spark ignition engine, Fuel 307 (2022) 121843 .
[99] Z. Chen, L. Wang, X. Wang, H. Chen, L. Geng, N. Gao, Experimental study on the
effect of water port injection on the combustion and emission characteristics of
diesel/methane dual-fuel engines, Fuel 312 (2022) 122950 .
[100] A.-H. Kakaee, P. Rahnama, A. Paykani, Influence of fuel composition on
combustion and emissions characteristics of natural gas/diesel RCCI engine,
J. Nat. Gas Sci. Eng. 25 (2015) 58 – 65 .
[101] J. Liu, J. Wang, H. Zhao, Optimization of the injection parameters and
combustion chamber geometries of a diesel/natural gas RCCI engine, Energy 164
(2018) 837 – 852 .
[102] L. Yang, S. Ji, W. Niu, A. Zare, J. Hunicz, R.J. Brown, Effect of split injection
strategy of diesel fuel on multi-stage heat release and performance of a RCCI
engine fueled with diesel and natural gas, Fuel 362 (2024) 130930 .
[103] A. Boretti, Novel dual fuel diesel-ammonia combustion system in advanced TDI
engines, Int. J. Hydrogen Energy 42 (10) (2017) 7071 – 7076 .
[104] A. Boretti, Numerical study of the substitutional diesel fuel energy in a dual fuel
diesel-LPG engine with two direct injectors per cylinder, Fuel Process. Technol.
161 (2017) 41 – 51 .
[105] Takahisa Koseki, Yasuhiro Daisho, Akihiro Ikeda, Ryoji Kihara, Takeshi saito,
Performance and exhaust emission characteristics of dual-fuel diesel engine with
a natural gas direct injection system: (Waseda University), JSAE Rev. 18 (2)
(1997) 209 .
T. Li et al. Journal of the Energy Institute 119 (2025) 102006 
27

<!-- PDF_PAGE: 28 -->

[106] P. Zoldak, A. Sobiesiak, D. Wickman, M. Bergin, Combustion Simulation of Dual
Fuel CNG Engine Using Direct Injection of Natural Gas and Diesel, vol. 8, 2015,
pp. 846 – 858 .
[107] G. McTaggart-Cowan, W. Bushe, P. Hill, S. Munshi, A supercharged heavy-duty
diesel single-cylinder research engine for high-pressure direct injection of natural
gas, Int. J. Eng. Res. - Int. J. Engine Res. 4 (2003) 315 – 330 .
[108] G.P. McTaggart-Cowan, H.L. Jones, S.N. Rogak, W.K. Bushe, P.G. Hill, S.
R. Munshi, The effects of high-pressure injection on a compression – ignition,
direct injection of natural gas engine, J. Eng. Gas Turbines Power 129 (2) (2006)
579 – 588 .
[109] M. Li, Q. Zhang, G. Li, S. Shao, Experimental investigation on performance and
heat release analysis of a pilot ignited direct injection natural gas engine, Energy
90 (2015) 1251 – 1260 .
[110] Q. Zhang, M. Li, S. Shao, Combustion process and emissions of a heavy-duty
engine fueled with directly injected natural gas and pilot diesel, Appl. Energy 157
(2015) 217 – 228 .
[111] G.D. Neely, R. Florea, J.T. Miwa, Z. Abidin, Efficiency and Emissions
Characteristics of Partially Premixed Dual-Fuel Combustion by Co-direct Injection
of NG and Diesel Fuel (DI2) - Part 2, 2017 .
[112] J. Liu, H. Zhao, J. Wang, N. Zhang, Optimization of the injection parameters of a
diesel/natural gas dual fuel engine with multi-objective evolutionary algorithms,
Appl. Therm. Eng. 150 (2019) 70 – 79 .
[113] H. Chen, X. Su, J. He, B. Xie, Investigation on combustion and emission
characteristics of a common rail diesel engine fueled with diesel/n-pentanol/
methanol blends, Energy 167 (2019) 297 – 311 .
[114] H. Chen, X. Su, J. Li, X. Zhong, Effects of gasoline and polyoxymethylene dimethyl
ethers blending in diesel on the combustion and emission of a common rail diesel
engine, Energy 171 (2019) 981 – 999 .
[115] E.G. Giakoumis, C.D. Rakopoulos, A.M. Dimaratos, D.C. Rakopoulos, Exhaust
emissions with ethanol or n-butanol diesel fuel blends during transient operation:
a review, Renew. Sustain. Energy Rev. 17 (2013) 170 – 190 .
[116] Z. Chen, J. He, H. Chen, L. Geng, P. Zhang, Comparative study on the combustion
and emissions of dual-fuel common rail engines fueled with diesel/methanol,
diesel/ethanol, and diesel/n-butanol, Fuel 304 (2021) 121360 .
[117] C. Yao, C.S. Cheung, C. Cheng, Y. Wang, Reduction of smoke and NOx from diesel
engines using a diesel/methanol compound combustion system, Energy Fuels 21
(2) (2007) 686 – 691 .
[118] C. Yao, C.S. Cheung, C. Cheng, Y. Wang, T.L. Chan, S.C. Lee, Effect of Diesel/
methanol compound combustion on Diesel engine combustion and emissions,
Energy Convers. Manag. 49 (6) (2008) 1696 – 1704 .
[119] X. Fang, X. Liu, W. Jin, S. Yan, A study on a DI compression ignition engine with
diesel-methanol injection by dual injection systems, Transact. Csice 21 (6) (2003)
411 – 414 .
[120] X. Yin, W. Li, H. Duan, Q. Duan, H. Kou, Y. Wang, B. Yang, K. Zeng,
A comparative study on operating range and combustion characteristics of
methanol/diesel dual direct injection engine with different methanol injection
timings, Fuel 334 (2023) 126646 .
[121] S ¸ . Altun, M. Fırat, Y. Varol, M. Okcu, Comparison of direct and port injection of
methanol in a RCCI engine using diesel and biodiesel as high reactivity fuels,
Process Saf. Environ. Protect. 174 (2023) 681 – 693 .
[122] Y. Wang, H. Wang, X. Meng, J. Tian, Y. Wang, W. Long, S. Li, Combustion
characteristics of high pressure direct-injected methanol ignited by diesel in a
constant volume combustion chamber, Fuel 254 (2019) 115598 .
[123] Q. Wang, F. Wei, P. Dong, G. Xiao, Z. Cui, J. Tian, X. Shi, W. Long, Visualization
study on combustion characteristics of direct-injected hydrous methanol ignited
by diesel in a constant volume combustion chamber, Fuel 335 (2023) 127063 .
[124] Z. Chen, P. Zhao, H. Zhang, H. Chen, H. He, J. Wu, L. Wang, H. Lou, An optical
study on the cross-spray characteristics and combustion flames of automobile
engine fueled with diesel/methanol under various injection timings, Energy 290
(2024) 130286 .
[125] X. Yin, G. Yue, J. Liu, H. Duan, Q. Duan, H. Kou, Y. Wang, B. Yang, K. Zeng,
Investigation into the operating range of a dual-direct injection engine fueled
with methanol and diesel, Energy 267 (2023) 126625 .
[126] T. Li, X. Zhou, N. Wang, X. Wang, R. Chen, S. Li, P. Yi, A comparison between low-
and high-pressure injection dual-fuel modes of diesel-pilot-ignition ammonia
combustion engines, J. Energy Inst. 102 (2022) 362 – 373 .
[127] S. Feng, S. Zhang, H. Zhang, J. Shi, Effect of nozzle geometry on combustion of a
diesel-methanol dual-fuel direct injection engine, Fuel 357 (2024) 129734 .
[128] Y. Li, Y. Cai, M. Jia, Y. Wang, X. Su, L. Li, A full-parameter computational
optimization of both injection parameters and injector layouts for a methanol/
diesel dual-fuel direct injection compression ignition engine, Fuel 369 (2024)
131733 .
[129] Y. Li, H. Li, B. Pang, F. Liu, M. Jia, W. Long, J. Tian, L. Guo, Co-optimization of
injection parameters and injector layouts for a methanol/diesel direct dual-fuel
stratification (DDFS) engine, Energy 284 (2023) 128647 .
[130] D. Tan, Y. Wu, J. Lv, J. Li, X. Ou, Y. Meng, G. Lan, Y. Chen, Z. Zhang, Performance
optimization of a diesel engine fueled with hydrogen/biodiesel with water
addition based on the response surface methodology, Energy 263 (2023) 125869 .
[131] Z. Zhang, J. Lv, G. Xie, S. Wang, Y. Ye, G. Huang, D. Tan, Effect of assisted
hydrogen on combustion and emission characteristics of a diesel engine fueled
with biodiesel, Energy 254 (2022) 124269 .
[132] H. Luo, M. Yu, C. Zhai, Y. An, C. Wang, K. Nishida, Study on fermentation gas
combustion with hydrogen addition under various throttle openings, Green
Energy Resour. 1 (1) (2023) 100003 .
[133] K. Wr ´obel, J. Wr ´obel, W. Tokarz, J. Lach, K. Podsadni, A. Czerwi ´nski, Hydrogen
Internal Combustion Engine Vehicles: A Review, Energies, 2022 .
[134] M. Ihsan Shahid, A. Rao, M. Farhan, Y. Liu, H. Ahmad Salam, T. Chen, F. Ma,
Hydrogen production techniques and use of hydrogen in internal combustion
engine: a comprehensive review, Fuel 378 (2024) 132769 .
[135] J. Lei, J. Niu, G. Tian, G. Xin, X. Yang, C. Shi, Advances in hydrogen as a zero-
carbon fuel for rotary engines: a review, Fuel 381 (2025) 133681 .
[136] A. Boretti, Advantages of the direct injection of both diesel and hydrogen in dual
fuel H2ICE, Int. J. Hydrogen Energy 36 (15) (2011) 9312 – 9317 .
[137] P. Rorimpandey, G. Zhai, S. Kook, E.R. Hawkes, Q.N. Chan, Effects of energy-
share and ambient oxygen concentration on hydrogen-diesel dual-fuel direct-
injection (H2DDI) combustion in compression-ignition conditions, Int. J.
Hydrogen Energy 49 (2024) 1346 – 1361 .
[138] X. Liu, L. Yang, Q.N. Chan, S. Kook, Split injection strategies for a high-pressure
hydrogen direct injection in a small-bore dual-fuel diesel engine, Int. J. Hydrogen
Energy 57 (2024) 904 – 917 .
[139] P. Rorimpandey, H.L. Yip, A. Srna, G. Zhai, A. Wehrfritz, S. Kook, E.R. Hawkes, Q.
N. Chan, Hydrogen-diesel dual-fuel direct-injection (H2DDI) combustion under
compression-ignition engine conditions, Int. J. Hydrogen Energy 48 (2) (2023)
766 – 783 .
[140] D. Dong, F. Wei, W. Long, P. Dong, H. Tian, J. Tian, P. Wang, M. Lu, X. Meng,
Optical investigation of ammonia rich combustion based on methanol jet ignition
by means of an ignition chamber, Fuel 345 (2023) 128202 .
[141] X. Meng, L. Liu, M. Qin, M. Miao, H. Zhao, W. Long, M. Bi, Study on ammonia/
methanol blends with ammonia cracking for low-carbon combustion and NO
reduction, J. Clean. Prod. 450 (2024) 141959 .
[142] P. Dong, S. Chen, D. Dong, F. Wei, M. Lu, P. Wang, W. Long, Future zero carbon
ammonia engine: Fundamental study on the effect of jet ignition system
characterized by gasoline ignition chamber, J. Clean. Prod. 435 (2024) 140546 .
[143] X. Meng, L. Liu, M. Qin, W. Zhu, W. Long, M. Bi, Modeling and chemical kinetic
analysis of methanol and reformed gas (H2/CO2) blending with ammonia under
lean-burn condition, Int. J. Hydrogen Energy 58 (2024) 190 – 199 .
[144] J.T. Gray, E. Dimitroff, N.T. Meckel, R.D. Quillian, Ammonia Fuel - Engine
Compatibility and Combustion, 1966 .
[145] K. Bro, P.S.J.d.e. Pedersen, Alternative diesel engine fuels: an experimental
investigation of methanol, ethanol, methane and ammonia in a D.I, Diesel Eng.
Pilot Inject. (1980) .
[146] A. Reiter, S.-C. Kong, Demonstration of compression-ignition engine combustion
using ammonia in reducing greenhouse gas emissions, Energy Fuels 22 (2008) .
[147] A.J. Reiter, S.-C. Kong, Combustion and emissions characteristics of compression-
ignition engine using dual ammonia-diesel fuel, Fuel 90 (1) (2011) 87 – 97 .
[148] E. Nadimi, G. Przyby ł a, M.T. Lewandowski, W. Adamczyk, Effects of ammonia on
combustion, emissions, and performance of the ammonia/diesel dual-fuel
compression ignition engine, J. Energy Inst. 107 (2023) 101158 .
[149] M. El-Adawy, M.A. Nemitallah, A. Abdelhafez, Towards sustainable hydrogen and
ammonia internal combustion engines: challenges and opportunities, Fuel 364
(2024) 131090 .
[150] M.I. Lamas, C.G. Rodriguez, Numerical model to analyze Nox reduction by
ammonia injection in diesel-hydrogen engines, Int. J. Hydrogen Energy 42 (41)
(2017) 26132 – 26141 .
[151] K.O.P. Bj ø rgen, D.R. Emberson, T. L ø vås, Combustion of liquid ammonia and
diesel in a compression ignition engine operated in high-pressure dual fuel mode,
Fuel 360 (2024) 130269 .
[152] Z. Chen, H. He, J. Wu, L. Wang, H. Lou, P. Zhao, T. Wang, H. Zhang, H. Chen, An
experimental study the cross spray and combustion characteristics diesel and
ammonia in a constant volume combustion chamber, Energy 293 (2024) 130733 .
[153] W. Zhang, Z. Zhang, H. Chen, Z. Ji, Y. Ma, F. Sun, A review on performance,
combustion and emission of diesel and alcohols in a dual fuel engine, J. Energy
Inst. 116 (2024) 101760 .
[154] G.D. Neely, S. Sasaki, Y. Huang, J.A. Leet, D.W. Stewart, New diesel emission
control strategy to meet US tier 2 emissions regulations, SAE Trans. 114 (2005)
512 – 524 .
[155] P.K. Arya, S. Tupkari, S. K, G.D. Thakre, B.M. Shukla, DME blended LPG as a
cooking fuel option for Indian household: a review, Renew. Sustain. Energy Rev.
53 (2016) 1591 – 1601 .
[156] R.L. Bechtold, Alternative Fuels Guidebook : Properties, Storage, Dispensing, and
Vehicle Facility Modifications, 1997 .
[157] X. Duan, X. Chu, R. Wang, Z. Chen, F. Zhou, T.M.M. Abdellatief, The performance
and emissions characteristics of the gasoline spark ignition engine fuelled with
green and renewable methanol and hydrogen, Renew. Energy 240 (2025)
122184 .
[158] Y. Huang, N.C. Surawski, Y. Zhuang, J.L. Zhou, G. Hong, Dual injection: an
effective and efficient technology to use renewable fuels in spark ignition engines,
Renew. Sustain. Energy Rev. 143 (2021) 110921 .
[159] R. Jayabal, Ammonia as a potential green dual fuel in diesel engines: a review,
Process Saf. Environ. Protect. 188 (2024) 1346 – 1354 .
[160] T. Larsson, O. Stenlaas, A. Erlandsson, Future fuels for disi engines: a review on
oxygenated, Liquid Biofuels (2019) .
T. Li et al. Journal of the Energy Institute 119 (2025) 102006 
28

<!-- PDF_PAGE: 29 -->

[161] S.T.P. Purayil, M.O. Hamdan, S.A.B. Al-Omari, M.Y.E. Selim, E. Elnajjar, Review
of hydrogen–gasoline SI dual fuel engines: engine performance and emission,
Energy Rep. 9 (2023) 4547–4573.
[162] I. Veza, A. Afzal, M.A. Mujtaba, A. Tuan Hoang, D. Balasubramanian, M. Sekar, I.
M.R. Fattah, M.E.M. Soudagar, A.I. El-Seesy, D.W. Djamari, A.L. Hananto, N.
R. Putra, N. Tamaldin, Review of artificial neural networks for gasoline, diesel
and homogeneous charge compression ignition engine, Alex. Eng. J. 61 (11)
(2022) 8363–8391.
[163] T. Wallner, S. Miers, S. McConnell, A Comparison of Ethanol and Butanol as
Oxygenates Using a Direct-Injection, Spark-Ignition (DISI) Engine, 2009.
[164] L. Wei, P. Geng, A review on natural gas/diesel dual fuel combustion, emissions
and performance, Fuel Process. Technol. 142 (2016) 264–278.
[165] F. Wu, C.K. Law, An experimental and mechanistic study on the laminar flame
speed, Markstein length and flame chemistry of the butanol isomers, Combust.
Flame 160 (12) (2013) 2744–2756.
[166] Z. Zhang, W. Long, Z. Cui, P. Dong, J. Tian, H. Tian, X. Meng, Visualization study
on the ignition and diffusion combustion process of liquid phase ammonia spray
ignited by diesel jet in a constant volume vessel, Energy Convers. Manag. 299
(2024) 117889.
[167] Z. Li, Y. Wang, Z. Yin, Z. Gao, Y. Wang, X. Zhen, An exploratory numerical study
of a diesel/methanol dual-fuel injector: effects of nozzle number, nozzle diameter
and spray spacial angle on a diesel/methanol dual-fuel direct injection engine,
Fuel 318 (2022) 123700.
[168] Z. Liu, A.M. Dizqah, J.M. Herreros, J. Schaub, O. Haas, Simultaneous control of
NOx, soot and fuel economy of a diesel engine with dual-loop EGR and VNT using
economic MPC, Control Eng. Pract. 108 (2021) 104701.
[169] W. Wang, C. Tang, Z. Huang, Diesel-natural gas dual fuel injection strategy effects
on engine ignition delay and cylinder pressure evolution, Case Stud. Therm. Eng.
53 (2024) 103795.
T. Li et al. Journal of the Energy Institute 119 (2025) 102006 
29
