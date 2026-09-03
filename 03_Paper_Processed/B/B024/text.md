<!-- PDF_PAGE: 1 -->

International Journal of Hydrogen Energy 72 (2024) 730–743
Available online 31 May 2024
0360-3199/© 2024 Hydrogen Energy Publications LLC. Published by Elsevier Ltd. All rights are reserved, including those for text and data mining, AI training, and
similar technologies.
Experimental characterization of a hydrogen hollow cone jet at 
under-expanded conditions via schlieren technique 
C. Coratella
a , *
, A. Tinchon
a
, R. Oung
a
, L. Doradoux
c
, G. Dober
b
, C. Hespel
a
, F. Foucher
a 
a
PRISME Laboratory, University of Orl ´eans, Orl ´eans, France 
b
PHINIA, Luxembourg 
c
PHINIA, France   
ARTICLE INFO  
Handling Editor: Prof. J. W. Sheffield  
Keywords: 
Hydrogen jet 
Outward-opening injector 
Under-expanded jet 
Shock wave transient 
ABSTRACT  
This study pertains to the combined action of pressure ratio with current energizing the injector coils on the 
development of the hydrogen jet exiting an outward-opening injector. Hydrogen shots are performed at the 
injection pressure of 36 bar, whilst backpressure ranges from 1.2 to 5 bar. Three current profiles are set. The 
schlieren technique is employed to visualize the jet images. Results show that, in addition to benefit the axial 
penetration and area, lower backpressures and greater currents promote the predominance of the radial 
development over the axial one but advance its decay. Decreasing backpressure shortens the shock wave tran -
sient and leads to a farther coalescence point of the waves, which are originated at the needle tip and the nozzle 
walls, from the injector. The findings provide a further insight into the hydrogen jet characterization, com -
plementing the key studies in the literature regarding gaseous jets exiting the outwardly opening nozzles.   
1. Introduction 
Over the last few decades, the ICE mobility has been subjected to an 
unprecedented world-scale growth, implying a significant increase in 
pollution levels as well as a faster depletion of fossil energy. This sce -
nario urged the research community to explore alternative solutions 
favouring the minimisation of the ICE vehicles ’ carbon footprint. A 
viable route being considered is the widespread replacement of fossil 
fuels with hydrogen. This switch retains satisfactory performances of 
existing IC engines and reduces tailpipe emissions below legislative 
targets. Several peculiarities to hydrogen combustion include:  
- great flame speed;  
- broad flammability range;  
- low ignition energy;  
- high diffusivity;  
- great octane number. 
These features are believed to facilitate hydrogen as an attractive 
solution for carbon-free mobility [ 1 – 10 ]. As a result, the automotive 
industry is directing considerable efforts to assess the feasibility of the 
hydrogen-fuelled engine from niche applications to mass market. Within 
this scope, the hydrogen jet development is known to play a crucial role 
in the H
2
/air mixing formation [ 11 – 30 ]. 
1.1. The influence of PR on the hydrogen jet penetration, area and shock 
wave transient 
The literature agrees in deeming PR as a pivotal factor dictating the 
hydrogen jet development. Several studies have indeed shown that 
higher PRs give rise to greater penetration rates and jet areas [ 11 – 22 ]. 
Within this scope, Roy et al. investigated the influence of PR on the 
hydrogen jet development via a high-speed camera [ 14 ]. The findings 
revealed that the jet structure varies significantly with the PR, increase 
in which benefits the penetration and jet area. Petersen et al. investi -
gated the hydrogen jet developing at under-expanded conditions into a 
nitrogen-filled ambiance via the Z-type and double-pass schlieren sys -
tem [ 15 ]. The increase in PR was expectedly observed to benefit the jet 
penetration. Likewise, Cheng et al. found that [ 16 ], besides boosting the 
jet penetration at the early injection stages, higher PRs than 2.5 suppress 
the jet propensity to a two-parts discrimination. Deng et al. analysed the 
combined effect of injection timing with PR on the hydrogen jet within 
an argon-filled environment [ 17 ]. A greater propensity of jet entraining 
argon was seen in response to increasing injection time, injection pres -
sure and ambient pressure. Differently, Abdul Rahman et al. [ 18 ] shifted 
the attention on the influence of backpressure on the hydrogen jet 
development. It was shown that increase in ambient pressure 
* Corresponding author. 
E-mail addresses: carlo.coratella@univ-orleans.fr (C. Coratella), fabrice.foucher@univ-orleans.fr (F. Foucher).  
Contents lists available at ScienceDirect 
International Journal of Hydrogen Energy 
journal homepage: www.else vier.com/loc ate/he 
https://doi.org/10.1016/j.ijhydene.2024.05.411 
Received 2 April 2024; Received in revised form 24 May 2024; Accepted 27 May 2024

<!-- PDF_PAGE: 2 -->

International Journal of Hydrogen Energy 72 (2024) 730–743
731
significantly affects the jet structure and exerts a curbing action on the 
jet. Lee et al. undertook a macroscopic characterization of the hollow 
cone hydrogen jet [ 19 ], showing that greater PRs result in longer axial 
penetration and larger area. Moreover, it was found that the timing of 
the jet collapse is advanced in case of high-density ambient conditions. 
Zhao et al. showed that, from the middle stage of the injection event, 
higher PRs enhance the hydrogen jet penetration exiting an outwardly 
opening nozzle [ 20 ]. Similarly, Wang et al. [ 21 ] found that the jet axial 
penetration and area are favoured by greater PRs. Regarding the shock 
wave downstream of the nozzle, literature demonstrated their impact on 
the gaseous jet development and the mixing process [ 22 – 25 ]. Prior to be 
stabilized, the shock waves were found to experience a transient 
depending on the PR [ 22 , 23 ]. Larger PRs were found to increase the 
Mach disk diameter and shock wave-to-nozzle distance [ 24 , 25 ]. 
Furthermore, higher PR were seen to determine the jet angle and the 
barrel shock structure, affecting the shock wave-originated turbulence 
to the benefit of the mixing process [ 24 , 25 ]. 
1.2. The role of the injector design on the hydrogen jet development 
Prior to the advent of the outward-opening nozzles, inward-opening 
injectors were traditionally employed. Within this trend, Ouellette et al. 
observed that the gas jets from single round nozzles are headed by a 
spherical vortex, whilst the upstream part develops in a quasi-steady 
state [ 26 ]. Fukuma et al. tested a broad selection of injectors, pro -
vided with various holes ’ number and angles of valve shroud, to inject 
hydrogen into a high swirl flow combustion chamber at an injection 
pressure of 80 bar [ 27 ]. The injector equipped with 8-holes nozzle was 
found to optimize the engine performance. Obermair et al. demonstrated 
that injector location and hole diameter exert a key role for the hydrogen 
jet development [ 28 ]. Via a numerical investigation simulating 
hydrogen shots at various SOI, delaying injection timing was revealed to 
accentuate the sensitivity of the mixing process to the nozzle geometry. 
Rogers et al. [ 29 ] demonstrated that, after a transition period, the 
hydrogen jet exiting a single hole injector is characterized by a constant 
ratio of the axial penetration to radial one. Hamzehloo et al. investigated 
the effect of the nozzle design on the hydrogen underexpanded jets 
within DI high-pressure systems using an OpenFOAM solver [ 30 ]. At 
unvaried PR, varying the nozzle design results in different jet penetra -
tion, the underexpansion level and the mass flow rate. Different mixing 
formations ensued. It is noteworthy that above studies were performed 
employing inward-opening injectors, which endow the jet shape with a 
pronounced axial morphology. By contrast, an outward-opening injector 
lends the jet a considerable radial propagation. The outward-opening 
injector is favoured for hydrogen injection, thanks to its larger nozzle 
cross-section, which is necessary to ensure adequate mass flow rates as 
required by gas engines [ 11 , 12 , 19 – 21 , 31 – 33 ]. Therefore, the design of 
the outwardly opening injectors gives rise to a radial-axial competition, 
which also depends on the injection settings. Within this scope, Zhao 
et al. showed that, from the middle stage of the injection event, higher 
PRs favour axial rather than radial penetration of the hydrogen jet 
exiting an outwardly opening nozzle [ 20 ]. Likewise, Wang et al. [ 21 ] 
found that both the axial penetration and radial propagation are fav -
oured by greater PRs. 
1.3. The proposed approach 
In spite of the extensive literature, the physical principles governing 
the hydrogen jet evolution are still a matter of debate. This has prompted 
the authors to undertake the present research. More specifically, at a 
fixed injection pressure, the study is centred on the joint action of 
backpressure and needle motion on the development of the jet, focusing 
on the axial penetration, along the injector axis, and the jet area. The 
focus is on the impact of injection scenarios on the contribution of axial 
penetration to the increase in jet area. This part of the study is believed 
to provide a further insight into the competition between axial and 
radial propagations. The influence of the injection settings on the shock 
wave transient is also examined. The jet images are captured and pro -
cessed via the schlieren technique and an in-house implemented MAT -
LAB code, respectively. The paper is outlined as follows. Section 2 
describes the experimental setup and methodology. Section 3 pertains to 
the experimental tests and analysis of the emerged findings. Conclusions 
are summarized in Section 4 . 
2. The experimental apparatus 
A sketch of the experimental apparatus, which enables hydrogen 
shots over a broad range of injection scenarios, is shown in Fig. 1 . 
A detailed description of the experimental setup and image pro -
cessing is provided by the following subsections. 
2.1. DI-CHG injector 
The injections were performed by means of a PHINIA-designed and 
manufactured DI-CHG 6 type injector, operating at medium pressure 
and able to supply a mass flow rate of 6 g/s at an injection pressure of 36 
bar [ 11 , 12 ] ( Fig. 2 ). 
The solenoid-driven injector is characterized by an outward-opening 
nozzle, provided with a conical seat producing a hollow cone jet in the 
Nomenclature 
A
JET 
jet area 
CNG compressed natural gas 
CVC constant volume chamber 
DI direct injection 
Ma Mach number 
p hydrogen pressure 
P
BACK 
backpressure 
PL
AXIAL 
axial penetration length 
PL
RADIAL
radial penetration length 
PR pressure ratio 
r radius of curvature 
u gas velocity 
WF current waveform 
Greek symbols 
ρ gas density 
χ coefficient of proportionality  
Fig. 1. Test rig: 1 – N
2 
bottle; 2 – H
2 
bottle; 3 – N
2 
pressure regulating valve; 4 – 
N
2 
storage; 5 – H
2 
pressure regulating valve; 6 – Pressurised H
2 
rail; 7 – H
2 
injector; 8 – Synchroniser; 9 – Plane mirror; 10 – Pin hole; 11 – High-speed 
camera; 12 – First concave mirror; 13 – Computer; 14 – CVC; 15 – Second 
concave mirror; 16 – LED emitter. 
C. Coratella et al.

