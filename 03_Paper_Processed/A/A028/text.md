<!-- PDF_PAGE: 1 -->

Renewable and Sustainable Energy Reviews 150 (2021) 111390
Available online 13 July 2021
1364-0321/© 2021 Elsevier Ltd. All rights reserved.
Numerical investigations on pilot ignited high pressure direct injection 
natural gas engines: A review 
Menghan Li
a , b , c
, Hanming Wu
c
, Xiaori Liu
a
, Zhangning Wei
a
, Hongjian Tian
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
Natural gas engine 
High pressure direct injection 
Underexpanded gas jet 
Numerical study 
Computational fluid dynamics model 
ABSTRACT  
Pilot ignited high pressure direct injection natural gas engines have a lower tendency of end-wall gas formation 
owing to the fuel introduction method. Thus, this type of engines are adaptable to high compression ratios and 
have the potential to achieve low emission levels. In this paper, numerical investigations concerning under -
expanded gas jets and in-cylinder working process of pilot ignited high pressure direct injection natural gas 
engines are involved. The different numerical models adopted in the previous studies are systematically eval -
uated, giving guidance for the selection of numerical methods during the development of pilot ignited natural gas 
engines. The results indicate that analytical models could predict jet penetration with high accuracy while Mach 
disk height and diameter could be well reproduced by empirical correlations. Computational fluid dynamic 
models could provide more detailed information of jet flow fluid compared to analytical models and empirical 
correlations. Among all the computational fluid dynamic models, RANS models are considered as the most 
computational efficient ones while DNS is the most time consuming choice. If only the macro parameters are 
concerned, RANS models are the best choices. However, if near-field detailed structures are emphasized, using 
LES models is a better solution. When conducting three-dimensional simulations of the engine working process, 
RANS models are the most efficient choices for the modeling of in-cylinder flow field while reduced dual fuel 
mechanism coupled with phenomenological soot models could capture the in-cylinder combustion and emission 
formation processes with high-precision.   
1. Introduction 
Natural gas, which is an alternative fuel for crude oil fuels, has been 
widely used as the energy source for internal combustion engines in the 
past decades [ 1 , 2 ]. With the increasing awareness of environmental and 
energy issues, the adoption of natural gas engines has been more and 
more focused owing to its domestic availability and low emissions. 
Generally, natural gas could be classified into conventional gas and 
unconventional gas [ 3 ]. Conventional gas could coexist with petroleum 
and thus, could also be drilled from wells [ 4 ]. Unconventional natural 
gas is commonly obtained from shales [ 5 , 6 ], tight sandstones, coal 
seams [ 7 ], deep aquifers or deep-sea sediments [ 8 ]. Though the 
composition of natural gas varies with origin, the primary species are 
consistent, i.e., methane, ethane, propane, isobutene, n-butane, C
5
+
hydrocarbons, carbon dioxide and nitrogen [ 9 ]. When evaluating the 
impacts of using natural gas engine powered vehicles, it is more 
appropriate to take the whole well-to-wheel(WTW) process into 
consideration rather than only focus on the vehicle operation process. 
The WTW analysis generally involves the natural gas extraction, pro -
cessing, transportation, supply and vehicle operation processes ( Fig. 1 ). 
As previously investigated, vehicles powered by natural gas engines tend 
* Corresponding author. School of Energy and Power Engineering, Shandong University, No. 17923 Jingshi Road, Lixia District, Jinan, Shandong Province, 
250061, China. 
** Corresponding author. National Engineering Laboratory for Mobile Source Emission Control Technology, China Automotive Technology & Research Center, Co., 
Ltd., No. 68 Xianfeng East Road, Dongli District, Tianjin, 300300, China. 
E-mail addresses: sduzhangqiang@sdu.edu.cn (Q. Zhang), lizhenguo@catarc.ac.cn (Z. Li).  
Contents lists available at ScienceDirect 
Renewable and Sustainable Energy Reviews 
journal homepage: www.else vier.com/loc ate/rser 
https://doi.org/10.1016/j.rser.2021.111390 
Received 26 June 2020; Received in revised form 18 June 2021; Accepted 20 June 2021

<!-- PDF_PAGE: 2 -->

Renewable and Sustainable Energy Reviews 150 (2021) 111390
2
to generate less WTW nitrogen oxides(NOx), particulate matters(PM) 
and sulphur dioxide(SO
2
) emissions as a result of its low sulphur and 
carbon contents as well as the lower adiabatic flame temperature 
( Fig. 2 ), implying that the promoted application of natural gas engines 
could help to improve air quality [ 10 , 11 ]. 
Natural gas engines could be classified as spark ignition natural gas 
engines and compression ignition natural gas engines. Spark ignition 
natural gas engines include lean burn natural gas engines, stoichiometric 
natural gas engines and low-pressure direct injection natural gas en -
gines. Spark ignition lean burn natural gas engines could obtain higher 
resistance to knock compared to stoichiometric natural gas engine en -
gines. Thus, higher compression ratio could be used, which will in turn 
lead to higher thermal efficiency and power output [ 12 ]. Besides, 
benefiting from the sufficient air in the intake-charge, this type of en -
gines could achieve lower engine-out NOx, CO, THC and PM emissions 
along with lower thermal load. However, as the fuel/air mixture is 
harder to be ignited reliably at lean conditions, large cyclic variations 
and misfiring issues would be accompanied [ 13 ]. Furthermore, with the 
implementation of more stringent emission standards, Selective Catalyst 
Reduction(SCR) and Oxidization Catalyst(OC) devices should be 
equipped with this type of engines. Nevertheless, even with these 
aftertreatment devices, the tailpipe emission levels are still higher than 
the demand of the current regulations if no additional thermal man -
agement strategies are applied [ 14 ]. Though spark ignition stoichio -
metric natural gas engines suffer from high combustion temperature and 
high knock tendency as well as high engine out emissions, they have the 
capability of achieving ultra-low emissions when operating with exhaust 
gas recirculation(EGR) and three way catalyst(TWC). Thereby, the de -
mand of the emission standards could be met with simplified after -
treatment system [ 15 ]. However, the noble metal contents of the 
catalyst are high in this type of natural gas engines, which would in turn 
lead to increases in cost. Spark ignition low-pressure direct injection 
natural gas engines could be characterized by introducing natural gas in 
a direct injection pattern with injection pressure lower than 10 MPa and 
injection timing slightly later than intake valve close. With the direct 
injection strategy and the subsequent stratified-charge combustion 
mode, the volumetric efficiency could be improved and the knocking 
tendency could be mitigated, raising the thermal efficiency and power 
output of engines [ 16 ]. However, the ignition reliability for this kind of 
engines is highly dependent on the control of the fuel/air mixing quality 
near the spark-plug. Therefore, the performance and emissions of this 
type of engines are very sensitive to all influencing factors related to 
intake air motion and in-cylinder flow field, making the development of 
these engines technically challenging [ 17 ]. Another issue associated 
List of abbreviations 
A1 benzene 
A2 naphthalene 
A2R5 acenaphthylene 
A3 phenanthrene 
A3 phenanthrenyl 
A4 pyrene 
CFD computational fluid dynamics 
CO carbon monoxide 
CO
2 
carbon dioxide 
D
m 
diameter of Mach diameter 
DNS direct numerical simulation 
DPF diesel particulate filter 
DRG direct relation graph 
DRGEP direct relation graph with error propagation 
EGR exhaust gas recirculation 
HCCI homogenous charge compression ignition 
HPDI high pressure direct injection 
LES large eddy simulation 
NOx nitrogen oxides 
NGSI natural gas single injection 
NPSOI start of injection for natural gas pre-injection 
OC oxidization catalyst 
PNPI proportion of natural gas pre-injection 
R
p 
total pressure ratio 
R
e 
exit pressure ratio 
H
m 
height of Mach disk 
PAH polycyclic aromatic hydrocarbon 
PM particulate matter 
RNG renormalization group 
RANS Reynolds-averaged Navier-Stokes 
SOx sulphur oxides 
SCR selective catalyst reduction 
THC total hydrocarbons 
TWC three way catalyst 
WTW well to wheel 
H
m 
height of Mach disk  
Fig. 1. General stages involved in the WTW process [ 10 ].  
M. Li et al.

<!-- PDF_PAGE: 3 -->

Renewable and Sustainable Energy Reviews 150 (2021) 111390
3
with this kind of engines is the high voltage demand of the spark plug, 
which could lead to increased burning rate of electrodes and the cor -
responding shortened life of the spark plug [ 18 ]. 
Compression ignition natural gas engines could be classified into 
pilot ignited premixed natural gas engines, glow plug ignited direct in -
jection natural gas engines and pilot ignited direct injection natural gas 
engines. For pilot ignited premixed natural gas engines, natural gas is 
mixed with air before introducing into the cylinder and ignited by liquid 
fuels(diesel, n-butanol, dimethyl ether, biodiesel et al.) directly injected 
into cylinder [ 19 , 20 ]. The pilot ignited premixed natural gas engines 
could be adapted to compression ratio higher than spark ignition pre -
mixed natural gas engines attributed to the multipoint ignition pattern 
and the consequent increases in flame propagation speed. However, 
near-wall premixed mixture still exists, suggesting that the possibility 
for knocking and cool-wall quenching is relatively high. Besides, as 
diesel is participated in the combustion process, diesel particulate filter 
(DPF) should be added in the aftertreatment system. The characteristics 
of glow plug ignited direct injection natural gas engines are similar to 
those of spark ignition direct injection natural gas engines, which means 
the ignition quality is highly dependent on mixture formation and 
ignition location. The reliability of the glow plug is better than that of 
the spark plug as its heat release process is a continuous process, 
avoiding the use of high-voltage discharge [ 21 ]. Pilot ignited direct in -
jection natural gas engines adopt the direct injection pattern for both 
fuels(pilot fuel and natural gas). Under this circumstance, the ignition 
timing could be more accurately controlled with the multiple ignition 
points sourced from pilot flames, achieving different combustion modes. 
As the gaseous fuel is directly injected and ignited stably, the risk of 
knocking could be reduced to an extremely low level. Thus, this type of 
engines could be adapted to higher compression ratios and achieve 
higher thermal efficiencies [ 22 ]. Additionally, good emission charac -
teristics could be obtained by adopting optimized injection strategies 
and the correponding optimized combustion modes at different oper -
ating points. It has been proved that the Euro VI emission standards 
could be met by optimizing the combustion event [ 23 ]. Meanwhile, the 
cost of aftertreatment system could be reduced compared to conven -
tional natural gas engines since methane emission is reduced and fewer 
noble metals are needed. Therefore, pilot ignited direct injection natural 
gas engines seem to be the most promising energy source for future 
vehicles after comparing different types of natural gas engines( Table 1 ). 
During the development of pilot ignited direct injection natural gas 
engines, researchers and engineers would first obtain an acquaintance 
with the possible parameters which could improve the emissions and 
performance of the engine, and then assess the corresponding parame -
ters by numerical simulations according to the design objectives. 
Finally, the preferable schemes selected by the numerical simulations 
would be tested and verified by the experiments. The authors of this 
paper have previously published a review work focused on the effects of 
Fig. 2. WTW NOx and PM emissions of natural gas vehicles and their diesel counterparts [ 10 ].  
M. Li et al.

<!-- PDF_PAGE: 4 -->

Renewable and Sustainable Energy Reviews 150 (2021) 111390
4
different influencing factors on the experiment results of pilot ignited 
natural gas engines [ 24 ]. In the previously published work, the effects of 
injection parameters(including injection timing, injection pressure and 
injection interval between both fuels), injector design and gaseous fuel 
composition on the combustion process, emissions and performance of 
pilot ignited direct injection natural gas engines were analyzed; addi -
tionally, the characteristics of injection strategies were summarized; the 
results of this previous review work could give guidelines for engine 
optimization and fuel selection. However, review of the numerical 
methods, which have become essential tools in the engine development 
process, were not included. Numerical approach enables the initial 
evaluation of different design schemes and the estimations of different 
influencing factors before the qualification tests of engines. It could also 
capture the detailed and transient in-cylinder information, which cannot 
be provided by the experiment results, with little effort. Therefore, it is 
meaningful to make a comprehensive review for the numerical methods 
employed during the development of pilot ignited natural gas engines. 
In this paper, the numerical work of pilot ignited natural gas engines 
are emphasized from two main aspects, i.e., the numerical investigations 
on underexpanded gas jets and the Computational Fluid Dynamic(CFD) 
investigations on the working process of the engine. The numerical in -
vestigations on underexpanded gas jets are analyzed in Section 2 to give 
guidance for the selection of models or correlations used in the injector 
design process of pilot ignited natural gas engines. In this section, 
analytical models for jet penetration, empirical models for Mack disk 
height and diameter along with CFD models are evaluated to gain the 
adaptable range, advantages and disadvantages of different models. 
Afterwards, numerical investigations on the working process of engine 
are assessed in Section 3 to give references to the design of the com -
bustion system and the calibration of engine parameters from three key 
points, i.e., turbulence model, kinetic mechanism and soot prediction 
model. Finally, the challenges associated with the numerical in -
vestigations in Section 2 and Section 3 are summarized in Section 4 and 
the most instructive conclusions are provided in Section 5 . 
2. Numerical investigations on underexpanded gas jets 
In pilot ignited high pressure direct injection natural gas engines, the 
injection pressure of natural gas is ranging from 100 bar to 300 bar. 
During the natural gas injection process of high pressure direct injection 
natural gas engines, the ratio between natural gas rail pressure and in- 
cylinder pressure is a continuously changing value, the maximum of 
which could be higher than 1.85 [ 25 ]. This means that at the instant of 
natural gas injection, transient turbulent jets would be formed at the 
nozzle exits. With the ongoing of the injection process, the velocity of 
natural gas at the nozzle exit would be near-sonic or supersonic, forming 
underexpanded gas jet. For underexpanded transient gas jets, the 
penetration distance, the concentration distribution, local velocity dis -
tribution, mixing behavior and near-field structures are the key pa -
rameters. These parameters could affect the combustion and emission 
formation process and consequently should be considered by the nu -
merical models. In general, there are three kinds of models for predicting 
the characteristics of underexpanded transient gas jets, i.e., analytical 
models, empirical models and CFD models. In the numerical in -
vestigations regarding underexpanded gas jets, analytical models have 
been mainly constructed for jet penetration as it is a continuously 
changing parameter while empirical correlations have been adopted for 
the prediction of Mach disk structures, which are the key representatives 
of near-field flow fluid. When describing the Mach disk structures 
( Fig. 3 ), height and diameter of the Mach disk are the most important 
parameters and have been involved in many previous studies. 
2.1. Analytical models for jet penetration 
Analytical models were mainly proposed in the earliest studies of 
underexpanded gas jets. The main focus of the analytical models is to 
solve the transient jet penetration as it is easier to be solved by mathe -
matical methods. To achieve this purpose, most of the analytical models 
for underexpanded transient gas jets used the concept of Turner, in 
which a buoyant plume is considered as a quasi-steady-state jet region 
headed by a traveling vortex, as their theoretical basis [ 26 ]. With the 
application of Turner ’ s theory, Witze [ 27 ] managed to obtain the 
penetration of transient turbulent jet tip by solving the momentum 
balance equations and solved the momentum balance equations by 
introducing the radical velocity profile of steady-state turbulent jet 
theory [ 28 ]; the tip penetrations calculated by his model matched well 
with the experiment data of subsonic turbulent air jets. Afterwards, 
Ouellette [ 29 ] extended the model of Witze to supersonic turbulent 
methane jets. In Ouellette ’ s model, the transient vortex region is 
considered as a sphere with radius R
v
( Fig. 4 ); the mass and momentum 
of the vortex region are provided by the quasi-steady state region at 
plane i, which is z
v 
from nozzle exit. Assuming z
v 
is close to the contact 
point between the quasi-steady state region and the transient vortex 
region, the jet penetration z
t 
and tip velocity U
t 
could be written as: 
z
t
= z
v
+ 2 R
v
(1)  
U
t
= U
v
+ 2
dR
v
dt
(2) 
Table 1 
Comparison of different natural gas engines.  
Engine type Ignition type and 
ignition source 
Natural gas 
introduction 
method 
Aftertreatment 
system 
Pros Cons 
Lean burn natural gas 
engine 
Spark ignition, 
spark plug 
Premixed in the 
intake system 
SCR + OC Relatively high thermal efficiency; low 
engine-out HC emissions; low thermal 
load. 
Large cyclic variations and misfiring 
issues; low conversion efficiency of the 
aftertreatment system. 
Stoichiometric natural gas 
engine 
Spark ignition, 
spark plug 
Premixed in the 
intake system 
TWC High conversion efficiency of the 
aftertreatment system; simplified 
aftertreatment system. 
Low thermal efficiency; high thermal 
load; high knocking tendency; high 
engine-out HC emissions. 
Low-pressure direct 
injection natural gas 
engine 
Spark ignition, 
spark plug 
Direct injection SCR + OC Relatively high thermal efficiency. Low ignition quality; shortened life of 
the spark plug. 
Pilot ignited premixed 
natural gas engine 
Compression 
ignition, pilot fuel 
Premixed in the 
intake system 
SCR + OC + DPF Relatively high thermal efficiency; high 
ignition reliability. 
High knocking tendency; complicated 
fuel supply system; high engine-out HC 
emissions. 
Glow plug ignited direct 
injection natural gas 
engine 
Compression 
ignition, glow plug 
Direct injection SCR + OC High thermal efficiency. Low ignition quality; complicated fuel 
supply system. 
Pilot ignited direct 
injection natural gas 
engines 
Compression 
ignition, pilot fuel 
Direct injection SCR + OC + DPF High thermal efficiency; high ignition 
reliability; low knocking tendency; low 
engine-out HC emissions. 
Complicated fuel supply system.  
M. Li et al.

