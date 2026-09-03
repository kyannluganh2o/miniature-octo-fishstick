<!-- PDF_PAGE: 1 -->

Performance and emissions of hydrogen-diesel
dual direct injection (H2DDI) in a single-cylinder
compression-ignition engine
Xinyu Liu a, Ale /C20s Srna a, Ho Lung Yip a, Sanghoon Kook a,*,
Qing Nian Chan a, Evatt R. Hawkes a,b
a School of Mechanical and Manufacturing Engineering, The University of New South Wales, Sydney, NSW, 2052,
Australia
b School of Photovoltaic and Renewable Energy Engineering, The University of New South Wales, Sydney, NSW,
2052, Australia
highlights
/C15First hydrogen-diesel dual-direct injection in a compression-ignition engine.
/C15Up to 50% hydrogen substitution by energy.
/C15Variation of H 2 injection timing for H 2 charge stratiﬁcation control.
/C15Demonstrated performance/efﬁciency comparable to diesel operation.
/C15Moderate NO x increase and lower noise related to H 2 injection timing.
article info
Article history:
Received 17 July 2020
Received in revised form
12 September 2020
Accepted 1 October 2020
Available online 24 October 2020
Keywords:
Hydrogen direct injection
Injection timing
Diesel engine
Dual-fuel combustion
Hydrogen energy fraction
abstract
Hydrogen-diesel dual direct-injection (H2DDI) is successfully implemented in a
compression-ignition engine, which is developed to circumvent the pre-ignition and
knocking limitations inherent to port fuel-injection hydrogen engines. An automotive-size
single-cylinder common-rail diesel engine was modiﬁed to ﬁt an additional high-pressure
hydrogen injector in the cylinder head. The engine is operated at intermediate load with
constant fuel-energy input using an energy-substitution principle e the diesel injection
duration is decreased as the hydrogen amount is increased while adjusting the diesel in-
jection timing to ﬁx the combustion phasing. The results show that, at early hydrogen
injection timings, the heat release rate and engine-out emissions show trends indicating
premixed combustion whereas later injection timings exhibit hydrogen mixing-controlled
combustion behaviour. At 50% hydrogen substitution ratio and optimised direct injection
timing of 40 ⁰CA bTDC, the uncompromised indicated efﬁciency of 47% is achieved while
the combustion-induced noise is decreased by 6 dB and the engine-out NO
x emission is
kept below 11 g/kWh.
© 2020 Hydrogen Energy Publications LLC. Published by Elsevier Ltd. All rights reserved.
* Corresponding author .
E-mail address: s.kook@unsw.edu.au (S. Kook).
Available online at www.sciencedirect.com
ScienceDirect
journal homepage: www.elsevier.com/locate/he
international journal of hydrogen energy 46 (2021) 1302 e1314
https://doi.org/10.1016/j.ijhydene.2020.10.006
0360-3199/© 2020 Hydrogen Energy Publications LLC. Published by Elsevier Ltd. All rights reserved.

<!-- PDF_PAGE: 2 -->

Introduction
The hydrogen-fuelled internal combustion engine (H 2ICE) is
an attractive energy conversion technology with a broad range
of beneﬁts including high thermodynamic efﬁciency,
straightforward conversion of existing petroleum- and gas-
fuelled engines as well as existing engineering and
manufacturing infrastructure [ 1e4]. The successful develop-
ment of H
2ICE will make a signiﬁcant impact on propulsion
and stationary applications, thereby accelerating the market
penetration of hydrogen as a future energy carrier.
Early studies of hydrogen combustion in engines focused
on spark-ignition (SI) engine applications with an aim to in-
crease the laminar ﬂame speed and enhance the engine
performance and stability [ 5], which achieved considerable
performance improvement [ 6e9]. The largest body of litera-
ture focuses on modiﬁed SI engines with the conventional
fuel supply system by carburettor [ 10e12] or hydrogen
fumigation system to create a premixed hydrogen-air
mixture in the intake port or manifold (port fuel injection,
PFI) [ 3,4,13]. It was shown that the high laminar ﬂame speed
and wide ﬂammability limits enable beneﬁts for efﬁcient
ultra-lean operation over the gasoline-engine counterparts
[2,4,13]. Moreover, the nitrogen oxides (NO
x) emissions were
measured below 100 ppm in lean operation, which could be
further reduced to sub-ppm levels under stoichiometric
operation realised with high exhaust gas recirculation (EGR)
for the use of three-way catalytic converters [ 14,15]. The peak
engine efﬁciency of up to 38% was achieved alongside with
efﬁciency improvements at part-load [ 13,16]. Nevertheless,
the maximum engine load in hydrogen operation is limited
due to pre-ignition and end-gas autoignition [ 9,17]. When
these further develop into more signiﬁcant knock, it may
cause a permanent damage to engine parts. Typically, the
engine peak power output suffers a 35 e50% reduction pri-
marily due to the knock issues that limit the global equiva-
lence ratio to values of about 0.6 e0.8 [ 2,4,13]. Furthermore,
the engine heat-losses, boosted by short quenching distance
of hydrogen, over-proportionally increase at high hydrogen
equivalence ratio operation, which can reach up to 45% of the
total fuel heating value [ 18,19] and thus considerably limiting
the engine efﬁciency and durability.
The limitations of PFI H
2ICE technology prompted the
development of boosted hydrogen engines with a stratiﬁed
charge operation featuring hydrogen injection directly into
the cylinder (DI). The early works demonstrated up to 42%
indicated thermal efﬁciency in an automotive-size engine
[20]. The essential need to reduce the engine heat losses
in hydrogen operation by using DI to create a stratiﬁed
charge away from the piston and cylinder walls was
identiﬁed [ 21e23], while others focused on managing the
NO
x/efﬁciency trade-off that arises from the different levels
of hydrogen stratiﬁcation associated with the injector ge-
ometry and ignition timing [ 21,23e25]. Notably, the ambi-
tious goals of 45% brake thermal efﬁciency with less than
0.8 g/kWh of NO
x emission at 13 bar peak load and part-load
efﬁciency of 33% were achieved by researchers at
Argonne National Laboratory and Sandia National
Laboratories in an engine size of 660 cm
3 per cylinder [ 26,27].
Furthermore, the teams of Japanese National Trafﬁc Safety
Laboratory and Tokyo City University reached 45% indicated
efﬁciency in a 1000 cm
3 per cylinder medium-duty engine
[24,28]. Additionally, their research demonstrated the po-
tential of a lean NO x trap using hydrogen as a reducing agent
to reach ultra-low tailpipe NO x emissions. Overall, the ben-
eﬁts of hydrogen direct injection and charge stratiﬁcation
are demonstrated, which include reduced NO
x emissions at
high loads and higher efﬁciency at partial loads than those
of PFI [ 3].
Despite the demonstrated success of SI H
2ICE research,
the concept is likely to face challenges associated with
knocking and non-ideal combustion phasing as the engine
size and load increase beyond 1 L/cylinder and 10 bar indi-
cated mean effective pressure (IMEP), respectively [ 17].
Recent progress in large gas or liquid-fuelled engine devel-
opment has shown great advantages of stratiﬁed combustion
in autoignition mode such as premixed-charge compression
ignition (PCCI), reactivity controlled compression ignition
(RCCI), gasoline compression ignition (GCI), premixed
mixture ignition in the end-gas region (PREMIER) and intel-
ligent charge compression ignition (ICCI) with unprecedented
high brake thermal efﬁciencies of 50% or higher being re-
ported [ 29e33]. The combustion phasing and peak heat
release rates can be tailored to the engine operating point by
managing the reactivity through fuel stratiﬁcation or mixing
of multiple fuels. Similar attempts using hydrogen in dual-
fuel operation with diesel-pilot ignition and hydrogen PFI
were made; however, they were limited due to pre-ignition
occurring in the high compression ratio compression-
ignition engines. Diesel energy substitution with hydrogen
was limited to about 40% at low loads and about 20% at in-
termediate loads with both inferior efﬁciency and NO
x
emissions compared to diesel-only operation [ 34]. The
notable exception is by Zhou et al. [ 35] who reported 40%
energy substitution ratio at intermediate load.
The present study aims to extend the hydrogen substi-
tution ratio in a hydrogen-diesel dual-fuel engine by intro-
ducing a 20 MPa hydrogen direct injection in a modiﬁed
automotive-size single-cylinder diesel engine. To the best of
the authors’ knowledge, this is the ﬁrst demonstration of a
hydrogen-diesel dual-fuel engine with dual direct injection
(namely, H2DDI). The operation limits and performances are
explored by systematically changing the hydrogen injection
timing in the range of 180 to 20
/C14CA before top dead centre
(bTDC) and hydrogen energy fraction of up to 50% while
keeping the mid-point combustion phasing position con-
stant at a ﬁxed load of about 7.8 bar IMEP. The tests were
designed to highlight the effect of hydrogen charge stratiﬁ-
cation on pre-ignition tendency, engine efﬁciency, and
emissions. The in-cylinder pressure and engine-out emis-
sions including NO
x, smoke, unburnt hydrocarbon (uHC),
and carbon monoxide (CO) were measured and compared to
a selected reference case with the conventional diesel-only
operation. Considering increased premixed charge combus-
tion, the combustion-induced noise was also estimated and
evaluated.
international journal of hydrogen energy 46 (2021) 1302 e1314 1303

