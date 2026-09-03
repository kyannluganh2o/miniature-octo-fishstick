<!-- PDF_PAGE: 1 -->

Standard Article
International J of Engine Research
2023, V ol. 24(2) 265–285
/C211IMechE 2021
Article reuse guidelines:
sagepub.com/journals-permissions
DOI: 10.1177/14680874211046912
journals.sagepub.com/home/jer
Heat release rate and emissions
regimes of stratified pilot-ignited
direct-injection natural gas combustion
Jeremy Rochussen1 , Gordon McT aggart-Cowan2 and
Patrick Kirchen1
Abstract
Natural gas (NG) is an attractive fuel for heavy-duty internal combustion engines because of its potential for reduced
CO2, particulate, and NO X emissions and lower cost of ownership. Pilot-ignited direct-injected NG (PIDING) combus-
tion uses a small pilot injection of diesel to ignite a main direct injection of NG. Recent studies have demonstrated that
increased NG premixing is a viable strategy to increase PIDING indicated efficiency and further reduce particulate and
CO emissions while maintaining low CH
4 emissions. However , it is unclear how the combustion strategies relate to one
another , or where they fit within the continuum of NG stratification. The objective of this work is to present a systema-
tic evaluation of pilot combustion, NG combustion, and emissions behavior of stratified-premixed PIDING combustion
modes that span from fully-premixed to non-premixed conditions. A sweep of the relative injection timing, RIT,o fN G
and pilot diesel was performed in a heavy-duty PIDING engine with P
inj = 140–220 bar ,fg = 0.47–0.71, and a constant
NG energy fraction of 94%. Apparent heat release rate and emissions analyses identified interactions between the pilot
fuel and NG, and qualitatively characterized the impact of NG stratification on combustion and emissions. Changes in
the RIT resulted in six distinct PIDING combustion regimes, for all considered injection pressures and equivalence
ratios: (i) RIT -insensitive premixed, (ii) stratified-premixed (early-cycle injection), (iii) NG jet impingement transition, (iv)
stratified-premixed (late-cycle injection), (v) variable premixed fraction, and (vi) minimally-premixed. Parametric defini-
tions for the bounds of each regime of combustion were valid for the wide range of P
inj and fg investigated, and are
expected to be relevant for other PIDING engines, as previously identified regimes agree with those identified here.
This conceptual framework encompasses and validates the findings of previous stratified PIDING investigations, including
optimal ranges of operation that provide significantly increased efficiency and lower emissions of incomplete combustion
products.
Keywords
Natural gas, direct-injection, partially-premixed, pilot-ignited, injection timing, stratified, non-premixed
Date received: 22 April 2021; accepted: 30 August 2021
Introduction
The transportation sector accounts for 28% of global
end-user energy consumption, of which on-road heavy-
duty vehicles (HDVs) are responsible for one quarter
of green house gas (GHG) emissions.
1 Moreover, by
the year 2030, on-road freight activity is forecasted to
grow 25%.
2 Filling these transportation needs while
simultaneously reducing GHG emissions is critical and
will require implementation of advanced propulsion
technologies with a high level of technical readiness.
One approach to reduce GHG emissions is through
fuel carbon intensity reduction by implementing fuels
that inherently produce less CO
2 in combustion.
Natural gas (NG) is composed primarily of CH 4 which
can result in up to 25% lower CO 2 emissions compared
to conventional fossil fuels such as diesel. NG has also
demonstrated the potential to reduce other harmful
emissions such as particulate matter (PM) and NO
X in
commercial HDV applications. 3,4 Life-cycle analysis
1The University of British Columbia, Vancouver , BC, Canada
2Simon Fraser University, Surrey, BC, Canada
Corresponding author:
Jeremy Rochussen, The University of British Columbia, 2054-6250
Applied Science Lane, Vancouver , BC V6T1Z4, Canada.
Email: jrochussen@mech.ubc.ca

<!-- PDF_PAGE: 2 -->

suggests a net reduction of GHG emissions of 10%–
15% is realistic for HDVs where diesel is replaced by
NG.1 Spark-ignition (SI) and pilot-ignition (PI) of
fumigated (i.e. homogeneously premixed) NG are rela-
tively simple strategies for heavy-duty NG engines,
however they suffer from low thermal efficiency, h, and
high unburned hydrocarbon (uHC) emissions relative
to direct-injection technologies, particularly at low
load.5 Because CH 4 is a potent GHG, 1 emissions of
uHCs from NG engines can result in net increases of
GHG emissions when conventional diesel applications
are converted to NG. 6,7 Four major sources of uHC
emission from premixed engines are commonly identi-
fied: (i) crevice volume quenching, (ii) slow flame
extinction, (iii) wall quenching, and (iv) direct blow-
through due to valve overlap.
8,9 The most significant of
these sources are crevice volume quenching and slow
flame extinction, which are effectively addressed by
using direct-injection (DI).
9
Pilot-ignited direct-injection NG combustion
(PIDING) uses a late-cycle pilot injection of diesel
(approximately 5% of total fuel energy) followed by a
main injection of NG which reacts predominantly in
non-premixed combustion. Pilot-ignition provides
robust, multi-point ignition of the NG, overcoming the
issues of weak early-flame development and high cycle-
to-cycle variability (CCV), which limits direct-injection
SI (DISI) technology.
10 Non-premixed PIDING com-
bustion allows for higher compression ratios, providing
high efficiency and low uHC emissions at the cost of
increased PM and NO X emissions relative to fumigated
systems.3,11 While the main PIDING combustion
process is typically characterized as non-premixed com-
bustion, a portion of the NG reacts in a rapid partially-
premixed mode in parallel to establishment of a
quasi-steady jet flame. 12 The fraction of fuel converted
in the partially-premixed fraction is predominantly
controlled by the relative injection timing ( RIT) of the
NG with respect to the pilot, defined here as:
RIT = SOING /C0 SOIpilot ð1Þ
where SOING and SOIpilot are the start of injection of
NG and the diesel pilot, respectively.
In conventional PIDING operation, pilot auto-
ignition is typically complete prior to the injection of
NG, requiring RIT /C29 0. This minimizes the residence
time of NG prior to the start of the partially-premixed
NG combustion. However, several investigations have
demonstrated that significant advantages in emissions
and efficiency can be achieved by increasing the NG
residence time and promoting more premixed combus-
tion by reducing the RIT to negative values. To this
end, two general approaches have been considered: (i)
slightly premixed combustion (SPC) modes using mod-
erate reduction of RIT from conventional non-
premixed PIDING values (e.g. Faghani et al.,
13
McTaggart-Cowan et al. 14,15), and (ii) stratified-
premixed PIDING modes where one or more NG
injections are performed during the compression stroke
to generate highly premixed conditions (e.g. Florea
et al., 16,17 Li et al. 18). For both these strategies, late-
cycle SOIpilot is used for fast-response combustion
phasing control.
SPC was studied by Faghani et al. 13 with
22m s \ RIT \+ 2 ms by retarding the SOIpilot (oper-
ating conditions with RIT \ 0 were designated SPC
modes). For an optimized SPC mode, a 90% reduction
in PM and a 2% increase of gross indicated efficiency,
h
i, g, were measured relative to a conventional high-
load PIDING operating condition without significant
NOX or CH 4 emissions penalties. The decreased PM
emissions were attributed to the increased NG resi-
dence time prior to NG ignition resulting in a reduction
of the mass of NG with equivalence ratio, f, in the PM
formation region (2 \ f \ 5). The reduced PM forma-
tion was experimentally validated by in-cylinder 2D
pyrometric imaging, which showed a lower peak soot
volume fraction as the RIT was reduced to SPC condi-
tions.
19 In earlier studies, increased efficiency and
reduction of CO and PM was also observed for similar
SPC operating conditions, which were attributed to
higher peak apparent heat release rate (AHRR) and
reduced combustion duration for SPC modes.
14,15 In
all of these studies, exhaust gas re-circulation (EGR)
was required to mitigate NO
X emissions for SPC
modes. The major drawbacks of the SPC mode were
indicated to be increased CCV (measured as COV of
peak cylinder pressure, P
cyl) and greater combustion
harshness measured by the maximum rate of pressure
rise (RoPR). At low- and mid-load conditions, moder-
ate increases of CH
4 emissions were also observed with
slight decreases in RIT.14,15
PIDING combustion using SOING up to 235 crank
angle degrees (CAD) after top dead center (aTDC) (ear-
lier than SPC modes) was investigated by Florea et al. 16
who established the co-direct injection (DI 2) combus-
tion strategy. In DI 2, the end of NG injection ( EOING)
occurs well before pilot injection and auto-ignition. As
for the SPC investigations, increased efficiency with
decreased PM and CO relative to non-premixed
PIDING combustion was observed. Furthermore,
CCV was deemed acceptable with COV(IMEP) limited
to less than 2%. Relative to fumigated NG operation, a
75% reduction in the emissions of unburned CH
4 was
achieved, however emissions became excessive for
SOI
NG \ /C0 34 CAD aTDC. This was attributed to the
lower piston bowl position at early crank angles result-
ing in poor targeting of the NG fuel jets and significant
penetration of NG into the crevice volumes. In a
follow-up investigation, a narrower NG injection angle
was successfully used to reduce unburned CH
4 emis-
sions and increase efficiency for early SOING.17 Similar
observations regarding the importance of the piston
position for DI fuel mixing processes have been made
for wall-guided DISI engines (e.g. Yadollahi and
Boroomand,
20 Baratta and Rapetto21).
266 International J of Engine Research 24(2)

