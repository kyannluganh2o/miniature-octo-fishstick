<!-- PDF_PAGE: 1 -->

The characteristic analysis of high-pressure gas jets for natural gas
engine based on shock wave structure
Quan Dong, Yue Li, Enzhe Song ⇑, Chong Yao, Liyun Fan, Jun Sun
Institute of Power and Energy Engineering, Harbin Engineering University, No. 145-1, Nantong Street, Nangang District, Harbin 150001, China
article info
Article history:
Received 21 March 2017
Received in revised form 23 May 2017
Accepted 6 June 2017
Available online 15 July 2017
Keywords:
Natural gas engine
Gas injection
Shock wave
Mach disk
Schlieren imaging
abstract
High gas injection pressure leads to the formation of under-expanded gas jet at nozzle exit. The shock
wave structure near the nozzle affects gas jet injection and mixing characteristics, which affects the com-
bustion and emission performance of the engine. Gas jet injection process and shock wave structure evo-
lution law under different nozzle pressure ratio (NPR) and oriﬁce diameter have been investigated with
the application of Schlieren imaging and numerical simulation. Results show that long injection duration
exists in gas injection process after the end of injection. It is attributed to the slow pressure reduction
velocity in the nozzle. This phenomenon is one of the key factors which inﬂuence the high HC emission
of gas fuel port injection natural gas engines. The change of pressure inside the nozzle also affects the
shock wave structure (Mach disk) near the nozzle. It is found that the increase of Mach disk width leads
to a large jet near-ﬁeld angle which promotes the spatial distribution and turbulent mixing of gas jet. In
addition to experimental results, numerical simulation is used to analyze the injection characteristics of
gas injection system. Increasing gas nozzle ﬂow area and shortening gas nozzle length are regarded as
effective ways to improve the responsiveness of gas injection system and reduce gas injection duration.
The range of Reynolds number at exit of the nozzle is 0.5–2.5 /C2 10
5 under various gas injection pressures
and oriﬁce diameters. This presents that gas jet is easily inﬂuenced by air turbulence in intake manifold.
Strong air turbulence in intake manifold is needed in a gas fuel port injection natural gas engine in order
to obtain homogeneous gas/air mixture.
/C2112017 Elsevier Ltd. All rights reserved.1. Introduction
Energy conservation and emission reduction have become the
most important issues in internal combustion engine (ICE) [1,2].
Natural gas is regarded as the best alternative fuel in ICEs due to
its abundant reserves, low price and good emission performance
[3,4]. Methane is the main component of natural gas, and it has
higher H/C ratio than other hydrocarbon fuels. Therefore, natural
gas engine can effectively reduce CO 2 emissions [5,6]. In addition,
the burning of natural gas produces less nitrogen oxide (NO x), sul-
fur oxide (SO x) and particulate matter (PM) in exhaust gases than
diesel fuel. Therefore, natural gas has been widely used in internal
combustion engines [7,8].
Direct injection (DI) and port injection (PI) of natural gas are
two typical application methods for natural gas engine [9,10]. Nat-
ural gas in-cylinder direct injection offers the accurate control of
gas fuel quality and high efﬁciency of air admission [11]. But it
has high requirement on gas injection system. In PI engine, the
gas fuel is injected into intake manifold, and the mixture of gas/
air enters the cylinder during intake stroke. At present, natural
gas port injection is widely used in China marine natural gas
engine, because of its low requirement on fuel injection system
compared with gas fuel direct injection in cylinder [12]. However,
natural gas port injection suffers from the unstable gas injection
quantity and high cycle-to cycle variations (CCV) [13,14]. More-
over, the mixture quality in the manifold determines the combus-
tion and emission characteristics of the engine [15]. Therefore, it is
necessary to study the transient injection characteristics of natural
gas port injection system in order to optimize engine combustion
performance.
A lot of studies have focused on the effect of gas injection strate-
gies on combustion and emission performance in natural gas
engine. Baratta studied the effect of end-of-injection timing on
mixture formation process. It is found that the injection timing
needs to advance in order to get good mixture preparation at high
speed or high load [16]. Mohamad investigated the combustion
http://dx.doi.org/10.1016/j.enconman.2017.06.015
0196-8904//C2112017 Elsevier Ltd. All rights reserved.
⇑ Corresponding author.
E-mail address: sez2005@sina.com (E. Song).
Energy Conversion and Management 149 (2017) 26–38
Contents lists available at ScienceDirect
Energy Conversion and Management
journal homepage: www.elsevi er.com/locate/enconman

<!-- PDF_PAGE: 2 -->

and performance of gas direct injection using spark plug fuel injec-
tor (SPFI). The results showed that running with SPFI increased vol-
umetric efﬁciency, engine output power and fuel conversion
efﬁciency [11]. Fan numerically investigated the inﬂuence of injec-
tion strategy on fuel distribution and combustion process in a port
injection natural gas engine. They concluded that the injection tim-
ing affects the fuel concentration ﬁelds signiﬁcantly, and the fuel
distribution has direct effect on combustion performance [14].I n
order to optimize the mixing effect of gas injection, several articles
analyzed the effect of nozzle structure on mixing characteristics.
Semin studied the mixing effect with different single-hole and
multi-hole nozzle in natural gas engine. Results showed that gas/
air mixing effect is related to gas jet ﬂow characteristics [17]. Erfan
investigated gaseous jet injection characteristics of a single-hole
nozzle and a multi-hole injector under different working condi-
tions. Results showed that gas fuel mass ﬂow rate is affected by
injection pressure linearly and new correlations for tip speed and
tip penetration are presented [18,19]. Recent studies showed that
gas jet ﬂow characteristics depend on the ratio of upstream total
pressure to the ambient pressure ( P
b) [20,21]. Upstream total pres-
sure is commonly used as gas injection pressure ( Po) and the ratio
is deﬁned as nozzle pressure ratio (NPR). At present, high pressure
is applied for natural gas injection in order to achieve high fuel
mass ﬂow rate in a natural gas engine. High injection pressure nor-
mally leads to the formation of under-expanded jets when gaseous
jet is injected through a nozzle [22].
A lot of researches have investigated the ﬂow characteristics of
under-expanded gas jet. Hamzehloo and Aleiferis investigated the
mixing characteristics of gas jets under different NPR. It was found
that high NPR leads to locally rich mixture in cylinder [23]. Moha-
mad studied high-pressure gas jet structure using a spark plug fuel
injector based on planar laser-induced ﬂuorescent (PLIF). The rela-
tionship between jet penetration, gas injection pressure and cylin-
der pressure were analyzed [24,25]. Vuorinen studied the gas jet
structure characteristics under the NPR from 4.5 to 10.5 using PLIF.
Results showed that the under-expanded level has a large inﬂu-
ence on mixture quality [26]. The under-expanded jet can be
divided into moderately under-expanded and highly under-
expanded according to NPR level. Gas jets are typically highly
under-expanded jet considering its high NPR (NPR /C21 4) [27].
Highly under-expanded gas jet leads to the formation of a strong
shock wave structure near the nozzle exit, called Mach disk.
Researchers have begun to study the effect of shock wave structure
on mixing characteristics. Donaldson and Snedeker ﬁrstly used
schlieren method and planar laser induced ﬂuorescence (PLIF) to
study the shock wave problem of under-expanded gas jet under
the condition of steady state. Results showed that the gas jet will
experience three typical jet ﬂow states and two transition states
as shown in Fig. 1 [27] . White analyzed the induced shock wave
structure of under-expanded gas injection by using Schlieren
method [28]. Yu and Vuorinen investigated the macro structure
of the shock wave and its effects on mixing turbulent based on PLIF
measurement and large eddy simulation (LES). It was found that
shock wave has important effects on jet behavior and fuel concen-
tration [29].
Previous experimental and computational works have focused
on shock wave structure information and gas jet mixing effect
under different NPR. But few studies concern about the effect of
shock wave structure on gas injection system, especially gas fuel
port injection system. Therefore, optimizing the injection charac-
teristics of gas fuel port injection system through the analysis of
shock wave structure is one of the main purposes of this article.
Gas nozzle is the key component of gas injection system. The ﬂow
conditions of the gas fuel in the nozzle directly affect the accuracy
and responsiveness of fuel injection. It is quite important to
combustion and emission performance of gas engines. At present,
little information is about the effect of shock wave structure on
ﬂow characteristics in the nozzle. Moreover, although three ﬂow
states of high-pressure gas jet have been presented, few article
studied the effect of these states on gas injection characteristic
parameters, such as the mass ﬂow rate at nozzle exit and the
injection duration.
Based on the analysis above, this paper focuses on a Yuchai 6 K
natural gas engine, aiming at investigating the effect of shock wave
structure on gas injection characteristics and optimizing the design
of gas injection system to solve the problem of high methane emis-
sions. The shock wave structure is obtained by the application of
Schlieren imaging and numerical simulation. The present paper
has three objectives: (1) Master the shock wave structure parame-
ters and analyze the ﬂow conditions of gas fuel in the nozzle. (2)
Analyze the effect of shock wave on jet macroscopic structure.
(3) Grasp high-pressure gas injection process under different con-
ditions and analyze the effect of gas injection pressure, oriﬁce
diameter and gas nozzle length on gas injection characteristics.
Nomenclature
ASOI after the start of injection
CCV cycle-to-cycle variations
ce local sound velocity at oriﬁce exit
D oriﬁce diameter
DI direct injection
fps frames per second
H Mach disk height
ICE internal combustion engine
LES large eddy simulation
M molar mass
Ma Mach number
NPR nozzle pressure ratio
P
o gas injection pressure
Pi oriﬁce inlet pressure
Pe oriﬁce exit pressure
Pb ambient pressure
PI port injection
PIV particle image velocimetry
PLIF planar laser-induced ﬂuorescent
R ideal gas constant
Re Reynolds number
r speciﬁc heat ratio
Ti oriﬁce inlet temperature
Te oriﬁce exit temperature
t time
Ve velocity at oriﬁce exit
W Mach disk width
Wmax maximum of Mach disk width
Greek symbols
hn jet near-ﬁeld angle
hf jet far-ﬁeld angle
a triple point angle
g conversion efﬁciency
l dynamic viscosity
qe density at oriﬁce exit
Q. Dong et al. / Energy Conversion and Management 149 (2017) 26–38 27