<!-- PDF_PAGE: 3 -->

International Journal of Hydrogen Energy 72 (2024) 730–743
732
near nozzle region. At fully injector opening, the needle displacement is 
0.36 mm. Being as the outward-opening nozzle is characterized by a 
higher cross section, it supplies a higher mass flow rate if compared to 
inward-opening injector [ 11 , 12 , 19 – 21 , 31 , 32 ]. The injector was posi -
tioned obliquely at an angle of 45
◦
with respect to the vertical axis 
through the centre of the CVC seen from the front view. Additionally, 
since the combined impact of the PR with the current waveform on the 
hydrogen jet development is the object of interest of the present study, a 
schematization of the time-history of the current-driven needle motion 
is provided ( Fig. 3 ). 
WF1 is the waveform provided with the highest current intensity, 
yielding the fastest needle descent. In contrast, WF3 waveform is char -
acterized by the lowest current. A rising stage, slope of which is indic -
ative of the needle speed, is followed by a stable phase, indicating the 
full injector opening. The injector opening is thereby dictated by the 
current waveform delivered to the injector coils. Therefore, at unvaried 
PR, the injector solenoid energization is expected to dictate the jet 
development. 
2.2. The CVC 
Hydrogen was injected into a quiescent nitrogen-filled CVC. The 
choice of the nitrogen was motivated by its inert nature, which prevents 
hydrogen from igniting, ensuring the safety of the experiments [ 7 , 10 , 
12 – 14 , 19 – 24 , 34 – 36 ]. Besides, the nitrogen molecular weight is close to 
that of air. Thus, large errors, when calculating the mass of ambient gas 
in the jet, are appreciably minimized [ 20 ]. The CVC is provided with two 
quartz windows of 100-mm diameters enabling the optical access to the 
jet. The ambient temperature was 20 
◦
C. The CVC, which can be heated 
up to 180 
◦
C by means of wall heating resistances, allows the nitrogen to 
be stored at a maximum pressure of 30 bar. A Labview-coded PID 
regulator was used to control the chamber walls temperature. 
2.3. Imaging set-up 
The jet images were captured by means of the Z-type Schlieren 
method, which is based upon the variation in the refractive index 
stemming from the density gradient arisen between hydrogen and ni -
trogen. A high-power monochromatic LED source, placed beside the 
CVC, was used to illuminate the jet. As the light beam is emitted by the 
LED, it is reflected by a concave mirror, and travels across the CVC. Once 
the light beam crosses the jet, it is subjected to a deflection. Then, a 
second concave mirror reflects the light beam. The light beam is further 
reflected by a plane mirror. Afterwards, the light beam is detected by a 
Photron-manufactured FastcamSA5 high-speed camera. The camera 
speed was set at 10,000 fps at a resolution of 640 x 640 pixels, with a 
spatial resolution of 0.170 mm/pixel. 
2.4. Image processing 
Once the jet development was captured by the camera, the images 
were processed via an in-house developed MATLAB script. Fig. 4 illus -
trates the steps of the MATLAB code. The initial removal of the back -
ground is followed by the subtraction from the raw images, highlighting 
the jet. For each condition, the ten repetitions are used to create a mean 
jet image for each time step, using a physic-based threshold to denoise 
the images. 
The mean and raw images are then binarized and the boundary of the 
jet is generated using the Canny method ( Fig. 5 ). The jet area within the 
boundary is defined as the cross-sectional area of the jet, whilst the axial 
penetration is given by the distance between the nozzle and the jet tip. 
A user-defined threshold is then set to detect the jet tip, namely the 
last pixel whose intensity is superior to the threshold. Afterwards, the 
image presents a satisfactory clearness. 
Fig. 2. The Phinia-manufactured DI-CHG6 injector.  
Fig. 3. The schematization of the time-history of the current-driven nee -
dle motion. 
C. Coratella et al.

<!-- PDF_PAGE: 4 -->

International Journal of Hydrogen Energy 72 (2024) 730–743
733
2.5. Tests conditions 
The tests were performed at various injection scenarios. Table 1 lists 
the injection settings and hydrogen properties [ 2 , 16 ], respectively. The 
injection settings led to state that hydrogen shots are characterized by 
highly under-expanded jets [ 34 ]. The needle lift profile was controlled 
using three different current profiles, for a total of 9 injection scenarios. 
The energizing time was set at 3 ms. 
WF1 is the profile giving the fastest needle displacement. In order to 
comply with PHINIA confidential policy, the authors are not authorized 
to disclose any details of the current waveforms energizing the injector 
coils or the actual needle speed. 
3. Results and discussion 
In order to provide a further contribution to the understanding of the 
physical principles governing the hydrogen jet development, an exper -
imental campaign was conducted focusing on the combined impact of 
ambient pressure and current profile on:  
- jet axial propagation;  
- jet area development;  
- the contribution of jet axial development to the increase in jet area;  
- shock wave development. 
The analysis of above factors is prompted by the literature, which 
agrees in deeming the jet area, axial penetration and shock waves 
Fig. 4. Image processing steps (P
INJ 
= 36 bar, P
BACK 
= 5 bar, WF1).  
C. Coratella et al.

<!-- PDF_PAGE: 5 -->

International Journal of Hydrogen Energy 72 (2024) 730–743
734
characteristics as key factors affecting the mixture process within DI 
engines [ 12 , 20 – 25 , 29 , 32 , 33 , 37 ]. 
3.1. Time-history of jet axial penetration 
Fig. 6 illustrates the time-history of the jet axial penetration averaged 
over ten consecutive shots for each of the 9 settings. The axial pene -
tration was determined through the number of pixels between the 
longest distance covered by the jet along the injector axis and the nozzle 
outlet. Given the windows 100-mm diameter, penetration is assessed till 
the jet covers said distance. 
Fig. 5. – The evolution of the jet boundary defined by the Canny method (P
INJ 
= 36 bar, P
BACK 
= 5 bar, WF3, time step = 0.1 ms).  
Table 1 
Injection settings during the tests.  
Injection pressure (bar)  36  
Temperature (
◦
C)  20  
H
2 
Density (kg/m
3
)  ≈ 2.876  
H
2
Viscosity ( μ Pa ⋅ s)  ≈ 8.875  
P
BACK 
(bar) 1.2 3 5 
PR 30 12 7.2 
N
2 
density (kg/m
3
) [ 11 , 21 ] ≈ 1.15 ≈ 2.5 ≈ 5.2 
Current Waveforms WF1, WF2, WF3  
Fig. 6. The jet penetration lengths averaged over ten shots for each current profile and at backpressures of 1.2 bar (a), 3 bar (b) and 5 bar (c).  
C. Coratella et al.

<!-- PDF_PAGE: 6 -->

