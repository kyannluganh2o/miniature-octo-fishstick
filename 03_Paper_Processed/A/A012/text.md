<!-- PDF_PAGE: 1 -->

THE INTERACTION BETWEEN THE PILOT DIESEL AND MAIN NG INJECTION IN AN HPDI 
ENGINE 
N. Diepstraten 
University of Technology 
Eindhoven 
Eindhoven, Netherlands 
X.L.J. Seykens 
TNO 
Helmond, Netherlands 
L.M.T. Somers 
University of Technology 
Eindhoven 
Eindhoven, Netherlands 
ABSTRACT 
High Pressure Direct Injection (HPDI) is a promising 
combustion concept for the medium - to heavy-duty industry to 
combat climate change. It uses a pilot diesel injection to ignite 
the main fuel consisting of  Natural Gas (NG ). Both fuels are 
injected directly in the combustion chamber using a dedicated 
HPDI injector. A significant reduction in carbon dioxide  and 
Particulate Matter is achieved due to the use of the low carbon 
fuel NG.  It is seen in literature that a small chan ge in pilot 
injection can have profound consequence s for the HPDI 
combustion. This research investigates the interaction between 
the pilot diesel and main NG injection. A relevant Computational 
Fluid Dynamics (CFD) simulation environment is setup for this 
purpose. It is observed that the main NG injection needs a 
certain pilot trigger to ignite. Furthermore, local conditions are 
derived to investigate driving factors of the ignition of NG on a 
fundamental level. A homogeneous reactor model is used to study 
Ignition Delay (ID) behavior by varying the initial temperature 
as well as concentrations of  radicals H and OH.  It is observed 
that both factors influence the ID. The initial temperature has to 
be higher than 1110 K in order to ignite the  NG under engine-
like conditions. It is also observed that species mole fractions H 
or OH encountered in the CFD simulation can reduce the ID up 
to 5.5 crank angle degrees at a speed of 1400 RPM.  
Keywords: HPDI, ignition delay, dual fuel, NG, diesel, CFD 
NOMENCLATURE 
Roman 
AMR Adaptive Mesh Refinement 
aROHR Apparent Rate Of Heat Release 
aTDC After Top Dead Center 
CAD Crank Angle Degree 
CFD Computational Fluid Dynamics 
GHG Greenhouse Gas 
gROHR Gross Rate Of Heat Release 
HPDI High Pressure Direct Injection 
HRM Homogeneous Reactor Model 
ICE Internal Combustion Engine 
ID Ignition Delay 
𝑀 molar mass 
MUSCL Monotonic Upstream -Centered Scheme for 
Conservation Laws 
NG  Natural Gas 
RIT  Relative Injection Timing 
𝑇  temperature 
TDC Top Dead Center 
𝑉 volume 
𝑋 mole fraction 
𝑐 specific heat of mixture 
ℎ enthalpy 
𝑚 mass 
𝑡 time 
Greek 
𝜔  reaction rate 
Sub- & Superscript 
0 initial condition 
𝑝 pressure 
𝑠 species 
1. INTRODUCTION
Climate change is widely accepted to be caused by greenhouse 
gases (GHG). Carbon dioxide and methane have the largest 
contribution to the GHG emissions [1]. To combat climate 
change, GHG emissions need to be reduced significantly; the 
ultimate goal is to achieve zero emission on the net balance by 
2050 [2]. Currently, transportation is responsible for a significant 
(~24%) amount of GHG emissions [3]. The Internal Combustion 
Engine (ICE) is predomin ant in the transportation sector and 
responsible for a large amount of GHG emissions. However, 
especially for medium and heavy duty applications, it is expected 
that the ICE principle will remain of vital importance in the 
foreseeable future [4]. For this reason, much research is 
Proceedings of the ASME 2021 
Internal Combustion Engine Division Fall Technical Conference 
ICEF2021 
October 13-15, 2021, Virtual, Online 
ICEF2021-74466
V001T06A013-1
Copyright © 2021 by ASME
Downloaded from asmedigitalcollection.​asme.​org/​ICEF/​proceedings-pdf/​ICEF2021/​85512/​V001T06A013/​6802978/​v001t06a013-icef2021-74466.​pdf by Dalian University Of Technology user on 31 August 2026

<!-- PDF_PAGE: 2 -->

