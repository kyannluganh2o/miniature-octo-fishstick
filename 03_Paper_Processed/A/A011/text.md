<!-- PDF_PAGE: 1 -->

Standard Article
International J of Engine Research
2020, V ol. 21(3) 497–513
/C211IMechE 2019
Article reuse guidelines:
sagepub.com/journals-permissions
DOI: 10.1177/1468087419836877
journals.sagepub.com/home/jer
Parametric study of pilot-ignited
direct-injection natural gas combustion
in an optically accessible heavy-duty
engine
Jeremy Rochussen1
 , Gordon McT aggart-Cowan2
and Patrick Kirchen1
Abstract
Natural gas is an attractive fuel for internal combustion engines in light of its potential for reduced greenhouse gas and
particulate emissions, and significant reserves. T o facilitate natural gas use in compression ignition engines, pilot-ignited
direct-injection natural gas combustion uses a small pilot injection of diesel to ignite a more significant direct injection of
natural gas. Compared to modern diesel combustion, this strategy is a promising technology for the reduction of CO
2
emissions while retaining diesel-like efficiency without a significant CH 4 emission penalty. T o further develop this technol-
ogy, investigation of in-cylinder combustion processes is needed to identify the primary fuel conversion processes. The
objective of this work was to provide a framework of conceptual understanding by identifying key processes in a typical
pilot-ignited direct-injection natural gas combustion event and characterizing their sensitivity to fuel injection para-
meters. A parametric sweep of injection pressure, natural gas injection duration, and relative timing of the diesel pilot
and natural gas injections was performed in an optically accessible 2 L single-cylinder engine. Combined heat release rate
and OH*-chemiluminescence reaction zone analysis was used to demarcate the transition from ignition reactions to pri-
mary natural gas heat release. Five distinct combustion processes were identified: (1) pilot auto-ignition; (2) natural gas
ignition; (3) rapid, distributed partially premixed natural gas combustion; (4) non-premixed combustion; and (5) late-
cycle oxidation. While natural gas ignition was found to be insensitive to injection pressure, it was strongly affected by
the time between pilot and natural gas injections. Reducing the relative injection timing from + 8/C176to 26/C176resulted in
the primary natural gas heat release transitioning from non-premixed, to distributed partially premixed, to stratified pre-
mixed flame propagation as a result of increasing natural gas premixing. The presented measurements and analysis serve
to refine an initial conceptual model of the combustion process and lay the groundwork for future, more focused studies
of pilot-ignited, direct-injection natural gas combustion.
Keywords
Natural gas, optical engine, gas direct injection, pilot ignition, chemiluminescence
Date received: 3 January 2019; accepted: 14 February 2019
Introduction
The global transportation sector accounts for 28% of
end-user energy consumption, with on-road heavy-duty
vehicles (HDVs) responsible for one-quarter of green-
house gas (GHG) emissions from this sector.
1 By the
year 2050, the energy use by on-road HDVs is projected
to increase by 50% over 2006 demands.
2 It is therefore
crucial to develop propulsion technologies that can
reduce GHGs and gain significant market penetration
in the HDV sector.
One approach to reduce GHG emissions is through
fuel carbon intensity reduction by implementing fuels
that produce less CO
2. Natural gas (NG) is composed
primarily of CH 4, which can result in up to 25% lower
CO2 emissions, compared with conventional fuels such
as diesel. NG has also demonstrated the potential to
1Department of Mechanical Engineering, The University of British
Columbia, Vancouver , BC, Canada
2Westport Fuel Systems Inc, Vancouver , BC, Canada
Corresponding author:
Patrick Kirchen, Department of Mechanical Engineering, The University
of British Columbia, Vancouver , BC V6T 1Z4, Canada.
Email: pkirchen@mech.ubc.ca

<!-- PDF_PAGE: 2 -->

reduce other harmful emissions such as particulate mat-
ter (PM) and NO x in commercial HDV applications. 3,4
Life-cycle analysis suggests a net reduction of GHG
emissions of 10%–15% is realistic for HDVs where die-
sel is replaced by NG.
1 This benefit, however, can be
lost if there are significant CH 4 emissions, due to the
high global warming potential of CH 4.1 Premixed NG
(i.e. port-injected), diesel pilot-ignited engines can have
substantial CH
4 emissions, particularly at low loads
and low diesel energy ratios. 5 In-use studies of such
premixed compression ignition systems (commonly
referred to as dual-fuel) indicated a net increase in the
GHG emissions. 6,7 For these premixed combustion
strategies, the most significant sources of CH 4 emis-
sions are considered to be the lean premixed charge
trapped in crevice volumes not being oxidized, wall
quenching, and bulk quenching arising from insuffi-
cient flame speeds.
8
As an alternative to premixed systems, pilot-ignited
direct-injection NG combustion provides diesel-like
efficiency and significantly lowers CH
4 emissions rela-
tive to premixed systems. 3,9 A small pilot injection of
diesel is used to ignite a late-cycle direct injection of
NG, which provides approximately 95% of the total
energy. This combustion strategy takes advantage of
the emissions reduction potential of NG combustion
while retaining the performance of conventional diesel
internal combustion engines.
The existing understanding of the in-cylinder pro-
cesses for pilot-ignited direct-injection NG combustion
draw on numerical simulation,
10–12 expansion of analy-
tical works, 13 and extension of conventional direct-
injection diesel investigations. 14 Numerous experimen-
tal works utilizing conventional metal (i.e. non-optical)
engines targeting specific control parameters have also
been performed.
15–18 To date, only a single investiga-
tion has been published applying in-cylinder imaging to
pilot-ignited direct-injection NG combustion. 10 There,
one load and fuel injection strategy were considered.
For further development of this technology, the fuel
conversion modes and the impacts of the injection con-
trol parameters must be assessed.
Current conceptual description
Although not comprehensively outlined elsewhere, the
overall features of the combustion process have been
proposed in several works. The first event is the small
diesel pilot injection ( ’5% of total fuel on an energy
basis), which is characterized as a ‘‘puff’’ jet that auto-
ignites and burns in a premixed manner.
10 High-pres-
sure NG subsequently enters the combustion chamber
as an under-expanded jet, which adjusts to the cylinder
conditions through a barrel shock. 11 Ignition of each
NG jet results from its interaction with the pilot reac-
tion zone. Numerical simulation and non-optical
engine measurements have suggested that the spatial
and temporal location of the pilot products relative to
the NG jet has a strong influence on the NG ignition
process
18 and ultimately emissions, efficiency, and com-
bustion variability. 12,19 However, the sensitivity of
direct-injection NG combustion to the pilot combus-
tion has yet to be demonstrated with in-cylinder optical
measurements.
The NG ignition process is sensitive to many para-
meters, including injection pressure ( P
inj), relative injec-
tion timing (RIT), the geometric angle between pilot
and NG jets, and the bulk charge motion (i.e. swirl).
Based on numerical simulations, ignition of the gas jet
is considered to typically occur along the sides of the
quasi-steady gas jet, followed by a flame propagation
process around the premixed periphery of the jet.
12,18
Conversely, recent in-cylinder imaging suggests that
under certain conditions, ignition of the NG occurs
near the head of the jet and then proceeds to the sides
of the jet.
10 In either case, some of the NG will mix
with air prior to ignition, and hence some flame propa-
gation through a partially premixed mixture is likely. It
has previously been suggested that a higher peak heat
release rate (HRR) indicates a greater degree of NG
premixing, which has been noted to significantly impact
engine performance.
15,17,20
Once the premixed NG is consumed, a non-premixed
turbulent jet flame forms and the HRR is governed by
the fuel injection. As in diesel combustion, increased
gas injection pressure has demonstrated advantages in
efficiency, PM, and CO emissions for pilot-ignited
direct-injection NG engines.
21 Experimental and
numerical investigations have shown that if injection
pressure is too low, the reduced fuel and oxidizer mix-
ing rates lead to slow combustion, emissions of incom-
plete combustion products, and low efficiency. If
injection pressure is too high, the jet may over-pene-
trate, causing significant wall quenching of the NG jet
flame.
12,19 It is unclear, for the given engine operating
conditions, when under- or over-mixing of the NG jet
occurs or how to characterize the degree of mixing.
What is evident, however, is the strong sensitivity of
direct-injection NG combustion to the injection control
parameters.
A more comprehensive conceptual description of
pilot-ignited direct-injection NG combustion is needed
to support and connect existing knowledge and to fur-
ther develop upon it. In particular, the modes of fuel
conversion (partially premixed, non-premixed, flame
propagation, and combinations thereof) need to be
identified and characterized to support future assess-
ment of pollutant formation mechanisms and to iden-
tify opportunities for further optimization.
The objective of this work was to survey and pro-
vide an initial characterization of the different combus-
tion processes in direct-injection NG combustion. To
this end, in-cylinder imaging was performed for varia-
tions of injection parameters. Identification of phenom-
ena common to all considered operating conditions is
used to identify characteristic features of the combus-
tion process and to characterize the sensitivity of the
fuel conversion processes to the considered fuelling
498 International J of Engine Research 21(3)