International Journal of Hydrogen Energy 72 (2024) 730–743
735
As expected, with the same current waveform, the PL
AXIAL 
curves are 
characterized by steeper slopes, indicating higher jet velocities, as a 
result of lower backpressures. It is worthy of attention that, at back -
pressures of 1.2 and 3 bar, WF1 yields the fastest PL
AXIAL
, whilst the WF3 
generates the slowest PL
AXIAL
s. On the other hand, at a backpressure of 5 
bar, the PL
AXIAL 
developments exhibit an insensitive behaviour to the 
currents. Particularly, at backpressure of 1.2 bar, WF1, WF2 and WF3 
engender a PL
AXIAL 
of 93.531 mm, 91.084 mm and 93.531 mm, 
respectively, within 1 ms. Regarding the shots at backpressure of 3 bar, 
WF1, WF2 and WF3 yield a PL
AXIAL 
of 84.965 mm, 84.790 mm and 
90.035 mm, respectively. Concerning the timings of the maximum 
PL
AXIAL
, the WF1 and WF2-produced jets cover the maximum PL
AXIAL 
within 1.4 ms, whilst the WF3-generated jet reaches the maximum 
PL
AXIAL 
at 1.5 ms. For what concerns the injections carried out at 
backpressure of 5 bar, WF1, WF2 and WF3 produce a PL
AXIAL 
of 89.510 
mm, 88.462 mm and 91.608 mm, respectively. With regard to the tim -
ings, the WF1 and WF2-related jets reach the maximum PL
AXIAL 
within 
2.1 ms and 2.2 ms respectively. The WF3-generated jet reaches the 
maximum PL
AXIAL 
at 2.1 ms. The following subsections provide an 
explanation of the results. 
3.1.1. The hypothesis of a needle-driven rarefaction wave boosting the 
hydrogen flow 
The WF1-produced PL
AXIAL
, exhibiting the fastest development at 
backpressures of 1.2 and 3 bar, may be ascribed to the needle-induced 
rarefaction arisen adjacently the needle surface [ 11 ]. The needle 
displacement is indeed presumed to generate a rarefaction wave, which 
promotes the gas momentum, to the advantage of jet penetration. 
Accordingly, a faster needle displacement is supposed to enhance the 
magnitude of the rarefaction wave and a longer PL
AXIAL 
ensues. How -
ever, at a backpressure of 5 bar, the time histories of the PL
AXIAL 
are 
insensitive to current intensities, showing a disagreement with the 
above physical interpretation. This finding may be explained by the 
needle speed, which is at least two orders of magnitude less than gas 
velocity. Therefore, the change of needle speed within certain ranges 
may be thereby irrelevant to the initial jet formation. 
3.1.2. The influence of the backpressure on the impact of current on the 
needle descent 
The 5-bar case leads to conceive that increasing backpressure tends 
to soften the impact of the current on the needle descent. This outcome 
can be ascribed to the higher backpressure, which is assumed to suppress 
the influence of the current profile on the needle displacement. 
Increasing backpressure is indeed presumed to slow the needle down, 
counteracting more strongly the effect of the currents on the needle 
descent. The impact of the currents on the needle descent thereby tends 
to be negligible at increasing backpressures. Therefore, the rarefaction 
wave may be impactful on the jet development solely following to 
considerable reduction in backpressure. Accordingly, at much higher 
backpressures, the PL
AXIAL 
development may not be explainable taking 
the currents into account. 
3.2. The development of the jet area 
Fig. 7 depicts the evolution of the jet area averaged over ten shots for 
each backpressure and current profile. The area development is analysed 
within the interval during which the jet reaches the longest detectable 
PL
AXIAL
. 
The curves are characterized by an uptrend. A consistency with the 
outcomes referring to the PL
AXIAL 
developments emerges. In fact, the 
slowest A
JET
s arise from the WF3 in all cases. Moreover, the WF1- 
produced A
JET 
exhibits a slightly faster evolution compared to the rest 
of current waveforms. However, regarding the backpressure of 1.2 bar, a 
slight decrease in A
JET 
is noted at timing of around 0.84 ms. It can be 
noticed also that, at the same ambient pressure, a slower needle 
displacement, stemming from a weaker current waveform, leads to 
slower area development. Likewise, increasing the ambient pressure 
curbs the jet area development. For an accurate assessment of the impact 
of backpressure and current waveform on the A
JET 
development, the 
following subsections describe the results and explain of the physical 
Fig. 7. – The time histories of jet areas averaged over ten injections for each current profile and at backpressures of 1.2 bar (a), 3 bar (b) and 5 bar (c).  
C. Coratella et al.

<!-- PDF_PAGE: 7 -->

International Journal of Hydrogen Energy 72 (2024) 730–743
736
principles underlying the merged findings. 
3.2.1. The joint impact of backpressure with current waveform on the jet 
area development 
An initial uptrend of A
JET 
is observed for each injection case. During 
this stage, the mass flow rate increases, due to the increase in cross 
sectional area at the nozzle, enabling the jet to cover larger areas. 
However, at a backpressure of 1.2 bar, a slowdown in A
JET 
development 
at 0.84 ms. This might be owed to lower backpressure promoting the jet 
overdispersion [19]. A decrease in local jet density, captured by the 
schlieren device, ensues. Consequently, the gradient of the refractive 
index diminishes [19], leading to a smaller detected A
JET
. Table 2 shows 
the largest areas detected within the time required by the PL
AXIAL 
to 
cover a 100 mm distance, namely the diameter of the CVC window. 
At constant ambient pressure and slower needle displacements, a 
lower A
JET,MAX 
is seen, indicating a narrower jet. As aforementioned, 
lower needle speeds are supposed to weaken the rarefaction wave. The 
drawing action on the hydrogen flow is thereby mitigated, causing a 
slower jet development. Thus, a decreasing trend of the A
JET,MAX 
arises. 
Additionally, larger backpressures augment the A
JET,MAX
, despite their 
slower development. It is also noteworthy that, as shown by Table 3, 
greater backpressure extends the time required to cover the maximum 
area. 
Lower ambient pressure favours the jet penetration. On the other 
hand, greater jet velocities promote the shear stress. Thus, the timing at 
which the jet experiences high shear stress is advanced. Due to faster jet, 
the jet area develops more rapidly, reaching its highest value earlier if 
compared to slower jets. However, since shear stress is promoted by high 
jet velocities, the jet tends to collapse earlier. As a result, the maximum 
area is smaller with respect to slower jets’ ones. In contrast, at higher 
ambient pressures, lower jet velocities are assumed to delay the timing 
of outweighing shear stress. Lower penetration rate of the jet reduces the 
interaction of the jet with the ambient gas [11,16,21,31,37]. Conse -
quently, the ambient gas entrainment occurs at a reduced rate but over a 
longer period. This leads to a larger A
JET,MAX
. For the sake of exhaus -
tiveness, Table 4 lists the medium A
JET 
propagation rate, given by the 
ratio of highest A
JET 
over the related timing, at the injection scenarios 
set in this study. 
It emerges that, at unvaried backpressure, weakening the current 
waveform slows the A
JET 
development down. Similarly, once the current 
waveform is set, increasing backpressure curbs the A
JET 
propagation 
rate, to the detriment of the jet diffusivity. For a more thorough inves -
tigation of the joint effect of PR with the current waveform on the A
JET 
development, Tables 5 and 6 list the variation in A
JET 
propagation rates 
ensuing from the increase in backpressure and weakening the current 
waveform. 
In the light of the above tables, it can be inferred that, in most cases, 
the reductions in A
JET 
diffusion, arisen from the increase in back -
pressure, is larger than ones ascribed to the weakening waveform. This 
conclusion shows agreement with the hypothesis regarding the 
influence of higher backpressure, which is presumed to prevail over the 
action of the current profile, on the needle displacement. Accordingly, as 
above mentioned, the current dictates the needle displacement less 
significantly at increasing backpressures. The magnitude of the needle- 
induced rarefaction wave is thus weaker if generated by an increase in 
backpressure, and a slower A
JET 
development ensues. 
3.2.2. The action of higher backpressure on the jet diffusivity 
The above findings can also be explained by the Chapman-Enskog 
theory [38], which states that the gas diffusivity is inversely propor -
tional to ambient pressure. Accordingly, once the current is fixed, 
greater ambiance pressure reduces the gas diffusivity, curbing the jet 
area development. It is worth noting that this physical interpretation 
agrees with the literature. In fact, Lee et al. demonstrated that the mo -
mentum exchange of a hollow cone jet takes place on the outer and inner 
jet surfaces [19]. A decrease in pressure, stemming from the flow mo -
tion, occurs on both jet surfaces. However, a pressure recover is not 
noticed in the inner section, whilst the pressure drop at the outer surface 
is compensated by the high volume of ambient gas. As a result, a pres -
sure gradient arises through the surfaces, causing a jet shrinkage. This 
phenomenon, meaningful of a slower A
JET 
development, is accentuated 
at higher backpressure [19]. Concerning the reduction in charts’ slope, 
observed at unvaried ambient pressure and slower needle motion, it may 
be attributed to the above weaker rarefaction wave. A slower hydrogen 
flow ensues, slowing the A
JET 
development down. 
3.2.3. The analysis of the A
JET 
development as a function of PL
AXIAL 
Fig. 8 shows the A
JET 
development plotted against the PL
AXIAL
. The 
slope of chart is significant of the jet radial propagation. 
An upward trend in, characterized by changing slopes, is observed, 
indicating a variable contribution of PL
RADIAL 
to the A
JET
. Increasing 
backpressure leads to lower slopes in most of the cases, indicating a 
slower macroscopic radial development of the jet shape. Similarly, at 
unchanged ambient pressure, the WF3 current waveform lowers the 
chart slopes, indicating a softened radial propagation. 
More specifically, as regard the 1.2-bar case, the WF1 waveform 
yields a chart reaching the A
JET,MAX 
of 2267.531 mm
2 
when the PL
AXIAL 
is 83.042 mm. The WF2 and WF3 waveforms generate a A
JET,MAX 
of 
2167.557 mm
2 
and 1835.878 mm
2 
at PL
AXIAL
s of 82.168 mm and 
82.343 mm, respectively. As concerns the 3-bar case, a A
JET,MAX 
of 
2954.912 mm
2 
is generated by the WF1 waveform, when the PL
AXIAL 
is 
84.965 mm. When the WF2 and WF3 waveforms are set, the charts reach 
Table 2 
The detected highest A
JET 
(in mm
2
).  
P
BACK 
(bar) WF1 WF2 WF3 
1.2 2267.531 2167.557 1835.878 
3 2954.912 2839.687 2839.319 
5 3659.81 3554.208 3137.317  
Table 3 
The timings (in ms) of the maximum detectable A
JET
.  
P
BACK 
(bar) WF1 WF2 WF3 
1.2 0.9 0.9 0.9 
3 1.4 1.4 1.4 
5 2 2.2 2  
Table 4 
The medium A
JET 
propagation rates (in m
2
/s).  
P
BACK 
(bar) WF1 WF2 WF3 
1.2 2.519 2.408 2.040 
3 2.111 2.028 2.028 
5 1.830 1.616 1.569  
Table 5 
The reduction in A
JET 
propagation rate (in m
2
/s), caused by increasing P
BACK
, at 
unvaried waveform.  
P
BACK 
(bar) WF1 WF2 WF3 
1.2 → 3 0.408 0.38 0.012 
3 → 5 0.306 0.412 0.459  
Table 6 
The reduction in A
JET 
propagation rate (in m
2
/s), caused by weakening wave -
form, at unvaried P
BACK
.  
P
BACK 
(bar) WF1 → WF2 WF2 → WF3 
1.2 0.111 0.368 
3 0.083 0 
5 0.189 0.047  
C. Coratella et al.

