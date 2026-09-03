<!-- PDF_PAGE: 1 -->

Experimental study on the development characteristics of the extremely 
under-expanded hydrogen jet structure for high pressure direct injection 
hydrogen engines
Ziteng Zhang
a
, Yafei Yuan
b
, Xiyu Yang
a , *
, Fangliang Yang
a
, Cheng Shi
a
, Xiaoyan Wang
c
a
School of Vehicle and Energy, Yanshan University, Qinhuangdao, 066004, China
b
Wuxi YaChai Technology Co.,Ltd, Wuxi, 534709, China
c
Weichai Power Co., Ltd., Weifang, 261000, China
ARTICLE INFO
Keywords:
Hydrogen internal combustion engine
Jet characteristics
Injection characteristics
Visualization
ABSTRACT
This paper investigates the injection process of extremely under-expanded high-pressure hydrogen in an internal 
combustion engine environment, focusing on transient flow characteristics and jet morphology to systematically 
reveal spatiotemporal evolution mechanisms under ultra-high pressure ratios. First, tests on a direct-acting 
injector reveal that, even under choked conditions, injection pressure and energizing time remain the domi -
nant parameters governing the injection rate. Results show that elevating injection pressure increases mass flow 
rate while significantly accelerating needle valve closure via enhanced internal pressure differentials, thereby 
shortening the injection duration by up to 11.6%. Second, high-speed schlieren imaging demonstrates that while 
higher injection pressure enhances spatial expansion, ambient pressure exerts a profound suppressive effect, 
particularly influencing initial jet tip velocity and cone angle. Because the hydrogen undergoes intense Prandtl- 
Meyer expansion immediately upon exiting the nozzle, a complex shock wave system forms, causing the near- 
field cone angle to consistently exceed its far-field cone angle. Finally, this study elucidates three distinct 
stages of massive Mach disk formation: the emergence of Prandtl-Meyer expansion fans, their intersection within 
the barrel shock, and their subsequent extension beyond the barrel shock. The pressure ratio is identified as the 
decisive parameter dictating the shock wave topology transition from a series of shock cells featuring Mach 
reflection to a single, massive Mach disk, clarifying the dynamic pathway of pressure energy release under 
extreme conditions.
1. Introduction
Against the backdrop of worldwide efforts to mitigate global 
warming, accelerating the low-carbon transformation of the energy 
system has become an inevitable choice for the transportation sector. 
Hydrogen offers the advantages of high calorific value, high burning 
velocity, and zero carbon emissions [ 1 – 3 ], and is regarded as one of the 
most important energy carriers in the 21st century [ 4 , 5 ]. Hydrogen fuel 
cells have strict requirements for hydrogen purity, while suffering from 
incomplete manufacturing systems and insufficient high-power perfor -
mance. These drawbacks have made hydrogen internal combustion en -
gines the technical solution for the stable implementation of 
hydrogen-powered systems at present [ 6 , 7 ].
Hydrogen has an extremely wide flammability range. Under the 
traditional port fuel injection mode, not only is there the problem of low 
volumetric efficiency, but also abnormal combustion phenomena such 
as backfire, pre-ignition and engine knock are very likely to occur. 
Therefore, the improvement in the performance of the internal com -
bustion engine is limited in this mode. For this reason, direct injection 
into the cylinder has become the main mode of fuel injection systems for 
hydrogen internal combustion engines at present [ 8 ].
According to the difference in injection pressure, direct injection 
systems can be divided into medium-pressure and high-pressure injec -
tion types [ 9 ]. Medium-pressure direct injection essentially operates in a 
premixed combustion mode, which still poses significant risks of 
pre-ignition and engine knock. In contrast, high-pressure direct injection 
typically injects hydrogen late in the compression stroke. When coupled 
with pilot fuel ignition, it enables hydrogen diffusion combustion, 
* Corresponding author.
E-mail address: yangxiyu@ysu.edu.cn (X. Yang). 
Contents lists available at ScienceDirect
Energy
journal homepag e: www.el sevier.com/loc ate/energy
https://doi.org/10.1016/j.energy.2026.141499
Received 25 March 2026; Received in revised form 6 May 2026; Accepted 27 May 2026  
Energy 359 (2026) 141499 
Available online 28 May 2026 
0360-5442/© 2026 Published by Elsevier Ltd.

<!-- PDF_PAGE: 2 -->