<!-- PDF_PAGE: 3 -->

parameters. This exploratory investigation is intended
to provide a framework that can be refined in future,
detailed characterizations of this combustion process.
Experimental facility and method
The experimental facility used in this investigation is
based on a 2.0-L, single-cylinder, optically accessible
Ricardo Proteus engine, the specifications of which are
given in Table 1. Further details can be found in previ-
ous works.
22–24 This facility is designed to operate in
either an optically accessible configuration with a
Bowditch piston and quartz window or in a conven-
tional all-metal configuration (thermodynamic config-
uration). In the thermodynamic configuration, the
engine is continuously fired, permitting measurement
of fuel and air flow rates, exhaust emissions, and brake
torque. In the optical configuration, the engine is oper-
ated in a skip-fired mode to prevent over-heating of the
quartz window. Details of the optical engine configura-
tion are presented in Figure 1.
To allow optical access by means of a large quartz
window, the Bowditch piston features a flat-bottomed
cylindrical piston bowl, which is offset by 4 mm from
the cylinder axis. The Bowditch piston bowl differs
from the toroidal bowl in the all-metal piston and is
T able 1. Engine specifications.
Parameter Thermodynamic Optical
Displacement (L) 2.0 2.0
Bore (mm) 130 130
Stroke (mm) 150 150
Compression ratio (–) 13.0:1 12.6:1
Maximum speed (r/min) 2100 1200
Maximum P
cyl (bar) 170 110
Piston bowl shape Eccentric toroid Eccentric cylinder
Tintake (/C176C) 28 52
Pintake (bar g) 0.92 1.0
Swirl number 0.1 0.1
Direct injector First-generation Westport HPDI
Pilot fuel Pump diesel (ULSD)
Primary fuel Natural gas ( ’95% CH
4)
ULSD: ultra-low-sulfur diesel; HPDI: high-pressure direct injection.
Figure 1. Optically accessible configuration of single-cylinder research engine facility.
Rochussen et al. 499

<!-- PDF_PAGE: 4 -->

expected to affect jet impingement and fluid flow pat-
terns. The impact of the differences in bowl shape on
the combustion processes is challenging to assess, but
will be the focus of future work employing in-cylinder
optical probe diagnostics.
25,26 In the current work, the
HRR for the optical and thermodynamic engine con-
figurations was found to be in good agreement with
one another for the considered operating conditions.
The Bowditch piston also produces a slightly lower
compression ratio (CR) than the all-metal piston (all-
metal CR = 13.0:1, Bowditch = 12.6:1), which necessi-
tates an increase in the intake charge temperature (all-
metal T
intake =2 8 /C176C, optical Tintake =5 2 /C176C) to match
the thermodynamic pilot ignition delay. As the intake
charge density was affected by changes in temperature,
the intake manifold pressure was adjusted (all-metal
P
intake = 0.92 bar g, optical Pintake =
1.00 bar g) to maintain cylinder charge mass and
equivalence ratio, F. In the current investigation, direct
injection of diesel and NG is performed via a develop-
mental version of a first-generation Westport High-
Pressure Direct Injection (HPDI) injector. Note that no
other aspects of the experimental facility were opti-
mized for the Westport HPDI fuel system (e.g. piston
bowl, CR, valve timing). In particular, the CR is low,
which will impact combustion processes such as the
diesel ignition delay.
In the optical configuration, two imaging systems
are used to simultaneously capture (1) OH*-chemilumi-
nescence (OH*-CL) at 307 nm and (2) natural luminos-
ity (NL) at 700 nm. The details of the imaging system
are provided in Table 2.
OH*-CL occurs as an electronically excited OH rad-
ical (OH*) relaxes to its ground state and emits a
photon, typically as a result of collisional quenching.
The formation of the excited radical is considered to
primarily occur via two reactions:
27
CH + O2 ! OH/C3 +C O ð1Þ
H+O+M ! OH/C3 +M ð2Þ
The OH radical is an important chemical species for
decomposition of fuel molecules and is commonly used
as a measure of local heat release in premixed flames
(i.e. Reaction 1) and as an early marker of ignition.
10,27
In addition to the concentration of OH, however, the
OH*-CL signal intensity is also sensitive to pressure,
F, and temperature for CH
4 flames at relevant cylinder
conditions (increasing OH*-CL intensity with decreas-
ing pressure, increasing F, or increasing tempera-
ture).
27,28 OH*-CL is also present in the burned gas
regions due to the recombination of H and O atoms at
elevated temperatures, particularly for lean combustion
where there is a higher concentration of O in the com-
bustion products (Reaction 2).
27 The dependence of
OH*-CL intensity on T, P, and F in non-premixed sys-
tems has less experimental characterization in the liter-
ature, due largely to interference from broadband soot
incandescence. However, numerical simulation indi-
cates the same strong dependence of OH*-CL on tem-
perature exists for non-premixed combustion, which
supports the use of OH*-CL as a marker for non-
premixed reaction fronts.
29 In the current work, OH*-
CL is used to qualitatively characterize the spatial dis-
tribution and intensity of high-temperature reaction
zones of premixed, partially premixed, and non-
premixed combustion.
The NL is expected to be dominated by soot incan-
descence and is only considered in the current work to
aid in interpretation of OH*-CL images, where there is
the possibility of soot attenuating the OH*-CL signal.
Specifications of the OH*-CL and NL imaging systems
are presented in Table 2.
In the optical configuration, the engine was operated
in a skip-fired mode consisting of three consecutive fired
cycles followed by 17 motored cycles (no combustion)
to allow the window to cool. Images were recorded on
the third fired cycle as there were no significant differ-
ences in HRR between the third and subsequent fired
cycles during thermodynamic testing. The images and
HRR presented in the current work are ensemble aver-
aged from a set of 15 skip-firing sequences (i.e. 15
imaged cycles). Imaging system parameters were fixed
for all measurements; therefore, pixel intensities are
comparable across all figures (note that color scales are
adjusted between figures to improve contrast, so colors
are not directly comparable between figures).
OH*-CL and NL imaging are line-of-sight methods,
and although it is not possible to infer variations along
the optical path, they do provide an indication of the
approximate position and intensity of the reaction
zone. A related source of uncertainty is light absorption
by soot along the optical path. In the current work,
soot has been noted to attenuate OH*-CL and intro-
duce uncertainty in the interpretation of OH*-CL sig-
nals for operating conditions with significant soot.
T able 2. Imaging system specifications.
Parameter OH *-CL imaging system
Camera Photron SA-1 high-speed CMOS
Image intensifier LaVision high-speed IRO
Lens Cerco 98 mm f/2.8 UV
Aperture f/5.6
Camera exposure 84 ms
Intensifier gating 10 ms
Frame rate 12,000 Hz
Resolution 430 3 430
Interference filter 307 nm CWL, 20 nm FWHM
NL imaging system
Camera Phantom v7.1 CMOS
Lens 60 mm f/2.8 Micro-Nikkor
Exposure 8–72 ms with f/5.6
Frame Rate 12,000 Hz
Resolution 166 3 166
Narrow band-pass filter 700 nm CWL, 10 nm FWHM
NL: natural luminosity; CWL: central wavelength; FWHM: full width at
half maximum.
500 International J of Engine Research 21(3)

