<!-- PDF_PAGE: 1 -->

Combustion process and emissions of a heavy-duty engine fueled
with directly injected natural gas and pilot diesel
Qiang Zhang a,⇑, Menghan Li a, Sidong Shao b
a School of Energy and Power Engineering, Shandong University, Jinan 250061, China
b Weichai&Westport New Energy Inc., Weifang 261001, China
highlights
/C15 Emissions are analyzed in detail in combination with combustion parameters.
/C15 Combustion characteristics are evidently affected by the diffusion of natural gas.
/C15 CO emissions ﬁrst increase then decrease with the advance of injection timing.
/C15 NOx emissions deteriorate at higher injection pressures.
/C15 Thermal efﬁciency can be improved by raising injection pressure.
article info
Article history:
Received 19 April 2015
Received in revised form 7 July 2015
Accepted 6 August 2015
Available online 22 August 2015
Keywords:
Directly injected
Natural gas engine
Pilot diesel
Emissions
abstract
In this paper, the combustion process and emissions of a heavy-duty engine fueled with directly injected
natural gas and pilot diesel were experimentally explored. The experiments were carried out under two
operating points (A:1275 rpm BMEP 1.05 MPa, B:1550 rpm BMEP 1.05 MPa) with diesel rail pressure
(DRP) varied from 18 MPa to 30 MPa and start of natural gas injection (NSOI) in the range of 1 /C176BTDC
to 19 /C176BTDC. Based on the experimental results, as the injection timing advances, the maximum in-
cylinder pressure and NOx emissions increase, the ﬂame development duration and brake speciﬁc fuel
consumption (BSFC) decrease, the maximum heat release rate shows a trend of ﬁrst decrease and then
increase while the changing trend for carbon monoxide (CO) emissions is ﬁrst increase and then
decrease; as the injection pressure raises, the combustion process takes place earlier, causing negative
effects on nitrogen oxides (NOx) emissions; with higher engine speed, however, the combustion events
are delayed, leading to lower peak value of heat release rate, improved CO and NOx emissions, impaired
total hydrocarbon (THC) emissions and higher BSFC.
/C2112015 Elsevier Ltd. All rights reserved.
1. Introduction
In order to reduce toxic emissions as well as GHG (greenhouse
gas), natural gas engines are widely used on taxis, buses and light-
duty trucks. With the development of natural gas combustion tech-
nology, utilization of natural gas engines has also been extended to
heavy-duty trucks and marine main impellers, where good power
performance is in great demand [1–5]. Traditional spark-ignited
natural gas engines, limited by knocking and slow combustion rate,
suffer from impaired thermal efﬁciency [6–8]. Engines operating
with directly injected natural gas and pilot diesel use the technique
of injecting pilot diesel prior to natural gas injection; natural gas,
ignited by pilot diesel ﬂame, burns in a predominantly non-
premixed manner; in this case, uncontrollable auto-ignition can
be avoided and compression ratio comparable to diesel engine
http://dx.doi.org/10.1016/j.apenergy.2015.08.021
0306-2619//C2112015 Elsevier Ltd. All rights reserved.
Abbreviations: ATDC, after top dead center; BTDC, before top dead center; CA,
crank angle; CA_Pmax, crank angle of maximum cylinder pressure; CA_H.R.Rmax,
crank angle of maximum heat release rate; C.H.R, cumulative heat release; CNG,
compressed natural gas; CO, carbon monoxide; DPW, injection pulse width of pilot
diesel; DFMF, diesel fuel mass ﬂow; DRP, diesel rail pressure; DSOI, start of injection
of pilot diesel; ECU, electronic control unit; EGR, exhaust gas recirculation; EOI, end
of injection; GHG, greenhouse gas; GPW, injection pulse width of natural gas; GSOI,
start of natural gas injection; HC, hydrocarbon; HCCI, homogeneous charge
compression ignition; HCDI, homogeneous charge direct injection; H.R.R, heat
release rate; H.R.Rmax, maximum heat release rate; LNG, liqueﬁed natural gas;
MBF, mass burnt fraction; Pmax, maximum cylinder pressure; PSEP, pilot diesel to
natural gas injection separation; rpm, revolutions per minute; N, engine speed;
TFMF, total fuel mass ﬂow; THC, total hydrocarbon; US EPA, United States
Environmental Protection Agency.
⇑ Corresponding author. Tel.: +86 13791033095.
E-mail address: sduzqtg@163.com (Q. Zhang).
Applied Energy 157 (2015) 217–228
Contents lists available at ScienceDirect
Applied Energy
journal homepage: www.elsevi er.com/locat e/apenergy

<!-- PDF_PAGE: 2 -->

