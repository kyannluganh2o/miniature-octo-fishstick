<!-- PDF_PAGE: 1 -->

Contents lists available at ScienceDirect
Fuel
journal homepage: www.elsevier.com/locate/fuel
Full Length Article
Visualization research on hydrogen jet characteristics of an outward-
opening injector for direct injection hydrogen engines
Xi Wang a, Bai-gang Sun a, Qing-he Luo a,⁎
, Ling-zhi Bao a, Jian-ye Su b, Jie Liu c, Xiang-chao Li d
a School of Mechanical Engineering, Beijing Institute of Technology, Zhongguancun South Street 5, 100081 Beijing, China
b United Automotive Electronic Systems Co., Ltd., No. 555 Rong Qiao Road, 201206 Shanghai, China
c Pan Asia Technical Automotive Center, No. 2199 Jufeng Road, 201201 Shanghai, China
d SAIC Motor Technical Center, No. 201 AnYan Rd, 201804 Shanghai, China
ARTICLE INFO
Keywords:
Outward-opening injector
Hydrogen direct-injection
Hydrogen jet characteristics
Penetration constant
ABSTRACT
The hydrogen jet characteristics have eﬀ ect on the performance of direction injector (DI) hydrogen engines
because they can in ﬂuence the process of mixture formation and heat release. In this study, the hydrogen jet
characteristics of an outward-opening injector were studied with high-speed schlieren imaging in a constant
volume chamber at di ﬀerent injection and ambient pressure ratios (PRs), which ranged from 10 to 140. Results
show that the hydrogen jet in the near- ﬁeld is a conical structure, while the jet structure develops into a spherical
vortex in the far- ﬁeld. The jet axial penetration, radial penetration, and volume increase with the increasing of
the PR. The jet spread angle is not sensitive to the PR except for the low PRs. The entrainment rate decreases
with the increasing of the PR. The normalization analysis of jet penetration shows that the hydrogen jets have a
good self-similarity under all PRs. A non-dimensional scaling correlation of axial penetration is proposed for this
kind of hydrogen jets. In the scaling correlation, the exponents of the non-dimensional penetration and time term
are 0.18 and 0.83, while the penetration constant is 13.18. The discovery of the above jet characteristics can
predict the free jet shape under any PR in the range of 10 to140. These results can also promote the application
of DI hydrogen engines.
1. Introduction
The growing consumption of foil fuels has accelerated the energy
crisis [1]. It is necessary to implement alternative energy sources. Many
researchers focus on the di ﬀerent renewable energy such as biofuel,
which can replace part of diesel because of its characteristics [2,3]. For
example, Nanthagopal et al [4] reported the performance at di ﬀerent
proportion of biofuel with diesel in the compression engines. The re-
sults showed that the brake thermal e ﬃ ciency drop 5.3% and the
emission of smoke also increase. Thus, to decrease the emission and
increase of performance of engines, hydrogen is a prominent selection
for the renewable and sustainable energy carrier in the future [5]. The
characteristics of high octane value, low ignition energy, and fast
combustion speed makes an ideal alternative fuel for spark ignition
internal combustion engines [6].
Port fuel injection (PFI) hydrogen internal combustion engine has
been comprehensively studied in the past. The part-load e ﬃ ciency of
the PFI hydrogen engine can be relatively high because of the long
mixing time of the hydrogen-air mixture [7]. But hydrogen occupies the
intake volume, resulting in a low power output [8]. In addition, PFI
hydrogen engines have the disadvantages such as knock [9] and
backﬁre [10]. The limitations related to PFI hydrogen engines pro-
moted the research of direct injection (DI) hydrogen engines [11].D I
can increase the engine power density, eliminate the possibility of
backﬁre and reduce the tendency for autoignition [12]. For example,
Takagi et al. [13] developed a test engine can achieve an IMEP of
1.64 MPa (150 Nm@1000 rpm) and more than 50% of ITE, which can
be used to a stationary power generator. However, the way of DI makes
the combustion quality [14] and NOx emissions [15] largely dependent
on the quality of the mixing of hydrogen and air in the cylinder. For DI
gaseous fuel engines, the mixing characteristics mainly rely on the gas
jet characteristics. Huang et al. [16,17] studied the combustion char-
acteristics of a DI engine with hydrogen-natural gas blends. The results
show that the turbulent combustion of gaseous fuel is greatly a ﬀected
by the turbulence intensity induced by gas jet of hydrogen-natural gas
blends. Abdul Rahman et al. [18] used spark-induced breakdown
spectroscopy to measure the local concentration of transient hydrogen
jet. They proposed that the increase of ambient pressure would a ﬀect
https://doi.org/10.1016/j.fuel.2020.118710
Received 27 February 2020; Received in revised form 6 July 2020; Accepted 11 July 2020
⁎ Corresponding author.
E-mail address: 7520180030@bit.edu.cn (Q.-h. Luo).
Fuel 280 (2020) 118710
Available online 20 July 2020
0016-2361/ © 2020 Elsevier Ltd. All rights reserved.
T

<!-- PDF_PAGE: 2 -->

