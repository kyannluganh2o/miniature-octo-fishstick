<!-- PDF_PAGE: 1 -->

Detonation-induced dynamics of RP-3 droplet deformation and breakup
Rui Yang
a
, Qibin Zhang
a , b , *
, Qiang Xiao
a , c , d , **
, Xinru Zhang
a
, Wei Fan
a , b
a
School of Power and Energy, Northwestern Polytechnical University, Xi ’ an, 710129, PR China
b
National Key Laboratory of Science and Technology on Advanced Light-duty Gas-turbine, Xi ’ an, 710072, PR China
c
Advanced Power Research Institute of Northwestern Polytechnical University in Sichuan Tianfu New Area, Chengdu, PR China
d
Science and Technology on Altitude Simulation Laboratory, Mianyang, 621000, PR China
ARTICLE INFO
Keywords:
Liquid-fueled detonation
Secondary atomization
Droplet deformation
Droplet breakup
ABSTRACT
Liquid-fueled detonation engines have attracted increasing interest for the next-generation propulsion, high -
lighting the need to better understand the fuel droplet breakup dynamics induced by detonation. The detonation- 
induced deformation and breakup of RP-3 fuel droplets were experimentally investigated over a range of initial 
diameters (0.25 – 1.27 mm) and Mach numbers (6.03 – 7.07), with those of water droplets serving as the 
comparative results. The high-speed shadowgraphy reveals that both the RP-3 and water droplets undergo 
catastrophic breakup, with RP-3 combustion inducing distinct wake structures compared to water. Furthermore, 
the cross-stream diameter of droplets induced by detonation can be predicted using the empirical formula of d
c
/ 
d
0 
= 1 + 0.72821 t *, with the drag coefficient being C
d 
= 0.23. The nondimensional breakup time converges to 
t
b
* = 10.06 for water droplets and t
b
* = 7.90 for RP-3 droplets. These parameters deviate significantly from those 
predicted under shock-induced conditions. While the surface tension significantly affects the breakup time, its 
influence on the cross-stream diameter is relatively limited. Finally, a detonation-adapted mass stripping model 
is proposed, which can accurately predict the breakup time of the experimental results.
1. Introduction
A detonation wave [ 1 , 2 ] comprises a leading supersonic shock fol -
lowed closely by a chemical reaction zone. The compression induced by 
the shock abruptly elevates the thermodynamic conditions of the 
combustible mixture, initiating exothermic reactions that release energy 
and sustain the leading shock propagation. In the 1950s, Nicholls [ 3 ] 
proposed detonation combustion as a means to enhance thermodynamic 
cycles, which spurred extensive research into its application in propul -
sion systems [ 4 – 6 ]. These efforts have led to the development of several 
detonation-based engine concepts, including pulse detonation engine 
[ 7 , 8 ], rotating detonation engine [ 9 , 10 ], and standing detonation en -
gine. Among them, two-phase detonation engines [ 11 – 13 ] have attrac -
ted growing interest due to the advantages of liquid fuels, such as ease of 
storage and high energy density. In these systems, injectors first atomize 
the liquid into droplets [ 14 ], which subsequently undergo secondary 
breakup in the flow field, generating finer fragments that significantly 
enhance fuel evaporation and combustion. Unlike gaseous detonation, 
the two-phase detonation process is considerably more complex due to 
the dynamic behavior of dispersed liquid droplets. Among these, droplet 
breakup plays a pivotal role, as it directly governs the evaporation and 
combustion rates of the liquid fuel [ 15 ]. Therefore, further investigation 
into droplet breakup dynamics induced by the detonation wave is 
essential to better understand the operational mechanisms of two-phase 
detonation engines.
The breakup of fuel droplets promotes mixing and vaporization [ 15 ], 
which in turn influences fuel efficiency, ignition delay, and combustion 
characteristics [ 16 ]. A deeper understanding of droplet breakup dy -
namics is vital for designing propulsion systems with enhanced perfor -
mance and efficiency. Extensive research has been devoted to 
understanding the mechanisms of aerodynamic droplet breakup. In 
theoretical studies, Bellman et al. [ 17 ] derived the growth rate of the 
Rayleigh – Taylor (RT) instability by considering the effects of surface 
tension and viscosity. Reitz et al. [ 18 ] later proposed a spray breakup 
model incorporating both Kelvin – Helmholtz (KH) and RT instabilities, 
where primary breakup is dominated by KH instability and secondary 
breakup is jointly governed by KH and RT mechanisms. Experimentally, 
Reinecke et al. [ 19 ] observed RT instability on droplet surfaces induced 
by acceleration. Arcoumanis et al. [ 20 ] reported that aerodynamic 
breakup typically begins with the formation of surface waves. 
* Corresponding author. School of Power and Energy, Northwestern Polytechnical University, Xi ’ an, 710129, PR China.
** Corresponding author. School of Power and Energy, Northwestern Polytechnical University, Xi ’ an, 710129, PR China.
E-mail addresses: zhangqibin@nwpu.edu.cn (Q. Zhang), qxiao@nwpu.edu.cn (Q. Xiao). 
Contents lists available at ScienceDirect
Acta Astronautica
journal homepag e: www.else vier.com/loc ate/actaastro
https://doi.org/10.1016/j.actaastro.2025.11.013
Received 7 July 2025; Received in revised form 19 October 2025; Accepted 4 November 2025  
Acta Astronautica 239 (2026) 434–445 
Available online 7 November 2025 
0094-5765/© 2025 IAA. Published by Elsevier Ltd. All rights are reserved, including those for text and data mining, AI training, and similar technologies.

<!-- PDF_PAGE: 2 -->

