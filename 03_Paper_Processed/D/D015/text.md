<!-- PDF_PAGE: 1 -->

Full Length Article
Effect of spray characteristics on the dynamic characteristics and mode 
distribution pattern of kerosene/air detonation
Wenkai Qin , Haocheng Wen
*
, Bing Wang
School of Aerospace Engineering, Tsinghua University, Beijing 100084, PR China
ARTICLE INFO
Keywords:
Rotating detonation
Spray characteristics
Extinction
Two-phase combustion
Kerosene
ABSTRACT
In the study, an experimental investigation of kerosene/air two-phase rotating detonation combustors using 
various types of atomizers is conducted. The spray flow field and mixing process of the atomizers are evaluated 
through planar laser-induced fluorescence and schlieren methods. The spatio-temporal trajectories of the 
rotating detonation wave (RDW) are converted into θ -t diagrams and analyzed alongside a reduced-order nu -
merical model to explore the dynamic characteristics of RDW. Multiple combustion modes are observed, 
including single-wave mode, counter double-wave mode, longitudinal pulse detonation (LPD), and mode tran -
sitions, as well as initiation and extinction phenomena. Results indicate that the velocity deficits of RDWs 
increased with larger wavenumbers. In the single-wave mode, deficits increase and then decrease as the 
equivalence ratio ( φ
t
) varies from 0.7 to 1.0, attributed to non-ideal spray characteristics. The coupling between 
spray characteristics and RDWs significantly influences wave evolution during dynamic processes, exhibiting 
disequilibrium during initiation and extinction, with feedback processes approximating LPD behavior. In 
contrast, critical equilibrium is observed during mode transitions, where dynamic changes in spray character -
istics can lead to the emergence of new modes. In stable modes, the number of RDWs increases when the oxidizer 
flow rate rise and φ
t 
decreases, resulted by smaller characteristic droplet sizes. With poor atomization quality, 
stable rotating detonation is difficult to achieve, leading to extinction or unstable modes. Furthermore, 
increasing the combustor channel width reduces back pressure of the atomizers and the velocity deficit of RDWs, 
promoting the formation of single-wave mode and helping to avoid extinction.
1. Introduction
First realized by Voitsekhovskii [ 1 ] in the 1950s, rotating detonation 
engine (RDE) has been widely regarded as a promising future propulsion 
technology due to its potential advantages of pressure gain and high 
thermal efficiency [ 2 , 3 ]. Owing to the widespread use of kerosene in 
aerospace propulsion, kerosene-based hydrocarbons are undoubtedly 
the preferred fuels for air-breathing RDEs. However, the use of kerosene 
in liquid – gas two-phase rotating detonation involves the spray process 
of fuel, including atomization, evaporation, and mixing [ 4 – 8 ]. This 
causes the combustion process to be complex, and the role of spray 
characteristics has not been fully recognized.
The nature of liquid – gas two-phase injection has significant impact 
on the flow field structure of two-phase rotating detonation wave, 
making it differ from those of gas-phase RDW. Recent researches have 
indicated that there exists a micro-explosion phenomenon caused by 
incomplete droplet evaporation. Larger droplets ( > 10 μ m) are unable to 
fully evaporate and burn within the current RDW, but instead migrate 
downstream and undergo secondary combustion [ 9 , 10 ]. They are ulti -
mately ignited at the contact point of the following RDW, leading to the 
formation of micro-explosions. The micro-explosions are strong enough 
to induce a secondary RDW close to the primary RDW and generate 
transverse waves, or to produce opposite-direction shock waves 
[ 9 , 11 , 12 ]. Similarly, due to the poor mixing effects caused by the two- 
phase injection, the recirculation zone of air is enlarged [ 13 ], and the 
length of the reaction zone also increases [ 10 , 14 , 15 ]. Huang et al. [ 16 ] 
also showed that droplet evaporation can form an evaporation wave, 
which couples with the incident shock wave and propagates together. 
Only when the atomized droplet size is relatively small (~5 μ m) can flow 
field structures similar to those of pure gas-phase detonation be 
observed, according to Salvadori et al. [ 17 ]. As a special case, detona -
tion waves can be stably maintained even when the droplets are all 
attached to the wall [ 18 ]. Therefore, the influence of spray character -
istics on two-phase RDW propagation is an important subject of 
research, but there is a lack of in-situ measurement results under RDE 
* Corresponding author.
E-mail address: wen@tsinghua.edu.cn (H. Wen). 
Contents lists available at ScienceDirect
Fuel
journal homepag e: www.else vier.com/loc ate/fuel
https://doi.org/10.1016/j.fuel.2026.138720
Received 23 April 2025; Received in revised form 4 January 2026; Accepted 7 February 2026  
Fuel 418 (2026) 138720 
Available online 16 February 2026 
0016-2361/© 2026 Elsevier Ltd. All rights are reserved, including those for text and data mining, AI training, and similar technologies.

<!-- PDF_PAGE: 2 -->

conditions.
Droplet size is an important indicator for evaluating spray charac -
teristics, and there have been valuable discussions regarding its effect on 
detonation characteristics. Previous experiments of liquid dieth -
ylcyclohexane (290 – 2600 μ m), decane (5 – 10 μ m) and dodecane (8 – 20 
μ m) detonation [ 19 – 21 ] show that the velocity deficit increase as the 
particle sizes increase, and the cell size is about twice that of gaseous 
detonation. Benmahammed et al. [ 22 ] further concluded that droplet 
diameter is a limiting factor for detonability. Droplet sizes is also criti -
cally important for rotating detonation [ 23 ]. Smaller droplets (~5 μ m) 
can evaporate completely within the RDW, while larger droplets ( > 20 
μ m) undergo secondary evaporation after the RDW and are consumed in 
the form of deflagration [ 15 , 24 , 25 ], resulting in an increase in velocity 
deficit as the droplet sizes increase [ 25 – 27 ]. Cao et al. [ 26 ] discovered 
that larger droplets also cause the reaction zone and the RDW to separate 
from the contact point and form a λ -shaped structure. By preheating the 
liquid fuel, both the evaporation of droplets and the mixing of two-phase 
jets are enhanced [ 28 ], which benefit the self-sustainment of RDW. 
However, Jin et al. [ 29 ] argued that preheated air can cause the auto- 
ignition of kerosene vapor in the filling zone. Li et al. [ 15 , 30 ] added 
that under fuel-lean or small droplets (5 μ m) condition, the contact 
between the mixed recants and the high-temperature products before 
RDW can lead to pre-ignition and perturb the flow field. Limited by 
observational methods, researches on the effect of droplet size were 
mainly numerical simulations, and thus could not fully reflect the flow 
field in an actual RDE.
In two-phase RDE experiments, mass flow rate ( ˙m ) and equivalence 
ratio ( φ ) are typically used for describing operating conditions, thus 
establishing a connection with the characteristics of RDW. Existing 
research on combustion mode indicated that, the number of RDW in -
creases with rising kerosene mass flux and decreasing φ [ 31 , 32 ]. 
Increasing φ near the fuel-lean limit enhances the peak pressure and 
stability of RDWs [ 33 ]. Similarly, increasing the oxygen content at the 
same kerosene mass flux results in higher RDW velocities, reaching up to 
95% V
CJ 
[ 34 ]. Furthermore, the peak pressure of RDWs shows an inverse 
relationship with the number of RDWs [ 35 ]. The number of RDWs may 
vary during operation (i.e., mode transition) even when the injection 
parameters remain constant, but the underlying mechanisms and evo -
lution are still not well understood [ 36 , 37 ]. However, due to difficulties 
of in-situ flow and heat release diagnostics, only some researchers 
conducted indirect or qualitative measurements (e.g. OH* chem -
iluminescence and heat flux) of RDW [ 38 – 42 ]. There are few studies that 
consider spray characteristics as an operating parameter or focus on the 
impact of spray characteristics on RDW [ 6 , 13 , 24 ], lacking quantitative 
correlations between spray characteristics and the RDW properties. 
Furthermore, ˙m and φ are usually measured in a quasi-steady pipeline 
upstream of the combustor, making it challenging to characterize the 
dynamic properties of RDW during the highly transient processes of 
ignition, extinction, and mode transition [ 43 – 45 ]. Hence, it is necessary 
to introduce new dynamic analysis methods.
The RDWs also have a feedback effect on the spray process in two- 
phase RDE. Recovery of the fuel and oxidizer injectors may not be 
simultaneous and leads to uneven distribution of reactants [ 46 , 47 ]. The 
peak pressure of single-wave mode is ~50% higher than that of dual- 
wave mode, resulting in greater disturbances to the oxidizer plenum 
[ 32 ]. However, pressure disturbances caused by RDWs can be sup -
pressed by altering the intake structure [ 48 – 50 ]. Due to the feedback 
effect of RDW, the spray characteristics may interact with it during 
dynamic processes, and the mechanisms and control methods involved 
remain inconclusive.
This paper examines the influence of spray characteristics on the 
steady characteristics, dynamic processes, and combustion modes of 
RDWs. Five combinations of combustors and atomizers are designed to 
achieve distinct spray properties, and a series of analytical methods are 
employed to analyze the dynamic processes. Mode distribution patterns 
are observed experimentally, and the effects of parameters are explored, 
aiding by the reduced order numerical model for RDW.
2. Experimental and analytical methodology
2.1. Experimental setup for two-phase rotating detonation
The fuel used is RP-3 aviation kerosene (C
10.623
H
19.687
, M
r 
= 147.2) 
[ 51 ], which has a density of 792 kg/m
3 
at 20
◦
C. The oxidizer is a gas 
mixture of oxygen and nitrogen (O
0.8
N
1.2
, M
r 
= 29.6), featuring an ox -
ygen volume fraction of 40.0 ± 0.5%. Under stoichiometric condition, 
the fuel-to-oxidizer mass ratio (F/O)
st 
is 0.128.
The schematics of the experiment system are depicted in Fig. 1a . The 
mass flow measurement of oxidizer is conducted directly with an 
EMERSON K200S (accuracy: ± 0.5%). Kerosene is supplied by nitrogen 
pressurization, with a turbine flow meter (Asmik DN10, accuracy: 
± 0.5%) installed to measure its volumetric flow. The N
2 
pressure can be 
obtained from the high-pressure side reading of reduction valve con -
nected to the N
2 
tank (accuracy: ± 2.0%). The mass flow rate of kerosene 
is calculated based on its known density (accuracy: ± 1.0%). A NI PXIe- 
1082 and PXIe-6368 are utilized for signal acquisition and timing con -
trol. The achievable oxidizer flow rate ranges from 0.3 to 2.0 kg/s, while 
the kerosene flow rate ranges from 0.04 to 0.13 kg/s. The ambient 
temperature is maintained at 20 ± 5 
◦
C throughout the experiment, 
which introduces an extra ± 0.5% error in kerosene mass flow rate aside 
from instrumental error.
Fig. 1b illustrates the rotating detonation device used in the experi -
ment. The oxidizer and kerosene first entered the oxidizer plenum and 
kerosene plenum, respectively. They are then atomized and injected into 
the annular combustor through atomizers mounted on the injection 
panel. The exhaust gases are subsequently discharged to the 
atmosphere.
The annular combustor is equipped with 30 atomizer units evenly 
distributed along the circumferential direction of the injection panel. 
The nozzle has a cone angle of 40
◦
, with the cross-sectional area of the 
throat equaling to that of the combustor.
The primary dimensions of the combustor are annotated in Fig. 2 , 
where L
c 
represents the combustor length, D
c1 
and D
c2 
denote the inner 
and outer diameters of the combustor, respectively. D
inj 
refers to the 
installation diameter of the injectors. Two combustors, C1 and C2, are 
designed to investigate the influence of the combustor channel width 
( W
c 
= ( D
c2
- D
c1
)/2). The channel width of combustors C1 and C2 are 15 
mm and 20 mm, respectively, while the other dimensions remained 
unchanged (see Table. 1 ) .
Two atomizer configurations are employed in the experiment 
( Fig. 3 ). Both configurations feature a kerosene injection hole diameter 
Nomenclature
A
+
Injection area ratio
A

