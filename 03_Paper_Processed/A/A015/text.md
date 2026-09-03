<!-- PDF_PAGE: 1 -->

Fuel 337 (2023) 127160
Available online 22 December 2022
0016-2361/© 2022 Elsevier Ltd. All rights reserved.
Full Length Article 
Effects of operating parameters on combustion and soot emissions in a pilot 
ignited HPDI natural gas engine for different combustion modes 
Guisheng Chen
a , *
, Shun Yang
a
, Feng Wei
a , *
, Kaiqi Zhang
a
, Da Nie
b
, Hang Gong
c 
a
Yunnan Key Laboratory of Internal Combustion Engine, Kunming University of Science and Technology, Kunming 650500, China 
b
School of Materials Science and Engineering, Kunming University of Science and Technology, Kunming 650500, China 
c
College of Civil Aviation and Aeronautics, Kunming University of Science and Technology, Kunming 650500, China   
ARTICLE INFO  
Keywords: 
Natural gas high-pressure direct injection 
Different combustion modes 
Combustion chamber type 
Spray angle 
Injection pressure 
Soot emissions 
ABSTRACT  
In this paper, a comprehensive numerical study of the combustion and emission characteristics of a direct in -
jection natural gas engine operating at the high load condition was presented. First, two combustion modes, 
natural gas mixing-limited combustion (NMLC) and natural gas slightly premixed combustion (NSPC), were 
defined separately. Subsequently, the potential of combustion chamber type, spray angle of natural gas (SAN), 
diesel injection pressure (DIP), and natural gas injection pressure (NIP) to achieve high thermal efficiency and 
low soot emissions are evaluated in both NMLC and NSPC modes. The results showed that in both NMLC and 
NSPC modes, the straight-sided combustion chamber (SSCC) has more potential to improve the indicated thermal 
efficiency (ITE) and reduce soot emissions. In NMLC mode, an appropriate increase in SAN can promote the 
development of vortex at the bowl bottom and improve the stratification state of concentration gradient, thus 
enhancing ITE, inhibiting the production of pyrene (A
4
) and acetylene (C
2
H
2
), and reducing soot emissions. 
However, an excessive increase in SAN will lead to fuel accumulation, thus deteriorating soot emissions. In NSPC 
mode, when SAN increases to 15
◦
, ITE reaches the maximum. Meanwhile, the production of soot precursors (A
4 
and C
2
H
2
) reduces, thus soot emissions reach an extremely low level. However, when SAN exceeds 15
◦
, soot 
emissions increase rapidly along with the rising SAN. In both combustion modes, when NIP is low, increasing DIP 
can significantly reduce soot emissions. In NMLC mode, the increase of NIP is more effective in enhancing ITE 
and inhibiting soot formation. In NSPC mode, when NIP reaches 30 MPa, the maximum pressure rise rate 
(MPRR) exceeds the limit (1.5 MPa/
◦
CA). When NIP exceeds 30 MPa, ITE begins to decrease. Therefore, NIP 
should be controlled within 30 MPa for NSPC mode.   
1. Introduction 
Under the pressure of global warming, major economies such as the 
Europe Union, Japan, and China have formulated and implemented 
policies to limit carbon dioxide (CO
2
) emissions. Examples of such 
policies stem from the Kyoto protocol [1] and the Paris agreement [2] 
which aim to address these issues by relying less on pollutant releasing 
energy sources thus to reduce the impact on global warming. In addi -
tion, environmental protection regulations have been upgraded to 
further curb pollution emissions [3 – 5] . To this end, researchers are 
constantly working on cleaner energy sources that can be used in in -
ternal combustion engines [6 – 8] . As a low-carbon fuel, natural gas has 
good prospects because of its high H/C ratio, low sulfur content, 
abundant reserves, and low prices [9,10] . 
Due to the relatively low activity of natural gas, the adoption of 
highly reactive diesel to ignite natural gas is an alternative way to utilize 
natural gas in engines [11 – 12] . Several studies have shown that high- 
pressure direct injection (HPDI) natural gas engines can achieve the 
mixture spatial gradient stratification, thus controlling combustion rate 
[13 – 15] . Furthermore, a high natural gas substitution rate can be ach -
ieved under most operating conditions [16 – 18] . For traditional HPDI 
natural gas engines, they were designed to operate at the natural gas 
mixing-limited combustion mode (NMLC), which uses pre-injected 
diesel as the ignition source to ignite main-injected natural gas near 
the top dead center (TDC). However, soot emissions in NMLC mode are 
significantly higher than those in the reactivity controlled compression 
ignition (RCCI) mode due to the higher diffusion combustion ratio 
[19,20] . In the upcoming Euro 7 regulations, their limits on particulate 
matter (PM) and particle number (PN) will be further strengthened 
* Corresponding authors. 
E-mail addresses: cgs_yly@163.com (G. Chen), 893549826@qq.com (F. Wei).  
Contents lists available at ScienceDirect 
Fuel 
journal homepag e: www.else vier.com/loc ate/fuel 
https://doi.org/10.1016/j.fuel.2022.127160 
Received 25 October 2022; Received in revised form 3 December 2022; Accepted 12 December 2022

<!-- PDF_PAGE: 2 -->

Fuel 337 (2023) 127160
2
[21,22] . Therefore, the combustion parameters of HPDI natural gas 
engines need to be further optimized in order to meet the requirements 
of future regulations. 
One of the effective ways to reduce soot emissions is to adopt natural 
gas slightly premixed combustion (NSPC) mode [23] . In NSPC mode, 
diesel injection timing (DIT) begins at the same time as natural gas in -
jection timing (NIT) or after NIT, allowing more premixing of the natural 
gas prior to ignition. Therefore, when the injection interval between 
diesel and natural gas (IDN) is equal to or less than 0
◦
CA, the combustion 
mode switches from NMLC mode to NSPC mode [24,25] . Currently, 
more and more researchers have focused on the application of NSPC 
mode on HPDI natural gas engines. Jin et al. [26] adopted CONVERGE to 
explore the effects of the NIT in NMLC and NSPC modes. They found that 
the mass, quantity, and diameter of the soot produced by the engine with 
the adoption of NMLC mode are larger than those with the adoption of 
NSPC. Zhang et al. [27] evaluated the performance and emissions of a 
pilot ignited direct injection natural gas engine operating in NSPC mode. 
Their results showed that the adoption of NSPC mode at low and me -
dium loads could lead to an increase in nitrogen oxide (NOx) emissions, 
while at medium and high loads, hydrocarbon (HC) emissions surge. 
They also revealed that using NSPC mode could cut down soot emission 
by more than 50 % at all loads. Faghani et al. [28] realized the NSPC 
mode by delaying pilot diesel injection and pointed out that the adop -
tion of NSPC mode can reduce soot emissions considerably at the 
appropriate exhaust gas recirculation (EGR) rate and global oxygen (O
2
) 
based equivalence ratio, without deteriorating NOx and CH
4 
emissions. 
However, although NSPC mode has certain advantages in reducing soot 
emissions, the delayed combustion process leads to difficulty in 
improving thermal efficiency of engines operating in NSPC mode. 
Therefore, it is still necessary to further explore the strategies for ther -
mal efficiency improvement of engines in NSPC mode. 
The combustion chamber types and fuel injection parameters (such 
as spray angle, injection pressure, etc) directly affect the mixing process 
and determine the fuel distribution in the cylinder, thus affecting the 
combustion process and soot formation for engines. However, current 
researches have focused on the effects of key factors such as combustion 
chamber types and injection parameters on the working process of RCCI, 
glow plug ignition, and spark ignition natural gas engines. Combing the 
genetic algorithm NSGA-II with KIVA-3V code, Liu et al. [29] conducted 
multi-objective optimization of combustion chamber types for a diesel/ 
natural gas RCCI engine. Their results showed that the straight-sided 
combustion chamber (SSCC) is effective in reducing methane (CH
4
) 
and improving fuel economy, while NOx emissions are the lowest for the 
reentrant-type combustion chamber. Yadollahi et al. [30] experimen -
tally studied the effects of combustion chamber geometry on engine 
performance in a spark plug ignition direct injection natural gas engine. 
They found that chamber type and nozzle arrangement highly affect 
mixture stratification state and combustion process. The flat piston 
shape causes the flow to be driven to cylinder edges, resulting in a 
narrower angle shape and more stratification. Meanwhile, the large 
bowl combustion chambers show generally similar characteristics as the 
base engine geometry. Kamran et al. [31] researched the effects of diesel 
injection pressure (DIP) and spray angle on engine performance and 
emission characteristics on a diesel/natural gas RCCI light duty engine. 
The results indicated that decreasing DIP in the first injection can in -
crease the gross indicated efficiency and retard the crank angle at 50 % 
of total heat release (CA 50), whereas lowering the diesel spray angle has 
the opposite effect. Pan et al. [32] studied the effects of injection pa -
rameters on flame propagation and combustion characteristics in a glow 
plug assisted direct-injection natural gas engine. They found that the 
high natural gas injection pressure (NIP) can reduce both peak in- 
cylinder pressure (PIP) and emissions in the natural gas engine. And 
the spray angle of natural gas (SAN) can influence natural gas com -
bustion characteristics by affecting the flame propagation out of the 
glow plug shield in the initial combustion stage. Chen et al. [33] carried 
out the effects of diesel injection pressure (DIP) on the combustion and 
emission of diesel/natural gas dual-fuel engines and found that when 
DIP rises, the flame propagation speed of CH
4 
and the ITE increases 
accordingly. Zhang et al. [34] further optimized the combustion 
chamber type in a heavy-duty spark ignition natural gas engine based on 
a combination of experiments and simulations. The results showed that 
by using the higher turbulence combustion chamber in the lean-burn 
spark ignition natural gas engine, the combustion rate dramatically in -
creases, which is conducive to the spark kernel formation and devel -
opment as well as the late turbulence flame propagation throughout the 
combustion chamber. Wang et al. [35] studied the effects of natural gas 
spray direction and position and NIP based on a multi-point injection 
spark ignition natural gas engine. Their results found that the natural gas 
spray direction perpendicular to the incoming air can enhance the 
disturbance effect, and the natural gas spray position far from the valve 
can increase the uniformity of the mixing of the intake. Moreover, when 
NIP was added to 736.63 kPa, the injection kinetic energy can be 
increased and emission characteristics can be improved. 
In conclusion, the combustion chamber types and injection 
Abbreviations 
NMLC natural gas mixture-limited combustion 
NSPC natural gas slightly premixed combustion 
SAN spray angle of natural gas 
DIP diesel injection pressure 
NIP natural gas injection pressure 
SSCC straight-sided combustion chamber 
ITE indicated thermal efficiency 
A
4 
pyrene 
C
2
H
2 
acetylene 
MPRR maximum pressure rise rate 
CO
2 
carbon dioxide 
HPDI high-pressure direct injection 
TDC top dead center 
RCCI reactivity controlled compression ignition 
PM particulate matter 
PN particle number 
DIT diesel injection timing 
NIT natural gas injection timing 
IDN injection interval between diesel and natural gas 
NOx nitrogen oxides 
HC hydrocarbon 
EGR exhaust gas recirculation 
O
2 
Oxygen 
CH
4 
methane 
CA 50 the crank angle at 50 % of total heat release 
PIP peak in-cylinder pressure 
CFD computational fluid dynamics 
LES Large Eddy Simulations 
KH Kelvin-Helmholtz 
RT Rayleigh-Taylor 
AMR adaptive mesh refinement 
HRR heat release rate 
BCC bow combustion chamber 
DCC deepened combustion chamber 
PHRR peak heat release rate 
CA crank angle 
ATDC after top dead center  
G. Chen et al.