<!-- PDF_PAGE: 3 -->

Splitting the main NG injection into early- and late-
cycle injections has also been considered as a strategy to
control NG stratification. Li et al. 18 report an increase
in efficiency and reduction of PM and CO when a
greater fraction of the NG (50%–90%) is injected in the
first of two injections. Munshi et al.
22 investigated a
similar split NG injection strategy with the NG pre-
injection occurring during the intake stroke and an
early pilot injection similar to reactivity controlled com-
pression ignition (RCCI) combustion. Experimental
investigation and numerical simulation suggested that
the increased turbulent mixing rates produced by the
late NG injection supported higher flame propagation
speeds and reduced CH
4 emissions.22 The importance
of injection-generated turbulence for enhancing flame
propagation speeds and therefore reducing slow flame
extinction and increasing combustion efficiency has also
been reported for several DISI investigations.
23–25
These findings are of particular importance to stratified
PIDING combustion due to the low flame propagation
speed of lean CH
4-air mixtures which exacerbates slow
flame extinction and uHC emissions.
Common to all stratified and lean-burn DI combus-
tion strategies is the importance of controlling fuel stra-
tification using the main fuel injection timing. For SI
applications this is typically defined as the fuel resi-
dence time between either the start or end of injection
until the spark-timing.
21,25,26 In the case of pilot-ignited
applications, either the RIT has been used, 12–15 and/or
the time delay between the main fuel injection and igni-
tion12 to characterize the fuel stratification.
In the case of PIDING systems, the combustion pro-
cesses and engine performance have been found to be
extremely sensitive to fuel stratification. In-cylinder
OH*-chemiluminescence (OH*-CL) imaging of
PIDING combustion showed that the combustion pro-
cess changed from a quasi-steady jet flame, to rapid
distributed-ignition, to flame propagation as the RIT
was set at + 1.3 ms, + 0.3 ms, and 21.0 ms, respec-
tively.
12 Numerical simulation indicates that parallel
processes of flame propagation, diffusion, and jet-
momentum induced mixing occur in DI
2 combustion.16
Numerical investigation of early-cycle injections from
2180 to 230 CAD aTDC indicate flame propagation
is the dominant process.
18 Characterizing additional
engine control parameters affecting fuel stratification
and identifying the conditions under which certain
combustion processes are dominant is critical to con-
tinue development of further optimized stratified
DING combustion.
In addition to the NG stratification, several studies
have concluded that complex interactions between the
NG jet and pilot jet and ignition are critical to
PIDING combustion performance.
27–29 Using a rapid
compression-expansion machine (RCEM), Fink et al. 28
demonstrated that for positive RIT where pilot ignition
occurs undisturbed by the NG jet, a wide range of
relative spray angles can be used to produce robust NG
ignition. However, when there is temporal overlap of
the pilot and NG jets (i.e. short and/or negative RIT),
thermal and chemical quenching of the pilot reactions
by the much larger NG jet can produce significant
increases in the pilot ignition delay and distance of
pilot ignition from the injector.
28,29 Because these fac-
tors modify ignition timing and location, they have an
impact on the NG stratification and ultimately the NG
combustion process(es) that ensue. These observations
were demonstrated for an unbounded pilot and NG
fuel jet pair (i.e. there was no piston bowl or chamber
walls), which the authors acknowledged as an impor-
tant caveat.
While no single NG stratification strategy has been
identified as optimal under all engine operating condi-
tions, there is potential for increased efficiency, with
low PM, CO, and CH
4 emissions as part of a PIDING
mixed-mode strategy. Despite the demonstrated advan-
tages, relatively few investigations of these stratified
PIDING combustion modes have been performed. As
a result, conclusions regarding the role of NG stratifi-
cation and pilot-NG jet interactions on combustion
performance are not well linked between these investi-
gations. The factors impacting the transition between
the distinct combustion regimes that have been identi-
fied as a function of RIT are also not well characterized
in terms of the fundamental combustion conditions
such as the NG mixture stratification. This work
addresses these gaps as a pre-requisite for further devel-
opment and optimization of stratified-PIDING com-
bustion technology.
Objectives & outline
To support development of higher efficiency PIDING
engines with low emissions, this work aims to survey
the stratified-PIDING combustion strategies that can
be achieved by controlling the NG residence time
through adjustment of RIT. The objectives of this sur-
vey are to:
1. Identify PIDING combustion regimes that exist as
a function of RIT and/or NG residence time (i.e.
NG stratification), where a regime is considered a
domain of RIT that exhibits consistent sensitivity
of pilot combustion, NG combustion, and emis-
sions behavior to major engine control parameters:
RIT, P
inj, and f.
2. Define and characterize generally-applicable (i.e.
not engine-specific) PIDING combustion metrics
that identify transitions between the identified
combustion regimes.
3. Use the identified com bustion regimes and regime
transition definitions to connect the limited stratified-
premixed PIDING literature (SPC and DI2) to con-
ventional NG combustion technologies (i.e. fumi-
gated dual-fuel and non-premixed PIDING).
Rochussen et al. 267

<!-- PDF_PAGE: 4 -->

4. Motivate and guide future in-cylinder optical inves-
tigations of NG mixture formation, ignition, and
NG combustion processes
In the initial results section, an overview of the sensi-
tivity of major engine performance parameters to RIT
is presented. In the main discussion, the NG stratifica-
tion is characterized using the NG residence time, tNG,
and the RIT. The impact of tNG, RIT, and pilot-NG
interactions on PIDING pilot and NG ignition, NG
combustion, and emissions are presented for early- and
late-cycle NG injections, separately. Finally, a summary
of six identified PIDING combustion regimes and the
novel parameters developed to describe the transitions
between these regimes is presented. These combustion
regimes span from conventional non-premixed
PIDING to fully-premixed pilot-ignited NG combus-
tion (dual-fuel). Stratified PIDING strategies identified
in the literature (SPC and DI
2) are also incorporated
into the summary of PIDING combustion regimes,
which augments descriptions of the distinctions between
stratified PIDING combustion strategies.
Experimental facility & measurement
description
The experimental facility used in this investigation is
based on a 2.0 L, single-cylinder, Ricardo Proteus
engine. This facility can be operated in either a ‘‘ther-
modynamic’’ or ‘‘optical’’ configuration. In the thermo-
dynamic configuration, a production aluminum piston
is used, while in the optical configuration a Bowditch
piston arrangement provides a large optical access to
the combustion chamber.
30 In the current work, only
the thermodynamic configuration is considered; how-
ever, injection imaging results from the optical engine
configuration are used to calculate the actual SOING
and SOIpilot. Future work will apply the optical config-
uration to provide more detailed characterization of
combustion regimes identified here. An overview of the
facility is given in Figure 1 and specifications are pro-
vided in Table 1.
To study PIDING combustion, the research engine
was fitted with a first generation Westport Fuel
Systems (WFS) High-Pressure Direct-Injection injector
(HPDI) and dome-loaded self-relieving regulator
(DLSR). The HPDI injector was designed by WFS for
non-premixed combustion and uses independently
actuated concentric needles to control the flow of the
pilot fuel and NG. Combined with a custom program-
mable engine control unit (ECU), this fuel system
allows arbitrary relative injection timing of the diesel
and NG injections. The pilot and NG injection delays
were characterized using in-cylinder Mie scattering
imaging, and all analyses presented in the current work
apply the actual injection timings (i.e. the injector
Figure 1. (a) Single-cylinder engine facility schematic, (b) injector spray configuration, and (c) important PIDING injection
nomenclature.
268 International J of Engine Research 24(2)

<!-- PDF_PAGE: 5 -->

delays are accounted for). The injector is mounted ver-
tically and concentric to the piston bowl. The nozzle
provides nine equally-spaced NG orifices and nine pilot
diesel orifices midway between each NG orifice. Diesel
rail pressure is controlled by the operator while the
DLSR maintains the NG rail pressure at 8 bar below
the diesel rail pressure to maintain stable injector oper-
ation. In all subsequent discussion, the injection pres-
sure, P
inj, refers to the diesel rail pressure. Note that to
accommodate both optical and thermodynamic config-
urations, the research engine has somewhat larger cre-
vice regions and other simplifications compared to a
modern heavy-duty diesel engine. As a result, unburned
fuel and partial combustion product emissions can be
higher than would be seen in an optimized production
PIDING engine.
Definition of measurement conditions
The primary engine control parameter used to charac-
terize stratified PIDING combustion modes is the
relative injection timing, RIT, of the NG with respect
to the pilot diesel (see equation (1) and Figure 1). To
investigate a broad range of RIT, SOI
NG was varied
from 2170 to 24.0 CAD aTDC. Very early SOING
(i.e. 2170 CAD aTDC) were included for comparison
with port-injected dual-fuel combustion, and late-cycle
SOING (210 to 24.0 CAD aTDC) were included to
encompass non-premixed PIDING strategies (i.e.
HPDI). Early SOI
NG was limited to where the intake
valve closes ( 2170 CAD aTDC) in order to avoid dis-
placing intake charge air. A late-cycle pilot injection
was used to control the combustion phasing for all
operating conditions, with SOI
pilot ranging from
228 to 24.5 CAD aTDC. For SOIpilot earlier than
228 CAD aTDC, pilot ignition became unstable. This
was considered to result from low charge temperatures
earlier in the compression stroke producing excessive
ignition delays and over-leaning of the pilot fuel. The
broad sweeps of RIT from highly premixed (very nega-
tive RIT) to predominantly non-premixed charge pre-
paration (positive RIT) were performed for six nominal
operating conditions defined by combinations of P
inj
and global equivalence ratio, fg:
fg = mdiesel /C1 A
F jdiesel, stoich + mNG /C1 A
F jNG, stoich
mair
= fdiesel + fNG
ð2Þ
where mdiesel, mNG, and mair are the measured mass of
diesel, NG, and air per cycle; A
F jdiesel, stoich and A
F jNG, stoich
are the stoichiometric air-fuel ratios for diesel and NG;
and fdiesel and fNG are the diesel and NG equivalence
ratios. The combinations of nominal operating condi-
tions are presented in Table 2, and baseline engine con-
trol parameters held constant for all measurements are
presented in Table 1. A range of P
inj was considered to
investigate the effects of mixing rates on NG stratifica-
tion, pilot-NG interactions, and the resulting combus-
tion modes. To support identification of chemical
effects on combustion processes and pilot-NG interac-
tions, a range of f
g was also considered.
T able 2. Nominal operating conditions and engine set-points.
Pinj [bar-a] fg[2] Pintake[bar-a] tinj, pilot[ms] tinj, NG [ms] RIT range[CAD] uPcyl, max [CAD aTDC]
140 0.63 1.23 1.10 2.93–3.30 [ 2148:224] + 10 /C176
140 0.63 1.23 1.10 2.14–2.63 [ 220: + 18] + 12.5 /C176
180 0.63 1.23 0.90 1.82–1.95 [ 2151:222] + 10 /C176
180 0.63 1.23 0.90 1.48–1.73 [ 217: + 18] + 12.5 /C176
220 0.47 1.66 0.75 1.10–1.36 [ 218: + 18] + 12.5 /C176
220 0.54 1.40 0.75 1.44–1.50 [ 2151:223] + 10 /C176
220 0.54 1.40 0.75 1.16–1.36 [ 216: + 18] + 12.5 /C176
220 0.63 1.23 0.75 1.45–1.54 [ 2153:221] + 10 /C176
220 0.63 1.23 0.75 1.14–1.36 [ 215: + 18] + 12.5 /C176
220 0.71 1.11 0.75 1.46–1.53 [ 2154:223] + 10 /C176
220 0.71 1.11 0.75 1.18–1.36 [ 214: + 18] + 12.5 /C176
Bold typeface indicates the adjusted parameter . All operating conditions performed at 1000 rpm.
T able 1. Engine specifications and constant operating set-
points.
Engine Parameter Value
Displacement [L] 2.0
Bore [mm] 130
Stroke [mm] 150
Compression ratio [ 2] 13.25:1
Piston bowl shape Eccentric torroid
Swirl number 0.1
Direct injector Westport fuel systems HPDI
Pilot fuel Pump diesel (ULSD)
Primary fuel Natural gas ( ’95% CH4)
Maximum engine speed [RPM] 2100
Maximum Pcyl [bar] 170
Operating parameter Set-point
Speed [RPM] 1000
T
intake½8C/C138 40
mdiesel [mg/cycle] 7 6 2
mNG [mg/cycle] 92 6 3
NG energy fraction [%] 94
Rochussen et al. 269