<!-- PDF_PAGE: 3 -->

2. Experimental setup
2.1. Schlieren system
The shock wave structure and gas injection process are investi-
gated by using Schlieren method. The schematic diagram of the
experimental setup is shown in Fig. 2 . The entire optical path is
layout as ‘Z’ shape. The lens group focuses the white light on the
main light axis, and the white light comes from a xenon lamp.
When the light passes through an aperture of 1 mm, it turns into
a point light source. The point light source is set in the focus of
the incident light spherical mirror. Through the reﬂect mirror
whose diameter is 100 mm, the light is reﬂected on the spherical
mirror and then forms a parallel light whose diameter is
190 mm. The high pressure gas injection makes the density gradi-
ent in measurement area changed during the experiment, changing
the refractive index of the incident light. The information of gas jet
ﬂow characteristics is transmitted to the high speed camera (Phan-
tom V7.3) through the symmetrical arrangement of spherical mir-
ror, reﬂect mirror and a knife edge at the focus.
2.2. Gas injection system and control system
The injection system is shown in Fig. 3 . The outlet diameter of
gas injection solenoid valve is 2 mm and the maximum needle lift
is 0.8 mm. The valve needs 1.64 ms to reach the maximum needle
lift, and the valve closing time is 0.8 ms. The gas goes through the
solenoid valve and enters into the gas nozzle. The oriﬁce diameter
(D) covers from 1.0 mm to 1.6 mm in this experiment. Gas injec-
tion control system sends the 24 V driving signal to the gas sole-
noid valve and synchronous control system sends a 5 V TTL
signal to high-speed camera simultaneously. The resolution of high
Mach disk
Nozzle
State State State 
Core 
area
Transition
area
Development
area Moderately
under-
expanded jetSubsonic jet
Highly
under-
expanded jet
Pe/Pb=1
1<Pi/Pb<1.85
1.1<Pe /Pb 2
1.95<Pi /Pb<3.85
P0
Pi
Pe
Pe /Pb>2
Pi /Pb>4.05
Velocity 
distribution
curves Shock 
unit
Pb
Transient 
State 
Transient 
State 
Shock wave
affected
area
Fig. 1. Schematic diagrams of the three ﬂow states of high-pressure gas jet [27].
Xenon 
lamp
Spherical mirror
Gas injection
control system
Gas injector
Aperture Reflect
mirror
Reflect
mirror
Spherical mirror
lens
Knife edge
Synchronous
control system
Monitor system
High speed
camera
CH4
Constant
Vo lum e v essel
Computer
Fig. 2. Schematic plan of experimental setup.
28 Q. Dong et al. / Energy Conversion and Management 149 (2017) 26–38

<!-- PDF_PAGE: 4 -->

speed camera is set as 256 /C2 512 pixels and the ﬂame frequency is
set to 20,000 frames per second (fps) in this experiment. The con-
trol signal pulse is 10 ms. This paper also deﬁnes four pressure con-
ditions. They are gas injection pressure ( P0), oriﬁce inlet pressure
(Pi), oriﬁce exit pressure ( Pe), and ambient pressure ( Pb).
The experiment uses methane gas with 99.999% purity. High
pressure gas comes from gas tanks and goes through the pressure
reducing valve to achieve the preset gas pressure. The gas injection
pressures are set as 0.6 MPa, 1.1 MPa and 1.6 MPa, respectively.
And the experiments are carried out under the conditions of atmo-
spheric pressure and the temperature is 298 K. The speciﬁcations
of the experimental parameters are shown in Table 1 .
2.3. Deﬁnition of shock wave structure parameters
The characteristic parameters of gas jet shock wave structure
are deﬁned in Fig. 4 including Mach disk height ( H), Mach disk
width ( W) and the triple point angle ( a). The variations of Mach
disk height is used to calculate the pressure information in gas
nozzle including oriﬁce inlet pressure and oriﬁce outlet pressure.
The pressure information in the nozzle is important to analyze
gas injection process. Mach disk height is deﬁned as the distance
from nozzle exit to the Mach disk. It is strongly affected by NPR.
Mach disk width is the dimension of Mach disk. Triple point angle
is deﬁned as the angle between the tangent of the expansion wave
and the axis [30].
The experiment repeats 10 times for each test conditions in
order to reduce the error and improve the accuracy of the results.
Shock wave structure is difﬁcult to obtain accurately due to the
small dimension. Therefore, an image processing program is
designed in MATLAB environment. The program enhances the orig-
inal image and obtains the characteristic parameters of the jet.
Eventually the characteristic parameters of gas jet and shock wave
structure can be extracted precisely and efﬁciently. The spatial res-
olution of visual images is 149
lm ⁄ 149 lm. The extraction error
of Mach disk height and Mach disk width is half of the height of
pixel height, which is 149 lm. The extraction error of triple point
angle and jet cone angle is ±1 /C176. The uncertainty of the measure-
ments of gas injection pressure is ±0.02 MPa.
3. Results and discussion
3.1. Evolution of gas injection process and shock wave structure based
on Schlieren imaging
Fig. 5 shows the Schlieren images of gas jets injection process
under different gas injection pressure and oriﬁce diameter. The
injection pulse width is 10 ms. It can be seen that shock wave
structure is clear to see near the nozzle exit. And obvious change
of ﬂow patterns exists in gas injection process. Gas jet state goes
from state I to state III after the start of injection ( ASOI) and then
it goes back from state III to state I at the end of injection. In addi-
tion, gas injection duration is obviously longer than control pulse
signal (10 ms). The total actual injection duration is longer than
80 ms when P
0 = 1.6 MPa, Pb = 0.1 MPa and D = 1.0 mm. Further
study investigated the injection process of multi-oriﬁce nozzle
through high-speed photography. The gas nozzle has 36 oriﬁces
with diameter of 1 mm ( P0 = 1.6 MPa, Pb = 0.1 MPa). It is found that
the actual injection duration is close to 25 ms under the same gas
injection pressure and control pulse signal.
The long injection duration makes a part of gas fuel hard to
entry the cylinder in intake stroke. This part of fuel is accumulated
in intake port and escapes to exhaust port during valve overlap
period in the next working cycle. This is harmful to the power
and emissions of the engine. Therefore, it is necessary to grasp
the gas injection law under different gas injection system. The
mass ﬂow rate at nozzle exit and total injection duration are also
important parameters to design gas injection system in natural
gas engines. Shock wave characteristic parameters changing rules
will be described and analyzed based on the experimental results
later.
Gas injection 
pressure (P0)
Injector adapter
Orifice inlet pressure (Pi)
Gas solenoid 
valve
24V 
Driving signal
Nozzle
Ambient pressure (Pb)
Orifice diameter (D)
Orifice length
Nozzle 
length
Orifice outlet pressure (Pe)
Fig. 3. Structure of high pressure gas injection system.
Table 1
Experimental parameters.
Item Parameter
Ambient temperature (K) 298
Oriﬁce diameter (mm) 1.0, 1.2, 1.4, 1.6, 1.8
Oriﬁce length (mm) 1
Nozzle length (mm) 82
Ambient pressure (MPa) 0.1
Gas injection pressure (MPa) 0.6, 1.1, 1.6
Injection duration (ms) 10
Jet gas species (–) Methane
Q. Dong et al. / Energy Conversion and Management 149 (2017) 26–38 29