conducted on the ICE to increase its efficiency and to reduce its 
emissions.  
Besides this long-term goal, there is also a legislative drive 
to improve the transportation sector on the short term. In 2025, 
the CO 2 emission needs to be reduced by 15% with respect to 
2019 for heavy -duty applications [5]. It is currently under 
discussion whether the CO 2 emissions in 2030 for these 
applications have to be reduced by 30% with respect to 2019.  
Also, the regulations for methane emissions become more 
stringent. It is expected that the methane emissions will have to 
reduce by 80-90% for heavy-duty applications in Europe [6]. 
High Pressure Direct Injection (HPDI) is a promising 
combustion concept. The underlying philosophy is that a high 
reactive fuel is used to trigger auto-ignition of a low reactive fuel. 
A pilot injection of diesel is employed to ignite the main fuel 
consisting of Natural Gas (NG). HPDI combustion unites two 
fundamental advantages of diesel and NG combustion [7]. From 
diesel combustion, it mainly preserves its high specific torques 
which is partly thanks to the fact that it allows for high 
compression ratios. It is shown that HPDI can reduce CO 2 
emissions with 20% and particulate m atter with 65% compared 
to a diesel engine, while preserving a high thermal efficiency [8]. 
The CO2 reduction is mainly due to the low carbon content of the 
NG; it consists for a vast majority of methane (~90 mass%). This 
shows that HPDI combustion concept is a good candidate to meet 
the earlier mentioned CO 2 legislations for 2025. Methane 
emissions, on the other hand, might be of a challenge as 
legislative limits on methane emissi ons are expected to become 
more stringent.  Besides the advantage of CO 2 and Particulate 
Matter emission reduction, the HPDI combustion concept 
requires few modifications on a diesel power train, making it a 
well-suited intermediate combustion technology towards a zero-
emission future. 
The HPDI combustion principle requires a dedicated 
injector, which has been developed by Westport Fuel Systems 
[9]. By using two concentric needles, both fuels can be controlled 
independently of each other. The dual concentric needle design 
allows for a maximal spatial efficiency in order to minimize the 
space required in the cylinder head . FIGURE 1 shows a 
schematic overview of the dual concentric needle concept.  
 
 
FIGURE 1: INJECTOR TIP ASSEMBLY OF HPDI INJECTOR, 
SHOWING THE DUAL CONCENTRIC NEEDLE DESIGN. 
ADAPTED FROM KHEIRKHAH [10]. 
As the piston approaches Top Dead Center (TDC), a small 
amount of diesel fuel is injected at approximately 300 bar as 
indicated by the diesel injection in  fig. 2. This is called the pilot 
injection and its function is to increase the reactivity of the in -
cylinder mixture. After a couple Crank Angle Degree  (CAD), 
NG is injected at a slightly lower pressure. This is called the main 
injection. The injected NG mass typically comprises 90-95% of 
the total injected – chemically stored – energy [11].  
 
FIGURE 2: SCHEMATIC REPRESEN TATION OF THE MAIN 
EVENTS IN HPDI COMBUSTION. 
The effect of different injection strategies on the heat release 
profile and emissions  is investigated in literature  [11]. In the 
work of Faghani et al., it is shown that one CAD difference in 
Relative Injection Timing (RIT)  can result in the halving of the 
peak Apparent Rate Of Heat Release (aROHR)  and engine-out 
emissions of methane and NOx  [12]. This indic ates that the 
timing of the pilot injection relative to the main injection timing 
influences the combustion and emissions to a large extent. Since 
the combustion is dominated by the main fuel, NG, the question 
arises which factors are driving the ignition of the NG. 
Also t he work of Ouellette indicates that there is a clear  
interaction between the combustion of the pilot and main 
injection [13]. In his work, two different mechanisms of main 
injection ignition by the pilot are suggested: 
▪ The pilot combustion causes a global rise in pressure and 
temperature of the in-cylinder mixture thus triggering the 
NG-jet to ignite. 
▪ There is a direct interaction between the pilot and main 
fuel jet. Hot combustion products of the pilot fuel 
combustion entrain the (gaseous) main fuel jet which 
causes a local temperature rise of the fuel/air mixture in 
the jet. 
The latter mechanism seems to be appropriate regarding the 
spatial and temporal resolution of this study. A detailed 
explanation of the effect of hot combustion products on the 
ignition of the main injection lacks. Besides a local temperature 
rise, also the chemical composition of the hot combustion 
products influences the ignition. However, the role of radicals is 
neglected in the work of Ouellette.  It appeared that there is a 
literature gap regarding the NG ignition on a detailed level. 
As earlier mentioned, the ignition of the NG determines the 
development of the combustion process, hence the emissions. In 
other words, the way the pilot diesel injection influences the 
ignition of the main NG can have profound consequences on the 
performance of the engine regarding efficiency and emissions. 
The aim of this research is to study the effect of the pilot diesel 
injection on the ignition of the main NG numerically. The earlier 
V001T06A013-2
Copyright © 2021 by ASME
Downloaded from asmedigitalcollection.​asme.​org/​ICEF/​proceedings-pdf/​ICEF2021/​85512/​V001T06A013/​6802978/​v001t06a013-icef2021-74466.​pdf by Dalian University Of Technology user on 31 August 2026

<!-- PDF_PAGE: 3 -->

explained work of Ouellette is taken as starting point. The next 
section describes the approach and the outline of the paper.  
 