<!-- PDF_PAGE: 6 -->

Fuel mass was held constant for all operating condi-
tions (see Table 1), so variation of fg was controlled by
varying mair through adjustment of Pintake. The NG
injection duration, tinj, NG, was also adjusted to main-
tain constant fuel mass across the wide range of SOING
considered. The pilot injection timing ( SOIpilot) for each
operating condition was selected such that the phasing
of peak Pcyl, uPcyl, max, was held constant across sweeps
of RIT. uPcyl, max was selected as a set-point for combus-
tion phasing (rather than CA50) to avoid excessive com-
bustion harshness, particularly in the range of
/C0 10.RIT.0 CAD where the combustion duration is
very short. For highly premixed conditions
(SOING. /C0 36 CAD aTDC), combustion durations
were significantly longer than for less premixed com-
bustion (SOING& /C0 30 CAD aTDC), so two set-points
for uPcyl, max were used: For highly premixed conditions
(i.e. SOING. /C0 36 CAD aTDC) uPcyl, max =1 060:5
CAD aTDC and for late-cycle NG injections,
uPcyl, max =1 2:560:5 CAD aTDC was used (see
Table 2). The selection of these combustion phasing
definitions resulted in CA50 that was within the range
of 7–10 CAD aTDC for all operating conditions, which
was considered appropriate for heavy-duty engine
applications. These operating specifications are repre-
sentative of a medium load for a heavy-duty engine,
with an observed range of GIMEP from 8.3–11.0 bar
Note that the wide range of operating conditions pro-
duces a wide range of efficiencies (see Figure 6), which
results in a range of GIMEP for the constant fuel mass
used.
To ensure repeatability of results, all measured oper-
ating conditions were repeated at minimum one week
after the original measurement. Experimental results
are presented as the average of the initial and repeat
measurements, with the individual (i.e. minimum and
maximum) measurements plotted as error bars. In all
cases, a high degree of repeatability in emissions and
combustion performance was observed.
Stratified PIDING engine performance
overview
In this section, an overview of PIDING combustion
performance and emissions characteristics is presented
for the full range of NG stratification conditions con-
sidered. The combustion performance characteristics
observed here are used to place the stratified PIDING
combustion modes identified in the literature (i.e. DI 2,
SPC, and non-premixed PIDING) into a single frame-
work of stratified PIDING engine operation. Because
direct measurement of NG stratification was not possi-
ble, the NG residence time, tNG, is used as a simple
indicator of NG stratification. Increasing tNG indicates
increased premixing time and therefore more homoge-
neous (i.e. less stratified) charge preparation. Variants
of this metric have been used in numerous DISI (e.g.
Baratta and Rapetto,
21 Chiodi et al. 24) and stratified
PIDING investigations. 12,13 Generally, tNG is defined
as the interval between the start or end of NG injection
(SOING or EOING) and some measure of the start of
NG combustion, uSOC, NG, as given in equation (3):
tNG = uSOC, NG /C0 SOING ð3Þ
In previous work, in-cylinder OH*-chemilumines-
cence (OH*-CL) imaging of PIDING combustion with
26 CAD \ RIT \ + 14 CAD showed that NG igni-
tion occurs near the pilot combustion regions before
the start of premixed NG combustion. 12 There, the
start of premixed NG combustion ( uSOC, NG) indicated
by OH*-CL was effectively identified by an inflection
in the slope of the rising edge of the main AHRR peak.
Note that in this work, apparent heat release rate
includes energy loss through heat transfer (i.e. no heat
transfer model is used). There, a metric based on the
slope (rather than magnitude) of AHRR was found to
match OH*-CL indicators for partially-premixed NG
combustion for a range of different peak AHRR result-
ing from different RIT and fuel masses. In the current
work however, a much broader range of RIT produces
a diverse set of AHRR shapes. This necessitated modi-
fication of the previous definition for u
SOC, NG (AHRR
inflection point) to the phasing at which the slope of
AHRR (dAHRR/d u) reaches 20% of its maximum
value:
uSOC, NG = ujdAHRR=du =0 :2/C1 max(dAHRR=du) ð4Þ
This modified definition was selected such that
uSOC, NG is consistent with the previously published def-
inition for non-premixed conditions, 12 while also pro-
viding a reliable marker for the start of premixed NG
combustion across a much wider range of RIT and NG
stratification conditions (which produce diverse AHRR
shapes). A graphical presentation of the calculation of
uSOC, NG for several distinct operating conditions is pre-
sented in Appendix 2 A wide range of mathematical
definitions for defining the start of premixed NG com-
bustion were compared and found to have negligible
impact on all calculations based on u
SOC,NG and tNG.
The exact threshold used in equation (4) is therefore
not considered critical to the conclusions of this work.
In Figure 2, the relationship between RIT and the NG
residence time, tNG, is presented for variations of Pinj
and fg.
For all nominal operating conditions considered, a
critical RIT, RITcrit’ 0:6860:17 ms (4 6 1 CAD) was
measured. Note that the precision of RITcrit is limited
by the spacing of RIT = 2 CAD = 0.34 ms and may
not be appropriate for all possible operating conditions
(e.g. higher P
inj). RITcrit separates two regimes of NG
stratification distinguished by the relationship between
RIT and tNG:
1. tNG 6¼ f(RIT): For RIT . RITcrit, tNG has no sensi-
tivity to RIT and is at a minimum value, tNG, min.
For a given Pinj, tNG, min indicates a minimum
270 International J of Engine Research 24(2)

<!-- PDF_PAGE: 7 -->