the structure of the hydrogen jet, slow the spray and reduce the pene-
tration, which will change the equivalent ratio of the spark position.
Takagi et al. [19] achieved high thermal e ﬃ ciency and near-zero
emissions in a DI hydrogen engine by optimizing the injection timing,
jet plume location, and jet geometry. They reported a new combustion
process using in the DI hydrogen engines, which is the Plume Ignition
Combustion Concept (PCC). The BTE can reach to 49% and the NOx
emission can be near-zero at di ﬀerent conditions [20].
In terms of application of DI gaseous fuel engines, multi-hole plain-
oriﬁce injectors are commonly used to inject gaseous fuel into the cy-
linder. Due to the high-pressure injection, the ratio of the injection
pressure to the ambient pressure (PR) is generally greater than the
critical pressure ratio. Petersen et al. [21] used the Z-type and double-
pass schlieren system to visualize the jet structure and the interaction
between the jets of the transient high-pressure hydrogen jet with a
three-hole injector. Erfan et al. [22] investigated the compressed nat-
ural-gas (CNG) jet from a multi-hole high-pressure DI injector by
schlieren photography. The results show that reducing the ambient
pressure is more e ﬀective than rising the injection pressure for the in-
crease in axial penetration. To facilitate the analysis, many researchers
used single round nozzles to study the high-pressure gas jet character-
istics. Deng et al. [23] studied the jet characteristics of hydrogen in an
argon environment. The capability of the gas jet to entrain argon in-
creases with the increasing of the injection time, injection pressure and
ambient pressure. Ouellette et al. [24,25] reviewed the transient tur-
bulent gas jet theory of the single round nozzles. The quasi-steady jet
theory assumes that the gas jet from single round nozzles is headed by
spherical vortex and the upstream part is quasi-steady state. The gas jet
has the characteristic of self-similarity, which means that the jet radial
penetration and axial penetration is proportional. Rogers et al. [26]
experimentally veri ﬁed the self-similarity of gas jets at PRs below 400.
The results show that after a certain development transition period, the
ratio of the radial penetration to axial penetration keeps constant, and
the ratio is 0.25 ± 0.05 at all PRs. Under the premise that the gas jet
achieves self-similarity, Ouellette and Hill [25] developed a scaling
relationship of the axial penetration, as shown in Eq. (1).
⎜⎟= ⎛
⎝
⎞
⎠
y M
ρ tΓ
̇
n
c
0.25
0.5
(1)
where, y (m) is the axial penetration, Γ is the penetration constant, ρc
(kg/m3) is the density of the ambient gas, and t (s) is the time after start
of injection. Ṁn (kg·m/s2) is the nozzle momentum injection rate which
can be calculated by Eq. (2).
=M mU̇ ̇nf n (2)
where,ṁf (kg/s) is the injector delivery rate, which is the rate of fuel
injection when the injector is held open. Un (m/s) is the chocked nozzle
velocity. The penetration constant Γ determined by Ouellette and Hill
[25] through the experiment was 3.0 ± 0.1. These researches pro-
moted the development of gas engines.
However, almost all injectors used in past studies of gas jets were
the inward-opening type. In practical applications, it was demonstrated
that the low mass ﬂow rates of such injectors limit the power output of
the gaseous fuel engines. Another type of the injector is the outward-
opening injector which has deﬁ nite advantages in the mass ﬂow rate
due to the large cross-section of its nozzle [27]. It could become a better
choice for gaseous fuel engines. In published studies, there have been
few reports on ﬂow characteristics of gas jets from the outward-opening
injector. Sankesh et al. [28] used high-speed schlieren imaging to study
the characteristics of CNG jet from an outward-opening injector at an
injection pressure of 20 to 160 bar. The results indicate that the scaling
correlation of penetration for gas jets emitted by outward-opening in-
jectors is same as the form as that of Eq. (1) for the gas jets of round
nozzles. And after an initial development phase of 0.5 ms, the pene-
tration constant Γ for conical jets is 1.15 ± 0.05. Zhao et al. [29]
studied the e ﬀect of ambient pressure on CNG jet characteristics of an
outward-opening gas injector. They ﬁnd that increasing ambient pres-
sure inhibits the increase in jet spread angle and jet penetration, which
leads to the decrease of jet entrainment rate. Table 1 lists the studies of
CNG jets with outward-opening nozzles.
The above work was performed on CNG jets, and few works con-
cerned about hydrogen jets. The demand for the high discharge in-
jectors in hydrogen engines is more urgent than that in CNG engines
since the low density of the hydrogen. The characteristics of the hy-
drogen jet directly a ﬀect the formation of the mixture in the DI hy-
drogen engine. Moreover, some key researches of the injectors were
used in the CI hydrogen engines, which were remolded from diesel jets.
Thus, to explore the suitable hydrogen jet for the hydrogen engines
modiﬁed by gasoline engines, this paper studied the hydrogen jet
characteristics of the outward-opening injector, which is essential to DI
hydrogen engines. In this study, the hydrogen jet characteristics of an
outward-opening injector was studied with high-speed schlieren ima-
ging in a constant volume chamber (CVC) at di ﬀerent PRs. The ex-
periment process and key equipment showed in the Section 2.1 and the
way of dealing with data in Section 2.2 . Based on the experiment data,
the structure of the hydrogen jets was analyzed in Section 3.1 , and the
variation rules of jet penetration, spread angle and ambient air mixing
were evaluated in Section 3.2 . A normalization study of jet axial pe-
netration was also performed in Section 3.3 .
2. Experiments
2.1. Experimental setup
In this study, the schlieren method was utilized to capture the image
of hydrogen jets from an outward-opening injector. The basic principle
of the schlieren method is that the refractive index gradient of light in
the measured ﬂow ﬁeld is proportional to the ﬂow ﬁeld density. Thus,
the density gradient in the ﬂow ﬁeld
is transformed into a change in
relative light intensity on the plane. The high-pressure gas jet will lead a
sharp density gradient in the ﬂow ﬁeld. The application of the schlieren
method can change the gas ﬂow that is invisible to the naked eye into
an observable and resolvable image. Combining high-speed photo-
graphy technology, which can record the development of the jet. The
experimental setup shown in Fig. 1 utilizes a typical Z-type schlieren
Nomenclature
PFI port fuel injection
DI direct injection
PR Ratio of injection pressure to ambient pressure
CNG compressed natural gas
CVC constant volume chamber
Γ penetration constant
y axial penetration
x radial penetration
θ spread angle
∅ entrainment rate
Table 1
Studies of CNG jets with outward-opening nozzles.
Penetration constant ( Г)P R P i (bar) P 0 (bar)
Sankesh et al. 1.15 20 –160 20 –160 1
Zhao et al. near- ﬁeld 1.65 far- ﬁeld 6.51 @
P0 = 1 bar near- ﬁeld 2.48 far- ﬁeld
4.20–6.49 @ P 0 greater than 1 bar
2–18 10 –18 1 –5
X. Wang, et al. Fuel 280 (2020) 118710
2