Theofanous [ 21 ] further identified KH and RT instabilities as the main 
drivers of aerodynamic droplet breakup and proposed two correspond -
ing modes: Rayleigh – Taylor piercing (RTP) and shear-induced entrain -
ment (SIE). Recent studies by Sharma et al. [ 22 ] and Chandra et al. [ 23 ] 
further analyzed the growth of RT and KH instabilities on droplet sur -
faces. While the aerodynamic breakup mechanisms of droplets have 
been extensively studied, whether fuel droplets follow similar breakup 
behavior induced by detonation waves remains to be further 
investigated.
In addition to breakup mechanisms, considerable research has 
focused on spatial characteristics of droplet breakup, such as streamwise 
displacement and cross-stream diameter. Ranger et al. [ 24 , 25 ] investi -
gated the relationship between centroid displacement and time, pro -
posing a clear parabolic correlation, which suggests that droplets 
undergo uniformly accelerated motion in the flow. However, the de -
tached child droplets can obscure the main droplet, resulting in signif -
icant errors when identifying the centroid. To address this, Simpkins 
et al. [ 26 ] adopted the front stagnation point displacement instead of the 
centroid one for characterizing the droplet acceleration. Kobiera et al. 
[ 27 ] applied this approach to streamwise displacement studies, finding 
that the front stagnation point displacement also follows a parabolic 
relationship with time, consistent with the centroid displacement. 
Furthermore, Ranger et al. [ 24 ] and Hsiang et al. [ 28 ] observed that in 
the early stages of breakup, the dimensionless cross-stream diameter 
increases linearly with the dimensionless time, as further confirmed by 
Schroeder et al. [ 16 ]. Although existing studies have primarily focused 
on shock-induced breakup, the intense flow-field gradients associated 
with detonation waves may alter the spatial characteristics of fuel 
droplet breakup. This potential deviation warrants further investigation.
Although the above studies have elucidated the mechanisms of 
shock-induced droplet breakup and the variation of associated spatial 
parameters, research on droplet breakup induced by supersonic reacting 
flows remains limited. A deeper understanding of this process is crucial 
for advancing the knowledge of microscale droplet behavior in two- 
phase detonations. Dabora et al. [ 29 , 30 ] found that the propagation 
speed of two-phase detonation waves is lower than the ideal 
Chapman-Jouguet (C-J) value, with the discrepancy becoming more 
pronounced as droplet size increases. Similar findings were reported by 
Bowen [ 31 ], Papavassiliou [ 32 ], and Tangirala [ 33 ]. Musick et al. [ 15 ] 
numerically investigated two-phase detonations, focusing on how 
droplet breakup affects the cellular structure and velocity deficit. Their 
results showed that breakup shortens droplet evaporation time by over 
two orders of magnitude, underscoring its key role in two-phase deto -
nation dynamics. Young et al. [ 34 ] experimentally studied spray deto -
nations and observed a pronounced velocity deficit relative to gaseous 
detonations. They further examined droplet survival times using both 
the theoretical KH – RT and empirical WERT49 breakup models adopted 
by Musick et al. However, Musick et al. [ 15 ] noted that these models still 
show considerable deviations under detonation conditions. Thus, the 
mechanisms and characteristic parameters of detonation-induced 
droplet breakup require further experimental clarification, and 
breakup models applicable to detonation environments need refinement 
or redevelopment [ 15 ]. These studies mainly focus on the influence of 
droplet diameter on detonation wave speed, with limited investigation 
into droplet breakup dynamics. Xu et al. [ 35 ] and Huang et al. [ 36 ] 
conducted numerical simulations of droplet breakup induced by deto -
nation, analyzing the underlying breakup mechanisms. Experiments by 
Salauddin et al. [ 37 ] analyzed the droplet breakup induced by shock and 
detonation waves, showing that droplet breakup is significantly more 
extensive under detonation waves due to stronger aerodynamic effects 
and chemical reaction kinetics. However, their diagnostic techniques 
failed to capture the detailed droplet breakup process, and their inves -
tigation of the detonation-induced droplet breakup was limited to a 
single test condition, neglecting the droplet deformation in the vertical 
gas flow and streamwise acceleration under varying conditions. This 
limits a deeper understanding of detonation-induced droplet breakup 
mechanisms. Burr et al. [ 38 ] recently investigated the breakup behavior 
of small droplets (~100 μ m) under detonation-wave conditions, 
analyzing the associated flow instabilities and droplet lifetimes. How -
ever, their breakup images provided limited clarity in identifying KH- or 
RT-related surface waves and did not include key spatial parameters 
commonly emphasized in breakup dynamics. Very recently, the present 
authors [ 39 ] investigated the breakup mechanisms of water droplets 
induced by detonation waves, focusing on the cross-stream diameter and 
downstream displacement. However, their study did not include RP-3 
fuel droplets, and the full breakup process was not revealed without 
quantitative analyses of the breakup dynamics. This paper thus aims to 
address these gaps.
Gubin et al. [ 40 ] and Malik et al. [ 41 ] developed a two-phase 
detonation structure model based on two key assumptions: first, that 
child droplets detached from the parent droplet burn instantaneously; 
and second, that droplet combustion behind the CJ plane does not 
contribute to detonation wave propagation. To estimate the mass of 
droplets combusted within the CJ plane, they used the mass stripping 
equation for shock-induced droplet breakup proposed by Reinecke et al. 
[ 42 , 43 ]. However, Dabora et al. [ 30 ] found that the droplet breakup 
time induced by detonation waves is approximately twice as long as that 
under shock wave conditions. As a result, the mass stripping equation 
derived for shock waves is not applicable to detonation waves. There -
fore, a suitable mass stripping equation for droplet breakup in detona -
tion waves remains to be developed, which is also the main focus of this 
study.
To advance detonation-based propulsion, it is essential to clarify the 
mechanisms of fuel droplet breakup induced by detonation waves, as 
they directly affect fuel atomization and combustion efficiency. Thus, 
the present work investigates the detonation wave-induced droplet 
breakup dynamics of RP-3 fuel, with water droplets employed as a 
reference for comparison. High-speed shadowgraphy was used to cap -
ture detailed breakup behavior, and flow instability analysis was con -
ducted to reveal the underlying mechanisms. A comparative analysis of 
the cross-stream diameter and streamwise displacement(representing 
the droplet deformation and acceleration, respectively)was carried out 
for both RP-3 and water droplets. These results were further compared 
with those from shock-induced droplet breakup. Finally, based on the 
experimental data and the mass stripping model proposed by Reinecke 
et al. [ 42 , 43 ], a modified equation applicable to detonation wave con -
ditions was derived, which can predict the droplet breakup time in a 
good accuracy.
2. Experimental methods
2.1. Experimental setup
The experimental system used in this study is largely identical to that 
Fig. 1. Photograph of the experimental detonation tube.
R. Yang et al.                                                                                                                                                                                                                                    Acta Astronautica 239 (2026) 434–445 
435

<!-- PDF_PAGE: 3 -->

described in our previous work [ 39 ]; therefore, only a brief summary is 
provided here. A photograph of the detonation tube is shown in Fig. 1 . A 
pre-detonator was used to initiate the detonation wave. The observation 
window measures 100 mm × 100 mm. Liquid droplets were generated 
using a custom-built piezoelectric droplet generator capable of stably 
producing droplets with diameters on the order of several hundred mi -
crometers. Further details of the detonation tube and droplet generator 
are available in Ref. [ 39 ].
In detonation-induced droplet breakup experiments, the selection of 
reactants is primarily determined by their ability to sustain a stable 
detonation wave. Ethylene, one of the main pyrolysis products of 
kerosene, serves as a representative gaseous hydrocarbon fuel. 
Compared with hydrogen, ethylene exhibits lower chemical reactivity, 
making it safer to handle under laboratory conditions. Considering these 
factors, ethylene mixed with oxygen-enriched air containing 50 % O
2 
was employed to initiate the detonation wave. A gaseous equivalence 
ratio of 0.9 was chosen to establish a fuel-lean environment, ensuring 
sufficient oxidizer availability for the subsequent combustion of kero -
sene droplets.
The experimental setup is shown in Fig. 2 . Ethylene and oxygen- 
enriched air (50 % O
2
) are delivered through separate lines, premixed 
in a chamber, and introduced into the detonation tube (red and orange 
streamlines indicate ethylene and oxidizer). Flow rates are regulated by 
precision mass flow controllers (1 L/min for ethylene, 5 L/min for 
oxidizer), with a measurement uncertainty of ± 0.5 % of reading and 
± 0.1 % FS. A control module maintains and displays real-time flow with 
a resolution of ± 0.001 L/min.
Droplet breakup induced by detonation waves was visualized using 
high-speed shadowgraphy (see the image on the right side of Fig. 2 ). The 
optical setup consisted of an X150A xenon lamp, a 100 mm diameter 
convex lens, and an i-SPEED 713 high-speed camera. Two objective 
lenses, with focal lengths of 200 mm and 100 mm, were employed to 
capture different stages of droplet deformation and fragmentation. The 
200 mm lens provided detailed breakup imagery for 250 μ m water and 
270 μ m RP-3 droplets at a spatial resolution of 35 pixels/mm, while the 
100 mm lens covered the full breakup sequence under other conditions 
with a resolution of 15 pixels/mm. The camera operated at 200,000 
frames per second (fps) with an exposure time of 1 μ s. At 200,000 fps, 
the i-SPEED 713 camera recorded at a resolution of 220 × 300 pixels 
(66,000 pixels per frame; aspect ratio 11:15) using the 200 mm lens, and 
at 330 × 190 pixels (62,700 pixels per frame; aspect ratio 33:19) using 
the 100 mm lens. To monitor detonation wave intensity, PCB pressure 
transducers were positioned 195 mm and 125 mm upstream and 
downstream of the droplet generator, respectively. Pressure signals were 
logged using a DEWETRON 3020 high-speed data acquisition system at a 
sampling rate of 1 MHz. Synchronization of the droplet generator, spark 
ignition, and high-speed imaging was achieved via a control system 
based on an ESP32 microcontroller. This system utilized pulse-width 
modulation (PWM) for fine voltage regulation and precise control of 
droplet ejection. Software coordination ensured that the droplet and 
detonation wave simultaneously reached the center of the camera ’ s field 
of view.
Using the shadowgraph method, the uncertainty in droplet contour 
detection was ± 0.5 pixels, corresponding to ± 1 pixel in droplet diam -
eter. This translates to ± 28.6 μ m for droplets smaller than 300 μ m and 
± 66.7 μ m for those larger than 500 μ m, with a maximum relative un -
certainty below 13 %. The relative uncertainty decreased with 
increasing cross-stream diameter and streamwise displacement. To 
minimize measurement error, the droplet diameter, cross-stream 
diameter, and streamwise displacement were each obtained by aver -
aging more than eight repeated measurements.
2.2. Testing conditions
The experimental conditions are summarized in Table 1 , where 
Group A corresponds to water droplets and Group B to RP-3 droplets. 
Table 1 lists the Mach numbers ( Ma ) of the detonation wave for each 
case, where the Mach number is calculated based on the detonation 
Fig. 2. Experimental supply, testing, and control systems.
Table 1 
Experimental conditions for the interaction of detonation waves with water 
(Group A) and RP-3 (Group B) droplets of varying diameters. Surface tension: 
water, 0.0728 N/m; RP-3, 0.0245 N/m.
Test case Ma d (mm) u
g
(m/s) ρ
g
(kg/m
3
) We Oh
A1 6.03 0.25 1407.99 4.55 30990 0.0075
A2 6.74 0.73 1512.13 4.64 106499 0.0044
A3 7.03 0.80 1555.59 4.68 124364 0.0042
A4 6.99 0.80 1549.18 4.67 123224 0.0042
A5 6.74 0.93 1512.13 4.64 135676 0.0039
A6 6.50 1.20 1477.62 4.62 166160 0.0041
B1 6.60 0.27 1492.20 4.63 95767 0.0223
B2 6.03 0.53 1407.99 4.55 195219 0.0159
B3 6.03 0.53 1407.99 4.55 195219 0.0159
B4 7.07 0.53 1558.89 4.68 245976 0.0159
B5 6.29 0.60 1445.98 4.59 234977 0.0150
B6 6.88 0.67 1532.56 4.66 299336 0.0142
B7 7.07 0.73 1558.89 4.68 339992 0.0136
B8 6.03 1.20 1407.99 4.55 442005 0.0106
B9 6.88 1.27 1532.56 4.66 567398 0.0103
R. Yang et al.                                                                                                                                                                                                                                    Acta Astronautica 239 (2026) 434–445 
436

