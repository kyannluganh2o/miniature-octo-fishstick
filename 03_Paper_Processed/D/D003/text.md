<!-- PDF_PAGE: 1 -->

International Journal of Multiphase Flow 101 (2018) 64–73 
Contents lists available at ScienceDirect 
International Journal of Multiphase Flow 
journal homepage: www.elsevier.com/locate/ijmulflow 
Potential of a jet-induced shock wave to inﬂuence an upstream 
droplet cloud in compression-ignition engines using multiple injection 
strategies 
Pascal Tétrault ∗, Patrice Seers 
Thermo-Fluid for Transport Laboratory, Département de génie mécanique, École de technologie supérieure, 110 0 rue Notre-Dame Ouest Montréal, QC H3C 
1K3, Canada 
a r t i c l e i n f o 
Article history: 
Received 19 July 2017 
Revised 13 December 2017 
Accepted 2 January 2018 
Available online 3 January 2018 
Keywords: 
Fuel injection 
Diesel spray 
Multiple injections 
Spray penetration 
Shock-wave 
Momentum transfer 
a b s t r a c t 
High-pressure diesel-fuel sprays have been shown to emit shock wave under certain conditions, while 
the advanced injection strategy used in internal-combustion engines involve multiple injections taking 
place within a short time frame. Experimental study of double injection has shown in two instances 
that the ﬁrst fuel-spray cloud could be accelerated before the arrival of the second fuel spray. Herein, 
it is hypothesized that a shock wave emitted from an injection interacts with the fuel-spray cloud of 
a preceding injection and is responsible of a push-away mechanism on the ﬁrst droplet cloud reported 
on in the literature. In this context, the shock waves emitted by fuel-spray jets with a commercial 5- 
hole diesel injector injecting into a pressure vessel were characterized with schlieren visualizations and 
dynamic pressure measurements taken with single- and double-injection strategies. The experimental 
results conﬁrm the shock presence based on schlieren measurements. The measured shock conditions 
show a different shock topology from most shock-tube experiments as the expansion wave closely fol- 
lowed the shock front, resulting in a thin shocked region and a short duration of the droplet exposition to 
the post-shock gas conditions. Experimental measurements were then used as initial conditions in a 1D 
multiphase simulation model allowing simulation of the shock-wave interaction with the droplet cloud 
under engine-related conditions. The model was used to conduct a parametric study on the droplet-cloud 
characteristics and showed that, as the cloud density increased, the shock intensity and droplet-induced 
velocity decreased. Finally, the model was used to illustrate that the push-away interaction mechanism 
could be explained by the shock wave–fuel-droplet-cloud interaction. 
© 2018 Elsevier Ltd. All rights reserved. 
1. Introduction 
Fuel-injection systems in diesel engines have been evolving 
over the years to reduce pollutant emissions and engine noise and 
to increase performance. As the injection pressure is known to re- 
duce the average droplet size in diesel-fuel sprays, resulting in a 
higher evaporation rate ( Hiroyasu et al., 1982 ), the maximum fuel- 
injection pressure has been increasing gradually over the years. 
Today’s commercial injection systems allow a maximum injection 
pressure of 220 MPa, making it possible to optimize the combus- 
tion process under a wide range of operating conditions. Devel- 
opments in injector technology also have yielded shorter injector 
opening and closing, allowing for multiple injection strategies as 
a practical solution to further reduce pollutant emissions and the 
∗ Corresponding author. 
E-mail addresses: Pascal.tetrault.1@ens.etsmtl.ca (P. Tétrault), 
Patrice.seers@etsmtl.ca (P. Seers). 
noise of compression-ignition engines. In a review article on differ- 
ent fuel-injection strategies, Mohan et al. (2013) showed that mul- 
tiple injection strategies may be used to reduce both NOx and par- 
ticulate emissions under speciﬁc conditions, pushing the NOx–soot 
tradeoff limit. Due to the great sensitivity of engine pollutant emis- 
sions to injection parameters, however, multiple injection-strategy 
implementations may result in the opposite result if injection tim- 
ing is not chosen properly, thereby illustrating the importance of 
the mixture formation process and associated fuel spray. 
Few authors have studied the fuel-spray behavior under multi- 
ple injection strategies. One of the ﬁrst studies was conducted with 
mechanical injectors by Arai et al. (1994) , who observed two dif- 
ferent spray growth mechanisms under multiple injections: (1) The 
ﬁrst injection was pushed forward by the second injection before 
the second jet caught up to the ﬁrst spray trailing edge and was la- 
beled a push-away growth pattern; (2) The second spray travelled 
faster and caught up to the ﬁrst injection spray and was labeled 
a catch-up growth pattern. Both observed behaviors dependent on 
https://doi.org/10.1016/j.ijmultiphaseﬂow.2018.01.001 
0301-9322/© 2018 Elsevier Ltd. All rights reserved.

<!-- PDF_PAGE: 2 -->