can be adopted, thus achieving low emission levels while main-
taining diesel like efﬁciency [9–12].
During the past decades, the beneﬁts and drawbacks for utiliza-
tion of engine fueled with directly injected natural gas and pilot
diesel have been sufﬁciently proved. Douville et al. [13] concluded
that the dynamic performance is maintained and CO 2 emissions
are reduced along with higher CH 4 emissions at all operating
points when an engine is varied from diesel engine to direct injec-
tion natural gas engine; the ignition delay is similar to that of reg-
ular diesel operation mode and the combustion rate is more
equally distributed, resulting in lower peak temperatures and con-
sequently, lower NOx emissions. According to Kalam and Masjuki
[14], the power output of direct injection natural gas engine is
slightly lower than gasoline engine while obviously higher than
conventional dual-fuel engine; It was found that, at full load, direct
injection natural gas engine produces higher HC and CO emissions
when compared with gasoline engine, lower HC and higher CO
emissions when compared with conventional dual-fuel engine.
Base on the previous studies, conclusion can be drawn that engines
fueled with directly injected natural gas and pilot diesel have per-
formance similar to conventional diesel and gasoline engines and
outperformed conventional dual fuel engines, however, there is
still room for further improvement of the combustion performance
and emission control remains a problem to comply with the more
stringent emission standard.
The methods of improving combustion and emission character-
istics of engines fueled with natural gas and pilot diesel have been
extensively studied in recent years, however, most of them are
focused on pilot-ignited premixed natural gas engines. It was
demonstrated by the results of Papagiannakis et al. [15] and Liu
et al. [16] that engine efﬁciency and CO and HC emissions can ben-
eﬁt from increasing pilot diesel quantity accompanied with raising
intake air temperature, however, harmful effects on engine
mechanical strength may be incurred at high loads. Adding hydro-
gen to natural gas also has very important impacts on the perfor-
mance of dual fuel engine. As mentioned in the study of Lounicia
et al. [17] and Navarro et al. [18], thermal efﬁciency, fuel economy
and all emissions except NOx can beneﬁt from the utilization of
this technique; but, the problems exist in the production and stor-
age process of hydrogen cannot be ignored. Adding EGR is another
methodology of improving engine performance; Abdelaal et al.
[19] presented that, with the employment of EGR on pilot ignited
natural gas engine, cylinder peak pressure, the maximum rate of
pressure rise along with HC, CO and NOx emissions can be consid-
erably reduced at the expense of increased complexity and mainte-
nance cost. Further, it was pointed out by Papagiannakis et al. [20]
that HC and CO can be possibly mitigated by the adjustment of the
engine tuning; and injection timing, however, is a parameter that
can be chosen for modiﬁcation to achieve better emission behavior.
Their hypothesis was conﬁrmed by Yang et al. [3] by evaluating the
effects of injection timing and pilot injection pressure on a natural
gas port injection dual-fuel engine, they summarized that combus-
tion and emission characteristics of dual-fuel engine can be evi-
dently improved by appropriately adjusting pilot injection
parameters and natural gas injection timing. For engines fueled
with directly injected natural gas and pilot diesel, the mixture
preparation duration of both fuels is relatively shorter, so we can
make the assumption that the injection strategy may play an even
more vital role in the optimization process for combustion and
emission characteristics; moreover, it is not difﬁcult to infer from
the proceeding studies that optimizing injection strategy is a feasi-
ble and cost-effective solution since no additional modiﬁcations
have to be done on the engine structure and there are no difﬁcul-
ties of refueling in the practical application. Several researches
have been conducted to ensure this theory from the prospective
of jet characteristics. Ouellette [21] characterized the jet
penetration and ﬂow distribution under various pressure ratio
and injection duration by the utilization of schlieren and shadow-
graph photography. His results showed that increasing pressure
ratio and injection duration could cause increases in jet penetra-
tion and jet diffusion rate. Both experimental and numerical inves-
tigations were performed by Chitsaz et al. [22] to explore the
behavior of gaseous fuel injection and it was concluded that tip
penetration could beneﬁt from higher pressure ratios and larger
nozzle diameters. To investigate the detailed jet ﬂow structures,
Yu et al. [23] adopted planar laser-induced ﬂuorescence to study
the mixture formation in direct injection gas engine. They proved
that the distribution of fuel/air mixture could be signiﬁcantly
improved at higher injection pressure by analyzing the turbulent
mixing process. In terms of the effects of injection strategy on
engine performance, Dumitrescu [24] investigated the inﬂuences
of injection pressure, injection timing on the combustion and emis-
sions of a single-cylinder two-stroke heavy duty engine by a set of
experiments at medium speed and low loads; according to their
ﬁndings, combustion rate and NOx emissions increase with gas
injection pressure while lower NOx emissions can be obtained by
appropriately delaying injection timing; however, their experi-
ments are performed at relatively low injection pressures from
10 MPa to16 MPa and they simply compared the emission results
at different operating point without in-depth analysis on the com-
bustion process. Harrington et al. [25] conducted developmental
tests on a six-cylinder four-stroke engine over AVL 8 modes with
three different operating strategies; their results suggested that
highest cycle NOx reduction can be achieved by optimizing injec-
tion timing without sacriﬁce of thermal efﬁciency; however, as a
result of the technique limitation, the injection pressure chosen
was 21 MPa and in addition, they did not present the optimization
process of the injection pressure. McTaggart-Cowan et al. [26–28]
investigated the effects of injection pressure on combustion and
emission characteristics on a four-stroke single-cylinder engine
by comparison of heat release rates and emissions at injection
pressures of 21 MPa and 30 MPa; On the basis of their experimen-
tal results, conclusions were drawn that the ignition and combus-
tion process of both fuels are shortened through the use of higher
injection pressure; NOx emissions are slightly inﬂuenced when
injection pressure raises while improved evidently by retarding
injection timing; CO emissions show different changing tendencies
for different engine speed with the increasing injection pressure;
though they tried to interpret the combustion events by in-
cylinder pressure traces and heat release rate, the explanations
seem to be insufﬁcient, it would be more convincing if the analyses
of combustion parameters and fuel economy are added. Therefore,
in order to get a thorough understanding of the combustion pro-
cess and how combustion, emission characteristics and fuel econ-
omy are related to each other in engines fueled with directly
injected natural gas and pilot diesel, a systematic study of this
issue is essential.
In this paper, the study of engines fueled with directly injected
natural gas and pilot diesel is extended to a commercial six-
cylinder heavy duty engine and investigation is carried out with
injection pressures up to 30 MPa, which is the highest permissible
value at present; the characteristics of cylinder pressure evolution,
heat release behavior, emission variation along with fuel economy
of a heavy-duty engine fueled with directly injected natural gas and
pilot diesel are analyzed by the aid of combustion phasing param-
eters (i.e. MBF0–10%, MBF50%, MBF10–50%, MBF10–90%). Besides,
the effects of injection strategy on each combustion phase are ana-
lyzed and suggestions on combustion and thermal efﬁciency
improvement are proposed for injection strategy optimization. Up
to now, in-depth description for each combustion phase, especially
the ﬁrst half of heat release (MBF10–50%) of engine fueled with
directly injected natural gas and pilot diesel, is particularly scarce.
218 Q. Zhang et al. / Applied Energy 157 (2015) 217–228

<!-- PDF_PAGE: 3 -->

2. Experimental apparatus and test method
The experiments were performed on a 6-cylinder, turbocharged
natural gas engine featured electrically controlled wastegate with-
out EGR. Speciﬁcations of the engine are listed in Table 1, deﬁnition
of injection parameters and schematic diagram of the test bed are
shown in Figs. 1 and 2 . The fuel subsystems of diesel and natural
gas were integrated and electronically controlled separately.
After pressurized and gasiﬁed, natural gas was provided to the fuel
regulating module and regulated to a proportionately lower pres-
sure to diesel. Both diesel and natural gas were injected into the
cylinder by a same Westport dual-fuel injector with a dual concen-
tric dual-needle design, where diesel was induced by the inner
nozzles and natural gas was induced by the outer nozzles. For tests
conducted in this paper, injection parameters such as injection
pressure and injection timing were adjusted by the fuel system
controller.
The engine was coupled to an eddy current dynamometer, by
which the engine torque and speed were measured. A Horiba
MEXA-7200 emission analyzer was used to obtain the engine emis-
sions of HC, CO and NOx. The cylinder pressure was measured by a
piezoelectric pressure transducer (Kistler 6067C) and data of 100
consecutive cycles were recorded by the AVL combustion analyzer
for future processing, corresponding crankshaft position was mea-
sured by a crank angle encoder (Kistler 2614A) with a resolution of
0.5/C176CA. The ﬂow rate of air was measured by a hot-ﬁlm type air
ﬂow meter. Fuel combustion rates of diesel and natural gas were
measure by a coriolis mass ﬂow meter (Emerson CNG050) and a
diesel consumption meter (AVL 733S) respectively. The accuracies
and measuring methods of measurements are given in Table 2. The
experiments reported here were conducted at two engine speed of
1275 rpm and 1550 rpm with BMEP of 1.05 MPa. Detailed test con-
ditions are listed in Table 3 .
The control strategy of fuel injection is to provide a small
amount of pilot diesel as the ignition source of the main fuel nat-
ural gas, which is injected directly into the cylinder after a certain
time interval. During the experimental process, the injection pulse
width of pilot diesel (DPW) and the pilot diesel to natural gas
Table 1
Engine speciﬁcations.
Item Speciﬁcations
Number of cylinder 6
Engine type Turbocharged, water cooled
Combustion chamber Re-entrant
Bore /C2 stroke (mm) 126 /C2 155
Displacement (L) 11.59
Compression ratio 17
Rated power (kW) 353
Rated speed (r min
/C0 1) 2100
Idle speed (r min /C0 1) 600
Fig. 1. Deﬁnition of injection parameters.
Fig. 2. The schematic diagram of the test bed.
Table 2
Accuracies and methods of measurements.
Parameter Measuring method Accuracy
Maximum pressure – ±1%
Crank angle – ±0.1 /C176
Diesel mass ﬂow rate – ±0.1%
Natural gas mass ﬂow rate – ±0.5%
HC emissions Flame ionization detector (FID) ±1 ppm
CO emissions Nondispersive infrared (NDIR) ±1 ppm
NOx emissions Chemiluminescent detector (CLD) ±1 ppm
Table 3
Test conditions.
Item Value
Fuel Natural gas and diesel
Speed 1275 rpm (A), 1550 rpm (B)
BMEP 1.05 MPa
DRP 18 MPa, 24 MPa, 30 MPa
NSOI 1–19 /C176BTDC
DPW 400
ls
PSEP 400 ls
Q. Zhang et al. / Applied Energy 157 (2015) 217–228 219