<!-- PDF_PAGE: 4 -->

wave speed and the speed of sound in reactants. The wave velocity is 
obtained by tracking the wavefront position in consecutive shadow -
graph frames. The speed of sound in the reactants is determined using 
the Chemical Equilibrium Applications (CEA) and is found to be 337 m/ 
s. And the CJ detonation Mach number is calculated to be 6.14. The table 
also includes the dimensionless Weber number ( We ), which represents 
the ratio of aerodynamic forces to surface tension, and the Ohnesorge 
number ( Oh ), which represents the ratio of viscous forces to surface 
tension. These non-dimensional parameters can be evaluated as 
We =
ρ
g
u
2
g
d
0
σ
(1) 
Oh =
μ
l
̅̅̅̅̅̅̅̅̅̅ ̅
ρ
l
σ d
0
√ (2) 
In Eq. (1) , ρ
g 
and u
g 
denote the density and velocity of the post- 
detonation flow, respectively. The term d
0 
represents the initial 
droplet diameter, and σ is the surface tension of the droplet. Unlike 
shocks, detonations exhibit significant density and velocity gradients in 
the post-detonation flow. Accordingly, the post-detonation density and 
velocity are estimated based on the approach proposed by Salauddin 
et al. [ 37 ], assuming an ideal Zeldovich – von Neumann – D ¨oring (ZND) 
[ 44 , 45 ] structure for the detonation wave, where a thin induction zone 
separates the shock front and the reaction zone. The induction zone flow 
density ( ρ
ind
) and velocity ( u
ind
) are determined using the experimen -
tally measured detonation Mach number and normal shock relations. 
The CJ detonation parameters ( ρ
CJ
, u
CJ
) are calculated using the CEA. All 
velocities above are given in the absolute reference frame. The density of 
the post-detonation flow is approximated as the average of the induction 
zone density and the burned gas density, i.e., ρ
g 
= ( ρ
ind 
+ ρ
CJ
)/2. 
Similarly, the post-detonation flow velocity is estimated as u
g 
= ( u
ind 
+
u
CJ
)/2. In Eq. (2) , μ
l 
and ρ
l 
represent the dynamic viscosity and density of 
the droplet, respectively. As shown in Table 1 , the Oh in this study 
ranges from 10
 2 
to 10
 3
, which is much smaller than 0.1. According to 
Hsiang et al. [ 28 ], at this range, the viscosity of the droplet has negli -
gible effect on the breakup process. Therefore, Oh will not be further 
discussed in the following sections.
Prior to calculating the Mach number, Weber number, and Ohne -
sorge number, it is essential to verify that the detonation wave propa -
gates stably through the droplet region. Fig. 3 presents the raw pressure 
data for the A5 case. The C-J detonation parameters were computed 
using CEA. Four PCB pressure sensors were employed during experi -
ments: two upstream and two downstream of the droplet generator, with 
70 mm spacing between P
1
– P
2 
and P
3
– P
4
, and 250 mm between P
2 
and 
P
3
. As shown in Fig. 3 , the wave speed was determined by dividing the 
distance between sensors by the time difference for the detonation wave 
to pass between them. Over the 390 mm pressure measurement range, 
the detonation propagation speed at different positions was close to the 
ideal C-J value with the difference less than 10 %, and did not exhibit 
any clear monotonic increasing or decreasing trend. The wave speed 
behaviors under other conditions were similar to those observed for case 
A5. Moreover, the maximum deviation between the wave speed 
measured from the shadowgraph images and that obtained from the 
pressure sensors was within 2 %, suggesting that the detonation wave 
had already propagated steadily through the droplets.
3. Results and discussion
3.1. Global observations of the deformation and breakup of RP-3 and 
water droplets
The transient droplet breakup dynamics in the A6 water case are 
analyzed as a representative example, as shown in Fig. 4 . The detonation 
wave Mach number for this case is 6.5, with a droplet diameter of 1.2 
mm and a Weber number of 16,610. Rayleigh-Taylor and Kelvin- 
Fig. 3. Detonation wave pressure and velocity at different positions for 
case A5.
Fig. 4. Breakup time dynamics of A6 water droplets. Ma = 6.50, droplet diameter = 1.20 mm, and We = 16,610.
R. Yang et al.                                                                                                                                                                                                                                    Acta Astronautica 239 (2026) 434–445 
437

<!-- PDF_PAGE: 5 -->