Outlet contraction ratio
D
32
Sauter mean diameter, μ m
˙m
O , t
Actual oxidizer mass flow rate, kg/s
V
CJ
Chapman-Jouguet velocity, m/s
κ Mixing rate coefficient
λ Reaction progress
φ
t
Actual equivalence ratio
LPD Longitudinal pulse detonation
PDF Probability density distribution
PLIF Planar laser-induced fluorescence
PSD Power spectral density
RDE Rotating detonation engine
RDW Rotating detonation wave
RFI Relative fluorescence intensity
W. Qin et al.                                                                                                                                                                                                                                     Fuel 418 (2026) 138720 
2

<!-- PDF_PAGE: 3 -->

of D
0 
= 0.45 mm, a swirl chamber diameter of D
s 
= 3.0 mm, and a total 
cross-sectional area of 0.56 mm
2 
at the inlet. Configuration I utilizes an 
annular oxidizer injection gap, whereas Configuration II incorporates 12 
oxidizer injection holes.
Furthermore, three different atomizers are designed to achieve 
various spray characteristics (droplet size, mixing rate, etc.), as detailed 
in Table. 2 . Atomizers A1 and A2 both adopt Configuration I, while A2 
having a larger D
2
. Atomizer A3 employs Configuration II. The oxidizer 
injection area of atomizers A1, A2, and A3 are designed to be approxi -
mately equal.
In terms of the time sequence, the kerosene valve is opened between 
T =  0.2 s and T = 1.0 s, while the oxidizer valve is opened between T =
0 s and T = 1.2 s. Data acquisition, imaging, and ignition begin at T = 0, 
0.3, and 0.45 s, respectively. The combustion duration is set at 500 ms, 
during which the maximum fluctuation of mass flow rates remains 
within 2%.
Two static pressure sensors (OMEGA PX409, 1 kHz sampling rate) 
are installed in the plenums to measure the pre-injection pressures of the 
oxidizer and kerosene. Six dynamic pressure sensors (PCB 113B24, 1 
MHz sampling rate) are mounted on the outer wall of the combustor and 
are labeled as PCB1 ~ PCB6. Three OMEGA PX409 are used to gauge the 
axial average pressure distribution within the combustor, denoted as 
Pc1 ~ Pc3. In addition, an ignition rod (with ignition energy of ~1 J) is 
installed for initiation. The layout of the sensors is illustrated in Fig. 2 . 
All sensors and ignition rod are fixed at six circumferential positions 
spaced 30
◦
apart. Pc1 ~ Pc3 feature an axial spacing of 50 mm. The axial 
spacing of PCB2 & 3, as well as PCB4 & 5, is 35 mm. PCB1/2/4/6 and Pc1 
are positioned 20 mm away from the injection panel.
2.2. Experimental set up for atomizer spray characteristics
High-speed schlieren imaging, planar laser-induced fluorescence 
(PLIF), and a granulometer (Spraylink E) are utilized to investigate the 
spray characteristics of atomizers A1 to A3, including steady-state 
droplet sizes and spray structure. Ex-situ measurements of atomizers 
are conducted under a typical steady back pressure of 0.1 MPa. The 
schematics of the spray characteristics measurement system is shown in 
Fig. 4 .
The high-speed schlieren imaging system employs a 400 W halogen 
lamp, two concave mirrors with an effective aperture of 96 mm, and a 
high-speed camera (Ispeed 726) for image acquisition. The granul -
ometer (Sparylink E, DV50 accuracy and repeatability: ± 0.5%) emits a 
638 nm laser beam toward the liquid mist and measures the angular 
variation in intensity of light scattered after the beam passes through. 
The characteristic droplet sizes are calculated according to the scattering 
pattern using Mie theory of light scattering [ 52 ]. However, the schlieren 
imaging system and the granulometer share the same light path and 
cannot be operated simultaneously.
The PLIF system is detailed in Fig. 4b . A Laser beam is produced by a 
Nd:YAG solid-state pump source and then passes sequentially through a 
dye laser, doubling crystals, and a series of optical lens to form a laser 
sheet. 5 wt% acetone is added to kerosene as the tracer, as its fluores -
cence can be excited by the laser. Fluorescence images are captured by 
an ICCD camera aligned parallel to the laser sheet, with a 370 – 400 nm 
Fig. 1. Schematics of (a) the two-phase rotating detonation experiment system and (b) the rotating detonation device.
W. Qin et al.                                                                                                                                                                                                                                     Fuel 418 (2026) 138720 
3

<!-- PDF_PAGE: 4 -->

narrowband filter installed in front of it. The PLIF system is synchro -
nously controlled through a digital pulse/delay generator.
2.3. Analytical method for dynamic characteristics of RDW
Various approaches are utilized to analyze the dynamic character -
istics of RDW, including the θ - t diagram, interpolated θ - t diagram, and 
reduced order numerical model for RDW. The original data mainly 
consist of high-frequency pressure data and high-speed images, based on 
which further detailed studies are conducted.
(1) θ -t diagram .
The θ - t diagram is reconstructed from the high-speed imaging taken 
from the rear of the combustor, using a fixed frame rate of 30,000 fps 
and a shutter speed of 1/30,000 s. In each image, pixels located at the 
mid-diameter (marked by the red dashed circle in Fig. 5 ) of the 
combustor channel are extracted in circumferential order, color- 
inverted, and arranged in a column. By organizing these pixel columns 
in time order, the θ -t diagram is obtained. The darker the pixel, the more 
intense the reaction, and the darkest pixels indicate the position of 
RDWs. The velocity of RDW can be calculated accordingly from the 
duration of one period.
(2) Interpolated θ -t diagram .
The interpolated θ - t diagram is reconstructed from high-frequency 
pressure data. During ignition or extinction, optical measurements are 
not available due to the bright flame around the nozzle, so the 
Fig. 2. (a) Front view and (b) Right-side view of the combustor and layout of sensors. (c) Schematics of the ignition rod.
Table 1 
Dimensions of the kerosene/air two-phase rotating detonation combustor.
Type W
c 
(mm) D
c1 
(mm) D
c2 
(mm) D
inj 
(mm) L
c 
(mm)
C1 15 120 150 135 200
C2 20 110
Fig. 3. Structures and dimensions of the atomizers. (a) Configuration I. (b) Configuration II.
Table 2 
Geometric parameters of three types of atomizers.
Type Configuration D
1 
(mm) D
2 
(mm)
A1 I 9.5 11.7
A2 I 10.5 12.8
A3 II 7.5 11.5
W. Qin et al.                                                                                                                                                                                                                                     Fuel 418 (2026) 138720 
4

<!-- PDF_PAGE: 5 -->

interpolated θ - t diagram is used instead. Pressure data of PCB1/2/4/6 
are employed to plot the interpolated θ - t diagram. In each pixel column, 
the gray levels of pixels 1/2/4/6 are mapped from the standardized 
pressure of PCB1/2/4/6, while pixel 3/5 are filled through linear 
interpolation. It is important to note that the interpolated θ - t diagram 
can only depict half of the flow field inside the combustor. Further 
charting details can be found in Fig. 5 .
(3) Reduced order numerical model for RDW .
In the rotating detonation combustor, physical processes such as 
atomization, mixing, and combustion that significantly influence the 
dynamics of the RDW primarily occur within a small annular layer at its 
head. A one-dimensional model for RDW is derived using the lumped- 
volume method [ 53 ] to approximate the flow field in this region. The 
reduced order numerical model draws on concepts from this method. 
The reduced order numerical model for RDW can be expressed as: 
∂
∂ t
⎛
⎜
⎜
⎝
ρ
ρ u
E
ρ λ
⎞
⎟
⎟
⎠
+
∂
∂ x
⎛
⎜
⎜
⎝
ρ u
ρ u
2
+ p
uE + up
ρ u λ
⎞
⎟
⎟
⎠
=
⎛
⎜
⎜
⎜
⎜
⎝
˙m
0
 ˙m
1
0
˙m
0
e
0
 ˙m
1
e
1
+ ˙ω q
˙ω  ρ κ H + λ ˙m
0
 λ ˙m
1
⎞
⎟
⎟
⎟
⎟
⎠
(1) 
where λ is the reaction progress variable ( λ = 0 indicates unreacted 
state). The mixing rate coefficient κ is an independently defined 
coefficient (equivalent to the H / s in [ 53 ]), which comprehensively 
characterizes the intensity of the atomization, evaporation, and mixing 
processes. A larger κ results in a faster recovery of λ . The injection area 
ratio and outlet contraction ratio are defined as A
+
= A
inj
/A and 
A