<!-- PDF_PAGE: 5 -->

3.2. Analysis of pressure characteristic parameters based on shock
wave structure
3.2.1. Oriﬁce inlet pressure
The nozzle pressure ratio between the upstream and down-
stream of the oriﬁce determines gas jet ﬂow conditions. The gas
enters the choking state at nozzle outlet when nozzle pressure
ratio exceeds the critical pressure ratio. Gas jet has become
under-expanded jet, and the speed of the gas jet at nozzle outlet
is the speed of sound. The analysis of oriﬁce inlet pressure evolu-
tion law is the key parameter to grasp gas jet state. However, the
pressure information is hard to measure directly. The achievement
of Mach disk height has become a major entry point for obtaining
the key parameters of high pressure pulse gas injection. Previous
study shows that there is a relationship between Mach disk height
(H), oriﬁce diameter ( D) and the ratio between oriﬁce inlet
pressure (Pi) and ambient pressure ( Pb) [31], the formula is shown
in Eq. (1). The pressure mentioned in this paper is absolute
pressure.
H
D ¼ 0:67
ﬃﬃﬃﬃﬃ
Pi
Pb
s
ð1Þ
Fig. 6 shows the height of Mach disk during the injection process
under different gas injection pressure and oriﬁce diameter. The def-
inition of tASOI = 0 ms is the time that the gas jet can be seen at noz-
zle outlet. It can be seen that from Fig. 6(a) that the height of Mach
disk increases with the time before tASOI = 5 ms. Then the Mach disk
height maintains a stable value until tASOI = 10 ms which indicates
that the oriﬁce inlet pressure has become stable. The maximum
Mach disk height increases from 1.64 mm to 2.61 mm when gas
injection pressure increases from 0.6 MPa to 1.6 MPa. Mach disk
Expansion 
waves
Compression 
waves
Mach disk height (H) Mach disk width (W)Triple point
Triple point 
angle ( )
Nozzle body Jet boundary
Mach Disk
Ma<1 Ma=1 Ma>1 Ma<1
P1<Pb<P2
Ma>1 Ma<1
Ambient pressure (Pb)
Fig. 4. Deﬁnition of shock wave characteristic parameters of high-pressure gas jet.
tASOI = 0 m s 5 m s       1 0 m s      1 5 m s       2 0 m s       2 5 m s       3 0 m s
25
0
5
10
15
20
Length [mm](a)
25
0
5
10
15
20
Length [mm](b)
25
0
5
10
15
20
Length [mm](c)
25
0
5
10
15
20
Length [mm](d)
Fig. 5. Evolution of shock wave structure under different working conditions. (a) NPR =6 , Pb = 0.1 MPa, D = 1.0 mm, (b) NPR = 11, Pb = 0.1 MPa, D = 1.0 mm, (c) NPR =6 ,
Pb = 0.1 MPa, D = 1.2 mm, and (d) NPR =6 , Pb = 0.1 MPa, D = 1.6 mm.
30 Q. Dong et al. / Energy Conversion and Management 149 (2017) 26–38

<!-- PDF_PAGE: 6 -->

height decreases gradually after tASOI = 10 ms. It is noticed that the
Mach disk structure maintain time is more than 20 ms in any pres-
sure condition and the time increases with the increase of gas injec-
tion pressure. The existence of Mach disk proves that the gas
injection process continues after the end of injection. The long
injection duration makes a portion of gas fuel hard to entry the
cylinder when gas fuel is injected into intake manifold. This part
of gas fuel is accumulated in the intake port and part of these fuel
escapes to the exhaust port during valve overlap period in the next
working cycle. This leads to high HC emissions in exhaust gases. In
addition, the instability of gas fuel quantity is easy to cause a high
CCV of natural gas engine.
The height of Mach disk under various oriﬁce diameters is
shown in Fig. 6(b) when P0 = 0.6 MPa and Pb = 0.1 MPa. It can be
seen that the increase of oriﬁce diameter enhances Mach disk
height and increases the time to reach the maximum value under
the same gas injection pressure. The existing period of Mach disk
decreases from 25 ms to 16.15 ms when oriﬁce diameter increases
from 1.0 mm to 1.6 mm. This phenomenon presents that the
design of gas nozzle plays an important role in optimizing gas
injection system. The long injection duration is bad for engine con-
trol, especially at low speed or low load conditions. The design of
gas nozzle needs to improve this phenomenon and enhance the
responsiveness of gas injection system. Increasing the ﬂow area
of gas nozzle is a good way for shortening injection duration of nat-
ural gas engine.
Fig. 7 shows the ratio of P
i/Pb calculated from Mach disk height
based on Eq. (1) under various gas injection pressures and oriﬁce
diameters. In this section, a parameter of P0/Pb is used to compare
oriﬁce inlet pressure with gas injection pressure. The valued of
P0/Pb are the ﬁxed value of 16, 11 and 6 corresponding to the gas
injection pressure of 1.6 MPa, 1.1 MPa and 0.6 MPa respectively.
But it can be seen from Fig. 7(a) that Pi/Pb presents the change rule
that the value increases ﬁrstly, maintains a short time and
decreases gradually. It illustrates that the pressure establishment
and the decrease in the nozzle need some time. The raise time of
Pi increases with high gas injection pressure due to the high mass
ﬂow rate at nozzle exit. In addition, the gap between the maximum
value of Pi/Pb and P0/Pb increases with the increase of gas injection
pressure. This is supposed to be caused by the throttle effect in the
solenoid valve. Oriﬁce inlet pressure is changing during gas injec-
tion process, this paper deﬁnes an energy conversion efﬁciency
g1 to evaluate the average oriﬁce inlet pressure during the whole
injection process. g1 is calculated based on Eq. (2).
g1 ¼ average Pi=average P0 ð2Þ
It is calculated that g1 are 73.2%, 67.7% and 62.7% corresponding to
gas injection pressure 0.6 MPa, 1.1 MPa and 1.6 MPa, respectively.
This illustrates that the increase of gas injection pressure makes
conversion efﬁciency reduce gradually. Therefore, gas injection
pressure should not be too high in gas supply system considering
the energy efﬁciency. In addition, high gas injection pressure leads
to long gas injection duration which goes against to the engine
control.
Fig. 7(b) shows the pressure ratio of Pi/Pb under different oriﬁce
diameter when P0 = 0.6 MPa and Pb = 0.1 MPa. It can be seen that
the maximum value of Pi/Pb decreases with the increase of oriﬁce
diameter. Large oriﬁce diameter increases the pressure establish-
ment time considering large mass ﬂow rate at nozzle exit. How-
ever, it is found that large oriﬁce diameter effectively shortens
the injection duration after the end of injection.
0
0.5
1
1.5
2
2.5
3
0 5 10 15 20 25 30 35 40
Mach disk height [mm]
tASOI [ms]
NPR=6 ,Pb=0.1MPa
NPR=11,Pb=0.1MPa
NPR=16,Pb=0.1MPa
(a)
0
0.5
1
1.5
2
2.5
3
0 5 10 15 20 25 30
Mach disk height [mm]
tASOI [ms]
D=1.0mm D=1.2mm
D=1.4mm D=1.6mm
(b)
Fig. 6. Effects of gas injection pressure and oriﬁce diameter on Mach disk height. (a) Various NPRs, D = 1.0 mm and (b) various oriﬁce diameters, NPR =6 , Pb = 0.1 MPa.
0
2
4
6
8
10
12
14
16
0 5 10 15 20 25 30 35 40
Pi/Pb [-]
tASOI [ms]
NPR=6 ,Pb=0.1MPa
NPR=11,Pb=0.1MPa
NPR=16,Pb=0.1MPa
(a)
0
1
2
3
4
5
6
7
8
0 5 10 15 20 25 30
Pi/Pb [-]
tASOI [ms]
D=1.0mm D=1.2mm
D=1.4mm D=1.6mm
(b)
Fig. 7. Effects of gas injection pressure and oriﬁce diameter on Pi/Pb. (a) Various NPRs, D = 1.0 mm and (b) various oriﬁce diameters, NPR =6 , Pb = 0.1 MPa.
Q. Dong et al. / Energy Conversion and Management 149 (2017) 26–38 31