<!-- PDF_PAGE: 5 -->

Engine operating conditions producing higher concen-
trations of soot tend to foul the window and attenuate
both NL and OH*-CL signals across the entire cycle.
To mitigate this effect, the window was cleaned after
every 15 imaged cycles. The limited dynamic range of
the imaging system requires a compromise in providing
detection of the ignition processes while still providing
an appropriate exposure for the remainder of the cycle.
The considered operating conditions were identified
using the thermodynamic engine configuration under
steady state operating conditions. These measurements
established appropriate engine control settings (i.e.
intake temperature and pressure, pilot injection timing
and duration, and NG injection timing and duration)
for the skip-fired optical measurements, as well as mea-
surement of air and fuel flow rates.
A datum operating condition was selected to be rep-
resentative of a medium-load operating condition. The
start of the diesel pilot and NG injections (pilot start of
injection (PSOI) and gas start of injection (GSOI),
respectively) were selected such that NG injection con-
tinues after the NG ignition, presumably resulting in a
quasi-steady, non-premixed jet flame similar to mid-
and high-load diesel combustion. Variations of injec-
tion pressure ( P
inj), commanded gas pulse width
(GPW), and the relative timing of the pilot and NG
injection events (RIT = PSOI – GSOI) were performed
based on the datum operating condition. Reported
injection pressures ( P
inj) correspond to the diesel rail
pressure. For all operating conditions, the NG injection
pressure was set to 10 bar below the diesel injection
pressure using a dome-loaded regulator. The consid-
ered control settings are given in Table 3. All measure-
ments were performed at 1000 r/min.
Datum operating condition and key
features
To identify the influence of the considered injection
parameters, the OH*-CL, NL, and HRR are first con-
sidered for a datum operating condition. Subsequently,
the influence of P
inj, GPW, and RIT on pilot and NG
ignition processes and the primary combustion pro-
cesses are discussed.
Datum condition
The datum operating condition is a medium-load
(11.5 bar GIMEP (gross indicated mean effective pres-
sure)) operating condition with typical injection timings
(see Table 3) and is considered as a baseline against
which the effects of injection parameters can be evalu-
ated. The OH*, NL, and HRR for the datum operating
condition are shown in Figure 2. After the diesel pilot
injection and ignition, an annular OH* cloud associ-
ated with a small heat release is apparent in the piston
bowl. The short pilot injection (0.7 ms) results in low-
momentum ‘‘puff’’ jets, which do not penetrate to the
piston bowl walls and remain in the central region of
the bowl.
The NG injection starts during the diesel heat
release, and the NG is ignited by the pilot combustion
products. Shortly before top dead center (TDC), the
NG ignition is apparent as an increase in the HRR and
an increase in OH*-CL intensity. A pilot-only operat-
ing condition (no NG injection) confirmed that HRR
following the minimum at ;–3/C176aTDC (after top dead
center) is due to the ignition of NG. The extent of the
reaction zone indicated by OH* does not change at the
start of NG ignition, indicating these reactions likely
take place within the existing region of high OH*. At
approximately 1/C176aTDC, the detected OH* reaches the
piston bowl wall and the HRR increases more rapidly.
In previous work, an in-cylinder infrared absorption
probe was used to characterize the NG jet penetration
for similar operating conditions with the same injector
hardware.
25,26 There, an increase in the CH 4 concentra-
tion was detected at the firedeck near the bowl wall
before the fuel was oxidized. This indicates that some
of the NG penetrates past the pilot combustion prod-
ucts and partially premixes prior to reacting.
At the HRR peak (3 /C176aTDC), the OH*-CL intensity
and coverage have increased rapidly around the NG
T able 3. Considered engine operating conditions.
Pinj sweep Relative injection timing sweep GPW sweep
Parameter Low Pinj Datum High Pinj Negative RIT Short RIT Datum Long RIT Short GPW Datum Long GPW
fNG (–) 0.5 6 0.01 0.5 6 0.01 0.23 0.5 0.67
GIMEP (bar) 11.5 6 0.3 11.5 6 0.3 5.3 11.5 14.2
CA50 (/C176aTDC) 6.7 6 0.3 6.7 6 0.3 + 3.3 + 6.7 + 8.7
Pinj (MPa) 14.0 18.0 22.0 18.0 18.0
PSOI (/C176aTDC) 222 218 216 216 211 218 224 218
PPW (ms) 1.0 0.7 0.6 0.7 0.7
GSOI (/C176aTDC) 214 210 28 222 29 210 210 210
GPW (ms) 2.1 1.45 1.2 1.45 1.05 1.45 1.85
RIT (/C176CA) 12 8 8 262 8 1 4
RIT: relative injection timing; GPW: gas pulse width; GSOI: gas start of injection; PSOI: pilot start of injection; aTDC: after top dead center; PPW:
pilot pulse width; GIMEP: gross indicated mean effective pressure.
Rochussen et al. 501

<!-- PDF_PAGE: 6 -->

jets and near the bowl wall. This is attributed to a dis-
tributed, multi-point conversion of the partially pre-
mixed charge. The OH* also spreads toward the
injector and remains anchored a short distance down-
stream of the injector orifices for the remainder of the
NG injection. This quasi-steady reaction zone indicates
the presence of non-premixed combustion processes.
Later in the cycle, the highest intensity regions of NL
are observed at the bowl wall where the NG jets
impinge. It is likely that this strong NL signal is an
indication of soot in the core of the NG jet, similar to
soot formation for diesel combustion.
14 Characteristics
of the soot formation region in the core of the imping-
ing jet will be sensitive to the unconventional geometry
(cylindrical bowl) and relatively cold piston surfaces.
During injector closing, the NG injection rate
decreases until approximately 6 /C176aTDC, at which point
the NL signal near the bowl wall becomes substantially
more intense, indicating a higher soot concentration
and/or hotter soot is present. After the end of injection
(EOI), the NL signal decreases and the OH*-CL signal
increases. Late in the cycle, the most intense OH*
remains near the bowl wall, indicating the location of
late-cycle oxidation reactions.
As stated previously, attenuation of OH*-CL by
soot introduces uncertainty to the OH*-CL measure-
ments. In the remainder of this discussion, only the
OH*-CL images are presented; however, the corre-
sponding NL images are supplied in Appendix 3 for
reference. A detailed discussion of the soot formation
and oxidation processes will be the focus of subsequent
investigations.
Stages of pilot-ignited direct-injection NG combustion
To better assess the multiple simultaneous processes,
the combustion event is considered here in separate
phases. The effects of injection parameters are consid-
ered for (1) the diesel combustion and NG ignition, and
(2) primary NG combustion. The pilot combustion and
NG ignition (stage 1) starts at pilot ignition ( u
ign, pilot)
uign, pilot = u HRR . 5 J
CAD /C1 m3
/C18/C19
ð3Þ
The start of primary NG combustion ( uSOC, NG)i s
considered to be the increase in HRR caused by the dis-
tributed combustion of partially premixed NG. Here,
u
SOC, NG is identified by the inflection point in the HRR
uSOC, NG = u d2HRR
dt2
/C12/C12/C12/C12
umaxHRR
PSOI
=0
 !
ð4Þ
When more than one u satisfies equation (4), the
inflection point closest to the maximum HRR
(u
maxHRR) is chosen (see Appendix 2). The selected defi-
nition for uSOC, NG is supported by the OH*-CL analy-
sis of reaction zone growth rates later in the discussion.
The primary NG combustion (stage 2) also includes all
fuel conversion processes subsequent to the peak HRR.
The following discussion will consider the influence of
the injection parameters on the two fuel conversion
stages.
Pilot and NG ignition
Combustion begins with the auto-ignition of the diesel
pilot, which is similar to conventional diesel pilot injec-
tions. The effects of bulk charge properties ( T, P )o n
the pilot ignition delay are well understood from diesel
combustion; however, if very early NG injections are
considered, interaction of the NG jets with the pilot
combustion may affect the process. Conversely, the NG
ignition processes are unique to pilot-ignited direct-
injection NG strategies and result from the interaction
Figure 2. HRR, OH*-CL, and NL ensemble averaged images for datum operating condition. Colorbar ranges are referenced to the
dynamic range of the corresponding camera sensor. Overbars indicate the start of injection to commanded end of injection.
502 International J of Engine Research 21(3)