<!-- PDF_PAGE: 8 -->

International Journal of Hydrogen Energy 72 (2024) 730–743
737
A
JET,MAX 
values of 2839.687 mm
2 
and 2839.319 mm
2
, respectively, 
whilst the corresponding PL
AXIAL
s are 83.741 mm. For what concerns the 
backpressure of 5 bar, the WF1-related charts reaches the A
JET,MAX 
value 
of 3659.81 mm
2 
at 85.839 mm of PL
AXIAL
. An A
JET,MAX 
of 3554.208 
mm
2
, at a PL
AXIAL 
of 88.462 mm, is reached by the WF2-generated chart. 
Differently, the WF3 waveforms produces a chart reaching the A
JET,MAX 
of 3137.317 mm
2 
at a PL
AXIAL 
of 91.608 mm. The analysis of the slope of 
the A
JET
-PL
AXIAL 
chart is believed to provide a more thorough assess -
ment of the jet development, setting the stage for the following intro -
duction of the χ factor. 
3.3. The impact of jet axial penetration on the increase in jet area 
In order to provide an in-depth assessment of the hydrogen jet, the χ 
factor, standing for the ratio of the increase in jet area divided by the 
increase in the axial penetration, is introduced. The χ factor is given by: 
χ ( t ) =
Δ A
JET
( t )
Δ PL
AXIAL
( t )
(1) 
and is calculated every 0.1 ms. Therefore, as sketched in the Fig. 9 , a 
greater χ indicates a more boosting impact of a 1 mm increase in the 
PL
AXIAL 
on the A
JET 
augmentation. 
The analysis of the effect of injection settings on the χ parameter is 
based on the subdivision of the jet body into layers orthogonal to the 
injector axis and provided with a height equal to the variation of the 
PL
AXIAL 
occurring every 0.1 ms. Moreover, as variations both in PL
AXIAL 
and in PL
RADIAL 
contribute to the increase in A
JET
, χ is presumed to 
describe the variation in PL
RADIAL
. The following mathematical pro -
cedure underlies this assumption. 
χ ( t ) =
δ A
JET
( t )
δ PL
AXIAL
( t )
∼
PL
RADIAL
( t ) • δ PL
AXIAL
( t ) + PL
AXIAL
( t ) • δ PL
RADIAL
( t )
δ PL
AXIAL
( t )
= PL
RADIAL
( t ) + PL
AXIAL
( t ) •
δ PL
RADIAL
( t )
δ PL
AXIAL
( t )
(2) 
Applying the time derivative of the χ parameter results in:   
Accordingly, a greater variation in χ factor, indicated by a steeper 
slope of χ chart, is meaningful of a larger increase in PL
RADIAL
. 
3.3.1. The reasons motivating the introduction of the χ factor 
The introduction of χ parameter is motivated by the jet asymmetric 
development with respect to injector axis [ 20 , 21 , 25 , 32 , 34 , 39 ]. More -
over, the jet asymmetry has been proven to vary with injection settings 
Fig. 8. The development of A
JET 
as a function of PL
AXIAL 
for each current profile and at backpressures of 1.2 bar (a), 3 bar (b) and 5 bar (c).  
δ χ ( t )
δ t
= δ PL
RADIAL
( t ) + δ PL
AXIAL
( t ) •
δ PL
RADIAL
( t )
δ PL
AXIAL
( t )
+ PL
AXIAL
( t ) •
[
δ
2
PL
RADIAL
( t ) • δ PL
AXIAL
( t )  δ
2
PL
AXIAL
( t ) • δ PL
RADIAL
( t )
( δ PL
AXIAL
( t ))
2
]
δ χ ( t )
δ t
∼ 2 • ( δ PL
RADIAL
( t ) + PL
AXIAL
( t ) • o

t
2
)
δ χ ( t )
δ t
∼ δ PL
RADIAL
( t )
(3)   
C. Coratella et al.

<!-- PDF_PAGE: 9 -->

International Journal of Hydrogen Energy 72 (2024) 730–743
738
[ 20 , 21 , 34 ]. It is worthy of attention that the subdivision of the jet body 
into layers orthogonal to the injector axis is commonly used to minimize 
the asymmetry-induced error in the assessment of the jet spatial distri -
bution, allowing a more accurate analysis of parameters unevenly 
developing along the radial direction [ 20 , 32 , 35 , 39 , 40 ]. 
This approach was employed by Tsujimura et al. for the analysis of 
the jet dispersion angle [ 25 ]. More specifically, the jet body was strat -
ified into discs, the heights of which were given by one pixel, at each 
detected jet PL
AXIAL
. Ni et al. used this approach for the 
fluorescence-based calculation of the gas concentration within a CNG jet 
[ 39 ]. Since the jet structure on both sides presented an asymmetry with 
respect to the injector axis, the jet was divided into discs with a 
single-pixel height. The jet was thus stratified into pixel scale along the 
injector axis and each layer was analysed. The calculation of the disc 
fluorescence was shown to diminish the errors due to the jet asymmetry. 
Likewise, Zhao et al. employed such a method to calculate the spatial 
distribution of hydrogen concentration within the jet exiting an 
outward-opening injector [ 20 ]. Therefore, a similarity between the 
above studies and the methodology here applied emerges. 
The introduction of χ factor is also justified by the various ap -
proaches devoted to the estimation of the jet angle, which is a parameter 
describing the jet spatial distribution [ 31 ]. Sankesh et al. [ 32 ] proposed 
the centroid method for determining the spread angle of an 
outward-opening nozzle, whilst Erfan et al. [ 41 ] defined the jet angle 
between the injector axis and the maximum distance of the edge of the 
jet exiting an inward-opening injector. Additionally, Lee et al. employed 
an equation for the calculation of the hollow cone jet angle [ 19 ]. This 
disagreement led Zhao et al. [ 31 ], who employed both methodologies in 
the jet angle acquisition, to observe large differences in the results. 
Accordingly, considering:  
- the jet asymmetry with respect to injector axis and its variability with 
injection settings,  
- that the jet subdivision into layers minimises the asymmetry-induced 
errors,  
- the discrepancy between the methodologies aiming at angle 
estimation,  
- that PL
AXIAL
, PL
RADIAL 
and A
JET 
lie within the set of parameters which 
best describe the jet exiting an outward-opening nozzle [ 32 ],  
- that the physical principles governing the jet exiting this type of 
injector are still unclear, 
the investigation of the χ parameter is believed to supplement the 
noteworthy studies which are milestones in the characterization of the 
hollow cone jet [ 19 – 21 , 31 , 32 , 37 ]. Although not providing the temporal 
evolution of the PL
RADIAL
, the χ parameter is assumed to describe its 
competition with the PL
AXIAL 
in contributing to the A
JET 
increase and 
determining the jet collapse timing. 
3.3.2. The temporal evolution of χ parameter 
Fig. 10 shows the time-history of χ parameter as a function of current 
waveform at constant backpressure. 
A rising stage is noticed for each injection case, indicating that a 
small increase in PL
AXIAL 
suffices to engender an appreciable increase in 
A
JET
. Accordingly, the radial propagation is supposed to amplify the 
effect of an albeit small variation in PL
AXIAL 
on the increase in A
JET
. It is 
also noteworthy that, at constant backpressure, the χ curve steepens in 
response to stronger currents. Additionally, the χ development is char -
acterized by a maximum value, which is meaningful of the greatest in -
crease in A
JET 
produced by a 1 mm increase in PL
AXIAL 
over the whole 
Fig. 10. The development of χ parameter at for each current profile and at backpressures of 1.2 bar (a), 3 bar (b) and 5 bar (c).  
Fig. 9. Larger χ is meaningful of an increase in PL
AXIAL 
sufficing to generate a 
larger variation in A
JET
. 
C. Coratella et al.

