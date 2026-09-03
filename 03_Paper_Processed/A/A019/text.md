<!-- PDF_PAGE: 1 -->

Direct injection of hydrogen main fuel and diesel
pilot fuel in a retroﬁtted single-cylinder
compression ignition engine
Xinyu Liu, Gabrielle Seberry, Sanghoon Kook *, Qing Nian Chan,
Evatt R. Hawkes
School of Mechanical and Manufacturing Engineering, The University of New South Wales, Sydney, Australia
highlights
/C15 90% hydrogen substitution by energy in a hydrogen-diesel dual direct-injection engine.
/C15 Combustion mode switch by injection timing control to inﬂuence charge stratiﬁcation, IMEP and NO x.
/C15 At 90% hydrogen, optimised IMEP and NO x emissions at 40 /C14 CA bTDC injection.
/C15 Up to 85.9% reduction of CO 2 with 13.3% higher efﬁciency than conventional diesel combustion.
article info
Article history:
Received 27 April 2022
Received in revised form
12 August 2022
Accepted 14 August 2022
Available online 29 September 2022
Keywords:
Hydrogen direct injection
Dual-fuel combustion
Diesel engine
CO
2 reduction
abstract
Up to 90% hydrogen energy fraction was achieved in a hydrogen diesel dual-fuel direct
injection (H2DDI) light-duty single-cylinder compression ignition engine. An automotive-
size inline single-cylinder diesel engine was modiﬁed to install an additional hydrogen
direct injector. The engine was operated at a constant speed of 2000 revolutions per minute
and ﬁxed combustion phasing of /C0 10 crank angle degrees before top dead centre (
/C14 CA
bTDC) while evaluating the power output, efﬁciency, combustion and engine-out emis-
sions. A parametric study was conducted at an intermediate load with 20 e90% hydrogen
energy fraction and 180-0 /C14 CA bTDC injection timing. High indicated mean effective
pressure (IMEP) of up to 943 kPa and 57.2% indicated efﬁciency was achieved at 90%
hydrogen energy fraction, at the expense of NO
x emissions. The hydrogen injection timing
directly controls the mixture condition and combustion mode. Early hydrogen injection
timings exhibited premixed combustion behaviour while late injection timings produced
mixing-controlled combustion, with an intermediate point reached at 40
/C14 CA bTDC
hydrogen injection timing. At 90% hydrogen energy fraction, the earlier injection timing
leads to higher IMEP/efﬁciency but the NO
x increase is inevitable due to enhanced pre-
mixed combustion. To keep the NO x increase minimal and achieve the same combustion
phasing of a diesel baseline, the 40 /C14 CA bTDC hydrogen injection timing shows the best
performance at which 85.9% CO 2 reduction and 13.3% IMEP/efﬁciency increase are
achieved.
© 2022 Hydrogen Energy Publications LLC. Published by Elsevier Ltd. All rights reserved.
* Corresponding author .
E-mail address: s.kook@unsw.edu.au (S. Kook).
Available online at www.sciencedirect.com
ScienceDirect
journal homepage: www.elsevier.com/locate/he
international journal of hydrogen energy 47 (2022) 35864 e35876
https://doi.org/10.1016/j.ijhydene.2022.08.149
0360-3199/© 2022 Hydrogen Energy Publications LLC. Published by Elsevier Ltd. All rights reserved.

<!-- PDF_PAGE: 2 -->

Introduction
Hydrogen internal combustion engines (H2ICEs) can be
divided into two main categories according to fuel injection
methods: port fuel injection (PFI) and direct injection (DI) [ 1,2].
PFI involves fuel injection into the intake manifold before the
air passes through the intake valves to the combustion
chamber, while DI delivers fuel directly into the combustion
chamber. Within these categories, several ignition strategies
are employed, including pilot diesel fuel [ 1] or utilisation of a
spark plug. PFI of hydrogen often has limited engine load
conditions due to pre-ignition, knock and backﬁre which arise
due to low minimum ignition energy and short quenching
distance of hydrogen. Furthermore, hydrogen displaces air in
the intake stroke, which reduces oxygen input and thus re-
quires more work of compression. This reduces engine power
density and volumetric efﬁciency [ 1]. Most studies employing
diesel pilot injection and hydrogen PFI have a hydrogen en-
ergy share limited to about 30 e40% at low to medium loads
and 6 e25% at high loads due to knocking [ 3,4]. One study re-
ported 97% hydrogen energy fraction with 49% indicated
thermal efﬁciency [ 5]; however, pressure ringing in their re-
sults suggests knocking. Another study achieving 92.3%
hydrogen PFI and maximum thermal efﬁciency of 42% re-
ported knock-free combustion, which however required up to
60% intake air dilution with nitrogen [ 6].
Hydrogen DI poses several improvements over hydrogen
PFI. Previous studies [ 1,2,7e9] reported that backﬁre can be
eliminated where injection happens after the intake valve
closure; pre-ignition can be largely avoided; the volumetric
efﬁciency loss due to displacement of air by hydrogen is
eliminated; and high-pressure hydrogen DI creates the
potential to achieve similar efﬁciency to conventional diesel
engines. Previous studies implementing DI in spark ignition
engines showed that hydrogen DI enables mixture stratiﬁca-
tion as opposed to the well-mixed condition of PFI [ 7]. The
control of injection timing makes a direct impact on engine
efﬁciency and power output with intermediate hydrogen in-
jection timing ( e.g. 80
/C14 CA bTDC) [ 9] achieving the best per-
formance. However, hydrogen DISI engines retain efﬁciency
inferior to diesel engines due to knocking and pre-ignition
which limit the compression ratio, and slower early stage
combustion due to a single ignition kernel formed from the
spark plug [ 1].
The present study focuses on a new approach named
hydrogen diesel dual-fuel direct injection (H2DDI) in a
compression ignition (CI) engine, which implements the use
of multi-hole diesel injector to cause multiple ignition kernels
from pilot fuel autoignition [ 1]. A previous study [ 10] used an
H2DDI strategy employing an integrated high-pressure dual-
fuel injector with a central diesel nozzle and three surround-
ing gas nozzles, which achieved 97.5% hydrogen energy frac-
tion and an indicated mean effective pressure (IMEP) of
2600 kPa. Two separate injectors, i.e. a hydrogen direct injector
and a diesel injector, were also used with a wide range of H
2
injection timings (180-20 /C14 CA bTDC) and energy fractions
(10e50%) tested to demonstrate higher efﬁciency than 100%
diesel and a great potential to optimise engine efﬁciency and
emissions [ 2]. An outstanding issue of H2DDI combustion is
oxides of nitrogen (NO
x) emissions similar with other
hydrogen ICEs [ 2,10e13]. A computational simulation study
[14] showed that the intermediate hydrogen injection timings
achieving the maximum efﬁciency leads to high probability of
in-cylinder local temperatures T > 2500 K and near-
stochiometric conditions 0.7 < 4 < 1.1 contributing to faster
NO
x production at mid-point heat release (CA50) and higher
total NOx. To extend the hydrogen energy fraction achievable
in an H2DDI engine and optimise operating conditions for
engine performance/efﬁciency and NO
x emissions, a new
hydrogen injection method is required.
This study bridges this gap by upgrading a hydrogen in-
jection system used from previous studies performed in the
same engine [2,14] - the new injection system was designed to
convert a multiple hole injector with an outlet recessed in a
duct above the engine head to a single hole capped injector
with the outlet aligned with the engine head to improve
mixing. The hydrogen jet is targeted at the piston bowl rather
than entering in a diffuse cloud, reducing combustion near
walls and associated wall heat losses. Furthermore, an
injector outlet aligned with the engine head eliminates
hydrogen trapped in the crevice volume. The combustion
characteristics, engine performance and emissions are
investigated with a range of H
2 injection timings of 180 e0 /C14 CA
bTDC and hydrogen energy fractions of up to 90%, - i.e. H2DDI
combustion with hydrogen main fuel and diesel pilot fuel. The
diesel pilot injection is executed before/after or during the
hydrogen injection depending on the injection timings. The
total energy input, mid-point combustion phasing (CA50) and
engine speed were held constant. The in-cylinder pressure,
CO
2 and NO x were measured and compared to a baseline
diesel combustion case. The noise produced by combustion
was also estimated and evaluated.
Abbreviations
4 Fuel-air equivalence ratio
aHRR Apparent heat release rate
aTDC After top dead centre
bTDC Before top dead centre
CA Crank angle
CA50 Crank angle after 50% heat release
CI Compression ignition
CO Carbon monoxide
CO
2 Carbon dioxide
CoV Coefﬁcient of variation
DI Direct injection
GDI Gasoline direct injection
H2DDI Hydrogen-diesel dual direct injection
ICE Internal combustion engine
IMEP Indicated mean effective pressure
NO
x Oxides of nitrogen, namely, NO, NO 2 and N2O
PFI Port fuel injection
SI Spark ignition
SOI Start of injection
T Temperature
uHC Unburnt hydrocarbons
international journal of hydrogen energy 47 (2022) 35864 e35876 35865