<!-- PDF_PAGE: 3 -->

Fuel 337 (2023) 127160
3
parameters can significantly improve the performance of RCCI, glow 
plug ignition and spark ignition natural gas engines. However, in recent 
years, there are few studies on the effects of combustion chamber types 
and injection parameters on the working process and soot formation of a 
diesel/natural gas double direct injection engine. At the same time, for 
different combustion modes, there is still a lack of cooperative matching 
optimization research on combustion chamber types and injection pa -
rameters. Such research would contribute a lot to improving the 
comprehensive performance of natural gas engines and reducing soot 
emissions. 
As described above, the study ’ s overall objective is to assess the 
potential of combustion chamber type, SAN, DIP, and NIP to achieve 
high thermal efficiency and low soot emissions in NMLC and NSPC 
modes. First, a computational fluid dynamics (CFD) numerical model 
coupled with a reaction kinetic mechanism was constructed. Based on 
the numerical simulation model, the effects of combustion chamber type 
on the combustion process and soot emission characteristics for a diesel/ 
natural gas double direct injection engine were studied at macro and 
micro levels in different combustion modes. Then, the SAN, DIP and NIP 
were optimized and matched based on the optimized combustion 
chamber type. These studies will provide a theoretical basis and prac -
tical guidance for natural gas direct injection engines to achieve high 
thermal efficiency and meet the PM/PN limits of future stringent 
emission regulations such as Euro 7. 
2. Numerical model establishment and validation 
2.1. Numerical model 
Computations were performed using the Converge 3.0 code. The test 
engine was a six-cylinder four-stroke Cummins ISX 400 engine [36,37] . 
The main engine specifications of the engine are shown in Table 1 , and 
the operating conditions are shown in Table 2 . 
Since the seven diesel injection holes and seven natural gas injection 
holes are evenly distributed in the combustion chamber, an axisym -
metric model of the cycle boundary was constructed by selecting 1/7 of 
the single cylinder volume to ease the computational burden. The diesel 
nozzle is parallel to the natural gas nozzle, and the angle between the 
nozzle and the horizontal plane is 10
◦
. Fig. 1 illustrates the schematic of 
1/7 engine sector domain. Moreover, to simulate the natural gas injec -
tion process, a liquid/gas dual direct injection model was constructed 
and the boundary conditions of the gas side were set at the nozzle inlet to 
control the mass flow [38] . 
In this work, the simulations were performed by the Eulerian- 
Lagrangian coupling approach and the dispersed phase was modeled 
in a Lagrangian framework by following the trajectories of computa -
tional particles. The Large Eddy Simulations (LES) Smagorinsky turbu -
lence model [39] was applied to study the flow characteristics in the 
cylinder. The liquid atomization and breakup were simulated using the 
Kelvin-Helmholtz/Rayleigh-Taylor (KH-RT) breakup model [40,41] , 
with the primary and secondary breakup processes governed by the KH 
and RT mechanisms, respectively. The KH mechanism assumes that the 
initial growth of perturbation on the droplet surface results in the 
stripping of small droplets, whereas the RT mechanism is driven by the 
disturbance wave generated by density variation along normal di -
rections of the liquid – gas surface. A modified heat transfer model pro -
posed by Han and Reitz [42] was used to model heat transfer. The 
evaporation model was based on the Frossling correlation, which cal -
culates the time gradient of droplet radius based on the laminar mass 
diffusivity of the fuel vapor, the mass transfer number, and the Sher -
wood number. The SAGE model [43] combined with a reaction kinetic 
mechanism [44] was chosen to describe the combustion process in the 
cylinder. The model calculates the reaction rates of each elementary 
reaction by Arrhenius-type correlation, and the transport equations are 
solved by the CFD solver correspondingly. The simplified mechanism 
contains 143 species and 746 individual reaction equations. For the 
conducted CFD calculation, a mixture of n -heptane and n -butylbenzene 
was used to simulate the chemical properties of diesel, and n -tetrade -
cane was used to simulate the physical properties of diesel. Meanwhile, 
the natural gas consisted of a mixture of methane, ethane and, propane. 
A phenomenological soot model - Gokul model [45] , which uses A4 as its 
inception species, was used for soot prediction. 
In the simulation process, the grid scale inevitably has an impact on 
the calculation results, thus a grid dependence analysis should be carried 
out first. Based on the grid independence analysis [46] , a base grid size 
of 2 mm was employed, and an adaptive mesh refinement (AMR) size of 
0.5 mm was applied in regions with high velocity and temperature 
gradients. To improve the accuracy of the simulation, a fixed embedding 
was added near the inflow region and diesel nozzle. For other bound -
aries around the combustion chamber, the mesh was refined to half of 
the base grid size to prevent losing details of the geometry. A variable 
time step from a minimum time step of 0.01 μ s to a maximum time step 
of 100 μ s was used in the calculation. 
The model validation was based on experimental data from Faghani 
[36] who conducted the experiments on a single-cylinder HPDI natural 
gas engine. The model validation has been completed in our previous 
study [46] , so only the key results were discussed in this paper. Fig. 2 a 
illustrates a comparison between the experimental [36] and simulation 
results of the in-cylinder pressure and heat release rate (HRR) profiles at 
an EGR rate of 18 %. As can be seen, the model could reasonably 
reproduce the experimental results. Fig. 2 b illustrates comparisons of 
Table 1 
Main specifications of the Cummins ISX engine.  
Parameters Values 
Cylinder number 6 
Cycle 4-stroke 
Cylinder bore (mm) 137 
Stroke (mm) 169 
Connecting rod length (mm) 262 
Compression ratio 17 
Swirl ratio 1.5 
Displacement (L) 2.5 
Intake valve closing time (
◦
CA ATDC)  90 
Exhaust valve opening time (
◦
CA ATDC) 140  
Table 2 
Main operating points of the Cummins ISX engine.  
Parameters Values 
Engine speed rpm 1500 
Diesel injection pressure (MPa) 27 
Pilot diesel mass (mg) 11.0 
DIT (
◦
CA ATDC)  17 
Diesel pulse width (
◦
CA) 7.56 
Natural gas injection pressure (MPa) 25 
Natural gas mass (mg) 173.7 
NIT (
◦
CA ATDC)  8 
Natural gas pulse width (
◦
CA) 21.51 
EGR rate (%) 0, 18, 24  
Fig. 1. Schematic of 1/7 engine sector domain.  
G. Chen et al.

<!-- PDF_PAGE: 4 -->