thereby enhancing combustion controllability and effectively mitigating 
knock [ 10 ]. Furthermore, unlike traditional fuels, hydrogen exhibits an 
extremely low critical pressure ratio and an extremely high speed of 
sound. These unique thermophysical properties profoundly influence 
the jet evolution. Under the same injection pressure ratio, the low 
density characteristic of hydrogen leads to a more rapid momentum 
decay, and it is highly susceptible to interference from the ambient 
aerodynamic drag. Moreover, its extremely high speed of sound means 
that when the nozzle is choked (Ma = 1), there is an extremely high 
actual initial jet velocity, thereby triggering more intense near-field 
shock wave phenomena. Under the high-pressure direct injection con -
dition of the internal combustion engine, the nozzle exit reaches a 
“ choked ” state, and the jet is injected at the local speed of sound. Ac -
cording to the principles of gas dynamics, when the pressure ratio ex -
ceeds the critical pressure ratio (for hydrogen, R* = 1.894), an 
under-expanded jet is formed; As the pressure ratio increases further, 
surpassing the threshold for Mach disk formation, the jet transitions into 
a highly or extremely under-expanded state. This particular state forces 
the gas to release excess pressure energy through a series of intense 
expansion and compression waves upon exiting the nozzle, generating 
highly complex macroscopic structures and mixing characteristics. 
Therefore, mastering the spatiotemporal evolution mechanisms and 
transient flow characteristics of high-pressure hydrogen jet is not only a 
prerequisite for achieving efficient and clean combustion [ 11 , 12 ], but 
also the key to optimizing the performance of high-pressure direct in -
jection hydrogen internal combustion engines.
In recent years, extensive research has been conducted on the fuel 
injection processes of hydrogen internal combustion engines. Abdul 
Rahman et al. [ 13 ] investigated the effect of ambient pressure (0.15 – 0.5 
MPa) on the local concentration distribution of transient hydrogen jet in 
a constant-volume vessel using spark-induced breakdown spectroscopy 
(SIBS). They found that as the ambient nitrogen pressure increased, the 
emission spectral line intensities of both hydrogen and nitrogen atoms 
were enhanced. However, high-density nitrogen simultaneously signif -
icantly alters the structure of the hydrogen jet, shortening its penetration 
and reducing its mixing rate. Deng et al. [ 14 ]utilized the schlieren 
method to investigate the non-reactive jet characteristics of hydrogen 
under an argon atmosphere at high pressure. They revealed that the 
ambient gas entrainment of the jet was significantly enhanced with 
increasing injection and ambient pressures. Based on these mixing 
characteristics, they concluded that the hydrogen direct injection 
strategy is highly conducive to achieving high engine power output and 
flexible operational control. Yip et al. [ 15 ] analyzed the influence of 
injection pressures ranging from 0.84 MPa to 1.4 MPa on the develop -
ment, ignition, and flame structure of hydrogen jet using schlieren im -
aging. Their results demonstrated that the auto-ignition delay of 
hydrogen jet is highly sensitive to ambient temperature but relatively 
insensitive to changes in injection pressure. Lee et al. [ 16 ] focused on the 
macroscopic evolution of a 10 MPa high-pressure hydrogen hollow-cone 
spray under varying ambient pressures. The results showed that as the 
ambient pressure increased, ambient aerodynamic drag and momentum 
exchange were enhanced, leading to a significant decrease in the axial 
penetration and projected area of the jet. Coratella et al. [ 17 , 18 ] used 
high-speed schlieren imaging to systematically investigate the effects of 
different actuation current profiles on needle valve dynamics and the 
resulting hydrogen spray of a medium-pressure outward-opening 
injector through high-speed schlieren imaging. They found that rare -
faction waves generated by the rapid opening of the needle valve could 
enhance the momentum of the hydrogen jet, and higher driving currents 
accelerated needle movement, thereby increasing the jet penetration 
velocity.
High-pressure hydrogen jet exhibit the typical characteristics of 
extremely under-expanded jet, wherein the gas pressure at the nozzle 
exit is substantially higher than the ambient pressure, causing the jet to 
undergo intense expansion upon exiting. his forces the gas to release 
excess pressure energy through a series of shock waves in the near-field 
region. Duronio et al. [ 19 ] investigated the influence of ambient pres -
sure on the macroscopic morphology of under-expanded jet, revealing a 
nonlinear correlation between the jet cone angle and the pressure ratio. 
At high pressure ratios, enhanced Prandtl-Meyer expansion fans cause 
the jet to exhibit intense radial expansion immediately at the nozzle exit. 
As the pressure ratio decreases, the jet boundary contracts significantly. 
Their work provided empirical correlations for jet penetration and cone 
angle under varying ambient pressures, laying an experimental foun -
dation for understanding fuel distribution across different operating 
conditions. Hamzehloo et al. [ 20 ] conducted a detailed analysis of the 
complex shock wave structures within under-expanded hydrogen jet 
using schlieren imaging combined with numerical simulations. Their 
study focused on the formation and evolution mechanisms of Mach disks 
and barrel shocks, identifying the nozzle pressure ratio as the dominant 
parameter determining the position and diameter of the Mach disk. Zhao 
et al. [ 21 ] investigated the turbulent dispersion and mixing mechanisms 
in extremely under-expanded jet. They demonstrated that although the 
strong Prandtl-Meyer expansion induced by high pressure ratios signif -
icantly broadens the near-field coverage of the jet, the resulting strong 
shock wave structures inherently inhibit radial turbulent exchange to 
some extent. Franquet et al. [ 22 ] provided a detailed description of 
under-expanded jet, dividing them into the near-field zone, transition 
zone, and far-field zone. They focused on analyzing the position and 
diameter of the Mach disk within the near-field zone, alongside the 
spatial evolution mechanisms of the jet.
Although extensive research has been conducted on hydrogen jet and 
under-expanded jet in recent years, studies focusing specifically on high- 
pressure hydrogen direct injection systems remain insufficient. Existing 
research has primarily focused on injection pressures below 15 MPa. 
Consequently, there is a notable lack of experimental data and mecha -
nistic understanding under the extreme high-pressure and high- 
pressure-ratio conditions demanded by future high-pressure direct-in -
jection (HPDI) hydrogen engines. Most of the detailed studies on the 
topological structure of extremely under-expanded jet shock waves are 
based on the theory of steady-state continuous jet, and they fail to reflect 
the dynamic influence of the transient pressure build-up and flow 
interruption processes with millisecond energizing time in the actual 
operating conditions of internal combustion engines on the evolution of 
the shock waves. Therefore, this study systematically measures and 
analyzes the transient flow characteristics of high-pressure hydrogen. 
Furthermore, using high-precision schlieren imaging, it further reveals 
the macroscopic dynamic evolution of highly under-expanded hydrogen 
jet and the fine topology of the induced shock waves, aiming to elucidate 
the spatiotemporal evolution mechanisms during the high-pressure 
hydrogen direct injection process.
2. Experimental setup
2.1. Experimental platform
The hydrogen jet was primarily visualized through the schlieren 
method. An in-line light path schlieren system manufactured by Luftvis 
Science (Model Luftvis-150) was used in the experiment. The system has 
a pair of high precision schlieren lens with 150 mm diamter and 750 mm 
focal length. The illumination was provided by a 40W white light LED 
illuminator. A knife-edge was positioned horizontally at the focal point 
with a cutoff ratio of 65%.
The high-speed camera operated at a resolution of 896 × 376 pixels, 
a frame rate of 40,000 frames per second (fps), and a shutter speed of 20 
μ s. To achieve precise synchronization between injector actuation and 
image acquisition, the control system output a 5V TTL synchronization 
signal to the external trigger port of the high-speed camera simulta -
neously with the triggering of the gas injector. In the fuel supply system, 
a gas booster pump was utilized to establish the required hydrogen in -
jection pressure. An air compressor provided the driving pressure for the 
booster pump, and this driving gas pressure was precisely regulated 
Z. Zhang et al.                                                                                                                                                                                                                                   Energy 359 (2026) 141499 
2

<!-- PDF_PAGE: 3 -->

using an SMC pneumatic proportional valve. The ambient gas supply 
system utilized high-pressure nitrogen cylinders, with the required 
ambient pressure established via pressure regulators. A master control 
computer was primarily responsible for timing synchronization and 
injector energizing time calibration, communicating with the synchro -
nization controller (local microcontroller) via the RS485 protocol. Upon 
decoding commands from the master computer, the synchronization 
controller sent a trigger signal to the high-speed camera to initiate image 
acquisition. Simultaneously, it converted the energizing time informa -
tion into a TTL signal of the corresponding energizing time and trans -
mitted it to the injector driving unit. The injector driving unit then 
generated the required actuation current based on this energizing time. 
Furthermore, pressure and temperature sensors installed in the constant- 
volume vessel collected real-time ambient condition data. These data 
were transmitted to the master computer via a data acquisition (DAQ) 
card for real-time monitoring. Finally, a dedicated data acquisition 
computer communicated with the high-speed camera via an Ethernet 
connection to ensure the high-speed transfer of image data.(see Fig. 1 ).
Furthermore, high-pressure hydrogen injection forms a typical 
under-expanded jet. According to Prandtl-Meyer expansion wave 
theory, a complex shock wave system is generated at the nozzle exit 
[ 23 ]. To this end, a small-aperture schlieren lens assembly combined 
with a telephoto lens was employed to capture the fine-scale shock 
structures in the near-field region of the jet. The experimental setup is 
illustrated in Fig. 2 . The small-aperture schlieren assembly generated a 
collimated light beam passing through the near-nozzle region, and a 
high-speed camera was utilized to capture the jet structure. This camera 
operated at a resolution of 1152 × 384 pixels, a frame rate of 40,000 
frames per second (fps), and an exposure time of 10 μ s.
The injection rate was measured using a combination of two 
methods. The transient flow profile was obtained by recording the jet 
impact force signal, while the injection mass per cycle was measured 
using the water displacement method. These two sets of data were 
coupled to calibrate and determine the final absolute injection rate of 
the hydrogen jet. Specifically, the impact force was measured using a 
Kistler-9217 high-precision piezoelectric force sensor. To accurately 
capture the highly transient impact force dynamics of the high-pressure 
hydrogen, the sampling frequency of the data acquisition system was set 
at 250 kHz. The sensor's output signal was routed through a charge 
amplifier, collected by a data acquisition (DAQ) card, and transmitted to 
Fig. 1. Visualization test platform.
Z. Zhang et al.                                                                                                                                                                                                                                   Energy 359 (2026) 141499 
3

