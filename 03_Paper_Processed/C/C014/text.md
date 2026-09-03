<!-- PDF_PAGE: 1 -->

Vol.:(0123456789)1 3
Experiments in Fluids (2020) 61:193 
https://doi.org/10.1007/s00348-020-03026-1
RESEARCH ARTICLE
Effect of Mach number on droplet aerobreakup in shear stripping 
regime
Zhaoguang Wang1  · Thomas Hopfes1 · Marcus Giglmaier1 · Nikolaus A. Adams1
Received: 20 April 2020 / Revised: 27 July 2020 / Accepted: 28 July 2020 / Published online: 9 August 2020 
© The Author(s) 2020
Abstract 
The present experimental study investigates the shear stripping breakup of single droplets in subsonic and supersonic gase-
ous flows. In contrast to most research that places emphasis on the Weber number (We), we focus on the individual effects 
exerted by flow Mach (M
∞ ) and Reynolds numbers (Re). Millimeter-sized droplets made of either ethylene glycol or water 
are exposed to shock-induced flows. Shadowgraph and schlieren images of the breakup process are recorded by an ultra-
high-speed camera. The experimental We is constrained at 1100, while M
∞  is varied from 0.3 to 1.19 and Re from 2600 to 
24,000. A systematic analysis of the experiment series reveals that the breakup pattern alters with M∞  although a constant We 
is maintained. The classical stripping behavior with fine mist shed from the peripheral sheet changes to rupture of multiple 
bags along the periphery at M
∞  = 0.63, and further to stretching of ligament structures from the leeward surface at M∞  = 1.19. 
The corresponding breakup initiation is delayed and the resultant fragments are sized less uniformly and distributed over a 
narrower spread. In terms of the early-stage deformation, droplets experience less intense flattening and slower sheet growth 
at higher M
∞ . The change of Re introduces additional variations, but only to a minor extent.
 * Zhaoguang Wang 
 zg.wang@tum.de
1 Chair of Aerodynamics and Fluid Mechanics, Technical 
University of Munich, 85748 Garching, Germany

<!-- PDF_PAGE: 2 -->

Experiments in Fluids (2020) 61:193
1 3193 Page 2 of 17
Graphical abstract
Wave 
scimanyD
Early-Stage 
noitamrofeD
pukaerB
Pattern
tnemgarF
noitubirtsiD
Subsonic vs Supersonic Droplet Breakup at Constant Weber Number 1100
Mach Number0.31 .2
(The length scale of images in the last row is half of that in the first three rows.)
multiple bags ligaments
normal shock oblique 
shock
less flattening
kinks shifted downstream
separation zone
liquid sheet
larger fragments over 
narrower spread
1 Introduction
Droplet breakup, also termed secondary atomization, refers 
to the fragmentation of a droplet subjected to aerodynamic 
forces. This phenomenon is relevant in diverse applications, 
such as fuel injection (Reitz and Diwakar 1986), spray coat-
ings (Mostaghimi et al. 2002) and metal powder production 
(Lagutkin et al. 2004). It has been widely recognized that the 
breakup morphology is primarily determined by the Weber 
number (We) and the Ohnesorge number (Oh) (Lane 1951; 
Hinze 1955):
where ρ
g and ug are the density and the velocity of the gas 
flow, and d0, σ, μd and ρd are the initial diameter, the surface 
tension, the dynamic viscosity and the density of the liquid 
droplet, respectively. The Weber number represents the ratio 
between the disruptive aerodynamic force and the restora-
tive surface tension, and the Ohnesorge number compares 
(1)
We = /u1D70Cgu2
gd0∕/u1D70E
(2)Oh = /u1D707d∕
√
/u1D70Cdd0/u1D70E,
the viscous force to the surface tension. According to Guil-
denbecher et al. (2009), the influence of liquid viscosity on 
the breakup regime diminishes when Oh drops below 0.1, 
leaving We as the dominant factor.
Several breakup mechanisms have been identified in the 
literature and are classified as bag breakup at 11 < We < 35 
and stripping breakup at We  > 80, with so-called multi -
mode breakup in the intermediate range (Hsiang and Faeth 
1995; Schmehl 2003). The bag breakup is conventionally 
understood as a result of the Rayleigh–Taylor instability 
developed at the droplet front (Joseph et al. 1999). How -
ever, some studies suggest different physical mechanisms, 
including the pressure imbalance between the front and rear 
side (Opfer et al. 2014), the stress repartition around the 
surface (Villermaux and Bossa 2009) and the structure of 
flow vortices in the wake (Inamura et al. 2009). The cause 
of the stripping breakup is also under debate. No agreement 
has been achieved on whether the viscous shear or the aer -
odynamic drag is the driving force. Correspondingly, the 
name of this regime varies among shear stripping (Ranger 
and Nicholls 1969), sheet thinning (Liu and Reitz 1997) and 
shear-induced entrainment (Theofanous and Li 2008). For

<!-- PDF_PAGE: 3 -->

