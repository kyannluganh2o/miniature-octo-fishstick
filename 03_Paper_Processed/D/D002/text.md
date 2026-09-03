<!-- PDF_PAGE: 1 -->

Effect of shock waves on the evolution of high-pressure fuel jets
Weidi Huang a,b, Zhijun Wu b,⇑, Ya Gao b, Lin Zhang b
a College of Mechanical and Vehicle Engineering, Hunan University, Changsha 410082, China
b School of Automotive Studies, Tongji University, Shanghai 201804, China
highlights
/C15 A new criterion of shock wave generation for high-pressure fuel jets is proposed according to the experiments.
/C15 Penetration characteristics of shock wave and non-shock wave fuel jets are acquired and major difference is found.
/C15 A modiﬁed numerical model, which has wide application range from subsonic state to supersonic state, is introduced.
article info
Article history:
Received 5 April 2015
Received in revised form 29 July 2015
Accepted 15 August 2015
Available online 21 September 2015
Keywords:
Shock wave
Fuel jets
Computational model
Diesel engine
abstract
In the modern diesel engine, with increasingly higher injection pressures, shock waves will appear with
high velocity fuel jets. To better understand the effect of shock waves on the atomization of fuel sprays,
diesel fuel injected at a pressure of 60 to 120 MPa was studied using a schlieren imaging visualisation
system. The initiation and boundary conditions of the shock wave initiated by fuel jets were examined.
A clear difference of spray penetration between the shock-wave state and the non-shock-wave state was
recorded in a nitrogen (N
2) and sulphur hexaﬂuoride (SF 6) gas atmosphere. By eliminating the other
potential explanations, such as pressure drop differences and the enhancement of gas density, it is shown
that the shock wave itself had a predominant effect on the evolution of high-pressure fuel jets.
Additionally, a computational model considering the Mach number was developed to predict the spray
penetration. The model was found to have excellent agreement with the presented experimental results.
/C2112015 Elsevier Ltd. All rights reserved.
1. Introduction
High-pressure fuel jets are an essential technology for many
applications, including fuel injection systems, thermal and plasma
spray coatings, and supersonic combustion [1–3]. In the case of a
fuel injection system, improving spray atomization is crucial for
the clean and efﬁcient combustion process in a diesel engines.
For this purpose, different studies that aimed to comprehend the
fundamentals of fuel injection have been conducted over decades.
The investigations proved that the quality of spray atomization
correlates strongly with the injection and environment conditions
[4–6]. The hydraulic behaviour inside the diesel nozzle also helps
to determine the spray evolution and air–fuel mixing process
[7–9]. Nevertheless, due to the highly transient and multiphase
process of fuel injection, the inherent mechanism of spray
atomization and evaporation still has not been conclusively
determined [10–12].
Currently, the most common approach to improve the quality of
spray atomization in a diesel engine is to increase the injection
pressure [13–17]. The common-rail system is capable of delivering
fuel at a pressure of over 160 MPa and has been widely applied to
modern diesel engines; however, even higher injection pressures
(approximately 300 MPa) have been achieved in the laboratory.
For example, Wang et al. [15] conducted a spray ﬂat-wall-
impinging experiment under ultra-high pressure (300 MPa). The
results showed that injections under ultra-high pressure generated
a higher momentum, providing better atomization quality
throughout the entire injection process.
With the elevated injection pressure, the speed of the fuel spray
increases accordingly, and a supersonic spray jet could eventually
be generated. Therefore, the generation of a shock wave in the
injection process of a modern diesel engine is inevitable. A shock
wave is a type of propagating disturbance that is potentiated by
a supersonic velocity that travels through a medium and carries
energy. By utilising the schlieren image technique, Nakahira et al.
ﬁrst found the existence of a shock wave during the injection pro-
cess of a diesel engine [18]. Then, with the X-ray radiograph image
technique, MacPhee et al. more clearly observed the shock wave
http://dx.doi.org/10.1016/j.apenergy.2015.08.053
0306-2619//C2112015 Elsevier Ltd. All rights reserved.
⇑ Corresponding author. Tel./fax: +86 21 69589205.
E-mail address: zjwu@tongji.edu.cn (Z. Wu).
Applied Energy 159 (2015) 442–448
Contents lists available at ScienceDirect
Applied Energy
journal homepage: www.elsevier.com/locate/apenergy

<!-- PDF_PAGE: 2 -->