Fuel 337 (2023) 127160
4
the experimental [36] and simulation results of NOx, CO, and soot 
emissions at different EGR rates. The trends of NOx, CO, and soot 
emissions in the simulation were consistent with the experimental re -
sults, with most of the prediction errors was kept within 20 %, which 
was reasonable for simulations of emissions. 
2.2. Cases setup 
After validation, a set of cases were designed to evaluate the effects 
of the IDN on combustion, ITE, and soot emissions in NMLC and NSPC 
modes. Fig. 3 shows a schematic diagram of the different combustion 
modes. Notably, in NSPC mode, diesel is usually injected after or 
simultaneously with the natural gas injection. Table 3 presents the 
simulation cases for DIT, NIT, and IDN in NMLC and NSPC modes. 
In this work, to investigate the effects of combustion chamber type 
on engine performance and soot emissions in different combustion 
modes, four types of combustion chamber were discussed, including 
chambers with bow combustion chamber (BCC), SSCC and deepened 
combustion chamber (DCC). Particularly, DCC is designed by reducing 
squish height, and squish heights for SSCC, TCC and BCC remain the 
same for each profile. The compression ratio remained consistent with 
the original engine for all types of combustion chambers to eliminate the 
effects of compression ratios on combustion and emissions. The detailed 
parameters of four types of combustion chambers are shown in Fig. 4 . 
The definition of SAN is shown in Fig. 5 . The variation of SAN was 
achieved mainly by varying the angle between the central axis of the 
natural gas jet and the horizontal direction, while the position of the 
diesel injection hole remained unchanged. It is worth noting that when 
SAN is too small, the jet tends to produce the Coanda Effect [47] 
(Coanda Effect: the fluid will attach to the surface due to surface friction 
Fig. 2. Validation of cylinder pressure, HRR, and emissions in the three- 
dimensional model at different EGR rates [46] . 
Fig. 3. Schematics of different combustion modes.  
Table 3 
Simulation cases for DIT, NIT, and IDN in NMLC and NSPC modes.  
DIT (
◦
CA ATDC) NIT(
◦
CA ATDC) IDN (
◦
CA) Combustion modes 
 25  8 17 NMLC 
 21  8 13 NMLC 
 17  8 9 NMLC 
 13  8 5 NMLC 
 8  8 0 NSPC 
 6  8  2 NSPC 
 4  8 4 NSPC  
G. Chen et al.

<!-- PDF_PAGE: 5 -->

Fuel 337 (2023) 127160
5
between the fluid and the surface of the object, resulting in a reduction 
in fluid momentum); when SAN is too large, the jet tends to form fuel 
accumulation at the bowl bottom. Therefore, SAN was studied in the 
ranges of 10
◦
, 15
◦
, 18
◦
and 20
◦
. 
Simulation cases for DIP and NIP in NMLC and NSPC modes are 
shown in Table 4 . It is worth noting that in the experiments, DIP was 
higher than NIP by more than 1 MPa in order to prevent natural gas from 
entering the diesel line due to the adoption of the coaxial dual injection 
technology. Therefore, DIP was kept higher than NIP by more than 1 
MPa in the calculation. 
In all cases, the engine speed was kept at 1500 r/min and the EGR 
rate was fixed at 18 %. The total energy of the natural gas and diesel 
supplied were 9245 J/cycle, which characterized the 75 % engine load. 
3. Results and discussions 
3.1. Effects of IDN on combustion and soot emissions in different 
combustion modes 
In this section, for different combustion modes, the BCC was selected 
as the basic combustion chamber in which the SAN was kept at 10
◦
, the 
DIP and NIP were fixed at 27 MPa and 25 MPa, respectively, and the NIT 
was retained at  8
◦
CA ATDC . To facilitate the analysis of the combus -
tion mode transition, the phase during which IDN decreases from 5
◦
CA 
to 0
◦
CA was defined as a transition phase. Notably, the transition phase 
still belongs to NMLC mode. 
Fig. 6 shows the effects of IDN on cylinder pressure and HRR in 
NMLC and NSPC modes [46] . Compared with NSPC mode, the peak heat 
release rates (PHRR) are generally lower and combustion duration is 
longer for different IDNs in NMLC mode. Moreover, the effects of IDN on 
PIP, PHRR, and the appearance moments of PIP and PHRR are not 
prominent. While in NSPC mode, the combustion phases are relatively 
lagged and the heat releases of the fuel are more concentrated in 
different IDNs. The above phenomenon can be attributed to the mixing 
quality of fuel and air. In NSPC mode, a complex interaction forms be -
tween the natural gas and diesel jets, which prolongs the low- 
temperature oxidation and leads to a long diesel ignition delay. Conse -
quently, the injected natural gas into the cylinder mixes well with air, 
forming a better stratification state in the cylinder. However, adopting 
an excessively decreased IDN is not appropriate in the NSPC mode. This 
is because when IDN excessively decreases, the combustion phase is 
greatly delayed, resulting in the fact that most of the fuel mixture cannot 
reach the stoichiometric ratio, which is not conducive to enhancing 
combustion intensity. 
Fig. 7 shows the effects of IDN on ITE and soot emissions in NMLC 
and NSPC modes [46] . In NMLC mode, the variation of IDN has a limited 
impact on improving soot emissions, and the ITE can be slightly 
enhanced by adopting larger IDNs (17
◦
CA, 13
◦
CA). For example, 
compared with an IDN of 9
◦
CA, ITE increases by 1.37 % and 1.42 % at 
Fig. 4. Detailed parameters of four combustion chamber types.  
Fig. 5. The definition of SAN.  
Table 4 
Simulation cases for DIP and NIP in NMLC and NSPC modes.  
Combustion chamber DIP(MPa) NIP(MPa) Combustion modes 
SSCC 27 20 NMLC, NSPC 
SSCC 27 25 NMLC, NSPC 
SSCC 37 20 NMLC, NSPC 
SSCC 37 25 NMLC, NSPC 
SSCC 37 30 NMLC, NSPC 
SSCC 37 35 NMLC, NSPC  
G. Chen et al.

<!-- PDF_PAGE: 6 -->

Fuel 337 (2023) 127160
6
IDNs of 17
◦
CA and 13
◦
CA, respectively. This might be due to that in 
NMLC mode, the intervention by natural gas in diesel combustion 
gradually increases with decreasing IDN. Subsequently, the intensified 
competition for O
2 
between the two fuels resulted in the formation of 
more local lean-O
2 
regions, limiting the spread of flame. As a result, the 
PHRRs are low and far from the TDC at IDNs of 9
◦
CA and 5
◦
CA, which is 
not favorable for enhancing ITE. The adoption of the NSPC mode is 
beneficial to reduce soot emissions. In general, as the IDN reduces 
continuously, the soot emissions decrease accordingly. Especially, 
compared with an IDN of 9
◦
CA, an IDN of  4
◦
CA creates favorable 
conditions for soot reduction which could be up to 95.5 %. This is 
because the ignition delay of natural gas significantly prolongs with 
decreasing IDN, thereby improving the homogeneity of the mixture 
distribution and inhibiting the soot formation. However, due to the lag 
of the combustion phase, it is difficult to further enhance ITE in NSPC 
mode. Therefore, the next work was conducted to evaluate the potential 
for efficient and clean combustion of engines in both combustion modes 
by further adjusting the combustion system parameters. 
Fig. 6. Effects of IDN on cylinder pressure and HRR in NMLC and NSPC modes [46] .  
Fig. 7. Effects of IDN on ITE and soot emissions in NMLC and NSPC modes [46] .  
G. Chen et al.

<!-- PDF_PAGE: 7 -->

Fuel 337 (2023) 127160
7
3.2. Effects of combustion chamber type on combustion and soot 
emissions in different combustion modes 
When studying the effects of combustion chamber type, SAN, DIP, 
and NIP, the point where DIT reaches  17
◦
CA ATDC and NIT reaches 
 8
◦
CA ATDC was selected as an operating point in NMLC mode. In 
addition, the point where DIT reaches  6
◦
CA ATDC and NIT reaches 
 8
◦
CA ATDC was selected as an operating point in NSPC mode. In this 
section, the effects of combustion chamber type were studied in different 
combustion modes. For different combustion modes, the SAN was kept 
at 10
◦
, while the DIP and NIP were fixed at 27 MPa and 25 MPa, 
respectively. 
Fig. 8 shows the effects of combustion chamber type on local 
equivalence ratio and flow field distribution in NMLC and NSPC modes. 
The development of gas jets is mainly divided into three stages: free jet 
development, the jet impinging on the wall and the jet development 
along the wall [48] . As shown in Fig. 8 , the high-speed jet from the hole 
goes through the free development stage and hits the lip of the com -
bustion chamber. Subsequently, one part of the natural gas jet flows into 
the bowl bottom and the other part goes upwards into the squish region. 
As the fuel continues to travel downward, a large-scale vortex structure 
with strong air winding ability is gradually formed through the combi -
nation of jet momentum, air resistance, and reversed squish flow. Af -
terwards, the proportion of the combustible mixture normally increases 
rapidly after the vortex structure enters the growth and torsion stages 
[49] . 
In NMLC mode, for BCC and TCC, more fuel travels toward the squish 
region after the jet strikes the throat and gradually forms a fuel accu -
mulation in the squish region. In contrast, for SSCC, most of the fuel 
travels toward to the bowl bottom. Therefore, for SSCC, the vortex 
structure formed at the bowl bottom is slightly larger than that for BCC 
and TCC. In addition, for DCC, reducing the height of the squish region 
at constant compression ratio leads to an increase in the depth of the 
combustion chamber, resulting in a lower average turbulence energy, 
which is not conducive to vortex structure formation. Consequently, 
when the crank angle (CA) reaches 16
◦
CA ATDC, no vortex structure is 
formed and a large accumulation of concentrated mixture is observed in 
the squish region with the adoption of DCC. 
In NSPC mode, the momentum of the natural gas jet reduces before 
hitting the wall due to the complex interaction between the two jets. 
Fig. 8. Effects of combustion chamber type on local equivalence ratio and flow field distribution in NMLC and NSPC modes.  
G. Chen et al.

<!-- PDF_PAGE: 8 -->