<!-- PDF_PAGE: 10 -->

International Journal of Hydrogen Energy 72 (2024) 730–743
739
injection event. This leads to argue that, at the χ
MAX
, the radial devel -
opment contributes to the increase in A
JET 
more appreciably with 
respect to the whole injection process. Particularly, regarding 1.2-bar 
case, the WF1 waveform produce a χ
MAX 
of 49.455 mm within 0.4 ms, 
whilst the WF2-generated shot yields a χ
MAX 
of 45.515 mm at 0.5 ms 
after the start of the injection. As the WF3 waveform is set, the χ factor 
reaches its maximum at 41.696 within 0.5 ms. Concerning the 3-bar 
case, as the WF1 waveform is set, the χ curve is seen to reach a 
maximum value of 46.839 mm after 0.4 ms. The WF2-generated shot 
yields a χ
MAX 
of 44.957 mm at a timing of 0.5 ms, whilst the WF3 
waveform is seen to generate a χ curve reaching a maximum value of 
46.226 mm within 0.6 ms. For what concerns the backpressure of 5 bar, 
WF1, WF2 and WF3 produce a χ
MAX 
of 54.312 mm, 55.565 mm, and 
47.606 mm, respectively. With regard to the timings, the WF1 and WF2- 
related χ
MAX 
are reached 0.5 ms and 0.8 ms, whilst the WF3 case jet at 
1.7 ms. In order to provide a thorough analysis of the joint impact of 
backpressure with current waveform on the χ temporal development, 
Table 7 lists the above χ
MAX
s and their timings. 
At a fixed current, greater backpressure leads to χ
MAX 
uptrend. 
Additionally, the χ
MAX 
values are reached less rapidly. Following to the 
χ
MAX 
timing, a decay is shown by 1.2-bar and 3-cases. However, this 
latter case shows a less pronounced decaying phase compared to back -
pressure of 1.2 bar. By contrast, backpressure of 5 bar does not exhibit 
the descending trend. Moreover, from Tables 7 and it emerges that an 
earlier radial decay, significant of restrained radial propagation, results 
from stronger currents or reduction in backpressure. A narrower jet, 
meaningful of a commencing axial predominance, ensues. The following 
subsections provide a detailed description and explanation of the 
outcomes. 
3.3.3. The influence of waveform on the on the contribution of axial 
penetration to the jet area 
Bearing in mind that design of an outward-opening nozzle benefits 
the radial penetration at the early injection phases [20,21,31,32], the 
ascending stage is significant of the radial propagation prevailing over 
the axial one. At the initial injection phases, the jet morphology is thus 
given by a conical shape provided with a constantly rising profile. 
Moreover, at constant backpressure, the χ curve steepens in response to 
stronger currents. This finding is owed to the above needle-driven 
rarefaction wave, magnitude of which is higher in case of faster nee -
dle displacements. A faster gas flow ensues, benefiting the effect of an 
outwardly opening nozzle on radial propagation [20,21,31,32]. There -
fore, the radial predominance is more appreciable in case of greater 
currents. Thus, the shorter time required for the χ
MAX 
is attributable to 
the combined action of the nozzle design of outward opening injector 
with lower current intensity. On the other hand, an earlier radial decay 
results from stronger currents. In fact, if on one hand the radial promi -
nence is accentuated at lower current intensities, on the other hand it is 
less durable. This finding can be owed to the fact that, since the radial 
predominance over axial development is enhanced at stronger wave -
forms, the onset of considerable shear stresses the along radial direction 
is advanced. Hence, the timing of the χ trend reversal, significant of 
commencing larger contribution of PL
AXIAL 
to A
JET
, is advanced. This 
leads to lower χ
MAX
, but reachable within shorter timings. Table 7 also 
shows that, at unvaried ambiance pressure, weakening current intensity 
prolongs the χ
MAX 
timing. This finding can be owed to the physical 
principles underlying the sensitivity of χ to backpressure. Higher 
backpressure and weaker current indeed lower the curves’ slope. It is 
presumable that higher backpressures and weaker currents mitigate the 
radial predominance and prolong its duration. A delayed reversal of χ 
trend, meaningful of retarded radial decay, ensues. 
3.3.4. The action of backpressure on the on the contribution of axial 
penetration to the jet area 
Fig. 11 plots the χ time-history as a function of backpressure for each 
current profile, so as to highlight the impact of backpressure at unvaried 
current waveform. 
A quantitative analysis of the charts can be carried out taking the 
above Table 7 into consideration. In fact, once the current is set, the 
increase in backpressure slows the χ development down till the timing of 
the χ
MAX 
relative to the backpressures of 1.2 and 3 bar, indicating a 
slower and prolonged radial growth of the jet width. Conversely, lower 
backpressures accentuate the radial predominance but shortens its 
duration, which ends at χ
MAX 
timing. These findings might be ascribed to 
the design of the outwardly opening injector, which lends the jet shape 
an initial radial prominence [20,21,31,32]. 
This outcome agrees with Lee’s study, which demonstrated that 
higher backpressures accentuate the jet shrinkage [19]. Furthermore, 
Lee’s research highlighted that higher backpressures contribute to the 
jet centroid moving toward the injector axis, to the detriment of radial 
propagation. Hence, as the jet shrinkage is meaningful of an out -
weighing axial propagation, the provided interpretations fall within the 
literature. 
At χ
MAX
, the radial predominance is more pronounced with respect to 
whole injection process. Afterwards, a decreasing trend of χ , significant 
of the starting radial decay, occurs. At a backpressure of 1.2 bar, an 
earlier radial decay is noticed. If on one hand lower ambient pressure 
boosts the jet velocity, on the other hand it advances the timing of shear 
stress curbing the radial penetration. An earlier decreasing χ trend en -
sues. For the sake of clarity, Table 8 synthesizes the above 
considerations. 
To summarize, employing an outward-opening injector and at un -
varied current waveform, lower backpressures promote the axial and 
radial penetration lengths, but favouring the radial development at the 
initial injection stages. On the other hand, decreasing backpressure 
shortens the duration of the radial predominance. 
3.3.5. The consistency of the physical interpretation of χ parameter with the 
literature 
It is noteworthy that the physical interpretation of χ time-history 
agrees with the literature pertinent to the jets exiting an outward 
opening injector. Several studies demonstrated that, at commencing 
injection, radial penetration is longer than axial one [20,21,31,32]. 
More specifically, in some research activities, radial propagation pre -
vails over the axial one during the entire injection event [32], whilst 
other works showed that the radial predominance ends at a timing 
depending on PR [20,21,31]. This disagreement leads to conclude that 
the competition between radial and axial penetrations is dictated also by 
the design of the outward-opening injector. In fact, likewise to the 
inward-opening injectors, the design of an outward-opening injector is 
characterized by several variables such as the diameter, needle 
displacement, cone angle, seat geometry etc., which determine the jet 
morphology [32]. Glossing over this discrepancy, the χ uptrend can be 
associated with the radial predominance revealed by above studies [20, 
21,31]. The reliability of the assessment of the χ time-history can be 
proven also by the consistency with the studies demonstrating that, at 
unvaried injection pressure, higher backpressure diminishes the jet 
angle and retards the timing of its maximum value [20,21,31,32]. These 
findings are associable with the lower χ and the retarded χ
MAX 
timing 
owed to the decreasing PR. Bearing in mind that an outward opening 
injector endows the jet with a pronounced radial propagation, 
decreasing backpressure indeed incentivizes the radial development. 
Larger angles ensue. On the other hand, greater jet radial velocities 
Table 7 
The χ
MAX 
values and related timings (in ms).   
WF1 WF2 WF3 
P
BACK 
(bar) χ
MAX 
t
χ ,max 
χ
MAX 
t
χ ,max 
χ
MAX 
t
χ ,max 
1.2 49.46 0.4 45.52 0.5 41.70 0.5 
3 46.84 0.4 44.96 0.5 46.27 0.6 
5 54.31 0.5 55.78 0.9 47.61 1.7  
C. Coratella et al.

