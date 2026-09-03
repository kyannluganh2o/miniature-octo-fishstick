<!-- PDF_PAGE: 1 -->

Standard Article
International J of Engine Research
2023, V ol. 24(5) 1892–1915
/C211IMechE 2022
Article reuse guidelines:
sagepub.com/journals-permissions
DOI: 10.1177/14680874221107188
journals.sagepub.com/home/jer
Optical characterization of stratified-
premixed natural gas direct-injection
combustion regimes
Jeremy Rochussen , Matthew Knight , Gibson Clark
and Patrick Kirchen
Abstract
Gaseous fuels for heavy-duty internal combustion engines provide inherent advantages for reducing CO 2, particulate
matter (PM), and NO X emissions. Pilot-ignited direct-injected NG (PIDING) combustion uses a small pilot injection of
diesel to ignite a late-cycle main direct injection of NG, resulting in significant reduction of unburned CH 4 emissions
relative to port-injected NG. Previous works have identified NG premixing as a critical parameter establishing
indicated efficiency and emissions performance. T o this end, a recent experimental investigation using a metal engine
identified six general regimes of PIDING heat release and emissions behavior arising from variation of NG stratification
through control of relative injection timing (RIT) of the NG with respect to the pilot diesel. The objective of the
current work is to provide comprehensive description of in-cylinder fuel mixing of direct injected gaseous fuel and its
impacts on combustion and pollutant formation processes for stratified PIDING combustion. In-cylinder imaging of
OH*-chemiluminescence (OH *-CL) and PM (700 nm), and measurement of local concentration of fuel is considered
for 11 different RIT, representing 5 regimes of stratified PIDING combustion (performed with P
inj =2 2:0 MPa and
f =0 :63). The magnitude and cyclic variability of premixed fuel concentration near the bowl wall provides direct
experimental validation of thermodynamic metrics ( RITpremix, SOING, trans, RIT/C3 ) that describe the fuel-air mixture state of
all 5 regimes of PIDING combustion. The local fuel concentration develops non-monotonically and is a function of RIT .
High indicated efficiency and low CH 4 emissions previously observed for stratified-premixed PIDING combustion in
previous (non-optical) investigations are due to: (i) very rapid reaction zone growth ( . 45 m/s) and (ii) more
distributed early reaction zones when overlapping pilot and NG injections cause partial pilot quenching. These results
connect and extend the findings of previous investigations and guide the future strategic implementation of NG
stratification for improved combustion and emissions performance.
Keywords
Direct injection, natural gas, optical, stratified, injection timing, pilot ignited, fuel mixing, chemiluminescence, partially
premixed
Date received: 9 November 2021; accepted: 6 May 2022
Introduction
On-road freight activity is forecasted to grow 25% by
2030 and is estimated to already account for 7% of
world energy-related CO
2 emissions.1,2 The stringent
energy density requirements for long-haul trucking repre-
sents a major challenge to the wide-spread electrification
in this sector and motivates the development of advanced
propulsion technologies for the short- and medium-term
which reduce greenhouse gas (GHG) emissions.
3
Life-cycle analysis indicates a net reduction of GHG
emissions of 10%–15% is realistic for heavy-duty vehi-
cles where diesel is replaced by NG in addition to
reduction of particulate matter (PM) and NO X emis-
sions.4–6 Development of NG propulsion technologies
also represents a commercially attractive pathway for
application of more deeply decarbonized gaseous fuels
Department of Mechanical Engineering, The University of British
Columbia, Vancouver , BC, Canada
Corresponding author:
Jeremy Rochussen, Department of Mechanical Engineering 2054-6250
Applied Science Lane, The University of British Columbia, Vancouver , BC
V6T1Z4, Canada.
Email: jrochussen@mech.ubc.ca

<!-- PDF_PAGE: 2 -->

such as renewable NG (RNG) and hydrogen, which
are still immature in terms of infrastructure and techni-
cal readiness.
Because the main constituent of NG, CH 4,i sa
potent GHG, 4 emissions of unburned hydrocarbons
(uHCs) from NG engines is an important challenge
that must be addressed. 7,8 Several premixed (i.e. port-
injected) NG combustion concepts such as reactivity-
controlled compression ignition and split diesel injec-
tions have been shown as valuable approaches for
reducing uHC emissions and increasing efficiency with
limited penalty to NOX at both low- and high-load con-
ditions.9,10 Pilot-ignited direct-injection NG (PIDING)
combustion is another concept, which uses a late-cycle
pilot injection of diesel (approximately 5% of total fuel
energy) followed by a main injection of NG. Typically,
the main PIDING combustion process is non-premixed,
which allows for higher compression ratios, providing
high efficiency and very low uHC emissions at the cost
of increased PM and NO
X emissions relative to highly
premixed (i.e. port-injected) NG systems.5,11
In PIDING combustion, a portion of the NG also
reacts in a rapid partially-premixed mode in parallel to
establishment of a quasi-steady jet flame. 12 The fraction
of fuel converted in the partially-premixed fraction,
fpremix, is predominantly defined by the time available
for premixing prior to ignition, which can be manipu-
lated through changes in the relative injection timing
(RIT) of the NG with respect to the pilot, defined as:
RIT = SOING /C0 SOIpilot ð1Þ
where SOING and SOIpilot are the commanded start of
NG and diesel pilot injection, respectively. Several
investigations have demonstrated that significant
advantages in emissions and efficiency can be achieved
by intentionally increasing the NG premixing time and
promoting more premixed combustion by reducing the
RIT to negative values (i.e. NG injection prior to pilot
injection). To this end, two general approaches have
been considered: (i) slightly premixed combustion
(SPC) modes using a small reduction of RIT from con-
ventional non-premixed PIDING values (e.g. Faghani
et al.
13 and McTaggart-Cowan et al. 14,15) and (ii)
stratified-premixed PIDING modes where one or more
NG injections are performed during the compression
stroke to generate highly premixed conditions (e.g.
Florea et al. 16, Neely et al., 17 Li et al., 18 and Munshi
et al. 19). For both these approaches, late-cycle SOIpilot
is used for fast-response combustion phasing control.
SPC was studied with 22m s \ RIT \ +2m s
(operating conditions with RIT \ 0 were designated
SPC modes) and an optimized SPC mode achieved a
90% reduction in PM mass and a 2% increase of gross
indicated efficiency, h
i, g, relative to a conventional
high-load PIDING operating condition. This opti-
mized SPC mode had negligible penalty to NO X or
CH4 emissions, however with advancing SOING emis-
sions of both NO X and CH 4 increased significantly. 13
The decreased PM emissions were attributed to the
increased NG premixing time prior to NG ignition
resulting in less NG with an equivalence ratio, f, in the
PM formation region (2 \ f \ 5). In earlier studies,
increased efficiency and reduction of CO and PM was
also observed for similar SPC operating conditions
(RIT . /C0 38), which were attributed to higher peak
apparent heat release rates (AHRR) and reduced com-
bustion duration.14,15 The major drawbacks of the SPC
mode were indicated to be increased cycle-to-cycle
variability (CCV, measured as COV of peak cylinder
pressure, P
cyl) and combustion harshness (maximum
rate of pressure rise, RoPR), and moderate increases of
CH
4 emissions at medium and low load. 14,15
Stratified-premixed PIDING combustion was inves-
tigated by advancing SOING up to 234 CAD after top
dead center (aTDC) such that the end of NG injection
(EOING) occurs well before pilot injection and auto-
ignition. This strategy has been termed co-direct injec-
tion (DI
2) and demonstrated increased efficiency with
decreased PM and CO relative to non-premixed
PIDING combustion and acceptable CCV (COV of
indicated mean effective pressure limited to less than
2%).
16 Based on numerical simulation, the authors
describe the DI2 combustion as rapid flame propaga-
tion through a stratified NG-air mixture, which initiates
at the pilot ignition regions. The flame propagation
occurs in parallel to NG-air mixing processes driven by
both diffusion and jet-induced turbulence.
16 Relative to
port-injected NG operation, a 75% reduction in the
emissions of CH 4 was achieved. However, CH 4 emis-
sions rapidly increased for SOING \ /C0 34 CAD aTDC
due to impingement of the NG fuel jets outside of the
piston bowl.16,17 Emissions of NO X were also observed
to be significantly higher for DI2 relative to comparable
non-premixed PIDING combustion. In light of the very
low PM emissions of DI2, EGR was considered a viable
method to reduce NO X, in agreement with earlier
experimental investigations.14,16
Splitting the main NG injection into early- and late-
cycle injections has also been considered as a strategy
to control NG stratification. 18,19 Increased efficiency
and a reduction of PM and CO were reported for these
strategies, although limiting uHC emissions was a chal-
lenge. These investigations indicated that the increased
turbulent mixing rates produced by the late NG injec-
tion supported higher flame propagation speeds and
reduced CH
4 emissions from slow flame extinction, 19
which has also been noted for DISI combustion. 20–22
Investigations of stratified-PIDING combustion
have used SOING to control the NG residence time
prior to combustion and therefore the degree of NG
stratification. This has been quantified using either
RIT,
12–15 and/or the time delay between NG injection
and the start of partially-premixed NG combustion,
u
SOC, NG.12,23,24 In-cylinder OH*-chemiluminescence
(OH*-CL) imaging of PIDING combustion with 26
ms \ RIT \ + 1.5 ms indicated that the leading edge
of the main AHRR peak coincided with start of
Rochussen et al. 1893

<!-- PDF_PAGE: 3 -->

