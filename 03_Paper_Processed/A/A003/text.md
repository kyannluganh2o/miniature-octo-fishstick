<!-- PDF_PAGE: 1 -->

Experimental investigation on performance and heat release analysis
of a pilot ignited direct injection natural gas engine
Menghan Li a, Qiang Zhang a, *, Guoxiang Li a, Sidong Shao b
a School of Energy and Power Engineering, Shandong University, 17923 Jingshi Road, Jinan, Shandong, 250061, China
b Weichai Westport Inc., 197 Fushou East Street, Weifang, Shandong, 261001, China
article info
Article history:
Received 3 September 2014
Received in revised form
3 May 2015
Accepted 22 June 2015
Available online 15 July 2015
Keywords:
Combustion characteristics
Direct injection natural gas engine
Heat release rate
abstract
Pilot ignited direct injection natural gas engines undertake signiﬁ cant advantages over conventional
diesel engine with speci ﬁc combustion mode. In this paper, extensive experiments have been carried out
to provide further understanding of performance and heat release rate under different operating con-
ditions. Through the experimental investigations and detailed analysis, it is demonstrated that shortened
injection interval and diesel injection pulse width as well as increased injection pressure lead to an
increase in maximum in-cylinder pressure and deteriorated combustion noise. The maximum heat
release rate is raised by retarding injection timing, reducing injection interval, shortening diesel injection
pulse width and increasing injection pressure. The stability of combustion shows uncertain trends with
the variation of injection timing and pilot diesel injection quantity, while can be generally improved by
the adoption of shorter injection interval and lower injection pressure. It is also revealed that fuel
economy can bene ﬁt from the application of advanced injection timing, smaller diesel injection pulse
width, shorter injection interval and higher injection pressure.
© 2015 Elsevier Ltd. All rights reserved.
1. Introduction
Nowadays, the increasing concerns on environmental crisis and
energy shortage have led to a research focus on the application of
alternative fuels for transportation applications, especially for
heavy-duty ones [1]. Natural gas, with the advantage of low carbon
content, is widely recognized as having great potential to solve the
problem of greenhouse gas emissions [2]. Further, rapid global
expansion of unconventional natural gas development, such as
shale gas and coal seam gas, has made it a more desirable fuel [3].
However, in most current spark ignition natural gas engines,
natural gas is premixed with air and a throttle is utilized to control
the air-fuel ratio, hence reduction in thermal efﬁ ciency and asso-
ciated sacriﬁce of output torque in order to avoid damages caused
by knocking are inevitable [4,5]. Pilot ignited direct injection nat-
ural gas engines use the technique of injecting small amount of
diesel to ignite the directly injected natural gas. As the fuels are
non-premixed, higher thermal efﬁ ciency could be obtained with
little changes to the baseline diesel engine [6]. In addition, pilot
ignited direct injection natural gas engines, by using the diesel
thermodynamic cycle, can maintain operating temperature similar
to diesel engines, thus eliminating the thermal load problems and
leading to improved durability.
The combustion process of pilot ignited direct injection natural
gas engines is fairly different from both spark ignition natural gas
engines and diesel engines, as the combustion is compression
initiated and two fuels are involved. Additionally, both fuels are
injected directly by the same injector at the end of compression
stroke, therefore the working behavior of pilot ignited direct injec-
tion natural gas engines is also distinguished from conventional dual
fuel engines and low pressure direct injection natural gas engines, in
which spark plug or glow plug is employed to act as ignition source.
Much work has been done on the performance and combustion
characteristics in this type of engine. Douville[7] developed a multi-
zone combustion analysis model to investigate the combustion rates
Abbreviations: ATDC, after top dead center; BTDC, before top dead center; BSFC,
brake speciﬁ c fuel consumption; CA, crank angle; C.H.R, cumulative heat release;
CNG, compressed natural gas; COV, coef ﬁcient of variation; D2P, second derivation
of in-cylinder pressure; DPW, injection pulse width of pilot diesel; DRP, diesel rail
pressure; ECU, electronic control unit; EGR, exhaust gas recirculation; GPW, in-
jection pulse width of natural gas; H.R.R, heat release rate; IMEP, indicated mean
effective pressure; LNG, lique ﬁed natural gas; MFB0 e10%, 0 e10% mass fraction
burned duration; MFB10 e90%, 10 e90% mass fraction burned duration; MFB50%,
phase angle of 50% mass fraction burned; PSEP, pilot diesel to natural gas injection
separation; rpm, revolutions per minute; n, engine speed; NSOI, start of natural gas
injection.
* Corresponding author. Tel.: þ86 13791033095.
E-mail address: sduzqtg@163.com (Q. Zhang).
Contents lists available at ScienceDirect
Energy
journal homepage: www.elsevier.com/locate/energy
http://dx.doi.org/10.1016/j.energy.2015.06.089
0360-5442/© 2015 Elsevier Ltd. All rights reserved.
Energy 90 (2015) 1251 e1260

<!-- PDF_PAGE: 2 -->