2. APPROACH 
This research consists of two parts. In the first part, two CFD 
simulations are performed: 
1. Pilot diesel and main NG injection (HPDI operation). 
2. Main NG injection only. 
Please note that all CFD settings remain the same, except for the 
pilot injection. The purposes of these simulations a re twofold.  
Firstly, the need for a pilot injection to trigger the NG ignition is 
checked. This is accomplished by comparing the Gross Rate of 
Heat Release (gROHR) of the two results. The first simulation is 
used to derive local conditions. These are used to investigate the 
driving factors of NG ignition on a fundamental level, which is 
done in the second part (section 5) of this research. For this 
purpose, a Homogeneous Reactor Model (HRM) will be used. 
The HRM allows for a proper analysis of the reaction kinetics, 
since chemistry is isolated from physical effects  [14]. For 
example, turbulence caused by fuel injections is not considered. 
The specific implem entation is based on MATLAB based 
Cantera model [15]. The input for the HRM is acquired from the 
CFD simulation results. In both CFD as well as the HRM, the 
same chemical mechanism is used [16]. The computation time 
of a HRM, however, is much shorter than a CFD simulation 
(approximately one second and thirty hours, respectively). It 
therefore allows to study certain effects more extensively than 
CFD in the available time span. 
Key features to setup a relevant CFD environment for HPDI 
combustion are explained in section 3. Subsequently, the results 
for the first part are used in section 4. Theory regarding the HRM 
is provided in section 5, in which it is also explained in detail 
how this part of the research is conducted. Next, the results of 
the second part of the research are presented in section 6. Finally, 
conclusions are drawn, and recommendations are made in 
section 7. 
 
3. CFD SIMULATION ENVIRONMENT 
CONVERGE is chosen to perform the CFD simulations [17]. To 
setup a relevant CF D simulation environment  that allows to 
model HPDI combustion , single cylinder measurement data is 
used to ensure a close link to experimental results. The numerical 
study is performed under engine -like conditions; an operation 
point was selected at medium  speed (1400 RPM) and medium 
load (1285 Nm). Experimental results show a predominantly 
premixed combustion at this operation point. Relevant engine 
parameters used to develop the CFD simulation environment are 
shown in tab. 1. CONVERGE allows the simulation time to be 
crank angle based. The simulated time is between -20 and 140 
CAD aTDC. All valves are closed in this interval. 
 
 
 
 
 
 
TABLE 1: ENGINE SPECIFICATIONS. 
Engine base type Volvo G13C 
Cylinder / Valves  6 / 4 
Swept vol. per cyl. 2 liters 
Bore / Stroke 131 / 158 mm 
Compression ratio ~17:1 
Piston bowl Re-entrant 
Injector Westport HPDI 
Number of injector nozzles 9 diesel, 9 NG, equally 
spaced 
 
3.1 Geometry 
The HPDI injector has 9 evenly spaced nozzle holes for each 
fuel, so it is symmetric around 40 °. The engine counts 4 valves 
per cylinder, making the head symmetric around 90 °. The in-
cylinder geometry as a whole is therefore not symmetric. 
Nonetheless, it is chosen to use a sector mesh of 40 °, for the 
advantage of a strongly reduced computation time. The piston 
deck height  is used to optimize the compression ratio to 
compensate for the error in the head volume due to the 
asymmetry. Fig. 3 shows a close-up of the injector. Fig. 4 & fig. 
5 show a top and side view of the geometry , respectively. The 
main NG injection is modelled as an inflow boundary . These 
boundaries are indicated by the  two green semi -circles; each 
semi-circle injects 50% of the total injected NG per nozzle hole. 
 
 
FIGURE 3: MESH ZOOM ON INJECTOR. 
 
FIGURE 4: TOP VIEW OF MESH. 
V001T06A013-3
Copyright © 2021 by ASME
Downloaded from asmedigitalcollection.​asme.​org/​ICEF/​proceedings-pdf/​ICEF2021/​85512/​V001T06A013/​6802978/​v001t06a013-icef2021-74466.​pdf by Dalian University Of Technology user on 31 August 2026

<!-- PDF_PAGE: 4 -->

FIGURE 5: SIDE VIEW OF MESH. 
3.2 Numerical Settings 
Implementation of the appropriate settings are required to solve 
this transient problem accurately. The numerical models used in 
this research are summarized in  tab. 2. The SAGE combustion 
model is used for its accurate prediction regarding Ignition Delay 
(ID) and flame lift off length [18].  
A 3D Monotonic Upstream-Centered Scheme for 
Conservation Laws (MUSCL)  is chosen to describe the 
convective flux scheme. Paired with the method of 
Venkatakrishnan [19], this setting provides second -order 
accuracy for the convection term and a smooth solution. MUSCL 
results in less numeric noise at large gradients compared to the 
default flux bending scheme,  but requires slightly more 
computational effort. 
Furthermore, Adaptive Mesh Refinement (AMR)  is used. 
This locally refines the mesh based on fluctuating and moving 
conditions if the sub-grid criterion is exceeded. In this research, 
a sub-grid criterion of 5 K is used for the temperature and 2 m/s 
for the velocity. The maximum embedding level is set to 4.  
Besides AMR, the mesh can also be locally refined at specified 
locations and times using a fixed embedding. In this research, the 
liner, head and piston are embedded throughout the simulation. 
The jet areas for both injections are  broadly embedded around 
the injections only. All embeddings and AMR are relative to the 
defined base mesh which, based on a sensitivity study, has a cell 
size of 4x4x4 mm3. 
 