<!-- PDF_PAGE: 7 -->

Fig. 8 shows the changing rate of Pi with time during injection
process with different gas injection pressure and oriﬁce diameter.
The changing rate of Pi is deﬁned as the ratio of pressure difference
and the time period between two adjacent visual images. The ratio
of bigger than zero, equal to zero and less than zero corresponds to
pressure establishment, pressure balance and pressure reduction
process, respectively. It can be seen from Fig. 8(a) that the pressure
establishment duration is divided into two stages for P0 = 1.1 MPa
and P0 = 1.6 MPa. They are rapid establishment stage and slow
establishment stage, the inﬂection point is tASOI = 2.3 ms. The slope
of the pressure change rate for P0 = 0.6 MPa is obviously smaller
than P0 = 1.1 MPa and P0 = 1.6 MPa. This presents that high gas
injection pressure improves the responsiveness of gas injection
system. It can be seen that the pressure changing rate has no obvi-
ous balance state and the ratio corresponding to pressure reduc-
tion state is between /C0 0.2 and 0 with various gas injection
pressures. Low pressure reduction ratio is considered to be the
main reason for long injection duration after the end of injection.
It can be seen from Fig. 8(b) that the changing rate curves with var-
ious oriﬁce diameters are similar to those under various gas injec-
tion pressures. Large oriﬁce diameter corresponds to large pressure
reduction ratio which can effectively shorten total injection dura-
tion. In view of gas fuel port injection natural gas engine, how to
effectively shorten the slow injection duration after electromag-
netic valve shutting down is the key to decrease the residual gas
in intake manifold. It is also the prerequisite to guarantee the high
performance of the engine.
3.2.2. Oriﬁce exit pressure
The oriﬁce exit pressure ( P
e) represents the expansion energy of
the gas when the jet leaves the nozzle. Pe directly determines the
downstream ﬂuid state and the subsequent macro-structure char-
acteristics of the gas jet. The oriﬁce exit pressure Pe is calculated
based on Eq. (3) and the assume that the gas is isentropic adiabatic
ideal gas.
Pe
Pi
¼ 1 þ r /C0 1
2 Ma2
/C18/C19 /C0 r
r/C0 1
ð3Þ
where r is gas speciﬁc heat ratio and the value is 1.32 for methane.
Ma is the average Mach number at nozzle outlet section.
It is difﬁcult to accurately measure the gas jet velocity of at noz-
zle outlet due to the limited short injection duration, small scale of
temporal and spatial evolution process of gas jet, and low signal-
to-noise ratio of gas images. Therefore, Mach number at the exit
of the nozzle is obtained by three-dimensional simulation in this
paper.
A three-dimensional geometric model of gas injection system is
established in the ANSYS-Fluent V15.0 environment. The geometric
model and mesh model are shown in Fig. 9 . Independent veriﬁca-
tions of grid number and time step have been carried out in order
to ensure the calculation quality and reduce the computing time.
The grid numbers are 150,000, 370,000 and 700,000, respectively.
The grids are all hexahedron structure. It is found that the grid
number 370,000 is suitable which can shorten calculation time
and guarantee calculation accuracy. Meanwhile, the investigation
of time step independence shows that 0.2 ls is suitable value. Sole-
noid valve structure uses dynamic mesh structure, the open dura-
tion and the close duration for the valve are 1.64 ms and 0.8 ms
respectively. The maximum lift of solenoid valve is 0.8 mm. In this
paper, k-e model is used as the turbulence model and the relevant
settings are shown in Table 2. The boundary conditions are shown
in Table 3 .
Mach disk information provides signiﬁcant information of effec-
tive upstream pressure of the gas jet, and the simulation model can
be veriﬁed based on these information [22]. Fig. 10 shows compar-
isons of Pi/Pb between simulations and experiments. It can be seen
that the simulation results are consistent well with the experimen-
tal results, especially under the condition of P0 = 0.6 MPa. The max-
imum error is 2.7%. The short pressure establishment time is
considered the main reason and Pi reached a relative stable condi-
tion quickly. However, Pi showed strong transient with the
increase of gas injection pressure. The simulation results are 9.1%
and 21% higher than experiment results respectively when
NPR = 10 and NPR = 15 at tASOI = 4 ms. The difference between sim-
ulation and experiment becomes small with time development.
The errors are 0.2% and 1.2% at tASOI = 8 ms. It is shown that the
simulation can be used to investigate the injection process and
pressure change in gas injection system.
Table 4 is the result of the maximum Mach number and the
average Mach number at nozzle exit section calculated by simula-
tion. It is important to note that the Mach numbers under different
gas injection pressure are all more than 1. As mentioned above, the
gas ﬂow velocity at the nozzle exit will reach the speed of sound
for high pressure gas injection. Ma will be equal to 1 at nozzle out-
let section for ideal gas. But there is a boundary layer in the nozzle
for actual compressible viscous ﬂuid. The location of Ma = 1 occurs
within the nozzle. Gas jet velocity accelerates to supersonic at noz-
zle outlet section. It is noted that Mach number remains stable
throughout the life cycle of the Mach disk.
Fig. 11 shows the results of Pe/Pb with various gas injection
pressures. It can be seen that Pe/Pi equals to 0.3726 based on for-
mula Eq. (4) with different gas injection pressure. This paper pre-
sents a parameter of g2 to evaluate the transfer efﬁciency from
pressure energy to kinetic energy of gas jet which ignores the con-
sumption of kinetic energy in the nozzle. g2 is calculated as Eq. (4).
g2 ¼ð Pi /C0 PeÞ=Pi ð4Þ
-0.3
-0.2
-0.1
0
0.1
0.2
0.3
0.4
0.5
0.6
0 5 10 15 20 25 30 35 40
Change rate of Pi [Mpa/ms]
tASOI [ms]
NPR=6 ,Pb=0.1MPa
NPR=11,Pb=0.1MPa
NPR=16,Pb=0.1MPa
(a)
-0.2
0
0.2
0.4
0.6
02468 1 0
-0.2
-0.1
0
0.1
0.2
0.3
0 5 10 15 20 25 30
Change rate of Pi [Mpa/ms]
tASOI [ms]
D=1.0mm D=1.2mm
D=1.4mm D=1.6mm
(b)
0
0.04
0.08
0.12
0.16
12345
Fig. 8. The change rate of Pi under different gas injection pressure and oriﬁce diameter. (a) Various NPRs, D = 1.0 mm and (b) various oriﬁce diameters, NPR =6 , Pb = 0.1 MPa.
32 Q. Dong et al. / Energy Conversion and Management 149 (2017) 26–38