<!-- PDF_PAGE: 11 -->

International Journal of Hydrogen Energy 72 (2024) 730–743
740
advance the timing of shear stress curbing the radial penetration. The 
radial predominance tends to decay, to the advantage of the axial 
penetration. An advanced jet angle shrinkage and an earlier onset of the 
χ downtrend arise. Analogous conclusions can be drawn from the earlier 
timing of the maximum jet angle at greater currents. Therefore, the χ 
factor, although not comparable to a deterministically acquired 
parameter, is deemed to reliably describe the radial development, sup -
plementing the findings of key studies which represent landmarks in the 
characterization of the hollow cone jet [ 19 – 21 , 31 , 32 , 37 ]. 
4. The investigation of shock wave transient 
Fig. 12 illustrates charts plotting the time-history of the position of 
the normal shock wave with respect to the needle tip. At 5 bar of 
backpressure, normal shock waves were not clearly discerned, in 
agreement with the literature remarking that higher PRs make the shock 
structures more observable [ 13 , 15 , 23 , 24 ]. 
The charts evidence that shock wave-to-needle distance is subjected 
to a transient, which is meaningful of the needle descent and its dura -
tion. The following subsections describe the results and provide an 
explanation of the merged findings. 
4.1. The stabilization of the shock wave-to-needle distance depending on 
the backpressure and the current waveform 
Regarding the injections performed at 1.2 bar of backpressure, the 
WF1 waveform is observed to yield a shock wave stabilization at 1.426 
mm from the needle tip, whilst the WF2 and WF3 waveforms generate 
distances of 1.235 mm and 1.163 mm, respectively. It is also noteworthy 
Fig. 11. The development of χ as a function of backpressure at the WF1 (a), WF2(b) and WF3(c) current waveforms.  
Table 8 
The variation in jet characteristics depending on the χ timing.  
t < t χ
MAX 
t > t χ
MAX 
Δ PL
AXIAL 
> 0 Δ PL
AXIAL 
> 0 
Δ PL
RADIAL 
> 0 Δ PL
RADIAL 
< 0 
PL
RADIAL 
> PL
AXIAL 
PL
AXIAL 
> PL
RADIAL 
Δ A
JET 
> 0 Δ A
JET >
0  
Fig. 12. The evolution of the needle-shock wave distance for each current profile and at backpressures of 1.2 bar (a) and 3 bar (b).  
C. Coratella et al.

<!-- PDF_PAGE: 12 -->

International Journal of Hydrogen Energy 72 (2024) 730–743
741
that the timing of distance stabilization, which is meaningful of full 
injector opening, tends to be shorter in case of stronger current intensity. 
Indeed, when WF1 and WF2 waveforms are set, the shock waves stabi -
lize at a timing of 0.7 ms. Differently, the shock wave position stabilizes 
at a timing of 0.8 ms when WF3 waveform is set. For what concerns the 
3-bar case, the WF1, WF2 and WF3 waveforms are observed to generate 
a stabilization of the needle-to-shock wave distance at 0.452 mm, 0.447 
mm and 0.420 mm at a timing of around 0.7 ms. For the sake of syn -
thesis, Table 9 schematizes these results as a function of the joint impact 
of backpressure with current waveform. 
The physical interpretation of these outcomes is following provided. 
4.2. The physical principles underlying the joint impact of backpressure 
with waveform on the stabilization of the shock wave-to-needle distance 
In the light of the above results, it can be concluded that, at unvaried 
backpressure, greater current waveforms lengthen the distance at which 
the shock waves stabilize and shorten the timing of their stabilization as 
well. Thus, since the stabilization is meaningful of the maximum needle 
displacement, it can be argued that, likewise to lower backpressures, 
greater current waveforms boost the needle descent, affecting the shock 
wave development and the following jet development. Bearing in mind 
the weaker magnitude of the needle-induced rarefaction wave in case of 
weaker current waveforms or greater backpressure, this hypothesis 
shows agreement with the Ewan ’ s equation, showing that greater 
ambiance pressures shorten the barrel length, which is comparable to 
the shock wave-to-needle distance [ 2 , 15 , 24 , 25 , 34 ]. Likewise, at con -
stant backpressure, the shock wave is prone to delay its stabilization in 
case of lower currents. This indicates a slower needle descent preceding 
the full injector opening. Therefore, weaker currents prolong the needle 
descent duration. Slower needle displacement in fact alleviates the in -
crease in hydrogen momentum, making the jet less under-expanded and 
retarding the timing of the shock wave stabilization. These conjectures 
might contribute to deduce the duration of the needle descent, 
contributing to circumvent the criticalities associated with the instal -
lation of dedicated displacement sensors, such as scarce physical 
accessibility to the internal part of the nozzle and the risk of disturbing 
the fuel flow [ 34 ]. In conclusion, a slower under-expanded flow, due 
either to higher backpressure or to weaker currents, is expected to 
shorten the shock wave-to-nozzle distance and retard the shock wave 
onset. 
4.3. Qualitative analysis of the combined impact of PR with injector 
geometry on the waves determining the shock structures 
Fig. 13 illustrates the waves-related phenomena, contributing to the 
appearance of the annular-shaped normal shocks, at fully opened 
injector. The images were acquired at a frequency of 100 kHz. 
The waves, originated on the needle tip and the nozzle internal wall, 
are seen to culminate in a point, where normal shocks arise. Once the gas 
flow rounds a convex curved surface, characterized by a varying cur -
vature, expansion waves indeed arise therein and mutually diverge, 
generating the Prandtl-Meyer expansion fan. The last wave is inclined at 
an angle θ
n
, with respect to the flow direction, equal to: 
θ
n
= arcsin
(
1
Ma
n
)
(4)  
where θ
n 
refers to the angle between the gas flow and the n-th expansion 
wave, whilst Ma
n 
stands for Mach number. Therefore, shrunken θ
i 
angles 
between the i-th expansion wave and the flow direction arise in response 
to greater Mach numbers stemming from higher PRs. This causes the n- 
th wave to diverge less from the surface along which the gas flows after 
the corner ( Fig. 14 ). 
At larger PRs, the expansion waves are prone to reach a farther point 
of the outer boundary, where they are reflected as compression waves, 
which then coalesce farther from the injector. As shown by 13, longer 
shock structure-nozzle distances ensue [ 2 , 13 , 15 , 24 , 34 ]. Concerning the 
expansion waves emanated from the needle, at lower backpressure, its 
onset is seen to arise closer to the needle terminal part. Besides the 
phenomena underlying the rise of the expansion waves, the Coand ˆa 
effect is also hypothesized to explain this outcome. The hydrogen flow 
on the needle tip is indeed governed by the equation: 
δ p ( r )
r
= ρ •
δ u ( r )
δ r
(5)  
where δ p, r, δ u and ρ stand for the pressure gradient leading the gas 
Table 9 
The stabilized position (in mm) of the shock wave with respect to the needle tip 
and timings (in ms).   
WF1 WF2 WF3 
P
BACK 
(bar) Position t Position t Position t 
1.2 1.426 0.4 1.235 0.5 1.163 0.5 
3 0.452 0.4 0.447 0.5 0.420 0.6  
Fig. 13. The convex surfaces on the nozzle internal wall and needle tip 
engender waves, indicated by yellow and red arrows, respectively, at back -
pressures of 1.2 bar (a) and 3 bar (b). The waves culminate towards a point, 
indicated by the white arrow, determining the normal shock appearance. (For 
interpretation of the references to colour in this figure legend, the reader is 
referred to the Web version of this article.) 
Fig. 14. The convex surface, approximated to an angular point, generates the 
Prandtl-Meyer fan, composed of expansion waves centred on the corner. 
C. Coratella et al.

<!-- PDF_PAGE: 13 -->