<!-- PDF_PAGE: 4 -->

the master computer for processing, thereby yielding a dimensionless 
momentum curve. The injection mass of each injection was obtained by 
the water displacement method, and then the momentum curve ob -
tained above can be calibrated to obtain the injection rate. As shown in 
Fig. 3 , given the use of a single-hole nozzle, the force sensor was posi -
tioned vertically directly below the nozzle orifice at a distance of less 
than 1 cm to ensure complete capture of the momentum signal [ 24 ].
2.2. Experimental method
2.2.1. Experimental plan
In practical applications of hydrogen internal combustion engines, 
parameters such as injection pressure must be dynamically adjusted in 
real time according to load and power demands to ensure precise fuel 
delivery. Because the injector serves as the core actuator of the fuel 
system, its dynamic response characteristics under varying operating 
conditions directly dictate the precision of fuel mass control and the 
quality of subsequent mixture formation. Therefore, to comprehensively 
characterize its dynamic actuation behaviors, this study conducted 
hydrogen jet tests across a range of injection and ambient pressures. All 
experiments were performed in a quiescent nitrogen environment, with 
the specific test parameters detailed in Table 1 .
2.2.2. Parameter definition and data processing
To quantitatively characterize the macroscopic jet structure, five key 
parameters were evaluated: jet penetration ( S ), jet tip velocity, far-field 
cone angle, projected area, and volume. The geometric definitions of 
these parameters are illustrated in Fig. 4 . Among them, the penetration S 
is defined as the distance from the nozzle exit to the jet tip. The jet tip 
velocity was calculated using a backward difference method in the 
discrete time domain; specifically, by dividing the difference in 
Fig. 2. Schematic diagram of the near-field small-scale jet and shock wave structure test of the nozzle.
Fig. 3. Injection rate test platform.
Table 1 
Experimental parameters.
Parameter Numerical value
Ambient temperature/K 302
Nozzle diameter/mm 0.58
Energizing time/ms 3
Types of fuel gases H
2
(purity > 99.98%)
Types of ambient gas N
2
Gas injection pressure/MPa 15, 20, 25, 30, 35
Ambient gas pressure/MPa 0.1,1, 2, 3
The diameter of light transmission in the test area/mm 150
Far-field spatial resolution 0.1754 mm/pixel
Near-field spatial resolution 0.0127 mm/pixel
Fig. 4. Definition of macrostructural characteristic parameters for jet.
Z. Zhang et al.                                                                                                                                                                                                                                   Energy 359 (2026) 141499 
4

<!-- PDF_PAGE: 5 -->

penetration between consecutive frames by the imaging time interval. 
The far-field cone angle was determined through a boundary-fitting al -
gorithm applied to the upstream half of the jet body (i.e., axial distance 
< S/2). The coordinates of the left and right jet boundaries were 
extracted at specified pixel intervals, and a linear fit was independently 
applied to each side. The angle formed by the intersection of these two 
fitted lines defines the far-field cone angle. Given that a single-hole 
circular nozzle was utilized in this experiment, the resulting free jet 
exhibited statistical axisymmetry. Based on this axisymmetric assump -
tion, the three-dimensional jet volume was reconstructed from the two- 
dimensional schlieren projections. Specifically, the total volume was 
calculated by integrating a series of cylindrical differential elements 
along the jet axis, where the height of each element corresponded to the 
spatial resolution of a single pixel. Although this two-dimensional to 
three-dimensional reconstruction method introduces certain approxi -
mations, the inherent error remains entirely acceptable for the 
comparative analysis of macroscopic volume trends under varying in -
jection pressures.
Image post-processing was performed using MATLAB, as shown in 
Fig. 5 . First, a pre-injection frame was recorded as the background 
reference. Background subtraction was then applied to eliminate 
ambient optical noise and isolate the transient jet region from the raw 
images. Subsequently, the isolated images were binarized to convert the 
jet morphology into a binary mask. Morphological closing operations 
were employed to bridge small gaps within the jet body and connect 
fragmented structures near the nozzle exit. An internal hole-filling al -
gorithm was then applied to remove enclosed cavities and suppress re -
sidual noise, followed by morphological dilation to smooth the jet 
boundary, thereby enabling accurate spatial delineation of the jet en -
velope. To ensure the reliability and objectivity of the aforementioned 
binarization process, an adaptive Otsu's method was utilized, effectively 
eliminating the subjective bias inherent in manual threshold selection. A 
threshold sensitivity analysis demonstrated that varying the segmenta -
tion threshold by ± 10% around the adaptive reference value resulted in 
a maximum deviation of only ± 6% in the calculated jet projected area, 
confirming the excellent robustness of the image processing algorithm.
3. Experimental results and discussion
3.1. Injection rate
Fig. 6 shows the injection mass under different operating conditions. 
As can be seen from the figure, the injection mass increases accordingly 
as the injection pressure and energizing time increase.
However, the curve exhibits a steeper, nonlinear slope for shorter 
energizing times. This nonlinearity arises because, during brief actua -
tion periods, the needle valve fails to reach its maximum lift. Conse -
quently, the injection rate assumes a triangular profile, leading to a 
nonlinear relationship between the injection mass and energizing time. 
Conversely, when the energizing time is sufficiently long, the needle 
valve attains its maximum lift, and the injection mass becomes linearly 
proportional to the energizing time. The detailed evolution of the in -
jection rate profiles is illustrated in Fig. 7 (a).
Fig. 7 (b) presents the injection rate profiles at various injection 
pressures for a fixed energizing time of 3 ms. Notably, the initial rise of 
the injection rate remains largely independent of the injection pressure. 
However, during the closing phase, a higher injection pressure signifi -
cantly advances the end of injection, shortening the maximum injection 
duration by up to 11.6%. This phenomenon occurs because elevating the 
injection pressure increases the gas pressure within the valve chamber, 
thereby exerting a greater downward aerodynamic force on the upper 
surface of the armature. During the initial opening phase, the electro -
magnetic driving force dominates the valve dynamics, rendering the 
opening delay relatively insensitive to varying injection pressures. In 
contrast, upon de-energization, the electromagnetic force dissipates. 
The high injection pressure then creates a substantial pressure differ -
ential across the armature, which significantly increases the seating 
force and accelerates the closure of the needle valve, as schematically 
illustrated in Fig. 8 .
3.2. Macroscopic structure and evolution of high-pressure hydrogen jet
To elucidate the macroscopic structural evolution mechanisms of 
extremely under-expanded hydrogen jet under varying operating con -
ditions, it is necessary to first determine the expansion state of the jet. 
Assuming hydrogen behaves as an ideal gas, based on one-dimensional 
isentropic flow theory, the flow state of the gas at the nozzle exit de -
pends on the ratio of the injection pressure to the ambient pressure. 
When this pressure ratio exceeds a critical value, the flow becomes 
choked, and the exit velocity reaches the local speed of sound. The 
critical pressure ratio R* is defined by Eq. (1) . 
R ∗ =
P
0
P
cr
=
(
2
γ + 1
)
γ
γ  1
(1) 
In Eq. (1) , P
cr 
represents the critical outlet static pressure, P
0 
is the up -
stream stagnation pressure, and γ is the specific heat ratio of the gas. For 
hydrogen, this critical pressure ratio is approximately 1.894. When the 
pressure ratio between the upstream and downstream exceeds this 
value, choking occurs. Because the pressure ratios under all operating 
conditions in this study far exceed this critical value, the jet is forced into 
an extremely under-expanded state. Upon exiting the nozzle, the gas 
releases excess pressure energy through a series of intense expansion 
Fig. 5. Jet image processing.
Fig. 6. The influence of energizing time and injection pressure on injec -
tion mass.
Z. Zhang et al.                                                                                                                                                                                                                                   Energy 359 (2026) 141499 
5