<!-- PDF_PAGE: 8 -->

It is calculated that g2 = 62.74% when P0 = 0.6 MPa and Pb = 0.1 MPa.
Therefore, g1 ⁄ g2 presents the total energy transfer efﬁciency from
gas source pressure energy to gas jet kinetic energy at nozzle exit.
Considering the transfer efﬁciency g1 = 73.2% from gas injection
pressure P0 to oriﬁce inlet pressure Pi, it can be seen that less than
45.93% of pressure energy turns into gas jet kinetic energy at nozzle
exit. In addition, g1 /C0 g1 ⁄ g2 presents the pressure energy for fur-
ther gas expansion process when gas jet leaves the nozzle. It is cal-
culated that 27.27% initial pressure energy needs to be transferred
into gas jet kinetic energy later. It is important to note that the for-
mation of Mach disk makes a part of pressure energy turned into
heat and turbulent kinetic energy. So the conversion efﬁciency from
gas source pressure energy to kinetic energy is low during the
whole injection process and the efﬁciency decreases further with
the increase of P0.
On the other hand, the kinetic energy of gas jet is small due to
the low gas density and gas jet velocity. The environment gas is dif-
ﬁcult to obtain more energy from gas jet, so large scale vortex is
hard to form. The gas entrainment and mixing effects become
weak. Abraham investigated the injection and mixing characteris-
tics of methane and diesel by simulation. It concluded that the jet
penetration of methane jet is larger than that of diesel jet (10% liq-
uid phase and 90% gas phase) with the same momentum and mass
ﬂow rate. The weak air entrainment and mixing ability is consid-
ered the main reason [32].
Fig. 12 shows the conversion efﬁciency with various oriﬁce
diameters. With the increase of oriﬁce diameter, the change of
transfer efﬁciency
g2 is small. It is because average Mach number
at nozzle outlet section is closed with different oriﬁce diameter.
The increase of oriﬁce diameter mainly affects the ratio of gas
injection pressure P0 to oriﬁce inlet pressure Pi. It can be seen that
the total energy transfer efﬁciency ( g1 ⁄ g2) from gas injection
pressure energy to gas jet kinetic energy at nozzle exit is less than
45% for different oriﬁce diameter. This presents that choking
phenomenon affects the gas jet kinetic energy signiﬁcantly. The
Valve
Nozzle
Orifice
(a) Geometry model
(b) Mesh model
Fig. 9. Geometric model and mesh model of gas injection system.
Table 2
Viscous model & solution setup.
Viscous model k- e
Density Compressible ideal gas
Solution methods SIMPLE
Spatial discretization Second Order Upwind
Table 3
Boundary conditions.
Name Parameter
Inlet pressure [MPa] 0.6/1.1/1.6
Outlet pressure [MPa] 0.1
Inlet temperature [K] 300
Outlet temperature [K] 300
0
2
4
6
8
10
12
14
16
18
3456789 1 0 1 1
Pi / Pb  [-]
tASOI [ms]
1.6MPa-exp 1.6MPa-num
1.1MPa-exp 1.1MPa-num
0.6MPa-exp 0.6MPa-num
Fig. 10. Comparison of Pi/Pb between experiment and simulation ( Pb = 0.1 MPa,
D = 1.0 mm).
Table 4
Mach numbers at nozzle exit corresponding to different gas injection pressures.
P0 = 0.6 MPa P0 = 1.1 MPa P0 = 1.6 MPa
Maximum Ma 1.4045 1.4092 1.4095
Average Ma 1.2914 1.3019 1.3022
0
1
2
3
4
5
6
0 5 10 15 20 25 30 35 40
Pe/Pb [-]
tASOI [ms]
NPR=6 ,Pb=0.1MPa
NPR=11,Pb=0.1MPa
NPR=16,Pb=0.1MPa
Fig. 11. Effects of gas injection pressure on Pe/Pb (D = 1.0 mm).
Q. Dong et al. / Energy Conversion and Management 149 (2017) 26–38 33

<!-- PDF_PAGE: 9 -->

limited velocity at nozzle exit is the main characteristic for gas jet
injection which is quite different from diesel jet.
3.3. Effect of shock wave structure on jet macroscopic structure
3.3.1. Jet cone angle
Mach disk width ( W) is one of the important parameters in gas
injection system design of natural gas engine. The increase of Mach
disk width presents stronger turbulence intensity in the jet, and it
also promotes turbulent mixing effect in the downstream area
[29]. In addition, the airﬂow temperature, pressure and density
increase, the gas velocity decreases when gas ﬂow goes through
Mach disk structure. The increase of temperature promotes the
low temperature oxidation of methane before combustion, while
the increase of density and the decrease of gas velocity affect the
gas mass ﬂow rate. Moreover, Mach disk width affects the macro-
scopic structure of the jet, such as the jet cone angle.
Fig. 13 shows the effects of gas injection pressure and oriﬁce
diameter on Mach disk width. Fig. 13(a) shows the evolution law
of Mach disk width with time development under different gas
injection pressure. It can be seen that the width of Mach disk
increases with the increasing gas injection pressure. But Mach disk
width does not exceed the oriﬁce diameter ( D = 1 mm) under the
three gas injection pressure. Speciﬁcally, the ratio of maximum
Mach disk area and oriﬁce area ( W
max/D)2 under the condition of
P0 = 0.6 MPa, 1.1 MPa and 1.6 MPa are 0.1119, 0.3354 and 0.8513,
respectively. It is considered that Mach disk has small effect on
gas jet when gas injection pressure is small. The impact strength
and area increase with the increase of gas injection pressure P0
and oriﬁce exit pressure Pe. The width of Mach disk under different
oriﬁce diameter has the same changing rules with Mach disk
height. Fig. 13(b) presents the ratio of Wmax/D with various oriﬁce
diameters. It can be seen that the ratio of Wmax/D is 0.38, 0.51, 0.54
and 0.55 respectively when D= 1 mm, 1.2 mm, 1.4 mm and
1.6 mm. The increasing Mach disk width proves stronger turbu-
lence intensity in the gas jet. In addition, larger Mach disk width
leads to the increase of the contact area between gas jet and sur-
rounding air. It is beneﬁcial to the mixing effect of gas injection
process.
As mentioned above, the Mach disk structure affects the macro-
scopic structure of gas jet. Gas jet near-ﬁeld cone angle ( hn)i s
deﬁned in this section to analyze the effect of Mach disk structure
on jet cone angle at early stage of gas injection. hn is deﬁned as the
jet angle from nozzle outlet to ﬁve oriﬁce length position. Fig. 14
shows the variations of near-ﬁeld cone angle with various gas
injection pressure and oriﬁce diameter. Fig. 14(a) shows the
near-ﬁeld cone angle with different gas injection pressure. The
changing rule of near-ﬁeld cone angle is consistent with Mach disk
width. This illustrates that the increase of Mach disk width has a
positive effect on the increase of near-ﬁeld cone angle of gas jet.
The reason is that the height of Mach disk is on the upstream of
measurement position of the near-ﬁeld cone angle. So the increase
of Mach disk width promotes the radial development of the gas jet.
In addition, the position of the Mach disk is closer to the near-ﬁeld
cone angle measurement location with the increase of gas injection
pressure. So the effect of increasing Mach disk width on the near-
ﬁeld cone angle is more obvious. Fig. 14(b) shows that the increase
of oriﬁce diameter increases the near-ﬁeld cone angle. The increase
of gas jet near-ﬁeld cone angle also promotes the increase of jet
far-ﬁeld angle. This makes the jet volume increase signiﬁcantly
[18,21]. The increasing volume of gas jet enhances the mixing
effect in the far-ﬁeld. Therefore, increasing oriﬁce diameter is ben-
eﬁcial to the design of gas injection system.
3.3.2. Triple point angle
Triple point angle is an important parameter to evaluate the
ﬂow conditions behind the Mach disk [30]. Fig. 15 shows the vari-
ations of triple point angle under various gas injection pressures
and oriﬁce diameters conditions. Fig. 15(a) presents the triple
point angle with different gas injection pressure. It is clear to see
that triple point angle has the same evolution law with changing
rate of oriﬁce inlet pressure P
i. As mentioned above, the changing
rate of Pi presents rapid pressure establishment process and slow
pressure establishment process at high gas injection pressure.
The time inﬂection point is also observed in Fig. 15(a). The increas-
ing gas injection pressure makes large Mach disk width. The
boundary layer is extruded with the increase of Mach disk width
0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
1 1.2 1.4 1.6
Conversion efficiency [-] 
Diameter [mm]
1 2
Fig. 12. Conversion efﬁciency with various oriﬁce diameters ( NPR =6 , Pb = 0.1 MPa).
0
0.2
0.4
0.6
0.8
1
1.2
0 1 02 03 04 0
Mach disk width [mm]
tASOI [ms]
NPR=6 ,Pb=0.1MPa
NPR=11,Pb=0.1MPa
NPR=16,Pb=0.1MPa
(a)
0
0.1
0.2
0.3
0.4
0.5
0.6
11 . 2 1 . 4 1 . 6
Wmax/D [-]
Diameter [mm]
(b)
Fig. 13. Effects of gas injection pressure and oriﬁce diameter on Mach disk width. (a) Various NPRs, D = 1.0 mm and (b) various oriﬁce diameters, NPR =6 , Pb = 0.1 MPa.
34 Q. Dong et al. / Energy Conversion and Management 149 (2017) 26–38