partially-premixed NG combustion and that this is an
appropriate metric for uSOC, NG.12 A subsequent non-
optical measurement campaign defined uSOC, NG as the
phasing at which the AHRR reaches 20% of its maxi-
mum value for 226.5 ms \ RIT \ +3 :0 ms:
uSOC, NG = ujAHRR =0 :2/C1 max(AHRR) ð2Þ
where uSOC, NG was used to define the NG premixing
time, tNG:
tNG½ms/C138 = uSOC, NG /C0 SOING ð3Þ
These previously introduced metrics to characterize the
NG premixing are graphically summarized in Figure 1
with a sample measurement of AHRR for a typical
(non-premixed) PIDING operating condition
(RIT = + 1 ms).
All investigations of stratified PIDING combustion
have noted transitions in the characteristic behavior of
PIDING combustion for different degrees of NG pre-
mixing (e.g. transition of PM sensitivity to RIT for
non-premixed PIDING vs SPC
14,25). However, the
majority of published investigations are limited to sub-
sets of the full spectrum of NG premixing that is possi-
ble with PIDING fuel systems, where RIT is
continuously variable. To connect the findings of these
investigations and develop a framework of generally-
relevant (i.e. not engine-specific) PIDING combustion
regimes, a systematic evaluation of stratified-PIDING
combustion and emissions spanning from fully-
premixed NG to non-premixed PIDING combustion
was recently conducted.
24 The identified regimes of
PIDING combustion motivate and guide the current
work and are summarized below.
Regimes of stratified PIDING combustion
To classify regimes of PIDING combustion, AHRR
and emissions behavior was analyzed for 226.5 ms
4RIT4 + 3.0 ms with f =0 :47 /C0 0:71, and
Pinj =1 4 /C0 22 MPa in a previous study employing an
all-metal engine. 24 A constant engine speed
(1000 RPM) was considered, so the range of RIT is
equivalently expressed on a crank angle basis as
/C0 15984RIT4 +1 88.
Experimental results of combustion and emissions
performance across the full range of NG premixing
conditions considered in the all-metal investigation are
presented in Figure 2. 24,26 Combustion regimes were
considered to be domains of RIT (representing NG
stratification) where relevant heat release features (e.g.
combustion duration, ignition delay, efficiency) and
emissions responded in the same manner to major
engine control parameters ( Pinj, RIT, f). Combustion
regime domains for the operating condition shown in
Figure 2 ( f =0 :63, Pinj = 22 MPa) are also identified
with dotted vertical lines. Combustion and emissions
behavior of the minimally-premixed, variable-premixed
fraction, and stratified-premixed (late-cycle) regimes
align with results in the literature of non-premixed
PIDING,5,11 SPC,13–15DI2,16,17,27 and port-injected
dual-fuel28 combustion strategies, respectively. Of par-
ticular interest is the stratified-premixed (late-cycle)
regime (termed DI2 elsewhere), where low CO and CH 4
emissions are achieved with high efficiency and moder-
ate combustion harshness.
In Figure 3, a generalized summary of the 6 identi-
fied regimes of PIDING combustion ( s1 !s6 ) and 4
critical injection phasings distinguishing transitions
between the regimes ( sA !sD ) is presented. These injec-
tion phasings were determined such that they are gen-
eral to a wide range of operating conditions ( f and
Pinj) and are intended to provide a common framework
within which to compare and investigate the effects of
NG stratification on direct-injected NG combustion
performance.
All combustion regimes were classified as either
early- or late-cycle regimes based on whether NG jet
impingement occurs inside (late-cycle) or outside the
piston bowl (early-cycle), which significantly influenced
injection control strategy, combustion behavior, and
emissions as noted in other investigations. 16,17 Near the
transition between early- and late-cycle NG injection
(SOING’SOING, transsB ) poor engine performance (com-
bustion stability and emissions) occurs. 16,24
Two early-cycle PIDING regimes were distinguished
by RITinsens: (sA , RITinsens:’ /C0 538): (i) The ‘‘RIT-
Insensitive Premixed Regime’’ ( s1 )f o r RIT \ RITinsens:,
emissions were not significantly affected by changes in
RIT and combustion and emissions behavior was
observed to be consistent with port-injected dual-fuel
combustion, and (ii) the ‘‘Stratified-Premixed Regime’’
(early-cycle) (
s2 ) for RIT . RITinsens:, where RIT had a
significant influence on combustion and emissions.
Figure 1. Definitions for key PIDING injection and combustion
phasings.
1894 International J of Engine Research 24(5)

<!-- PDF_PAGE: 4 -->