Helmholtz instabilities play key roles in the droplet breakup process 
[ 21 – 23 ]. The acceleration of the droplet under the post-detonation flow 
promotes the development of Rayleigh-Taylor instability (RTI) on its 
surface. RTI appears as surface waves on the droplet ’ s flattened front, 
perpendicular to the flow [ 23 ]. The post-detonation flow deflects and 
accelerates as it passes over the droplet surface. Shear forces from the 
high-speed flow induce Kelvin-Helmholtz instability (KHI) at the droplet 
interface. Surface ripples observed between the front stagnation point 
and the equator during breakup are characteristic of KHI [ 22 ]. With the 
detonation wave Mach number of 6.5, convective effects are highly 
pronounced, leading to the rapid development of the KHI. The shear 
forces induced by KHI cause the droplet to undergo mass stripping 
within a very short time (less than 10 μ s), as shown in the shadowgraph 
image at 10 μ s in Fig. 4 . However, due to the limitations in the temporal 
and spatial resolution of the imaging system, the corresponding KH 
waves were not captured at this moment. The mechanism by which KHI 
promotes droplet deformation and breakup is shown in Fig. 4 for the 
time interval between 35 μ s and 60 μ s. At 35 μ s, a distinct KH wave is 
observed near the droplet ’ s front stagnation point. This KH wave carries 
a mass of liquid, which, under the shear forces of the flow, moves toward 
the droplet ’ s equator. As a result, liquid accumulates near the equator, 
promoting droplet deformation in the vertical flow direction and 
increasing the droplet ’ s cross-stream diameter. At the same time, some 
liquid detaches from the droplet ’ s main body and further fragments into 
smaller droplets within the flow field [ 22 ]. The growth of the gas-liquid 
interface in the vertical flow direction creates favorable conditions for 
the onset of RTI [ 23 ]. At 60 μ s, an RTI develops on the droplet ’ s flattened 
front surface in the vertical flow direction. Over time, the RTI evolves, 
with both its amplitude ( h ) and wavelength ( λ ) steadily increasing. By 
105 μ s, h and λ increased from 0.46 d
0 
and 0.63 d
0 
at 60 μ s to 2.3 d
0 
and 
2.6 d
0
, respectively. At this stage, distinct piercing behavior is observed, 
as the large-amplitude, long-wavelength RT waves penetrate the 
droplet, causing significant fragmentation and triggering catastrophic 
breakup [ 39 , 46 ]. It is important to note that, due to the high Mach 
number of the detonation wave ( > 6), the shear effects of the flow are 
considerable, causing KHI to persist throughout the entire breakup 
process. In contrast, RTI primarily influences the final stage of the 
breakup.
Global observations of the time evolution of water and RP-3 droplets 
with similar Mach numbers and diameters are presented in Fig. 5 . It is 
clear that both water and RP-3 droplets follow the same breakup 
mechanism. Based on the transient evolution of liquid mass, the cata -
strophic breakup of the droplets induced by the detonation wave can be 
categorized into two stages. Stage I is characterized by the shear- 
induced breakup driven by KHI. Due to the significant difference in 
the growth rates of KHI and RTI, KHI always appears earlier than RTI, as 
is consistent with the result of Ref. [ 22 ]. Under the influence of KHI, the 
droplet undergoes shear-induced breakup, while deformation in the 
Fig. 5. Comparison of the breakup time evolution of water (Group A) and RP-3 (Group B) droplets. (a) A6: We = 166,160, Ma = 6.50, d
0 
= 1.20 mm; (b) B9: We =
567,398, Ma = 6.88, d
0 
= 1.27 mm; (c) A3: We = 113,482, Ma = 7.03, d
0 
= 0.80 mm; (d) B7: We = 339,992, Ma = 7.07, d
0 
= 0.73 mm; (e) A2: We = 106,499, Ma =
6.74, d
0 
= 0.73 mm; (f) B6: We = 106,499, Ma = 6.88, d
0 
= 0.67 mm.
Fig. 6. Enlarged views of Fig. 5 (d) and (f) at 30 μ s.
R. Yang et al.                                                                                                                                                                                                                                    Acta Astronautica 239 (2026) 434–445 
438

<!-- PDF_PAGE: 6 -->

vertical flow direction becomes increasingly pronounced, thereby 
creating favorable conditions for the onset of RTI [ 23 ]. Stage II is 
characterized by the combined effects of KHI and RTI. Following the 
onset of RTI, it progressively develops, with both wavelength and 
amplitude increasing over time. This ultimately leads to piercing, 
causing the detachment of liquid fragments, which are subsequently 
further fragmented into smaller droplets within the flow field. It is worth 
noting that in Fig. 5 (d) and (f), the red dashed line in the 30 μ s image 
marks the gas – liquid interface that is perpendicular to the flow and 
located at the droplet edge (see the enlarged views in Fig. 6 ). This 
interface position indicates that the RTI initiates from the droplet ’ s edge. 
Moreover, owing to the smaller surface tension and diameter of the RP-3 
droplets, the timescale for RT piercing is extremely short. Consequently, 
the intermediate RTI development process observed in other cases is not 
captured here; by 35 μ s, piercing has already occurred, and the resulting 
small liquid fragments have completely disintegrated.
According to the studies of Guan [ 47 ], Sembian [ 48 ], and Sharma 
[ 22 ], the region with a density gradient in the droplet wake is identified 
as the recirculation zone, as shown in the 40 μ s image in Fig. 5 (b). 
Comparing the breakup processes of water and RP-3 droplets, two 
distinct differences are observed. First, the recirculation zone in the 
wake of RP-3 droplets is more pronounced than that of water droplets. 
Second, noticeable small particles appear within the projected wake 
region of the RP-3 droplets, suggesting that they are likely entrained by 
the wake flow. It should be noted, however, that the present shadow -
graph system provides two-dimensional projection images; therefore, 
this interpretation is qualitative. The following analysis investigates the 
causes of these two differences. According to droplet stability theory 
[ 14 ], the theoretical maximum droplet diameter that can stably exist in 
a given flow field is calculated using the formula [ 37 ]: 
d
max
=
8 σ
C
d
ρ
g
u
2
r
(3) 
In Eq. (3) , σ represents the surface tension of the droplet. For RP-3 
droplets, the surface tension is 0.0245 N/m, while for water droplets, 
it is 0.0728 N/m. C
d 
is the drag coefficient, which will be calculated and 
discussed later. ρ
g 
denotes the gas density, and u
r 
is the relative velocity 
between the gas ( u
g
) and droplet ( u
d
). We adopt constant σ at the 
measurement condition. Effects of droplet – droplet interactions and local 
cloud-induced modifications of drag coefficient are not modeled; this is 
consistent with the engineering-level simplifications typically employed 
for trend comparisons [ 16 , 37 ], as a complete predictive theory for 
sprays is not available [ 14 ]. Theoretical maximum stable child droplet 
diameters ( d
max
) of RP-3 and water droplets at different instants are 
shown in Fig. 7 . Under comparable flow and droplet diameter condi -
tions, the d
max 
resulting from RP-3 breakup is much smaller than that of 
water, indicating that RP-3 droplets are more prone to undergo breakup 
and form smaller child droplets. Nevertheless, shadowgraph images 
reveal that no distinct particles are observed in the wake of water 
droplets throughout the entire breakup process, whereas for the more 
easily breakable RP-3 droplets, distinct particles appear in the wake at a 
certain instant and persist thereafter. This apparent inconsistency sug -
gests that the particles observed in the RP-3 wake are unlikely to be 
breakup-generated child droplets.
Based on the theoretically estimated d
max
, the present flow condi -
tions are capable of producing extremely fine fragments. As noted by 
Musick et al. [ 15 ], droplet breakup generates much smaller child 
droplets that evaporate rapidly, thereby shortening the parent droplet 
lifetime by nearly two orders of magnitude. Consequently, for RP-3 
droplets, the fine child droplets formed after breakup are expected to 
evaporate quickly, producing RP-3 vapor that mixes with the sur -
rounding oxidizer. The recirculation zone in the droplet wake provides 
favorable conditions for combustion of RP-3 vapor. Meanwhile, the 
post-detonation environment exhibits extremely high temperatures and 
Fig. 7. Variation of d
max 
for RP-3 and water droplets at different times.
Fig. 8. Time evolution of breakup for small diameter ( d
0 
< 300 μ m) water and RP-3 droplets. (a) A1, water, We = 30,090, Ma = 6.03, d
0 
= 250 μ m, (b) B1, RP-3, We 
= 95,767, Ma = 6.60, d
0 
= 270 μ m.
R. Yang et al.                                                                                                                                                                                                                                    Acta Astronautica 239 (2026) 434–445 
439

<!-- PDF_PAGE: 7 -->