TABLE 2: NUMERICAL CFD SETTINGS. 
Topic Setting 
Combustion SAGE with Adaptive Zoning 
CVODES with dense solver 
Chemical reaction 
mechanism 
NG/n-heptane mechanism: 76 
species, 464 reactions [16]  
Navier-Stokes solver PISO, density-based 
Convective flux MUSCL, Venkatakrish nan flux 
limiter 
Turbulence RANS approach, RNG κ-ε model 
Spray Frossling evaporation model 
O’Rourke turbulent dispersion 
Kelvin-Helmholtz & Rayleigh -
Taylor spray atomization 
Gas E.o.S. Redlich-Kwong 
 
3.3 HPDI injector 
The pilot diesel injection is modelled using the dedicated spray 
modelling module for liquid fuel injection in CONVERGE. 
Relevant pilot injection parameters are included in tab. 3. A high 
caloric NG consisting of 89 mass% methane is used in this 
research as main fuel. In reality, is pressurized using a cryogenic 
pump and a gas conditioning module ensures that it is contained 
between 150 -300 bar [7]. The NG is liquefied under these 
circumstances. During the transportation of the fuel from the 
tank to the injector, heat is transferred by convection which 
results in a rise of fuel temperature. The temperature of the NG 
at the injector nozzle is estimated at 328 K. The injection 
pressure is ~235 bar. Under these circumstances, the fuel is not 
liquid anymore, but supercritical. The main fuel injection c an 
therefore not be implemented similarly to the pilot fuel injection; 
an inflow boundary was defined instead. This is realized by 
defining a mass flow profile and a fixed fuel temperature (328 
K). The pressure was constrained by a Neumann boundary 
condition. Relevant main injection parameters are included in  
tab. 3. 
 
TABLE 3: INJECTION PARAMETERS. 
Parameter Pilot diesel Main NG 
SOI [CAD aTDC] -15.3 -11.1 
DOI [CAD aTDC] 10.7 18.1 
Mass [mg/stroke] 2.27 122 
Pressure [bar] 245 234 
 
4. CFD RESULTS 
The results of the first part of the research are presented in this 
section. As earlier explained, it is studied to which extent the NG 
needs a n ignition  trigger from the pilot. This is done by 
comparing the gROHR of a HPDI operation cycle and a main 
NG injection only cycle. After that, the inputs for the HRM 
simulations are gathered. 
Fig. 6  shows the gROHR of the HPDI operation and the 
main injection only cycle. The pilot combustion of the HPDI 
operation is observed between -8 until -5 CAD aTDC, 
approximately. The combustion of the main fuel starts around -
5 CAD aTDC. There is no heat released during the main injection 
only cycle, hence the NG did not ignite. It can therefore be 
concluded that the NG needs a pilot trigger to combust. 
To investigate the NG ignition in more detail, 3D simulation 
results of the HPDI operation are used to localize the ignition of 
the NG. An often used indicator for ignition is OH concentration. 
However, OH production due to ignition occurs in diesel as well 
as NG combustion. Consequently, the location of ignited NG 
becomes indistinguishable from the pilot diesel combustion . 
Since this study aims to isolate the NG ignition from the pilot 
diesel combustion, this parameter is not suitable in this study.  
V001T06A013-4
Copyright © 2021 by ASME
Downloaded from asmedigitalcollection.​asme.​org/​ICEF/​proceedings-pdf/​ICEF2021/​85512/​V001T06A013/​6802978/​v001t06a013-icef2021-74466.​pdf by Dalian University Of Technology user on 31 August 2026

<!-- PDF_PAGE: 5 -->

Inspecting the reaction ki netics of the main component of the 
NG, which is methane, learns that three possible reactions can 
initiate the combustion of methane. These reactions are: 
 