<!-- PDF_PAGE: 5 -->

Renewable and Sustainable Energy Reviews 150 (2021) 111390
5
The change in position of the transient vortex(U
v
) could be expressed 
by: 
U
v
=
dz
v
dt
(3) 
The changes in velocity(U
v
), total mass(m
v
) and methane mass 
fraction(m
CH4
) of the transient vortex could be expressed by: 
U
v
=
dz
v
dt
(4)  
dm
v
dt
= 2 π
∫
r
0
0
ρ ( U  U
v
) rdr (5)  
dm
CH 4
dt
= 2 π
∫
r
0
0
αρ
CH 4
( U  U
v
) rdr (6)  
where α represents the volume concentration of methane at plane i with 
radius r. 
After comparison of the model predicted results and experiment re -
sults of underexpanded methane jets, it was found that Ouellette ’ s 
model could capture the penetration rate far from the nozzle exit 
accurately; nevertheless, this analytical model failed to reproduce the jet 
penetration rate at the initial moments of injection. Later, to simplify the 
penetration solving process, Hill et al. [ 30 ] adopted the assumptions of 
self-similarity and uniform nozzle exit velocity. The transient penetra -
tion of the underexpanded z
t 
could be written as Eq. (7) to avoid the 
consideration of associated forces; his model was proved to capture the 
penetration of underexpanded natural gas jets with high accuracy. 
z
t
/
d
̅̅̅̅ ̅
ρ
n
ρ
a
√
= Γ
̅̅̅ ̅
π
4
√ (
U
0
t
/
d
̅̅̅̅ ̅
ρ
n
ρ
a
√ )
1 / 2
(7)  
where d, U
0
, ρ
n 
and ρ
a 
represent the nozzle diameter, exit velocity, exit 
gas density and surrounding density while Γ is a constant. 
However, since the twenty-first century, scarce research regarding 
analytical models for jet penetration has been reported. This is because 
in recent years, more detailed parameters, such as the near-field struc -
tures, the spatial and transient flow characteristics are more frequently 
investigated. These parameters could not be precisely expressed by 
analytical models. 
2.2. Correlations for Mack disk height and diameter 
2.2.1. Height of Mach disk 
For highly underexpanded gas jet with pressure ratio higher than 
4.05 [ 25 ], Mach disk appears at the near-field region. Most in -
vestigations regarding the description of Mach disk structures are 
mainly focused on empirical models since this kind of models, which are 
mainly derived from experiment results or mathematical methods, are 
reliable and accurate enough for the computation of Mach disk height 
and diameter. In order to calculate the height of Mach(H
m
) disk more 
conveniently, H
m 
is non-dimensionalized by the exit diameter(d) in all 
the corresponding correlations. A summary of the available correlations 
for the prediction of Mach disk height is illustrated in Table 2 . As 
generally agreed, the height of Mach disk is closely associated with total 
pressure ratio(R
p
) in the form of Eq. (8) . In the studies of Ashkenas and 
Sherman [ 31 ] as well as Crist et al. [ 32 ], the correlations for the height 
of Mach disk are proposed for convergent and conical nozzles at total 
pressure ratios higher than 10. The correlation of Ashkenas and Sherman 
[ 31 ] was summarized from experiment results, albeit the correlation of 
Crist et al. [ 32 ] was obtained based on the method of characteristics. At 
total pressure ratios lower than 10, modified empirical expressions 
developed by Orescanin and Austin [ 33 ] exhibited better agreement 
with the experiment results. Although Jothi and Srinivasan [ 34 ] proved 
that the empirical correlation of Norum and Seiner [ 35 ] originally 
proposed for average shock cell spacing could predict the height of Mach 
disk with acceptable accuracy at low pressure ratios, the validation for 
this correlation was limited to only one set of data. 
H
m
d
= C
m
(
R
a
p
+ A
)
b
(8) 
C
m
, a, A and b are constants related to nozzle geometry, range of total 
pressure ratio and type of reservoir. 
For slot nozzles, the height of the nozzle(h) is used for the calculation 
of Mach disk height instead of exit diameter as can be seen from the 
correlation proposed by Gannochenko et al. [ 36 ](Eq. (9) ). 
H
m
h
= 0 . 98 R
p
(9) 
According to the experiment results, the height of Mach disk could 
also be described as a function of the exponential form of exit pressure 
Fig. 3. The structure of underexpanded gas jets [ 25 ].  
Fig. 4. Diagram of transient turbulent jet model.  
M. Li et al.

<!-- PDF_PAGE: 6 -->

Renewable and Sustainable Energy Reviews 150 (2021) 111390
6
ratio(R
e
), polytropic coefficient, exit Mach number(M
n
) and ambient 
Mach number(M
a
) in the following form [ 36 – 40 ]: 
H
m
d
= C
m
M
a
n
γ
b
R
c
e
M
d
a
+ A (10)  
where C
m
, a, b, c and d are constants related to nozzle geometry, exit 
Mach number, fluid type, range of pressure ratio and ambient Mach 
number. γ is the polytropic coefficient. A is a constant, which is possible 
to have a non-zero value at exit pressure ratios ranging from 1.59 to 40 
[ 39 – 41 ]. In all the correlations following the format of Eq. (10) , the 
correlation of D ’ Attore and Harshbarger [ 40 ] is the only one taken the 
effects of ambient flow velocity into consideration. 
Based on the entropy-balance principle, Young [ 42 ] also proposed an 
analytical function which relates height of Mach disk with polytrophic 
coefficient and square root of pressure ratio. Though the calculated 
Mach disk heights based on Young ’ s correlation were shown to have 
distinguishable differences between different gas types, this behavior 
was not that obvious in experiments [ 42 ]. Other empirical correlations, 
which are expressed by exit pressure ratio along with one or two other 
parameters(Mach number, polytropic coefficient and exit diameter in 
different formats), were also proposed to describe the height of the Mach 
disk with high accuracy [ 43 – 47 ]. Among all the correlations reported for 
the prediction of Mach disk height issuing from round nozzles, the 
correlation proposed by Ashkenas and Sherman [ 31 ] as well as the 
correlation proposed by Crist et al. [ 32 ] were shown to reproduce the 
Mach disk height precisely in a wide range of total pressure ratios higher 
than 10 while the correlations of Orescanin and Austin [ 33 ] as well as 
the correlation of Billig et al. [ 38 ]are better choices at total pressure 
ratios lower than 10. The predicted values of Mach disk height by the 
correlation of Crist et al. [ 32 ] matched well with those observed in the 
experiments of Gao et al. [ 48 ], which were conducted for two-phase 
flow. However, when nozzles with slot structure are adopted, the cor -
relations of Gannochenko et al. [ 36 ] and Richard [ 47 ] tend to be more 
appropriate. Nonetheless, when the ambient environment is not static, 
the ambient fluid velocity should be taken into consideration; under this 
circumstance, the correlation of D ’ Attore and Harshbarger [ 40 ] is a good 
reference. 
2.2.2. Diameter of Mach disk 
The diameter of Mach disk(D
m
) is also closely related to pressure 
ratio, thus could be described by total pressure ratio(R
p
) or exit pressure 
ratio(R
e
). A summary of the available correlations for the prediction of 
Mach disk diameter is illustrated in Table 3 . Using total pressure ratio to 
calculate the diameter of Mach disk(D
m
), empirical correlations in the 
form of Eq. (11) have been proposed by Gibbings et al. [ 49 ], Addy [ 50 ] 
and Otobe et al. [ 51 ]. This type of equations have been proven to 
reproduce the Mach disk diameter with high precision. However, the 
correlation of Otobe et al. [ 51 ], which was given regardless of nozzle 
geometry, showed improved accuracy compared to that of Addy [ 50 ] 
while the correlation of Gibbings et al. [ 49 ] was only proved to be 
adaptable to conditions with very low total pressure ratios( ≤ 5). 
D
m
d
= C
m

C
R
R
p
 A
)
n
(11)  
where C
m
, C
R
, A and n are constants related to nozzle geometry and 
pressure ratio. 
When the diameter of Mach disk is expressed by the exit pressure 
ratio, various empirical correlations in other mathematical formats, i.e., 
exponential function and logarithmic function, were proposed in the 
studies of Avduevskii et al. [ 43 ], Billig et al. [ 38 ] and Antsupov [ 52 ]. 
Though the correlations in the study of Avduevskii et al. [ 43 ] were 
proposed for conditions with a wide range of pressure ratios, systematic 
validations were not available. The correlation of Billig et al. [ 38 ] were 
validated over exit pressure ratios ranging from 1 to 54; the results 
calculated by the correlation of Antsupov [ 52 ] fitted well with the 
experiment results at exit pressure ratios lower than 40. At exit pressure 
Table 2 
Correlations for the prediction of Mach disk height.  
Correlation Pressure ratio Nozzle 
geometry 
Mach 
number 
Gas type 
H
m
d
= 0 . 67
̅̅̅̅̅ ̅
R
p
√
(Ashkenas and Sherman 1964)  
15 – 1.7 ×
10
4
(R
p
) 
Convergent 0.05 – 4 Air, Ar 
H
m
d
= 0 . 645
̅̅̅̅̅ ̅
R
p
√
(Crist et al., 1966)  
10 – 2.5 ×
10
5
(R
p
) 
Conical 1 – 23 N
2
, Ar, He, Ar + He, CO
2
, 
Freon 22 
H
m
d
= C ( γ )
̅̅̅̅̅ ̅
R
p
√
(Young 1975)  
10 – 2000(R
p
) Convergent – Air, Ar, CO
2
, N
2
, H
2 
H
m
h
= 0 . 98 R
p
(Gannochenko et al., 1986)  
1-110(R
p
) Slot – Air 
H
m
d
= 0 . 53 R
0 . 6
p 
for infinite reservoir 
H
m
d
= 0 . 44 R
0 . 66
p 
for finite reservoir(Orescanin and Austin 2010)  
5-15(R
p
) Convergent – N
2
, He 
H
m
d
= 1 . 1
̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅ ̅
5 R
2 / 7
p
 6 . 0
√
(Jothi and Srinivasan 2019)  
2-6(R
p
) Circular slot ≤ 1.85 Air 
H
m
d
= 0 . 69 M
n
̅̅̅̅̅̅̅
γ R
e
√
(Lewis Jr and Carlson 1964)  
1 – 550(R
e
) Conical 1 – 3 N
2
, CO
2
, He 
H
m
d
= C
m
M
n
γ
1 / 2
R
c
e
M
d
a 
C
m 
= 0.69, c = 0.5 with 15
◦
nozzle exit angle, C
m 
= 0.813, c = 0.625 with 0
◦
nozzle exit angle; d =
0 when M
a
= 0, d =  0.5c when M
a
> 1(D ’ Attore and Harshbarger 1965)  
1 – 550(R
e
) Conical – Gas with γ v alue of 1.4, 
Gas with γ v alue of 1.225  
H
m
d
= 3 . 2
M
2
n
M
2
n
+ 1
R
0 . 39
e
(Finat ’ Ev 1968)  
10 – 1.0 ×
10
4
(R
e
) 
– 1 – 4.85 Air, CO
2 
H
m
d
= ( 0 . 8 + 0 . 085 ( M
n
 2 . 1 )
2
) M
n
( R
e
 0 . 5 )
0 . 5
when M
n 
= 1.0 – 3.6 
H
m
d
= ( 2 . 0 + 0 . 435 M
n
)( R
e
 0 . 5 )