= A
exit
/A , where A
inj 
and A
exit 
represent the areas of the injection gap 
and the nozzle throat, respectively [ 53 ].
In the following simulations, the reactants consist of stoichiometric 
kerosene vapor and oxygen-enriched air (O
0.8
N
1.2
). The dimensionless 
specific heat ratio, calorific value, von Neumann temperature, activation 
energy, and Damkohler number of the reactants are γ = 1.2, q = 54.5, 
T
VN 
= 6, E
a 
= 10, and Da = 22, respectively. Additionally, the numerical 
θ - t diagrams of pressure and reaction progress are generated from nu -
merical results, which correspond to the circumference of the 
combustor. More details are available in Appendix A .
Fig. 6 presents comparisons among θ - t diagram, interpolated θ - t di -
agram, and numerical θ - t diagram. In the counter double-wave mode, 
both experimental and numerical results exhibit steady wave velocities 
and collision points. The two oppositely moving RDWs maintain the 
same velocities and intensities, remaining stable during propagation. In 
the LPD mode, RDWs are periodically reignited but quickly decay within 
each cycle. The numerical result in Fig. 6d captures the decoupled re -
action zones and shock waves following collisions, along with the re -
sidual pressure waves. In the single-wave mode, both Fig. 6e & f illustrate 
Fig. 4. Schematics of (a) granulometer and high-speed schlieren imaging system, and (b) planar laser-induced fluorescence system.
W. Qin et al.                                                                                                                                                                                                                                     Fuel 418 (2026) 138720 
5

<!-- PDF_PAGE: 6 -->

that a single wave of fixed wave velocity forms ultimately. It is evident 
that the numerical results closely align with the experimental observa -
tions, demonstrating their effectiveness for dynamic characteristics 
analysis.
3. Spray and mixing characteristics of atomizers
This study employs high-speed schlieren imaging to visualize the 
spray flow field of three atomizers and utilized PLIF system to analyze 
the mixing characteristics of kerosene atomizers under steady back 
Fig. 5. Drawing methods of θ -t diagram and interpolated θ -t diagram.
Fig. 6. Counter double-wave mode in (a) θ - t diagram and (b) numerical θ - t diagram. LPD in (c) θ - t diagram and (d) numerical θ - t diagram. Single-wave mode in (e) 
interpolated and (f) numerical θ - t diagram.
W. Qin et al.                                                                                                                                                                                                                                     Fuel 418 (2026) 138720 
6

<!-- PDF_PAGE: 7 -->

pressure. Additionally, a granulometer measures the distribution of 
characteristic atomized droplet sizes. Due to the use of an axisymmetric 
atomizer layout in firing tests, and considering symmetry as well as the 
single-point measurement characteristics of the devices, a 1/30 sector is 
employed for single-point measurement of steady-state spray charac -
teristics. The representative back pressure of steady-state test is p
amb 
=
100 kPa, and the measurement results are then used for the analysis of 
RDW properties.
The atomizers become blocked upon the arrival of RDWs, and 
gradually recover behind the waves as the pressure decreases. However, 
the pressure drop behind the RDWs is nearly exponentially. The back 
pressure of the atomizers quickly reduces to a low level (~0.1 MPa) and 
then stabilizes with minor fluctuations ( Fig. 14b ). Therefore, spray 
characteristics measured under representative steady back pressures 
approximately characterize the atomizer ’ s average performance inside 
the combustor.
3.1. Spray characteristics
To align with the parameters used in the ignition tests, it is necessary 
to determine the parameters during the steady back pressure tests. Here, 
the equivalent total oxidizer mass flow rate ˙m
O , t 
is defined as 30 times of 
the oxidizer flow rate of a single atomizer under the same injection 
pressure. The total spray equivalence ratio φ
t 
is given by: 
φ
t
=
˙m
F , t
˙m
O , t
( F / O )
st
, ( F / O )
st
= 0 . 128 (2) 
In the context of the ignition tests, ˙m
O , t 
and φ
t 
represent the actual 
oxidizer mass flow rate and equivalence ratio, respectively.
The spray flow field structure of atomizers A1 to A3 is obtained by 
averaging 100 frames of transient high-speed schlieren images (5000 
fps, 1/200000 s shutter speed), as shown in Fig. 7 . The oxidizer jets from 
atomizers A1 and A2 exhibit a converging trend at the outlet, while the 
oxidizer jet from atomizer A3 creates strong shock trains downstream, 
leading to significant total pressure loss and weakened mixing of kero -
sene droplets. Kerosene first undergoes primary swirl atomization at the 
center of the atomizers, and subsequently collides with the high-speed 
oxidizer jets downstream. This collision produces effective secondary 
atomization and mixing of the kerosene through strong shear force, and 
forms small fuel droplets ( < 5 μ m) for stable rotating detonation under 
room temperature condition.
It is evident that, despite structural differences, all three atomizers 
exhibit a similar atomization mechanism. The primary atomization of 
kerosene occurs through the central swirling atomizer, followed by the 
secondary atomization of droplets facilitated by the shear forces from 
the collision with high-speed oxidizer jets. Mixing gradually completes 
downstream. Direct measurements of velocity distribution and spread 
angle of atomizers are not conducted due to complexity of in-situ mea -
surements. There might be collisions between propellants and channel 
walls under RDWs, which will affect the transportation of droplets as 
well as the stability of RDWs to some degree.
3.2. Mixing characteristics
PLIF is employed to measure the spray flow field of the kerosene/ 
acetone mixture. By averaging 30 frames of transient fluorescence im -
ages (10 fps), the acetone fluorescence distribution at the central cross- 
section is obtained. Fig. 8 reveals a kerosene-rich zone at the atomizer 
outlet, where the kerosene droplets have not yet undergone complete 
secondary atomization and have not mixed with the oxidizer jet. The 
core of the kerosene jet rapidly contracts downstream of the atomizer, 
and the kerosene concentration decreases, indicating that the kerosene 
gradually mixes with the oxidizer.
The measured fluorescence intensity is primarily determined by 
acetone concentration and solvent effect of kerosene, and does not have 
a strict linear relationship with kerosene concentration. Therefore, the 
normalized relative fluorescence intensity (RFI) is used to represent the 
relative concentration of kerosene. The axial distributions of RFI for the 
three atomizers are shown in Fig. 9 , where x  = 0 mm corresponds to the 
outlet cross-section. Fig. 8 and Fig. 9 suggest that atomizer A3 exhibits 
the smallest rate of RFI decrease along the axis, indicating the poorest 
mixing performance due to the weakest shear effects of the oxidizer jets 
on the kerosene. In contrast, the spray fields of atomizers A1 and A2 
display similar structures and achieve effective mixing over a short 
distance.
3.3. Atomized particle size
To avoid interference from strong shock waves near the outlet, the 
measurement area is selected to be 50 mm downstream of the atomizer, 
which is the approximate location of the RDW in most cases. The light 
spot diameter of the granulometer is 15 mm. In this study, the widely- 
used Sauter mean diameter D
32 
is employed to quantify the character -
istic droplet sizes. Let N
i 
represent the number of droplets of diameter d
i
, 
the definition of D
32 
is given by: 
D
32
=
∑
N
i
d
3
i
∑
N
i
d
2
i
(3) 
Fig. 10 illustrates the distribution of D
32 
relative to ˙m
O , t 
and φ
t 
for at -
omizers A1 to A3. It is evident from Fig. 10 that the characteristic 
droplet size decreases gradually as ˙m
O , t 
increases and φ
t 
decreases. When 
˙m
O , t 
and φ
t 
are in the range of 0.5 – 1.0 kg/s and 0.6 – 1.2, respectively, the 
Fig. 7. Time average high-speed schlieren images of the spray field. The actual oxidizer flow rate is 23 ± 0.7 g/s. Equivalent ˙m
O , t
: 0.70 ± 0.02 kg/s, equivalent φ
t
: 
0.83 ± 0.02.
W. Qin et al.                                                                                                                                                                                                                                     Fuel 418 (2026) 138720 
7

<!-- PDF_PAGE: 8 -->

characteristic droplet size of atomizer A3 is 3.6 – 5.2 μ m, while that of 
atomizers A1 and A2 is 3.2 – 3.6 μ m. Thus, the atomization qualities of A1 
and A2 are comparable, and A3 exhibits the worst atomization quality. 
Since in-situ droplet size measurements are not applicable, the ex-situ 
results (i.e., Fig. 10 ) are taken as characteristic droplet size to repre -
sent the droplet sizes under RDE conditions.
4. Steady characteristics of rotating detonation waves
4.1. Overall profile
A series of two-phase rotating detonation experiments are conducted 
by controlling key variables such as the type of atomizer, combustor 
channel width, ˙m
O , t
, and φ
t
. In the following text, case A1C1-0.50 – 0.83 
indicates that a combination of atomizer A1 and a combustor C1 is used, 
with a ˙m
O , t 
of 0.50 kg/s, and a φ
t 
of 0.83, and so on.
Various modes, including single-wave mode, double-wave mode (co- 
rotating and counter), counter four-wave mode, LPD, extinction, and 
mode transition, are obtained, allowing for the simultaneous maintenance 
of up to four RDWs. The typical θ - t diagrams of these stable modes are 
presented in Fig. 11 , with dashed lines indicating the RDWs. During 
observation, all RDWs exhibit stable velocity without any decay, as indi -
cated by the parallel straight lines, and the collision points of multi-wave 
modes remain relatively stationary. Fundamental frequencies and their 
harmonics are also identified in the Power spectral density (PSD) dia -
grams. Corresponding details can be found in the Supplementary Material .
Generally, as the number of RDWs increases, the velocity deficit in -
creases under similar ˙m
O , t 
and φ
t
. CEA software [ 54 ] is employed to 
calculate the theoretical CJ velocity ( V
CJ
) of kerosene surrogate (Jet-A) 
and oxygen-enriched air (O
2 
+ 1.5 N
2
), with initial temperature and 
pressure set at 300 K and 100 kPa, respectively. Consequently, the ve -
locity deficit can be derived. The approximate velocity deficit for single- 
wave, co-rotating double-wave, counter double-wave, and counter four- 
wave mode are ~0.15 V
CJ
, ~0.3 V
CJ
, ~0.35 V
CJ
, and ~0.45 V
CJ
, respec -
tively. This indicates that more frequent collisions between the RDWs 
result in greater dissipation, making a larger number of RDWs unfa -
vorable for the steady propagation of the RDWs.
4.2. Single-wave mode
Single-wave mode represents the simplest form of rotating detona -
tion, characterized by one stable RDW that periodically rotates in the 
combustor while maintaining stable wave velocity and pressure. In a 
typical single-wave mode (case A1C2-0.71 – 1.02, see Section 1.1 of 
Supplementary Material ), the wave velocity remains constant over time. 
The measured RDW velocities is 1728 m/s, with a velocity deficit of 
0.15 V
CJ
.
Additionally, the RDW velocity characteristics of single-wave mode 
are analyzed statistically. The average RDW velocities over 50 periods 
are calculated for Type A1C2 (combination of atomizer A1 and 
combustor C2, and similarly for others) and A2C2 across a range of φ
t 
as 
shown in Fig. 12 , where ˙m
O , t 
is set to either 0.7 kg/s or 1.0 kg/s. Type 
A1C2 and A2C2 are represented by squares and dots, respectively. The 
dashed lines indicate 0.8 V
CJ 
and 0.9 V
CJ
, respectively.
The observed RDW velocities in the experiments primarily fall within 
the range of (0.8~0.9) V
CJ
, indicating a velocity deficit of approximately 
(0.1~0.2) V
CJ
. This velocity deficit is attributed mainly to the following 
reasons: (1) Kerosene enters the combustor as droplets. A portion of the 
droplets ( Fig. 10 ) have larger diameters, requires a longer evaporation 
time, and does not fully participate in the detonation. These unburned 
droplets undergo deflagration behind the RDW, the resulting energy 
dissipation contribute to the observed velocity deficit; (2) The actual 
spray field in the combustor is neither uniform nor premixed, particu -
larly in the downstream area. Local enrichment of kerosene leads to 
incomplete combustion, contributing to overall inhomogeneity; (3) In 
the refilling zone of the combustor, some droplets are attached to the 
wall, while others deflagrate on the contact surface. This reduces the 
amount of kerosene participating in the detonation, resulting in 
decreased thermal efficiency and an increased velocity deficit. Other 
factors related to droplets, including commensal combustion and recir -
culation zone, will also affect the velocity deficit [ 38 , 46 ].
Atomizer A1 exhibits stable single-wave or multiple-wave modes in 
most cases, while atomizer A2 struggles to form stable modes (see Sec -
tion 6 ). Despite to the significant differences in mode distribution pat -
terns reflecting the dynamic characteristics, the differences in RDW 
velocities are not substantial. This indicates that the mode distribution 
pattern is more sensitive to changes in spray characteristics compared to 
the RDW velocity. As shown in Fig. 12 , increasing ˙m
O , t 
results in a slight 
Fig. 8. Acetone fluorescence distribution at the central cross-section. The actual oxidizer flow rate is 23 ± 0.7 g/s. Equivalent ˙m
O , t
: 0.70 ± 0.02 kg/s, equivalent φ
t
: 
0.83 ± 0.02.
Fig. 9. Axial RFI distribution of atomizers A1, A2 and A3.
W. Qin et al.                                                                                                                                                                                                                                     Fuel 418 (2026) 138720 
8