CH4 + M ⇌ CH3 + H + M  (1a) 
CH4 + H ⇌ CH3 + H2  (1b) 
CH4 + OH ⇌ CH3 + H2O  (1c) 
 
 
FIGURE 6: GROHR OF THE HPDI OPERATION CYCLE AND 
MAIN INJECTION ONLY CYCLE, INCLUDING INJECTION 
PROFILES. 
All create a methyl radical: CH 3.  High concentrations of CH 3 
instead of OH are for this reason used to find the location at 
which the NG starts to combust. Fig. 8a and 8b show the sector 
mesh at crank angle at -7.2 (±0.1) CAD aTDC. The NG jet is 
visualized by the light (white) iso -surface. The high local 
temperatures are the result of the  pilot diesel combustion. This 
angle is chosen because this is the first instance  at which CH3 
clearly emerges from  the NG ignition and not from  the pilot 
diesel combustion. 
The penetration of the pilot diesel spray is rather small. As 
a result, the NG jet is ignited close to the injector. At the moment 
of ignition, the NG is already being injected for approximately 4 
CAD. The gaseous jet has penetrated relatively far at this poi nt 
and a significant part of the injected fuel has had the opportunity 
to mix with surrounding air.  The first  peak occurring after 
ignition is often referred to as the premixed peak in conventional 
diesel combustion. As can be seen  in fig. 6 , combustion is 
dominated by the premixed peak.  
It is also observed that the pilot combustion has a flat surface 
adjacent to the NG jet. At its border area ( dark bluish surface), 
the interaction with the NG jet is high. Within this interface, the 
CH3 mass fraction is  observed to be  higher than 10-4. The 
coordinate indicated by the red dot is chosen to derive local 
conditions to investigate the NG ignition on a fundamental level 
using the HRM. It should be noted that the conditions do not vary 
significantly in the interface  Appendix A ). The selected 
properties are therefore a proper representation of the conditions 
just before ignition.  In fig. 9, the main NG injection only result 
is shown. The same coordinate is indicated by the red dot as in  
fig. 8 . This simulation provides information on mixing of NG 
with air only. 
 
 
FIGURE 7A: CONTOUR PLOT OF SECTOR MESH AT -7.2 CAD 
ATDC, SHOWING ISO -SURFACES OF TEMPERATURE (200 0K, 
GREEN), CH4 (5 %MASS, WHITISH), MASS FRACTION CH3 (0.01 
%MASS, DARK BLUISH) AND SELECTED COORDINATE (RED). 
 
 
FIGURE 8B: CLOSE-UP OF SECTOR MESH  AROUND 
INJECTION AT -7.2 CAD ATDC, SHOWING ISO -SURFACES OF 
TEMPERATURE (2000K, GREEN), CH4 (5 %MASS, WHITISH), 
MASS FRACTION CH3 (0.01 %MASS, DARK BLUISH) AND 
SELECTED COORDINATE (RED). 
V001T06A013-5
Copyright © 2021 by ASME
Downloaded from asmedigitalcollection.​asme.​org/​ICEF/​proceedings-pdf/​ICEF2021/​85512/​V001T06A013/​6802978/​v001t06a013-icef2021-74466.​pdf by Dalian University Of Technology user on 31 August 2026

<!-- PDF_PAGE: 6 -->

FIGURE 9: SECTOR MESH OF THE MAIN NG INJECTION 
ONLY SIMULATION SHOWING ISOSURFACE OF METHANE (5 
MASS%) AND SELECTED COORDINATE IN RED. 
The chemical composition at this coordinate is shown in fig. 10, 
displaying the 20 most dominant species. From these 
characteristic levels of the radi cals at the point of ignition are 
extracted. The base HRM inputs, i.e. composition, pressure and 
temperature are extracted from the NG only simulations and  are 
shown in tab. 4. The equivalence ratio of the composition is also 
shown to indicate the richness of the mixture.  The next section 
elaborates the second part of the research. 
 
 
FIGURE 10: CHEMICAL COMPOSITION OF THE SELECTED 
COORDINATE. 
 
 
 
 
TABLE 4: PROPERTIES OF THE SELECTED COORDINATE. 
Parameter Value 
Pressure [bar] 90.5 
Temperature [K] 851 
Equivalence ratio [-] 0.91 
N2 [Massfrac] 0.73 
O2 [Massfrac] 0.22 
CH4 [Massfrac] 0.043 
OH [Massfrac] 3.46e-14 
H [Massfrac] 7.94e-19 
 
5. HRM THEORY 
Thanks to the simplified approach of a HRM with respect to 
CFD, the driving factors of the main NG ignition can be analyzed 
on a more fundamental level, while computation time remains 
small. In the used HRM, the pressure is taken to be constant and 
the gas is assumed ideal. Furthermore, no mass or heat flux in or 
out the boundary is allowed.  The resulting governing equations 
can be expressed as: 
 
𝑚𝑐𝑝
𝑑𝑇
𝑑𝑡 = ∑ ℎ𝑠
𝑑𝑚𝑠
𝑑𝑡
𝑁𝑠
𝑠    (2a) 
𝑑𝑚𝑠
𝑑𝑡 = 𝑉 ⋅ 𝑀𝑠𝜔𝑠   (2b) 
 
where 𝑚 is the mass, 𝑇 the temperature, 𝑡 time, 𝑐𝑝 the specific 
heat of the mixture, ℎ𝑠 the enthalpy of species 𝑠, 𝑉 the volume, 
𝑀 the molar mass and 𝜔𝑠 the reaction rate of species 𝑠. 𝑁𝑠 is the 
total number of species cons idered. The reaction rates are 
computed from the same chemical mechanism used in the CFD 
simulations [16]. 
To study the ignition of the main NG, both temperature and 
species mass fractions are varied. Two species are selected in this 
research. Equation s 1a - 1c show the three reactions that can 
initiate the combustion of the main component of the main fuel, 
which is methane. It can be seen that M, H and OH are the only 
species that can i nitiate (hence ignite) the combustion. Third 
body M can embody any species  and will determine the auto -
ignition of NG . The two radicals OH and H  determine the 
initiation when a radical pool, like here, is present. Other species 
or radicals that might initiate the ignition of other components of 
the main fuel are left out of the scope of this research. 
The NG is defined to ignite when the temperature rise has 
reached 5% of the maximal temperature rise, also known as the 
τ5 criterion: 
 