along with heat transfer to cylinder walls and evaluated the effects
of injection timing, injection rate, engine load and speed using both
experimental and computational methods. It can be summarized
from his study that the combustion rate of dual fuel mode was
higher than that of pure diesel mode and the combustion rates of
both modes decreased with increasing load as a result of the
increased proportion of mixing-controlled combustion. Hill and
Douville [8] proposed a method incorporating nonlinear regression
technique to determine the cylinder heat loss rate, the ignition delay,
the mass burning rate as well as the burned gas temperature by
measurements of intake/exhaust charge and in-cylinder pressure
curves. Li et al. [9] presented a CFD (computational ﬂuid dynamics)
combustion model together with an injector model to simulate the
in-cylinder mixing and combustion process. They also calibrated
and validated the model by a set of experimental results. It was
revealed by their simulation results that the model could simulate
accurately under conditions without EGR (exhaust gas recircula-
tion), however, under high EGR conditions, the model had large
prediction errors. Lee et al. [10] modeled the combustion of both
fuels based on different detailed chemical mechanisms to ﬁnd a
mechanism that could adequately predict the combustion process
with reasonable computational ef ﬁciency. On the basis of the
modeling work, they concluded that the changing trends of the
simulation results were not sensitive to the mechanism applied.
McTaggart-Cowan et al. assessed the effects of injection pressure,
injection interval [1 1,12], fuel composition [13] as well as compres-
sion ratio [14] on the combustion behavior. Their experimental re-
sults suggested that the whole combustion duration of both fuels
were shortened at higher injection pressures and the combustion
events of diesel and natural gas were dif ﬁcult to differentiate at
shorter injection intervals. They also found that ignition delay and
maximum heat release rate could be reduced by adding nitrogen,
hydrogen, ethane and propane to natural gas and the combustion
duration was prolonged with the addition of hydrogen, ethane and
propane. Besides, the peak cylinder pressure was reduced and the
maximum heat release rate was increased resulting from the
reduction of compression ratio. Wager and Wallace[15] conducted a
series of experiments to make comparisons between the mixing
rates and combustion characteristics of natural gas jets issuing from
elliptical and round nozzle designs. They stated that the overall
combustion process, including ignition delay and combustion
duration, exhibited little differences between the two nozzle de-
signs, though the peak value of heat release rate and the combustion
efﬁciency were higher with the employment of round nozzles. They
also adopted the optical devices to make combustion image analysis.
The image histograms indicated that more intense ﬂames and an
earlier peak of luminosity could be observed by using elliptical
nozzles. Munshi et al. [16] incorporated both experimental and
computational methods to analyze the effect of partially-premixed
combustion strategy on the engine performance and emission
characteristics. Their experimental results indicated that the opti-
mum engine performance could be obtained with the utilization of
different combustion strategies under different loads and their CFD
modeling results demonstrated that the level of turbulence was a
key factor for ﬂame propagation, which was highly dependent on
the mixing condition in the combustion chamber. Cheenkachorn
et al. [1 7]compared the performance and emission characteristics of
the dual fuel operation with that of the diesel operation. According
to their ﬁndings, the thermal efﬁciency and volumetric efﬁciency of
dual fuel operation were lower than single diesel operation while
the speciﬁc fuel consumption was slightly improved. What's more,
the effects of injector structure were systematically tested by Laforet
[18] with three different injectors, including the baseline one; it was
found
that the new injectors could achieve better fuel economy
under most operating conditions.
In the present study, heat release rate, cyclic variation along
with BSFC (brake speciﬁc fuel consumption) were analyzed to make
a further understanding of the combustion characteristics and
evaluate the effects of four important injection parameters on the
performance of a pilot ignited direct injection natural gas engine.
Systematic experiments were carried out at a constant engine
speed of 1200 rpm with engine torques of 1300 N m and 1 700 N m,
as these are the most commonly used operating conditions for
heavy-duty engines. As mentioned above, most previous studies
focused on heat release analysis of this type of engine are based on
numerical simulation, very limited researches have been done on
the thoroughly exploration of the general performance of this kind
of engine, particularly the combustion cyclic variation.
2. Experimental apparatus and test conditions
2.1. Experimental apparatus
The baseline engine for the experiments was a turbocharged,
intercooled 6-cylinder diesel engine. The speci ﬁcations of the en-
gine are listed in Table 1. The engine was modiﬁed by incorporating
a fuel supply system with integrated pressure regulating module for
adjusting the injection pressure of both fuels and re ﬁtting the en-
gine head in order to equip with concentric needle injectors, in
which the injection timing was controlled by two solenoids sepa-
rately. The engine was coupled to an eddy current dynamometer
(Xiangyi GW630) and instrumented with piezoelectric transducers
(Kistler 6067C) ﬂush mounted to the bottom of cylinder head to
measure the in-cylinder pressure at a resolution of 0.5
/C14 CA (crank
angle). A coriolis mass ﬂowmeter (Emerson CNG050) and a diesel
consumption meter (AVL 733S) were also equipped for natural gas
mass and diesel ﬂow measurements. As shown in the schematic
diagram of the test bed in Fig. 1, natural gas was supplied to the gas
rail after pressurized by the pump and regulated to the appropriate
pressure by the integrated pressure regulating module, where the
pressure of diesel was also adjusted to a value a little higher than
that of natural gas after pressurized by the diesel pump. Intake air
mass ﬂow rate measurements were made before the compressor
with a laminar ﬂowmeter (ToCeiL-LFE400). The pressure and tem-
perature of the intake charge were measured by an intake pressure
sensor (Kistler 4007B) and an intake temperature sensor (Delphi
25036751), both of which were located in the intake manifold. It
should be noted that before the measurements (including in-
cylinder pressure of 100 consecutive cycles) of every single test
condition, the engine was stabilized for at least ﬁve minutes.
2.2. Test conditions
The purpose of this work is to examine systematically the
effects of various injection parameters on the performance and
combustion characteristics of pilot ignited direct injection natural
gas engine. The effect of every parameter was identi ﬁed by
Table 1
Engine speciﬁ cations.
Item Speci ﬁcation
Number of cylinder 6
Engine type Turbocharged, water cooled
Combustion chamber bowl
Bore /C2 stroke/mm 126 /C2 155
Displacement/L 11.6
Compression ratio 17
Rated power/kW 353
Rated speed/r $min/C0 1 2100
Idle speed/r $min/C0 1 600
M. Li et al. / Energy 90 (2015) 1251 e12601252

