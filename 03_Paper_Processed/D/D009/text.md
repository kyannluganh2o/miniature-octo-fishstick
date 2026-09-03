<!-- PDF_PAGE: 1 -->

Combustion and Flame 244 (2022) 112271 
Contents lists available at ScienceDirect 
Combustion and Flame 
journal homepage: www.elsevier.com/locate/combustflame 
On the propagation stability of droplet-laden two-phase rotating 
detonation waves 
Haocheng Wen, Wei Wei, Wenqi Fan, Qiaofeng Xie, Bing Wang ∗
School of Aerospace Engineering, Tsinghua University, Beijing, China, 10 0 084 
a r t i c l e i n f o 
Article history: 
Received 13 August 2021 
Revised 16 June 2022 
Accepted 17 June 2022 
Available online 12 July 2022 
Keywords: 
Two-phase detonation 
Rotating detonation waves 
Droplets 
Stability criterion 
Numerical simulations 
a b s t r a c t 
The propagation characteristics and stability of droplet-laden two-phase rotating detonation waves are 
studied by theoretical analysis and numerical simulations. The stability criterion of rotating detona- 
tion waves is proposed for an annular combustor fueled by liquid kerosene, which combines the pre- 
evaporation equivalence ratio ϕpre and a dimensionless parameter /Delta1. The latter one is deﬁned as the ra- 
tio of the droplet evaporation distance L E to the detonation wave front height L D . The maximum droplet 
diameter as well as the stability boundary for the rotating detonation wave without pre-evaporation is 
found theoretically. Furthermore, numerical simulations are conducted on the two-phase rotating detona- 
tion waves produced by kerosene droplets and high-temperature air by means of the Eulerian-Lagrangian 
method. The effects of initial droplet diameter d 0 and ϕpre on the propagation characteristics of rotating 
detonation waves are analyzed. The mechanism of detonation instability and wave-quenching as d 0 and 
ϕpre exceed the stability boundary is explored. Results show that for ϕpre = 0, the droplet evaporation 
becomes longer and the rotating detonation wave tends to be less stable as /Delta1gradually increases. The 
unburned reactant pockets are generated at the detonation front and are consumed by the transverse 
detonation waves. When /Delta1is approximately equal to 1.0, the insuﬃcient evaporation leads to the for- 
mation of local larger unburned reactant pockets. If the unburned reactant zones gradually enlarge, the 
ﬂame and shock wave will be decoupled, and the detonation quenched soon. Increasing ϕpre can sig- 
niﬁcantly improve the propagation stability of detonation wave for /Delta1∼ O(1.0). The stability regime of 
droplet-laden two-phase rotating detonation waves is obtained and the above stability criterion is veri- 
ﬁed based on the simulation cases. The conclusion will inspire the optimization design of the liquid-fuel 
rotating detonation engine. 
© 2022 The Combustion Institute. Published by Elsevier Inc. All rights reserved. 
1. Introduction 
Detonation is a typical form of pressure-gained combustion in 
which the shock wave and ﬂame are coupled and propagate at 
supersonic speed. Compared with the Brayton cycle based on 
deﬂagration, the detonation-based thermodynamic cycle has 
higher cycle eﬃciency and can signiﬁcantly improve the traditional 
propulsion system performance [1] . Since 1950s, the Pulse Detona- 
tion Engine [2] , Oblique Detonation Engine [3] and Rotating Deto- 
nation Engine (RDE) [4] have been put forward and tested succes- 
sively. Among them, RDE stands out due to its great potential and 
application advantages. In recent years, beneﬁted from the deep- 
ening understanding of its characteristics and physics mechanism, 
the rotating detonation and the related propulsion technology have 
become a research hotspot. 
∗ Corresponding author. 
E-mail address: wbing@tsinghua.edu.cn (B. Wang) . 
At present, most researches on rotating detonation focus on the 
gaseous fuels, including H 2 [5–9] , CH 4 [10] , C 2 H 2 [11] , C 2 H 4 [12] , 
etc. Extant studies show that the propagation behavior and stabil- 
ity of rotating detonation are affected by multiple factors such as 
the physical-chemical properties of the reactant [13 , 14] , injection 
conditions [15–17] , and the geometric conﬁguration of combustor 
[9 , 18–20] . Additionally, a variety of unstable phenomena are iden- 
tiﬁed in the experimental and numerical studies, including counter 
two-wave detonation [5 , 17 , 21] , low frequency oscillation [5 , 21 , 22] , 
acoustic related instability [17 , 23] , etc. 
However, in consideration of the future potential propulsion de- 
vices, including the ramjet-type [24 , 25] and turbojet-type [12 , 26] 
RDE, the liquid hydrocarbon fuel is an inevitable choice. The 
droplet-laden two-phase rotating detonation combustor involves 
complex two-phase processes such as atomization, evaporation, 
mixing and their interaction with detonation waves [27] , and thus 
its working conditions and mechanism can be signiﬁcantly differ- 
ent from those of gaseous rotating detonation. A few experimen- 
tal and numerical studies have been performed using kerosene/ 
gasoline as fuel and air/oxygen-enriched air as oxidizer and pro- 
https://doi.org/10.1016/j.combustﬂame.2022.112271 
0010-2180/© 2022 The Combustion Institute. Published by Elsevier Inc. All rights reserved.

<!-- PDF_PAGE: 2 -->

H. Wen, W. Wei, W. Fan et al. Combustion and Flame 244 (2022) 1 12271 
Nomenclature 
α Distance coeﬃcient 
/Delta1 Dimensionless parameter 
κ Evaporation coeﬃcient 
ϕt Spray total equivalence ratio 
ϕpre Pre-evaporation equivalence ratio 
ϕlb Lower detonative limit 
B M Mass transfer coeﬃcient 
d Droplet diameter 
L E Droplet evaporation distance 
L D Detonation height 
˙ m Mass ﬂow rate 
P Pressure 
T Temperature 
Y Species mass fraction 
u velocity 
Pr Prandtl number 
Re Reynold number 
Nu Nusselt number 
Sh Schmidt number 
Sc Sherwood number 
Subscript 
0 Initial or stagnation status 
d Droplet parameter 
D Detonation parameter 
k Index of species 
Superscript 
¯ Average parameter 
vide a preliminary understanding on the two-phase rotating deto- 
nation. 
Bykovskii et al. [11 , 28] conducted early experiments with 
kerosene/air or oxygen-enriched air and found that the width of 
the combustor is crucial to the formation of stable rotating deto- 
nation. Recently, they carried out another experiment on the mix- 
ture of kerosene/standard air rotating detonation with the ad- 
dition of H 2 /(CO + 3H 2 ), and obtained multi-wave detonation and 
counter two-wave detonation [29] . Kindracki [30] studied the ig- 
nition and propagation process of rotating detonation waves based 
on (kerosene + H 2 )/standard air. His-result shows that without the 
addition of a small amount of H 2 , the stable and self-sustained ro- 
tating detonation can hardly form at room temperature. Wolanski 
et al. [31] adopted a special method to produce a partially pre- 
mixed mixture with preheated Jet-A/gasoline and hot air (above 
the rich ﬂammable limit). When the fuel and air temperature reach 
160 °C and 100 °C respectively, the stable rotating detonation is 
achieved without any other additives. Li et al. [32] tested differ- 
ent injection conﬁgurations in the Jet-A/standard air rotating det- 
onation combustor. The self-sustained rotating detonation formed 
when the non-premixed injection conﬁguration was used and 10% 
kerosene was pre-evaporated, while the detonation failed with 
the premixed injection conﬁguration. Zhong et al. [33] used pre- 
combustion cracked kerosene and oxygen-enriched air in their ex- 
periments and studied the effect of combustor channel width and 
injection slot width on the regime and operating boundary of ro- 
tating detonation. 
Although the aforementioned experimental studies have 
veriﬁed the feasibility of droplet-laden two-phase rotating 
detonation, limited by the experimental observation ability, it 
is necessary to performed numerical studies to further understand 
the detailed ﬂow ﬁeld structures and related mechanisms in 
the combustor. Hayashi et al. [34] applied the Eulerian–Eulerian 
method to numerically study the two-dimensional JP-10/air two- 
phase rotating detonation. The effect of multiple parameters on 
the detonation wave velocity and working limit were discussed, 
including the equivalence ratio, pre-evaporation factor and droplet 
diameter (1 ∼10 μm), etc. They found that the detonation quenches 
when the initial droplet size is greater than 4 μm and the pre- 
evaporation factor is less than 20% (with inlet air temperature of 
300 K). The formation of unburned mixture and its role in the 
detonation quenching was also analyzed. Meng et al. [35] also an- 
alyzed the inﬂuence of the pre-evaporation ratio and droplet size 
(5 ∼50 μm) on the rotating detonation of partially pre-evaporated 
C 7 H 16 and H 2 mixture with the Eulerian–Lagrangian method. 
The result showed that for large droplet sizes, some droplets are 
consumed after the detonation wave as deﬂagration, and thus the 
detonative combustion eﬃciency is reduced. Furthermore, they 
analyzed the evaporation feature of droplets in the reﬁlled zone 
and found a vapor layer near the deﬂagration surface [36] . 
The design principle of the droplet-laden two-phase rotating 
detonation combustor will beneﬁt its engineering application a lot, 
which has not been discussed in the extant researches. In the 
present study, we will propose a stability criterion of two-phase 
rotating detonation and perform multiple numerical simulations to 
validate the criterion. This stability criterion can help determine 
the critical droplet diameter d 0 and the pre-evaporation equiva- 
lence ratio ϕpre for the stable two-phase rotating detonation. Ad- 
ditionally, the simulations also show the detonation propagation 
behavior under different d 0 and ϕpre , and illustrate the mechanism 
of instability and detonation quenching. 
2. Theoretical analysis of the stability criterion 
2.1. Establishment of the stability criterion 
The real physics process in the droplet-laden two-phase ro- 
tating detonation combustor is complex. As aforementioned, the 
propagation stability of the detonation wave is affected by the 
reactant physicochemical properties, combustor geometry, injec- 
tion conﬁguration, atomization properties of liquid fuels, and many 
other factors. In order to analyze the propagation stability of 
droplet-laden two-phase rotating detonation, some assumptions 
are made as follows 
(a) An annular combustor without nozzles is considered, but the 
three-dimensional effect is ignored, and thus the combustor 
can be unrolled into a two-dimensional rectangular region; 
(b) The ignition energy is suﬃcient enough, and the 
deﬂagration-detonation-transition process is not involved, 
only the propagation stability of the rotating wave is 
considered; 
(c) The gaseous reactant and droplets are ideally premixed be- 
fore entering the combustor; the gas-phase velocity, pres- 
sure and temperature in the reﬁlled zone are uniform; 
(d) The real atomizer performance is modeled by the uni- 
form initial droplet diameter and the pre-evaporation ra- 
tio; the volume fraction of dispersed droplets is less than 
1.26 × 10 −4 and thus the droplet phase is assumed as di- 
lute; the relative velocity between the droplet and gaseous 
reactant is zero; 
(e) The droplet evaporation satisﬁes the D 2 evaporation law. 
The simpliﬁed two-dimensional combustor is shown in Fig. 1 . 
The black circles in the reﬁlled zone represent fuel droplets, and 
the size of the circle represents the droplet size. The mixture of 
air (with total pressure P 0 and total temperature T 0 ) and pre- 
evaporated fuel is injected from the combustor head, and fuel 
droplets (with initial uniformed diameter d 0 ) are fully premixed 
with the gas mixture. Deﬁne the spray total equivalence ratio ϕt 
2