𝑇(𝜏5) − 𝑇0 =
5
100 ⋅ (max(𝑇) − 𝑇0)  (3) 
 
where 𝑇0 is the initial temperature and 𝜏5 the time after which 
the temperature has reached 5% of the maximal temperature rise. 
This time is used to define ID in this work. 
The HRM is used to compute the ID of certain chemical 
composition at a certain pressure and temperature. The maximal 
allowed ID is set to 7 CAD. Please note that the initial 
V001T06A013-6
Copyright © 2021 by ASME
Downloaded from asmedigitalcollection.​asme.​org/​ICEF/​proceedings-pdf/​ICEF2021/​85512/​V001T06A013/​6802978/​v001t06a013-icef2021-74466.​pdf by Dalian University Of Technology user on 31 August 2026

<!-- PDF_PAGE: 7 -->

composition is taken at -7.2 CAD aTDC, so an ID of 7 CAD 
means that the ignition would occur just before TDC. If the NG 
ignites after this point, the combustion timing is considered too 
late. 
 
6. HRM RESULTS 
The initial temperature and the mass fractions of the selected 
species are varied. The minimum values for the initial 
temperature and species concentration (left bottom of fig. 11 & 
fig. 12 ) are  equal to the conditions obtained at the selected 
coordinate of the main NG injection only cycle (fig. 9 & fig. 10). 
As can be seen these initial values gathered from the main NG 
only cycle (tab. 4 and fig. 10) also do not ignite within the period 
of 7 CAD  in this HRM simulatio n which is  in line with  the 
observations from section 4. A series of HRM’s is computed 
with t he initial temperature spanning the range from probed 
value up to 1400 K  and the initial H and OH  concentration 
spanning the range from the probed value up to 1 mass%. 
The result for varying the temperature and OH is shown in  
fig. 11  and the same for  varying the H radical in fig. 12. The 
vertical axis is given in mole fraction  since reaction rates are 
determined by concentration . The grey iso -lines indicate the 
values of 0.1, 0.5, 1, 2, ..., 7 CAD. The white, or uncovered area 
at low temperature and species concentrations indicates that the 
NG does not ignite  sufficiently fast under these circumstances.  
The shaded area in the upper part of the figures indicate s that 
such (high) mole fractions are not encountered in  the CFD 
simulations. These values are 8∙10-4 and 3.8∙10-3 for H and OH, 
respectively. In fact, t ypical c onditions that are encountered 
within the probe volume of fig. 8 are indicated by the blue dotted 
box. Temperatures within the probe volume of fig. 8 reach up to 
2400 K, thereby outranging the computed HRM’s. It can be seen 
that the presence of OH and H radicals influences the ID under 
circumstances representing engine -like conditions . Please note 
that the staircase behavior at low temperatures and high  mole 
fractions is due to the large sensitivity of ID on T and H and OH 
mole fractions at these conditions and that the chosen resolution 
is not high enough . Moving along the x -axis mimics addin g a  
heat source whilst keeping the composition constant, whereas 
moving along the y-axis a radical source is added at constant T.  
Both figures indicate that adding a species source, either H 
or OH, is only effective if large, unrealistic amounts are added. 
Above 1100 K the reactivity increase by T only dominates (e.g. 
∂ID/∂𝑋𝐻≈ 0). Only between 950 - 1100 K, the H and OH have 
a significant impact at realistic concentrations. For both H and 
OH, that holds for fractions above 10 -6. Increasing the mol e 
fraction H can reduce the ID up to approximately 4.5 CAD; for 
OH this reduction can reach up to 5.5 CAD. These are significant 
reductions which hav e profound consequences for the 
combustion behavior. 
 
FIGURE 11: CONTOUR PLOT OF TEMPERATURE AND OH 
MASS FRACTION V ARIATION INDICATING ID IN CAD AT 1400 
RPM. BLUE DOTTED BOX INDICATES TYPICAL V ALUES 
FOUND IN THE PROBE VOLUME. 
 
FIGURE 12: CONTOUR PLOT OF TEMPERATURE AND H 
MASS FRACTION V ARIATION INDICATING ID IN CAD AT 1400 
RPM. BLUE DOTTED BOX INDICATES TYPICAL V ALUES 
FOUND IN THE PROBE VOLUME. 
7. CONCLUSIONS AND RECOMMENDATIONS 
In this research, a CFD simulation environment with appropriate 
geometry and injection settings is developed to investigate the 
interaction between the pilot and main injection in a HPDI 
engine. The developed CFD model enabled t he visualization of 
the HPDI combustion. With these results, it is shown that the 
main fuel does not ignite without the pilot injection at the 
selected operation point. In other words, the NG requires a 
trigger from pilot diesel combustion to ignite. 
The ignition of the NG is determined at -7.2 CAD aTDC for 
a medium load point . At this point, a significant part of the 
V001T06A013-7
Copyright © 2021 by ASME
Downloaded from asmedigitalcollection.​asme.​org/​ICEF/​proceedings-pdf/​ICEF2021/​85512/​V001T06A013/​6802978/​v001t06a013-icef2021-74466.​pdf by Dalian University Of Technology user on 31 August 2026