<!-- PDF_PAGE: 3 -->

Engine test facility and operation strategy
Single-cylinder dual direct-injection hydrogen-diesel engine
facility
The H2DDI engine used for performance and emissions
testing in the present study was derived from an inline four-
cylinder diesel engine (Hyundai D4EA series), with a single-
cylinder swept volume of 497.8 cm
3. The modiﬁcations to
the cylinder head include deactivation of three out of four
cylinders, modiﬁcation to the glow-plug mounting hole to ﬁt a
hydrogen direct injector and installation of an in-cylinder
pressure transducer. The schematic diagram of the engine
facility, a cross-sectional view of the combustion chamber and
actual setup pictures are shown in Fig. 1 . The details of the
engine conﬁguration are listed in Table 1.
The single-cylinder engine has 83 mm bore and 92 mm
stroke. The piston has a cylindrical bowl with a diameter of
55 mm resulting in a geometric compression ratio of 17.4. The
engine is naturally aspirated and unthrottled. The intake and
exhaust pipes are connected with two large 60 dm
3 surge
tanks to dampen the pressure oscillations associated with
single-cylinder operation. The engine is equipped with a
Fig. 1 e Schematic diagram of the hydrogen-diesel dual direct-injection (H2DDI) engine setup (top) and photographs of the
key engine components with a schematic showing the injector arrangement (bottom).
international journal of hydrogen energy 46 (2021) 1302 e13141304

<!-- PDF_PAGE: 4 -->

production common-rail injection system with a high-
pressure pump (Bosch CP3) and a 7-hole solenoid common-
rail injector (Bosch CRI2) for diesel fuelling. The nozzle holes
have a nominal diameter of 134 mm, discharge coefﬁcient of
0.86 and Bosch K-factor of 1.5 with a standard hydraulic ﬂow
rate of 400 cm
3. A conventional ultra-low sulphur diesel fuel
with a guaranteed minimum cetane number of 51 was used
throughout the experiments. The nominal swirl ratio of the
production cylinder head is 1.4, measured on a steady ﬂow rig.
For hydrogen direct injection, the glow-plug hole in the
cylinder head was modiﬁed to house a commercial 6-hole
spray-guided gasoline direct injector (GDI, Bosch 0261500533)
as illustrated in Fig. 1 . The injector features six holes with a
diameter of approximately 160 mm and included angle of 70
/C14
according to X-ray computed tomography imaging. The
steady ﬂow rate of hydrogen through the GDI injector is 1.37 g/
s at 20 MPa pressure. This commercial GDI injector was cho-
sen due to its good sealing integrity at desired high hydrogen
pressure and due to the lack of commercial availability of
high-pressure gaseous fuel injectors. It was noted that no
injector failure was observed for the entire tests of the present
study. The injector needle lubrication was a concern, which
was addressed by adding a droplet of engine oil into the
injector inlet each day before starting the experiments.
However, for longer-term operation in commercial applica-
tions, this solution will likely not fulﬁl the lifetime re-
quirements and, therefore, a new hydrogen injector
development would be needed. This, however, is not within
the scope of the current work.
As illustrated in Fig. 1, the nozzle exit is located in a 7.5 mm
duct connected to the combustion chamber, under an angle of
45
/C14to the cylinder head plane, and retracted 12.3 mm from the
cylinder head plane. This position is dictated by the space
constraints within the production cylinder head. It is noted
that the duct reduces the compression ratio to 17.4, compared
to the production engine with a compression ratio of 17.7. The
injector is supplied with pressurised hydrogen at 20 MPa from
a 1000 cm
3 accumulator, which is achieved using a custom-
made hydrogen boost pump system (Zenobalti, ZB-1301).
This system employs a single-stage, single acting pneumatic
hydrogen pump (Haskel, AG-62-86979) capable of 62 MPa
maximum hydrogen pressure with 50.8 cm
3 displacement per
pumping cycle and one pumping cycle per second, which
exceed both the ﬂow rate and injection pressure requirements
of the present study.
Engine instrumentation
The engine is instrumented with a piezoelectric in-cylinder
pressure transducer (Kistler 6056A with ampliﬁer 5015A)
installed onto the cylinder head. The crankshaft position is
monitored with a precision encoder (Autonics, 1800 pulses per
revolution) and the engine speed is controlled by an eddy
current dynamometer (FroudeHoffmann, AG-30HS). A uni-
versal engine control unit (Zenobalti, ZB-9013P) is used to
control the diesel common-rail pressure and adjust the in-
jection timing and duration for both diesel and hydrogen
direct injectors. Throughout the experiments, the engine
coolant temperature was controlled at 363 K (90
/C14C) to simu-
late a warmed-up engine operation.
Four engine-out emissions are measured including NO x
(NO and NO 2), smoke, carbon monoxide (CO) and unburnt
hydrocarbon (uHC). For NO x, a non-dispersive infrared ana-
lyser (Testo 350XL with 5% accuracy) is used while another
analyser measures CO and uHC (Horiba Mexa-584L with 1.7%
accuracy). An opacimeter is used for the detection of exhaust
smoke level (Horiba Mexa-600L, 0.15 m
-1 accuracy of absorp-
tion). The injected diesel fuel mass, injection duration, and
proﬁle are measured in a ‘Bosch-tube’ type injection rate
analyser with simulated backpressure as during the engine
operation. A detailed description of this experimental pro-
cedure is provided in Refs. [ 36]. The hydrogen consumption
was measured ofﬂine. In a constant volume vessel of 1.29 dm
3
volume, the pressure increase due to the injection of hydrogen
was measured, similar with the Zeuch method. The ideal-gas
law was applied to derive the injected hydrogen mass. The
tests were repeated for a range of injector electronic injection
durations to obtain an injector characteristic curve (injected
mass versus duration of the electronic command), which was
used in the engine tests to determine the required duration of
injection and the desired mass of injected hydrogen. The
measurement was performed using a high-precision pressure
sensor (Sensys, model PSH, 1 MPa full scale, 0.15% precision)
while the injector was kept at 363 K as in the engine. When the
Table 1 e Engine and injection system speciﬁcations.
Displacement volume 497.8 cm 3
Bore 83 mm
Stroke 92 mm
Piston Top-hat cylindrical bowl (55 mm diameter)
Number of valves 2 intake and 2 exhaust
Compression ratio 17.4
Swirl ratio 1.4
Injection system Hydrogen Diesel
Zenobalti Hydrogen Boost Pump System
Haskel Hydrogen Pump (AG-62-86979)
Bosch spray-guided GDI injector
Number of holes: 6 /C2160 mm
Steady ﬂow rate: 1.37 g/s at 20 MPa H
2 pressure
Bosch CP3, common-rail
Number of holes: 7
Nominal hole diameter: 134 mm
Included angle: 150 /C14
K-factor: 1.5
Discharge coefﬁcient: 0.86
HFR: 400 cm 3 in 30 s at 10 MPa pressure
international journal of hydrogen energy 46 (2021) 1302 e1314 1305