<!-- PDF_PAGE: 3 -->

conducting separate set of experiments and analyzing the results in
detail.
The intake air temperature and engine speed were kept con-
stant at 298 K and 1200 rpm, while the natural gas injection
duration was adjusted in accordance to operating conditions. In the
evaluation process of every single parameter, other parameters
were ﬁxed to appropriate values. In order to eliminate the impact of
cyclic variations, the net heat release rate of each test condition was
calculated from the averaged in-cylinder pressure of 100 consecu-
tive cycles with the following equation based on the ﬁrst law of
thermodynamics combining the ideal gas law [19]:
dQnet
dq ¼ g
g /C0 1 p dV
dq þ 1
g /C0 1 V dp
dq (1)
g ¼ Cp
CV
(2)
where dQnet =dq is the net heat release rate, q is the crank angle, p is
the in-cylinder pressure, V is the working volume, Cp is the speciﬁc
heat at constant pressure and CV is the speci ﬁc heat at constant
volume. In this paper, the calculation of all combustion parameters
are based on net heat release rate.
In order to investigate the cyclic variation of the combustion
process, the COVs (coef ﬁcients of variation) of MFB0 e10%,
MFB10e90% and IMEP (indicated mean effective pressure) are
calculated from the recorded in-cylinder pressure data of 100
consecutive cycles for each test point. The equation for COV (coef-
ﬁcient of variation) is given as follows:
COV ¼ s
x /C2 100% (3)
s ¼
ﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃPn
i¼1 ðxi /C0 xÞ2
n /C0 1
s
(4)
where s is the standard deviation, x is the averaged value of the
parameter, xi is the value for each cycle, and n is the number of
cycles.
2.3. Uncertainty analysis
The uncertainties of the experimental parameters are affected
by different error sources, namely, the random ﬂuctuation of
employed instruments, the calibration of the test bed, the obser-
vation accuracy and the methodology of the experiments [20].
Thus, before the experiments, all the apparatuses used were cali-
brated under operating conditions in accordance with the test
points. To ensure the reliability of the data measured, pressure data
of 100 consecutive cycles were recorded for each test condition.
And three measurements of other parameters (mass ﬂow rates of
natural gas, diesel and intake air etc.) were also conducted for each
test point. The detailed analysis in this paper is based on the
averaged values of all three measurements for every single test
point. And the maximum COV of each parameter among all the test
points (repeatability uncertainty) is chosen to evaluate the
repeatability of the experiments [21]. For directly measured pa-
rameters, the measurement uncertainties are de ﬁned by the ac-
curacies of the experimental instruments. For computed
parameters, the measurement uncertainties are determined based
on the principle of root-mean square method [22] and the mea-
surement accuracies of the measured parameters:
eR ¼
"/C18 vf
vx1
e1
/C19 2
þ
/C18 vf
vx2
e2
/C19 2
þ / þ
/C18 vf
vxn
en
/C19 2#1
2
(5)
where eR is the measurement uncertainty of the computed
parameter, f is the given function of the computed parameter, e1, e2,
……, en are the measurement uncertainties of the related measured
parameters. The uncertainties of the measured and computed pa-
rameters are shown in Table 2. As shown, the uncertainties of each
parameter are less than 3%, therefore the experiments are of high
precision.
3. Results and discussions
3.1. Effect of injection timing
When examining the effect of injection timing at 1200 rpm, the
engine torque was ﬁxed at 1300 N m with injection pressure of
Fig. 1. The schematic diagram of the test bed.
M. Li et al. / Energy 90 (2015) 1251 e1260 1253

<!-- PDF_PAGE: 4 -->