<!-- PDF_PAGE: 7 -->

of the NG jets with the pilot combustion products,
which is not well understood. To gain insight into the
ignition processes, the impacts of P
inj and RIT on the
pilot and NG ignition processes are investigated here.
Injection pressure
Increased injection pressure improves the atomization
and mixing of diesel with air and ultimately reduces the
diesel ignition delay.
30 In the current work, an
advanced pilot injection timing was used for lower Pinj
to maintain a constant crank angle of 50% integrated
heat release (CA 50), which will increase the pilot igni-
tion delay ( tign, pilot). The impact of increased Pinj on the
NG start of combustion ( uSOC, NG) is not immediately
clear. In previous non-optical investigations, reduced
NG ignition delays have been observed with increasing
Pinj.18,31 In the current investigation, the NG start of
combustion delay (tSOC, NG) is considered as the elapsed
time from the NG injector needle opening to the start
of primary NG combustion (i.e. uSOC, NG as defined in
equation (4), see Appendix 2). The pilot ignition delay
was defined as the elapsed time from pilot needle open-
ing to HRR . 5 J/CAD -m
3 (equation (3)). The diesel
and NG needle opening times were estimated based on
the command signals and Mie scattering imaging of
diesel droplets in the pilot spray and tracer diesel dro-
plets in the NG jet. The Mie scattering system used a
high-power LED light source and the high-speed NL
camera specified in Table 2. The injection delay esti-
mate does not account for changes in needle opening
dynamics, which are known to be sensitive to both
cylinder and fuel rail pressures. As shown in Figure 3,
t
SOC, NG has a similar sensitivity to injection pressure as
tign, pilot, despite having a very different ignition process.
To distinguish whether the NG ignition is acceler-
ated by increased Pinj or whether the reduced pilot igni-
tion delay has provided an ignition source earlier in the
cycle, the ignition process is considered relative to the
pilot ignition timing ( uign, pilot), and the HRR and OH*-
CL are referenced to the pilot ignition ( /C176aPI). As shown
in Figure 4, the HRR for all Pinj is very similar in mag-
nitude and phasing for the considered Pinj. To highlight
the start and end of the ignition processes, the portions
of HRR occurring before and after the defined bounds
for stage 1 are plotted with dotted lines. HRR and pres-
sure data are given with respect to TDC in Appendix 4.
Figure 3. Pilot ignition delay and NG start of combustion delay
for Pinj = 14, 18, and 22 MPa. Error bars represent the 95%
confidence interval. tign, pilot and tSOC, NG calculated using
equations (3) and (4), respectively.
Figure 4. HRR and ensemble averaged OH *-CL images of the ignition processes for Pinj = 14, 18, and 22 MPa. Overbars indicate
estimated NG injection duration until start of needle closing.
Rochussen et al. 503

<!-- PDF_PAGE: 8 -->

Despite similar HRR, Pinj does influence the reaction
zone structure, as indicated by OH*-CL. Increasing Pinj
resulted in higher intensity OH*-CL and greater pilot
reaction zone penetration (1–3 /C176aPI). The increase in
HRR at 3–4/C176aPI was due to NG ignition, as confirmed
by comparison with pilot-only operation (i.e. without
NG injection). Across all Pinj, the NG ignition is not
accompanied by a significant increase in the spatial cov-
erage of the OH*, indicating that NG ignition is taking
place in the same region as the pilot combustion.
Following NG ignition, the reaction zones travel
toward the bowl wall more rapidly for higher P
inj.
The effect of Pinj on the ignition zone structure was
considered using reaction zone growth rates evaluated
from the OH*-CL images. Reaction zone boundaries were
identified using a binary threshold (1% of sensor dynamic
range), and the displacement of the boundaries in subse-
quent frames was used to ca lculate the reaction zone
growth rate during ignition. Unlike homogeneous com-
bustion systems, a range of reaction zone conditions exist
due to heterogeneous temperature, fuel, and radical distri-
butions. Thus, the displacement calculation was per-
formed at every pixel along the reaction zone boundary to
provide a reaction zone growth rate distribution. Details
of this technique are provided elsewhere.
22 In Figure 5,
the reaction zone growth rate distribution is compared to
the HRR for the ignition processes. In general, a common
sequence is observed for all consideredP
inj:
1. From 0 to 1 /C176aPI, there is a high growth rate corre-
sponding to the multi-point pilot auto-ignition.
2. From 2 to 4 /C176aPI, the mean reaction zone growth
rates indicated by OH*-CL increase gradually from
approximately 5 to 10 m/s. During the same inter-
val, there is very little heat release and the peak
OH* intensity within the reaction zones (see Figure
4) decreases, indicating limited chemical activity.
3. From 4 to 6 /C176aPI, the OH*-CL intensity in the core
of the reaction zones begins to increase, and an
increase in HRR is observed; however, the mean
reaction zone growth rate remains constant during
this interval. The increased HRR and OH* indi-
cate the ignition of the NG by the hot pilot com-
bustion products. While it cannot be resolved from
the OH* imaging, this likely occurs around the
sides of the NG jets, as previously reported.
18
4. The start of the primary NG combustion (i.e.
uSOC, NG) is observed at 6 /C176aPI. At the same time, a
rapid increase in the mean reaction zone growth
rate is noted, which increases with increasing Pinj.
This is attributed to the rapid conversion of par-
tially premixed NG near the piston bowl wall
noted in Figure 2. The phasing of the increase in
reaction zone growth rate supports the selection of
the HRR inflection point (Equation (4)) to define
the start of primary NG combustion.
Relative injection timing
The relative timing of the diesel pilot and NG injections
can substantially affect the interaction of the NG jet
with pilot combustion products, as well as the degree
of NG premixing prior to ignition. To explore these
effects, a range of RIT was selected to include timings
where: (1) NG injection is completed prior to the diesel
pilot injection, (2) NG and diesel injections are overlap-
ping, and (3) the diesel injection is completed prior to
NG injection. The latter is approximately equivalent to
a diesel fueling strategy employing a pilot injection and
is considered to be a typical fuelling strategy for pilot-
ignited direct-injection NG.
Because the NG requires the diesel pilot as an igni-
tion source, a shorter RIT results in an increased
t
SOC, NG (shown in Figure 6, defined by equation (4))
and associated increase in NG premixing. tign, pilot
(defined by equation (3)) is also sensitive to RIT; how-
ever, this is due to the adjustment of the pilot injection
timing (PSOI) required to maintain a constant CA
50 for
all RIT (see Table 3). As would be expected for conven-
tional diesel combustion, the early PSOI (–24 /C176aTDC)
required for the long RIT (14 /C176) resulted in a longer
t
ign, pilot and reduced heat release due to pilot over-mix-
ing.32 Despite the weaker pilot combustion, there is rel-
atively little impact on tSOC, NG (Figure 6). The late
pilot injection timing for the RIT = 2 /C176condition
(PSOI = –11/C176aTDC) resulted in a reduced tign, pilot.
Operation with only a pilot injection (i.e. without NG
injection) confirmed that the change in PSOI for
RIT = 2/C176and 14 /C176was responsible for the different
Figure 5. HRR and distribution of reaction zone growth rates
during the ignition processes for Pinj= 14, 18, and 22 MPa.
504 International J of Engine Research 21(3)

<!-- PDF_PAGE: 9 -->