<!-- PDF_PAGE: 5 -->

hydrogen is injected in a gaseous state, the ﬂow through the
nozzle will be choked as long as the pressure ratio across the
injector exceeds two, a condition that is always fulﬁlled in this
study. As the theory of choked ﬂow suggests, the hydrogen
mass ﬂow rate will be independent of the backpressure. This
was tested by increasing the backpressure from atmospheric
pressure to 4 MPa, which corresponds to the in-cylinder
pressure at the time of hydrogen direct injection, and the
injected mass results agreed within 2%.
Engine operation strategy
The engine was operated at a constant speed of 2000 revolu-
tions per minute (rpm) at which the production engine rea-
ches the maximum torque output. Considering the additional
degrees of freedom associated with two fuel injectors, a fuel-
substitution strategy was employed for this study e the total
energy injected per cycle (820 J) was kept constant resulting in
an intermediate load of about 7.8 bar indicated mean effective
pressure (IMEP). When increasing the amount of injected
hydrogen by increasing the hydrogen injection duration, the
injection duration of diesel fuel was reduced to the corre-
sponding energy proportion. The combustion phasing was
controlled by adjusting the injection timing of diesel fuel for
each hydrogen substitution ratio and hydrogen injection
timing to keep the mid-point combustion phasing constant e
i.e. the crank-angle degree at 50% chemical energy conversion
(CA50) was ﬁxed at 11 ± 0.5
/C14CA after the top dead centre
(aTDC). This timing was found optimal for high efﬁciency in
previous studies utilising diesel, gasoline, and ethanol-based
fuels in the same engine [ 37e39]. Details of the operation
strategy are listed in Table 2.
The focus of this study was to evaluate the effects of energy
substitution ratio and hydrogen injection timing on the engine
performance and emissions. The ﬂexibility in the hydrogen
injection timing is the advantage of a hydrogen DI system and
will change the stratiﬁcation of hydrogen charge at the time of
diesel injection. Therefore, a wide range of hydrogen injection
timings was tested with the start of injection (SOI) at 180, 140,
90, 60, 40, and 20
/C14CA before TDC. These timings were sys-
tematically chosen e injecting hydrogen at 180 /C14CA bTDC
allowed a high level of premixing, approximating port fuel
injection mixing level, while the intake valves have not yet
completely closed and some charge might ﬂow back into the
intake manifold. The timing at 140
/C14CA bTDC is exactly after
the intake valve closing, followed by a range of intermediate
injection timings with an increasing level of stratiﬁcation. The
latest timing with the highest level of stratiﬁcation was
selected as 20
/C14CA bTDC, since at this timing and the highest
hydrogen substitution ratio, the hydrogen injection ends at
about 26
/C14CA aTDC and any later injection timing would lead
to undesired efﬁciency loss or misﬁre due to over-retarded
combustion phasing.
Data analysis
The in-cylinder pressure results were recorded for 240
continuous ﬁring cycles to ensure statistical relevance. The
data was ensemble-averaged to obtain in-cylinder pressure
trace and crank angle position, which were used to calculate
apparent heat release rate (aHRR), IMEP and CoV of IMEP.
Details of these calculations can be found in our previous
study [37]. Combustion phasing of CA10, CA50, and CA80 was
evaluated by calculating the crank angle position corre-
sponding to 10, 50, and 80% of total heat release. Knowing the
potential issue of combustion-induced noise in a premixed
charge combustion regime, the combustion noise was esti-
mated using the method introduced by Shahlari et al. [ 40,41].
In this method, the measured in-cylinder pressure was con-
verted to decibel (dB) by the application of ﬁlters for noise
transmission loss with consideration of engine structure and
the frequency response in the human hearing system. The
data sampling rate for this estimation was 200 kHz, which is
ten times higher than the required rate to resolve the atten-
uation function frequencies ranged in 0.1 e10 kHz.
Results and discussion
In-cylinder pressure and heat release rate analysis
The ensemble-averaged in-cylinder pressure and the derived
aHRR traces are presented in Fig. 2 for 0% (diesel baseline) to
50% hydrogen energy substitution ratio (H 2 fraction) at six
different hydrogen injection timings in the range of 180 to 20
/C14CA bTDC. In each plot, the hydrogen energy fraction is coded
by colour of the traces. The arrows illustrated on the aHRR
traces denote the diesel injection timing and duration selected
for a ﬁxed mid-point combustion phasing (CA50). The general
observation from these plots is that, for all six injection tim-
ings tested in the present study, up to 50% hydrogen energy
substitution was achieved with no pre-ignition or knocking
issues. This marks a signiﬁcant beneﬁt of hydrogen direct
injection effectively utilising the overall lean stratiﬁed
hydrogen charge. It has to be noted that small pressure ﬂuc-
tuations are visible on some of the pressure traces e while this
Table 2 e Engine operating and fuel injection conditions.
Engine speed [rpm] 2000
Intake air pressure [kPa] 101.3 (Natural aspiration)
Intake air
temperature [K]
300
Coolant (water)
temperature [K]
363
Net IMEP [kPa] 740 e800
Fuel Hydrogen Diesel
Cetane number e 51
Fuel density at 15 /C14C
[kg/m3]
0.089 848
Low heating value [MJ/kg] 119.7 43.4
Fuel injection pressure
[MPa]
20 100
Fuel injection timing
[/C14CA bTDC]
180, 90, 60, 40, 20 7 e3
Combustion phasing
[CA50, /C14CA aTDC]
11
Total energy input [J/
cycle]
820
Energy fraction [%] 0, 20, 30, 40, 50 100, 80, 70, 60, 50
Injection duration [ /C14CA] 0, 24, 30, 36, 42 11.7, 10.9, 10.2, 9.6, 9.2
international journal of hydrogen energy 46 (2021) 1302 e13141306