<!-- PDF_PAGE: 4 -->

injection separation (PSEP) were kept constant at 400 ls to ensure
the ignition stability of pilot diesel; the injection pulse width of
natural gas (GPW) was adjusted in accordance with the operating
conditions.
The averaged and smoothed cylinder pressure of 100 consecu-
tive cycles was acquired to eliminate the impact of cyclic variation
on HRR calculation [29]. The corresponding net heat release rate
was calculated with the following equation [30]:
dQ net
dh ¼ c
c /C0 1 p dV
dh þ 1
c /C0 1 V dp
dh ð1Þ
c ¼ Cp
CV
ð2Þ
where dQnet
dh is the net heat release rate, h is the crank angle, p is the
cylinder pressure, V is the working volume, Cp is the speciﬁc heat at
constant pressure and CV is the speciﬁc heat at constant volume.
The value of c is calculated from a polynomial function of in-
cylinder temperature, which can be obtained by the ideal gas state
equation. In this paper, the combustion parameters, such as 50% and
90% combustion phase angles, are calculated from the net heat
release rate.
3. Results and discussion
3.1. Cylinder pressure
Fig. 3 illustrates a typical curve of cylinder pressure along with
its corresponding rate of pressure rise. It is manifested by the
curves that the variation of cylinder pressure against crank angle
can be divided into the following stages:
/C15 The pure compression phase before pilot diesel injection, the
pressure of which is in good agreement with the motored line.
/C15 The mixture preparation phase, in which the cylinder pressure
is slightly lower than the motored line due to the heat absorbed
by the atomization and evaporation of the liquid fuel as well as
the chemical reactions before ignition.
/C15 The pilot diesel combustion phase and the injection process of
natural gas, the pressure rise rate of which increases rapidly
after the initiation of pilot fuel combustion and decreases
rapidly afterward; this is because the amount of diesel is tiny
(no more than 10%), thus resulting in very short combustion
duration; moreover, ﬂame extinction attributed to the cooling
effect of natural gas jet injected after the pilot ignition and
the heat absorbed during the physical and chemical delay
before the natural gas ignition may be another explanation for
this phenomenon; additionally, it can be noted that, in this
phase, the cylinder pressure trace is a little higher than the
motored line as a consequence of the heat release of pilot diesel.
/C15 The main fuel combustion phase; this is the predominant part
of the whole combustion process, during which, the pressure
rise rate shows a trend of ﬁrst rapid increase and then decrease
as a result of fuel exhaustion.
The cylinder pressure curves of different injection pressures and
injection timings at both operating points are depicted in Fig. 4 .
The corresponding maximum cylinder pressure and crank angle
-30 -15 0 15 30 45 60
-6
-4
-2
0
2
4
6
8
10
12
-30 -15 0 15 30 45 60
0
20
40
60
80
100
120
140
Crank angle (°CA)
dp/dθ
Rate of pressure rise (bar·CA°
-1
)NSOI=BTDC19°CA
DPR=24MPa
Cylinder pressure (bar)
 Motored line
 Cylinder pressure
Fig. 3. A typical in-cylinder pressure and corresponding pressure rise rate.
-30 -15 0 15 30 45 60
0
30
60
90
120
30
60
90
120
30
60
90
120
Crank angle (°CA)
NSOI1
NSOI4
NSOI7
NSOI10
NSOI13
Cylinder pressure (bar)
NSOI1
NSOI4
NSOI7
NSOI10
NSOI13
NSOI16
NSOI19
DRP=30MPa
DRP=24MPa
DRP=18MPa NSOI1
NSOI4
NSOI7
NSOI10
NSOI13
NSOI16
NSOI19
(a) 
-30 -15 0 15 30 45 60
0
30
60
90
120
150
30
60
90
120
150
30
60
90
120
150
Crank angle (°CA)
NSOI2
NSOI5
NSOI8
NSOI11
NSOI14
NSOI17
Cylinder pressure (bar)
NSOI2
NSOI5
NSOI8
NSOI11
NSOI14
NSOI17
NSOI2
NSOI5
NSOI8
NSOI11
NSOI14
NSOI17
DRP=18MPa
DRP=24MPa
DRP=30MPa
(b) 
Fig. 4. Cylinder pressure (a) A:N = 1275 rpm and (b) B:N = 1550 rpm.
220 Q. Zhang et al. / Applied Energy 157 (2015) 217–228

<!-- PDF_PAGE: 5 -->