tign, pilot. For RIT = –6/C176, it is expected that there will be
partially premixed NG at the pilot ignition sites.
Although variability in tign, pilot increased, the mean
tign, pilot was similar for the datum and RIT = –6/C176condi-
tions. This indicates that the inhibiting effects of pre-
mixed NG on diesel ignition are different from those
widely observed for fully premixed pilot-ignited NG
combustion (i.e. dual-fuel),
33 where an increase in
tign, pilot would be expected.
The interaction between the diesel pilot and NG is
evident in Figure 7. For RIT = 8 /C176and 14 /C176, no signifi-
cant interaction is observed between the NG jets and
the pilot reaction zones. For RIT = 2 /C176and 26/C176,
however, the NG start of injection (SOI) is before the
pilot heat release, and some interaction is expected
between the NG jets and the pilot reaction zones. For
these RIT, the initial pilot reaction zone structures are
smaller, with lower intensity OH*-CL, and are located
closer to the injector than for the datum operating con-
dition (RIT = 8/C176). For RIT = 2 /C176, the OH* of the pilot
reaction zones is disturbed by the NG jets from 2 to 3 /C176
aPI. The initial pilot reaction zone growth rate is also
observed to be slower ( \ 35 m/s), as shown in Figure
8, and is followed by rapid reaction growth toward the
bowl wall and low HRR. The low HRR suggests lim-
ited fuel conversion occurs during the reaction zone
growth period (2–3 /C176aPI) and implies that advection of
pilot combustion products by the NG jets may also
transport heat and radicals to the bowl wall. At 4 /C176aPI,
the OH* reaches the bowl wall, and high HRR and
reaction zone growth rates occur due to the distributed
conversion of the partially premixed NG injected dur-
ing the longer t
SOC, NG.
The structure of the OH* during the pilot combus-
tion for RIT = –6 /C176is more homogeneous, with less
defined clouds compared to the other operating condi-
tions. The reaction zone growth proceeds in all direc-
tions rather than preferentially along the NG jet axes,
and the transition from pilot combustion to start of pri-
mary NG combustion is difficult to identify in both the
OH* images and HRR. These significantly different
ignition processes occur because the NG has been
injected into the cylinder prior to pilot ignition, produc-
ing a stratified, partially premixed charge. Despite lower
Figure 6. Pilot ignition and NG start of combustion delays for
RIT = –6/C176to + 14 /C176. Error bars represent 95% confidence
interval. tign, pilot and tSOC, NG calculated using equations (3) and
(4), respectively.
Figure 7. HRR and ensemble averaged OH *-CL images of the ignition processes for RIT = –6 /C176to + 14 /C176, with pilot ignition beginning
at 23.6/C176, + 0.2 /C176, 25.2/C176, and 28.5/C176, respectively. Dotted lines indicate the portion of HRR outside stage 1, and overbars indicate
estimated NG injection duration until start of needle closing. Note that for RIT = –6 /C176, NG injection has ended prior to pilot ignition.
Rochussen et al. 505

<!-- PDF_PAGE: 10 -->

HRR, the presence of premixed NG near the pilot auto-
ignition regions produces higher reaction zone growth
rates (50–68 m/s) than observed for other conditions.
After the initial ignition (and rapid reaction zone
growth), the reaction zone grows at a lower, but con-
stant rate ( ;10 m/s from 3 to 5 /C176aPI). At 6 /C176aPI, the
mean reaction zone growth rate increases from 10 to
25 m/s. Because the NG is partially premixed, the reac-
tion zone growth rate is defined by the local mixture
equivalence ratio, turbulence intensity, and tempera-
ture. These observations for RIT = –6 /C176share features
with the conceptual model of fully premixed dual-fuel
combustion proposed by Karim et al.,
34 where pilot
auto-ignition and combustion of NG entrained by the
pilot injection constitute the ignition processes, and are
followed by turbulent flame propagation through the
remainder of the premixed charge.
Primary NG combustion
Following the ignition of the NG jets, the remaining
fuel is converted during the primary NG combustion.
The manner in which this occurs is influenced by the
injection parameters. For the datum condition, the
momentum of the jets carries combustion products
from the pilot and NG ignition sites to the outside of
the combustion chamber where combustion of partially
premixed NG that has accumulated during t
SOC, NG
occurs. The HRR from the partially premixed combus-
tion is high and occurs while additional fuel and
momentum are injected, resulting in non-premixed
and/or partially premixed fuel conversion mechanisms.
The location, relative magnitude, and rate of partially
premixed and non-premixed processes are dictated pri-
marily by the NG injection pulse width (GPW), P
inj,
and RIT. To separate the primary NG heat release
from the ignition phenomena, presentation of OH* and
HRR are phased relative to the start of NG combus-
tion, u
SOC, NG (i.e. /C176aNGSOC, see section ‘‘Stages of
pilot-ignited direct-injection NG combustion’’). In the
previous section, this datum was shown to match the
phasing of a rapid increase in the reaction zone growth
rate indicated by OH*-CL, interpreted here as indicat-
ing the start of the primary NG combustion.
Injection duration
The commanded NG injection duration gas pulse width
(GPW), along with injection pressure, is used to control
the injected fuel quantity and load. To assess the influ-
ence of GPW on combustion, P
inj, PSOI, and GSOI
were held constant and the GPW was varied. Increasing
GPW resulted in higher GIMEP (corresponding to
increased F) and a more retarded combustion phasing
(see Table 2).
The partially premixed NG combustion is expected
to have a significant impact on NO
x emissions, which
have been shown to correlate with the peak HRR. 15,21
For GPW longer than tSOC, NG, increasing GPW
increases the fraction of energy released from the
quasi-steady portion of the jet flame (i.e. by non-
premixed combustion processes), but has little impact
on the partially premixed combustion heat release or
ignition processes. However, the peak HRR is affected
for shorter GPW. The ignition processes and start of
the partially premixed NG heat release up to
;2/C176aNGSOC are the same for all considered condi-
tions, as shown in Figure 9. At 2 /C176aNGSOC, the HRR
for the shortest injection duration (GPW = 1.05 ms)
decreases relative to the HRR for the longer injection
durations and ultimately results in a substantially lower
peak HRR. Furthermore, the quasi-steady NG jet reac-
tion zones (i.e. non-premixed combustion) do not
appear to stabilize near the injector, suggesting that
there is limited non-premixed fuel conversion. This
occurs because the NG needle starts to close (indicated
by the end of the black overbar in Figure 9) prior to
the peak HRR.
The reduced non-premixed combustion is expected
to reduce the production of soot, which agrees with the
lower NL intensity (see Appendix 3), and observations
of the soot formation regions in diesel combustion.
14
The reduced soot also implies reduced attenuation of
the OH*-CL for GPW = 1.05 ms, which has the high-
est intensity OH*-CL measured despite the lowest total
heat release.
The late-cycle HRR after the end of NG injection is
higher for longer GPW. Elsewhere, increased CO emis-
sions have been noted with increasing load, a well-
established effect of increasing the global equivalence
Figure 8. HRR and distribution of reaction zone growth rates
during the ignition processes for RIT = –6 /C176to + 8 /C176.
506 International J of Engine Research 21(3)

<!-- PDF_PAGE: 11 -->