For late-cycle operating conditions
(SOING . SOING, trans), ignition, main combustion, and
emissions behavior were very sensitive to Pinj and RIT.
Defining general late-cycle PIDING combustion
regimes valid for P
inj =1 4 /C0 22 MPa and
f =0 :47 /C0 0:71 required RIT to be scaled by the NG
injection duration:
RIT/C3 = RIT /C0 RITcrit
tinj, NG
ð4Þ
where tinj;NG is the NG injection duration (see Figure
fig : PIDINGDefinitionsÞ, RIT/C3 is the scaledRIT; andRITcrit is
the minimum RIT at which tNG remains at the minimum
value observed for typical non-premixed PIDING and is
not sensitive to RIT. In a previous investigation,
RIT
crit ¼ 0:6860:17 ms was measured for all operating
conditions covered in the current work.rochussen2021 heat
However, it should be noted that this value of RITcrit is
expected to be sensitive to injector geometry and engine
speed, and is thereforeapplication specific.
Figure 2. Summary of PIDING emissions and engine performance metrics across spectrum of NG premixing ( f =0 :63, Pinj =2 2M P a ) .
Figure 3. Summary of identified regimes of AHRR and emissions behavior of stratified-PIDING combustion with respect to critical
injection phasings for /C0 1538 \ RIT \ +1 88,0 :47 \ f \ 0:71, and 14 4Pinj422 MPa. Figure adapted from Rochussen et al. 24
Rochussen et al. 1895

<!-- PDF_PAGE: 5 -->

The three late-cycle combustion regimes were identi-
fied using RIT/C3 : (i) The ‘‘Stratified-Premixed Regime’’
(late-cycle) ( s4 ) is characterized by RIT/C3 \ /C0 1( sC )
where the NG injection is sufficiently early that EOING
occurs well before the start of combustion ( uSOC, NG)
and combustion and emissions behavior is consistent
with DI2 combustion.16,17 For /C0 1 ; RIT/C3 \ 0, overlap-
ping pilot and NG injections and tNG = f(RIT) indi-
cated that fpremix = f(RIT). This regime was labeled the
‘‘Variable Premixed Fraction Regime’’ ( s5 ) and com-
bustion and emissions behavior was consistent with
SPC behavior. 13,14 For a large portion of the variable
premixed fraction regime, the overlapping pilot and
NG injections resulted in quenching of the pilot by the
NG jets. For RIT
/C3 . 0( sD ), tNG was at a minimum
value and insensitive to RIT. This range of RIT includes
typical non-premixed PIDING applications and is
labeled the ‘‘Minimally-Premixed Regime’’ ( s6 ).
The above description of the spectrum of stratified
PIDING combustion connects investigations of differ-
ent stratified PIDING combustion strategies into a sin-
gle generalized framework. To develop and refine this
framework into a useful conceptual tool for PIDING,
complementary measurements investigating the stratifi-
cation and structure of NG mixing and combustion
processes are needed. To address this gap, investigators
have performed in-cylinder imaging of PIDING com-
bustion processes following one of two general
approaches: (i) optically-accessible engines fitted with
production multi-jet PIDING injectors,
12,29–32 or (ii)
more fundamental investigations of single pilot-NG jet
pairs in rapid compression/expansion machines
(RCEMs).
23,33,34 These investigations have been valu-
able for characterizing the structure of typical non-
premixed PIDING combustion, however only a subset
of these investigations address PIDING combustion
with RIT
/C3 \ 0.
Study of single pilot-NG jet pairs in RCEMs has
demonstrated that RIT and the geometric injection
angle between the pilot and NG jets has significant
impact on both pilot and NG ignition.
23,33,34 In partic-
ular, quenching of the pilot reactants by the cold NG
jet has shown to increase variability in the ignition
phasing and location of both fuels, which impacts NG
premixing and main combustion behavior, as has been
noted in optical engine experiments.
12,29,31 Crucially,
these fundamental studies only consider unbounded
NG jets, and do not provide insight to the effects of
NG jet impingement on combustion chamber surfaces
(i.e. the piston bowl).
Decreasing RIT from the minimally-premixed
regime such that the pilot injection is timed to ignite
the tail of the NG jet (i.e. negative RIT) was demon-
strated to entrain the diesel pilot by the NG jet in an
optical engine.
30 This resulted in increased NG premix-
ing and more rapid heat release. In-cylinder OH*-CL
imaging for a slightly wider range of RIT has demon-
strated that the main combustion process changes from
a quasi-steady jet flame, to rapid distributed-ignition,
to flame propagation as the RIT is adjusted between
+ 1.3, + 0.3, and 21.0 ms, respectively. For the same
measurement conditions, pyrometric imaging indicated
significant reduction of in-cylinder soot production as
RIT was decreased,
32 which corroborates numerical
modeling results.13
RCEM and optically-accessible engine measure-
ments of stratified PIDING combustion to date have
provided significant insight to the role of pilot-NG
interactions and the effects of increased NG premixing
on PIDING combustion behavior. However, the range
of NG premixing conditions investigated is narrowly
focused on the transition between the minimally-
premixed and variable premixed fraction regimes.
Additional consideration of the role of combustion
chamber geometry is needed as this is a critical para-
meter for stratified PIDING combustion.
16,17,24
Finally, comparison of in-cylinder NG stratification
and reaction zone structures to combustion and emis-
sions performance is needed.
Objectives and outline
The objectives of this work are to: (i) support and
refine the previously identified regimes of PIDING
combustion and associated critical injection phasings
and (ii) describe the in-cylinder mixing processes of
direct injected gaseous fuel and its impacts on combus-
tion and in-cylinder pollutant formation processes.
These objectives are addressed by applying in-cylinder
imaging and local fuel concentration measurements to
stratified PIDING combustion conditions ranging
from homogeneously-premixed to nominally non-
premixed in an optically-accessible engine.
The optical research engine facility, measurement
diagnostics, and selected stratified PIDING combus-
tion conditions are described first. Discussion of results
is divided into 3 parts addressing adjacent domains of
the spectrum of stratified PIDING combustion: (i)
Minimally-premixed and variable premixed fraction
regimes, (ii) Variable premixed fraction and stratified-
premixed (late-cycle) regimes, and (iii) Early-cycle
regimes. Last, a summary of the important in-cylinder
processes is presented for all combustion regimes.
Experimental facility and methods
The experimental facility used in this investigation is
based on a 2.0 L, single-cylinder, optically-accessible
Ricardo Proteus engine, the specifications of which are
given in Table 1. This facility is operated in either an
optically-accessible configuration with a Bowditch pis-
ton and quartz window, or in a conventional all-metal
configuration (thermodynamic configuration). The cur-
rent investigation only considers the optical engine con-
figuration, however recently published measurements
collected using the thermodynamic engine configura-
tion were used to guide the current work and provide
complementary measurement of fuel, air, and exhaust
1896 International J of Engine Research 24(5)

<!-- PDF_PAGE: 6 -->

emissions flowrates.24 Details of the optical engine con-
figuration are presented in Figure 4.
The research engine facility is fitted with a first gen-
eration Westport Fuel Systems (WFS) High-Pressure
Direct-Injection (HPDI) injector and commercial WFS
dome-loaded self-relieving regulator (DLSR). A cus-
tom programmable engine control unit (ECU) and
HPDI injector with independently actuated concentric
needles allows arbitrary relative injection timing of the
diesel and NG injections. The injector is mounted verti-
cally and concentric to the piston bowl with 9 equally-
spaced NG orifices and 9 pilot diesel orifices midway
between each NG orifice (see Figure 5). Diesel rail pres-
sure is controlled by the operator and the DLSR auto-
matically maintains the NG rail pressure at 8 bar below
the diesel rail pressure. Detailed characterization of the
pipeline NG used for the primary fuel was out of scope
in the current work. The effects of NG composition on
the main PIDING combustion processes have been
reported to be predominantly related to differences in
fuel density (impacting injection duration) and PM
emissions due to varying fractions of longer chain
hydrocarbons.
36 These observations have been made
for non-premixed PIDING combustion, and it should
be noted they may not apply to the wide range of strati-
fied PIDING conditions considered in the current
work.
A Bowditch piston with a flat-bottomed, cylindrical
piston bowl housing a quartz window offset from the
cylinder axis by 4 mm provides a 78 mm diameter opti-
cal access to the combustion chamber (see Figure 5).
This piston bowl differs from the torroidal bowl in the
thermodynamic piston and may affect jet impingement
and fluid flow patterns, however AHRR measurement
for all conditions indicated limited discrepancy in com-
bustion behavior. The Bowditch piston also has a
slightly lower geometric compression ratio, which
requires adjustment of intake temperature and pressure
to match P
cyl and estimated Tcyl at SOIpilot.
Combustion imaging
Two imaging systems were used to simultaneously
record: (i) OH*-CL at 310 nm and (ii) emission from
PM at 700 nm. The imaging systems were synchronized
to one another with a constant framerate of 15,000 Hz
(’0.4 CAD image temporal resolution) and focused to
the horizontal midplane of the combustion chamber at
TDC. All imaging is line-of-sight and although it is not
possible to infer variations along the optical path, they
provide qualitative indication of the position and inten-
sity of reaction zones and soot clouds. Specifications of
the imaging system hardware is provided in Table 2.
OH*-CL measurements are used to analyze ignition,
main combustion reaction zone structure and growth
rates. The 700 nm images are used as an indicator of
PM, with broadband incandescence from PM being the
dominant emitter at 700 nm.
37 The presence of PM has
also been shown to significantly attenuate OH*-CL,
which must be considered when analyzing OH*-CL for
non-premixed combustion systems. 32 Further detail on
the analysis of OH*-CL images is provided in
Appendix B.
Due to the wide range of combustion conditions
imaged (i.e. non-premixed, partially-premixed, fully-
premixed) the exposures were adjusted for each operat-
ing condition in order to maximize the dynamic range
used on each camera sensor without incurring sensor
saturation (exposures provided in Table 4). Where
applicable, measurements of OH*-CL and PM image
intensities are scaled by 1/exposure to allow direct com-
parison of different operating conditions.
Local fuel concentration measurement
To characterize the fuel-air mixture development, an
infrared absorption probe (LaVision ICOS) was used
to measure the local CH 4 concentration. The develop-
ment and theory of the ICOS is described in detail else-
where,
38 and implementation of this instrument in the
T able 1. Engine specifications and engine set-points common to all measurement conditions. Operating conditions for the
thermodynamic configuration correspond to previously published measurements. 24
Parameter Thermodynamic Optical
Displacement [L] 2.0 2.0
Bore [mm] 130 130
Stroke [mm] 150 150
Compression ratio [-] 13.25:1 12.6:1
Piston bowl shape Eccentric torroid Eccentric cylinder
Speed [rpm] 1000 1000
T
intake [8C] 40 8 558
Pintake [bar-a] 1.26 1.4
Pinj [bar] 220 220
Swirl number 0.1
Direct injector Westport Fuel Systems 1 st Generation HPDI
Pilot fuel Shell V-power (ULSD)
Pilot fuel CN . 40 (CAN/CGSB-3.517)
Primary fuel Pipeline natural gas
Primary fuel comp. T ypically . 96% CH
4 (e.g. McT aggart-Cowan et al.35,36)
Rochussen et al. 1897

<!-- PDF_PAGE: 7 -->

current experimental facility is described in previous
work.39 A brief review of the theory and implementa-
tion are presented here.
The ICOS measures absorption of light sent via fiber
optic cable from a quartz-tungsten-halogen lamp to a
20 mm
3 measurement volume protruding from the
cylinder head. Light introduced to the measurement
volume is reflected by a mirrored surface, transmitted
back to a second fiber optic cable and 3.4 m m narrow
band-pass filter before reaching the detector. This
absorption band measures the C-H vibrational band,
characteristic of hydrocarbon fuels, and is related to
the fuel molar concentration within the measurement
volume, X
fuel.
In the current work, the relative magnitude of Xfuel
between operating conditions is analyzed. It is therefore
permissible to not account for the sensitivity of the
spectral absorption strength of the mixture, s, to com-
bustion chamber pressure and local fuel temperature,
which are approximately equivalent throughout the
compression stroke of all operating conditions consid-
ered in this work. To denote that this is a qualitative
measurement, the relative fuel molar concentration is
denoted as X
0
fuel throughout the remainder of the
discussion. The calculation of X0
fuel is developed in detail
in Appendix A, and is summarized by equation (11):
X0
fuel(u)a
In I uðÞ
Io
/C16/C17
P uðÞ
1
g
0
@
1
A ð5Þ
Where I(u) is the measured IR light intensity as a func-
tion of crank angle, Io is a reference light intensity mea-
sured each cycle, P(u) is the measured cylinder pressure,
and g is the ratio of specific heats (assumed to be
constant).
The ICOS provides a point measurement, therefore
detailed observations of X0
fuel(u) are specific to the posi-
tion of the ICOS measurement volume. As shown in
Figure 5, the ICOS is located near the piston bowl wall
(at 74% of bowl radius) and midway between two NG
jet axes. Previous OH*-CL imaging of minimally-
premixed PIDING combustion indicates this position is
at a greater radius than the pilot ignition sites and is a
suitable location for characterizing the NG mixture
development prior to the partially-premixed combus-
tion processes.
12 Analysis of the phasing of CH 4 con-
sumption (i.e. rapid decrease of X0
fuel) therefore provides
Figure 4. Single-cylinder optical engine facility. LaVision ICOS and high-speed imaging systems configuration shown. Note that
ICOS measurement volume is located between two adjacent NG injection axes (see Figure 5).
1898 International J of Engine Research 24(5)

<!-- PDF_PAGE: 8 -->

a premixed combustion phasing measurement that is
complementary to the line-of-sight OH*-CL imaging,
but measured completely independently. The center of
the measurement volume is positioned 9 mm below the
firedeck (see Figure 4) to minimize the influence of
combustion chamber walls on X
0
fuel.
Selected operating conditions
The operating conditions considered in this investiga-
tion replicate a subset of recently published measure-
ments collected using the thermodynamic engine
configuration.
24 There, a fine sweep of RIT was per-
formed for /C0 1598 \ RIT \ +1 88 with Pinj = 14, 18, 22
MPa and f =0 :47, 0:54, 0:63, 0:71. Here, only
Pinj = 22 MPa and f =0 :63 are considered for 11 RIT
values. The 11 operating conditions were selected such
that each regime of PIDING combustion has at least
one measurement, with the exception of the transition
NG jet impingement transition regime where combus-
tion was too unstable to be measured in the optical
engine. Engine operating parameters held constant
across all considered operating conditions are presented
in Table 3 and injection parameters are given in Table
4. SOI
pilot and SOING given in Table 4 are the com-
manded injection timings. In all figures and analysis
presented within this work the actual injection timings
(i.e. including needle opening delay) are presented. 26
The injector needle dynamics are also sensitive to cylin-
der pressure, so t
inj, NG was adjusted to maintain a
constant mNG for all SOING. In Figure 6, the selected
operating conditions are presented in terms of SOIpilot
and SOING, and are compared to the thermodynamic
operating conditions previously investigated with
Pinj = 22 MPa and f =0 :63.
The engine was operated in a skip-firing mode con-
sisting of 3 consecutive fired cycles followed by 17
motored cycles (no combustion) to allow the window
to cool. Images were recorded on the 3
rd fired cycle as
there were no significant differences in AHRR between
the third and subsequent fired cycles. The images,
AHRR, and ICOS measurements presented in the cur-
rent work are ensemble averaged from a set of 15 skip-
firing sequences (i.e. 15 imaged cycles) unless explicitly
indicated to be single-cycle measurements. Using an
intake by-pass valve (see Figure 4), the intake air sys-
tem was pre-conditioned to the desired temperature
and pressure prior to every test. This reduced variabil-
ity in the intake charge conditions between tests and
improved repeatability of measurements.
Characterization of regimes of PIDING
combustion
In this work, characterization of the NG mixture devel-
opment and the resulting features of the combustion
Figure 5. Camera view through Bowditch piston bowl.
T able 2. Imaging system specifications.
Parameter OH *-CL Imaging System
Camera Photron SA-1 CMOS
Image intensifier LaVision high speed IRO
Lens Cerco 98 mm-f/2.8 UV
Aperture f/2.8
Frame rate 15,000 Hz
Resolution 410 3 410
Narrow band-pass 310 nm CWL, 20 nm
Filter FWHM
700 nm Imaging System
Camera Photron S-12 CMOS
Lens 60 mm-f/2.8 Micro-Nikkor
Aperture f/2.8
Frame rate 15,000 Hz
Resolution 410 3 410
Narrow band-pass 700 nm CWL, 10 nm
filter FWHM
T able 3. Baseline operating conditions.
Operating parameter Set-point
Speed [RPM] 1000
Tintake [8C] 55
Pintake [bar-a] 1.4
mdiesel [mg/cycle] 7 62
mNG [mg/cycle] 92 63
NG energy fraction [%] 94
f [-] 0.63
P
inj [bar] 220
Rochussen et al. 1899

<!-- PDF_PAGE: 9 -->

structure(s) are investigated to refine descriptions of the
regimes of PIDING combustion previously proposed
based on emissions and AHRR analysis. Local relative
fuel-air ratio, X
0
fuel, for non-reacting cases (no pilot igni-
tion) is assessed to qualitatively characterize the NG
mixture development with respect to RIT and NG pre-
mixing time, tNG. Subsequently, X0
fuel for reacting con-
ditions is compared to in-cylinder imaging and AHRR
to characterize the reaction zone structures and relative
phasing of premixed fuel consumption for each regime
of PIDING combustion. To distinguish characteristics
of each regime of PIDING combustion, the discussion
compares adjacent domains of RIT:
1. Minimally-premixed ! variable-premixed
2. Variable-premixed ! stratified-premixed (late-
cycle)
3. Stratified-premixed (early-cycle) ! RIT-insensitive
premixed
To describe the spectrum of premixed PIDING com-
bustion regimes, a summary of X
0
fuel characteristics,
AHRR features, and reaction zone structures is pre-
sented as a function of RIT for all regimes of PIDING
combustion.
Non-reacting NG mixture development
The NG mixture stratification is a key parameter influ-
encing ignition, main combustion, and emissions beha-
vior for all regimes of PIDING combustion. Following
direct injection of the NG, complex fluid mixing pro-
cesses will cause the fuel-air mixture to develop from a
highly stratified state (i.e. pure fuel in the core of the
NG jet) toward a fully-developed homogeneous state.
The transient fuel-air mixture states are a function of
the NG premixing time, t
NG, and the turbulent flow
field of the combustion chamber. The NG premixing
time is readily controlled by RIT, however the flow
field is a function of a multitude of parameters many of
which are also time-varying (e.g. chamber geometry,
turbulent kinetic energy, etc.).
In Figure 7, X0
fuel for non-reacting operation,
X0
fuel, NR, is presented to characterize fuel-air mixing for
the considered regimes of PIDING combustion. Non-
reacting engine operation was performed by removing
the pilot injection (i.e. the ignition source) and main-
taining all other measurement parameters equivalent to
the corresponding reacting condition. Figure 7 divides
the measurements into the three ranges of RIT, which
are also used to structure subsequent discussion of the
corresponding reacting cases. As a point measurement,
X
0
fuel is sensitive to turbulent advection of fuel, which
results in high cyclic variability of X0
fuel shortly after
SOING when the NG distribution is most heteroge-
neous. For the relatively small sample sizes discussed in
this work (15 repeated measurements), this cyclic varia-
bility can impact the ensemble averaged X
0
fuel shortly
after SOING (e.g. small difference between two operat-
ing conditions with SOING =+ 4 :58 in Figure 7).
For all non-fired operating conditions shown in
Figure 7, X0
fuel, NR is a strong, non-monotonic function
of the NG premixing time (i.e. CAD after SOING) for
approximately 60–70 CAD ( ’10–12 ms) after SOING
before a homogeneous mixture is indicated by
d=dt(X0
fuel, NR)’0. Features of the development of
X0
fuel, NR are also sensitive to RIT for conditions where
SOING is varied (all RIT \ /C0 28, see Figure 6). To
T able 4. Summary of operating conditions investigated in optical engine. SOING and SOIpilot also presented in Figure 6.
Regime RIT
[CAD]
SOIpilot
[CAD aTDC]
tinj, pilot
[ms]
SOING
[CAD aTDC
tinj, NG
[ms]
Exposure
(310 nm)
[m s]
Exposure
(700 nm) [m s]
RIT/C3 . 0 + 10 –14.5 0.75 –4.5 1.27 18.0 1.7
RIT/C3 . 0 + 6 –10.5 0.75 –4.5 1.27 18.0 1.6
/C0 1 \ RIT/C3 \ 0 + 2 –7.5 0.75 –5.5 1.26 12.5 6.7
/C0 1 \ RIT/C3 \ 0 –2 –7.0 0.75 –9.0 1.24 7.0 2.0
RIT/C3 \ /C0 1 –6 –6.0 0.75 –12.0 1.29 6.0 2.0
RIT/C3 \ /C0 1 –10 –6.0 0.75 –16.0 1.31 6.5 12.5
RIT/C3 \ /C0 1 –14 –7.0 0.75 –21.0 1.32 7.0 12.5
RIT . RITinsens: –33 –19.0 0.75 –52.0 1.48 18.0 25.0
RIT’RITinsens: –53 –17.0 0.75 –71.0 1.50 9.0 25.0
RIT \ RITinsens: –95 –17.0 0.75 –110.0 1.50 10.0 25.0
RIT \ RITinsens: –153 –18.0 0.75 –171.0 1.50 12.0 25.0
Figure 6. Operating conditions investigated with optical engine
(circular markers). Previously investigated operating conditions from
the thermodynamic engine configuration shown with solid line.24
1900 International J of Engine Research 24(5)

<!-- PDF_PAGE: 10 -->

highlight the difference in NG mixture development as
it pertains to combustion, approximate phasing of 50%
indicated heat release, CA
50, is also shown in Figure 7.
For all conditions with late-cycle injections (top and
middle plot of Figure 7), NG stratification has not
fully-developed by the time of combustion. The peak
X0
fuel, NR occurs after CA 50 for RIT ø 2 CAD
(RIT/C3 ø /C0 0:3), but prior to CA50 for RIT4 /C0 2 CAD
(RIT/C3 4 /C0 0:8). X0
fuel, NR in the bottom plot of Figure 7
indicates fully-developed homogeneous fuel-air mix-
tures at the time of combustion are likely for very early
SOI
NG, but may not have developed for
RIT =/C0 338, /C0 538.
The development of X0
fuel, NR for early-cycle NG
injections (bottom plot of Figure 7) is distinct from that
of late-cycle injections due to very different chamber
conditions (i.e. chamber geometry, charge density, and
injection pressure ratio). The very high initial X
0
fuel, NR
in the bottom plot of Figure 7 is a result of the NG jet
passing the ICOS measurement volume while there is
low charge density for very early SOING.
While the X0
fuel, NR behavior for each operating con-
dition is particular to the location of the fuel concentra-
tion measurement volume, the observed behavior
demonstrates that SOING and the subsequent interac-
tion of the NG injection with the cylinder flow field has
significant implications for the development of the
NG-air mixture.
Variable premixed fraction regime
For PIDING combustion in the minimally-premixed
and variable premixed fraction regimes, late SOING
produces heterogeneous fuel-air mixtures. In the
minimally-premixed regime, tNG has a minimum value
and tNG 6¼ f(RIT) which indicates that the premixed
fraction of NG, fpremix is also at a minimum and NG
stratification is therefore at a maximum. Combustion
transitions to the variable premixed fraction regime
when RIT is reduced below RIT
/C3 = 0 and tNG begins
to increase.24
In Figure 8, X0
fuel for reacting and non-reacting oper-
ation ( X0
fuel and X0
fuel, NR, respectively) are compared to
AHRR for minimally-premixed and variable-premixed
Figure 7. Comparison of non-fired (i.e. NG injection only)
relative equivalence ratio, X0
fuel, NR for all PIDING operating
conditions.
Figure 8. Comparison of AHRR, X0
fuel, and X0
fuel, NR to assess
relative phasing of the start of NG combustion, uSOC, NG and fuel
consumption at the ICOS, uSOC, ICOS (*) for minimally-premixed
(RIT/C3 . 0) and variable premixed fraction ( /C0 1 \ RIT/C3 \ 0)
operating conditions. Ensemble averaged quantities shown.
Rochussen et al. 1901

<!-- PDF_PAGE: 11 -->

fraction operating conditions. For RIT/C3 . 0, X0
fuel
increases in the interval between the pilot AHRR and
the start of the main NG combustion ( uSOC, NG) indicat-
ing some mass of NG penetrates past the pilot ignition
regions and premixes. However, the maximum X
0
fuel is
limited to well below the peak of X0
fuel, NR because a sig-
nificant mass of NG is consumed in non-premixed
combustion prior to reaching the ICOS measurement
volume. For RIT
/C3 \ 0, decreasing RIT/C3 increases tNG
and therefore a greater mass of NG premixes, which is
measured as an increased peak X0
fuel in Figure 8.
The start of premixed NG conversion at the ICOS is
indicated by a sharp drop in X0
fuel, which is denoted
uSOC, ICOS and indicated with an (*) in Figure 8. For all
conditions shown in Figure 8, uSOC, ICOS precedes peak
X0
fuel, NR because tNG is insufficient for the complete
mass of NG to premix (i.e. fpremix \ 100%) for
RIT/C3 . /C0 0:8. For all conditions shown in Figure 8,
X0
fuel diverges from X0
fuel, NR prior to uSOC, ICOS, indicat-
ing some influence of the pilot injection on the NG
concentration measurement. This may be due to pres-
sure and temperature effects on the absorption strength
coefficient (s), pilot injections modifying the fluid mix-
ing field in the combustion chamber, and/or injector
dynamics.
To investigate the spatial distribution of the reaction
zones for minimally-premixed and variable-premixed
fraction PIDING combustion, Figure 9 presents in-
cylinder imaging for /C0 0:8 \ RIT
/C3 \ +0 :8. Images in
Figure 9 present the ensemble averaged images
recorded at 310 nm (OH*-CL) with 700 nm (nominally
PM) images overlaid. The overlay of the 700 nm images
as a hatch is used to indicate that the presence of PM
contributes to significant attenuation of the OH*-CL
signal; locations where there is a strong PM signal, the
local magnitude of the measured OH*-CL intensity
Figure 9. Comparison of ensemble averaged images of OH *-CL (310 nm) and PM (700 nm) with AHRR,
Ð
310 nm, and
Ð
700 nm for
minimally-premixed (RIT/C3 . 0) and variable premixed fraction ( RIT/C3 \ 0) operating conditions. Note all temporal phasing is relative
to uSOC, NG. Shaded regions in AHRR,
Ð
310 nm and
Ð
700 nm indicate cycle to cycle standard deviation of the respective measurement.
1902 International J of Engine Research 24(5)

<!-- PDF_PAGE: 12 -->

cannot be reliably interpreted or compared to other
regions.12,32 The images for each operating condition
are compared to the AHRR, and integrated light inten-
sity (
Ð
310 nm and
Ð
700 nm), which are phased relative
to uSOC, NG. The shaded regions for AHRR, Ð 310 nm,
and Ð 700 nm indicate the standard deviation of the
measurement as a function of crank angle.
The ensemble averaged images in Figure 9 demon-
strate significantly different reaction zone structures for
minimally-premixed ( RIT/C3 . 0) and variable premixed
fraction ( RIT/C3 \ 0) combustion. For RIT/C3 . 0, the
non-premixed NG jet structures are visible in the OH*-
CL from 0 8 /C0 48 after uSOC, NG. The non-premixed com-
bustion results in a strong PM signal developing near
the piston bowl wall after peak AHRR, which agrees
with pyrometric imaging of similar PIDING operating
conditions.
32 For RIT/C3 . 0 in Figure 9, Ð 310 nm
and Ð 700 nm are also very similar in phasing and
magnitude, indicating that the constant tNG for all
minimally-premixed PIDING combustion modes pro-
duces nominally the same main combustion processes.
A significantly different main combustion process is
observed for variable premixed fraction combustion
(RIT
/C3 \ 0 in Figure 9), where fpremix increases with
decreasing RIT/C3 . The increased fpremix reduces the
locally-rich non-premixed combustion, which results in
significantly reduced PM in the images and low
Ð
700
nm for RIT/C3 =/C0 0:3, /C0 0:8. The OH*-CL images
(310 nm) and peak AHRR for RIT/C3 \ 0 indicate that a
more rapid fuel conversion process near the piston bowl
wall becomes dominant as RIT/C3 is reduced from the
minimally-premixed to variable-premixed combustion
regime. At uSOC, NG, the OH*-CL for RIT/C3 \ 0 is signif-
icantly reduced relative to conditions with RIT/C3 . 0,
due to pilot quenching by the NG jets. 24 Despite the
increased tNG for the variable premixed fraction condi-
tions (RIT/C3 \ 0), the OH*-CL in the center of the com-
bustion chamber remains weak throughout the cycle.
This is an indication of the incomplete premixing of the
NG, which is also indicated by X
0
fuel in Figures 7 and 8
for all conditions shown in Figure 9.
In Figure 10, the local reaction zone speed, SRZ,i s
presented to investigate differences in the fuel conver-
sion processes for RIT
/C3 ø /C0 0:8. SRZ is evaluated by
applying a pixel intensity threshold to single-cycle
OH*-CL images of PIDING combustion and measur-
ing the distance between the boundaries of thresholded
images in consecutive frames for every point on the
perimeter of the first thresholded image. This method
has previously been described in detail for characteriza-
tion of flame propagation speeds in premixed dual-fuel
combustion.
40 While SRZ is related to the reaction zone
Figure 10. Distribution of local reaction zone speed, SRZ , presented as a fraction, f (SRZ ), of all local measurements at each recorded
frame. 50th,7 5th, and 90 th percentiles of SRZ shown (SRZ,5 0, SRZ,7 5, SRZ,9 0). Representative single-cycle OH *-CL images (image phasing
indicated by dotted line) with red vectors indicating the measured displacement of reaction zone boundaries used to calculate SRZ .
Rochussen et al. 1903

<!-- PDF_PAGE: 13 -->

growth rate, quantitative analysis of this measurement
is limited by the line-of-sight imaging of OH*-CL used
here.
In Figure 10, the distribution of SRZ is presented as
a probability density of SRZ, f(SRZ) (binned in intervals
of 2 m/s). For each operating condition, a representa-
tive single-cycle OH*-CL image is presented with red
vectors indicating the local S
RZ. For conditions with
RIT/C3 ø /C0 0:3, an early peak in SRZ during pilot igni-
tion (distributed auto-ignition) is followed by a second
larger peak during the main premixed NG combustion
heat release peak. The phasing and magnitudes of the
peaks in S
RZ for RIT/C3 ø /C0 0:3 agree with previous
measurements of PIDING combustion for RIT/C3 . 0.12
However, for RIT/C3 =/C0 0:8 there is only a single peak
in the SRZ. This suggests pilot and NG ignition pro-
cesses occur simultaneously, rather than sequentially.
Despite the significantly higher peak AHRR and
increased fpremix for RIT/C3 =/C0 0:3 compared to
RIT/C3 . 0 (see Figure 8), the peak SRZ in Figure 10 are
very similar for these conditions. The single-cycle OH*-
CL images for RIT
/C3 ø /C0 0:3 show that the larger SRZ
vectors are predominantly oriented radially-outward,
which may indicate that the high SRZ observed during
the premixed NG combustion for RIT/C3 ø /C0 0:3i sg e n -
erated by the NG injection momentum. For
RIT
/C3 =/C0 0:8, a significant increase in the peak SRZ
and more isotropic orientation of the SRZ vectors indi-
cates different processes drive reaction zone growth for
RIT
/C3 =/C0 0:8 compared to RIT/C3 ø /C0 0:3.
Late-cycle stratified-premixed regime
Late-cycle stratified-premixed PIDING combustion is
defined by NG injection impingement within the piston
bowl and the entire mass of NG premixing prior to
ignition (i.e. f
premix = 100%). The exact RIT at which
fpremix = 100% occurs is challenging to directly mea-
sure, however the phasing of peak X0
fuel, NR (Figure 7)
suggests that RIT/C3 ’ /C0 1 (see equation (4)) is a reason-
able estimate. Although fpremix = 100%, late-cycle NG
injections do not produce tNG sufficiently long for a
uniform mixture distribution (i.e. steady state X0
fuel)t o
develop (see Figure 7). It is therefore expected that NG
stratification will be an important factor in the ignition,
main combustion, and emissions performance in the
stratified-premixed combustion regime.
In Figure 11, X
0
fuel and X0
fuel, NR are compared to
AHRR for /C0 2:34RIT4 /C0 0:8. COV of X0
fuel is also
presented in Figure 11 to describe the cyclic variability
of the mixture development processes. For
RIT
/C3 =/C0 0:8, /C0 1:3, uSOC, ICOS precedes peak X0
fuel, NR
indicating pilot ignition is occurring within premixed
NG near the ICOS probe. For RIT/C3 =/C0 0:8, /C0 1:3,
X0
fuel deviates from X0
fuel, NR prior to ignition, which
indicates systematic differences in the NG mixing
processes for the reacting and non-reacting NG injec-
tions. Conversely, for RIT
/C3 =/C0 1:8, /C0 2:3, where the
NG and pilot injections do not overlap (i.e.
SOI
pilot . EOING), the deviation of X0
fuel and X0
fuel, NR
prior to ignition is significantly reduced. This suggests
that the pilot injection impacts the NG mixing pro-
cesses due to injector dynamics and/or in-cylinder mix-
ing processes when pilot and NG injections overlap
temporally.
Increased t
NG for RIT/C3 =/C0 1:8, /C0 2:3 results in
comparatively steady X0
fuel, NR (relative to
RIT/C3 ø /C0 1:3) and low COV( X0
fuel,X0
fuel, NR ) evaluated
at uSOC, NG (COV(X0
fuel)juSOC, NG ). This indicates
decreasing CCV of the NG mixing processes with
increasing t
NG, which was previously observed as
decreasing COV of indicated mean effective pressure
for the same range of RIT
/C3 .24
OH*-CL (310 nm) and PM (700 nm) imaging is com-
pared for RIT/C3 =/C0 0:8, /C0 1:3, /C0 1:8, /C0 2:3 in Figure
12. The AHRR, reaction zone structures (OH*-CL),
and PM structures change significantly between
/C0 1:8 \ RIT \ /C0 1:3 with higher peak AHRR and
Figure 11. Comparison of AHRR, X0
fuel , and COV( X0
fuel, NR )t o
assess relative phasing of uSOC, NG and uSOC, ICOS and the NG
mixture variability for variable premixed fraction
(/C0 14RIT
/C3 \ 0) and stratified-premixed ( RIT/C3 \ /C0 1) operating
conditions. Ensemble averaged quantities shown.
1904 International J of Engine Research 24(5)

<!-- PDF_PAGE: 14 -->

Ð 310 nm for RIT/C3 ø /C0 1:3. For RIT/C3 ø /C0 1:3, the
regions of highest intensity reactions (indicated by
OH*-CL) form a ring around the bowl wall, where pre-
mixed NG combustion has been observed for
minimally-premixed and variable premixed fraction
combustion.
12 With increasing tNG (i.e. increasingly
negative RIT/C3 ) the OH*-CL intensity in this ring
diminishes significantly near peak AHRR (3 8 /C0 68 after
uSOC, NG in Figure 12), which is accompanied by a sig-
nificant decrease of peak AHRR. The decrease in
OH*-CL is most significant between RIT
/C3 =/C0 1:3 and
RIT/C3 =/C0 1:8, which coincides with the RIT/C3 for which
X0
fuel, NR decreases prior to uSOC, ICOS, indicating
increased fuel mixing away from the bowl wall.
In Figure 12, the ensemble averaged images for
u . 38 after uSOC, NG show increasing definition of dis-
tinct reaction zones as RIT/C3 is reduced (i.e. 9 distinct
reaction zones for each NG jet become more clear for
more negative RIT/C3 ). This indicates that there is
lower CCV in the reaction zone structure and location
as t
NG increases for the late-cycle stratified-premixed
regime. This may be a result of the decreasing CCV of
NG mixture formation indicated by decreasing
COV(X0
fuel)juSOC, NG (see Figure 11). The relatively high
variability in the reaction zone structures for
RIT/C3 =/C0 0:8, /C0 1:3 may also be a result of pilot
quenching by the NG jet, which was previously mea-
sured for these conditions.
24
Figure 12. Comparison of ensemble averaged images of OH *-CL (310 nm) and PM (700 nm) with AHRR, Ð 310 nm, andÐ 700 nm
for variable premixed fraction ( /C0 14RIT/C3 \ 0) and late-cycle stratified-premixed fraction ( RIT/C3 \ /C0 1) operating conditions. Note
that all temporal phasing is relative to uSOC, NG. Shaded regions in AHRR, Ð 310 nm andÐ 700 nm indicate cycle to cycle standard
deviation of the respective measurement.
Rochussen et al. 1905

<!-- PDF_PAGE: 15 -->

For all conditions shown in Figure 12, PM indicated
by 700 nm imaging is significantly lower than for the
minimally-premixed conditions shown in Figure 9
(maximum 700 nm signal is a factor of 11 greater in
Figure 9 than in Figure 12). For the late-cycle stratified
conditions shown, the most intense PM is observed
before the peak AHRR (2–3 CAD after u
SOC, NG in
Figure 12). This contrasts observations of non-
premixed and variable premixed fraction combustion
regimes where peak PM results from the main
NG combustion process following peak AHRR (see
Figure 9).
32 For the stratified-premixed conditions, the
peak PM signal is also localized in the 9 pilot ignition
regions, indicating the pilot ignition process is more sig-
nificant for PM production than the premixed NG
combustion process for these operating conditions. For
RIT
/C3 =/C0 0:8 where pilot quenching is most signifi-
cant,24 the initial peak in the
Ð
700 nm is further
reduced, indicating that PM produced in the pilot reac-
tions is mitigated by the quenching.
In Figure 13, the distribution of reaction zone
speeds, S
RZ, is compared for RIT/C3 =/C0 0:8,
/C0 1:3, /C0 1:8, /C0 2:3. For RIT/C3 =/C0 0:8, where there is
measurable quenching of the pilot by the NG jets, 24
there is a single peak in the SRZ distribution. In con-
trast, for RIT/C3 4 /C0 1:3 (no measurable pilot quenching)
there is a peak in SRZ due to pilot auto-ignition fol-
lowed by high SRZ around 2 CAD after uSOC, NG.W i t h
increasing tNG (i.e. decreasing RIT/C3 ), peak AHRR and
peak SRZ after pilot-ignition decrease. This trend of
decreasing SRZ may result from: decreasing local NG
concentration near the bowl wall (where the premixed
combustion tends to be most prominent, see Figure
12), decay of injection-generated turbulence, and/or
reduced entrainment of the reactive pilot fuel from
pilot quenching.
The single-cycle images presented in Figure 13 indi-
cate a significant change in reaction zone structure for
RIT
/C3 ø /C0 1:3 and RIT/C3 4 /C0 1:8. For RIT/C3 =/C0 0:8,
/C0 1:3 premixed NG combustion initiates in a large reac-
tion zone volume located close to the bowl wall (where
X
0
fuel is measured). In contrast, for RIT/C3 =/C0 1:8, /C0 2:3,
EOING is early enough that pilot quenching does not
occur, so pilot reactants remain near the center of the
combustion chamber. Ignition therefore occurs closer
to the center of the chamber and the reaction zone must
propagate outward through more thoroughly premixed
NG.
Early-cycle combustion regimes
With early-cycle SOING, NG jet impingement outside
the piston bowl and long tNG produce more homoge-
neous mixture properties prior to the start of combus-
tion relative to late-cycle combustion regimes. Analysis
of X
0
fuel, NR in Figure 7 indicates that a steady-state NG
Figure 13. Distribution of local reaction zone speed, SRZ , presented as a fraction, f (SRZ ), of all local measurements at each recorded
frame. 50th,7 5th, and 90 th percentiles of SRZ shown (SRZ,5 0, SRZ,7 5, SRZ,9 0). Representative single-cycle OH *-CL images (image phasing
indicated by dotted line) with red vectors indicating the measured displacement of reaction zone boundaries used to calculate SRZ .
1906 International J of Engine Research 24(5)

<!-- PDF_PAGE: 16 -->

concentration distribution is developed by typical CA 50
for RIT4 /C0 538. This coincides with a marked decrease
in the sensitivity of emissions to RIT that was previ-
ously identified at RITinsens: =/C0 538.24 However, for
RIT \ RITinsens: the AHRR shape was still sensitive to
variation of RIT, indicating parameters other than fuel
concentration distribution were significant for combus-
tion processes.
The development of X
0
fuel for early-cycle PIDING
combustion with RIT . RITinsens:, RIT’RITinsens:, and
RIT \ RITinsens: is shown in Figure 14. For
RIT’RITinsens: (RIT =/C0 538), COV( X0
fuel) reaches a
minimum value shortly prior to the start of combustion
(u
SOC, NG), which is approximately equal to the corre-
sponding COV(X0
fuel) for the operating conditions with
much longer tNG (RIT =/C0 958, /C0 1538). This indicates
RITinsens: is a reasonable estimate of the injection phas-
ing required for CCV of the NG mixing processes to
reach steady state prior to combustion.
For RIT. RIT
insens: (RIT=/C0 338), COV(X0
fuel)juSOC, NG
in Figure 14 is relatively high, and unlike all other
operating conditions (both l ate- and early-cycle) is
increasing rather than decreasing prior to the start of
combustion. This unique mixture development beha-
vior for RIT =/C0 338 likely results from impingement
of the NG jet near the piston bowl edge, which causes
a highly variable X
0
fuel and AHRR. Due to the high
CCV of both X0
fuel and AHRR, the ensemble average
of both these quantities is not representative of the
majority of measured cycles.
For all early-cycle operating conditions in Figure 14,
X
0
fuel begins to increase after the combustion event
starting at approximately 20 8 aTDC. This likely indi-
cates significant unburned fuel from quench and crevice
volumes in the combustion chamber entering the ICOS
measurement volume. X0
fuel measured subsequent to the
combustion event (average X0
fuel from 30 to 90 CAD
aTDC), X0
fuel, post, correlates with exhaust CH 4 emis-
sions measured using the thermodynamic engine (see
Appendix C).
24
In Figure 15, SRZ is compared for RIT =/C0 338,
/C0 538, /C0 958, /C0 1538. For RIT4RITinsens:, a common
pattern in the distribution of SRZ is observed: high ini-
tial SRZ during pilot auto-ignition, followed by rela-
tively low SRZ during flame propagation. This behavior
and the magnitude of SRZ is similar to previous mea-
surements of port-injected dual-fuel combustion with
similar f in the same facility. 40 For RIT =/C0 338, the
peak SRZ is retarded and less prominent than for
RIT4RITinsens:. This is a consequence of the high CCV
of combustion phasing for RIT =/C0 338 preventing the
pilot ignition of individual cycles from aligning
temporally.
Despite a significant decrease in peak AHRR for
RIT =/C0 1538 relative to RIT =/C0 958, /C0 538, SRZ
appears very similar for these conditions. This discre-
pancy may be related to non-simultaneous pilot igni-
tion and main combustion processes for RIT =/C0 1538
(i.e. earlier pilot ignition on right side of combustion
chamber, see Appendix D).
Characterization of the spectrum of
premixed NG combustion
In this section, a summary of combustion behavior for
all regimes of PIDING combustion is presented to
characterize the spectrum of stratified PIDING com-
bustion. In Figure 16, metrics characterizing NG mix-
ture development, fuel conversion rate, and in-cylinder
emissions are presented with representative single-cycle
images of OH*-CL (310 nm) and PM (700 nm). NG
mixture development is characterized by X
0
fuel, premix,c a l -
culated as the magnitude of X0
fuel evaluated at the start
of premixed NG combustion ( uSOC, NG). Fuel conver-
sion rate is characterized by the reaction zone growth
rate, S
RZ,9 0. The maximum integrated PM signal from
Figure 14. Comparison of AHRR, X0
fuel , and COV( X0
fuel )t o
assess relative phasing of uSOC, NG and uSOC, ICOS and the NG
mixture variability for early-cycle PIDING combustion
conditions. Ensemble averaged quantities shown.
Rochussen et al. 1907

<!-- PDF_PAGE: 17 -->

700 nm imaging (max( Ð 700 nm)) and X0
fuel measured
after combustion ( X0
fuel, post) are used to characterize in-
cylinder PM and unburned CH 4, respectively.
For minimally-premixed combustion, X0
fuel, premix . 0
indicates that some NG penetrates past the ignition
zones and premixes prior to the start of premixed NG
combustion (u
SOC, NG). The NG injection occurs simul-
taneously to initiation of premixed NG combustion, so
the premixed NG concentration has high cyclic varia-
bility (high COV( X
0
fuel, premix)). NG combustion initiates
in the NG jet and subsequently spreads to the premixed
NG near the bowl wall. 12,31 Unburned CH 4 indicated
by X0
fuel, post is low because NG premixing is limited.
High
Ð
700 nm and 700 nm imaging demonstrates rela-
tively high PM near the bowl wall is generated subse-
quent to non-premixed combustion, which agrees with
previous pyrometric imaging of similar PIDING com-
bustion conditions.
32
When RIT/C3 is reduced from minimally-premixed
conditions past RIT/C3 = 0 to the variable premixed frac-
tion regime, a greater mass of NG premixes (increasing
X
0
fuel, premix) prior to uSOC, NG (Figure 8) and there is a
significant reduction in COV( X0
fuel, premix). This is
accompanied by a moderate increase of X0
fuel, post, which
qualitatively matches an increase of exhaust CH 4 emis-
sions and an order of magnitude drop in in-cylinder
PM ( Ð 700 nm). 24 The transition to the variable
premixed fraction regime is also marked by a signifi-
cant increase in OH*-CL intensity near the piston bowl
wall, however SRZ remains relatively unaffected, likely
because the reaction zone growth rate is dominated by
injection generated turbulence for a given f and charge
temperature (Figure 10).
For RIT previously shown to cause quenching of the
pilot by the NG jets ( /C0 68 \ RIT4 +2 8), premixed NG
combustion initiates over a greater volume close to the
bowl wall, which is unique among all investigated oper-
ating conditions. Conditions with pilot quenching also
feature much higher S
RZ and OH*-CL intensity, which
indicates that a bulk or multi-zone reaction initiation
occurs, rather than OH*-CL being aligned with the
pilot fuel jets, as is characteristic of most PIDING con-
ditions. Pilot quenching also likely contributes to the
lowest in-cylinder PM (Ð 700 nm) of all late-cycle oper-
ating conditions. High S
RZ and distributed reaction
zones are considered likely causes for the high thermal
efficiency observed for the late-cycle stratified-premixed
regime (and DI
2 combustion).16,24
For late-cycle stratified-premixed conditions
(RIT/C3 \ /C0 1), peak AHRR and SRZ reduce with
increasing NG residence time ( tNG) as the
COV(X0
fuel, premix) reduces to a similar level measured for
homogeneously premixed conditions despite much
shorter NG residence time. For RIT/C3 \ /C0 1:3
Figure 15. Distribution of local reaction zone speed, SRZ , presented as a fraction, f (SRZ ), of all local measurements at each recorded
frame. 50th,7 5th, and 90 th percentiles of SRZ shown (SRZ,5 0, SRZ,7 5, SRZ,9 0). Representative single-cycle OH *-CL images (image phasing
indicated by dotted line) with red vectors indicating the measured displacement of reaction zone boundaries used to calculate SRZ .
1908 International J of Engine Research 24(5)

<!-- PDF_PAGE: 18 -->

(RIT \ /C0 68), NG injection is too advanced to quench
the pilot combustion, so distinct pilot reaction zones
are observed in the OH*-CL.
For all operating conditions, COV( X
0
fuel, premix)
decreases with increasing tNG, except for RIT =/C0 338.
This unique NG mixture development behavior for
RIT =/C0 338 is considered a consequence of NG jet
impingement near the piston bowl edge and possibly
the influence of squish flow from piston motion.
This variability results in weak reaction zones (i.e. low
OH*-CL intensity), with irregular structures (high cyc-
lic variability).
A step-change in the behavior of all considered NG
mixing and combustion metrics occurs across the tran-
sition from late-cycle to early-cycle combustion
regimes, where NG jet impingement transitions from
inside the piston bowl (late-cycle) to outside the piston
bowl (early-cycle). Across this transition, the
max(AHRR) and S
RZ,9 0 decrease, and X0
fuel, post
increases significantly, which qualitatively matches the
Figure 16. Overview of the spectrum of PIDING combustion with varying NG premixing. Normalized X0
fuel, premix and
COV(X0
fuel, premix) shown to characterize NG premixing. Normalized SRZ,9 0 shown to characterize fuel conversion rates. Normalized
X0
fuel, post andÐ 700 nm shown to characterize incomplete combustion of CH 4 and in-cylinder PM, respectively. Representative single-
cycle OH*-CL and 700 nm images shown for each regime of PIDING combustion ( RIT = /C0 1538, /C0 338, /C0 148, /C0 68, /C0 28,+ 2 8,
+6 8).
Rochussen et al. 1909

<!-- PDF_PAGE: 19 -->

observed increase of exhaust CH 4 emissions for early-
cycle PIDING relative to late-cycle. 24 Premixed NG
near the bowl wall is consumed much later for early-
cycle conditions relative to late-cycle conditions due to
slower reaction zone propagation (i.e. lower S
RZ).
Early-cycle PIDING combustion is similar to port-
injected dual-fuel combustion, except that flame speed
(and therefore efficiency) is a function of the RIT, with
greater flame speeds achieved with later SOI
NG.
Conclusions
In-cylinder imaging of OH*-CL (310 nm) and PM
(700 nm) was performed for 11 PIDING operating con-
ditions, representing 5 regimes of stratified PIDING
combustion previously identified based on AHRR and
emissions behavior.
24 To support in-cylinder imaging,
local measurement of relative molar fuel concentration
was performed for reacting and non-reacting engine
operation to characterize gaseous fuel mixing evolu-
tion. The objectives of this investigation were to: (i)
support and refine the previously identified regimes of
PIDING combustion and critical injection phasings
and (ii) describe the in-cylinder mixing process of direct
injected gaseous fuel and its impacts on combustion
and in-cylinder pollutant formation processes. Detailed
descriptions of the in-cylinder processes of each regime
are given in x4.
The in-cylinder imaging and relative fuel concentra-
tion measurements provided an improved understand-
ing all PIDING combustion regimes and critical
injection phasings ( RIT
premix, SOING, trans, RIT/C3 =/C0 1,
and RIT/C3 = 0):
1. RITpremix: Measurement of premixed NG concen-
tration at the bowl wall in non-fired experiments
indicates that an approximately homogeneous
fuel-air mixture is reached 12 ms after EOI
NG,
which corresponds to the NG residence time of
RIT
premix. Thus, for RIT \ RITpremix, the emissions
are less sensitive to RIT as the mixture is homoge-
neous. Further, this validates the previously pro-
posed approach for metal engines, in which the
sensitivity of CO and CH
4 to RIT are used to iden-
tify a homogeneous charge.
2. SOING, trans: When SOING is advanced past
SOING, trans, the premixed fuel concentration near
the bowl wall undergoes a step decrease in magni-
tude and a step increase in cyclic variability.
Imaging results also show high cyclic variability in
the reaction zone structures. This demonstrates
that adverse mixing occurring when the NG jets
align with the piston bowl corner at SOI
NG is the
cause for the rapid deterioration of combustion
and emissions performance observed in metal
engine experiments. To improve stratified-
premixed PIDING combustion, gaseous fuel injec-
tion angle and piston bowl geometry (which define
SOI
NG, trans) should be designed to advance
SOING, trans as much as possible.
3. RIT/C3 : With decreasing RIT from minimally-
premixed PIDING operation, the magnitude of
the premixed NG concentration near the bowl wall
begins to increase at RIT
/C3 = 0 and reaches a maxi-
mum value at approximately RIT/C3 =/C0 1. This
indicates that RIT/C3 (calculated using metal engine
measurements) is an appropriate metric to qualita-
tively characterize the premixed NG fraction,
f
premix. These observations also strengthen
RIT/C3 =/C0 1 and RIT/C3 = 0 as valid boundaries
between the stratified-premixed, variable-premixed
fraction, and minimally-premixed PIDING com-
bustion regimes.
Several important features of direct-injected gaseous
fuel mixing and the corresponding implications for
combustion performance and in-cylinder pollutant for-
mation have been identified:
1. NG mixture evolution: Regardless of the operating
condition or RIT, NG premixing takes place near
the piston bowl wall prior to ignition, including
operation where the gaseous fuel is injected after
the pilot combustion. The evolution of premixed
NG concentration near the bowl wall is sensitive
to RIT and does not develop monotonically with
increasing NG residence time. For late-cycle oper-
ation, when SOI
pilot is before EOING, the NG pre-
mixing processes near the piston bowl wall are
additionally influenced by the pilot injection.
2. High indicated efficiency combustion: Very short
combustion durations in the variable-premixed
and stratified-premixed (late-cycle) PIDING com-
bustion regimes (SPC 13 and DI216,17 elsewhere) is
likely due to very rapid reaction zone growth rates
( . 45 m/s) driven by high injection generated tur-
bulence shortly after EOING. When pilot and NG
injections overlap, the pilot combustion is (par-
tially) quenched. This results in more premixing,
more uniformly distributed early reaction zones
(possible multi-point ignition), and even higher
reaction zone growth and heat release rates. For
these operating conditions, the highest intensity
combustion occurs near the piston bowl wall,
which may mitigate wall quenching and CH
4 emis-
sions; this is a recommended area of focus for
future investigation.
3. Early-cycle PIDING combustion: For
homogeneously-premixed PIDING combustion,
flame propagation speeds decrease from approxi-
mately 15 to 10 m/s as SOI
NG is advanced from
2528 to /C0 1718 aTDC. This results in increased
combustion durations and reduced indicated effi-
ciency observed in metal engine experiments. The
role of injection-generated turbulence is recom-
mended as an area to be investigated further for
1910 International J of Engine Research 24(5)

<!-- PDF_PAGE: 20 -->

high efficiency fully-premixed direct-injected NG
combustion.
This investigation has validated the previously iden-
tified regimes of PIDING combustion and has aug-
mented them with description of the in-cylinder NG
mixture development and its impacts on combustion
and pollutant formation processes. Further investiga-
tion of NG mixing, pilot-NG interactions, and the
implementation of numerical modeling of stratified-
premixed PIDING combustion is needed to further
support and extend the conclusions presented in the
current work. These results, combined with recom-
mended future areas of research offer significant
opportunity for developing higher-efficiency gaseous
fuel direct-injection combustion strategies with low pol-
lutant emissions.
Acknowledgements
The authors would like to acknowledge the technical and
financial support provided by Westport Fuel Systems, Inc.
The technical support and contributions of Drs. Sandeep
Munshi, Gord Mc-Taggart Cowan, Steve Rogak, and Jim
Huang. The technical contributions of fellow researchers at
The University of British Columbia’s Clean Energy Research
Centre are also gratefully acknowledged.
Declaration of conflicting interests
The author(s) declared no potential conflicts of interest with
respect to the research, authorship, and/or publication of this
article.
Funding
The author(s) disclosed receipt of the following financial sup-
port for the research, authorship, and/or publication of this
article: This work was supported by the Natural Sciences and
Engineering Research Council of Canada (NSERC)
Collaborative Research and Development (CRD) grants
(CRDPJ 451208-13 and 530547-18) in conjunction with
Westport Fuel Systems, the Canadian Foundation for
Innovation (CFI) John Evans Leaders Fund (JELF) grant
(no. 32637), the NSERC Discovery Grant Program (RGPIN
418700-13).
ORCID iDs
Jeremy Rochussen https://orcid.org/0000-0002-7098-2340
Matthew Knight https://orcid.org/0000-0001-5747-8775
Gibson Clark https://orcid.org/0000-0002-5033-0919
Patrick Kirchen https://orcid.org/0000-0002-1154-8923
References
1. Teter J, Cazzola P and Gu ¨lT . The future of trucks . Paris:
International Energy Agency, 2017.
2. IEA. World Energy Outlook 2019 . Paris: International
Energy Agency, 2019.
3. Gross S. The challenge of decarbonizing heavy transport .
Washington: Brookings Institute, 2020.
4. Intergovernmental Panel on Climate Change. AR5 Cli-
mate Change 2014: Mitigation of Climate Change: Work-
ing Group III Contribution to the IPCC Fifth Assessment
Report. Cambridge: Cambridge University Press, 2015.
5. Ouellette P, Goudie D and McTaggart-Cowan G. Prog-
ress in the development of natural gas high pressure
direct injection for Euro VI heavy-duty trucks. In: Liebl
J and Beidl C (eds) Internationaler Motorenkongress .
Wiesbaden: Springer, 2016, pp.591–607.
6. Harrington J, Munshi S, Nedelcu C, Ouellette P, Thomp-
son J and Whitfield S. Direct injection of natural gas in a
heavy-duty diesel engine. SAE technical paper 2002-01-
1630, 2002.
7. Besch MC, Israel J, Thiruvengadam A, Kappanna H
and Carder D. Emissions characterization from different
technology heavy-duty engines retrofitted for CNG/die-
sel dual-fuel operation. SAE Int J Engines 2015; 8: 1342–
1358.
8. Stettler ME, Midgley WJ, Swanson JJ, Cebon D and
Boies AM. Greenhouse gas and noxious emissions from
dual fuel diesel and natural gas heavy goods vehicles.
Environ Sci Technol 2016; 50: 2018–2026.
9. Yousefi A, Guo H and Birouk M. An experimental and
numerical study on diesel injection split of a natural gas/
diesel dual-fuel engine at a low engine load. Fuel 2018;
212: 332–346.
10. Yousefi A, Guo H, Dev S, Liko B and Lafrance S. Effect
of pre-main-post diesel injection strategy on greenhouse
gas and nitrogen oxide emissions of natural gas/diesel
dual-fuel engine at high load conditions. Fuel 2021; 302:
121110.
11. McTaggart-Cowan G. Pollutant formation in a gaseous-
fuelled, direct injection engine . Vancouver, BC: University
of British Columbia, 2006.
12. Rochussen J, McTaggart-Cowan G and Kirchen P. Para-
metric study of pilot-ignited direct-injection natural gas
combustion in an optically accessible heavy-duty engine.
Int J Engine Res 2020; 21: 497–513.
13. Faghani E, Kheirkhah P, Mabson C, McTaggart-Cowan
G, Kirchen P and Rogak S. Effect of Injection Strategies
on Emissions from a Pilot-Ignited Direct-Injection Natu-
ral-Gas Engine-Part II: Slightly Premixed Combustion.
SAE technical paper 2017-01-0763, 2017.
14. McTaggart-Cowan G, Bushe WK, Rogak SN, Hill PG
and Munshi SR. Injection parameter effects on a direct
injected, pilot ignited, heavy duty natural gas engine with
EGR. SAE technical paper 2003-01-3089, 2003.
15. McTaggart-Cowan G, Bushe W, Rogak S, Hill P and
Munshi S. PM and NOx reduction by injection parameter
alterations in a direct injected, pilot ignited, heavy duty
natural gas engine with EGR at various operating condi-
tions. SAE technical paper 2005-01-1733, 2005.
16. Florea R, Neely G, Miwa J and Abidin Z. Efficiency and
emissions characteristics of partially premixed dual-fuel
combustion by co-direct injection of NG and diesel fuel
(DI
2 ). SAE technical paper 2016-01-0779, 2016.
17. Neely G, Florea R, Miwa J and Abidin Z. Efficiency and
emissions characteristics of partially premixed dual-fuel
combustion by co-direct injection of NG and diesel fuel
(DI
2 ) - Part 2. SAE, 2017.
18. Li M, Zheng X, Zhang Q, Li Z, Shen B and Liu X. The
effects of partially premixed combustion mode on the per-
formance and emissions of a direct injection natural gas
engine. Fuel 2019; 250: 218–234.
Rochussen et al. 1911

<!-- PDF_PAGE: 21 -->

19. Munshi S, McTaggart-Cowan G, Huang J and Hill P.
Development of a partially-premixed combustion strategy
for a low-emission, direct injection high efficiency natural
gas engine. In: Proceedings of the AMSE 2011 internal
combustion engine division fall technical conference, 2011.
20. Kim T, Song J and Park S. Effects of turbulence enhance-
ment on combustion process using a double injection
strategy in direct-injection spark-ignition (DISI) gasoline
engines. Int J Heat Fluid Flow 2015; 56: 124–136.
21. Chiodi M, Berner H and Bargende M. Investigation on
different injection strategies in a direct-injected turbo-
charged CNG-engine. SAE technical paper 2006-01-3000,
2006.
22. Zoldak P and Naber J. Spark ignited direct injection nat-
ural gas combustion in a heavy duty single cylinder test
engine-start of injection and spark timing effects. SAE
technical paper 2015-01-2808, 2015.
23. Fink G, Jud M and Sattelmayer T. Fundamental study of
diesel-piloted natural gas direct injection under different
operating conditions. J Eng Gas Turbine Power 2019; 141:
071013.
24. Rochussen J, McTaggart-Cowan G and Kirchen P. Heat
release rate and emissions regimes of stratified pilot-
ignited direct-injection natural gas combustion. Int J
Engine Res . Epub ahead of print 15 September 2021.
DOI: 10.1177/14680874211046912
25. Faghani E, Kirchen P and Rogak S. Application of fuel
momentum measurement device for direct injection natu-
ral gas engines. SAE technical paper 2015-01-0915, 2015.
26. Rochussen J. Characterizing regimes of stratified pilot-
ignited direct-injection natural gas combustion in an
optically-accessible engine. Vancouver, BC: University of
British Columbia, 2021.
27. Zoldak P, Sobiesiak A, Wickman D and Bergin M. Com-
bustion simulation of dual fuel CNG engine using direct
injection of natural gas and diesel. SAE Int J Engines
2015; 8: 846–858.
28. Karim GA. Combustion in gas fueled compression igni-
tion engines of the dual fuel type. J Eng Gas Turbine
Power 2003; 125: 827–836.
29. Gleis S, Frankl S, Waligorski D, Prager I and Wachtmeis-
ter I. Investigation of the high-pressure-dual-fuel (HPDF)
combustion process of natural gas on a fully optically
accessible research engine. SAE technical paper 2019-01-
2172, 2019.
30. Frankl S, Gleis S and Wachtmeister G. Interpretation of
ignition and combustion in a full-optical High-Pressure-
Dual-Fuel (HPDF) engine using 3D-CFD methods. In:
CIMAC CONGRESS 19, 29th CIMAC world congress on
combustion engine, meeting the future of combustion
engines, Vancouver, BC, 10–14 June 2019.
31. Hatzipanagiotou A, Marko F, Koenig G, Krueger C,
Wenzel P and Koch T. Numerical and optical analysis of
heterogeneous gas combustion with diesel pilot ignition
in a commercial vehicle engine. Int J Engine Res 2018; 19:
109–119.
32. Khosravi M, McTaggart-Cowan G and Kirchen P. Pyro-
metric imaging of soot processes in a pilot ignited direct
injected natural gas engine. Int J Engine Res 2021; 22:
1605–1623.
33. Ishibashi R and Tsuru D. An optical investigation of
combustion process of a direct high-pressure injection of
natural gas. J Mar Sci Technol 2017; 22: 447–458.
34. Fink G, Jud M and Sattelmayer T. Influence of the spa-
tial and temporal interaction between diesel pilot and
directly injected natural gas jet on ignition and combus-
tion characteristics. J Eng Gas Turbine Power 2018; 140:
102811-1–102811-8.
35. McTaggart-Cowan GP, Rogak SN, Munshi SR, Hill PG
and Bushe WK. The influence of fuel composition on a
heavy-duty, natural-gas direct-injection engine. Fuel
2010; 89: 752–759.
36. McTaggart-Cowan G, Huang J and Munshi S. Impacts
and mitigation of varying fuel composition in a natural
gas heavy-duty engine. SAE Int J Engines 2017; 10: 1506–
1517.
37. Gaydon A. The spectroscopy of flames . London: Chap-
man & Hall, 2012.
38. Grosch A, Beushausen V, Thiele O and Grzeszik R.
Crank angle resolved determination of fuel concentration
and air/fuel ratio in a SI-internal combustion engine
using a modified optical spark plug. SAE technical paper
2007-01-0644, 2007.
39. Yeo J, Rochussen J and Kirchen P. Application of an in-
cylinder local infrared absorption fuel concentration sen-
sor in a diesel-ignited dual-fuel engine. SAE technical
paper 2016-01-2310, 2016.
40. Rochussen J and Kirchen P. Characterization of reaction
zone growth in an optically accessible heavy-duty diesel/
methane dual-fuel engine. Int J Engine Res 2019; 20: 483–
500.
41. Nori V and Seitzman J. Evaluation of chemiluminescence
as a combustion diagnostic under varying operating con-
ditions. In: 46th AIAA aerospace sciences meeting and
exhibit, 7–10 January 2008, Reno, Nevada, p.953.
Appendix A
Calculation of X’fuel
To characterize the fuel-air mixture development the
LaVision Internal Combustion Optical Sensor (ICOS)
was implemented. The development and theory of the
ICOS is described in detail elsewhere,
38 and implemen-
tation of this instrument in the current experimental
facility is described in previous work. 39 The ICOS mea-
sures absorption of light sent via fiber optic cable from
a quartz-tungsten-halogen lamp to a 20 mm
3 measure-
ment volume protruding from the cylinder head. Light
introduced to the measurement volume is reflected by a
mirrored surface, transmitted back to a second fiber
optic cable and 3.4 m m narrow band-pass filter before
reaching the detector. This absorption band measures
the C-H vibrational band, characteristic of hydrocar-
bon fuels, and is related to the fuel molar concentration
within the measurement volume using the Beer-
Lambert law:
Nfuel =/C0
ln ( I
I0
)
L /C1 s ðA:1Þ
where I is the light intensity measured by the detector,
I0 is the measured light intensity with no fuel present
(measured as the average I from 22008 to 21808 aTDC
1912 International J of Engine Research 24(5)

<!-- PDF_PAGE: 22 -->

for every cycle), s is the absorption strength coefficient
(species-specific), and L is the absorption path length.
To account for broadband IR emission from hot
combustion chamber surfaces, an optical chopper mod-
ulates the light source at 30 kHz. Thus, the measured
intensity, I (equation (A.1)) is the difference between
the transmitted intensity with the light on, and the
recorded intensity with the light off ( I = I
on /C0 Ioff). The
fuel mole fraction, Xfuel, in the ICOS measurement vol-
ume is given by:
Xfuel(u)= Nfuel(u)
Ntot, u(u) ðA:2Þ
where Ntot, u is the total molar concentration (including
all species) of the unburned mixture in the cylinder, and
is assumed to be the same as the mixture within the
ICOS measurement volume. Ntot, u varies throughout a
cycle due to: (i) the changing cylinder volume, Vcyl and
(ii) compression of unburned gases by the expanding
burned gases following ignition. Assuming ideal gas
behavior, N
tot, u can be calculated as:
Ntot, u(u)=
P ni
Vcyl(u) = ntot
Vcyl(u) = P(u)
R /C1 Tu(u) ðA:3Þ
where ni and ntot are the number of mols of the ith and
of all species, respectively. P is the measured cylinder
pressure, R is the universal gas constant, and Tu is the
unburned gas temperature. Tu is estimated by assuming
isentropic compression of the unburned gases by the
cylinder volume change and burned gas expansion,
using the relation:
Tu(u)= Tref /C1 P(u)
Pref
/C18/C19 g/C0 1
g
ðA:4Þ
where g =1 :36, and Pref and Tref are evaluated at 2170
CAD aTDC and assumed to be the same as the mea-
sured inlet manifold conditions at 2170 CAD aTDC.
When equations (A.1)–(A.4) are combined, the follow-
ing expression for X
0
fuel is obtained:
X0
fuel(u)= /C0 R
L /C1 s
/C18/C19
/C1 Tref
Pref
g/C0 1
g
 !
/C1
In I uðÞ
Io
/C16/C17
P uðÞ
1
g
0
@
1
A ðA:5Þ
The calculation of Ntot, u considers the unburned gas
temperature, Tu (equation (A.4)) and is not valid when
the ICOS measurement volume contains the burned
gases or reacting mixture (i.e. during and after the oxi-
dation of fuel in the ICOS measurement volume). A
sharp drop in N
fuel (i.e. drop in fuel concentration) pro-
vides clear indication of the crank angle phasing when
the fuel in the ICOS measurement volume is oxidized
and therefore the limit of where X
0
fuel as described above
can be applied.
In future work, the spectral, temperature, and pres-
sure sensitivities of s will be considered to provide
quantitative assessment of Xfuel. In the current work
however, qualitative comparisons of X0
fuel are made so
s can be assumed constant and combined with other
parameters into a proportionality constant. This results
in the following form of X
0
fuel:
X0
fuel(u)a
In I uðÞ
Io
/C16/C17
P uðÞ
1
g
0
@
1
A ðA:6Þ
Appendix B
Analysis of OH*-Chemiluminescence
Analysis of OH*-CL must consider the mechanisms
leading to OH radical production and chemilumines-
cence as well as the impact of combustion chamber con-
ditions on OH*-CL. The formation of the OH* radical
is considered to primarily occur via two reactions
41:
CH + O2 /C0 . OH/C3 +C O ðR1Þ
H+O+M /C0 . OH/C3 +M ðR2Þ
The OH*-CL intensity is sensitive to pressure, f, and
temperature for CH 4 flames at relevant cylinder condi-
tions (increasing OH*-CL intensity with decreasing
pressure, increasing f, or increasing T) and is com-
monly used as a measure of local heat release in pre-
mixed flames (i.e. R1).
31,41 OH*-CL is also emitted
from the burned gas regions due to the recombination
of H and O atoms at elevated temperatures, particu-
larly for lean combustion where there is a higher con-
centration of O in the combustion products (R2).
41 The
presence of PM has been shown to significantly attenu-
ate OH*-CL, which must be considered when interpret-
ing OH*-CL for non-premixed combustion systems.
32
Appendix C
Comparison of CH4 Emissions and X’fuel, post
To characterize unburned CH 4 due to incomplete com-
bustion, local measurement of X0
fuel following combus-
tion, X0
fuel, post, is compared to exhaust emissions of CH 4
in Figure A1. The calculation of X0
fuel presented in this
work (equations (A.1)–(A.5)) used the properties of the
unburned gases to estimate the total molar concentra-
tion in the cylinder, N
tot, u (equation (A.3)). To calcu-
late X0
fuel, post, the burned gas properties are assumed to
be representative of the entire charge (i.e. a single ther-
modynamic zone) and are used to estimate N
tot, b:
Ntot, b = ntot
V(u) = mcyl
fMex /C1 V(u)
= (mair + mNG + mdiesel)
fMex /C1 V(u)
ðA:7Þ
where the molar mass, fMex, is estimated assuming
complete combustion of the reactants. X0
fuel is then cal-
culated as previously described (equation (A.2)), using
equation (A.7) for N
tot, b. X0
fuel, post is calculated as the
average of X0
fuel over the interval of u = ½30, 90/C138 CAD
aTDC. Exhaust emissions were measured in a previous
Rochussen et al. 1913

<!-- PDF_PAGE: 23 -->

investigation of the same operating conditions using
the thermodynamic configuration of the engine facility
applied in the current work. 24 Note that due to the sig-
nificant increase in CH 4 emissions for early-cycle
regimes relative to late-cycle regimes, a log scale is used
for the CH 4 emissions axis to improve legibility.
Appendix D
Early-cycle combustion imaging
In Figure A2 ensemble averaged images of OH*-CL
are compared for all early-cycle combustion modes
(note PM and
Ð
700 nm not shown due to low PM sig-
nal for early-cycle operating conditions). The reaction
zone structure and AHRR for RIT . RIT
insens: is
unique compared to other conditions shown with
RIT4RITinsens:. Following pilot ignition, OH*-CL
images for RIT =/C0 338 in Figure A2 ( uø 68 after
uSOC, NG) show the pilot reaction zones merging in the
center of the combustion chamber. Despite high CCV
of RIT =/C0 338, single-cycle images indicate similar
reaction zone structures to the ensemble average (e.g.
see Figure 15).
Figure A1. Correlation of post combustion CH 4
concentration measured in-cylinder ( X0
fuel, post, see Appendix C)
with exhaust emissions of unburned CH 4 measured using
thermodynamic engine configuration. 24
Figure A2. Comparison of ensemble averaged images of OH *-CL (310 nm) with AHRR and
Ð
310 nm for early-cycle PIDING
combustion conditions. Note that all temporal phasing is relative to uSOC, NG.
1914 International J of Engine Research 24(5)

<!-- PDF_PAGE: 24 -->

For RIT4RITinsens:, a long delay between ignition
(indicated by AHRR) and premixed NG combustion
near the bowl wall (measured by the ICOS) demon-
strates a relatively slow flame propagation process. The
AHRR and
Ð
310 nm indicate very similar combustion
for RIT =/C0 538,/C0 958, but the magnitude of both
decrease significantly for RIT =/C0 1538 where systema-
tic asymmetries in the combustion process become
prominent.
For RIT =/C0 1538, pilot auto-ignition starts earlier
for reaction zones on the right side of the chamber (see
18 /C0 38 after u
SOC, NG in Figure A2), followed by higher
OH*-CL intensity for reaction zones on the left side of
the combustion chamber during main combustion.
While the combustion chamber itself is asymmetric
(e.g. intake and exhaust valves on the left side of the
combustion chamber, see Figure 5), the reason ignition
and main combustion are more sensitive to these asym-
metries for RIT =/C0 1538 remains an open question.
Notation
T erm Description
g Ratio of specific heats
hi, g Indicated gross thermal efficiency
u Crank angle
uSOC, NG Crank angle phasing of the start of NG combustion
uSOC, ICOS Crank angle phasing when the ICOS detects fuel
consumption
s Radiative absorption strength coefficient
tNG NG premixing time (in cylinder prior to
combustion)
tinj, NG NG injection duration
f Equivalence ratio
AHRR Apparent heat release rate
aTDC After top dead center
C
fuel Local molar fuel concentration
CA50 Phasing of 50% indicate heat release
CAD Crank angle degree
CCV Cycle-to-cycle variability
DI
2 Co-direct injection
DISI Direct-injection spark-ignition
DLSR Dome-loaded self-relieving regulator
ECU Engine control unit
EOING NG end of injection
fpremix Fraction of NG that premixes prior to
combustion
(continued)
(Continued)
T erm Description
GHG Greenhouse gas
HPDI High-pressure direct-injection
I Light intensity measured by ICOS
ICOS LaVision in-cylinder optical sensor
IR Infrared
L ICOS absorption optical path length
m
air Mass of air in cylinder charge
mcyl Mass of cylinder charge
mdiesel Mass of diesel in cylinder charge
mNG Mass of NG in cylinder charge
eMex Molar mass of burned gases
Nfuel Molar concentration of fuel in cylinder
Ntot, b Molar concentration of cylinder burned gases
Ntot, u Molar concentration of cylinder unburned gases
NG Natural gas
OH*-CL OH *-chemiluminescence
P
cyl Cylinder pressure
Ppeg Pegging pressure at intake manifold
PIDING Pilot-ignited direct-injection natural gas
PM Particulate matter
R Universal gas constant
RCEM Rapid compression/expansion machine
RIT Relative injection timing
RIT
/C3 Scaled RIT
RITcrit RIT distinguishing minimally-premixed PIDING
combustion
RITinsens: Largest RIT at which emissions show strong
sensitivity to RIT
RoPR Rate of pressure rise
SOING NG start of injection
SOING, trans NGSOI where NG orifice aligns with piston bowl
corner
SOIpilot Pilot start of injection
SPC Slightly premixed combustion
Tpeg Pegging temperature at intake manifold
TDC T op dead center
TKE T urbulent kinetic energy
uHC Unburned hydrocarbon
V Cylinder volume
WFS Westport fuel systems
X
0
fuel Relative fuel molar concentration (fired operation)
X0
fuel, NR Relative fuel molar concentration (non-reacting
operation)
X0
fuel, post Average X0
fuel measured over u = ½ +3 08,+ 9 08/C138
aTDC
X0
fuel, premix X0
fuel measured at uSOC, NG
Rochussen et al. 1915