International Journal of Hydrogen Energy 72 (2024) 730–743
742
towards the convex surface of the needle tip, the radius determining the 
curvature of the needle tip, gas velocity gradient and gas density, 
respectively. At unvaried curvature, greater gas velocities accentuate 
the pressure gradient orthogonal to the gas flowing along the needle 
surface. The fluid is more prone to follow the convex surface, delaying 
its detachment from the needle. Thus, the expansion waves arise closer 
to the needle tip. As a result, besides giving rise to discernible normal 
shocks [ 13 , 15 , 24 , 25 , 34 , 36 ], higher PRs cause the coalescence points to 
take place farther from the nozzle. Equation (5) also highlights the key 
role of the curvature of the convex surfaces, which define the nozzle 
geometry, in the expansion waves development and their spatial dis -
tribution. Bearing in mind the high sensitivity of the hydrogen flow 
structure to the even smaller change in geometry of the mechanical 
components defining the flow path, the significancy of impact of the 
injector components ’ design on the shock waves evolution and on the 
needle-induced rarefaction wave gains credibility. 
5. Conclusions 
An experimental campaign, lying within the research line under -
taken by Blois-based PHINIA technical centre, was carried out to 
investigate the development of the hydrogen jet by means of schlieren 
technique. The study dealt with the joint action of ambiance pressure 
with current intensity on the hydrogen jet exiting an outwardly opening 
injector. The investigation was centred on the effect of above parameters 
on:  
- jet axial penetration;  
- development of jet area;  
- the impact of jet axial development to the jet area;  
- the shock waves transient. 
The shots were performed at an injection pressure of 36 bar, whilst 
ambient pressure was at 1.2, 3 and 5 bar. Energizing time was set at 3 
ms, and three current waveforms energizing the injector coils were 
tested. The emerged findings lead to draw the following conclusions.  
- The needle descent is presumed to engenders a rarefaction wave, 
magnitude of which depends on the initial needle speed. At unvaried 
PR, stronger currents yield faster needle motions, and greater mag -
nitudes of the rarefaction wave ensue. This phenomenon is believed 
to affect the jet axial penetration only at increasing PRs. Being as the 
needle speed is at least two orders of magnitude less than gas ve -
locity, a variation of needle speed may indeed be impactful to the jet 
formation solely within certain ranges and at increasing PRs.  
- Higher PRs enhance jet axial penetration and jet area. On the other 
hand, greater jet velocities promote the shear stress on the jet body. 
Therefore, the timing at which the jet experiences great shear stress 
is advanced. The jet collapse occurs earlier. As a result, the maximum 
area is smaller compared to slower jets. By contrast, at lower PRs, the 
jet development is slower but covers larger maximum areas. Lower 
PRs indeed minimize the gas entrainment, which occurs at a reduced 
rate but within a longer period.  
- Employing an outwardly opening injector, at the initial injection 
stages, the radial propagation contributes to the increase in jet area 
more largely than the axial penetration. Given the design of outward- 
opening nozzle, greater PRs accentuate the radial prominence of the 
jet shape at the initial injection stages. On the other hand, higher PRs 
advance the decay of the radial predominance over the axial devel -
opment. The timing of commencing radial decay depends on the PR 
and current profile.  
- The shock waves experience a transient before the needle reaches the 
maximum displacement. At full injector opening, the shock wave is 
stabilized. The transient duration depends on the PR and current 
waveform. Under constant PR, weaker currents prolong the needle 
descent duration and the shock wave transient. This might be 
ascribed to the aforementioned rarefaction wave, which determines 
the gas flow velocity and jet morphology.  
- Larger PRs cause the expansion waves, released by the gas flow 
rounding the internal convex surfaces of the injector, to coalesce 
farther from the nozzle. A longer normal shock-to-nozzle distance 
ensues. At unvaried PR and weaker currents, the shock waves arise 
closer to the injector. These outcomes may be due to the rarefaction 
wave, whose boosting action on the gas momentum dictates the 
shock wave-related phenomena and the jet morphology.  
- Higher PRs accentuate the pressure gradient perpendicular to the gas 
flow along the needle surface. The Coand ˆa effect is stronger, causing 
the gas to follow the convex surface of the needle tip longer, delaying 
its detachment. The expansion waves arise closer to needle end, 
leading the compression waves to coalesce farther from the nozzle. A 
longer normal shock-to-nozzle distance ensues. 
To summarize, this paper highlights the crucial role of the combined 
action of needle dynamics, determined by pressure ratio and current 
waveform, with injector components ’ geometry on hydrogen jet devel -
opment. Particularly, along with the injection settings, the curvature of 
the injector components surfaces determines the spatial distribution of 
the jet in the near-field region. Furthermore, it is the authors ’ opinion 
that, given the scarce physical accessibility to the internal parts of the 
nozzle, a numerical investigation is a viable approach to deepen the 
combined impact of:  
- PR,  
- needle speed,  
- needle geometry, 
on the needle-induced rarefaction wave. This research proposal is 
believed to provide a further insight into the physical principles gov -
erning the hydrogen jet development. 
CRediT authorship contribution statement 
C. Coratella: Writing – review & editing, Writing – original draft, 
Methodology, Investigation, Formal analysis, Conceptualization. A. 
Tinchon: Writing – review & editing, Software, Methodology, Investi -
gation, Formal analysis. R. Oung: Writing – review & editing, Super -
vision, Formal analysis. L. Doradoux: Supervision, Resources. G. 
Dober: Writing – review & editing, Supervision, Resources, Investiga -
tion, Formal analysis. C. Hespel: Writing – review & editing, Writing – 
original draft, Investigation, Formal analysis. F. Foucher: Writing – 
review & editing, Supervision, Project administration, Formal analysis, 
Conceptualization. 
Declaration of competing interest 
The authors declare the following financial interests/personal re -
lationships which may be considered as potential competing interests. 
The authors report that the support was provided by ADEME - 
Agence de la transition ´ecologique. The authors have no known 
competing financial interests or personal relationships that could have 
appeared to influence the work reported in this paper. 
Acknowledgement 
The authors are grateful to the Blois-based PHINIA technical centre 
for the injector supply and technical support. This work was supported 
by the ADEME - Agence de la transition ´ecologique. 
C. Coratella et al.

<!-- PDF_PAGE: 14 -->