0 . 5 
when M
n 
= 3.6 – 6.0(Avduevskii et al., 1970)  
1 – 4.0 ×
10
4
(R
e
) 
– 1 – 6 Air 
H
m
d
= M
1 / 4
n
̅̅̅̅̅
R
e
√
(Billig et al., 1971)  
1 – 10
5
(R
e
) Conical 1 – 4.5 Air, N
2 
H
m
d
=
(
γ M
2
n
R
e
j + 1
) 1 / ( j + 1 )
( γ M
n
)
j  1
(Richard 1972)  
29.4 – 915.6 
(R
e
) 
Slot, conical 2.89, 2.99 Air 
H
m
d
= 0 . 77 + 0 . 068 d
0 . 35
R
e
(Ewan 1986)  
3 – 14(R
e
) Contoured – Air 
H
m
d
= C
m
⋅ 1 . 58 ( R
e
 1 . 0 )
0 . 31
When R
e 
≤ 2.0
H
m
d
= C
m
( 1 . 89 R
0 . 39
e
 0 . 9 ) When R
e 
≥ 2.0 (D ’ Ambrosio 
et al., 1999)  
2 – 40(R
e
) – – Air  
M. Li et al.

<!-- PDF_PAGE: 7 -->

Renewable and Sustainable Energy Reviews 150 (2021) 111390
7
ratios higher than 100, Murzinov [ 53 ] derived a rather complex corre -
lation for the prediction of Mach disk diameter based on self-similarity 
assumption; he found that the Mach disk diameter is proportional to 
Mach disk height for highly expanded gas jets. The relationship between 
the height and diameter of Mach disk pointed out by Murzinov [ 53 ] was 
further confirmed by the study of Hatanaka and Saito [ 54 ], in which the 
Mach disk diameter is linear to Mach disk height at total pressure ratios 
in the range of 10 – 80 and the ratio between these two parameters varies 
with different nozzle geometries. 
2.3. CFD investigations on underexpanded gas jets 
With the development of numerical methods and computer tech -
nology, CFD has been recognized as a more reliable way for the pre -
diction of the structures and characteristics of underexpanded gas jets. 
Therefore, in the recent twenty years, extensive CFD studies have been 
conducted for underexpanded gas jets. In the previous studies, three 
kinds of numerical methods have been utilized, i.e., Reynolds-averaged 
Navier-Stokes(RANS) models, direct numerical simulation(DNS) and 
large eddy simulation(LES) models. 
2.3.1. Investigations based on RANS 
RANS models, which use time-averaged flow quantities for flow 
resolution, could save computational sources to a large extent and thus 
are widely used in the engineering field. When simulating the flow field 
of underexpanded gas jets, two-equation RANS turbulence models have 
been proved to be robust in the flow fluid prediction [ 55 ]. Li et al. [ 56 ] 
adopted standard k- ε turbulence model to capture the velocity and 
pressure distribution of underexpanded gas jets with total pressure ra -
tios ranging from 18.6 to 81.4; both of the axial velocity and pressure 
results agreed well with the results of an analytical model; meanwhile, 
the results of Mach disk height fitted well with the experiment results; 
however, the oscillations of axial pressure and velocity were not vali -
dated against experiment results. Ashraful et al. [ 57 ] numerically 
studied the near-field structure of underexpanded gas jets with total 
pressure ratios of 4.57, 5.23 and 6.2 based on Goldberg ’ s k-R turbulence 
model; it was demonstrated in their study that the simulated density 
contour was in good agreement with the schlieren image, indicating that 
Goldberg ’ s k-R turbulence model is adaptable for the prediction of Mach 
disk structures in underexpanded gas jets. By introducing additional 
compressibility correction source terms of local Mach number into the 
standard k- ε turbulence model, Birkby and Page [ 58 ] managed to obtain 
higher accuracy of turbulent viscosity reduction and centerline velocity 
prediction for underexpanded gas jets with exit pressure ratios of 
3.5 – 30; after comparing with the experiment data, it was depicted that 
compared to standard k- ε turbulence model, the prediction accuracy for 
the velocity in the far-field could be improved by the adoption 
compressibility-corrected k- ε turbulence model, albeit in the near-field 
regions, large diversities still existed. In order to attain better perfor -
mance in predicting the shock reflection, Fu et al. [ 59 ] modified the 
compressibility-corrected k- ε turbulence model of Birkby and Page [ 58 ] 
by improving the equation for the calculation of turbulent viscosity; the 
model was shown to reproduce the centerline Mach number of the 
underexpanded jets precisely( Fig. 5 ) and was then coupled with chem -
ical kinetic mechanism to reveal the effects of combustion on the char -
acteristics of underexpanded gas jets with exit pressure ratios ranging 
from 4.3 to 17.2; as suggested by their results, combustion could affect 
the distribution of velocity, temperature and shock cell structure. 
Recently, the numerical investigations of underexpanded gas jets 
based on RANS turbulence models have been focused on the assessment 
for the performances of various models. Evgenevna et al. [ 60 ] evaluated 
the performance of different RANS turbulence models in terms of the 
simulation of underexpanded gas jets with exit pressure ratio of 1.445; 
among standard k- ε model, realizable k- ε model, RNG k- ε model, stan -
dard SST k- ω model and transitional SST k- ω model, realizable k- ε model 
was shown to have the highest accuracy for the prediction of centerline 
pressure oscillations and low accuracy of near-field structure while 
transitional SST k- ω model could capture the near-field structure with 
high accuracy and showed poor performance in centerline pressure 
prediction; other RANS models showed poor performance in the pre -
diction of pressure oscillations and near-field structure. Besides, as 
pointed out in the study of Li et al. [ 61 ], realizable k- ε model could also 
capture the centerline velocity and concentration of injected fluid 
accurately with modified inlet boundary condition. In another study of 
Li et al. [ 62 ], the performance of different RANS models was also 
compared with each other; they pointed out that RSM model could 
capture the mass fraction of underexpanded helium and hydrogen jets 
with higher accuracy than k- ε and k- ω models at total pressure ratio of 
13 and 37; their results are different from those of Evgenevna et al. [ 60 ]; 
this phenomenon may be attributed to the discrepancies in nozzle ge -
ometry(round nozzle in the study of Evgenevna et al. [ 60 ] and slot 
nozzle in the study of Li et al. [ 62 ]) and pressure ratio. The assumption 
Table 3 
Correlations for the prediction of Mach disk diameter.  
Correlation Pressure ratio Nozzle geometry Mach 
number 
Gas type 
D
m
d
= ( 0 . 25 R
p
 3 . 47 )
0 . 86
(Gibbings et al., 1972)  
3.5 – 5(R
p
) Convergent – Air 
D
m
d
= 0 . 36
̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅ ̅
R
p
 3 . 9
√
for smooth nozzle 
D
m
d
= 0 . 31
̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅ ̅
R
p
 5 . 0
√
for sharp-edged nozzle(Addy 1981)  
1-10(R
p
) Convergent, 
divergent 
– Air 
D
m
d
= 0 . 115 R
p
 0 . 25(Otobe et al., 2008)  
4-12(R
p
) Convergent, 
divergent 
– Air 
D
m
d
=
[
γ + 1
4 . 8 γ
(
γ  1
2
)
γ
γ  1
]
M
1
γ  1
n
(Crist et al., 1966)  
10 – 2.5 ×
10
5
(R
p
) 
Conical 1 – 23 N
2
, Ar, He, Ar + He, CO
2
, 
Freon 22 
D
m
d
= ( 1 . 7 M
0 . 25
n
 1 . 0 )(
̅̅̅̅ ̅
R
e
√
 1 . 0 ) when R
e
> R
e
* 
D
m
d
≈ 1 . 0 when R
e
≤ R
*
e
, R
*
e
≈ [ M
n
/ ( M
n
 0 . 59 )]
2
(Avduevskii et al., 1970)  
1 – 4.0 × 10
4
(R
e
) – 1 – 6 Air 
D
m
d
=
0 . 72
d
(
1 . 0 +
2
γ  1
1
M
2
n
)
1 / 4
M
n
̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅ ̅
1 . 0 
1 . 0 +
1
γ M
2
n
̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅ ̅
1 . 0 +
2
γ  1
1
M
2
n
√
√
√
√
√
√
√
√
√
√
̅̅̅̅̅̅̅
γ R
e
√
, 
D
m
X
m
=
CONSTANT (Murzinov 1971)  
100 – 1.0 ×
10
4
(R
e
) 
Contoured 3 – 5 – 
D
m
d
= 3 . 6 [ 1 . 0  1 . 07 exp (  0 . 07 R
e
)] (Billig et al., 1971)  
1 – 54(R
e
) Contoured 1 – 3.0 Air 
D
m
d
=
5
2
log R
e

3
4
(Antsupov 1974)  
1-40(R
e
) Convergent 1 – 5.05 Air + alcohol + oxygen  
M. Li et al.

<!-- PDF_PAGE: 8 -->

Renewable and Sustainable Energy Reviews 150 (2021) 111390
8
that the adaptability of turbulence model to the simulation of under -
expanded gas jets is sensitive to nozzle geometry and pressure ratio was 
confirmed by the research of Stewart [63]; his research results indicated 
that among standard k- ε model, corrected k- ε models, Renormalization 
Group(RNG) k- ε model, SST k- ω model and RSM model, the simulated 
mass fractions of standard k- ε model were closest to the experiment 
results for underexpanded hydrogen jet through round nozzle at total 
pressure ratio of 10 while for underexpanded gas jet issued from rect -
angular nozzle with the same pressure ratio, the simulation results of 
SST k- ω model showed better agreement with experiment results than 
other models(Fig. 6). It could be concluded from the above mentioned 
studies that SST k- ω model is a generally agreed reliable choice for the 
simulation of near-field characteristics of underexpanded gas jets in all 
the RANS models, its prediction accuracy of Mach disk height could be 
ensured by coupling with Peng-Robinson equation of state especially at 
extremely high pressure ratio [64]. Though various k- ε models have 
high accuracies in terms of centerline pressure, centerline velocity or 
injected gas mass fraction, they could not capture the near-field fluid 
characteristics successfully. The comparison of different RANS models is 
illustrated in Table 4. It could be found that compressibility-corrected 
k- ε turbulence model and realizable k- ε model are superior to other 
models if velocity oscillations and Mach disk location are considered. 
However, its prediction accuracy of detailed near-field structure should 
be further improved. 
2.3.2. Investigations based on DNS 
Different from RANS turbulence models, DNS solves the Navier– -
Stokes equations numerically; this means all the temporal and spatial 
scales of the turbulence are calculated, leading to excessive consumption 
of computational sources. Thereby, there are very limited investigations 
regarding underexpanded gas jets based on DNS. In order to avoid the 
complexity of the modeling process, Cheng and Lee [72] utilized the 
weighted essentially non-oscillatory scheme with fourth order accuracy 
for both time and space to solve the governing equations directly; their 
simulations were performed at exit pressure ratio of 1.45 and Mach 
number of 2.0; the simulated axial mean velocity, pressure oscillations 
and radical velocity showed good agreement with the experiment re -
sults. Velikorodny and Kudriakov [73] performed simulations of 
underexpanded supersonic jet with total pressure ratio of 29.6 by solv -
ing the governing equations based on finite volume approach with 
second order spatial and temporal accuracy; Though the values of the 
simulated centerline pressure showed little deviation from the experi -
ment results at near-field regions, the mean pressure values and pressure 
oscillations at far-field regions were not well captured. In summary, the 
previous DNS simulations are not sufficient to come to a reliable 
conclusion; it could only be deduced that solving methods with higher 
order of accuracy seems to be able to achieve better performance for the 
prediction of jet characteristics. In addition, in order to achieve the 
adoption of DNS in the simulation of pilot ignited direct injection nat -
ural gas engines, it is essential to develop more efficient equation solving 
algorithm. 
2.3.3. Investigations based on LES 
In view of computational consumption, LES is a compromise be -
tween RANS and DNS. Its main advantage over RANS is that it could 
capture the transient flow structure accurately. LES simulations of 
underexpanded gas jets have become more and more concerned in 
recent twenty years owing to the rapid development of computer tech -
nology. Liu et al. [74] managed to capture the fluid structure and 
acoustic properties of the underexpanded gas jets with total pressure 
ratios ranging from 2.5 to 5.0 by LES with flux limiter for subgrid-scale 
modeling; as indicated by the comparison between simulation and 
experiment results, not only pressure and velocity profiles but also the 
spectra of near-field sound pressure level could be well captured by their 
model, implying that LES with flux limiter could be a powerful tool for 
the prediction of fluid and acoustic characteristics of underexpanded gas 
jets. Similar simulation approach(large-eddy simulations with flux lim -
iter) was also used by Munday et al. [75,76] for the simulation of 
Fig. 5. Comparison between the compressibility-corrected k- ε turbulence models and experiment data [59].  
Fig. 6. Comparison for the simulated mass fraction of different RANS models with experiment data: left(round nozzle), right(rectangular) [63].  
M. Li et al.

<!-- PDF_PAGE: 9 -->