phenomenon in diesel sprays. Moreover, they also found that there
was an average of a 15% increase in the gas density near the shock
front [19].
The existence of shock wave generation in diesel sprays has been
proved, and an increased effort has been given to investigate the
inﬂuence of shock waves on the diesel spray characteristics. In
one aspect, different from the other supersonic processes, the diesel
fuel injected by the common rail system is continuous, compress-
ible and multiphase. Therefore, it is important to consider the initial
shock wave condition in the diesel injection process to better eval-
uate the possibility and range of shock wave existence under prac-
tical diesel engine working conditions. The majority of the previous
investigations used a spray tip velocity that exceeded the local
sound speed as the initial condition for shock wave generation in
the diesel spray [20–22]. Research indicates that Pickett et al. pro-
vided the most representative investigation [22]. It was concluded
that increasing the ambient temperature and density both inhibit
shock wave generation. Thus, spray-generated shock waves are
not expected at the injection timings typical of a diesel engine [22].
However, the measuring results of the mass ﬂow rate and the
momentum at the nozzle exit indicate that the speed of fuel jets
initially increase, stabilize and ﬁnally decrease throughout the
injection process [23–26]. Therefore, if fuel injection is simply con-
sidered as diesel droplets that successively exit from the nozzle,
the velocity of the ﬁrst droplet (the spray tip velocity) is not the
highest. Moon et al. also found that the liquid jets decelerate in
both the axial and transverse directions after exiting the oriﬁce
through the use of the multi-exposed X-ray phase-contrast image
technique [27]. As a consequence, the initial shock wave condition
in the diesel injection process should be reconsidered.
In another aspect, various studies have been conducted to
unveil the interaction mechanism experimentally and numerically
between the diesel spray and the shock wave. Amongst the exper-
imental investigations, Sittiwong et al. found that diesel sprays
under actual conditions may deviate from the theoretical predic-
tions of the injection pressure ﬂuctuation, the gas density uneven-
ness and the shock wave occurrence [28]. Payri et al. found a 6%
difference of spray tip penetration between the results from N 2
and SF 6 and attributed this difference to shock wave generation.
However, they did not present any further analysis [29].
Amongst the numerical investigations, Roisman et al. proposed
a correlation to simulate the spray penetration in the supersonic
state by approximating the shock as a normal adiabatic compres-
sion wave [30]. However, the results calculated with the correla-
tion were underestimated compared to the experimental data
given by MacPhee et al. [19]. Im et al. [31] also analysed the mech-
anism of shock wave generation and its impact on spray behaviour
numerically. Although these simulation results achieved excellent
agreement in the excess air density with the experimental data,
their ability to predict spray tip penetration still lacks precision.
The spray tip penetration and prediction model are very important
in diesel spray investigations and engine design [32–34]. A detailed
study of the supersonic-state spray evolution can help researchers
to better understand spray behaviour in the modern diesel engine.
The main objective of the present work was to investigate the
effect of shock wave on the evolution of high-pressure diesel jets.
For this purpose, the study ﬁrst focused on the shock wave initia-
tion condition during the injection process. Then, based on the
property that local sound speeds at different atmospheres differ
greatly, spray jets of the shock wave state and non-shock wave
state were achieved under the same injection pressure and same
gas densities. By comparing the variance of the spray characteris-
tics at these two states, the inﬂuence of the shock wave on the
spray development was effectively and quantitatively analysed.
Furthermore, a modiﬁed model was developed to estimate the
penetration behaviour of supersonic liquid jets.
2. Experimental details
2.1. Experimental apparatus
The experiment was conducted using the schlieren imaging
visualisation test system, which is illustrated in Fig. 1 . The test
rig consisted of a common rail injection system, a control unit, a
constant volume vessel and an imaging system. The schlieren
images of the shock waves were collected at 150,000 fps, a 1
ls
exposure time and a resolution of 256 /C2 24 pixels. Detailed
descriptions of the experimental method were given in a previous
publication [35].
2.2. Image processing
An imaging processing program was developed with Matlab to
analyse the original schlieren images captured by the high-speed
camera. Fig. 2 shows a typical image before and after imaging pro-
cessing (the nozzle tip was added afterwards to work as a refer-
ence). The spray is characterised by spray tip penetration ( S),
which has been widely applied in previous investigations. The
velocities of the spray tip and the shock wave were accordingly cal-
culated by the displacement of the leading-edge position and the
imaging rate. To better present the shock-wave structure, the
images were re-coloured according to the image grayscale. Re-
coloured blue
1 and red areas corresponded to the original light-
coloured area (small gas density) and the original dark-coloured area
(large gas density), respectively, while the white area represented
the background.
2.3. Experimental conditions
Two single-hole nozzles (HEG-0 and HEG-9.0) with similar
internal geometries were employed for the investigation. Four
structural parameters, including the outlet diameter, inlet diame-
ter, oriﬁce length and inlet rounding radius, were used to charac-
terise the nozzle internal geometries. Their deﬁnitions can be
found in Refs. [36,37]. The nozzle geometries were measured by
Huang [36] and are summarised in Table 1. It should be mentioned
that the inlet diameter and the outlet diameter of these nozzles
were designed to be 180
lm and 160 lm, respectively. Thus, the
oriﬁce is divergent and the K-factor equals 2. However, it can be
seen in Table 1 that the measuring results are different from the
design values. These deviations correlate strongly with the manu-
facturing values. More in-depth analysis regarding the relationship
of the nozzle internal geometry and manufacturing can be drawn
from Ref. [37].
To create variation in the initial speed of the jets, four injection
pressures of 60 MPa, 80 MPa, 100 MPa and 120 MPa were selected.
For each tested injection pressure, two ambient gas densities were
used, 11.5 kg/m 3 and 34.5 kg/m 3. The experimental conditions and
properties of the two types of gases are listed in Table 2 .
3. Results and discussion
3.1. Boundary condition of shock wave initiation
To characterise the fuel spray in the shock-wave state and non-
shock-wave state, the boundary conditions of shock-wave initia-
tion should ﬁrst be deﬁned. The shock wave was initiated in all
of the tested conditions in a SF 6 atmosphere; therefore, Fig. 3 (a)
only illustrates the spray developments and initiation of the shock
1 For interpretation of colour in Fig. 2, the reader is referred to the web version of
this article.
W. Huang et al. / Applied Energy 159 (2015) 442–448 443