of the maximum cylinder pressure are given in Fig. 5 . At engine
speed of 1275 rpm and injection pressure of 30 MPa, the advance-
ment of injection timing beyond 13 /C176BTDC is limited by the maxi-
mum pressure rise rate, namely, the signiﬁcantly deteriorated
combustion noise. As shown in Fig. 4, the cylinder pressure curves
illustrate two peak values with NSOI ranging from 1 /C176BTDC to 11 /C176
BTDC, where the ﬁrst peak takes place at the top dead center as
a consequence of the retarded initiation of combustion events
while the second peak induced by the heat release of main fuel nat-
ural gas occurs after a drop caused by the downward movement of
piston in the expansion stroke; as the injection timing advances
from 13 /C176BTDC to 19 /C176BTDC, the bulk of total heat is released prior
to the top dead center, resulting in more rapid rise and decline of
cylinder pressure with a single peak. It can also be noticed from
Fig. 4 that, at the same injection pressure, the maximum cylinder
pressure increases and the bulge area of cylinder pressure curve,
which is derived from the combustion of pilot diesel, becomes
more obvious with the advancing of injection timing. This is pri-
marily because the ignition delay of pilot diesel is prolonged with
advanced injection timing, providing more time for mixing,
thereby, more ﬂammable mixture is generated before ignition,
leading to increased contributions to cylinder pressure during the
combustion period of pilot fuel. Further, the injection rate and cor-
responding amount of fuel injected during unit time are increased
with higher injection pressure, which favors the mixing process
and the speed of ﬂame propagation, thus, resulting in increased
pressure rise rates and steeper cylinder pressure curves. This, how-
ever, can be further conﬁrmed by the simulations of Choi et al. [31].
Additionally, it can be seen from the curves that the cylinder pres-
sure before injections, especially near the end of compression
stroke, increases with the retarding injection timing as a result of
the higher exhaust temperature and subsequent raised exhaust
energy as well as consequent higher boost pressure. When com-
paring the cylinder pressure curves under different engine speeds,
it can be found that the changing rate of cylinder pressure at higher
engine speed is slower than that of lower engine speed since time
for each crank angle is shorter at higher engine speed and therefore
heat released within the same crank-angle period is reduced.
It can be noted from Fig. 5 a that the maximum cylinder pres-
sure increases with the injection pressure for both operating
points; a reasonable explanation, as above mentioned, is the pro-
moted atomization of diesel and the accelerated diffusion of natu-
ral gas, which leads to shortened combustion duration and the
subsequent raised maximum cylinder pressure. In addition, by
analyzing the maximum cylinder pressure at the same injection
pressure, it is found that the injection timing has bigger impact
on the maximum cylinder pressure at higher engine speed. At
operating point A with engine speed of 1275 rpm, the maximum
cylinder pressure has an average increase of 9.7 MPa as the injec-
tion pressure increases from 18 MPa to 24 MPa, however, the aver-
age increase is only 7.3 MPa when the injection pressure increased
from 24 MPa to 30 MPa; At operating point B with engine speed of
1550 rpm, an average increase of 16.8 MPa in the maximum cylin-
der pressure can be observed as the injection pressure increased
from 18 MPa to 24 MPa while the average increase is declined to
6.8 MPa as the injection pressure continues to increase to
30 MPa. The data in Fig. 5 a also indicate that when the injection
pressure is raised from 18 MPa to 24 MPa, a more signiﬁcant
increase in maximum cylinder pressure than that of from 24 MPa
to 30 MPa can be noticed, which can be explained by the weakened
impact of pressure ratio on the spreading speed and penetration
distance of gaseous jets at higher injection pressures.
It can be deduced from the effects of injection pressure on the
crank angle of maximum cylinder pressure shown in Fig. 5 b that
the maximum combustion pressure takes place earlier with
advancing injection timing, reducing engine speed and rising injec-
tion pressure. At operating point A with relatively lower engine
speed, when the injection pressure increased from 18 MPa to
24 MPa, the inﬂuence of injection pressure on the crank angle of
maximum cylinder pressure is similar to that of 24 MPa to
30 MPa; at operating point B with relatively higher engine speed,
the crank angle of maximum cylinder pressure is more sensitive
to injection pressure at the range of from 18 MPa to 24 MPa; the
explanation for this is similar to that of the changing trend for
the maximum cylinder pressure.
3.2. Heat release rate
As can be seen from Fig. 6 , the pulse width of pilot diesel and
the diesel to natural gas separation are 3 /C176
CA along with a 8.7 /C176CA
injection pulse width of natural gas. During the ignition delay,
the heat release rate shows a downward trend and appears to be
negative owing to the heat absorbed by physical and chemical
reactions. The combustion process initiates in the injection process
of natural gas (about 6 /C176CA after the pilot diesel injection), leading
to an increase in heat release rate; then the heat release rate begins
to decline a certain time after the ignition of pilot diesel because of
the depletion of pilot diesel; further, natural gas is ignited 6 /C176CA
after its start of injection, resulting in a sharp increase of heat
release rate, after which the natural gas continues to inject; thus,
the slope of heat release rate changes slightly from the start of
048 1 2 1 6 2 0
70
80
90
100
110
120
130
140
150
Pmax (bar)
NSOI (°CA)
A_18
A_24
A_30
B_18
B_24
B_30
(a)
048 1 2 1 6 2 0
0
4
8
12
16
20
24
CA_Pmax (°ATDC)
NSOI (°CA)
A_18
A_24
A_30
B_18
B_24
B_30
(b)
Fig. 5. Cylinder pressure parameters (a) maximum combustion pressure and (b)
corresponding crank angle (A_18:N = 1275 rpm, DRP = 18 MPa; A_24:N = 1275 rpm,
DRP = 24 MPa; A_30:N = 1275 rpm, DRP = 30 MPa; B_18:N = 1550 rpm, DRP =
18 MPa; B_24:N = 1550 rpm, DRP = 24 MPa; B_30:N = 1550 rpm, DRP = 30 MPa).
Q. Zhang et al. / Applied Energy 157 (2015) 217–228 221

<!-- PDF_PAGE: 6 -->

natural gas combustion to the end of natural gas injection and
shows a ﬁrst increase and then decrease trend following the end
of natural gas injection; however, after reaching at the maximum
value, the heat release rate exhibits a rapid reduction, after which,
the declining heat release rate gradually comes to a standstill until
the end of combustion.
Fig. 7 shows the heat release rate at both operating points. It can
be clearly noticed from Fig. 7 that with the advancement of injec-
tion timing, the peak heat release value resulting from the heat
release of pilot diesel combustion increases signiﬁcantly. This can
be attributed to the longer ignition delay of pilot fuel and subse-
quent larger proportion of diesel burnt in premixed combustion
event, which are caused by the relative low cylinder pressure
and temperature at the instant of injection. By comparison of the
heat release curves among different injection pressures, it can be
concluded that the heat release rate narrows and the peak value
of diesel combustion increases with the increase of injection pres-
sure. For example, at operating point B ( Fig. 8 ), the peak values
during diesel combustion at injection timing of 17 /C176BTDC are 3.2 J
/C176CA
/C0 1, 13.0 J /C176CA/C0 1, 20.80 J /C176CA/C0 1 at injection pressures of 18 MPa,
24 MPa and 30 MPa respectively. This is attributed to the enhanced
atomization, evaporation and mixing quality caused by higher
pressure ratio, thus leading to higher combustion rate and larger
heat release peak value during the main fuel combustion process.
Similar trend is presented in the work of McTaggart-Cowan et al.
[26].
As the maximum heat release rate shown in Fig. 9 a, the maxi-
mum heat release rate shows a trend of ﬁrst decrease then increase
with the advancing of injection timing. This is because the maxi-
mum heat release rate, which is associated with fuel injection
quantity and regularity of heat release, occurs earlier with the
advance of injection timing and the consequently advanced heat
release ( Fig. 9 b). Discrepancies can be found in the results of
another work by McTaggart-Cowan et al. [28], where both peak
values of heat release raise as injection timing advances. The differ-
ences in EGR rates and injection separation may be responsible for
this phenomenon. As the fuel mass ﬂow (diesel equivalent) illus-
trated in Fig. 10 , operating point B is taken as an example to help
explain the changing trend of the maximum heat release rate. It
can be seen that the total fuel mass ﬂow (TFMF: diesel equivalent)
shows a decreasing trend, which is gradually slowing down with
the advancing injection timing and similar to that of the maximum
heat release rate. Hence, when the injection advance angle is rela-
tively small (3 /C176BTDC to 11 /C176BTDC), the injection quantity is an
important factor for the decrease of maximum heat release rate;
as the injection timing continues to advance from 11 /C176BTDC, the
total fuel mass keeps declining, however, the maximum heat
release shows a converse trend of increase. This can be explained
by the ignition delay of pilot diesel, which plays an important role
in this stage; when the injection advance angle exceeds 11 /C176BTDC,
injection quantity witnesses minor changes while the ignition
delay of pilot diesel increases considerably with the advancing of
injection timing, leading to larger premixed combustion phase of
pilot diesel and enhanced intensity of ignition ﬂame; meanwhile,
the proportion for premixed combustion phase of natural gas is
also increased, resulting in higher initial burning rate of natural
gas and maximum heat release rate.
As also plotted in Fig. 9 , the maximum heat release rate for a
ﬁxed operating point occurs earlier and reaches a higher value
-30 -15 0 15 30 45 60
0
60
120
180
240
300
NSOI=19°BTDC
DPR=24MPa
GPWDPW
 H.R.R
 C.H.R