<!-- PDF_PAGE: 3 -->

setup, with a diameter of the parallel beam of 100 mm. The model of
the high-speed camera is Phantom V7.3. All the experiments in this
study are performed at a resolution of 512 × 384 pixels, a shooting
frequency of 15,037 fps, and an exposure time of 20 μs. This setting can
achieve high spatiotemporal resolution (0.21 mm/pixel, 66.5 μs in-
terval time between adjacent images). A cube-shaped CVC with an in-
ternal volume of 1.6 L is used to make ambient pressure adjustable, and
the permissible pressure is 1 bar to 5 bar. The observation window of
the CVC is made of quartz optical glass, with a size of 127 × 107 mm
and a thickness of 20 mm. The background gas in the experiment is
nitrogen, and the ambient temperature of the test is 20 °C.
An outward-opening injector with a 90° conical annular nozzle was
used to inject hydrogen. The cross-section of the nozzle is shown in
Fig. 2. The lift of the nozzle needle is approximately 30 µm, and the
angle at the nozzle seat is about 90°. A piezoelectric drive circuit
module is self-made to control this injector, with the driving voltage of
146 V, and the maximum current of 8 A. Woodward's rapid prototype
controller is used to generate two 5 V TTL signals, which trigger high-
speed camera and injector simultaneously. The outward-opening in-
jector is installed vertically in the center of the top of the CVC. The
distance of the nozzle protruding from the inner surface of the CVC is
set as 6 mm to ensure that the free jet is not a ﬀected by the Coanda
eﬀect [26].
According to the Eq. (2), the mass ﬂow characteristics of the injector
is a signi ﬁcant parameter for analyzing the gas jets. Before the schlieren
test, the mass ﬂow rate of the injector was measured by the CVC test
platform. The measurement method was repeated injection of hydrogen
into the CVC with a ﬁxed injection duration, and then use the gas state
equation to calculate the average mass for each injection from the
pressure increase in CVC. The mass ﬂow rate with di ﬀerent injection
pressures (40 –140 bar) and various injection duration (1 –5 ms) was
measured. The initial background pressure was 1 bar, and the PR during
the test was much larger than the critical pressure ratio, so that the ﬂow
was chocked at the nozzle. According to the research of Erfan et al.
[30], the mass ﬂow rate of an injector was not a ﬀected by the pressure
of the chamber under critical conditions. Thus, the mass of each in-
jection is the same under the same injection conditions. Fig. 3 shows the
ﬂow characteristics of the injector. The average single injection mass of
the injector increases linearly with the increase of the injection duration
from Fig. 3 (a). From Fig. 3 (b), the injection delivery rate of hydrogen
also increases linearly with the increase of the injection pressure.
2.2. Image and data processing
The hydrogen jet image sequences were obtained through high-
speed schlieren imaging. The quantitative parameters for evaluating the
characteristics of the hydrogen jet can be obtained by post-processing
the jet image sequences, including the jet axial penetration, jet radial
penetration, jet spread angle, jet velocity, jet volume, etc. Before
quantitative parameter extraction, the projected contour of the jet on
the observation plane needs to be obtained by processing the original
jet image sequences. A series of image morphology MATLAB functions
are used to obtain images of the jet contours, as shown in Fig. 4. First,
remove the environmental background to highlight the jet. The back-
ground image with no injection is subtracted from the images in jet
sequences, as shown in Fig. 4(b). The ﬁltering function is used to
eliminate excess noise in the background, as shown in Fig. 4(c).
Then,
the jet is reconstructed by the dilation and ﬁlling functions to obtain the
jet contour, as shown in Fig. 4(d) –(f).
Unlike the gas jets from the inward-opening injector with the plain-
oriﬁce nozzle, the structure of the outward-opening injector makes the
gas jets have a strong di ﬀusivity in the radial direction. Sankesh et al.
[28] deﬁned the radial penetration, axial penetration and spread angle
of the CNG jet characteristics from an outward-opening injector. A si-
milar approach is used to deﬁ ne the jet parameters in this research. As
shown in Fig. 5, the injector axis divides the image into left and right
halves. For each half, the longest distance between the jet contour and
the nozzle in the axial direction is recorded as y1 and y2, and the
longest distance between the jet contour and the central axis in the
radial direction is recorded as x1 and x2. Then the axial penetration y
can be de ﬁned as:
y = (y1 + y2)/2 (3)
Fig. 1. Schematic of the experimental setup.
Fig. 2. Sectional view of the injector nozzle.
X. Wang, et al. Fuel 280 (2020) 118710
3

<!-- PDF_PAGE: 4 -->