pressures, providing abundant ignition energy. Under these combined 
conditions — fuel vapor, oxidizer, and sustained heat — it is reasonable to 
infer that local combustion occurs in the wake. This inference is further 
supported by Kauffman et al. [ 49 ], who reported that shock-induced 
combustion of fuel droplets predominantly occurs within the wake re -
gion. The combustion of RP-3 vapor creates a large density gradient in 
the recirculation zone of the RP-3 droplet wake, making it more pro -
nounced compared to water droplets. Moreover, the addition of extra 
RP-3 vapor leads to a locally rich equivalence ratio, which results in the 
formation of carbon soot particles, contributing to the presence of par -
ticles in the RP-3 droplet wake.
To evaluate whether small droplets ( d
0 
< 300 μ m) follow the same 
breakup mechanism as larger droplets discussed previously, water 
droplets under the A1 case and RP-3 droplets under the B1 case are 
analyzed, as shown in Fig. 8 . The water droplet has a diameter of 250 
μ m, with Mach and Weber numbers of 6.03 and 30,090, respectively. For 
the B1 case, the droplet diameter, Mach number, and Weber number are 
270 μ m, 6.6, and 95,767, respectively. As shown in the figure, small 
droplets follow the same catastrophic breakup mechanism as larger 
droplets, but with a shorter timescale. Furthermore, due to the higher 
We of RP-3 droplets compared to water droplets, RP-3 droplets break up 
more rapidly. Specifically, the RP-3 droplet had already undergone 
piercing by 15 μ s, whereas the water droplet showed no obvious piercing 
even at 20 μ s. At 20 μ s in Figs. 8(a) and 10 μ s in Fig. 8 (b), a gas-liquid 
interface in the vertical flow direction is observed, as indicated by the 
white dashed lines. RTI is clearly evident at this interface. However, 
similar to Fig. 5 (d) and (f), RT piercing occurs too rapidly, preventing 
the full development of RTI from being captured. By the next frame, 
piercing has already occurred, and the resulting liquid fragments are 
nearly fully fragmented.
3.2. Analysis of spatial characteristics
This section analyzes the shadow images to extract parameters that 
characterize droplet deformation and acceleration. Specifically, the 
cross-stream diameter d
c 
and streamwise displacement x are used to 
represent the droplet deformation and acceleration characteristics, 
respectively. Schematic diagrams of d
c 
and x are shown in Fig. 9 for 
clarity. The streamwise displacement characterizing droplet accelera -
tion is typically determined by the displacement of the centroid [ 21 , 50 ]. 
However, as noted in Section 3.1 , the deformation of 
detonation-induced droplets lasts only 10 μ s, after which breakup oc -
curs, causing the leeward side to become blurred and accompanied by 
mass stripping. This presents challenges in accurately determining the 
centroid. To overcome this, the displacement of the droplet ’ s front 
stagnation point is used as the streamwise displacement for analysis. 
This approach is similar to the approximation methods proposed by 
Simpkins [ 26 ] and Kobiera [ 27 ]. To reduce reading errors, each value 
was measured multiple times and the average was taken.
The wide range of droplet diameters (0.25 – 1.27 mm) leads to 
notable variations in breakup-related parameters under different con -
ditions. For the comparative analyses of the droplet break-up dynamics, 
the cross-stream diameter and streamwise displacement are normalized 
by the initial droplet diameter. The non-dimensional time is defined as 
[ 23 , 26 ]: 
t
*
=
tu
g
d
0
̅̅̅̅̅̅̅̅̅ ̅
ρ
l
/
ρ
g
√ (4) 
where t represents the absolute time. The relationship between the 
nondimensional cross-stream diameter and the nondimensional time is 
shown in Fig. 10 . It can be seen that the nondimensional cross-stream 
diameter initially increases almost linearly with nondimensional time, 
reflecting a steady deformation phase. As time advances, the growth rate 
declines and eventually reverses, resulting in a reduction in cross-stream 
diameter. This behavior is consistent with the observations of Schroeder 
et al. [ 16 ] in shock-induced droplet breakup at high Mach numbers 
( > 5.2). From the droplet evolution analysis in Section 3.1 , the initial 
linear growth stage is governed by KHI, where shear forces in the flow 
deform the droplet and increase its cross-stream diameter. As the 
gas – liquid interfacial area expands in the cross-stream direction, shear 
Fig. 9. Schematic diagram of spatial characteristic parameters.
Fig. 10. Variation of nondimensional cross-stream diameter with nondimensional time under different conditions.
R. Yang et al.                                                                                                                                                                                                                                    Acta Astronautica 239 (2026) 434–445 
440

<!-- PDF_PAGE: 8 -->

effects on the windward side weaken, suppressing further KHI devel -
opment and facilitating the onset of RTI. Accordingly, the cross-stream 
diameter growth slows. Meanwhile, RTI emerges, and interface 
piercing progressively develops, eventually leading to mass stripping 
and a subsequent decrease in cross-stream diameter.
The nondimensional cross-stream diameter data from all cases are 
then consolidated and fitted, as presented in Fig. 11 . The slope of the 
fitted line for the water droplet data (green dashed line) is 0.71438, 
which agrees well with our previous experimental results [ 39 ], showing 
a deviation of only 6.2 %. In comparison, the slope for RP-3 droplets (red 
dashed line) is 0.74577. The difference between the two slopes is 
approximately 0.03, suggesting that both water and RP-3 droplets 
exhibit a similar linear growth behavior in nondimensional cross-stream 
diameter with respect to nondimensional time. It is important to note 
that the nondimensionalization of both cross-stream diameter and time 
does not account for the influence of surface tension. Despite water 
droplets having roughly three times the surface tension of RP-3 droplets, 
the variation in nondimensional cross-stream diameter is nearly iden -
tical for both, suggesting that surface tension has a minimal effect on the 
change in cross-stream diameter. This is attributed to the fact that the 
cross-stream diameter is primarily governed by shear-induced entrain -
ment [ 22 ]. Under identical flow conditions, the entrainment velocity of 
liquid on the windward side remains essentially unchanged. Further -
more, the Weber number in the present study exceeds 30,000, indicating 
that aerodynamic forces overwhelmingly surpass surface tension effects. 
Consequently, the influence of surface tension on the cross-stream 
diameter is negligible.
The data from all cases were combined and fitted, yielding the fitted 
line shown by the blue dashed line in Fig. 11 . Nearly all experimental 
data lie within the 95 % confidence and prediction band of the fitted line 
( d
c
/ d
0 
= 1 + 0.72821 t *), demonstrating the accuracy of the empirical 
correlation. Notably, this correlation also provides good agreement with 
the experimental data on detonation-induced RP-2 droplet deformation 
reported by Salauddin et al. [ 37 ]. The black dashed line represents the 
fitted curve proposed by Schroeder et al. [ 16 ], given by d
c
/ d
0 
= 1 +
1.78 t *. While Schroeder et al. [ 16 ] investigated shock-induced droplet 
breakup, the present study focuses on breakup under detonation waves. 
As analyzed in the following subsection, the nondimensional breakup 
time for shock-induced cases is roughly half that observed under deto -
nation conditions, resulting in a shorter linear growth period in 
cross-stream diameter. Accordingly, Schroeder et al. ’ s fitted curve 
appears shorter. Comparison of the two fitted lines reveals that the slope 
in the present study is approximately 60 % lower than that of Schroeder 
et al. [ 16 ], highlighting the distinct deformation characteristics induced 
by detonation versus shock waves. This suggests that empirical corre -
lations derived from shock-induced breakup may not be directly appli -
cable to detonation-driven cases. To date, no reports in the literature 
have addressed this phenomenon.
To clarify the differences in droplet deformation induced by deto -
nation and shock waves, ZND profiles were computed under the 
experimental conditions using the SD Toolbox. Fig. 12 shows the post- 
detonation pressure distribution, alongside the post-shock profile at 
the same Mach number for comparison. Unlike the post-shock flow, the 
post-detonation flow exhibits a pronounced pressure gradient along the 
flow direction, generating a counter-flow pressure-gradient force. This 
force further decelerates the mainstream, weakening convective effects. 
Simultaneously, it slows the airflow within the boundary layer, 
increasing its thickness and reducing the velocity gradient, which in turn 
Fig. 11. Fitting of nondimensional cross-stream diameter data.
Fig. 12. Pressure profiles in the post-detonation and post-shock regions.
R. Yang et al.                                                                                                                                                                                                                                    Acta Astronautica 239 (2026) 434–445 
441

<!-- PDF_PAGE: 9 -->