<!-- PDF_PAGE: 8 -->

injected NG mass has mixed with surrounding air causing a 
predominantly premixed combustion behavior. 
The HRM simulations show that the ignition behavior of 
NG is both temperature as well as species dependent. The NG/air 
mixture can be ignited sufficiently fast enough if only a heat 
source is added. Also adding a H sources could cause ignition. 
However, required concentrations are higher than typical values 
encountered in the CFD simulation.  The knowledge gathered 
from these simulations can be useful for further development of, 
for example, injector geometry and injection parameters 
optimization. 
It is seen that the sensitivity of the H and OH concentrations 
on th e ID can reach up to 5.5 CAD, which is a rather large 
sensitivity. This could indicate the need to control the H and OH 
concentrations at NG ignition for further HPDI combustion 
development. The ID can be reduced maximally if both local OH 
and H concentrat ions as well as  the local  temperature is 
increased. This can, for example, be achieved by increasing the 
pilot combustion (increasing the injected diesel mass). However, 
this is not preferred due to its negative emission effects. Another 
possibility is to enhance the injection interaction (by changing 
the nozzle hole geometry or increasing turbulence).   
This research has analyzed the effect of temperature and 
species concentrations H and OH on the ID separately using 
HRM simulations. It is recommended to s tudy the individual 
effects (temperature and species concentration) in CFD . When 
the driving factors of the ignition are studied separately in CFD, 
physical effects such as turbulence are taken into account. This 
can be done by adding local energy or species sources. 
 
REFERENCES 
[1] IPCC, 2014,  “Climate Change 2014 Mitigation of 
Climate Change”. 
[2] UN, 2015, “Paris Agreement.” p. 27. 
[3] IEA, 2020, “Tracking Transport 2020,” Paris. 
[4] Kalghatgi G. T., 2015  “Developments in internal 
combustion engines and implications for combustion 
science and future transport fuels,” Proc. Combust. Inst., 
vol. 35, no. 1, pp. 101–115. 
[5] EU, 2019, “Regulation (EU) 2019/1242 of the European 
Parliament and of the Council of 20 June 2019 Setting 
CO2 emission performance standards for new heavy -
duty vehicles and amending Regulations (EC) No 
595/2009 and (EU) 2018/956 of the European 
Parliament,” Off. J. Eur. Union, vol. L 198, no. April, pp. 
202–240. 
[6] ACEA, 2020 , “ACEA Position Paper Views on 
proposals for Euro 7 emission standard” . 
[7] Ouelette, P., Goudie, D., and McTaggart-Cowan, G., 
2016, “Progress in the development of natural gas high 
pressure direct injection for Euro VI heavy -duty 
trucks,”. 
[8] Harrington, J., Munshi, S., Nedelcu, C., Ouellette, P., 
Thompson, J., and Whitfield, S., 2002, “Direct injection 
of natural gas in a heavy-duty diesel engine,” Reno. 
[9] Westport, “Westport HPDI 2.0,” 2021. [Online]. 
Available: https://wfsinc.com/our -solutions/hpdi-
2.0#section2. [Accessed: 26-Jan-2021]. 
[10] Kheirkhah, P., 2015, “CFD modeling of injection 
strategies in a High -Pressure Direct - Injection (HPDI) 
natural gas engine,” no. April. 
[11] Faghani, E., Kheirkhah, P., Mabson, C. W. J. , 
McTaggart-Cowan, G., Kirchen, P., and Rogak, S., 2017, 
“Effect of Injection Strategies on Emissions from a Pilot-
Ignited Direct-Injection Natural-Gas Engine- Part I: Late 
Post Injection,” SAE Tech. Pap., no. March. 
[12] Faghani, E., Kheirkhah, P., Mabson, C., McTaggart -
Cowan, G., Kirchen, P., and Rogak, S.,, 2017, "Effect of 
Injection Strategies on Emissions from a Pilot -Ignited 
Direct-Injection Natural -Gas Engine - Part II: Slightly 
Premixed Combustion," SAE Tech. Pap. 2017-01-0763, 
doi:10.4271/2017-01-0763. 
[13] Ouellette, P., 1996, “Direct injection of natural gas for 
diesel engine fueling” PhD thesis Univ. vritish columbia, 
no. February. 
[14] Somers, L. M. T., Bakker, P. C., Maes, N. C. J. , and 
Seykens, X. L. J. , 2019, “Reader: Clean engines and 
future fuels.” Eindhoven, p. 177. 
[15] Goodwin, D. G., Speth, R. L., Moffat, H. K., and Weber, 
B. W. , 2018, “Cantera: An Object -oriented Software 
Toolkit for Chemical Kinetics, Thermodynamics, and 
Transport Processes,” . [Online]. Available: 
https://www.cantera.org. [Accessed: 18-Jan-2021]. 
[16] Rahimi, A., Fatehifar, E., and Saray, R. K. , 2010, 
“Development of an optimized chemical kinetic 
mechanism for homogeneous charge compression 
ignition combustion of a fuel blend of n -heptane and 
natural gas using a genetic algorithm,” Proc. Inst. Mech. 
Eng. Part D J. Automob. Eng., vol. 224, no. 9, pp. 1141–
1159. 
[17] Richards, K. J., Senecal, P. K., and Pomraning, E., 
CONVERGE 3.0, Convergent Science, Madison, WI 
(2020). 
[18] Moiz, A. A., Som, S., Bravo, L., and Lee, S. Y ., 2015, 
“Experimental and Numerical Studies on Combustion 
Model Selection for Split Injection Spray Combustion,” 
SAE Tech. Pap., vol. 2015-April, no. April. 
[19] Venkatakrishnan, V., 1993, “On the accuracy of limiters 
and convergence to steady state solutions,” Reno, NV , 
United States. 
 
  
V001T06A013-8
Copyright © 2021 by ASME
Downloaded from asmedigitalcollection.​asme.​org/​ICEF/​proceedings-pdf/​ICEF2021/​85512/​V001T06A013/​6802978/​v001t06a013-icef2021-74466.​pdf by Dalian University Of Technology user on 31 August 2026