Fuel 337 (2023) 127160
8
Thus, the proportion of fuel entering the bowl bottom in NSPC mode 
increases compared to that in NMLC mode, which facilitates the devel -
opment of subsequent large-scale vortex structures. Therefore, when the 
crank angle reaches 16
◦
CA ATDC, the vortex structures in the BCC, 
SSCC, and TCC all show a tendency to move away from the bottom and 
gradually travel toward the center of the combustion chamber. In 
addition, the area of the in-cylinder concentrated mixture region in 
NSPC mode is significantly smaller than that in NMLC mode, especially 
near the injection holes. This is mainly due to the fact that combustion 
and mixing occur simultaneously in NMLC mode. As the flame propa -
gates, it continuously consumes the surrounding O
2
, which limits further 
mixing of fuel and air. Consequently, the in-cylinder concentrated 
mixture increases. In contrast, in NSPC mode, the lagging ignition delay 
together with the twisting and growing of the large-scale vortex struc -
ture promotes the homogenization of the mixture. It is worth noting that 
when the crank angle reaches 16
◦
CA ATDC, there is still a small portion 
of the concentrated mixture in the squish region of BCC, TCC, and DCC, 
while in SSCC, part of the mixture exists near the throat but does not 
progress to the squish region. 
Fig. 9 shows the effects of combustion chamber type on cylinder 
pressure and HRR in NMLC and NSPC modes. In NMLC mode, the dif -
ferences in PIP and PHRR are not obvious in terms of the three com -
bustion chamber types (SSCC, BCC, and TCC). It is worth noting that PIP 
and PHRR reach the lowest for DCC. Meanwhile, the cylinder pressure 
profile in the middle and late phases of combustion is significantly lower 
than that for the rest three combustion chambers, which means that the 
engine ’ s working capacity reduces after adopting DCC. This is mainly 
due to the fact that the squish region, where a larger proportion of the 
fuel is concentrated, restricts the propagation of the subsequent diffu -
sion flame with its low temperature and weak mobility. In addition, in 
the squish region, there is a high probability of incomplete combustion 
of the fuel. To this end, the PIP and PHRR are the lowest, and the en -
gine ’ s work capacity reduces with the adoption of DCC. 
It is also can be seen from Fig. 9 that the combustion chamber types 
greatly affect combustion parameters such as PIP, PHRR, and combus -
tion phase in NSPC mode. Compared with the adoption of BCC, the 
adoption of SSCC, TCC and DCC is all beneficial to increase the flame 
propagation speed. Among them, the adoption of SSCC creates the most 
favorable condition in which flame propagation speed is the fastest, PIP 
is the highest, and PIP appears earlier. This can be attributed to the fact 
that the mixture of natural gas and air that close to the stoichiometric 
ratio increases for SSCC. As shown in Fig. 10 , after the crank angle 
reaches 4
◦
CAATDC, the mixture close to the stoichiometric ratio grad -
ually increases in SSCC and is most pronounced at the crank angle of 
16
◦
CAATDC. As a result, the rapid flame propagation is facilitated. In 
can be concluded that, in NSPC mode, adopting SSCC plays a vital part in 
improving combustion intensity. 
Fig. 11 shows the effects of combustion chamber type on the MPRR 
and ITE in NMLC and NSPC modes. In NMLC mode, the over- 
concentrated mixture for SSCC reduces compared to that for BCC, 
which means that the uniformity of the mixture increases relatively. As a 
result, ITE slightly improves. In addition, ITE is the lowest for DCC due 
to the reduction of the engine ’ s work capacity. It can also be seen in 
Fig. 11 that MPRR does not vary much and is controlled at a low level in 
all four combustion chambers. Compared with NMLC mode, NSPC mode 
helps to promote flame propagation and thus leads to a higher MPRR 
because a large amount of homogeneous mixture burns simultaneously 
in this mode. At the same time, the relatively concentrated heat release 
further shortens the combustion duration and reduces the heat transfer 
loss in the late stage of combustion, which results in a significant in -
crease in ITE. Moreover, in NSPC mode, ITE is relatively high for SSCC 
and TCC while it reaches the lowest for DCC. Compared with DCC, ITE 
increases by 4.2 % and 6.9 % respectively for BCC and SSCC. 
Fig. 12 shows the effects of combustion chamber type on soot 
emissions in NMLC and NSPC modes. In NMLC mode, compared with 
BCC, soot emissions reduce by 27.7 % and 66.5 % respectively by 
adopting TCC and SSCC, while the soot emission increases by 172.5 % 
for DCC. Moreover, in NSPC mode, soot emissions are kept low for 
different combustion chambers. Among all the combustion chambers, 
SSCC presents the lowest soot emission which reduces by 96 % 
compared to that for BCC. The above phenomena can be explained by 
Fig. 13 and Fig. 14 . 
Fig. 13 shows the effects of combustion chamber type on mean 
temperature and soot formation process in NMLC and NSPC modes. In 
NMLC mode, the peak values of soot formation for different cases are 
higher than those in NSPC mode. In addition, compared with BCC, TCC 
Fig. 9. Effects of combustion chamber type on cylinder pressure and HRR in NMLC and NSPC modes.  
G. Chen et al.

<!-- PDF_PAGE: 9 -->

Fuel 337 (2023) 127160
9
and DCC, SSCC presents a lower peak value of soot formation and faster 
oxidation rate, thus resulting in a significant reduction in the final soot 
emission. This is mainly due to the fact that the lack of fuel accumulation 
in the squish region of the SSCC ( Fig. 14 ) inhibits soot formation 
considerably. Meanwhile, higher PIP and PHRR lead to higher com -
bustion temperature ( Fig. 13 a), which promotes the oxidation of soot. In 
contrast, for BCC, TCC, and DCC, there are different areas of high soot 
concentration in the squish region. Among them, the fuel accumulation 
phenomenon is more obvious for DCC and the final soot emission is the 
highest. Therefore, in NMLC mode, soot emissions are controlled mainly 
by adjusting the mixture distribution and reducing the fuel that flows to 
the squish region. It could also be concluded that in NSPC mode, the 
longer ignition delay further inhibits the formation of soot, leading to 
the in-cylinder soot distribution reduction. By comparing with other 
combustion chambers, it can be seen that the peak value of soot 
Fig. 10. Effects of combustion chamber type on the equivalence ratio mass fraction in the NSPC mode.  
Fig. 11. Effects of combustion chamber type on MPRR and ITE in NMLC and 
NSPC modes. 
Fig. 12. Effects of combustion chamber types on soot emissions in NMLC and 
NSPC modes. 
G. Chen et al.

<!-- PDF_PAGE: 10 -->

Fuel 337 (2023) 127160
10
Fig. 13. Effects of combustion chamber type on mean temperature and soot formation process in NMLC and NSPC modes.  
Fig. 14. Effects of combustion chamber type on the distribution of soot mass fraction in NMLC and NSPC modes.  
Fig. 15. Effects of SAN on local equivalence ratio and flow field distribution in NMLC and NSPC modes.  
G. Chen et al.

<!-- PDF_PAGE: 11 -->