<!-- PDF_PAGE: 9 -->

Fig. 10. Contour map of D
32 
relative to equivalent ˙m
O , t 
and φ
t
, where equivalent ˙m
O , t 
is defined as 30 times of the oxidizer flow rate of the tested atomizer. (a) 
Atomizer A1 and A2, (b) Atomizer A3.
Fig. 11. θ - t diagram of (a) Single-wave mode, (b) Co-rotating double-wave mode, (c) Counter double-wave mode, (d) Counter four-wave mode, and (e) LPD.
W. Qin et al.                                                                                                                                                                                                                                     Fuel 418 (2026) 138720 
9

<!-- PDF_PAGE: 10 -->

increase in the RDW velocity deficit. When ˙m
O , t 
is raised from 0.7 kg/s to 
1.0 kg/s, the velocity deficit increases by approximately (0.01~0.03) 
V
CJ
, as a result of the more abundant energy supply. As φ
t 
increases, the 
velocity deficit of both types first decreases and then increases, reaching 
a minimum near φ
t 
= 0.85. This nonlinear behavior is primarily due to 
local fuel enrichment caused by the non-uniform spray field. When the 
global φ
t 
approaches stoichiometric (i.e., 1.0), the local φ
t 
in the fuel 
enrichment zone may exceed 1.0, leading to incomplete combustion. 
Therefore, the velocity deficit arises from a series of non-ideal processes.
5. Dynamic characteristics of rotating detonation waves
Nonlinear and non-ideal dynamic processes, such as spray and 
mixing processes, contribute to the complex dynamic characteristics of 
the rotating detonation waves. The coupling between spray character -
istics and RDWs dominates the dynamic properties, and initiation and 
extinction are examples of this coupling exhibiting disequilibrium. The 
disequilibrium is amplified and turns into chaotic combustion pattern in 
unstable modes. The system reaches critical equilibrium during mode 
transitions, as the waves lose stability and then quickly regain equilib -
rium. Spray characteristics influence the RDW by atomizing kerosene 
droplets and adjusting the energy supply, while RDWs affect the spray 
field through periodic disturbances as they rotate within the combustor. 
Therefore, the coupling between spray characteristics and RDWs plays 
an important role in dynamic processes. Specific analysis of different 
dynamic processes is presented below.
5.1. Initiation
Regardless of the stable combustion mode, the wave system exhibits 
similar evolution during initiation process. As shown in Fig. 13 , two 
RDWs propagating in opposite directions are formed after ignition. The 
two RDWs collide after one period and then extinguish due to insuffi -
cient reactant refilling. The flame core is blown downstream and reig -
nites the mixture after several milliseconds, indicating that the coupling 
of RDWs and spray characteristics has not yet reach equilibrium. By 
repeating this process, longitudinal pulses similar to LPD are obtained. 
In the example depicted in Fig. 13b , the two RDWs extinguish and 
reignite after collision, and eventually reach equilibrium after six pulses, 
which results in a stably maintained counter double-wave mode.
The coupling between the RDWs and the spray characteristics 
significantly impacts the initiation process. For the initiation process 
that eventually forms a stable mode ( Fig. 13b & c ), the peak pressure of 
the initial RDWs gradually decreases (as indicated by its fading color). 
This leads to a faster drop in pressure near the atomizers that dropping 
below the injection pressure, and results in quicker refilling of the re -
actants, indicated by the shortened pulse intervals (2 – 8 ms in Figs. 13b 
and 1-5 ms in Fig. 13c ). As intensity of the initial RDWs weakens, the 
operation of the atomizers stabilizes, and the interaction between the 
RDWs and spray characteristics approaches equilibrium (after 10 ms in 
Fig. 13b & c ). The mode of the stable detonation that forms later is related 
to supply parameters including ˙m
O , t 
and φ
t 
( Figs. 19 – 21 ). Additionally, 
stable LPD can also form when the coupling of RDWs and spray char -
acteristics reaches equilibrium in special case ( Fig. 13a ).
As shown in Fig. 13d , a stronger initial RDW can be achieved by 
enlarging the inertial area of initialization in the simulation. In this 
scenario, the initial field at t = 0 is specified as p = T = 1, λ = 0 ( x <
21.6), λ = 1 ( x > 21.6), with other settings unchanged. The inertial area 
is enlarged by 4.5 times, leading to LPD under parameters ( κ = 0.075, 
A
+
= 0.5) that would normally result in a single-wave mode ( Fig. 22 ). 
However, a rapid instability occurs at t = 200 and finally lead to a single- 
wave mode, indicating that a faster refilling rate of reactants cannot 
sustain LPD. Under critical conditions, excessively high intensity of 
RDWs prevents the stable operation of the atomizers, causing the 
counter double-wave to collide and extinguish soon (3 – 10 ms in 
Fig. 13a ). Nevertheless, the residual pressure waves are still sufficient to 
ignite the refilled mixture again, ultimately resulting in a stable LPD 
(after 10 ms in Fig. 13a ).
In fact, although the ignition processes may be similar, different 
supply parameters would induce distinct combustion modes. Specific 
combinations of ˙m
O , t 
and φ
t 
result in the formation of LPD, counter 
double-wave, and single-wave mode, respectively. Each set of supply 
parameters corresponds to only one mode, unless it lies at the boundary 
between two modes. This finding indicates an inherent relationship 
between the combustion modes and the system characteristics, which is 
not solely dependent on dynamic characteristics. Further discussion is 
provided in Section 6 .
5.2. Extinction
Extinction refers to the failure to maintain a continuously stable 
rotating detonation after ignition, resulting in instability that manifests 
as a degradation from detonation to deflagration. During this dynamic 
process, the flow velocity within the combustor may be too high to 
stabilize the flame, causing the flame core and reactants to be blown 
away. Therefore, a degenerated deflagration forms downstream of the 
combustor or even outside of it. Three types of extinction are observed in 
the experiments, each characterized by different evolution processes 
and mechanisms.
(1) Type I: Failed ignition
Type I extinction is closely associated with poor atomization quality. 
This occurs only with the use of the atomizer A3, as depicted in the 
interpolated θ - t diagram of Fig. 14a (case A3C1-0.70 – 0.81). Fig. 14b
compared the static pressure between Type I and Type II extinction. The 
measured peak pressure of Type I extinction is only 0.3 MPa, much 
lower than the 1.5 MPa peak pressure observed in Type II extinction. 
Moreover, the pressure drops rapidly within several milliseconds after 
the ignition. This pressure pattern indicates the absence of any RDW, 
signifying an ignition failure in Type I extinction.
In addition to the velocity deficit discussed in Section 4 , large 
droplets also contribute to the ignition failure. Atomizer A3, used in this 
study, produces larger characteristic droplet sizes and has the poorest 
mixing effect ( Fig. 9 & 10 ). The larger and heavier droplets may form a 
liquid mist that is not well mixed and cannot burn completely within 
RDW. These droplets undergo secondary combustion after the initial 
RDW and prevent the formation of new RDWs. As a result of poor spray 
characteristics, Type I extinction fails to generate new RDWs and only 
results in deflagration.
(2) Type II: High Equivalence ratio .
In Type II extinction, the initial RDW forms successfully but fails to 
Fig. 12. RDW velocities relative to ˙m
O , t 
and φ
t 
in single-wave mode for Type 
A1C2 and A2C2.
W. Qin et al.                                                                                                                                                                                                                                     Fuel 418 (2026) 138720 
10

<!-- PDF_PAGE: 11 -->