<!-- PDF_PAGE: 3 -->

H. Wen, W. Wei, W. Fan et al. Combustion and Flame 244 (2022) 1 12271 
Fig. 1. Schematic of the ﬂow ﬁeld near rotating detonation front in a simpliﬁed 2D 
droplet-laden two-phase rotating detonation combustor. 
and the pre-evaporation equivalence ratio ϕpre as follows 
ϕ t = 
( ˙ m F , vapor + ˙ m F , droplets ) / ( ˙ m air Y O 2 ) 
(F / O) st 
(1) 
ϕ pre = 
˙ m F , vapor / ( ˙ m air Y O 2 ) 
(F / O) st 
(2) 
where ˙ m F , vapor , ˙ m F , droplets , ˙ m air are the mass ﬂow rate of inlet fuel 
vapor, fuel droplet and air, respectively. Y O2 is the oxygen mass 
fraction in the air. (F/O) st is the mass ratio of chemical stoichio- 
metric fuel and oxidizer. 
The fuel droplets evaporate continuously after entering the 
combustor, and thus the mass fraction of gaseous fuel and the local 
equivalence ratio ϕ in the reﬁlled zone along the x -direction grad- 
ually increase. Based on the aforementioned assumptions (c)-(e), 
the droplet diameter d in the reﬁlled zone is a function of coordi- 
nate x 
d ( x ) = 
( L E − x 
L E 
)1 / 2 
d 0 , x < L E (3) 
Here L E is the droplet evaporation distance as shown in Fig. 1 . 
The gaseous fuel species in front of the detonation is composed 
of the pre-evaporated part and the evaporated part in the reﬁlled 
zone. Therefore, the local equivalence ratio can be calculated by 
ϕ ( x ) = ϕ pre + 
[
1 −
( L E − x 
L E 
)3 / 2 ]
( ϕ t − ϕ pre ) (4) 
Obviously, ϕ( x ) increases monotonically with x when x < L E . 
Ignoring the suppression effect of droplets on detonation, the 
stability of a fully premixed droplet-laden two-phase rotating det- 
onation mainly depends on the local equivalence ratio distribution 
ϕ( x ) under the given total pressure P 0 and temperature T 0 . Hypoth- 
esize that the condition for the stable detonation of a certain re- 
actant composition is: the local equivalence ratio at x 0 ( x 0 ≤ L D ) is 
greater than the lower detonative limit ϕlb of the gaseous detona- 
tion of the same reactant composition, that is 
ϕ ( x 0 ) ≥ ϕ lb (5) 
Deﬁne 
x 0 = αL D , 0 ≤ α ≤ 1 (4) 
where L D is the height of detonation front. Substitute into Eq. (4) , 
and then the stability criterion for two-phase rotating detonation 
is obtained, as follow 
ϕ pre + 
[
1 −
(
1 − αL D 
L E 
)3 / 2 ]
( ϕ t − ϕ pre ) ≥ ϕ lb (5) 
Deﬁne a dimensionless parameter /Delta1to describe the relative ra- 
tio of the evaporation distance and detonation height 
/Delta1= 
L E 
L D 
, /Delta1> 0 (6) 
The calculation method of /Delta1will be presented in the following 
section. 
Then Eq. (5) can be further simpliﬁed as 
ϕ t − ϕ pre 
ϕ t − ϕ lb 
≤
(
1 − α
/Delta1
)−3 / 2 
(7) 
In the stability criterion Eq. (7) , ϕt is the designed parameter of 
a rotating detonation combustor. The variables α and ϕlb are non- 
linearly related to multiple parameters (including reactant compo- 
sition, P 0 and T 0 , etc.), with the limitation of ϕ lb <ϕ t . Once the re- 
actant composition and inlet conditions are given, the value of α
and ϕlb can be obtained through experimental or numerical meth- 
ods. 
2.2. The dimensionless parameter /Delta1
Based on the previous assumptions (c)-(e), the evaporation dis- 
tance L E of the droplet can be calculated by 
L E = ¯u t E = κ¯u d 2 
0 (8) 
where ¯u is the average x -velocity component of the gas mixture 
in the reﬁlled zone; к (s/m 2 ) is the evaporation coeﬃcient that is 
mainly related to the static temperature and pressure in the re- 
ﬁlled zone. 
The detonation height L D can be calculated as 
L D = 
¯u 
u D 
L y (9) 
where u D is the detonation wave velocity and L y is the y -direction 
length of the combustor. Then the dimensionless parameter /Delta1can 
be expressed by 
/Delta1= 
κ
L y / u D 
d 2 
0 (10) 
Here, the parameters к , u D and L y can be theoretically cal- 
culated for the given reactant and combustor conﬁguration. The 
evaporation coeﬃcient к for kerosene at 50 0 ∼10 0 0 K is in the or- 
der of 10 6 s/m 2 . The y -direction dimension L y for a rotating det- 
onation combustor is usually in the order of 0.1 m, and u D for 
kerosene detonation is in the order of 10 3 m/s. Therefore, the re- 
quired d 0 for /Delta1= 1.0 is in the order of 10 μm. 
2.3. Parametric analysis on the stability criterion 
Taking 
√ 
/Delta1∝ d 0 as the independent variable, the stability 
boundary of ϕpre determined by Eq. (7) under different α and ϕlb 
can be obtained, as shown in Fig. 2 . The total equivalence ratio ϕt 
is assigned by 1.0 here. The upper left zone of the boundary is the 
stable zone, and the lower right zone is the quenched zone. 
From Fig. 2 a, the critical ϕpre gradually approaches ϕlb as /Delta1
increases. As α increases, the stable zone becomes larger and the 
critical 
√ 
/Delta1(or d 0 ) becomes smaller for a given ϕpre . When α is 
equal to 1, the stable detonation can be realized in the entire pa- 
rameter range. As shown in Fig. 2 b, the stable zone shrinks signif- 
icantly when ϕlb increases. 
When 
/Delta1≤ α
1 − ( 1 − ϕ lb / ϕ t ) 2 / 3 (11) 
or 
d 0 ≤
√ 
α
1 − ( 1 − ϕ lb / ϕ t ) 2 / 3 
L y / u D 
κ (12) 
3

<!-- PDF_PAGE: 4 -->