<!-- PDF_PAGE: 10 -->

which makes the triple point angle decreased. Fig. 15(b) shows the
variation of triple point angle with different oriﬁce diameter. The
changing rule is similar to Fig. 15(a). The triple point angle
decreases with the increase of oriﬁce diameter. It is thought that
the triple point angle is inversely proportional to the jet energy.
The gas disturbance in intake ports promotes gas jet radial devel-
opment process when jet energy is low, making a large triple point
angle.
Fig. 16 shows the curves of Mach disk width, jet near-ﬁeld
angle, jet far-ﬁeld angle (the maximum radial expand angle to
the jet front) and triple point angle when NPR =6 , P
b = 0.1 MPa
and D = 1 mm. It can be seen that jet near-ﬁeld angle, jet far-ﬁeld
angle and Mach disk width have the same changing rules. The
curves of triple point angle and Mach disk width are changed with
a contrary tendency. Jet near-ﬁeld cone angle is more sensitive to
variations of Mach disk width than jet far-ﬁeld angle. It is because
Mach disk is on the upstream of the measurement position of near-
ﬁeld cone angle. The increase of Mach disk width improves the
radial development of gas jet. This is beneﬁcial to downstream
mixing process. The curve of triple point angle presents that triple
point angle decreases with jet development and large triple point
angle corresponds to small jet cone angle. It can be seen that triple
point angle is directly affected by Mach disk width. Triple point
angle reﬂects the level of jet development. It reaches the minimum
value when jet has become stable under-expanded jet near
t
ASOI = 5 ms.
3.4. Injection characteristics of high-pressure gas jets
3.4.1. Mass ﬂow rate
Grasping the mass ﬂow rate of gas injection system is the foun-
dation of fuel quantity control and gas injection system optimiza-
tion. Fig. 17 shows the mass ﬂow rate at nozzle exit under different
gas injection pressure and oriﬁce diameter based on numerical
simulation. Fig. 17(a) presents the mass ﬂow rate under different
gas injection pressure when D = 1 mm. The curves can be divided
into three stages as time goes on: Stage 1 refers to the pressure
establishment in the nozzle. The mass ﬂow rate increases rapidly.
Stage 2 refers to stable gas injection process. The curves present a
slight ﬂuctuation from Stage 1 to Stage 2 due to the effect of
transient pressure change. Stage 3 refers to the pressure reduction
process. The residual gas fuel in the nozzle is injected into the
20
25
30
35
40
45
50
0 5 10 15 20 25 30
n
tASOI [ms]
NPR=6 ,Pb=0.1MPa
NPR=11,Pb=0.1MPa
NPR=16,Pb=0.1MPa
(a)
15
20
25
30
35
40
45
50
55
60
0 5 10 15 20 25
n
tASOI [ms]
D=1.0mm D=1.2mm
D=1.4mm D=1.6mm
(b)
Fig. 14. Effects of gas injection pressure and oriﬁce diameter on jet near-ﬁeld angle. (a) Various NPRs, D = 1.0 mm and (b) various oriﬁce diameters, NPR =6 , Pb = 0.1 MPa.
25
27
29
31
33
35
37
39
41
43
45
0 5 10 15 20 25 30
t
ASOI [ms]
NPR=6 ,Pb=0.1MPa
NPR=11,Pb=0.1MPa
NPR=16,Pb=0.1MPa
(a)
20
25
30
35
40
45
0 5 10 15 20 25
tASOI [ms]
D=1.0mm D=1.2mm
D=1.4mm D=1.6mm
(b)
Fig. 15. Effects of gas injection pressure and oriﬁce diameter on triple point angle. (a) Various NPRs, D = 1.0 mm and (b) various oriﬁce diameters, NPR =6 , Pb = 0.1 MPa.
0
0.5
1
1.5
2
0
5
10
15
20
25
30
35
40
45
0 5 10 15 20 25 30
Mach disk width [mm]
Jet cone angle and triple 
tASOI [ms]
Triple point angle
Jet near-field angle
Jet far-field angle
Mach disk width
Fig. 16. Variation of Mach disk width, jet near-ﬁeld angle, far-ﬁeld angle and triple
point ( NPR =6 , Pb = 0.1 MPa, D = 1 mm).
Q. Dong et al. / Energy Conversion and Management 149 (2017) 26–38 35

<!-- PDF_PAGE: 11 -->