be sustained, primarily due to the coupling between the RDWs and spray 
characteristics. Fig. 15a presents the interpolated θ -t diagram of the 
pressure signal for case A1C2-1.00 – 0.86, where one stronger RDW and 
one weaker RDW propagate in opposite directions after ignition.
Due to the high φ
t
, both RDWs exhibit relatively high intensity and 
pressure. These stronger RDWs may disrupt the normal operation of the 
atomizers, likely impeding the refilling of reactants behind the waves. 
According to the numerical θ -t diagram of the reaction progress 
( Fig. 15c ), λ is relatively high before RDWs arrive, indicating an insuf -
ficient supply of propellants for detonation. Therefore, the two RDWs 
begin to decelerate before they collide due to a lack of reactants ( t ≈ 12 
in Fig. 15b ). After the collision, the shock waves quickly decouple from 
the reaction zone, and the refilling of reactants behind the waves be -
comes noticeably slower ( t ≈ 45 in Fig. 15c ). Numerical results display 
the same evolution pattern as the experiments, supporting the argument 
that stronger RDWs disturb the spray characteristics and verifying the 
feasibility of the numerical model. As the energy supply is insufficient to 
support counter double-wave mode (i.e., high λ at t ≈ 45 in Fig. 15c ), the 
waves quickly decay after the collision, and no new RDW form thereafter 
(2 – 3 ms in Fig. 15a ). This type of extinction typically occurs in high φ
t 
cases and only lasts for several milliseconds.
(3) Type III: Gradual extinction
Type III extinction exhibits a near-equilibrium coupling between the 
RDWs and spray characteristics. This type of extinction is more compli -
cate and shows a degree of randomness, positioning it closer to stability 
compared to other types of extinction. A typical scenario is illustrated in 
Fig. 16a (case A2C1-0.98 – 0.68), where an unstable mode emerges after 
ignition, and fluctuates between counter double-wave and single-wave 
mode. Following a period of evolution, this unstable mode can hardly 
maintain itself and finally extinguishes. Shortly after the unstable mode, 
an unsteady LPD forms at the end of the evolution, and the system ulti -
mately reaches deflagration after several pulses. The duration from 
ignition to deflagration in Type III extinction is on the order of 1 – 10 ms.
In Fig. 16a , the longitudinal pulse interval increases from 1.4 ms to 2.1 
ms before transitioning to deflagration, with the pulse strengths also 
increasing. This trend contrasts with the initiation process ( Fig. 13c ), 
where a stable mode forms after both pulse strengths and intervals 
decrease. A simulation with similar pattern ( Fig. 16b ) is conducted to 
explain these pulses, where κ is gradually decreased while keeping other 
parameters fixed ( A
+
= 0.3, A

= 0.8). As κ decreases from 0.09 to 0.07, 
Fig. 13. Wave evolution of (a) LPD, (b) counter double-wave mode, and (c) single-wave mode during initiation process (Time unit: ms). (d) Stronger RDWs is formed 
with larger inertial area ( κ = 0.075, A
+
= 0.5, and A

= 0.8).
W. Qin et al.                                                                                                                                                                                                                                     Fuel 418 (2026) 138720 
11

<!-- PDF_PAGE: 12 -->

the wave velocities of the counter double-wave mode slow down. With 
further reductions in κ , a LPD occurs. The intervals between longitudinal 
pulses continue to widen as κ decreased, eventually resulting in extinction.
These similar results indicate that Type III extinction is closely 
associated with the interaction between spray characteristics and the 
RDWs. A possible explanation of the pulses is the monotonic changes in 
spray characteristics. The coupling between spray characteristics and 
RDWs is near critical, leading to variant but transient modes during 
evolution, along with somewhat random mode characteristics (5 – 41 ms 
in Fig. 16a ). Specifically, this coupling effect undergoes positive feed -
back during the LPD in the later evolution stages and amplifies the 
instability, which increases the pulse intervals and finally results in 
deflagration (41 – 50 ms in Fig. 16a ). When the coupling reaches a steady 
state during initiation, stable modes gradually form ( Fig. 13b & c ). In 
contrast, the interaction becomes unstable and eventually leads to 
deflagration during Type III extinction.
5.3. Mode transition
Mode transition is an instability process in which critical equilibrium 
is disrupted by small random perturbations, partially driven by the dy -
namic changes in spray characteristics. Typically, it occurs at the 
boundaries of different stable modes according to the mode distribution 
patterns, as detailed in Section 6 . Unlike unstable modes that seldom 
exhibit any modal characteristics, the wave system is of stable mode 
before transition, and can stabilize back into another stable mode after 
transition. The following section analyzes two major types of mode 
transitions, all of which involve the frequently observed counter double- 
wave mode.
(1) Single-wave mode & Counter double-wave mode .
The experimentally observed mode transition between single-wave 
mode and counter double-wave mode is illustrated in Fig. 17a (case 
A1C2-0.50 – 0.81). In the counter double-wave mode, the weaker wave is 
easily affected by perturbations and gradually decays, leading to a 
transition into single-wave mode. In single-wave mode, small pertur -
bation initially develops into a weaker RDW of opposite direction, which 
then intensifies to a stronger RDW, subsequently causing the original 
wave to attenuate. Under the same reactant supply, the counter double- 
wave mode exhibits a lower wave velocity due to the losses incurred 
from collisions between RDWs. Neither mode can be sustained for an 
Fig. 14. (a) Evolution of Type I extinction in interpolated θ - t diagram. (b) Pressure comparison of Type I & II extinction (measured by PCB1).
Fig. 15. (a) Evolution of Type II extinction. Numerical θ - t diagram of (b) pressure and (c) reaction progress. Parameters are κ = 0.035, A
+
= 0.3, and A

= 0.8 
in simulation.
W. Qin et al.                                                                                                                                                                                                                                     Fuel 418 (2026) 138720 
12

<!-- PDF_PAGE: 13 -->

Fig. 16. (a) Evolution of Type III extinction. (b) Numerical θ - t diagram of pressure as κ gradually decreased. ( A
+
= 0.3, A

= 0.8).
Fig. 17. (a) Transitions between single-wave mode and counter double-wave mode. (b) Numerical θ - t diagram of the same transition under variable κ ( A
+
= 0.3, A

= 0.8).
W. Qin et al.                                                                                                                                                                                                                                     Fuel 418 (2026) 138720 
13

<!-- PDF_PAGE: 14 -->

extended period in these critical conditions, resulting in frequent ex -
changes between the two modes.
The oscillation between two modes is considered to be related to the 
dynamic spray characteristics. As depicted in Fig. 17b , the combustion 
mode switches from one to another as κ changes in the simulations. The 
velocities of the two waves converge as κ is decreased to 0.06, followed 
by the attenuation and decay of one RDW. When κ is gradually restored 
to 0.09, a weak disturbance gradually strengthens into a RDW in the 
opposite direction, leading to counter double-wave mode. This result 
indirectly confirms that changes in spray characteristics (i.e., different 
settings of κ at t = 50, 100 … ) can induce instability and influence the 
combustion mode. Particularly, since changes in spray characteristics 
primarily stem from the disturbances of RDWs under experimental 
conditions, it is easier to form oscillations under critical conditions such 
as mode transitions.
It is also noteworthy that the numerical mode distribution pattern of 
A

= 0.8 ( Fig. 22 ) indicates that κ = 0.08 and κ = 0.07 correspond to 
different modes. However, when κ is decreased from 0.08 to 0.07 (or 
vice versa) in this case, the combustion modes remain unchanged. This 
observation implies that the combustion mode may also be related to the 
evolution history of the system, and exhibits an “ inertia ” to maintain 
previous mode under small changes in parameters.
(2) Longitudinal pulse detonation & Counter double-wave mode .
Mode transition between counter double-wave mode and LPD is also 
observed. The measurement results are shown in Fig. 18 (case A2C1- 
0.50 – 0.91), where the time range of Fig. 18b (PSD of pressure data) is 
broader. The initial mode is counter double-wave mode, where the 
strength of the weaker wave decreases first, disrupting the stronger 
wave. Ultimately, both waves become unstable, followed by the 
destruction of the original wave system's structure. After reconstruction 
of the wave system, a stable LPD is established.
The static pressure inside the combustor pressure increases by 
approximately 10% after the transition, accompanied with a larger 
amplitude of the pressure oscillations. The PSD diagram in Fig. 18b
shows that the fundamental frequency of LPD is much lower than that of 
the counter double-wave mode. As evidence of stronger dissipation, the 
oscillation amplitudes of the lower-order harmonics are also larger than 
before. Due to the dynamic interaction between RDWs and spray char -
acteristics, the pulse intervals are not fixed until a stable LPD forms.
6. Combustion mode distribution pattern
This work constructs two-dimensional mode distribution patterns by 
summarizing experimental and numerical data ( Figs. 19 – 22 ). These 
show the mode distribution relative to ˙m
O , t 
and φ
t 
of different combi -
nations of various atomizers and combustors (i.e., Type A1C1, A1C2, 
A2C1, A2C2, and A3C1). The parameter ranges are incomplete due to 
the limitations of the experimental facilities. When ˙m
O , t 
and φ
t 
are too 
low, the kerosene injection pressure falls below the design pressure, 
making effective atomization impossible. Conversely, when ˙m
O , t 
and φ
t 
are too high, the kerosene injection pressure exceeds the pressure limits 
of the pipelines. Therefore, the feasible domain is approximately an 
inclined band, with the untested regions marked as shaded areas in the 
mode distribution patterns.
6.1. Influence of oxidizer flow rate and equivalence ratio
Different levels of ˙m
O , t 
and φ
t 
lead to varying modes, and all five 
types demonstrate a clear trend that the number of RDWs increases with 
an increase of ˙m
O , t 
and a decrease in φ
t
. The mode distribution of the 
Type A1C1 shown in Fig. 19 includes plentiful modal characteristics. 
The dotted purple lines represent the isopleths of total mass flow rate, 
Fig. 18. Mode transition from counter double-wave mode to LPD. (a) θ -t diagram. (b) Short-time Fourier transform result of PCB1.
Fig. 19. Mode distribution of Type A1C1 relative to ˙m
O , t 
and φ
t
. The bidirec -
tional arrow “↔” represents mode transitions.
W. Qin et al.                                                                                                                                                                                                                                     Fuel 418 (2026) 138720 
14

<!-- PDF_PAGE: 15 -->