suppresses shear effects. Consequently, the growth rate of the cross- 
stream diameter is lower under detonation-driven conditions than 
under shock-driven ones.
Fig. 13 presents the streamwise displacement data for droplets from 
this study, alongside displacement data under shock conditions from 
Ranger [ 25 ], Simpkins [ 26 ], Kobiera [ 27 ], and Schroeder [ 16 ], together 
with detonation-induced droplet displacement data from Salauddin 
et al. [ 37 ]. As shown, both shock and detonation waves lead to a distinct 
quadratic parabolic relationship between nondimensional streamwise 
displacement and nondimensional time. This suggests that the droplet 
undergoes uniformly accelerated motion under the influence of the flow. 
Under the influence of the detonation wave, the nondimensional 
streamwise displacement of both water and RP-3 droplets is nearly 
identical, following the curve x / d
0 
= 0.08054( t *)
2
.
Salauddin et al. [ 37 ] reported slightly larger displacement values, 
mainly due to their use of hydrogen fuel, in contrast to ethylene used in 
this study. In comparison, literature data for shock-induced droplet ac -
celeration show a significantly steeper nondimensional streamwise 
displacement curve, with a slope approximately ten times greater than 
that observed under detonation conditions. This highlights a distinct 
difference in droplet acceleration mechanisms between shock and 
detonation waves, consistent with the conclusions drawn in our previous 
work [ 39 ].
To provide an intuitive measure of acceleration variation, the 
windward drag coefficient C
d 
is employed to analyze the droplet motion 
[ 24 , 26 ]. At the initial time, the droplet is assumed to be a sphere with 
constant mass. The corresponding momentum equation is as follows 
[ 24 ]: 
1
2
C
d
ρ
g
Au
2
r
= ρ
l
Va (5) 
In Eq. (5) , A denotes the droplet cross-sectional area, V represents the 
droplet volume, and a is the droplet acceleration. Assuming the droplet 
is initially stationary, u
r 
= u
g
. This allows for further simplification, 
yielding: 
a =
3
4
C
d
u
2
g
1
d
0
ρ
l
/
ρ
g
(6) 
As mentioned earlier, the droplet experiences uniformly accelerated 
motion within the flow field. Hence, the corresponding displacement 
equation can be derived from Eq. (6) as follows: 
x
d
0
=
3
8
C
d
u
2
g
1
d
2
0
ρ
l
/
ρ
g
t
2
(7) 
By incorporating the expression for nondimensional time t *, Eq. (7)
can be rewritten as follows: 
Fig. 13. Nondimensional streamwise displacement curves from different literature sources. Displacement data for shock-induced droplets are taken from Ranger 
[ 25 ], Simpkins [ 26 ], Kobiera [ 27 ], and Schroeder [ 16 ], while detonation-induced droplet displacement data are from Salauddin et al. [ 37 ].
Fig. 14. Comparison of drag coefficient with literature data. Ranger [ 25 , 51 ], Simpkins [ 26 ], Kobiera [ 27 ], Schroeder [ 16 ], Krauss [ 52 ], and Reinecke [19] provide 
data for shock-induced droplets, while Salauddin et al. [ 37 ] report data for detonation-induced droplets.
R. Yang et al.                                                                                                                                                                                                                                    Acta Astronautica 239 (2026) 434–445 
442

<!-- PDF_PAGE: 10 -->

x
d
0
=
3
8
C
d
( t
*
)
2
(8) 
Based on Eq. (8) , the drag coefficient is extracted from Fig. 13 , with 
the results presented in Fig. 14 . The figure also includes drag coefficient 
data from Ranger [ 25 ], Simpkins [ 26 ], Kobiera [ 27 ], and Schroeder [ 16 ] 
under shock conditions, along with the fitted drag coefficient curves for 
shock-induced droplets by Ranger [ 51 ], Krauss [ 52 ], and Reinecke [ 19 ], 
as well as detonation-induced drag coefficient data reported by Sal -
auddin et al. [ 37 ]. As shown in Fig. 14 , the drag coefficient for droplets 
induced by detonation, based on both the present experimental data and 
that reported by Salauddin et al. [ 37 ], converges to an average value of 
C
d 
= 0.23, with a standard deviation of 0.069. This indicates that the 
acceleration process of droplets induced by detonation is predictable. 
Compared to the data under shock conditions, the drag coefficient for 
droplet induced by detonation is significantly reduced, being only about 
10 % of that observed under shock conditions. This finding indicates that 
the empirical drag coefficient correlations derived for shock conditions 
cannot be directly applied to detonation wave scenarios, highlighting 
the need for the present study. The difference in droplet acceleration 
between detonation and shock waves primarily stems from the adverse 
pressure-gradient force in the post-detonation flow, which weakens 
gas-phase convection and diminishes the aerodynamic force responsible 
for droplet acceleration. Additionally, this opposing pressure-gradient 
force may directly impede the acceleration of the droplet.
3.3. Droplet breakup dynamics
In this section, the dynamics of droplet breakup are examined. The 
breakup criterion follows that used by Schroeder et al. [ 16 ], defining the 
completion of breakup as the instant when no coherent liquid core is 
visible in the shadowgraph images and the droplet region appears as a 
transparent mist, indicating full disintegration of the parent droplet. 
Fig. 15 illustrates an example of the interaction between a 530 μ m RP-3 
droplet and a Mach 7.03 detonation wave. Under the shear forces of the 
high-velocity flow post-detonation, the droplet rapidly experiences mass 
stripping. At 25 μ s, RT piercing begins to develop. Under the combined 
influence of KHI and RTI, complete breakup occurs by 40 μ s. At this 
stage, the droplet – mist structure exhibits no discernible collective mass, 
as evidenced by the absence of a distinct shadow under collimated 
illumination. The breakup time is therefore estimated to lie between 35 
μ s and 40 μ s, and a representative value of 37.5 μ s is adopted to mini -
mize experimental uncertainty. The uncertainty associated with this 
breakup time measurement approach is estimated to be ± 3.0 μ s. The 
maximum relative error occurs for the 270 μ m RP-3 droplet case (17 %), 
while the minimum is 2 % for the 1.2 mm water droplet case.
The breakup times for all cases were calculated and non -
dimensionalized using Eq. (4) , as shown in Fig. 16 . The vertical axis 
represents the nondimensional breakup time, while the horizontal axis 
corresponds to the experimental condition number. As seen in Fig. 16 , 
under detonation wave conditions, the nondimensional breakup time for 
water droplets collapses to t
b
* = 10.06, whereas for RP-3 droplets, it 
collapses to t
b
* = 7.90. Nearly all the data points and their associated 
error bars fall within the 95 % prediction band of the fitted line. The 
average nondimensional breakup time for water droplets is 27 % greater 
than that for RP-3 droplets. As discussed earlier, the non -
dimensionalization of time does not account for surface tension. Under 
identical flow conditions and droplet diameters, greater surface tension 
reduces the growth rate of interfacial instabilities, thereby prolonging 
the absolute breakup time and consequently increasing the nondimen -
sional breakup time. Fig. 16 also includes the nondimensional breakup 
times for shock-induced water droplets as observed by Ranger et al. [ 24 ] 
and Reinecke et al. [ 43 ] A comparison with the present data reveals that 
the nondimensional breakup time for detonation-induced droplets is 
approximately twice that for shock-induced droplets. This finding aligns 
with the study by Dabora et al. [ 30 ], who identified dynamic pressure as 
the primary driver of droplet breakup. The pronounced pressure 
gradient in the post-detonation flow reduces the average dynamic 
pressure compared to the post-shock flow at the same Mach number, 
resulting in a longer breakup time. In addition, as discussed in Section 
3.2 , the adverse pressure-gradient force in the post-detonation flow 
weakens convection and reduces the aerodynamic force on the droplet, 
thereby also contributing to the prolonged breakup time.
The mass stripping during the breakup process can be predicted 
using the empirical equation derived by Reinecke et al. [ 42 , 43 ] from 
experimental data, as shown in Eq. (9) . This equation, validated through 
X-ray experiments [ 43 ], accurately predicts the mass variation during 
the breakup of droplets with high Weber numbers (We > 1000). It has 
also been widely applied in the study of two-phase detonations [ 37 , 40 ,
41 ]. 
m
m
0
=
1
2
(
1 + cos
(
π tu
g
t
*
b
d
0
̅̅̅̅ ̅
ρ
g
ρ
l
√
))
(9) 
In Eq (9) , m represents the remaining mass of the droplet at time t , 
and m
0 
is the initial droplet mass. It is important to note that, due to the 
significant difference in nondimensional breakup times between deto -
nation and shock wave conditions, the general form of the mass strip -
ping equation derived by Reinecke et al. [ 42 , 43 ] is not directly 
applicable to detonation waves when their nondimensional breakup 
time ( t
b
* = 3.5) is used. By substituting the nondimensional breakup 
times obtained from Fig. 16 into Eq. (9) , the mass stripping equation for 
RP-3 droplet breakup induced by detonation is provided in Eq. (10) , 
Fig. 15. Example of breakup dynamics for B4 droplet ( d
0 
= 530 μ m, Ma = 7.03, We = 245976).
Fig. 16. Nondimensional breakup times under different experi -
mental conditions.
R. Yang et al.                                                                                                                                                                                                                                    Acta Astronautica 239 (2026) 434–445 
443