Experiments in Fluids (2020) 61:193 
1 3 Page 3 of 17 193
the current work, we focus on the stripping breakup and 
adopt the concept proposed by Theofanous and Li (2008).
Although the breakup mechanism is mainly governed 
by the Weber number, other non-dimensional parameters 
influence the breakup behavior as well. Chou et al.  (1997) 
conduct experiments with Ohnesorge numbers below 0.1, 
and observe larger micro-drops generated at higher Oh. Pilch 
and Erdman (1987) analyze the effect of Oh on the breakup 
time and conclude a consistent postponement of the breakup 
initiation as Oh increases. Lee and Reitz (2000) experimen-
tally show that the liquid–gas density ratio (ε =  ρ
d/ρg) exerts 
negligible effects on the breakup process at values higher 
than 100. In numerical simulations by Kékesi et al.  (2014); 
however, new breakup patterns appear for density ratios 
below 100. In terms of the flow Reynolds number (Re =  
ρ
gugd0/µg), the work of Liu and Reitz (1997) indicates that 
the breakup behavior is independent of Re when Re > 500. 
The dependence becomes important only in the Stokes flow 
(Aalburg et al. 2003) and in liquid–liquid breakup systems 
(Hsiang and Faeth 1995).
Another non-dimensional parameter, which is of sig-
nificance but not fully explored, is the flow Mach number 
M
∞ . Most of preceding experiments are conducted at sub-
sonic conditions, where the effect of the flow compress-
ibility is marginal. However, with the recent development 
of supersonic combustion systems including pulse detona-
tion engines (Kailasanath 2003), scramjet engines (Curran 
2001) and supersonic gas atomizers (Anderson et al. 1991), 
droplet breakup in high-speed flows becomes of increasing 
importance. Dinh et al. (2003) and Theofanous et al. (2004) 
investigate various breakup regimes in a highly rarified flow 
at M
∞  =  3. They find that the morphologies differ signifi-
cantly from those categorized in subsonic flows and attrib-
ute the differences to changes in pressure fields. Ortiz et al. 
(2004) measure the drag coefficients of droplets in different 
airstreams and observe a rapid increase as the flow Mach 
number approaches supersonic conditions. Xiao et al. (2017) 
numerically simulate the deformation of droplets exposed to 
supersonic flows and conclude that the onset of breakup is 
postponed compared to subsonic cases. Igra and Takayama 
(2003) and Meng and Colonius (2015) conduct experimental 
and numerical research on water column breakup in high-
speed flows, respectively. Both works quantitatively show 
a slower temporal increase of the cross-stream diameter at 
higher M
∞ .
Although the abovementioned research reveals distinct 
breakup features in supersonic flows, the experimental data-
base addressing the effect of M
∞  is rather limited. Moreover, 
a change of M∞  in experiments is commonly accompanied 
with a change of Re, which renders the independent investi-
gation of M
∞  difficult. In the present work, we constrain the 
Weber number at 1100 and decouple the correlation between 
M
∞  and Re by applying different liquid–gas combinations 
and carefully choosing operating conditions. This creates a 
test matrix which allows us to study the effects of M
∞  and 
Re individually.
2  Experimental setup
The layout of the shock tube used for the current experi-
ments is depicted in Fig.  1. The tube, which has an overall 
length of 24 m and an inner diameter of 290 mm, consists of 
three segments: the driver, the driven and the test sections. A 
cookie cutter is installed in front of the test section to remove 
the boundary flows and to contract the cross section to a 
190 × 190 mm
2 square. In the experiments, a 0.15 mm-thick 
Mylar diaphragm is placed between the driver and driven 
sections and in contact with a pair of 0.1 mm-thick crossed 
NiCr heating wires. Each section of the shock tube is first 
filled to pressure levels corresponding to desired flow condi-
tions. Then, a single droplet is produced in the test section 
by expelling liquids through a hypodermic needle with an 
outer diameter of 0.9 mm. The droplet falls through a pair of 
aligned laser emitter and receiver. This triggers the rupture 
of the Mylar diaphragm by supplying an electric current of 
3 A to the heating wires. Subsequently, a planar shock wave 
Fig. 1  Layout of the shock tube and the measurement system

<!-- PDF_PAGE: 4 -->

Experiments in Fluids (2020) 61:193
1 3193 Page 4 of 17
forms, propagates towards the downstream test section and 
induces a flow with uniform flow conditions.
The pressure variation along the shock tube is measured 
by flush-mounted PCB Piezotronics  ICP® fast-response 
pressure sensors. The measured signals are acquired by 
a LTT transient data recorder at a sampling frequency of 
1 MHz. We calculate the shock velocity based on the time 
lag between moments when the incident shock passes two 
pressure sensors ahead of the test section. The combination 
of the shock velocity and initial pre-shock conditions yields 
post-shock flow properties based on moving shock relations. 
Another sensor in the test section measures the pressure rise 
across the incident shock. A representative pressure signal 
normalized against the theoretical post-shock pressure is 
provided in Fig.  2. The shock-induced freestream remains 
steady over 1.6 ms which well covers the investigated period 
of droplet breakup (maximally 1.4 ms). The slight decline in 
the pressure signal is attributed to the growth of the bound-
ary layer as well as the nature of the piezoelectric sensors. 
This pressure signal also serves as a trigger for the image 
recording.
As for the flow visualization, a Shimadzu HyperVision 
HPV-X ultra-high-speed camera is integrated in a Z-type 
shadowgraph/schlieren photography system. The cam-
era records 128 consecutive images with a resolution of 
0.087 mm/pixel at a framing rate of 100 kfps.
For the present experiments, the combinations of two liq-
uids (ethylene glycol and water) and two gases (air and  CO
2) 
are exploited to analyze the effects of M ∞  and Re indepen-
dently at a constant We. The Weber number, which is con-
strained at 1100 with a standard deviation of 50, lies within 
the stripping breakup regime and allows a wide variation 
of M
∞  and Re. Figure  3 shows the inversely proportional 
correlation between M∞  and Re for different liquid–gas com-
binations. The eight labelled points represent the operating 
conditions selected for current experiments, and the associ-
ated error bars (magnified twice in the plot) stand for the 
ranges of M
∞  and Re from repeated experiments. The eight 
operating conditions are numbered as i·j, where the values of 
i and j correspond to the relative magnitudes of M∞  and Re, 
respectively. Detailed parameters averaged from repeated 
experiments at each operating condition are summarized in 
Table  1.
For water (ρ
d  = 998  kg/m 3, σ  = 7.28e-2  N/m, 
μd = 8.9e-4  kg/m  s), the average droplet diameter is 
3.1 mm, resulting in an Oh of 0.002. For ethylene glycol (ρd  
= 1113 kg/m 3, σ = 4.73e-2 N/m, μd = 1.61e-2 kg/m s), the 
lower surface tension leads to smaller droplets with an aver-
age diameter of 2.6 mm and the considerably higher viscos-
ity yields an Oh of 0.043. Concerning all the experiments, 
the freestream Mach number M
∞  varies from subsonic (0.3) 
to supersonic (1.19) levels and the droplet diameter-based 
flow Reynolds number Re ranges over an order of magnitude 
(from 2.6e3 to 2.4e4). The liquid–gas density and viscosity 
ratios are also provided in Table  1 for completeness.
Case 1.4, 2.3, 3.2 and 5.1 are conducted with the same 
liquid and gas. Comparisons between them highlight the 
overall influences of parameters other than We and Oh. 
Moreover, Case 2.3, 4.3 and 5.3 have comparable Re but 
different M
∞ , while Case 5.1, 5.2, and 5.3 share the same 
M∞  but changing Re. Comparisons of the former and of the 
latter group shed light on the individual role played by M ∞  
and Re, respectively.
3  Results and discussion
A brief overview of the typical stripping breakup process 
in subsonic flows (Case 1.4, M
∞  = 0.3, liquid: ethylene gly-
col, gas: air) is provided in Fig.  4. Here, the experimental 
time t is regarded as zero at the moment when the incident 
shock impacts on the droplet. Furthermore, t  is normalized 
against the characteristic transport time derived by Ranger 
and Nicholls (1969) based on droplet deformation in incom-
pressible flows, yielding the dimensionless time T as
Fig. 2  Step-wise pressure rise 
across the incident shock meas-
ured in the test section

<!-- PDF_PAGE: 5 -->

