<!-- PDF_PAGE: 1 -->

International Journal of Hydrogen Energy 67 (2024) 172–191
Available online 19 April 2024
0360-3199/Crown Copyright © 2024 Published by Elsevier Ltd on behalf of Hydrogen Energy Publications LLC. This is an open access article under the CC BY license
(http://creativecommons.org/licenses/by/4.0/).
Contents lists available at ScienceDirect
International Journal of Hydrogen Energy
journal homepage: www.elsevier.com/locate/he
Effects of jet interaction angle on the ignition and combustion characteristics
of hydrogen-diesel dual-fuel direct injection
Patrick Rorimpandey, Guanxiong Zhai, Sanghoon Kook, Evatt R. Hawkes, Qing Nian Chan∗
School of Mechanical and Manufacturing Engineering, The University of New South Wales, NSW 2052, Australia
A R T I C L E I N F O
Keywords:
Hydrogen
Dual fuel
Direct injection
Compression-ignition engine
A B S T R A C T
This study investigates the ignition and combustion characteristics of intersecting diesel surrogate (pilot)
and hydrogen (H 2, main) jets under engine-relevant conditions. The experiments, performed in an optically
accessible constant-volume combustion chamber (CVCC), utilised two converging single-hole injectors, with
the pilot fuel accounting for 12% of the total injected fuel energy. This study investigated the effects of two
key parameters on the ignition process: jet interaction angle (12 ◦ to 19 ◦) and ambient O 2 concentration (10
to 21 vol.%). The results show that the presence of H 2 either advances or delays pilot ignition depending on
whether the pilot n-heptane jet ignites before or after interacting with the H 2 jet, respectively. The pilot-main
ignition transition period is influenced by both jet interaction angle and ambient O 2 concentration. Under
identical ambient conditions, a smaller jet interaction angle results in a longer transition, while for a constant
angle, lower ambient O 2 leads to a more prolonged transition. Under 10 vol.% O 2 conditions, flame kernels
emerge upstream of the main flame body, before eventually merging with the reacting jet downstream, with
this phenomenon observed to induce variation in heat and flame stabilisation characteristics. An explanation
for the upstream kernel formation is offered based on the entrainment of residual pilot n-heptane-jet fuel into
the upstream region of the still-injecting main jet, with the relative jet momentum a likely key contributor
influencing this entrainment that impacts kernel formation.
1. Introduction
Driven by the urgent need for cleaner combustion, dual-fuel strate-
gies are gaining traction in compression-ignition engine research [1–3].
Conventional compression-ignition diesel engines, where ignition of the
diesel fuel is the sole energy source of the engine power [ 4], are able
to achieve low output emissions when coupled with an aftertreatment
system [5]. Further emission gains can be achieved with the dual-fuel
approach, which utilises diesel ignition to ignite less carbon-intensive
fuels, even those with poor compression ignition qualities such as
ammonia [6] and – the focus of this study – hydrogen (H 2) [7,8], with
the integration of these cleaner fuels into existing systems paving the
way for significant emission reductions.
Among various dual-fuel combustion strategies, dual-fuel direct
injection (DFDI) that involves injecting both fuels directly into the
cylinder, enabling precise control over the combustion process, has
drawn considerable interest [ 9,10]. DFDI can be implemented using
either separate injectors for each fuel [ 7,11] or a single injector ca-
pable of handling both [ 12–14]. Previous DFDI studies have reported
the interplay between injector configuration [ 15–17], injection tim-
ing [16–19], and ambient conditions [ 17–20] in shaping the ignition
∗ Corresponding author.
E-mail address: qing.chan@unsw.edu.au (Q.N. Chan).
and combustion processes. However, the specific configuration of the
injector plays a dominant role in affecting the interaction between the
fuel jets, which directly impacts the attainable ignition and combustion
modes.
Perhaps among the best available DFDI data on the topic of injector
configuration is the optical study of natural gas-diesel study performed
by Fink et al. [ 16,17] within a rapid compression expansion machine
(RCEM). Their results show that a diverging injector configuration,
where the jet axes point away from each other, enables gas fuel-
air premixing and diesel autoignition without direct jet interaction.
This allows for a greater degree of natural gas-air premixing, and in
some cases, jet-wall interaction and redirection, before the gaseous fuel
encounters the burned diesel products and ignites, ensuing premixed
combustion. In the same study, a converging injector setup with in-
tersecting jet axes was found to promote direct interaction between
the jets, potentially leading to more reliable ignition. However, the
entrainment of diesel fuel into the natural gas jet, observed in some
cases for a converging configuration, can delay or even quench diesel
autoignition [16,17].
https://doi.org/10.1016/j.ijhydene.2024.04.166
Received 12 February 2024; Received in revised form 4 April 2024; Accepted 14 April 2024

<!-- PDF_PAGE: 2 -->

International Journal of Hydrogen Energy 67 (2024) 172–191
173
P. Rorimpandey et al.
While literature has explored the interplay of injector configuration,
premixing, and combustion in DFDI, knowledge specifically for H 2-
diesel DFDI remains limited. This gap partly arises from the recent
development of H2 direct-injection technologies [21,22]. For example,
while there are reports of diesel fuel autoignition delays or quenching
arising from interaction with natural gas jet in natural gas-diesel DFDI
experiments [16,17], similar observations have not been documented
with H 2. However, existing studies suggest potential parallels. For
instance, Hernandez et al. [23] found that in a constant volume com-
bustion chamber (CVCC) at 876 K and 11—21 bar pressure, the diesel
ignition delay increased with H2 substitution. This was observed when
ambient air was premixed with H 2 within a global equivalence ratio
range of 0.4–0.8. The study attributed the increase, approximately
6.5% over the range examined, to reduced radical availability for H 2
abstraction, which initiates the first stage of ignition involving low-
temperature chemistry (LTC) processes [24,25]. On the other hand,
Yang et al. [26] reported a comparatively longer diesel ignition delay in
a CVCC at 750 K and 13 kg/m 3 density when diesel was injected into
a premixed natural gas and air mixture at a global equivalence ratio
of 0.58. This resulted in almost double the delay compared to cases
without premixed gas. The study suggested that this difference could be
due to changes in reaction rates and transient product concentrations
caused by the premixed methane/air mixture. While direct comparison
of these studies is challenging because of the differing conditions, they
highlight the need for targeted research on H 2-diesel direct injection
configurations.
Building on previous research suggesting that fuel jet overlap can
enhance ignition consistency, this study focuses on assessing the im-
pact of varying converging angles on the ignition and combustion
processes of intersecting H 2 and diesel jets within a H 2-diesel DFDI
configuration. H 2 and n-heptane, a diesel substitute, were injected
into a quiescent high-temperature, high-pressure environment using a
converging setup with two separate single-hole injectors in a constant
volume combustion chamber (CVCC). The study employed high-speed
schlieren imaging and pressure measurements for diagnostics. Concerns
regarding NO x emissions in H 2-fuelled engines [27,28] have necessi-
tated the use of dilution strategies like exhaust gas recirculation (EGR),
where exhaust gases are reintroduced into the intake to increase heat
capacity and hence reduce temperature during combustion, which have
shown to be an effective method of controlling NO x emissions [29–
31]. However, the resulting lower O2 content is known to reduce
the reactivity of the fuel ignition process. Previous studies on single
jets have demonstrated that lower O2 conditions can influence the
combustion processes of both diesel [19] and H 2 [32] fuels, leading
to several phenomena such as longer ignition delays and lower heat
release magnitudes. Given these known effects, in the context of H 2-
diesel DFDI, it is likely that lower O2 levels associated with dilution
strategies would likely increase the interaction between the jets, po-
tentially impacting the subsequent ignition and combustion processes.
Therefore, the current study further considers the effects of ambient O2
concentration on H2-diesel DFDI combustion.
It is noted that the authors previously conducted an experiment
investigating the impact of varying the relative fuel proportion by ad-
justing the injection durations of simultaneously injected, intersecting
diesel surrogate and H2 jets at a constant converging angle [20]. Their
findings showed a reduction in H 2 flame lift-off only in cases where
the diesel surrogate injection duration was shorter than the H 2 jet.
They attributed this observation to the interaction between the H 2-air
mixture and diesel combustion products, which extended to the injector
nozzle after the diesel injection ended due to combustion recession. The
study also demonstrated the entrainment of the inactive diesel jet into
the main H2 jet. Thus, while not the primary focus of the current work,
this study also further varies the pilot injection duration to monitor
the response of the reacting jet as a means to provide insights into
the observed changes in ignition and combustion characteristics arising
from variations in jet interaction angle and ambient conditions.
2. Experimental details
2.1. Constant-volume combustion chamber
The experiments were performed in an optically accessible CVCC,
simulating high pressure and temperature conditions relevant to
compression-ignition (CI) engines. The cubic chamber, with sides mea-
suring 114 mm, features six interchangeable ports on its wall. The
wall was maintained at a temperature of 403 K during experiments
to prevent water condensation. A mixing fan installed on the top port
ensured even distribution of the ambient charge. Three sapphire glass
windows with 101.6 mm clear apertures installed on the other ports
provided optical access. Single-hole fuel injectors for H 2 and diesel
were positioned on one side port opposite a flat metal wall on the
opposing side. A schematic diagram of the CVCC setup is provided in
Fig. 1(a).
To achieve varying jet interaction angles, the relative injector angles
were adjusted for downstream convergence at 12 deg, 15 deg, and
19 deg. For 12 deg, the H 2 injector was centred with the diesel
injector positioned above, angled 12 deg relative and towards the H 2-
jet axis. Due to spatial limitations within the CVCC, the H 2 injector
had to be shifted off centre for the 15 deg and 19 deg configuration,
positioned progressively lower as the angle increased. Fig. 2 shows the
injector configurations for each angle, highlighting the relative position
of the injectors to the CVCC centreline. Dedicated side ports were
manufactured to hold the injectors at the targeted angles.
Achieving the desired high pressure and temperature conditions
within the CVCC followed a pre-burn process described in previous
publications [33–35]. Briefly, the spark ignition of a compressed lean
mixture of C 2H2, H 2, O2 and N2, followed by a subsequent cool-
down phase where heat transferred to the chamber walls, was used to
generate the desired conditions. Fuel injection was triggered when a
specific target pressure (and corresponding temperature) was reached
during the cool-down phase, as shown in Fig. 1(b). The in-chamber
pressure was monitored through a piezoelectric pressure transducer
(Kistler 6052C with amplifier 5015 A). The recorded pressure trace was
also used to derive apparent heat release rate (AHRR),similar to past
studies [36,37] in helping interpreting results. For this study, the pre-
combustion mixture was tailored to achieve 21 vol.%, 15 vol.%, and
10 vol.% O2 concentration after the premixed ambient gas combustion
stage (Fig. 1(b)), with the ambient density set to 23.8 kg/m 3. The
chosen ambient O2 concentration levels reflect varying EGR levels that
have been studied in past diesel combustion studies [19].
The charge core temperature in the geometrical centre of the CVCC
was characterised with a thin-wire K-type thermocouple separately and
adopted as a representative charge temperature in this study. A charge
temperature of 830 K was realised by setting a 4.7 MPa target pressure
at injection. However, at 15 deg and 19 deg angles, the lower H 2
injector placement meant injections occurred in a comparatively cooler
region due to an in-chamber temperature gradient. This can lead to
longer ignition delays despite identical bulk pressures. To compensate
for these local variations, the trigger pressure was adjusted for the
higher angle cases to ensure pilot ( i.e., n-heptane) ignition delays
were within 0.1 ms of the 12 deg case. Similar AHRR profiles and
flame development in schlieren images confirmed comparable ambient
conditions across all injector angle configurations (see Appendix B.1).
Table 1 summarises the experiment settings, including the gas mix-
tures before spark ignition, used to achieve the different O2 concen-
trations at the start of fuel injection. The H 2 ignition delay under
tested conditions is an order of magnitude longer than that of n-
heptane [38,39]. Therefore, it is reasonable to assume that the H 2-jet
ignition occurs due to interaction with a reacting or burnt n-heptane
jet.

<!-- PDF_PAGE: 3 -->

International Journal of Hydrogen Energy 67 (2024) 172–191
174
P. Rorimpandey et al.
Fig. 1. (a) Cross-section schematic of the constant-volume combustion chamber
(CVCC). (b) Sample CVCC pressure trace data during an experiment run. Starting at
spark ignition, it highlights the following four key events: (i) premixed ambient gas
combustion, (ii) cool-down period, (iii) start of fuel injection and (iv) fuel ignition.
Table 1
Summary of the experimental conditions, and the gas composition prior to spark
ignition for each O 2 concentration.
CVCC ambient conditions
Wall temperature (K) 403
Ambient O 2 concentration (vol.%) 21, 15, 10
Ambient gas density (kg/m 3) 23.8
Ambient core gas temperature (K) 830
Ambient gas pressure (MPa) 4.70 (at 12 deg, see text for details)
Ambient gas composition
O2 product Reactants (Mole fraction, %)
C2H2 H2 O2 N2
21 vol.% 3.00 0.50 28.38 68.12
15 vol.% 3.06 0.50 22.63 73.81
10 vol.% 3.10 0.50 17.83 78.57
Fig. 2. Detailed view of the H 2 and diesel injectors layout for (a) 12 deg, (b) 15 deg,
and (c) 19 deg, representing H 2 (blue) and n-heptane jet cones (red), along with points
of jet axis and cone intersection. Grey dashed lines used to indicate the in-chamber
centreline; for 12 deg, the H 2-jet axis intersects with the centreline. (For interpretation
of the references to colour in this figure legend, the reader is referred to the web version
of this article.)
2.2. Injection conditions
This study employed separate single-hole injectors for H2 and diesel
fuel within the CVCC. This simplified the interpretation of results by
avoiding complex interactions from multi-hole injectors and provided
clearer visuals for optical diagnostics. As shown in Fig. 2 , the H 2
injector was positioned lower as the converging angle increases. The
diesel injector placement was located at different heights above the

<!-- PDF_PAGE: 4 -->

International Journal of Hydrogen Energy 67 (2024) 172–191
175
P. Rorimpandey et al.
Table 2
Summary of injection conditions.
Fuel injection conditions
Fuel H 2 n-heptane
Nozzle diameter (mm) 0.51 0.105
Fuel reservoir pressure (MPa) 20 70
Low heat. value [ 40] (MJ/kg) 120.0 43.2
Relative injector angle (deg) 12, 15, 19
Total energy output (J) 496
Hydraulic injection duration (ms) 4.7 0.6
Energy share 88% 12%
H2 injector, ensuring their axes intersected downstream at the targeted
angle.
Taking into consideration the estimated jet cone angles of 25 deg
for the H2 jet and 20 deg for the n-heptane jet, the jets are expected to
begin overlapping at varying distances depending on the target angle.
Specifically, they are predicted to start overlapping at approximately
21 mm, 17 mm, and 13 mm from the H 2 injector nozzle for 12 deg,
15 deg, and 19-deg configurations, respectively.
To minimise compositional complexities, neat n-heptane was
utilised as a single-component diesel surrogate. It was injected at
70 MPa through a custom single-hole nozzle, while the H2 injector was
a modified commercial gasoline direct-injection injector equipped with
a 0.51 mm single-hole nozzle attachment [ 38]. Compressed H 2 from
a reservoir was supplied using a pneumatic compressor, with a reser-
voir pressure of 20 MPa resulting in approximately 14 MPa pressure
upstream of the H 2 injector nozzle, with the difference attributed to
frictional losses [38]. The H2 fuel temperature is estimated to have an
upper limit of 403 K, the predicted temperature of the injector as it is in
direct contact with the chamber wall. However, while the injected H 2
gas include gases near and within the injector likely in equilibrium with
the chamber wall, it also likely includes H2 gas residing at the fuel-line
away from the chamber that will have a lower fuel temperature.
Two independent injector drivers (Zenobalti ZB-5012 and ZB-5014)
controlled the timing and energisation of the H 2 and diesel injectors,
respectively. A digital delay and pulse generator (Stanford Research
Systems DG535) precisely synchronised their start of injection (SOI).
Both fuels maintained a constant SOI timing. To assess the effects of
pilot entrainment, the injection duration of H 2 (4.7 ms) was set to
surpass that of n-heptane (0.6 ms), while fixing the SOI timings so that
n-heptane is injected 0.6 ms after H 2 SOI to ensure there is sufficient
H2 presence when the jets intersect. Additionally, the n-heptane (pilot)
injection duration was kept short to minimise the use of carbon-
intensive fuel and reduce overall carbon emissions, which interests the
wider community. These injection durations represent the minimum
achievable with the existing injectors while ensuring reliable operation.
This limit stems from the hardware itself, not the proposed approach.
The n-heptane (pilot) injection duration was kept short to minimise the
use of carbon-intensive fuel and reduce overall carbon emissions, which
interests the wider community. These injection durations represent the
minimum achievable with the existing injectors while ensuring reliable
operation. This limit stems from the hardware itself, not the proposed
approach. Under the injection and ambient conditions used in this
study, the n-heptane fuel ignites after its end-of-injection (EOI) timing,
creating a positive ignition dwell event.
The n-heptane mass flow was measured under the similar conditions
using a Bosch-tube injection rate meter. The quantity of injected H 2
gas (main) was determined in separate experiments by measuring the
change in chamber pressure after H2 injection. Table 2 summarises the
injection conditions used for this study.
2.3. Schlieren imaging
A Z-type schlieren imaging setup was used in this study to capture
the jet boundary and high-temperature reaction zone, as depicted in
Fig. 3. A schematic of the constant-volume combustion vessel (CVCC) and the high-
speed schlieren imaging optical arrangement. The light path (transparent yellow) from
the schlieren imaging light source and a model of the penetrating jet (red) are shown.
(For interpretation of the references to colour in this figure legend, the reader is referred
to the web version of this article.)
Fig. 3 . The setup involved directing collimated light from a 150 W
xenon arc lamp (Abet Technologies LS-150) through a 50 mm plano-
convex lens with a 75 mm focal length. The light then passes through a
2 mm aperture and is collimated using a 108 mm f/6 parabolic mirror.
Subsequently, the collimated light beam crosses through the CVCC and
reaches the high-speed camera through a series of mirrors. To enhance
imaging sensitivity, a 2 mm pin-hole aperture was positioned between
the second parabolic mirror and the camera lens at the beam focal
point. The high-speed camera used was a Phantom VEO 1310, equipped
with an 85 mm f#1.8 AF-D Nikkor lens. A frame rate of 30,000 frames
per second and an exposure time of1.4 μs was used, providing an image
resolution of approximately 0.13 mm per pixel.
Schlieren imaging is an optical technique that detects refractive
index gradients along the line-of-sight induced by fuel evaporative
cooling, mixing, and combustion events. These variations display as
intensity changes in the captured images [ 34]. A high-temperature
combustion event creates a sharp refractive index gradient, which
appears as a darkened region in the schlieren image, as illustrated in
Fig. 4(a). The background schlieren pattern, representing the ambient
gas, remains mostly stationary compared to the effects caused by the
fast-moving jet. Consequently, the jet-induced schlieren effects can be
identified from the background patterns by analysing the differences
between consecutive video frames [ 41], as demonstrated in Fig. 4 (b).
Fig. 4(c) shows the post-processed image, outlining the boundaries of
the non-reacting H 2 (blue) and n-heptane (red) jets, as well as the
darkened burned-zone region (green). Note that ‘non-reacting’ refers
to a flow condition where chemical reactions have yet to progress to
the point of producing a measurable schlieren effect.
2.4. Experimental parameters and notations
This study investigates the ignition and combustion characteristics
of H2-diesel DFDI under varied jet interaction angles and ambient O2
concentrations. For this study, a concise notation system, where ‘jet
interaction angle/ambient O2’ represents each case. For instance, a
DF case with a jet interaction angle of 15 deg and an ambient O2
concentration of 21 vol.% O2 is denoted as ‘15 deg/21 O2’.
During the course of this study, H 2-diesel DFDI combustion was
investigated at jet interaction angles of 12 deg, 15 deg, and 19 deg, all
conducted under ambient O2 concentrations of 21 vol.%, 15 vol.%, and
10 vol.%. A broad overview of these results are discussed in Section 3 .

<!-- PDF_PAGE: 5 -->

International Journal of Hydrogen Energy 67 (2024) 172–191
176
P. Rorimpandey et al.
Fig. 4. (a) Sample raw schlieren high-speed image, (b) image corrected by subtracting
the pixel intensity values from the previous frame, and (c) processed image showing
the non-reacting n-heptane (red) and H 2 (blue) jets, and burned zone (green). (For
interpretation of the references to colour in this figure legend, the reader is referred
to the web version of this article.)
Table 3
Summary of the specific cases investigated when studying the effects of jet interaction
angles and ambient O 2 concentration.
Cases investigated
Case name Injector angle Ambient O 2 vol.%
Jet interaction angle
12 deg/15 O 2 12 deg 15 vol.%
15 deg/15 O 2 15 deg 15 vol.%
19 deg/15 O 2 19 deg 15 vol.%
Ambient O 2 concentration
12 deg/21 O 2 15 deg 21 vol.%
12 deg/15 O 2 15 deg 15 vol.%
12 deg/10 O 2 15 deg 10 vol.%
However, specific cases were selected to investigate the effects of
varying jet interaction angles and ambientO2 concentrations. The cases
focused for each parameter are summarised in Table 3 , detailing their
settings and corresponding notations.
2.5. Dual-fuel ignition delay
In H 2-diesel DFDI combustion, there are separate ignition events:
the autoignition of n-heptane and the subsequent ignition of H 2 after
interacting with the burned n-heptane fuel.
While n-heptane autoignition leads to a distinct rise in the pressure
trace at 21 vol.% O2, the pressure rise becomes less distinguishable at
lower ambient O2 concentrations. Additionally, the rapid succession
from n-heptane to H 2 ignition implies that only a single rise in the
pressure trace is detectable, preventing discernment of the two igni-
tion events and their ignition delay timings. Consequently, high-speed
schlieren images were employed to determine the ignition delay time
of n-heptane for all experimental cases consistently. The pilot ignition
delay time is defined as the first schlieren image frame wherein a
darkened high-temperature region initially appears. Specifically, the
timing was identified when the localised intensity decreased by 10%,
providing a consistent measure across all experiments.
In DF cases, schlieren effects induced by the burned n-heptane fuel
complicate the optical evaluation of H 2 ignition, posing challenges in
determining the H2 ignition delay. As a significant portion of the heat
release occurs rapidly during H 2 ignition, the timing of H 2 ignition
is derived from the AHRR using specific thresholds. While a lower
AHRR threshold is desirable to accurately match the ignition time,
caution is exercised to ensure that the AHRR rise is attributable to H 2
ignition rather than n-heptane. The H 2 ignition event is identified by
an exceeding 150 kJ/s, with the main ignition delay defined as the
instant AHRR exceeds 30 kJ/s (above noise floor) during this rise. This
threshold, based on the peak AHRR of n-heptane-only injections not
exceeding 100 kJ/s, conservatively differentiates H 2 ignition during
DF combustion. However, it should be noted that in rapid successive
ignition events, the heat release of H 2 ignition is not strictly limited to
H2 alone, as the n-heptane autoignition heat release also contributes.
3. Results and discussion
The experiments aimed to investigate the combustion characteristics
of H 2-diesel DFDI at varied jet interaction angles and ambient O2
levels. The experiments included both DF cases and their single-fuel
(SF) references (i.e., n-heptane only injections under the same ambient
conditions).
The results, depicted in Fig. 5(a), shows the difference in measured
pilot ignition delay for DF cases compared to SF cases. The colourmap
visually represents the change in pilot ignition delay across varying jet
interaction angles and ambient O2 concentrations. Pilot ignition delay
values are denoted by either a solid dot or an open circle, indicating
whether they fall within or outside one standard deviation of their
corresponding mean SF ignition delay, respectively. The red line in the
colourmap represents zero change in pilot ignition delay, with the left
region indicating cases with increased pilot ignition delay and the right
region indicating cases of decreased pilot ignition delay. Analysis of the
colourmap reveals a consistent trend of increased pilot ignition delay
with greater jet interaction angles – consistent with results from the
natural gas-diesel dual-fuel study by Fink et al. [ 17] – and decreasing
ambient O2 concentrations. Notably, at 10 vol.% ambient O2, the DF
pilot ignition delay consistently exceeds one standard deviation beyond
the mean SF ignition delay for all jet interaction angles, highlighting the
more significant pilot ignition changes at lower O2 concentrations.
Fig. 5(b), on the other hand, presents a colourmap extrapolation of
the time difference between main and pilot ignition delay, also known
as the pilot-main interval, for the same test cases. This colourmap can
be used to quantify the transition period from pilot ignition to the
ignition of the H 2 jet, or main ignition, as defined in Section 2.5 .
The colourmap indicates that the pilot-main interval increases with
decreasing jet interaction angle and lower ambient O2 concentration,
with the slowest transition observed at a jet interaction angle of 12 deg
and 10 vol.% O2.
The findings indicate that in DF scenarios, compared to SF coun-
terparts, the pilot ignition delay lengthened with both increased jet
interaction angle and lower ambient O2 levels. A wider jet interac-
tion angle, indicating more immediate fuel interaction ( Fig. 2 ), and
lower O2, allowing time for extended jet-jet interaction before igni-
tion, contributed to this delay. Interestingly, the pilot-to-main ignition
interval shortened with larger jet interaction angles, but lengthened
with lower O2. At larger angles, extensive pre-ignition jet interaction
likely shortened the transition to main ignition once pilot combustion
commenced. Conversely, at lower O2 levels, despite promoting pre-
ignition interaction, limited the available O2 for combustion, leading
to a slower transition from pilot to main ignition.
The colourmap trends reveal non-monotonic relationships between
jet interaction angle and ambient O2 on DF ignition. As per Fig. 5 (a),
when the jet interaction angle varies from 12 deg to 19 deg at a fixedO2
concentration of 15 vol.%, the pilot ignition delay for DF cases initially
increases but plateaus at higher angles. To elucidate the underlying

<!-- PDF_PAGE: 6 -->

International Journal of Hydrogen Energy 67 (2024) 172–191
177
P. Rorimpandey et al.
Fig. 5. Interpolated colourmap depicting (a) pilot ignition delay change between dual-fuel and single-fuel counterparts, (b) pilot-to-main interval change, and (c) test matrix for
analysis. For (a), cross symbol ‘ ×’ represent measured values within one standard deviation of mean single-fuel delay, open circles ‘ ◦’ denote those outside. Red line signifies no
change in pilot ignition delay. (For interpretation of the references to colour in this figure legend, the reader is referred to the web version of this article.)
mechanisms, a comprehensive analysis of all diagnostic information
is necessary, employing a dual parametric variation approach. Here,
a systematic examination of the effects of each parameter is performed
whilst holding the other constant. First, the O2 concentration is held at
15 vol.%, and the jet interaction angle is swept from 12 deg to 19 deg.
Then, the jet interaction angle is fixed at 15 deg, whilst the ambient O2
concentration is varied from 10 vol.% to 21 vol.%. The test matrices for
these variations are depicted in Fig. 5(c), with the baseline case at the
intersection (15 deg/15 O2).
3.1. Jet interaction angle
Fig. 6(a) presents sample schlieren images for DF cases at jet inter-
action angles of 12 deg, 15 deg, and 19 deg under ambient 15 vol.%
O2 concentration. The selected images correspond to frames captured
immediately after pilot ignition delay, main ignition delay, 0.1 ms
after main ignition delay, at peak AHRR, and 0.5 ms before main EOI.
These images are used to show the ignition and flame development
characteristics under varied jet interaction angles.
While acknowledging the inherent line-of-sight limitation of
schlieren diagnostics, which precludes the precise determination of
kernel locations in a three-dimensional space, the presented images
suggest that ignition of the pilot n-heptane jet initiates near its jet
head region. At 12 deg, the pilot n-heptane jet ignites more externally
to the H 2-jet boundary, while at 15 deg and 19 deg, the n-heptane
jet appears to ignite within the H 2-jet boundary, indicating ignition
during entrainment into the H 2 jet. In the subsequent two frames, the
reaction front propagates from the region of contact, ranging from
approximately 13 to 22 mm from the nozzle. At peak AHRR, the
images reveal downstream propagation of the reaction front, reaching
the H2-jet tip in most cases. Additionally, the flame exhibits upstream
travel after ignition. As injection continues, schlieren images indicate
stabilisation of the reaction front near the nozzle before the main EOI
for all cases.
Fig. 6(b) presents the flame propagation development overtime,
showing the temporal flame penetration and recession trends relative
to pilot SOI, derived by tracking the most downstream and upstream
positions of the distinct darkened region observed in the schlieren
images. In this study, the term ‘‘flame penetration’’ refers to the most
downstream position of the flame body, while ‘‘recession’’ conversely
refers to the most upstream position. The plot shows that after ignition,
the flame spreads to match the non-reacting jet tip reference for all
cases. Regarding the recession trend, the flame recession commences
after the main jet ignition, eventually stabilising at near-nozzle region
for all cases.
For further interpretation, Fig. 7 presents a comparative analysis
of average flame penetration (Fig. 7(a)) and recession (Fig. 7(b)),
alongside their respective rates, for all cases. The plots are referenced
to a datum, defined as the time of initial flame kernel detection in
the schlieren images, facilitating a more straightforward comparison.
Analysis of the penetration rates reveal that the initial rate in the 12 deg
case is slightly lower, possibly due to an initial flame front within
the pilot n-heptane jet that ignited externally before transferring to
the main jet via their contact region. A closer look at the schlieren
frames for different jet interaction angle cases in Fig. 6(a) reveals that
at 12 deg, the burnt pilot fuel zone remains distinguishable from the
gas jet after overlapping. A distinct bulge is observable at the upper
H2 boundary even after jet interaction, gradually becoming less pro-
nounced in later stages. The observation suggests a potential influence
of the jet interaction angle on the merging of the two jets, which
affected the initial propagation of the reaction front from the ignited
diesel pilot to the main jet. This phenomenon will be further discussed
in Section 3.2, with Appendix A providing further schlieren images
comparing observation of the jet bulge between all jet interaction angle
and ambient O2 cases.
Regarding recession trends, the 12 deg case – with the greatest
distance between the region of contact between the jets and the nozzle
– exhibits a comparatively higher initial recession rate. However, the
recession rate becomes comparable to the other jet interaction angle
cases once the reaction front reaches a similar distance from the
nozzle where initial ignition kernels are first detected. While the exact
mechanisms remain unclear, it is reasonable to expect that the forces
driving the flame back towards its natural stabilisation distance (near
the nozzle at 21 vol.% O2) are alike between cases when the flame front
reaches similar distances from the nozzle [42].
Fig. 8(a) presents the average AHRR profiles for the different jet
interaction angle cases, plotted relative to their corresponding SF igni-
tion delays to analyse the changes in n-heptane ignition delay between

<!-- PDF_PAGE: 7 -->

International Journal of Hydrogen Energy 67 (2024) 172–191
178
P. Rorimpandey et al.
Fig. 6. (a) High-speed schlieren images for dual-fuel cases at jet interaction angles of 12 deg (top), 15 deg (middle), and 19 deg (bottom), under ambient 15 vol.% O2 concentration.
Highlighted are the n-heptane jet boundary (red), H 2-jet boundary (blue), and high-temperature flame (green). The n-heptane jet boundary averaged from all single-fuel runs is
overlaid on the DF frames (yellow). Axial and radial distances from the injection nozzle are represented as x and r, respectively. The first frame following main ignition delay
time is outlined by a red border. Time sequence is relative to n-heptane SOI. (b) Average flame penetration and recession paths for the same cases. Also shown is the non-reacting
H2-jet penetration path by a blue dot-dash line, the average upstream location of the n-heptane jet kernel by an orange error bar, and the start of jet-jet overlap highlighted by a
red cross. (For interpretation of the references to colour in this figure legend, the reader is referred to the web version of this article.)
DF and SF conditions while excluding SF ignition delay variation be-
tween jet interaction angles (noting difference does not exceed 0.1 ms).
Fig. 8(b) further provides the average pilot ignition delays of the DF
cases relative to their SF references and their combustion durations,
with Fig. 8 (c) showing the pilot-main intervals at the different jet
interaction angles. The AHRR profiles reveal that for all cases, the pilot
and main fuels ignite nearly simultaneously, resulting in a single AHRR
peak with a magnitude approximately 2.3 times the steady-state AHRR
of around 125 kJ/s. During the steady-state mixing-controlled phase,
the AHRR matches the heating value of the H 2 inflow at a measured
injection rate of 1.06 mg/ms. However, subtle differences in the peak
AHRR exists, with slightly higher magnitudes observed for the higher
jet interaction angle cases at ignition.
While the average values fall within the uncertainty ranges of
each other, Fig. 8(b) reveals that the pilot ignition delay time for the
12 deg case is comparatively advanced with respect to the pilot-only
case under the same ambient conditions. Conversely, the 15 deg and
19 deg jet interaction angle cases exhibit a comparative delay to their
respective SF references, with the greatest average change being 10.5%
from 15 deg. Noting the short injection duration, a positive ignition
dwell event occurs as the ignition takes place after the pilot EOI. It is
anticipated that the pilot ignition is susceptible to ambient conditions,
given the initial ambient gas entrainment increase to compensate for
the reduced mass flux at the nozzle [ 43]. In the 12 deg case, where
pilot ignition occurs external to the H 2-jet boundary, previous studies
have shown that the increased velocity and turbulence generated by a
preceding injection can influence the mixing of the subsequent injec-
tion [44]. Hence, a plausible explanation is that the turbulence from
the H2-jet may have altered the fuel-air mixing rate of the approaching
n-heptane jet, leading to the slightly advanced ignition. For the 15 deg
and 19 deg jet interaction angle cases, where the initial ignition kernel
appears within the H2-jet boundary, and considering previous research
indicating that the presence of H2 can delay diesel surrogate ignition in
a homogeneous H 2-air background [ 45,46], the observed delay aligns
with these prior findings. Since the AHRR during the premixed burn
phase depends on the mass and distribution of readily combustible fuel-
air mixture within the jet, the prolonged ignition delay in the higher
jet interaction angle cases allows for increased injection and mixing of
H2 before ignition, leading to the higher AHRR peak.
Properties of the H 2 gas itself also likely influences the extent of
change in pilot ignition delay. Comparing premixed studies on natural-
gas by Yang et al. [ 26] and H 2 by Hernandez et al. [ 23], referenced
in Section 1, show greater change in pilot ignition when the ambient
gases are premixed with natural-gas compared to H 2. The study by
Fink et al. [17], which uses a similar converging setup but at a higher
ambient temperature of 920 K, show a 20% increase in pilot ignition
delay at 20 deg jet interaction angle, greater than the 10.5% observed
in this study even under lower reactive conditions, highlighting the
potential benefit of a more robust ignition when using H 2. However,
direct comparison between studies is not possible due to differences in

<!-- PDF_PAGE: 8 -->

International Journal of Hydrogen Energy 67 (2024) 172–191
179
P. Rorimpandey et al.
Fig. 7. Average flame penetration (a) and recession (b) paths for DF cases
12 deg/15 O2 (red), 15 deg/15 O2 (blue), and 19 deg/15 O2 (green), shown from
initial kernel appearance in the schlieren images up to time of H 2 EOI, to highlight
the relative flame developments during injection. The corresponding spreading rate is
provided below the flame paths. (For interpretation of the references to colour in this
figure legend, the reader is referred to the web version of this article.)
setup, and thus further study is required using identical experimental
configurations to compare the differences in pilot ignition delay effect
between the different gas fuels.
As noted, Fig. 8(b) also presents the time intervals between 10%
(CHR10) and 90% (CHR90) of cumulative heat release, commonly used
to signify combustion duration. The pilot-main interval data in Fig. 8(c)
reflects the efficacy of the gas jet ignition by the n-heptane jet. While
recognising that the average values fall within one standard deviation
of each other, the data suggest that the combustion duration and pilot-
main interval are longest for the 12 deg case. The data for the 12 deg
case also exhibits the least fluctuation, indicating higher ignition sta-
bility. Considering that n-heptane represents 12% of the energy share
under the experimental conditions (Table 2), the slightly advanced
timing of pilot ignition and occurring before interaction with the H 2-
jet boundary, along with the slower initial flame penetration, all likely
contributes to its longer combustion duration at 12 deg. Additionally,
the earlier jet interaction before ignition for the 15 deg and 19 deg
configuration (Section 2.2), due to more upstream crossover, may be
more conducive to faster flame propagation through the more premixed
mixture after ignition, leading to a shorter combustion duration.
3.2. Ambient O2 concentration
Fig. 9(a) presents schlieren images for DF cases at ambient O2
concentrations of 21 vol.%, 15 vol.%, and 10 vol.%, with a fixed jet
interaction angle of 15 deg, following the format of Fig. 6(a). In the
21 vol.% case, pilot n-heptane-jet ignition occurs outside the H 2-jet
boundary, spreading the reaction front from the pilot to the main
jet through the contact region. By peak AHRR, the flame engulfs the
H2-jet tip and fully recedes to the nozzle 0.4 ms after peak AHRR,
enveloping the H 2 jet until main EOI. In the 15 vol.% case, pilot n-
heptane-jet ignition occurs close to or within the H 2-jet boundary. The
flame reaches the H2-jet tip at peak AHRR but has not yet reached the
H2 nozzle 0.4 ms after peak AHRR. By 0.5 ms before EOI, the flame
stabilises near the nozzle but does not attach to it. In the 10 vol.%
case, the pilot n-heptane jet ignites within the H2-jet boundary, near the
H2-jet centreline. The flame reaches the H 2-jet tip by peak AHRR and
stabilises upstream 0.4 ms after, only to stabilise closer to the nozzle
0.5 ms before main EOI. When observing the frame at 3.30 ms aSOI
for the 10 vol.% case, a separate kernel is seen to appear upstream
of the initial H 2 flame lift-off, growing and merging with the reacting
jet downstream by 3.60 ms aSOI; this phenomenon will be discussed
further in Section 3.3. Across all ambient O2 cases at a fixed jet
interaction angle of 15 deg, no discernible bulge is seen formed after
jet interaction.
Fig. 9(b) presents the mean flame penetration and recession paths
across the H 2 jet, along with the mean spatial and temporal start
of jet-jet overlap for various ambient O2 concentrations, maintaining
the format of Fig. 6(b). The plot shows that following ignition, flame
penetration distance increase to match the non-reactive jet penetration
for all cases. At 21 vol.%O2, the n-heptane jet ignites outside the H2 jet,
with flame propagation commencing shortly after the jets are observed
to overlap with prior minimal interaction. Conversely, the 15 vol.%
and 21 vol.% O2 cases display delays between jet overlap and ignition,
spanning approximately 0.55 ms and 1.03 ms, respectively, before
flame propagation ensues. The distance at which the flame stabilises
from the nozzle increases with decreasing ambient O2, with notably
substantial run-to-run variations observed at 10 vol.% O2.
In Fig. 10(a) and (b), mean flame penetration and recession rates,
respectively, are presented for each ambient O2 concentration, along-
side their respective trends. These plots are referenced to a datum
defined as the time of initial flame kernel detection in the schlieren
images. Comparing penetration rates at 21 vol.% and 15 vol.% O2,
flame penetrations are similar despite the difference in pilot n-heptane-
jet ignition location relative to the H2 boundary. The initial penetration
rate trend for 15 deg/21 O2 differs with that of 12 deg/15 O2 (see

<!-- PDF_PAGE: 9 -->

International Journal of Hydrogen Energy 67 (2024) 172–191
180
P. Rorimpandey et al.
Fig. 8. (a) AHRR for DF cases 12 deg/15 O2 (red), 15 deg/15 O2 (blue), and
19 deg/15 O2 (green), relative to SF ignition delay to exclude its variation between
jet interaction angles (noting difference does not exceed 0.1 ms). Mean ignition delay
shown with uncertainty of 1 standard deviation plotted along horizontal time-axis. (b)
Pilot ignition delay (blue), combustion duration CHR90-CHR10 (orange), and (c) pilot-
main interval for similar DF cases. Pilot ignition delay shown relative to SF ignition
delay, highlighting the changes in pilot ignition delay between SF and DF cases. (For
interpretation of the references to colour in this figure legend, the reader is referred
to the web version of this article.)
Fig. 7(a)), despite pilot ignition occurring externally to the H 2-jet
boundary in both cases. This suggests that the configuration of the
jet interaction angle has an impact on the initial spreading of the
reaction front to the main jet from the pilot flame kernel, with a larger
jet interaction angle appearing to promote better merging of the jets
and initial flame propagation under the current test conditions. In the
10 vol.% case, the combustion front progression time relative to the
H2-jet tip is the longest among ambient O2 conditions, displaying a
comparatively faster rate during the period when the flame is still
progressing, while other cases have already reached their respective tip
boundaries.
As ambient O2 levels vary, and the relative position of pilot-induced
ignition to the natural flame stabilisation distance changes, reces-
sion trends show significant differences. Recession rates are generally
greater for higher ambient O2 cases with closer flame stabilisation
distances to the nozzle during the jet recession period, consistent with
earlier discussion that a greater distance between the ignition site and
the natural stabilisation distance results in a stronger driving force
acting on the flame. Occasional spikes observed in the 15 vol.% and
10 vol.% flame recession rates correspond to the appearance of the
upstream kernel, quickly shifting the flame position upstream that leads
to higher recession rate values.
Fig. 11(a) presents the AHRR profiles for different ambient O2
concentration cases. The figure shows that the measured peak AHRR
increases by 11% from 21 vol.% O2 to 15 vol.% O2, indicative of
greater premixed combustion and aligning with the conventional diesel
combustion trend of higher peak pressure with longer ignition delay.
However, the peak AHRR becomes less pronounced at lowerO2 concen-
trations, decreasing by 26% from 15 vol.% O2 to 10 vol.% O2, despite a
further increase in ignition delay. This phenomenon may be associated
with altered equivalence ratio distributions resulting from the lower
O2 levels, leading to a longer persistence of fuel-rich zones [32,47].
The AHRR levels off at a consistent level during the mixing-controlled
combustion phase, in line with the expected H 2 mass flow. However,
for the 10 vol.% O2 case, a smaller secondary peak emerges during the
mixing-controlled phase. This coincides with the appearance and up-
stream propagation of a separate flame kernel towards the downstream
reaction zone, which will be further discussed in Section 3.3.
Fig. 11(b) additionally presents the average pilot ignition delays
of the DF cases relative to their SF references and their combustion
durations, and Fig. 11(c) shows the pilot-main intervals for the different
ambient O2 concentrations. Again, it is noted that these values fall
within the standard deviations of each other. Trends in average pilot
ignition delays show increased periods of delay relative to their SF
references under similar ambient conditions for lower ambient O2
cases, with the extent of this delay increasing from 0.15 ms at 15 vol.%
O2 to 0.35 ms at 10 vol.% O2. Conversely, the mean pilot ignition delay
at 21 vol.% O2 advances by 0.11 ms compared to its SF reference.
The pilot-main interval is shortest at 21 vol.% O2 and longest
at 10 vol.% O2. However, the combustion duration (CHR90-CHR10)
shows the opposite trend. The 21 vol.% case burns slowest, while the
15 vol.% and 10 vol.% O2 cases have similar and shorter durations.
The 15 deg/21 O2 case, despite its faster initial flame penetration
rate and shorter pilot-main interval, has the longest combustion du-
ration. As in jet interaction cases, the longer combustion duration at
21 vol.% O2 likely stems from earlier pilot diesel autoignition before
H2 interaction, leading to an extended overall process. For lower O2
cases, prolonged periods of jet interaction before ignition promotes
faster flame propagation, contributing to shorter combustion durations.
In the 10 vol.% O2 case, the lower total heat release (evident in
AHRR profiles) compensates for a slower flame spread, resulting in a
combustion duration comparable to 15 vol.% O2.

<!-- PDF_PAGE: 10 -->

International Journal of Hydrogen Energy 67 (2024) 172–191
181
P. Rorimpandey et al.
Fig. 9. (a) High-speed schlieren images for dual-fuel cases at ambient O2 concentrations of 21 vol.% (top), 15 vol.% (middle), and 10 vol.% (bottom), at a fixed jet interaction
angle of 15 deg. Highlighted are the n-heptane jet boundary (red), H 2-jet boundary (blue), and high-temperature flame (green). The n-heptane jet boundary averaged from all
single-fuel runs is overlaid on the DF frames (yellow). Axial and radial distances from the injection nozzle are represented as x and r, respectively. The first frame following main
ignition delay time is outlined by a red border. Time sequence is relative to n-heptane SOI. (b) Average flame penetration and recession paths for same cases. Also shown is the
non-reacting H 2-jet penetration path by a blue dot-dash line, the average upstream location of the n-heptane jet kernel by an orange error bar, and the start of jet-jet overlap
highlighted by a red cross. (For interpretation of the references to colour in this figure legend, the reader is referred to the web version of this article.)
3.3. Upstream kernel
As discussed in Section 3.2 , a distinct kernel appears upstream of
the initial H2 flame lift-off in the 15 deg/10 O2 case. Fig. 12 provides a
temporal analysis of the relationship between the flame recession front
position, AHRR, and flame development within the H 2 jet to further
understand this phenomenon. Two high-speed schlieren sequences from
the 15 deg/10 O2 runs are used for this analysis, highlighting the
upstream kernel’s formation and growth. Time instances are presented
relative to the initial kernel appearance, aiding in a clear understanding
of the flame development evolution.
The AHRR profile in Fig. 12 (a) exhibits two distinct peaks. Com-
paring the AHRR profile against the schlieren frames reveal that the
emergence of the upstream kernel coincides roughly with a period
where the AHRR value begins decreasing after the initial peak. The
AHRR is then observed to peak again as the upstream kernel grows and
merges with the downstream flame body. This indicates a correlation
between the upstream kernel formation and the observed fluctuations
in the AHRR profile. However, when the upstream flame kernel appears
before the downstream flame body fully develops and reaches the
H2-jet tip, as shown in Fig. 12 (b), the associated heat release is not
discernible in the AHRR profile.
The high-speed schlieren images in Fig. 12 include the spatial trajec-
tory of the n-heptane jet’s outer boundary over time, derived from the
SF reference case. These images clearly show a noticeable radial shift
of the n-heptane jet as its injection ceases, interacting with the still-
injecting H2 jet. This observation suggests an interaction between the
actively injecting H 2 jet and the surrounding low-momentum ambient
gases, leading to a radial shift and entrainment of the n-heptane jet.
Previous multiple-injection studies [ 34,44] have shown that the pro-
gression of the reaction from the first injection can significantly impact
the mixing, ignition, combustion, and emission formation of subsequent
injections. In this specific case, the entrained n-heptane mixture likely
includes unreacted, or potentially reacted fuel in quantities insufficient
to induce detectable schlieren effects, but still sufficient to induce the
formation of a separate flame kernel upstream, impacting the flame
stabilisation and heat release characteristics. Noteworthy is that in
a separate study [ 32], the UNSW group used laser-induced plasma
to ignite H 2 under compression-ignition engine-relevant conditions,
including at an ambient O2 level of 21 vol.% and temperature of 800 K.
Despite a slight temperature difference, no isolated upstream kernel
from the main flame body was observed to form after its establish-
ment. This aligns with observations from this study suggesting that
entrainment of the pilot n-heptane jet is necessary for upstream kernel
formation.

<!-- PDF_PAGE: 11 -->

International Journal of Hydrogen Energy 67 (2024) 172–191
182
P. Rorimpandey et al.
Fig. 10. Average flame penetration (a) and recession (b) paths for DF cases
15 deg/21 O2 (red), 15 deg/15 O2 (blue), and 15 deg/10 O2 (green), shown from
initial kernel appearance in the schlieren images up to time of H 2 EOI, to highlight
the relative flame developments during injection. The corresponding spreading rate is
provided below the flame paths. (For interpretation of the references to colour in this
figure legend, the reader is referred to the web version of this article.)
Fig. 11. (a) AHRR for DF cases 15 deg/21 O2 (red), 15 deg/15 O2 (blue), and
15 deg/10 O2 (green), relative to pilot-fuel SOI. Mean ignition delay shown with
uncertainty of 1 standard deviation plotted along horizontal time-axis. (b) Pilot
ignition delay (blue), combustion duration CHR90-CHR10 (orange), and (c) pilot-main
interval for similar DF cases. Pilot ignition delay shown relative to SF ignition delay,
highlighting the changes in pilot ignition delay between SF and DF cases. (For
interpretation of the references to colour in this figure legend, the reader is referred
to the web version of this article.)

<!-- PDF_PAGE: 12 -->

International Journal of Hydrogen Energy 67 (2024) 172–191
183
P. Rorimpandey et al.
Fig. 12. H2 flame recession front evolution and AHRR (top), and high-speed schlieren
images (bottom), from sample runs of 15 deg/10 O2, during the appearance and
development of the upstream kernel when the downstream reaction zone has (a)
reached the H 2-jet tip, and (b) still propagating downstream towards the H 2-jet tip.
Timing of each schlieren frame indicated by the position of their respective coloured
circle (shown on bottom left corner of each frame) along the flame recession and AHRR
plot. Yellow circles are used to identify the secondary kernel, with yellow arrows to
indicate the movement of the kernel towards the initial reaction zone. Yellow lines
used to indicate n-heptane spatial trajectory. (For interpretation of the references to
colour in this figure legend, the reader is referred to the web version of this article.)
3.4. Pilot injection duration and relative jet momentum
The explanation for the observed results in the previous sections
centres around the presumed role of relative jet momentum. As pro-
posed earlier, the short injection duration may have led to the suscep-
tibility of pilot ignition to ambient conditions influenced by the still
actively injecting main jet after the EOI of the pilot fuel. To further
investigate the critical role of relative jet momentum in the observed
flame dynamics, this section explores its influence by adjusting the
injection duration of the pilot fuel. Specifically, the injection period is
extended from 0.6 ms to 1.8 ms. The prolonged injection duration is
expected to modify the jet dynamics, in addition to creating a negative
ignition dwell event where pilot combustion initiates before its EOI
timing, in contrast to the cases presented thus far in this study where
the pilot fuel ignites after its EOI timing, creating a positive ignition
dwell event [48].
Fig. 13 (a) presents the schlieren images for both negative and
positive dwell events. In comparison to the positive ignition dwell case,
the negative dwell event shows an initial ignition kernel concentrated
at the upper boundary of the n-heptane jet periphery, contrasting with
the more uniformly distributed kernel observed across the jet head
region in the positive ignition dwell case. In the negative ignition dwell
case, the upstream flame stabilisation position appears comparatively
more downstream in the lead-up to main EOI compared to the positive
ignition dwell event.
Fig. 14 presents higher temporal resolution schlieren images that
highlight the upstream flame recession characteristics for the same
selected runs. Comparing the spatial position of the pilot n-heptane
jet against the SF reference (yellow dot-dash line) in the negative
ignition dwell case reveals a radial shift for the n-heptane jet, albeit to
a lesser degree than that observed for the positive ignition dwell event
at similar time steps. In both schlieren sequences, an isolated ignition
kernel forms upstream and subsequently merges with the downstream
reaction zone. Notably, for the negative ignition dwell case, the kernel
appears closer to the upper edge of then-heptane jet boundary where it
intersects the H 2 jets, while the positive ignition dwell case exhibits a
more central and upstream kernel formation. Although the underlying
mechanisms for these observed differences are not well-understood and
require further investigation, these findings align with the perceived
role that relative jet momentum has, while not excluding other factors.
Fig. 13(b) presents the mean flame penetration and recession paths
for both ignition dwell cases. The plot shows that the negative ignition
dwell case exhibits an ignition location more downstream than the
positive ignition dwell case, possibly due to the delayed decay of n-
heptane jet momentum in the negative ignition dwell event, given its
longer injection duration. When examining the recession trends for
both events, both cases show highly variable flame recession paths,
attributed to the presence of upstream kernels causing a rapid decrease
in flame stabilisation distances when formed. The plot also shows that
the final flame stabilisation distance is further downstream for the
negative ignition dwell case compared to the positive ignition dwell
case at the same timings. The observed effects of injection duration
variation, which directly influences the onset of jet momentum decay,
support the notion that relative jet momentum impacts the occurrence
and location of upstream flame kernels.
Finally, Fig. 15 compares the ignition delays of the ignition dwell
events to their SF references. Unlike the positive dwell case, the neg-
ative dwell case exhibits a pilot ignition delay comparable to the SF
reference, aligning with the expected reduced susceptibility of the pilot
ignition delay with a longer injection duration.
3.5. Further discussion
The results presented in this study were conducted under relatively
steady ambient conditions within the CVCC, where there is little turbu-
lence in the ambient gases during fuel combustion events. The results
from the study by Fink et al., as discussed in Section 1 , used an RCEM
setup that have shown to produce quasi turbulent-free conditions near
top-dead centre (TDC) [ 49,50]. However, under engine applications,
the presence of in-cylinder swirl can influence the jet trajectory, with
the added ambient fluid motion likely to divert the jets apart or redirect
the jets towards each other [ 51]. Further study is required to assess
whether the effects of jet entrainment on pilot ignition, as observed in
this and past studies, is observable with ambient turbulence similar to
engine operating conditions.
This study used n-heptane as a diesel surrogate to reduce the
compositional complexities and variables associated with commercial
fuels, in addition to having considerably known properties [ 19,52,53].
However, with greater decarbonisation potential when using more
environmentally sustainable diesel sources, such as biodiesel [ 35,54],
further study is recommended using the cleaner fuel as the pilot fuel,
which are known to have distinct combustion characteristics from
conventional diesel [ 55,56] and thus may exhibit varying dual-fuel
ignition and combustion behaviour.

<!-- PDF_PAGE: 13 -->

International Journal of Hydrogen Energy 67 (2024) 172–191
184
P. Rorimpandey et al.
Fig. 13. (a) High-speed schlieren images for dual-fuel cases where the pilot n-heptane jet undergoes negative ignition dwell (top) and positive ignition dwell (bottom), under
ambient 10 vol.% O2 concentration and a fixed jet interaction angle of 15 deg. Highlighted are the n-heptane jet boundary (red), H 2-jet boundary (blue), and high-temperature
flame (green). The n-heptane jet boundary averaged from all single-fuel runs is overlaid on the DF frames (yellow). Axial and radial distances from the injection nozzle are
represented as x and r, respectively. The first frame following main ignition delay time is outlined by a red border. Time sequence is relative to n-heptane SOI. (b) Average flame
penetration and recession paths for same cases. Also shown is the non-reacting H 2-jet penetration path by a blue dot-dash line, the average upstream location of the n-heptane jet
kernel by an orange error bar, and the start of jet-jet overlap highlighted by a red cross. (For interpretation of the references to colour in this figure legend, the reader is referred
to the web version of this article.)
Regarding real-world applications, the use of a H 2-diesel DFDI
engine can be beneficial for hydrogen carriers. Since the transported
liquefied H2 are susceptible to boil-off [ 57], a H 2-diesel DFDI engine
can utilise the H 2 boil-off as fuel, subsequently reducing diesel usage
and further lowering carbon emissions. With hydrogen carriers already
in use to export hydrogen between Australia and Japan [ 58], it is ben-
eficial to conduct further constant-volume studies under marine engine
conditions, which can reach in-cylinder pressures of up to 20 MPa [59],
beyond the equipment capabilities used in this study.
Finally, further work with high-fidelity measurements and numer-
ical simulations can help provide measurements that are difficult to
obtain experimentally. Indeed, existing numerical simulation studies on
H2-diesel dual-direct combustion have already presented measurements
generally difficult to obtain under experimental conditions [60–63]. For
this study, having information such as equivalence ratio distribution
within the fuel jets can help better explain the observations made in
this study, including the emergence of an upstream kernel beyond
flame stabilisation at low ambient O2 concentrations. Additionally,
limitations in schlieren imaging means the process of flame propagation
from pilot to H 2 is not clearly observable when the jets have merged,
and thus the mechanism driving H 2 ignition is not fully understood.
Therefore, the use of more complex high-fidelity numerical studies in
future works can help enhance the findings presented in this study.
While the results from this study is useful for model validation, parallel
experimental efforts with multi-species optical diagnostics are likely
required to provide further data for validation.
4. Summary and conclusions
This study investigated the ignition and combustion characteristics
of intersecting n-heptane (pilot fuel, diesel surrogate) and H 2 jets
under engine-relevant high pressure, high temperature conditions. The
experiments were conducted in an optically accessible constant-volume
combustion chamber (CVCC) using high-speed schlieren imaging and
pressure trace analysis. Single-nozzle injectors arranged with converg-
ing angles ranging from 12 deg to 19 deg were employed for fuel

<!-- PDF_PAGE: 14 -->

International Journal of Hydrogen Energy 67 (2024) 172–191
185
P. Rorimpandey et al.
Fig. 14. Extra schlieren frames from Fig. 13 (a) with smaller time intervals, using
similar formatting, highlighting the flame upstream movement for pilot negative dwell
(left column) and positive dwell (right column).
Fig. 15. Pilot ignition delay for DF cases 15 deg/10 O2 with negative and positive
ignition dwell. Pilot ignition delay is shown relative to their corresponding SF ignition
delay, to highlight the changes in pilot ignition delay between SF and DF cases.
injection. The pilot fuel interacted with the H 2 jet within the CVCC,
with the injection duration of H 2 (4.7 ms) set to surpass that of n-
heptane (0.6 ms), as well as injecting n-heptane 0.6 ms after H 2 SOI
to ensure sufficient H 2 presence when the jets intersect. The influence
of ambient O2 concentration on the ignition and combustion behaviour
was assessed and compared to reference cases involving only n-heptane
injections under identical conditions.
The following conclusions apply under the conditions investigated
in this study:
1. The interaction between the H 2 jet and the pilot fuel can affect
the pilot ignition characteristics. Unlike studies on other fuels,
no quenching of pilot fuel was observed with the H 2 jets. How-
ever, the presence of the H 2 jet could either advance or delay
the pilot fuel’s ignition compared to the reference case without
the H2 jet.
2. When the pilot n-heptane jet ignited before directly interact-
ing with the H 2 jet, its ignition delay was slightly advanced
compared to the single-fuel (SF) reference case. The advance-
ment was attributed to the enhanced fuel-air mixing of the
approaching n-heptane by the turbulence induced by the H 2
jet. Conversely, when the pilot n-heptane jet ignited only after
interacting with the H 2 jet, a slight delay in ignition delay
relative to the SF reference was observed.
3. Under the test conditions, the H 2-jet ignition occurred after in-
teraction with the ignited pilot fuel. The reaction front transition
period from pilot to main jet was significantly influenced by
the jet interaction angle. Configurations that promote greater
jet overlap generally shortened the ignition transition period,
even in cases where pilot ignition was slightly delayed by the
interaction. This is potentially attributed to the better merging
and more extensive interaction between the jets, allowing the
flame to propagate more readily once ignition has occurred.
4. The reaction front transition period also depends on the reac-
tivity of the ambient condition. A more prolonged transition
period is required after successful ignition under less reactive
conditions, such as a lower ambient O2 level.
5. At 10 vol.% O2 concentration, the least reactive ambient con-
dition tested in this study, considerable run-to-run variability
in flame stabilisation and heat release was observed. This be-
haviour may be attributed to the interaction between the contin-
uously injecting H2 jet with the remnants of the pilot n-heptane
jet, leading to the formation of a flame kernel upstream of
the main flame body. The kernel merges with the downstream
reaction zone, resulting in the observed flame stabilisation and
associated AHRR variability.
CRediT authorship contribution statement
Patrick Rorimpandey: Investigation, Writing – original draft, Writ-
ing – review & editing. Guanxiong Zhai: Writing – review & editing.
Sanghoon Kook: Writing – review & editing, Project administration,
Funding acquisition. Evatt R. Hawkes: Writing – review & editing,
Project administration, Funding acquisition. Qing Nian Chan: Super-
vision, Writing – original draft, Writing – review & editing, Project
administration, Funding acquisition, Conceptualisation.
Declaration of competing interest
The authors declare that they have no known competing finan-
cial interests or personal relationships that could have appeared to
influence the work reported in this paper.

<!-- PDF_PAGE: 15 -->

International Journal of Hydrogen Energy 67 (2024) 172–191
186
P. Rorimpandey et al.
Fig. 16. Sample schlieren images from three experimental runs at jet interaction angles of (left to right) 12 deg, 15 deg, and 19 deg, at ambient O2 concentrations of (top to
bottom) 21 vol.%, 15 vol.%, 10 vol.%, all taken at 2.90 ms after pilot SOI. An example of the jet bulge is indicated in the first frame of 12 deg/21 O2 (top left corner) below the
cyan arc.
Acknowledgements
The financial support by the Australian Renewable Energy Agency
(ARENA) is gratefully appreciated. The first author acknowledges the
support of the Commonwealth through the Australian Government
Research Training Program Scholarship. The corresponding author ac-
knowledges the support of the Commonwealth Scientific and Indus-
trial Research Organisation (CSIRO) International Hydrogen Research
Program Mid-Career Fellowship.

<!-- PDF_PAGE: 16 -->

International Journal of Hydrogen Energy 67 (2024) 172–191
187
P. Rorimpandey et al.
Fig. 17. (a) High-speed schlieren images of single-fuel cases at jet interaction angles of 12 deg (top), 15 deg (middle), and 19 deg (bottom), under ambient 15 vol.% O2
concentration. Highlighted are the n-heptane jet boundary (red) and high-temperature flame (green). Axial and radial distances from the injection nozzle are represented as x and
r, respectively. The first frame following pilot ignition delay time is outlined by a red border. Frames are shown at equal times after n-heptane SOI. Yellow lines are used to show
the estimated spray angle. Ignition delay (b) and AHRR (c) for these cases are also shown. (For interpretation of the references to colour in this figure legend, the reader is
referred to the web version of this article.)
Appendix A. Observation of jet bulge from high-speed schlieren
images
Fig. 16 shows three sample runs at 2.90 ms after pilot SOI from all
jet interaction angle cases of 12 deg, 15 deg, and 19 deg, under all
ambient O2 concentrations of 21 vol.%, 15 vol.%, and 10 vol.%. This
is to highlight that the observed jet bulge in the upper boundary of
the H 2 jet seen for 12 deg, correlating to the nature of the merging
jets influenced by the lower jet interaction angle, as discussed in
Section 3.1 , is not as prominent in other jet interaction angles. This
is consistent in all ambient O2 concentrations. An example of the jet
bulge is indicated below the cyan arc in the first frame of 12 deg/21O2
in Fig. 16.
Appendix B. Single-fuel reference cases: n-heptane
B.1. Jet interaction angle
Fig. 17 (a) shows sample high-speed schlieren frames of SF cases
at 12 deg, 15 deg, and 19 deg jet interaction angle under ambient
15 vol.% O2 concentration, shown at equal time instances after start-
of-injection (SOI). The frame following pilot ignition is shown by a
red border. The schlieren images in Fig. 17 (a) show that n-heptane
combustion is similar at all angles. At 0.7 ms aSOI, after end-of-
injection (EOI), no ignition of the n-heptane jet is observed for all jet
interaction angles. The distinct darkened region of high-temperature
ignition appears at 0.8 ms aSOI at the jet-head after EOI for all angles,
with flame recessing after EOI.

<!-- PDF_PAGE: 17 -->

International Journal of Hydrogen Energy 67 (2024) 172–191
188
P. Rorimpandey et al.
Fig. 18. (a) High-speed schlieren images of single-fuel cases at ambient O2 concentrations of 21 vol.% (top), 15 vol.% (middle), and 10 vol.% (bottom), at a fixed jet interaction
angle of 15 deg. Highlighted are the n-heptane jet boundary (red) and high-temperature flame (green). Axial and radial distances from the injection nozzle are represented as x
and r, respectively. The first frame following pilot ignition delay time is outlined by a red border. Frames are shown at equal times after n-heptane SOI. Yellow lines are used to
show the estimated spray angle. Ignition delay (b) and AHRR (c) for these cases are also shown. (For interpretation of the references to colour in this figure legend, the reader
is referred to the web version of this article.)
Considering the injector is angled further downward radially, the
downstream axial penetration (relative to the horizontal/H 2 injector
axis) is relatively shorter for larger jet interaction angles. As shown
in Fig. 17(a), at the same time instances, the n-heptane jet penetrates
further axially at a 12 deg angle than at a 15 deg angle, and further at
a 15 deg angle than at a 19 deg angle.
Fig. 17 presents the measured pilot ignition delay in relation to
the pilot EOI ( Fig. 17(b)), as well as the AHRR relative to pilot SOI
(Fig. 17 (c)) for SF cases at the varying jet interaction angles. As
noted in Section 2.1 , the ambient pressure is adjusted to ensure the
difference in pilot ignition delay does not exceed 0.1 ms between jet
interaction angles. This is because the fuel is injected into a more off-
centre location within the CVCC, where the ambient gases are cooler
if the trigger pressure were to kept constant, increasing ignition delay.
Fig. 17(c) shows that the AHRR is similar across each jet interaction
angle.
B.2. Ambient O2 concentration
Fig. 18(a) shows sample schlieren frames of SF cases at 21 vol.%,
15 vol.%, and 10 vol.% ambient O2 concentrations. These images were
taken with the injector positioned at a fixed angle of 15 deg relative
to horizontal axis, shown at equal time instances after SOI. The image
following pilot ignition is highlighted with a red border. Images reveal
that the time before high-temperature ignition is longer at lower O2
concentrations, as expected. The n-heptane jet initially appears trans-
parent, a feature typical of low-temperature ignition [ 41,53], before a
darkened region appears at the jet head, indicating high-temperature
ignition.

<!-- PDF_PAGE: 18 -->

International Journal of Hydrogen Energy 67 (2024) 172–191
189
P. Rorimpandey et al.
Fig. 19. (a) High-speed schlieren images of single-fuel cases with negative ignition dwell (top) and positive ignition dwell (bottom), under ambient 10 vol.% O2 concentration
and a fixed jet interaction angle of 15 deg. Highlighted are the n-heptane jet boundary (red) and high-temperature flame (green). Axial and radial distances from the injection
nozzle are represented as x and r, respectively. The first frame following pilot ignition delay time is outlined by a red border. Frames are shown at equal times after n-heptane
SOI. Yellow lines are used to show the estimated spray angle. Ignition delay (b) and AHRR (c) for these cases are also shown. (For interpretation of the references to colour in
this figure legend, the reader is referred to the web version of this article.)
Fig. 18 shows the measured pilot ignition delay relative to pilot EOI
(Fig. 18(b)), as well as AHRR relative to pilot SOI ( Fig. 18(c)) for SF
cases at varied ambient O2 concentration. Fig. 18(b) shows a negative
correlation between pilot ignition delay and ambient O2 concentration.
Specifically, the ignition delay decreases by 32.3% as the ambient
O2 concentration increases from 10 vol.% to 15 vol.%, and further
decreases by 20.8% at 21 vol.% O2. In contrast, Fig. 18 (c) reveals a
positive correlation between peak AHRR and ambientO2 concentration.
The peak AHRR decreases by 24.3% as the ambient O2 concentration
decreases from 21 vol.% to 15 vol.%, and decreases further by 49.6%
at 10 vol.% O2.
B.3. Pilot injection duration
Fig. 19 (a) shows sample high-speed schlieren frames of SF cases
with positive and negative ignition dwell, under ambient 10 vol.% O2
concentration and 15 deg jet interaction angle, shown at equal time
instances after SOI. The frame following pilot ignition is shown by a
red border. The schlieren frames show the n-heptane jet igniting at the
jet-head for both dwell cases. The longer injection duration for negative
dwell means the axial penetration at same time instances surpasses
positive dwell after EOI, due to continual momentum induced during
injection. For negative dwell, a flame-lift-off is visible around 35 mm
from H 2 nozzle during injection and lingers after EOI, as shown at
2.40 ms.
Fig. 19 also shows the measured pilot ignition delay relative to pilot
EOI ( Fig. 19 (b)), and AHRR relative to pilot SOI ( Fig. 19 (c)) for SF
cases with positive and negative ignition dwell. Fig. 19 (b) shows that
ignition delay between positive and negative dwell are within 0.1 ms.
Fig. 19 (c) shows that the peak AHRR increases by a magnitude of
2.4 for negative dwell compared to positive dwell, due to the longer
injection duration of negative dwell. However, the AHRR does not show
a distinct mixing-controlled combustion phase for either case.
References
[1] Yip HL, Srna A, Yuen ACY, Kook S, Taylor RA, Yeoh GH, Medwell PR, Chan QN.
A review of hydrogen direct injection for internal combustion engines: towards
carbon-free combustion. Appl Sci 2019;9(22):4842.
[2] Nguyen VN, Nayak SK, Le HS, Kowalski J, Deepanraj B, Duong XQ, Truong TH,
Tran VD, Cao DN, Nguyen PQP. Performance and emission characteristics of
diesel engines running on gaseous fuels in dual-fuel mode. Int J Hydrog Energy
2024;49:868–909.
[3] Dimitriou P, Tsujimura T. A review of hydrogen as a compression ignition engine
fuel. Int J Hydrog Energy 2017;42(38):24470–86.
[4] Lu X, Han D, Huang Z. Fuel design and management for the control of
advanced compression-ignition combustion modes. Prog Energy Combust Sci
2011;37(6):741–83.
[5] Xia C, Zhu Y, Liu D, Zhou S, Feng Y, Shi J, Jun Y. Newly developed detailed urea
decomposition mechanism by marine engine urea-SCR system crystallization test
and DFT calculations. Chem Eng J 2023;470:144176.

<!-- PDF_PAGE: 19 -->

International Journal of Hydrogen Energy 67 (2024) 172–191
190
P. Rorimpandey et al.
[6] Wu X, Feng Y, Gao Y, Xia C, Zhu Y, Shreka M, Ming P. Numerical simulation
of lean premixed combustion characteristics and emissions of natural gas-
ammonia dual-fuel marine engine with the pre-chamber ignition system. Fuel
2023;343:127990.
[7] Liu X, Seberry G, Kook S, Chan QN, Hawkes ER. Direct injection of hydrogen
main fuel and diesel pilot fuel in a retrofitted single-cylinder compression ignition
engine. Int J Hydrog Energy 2022;47(84):35864–76.
[8] Gültekin N, Ciniviz M. Examination of the effect of combustion chamber geome-
try and mixing ratio on engine performance and emissions in a hydrogen-diesel
dual-fuel compression-ignition engine. Int J Hydrog Energy 2023;48(7):2801–20.
[9] Frankl S, Gleis S, Karmann S, Prager M, Wachtmeister G. Investigation of
ammonia and hydrogen as CO 2-free fuels for heavy duty engines using a high
pressure dual fuel combustion process. Int J Engine Res 2021;22(10):3196–208.
[10] Bhagat RN, Sahu KB, Ghadai SK, Kumar CB. A review of performance and
emissions of diesel engine operating on dual fuel mode with hydrogen as gaseous
fuel. Int J Hydrog Energy 2023;48(70):27394–407.
[11] Liu X, Yang L, Chan QN, Kook S. Split injection strategies for a high-pressure
hydrogen direct injection in a small-bore dual-fuel diesel engine. Int J Hydrog
Energy 2024;57:904–17.
[12] McTaggart-Cowan G, Mann K, Huang J, Singh A, Patychuk B, Zheng ZX,
Munshi S. Direct injection of natural gas at up to 600 bar in a pilot-ignited
heavy-duty engine. SAE Int J Engines 2015;8(3):981–96.
[13] Florea R, Neely GD, Abidin Z, Miwa J. Efficiency and emissions characteristics of
partially premixed dual-fuel combustion by co-direct injection of NG and diesel
fuel (DI 2). In: SAE 2016 world congress and exhibition. SAE Int; 2016.
[14] Neely GD, Florea R, Miwa J, Abidin Z. Efficiency and emissions characteristics of
partially premixed dual-fuel combustion by co-Direct injection of NG and siesel
Fuel (DI 2) - Part 2. In: WCX 17: SAE world congress experience. SAE Int; 2017.
[15] White TR. Simultaneous diesel and natural gas injection for dual-fuelling
compression-ignition engines (Ph.D. thesis), University of New South Wales
Sydney, Australia; 2006.
[16] Fink G, Jud M, Sattelmayer T. Influence of the spatial and temporal interaction
between diesel pilot and directly injected natural gas jet on ignition and
combustion characteristics. J Eng Gas Turb Power 2018;140(10):102811.
[17] Fink G, Jud M, Sattelmayer T. Fundamental study of diesel-piloted natural gas
direct injection under different operating conditions. J Eng Gas Turb Power
2019;141(9):091006.
[18] Rorimpandey P, Yip HL, Srna A, Zhai G, Wehrfritz A, Kook S, Hawkes ER,
Chan QN. Hydrogen-diesel dual-fuel direct-injection (H2DDI) combustion under
compression-ignition engine conditions. Int J Hydrog Energy 2023;48(2):766–83.
[19] Idicheria CA, Pickett LM. Ignition, soot formation, and end-of-combustion
transients in diesel combustion under high-EGR conditions. Int J Engine Res
2011;12(4):376–92.
[20] Rorimpandey P, Zhai G, Kook S, Hawkes ER, Chan QN. Effects of energy-share
and ambient oxygen concentration on hydrogen-diesel dual-fuel direct-injection
(H2DDI) combustion in compression-ignition conditions. Int J Hydrog Energy
2024;49:1346–61.
[21] Wittek K, Cogo V, Prante G. Development of a pneumatic actuated low-pressure
direct injection gas injector for hydrogen-fueled internal combustion engines. Int
J Hydrog Energy 2023;48(27):10215–34.
[22] Srna A. Is there a place for H 2 internal combustion engines? Report, U.S.
Department of Energy - Hydrogen and Fuel Cell Technologies Office; 2022.
[23] Hernández JJ, Salvador JB, Cova-Bonillo A. Autoignition of diesel-like fuels
under dual operation with H 2. Adv Mech Eng 2019;11(6):1687814019856781.
[24] Gu S. Direct numerical simulation of hydrogen-diesel dual-fuel combustion (Ph.D.
thesis), Sydney, NSW: University of New South Wales; 2023.
[25] Yan J, Wang P, Yan T, Ao C, Zhang L, Lei L. A theoretical calculation and kinetic
modeling analysis of H-abstraction from 1-octene for subsequent isomerization
and beta-dissociation. Int J Hydrog Energy 2024;55:1028–36.
[26] Yang X, Vinhaes VB, Turcios M, McTaggart-Cowan G, Huang J, Naber J,
Shahbakhti M, Schmidt H, Atkinson W. Process for study of micro-pilot diesel-
NG dual fuel combustion in a constant volume combustion vessel utilizing the
premixed pre-burn procedure. SAE Paper, 2019-01-1160, 2019.
[27] Wallner T, Ciatti S, Bihari B. Investigation of injection parameters in a hydrogen
DI engine using an endoscopic access to the combustion chamber. In: SAE world
congress & exhibition. SAE Int; 2007.
[28] Liu X, Srna A, Yip HL, Kook S, Chan QN, Hawkes ER. Performance and
emissions of hydrogen-diesel dual direct injection (H2DDI) in a single-cylinder
compression-ignition engine. Int J Hydrog Energy 2020;46(1):1302–14.
[29] Verhelst S, Maesschalck P, Rombaut N, Sierens R. Increasing the power output
of hydrogen internal combustion engines by means of supercharging and ex-
haust gas recirculation. Int J Hydrog Energy 2009;34(10):4406–12, 2nd World
Hydrogen Technologies Convention.
[30] Saravanan N, Nagarajan G, Kalaiselvan K, Dhanasekaran C. An experimental
investigation on hydrogen as a dual fuel for diesel engine system with exhaust
gas recirculation technique. Renew Energy 2008;33(3):422–7.
[31] Naber J, Siebers D. Hydrogen combustion under diesel engine conditions. Int J
Hydrog Energy 1998;23(5):363–71.
[32] Yip HL, Srna A, Zhai G, Wehrfritz A, Kook S, Hawkes ER, Chan QN. Laser-
induced plasma-ignited hydrogen jet combustion in engine-relevant conditions.
Int J Hydrog Energy 2023;48(4):1568–81.
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
[36] Han D, Duan Y, Zhai J. Autoignition comparison of n-dodecane/benzene and
n-dodecane/toluene blends in a constant volume combustion chamber. Energy
Fuels 2019;33(6):5647–54.
[37] Han D, Zhai J, Huang Z. Autoignition of n-hexane, cyclohexane, and
methylcyclohexane in a constant volume combustion chamber. Energy Fuels
2019;33(4):3576–83.
[38] Yip HL, Srna A, Liu X, Kook S, Hawkes ER, Chan QN. Visualiza-
tion of hydrogen jet evolution and combustion under simulated direct-
injection compression-ignition engine conditions. Int J Hydrog Energy
2020;45(56):32562–78.
[39] Dec JE. A conceptual model of dl diesel combustion based on laser-sheet imaging.
SAE Trans 1997;106:1319–48.
[40] Heywood J. Internal combustion engine fundamentals 2E. McGraw-Hill
Education; 2018.
[41] Pickett LM, Kook S, Williams TC. Visualization of diesel spray penetration,
cool-flame, ignition, high-temperature combustion, and soot formation using
high-speed imaging. SAE Int J Engines 2009;2(1):439–59.
[42] Pickett LM, Kook S, Persson H, Andersson Ö. Diesel fuel jet lift-off stabi-
lization in the presence of laser-induced plasma ignition. Proc Combust Inst
2009;32(2):2793–800.
[43] Musculus MP, Miles PC, Pickett LM. Conceptual models for partially
premixed low-temperature diesel combustion. Prog Energy Combust Sci
2013;39(2):246–83.
[44] Skeen S, Manin J, Pickett LM. Visualization of ignition processes in high-
pressure sprays with multiple injections of n-dodecane. SAE Int J Engines
2015;8(2):696–715.
[45] Subramanian G, Cruz APD, Bounaceur R, Vervisch L. Chemical impact of CO and
H2 addition on the auto-ignition delay of homegeneous n-heptane/air mixtures.
Combust Sci Technol 2007;179(9):1937–62.
[46] Comandini A, Chaumeix N, Maclean J, Ciccarelli G. Combustion properties of
n-heptane/hydrogen mixtures. Int J Hydrog Energy 2019;44(3):2039–52.
[47] Yip HL, Srna A, Wehrfritz A, Kook S, Hawkes ER, Chan QN. A parametric study
of autoigniting hydrogen jets under compression-ignition engine conditions. Int
J Hydrog Energy 2022;47(49):21307–22.
[48] Reitz R, Hessel R, Musculus M. A visual investigation of CFD-predicted in-
cylinder mechanisms that control first- and second-stage ignition in diesel jets.
SAE paper, 2019-01-0543, 2019.
[49] Kammermann T, Koch J, Wright YM, Soltic P, Boulouchos K. Generation of tur-
bulence in a RCEM towards engine relevant conditions for premixed combustion
based on CFD and PIV investigations. SAE Int J Engines 2017;10(4):2176–90.
[50] Gerke U, Steurs K, Rebecchi P, Boulouchos K. Derivation of burning veloc-
ities of premixed hydrogen/air flames at engine-relevant conditions using a
single-cylinder compression machine with optical access. Int J Hydrog Energy
2010;35(6):2566–77.
[51] Li G. Optimization study of pilot-ignited natural gas direct-injection in diesel
engines. SAE Trans 1999;108:1739–48.
[52] Zhai G, Xing S, Yuen AC, Medwell PR, Kook S, Yeoh GH, Chan QN. Laser
ignition of iso-octane and n-heptane jets under compression-ignition conditions.
Fuel 2021;122555.
[53] Pastor J, García-Oliver J, López J, Vera-Tudela W. An experimental study of the
effects of fuel properties on reactive spray evolution using primary reference
fuels. Fuel 2016;163:260–70.
[54] Ming C, Rizwanul Fattah I, Chan QN, Pham PX, Medwell PR, Kook S,
Yeoh GH, Hawkes ER, Masri AR. Combustion characterization of waste cooking
oil and canola oil based biodiesels under simulated engine conditions. Fuel
2018;224:167–77.
[55] Ming C, Rizwanul Fattah IM, Chan QN, Medwell PR, Kook S, Hawkes ER,
Yeoh GH. Combustion measurements of waste cooking oil biodiesel. In: 11th
Asia-Pacific conference on combustion. ASPACC 2017, Vol. 2017-December,
2017.
[56] Rajasekar E, Selvi S. Review of combustion characteristics of CI engines fueled
with biodiesel. Renew Sustain Energy Rev 2014;35:390–9.
[57] Niermann M, Timmerberg S, Drünert S, Kaltschmitt M. Liquid organic hydrogen
carriers and alternatives for international transport of renewable hydrogen.
Renew Sustain Energy Rev 2021;135:110171.
[58] Wang F, Swinbourn R, Li C. Shipping Australian sunshine: Liquid renewable
green fuel export. Int J Hydrog Energy 2023;48(39):14763–84.
[59] Bilousov I, Bulgakov M, Savchuk V. Four-stroke marine engines. In: Modern
marine internal combustion engines: a technical and historical overview. Cham:
Springer; 2020, p. 1–165.

<!-- PDF_PAGE: 20 -->

International Journal of Hydrogen Energy 67 (2024) 172–191
191
P. Rorimpandey et al.
[60] Ramsay C, Dinesh KR. Numerical modelling of a heavy-duty diesel-hydrogen
dual-fuel engine with late high pressure hydrogen direct injection and diesel
pilot. Int J Hydrog Energy 2024;49:674–96.
[61] Dinesh KR, Ramsay C. High hydrogen content diesel-hydrogen dual-fuel com-
bustion with direct injection of hydrogen main fuel and diesel pilot fuel. In:
Powertrain systems for a sustainable future. CRC Press; 2023, p. 353–62.
[62] Ramsay C, Dinesh KR. High pressure direct injection of gaseous fuels using
a discrete phase methodology for engine simulations. Int J Hydrog Energy
2022;47(3):2017–39.
[63] Wang Y, Evans A, Srna A, Wehrfritz A, Hawkes E, Liu X, Kook S, Chan QN. A
numerical investigation of mixture formation and combustion characteristics of
a hydrogen-diesel dual direct injection engine. In: SAE wCX digital summit. SAE
Int; 2021.