Crank angle (°CA)
Heat realse rate (J·°CA
-1
)
EOI
0
20
40
60
80
100
 C.H.R (%)
 Injection pulse
Fig. 6. A typical heat release rate.
-30 -15 0 15 30 45 60
0
100
200
300
0
100
200
300
0
100
200
300
Crank angle (°CA)
NSOI1
NSOI4
NSOI7
NSOI10
NSOI13
Heat release rate (J·°CA
-1
)
NSOI1
NSOI4
NSOI7
NSOI10
NSOI13
NSOI16
NSOI19
DRP=30MPa
DRP=24MPa
DRP=18MPa
NSOI1
NSOI4
NSOI7
NSOI10
NSOI13
NSOI16
NSOI19
(a)
-30 -15 0 15 30 45 60
0
100
200
300
0
100
200
300
0
100
200
300
Crank angle (°CA)
NSOI2
NSOI5
NSOI8
NSOI11
NSOI14
NSOI17
Heat release rate (J·°CA
-1
)
NSOI2
NSOI5
NSOI8
NSOI11
NSOI14
NSOI17
NSOI2
NSOI5
NSOI8
NSOI11
NSOI14
NSOI17
DRP=18MPa
DRP=24MPa
DRP=30MPa
(b)
Fig. 7. Heat release rate (a) A:N = 1275 rpm and (b) B:N = 1550 rpm.
222 Q. Zhang et al. / Applied Energy 157 (2015) 217–228

<!-- PDF_PAGE: 7 -->

when injection pressure is increased from 18 MPa to 30 MPa. At
operating point A, the maximum heat release rate has an average
increment of 64.4 J /C176CA/C0 1 with corresponding average phase angle
advanced by 2.6 /C176CA as injection pressure raises from 18 MPa to
24 MPa; however, when injection pressure continues to increase
to 30 MPa, average increment and advancement of maximum heat
release rate are reduced to 39.3 J /C176CA/C0 1 and 1.9 /C176CA. At operating
point B, the maximum heat release rate averagely increases by
66.6 J /C176CA/C0 1 along with a 3.5 /C176CA advancement in corresponding
phase angle as injection pressure increased from 18 MPa to
24 MPa, while increase by 37.4 J /C176CA with a 1.3 /C176CA advancement
in corresponding phase angle when injection pressure increased
to 30 MPa. One reason for this is the better atomization quality
resulting from higher injection pressure, another reason is the
increased injection quantity of pilot diesel (as the DFMF presented
in Fig. 10 ), both of which contribute to an increase in the ignition
energy of pilot diesel, and thus improving the ignition capability
for natural gas, causing faster heat release, advanced combustion
process as well as higher maximum heat release rate and advanced
phase angle. Though the energy fraction of pilot fuel is clearly
increased as injection pressure raises ( Fig. 11 ), which indicates
decreases in natural gas quantity, the improvement of the mixture
formation process is more crucial for the achievement of higher
maximum heat release rate at higher injection pressures.
By comparison of the values at the same injection pressure and
injection timing, it can be analyzed that the maximum heat release
rate drops sharply when the operating point changing from A to B,
besides, the occurrence of maximum heat release is retarded.
Because the combustion duration (in crank angle) is prolonged.
The main reason for this trend is arising from the decreasing heat
release during each crank angle and the increasing combustion
duration (in crank angle) with the increasing engine speed.
3.3. Combustion parameters
Fig. 12a and b represent the ﬂame development duration, which
is deﬁned as the interval between the injection of pilot diesel and
-30 -15 0 15 30 45 60
0
100
200
300
400
500
600
700
0
20
40
60
80
100
120
140
Crank angle (°CA)
Heat release rate (J·°CA
-1
)
Cylinder pressure (bar)
Injection pluse
H.R.RCylinder pressure
 18
 24
 30
 18
 24
 30
Operating point B
NSOI=17°BTDC
 18
 24
 30
Fig. 8. Cylinder pressure and heat release rate at different injection pressures.
048 1 2 1 6 2 0
150
200
250
300
350
400
H.R.Rmax (J·°CA
-1
)
NSOI (°CA)
A_18
A_24
A_30
B_18
B_24
B_30
(a)
048 1 2 1 6 2 0
-5
0
5
10
15
20
CA_H.R.Rmax (°ATDC)
NSOI (°CA)
A_18
A_24
A_30
B_18
B_24
B_30
(b)
Fig. 9. Heat release parameters (a) maximum heat release rate and (b) correspond-
ing crank angle.
2 4 6 8 10 12 14 16 18
0
15
105
120
135
Operating point B
Fuel mass flow (mg/cycle)
NSOI (°CA)
18_DFMF
24_DFMF
30_DFMF
 18_TFMF
 24_TFMF
 30_TFMF
Fig. 10. Total fuel mass ﬂow (TFMF) and pilot diesel mass ﬂow (DFMF) at operating
point B.
048 1 2 1 6 2 0
2
4
6
8
10
B_18
B_24
B_30
Pilot energy fraction (%)
NSOI (°CA)
A_18
A_24
A_30
Fig. 11. Energy fraction of pilot diesel.
Q. Zhang et al. / Applied Energy 157 (2015) 217–228 223

<!-- PDF_PAGE: 8 -->