Renewable and Sustainable Energy Reviews 150 (2021) 111390
9
underexpanded gas jets with total pressure ratios of 2.5 – 5.0; the calcu -
lated velocity profiles of their model also fitted well with the experiment 
results, further confirming the reliability of LES in terms of the simula -
tion of underexpanded jet velocity. In the study of Vuorinen et al. [ 77 ] 
and Yu et al. [ 78 ], LES based on scale selective discretization and a 
second order filter for the compression correction of viscosity was 
applied for the simulation of underexpanded gas jets with exit pressure 
ratios ranging from 3.0 to 8.5; different from the previous studies, their 
simulation results were compared to acetone planar laser-induced 
fluorescence(PLIF) images rather than the curves of different parame -
ters; in this case, the reliability of the specific near-field structures 
(including the location and size of the Mach disk, the reflection angle 
et al.) could be guaranteed( Fig. 7 ). In addition, as pointed out by Yu 
et al. [ 78 ], LES could demonstrate more detailed information that could 
not be provided by the experiment results, such as Mach number, local 
temperature distribution and scalar dissipation rate( Fig. 8 and Fig. 9 ). 
In the further study of Vuorinen et al. [ 79 ], LES based on scale se -
lective discretization was used to disclose the differences between the 
mixing characteristics of CH
4 
and N
2 
underexpanded jets with total 
pressure ratios ranging from 4.5 to 10.5, the simulated heights of Mach 
disk showed good agreement with the results calculated by the corre -
lation of Ashkenas and Sherman [ 31 ]; their results showed that the gas 
type has considerable effects on the jet characteristics, which implies 
Table 4 
RANS models used in the CFD investigations of underexpanded gas jets.  
Model Data for validation Advantages Gaps 
Standard k- ε (Li et al., 
2004, Stewart 2020) 
Calculated results of the method of 
characteristics [ 137 ]: centerline and axial 
velocity; centerline and axial pressure (R
p 
=
81.4; round nozzle). 
Experiment results of Adamson and Nicholls 
[ 65 ]: Mach disk location(R
p 
= 18.6, 46.5, 81.4; 
convergent-divergent nozzle). 
Experiment results of Ruggles and Ekoto [ 66 , 
67 ]: centerline mass fraction of injected fluid 
(R
p 
= 10; round nozzle & R
p 
= 300; slot nozzle). 
High-accuracy prediction of pressure, velocity 
and Mach disk location at high pressure ratios; 
high-accuracy prediction of centerline mass 
fraction issuing from round nozzle. 
Not validated for near-field pressure and 
velocity oscillations at relatively low pressure 
ratios; not validated for near-field structure; 
low-accuracy prediction of centerline mass 
fraction issuing from slot nozzle. 
Goldberg ’ s k-R(Ashraful 
et al., 2009) 
Experiment result of Ashraful et al.: schlieren 
image of near-field structure(R
p 
= 6.2; 
convergent nozzle). 
High-accuracy prediction of near-field structure. Not validated for pressure and velocity. 
Compressibility 
corrected k- ε (Birkby 
and Page 2001) 
Experiment results of Stickland et al. [ 68 ]: 
centerline velocity(R
e 
= 3.5, 5.0; round 
nozzle). 
Experiment results of Love et al. [ 69 ]: Mach 
disk height(R
e 
= 5 – 30; convergent-divergent 
nozzle). 
Higher accuracy of far-field velocity prediction 
compared to standard k- ε model; High-accuracy 
prediction of Mach disk location. 
Low prediction accuracy of near-field velocity 
oscillations. 
Modified 
compressibility- 
corrected k- ε (Fu et al., 
2014) 
Experiment results of Stickland et al. [ 68 ]: 
centerline velocity(R
e 
= 3.5, 5.0; round 
nozzle). 
Highest accuracy of velocity oscillations and far- 
field velocity among standard k- ε , compressibility 
corrected k- ε and modified compressibility 
corrected k- ε models; High-accuracy prediction of 
Mach disk location. 
Not validated for near-field structure and 
pressure. 
Realizable k- 
ε (Evgenevna et al., 
2014, Li et al., 2021) 
Experiment results of Dash et al. [ 70 ]: 
centerline pressure(R
e 
= 1.445; profiled 
nozzle). 
Experiment results of Li et al. [ 61 ]: centerline 
velocity and mass fraction of injected fluid(R
p 
= 10; round nozzle). 
Experiment result of Evgenevna et al. [ 60 ]: 
schlieren image of near-field structure(R
e 
= 24; 
profiled nozzle). 
Higher accuracy of pressure oscillations compared 
to k- ε RNG and SST k- ω ; High-accuracy prediction 
of centerline velocity and mass fraction of injected 
fluid. 
Low prediction accuracy of near-field structure; 
not validated for near-field structure. 
Standard SST k- 
ω (Stewart 2020) 
Experiment results of Ruggles and Ekoto [ 66 , 
67 ]: centerline mass fraction of injected fluid 
(R
p 
= 10; round nozzle & R
p 
= 300; slot nozzle). 
High-accuracy prediction of centerline mass 
fraction issuing from slot nozzle. 
Low-accuracy prediction of centerline mass 
fraction issuing from round nozzle; not 
validated for near-field structure, pressure and 
velocity. 
Transitional SST k- 
ω (Evgenevna et al., 
2014) 
Experiment results of Dash et al. [ 70 ]: 
centerline pressure(R
e 
= 1.445; profiled 
nozzle). 
Experiment result of Evgenevna et al.: schlieren 
image of near-field structure(R
e 
= 24; round 
nozzle). 
High prediction accuracy of near-field structure. Low accuracy of pressure oscillations; not 
validated for velocity. 
RSM(Li et al., 2019) Experiment results of Li et al. [ 71 ]: centerline 
mass fraction of injected fluid(R
p 
= 13, 37; slot 
nozzle). 
High prediction accuracy of centerline mass 
fraction of injected fluid. 
Not validated for pressure, velocity and near- 
field structure.  
Fig. 7. Comparison between LES and PLIF image of the underexpanded jets at 
exit pressure of 6.5 [ 78 ]. 
M. Li et al.

<!-- PDF_PAGE: 10 -->

Renewable and Sustainable Energy Reviews 150 (2021) 111390
10
that other gases, such as N
2 
and air, could not be used instead of natural 
gas in the experiment investigations regarding injector optimization. 
Zhang et al. [ 80 ] conducted simulations of underexpanded gas jets by 
LES based on stretched-vortex subgrid scale model at exit pressure ratio 
of 1.4; after comparing with the experiment results, it was found that 
their model could achieve high-precision prediction for the evolution of 
the vortex ring structure. 
Li et al. [ 81 , 82 ] investigated the pressure distribution, velocity dis -
tribution, shock wave structure and mixing characteristics of highly 
underexpanded hydrogen and nitrogen jets with total pressure ratio of 
5.6 by LES model based on one-equation subgrid scale model with linear 
eddy diffusivity assumption; in their study, the simulated flow fluid 
structure of the whole jet was verified by schlieren and PLIF images, the 
penetration distance, Mach disk height and diameter were proved to be 
accurately captured; based on the simulations carried out using the 
verified model, it was concluded that gas with lower density could 
obtain a higher penetration value but a smaller mixing volume. LES 
based on wall-adapting local-eddy viscosity subgrid scale model, which 
has been considered to be capable of reproducing the instabilities of the 
shear layer accurately, was utilized by Hamzehloo and Aleiferis [ 83 ] as 
well as Cui et al. [ 84 ] for simulations of underexpanded gas jets with 
different total pressure ratios (4.03, 8.5 and 10.0) and different back 
pressures(1 bar, 5 bar and 10 bar); however, in their study, not only 
near-field structure but also jet penetration and centerline velocity were 
verified, indicating that this model is capable of reproducing both 
detailed jet structure and fluid parameters with high precision. In 
summary, investigations based on LES paid more attention to the spatial 
structures and the instabilities of the flow field; in the LES simulations 
based on different subgrid scale models, including flux limiter, scale 
selective discretization, stretched-vortex, turbulent kinetic energy 
one-equation and local-eddy viscosity, good agreements with the 
experiment images of near-field structures were depicted. Nevertheless, 
systematic simulation investigations concerning the comparison be -
tween different LES methods in view of the flow field prediction for 
underexpanded gas jets have not been conducted yet. The pros and cons 
of different LES models are summarized in Table 5 . It could be concluded 
from the information in Table 5 that LES methods based on flux limiter 
and wall-adapting local-eddy viscosity subgrid scale models were more 
comprehensively validated. However, the validations of all the LES 
models were conducted for the simulation of round nozzles, their per -
formance in view of the prediction of underexpanded gas jets issuing 
from slot nozzles should be investigated in the future studies. 
3. Numerical investigations on the working process of engine 
Utilizing numerical approaches for the simulations of the engine 
working process could reduce experimental costs and shorten engine 
period. Therefore, CFD numerical simulation of the in-cylinder working 
process has become an essential part in the engine development process. 
It can be summarized from the previous studies that there are three key 
points in the simulation of the working process of pilot ignited direct 
injection natural gas engines, i.e., turbulence model, kinetic mechanism 
and soot model. A summary of the numerical methods adopted in the 
previous studies is given in Table 6 . 
3.1. Turbulence models employed for the simulation of in-cylinder flow 
field 
In the earliest numerical investigations, including the research work 
of Mtui [ 89 ], Ouellette et al. [ 90 , 91 ], Li et al. [ 92 ], etc., standard k- ε 
turbulence model is used for the simulation of in-cylinder flow field, 
development of natural gas jets and the fuel/air mixing processes. 
Though standard k- ε model is widely used in the earlier studies, 
Renormalization Group(RNG) k- ε model has been proved to have better 
performance in capturing the mean in-cylinder flow trend when the 
effects of the small-scale motions of high pressure natural gas jets and 
in-cylinder flow are considered [ 93 – 95 ]. Thus, RNG k- ε model was used 
in the studies of Lee and Montgomery [ 96 ], Li et al. [ 97 – 100 ] and Liu 
et al. [ 101 , 102 ]; nevertheless, RNG k- ε model is only capable of 
capturing the mean flow trends and unable to reproduce the detailed 
transient characteristics of in-cylinder flow. To obtain the detailed 
in-cylinder flow structure and turbulence fluctuations, Faghani et al. 
[ 103 , 104 ], Mabson et al. [ 105 ] and Kheirkhah [ 106 ] employed LES 
instead of RNG k- ε model for the simulation of in-cylinder flow field; it is 
no doubt that LES can capture the transient features of vortices with high 
accuracy [ 107 – 110 ]; however, the demand of computational sources is 
Fig. 8. LES results for the local temperature distribution of underexpanded jets with different pressure ratios [ 78 ].  
Fig. 9. LES results for the Mach number and concentration of underexpanded jets with different pressure ratios [ 78 ].  
M. Li et al.

<!-- PDF_PAGE: 11 -->

Renewable and Sustainable Energy Reviews 150 (2021) 111390
11
markedly higher compared to RNG k- ε model when coupled with 
detailed kinetic mechanisms. Actually, the engineering requirements 
could be well satisfied by RNG k- ε model when cyclic variations are not 
taken into consideration; therefore, in most recent studies, RNG k- ε 
model is a more favorable choice. Besides, it should also be noticed that 
the RANS turbulence models with high accuracy in the simulation of 
unexpanded gas jets, such as realizable k- ε model and 
compressibility-corrected turbulence model mentioned in Section 2.3.1 , 
have not been applied to the simulation of in-cylinder flow field of pilot 
ignited direct injection natural gas engines yet. 
3.2. Kinetic mechanisms employed for the simulation of in-cylinder 
combustion and emission formation 
In pilot ignited natural gas engines, one liquid fuel and one gaseous 
fuel are involved. Generally, diesel is used as the pilot fuel and natural 
gas is used as the gaseous fuel. From theoretical aspect, bio-CNG, which 
has high percentages of CH
4 
and CO
2
, could also be adopted as the 
gaseous fuel in pilot ignited natural gas engines. However, its production 
capability is limited, thus, has not been used as energy source in this type 
of engines yet. In this case, only the mechanisms of diesel and natural 
gas were considered in the previous simulation studies. The comparison 
of kinetic mechanisms used in the CFD investigations of pilot ignited 
direct injection natural gas engines is provided in Table 7 . 
In the study of Mtui [ 89 ], surrogate fuels with single composition, 
C
13
H
23 
and CH
4
, were selected to represent the commercial diesel and 
natural gas, respectively; meanwhile, with the purpose of describing the 
combustion process, single-step kinetic mechanisms were adopted for 
the prediction of fuel ignition and fuel consumption; for the prediction 
of NOx emissions, the Zeldovich mechanism(proposed in Ref. [ 111 ]) 
with six reaction steps were used; moreover, to take the mixing effects 
into consideration, the Magnussen combustion model(proposed in 
Ref. [ 112 ]) was applied in combination with the kinetic mechanisms to 
determine the overall reaction rates. Nonetheless, their model was 
validated against cylinder pressure at only one operating point, implying 
that the reliability of this model in terms of combustion and emission 
prediction is questionable. Ouellette et al. [ 90 , 91 ] improved the accu -
racy for the prediction of flame temperature by changing the single-step 
kinetic mechanism of methane to a stage-based methane mechanism, i.e. 
single-step mechanism for the ignition stage and two-step mechanism 
for the remainder combustion stages; however, the accuracy is still not 
sufficient for the prediction under various engine conditions. In the 
study of Li et al. [ 113 ], the prediction of pilot fuel ignition was improved 
by changing the pilot diesel mechanism from the single-step model to 
the 8-step Shell model, meanwhile, the characteristic-time combustion 
model was tuned to achieve higher prediction accuracy for the simula -
tion of the natural gas combustion process. Shell model could predict the 
pilot fuel ignition accurately at conditions without EGR, however, at 
conditions with EGR, the prediction of the Shell model is not reliable due 
to the limited number of reactions; the flaw of Zeldovich mechanism is 
similar to that of the Shell model, which means the trend for NOx 
emissions at conditions with EGR could not be well captured. Munshi 
et al. [ 114 ] improved the prediction accuracies of the ignition and heat 
release processes at conditions with EGR by the adoption of detailed 
mechanism instead of global reaction steps; in their study, a detailed 
mechanism with 170 species and 1500 reactions originated from the 
mechanism of LLNL [ 115 ] was adopted for the surrogate fuel of diesel 
and a modified GRI mechanism(i.e. UBC mechanism) with 54 species 
and 277 reactions [ 116 ] was adopted for the surrogate fuel of natural 
gas; besides, a NOx mechanism with 17 species and 102 reactions 
extracted from the GRI mechanism [ 117 ] was adopted to improve the 
prediction of NOx. Though the accuracies for the prediction of the 
chemical processes were improved by using more detailed mechanisms, 
the computational consumption was seriously raised. With the purpose 
of reducing computational consumption without sacrificing accuracy, 
Lee and Montgomery [ 96 ] employed the ERC mechanism [ 118 ], which 
Table 5 
LES models used in the CFD investigations of underexpanded gas jets.  
Model Data for validation Advantages Gaps 
LES with flux 
limiter(Liu 
et al., 2009; 
Munday et al., 
2008 and 
2011) 
Experiment results of 
Liu et al. [ 74 ]: radical 
and axial pressure(R
p 
=
3.5, 4.0; round nozzle); 
radical velocity(R
p 
=
4.0; round nozzle); 
spectra of near-field 
pressure(R
p 
= 3.5, 4.0; 
round nozzle); 
wavelength(R
p 
=
2.5 – 4.0; round nozzle). 
Experiment results of 
Munday et al. [ 75 , 76 ]: 
centerline pressure(R
p 
= 4.0; conical 
convergent-divergent 
nozzle); centerline 
velocity(R
p 
= 4.0; 
conical 
convergent-divergent 
nozzle); shock-cell 
spacing and 
shock-associated noise 
frequency (R
p 
=
2.5 – 5.0; conical 
convergent-divergent 
nozzle). 
High-accuracy 
prediction of 
pressure, 
velocity, shock- 
cell spacing and 
acoustic 
characteristics. 
Not validated 
for near-field 
structure; the 
prediction of 
wavelength 
could be 
further 
improved. 
LES based on 
scale selective 
discretization 
(Vuorinen 
et al., 2013 
and 2014, Yu 
et al., 2013) 
Experiment results of 
Yu et al. [ 78 , 85 ]: PLIF 
image of the near-field 
structure(R
P 
= 6.5; 
straight round nozzle); 
PLIF images of 
near-field structure(R
P 
= 5.5, 7.5; convergent 
nozzle). 
Calculated results of the 
method of Ashkenas and 
Sherman [ 31 ]: Mach 
disk height(R
P 
= 6.5; 
convergent nozzle). 
High-accuracy 
prediction of 
near-field 
structure. 
Not validated 
for pressure 
and velocity. 
LES based on 
stretched- 
vortex subgrid 
scale model 
(Zhang et al., 
2014) 
Experiment results of 
Zare-Behtash et al. [ 86 ]: 
Particle Image 
Velocimetry(PIV) image 
(R
p 
= 4.0; circular 
nozzle). 
High-accuracy 
prediction for the 
evolution of the 
vortex ring 
structure. 
Not validated 
for pressure, 
velocity and 
near-field 
structure. 
LES model based 
on turbulent 
kinetic energy 
one-equation 
subgrid scale 
model with 
linear eddy 
diffusivity 
assumption(Li 
et al., 
2016 & 2017) 
Experiment result of 
Meng [ 87 ]: schlieren 
image of the whole jet 
structure(R
p 
= 5.6; 
convergent nozzle). 
Experiment result of Yu 
et al. [ 77 ]: PLIF image 
of the whole jet 
structure(R
P 
= 5.5; 
convergent nozzle). 
High-accuracy 
prediction of the 
whole jet 
structure. 
Not validated 
for pressure 
and velocity. 
LES based on 
wall-adapting 
local-eddy 
viscosity 
subgrid scale 
model 
(Hamzehloo 
and Aleiferis 
2016, Cui 
et al., 2021) 
Experiment result of 
Ruggles and Ekoto [ 66 ]: 
schlieren image of 
near-field structure(R
P 
= 10.0; convergent 
nozzle). 
Simulation results of 
Vuorinen et al. [ 77 ]: jet 
penetration(R
P 
= 8.5; 
convergent nozzle). 
Experiment result of 
Henderson et al. [ 88 ]: 
centerline velocity and 
PIV image(R
P 
= 4.03; 
convergent nozzle). 
High-accuracy 
prediction of 
near-field 
structure, jet 
penetration and 
centerline 
velocity. 
Not validated 
for pressure.  
M. Li et al.