<!-- PDF_PAGE: 6 -->

might be an indication of knock, it is in fact the natural fre-
quency of the combustion chamber, ampliﬁed by the some-
what recessed pressure sensor mount. Knock produces a
signiﬁcant acoustic noise which was not detected during the
engine operation.
The in-cylinder pressure traces in Fig. 2 show a noticeable
trend in the end-of-compression pressure e the pressure at
TDC shows a monotonic increase with the addition of
hydrogen, which is prominent at all injection timings but 20
/C14CA bTDC. A close inspection suggests the TDC pressure gap
between 50% hydrogen energy fraction and the diesel baseline
decreases as the hydrogen injection timing is more retarded.
For hydrogen injection at 20
/C14CA bTDC, the injection lasted
beyond the TDC for all hydrogen energy fractions leading to
no compression pressure gap. The increased compression
pressure at higher hydrogen energy fraction means decreased
ignition delay for diesel combustion. For ﬁxed combustion
phasing (CA50), this required retarded diesel injection timing.
Interestingly, the ignition delay of diesel fuel remains roughly
constant at all tested operating conditions as the higher
compression pressure and later diesel injection timing bal-
ance out.
The hydrogen injection at 180
/C14CA bTDC approaches the
conditions of hydrogen port fuel injection and creates the
most homogeneous hydrogen mixture in the test matrix of
this study. With increasing hydrogen energy fraction, the peak
aHRR increases indicating increased premixed burn. Similar
trends are observed for the hydrogen injection at 140 and 90
/C14CA bTDC with increasing peak aHRR for higher hydrogen
energy fraction. However, for later injection timings of 60 to 20
/C14CA bTDC, the trend is reversed with the peak aHRR
decreasing for higher hydrogen energy fraction. This suggests,
at the hydrogen injection timing later than 60
/C14CA bTDC, a
critical level of hydrogen stratiﬁcation was achieved to cause
sequential ignition of mixtures and ﬂame propagation while
avoiding spontaneous ignition of the large volume of mix-
tures. For the two most retarded injection timings of 40 and 20
/C14CA bTDC, this charge stratiﬁcation effect is most pronounced
as the hydrogen injection is overlapped with the diesel in-
jection. It is believed that, for these two hydrogen injection
timings, the time available for mixing of hydrogen is insufﬁ-
cient and therefore, a large portion of the hydrogen mixture is
burnt in a mixing-controlled combustion mode.
For a ﬁxed hydrogen energy fraction of 20% and 50%, the in-
cylinder pressure and aHRR traces of Fig. 2 were replotted to
further discuss this important hydrogen injection timing ef-
fect in an H2DDI engine. The results are shown in Fig. 3 .A ta
lower hydrogen energy fraction of 20%, the aHRR maintains its
characteristic shape and width of the peak. As the hydrogen
charge stratiﬁcation increases by delaying the injection, the
peak aHRR increases up to the hydrogen start of injection of 60
/C14CA bTDC. This indicates that the stratiﬁed charge of
hydrogen can combust at a faster rate, either through being
entrained into the diesel jet or by consequent ﬂame
Fig. 2 e The effect of hydrogen energy fraction (indicated by the line colour) on in-cylinder pressure and apparent heat
release rate (aHRR) at ﬁxed hydrogen injection timings (SOI: start of injection). The injection timing and duration of diesel
fuel are annotated by the arrows at the bottom of the plot. The end of hydrogen injection is annotated at two latest hydrogen
injection timing cases ((e) and (f)). (For interpretation of the references to color/colour in this ﬁgure legend, the reader is
referred to the Web version of this article.)
international journal of hydrogen energy 46 (2021) 1302 e1314 1307

<!-- PDF_PAGE: 7 -->

propagation. For later 40 and 20 /C14CA bTDC, however, this no
longer is the case with the peak aHRR showing a decreasing
trend. This suggests widespread fuel-rich hydrogen mixtures
which cannot sustain the same rate of aHRR. At a higher en-
ergy fraction of 50% hydrogen, the hydrogen mixing appears
to play a more dominant role than that at 20% hydrogen en-
ergy fraction. The diesel injection timing had to be consis-
tently advanced for retarded hydrogen injection timing to
maintain the CA50, leading to the start of combustion earlier
in the cycle. The peak aHRR shows a decreasing trend with
retarded hydrogen injection timing, which suggests mixing-
limited combustion.
TDC pressure, peak aHRR and combustion phasing
The trends observed from the in-cylinder pressure and aHRR
traces are further discussed using the end-of-compression
pressure (TDC pressure), the peak value of the aHRR and the
characteristic combustion phasing values (CA10, CA50 and
CA80 corresponding to 10%, 50% and 80% of total heat release,
respectively) for all tested conditions of the present study. The
results are plotted in Fig. 4.
Previously in Fig. 2 , the in-cylinder pressure traces
exhibited a trend of increasing TDC pressure due to the mass
of gaseous hydrogen added into the cylinder, which was less
pronounced for later hydrogen injection timings. This inter-
esting parameter is presented in Fig. 4 (top-left). As expected,
the TDC pressure almost directly varies with hydrogen energy
fraction for most of the hydrogen injection timings. This is
particularly noticeable from earlier injection timings of 180 to
90
/C14CA bTDC. Thermodynamic calculation suggests that be-
sides the added mass, the early injection of hydrogen also
induces some compression heating of the charge (up to 12 K at
TDC at 50% H
2 fraction). However, as the injection timing is
more retarded, the TDC pressure increase due to hydrogen
direct injection generally becomes lower. This was likely a
balance of the increased compression heating due to
hydrogen mass addition and the competing cooling effect of
hydrogen injected into hot compressed charge at later injec-
tion timings, leading to a net-zero effect on the charge
temperature. Notably, the latest 20
/C14CA bTDC injection shows
no change in the TDC pressure since the injection of hydrogen
lasted well into the expansion stroke.
The value of the peak aHRR ( Fig. 4 , bottom-left) is of high
importance to understand the underlying phenomena as
discussed above. The plot shows that the peak aHRR value
varies to an increase in the hydrogen energy fraction differ-
ently depending on the hydrogen injection timing. The results
can be grouped into two with the earlier hydrogen injection
timings of 180 to 90
/C14CA bTDC showing little change or mod-
erate increase and the later hydrogen injection timings of 60 to
20
/C14CA bTDC displaying decreasing peak aHRR with increasing
hydrogen energy fraction. For the earlier hydrogen injection
timings, the value of peak aHRR exceeds the diesel baseline at
all hydrogen energy fractions, indicating a large amount of
entrained hydrogen combusting simultaneously with the
diesel fuel. With increased hydrogen stratiﬁcation for the later
hydrogen injection timings, the peak aHRR declined due to an
increased role of mixing-controlled combustion and poten-
tially diffusion ﬂames. Given a signiﬁcantly reduced concern
on the smoke-NO
x trade-off due to hydrogen combustion, the
lower peak aHRR at the later hydrogen injection timings,
which is lower than the diesel baseline, is promising for
reduced thermal NO formation - this will be discussed in the
following section.
As mentioned previously ( Table 2 ), the CA50 was kept
constant at 11 ± 0.5
/C14CA aTDC by adjusting the diesel injection
timing. At this ﬁxed CA50 condition, CA10 shows a mixed
trend depending on the hydrogen energy fraction and injec-
tion timing. Overall, the CA10 is measured later than the
diesel baseline at all H2DDI cases. This indicates the capacity
of hydrogen entrained in the diesel jet to accelerate the initial
combustion to reach the CA50 point in a shorter time. With
increasing hydrogen energy fraction, the CA10 decreases for
the late hydrogen injection timings of 60 to 20
/C14CA bTDC. This
was because high levels of hydrogen charge stratiﬁcation
caused slower combustion within fuel-rich hydrogen mix-
tures and thus took a longer time to reach the same CA50.
Among these three hydrogen injection timings, the earlier 60
/C14CA bTDC shows higher CA10 at any ﬁxed hydrogen energy
Fig. 3 e Effect of hydrogen injection timing on in-cylinder pressure and apparent heat release rate (aHRR) at selected
hydrogen energy fractions of 20% (left) and 50% (right). The injection timings and durations of diesel fuel for the different
hydrogen injection timing cases are annotated by the arrows at the bottom of the plots.
international journal of hydrogen energy 46 (2021) 1302 e13141308