The axial penetration × can be de ﬁned as:
x = x1 + x2 (4)
The jet spread angle is deﬁ ned based on the centroid of the half jet
contour. Speci ﬁcally, the spread angle θ is the angle formed between
the centroid of each half and the assumed jet apex. As shown in Fig. 5,
the centroids of the two halves are C1 and C2, respectively. The position
of the assumed jet apex is on the injector axis and is horizontal to the
injector outlet.
The jet velocities in the axial and radial directions can be obtained
by deriving the corresponding penetration. The jet volume is de ﬁned as
the average value of the volume formed by the left half and right half of
the jet rotating around the axis of the injector. The above parameters
were all calculated by a custom MATLAB program. The error of the jet
parameters mainly comes from the injection and ambient pressure
gauges, the jet-to-jet variation and the image processing. The accuracy
of the pressure gauges is ± 0.2% of full-scale output. The experiment
was repeated 10 times under each PR to ensure the accuracy of the data.
The image processing error of penetration is less than 0.4 mm, which is
within the standard deviation of repeated tests.
Fig. 3. Flow characteristics of the hydrogen injector: (a) Single injection mass changes with injection duration, (b) Injection delivery rate changes with injection
pressure.
Fig. 4. Image processing: (a) Original image; (b) Background removal; (c) Filtering; (d) Dilation; (e) Filling; (f) Outlined original.
X. Wang, et al. Fuel 280 (2020) 118710
4

<!-- PDF_PAGE: 5 -->

2.3. Experimental conditions
In this study, PR is the experimental variable, and the experimental
conditions are shown in Table 2. Restricted by the allowable pressure of
the CVC and the common working pressure of the hydrogen injector,
neither Pi nor P0 in the experimental conditions are ﬁxed. But we try to
make the P i or P 0 of the adjacent test points equal, except PR60 and
PR80, to ensure the comparability of the adjacent test points. Assuming
that the jet parameters are only a ﬀected by the PR, di ﬀerent combi-
nations of P i and P0 will not signi ﬁcantly aﬀect the jet parameters, then
all experimental points in Table 2 are comparable. We conducted ex-
periments to verify this hypothesis, as shown in Fig. 6. The four ex-
perimental points in Fig. 6 have diﬀerent combinations of P i and P0. The
PR of test point 1 and test point 2 are both 20, and the PR of test point 3
and test point 4 are both 40. The jet parameter curves of test point 1
and test point 2 almost overlap each other, and so do test point 3 and
test point 4. The test results verify that under a ﬁxed PR, diﬀerent P
i and
P0 combinations will not signi ﬁcantly a ﬀect the jet parameters.
3. Results and discussion
Fig. 7 shows the schlieren image sequence of hydrogen jet under
diﬀerent PRs. The hydrogen jets from the outward-opening injector has
a unique structure. The size of the hydrogen jet in the axial and radial
directions increase with the increasing of the PR. In order to determine
the detailed mechanism of the hydrogen jet, this study discusses the
hydrogen jet characteristics of an outward-opening injector from three
aspects: jet structure, jet parameters, and penetration normalization.
3.1. Hydrogen jet structure
Fig. 7 shows an interesting ﬂow pattern produced by a hydrogen jet
from a 90° conical annular nozzle. Hydrogen jets show di ﬀerent
morphologies in the near- ﬁeld and far-ﬁ eld. The jet structure is conical
in the near ﬁeld of the nozzle, while the structure of the jet head is a
spherical vortex when the jet develops into the far- ﬁeld. The hydrogen
jet ﬂows out through the annular nozzle hole, while the angle between
the valve seat and the injector axis is 45°, which leads that the jet is
guided by the valve seat to form a cone structure in the near- ﬁeld. In the
early stage of jet development, the conical structure is enveloped with
ambient gas, which is called a hollow conical structure. As the jet
continues to develop, the ambient gas inside the cone is drawn into the
jet. The velocity component of the jet in the radial direction drops ra-
pidly due to the lower momentum of the hydrogen jet. These two
reasons cause the jet to shrink towards the axis as it continues to
develop. The continuous friction of the ambient gas to the outside of the
jet will cause the jet to generate a velocity gradient outward along the
axis. The jet velocity at the axis is continuously increasing, which
eventually leads to the formation of a spherical vortex head. The jet
appears as a spherical eddy current guiding structure at this time.
Comparing the jet structures under di ﬀerent PRs, it is found that as the
PR increases, the dimensions of the near- ﬁeld cone and far-ﬁ eld sphe-
rical vortices increase in all directions. However, PR has no signi ﬁcant
eﬀect on the occurrence time of far-ﬁ eld spherical eddy currents except
PR10. At 0.665 ms, it can be observed that the jet spherical vortex head
has clearly separated from the cone structure under PR10. At this time,
the structure of the spherical vortex head has not been completely
generated under other PRs, and the separation phenomenon can not be
observed until 0.9975 ms. Under the same PR, the size of the near- ﬁeld
cone structure does not change signi ﬁcantly with the development of
the jet. By discussing the structure of the hydrogen jet, a reasonable
explanation can be made for the variation rule of the characteristics of
the hydrogen jet mentioned below.
3.2. Hydrogen jet parameters
3.2.1. Jet penetration
The average penetrations in the radial and axial directions are
plotted in Figs. 8 and 9. The standard deviations of the 10 repeated test
values are marked in the ﬁgures with error bars. It can be seen that both
radial penetration and axial penetration increase with the increasing of
the PR. This is because with the increase of the PR, the injection
pressure increases or the ambient pressure decreases so that the jet has
greater mass ﬂow rate or less ambient resistance, both of which will
increase the propagation range of the jet. The di ﬀerence in both pe-
netrations
between adjacent PRs decrease with the increasing of the PR,
and the tendency is exaggerated for radial penetration. The radial pe-
netration increases rapidly at the beginning and then slowly increases
with time. Because the radial penetration re ﬂects the size of the conical
jet in the early stage of the jet, and after the spherical vortex structure
dominates, the radial penetration is a characterization of the radial
dimension of the vortex. The axial penetration increases linearly with
time after 0.266 ms except PR 10 and 20. The lower PR value makes the
jet decelerate earlier due to the e ﬀect of the ambient gas, so that the
slopes of the axial penetration curves under PR 10 and 20 gradually
decrease with time. The jet spherical vortex head of PR10 appears early
than that of PR20, which results in the axial penetration of PR10 equal
to PR20 at about 0.9 ms. Comparing Figs. 8 and 9 it can be seen that the
radial penetration under all PRs is greater than the axial penetration in
the jet initial stage, and the axial penetration distance will gradually
exceed the radial penetration distance with the development of the jet.
The di ﬀerence between the penetrations becomes larger over time,
which is determined by the transition of the jet structure from the near-
ﬁeld to the far-ﬁeld. In addition, the radial penetration of PR20 is larger
than that of PR 140 at a later stage. This may be because the constant
volume chamber is relatively small, and the jet under PR 140 is a ﬀected
by the re ﬂected wave from the wall.
Fig. 5. Schematic of jet penetration and spread angle.
Table 2
PR conditions for experimental.
PR Pi (bar) P0 (bar)
10 40 4
20 80 4
30 120 4
40 120 3
60 120 2
80 80 1
100 100 1
120 120 1
140 140 1
X. Wang, et al.
Fuel 280 (2020) 118710
5