<!-- PDF_PAGE: 12 -->

Renewable and Sustainable Energy Reviews 150 (2021) 111390
12
is a reduced mechanism originally developed for the oxidation of 
n-heptane, to simulate the oxidation of both n-heptane and methane; 
this mechanism was proved to have good performance in the prediction 
of the ignition delay for n-heptane; the prediction accuracy of methane 
oxidation, however, was not validated for this mechanism, suggesting 
that the prediction for the oxidation and emission formation processes of 
natural gas may be not reliable in their numerical study. 
As could be summarized from the above analysis, the accuracies of 
flame temperature and ignition delay are at low levels when kinetic 
mechanisms with several steps are used for diesel oxidation, natural gas 
oxidation and NOx formation. As indicated by the results of Li et al. 
[ 113 ], the use of mechanisms within ten steps would lead to the under 
Table 6 
Numerical methods used in the previous studies of in-cylinder working process.  
Cylinder bore ×
stroke 
CR Turbulence 
model 
Surrogate 
fuel for 
diesel 
Surrogate 
fuel for 
natural gas 
Kinetic mechanism Combustion 
model 
NOx model Soot model 
108 mm × 127 
mm(Mtui P, 
1996) 
16:1 Standard k- ε 
model 
C
13
H
23 
CH
4 
Single-step(C
13
H
23
) for diesel 
oxidation, single-step(CH
4
) 
for natural gas oxidation 
Magnussen 
model 
6-step Zeldovich 
mechanism 
– 
123 mm × 127 
mm(Ouellette P 
et al., 
1996 & 1998) 
17:1 Standard k- ε 
model 
C
12
H
26 
or 
C
13
H
23 
CH
4 
Single-step(C
12
H
26 
or C
13
H
23
) 
for diesel, single-step(CH
4
) 
for natural gas ignition, two- 
step(CH
4
) for the remainder 
combustion process 
Magnussen 
model 
– – 
137 mm × 169 
mm(Li et al., 
2005) 
17:1 Standard k- ε 
model 
C
14
H
30 
CH
4 
8-step Shell model(C
14
H
30
), 
single-step(CH
4
) for natural 
gas oxidation 
Characteristic- 
time combustion 
model 
6-step Zeldovich 
mechanism 
– 
137 mm × 169 
mm(Munshi 
et al., 2011) 
15.3:1 Not 
mentioned 
n-C
7
H
16 
CH
4 
170 species and 1500 
reactions(LLNL mechanism, 
n-C
7
H
16
), 54 species and 277 
reactions(UBC mechanism, 
CH
4
) 
– NOx sub- 
mechanism in the 
GRI 2.11 
mechanism(17 
species, 102 
reactions) 
– 
175 mm × 221.6 
mm(Lee and 
Montgomery, 
2014) 
15.4:1 RNG k- ε 
model 
n-C
7
H
16 
CH
4 
Mechanism with 31 species 
and 55 reactions(n-C
7
H
16
, 
CH
4
) 
– – – 
137 mm × 169 
mm(Florea 
et al., 2016) 
– Standard k- ε 
model 
n-C
7
H
16 
CH
4 
Mechanism with 62 species 
and 358 reactions(n-C
7
H
16
, 
CH
4
) 
– NOx sub- 
mechanism in the 
GRI 3.0 
mechanism(14 
species, 106 
reactions) 
– 
137 mm × 169 
mm(Mabson 
et al., 2016) 
17:1 LES n-C
7
H
16 
CH
4 
170 species and 1500 
reactions(LLNL mechanism, 
n-C
7
H
16
), 55 species and 278 
reactions(UBC mechanism, 
CH
4
) 
– NOx sub- 
mechanism in the 
GRI 2.11 
mechanism(16 
species, 101 
reactions) 
2-step Hiroyasu 
model 
137 mm × 169 
mm(Kheirkhah 
2015, Faghani 
et al., 2016) 
17:1 LES n-C
7
H
16 
CH
4 
170 species and 1500 
reactions(LLNL mechanism, 
n-C
7
H
16
), 55 species and 278 
reactions(UBC mechanism, 
CH
4
) 
– 6-step Zeldovich 
mechanism 
2-step Hiroyasu 
model 
150 mm × 150 
mm(Li et al., 
2017) 
15.7:1 RNG k- ε 
model 
n-C
7
H
16 
CH
4 
Mechanism with 43 species 
and 225 reactions(n-C
7
H
16
, 
CH
4
) 
– 12-step NOx 
mechanism 
2-step Hiroyasu 
model 
150 mm × 150 
mm(Li et al., 
2018) 
15.7:1 RNG k- ε 
model 
Mixture of 
n-C
7
H
16 
and 
C
7
H
8 
CH
4 
Mechanism with 80 species 
and 324 reaction steps 
(mixture of n-C
7
H
16 
and 
C
7
H
8
, CH
4
) 
– 12-step NOx 
mechanism 
Phenomenological 
soot model 
150 mm × 150 
mm(Li et al., 
2019) 
15.7:1 RNG k- ε 
model 
n-C
7
H
16 
Mixture of 
CH
4
, C
2
H
6 
and C
3
H
8 
Mechanism with 77 species 
and 415 reaction steps(n- 
C
7
H
16
, mixture of CH
4
, C
2
H
6 
and C
3
H
8
) 
– 12-step NOx 
mechanism 
2-step Hiroyasu 
model 
137 mm × 169 
mm(Liu et al., 
2019 & 2020) 
17:1 RNG k- ε 
model 
Mixture of 
n-C
7
H
16 
and 
C
7
H
8 
Mixture of 
CH
4
, C
2
H
6 
and C
3
H
8 
Mechanism with 81 species 
and 421 reaction steps 
(mixture of n-C
7
H
16 
and 
C
7
H
8
, mixture of CH
4
, C
2
H
6 
and C
3
H
8 
in the study of Liu 
et al., 2019; mixture of n- 
C
7
H
16 
and C
7
H
8
, mixture of 
CH
4
, C
2
H
6
, C
3
H
8 
and n-C
4
H
10 
in the study of Liu et al., 
2020) 
– 15-step extended 
NOx mechanism 
Reduced mechanism 
for soot formation 
150 mm × 150 
mm(Li et al., 
2021) 
15.7:1 RNG k- ε 
model 
n-C
7
H
16 
Mixture of 
CH
4
, C
2
H
6 
and C
3
H
8 
Mechanism with 100 species 
and 543 reaction steps(n- 
C
7
H
16
, mixture of CH
4
, C
2
H
6 
and C
3
H
8
) 
– 12-step NOx 
mechanism 
Phenomenological 
soot model 
– indicates that the model was not used or the type of model or the value was not given. 
M. Li et al.

<!-- PDF_PAGE: 13 -->

Renewable and Sustainable Energy Reviews 150 (2021) 111390
13
prediction of in-cylinder heat release and NOx emissions due to the 
omission of some intermediate reactions and species; besides, when EGR 
is added, the NOx formation process could not be well predicted by 
simplified mechanisms as some NOx formation pathways are ignored. 
Consequently, more detailed mechanisms should be selected to ensure 
the prediction of the whole combustion process. Though, the mecha -
nisms with thousands of reactions used in the studies of Munshi et al. 
[114], Faghani et al. [103,104], Mabson et al. [105] and Kheirkhah 
[106] have been validated over a wide range of operating conditions in 
terms of ignition delay of the surrogate fuels, the computational expense 
is excessively large; besides, the sub-mechanism for the formation of 
soot precursors is not included, which means that these mechanisms are 
not adaptable to phenomenological or detailed soot models; in this case, 
only empirical soot models could be used in their studies. The short ERC 
mechanism [118] adopted in the study of Lee and Montgomery [96] and 
the reduced mechanism [119] adopted in the study of Liu et al. [101, 
102], which have been validated for the ignition delay and in-cylinder 
combustion process of n-heptane and toluene, could predict the 
combustion characteristics of diesel precisely and save computational 
resources. However, the prediction accuracies of the natural gas com -
bustion and emission formation processes are suspicious. As pointed out 
by Lee and Montgomery [96], compared to the mechanism with reliable 
natural gas reaction steps, IMEP and NOx emissions would be over -
estimated and CO emissions would be under predicted by the short ERC 
mechanism; the discrepancies are more distinct for CO emissions, sug -
gesting that the insufficient consideration for the oxidation steps of 
natural gas would seriously reduce the accuracy of CO prediction. To 
improve the prediction for the combustion process of natural gas, Florea 
et al. [120] adopted a reduced mechanism validated against cylinder 
pressure traces at conditions of both diesel and natural gas operation in 
HCCI engines [121]; nevertheless, the key combustion parameters of 
diesel and natural gas flames were not verified for this mechanism, 
indicating that the flame characteristics may not be well reproduced. 
The reduced mechanisms developed by Li et al. [97] and Jud et al. [122] 
contain the reaction steps for both diesel surrogate fuel and natural gas 
surrogate fuel(Fig. 10); their mechanisms were systematically validated 
for the ignition and flame propagation characteristics of both diesel and 
natural gas, suggesting that accuracies of the mechanisms are sufficient 
for the simulation of diesel and natural gas combustion; however, the 
mole fraction traces of the key intermittent species, which are vital for 
emission prediction during fuel oxidation, were not validated; addi -
tionally, these mechanisms are unable to realize the prediction of PAHs, 
implying that they are unadaptable to be coupled with phenomenolog -
ical or detailed soot models. 
In the further study of Li et al. [98], these problems were fixed by 
adding a PAH sub-mechanism into the dual fuel mechanism; meanwhile, 
validations for the mole fraction traces of the key species and soot 
precursors during oxidation were conducted to guarantee the accuracy 
of soot prediction(Fig. 11). The PAH sub-mechanism proposed in their 
study is consisted of the reaction pathways for the formation and con -
sumption of PAHs with one to four benzene rings. As illustrated in 
Fig. 12, benzene(A1) is formed by the reactions between species with 
three carbon atoms; naphthalene(A2) is produced by two channels: the 
first one is the recombination of C2–C4 species and aromatics with one 
benzene ring, the second one is the self-combination of cyclopentadieny 
(C
5
H
5
); the formation of phenanthrene(A3) is mainly associated with the 
recombination of aromatics with two benzene rings and C2–C4 species; 
after hydrogen abstraction, A3 would be converted to phenanthrenyl 
(A3-); A3-then reacts with acetylene(C
5
H
5
), leading to the formation of 
pyrene(A4); A4 could also be generated from the self-combination of 
indenyl. Besides, to realize more precise approximation to commercial 
diesel, the surrogate fuel of diesel was changed from n-heptane to the 
mixture of n-heptane and toluene. In another study of Li et al. [99], 
natural gas was represented by the mixture of methane, ethane and 
propane rather than barely methane to obtain more accurate predictions 
for the combustion and emission characteristics of natural gas. It should 
be mentioned that though the accuracies of combustion and emission 
predictions have been apparently improved in the recent studies of Li 
et al. [97–99], the computational efficiency was not impaired due to the 
application of efficient mechanism reduction methods, including direct 
relation graph(DRG) and direct relation graph with error propagation 
(DRGEP) [123–125], limiting the reactions to shorter than 500 steps. 
However, in these studies, only the PAH mole fraction profiles of 
n-heptane and methane were validated, which means that the other 
species in commercial natural gas could not be considered sufficiently in 
view of soot formation. This issue was solved by a recent study of Li et al. 
[100], in which PAH formation pathways and oxidation pathways of 
ethane and propane were considered and validated. Nevertheless, when 
these reactions were added, the total number of species was increased to 
100 species and the total number of reactions was increased to more 
than 500, indicating that the computational cost was undoubtedly 
raised. Moreover, it should be noticed that the mole fraction traces of 
many important soot precursors, such as acenaphthylene(A2R5), C
3
H
3 
and C
3
H
5
, have not been validated in the previously developed 
Table 7 
Comparison of kinetic mechanisms used in the CFD investigations of pilot 
ignited direct injection natural gas engines.  
Oxidation 
mechanism 
Mechanism 
for soot 
formation 
Advantages Gaps 
Single-step 
mechanism 
for diesel and 
one-step or 
two-step 
mechanism 
for natural 
gas 
Not 
available 
High computation 
efficiency. 
Low prediction 
accuracy for 
combustion and 
emission prediction. 
Eight-step 
mechanism 
for diesel and 
two-step 
mechanism 
for natural 
gas 
Not 
available 
High computational 
efficiency; improved 
prediction accuracy 
for the ignition 
process at conditions 
without EGR. 
Low prediction 
accuracy for the 
ignition process at 
conditions with EGR; 
low prediction 
accuracy for the 
combustion and 
emission prediction of 
natural gas. 
Reduced 
mechanism 
for diesel 
Not 
available 
Medium 
computational 
efficiency; high 
prediction accuracy 
for the ignition 
process. 
Low prediction 
accuracy for 
combustion and 
emission prediction of 
natural gas. 
Reduced 
mechanism 
for both 
diesel and 
natural gas 
Not 
available 
Medium 
computational 
efficiency; high 
prediction accuracy 
for the combustion 
process of diesel and 
natural gas. 
Could not be coupled 
with 
phenomenological 
and detailed soot 
models. 
Reduced 
mechanism 
for both 
diesel and 
natural gas 
PAH 
reaction 
steps 
High prediction 
accuracy for the 
combustion process of 
diesel and natural gas; 
high prediction 
accuracy for the 
formation of PAH 
species; could be 
coupled with 
phenomenological 
and detailed soot 
models. 
Relatively low 
computational 
efficiency. 
Detailed 
mechanism 
for both 
diesel and 
natural gas 
Not 
available 
High prediction 
accuracy for the 
combustion process of 
diesel and natural gas 
over a wide range of 
conditions. 
Very low 
computational 
efficiency; could not 
be coupled with 
phenomenological 
and detailed soot 
models.  
M. Li et al.