<!-- PDF_PAGE: 3 -->

Engine setup and experiment procedure
The H2DDI engine is modiﬁed from an inline four-cylinder
production engine (Hyundai D4EA series), including the
deactivation of three cylinders, installation of a hydrogen
direct injector, and ﬁtting for an in-cylinder pressure trans-
ducer. The schematic diagram of the engine test facility is
shown in Fig. 1, engine and injection system speciﬁcations are
summarised in Table 1 and photos for key testing instruments
and a schematic of injector arrangement are shown in Fig. 2.
Hydrogen-diesel dual direct injection (H2DDI) engine setup
The single-cylinder engine has an 83 mm bore and 93 mm
stroke, resulting in a displacement volume of 497.78 cm 3. The
engine has a geometric compression ratio of 17.7 with a cy-
lindrical bowl of 55 mm in diameter. The nominal swirl ratio
of the production engine head is 1.4, measured on a steady
ﬂow rig. The engine is unthrottled and naturally aspirated for
air intake. Two 60 dm
3 surge tanks are connected with intake
and exhaust manifolds respectively to dampen the pressure
variation associated with single-cylinder operation.
Hydrogen is fuelled by a retroﬁtted injector that was
modiﬁed from a gasoline direct injector (GDI, Bosch
026,150,533), accommodated in the modiﬁed glow-plug hole of
the production engine head at 45
/C14 to the engine head plane.
The original injector features 6 holes with a diameter of
approximately 160 mm and included angle of 70
/C14 as measured
by X-ray computed tomography imaging. This commercial
GDI injector was chosen because of its sealing integrity at
desired hydrogen feed pressure. The hydrogen injector as
illustrated in Fig. 2 bottom-right, is modiﬁed with an added
cap on top of the original injector tip. The added cap has a
single hole with a 1 mm diameter. The direction of the
hydrogen jet is aligned with the injector body as illustrated in
Fig. 2 (bottom-right). As the original liquid-fuelling injector
body has been used for gaseous hydrogen injection without
fuel-passing lubrication, one droplet of engine oil has been
added to the injector feed before each day of the experiments
for needle lubrication. Injector failure was not observed the
entire test. Further information about the hydrogen direct
injector used in the present study is found in a ﬁled patent
[15].
The hydrogen injector was supplied with 20 MPa hydrogen
from a 1 dm
3 accumulator using a custom-made boost pump
system (Zenobalti ZB-1301), which uses a single-stage, single-
acting pneumatic hydrogen pump (Haskel AG-62-86,979). The
pump is capable of producing a maximum of 62 MPa hydrogen
pressure with a volume of 50.8 cm
3 per pumping cycle at one
pumping cycle per second, which exceeds the ﬂow rate and
injection pressure required for the study. The hydrogen ﬂow
rate of this retroﬁtted injector is 1.44 g/s at 20 MPa injection
pressure. Hydrogen consumption rate was determined using a
1.29 dm
3 chamber by measuring the pressure rise from
injected hydrogen, similar with the Zeuch method. The
chamber was operated at a wall temperature of 363 K (90 /C14 C)
for mirroring warmed-up engine condition. Ideal gas law was
then applied to derive the injected hydrogen mass at each
electronic signal duration. A high-precision pressure sensor
was used for this test (Sensys PSH, 1 MPa scale with 0.15%
precision). The tests were repeated at different back pressures
from 0 to 5 MPa for simulating the cylinder pressure condi-
tions across the compression stroke while maintaining the
hydrogen direct injection pressure.
Fig. 1 e Schematic diagram of the hydrogen-diesel dual direct-injection (H2DDI) engine setup.
international journal of hydrogen energy 47 (2022) 35864 e3587635866

<!-- PDF_PAGE: 4 -->

Table 1 e Engine conﬁguration details.
Displacement volume 497.8 cm 3
Bore 83 mm
Stroke 92 mm
Compression ratio 17.7
Swirl ratio 1.4
Valves 2 intake, 2 exhaust
Piston 55 mm diameter top-hat cylindrical bowl
Intake Naturally aspirated, unthrottled
Injection system Hydrogen Diesel
Injector Modiﬁed Bosch spray-guided GDI injector Bosch CRI2,
150
/C14 included angle
Number of holes 6 x 160 mm. Injector cap has a 1 mm
diameter axially drilled hole
7 x 134 mm
Flow rate 1.44 g/s at 200 MPa H 2 pressure 800 cm 3/min at 10 MPa pressure
Discharge coefﬁcient 0.86
Bosch K-factor 1.5
Pump Zenobalti Hydrogen Boost Pump System (ZB-1301)
Haskel Hydrogen Pump (AG-62-86,979)
Bosch CP3, common-rail
Fig. 2 e Photographs of the engine setup (top) and a schematic for injector arrangement (bottom) [ 15].
international journal of hydrogen energy 47 (2022) 35864 e35876 35867