<!-- PDF_PAGE: 6 -->

and compression waves, thus presenting the complex jet structures 
observed in Figs. 9 and 10 .
At the downstream end of the jet, a distinct curved structure appears 
ahead of the jet tip. This phenomenon occurs because the jet tip velocity 
of the highly under-expanded jet exceeds the local ambient speed of 
sound, strongly compressing the quiescent gas ahead and forming a 
detached bow shock. As this shock wave propagates through the 
ambient gas, it is accompanied by an intense aerodynamic compression 
effect. Furthermore, Figs. 9 and 10 illustrate the macroscopic spatio -
temporal evolution of the extremely under-expanded hydrogen jet. 
Temporally, the jet rapidly expands outward and undergoes intense 
volumetric expansion immediately upon exiting the nozzle. Fig. 9
clearly demonstrates the suppressive effect of varying ambient pressures 
on the jet flow at a constant injection pressure. As ambient pressure 
increases, the ambient gas density and aerodynamic drag also increase 
sharply, severely constraining the radial expansion of the jet. The axial 
advancement of the leading edge is significantly hindered, causing the 
overall jet morphology to transition gradually from a broad plume under 
low ambient pressure to a slender profile under high ambient pressure. 
Fig. 10 illustrates the influence of injection pressure on jet morphology 
under a constant ambient pressure. As injection pressure increases, the 
initial momentum of the jet becomes greater, leading to more intense 
radial expansion and deeper axial penetration at any given time instant. 
Concurrently, the contrast between the light and dark regions at the jet 
boundary and within its interior is significantly enhanced, directly 
reflecting the sharper density gradients produced under higher injection 
pressures. These qualitative macroscopic observations provide a solid 
foundation for the subsequent quantitative analysis of the jet charac -
teristic parameters.
Fig. 7. The influence of energizing time and injection pressure on injection rate.
Fig. 8. Needle valve working principle diagram.
Fig. 9. The influence of ambient pressure on the macroscopic structure of the jet.
Z. Zhang et al.                                                                                                                                                                                                                                   Energy 359 (2026) 141499 
6

<!-- PDF_PAGE: 7 -->

Fig. 10. The influence of injection pressure on the macroscopic structure of the jet.
Fig. 11. The influence of injection pressure and ambient pressure on the jet penetration.
Z. Zhang et al.                                                                                                                                                                                                                                   Energy 359 (2026) 141499 
7

<!-- PDF_PAGE: 8 -->

3.2.1. Jet penetration characteristics
Jet penetration is a critical parameter for evaluating the macroscopic 
spatial distribution of the fuel and its mixing characteristics with the 
ambient gas Fig. 11 (a) illustrates the effect of injection pressure on 
hydrogen jet penetration at a constant ambient pressure of 0.1 MPa. 
During the initial stage of the jet, the penetration under different jet 
pressures show no significant variation. However, as the jet evolves, 
higher injection pressures result in markedly longer penetration, as 
depicted in Fig. 11 (c). Analysis reveals that for highly under-expanded 
jet, although the nozzle exit is choked, the gas undergoes intense 
Prandtl-Meyer expansion upon exiting and is rapidly accelerated in the 
near-field region. Theoretically, a higher injection pressure should 
trigger a stronger post-exit acceleration effect. The primary reason for 
the negligible difference observed in the early-stage penetration lies in 
the transient throttling effect during the needle valve opening process of 
the direct-acting injector. Within the extremely short initial opening 
phase, the needle valve has not yet reached its maximum lift, severely 
restricting the effective flow area at the nozzle orifice. Consequently, the 
actual driving pressure is not yet fully established. Furthermore, the 
initial jet front must overcome the substantial static inertial resistance of 
the surrounding ambient gas. The combined effect of these two factors 
temporarily masks the initial acceleration advantage associated with 
higher injection pressure. Once the needle valve is fully open and the 
quasi-steady flow field is established, the strong expansion-induced ac -
celeration and momentum advantages produced by the higher injection 
pressure become dominant, leading to significant divergence in pene -
tration during the intermediate and later stages.
Compared to the injection pressure, the ambient pressure exerts a 
more profound influence on jet penetration. As illustrated in Fig. 11 (b), 
at an injection pressure of 35 MPa and T
ASOI 
= 1 ms, increasing the 
ambient pressure from 0.1 MPa to 3 MPa causes the penetration to 
decrease by nearly 45%. Higher ambient pressures correspond to 
increased ambient gas densities. During the penetration process, the jet 
must displace and entrain the surrounding quiescent gas. Consequently, 
a higher ambient density subjects the jet to greater aerodynamic drag, 
leading to a more rapid decay of momentum. Furthermore, an increase 
in ambient pressure reduces the degree of under-expansion at the nozzle 
exit, which weakens the expansion-induced acceleration effect, subse -
quently reducing the momentum and penetrating capability of the jet. 
Although gas jet lack the secondary breakup and fragmentation pro -
cesses characteristic of liquid sprays, their initial kinetic energy at the 
nozzle exit is finite; thus, under the continuous action of aerodynamic 
drag, the gas jet progressively decelerates.
The jet tip velocity is a crucial parameter for characterizing the 
spatial progression of the gas and estimating its flow velocity distribu -
tion. Although the severe under-expansion forces the gas to accelerate 
rapidly upon exiting the nozzle orifice, this near-field internal acceler -
ation has a limited impact on the macroscopic jet tip velocity of the jet. 
Fig. 12 (a) presents the temporal evolution of the jet tip velocity under 
various injection pressures at a constant ambient pressure of 0.1 MPa. 
During the initial injection stage, a higher injection pressure yields a 
higher maximum jet tip velocity. However, as the jet develops, the jet tip 
velocity begins to decline rapidly, and the divergence between the ve -
locity curves under different injection pressures gradually diminishes. 
Because high-pressure hydrogen jet inherently possess a low mass flow 
rate, the choked condition at the outlet fundamentally restricts the total 
injected kinetic energy, causing the forward momentum to dissipate 
rapidly under ambient aerodynamic drag. Additionally, an elevated in -
jection pressure intensifies the radial expansion of the jet, which in -
creases the frontal interaction area with the ambient gas and 
consequently induces greater aerodynamic drag. These factors balance 
each other, so that over time, the jet tip velocity becomes relatively 
small under different injection pressures, and the differences between 
them become insignificant.
Fig. 12 (b) illustrates the influence of ambient pressure on the jet tip 
velocity at a constant injection pressure of 35 MPa. This suppressive 
effect on the jet tip velocity is highly pronounced due to the entrainment 
of the ambient gas and the resulting aerodynamic drag. With increasing 
ambient pressure, the jet tip velocity decreases significantly. Notably, at 
an ambient pressure of 3 MPa, the maximum velocity does not exceed 
220 m/s, and it continues to decay progressively over time.
3.2.2. Jet spatial morphological characteristics
Fig. 13 (a) shows the influence of different injection pressures on the 
jet far-field cone angle at an ambient pressure of 0.1 MPa. The results 
indicate that the far-field cone angle initially exhibits a sharp decrease 
before transitioning into a fluctuating quasi-steady state. This phe -
nomenon occurs because, during the initial injection stage, the transient 
throttling effect of the needle valve severely restricts the mass flow rate. 
Furthermore, hydrogen is characterized by extremely low density and 
large intermolecular distances, resulting in weak intermolecular forces 
and high compressibility. Macroscopically, this manifests as severe 
morphological instability at the jet boundary, leading to significant 
initial fluctuations in the far-field cone angle. Once the quasi-steady flow 
rate is established, the macroscopic jet morphology stabilizes. In addi -
tion, due to the increase in injection pressure, the injection mass of the 
jet increases, which leads to an increase in the jet far-field cone angle at 
the initial stage of the jet as the injection pressure increases. Fig. 13 (b) 
shows the influence of different ambient pressures on the jet far-field 
cone angle when the injection pressure is 35 MPa. As ambient pres -
sure increases, the elevated ambient density exerts greater aerodynamic 
drag on the developing jet, thereby suppressing its radial expansion 
Fig. 12. The influence of injection pressure and ambient pressure on the jet tip velocity.
Z. Zhang et al.                                                                                                                                                                                                                                   Energy 359 (2026) 141499 
8