<!-- PDF_PAGE: 3 -->

wave under the different injection pressures in N 2 atmosphere.
When the injection pressure was higher than 80 MPa, shock waves
began to emerge. However, the peak velocity of the spray tip,
which is usually employed to determine whether the shock wave
would generate or not, was far below the local sound speed, as
shown in Fig. 3 (b). With further measurement, it was found that
the spreading speed of all of the waves was very close to
345.8 m/s, which was exactly the local sound speed. Therefore, it
could be concluded that the waves initiated by fuel spray were
indeed shock waves, even though the spray tip velocity was far
from the local sound speed.
Several issues were considered in attempting to explain this
observed phenomenon. First, the image resolution may cause a
measuring error within only 20 m/s, which was not sufﬁcient to
inﬂuence the results. Second, the impurity of the gas constituents
in the testing vessel could also be excluded because the spreading
speed of the shock waves remained stable at 345 m/s (close to N 2
local sound speed). Therefore, we come to the conjecture that the
spray tip velocity was not sufﬁcient to determine the generation
of the shock wave as we previously thought.
According to previous investigations [25,26], the velocity of the
fuel ﬂow at the nozzle exit is: _m
f ¼ qf /C2 Uo /C2 Ao, where _mf is the
instantaneous mass ﬂow rate, Uo is the nozzle outlet velocity, qf
is the fuel density (830 kg/m 3 in this study) and Ao is the nozzle
outlet area. The mass ﬂow rates were tested under different injec-
tion pressures based on the Bosch Long Tube method [36],b y
which the velocity of the fuel ﬂow at the nozzle exit could be cal-
culated. As shown in Fig. 4, under the injection pressure of 80 MPa,
the ﬂow speed at the nozzle exit in this study reached 354 m/s,
which was adequate to generate a shock wave in a N 2 atmosphere.
However, the supersonic moving speed of the bulges on the surface
of the spray jets could also initiate the shock waves. The generation
and spread of the shock waves at the nozzle exit areas in a N 2 gas
Fig. 1. The schlieren imaging visualisation test system [35].
Original Image
Background
Recoloured 
Image
small density large density 
Spray /g415p Penetra/g415on / St
Shock wave penetra/g415on / Sw
x 
Fig. 2. Original image, background image and the image after processing.
Table 1
Measurement results of the nozzle geometries [36].
HEG-0 HEG-9.0 Units
Outlet diameter 160.1 157.7 ( lm)
Inlet diameter 178.4 190.7 ( lm)
Oriﬁce length 648.4 651.1 ( lm)
Inlet rounding radius 21.8 57.4 ( lm)
Table 2
Experimental conditions.
N2 SF6 Units
Injection pressure 60, 80, 100, 120 (MPa)
Injection duration 1500 ( ls)
Molecular weight 28.01 146.05 (g/mol, 25 /C176C, 1 atm)
Sound speed 352.6 138.9 (m/s, 25 /C176C)
Gas density qa/Gas pressure Pb 11.5/(1) 11.5/(0.2) (kg/m 3/(MPa), 25 /C176C)
34.5/(3) 34.5/(0.6) (kg/m 3/(MPa), 25 /C176C)
444 W. Huang et al. / Applied Energy 159 (2015) 442–448