Experiments in Fluids (2020) 61:193 
1 3 Page 5 of 17 193
The time scaling in Eq. (3 ) does not account for the com-
pressibility effects, which govern the droplet breakup in the 
current study. Nevertheless, this scaling is used to present 
the results in a consistent and comparable way with previ-
ous literature. Presented images are processed with subtrac-
tion of the background noise, contrast stretching and super 
resolution using MATLAB’s Very Deep Super-Resolution 
convolutional neural network (Kim et al. 2016).
The entire breakup process is divided into four stages. It 
starts with the shock-droplet interaction which establishes 
a flow field resembling that around a solid sphere (T < 0.1). 
Then, the droplet is flattened along the streamwise direction 
(T = 0.2) and a liquid sheet emerges at the equator (T = 0.3). 
The rupture of the sheet indicates the breakup initiation 
(T = 0.4) and the coherent body is continuously eroded at 
(3)
T = t ⋅ ug∕
/parenleft.s2
d0
/uni221A.s1
/u1D70Cd∕/u1D70Cg
/parenright.s2
, the periphery afterwards. The last stage is achieved when the 
whole droplet disintegrates into fragments distributed widely 
in the flow field (out of the time window shown in Fig.  4).
Figure  4 also presents the quantitative change of the drop-
let cross-stream diameter d
c. The error bar represents the 
uncertainty (90% confidence level based on the Student’s 
t-distribution) calculated from four repeated experiments. 
Before the onset of breakup (T  < 0.37), the increase of d
c 
indicates the flattening of the intact body and the associated 
uncertainty is low. Once the breakup starts, the intact body is 
shadowed by the fine mist. The interpretation of d
c changes 
to a description of the spatial distribution of liquid frag-
ments. The corresponding uncertainty significantly increases 
as micro-drops are more sensitive to local flow disturbance 
than the coherent body. Considering the uncertainty levels 
are similar for all cases, the error bars are omitted in the fol-
lowing plots for the sake of brevity.
In following sections, we compare cases with varia-
tions in flow Mach and Reynolds numbers with respect to 
Fig. 3  Inversely proportional correlation between M α and Re at 
We = 1100. Each line corresponds to a certain liquid–gas combina-
tion. The eight operating conditions are labeled as i·j, with i and j 
representing the relative magnitudes of M α and Re respectively. The 
associated error bars stand for the ranges of conditions from repeated 
experiments and are magnified twice in the plot for a clearer display
Table 1  Operating conditions 
averaged from repeated 
experiments
Liquid Gas We Oh Re M∞ ρd/ρg μd/μg
Case 1.4 E.G Air 1060 0.042 2.4e4 0.3 7.1e2 796
Case 2.3 E.G Air 1056 0.044 8.6e3 0.63 3.6e3 697
Case 3.2 E.G Air 1120 0.043 5.9e3 0.83 7.1e3 635
Case 5.1 E.G Air 1050 0.044 2.6e3 1.19 2.1e4 508
Case 3.3 Water Air 1160 0.002 9.5e3 0.83 4.5e3 35
Case 4.3 E.G CO2 1100 0.044 8.8e3 0.94 4.7e3 802
Case 5.2 E.G CO2 1120 0.043 5.9e3 1.19 9.0e3 713
Case 5.3 Water CO2 1080 0.002 8.6e3 1.19 6.1e3 39

<!-- PDF_PAGE: 6 -->

Experiments in Fluids (2020) 61:193
1 3193 Page 6 of 17
each stage of the breakup process, namely wave dynam-
ics, early-stage deformation, breakup patterns, and frag-
ment sizes and spatial distributions. The main comparison 
is made between Case 1.4, 2.3, 3.2 and 5.1 all of which 
employ the same liquid and gas, to illustrate the overall 
tendency. This is further complemented by comparisons 
between constant-Re and constant-M
∞  cases to highlight 
the individual effects of M ∞  and Re, respectively. The 
discussion is concluded with a brief analysis of the influ -
ence of Oh.
3.1  Wave dynamics
Figure  5 presents a visualization of wave dynamics sur -
rounding ethylene glycol droplets in airstreams after the 
impact of the incident shock for Case 1.4, 2.3, 3.2 and 5.1. 
At M
∞  = 0.3, typical features including the reflected shock 
(RS) at the windward surface, the diffracted shock (DS) 
enclosing the droplet and separation zones (SZ) attached at 
the rear are clearly identified. These characteristics are in 
good agreement with the experimental and numerical results 
of water column breakup from Igra and Takayama ( 2001) 
and Meng and Colonius (2015).
Fig. 4  Breakup patterns and cross-stream diameter variation of an ethylene glycol droplet at M α = 0.3 (Case 1.4). The error bars represent uncer -
tainties of dc calculated from four repeated experiments
Fig. 5  Wave dynamics around ethylene glycol droplets in air. The operating conditions from left to right are Case 1.4, 2.3, 3.2 and 5.1. RS 
reflected shock, DS diffracted shock, SZ separation zone, NS normal shock, OS oblique shock)

<!-- PDF_PAGE: 7 -->

Experiments in Fluids (2020) 61:193 
1 3 Page 7 of 17 193
The main change at M ∞  = 0.63 is that the separation 
zone behind the droplet extends over a wider region. As the 
freestream speed enters the transonic range (M ∞  = 0.83), a 
normal shock (NS) appears behind the droplet and fluctu -
ates slightly around the displayed location. This suggests 
that the surrounding flow accelerates to supersonic condi-
tions as it bypasses the droplet. For the case at M
∞  = 1.19, 
an oblique shock cone (OS) appears, stretching downstream 
over a broad region. Meanwhile, the reflected shock ahead 
of the droplet settles as a detached bow shock.
Considering the droplet does not undergo noticeable 
deformation during the short period of shock-droplet inter -
action, the surrounding pressure field is expected to resem-
ble that around a solid sphere, which is also implied by the 
wave patterns presented in Fig.  5. As M
∞  changes, the pres-
sure imposed on the spherical surface differs significantly 
(Charters and Thomas 1945; Bailey and Haitt 1972). These 
differences are held accountable for the more pronounced 
distinctions in succeeding deformation and breakup pro-
cesses (Hanson et al. 1963).
The travelling velocity of the reflected shock is plotted 
in Fig.  6 with respect to the position relative to the droplet 
front. The distance s  between the reflected shock and the 
droplet leading edge is normalized by the droplet diameter 
d
0. The Mach number of the reflected shock relative to the 
freestream flow is calculated as Mr = (ds/dt + ug)/a, where 
a is the speed of sound in the freestream. For cases with 
M∞  < 1, the reflected shock decays to sonic waves, and the 
corresponding Mr falls towards 1. For the supersonic case 
with M∞  = 1.19, however, the decreasing M r settles at M ∞  
and the normalized distance s /d0 is stabilized around 0.65 
which matches the value measured for a solid sphere at simi-
lar conditions (Liepmann and Roshko 2001).
3.2  Early‑stage deformation
The early-stage droplet deformation for subsonic and super-
sonic cases is compared in Fig.  7. As described in Fig.  4, 
the droplet at M∞  = 0.3 exhibits typical deformation features 
such as flattening at frontal and rear surfaces and stretching 
of the liquid sheet around the equator. Generally, droplets at 
higher-M
∞  follow similar deformation patterns, but a thor -
ough examination reveals noticeable distinctions that are 
summarized as follows:
• the liquid sheet emerges further downstream in the super-
sonic flow (T = 0.20);
• the flattening of the leeward surface becomes weaker as 
M
∞  increases (T = 0.30);
• the liquid sheet grows more rapidly at lower M ∞  
(T = 0.48).
As the windward surface of the droplets gets flattened, 
kinks form around the droplet equator at T  = 0.2. These 
kinks are the origins of the subsequent development of liq-
uid sheets. In subsonic flows, the kink is located ahead of 
the equatorial plane and the angle of inclination of the line 
connecting the kink to the droplet center is approximately 
80° with respect to the flow direction. However, the position 
of the kink is shifted considerably downstream in the super-
sonic flow and the corresponding angle of inclination is 92°. 
The kink locations are in good accordance with the trajec-
tory of the separation point at the surface of a solid sphere 
measured by Charters and Thomas (1945). In their work, the 
separation point stays with an angle of inclination between 
70° and 80° at subsonic conditions and drifts downstream 
beyond 90° at M
∞ = 1.2.
During the period shown in Fig.  7, the leeward surface 
of the droplet is continuously flattened. The extent of the 
flattened area at T  = 0.3 is estimated relative to the initial 
droplet diameter. As M
∞ increases from 0.3 to 1.19, the cor-
responding flattened area shrinks from 0.84d0 to 0.5d0. This 
could be associated to the change of the pressure imposed on 
the droplet rear at different flow conditions. Karyagin et al. 
(1991) experimentally measure the pressure distribution 
over the surface of a sphere, and observe that the pressure 
Fig. 6  Mach number of the 
reflected shock relative to the 
freestream flow (Mr) with 
respect to the normalized dis-
tance from the reflected shock 
to the droplet front (s/d
0) for 
Case 1.4, 2.3, 3.2, 4.3 and 5.1