<!-- PDF_PAGE: 8 -->

fraction due to a lower level of fuel-rich hydrogen mixtures. At
the earliest hydrogen injection timing of 180 /C14CA bTDC, a
directly opposite trend of increasing CA10 with increasing
hydrogen energy fraction is measured. As mentioned previ-
ously, this is the case with the homogeneous hydrogen mix-
tures, which therefore accelerates the dual-fuel combustion.
The intermediate injection timings of 140 and 90
/C14CA bTDC
show a transitional behaviour between this 180 /C14CA bTDC
injection and the late injection timings.
Similarly, CA80 with increasing hydrogen energy share
shows a mixed trend governed by the hydrogen injection
timing. For the 180
/C14CA bTDC, with increasing diesel substi-
tution, hydrogen ﬂame speed increases while the entrainment
of unburnt gases into burnt diesel plumes reduces due the
reduced diesel injection durations. The former effect appears
to prevail since the CA80 increases with higher hydrogen
fraction at 180
/C14CA bTDC injection timing. At intermediate
hydrogen injection timings of 140 and 90 /C14CA bTDC, the CA80
decreases as it maintained a high burning rate in a stratiﬁed
hydrogen charge. For the late hydrogen injection timings of 60
to 20
/C14CA bTDC, the CA80 tends to increase again with
increasing hydrogen energy fraction, which indicates a
mixing-controlled combustion mode. It was noted, the 90
/C14CA
bTDC injection achieved both the fastest initial burn (CA10 to
CA50) and late-cycle burn (CA50-CA80), suggesting the opti-
mised charge stratiﬁcation. It was also noted, at the latest
injection timing of 20
/C14CA bTDC, the CA80 is similar to the
diesel baseline, suggesting a comparable extent of mixing-
controlled combustion.
Engine power output and indicated efﬁciency
The engine power output and indicated efﬁciency are esti-
mated based on the ensemble-averaged indicated mean
effective pressure (IMEP) using the known lower heating value
of fuel injected per cycle ( Fig. 5 , top-left panel). Since the
fuelling rate was kept constant throughout the study, the IMEP
and the indicated efﬁciency follow the same trend. Relative to
the diesel baseline, the IMEP and efﬁciency are higher at all
hydrogen energy fractions and injection timings except for the
latest hydrogen injection at 20
/C14CA bTDC, which shows a
deteriorated efﬁciency. The combustion is stable with low
cyclic variability of IMEP, with the coefﬁcient of variation
(CoV) of IMEP below 3% for all tested conditions. Relative to the
baseline diesel condition, the CoV is only marginally higher
except for the 20
/C14CA bTDC injection, where it increases lin-
early with the hydrogen energy fraction up to about 3%, which
is still well below the limit of unstable combustion.
It is interesting to note that even at low hydrogen energy
fraction and early injection, the engine efﬁciency does not
deteriorate despite the very lean hydrogen global equivalence
ratio ( 4 z 0.1 at 20% hydrogen fraction). This highlights the
advantages of using diesel injection as an ignition source e
the high momentum and mixing induced by the diesel fuel
injection successfully entrains the lean hydrogen mixture,
which then co-combusts with the diesel fuel, leading to an
even increased peak aHRR at the time of ignition (c.f. Fig. 4). As
mentioned previously, the part of the hydrogen which did not
get entrained into the diesel jets was likely to burn when it
Fig. 4 e Effect of hydrogen energy fraction and injection timing on TDC pressure, peak aHRR and combustion phasing (CA10,
CA50, and CA80).
international journal of hydrogen energy 46 (2021) 1302 e1314 1309

<!-- PDF_PAGE: 9 -->

was mixed with hot combustion products of the diesel com-
bustion, or at sufﬁcient stratiﬁcation, ﬂame propagation
would occur within the hydrogen mixtures. At the tested
conditions of this study, no pre-ignition or knocking was
detected on the cylinder pressure traces, therefore it is likely
that the hydrogen mixture did not undergo autoignition. In
any case, the conversion of the hydrogen was sufﬁciently fast
to reduce the role of heat release late in the cycle, leading to an
even advanced timing of CA80 for the early injected hydrogen
cases.
The trends of the indicated efﬁciency highlight the role of
the hydrogen charge stratiﬁcation achieved by the variation of
hydrogen injection timing. The highest indicated efﬁciencies
are measured at the intermediate hydrogen injection timings
of 60
/C14and 90 /C14CA bTDC; this observation is universal at all
tested hydrogen energy fractions. The explanation of the
observed efﬁciency trends is again offered by the in-cylinder
pressure and aHRR traces ( Figs. 2 and 3) and the combustion
phasing results ( Fig. 4 right). The cases with these interme-
diate hydrogen injection timings result in the fastest com-
bustion as indicated by a high peak aHRR and short burn
duration. This indicates a level of hydrogen charge stratiﬁca-
tion, which enabled fast ﬂame propagation through the
remaining hydrogen mixtures which readily got entrained
into the diesel jets. It was also likely that the wall heat losses
are minimised by the hydrogen charge stratiﬁcation.
At earlier hydrogen injection timings, a more homogenous
mixture formed, which was very lean even at the highest
hydrogen energy fractions (global 4
H2 z 0.25 at 50% energy
fraction). Therefore, only the hydrogen entrained by the diesel
jets could readily combust at ignition while the subsequent
processes of ﬂame propagation and/or mixing with hot burnt
gases proceed at a slower rate leading to a somewhat deteri-
orated efﬁciency compared to intermediate injection timing.
On the other hand, when hydrogen was injected late, the time
available for hydrogen mixture formation was short and
hydrogen was likely to undergo diffusion combustion as pre-
viously discussed on the aHRR traces ( Fig. 2) and late timing of
CA80 (Fig. 4). This would delay the conversion of hydrogen to
late after the TDC, considerably deteriorating the indicated
efﬁciency which became lower than the efﬁciency of the
baseline diesel combustion.
Engine-out emissions
The nitric oxides (NO X) are the pollutant of the primary
concern in hydrogen engines and therefore, are exclusively
discussed using the results shown in Fig. 6. The plot on the left
side presents the total emissions of nitric oxides (NO and NO 2)
for a variation of hydrogen energy fraction and injection
timing. Additionally, the NO
x emissions are correlated with
the peak aHRR of Fig. 4 to discuss the role of the premixed
combustion and the high ﬂame temperature induced by the
fast combustion on the formation of NO
x (Fig. 6 , right). This
was of particular interest given Fig. 4 showed increasing or
decreasing peak aHRR trends for higher hydrogen fraction
depending on the hydrogen injection timing. The dual-fuel
combustion of hydrogen and diesel leads to increased for-
mation of NO
x compared to the diesel baseline. At all injection
timings, the emission of NO x increases almost linearly with
the hydrogen energy fraction, and the highest detected
emission is about twice higher than the diesel baseline
emission. While the increased NO
x is expected since the
adiabatic ﬂame temperature of hydrogen at stoichiometric
Fig. 5 e The effect of hydrogen energy fraction and injection timing on the indicated mean effective pressure (IMEP),
coefﬁcient of variation of IMEP, and indicated efﬁciency.
international journal of hydrogen energy 46 (2021) 1302 e13141310