Fuel 337 (2023) 127160
11
formation and final soot emission for SSCC are the lowest. This is 
because a rational equivalence ratio distribution for SSCC promotes 
flame propagation, increasing the proportion of the fuel involved in 
combustion in the early stage, which leads to a higher mean temperature 
in the cylinder. Afterwards, the soot oxidation is promoted. 
In summary, in NMLC mode, the combustion processes of BCC, TCC 
and SSCC do not differ significantly and the mixture distribution is the 
main factor affecting ITE and soot emissions. Among them, relatively 
high ITE and low soot emission can be obtained after adopting SSCC. In 
addition, the engine ’ s work capacity decreases after adopting DCC, 
which adversely affects both ITE and soot emission. Therefore, SSCC is 
the best solution in NMLC mode. In NSPC mode, combustion chamber 
types have a great influence on the combustion process in the cylinder. 
Higher PIP and PHRR can be obtained by adopting SSCC, and high ITE 
can be maintained under the condition of meeting the MPRR limit [46] , 
while the adoption of BCC and TCC is not advantageous in terms of ITE. 
In addition, among all combustion chamber types, SSCC produces the 
lowest soot emissions. Therefore, SSCC is the best solution in NSPC 
mode. 
3.3. Effects of SAN on combustion and soot emissions in different 
combustion modes 
In this section, the effects of SAN were studied in different combus -
tion modes. For different combustion modes, the SSCC was selected as 
the basic combustion chamber in which the DIP and NIP were fixed at 
27 MPa and 25 MPa, respectively. In SSCC, when SAN reached 10
◦
, this 
case was noted as S-10, and so on for other cases. 
Fig. 15 shows the effects of SAN on local equivalence ratio and flow 
field distribution in NMLC and NSPC modes. In NMLC mode, as the jet 
impingement position keeps moving below the throat with rising SAN, 
the momentum of the bottom jet keeps increasing, promoting the 
development of the vortex structure at the bowl bottom. At SANs of 10
◦
and 15
◦
, the vortex structures have not yet traveled out of the bottom 
when the crank angle reaches 16
◦
CA ATDC. And at SANs of 18
◦
and 20
◦
, 
the bottom vortex structures grow stronger and gradually develop to -
ward the center of the combustion chamber when the crank angle rea -
ches 16
◦
CA ATDC. Meanwhile, part of the fuel hits the wall and climbs 
upward, forming a small vortex structure above the throat, which pro -
motes the mixing process above the throat. It can also be concluded from 
Fig. 15 that at a SAN of 15
◦
, fuel accumulation is more easily observed at 
the bowl bottom under the effects of jet momentum. And at SANs of 18
◦
and 20
◦
, more combustible mixture is formed in the cylinder. 
In NSPC mode, the proportion of combustible mixture formed in the 
center of the combustion chamber goes up with increasing SAN, and the 
fuel accumulation phenomenon at the bottom becomes more prominent. 
This is mainly because the momentum of the natural gas jet in NSPC 
mode is lower than that in NMLC mode, thus a large amount of fuel 
enters the bottom when SAN increases. However, the formation of a 
vortex structure at the bottom is insufficient to drive a large amount of 
aggregated fuel to participate in mixing in a short time. Therefore, the 
distribution of the mixture NSPC mode is more sensitive to the variation 
of SAN. 
Fig. 16 shows the effects of SAN on cylinder pressure and HRR in 
NMLC and NSPC modes. In NMLC mode, PIP and PHRR reach the lowest 
at a SAN of 15
◦
. This is mainly due to the lower momentum of the 
natural gas jet limits the growth and distortion of the vortex structure, 
resulting in a slower flame propagation at the bottom. Meanwhile, a 
medium temperature region is formed at the bottom ( Fig. 17 ). In addi -
tion, the flame propagation is further accelerated by the formation of a 
large amount of combustible mixture in the center of the combustion 
chamber at larger SANs (18
◦
and 20
◦
), producing higher PIP, PHRR and 
earlier appearances of PIP and PHRR. 
In NSPC mode, PIP is the highest and the HRR profile rises the fastest 
at a SAN of 10
◦
. This is mainly attributed to the fact that the increase in 
the uniformity of the mixture distribution in the combustion chamber at 
a SAN of 10
◦
reduces the regions with a high equivalence ratio, and 
therefore the flame propagation speed is significantly higher. It is worth 
noting that at a SAN of 18
◦
, the diesel ignition core forms later, implying 
that the natural gas jet has a greater effect on the diesel ignition core 
( Fig. 17 ). Therefore, when SAN is 18
◦
, the ignition delay of natural gas is 
substantially prolonged and the main combustion process is delayed. 
However, although the degree of fuel premixing increases at a SAN of 
18
◦
, the equivalence ratio of the partially premixed gas in the cylinder 
before the start of combustion is already less than the stoichiometric 
ratio. As a result, flame propagation is hindered and PHRR decreases. 
When SAN is 20
◦
, on the one hand, the formation of a large amount of 
premixed gas in the center of the combustion chamber promotes the 
premixed combustion process, which leads to a higher PHRR; on the 
other hand, the large accumulation of fuel at the bottom leads to a lower 
after-burning ratio during the expansion stroke and reduces the engine ’ s 
working capacity. 
Fig. 18 shows the effects of SAN on MPRR and ITE in NMLC and 
NSPC modes. In NMLC mode, MPRR and ITE are relatively high when 
SANs are 18
◦
and 20
◦
, which is attributed to faster flame propagation 
and higher PHRR. The ITE reaches its highest (43.4 %) at a SAN of 18
◦
, 
which is 3.4 % higher than that at a SAN of 10
◦
. In addition, it can be 
seen from Fig. 18 that ITE is the lowest at a SAN of 15
◦
, which decreases 
by 2 % compared to that at a SAN of 10
◦
. This is mainly due to the 
presence of a high equivalence ratio region at the bottom, where O
2 
utilization is inefficient and flame propagation is hindered, results in a 
significantly lower after-burning ratio, implying more possibility of 
incomplete combustion. In contrast to NMLC mode, the adoption of a 
larger SAN is not conducive to enhancing ITE in NSPC mode due to the 
limitations of the mixing process. Notably, a proper reduction of SAN 
can significantly improve the ITE in NSPC mode. For example, ITE in -
creases by 5.1 % at a SAN of 10
◦
and by 5.2 % at a SAN of 15
◦
compared 
to that at a SAN of 20
◦
. In addition, due to the increased intensity of 
combustion, a smaller SAN also leads to an increase in MPRR. 
Fig. 19 shows the effects of SAN on soot emissions in NMLC and 
NSPC modes. In NMLC mode, soot emissions first reduce and then rise as 
SAN increases. Meanwhile, the soot emissions reach a minimum at a 
SAN of 18
◦
. In addition, when SAN is 18
◦
, the soot emission decreases by 
54.7 % compared to that at a SAN of 10
◦
. In NSPC mode, soot emissions 
are more sensitive to a large SAN. When SAN is above 15
◦
, soot emis -
sions rise rapidly with increasing SAN. When SAN increases to 20
◦
, the 
soot emissions reach 0.0193 g/kW ⋅ h. 
The variation of soot emissions shown in Fig. 19 can be explained by 
the soot particle formation and oxidation processes. Soot particle for -
mation and oxidation are local phenomena that are affected by the 
Fig. 16. Effects of SAN on cylinder pressure and HRR in NMLC and 
NSPC modes. 
G. Chen et al.

<!-- PDF_PAGE: 12 -->

Fuel 337 (2023) 127160
12
temporal and spatial thermodynamic and chemical state of the fuel/air 
mixture distribution [50] . Therefore, the localized quantitative analysis 
of temperature, equivalence ratio, pyrene (A
4
), and acetylene (C
2
H
2
) 
was required to be performed to provide a comprehensive understand -
ing of soot evolution. 
Fig. 20 shows the effects of SAN on the formation processes of soot, 
A
4 
and C
2
H
2 
in NMLC and NSPC modes. In NMLC mode, the peak values 
of A
4
, C
2
H
2 
and soot formation are the highest at a SAN of 15
◦
. While at 
SANs of 18
◦
and 20
◦
, lower peak values of A
4 
and C
2
H
2 
formation can be 
observed. This can be be explained by the effects of SAN on cell data of 
soot mass fraction, as can be seen in Fig. 21 . The high concentrations of 
soot usually occur in the 1.0 – 2.0 equivalence ratio range at SANs of 18
◦
and 20
◦
, while at a SAN of 15
◦
, the high concentrations of soot usually 
occur in the 1.0 – 2.4 equivalence ratio range. Thus, in the lean-O
2 
region, 
more hydrocarbon molecules are cleaved to produce unsaturated 
hydrocarbons and aromatics. Finally, the rising peak values of A
4 
and 
C
2
H
2 
formation intensify the initial nucleation and surface growth re -
actions of soot particles, bringing about more soot emissions. However, 
as the piston moves down, the accumulated fuel at the bottom gradually 
mixes with air to form the equivalence ratio suitable for combustion, so 
the after-burning temperature goes up at a SAN of 15
◦
( Fig. 22 ) and the 
soot oxidation rate rises accordingly. Eventually, the soot emissions are 
slightly lower at a SAN of 15
◦
compared to that at a SAN of 10
◦
. At SANs 
of 18
◦
and 20
◦
, the peak values of A
4 
and C
2
H
2 
formation are lower due 
to the faster premixed flame propagation and earlier appearances of PIP 
and PHRR. However, when SAN is 20
◦
, the cylinder temperature is 
relatively low in the late stage of combustion, thus the soot oxidation 
declines substantially. Consequently, the soot emission escalates when 
SAN increases from 18
◦
to 20
◦
. 
Fig. 17. Effects of SAN on temperature distribution in NMLC and NSPC modes.  
Fig. 18. Effects of SAN on MPRR and ITE in NMLC and NSPC modes.  
Fig. 19. Effects of SAN on soot emissions in NMLC and NSPC modes.  
G. Chen et al.

<!-- PDF_PAGE: 13 -->

Fuel 337 (2023) 127160
13
In NSPC mode, at SANs of 10
◦
and 15
◦
, data show that the peak 
values of A
4 
and C
2
H
2 
formation decrease, the reaction duration of A
4 
and C
2
H
2 
is relatively short, and the corresponding soot formation de -
creases. Two factors contributed to this. On the one hand, at SANs of 10
◦
and 15
◦
, the concentrated combustion leads to a shorter retention time 
of the fuel in the high-temperature combustion atmosphere, so the for -
mation of initial soot particles and the surface growth reaction are 
weakened. On the other hand, the uniformity of mixture distribution is 
elevated, which inhibits high-temperature fuel cracking and dehydro -
genation reactions. It is worth noting that, at a SAN of 18
◦
, due to the 
delayed combustion stage, the mixture homogeneity is substantially 
improved and the soot formation reduces accordingly. However, the 
excessively delayed back combustion phase leads to a lower mean in- 
cylinder temperature ( Fig. 22 ), therefore soot oxidation rate is lower 
at the late combustion stage, which brings about higher final soot 
emission at a SAN of 18
◦
. And when SAN is 20
◦
, the peak values of A
4 
and C
2
H
2 
formation rise substantially. In addition, as seen in Fig. 21 , the 
distribution of high soot concentrations in the high equivalence ratio 
regions increases heavily at a SAN of 20
◦
compared to those at SANs of 
10
◦
and 15
◦
due to the presence of fuel accumulation at the bottom. 
Meanwhile, due to the lower in-cylinder temperature in the late com -
bustion stage, the soot oxidation rate decreases, resulting in a substantial 
increase in the final soot emission when SAN rises to 20
◦
. 
In summary, in NMLC mode, it is when SAN is 18
◦
that the fuel 
Fig. 20. Effects of SAN on the formation processes of soot, A
4 
and C
2
H
2 
in NMLC and NSPC modes.  
Fig. 21. Effects of SAN on cell data of soot mass fraction in NMLC and NSPC modes when crank angle is 30
◦
CA ATDC.  
G. Chen et al.

<!-- PDF_PAGE: 14 -->

