<!-- PDF_PAGE: 1 -->

International Journal of Hydrogen Energy 49 (2024) 1346–1361
Available online 17 November 2023
0360-3199/© 2023 The Author(s). Published by Elsevier Ltd on behalf of Hydrogen Energy Publications LLC. This is an open access article under the CC BY license
(http://creativecommons.org/licenses/by/4.0/).
Contents lists available at ScienceDirect
International Journal of Hydrogen Energy
journal homepage: www.elsevier.com/locate/he
Effects of energy-share and ambient oxygen concentration on
hydrogen-diesel dual-fuel direct-injection (H2DDI) combustion in
compression-ignition conditions
Patrick Rorimpandey, Guanxiong Zhai, Sanghoon Kook, Evatt R. Hawkes, Qing Nian Chan∗
School of Mechanical and Manufacturing Engineering, The University of New South Wales, NSW 2052, Australia
A R T I C L E I N F O
Keywords:
Hydrogen
Dual fuel
Direct injection
Compression-ignition engine
A B S T R A C T
This study investigates the ignition and combustion characteristics of interacting hydrogen (H 2) and diesel
surrogate jets under simulated compression-ignition engine conditions. The experimental setup includes two
converging single-hole injectors in an optically accessible constant-volume combustion chamber (CVCC). The
parameters varied in the study are fuel injection durations and ambient O2 concentrations (10 to 21 vol.%). The
results show that a longer interaction between the diesel products and the H2 jet is required to achieve ignition
of the H2 jet at lower O 2 concentrations. Once ignited, the flame stabilises near or at the nozzle, except under
the lowest ambient O 2 condition of 10 vol.% where a lifted flame is observed. The lift-off response, however,
is influenced by the relative injection duration of the fuels, with the interaction between the incoming H 2 jet
and the diesel combustion recession products possibly playing a role. The interaction between the jets also
affects the recorded intensity and the distribution of the diesel fuel jet soot zone.
1. Introduction
The dual-fuel combustion approach, which involves injecting a
smaller quantity of diesel as an ignition source before, during, or
shortly after the main injection, has gained significant interest in the
engine community [ 1–3]. This approach is particularly attractive for
integrating cleaner alternative fuels with poorer ignition quality than
traditional fuels [ 4,5]. For example, past studies integrating ammonia
into existing natural-gas marine engines have demonstrated the benefit
of reducing engine-out carbon emissions while still providing sufficient
combustion performance [ 6], while drawing on the carbon-neutral
potential of hydrogen (H 2), past dual-fuel studies have also integrated
H2 with secondary fuels including methanol [ 7] and biodiesel [ 8],
showing clear reduction in carbon emissions but still with elevated NOx
levels when H2 substitution is increased, motivating dilution strategies
to help mitigate pollution emissions. Further emissions improvement is
possible if the engine is coupled with an aftertreatment system, with
ongoing work conducted to improve aftertreatments for use with alter-
native engine technologies [ 9]. For this study, the focus is placed on
hydrogen-diesel dual-fuel combustion. In a conventional diesel engine,
fuel ignition occurs through compression ignition, where the fuel is
injected and ignited due to compression [ 10,11]. However, the timing
and location of ignition are primarily determined by engine design
∗ Corresponding author.
E-mail address: qing.chan@unsw.edu.au (Q.N. Chan).
and parameters like compression ratio and fuel injection timing [ 12–
14], offering limited control over the process. In contrast, the dual-fuel
direct injection approach provides additional control by utilising fuel
injection settings as parameters to adjust both timing and sequence [15,
16], as well as duration of injections [ 17,18], allowing for greater
control over in-cylinder mixture preparation [ 19]. This control over
injection parameters can directly influence the distribution of ignition
and heat release between the fuels [ 20], thus impacting thermal effi-
ciency and emissions. To fully harness the advantages of this approach,
it is essential to analyse the interactions among the additional degrees
of freedom, identify potential mechanisms at play, and understand how
they can collectively impact the overall performance.
Previous research on dual-fuel direct injection primarily concen-
trated on studying how various parameters affect the ignition and
combustion of fuels. Notably, the angle of the fuel jet and injection
timing emerged as critical factors influencing mixture formation, com-
bustion, and peak heat release rates. For instance, optical investigations
conducted by Fink et al. [ 21,22] in a rapid compression expansion
machine (RCEM) revealed that altering injection timing has a substan-
tial impact when the jets converge at around 10 degrees under an
ambient temperature of 920 K [22]. In this configuration, injecting the
gas fuel first leads to more premixed combustion and increased heat
release rates, while injecting diesel first results in mixing-controlled
https://doi.org/10.1016/j.ijhydene.2023.11.106
Received 8 September 2023; Received in revised form 6 November 2023; Accepted 8 November 2023

<!-- PDF_PAGE: 2 -->

International Journal of Hydrogen Energy 49 (2024) 1346–1361
1347
P. Rorimpandey et al.
combustion. At a lower temperature of 780 K, misfire occurs when
the gas fuel is injected first as the entrained diesel jet fails to ignite.
Beyond this angle, premixed combustion tends to occur since the jets
are too far apart for consistent interaction. This allows the gas fuel–
air to premix with diesel autoignition before ignition by contact with
burnt diesel products. Ishibashi and Tsuru [15] also examined natural-
gas dual-fuel combustion within an RCEM at a fixed converging jet
angle of 7.5 degrees. By fixing the gas injection timing, they found
that varying the start of diesel injection before, after, or at the time
of gas injection significantly influenced the combustion process and
heat release rate. Injecting diesel before or simultaneously with gas led
to more mixing-controlled combustion, while injecting diesel after gas
allowed for better premixing before ignition, resulting in higher heat
release rates. However, these studies generally kept the fuel injection
durations fixed, favouring longer durations for gaseous fuels to optimise
their energy contribution and minimise carbon-intensive diesel usage
for reduced carbon emissions [23]. Nonetheless, the broader potential
of the dual-fuel approach, especially its operational flexibility to adjust
energy share proportions based on fuel supply conditions, remains un-
derexplored. Consequently, limited understanding exists regarding the
variations that can arise under these changes, particularly the interplay
between the jets when different injection durations are specified and
their associated effects on combustion processes.
Prior research on hydrogen-diesel dual-fuel systems, as conducted
by Liu et al. [17,18] in a modified single-cylinder engine, has high-
lighted the direct influence of injection duration on the combustion
process. Notably, challenges in controlling combustion phasing have
been observed for largely stratified charge cases [18]. Indeed, the
combustion characteristics of the diesel jet, driving the dual-fuel com-
bustion, would be influenced within the presence of a fast penetrating
H2 jet. Existing knowledge suggests that varied injection duration
could influence fluid flow and combustion dynamics of diesel jets,
including the ignition mechanism within a diesel jet [24], resulting
soot formation [25], and enhanced ambient entrainment after fuel
injection ceases [26], characteristics that would presumably be dis-
rupted by interaction with a fast penetrating gas jet. In fact, past
studies have demonstrated that at fixed injection durations, interaction
with the gas jet can influence the diesel ignition process for both
natural-gas [22] and H 2 [16] dual-fuel combustion, varying ignition
delay and even leading to misfires [22]. The added complexities of
varied injection duration has on jet development, and how this affects
dual-fuel combustion necessitates further understanding.
Given the background detailed above, this study’s main objective is
to assess the effects of injection duration and ambient gas concentration
on the ignition and combustion processes of H 2-diesel dual-fuel direct
injection (H2DDI) under conditions relevant to engine operation. The
experimental setup involved injecting H 2 and n-heptane (as a diesel
surrogate) into a quiescent, high-temperature, high-pressure charge
within an optically accessible constant-volume combustion chamber
(CVCC). As briefly discussed, considering that the jet–jet interaction
process is influenced by the interplay among the geometric arrange-
ment of the nozzles, ambient conditions, and injection settings, a fixed
converging setup of two single-hole injectors, which has shown to
yield optimal ignition performance compared to a diverging or parallel
injector setup [21,27], were used to isolate the relative effect of varied
injection duration in the test matrix and minimise interdependencies
among different parameters. Additionally, the relative times at which
both fuel injection starts (i.e., the injection delay) were fixed. To effec-
tively mitigate engine pollutant emissions in hydrogen-fuelled engines,
strategies like exhaust gas recirculation (EGR) can be implemented [28–
31]. EGR involves reintroducing a portion of the engine’s exhaust gases
back into the intake air, reducing the oxygen content in the combustion
chamber and resulting in a more dilute mixture. This is particularly
relevant due to the correlation between higher carbon-based emissions
and an increased diesel energy share, along with potential concerns
regarding NOx emissions in hydrogen-fuelled engines [17,32] as indi-
cated by previous studies. Therefore, this study included the variation
of ambient O2 concentration as a significant parameter of interest. The
experimental diagnostics employed in this study include high-speed
schlieren imaging and pressure-trace measurements.
2. Experimental details
2.1. Constant-volume combustion chamber
Experiments for this study were conducted in an optically accessible
CVCC, able to create a high pressure and temperature charge repre-
sentative of compression-ignition (CI) engine conditions. The CVCC is
cubic with each side measuring 114 mm, featuring six interchangeable
ports located on the chamber walls. The walls were kept at a temper-
ature of 403 K to prevent the formation of water condensation during
experimentation. The H 2 and diesel fuel injectors were placed on one
side port, facing a simple flat metal wall installed on the opposing port.
A mixing fan installed in the top port is used to evenly distribute the
ambient charge. Optical access is possible via sapphire glass windows,
having a clear aperture of 101.6 mm, installed on the remaining three
ports. A schematic diagram of the CVCC setup is provided in 1(a).
The pre-burn process for reaching the quiescent-steady high pres-
sure and temperature conditions within the CVCC has been detailed in
previous studies [33–35] To summarise, high in-chamber pressure and
temperature were achieved by spark igniting a compressed lean mixture
of C 2H2, H 2, O2 and N2, followed by a subsequent cool-down period
as heat transfers to the surrounding chamber walls. A piezoelectric
pressure transducer (Kistler 6052C with amplifier 5015A) was used to
monitor the in-chamber pressure. The fuel injection event is triggered
when a set target in-chamber pressure (and hence temperature) con-
dition is reached during the cool-down phase (see Fig. 2, showing a
typical pressure trace sequence during experimentation). To remove
the effects of heat transfer to the surrounding walls when processing
heat release data, the pressure trace was corrected against the esti-
mated falling pressure rate during the cool-down period by a method
of curve-fitting, as used in past studies [33,36]. For this study, the
partial-pressure metered composition was tailored to achieve 21 vol.%,
15 vol.%, and 10 vol.% O2 concentration after pre-combustion, with
ambient density set to 23.8 kg/m 3. The pressure trace measurement
was also used to derive the apparent heat release rate (AHRR).
A thin-wire K-type thermocouple was used to measure the am-
bient temperature within the CVCC geometrical centre during the
pre-combustion event. The ambient temperature represents the charge
temperature for the study, which was fixed at 890 K by setting the
target in-chamber pressure to 5.2 MPa at start of injection (SOI),
comparable to in-cylinder top dead centre (TDC) conditions measured
in previous H 2DDI studies [17,18] A summary of the experimental
conditions is provided in Table 1, including the gas composition used
to achieve the different O2 concentrations prior to spark ignition. At the
temperature condition of this study, the H 2 ignition delay is consider-
ably greater than that of n-heptane [37,38]. Thus, under the conditions
used in this study, it is reasonable to assume that the interaction with
a reacting or burnt n-heptane jet is the direct factor towards H 2 jet
ignition.
2.2. Injection conditions
The experimental setup employed two converging single-hole injec-
tors for separate injection of H 2 and diesel into the CVCC. The use of
single-hole injectors instead of multi-hole injectors aimed to simplify
result interpretation by avoiding complexities associated with multiple
jet interactions from the same injector. The simplified jet interaction
configuration is also more suited for optical diagnostics, providing
clearer visualisation of ignition and combustion processes. The H 2
injector was positioned at the port centre, aligned with the port axis, as

<!-- PDF_PAGE: 3 -->

International Journal of Hydrogen Energy 49 (2024) 1346–1361
1348
P. Rorimpandey et al.
Fig. 1. (a) Cross-section schematic of the constant-volume combustion chamber
(CVCC). (b) Detailed view of the H 2 and diesel injectors layout, representing H 2 (blue)
and n-heptane jet cones (red), along with points of jet axis and cone intersection. (For
interpretation of the references to colour in this figure legend, the reader is referred
to the web version of this article.)
Fig. 2. Sample CVCC pressure trace data during an experiment run. Starting at
spark ignition, it highlights the following four key events: (i) premixed ambient gas
combustion, (ii) cool-down period, (iii) start of fuel injection and (iv) fuel ignition.
Table 1
Summary of the experimental conditions, and the gas composition prior to spark
ignition for each O2 concentration.
CVCC ambient conditions
Wall temperature (K) 403
Ambient O2 concentration (vol.%) 21, 15, 10
Ambient gas density (kg/m 3) 23.8
Ambient gas pressure (MPa) 5.20
Ambient core gas temperature (K) 890
Ambient gas composition
O2 product Reactants (Mole fraction, %)
C2H2 H2 O2 N2
21 vol.% 3.00 0.50 28.38 68.12
15 vol.% 3.06 0.50 22.63 73.81
10 vol.% 3.10 0.50 17.83 78.57
Table 2
Summary of injection conditions.
Fuel injection conditions
Fuel H 2 n-heptane
Nozzle diameter (mm) 0.51 0.105
Fuel reservoir pressure (MPa) 20 70
Low heat. value [ 10] (MJ/kg) 120.0 43.2
Total energy output (J) 624
Injection duration See Table 3
depicted in Fig. 1(a). The diesel injector orifice was positioned 12.3 mm
above the H2 injector orifice, inclined at a 12 ◦ angle relative to the H2
injector axis. The two jet axes intersected 57.2 mm downstream from
the H2 nozzle. Considering estimated cone angles of 25 ◦ for the H2 jet
and 20◦ for the n-heptane jet, the jets are expected to start overlapping
at a distance of around 21 mm from the H 2 injector, along the H 2 jet
boundary.
To minimise the compositional complexities and variables asso-
ciated with commercial fuels, neat n-heptane was used as a single-
component diesel fuel surrogate. It was injected at a rail pressure of
70 MPa through a custom single-hole nozzle attached to a commercial
common rail injector (Bosch, solenoid, generation 2). The H 2 injector
was derived from a modified commercial gasoline direct-injection (GDI,
Bosch, HDEV5.1) injector equipped with a 0.51 mm single-hole diam-
eter nozzle attachment [37]. Compressed H2 from a 1 dm 3 pressurised
reservoir was supplied to the H 2 injector, charged using a pneumatic
H2 compressor (Haskel with Zenobalti pressure controller). A reservoir
pressure of 20 MPa resulted in approximately 14 MPa H 2 pressure
upstream of the nozzle, accounting for friction losses associated with
gas passage through narrow channels within the injector [ 37].
Two separate external injector drivers (Zenobalti ZB-5012 for H 2
and ZB-5014 for diesel) were used to energise the H 2 and diesel
injectors, with timing controlled by a digital delay and pulse generator
(Stanford Research Systems DG535). The SOI timing for both fuels was
fixed without any set delay to facilitate near-simultaneous injection.
A delay of 0.08 ms existed between H 2 SOI to n-heptane SOI due to
delays associated with nozzle opening and closing, as well as back
pressure effects. The n-heptane mass flow was measured under identical
conditions using a Bosch-tube injection rate meter [ 39]. The injected
amount of H2 gas was determined by measuring the change in chamber
pressure after H 2 injection [ 37]. The hydraulic injection durations
of H 2 and n-heptane were determined based on the targeted energy
contribution from each fuel, while maintaining a fixed total energy
output of 624 J. A summary of the injection conditions utilised in this
study is provided in Table 2. It is noted that the injector configuration
and settings, including injector pressure and duration, were specifi-
cally selected to expose different aspects of the dual-fuel interaction
processes. Therefore, they are not aimed at any specific load condition.

<!-- PDF_PAGE: 4 -->

International Journal of Hydrogen Energy 49 (2024) 1346–1361
1349
P. Rorimpandey et al.
Fig. 3. A schematic of the constant-volume combustion vessel (CVCC) and the high-
speed schlieren imaging optical arrangement. The light path (transparent yellow) from
the schlieren imaging light source and a model of the penetrating jet (red) are shown.
(For interpretation of the references to colour in this figure legend, the reader is referred
to the web version of this article.)
2.3. Optical diagnostics
2.3.1. Schlieren imaging
This study employed a Z-type schlieren imaging setup to capture
the jet boundary and the high-temperature reaction zone, as depicted
in Fig. 3. The setup involved directing collimated light from a 150 W
xenon arc lamp (Abet Technologies LS-150) through a 50 mm plano-
convex lens with a 75 mm focal length. The light then passed through
a 2 mm aperture and was collimated using a 108 mm f/6 parabolic
mirror. Subsequently, the collimated light beam traversed the CVCC
and reached the high-speed camera through a series of mirrors. To
enhance imaging sensitivity, a 2 mm pin-hole aperture was positioned
between the second parabolic mirror and the camera lens at the beam
focal point. The high-speed camera used was a Phantom VEO 1310,
equipped with an 85 mm f#1.8 AF-D Nikkor lens. It operated at a frame
rate of 30,000 frames per second with a1.4 μs exposure time, providing
an image resolution of approximately 0.13 mm per pixel.
Schlieren imaging is an optical technique that detects refractive
index gradients along the line-of-sight induced by fuel evaporative
cooling, mixing, and combustion events. These variations manifest as
intensity changes in the captured images [ 34]. A high-temperature
combustion event generates a sharp refractive index gradient, which
appears as a darkened area in the schlieren image, as illustrated in
Fig. 4(a). The background schlieren pattern, representing the ambient
gas, remains relatively stationary compared to the effects caused by
the fast-moving jet. Consequently, the jet-induced schlieren effects
can be distinguished from the background patterns by analysing the
differences between consecutive video frames [ 40], as demonstrated
in Fig. 4(b). Additionally, the processed image outlines the boundaries
of the non-reacted H 2 (blue) and n-heptane (red) jets, as well as the
darkened burnt-zone region (green), as depicted in Fig. 4 (c).
2.3.2. Photodiode
A photodiode (Thorlabs PDA100A-EC) with a spectral sensitivity
ranging from 340 to 1100 nm and operating at a sampling rate of
200 kHz was used to provide a spatially-integrated measurement of
luminosity during events of combustion within the chamber. The pho-
todiode output is proportional to the incident light it receives. The
measurements of flame luminosity offer a qualitative indication of the
differences in soot formation in the fuel jets [41,42]. To prevent satura-
tion and optimise the signal-to-noise ratio, the gain of the photodiode
Fig. 4. (a) Sample raw schlieren high-speed image, (b) image corrected by subtracting
the pixel intensity values from the previous frame, and (c) processed image showing
the unreacted n-heptane (red) and H 2 (blue) jets, and reacted region (green). (For
interpretation of the references to colour in this figure legend, the reader is referred
to the web version of this article.)
was adjusted according to the luminosity level. The recorded signal was
corrected based on the gain adjustment before comparing.
2.4. Pressure trace and apparent heat release rate
Pressure trace measurements were used to determine the AHRRs,
similar to past studies [ 43,44], to help assist in result interpretation.
The instantaneous AHRR was derived from the heat release rate for-
mula shown in Eq. (1) [33], where P represents the in-chamber pressure
trace, V represents the chamber volume and 𝛾 represents the ratio of
the specific heats, typically set to 1.35 at the conducted experimental
ambient temperatures [10].
𝑑𝑄
𝑑𝑡 = 𝛾
𝛾 − 1 𝑃 𝑑𝑉
𝑑𝑡 + 1
𝛾 − 1 𝑉 𝑑𝑃
𝑑𝑡 (1)
Since volume is constant within the CVCC, the volumetric term
𝑑𝑉 ∕𝑑𝑡 becomes zero, removing the first term within the equation
and simplifying the AHRR formula within the CVCC to that shown
in Eq. (2).
𝑑𝑄
𝑑𝑡 = 1
𝛾 − 1 𝑉 𝑑𝑃
𝑑𝑡 (2)
This study focuses on the AHRR shape and features, which can
become smeared due to ignition delay variability when ensemble-
averaged. To address this concern, a mitigation strategy by shifting
AHRR traces along the time axis based on the difference between the
individual ignition delay and the mean ignition delay was adopted.
Algebraically, the following ensemble averaging formula was used:
AHRR(𝑡) = 1
𝑛
𝑛∑
𝑖=1
AHRR𝑖(𝑡 + 𝑡ID,𝑖 − 𝑡ID) (3)
where n denotes the total number of cycles, 𝑡ID the ignition delay and
the overline signifies ensemble-averaged quantities.

<!-- PDF_PAGE: 5 -->

International Journal of Hydrogen Energy 49 (2024) 1346–1361
1350
P. Rorimpandey et al.
Table 3
Summary of the cases investigated and its associated case names. Injection duration
and injected mass of each energy share cases are provided at the bottom of table.
Cases investigated
Case name Energy share Ambient
H2 Diesel O2 vol.%
21 vol.% O2 concentration
H90/D10/21O2 90% 10% 21 vol.%
H80/D20/21O2 80% 20% 21 vol.%
H60/D40/21O2 60% 40% 21 vol.%
H40/D60/21O2 40% 60% 21 vol.%
15 vol.% O2 concentration
H90/D10/15O2 90% 10% 15 vol.%
H80/D20/15O2 80% 20% 15 vol.%
H60/D40/15O2 60% 40% 15 vol.%
H40/D60/15O2 40% 60% 15 vol.%
10 vol.% O2 concentration
H90/D10/10O2 90% 10% 10 vol.%
H80/D20/10O2 80% 20% 10 vol.%
H60/D40/10O2 60% 40% 10 vol.%
H40/D60/10O2 40% 60% 10 vol.%
Injection durations by energy share
Energy share Duration (ms) Mass injected (mg)
H2 Diesel H 2 Diesel H 2 Diesel
90% 10% 3.79 0.68 4.43 1.37
80% 20% 3.35 1.16 3.93 2.73
60% 40% 2.68 2.62 2.95 5.46
40% 60% 2.03 3.77 1.97 8.19
2.5. Experimental parameters and notations
Table 3 summarises the investigated cases, their settings, and corre-
sponding notations. In this study, the adopted notation system describes
the energy proportion supplied by the H 2 and n-heptane fuels (D)
and the ambient O2 concentration condition. For instance, a dual-
fuel (DF) case with 90% energy contribution from H 2, 10% from
n-heptane, and an ambient O2 concentration of 21 vol.% O2 is denoted
as ‘H90/D10/21 O2’. For the single-fuel (SF) reference case using n-
heptane only as the fuel, only the diesel energy share (in the context
of the dual-fuel scenario) and the ambient O2 condition are specified
(e.g., D10/21O2).
2.6. Dual-fuel ignition delay
There may be two separate ignition events in DF combustion: the
𝑛-heptane autoignition and subsequent H 2 ignition after interaction
with the burnt 𝑛-heptane fuel. For this study, it is observed that whilst
𝑛-heptane autoignition leads to a distinct rise in the pressure trace
at 21% O2, the pressure rise becomes less defined at lower ambient
O2. This creates difficulty in identifying the 𝑛-heptane ignition event
from the pressure trace alone. Additionally, during DF combustion,
only a single rise in the pressure trace is detectable for the events
where n-heptane and H 2 ignite in close succession. This prevents the
discernment of the two ignition events and their ignition delay timings.
To ensure consistency, the timings of 𝑛-heptane ignition for all experi-
mental cases were determined using high-speed schlieren images. The
ignition delay time of 𝑛-heptane was derived from the schlieren image
frame, where a darkened high-temperature region first appeared within
the 𝑛-heptane jet. Specifically, the timing was identified when the
localised intensity decreased by 10%, providing a consistent measure
across all experiments.
In the DF cases, the presence of schlieren effects caused by the burnt
n-heptane fuel obscures the optical evaluation of H2 ignition, hindering
the determination of the H 2 ignition delay. Since a significant portion
of the heat release rapidly occurs during H 2 ignition, the timing of
H2 ignition is derived from the AHRR using specific thresholds. While
ideally the AHRR threshold should be as low as possible to match the
actual time of ignition, it must be ensured that the rise in AHRR is
a result of H 2 ignition and not n-heptane. Thus, ignition of the H 2
jet is firstly identified, defined as when the AHRR rises and reaches a
high threshold of 150 kJ/s. After identifying the H2 ignition event from
the AHRR, H 2 ignition delay can be defined as the instant the AHRR
passes 30 kJ/s (above the noise floor of the AHRR data) during the rise
towards the 150 kJ/s threshold. This choice of threshold is motivated
by the fact that the peak AHRR of n-heptane-only injections does not
exceed 100 kJ/s for the different injection durations cases. A threshold
of 150 kJ/s, therefore, serves as a reasonably conservative indicator of
H2 ignition during DF combustion. Note that by the above definition,
in cases where the two ignition events occur in quick succession, the
H2 ignition is not strictly limited to H 2 alone, as the heat release from
𝑛-heptane autoignition also contributes.
3. Results and discussion
3.1. Ambient 21 vol.% O2 concentration
Fig. 5 shows the schlieren sequences depicting four DF energy share
cases, H90/D10, H80/D20, H60/D40, and H40/D60, under an ambient
O2 concentration of 21 vol.%. The images show the progression of
time after the 𝑛-heptane SOI, with the time instants specified at the
bottom-left corners. Additionally, the corresponding frames for the SF
scenario involving 𝑛-heptane only are provided below the DF frames for
comparison. Red contours are used in the DF and SF frames to outline
the non-reacting 𝑛-heptane jet boundary, with blue contours used in
DF frames to highlight the non-reacting H 2 jet boundary. In the DF
and SF frames, a green contour is used to signify the reaction zone.
To aid comparison, overlaid in the DF frames are yellow contours to
outline the mean combined area of unreacted and reacted 𝑛-heptane
jets, averaged from the schlieren images of all SF runs. The radial ( 𝑟)
and axial ( 𝑥) distances from the H 2 injector nozzle are indicated for
reference. The schlieren images were selected from experimental runs
with a main ignition delay time closest to the average value. The initial
image presents the onset of the ignition kernel ( n-heptane ignition
delay), while the second and third frames correspond to the H2 ignition
delay and peak AHRR, respectively. Finally, the fourth and fifth frames
were chosen to highlight distinct features in the combustion sequences
for their individual cases. The injector orifices are located at the far
left centre of each image, with fuels being injected to the right. The ‘o’
and ‘x’ symbols at the nozzles are used to denote if the corresponding
injector is opened or closed, respectively, at the time instances shown.
In all cases, the 𝑛-heptane jet ignites externally to the H2 jet bound-
aries, with the initial ignition kernel originating from the 𝑛-heptane
jet head section. In the subsequent two frames, the reaction front
appears to propagate from the region of contact between the jets,
starting at approximately 20 mm from the H 2 nozzle along the H 2
jet boundary (refer to Fig. 4). The reaction front moves towards the
nozzle and jet tip as it engulfs the unburnt H 2 jet regions, with bright
soot luminosity regions becoming visible in the images shortly after
autoignition. The second frames, corresponding to schlieren images
captured at H2 ignition delay, reveal high-temperature schlieren effects
are detectable within the H 2 jet boundaries. This supports the use of
the AHRR criteria as outlined in Section 2.6 as a reasonable ignition
indicator for the H 2 jet.
In the schlieren images, the luminous region becomes visible around
30 mm from the injector shortly after autoignition in both SF and DF
cases. For SF cases with longer injection durations (D40 and D60),
the bright zone grows and reaches a quasi-steady state, maintaining
a consistent axial length throughout the injection time.
While there are certain similarities in the characteristics of the soot
regions when comparing the DF and SF cases, with the soot luminous
zones initially appearing at comparable locations and times as shown

<!-- PDF_PAGE: 6 -->

International Journal of Hydrogen Energy 49 (2024) 1346–1361
1351
P. Rorimpandey et al.
Fig. 5. High-speed schlieren images for energy share cases H90/D10, H80/D20, H60/D40, and H40/D60 under ambient 21 vol.% O2. The corresponding n-heptane only cases at
the same time aSOI are shown at the same frame under the dual-fuel (DF) case. Highlighted are the n-heptane jet boundary (red), H 2 jet boundary (blue), and high-temperature
flame (green). The n-heptane jet boundary averaged from all SF runs is overlaid on the DF frames (yellow). Axial and radial distances from the injection nozzle are represented as
x and r, respectively. The first frame following H 2 ignition delay time is outlined by a red border. Time sequence is relative to n-heptane SOI. (For interpretation of the references
to colour in this figure legend, the reader is referred to the web version of this article.)
in the third column of Fig. 5 , there are also noticeable differences
between the DF and SF cases at comparable times. Specifically, when
the soot luminous regions in the DF cases first form, they are already
less uniformly distributed across the jet head regions compared to that
observed in the SF cases. However, there are noticeable differences
between DF and SF cases at similar timings. The axial lengths of the
soot luminous regions in DF cases extend beyond those observed in SF
cases, with the duration of the fuel injection playing a role. The DF
case with the shortest n-heptane injection duration (H90/D10) shows
the luminous region intensity rapidly diminish after initial formation
due to the short injection duration of n-heptane. Hence, no soot data
is available for this condition. However, for DF cases with longer n-
heptane injection durations (H80/D20, H60/D40, and H40/D60), the
soot luminous region further extends to the H 2 jet tip, surpassing the
averaged axial length of n-heptane soot zone in the corresponding SF
case, while both injectors are active. In cases where n-heptane injec-
tion duration exceeds H 2 injection (H40/D60), the axial length of the
luminous soot region reverts to a length similar to the corresponding SF
case, during sole n-heptane injection, after H 2 end of injection (EOI).
Previous studies [45] have indicated that the unchanging axial length
of the sooting region during the injection period in SF cases suggests
complete oxidation of soot within the established quasi-steady flame
region. However, the observed variations in the axial extent of the
luminous soot region during simultaneous H 2 and n-heptane injection
suggests the presence of H 2 injection can influence the soot processes
within the n-heptane jet. For instance, in the converging setup, the
merging of the jets can result in a higher combined velocity than each
jet alone, potentially affecting soot oxidation or pushing the soot region
further downstream. The exact mechanisms involved require further
investigation for confirmation. Whilst there are differences between this
study’s experimental setup and real engines, the observed extension of
the soot region beyond its expected oxidation range in the presence of
H2 injection raises the need to assess its impact on actual engine-out
particulate emissions.
Further analysis of the schlieren images suggests that a distinct
‘‘roll-up’’ phenomenon becomes apparent after the jets overlap and
ignition occurs. Fig. 6 displays image sequences for the H40/D60/21O2
case, using a colour scheme, format, and annotations consistent with
Fig. 5. The time instants after SOI (aSOI) are indicated in the bottom-
left corners of the panels, with smaller time steps compared to the

<!-- PDF_PAGE: 7 -->

International Journal of Hydrogen Energy 49 (2024) 1346–1361
1352
P. Rorimpandey et al.
schlieren panels in Fig. 6, specifically chosen to highlight the ‘‘roll-up’’
phenomenon.
In these schlieren frames, a small cyan-coloured annotation arc
highlights the region where the roll-up phenomenon eventually occurs.
Within these images, an outward bulge forms at the upper boundary of
the n-heptane jet periphery and grows beyond the average n-heptane
jet boundary, roughly coinciding in timing and location with the oc-
currence of combustion propagation between the jets. The region below
the annotation arc initially brightens over time, revealing a luminous
flame structure that appears to counter-rotate as the outward bulge
increases. The intensity then gradually diminishes as the structure
shifts downstream. This is visualised in the last frame, which shows
a time-averaged schlieren captured between 0.30 ms and 2.97 ms after
n-heptane SOI, where soot luminosity is most prominent, highlighting
the apparent upwards movement or ‘‘roll-up’’ of the n-heptane jet
(indicated by the red arrow) creating the outward bulge, and the
luminous region propagating from this bulge towards the H 2 jet-tip
downstream (indicated by the yellow arrow). The reader is also referred
to the high-speed schlieren movie in the Supplementary Material, in
which the roll-up features more distinguishable. The flame evolution
patterns depicted in Fig. 5 for the H40/D60 case were also observed
in other cases. An analysis of all 20 experimental runs conducted for
various DF cases at 21 vol.% O2 indicates that the roll-up phenomenon
occurred in at least 65% of the runs, considering schlieren diagnostic
limitations can hinder detection of the phenomenon occurring along
its line-of-sight. The roll-up phenomenon is similarly observed for 60%
and 17.5% of runs from the 15 and 10 vol.% O2 cases, respectively.
These observations highlight that the interaction betweenn-heptane
and H2 jets in the DF cases can produce flow and combustion patterns
not present in the SF counterparts. The interaction between the fuel jets
in DF combustion processes, depending on the ambient conditions, can
create a localised region with mixture composition, temperature, and
strain conditions that are initially favourable for soot formation before
additional interactions between the vortical structures and flames oc-
cur. Considering that this anomaly is only observed in 17.5% of the
experimental runs at the lower reactive ambient 10 vol.%O2, while this
was observed in 60%–65% of the runs at the more reactive higher O2
concentration cases, it is likely that the phenomenon is primarily driven
by the effects of dual-fuel combustion. Considering that this anomaly is
only observed in 17.5% of the experimental runs at the lower reactive
ambient 10 vol.% O2, while this was observed in 60%–65% of the
runs at the more reactive higher O2 concentration cases, it is likely
that this anomaly is due to effects of dual-fuel combustion rather than
effects from non-reactive jet flow and interaction. However, the exact
mechanisms underlying these observations cannot be fully explained
with the data from this study alone.
Fig. 7 presents the averaged AHRR, apparent total HR, natural lu-
minosity and flame recession for the DF cases and their SF counterparts
under ambient 21 vol.% O2 concentration. The average n-heptane and
H2 ignition delay times are shown by an orange dotted line and blue
dash-dotted line, respectively, with uncertainty represented by an error
bar along the time-axis. The first row of the figure shows the average
AHRR evolution, which can be analysed similarly to interpreting diesel
engine AHRR. After ignition, an increase in AHRR is expected during
the premixed-burn phase, with a magnitude dependent on the mass and
distribution of the readily combustible fuel–air mixture within the jet.
Following the premixed-burn phase, a more stable AHRR, proportional
to the fuel–air mixing rate, is anticipated during the mixing-controlled
combustion period. Analysis reveals that the AHRR rapidly rises after
ignition for the DF cases, followed by a stable phase as the flame
further develops. The peak AHRR values of the DF cases exhibit a
similar magnitude, aligning with similar flame penetrations observed in
the schlieren images at peak AHRR timings. This suggests comparable
amounts and distributions of readily combustible fuel–air mixtures at
ignition.
Fig. 6. High-speed schlieren images for energy share case H40/D60 under ambient
21 vol.% O2, to highlight the ‘‘roll-up’’ phenomenon shown in the region below the
cyan-coloured annotation arc. Highlighted are the n-heptane jet boundary (red), H 2
jet boundary (blue), and high-temperature flame (green). Axial and radial distances
from the injection nozzle are represented as x and r, respectively. Time sequence is
relative to n-heptane SOI. The last frame shows a time-averaged schlieren captured
between 0.30 ms–2.97 ms, with the upward movement of the n-heptane jet indicated
by a red arrow, and downstream propagation of the luminous region indicated by a
yellow arrow. (For interpretation of the references to colour in this figure legend, the
reader is referred to the web version of this article.)
For DF cases with longer H 2 injection durations (H90/D10 and
H80/D20), a steady AHRR period is established after peak. For DF cases
with longer diesel injection durations, a more transient AHRR profile
is established after the peak, increasing slightly until close to the H 2
EOI. In the H40/D60 case, where n-heptane injection duration exceeds
H2, the AHRR profile resembles that of the SF case between H 2 and
n-heptane EOI timings. Notably, the SF cases also exhibit a premixed-
burn peak followed by a stabilisation phase. In the latter phase, there
is a continuous increase in AHRR until the n-heptane EOI, suggesting
incomplete fuel–air mixing with n-heptane, leading to localised fuel-
rich regions and delayed combustion. Since the n-heptane injection is
optimised for stable and minimal fuel quantity required for ignition,

<!-- PDF_PAGE: 8 -->

International Journal of Hydrogen Energy 49 (2024) 1346–1361
1353
P. Rorimpandey et al.
the suboptimal fuel–air mixing and resulting heat release performance
are expected.
The second row of Fig. 7 presents the total heat release data for
both the DF and SF cases, or the cumulative heat released, normalised
against the expected total heat release of each case, determined by
accounting mass flow rate and fuel lower heating value. Analysis of the
DF cases shows relatively consistent total heat release that correspond
to the fuel energy content, ranging from 97% of the fuel energy content
at H90/D10 to 91% for H40/D60, decreasing with lower H 2 energy
share. In contrast, the SF cases exhibit a lower total heat release
ranging from 70% to 79%, aligning with expected suboptimal fuel–air
mixing. The higher total heat release in the DF cases suggests that co-
combustion of fuels leads to more complete combustion compared to
n-heptane alone in the SF cases. This can be attributed to the physical
and thermochemical properties of H2, including high dispersion speed,
effective fuel and air mixing, wide flammability limit, high flame speed,
and the ability to operate under lean conditions, enhancing thermal
efficiency [46].
The third row of Fig. 7 shows the spatially-integrated measured
luminosity for the DF cases and their SF counterparts, captured by
the photodiode, providing a qualitative indication of the luminosity
emitted from soot formation [40,47]. In the H90/D10 DF case, where
the n-heptane injection duration is shortest, a significant reduction
in luminosity is observed, representing only 20% of the maximum
intensity in the SF case. As the energy share from n-heptane increases,
the luminosity in the DF cases increases in similarity to the SF cases,
reaching approximately 80% of the maximum intensity in the SF cases.
The results suggest that the elongation of the soot region observed in
the DF schlieren images may not necessarily result in higher detected
luminosity or soot levels. Instead, the findings indicate slightly lower
soot levels in the DF cases compared to the SF cases, with a more
noticeable reduction observed when the 𝑛-heptane injection duration
is short. However, further validation of this observation requires ad-
ditional quantitative measurement techniques, such as laser-induced
incandescence [48], coupled with more quantitative image processing
methodologies [49].
The fourth row of Fig. 7 displays averaged and individual flame
recession data obtained from the schlieren images for all DF cases, with
the estimated mean spatial and temporal start of jet–jet interaction,
indicated by a red cross. The averaged axial ignition location of the first
combustion kernel detected is also indicated. The recession trends con-
sistently shows propagation of combustion from the upstream region of
jet–jet interaction and the first combustion kernel towards the nozzle,
regardless of changes in the energy share between the fuels. The start of
flame recession appears to occur shortly after the emergence of the first
kernel. While the accurate flame position determination is challenging
near the nozzle due to imaging limitations, it can be derived that the
flame position stabilisation timing approximately corresponds to the
point where the AHRR profile levels off, indicating the presence of an
established diffusion flame. The exact mechanisms behind the observed
combustion recession cannot be definitively determined based on the
current experimental methods and dataset. However, the previous stud-
ies performed by the authors have suggested that flame deflagration,
among other potential mechanisms, likely contributes to the observed
recession response [50].
Table 4 presents the ignition delay times forn-heptane and H2 in the
DF cases under ambient conditions with 21 vol.%O2 concentration. The
table also includes the ignition delay time difference between H 2 and
n-heptane, which indicates the effectiveness and stability of igniting
the gas jet, since ignition of the H 2 jet is initiated by combustion
of the 𝑛-heptane jet. The table also provides the time intervals be-
tween 10% (CHR10) and 90% (CHR90) of the cumulative heat release,
respectively, commonly used to indicate the combustion duration.
Analysis of the data reveals comparable n-heptane ignition delay
times among the DF cases, falling within the uncertainty ranges of the
corresponding SF ignition delay times. Similarly, the data show similar
differences in ignition delay timings between H2 and n-heptane, which
aligns with observations of the schlieren images. The n-heptane jet con-
sistently ignites externally to the H 2 jet boundary before propagating
to the H2 jet from the region where the jets overlap. The results of this
study contradict previous research [51–54] on the ignition ofn-heptane
in a homogeneous H 2-air background. Prior studies reported that the
presence of H2 retards the ignition of the diesel surrogate. However, in
this case, part of the n-heptane jet is external to the H 2 jet, preventing
this effect. The presence of the H 2 jet does not noticeably alter the n-
heptane ignition delay. This results in similar ignition timings observed
in both the DF and SF cases, with values that are within one standard
deviation of each other. However, a fluctuation in n-heptane ignition
delay between DF cases compared to SF can be observed, and is likely
due to the influence of the H 2 jet partially increasing the variability of
the n-heptane jet ignition. Noting that only 5 runs were conducted for
each case due to experimental constraints, further repetitions is likely
required to fully capture the true variance in n-heptane ignition delay
under DF conditions. Regardless, the DF n-heptane ignition delay for
all DF cases is within 1 standard deviation of each other, meaning the
ignition delay variance is perhaps insignificant.
The combustion duration of DF cases show a decreasing trend with
increasing energy share from n-heptane before increasing to reach
the longest duration in the DF case with the largest energy share
(H40/D60). The variations in combustion duration among the DF cases
can be attributed to complex interplay between different factors such
as mass flow rate and energy content of each fuel. The mass flow rate of
𝑛-heptane is approximately two times that of H2, while the low heating
value (LHV) of 𝑛-heptane is approximately three times lower than that
of H2 (refer to Table 2). The distinctive combustion characteristics of
each fuel and their interaction during co-combustion also contribute to
the variation. H 2 has a wide flammability limit and high flame speed,
which can impact the heat release from the fuels.
3.2. Ambient 15 vol.% O2 concentration
This section examines the impact of ambient oxygen concentration
on the DF cases. Fig. 8 displays sample images for the H90/D10,
H80/D20, H60/D40, and H40/D60 DF cases, along with their corre-
sponding SF counterparts, under ambient conditions with 15 vol.% O2
concentration. The images maintain the same colour scheme, format,
and annotations as Fig. 5.
At 15 vol.% O2 concentration, the combustion process in the DF
cases are similar to that observed at ambient 21 vol.% O2. Combustion
initially starts from the n-heptane jet igniting at the jet head region,
external to the H 2 jet boundary, followed by combustion spreading
to the H 2 jet across the overlapping region between the two jets. As
combustion progresses towards the nozzle and jet tip, it engulfs the
region of unburnt H 2. However, a noticeable difference observed at
15 vol.% O2 is the flame stabilising around 5 to 7 mm from nozzle,
before it fully recedes to nozzle after H 2 EOI. For H40/D60, the flame
still actively travels upstream at time of EOI, and hence is not observed
to attain a stabilised position during H 2 injection. Another difference
is in the soot luminous zone. In contrast to the 21 vol.% O2 SF case,
the SF case at 15 vol.% O2 concentration shows a different behaviour.
The bright soot zone in the SF case forms mainly at the jet head and
progresses downstream before the n-heptane EOI. Only the SF case with
the longest n-heptane injection duration (D60/15 O2) exhibits a quasi-
steady soot zone just before n-heptane EOI. In contrast, the DF case
shows no formation of transient soot cloud at the jet head region. The
luminous soot region in the DF case, affected by the H2 jet, also appears
to occupy a narrower region, further indicating the interaction between
the H 2 jet and n-heptane alters the flow, combustion dynamics, and
associated soot processes.
The AHRR plots of the 15 vol.% O2 cases (Fig. 9, first row) show
a rapid increase at ignition, forming a peak before reaching a more
quasi-steady state. The peak and lower steady-state AHRR magnitudes

<!-- PDF_PAGE: 9 -->

International Journal of Hydrogen Energy 49 (2024) 1346–1361
1354
P. Rorimpandey et al.
Fig. 7. The averaged AHRR, apparent total heat release, photodiode measured spatially-integrated luminosity, and flame recession for energy share cases H90/D10, H80/D20,
H60/D40, and H40/D60, under ambient 21 vol.% O2 concentration, shown at equal time sequence after n-heptane SOI. Data relating to dual-fuel (DF) or single-fuel (SF) cases
are highlighted by blue or orange lines, respectively, with the H 2 and diesel EOI times shown in each plot. For the fourth row flame position plot, the temporal flame position
from each run is shown by blue dashed lines, with the extracted average flame position highlighted by black lines; the average upstream location of the n-heptane jet kernel is
highlighted by an orange error bar, with start of jet–jet overlap highlighted by a red cross. (For interpretation of the references to colour in this figure legend, the reader is
referred to the web version of this article.)
Table 4
Average n-heptane and H 2 ignition delay times, mean difference between the two ignition events, and combustion duration CHR90-CHR10
for all dual-fuel (DF) cases at ambient 21 vol.% O2 concentration, relative to n-heptane SOI. Single-fuel ignition delay provided for reference.
Uncertainty provided as one standard deviation.
Ignition delay times — 21 vol.% O2 concentration
Case Single-fuel Dual-fuel
n-heptane n-heptane H 2 (H2 - n-heptane) CHR90-CHR10
Ignition delay (ms) Ignition delay (ms) Ignition delay (ms) Ignition delay (ms) (ms)
H90/D10/21O2 0.43 ± 0.02 0.47 ± 0.02 0.55 ± 0.03 0.09 ± 0.02 2.80 ± 0.06
H80/D20/21O2 0.47 ± 0.05 0.49 ± 0.08 0.57 ± 0.02 0.08 ± 0.07 2.51 ± 0.02
H60/D40/21O2 0.47 ± 0.04 0.44 ± 0.03 0.53 ± 0.03 0.09 ± 0.02 2.41 ± 0.04
H40/D60/21O2 0.47 ± 0.03 0.47 ± 0.01 0.57 ± 0.02 0.09 ± 0.03 3.17 ± 0.03
are comparable to those observed for the 21 vol.% O2 cases. However,
differences in the AHRR profiles exist between the ambient O2 cases
after the end of H 2 injection. Compared to 21 vol.% O2 DF cases, the
15 vol.% O2 DF cases with H2 injection duration longer than n-heptane
(H90/D10, H80/D20, and H60/D40) exhibits slower transitions from
steady AHRR to zero after time of H2 EOI, which is expected with lower
ambient O2. A gradual transition is observed for DF cases with longern-
heptane injection duration compared to H 2 (H40/D60). The DF AHRR
converges to a profile similar to the SF AHRR, exhibiting lower heat
release over a longer period at 15 vol.% O2.
The normalised total heat release data (Fig. 9, second row) shows
that, similar to the 21 vol.% O2 DF cases, the 15 vol.% O2 cases also
exhibit near-complete heat release of the fuel energy content. However,
unlike 21 vol.% O2, total heat release peaks at H80/D20 at 98% and de-
creases to 88% at the lowest H2 energy share of H40/D60. Meanwhile,
H90/D10 total heat release is measured at 95%, a 2% decrease from
that measured at 21 vol O2. A possible explanation is that at 15 vol.%
O2, the ignition timing of n-heptane in the DF case with the shortest
injection duration (H90/D10) occurs close to its EOI. The proximity to
the EOI may lead to local entrainment dynamics being influenced by
the EOI transient [26] to impact the heat release processes. The exact
mechanism requires further investigation to confirm. Nonetheless, all
DF cases still have higher normalised heat release values than that
measured for the SF cases, ranging from 55% to 76%.
The third row of Fig. 9 displays the averaged spatially-integrated
luminosity for the DF cases and their SF counterparts. The luminos-
ity values for the 15 vol.% cases are lower than those observed at
21 vol.% O2 concentration, consistent with the expected less favourable
soot formation processes under lower ambient O2 conditions. The DF
cases show no detected luminosity at H90/D10, the shortest n-heptane
injection duration case, with minimal luminosity also measured for the
SF case. Luminosity becomes detectable only at longer n-heptane in-
jection durations (i.e., higher n-heptane energy share). Consistent with
schlieren observations, the DF cases exhibit less transient luminosity
trends compared to the SF cases, as DF cases with extended n-heptane
injection durations show a quasi-steady period that is not observed in
the SF cases. Similar to the 21 vol.% O2 cases, the luminosity of the DF
cases never reaches the intensity levels measured for SF. On average,

<!-- PDF_PAGE: 10 -->

International Journal of Hydrogen Energy 49 (2024) 1346–1361
1355
P. Rorimpandey et al.
Fig. 8. High-speed schlieren images for energy share cases H90/D10, H80/D20, H60/D40, and H40/D60 under ambient 15 vol.% O2. The corresponding n-heptane only cases at
the same time aSOI are shown at the same frame under the dual-fuel (DF) case. Highlighted are the n-heptane jet boundary (red), H 2 jet boundary (blue), and high-temperature
flame (green). The n-heptane jet boundary averaged from all single-fuel (SF) runs is overlaid on the DF frames (yellow). Axial and radial distances from the injection nozzle are
represented as x and r, respectively. The first frame following H 2 ignition delay time is outlined by a red border. Time sequence is relative to n-heptane SOI. (For interpretation
of the references to colour in this figure legend, the reader is referred to the web version of this article.)
it reaches 60% of the maximum SF luminosity for each case, reflecting
an increased reduction in intensity between DF and SF compared to
the 21 vol.% O2 cases. An outlier is H80/D20/15 O2, reaching 77% of
the maximum SF luminosity. This result could be due to the majority of
soot processes occurring within a timing and spatial range less impacted
by the jet–jet interaction under 15 vol.% O2. However, the relative
reduction in luminosity between SF and DF is still greater than that
observed at 21 vol.% O2.
In the fourth row of Fig. 9 , the averaged and individual flame
recession data obtained from the schlieren images for all DF cases
are presented. Comparing the flame position plots of the 21 vol.%
and 15 vol.% O2 cases, it is evident that the flame recession begins
at a more downstream location relative to the position where the
combustion kernel is first detected in the latter case. While the flame
still recedes towards the nozzle after ignition, similar to the 21 vol.%
O2 cases, it reaches the nozzle after the end of H2 injection at 15 vol.%
O2, stabilising approximately 5 to 7 mm from the nozzle during H 2
injection. As mentioned earlier, the exception is H40/D60, where the
flame still actively recedes to the nozzle at H 2 EOI.
Table 5 presents the n-heptane and H2 ignition delays, the difference
between the two ignition events, and combustion duration CHR90-
CHR10, showing comparable ignition delay timings for n-heptane in
both DF and SF configurations. A comparison of data between Tables 5
and 4 reveals that the difference in ignition delays between n-heptane
and H2 jets at 15 vol.% O2 is longer compared to that at 21 vol.% O2,
while a similar combustion duration is observed under both conditions.
The data also aligns with the observations of the flame position plots
of both cases. The figures show that the flame recession starts at
a more downstream location from the nozzle under lower ambient
O2 conditions, which is consistent with the longer interaction period
required before a more rapid heat release, exceeding the pre-defined
threshold used to indicate H 2 jet ignition. However, once ignition
occurs, a similar combustion duration is observed for both cases.
3.3. Ambient 10 vol.% O2 concentration
Fig. 10 presents selected schlieren images of the DF and SF cases at
a lower ambient condition of 10 vol.% O2 concentration, following the
same convention as Figs. 5 and 8. Comparison of the schlieren images
against the higher ambient O2 cases show that the initial ignition
location emerges alongside the H2 jet boundary at 10 vol.% O2, before
the flame propagates across the H 2 jet. Notably, for DF cases with
longer n-heptane injection durations (H60/D40 and H40/D60), the
flame does not reach the nozzle but stabilises 20–30 mm from H 2
nozzle before H 2 EOI. While the flame similarly stabilises from nozzle
for DF cases with shorter n-heptane injection durations (H90/D10 and

<!-- PDF_PAGE: 11 -->

International Journal of Hydrogen Energy 49 (2024) 1346–1361
1356
P. Rorimpandey et al.
Fig. 9. The averaged AHRR, apparent total heat release, photodiode measured spatially-integrated luminosity, and flame recession for energy share cases H90/D10, H80/D20,
H60/D40, and H40/D60, under ambient 15 vol.% O2 concentration, shown at equal time sequence after n-heptane SOI. Data relating to dual-fuel (DF) or single-fuel (SF) cases
are highlighted by blue or orange lines, respectively, with the H 2 and diesel EOI times shown in each plot. For the fourth row flame position plot, the temporal flame position
from each run is shown by blue dashed lines, with the extracted average flame position highlighted by black lines; the average upstream location of the n-heptane jet kernel is
highlighted by an orange error bar, with start of jet–jet overlap highlighted by a red cross. (For interpretation of the references to colour in this figure legend, the reader is
referred to the web version of this article.)
Table 5
Average n-heptane and H 2 ignition delay times, mean difference between the two ignition events, and combustion duration CHR90-CHR10 for
all dual-fuel (DF) cases at ambient 15 vol.% O2 concentration, relative to n-heptane SOI. Single-fuel (SF) ignition delay provided for reference.
Uncertainty provided as one standard deviation.
Ignition delay times — 15 vol.% O2 concentration
Case Single-fuel Dual-fuel
n-heptane n-heptane H 2 (H2 - n-heptane) CHR90-CHR10
Ignition delay (ms) Ignition delay (ms) Ignition delay (ms) Ignition delay (ms) (ms)
H90/D10/15O2 0.55 ± 0.02 0.58 ± 0.03 0.70 ± 0.03 0.12 ± 0.01 2.83 ± 0.06
H80/D20/15O2 0.61 ± 0.05 0.61 ± 0.03 0.75 ± 0.02 0.14 ± 0.03 2.58 ± 0.07
H60/D40/15O2 0.56 ± 0.04 0.57 ± 0.03 0.71 ± 0.04 0.14 ± 0.01 2.72 ± 0.14
H40/D60/15O2 0.55 ± 0.05 0.55 ± 0.04 0.68 ± 0.03 0.13 ± 0.02 3.34 ± 0.05
H80/D20) before H 2 EOI, the flame does progress further upstream
and eventually lifts approximately 10–15 mm from H2 nozzle, a shorter
H2 flame lift-off compared to H60/D40 and H40/D60. No combustion
retreat is observed for the H 2 jet after H2 EOI.
The reduction in H2 flame lift-off length in shorter n-heptane injec-
tion duration DF cases, where n-heptane EOI occurs before H 2 EOI, is
an important observation, as this suggests that the interaction between
the H2-air mixture and n-heptane combustion products, which extends
to the injector nozzle due to combustion recession within then-heptane
jet, may play a role in reducing the H 2 combustion lift-off length.
Fig. 11 provides schlieren image sequences for DF case H90/D10/10O2
alongside its corresponding SF case, ensemble-averaged across all ex-
perimental runs at equal time sequences, and processed with false
colour to highlight the two jet bodies. Prior to ensemble-averaging,
each frame is subtracted by their preceding frame to remove the
background schlieren patterns. Also shown is the outline representing
the spatial trajectory that the external boundary of the n-heptane jet
occupies over time, as derived from the corresponding SF case, to help
show the change in jet trajectory under DF conditions.
Comparing the DF and SF images at the same time, a noticeable
radial shift of the burnt n-heptane jet towards the H2 jet is observed in
the DF case after n-heptane EOI and during H 2 injection, indicated by
the yellow arrow from 0.57 ms to 2.90 ms. The comparison suggests
that an interaction exists between the actively injecting H 2 jet with
the surrounding low-momentum ambient gases, which consists of com-
bustion products from the burnt n-heptane jet. The entrainment of hot
combustion products and effects of high-temperature, low-density gases
can reduce local strain and turbulence levels of shear flows [55]. Addi-
tionally, this entrainment can ignite the incoming H 2-air charge [55],
contributing to the observed upstream shifting and stabilisation of the
H2 flame lift-off length in cases H90/D10 and H80/D20. The absence
of upstream shifting and stabilisation in the H 2 flame lift-off length
for cases with longer n-heptane injection durations further suggests the
role played by the relative momentum and position of the combustion
products of the jets.
Fig. 12 presents the averaged AHRR, apparent total HR, photodiode,
and flame recession plots for the DF and SF cases at ambient 10 vol.%
O2 concentration, while Table 6 provides the corresponding H 2 and

<!-- PDF_PAGE: 12 -->

International Journal of Hydrogen Energy 49 (2024) 1346–1361
1357
P. Rorimpandey et al.
Fig. 10. High-speed schlieren images for energy share cases H90/D10, H80/D20, H60/D40, and H40/D60 under ambient 10 vol.% O2. The corresponding n-heptane only cases at
the same time aSOI are shown at the same frame under the dual-fuel case. Highlighted are the n-heptane jet boundary (red), H 2 jet boundary (blue), and high-temperature flame
(green). The n-heptane jet boundary averaged from all SF runs is overlaid on the DF frames (yellow). Axial and radial distances from the injection nozzle are represented as x
and r, respectively. The first frame following H 2 ignition delay time is outlined by a red border. Time sequence is relative to n-heptane SOI. (For interpretation of the references
to colour in this figure legend, the reader is referred to the web version of this article.)
n-heptane ignition delays, time difference between the two ignition
events, and CHR90-CHR10 combustion duration.
Notably, the ignition delay timings for n-heptane in the DF cases
remain unchanged compared to the n-heptane-only SF cases, even
though n-heptane seems to ignite closer to the H2 jet boundary at lower
ambient O2 concentrations. This finding indicates that the quenching of
pilot fuel, which has been reported for natural gas jets under dual-fuel
direct injection approaches elsewhere [ 22], was not observed with H 2
jets under the conditions and settings used in this study. The data also
shows that at 10 vol.% O2, the difference in ignition delay between
n-heptane and H2 jets is longer compared to higher ambient O2 levels.
This suggests the presence of a more extended interaction period before
a rapid increase in heat release, used in this study to indicate H 2 jet
ignition, is observed.
The AHRR plots display increased variability at 10 vol.% O2 com-
pared to higher ambient O2 cases. This variability may be attributed to
the longer n-heptane injection duration and a more prolonged jet–jet
interaction period before H 2 jet ignition at 10 vol.% O2, as shown in
Table 6. Consequently, a larger H2 jet region with a leaner equivalence
ratio can be formed, which is less favourable for combustion propaga-
tion, potentially leading to increased AHRR variability. It is nonetheless
recognised that combustion propagation may be more pronounced in
near-stoichiometric regions [56], and lean hydrogen flames can exhibit
rapid burning due to diffusive thermal instability [ 57]. During the
mixing-controlled combustion phase at 10 vol.%O2, especially for cases
H90/D10 and H80/D20, a stabilisation of AHRR is observed, but at
lower magnitudes, approximately 10 kJ/s less than at higher O2 con-
centrations. In cases with longer injection duration, such as H60/D40
and H40/D60, the mixing-controlled combustion phase becomes less
defined, particularly for DF cases with shorter H 2 injection duration,
where ignition occurs closer to the H 2 EOI. Additionally, the larger
mass of H 2 available at ignition, compared to the higher ambient O2
cases, also prolongs the premixed-burn phase. Compared to 21 and
15 vol.% O2, higher fluctuation levels are observed across the AHRR
profile at 10 vol.%O2 for all DF cases. While this may suggest less stable
combustion at lower O2 concentrations, whether this is considered sta-
ble combustion will require further work since the stationary ambient
conditions in the CVCC does not replicate the turbulence experienced
within an engine cylinder that could otherwise influence the overall
combustion stability. The results from this study can only confirm
greater combustion variability at lower ambient O2 concentrations.
Compared to 21 and 15 vol.%O2, higher fluctuation levels are observed
across the AHRR profile at 10 vol.% O2 for all DF cases. While this
may suggest less stable combustion at lowerO2 concentrations, whether
this is considered stable combustion will require further work since
the stationary ambient conditions in the CVCC does not replicate the

<!-- PDF_PAGE: 13 -->

International Journal of Hydrogen Energy 49 (2024) 1346–1361
1358
P. Rorimpandey et al.
Fig. 11. Ensemble-averaged high-speed schlieren images, with false colour, obtained
for the dual-fuel (DF) case H90/D10/10 O2 and the corresponding single-fuel (SF) case.
These images were averaged across all experimental runs at equal time intervals. A red
outline representing the spatial trajectory that the external boundary of the n-heptane
jet follows over time is included to emphasise the change in jet trajectory under DF
conditions. Yellow arrows are used to highlight the radial shift. (For interpretation of
the references to colour in this figure legend, the reader is referred to the web version
of this article.)
turbulence experienced within an engine cylinder that could otherwise
influence the overall combustion stability. The results from this study
can only confirm greater combustion variability at lower ambient O2
concentrations.
The normalised total heat release at ambient 10 vol.% O2 concen-
tration ( Fig. 12 , second row) shows changes in the magnitude and
timing of maximum heat release compared to the 21 and 15 vol.%
O2 cases. Despite these variations, the DF cases still consistently show
higher total heat release values than the SF cases for all energy shares.
The total heat release peaks at an H 2 energy share of 80% (total heat
release of 97%) and decreases with lower H 2 energy share. However,
a drop in total heat release is observed for H90/D10/10O2, decreasing
by 9% compared to 15 vol.% O2. Considering that n-heptane ignition
occurs after its EOI at 10 vol.% O2, this again indicates a poten-
tial influence from the EOI transient. The combustion duration of DF
cases increases as the energy share from n-heptane increases, implying
potential changes to combustion phasing when significant dilution is
present.
At an ambient oxygen concentration of 10 vol.%, the luminosity
values (Fig. 12, third row) are at least an order of magnitude lower
than those observed at higher ambient O2 levels. The low luminosity
observed after autoignition, a characteristic of chemiluminescence [40,
47], indicates minimal or no soot production during combustion at
10 vol.% O2. It is worth noting that there is no visible bright soot
luminosity region in the schlieren images of the 10 vol.% O2 cases.
The flame recession plots in Fig. 12 (fourth row) display the aver-
aged and individual flame recession data obtained from the schlieren
images for all DF cases at 10 vol.% O2. Comparing the flame position
plots at all O2 levels, it is evident that the flame recession initiates
further downstream from the location of the first combustion kernel
detection in cases with lowerO2 concentrations. This suggests that com-
bustion propagates some distance downstream before substantial heat
release occurs, consistent with the earlier assertion that an extended
interaction period before H 2 ignition at lower ambient O2 conditions.
Additionally, at 10 vol.% O2, the flame does not fully retreat to the
nozzle for DF cases but stabilises at various distances from the nozzle,
maintaining a quasi-steady lift-off during H2 injection and not receding
to the nozzle after H 2 EOI. Considering that the mass of fuel in the jet
increases with distance from the injector during steady injection [ 26],
this raises the need to evaluate the possibility of increased engine-out
emissions of unburned fuel when the flame lift-off is located further
downstream, especially when heavy dilution is involved.
4. Summary and conclusions
The following conclusions apply under the conditions investigated
in this study:
1. For the converging setup used in this study, n-heptane ignition
was unaffected by interaction with the H 2 jet, with 𝑛-heptane
consistently igniting external to the H 2 jet boundary. Thus,
quenching of the pilot-fuel when interacting with the gas jet, re-
ported from past studies [21,22], was not observed. However, it
is noted that such an effect cannot be ruled out in configurations
that promote more significant jet–jet interaction.
2. The H 2 jet ignition occurs following a period of interaction
with the burnt products from the diesel surrogate. The duration
of this interaction required is influenced by the ambient O2
concentration, with a longer interaction time necessary before
the H2 jet can ignite under less reactive conditions.
3. Following ignition, the reaction front propagates from the igni-
tion location and spreads across the downstream volume of the
jet, while receding upstream from the ignition spot. The distance
from nozzle to where the flame stabilises depend on ambient
conditions. At 21 vol.% O2, the flame is observed to attach to
the nozzle, but becomes increasingly lifted at lower ambient O2
concentrations. At 15 vol.% O2, the flame lifts around 5 mm
from the H 2 nozzle, increasing to 7 mm for cases with short
n-heptane injection duration. Meanwhile, at 10 vol.% O2, the
lift-off distance ranges from 10 to 30 mm.
4. At 10 vol.%, a shorter flame stabilisation location is observed
in cases where the H 2 injection duration exceeds that of the
diesel surrogate. A potential mechanism is offered based on the
interaction between the H 2 jet and the combustion products
resulting from the recession of the diesel surrogate combustion
near the nozzle region.
5. The schlieren images reveal that, when compared with single-
jet reference cases, the interaction between the two jets can
modify the flow, combustion dynamics, and the associated soot
processes. The ambient O2 concentration also influences these
phenomena.

<!-- PDF_PAGE: 14 -->

International Journal of Hydrogen Energy 49 (2024) 1346–1361
1359
P. Rorimpandey et al.
Fig. 12. The averaged AHRR, apparent total heat release, photodiode measured spatially-integrated luminosity, and flame recession for energy share cases H90/D10, H80/D20,
H60/D40, and H40/D60, under ambient 10 vol.% O2 concentration, shown at equal time sequence after n-heptane SOI. Data relating to dual-fuel (DF) or single-fuel (SF) cases
are highlighted by blue or orange lines, respectively, with the H 2 and diesel EOI times shown in each plot. For the fourth row flame position plot, the temporal flame position
from each run is shown by blue dashed lines, with the extracted average flame position highlighted by black lines; the average upstream location of the n-heptane jet kernel is
highlighted by an orange error bar, with start of jet–jet overlap highlighted by a red cross. (For interpretation of the references to colour in this figure legend, the reader is
referred to the web version of this article.)
Table 6
Average n-heptane and H 2 ignition delay times, mean difference between the two ignition events, and combustion duration CHR90-CHR10 for
all dual-fuel (DF) cases at ambient 10 vol.% O2 concentration, relative to n-heptane SOI. Single-fuel (SF) ignition delay provided for reference.
Uncertainty provided as one standard deviation.
Ignition delay times — 10 vol.% O2 concentration
Case Single-fuel Dual-fuel
n-heptane n-heptane H 2 (H2 - n-heptane) CHR90-CHR10
Ignition delay (ms) Ignition delay (ms) Ignition delay (ms) Ignition delay (ms) (ms)
H90/D10/10O2 0.92 ± 0.04 1.02 ± 0.08 1.32 ± 0.12 0.31 ± 0.09 2.43 ± 0.13
H80/D20/10O2 0.89 ± 0.04 0.91 ± 0.04 1.22 ± 0.16 0.31 ± 0.17 2.64 ± 0.12
H60/D40/10O2 0.90 ± 0.03 0.91 ± 0.04 1.16 ± 0.21 0.25 ± 0.18 3.02 ± 0.21
H40/D60/10O2 0.88 ± 0.02 0.90 ± 0.05 1.18 ± 0.17 0.28 ± 0.14 3.46 ± 0.17
6. The apparent heat release-rate (AHRR) in the dual-fuel case is
mainly influenced by H 2 combustion. When the injection and
combustion periods of H 2 are longer than that of the diesel
surrogate, peak AHRR occurs immediately after H 2 jet igni-
tion, followed by a steady AHRR period until end of H 2 in-
jection, unless the diesel surrogate injection and combustion
duration surpasses premixed combustion, at which the AHRR
profile becomes transient. However, if diesel surrogate injection
and combustion duration exceeds that of H 2, the AHRR profile
eventually converges to a profile that resembles n-heptane-only
combustion. The characteristics of the AHRR profile is further
influenced by the ambient O2 concentration.
7. Simultaneous pressure trace measurements, obtained alongside
optical imaging, show consistently high total heat release in
all dual-fuel cases, despite the injection settings of the diesel
surrogate being optimised to achieve stable combustion and min-
imal fuel quantity necessary for ignition, rather than maximising
fuel–air mixing for heat release.
Declaration of competing interest
The authors declare that they have no known competing finan-
cial interests or personal relationships that could have appeared to
influence the work reported in this paper.
Acknowledgements
The financial support by the Australian Renewable Energy Agency
(ARENA) is gratefully appreciated. The first author acknowledges the
support of the Commonwealth through the Australian Government
Research Training Program Scholarship.
Appendix A. Supplementary data
Supplementary material related to this article can be found online
at https://doi.org/10.1016/j.ijhydene.2023.11.106.

<!-- PDF_PAGE: 15 -->

International Journal of Hydrogen Energy 49 (2024) 1346–1361
1360
P. Rorimpandey et al.
References
[1] Frankl S, Gleis S, Karmann S, Prager M, Wachtmeister G. Investigation of
ammonia and hydrogen as CO2-free fuels for heavy duty engines using a high
pressure dual fuel combustion process. Int J Engine Res 2021;22(10):3196–208.
[2] Bhagat RN, Sahu KB, Ghadai SK, Kumar CB. A review of performance and
emissions of diesel engine operating on dual fuel mode with hydrogen as gaseous
fuel. Int J Hydrogen Energy 2023;48(70):27394–407.
[3] Dimitriou P, Tsujimura T. A review of hydrogen as a compression ignition engine
fuel. Int J Hydrogen Energy 2017;42(38):24470–86.
[4] Verhelst S, Wallner T. Hydrogen-fueled internal combustion engines. Prog Energy
Combust Sci 2009;35(6):490–527.
[5] Hosseini SE, Butler B. An overview of development and challenges in hydrogen
powered vehicles. Int J Green Energy 2019;17(1):13–37.
[6] Wu X, Feng Y, Gao Y, Xia C, Zhu Y, Shreka M, Ming P. Numerical simulation
of lean premixed combustion characteristics and emissions of natural gas-
ammonia dual-fuel marine engine with the pre-chamber ignition system. Fuel
2023;343:127990.
[7] Gong C, Li Z, Yi l, Huang K, Liu F. Research on the performance of a hydro-
gen/methanol dual-injection assisted spark-ignition engine using late-injection
strategy for methanol. Fuel 2020;260:116403.
[8] Tutak W, Grab-Rogaliński K, Jamrozik A. Combustion and emission characteris-
tics of a biodiesel-hydrogen dual-fuel engine. Appl Sci 2020;10(3).
[9] Xia C, Zhu Y, Liu D, Zhou S, Feng Y, Shi J, Jun Y. Newly developed detailed urea
decomposition mechanism by marine engine urea-SCR system crystallization test
and DFT calculations. Chem Eng J 2023;470:144176.
[10] Heywood J. Internal combustion engine fundamentals 2E. McGraw-Hill
Education; 2018.
[11] Lu X, Han D, Huang Z. Fuel design and management for the control of
advanced compression-ignition combustion modes. Prog Energy Combust Sci
2011;37(6):741–83.
[12] Musculus MP, Miles PC, Pickett LM. Conceptual models for partially
premixed low-temperature diesel combustion. Prog Energy Combust Sci
2013;39(2):246–83.
[13] Raheman H, Ghadge S. Performance of diesel engine with biodiesel at varying
compression ratio and ignition timing. Fuel 2008;87(12):2659–66.
[14] Lalsangi S, Yaliwal V, Banapurmath N, Soudagar MEM, Balasubramanian D,
Sonthalia A, Varuvel EG, Wae-Hayee M. Influence of hydrogen injection timing
and duration on the combustion and emission characteristics of a diesel engine
operating on dual fuel mode using biodiesel of dairy scum oil and producer gas.
Int J Hydrogen Energy 2023;48(55):21313–30, Biohydrogen generation from lab
to industry: Challenges and perspectives.
[15] Ishibashi R, Tsuru D. An optical investigation of combustion process of a direct
high-pressure injection of natural gas. J Mar Sci Technol 2017;22(3):447–58.
[16] Rorimpandey P, Yip HL, Srna A, Zhai G, Wehrfritz A, Kook S, Hawkes ER,
Chan QN. Hydrogen-diesel dual-fuel direct-injection (H2DDI) combustion
under compression-ignition engine conditions. Int J Hydrogen Energy
2023;48(2):766–83.
[17] Liu X, Srna A, Yip HL, Kook S, Chan QN, Hawkes ER. Performance and
emissions of hydrogen-diesel dual direct injection (H2DDI) in a single-cylinder
compression-ignition engine. Int J Hydrogen Energy 2020;46(1):1302–14.
[18] Liu X, Seberry G, Kook S, Chan QN, Hawkes ER. Direct injection of hydrogen
main fuel and diesel pilot fuel in a retrofitted single-cylinder compression ignition
engine. Int J Hydrogen Energy 2022;47(84):35864–76.
[19] Sukumaran S, Kong S-C. Numerical study on mixture formation charac-
teristics in a direct-injection hydrogen engine. Int J Hydrogen Energy
2010;35(15):7991–8007, The 10th Chinese Hydrogen Energy Conference.
[20] Rochussen J, McTaggart-Cowan G, Kirchen P. Parametric study of pilot-ignited
direct-injection natural gas combustion in an optically accessible heavy-duty
engine. Int J Engine Res 2020;21(3):497–513.
[21] Fink G, Jud M, Sattelmayer T. Influence of the spatial and temporal interaction
between diesel pilot and directly injected natural gas jet on ignition and
combustion characteristics. J Eng Gas Turb Power 2018;140(10):102811.
[22] Fink G, Jud M, Sattelmayer T. Fundamental study of diesel-piloted natural gas
direct injection under different operating conditions. J Eng Gas Turb Power
2019;141(9):091006.
[23] Gültekin N, Ciniviz M. Examination of the effect of combustion cham-
ber geometry and mixing ratio on engine performance and emissions in a
hydrogen-diesel dual-fuel compression-ignition engine. Int J Hydrogen Energy
2023;48(7):2801–20.
[24] Reitz R, Hessel R, Musculus M. A visual investigation of CFD-predicted in-
cylinder mechanisms that control first- and second-stage ignition in diesel jets.
SAE Pap 2019;2019-01-0543.
[25] Idicheria CA, Pickett LM. Ignition, soot formation, and end-of-combustion
transients in diesel combustion under high-EGR conditions. Int J Engine Res
2011;12(4):376–92.
[26] Knox BW, Genzale CL, Pickett LM, Garcia-Oliver JM, Vera-Tudela W. Com-
bustion recession after end of injection in diesel sprays. SAE Int J Engines
2015;8(2):679–95.
[27] White TR. Simultaneous diesel and natural gas injection for dual-fuelling
compression-ignition engines (Ph.D. thesis), Australia: University of New South
Wales Sydney; 2006.
[28] Suzuki Y, Tsujimura T. The combustion improvements of hydrogen / diesel dual
fuel engine. 2015.
[29] Wu H-W, Wu Z-Y. Investigation on combustion characteristics and emissions of
diesel/hydrogen mixtures by using energy-share method in a diesel engine. Appl
Therm Eng 2012;42:154–62, Heat Powered Cycles Conference, 2009.
[30] Dhyani V, Subramanian K. Control of backfire and NOx emission reduction in
a hydrogen fueled multi-cylinder spark ignition engine using cooled EGR and
water injection strategies. Int J Hydrogen Energy 2019;44(12):6287–98.
[31] Banerjee R, Roy S, Bose PK. Hydrogen-EGR synergy as a promising pathway
to meet the PM–NOx–BSFC trade-off contingencies of the diesel engine: A
comprehensive review. Int J Hydrogen Energy 2015;40(37):12824–47.
[32] Naber J, Siebers D. Hydrogen combustion under diesel engine conditions. Int J
Hydrogen Energy 1998;23(5):363–71.
[33] Zhai G, Xing S, Yuen A, Yeoh GH, Chan QN. Spray and combustion character-
istics of gasoline-like fuel under compression-ignition conditions. Energy Fuels
2020;34(12):16585–98.
[34] Xing S, Zhai G, Mo H, Medwell PR, Yuen AC, Kook S, Yeoh GH, Chan QN.
Study of ignition and combustion characteristics of consecutive injections with
iso-octane and n-heptane as fuels. Energy Fuels 2020;34(11):14741–56.
[35] Fattah IMR, Ming C, Chan QN, Wehrfritz A, Pham PX, Yang W, Kook S, Med-
well PR, Yeoh GH, Hawkes ER, Masri AR. Spray and combustion investigation
of post injections under low-temperature combustion conditions with biodiesel.
Energy Fuels 2018;32(8):8727–42.
[36] Lillo PM, Pickett LM, Persson H, Andersson O, Kook S. Diesel spray ignition
detection and spatial/temporal correction. SAE Int J Engines 2012;5(3):1330–46.
[37] Yip HL, Srna A, Liu X, Kook S, Hawkes ER, Chan QN. Visualiza-
tion of hydrogen jet evolution and combustion under simulated direct-
injection compression-ignition engine conditions. Int J Hydrogen Energy
2020;45(56):32562–78.
[38] Dec JE. A conceptual model of dl diesel combustion based on laser-sheet imaging.
SAE Trans 1997;106:1319–48.
[39] Woo C, Kook S, Rogers P, Marquis C, Hawkes E, Tupufia S. A comparative
analysis on engine performance of a conventional diesel fuel and 10% biodiesel
blends produced from coconut oils. SAE Int J Fuels Lubr 2015;8(3):597–609.
[40] Pickett LM, Kook S, Williams TC. Visualization of diesel spray penetration,
cool-flame, ignition, high-temperature combustion, and soot formation using
high-speed imaging. SAE Int J Engines 2009;2(1):439–59.
[41] Wan Q, Zhai G, Wang C, Yuen AC, Medwell PR, Kook S, Yeoh GH, Chan QN. A
parametric investigation of methane jets in direct-injection compression-ignition
conditions. Fuel 2023;334:126521.
[42] Wan Q, Zhai G, Wang C, Evans MJ, Medwell PR, Yuen ACY, Kook S,
Yeoh GH, Chan QN. Parametric study of autoigniting hydrogen–methane jets
in direct-injection engine conditions. Energy Fuels 2023;37(1):644–56.
[43] Han D, Duan Y, Zhai J. Autoignition comparison of n-dodecane/benzene and
n-dodecane/toluene blends in a constant volume combustion chamber. Energy
Fuels 2019;33(6):5647–54.
[44] Han D, Zhai J, Huang Z. Autoignition of n-hexane, cyclohexane, and
methylcyclohexane in a constant volume combustion chamber. Energy Fuels
2019;33(4):3576–83.
[45] Pickett LM, Siebers DL. Soot in diesel fuel jets: effects of ambient temperature,
ambient density, and injection pressure. Combust Flame 2004;138(1):114–35.
[46] Yip HL, Srna A, Yuen ACY, Kook S, Taylor RA, Yeoh GH, Medwell PR, Chan QN.
A review of hydrogen direct injection for internal combustion engines: towards
carbon-free combustion. Appl Sci 2019;9(22):4842.
[47] Dec JE, Espey C. Chemiluminescence imaging of autoignition in a DI diesel
engine. SAE Trans 1998;107:2230–54.
[48] Qamar NH, Nathan GJ, Alwahabi ZT, Chan QN. Soot sheet dimensions in
turbulent nonpremixed flames. Combust Flame 2011;158(12):2458–64.
[49] Escudero F, Demarco R, Cruz J, Verdugo I, Carvajal G, Olivares G, Valen-
zuela F, Han D, Lin H, Fuentes A. Determining spatially-resolved thermal
radiation from non-intrusive measurements of soot properties. Appl Therm Eng
2022;215:118968.
[50] Yip HL, Srna A, Zhai G, Wehrfritz A, Kook S, Hawkes ER, Chan QN. Laser-
induced plasma-ignited hydrogen jet combustion in engine-relevant conditions.
Int J Hydrogen Energy 2023;48(4):1568–81.
[51] Subramanian G, Pires Da Cruz A, Bounaceur R, Vervisch L. Chemical impact of
CO and H2 addition on the auto-ignition delay of homegeneous n-heptane/air
mixtures. Combust Sci Technol 2007;179(9):1937–62.
[52] Comandini A, Chaumeix N, Maclean J, Ciccarelli G. Combustion properties of
n-heptane/hydrogen mixtures. Int J Hydrogen Energy 2019;44(3):2039–52.

<!-- PDF_PAGE: 16 -->

International Journal of Hydrogen Energy 49 (2024) 1346–1361
1361
P. Rorimpandey et al.
[53] Guo H, Neill WS. The effect of hydrogen addition on combustion and emission
characteristics of an n-heptane fuelled HCCI engine. Int J Hydrogen Energy
2013;38(26):11429–37.
[54] An H, Chung J, Lee S, Song S. The effects of hydrogen addition on the auto-
ignition delay of homogeneous primary reference fuel/air mixtures in a rapid
compression machine. Int J Hydrogen Energy 2015;40(40):13994–4005.
[55] Pickett LM, Kook S, Persson H, Andersson Ö. Diesel fuel jet lift-off stabi-
lization in the presence of laser-induced plasma ignition. Proc Combust Inst
2009;32(2):2793–800.
[56] Borghesi G, Krisman A, Lu T, Chen JH. Direct numerical simulation of a tempo-
rally evolving air/n-dodecane jet at low-temperature diesel-relevant conditions.
Combust Flame 2018;195:183–202, Special Commemorative Issue: Professor
Chung King (Ed) Law 70th Birthday.
[57] Huang Z, Zhang Y, Zeng K, Liu B, Wang Q, Jiang D. Measurements of
laminar burning velocities for natural gas–hydrogen–air mixtures. Combust Flame
2006;146(1):302–11.