<!-- PDF_PAGE: 9 -->

capability. Therefore, at the initial stage of injection, the ambient 
pressure increases, the far-field cone angle decreases, and then tends to 
fluctuate.
Clarifying the macroscopic spatial distribution of the jet and its 
mixing characteristics with the ambient gas is crucial for optimizing 
subsequent combustion and emission processes. To effectively evaluate 
the quality of mixture formation and optimize the injection system 
design, it is necessary to acquire the temporal evolution of the jet's 
projected area and volume, in addition to mastering the injection rate.
Fig. 14 (a) shows the influence of different injection pressures on the 
jet area when the ambient pressure is 0.1 MPa. As the injection pressure 
increases, the injection rate also increases. The higher injection pressure 
at the outlet promotes its spatial distribution after expansion. Therefore, 
the area of the jet increase with the increase of the injection pressure. 
The influence of ambient pressure on the gas jet area when the injection 
pressure is 35 MPa as shown in Fig. 14 (b). At T
ASOI 
= 1 ms, the jet area at 
0.1 MPa pressure is approximately 70% higher than that at an ambient 
pressure of 3 MPa and about 50% higher than that at an ambient pres -
sure of 1 MPa. For direct-injection engines, substantially elevating the 
injection pressure serves as an effective strategy to expand the spatial 
distribution of the gaseous fuel and enhance mixture uniformity.
Fig. 15 (a) shows the influence of different injection pressures on the 
jet volume at P
b 
= 0.1 MPa, and Fig. 15 (b) shows the influence of 
different ambient pressures on the jet volume at P
inj 
= 35 MPa. Fig. 16
shows the rate of volume change under different injection pressures and 
different ambient pressures. Specifically, the instantaneous relative 
volume change rate was calculated using a discrete difference method, 
defined as the volume difference between consecutive frames divided by 
the volume of the preceding frame.
Analysis indicates that under low ambient pressure 
conditions — characterized by reduced aerodynamic drag — the gas jet 
exhibits robust spatial expansion capabilities. For instance, at T
ASOI 
=
1.0 ms, the ambient pressure decreases from 3 MPa to 0.1 MPa, and the 
jet volume expands nearly 7 times. Additionally, the jet volume in -
creases monotonically with elevated injection pressures. Regarding the 
relative volume change rate, the initial values under all tested injection 
and ambient pressures exceed 100%, but progressively stabilize below 
50% over time. These results suggest that while an elevated injection 
pressure significantly enlarges the volume of the jet, it exerts a negligible 
impact on the rate of volume change. This phenomenon occurs because, 
during the initial injection stage, the rapid geometric expansion causes 
the local fuel concentration to decay sharply, prompting the volume 
change rate to plummet before reaching a quasi-steady state. Although a 
higher injection pressure enhances both the injection mass and injection 
rate, it concurrently intensifies the turbulent disturbance and ambient 
gas entrainment. Therefore, its impact on the average fuel-air ratio 
throughout the entire injection process is not significant.
Fig. 13. The influence of injection pressure and ambient pressure on the far-field cone angle.
Fig. 14. The influence of injection pressure and ambient pressure on the jet area.
Z. Zhang et al.                                                                                                                                                                                                                                   Energy 359 (2026) 141499 
9

<!-- PDF_PAGE: 10 -->

Fig. 15. The influence of injection pressure and ambient pressure on the jet volume.
Fig. 16. Volume change rate under different injection pressures.
Fig. 17. Diagram of the structure and formation mechanism of shock waves.
Z. Zhang et al.                                                                                                                                                                                                                                   Energy 359 (2026) 141499 
10

<!-- PDF_PAGE: 11 -->