<!-- PDF_PAGE: 8 -->

Experiments in Fluids (2020) 61:193
1 3193 Page 8 of 17
at the rear surface drops consistently as M ∞ increases. The 
same trend is also reported in the numerical work by Nagata 
et al. (2016).
By T = 0.48, the liquid sheets for all cases have grown 
to considerable sizes and stretched out radially from the 
main body. Similarly to the experimental observation by 
Theofanous et al. (2012) and the numerical analyses by 
Jalaal and Mehravaran ( 2014), the growth of the liquid 
sheets is enhanced by the emergence of propagative waves 
at the droplet surface, as shown in Fig.  8. These surface 
waves are induced by Kelvin–Helmholtz instabilities at the 
windward surface, where the liquid–gas interface suffers 
Fig. 7  Droplet flattening and 
development of liquid sheets 
(left to right: Case 1.4, 2.3, 3.2 
and 5.1)
M∞ = 0.30 M∞ = 0.63 M∞ = 0.83 M∞ = 1.19 
T = 0.20
T = 0.25
T = 0.30
T = 0.40
T = 0.48
Fig. 8  Emergence, propagation 
and merging of surface waves 
at the droplet periphery (Case 
3.2, M
∞ = 0.83). Dark and white 
arrows indicate locations and 
movement directions of the 
surface waves, respectively

<!-- PDF_PAGE: 9 -->

Experiments in Fluids (2020) 61:193 
1 3 Page 9 of 17 193
strong shear. The waves are transported towards the equator 
under drag forces and then merge with the preceding waves.
Papamoschou and Roshko (1988) point out that increas-
ing the flow Mach number reduces the growth rate of the 
shear layer between two streams rapidly, because the asso-
ciated compressibility effect tends to stabilize the flow dis-
turbance. Moreover, according to Liepmann and Roshko 
(2001) and Nayfeh and Saric (1971), the pressure distribu-
tion around small-scale waves is out of phase with the wave 
profile in supersonic flows and thus suppresses the develop-
ment of instabilities. Consequently, the growth rate of the 
liquid sheet is lower at higher M
∞. This explains the obser-
vation at T  = 0.48 in Fig.  7 that the liquid sheet becomes 
smaller as M∞ increases.
Figure  9 compares the droplet contours at T = 0.4 between 
Case 3.2, 5.2 and 5.1. The dimensions are normalized 
against the initial droplet diameter, and the origin represents 
the position of the initial droplet center. Case 5.2 has the 
same M
∞ as Case 5.1, and shares a comparable Re with Case 
3.2. The resemblance of the droplet contours between Case 
5.2 and Case 5.1 indicates that Re exerts negligible effects 
on the early-stage deformation, while M
∞ plays a critical 
role in determining the flattening intensity and the sheet 
development.
To further quantify the droplet deformation, streamwise 
displacements of the leading edge, the mass center and the 
trailing edge are measured. These parameters are of particu-
lar interest for numerical validations.
The position of the mass center, which is calculated with 
the assumption that the droplet cross section normal to the 
flow direction is axisymmetric, is plotted in Fig.  10. For 
all cases, the trajectory of the droplet mass center approxi-
mates to be parabolic over the shown period. The drag coef-
ficient CD is estimated by fitting the data into the relation 
xmc/d
0 = 3/8CDT2 derived by Ranger and Nicholls (1969). 
The subsonic case at M ∞ = 0.3 experiences a drastic accel-
eration around T = 0.25. This results from the rapid growth 
of the cross-stream diameter, as shown in Fig.  7, and yields 
a relatively high CD of 1.4. For the other three cases that 
share comparable cross-stream diameters before T  = 0.4, 
the streamwise drift of the droplet mass center is faster at 
higher M
∞. The corresponding drag coefficients are calcu -
lated to be 0.9 for M∞ = 0.63, 1.0 for M∞ = 0.83 and 1.2 for 
M∞ = 1.19. This trend agrees with the drag coefficients for a 
solid sphere measured by Bailey and Haitt (1972) and Char-
ters and Thomas (1945), but the values are much higher due 
to the droplet flattening.
Figure  11 compares the streamwise displacements of the 
leading edge and the trailing edge at different flow condi-
tions. It is noteworthy that the difference of the leading edge 
shift is negligible among all present cases. Therefore, as also 
stated by Theofanous (2011), the displacement of the lead-
ing edge is not a proper parameter to represent the drag. In 
terms of the trailing edge, the displacement shows certain 
degrees of variations between cases and becomes smaller at 
higher M
∞. This tendency is consistent with the observation 
Fig. 9  Droplet outlines of Case 
3.2, 5.2 and 5.1 at T = 0.4. The 
mass center of the initial droplet 
lies at (0, 0)

<!-- PDF_PAGE: 10 -->