250 bar, diesel pulse width of 0.3 ms and injection interval of
0.4 ms.
Fig. 2 shows the effect of injection timing on in-cylinder pres-
sure, as shown by the in-cylinder pressure traces, the pressure
during the pure compression process before combustion is lower
with advanced injection timing as a result of the reduced exhaust
energy and corresponding lower boost ratio. And the maximum in-
cylinder pressure is increased and the corresponding crank angle of
occurrence is advanced with the advancement of injection timing
due to the earlier start of combustion and increased heat released
before top dead center.
Fig. 3 represents the effect of injection timing on rate of pressure
rise and second derivation of in-cylinder pressure, which are two
important indications of combustion noise. It can be seen that the
rate of pressure rise at different injection timings features a pro ﬁle
of two peaks, the rate of pressure rise reaches the ﬁrst peak shortly
after the start of combustion, then decrease to a certain extent and
rise rapidly to the maximum value (i.e. the second peak). The ﬁrst
and second peaks of pressure rise rate are attributed to the com-
bustion of pilot diesel and natural gas respectively. And at relatively
retarded injection timing of 4
/C14 BTDC (before top dead center) to
12 /C14 BTDC, the ﬁrst peak is less recognizable compared with that of
more advanced injection timings. This is because ignition delay of
pilot diesel is shorter at retarded injection timings, leading to more
diffusive diesel combustion pattern and slower heat release of pilot
diesel, which, in turn extend the rapid combustion duration of
diesel, thus making the rate of pressure rise during diesel com-
bustion less distinguishable.
It is also displayed in Fig. 3 that the second derivation of in-
cylinder pressure has two positive peaks and one negative peak.
The two positive peaks represent the in ﬂection points of the rising
rate of the pressure rise rate for diesel and natural gas, the rising
rate of the pressure rise rate for diesel witnesses a trend of ﬁrst
increase then decrease, and for natural gas, a similar tendency is
revealed. The negative peak represents the rapid decrease of
pressure rise rate during natural gas combustion, which is more
pronounced at retarded injection timings. As shown, both positive
peaks are generally higher at early injection timings due to the
more premixed combustion of pilot diesel and the promoting effect
of compression process, and the negative peak is more evident at
retarded injection timings as the rapid combustion event is pro-
ceeded late into the expansion stroke when the drop of pressure
and temperature has greater impact on the ﬂame propagation.
Fig. 4 displays the effect of injection timing on heat release rate.
As shown, the heat release rate can be divided into two sections
before reaching the peak value, the ﬁrst section is the contribution
of pilot diesel combustion and the second section is attributed to
the combustion of main fuel natural gas. Due to the trace quantity
of pilot diesel, the proportion of the ﬁrst section is apparently
smaller, and the heat release rate rises markedly at the start of
natural gas combustion since natural gas is the primary fuel. It can
also be seen from the ﬁrst section that the burning rate of pilot
diesel decreases with retarded combustion timing causing by larger
proportion of pilot diesel burnt in mixing-controlled combustion
phase. Meanwhile, the maximum heat release rate is higher at
retarded injection timings. This is mainly because the maximum
Table 2
Uncertainties of measured parameters.
Measured parameter Measurement
uncertainty
Repeatability
uncertainty
(%)
Air ﬂow rate ±0.5% 1.1
Natural gas ﬂow rate ±0.5% 2.4
Diesel ﬂow rate ±0.1% 2.9
Intake air temperature ±1.2 K 1.0
Intake air pressure ±0.01 bar 2.7
Engine speed ±1 rpm 0.4
Engine torque ±0.5% 0.8
Engine power ±0.1% 1.2
BSFC ±2.4% 2.4
Fig. 2. Effect of injection timing on in-cylinder pressure.
Fig. 3. Effect of injection timing on rate of pressure rise and second derivative of in-
cylinder pressure.
M. Li et al. / Energy 90 (2015) 1251 e12601254

<!-- PDF_PAGE: 5 -->

heat release rate occurs during the combustion process of natural
gas and more natural gas is consumed during the premixed com-
bustion phase when the pilot diesel combustion is less intense.
Similar results were obtained in Ref. [23] on a biodiesel/natural gas
dual fuel engine. However, according to Zeng et al. [24], the
maximum heat release rate of spark ignition direct injection natural
gas engine showed an inconsistent trend of ﬁrst increase and then
decrease with the advancement of injection timing. The difference
in ignition pattern may be the main explanation for this.
In this paper, the ignition delay, involving the premixed and
mixing-controlled combustion of pilot diesel as well as the com-
bustion initiation period of natural gas, is deﬁned as the crank angle
between the diesel start of injection and 10% mass fraction of total
fuel burned. As shown in Fig. 5 ,0 e10% MFB0e10% (mass fraction
burned duration) exhibits a decreasing trend over the injection
timing range of 4
/C14 BTDC to 15 /C14 BTDC, while has marginal changes
when injection timing varies from 15 /C14 BTDC to 22 /C14 BTDC. This is
mainly due to the combining effect of the longer diesel combustion
duration at retarded injection timings and the subsequent slower
initiation of natural gas combustion, however, when the injection
timing exceeds 15 /C14 BTDC, the longer pilot ignition delay offsets the
time shortened by the more premixed combustion of pilot diesel.
As also can be seen, MFB50% (phase angle of 50% mass fraction
burned) advances with the advance of injection timing resulting
from the earlier start of combustion. MFB10 e90% (10 e90% mass
fraction burned duration) shows a trend of ﬁrst decrease then in-
crease at the injection timing range from 4 /C14 BTDC to 20 /C14 BTDC,
while reduces slightly when the injection timing continues to
advance. This can be explained by the competing effects of the
more premixed natural gas combustion and slower heat release in
later stages with the retardation of injection timing.
Fig. 6 gives the effect of injection timing on combustion sta-
bility and fuel economy. It is indicated that COV of MFB0 e10%
seems to be independent of injection timing. This is because
MFB0e10% is in ﬂuenced by many other factors including ﬂuc-
tuations of cyclic pilot injection quantity, natural gas injection
quantity and the variations in the diffusion process of natural gas,
all of these appear to be little affected by injection timing. COV of
MFB10e90% shows a generally decreasing trend as a result of the
increased proportion of more stable mixing-controlled combus-
tion of natural gas. COV of IMEP (indicated mean effective pres-
sure) presents a ﬁrst increase and then decrease trend with
advanced injection timing when injection timing is varied from
4
/C14 BTDC to 20 /C14 BTDC, however, when NSOI (start of natural gas
injection) reaches 22 /C14 BTDC, an increase in the COV of IMEP can
be observed. It can be noticed that the changing trend for COV of
IMEP is just opposite to that of MFB10 e90%, indicating that the
shortening of rapid combustion duration has a negative impact
on COV of IMEP. This can be explained by the ﬂame propagation
rate of natural gas combustion, which in ﬂuences the length of
rapid combustion duration directly. When the overall ﬂame
propagation speed of natural gas combustion increases, the
possibility of cyclic irregularity increases accordingly, thus lead-
ing to an increase in COV of IMEP. Moreover, the fuel economy is
signiﬁcantly improved with the advancement of injection timing
in the range of 6
/C14 BTDC to 20 /C14 BTDC owing to the advanced
combustion event, while a slight increase can be observed at
22 /C14 BTDC as a consequence of the remarkably increased power
loss during the compression stroke.
3.2. Effect of injection interval
In order to evaluate the effect of injection interval, the injection
pressure was ﬁxed at 200 bar, the diesel injection pulse width was
kept at 0.3 ms, and the injection timing was remained at 12 /C14 BTDC
with the constant engine torque of 1700 N m, while the injection
interval was varied from 0.3 ms to 0.9 ms.
Fig. 4. Effect of injection timing on heat release rate.
Fig. 5. Effect of injection timing on combustion parameters. Fig. 6. Effect of injection timing on combustion stability and fuel economy.
M. Li et al. / Energy 90 (2015) 1251 e1260 1255