<!-- PDF_PAGE: 11 -->

while the corresponding equation for water droplets is given in Eq. (11) . 
m
m
0
=
1
2
(
1 + cos
(
π tu
g
7 . 90 d
0
̅̅̅̅ ̅
ρ
g
ρ
l
√
))
(10) 
m
m
0
=
1
2
(
1 + cos
(
π tu
g
10 . 06 d
0
̅̅̅̅ ̅
ρ
g
ρ
l
√
))
(11) 
Based on Eqs. (10) and (11) , an example of the predicted mass 
variation over time for a droplet is presented in Fig. 17 . Typical cases A1, 
B1, A2, and B6 are analyzed. As shown in Fig. 17 , for droplets of similar 
diameter, the mass variation curve for RP-3 droplets is steeper, indi -
cating a higher mass stripping rate compared to water droplets and 
resulting in an earlier complete breakup. This trend is consistent with 
the experimental observations discussed previously.
Additionally, Fig. 18 (a) presents 12 representative experimental data 
sets of droplet breakup time reported by Burr et al. [ 38 ]. Fig. 18 (b) 
compares the breakup times predicted by Eqs. (10) and (11) with the 
experimental results obtained in both the present study and that of Burr 
et al. [ 38 ]. As shown in Fig. 18 (b), under the experimental conditions 
( d
0 
= 100 μ m to 1.27 mm, Ma = 4.6 to 7.07), the mass stripping equa -
tions, derived using the nondimensional breakup time for droplet 
breakup induced by detonation, reasonably predict the breakup times 
for both water and RP-3 droplets. The average prediction error relative 
to experimental data is 10.0 %.
4. Conclusions
Experiments were conducted to investigate the detonation-induced 
breakup dynamics of RP-3 droplets, with water droplets used as a 
reference. This study primarily focuses on the breakup mechanisms, the 
evolution of spatial parameters, and predictive modeling of droplet 
breakup induced by detonation. In addition, it presents a comparative 
analysis of the deformation and breakup dynamics of RP-3 and water 
droplets, as well as a comparison between detonation- and shock- 
induced breakup behavior. The main conclusions are as follows: 
(1) Both RP-3 and water droplets undergo catastrophic breakup, 
progressing from a KHI-dominated stage to a coupled KHI – RTI 
stage. A novel finding is that the combustion of RP-3 droplets 
induced by detonation produces distinct breakup wakes 
compared with inert water droplets.
(2) The deformation and acceleration behaviors of droplets can be 
quantitatively predicted. However, the prediction equations 
derived for shock wave conditions do not apply to detonation 
waves. A new predictive correlation for the cross-stream diameter 
of detonation-induced droplets was established as d
c
/ d
0 
= 1 +
0.72821 t * in the KHI-dominated stage, with the drag coefficient 
collapsing to C
d 
= 0.23. Surface tension has no significant effect 
on the cross-stream diameter.
(3) The nondimensional breakup time for water droplets induced by 
detonation collapses to t
b
* = 10.06, while for RP-3 droplets, it 
converges to t
b
* = 7.90. Surface tension significantly affects 
droplet breakup time. Moreover, detonation-induced breakup 
times are found to be nearly twice those under shock-induced 
conditions. A new mass stripping equation for droplet breakup 
induced by detonation was derived, effectively predicting the 
breakup time.
This work further clarifies the breakup mechanisms of detonation- 
induced droplets, establishes dimensionless empirical correlations for 
the cross-stream diameter and drag coefficient under detonation con -
ditions, and develops a mass-stripping equation specific to detonation- 
induced breakup. These advances highlight the significance of the pre -
sent study in deepening the understanding of microscale droplet dy -
namics in two-phase detonations.
CRediT authorship contribution statement
Rui Yang: Writing – original draft, Formal analysis, Data curation. 
Fig. 17. Mass stripping equation calculations.
Fig. 18. Verification of the mass-stripping equation. (a) Representative experimental data from Burr et al. [ 38 ] (b) Comparison of predicted breakup time with 
experimental breakup time.
R. Yang et al.                                                                                                                                                                                                                                    Acta Astronautica 239 (2026) 434–445 
444

<!-- PDF_PAGE: 12 -->