fraction of the total NG mass is premixed at
uSOC, NG; fpremix = fpremix, min.
2. tNG = f(RIT): For RIT \ RITcrit a linear increase
in tNG occurs with advancing SOING relative to
SOIpilot (i.e. with decreasing RIT) and
fpremix . fpremix, min.
Here, fpremix is used to qualitatively describe the NG
mixture state in terms of tNG (i.e. distinguishing
whether the minimum, maximum, or an intermediate
amount of NG premixes prior to u
SOC, NG). For all of
the considered nominal operating conditions (combina-
tions of Pinj and fg) distinct injection control strategies
(SOIpilot and SOING) are required to maintain appro-
priate combustion phasing for different RIT. The
SOIpilot and SOING used for all measurements is pre-
sented in Figure 3.
For /C0 404SOING4 /C0 30 CAD aTDC, combustion
was unstable and significantly advanced SOIpilot was
necessary to further decrease RIT. This is indicated by
discontinuous lines for each injection control strategy
in Figure 3. Florea et al.
16,17 observed the same abrupt
Figure 2. Relationship between relative injection timing ( RIT) of NG and pilot and the NG residence time, tNG , prior to the start of
the main premixed combustion. Critical RIT, RITcrit, where tNG = f (RIT) highlighted with dashed line. Left: Variation of Pinj, Right:
variation of fg.
Figure 3. Injection strategy used to maintain constant combustion phasing (see T able 2) across variation of RIT. Data sets for
variation of fg and Pinj shown at top and bottom, respectively. Note that the x-axis is presented in terms of SOING, which is in
contrast to all other figures which use RIT for the x-axis. Lines of constant RIT are shown in the figure background.
Rochussen et al. 271

<!-- PDF_PAGE: 8 -->

transition for DI 2 combustion when SOING was
advanced past SOING = 234 CAD aTDC. They con-
cluded that the abrupt change in combustion behavior
was a result of different NG impingement geometries
caused by piston motion during the NG injection. For
late SOI
NG, the NG jet impinges within the piston
bowl, while for early SOING, NG jet impingement
occurs in the squish volume and cylinder wall. In the
current work, the crank angle where the NG jet orifice
is geometrically aligned with the corner of the piston
bowl (separating piston bowl and squish volume)
occurs at SOI
NG, trans: = /C0 36 CAD aTDC (note that
SOING, trans: does not account for the NG jet transit
time from the injector to the bowl wall). The possible
jet impingement geometries are illustrated in Figure 4.
For a given P
inj, the range of SOING that produces
unstable combustion is approximately the same as the
NG injection duration, tinj, NG, which is demonstrated
for Pinj = 22 MPa in Figure 3.
The different jet impingement geometries are funda-
mental to NG stratification and crevice volume pene-
tration and are therefore used here to classify all the
stratified PIDING combustion modes as either early-
or late-cycle NG injection strategies. This distinction is
highlighted in all relevant figures with early- and late-
cycle NG injection measurements indicated with square
and circular markers, respectively.SOI
NG, trans: is also indi-
cated with a blue dashed line in Figure 3. Using RITcrit
and SOING, trans: as reference injection timings, common
patterns in the injection control strategy are noted for all
nominal operating conditions in Figure 3:
1. SOI
NG \ SOING, trans::Combustion phasing is con-
trolled by SOIpilot. For a given Pinj or fg, SOIpilot is
held approximately constant while SOING is
adjusted to adjust RIT.
2. SOING . SOING, trans: and RIT \ RITcrit: SOIpilot
and SOING must be adjusted simultaneously to
vary RIT while maintaining constant combustion
phasing. Details of the control strategy are sensi-
tive to both Pinj and fg.
3. RIT . RITcrit : Combustion phasing is controlled
by SOING. For a given Pinj, SOING is held constant
while SOIpilot is adjusted to vary RIT. Injection tim-
ing is not sensitive to fg for 0:47 \ fg \ 0:71.
Common patterns in emissions and indicated com-
bustion metrics were also observed through variation
of RIT. An overview of emissions performance and
indicated combustion metrics are presented for all nom-
inal operating conditions in Figures 5 and 6, respec-
tively. Omitted data points in the plots of Figure 5
indicate exhaust species measurements that were above
the calibrated range of the emissions analysis equip-
ment (CH
4 and NO X emissions for Pinj = 180 bar and
/C0 120 \ RIT \ /C0 40 CAD omitted due to poor agree-
ment between initial and repeated measurements).
For RIT . RITcrit, variation of RIT does not corre-
spond to any change in tNG, therefore combustion and
emissions performance is relatively insensitive to RIT.
When RIT \ RITcrit, tNG begins to increase and the
fraction of NG that premixes prior to ignition, fpremix,
increases. Across this transition from minimally-
premixed combustion (i.e. non-premixed PIDING) to
slightly premixed combustion (SPC), all aspects of com-
bustion become highly sensitive to RIT, consistent with
other investigations.
12–14 The increasingly premixed
combustion results in higher efficiency (Figure 6) and
lower CO emissions with a very minor increase in CH
4
emissions from 1–2 mg/g-fuel (Figure 5), consistent with
other investigations of SPC.
13,14 The transition to SPC
produces significant increases of combustion harshness
(maximum RoPR) and NOX emissions, which have also
been previously reported. The increased NO X emissions
correlate with a marked increase to the mean cylinder
temperature (see Appendix 3) for SPC operation. EGR
is considered a viable method for reducing both NO X
and combustion harshness to more acceptable
Figure 4. Three combustion chamber geometries corresponding to different NG jet impingement scenarios at different SOING: (i)
squish volume and cylinder wall, (ii) transition between squish volume and piston bowl, and (iii) within piston bowl.
272 International J of Engine Research 24(2)

<!-- PDF_PAGE: 9 -->

Figure 5. Overview of PIDING emissions performance for all nominal operating conditions at all considered RIT. Sensitivity of
emissions to fg and Pinj shown in right and left columns, respectively. Omitted data points indicated species concentrations above
the calibration range of the emissions analysis instruments.
Figure 6. Overview of key indicated combustion metrics for PIDING performance for all nominal operating conditions at all
considered RIT. Sensitivity of engine performance to fg and Pinj shown in right and left columns, respectively.
Rochussen et al. 273

<!-- PDF_PAGE: 10 -->

levels,13,15 but was not available for the current mea-
surements. With the transition to SPC, a slight increase
in CCV is observed, however it is not significantly
greater than that of the non-premixed combustion pre-
viously reported.
13
As RIT is reduced further from RITcrit, combustion
becomes increasingly premixed. Depending on Pinj,
EOING occurs prior to pilot ignition (e.g. for
Pinj = 22 MPa and RIT \ /C0 6 CAD) and the entire
mass of NG premixes to some extent (i.e.
fpremix = 100%). The increasingly premixed conditions
improve the combustion behavior observed in Figures
5 and 6: increasing efficiency, decreasing harshness,
and decreasing NO
x emissions while maintaining low
CO emissions. A slight increase in CH 4 emissions is
observed and COV(GIMEP) is observed to increase
(from approximately 2% to 4%), before reducing back
to an acceptable level of 2% near RIT’ /C0 15 CAD for
all late-cycle operating conditions except for
Pinj = 14 MPa. This optimal range of NG stratification
matches the behavior of DI 2 previously reported to be
flame propagation driven by diffusion and injection-
generated turbulence.
16,17
For early-cycle NG injections (i.e.
SOING \\ SOING, trans), combustion behavior is less
sensitive to RIT than for late-cycle strategies. As for
port-injected combustion (e.g. dual-fuel), flame propa-
gation is expected to be the dominant combustion pro-
cess for early-cycle strategies due to the long NG
residence times. Significant CH
4 emissions result from
increased penetration of NG into crevice volumes and
slow flame extinction. Consistent with investigations of
dual-fuel and DISI combustion, increasing fg and Pinj
increases the flame propagation speed and maintains
the mixture above the CH 4 lean flammability limit.
This is demonstrated in Figures 5 and 6 where CH 4
emissions and CCV decrease for increasing fg and Pinj.
Common patterns in combustion and emissions
behavior are observed as a function of RIT in Figures 5
and 6 and qualitatively match observations from other
studies of stratified PIDING combustion (SPC 13,14 and
DI216,17) for similar RIT. This indicates that these RIT
intervals represent generally relevant stratification
conditions that characterize distinct regimes of
PIDING combustion.
Identifying & characterizing stratified
premixed PIDING combustion regimes
In the context of this work, a combustion regime is a
domain of RIT (representing NG stratification) where
pilot combustion, NG combustion, and emissions beha-
vior are consistent. Consistency between operating con-
ditions is indicated if all relevant heat release features
(e.g. combustion duration, ignition delay) and exhaust
emissions respond in the same manner (i.e. increase,
decrease, or are insensitive) to variations of the major
engine control parameters investigated in this work:
P
inj, RIT, and fg. The objective of this discussion is to
identify and classify distinct combustion regimes and
the parameters that govern transitions between these
regimes based on AHRR and emissions.
Early-cycle NG injection combustion regimes
This section examines the early-cycle PIDING combus-
tion strategies where the NG jets impinge above the
piston (i.e. SOI
NG \\ SOING, trans, see Figure 4) and
significant premixing of the NG occurs prior to pilot
ignition. For long NG residence times, early-cycle
PIDING engine performance and combustion proper-
ties are expected to approach that of a fully-premixed
combustion (i.e. dual-fuel combustion). Here, the pilot
ignition delay, AHRR, and emissions performance
trends of PIDING combustion with early-cycle NG
injections are discussed in the context of the expected
behavior for homogeneously-premixed pilot-ignited
NG combustion. Relevant expected behavior for pilot-
ignited premixed NG combustion is briefly summarized
in Table 3.
For PIDING combustion with early-cycle NG injec-
tions, there may be insufficient time to produce a
homogeneous mixture throughout the combustion
chamber, so f
local = f(fg, RIT). Furthermore, charge-
cooling and turbulence resulting from the direct NG
injection imply that T
mix = f(RIT) and TKE = f(RIT)
T able 3. Expected effects of f, fuel-air mixture temperature ( Tmix), and turbulent kinetic energy (TKE) on pilot-ignited combustion
of premixed NG.
Pilot Ignition Flame Propagation CH4 Emissions
f (f \ 1) f " = tign " (pre-ignition
radical competition31)
f " = CA10/C0 90% #
f " = max(AHRR) "(increasing
laminar flame speed 32)
f " =C H4#
(reduced slow-flame
extinction33)
Tmix Tmix " = tign #
(pilot evaporation &
kinetics34)
Tmix " = CA10/C0 90% #
Tmix " = max(AHRR) "
(increasing laminar flame speed 32)
Tmix " =C H4#
(reduced slow-flame extinction
and surface quenching 33)
TKE TKE " = CA10/C0 90% #
TKE " = max(AHRR) " (increasing
turbulent flame speed 34)
TKE " =C H4# (reduced slow-
flame extinction34)
274 International J of Engine Research 24(2)