<!-- PDF_PAGE: 4 -->

atmosphere under an 80 MPa injection pressure became reason-
able. At an injection pressure of 60 MPa, the ﬂow speed at the noz-
zle exit was 300.2 m/s and did not meet the lowest requirement for
the shock wave generation; this result coincided with the experi-
ments conducted in the present study. In the study by Pickett
et al. [22], under a certain condition (injection pressure of
150 MPa, environmental gas density of 11.7 kg/m 3 and environ-
ment gas temperature of 455 K), an unexpected but clear shock
wave was observed when the velocity of the spray tip was 10% less
than local sound speed (432 m/s), and this phenomenon was
attributed to inadequate image resolution by the author. However,
the ﬂow velocity at the nozzle exit in the experiment by Pickett
et al.’s was 522 m/s (estimated by mass ﬂow rate) in the steady
state, which was higher than local sound speed. Hence, the
observed phenomenon might not be caused by the low image res-
olution as Pickett et al. considered. Finally, the velocity of the spray
at the nozzle exit is more suitable than the velocity at the spray tip
to predict shock wave generation. In modern diesel engines, the
injection pressure has been increased to over 160 MPa. Besides,
pre-injection technology (a short pilot injection before main injec-
tion) has increasingly been widely adopted in injection systems.
The combustion chamber is likely to be ﬁlled with a fuel vapour–
air mixture under high temperature before main injection begins.
It has been recognised that the mixture has a sonic speed that is
lower than that of either fuel vapour or air [19], so the generation
of shock waves during the fuel injection process should not be sur-
prising, even at elevated engine operating temperatures. Conse-
quently, studies of the inﬂuence of shock waves on the diesel
spray characteristics are needed.
3.2. Comparison of the penetration of the liquid jet between the shock
wave state and non-shock wave state
On the basis of the above investigations, two types of spray jets,
the shock-wave state and the non-shock-wave state, were
achieved under the same environmental gas density. The penetra-
tion of the fuel spray injected at 60 MPa under various densities are
shown in Fig. 5. Under the same gas density, the sprays with shock
waves (under SF
6 gas) developed apparently slower than the
sprays without shock waves (under N 2 gas). For instance, at an
injection timing of 600 ls, the spray tip penetration (Nozzle
HEG-0, gas density 11.5 kg/m 3) at the shock wave state was
20.6% smaller than at the non-shock wave state. With the gas den-
sity increased to 34.5 kg/m 3, the variance became 7.5% at the same
injection timing.
It is often assumed that different gas atmospheres might impact
spray jets differently and result in different spray characteristics
even with the same density. Fig. 6 presents the spray penetration
curves in N 2 and SF 6 at the same injection pressure of 120 MPa.
Under these experimental conditions, the spray jets were all
accompanied with shock waves. As is clearly shown in Fig. 6 , the
penetration curves under different gas atmospheres coincided if
the gas density was identical. Unfortunately, the needle of the
tested injector could only be opened when the injection pressure
was higher than 30 MPa. At this condition, the velocity of the spray
tip at the nozzle exit was 206.7 m/s, which was still higher than the
local sound speed in SF 6. Therefore, it was incapable of comparing
the non-shock wave state spray jets in different gas atmospheres,
which if achieved, might provide better veriﬁcation for this study.
It is important to note that the pressure drops from the inside to
the outside of the nozzles were distinct under N 2 and SF6 even with
the same gas density because the molecular weight of SF 6 is ﬁve
times higher than that of N 2. However, according to research by
Hiroyasu et al. [4], the calculation results showed that the spray
tip penetration variance caused by the pressure drops in the pre-
sent study was less than 1%, which could not explain the experi-
ment results. Another explanation may come from MacPhee et al.
[19] who observed a 15% average increase of gas density near the
shock front. This enhancement could inhibit the movement of a
droplet and may result in the penetration difference between the
shock wave state and the non-shock wave state. To analyse this
possibility, it was assumed that the enhanced gas density phe-
nomenon existed during the entire spray development process.
The investigation by Hiroyasu et al. produced a calculation
result that showed that penetration would only decrease by
(a) Re-coloured images of the spray and shock wave
(b) Velocity of spray tip versus time 
60 MPa 
80 MPa 
100 MPa 
120 MPa 
Fig. 3. Comparison of the spray images under different injection pressures in N 2
atmosphere. (injection timing 145 ls, gas density 34.5 kg/m 3).
Fig. 4. Nozzle exit velocity under different injection pressures in N 2 atmosphere.
W. Huang et al. / Applied Energy 159 (2015) 442–448 445

