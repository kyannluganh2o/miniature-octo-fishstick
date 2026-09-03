<!-- PDF_PAGE: 1 -->

Hydrogen-diesel dual-fuel direct-injection (H2DDI)
combustion under compression-ignition engine
conditions
Patrick Rorimpandey a, Ho Lung Yip a, Ale /C20s Srna b, Guanxiong Zhai a,
Armin Wehrfritz c, Sanghoon Kook a, Evatt R. Hawkes a,
Qing Nian Chan a,*
a School of Mechanical and Manufacturing Engineering, The University of New South Wales, NSW, 2052, Australia
b Combustion Research Facility, Sandia National Laboratories, Livermore, CA, 94551, USA
c Mechanical Engineering, University of Turku, Turun Yliopisto, FI-20014, Finland
article info
Article history:
Received 9 June 2022
Received in revised form
20 September 2022
Accepted 25 September 2022
Available online 19 October 2022
Keywords:
Hydrogen
Dual fuel
Direct injection
Compression-ignition engine
abstract
This study investigates the ignition and combustion characteristics of interacting diesel-
pilot and hydrogen (H
2) jets under simulated compression-ignition engine conditions.
Two converging single-hole injectors were used to inject H 2 and diesel-pilot jets into an
optically accessible constant-volume combustion chamber (CVCC). The parameters varied
include fuel injection sequence, timing between injections, and ambient temperature (780
e890 K). The results indicate that when diesel-pilot is injected before H
2, with increasing
time separation, the burnt diesel products mix and cool down, requiring longer jet-jet
interaction to ignite the H
2 jet. When H 2 is injected before diesel-pilot, the H 2-air mixing
amount prior to pilot-fuel igniting impacts the combustion spreading through the H 2 jet. If
ignition of the H 2 jet occurs beyond its end-of-injection (EOI), the H 2 mixture zone where
the pilot-diesel interacts with becomes too lean for combustion. At lower ambient tem-
peratures, the combustion variability increases, attributed to the diesel-pilot lean out.
© 2022 The Authors. Published by Elsevier Ltd on behalf of Hydrogen Energy Publications
LLC. This is an open access article under the CC BY-NC-ND license ( http://
creativecommons.org/licenses/by-nc-nd/4.0/).
Introduction
Hydrogen (H 2) is considered a potential energy carrier in
transportation powertrains because of its carbon-neutral and
renewable potential [ 1e3]. As a fuel in internal combustion
engines (ICE), the wide ﬂammability limit (4 e76 vol% in air)
and high laminar ﬂame speed of H
2 (1.85 m/s in air a,c,d)1 result
in a short combustion duration even under very lean opera-
tion, which increases the thermal efﬁciency [ 1,4,5].
Nonetheless, the low volumetric density and minimum igni-
tion energy of H
2 pose challenges for traditional H 2 ICE ap-
plications with port fuel injection. Due to the low volumetric
energy content (10.7 MJ/m 3 a,b ), the engine volumetric efﬁ-
ciency is reduced. Despite a high autoignition temperature
(858 K [ 6]), the low minimum ignition energy of H
2 (0.02 mJ a,d)
[4,6] increases the pre-ignition tendency of H 2 by hot spots or
residues within the engine chamber, leading to a loss of
combustion phasing control, knocking and possible mechan-
ical engine failure [ 1,7]. The short quenching distance of H
2
* Corresponding author .
E-mail address: qing.chan@unsw.edu.au (Q.N. Chan).
1 a at 1 bar, b at 273 K, c at 298 K and d at stoichiometry.
Available online at www.sciencedirect.com
ScienceDirect
journal homepage: www.elsevier.com/locate/he
international journal of hydrogen energy 48 (2023) 766 e783
https://doi.org/10.1016/j.ijhydene.2022.09.241
0360-3199/© 2022 The Authors. Published by Elsevier Ltd on behalf of Hydrogen Energy Publications LLC. This is an open access article under the CC BY-NC-ND
license ( http://creativecommons.org/licenses/by-nc-nd/4.0/).

<!-- PDF_PAGE: 2 -->

(0.64 mm a,c,d), combined with its high laminar ﬂame speed,
implies an increased backﬁring risk into the intake manifold,
and higher temperature gradients near the cylinder wall that
increases heat loss and engine oil consumption.
Various in-cylinder mixture preparation and ignition pro-
cesses have been studied previously, and direct injection (DI)
of H
2 was shown to alleviate backﬁring, pre-ignition, and
volumetric efﬁciency loss challenges associated with port and
manifold injection approaches [ 1,4,8]. The requirement of an
additional ignition source was noted since the high H 2 auto-
ignition temperature requires intake-air preheating or
impractical compression ratio (CR) of >26e42 for reliable
compression ignition (CI) [ 9,10]. Different ignition options
include spark discharge ignition [11e13], hot surface [14,15], or
pilot-fuel ignition (dual-fuel) [16e18,54]. This study focuses on
the dual-fuel combustion approach, which involves creating a
high-temperature environment via diesel-fuel combustion to
ignite the H
2 main fuel. The dual-fuel approach was success-
fully commercialized for natural-gas engines, where excep-
tional combustion stability was demonstrated, aside from the
operational ﬂexibility as such engines can operate on diesel
fuel only if needed [ 19e21]. Some dual-fuel engines operate
with early main fuel injection to create a homogeneous or
moderately stratiﬁed gaseous fuel mixture ignited by a pilot
fuel injection near TDC, with ﬂame propagation as the domi-
nant combustion mechanism [ 22]. Such engines typically
exhibit good efﬁciency and low pilot-fuel consumption [23,24],
but do not entirely eliminate the pre-ignition issues. Late
high-pressure main-fuel injection is a more robust approach
for dual-fuel H
2 engine applications. In this concept, the main-
fuel and pilot-fuel are injected near the TDC, and diffusion
combustion is the dominant fuel conversion process [ 20].
The H
2-diesel dual-fuel direct-injection (H2DDI) mode is a
relatively novel approach with limited experimental or nu-
merical studies. However, previous studies utilising natural
gas as the main fuel identiﬁed various factors that will likely
affect the ignition and combustion processes of H2DDI. The
relative orientation between the injectors dwhich can be
categorized as diverging (the injectors are directed away from
Fig. 1 e (a) Cross-section schematic of the constant-volume
combustion chamber. (b) Detailed view of the H 2 and diesel
injector layouts, showing symbolic H 2 (blue) and n-heptane
jet cones (red), with the points of jet axis and cone
intersection. (For interpretation of the references to colour
in this ﬁgure legend, the reader is referred to the Web
version of this article.)
Fig. 2 e Sample CVCC pressure trace data during an
experiment run. Starting at spark ignition, it highlights the
following four key events: (i) premixed ambient gas
combustion, (ii) cool-down period, (iii) start of fuel injection
and (iv) fuel ignition.
Table 1 e Summary of the experimental conditions. Bold
values are the reference conditions.
CVCC Ambient Conditions
Wall temperature (K) 403
Ambient O 2 concentration (vol%) 21
Ambient gas density (kg/m 3) 23.8
Ambient gas pressure (MPa) 5.20, 4.60, 4.45
Ambient core gas temperature (K) 890, 820, 780
international journal of hydrogen energy 48 (2023) 766 e783 767

<!-- PDF_PAGE: 3 -->

each other), parallel (the injector axes are aligned) or
converging (the injector axes intersect downstream) [ 25]dcan
affect fuel interaction and the ensuing combustion process.
There are several studies of the effects of jet orientation on the
combustion processes. Li et al. [ 21] reported a statistical cor-
relation between the combustion instabilities of their engine
performance tests with the changing spatial interaction be-
tween the pilot diesel and natural gas jets that their integrated
two-fuel HDPI multi-hole injector produced. More recent
studies by Fink et al. [26,27] provided direct visualisation of the
dependency of ignition and combustion processes on the
spatial jet interaction, which showed improved ignition with
converging jet arrangements, especially at low ambient tem-
perature. It is noteworthy that other studies have shown that
the pilot-fuel entrainment into the main-fuel jet can quench
the pilot-fuel autoignition [ 26e28].
Previous natural-gas dual-fuel studies also showed the
importance of the fuel injection sequence (pilot-fuel or main-
fuel injected ﬁrst, and the associated dwell time) on com-
bustion stability, peak AHRR, and combustion noise. It was
demonstrated that the combustion noise and peak apparent
heat release rate (AHRR) are reduced when the main-fuel is
ignited as early after injection as possible, which occurs when
pilot-fuel is injected somewhat before the main injection
[20,26,29,30]. This is associated with the minimal degree of
main-fuel premixing at the time of ignition by the pilot fuel. At
other dwell times, the interaction of main fuel with pilot is
delayed (main fuel injected before pilot), or the pilot-fuel burnt
gases cool down due to mixing (pilot injected long before
main). Both cases delay the main-fuel ignition and increase
the AHRR. At more extreme timings, the ignition and com-
bustion become unstable, resulting in lower AHRR and high
cyclic variability [ 26].
Despite the wealth of available literature or existing
studies on the natural-gas dual-fuel engines, there is a
considerable knowledge gap in the interplay between injector
conﬁguration, ambient condition and fuel-air premixing
speciﬁc to H
2 dual-fuel combustion. Under the assumption
that maximising the overlap between the fuel jets yields the
best ignition performance, a converging setup using two
single-hole injectors is used in this study. The effects of in-
jection sequence, injection timing, and ambient gas
temperature on the H2DDI ignition and combustion pro-
cesses under DI CI engine relevant conditions are assessed.
H
2 and n-heptane as a diesel surrogate were injected into a
quiescent high-temperature, high-pressure charge within an
optically accessible constant-volume combustion chamber
(CVCC). Experimental diagnostics include high-speed
schlieren imaging and pressure measurements.
Experimental details
Constant-volume combustion chamber
The experiments were conducted in an optically accessible
CVCC with a quiescent high-pressure, high-temperature
charge representative of CI engine conditions. The chamber is
cubical with side dimensions of 114 mm, incorporating six
interchangeable ports at the chamber faces. To avoid water
condensation from the combustion products, the walls were
kept at 403 K throughout the experiments. The H
2 and diesel
injectors were installed in one side port, and a ﬂat metal wall
was installed in the opposite port. A mixing fan was installed
in the top port to homogenize the ambient charge. Sapphire
glass windows with 101.6 mm clear aperture were ﬁtted in the
remaining three ports (bottom port and ports perpendicular to
the injector) to allow optical access. Fig. 1 (a) shows a sche-
matic of the CVCC setup.
The pre-burn procedure for reaching high-pressure, high-
temperature conditions in this CVCC has been detailed in
Refs. [ 31e33,53]. In summary, a compressed lean mixture of
C
2H2,H 2,O 2 and N 2 was spark ignited to increase the in-
chamber pressure and temperature, followed by a cool-
down period as the heat is transferred to the surrounding
chamber walls. The in-chamber pressure was monitored via a
Table 2 e Summary of injection conditions and fuel
properties [4,16,37].
Fuel Injection Conditions
Fuel n-heptane H 2
Nozzle diameter (mm) 0.105 0.58
Fuel reservoir pressure (MPa) 70 20
Electronic injection command duration (ms) 0.4 3.0
Hydraulic injection duration (ms) 0.7 3.3
Mass injected (mg) 0.99 5.28
Low. heat. value [ 38] (MJ/kg) 43.2 120.0
Energy (J) 43.2 633.6
Total energy (J) 676.8
Energy share (%) 6.4 93.6
Research octane number (RON) 0 130
Cetane number 56 e
Density at 293.15 K (kg/m
3) 680 0.09
Auto-ignition temperature (K) 493.15 856
Fig. 3 e A schematic of the combustion vessel and the
high-speed schlieren imaging optical arrangement. The
light path (transparent yellow) from the schlieren imaging
light source and a model of the penetrating jet (red) are
shown. (For interpretation of the references to colour in
this ﬁgure legend, the reader is referred to the Web version
of this article.)
international journal of hydrogen energy 48 (2023) 766 e783768

<!-- PDF_PAGE: 4 -->

piezoelectric pressure transducer (Kistler 6052C with ampliﬁer
5015A) to trigger the fuel injection event once the target in-
chamber pressure (and hence temperature) condition was
achieved during the cool-down phase. Fig. 2 shows the pres-
sure history during a typical experiment run. For this study,
the partial-pressure metered composition was tailored to
achieve 21 vol% O
2 concentration after the pre-combustion,
with an ambient density set to 23.8 kg/m 3.
The ambient temperature in the geometrical centre of
the CVCC during the pre-combustion event was character-
ized using a thin-wire K-type thermocouple and is adopted
as the representative charge temperature in this study. A
baseline condition ambient temperature was set at 890 K,
achieved by setting the target in-chamber pressure at SOI to
5.2 MPa. Lower ambient temperatures of 820 K and 780 K
(4.6 MPa and 4.45 MPa, respectively) were used to investigate
dual-fuel combustion under cooler temperature conditions
(Section 2.5). Table 1 summarizes the experimental condi-
tions. The H
2 ignition delay under tested conditions is
considerably longer than that of n-heptane [ 34,35]. There-
fore, it is reasonable to assume that the ignition of H 2 jet
occurs due to its interaction with reacting or burnt n-hep-
tane jet.
Injection settings
Two single-hole injectors with a converging conﬁguration
were used to separately inject the H
2 and diesel-pilot into the
CVCC. Single-hole injectors were used instead of multi-hole
injectors to simplify interpretation of experiments and avoid
the complexities that arise from multiple jet interactions from
the same injector. As shown in Fig. 1 (a), the H
2 injector was
positioned at the centre of the port aligned with the port axis.
The diesel injector oriﬁce was positioned 12.3 mm above the
H
2 injector oriﬁce, at 12/C14 relative to the H2 injector axis. The jet
axes intersect at 57.2 mm distance from the H 2 nozzle.
Schlieren imaging suggests the jets start to interact as close as
28 mm from the H
2 injector or even closer when the diesel-
pilot is injected before H 2 (see Section 3.2). Neat n-heptane
was used as a single-component diesel-pilot fuel surrogate to
reduce any compositional complexity and variables that can
arise from using commercial fuels. Use of high cetane-number
(low-octane) fuel is desired for the pilot-fuel to serve as a
repeatable and reliable ignition source. The n-heptane fuel
was injected at 70 MPa rail pressure using a commercial
common rail injector (Bosch, solenoid, generation 2) equipped
with a custom single-hole nozzle. The H
2 injector was derived
from a modiﬁed commercial gasoline direct-injection (GDI,
Bosch, HDEV5.1) injector that was ﬁtted with a 0.58 mm single-
hole diameter nozzle attachment [ 34]. The H
2 injector was
supplied with compressed H 2 from a 1 dm 3 pressurized
reservoir, which was charged using a pneumatic H 2
Fig. 4 e (a) Sample raw schlieren high-speed image, (b)
image corrected by subtracting the pixel intensity values
from the previous frame and (c) processed image showing
the unreacted n-heptane (red) and H
2 (blue) jets, and
reacted region (green). (For interpretation of the references
to colour in this ﬁgure legend, the reader is referred to the
Web version of this article.)
Table 3 e Summary of the investigated cases, their
experimental settings and corresponding notations. Bold
texts are the reference conditions.
Cases Investigated
Case Name Dwell Time Ambient
Pilot Main Temperature
H-0.07 ms-D/890K 0.07 ms - 890 K
D-0.93 ms-H/890K e 0.93 ms 890 K
D-1.93 ms-H/890K e 1.93 ms 890 K
D-2.93 ms-H/890K e 2.93 ms 890 K
H-1.07 ms-D/890K 1.07 ms e 890 K
H-2.07 ms-D/890K 2.07 ms e 890 K
H-3.07 ms-D/890K 3.07 ms e 890 K
H-0.07 ms-D/820K 0.07 ms e 820 K
H-0.07 ms-D/780K 0.07 ms e 780 K
Experimental Parameters
Parameter Cases Investigated
Pilot-Main
Injection Strategy
H-0.07 ms-D/890K
D-0.93 ms-H/890K
D-1.93 ms-H/890K
D-2.93 ms-H/890K
Main-Pilot
Injection Strategy
H-0.07 ms-D/890K
H-1.07 ms-D/890K
H-2.07 ms-D/890K
H-3.07 ms-D/890K
Lower Ambient
Gas Temperature
H-0.07 ms-D/890K
H-0.07 ms-D/820K
H-0.07 ms-D/780K
international journal of hydrogen energy 48 (2023) 766 e783 769

<!-- PDF_PAGE: 5 -->

compressor (Haskel with Zenobalti pressure controller). A
reservoir pressure of 20 MPa was set, which resulted in
roughly 14 MPa H 2 pressure upstream of the nozzle as a result
of friction losses associated with the passage of gas through
narrow channels within the injector [ 34].
The H
2 and n-heptane injectors were energized by inde-
pendent external injector drivers (Zenobalti ZB-5012 and ZB-
5014, respectively) with the timing set by a digital delay and
pulse generator (Stanford Research Systems DG535). The hy-
draulic injection duration of H
2 and n-heptane were set to
3.3 ms and 0.7 ms, respectively, taking into account the delays
associated with the opening and closing of the nozzles, and
back pressure effects. The n-heptane mass ﬂow was measured
under nominally identical conditions using a Bosch-tube in-
jection rate meter [ 36]. The injected amount of H
2 gas was
determined by measuring the chamber pressure change when
H
2 was injected [ 34]. Under the tested conditions, the injected
fuel mass was 0.99 mg for n-heptane and 5.28 mg for H2. Based
on the fuels heating value, this means 6.4% of the energy share
is from the n-heptane jet, with the rest from the H
2. Table 2
summarizes the experimental fuel injection conditions.
Optical diagnostics
Fig. 3 shows a schematic of the experimental optical
arrangement. A Z-type schlieren imaging setup was used to
detect the jet boundary and the high-temperature reaction
zone. The roughly collimated light from a 150 W xenon arc
lamp (Abet Technologies LS-150) was focused using a 50 mm
plano-convex lens with a 75 mm focal length, which was then
passed through a 2 mm aperture before collimation via a
108 mm f/6 parabolic mirror. The collimated light beam was
directed through the CVCC, a second parabolic mirror, then
into the high-speed camera through a series of mirrors. A
2 mm pin-hole aperture was placed between the second
parabolic mirror and the camera lens at the beam focal point
to enhance imaging sensitivity. The high-speed camera used
is a Photron Fastcam SA5 equipped with an 85 mm f#1.8 AF-D
Nikkor lens, operated at a 30,000 frames per second frame rate
and a 1/525,000 s shutter speed, resulting in an image reso-
lution of about 0.15 mm per pixel.
Schlieren imaging is an optical technique that is sensitive
to refractive index gradients along the line-of-sight, induced
by fuel evaporative cooling, mixing and combustion events,
which are detectable as intensity variations on the image [ 32].
A high-temperature combustion event results in a steep
refractive index gradient that can be identiﬁed as a darkened
area on the schlieren image, as shown in Fig. 4 (a). The
ambient gas (and hence the background schlieren pattern)
was relatively stationary compared to the effects induced by
the fast-moving jet. Therefore, the jet-induced schlieren ef-
fects can be discerned from the background structures by
tracking the differences between video frames [ 39], as shown
in Fig. 4 (b). The identiﬁed boundaries of the unreacted H
2
(blue) and n-heptane jets (red), along with the darkened burnt-
zone region (green) are shown Fig. 4 (c).
Pressure trace and apparent heat release rate
In addition to the optical diagnostics, the pressure trace
measurements acquired during the experiments were used to
derive the AHRRs, to aid with the interpretation of results. For
this study, we focus on the AHRR shape and features, which
could be smeared by ensemble averaging in case of ignition
delay variability. As a mitigation, before ensemble averaging,
individual AHRR traces were shifted in time by the difference
between the individual experiment realization ignition delay
and the mean ignition delay. The following ensemble aver-
aging formula was used:
AHRR
________
ðtÞ¼ 1
n
Xn
i¼1
AHRRiðt þ tID;i /C0 tID
___
Þ (1)
Fig. 5 e Schlieren-based ignition delay times of n-heptane
at ambient temperatures of 780 K, 820 K and 890 K, with
standard deviation shown as error bars.
Table 4 e Average schlieren-based ignition delay time, the average times where 10% and 90% of the total heat release
occurs (notated as CA10 and CA90, respectively), and the corresponding combustion duration of n-heptane at ambient
temperatures of 890 K, 820 K and 780 K. Uncertainty provided as one standard deviation.
Ignition Delay and Combustion Duration of n-heptane
Core temperature Pilot ignition delay
schlieren-based (ms)
CA10 (ms) CA90 (ms) Combustion duration
CA10eCA90 (ms)
890 K 0.62 ± 0.04 0.79 ± 0.05 1.72 ± 0.40 0.93 ± 0.35
820 K 0.93 ± 0.05 0.91 ± 0.07 2.39 ± 0.41 1.48 ± 0.47
780 K 1.68 ± 0.12 1.10 ± 0.15 5.25 ± 1.37 4.15 ± 1.52
international journal of hydrogen energy 48 (2023) 766 e783770

<!-- PDF_PAGE: 6 -->

where n denotes the total number of cycles, tID the ignition
delay and the overline signiﬁes ensemble-averaged
quantities.
Experimental parameters and notations
The H2DDI combustion process was investigated under:
/C15 Pilot-main injection strategy, where the pilot fuel ( n-hep-
tane) is injected prior to the main-fuel (H 2) start-of-
injection (SOI).
/C15 Main-pilot injection strategy, where the main fuel is injec-
ted before the pilot-fuel SOI.
This work uses the “pilot” and “main” fuel nomenclature
widely used in dual-fuel combustion research, where “pilot-
fuel” refers to the injection of diesel-like fuel serving as
ignition source and “main-fuel” refers to the low ignition
quality fuel that contributes the largest share of fuel LHV.
This nomenclature is not to be confused with pilot and main
injection in multiple-injection diesel engines.
Table 5 e Average pilot and main ignition delay times, relative to pilot-fuel and main-fuel SOI, for the reference case and
pilot-main injection cases. Bold text indicates the reference case. The pilot ignition delay time relative to main-fuel SOI is
omitted when the pilot-fuel autoignites prior to main-fuel SOI. Uncertainty provided as one standard deviation.
Ignition Delay Times
Case name Relative to pilot-fuel SOI Relative to main-fuel SOI
Pilot (ms) Main (ms) Pilot (ms) Main (ms)
H-0.07 ms-D/890K 0.62 ±0.03 0.63 ±0.04 0.69 ±0.03 0.70 ±0.04
D-0.93 ms-H/890K 0.58 ± 0.09 1.19 ± 0.09 e 0.26 ± 0.09
D-1.93 ms-H/890K 0.69 ± 0.03 2.30 ± 0.05 e 0.36 ± 0.05
D-2.93 ms-H/890K 0.66 ± 0.03 3.43 ± 0.14 e 0.49 ± 0.13
Fig. 6 e Processed schlieren images at select timings for n-heptane only injection, at ambient temperatures of 890 K (left),
820 K (middle), and 780 K (right). Overlaid are the unreacted n-heptane jet boundary (red) and the burn zone (green). Axial
and radial distances from the H 2 injection nozzle are represented as x and r, respectively. (For interpretation of the
references to colour in this ﬁgure legend, the reader is referred to the Web version of this article.)
international journal of hydrogen energy 48 (2023) 766 e783 771

<!-- PDF_PAGE: 7 -->

The dwell time, deﬁned as the time between the primary
and secondary actual SOI timings, was varied to investigate its
effect. The fuel to which the dwell time refers depends on the
parameter investigated. For a pilot-main case, the dwell time
refers to the main-fuel SOI relative to the time after pilot-fuel
SOI, and vice versa for a main-pilot case. As noted previously,
the dwell time was set externally using a signal generator.
Taking into account the electronic command delays and the
actual opening and closing of the H
2 and diesel nozzles, dwell
times of 0.93 ms, 1.93 ms and 2.93 ms were used for pilot-main
cases, and dwell times of 1.07 ms, 2.07 ms and 3.07 ms were
used for main-pilot cases. A near-simultaneous dual-injection
case, where the pilot fuel was injected 0.07 ms after main-fuel
SOI, was performed and used as a reference to compare re-
sults when investigating each parameter. In addition to the
baseline ambient temperature of 890 K, the near-
simultaneous dual-injection case was also tested under
lower ambient temperatures of 820 K and 780 K. Furthermore,
n-heptane only injection cases were also conducted in the
three ambient temperatures as a reference. Each experi-
mental case was repeated at least four times to eliminate
outliers.
Table 3 summarizes the investigated cases, their settings
and notations. For this study, the notation system adopted
lays out the dwell time between the two fuels and the ambient
temperature condition, with abbreviations of the diesel pilot
(D) and H
2 main fuel (H) placed in the order of the injection
sequence. For example, a main-pilot case with a dwell time of
1.07 ms and ambient temperature of 890 K is notated as ‘H-
1.07 ms-D/890K’, while a pilot-main case with a dwell time of
0.93 ms at the same ambient temperature is notated as ‘D-
0.93 ms-H/890K’.
Ignition delay: pilot and main ignition
There may be two separate ignition events in dual-fuel com-
bustion: the pilot-fuel autoignition and the main-fuel ignition
that occurs after the jet interacts with the burnt pilot fuel.
When separate ignition events occur, they are referred to as
“pilot ignition” and “main ignition”, respectively.
For this study, the pilot ignition is deﬁned as the auto-
ignition of n-heptane. While the autoignition of n-heptane
leads to a distinct rise in the pressure trace at 890 K, the
pressure rise becomes less deﬁned at lower temperatures.
This creates difﬁculty in identifying the pilot-ignition event
from the pressure trace alone. Additionally, during the dual-
fuel combustion, for the events where the pilot- and main-
ignition events occur in close succession, only a single rise
in the pressure trace can be detected. This prevents the
discernment of the two ignition events and their ignition
delay timings. For consistency reasons, high-speed schlieren
images are used to determine the timing of the pilot ignition
for all experimental cases. The pilot-ignition delay time is
derived from the schlieren image frame where darkened high-
temperature region ﬁrst appears within the n-heptane jet.
For the dual-fuel cases, the schlieren effects from burnt
pilot fuel obscures the main-fuel ignition, preventing an opti-
cal evaluation of the main ignition delay. Noting that a bulk of
the heat release occurs during the main ignition, main-ignition
time is derived based on the AHRR using thresholds, more
precisely, the main ignition delay time was pinpointed as the
latest time of AHRR not exceeding 18 kJ/s (above the noise ﬂoor
of the AHRR data) before the 100 kJ/s was reached. This is
motivated by the peak AHRR of pilot-only injections not
exceeding 80 kJ/s. Note that by the above deﬁnition, in some
instances, the main ignition is not strictly just the H
2 ignition,
-20
0
20
40
60
80AHRR (kJ/s)
890 K
-20
0
20
40
60
80AHRR (kJ/s)
820 K
0246
Time aSOI (ms)
-20
0
20
40
60
80AHRR (kJ/s)
780 K
Average
Uncertainty
CA10
CA90
Fig. 7 e Averaged AHRR proﬁles for n-heptane only
injection cases at ambient temperatures of 890 K (top),
820 K (middle) and 780 K (bottom). The average times
where 10% and 90% of the total heat release occur (notated
as CA10 and CA90, respectively) are plotted as blue and red
dashed lines, respectively, with standard deviation shown
along the time-axis. (For interpretation of the references to
colour in this ﬁgure legend, the reader is referred to the
Web version of this article.)
international journal of hydrogen energy 48 (2023) 766 e783772

<!-- PDF_PAGE: 8 -->

as the heat release from n-heptane autoignition also contrib-
utes if the two ignition events occur in quick succession.
Results and discussion
Combustion characteristic of n-heptane
The n-heptane combustion (in the absence of H 2) was char-
acterized at different ambient temperatures in terms of igni-
tion delay, burnt-zone evolution and AHRR. Fig. 5 and Table 4
present the average and standard deviation of schlieren-based
ignition delay of n-heptane at various ambient temperatures
relative to different SOI timings. The ignition delay of n-
heptane increases with lower temperature [ 40], increasing by
a factor of 2.8 as the temperature decreases.
Fig. 5 shows ignition occurs before the EOI at the highest
temperature ( i.e. negative ignition dwell [ 41]). This is note-
worthy since aEOI, the entrainment wave rapidly leans out the
jet, which was shown to impact the jet ignition relative to a
longer injection [ 42] and change the burnt gas temperature
that the interacting H
2 jet will experience.
Fig. 6 provides sample schlieren images for n-heptane-only
case, highlighting the unreacted jet (red) and the ﬂame (green)
development at different temperatures. The main difference
is in the ignition location and the spreading rate of combus-
tion from the initial ignition spot - both of these effects can
impact the main-fuel ignition. At 890 K, the autoignition
Fig. 8 e Processed schlieren images at select time instants for (a) reference case H-0.07 ms-D/890K, and pilot-main injection
cases (b) D-0.93 ms-H/890K, (c) D-1.93 ms-H/890K and (d) D-2.93 ms-H/890K. Highlighted are the n-heptane jet boundary
(red), H 2 jet boundary (blue), and high-temperature ﬂame (green). Axial and radial distances from the injection nozzle are
represented as x and r, respectively. The ﬁrst frame following pressure-based ignition delay time is outlined by a red border.
Time sequence is relative to the earlier injection ( i.e., n-heptane SOI). (For interpretation of the references to colour in this
ﬁgure legend, the reader is referred to the Web version of this article.)
international journal of hydrogen energy 48 (2023) 766 e783 773

<!-- PDF_PAGE: 9 -->

occurred at the jet head prior to the separate ignition spot aEOI
in the near-nozzle jet tail. The two ignited regions merged
over time. A similar ignition process was observed at 820 K,
but the two ignited regions did not combine within the
observation period. At 780 K, the ignition only occurred aEOI
near the nozzle and failed to spread. The mixture in the jet
head has the longest residence time in the hot environment
and initially a favourable fuel-to-air ratio [ 43], however, it
rapidly leans out after EOI. This is why this region is the ﬁrst to
autoignite at 890 K, but becomes too lean to autoignite at
780 K. Regions near the injector may remain fuel-richer longer
due to the EOI ramp-down and the injector needle-bouncing
injecting low-velocity droplets. These can lead to separate
ignition pockets [44] visible near-nozzle at 890 K and 820 K and
the sole source of ignition at 780 K.
The pilot-only ignition timing and combustion phases are
evaluated based on AHRR ( Fig. 7 )[ 12,34,45]. The peak AHRR
decreases by a factor of 2 from 890 K to 820 K, while no AHRR
peak is distinguishable from the AHRR proﬁle at 780 K. These
trends are contrary to the traditional long-injection diesel
combustion with increasing premixed peak at a longer igni-
tion delay; this indicates that the studied pilot-injections
become signiﬁcantly lean before ignition, which reduces the
overall fuel reactivity and slows the combustion.
The cyclic variability of the pressure-derived AHRR (shaded
region, ±1 standard deviation) is low at higher temperatures,
while the AHRR cannot be distinguished from noise at 780 K.
Fig. 7 shows the timings where 10% (CA10) and 90% (CA90) of
the cumulative heat release occur, analogous to typical engine
study notations, serving as reference for the parametric vari-
ation results presented next. Table 4 provides the ignition
delay and combustion duration (deﬁned as the time between
CA10 and CA90), showing that the time of CA10, CA90 and
combustion duration increase with decreasing ambient tem-
perature, with increased cyclic variability.
Pilot-main injection strategy
Injecting the pilot fuel before the main-fuel SOI allows the
pilot jet to develop before interacting with the main jet. In all
tested pilot-main injection cases with a dwell time of 0.93 ms
after n-heptane SOI (D-0.93 ms-H/890K) and longer, the n-
heptane jet has ignited before H
2 SOI. Fig. 8 shows selected
high-speed schlieren images for the reference case H-0.07 ms-
D/890K and the pilot-main injection cases D-0.93 ms-H/890K,
D-1.93 ms-H/890K and D-2.93 ms-H/890K, exemplifying the
key instances of ﬂame evolution referenced to the pilot-fuel
SOI (i.e., n-heptane SOI).
For the reference case H-0.07 ms-D/890K ( Fig. 8 (a)), at
0.60 ms aSOI, the n-heptane jet ignites outside the H
2 jet
boundary. The ignition kernel originates from the head sec-
tion and one image frame later, the H 2 jet ignited at around
28 mm from the H2 nozzle. Despite the line-of-sight diagnostic
limitations, the evolution of the burnt zone after ignition, in
addition to the steep pressure rise at this timing, gives conﬁ-
dence that the H
2 jet is indeed burning. Also for the pilot-main
cases, the H 2 jet ignites after interacting with the burnt n-
heptane jet.
Fig. 9 provides the averaged AHRR proﬁles for the reference
and pilot-main injection strategy. Table 5 states the average
pilot and main ignition delay times derived based on high-
speed schlieren imaging and pressure data, respectively. For
the reference case H-0.07 ms-D/890K ( Fig. 9 (a)), the un-
changed ignition delay relative to pilot-only case (Section 3.1)
indicates that the H
2 jet does not impact the ignition of n-
heptane. The n-heptane and H 2 ignite nearly simultaneously
leading to a single AHRR peak with magnitude of roughly 2.5
times the steady-state AHRR of 190 kJ/s. During the steady-
stage mixing-controlled phase, the AHRR matches the heat-
ing value of H
2 inﬂow at measured injection rate of 1.56 mg/ms
[34]. For the pilot-main cases, two distinct AHRR peaks are
visible, which correspond to the pilot- and main-ignition
events. The pilot ignites before interacting with H
2 jet, with
an unchanged ignition delay relative to pilot-only case, within
experimental uncertainty. Subtle differences in the peak
AHRR and the ignition timing after the interaction with pilot-
jet are best visible when the AHRR proﬁles are plotted relative
to main-fuel SOI ( Fig. 9 (b)). The main-ignition delay and the
02468
Time after pilot-fuel SOI (ms)
(a)
0
200
400
600AHRR (kJ/s)
02468
Time after main-fuel SOI (ms)
(b)
0
200
400
600AHRR (kJ/s)
H-0.07ms-D
D-0.93ms-H
D-1.93ms-H
D-2.93ms-H
Uncertainty
Fig. 9 e Averaged AHRR relative to (a) pilot-fuel SOI and (b)
main-fuel SOI for reference case H-0.07 ms-D/890K, and
pilot-main injection cases D-0.93 ms-H/890K, D-1.93 ms-H/
890K and D-2.93 ms-H/890K, with the AHRR variability
between experimental runs shown. Ignition delay
uncertainty of each case shown by red line along time-axis
of (a). See text for further details. (For interpretation of the
references to colour in this ﬁgure legend, the reader is
referred to the Web version of this article.)
international journal of hydrogen energy 48 (2023) 766 e783774

<!-- PDF_PAGE: 10 -->

Fig. 10 e Flame penetration for (a) reference case H-0.07 ms-D/890K, and pilot-main injection cases (b) D-0.93 ms-H/890K, (c)
D-1.93 ms-H/890K and (d) D-2.93 ms-H/890K. See text for detailed explanation of the plot.
Fig. 11 e Processed schlieren images at select time instants for (a) reference case H-0.07 ms-D/890K, and main-pilot injection
cases (b) H-1.07 ms-D/890K, (c) H-2.07 ms-D/890K and (d) H-3.07 ms-D/890K. Highlighted are jet boundaries for n-heptane
(red), H2 (blue), and high-temperature ﬂame (green). Axial and radial distances from the injection nozzle are represented as x
and r, respectively. The ﬁrst frame following pressure-based ignition delay time is outlined by a red border. Time sequence
is relative to the earlier injection ( i.e.,H 2 SOI.). (For interpretation of the references to colour in this ﬁgure legend, the reader
is referred to the Web version of this article.)
international journal of hydrogen energy 48 (2023) 766 e783 775

<!-- PDF_PAGE: 11 -->

peak AHRR increase with a longer dwell time, as further dis-
cussed below.
To aid further interpretation, Fig. 10 provides the schlieren-
derived ﬂame penetration trends (represented by a solid green
line) plotted relative to the pilot-fuel SOI. The experimental
run with the pilot-ignition delay closest to the average is
presented with solid lines while other runs are showed with
dashed lines and show repeatable trends. A non-reacting H
2-
only-case jet penetration (represented using a dashed black
line) is provided as a reference. Note that in dual-fuel cases,
the pilot-fuel slip-stream effect and the jet expansion due to
combustion might lead to a faster H
2-jet penetration than the
non-reactive reference [ 46]. The H 2 and n-heptane jet pene-
trations during their main-ignition timings are marked in blue
and red, respectively. The H
2 jet penetration when it ﬁrst ap-
pears to interact with the n-heptane jet is marked by a circle.
The time of pilot-only case CA90 ( c.f. Section 3.1) is indicated
using a vertical red dashed line.
For the reference case H-0.07 ms-D/890K ( Fig. 10 (a)), the H2
jet ignites upstream of its jet tip at about 0.6 ms aSOI. The
ﬂame penetration reached the H 2 jet tip by 1.0 ms aSOI, after
which the penetration is marginally faster than the non-
reacting jet reference. For the pilot-main cases, the H
2 jet
starts to interact with burnt pilot-fuel at the tip, where it also
ignites shortly after. Sometime after the ignition of the main
jet, the inﬂection point in the ﬂame penetration indicates the
burnt H
2 jet has accelerated beyond the pilot-jet. The simi-
larity in ﬂame penetration trends with different dwell times
indicates that the H 2 jet momentum drives the penetration of
the burnt zone later after ignition. Fig. 10 also shows an
increasing time separation and distance between the initial
jet-jet interaction (black circle) and ignition (star symbols)
with increasing dwell time. These ﬁndings indicate that at a
longer dwell time, a longer jet-jet interaction is required to
ignite the H
2 jet because of the cooler n-heptane jet at the time
of interaction.2 The prolonged jet-jet interaction period before
H2 jet ignition increases the amount of the injected and mixed
H2 as it ignites, which explains the higher AHRR at ignition
(Fig. 9 ). The reference case is an exception to this trend
because the time of jet-jet interaction is governed by the
slower pilot-fuel jet penetration, not the H 2 jet penetration.
Main-pilot injection strategy
This section investigates the effects of dwell time on ﬂame
evolution and AHRR in a main-pilot strategy. Fig. 11 provides
the sample high-speed images for the cases H-0.07 ms-D/
890K, H-1.07 ms-D/890K, H-2.07 ms-D/890K and H-3.07 ms-D/
890K, using the same colour scheme, format, and annotation
used in Section 3.2. In all main-pilot cases, the n-heptane jet
autoignites before interacting with the H
2 jet at approximately
28 mm from the H 2 nozzle. The amount of H 2-air mixture
injected before jet-jet interaction increases with a longer
dwell time. The combustion propagates from the point of
contact between the jets towards the nozzle and jet tip as it
engulfs the unburnt H
2 jet regions. At the longest tested dwell
(H-3.07 ms-D/890K), the H 2 ﬂame fails to propagate towards
the H2 jet tip and radial periphery regions. The reasons for the
limited extent of ﬂame propagation at longest dwell will be
discussed in Section 3.3.1.
The impacts of dwell time and ﬂame evolution on AHHR
are shown in Fig. 12, relative to pilot- and main-fuel SOI. At the
0123456
Time after main-fuel SOI (ms)
(a)
0
200
400
600AHRR (kJ/s)
0123456
Time after pilot-fuel SOI (ms)
(b)
0
200
400
600AHRR (kJ/s)
0123456
Time after pilot-fuel SOI (ms)
(c)
0
200
400
600AHRR (kJ/s)
H-0.07ms-D
H-1.07ms-D
H-2.07ms-D
H-3.07ms-D
Uncertainty
Fig. 12 e Averaged AHRR relative to (a) main-fuel SOI and (b)
pilot-fuel SOI for reference case H-0.07 ms-D/890K and
main-pilot injection cases H-1.07 ms-D/890K and H-
2.07 ms-D/890K. AHRR for H-3.07 ms-D/890K case individual
runs (c). All times relative to pilot-fuel SOI. Ignition delay
uncertainty of each case shown by red line along time-axis
of (a). See text for more details. (For interpretation of the
references to colour in this ﬁgure legend, the reader is
referred to the Web version of this article.)
2 The ambient gas temperature decreases roughly 0.15 K/ms -
this effect on the jet-jet interaction is considered negligible.
international journal of hydrogen energy 48 (2023) 766 e783776

<!-- PDF_PAGE: 12 -->

longest dwell (H-3.07 ms-D/890K), the AHRR is not ensemble
averaged due to the large cyclic variability dsingle-cycle
traces are shown instead. All cases show a single AHRR peak
due to the close succession of pilot- and main-ignition events.
The main-jet residence time before ignition increases with a
longer dwell time (delayed interaction with pilot), which in-
creases the AHRR analogous to conventional diesel combus-
tion at longer ignition delay. However, at longer dwells, the
mixing-controlled combustion phase (steady AHRR phase)
becomes less deﬁned since ignition is too close to the EOI. The
larger mass of H
2 available at ignition also prolongs the
premixed-burn phase.
It is noteworthy that the pilot- and main-ignition delays
summarized in Table 6 show a shorter pilot-ignition delay for
the main-pilot cases than in the pilot-only case at the same
ambient temperature (Section 3.1). As noted in previous
studies [46e48], the increased velocity and turbulence that the
ﬁrst injection produces can enhance the mixing of the sub-
sequent injection. In present case, the turbulence from the H
2
jet may increase the fuel-air mixing rate of the approaching n-
heptane jet. An alternative explanation is that the H 2 jet ho-
mogenizes the temperature difference between the cooler
gases near the vessel walls and hotter gasses in the core; this
changes the conditions that the pilot jet experiences in the
initial penetration stages. The exact mechanism requires
further investigation to conﬁrm.
Fig. 13 provides the schlieren-derived ﬂame penetration
trends plotted relative to the main-fuel SOI, following the
Fig. 13 e Flame penetration for (a) reference case H-0.07 ms-D/890K and main-pilot injection cases (b) H-1.07 ms-D/890K, (c)
H-2.07 ms-D/890K (all runs shown by green solid or dashed lines) and (d) H-3.07 ms-D/890K (all runs shown by solid lines,
with the line colors selected to match that of their AHRR proﬁles in Fig. 12 (c)). Non-reacting H
2 jet penetration shown as
black dashed lines. Markers used to identify jet penetration of H 2 (blue) and n-heptane (red) at H 2 ignition. Circle marker
used to identify H 2 jet penetration at start of interaction with n-heptane jet. Time sequence starts relative to ﬁrst SOI ( i.e.,H 2
SOI). Mean CA90 time of n-heptane shown by red dash line, with standard deviation shown along the time-axis. (For
interpretation of the references to colour in this ﬁgure legend, the reader is referred to the Web version of this article.)
Table 7 e Input parameters used to set up the Musculus
and Kattke jet model [42 ,50] simulating H 2 mixing aEOI.
Jet Model Input Parameters
Ambient gas temperature 890 K
Ambient gas density 23.8 kg/m 3
Fluid (H 2) density 3.13 kg/m 3
Nozzle diameter 0.58 mm
Injection velocity 2991 ms
/C0 1
Ramp down time EOI 0.05 ms
Jet angle 25 /C14
Table 6 e Average pilot and main ignition delay times, relative to pilot-fuel and main-fuel SOI, for the reference case and
main-pilot injection cases. Bold texts indicate reference case. Uncertainty provided as one standard deviation.
Ignition Delay Times
Case name Relative to pilot-fuel SOI Relative to main-fuel SOI
Pilot (ms) Main (ms) Pilot (ms) Main (ms)
H-0.07 ms-D/890K 0.62 ±0.03 0.63 ±0.04 0.69 ±0.03 0.70 ±0.04
H-1.07 ms-D/890K 0.46 ± 0.10 0.51 ± 0.10 1.55 ± 0.09 1.59 ± 0.09
H-2.07 ms-D/890K 0.50 ± 0.02 0.56 ± 0.04 2.57 ± 0.03 2.64 ± 0.04
H-3.07 ms-D/890K 0.42 ± 0.05 0.50 ± 0.04 3.49 ± 0.06 3.57 ± 0.04
international journal of hydrogen energy 48 (2023) 766 e783 777

<!-- PDF_PAGE: 13 -->

same convention as Fig. 10 . A non-reacting H 2-only-case jet
penetration is also provided as reference. The results show
that the H
2 jet penetration at the time of ignition increases
with a longer dwell time, which is expected because of the
increased delay when H
2 starts interacting with the burnt pilot
fuel. The ﬂame penetration of the main-pilot cases occurs in a
repeatable manner after ignition. The case with the longest
tested dwell (H-3.07 ms-D/890K) is an exception to this trend
as it shows large cyclic variability in its ﬂame penetration
path. Referring back to the AHRR proﬁles for the case H-
3.07 ms-D/890K (Fig. 12 (c)), it is notable that the magnitude of
the peak AHRR roughly corresponds to the rate at which the
ﬂame proceeded throughout the jet volume. A noteworthy
observation is that, unlike other main-pilot cases, the pilot
fuel ignites after the main-fuel EOI for case H-3.07 ms-D/890K.
This suggests that the fuel-air mixing effects of aEOI
contribute to inconsistent ﬂame penetration paths and AHRR
proﬁles for the longest dwell.
Pilot-fuel injection after main-fuel EOI
This section investigates the EOI effects on the fuel-air mixing
in the case of the longest dwell, considering previous studies
have reported the rapid leaning out of the fuel jet by the
entrainment aEOI [ 42,44,49]. A jet model based on the Mus-
culus and Kattke control-volume jet model [ 42,50] is used to
assess the EOI effects on the H
2-air mixture at the time of
interaction with n-heptane jet. All model parameters were
kept the same as in the experiments (summarized in Table 7),
and the jet cone angle was tuned to match the modelled and
the experimental penetration trends. A spray cone angle of 25
/C14
was found to yield a good agreement for the jet penetration
between the model and experimental data. The approach of
tuning model cone angle to match the experimental pene-
tration was previously validated to be capable of generating
accurate mixture predictions of vaporized sprays [ 51]. The
good agreement between the very lean modelled contour with
the experimental jet boundary (not shown) provides further
conﬁdence in the model results.
Fig. 14 shows the modelled equivalence ratio ( 4) distribu-
tions at selected timesteps to provide indications of the
mixture states of the experimental frames in Fig. 11 (d) . The 4
contours are calculated based on 21% ambient O
2 concentra-
tion. The plotted contour levels are motivated by the H 2
ﬂammability limits of 4 ¼ 0.1 and 6.5 at standard temperature
and pressure [ 6] as rough estimates of the ﬂammable mixture
extent in the jet, neglecting the pressure/temperature effects
[52]. Fig. 14 shows that the near-nozzle fuel concentration
continuously decreases aEOI, which suggests the jet-jet
interaction occurs in very lean H
2 jet regions that are less
favourable for ﬂame propagation. This explains the experi-
mentally observed slower combustion spreading, cyclic vari-
ability and the unburnt zones remaining late after ignition. It
is emphasized that whilst the simpliﬁed model provides
useful insights, the model does not provide an exact simula-
tion of the fuel-air mixture distribution within the H
2 jet as
several jet model parameters required estimation. The model
also does not reproduce cyclic variations and other relevant
processes, including turbulence-chemistry interaction, which
can affect the ignition of the fuel mixtures.
Cases with lower ambient gas temperature
This section investigates the ambient temperature effects on
the ﬂame evolution and AHRR of the dual-fuel cases. Fig. 15
shows selected high-speed schlieren images for the refer-
ence case H-0.07 ms-D/890K and the lower ambient temper-
ature cases H-0.07 ms-D/820K and H-0.07 ms-D/780K,
following the same convention as Fig. 8. When comparing the
Fig. 14 e Time sequence of the modelled fuel spray aEOI,
based on the Musculus and Kattke control-volume jet
model [ 42,50], showing the change in equivalence ratio
across the jet body.
international journal of hydrogen energy 48 (2023) 766 e783778

<!-- PDF_PAGE: 14 -->

schlieren images of the three cases, the initial ignition spot
locates externally to the H 2 jet boundary at 890 K but appears
to emerge at a location that is closer to, or within the H 2 jet
boundary at lower temperatures. Recognising the line-of-sight
limitation of schlieren diagnostics that prevents the deter-
mination of the exact kernel locations in a three-dimensional
space, the shift in the relative positioning of the ignition spot,
nevertheless, suggests that at lower ambient temperature the
n-heptane jet autoignites after interacting with the H
2 jet. The
ﬂame penetration plots presented for previous variations are
not informative for the ambient temperature cases and are
not presented.
Fig. 16 presents the averaged AHRR traces for the ambient
temperature variation cases, with Table 8 summarizing the
pilot and main ignition delay times. The statistically indif-
ferent ignition delay of the tested ambient temperature
variation cases relative to the pilot-only cases (Section 3.1)
indicates that the interaction between the H
2 and n-heptane
jets does not affect the pilot ignition. Similarly to previous
variations that led to increased main-fuel ignition delay, the
increase in ignition delay and, therefore, the corresponding
residence time of the main jet before ignition also increase the
AHRR at lower temperatures. The mixing-controlled com-
bustion phase becomes less deﬁned at the lowest temperature
(H-0.07 ms-D/780K). This may be partly attributable to the
ensemble averaging method ( e.g., shifting the AHRR to align
with the ignition time shifts relative to the EOI, which might
introduce non-physical variability in late combustion stages).
The less-deﬁned mixing-controlled AHRR can also be attrib-
uted to the variability in the n-heptane ignition location at
780 K ( Fig. 17 )dthe ignition location impacts the premixed
burn transient that can last until nearly the EOI.
Fig. 15 e Processed schlieren images at select time instants for (a) reference case H-0.07 ms-D/890K, and lower ambient
temperature cases (b) H-0.07 ms-D/820K and (c) H-0.07 ms-D/780K. Highlighted are the n-heptane jet boundary (red), H 2 jet
boundary (blue), and high-temperature ﬂame (green). Axial and radial distances from the injection nozzle are represented
as x and r, respectively. The ﬁrst frame following pressure-based ignition delay time is outlined by a red border. Time
sequence starts relative to H
2 SOI. (For interpretation of the references to colour in this ﬁgure legend, the reader is referred to
the Web version of this article.)
international journal of hydrogen energy 48 (2023) 766 e783 779

<!-- PDF_PAGE: 15 -->

Fig. 17 (a) shows select schlieren frames from three
experimental runs of case H-0.07 ms-D/780K to highlight the
source of cyclic variations. The n-heptane ignition may origi-
nate from the jet head, jet tail, as well as both jet-head and jet-
tail sections. The corresponding AHRR proﬁles, which are
provided in Fig. 17 (b), show that the AHRR proﬁle changes
depending on the initial ignition kernel location and the
ignition delay of each run. The AHRR proﬁle of the run in
Fig. 17 (a)(i), which exhibits jet-head ignition and shorter-
than-average ignition delay, has a distinct premixed com-
bustion AHRR peak followed by a steady diffusion ﬂame
period that is similar to the higher temperature cases. When
ignition occurs later, in the near-nozzle region (Fig. 17 (a)(ii)) or
with two ignition kernels (Fig. 17 (a)(iii)), the peak AHRR proﬁle
is wider and slowly decays to the steady AHRR value that it
reaches around the EOI. The wider AHRR peak proﬁle with a
reduced amplitude can be associated with a slower ﬂame
evolution through the H
2 jet volume. The reasons for slower
evolution are two-fold: (1) ﬂame propagating through an
overall leaner H
2 mixture due to the delayed ignition; (2) the
ignition initially occurs in a mixture less favourable for ﬂame
propagation leading to slower combustion spreading. The
relative importance of these mechanisms needs further
examination.
Summary and conclusions
The ignition and combustion characteristics of intersecting H2
and diesel jets were investigated under engine-relevant high-
pressure high-temperature conditions in an optically acces-
sible constant-volume combustion chamber (CVCC) using
high-speed schlieren imaging and pressure trace analysis. The
H
2 (main fuel) and n-heptane (pilot fuel, diesel surrogate) were
injected using single nozzle injectors arranged with a
converging angle of 12
/C14 . The pilot fuel accounted for 6% of the
injected fuel energy. The effects of ambient temperature and
injection sequence (pilot-main injection, main-pilot injection,
and near-simultaneous injections) on the ignition and com-
bustion properties were investigated and compared to refer-
ence cases with only n-heptane injections under otherwise
unchanged conditions.
The following conclusions apply under the conditions
investigated in this work:
0
200
400
600
800AHRR (kJ/s)
890 K
0
200
400
600
800AHRR (kJ/s)
820 K
012345
Time after main-fuel SOI (ms)
0
200
400
600
800AHRR (kJ/s)
780 K
Average
Uncertainty
Fig. 16 e Averaged AHRR relative to main-fuel SOI at
varying ambient gas temperatures: H-0.07 ms-D/890K
(top), H-0.07 ms-D/820K (middle) and H-0.07 ms-D/780K
(bottom). Ignition delay uncertainty of each case shown by
red line along time-axis. (For interpretation of the
references to colour in this ﬁgure legend, the reader is
referred to the Web version of this article.)
Table 8 e Average pilot and main ignition delay times relative to pilot-fuel and main-fuel SOI, respectively, for the reference
case and lower temperature cases. Ignition delay of n-heptane (discussed in Section 3.1) is also shown for reference. Bold
texts indicate reference case. Uncertainty provided as one standard deviation.
Ignition Delay Times
Case name Pilot ignition Main ignition n-heptane only
relative to pilot-fuel SOI (ms) relative to main-fuel SOI (ms) ignition delay (ms)
H-0.07 ms-D/890K 0.62 ±0.03 0.70 ±0.04 0.62 ±0.04
H-0.07 ms-D/820K 0.93 ± 0.07 1.03 ± 0.09 0.93 ± 0.05
H-0.07 ms-D/780K 1.42 ± 0.19 1.73 ± 0.34 1.68 ± 0.12
international journal of hydrogen energy 48 (2023) 766 e783780

<!-- PDF_PAGE: 16 -->

1. The pilot-fuel ignition is not inﬂuenced by the interaction
with H 2 jet. The quenching of pilot-fuel when interacting
with natural-gas jets, reported elsewhere, was not
observed with H
2 jets. However, such an effect cannot be
excluded in a conﬁguration promoting stronger interaction
between both jets.
2. The H 2 jet ignites after a period of interaction with the
burnt products from the pilot fuel. The duration of this
interaction depends on the dwell time between the pilot
SOI, the onset of jet interaction, and the charge tempera-
ture. A prolonged interaction is required for successful
ignition under less reactive conditions and when the dwell
time causes the pilot-fuel combustion products to lean-out
and cool-down before the interaction begins.
3. The AHRR is dominated by the H
2 combustion and shows
analogous characteristics to autoigniting diesel jets. The peak
AHRR directly succeeds the ignition of the H2 jet, and the peak
AHRR amplitude increases with the elapsed time between H2
SOI and ignition (i.e., the mass of hydrogen within the jet at
ignition). After the peak AHRR, a steady AHRR period with
diffusion ﬂame is established until the H
2 EOI. In most cases,
the peak AHRR corresponds to the H2 ﬂame propagation from
the ignition location across the H2 jet volume.
4. When pilot-fuel ignites after the H 2 EOI, the jet-jet inter-
action occurs in H 2 jet region with a very lean H 2 equiva-
lence ratio. This results in slower combustion propagation
through the H
2 jet with large unburnt zones persisting late
after ignition and large cyclic AHRR variability.
5. Very long pilot ignition delays induce a cyclic variability in
the ignition delay, the pilot-ignition location, and the
location of H
2 jet ignition. This cyclic variability results in
variable ﬂame evolution through the H 2 jet and associated
AHRR variability.
Declaration of competing interest
The authors declare that they have no known competing
ﬁnancial interests or personal relationships that could have
appeared to inﬂuence the work reported in this paper.
Acknowledgements
The ﬁnancial support by the Australian Renewable Energy
Agency (ARENA) and MAN Energy Solutions is gratefully
appreciated. The ﬁrst author acknowledges the support of the
Commonwealth through the Australian Government Research
Training Program Scholarship. The technical support during
commissioning and operation of the CVCC facility by Mr Bryce
Edmonds is also gratefully appreciated. The authors also
acknowledge fruitful discussions with Dr Alexander Knaﬂ and
Marcus Becher from MAN Energy Solutions.
This Article has been authored by National Technology and
Engineering Solutions of Sandia, LLC. under contract No. DE-
NA0003525 with the U.S. Department of Energy/National Nu-
clear Security Administration. The United States Government
retains and Elsevier, by accepting the article for publication,
acknowledges that the United States Government retains a
non-exclusive, paid-up, irrevocable, world-wide license to
publish or reproduce the published form of this manuscript, or
allow others to do so, for United States Government purposes.
Fig. 17 e (a) High-speed images from three runs for H-
0.07 ms-D/780K, showing ignition originating from the n-
heptane jet head-section (i), tail-section (ii), as well as both
head and tail-section (iii). Highlighted are the n-heptane jet
boundary (red), H
2 jet boundary (blue) and high-temperature
ﬂame (green). (b) The corresponding AHRR of the H-0.07 ms-
D/780K experimental runs shown in (a). (For interpretation
of the references to colour in this ﬁgure legend, the reader is
referred to the Web version of this article.)
international journal of hydrogen energy 48 (2023) 766 e783 781

<!-- PDF_PAGE: 17 -->

references
[1] Yip HL, Srna A, Yuen ACY, Kook S, Taylor RA, Yeoh GH,
Medwell PR, Chan QN. A review of hydrogen direct injection
for internal combustion engines: towards carbon-free
combustion. Appl Sci 2019;9:4842 .
[2] Berry GD, Pasternak AD, Rambach GD, Ray Smith J,
Schock RN. Hydrogen as a future transportation fuel. Energy
1996;21:289e303.
[3] A review of hydrogen usage in internal combustion engines
(gasoline-lpg-diesel) from combustion performance aspect.
Int J Hydrogen Energy 2020;45:35257 e68. 4th International
HYDROGEN TECHNOLOGIES Congress .
[4] Verhelst S, Wallner T. Hydrogen-fueled internal combustion
engines. Prog Energy Combust Sci 2009;35:490 e527.
[5] Konnov AA, Mohammad A, Kishore VR, Kim NI, Prathap C,
Kumar S. A comprehensive review of measurements and
data analysis of laminar burning velocities for various
fuelþair mixtures. Prog Energy Combust Sci 2018;68:197 e267.
[6] Rosati MF, Aleiferis PG. Hydrogen SI and HCCI combustion in
a direct-injection optical engine. SAE International Journal of
Engines 2009;2:1710 e36.
[7] Kawahara N, Tomita E. Visualization of auto-ignition and
pressure wave during knocking in a hydrogen spark-ignition
engine. Int J Hydrogen Energy 2009;34:3156 e63.
[8] Liu X, Srna A, Yip HL, Kook S, Nian Q, Hawkes E. Comparison
of hydrogen port injection and direct injection (DI) in a
single-cylinder dual-fuel diesel engine. In: 22nd Australian
ﬂuid mechanics conference, AFMC2020. Brisbane, Australia:
The University of Queensland; 2020 .
[9] Lee K, Kim Y, Byun C, Lee J. Feasibility of compression
ignition for hydrogen fueled engine with neat hydrogen-air
pre-mixture by using high compression. Int J Hydrogen
Energy 2013;38:255 e64.
[10] Gomes Antunes J, Mikalsen R, Roskilly A. An experimental
study of a direct injection compression ignition hydrogen
engine. Int J Hydrogen Energy 2009;34:6516 e22.
[11] White C, Steeper R, Lutz A. The hydrogen-fueled internal
combustion engine: a technical review. Int J Hydrogen
Energy 2006;31:1292 e305.
[12] Zhai G, Xing S, Yuen AC, Medwell PR, Kook S, Yeoh GH,
Chan QN. Laser ignition of iso-octane and n-heptane jets
under compression-ignition conditions. Fuel 2021:122555 .
[13] Van Blarigan P, Keller J. A hydrogen fuelled internal
combustion engine designed for single speed/power
operation. Int J Hydrogen Energy 1998;23:603 e9.
[14] Homan H, Reynolds R, De Boer P, McLean W. Hydrogen-
fueled diesel engine without timed ignition. Int J Hydrogen
Energy 1979;4:315 e25.
[15] Furuhama S, Kobayashi Y. Development of a hot-surface-
ignition hydrogen injection two-stroke engine. Int J
Hydrogen Energy 1984;9:205 e13.
[16] Dimitriou P, Tsujimura T. A review of hydrogen as a
compression ignition engine fuel. Int J Hydrogen Energy
2017;42:24470e86.
[17] Kumar M, Bhowmik S, Paul A. Effect of pilot fuel injection
pressure and injection timing on combustion, performance
and emission of hydrogen-biodiesel dual fuel engine. Int J
Hydrogen Energy 2022;47:29554 e67.
[18] Bakar R, Widudo, Kadirgama K, Ramasamy D, Yusaf T,
Kamarulzaman M, Sivaraos, Aslfattahi N, Samylingam L,
Alwayzy SH. Experimental analysis on the performance,
combustion/emission characteristics of a di diesel engine
using hydrogen in dual fuel mode. Int J Hydrogen Energy
2022.
[19] Woodyard D. Chapter two - dual-fuel and gas engines. In:
Woodyard D, editor. Pounder 's marine diesel engines and gas
turbines. 9th ed. Oxford: Butterworth-Heinemann; 2009.
p. 41 e60.
[20] L i uH ,L iJ ,W a n gJ ,W uC ,L i uB ,D o n gJ ,L i uT ,Y eY ,W a n gH ,
Yao M. Effects of injection strategies on low-speed marine
engines using the dual fuel of high-pressure direct-
injection natural gas and diesel. Energy Sci Eng
2019;7:1994 e2010.
[21] Li G. Optimization study of pilot-ignited natural gas direct-
injection in diesel engines. SAE Trans 1999;108:1739 e48.
[22] Liu J, Yang F, Wang H, Ouyang M, Hao S. Effects of pilot fuel
quantity on the emissions characteristics of a CNG/diesel
dual fuel engine with optimized pilot injection timing. Appl
Energy 2013;110:201 e6.
[23] Liu X, Srna A, Yip HL, Kook S, Chan QN, Hawkes ER.
Performance and emissions of hydrogen-diesel dual direct
injection (H2DDI) in a single-cylinder compression-ignition
engine. Int J Hydrogen Energy 2021;46:1302 e14.
[24] Y. Wang, A. Evans, A. Srna, A. Wehrfritz, E. Hawkes, X. Liu, S.
Kook, Q. N. Chan, A numerical investigation of mixture
formation and combustion characteristics of a hydrogen-
diesel dual direct injection engine, SAE Paper 2021-01-0526
(2021).
[25] White TR. Simultaneous diesel and natural gas injection for
dual-fuelling compression-ignition engines. Sydney,
Australia: Ph.D. thesis, University of New South Wales; 2006 .
[26] Fink G, Jud M, Sattelmayer T. Inﬂuence of the spatial and
temporal interaction between diesel pilot and directly
injected natural gas jet on ignition and combustion
characteristics. J Eng Gas Turbines Power 2018;140:102811 .
[27] Fink G, Jud M, Sattelmayer T. Fundamental study of diesel-
piloted natural gas direct injection under different operating
conditions. J Eng Gas Turbines Power 2019;141:091006 .
[28] Yang X, Vinhaes VB, Turcios M, McTaggart-Cowan G,
Huang J, Naber J, Shahbakhti M, Schmidt H, Atkinson W.
Process for study of micro-pilot diesel-NG dual fuel
combustion in a constant volume combustion vessel
utilizing the premixed pre-burn procedure. 2019. SAE Paper
2019-01-1160.
[29] Trusca B. High pressure direct injection of natural gas and
hydrogen fuel in a diesel engine. Ph.D. thesis. Canada:
University of British Columbia; 2001 .
[30] Ishibashi R, Tsuru D. An optical investigation of combustion
process of a direct high-pressure injection of natural gas. J
Mar Sci Technol 2017;22:447 e58.
[31] Zhai G, Xing S, Yuen A, Yeoh GH, Chan QN. Spray and
combustion characteristics of gasoline-like fuel under
compression-ignition conditions. Energy Fuels
2020;34:16585e98.
[32] Xing S, Zhai G, Mo H, Medwell PR, Yuen AC, Kook S, Yeoh GH,
Chan QN. Study of ignition and combustion characteristics
of consecutive injections with iso-Octane and n-Heptane as
fuels. Energy Fuels 2020;34:14741 e56.
[33] Fattah IMR, Ming C, Chan QN, Wehrfritz A, Pham PX,
Yang W, Kook S, Medwell PR, Yeoh GH, Hawkes ER, Masri AR.
Spray and combustion investigation of post injections under
low-temperature combustion conditions with biodiesel.
Energy Fuels 2018;32:8727 e42.
[34] Yip HL, Srna A, Liu X, Kook S, Hawkes ER, Chan QN.
Visualization of hydrogen jet evolution and combustion
under simulated direct-injection compression-ignition
engine conditions. Int J Hydrogen Energy 2020;45:32562 e78.
[35] Dec JE. A conceptual model of Dl diesel combustion based on
laser-sheet imaging. SAE Trans 1997;106:1319 e48.
[36] Woo C, Kook S, Rogers P, Marquis C, Hawkes E, Tupuﬁa S. A
comparative analysis on engine performance of a
conventional diesel fuel and 10% biodiesel blends produced
from coconut oils. SAE International Journal of Fuels and
Lubricants 2015;8:597 e609.
international journal of hydrogen energy 48 (2023) 766 e783782

<!-- PDF_PAGE: 18 -->

[37] PubChem compound summary for CID 8900, heptane. 2022. .
[Accessed 7 September 2022] .
[38] Heywood J. Internal combustion engine fundamentals 2E.
McGraw-Hill Education; 2018 .
[39] Pickett LM, Kook S, Williams TC. Visualization of diesel spray
penetration, cool-ﬂame, ignition, high-temperature
combustion, and soot formation Using high-speed imaging.
SAE International Journal of Engines 2009;2:439 e59.
[40] Liang X, Zhong A, Sun Z, Han D. Autoignition of n-heptane
and butanol isomers blends in a constant volume
combustion chamber. Fuel 2019;254:115638 .
[41] Musculus MP, Miles PC, Pickett LM. Conceptual models for
partially premixed low-temperature diesel combustion. Prog
Energy Combust Sci 2013;39:246 e83.
[42] Musculus M, Kattke K. Entrainment waves in diesel jets. SAE
International Journal of Engines 2009;2:1170 e93.
[43] Reitz R, Hessel R, Musculus M. A visual investigation of CFD-
predicted in-cylinder mechanisms that control ﬁrst- and
second-stage ignition in diesel jets. 2019. SAE Paper 2019-01-
0543.
[44] Knox BW, Genzale CL, Pickett LM, Garcia-Oliver JM, Vera-
Tudela W. Combustion recession after end of injection in
diesel sprays. SAE International Journal of Engines
2015;8:679e95.
[45] Zhai G, Xing S, Srna A, Wehrfritz A, Kook S, Hawkes ER,
Chan QN. Ignition and ﬂame stabilisation of primary
reference fuel sprays at engine-relevant conditions. Combust
Flame 2021;233:111620 .
[46] Skeen S, Manin J, Pickett LM. Visualization of ignition
processes in high-pressure sprays with multiple injections of
n-Dodecane. SAE International Journal of Engines
2015;8:696e715.
[47] Zhang Y, Ito T, Nishida K. Characterization of mixture
formation in split-injection diesel sprays via laser absorption-
scattering (LAS) technique. SAE Trans 2001;110:2189 e200.
[48] Anders JW, Magi V, Abraham J. A computational
investigation of the interaction of pulses in two-pulse jets.
Numer Heat Tran, Part A: Applications 2008;54:999 e1021.
[49] Kook S, Pickett LM, Musculus MP. Inﬂuence of diesel
injection parameters on end-of-injection liquid length
recession. SAE International Journal of Engines
2009;2:1194e210.
[50] Network EC. Download code. 2019. https://ecn.sandia.gov/
download-code/. [Accessed 14 February 2021].
[51] Pickett LM, Manin J, Genzale CL, Siebers DL, Musculus MP,
Idicheria CA. Relationship between diesel fuel spray vapor
penetration/dispersion and local fuel mixture fraction. SAE
International Journal of Engines 2011;4:764 e99.
[52] Shapiro ZM, Moffette TR. Hydrogen ﬂammability data and
application to pwr loss-of-coolant accident. 1957 .
[53] Yip HL, Srna A, Wehrfritz A, Kook S, Hawkes ER, Chan QN. A
parametric study of autoigniting hydrogen jets under
compression-ignition engine conditions. Int J Hydrogen
Energy 2022;47:21307 e22.
[54]
Liu X, Seberry G, Kook S, Chan QN, Hawkes ER. Direct
injection of hydrogen main fuel and diesel pilot fuel in a
retroﬁtted single-cylinder compression ignition engine. Int J
Hydrogen Energy 2022 .
international journal of hydrogen energy 48 (2023) 766 e783 783