<!-- PDF_PAGE: 11 -->

(i.e. effect of Tmix and TKE from injection will decrease
with increasingly advanced SOING). Rigorously distin-
guishing the role of each of these effects is out of the
scope of the current work, however assessment of the
net effect of RIT on ignition and main premixed com-
bustion processes provides valuable insight into
PIDING combustion with early-cycle NG injections.
Experiments comparing t
ign for full combustion (i.e.
pilot + NG) and pilot-only operation were performed
to quantify the net impact of the NG direct injection
and premixing on t
ign. D(tign) is defined as the increase
in the pilot ignition delay caused by the NG injection:
D(tign)= tignjpilot + NG /C0 tignjpilot/C0 only ð5Þ
where tign is calculated as the elapsed time between
SOIpilot and the AHRR increasing above a threshold of
30 kJ/CAD-m3:
tign = ujAHRR . 30 /C0 SOIpilot ð6Þ
The tign for pilot-only operation was measured imme-
diately after NG injection was disabled from steady-state
operation. Measurement of tignjpilot/C0 only uses the average
AHRR of the first two cycles after NG injection is dis-
abled to match the combustion chamber conditions (i.e.
cylinder wall temperature, residuals, engine speed, etc.)
as closely as possible between the full combustion and
pilot-only measurements. Note that because only two
cycles are used to measure t
ignjpilot/C0 only some signal noise
remains in the AHRR measurement. Reducing sensitivity
of tignjpilot/C0 only to signal noise moti vated the selection of
AHRR . 30 kJ/CAD-m3 as the ignition criterion.
Pilot-only and full combustion AHRR measure-
ments are presented for several early-cycle RIT along
with the measured D(tign) in Figure 7. With the excep-
tion of the condition with the latest NG injection
(RIT = /C0 5:4m s= 232.5 CAD), the AHRR resem-
bles typical dual-fuel combustion; the first AHRR peak
corresponds to auto-ignition of diesel and entrained
NG, and the second peak corresponds to flame propa-
gation through the remaining premixed NG.
33
Consistent with dual-fuel combustion literature, the
presence of premixed NG increases tign for all early-
cycle RIT. Both the magnitude of D(tign) and the shape
of the full combustion AHRR vary with RIT. This
indicates that for the nominal operating condition
shown in Figure 7 ( f
g =0 :63, Pinj = 220 bar), the NG
mixture properties (thermodynamic and/or fluid
mechanical) have not reached a steady-state with
respect to RIT. Near the NG jet impingement transi-
tion at SOI
NG, trans (RIT’ /C0 20 CAD), the complex
flow and mixture distribution resulting from the NG
jet impingement with both the squish volume and pis-
ton bowl result in a AHRR shape that is distinctly dis-
similar from the dual-fuel shape (e.g. RIT = /C0 32:5
CAD in Figure 7). In this transition region, it is
unlikely that the conceptual model of premixed dual-
fuel combustion can appropriately describe the fuel
conversion processes.
For all operating conditions except for the latest NG
injections near SOI
NG, trans, the sensitivity of combustion
metrics to fg is consistent with flame propagation beha-
vior where increasing fg results in higher peak AHRR
and lower CH 4 emissions (see Table 3). In Figure 8,
D(tign) is compared to the combustion duration and
emissions of incomplete combustion products (CH4 and
CO) to assess the role of NG stratification on the flame
propagation process. For all combustion metrics shown
in Figure 8, a significant reduction in sensitivity to RIT
is observed at approximately the same RIT, denoted as
RITinsens:. For RITinsens: \ RIT \ RITNG, trans CH4 and
CO emissions increase with increasing tNG indicating
increased NG penetration to crevice volumes and/or
slow flame extinction is occurring. While the injection-
generated turbulence should support more rapid flame
propagation for later NG injections, long combustion
durations observed for RIT
insens: \ RIT \ RITNG, trans
and simultaneously low CH 4 indicate that NG
Figure 7. Comparison of AHRR for full combustion and pilot-only combustion for the fg = 0.63/Pinj = 220 bar operating condition
with early-cycle NG injection. Comparison of the difference in pilot ignition delay, D(tign), used to qualitatively assess the state of
NG premixing and stratification. Red lines indicate the measurement of D(tign).
Rochussen et al. 275

<!-- PDF_PAGE: 12 -->

stratification dominates the flame propagation process
and mass of NG in the crevice volumes. For the same
range of RIT, D(t
ign) increases with increasing tNG.
This may indicate increasing NG concentration in the
vicinity of the pilot ignition regions while f
local
approaches fg with increasing tNG.
For RIT \ RITinsens:, D(tign) decreases with decreas-
ing RIT rather than increasing as for RIT . RITinsens:.
This transition is considered to be a result of tNG
exceeding the duration required to develop an approxi-
mately homogeneous concentration of NG throughout
the combustion chamber by the time of ignition. For
RIT \ RIT
insens:, optimal early-cycle engine operation
occurs for tNG’ 15 ms, where the flame propagation
process is most rapid and CH 4 emissions are moder-
ately reduced. This optimal early-cycle RIT may be a
balance between the influence of unstable combustion
conditions near the jet impingement transition and high
injection-generated turbulence for later NG injections.
Interestingly, for RIT \ RIT
insens:, increasing tNG pro-
duces decreasing D(tign). This may be due to the dimin-
ishing impact of charge-cooling on ignition delay for
earlier SOI
NG, however further investigation is required
to characterize this effect.
Late-cycle NG injection combustion regimes
This section examines the different combustion regimes
that exist for late-cycle PIDING strategies, correspond-
ing to SOI
NG . SOING, trans. With late-cycle NG injec-
tions, NG stratification and PIDING combustion
behavior is extremely sensitive to RIT. Non-premixed
PIDING (e.g. Ouelette et al., 3 McTaggart-Cowan
et al., 11,14), SPC, 13 and DI 216,17 combustion strategies
all occur with late-cycle NG injections and are predo-
minantly distinguished from one another by the RIT
used. For late-cycle NG injections, SOI
pilot and SOING
are close to one another and the fluid mechanic and
chemical interactions between the two fuel injections
can significantly influence ignition and NG combustion
behavior.
12,28,29 In particular, the fraction of NG that
undergoes premixing prior to NG combustion, fpremix,
is sensitive to RIT with three general scenarios being
possible:
1. RIT . RITcrit and fpremix = fpremix, min. Pilot injec-
tion occurs sufficiently in advance of the NG injec-
tion such that tNG is minimized (see Figure 2). This
results in the minimum NG premixed fraction,
f
premix, min, and is typical of non-premixed PIDING
combustion.
2. RIT . RITcrit and fpremix = f(RIT). As RIT is
reduced from RITcrit, there is overlap of the pilot
and NG injections, tNG increases, and an increas-
ing mass of NG premixes prior to the NG combus-
tion process (i.e. f
premix . fpremix, min). This occurs
for the SPC strategy.
3. fpremix = 100%. The NG injection is completed suf-
ficiently early (i.e. EOING \\ uSOC, NG) such that
the entire mass of NG undergoes some premixing
prior to the NG combustion process. This occurs
for the DI
2 strategy.
The following discussion will examine each of the
above scenarios in terms of pilot combustion, NG com-
bustion, and emissions behaviors.
Figure 8. Effect of RIT and tNG on pilot ignition delay ( D(tign)), combustion duration ( CA10/C0 90%), CH4 emissions, and CO emissions
for early-cycle NG injections.
276 International J of Engine Research 24(2)

<!-- PDF_PAGE: 13 -->