Experiments in Fluids (2020) 61:193
1 3193 Page 10 of 17
in Fig.  7 that the flattening at the leeward surface is weak -
ened as M∞ increases.
3.3  Breakup patterns
Breakup patterns of droplets at different flow conditions 
are displayed in Fig.  12. The first row represents the indi-
vidual breakup initiation which is defined as the onset of 
the formation of liquid fragments. Each of the remaining 
rows corresponds to a specific time moment. Although the 
breakup process shows certain degrees of chaotic behavior 
(Hardalupas and Whitelaw 1994; Engelbert et al. 1995), the 
features discussed in the following are consistently observed 
in repeated experiments. Generally speaking, three types of 
breakup patterns are categorized:
• fragmentation of the liquid sheet (M∞  = 0.3);
• development of multiple bags along the periphery 
(M
∞  = 0.63);
• formation of streamwise ligaments in the wake 
(M
∞  = 1.19).
The droplet at M ∞  = 0.3 experiences a typical strip-
ping breakup initiated with the fracture of the liquid sheet. 
Afterwards, the windward surface is continuously flattened 
and expands over an increasingly broad region. At regions 
encircling the smooth front, small-scale waves generated by 
Kelvin–Helmholtz instabilities appear. These waves propa-
gate towards the periphery peeling micro-drops off from the 
droplet. The micro-drops are entrained in the flow and dis-
tributed widely in the cross-stream direction.
The breakup pattern is altered as the flow Mach number 
increases. At M
∞  = 0.63, the breakup onset is not indicated 
by entrainment of micro-drops, but by the formation of mul-
tiple bags along the periphery. Figure 13 shows the evolution 
from the bending of the liquid sheet to the inflation of the 
multiple bags. As the sheet extends downstream, the periph-
eral region is straightened to directly face the freestream 
flow (T = 0.54). Then, multiple bags form along the rim and 
Fig. 10  Streamwise displacement of the mass center for Case 1.4, 2.3, 3.2 and 5.1. Initial droplet center lies at x = 0. The plotted data are aver -
aged values from four repeated experiments
Fig. 11  Streamwise displace-
ment of the leading edge and 
the trailing edge for Case 1.4, 
2.3, 3.2 and 5.1. Initial droplet 
center lies at x = 0. The plotted 
data are averaged values from 
four repeated experiments

<!-- PDF_PAGE: 11 -->

Experiments in Fluids (2020) 61:193 
1 3 Page 11 of 17 193
inflate rapidly (T = 0.59). These bags rupture into fine mist 
and the rings that the bags are attached to disintegrate into 
larger interconnected fragments as indicated at T  = 0.8 in 
Fig.  12. The remaining coherent body of the droplet deforms 
into a crescent shape and the succeeding breakup process 
resembles the typical stripping pattern.
According to Theofanous et al. (2004) and Guildenbecher 
et al.  (2009), the wave number n of the fastest-growing wave 
induced by Rayleigh–Taylor instabilities at the droplet front 
can be calculated with the following relation:
For Case 2.3 at T  = 0.56, d
c is 1.53 times of the initial 
diameter d0 (see Fig.  15) and the average value of CD is 0.9 
(see Fig.  10), which yields n  = 11.7. The actual value of n 
should be higher considering the real-time C D is growing 
over time. Nevertheless, the calculated wave number agrees 
(4)n = 1
2/u1D70B
�dc
d0
�2√
CD ⋅ We
well with the observation in Fig.  13 that the straightened 
edge, where bags develop occupies 1/12.5 of the entire 
cross-stream diameter. This implies that the Rayleigh–Taylor 
instability is the underlying reason for the local bag forma-
tion. Similar bag structures are also observed in the numeri-
cal simulation of diesel jet breakup at We = 1270 by Shinjo 
and Umemura (2010).
For Case 5.1 at M
∞  = 1.19, the droplet breakup is char -
acterized by the generation of long and thin streamwise 
ligaments in the wake, similarly to the observation by Liu 
and Reitz (1997). Figure  14 presents the deformation of the 
liquid sheet which induces the succeeding generation of liga-
ments. After emerging from the main body, the liquid sheet 
bends along the flow direction and folds to wrap the drop-
let rear before the breakup is initiated. The sheet becomes 
thinner as it stretches and thus is increasingly sensitive to 
instabilities. According to the study of sheet breakup in co-
flow by Stapper and Samuelsen ( 1990), surface instability 
is mainly caused by the growth of the streamwise vortical 
Fig. 12  Droplet breakup pat-
terns (left to right: Case 1.4, 
2.3, 3.2, 5.1 and 5.2). The top 
row corresponds to the breakup 
initiation
T = 1.3 T = 1.0 T = 0.8
M∞ = 0.30 
Re = 2.4e4 
M∞ = 0.63 
Re = 8.6e3 
M∞ = 0.83 
Re = 5.9e3 
M∞ = 1.19 
Re = 2.6e3 
M∞ = 1.19 
Re = 5.9e3 
T = 0.39 
T = 0.58 
T = 0.63 
T = 0.69 
T = 0.66 
Fig. 13  Straightening of the droplet rim (indicated by the arrows) and formation of multiple bags along the periphery for Case 2.3 at M∞ = 0.63

<!-- PDF_PAGE: 12 -->

Experiments in Fluids (2020) 61:193
1 3193 Page 12 of 17
waves when the flow velocity is high. As a result, streamwise 
ligaments connected by thin films are formed ( T = 0.69 in 
Fig.  12). After the films burst into micro-drops, the liga-
ments are stretched under the viscous shear of the flow and 
break into larger fragments in the presence of Rayleigh-Pla-
teau instabilities. The subsequent breakup of the droplet con-
tinues in the pattern that new ligaments form and fragment. 
It is occasionally observed that large liquid clumps (T = 1.3 
in Fig.  12) detach from the intact body and disintegrate sepa-
rately. It is noteworthy that recent studies (Jalaal and Meh-
ravaran 2014; Meng and Colonius 2018; Biasiori-Poulanges 
and El-Rabii 2019; Dorschner et al. 2020) propose the mech-
anism of transverse azimuthal modulation as an alternative 
explanation for the generation of streamwise ligaments. It is 
stated that the growth of Kelvin–Helmholtz instabilities near 
the droplet periphery triggers Rayleigh–Taylor instabilities 
in the transverse plane which further lead to the formation 
of ligaments.
The breakup process of Case 5.2 is also presented in 
Fig.  12. The droplet exhibits few breakup features in com-
mon with the identical-Re Case 3.2, but resembles approxi-
mately the same characteristics as the identical-M
∞  Case 
5.1. A minor difference between Case 5.2 and Case 5.1 is 
that the former generates slightly thinner ligaments than the 
latter. This suggests that M
∞  plays a dominant role in deter-
mining the breakup patterns, while Re only affects detailed 
structures.
Figure  15 compares the change of the droplet cross-stream 
diameter d
c between subsonic and supersonic conditions. 
Before T = 0.25, the droplet deformation is characterized by 
the flattening of the main body. During this stage only mar-
ginal differences are identified among all cases. Afterwards 
the liquid sheet starts to develop, resulting in a rapid growth 
of d
c. The growth rate is significantly higher for M ∞  = 0.3 
than the others, which is in accordance with the observation 
in Fig.  7. Although the differences between high-M
∞  cases 
(Case 2.3, 3.2 and 5.1) are comparatively small, there exists 
a consistent tendency that the cross-stream diameter grows 
more slowly as M
∞  increases. Once the breakup is initi-
ated (marked by the red points in Fig.  15), dc represents the 
cross-stream spread of the liquid fragments instead. With 
the breakup onset as a separating point, the overall d
c pro-
file is divided into two power-law stages. The short-duration 
plateaus ahead of the breakup initiation correspond to the 
Fig. 14  Folding of the liquid sheet (indicated by the arrows) and generation of ligaments connected by thin membranes for Case 5.1 at M∞ = 1.19
Fig. 15  Variation of the cross-
stream diameter for Case 1.4, 
2.3, 3.2 and 5.1. The red dots 
represent the breakup initiation. 
The plotted data are averaged 
values from four repeated 
experiments