<!-- PDF_PAGE: 10 -->

conditions exceeds the adiabatic ﬂame temperature of diesel
fuel by about 200 K, important differences are observed among
the results at different hydrogen injection timings. The high-
est emission of NO
x is detected at intermediate hydrogen in-
jection timings of 60 and 90 /C14CA bTDC, which also exhibit the
highest efﬁciency, highest peak aHRR, and the highest peak
in-cylinder pressure as discussed in the previous sections.
This is meaningful since the high peak aHRR is likely associ-
ated with large zones with stratiﬁed mixtures of hydrogen
with conditions near stoichiometry, which were readily
combusted and at the same time led to conditions favourable
for NO
x production. The lower NOx emissions at 180 /C14CA bTDC
injection can be explained by a higher homogeneity of
hydrogen charge, which resulted in a formation of less
extensive hot and lean zones. On the other hand, the late in-
jection of hydrogen led to diffusion combustion, and there-
fore, the ﬂame temperature reduced and thereby limiting the
NO
x production. When both the efﬁciency and low NO x are
considered, the optimised level of hydrogen stratiﬁcation was
achieved with the hydrogen injection timing of 40
/C14CA bTDC e
the combustion was fast nevertheless the extent of hot and
lean mixtures was sufﬁciently small to limit the NO x forma-
tion at about 11 g/kWh e some 40% increase over the diesel
baseline.
Fig. 6 (right) shows both positive and negative correlations
between the peak aHRR and engine NO x emission depending
on the hydrogen injection timing while the arrows indicate
increasing hydrogen energy fraction. For early hydrogen in-
jection timing of 180 to 90
/C14CA bTDC, the overall positive
correlation is exhibited, which was attributed to the higher
ﬂame temperature and the extent of the readily ignitable lean
and stoichiometric charge as discussed previously. By
contrast, the emission of NO
x increases despite decreased
peak aHRR for later injection timings of 60 to 20 /C14CA bTDC.
This suggests the peak aHRR inducing higher ﬂame temper-
ature alone cannot explain the NO
x tendency of hydrogen-
diesel dual-fuel combustion. As previously shown in Fig. 2 ,
the peak aHRR decreased but with extended width at higher
hydrogen energy fraction, during which the hydrogen-diesel
diffusion ﬂames could induce signiﬁcant thermal NO forma-
tion. While the advantage of H2DDI employing very late
hydrogen injection timings on NO
x reduction is demonstrated,
the NO x emission is still an outstanding issue, which will
require further investigation.
Other engine-out emissions including smoke (opacity),
unburnt hydrocarbons (uHC), and carbon monoxide (CO) are
shown in Fig. 7 . In consideration of intense premixed com-
bustion exhibited in early hydrogen injection timings, the
combustion-induced noise is also presented for all tested
conditions of the present study. It should be reminded that the
hydrocarbon-based emissions of smoke, uHC, and CO are
originated from diesel fuel and engine oil combustion and
thus are expected to decrease as the hydrogen energy fraction
increase. The smoke opacity shows this expected trend with a
minimum of 58% reduction. This was expected as soot for-
mation would be reduced due to added hydrogen. Also,
increased hydrogen would produce a higher concentration of
hydroxyl (OH) radicals, which is known to aid the oxidation of
soot. The intermediate timing of hydrogen injection leads to
virtually smokeless combustion while other injection timings
achieve a factor of three to four decreases with low sensitivity
to the actual hydrogen fraction.
The measured level of uHC/CO emissions is extremely low.
The uHC concentration is in the range of 6 e11 ppm, which is
at the low-end of the detection range of the used gas analyser
with a full-scale range of 10,000 ppm. The emission of CO also
shows a very low level for all tested operating conditions.
Trend-wise, the hydrogen injection at intermediate timings
appears to achieve the lowest CO emissions regardless of the
hydrogen energy fraction with a factor of three to four over the
diesel baseline being demonstrated. At a late hydrogen in-
jection condition, the CO emission tends to increase with the
hydrogen energy fraction. Considering the potential diffusion
ﬂames of hydrogen, it is interpreted that some diesel fuel was
Fig. 6 e Nitrogen oxides (NO x) emissions for various hydrogen energy fractions and injection timings (left) and the
correlation of NOx emission to the peak apparent heat release rate (aHRR, right). The arrows on the left plot indicate the
direction of increasing hydrogen energy fraction at each hydrogen injection timing. The uncertainty of NOx emission
measurement is ±5%.
international journal of hydrogen energy 46 (2021) 1302 e1314 1311

<!-- PDF_PAGE: 11 -->