International Journal of Hydrogen Energy 72 (2024) 730–743
743
References 
[1] St ę pie ´n Z. A comprehensive overview of hydrogen-fueled internal combustion 
engines: achievements and future challenges. Energies 2021;14(20):6504. https:// 
doi.org/10.3390/en14206504 . 
[2] Yip HL, Srna A, Yuen ACY, Kook S, Taylor RA, Yeoh GH, Chan QN. A review of 
hydrogen direct injection for internal combustion engines: towards carbon-free 
combustion. Appl Sci 2019;9(22):4842. https://doi.org/10.3390/app9224842 . 
[3] Yosri M, Palulli R, Talei M, Mortimer J, Poursadegh F, Yang Y, Brear M. Numerical 
investigation of a large bore, direct injection, spark ignition, hydrogen-fuelled 
engine. Int J Hydrogen Energy 2023;48(46):17689 – 702. https://doi.org/10.1016/ 
j.ijhydene.2023.01.228 . 
[4] Maio G, Boberic A, Giarracca L, Aubagnac-Karkar D, Colin O, Duffour F, 
Pischinger S. Experimental and numerical investigation of a direct injection spark 
ignition hydrogen engine for heavy-duty applications. Int J Hydrogen Energy 2022; 
47(67):29069 – 84. https://doi.org/10.1016/j.ijhydene.2022.06.184 . 
[5] Luo QH, Sun BG. Inducing factors and frequency of combustion knock in hydrogen 
internal combustion engines. Int J Hydrogen Energy 2016;41(36):16296 – 305. 
https://doi.org/10.1016/j.ijhydene.2016.05.257 . 
[6] Takagi Y, Mori H, Mihara Y, Kawahara N, Tomita E. Improvement of thermal 
efficiency and reduction of NOx emissions by burning a controlled jet plume in 
high-pressure direct-injection hydrogen engines. Int J Hydrogen Energy 2017;42 
(41):26114 – 22. https://doi.org/10.1016/j.ijhydene.2017.08.015 . 
[7] Takagi Y, Oikawa M, Sato R, Kojiya Y, Mihara Y. Near-zero emissions with high 
thermal efficiency realized by optimizing jet plume location relative to combustion 
chamber wall, jet geometry and injection timing in a direct-injection hydrogen 
engine. Int J Hydrogen Energy 2019;44(18):9456 – 65. https://doi.org/10.1016/j. 
ijhydene.2019.02.058 . 
[8] Dimitriou P, Tsujimura T. A review of hydrogen as a compression ignition engine 
fuel. Int J Hydrogen Energy 2017;42(38):24470 – 86. https://doi.org/10.1016/j. 
ijhydene.2017.07.232 . 
[9] Verhelst S. Recent progress in the use of hydrogen as a fuel for internal combustion 
engines. Int J Hydrogen Energy 2014;39(2):1071 – 85. https://doi.org/10.1016/j. 
ijhydene.2013.10.102 . 
[10] Ahmed A, Al-Amin AQ, Ambrose AF, Saidur R. Hydrogen fuel and transport system: 
a sustainable and environmental future. Int J Hydrogen Energy 2016;41(3): 
1369 – 80. https://doi.org/10.1016/j.ijhydene.2015.11.084 . 
[11] Coratella C, Tinchon A, Oung R, Doradoux L, Foucher F. Experimental 
investigation of the combined impact of backpressure with the pintle dynamic on 
the hydrogen spray exiting a medium pressure DI outward-opening injector. Int J 
Hydrogen Energy 2024;49:432 – 49. https://doi.org/10.1016/j.ijhydene.2023.08.1 
24 . 
[12] Tinchon A, Foucher F, Doradoux L. Hydrogen jet characterization of an internal 
combustion engine injector using schlieren imaging (No. 2023-01-0301). SAE 
Technical Paper, https://doi.org/10.4271/2023-01-0301 ; 2023. 
[13] Owston Rebecca, Magi Vinicio, Abraham John. Fuel-air mixing characteristics of 
DI hydrogen jets. SAE Int J Engines 2009;1(1):693 – 712. https://doi.org/10.4271/ 
2008-01-1041 . 
[14] Roy MK, Kawahara N, Tomita E, Fujitani T. High-pressure hydrogen jet and 
combustion characteristics in a direct-injection hydrogen engine. SAE Int J Fuels 
Lubricants 2012;5(3):1414 – 25. https://doi.org/10.4271/2011-01-2003 . 
[15] Petersen BR, Ghandhi JB. Transient high-pressure hydrogen jet measurements. SAE 
Transactions; 2006. p. 354 – 64. https://doi.org/10.4271/2006-01-0652 . 
[16] Cheng X, Baigang S, Zhen H. Investigation on jet characteristics of hydrogen 
injection and injection strategy for backfire control in a port fuel injection 
hydrogen engine. Energy Proc 2017;105:1588 – 99. https://doi.org/10.1016/j. 
egypro.2017.03.508 . 
[17] Deng J, Zhong H, Gong Y, Gong X, Li L. Studies on injection and mixing 
characteristics of high pressure hydrogen and oxygen jet in argon atmosphere. Fuel 
2018;226:454 – 61. https://doi.org/10.1016/j.fuel.2018.04.038 . 
[18] Rahman MTA, Kawahara N, Tsuboi K, Tomita E. Effect of ambient pressure on local 
concentration measurement of transient hydrogen jet in a constant-volume vessel 
using spark-induced breakdown spectroscopy. Int J Hydrogen Energy 2015;40(13): 
4717 – 25. https://doi.org/10.1016/j.ijhydene.2015.01.121 . 
[19] Lee S, Kim G, Bae C. Behavior of hydrogen hollow-cone spray depending on the 
ambient pressure. Int J Hydrogen Energy 2021;46(5):4538 – 54. https://doi.org/ 
10.1016/j.ijhydene.2020.11.001 . 
[20] Zhao J, Liu W, Liu Y. Experimental investigation on the microscopic characteristics 
of underexpanded transient hydrogen jets. Int J Hydrogen Energy 2020;45(33): 
16865 – 73. https://doi.org/10.1016/j.ijhydene.2020.04.140 . 
[21] Wang X, Sun BG, Luo QH, Bao LZ, Su JY, Liu J, Li XC. Visualization research on 
hydrogen jet characteristics of an outward-opening injector for direct injection 
hydrogen engines. Fuel 2020;280:118710. https://doi.org/10.1016/j. 
fuel.2020.118710 . 
[22] Tang X, Asahara M, Hayashi AK, Tsuboi N. Numerical investigation of a high 
pressure hydrogen jet of 82 MPa with adaptive mesh refinement: the starting 
transient evolution and Mach disk stabilization. Int J Hydrogen Energy 2017;42 
(10):7120 – 34. https://doi.org/10.1016/j.ijhydene.2017.01.016 . 
[23] Dong Q, Li Y, Song E, Fan L, Yao C, Sun J. Visualization research on injection 
characteristics of high-pressure gas jets for natural gas engine. Appl Therm Eng 
2018;132:165 – 73. https://doi.org/10.1016/j.applthermaleng.2017.12.093 . 
[24] Yu J, Vuorinen V, Kaario O, Sarjovaara T, Larmi M. Characteristics of high pressure 
jets for direct injection gas engine. SAE Int J Fuels Lubricants 2013;6(1):149 – 56. 
https://doi.org/10.4271/2013-01-1619 . 
[25] Tsujimura T, Mikami S, Achiha N, Tokunaga Y, Senda J, Fujimoto H. A study of 
direct injection diesel engine fueled with hydrogen. SAE Trans 2003:390 – 405. 
https://doi.org/10.4271/2003-01-0761 . 
[26] Ouellette PHPG, Hill PG. Turbulent transient gas injections. J Fluid Eng 2000;122 
(4):743 – 52. https://doi.org/10.1115/1.1319845 . 
[27] Fukuma T, Fujita T, Pichainarong P, Furuhama S. Hydrogen combustion study in 
direct injection hot surface ignition engine. SAE Trans 1986:973 – 86. https://doi. 
org/10.4271/861579 . 
[28] Obermair H, Scarcelli R, Wallner T. Efficiency improved combustion system for 
hydrogen direct injection operation. No. 2010-01-2170). SAE Technical Paper, 
https://doi.org/10.4271/2010-01-2170 ; 2010. 
[29] Rogers T, Petersen P, Koopmans L, Lappas P, Boretti A. Structural characteristics of 
hydrogen and compressed natural gas fuel jets. Int J Hydrogen Energy 2015;40(3): 
1584 – 97. https://doi.org/10.1016/j.ijhydene.2014.10.140 . 
[30] Hamzehloo A, Aleiferis PG. Large eddy simulation of highly turbulent under- 
expanded hydrogen and methane jets for gaseous-fuelled internal combustion 
engines. Int J Hydrogen Energy 2014;39(36):21275 – 96. https://doi.org/10.1016/ 
j.ijhydene.2014.10.016 . 
[31] Zhao J, Liu W, Grekhov L. Visualization research on influence of ambient pressure 
on CNG jet characteristics of gas injector with outward-opening nozzle. Fuel 2019; 
257:116084. https://doi.org/10.1016/j.fuel.2019.116084 . 
[32] Sankesh D, Petersen P, Lappas P. Flow characteristics of natural-gas from an 
outward-opening nozzle for direct injection engines. Fuel 2018;218:188 – 202. 
https://doi.org/10.1016/j.fuel.2018.01.009 . 
[33] Seboldt D, Lejsek D, Wentsch M, Chiodi M, Bargende M. Numerical and 
experimental studies on mixture formation with an outward-opening nozzle in a SI 
engine with CNG-DI (No. 2016-01-0801). SAE Technical Paper, https://doi.org/1 
0.4271/2016-01-0801 ; 2016. 
[34] Yu J, Vuorinen V, Kaario O, Sarjovaara T, Larmi M. Visualization and analysis of 
the characteristics of transitional underexpanded jets. Int J Heat Fluid Flow 2013; 
44:140 – 54. https://doi.org/10.1016/j.ijheatfluidflow.2013.05.015 . 
[35] Sathiah P, Dixon CM. Numerical modelling of release of subsonic and sonic 
hydrogen jets. Int J Hydrogen Energy 2019;44(17):8842 – 55. https://doi.org/ 
10.1016/j.ijhydene.2018.09.182 . 
[36] Nagashima T, et al. An experimental study on transverse hydrogen gas injection 
into mach 1.8 airflow channel: the 1st report: single circular injector. J Therm Sci 
1997;6:207 – 17. https://doi.org/10.1007/s11630-997-0038-x . 
[37] Yeganeh M, Akram MS, Cheng Q, Karimkashi S, Kaario O, Larmi M. Experimental 
study of hydrogen jet dynamics: investigating free momentum and impingement 
phenomena. Int J Hydrogen Energy 2024;68:1423 – 37. https://doi.org/10.1016/j. 
fuel.2022.125762 . 
[38] Chapman, Sydney. "V. On the kinetic theory of a gas. Part II. — a composite 
monatomic gas: diffusion, viscosity, and thermal conduction.". Philos Trans R Soc 
Lond - Ser A Contain Pap a Math or Phys Character 1918;217:115 – 97. 549-560 . 
[39] Ni Z, Dong Q, Wang D, Yang X. Visualization research of natural gas jet 
characteristics with ultra-high injection pressure. Int J Hydrogen Energy 2022;47 
(76):32473 – 92. https://doi.org/10.1016/j.ijhydene.2022.07.132 . 
[40] Li X, Christopher DM, Hecht ES, Ekoto IW. Comparison of two-layer model for 
hydrogen and helium jets with notional nozzle model predictions and experimental 
data for pressures up to 35 MPa. Int J Hydrogen Energy 2017;42(11):7457 – 66. 
https://doi.org/10.1016/j.ijhydene.2016.05.214 . 
[41] Erfan I, Chitsaz I, Ziabasharhagh M, Hajialimohammadi A, Fleck B. Injection 
characteristics of gaseous jet injected by a single-hole nozzle direct injector. Fuel 
2015;160:24 – 34. https://doi.org/10.1016/j.fuel.2015.07.037 . 
C. Coratella et al.