<!-- PDF_PAGE: 13 -->

Experiments in Fluids (2020) 61:193 
1 3 Page 13 of 17 193
periods when the liquid sheet is bent along the flow direction 
rather than stretched out radially.
For all cases, the breakup begins when the normalized 
dc reaches approximately 1.5. The subsonic Case 1.4 at 
M∞  = 0.3 experiences the earliest breakup, and the cor -
responding initiation time T  = 0.39 matches the empirical 
correlation proposed by Pilch and Erdman (1987). The 
postponement of the breakup initiation as M
∞  increases is a 
consequence of the change in the breakup pattern as shown 
earlier. The fragmentation of multiple bags and the disin-
tegration of streamwise ligaments at high M
∞  need signifi-
cantly longer time than the direct sheet rupture at low M∞ .
3.4  Fragment sizes and spatial distributions
In industrial applications that involve atomization pro-
cesses, the fragment sizes are of particular significance. 
For instance, small fragments are desired in fuel injections 
to achieve efficient evaporation and combustion. Figure  16 
compares the droplet fragmentation at T  = 2.0 for Case 1.4, 
2.3, 3.2 and 5.1. At this stage, the coherent body is difficult 
to identify as the windward surface is severely eroded. Drop-
lets break into uniformly fine mist at subsonic conditions, 
while the supersonic flow leads to large discrete particles 
that are scattered among tiny micro-drops. These large par-
ticles are mainly caused by the disintegration of ligament 
structures.
Apart from the size distribution, the spatial spread of the 
fragments is also of practical importance, since it determines 
the likelihood of micro-drops coalescing into larger parti-
cles. Figures  17, 18 present the outlines of dispersed frag-
ments for various cases at T = 2.0. The outlines are extracted 
with  MATLAB
® based on the modified Moore-Neighbor 
tracing algorithm (Gonzalez et al. 2004). The differences 
among Case 2.3, 4.3 and 5.3 (Fig. 17), which share the same 
Re, indicate that higher M
∞  leads to a narrower cross-stream 
spread of the fragments. Such an effect could be related to 
the fact that the windward surface of the droplet is less flat-
tened but more curved at higher M
∞  (see Figs.  7, 12). Corre-
spondingly, the fragments gain lower cross-stream momen-
tum from the gas flow when detaching from the droplet 
periphery and are hence distributed less widely in the cross-
stream direction. The comparison between Case 5.1, 5.2 and 
5.3 (Fig.  18), which share an identical M
∞ , shows that lower-
ing Re also tends to constrain the spatial distribution of the 
fragments, but much less effectively than increasing M
∞ .
Fig. 16  Spatial distributions of liquid fragments at T = 2.0 for Case 1.4, 2.3, 3.2 and 5.1. The white circles represent the initial droplet sizes

<!-- PDF_PAGE: 14 -->

Experiments in Fluids (2020) 61:193
1 3193 Page 14 of 17
3.5  Effect of the Ohnesorge number
Figure  19 displays the breakup process of water droplets 
at M∞  = 0.83 (Case 3.3) and M ∞  = 1.19 (Case 5.3). Com-
pared to ethylene glycol, water is much less viscous and 
yields a 20 times lower Ohnesorge number. The reduction 
in the liquid viscosity weakens the capability of sustaining 
large liquid sheets. Consequently the corresponding breakup 
initiations are much earlier than those of ethylene glycol 
droplets at the same M
∞  (0.39 vs. 0.63 at M ∞  = 0.83, 0.56 
vs. 0.69 at M∞  = 1.19). Furthermore, in contrast to the long 
outstretched ligaments observed for ethylene glycol droplets 
in supersonic flows, the ligaments of water droplets extend 
over a very limited distance before disintegration (T  = 0.56 
Fig. 17  Comparison of frag-
ment spreads at T = 2.0 between 
Case 2.3, 4.3 and 5.3. For all 
cases, Re is approximately 
8.6e3
Fig. 18  Comparison of frag-
ment spreads at T = 2.0 between 
Case 5.1, 5.2 and 5.3. For all 
cases, M
α equals to 1.19

<!-- PDF_PAGE: 15 -->

Experiments in Fluids (2020) 61:193 
1 3 Page 15 of 17 193
at M∞  = 1.19). This is consistent with the observation by 
Stapper et al. (1992) that less viscous liquids sustain shorter 
ligaments.
4  Conclusions
The present experimental work compares the stripping 
breakup of liquid droplets in subsonic and supersonic flows. 
Millimeter-sized droplets are impacted by a planar shock 
wave generated in a shock tube. The process of deformation 
and fragmentation is visualized in a shadow/schlieren system 
and recorded by an ultra-high-speed camera. Through con-
trolling the shock strength and employing different liquids 
and gases, the Weber number is maintained around 1100, 
while the flow Mach number M
∞  varies from 0.3 to 1.19 and 
the Reynolds number Re from 2600 to 24,000. The effects of 
changing flow conditions on the breakup process are sum-
marized as follows.
The droplet deformation prior to the breakup, including 
flattening of windward and leeward surfaces and growth 
of the liquid sheet at the equator, is weakened by increas-
ing M
∞ . The sheet is initiated further downstream along 
the droplet surface at higher M∞ .
In subsonic flows, the stripping breakup starts with the 
fragmentation of the liquid sheet. As M
∞  increases, dis-
tinct breakup features emerge at the breakup initiation, 
such as multiple bags formed along the periphery and 
ligament structures stretching in the wake. Correspond -
ingly, the breakup initiation is significantly postponed.
In subsonic flows, the breakup generates uniformly fine 
fragments spreading widely in the cross-stream direc -
tion. At higher M
∞ , the fragments are of less uniform 
sizes and constrained within a narrower region behind 
the main body.
Although decreasing Re tends to have a complementary 
role to increasing M
∞ , the effect is marginal on main 
breakup behaviors.
Lowering Oh reduces the size of liquid sheets and liga-
ments and results in earlier breakup initiation.
Although many features discussed in the present study 
focus on detailed breakup structures, they play crucial 
roles in determining the final fragmentation pattern. The 
dependency of fragment sizes and spatial distributions on 
the flow Mach number is especially important for indus-
trial applications, where the atomization process is con-
stantly optimized to generate widely-spread uniformly-
sized fragments.
Fig. 19  Breakup process of 
water droplets at Mα = 0.83 
(Case 3.3) and 1.19 (Case 5.3)
M∞ = 0.83 M∞ = 1.19 
T = 0.30
T = 0.39
T = 0.56
T = 0.80