<!-- PDF_PAGE: 14 -->

Renewable and Sustainable Energy Reviews 150 (2021) 111390
14
mechanisms. Improving the pathways for more soot precursors could be 
a direction for the improvement of kinetic mechanism in the future 
research. 
3.3. Soot models employed for the simulation of in-cylinder soot 
formation and oxidation 
In the earlier studies, soot emissions were rarely investigated in the 
CFD investigations of pilot ignited direct injection natural gas engines 
because they were not limited in earlier emissions standards. Most 
studies related to soot emissions have been carried out after the imple -
mentation of Euro VI emission standards, in which the limitations of soot 
for natural gas engines were proposed. The soot emission models that 
could be applied in the CFD study of pilot ignited natural gas engines 
include two-step Hiroyasu model, phenomenological soot models and 
detailed soot models. All of these three kinds of soot models are capable 
to capture the spatial and temporal evolution of in-cylinder soot mass as 
shown in Fig. 13 . However, the accuracy, adaptability and computa -
tional efficiency are different for different kinds of models. 
In the studies of Faghani et al. [ 103 , 104 ], Mabson et al. [ 105 ] and 
Kheirkhah [ 106 ] as well as in the two of Li et al.‘s numerical studies [ 97 , 
99 ], the 2-step Hiroyasu model [ 126 ], which contains one step for soot 
formation and another step for soot oxidation, was applied for soot 
prediction due to its high adaptability to mechanisms. Though a crude 
Fig. 10. Main reaction paths for the mechanism of Li et al. [ 97 ].  
Fig. 11. Validation of PAH species in natural gas and diesel surrogate fuels [ 98 ].  
Fig. 12. Main reaction paths for the PAH sub-mechanism of Li et al. [ 98 ].  
M. Li et al.

<!-- PDF_PAGE: 15 -->

Renewable and Sustainable Energy Reviews 150 (2021) 111390
15
trend of soot could be gained by the 2-step empirical model, it was 
oversimplified and was developed for conventional diesel engines [ 127 ]; 
thus, its accuracy of soot emission prediction in pilot ignited direct in -
jection natural gas engines is to some extent questionable. When 
coupled with PAH mechanisms accurate in both diesel and natural gas 
flames, the phenomenological soot model [ 128 ] adopted in Ref. [ 98 ] 
could obtain more reliable prediction of soot emissions than the 2-step 
soot model, whereas the demand for computational resources will be 
higher because the inception, coagulation, surface growth and oxidation 
processes of soot particles are taken into consideration; moreover, when 
comes to soot particle size, only mean diameter could be obtained. 
Detailed soot models, such as the method of moments [ 129 – 131 ], the 
sectional method [ 132 , 133 ] and the Monte Carlo method [ 134 – 136 ], 
have the capability to resolve the spatial particle size distribution and 
track the transient changes in particle sizes by solving the population 
balance equation. However, these detailed soot models were not used in 
the previous studies since the computational expense is relatively high 
and the previous researchers were less concerned with particle size 
distribution and evolution. As the evaluation of particle size distribution 
has become an important research interest in recent years, the adoption 
of detailed soot models in pilot ignited direct injection natural gas en -
gines is required to be investigated in the future work. 
4. Challenges associated with numerical investigations  
(1) Most analytical models were focused on the mathematical 
description of jet penetration. Detailed near-field structures, such 
as Mach disk height and diameter, could not be accurately pre -
dicted by analytical models until now.  
(2) Mack disk height and diameter could be reproduced well by 
empirical correlations. However, it seems that geometry of the 
nozzles has profound effects on the parameters of Mach disk, 
which means that the previously developed correlations may be 
not adaptable to nozzles with new designs.  
(3) Most of the RANS models could not capture the detailed near- 
field structures of underexpanded gas jets. Also, this kind of 
models are not adaptable to the simulation of the turbulent 
fluctuations of the flow field.  
(4) Though DNS and LES could capture the detailed near-field 
structure and turbulent fluctuations of underexpaned gas jets 
with high accuracies if solving method and sub-grid model are 
appropriately selected, the computational costs of these models 
are relatively high. This is because instantaneous Navier – Stokes 
equations are solved when DNS model is applied and large scale 
motions are solved when LES model is adopted. Besides, fine 
meshes are required when using DNS or LES, which further in -
creases the computational consumption. Thereby, high-efficiency 
computation is the biggest challenge facing these two kinds of 
models.  
(5) As the transient simulation of underexpanded gas jets is involved 
in the CFD simulation for the working process of pilot ignited 
direct injection natural gas engines, the computational cost is 
rather large when coupled with chemical mechanism and soot 
model. Therefore, it is challenging to reduce computation cost 
without sacrifices in accuracies for the prediction of combustion 
and emission formation processes. 
5. Conclusions and prospects 
5.1. Conclusions 
This paper offers a comprehensive review of the numerical methods 
used in the development of pilot ignited high pressure direct injection 
natural gas engines. The numerical methods are evaluated from different 
aspects, the key findings can be concluded as follows:  
(1) Penetration of underexpanded jets is a basic parameter that could 
be described by analytical models. Most analytical models 
regarding this parameter are based on the concept that the gas 
jets could be treated as two parts, i.e. a quasi-steady-state region 
and a traveling vortex. On the basis of this theory, the penetration 
of underexpanded gas jets was obtained by solving the mo -
mentum balance equations and gas properties were taken into 
consideration to get more reasonable results. Further, self- 
similarity assumption was adopted, forming a simplified analyt -
ical model with high computational efficiency and high precision. 
However, investigations on analytical models became rarer in the 
past twenty years due to the development of the advanced nu -
merical methods.  
(2) For the prediction of Mach disk height of underexpanded gas jets 
issuing form round nozzles, the correlations proposed by Ashke -
nas and Sherman along with the correlation proposed by Crist 
et al.was proved to be the preferable choices at total pressure 
ratios higher than 10, whereas the correlations of Orescanin and 
Austin [ 32 ] as well as the correlation of Billig et al. [ 39 ] are more 
reliable at total pressure ratios lower than 10. For the prediction 
of Mach disk height of underexpanded gas jets issuing form slot 
nozzles, the correlations of Gannochenko et al. [ 37 ] and Richard 
[ 47 ] were validated against experiment data and tend to be more 
accurate. 
Fig. 13. Local soot mass fraction distribution of different injection strategies at 15
◦
ATDC: NGSI represents natural gas single injection strategy, PNPI represents 
proportion of natural gas pre-injection, NPSOI represents start of injection for natural gas pre-injection [ 99 ]. 
M. Li et al.

<!-- PDF_PAGE: 16 -->

Renewable and Sustainable Energy Reviews 150 (2021) 111390
16
(3) With regard to the Mach disk diameter, most investigations are 
focused on round nozzles. The correlation of Otobe et al. [51] 
performs well at total pressure ratios lower than 12 for both 
converge and divergent nozzles. For contoured nozzle, the cor -
relation of Billig et al. [39] could be chosen at exit pressure ratios 
in the range of 1–54. For convergent nozzle, the correlation of 
Antsupov [54] has high accuracy at exit pressure ratios lower 
than 40. At total pressure ratios higher than 10, the Mach disk 
diameter is linear to the Mach disk height while the ratio between 
these two parameters is associated with the nozzle geometry. 
(4) Among all the RANS models used for the simulation of under -
expanded gas jets, RSM model, standard k- ε model and SST k- ω 
model have the capability to reproduce the mass fraction of the 
injected gas precisely at specific conditions. Compressibility- 
corrected k- ε model and realizable k- ε model have better per -
formance if velocity or pressure oscillations become the research 
focus while compressibility-corrected k- ε model is superior to 
realizable k- ε model when prediction the location of Mach disk. If 
the near-field structure is emphasized, SST k- ω model coupling 
with Peng-Robinson equation tends to be the best choice. 
(5) By the adoption of LES, the transient evolution of the under -
expanded gas jets could be better captured with sacrifices in the 
consumption of computation sources. In the previous studies, LES 
methods based on different subgrid scale models, including flux 
limiter, scale selective discretization, stretched-vortex and linear 
eddy diffusivity assumption, have been employed for the simu -
lation of underexpanded gas jets. LES methods based on flux 
limiter and wall-adapting local-eddy viscosity subgrid scale 
models were validated for its prediction accuracies of pressure 
distribution, velocity distribution and jet penetration while other 
LES models were mainly validated for their prediction accuracies 
of near-field structures. Besides, the systematic comparison be -
tween different LES models in view of the simulation of under -
expanded gas jets has not been investigated yet.  
(6) In view of the numerical studies of engine working process, RNG 
k- ε model is regarded as an efficient and reliable choice for the 
simulation of in-cylinder flow field if transient flow fluctuations 
and detailed vortex structure are not the research focus. If these 
details are systematically considered or cyclic variations become 
a focus, LES may be more preferable. Additionally, 
compressibility-corrected k- ε model and realizable k- ε model are 
worth trying in the in-cylinder simulation of pilot ignited natural 
gas engines due to their good performance in the prediction for 
the characteristics of underexpanded gas jets. 
(7) For pilot ignited direct injection natural gas engines, as super -
sonic jet simulation is involved in the simulation of in-cylinder 
working process, the computational costs are generally high. 
Thereby, it is not realistic to use detailed kinetic mechanisms in 
the CFD simulations. However, mechanisms with several reaction 
steps are over-simplified and thus have shown poor accuracy. In 
this case, reduced chemical mechanisms for surrogate fuels with 
no more than 100 species have been considered as a reliable and 
high-accuracy option for prediction of the combustion and 
emission formation processes in pilot ignited direct injection 
natural gas engines. 
(8) Three kinds of models are widely used for soot prediction in en -
gines, namely, 2-step empirical model, phenomenological model 
and detailed model. The 2-step empirical model(Hiroyasu model) 
has only been verified for diesel engines, its use on pilot ignited 
high pressure direct injection natural gas engines is highly 
doubtful. Phenomenological soot models could achieve a good 
compromise between accuracy and computational efficiency; 
however, as PAHs are used as the soot precursor of the 
phenomenological soot models, PAH sub-mechanism should be 
added in the kinetic mechanism, which means phenomenological 
soot models have high demand for the prediction accuracy of the 
concentration of PAH species. Detailed soot models are recom -
mended if soot particle size distribution is considered; but this 
kind of models have not been applied in pilot ignited high pres -
sure direct injection natural gas engines yet due to the higher 
computational cost. 
5.2. Practical implications 
The practical implications of this paper could be summarized as 
follows:  
(1) The review of analytical models of jet penetration along with the 
empirical correlations of Mach disk height and diameter could 
give guidance in the injector design process of pilot ignited nat -
ural gas engines.  
(2) The review of CFD methods of underexpanded gas jets could aid 
the design of injector geometry and the optimization of injection 
parameters(injection pressure, injection timing and injection 
strategy et al.).  
(3) The review of CFD models for the in-cylinder working process is 
vital for the design of the combustion system, the calibration of 
injection parameters and the assessment of different combustion 
modes. 
5.3. Limitations and prospects 
The limitations and prospects of this paper are given as follows:  
(1) As the near-field structure of underexpanded gas jets could be 
considerably affected by fluid properties, correlations of Mach 
disk diameter and height specific for the underexpanded jets of 
natural gas should be further investigated to improve the pre -
diction accuracies during the development of pilot ignited natural 
gas engines. Moreover, the effects of nozzle geometry(conver -
gent, divergent, slot et al.) on the Mach disk structures have not 
been systematically clarified until now. Thus, in the future work, 
the effects of nozzle geometry on Mach disk diameter and height 
should be symmetrically investigated and considered in the 
empirical correlations.  
(2) For CFD simulations of underexpanded gas jets, both macroscopic 
and microscopic characteristics should be guaranteed. Most of 
the previous LES models were only validated for the near-field 
microscopic structure and neglected the validation of the 
macroscopic characteristics, such as centerline pressure, center -
line velocity and species concentration. Under this circumstance, 
when adopted to predict these macroscopic characteristics, the 
reliability of these LES models is suspicious. Besides, all the LES 
models were not verified for the prediction of underexpanded gas 
jets issuing from slot nozzles. Thereby, the performance of LES 
methods in view of macroscopic parameter prediction should be 
further studied and simulations of underexpanded gas jets dis -
charging from slot nozzles will be a subject of future studies based 
on LES methods.  
(3) After modification, compressibility-corrected k- ε turbulence 
model, which has high accuracies in the predictions of velocity 
and Mach disk location, and SST k- ω model, which could capture 
the near-field structure precisely, have not been used in the CFD 
simulations of pilot ignited direct injection natural gas engines 
yet. Therefore, the adaptability of these models in the CFD sim -
ulations of pilot ignited direct injection natural gas engines 
should be evaluated. Meanwhile, compressibility-corrected k- ε 
turbulence model should be further modified for its prediction of 
near-field structure.  
(4) As the evolution of soot particle size distribution has become 
increasingly attractive recently, research focused on the adoption 
M. Li et al.

<!-- PDF_PAGE: 17 -->