calculated as ˙m = ( 1 + 0 . 128 φ
t
) ˙m
O , t
. The four lines from left to right 
correspond total flow rates of 0.55, 0.77, 1.07, and 1.35 kg/s, respec -
tively. The gray dashed lines indicate approximate modal boundaries.
Cases with low ˙m
O , t 
and high φ
t 
tend to form stable counter double- 
wave mode, found in the upper left area. Mode transitions from counter 
double-wave to counter four-wave mode are observed under moderate 
˙m
O , t 
and φ
t
, with counter four-wave mode dominating at small φ
t
. Ulti -
mately, at high ˙m
O , t 
and low φ
t
, the counter four-wave mode forms. In 
cases of low ˙m
O , t 
and φ
t
, the area corresponding to Type III extinction lies 
below that of the counter double-wave mode, which can be regarded as 
the instability process of a stable mode. Similar patterns are also 
observed for Type A1C2 and A2C2 ( Fig. 21 ), where higher ˙m
O , t 
and 
lower φ
t 
tend to induce more stable RDWs.
6.2. Influence of the atomization characteristics
Atomization characteristics significantly affect the mode distribution 
pattern. When comparing atomizers A1 and A2, both exhibit similar 
characteristic droplet sizes under steady back pressure. However, A2 
struggles to reach stable combustion modes. As shown in Fig. 20a , unlike 
Type A1C1 that forms extinction at low ˙m
O , t 
and φ
t
, Type A2C1 expe -
riences extinction over a wider range, including moderate ˙m
O , t 
and φ
t
. 
Additionally, mode transitions from LPD to counter double-wave mode 
occur at low ˙m
O , t 
and high φ
t
, while unstable modes appear at high ˙m
O , t 
and high φ
t
. Since the secondary shearing process is dominated by the 
oxidizer jet, atomizer A2, which has a larger oxidizer injection gap, re -
quires longer time to stabilize the spray field. Hence, the spray process is 
prone to coupling with the RDWs, and is more easily disturbed by them, 
resulting in extinction or unstable modes.
As for atomizer A3, it fails to sustain any stable mode. Due to its 
larger characteristic droplet sizes and poorer mixing effect, it only re -
sults in Type I and Type III extinction ( Fig. 20b ). With insufficient 
Fig. 20. Mode distribution of (a) Type A2C1 and (b) Type A3C1 relative to ˙m
O , t 
and φ
t
. The bidirectional arrow “↔” represents mode transitions.
Fig. 21. Mode distribution of (a) Type A1C2 and (b) Type A2C2 relative to ˙m
O , t 
and φ
t
. The bidirectional arrow “↔” represents mode transitions.
Fig. 22. Numerical combustion mode distribution relative to κ and A
+
( A

= 0.8).
W. Qin et al.                                                                                                                                                                                                                                     Fuel 418 (2026) 138720 
15

<!-- PDF_PAGE: 16 -->

oxidizer jet flow ( ˙m
O , t
≤ 0 . 7kg / s), the secondary shearing effect is 
inadequate, leading to an average characteristic droplet size of nearly 5 
μ m. Consequently, successful ignition is not achieved, often leading to 
Type I extinction. When ˙m
O , t 
exceeds 1.0 kg/s, the characteristic droplet 
size decreases to approximately 3.6 μ m, meeting the ignition conditions. 
However, atomizer A3 requires a relative long recovery time, similar to 
atomizer A2, which makes it difficult for the RDWs to propagate without 
enough reactant supply. Eventually, the RDWs decays and Type III 
extinction forms.
6.3. Influence of the channel width of the combustor
Increasing the channel width favors the formation of stable modes. 
Compared to combustor C1, the channel width of combustor C2 in -
creases by 5 mm (33%), which result in a decrease in flow density within 
the combustor and an increase in the height of the wave fronts. Conse -
quently, the radial structure of the spray field changes, impacting the 
dynamic process of the restart of the atomizer after the RDWs. Fig. 21
illustrates that combustor C2 prefers to form stable single-wave mode 
more readily than combustor C1.
Compared to the mode distribution pattern of combustor C1 
( Fig. 20 ) , the single-wave mode showcases a larger coverage in the mode 
distribution pattern of combustor C2. At low ˙m
O , t 
and high φ
t
, where 
Type A1C1 forms counter double-wave mode ( Fig. 19 ), Type A1C2 is 
able to induce single-wave mode. In regions where Type A2C1 displays 
instabilities or results in extinction ( Fig. 20 ) , Type A2C2 can generate a 
single-wave mode or experience mode transition from single-wave to 
counter double-wave mode under low φ
t
. While predominantly 
assuming the single-wave mode, the mode distribution pattern of 
combustor C2 follows the trend that higher ˙m
O , t 
and lower φ
t 
lead to 
more RDWs, as the characteristics droplets sizes will be smaller. Type 
A1C2 nearly skips the double-wave mode when transitioning from 
single-wave to counter four-wave mode, while Type A2C2 maintains at 
most two RDWs during the experiments. This demonstrates that 
combustor C2 is advantageous for the stable propagation of RDWs and 
influences the evolution of wave trains during the early stages of 
rotating detonation.
6.4. Underlying mechanism
Various parameters, including ˙m
O , t
, φ
t
, atomization quality, and 
channel width, all influence the combustion mode by impacting the 
pivot variable, specifically the spray characteristics. Based on the anal -
ysis above, it is both feasible and effective to simulate the mode distri -
bution pattern using numerical simulation. By adapting the mixing rate 
coefficient κ as the horizontal axis in the numerical mode distribution 
pattern, a clearer picture emerges. Fig. 22 shows the mode distribution 
pattern relative to A
+
and κ for a fixed A

, which corresponds to the 
experimental mode distribution patterns of various combinations of 
atomizers and combustors.
Larger ˙m
O , t 
and smaller φ
t 
enhance the spray characteristics, pro -
moting the formation of more RDWs. For a given A
+
, the combustion 
mode strengthens with increasing κ , transitioning gradually from LPD or 
extinction to single-wave mode, counter double-wave mode, and rea -
ches multi-wave modes ultimately. In fact, as φ
t 
decreases at a constant 
total mass flow rate, the relative proportion of oxidizer jet to fuel jet 
increases. This relatively greater oxidizer jet enhances the effect of 
secondary shearing, breaking large droplets into smaller ones, and 
resulting in smaller characteristic droplet sizes ( Fig. 10a , ex-situ mea -
surements). This improvement in atomization and mixing effect reduces 
incomplete detonation, and facilitates the formation of more dissipative 
mode and additional RDWs, as indicated by the arrow in Fig. 19 . The 
lower-right area of Fig. 22 corresponds to this arrow, showing a ten -
dency to form more RDWs as the mixing improves (i.e., decreasing φ
t 
or 
increasing κ ).
Poor atomization quality hinders the achievement of stable detona -
tion modes. Because of the disturbance of the RDWs to the injection, 
Type A2C1 exhibits undesirable spray characteristics and only realizes a 
low-level mixing effect compared with Type A1C1, which corresponds to 
a lesser κ . Due to larger characteristic droplet sizes and insufficient 
mixing process, the overall performance of atomizer A3 is the worst, 
represented by the smallest κ in numerical simulations. Neither Type 
A2C1 and A3C1 attains stable combustion modes. The left one-third area 
of Fig. 22 represents their mode distribution patterns, where improved 
spray characteristics is still beneficial for avoiding extinction under poor 
atomization. Furthermore, the evolution sequences of combustion mode 
differ slightly between experimental and numerical mode distribution 
pattern. This discrepancy indicates that the influence of spray charac -
teristics on combustion modes is nonlinear, necessitating further 
exploration of detailed mechanisms.
Wider channel widths contribute to the reduction of back pressure 
and stabilize the RDWs. Measurements from two cases with similar 
supply parameters (A1C1-0.98 – 0.64 and A1C2-0.98 – 0.68) demonstrate 
that increasing the channel width lowers the average static pressure 
(measured by Pc1 ~ Pc3) and velocity deficit by 27 kPa and 0.04 V
CJ
, 
respectively. The lower back pressure in combustor C2 enhances the 
recovery of the injection behind the waves, weakens the coupling be -
tween the RDWs and spray characteristics, and produces a more stable 
spray field. Additionally, a wider channel width may reduce fuel loss by 
making droplets less likely to adhere to the wall. As a result, combustor 
C2 does not exhibit Type III extinction at low ˙m
O , t 
and low φ
t
, unlike 
combustor C1. Instead, it forms Type II extinction under high φ
t 
due to 
excessive energy supply. This occurs because the improved mixing leads 
to stronger a counter double-wave after ignition, which in turn inhibits 
the restart of the atomizer behind the waves, resulting in the decay of 
RDWs due to inadequate reactant supply.
Thus, the arrows at the middle-right and the middle parts of Fig. 22
correspond to Type A1C2 and Type A2C2, respectively. This observation 
suggests that medium spray quality helps suppress the formations of 
excessive RDWs, stabilizes the rotating detonation, and prevents the 
system from transitioning into deflagration. Moreover, the irregular 
modal boundaries observed in both the experimental and numerical 
mode distribution patterns indicate that rotating detonation is highly 
complex and nonlinear, where even subtle changes in parameters may 
result in drastically different combustion modes.
7. Conclusion
This study conducted experimental study of kerosene/air two-phase 
rotating detonation. The steady characteristics, dynamic processes and 
mode distribution pattern of two-phase RDE are analyzed in detail using 
atomizers A1 ~ A3. The main research conclusions are as follows: 
(1) In experiments, a maximum of four RDWs can maintain stable 
propagation simultaneously. The velocity deficits for different 
stable modes range from 5% to 45% V
CJ
, and enlarge as the 
number of RDWs increase. These velocity deficits primarily result 
from non-uniform spray, the attachment of droplets to the wall, 
and the deflagration of some droplets outside the RDW. Specif -
ically, velocity deficits of single-wave mode are ~0.15 V
CJ
, 
exhibiting a trend of first decreasing and then increasing with 
rising φ
t
. This behavior is attributed to the formation of local fuel- 
rich areas and the incomplete combustion of larger droplets.
(2) Dynamic processes, including initiation, extinction and mode 
transition, are related with the coupling between RDWs and spray 
characteristics. During initiation process, stable modes can form 
if the pulse intervals shorten and finally stabilize. Extinction 
process can be divided into three categories: Type I to Type III. 
Type I is an ignition failure that is observed with larger charac -
teristic droplet sizes ( > 5 μ m), and only be achieved by using 
atomizer A3. Type II occurs at larger φ
t
, as the overly strong RDW 
W. Qin et al.                                                                                                                                                                                                                                     Fuel 418 (2026) 138720 
16

<!-- PDF_PAGE: 17 -->