mixed into a very fuel-rich hydrogen charge, which did not
lean-out until late-cycle, when the in-cylinder temperatures
were below the threshold needed for the oxidation of CO.
The noise emission (Fig. 7, top-right panel), estimated from
the pressure-trace using the method developed by Shahlari
et al. [ 35,36] shows the early hydrogen injection at 180 to 90
/C14CA bTDC resulted in one to two dB higher combustion-
induced noise than that of the diesel baseline. As discussed
previously, the large volume of the readily ignitable mixture at
the early hydrogen injection timings led to a fast pressure rise
at ignition, which increased the noise above the level of
baseline diesel combustion. In this aspect, a great advantage
of H2DDI employing later injection timings is demonstrated,
leading up to 6 dB reduction in noise e corresponding to a 50%
reduced emitted acoustic power e when diffusion ﬂames are
effectively utilised.
Conclusions
The performance and emissions of the hydrogen-diesel dual
direct-injection (H2DDI) engine combustion concept have
been investigated in an automotive-size single-cylinder
compression ignition engine at an intermediate engine load.
The combustion phasing at 50% fuel energy conversion (CA50)
was ﬁxed at 11
/C14CA after the top dead centre and a range of
hydrogen injection timings (180 e20 /C14CA bTDC) and hydrogen
energy fractions (0e50%) was tested. The engine performance
was evaluated based on the in-cylinder pressure measure-
ment to derive the indicated mean effective pressure, efﬁ-
ciency, combustion phasing, and apparent heat release rate
and put into perspective of the engine-out NO
x, CO, uHC, and
smoke emissions. The main ﬁndings are summarised and
conclusions are drawn as follows:
1. H2DDI combustion at controlled CA50 and up to 50%
hydrogen energy fraction is feasible at all injection timings
of hydrogen without pre-ignition or knocking. The cyclic
variation of IMEP is below 3%, indicating stable operation.
2. Direct injection of hydrogen into the cylinder induces up to
10% increase in the end-of-compression pressure, which is
associated with additional compression work. At later in-
jection timings, this effect is less pronounced.
3. Under the conditions of this work, the shape of the
apparent heat release rate (aHRR) resembles that of the
baseline diesel combustion, except when hydrogen is
injected late resulting in insufﬁcient time for mixing, in
which case slower aHRR indicative of a hydrogen mixing-
controlled combustion is observed.
4. A complex interplay between the aHRR at ignition, com-
bustion duration, efﬁciency, and NO
x emission, governed
by the hydrogen injection timing, is unveiled. With
retarding the hydrogen injection from the bottom dead
centre, the stratiﬁcation of hydrogen charge increases.
With increasing the hydrogen energy fraction and the
hydrogen stratiﬁcation, the amount of hydrogen entrained
into the diesel jets would increase and the stratiﬁed charge
outside the diesel jets would burn faster. This leads to
higher in-cylinder temperatures, which along with the
high hydrogen adiabatic ﬂame temperature results in an
increased formation of NO
x, additionally exacerbated by a
stratiﬁed hydrogen charge. Nevertheless, with even later
Fig. 7 e Engine-out emissions of smoke (opacity), unburnt hydrocarbon (uHC), and carbon monoxide (CO) as well as
estimated combustion-induced noise for a variation of hydrogen energy fraction and hydrogen injection timing.
Measurement uncertainties: Smoke: 0.1% absolute, uHC: ±0.04 g/kWh, CO: ±0.56 g/kWh.
international journal of hydrogen energy 46 (2021) 1302 e13141312

<!-- PDF_PAGE: 12 -->

hydrogen injections of 40 and 20 /C14CA bTDC, the available
time for mixing of hydrogen becomes insufﬁcient, result-
ing in diffusion combustion of hydrogen. This results in
lower combustion noise and reduced formation of NO
x.
The carbon-based emissions of H2DDI combustion are in
general lower than the selected diesel baseline except at
extreme hydrogen injection timings.
5. The results demonstrate that the overall best compromise
of efﬁciency and emissions might be achieved by setting
the hydrogen injection timing at 40
/C14CA bTDC and the
hydrogen energy fraction at 50%. The efﬁciency, uHC and
CO emissions in such operation remain uncompromised
relative to the diesel baseline, while achieving a ten-fold
decrease in smoke emission and 6 dB noise reduction.
The NOx emission remains at 11 g/kWh, which marks a
40% increase relative to the diesel baseline. While it is still
problematic, it is considered a moderate increase relative
to port-injection hydrogen engines.
Declaration of competing interest
The authors declare that they have no known competing
ﬁnancial interests or personal relationships that could have
appeared to inﬂuence the work reported in this paper.
Acknowledgments
Experiments were performed at the UNSW Engine Research
Laboratory, Sydney, Australia. The ﬁnancial support for this
research project was provided by the Australian Renewable
Energy Agency (ARENA). The authors thank Alexander Knaﬂ
and Marcus Becher at MAN Energy Solutions for useful dis-
cussions and additional funding support. A signiﬁcant tech-
nical contribution made by Bryce Edmonds for the H2DDI
engine setup and hydrogen system installation is also
acknowledged.
references
[1] Yip HL, Srna A, Yuen ACY, Kook S, Taylor RA, Yeoh GH, et al.
A review of hydrogen direct injection for internal
combustion engines: towards carbon-free combustion. Appl
Sci 2019;9:1 e30. https://doi.org/10.3390/app9224842.
[2] Verhelst S. Recent progress in the use of hydrogen as a fuel
for internal combustion engines. Int J Hydrogen Energy
2014;39:1071e85. https://doi.org/10.1016/
j.ijhydene.2013.10.102.
[3] Verhelst S, Wallner T, Sierens R. Hydrogen-Fueled internal
combustion engines. Handb Hydrog Energy 2014:821 e902.
https://doi.org/10.1201/b17226.
[4] Verhelst S, Wallner T. Hydrogen-fueled internal combustion
engines. Prog Energy Combust Sci 2009;35:490 e527. https://
doi.org/10.1016/j.pecs.2009.08.001.
[5] Das LM. Hydrogen-oxygen reaction mechanism and its
implication to hydrogen engine combustion. Int J Hydrogen
Energy 1996;21:703 e15. https://doi.org/10.1016/0360-3199(95)
00138-7.
[6] Mehra RK, Duan H, Juknelevi /C20cius R, Ma F, Li J. Progress in
hydrogen enriched compressed natural gas (HCNG) internal
combustion engines - a comprehensive review. Renew
Sustain Energy Rev 2017;80:1458 e98. https://doi.org/10.1016/
j.rser.2017.05.061.
[7] Wang S, Ji C. Cyclic variation in a hydrogen-enriched spark-
ignition gasoline engine under various operating conditions.
Int J Hydrogen Energy 2012;37:1112 e9. https://doi.org/
10.1016/j.ijhydene.2011.02.079.
[8] Das LM. Hydrogen engines: a view of the past and a look into
the future. Int Assoc Hydrog Energy 1990;15:425 e43. https://
doi.org/10.1016/0360-3199(90)90200-I.
[9] Mathur HB, Das LM. Performance characteristics of a
hydrogen fuelled S.I. engine using timed manifold injection.
Int J Hydrogen Energy 1991;16:115 e27. https://doi.org/
10.1016/0360-3199(91)90038-K.
[10] King RO, Rand M. The hydrogen engine. Nature
1954;174:975e6.
[11] Anzilotti WF, Rogers JD, Scott GW, Tomsic VJ. Combustion of
hydrogen as related to knock - parallel behavior of hydrogen
and parafﬁnic fuels. Ind Eng Chem 1954;46:1314 e8.
[12] Anzilotti WF, Tomsic VJ. Combustion of hydrogen and
carbon monoxide as related to knock. Proc Combust Inst
1955;5:356e66.
[13] White CM, Steeper RR, Lutz AE. The hydrogen-fueled internal
combustion engine: a technical review. Int J Hydrogen
Energy 2006;31:1292 e305. https://doi.org/10.1016/
j.ijhydene.2005.12.001.
[14] Heffel JW. NOx emission and performance data for a
hydrogen fueled internal combustion engine at 1500 rpm
using exhaust gas recirculation. Int J Hydrogen Energy
2003;28:901e8. https://doi.org/10.1016/S0360-3199(02)00157-
X.
[15] Wallner T, Matthias NS, Scarcelli R, Kwon JC. Evaluation of
the efﬁciency and the drive cycle emissions for a hydrogen
direct-injection engine. Proc Inst Mech Eng - Part D J
Automob Eng 2013;227:99 e109. https://doi.org/10.1177/
0954407012461875.
[16] Tang X, Kabat DM, Natkin RJ, Stockhausen WF. Ford P2000
hydrogen engine dynamometer development. SAE Tech Pap
2002. https://doi.org/10.4271/2002-01-0242.
[17] Szwaja S, Naber JD. Dual nature of hydrogen combustion
knock. Int J Hydrogen Energy 2013;38:12489 e96. https://
doi.org/10.1016/j.ijhydene.2013.07.036.
[18] Shudo T, Nabetani S. Analysis of degree of constant volume
and cooling loss in a hydrogen fuelled SI engine. SAE Tech
Pap 2001. https://doi.org/10.4271/2001-01-3561.
[19] Rahman MM, Hamada KI, Aziz A A. Characterization of the
time-averaged overall heat transfer in a direct-injection
hydrogen-fueled engine. Int J Hydrogen Energy
2013;38:4816e30. https://doi.org/10.1016/
j.ijhydene.2013.01.136.
[20] Wimmer A, Wallner T. H2-Direct injection e a highly
promising combustion concept. SAE Tech Pap 2005. https://
doi.org/10.4271/2005-01-0108.
[21] Takagi Y, Mori H, Mihara Y, Kawahara N, Tomita E.
Improvement of thermal efﬁciency and reduction of NOx
emissions by burning a controlled jet plume in high-pressure
direct-injection hydrogen engines. Int J Hydrogen Energy
2017;42:26114e22. https://doi.org/10.1016/
j.ijhydene.2017.08.015.
[22] Takagi Y, Oikawa M, Sato R, Kojiya Y, Mihara Y. Near-zero
emissions with high thermal efﬁciency realized by
optimizing jet plume location relative to combustion
chamber wall, jet geometry and injection timing in a direct-
injection hydrogen engine. Int J Hydrogen Energy
2019;44:9456e65. https://doi.org/10.1016/
j.ijhydene.2019.02.058.
international journal of hydrogen energy 46 (2021) 1302 e1314 1313