intake port. It can be seen that the injection duration for Stage 3 are
7.5 ms, 12.5 ms, 15 ms respectively under NPR = 6, 11, 16. As men-
tioned before, large oriﬁce diameter can effectively decrease the
pressure reduction duration. Fig. 17(b) presents the mass ﬂow rate
with different oriﬁce diameter. It is clear to see that the total injec-
tion duration decrease from 17.5 ms to 13.5 ms when oriﬁce diam-
eter increases from 1 mm to 1.6 mm. In addition, large oriﬁce
diameter increases the maximum value of mass ﬂow rate. This
can shorten the gas injection pulse width, and it is beneﬁcial to
ﬂexible control of gas injection timing.
In addition to study the inﬂuence of gas injection pressure and
oriﬁce diameter on gas injection process, the nozzle volume
between the valve and the oriﬁce is also an important parameter
for gas injection system design. This paper investigates the effect
of gas nozzle length on gas injection process based on numerical
simulation. The length of the nozzle is 22 mm, 52 mm and
82 mm. Fig. 18 shows the mass ﬂow rate at nozzle exit with differ-
ent nozzle length when P0 = 1.6 MPa, Pb = 0.1 MPa and D = 1.0 mm.
It can be seen from the ﬁgure that short gas nozzle length corre-
sponds to short gas injection duration. The injection duration
reduces from 25 ms to 15.7 ms when gas nozzle length decrease
from 82 mm to 22 ms. This presents that gas nozzle should be
made as short as possible. But it is worth noting that gas nozzle
is always inserted from inlet manifold to intake manifold in natural
gas engine. Short gas nozzle means that gas nozzle exit is close to
the inlet of intake manifold. Gas injection is similar to gas inlet
single-point injection method. The quantity of gas fuel enters into
cylinder is unstable and the engine responsiveness is poor. There-
fore, gas nozzle length should be controlled in an appropriate scope
to guarantee gas injection responsiveness and reduce the injection
duration.
3.4.2. Reynolds number
Reynolds number ( Re) is an important parameter to analyze the
mixing speed and quality of methane gas. Assuming high pressure
gas is isentropic adiabatic ideal gas, the Reynolds number at nozzle
outlet can be calculated according to Eq. (5).
Re ¼ qe /C1 Ve /C1 D
l ð5Þ
where qe is the gas density at oriﬁce exit, D is oriﬁce diameter, l is
methane dynamic viscosity at the exit and the value is related to
outlet temperature. Ve is gas velocity at oriﬁce exit. The solution
of qe and Ve are based on the following formula:
Te
Ti
¼ 1 þ r /C0 1
2 Ma2
/C18/C19 /C0 1
ð6Þ
qe ¼ PeMCH4
RTe
ð7Þ
Ce ¼
ﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ
r R
MCH4
Te
s
ð8Þ
Ve ¼ ce /C1 Ma ð9Þ
where Ti and Te are inlet and outlet temperature of the nozzle, ce is
the local sound velocity, MCH4 is the molar mass of methane, R is the
ideal gas constant.
Fig. 19 is the changing rule of Reynolds number with time
development under different gas injection pressure and the com-
parison of maximum Reynolds number under different oriﬁce
diameter. It can be seen from Fig. 19(a) that Reynolds number at
nozzle outlet increases with the increase of the gas injection pres-
sure. The curves are consistent with the evolution law of oriﬁce
inlet pressure Pi which indicates that the Reynolds number at noz-
zle exit shows high dynamic performance in the whole gas injec-
tion process. High Reynolds number represents not only the high
under-expanded level but also the increased turbulence distur-
bance intensity. The Reynolds number for diesel spray is on the
order of magnitude 10 4. However, the Reynolds number for high
Fig. 17. Effects of gas injection pressure and oriﬁce diameter on mass ﬂow rate at nozzle exit. (a) Various NPR, D = 1.0 mm and (b) various oriﬁce diameter, NPR =6 ,
Pb = 0.1 MPa.
Fig. 18. Effects of gas nozzle length on mass ﬂow rate at nozzle exit ( NPR = 16,
Pb = 0.1 MPa, D = 1.0 mm).
36 Q. Dong et al. / Energy Conversion and Management 149 (2017) 26–38

<!-- PDF_PAGE: 12 -->

pressure gas at nozzle outlet is on the order of magnitude10 5. Gas-
eous fuel has a higher binary diffusion coefﬁcient than diesel fuel
which means that gas fuel has stronger diffusion ability. However,
the small density difference between gas jet and the surrounding
air makes the diffusion velocity slow. The entrainment capacity
of gas jet is weak. It is difﬁcult to achieve good fuel/air homoge-
neous mixture during intake stroke. The high Reynolds number
of gas jet also presents that gas jet is more easily affected by sur-
rounding air movement. Therefore, it is necessary to increase the
gas turbulence in intake port to promote mixing process. This is
beneﬁcial to avoiding local too thick mixture concentration in
cylinder. Fig. 19(b) shows the maximum Reynolds number with
various oriﬁce diameter when P0 = 0.6 MPa and Pb = 0.1 MPa. The
maximum Reynolds number increases from 1.07 ⁄ 105 to
1.33 ⁄ 105 when oriﬁce diameter increases from 1.0 mm to
1.6 mm. This illustrates that large oriﬁce diameter leads to high
diffusivity ability and high kinetic energy of gas jet. The interaction
between gas jet and surrounding air increases, it beneﬁts the mix-
ing effect in intake port.
4. Conclusions
This current study used Schlieren imaging and numerical simu-
lation to investigate the evolution of shock wave structure of high
pressure gas injection. The effect of shock wave structure on gas
injection process and jet structure are analyzed. The main conclu-
sions of this paper are summarized as follows:
(1) Shock wave structure (Mach disk) is the main feature of high
pressure gas jet. The increase of Mach disk width promotes
gas jet near-ﬁeld cone angle which has positive effect on
mixing effect. The pressure situations in the nozzle are ana-
lyzed based on shock wave structure. It is shown that gas jet
will experience three different stages during the injection
process. The establishment and reduction of gas pressure
in the nozzle need some time. The long injection duration
after the end of gas injection is the main reason for high
HC emissions in PI natural gas engine.
(2) The energy transfer efﬁciency from gas source pressure
energy to gas jet kinetic energy at nozzle exit is less than
50% for different gas injection pressure and oriﬁce diameter.
Choking phenomenon limits the gas velocity at nozzle exit
and leads to small kinetic energy of gas jet. The small density
difference between gas jet and the surrounding air makes air
entrainment effect is weak. The high Reynolds number also
presents that it is necessary to strengthen air disturbance
in intake manifold in order to achieve homogeneous mixture
formation.
(3) High gas injection pressure and large oriﬁce diameter
increase the mass ﬂow rate of gas fuel at nozzle exit. This
is beneﬁcial to shorten gas injection pulse width and obtain
a homogeneous mixture. Decreasing the nozzle length and
increasing the nozzle ﬂow area are regarded as the most
effectively methods to reduce gas injection duration.
Acknowledgement
This work was supported by the National Natural Science Foun-
dation of China (Grant nos. 51406040), the Research Fund for Doc-
toral Program of Higher Education of China (Grant no.
20132304120034), Postdoctoral Science Foundation (Grant no.
2015M571392), and Heilongjiang Postdoctoral Science Foundation
(Grant no. LBH-Z14053).
References
[1] Youseﬁ A, Biroukb M, Lawlerc B, Gharehghania A. Performance and emissions
of a dual-fuel pilot diesel ignition engine operating on various premixed fuels.
Energy Convers Manage 2015;106:322–36. http://dx.doi.org/10.1016/j.
enconman.2015.09.056.
[2] Fan B, Pan J, Liu Y, Zhu Y. Effects of ignition parameters on combustion process
of a rotary engine fueled with natural gas. Energy Convers Manage
2015;103:218–34. http://dx.doi.org/10.1016/j.enconman.2015.06.055.
[3] Pourkhesalian AM, Shamekhi AH, Salimi F. Alternative fuel and gasoline in an
SI engine: a comparative study of performance and emissions characteristics.
Fuel 2010;89:1056–63. http://dx.doi.org/10.1016/j.fuel.2009.11.025.
[4] Kalam M, Masjuki H. An experimental investigation of high performance
natural gas engine with direct injection. Energy 2011;36:3563–71. http://dx.
doi.org/10.1016/j.energy.2011.03.066.
[5] Wei L, Peng G. A review on natural gas/diesel dual fuel combustion, emissions
and performance. Fuel Process Technol 2016;142:264–78. http://dx.doi.org/
10.1016/j.fuproc.2015.09.018.
[6] Cho HM, He BQ. Spark ignition natural gas engines – a review. Energy Convers
Manage 2007;48:608–18. http://dx.doi.org/10.1016/j.enconman.2006.05.023.
[7] Yang B, Wei X, Xi C, Liu Y, Zeng K, Lai MC. Experimental study of the effects of
natural gas injection timing on the combustion performance and emissions of
a turbocharged common rail dual-fuel engine. Energy Convers Manage
2014;87:297–304. http://dx.doi.org/10.1016/j.enconman.2014.07.030.
[8] Wang B, Li T, Ge L, Ogawa H. Optimization of combustion chamber geometry
for natural gas engines with diesel micro-pilot-induced ignition. Energy
Convers Manage 2016;122:552–63. http://dx.doi.org/10.1016/j.
enconman.2016.06.027.
[9] Chitsaz I, Saidi MH, Mozafari AA, Hajialimohammadi A. Experimental and
numerical investigation on the jet characteristics of spark ignition direct
injection gaseous injector. Appl Energy 2013;105:8–16. http://dx.doi.org/
10.1016/j.apenergy.2012.11.023.
[10] Zhang Q, Li MH, Shao SD. Combustion process and emissions of a heavy-duty
engine fueled with directly injected natural gas and pilot diesel. Appl Energy
2015;157:217–28. http://dx.doi.org/10.1016/j.apenergy.2015.08.021.
[11] Mohamad TI, Yusoff A, Abdullah S, Jermy M, Harrison M, Geok HH. The
combustion and performance of a converted direct injection compressed
natural gas engine using spark plug fuel injector. SAE technical paper; 2010.
http://dx.doi.org/10.4271/2010-32-0078.
0
0.5
1
1.5
2
2.5
3
0 5 10 15 20 25 30
Reexit [105]
tASOI [ms]
NPR=6 ,Pb=0.1MPa
NPR=11,Pb=0.1MPa
NPR=16,Pb=0.1MPa
(a)
0
0.2
0.4
0.6
0.8
1
1.2
1.4
11 . 2 1 . 4 1 . 6
Remax [105]
Diameter (mm)
(b)
Fig. 19. Effects of gas injection pressure and oriﬁce diameter on Reynolds number at nozzle exit. (a) Various NPRs, D = 1.0 mm and (b) various oriﬁce diameters, NPR =6 ,
Pb = 0.1 MPa.
Q. Dong et al. / Energy Conversion and Management 149 (2017) 26–38 37