Fuel 337 (2023) 127160
14
stratification state reaches its best, ITE can be raised to 43.4 %, and the 
soot emission can be reduced to its minimum. In NSPC mode, it is when 
SAN is 15
◦
, the combustion intensity reaches its highest, ITE can be 
increased to 44.7 % while soot emission was limited to an extremely low 
level. 
3.4. Effects of DIP and NIP on combustion and soot emissions in different 
combustion modes 
In this section, the effects of DIP and NIP were studied in different 
combustion modes. For different combustion modes, the SSCC was 
selected as the basic combustion chamber in which the DIP and NIP were 
fixed at 27 MPa and 25 MPa, respectively. In SSCC, when DIP reached 
27 MPa and NIP reached 20 MPa, this case was noted as S-27 – 20, and so 
on for other cases. 
Fig. 23 shows the effects of DIP and NIP on equivalence ratio and 
flow field distribution in NMLC and NSPC modes. In NMLC mode, since 
the diesel substitution rate is low, the variation of DIP has little impact 
on the in-cylinder mixture distribution, while the impact of NIP on the 
mixture gradient distribution is significant. As NIP increases, the outlet 
pressure of the natural gas hole increases, leading to a larger momentum 
of the natural gas jet. Such momentum can not only drives the in- 
cylinder airflow movement and accelerates the mixing of fuel and air 
but also facilitates the natural gas jet to hit the combustion chamber wall 
earlier, promoting the spatial distribution of the mixture. At NIPs of 30 
MPa and 35 MPa, when the crank angle reaches 16
◦
CA ATDC, the large 
scale vortex structures that gradually spread to the center of the com -
bustion chamber are observed, along with a large area of homogeneous 
mixture in the bottom and center regions. However, as the momentum of 
the jet increases, the proportion of the fuel entering the squish region 
rises, indicating that the phenomenon of fuel accumulation is more 
likely to occur in the squish region at a large NIP. In NSPC mode, the 
effect of DIP is found to be insignificant compared to that of NIP. At a 
smaller NIP (20 MPa), the entrainment and disturbance effects of the 
free jet reduce. Therefore, a large proportion of the fuel still accumulates 
in the free jet development region at the top of the combustion chamber 
when the crank angle reaches 16
◦
CA ATDC. At the same time, the vortex 
structure at the bottom travels more slowly. In addition, at a larger NIP 
(35 MPa), it can be observed that part of the fuel entered the squish 
region, which can be concluded that rising NIP results in an increase in 
the proportion of fuel entering the squish region. 
Fig. 24 shows the effects of DIP and NIP on cylinder pressure and 
HRR in NMLC and NSPC modes. In NMLC mode, rising DIP can affect the 
PIP and PHRR only in a limited way. However, when NIP is small (20 
MPa), rising DIP can increase the momentum of diesel, which is 
conducive for diesel to further mixing with air, so the combustion in -
tensity increases in the late stage of combustion. It can also be seen that 
the PIP and PHRR gradually increase with rising NIP. This is mainly due 
to a better spatial distribution of the fuel and O
2 
mixture, as a result of 
the increased NIP, enhances the diffusion flame propagation rate and 
Fig. 22. Effects of SAN on the mean temperature in NMLC and NSPC modes.  
Fig. 23. Effects of DIP and NIP on local equivalence ratio and flow field dis -
tribution in NMLC and NSPC modes. 
G. Chen et al.

<!-- PDF_PAGE: 15 -->

Fuel 337 (2023) 127160
15
increases the chemical reaction rate in the combustion region, thus 
increasing the combustion intensity. 
In NSPC mode, when NIP is small (20 MPa), the natural gas jet has a 
reduced entrainment effect, so the interference of diesel and natural gas 
jets is weakened. Therefore, rising DIP can facilitate the multi-point 
ignition of natural gas. Instead, when NIP is 25 MPa, rising DIP delays 
the main combustion process. This is mainly because the entrainment 
effect of the natural gas jet is enhanced as NIP increases from 20 MPa to 
25 MPa. So if DIP increases, more injected diesel would be impacted by 
the natural gas-free jet, which makes the local diesel mixture too lean. 
Consequently, the ignition ability of diesel is weakened. What ’ s more, it 
can also be seen from Fig. 24 that the flame propagation becomes faster 
and the PHRR becomes higher during the main combustion stage when 
NIP increases from 25 MPa to 30 MPa. This is mainly because the 
penetration distance of the gas jet, which goes up as NIP increases, 
drives the air in the cylinder to flow to form a more uniform mixture. 
When NIP is 35 MPa, the natural gas has a stronger entrainment effect on 
the diesel, causing the local diesel mixture to be too lean, which makes 
compression ignition difficult and delays the main combustion stage. 
Fig. 25 shows the effects of DIP and NIP on MPRR and ITE in NMLC 
and NSPC modes. In NMLC mode, MPRR and ITE both show a rising 
trend with increasing DIP when NIP is low (20 MPa). However, ITE is not 
sensitive to the variation of DIP when NIP is high (25 MPa). It can also be 
seen in Fig. 25 that at different DIPs, MPRR and ITE rise simultaneously 
with increasing NIP. For instance, ITE can reach 44.1 % at a NIP of 35 
MPa. In this phase, the mass of natural gas entering the cylinder during a 
fixed time rises as the NIP increases. The intensive airflow movement in 
the cylinder accelerates the contact between the natural gas and the high 
temperature flame, promoting the propagation of the flame in the early 
phase of combustion. Therefore, in NMLC mode, increasing NIP and DIP 
is favorable for improving ITE. Meanwhile, the MPRR can be controlled 
within 1 MPa/
◦
CA. 
In NSPC mode, when DIP is 27 MPa and NIP is 25 MPa, or when DIP 
is 37 MPa and NIP is 20 MPa, ITE is relatively high because PIP and 
PHRR are pretty close to TDC. When DIP is 37 MPa and NIP is 30 MPa, 
PHRR is the highest and ITE reaches its maximum level (45.0 %) due to 
the intense combustion caused by the much premixed gas. However, the 
MPRR exceeds 1.5 MPa/
◦
CA. In addition, the ITE reaches its lowest 
when NIP is 35 MPa due to the reduced work capacity of the engine 
caused by the delayed combustion. 
Fig. 26 shows the effects of DIP and NIP on soot emissions in NMLC 
and NSPC modes. In NMLC mode, the use of high DIP can significantly 
reduce soot emissions when NIP is low (20 MPa). However, when NIP 
increases to 25 MPa, the increase of DIP is not conducive to reducing 
soot emissions. In general, the soot emissions first decrease and then 
increase with rising NIP for different DIPs, and reach the lowest value at 
a NIP of 30 MPa. The effect of DIP on soot emissions in NSPC mode is 
similar to that in NMLC mode. In NSPC mode, the effect of DIP on soot 
emissions is similar to those in NMLC mode. Meanwhile, soot emissions 
are generally low for different NIPs and show a declining trend. The 
above phenomena can be explained by the formation processes of soot, 
A
4 
and C
2
H
2 
at different DIPs and NIPs in NMLC and NSPC modes, as 
Fig. 24. Effects of DIP and NIP on cylinder pressure and HRR in NMLC and NSPC modes.  
Fig. 25. Effects of DIP and NIP on MPRR and ITE in NMLC and NSPC modes.  
G. Chen et al.

<!-- PDF_PAGE: 16 -->