<!-- PDF_PAGE: 6 -->

The radial and axial velocities of the hydrogen jet are plotted in
Figs. 10 and 11. The radial velocity and the axial velocity are derived
from the corresponding average penetration data. It should be pointed
out that at the shooting frequency of this experiment, there was only
one or two sampling points before the peak velocity appeared. There-
fore, the value of the peak velocity has a large error and cannot accu-
rately re ﬂect the relationship between the peak velocity and PR. In the
initial stage, the jet has extremely fast peak velocity in the radial di-
rection, and the peak appears at about 0.1 ms, while the peak velocity
of the jet in the axial direction appears at about 0.2 ms, indicating that
the nozzle is fully opened at this time. However, the radial velocity at
0.2 ms has decreased rapidly. The radial velocity of PR10 has been
reduced to 15 m/s, which indicates that the radial dimension of the
cone structure has reached the maximum, and the spherical vortex head
has begun to form. As the PR increases, it takes longer time to reduce
the radial velocity below 50 m/s. This phenomenon indicates that the
higher the PR, the larger the size of the near- ﬁeld cone structure. After
about 0.5 ms, the jet is transformed into the spherical vortex guide. At
this time, the jet state is relatively stable, and the gas jet will slow down
in the radial and axial directions with the interaction with the ambient.
3.2.2. Jet spread angle
One of the key parameters for evaluating the distribution of gas jets
in space is the spread angle. The average jet spread angle of the hy-
drogen jet is shown in Figs. 12 and 13. The initial average jet spread
angle is between 70 and 80°, which is slightly smaller than the angle of
the nozzle valve seat. From Fig. 12, the jet spread angle gradually de-
creases with time and will stabilize at about 20°, which is consistent
with the change of the jet structure. The curves of the jet spread angle
with time under di ﬀerent PRs other than PR10 almost coincide, and the
ﬂuctuation range is within 3% of the average. The jet spread angle is
not sensitive to PR in the PR range of 20 to 140, which indicates that
the hydrogen jets have good structural similarity in this PR rang at the
same injection time. The jet spread angle curve of PR10 basically co-
incides with the curves of other PRs before 0.665 ms, and starts to
deviate downward after 0.665 ms. Because the spherical vortex head of
the jet under PR10 appears earlier than the jets of other PRs, this ac-
celerates the increase of its axial penetration and results in a smaller
spread angle. In the later stage of the jet under PR10, the axial velocity
of the jet decreases rapidly under the resistance of ambient gas, which
slows down the rate of decrease of the spread angle, so the spread angle
of PR10 gradually approaches the spread angles of other PRs. Fig. 13
shows the average jet spread angle with the axial penetration for PRs 10
to 140. The jet spread angle increases with the increasing of the PR in
the PR range of 20 to 60. When the PR reaches 60 or more, the spread
angle hardly increases and collapses into a curve. The variation of the
spread angle with the axial penetration also appears to be insensitive to
PR for PRs 60 to 140. The above characteristics of the jet spread angle
can be used in DI hydrogen engines to optimize the formation of the
fuel-air mixtures. For one thing, the injection pressure of DI hydrogen
engines is recommended to be above 60 bar, which helps the formation
of homogeneous mixtures to reduce cycle-by-cycle variation. For an-
other, multiple injection techniques can be used to achieve a larger
spread angle for each hydrogen injection, which facilitates the forma-
tion of homogeneous mixtures. Because in the compression stroke, al-
though the upward movement of the piston increases the pressure in the
cylinder, the spread angle of the hydrogen jet is not a ﬀected.
3.2.3. Jet volume
Fig. 14 shows the time course of the jet volume. The volume of the
jet increase with the increasing of the PR, which is caused by the in-
crease of the ratio of the hydrogen mass ﬂow rate to the ambient
pressure. As the pressure ratio increases, the amount of jet volume in-
crease decreases. The changes of the jet volume with axial penetration
are plotted in Fig. 15. The jet volume almost collapsed into a line under
the PR range of 100 to140, which indicates that after PR100, the ability
of the hydrogen jet to entrain surrounding gas decreases with the in-
creasing of the PR.
During the development of the gas jet, the ambient gas is entrained
into the jet body. To evaluate the entrainment ability, the entrainment
rate ∅ is proposed to indicate the degree of mixing in gas jets, which is
deﬁned in Eq. (5).
∅= −VV
V
jet 0
0 (5)
where, V0 refers to the volume occupied by the total mass of the in-
jected gas after the start of injection under the pressure and tempera-
ture of the ambient. Vjet is the jet volume. The entrainment ratio of the
hydrogen jet is shown in Fig. 16 . Due to the unstable mass ﬂow of the
injector in the initial stage, only the entrainment rate after 0.5 ms is
displayed. The entrainment rate decreases signi ﬁcantly with the in-
creasing of the PR, and the di ﬀerence between adjacent PRs also de-
creases. With the exception of PR10, the entrainment rate increases
with time. The entrainment rate at PR10 ﬁrst decreases and then
Fig. 6. Jet parameter of di ﬀerent P i and P 0 combinations: (a) Radial penetra-
tion; (b) Axial penetration.
X. Wang, et al. Fuel 280 (2020) 118710
6