Renewable and Sustainable Energy Reviews 150 (2021) 111390
17
of detailed soot models in the CFD simulations of pilot ignited 
high pressure direct injection natural gas engines is required.  
(5) The effects of the adoption of bio-CNG have not been evaluated 
by simulations yet. Future research focused on this aspect will 
contribute to the increase of sustainability of this kind of engines. 
Declaration of competing interest 
The authors declare that they have no known competing financial 
interests or personal relationships that could have appeared to influence 
the work reported in this paper. 
Acknowledgement 
This work was funded by the National Natural Science Foundation of 
China(No.51906057), the Science and Technology Project of Hebei 
Education Department (No.QN2019056), the Natural Science Founda -
tion of Hebei Province (No.E2019202198), Key Training Fund for 
“ Project & Team ” of Tianjin of China (No.XC202042), Hebei Engineer -
ing Research Center of Pollution Control in Power System. It should also 
be noted that the reuse permission for all the figures cited in this paper 
has been obtained by the authors. 
References 
[1] Korakianitis T, Namasivayam AM, Crookes RJ. Natural-gas fueled spark-ignition 
(SI) and compression-ignition (CI) engine performance and emissions. Prog 
Energy Combust 2011;37(1):89 – 112 . 
[2] Hegab A, Rocca AL, Shayler P. Towards keeping diesel fuel supply and demand in 
balance: dual-fuelling of diesel engines with natural gas. Renew Sustain Energy 
Rev 2017;70:666 – 97 . 
[3] Speight JG. Natural gas: a basic handbook. Houston: Texas: Gulf Publishing 
Company; 2007 . 
[4] Speight JG. Handbook of petroleum product analysis. second ed. New York: John 
Wiley and Sons Inc; 2015 . 
[5] Prinzhofer A, Battani A. Gas isotopes tracing: an important tool for hydrocarbons 
exploration. Oil Gas. Sci Technol Rev IFP 2003;58(2):299 – 311 . 
[6] Golding SD, Boreham CJ, Esterle JS. Stable isotope geochemistry of coal bed and 
shale gas and related production waters: a review. Int J Coal Geol 2013;120: 
24 – 40 . 
[7] Moore TA. Coalbed methane: a review. Int J Coal Geol 2012;101:36 – 81 . 
[8] Wuerthner G. Gas hydrates: a dangerously large source of unconventional 
hydrocarbons. In: Butler T, Wuerthner G, Lerch D, editors. The energy reader: 
overdevelopment and the delusion of endless growth. New York: watershed 
media; 2012. p. 1 – 4 . 
[9] Speight JG. Liquid fuels from natural gas. In: Lee S, Speight JG, Loyalka SK, 
editors. Handbook of alternative fuel technologies. second ed. Oxford: Taylor and 
Francis Group; 2015. p. 157 – 78 . 
[10] Cai H, Burnham A, Chen R, Wang M. Wells to wheels: environmental implications 
of natural gas as a transportation fuel. Energy Pol 2017;109:565 – 78 . 
[11] Aslam MU, Masjuki HH, Kalam MA, Abdesselam H, Mahlia TMI, Amalina MA. An 
experimental investigation of CNG as an alternative fuel for a retrofitted gasoline 
vehicle. Fuel 2006;85(5 – 6):717 – 24 . 
[12] Einewall P, Tunestål P, Johansson B. Lean burn natural gas operation vs. 
stoichiometric operation with EGR and a three way catalyst. SAE Tech Pap 2005. 
2005-01-0250 . 
[13] Korb B, Kuppa K, Nguyen HD, Dinkelacker F, Wachtmeister G. Experimental and 
numerical investigations of charge motion and combustion in lean-burn natural 
gas engines. Combust Flame 2020;212:309 – 22 . 
[14] Li MH, Zhang Q, Li GX. Emission characteristics of a natural gas engine operating 
in lean-burn and stoichiometric modes. J Energy Eng 2015;142(3). 04015039 . 
[15] Yan BW, Wang H, Zheng ZQ, Qin YF, Yao MF. The effects of LIVC Miller cycle on 
the combustion characteristics and thermal efficiency in a stoichiometric 
operation natural gas engine with EGR. Appl Therm Eng 2017;122(25):439 – 50 . 
[16] Zeng K, Huang Z, Liu B, Liu LX, Jiang DM, Ren Y, Wang JH. Combustion 
characteristics of a direct-injection natural gas engine under various fuel injection 
timings. Appl Therm Eng 2006;26(8 – 9):806 – 13 . 
[17] Moon S. Potential of direct-injection for the improvement of homogeneous-charge 
combustion in spark-ignition natural gas engines. Appl Therm Eng 2018;136: 
41 – 8 . 
[18] Zhang D. Direct injection natural gas engines. In: Zhao H, editor. Advanced direct 
injection combustion engine technologies and development. Cambridge: 
Woodhead Publishing; 2010. p. 199 – 228 . 
[19] Meng XY, Tian H, Zhou YH, Tian JP, Long WQ, Bi MS. Comparative study of pilot 
fuel property and intake air boost on combustion and performance in the CNG 
dual-fuel engine. Fuel 2019;253:116003 . 
[20] Meng XY, Tian H, Long WQ, Zhou YH, Bi MS, Tian JP, Lee CF. Experimental study 
of using additive in the pilot fuel on the performance and emission trade-offs in 
the diesel/CNG (methane emulated) dual-fuel combustion mode. Appl Therm Eng 
2019;157:113718 . 
[21] Chown D, Habbaky C, Wallace JS. An experimental investigation of combustion 
chamber design parameters for hot surface ignition. In: ASME paper No; 2014. 
ICEF2014-5646 . 
[22] Brown BS. High-pressure direct-injection of natural gas with entrained diesel into 
a compression-ignition engine. Vancouver: Master Thesis, University of British 
Columbia; 2008 . 
[23] Ouellette P, Goudie D, McTaggart-Cowan G. Progress in the development of 
natural gas high pressure direct injection for Euro VI heavy-duty trucks. In: 
Liebl J, Beidl C, editors. Internationaler motorenkongress 2016. Wiesbaden: 
Springer Vieweg; 2016. p. 591 – 607 . 
[24] Li MH, Wu HM, Zhang TC, Shen BX, Zhang Q, Li ZG. A comprehensive review of 
pilot ignited high pressure direct injection natural gas engines: factors affecting 
combustion, emissions and performance. Renew Sustain Energy Rev 2020;119: 
109653 . 
[25] Dong Q, Li Y, Song EZ, Yao C, Fan LY, Sun J. The characteristic analysis of high 
pressure gas jets for natural gas engine based on shock wave structure. Energy 
Convers Manag 2017;149:26 – 38 . 
[26] Turner JS. The ‘starting plume ’ in neutral surroundings. J Fluid Mech 1962;13: 
356 – 68 . 
[27] Witze PO. The impulsively started incompressible turbulent jet. 1980. Sandia 
Laboratories Energy Report, SAND80-8617, Livermore, California . 
[28] Warren WR. An analytical and Experimental study of compressible free jets. In: 
Aeronautical engineering laboratory. Princeton University; 1957. Report 381 . 
[29] Ouellette P. High pressure injection of natural gas for diesel engine fueling. 
Vancouver: Master Thesis, University of British Columbia; 1992 . 
[30] Hill PG, Ouellette P. Transient turbulent gaseous fuel jets for diesel engines. 
J Fluid Eng-T ASME 1999;121(1):93 – 101 . 
[31] Ashkenas H, Sherman FS. The structure and utilization of supersonic free jets in 
low density wind tunnels. Proc 4th Int Sympos Rarefied Gas Dynam 1964;2(7): 
84 – 105 . 
[32] Crist S, Glass DR, Sherman PM. Study of the highly underexpanded sonic jet. 
AIAA J 1966;4(1):68 – 71 . 
[33] Orescanin MM, Austin JM. Exhaust of underexpanded jets from finite reservoirs. 
J Propul Power 2010;26(4):744 – 53 . 
[34] Jothi TJS, Srinivasan K. Shock structures of underexpanded non-circular slot jets. 
S ¯adhan ¯a 2019;44:25 . 
[35] Norum TD, Seiner JM. Broadband shock noise from supersonic jets. AIAA J 1982; 
20(1):68 – 73 . 
[36] Gannochenko GI, Ermolayev LS, Zadorozhnyi NA. On the position of the central 
compression shock in an underexpanded sonic jet issuing from a slot nozzle. 
J Appl Mech Tech Phys 1986;4:89 + 91 . 
[37] Carlson DJ, Lewis CH. Normal shock location in underexpanded gas and gas- 
particle jets. AIAA J 1964;2(4):776 – 7 . 
[38] Billig FS, Orth RC, Lasky M. Unified analysis of gaseous jet penetration. AIAA J 
1971;9(6):1048 – 58 . 
[39] D ’ Ambrosio L, De Socio LM, Gaffuri G. Physical and numerical experiments on an 
underexpanded jet. Meccanica 1999;34:267 – 80 . 
[40] D ’ Attore L, Harshbarger F. Parameters affecting the normal shock location in 
underexpanded gas jets. AIAA J 1965;3(3):530 – 1 . 
[41] Lewis Jr CH, Carlson DJ. Normal shock location in underexpanded gas and gas- 
particle jets. AIAA J 1964;2(4):776 – 7 . 
[42] Young WS. Derivation of the free-jet Mach-disk location using the entropy- 
balance principle. Phys Fluids 1975;18(11):1421 – 5 . 
[43] Avduevskii VS, Ivanov AV, Karpman IM, Traskovskii VD, Yudelovich MY. Flow in 
supersonic viscous underexpanded jet. Fluid Dynam + 1970;5:409 – 14 . 
[44] Finat ’ Ev YP, Shcherbakov LA, Gorskaya NM. Mach number distribution over the 
axis of supersonic underexpanded jets. J Eng Phys Thermophys 1968;15(6): 
1153 – 7 . 
[45] Driftmyer RT. A correlation of free jet data. AIAA J 1972;10:1093 – 5 . 
[46] Ewan BCR, Moodie K. Structure and velocity measurements in underexpanded 
jets. Combust Sci Technol 1986;45(5 – 6):275 – 88 . 
[47] Richard TD. A correlation of free jet data]. AIAA J 1972;10(8):1093 – 5 . 
[48] Gao W, Lin YZ, Xin H, Zhang C, Xu QH. Injection characteristics of near critical 
and supercritical kerosene into quiescent atmospheric environment. Fuel 2019; 
235:775 – 81 . 
[49] Gibbings JC, Ingham J, Johnson D. Flow in a supersonic jet expanding from a 
convergent nozzle. Aeronaut Res Council 1972. Technical report C.P.No. 1197 . 
[50] Addy AL. Effects of axisymmetric sonic nozzle geometry on Mach disk 
characteristics. AIAA J 1981;19(1):121 – 2 . 
[51] Otobe Y, Kashimura H, Matsuo S, Setoguchi T, Kim HD. Influence of nozzle 
geometry on the near-field structure of a highly underexpanded sonic jet. J Fluid 
Struct 2008;24(2):281 – 93 . 
[52] Antsupov AV. General properties of underexpanded and overexpanded supersonic 
gas jets. Sov Phys Tech Phys 1974;19(2):234 – 8 . 
[53] Murzinov LN. Similarity parameters for the escape of a strongly underexpanded 
jet into a flooded space. Fluid Dynam + 1971;6:675 – 80 . 
[54] Hatanaka K, Saito T. Influence of nozzle geometry on underexpanded 
axisymmetric free jet characteristics. Shock Waves 2012;22:427 – 34 . 
[55] Lehnasch G, Bruel P. A robust methodology for RANS simulations of highly 
underexpanded jets. Int J Numer Methods Fluid 2008;56(12):2179 – 205 . 
[56] Li Y, Kirkpatrick A, Mitchell C, Willson B. Characteristic and computational fluid 
dynamics modeling of high-pressure gas jet injection. J Eng Gas Turbines Power 
2004;126(1):192 – 7 . 
M. Li et al.

<!-- PDF_PAGE: 18 -->