<!-- PDF_PAGE: 6 -->

Fig. 7 presents the effect of injection interval on in-cylinder
pressure. It can be seen from the in-cylinder pressure traces that
earlier detachment from motoring line can be observed at larger
injection interval due to the earlier start of diesel injection, whereas
the maximum in-cylinder pressure decreases and occurs later with
the increase of injection interval. Little divergences of maximum in-
cylinder pressure are exhibited at injection intervals of 0.3 ms,
0.4 ms and 0.5 ms, however, when the injection interval is further
increased to 0.7 ms, the maximum in-cylinder pressure reduces
signiﬁcantly. As also displayed in Fig. 7, the ﬁrst peak values of rate
of pressure rise and D2P (second derivation of in-cylinder pressure)
are higher and the corresponding phase angles are advanced at
larger injection intervals owing to longer pilot ignition delay, while
the maximum values of pressure rise rate and D2P show a converse
trend of decrease with increased injection interval. At injection
intervals of 0.7 ms and 0.9 ms, the appearance of maximum pres-
sure rise rate is obviously delayed, suggesting that the adoption of
overlong injection interval has adverse effect on ignition quality
while is beneﬁ cial to combustion noise.
Fig. 8 illustrates the effect of injection interval on heat release
rate. As demonstrated, the heat release starts earlier and the peak
heat release rate during the combustion process of pilot diesel in-
creases with increasing injection interval. At larger injection in-
tervals, the ignition delay of pilot diesel is extended owing to the
advanced diesel injection, thus leading to larger proportion of
diesel premixed combustion and subsequent more concentrated
combustion of pilot diesel. It is also noted that the maximum heat
release rate during the whole combustion process, which is
attributed to the combustion of natural gas, reduces with increased
injection interval. The heat release rate of natural gas is dependent
on the strength of the ignition ﬂame and the concentration of
surrounding fuel-air mixture. With the extension of injection in-
terval, more pilot diesel is burned before the ignition of natural gas,
hence less contributions from pilot diesel is made to the maximum
heat release rate. What's more, the ignition of natural gas seems to
be delayed at longer injection intervals of 0.7 ms and 0.9 ms due to
the weak ignition of natural gas. In addition, It can be noticed from
the cumulative heat release rate that in the initial stages, cumula-
tive heat release is relatively higher at injection intervals of 0.7 ms
and 0.9 ms as the combustion of pilot diesel is more premixed,
however, in later stages, cumulative heat release of smaller injec-
tion intervals is apparently higher due to the more rapid combus-
tion of main fuel natural gas. McTaggart-Cowan et al. [12] also had
the similar ﬁndings.
Fig. 9 shows the effect of injection interval on combustion pa-
rameters. As demonstrated, MFB0 e10%, MFB50% as well as
MFB10e90% increase with extended injection interval. This implies
that earlier start of pilot fuel injection delays the main combustion
process due to the slower burn rate of natural gas. Besides,
MFB10e90% appears to be more sensitive to injection interval at
smaller injection intervals (0.3 ms e0.5 ms) and less dependent on
injection interval at larger injection intervals.
Fig. 10 illustrates the effect of injection interval on combustion
stability and fuel economy. As can be seen, COV of MFB0 e10%
shows no deﬁnite trend with increased injection interval, while the
peak value appears at the injection interval of 0.3 ms, possibly
because the pilot combustion is more in ﬂuenced by the natural gas
injection and the two fuels may compete for oxygen with each
Fig. 7. Effect of injection interval on in-cylinder pressure parameters.
Fig. 8. Effect of injection interval on heat release rate.
Fig. 9. Effect of injection interval on combustion parameters.
M. Li et al. / Energy 90 (2015) 1251 e12601256

<!-- PDF_PAGE: 7 -->