<!-- PDF_PAGE: 5 -->

approximately 3.5% when the shock wave was generated, which
was still much smaller compared to the presented experimental
results. Consequently, the enhancement of gas density near the
shock wave front should also not be assumed to be the main reason
to explain the difference of penetration observed in this investiga-
tion. After excluding all of the other possibilities, it was determined
that the shock wave phenomenon itself caused the penetration dif-
ferences observed in these experiments.
3.3. Numerical simulation of the supersonic liquid jets penetration
As previously stated, the spray tip penetration and its predic-
tion model are crucial in diesel spray investigation and engine
design. To better understand the spray behaviour in modern diesel
engines, a modiﬁed model to predict the spray characteristics in
the supersonic ﬂow condition was established, which considered
the spray behaviour as movements of single droplets based on
the method proposed by Sazhin et al. [38,39]. The equation is usu-
ally described by the following:
d
2
s
dt
2 ¼/C0 3
8r
qg
qd
CD
ds
dt /C0 vg
/C12/C12
/C12
/C12
/C12/C12
/C12
/C12
ds
dt /C0 vg
/C18/C19
ð1Þ
where s is the penetration; qg and qd are the densities of gas and
droplet, respectively; r is the radius of droplet; vd ¼ ds=dt; vg is
velocity of gas; and t is the time. The most important parameter
in the model is the drag coefﬁcient ( CD), which signiﬁcantly affects
the behaviour of the single droplet spray. Usually CD is only related
to the Reynolds’s number ðRe ¼ 2qg jvd /C0 vg jr=lg , and lg is the gas
kinetic viscosity). Using the traditional CD, the spray penetrations in
the shock-wave and non-shock-wave states should be the same, as
shown in Fig. 7 (Sim._original in the ﬁgure). However, the spray
penetration in the shock-wave state was obviously smaller than
in the non-shock-wave state. Consequently, it is concluded that
the Mach number ( M) plays an important role in the development
of the fuel spray when the velocity of the liquid jet is close to the
local sound speed. The proposed group of formulas by Parmar
et al. predict the relationship amongst CD, Re, and M within a certain
ranges ( Re 6 2 /C2 105 and 0 :6 6 M 6 1:75) [40]. When M < 0.6, the
suggestion of Sazhin et al. is used [38]. Ultimately, CD is calculated
according to Eq. (2). In this model, the droplet diameter and the gas
density are assumed to be constant. Two model parameters, k_11.5
and k_34.5, were added accordingly to account for the inﬂuence of
different gas density.
CDðRe; MÞ¼
0:44 if M 6 Mcr ¼ 0:6
CD;subðRe; MÞ if Mcr < M 6 1:0
CD;supðRe; MÞ if 1 :0 < M 6 1:75
8
><
>:
ð2Þ
In the supersonic regime, the drag coefﬁcient is expressed as:
CD;supðRe; MÞ¼ CD;M¼1ðReÞþ CD;M¼1:75ðReÞ/C0 CD;M¼1ðReÞ½/C138 nsupðRe; MÞ
ð3Þ
HEG-9.0
HEG-0
Fig. 5. The comparison of the spray penetration developments under the different
shock wave states. (injection pressure 60 MPa, non: non-shock wave state; sw:
shock wave state).
HEG-0 
HEG-9.0
Fig. 6. The comparison of the spray penetration developments under the same
shock wave states. (injection pressure 120 MPa, sw: shock-wave state.)
446 W. Huang et al. / Applied Energy 159 (2015) 442–448