Effects of late-cycle NG injection on pilot
combustion. Interaction of the pilot and NG jets has
been identified as a critical factor for PIDING combus-
tion performance. 13 Investigations examining interac-
tions between direct pilot and NG injections have
shown that quenching and advection of the pilot reac-
tants and products by the NG jet can occur when there
is significant overlap of the two fuel jets (spatial and
temporal overlap).
12,28,29 In these cases, quenching of
the pilot may be as a result of one or more of: (i)
reduced local temperature, (ii) reduced local oxygen
concentration, (iii) excessive local strain rate, or (iv)
chemical competition for pre-ignition radicals. Further
interaction between the pilot and NG jets may occur as
the NG jets that have penetrated to the bowl wall are
reflected and return toward the center of the combus-
tion chamber.
12,19
Attributing quenching to individual processes is
challenging, however the net effect on pilot ignition can
be investigated using D(t
ign) (equation (5)). In Figure 9,
the sensitivity of D(tign) to late-cycle NG injections is
presented for four different RIT covering the three dif-
ferent NG premixing scenarios identified. Only the
ignition sequence of each AHRR is shown in Figure 9
to improve visualization of D(t
ign).
For RIT = + 10 CAD, pilot injection and auto-
ignition is complete prior to SOING and there is negligi-
ble difference in the pilot-only and full combustion
AHRR in Figure 9, indicating this is considered free
pilot auto-ignition. For RIT = 0 CAD, the pilot and
NG injections overlap (dashed lines in Figure 9). This
results in a strong quenching of the pilot by the NG jet,
indicated by an increase in D(t
ign) and a reduced area
under the pilot ignition AHRR curve for the full com-
bustion case. Reduced area under the pilot AHRR
implies a portion of the diesel remains unreacted until
the main NG combustion process. For RIT = /C0 10
CAD, all of the NG is injected prior to pilot injection
(EOI
NG \ SOIpilot, therefore fpremix = 100%), however
D(tign) is small and there is little impact on the leading
edge of the ignition AHRR. With further advanced
SOING (RIT = /C0 17 CAD), a longer tNG results in
greater mixing of NG and pilot reactants and an
increased pilot ignition delay and a more gradual pilot
ignition AHRR. This suggests that for RIT = /C0 17
CAD the NG has had sufficient time to premix near
the pilot causing an increase in the pilot ignition delay
due to competition for pre-ignition radicals and/or
reduced local oxygen concentration.
For all nominal operating conditions, a characteris-
tic pattern of pilot quenching behavior with respect to
variation of RIT occurs. To support comparison of this
behavior between all nominal operating conditions, a
normalized definition of RIT, RIT*, is proposed:
RIT* = RIT /C0 RITcrit
tinj, NG
ð7Þ
RIT* = 0 corresponds to RIT = RITcrit (i.e. the limit
for minimally-premixed combustion) and RIT*’ /C0 1
corresponds to the injection timing where SOING has
been advanced by one injection duration ( tinj, NG) from
RITcrit. Therefore, RIT*’ /C0 1 provides an estimate of
the maximum RIT where the NG injection is suffi-
ciently early to allow some premixing of the entire mass
of NG prior to combustion.
In Figure 10, the sensitivity of late-cycle D(tign)t o
Pinj and fg is presented using both RIT and RIT* (top
and bottom of Figure 10, respectively). Plotting D(tign)
with respect to RIT* results in a common domain of
pilot quenching for all nominal operating conditions
for /C0 1 \ RIT* \ 0, which is not clear when RIT is
used. This motivates application of RIT* instead of
RIT for comparing combustion and emissions perfor-
mance for late-cycle NG injections.
For all nominal operating conditions, the maximum
pilot quenching effect (largest D(tign)) occurs at
RIT*’ /C0 0:5 (i.e. SOIpilot occurs midway through NG
injection). For RIT* . 0, SOING is sufficiently retarded
with respect to SOIpilot that free pilot auto-ignition
occurs and there is only a small D(tign). For all operat-
ing conditions, the NG injection becomes too advanced
to measurably quench the pilot at RIT*. /C0 1.
Figure 9. Comparison of AHRR for full combustion and pilot-only combustion to assess the impact of late-cycle NG injections on
pilot ignition delay. Red lines indicate the measurement of D(tign). fg = 0.63/Pinj = 180 bar operating condition shown.
Rochussen et al. 277

<!-- PDF_PAGE: 14 -->

For Pinj ø 180 bar and fg ø 0:63, NG injection
causes the pilot auto-ignition process to advance
(D(t
ign) \ 0) for /C0 2 \ RIT* \ /C0 1:25 in Figure 10).
No clear chemical or fluid cause for this behavior has
been found in the literature or measurements consid-
ered here. This unique ignition behavior may contrib-
ute to high h
i, g and low COV(GIMEP) (see Figure 6)
noted for this range of RIT* and therefore warrants
further investigation.
In all cases in Figure 10, an increase in D(tign) occurs
for the most negative RIT*. This range of RIT* corre-
sponds to the DI2 strategy presented by Florea
et al. 16,17 For this RIT*, EOING \\ SOIpilot therefore
increasing D(tign) is likely due to chemical competition
for pre-ignition radicals. As in homogeneously pre-
mixed NG systems, the pilot ignition delay increases
with increasing f
g for very negative RIT* (i.e.
D(tign)jf =0 :71 . D(tign)jf =0 :63 . D(tign)jf =0 :54 for
RIT* \ /C0 2:25). Because impingement of the NG jet
with the piston bowl edge occurs earlier for higher Pinj,
the minimum RIT for each Pinj is different and the
effects of Pinj on D(tign) in this regime of combustion
are unclear.
Effects of late-cycle NG injection on NG combustion. In this
section, the three domains of RIT* identified in the pre-
vious section (RIT* . 0, /C0 1.RIT* \ 0, and RIT*. /C0 1
) are connected to NG combustion and emissions beha-
viors, which were shown to be highly sensitive to late-
cycle RIT in Figures 5 and 6. To support the proposed
combustion regimes, Figure 11 contrasts the AHRR for
adjacent regimes.
In Figure 11, the peak heat release rate produced by
premixed NG combustion increases rapidly as RIT
* is
adjusted from positive to negative values. This transi-
tion is defined by RIT
* = 0 where tNG becomes a func-
tion of RIT and fpremix increases with decreasing RIT
(see Figure 2). Near this transition pilot heat release is
less prominent, indicating the NG jets are quenching
the pilot reactions (see Figure 10). This may lead to
some fraction of the pilot reactants being consumed in
the NG combustion process further contributing to the
high peak AHRR, short combustion duration, and high
indicated gross efficiency, h
i, g (see Figure 6).
For /C0 1 \ RIT* \ 0( /C0 10 CAD \ RIT \ 2 CAD),
the AHRR shape is remarkably insensitive to RIT* in
Figure 11. This suggests that tNG does not influence
heat release for this regime of combustion. This is in
contrast to the decreasing peak AHRR with decreasing
RIT
* for RIT* \ /C0 1, indicating tNG is important for
this range of RIT*. The contrast in sensitivity of AHRR
to tNG (i.e. sensitivity to RIT*) across RIT*’ /C0 1 rein-
forces the utility of RIT* (equation (7)) for defining
regimes of PIDING combustion.
Combustion duration ( CA10/C0 90%), NG residence
time ( tNG), and emissions of incomplete combustion
products are compared using RIT* for all nominal
operating conditions in Figure 12. For all conditions, a
rapid reduction of combustion duration and CO emis-
sions occurs at the RIT
* = 0 regime transition. As
RIT* is reduced through 0 . RIT* . /C0 1, there is only
Figure 10. Effect of late-cycle NG injection on pilot ignition delay. T op row: D(tign) with respect to RIT. Bottom row: D(tign) with
respect to normalized relative injection timing, RIT/C3 , where RITcrit =0 :68 ms (4 CAD), tinj, NG’2:3, 1.7, and 1.3 ms for Pinj = 140, 180,
and 220 bar, respectively.
278 International J of Engine Research 24(2)

<!-- PDF_PAGE: 15 -->

very moderate increase in CH 4 emissions despite an
increasing fpremix. For all conditions, a minimum com-
bustion duration and CO emissions level are reached at
RIT*’ /C0 1. This minimum level is insensitive to Pinj
and fg for fg ø 0:63, and is constant for further
decreases in RIT* despite the noted decrease in peak
Figure 11. Comparison of AHRR for different late-cycle PIDING combustion regimes Left: RIT/C3 . 0 versus /C0 1.RIT/C3 \ 0. Right:
RIT/C3 \ 0 vs. RIT/C3 . /C0 1. Pinj = 180 bar and fg = 0.63 operating condition shown.
Figure 12. Effect of RIT/C3 on combustion duration ( CA10/C0 90%), NG residence time ( tNG), CH4 emission concentration, and CO
emission concentration for late-cycle NG injections. Pinj and fg effects shown at left and right, respectively. Defined combustion
regime transitions denoted with dashed lines. Note that by definition, RIT/C3 = 0 coincides with the change of tNG = tNG, min to
tNG = f (RIT).
Rochussen et al. 279

<!-- PDF_PAGE: 16 -->

AHRR for RIT* \ /C0 1 in Figure 11. This indicates
that unlike flame propagation, neither increased turbu-
lence or closer-to-stoichiometric chemistry influence
the global reaction speed in this regime of combustion.
For RIT
* \ /C0 1, CH 4 emissions increase more rap-
idly with decreasing RIT* (i.e. increasing tNG) than for
/C0 1 \ RIT* \ 0, and become sensitive to fg. Here, the
CH4 emissions are more sensitive to fg with decreasing
fg, and there is no sensitivity between fg =0 :63 and
0.71. This change in CH 4 emissions behavior at
RIT*’ /C0 1 indicates that one or more CH 4 emissions
sources becomes more prominent for RIT* \ /C0 1.
For RIT* \ /C0 1, combustion duration decreases
moderately with increasing fg for fg \ 0:63. This may
account for the observed increase in CH 4 emissions as a
result of slow flame extinction (for fg \ 0:63, here).
For fg ø 0:63 and all considered Pinj,C H 4 emissions
show only very weak sensitivity to tNG indicating that
the NG is effectively constrained to the piston bowl vol-
ume and crevice volume quenching is not significant.
The above discussion has demonstrated that
RIT
* = 0 and RIT*’ /C0 1 are effective for classifying
PIDING combustion with late-cycle NG injection into
3 regimes. Within each regime, the pilot combustion,
NG combustion, and emissions behavior are consistent
with respect to variation of Pinj, fg, and RIT*. Across
the regime boundaries ( RIT* = 0 and RIT*’ /C0 1) pilot
combustion, NG combustion, and emissions behavior
changes rapidly with respect to varying RIT*. This
demonstrates that the definition of RIT* relates para-
meters critical to the NG stratification, and that RIT*
is an appropriate parameter for characterizing late-
cycle PIDING combustion regimes.
Summary of stratified-premixed PIDING
combustion modes
This section summarizes the identified stratified
PIDING combustion regimes, their key characteristics,
and the parameters that define their domains. In
Figure 13, the six identified combustion regimes (1 ! 6)
are presented with respect to four injection phasings
(A! D). Figure 14 presents exemplary AHRR for each
Figure 13. Conceptual summary of the six identified stratified PIDING combustion regimes and four fundamental injection
phasings distinguishing the combustion regimes. Characterization of the NG injection, stratification, pilot combustion, and NG
combustion of each combustion regime presented with respect to fundamental domains of RIT.
280 International J of Engine Research 24(2)