<!-- PDF_PAGE: 7 -->

increases. The reason is that the lower jet ﬂow volume causes more
ambient gas near the nozzle to be enclosed in the jet during the initial
development stage. At the same time, the ability of the jet to entrain
surrounding gas is weak, so that the volume of the gas inside the jet is
almost unchanged. The mass of the jet continues to increase over time,
resulting in a decrease in entrainment. The volume ratio of hydrogen to
air under the stoichiometric ratio is 2.38, then the entrainment ratio of
the hydrogen jet at the theoretical air-fuel ratio is 1.38. Although the
entrainment capability is weak at high PR, the hydrogen jet can still
entrain enough air. Hydrogen jets above PR 100 have a high equiva-
lence ratio, which is conducive to the realization of strati ﬁed
combustion of an injection-guided DI hydrogen engine.
3.3. Normalization of penetration
3.3.1. Self-similarity
It is found that the far- ﬁeld structure of the hydrogen jet from an
outward-opening injector is similar to that of an inward-opening in-
jector with a circular single-hole nozzle by comparing the jet structure.
Thus, this study used the same self-similarity parameter x/y as the
single-hole nozzle jets. The change of the self-similar parameters of the
hydrogen jet under di ﬀerent PR is shown in Fig. 17 . The self-similarity
Fig. 7. Sequence of hydrogen jets for PRs 10 to 140.
X. Wang, et al. Fuel 280 (2020) 118710
7

<!-- PDF_PAGE: 8 -->

parameters of all PRs are collapsed into a curve after 0.266 ms. And
after a certain transition period, the self-similarity parameter stabilized
at about 0.53, which is bigger than 0.25 [26] of a single-hole nozzle jet.
A high self-similarity value indicates that the radial penetration of the
gas jet is larger than the axial penetration, which indicates that the
hydrogen jet of the outward-opening injector has a wider radial dis-
tribution range than the inward-opening injector with a circular single-
hole nozzle.
3.3.2. Penetration constant
The research of Sankesh [28] veriﬁed that the penetration scaling
formula of the single-hole nozzle jets shown in Eq. (1), is also applicable
to the CNG jets from outward-opening injector. To verify whether the
hydrogen jet from the outward-opening injector satis ﬁes Eq. (1), Fig. 18
shows the change law of the non-dimensional penetration y/(
Ṁn/ρc)0.25
with t 0.5. Except PR10, the non-dimensional penetration curves at all
pressure ratios collapse into a single line, and all the curves have ob-
vious turning points. The turning point of PR10 appeared at about
0.023 s 0.5, while other PRs appeared at about 0.029 s 0.5. The corre-
sponding time points are 0.53 ms and 0.86 ms. From Fig. 7 and the
previous discussion of the jet structure, it can be inferred that the
turning point of non-dimensional penetration corresponds to the point
of occurrence of the spherical vortex head. Although the change of y/
(Ṁn/ρc)0.25 relative to t 0.5 can re ﬂect the evolution of the jet structure,
the existence of the turning point makes Γnot constant. By modifying
the exponentsof thenon-dimensional penetration andthe timeterm,it
is found that y/( Ṁn/ρc)0.18 and t 0.83 show a proportional relationship.
As shown in Fig. 19, the penetration curves under all PRs collapse into a
straight line. This shows that the axial penetration of the hydrogen jet
from the outward-opening injector follows the following equation:
⎜⎟= ⎛
⎝
⎞
⎠
y M
ρ tΓ
̇
H
n
c
2
0.18
0.83
(6)
The ordinary least squares method is used to ﬁt the axial penetration
of all group experiments. There were 10 repeated experiments under
each PR, and a total of 900 experiments were conducted. The results are
shown in Fig. 20 , the cross mark represents the axial penetration ob-
tained from each shot. Monte Carlo simulation was carried out to verify
the rationality of linear regression. The number of simulations is one
million, and the number of simulation slope deviations greater than
twice the standard error (0.0245) is 45788. The corresponding prob-
ability is 4.58%. This proves that linear regression is reasonable. So the
penetration constant
ΓH2 is 13.18, with the standard deviation 0.0245.
The scaling correlation of hydrogen jet is di ﬀerent from the conclusion
of Sankesh [28] on the CNG jet for the similar outward-opening in-
jector. This is due to the di ﬀerence in jet structure. As the density of
CNG is eight times that of hydrogen. The larger momentum of the CNG
jet makes it di ﬀusion farther in the radial direction, and the size of the
conical structure of the jet is larger than that of the hydrogen jet. As a
result, CNG jets cannot gather to the injector axis to form a spherical
vortex in the far-ﬁ eld.
The Eq. (6) is of great signi ﬁcance for the application of such an
injector in a DI hydrogen engine. For example, when the injection
pressure is changed, the change in axial penetration distance can be
predicted by combining the injector mass ﬂow characteristics and Eq.
(6). Eq. (6) can also predict the axial penetration distance at the dif-
ferent start of injection times, considering that the in-cylinder pressure
changes in the injection window. Combining the previously discussed
jet spread angle and self-similarity characteristics, the jet spread angle
and radial penetration can also be predicted.
4. Conclusions
In this research, high-speed schlieren imaging was utilized to study
the characteristics of hydrogen jets from an outward-opening injector
Fig. 8. Radial penetration for PRs 10 to 140.
Fig. 9. Axial penetration for PRs 10 to 140.
Fig. 10. Jet velocity in radial directions for PRs 10 to 140.
X. Wang, et al. Fuel 280 (2020) 118710
8