Renewable and Sustainable Energy Reviews 150 (2021) 111390
18
[57] Ashraful AMM, Mahabubul AM, Shigeru M, Toshiake S, Dong KH. Numerical 
simulation of supersonic microjets. Proc Int Conf Mech Eng Dhaka: Bangladesh, 
ICME09-FM- 2009;12 . 
[58] Birkby P, Page GJ. Numerical predictions of turbulent underexpanded sonic jets 
using a pressure-based methodology. Proc Instn Mech Engrs 2001;215:165 – 73 . 
[59] Fu DB, Yu Y, Niu QL. Simulation of underexpanded supersonic jet flows with 
chemical reactions. Chin J Aeronaut 2014;27(3):505 – 13 . 
[60] Evgenevna IE, Evgenevna IT, Viktorovich BP. Analysis of the application of 
turbulence models in the calculation of supersonic gas jet. Am J Appl Sci 2014;11: 
1914 – 20 . 
[61] Li XF, Chowdhury BR, He Q, Christopher DM, Hecht ES. Validation of two-layer 
model for underexpanded hydrogen jets. Int J Hydrogen Energy 2021;46: 
12545 – 54 . 
[62] Li XF, Chen Q, Chen MJ, He Q, Christopher DM, Cheng X, Chowdhury BR, 
Hecht ES. Modeling of underexpanded hydrogen jets through square and 
rectangular slot nozzles. Int J Hydrogen Energy 2019;44:6353 – 65 . 
[63] Stewart JR. CFD modelling of underexpanded hydrogen jets exiting rectangular 
shaped openings. Process Saf Environ 2020;139:283 – 96 . 
[64] Zhang JB, Zhang X, Huang WW, Dong H, Wang T. Isentropic analysis and 
numerical investigation on high-pressure hydrogen jets with real gas effects. Int J 
Hydrogen Energy 2020;44:6353 – 65 . 
[65] Adamson TC, Nicholls JA. On the structure of jets form highly underexpanded 
nozzles into still air. J Aero Sci 1959;26:16 – 24 . 
[66] Ruggles AJ, Ekoto IW. Ignitability and mixing of underexpanded hydrogen jets. 
Int J Hydrogen Energy 2012;37(22):17549 – 60 . 
[67] Ruggles AJ, Ekoto IW. Experimental investigation of nozzle aspect ratio effects on 
underexpanded hydrogen jet release characteristics. Int J Hydrogen Energy 2014; 
39(35):20331 – 8 . 
[68] Stickland MT, Green LG, Russel C. RA98(CHAM Nozzle) flow survey of 
underexpanded supersonic jets in the 5.5m low speed wind tunnel static test 
facility-volume 2. In: British aerospace report BAe-WWt-RP-RES-AXR-139; 1988 . 
[69] Love ES, Grigsby CE, Lee LP, Woodling JM. Experimental and theoretical studies 
of axisymmetric free jets. NASA Tech Rep R-6 1959 . 
[70] Dash SM, Seiner JM, Wolf DE. Analysis of turbulent underexpanded jets. Part 1: 
parabolized Navier Stokes model, SCIPVIS. AIAA J 1985;23(4):505 – 14 . 
[71] Li X, Chen M, Wang Y, Hu J, Sun Z, Christopher DM, Cheng L. Measurements of 
concentration decays in underexpanded jets through rectangular slot nozzles. Int 
J Hydrogen Energy 2018;43(20):9884 – 93 . 
[72] Cheng TS, Lee KS. Numerical simulations of underexpanded supersonic jet and 
free shear layer using WENO schemes. Heat Fluid Flow 2005;26:755 – 70 . 
[73] Velikorodny A, Kudridkov S. Numerical study of the near-field of highly 
underexpanded turbulent gas jets. Int J Hydrogen Energy 2012;37(22):17390 – 9 . 
[74] Liu JH, Kailasanath K, Ramamurti R, Munday D, Gutmark E. Large-eddy 
simulations of a supersonic jet and its near-field acoustic properties. AIAA J 2009; 
47(8):1849 – 64 . 
[75] Munday D, Gutmark E, Liu J, Kailasanath K. Flow structure and acoustics of 
supersonic jets from conical convergent-divergent nozzles. Phys Fluids 2011;23: 
116102 . 
[76] Munday D, Gutmark E, Liu J, Kailasanath K. Flow and acoustic radiation from 
realistic tactical jet C-D nozzles. In: 14
th 
AIAA/CEAS aeroacoustics conference. 
Vancouver: British Columbia; 2008. p. 2008 – 838 . 
[77] Vuorinen V, Yu J, Tirunagari S, Kaario O, Larmi M, Duwig C, Boersma BJ. Large- 
eddy simulation of highly underexpanded transient gas jets. Phys Fluids 2013;25. 
016101 . 
[78] Yu JZ, Vuorinen V, Kaario O, Sarjovaara T, Larmi M. Visualization and analysis of 
the characteristics of transitional underexpanded jets. Int J Heat Fluid Flow 2013; 
44:140 – 54 . 
[79] Vuorinen V, Wehrfritz A, Duwig C, Boersma BJ. Large-eddy simulation on the 
effect of injection pressure and density on fuel jet mixing in gas engines. Fuel 
2014;130:241 – 50 . 
[80] Zhang HH, Chen ZH, Li BM, Jiang XH. The secondary vortex rings of a supersonic 
underexpanded circular jet with low pressure ratio. Eur J Mech B Fluid 2014;46: 
172 – 80 . 
[81] Li XP, Wu K, Yao W, Fan XJ. A comparative study of highly underexpanded 
nitrogen and hydrogen jets using large eddy simulation. Int J Hydrogen Energy 
2016;41:5151 – 61 . 
[82] Li XP, Fan E, Yao W, Fan XJ. Numerical investigation of characteristic frequency 
excited highly underexpanded jets. Aero Sci Technol 2017;63:304 – 16 . 
[83] Hamzehloo A, Aleiferis PG. Gas dynamics and flow characteristics of highly 
turbulent under-expanded hydrogen and methane jets under various nozzle 
pressure ratios and ambient pressures. Int J Hydrogen Energy 2016;41:6544 – 66 . 
[84] Cui W, Xu JL, Wang BC, Zhang P, Qin QH. The initial flow structures and 
oscillations of an underexpanded impinging jet. Aero Sci Technol 2021;115: 
106740. https://doi.org/10.1016/j.ast.2021.106740 . 
[85] Yu JZ, Vuorinen V, Hillamo H, Sarjovaara T, Kaario O, Larmi M. An experimental 
study on high pressure pulsed jets for DI gas engine using planar laser-induced 
fluorescence. SAE Tech Pap 2012. 2012-01-1655 . 
[86] Zare-Behtash H, Kontis K, Takayama K. Compressible vortex loops studies in a 
shock tube with various exit geometries. In: 46th AIAA aerospace sciences 
meeting and exhibit; 2008. Reno, Nevada, AIAA2008-A2362 . 
[87] Meng Y. High speed pulsed schlieren technology and its application to flow 
visualization in supersonic combustion. Master ’ s thesis, institute of mechanics, 
Chinese academy of science; 2012 [in Chinese] . 
[88] Henderson BB, Bridges J, Wernet M. An experimental study of the oscillatory flow 
structure of tone-producing supersonic impinging jets. J Fluid Mech 2005;542: 
115 – 37 . 
[89] Mtui P. Pilot-ignited natural gas combustion in diesel engines. Vancouver: Doctor 
Thesis, University of British Columbia; 1996 . 
[90] Ouellette P. Direct injection of natural gas for diesel engine fueling. Vancouver: 
Doctor Thesis, University of British Columbia; 1996 . 
[91] Ouellette P, Mtui P, Hill PG. Numerical simulations of directly injected natural 
gas and pilot diesel fuel in a two-stroke compression ignition engine. In: SAE 
Technical paper No. 981400; 1998 . 
[92] Li GW, Lennox T, Goudie D, Dunn M. Modeling HPDI natural gas heavy duty 
engine combustion. In: Proceedings of the ASME 2005 internal combustion 
engine division fall technical conference. Ottawa: Canada; 2005. ICEF2005-1307 . 
[93] Han Z, Reitz RD, Corcione FE, Valentino G. Interpretation of k- ε computed 
turbulence length-scale predictions for engine flows. Sympos (Int) Combust 1996; 
26(2):2717 – 23 . 
[94] Yang X, Gupta S, Kuo TW, Gopalakrishnan V. RANS and large eddy simulation of 
internal combustion engine flows — a comparative study. J Eng Gas Turbines 
Power 2014;136(5). 051507 . 
[95] Baratta M, Misul D, Spessa E, Viglione L, Carpegna G, Perna F. Experimental and 
numerical approaches for the quantification of tumble intensity in high- 
performance SI engines. Energy Convers Manag 2017;138:435 – 51 . 
[96] Lee WG, Montgomery D. Numerical investigation of the performance of a high 
pressure direct injection (HPDI) natural gas engine. In: Proceedings of the ASME 
2014 internal combustion engine division fall technical conference; 2014. 
ICEF2014 – 5681 . 
[97] Li MH, Zhang Q, Li GX, Li PX. Effects of hydrogen addition on the performance of 
a pilot-ignition direct-injection natural gas engine: a numerical study. Energy 
Fuel 2017;31(4):4407 – 23 . 
[98] Li MH, Zhang Q, Liu XR, Ma YX, Zheng QP. Soot emission prediction in pilot 
ignited direct injection natural gas engine based on n-heptane/toluene/methane/ 
PAH mechanism. Energy 2018;163:660 – 81 . 
[99] Li MH, Zheng XL, Zhang Q, Li ZG, Shen BX, Liu XR. The effects of partially 
premixed combustion mode on the performance and emissions of a direct 
injection natural gas engine. Fuel 2019;250:218 – 34 . 
[100] Li MH, Wei ZN, Liu XR, Wang XY, Zhang Q, Li ZG. A numerical investigation on 
the effects of gaseous fuel composition in a pilot ignited direct injection natural 
gas engine. Energy 2021;217:119467 . 
[101] Liu J, Zhao HB, Wang JL, Zhang N. Optimization of the injection parameters of a 
diesel/natural gas dual fuel engine with multi-objective evolutionary algorithms. 
Appl Therm Eng 2019;150. 70-19 . 
[102] Liu J, Ma B, Yu RG, Guo Q. Optimization of the direct injection natural gas engine 
under different combustion modes. Fuel 2020;272:117699 . 
[103] Faghani E, Kheirkhah P, Mabson CWJ, McTaggart-Cowan GP, Kirchen P, Rogak S. 
Effect of injection strategies on emissions from a pilot-ignited direct-injection 
natural-gas engine- Part I: late post injection. In: SAE technical paper No; 2017. 
2017-01-0774 . 
[104] Faghani E, Kheirkhah P, Mabson CWJ, McTaggart-Cowan G, Kirchen P, Rogak S. 
Effect of Injection Strategies on Emissions from a pilot-ignited direct-injection 
natural-gas engine- Part II: slightly premixed combustion. In: SAE technical paper 
No; 2017. 2017-01-0763 . 
[105] Mabson CWJ, Faghani E, Kheirkhah P, Kirchen P, Rogak SN, McTaggart- 
Cowan GP. Combustion and emissions of paired-nozzle jets in a pilot-ignited 
direct-injection natural gas engine. In: SAE technical paper No; 2016. 2016-01- 
0807 . 
[106] Kheirkhah P. CFD modeling of injection strategies in a high-pressure direct- 
injection (HPDI) natural gas engine. Master Thesis. Vancouver: University of 
British Columbia; 2015 . 
[107] Berglund M, Fureby C. LES of supersonic combustion in a scramjet engine model. 
Proc Combust Inst 2007;31(2):2497 – 504 . 
[108] Vermorel O, Richard S, Colin O, Angelberger C, Benkenida A, Veynante D. 
Towards the understanding of cyclic variability in a spark ignited engine using 
multi-cycle LES. Combust Flame 2009;156(8):1525 – 41 . 
[109] Baum E, Peterson B, B ¨ohm B, Dreizler A. On the validation of LES applied to 
internal combustion engine flows: Part 1: comprehensive experimental database. 
Flow, Turbul Combust 2014;92(1 – 2):269 – 97 . 
[110] Liu CB, Liu CS, Ma WX. RANS, detached eddy simulation and large eddy 
simulation of internal torque converters flows: a comparative study. Eng Appl 
Comp Fluid 2015;9(1):1 – 12 . 
[111] Brownh AJ, Heywood JB. A fundamentally-based stochastic mixing model 
method for predicting NO and soot emissions from direct injection diesel engines. 
Combust Sci Technol 1988;58(1 – 3):195 – 207 . 
[112] Magnussen BF, Hjertager H. On mathematical modeling of turbulent combustion 
with special emphasis on soot formation and combustion. Sympos Combust 1977; 
16(1):719 – 29 . 
[113] Li GW, Lennox T, Goudie D, Dunn M. Modeling HPDI natural gas heavy duty 
engine combustion. In: Proceedings of the ASME 2005 internal combustion 
engine division fall technical conference; 2005. ICEF2005-1307 . 
[114] Munshi SR, McTaggart-Cowan GP, Huang J, Hill PG. Development of a partially- 
premixed combustion strategy for a low-emission, direct injection high efficiency 
natural gas engine. In: Proceedings of the ASME 2011 internal combustion engine 
division fall technical conference; 2011. ICEF2011-60181 . 
[115] Curran HJ, Gaffuri P, Pitz WJ, Westbrook CK. A comprehensive modeling study of 
n-heptane oxidation. Combust Flame 1998;114:149 – 77 . 
[116] Huang J, Bushe WK. Experimental and kinetic study of auto-ignition in methane/ 
ethane/air and methane/propane/air mixtures under engine-relevant conditions. 
Combust Flame 2006;144(1 – 2):74 – 88 . 
M. Li et al.

<!-- PDF_PAGE: 19 -->

Renewable and Sustainable Energy Reviews 150 (2021) 111390
19
[117] Bowman CT, Hanson RK, Davidson DF, Gardiner WC, Lissianski JV, Smith GP, 
Golden DM, Frenklach M, Goldenberg M. http://www.me.berkeley.edu/gr 
i_mech/. 
[118] Patel A, Kong S, Reitz R. Development and validation of a reduced reaction 
mechanism for HCCI engine simulations. In: SAE technical paper No; 2004. 2004- 
01-0558. 
[119] Mattarelli E, Rinaldini CA, Golovitchev VI. CFD-3D analysis of a light duty dual 
fuel (diesel/natural gas) combustion engine. Energy Procedia 2014;45:929–37. 
[120] Florea R, Neely GD, Abidin Z, Miwaj J. Efficiency and emissions characteristics of 
partially premixed dual-fuel combustion by co-direct injection of NG and diesel 
fuel (DI2). In: SAE technical paper No. 2016-01-0779; 2016. 
[121] Rahimi A, Fatehifar E, Saray RK. Development of an optimized chemical kinetic 
mechanism for homogeneous charge compression ignition combustion of a fuel 
blend of n-heptane and natural gas using a genetic algorithm. P I Mech Eng-J Aut 
2010;224(9):1141–59. 
[122] Jud M, Wieland C, Fink G, Sattelmayer T. Numerical analysis of the combustion 
process in dual-fuel engines with direct injection of natural gas. In: ASME 2018 
internal combustion engine division fall technical conference; 2018. ICEF2018- 
9579. 
[123] Lu TF, Law CK. Strategies for mechanism reduction for large hydrocarbons: n- 
heptane. Combust Flame 2008;154:153–63. 
[124] Niemeyer KE, Sung CJ. On the importance of graph search algorithms for DRGEP- 
based mechanism reduction methods. Combust Flame 2016;158(8):1439–43. 
[125] Rui L, He G, Zhang D, Qin F. Skeletal kinetic mechanism generation and 
uncertainty analysis for combustion of iso-octane at high temperatures. Energy 
Fuel 2018;32(3):3842–50. 
[126] Hiroyasu H, Kadota T. Models for combustion and formation of nitric oxide and 
soot in direct injection diesel engines. In: SAE technical paper No. 760129; 1976. 
[127] Omidvarborna H, Kumar A, Kim DS. Recent studies on soot modeling for diesel 
combustion. Renew Sustain Energy Rev 2015;48:635–47. 
[128] Vishwanathan G, Reitz RD. Development of a practical soot modeling approach 
and its application to low-temperature diesel combustion. Combust Sci Technol 
2010;182(8):1050–82. 
[129] Mueller E, Blanquart G, Pitsch H. A joint volume-surface model of soot 
aggregation with the method of moments. Proc Combust Inst 2009;32(1):785–92. 
[130] Liu JP, Wei MR, Xiao HL, Peng F. The effects of nucleation on soot dynamic 
evolution based on the method of moments. Appl Mech Mater 2014;529:232–6. 
[131] Zhong BJ, Dang S, Song YN, Gong JS. 3-D simulation of soot formation in a direct- 
injection diesel engine based on a comprehensive chemical mechanism and 
method of moments. Combust Theor Model 2012;16(1):143–71. 
[132] Netzell K, Lehtiniemi H, Mauss F. Calculating the soot particle size distribution 
function in turbulent diffusion flames using a sectional method. Proc Combust 
Inst 2007;31(1):667–74. 
[133] Rodrigues P, Franzelli B, Vicquelin R, Gicque O, Darabiha N. Coupling an LES 
approach and a soot sectional model for the study of sooting turbulent non- 
premixed flames. Combust Flame 2018;190:477–99. 
[134] Balthasar M, Frenklach M. Monte-Carlo simulation of soot particle coagulation 
and aggregation: the effect of a realistic size distribution. Proc Combust Inst 2005; 
30(1):1467–75. 
[135] Lucchesi M, Abdelgadir A, Attili A, Bisetti F. Simulation and analysis of the soot 
particle size distribution in a turbulent nonpremixed flame. Combust Flame 2017; 
178:35–45. 
[136] Mehta RS, Haworth DC, Modest MF. Composition PDF/photon Monte Carlo 
modeling of moderately sooting turbulent jet flames. Combust Flame 2010;157 
(5):982–94. 
[137] Shapiro A. The dynamics and thermodynamics of compressible fluid flow, vol. I. 
New York: John Wiley and Sons inc; 1951. 
M. Li et al.