Fuel 337 (2023) 127160
16
shown in Fig. 27 . 
As shown in Fig. 27 , in NMLC mode, the peak values of A
4
, C
2
H
2, 
and 
soot formation reduce simultaneously with rising DIP when NIP is 20 
MPa. This is due to the fact that the relatively high DIP promotes the 
middle and late combustion process of natural gas (after the crack angle 
reaches 20
◦
CA ATDC) and increases the combustion temperature in the 
cylinder ( Fig. 28 ). At the same time, the increase of the in-cylinder 
temperature in the middle and late combustion stages also promotes 
the oxidation of soot, thus reducing soot emissions. However, when NIP 
further increases (25 MPa), the interaction between the high- 
momentum natural gas jet and unburned diesel is enhanced. Such 
interaction is not conducive to the subsequent combustion of unburned 
diesel, so the inhibition effect of the increase in DIP on the production of 
precursors such as A
4 
and C
2
H
2 
is weakened. Consequently, the increase 
of DIP is not helpful to the improvement of soot emissions when NIP 
increases to 25 MPa. In addition, it can be seen from Fig. 29 that, when 
NIP is 20 MPa, the soot of high concentrations usually emerges in the 
equivalence ratio range of 1.0 – 2.7, while the equivalence ratio range for 
high concentrations of soot reduces to 1.0 – 2.0 when NIP increases to 30 
MPa. Therefore, an appropriate increase of NIP can greatly improve the 
mixture uniformity, thereby inhibiting fuel pyrolysis, dehydrogenation 
reaction, initial soot nucleation and surface growth. Ultimately, when 
NIP reaches 30 MPa, the peak value of A
4 
formation significantly re -
duces, the C
2
H
2 
reaction duration shortens, and the final soot emission 
reduces. When NIP increases from 30 MPa to 35 MPa, the equivalence 
ratio of soot of high concentrations does not change substantially, thus 
there is little change in the peak values of A
4
, C
2
H
2 
and soot formation. 
However, when NIP is 35 MPa, the temperature in the cylinder decreases 
at the late stage of combustion, so the soot oxidation rate becomes slow, 
leading to an increase in the final soot emissions. 
In NSPC mode, at a low NIP (20 MPa), the increase of DIP promotes 
the multi-point ignition process, leading to the early appearances of PIP 
and PHRR, which is beneficial to the increase of combustion tempera -
ture in the middle and late stages. Therefore, the process of soot 
oxidation is intense. While at a high NIP (25 MPa), the peak values of A
4
, 
C
2
H
2 
and soot formation vary little with the increase of DIP, which 
means that DIP has little effect on the process of soot formation. Addi -
tionally, for different DIPs, when NIP is 20 MPa, the disturbance effect of 
the natural gas jet on the airflow reduces, leading to the formation of 
local concentrated mixed gas regions in the cylinder ( Fig. 23 ). Therefore, 
the peaks values of A
4 
and soot formation are relatively high and C
2
H
2 
reaction duration is relatively long, resulting in more soot emissions. 
With the gradual increase of NIP, the local concentrated mixed gas re -
gions in the cylinder decrease. Especially when NIP reaches 35 MPa, 
where the degree of gas mixture homogenization in the cylinder is the 
highest and high concentrations of soot appear in a narrow equivalence 
ratio range of 1 – 1.7, soot emissions are extremely low. 
In summary, in NMLC mode, the soot emissions reach the lowest 
level at a DIP of 37 MPa and a NIP of 30 MPa, and ITE can reach the 
highest while MPRR maintains in a low level. Therefore, the operating 
point with a DIP of 37 MPa and a NIP of 30 MPa is found to be the 
optimal option for SSCC in NMLC mode. In NSPC mode, at a DIP of 37 
MPa and a NIP of 35 MPa, ITE is the highest and the soot emission is the 
lowest, but MPRR exceeds the limit (1.5 MPa/
◦
CA). As a result, the 
operating point with the DIP of 37 MPa and the NIP of 35 MPa is found 
to be the optimal option for SSCC in NSPC mode, which not only meets 
the MPRR limit but also maintains a high ITE and keeps the soot emis -
sion at an extremely low level. 
4. Conclusions 
In this paper, the potential of combustion chamber type, SAN, NIP, 
and DIP to achieve high thermal efficiency and low soot emissions in 
NMLC and NSPC modes was investigated by constructing the CFD nu -
merical model. The main findings can be summarized as follows: 
In NMLC mode, there is no significant difference in PIP and PHRR 
among the three combustion chamber types of SSCC, BCC, and TCC. 
The use of BCC and SSCC is beneficial to improve ITE and soot 
emissions simultaneously. In NSPC mode, the flame propagation is 
the fastest, and PIP and ITE are the highest for SSCC. Meanwhile, the 
soot emission is the lowest, which is 96 % lower than that of BCC. 
Fig. 26. Effects of DIP and NIP on soot emissions in NMLC and NSPC modes.  
G. Chen et al.

<!-- PDF_PAGE: 17 -->

Fuel 337 (2023) 127160
17
In NMLC mode, PIP and PHRR are the lowest when SAN is 15
◦
. When 
SAN increases from 15
◦
to 20
◦
, PIP and PHRR increase and ITE im -
proves. In addition, as SAN increases, soot emissions first decrease 
and then increase. When SAN is 18
◦
, the peak values of A
4 
and C
2
H
2 
formation and the final soot emission are the lowest due to the faster 
premixed flame propagation. In NSPC mode, the relatively small 
SANs (10
◦
, 15
◦
) are beneficial to reduce the fuel accumulation at the 
bowl bottom and promote flame propagation, thus improving ITE 
and inhibiting A
4 
and C
2
H
2 
formation. At the larger SAN (20
◦
), the 
final soot emission rapidly increases to 0.0193 g/kW ⋅ h. 
In NMLC mode, the effects of rising DIP on PIP and PHRR are limited. 
When NIP is small (20 MPa), increasing DIP has obvious effects on 
ITE and soot emissions. In NSPC mode, at small NIP (20 MPa), rising 
DIP facilitates the multi-point ignition of fuel. When NIP increases to 
25 MPa, increasing DIP delays the main combustion process, which is 
not conducive to improving ITE. 
In NMLC mode, with the increase of NIP, PIP and PHRR gradually 
rise, and ITE shows a rising trend. An excessively high NIP is not 
conducive to the oxidation of soot and leads to an increase in the 
final soot emissions. In NSPC mode, when NIP increases to 30 MPa, 
PHRR and ITE reach the highest value, but MPRR exceeds the limit 
(1.5 MPa/
◦
CA). When NIP further increases to 35 MPa, ITE de -
creases. Therefore, for NSPC mode, NIP should be controlled within 
30 MPa. In a word, the in-cylinder combustion process is more 
affected by injection parameters for NSPC mode. 
CRediT authorship contribution statement 
Guisheng Chen: Conceptualization, Methodology, Project adminis -
tration, Supervision, Writing – review & editing. Shun Yang: Method -
ology, Investigation, Formal analysis, Writing – original draft. Feng 
Wei: Investigation, Supervision, Validation, Supervision. Kaiqi Zhang: 
Investigation, Supervision, Validation. Da Nie: Data curation, Visuali -
zation. Hang Gong: Supervision. 
Declaration of Competing Interest 
The authors declare that they have no known competing financial 
interests or personal relationships that could have appeared to influence 
the work reported in this paper. 
0 20 40 60 80 100 120 140
0.00
0.02
0.04
0.06
0.08snoissimetoos (g/kW·h)
Crank angle (°CA ATDC)
NMLC mode
 S-27-20
 S-27-25
 S-37-20
 S-37-25
 S-37-30
 S-37-35
NSPC mode
 S-27-20
 S-27-25
 S-37-20
 S-37-25
 S-37-30
 S-37-35
0 20 40 60 80
0.00
0.03
0.06
0.09
0.12A4 (g/kW·h)
Crank angle (°CA ATDC)
NMLC mode
 S-27-20
 S-27-25
 S-37-20
 S-37-25
 S-37-30
 S-37-35
NSPC  mode
 S-27-20
 S-27-25
 S-37-20
S-37-25
 S-37-30
 S-37-35
(a) (b)
0 20 40 60 80
0.00
0.04
0.08
0.12
0.16A4 (g/kW·h)
Crank angle (°CA ATDC)
NMLC mode
 S-27-20
 S-27-25
 S-37-20
 S-37-25
 S-37-30
 S-37-35
NSPC  mode
 S-27-20
 S-27-25
 S-37-20
 S-37-25
 S-37-30
 S-37-35
(c)
Fig. 27. Effects of DIP and NIP on the formation processes of soot, A
4, 
and C
2
H
2 
in NMLC and NSPC modes.  
G. Chen et al.

<!-- PDF_PAGE: 18 -->

Fuel 337 (2023) 127160
18
Data availability 
The data that has been used is confidential. 
Acknowledgements 
The authors would like to acknowledge the financial supports to the 
research provided by National Natural Science Foundation of China 
(51866004), Extracurricular Academic Science and Technology Inno -
vation Fund Project for Students of Kunming University of Science and 
Technology (2022ZK065), and Scientific Research Foundation of 
Yunnan Provincial Department of Education (2022Y157). 
References 
[1] Grunewald N, Martinez-Zarzoso I. Did the Kyoto protocol fail? An evaluation of the 
effect of the Kyoto protocol on CO2 emissions. Environ Dev Econ 2016;21:1 – 22 . 
[2] Salman M, Long X, Wang G, Zha D. Paris climate agreement and global 
environmental efficiency: New evidence from fuzzy regression discontinuity 
design. Policy 2022;168:113128 . 
[3] Gao J, Huang J, Li X, Tian G, Wang X, Yang C, et al. Challenges of the UK 
government and industries regarding emission control after ICE vehicle bans. Sci 
Total Environ 2022;835:155406 . 
[4] Ximinis J, Massaguer A, Massaguer E. Towards compliance with the prospective 
EURO VII NOx emissions limit using a thermoelectric aftertreatment heater. Case 
Stud in Therm Eng 2022;36:102182 . 
[5] Yuan Z, Xie L, Sun X, Wang R, Li H, Liu J, et al. Effects of water vapor on auto- 
ignition characteristics and laminar flame speed of methane/air mixture under 
engine-relevant conditions. Fuel 2022;315:123169 . 
Fig. 28. Effects of DIP and NIP on the mean temperature in NMLC and NSPC modes.  
Fig. 29. Effects of DIP and NIP on cell data of soot mass fraction in NMLC and NSPC modes when crank angle is 30
◦
CA ATDC.  
G. Chen et al.

<!-- PDF_PAGE: 19 -->