10% total fuel burned, for both operating points in crank angle and
millisecond respectively. It can be seen that the ﬂame development
duration shows a decreasing trend as the injection timing
advances, furthermore, the effects of injection timing is diminish-
ing during this process. Generally, the ﬂame development duration
is dominated by the combined effects of pilot ignition delay, the
fuel–air mixing quality during the ignition delay and the strength
of pilot ﬂame. When the pilot diesel is injected near the top dead
center, the in-cylinder temperature and pressure are relatively
high, consequently, the ignition delay of diesel is relatively short,
hence less combustible mixture is formed before pilot ignition,
leading to less intensiﬁed pilot ﬂame and corresponding lower
initial ﬂame propagation rate and longer ﬂame development dura-
tion. With the injection timing advancing, the ignition delay of
pilot diesel prolongs, resulting in more diesel burnt in the pre-
mixed combustion phase, thereby natural gas is ignited by more
intensiﬁed ignition source, as a result, the ﬂame propagation rate
after ignition is faster. Therefore, the ﬂame development duration
are shortened, albeit the ignition delay of pilot diesel is extended.
As displayed in Fig. 12a and b, at the same injection timing, the
ﬂame development duration for both operating points presents the
consistent downward trend with injection pressure. At operating
point A, increasing injection pressure from 18 MPa to 24 MPa
shortens the average ﬂame development duration by an average
048 1 2 1 6 2 0
16
18
20
22
24
26
28
MBF0-10% (°CA)
NSOI (°CA)
A_18
A_24
A_30
B_18
B_24
B_30
(a)
048 1 2 1 6 2 0
2.0
2.2
2.4
2.6
2.8
3.0
MBF0-10% (ms)
NSOI (°CA)
A_18
A_24
A_30
B_18
B_24
B_30
(b)
048 1 2 1 6 2 0
-5
0
5
10
15
20
25
MBF50% (°ATDC)
NSOI (°CA)
A_18
A_24
A_30
B_18
B_24
B_30
(c)
048 1 2 1 6 2 0
28
30
32
34
36
38
40
MBF10-90% (°CA)
NSOI (°CA)
A_18
A_24
A_30
B_18
B_24
B_30
(d)
4
6
8
10
18_θ1/θ2
24_θ1/θ2
30_θ1/θ2
18_θ1
24_θ1
30_θ1
A
18_θ1
24_θ1
30_θ1
12
16
20
24
28
048 1 2 1 6 2 0
4
6
8
10
NSOI (°CA)
B
18_θ1/θ2
24_θ1/θ2
30_θ1/θ2
MBF10-50% (°CA)
12
16
20
24
28
 MBF10-50%/MBF10-90% (%)
(e)
Fig. 12. Combustion parameters (a) 0–10% ﬂame development duration in crank angle, (b) 0–10% ﬂame development duration in millisecond, (c) 50% combustion ph ase
angle, (d)10–90% rapid combustion duration and (e) 10–50% fuel burnt and corresponding percentage of the rapid combustion duration ( h1:MBF10–50%; h1/h2: MBF10–50%/
MBF10–90%).
224 Q. Zhang et al. / Applied Energy 157 (2015) 217–228

<!-- PDF_PAGE: 9 -->

value of 2.3 /C176CA, however, when injection pressure increases from
24 MPa to 30 MPa, the ﬂame development duration is shortened
by 1.7 /C176CA averagely. At operation point B, these two values are
3.4/C176CA and 1.3 /C176CA respectively. Since the width of pilot diesel
injection is ﬁxed during the experimental process, the injection
quantity of pilot diesel increases with the rising injection pressure;
moreover, better atomization, evaporation and more complete
mixing can be achieved, both contribute to increased energy of
ignition source, shorter ignition delay as well as faster initial com-
bustion rate of natural gas, namely shorter ﬂame development
duration. It can also be deduced that the ﬂame development dura-
tion exhibits a higher value at higher engine speed owing to the in-
cylinder temperature and ﬂuid movement. Yet, when compared to
that of injection pressure, the effects of operating points on the
ﬂame development duration in millisecond are small.
As illustrated in Fig. 12c, the 50% phase angle advances with the
advance of injection timing due to the early start of injection, the
injection pressure, however, has more profound effects on the
50% phase angle when raised from 18 MPa to 24 MPa, which is
consistent with that of the ﬂame development duration, implying
that increasing pressure exerts beneﬁcial effects on the ﬂame prop-
agation in initial stages. Fig. 12 c also demonstrates that the 50%
phase angle is retarded at higher engine speed since the combus-
tion duration (in crank angle) is signiﬁcantly extended at higher
engine speed.
Fig. 12 d displays the rapid combustion duration for both oper-
ating points. It can be seen that the rapid combustion duration ﬁrst
extends and then decreases with the advancement of injection
timing at operating point A, while a monotonically increasing trend
is displayed at operating point B. At operating point A, there is little
difference presented by the rapid combustion duration at the injec-
tion pressures of 18 MPa and 24 MPa, however, at the injection
pressure of 30 MPa, the rapid combustion duration is evidently
longer. At operating point B, the rapid combustion duration is
the longest at the injection pressure of 24 MPa. Different from
spark-ignition natural gas engine, the rapid combustion duration
of pilot ignited direct injection natural gas engine is not only
affected by the ﬂame propagation rate, but also the diffusion rate
of natural gas in the late combustion stages, which is highly inﬂu-
enced by injection pressure, injection timing as well as in-cylinder
ﬂuid movement. This provides an explanation for the inconsistent
variations of rapid combustion duration.
Fig. 12 e indicates that the 10–50% fuel burnt duration, which
accounts for a smaller percentage of the rapid combustion dura-
tion, basically shows a trend of ﬁrst increase and then decrease
with advancing injection timing and a decrease trend with rising
injection pressure. The results suggest that the ﬂame propagation
speed in the initial stages of rapid combustion duration is likely
to be beneﬁted from the rising injection pressure at both operating
points, but the situation for the late stages varies with operating
points. This is mainly due to the ﬂuid motion, which is associated
with engine speed and the pulse width of natural gas injection;
when the engine speed is relatively low, the in-cylinder ﬂuid
motion is correspondingly weaker, thus longer penetration of nat-
ural gas jet can be achieved with higher injection pressure of
30 MPa, enables longer jet penetration and consequent more natu-
ral gas injected near the cylinder wall. As known, the low temper-
ature and weak ﬂow movement of near-wall area have negative
impacts on the formation of ﬂammable mixture and the rate of
ﬂame propagation, thereby, reducing combustion rate in later
stages; though the pulse width of natural gas injection is relatively
short, the effects of penetration distance can not be offset. when
the engine speed is relatively high, the in-cylinder ﬂuid motion is
strengthened, generating enhanced swirling ﬂow, which deters
the penetration of natural gas jet, meanwhile, stronger ﬂuid
motion promotes the diffusion of natural gas and the ﬂame
propagation, which can mitigate the impact of the longer penetra-
tion distance caused by higher injection pressure, resulting in
uncertain trend of rapid combustion duration with injection
pressure.
3.4. Emissions and fuel economy
Fig. 13 a displays the effects of injection parameters on THC
emissions at both operating points. It can be found that at the oper-
ating points B, THC emissions drop with the advancement of injec-
tion timing, which is possibly due to the decreasing tendency of
048 1 2 1 6 2 0
0.6
0.8
1.0
1.2
1.4
1.6
1.8
THC (g/kW·h)
NSOI (°CA)
18_A
24_A
30_A
18_B
24_B
30_B
(a)
048 1 2 1 6 2 0
2
4
6
8
10
12
14
CO (g/kW·h)
NSOI (°CA)
18_A
24_A
30_A
18_B
24_B
30_B
(b)
048 1 2 1 6 2 0
2
4
6
8
10
12
NOx (g/kW·h)
NSOI (°CA)
18_A
24_A
30_A
18_B
24_B
30_B
(c)
Fig. 13. Emission characteristics (a) THC emissions, (b) CO emissions and (c) NOx
emissions.
Q. Zhang et al. / Applied Energy 157 (2015) 217–228 225

<!-- PDF_PAGE: 10 -->