P. Tétrault, P. Seers / International Journal of Multiphase Flow 101 (2018) 64–73 65 
the time delay and the injected momentum of the injection strat- 
egy. Arai et al. (1994) suggested that catch-up behavior is related 
to the axial ﬂow induced by the ﬁrst injection, which reduces the 
droplet drag of the second fuel jet, while no hypothesis was pro- 
posed for the push-away pattern. 
The push-away behavior was also observed by 
Tetrault et al. (2015) using an electrically controlled common- 
rail fuel-injection system, which gave rise to the hypothesis 
that the shock wave of the second injection interacts with the 
preceding injection’s droplets. The hypothesis was motivated by 
Nakahira et al. (1992) and Wang et al. (2002) observing a shock 
wave forming near the injector tip and the supersonic Bernoulli 
velocity at the injector tip. A comprehensive study of the fuel- 
spray-emitted shock waves was conducted by Pickett et al. (2010) , 
who studied the effect of ambient pressure and temperature for 
conditions up to 950 K and 22.8 kg/m 3 and representative of diesel 
in-cylinder conditions. They reported bow shock-wave formation 
up to 6 kg/m 3 at 800 K for a 150 MPa injection pressure. Ultra-high 
pressure (up to 300 MPa) diesel sprays were also studied recently 
by Jia et al. (2017) , who observed a change in the spray-tip 
morphology with the appearance of a conical fuel-spray tip in the 
presence of conical shocks. 
While the push-away mechanism has been seldom reported in 
the literature, the shock wave–fuel-droplet interaction has been 
studied more extensively in general. For example, for a moderate 
shock-wave Mach number between 1.2 and 1.9, Smolders and Van 
Dongen (1992) did not observe droplet breakup for Weber num- 
bers (We) up to 13. On the other hand, droplet breakup by shock 
interaction was observed experimentally by Kobiera et al. (2009) at 
high We between 21,0 0 0 and 278,0 0 0 with hexane droplets. In 
Chauvin et al., (2016) , the importance of modeling droplet atom- 
ization during shock-droplet interaction was identiﬁed for shock 
traveling at Mach of 1.5, resulting in droplet We above 800 and 
showing that droplets attenuate shock-wave intensity, depending 
on droplet size and droplet production rate. 
The increase in maximum injection pressure since the ex- 
periments conducted by Pickett et al. (2010) and the usage 
of early injections in homogeneous-charge compression-ignition 
(HCCI) strategies, such as in Helmantel and Denbratt (2004) , make 
shock formation in compression-ignition engines plausible un- 
der certain conditions. This behavior in cold spray conditions is 
also of practical usage as nonevaporative conditions are regularly 
used in fuel-spray experiments and simulations. For an example, 
Hori et al. (2006) used nonevaporative experimental results to val- 
idate their CFD model, while nonevaporative experiments have also 
been conducted to isolate fuel evaporation from the parameters of 
interest in Han et al. (2002) and Hillamo et al. (2008) . 
The observation of the coupling behavior between successive 
injections led to the study of shocks emitted by fuel sprays as a 
potential driving mechanism. The main objective of this paper is to 
study and characterize the emitted shocks from short-duration in- 
jections and the interaction of the shock fuel spray under a double- 
injection strategy. This latter objective has been motivated by the 
increased usage of multiple shorter injections instead of a single 
long injection in diesel engines and to propose a physical expla- 
nation of the push-away pattern reported by Arai et al. (1994) . To 
reach this objective, experiments were ﬁrst conducted to assess the 
inﬂuence of the injection duration and double-injection strategy on 
shock characteristics. Based on these experimental results, a model 
was developed to conduct a parametric study of the shock wave–
droplet-cloud interaction so as to quantify the push-away mecha- 
nism. Finally, the model was used to simulate the experimental re- 
sults when a shock wave–fuel-spray-droplet cloud interaction has 
been reported in the literature, illustrating the plausible mecha- 
nism of the push-away behavior. 
Fig. 1. Spray-visualization-chamber schematic (top) and dynamic pressure-sensor 
position (bottom). 
2. Experimental description 
Experiments were conducted with a pressurized vessel ﬁlled 
with nitrogen. This vessel is equipped with 6 customizable and 
interchangeable caps allowing different measurement setups. The 
chamber can be pressurized up to 50 bars at room temperature 
and has 7.6 cm optical accesses. Fig. 1 (top) provides a schematic 
of the fuel-injection system and pressure vessel. During the exper- 
iments, a constant injection-pressure differential of 1600 bar was 
used while varying the backpressure. This pressure differential cor- 
responds to a theoretical jet Mach number of 1.8 based on the 
Bernoulli relation for fuel jet. The injection duration was varied be- 
tween 200 μs and 2000 μs to study its inﬂuence on the shock char- 
acteristics with the 200 μs lower limit representative of the short- 
est injection duration possible with this injector without injection 
misﬁre. The 20 0 0 μs limit was used to represent a quasi-steady 
fuel jet. The temperature was held constant at room temperature 
during the experiments, leading to nonevaporative conditions. The 
experimental conditions studied by schlieren visualization and dy- 
namic pressure measurements are summarized in Table 1 , which 
also deﬁnes double injection strategies evaluated based on electric 
command durations (elec. duration) and time interval between in- 
jections. 
Conventional #2 diesel fuel fed a common-rail system with 
three out of four outlets plugged. The injector installed on the 
common-rail is a ﬁve-hole (120 μm oriﬁces) Delphi solenoid- 
actuated indirect diesel-fuel injector. The fuel-injection system 
was pressurized with a Haskel DSHF-300 pneumatic high-pressure 
pump. The injector feeding pipe was equipped with a Kistler

<!-- PDF_PAGE: 3 -->

66 P. Tétrault, P. Seers / International Journal of Multiphase Flow 101 (2018) 64–73 
Table 1 
Experimental conditions. 
Parameter Range 
Dynamic 
pressure 
measurements 
Schlieren 
visualization 
Ambient pressure 1–30 bar 1 bar 
Ambient density 1,2–35 kg/m 3 1,2 kg/m 3 
Ambient temperature 298 K 298 K 
Injection pressure 1600 bar 1600 bar 
Injection duration (single 
injection) 
20 0–60 0 0 μs 20 0–20 0 0 μs 
Injection strategies 
(double injection) 
1st inj. elec duration / interval 
/ 2nd inj. elec. 
duration 
20 0/625/50 0 μs 20 0/625/50 0 
250/625/500 
250/313/390 
250/625/390 
250/1250/390 
250/10 0 0/50 0 
Table 2 
Simulation parameter ranges. 
Parameter Range Unit 
Cloud properties Cloud density 0.003–24 kg/m 3 
Cloud thickness 1.5–4.5 mm 
Droplet diameter 0.05–50 μm 
Gas phase Gas pressure 1–40 bar 
Gas density 1.18–48.14 kg/m 3 
Gas temperature 293–800 K 
Shock amplitude 1.001–1.25 
Shock thickness 10–20 mm 
4067C20 0 0 dynamic pressure sensor calibrated in both pressure 
and temperature, allowing high-frequency pressure measurements 
directly at the injector inlet. 
Both the injector command and the pressure-sensor data were 
acquired using a National Instruments (NI) CompactRIO 9074 con- 
troller. The controller was equipped with an NI-9751 direct-injector 
driver module, an NI-9222 voltage-input module, and an NI-9401 
TTL input/output module. All modules shared the same 40 MHz 
clock, allowing precise synchronization between injector com- 
mand, pressure-data acquisition, and camera synchronization. All 
analog channels were simultaneously recorded at a rate of 250 kHz 
during 8 ms following the electrical command to the injector, 
which deﬁnes the start of injection (SOI) herein. It should be noted, 
however, that the SOI doesn’t correspond to the actual fuel injec- 
tion due to injection opening delay. It is associated with the be- 
ginning of the injection sequence and, as such, is used as an initial 
reference. Dynamic pressure measurements of shock timing and 
amplitude from the SOI were recorded at 250,0 0 0 samples per sec- 
ond using a Kistler 6052b piezoresistive pressure sensor (linearity 
of ±0.2% on a 50 bar calibration) installed in the pressure cham- 
ber near the injector tip. The sensor position was determined using 
schlieren results to ensure fully formed shocks at the sensor loca- 
tion located 30 mm from the injector tip as shown in Fig. 1 (bot- 
tom). 
2.1. Schlieren visualization 
Z-type schlieren imaging was used with a 1 mm slit and a 
150 W halogen light source (Dolan-Jenner model 180) at the ﬁrst 
mirror’s focal length. A straight knife edge was installed parallel 
to the slit at the second mirror’s focal length. The incidence an- 
gle of the source and knife edge to the mirrors axis was kept at 
about 10 ° to limit astigmatism. The injection system was installed 
halfway between the spherical mirrors. Fig. 2 provides a schematic 
of this setup. 
Fig. 2. Schlieren experiment diagram. 
Images were recorded with a Vision Research Phantom V9.1 
camera equipped with a 50 mm focal-length lens with an aper- 
ture size of f/1.4. Images were recorded at 60,606 frames per sec- 
ond, limiting the spatial resolution to 288 × 48 pixels. An exposure 
duration of 4 μs was used to minimize motion blur, while allow- 
ing enough light intensity. A resolution of 250 μm per pixel was 
thus obtained with this experimental setup. For this speciﬁc spatial 
and temporal resolution, a ±1 pixel shock-position incertitude on 
two consecutive frames corresponded to an approximated ±30 m/s 
incertitude on the wave velocity. The measurement duration was 
limited to the time needed for the shock to exit the measurement 
domain. Image post-treatment involved using normalization binary 
threshold set at 14% while contrast and luminosity adjustements 
were achieved using imcontrast and imadjust functions from Mat- 
lab (Mathworks.com, 2017a), (Mathworks.com, 2017b). 
The schlieren visualization experiment was used to collect the 
apparent shock-formation position from the injector tip and to es- 
timate the propagation speed of the shock waves. Schlieren mea- 
surements were conducted at atmospheric conditions as increased 
air density due to higher pressure is known to decrease the shock- 
formation distance from the injector tip and has no apparent im- 
pact to the shock velocity ( Pickett et al., 2010 ). 
2.2. Experimental results 
2.2.1. Schlieren visualization 
Measurements at 160 MPa of injection pressure and ambient 
backpressure for single and double injections, the latter presented 
in Fig. 3 , revealed bow shock characteristics when using a single 
injection duration between 200 μs and 20 0 0 μs with the multi- 
oriﬁce injector herein. These results are consistent with results 
from Jia et al. (2017) , who observed bow shocks for injection pres- 
sures of 150 MPa that transitioned to stronger oblique shocks when 
the fuel injections increased to 300 MPa. 
Under the injection conditions studied, the shock appearance 
was observed at a distance slightly less than 30 mm from the in- 
jector tip which can be seen in Fig. 3 a. Images of the ﬁrst injec- 
tion of a double injection sequence is presented in the left col- 
umn of Fig. 3 in which each row is separated by a time step of 
1.65 ×10 −5 s. Shock formation can be observed at the 8th frame 
from the SOI of the ﬁrst injection (SOI1) ( Fig. 3 d) and is located 
approximately 30 mm in front of the injector at frame 9, corre- 
sponding to 148 μs after SOI1. Shock propagation speed was ap- 
proximated as sonic for all measurements, and the separation of 
the shock from the spray tip ( Fig. 3 e) was linked to the decrease 
in spray tip velocity over time due to ambient air. Moreover, as 
can be seen in Fig. 3 f (left) in the 11th–13th frames, a series of 
secondary waves were emitted following the principal shock. 
Fig. 3 (right column) shows images of the second fuel spray of 
a double-injection strategy with a 600 μs delay between the ﬁrst 
and second injections with the SOI of the second injection (SOI2) 
( Fig. 3 g). The shock wave emitted by the second fuel spray is barely 
discernable in the 11th–13th frames ( Fig. 3 h) due, in part, to the 
droplet cloud obstructing visibility (visualization technique limita- 
tion) or the presence of a weaker shock or of shock attenuation as