<!-- PDF_PAGE: 13 -->

[12] Ryu K. Effects of pilot injection timing on the combustion and emissions
characteristics in a diesel engine using biodiesel–CNG dual fuel. Appl Energy
2013;111:721–30. http://dx.doi.org/10.1016/j.apenergy.2013.05.046.
[13] Ji S, Lan X, Cheng Y, Zhao X, Li X, Wang F. Cyclic variation of large-bore multi
point injection engine fuelled by natural gas with different types of injection
systems. Appl Therm Eng 2016;102:1241–9. http://dx.doi.org/10.1016/j.
applthermaleng.2016.03.082.
[14] Fan B, Pan J, Yang W, Liu Y, Bani S, Chen W. Numerical investigation of the
effect of injection strategy on mixture formation and combustion process in a
port injection natural gas rotary engine. Energy Convers Manage
2017;133:511–23. http://dx.doi.org/10.1016/j.enconman.2016.10.070.
[15] Yu J, Vuorinen V, Hillamo H, Sarjovaara T, Kaario O, Larmi M. An experimental
investigation on the ﬂow structure and mixture formation of low pressure
ratio wall-impinging jets by a natural gas injector. J Nat Gas Sci Eng
2012;9:1–10. http://dx.doi.org/10.1016/j.jngse.2012.05.003.
[16] Baratta M, Rapetto N. Mixture formation analysis in a direct-injection NG SI
engine under different injection timings. Fuel 2015;159:675–88. http://dx.doi.
org/10.1016/j.fuel.2015.07.027.
[17] Semin, Cahyono B, Amiadji, Bakar RA. Air–fuel mixing and fuel ﬂow velocity
modeling of multi holes injector nozzle on CNG marine engine. Proc Earth
Planet Sci 2015;14:101–9. http://dx.doi.org/10.1016/j.proeps.2015.07.09.
[18] Erfan I, Hajialimohammadi A, Chitsaz I, Ziabasharhagh M, Martinuzzi RJ.
Inﬂuence of chamber pressure on CNG jet characteristics of a multi-hole high
pressure injector. Fuel 2017;197:186–93. http://dx.doi.org/10.1016/
j.fuel.2017.02.018.
[19] Erfan I, Chitsaz I, Ziabasharhagh M, Hajialimohammadi A, Fleck B. Injection
characteristics of gaseous jet injected by a single-hole nozzle direct injector.
Fuel 2015;160:24–34. http://dx.doi.org/10.1016/j.fuel.2015.07.037.
[20] Vuorinen V, Yu J, Tirunagari S, Kaario O, Larmi M, Duwig C, et al. Large-eddy
simulation of highly underexpanded transient gas jets. Phys Fluids
2013;25:016101–16122. http://dx.doi.org/10.1063/1.4772192.
[21] Rogers T, Petersen P, Koopmans L, Lappas P, Boretti A. Structural
characteristics of hydrogen and compressed natural gas fuel jets. Int J
Hydrogen Energy 2015;40:1584–97. http://dx.doi.org/10.1016/j.
ijhydene.2014.10.140.
[22] Otobe Y, Kashimura H, Matsuo S, Setoguchi T, Kim HD. Inﬂuence of nozzle
geometry on the near-ﬁeld structure of underexpanded sonic jet. J Fluid Struct
2008;24:281–93. http://dx.doi.org/10.1016/j.jﬂuidstructs.2007.07.003.
[23] Hamzehloo A, Aleiferis PG. Gas dynamics and ﬂow characteristics of highly
turbulent under-expanded hydrogen and methane jets under various nozzle
pressure ratios and ambient pressures. Int J Hydrogen Energ
2016;41:6544–66. http://dx.doi.org/10.1016/j.ijhydene.2016.02.017
.
[24] Mohamad TI, Harrison M, Jermy M, How HG. The structure of the high-
pressure gas jet from a spark plug fuel injector for direct fuel injection. J
Visualiz 2010;13(2):121–31. http://dx.doi.org/10.1007/s12650-009-0017-2.
[25] Mohamad TI. In-water injection of high-pressure pulsed gas jet: a simple
analytical tool for direct injection of gaseous fuels in automotive engine. Fuel
2015;160:386–92. http://dx.doi.org/10.1016/j.fuel.2015.07.083.
[26] Vuorinen V, Wehrfritz A, Duwig C, Boersma BJ. Large-eddy simulation on the
effect of injection pressure and density on fuel jet mixing in gas engines. Fuel
2014;130:241–50. http://dx.doi.org/10.1016/j.fuel.2014.04.045.
[27] Donaldson CD, Snedeker RS. A study of free jet impingement. Part 1 – Mean
properties of free and impinging jets. J Fluid Mech 1971;45:281–319. http://
dx.doi.org/10.1017/s0022112071000053.
[28] White TR, Milton BE. Shock wave calibration of under-expanded natural gas
fuel jets. Shock Waves 2008;18:353–64. http://dx.doi.org/10.1007/s00193-
008-0158-6.
[29] Yu J, Vuorinen V, Kaario O, Sarjovaara T, Larmi M. Visualization and analysis of
the characteristics of transitional underexpanded jets. Int J Heat Fluid
2013;44:140–54. http://dx.doi.org/10.1016/j.ijheatﬂuidﬂow.2013.05.015.
[30] Hamzehloo A, Aleiferis PG. Large eddy simulation of highly turbulent under-
expanded hydrogen and methane jets for gaseous-fuelled internal combustion
engines. Int J Hydrogen Energ 2014;39:21275–96. http://dx.doi.org/10.1016/j.
ijhydene.2014.10.016.
[31] Ashkenas H. The structure and utilization of supersonic free jets in low density
wind tunnels. Rareﬁed Gas Dyn 1966;2:84 .
[32] Abraham J, Magi V, Maclnnes J, Bracco FV. Gas versus spray injection: which
mixes faster? SAE technical paper 940895. http://dx.doi.org/10.4271/940895.
38 Q. Dong et al. / Energy Conversion and Management 149 (2017) 26–38