<!-- PDF_PAGE: 6 -->

where
CD;M¼1ðReÞ¼ 24
Re ð1 þ 0:118Re0:813Þþ 0:69 1 þ 3550
Re0:793
/C18/C19 /C0 1
ð4Þ
CD;M¼1:75ðReÞ¼ 24
Re 1 þ 0:107Re0:867
/C16/C17
þ 0:646 1 þ 861
Re0:634
/C18/C19 /C0 1
ð5Þ
and
nsup ðRe; MÞ¼
X3
i¼1
f i;supðMÞ
Y3
j–i
j¼i
log Re /C0 Cj;sup
Ci;sup /C0 Cj;sup
ð6Þ
with
f 1;supðMÞ¼/C0 2:963 þ 4:392M /C0 1:169M2 /C0 0:027M3
/C0 0:233 exp½ð1 /C0 MÞ=0:011/C138ð 7Þ
f 2;supðMÞ¼/C0 6:617 þ 12:11M /C0 6:501M2 þ 1:182M3
/C0 0:174 exp½ð1 /C0 MÞ=0:01/C138ð 8Þ
f 3;supðMÞ¼/C0 5:866 þ 11:57M /C0 6:665M2 þ 1:312M3
/C0 0:350 exp½ð1 /C0 MÞ=0:012/C138ð 9Þ
and C1;sup ¼ 6:48; C2;sup ¼ 8:93; C3;sup ¼ 12:21.
In the intermediate regime, the drag coefﬁcient is expressed as
a nonlinear interpolation between M ¼ Mcr and M ¼ 1:
CD;Mcr ðReÞ¼ 24
Re 1 þ 0:15Re0:684
/C16/C17
þ 0:513 1 þ 483
Re0:669
/C18/C19 /C0 1
ð10Þ
CD;subðRe; MÞ¼ CD;Mcr ðReÞ
þ CD;M¼1ðReÞ/C0 CD;Mcr ðReÞ½/C138 nsubðRe; MÞð 11Þ
where
nsubðRe; MÞ¼
X3
i¼1
f i;subðMÞ
Y3
j–i
j¼i
log Re /C0 Cj;sub
Ci;sub /C0 Cj;sub
ð12Þ
with
f 1;subðMÞ¼/C0 1:884 þ 8:422M /C0 13:70M2 þ 8:162M3 ð13Þ
f 2;subðMÞ¼/C0 2:228 þ 10:35M /C0 16:96M2 þ 9:840M3 ð14Þ
f 3;subðMÞ¼ 4:362 /C0 16:91M þ 19:84M2 /C0 6:296M3 ð15Þ
and C1;sub ¼ 6:48; C2;sub ¼ 9:28; C3;sub ¼ 12:21.
The computational results are illustrated in Fig. 7 (Sim._new_
non and Sim._new_sw in the ﬁgure). It can be seen from Fig. 7 that
the new model with the introduction of variable CDðRe; MÞ can pre-
dict the spray characteristics in the two states well. It demon-
strates that the inﬂuence of M is ineligible in the investigations
of supersonic diesel spray, especially considering the increasingly
higher injection pressure in modern diesel engines.
4. Conclusions
In this study, the effect of shock waves on the characteristics of
a high-pressure fuel spray was investigated in a N 2 and SF 6 gas
atmosphere. The schlieren imaging system clearly distinguished
the spray jets in the shock-wave state and in the non-shock-
wave state. Furthermore, the spray boundary condition in the
shock-wave state was acquired. The effect of the appearance of a
shock wave on the fuel spray evolution was experimentally and
numerically examined under the same injection pressure and
ambient gas density. The following conclusions could be drawn:
(1) To predict the generation of shock waves, instead of the
spray velocity at the spray tip, the velocity at the nozzle exit
should be employed. The possibility of shock wave genera-
tion in an engine cylinder is much higher with this new cri-
terion than formerly considered.
(2) The fuel spray characteristics between the shock-wave state
and non-shock-wave state sprays are found to be of great
difference.
(3) A modiﬁed numerical model is developed to predict the pen-
etration of supersonic liquid jets by introducing a variable
CD ðRe; MÞ number and is validated by the experimental data.
This new model can better simulate the penetration of fuel
spray over a wide range, from the subsonic state to the
supersonic state.
Acknowledgements
We acknowledge discussions with Jin Wang from Argonne
National Laboratory and Zhengbai Liu from Dongfeng Motor Corpo-
ration. This study was also supported by the National Nature Foun-
dation (51076118, 91441125, 51006075).
Fig. 7. The comparison of the penetration evolution between computational and
experimental data. (injection pressure 60 MPa; Sim.: simulation results; Exp.:
experimental results.)
W. Huang et al. / Applied Energy 159 (2015) 442–448 447