ratio, F, because of reduced O 2 availability.35 For all
injection durations, late-cycle oxidation reactions indi-
cated by OH*-CL remain concentrated around the
bowl wall where the partially premixed combustion was
noted. The extent to which these reaction zones con-
tinue in the squish region (not visible through Bowditch
piston) is unknown.
Injection pressure
Similar to GPW, Pinj is used to control the injected fuel
mass and also impacts the partially premixed and non-
premixed combustion processes. Increasing P
inj will
increase fuel-oxidizer mixing rates, leading to higher
heat release during the non-premixed combustion pro-
cess and more rapid mixing of the partially premixed
portion of the charge. However, if P
inj is too high, over-
leaning and quenching of the partially premixed NG
may occur, resulting in increased CH
4 emissions and
reduced efficiency.18
The influence of Pinj on the primary combustion
phase is shown in Figure 10. For the range of consid-
ered P
inj, there is no significant impact on the HRR
before 2 /C176aNGSOC. At 2 /C176aNGSOC, the OH* for all
Pinj has reached the bowl wall, and the rapid, partially
premixed combustion around the bowl wall begins. At
this point, the HRR for P
inj = 14 MPa diverges from
the higher injection pressures. This is indicative of
reduced partially premixed NG mass, lower injection
momentum, and less fuel being added to the reaction
zone. Just before 3 /C176aNGSOC, the HRR for P
inj =1 8
and 22 MPa diverges; however, the difference in peak
HRR is significantly less than between P
inj =1 4 a n d
18 MPa.
Concurrent to the partially premixed combustion,
non-premixed combustion is indicated by the quasi-
steady OH* in the tails of the jets. Because of the
choked NG nozzle conditions, variation of injection
pressure does not significantly affect the observed lift-
off length (note the observed lift-off length is sensitive
to the imaging system settings). Despite this, the NG jet
penetration and mixing rates will increase linearly with
the increased fuel jet momentum resulting from increas-
ing injection pressure, for a given charge density.
36
The late-cycle HRR is not affected by the Pinj con-
sidered, despite the increased mixing rates and greater
premixing. Similar to the GPW variation, the highest
intensity OH*-CL is observed to persist at the peri-
meter of the piston bowl (and possibly extends to the
hidden squish region) for all P
inj. For Pinj = 14 MPa,
significant OH* remains along the NG jet axes late in
the cycle, compared to the more homogeneous distribu-
tions for higher P
inj conditions. This indicates that Pinj
does impact late-cycle reaction zone structure, despite a
negligible difference in HRR.
Relative injection timing
RIT influences the ignition processes, in particular
t
SOC, NG, which impacts the subsequent partially pre-
mixed and non-premixed combustion. A shorter RIT
results in a longer tSOC, NG and increased HRR due to
increased premixing of the NG prior to ignition. 15–17 In
other investigations, it has been noted that as the NG
EOI is advanced relative to the partially premixed
HRR peak, significant reduction of PM emissions can
be achieved, although this is at the cost of higher
unburned CH
4 and NO x emissions.15,17,20,37 These
Figure 9. HRR and ensemble averaged OH *-CL images of the primary heat release processes for GPW = 1.05 ms, 1.45 ms, and
1.85 ms. Overbars indicate estimated NG injection duration until start of needle closing.
Rochussen et al. 507

<!-- PDF_PAGE: 12 -->

observations motivate improved understanding of the
role the RIT plays in primary heat release.
Reducing RIT from 8 /C176to 2 /C176resulted in a longer
tSOC, NG (see Figure 6), allowing for a greater mass of
NG to partially premix prior to ignition. 17 This yields
very high HRR, and produces the most intense OH*-
CL signal of the considered operating conditions, as
shown in Figure 11. For RIT = 2 /C176, the peak OH* cov-
erage is reached more rapidly than the other operating
conditions ( ;4/C176aNGSOC), while OH* intensity also
rapidly increases, suggesting a bulk or well-distributed
partially premixed combustion process. Despite the
high reaction rates, the reaction zone remains confined
to the bowl perimeter.
A longer RIT (RIT = 14 /C176) also resulted in a higher
peak HRR than the datum RIT (8 /C176), despite having the
same t
SOC, NG as the datum. To maintain fixed combus-
tion phasing (CA 50) for the long RIT case, the pilot
injection is advanced. This earlier injection leads to a
lower pilot heat release and less OH* emission from the
pilot (see Figure 7), suggesting that the pilot reaction
zones would have lower temperatures and/or fewer
radicals available to ignite the main NG jets. This leads
to the gas jets igniting further out toward the bowl wall,
as indicated in Figure 11. The subsequent reaction zone
growth between 0–3 /C176aNGSOC is more similar to that
seen with short RIT (RIT = 2 /C176) than for the datum
case. These same cases also show higher peak HRR
than in the datum case. In both short and long RIT
cases, OH* is detected (and hence reactions are likely
to be occurring) at the piston bowl wall prior to full
ignition of the gas (as defined by t
SOC, NG, equation (4),
and shown by 0 /C176aNGSOC in Figure 11). The subse-
quent reaction zone growth is more rapid, resulting in a
higher HRR rise rate (0–2 /C176aNGSOC in Figure 11).
These observations suggest the reduced pilot ignition
heat release allows a more significant fraction of the
NG jets to penetrate to the bowl wall and mix prior to
ignition.
For RIT = –6/C176, the NG injection is complete prior
to the pilot ignition, and the NG jet structure is not
apparent in the OH*-CL images during the primary
heat release. The partially premixed NG is distributed
throughout the visible part of the chamber rather than
confined to the bowl wall, as evidenced by the more
uniformly distributed OH* during the primary heat
release. This indicates that RIT = 26/C176provides time
for NG to mix with air in the center of the combustion
chamber, resulting in leaner conditions at the bowl
wall. Previously, a similar hypothesis suggested that the
lower flame temperature produced by the locally leaner
combustion was the cause for reduced peak HRR for
negative RIT operation.
17 Here, the isotropic reaction
zone growth during ignition and primary heat release
indicates that NG is converted by flame propagation
rather than the distributed combustion of partially pre-
mixed NG noted for other operating conditions. The
flame propagation process is limited by the diffusion
and turbulent mixing of heat and radicals ahead of the
reaction zone and results in a lower peak HRR. These
observations are qualitatively similar to previous inves-
tigations of dual-fuel combustion where flame propaga-
tion through completely premixed NG was observed
and characterized.
22
Figure 10. HRR and ensemble averaged OH *-CL images of the primary heat release processes for Pinj = 14, 18, and 22 MPa. The
start of primary NG heat release was calculated to be 20.8, + 1.5, and + 1.8 /C176aTDC for Pinj = 14, 18, and 22 MPa, respectively.
Overbars indicate estimated NG injection duration until start of needle closing.
508 International J of Engine Research 21(3)

<!-- PDF_PAGE: 13 -->

Updated conceptual description of pilot-
ignited direct-injection NG combustion
Based on the above, an updated conceptual descrip-
tion of the combustion event in a pilot-ignited direct-
injection NG engine is provided. The process is char-
acterized by the presence of multiple combustion
modes, some of which occur simultaneously. These
processes are summarized in Figure 12 with the HRR
of the datum operating condition and representative
OH*-CL images. A typical combustion process
(where RIT . 0) is described in five stages:
1. Pilot auto-ignition: Low-momentum diesel ‘‘puff’’ jets
auto-ignite away from the bowl walls. For the datum
operating condition, the pilot heat release was com-
plete prior to the NG injection. A sufficiently short
RIT (RIT = 2/C176) resulted in a lower pilot HRR and
disturbance of the pilot OH* by NG.
2. NG ignition: High temperature products and radicals
from the pilot combustion ignite the NG jets within
the pilot reaction zones. NG conversion and jet
momentum cause the reaction zones to grow in a
predominantly radial direction, with a low HRR,
and an average reaction zone growth rate of approx-
imately 10 m/s. Although the NG is ignited by the
pilot products, some unrea cted NG will penetrate
past the pilot ignition zones and may reach the bowl
wall where it mixes with air. When the pilot heat
release is too small (e.g. due to very advanced injec-
tion timing), increased penetration of unreacted NG
past the pilot reaction zones occurs.
3. Rapid, distributed partially premixed NG combus-
tion: As the reaction zone reaches the piston bowl
wall, the partially premixed NG at the bowl wall is
converted and results in a high HRR. The
Figure 12. HRR and OH *-CL images of combustion reaction
zones through a typical pilot-ignited direct-injection NG
combustion event.
Figure 11. HRR and ensemble averaged OH *-CL images of primary heat release for RIT = + 14 /C176to 26/C176.
Rochussen et al. 509

<!-- PDF_PAGE: 14 -->