<!-- PDF_PAGE: 17 -->

of the identified combustion regimes. Late-cycle
PIDING combustion regimes are best defined using
the non-dimensional parameter, RIT*, while early-cycle
operating conditions are more effectively defined using
the absolute injection timings in terms of CAD (i.e.
SOING, trans, and RIT).
In order of decreasing NG residence time, tNG:
1. RIT-insensitive Premixed Regime ( RIT \ RITinsens:):
Pilot combustion, NG combustion, and emissions
behavior is consistent with homogeneously pre-
mixed NG combustion (i.e. flame propagation). In
this regime, there is significantly reduced sensitivity
of pilot combustion, NG combustion, and emis-
sions to RIT compared to all other combustion
regimes.
2. Early-Cycle Stratified-Premixed Regime
(RIT
insens: \ RIT, SOING \\ SOING, trans): Pilot
combustion and NG combustion behavior sensitiv-
ity to fg is consistent with homogeneously pre-
mixed NG combustion. However, CH 4 emissions
increase with increasing tNG, indicating that NG
has not completely penetrated the crevice volumes
due to significant NG stratification.
3. NG Impingement Transition Regime
(SOING’ SOING, trans): Alignment of the NG injec-
tion axis with the piston bowl at SOING, trans causes
the NG jet to impinge near the edge of the piston
bowl resulting in unstable combustion.
4. Late-Cycle Stratified-Premixed Regime
(SOING /C29 SOING, trans, RIT* \/C0 1): The NG jet
impinges within the piston bowl and NG injection
terminates sufficiently early such that the entire
mass of NG premixes to some degree. The result-
ing combustion process is very rapid, yielding high
h
i, g combined with low CH 4 and CO emissions
and low combustion harshness. This regime
encompasses the DI 2 combustion strategy reported
by Florea et al. 16,17
5. Variable Premixed Fraction Regime ( /C0 1.RIT*
\ 0, fpremix = f(RIT)): Overlapping pilot and NG
injection processes cause the NG residence time
and premixed fraction of NG to be directly con-
trolled by RIT. Quenching of the pilot products by
the NG jets results in some mass of diesel reacting
in the NG combustion event. Heat release is
extremely rapid and insensitive to Pinj, fg, and
RIT. Combustion in this regime with RIT*
approaching 0 has been investigated as SPC. 13
6. Minimally-Premixed Regime ( RIT* . 0): Free pilot
auto-ignition occurs prior to significant NG jet
penetration, resulting in the minimum NG resi-
dence time and minimum premixed NG fraction.
This regime of PIDING combustion is applied in
typical HPDI applications.
3
Conclusions
A survey of stratified PIDING combustion regimes
was conducted by sweeping the relative injection tim-
ing, RIT, of a heavy duty PIDING engine from 2150
CAD to + 18 CAD for Pinj = 140 /C0 220 bar,
fg =0 :47 /C0 0:71, at 1000 rpm. Regimes of PIDING
combustion were identified as domains of RIT (repre-
senting NG stratification) where pilot and NG combus-
tion AHRR, and emissions behaved consistently with
respect to variation of f
g, Pinj, and RIT.
The following six stratified PIDING combustion
regimes were identified, presented here in order of
decreasing NG residence time:
1. RIT-insensitive Premixed
2. Early-Cycle Stratified-Premixed
3. NG Impingement Transition
4. Late-Cycle Stratified-Premixed
5. Variable Premixed Fraction
6. Minimally-Premixed
Figure 14. Characteristic AHRRs for each identified stratified-premixed PIDING combustion regime. Numbering references Figure
13.
Rochussen et al. 281

<!-- PDF_PAGE: 18 -->

These regimes span from fully-premixed to predomi-
nantly non-premixed NG combustion and encompass
several injection strategies (HPDI, 3 SPC,13DI216) that
have been previously identified by other investigators.
Qualitative agreement in combustion performance and
emissions between the current work and that of other
investigations was observed for equivalent ranges of
RIT, despite these works being independently com-
pleted on different engines. This substantiates the util-
ity of RIT to characterize the regimes of PIDING
combustion.
The fine RIT resolution considered here, enabled the
transitions in combustion and emissions behavior
between the identified regimes of PIDING combustion
to be elucidated, and the RIT domain of each regime to
be described using generic PIDING parameters for the
first time. A novel parameter, RIT
* (equation (7)), was
introduced to classify PIDING regimes for late-cycle
NG injections based on the NG injection duration,
t
inj, NG, and the NG residence time, tNG. The domain of
/C0 1.RIT* \ 0 is of particular relevance as this range of
injection timings results in the NG injection quenching
the pilot reactions, which has not previously been char-
acterized in a PIDING engine. Quenching was identi-
fied here by comparing the pilot ignition delay with
and without the NG injection, D(t
ign, pilot) (equation
(5)).
The novel experimental methods and identified
regimes of stratified PIDING combustion are consid-
ered to be generally applicable results that can be
extended to other PIDING applications. Future inves-
tigations will use in-cylinder imaging and measurement
of local NG concentration to improve the characteriza-
tion of the NG stratification, pilot-NG interactions,
and the description of the combustion processes for
each identified combustion regime. This information
will guide the design of future detailed experimental
investigation, numerical simulation, and hardware
design for high efficiency, low-emissions stratified
PIDING engines.
Acknowledgements
The author(s) would like to acknowledge the technical and
financial support provided by Westport Fuel Systems, Inc.
The technical support and contributions of Drs. Sandeep
Munshi, Steve Rogak, and fellow researchers at The
University of British Columbias Clean Energy Research
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
(no. 32637), and the NSERC Discovery Grant Program
(RGPIN 418700-13).
ORCID iDs
Jeremy Rochussen https://orcid.org/0000-0002-7098-2340
Gordon McTaggart-Cowan https://orcid.org/0000-0001-
9784-6456
Patrick Kirchen
https://orcid.org/0000-0002-1154-8923
References
1. Intergovernmental Panel on Climate Change. Climate
change 2014:m itigation ofclimatechange: Workinggroup III
contribution to the IPCCfifth assessmentreport.C a m b r i d g e ,
UK and New York, NY: Cambridge University Press, 2015.
2. IEA. World energy outlook 2019. 2019.
3. Ouelette P, Goudie D and McTaggart-Cowan G. Prog-
ress in the development of natural gas high pressure
direct injection for euro vi heavy-duty trucks. In: Liebl J
and Beidl C (eds) Internationaler Motorenkongress 2016 .
Wiesbaden, Germany: Springer, 2016, pp.591–607.
4. Harrington J, Munshi SR, Nedelcu C, et al. Direct injec-
tion of natural gas in a heavy-duty diesel engine. SAE
2002-01-1630, 2002.
5. Papagiannakis RG, Rakopoulos CD, Hountalas DT and
Rakopoulos DC. Emission characteristics of high speed,
dual fuel, compression ignition engine operating in a
wide range of natural gas/diesel fuel proportions. Fuel
2010; 89(7): 1397–1406.
6. Besch MC, Israel J, Thiruvengadam A, Kappanna H
and Carder D. Emissions characterization from different
technology heavy-duty engines retrofitted for CNG/die-
sel dual-fuel operation. SAE Int J Engines 2015; 8(3):
1342–1358.
7. Stettler ME, Midgley WJ, Swanson JJ, Cebon D and
Boies AM. Greenhouse Gas and NO
Xious emissions
from dual fuel diesel and natural Gas heavy goods vehi-
cles. Environ Sci Technol 2016; 50(4): 2018–2026.
8. Ko¨nigsson F, Kuyper J, Stalhammar P and Angstrom
HE. The influence of crevices on hydrocarbon emissions
from a diesel-methane dual fuel engine. SAE Int J
Engines 2013; 6(2): 751–765.
9. Nieman DE, Morris AP, Miwa JT, et al. Methods of
improving combustion efficiency in a high-efficiency,
lean burn dual-fuel heavy-duty engine. SAE 2019-01-
0032, 2019.
10. Fansler TD, Reuss DL, Sick V and Dahms RN. Invited
review: combustion instability in spray-guided stratified-
charge engines: a review. Int J Engine Res 2015; 16(3):
260–305.
11. McTaggart-Cowan GP. Pollutant formation in a gaseous-
fuelled, direct injection engine . PhD Thesis, University of
British Columbia, 2006.
12. Rochussen J, McTaggart-Cowan G and Kirchen P. Para-
metric study of pilot-ignited direct-injection natural gas
combustion in an optically accessible heavy-duty engine.
Int J Engine Res 2020; 21: 497–513.
282 International J of Engine Research 24(2)