H. Wen, W. Wei, W. Fan et al. Combustion and Flame 244 (2022) 1 12271 
Fig. 2. Stability boundary of ϕpre as a function of 
√ 
/Delta1. (a) varying α with ϕlb = 0.7 and ϕt = 1.0; (b) varying ϕlb with α = 0.1 and ϕt = 1.0. 
The stability criterion Eq. (7) is always satisﬁed. Eq. (12) is the 
droplet diameter condition of the stable two-phase rotating deto- 
nation without fuel pre-evaporation. 
2.4. Effect of non-ideal factors on stability criterion 
The deduction of stability criterion is based on some ideal as- 
sumptions, which may not be satisﬁed in real rotating detonation 
combustors. The effects of non-ideal factors on the stability crite- 
rion and the related revision are discussed in this section. 
2.4.1. Real droplet size distribution 
First, the initial droplet size is assumed as uniform, while the 
real distribution of droplet sizes can be described by the Rosin- 
Rammler distribution as follows 
R ( d p ) = e −( d p / d e ) 
n 
(13) 
Here R ( d p ) is the cumulative percent passing, which refers to 
the integral proportion of the volume of all droplets in the range 
of droplet size [0, d p ]. d e is the average droplet size. n is the distri- 
bution parameter, indicating the concentration of the distribution. 
Then the increased equivalence ratio by droplet evaporation is ex- 
pressed as 
ϕ evp = ( ϕ t − ϕ pre ) 
∫ ∞  
0 
{ [ 
1 −
(
1 − α
/Delta1( d p ) 
) 3 
2 
] 
H [ /Delta1( d p ) − α] + H [ α− /Delta1( d p ) ] 
} 
d R ( d p ) 
(14) 
where H is the Heaviside function and 
d R ( d p ) = n 
d n −1 
p 
d n 
e 
e −( d p / d e ) 
n 
d d p (15) 
Deﬁne d 0 is the equivalent uniform diameter of the droplet 
groups and satisﬁes 
1 −
(
1 − α
/Delta1( d 0 ) 
) 3 
2 
= 
∫ ∞  
0 
{ [ 
1 −
(
1 − α
/Delta1( d p ) 
) 3 
2 
] 
H [ /Delta1( d p ) − α] + H [ α− /Delta1( d p ) ] 
} 
d R ( d p ) 
(16) 
Then, d 0 is expressed as 
d 0 = 
√ 
α
1 − ( 1 − /Pi1) 2 / 3 
L y / u D 
κ (17) 
where 
/Pi1= 
∫ ∞  
0 
{ [ 
1 −
(
1 − α
/Delta1( d p ) 
) 3 
2 
] 
H [ /Delta1( d p ) − α] + H [ α− /Delta1( d p ) ] 
} 
d R ( d p ) (18) 
Fig. 3. Effect of parameters n and α on the variation of de/d0. 
Fig. 4. Schematic of 2D unrolled droplet-laden two-phase rotating detonation com- 
bustor and inlet conﬁguration. 
From Eq. (17) , d 0 is a function of d e and affected by the multiple 
parameters. For a speciﬁc combustor, the values of к , u D , and L y can 
be estimated. Given к = 10 6 s/m 2 , u D = 1750 m/s, and L y = 0.1 m, 
the relationship of d 0 , d e , n and αis illustrated in Fig. 3 . The value 
of d e / d 0 is approximately in the range of (0.7, 1.3) when d 0 varies 
from 4 μm to 10 μm. When n approaches ∞  , that is the droplet 
size distribution is more concentrated, d e / d 0 tends to be equal to 
1.0. Fig. 3 shows that the estimation error of α also has small im- 
pact of d e / d 0 . The larger α leads to smaller d e / d 0 , but the value of 
d e / d 0 is still in the vicinity of 1.0. Therefore, when the real droplet 
4

<!-- PDF_PAGE: 5 -->

H. Wen, W. Wei, W. Fan et al. Combustion and Flame 244 (2022) 1 12271 
Fig. 5. Temperature contour of the rotating detonation with different d0 (2–5 μm). 
Fig. 6. Cellular structure of the rotating detonation with different d0 (2–5 μm). 
distribution is considered, the required droplet average size d e can 
be obtained by Eq. (17) without a large estimation error. 
2.4.2. Start-up process of atomizer 
Given assumption (c), the response rates of fuel and air injec- 
tors during the start-up process of atomizer are assumed as the 
same in this study, which may be different in the real combustors. 
If the injection response of fuel is faster than that of air, a small 
amount of fuel droplets will be injected into the burned gas af- 
ter the detonation wave, and thus the fuel mass fraction and the 
equivalent ϕt in the reﬁlled zone will be reduced. According to 
Eq. (7) , the minimum ϕpre for the stable detonation propagation 
will be increased. However, because the pressure decreases rapidly 
after the detonation wave, the starting process is much shorter 
when compared with the detonation propagation period. There- 
fore, the mass fraction of droplets injected into the burned gas is 
very small, indicating that ϕpre does not change a lot. 
Based on the theoretical analysis in this section and neglect- 
ing the non-ideal factors, the two variables d 0 and ϕpre are cho- 
sen and their effects on the stability and propagation characteris- 
tics of droplet-laden two-phase rotating detonation are numerically 
studied. The instability and quenching mechanism when the vari- 
ables are beyond the stability boundary is analyzed. Furthermore, 
the numerical results verify the proposed stability criterion. 
3. Numerical method 
3.1. Governing equations 
Assume the fuel droplets in the ﬂow ﬁeld are sparse, and 
thus the two-way coupling Eulerian-Lagrangian method is used to 
simulate two-dimensional kerosene/air rotating detonation in this 
study. The continuous phase is solved by the compressible, multi- 
species, reactive Navier-Stokes equations, as follows 
∂ρ
∂t 
+ ∇ · ( ρu ) = S M (19) 
∂ ( ρu ) 
∂t 
+ ∇ ·[ u ( ρu ) ] + ∇ p = ∇ · τ + S F (20) 
∂ ( ρE ) 
∂t 
+ ∇ ·[ ( ρE + p ) u ] = ∇ · ( τ · u ) + ∇ · q + S E (21) 
∂ ( ρY k ) 
∂t 
+ ∇ ·[ ( ρY k ) u ] = ∇ · ( ρD k ∇ Y k ) + ˙ ω k + S Y k (22) 
Here ρis the density, u is the velocity vector, T is the gas-phase 
temperature, p is the pressure and satisﬁes the ideal gas equation 
p = ρRT , τ is the viscous stress tensor, E is the total energy. Y k and 
˙ ω k are the mass fraction and net production rate of k th species 
(C 10 H 20 , CO, CO 2 , O 2 , N 2 ) respectively. The thermal diffusion ﬂux q 
consists of thermal diffusion caused by temperature gradient and 
component diffusion 
q = λ∇ T −
N s ∑  
k =1 
ρh k D k ∇ Y k (23) 
where λis the thermal conductivity of gas phase, h k is the sensible 
enthalpy of k th species and D k is the transport coeﬃcient. 
The source terms S M , S F , S E , S Y k in the governing Eqs. (16) - 
(22) are calculated by averaging the mass, momentum, mass and 
species change caused by all N d droplets in a single gas-phase grid. 
The expressions are as follows, 
S M = − 1 
/Delta1V 
∑  
N d 
˙ m d (24) 
5

<!-- PDF_PAGE: 6 -->