hinders the reactants refilling after the wave. In Type III, this 
coupling approaches the critical state, displays a pulse phenom -
enon similar to LPD, and reach extinction gradually. According to 
numerical comparison, mode transition can be induced by dy -
namic changes in spray characteristics, where small disturbances 
eventually evolve into new modes.
(3) Steady-state measurements show that atomizer A1 & A2 have 
similar characteristic droplet sizes (~3 μ m), while A3 has the 
worst spray performance (~5 μ m). Consequently, Type A3C1 
only leads to Type I & III extinction. The observed mode distri -
butions of Type A1C1 & A1C2 show that the number of RDWs 
increases as the φ
t 
decreases and ˙m
O , t 
increases. The increasing 
direction of wavenumbers coincides with the decreasing direc -
tion of characteristic droplet sizes of atomizer A1, and the 
wavenumber also increases with the rise of κ in reduced order 
numerical model. These indicate that improving atomization 
quality helps to maintain more RDWs simultaneously. When the 
combustor C2 is used instead of C1, the channel width increases 
by 33%, while the back pressure and velocity deficit decrease by 
~ 15% and ~ 0.04 V
CJ
, respectively. This facilitates preventing 
extinction, and more frequently leads to a single-wave mode.
CRediT authorship contribution statement
Wenkai Qin: Writing – review & editing, Visualization, Methodol -
ogy, Investigation, Conceptualization. Haocheng Wen: Writing – re -
view & editing, Supervision, Project administration, Funding 
acquisition, Conceptualization. Bing Wang: Writing – review & editing, 
Investigation.
Declaration of competing interest
The authors declare that they have no known competing financial 
interests or personal relationships that could have appeared to influence 
the work reported in this paper.
Acknowledgments
The authors would like thank the support from National Natural 
Science Foundation of China (No. 52306152 and No. 12441201) and 
Beijing Natural Science Foundation (No. L241040).
Appendix A 
A Reduced order numerical model for RDW
A1 Physical model
Fig. A1. Schematics of the numerical model.
As shown in Fig. A.1 , the three-dimensional combustor is modeled by a reduced order numerical model for RDW. The flow parameters are averaged 
in radial direction to reduce dimension, and the circumference of the combustor is expanded to a rectangular area, thereby deriving a two-dimensional 
mean field. The injection process is simulated as a function of combustor pressure, and the expansion process is assumed to be isentropic. By ignoring 
the axial difference in the thin layer, a one-dimensional computational domain is obtained, as demonstrated in Eqs. (1) .
In Eqs. (1) , u is the circumferential velocity, E is the total energy. ˙m
0 
and ˙m
1 
are the mass flow rate at the inlet and outlet, respectively. e
0 
and e
1 
are 
the specific internal energies at the inlet and outlet, respectively. ω is the chemical reaction rate, and q is the calorific value of reactants. Then the inlet 
mass flow rate is ˙m
0
= α A
+
H ( p )
̅̅̅̅̅̅̅̅̅ ̅
p
0
ρ
0
√
, and the outlet mass flow rate is ˙m
1
= α A

̅̅̅̅̅̅̅̅̅ ̅
p
0
ρ
0
√
, where α is a function of γ : 
α =
̅̅ ̅
γ
√
(
2
γ + 1
)
γ + 1
2 ( γ  1 )
(A.1) 
H ( ⋅ ) is the injection model function, which is defined as: 
H ( p ) = H
(
1 
p
p
0
)(
1  H
(
p
p
0
 n
)
p / p
0
 n
1  n
)
, n =
(
γ + 1
2
)

γ
γ  1
(A.2) 
where H ( ⋅ ) is the Heaviside step function, and n is a function of the specific heat ratio γ . This equation indicates that fresh mixture is injected only when 
the back pressure is less than the injection pressure.
W. Qin et al.                                                                                                                                                                                                                                     Fuel 418 (2026) 138720 
17

<!-- PDF_PAGE: 18 -->

In this computational analysis, the detailed processes of kerosene atomization and evaporation are not considered. Instead, the effects of the spray 
process are collectively represented by the mixing rate coefficient κ . A higher κ indicates better mixing and atomization. In addition, a single step 
model is adopted to calculate the chemical reactions. Moreover, one can obtain the numerical θ -t diagram by arranging the one-dimensional numerical 
results in time order, similar to the θ -t diagram and the interpolated θ -t diagram.
A2 Non-dimensionalization and numerical solver
In this simulation, the length of the one-dimensional computational domain is chosen to approximate the combustor perimeter (0.48 m), which 
corresponds to a dimensionless length of L = 24 and a grid size of Δ x = 0.024. The characteristic parameters are p
0 
= 1 MPa, T
0 
= 300 K, z
0 
= 0.02 m, 
and t
0 
= 72.3 μ s, which serves to nondimensionalize the pressure, temperature, position, and time, respectively. After non-dimensionalization, a 
numerical analysis program is developed using the open-source partial differential equation solver PyClaw [ 55 ]. In this program, the numerical flux is 
computed utilizing the Harten-Lax-van Leer (HLL) Riemann solver and a total variation diminishing (TVD) scheme, while time advancement is 
performed with a second-order Runge-Kutta method. The verification and validation of this numerical model has been already examined in literature 
[ 56 ].
Appendix B. Other characteristic droplets size measurement results
Fig. B.1 Show the detailed characteristic droplet sizes of atomizers A1 and A3. Both atomizers A1 and A2 employ the same configuration, with only 
a slight difference in dimensions. Therefore, the probability density function (PDF) and D10 distribution of atomizer A1 can represent both atomizers 
A1 and A2, and are shown as below.
Fig. B1. Typical droplet size PDF of (a) atomizers A1,  = 0.71 kg/s, φ
t 
= 0.88 and (b) atomizer A3,  = 0.96 kg/s, φ
t 
= 0.63. Contour map of D
10 
relative to equivalent 
and φ
t 
of atomizer (c) A1 and (d) A3.
W. Qin et al.                                                                                                                                                                                                                                     Fuel 418 (2026) 138720 
18

<!-- PDF_PAGE: 19 -->