<!-- PDF_PAGE: 19 -->

13. Faghani E, Kheirkhah P, Mabson C, et al. Effect of injec-
tion strategies on emissions from a pilot-ignited direct-
injection natural-gas engine-part ii: slightly premixed
combustion. SAE Technical Paper 2017-01- 0744, 2017.
14. McTaggart-Cowan GP, Bushe WK, Rogak SN, Hill PG
and Munshi SR. Injection parameter effects on a direct
injected, pilot ignited, heavy duty natural gas engine with
EGR. SAE 2003-01-3089, 2003.
15. McTaggart-Cowan GP, Bushe WK, Rogak SN, et al.
PM and NO X reduction by injection parameter altera-
tions in a direct injected, pilot ignited, heavy duty natural
gas engine with EGR at various operating conditions.
SAE 2005-01-1733, 2005.
16. Florea R, Neely GD, Miwa J, et al. Efficiency and emis-
sions characteristics of partially premixed dual-fuel com-
bustion by Co-direct injection of NG and diesel fuel
(DI
2). SAE Technical Paper 2016-01-0779, 2016.
17. Neely GD, Florea R, Miwa J, et al. Efficiency and emis-
sions characteristics of partially premixed dual-fuel com-
bustion by Co-direct injection of NG and diesel fuel (DI 2)
– part 2. SAE 2017-01-0776, 2017.
18. Li M, Zheng X, Zhang Q, Li Z, Shen B and Liu X. The
effects of partially premixed combustion mode on the per-
formance and emissions of a direct injection natural gas
engine. Fuel 2019; 250: 218–234.
19. Khosravi M, McTaggart-Cowan G and Kirchen P. Pyro-
metric imaging of soot processes in a pilot ignited direct
injected natural gas engine. Int J Engine Res 2021; 22:
1605–1623.
20. Yadollahi B and Boroomand M. The effect of piston
head geometry on natural gas direct injection and mixture
formation in a si engine with centrally mounted single-
hole injector. SAE 2011-01-2448, 2011.
21. Baratta M and Rapetto N. Mixture formation analysis in
a direct-injection ng si engine under different injection
timings. Fuel 2015; 159: 675–688.
22. Munshi S, McTaggart-Cowan G, Huang J, et al. Devel-
opment of a partially-premixed combustion strategy for a
low-emission, direct injection high efficiency natural gas
engine. In Proceedings of the AMSE 2011 internal com-
bustion engine division fall technical conference . Morgan-
town, West Virgina, October 2–5, 2011
23. Kim T, Song J and Park S. Effects of turbulence enhance-
ment on combustion process using a double injection
strategy in direct-injection spark-ignition (DISI) gasoline
engines. Int J Heat Fluid Flow 2015; 56: 124–136.
24. Chiodi M, Berner HJ and Bargende M. Investigation on
different injection strategies in a direct-injected turbo-
charged CNG-engine. SAE 2006-01-3000, 2006.
25. Zoldak P and Naber J. Spark ignited direct injection nat-
ural gas combustion in a heavy duty single cylinder test
engine-start of injection and spark timing effects. SAE
2015-01-2813, 2015.
26. Zeng K, Huang Z, Liu B, et al. Combustion characteris-
tics of a direct-injection natural gas engine under various
fuel injection timings. Appl Therm Eng 2006; 26(8-9):
806–813.
27. Li G, Ouellette P, Dumitrescu S, et al. Optimization
study of pilot-ignited natural Gas direct-injection in die-
sel engines. SAE 1999-01-3556, 1999.
28. Fink G, Jud M and Sattelmayer T. Influence of the spa-
tial and temporal interaction between diesel pilot and
directly injected natural gas jet on ignition and
combustion characteristics. J Eng Gas Turbine Power
2018; 140(10): pp.102811-1–102811-8.
29. Fink G, Jud M and Sattelmayer T. Fundamental study
of diesel-piloted natural gas direct injection under differ-
ent operating conditions. J Eng Gas Turbine Power 2019;
141(9): pp.091006-1–091006-8.
30. Rochussen J. Characterizing regimes of stratified pilot-
ignited direct-injection natural Gas combustion in an
optically-accessible engine . PhD Thesis, University of
British Columbia, 2021.
31. Liu Z and Karim GA. An examination of the ignition
delay period in gas-fueled diesel engines. J Eng Gas Tur-
bine Power 1998; 120(1): 225–231.
32. Glassman I, Yetter RA and Glumac NG. Combustion.
Waltham, MA; San Diego, CA; London, UK; Oxford,
UK: Academic Press, 2014.
33. Karim GA. Combustion in gas fueled compression: igni-
tion engines of the dual fuel type. J Eng Gas Turbine
Power 2003; 125(3): 827–836.
34. Heywood JB. Internal combustion engine fundamentals .
New York; Chicago; San Francisco; Athens; London;
Madrid; Mexico City; Milan; New Delhi; Singapore; Syd-
ney; Toronto: McGraw-Hill Education, 2018.
Appendix 1
Notation
T erm Description
D(tign) Difference in ignition delay
hi, g Gross indicated thermal efficiency
f Equivalence ratio
fg Global equivalence ratio
fNG NG equivalence ratio
fdiesel Diesel equivalence ratio
uPcyl, max Crank angle of max. cylinder pressure
uSOC, NG Crank angle of start of NG premixed
combustion
tign Ignition delay
tNG NG residence time
A
F Air-Fuel ratio
AHRR Apparent Heat Release Rate
aTDC After T op Dead Center
CAD Crank Angle Degree
CA
10/C0 90% Crank angle duration for 10-90% burn
fraction
CI Compression Ignition
COV Coefficient of Variance
CCV Cycle-to-Cycle Variability
DI Direct Injection
DI2 Co-Direct Injection
DISI Direct Injection Spark Ignition
DLSR Dome-Loaded Self-relieving Regulator
ECU Engine Control Unit
EGR Exhaust Gas Recirculation
EOING NG End of Injection
fpremix Mass fraction of NG that premixes prior
to combustion
f
premix, min Minimum f premix (for a given nominal
operating condition)
GHG Green House Gas
HDV Heavy-duty vehicle
(continued)
Rochussen et al. 283

<!-- PDF_PAGE: 20 -->

Appendix 2
Calculation of uSOC, NG
In this work, the phasing of the start of premixed NG
combustion, uSOC, NG, is calculated as the phasing at
which the derivative of AHRR reaches 20% of its max-
imum value:
uSOC, NG = ujAHRR =0 :2/C1 max(AHRR) ð8Þ
The threshold of 20% of dAHRR/d u was selected
to match previously published work, which used in-
cylinder imaging of OH*-chemiluminescence to identify
the start of premixed NG combustion for non-premixed
PIDING engine operation.
12 However, in the current
work, a much more diverse range of combustion modes
were explored, resulting in very different AHRR
shapes. For the wide variety of AHRR shapes mea-
sured, the 20% threshold was observed to provide more
robust characterization of the start of premixed NG
combustion than inflection methods. The calculation
method for u
SOC, NG used in the current work is pre-
sented graphically for AHRR measurements from each
of the six identified regimes of PIDING combustion in
Figure 15.
In Figure 15, the dashed blue line indicates the 20%
of dAHRR/d u threshold, the dotted black line indi-
cates the phasing (i.e. u) where the 20% of dAHRR/d u
is met prior to maximum dAHRR/d u, and the black
dot indicates the AHRR magnitude at the calculated
uSOC, NG.
Appendix 3
Mean cylinder temperatures for regimes of PIDING
combustion
The mean cylinder temperature was calculated assum-
ing ideal gas properties and no heat or mass transfer
during the compression and combustion processes.
Sample results of these calculations are presented in
Figure 16 for operating conditions representative of
each of the six identified regimes of PIDING
combustion.
Continued
T erm Description
HPDI High Pressure Direct Injection
IMEP Indicated Mean Effective Pressure
mair, NG, diesel Mass of air , NG, or diesel
NG Natural Gas
Pcyl Cylinder pressure
Pinj Injection pressure (diesel rail pressure)
Pintake Intake pressure
PI Pilot Ignition
PIDING Pilot-Ignited Direct-Injection Natural Gas
PM Particulate Matter
RCCI Reactivity Controlled Compression
Ignition
RCEM Rapid Compression-Expansion Machine
RoPR Rate of Pressure Rise
RIT Relative Injection Timing
RIT
/C3 Normalized RIT
RITcrit Critical RIT where tNG = f(RIT)
RITinsens: RIT where combustion and emission
become insensitive to RIT
SI Spark Ignition
SOING NG Start of Injection
SOIpilot Pilot Start of Injection
SPC Slight Premixed Combustion
TKE T urbulent Kinetic Energy
Tmix Charge mixture temperature
uHC Unburned Hydrocarbon
WFS Westport Fuel Systems
Figure 15. Sample calculations of uSOC, NG for AHRR data
representative of each of the six identified regimes of PIDING
combustion. u
SOC, NG calculated as the phasing where the slope
of AHRR reaches 20% of its maximum value.
284 International J of Engine Research 24(2)

<!-- PDF_PAGE: 21 -->

Figure 16. Mean cylinder temperature for operating conditions
representative of all six regimes of PIDING combustion.
Rochussen et al. 285