<!-- PDF_PAGE: 5 -->

Diesel is fuelled by a centrally mounted 7-hole solenoid
common-rail injector (Bosch CRI2), fed by a production
common-rail injection system with a high-pressure pump
(Bosch CP3). The injector nozzle holes have a 134 mm diameter,
150
/C14 included angle, discharge coefﬁcient of 0.86, a Bosch K-
factor of 1.5 and a standard hydraulic ﬂow rate of 400 cm 3.A
commercial ultra-low sulphur diesel fuel with a minimum
cetane number of 51 is used throughout this study. The
injected diesel fuel mass, injection duration, and proﬁle are
measured in a Bosch-tube type injection rate meter at simu-
lated back pressures, as in the previous study [ 16].
Instruments for engine control and data acquisition
The in-cylinder pressure data is measured by a piezoelectric
pressure transducer (Kistler 6056A with an ampliﬁer Kistler
5015A) with 200 kHz acquisition rate. For each test condition,
the in-cylinder pressure data were recorded for 240 contin-
uous ﬁring cycles to ensure statistical relevance. The pressure
traces were ensemble averaged and used to calculate
apparent heat release rate (aHRR), net IMEP and coefﬁcient of
variation (CoV) of IMEP. Combustion phasing including CA10,
CA50, and CA90 was calculated by the crank angle position
where corresponding to 10%, 50%, and 90% of the total heat
release. Burn duration including early-cycle, late-cycle, and
total combustion duration are calculated and labelled as
CA10-50, CA50-90, and CA10-90, respectively.
The injection timing (signal start of injection, SOI), injec-
tion duration, and diesel common-rail pressure are governed
by a universal controller (Zenobalti, ZB-9013P), timed with
monitored crankshaft position by using an encoder with a
precision of 1800 pulses per revolution (Autonics E40S8). En-
gine speed is controlled by an Eddy Current dynamometer
(FroudeHoffmann, AG-30HS). Engine coolant (water) temper-
ature of 363 K (90
/C14 C) is maintained by a water temperature
controller (Thermalcare, Aquatherm RQE0920) for simulating
warmed-up engine conditions.
For engine-out emissions, NO
x was measured using a non-
dispersive infrared analyser (Testo 350 XL with 5% accuracy)
and CO
2 was measured with a non-dispersive infrared ana-
lyser (Horiba Mexa-584L, 1.7% accuracy). The same analyser
also recorded carbon monoxide and unburnt hydrocarbon
emissions, which however were below the detection limit at
high hydrogen energy fraction operations and thus did not
return any meaningful data. The exhaust opacity was also
measured using an opacimeter (Horiba MEXA-600S, 0.15 ±m
/C0 1
light absorption coefﬁcient accuracy), but due to the same
reason, it is not discussed in this study. The combustion noise
was also estimated from the in-cylinder pressure using the
method developed by Shahlari et al. [ 17,18] with respect to
engine structure and frequency response in human hearing.
Engine operating parameters
The study aimed to systematically investigate the effect of
hydrogen injection timing and hydrogen energy fraction on
combustion, engine performance and engine-out emissions.
Hydrogen injection timings (SOI) between 180
/C14 CA bTDC and
TDC were tested, though with increasing hydrogen energy
fraction some early injection timings could not be achieved
due to knocking, and some late injection timings were tested
with CA50 outside the determined range. A wide range of
hydrogen injection timings were selected to cause variations
in charge stratiﬁcation and premixed/mixing-controlled
combustion mode. For example, injection timing 180
/C14 CA
bTDC gives a high level of premixing, approaching PFI condi-
tions. H
2 SOI of 140 /C14 CA bTDC is just after the intake valve
closes. A range of intermediate and late injection timings were
also implemented. While varying the injection timing, the
hydrogen energy fraction was also varied between 20% and
90% by adjusting the injection duration. For instance, at 90%
hydrogen energy fraction, diesel supplementing the remain-
ing energye i.e. a combustion mode with hydrogen as a main
fuel and diesel as a pilot fuel. For the selected load/speed
conditions of the present study, the hydrogen energy fraction
was limited by the minimum injection duration required for
the diesel injector used. Higher energy fraction would be
achieved if higher load conditions are tested in future.
Engine operating conditions are summarised in Table 2 .
Some operating conditions were held constant including the
engine speed, intake air pressure and temperature as well as
the coolant temperature. The engine speed was ﬁxed at
2000 rpm as this is the maximum torque speed of the base
prodctuioin engine. The engine was operated at a natural
aspiration mode and the coolant temperature was controlled
to simulated a warmed-up engine condition. Hydrogen and
diesel injection pressures were ﬁxed at 20 MPa and 100 MPa,
respectively. While the hydrogen and diesel injection duration
and timing were adjusted to vary the hydrogen energy frac-
tion and mixture distributions, the total energy injected per
cycle was held constant at 820 J. Furthermore, the combustion
phasing of CA50 (midpoint of the total heat release) was held
constant at 10 ± 0.8
/C14 CA aTDC by adjusting the diesel injection
timing. It should be noted some high hydrogen fraction and
late injection timing conditions could not achieve this ﬁxed
CA50, which will be discussed in the following section.
Results and discussion
Effect of hydrogen injection timing
The in-cylinder pressure and aHRR traces for hydrogen in-
jection timing (H
2 SOI) variation are illustrated in Fig. 3 for two
selected hydrogen energy fractions of 50% and 90%. Diesel
injection timing and duration for H 2 SOI is illustrated in ar-
rows on the aHRR traces. As mentioned previously, this was
adjusted to achieve ﬁxed mid-point combustion phasing
(CA50). The hydrogen injection duration is also illustrated for
the later H
2 SOIs as it is in the crank angle range displayed in
Fig. 3 . 90% H 2 energy fraction was achieved (H 2 4¼0.36)
without pre-ignition or knocking issues. This demonstrates
the signiﬁcant beneﬁts of hydrogen direct injection at an
overall lean hydrogen charge. It also demonstrates the
advantage of this new single-hole injector for mixture control
to increase the H
2 energy fraction, compared to the previous
work [ 2] achieving only up to 50% H 2 because an unmodiﬁed
multi-hole injector was used with an outlet recessed in a duct
above the engine head. Computational simulation of the un-
modiﬁed injector [ 14] identiﬁed a need for better mixture
international journal of hydrogen energy 47 (2022) 35864 e3587635868