3.3. Analysis of under-expanded jet shock wave structure
The shock wave system of extremely under-expanded hydrogen jet is 
relatively complex. The drastic pressure and velocity gradients induced 
by these shock waves fundamentally alter the mixing characteristics 
between the jet and the ambient medium. Furthermore, the resulting 
unstable shear layers significantly influence the macroscopic morpho -
logical evolution of the jet.Although Wu et al. [ 25 ] characterized the 
shock wave structures of medium-pressure hydrogen jet (below 2.5 
MPa), and Dong et al. [ 26 ] systematically analyzed the impact of 
high-pressure natural gas shock structures on engines, these findings 
derived from heavier gases cannot be directly extrapolated to 
high-pressure hydrogen. Under high-pressure conditions, natural gas jet 
typically exhibit a topological structure comprising a series of reflected 
shock cells. Conversely, due to the exceptionally high speed of sound 
and low density of hydrogen, the Prandtl-Meyer expansion effect at the 
nozzle exit is far more pronounced. The excess pressure potential energy 
often concentrates in the near field and tends to rapidly merge into a 
single large Mach disk. However, previous experimental studies have 
mostly focused on lower injection pressures and other types of gaseous 
fuels. For hydrogen, a gaseous fuel that combines high speed of sound 
and low density, there are few studies on the structural evolution 
characteristics of the induced shock waves generated by its 
high-pressure injection.
The topological structure and formation mechanisms of the under- 
expanded shock waves near the nozzle are schematically illustrated in 
Fig. 17 . At the nozzle exit cross-section, the hydrogen flow is choked, 
exiting at the local speed of sound. Immediately upon exiting the nozzle, 
the high-pressure hydrogen is suddenly exposed to the relatively low- 
pressure ambient gas. According to Prandtl-Meyer expansion theory, 
the high-pressure gas deflects radially outward at the nozzle lip and 
accelerates through a highly divergent expansion fan, attaining a Mach 
number significantly greater than unity. Subsequently, these adjacent, 
high-speed deflected airflow streamlines intersect. Because fluids cannot 
penetrate each other, a series of compression waves are generated at the 
convergence of streamlines. As these compression waves propagate, 
they continuously superimpose and steepen, eventually coalescing into a 
strong oblique shock wave. Given the circular structure of the nozzle, 
this oblique shock wave presents as a barrel shock wave in three- 
dimensional space. Subsequently, constrained by the barrel shock 
wave, the circumferential supersonic hydrogen jet deflects inward and 
converges, eventually colliding strongly along the jet axis to form a 
normal shock wave, known as the Mach disk. Across the Mach disk, the 
high-pressure hydrogen jet undergoes a sudden transition from highly 
supersonic to subsonic flow, abruptly recovering to a pressure state 
nearly in equilibrium with the ambient environment [ 27 , 28 ].
Fig. 18 shows the influence of different injection pressures and 
different ambient pressures on the near-field structure of the jet at the 
same time. The experimental results show that when the ambient 
pressure is 0.1 MPa and 1 MPa, the jet exhibits an extremely under- 
expanded structure, and the single large Mach disk structure at the 
nozzle is clearly visible. As the ambient pressure increases, the overall 
shape of the Mach disk decreases. When the ambient pressure reaches 2 
MPa, shock cells featuring Mach reflection emerge as the injection 
pressure decreases. When the ambient pressure is 3 MPa, the overall 
manifestation is a shock cells with a Mach reflection structure, charac -
terized by the appearance of a normal shock wave perpendicular to the 
incoming flow along the axis. The shape of under-expanded jet is 
directly related to the pressure ratio. As the pressure ratio increases, the 
shock wave topology of the jet undergoes a transformation from a shock 
cells with a Mach reflection structure to a single huge Mach disk form. 
Specifically, when the pressure ratio is less than 12.5, the expansion 
waves reaching the free boundary of the jet is reflected as compression 
waves due to the constant-pressure ambient boundary condition. These 
compression waves converge in the core area of the jet and re-compress 
the fluid, raising the pressure above the ambient pressure and thereby 
Fig. 18. Near-field structure diagrams of jet with different injection pressures and different ambient pressures.
Z. Zhang et al.                                                                                                                                                                                                                                   Energy 359 (2026) 141499 
11

<!-- PDF_PAGE: 12 -->

triggering the expansion process again. This cycle of “ expansion to 
compression to re-expansion ” repeats along the axial direction, forming 
a typical shock wave cells with Mach reflection structure. When the 
pressure continues to increase and the pressure ratio exceeds 12.5, the 
intense expansion effect causes the size of the first Mach disk to increase 
sharply and move backward along the jet. This strong normal shock 
induces a substantial total pressure loss downstream, thereby sup -
pressing the formation of subsequent periodic shock wave structures. 
Meanwhile, the Mach disk induced a large area of low-speed core behind 
it, and a strong velocity discontinuity was formed between this low- 
speed area and the high-speed fluid surrounding it, that is, the inter -
nal shear layer (slip line).
The Mach disk is the core structure for the transition of the jet from 
an extremely under-expanded state to ambient pressure equilibrium. Its 
position and intensity affect the topological structure and mixing pro -
cess in the near-field region of the jet. As shown in Fig. 19 , it was found 
through experiments that for hydrogen, a gas with high sound speed and 
low density, the formation of the Mach disk goes through three stages. In 
the first stage ( T
ASOI 
≤ 0.05 ms), immediately following the start of in -
jection, the exiting gas flow encounters a sudden geometric expansion at 
the nozzle lip. Driven by the immense pressure differential, the flow 
must deflect radially to expand and depressurize. The deflection of this 
supersonic flow around the convex corner inevitably generates an 
expansion fan. Macroscopically, this manifests as a fan-shaped Prandtl- 
Meyer (P-M) expansion wave originating at the upper and lower lips of 
the nozzle exit, indicated by the yellow dotted arc in Fig. 19 (a).
As the injection progresses into the second stage (0.05 < T
ASOI 
≤
0.15 ms). The jet is still affected by the spatial shape at the nozzle exit, so 
the cross-section of the jet has not been fully expanded. The Prandtl- 
Meyer expansion waves at the nozzle exit converge and propagate to -
wards the jet axis to reduce the pressure difference between the injection 
pressure and the ambient pressure. Due to the short propagation path 
and limited space, these expansion waves will cross within the range 
constrained by the barrel shock wave. Macroscopically, this manifests at 
approximately T
ASOI 
= 0.075 ms as the P-M wave propagating outward 
from the jet and interacting with the jet boundary, thereby generating 
compression waves. At the same time, the initial form of a barrel shock 
wave is formed inside the jet, and the intersection of expansion waves 
occurs within the barrel shock wave,as shown in Fig. 19 (b).
In the third stage ( T
ASOI 
> 0.15 ms), as the injection process con -
tinues, the cross-section of the jet expands, the barrel wave gradually 
extends outward. Meanwhile, when the P-M wave reaches the free 
boundary, it will be “ reflected ” by the jet boundary into a compressed 
wave. At this juncture, the propagation direction of the expansion waves 
transitions from converging toward the axis to diverging outward 
alongside the jet boundary. The expansion of the jet space and the 
boundary reflection of the expansion wave work together to prevent the 
expansion waves above and below the nozzle from crossing towards the 
center, but instead propagate outward along the boundary as the jet 
expands. Ultimately, the expansion waves no longer intersect within the 
barrel shock. The macroscopic manifestation of this stage is the fully 
developed barrel shock accompanied by a distinct Mach disk, as depic -
ted in Fig. 19 (c).
3.3.1. Analysis of characteristic parameters of under-expanded jet shock 
waves under different injection pressures
The distance of the Mach disk from the nozzle exit indicates the 
degree of jet under-expansion, while its diameter reflects the expansion 
boundary and mass flow rate of the jet along the axis. The maximum 
diameter of the barrel shock defines the lateral boundary of the jet, and 
the point where the barrel shock converges corresponds to the Mach disk 
height. To quantitatively characterize the shock wave system, this study 
selected the Mach disk height, Mach disk width, maximum barrel shock 
diameter, and the jet angle measured at an axial distance of five nozzle 
diameters from the nozzle exit (near-field cone angle) as the key geo -
metric parameters. Fig. 17 illustrates the definitions and measurement 
locations of these parameters within the shock wave topology.
In extremely under-expanded jet, the injection pressure exerts a 
profound impact on the morphology of the Mach disk. During the 
transient injection startup, the flow transitions from subsonic to highly 
under-expanded supersonic conditions; therefore, the Mach disk does 
not form instantaneously upon jet emergence. Fig. 20 (a) – (c) shows the 
test results of shock wave parameters obtained by using a 0.58 mm 
diameter nozzle at an ambient pressure of 0.1 MPa. As the pressure ratio 
increases, the degree of under-expansion intensifies. The jet requires a 
longer distance to complete the full expansion process and undergoes 
Fig. 19. The development process diagram of the Mach disk.
Z. Zhang et al.                                                                                                                                                                                                                                   Energy 359 (2026) 141499 
12