<!-- PDF_PAGE: 9 -->

APPENDIX A 
The chemical composition of three additional coordinates (indicated by point 2 -4) are provided in tab. 5. All these coordinates are 
located within the volume containing ≥  0.01 mass% CH3 of fig. 8 and at a similar temperature. However, they are distributed over the 
CH3 iso-surface volume. Please note that the compositions presented are taken from the main NG injection only cycle. The properties 
of these coordinates show that the physical and chemical properties of these points are quite similar. This means that the sensi tivity of 
the initial chemical composition on the ID will be relatively small.  
 
TABLE 5: PROPERTIES OF FOUR COORDINATES INSIDE PROBE VOLUME 
 
Point 1 Point 2 Point 3 Point 4 Avg. ± dev. [%] 
Pressure 9.05E+06 9.06E+06 9.05E+06 9.04E+06 9.05E+06 ± 0.07 
Temperature 851.5 863.5 848.8 865.1 857.2       ± 0.98 
Equivalence ratio 0.912 0.737 1.027 0.699 0.844       ± 21.7 
Mass frac. N2 0.733 0.7398 0.73 0.7414 0.7360     ± 0.82 
Mass frac. O2 0.2188 0.2209 0.218 0.2214 0.2198     ± 0.83 
Mass frac. CH4 0.04334 0.03528 0.04682 0.03348 0.03973   ± 17.8 
Mass frac. C2H6 0.00428 0.00349 0.00463 0.00331 0.00393   ± 17.8 
Mass frac. C3H8 0.00057 0.00047 0.00062 0.00044 0.00052   ± 17.8 
Mass frac. C2H4 3.41E-10 3.37E-10 3.01E-10 2.90E-10 3.17E-10 ± 8.59 
Mass frac. CH3 1.21E-10 1.30E-10 1.20E-10 1.14E-10 1.21E-10 ± 7.49 
Mass frac. CH2O 6.50E-11 6.78E-11 6.50E-11 6.74E-11 6.63E-11 ± 2.26 
Mass frac. H2O 3.91E-11 4.08E-11 3.91E-11 4.05E-11 3.99E-11 ± 2.33 
Mass frac. C3H6 2.69E-11 2.66E-11 2.38E-11 2.29E-11 2.50E-11 ± 8.54 
Mass frac. H2O2 1.01E-11 9.33E-12 7.94E-12 7.90E-12 8.81E-12 ± 14.3 
Mass frac. CO2 1.68E-13 1.44E-13 1.53E-13 1.39E-13 1.51E-13 ± 11.1 
Mass frac. OH 3.46E-14 2.70E-14 3.77E-14 8.58E-14 4.63E-14 ± 85.3 
Mass frac. CO 3.18E-14 3.40E-14 3.36E-14 3.63E-14 3.39E-14 ± 6.92 
Mass frac. H2 3.04E-16 3.02E-16 2.60E-16 2.48E-16 2.79E-16 ± 10.9 
Mass frac. H 7.94E-19 1.02E-18 8.81E-19 7.22E-19 8.54E-19 ± 19.5 
Mass frac. C2H2 1.94E-19 1.97E-19 1.84E-19 2.03E-19 1.95E-19 ± 5.20 
Mass frac. C6H12 5.40E-24 5.19E-24 4.52E-24 4.61E-24 4.93E-24 ± 9.60 
Mass frac. NO 1.33E-24 1.38E-24 1.42E-24 1.53E-24 1.41E-24 ± 8.14 
Mass frac. C7H16 1.36E-27 1.19E-27 1.13E-27 1.14E-27 1.21E-27 ± 13.1 
Mass frac. NO2 1.51E-28 1.55E-28 1.50E-28 1.55E-28 1.53E-28 ± 1.70 
 
V001T06A013-9
Copyright © 2021 by ASME
Downloaded from asmedigitalcollection.​asme.​org/​ICEF/​proceedings-pdf/​ICEF2021/​85512/​V001T06A013/​6802978/​v001t06a013-icef2021-74466.​pdf by Dalian University Of Technology user on 31 August 2026