<!-- PDF_PAGE: 6 -->

preparation, which has been realised using the single hole
nozzle exposed directly to the combustion chamber and
formed air-hydrogen mixture within the piston bowl. It is
noted that 90% H2 energy fraction was stopped but not limited,
because at this condition the diesel injection duration reached
its minimum limit regarding the reliable and repeatable nee-
dle movement. For H
2 energy fraction of 50%, injection timings
across compression stroke (180 /C14 CA bTDC to TDC) were tested
successfully, including two additional very late injection
timings at 10
/C14 CA and TDC crank angle position over the
previous work [ 2]. For 90% H 2 energy fraction, the most
advanced H 2 SOI is limited at 90 /C14 CA bTDC as earlier H 2 SOI
resulted in knocking and excessive combustion noise and
therefore data was not recorded.
The in-cylinder pressure traces in Fig. 3 show a consistent
trend in the end-of-compression pressure, where the pressure
at TDC shows a monotonic increase with either earlier H
2 SOI
or higher H 2 energy fraction from compression work and/or
added H2 mass, similar with ﬁndings in the previous study [ 2].
For 50% H2 fraction, an earlier H 2 SOI leads to a slightly higher
peak in-cylinder pressure up to 90 /C14 CA bTDC, dominated by
enhanced premixed hydrogen combustion from longer mix-
ing. For earlier H
2 SOI of 140 /C14 CA bTDC and 180 /C14 CA bTDC,
more advanced H 2 SOI results in a lower peak pressure. It is
explained by the overall fuel-lean hydrogen charge ( 4¼0.2)
with high homogeneity at these SOIs, which is also evidenced
by the slightly lower peak aHRR. For late SOIs ( i.e. 20
/C14 CA bTDC
to TDC), the combustion is dominated by mixing-controlled
hydrogen burn from the lengthy injection that overlaps with
diesel injection. That is, diesel ﬂame develops while the
hydrogen injection continues and thus the reaction rate is
limited by the air-hydrogen mixing.
For 90% H
2 fraction, the increment of TDC pressure is
intensiﬁed clearer by compression work of early injected H 2,
with the addition of H 2 mass compared to 50% H 2 fraction
cases. The shape of in-cylinder pressure and the proﬁle of
aHRR traces indicate there is a clear switch of combustion
mode from hydrogen premixed combustion to mixing-
controlled combustion by retarding H
2 SOI. At early H 2 SOI of
90 /C14 CA bTDC, both the peak pressure and maximum aHRR
exceed the diesel baseline, indicating a large amount of pre-
mixed hydrogen combusting simultaneously with the diesel
fuel. More advanced injection timings could not be achieved
due to knocking caused by the premixed hydrogen combus-
tion. Given the combustion phasing is ﬁxed, increased power
Table 2 e Engine operating and fuel injection conditions.
Engine speed [RPM] 2000
Intake air pressure [kPa] 101.3
Intake air temperature [ /C14 C] 27
Coolant (water)
temperature [ /C14 C]
90
Combustion phasing
[CA50, /C14 CA aTDC]
10
Energy input per cycle [J] 820
Fuel Hydrogen Diesel
Fuel injection pressure [MPa] 20 100
Low heating value [MJ/kg] 119.7 43.4
Fuel injection timing
(SOI) [
/C14 CA bTDC]
180, 140, 90,
60, 40, 20, 10, 0
12e4
Energy fraction [%] 20, 30, 40, 50, 60,
70, 80, 90
80e10
Fuel mass [mg] 1.37, 2.06, 2.74, 3.43,
4.11, 4.80, 5.48, 6.17,
15.12e1.89
Injection duration [ms] 2.0 e5.5 0.72 e0.39
Injection duration [ /C14 CA] 24 e65.9 8.6 e4.7
Fig. 3 e Effect of hydrogen injection timing on in-cylinder pressure and apparent heat release rate (aHRR) at hydrogen
energy fraction of 50% and 90%. The injection timing and duration of diesel fuel are annotated by the arrows at the bottom of
the plot. The hydrogen injection is annotated at the top of the plot.
international journal of hydrogen energy 47 (2022) 35864 e35876 35869

<!-- PDF_PAGE: 7 -->

output and higher engine efﬁciency is expected. At delayed H 2
SOIs of 60 and 40 /C14 CA bTDC, the peak pressure and maximum
aHRR are lower than those of the 90 /C14 CA bTDC hydrogen in-
jection; however, the late-cycle aHRR is measured higher. This
suggests enhanced mixing-controlled combustion.
For H
2 SOI later than 20 /C14 CA bTDC, it is noted that the mid-
point combustion phasing of CA50 control was not possible
regardless of diesel injection control and thus they cannot be
directly compared to the earlier H
2 SOI cases. The latest in-
jection timing tested was TDC (0 /C14 CA aTDC) as further delay
caused misﬁring. Fig. 3 shows the magnitude of peak pressure
and maximum aHRR continue to decrease with a more
retarded H2 SOI. However, the late-cycle aHRR (e.g. after 20 /C14 CA
aTDC) shows an increasing trend with a more retarded H 2 SOI.
The decreasing peak aHRR suggests hydrogen mixing became
dominator where the limited mixing and fuel-rich hydrogen
mixtures cannot maintain the high rate of early-phase heat
release, which explains the failed combustion phasing con-
trol. These three late H
2 SOI cases indeed show that the
lengthy injection overlaps with diesel injection and thus
diesel ﬂames develop during or even before the hydrogen in-
jection. This sequence of pilot diesel injection and hydrogen
injection, together with decreasing peak aHRR trend and
higher late-cycle heat release rate, suggests hydrogen mixing-
controlled combustion or diffusion ﬂames for the late H
2 SOI
of 20, 10 and 0 /C14 CA bTDC.
Hydrogen combustion modes
The results shown in Fig. 3 provided an overview of hydrogen
combustion initiated by diesel ﬂames with early H 2 SOI
exhibiting premixed combustion and late H 2 SOI displaying
mixing-controlled combustion behaviour. To further analyse
premixed combustion of hydrogen observed for early
Fig. 4 e Effect of hydrogen energy fraction on in-cylinder pressure and apparent heat release rate (aHRR) for hydrogen
injection timings of 180, 140, 90, and 60 /C14 CA bTDC (SOI: start of injection).
international journal of hydrogen energy 47 (2022) 35864 e3587635870

<!-- PDF_PAGE: 8 -->