retarded combustion caused by the longer combustion duration (in
crank angle) at relatively higher engine speed, further increasing
the injection advance angle, THC emissions change gently as a
result of the diminished inﬂuence of retarded combustion. This
can be conﬁrmed by the results of Dumitrescu et al. [24]. At the
operating point A, the engine speed is relatively low, providing
enough time for HC oxidation, so THC emissions seem to be insen-
sitive to injection timing. In addition, THC emissions are improved
with lower engine speed considering lower possibility of local
extinction events and longer reaction time. Moreover, at low
engine speed, THC emissions suffer more from high pressure as a
result of increased fuel injected into crevice and near-wall regions
caused by longer penetration. However, at high engine speed,
inconsistent trend is revealed, poor mixing quality incurred by
excessively low injection pressure may lead to deteriorated THC
emissions, which, however, is disagree with that displayed in the
study of McTaggart-Cowan et al. [28] on a single cylinder engine
with EGR.
Fig. 13 b reveals the effects of injection parameters and operat-
ing conditions on CO emissions. It can be clearly noticed that CO
emissions have a maximum value over the whole range of injection
timing, suggesting that more complete combustion can be
obtained by either advancing or retarding from the certain injec-
tion timing. As widely accepted, CO emissions are strongly inﬂu-
enced by both oxygen concentration and combustion
temperature. In the present work, as the experiments were per-
formed under medium load, the electrically wastegate was kept
closed at both operating points, therefore, the boost pressure is
mainly determined by exhaust energy. At relatively retarded injec-
tion timings, the combustion process proceeds later into the
expansion stroke, resulting in increased exhaust energy, higher
boost pressure and excess air ratio ( Fig. 14 ), which promotes the
oxidation of CO. At relatively advanced injection timings, the pos-
itive effect of increased combustion temperature offsets the nega-
tive effect of decrease excess air ratio on CO oxidation, a
considerable decrease in CO emissions can be observed. This trend
is inconsistent with that found by Zeng et al. [32] as a result of the
different experimental method used, in their study, the fuel injec-
tion quantity rather than BMEP is kept at a constant value. The
variation with injection pressure, however, exhibits inconsistent
trends at different operating points as a result of the competing
effects of the improved mixing and intensiﬁed turbulent shear
stresses induced by higher injection pressure. Contrary to the
response of THC emissions, CO emissions are signiﬁcantly reduced
when varying from operating point A to B. When engine speed
increases, the combustion process is retarded accordingly, causing
a signiﬁcant increase in exhaust temperature and exhaust energy.
Consequently, boost pressure and excess air ratio are raised, lead-
ing to enhanced CO oxidation. Also, the turbulence movement is
also strengthen at higher speeds, which also contributions to the
completion of combustion and reduction of CO emissions.
Fig. 13c shows the effects of injection parameters and operating
conditions on NOx emissions. Both advanced injection timing and
higher injection pressure result in earlier combustion and corre-
sponding higher in-cylinder temperature, thus increasing the
NOx emissions. NOx emissions are also shown to be obviously
0 4 8 12 16 20
1.6
1.7
1.8
1.9
2.0
2.1
2.2
Boost pressure (bar)
NSOI (°CA)
18_A
24_A
30_A
18_B
24_B
30_B
(a)
048 1 2 1 6 2 0
1.8
1.9
2.0
2.1
2.2
2.3
2.4
2.5
Excessive air ratio
NSOI (°CA)
18_A
24_A
30_A
18_B
24_B
30_B
(b)
Fig. 14. Boost pressure (a) and excess air ratio (b).
048 1 2 1 6 2 0
205
210
215
220
225
230
BSFC (g/kW·h)
NSOI (°CA)
18_A
24_A
30_A
18_B
24_B
30_B
(b)
048 1 2 1 6 2 0
37
38
39
40
41
42
Thermal Efficiency (%)
NSOI (°CA)
18_A
24_A
30_A
18_B
24_B
30_B
(a)
Fig. 15. Brake speciﬁc fuel consumption.
226 Q. Zhang et al. / Applied Energy 157 (2015) 217–228

<!-- PDF_PAGE: 11 -->