H. Wen, W. Wei, W. Fan et al. Combustion and Flame 244 (2022) 1 12271 
Fig. 7. Mass fraction contour of fuel vapor for case B2 (each black point represents a droplet). 
Fig. 8. Distribution of (a) fuel vapor mass fraction and (b) temperature in the x-direction at the front of detonation. 
S F = − 1 
/Delta1V 
∑  
N d 
( F d + ˙ m d u d ) (25) 
S E = − 1 
/Delta1V 
∑  
N d 
(
Q d + ˙ m d 
( u d · u d 
2 
+ h vp 
))
(26) 
S Y k = 
{ 
− 1 
/Delta1V 
∑ 
N d 
˙ m d for kerosene 
0 for other species 
(27) 
where ˙ m d is the droplet mass change rate, u d is the droplet ve- 
locity vector, /Delta1V is the volume (or surface) of a single gas-phase 
grid, F d is the drag force vector of the droplet, Q d is the convective 
heat transfer with gas phase, h vp and is the sensible enthalpy of 
kerosene vapor. 
For the discrete phase, the mass-point model of droplets is con- 
sidered in the present study, which means the droplet is dilute and 
the collision and coalescence among droplets are ignored. The in- 
dividual droplet is released and traced in the Lagrangian trajectory 
model. Then the governing equations of the discrete phase are as 
follows. 
d x d 
d t 
= u d (28) 
d u d 
d t 
= 
F d 
m d 
(29) 
d T d 
d t 
= 
Q d + ˙ m d L V 
m d c L 
(30) 
d m d 
d t 
= − ˙ m d (31) 
where x d is the droplet position vector, T d is the droplet tempera- 
ture, and c L is the speciﬁc heat of liquid fuel. L V is the latent heat 
6

<!-- PDF_PAGE: 7 -->

H. Wen, W. Wei, W. Fan et al. Combustion and Flame 244 (2022) 1 12271 
Fig. 9. Enlarged detail of temperature and pressure contour near the detonation front for Case B4. 
Fig. 10. Proﬁles of the maximum pressure in y-direction near the detonation front for Case A0, B2, B3 and B4. 
of evaporation and the empirical formula given by Watson [37] is 
used in the calculation 
L V = L V , T B 
(
T C , L − T d 
T C , L − T B 
) 0 . 38 
(32) 
where T B is the liquid boiling temperature in the standard state 
and T C,L is the critical temperature of the liquid. 
The high-order conservative scheme WENOLF [38] with ﬁfth- 
order accuracy is applied for the convection term in governing 
Eqs. (19) - (22) of the continuous phase. The viscous diffusion term 
is discretized by the sixth-order central difference scheme. The Roe 
Reimann solver is adopted. The unsteady term is integrated by the 
third-order Runge-Kutta method. The chemical term in Eq. (22) is 
calculated with the implicit method. 
7

<!-- PDF_PAGE: 8 -->

H. Wen, W. Wei, W. Fan et al. Combustion and Flame 244 (2022) 1 12271 
Fig. 11. Schematic of the releasing position of tracked particles for case B4. 
In order to solve the governing Eqs. (28) - (31) of the discrete 
phase, the gas phase properties (i.e. velocity, temperature and 
species) at the droplet location are required, which are obtained by 
the fourth-order Lagrange interpolation method. The second-order 
Adams-Bashforth method is adopted for the unsteady terms. The 
two-way coupling of S M , S F , S E , S Y k between the two phases is cal- 
culated for each time step. 
The aforementioned methods are achieved in our in-house 
codes which have been used to investigate multiple problems on 
the compressible reacting ﬂow [39 , 40] . 
3.2. Discrete phase models 
3.2.1. Drag force model 
Only the aerodynamic drag force is included in the study, ig- 
noring the Saffman force, thermophoretic force, and Basset force 
on the droplet. Then F d in the discrete phase Eq. (29) can be ex- 
pressed by 
F d = m d 
(
f 1 
τd 
)
(u − u d ) (33) 
The characteristic relaxation time τd is 
τd = 
ρd d 2 
18 μ (34) 
The correction coeﬃcient f 1 for Stokes’s law based on experi- 
mental data is 
f 1 = Re d 
24 
(
24 
Re d 
(
1 + 0 . 15 Re 0 . 687 
d 
)
+ 0 . 42 
1 + 42500 Re −1 . 16 
d 
)
Re d ≤ 2 ×10 5 (35) 
where Re d is 
Re d = 
ρ| u − u d | d 
μ (36) 
3.2.2. Heat transfer model 
Since the droplet diameter used in the study is small enough 
( d 0 < 10 μm), it is assumed that the internal temperature of the 
Fig. 12. Variation of droplet temperature, surrounding gas temperature and droplet diameter squared during the evaporation process for Case B4. 
8

<!-- PDF_PAGE: 9 -->

H. Wen, W. Wei, W. Fan et al. Combustion and Flame 244 (2022) 1 12271 
fuel droplet is instantaneously balanced. The convective heat trans- 
fer Q d is calculated by 
Q d = m d c L 
(
f 2 
τd 
) ( Nu 
3 Pr 
)( c p 
c L 
)
(T − T d ) (37) 
The Prandtl number of gas phase Pr and Nusselt number Nu are 
as follows, 
Pr = 
μc p 
λ , Nu = 2 + 0 . 552 Re 0 . 5 
d 
1 / 3 
Pr (38) 
f 2 is the correction coeﬃcient for the convective heat transfer 
caused by droplet evaporation. 
f 2 = 
β
e β − 1 
(39) 
The dimensionless evaporation coeﬃcient β is deﬁned as 
β = −1 . 5 Pr τd 
(
˙ m d 
m d 
)
(40) 
3.2.3. Evaporation model 
The droplet mass change rate ˙ m d in Eq. (30) is calculated by 
˙ m d = m d 
( 1 
τd 
) (
Sh 
3 Sc 
)
ln (1 + B M ) (41) 
where the Schmidt number Sc and Sherwood number Sh are as 
follows 
Sc = 
μ
ρD 
, Sh = 2 + 0 . 552 Re 0 . 5 
d S c 1 / 3 (42) 
The mass transfer coeﬃcient B M is 
B M = 
Y sf − Y V 
1 − Y sf 
(43) 
where Y v is the fuel vapor mass fraction of the gas phase at the 
droplet position. Y sf is calculated by 
Y sf = 
χsf 
χsf + (1 − χsf ) W/ W V 
(44) 
where W is the mole mass of gaseous mixture at the droplet po- 
sition. W V is the mole mass of the fuel vapor. The fuel vapor mole 
fraction at the droplet surface χsf is 
χsf = 
p atm 
p 
exp 
(
L V 
R u / W V 
(
1 
T B , L 
− 1 
T d 
))
(45) 
where p atm = 101.325 kPa. T B,L is the liquid boiling temperature at 
ambient pressure P (unit: mmHg) and is calculated by the empiri- 
cal formula of Sato [41] 
T B , L = 
(
P 0 . 119 − 22 . 4 
11 . 9 
) 1 / 0 . 119 
(46) 
3.3. Chemical reaction model 
The real composition of kerosene is complex. In this study, the 
substituted composition (C 10 H 20 ) given by Franzelli et al. [42] and 
the two-step reactions as follows are adopted. The ignition de- 
lay time predicted by this model is in good agreement with the 
experimental data in a wide range of parameters ( p ∈ [1, 12] atm, 
T 0 ∈ [90 0, 160 0] K and equivalence ratio ϕ∈ [0.5, 2]), indicating that 
this model is suitable for the detonation simulation. 
C 10 H 20 + 10 O 2 ⇒  10 CO + 10 H 2 O (47) 
CO + 0 . 5 O 2 ⇔  C O 2 (48) 
Table 1 
Parameters for C 10 H 20 two-step reactions (unit: mol, cm 3 and cal/mol). 
Reaction A E a n 
(41) 8.00 × 10 11 4.15 × 10 4 n 11 = 0.55, n 12 = 0.90 
(42) 4.50 × 10 10 2.00 × 10 4 n 21 = 1.00, n 22 = 0.50 
The forward reaction rates k 1 and k 2 of reaction (41) and (42) 
are 
k 1 = A 1 b 1 (ϕ) exp (− E 1 /RT ) [ C 10 H 20 ] n 11 [ O 2 ] n 12 (49) 
k 2 = A 2 b 2 (ϕ) exp (− E 2 /RT ) [ CO ] n 21 [ O 2 ] n 22 (50) 
where A is the pre-exponential factor, E a is the activation energy, 
n is the reaction exponent. b 1 and b 2 are the correction factors for 
reaction rates based on equivalence ratio [42] . The detailed param- 
eters are listed in Table 1 . 
The validation for the above chemical reaction model and nu- 
merical method can refer to Appendix A. 
4. Physics model and simulation set-up 
4.1. Rotating detonation combustor model 
Figure 4 shows the schematic of two-dimensional (2D) unrolled 
rotating detonation combustor and its inlet conﬁguration. The up- 
per and lower boundaries are periodic boundaries, the left bound- 
ary is the reactant inlet, and the right boundary is the outlet with 
an ambient pressure of 100 kPa. The detonation propagates from 
bottom to up. The physical sizes of the computation domain are 
0.08 m and 0.10 m in the x - and y - direction, respectively. Based 
on the grid sensitivity analysis (see Appendix B), the uniform grid 
size is chosen as 50 μm. 
The reactant inlet boundary refers to the inlet model given by 
Fievisohn et al. [43] , taking into account the pressure loss of gas 
phase due to the expansion from the plenum to combustor. The 
expansion ratio ( Fig. 4 ) is set as A 1 / A 3 = 5.0, where A 1 is the injec- 
tion slit width and A 3 is the combustor channel width. 
Kerosene droplets (black circles in Fig. 4 ) with uniform diame- 
ter d 0 are released from the inlet and fully mixed with the pre- 
mixed gas before entering the calculation domain. The aerody- 
namic thermal parameters ( u d and T d ) are set as the same as the 
local gas phase, suggesting that this is no slip between the droplets 
and gas at the inlet. 
4.2. Simulation cases 
Based on the typical working conditions of RDEs [24 , 25] , the 
inlet total pressure and temperature are taken as P 0 = 700 kPa and 
T 0 = 900 K. The total equivalence ratio ϕt in the present study is 
ﬁxed at 1.0. Case A0 with fully pre-evaporated fuel ( ϕ pre = ϕ t = 1) 
is ﬁrstly simulated and selected as the baseline (see Appendix C). 
Then, the rest of cases with different droplet initial diameter d 0 
and pre-evaporation equivalence ratio ϕpre are calculated based on 
Case A0. All the simulation cases are listed in Table 2 . 
5. Parametric analysis on the propagation characteristics and 
stability 
5.1. Effects of initial droplet diameter d 0 
The droplet evaporation can be inﬂuenced by multiple factors, 
including the droplet diameter, droplet temperature, ambient tem- 
perature and pressure, and the slip velocity of droplet and gas. The 
9

<!-- PDF_PAGE: 10 -->

H. Wen, W. Wei, W. Fan et al. Combustion and Flame 244 (2022) 1 12271 
Fig. 13. Temperature contour of case B5 during the detonation quenching process. 
Fig. 14. Detonation cellular structure of B5 showing the quenching process. 
most important factor d 0 (2–5 μm) is involved in this section. The 
fuel pre-evaporation for all cases in this section is zero. 
Temperature distribution and cellular structure of the rotating 
detonation with different d 0 are compared in Fig. 5 and Fig. 6 . Due 
to the small droplet size (2 μm) of Case B2, the droplets can evap- 
Table 2 
Parameters for simulation case (P0 = 700 kPa). 
Case d 0 (μm) ϕpre ϕt 
A0 0 1.0 1.0 
B2 2 0 
B3 3 0 
B4 4 0 
B5 5 0 
C2 5 0.2 
C3 0.3 
C4 0.4 
C5 0.5 
C6 0.6 
orate in a short distance and the ﬂow ﬁeld structure is similar to 
Case A0. From the distribution of fuel vapor and droplets ( Fig. 7 ), it 
can be conﬁrmed that the evaporation distance L E is indeed much 
smaller than the detonation height L D . 
Figure 8 shows the distribution curves of fuel vapor mass frac- 
tion and temperature in front of the detonation wave. As the 
droplet size increases, the evaporation distance becomes longer 
and a larger zone with low equivalence ratio forms near the inlet 
boundary. As a result, the rotating detonation shown in Fig. 6 and 
Fig. 7 tends to less stable. For case B4, because the local equiv- 
alence ratio in the vicinity of the inlet is too low to reach the 
detonative limit, a shock wave forms instead of the detonation 
wave, followed by an unburned reactant zone (see Fig. 9 ). Fur- 
thermore, the unburned reactant pockets are generated from the 
detonation front, and the shock wave and reaction zone are de- 
coupled in these cores. The unburned reactant can be re-ignited 
10

<!-- PDF_PAGE: 11 -->

H. Wen, W. Wei, W. Fan et al. Combustion and Flame 244 (2022) 1 12271 
Fig. 15. Comparison of temperature distribution in the combustor under different ϕpre . 
Fig. 16. Comparison of detonation cellular structure under different ϕpre . 
Fig. 17. Mass fraction contour of fuel vapor for Case C5 (each black point represents a droplet). 
11

<!-- PDF_PAGE: 12 -->

H. Wen, W. Wei, W. Fan et al. Combustion and Flame 244 (2022) 1 12271 
Table 3 
Propagation parameters of rotating detonation under different /Delta1( ϕpre = 0). 
Case A0 B2 B3 B4 B5 
/Delta1 / 0.13 ∼O(0.1) 0.31 ∼O(0.1) 0.55 > O (0.1) 0.84 ∼O(1) 
u D (m/s) 1774 1728 1696 1618 Failed 
λc (mm) 1.13 1.63 1.83 2.04 Failed 
and consumed by a strong transverse detonation wave ( Fig. 9 ). 
As shown in the detonation cellular structure ( Fig. 6 ), the high- 
pressure stripes can be identiﬁed and these structures strengthen 
as the droplet size increases. This fact indicates that the transverse 
detonation wave (TDW) with greater intensity than the transverse 
waves forms and propagates in the combustor. The TDW propa- 
gates rapidly downstream and ﬁnally attenuates after entering the 
burned zone. 
Table 3 shows the statistics of the cell size and detonation ve- 
locity under different /Delta1. The calculation method of detonation cell 
size and detonation velocity can refer to Appendix B. Obviously, as 
the droplet diameter increases, the detonation propagation tends 
to be unstable, the detonation velocity decreases, and the cell size 
gradually increases. 
The proﬁles of the maximum pressure in the y -direction 
near the detonation front for Case A0, B2–4 are com- 
pared in Fig. 10 . The maximum pressure is calculated by 
P y ,max (x) = max 
y det − δ≤ y ≤ y det + δ
P ( x , y ) , where y det is the y -coordinate 
of detonation wave front and δ = 0.2 L y . It can be seen that as 
the droplet diameter increases, the number of pressure peaks de- 
creases, indicating that the cell size becomes larger. In comparison, 
the average pressure ¯p on the detonation front does not change 
much for these cases. In Fig. 10 d, a strong peak denoting the 
TDW appears near the inlet boundary. Compared with ordinary 
transverse waves, the dimension of TDW is larger and a large-scale 
unburned reactant pocket exists in the vicinity. 
In order to study the dynamics behavior of droplets, three 
droplets (Particle A-C) are released at different positions ( y = 0.02, 
0.04 and 0.06 m) at the combustor inlet of Case B4 ( Fig. 11 ), and 
are tracked in the Lagrangian coordinate system. 
The variation of main droplet variables during the droplet life 
cycle is given in Fig. 12 . Particle A encounters the shock wave 
shortly after entering the combustor. The surrounding gas temper- 
ature rises rapidly from 900 K to 20 0 0 K and the evaporation rate 
accelerates. Therefore, the survival time of Particle A is the short- 
est, namely 7.6 μs. Particle B is located in the reﬁlled zone at the 
initial moment. Before traversing the detonation wave, Particle B 
follows the D 2 evaporation law and its diameter squared decreases 
linearly. Later, Particle B encounters the detonation wave and the 
surrounding gas temperature rises from 800 K to 30 0 0 K and com- 
pletely evaporates at 16 μs. Particle C has the longest survival time 
of 21 μs because its release location is furthest away from the det- 
onation wave. 
The rotating detonation cannot self-sustain when the droplet 
diameter is larger than 4 μm. For Case B5, the detonation quenches 
soon after the fuel droplets inject instead of the fuel vapor and 
the temperature contour in Fig. 13 shows this quenching process. 
At t = 0.01 ms, the local equivalence ratio near the inlet be- 
comes extremely low after the droplets inject. In this region, the 
chemical reaction rate signiﬁcantly decreases, causing the local de- 
coupling of the leading shock wave and ﬂame. Sequentially, the 
detonation height gradually becomes shorter, while the upstream 
unburned zone becomes larger. Finally, the leading shock and 
ﬂame are completely decoupled and the detonation is extinguished 
at 0.04 ms. 
Fig. 14 shows the cellular structure showing the detonation 
quenching process. In the initial stage of stable detonation, the det- 
Table 4 
Propagation parameters of rotating detonation under different ϕpre ( /Delta1= 0.84). 
Case C2 C3 C4 C5 C6 A0 
ϕpre 0.2 0.3 0.4 0.5 0.6 1.0 
u D (m/s) Failed Failed 1686 1701 1711 1774 
λc (mm) Failed Failed 2.31 1.45 1.27 1.13 
onation cell is relatively regular. Afterwards, the transverse wave 
near the inlet boundary attenuates and the cellular structure be- 
comes irregular. Finally, when the detonation quenches, the cellu- 
lar structure disappears. 
5.2. Effects of pre-evaporation equivalence ratio ϕpre 
The pre-evaporation of fuel droplets can facilitate the formation 
and stable propagation of the rotating detonation. In this section, 
ﬁve cases C2-C6 with ϕpre varying from 0.2 to 0.6 are calculated to 
study the effect of ϕpre on the detonation propagation. The initial 
droplet diameter is set to 5 μm in this section. The detailed calcu- 
lation parameters are listed in Table 2 . Among these cases, the sta- 
ble rotating detonation is achieved for case C4-C6 ( ϕpre = 0.4, 0.5 
and 0.6), while the detonation quenches for C2 and C3 ( ϕpre = 0.2 
and 0.3). 
Figure 15 and 16 show the temperature contour and cellu- 
lar structure of the combustor under different ϕpre . The propaga- 
tion of the detonation wave becomes more stable when ϕpre in- 
creases and the cellular structure becomes less evident. For Case 
C5, the droplet evaporation distance L E is close to the detona- 
tion height L D as shown in Fig. 17 . However, due to the presence 
of pre-evaporation, the local equivalence ratio at the inlet is high 
enough to maintain the stable propagation of the detonation wave 
and numerous fuel droplets are consumed behind the detonation 
front. 
There are two signiﬁcant differences between Case C4 and A0 
on the temperature distribution and cellular structure. On the one 
hand, an unburned zone exists near the triple point in Case C4. The 
main reason is that the fresh gaseous mixture expands and accel- 
erates after entering the combustor, which can be seen in Fig. 18 
showing the x- velocity component contour. Additionally, the relax- 
ation effect of droplets in Case B4 is stronger due to the larger 
droplet diameter and the acceleration of droplets will be slower 
than that of the gas. Therefore, only a small amount of droplets 
evaporate in the vicinity of the contact surface at the reﬁlled side 
and a low equivalence ratio zone is generated ( Fig. 18 ). Conse- 
quently, the shock wave is decoupled with the ﬂame in this region. 
On the other hand, the high-pressure strips indicating the trans- 
verse waves appear in the cellular structure of Case C4. By com- 
paring Figs. 19 and 9 , it is found that there are more but smaller 
unburned cores on the detonation front of Case C4 than that of 
Case B4. 
Table 4 lists the detonation propagation parameters of the 
above cases. It is clear that the detonation velocity increases and 
the cell size becomes smaller as ϕpre increases, indicating the det- 
onation propagation tends to be more stable. 
The pressure distributions on the detonation front for the above 
cases are shown in Fig. 20 . When increasing ϕpre , the number 
12

<!-- PDF_PAGE: 13 -->

H. Wen, W. Wei, W. Fan et al. Combustion and Flame 244 (2022) 1 12271 
Fig. 18. Contours of temperature, x-velocity component (unit: m/s), and fuel vapor mass fraction for Case C4. 
Fig. 19. Enlarged detail of temperature and pressure contour near the detonation front for Case C4. 
of pressure peaks increase, indicating the smaller cell size. Three 
transverse waves exist in Case C4, while the transverse waves ob- 
viously attenuate and the pressure ﬂuctuation weakens as ϕpre in- 
creases 
Fig. 21 shows the detonation quenching process of Case C2. De- 
spite the pre-evaporation, the local equivalence ratio near the inlet 
is still insuﬃcient. Therefore, the intensity of the transverse waves 
is too weak to support the stable detonation propagation. Eventu- 
ally, similar to Case B5 ( Fig. 13 ) the unburned zone on the deto- 
nation front enlarges gradually and the detonation quenches in the 
end. 
Although the detonation quenching phenomena as shown in 
Case C2 and Case B5 are both due to the insuﬃcient droplet evapo- 
ration, the detonation propagation characteristics before quenching 
show some differences when comparing Case B4 ( Fig. 6 ) and Case 
C4 ( Fig. 16 ). For Case B4, because d 0 is smaller, droplets can rapidly 
evaporate after the strong TDW to support the detonation propa- 
gation. When d 0 increases to 5 μm, the droplet evaporation rate is 
much lower to support strong TDWs. The detonation propagation 
is more dependent on the pre-evaporation. Therefore, the intensity 
Table 5 
Propagation parameters of gaseous rotating detonation under different ϕt. 
Case A1 A2 A0 
ϕt 0.7 0.8 1.0 
u D (m/s) Failed 1715 1774 
λc (mm) Failed 1.14 1.13 
of transverse detonation wave of Case C4 is much weaker than that 
of Case B4. 
5.3. Validation of the stability criterion 
In order to obtain the lower detonative limit ϕlb for gaseous 
kerosene rotating detonation, the complementary calculations of 
the fully pre-evaporated cases are made for ϕpre = ϕt = 0.7 and 
0.8 (see Appendix C). The detailed results are given in Table 5 , from 
which the lower detonative limit is determined as ϕlb = 0.7. 
Furthermore, supplementary calculations are made for d 0 = 6.0, 
7.5, 10 μm and different ϕpre to obtain the stability regime of 
13

<!-- PDF_PAGE: 14 -->

H. Wen, W. Wei, W. Fan et al. Combustion and Flame 244 (2022) 1 12271 
Fig. 20. Proﬁles of the maximum pressure in y-direction near the detonation front for Case C4, C5, C6 and A0. 
Fig. 21. Temperature contour and fuel mass fraction contour during the detonation quenching process of Case C2. 
14

<!-- PDF_PAGE: 15 -->

H. Wen, W. Wei, W. Fan et al. Combustion and Flame 244 (2022) 1 12271 
Fig. 22. Stability regime of the droplet-laden two-phase rotating detonation as a 
function of d0 ( 
√ 
/Delta1) and ϕpre . The circle ◦represents the case where the detonation 
propagates stably. The cross × represents the case where the detonation quenches 
in the end. The solid red line is the working limit expressed by Eq. (7) . 
Fig. 23. Distribution of fuel vapor mass fraction at the front of detonation for stable 
cases near the working limit. 
droplet-laden two-phase rotating detonation. Fig. 22 shows all the 
calculation cases with the variation of d 0 and ϕpre . The stable case 
is denoted by ◦and the quenched case is denoted by × . When the 
droplet diameter is small enough ( d 0 ≤ 4 μm), the self-sustained 
detonation can be achieved without pre-evaporation. When d 0 is 
larger, the required ϕpre for the stable detonation increases. 
Fig. 23 shows the instantaneous distribution of fuel vapor mass 
fraction in front of detonation along the x -direction for stable cases 
near the working limit, where the horizontal and vertical dash 
lines represent the ϕlb = 0.7 and x / L D = 0.4, respectively. It can 
be concluded from Fig. 23 that the stable propagation of rotating 
detonation needs to meet 
ϕ ( 0 . 4 L D ) ≥ ϕ lb (51) 
Assign ϕt = 1.0, ϕlb = 0.7 and α = x/L D = 0.4 into Eq. (7) , the 
stability boundary simpliﬁed as 
ϕ pre ≥ 1 − 0 . 3 
(
1 − 0 . 4 
/Delta1
)−3 / 2 
(52) 
which is given by the solid red line in Fig. 22 . Obviously, this red 
line precisely divides Fig. 22 into the stable and quenched region, 
which shows the reliability of the criterion. 
Assign ϕpre = 0 into Eq. (52) , we obtain 
/Delta1≤ 0 . 72 (53) 
This is the requirement for stable kerosene two-phase rotat- 
ing detonation without pre-evaporation at P 0 = 700 kPa and 
T 0 = 900 K. 
6. Conclusion 
The propagation stability of droplet-laden two-phase rotating 
detonation waves is analyzed, and a theoretical stability criterion 
is proposed via analyzing the droplet evaporation process and lo- 
cal equivalence ratio distribution in the reﬁlled zone. The criterion 
is related to the reactant properties, inlet conditions, and spray pa- 
rameters, and is validated through the numerical simulations. The 
propagation characteristics and the detonation quenching are ana- 
lyzed for different initial droplet diameters d 0 and pre-evaporation 
equivalence ratios ϕpre . The main conclusions are as follows. 
The stability criterion is formulated as a function of ϕpre and a 
dimensionless parameter /Delta1, which describes the relative dimen- 
sion of the droplet evaporation distance L E and the detonation 
height L D . By simplifying the expression of /Delta1, it is found to be pro- 
portional to d 0 2 . The other parameters in the criterion, including 
the parameter α and the lower limit ϕlb for the kerosene/air det- 
onation, can signiﬁcantly affect the stability boundary of droplet- 
laden two-phase rotating detonation and are determined by the 
numerical method in the study. 
The numerical result shows that for the cases without pre- 
evaporation, when /Delta1on the order of 0.1, the detonation can propa- 
gate stably. As /Delta1increases, the detonation becomes less stable and 
an unburned reactant pocket is formed on the detonation front. 
The unburned reactant can be reignited by a strong transverse det- 
onation wave (TDW). When /Delta1is close to unity, a large area of un- 
burned reactant appears near the combustor inlet and gradually 
expands, eventually leading to the detonation quenching. The pa- 
rameter /Delta1is mainly related to d 0 , which is ranged from 2 to 10 μm 
in this study. 
In order to improve the stability of rotating detonation at /Delta1≥
O (1.0), the droplet pre-evaporation is considered. It is found that 
the relaxation effect of the droplets results in the formation of a 
low equivalence ratio zone near the detonation triple point, where 
the fuel vapor does not reach the detonative limit and extends to 
the downstream of the combustor to form an unburned band. With 
the decrease of ϕpre , multiple smaller unburned reactant pockets 
and weaker TDWs reappear on the detonation front. The intensity 
of TDW continues to decrease for lower ϕpre . When ϕpre is smaller 
than a critical value, the TDW cannot re-ignite the unburned reac- 
tant and the detonation quenches soon. 
Finally, the stability regime is found for the kerosene-droplet 
two-phase rotating detonation waves based on the simulation 
cases. Assign the obtained values of ϕlb and α, the stability cri- 
terion predicts the stability boundary very well in the regime. 
The two key variables d 0 and ϕpre are chosen and discussed in 
the present study, while the other parameters ϕ t , ϕ lb , α and κ in 
the stability criterion which are related to the reactant composi- 
tion and inlet condition are not analyzed here. The effect of these 
parameters will be further studied in the future work. 
Declaration of Competing Interest 
The authors declare that they have no known competing ﬁnan- 
cial interests or personal relationships that could have appeared to 
inﬂuence the work reported in this paper. 
15

<!-- PDF_PAGE: 16 -->

H. Wen, W. Wei, W. Fan et al. Combustion and Flame 244 (2022) 1 12271 
Acknowledgement 
The authors thank to the ﬁnancial support from the NSFC un- 
der the Grant No. NSAF-U1730104 & No. 51676111, and the National 
Science and Technology Major Project under the Grant No. 2017-II 
I-0 0 05-0 030. 
Appendix A: Validation of chemistry reaction model and 
numerical method 
The chemistry reaction model and numerical method are vali- 
dated through the comparison of numerical and experimental re- 
sults of kerosene/air detonation cell sizes, as shown in Fig. A.1 . The 
experiments were performed by Austin and Shepherd at the initial 
pressure and temperature of 100 kPa and 353 K [44] . The fuel used 
in the experiments is JP-10 and its molecular formula is C 10 H 16 . 
The average detonation cell size λc is obtained from the statistics 
of detonation cells in the ﬂowﬁeld. The error bar implies the max- 
imum cell size and the minimum cell size. Because the cell size 
of C 10 H 16 is larger than that of C 10 H 20 , the average numerical cell 
sizes are smaller than the experimental ones, while the error bars 
overlap. The result indicates that the chemistry reaction model and 
numerical method could conduct a reliable simulation. 
Fig. A1. Comparison of detonation cell size with the initial pressure of 100 kPa and 
initial temperature of 353 K. 
Appendix B: Grid sensitivity analysis 
The grid sensitivity analysis is conducted for three grid sizes 
/Delta1x = 50, 100, and 200 μm. As shown in Fig. A.2 , the main ﬂow 
Fig. A3. Pressure proﬁles at the inlet monitoring point of the combustor for differ- 
ent grid sizes. 
ﬁeld structures, including the detonation wave, oblique shock, and 
contact surface are similar for the three grid sizes. The transverse 
waves on the detonation front can be well simulated when adopt- 
ing the grid size of 50 μm, which is important to the detona- 
tion propagation stability. The average pressure peak increases as 
the grid size is reduced, as shown in Fig. A.3 . The pressure peaks 
for /Delta1x = 50 and 100 μm are close. When grid size of 50 μm 
is applied, the pressure peak ﬂuctuated to the transverse waves. 
The average detonation wave velocity u D can be calculated from 
Fig. A.3 by u D = L y / /Delta1t . The average velocity and its ratio to theo- 
retical Chapman-Jouguet velocity u CJ = 1772 m/s for different grid 
sizes are listed in Table A.1 . The calculation conditions for u CJ is 
400 kPa and 750 K, which are approximately equal to the gas- 
phase parameters in the reﬁlled zone of Case A0. It can be seen 
that the wave velocity is well predicted when /Delta1x = 50 μm. Based 
on the above analysis, the grid size of 50 μm is chosen to perform 
the simulations in the study. 
Table A1 
Detonation wave velocity for different grid sizes. 
/Delta1x (μm) u D (m/s) u D / u CJ 
200 1701 0.96 
100 1741 0.98 
50 1774 1.00 
Fig. A2. Numerical schlieren diagrams of the rotating detonation for3 different grid sizes of 200, 100, and 50 μm, respectively, with the same inlet conditions of Case A0. 
16

<!-- PDF_PAGE: 17 -->

H. Wen, W. Wei, W. Fan et al. Combustion and Flame 244 (2022) 1 12271 
Fig. A4. Flow structure of rotating detonation for baseline Case A0. 
Fig. A5. Pressure proﬁle at the head monitor point ( x = 2 mm, y = 50 mm) for 
Case A0. 
Appendix C: Baseline case A0 and failure case A1 
Figure A.4 shows the temperature contour of Case A0 after sev- 
eral cycles of stable detonation propagation, where the disconti- 
nuity surface A is the detonation wave front, B is the slip line, C 
is the oblique shock wave, and D is the contact surface between 
the fresh mixture and burned gas. This structure is basically the 
same as the structure of the H 2 /air rotating detonation ﬂow ﬁeld 
obtained previously [45] . 
The pressure proﬁle at the head monitor point ( x = 2 mm, 
y = 50 mm) of the combustor is shown in Fig. A.5 . The av- 
erage time interval between two pressure peaks of the ten cy- 
cles is /Delta1t = 0.0564 ms, and the average detonation velocity is 
u D = 1774 m/s. 
The pressure peak of each cycle shown in Fig. A.5 ﬂuctu- 
ates evidently and the maximum pressure peak (3.58 MPa) is ap- 
proximately 50% higher than the minimum one (2.35 MPa). The 
ﬂuctuation is mainly due to the transverse waves propagating 
at the detonation front. Fig. A.6 shows the wave system evolu- 
tion of the detonation front. At the beginning instant, the leading 
shock of the rotating detonation consists of a Mach stem (deto- 
nated as MS) and an induced shock wave (ISW). Two transverse 
waves (TWs) propagate in the opposite direction in the heat re- 
lease zone behind the leading shock. At 2.4 μs, the two transverse 
waves collide and generate a triple point (TP) where the pres- 
sure, temperature, and heat release rate signiﬁcantly increase. Sub- 
sequently, a new MS-ISW-TW structure is formed near the triple 
point. 
Figure A.7a shows the pressure contour in the vicinity of det- 
onation wave front and the local high-pressure points ( P i , i = 1, 
2, …,  6) can be clearly identiﬁed. From the pressure distribution 
proﬁle of the wave front ( Fig. A7 b), it is found that the ﬂuctua- 
tion is gradually strengthened from the inlet to the downstream. 
The cellular structure of the rotating detonation, which is clear and 
regular, can be found in Fig. A.8 . The cell size is approximately 
1.13 mm. 
When the total equivalence ratio is reduced to 0.7, the deto- 
nation cannot self-sustain. As shown in Fig. A.9 , the unburned re- 
actant zone close to the combustor inlet is continuously enlarged, 
which ﬁnally leads to the detonation quenching. 
Fig. A6. Pressure and temperature contour showing the wave system evolution of the detonation wave front. (MS - Mach Stem, ISW - Induced Shock Wave, TW - Transverse 
Wave, TP - Tripel Point). 
17

<!-- PDF_PAGE: 18 -->

H. Wen, W. Wei, W. Fan et al. Combustion and Flame 244 (2022) 1 12271 
Fig. A7. (a) Pressure contour in the vicinity of detonation wave front; (b) pressure distribution on the detonation wave front for Case A0. 
Fig. A8. Detonation cellular structure in a single cycle for Case A0. 
Fig. A.9. Temperature contour for the detonation quenching Case A1. 
18

<!-- PDF_PAGE: 19 -->

H. Wen, W. Wei, W. Fan et al. Combustion and Flame 244 (2022) 1 12271 
References 
[1] P. Wola ´nski, Detonative propulsion, Proc. Combust. Inst. 34 (2013) 125–158, 
doi: 10.1016/j.proci.2012.10.005 . 
[2] J.A. Nicholls, H.R. Wilkinson, R.B. Morrison, Intermittent detonation as a 
thrust-producing mechanism, J. Jet Propuls. 27 (1957) 534–541, doi: 10.2514/8. 
12851 . 
[3] D.T. Pratt, J.W. Humphrey, D.E. Glenn, Morphology of standing oblique 
detonation waves, J. Propuls. Power. 7 (1991) 837–845, doi: 10.2514/3. 
23399 . 
[4] J.A. Nicholls, R.E. Cullen, K.W. Ragland, Feasibility studies of a rotating detona- 
tion wave rocket motor, J. Spacecr. Rockets. 3 (1966) 893–898, doi: 10.2514/3. 
28557 . 
[5] V. Anand, A. St. George, R. Driscoll, E. Gutmark, Characterization of instabilities 
in a rotating detonation combustor, Int. J. Hydrogen Energy. 40 (2015) 16649–
16659, doi: 10.1016/j.ijhydene.2015.09.046 . 
[6] Q. Xie, H. Wen, W. Li, Z. Ji, B. Wang, P. Wolanski, Analysis of operating diagram 
for H2/Air rotating detonation combustors under lean fuel condition, Energy 
151 (2018) 408–419, doi: 10.1016/j.energy.2018.03.062 . 
[7] B.A. Rankin, D.R. Richardson, A.W. Caswell, A.G. Naples, J.L. Hoke, F.R. Schauer, 
Chemiluminescence imaging of an optically accessible non-premixed rotat- 
ing detonation engine, Combust. Flame. 176 (2017) 12–22, doi: 10.1016/j. 
combustﬂame.2016.09.020 . 
[8] S.M. Frolov, V.S. Aksenov, V.S. Ivanov, I.O. Shamshin, Large-scale hydrogen–air 
continuous detonation combustor, Int. J. Hydrog. Energy. 40 (2015) 1616–1623, 
doi: 10.1016/j.ijhydene.2014.11.112 . 
[9] H. Zhang, W. Liu, S. Liu, Effects of inner cylinder length on H2/air rotating det- 
onation, Int. J. Hydrog. Energy. 41 (2016) 13281–13293, doi: 10.1016/j.ijhydene. 
2016.06.083 . 
[10] J. Kasahara, Y. Kato, K. Ishihara, K. Goto, K. Matsuoka, A. Matsuo, I. Funaki, 
H. Moriai, D. Nakata, K. Higashino, N. Tanatsugu, Application of detonation 
waves to rocket engine chamber, in: J.-M. Li, C.J. Teo, B.C. Khoo, J.-P. Wang, 
C. Wang (Eds.), Detonation Control Propuls. Pulse Detonation Rotating Detona- 
tion Engines, Springer International Publishing, Cham (2018), pp. 61–76 . 
[11] F.A . Bykovskii, S.A . Zhdan, E.F. Vedernikov, F.A . Bykovskii, S.A . Zhdan, E.F. Ved- 
ernikov, F.A. Bykovskii, S.A. Zhdan, E.F. Vedernikov, F.A . Bykovskii, S.A . Zhdan, 
E.F. Vedernikov, Continuous spin detonations, J. Propul. Power 22 (2006) 1204–
1216, doi: 10.2514/1.17656 . 
[12] J. Higashi, S. Nakagami, K. Matsuoka, J. Kasahara, A. Matsuo, I. Funaki, H. Mo- 
riai, Experimental study of the disk-shaped rotating detonation turbine engine, 
55th AIAA Aerosp. Sci. Meet., 2017, doi: 10.2514/6.2017-1286 . 
[13] F.A . Bykovskii, S.A . Zhdan, E.F. Vedernikov, Continuous spin detonation in an- 
nular combustors, Combust. Explos. Shock Waves. 41 (2005) 449–459, doi: 10. 
1007/s10573- 005- 0055- 6 . 
[14] Q. Xie, B. Wang, H. Wen, P. Wolanski, W. He, P. Wolanski, Enhancement of 
continuously rotating detonation in hydrogen and oxygen-enriched air, Proc. 
Combust. Inst. 37 (2019) 3425–3432, doi: 10.1016/j.proci.2018.08.046 . 
[15] V. Anand, A. St. George, R. Driscoll, E. Gutmark, Analysis of air inlet and fuel 
plenum behavior in a rotating detonation combustor, Exp. Therm. Fluid Sci. 70 
(2016) 408–416, doi: 10.1016/j.expthermﬂusci.2015.10.007 . 
[16] J. Duvall, F. Chacon, C. Harvey, M. Gamba, Study of the Effects of various injec- 
tion geometries on the operation of a rotating detonation engine, 2018 AIAA 
Aerosp. Sci. Meet, American Institute of Aeronautics and Astronautics, 2018, 
doi: 10.2514/6.2018-0631 . 
[17] R. Bluemner, M. Bohon, H.-.Q. Nguyen, C.O. Paschereit, E.J. Gutmark, Inﬂuence 
of reactant injection parameters on RDC mode of operation, AIAA Scitech 2019 
Forum, American Institute of Aeronautics and Astronautics, 2019, doi: 10.2514/ 
6.2019-2021 . 
[18] A.S. George, R. Driscoll, V. Anand, E. Gutmark, A. St. George, R. Driscoll, 
V. Anand, E. Gutmark, On the existence and multiplicity of rotating detona- 
tions, Proc. Combust. Inst. 36 (2017) 2691–2698, doi: 10.1016/j.proci.2016.06. 
132 . 
[19] H. Wen, Q. Xie, B. Wang, Propagation behaviors of rotating detonation in an 
obround combustor, Combust. Flame. (2019) 210, doi: 10.1016/j.combustﬂame. 
2019.09.008 . 
[20] R.B. Driscoll, V. Anand, A.C. St. George, E.J. Gutmark, Investigation on RDE op- 
eration by geometric variation of the combustor annulus and Nozzle Exit Area, 
9th U.S. Natl. Combust. Meet. (2015), pp. 1–10. https://www.researchgate. 
net/publication/277588785 _ Investigation _ on _ RDE _ Operation _ by _ Geometric _ 
Variation _ of _ the _ Combustor _ Annulus _ and _ Nozzle _ Exit _ Area . 
[21] Q. Xie, H. Wen, W. Li, Z. Ji, B. Wang, P. Wolanski, Analysis of operating diagram 
for H2/Air rotating detonation combustors under lean fuel condition, Energy 
(2018) 151, doi: 10.1016/j.energy.2018.03.062 . 
[22] D.A. Schwer, K. Kailasanath, Feedback into mixture plenums in rotating deto- 
nation engines, 50th AIAA Aerosp. Sci. Meet. Incl. New Horizons Forum Aerosp. 
Expo., 2012, doi: 10.2514/6.2012-617 . 
[23] H. Wen, B. Wang, Experimental study of perforated-wall rotating detonation 
combustors, Combust. Flame. (2020) 213, doi: 10.1016/j.combustﬂame.2019.11. 
028 . 
[24] S. Liu, W. Liu, Y. Wang, Z. Lin, Free jet test of continuous rotating detona- 
tion ramjet engine, 21st AIAA Int. Sp. Planes Hypersonics Technol. Conf., 2017, 
doi: 10.2514/6.2017-2282 . 
[25] S.M. Frolov, V.I. Zvegintsev, V.S. Ivanov, V.S. Aksenov, I.O. Shamshin, 
D.A. Vnuchkov, D.G. Nalivaichenko, A .A . Berlin, V.M. Fomin, Wind tunnel tests 
of a hydrogen-fueled detonation ramjet model at approach air stream Mach 
numbers from 4 to 8, Int. J. Hydrog. Energy. 42 (2017) 25401–25413, doi: 10. 
1016/j.ijhydene.2017.08.062 . 
[26] A. Naples, J. Hoke, R. Battelle, M. Wagner, F. Schauer, Rotating detonation en- 
gine implementation into an open-loop T63 gas turbine engine, AIAA SciTech 
Forum - 55th AIAA Aerosp. Sci. Meet, American Institute of Aeronautics and 
Astronautics Inc., 2017, doi: 10.2514/6.2017-1747 . 
[27] J. Humble, S. Heister, Heterogeneous detonation physics as applied to high 
pressure rotating detonation engines, AIAA Scitech 2021 Forum, American In- 
stitute of Aeronautics and Astronautics Inc, AIAA (2021), pp. 1–23, doi: 10.2514/ 
6.2021-1027 . 
[28] F.A. Bykovskii, E.F. Vedernikov, Continuous detonation of a subsonic ﬂow of a 
propellant, Combust. Explos. Shock Waves. 39 (2003) 323–334, doi: 10.1023/A: 
1023800521344 . 
[29] F.A . Bykovskii, S.A . Zhdan, E.F. Vedernikov, Continuous detonation of the liquid 
kerosene—air  mixture with addition of hydrogen or syngas, Combust. Explos. 
Shock Waves. 55 (2019) 589–598, doi: 10.1134/S0010508219050101 . 
[30] J. Kindracki, Experimental research on rotating detonation in liquid fuel –
gaseous air mixtures, Aerosp. Sci. Technol. 43 (2015) 445–453, doi: 10.1016/j. 
ast.2015.04.006 . 
[31] P. Wola ´nski, W. Balicki, W. Perkowski, A. Bilar, Experimental research of liquid- 
fueled continuously rotating detonation chamber, Shock Waves 1 (2021) 3, 
doi: 10.10 07/s0 0193- 021- 01014- w . 
[32] J.M. Li, P.H. Chang, L. Li, Y. Yang, C.J. Teo, B.C. Khoo, Investigation of in- 
jection strategy for liquid-fuel rotating detonation engine, AIAA Aerosp. Sci. 
Meet. 2018, American Institute of Aeronautics and Astronautics Inc, AIAA, 2018, 
doi: 10.2514/6.2018-0403 . 
[33] Y. Zhong, Y. Wu, D. Jin, X. Chen, X. Yang, S. Wang, Investigation of rotating det- 
onation fueled by the pre-combustion cracked kerosene, Aerosp. Sci. Technol. 
95 (2019) 105480, doi: 10.1016/j.ast.2019.105480 . 
[34] A.K. Hayashi, N. Tsuboi, E. Dzieminska, Numerical study on JP-10/Air detona- 
tion and rotating detonation engine, AIAA J (2020), doi: 10.2514/1.J058167 . 
[35] Q. Meng, M. Zhao, H. Zheng, H. Zhang, Eulerian-Lagrangian modelling of ro- 
tating detonative combustion in partially pre-vaporized n-heptane sprays with 
hydrogen addition, Fuel 290 (2021) 119808, doi: 10.1016/j.fuel.2020.119808 . 
[36] Q. Meng, N. Zhao, H. Zhang, On the distributions of fuel droplets and in situ 
vapor in rotating detonation combustion with prevaporized n -heptane sprays, 
Phys. Fluids. 33 (2021) 043307, doi: 10.1063/5.0045222 . 
[37] K.M. Watson, Thermodynamics of the Liquid State, Ind. Eng. Chem 35 (1943) 
398–406, doi: 10.1021/ie5040 0a0 04 . 
[38] X.Y. Hu, N.A. Adams, C.W. Shu, Positivity-preserving method for high-order 
conservative schemes solving compressible Euler equations, J. Comput. Phys. 
242 (2013) 169–180, doi: 10.1016/J.JCP.2013.01.024 . 
[39] Z. Ren, B. Wang, G. Xiang, L. Zheng, Effect of the multiphase composition in a 
premixed fuel–air stream on wedge-induced oblique detonation stabilisation, 
J. Fluid Mech. 846 (2018) 411–427, doi: 10.1017/JFM.2018.289 . 
[40] Z. Ren, L. Zheng, Numerical study on rotating detonation stability in two- 
phase kerosene-air mixture, Combust. Flame. 231 (2021) 111484, doi: 10.1016/J. 
COMBUSTFLAME.2021.111484 . 
[41] T. Kitano, J. Nishio, R. Kurose, S. Komori, Effects of ambient pressure, gas tem- 
perature and combustion reaction on droplet evaporation, Combust. Flame. 161 
(2014) 551–564, doi: 10.1016/j.combustﬂame.2013.09.009 . 
[42] B. Franzelli, E. Riber, M. Sanjosé, T. Poinsot, A two-step chemical scheme for 
kerosene-air premixed ﬂames, Combust. Flame. 157 (2010) 1364–1373, doi: 10. 
1016/j.combustﬂame.2010.03.014 . 
[43] R.T. Fievisohn, K.H. Yu, Steady-State analysis of rotating detonation engine 
ﬂowﬁelds with the method of characteristics, J. Propuls. Power. 33 (2017) 89–
99, doi: 10.2514/1.B36103 . 
[44] J.M. Austin, J.E. Shepherd, Detonations in hydrocarbon fuel blends, Combust. 
Flame. 132 (2003) 73–90, doi: 10.1016/S0010- 2180(02)00422- 4 . 
[45] M. Hishida, T. Fujiwara, P. Wolanski, Fundamentals of rotating detonations, 
Shock Waves 19 (2009) 1–10, doi: 10.10 07/s0 0193-0 08-0178-2 . 
19