injection timings, the ensemble-averaged in-cylinder pres-
sure and derived aHRR traces are depicted in Fig. 4 for H2 SOI
of 180 e60 /C14 CA bTDC with varied H 2 energy fractions. On the
aHRR plots, the diesel injection timing is illustrated with a
note of corresponding diesel energy fraction. The early H
2 SOI
cases of 180 and 140 /C14 CA bTDC achieved up to 70% and 80% H 2
energy fraction, respectively. In these premixed burn domi-
nant H
2 SOIs, higher H 2 energy fraction was limited by pres-
sure ringing (knocking) and audible noise. For each injection
timing, peak in-cylinder pressure increases almost mono-
tonically with a higher H
2 energy fraction. On the other hand,
the peak aHRR shows a decreasing trend. Furthermore, with
increasing H2 energy fraction, aHRR curves tend to be shorter
and wider, suggesting the hydrogen-air mixture is less ho-
mogenous e i.e. charge stratiﬁcation effects. As the H
2 SOI is
further delayed to 90 and 60 /C14 CA bTDC, the enhanced charge
stratiﬁcation led to higher H 2 energy fraction up to 90%
without knocking as shown in Fig. 4(bottom). The same trend
of increasing TDC pressure and peak pressure is observed for
higher H
2 energy fractions. The peak aHRR also shows the
same decreasing trend with increasing H 2 energy fraction.
Fig. 5 shows the ensemble-averaged in-cylinder pressure
and derived aHRR traces for cases with late H 2 SOIs in the
range of 40 e0 /C14 CA bTDC. The maximum H 2 energy fraction of
90% was achieved for all H2 SOIs in this range. As the hydrogen
injection timing is later, the TDC pressure increase due to
hydrogen compression becomes minimal. Also, the hydrogen
injection continues within the displayed crank angle range of
Fig. 5 as illustrated on the pressure curves. In most cases, the
diesel injection timing (illustrated on the aHRR curves) over-
laps with the hydrogen injection duration e i.e. the diesel
ﬂames developing within the hydrogen jet. This overlap
Fig. 5 e Effect of hydrogen energy fraction on in-cylinder pressure and apparent heat release rate (aHRR) for hydrogen
injection timings of 40, 20, 10, and 0 /C14 CA bTDC (SOI: start of injection).
international journal of hydrogen energy 47 (2022) 35864 e35876 35871

<!-- PDF_PAGE: 9 -->

becomes so signiﬁcant that the diesel and hydrogen injection
start almost at the same time for 10 /C14 CA bTDC H 2 SOI, sug-
gesting a hydrogen diffusion ﬂame. For TDC (0 /C14 CA bTDC) H 2
SOI, the diesel injection timing is earlier than the hydrogen
start of injection, which further empathises a hydrogen
diffusion ﬂame. Notably, at 40
/C14 CA bTDC H2 SOI, both peak in-
cylinder pressure magnitude and position are similar for all H2
energy fractions without any observed trends. This suggests
40
/C14 CA bTDC H 2 SOI as the crossover point between the pre-
mixed and mixing-controlled combustion at all hydrogen
energy fractions.
Another evidence that the 40
/C14 CA bTDC H 2 SOI is a cross-
over point of the combustion mode is found from CA50, the
mid-point combustion phasing, and CA10-CA50, the early
burn duration. Fig. 6 shows CA50 and CA10-CA50 for each H
2
SOI and H 2 energy fraction. Both CA50 and CA10-CA50 are
generally uniform as the diesel injection timing was adjusted
to achieve it. However, for late H
2 SOIs of 20 e0 /C14 CA bTDC,
some high H2 energy fractions (marked by a dashed line) could
not achieve ﬁxed CA50 and CA10-CA50 despite a range of
diesel injection timings attempted. Speciﬁcally, up to 40% H
2
energy fraction, all H 2 SOIs achieved the ﬁxed CA50 of 10 /C14 CA
aTDC. However, at 50% H2 energy fraction, a H2 SOI of TDC had
to allow a more retarded CA50 of 15 /C14 CA aTDC. This becomes
worse at 60 and 70% H 2 energy fraction to have 0 and 10 /C14 CA
bTDC H 2 SOI failed to achieve the ﬁxed CA50. At higher H 2
energy fractions of 80 and 90%, this issue is found at 20 /C14 CA
bTDC H2 SOI and later. At a H 2 SOI of 40 /C14 CA bTDC and earlier,
the CA50 was successfully ﬁxed for all H 2 energy fractions
through the control of diesel injection timing. When hydrogen
combustion was predominantly in a mixing-controlled mode
(i.e. H2 SOI later than 40 /C14 CA bTDC), the peak aHRR was lower
but the late-cycle aHRR was higher and lasted longer (see
Fig. 3). For low H
2 energy fractions, the diesel injection timing
was effective in controlling CA50 of a hydrogen diffusion
ﬂame as much as of premixed hydrogen combustion. How-
ever, at high H
2 energy fractions, the charge was with a sig-
niﬁcant level of stratiﬁcation and the mixture inhomogeneity
was very high during combustion due to very late hydrogen
injection partly into diesel ﬂames. Therefore, a direct com-
parison between the premixed hydrogen combustion and
diffusion hydrogen ﬂames against the same diesel baseline
was not possible. However, the remaining H
2 energy fractions
and H 2 SOIs provide meaningful trends to discuss. In the
following sections, the operating conditions with delayed
CA50 will be marked by illustrating a great region, similar with
Fig. 6.
Engine power output and indicated efﬁciency
The net IMEP, CoV of IMEP and net indicated efﬁciency are
depicted in Fig. 7 against H 2 SOI for each H 2 energy fraction.
For all operating conditions, IMEP values similar to or above
t h ed i e s e lb a s e l i n ew e r ea c h i e v e df o ra tl e a s to n eh y d r o g e n
injection timing. The early to intermediate hydrogen injec-
tion timings exhibit generally uniform IMEP for H
2 energy
fractions 20 e50%, with a more pronounced peak for greater
H2 energy fractions. As the total energy input was held con-
stant, the net indicated efﬁciency shows exactly the same
trend.
IMEP values in signiﬁcant excess of the diesel baseline were
achieved for H
2 energy fractions 60% and greater. Notably,
very high efﬁciency and IMEP values are observed for 80 and
90% H2 energy fractions. At 80% H2 energy fraction and 140/C14 CA
bTDC H2 SOI, IMEP of 834 kPa is achieved with 50.6% efﬁciency.
At 90% H 2 energy fraction and 90 /C14 CA bTDC H 2 SOI, IMEP of
943 kPa is achieved with 57.2% efﬁciency, which is 27% greater
than the diesel baseline. These peak IMEP values are
measured at an intermediate injection timing of 60
/C14 CA bTDC
H2 SOI. This is attributed to a balance between premixed burn
and mixing-controlled combustion with the former increasing
the peak pressure and the latter extending the relatively high
aHRR period. When the charge is more homogenous at earlier
H
2 SOI, lean hydrogen combustion led to lower aHRR. The
opposite end is found from the hydrogen diffusion ﬂame cases
(grey region) where the peak aHRR occurring near TDC is
much lower and the longer lasting aHRR in the expansion
stroke could not produce high power output. It is therefore a
premixed hydrogen charge with signiﬁcant mixture stratiﬁ-
cation that can provide an optimised charge condition to
produce the maximum power output and engine efﬁciency.
The CoV of IMEP results in this study are within the
acceptable range, with all values 3.1% or lower, and the lowest
CoV of IMEP values are achieved at higher H
2 energy fractions.
The achievement of very high IMEP with hydrogen-diesel
dual-fuel combustion is not unprecedented. Roy et al. [ 6]
used a hydrogen-diesel dual-fuel CI engine with hydrogen PFI
and diesel DI with hydrogen energy fraction of 89.25 e92.3%
and achieved a maximum IMEP of 908 kPa with 42% thermal
efﬁciency. With 40 e50% nitrogen gas dilution, the maximum
Fig. 6 e Effect of hydrogen energy fraction and injection
timing on mid-point combustion phasing (CA50) and early
burn duration (CA10-50).
international journal of hydrogen energy 47 (2022) 35864 e3587635872