<!-- PDF_PAGE: 16 -->

Experiments in Fluids (2020) 61:193
1 3193 Page 16 of 17
Acknowledgements Open Access funding provided by Projekt DEAL. 
The authors acknowledge funding by the European Research Council 
(ERC) under the European Union’s Horizon 2020 research and innova-
tion program (Grant agreement No. 667483).
Compliance with ethical standards 
Conflict of interest There is no financial or personal relationship be-
tween authors and other people or organizations that could inappropri-
ately influence or bias the work.
Open Access This article is licensed under a Creative Commons Attri-
bution 4.0 International License, which permits use, sharing, adapta-
tion, distribution and reproduction in any medium or format, as long 
as you give appropriate credit to the original author(s) and the source, 
provide a link to the Creative Commons licence, and indicate if changes 
were made. The images or other third party material in this article are 
included in the article’s Creative Commons licence, unless indicated 
otherwise in a credit line to the material. If material is not included in 
the article’s Creative Commons licence and your intended use is not 
permitted by statutory regulation or exceeds the permitted use, you will 
need to obtain permission directly from the copyright holder. To view a 
copy of this licence, visit http://creat iveco mmons .org/licen ses/by/4.0/.
References
Aalburg C, Faeth GM, van Leer B (2003) Deformation and drag prop-
erties of round drops subjected to shock-wave disturbances. AIAA 
J 41(12):2371–2378. https ://doi.org/10.2514/2.6862
Anderson IE, Figliola RS, Morton H (1991) Flow mechanisms in high 
pressure gas atomization. Mater Sci Eng A 148(1):101–114. https 
://doi.org/10.1016/0921-5093(91)90870 -S
Bailey AB, Haitt J (1972) Sphere drag coefficients for a broad range of 
Mach and Reynolds numbers. AIAA J 10(11):1436–1440. https  
://doi.org/10.2514/3.50387 
Biasiori-Poulanges L, El-Rabii H (2019) High-magnification shadow-
graphy for the study of drop breakup in a high-speed gas flow. 
Opt Lett 44(23):5884–5887. https ://doi.org/10.1364/ol.44.00588 4
Charters AC, Thomas RN (1945) The aerodynamic performance of 
small spheres from subsonic to high supersonic velocities. J Aero-
naut Sci 12(4):468–476. https ://doi.org/10.2514/8.11287 
Chou WH, Hsiang LP, Faeth GM (1997) Temporal properties of 
drop breakup in the shear breakup regime. Int J Multiph Flow 
23(4):651–669.  https ://doi.org/10.1016/S0301 -9322(97)00006 -2
Curran ET (2001) Scramjet engines: the first forty years. J Propul 
Power 17(6):1138–1148. https ://doi.org/10.2514/2.5875
Dinh TN, Li GJ, Theofanous TG (2003) An investigation of drop-
let breakup in a high mach, low weber number regime. In: 41st 
aerospace sciences meeting and exhibit. American Institute of 
Aeronautics and Astronautics, Reston, Virigina, p 317.  https ://
doi.org/10.2514/6.2003-317
Dorschner B, Biasiori-Poulanges L, Schmidmayer K, El-Rabii H, and 
Colonius T. (2020) On the formation and recurrent shedding of 
ligaments in droplet Aerobreakup.  arXiv :2003.00048 
Engelbert C, Hardalupas Y, Whitelaw JH (1995) Breakup phenom-
ena in coaxial airblast atomizers. Proc Royal Soc London, A 
451(1941):189–229. https ://doi.org/10.1098/rspa.1995.0123
Gonzalez RC, Woods RE, Eddins SL (2004) Digital image processing 
using MATLAB. Pearson Education India
Guildenbecher DR, López-Rivera C, Sojka PE (2009) Secondary 
atomization. Exp Fluids 46(3):371–402. https ://doi.org/10.1007/
s0034 8-008-0593-2
Hanson AR, Domich EG, Adams HS (1963) Shock tube investigation 
of the breakup of drops by air blasts. Phys Fluids 6(8):1070–1080. 
https ://doi.org/10.1063/1.17068 64
Hardalupas Y, Whitelaw JH (1994) Characteristics of sprays produced 
by coaxial airblast atomizers. J Propul Power 10(4):453–460. https 
://doi.org/10.2514/3.23795 
Hinze JO (1955) Fundamentals of the hydrodynamic mechanism of 
splitting in dispersion processes. AIChE J 1(3):289–295. https ://
doi.org/10.1002/aic.69001 0303
Hsiang L-P, Faeth GM (1995) Drop deformation and breakup due 
to shock wave and steady disturbances. Int J Multiph Flow 
21(4):545–560. https ://doi.org/10.1016/0301-9322(94)00095 -2
Igra D, Takayama K (2001) Investigation of aerodynamic breakup 
of a cylindrical water droplet. At Sprays 11(2):20. https ://doi.
org/10.1615/Atomi zSpr.v11.i2.50
Igra D, Takayama K (2003) Experimental investigation of two cylin-
drical water columns subjected to planar shock wave loading. J 
Fluids Eng 125(2):325–331. https ://doi.org/10.1115/1.15386 28
Inamura T, Yanaoka H, Kawada T (2009) Visualization of airflow 
around a single droplet deformed in an airstream. At Sprays 
19(7):667–677. https ://doi.org/10.1615/Atomi zSpr.v19.i7.50
Jalaal M, Mehravaran K (2014) Transient growth of droplet insta-
bilities in a stream. Phys Fluids 26(1):012101. https ://doi.
org/10.1063/1.48510 56
Joseph DD, Belanger J, Beavers G (1999) Breakup of a liquid drop 
suddenly exposed to a high speed airstream. Int J Multiph Flow 
25:1263–1303. https ://doi.org/10.1016/S0301 -9322(99)00043 -9
Kailasanath K (2003) Recent developments in the research on 
pulse detonation engines. AIAA J 41(2):145–159.  https ://doi.
org/10.2514/2.1933
Karyagin VP, Lopatkin AI, Shvets AI, Shilin NM (1991) Experi -
mental investigation of the separation of flow around a sphere. 
Fluid Dyn 26(1):126–129.  https ://doi.org/10.1007/bf010 50124 
Kékesi T, Amberg G, Prahl Wittberg L (2014) Drop deformation 
and breakup. Int J Multiph Flow 66(June):1–10. https ://doi.
org/10.1016/j.ijmul tipha seflo w.2014.06.006
Kim J, Kwon Lee J, Mu Lee K (2016) Accurate image super-reso-
lution using very deep convolutional networks. In: 2016 IEEE 
conference on computer vision and pattern recognition (CVPR), 
pp 1646–1654.  https ://doi.org/10.1109/CVPR.2016.182
Lane WR (1951) Shatter of drops in streams of air. Ind Eng Chem 
43(6):1312–1317. https ://doi.org/10.1021/ie504 98a02 2
Lee CH, Reitz RD (2000) An experimental study of the effect of gas 
density on the distortion and breakup mechanism of drops in 
high speed gas stream. Int J Multiph Flow 26(2):229–244. https 
://doi.org/10.1016/S0301 -9322(99)00020 -8
Liepmann HW, Roshko A (2001) Elements of gasdynamics. Courier 
Corporation
Liu Z, Reitz RD (1997) An analysis of the distortion and breakup 
mechanisms of high speed liquid drops. Int J Multiph Flow 
23(4):631–650. https ://doi.org/10.1016/S0301 -9322(96)00086  
-9
Meng JC, Colonius T (2015) Numerical simulations of the early stages 
of high-speed droplet breakup. Shock Waves 25(4):399–414. https 
://doi.org/10.1007/s0019 3-014-0546-z
Meng JC, Colonius T (2018) Numerical simulation of the aerobreakup 
of a water droplet. J Fluid Mech 835:1108–1135. https ://doi.
org/10.1017/jfm.2017.804
Mostaghimi J, Pasandideh-Fard M, Chandra S (2002) Dynamics of 
splat formation in plasma spray coating process. Plasma Chem 
Plasma Process 22(1):59–84. https ://doi.org/10.1023/A:10129  
40515 065