<!-- PDF_PAGE: 7 -->

References
[1] Khan MN, Shamim T. Investigation of a dual-stage high velocity oxygen fuel
thermal spray system. Appl Energy 2014;130:853–62 .
[2] Wang ZG, Wu LY, Li QL, Li C. Experimental investigation on structures and
velocity of liquid jets in a supersonic crossﬂow. Appl Phys Lett
2014;105:134102(1)–2(4).
[3] Nakaya S, Hikichi Y, Nakazawa Y, Sakaki K, Choi M, Tsue M, et al. Ignition and
supersonic combustion behavior of liquid ethanol in a scramjet model
combustor with cavity ﬂame holder. Proc Combust Inst 2015;35:2091–9 .
[4] Hiroyasu H, Arai M. Structure of fuel sprays in diesel engine. SAE Tech Paper
900475; 1990.
[5] Li D, Zhen H, Xingcai L, Wu-gao Z, Jian-guang Y. Physico-chemical properties of
ethanol–diesel blend fuel and its effect on performance and emissions of diesel
engines. Renewable Energy 2005;30:967–76 .
[6] Soid SN, Zainal ZA. Spray and combustion characterization for internal
combustion engines using optical measuring techniques – a review. Energy
2011;36(2):724–41
.
[7] Payri R, Salvador FJ, Gimeno J, Novella R. Flow regime effects on non-cavitating
injection nozzles over spray behavior. Int J Heat Fluid Flow 2011;32
(1):273–84.
[8] Som S, Ramirez AI, Longman DE, Aggarwal SK. Effect of nozzle oriﬁce geometry
on spray, combustion, and emission characteristics under diesel engine
conditions. Fuel 2011;90(3):1267–76
.
[9] Mohan B, Yang W, Yu W. Effect of internal nozzle ﬂow and thermo-physical
properties on spray characteristics of methyl esters. Appl Energy
2014;129:123–34.
[10] Jiang X, Siamas GA, Jagus K, Karayiannis TG. Physical modelling and advanced
simulations of gas a liquid two-phase jet ﬂows in atomization and sprays. Prog
Energy Combust Sci 2010;36:131–67
.
[11] Linne M. Imaging in the optically dense regions of a spray: a review of
developing techniques. Prog Energy Combust Sci 2013;39:403–40 .
[12] Cung K, Moiz A, Johnson J, Lee SY, Kweon CB, Montanaro A. Spray-combustion
interaction mechanism of multiple-injection under diesel engine conditions.
Proc Combust Inst 2014:3061–8 .
[13] Delacourt E, Desmet B, Besson B. Characterisation of very high pressure diesel
sprays using digital imaging techniques. Fuel 2005;84:859–67 .
[14] Klein-Douwel RJH, Frijters PJM, Seykens XLJ, Somers LMT, Baert RSG. Gas
density and rail pressure effects on diesel spray growth from a heavy-duty
common rail injector. Energy Fuels 2009;23(2):1832–42 .
[15] Wang X, Huang Z, Zhang W, Kuti OA, Nishida K. Effects of ultra-high injection
pressure and micro-hole nozzle on ﬂame structure and soot formation of
impinging diesel spray. Appl Energy 2011;88:1620–8 .
[16] Kuti OA, Nishida K, Zhu J. Experimental studies on spray and gas entrainment
characteristics of biodiesel fuel: implications of gas entrained and fuel oxygen
content on soot formation. Energy 2013;57:434–42
.
[17] Eagle EW, Morris SB, Wooldridge MS. High-speed imaging of transient diesel
spray behavior during high pressure injection of a multi-hole fuel injector.
Fuel 2014;116:299–309 .
[18] Nakahira T, Komori M, Nishida M, Tsujimura K. The shock wave generation
around the diesel fuel spray with high pressure injection. SAE-920460; 1992.
[19] MacPhee AG, Tate MW, Powell CF, et al. X-ray imaging of shock waves
generated by high-pressure fuel sprays. Science 2002;2002(295):1261–3
.
[20] Im K, Lai M, Wang J. Development process of shock waves by supersonic spray.
SAE-2004-01-1769; 2004.
[21] Pianthong K, Matthujak A, Takayama K, Milton BE, Behnia M. Dynamic
characteristics of pulsed supersonic fuel sprays. Shock Waves 2008;18:1–10 .
[22] Pickett LM, Kook S. Effect of ambient temperature and density on shock wave
generation in a diesel engine. Atomization Sprays 2010;20(2):163–75 .
[23] Im K-S, Fezzaa K, Wang YJ, Liu X, Wang J, Lai M-C. Particle tracking velocimetry
using fast X-ray phase-contrast imaging. Appl Phys Lett 2007;90:091919 .
[24] Desantes JM, Payri R, Garcia JM, Salvador FJ. A contribution to the
understanding of isothermal diesel spray dynamics. Fuel 2007;86:1093–101 .
[25] Payri R, Salvador FJ, Gimeno J, De la Morena J. Inﬂuence of injector technology
on injection and combustion development – Part 1: Hydraulic
characterization. Appl Energy 2011;88(4):1068–74
.
[26] Macian V, Payri R, Ruiz S, Bardi M, Plazas AH. Experimental study of the
relationship between injection rate shape and diesel ignition using a novel
piezo-actuated direct-acting injector. Appl Energy 2014;118:100–13 .
[27] Moon S, Gao Y, Wang J, Fezzaa K, Tsujimura T. Near-ﬁeld dynamics of high-
speed diesel sprays: effects of oriﬁce inlet geometry and injection pressure.
Fuel 2014;133:299–309
.
[28] Sittiwong W, Pianthong K, Seehanam W, Milton BE, Takayama K. Effects of
chamber temperature and pressure on the characteristics of high speed diesel
jets. Shock Waves 2012;22:215–23 .
[29] Desantes JM, Payri R, Salvador FJ, Soare V. Study of the inﬂuence of geometrical
and injection parameters on diesel sprays characteristics in isothermal
conditions. SAE-2005-01-0913; 2005.
[30] Roisman IV, Araneo L, Tropea C. Effect of ambient pressure on penetration of a
diesel spray. Int J Multiphase Flow 2007;33:904–20 .
[31] Im KS, Cheong SK, Liu X, et al. Interaction between supersonic disintegrating
liquid jets and their shock waves. Phys Rev Lett 2009;102:1–4
.
[32] Kostas J, Honnery D, Soria J. Time resolved measurements of the initial stages
of fuel spray penetration. Fuel 2009;88(11):2225–37 .
[33] Payri R, Gimeno J, Bardi M, Plazas AH. Study liquid length penetration results
obtained with a direct acting piezo electric injector. Appl Energy
2013;106:152–62.
[34] Han D, Wang C, Duan Y, Tian Z, Huang Z. An experimental study of injection
and spray characteristics of diesel and gasoline blends on a common rail
injection system. Energy 2014;75:513–9
.
[35] Huang WD, Wu ZJ, Gao Y, Li ZL, Li LG. Shock wave generation and its
inﬂuencing parameters based on diesel injector. Chin Sci Bull 2014;59
(27):3504–10.
[36] Huang WD. Measurement of nozzle internal structure based on high energy X-
ray and study of its inﬂuence mechanism on diesel spray characteristics [Ph.D.
thesis]. Tongji University Press; 2014.
[37] Huang WD, Wu ZJ, Gao Y, Li ZL, Gong HF, Li LG. Effects of hydro erosive
grinding on the symmetry of nozzle oriﬁce geometries. Chin Int Combust
Engine Eng 2014;35(3):57–61 .
[38] Sazhin S, Crua C, Kennaird D, Heikal M. The initial stage of fuel spray
penetration. Fuel 2003;82(8):875–85
.
[39] Turner MR, Sazhin SS, Healey JJ, Crua C, Martynov SB. A breakup model for
transient diesel fuel sprays. Fuel 2012;97:288–305 .
[40] Parmar M, Haselbacher A, Balachandar S. Improved drag correlation for
spheres and application to shock-tube experiments. AIAA J 2010;48
(6):1273–6
.
448 W. Huang et al. / Applied Energy 159 (2015) 442–448