<!-- PDF_PAGE: 10 -->

IMEP achieved increased to 1013 kPa. Furthermore, Gleis
et al.‘s H2DDI study [ 10] employing a specialised high-
pressure dual fuel injector with 97.5% hydrogen energy
fraction achieved an IMEP of about 2600 kPa. These points
suggest that the peak IMEP values obtained are reliable and
demonstrate the success and potential of H2DDI combustion
Fig. 7 e Effect of hydrogen energy fraction and injection timing on indicated mean effective pressure (IMEP), coefﬁcient of
variation of IMEP, and indicated efﬁciency.
Fig. 8 e Engine-out emissions of carbon dioxide (CO 2), nitrogen oxides (NO x), estimated combustion-induced noise as well
as peak pressure rise rate (PRR) for a variation of hydrogen energy fraction and hydrogen injection timing.
international journal of hydrogen energy 47 (2022) 35864 e35876 35873

<!-- PDF_PAGE: 11 -->

with hydrogen as a main fuel and diesel as a pilot fuel for
ignition. Engine-out emissions.
The CO 2 and NO x emissions, two most concerned air
polluting emissions of H2DDI engines, are shown in Fig. 8 for
each H2 SOI and H2 energy fraction. The order of magnitude of
the results is consistent with other CI hydrogen-diesel dual-
fuel studies with lower H
2 energy fraction for both CO2 [19] and
NOx [2,10]. Both CO and unburned hydrocarbons (uHC) emis-
sions were below the measurement limit for all cases.
The CO2 emissions decrease monotonically for each H 2 SOI
as H 2 energy fraction increases. This trend is as expected
because as the diesel fraction decreases, there is reduced
combustion of fuel containing carbon atoms, reducing CO 2
produced. At 90% hydrogen energy fraction and a H 2 SOI of
60/C14 CA bTDC, the minimum CO2 for this test matrix is achieved
at 142 g/kWh (2.1% volume), which is just 22% of the diesel
baseline of 643 g/kWh, marking an almost ﬁve-fold decrease.
Though a ten-fold decrease might be anticipated, examina-
tion of chemical equations for complete combustion indicates
CO
2 emissions decrease almost but not quite linearly with
increasing H2 energy fraction, giving a theoretical CO 2 reduc-
tion of 88% for 90% H 2 energy fraction. The remaining
discrepancy is likely due to the incomplete combustion of
diesel. For each hydrogen energy fraction, there is a slight
increase in CO2 emissions for very late H2 SOIs, which could be
due to the improved combustion efﬁciency of the pilot diesel.
The trends exhibited for NO x are very similar to those
observed for IMEP and efﬁciency, which corresponds to the
well-known trade-off between NO
x and power output
[9,20,21], where high power is associated with high heat
release, high ﬂame temperature and NO x emissions. For H 2
energy fractions 20e80%, maximum NOx is produced at 60/C14 CA
bTDC H 2 SOI, which corresponds to the point where
maximum IMEP is achieved ( Fig. 7 ). For early to intermediate
H2 SOIs of 180 e60 /C14 CA bTDC, NO x generally increases with H 2
energy fraction. This accords with studies that have shown
very high NOx for hydrogen fuel combustion [2,11e13]; indeed,
since hydrogen has an adiabatic ﬂame temperature of about
200 K more than diesel [ 1], hydrogen combustion produces
higher levels of thermal NO
X.A sH 2 energy fraction increases,
so too do the NO x trends associated with hydrogen combus-
tion. The NO x levels are also very similar with the corre-
sponding results for H 2 energy fractions 20 e50% observed for
a similar engine setup but recessed and unmodiﬁed multi-
hole hydrogen injector [ 2].
Almost all data points exhibit NO
x greater than that for the
diesel baseline. Very high NO x values of 10 e23 g/kWh
(1100e3200 ppm) are produced for H 2 energy fractions
30e90%, an increase of more than three times the diesel
baseline of 6.4 g/kWh. At early to intermediate H 2 SOIs, there
is increased premixed hydrogen combustion, which promotes
thermal NO formation. The very high NO
x of 23 g/kWh, which
greatly exceeds the general trends observed, attained at 90%
H
2 energy fraction and 90/C14 CA bTDC H2 SOI suggests a very high
temperature and lean fuel condition near-critical NO x for-
mation conditions of 4 ~0.77 which promotes the production
of NOx [14]. This result emphasises the importance of H2 SOI to
avoid excessive NO x.
For later H 2 SOIs, NOx output trends are mixed, but higher
H2 energy fractions tend to produce lower NO x. This crossover
in NO x trend is mirrored by the crossover from premixed to
mixing-controlled combustion of hydrogen as observed in
previous sections. For 50 e90% H
2 energy fraction and TDC H 2
SOI, and 80 e90% H 2 energy fraction and 10 /C14 CA bTDC H 2 SOI,
NOx emissions are lower than that for diesel combustion, with
minimum values of 3.5 g/kWh (300 ppm) achieved, which is a
45% decrease compared to the diesel baseline. For late H
2 SOIs,
the in-cylinder charge is more stratiﬁed and a hydrogen
diffusion ﬂame is developed, with rich zones reduced below
the peak NO
x emission air/fuel ratio of 4 ~0.77. Furthermore,
these data points are associated with reduced aHRR, which
could indicate lower temperature combustion. Therefore, the
in-cylinder conditions are not optimal for producing NO
x.A t
very early H 2 SOIs, the NO x is reduced as a signiﬁcant portion
of the mixtures being locally lean to suppress the ﬂame tem-
perature below the NO formation limit. These results indicate
how H
2 SOI may be used strategically to minimise NO x emis-
sions. However, for the data collected, higher IMEP or lower
NO
x compared to the diesel baseline can be achieved for
H2DDI, but not both, indicating an avenue for future
improvement.
Fig. 8(right) shows noise and pressure rise rate results. The
analysis is in consideration of increased noise occurring for
enhanced premixed combustion, which generally accords to
higher power output and higher NO
x emission conditions. The
noise produced by the engine is estimated from the pressure
trace using the method developed by Shahlari et al. [ 17,18].
The estimated noise and pressure rise rate generally decrease
with increasing H
2 energy fraction, with the maximum noise
98.6 dB, which is 1.5 dB above the diesel baseline, reached at
20% H
2 energy fraction and 60 /C14 CA bTDC H 2 SOI. This follows
the trend expected from premixed combustion. However, for
H2 energy fractions 60% and greater, most H 2 SOIs produce
lower noise than diesel, including the timing where IMEP is
the highest for each H
2 energy fraction. This demonstrates a
signiﬁcant potential of hydrogen combustion with signiﬁcant
charge stratiﬁcation and/or diffusion ﬂames in avoiding
combustion-induced noise.
The noise results in Fig. 8(right) shows a high sensitivity to
H
2 SOI. An overall trend is that the TDC noise level is lowest for
most H 2 energy fractions, with a minimum of 90.2 dB ach-
ieved, thanks to a hydrogen diffusion ﬂame. At very early H 2
SOIs, the noise also shows a decreasing trend, which is likely
due to a signiﬁcant portion of mixtures being locally lean,
similar with the NO
x. For later H 2 SOIs until the intermediate
timings, more robust premixed combustion played a domi-
nant role. For more retarded H
2 SOIs, noise generally de-
creases, but there is a signiﬁcant dip in noise and pressure rise
rate at 40
/C14 CA bTDC H 2 SOI and subsequent peak at 20 /C14 CA
bTDC. This consistent phenomenon is related to the crossover
from premixed to mixing controlled combustion that was
observed to occur at the same H
2 SOI was observed previously
for a recessed and unmodiﬁed multi-hole injector system for a
similar engine setup [ 2]. In other words, an optimised strati-
ﬁed premixed charge was made to cause a lower pressure rise
rate than more premixed combustion. Also, it was before a
international journal of hydrogen energy 47 (2022) 35864 e3587635874