<!-- PDF_PAGE: 13 -->

more intense radial expansion at the nozzle exit. The expansion fan 
emanating from the nozzle lip becomes stronger, thereby increasing the 
initial expansion angle of the jet. Macroscopically, this manifests as an 
increase in the maximum barrel shock diameter, a widening of the Mach 
disk, and an elevation in the Mach disk height.
Fig. 20 (d) shows the influence of different injection pressures on the 
near-field cone angle of the jet. Temporally, the near-field cone angle 
initially exhibits a rapid increase before entering a fluctuating quasi- 
steady phase. These fluctuations reflect the irregular dynamics of the 
turbulent structures within the shear layer. Moreover, as the injection 
pressure increases, the near-field cone angle also increases. At an in -
jection pressure of 35 MPa, the average near-field cone angle stabilizes 
at approximately 68
◦
, whereas at 15 MPa, it is only about 55
◦
. This in -
dicates that the higher injection pressure significantly alters the near- 
field spatial morphology of the jet. The underlying physical mecha -
nism is that a higher pressure ratio drives a more intense Prandtl-Meyer 
expansion fan at the nozzle exit. To release the excess pressure and 
equilibrate with the ambient environment, the exiting gas is forced to 
undergo a larger radial deflection, thereby broadening the near-field 
cone angle.
3.3.2. Analysis of characteristic parameters of under-expanded jet shock 
waves under different ambient pressures
For extremely under-expanded high-speed jet, the decisive param -
eter governing the shock wave topology is the pressure ratio. Therefore, 
investigating the injection pressure in isolation provides an incomplete 
perspective; a coupled analysis incorporating ambient pressure 
variations is essential. As illustrated in Fig. 21 (a) – (c), at a constant in -
jection pressure of 35 MPa, an increase in ambient pressure causes the 
maximum diameter of the barrel shock to decrease. Furthermore, the 
Mach disk shifts upstream closer to the nozzle exit, and its radial width 
narrows significantly.
Fig. 21 (d) shows the influence of different ambient pressures on the 
near-field cone angle at an injection pressure of 35 MPa. Under an 
ambient pressure of 0.1 MPa, the jet exhibits extremely expansive 
characteristics, with an average near-field cone angle of approximately 
68
◦
. However, as the ambient pressure increases from 0.1 MPa to 4 MPa, 
the downward trend of the jet near-field cone angle is obvious. At 4 MPa, 
the radial expansion is severely constrained, with the average near-field 
cone angle contracting to approximately 39
◦
. The primary physical 
mechanism behind this radial suppression is the reduction in the pres -
sure ratio, which attenuates the strength of the Prandtl-Meyer expansion 
fan and correspondingly reduces the outward deflection angle of the 
exiting streamlines. Additionally, the elevated ambient gas density in -
duces greater aerodynamic drag, which further restricts the radial 
dispersion of the jet and forces it to maintain a more convergent profile. 
Furthermore, a comparative analysis of Figs. 12 and 20(d) and 21(d)
reveals that the near-field cone angle of the jet is consistently larger than 
its far-field counterpart. This discrepancy arises because the intense 
Prandtl-Meyer expansion at the nozzle exit dictates the large initial near- 
field cone angle. However, as the jet develops downstream, the reduced 
relative velocity between the jet core and the entrained ambient gas 
suppresses lateral momentum exchange and radial mixing, thereby 
resulting in a narrower far-field cone angle.
Fig. 20. The influence of different injection pressures on shock wave structure.
Z. Zhang et al.                                                                                                                                                                                                                                   Energy 359 (2026) 141499 
13

<!-- PDF_PAGE: 14 -->

4. Conclusion
This paper investigated the transient injection characteristics of a 
high-pressure hydrogen injector and systematically characterized the 
spatiotemporal evolution mechanisms of extremely under-expanded 
hydrogen jet under varying injection and ambient pressures. The main 
conclusions are as follows. 
(1) Based on combined measurements using the momentum method 
and the water displacement method, it was found that for the 
direct-acting high-pressure hydrogen injector, the injection 
pressure not only determines the maximum transient flow rate 
but also significantly influences the needle valve dynamics. At the 
same energizing time, as the injection pressure increased from 15 
MPa to 35 MPa, the peak transient mass flow rate rose from 0.58 
mg/ms to 1.26 mg/ms, representing an increase of 117%. 
Concurrently, the enhanced pressure differential across the nee -
dle valve accelerated its seating, resulting in an 11.6% reduction 
in the injection duration.
(2) Based on the schlieren imaging system, the evolution character -
istics of highly under-expanded hydrogen jet was clarified. The 
results showed that, at a constant energizing time, increasing the 
injection pressure from 15 MPa to 35 MPa led to a 41% increase 
in the penetration. The ambient pressure exerts a strong sup -
pressive effect. As it increases from 0.1 MPa to 3 MPa, the 
penetration decreases by 86%. Furthermore, strong ambient 
aerodynamic drag restricts the maximum jet tip velocity to below 
450 m/s. During the intermediate and later stages of injection, 
the jet tip velocity is governed by the competing effects of nozzle 
choking and aerodynamic drag, resulting in marginal differences 
in tip velocities across varying injection pressures.
(3) The spatial expansion capability of extremely under-expanded 
hydrogen jet was systematically evaluated using characteristic 
parameters such as the far-field cone angle, projected area, and 
volume. The results indicate that the far-field cone angle fluctu -
ates during the initial stage due to morphological instability 
before transitioning to a stable plateau. Low ambient pressure 
promotes the spatial dispersion of the jet. At an injection pressure 
of 35 MPa and an ambient pressure of 0.1 MPa, the jet volume is 
nearly six times larger than that at 4 MPa. Moreover, under all 
tested injection pressures, the initial relative volume change rate 
consistently exceeded 100%, gradually stabilizing below 40% as 
the jet developed. This confirms that the jet undergoes a highly 
intense and rapid turbulent mixing process during the early in -
jection phase.
(4) The shock wave topology of extremely under-expanded jet is 
fundamentally dictated by the pressure ratio. As the pressure 
ratio increases, the shock structure transitions from a series of 
shock cells featuring Mach reflection to a single, massive Mach 
disk. The formation of this massive Mach disk progresses through 
three distinct stages: the emergence of Prandtl-Meyer expansion 
fans, the intersection of these expansion waves within the nascent 
barrel shock, and the subsequent propagation of these expansion 
waves beyond the barrel shock. This sequence reveals the dy -
namic pathway of pressure potential energy release under ultra- 
high pressure ratios. Furthermore, shock evolution directly dic -
tates the macroscopic jet morphology; a higher pressure ratio 
Fig. 21. The influence of different ambient pressures on shock wave structure.
Z. Zhang et al.                                                                                                                                                                                                                                   Energy 359 (2026) 141499 
14

<!-- PDF_PAGE: 15 -->