Appendix C. Supplementary data
Supplementary data to this article can be found online at https://doi.org/10.1016/j.fuel.2026.138720 .
Data availability
Data will be made available on request.
References
[1] Voitsekhovskii BV. Stationary spin detonation. Sov J Appl Mech Tech Phys 1960;3: 
157 – 64 .
[2] Hayashi AK. Numerical study on pressure gain of rotating detonation system. AIAA 
SCITECH 2023 forum, National Harbor, MD & Online. American Institute of 
Aeronautics and Astronautics; 2023. 10.2514/6.2023-2565 .
[3] Wen H, Xie Q, Wang B. Propagation behaviors of rotating detonation in an obround 
combustor. Combust Flame 2019;210:389 – 98. https://doi.org/10.1016/j. 
combustflame.2019.09.008 .
[4] Wen H, Fan W, Xu S, Wang B. Numerical study on droplet evaporation and 
propagation stability in normal-temperature two-phase rotating detonation system. 
Aerosp Sci Technol 2023;138:108324. https://doi.org/10.1016/j. 
ast.2023.108324 .
[5] Xu G, Wu Y, Xiao Q, Ding C, Xia Y, Li Q, et al. Characterization of wave modes in a 
kerosene-fueled rotating detonation combustor with varied injection area ratios. 
Appl Therm Eng 2022;212:118607. https://doi.org/10.1016/j. 
applthermaleng.2022.118607 .
[6] Xu G, Wu Y, Kang C, Lei T, Qiu Y, Ding C, et al. Propagation behaviors of kerosene- 
fueled rotating detonation wave with varied atomizer locations. Aerosp Sci Technol 
2023;142:108676. https://doi.org/10.1016/j.ast.2023.108676 .
[7] Xu S, Song F, Wu Y, Zhou J, Cheng P, Yang X, et al. Experimental investigation on 
combustion efficiency of a partially premixed kerosene-air rotating detonation 
combustor. Fuel 2022;329:125418. https://doi.org/10.1016/j.fuel.2022.125418 .
[8] Jourdaine N, Tsuboi N, Hayashi AK. Investigation of liquid n-heptane/air spray 
detonation with an Eulerian-Eulerian model. Combust Flame 2022;244:112278. 
https://doi.org/10.1016/j.combustflame.2022.112278 .
[9] Yao S, Guo C, Zhang W. Effects of droplet evaporation on the flow field of 
hydrogen-enhanced rotating detonation engines with liquid kerosene. Int J Hydrog 
Energy 2023;48:33335 – 45. https://doi.org/10.1016/j.ijhydene.2023.04.314 .
[10] Yan C, Zhao J, Tong Y, Wang B, Shu C, Nie W, et al. Formation and evolution of the 
numerical air-breathing rotating detonation fueled by C
12 
H
23
. Combust Sci 
Technol 2025;197:276 – 309. https://doi.org/10.1080/00102202.2023.2226816 .
[11] Fan W, Shi Y, Wen H, Hu H, Chen H, Wang B. Analysis of waves dynamics in a 
rotating detonation combustor fueled by kerosene. Phys Fluids 2024;36:106135. 
https://doi.org/10.1063/5.0231516 .
[12] Yao S, Tang X, Zhang W. Structure of a heterogeneous two-phase rotating 
detonation wave with ethanol – hydrogen – air mixture. Phys Fluids 2023;35: 
031712. https://doi.org/10.1063/5.0144920 .
[13] Liu H, Song F, Jin D, Xu S, Yang X. Experimental investigation on spray and 
detonation initiation characteristics of premixed/non-premixed RDE. Fuel 2023; 
331:125949. https://doi.org/10.1016/j.fuel.2022.125949 .
[14] Prakash S, Fi ´evet R, Raman V, Burr J, Yu KH. Analysis of the detonation wave 
structure in a linearized rotating detonation engine. AIAA J 2020;58:5063 – 77. 
https://doi.org/10.2514/1.J058156 .
[15] Li J, Lei Y, Yao S, Yu J, Li J, Zhang W. Investigation of multi-stage evaporation and 
wave multiplicity of two-phase rotating detonation waves fueled by ethanol. Acta 
Astronaut 2023;213:418 – 30. https://doi.org/10.1016/j.actaastro.2023.08.037 .
[16] Huang X, Lin Z. Analysis of coupled-waves structure and propagation 
characteristics in hydrogen-assisted kerosene-air two-phase rotating detonation 
wave. Int J Hydrog Energy 2022;47:4868 – 84. https://doi.org/10.1016/j. 
ijhydene.2021.11.105 .
[17] Salvadori M, Panchal A, Ranjan D, Menon S. Numerical study of detonation 
propagation in H2-air with kerosene droplets. AIAA SCITECH 2022 forum, San 
Diego, CA & Virtual. American Institute of Aeronautics and Astronautics; 2022. 
10.2514/6.2022-0394 .
[18] Ragland K, Dabora E, Nicholls J. A study of heterogeneous detonations. 3rd 4th 
Aerosp. Sci. Meet. New York, U.S.A.: American Institute of Aeronautics and 
Astronautics; 1966. 10.2514/6.1966-109 .
[19] Dabora EK, Ragland KW, Nicholls JA. Drop-size effects in spray detonations. Symp 
Int Combust 1969;12:19 – 26. https://doi.org/10.1016/S0082-0784(69)80388-7 .
[20] Agee S, Young C, Duke-Walker V, Paudel M, McFarland JA. Impact of liquid fuel 
droplet size on detonation dynamics. AIAA SCITECH 2025 Forum. Orlando, FL: 
American Institute of Aeronautics and Astronautics; 2025. Doi:10.2514/6.2025- 
0175 .
[21] Papavassiliou J, Makris A, Knystautas R, Lee JHS, Westbrook CK, Pitz WJ. 
Measurements of cellular structure in spray detonation. Dyn Asp Explos Phenom, 
Am Inst Aeronaut Astronaut 1993:148 – 69. https://doi.org/10.2514/ 
5.9781600866272.0148.0169 .
[22] Benmahammed MA, Veyssiere B, Khasainov BA, Mar M. Effect of gaseous oxidizer 
composition on the detonability of isooctane – air sprays. Combust Flame 2016;165: 
198 – 207. https://doi.org/10.1016/j.combustflame.2015.12.004 .
[23] Hayashi AK, Tsuboi N, Dzieminska E. Numerical study on JP-10/air detonation and 
rotating detonation engine. AIAA J 2020;58:5078 – 94. https://doi.org/10.2514/1. 
J058167 .
[24] Zhao M, Zhang H. Rotating detonative combustion in partially pre-vaporized dilute 
n-heptane sprays: Droplet size and equivalence ratio effects. Fuel 2021;304: 
121481. https://doi.org/10.1016/j.fuel.2021.121481 .
[25] Jin S, Zhang H, Zhao N, Zheng H. Simulations of rotating detonation combustion 
with in-situ evaporating bi-disperse n-heptane sprays. Fuel 2022;314:123087. 
https://doi.org/10.1016/j.fuel.2021.123087 .
[26] Cao W, Liu Q, Wang F, Weng C. Effects of the droplet size and engine size on two- 
phase kerosene/air rotating detonation engines in flight operation conditions. Acta 
Astronaut 2024;223:108 – 18. https://doi.org/10.1016/j.actaastro.2024.07.002 .
[27] Meng Q, Zhao M, Zheng H, Zhang H. Eulerian-Lagrangian modelling of rotating 
detonative combustion in partially pre-vaporized n-heptane sprays with hydrogen 
addition. Fuel 2021;290:119808. https://doi.org/10.1016/j.fuel.2020.119808 .
[28] Wang J, Lin W, Huang W, Shi Q, Zhao J. Numerical study on atomization and 
evaporation characteristics of preheated kerosene jet in a rotating detonation 
scramjet combustor. Appl Therm Eng 2022;203:117920. https://doi.org/10.1016/ 
j.applthermaleng.2021.117920 .
[29] Jin S, Xu C, Zheng H, Zhang H. Detailed chemistry modeling of rotating 
detonations with dilute n-heptane sprays and preheated air. Proc Combust Inst 
2023;39:4761 – 9. https://doi.org/10.1016/j.proci.2022.08.075 .
[30] Li J, Yao S, Yu J, Li J, Lei Y, Zhang W. Shock interactions and re-initiation 
mechanism of liquid ethanol-fueled rotating detonation wave. Phys Fluids 2024; 
36:096106. https://doi.org/10.1063/5.0217517 .
[31] Han X, Huang Y, Zheng Q, Xiao Q, Xu H, Wang F, et al. Study of the characteristics 
and combustion efficiency of liquid kerosene/oxygen-enriched air rotating 
detonation wave with different modes. Fuel 2024;355:129424. https://doi.org/ 
10.1016/j.fuel.2023.129424 .
[32] Meng H, Zheng Q, Weng C, Wu Y, Feng W, Xu G, et al. Propagation mode analysis 
of rotating detonation waves fueled by liquid kerosene. Acta Astronaut 2021;187: 
248 – 58. https://doi.org/10.1016/j.actaastro.2021.06.043 .
[33] Meng H, Li B, Xu G, Wang Z, Weng C. Characteristics of rotating detonation wave 
fueled by liquid kerosene with increasing equivalence ratios. FirePhysChem 2023; 
3:300 – 10. https://doi.org/10.1016/j.fpc.2023.02.003 .
[34] Wang D, Zhou J, Lin Z. Experimental investigation on operating characteristics of 
two-phase continuous rotating detonation combustor fueled by kerosene. J Propuls 
Technol 2017;38:471 – 80. https://doi.org/10.13675/j.cnki.tjjs.2017.02.028 .
[35] Ding C, Wu Y, Xu G, Xia Y, Li Q, Weng C. Effects of the oxygen mass fraction on the 
wave propagation modes in a kerosene-fueled rotating detonation combustor. Acta 
Astronaut 2022;195:204 – 14. https://doi.org/10.1016/j.actaastro.2022.03.003 .
[36] Hasti VR, Ranjan R. Numerical investigation of wave dynamics during mode 
transition in a hydrogen-fueled rotating detonation engine combustor. Vol. 9 Heat 
Transf. Therm. Eng. Portland, Oregon, USA: American Society of Mechanical 
Engineers; 2024. Doi:10.1115/IMECE2024-145858 .
[37] Hasti VR, Pratt J, Ranjan R. Dynamically dominant flow features during wave 
mode transition in a rotating detonation engine combustor. AIAA SCITECH 2025 
Forum. Orlando, FL: American Institute of Aeronautics and Astronautics; 2025. 
Doi:10.2514/6.2025-0402 .
[38] Feleo A, Chacon F, Gamba M. Effects of heat release distribution on detonation 
properties in a H2/air rotating detonation combustor from OH* chemiluminesence. 
AIAA Propuls. Energy 2019 Forum. Indianapolis, IN: American Institute of 
Aeronautics and Astronautics; 2019. Doi:10.2514/6.2019-4045 .
[39] Zhou W, Cao Z, Dou S, Yang Q, Xu L. 120 kHz mid-infrared TDLAS sensor for H2O 
concentration and temperature measurement in rotating detonation engine exhaust 
flows. Measurement 2024;234:114787. https://doi.org/10.1016/j. 
measurement.2024.114787 .
[40] Shi Y, Zhang Y, Jin X, Wen H, Wang B. Parameter influence and calculation model 
of wall heat flux in kerosene two phase rotating detonation combustor. Combust 
Flame 2025;273:113924. https://doi.org/10.1016/j.combustflame.2024.113924 .
[41] Athmanathan V. Investigation of rotating detonation combustion dynamics using 
advanced in-situ optical diagnostics. ProQuest Dissertations & Theses. Purdue 
University; 2021 .
[42] Peng H-Y, Liu W-D, Liu S-J, Zhang H-L, Huang S-Y. The competitive relationship 
between detonation and deflagration in the inner cylinder-variable continuous 
rotating detonation combustor. Aerosp Sci Technol 2020;107:106263. https://doi. 
org/10.1016/j.ast.2020.106263 .
[43] Fan W, Peng H, Liu S, Sun M, Yuan X, Zhang H, et al. Initiation process of non- 
premixed continuous rotating detonation wave through Schlieren visualization. 
Combust Flame 2024;265:113437. https://doi.org/10.1016/j. 
combustflame.2024.113437 .
[44] Jia B, Zhang Y, Pan H, Hong Y. Experimental Study on Initiation Process of Liquid 
Hydrocarbon Rotary Detonation Engine. J Propuls Technol 2021;42:906 – 14. 
https://doi.org/10.13675/j.cnki.tjjs.200752 .
[45] Han X. Experimental study on propagation, quenching, and re-initiation 
characteristics of rotating detonation wave with liquid kerosene – oxygen-enriched 
air. Exp Therm Fluid Sci 2023 .
W. Qin et al.                                                                                                                                                                                                                                     Fuel 418 (2026) 138720 
19

<!-- PDF_PAGE: 20 -->

[46] Raman V, Prakash S, Gamba M. Nonidealities in rotating detonation engines. Annu 
Rev Fluid Mech 2023;55:639 – 74. https://doi.org/10.1146/annurev-fluid-120720- 
032612 .
[47] Prakash S, Raman V, Lietz CF, Hargus WA, Schumaker SA. Numerical simulation of 
a methane-oxygen rotating detonation rocket engine. Proc Combust Inst 2021;38: 
3777 – 86. https://doi.org/10.1016/j.proci.2020.06.288 .
[48] Yang X, Song F, Wu Y, Zhou J. Experimental study of mode control in rotating 
detonation combustor using Tesla valve mode control configuration fueled by 
kerosene. Exp Therm Fluid Sci 2024;151:111075. https://doi.org/10.1016/j. 
expthermflusci.2023.111075 .
[49] Bedick C, Ferguson D, Sisler A, Strakey P, Nix A, Billips D. Characterization of 
Novel Rotating Detonation Engine Inlet Concepts in a Lab-Scale Experimental 
Testing Platform, 2017.
[50] Yang X, Song F, Wu Y, Guo S, Xu S, Zhou J, et al. Suppression of pressure feedback 
of the rotating detonation combustor by a Tesla inlet configuration. Appl Therm 
Eng 2022;216:119123. https://doi.org/10.1016/j.applthermaleng.2022.119123 .
[51] Jin L. Investigations on the supercritical injection, evaporation, and detonation 
characteristics of the RP-3 aviation kerosene. Northwestern Polytechnical 
University; 2016. PhD Thesis .
[52] Mie G. Beitr ¨age zur Optik trüber Medien, speziell kolloidaler Metall ¨osungen. Ann 
Phys 1908;330:377 – 445. https://doi.org/10.1002/andp.19083300302 .
[53] Koch J, Kutz JN. Modeling thermodynamic trends of rotating detonation engines. 
Phys Fluids 2020;32:126102. https://doi.org/10.1063/5.0023972 .
[54] Mcbride BJ, Gordon S. Computer program for calculation of complex chemical 
equilibrium compositions and applications. Cleveland, OH: NASA Lewis Research 
Center; 1994 .
[55] Ketcheson DI, Mandli KT, Ahmadia A, Alghamdi A, Quezada M, Parsani M, et al. 
PyClaw: accessible, extensible, scalable tools for wave propagation problems. SIAM 
J Sci Comput 2012;34:C210 – 31. https://doi.org/10.1137/110856976 .
[56] Wang X, Wen H, Hu T, Wang B. Flow-field reconstruction in rotating detonation 
combustor based on physics-informed neural network. Phys Fluids 2023;35: 
076109. https://doi.org/10.1063/5.0154979 .
W. Qin et al.                                                                                                                                                                                                                                     Fuel 418 (2026) 138720 
20