beginning of the partially premixed NG combus-
tion is also characterized by high reaction zone
growth rates ( . 40 m/s). During the rapid heat
release, any ongoing NG injection provides addi-
tional NG and momentum to the partially pre-
mixed reaction zone, which remains near the bowl
perimeter and becomes increasingly mixing rate
limited. If NG SOI is after the pilot EOI, and NG
injection is completed prior to the peak HRR, the
mass of partially premixed fuel and partially pre-
mixed HRR peak are decreased. RIT shorter than
the datum condition results in higher peak HRR
due to increased t
SOC, NG and premixing of the
NG; however, the partially premixed reaction zone
does not extend to the center of the combustion
chamber.
4. Non-premixed combustion: During and after the par-
tially premixed HRR, any ongoing fuel injection
adds NG to the reaction zone at the bowl wall. In
addition, the reaction zone moves upstream along
jets toward the injector and establishes a quasi-
steady lifted jet flame. The NG jets are constrained
by the bowl wall, where high-intensity OH*-CL indi-
cates a significant portion of the mixing-controlled
combustion occurs. Increasing P
inj increases NG jet
momentum and the HRR due to increased fuel-
oxidizer mixing rates during this phase.
5. Late-cycle oxidation: After the end of NG injection,
remaining reactants, partial oxidation products, and
oxidizer react throughout the combustion chamber.
OH*-CL indicates that late-cycle reactions are predo-
minantly located where the highest intensity reactions
occurred earlier in the cycle (i.e. around the bowl peri-
meter). The heat release during late-cycle oxidation
increases with increasing injection duration, but is rel-
atively insensitive toP
inj and RIT.
Processes 3 and 4 constitute a transitional combus-
tion regime, during which multiple combustion pro-
cesses may occur simultaneously. The interaction of the
injected NG with the bowl wall implies that the radius
and shape of the bowl wall will impact fuel mixing and
distribution. Furthermore, fuelling strategy and jet mix-
ing dynamics (particularly in the wall-affected region)
impact the relative proportion of heat release by pro-
cess 3 or 4.
A negative RIT (RIT = –6 /C176) produces a different
combustion process than discussed above. A long
t
SOC, NG results in a partially premixed NG–air mixture
throughout the combustion chamber (not restricted to
the bowl wall) within which pilot auto-ignition occurs.
This causes an increase in the ignition reaction zone
growth rates compared to pilot ignition reaction zones
in air, but does not significantly increase the pilot igni-
tion delay, unlike for port-injected dual-fuel combus-
tion. These ignition reaction zones grow more
isotropically than for conventional RIT operation.
Following ignition, flame propagation through the par-
tially premixed charge results in lower peak HRR than
the rapid partially premixed combustion processes near
the bowl wall for a typical combustion event. This lower
HRR results in a longer overall combustion duration.
Ultimately, the impact of the identified stages of pilot-
ignited direct-injection NG combustion on efficiency and
exhaust emissions is of interest. Correlation of the optical
results presented here with efficiency and emission mea-
surements obtained using th e complementary all-metal
engine configuration is an area of ongoing work.
Conclusion
The objective of this work was to survey and character-
ize the different processes of typical pilot-ignited direct-
injection NG combustion to develop a conceptual
understanding of the process and to guide future inves-
tigations. To this end, a parametric study considering
P
inj, GPW, and RIT was performed using an optically
accessible single-cylinder research engine facility. HRR
analysis, OH*-CL imaging, and reaction growth rate
analysis were used to evaluate the influence of injection
parameters on pilot-ignited direct-injection NG com-
bustion and resulted in the following:
1. An updated conceptual description of pilot-ignited
direct-injection NG combustion based on analysis
of two general stages of combustion: (1) pilot com-
bustion and NG ignition, and (2) primary NG
combustion.
2. Ignition of the NG jets occurs along the side of the
jet (in contrast to recently published imaging
results),
10 which permits NG to penetrate past the
pilot products and mix with air near the cylinder
wall prior to ignition. The resulting partially pre-
mixed combustion process was observed to occur
near the bowl wall and is expected to significantly
impact emissions of NO
x, unburned CH 4, and
PM, as noted in previous works. The penetration
and mixing of the fuel is affected by Pinj and, to a
greater degree, by RIT and has not been fully cap-
tured in existing conceptual descriptions of pilot-
ignited direct-injection NG combustion.
3. Reducing RIT from typical values affected the igni-
tion due to the interaction of injected NG with the
pilot auto-ignition processes. Reduction of RIT
also substantially impacted the partially premixed
NG combustion process, which was observed to
transition from distributed partially premixed com-
bustion to flame propagation, similar to fully pre-
mixed dual-fuel combustion.
Despite limitations of the optical engine facility (e.g.
low CR, cylindrical piston bowl, and line-of-sight ima-
ging), agreement of OH*-CL and HRR analyses, as
well as agreement to previous works, demonstrates that
the refined conceptual model is representative of typical
pilot-ignited direct-injection NG combustion. The
updated conceptual description is based on relatively
510 International J of Engine Research 21(3)

<!-- PDF_PAGE: 15 -->

simple chemiluminescence imaging and provides a
foundation for further development of pilot-ignited
direct-injection NG combustion strategies and high-
lights the necessity of detailed and targeted evaluations
of the injection, fuel mixing, ignition, and emission for-
mation processes.
Acknowledgements
The authors would like to acknowledge the technical
and financial support provided by Westport Fuel
Systems, Inc. The technical support and contributions
of Drs Sandeep Munshi, Jim Huang, and Steve Rogak,
Mr Mahdiar Khosravi, Mr Ashish Singh, and fellow
researchers at The University of British Columbia’s
Clean Energy Research Centre are also gratefully
acknowledged.
Declaration of conflicting interests
The author(s) declared no potential conflicts of interest
with respect to the research, authorship, and/or publi-
cation of this article.
Funding
The author(s) disclosed receipt of the following financial
support for the research, authorship, and/or publication
of this article: This work was supported by the Natural
Sciences and Engineering Research Council of Canada
(NSERC) Collaborative Res earch and Development
(CRD) grant (CRDPJ 451208-13) in conjunction with
Westport Fuel Systems, the Canadian Foundation for
Innovation (CFI) John Evans Leaders Fund (JELF)
grant (no. 32637), the NSERC Discovery Grant Program
(RGPIN 418700-13), CREATE Clean Combustion
Engines, and the John TIEDJE Fellowship.
ORCID iDs
Jeremy Rochussen
 https://orcid.org/0000-0002-7098-2340
Patrick Kirchen
 https://orcid.org/0000-0002-1154-8923
References
1. Intergovernmental Panel on Climate Change. Climate
change 2014: mitigation of climate change: working group
III contribution to the IPCC fifth assessment report .C a m -
bridge: Cambridge University Press, 2015.
2. International Energy Agency. Transport energy and CO2:
moving towards sustainability . Paris: OECD Publishing,
2009.
3. Ouelette P, Goudie D and McTaggart-Cowan G. Prog-
ress in the development of natural gas high pressure direct
injection for Euro VI heavy-duty trucks. In: Proceedings
of the Internationaler Motorenkongress 2016 , Wiesbaden,
9 April 2016, pp.591–607. New York: Springer.
4. Harrington J, Munshi SR, Nedelcu C, Ouellette P,
Thompson J and Whitfield S. Direct injection of natural
gas in a heavy-duty diesel engine. SAE technical paper
2002-01-1630, 2002.
5. Papagiannakis RG, Rakopoulos CD, Hountalas DT and
Rakopoulos DC. Emission characteristics of high speed,
dual fuel, compression ignition engine operating in a
wide range of natural gas/diesel fuel proportions. Fuel
2010; 89(7): 1397–1406.
6. Stettler ME, Midgley WJ, Swanson JJ, Cebon D and
Boies AM. Greenhouse gas and noxious emissions from
dual fuel diesel and natural gas heavy goods vehicles.
Environ Sci Technol 2016; 50(4): 2018–2026.
7. Besch MC, Israel J, Thiruvengadam A, Kappanna H and
Carder D. Emissions characterization from different tech-
nology heavy-duty engines retrofitted for CNG/diesel dual-
fuel operation.SAE Int J Engines 2015; 8(3): 2015–2001.
8. Ko¨nigsson F, Kuyper J, Stalhammar P and Angstrom
H. The influence of crevices on hydrocarbon emissions
from a diesel-methane dual fuel engine. SAE Int J
Engines 2013; 6(2): 751–765.
9. McTaggart-Cowan G, Mann K, Wu N and Munshi S. An
efficient direct-injection of natural gas engine for heavy
duty vehicles. SAE technical paper 2014-01-1332, 2014.
10. Hatzipanagiotou A, Marko F, Koenig G, Krueger C,
Wenzel P and Koch T. Numerical and optical analysis of
heterogeneous gas combustion with diesel pilot ignition
in a commercial vehicle engine. Int J Engine Res 2018;
19(1): 109–119.
11. Ouellette P, Mtui PL and Hill PG. Numerical simulations
of directly injected natural gas and pilot diesel fuel in a
two-stroke compression ignition engine. SAE technical
paper 981400, 1998.
12. Li G, Ouellette P, Dumitrescu S and Hill P. Optimization
study of pilot-ignited natural gas direct-injection in diesel
engines. SAE technical paper 1999-01-3556, 1999.
13. Hill PG and Ouellette P. Transient turbulent gaseous fuel
jets for diesel engines. Trans Am Soc Mech Eng J Fluid
Eng 1999; 121: 93–101.
14. Dec J. A conceptual model of DI diesel combustion based
on laser-sheet imaging. SAE technical paper 970873, 1997.
15. McTaggart-Cowan GP, Bushe WK, Rogak SN, Hill PG
and Munshi SR. Injection parameter effects on a direct
injected, pilot ignited, heavy duty natural gas engine with
EGR. SAE technical paper 2003-01-3089, 2003.
16. McTaggart-Cowan GP, Bushe WK, Rogak SN, Hill PG
and Munshi SR. PM and NOx reduction by injection
parameter alterations in a direct injected, pilot ignited,
heavy duty natural gas engine with EGR at various oper-
ating conditions. SAE technical paper 2005-01-1733, 2005.
17. Faghani E, Kheirkhah P, Mabson C, McTaggart-Cowan
GP, Kirchen P and Rogak S. Effect of injection strategies
on emissions from a pilot-ignited direct-injection natural-
gas engine-part ii: slightly premixed combustion. SAE
technical paper 2017-01-0774, 2017.
18. McTaggart-Cowan GP. Pollutant formation in a gaseous-
fuelled, direct injection engine. PhD Thesis, The University
of British Columbia, Vancouver, BC, Canada, 2006.
19. Dumitrescu S and Hill PG. Effects of injection changes
on efficiency and emissions of a diesel engine fueled by
direct injection of natural gas. SAE technical paper 2000-
01-1805, 2000.
20. Munshi S, McTaggart-Cowan GP, Huang J and Hill PG.
Development of a partially-premixed combustion strategy
for a low-emission, direct injection high efficiency natural
gas engine. In: Proceedings of the ASME 2011 internal com-
bustion engine division fall technical conference , Morgan-
town, WV, 2–5 October 2011, pp.515–528. New York:
ASME.
Rochussen et al. 511