other when the two injections are too close to each other [25].
Additionally, COVs of MFB10 e90% and IMEP seem to be higher at
larger injection intervals due to the impaired ignition reliability and
fuel economy gets worse with the increasing injection interval due
to deteriorated combustion.
3.3. Effect of diesel injection pulse width
The effect of diesel injection pulse width was investigated at the
injection interval of 0.4 ms, injection timing of 12 /C14 BTDC, and in-
jection pressure of 200 bar under engine load of 1700 N m. The
diesel injection pulse width was varied from 0.25 ms to 0.7 ms with
other parameters held constant.
Fig. 1 1displays the effect of diesel injection pulse width on in-
cylinder pressure parameters. An increase in diesel injection
pulse width (i.e. diesel injection quantity) is accompanied by a
reduction in natural gas injection quantity since the engine torque
was kept constant during the evaluation process. Also, the injection
of pilot diesel is advanced with increased diesel injection pulse
width when the injection interval is a ﬁxed value.
It can be found from Fig. 1 1that the start of diesel combustion is
advanced and the ﬁrst peak values of pressure rise rate and second
derivation of in-cylinder pressure during pilot diesel combustion
process are raised with the increase of diesel injection pulse width
as a consequence of earlier start of diesel injection and increased
pilot diesel quantity. This result is in good agreement with that
available in the study on a pilot ignited premixed natural gas engine
of Sun et al. [26]. Moreover, it can also be observed that the
maximum values of in-cylinder pressure, maximum pressure rise
rate as well as second derivation of in-cylinder pressure reduce
with increasing diesel injection pulse width when diesel injection
pulse width varies from 0.3 ms to 0.7 ms, while increase slightly
when diesel injection pulse width extends from 0.25 ms to 0.3 ms.
This, however, is inconsistent with that reported in an investigation
on conventional dual fuel engine [26], where the natural gas is
premixed before inducted into the cylinder and, consequently, the
mixing quality of natural gas is independent of the ignition delay.
For direct injection natural gas engine studied in the present work,
the formation of combustible mixture is highly dependent on the
ignition process because natural gas is directly injected into the
cylinder, thus, the time available for mixture formation is quite
limited. As the diesel injection pulse width extended from 0.3 ms,
the ignition process is accordingly enhanced, resulting in earlier
start of main fuel combustion and less ﬂammable mixture formed
during the ignition delay of natural gas. Besides, the total amount of
natural gas is reduced with the extension of diesel injection pulse
width, which is also a possible explanation. However, when the
diesel injection pulse width is shortened to 0.25 ms, the ignition
energy cannot be guaranteed since the quantity of pilot diesel is too
little, thereby leading to poorer initial combustion and subsequent
impaired later combustion stages compared to that of 0.3 ms.
Fig. 12 demonstrates the effect of diesel injection pulse width on
heat release rate. As displayed by the curves in the ﬁgure, the peak
value of heat release is signi ﬁcantly higher at smaller diesel injec-
tion pulse widths of 0.25 ms and 0.3 ms. This is possibly due to the
correspondingly larger proportion of natural gas and the increased
combustible mixture formed before natural gas ignition. It can also
be observed from the cumulative heat release rate that the appli-
cation of diesel injection pulse width of 0.3 ms results in the fastest
combustion while little differences in cumulative heat release rate
can be found among the other three diesel injection pulse widths.
The effect of diesel injection pulse width on combustion param-
eters is provided byFig. 13. It is clearly noted that MFB0e10% increases
Fig. 10. Effect of injection interval on combustion stability and fuel economy.
Fig. 1 1. Effect of diesel injection pulse width on in-cylinder pressure parameters. Fig. 12. Effect of diesel injection pulse width on heat release rate.
M. Li et al. / Energy 90 (2015) 1251 e1260 1257

<!-- PDF_PAGE: 8 -->

with the increase of diesel injection pulse width mainly due to the
increased pilot injection duration. MFB10 e90%, however, shows a
consistent increasing trend as a result of slower natural gas com-
bustion rate at longer diesel injection pulse widths. Moreover, the
most advanced MFB50% appears at the diesel injection pulse width of
0.3 ms, any deviation from this point will lead to a retardation.
The effect of diesel injection pulse width on combustion stabil-
ity and fuel economy is illustrated in Fig. 14 .A ss h o w n ,C O V
of MFB0 e10% decreases with the increase of diesel injection pulse
width, suggesting that the cyclic irregularity of mechanical injector
operation may play an important role. Cyclic variations of
MFB10e90% and IMEP , however, seems to be independent of diesel
injection pulse, implying that the ﬂuctuations of the premixed and
diffusive combustion events may be the main in ﬂuencing factors
contributing to the operating stability in pilot ignited direct injection
natural gas engine, rather than the quantity of pilot diesel. BSFC,
however, shows an upward trend with increasing diesel injection
pulse width due to the cooperative effects of retarded combustion
and increased proportion of diesel, which has a lower heating value.
3.4. Effect of injection pressure
As the effect of injection pressure on in-cylinder pressure pa-
rameters shown in Fig. 15, the increase of injection pressure results
Fig. 13. Effect of diesel injection pulse width on combustion parameters.
Fig. 14. Effect of diesel injection pulse width on combustion stability and fuel
economy.
Fig. 15. Effect of injection pressure on in-cylinder pressure parameters.
M. Li et al. / Energy 90 (2015) 1251 e12601258

<!-- PDF_PAGE: 9 -->