<!-- PDF_PAGE: 12 -->

diffusion ﬂame was formed to signiﬁcantly reduce the heat
release rate and minimise the combustion-induced noise.
H2 SOI optimisation
Of the data recorded in the test matrix, the 90% H 2 energy
fraction data is of greatest signiﬁcance as it points towards the
concept of a hydrogen main fuel engine with diesel pilot fuel,
as opposed to a dual-fuel engine with low hydrogen usage.
From this data, the intermediate-early H
2 SOI of 40 /C14 CA bTDC
to be the most promising. At this timing, a balance between
improved IMEP and relatively reduced NO x is reached. An
IMEP of 843 kPa is achieved, which is 14% greater than the
diesel baseline, and NO
x of 10.3 g/kWh, which is 61% higher
than the diesel baseline but reduced compared to much of the
data recorded in this study. Furthermore, CO
2 of 147.8 g/kWh
is attained at 23% of the diesel baseline, and a low noise
condition of 93.6 dB is achieved at 3.5 dB below the diesel
baseline. This H
2 SOI also has combustion characteristics
marked by a transition between premixed and mixing-
controlled combustion, as suggested from the peak pressure,
peak aHRR, CA50, CA10-CA50, IMEP, efﬁciency and NO
x data.
Accordingly, the charge distribution at this timing is a blend
between well-mixed and stratiﬁed, albeit likely with a greater
proportion of stratiﬁed charge. These results were achieved
with the improved hydrogen injector cap system and subse-
quent improved mixture distribution within the piston bowl.
Conclusions
The performance and emissions of a hydrogen diesel dual-
fuel direct injection system in a retro-ﬁtted compression
ignition combustion engine were investigated. A parametric
study was conducted with constant mid-point combustion
phasing and engine speed. In the study, a range of hydrogen
injection timings 180-0
/C14 CA bTDC and hydrogen energy frac-
tions 20e90% were tested, with the remaining energy supplied
by diesel. The in-cylinder pressure was measured to deter-
mine the apparent heat release rate, indicated mean effective
pressure and efﬁciency, combustion phasing and combustion
noise. The engine-out emissions of CO
2 and NO x were
measured and analysed. The main ﬁndings and conclusions of
this experimental study are as follows.
1. 90% hydrogen energy fraction was achieved with up to
85.9% reduction in CO
2 in an H2DDI engine without knock
or pre-ignition for hydrogen injection timings 90-0 /C14 CA
bTDC. The maximum IMEP of 943 kPa was achieved with
57.2% indicated efﬁciency at 90
/C14 CA bTDC hydrogen injec-
tion timing, which is 27% greater than the diesel baseline.
2. Two combustion modes emerge for H2DDI, where gener-
ally early to intermediate180-60 /C14 CA bTDC hydrogen in-
jection timing causes primarily premixed combustion, a
crossover point emerges around 40
/C14 CA bTDC and for late
injection timings of 20 e0 /C14 CA bTDC there is primarily
mixing-controlled combustion with a hydrogen diffusion
ﬂame. For this study, premixed combustion cases exhibit
higher peak in-cylinder pressure, peak aHRR, IMEP and
efﬁciency but also higher NO
x.
3. A trade-off between engine performance quantiﬁed by
IMEP and efﬁciency, and low NO x emissions emerges. The
maximum IMEP, efﬁciency and NO x are attained at 40 /C14 CA
bTDC hydrogen injection timing, at which point the
hydrogen charge is intermediate between well-mixed and
stratiﬁed, enabling fast ﬂame propagation.
4. Higher hydrogen energy fraction produces higher NO
x
emissions up to greater than three times the diesel base-
line for 90% hydrogen energy fraction and 90
/C14 CA bTDC
injection timing. However, varying hydrogen direct injec-
tion timing enables reduction of NO
x, even below the diesel
baseline, for very late hydrogen injection timing for
80e90% hydrogen energy fraction. However, there is an
associated reduction in IMEP and efﬁciency as the com-
bustion phasing cannot be ﬁxed but retarded.
5. 40
/C14 CA bTDC injection timing at 90% hydrogen energy
fraction emerges as a good balance of IMEP and NO x, with
843 kPa IMEP (13.3% above diesel baseline) and 90 g/kWh
CO
2 (85.9% below diesel baseline). At this condition, the
estimated combustion noise is 93.6 dB at 3.5 dB below the
diesel baseline. The combustion characteristics at this
point are intermediate between premixed and mixing-
controlled combustion, with a blend of well-mixed and
stratiﬁed charge.
Declaration of competing interest
The authors declare that they have no known competing
ﬁnancial interests or personal relationships that could have
appeared to inﬂuence the work reported in this paper.
Acknowledgements
Experiments were performed at the UNSW Engine Research
Laboratory, Sydney, Australia. The ﬁnancial support for this
research project was provided by the Australian Renewable
Energy Agency (ARENA). The authors thank Alexander Knaﬂ
and Marcus Becher at MAN Energy Solutions for useful dis-
cussions and additional funding support. Thanks are also due
to Mr Bryce Edmonds for his technical support.
references
[1] Yip H, Srna A, Yuen A, Kook S, Taylor R, Yeoh G, Medwell P,
Chan Q. A review of hydrogen direct injection for internal
combustion engines: towards carbon-free combustion. Appl
Sci 2019;9(22):4842. https://doi.org/10.3390/app9224842.
[2] Liu X, Srna A, Yip H, Kook S, Chan Q, Hawkes E. Performance
and emissions of hydrogen-diesel dual direct injection
(H2DDI) in a single-cylinder compression-ignition engine. Int
J Hydrogen Energy 2021;46(1):1302 e14. https://doi.org/
10.1016/j.ijhydene.2020.10.006.
[3] Chintala V, Subramanian K. A comprehensive review on
utilization of hydrogen in a compression ignition engine
under dual fuel mode. Renew Sustain Energy Rev
2017;70:472e91. https://doi.org/10.1016/j.rser.2016.11.247.
[4] Dimitriou P, Tsujimura T. A review of hydrogen as a
compression ignition engine fuel. Int J Hydrogen Energy
international journal of hydrogen energy 47 (2022) 35864 e35876 35875