intensifies the post-exit expansion, yielding a broader near-field 
cone angle.
CRediT authorship contribution statement
Ziteng Zhang: Writing – review & editing, Writing – original draft, 
Validation, Methodology. Yafei Yuan: Investigation. Xiyu Yang: Su -
pervision, Project administration, Funding acquisition. Fangliang 
Yang: Software. Cheng Shi: Investigation. Xiaoyan Wang: Formal 
analysis.
Declaration of competing interest
The authors declare that they have no known competing financial 
interests or personal relationships that could have appeared to influence 
the work reported in this paper.
Acknowledgments
The authors would like to acknowledge the financial supports pro -
vided by National Key Laboratory of Internal Combustion Engine and 
Power System Open Project Fund (Grant No. skleps-sq-2024-214); Nat -
ural Science Foundation of Hebei Province (Grant No. E202403064); 
Science and Technology Program of Higher Education Institutions, 
Department of Education of Hebei Province (Grant No. QN2025062); 
Hebei Province Yanzhao Golden Peak Talent Program (Returnees Inte -
gration Platform) (Grant No. A2025007).
Data availability
Data will be made available on request.
References
[1] Zhou F, Wu C, Fu J, et al. Abnormal combustion and NOx emissions control 
strategies of hydrogen internal combustion engine. Renew Sustain Energy Rev 
2025;219:115847 .
[2] Turner JWG. Future technological directions for hydrogen internal combustion 
engines in transport applications. Applications in Energy and Combustion Science 
2025;21:100302 .
[3] Kiouranakis KI, de Vos P, Zoumpourlos K, et al. Methanol for heavy-duty internal 
combustion engines: review of experimental studies and combustion strategies. 
Renew Sustain Energy Rev 2025;214:115529 .
[4] Akhtar MUS, Asfand F, Khan MI, et al. Performance and emissions characteristics of 
hydrogen-diesel dual-fuel combustion for heavy-duty engines. Int J Hydrogen 
Energy 2025 .
[5] Babayev R, Mor ´en M, Johansson B. Comparative computational study of hydrogen 
and natural gas in high-pressure direct-injection (HPDI) compression-ignition 
engines: combustion characteristics, thermal efficiency, and local pollutant and 
greenhouse gas emissions. Fuel 2025 .
[6] Abe JO, Popoola API, Ajenifuja E, et al. Hydrogen energy, economy and storage: 
review and recommendation. Int J Hydrogen Energy 2019;44(29):15072 – 86 .
[7] Peters M, Maes N, Dam N, et al. Characterizing and visualizing the direct injection 
of hydrogen into high-pressure argon and nitrogen environments. Int J Hydrogen 
Energy 2024;66:304 – 15 .
[8] Khalid AH, Said MFM, Veza I, et al. Hydrogen port fuel injection: review of fuel 
injection control strategies to mitigate backfire in internal combustion engine 
fuelled with hydrogen. Int J Hydrogen Energy 2024;66:571 – 81 .
[9] Tinchon A, Foucher F, Doradoux L. Hydrogen jet characterization of an internal 
combustion engine injector using Schlieren imaging[R]. SAE Technical Paper 
2023 .
[10] Yip HL, Srna A, Yuen ACY, et al. A review of hydrogen direct injection for internal 
combustion engines: towards carbon-free combustion. Applied Sciences 2019;9 
(22):4842 .
[11] Goyal H, Jones P, Bajwa A, et al. Design trends and challenges in hydrogen direct 
injection (H2DI) internal combustion engines – A review. Int J Hydrogen Energy 
2024;86:1179 – 94 .
[12] Ampah JD, Jin C, Afrane S, et al. Race towards net zero emissions (NZE) by 2050: 
reviewing a decade of research on hydrogen-fuelled internal combustion engines 
(ICE). Green Chem 2024;26(16):9025 – 47 .
[13] Rahman MTA, Kawahara N, Tsuboi K, et al. Effect of ambient pressure on local 
concentration measurement of transient hydrogen jet in a constant-volume vessel 
using spark-induced breakdown spectroscopy. Int J Hydrogen Energy 2015;40(13): 
4717 – 25 .
[14] Deng J, Zhong H, Gong Y, et al. Studies on injection and mixing characteristics of 
high pressure hydrogen and oxygen jet in argon atmosphere. Fuel 2018;226: 
454 – 61 .
[15] Yip HL, Srna A, Liu X, et al. Visualization of hydrogen jet evolution and combustion 
under simulated direct-injection compression-ignition engine conditions. Int J 
Hydrogen Energy 2020;45(56):32562 – 78 .
[16] Lee S, Kim G, Bae C. Behavior of hydrogen hollow-cone spray depending on the 
ambient pressure. Int J Hydrogen Energy 2021;46(5):4538 – 54 .
[17] Coratella C, Tinchon A, Oung R, et al. Experimental investigation of the combined 
impact of backpressure with the pintle dynamic on the hydrogen spray exiting a 
medium pressure DI outward-opening injector. Int J Hydrogen Energy 2024;49: 
432 – 49 .
[18] Coratella C, Tinchon A, Oung R, et al. Experimental characterization of a hydrogen 
hollow cone jet at under-expanded conditions via schlieren technique. Int J 
Hydrogen Energy 2024;72:730 – 43 .
[19] Duronio F, De Vita A. CFD analysis of hydrogen and methane turbulent transitional 
under-expanded jets. Int J Heat Fluid Flow 2024;107:109381 .
[20] Hamzehloo A, Aleiferis PG. Gas dynamics and flow characteristics of highly 
turbulent under-expanded hydrogen and methane jets under various nozzle 
pressure ratios and ambient pressures. Int J Hydrogen Energy 2016;41(15): 
6544 – 66 .
[21] Zhao J, Liu W, Liu Y. Experimental investigation on the microscopic characteristics 
of underexpanded transient hydrogen jets. Int J Hydrogen Energy 2020;45(33): 
16865 – 73 .
[22] Franquet E, Perrier V, Gibout S, et al. Free under-expanded jets in a quiescent 
medium: a review. Prog Aero Sci 2015;77:25 – 53 .
[23] Nandagopal NS. Shock waves and shock wave relationships, isentropic 
(Prandtl – Meyer) expansion and Compression[M]//Compressible flow: a 
straightforward approach with practical applications including pipeline flow. 
Cham: Springer Nature Switzerland; 2025. p. 143 – 244 .
[24] Yang X, Wang X, Dong Q, et al. Experimental study on the two-phase fuel transient 
injection characteristics of the high-pressure natural gas and diesel co-direct 
injection engine. Energy 2022;243:123114 .
[25] Wu H, Silva M, Houidi MB, et al. Experimental characterization of a high-flow 
hydrogen injector with four-hole jet-forming cap. Fuel 2026;405:136619 .
[26] Dong Q, Li Y, Song E, et al. The characteristic analysis of high-pressure gas jets for 
natural gas engine based on shock wave structure. Energy Convers Manag 2017; 
149:26 – 38 .
[27] Yu J, Vuorinen V, Kaario O, et al. Characteristics of high pressure jets for direct 
injection gas engine. SAE Int J Fuels Lubr 2013;6(1):149 – 56 .
[28] Yu J, Vuorinen V, Kaario O, et al. Visualization and analysis of the characteristics 
of transitional under-expanded jets. Int J Heat Fluid Flow 2013;44:140 – 54 .
Z. Zhang et al.                                                                                                                                                                                                                                   Energy 359 (2026) 141499 
15