in increases in the peak values of in-cylinder pressure, rate of
pressure rise and second derivation of in-cylinder pressure. At
higher injection pressures, the injection rate and penetration of
both fuels are increased, consequently, the mixing of fuels with the
surrounding air is enhanced, which in turn leads to faster com-
bustion and more rapid pressure rise.
Fig. 16shows the effect of injection pressure on heat release rate.
As depicted, the burning rate of pilot diesel is slightly higher at
higher injection pressures owing to the improved atomization and
evaporation process of diesel, meanwhile the combustion of natural
gas is also intensi ﬁed resulting from enhanced turbulence and jet
penetration as well as the subsequent improved mixing process.
Also, at higher injection pressures, the injection pulse width of
natural gas is shorter with faster injection rates, thereby raising the
quantity of premixed mixture and resulting in a less distinctive
transition from premixed combustion phase to mixing-controlled
combustion phase.
As mentioned above, the combustion process is more intensiﬁed
both in the initial stages and later stages, also, ignition delay is
shortened as a result of improved mixing with higher injection
pressures, leading to reductions in MFB0 e10% and MFB10 e90%;
MFB50%, however, happens earlier accordingly ( Fig. 17 ). Similar
trends were also reported by previous studies [27,28] on pilot
ignited gaseous engines, implying that the fuel injection pressure is
a crucial factor for the combustion enhancement of engines with
pilot ignition.
Fig. 18 reveals the effect of injection pressure on combustion
stability and fuel economy. Under both operating conditions, COV of
0e10% tends to be the highest at the highest injection pressure due
to the increased cyclic variation of diesel injection. In terms of
MFB10e90%, the changing tendency is just reversed, the more
erratic diffusion of natural gas induced by lower pressure may be a
reason for this. As the injection pressure increases, COV of IMEP
shows a rising trend ascribed to the combined effects of ignition
irregularity, ﬂow movement ﬂuctuation and variability in the in-
jection process. Furthermore, fuel economy is improved with the
utilization of higher injection pressures on account of the subse-
quent promoted mixing and combustion process.
4. Conclusions
For pilot ignited direct injection natural gas engine, the injection
parameters have direct effects on the combustion process. In this
study, detailed combustion analysis has been done under different
operating conditions, the following conclusions are drawn:
(1) Maximum in-cylinder pressure and maximum rate of pres-
sure rise increase with the advancement of injection timing,
the decrease of injection interval and the increase of injec-
tion pressure, while decrease considerably when diesel in-
jection pulse width is extended from 0.3 ms to 0.7 ms.
(2) Higher maximum heat release rate can be achieved by
retarding injection timing, shortening injection interval,
reducing pilot pulse width or raising injection pressure.
MFB0e10% and MFB10 e90% are extended, MFB50% is
delayed with larger injection interval, longer diesel injection
pulse width and lower injection pressure. Meanwhile,
MFB0e10% decreases slightly, MFB 10e90% shows a trend of
Fig. 16. Effect of injection pressure on heat release rate.
Fig. 17. Effect of injection pressure on combustion parameters.
Fig. 18. Effect of injection pressure on combustion stability and fuel economy.
M. Li et al. / Energy 90 (2015) 1251 e1260 1259

<!-- PDF_PAGE: 10 -->

ﬁrst decrease then increase and MFB50% advances gradually
with advanced injection timing.
(3) Combustion stability is less likely to be associated with in-
jection timing and diesel injection pulse width, however, it
can be improved by the adoption of shorter injection in-
tervals and lower injection pressures.
(4) Improved fuel economy can be gained by advancing the in-
jection timing in the range of 6 /C14 BTDC to 20 /C14 BTDC, applying
smaller diesel injection pulse width and shortened injection
interval as well as increasing the injection pressure.
Acknowledgment
The authors acknowledge ﬁnancial support from the Ministry of
Industry and Information Technology of the People's Republic of
China (2060303) and assistance from Weichai Westport Inc. in
conducting the experiments.
References
[1] Poompipatpong C, Cheenkachorn K. A modi ﬁed diesel engine for natural gas
operation: performance and emission tests. Energy 2011;36:6862 e6. http://
dx.doi.org/10.1016/j.energy.2011.10.009.
[2] Cho HM, He BQ. Spark ignition natural gas engines e a review. Energy Convers
Manag 2007;48:608 e18. http://dx.doi.org/10.1016/j.enconman.2006.05.023.
[3] Korakianitis T, Namasivayam AM, Cr ookeset RJ. Natural-gas fueled spark
ignition (SI) and compression-ignition (CI) engine performance and emis-
sions. Prog Energy Combust Sci 2011;37:89 e112. http://dx.doi.org/10.1016/
j.pecs.2010.04.002 .
[4] Lounici MS, Loubar K, Tarabet L, Balistrou M, Niculescu DC, Tazerout M. To-
wards improvement of natural gas-diesel dual fuel mode: an experimental
investigation on performance and exhaust emission. Energy 2014;64:200 e11.
http://dx.doi.org/10.1016/j.energy.2013.10.091.
[5] Duarte J, Amador G, Garcia J, Fontalvo A, Padilla RV, Sanjuan M, et al. Auto-
ignition control in turbocharged internal combustion engines operating
with gaseous fuels. Energy 2014;71:137 e47. http://dx.doi.org/10.1016/
j.energy.2014.04.040 .
[6] Harrington J, Munshi S, Nedelcu C, Ouellette P, Thompson J, White ﬁeld S.
Direct injection of natural gas in a heavy-duty diesel engine. SAE Technical
Paper. 2002. http://dx.doi.org/10.4271/2002-01-1630. 2002-01-1630.
[7] Douville B. Performance, emissions and combustion characteristics of natural
gas fueling of diesel engines. Master Thesis. Vancouver, Canada: The Univer-
sity of British Columbia; 1994. http://hdl.handle.net/2429/5128.
[8] Hill PG, Douville B. Analysis of combustion in diesel engines fueled by directly
injected natural gas. J Eng Gas Turbines Power 2000;122:141 e9. http://
dx.doi.org/10.1115/1.483185.
[9] Li GW, Lennox T, Goudie D, Dunn M. Modeling HPDI natural gas heavy duty
engine combustion. In: Proceedings of ICEF2005 ASME internal combustion
engine division 2005 fall technical conference; September 11 e14, 2005.
http://dx.doi.org/10.1115/ICEF2005-1307. Ottawa, Canada; ICEF2005-1307.
[10] Lee WG, Montgomery D. Numerical investigation of the performance of a high
pressure injection (HPDI) natural gas engine. In: Proceedings of the ASME
2014 internal combustion engine division fall technical conference ICEF2014;
October 19 e22, 2014. http://dx.doi.org/10.1115/ICEF2014-5681. Columbus,
USA; ICEF2014-5681.
[11] McTaggart-Cowan GP, Mann K, Huang J, Singh A, Patychuk B, Zheng ZX, et al.
Direct injection of natural gas at up to 600 bar in heavy-duty engine. SAE
Technical Paper. 2015. http://dx.doi.org/10.4271/2015-01-0865. 2015-01-0865.
[12] McTaggart-Cowan GP, Bushe WK, Rogak SN, Hill PG, Munshi SR. Injection
parameter effects on a direct injected, pilot ignited, heavy duty natural gas
engine with EGR. SAE Technical Paper. 2003. http://dx.doi.org/10.4271/2003-
01-3089. 2003-01-3089.
[13] McTaggart-Cowan GP, Rogak SN, Munshi SR, Hill PG, Bushe WK. The in ﬂuence
of fuel composition on a heavy-duty, natural-gas direct-injection engine. Fuel
2010;89:752e9. http://dx.doi.org/10.1016/j.fuel.2009.10.007.
[14] McTaggart-Cowan GP, Mann K, Wu N, Munshi S. An ef ﬁcient direct-injection
of natural gas engine for heavy duty vehicles. 2014. http://dx.doi.org/10.4271/
2014-01-1332. SAE Technical Paper 2014-01-1332.
[15] Wager D, Wallace JS. The in ﬂuence
 of elliptical nozzle holes on ignition and