<!-- PDF_PAGE: 9 -->

Fig. 11. Jet velocity in axial directions for PRs 10 to 140.
Fig. 12. Jet spread angle with time for PRs 10 to 140.
Fig. 13. Jet spread angle with axial penetration for PRs 10 to 140.
Fig. 14. Jet volume with time for PRs 10 to 140.
Fig. 15. Jet volume with axial penetration for PRs 10 to 140.
Fig. 16. Entrainment rate for PRs 10 to 140.
X. Wang, et al. Fuel 280 (2020) 118710
9

<!-- PDF_PAGE: 10 -->

with a 90° conical annular nozzle. The characteristics of jets with PRs
ranging from 10 to 140 were studied under di ﬀerent injection pressure
and background pressure combinations. Some conclusions can be
drawn from the results:
(1) The hydrogen jet structure from conical annular nozzle in the near-
ﬁeld is conical structure, while the jet structure develops into a
spherical vortex in the far-ﬁ eld, which is di ﬀerent from the CNG jet.
(2) The axial and radial penetration increase with the increasing of the
PR, while the di ﬀerence between adjacent PR decreases with the
increasing of the PR. The jet volume also follow this changing
tendency.
(3) Both the time course and the axial penetration course of the jet
spread angle are not sensitive to the PR in a certain PR range. The
range of PR is 20 to 140 for the time course, while the range is 60 to
140 for the axial penetration course
(4) The entrainment rate of hydrogen jets is negatively related to the
PR, which is a di ﬀerent characteristic to the hydrogen jets.
Although the entrainment capability is weak at high PR, the hy-
drogen jet can still entrain enough air.
(5) The hydrogen jet has good self-similarity after 0.27 ms under all
PRs, and the self-similarity parameter stabilized at about 0.53,
which can be used to control the mixture formation in the DI hy-
drogen engines.
(6) The non-dimensional penetration of the existing scaling correlation
of penetration for gas jets from round nozzles can re ﬂect the evo-
lution of the jet structure, but the existence of the turning point
makes Γ not constant. By modifying the exponents of the non-di-
mensional penetration and time term changed from 0.25 and 0.5 to
0.18 and 0.83, it is found that the scaling correlation is satis ﬁed
with the hydrogen jet from conical annular nozzle. The penetration
constant of the hydrogen jet
ΓH2 is 13.18.
(7) This paper studies the compound e ﬀect of P i and P 0 and we will
explore the jet characteristics at higher background pressure and
the imaging characteristics in the DI hydrogen engines.
CRediT authorship contribution statement
Xi Wang: Data curation, Writing - original draft, Visualization. Bai-
gang Sun: Conceptualization, Supervision. Qing-he Luo: Investigation,
Writing - review & editing. Ling-zhi Bao: Software. Jian-ye Su:
Methodology, Resources. Jie Liu: Validation. Xiang-chao Li: Formal
analysis.
Fig. 17. Self-similarity parameter for PRs 10 to 140.
Fig. 18. Non-dimensional penetration y/(Ṁn/ρc)0.25 with t0.5 for PRs 10 to 140.
Fig. 19. Non-dimensional penetration y/( Ṁn/ρc)0.18 with t 0.83 for PRs 10 to
140.
Fig. 20. Ordinary least squares result of 900 experiments.
X. Wang, et al. Fuel 280 (2020) 118710
10

<!-- PDF_PAGE: 11 -->