Qibin Zhang: Writing – review & editing, Conceptualization. Qiang 
Xiao: Writing – review & editing. Xinru Zhang: Data curation. Wei 
Fan: Supervision.
Declaration of competing interest
The authors declare that they have no known competing financial 
interests or personal relationships that could have appeared to influence 
the work reported in this paper.
Acknowledgments
This work is supported by National Natural Science Foundation of 
China (52176133, 52106172), Sichuan Provincial Natural Science 
Foundation (NO: 2025ZNSFSC1247), the Fundamental Research Funds 
for the Central Universities, and China Space Foundation Aerospace 
Propulsion Special Fund (KDJJ20240402010).
Data availability
The data that support the findings of this study are available from the 
corresponding author upon reasonable request.
References
[1] Q. Xiao, On the geometrical scaling of hydrocarbon detonation dynamics, Combust. 
Flame 251 (2023) 112714 .
[2] Q.Y. Meng, C. Xu, L.Q. Zhang, et al., Simulations of n-dodecane/oxygen/nitrogen 
cellular detonations, Acta Astronaut. 218 (2024) 221 – 231 .
[3] J. Nicholls, H. Wilkinson, R. Morrison, Intermittent detonation as a thrust 
producing mechanism, Jet Propuls 27 (5) (1957) 534 – 541 .
[4] Q.B. Zhang, K. Wang, J.G. Wang, et al., Experimental research on vector control 
features of a pulse detonation tube with fluidic nozzle, Aero. Sci. Technol. 116 
(2021) 106456 .
[5] J.H. Kang, F.L. Song, X. Chen, et al., Performance enhancement of rotating 
detonation afterburner through combined injection scheme, Acta Astronaut. 235 
(2025) 639 – 652 .
[6] Y. Wang, F. Chen, Y. Meng, et al., Numerical study on flow and combustion 
properties of oblique detonation engine in a wide speed range, Acta Astronaut. 226 
(2025) 637 – 647 .
[7] Q.B. Zhang, K. Wang, R.X. Dong, et al., Experimental research on propulsive 
performance of the pulse detonation rocket engine with a fluidic nozzle, Energy 
166 (2019) 1267 – 1275 .
[8] J.S. Gong, H. Ma, Experimental study on pulse detonation engine with two-phase 
inhomogeneous mixture, Int J Aerosp Eng 2020 (2020) 1 – 11 .
[9] S.B. Zhou, R. Wang, F. Liu, et al., Experimental investigation on propagation 
characteristics of rotating detonation wave fueled by diesel, Acta Astronaut. 225 
(2024) 949 – 959 .
[10] Y.W. Wu, J.X. Guo, G. Xu, et al., Wave mode observation of hydrogen/oxygen 
driven rotating detonations in the hollow and annular rotating detonation rocket 
engine, Phys. Fluids 36 (11) (2024) 115105 .
[11] Q.B. Zhang, X.Q. Qiao, W. Fan, et al., Study on operation and propulsion features of 
a pulse detonation rocket engine with secondary oxidizer injection, Appl. Therm. 
Eng. 180 (2020) 115661 .
[12] F. Wang, C. Wang, H. Zhang, et al., Semi-confined layered kerosene/air two-phase 
detonations bounded by nitrogen gas, Combust. Flame 258 (2023) 113104 .
[13] X.F. Li, J.Z. Li, Q.Y. Qin, et al., Experimental study on detonation characteristics of 
liquid kerosene/air rotating detonation engine, Acta Astronaut. 215 (2024) 
124 – 134 .
[14] A.H. Lefebvre, V.G. McDonell, Atomization and Sprays, second ed., CRC Press, 
Boca Raton, 2017 .
[15] B.J. Musick, M. Paudel, P.K. Ramaprabhu, et al., Numerical simulations of droplet 
evaporation and breakup effects on heterogeneous detonations, Combust. Flame 
257 (2023) 113035 .
[16] S. Schroeder, S. Salauddin, A. Morales, et al., Deformation and aerobreakup of RP-2 
droplets from hypersonic shock waves, Proc. Combust. Inst. 40 (1 – 4) (2024) 
105338 .
[17] R. Bellman, R.H. Pennington, Effects of surface tension and viscosity on Taylor 
instability, Q J Appl Math 12 (1954) 151 – 162 .
[18] J.C. Beale, R.D. Reitz, Modeling spray atomization with the Kelvin-Helmholtz/ 
Rayleigh-Taylor hybrid model, Atomization Sprays 9 (1999) 623 – 650 .
[19] W.G. Reinecke, W.L. McKay, Experiments on water drop breakup behind Mach 
3 – 12 shocks, Tech Rep, AVCO Everett Research Lab (1969) .
[20] C. Arcoumanis, L. Khezzar, D.S. Whitelaw, et al., Breakup of Newtonian and non- 
Newtonian fluids in air jets, Exp. Fluid 17 (6) (1994) 405 – 414 .
[21] T.G. Theofanous, Aerobreakup of Newtonian and viscoelastic liquids, Annu. Rev. 
Fluid Mech. 43 (1) (2011) 661 – 690 .
[22] S. Sharma, A.P. Singh, S.S. Rao, et al., Shock induced aerobreakup of a droplet, 
J. Fluid Mech. 929 (2021) A27 .
[23] N.K. Chandra, S. Sharma, S. Basu, et al., Shock-induced aerobreakup of a polymeric 
droplet, J. Fluid Mech. 965 (2023) A1 .
[24] A.A. Ranger, J.A. Nicholls, Aerodynamic shattering of liquid drops, AIAA J. 7 (2) 
(1969) 285 – 290 .
[25] A.A. Ranger, J.A. Nicholls, Atomization of liquid droplets in a convective gas 
stream, Int. J. Heat Mass Tran. 15 (6) (1972) 1203 – 1211 .
[26] P.G. Simpkins, E.L. Bales, Water-drop response to sudden accelerations, J. Fluid 
Mech. 55 (4) (1972) 629 – 639 .
[27] A. Kobiera, J. Szymczyk, P. Wola ´nski, et al., Study of the shock-induced 
acceleration of hexane droplets, Shock Waves 18 (2009) 475 – 485 .
[28] L.P. Hsiang, G.M. Faeth, Near-limit drop deformation and secondary breakup, Int. 
J. Multiphas. Flow 18 (5) (1992) 635 – 652 .
[29] K.W. Ragland, E.K. Dabora, J.A. Nicholls, Observed structure of spray detonations, 
Phys. Fluids 11 (11) (1968) 2377 – 2388 .
[30] E.K. Dabora, K.W. Ragland, J.A. Nicholls, Drop-size effects in spray detonations, 
Symp (Int) Combust 12 (1) (1969) 19 – 26 .
[31] J.R. Bowen, K.W. Ragl, F.J. Steffes, et al., Heterogeneous detonation supported by 
fuel fogs or films, Symp (Int) Combust 13 (1) (1971) 1131 – 1139 .
[32] J. Papavassiliou, A. Makris, R. Knystautas, et al., Measurements of cellular 
structure in spray detonation, Prog. Astronaut. Aeronaut. 154 (1993) 148 .
[33] V. Tangirala, A. Dean, O. Peroomian, et al., Investigations of two-phase detonations 
for performance estimations of a pulsed detonation engine, in: 45th AIAA 
Aerospace Sciences Meeting and Exhibit, Nevada, Reno, 2007, p. 1173 .
[34] C.J. Young, V.O. Duke-Walker, J.A. McFarland, Droplet breakup and evaporation 
in liquid-fueled detonations, Exp. Therm. Fluid Sci. 160 (2024) 111324 .
[35] S. Xu S, X. Jin X, W.Q. Fan, et al., Numerical investigation on the interaction 
characteristics between the gaseous detonation wave and the water droplet, 
Combust. Flame 269 (2024) 113713 .
[36] X.X. Huang, Z.Y. Lin, Study of the mechanism of shock-induced and detonation- 
induced droplet breakup based on hybrid solvers, Phys. Fluids 36 (8) (2024) 
086102 .
[37] S. Salauddin, A.J. Morales, R. Hytovick, et al., Detonation and shock-induced 
breakup characteristics of RP-2 liquid droplets, Shock Waves 33 (3) (2023) 
191 – 203 .
[38] J.R. Burr, M.A. Maybee, B.R. Bigler, et al., Detonation enhanced secondary 
atomization of liquid droplets, in: 34th ILASS-Americas Conference on Liquid 
Atomization and Spray Systems, 2024. Ithaca, NY, USA .
[39] R. Yang, Q.B. Zhang, Q. Xiao, et al., Breakup characteristics of droplets induced by 
detonation waves under different diameters and Mach numbers, Phys. Fluids 37 (1) 
(2025) 016139 .
[40] S.A. Gubin, M. Sichel, Calculation of the detonation velocity of a mixture of liquid 
fuel droplets and a gaseous oxidizer, Combust. Sci. Technol. 17 (3 – 4) (1977) 
109 – 117 .
[41] V. Malik, S. Salauddin, R. Hytovick, et al., Detonation wave driven by aerosolized 
liquid RP-2 spray, Proc. Combust. Inst. 39 (3) (2023) 2807 – 2815 .
[42] G.D. Waldman, W.G. Reinecke, Particle trajectories, heating, and breakup in 
hypersonic shock layers, AIAA J. 9 (6) (1971) 1040 – 1048 .
[43] W.G. Reinecke, G.D. Waldman, Shock layer shattering of cloud drops in reentry 
flight, in: 13th Aerospace Sciences Meeting, 1975. Pasadena, C A, U.S.A .
[44] Q. Xiao, Q.B. Zhang, A. Chinnayya, The universal gaseous detonation dynamics, 
Combust. Flame 270 (2024) 113757 .
[45] Q. Xiao, A. Sow, B.M. Maxwell, et al., Effect of boundary layer losses on 2D 
detonation cellular structures, Proc. Combust. Inst. 38 (3) (2021) 3641 – 3649 .
[46] M. Pilch, C.A. Erdman, Use of breakup time data and velocity history data to 
predict the maximum size of stable fragments for acceleration-induced breakup of 
a liquid drop, Int. J. Multiphas. Flow 13 (6) (1987) 741 – 757 .
[47] B. Guan, Y. Liu, C.Y. Wen, et al., Numerical study on liquid droplet internal flow 
under shock impact, AIAA J. 56 (9) (2018) 3382 – 3387 .
[48] S. Sembian, M. Liverts, N. Tillmark, et al., Plane shock wave interaction with a 
cylindrical water column, Phys. Fluids 28 (5) (2016) 056102 .
[49] C.W. Kauffman, J.A. Nicholls, Shock-wave ignition of liquid fuel drops, AIAA J. 9 
(5) (1971) 880 – 885 .
[50] M. Jalaal, K. Mehravaran, Transient growth of droplet instabilities in a stream, 
Phys. Fluids 26 (1) (2014) 012101 .
[51] A.A. Ranger, The aerodynamic shattering of liquid drops [PhD dissertation], 
University of Michigan, Ann Arbor (MI), 1968 .
[52] W.E. Krauss, Water drop deformation and fragmentation due to shock wave impact 
[PhD dissertation], University of Florida, Gainesville (FL), 1970 .
R. Yang et al.                                                                                                                                                                                                                                    Acta Astronautica 239 (2026) 434–445 
445