<!-- PDF_PAGE: 13 -->

2017;42(38):24470e86. https://doi.org/10.1016/
j.ijhydene.2017.07.232.
[5] Santoso W, Bakar R, Nur A. Combustion characteristics of
diesel-hydrogen dual fuel engine at low load. Energy Proc
2012;32:3e10. https://doi.org/10.1016/j.egypro.2013.05.002.
[6] Roy M, Tomita E, Kawahara N, Harada Y, Sakane A. An
experimental investigation on engine performance and
emissions of a supercharged H2-diesel dual-fuel engine. Int J
Hydrogen Energy 2010;35(2):844 e53. https://doi.org/10.1016/
j.ijhydene.2009.11.009.
[7] Wimmer A, Wallner T, Ringler J, Gerbig F. H2-direct injection
e a highly promising combustion concept. SAE Technical
Paper; 2005. https://doi.org/10.4271/2005-01-0108.
[8] Matthias N, Wallner T, Scarcelli R. A hydrogen direct
injection engine concept that exceeds U.S. DOE light-duty
efﬁciency targets. SAE Int J Engine 2012;5(3):838 e49. https://
doi.org/10.4271/2012-01-0653.
[9] Mohammadi A, Shioji M, Nakai Y, Ishikura W, Tabo E.
Performance and combustion characteristics of a direct
injection SI hydrogen engine. Int J Hydrogen Energy
2007;32(2):296e304. https://doi.org/10.1016/
j.ijhydene.2006.06.005.
[10] Gleis S, Frankl S, Prager M, Wachtmeister G. Optical analysis
of the combustion of potential future E-Fuels with a high
pressure dual fuel injection system, ” 14th International AVL
symposium on propulsion diagnostics . Baden-Baden; 2020 .
[11] Liu X, Srna A, Yip H, Kook S, Chan Q, Hawkes E. Comparison
of hydrogen port injection and direct injection (DI) in a
single-cylinder dual-fuel diesel engine. In: Proceedings of the
22nd australasian Fluid Mechanics Conference AFMC2020;
2020. https://doi.org/10.14264/a1cd1dc.
[12] Tang X, Kabat D, Natkin R, Stockhausen W, Heffel J, Ford.
Hydrogen engine dynamometer development. SAE Technical
Paper; 2002. https://doi.org/10.4271/2002-01-0242. 2022-01-
0242.
[13] Du Y, Yu X, Liu L, Li R, Zuo X, Sun Y. Effect of addition of
hydrogen and exhaust gas recirculation on characteristics of
hydrogen gasoline engine. Int J Hydrogen Energy 2017;42(12).
https://doi.org/10.1016/j.ijhydene.2017.02.197. 8828-8298.
[14] Wang Y, Evans A, Srna A, Wehrfritz A, Hawkes E, Liu X,
Kook S, Chan Q. A numerical investigation of mixture
formation and combustion characteristics of a hydrogen-
diesel dual direct injection engine. SAE Technical Paper;
2021. https://doi.org/10.4271/2021-01-0526. 2021-01-0526.
[15] Kook S, Liu X, Edmonds B. Hydrogen-diesel direct injection
dual-fuel system for internal combustion engines. Australian
Patent Provisional; 2022. Application No. 2022900118, ﬁled 21
Jan.
[16] Liu X, Srna A, Chan Q, Kook S. Effect of exhaust gas
recirculation and intake air e-boosting on gasoline
compression ignition combustion. SAE International Journal
of Engines 2020;13(3):377 e90. https://doi.org/10.4271/03-13-
03-0025.
[17] Shahlari A, Kurtz E, Hocking C, Antonov S. Correlation of
cylinder pressure-based engine noise metrics to measured
microphone data. Int J Engine Res 2015;16(7):829 e50.
[18] Shahlari A, Hocking C, Kurtz E, Ghandhi J. Comparison of
compression ignition engine noise metrics in low-
temperature combustion egimes. SAE International Journal
of Engines 2013;6(1):541 e52. https://doi.org/10.4271/2013-01-
1659
.
[19] Liew C, Li H, Besch M, Ralston B, Clark N, Huang Y. Exhaust
emissions of a H2-enriched heavy-duty diesel engine
equipped with cooled EGR and variable geometry
turbocharger. Fuel 2011;91(1):155 e63. https://doi.org/10.1016/
j.fuel.2011.08.002.
[20] Wallner T, Nande A, Naber J. Study of basic injection
conﬁgurations using a direct-injection hydrogen research
engine. SAE International Journal of Engines
2009;2(1):1221e30. https://doi.org/10.4271/2009-01-1418.
[21] Verhelst S. Recent progress in the use of hydrogen as a fuel
for internal combustion engines. Int J Hydrogen Energy
2014;39(2):1071e85. https://doi.org/10.1016/
j.ijhydene.2013.10.102.
international journal of hydrogen energy 47 (2022) 35864 e3587635876