Declaration of Competing Interest
The authors declare that they have no known competing ﬁnancial
interests or personal relationships that could have appeared to inﬂ u-
ence the work reported in this paper.
Acknowledgments
This work was supported by the National Natural Science
Foundation of China (Grant No. 51276019), Shanghai Automotive
Industry Science and Technology Development Foundation, and China
Postdoctoral Science Foundation (PFCPSF2018M641215).
References
[1] Dhinesh B, Annamalai M. A study on performance, combustion and emission be-
haviour of diesel engine powered by novel nano nerium oleander biofuel. J Clean
Prod 2018;196:74 –83.
[2] Vigneswaran R, Annamalai K, Dhinesh B, et al. Experimental investigation of un-
modiﬁed diesel engine performance, combustion and emission with multipurpose
additive along with water-in- diesel emulsion fuel. Energy Convers Manage
2018;172:370–80.
[3] Dhinesh B, Raj YMA, Kalaiselvan C, et al. A numerical and experimental assessment
of a coated diesel engine powered by high-performance nano biofuel. Energy
Convers Manage 2018;171:815 –24.
[4] Nanthagopal K, Ashok B, Garnepudi RS, et al. Investigation on diethyl ether as an
additive with Calophyllum Inophyllum biodiesel for CI engine application. Energy
Convers Manage 2019;179:104 –13.
[5] Verhelst S. Recent progress in the use of hydrogen as a fuel for internal combustion
engines. Int J Hydrogen Energy. 2014;39(2):1071 –85.
[6] Verhelst S, Wallner T. Hydrogen-fueled internal combustion engines. Prog Energ
Combust 2009;35:490 –527.
[7] Luo Q, Hu J, Sun B, Liu F, Wang X, Li C, et al. E ﬀect of equivalence ratios on the
power, combustion stability and NOx controlling strategy for the turbocharged
hydrogen engine at low engine speeds. Int J Hydrogen Energy 2019;44:17095 –102.
[8] Wang X, Sun B, Luo Q. Energy and exergy analysis of a turbocharged hydrogen
internal combustion engine. Int J Hydrogen Energy 2019;44:5551 –63.
[9] Luo QH, Sun BG. Inducing factors and frequency of combustion knock in hydrogen
internal combustion engines. Int J Hydrogen Energy 2016;41(36):16296 –305.
[10] Duan J, Liu F, Sun B. Back ﬁre control and power enhancement of a hydrogen in-
ternal combustion engine. Int J Hydrogen Energy 2014;39(9):4581 –9.
[11] Wimmer A, Wallner T, Ringler J, Gerbig F. H2-direct injection-a highly promising
combustion concept. SAE Int 2005 .
[12] Hydrogen YK, Fueled ICE. Successfully overcoming challenges through high pres-
sure direct injection technologies: 40 years of Japanese hydrogen ICE research and
development. SAE Int 2018 .
[13] Tsujimura T, Suzuki Y. Development of a large-sized direct injection hydrogen
engine for a stationary power generator. Int J Hydrogen Energy 2019;44:11355 –69.
[14] Li Y, Gao W, Zhang P, Ye Y, Wei Z. E ﬀects study of injection strategies on hydrogen-
air formation and performance of hydrogen direct injection internal combustion
engine. Int J Hydrogen Energy 2019;44:26000 –11.
[15] Takagi Y, Mori H, Mihara Y, Kawahara N, Tomita E. Improvement of thermal ef-
ﬁciency and reduction of NOx emissions by burning a controlled jet plume in high-
pressure direct-injection hydrogen engines. Int J Hydrogen Energy
2019;42:26114–22.
[16] Huang
Z, Wang J, Liu B, et al. Combustion characteristics of a direct-injection en-
gine fueled with natural gas-hydrogen blends under di ﬀerent ignition timings. Fuel
2007;86:381–7.
[17] Wang J, Huang Z, Miao H, et al. Characteristics of direct injection combustion
fueled by natural gas-hydrogen mixtures using a constant volume vessel. Int J
Hydrogen Energy 2008;33:1947 –56.
[18] Abdul Rahman MT, Kawahara N, Tsuboi K, et al. E ﬀect of ambient pressure on local
concentration measurement of transient hydrogen jet in a constant-volume vessel
using spark-induced breakdown spectroscopy. Int J Hydrogen Energy
2015;40(13):4717–25.
[19] Takagi Y, Oikawa M, Sato R, Kojiya Y, Mihara Y. Near-zero emissions with high
thermal eﬃ ciency realized by optimizing jet plume location relative to combustion
chamber wall, jet geometry and injection timing in a direct-injection hydrogen
engine. Int J Hydrogen Energy 2019;44:9456 –65.
[20] Takagi Y, Mori H, Mihara Y, Kawahara N, Tomit E. Improvement of thermal e ﬃ -
ciency and reduction of NOx emissions by burning a controlled jet plume in high-
pressure direct-injection hydrogen engines. Int J Hydrogen Energy
2017;42:26114–22.
[21] Petersen BR, Ghandhi JB. Transient high-pressure hydrogen jet measurements. SAE
Int 2006-01-0652.
[22] Erfan I, Hajialimohammadi A, Chitsaz I, et al. In ﬂuence of chamber pressure on
CNG jet characteristics of a multi-hole high pressure injector. Fuel
2017;197:186–93.
[23] Deng J, Zhong H, Gong Y, et al. Studies on injection and mixing characteristics of
high pressure hydrogen and oxygen jet in argon atmosphere. Fuel
2018;226:454–61.
[24] Ouellette P. Direct injection of natural gas for diesel engine fueling. Vancouver,
Canada: University of British Columbia; 1996 .
[25] Ouellette P, Hill PG. Turbulent transient gas injections. J Fluids Eng
1999;122(4):743–52.
[26] Rogers T, Petersen P, Koopmans L, Lappas P, Boretti A. Structural characteristics of
hydrogen and compressed natural gas fuel jets. Int J Hydrogen Energy
2015;40(3):1584–97.
[27] Seboldt D, Lejsek D, Wentsch M, Chiodi M, Bargende M. Numerical and experi-
mental studies on mixture formation with an outward-opening nozzle in a SI engine
with CNG-DI. SAE Int 2016 .
[28] Sankesh D, Petersen P, Lappas P. Flow characteristics of natural-gas from an out-
ward-opening nozzle for direct injection engines. Fuel 2018;218:188 –202.
[29] Zhao J, Liu W, Grekhov L. Visualization research on in ﬂuence of ambient pressure
on CNG jet characteristics of gas injector with outward-opening nozzle. Fuel
2019;257:110684.
[30] Erfan
 I, Chitsaz I, Ziabasharhagh M, et al. Injection characteristics of gaseous jet
injected by a single-hole nozzle direct injector. Fuel 2015;160:24 –34.
X. Wang, et al. Fuel 280 (2020) 118710
11