inﬂuenced by operating points, at operating points with higher
speed, the combustion duration is shortened and hence, leading
to lower NOx emissions.
Fig. 15 provides the thermal efﬁciency and BSFC at both operat-
ing points. It can be seen from Fig. 15 a that thermal efﬁciency
shows a trend of ﬁrst increase then decrease with advancing injec-
tion timing at operating point A with injection pressures of 18 MPa
and 24 MPa, however, at other conditions, an increasing trend can
be observed. The changing trends of BSFC, as illustrated in Fig. 15b,
are just opposite to that of thermal efﬁciency. This is because,
when operating at relatively lower speed with higher mechanical
efﬁciency, the combustion is more complete, thus higher thermal
efﬁciency and better economic characteristics can be achieved.
Also, the increase of injection pressure, which contributes to
advanced 50% combustion phase angle and earlier combustion
events, leads to improved thermal efﬁciency and lower fuel
consumption.
4. Conclusions
This study aims at investigating the variations of combustion,
emission as well as economic characteristics with injection param-
eters and operating conditions on a pilot ignited, direct injection
natural gas engine. The following conclusions can be drawn from
the present work:
1. The combustion process of pilot ignited direct can be cata-
logued into four main stages: the pure compression phase, the
mixture preparation phase, the pilot diesel combustion phase
and the main fuel combustion phase.
2. Increased value and earlier occurrence of maximum cylinder
pressure can be obtained by advancing the injection timing
and raising the injection pressure. When operating at the higher
engine speed of 1550 rpm, the maximum cylinder pressure
reaches lower value with delayed occurrence compared with
that of lower speed of 1275 rpm.
3. The maximum heat release rate increases and takes place ear-
lier with higher injection pressure and lower engine speed.
However, as the injection timing advances, a ﬁrst decrease then
increase trend of maximum heat release can be observed, also,
the corresponding time of occurrence is advanced.
4. The ﬂame development duration shows a generally decreasing
trend with advancing injection timing. Moreover, raising injec-
tion pressure and decreasing engine speed also reduce the
ﬂame development duration. The effects of operating condi-
tions on rapid combustion duration, however, seem to be
uncertain, exhibiting different tendencies at different injection
pressures.
5. When operating at higher engine speed of 1550 rpm, THC emis-
sions can be improved by advancing injection timing, while at
lower engine speed of 1275 rpm, reducing the injection pres-
sure would be more effective.
6. Combustion process and thermal efﬁciency can be improved by
appropriately advancing injection timing or raising injection
pressure.
7. CO emissions show a ﬁrst increase and then decrease trend with
injection timing while get worse with lower engine speed, how-
ever, the changing trend with injection pressure is inconsistent
at different engine speed.
8. NOx emissions suffer from advanced injection timing, higher
injection pressure as well as lower engine speed, all of which,
on the contrary, have positive effects on fuel economy. Thus,
the selection of injection strategy should base on the compro-
mise between NOx emissions and fuel economy.
Acknowledgements
The authors acknowledge ﬁnancial support from the Ministry of
Industry and Information Technology of the People’s Republic of
China (2060303) and assistance from Weichai&Westport new
energy Inc. in conducting the experiments.
References
[1] Selim MYE. Effect of exhaust gas recirculation on some combustion
characteristics of dual fuel engine. Energy Convers Manage 2003;44:707–21 .
[2] Abd Alla GH, Soliman HA, Badr OA, Abd Rabbo MF. Effect of injection timing on
the performance of a dual fuel engine. Energy Convers Manage 2002;43
(2):269–77
.
[3] Yang B, Xi CX, Wei X, Zeng K, Lai MC. Parametric investigation of natural gas
port injection and diesel pilot injection on the combustion and emissions of a
turbocharged common rail dual-fuel engine at low load. Appl Energy
2015;143:130–7
.
[4] Karim GA. A review of combustion processes in the dual fuel engine – the gas
diesel engine. Prog Energy Combust Sci 1980;6:277–85 .
[5] Peterson MB, Barter GE, West TH, Manley DK. A parametric study of light-duty
natural gas vehicle competitiveness in the United States through 2050. Appl
Energy 2014;125:206–17 .
[6] Faiz A, Weaver CS, Walsh MP. Air pollution from motor vehicles: standards and
technologies for controlling emissions. SAE 962102; 1996.
[7] Zhang F, Okamoto K, Morimoto S, Shoji F. Methods of increasing the BMEP
(power output) for natural gas spark ignition engines. SAE 981385; 1998.
[8] Chiu JP, Wegrzyn J, Murphy KE. Low emissions class 8 heavy-duty on-highway
natural gas and gasoline engine, SAE 2004-01-2982; 2004.
[9] McTaggart-Cowan GP, Rogak SN, Munshi SR, Hill PG, Bushe WK. The inﬂuence
of fuel composition on a heavy-duty, natural-gas direct-injection engine. Fuel
2010;89:752–9.
[10] McTaggart-Cowan GP, Reynolds CCO, Bushe WK. Natural gas fuelling for
heavy-duty on-road use: current trends and future direction. Int J Environ Stud
2006;63(4):421–40
.
[11] McTaggart-Cowan GP, Jones HL, Rogak SN, Bushe WK, Hill PG, Munshi SR. The
effects of high pressure injection on a compression ignition, direct injection of
natural gas engine. ASME J Eng Gas Turb Power 2007;129:579–88 .
[12] Jones HL, McTaggart-Cowan GP, Rogak SN, Bushe WK, Munshi SR, Buchholz
BA. Source apportionment of particulate matter from a direct injection
pilot ignited natural gas fuelled heavy duty DI engine. SAE 2005-01-2149;
2005.
[13] Douville B, Ouellette P, Touchette A, Ursu B. Performance and emissions of a
two-stroke engine fueled using high-pressure direct injection of natural gas.
SAE 981160; 1998.
[14]
Kalam MA, Masjuki HH. An experimental investigation of high performance
natural gas engine with direct injection. Energy 2011;36:3563–71
.
[15] Papagiannakis RG, Kotsiopoulos PN, Zannis TC, Yfantis EA, Hountalas DT,
Rakopoulos CD. Theoretical study of the effects of engine parameters on
performance and emissions of a pilot ignited natural gas diesel engine. Energy
2010;35:1129–38.
[16] Liu J, Yang FY, Wang HW, Ouyang MG, Hao SG. Effects of pilot fuel quantity on
the emissions characteristics of a CNG/diesel dual fuel engine with optimized
pilot injection timing. Appl Energy 2013;110:201–6
.
[17] Lounicia MS, Boussadib A, Loubara K, Tazerouta M. Experimental investigation
on NG dual fuel engine improvement by hydrogen enrichment. Int J Hydr
Energy 2014;39(36):21297–306 .
[18] Navarro E, Leo TJ, Corral R. CO 2 emissions from a spark ignition engine
operating on natural gas–hydrogen blends (HCNG). Appl Energy
2013;101:112–20.
[19] Abdelaal MM, Hegab AH. Combustion and emission characteristics of a natural
gas-fueled diesel engine with EGR. Energy Convers Manage 2012;64
(12):301–12.
[20] Papagiannakis RG, Rakopoulos CD, Hountalas DT, Rakopoulos DC. Emission
characteristics of high speed, dual fuel, compression ignition engine operating
in a wide range of natural gas/diesel fuel proportions. Fuel 2010;89:1397–406
.
[21] Ouellette P. High pressure injection of natural gas for diesel engine fueling. Ph.
D Thesis. The University of British Columbia; 1992.
[22] Chitsaz I, Saidi MH, Mozafari AA, Hajialimohammadi A. Experimental and
numerical investigation on the jet characteristics of spark ignition direct
injection gaseous injector. Appl Energy 2013;105:8–16
.
[23] Yu JZ, Vuorinen V, Hillamo H, Sarjovaara T, Kaario O, Larmi M. An experimental
study on high pressure pulsed jets for DI gas engine using planar laser-induced
ﬂuorescence. SAE 2012-01-1655; 2012.
[24] Dumitrescu S. Pilot ignited high pressure direct injection of natural gas fueling
of diesel engine. M.D Thesis. The University of British Columbia; 1999.
[25] Harrington J, Munshi S, Nedelcu C, Ouellette P, Thompson J, Whitﬁeld S. Direct
injection of natural gas in a heavy-duty diesel engine. SAE 2002-01-1630;
2002.
[26] McTaggart-Cowan GP, Jones HL, Rogak SN, Bushe WK, Hill PG, Munshi SR. The
effects of high-pressure injection on a compression-ignition, direct injection of
natural gas engine. In: Proceedings of ICEF2005 ASME Internal Combustion
Q. Zhang et al. / Applied Energy 157 (2015) 217–228 227

<!-- PDF_PAGE: 12 -->

Engine Division 2005 Fall Technical Conference. September 11–14, 2005,
Ottawa, Canada.
[27] McTaggart-Cowan GP, Bushe WK, Rogak SN, Hill PG, Munshi SR. PM and NOx
reduction by injection parameter alterations in a direct injected, pilot ignited,
heavy duty natural gas engine with EGR at various operating conditions. SAE
2005-01-1733; 2005.
[28] McTaggart-Cowan GP. Injection parameter effects on a direct injected, pilot
ignited, heavy duty natural gas engine with EGR. SAE 2003-01-3089; 2003.
[29] Rakopoulos DC, Rakopoulos CD, Giakoumis EG, Papagiannakis EG, Kyritsis DC.
Inﬂuence of properties of various common bio-fuels on the combustion and
emission characteristics of high-speed DI (direct injection) diesel engine:
vegetable oil, bio-diesel, ethanol, n-butanol, diethyl ether. Energy
2014;73:354–66.
[30] Heywood JB. Internal combustion engine fundamentals. New York
(USA): McGraw-Hill Publications; 1988 .
[31] Choi MG, Lee SH, Park SW. Numerical and experimental study of gaseous fuel
injection for CNG direct injection. Fuel 2015;140:693–700
.
[32] Zeng K, Huang ZH, Liu B, Liu LX, Jiang DM, Ren Y, et al. Combustion
characteristics of a direct-injection natural gas engine under various fuel
injection timings. Appl Therm Eng 2006;26(8–9):806–13 .
228 Q. Zhang et al. / Applied Energy 157 (2015) 217–228