<!-- PDF_PAGE: 16 -->

21. McTaggart-Cowan GP, Mann K, Huang J, Singh A,
Patychuk B, Zheng ZX and Munshi S. Direct injection of
natural gas at up to 600 bar in a pilot-ignited heavy-duty
engine. SAE Int J Engines 2015; 8: 981–996.
22. Rochussen J and Kirchen P. Characterization of reaction
zone growth in an optically accessible heavy-duty diesel/
methane dual-fuel engine. Int J Engine Res . Epub ahead
of print 22 February 2018. DOI: 10.1177/146808741
8756538.
23. Rochussen J. Thermodynamic and optical investigation of
the combustion mechanisms of diesel-ignited dual-fuel natu-
ral gas combustion . Master’s Thesis, The University of
British Columbia, Vancouver, BC, Canada, 2015.
24. Khosravi M and Kirchen P. Refinement of the two-color
method for application in a direct injection diesel and nat-
ural gas compression ignition engine. Proc IMechE, Part
D: J Automobile Engineering, in press.
25. Yeo J. Development and application of in-cylinder fuel con-
centration and pyrometry optical diagnostic tools in diesel-
ignited dual-fuel natural gas engines . Master’s Thesis, The
University of British Columbia, Vancouver, BC, Canada,
2017.
26. Yeo J, Rochussen J and Kirchen P. Application of an in-
cylinder local infrared absorption fuel concentration sen-
sor in a diesel-ignited dual-fuel engine. SAE technical
paper 2016-01-2310, 2016.
27. Nori V and Seitzman J. Evaluation of chemiluminescence
as a combustion diagnostic under varying operating con-
ditions. In: Proceedings of the 46th AIAA aerospace
sciences meeting and exhibit , Reno, NV, 7–10 January
2008, p.953. Reston, VA: AIAA.
28. Higgins B, McQuay M, Lacas F, Rolon JC, Darabiha N
and Candel S. Systematic measurements of OH chemilu-
minescence for fuel-lean, high-pressure, premixed, lami-
nar flames. Fuel 2001; 80(1): 67–74.
29. Panoutsos C, Hardalupas Y and Taylor A. Numerical eva-
luation of equivalence ratio measurement using OH* and
CH* chemiluminescence in pr emixed and non-premixed
methane–air flames.Combust Flame2009; 156(2): 273–291.
30. Heywood JB. Internal combustion engine fundamentals .
New York: McGraw-Hill, 1988.
31. Benajes J, Molina S, Garcia-Oliver JM and Novella R.
Influence of boost pressure and injection pressure on
combustion process and exhaust emissions in a HD diesel
engine. SAE technical paper 2004-01-1842, 2004.
32. Stiesch G. Modeling engine spray and combustion pro-
cesses. New York: Springer, 2013.
33. Karim G, Ito K, Abraham M and Jensen L. An examina-
tion of the role of formaldehyde in the ignition processes
of a dual fuel engine. SAE technical paper 912367, 1991.
34. Karim G, Liu Z and Jones W. Exhaust emissions from
dual fuel engines at light load. SAE technical paper
932822, 1993.
35. McTaggart-Cowan GP, Jones H, Rogak S, Bushe WK,
Hill PG and Munshi SR. The effects of high-pressure
injection on a compression–ignition, direct injection of
natural gas engine. J Eng Gas Turb Power 2007; 129(2):
579–588.
36. Ouellette P and Hill P. Turbulent transient gas injections.
J Fluid Eng 2000; 122(4): 743–752.
37. Florea R, Neely GD, Miwa J and Abidin Z. Efficiency
and emissions characteristics of partially premixed dual-
fuel combustion by co-direct injection of NG and diesel
fuel (DI). SAE technical paper 2017-01-0766, 2017.
Appendix 1
Notation
F equivalence ratio
tign, pilot pilot ignition delay
tSOC, NG natural gas start of combustion delay
uign, pilot crank angle of pilot ignition
umaxHRR crank angle of maximum HRR
uSOC, NG crank angle of natural gas start of
combustion
CA50 crank angle of 50% heat release
Pinj injection pressure
Appendix 2
-15 -10 -5 0 5 10
°CA aTDC
HRR
Estimated Injection Rate
HRR
Pilot Injection Rate
NG Injection Rate
-10 -5 0  5  10 15 
°CA aPI
-15 -10 -5 0  5  10 
°CA aNGSOC
PPW
RIT
GPW
ign,pilot
ign,pilot
(equation 3)
SOC,NG
SOC,NG
(equation 4)
Figure 13. Diagram relating key nomenclature and physical
processes of pilot-ignited direct-injection natural gas (NG)
combustion.
tign, pilot: pilot ignition delay, tSOC, NG : NG start of combustion delay,
uign, pilot: crank angle of pilot ignition, uSOC, NG : crank angle of start of NG
combustion, GPW: gas (NG) pulse width, PPW: pilot pulse width, RIT:
relative injection timing, /C176CA aPI: crank angle degrees after pilot ignition,
/C176CA aNGSOC: crank angle degrees after NG start of combustion.
512 International J of Engine Research 21(3)

<!-- PDF_PAGE: 17 -->

Appendix 3
Natural luminosity images
Natural luminosity (NL) images recorded for all oper-
ating conditions are presented here, in Figure 14. The
images were recorded simultaneously to the OH*-CL
images discussed in this work and were imaged using a
700-nm narrow band-pass filter (see Table 2).
Appendix 4
Heat release rate and pressure data
To complement the heat release rate (HRR) data pre-
sented referenced to pilot ignition ( /C176aPI) and NG start
of combustion ( /C176aNGSOC), HRR and cylinder pres-
sure data for all the operating points considered in the
current work are presented referenced to top dead cen-
ter (TDC) here, in Figure 15.
Figure 14. Natural luminosity images for all operating conditions.
Figure 15. HRR (solid lines) and cylinder pressure (dotted
lines) data for the sweep of Pinj (top), RIT (middle), and injection
duration (bottom).
Rochussen et al. 513