Fuel 337 (2023) 127160
19
[6] Aghahasani M, Gharehghani A, Andwari AM, Mikulski M, K ¨onn ¨o J. Effect of 
natural gas direct injection (NGDI) on the performance and knock behavior of an SI 
engine. Energy Convers Manage 2022;269:116145 . 
[7] Liu J, Ma H, Liang W, Yang J, Sun P, Wang X, et al. Experimental investigation on 
combustion characteristics and influencing factors of PODE/methanol dual-fuel 
engine. Energy 2022;260:125131 . 
[8] Wang X, Gao J, Chen Z, Chen H, Zhao Y, Huang Y, et al. Evaluation of hydrous 
ethanol as a fuel for internal combustion engines: A review. Renew Energy 2022; 
194:504 – 25 . 
[9] Hall C, Kassa M. Advances in combustion control for natural gas – diesel dual fuel 
compression ignition engines in automotive applications: A review. Renew Sust 
Energy Rev 2021;148:111291 . 
[10] Yang X, Wang X, Dong Q, Ni Z, Song J, Zhou T. Experimental study on the two- 
phase fuel transient injection characteristics of the high-pressure natural gas and 
diesel co-direct injection engine. Energy 2022;243:123114 . 
[11] Wang Z, Fu X, Wang D, Xu Y, Du G, You J. A multilevel study on the influence of 
natural gas substitution rate on combustion mode and cyclic variation in a diesel/ 
natural gas dual fuel engine. Fuel 2021;294:120499 . 
[12] Armin M, Gholinia M, Pourfallah M. Investigation of the fuel injection angle/time 
on combustion, energy, and emissions of a heavy-duty dual-fuel diesel engine with 
reactivity control compression ignition mode. Energy Rep 2021;7:5239 – 47 . 
[13] Ouellette P, Goudie D, McTaggart-Cowan G. Progress in the development of natural 
gas high pressure direct injection for Euro VI heavy-duty trucks. Int 
Motorenkongress 2016:591 – 607 . 
[14] Li M, Zhang Q, Liu X, Ma Y, Zheng Q. Soot emission prediction in pilot ignited 
direct injection natural gas engine based on n-heptane/toluene/methane/PAH 
mechanism. Energy 2018;163:660 – 81 . 
[15] Faghani E, Kheirkhah P, Mabson CWJ, McTaggart-Cowan G, Kirchen P, Rogak S. 
Effect of injection strategies on emissions from a pilot-ignited direct-injection 
natural-gas engine part I: late post injection. SAE Tech Paper 2017-01-0774. 
[16] Rochussen J, Mctaggart-Cowan G, Kirchen P. Parametric study of pilot-ignited 
direct-injection natural gas combustion in an optically accessible heavy-duty 
engine. Int J Engine Res 2020;21(3):497 – 513 . 
[17] Mc Taggart-cowan GP, Rogak SN, Munshi SR. The influence of fuel composition on 
a heavy-duty, natural-gas direct injection engine. Fuel 2010;89:752 – 79 . 
[18] McTaggart-Cowan GP, Mann K, Huang J, Singh A, Patychuk B, Zheng ZX, et al. 
Direct injection of natural gas at up to 600 bar in a pilot-ignited heavy duty engine. 
SAE Int J Engines 2015;3:981 – 96 . 
[19] Lu X, Wei L, Zhong J. Effects of injection overlap and EGR on performance and 
emissions of natural gas HPDI marine engine. Combust Sci Tech 2022:1 – 18 . 
[20] Li M, Wu H, Zhang T, Shen B, Zhang Q. A comprehensive review of pilot ignited 
high pressure direct injection natural gas engines: Factors affecting combustion, 
emissions and performance. Renew Sust Energy Rev 2020;119:109653 . 
[21] Johnson T, Joshi A. Review of vehicle engine efficiency and emissions. SAE Int J 
Engines 2018;11(6):1307 – 30 . 
[22] Macian V, Monsalve-serrano J, Villalta D. Extending the potential of the dual-mode 
dual-fuel combustion towards the prospective EURO VII emissions limits using 
gasoline and OMEx. Energy Conver Manage 2021;223:113927 . 
[23] Mc Taggart-Cowan G, Bushe W, Rogak S, Hill P, Munshi S. Injection parameter 
effects on a direct injected, pilot ignited, heavy duty natural gas engine with EGR. 
SAE Trans 2003:2103 – 9 . 
[24] Zhang Q, Song G, Wang X, Mei L. Effects of injection strategy on the knocking 
behavior of a pilot ignited direct injection natural gas engine. Fuel 2022;308: 
121920 . 
[25] Cao DN, Hoang AT, Luu HQ. Effects of injection pressure on the NOx and PM 
emission control of diesel engine: a review under the aspect of PCCI combustion 
condition. Energy Source Part A 2020:1754531 . 
[26] Jin S, Li J, Deng L, Wu B. Effect of the HPDI and PPCI combustion modes of direct- 
injection natural gas engine on combustion and emissions. Energies 2021;14(7): 
1957 . 
[27] Zhang Q, Wang X, Song G, Li M. Performance and emissions of a pilot ignited direct 
injection natural gas engine operating at slightly premixed combustion mode. Fuel 
Process Tech 2022;227:107128 . 
[28] Faghani E, Kheirkhah P, Mabson CWJ, McTaggart-Cowan G, Kirchen P, Rogak S. 
Effect of injection strategies on emissions from a pilot-ignited direct-injection 
natural-gas engine - Part II: slightly premixed Combustion. SAE Tech Paper 2017- 
01-0774. 
[29] Liu J, Wang J, Zhao H. Optimization of the injection parameters and combustion 
chamber geometries of a diesel/natural gas RCCI engine. Energy 2018;164:837 – 52 . 
[30] Yadollahi B, Boroomand M. The effect of combustion chamber geometry on 
injection and mixture preparation in a CNG direct injection SI engine. Fuel 2013; 
107:52 – 62 . 
[31] Kamran P, Saray RK, Ansari E. Effect of diesel injection strategies on natural gas/ 
diesel RCCI combustion characteristics in a light duty diesel engine. Appl Energy 
2017;199:430 – 46 . 
[32] Pan K, Wallace J. Computational studies of fuel injection strategies on natural gas 
combustion characteristics in direct-injection engines. Fuel 2021;288:119823 . 
[33] Chen Y, Zhu Z, Chen Y, Huang H, Zhu Z, Lv D, et al. Study of injection pressure 
couple with EGR on combustion performance and emissions of natural gas-diesel 
dual-fuel engine. Fuel 2020;261:116409 . 
[34] Zhang S, Duan X, Liu Y, Guo G, Zeng H, Liu J, et al. Experimental and numerical 
study the effect of combustion chamber shapes on combustion and emissions 
characteristics in a heavy-duty lean burn SI natural gas engine coupled with detail 
combustion mechanism. Fuel 2019;258:116130 . 
[35] Wang H, Dong Q, Yan J, Zhang Y, Wang S. Influence of Injection Strategy on 
Combustion and Emissions of multi-point injection natural gas engine. J Xi ’ an 
Jiaotong Univ 2022;56(2):57 – 65 . 
[36] Faghani E. Effect of injection strategies on particulate matter emissions from HPDI 
natural-gas engine. Mechanical Engineering. British Columbia;2015. 
[37] Mabson CWJ. Emissions characterization of paired gaseous jets in a pilot-ignited 
natural-gas compression-ignition engine. Mechanical Engineering. Mechanical 
Engineering. British Columbia; 2015. 
[38] Le Moine J, Senecal PK, Kaiser SA, Salazar VM, Anders JW, Svensson KI, et al. 
A Computational study of the mixture preparation in a direct-injection hydrogen 
engine. J Eng Gas Turb Power 2015;137(11):111508 . 
[39] Smagorinsky J. General circulation experiments with the primitive equations: I. 
The basic experiment. General Circulation Research Laboratory, US Weather 
Bureau, Washington, DC 1963;91(3):99-164. 
[40] Reitz RD. Modeling atomization processes in high-pressure vaporizing sprays. At 
Spray Technol 1987;3:309 – 37 . 
[41] Beale JC, Reitz RD. Modeling spray atomization with the Kelvin-Helmholtz/ 
Rayleigh-Taylor hybrid model. Atomization Spray 1999;9(6):623 – 50 . 
[42] Han Z, Reitz RD. A temperature wall function formulation for variable-density 
turbulent flows with application to engine convective heat transfer modeling. Int J 
Heat Mass Tran 1997;40(3):613 – 25 . 
[43] Senecal P K, Pomraning E, Richards K J, Briggs T E, Choi C Y, McDavid R M, et al. 
Multi-dimensional modeling of direct-injection diesel spray liquid length and flame 
lift-off length using CFD and parallel detailed chemistry. SAE Trans 2003-01-1043. 
[44] Huang H, Lv D, Zhu J, Zhu Z, Chen Y, Pan Y, et al. Development of a new reduced 
diesel/natural gas mechanism for dual-fuel engine combustion and emission 
prediction. Fuel 2019;236:30 – 42 . 
[45] Vishwanathan G, Reitz RD. Modeling soot formation using reduced polycyclic 
aromatic hydrocarbon chemistry in n-Heptane lifted flames with application to low 
temperature combustion. J Eng Gas Turb Power 2009;131(3):29 – 36 . 
[46] Chen G, Wei F, Xiao R, Chen M, Wang Z, Zhang H. Numerical analysis of 
performance and soot emissions of a natural gas engine operating in HPDI and SPC 
combustion modes. Fuel 2022;327:125226 . 
[47] Chen G, Wei F, Yang J, Huang Z, Zhang X. Effect of jet angles on combustion 
process of a dual fuel engine. Trans Csice 2022;40(4):297 – 305 . 
[48] Mirko B, Daniela M, Ludovico V, Xu J. Combustion chamber design for a high- 
performance natural gas engine: CFD modeling and experimental investigation. 
Energ Conver Manage 2019;192:221 – 31 . 
[49] Yu J, Ville V, Harri H. An experimental investigation on the flow structure and 
mixture formation of low pressure ratio wall-impinging jets by a natural gas 
injector. J Nat Gas Sci Eng 2012;9:1 – 10 . 
[50] An Y, Jaasim M, Vallinayagam R, Vedharaj S, Im HG, Johansson B. Numerical 
simulation of combustion and soot under partially premixed combustion of low- 
octane gasoline. Fuel 2018;211:420 – 31 . 
G. Chen et al.