combustion of transient natural gas jets. In: Proceedings of the ASME internal
combustion engine division 2009 spring technical conference ICES2009; May
3e6, 2009. http://dx.doi.org/10.1115/ICES2009-76147. Milwaukee, Wiscon-
sin, USA, ICES2009-76147.
[16] Munshi SR, McTaggart-Cowan GP, Huang J, Hill PG. Development of a
partially-premixed combustion strategy for a low-emission, direct injection
high efﬁciency natural gas engine. In: Proceedings of the ASME 2011 internal
combustion engine division fall technical conference, Morgantown, west
Virginia, USA; October, 2011. http://dx.doi.org/10.1115/ICEF2011-60181.
ICEF2011.
[17] Cheenkachorn K, Poompipatpong C, Ho CG. Performance and emissions of a
heavy-duty diesel engine fuelled with diesel and LNG (liquid natural gas).
Energy 2013;53:52 e7. http://dx.doi.org/10.1016/j.energy.2013.02.027.
[18] Laforet CA. Combustion of natural gas with entrained diesel in a heavy-duty
compression-ignition engine. Master Thesis. Vancouver, Canada: The Uni-
versity of British Columbia; 2009. http://hdl.handle.net/2429/17010.
[19] Rakopoulos CD, Rakopoulos DC, Giakoumis EG, Dimaratos AM. Investigation of
the combustion of neat cottonseed oil or its neat bio-diesel in a HSDI diesel
engine by experimental heat release and statistical analyses. Fuel 2010;89:
3814e26. http://dx.doi.org/10.1016/j.fuel.2010.07.012.
[20] Paul A, Bose PK, Panua RS, Banerjee R. An experimental investigation
of performance-emission trade off of a CI engine fueled by diesel-
compressed natural gas (CNG) combination and diesel-ethanol blends
with CNG enrichment. Energy 2013;55:787 e802. http://dx.doi.org/10.1016/
j.energy.2013.04.002 .
[21] Holman JP. Experimental methods for engineers. 6th ed. New York: McGraw-
Hill; 1994 .
[22] Rahman MM, Hamada KI, Aziz ARA. Characterization of the time-
averaged overall heat transfer in a direct-injection hydrogen-fueled en-
gine. Int J Hydrog Energy 2013;38:4816 e30. http://dx.doi.org/10.1016/
j.ijhydene.2013.01.136 .
[23] Ryu K. Effects of pilot injection timing on the combustion and emissions
characteristics in a diesel engine using biodiesel eCNG dual fuel. Appl Energy
2013;111:721e30. http://dx.doi.org/10.1016/j.apenergy.2013.05.046.
[24] Zeng K, Huang ZH, Liu B, Liu LX, Jiang DM, Ren Y, et al. Combustion charac-
teristics of a direct-injection natural gas engine under various fuel injection
timings. Appl Therm Eng 2006;26(8 e9):806e13. http://dx.doi.org/10.1016/
j.applthermaleng.2005.10.011.
[25] Larson CR. Injection study of a diesel engine fueled with pilot-ignited,
directly-injected natural gas. Master Thesis. Vancouver, Canada: The Univer-
sity of British Columbia; 2003. http://hdl.handle.net/2429/14159.
[26] Sun L, Liu YF, Zeng K, Yang R, Hang ZH. Combustion performance and stability
of a dual-fuel diesel-natural-gas engine. Proc IMechE Part D J Automob Eng
2014;229(2):235e46. http://dx.doi.org/10.1177/0954407014537814.
[27] Liu JH, Yao A, Yao C. Effects of diesel injection pressure on the performance
and emissions of a HD common-rail diesel engine fueled with diesel/
methanol dual fuel. Fuel 2015;140:192 e200. http://dx.doi.org/10.1016/
j.fuel.2014.09.109 .
[28] Yang B, Xi CX, Wei X, Zeng K, Lai MC. Parametric investigation of
natural gas port injection and diesel pilot injection on the combus-
tion and emissions of a turbocharged common rail dual-fuel engine at
low load. Appl Energy 2015;143:130 e7. http://dx.doi.org/10.1016/
j.apenergy.2015.01.037.
M. Li et al. / Energy 90 (2015) 1251 e12601260