<!-- PDF_PAGE: 17 -->

Experiments in Fluids (2020) 61:193 
1 3 Page 17 of 17 193
Nagata T, Nonomura T, Takahashi S, Mizuno Y, Fukuda K (2016) 
Investigation on subsonic to supersonic flow around a sphere 
at low Reynolds number of between 50 and 300 by direct 
numerical simulation. Phys Fluids 28(5):056101. https ://doi.
org/10.1063/1.49472 44
Nayfeh AH, Saric WS (1971) Non-linear kelvin-helmholtz instabil-
ity. J Fluid Mech 46(2):209–231. https ://doi.org/10.1017/S0022  
11207 10004 91
Opfer L, Roisman IV, Venzmer J, Klostermann M, Tropea C (2014) 
Droplet-air collision dynamics: evolution of the film thick -
ness. Phys Rev E 89(1):013023. https ://doi.org/10.1103/PhysR 
evE.89.01302 3
Ortiz C, Joseph DD, Beavers GS (2004) Acceleration of a liquid 
drop suddenly exposed to a high-speed airstream. Int J Multiph 
Flow 30(2):217–224. https ://doi.org/10.1016/j.ijmul tipha seflo  
w.2003.11.004
Papamoschou D, Roshko A (1988) The compressible turbulent shear 
layer: an experimental study. J Fluid Mech 197(1973):453–477. 
https ://doi.org/10.1017/S0022 11208 80033 25
Pilch M, Erdman CA (1987) Use of breakup time data and velocity 
history data to predict the maximum size of stable fragments for 
acceleration-induced breakup of a liquid drop. Int J Multiph Flow 
13(6):741–757. https ://doi.org/10.1016/0301-9322(87)90063 -2
Ranger AA, Nicholls JA (1969) Aerodynamic shattering of liquid 
drops. AIAA J 7(2):285–290. https ://doi.org/10.2514/3.5087
Reitz RD, Diwakar R (1986) Effect of Drop breakup on fuel sprays. 
SAE transactions, pp 218–227. https ://doi.org/10.4271/86046 9
Schmehl R (2003) Modeling droplet breakup in complex two-phase 
flows. In: 9th international conference on liquid atomization and 
spray systems, ICLASS 13-17 July 2003, Surrento, Italy
Shinjo J, Umemura A (2010) Simulation of liquid jet primary breakup: 
dynamics of ligament and droplet formation. Int J Multiph 
Flow 36(7):513–532. https ://doi.org/10.1016/j.ijmul tipha seflo  
w.2010.03.008
Lagutkin S, Achelis L, Sheikhaliev S, Uhlenwinkel V, Srivas-
tava V (2004) Atomization process for metal powder. Mater 
Sci Eng A 383(1 SPEC. ISS.):1–6. https ://doi.org/10.1016/j.
msea.2004.02.059
Stapper BE, Samuelsen GS (1990) An experimental study of the 
breakup of a two-dimensional liquid sheet in the presence of co-
flow air shear. In: 28th aerospace sciences meeting, p 461. https  
://doi.org/10.2514/6.1990-461
Stapper BE, Sowa WA, Samuelseni GS (1992) An Experimental study 
of the effects of liquid properties on the breakup of a tiro-dimen-
sional liquid sheet. J Eng Gas Turb Power 114(1):39–45.  https ://
doi.org/10.1115/1.29063 05
Theofanous TG (2011) Aerobreakup of newtonian and viscoelas-
tic liquids. Annu Rev Fluid Mech 43(1):661–690. https ://doi.
org/10.1146/annur ev-fluid -12210 9-16063 8
Theofanous TG, Li GJ (2008) On the physics of aerobreakup. Phys 
Fluids 20(5):052103. https ://doi.org/10.1063/1.29079 89
Theofanous TG, Li GJ, Dinh TN (2004) Aerobreakup in rarefied 
supersonic gas flows. J Fluids Eng 126(4):516. https ://doi.
org/10.1115/1.17772 34
Theofanous TG, Mitkin VV, Ng CL, Chang C-H, Deng X, Sushchikh 
S (2012) The physics of aerobreakup. II. Viscous liquids. Phys 
Fluids 24(2):022104. https ://doi.org/10.1063/1.36808 67
Villermaux E, Bossa B (2009) Single-drop fragmentation determines 
size distribution of raindrops. Nat Phys 5(9):697–702. https ://doi.
org/10.1038/nphys 1340
Xiao F, Wang ZG, Sun MB, Liu N, Yang X (2017) Simulation of drop 
deformation and breakup in supersonic flow. Proc Combust Inst 
36(2):2417–2424. https ://doi.org/10.1016/j.proci .2016.09.016
 
Publisher’s Note Springer Nature remains neutral with regard to 
jurisdictional claims in published maps and institutional affiliations.