<!-- PDF_PAGE: 13 -->

[23] Tanno S, Ito Y, Michikawauchi R, Nakamura M, Tomita H.
High-efﬁciency and Low-NOx hydrogen combustion by high
pressure direct injection. SAE Int J Engines 2010;3:259 e68.
https://doi.org/10.4271/2010-01-2173.
[24] Naganuma K, Honda T, Yamane K, Takagi Y, Kawamura A,
Yanai T, et al. Efﬁciency and emissions-optimized operating
strategy of a high-pressure direct injection hydrogen engine
for heavy-duty trucks. SAE Int J Engines 2010;2:132 e40.
https://doi.org/10.4271/2009-01-2683.
[25] Roy MK, Kawahara N, Tomita E, Fujitani T. Jet-guided
combustion characteristics and local fuel concentration
measurements in a hydrogen direct-injection spark-ignition
engine. Proc Combust Inst 2013;34:2977 e84. https://doi.org/
10.1016/j.proci.2012.06.103.
[26] Matthias NS, Wallner T, Scarcelli R. A hydrogen direct
injection engine concept that exceeds U.S. DOE light-duty
efﬁciency targets. SAE Int J Engines 2012;5:838 e49. https://
doi.org/10.4271/2012-01-0653.
[27] Obermair H, Scarcelli R, Wallner T. Efﬁciency improved
combustion system for hydrogen direct injection operation.
SAE Tech Pap 2010. https://doi.org/10.4271/2010-01-2170.
[28] Kawamura A, Sato Y, Naganuma K, Yamane K, Takagi Y.
Development project of a multi-cylinder DISI hydrogen ICE
system for heavy duty vehicles. SAE Tech Pap 2010. https://
doi.org/10.4271/2010-01-2175.
[29] Huang G, Li Z, Zhao W, Zhang Y, Li J, He Z. Effects of fuel
injection strategies on combustion and emissions of
intelligent charge compression ignition (ICCI) mode fueled
with methanol and biodiesel. Fuel 2020;274:117851. https://
doi.org/10.1016/j.fuel.2020.117851.
[30] Li Z, Zhang Y, Huang G, Zhao W, He Z, Qian Y, et al. Conteol
of intake boundary conditions for enabling clean combustion
in variable engine conditions under intelligent charge
compression ignition (ICCI) mode. Appl Energy
2020;274:115297. https://doi.org/10.1016/
j.apenergy.2020.115297.
[31] Kokjohn SL, Hanson RM, Splitter DA, Reitz RD. Fuel reactivity
controlled compression ignition (RCCI): a pathway to
controlled high-efﬁciency clean combustion. Int J Engine Res
2011;12:209e26. https://doi.org/10.1177/1468087411401548.
[32] Kalghatgi G, Johansson B. Gasoline compression ignition
approach to efﬁcient, clean and affordable future engines.
Proc Inst Mech Eng - Part D J Automob Eng 2018;232:118 e38.
https://doi.org/10.1177/0954407017694275.
[33] Aksu C, Kawahara N, Tsuboi K, Kondo M, Tomita E.
Extension of PREMIER combustion operation range using
split micro pilot fuel injection in a dual fuel natural gas
compression ignition engine: a performance-based and
visual investigation. Fuel 2016;185:243 e53. https://doi.org/
10.1016/j.fuel.2016.07.120.
[34] Chintala V, Subramanian KA. A comprehensive review on
utilization of hydrogen in a compression ignition engine
under dual fuel mode. Renew Sustain Energy Rev
2017;70:472e91. https://doi.org/10.1016/j.rser.2016.11.247.
[35] Zhou JH, Cheung CS, Leung CW. Combustion, performance,
regulated and unregulated emissions of a diesel engine with
hydrogen addition. Appl Energy 2014;126:1 e12. https://
doi.org/10.1016/j.apenergy.2014.03.089.
[36] Liu X, Srna A, Chan QN, Kook S. Effect of exhaust gas
recirculation and intake air E-boosting on gasoline
compression ignition combustion. SAE Int J Engines
2020;13:3e13. https://doi.org/10.4271/03-13-03-0025.
[37] Padala S, Woo C, Kook S, Hawkes ER. Ethanol utilisation in a
diesel engine using dual-fuelling technology. Fuel
2013;109:597e607. https://doi.org/10.1016/j.fuel.2013.03.049
.
[38] Woo C, Kook S, Rogers P, Marquis C, Hawkes E, Tupuﬁa S. A
comparative analysis on engine performance of a
conventional diesel fuel and 10% biodiesel blends produced
from coconut oils. SAE Int J Fuels Lubr 2015;8:597 e609.
https://doi.org/10.4271/2015-24-2489.
[39] Goyal H, Kook S, Hawkes E, Chan QN, Padala S, Ikeda Y.
Inﬂuence of engine speed on gasoline compression ignition
(GCI) combustion in a single-cylinder light-duty diesel
engine. SAE Tech Pap 2017;2017-March. https://doi.org/
10.4271/2017-01-0742.
[40] Shahlari AJ, Hocking C, Kurtz E, Ghandhi J. Comparison of
compression ignition engine noise metrics in low-
temperature combustion regimes. SAE Int J Engines
2013;6(2013):1. https://doi.org/10.4271/2013-01-1659. 1659.
[41] Shahlari AJ, Kurtz E, Hocking C, Antonov S. Correlation of
cylinder pressure-based engine noise metrics to measured
microphone data. Int J Engine Res 2015;16:829 e50. https://
doi.org/10.1177/1468087414552831.
international journal of hydrogen energy 46 (2021) 1302 e13141314