<!-- PDF_PAGE: 4 -->

P. Tétrault, P. Seers / International Journal of Multiphase Flow 101 (2018) 64–73 67 
Fig. 3. Schlieren sequence of a double-injection strategy with the ﬁrst injection (left 
column) and second injection (right column). 
Fig. 4. Shock position and fuel-spray tip penetration as a function of time for three 
250 μs injection events. 
it goes through the ﬁrst injection-droplet cloud. This latter point 
will be further analyzed in the section pertaining to dynamic pres- 
sure measurements. Nevertheless, the shock position and timing 
from the SOI2 were similar to results obtained from the SOI under 
single injection, before interaction between the shock and the ﬁrst 
injection droplets. At the sensor position, 30 mm from the injector 
( Fig. 3 b), the shock was still attached to the spray tip. It is also ob- 
served on Fig. 3 that once the shock detaches from the spray tip 
at 30 mm from the nozzle, the distance between the spray tip and 
the shock increases over time as the spray velocity decreases. 
From the high-speed schlieren imaging, shock position and fuel- 
spray tip penetration over time for the ﬁrst injection were deter- 
mined as presented in Fig. 4 for three different injection events. It 
is observed that the bow shock and the spray tip followed an ap- 
proximately linear propagation speed as the injector was open and 
provided fuel-spray momentum. From these sequences, the shock 
propagation velocity was estimated at 350 ±30 m/s, correspond- 
ing approximately to the speed of sound calculated at 344 m/s at 
room temperature using an ideal gas assumption. To conﬁrm the 
schlieren shock wave observations, fuel velocity at the nozzle exit 
was estimated based on Bernoulli equation, resulting in a fuel ve- 
locity of 600 m/s for the pressure conditions considered herein. 
Fig. 5. Dynamic pressure measurements 30 mm from the injector oriﬁce for injec- 
tion durations of 200 μs (top), 500 μs (middle), and 20 0 0 μs (bottom) using a /Delta1P 
of 1600 bar for 1 bar absolute backpressure. 
This fuel nozzle velocity was deem more suitable to predict shock 
wave presence by Huang et al. (2015) than fuel spray tip velocity. 
Moreover, the sound pressure level (SPL) has been computed us- 
ing the pressure transducer measurement and a value above 148 
(as in Fig. 5 , for example) has been obtained while SPL above 135 
can be considered discrete shock wave ( Hargather et al., (2010) ). 
Together, those results conﬁrm the presence of shock observed by 
the schlieren measurement technique. 
Finally, Fig. 4 also show that the distance between the shock 
and the spray tip increases over time. This growing distance can 
be converted to a time delay by dividing by the spray tip veloc- 
ity. The time delay between the shock and the fuel jet passage 
has been estimated at 115 μs at 40 mm from the injector noz- 
zle, slightly upstream from the pressure sensor. This time delay is 
used to estimate the shock potential in inﬂuencing droplets of the 
ﬁrst spray prior to the second fuel-spray arrival as the role of the 
emitted shock wave will be indiscernible once fuel-spray interac- 
tion occurred. This delay grew along the axial position as the spray 
penetration rate decreased over time, while the shock velocity was 
nearly constant at the sound velocity. For double injections, this 
velocity difference between the second spray and its shock trans- 
lated in a greater interaction potential if the ﬁrst fuel spray was 
further from the nozzle. This effect was, however, inhibited by a 
thicker droplet cloud dissipating the shock. The effect of the cloud 
thickness on the shock amplitude at the tip of the preceding cloud 
and the resulting induced cloud velocity will be discussed with 
simulations later in this paper. 
2.2.2. Dynamic pressure measurements 
Average dynamic pressure trace recordings of 25 single injec- 
tion events using a /Delta1P of 1600 bar are presented in Fig. 5 to 
illustrate the shock passage from SOI for three injection dura- 
tions of 200 μs (top), 500 μs (middle), and 2000 μs (bottom). The 
ﬁrst two injection durations were chosen as they are similar in 
duration to an optimized double-injection strategy presented in 
Plamondon (2015) with a low-duty diesel engine equipped with 
the same injector model. Based on the dynamic pressure sensor, 
shock amplitude was observed to be independent of injection du- 
ration for injection durations above 500 μs (up to 6 ms has been

<!-- PDF_PAGE: 5 -->

68 P. Tétrault, P. Seers / International Journal of Multiphase Flow 101 (2018) 64–73 
Fig. 6. Shock amplitude as a function of injection duration. 
tested but not reported herein) under atmospheric conditions and 
higher environmental pressure. 
In Fig. 5 , the dotted vertical lines represent the end of the 
electrical signal of injection (EOI), while the dashed vertical lines 
correspond to the shock-wave maximum pressure. As shown, the 
maximum wave amplitude was at 700 μs after the SOI and was in- 
dependent of the injection duration. This result is consistent with 
schlieren visualization as shock-wave timing has been observed to 
be independent of injection command duration. The pressure oscil- 
lations following the ﬁrst pressure wave during the injection pro- 
cess are consistent with the complex secondary-wave structure ob- 
served during schlieren visualization. 
In Fig. 5 , the 500 and 2000 μs injection duration showed the 
same pressure wave amplitude, while the 200 μs wave was weaker 
by about half. This dependence of the shock amplitude before 
a certain injection duration threshold can be explained by the 
electrical-command duration being shorter than the time needed 
for this injector to reach its steady-state mass ﬂow rate as ex- 
perimentally shown by Payri et al. (2004) for a similar injector 
topology. The shock amplitude being weakly inﬂuenced by the 
injection duration suggests that the shock amplitude was likely 
a weak function of the injection strategy under multiple injec- 
tion strategies made with short injections. This behavior was con- 
ﬁrmed at higher backpressures, as shown in Fig. 6 , which shows 
the shock-pressure amplitude as being a function of ambient den- 
sity for different injection durations. The measured shock ampli- 
tude for the shortest injection of 200 μs was approximately half 
the recorded value of the long-injection case. This difference de- 
creased at higher ambient densities. Injections longer or equal to 
500 μs reveal shock amplitude as independent of injection dura- 
tion. Results taken from Nakahira et al. (1992) have also been in- 
cluded in Fig. 6 on a second vertical axis on the right. The results 
from Nakahira et al. (1992) were obtained with similar injection 
conditions with a single oriﬁce injector instead of a multihole one. 
Comparing the results from both studies shows similar trends on 
the impact of ambient density on the measured shock pressure, 
but also reveals signiﬁcantly weaker shocks for the multihole in- 
jector. This difference between the single hole injector reported in 
Nakahira et al. (1992) and the results from this study might be 
attributable to a slower axial exit velocity from the multihole in- 
jector during the early stage of the injection process as exposed 
experimentally by Moon et al. (2015) . The shock amplitude rel- 
ative to the backpressure (P shock /P amb ) makes it possible to esti- 
mate post-shock conditions with Rankine-Hugoniot relations, such 
as shock-wave velocity with Eq. (1) from Anderson (2004) . Overall, 
P shock /P amb decreased with increasing ambient density. 
M shock = 
√ 
γ − 1 
2 γ
( P shock 
P b 
− 1 
)
+ 1 . (1) 
Eq. (1) was used to estimate the travelling-shock Mach num- 
ber based on the data in Fig. 6 , providing a range of shock veloc- 
ity from M = 1.0 0 05 to M = 1.1 (343–377 m/s at ambient tempera- 
ture) for multihole and single-hole injectors, respectively. With in- 
creasing ambient density, a slight decrease of the shock travelling 
speed was observed. This behavior had already been reported by 
Pickett et al. (2010) , who observed that the ambient density in- 
hibited shock formation observed as attached oblique shocks at 
low gas density (below or equal to 2.55 kg/m 3 ) transitioning to 
weaker detached bow shocks with an increasing ambient density 
(above 11.7 kg/m 3 ). A similar analysis was conducted using dy- 
namic pressure measurements with double-injection strategies to 
verify their inﬂuence on shock amplitude. The results, not shown 
for brevity, presented wave amplitudes and shock velocities simi- 
lar to the single-injection event for both the ﬁrst and second in- 
jections of double-injection strategies, indicating that shock-wave 
formation occurred independently of injection strategy as long as 
the injection pressure was high enough to sustain shock formation. 
2.3. Numerical model 
We used a simpliﬁed physical 1D transient model to validate 
the hypothesis set forth in the introduction in order to verify 
the potential of a shock wave to generate a push-forward mech- 
anism for an upstream droplet cloud. The simpliﬁed model allows 
for studying the emitted shock wave of the second injection and 
the ensuing fuel droplet cloud–shock-wave interaction. The sim- 
ulations used a 1D ﬁnite volume scheme based on the work of 
Jourdan (2010) and Saurel and Daniel (1994) as well as the nu- 
merical code of Toro (1999) to model shock-spray interaction with 
an upstream cloud along the spray axis. The simulated approach 
is of practical interest as it makes it possible to isolate the shock 
from the second injection and to study its inﬂuence separately. A 
short description of the model, written in MATLAB, is thus pre- 
sented, although the reader is invited to consult references Jourdan 
(2010), Saurel and Daniel (1994) and Toro (1999) for more details. 
The numerical model is based on the diluted multiphase problem 
as encountered in the gas-droplet mixture and is represented by 
the general Eq. (2) : 
∂CS 
∂t 
+ di v 
(⃗ F 
)
= H ( U ) (2) 
where CS is represented by Eq. (3) , in which the ﬁrst 3 terms 
correspond to the gas phase’s density ( ρg ), momentum ( ρg 
−→  u g ), 
and energy ( ρg ϵg ), while the remaining 4 terms are, respectively, 
the droplet cloud phase density ( ρd ), momentum ( ρd 
−→  u d ), energy 
( ρd ϵd ), and the number of droplets within the cloud ( n d ): 
CS = 
⎡ 
⎢ 
⎢ 
⎢ 
⎢ 
⎢ 
⎢ 
⎢ 
⎢ 
⎢ 
⎢ 
⎣ 
ρg 
ρg 
−→  u g 
ρg ϵg 
ρd 
ρd 
−→  u d 
ρd ϵd 
n d 
⎤ 
⎥ 
⎥ 
⎥ 
⎥ 
⎥ 
⎥ 
⎥ 
⎥ 
⎥ 
⎥ 
⎦ 
(3) 
The matrix ⃗ F represents ﬂux terms expressed as per Eq. (4) , in 
which P and PI are source terms and −→  u d is the velocity vector as- 
sociated with the droplet cloud:

<!-- PDF_PAGE: 6 -->

P. Tétrault, P. Seers / International Journal of Multiphase Flow 101 (2018) 64–73 69 
⃗ F = 
⎡ 
⎢ 
⎢ 
⎢ 
⎢ 
⎢ 
⎢ 
⎢ 
⎢ 
⎢ 
⎢ 
⎢ 
⎣ 
ρg 
−→  u g 
ρg 
−→  u g 
−→  u g + P I 
ρg 
−→  u g ϵg + P 
ρd 
−→  u d 
ρd 
−→  u d 
−→  u d 
ρd 
−→  u d ϵd 
n d 
−→  u d 
⎤ 
⎥ 
⎥ 
⎥ 
⎥ 
⎥ 
⎥ 
⎥ 
⎥ 
⎥ 
⎥ 
⎥ 
⎦ 
(4) 
Finally, the source terms of Eq. (2) are given by Eq. (5) : 
H = 
⎡ 
⎢ 
⎢ 
⎢ 
⎢ 
⎢ 
⎢ 
⎢ 
⎢ 
⎣ 
0 
−−−→  
− F drag 
− Q g− d −−−→  
F drag 
·−→  u d 
0 
−−→  
F drag 
Q g− d + −−→  
F drag 
·−→  u d 
˙ n d 
⎤ 
⎥ 
⎥ 
⎥ 
⎥ 
⎥ 
⎥ 
⎥ 
⎥ 
⎦ 
(5) 
In this multiphase formulation, the interaction between the gas 
and the liquid phase is accounted for by the source terms 
−−→  
F drag and 
Q g− d from Eq. (5) . 
−−→  
F drag is used to model the aerodynamic drag of 
the droplet cloud, while a heat transfer model Q g− d is used to esti- 
mate the heat transfer between phases. Droplet breakup rate ( ˙ n d ) 
is neglected and thus set to 0. 
The number of droplets is calculated from the droplet diameter 
( φ), ρd and the fuel density ( ρ∗) as expressed by Eq. (6) , which is 
used to convert properties like drag and heat transfer, computed 
on individual droplets, to ﬂux terms applied to the droplet cloud 
within the cell: 
n d = 
6 ρd 
φ3 πρ∗ (6) 
The split-scheme approach allows for approximating the solu- 
tion of Eq. (2) in two steps. First, the homogeneous part of the 
problem obtained by equating the right-hand side of Eq. (2) to zero 
is solved using the MUSCL scheme with a central difference ap- 
proximation. The resultant equation is split into two subsystems to 
independently solve the PDE problem associated with each phase. 
Terms 1 to 3 of the conserved variable, ﬂux vector, and source 
term expressed in Eqs. (3) –(5) are associated to the gas phase 
while terms 4 to 7 are associated to the droplet cloud. Different 
Riemann solvers are used for the gas and liquid solution to account 
for the different possible wave conﬁgurations of the ideal gas and 
dilute phase. The gas MUSCL scheme uses a MINMOD slope limiter 
( Toro, 1999 ) with an iterative exact three-wave Riemann solver for 
an ideal gas as in ( Toro, 1999 ). The liquid-phase MUSCL scheme 
in Saurel and Daniel (1994) and Toro (1999) with a central dif- 
ference approximation also uses a MINMOD slope limiter, while a 
Van Leer slope limiter has also been tested for both phases and 
gave similar results not shown in this paper. An uniform grid of 
10 0 0 cells is used for both the 3,73 m shock tube validation do- 
main and the 300 mm 1D spray simulation domain. A grid depen- 
dence study was conducted and the chosen grid has shown to be a 
compromise between accuracy and calculation time. Variable time 
step has been used while ensuring a maximum CFL number of 0.7. 
The Riemann problem for the liquid phase is based on a two- 
wave Riemann Problem with 6 different wave conﬁgurations ex- 
pressed in Eq. (7) with associated descriptions in Eqs. (8) –(11) . In 
these equations, UR and UL refer to the right (R) and left (L) con- 
served quantity such as the wave characteristics of a two wave Rie- 
mann problem as described in Saurel and Daniel (1994) . Cases A, B 
and C correspond to a cloud expansion where the local cloud den- 
sity is decreasing (UR > UL) while cases D, E and F correspond to 
a cloud compression. Cases A, B and E also correspond to a right 
moving cloud while cases C, D and F correspond to a left mov- 
ing cloud. A stationary cloud is computationally deﬁned as a right 
moving case with zero velocity Saurel and Daniel (1994) ). The Rie- 
mann similarity solutions along x/t = 0 are calculated using Eqs. 
(8 )–( (11) based on the different wave conﬁgurations ( Eq. (7) ): 
case A if UR > UL and UL > 0 
case B if UR > UL and UL < 0 and UR > 0 
case C if UR > UL and UL < 0 and UR < 0 
case D if UL > UR and UR > 0 
case E if UL > UR and UR < 0 and UL > 0 
case F if UL > UR and UL < 0 and UR < 0 (7) 
Density: 
ρ
( x 
t 
= 0 
)
= 
⎧ 
⎪ ⎪ ⎪ ⎪ ⎨ 
⎪ ⎪ ⎪ ⎪ ⎩ 
ρL if case A 
0 if case B 
ρR if case C 
ρL f case D 
ρL + ρR if case E 
ρR if case F 
(8) 
Velocity: 
U 
( x 
t 
= 0 
)
= 
⎧ 
⎪ ⎪ ⎪ ⎪ ⎨ 
⎪ ⎪ ⎪ ⎪ ⎩ 
U L if case A 
0 if case B 
U R if case C 
U L if case D 
( ρL U L + ρR U R ) 
ρL + ρR if case E 
U R if case F 
(9) 
Number of droplets 
n d 
( x 
t 
= 0 
)
= 
⎧ 
⎪ ⎪ ⎪ ⎪ ⎨ 
⎪ ⎪ ⎪ ⎪ ⎩ 
n d L if case A 
0 if case B 
n d R if case C 
n d L if case D 
( ρL n d L + ρR n d R ) 
ρL + ρR if case E 
n d R if case F 
(10) 
Energy 
ϵ
( x 
t 
= 0 
)
= 
⎧ 
⎪ ⎪ ⎪ ⎪ ⎨ 
⎪ ⎪ ⎪ ⎪ ⎩ 
ϵL if case A 
0 if case B 
ϵR if case C 
ϵL if case D 
( ρL ϵL + ρR ϵR ) 
ρL + ρR if case E 
ϵR if case F 
(11) 
Source terms (H(U)) are then accounted for by solving Eq. (12) , 
which requires droplet drag, heat transfer, and droplet breakup 
models. Eq. (12) is solved using the ODE45 solver based on the 
Dormand-Prince method from the MATLAB environment (Math- 
works.com, 2017c). 
dCS 
dt 
= H ( U ) (12) 
The droplet drag model is based on the drag coeﬃcient of 
an average droplet having a diameter corresponding to the cloud 
Sauter mean diameter (SMD). The drag coeﬃcient was calculated 
using an empiric model described in Jourdan (2007) obtained by 
measuring the droplet drag of individual droplets in a shock tube. 
Herein, the drag model is averaged over the shock passage dura- 
tion and takes into account droplet size and relative velocity to 
the gas phase. One possible limitation of this model is the un- 
derstatement of the droplet drag peak when the pressure front 
is at the droplet’s equator for thin shocked regions ( Sun et al., 
2005 ). Because the droplet cloud was exposed to the shock for ap- 
proximately 0.0 0 01 s, corresponding to approximately 10 0 0 droplet

<!-- PDF_PAGE: 7 -->

70 P. Tétrault, P. Seers / International Journal of Multiphase Flow 101 (2018) 64–73 
Fig. 7. Vertical Shock Tube Experiment (shown horizontally). 
characteristic physical times ( τd ) expressed by Eq. (13) ( Sun et al., 
2005 ) and because the pressure drag is considered stabilized to 
its steady-state value after a τp of approximately 5, the model 
thus neglects the higher initial pressure drag, while the shock front 
crosses the droplet by using an averaged drag coeﬃcient formula- 
tion. 
τd = 
r d √ 
R T 0 
(13) 
The heat-transfer model uses Newton’s law of cooling and 
is based on the droplet temperature, size, and relative velocity, 
while the convective coeﬃcient is computed from an empirical 
model presented in Ranz and Marshall (1952) . Droplet breakup and 
droplet coalescence are both neglected due to the weak shock na- 
ture encountered herein as droplet breakup has been shown to be 
negligible on the gas phase topology by Chauvin et al. (2016) for 
such cases. To conﬁrm this latter hypothesis, droplet We and Oh 
were computed over the simulation duration and showed that the 
We was maximum immediately after the shock passage and below 
the critical We of 12 reported in Pilch and Erdman (1987) . Further- 
more, diesel fuel-spray droplets are much smaller than values used 
in the shock-droplet experiment such as in Kobiera et al. (2009) for 
example, who reported maximum We of 14 for 50 μm droplets 
with a Mach 1.1 shock wave, thus conﬁrming our preliminary cal- 
culation and hypothesis. Finally, numerical results from Yeom and 
Chang (2012) indicated that a droplet breakup model is necessary 
for droplets larger than or equal to 100 μm to properly predict ﬂow 
disturbance by droplet presence. 
To ensure proper modeling of the problem, the model was ﬁrst 
validated against experimental data from Jourdan (2010) obtained 
from shock-tube measurements of a shock wave crossing a cloud 
of droplets. A schematic of Jordan (2010) ’s experiment is shown 
on Fig. 7 . The shock tube is arranged vertically and a droplet in- 
jector is installed on top of the driven section. The shock propa- 
gates upward from the driver section to the injector plate by pass- 
ing through the droplet cloud. The shock is then reﬂected at the 
injector plate, causing the reﬂection to pass through the droplet 
cloud in the reverse direction. 
Conditions in this study differed slightly from fuel-injection 
conditions, as shocked state duration, domain length, and droplet 
diameter were on a larger scale in the shock tub problem. Fig. 8 
presents experimental data from Jourdan (2010) against simula- 
tion results from our study using boundary and initial condi- 
tions simulating the reported experimental conditions. Fig. 8 shows 
the pressure history of a dynamic-pressure sensor placed before 
the droplet cloud 1770 mm from the shock tube’s driver end (P8 
on Fig. 7 ) and two pressure sensors within the droplet cloud at 
2970 mm (P6 on Fig. 7 ) and 3410 mm (P3 on Fig. 7 ). A ﬁrst pressure 
jump observed at t = 0 up to approximately 6 ms corresponds to 
the shock wave and expansion wave generated by the shock tube 
before reaching the droplet cloud. A ﬁrst shock reﬂection from the 
cloud interface is observed as a pressure rise at approximately 9 ms 
before the reﬂection from the tube end reaches the sensor at ap- 
proximately 11 ms. Comparison of the simulation and experimental 
results shows a good concordance in trends with disparities similar 
to the that reported in Jourdan (2010) ; as such, the model’s sim- 
pliﬁed physical representation and accuracy is considered suﬃcient 
to capture the shock wave–droplet-cloud interaction potential. The 
Fig. 8. Validation against shock-tube data (adapted from Jourdan (2010) ). 
observed overestimation of the reﬂected shock might be due to 
physical mechanisms not considered in the current model such as 
viscous effects within the gas phase and water evaporation that 
might dissipate the shock wave. However, droplet breakup was in- 
vestigated by Jourdan (2010) and found to have a negligible impact 
on the shock at low Mach number as discussed herein. 
3. Simulation conditions 
3.1. Equivalent shock-tube problem for 1D simulation initial 
conditions 
The above experimental measurements were used to initialize 
the 1D transient model described in the ﬁrst section of this paper, 
model the post-shock velocity and density, and study the shock 
wave–fuel-droplet cloud interaction for a double-injection strategy. 
In the model, the driven section is initialized with the experimen- 
tal ambient density, pressure, and droplet cloud properties, if nec- 
essary, while in the driver-section pressure and density are ad- 
justed to obtain a moving shock corresponding to the shock am- 
plitude measured experimentally. Moreover, the driver length has 
been adjusted to obtain a shock thickness, deﬁned as the distance 
between the start of the shock (behind the shock front) to the re- 
turn to ambient conditions behind the decompression wave that 
was qualitatively similar to the schlieren images and pressure-trace 
history reported above. 
3.1.1. Boundary and initial conditions 
The left boundary was modeled at the injector’s nozzle tip and 
the right boundary was far enough to avoid the droplet cloud 
reaching it at its location 30 cm from the nozzle. Fully transmissive 
boundary conditions were deﬁned at both boundaries by adding 
two nodes outside the domain, thus preventing shocks bouncing 
back and reducing the analysis to the shock-droplet cloud interac- 
tion. Fig. 9 shows the initial conditions inside the domain in which 
the droplet cloud is uniform with a density equal to αand a mean 
droplet diameter equal to the SMD. Moreover, Fig. 9 -top illustrates 
the ﬁrst and second fuel spray separated by a shock wave while

<!-- PDF_PAGE: 8 -->

P. Tétrault, P. Seers / International Journal of Multiphase Flow 101 (2018) 64–73 71 
Fig. 9. Initial conditions of the domain. 
Fig. 10. Velocity distributions at the time the shock left the cloud at different cloud 
densities. 
the middle and bottom sections of the same ﬁgure illustrate the 
initial properties of the gas phase and the droplet cloud position, 
respectively. Droplet-cloud properties were estimated by consid- 
ering a droplet cloud of constant density deﬁned from the shock 
front to a ﬁxed spray-tip position, based on experimental fuel in- 
jected mass and spray penetration from Tetrault et al. (2015) . From 
the data, the average cloud density for the reference 1D simula- 
tion is obtained by deducing a spray volume from experimental 
spray propagation using a truncated cone having a 20 ° spray angle, 
which results in an average phase density of 6 kg/m 3 . A schemati- 
zation of the axisymmetric spray geometry and 1D simulation do- 
main is shown on Fig. 9 . Ambient conditions were set at 2 MPa and 
293 K with a shock amplitude of 1.085 based on the pressure ratio. 
From this reference case, a parametric study on the droplet 
cloud properties was conducted by varying the cloud density, 
cloud thickness, and droplet diameter with each range reported in 
Table 1 in the cloud properties section. The effect of ambient con- 
ditions was also studied with the range covered for each property 
of the gas phase provided in Table 1 . 
3.2. Simulation results and discussion 
3.2.1. Effect of droplet cloud properties 
The effect of the cloud density on the simulation results was 
initially studied over a broad range of conditions (0.003–24 kg/m 3 ) 
corresponding to liquid volume fractions ( α) between 0% and 3%. 
Fig. 10 presents the cloud velocity and gas-velocity amplitude dis- 
tribution at the time the shock left the droplet cloud, showing that, 
as the droplet cloud density increased, it weakened the shock- 
induced velocity of the droplet cloud, resulting in a slower cloud 
velocity at the tip but with faster spray tail. The tail velocity was 
also affected by the cloud density as part of the shock-wave energy 
Fig. 11. Velocity distributions at the time the shock left the cloud for different 
cloud thicknesses. Top: cloud velocity (left axis); Bottom: gas velocity (right axis). 
Fig. 12. Effect of droplet size on droplet cloud response to shock impulsion. 
is reﬂected at the interface, slightly reducing the shock intensity 
seen by the cloud tail. The reﬂected shock intensity was propor- 
tional to the cloud density. 
Next, the effect of the fuel-cloud thickness on the spray-velocity 
distribution was evaluated for a droplet cloud with a 6 kg/m 3 den- 
sity and a 50 μm droplet diameter. The simulation results pre- 
sented in Fig. 11 for different cloud thicknesses show an almost 
linear decrease in shock-induced spray-tip velocity with increasing 
cloud thickness. This, in turn, allows for predicting that varying the 
cloud thickness by ±50% might result in a post-shock passage fuel- 
spray tip velocity of ±10% around the reference case. 
Finally, the effect of the droplet size, for a constant total liq- 
uid mass injected, on the spray-tip velocity (V tip ) and position was 
studied with a Lagrangian approach by following the spray tip over 
time ( Fig. 12 ) and where spray-tip position (S tip ) was obtained by

<!-- PDF_PAGE: 9 -->

72 P. Tétrault, P. Seers / International Journal of Multiphase Flow 101 (2018) 64–73 
integrating the spray-tip velocity over time as per Eq. (14) . 
S tip ( t ) = 
t 
∫ 
0 
V tip 
(
t ′ )
dt ′ (14) 
Fig. 12 shows that a droplet cloud with a uniform 0.05 μm 
droplet diameter is a limiting case as the droplet cloud almost per- 
fectly followed the gas velocity with a slip velocity under 2% of the 
gas velocity. Larger droplets followed the gas velocity with less ac- 
curacy, as can be seen in Fig. 12 , where the droplet cloud instanta- 
neous velocity and spray-tip position are expressed as a function of 
time. Increasing the droplet diameter resulted in a lower maximum 
velocity due to slower droplet cloud acceleration rate relative to 
the shocked-state duration. Low tracking accuracy is also observ- 
able through a slower droplet cloud deceleration rate. The com- 
bined effect of the lower velocity peak and slower deceleration rate 
is to attenuate the effect of droplet diameter on the spray-tip po- 
sition for integration periods shorter than the time delay between 
the shock passage and the second injection-tip catch-up. Based on 
the results in Fig. 12 , the mechanical droplet relaxation time was 
estimated based on the droplet reaching 63% of the droplet maxi- 
mum velocity and was equal to 40 μs for a 5 μm diameter droplet, 
which was to be compared to the Stokes response time ( τst ) cal- 
culated as per Eq. (15 ) (Yeom et al. (2012)), which was equal to 
75 μs. For larger droplets, such as 50 μm, the shocked-state dura- 
tion (60 μs) was much shorter than τst which was 750 μs. On the 
other hand, the smaller 0.05 and 0.5 μm droplets had predicted 
response times of 7.5 ns and 750 ns based on Eq. (15 ), which is 
consistent with the observed perfect tracking of the droplets, and 
much shorter than the shocked-state duration. 
τst = 
ρd d 2 
d 
18 μair 
(15) 
While this ﬁgure does not show the impact of droplet diameter 
on the shock amplitude, simulation results revealed that smaller 
droplets extracted more momentum from the shock wave for a 
constant total mass injected, resulting in a peak gas velocity rang- 
ing from 10.7 m/s for the largest 50 μm droplets to 9.1 m/s for the 
smallest 0.05 μm droplets. Nevertheless, the droplet size was ob- 
served to have a minor inﬂuence on the shock intensity between 
the 5 and 50 μm diameter range, which is representative of diesel 
fuel spray droplets observed experimentally with various fuels by 
Chen et al. (2013) . Based on the model’s results in Fig. 12 , the 
maximum droplet cloud velocity was reached 30 μs after the pas- 
sage of the shock, which is consistent with the 300 μs reported 
by Kobiera et al. (2009) for droplets in the millimeter range and 
stronger shock (M = 2 and 2.9) as the increased diameter tended 
to increase the response time. 
3.2.2. Shock-Induced Velocity as a Mechanism for the Push-Forward 
Interaction between Successive Injections 
The push-forward type of interaction intensity ﬁrst reported 
by Arai et al. (1994) was studied based on the results published 
in Tetrault et al. (2015) , in which the phenomenon was also ob- 
served. In Tetrault et al. (2015) , it was hypothesized that the shock 
wave from the second injection could be responsible for the accel- 
eration of the ﬁrst spray cloud before interaction of both sprays. 
Thus, using the above model, the conditions for which the push- 
forward was reported in Tetrault et al. (2015) were reproduced. 
The shock was initiated at a 30 mm position, corresponding to a 
shock detachment position reported in the Schlieren section of this 
paper. However, it is noted that the shock is expected to detach 
closer to the injector at higher backpressure based on the obser- 
vation of Pickett et al. (2010) but as shock wave measurements 
were not pursued by Tetrault et al. (2015) , the exact detachment 
timing is unknown and thus the above result has been used. The 
droplet-cloud density was equal to 6 kg/m 3 from the shock front 
Fig. 13. Simulated and experimental spray reacceleration. 
to the spray-tip position of 49 mm, as measured on the ensemble- 
averaged spray-penetration curve in Tetrault et al. (2015) . The ex- 
perimental spray-penetration curve has been reproduced in Fig. 13 , 
which shows an increase in fuel-spray tip penetration following 
a plateau region and way before the arrival of the second spray 
at 2,5 ms after SOI1 as shown by the arrow tip on Fig. 13 . The 
simulation results were added and show that the modeled reac- 
celeration amplitude was slightly higher than the measured spray 
reacceleration, while being of the same order of magnitude. The 
proposed simpliﬁed model nevertheless reveals that the shock- 
induced velocity from the second injection was of the same or- 
der of magnitude as the observed reacceleration, suggesting that a 
shock from the second injection is a plausible physical mechanism 
for the push-away behavior prior to cloud collision. The difference 
between the simulation results and experimental data might be 
attributable to the droplet-cloud density and to a slightly thinner 
or weaker shock. Results also show that the droplet diameters be- 
tween 5 and 50 μm had little effect on the reacceleration behavior, 
as the cloud composed of smaller droplets achieved faster tip ac- 
celeration and deceleration due to the shock passage, while having 
a slightly lower ﬁnal spray penetration. 
4. Conclusions 
This paper reports on an experimental study conducted to 
quantify the shock-wave characteristics as emitted by a diesel fuel 
injector under single- and double-injection strategies. In this study, 
the shock amplitude was not inﬂuenced by the injection duration 
as long as the full mass ﬂow rate was reached. Only very short in- 
jections close to the injector limit exhibited lower shock amplitude 
with respect to longer injection duration. The diesel-fuel spray in- 
duced shocks having a very thin shocked state with an expansion 
wave closely following the shock front. The multihole injector used 
herein also exhibited weaker shock characteristics than single-hole 
injectors referred to in the literature. 
Subsequent to the experimental study, a 1D two-phase model 
was used to simulate shock wave–fuel-spray-cloud interaction 
based on the experimental results. The parametric study illustrated 
that cloud density is an important parameter that decreased the 
shock-wave amplitude. Fuel-droplet diameter in the range encoun- 
tered in diesel sprays was also investigated and showed that cloud 
acceleration was possible for droplets in the tens of micrometers. 
Finally, the model was used to study the fuel-spray tip penetration 
of a droplet cloud initialized at zero velocity and accelerated by 
shock waves emitted from a second injection resulting in a good 
agreement with results in the literature showing the push-away 
behavior. Hence, the results suggest that shock waves are a proba- 
ble mechanism for the push-away mechanism reported in the lit-

<!-- PDF_PAGE: 10 -->

P. Tétrault, P. Seers / International Journal of Multiphase Flow 101 (2018) 64–73 73 
erature between successive injections and also illustrated that it 
could inﬂuence the mixture-formation process. 
Conﬂicts of interest 
None. 
Web references 
1. ODE45, Mathworks.com, https://www.mathworks.com/help/ 
matlab/ref/ode45.html , (accessed July 18, 2017). 
2. IMCONTRAST, Mathworks.com, https://www.mathworks.com/ 
help/images/ref/imcontrast.html , (accessed December 10, 2017). 
3. IMADJUST, Mathworks.com, https://www.mathworks.com/help/ 
images/ref/imadjust.html , (accessed December 10, 2017). 
Acknowledgement 
The authors are thankful for the scholarship provided by the 
FRQNT. 
References 
Anderson, J.D. , 2004. Modern Compressible Flow, third ed. McGraw-Hill . 
Arai, M. , Amagai, K. , 1994. Experimental study on a diesel spray of multi-stage in- 
jection. International symposium COMODIA, 94 . 
Chauvin, A. , Daniel, E. , Chinnayya, A. , Massoni, J. , Jourdan, G. , 2016. Shock waves in 
sprays: numerical study of secondary atomization and experimental compari- 
son. Shock waves 26 (4), 403–415 . 
Chen, P.C. , Wang, W.C. , Roberts, W.L. , Fang, T. , 2013. Spray and atomization of diesel 
fuel and its alternatives from a single-hole injector using a common rail fuel 
injection system. Fuel 103, 850–861 . 
Han, J.-S. , Lu, P.-H. , Xie, X.-B. , Lai, M.-C. , Henein, N.A , 2002. Investigation of Diesel 
Spray Primary Break-up and Development for Different Nozzle Geometries No. 
2002-01-2775. SAE Technical Paper . 
Hargather, M.J. , Settles, G.S. , Madalis, M.J. ,2 0 1 0 . Schlieren imaging of lound sounds 
and weak shock waves in air near the limit o visibility. Shock Waves 20, 9–17 . 
Helmantel, A., Denbratt, I., 2004. HCCI Operation of a Passenger Car Common Rail 
DI Diesel Engine with Early Injection of Conventional Diesel Fuel SAE Technical 
Paper 2004-01-0935 doi: 10.4271/2004- 01- 0935 . 
Hillamo, H. , Sarjovaara, T. , Vuorinen, V. , Larmi, M. , Isaksson, S. , Wik, C. , 2008. Diesel 
Spray Penetration and Velocity Measurements No. 2008-01-2478. SAE Technical 
Paper . 
Hiroyasu, H. , Shimizu, M. , Arai, M. , 1982. The breakup of high speed jet in a high 
pressure gaseous atmosphere. In: Proceedings of the 2nd International Confer- 
ence on Liquid Atomization and Spray Systems . 
Hori, T. , Senda, J. , Kuge, T. , Fujimoto, H. , 2006. Large Eddy Simulation of Non-E- 
vaporative and Evaporative Diesel Spray in Constant Volume Vessel by Use of 
KIVALES No. 2006-01-3334. SAE Technical Paper . 
Huang, W. , Wu, Z. , Gao, Y. , Zhang, L. , 2015. Effect of shock waves on the evolution 
of high-pressure fuel jets. Appl. Energy 159, 4 42–4 48 . 
Jia, T.-M. , Yu, Y.-S. , Li, G.-X. , 2017. Experimental investigation of effects of super high 
injection pressure on diesel spray and induced shock waves characteristics. Exp. 
Thermal Fluid Sci . 
Jourdan, G. , 2007. Drag coeﬃcient of a sphere in a non-stationary ﬂow: new results. 
Proc. R. Soc. A . 
Jourdan, G. , 2010. Attenuation of a shock wave passing through a cloud of water 
droplets. Shock Waves . 
Kobiera, A. , Szymczyk, J. , Wola ´nski, P. , Kuhl, A. , 2009. Study of the shock-induced 
acceleration of hexane droplets. Shock Waves 18 (6), 475–485 . 
Mohan, B. , Wenming, Y. , Chou, S.k , 2013. Fuel injection strategies for performance 
improvement and emissions reduction in compression ignition engines—a  re- 
view. Renew. Sustain. Energy Rev. 28, 664–676 0 . 
Moon, S. , Gao, Y. , Park, S. , Wang, J. , Kurimoto, N. , Nishijima, Y. , 2015. Effect of the 
number and position of nozzle holes on in-and near-nozzle dynamic character- 
istics of diesel injection. Fuel 150, 112–122 . 
Nakahira, T., Komori, M., Nishida, M., Tsujimura, K., 1992. The Shock Wave Gener- 
ation Around the Diesel Fuel Spray with High Pressure Injection SAE Technical 
Paper 920460 doi: 10.4271/920460 . 
Payri, R. , Climent, H. , Salvador, F.J. , Favennec, A.G. , 2004. Diesel injection system 
modelling. Methodology and application for a ﬁrst-generation common rail sys- 
tem. Proc. Inst. Mech. Eng. Part D 218 (1), 81–91 . 
Pickett, L.M. , Kook, S. , 2010. Effect of ambiant temperature and density on shock 
wave generation in a Diesel engine. Atomization Sprays 20 (2), 163–175 . 
Pilch, M. , Erdman, C.A. , 1987. Use of breakup time data and velocity history data to 
predict the maximum size of stable fragments for acceleration-induced breakup 
of a liquid drop. Int. J. Multiphase Flow 13 (6), 741–757 . 
Plamondon, É. , 2015. Impact de l’utilisation des stratégies d’injection multiple et de 
biodiesel sur un moteur diesel àr a m p e commune d’injection. École de tech- 
nologie supérieure . 
Ranz, W.E. , Marshall Jr, W.R. , 1952. Evaporation from drops. Chem. Eng. Progress 48 
(3), 141–173 . 
Saurel, R. , Daniel, E. , 1994. Two-phase ﬂows: second-order schemes and boundary 
conditions. AIAA J. 2 (6) . 
Smolders, H.J. , Van Dongen, M.E.H. , 1992. Shock wave structure in a mixture of gas, 
vapour and droplets. Shock Waves 2 (4), 255–267 . 
Sun, M. , Saito, T. , Takayama, K. , Tanno, H. , 2005. Unsteady drag on a sphere by shock 
wave loading. Shock waves 14 (1–2), 3–9 . 
Tetrault, P., Plamondon, E., Breuze, M., Hespel, C., et al., 2015. Fuel Spray Tip Pene- 
tration Model for Double Injection Strategy SAE Technical Paper 2015-01-0934 
doi: 10.4271/2015- 01- 0934 . 
Toro, E.F. , 1999. Riemann Solvers and Numerical Methods for Fluid Dynamics, sec- 
ond ed. Springer-Verlag . 
Wang, J., MacPhee, A., Powell, C.F., Yue, Y., Narayanan, S., 2002. Shock Waves Gener- 
ated by High-Pressure Fuel Sprays Directly Imaged by X-Radiography 2002, SAE 
Technical Paper 2002-01-1892 doi: 10.4271/2002- 01- 1892 . 
Yeom, G.S. , Chang, K.S. , 2012. Dissipation of shock wave in a gas-droplet mixture by 
droplet fragmentation. Int. J. Heat Mass Transfer 55 (4), 941–957 .
