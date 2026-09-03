<!-- PDF_PAGE: 1 -->

Available online at www.sciencedirect.com 
Proceedings of the Combustion Institute 39 (2023) 3063–3072 
www.elsevier.com/locate/proci 
Simulation of liquid droplets combustion in a rotating 
detonation engine 
Marc Salvadori a , ∗, Achyut Panchal b , Suresh Menon b 
a George W. Woodruff School of Mechanical Engineering, Georgia Institute of Technology, Atlanta, GA, 30332, United 
States 
b School of Aerospace Engineering, Georgia Institute of Technology, Atlanta, GA 30332, United States 
Received 2 January 2022; accepted 1 September 2022 
Available online 22 October 2022 
Abstract 
Recent research towards using liquid fuel in rotating detonation engines (RDE) has been assessed here us- 
ing numerical simulations of a representative three-dimensional (3D) configuration. Eulerian-Lagrangian 
simulations of a 3D non-premixed RDE configuration are conducted and it is demonstrated that kerosene 
injection through the air plenum helps stabilize the RDE operation at the conditions where a pure gaseous H 2 
RDE is unable to sustain the propagation of a detonation. The H 2 -fueled RDE is first simulated at a global 
equivalence ratio of 0.5, which shows unstable burning with localized extinction and re-ignition followed by 
system failure, and then compared against another simulation where kerosene droplets are injected in the air 
plenum keeping the same H 2 fueling condition. The results show that the existence of the detonation aids 
in the evaporation of the injected droplets behind it, allowing the vaporized mixture to properly mix before 
the next detonation cycle such that continuous (cyclic and stable) propagation can be achieved. It is further 
shown that whereas hydrogen mainly reacts near the bottom of the chamber, the injected droplets vaporize 
slow and react at larger heights. As a result, for the latter case the heat release is more distributed and provides 
an additional mechanism to stabilize the detonation cycle. 
© 2022 The Combustion Institute. Published by Elsevier Inc. All rights reserved. 
Keywords: Detonation; Rotating detonation engine; Liquid droplets; Lagrangian 
1. Introduction 
Rotating Detonation Engine (RDE) is a novel 
pressure gain combustor where an increased ther- 
modynamic efficiency is achieved by utilizing a near 
constant volume combustion process of a detona- 
∗ Corresponding author. 
E-mail address: msalvadori3@gatech.edu 
(M. Salvadori). 
tion wave [1–3] . The detonation wave propagates 
azimuthally in an annular combustor and it is sus- 
tained by the fast mixing induced from discrete in- 
jectors ahead of it. Although previous efforts have 
studied RDEs with gaseous fuels [1,4–8] , the cur- 
rent study focuses on liquid fuels injection due to 
their high energy content, practicality, safety, and 
storage benefits. 
Past experimental studies [9–11] have shown 
that a self-sustained detonation wave can be 
achieved using liquid droplets and air when another 
https://doi.org/10.1016/j.proci.2022.09.002 
1540-7489 © 2022 The Combustion Institute. Published by Elsevier Inc. All rights reserved.

<!-- PDF_PAGE: 2 -->

3064 M. Salvadori, A. Panchal and S. Menon / Proceedings of the Combustion Institute 39 (2023) 3063–3072 
gaseous fuel, in very small amount such as hydro- 
gen is also used. The burning of hydrogen would 
allow high heat release and rapid evaporation of 
the droplets to facilitate formation and develop- 
ment of a detonation wave [9] inside the combustor. 
Other methods such as using oxygen-enriched oxi- 
dizer [12] or increase oxidizer injection temperature 
[13] have also been considered. Computational ef- 
forts in this direction are few and have been limited 
to simplified two-dimensional (2D) domains [14–
16] or 3D with gaseous fuel [6] . 3D simulations of 
a realistic RDE with liquid fuel are, to the best of 
our knowledge, not yet demonstrated. 
The focus of this study is to demonstrate and 
understand the capability of liquid fuel to sustain 
a detonation wave in a realistic RDE geometry 
[5,8,17] . This RDE was recently simulated using 
gaseous hydrogen as a fuel [8] and it was shown 
that stable operation can be achieved, as seen in 
experiments. Starting from this established stable 
burning at stoichiometric conditions, first the injec- 
tion rate of gaseous hydrogen is lowered to reach 
a lean limit of propagation where the detonation 
is unable to sustain. Then, a separate simulation is 
conducted where the hydrogen injection rate is still 
reduced and kerosene droplets are injected to sus- 
tain the detonation wave. The use of hydrogen has 
been proven to enhance the detonation sensitivity 
of a kerosene-air mixture in the past [9,18] . The ob- 
tained results are analyzed at this obtained quasi- 
steady operation. 
An Eulerian-Lagrangian (EL) method [19,20] is 
used to simulate the compressible reactive two- 
phase flows and a reduced chemical mechanism 
for hydrogen/kerosene/air combustion is employed. 
In the following sections, the simulation config- 
uration, numerical details, and the results are 
discussed. 
2. Simulation approach and numerical setup 
Unsteady, compressible, reactive Navier-Stokes 
equations are solved using the EL framework in 
a well-established solver LESLIE. A detailed de- 
scription of the numerical scheme and the govern- 
ing equations can be found elsewhere [19,20] . Con- 
sidering that the focus here is to model the inter- 
action of droplets with the detonation wave in the 
chamber, and typically the liquid injectors are lo- 
cated away from the detonation wave [11] , a dilute 
modeling approach is used, although dense model- 
ing is also possible [20] . The droplets are assumed 
as point-particles and tracked using a Lagrangian 
tracking approach. Collision, breakup, droplet de- 
formation effects are neglected at present. Since 
the droplets are injected away from the detonation 
wave for this configuration (described later), the liq- 
uid volume loading within the combustor is esti- 
mated to be < 0.02% suggesting minimal collisional 
effects. Additionally, the Weber number (We) is < 12 
for 50% of the injected droplets, and therefore, sec- 
ondary breakup is not expected to affect the results 
significantly [21] . Using a breakup model is not ex- 
pected to incur a significant increase in the compu- 
tational cost, however, we would like to note that 
even though modeling secondary breakup may be 
computationally feasible [22] , fundamental models 
for secondary breakup in presence of detonations 
are not widely available. 
Drag and heat/mass transfer of the droplets 
is modeled using well-established models for gas- 
liquid flows [23] , however, it is noted that funda- 
mental studies may be required in the future to im- 
prove them in presence of detonation waves. To 
make these simulations computationally tractable, 
the physical particles are combined in groups of 
eight, known as computational “parcels” [23,24] , 
which are then tracked instead. Parcels are mod- 
eled as point-particles, and they are connected to 
the local gas-phase quantities (and therefore, the 
detonation wave) via drag and heat/mass-transfer 
laws [23] . These laws are obtained from shocked 
particles but considering that the droplet evap- 
oration timescale ( τdrop ≈0.8 ms) is significantly 
larger than that of the detonation-wave passage 
( d p /U D = 14 ns), these can be considered valid. The 
interphase momentum and work transfer also in- 
clude pressure-gradient terms, which are expected 
to be dominant near the detonation wave. Although 
an analysis on the effects of number of particles 
within a parcel was not performed for this configu- 
ration, it was previously shown [24] that a particles- 
per-parcel value of 8 was a reasonable choice. 
The RDE combustor that is used in this study 
employs 80 discrete hydrogen injectors and a con- 
tinuous radial slot for air. The annular channel has 
a width of 7.6 mm. Figure 1 shows the overall com- 
putational domain and the grid in the injector near- 
field. This has been used in previous experimental 
[5,17] and computational studies [8] , as noted ear- 
lier. The inflow mass flow rate ( ˙ m in ) and the temper- 
ature for both the hydrogen (entering the chamber 
through the injectors) and the air (entering through 
a plenum) are 0.005 kg/s, 300 K, and 0.33 kg/s, 
300 K, respectively. Liquid droplets of diameter d d 
= 20 μm are injected from the air plenum with a 
mass flow rate of 0.0112 kg/s and temperature 300 
K. In absence of any experimental data, a mono- 
disperse injection is considered here, however, a 
poly-disperse injection is also possible. The droplet 
injection procedure used here follows recent exper- 
iments on two-phase RDE [17] , where the authors 
showed that premixing air with solid particles could 
induce early mixing and sustain the propagating 
detonation wave. The injected droplet size is within 
the range of the other studies that have explored 
the use of liquid sprays in RDE [12,14,15,18] , and 
further studies focused on its sensitivity can be con- 
sidered in the future.

<!-- PDF_PAGE: 3 -->

M. Salvadori, A. Panchal and S. Menon / Proceedings of the Combustion Institute 39 (2023) 3063–3072 3065 
Fig. 1. Three-dimensional non-premixed RDE combustor schematic. 3D flow-field under steady operation is shown in (a) 
along with the injectors and the plenum. Computational grid in the injector near-field is shown in (b). 
The complex RDE geometry is modeled using 
82 separate multi-block structured grids that are 
joined with each other via non-conformal grid in- 
terfaces [8] . The overall mesh contains approxi- 
mately 55 million grid points with ∼100 μm cell 
size in the near injector region. The grid pro- 
gressively coarsens towards the outflow. Charac- 
teristic boundary conditions [25] are used for in- 
flow/outflow allowing acoustic waves to leave the 
domain [25] , whereas walls are modeled as no-slip 
and adiabatic. Adiabatic walls are used in this work 
in absence of any experimental measurements of 
temperatures or heat-fluxes through the wall (via 
a cooling system, for instance). Either isothermal 
or constant heat flux walls can be used in the fu- 
ture to model heat losses through the wall if such 
data is available. The validation of the grid and the 
boundary conditions is provided elsewhere and it 
is not discussed here for brevity [8] . In the current 
study, kerosene vapor is modeled as C 10 H 2 0 and 
a two-step semi-global mechanism containing fiv e 
species is used [26] for its combustion. A seven-step, 
six-species [27] reduced mechanism is used for hy- 
drogen combustion. Both kinetics are merged to- 
gether to model the kerosene/hydrogen/air combus- 
tion considered here (validation in the Appendix). 
Two simulations are analyzed and discussed in 
this paper. In one simulation, the hydrogen-air 
global equivalence ratio ( φg ) is lowered to 0.5 from 
an existing stable solution at stoichiometric condi- 
tions [8] . Simulation outputs, such as pressure, to- 
tal heat release rate (HRR) are recorded, and this 
case serves as a baseline. In the second simulation, 
the hydrogen mass flow rate is reduced to the same 
global φg = 0 . 5 , but the liquid droplets are injected 
at the same time in the air plenum. The total mass 
flow rate of kerosene (assuming all injected droplets 
are evaporated and burned) with the same H 2 in- 
jection corresponds to an effective global equiva- 
lence ratio of unity. Simulations are carried out us- 
ing a Intel Xeon Gold 6226 ”Cascade Lake” clus- 
ter. A single detonation cycle (the time for one rev- 
olution of the detonation front) requires around 
76,000 single-processor hours. As per the code scal- 
ability reported previously [8] , the simulations were 
carried out on 3200 processors. Seven detonation 
cycles are simulated for each case to obtain a quasi- 
steady behavior that is independent of any initial 
transients. 
3. Results and discussion 
3.1. Unsteady flow features 
As the mass flow rate of hydrogen is decreased 
to obtain to reach φg = 0 . 5 , the behavior of the 
propagating detonation begins to change. Fig. 2 
compares the total HRR of this case against the 
case for which the liquid kerosene droplets are, in 
addition, injected. After t/τcycle ∼ 1o f imposing 
the reduced injection rate for the hydrogen alone 
case, an unstable mode of propagation triggers in 
which local extinctions and re-ignitions occur, as 
seen in other studies [5,28] . After t/τcycle ∼ 6 , the 
HRR stays continuously low and no local ignition 
is possible, showing system failure. This scenario 
is drastically different when the liquid droplets are 
injected, as a periodic and continually propagat- 
ing front is achieved. The liquid fuel provides ad- 
ditional heat release that allows the detonation 
to be sustained. The time-averaged HRR of the 
kerosene- H 2 -air case (at φH 2 = 0.5, φKERO = 0.5) is 
0.838 MW, whereas it was 0.995 MW for H 2 -air sys- 
tem at φH 2 = 1 [8] . Although not shown here, the liq- 
uid and the vaporized fuel mass integrated within 
the chamber stabilize after t/τcycle ∼ 2 , suggesting 
a quasi-steady behavior. Some additional details of 
these cyclic processes are in the attached Supple- 
mentary material as animations S1-S4.

<!-- PDF_PAGE: 4 -->

3066 M. Salvadori, A. Panchal and S. Menon / Proceedings of the Combustion Institute 39 (2023) 3063–3072 
Fig. 2. Time-varying total heat release rate (HRR) for 
both cases. 
The observations are further confirmed from the 
pressure traces shown in Fig. 3 taken at four an- 
gular locations. The velocity of the front is com- 
puted as U D = (2 πr mean ) / (1 . 0 /f F F T ) where r mean is 
the mean radius of the RDE chamber, and f F F T is 
the dominant frequency in the Fast Fourier Trans- 
form (FFT) analysis, which is found to be 2930 
Hz. This results in a speed of 1342.07 m/s, which 
is comparable with values found in the literature 
for experimental liquid kerosene-air RDEs with hy- 
drogen addition [11] . Previous experimental H 2 -air 
RDEs [5,17] with a similar injection configuration 
reported 2900 < f F F T < 3400 Hz and our past nu- 
merical results show an f F F T = 4148.6 Hz for a 
single-wave system [8] . The two-phase results can- 
Fig. 3. Time-varying pressure traces recorded at various 
azimuthal locations for both cases. 
Fig. 4. Instantaneous (a) three-dimensional view of detonation front and droplets, and 2D unwrapped mid-plane of (b) 
temperature, (c) hydrogen, and (d) kerosene vapor mass fraction. To identify the structure of the detonation wave the iso- 
surfaces (colored by temperature) in (a) and iso-contours in (c-d) of pressure are shown. The selected range of pressure 
values is 0.4- 1.0 MPa.

<!-- PDF_PAGE: 5 -->

M. Salvadori, A. Panchal and S. Menon / Proceedings of the Combustion Institute 39 (2023) 3063–3072 3067 
not be directly compared to the limited experiments 
[9] as they use a different configuration and injec- 
tion conditions, but the recorded detonation veloc- 
ities for the mixture kerosene- H 2 -air were 1500 m/s 
at φg = 1.1 and 1350 m/s for φg = 0.8, which are sim- 
ilar in magnitude to our simulation results (1342.07 
m/s). 
The detonation cycle time is then computed as 
τcycle = 1 /f F F T . The gaseous H 2 case clearly shown 
an unstable mode of propagation ( Fig. 3 (a)) where 
the peaks do not resemble a continuous oscilla- 
tory behavior but rather show irregular pressure 
peaks ranging from 0.4 MPa to 2.0MPa as a re- 
sult of local extinctions and re-ignitions. Experi- 
mental [5,28,29] and numerical [6–8] studies have 
shown that for a steady cyclic operation of an RDE 
the pressure profiles should have a nearly constant 
time separation between the angular locations. The 
pure hydrogen case shows that during the unsta- 
ble operation, multiple pressure fronts of differ- 
ent strength co-exist at the same angular location. 
On the other hand, the case with liquid injection 
( Fig. 3 (b)) shows a self-sustained and continually 
propagating detonation wave with strong pressure 
peaks and with nearly periodic oscillations consis- 
tent with a stable behavior typically found in past 
studies of gaseous RDEs [5–9] . 
The overall flow field for the case with liq- 
uid injection at an instant is presented in Fig. 4 . 
Fig. 4 (a) shows instantaneous 3D detonation struc- 
ture during its propagation along with the dis- 
persed droplets within the chamber, and Fig. 4 (b- 
d) show unwrapped 2D flow-fields. The shock front 
has a corrugated structure that extends almost up 
to the full chamber height ( z/H = 0 . 8 ). High pres- 
sure and high temperature are found downstream 
of the detonation front over a significant angu- 
lar distances ( ∼ 50 ◦ and ∼ 120 ◦, respectively). The 
droplet diameter reduces from 20 μm at the in- 
jection plane to almost 10 μm at mid-chamber as 
a result of vaporization. Hydrogen fuel is primar- 
ily concentrated at lower heights ( z/H < 0 . 2 ) and 
ahead of the detonation front, whereas, Kerosene 
vapor is present up to z/H ∼ 0 . 6 and even behind 
the detonation front as a result of liquid vaporiza- 
tion. Both hydrogen and kerosene vapor are low 
behind the detonation front, suggesting their con- 
sumption. Some burning also occurs upstream of 
the detonation wave as commonly found in other 
gaseous RDEs [6–8] . 
3.2. Azimuthal detonation structure 
After a quasi-steady state is reached, the flow- 
field quantities at an instant are averaged over the 
radial direction to understand the detonation struc- 
ture in the azimuthal direction at different heights. 
These are shown in Fig. 5 and 6 . The pressure pro- 
files show a strong spike at around θ≈ 150 , sug- 
gesting a detonation front that goes up to z/H = 
0 . 5 . Temperatures at the shock front are close to the 
Fig. 5. Instantaneous radially averaged azimuthal pro- 
files of (a) pressure, (b) temperature and (c) heat release 
rate (HRR) at different chamber heights. The height is 
normalized by the total height of the combustor (H) 
which corresponds to 100 mm. 
post-detonation CJ temperature of an atmospheric 
mixture of gaseous H 2 -air at φ = 0 . 5 ( T CJ = 2204 . 1 
K). The temperature reduces from about 2200 K 
at θ≈ 150 (detonation front) to 300 K at θ= 0 
(post detonation) for z/H = 0 as a result of the 
cold injection from the bottom, however, at higher 
heights, the higher temperature is maintained for 
longer azimuthal distances. For instance, at z/H = 
0 . 6 , the temperature stays above 1500 K at all lo- 
cations. This appears to be the result of the re- 
maining hot products that eventually exit through 
the outflow on the top, as well as due to possi- 
ble burning of kerosene vapor behind the front 
(shown later). The HRR peaks at the detonation 
front but still maintain a finite value behind it. 
Along the chamber height, the HRR increases up 
to two orders of magnitude, and this is mainly

<!-- PDF_PAGE: 6 -->

3068 M. Salvadori, A. Panchal and S. Menon / Proceedings of the Combustion Institute 39 (2023) 3063–3072 
Fig. 6. Instantaneous radially averaged azimuthal pro- 
files of (a) hydrogen mass fraction ( Y H2 ) and (b) kerosene 
gas mass fraction ( Y KERO ) at different chamber heights. 
The height is normalized by the total height of the com- 
bustor (H) which corresponds to 100 mm. 
due to burning of kerosene vapor, which becomes 
available via liquid fuel vaporization along the 
height. More details on this process are provided 
later. 
Ahead of the detonation front ( θD > 150 ◦), the 
hydrogen concentration is the highest at the bot- 
tom ( z/H = 0 ) since that is where it is injected 
from, but it reduces almost to zero by z/H = 0 . 6 
(see Fig. 6 ). Hydrogen is consumed along the det- 
onation front ( θD ≈ 150 ◦), and as a result it re- 
duces to zero in the post-detonation regions at all 
heights. Kerosene shows a very different behavior. 
Unlike hydrogen, the kerosene concentration in- 
creases behind the detonation front at z/H = 0 (by 
∼3 times), and this is due to a substantial liquid 
vaporization that occurs in the high temperature 
post-detonation region. Going up in the chamber 
height ( z/H = 0 . 1 − 0 . 6 ), the kerosene concentra- 
tion reduces along the detonation wave, suggesting 
its consumption at the front. However, unlike hy- 
drogen, its concentration ahead of the detonation 
wave does not reduce but stays constant as a re- 
sult of the continuous liquid vaporization that oc- 
curs along the chamber height (shown later). Even 
though the hydrogen consumption at the detona- 
tion front reduces along the chamber height due to 
the lack of available fuel ahead of it, the kerosene 
consumption does not since its vapor is available 
for burning at least up to z/H = 0 . 6 . This is fur- 
Fig. 7. Instantaneous radially averaged azimuthal pro- 
files of the reaction rates of (a) hydrogen ( ˙ ω H2 ) and (b) 
kerosene ( ˙ ω KERO ) at different chamber heights. The az- 
imuthal range is chosen to be a close-up view of the deto- 
nation front ( θD ≈ 150 o ). The height is normalized by the 
total height of the combustor (H) which corresponds to 
100 mm. 
ther confirmed by radially averaged hydrogen and 
kerosene (vapor) reaction rates ( ˙ ω H 2 and ˙ ω KERO ) 
plotted in Fig. 7 . The peaks of the hydrogen re- 
action rate reduce along the chamber height, e.g., 
peak of ˙ ω H 2 reduces by 10 2 times from z/H = 0 . 0 
to z/H = 0 . 4 , whereas, the kerosene reaction rates 
stay almost the same, at least till z/H = 0 . 4 . This 
also confirms the earlier argument that the higher 
heat release observed at for z/H = 0 . 2 − 0 . 6 is pri- 
marily due to kerosene. 
3.3. Liquid-phase features 
To further understand distribution of the liq- 
uid fuel and its vaporization, the averaging in the 
radial direction is also conducted for liquid vol- 
ume fraction ( αd ), Sauter mean diameter (SMD, 
d p ), and evaporation rate ( ˙ m d ) at different heights 
(see Fig. 8 ). Both αd and d p predominantly vary 
along the chamber height as compared to the az- 
imuthal direction. This indicates that although the 
consumption of gaseous reactants (kerosene vapor 
and hydrogen) happens rapidly across the detona- 
tion front (see Fig. 6 ), the vaporization is a much 
slower process. A time-scale of liquid vaporization

<!-- PDF_PAGE: 7 -->

M. Salvadori, A. Panchal and S. Menon / Proceedings of the Combustion Institute 39 (2023) 3063–3072 3069 
Fig. 8. Instantaneous radially averaged azimuthal pro- 
files of (a) volume fraction ( αd ), (b) droplet diameter ( d p ), 
and (c) evaporation rate ( ˙ m d ) at different chamber heights. 
The height is normalized by the total height of the com- 
bustor (H) which corresponds to 100 mm. 
was estimated to be τdrop = 0 . 8 ms based on a sin- 
gle droplet (20 μm, 300 K) evaporation in a quies- 
cent environment at 1273.5 K. Based on this, for the 
currently injected 20 μm droplets, τdrop /τcycle ≈ 2 . 3 , 
which means that it takes a couple cycles of the 
detonation wave for the droplets to vaporize com- 
pletely and they don’t vaporize at an instant ahead 
of the detonation wave. 
Along the chamber height, as the vaporization 
occurs, the volume-fraction reduces from 10 −2 at 
z/H = 0 . 0 to 10 −5 at z/H = 0 . 6 , suggesting a near 
complete vaporization. Only a few droplets do es- 
cape via the outflow. The SMD reduces from the 
initial 20 μm to 5 μm by z/H = 0 . 6 . The kerosene 
vapor is continuously made available for burning 
via this vaporization process, at least till z/H = 0 . 6 . 
Fig. 9. Time-averaged axial profiles 20 o ahead of the det- 
onation wave of (a) mass fraction of gaseous hydrogen 
and kerosene, (b) kerosene mass fraction with liquid vol- 
ume fraction, and (c) temperature and diameter of liq- 
uid droplets. The axial location is normalized by the total 
height of the combustor (H) which corresponds to 100 
mm. 
The evaporation rates ˙ m d do show an azimuthal 
variation. The evaporation rate at z/H = 0 . 0 is ∼10 
times higher in the post-detonation region ( 0 0 > 
θ> 150 ◦) as the temperatures are high resulting 
from hydrogen burning. Both the azimuthal vari- 
ation in the evaporation rate and its absolute value 
reduce with chamber height as lesser liquid fuel re- 
mains available. 
3.4. Mixture composition ahead of the front 
To understand the behavior of the mixture, 
the liquid droplets ahead of the wave that allows 
for self-sustained propagation are investigated fur- 
ther. The radially averaged properties 20 o ahead 
of the front are time-averaged over a single cycle 
and the results are shown in Fig. 9 . At the injec- 
tion plane ( 0 . 0 < z/H < 0 . 05 ) most of the fuel is 
in the form of hydrogen, but along the chamber 
height the dominant fuel becomes gaseous kerosene 
with a nearly uniform profile. Even though the va- 
por kerosene burns at the front, it is replenished 
via the vaporization process along the height, as 
noted before. The liquid volume fraction exhibits 
a rapid decrease initially, indicative of a fast evap- 
oration between z/H = 0 . 0 and z/H = 0 . 02 , but 
the reduction after that is gradual. This results in 
a peak in kerosene vapor concentration at around

<!-- PDF_PAGE: 8 -->

3070 M. Salvadori, A. Panchal and S. Menon / Proceedings of the Combustion Institute 39 (2023) 3063–3072 
Fig. 10. Ignition delay time for various concentration of 
hydrogen and kerosene vapor computed at 10 atm and 
50 atm. Each symbol corresponds to a different amount 
of γ. Solid and dashed lines correspond to the detailed 
[31] and reduced mechanism, respectively. 
z/H = 0 . 02 . Sauter mean droplet diameter ( d p ) and 
the temperature ( T d ) variation along the cham- 
ber height show typical behavior of a vaporizing 
droplet. T d initially increases rapidly as the droplets 
heat up in the background high temperature, but 
it stays nearly constant after reaching its wet-bulb 
temperature. The SMD d p reduces from 20 μm 
to 10 μm from z/H = 0 . 0 to z/H = 0 . 4 along the 
chamber height as expected, providing the vapor- 
ized fuel for burning. 
4. Conclusions 
Numerical simulations of a realistic non- 
premixed RDE combustor [8] are conducted to un- 
derstand the ability of liquid fuel to enable a self- 
sustained detonation wave at low gaseous fuel in- 
jection rates. As per the author’s knowledge this is 
a first such simulation that demonstrates and stud- 
ies liquid-fuel burning in a realistic RDE. Two sim- 
ulations are discussed here, one with only gaseous 
hydrogen, but at a low global equivalence ratio of 
0.5 (at which the detonation eventually dies off), 
and another where in addition to this gaseous hy- 
drogen, liquid kerosene (20 μm droplets) is also 
injected, resulting in sustained and stable cyclic 
detonation. 
The 3D flow-field is analyzed to understand the 
detonation structure with liquid fuel. The 3D det- 
onation wave is highly corrugated and extends in 
height at least up to z/H = 0 . 6 . At lower chamber 
heights ( z/H < 0 . 1 ), the gaseous hydrogen com- 
bustion dominates, however, for z/H = 0 . 2 − 0 . 6 
it is the kerosene vapor that burns predominantly. 
The time-scale of liquid vaporization compared 
to the detonation wave is larger: τdrop /τcycle ∼ 2 . 4 , 
and as a result, the liquid vaporization takes place 
along the chamber height. The liquid properties 
show minimal variation in the azimuthal direction 
along the detonation wave. Ahead of the detona- 
tion front, the available gaseous hydrogen reduces 
with the chamber height, but the kerosene vapor 
stays about constant at least till z/H = 0 . 4 as it 
gets replenished via liquid vaporization. The liquid 
volume-fraction ahead of the front reduces from 
10 −2 at z/H = 0 . 0 to 10 −4 at z/H = 0 . 4 , suggesting 
a near complete vaporization. Even though there is 
only minimal hydrogen left to burn for z/H > 0 . 2 , 
as a result of the burning of kerosene vapor, the 
HRR peaks go up by almost two orders of magni- 
tude as compared to those of z/H = 0 . 0 . 
This study demonstrates that a stable detona- 
tion can be achieved when liquid droplets are in- 
jected in a realistic RDE. Although hydrogen rep- 
resents an additive that aids in burning and evapo- 
ration of the liquid phase, the combined effects re- 
sults in a steady operation of the RDE. The use of 
hydrogen alone at such low equivalence ratio leads 
to insufficient heat release, leading to an instability 
as also observed in some experiments [28,30] . Fu- 
ture work can focus on understanding effects of the 
droplet injection parameters (diameter, breakup, 
etc.), and if some of them can lead to a stable RDE 
operation with pure liquid fuels. Understanding the 
effect of liquid fuel addition on multi-wave RDE 
systems is another avenue for future work. Mod- 
eling breakup and collisions maybe of importance 
if the liquid fuel is to be injected directly into the 
combustion chamber. Although, such simulations 
could get prohibitively expensive due to the resolu- 
tion requirements of capturing the primary atom- 
ization and breakup. 
Supplementary data 
See the Supplementary material for animations 
of the transient propagation of the detonation 
wave within the RDE associated with the simulated 
cases. 
Declaration of Competing Interest 
The authors declare that they have no known 
competing financial interests or personal relation- 
ships that could have appeared to influence the 
work reported in this paper.

<!-- PDF_PAGE: 9 -->

M. Salvadori, A. Panchal and S. Menon / Proceedings of the Combustion Institute 39 (2023) 3063–3072 3071 
Acknowledgments 
This work is supported in part by the Georgia 
Tech Foundation funds for the Hightower Profes- 
sorship. The second author is supported in part 
by NASA Glenn Research Center grant. The com- 
putational resource provided by the Georgia Tech 
Partnership for an Advanced Computing Environ- 
ment (PACE) is greatly appreciated. 
Appendix A. Validation of chemical mechanism 
To validate the reduced kinetics, premixed 1D 
detonation wave speeds ( U D ) and auto-ignition de- 
lay times ( τign ) are computed and compared against 
a detailed kinetics [31] at RDE representative con- 
ditions. The U D computed using the reduced kinet- 
ics at global RDE operating conditions ( φH 2 = 0.5, 
φKERO = 0.5, 300 K, 1 atm) matches against the de- 
tailed kinetics with a < 4% error (Reduced: 1868.97 
m/s, Detailed: 1786.86 m/s). The τign computed us- 
ing the reduced and the detailed kinetics are com- 
pared for various concentration of hydrogen and 
kerosene vapor at 10 atm and 50 atm in Fig. 10 . 
Here, γ = X H 2 / (X H 2 + X KERO ) and X H 2 and X KERO 
are mole fractions of the hydrogen and the kerosene 
vapor, respectively. The reduced mechanism is able 
to capture the variation of τign with γ. There are 
quantitative differences at lower temperatures and 
in the pure hydrogen limit, however, these are ex- 
pected of a reduced kinetics and using a detailed 
kinetics for the 3D computations is prohibitively 
expensive. 
Supplementary material 
Supplementary material associated with this ar- 
ticle can be found, in the online version, at doi: 10. 
1016/j.proci.2022.09.002 
References 
[1] F.A. Bykovskii , S.A. Zhdan , E.F. Vedernikov , Con- 
tinuous spin detonations, J. Prop. Power 22 (6) (2006) 
1204–1216 . 
[2] P. Wola ´nski , Detonative propulsion, Proc. Combust. 
Inst. 34 (1) (2013) 125–158 . 
[3] F.K. Lu , E.M. Braun , Rotating detonation wave 
propulsion: Experimental challenges, modeling, and 
engine concepts, J. Prop. Power 30 (5) (2014) 
1125–1142 . 
[4] D. Schwer , K. Kailasanath , Fluid dynamics of ro- 
tating detonation engines with hydrogen and hy- 
drocarbon fuels, Proc. Combust. Inst. 34 (2) (2013) 
1991–1998 . 
[5] B.A. Rankin , J.R. Codoni , K.Y. Cho , J.L. Hoke , 
F.R. Schauer , Investigation of the structure of det- 
onation waves in a non-premixed hydrogen–air ro- 
tating detonation engine using mid-infrared imaging, 
Proc. Combust. Inst. 37 (3) (2019) 3479–3486 . 
[6] T. Sato , F. Chacon , L. White , V. Raman , M. Gamba , 
Mixing and detonation structure in a rotating deto- 
nation engine with an axial air inlet, Proc. Combust. 
Inst. 38 (3) (2021) 3769–3776 . 
[7] S. Prakash , V. Raman , C.F. Lietz , W.A. Har- 
gus , S.A. Schumaker , Numerical simulation of a 
methane-oxygen rotating detonation rocket engine, 
Proc. Combust. Inst. 38 (3) (2021) 3777–3786 . 
[8] M. Salvadori , P. Tudisco , D. Ranjan , S. Menon , Nu- 
merical investigation of mass flow rate effects on 
multiplicity of detonation waves within a h2/air ro- 
tating detonation combustor, Int. J. H. Energy 47 
(2022) 4155–4170 . 
[9] J. Kindracki , Experimental research on rotating 
detonation in liquid fuel–gaseous air mixtures, 
Aerospace Sci. Technol. 43 (2015) 445–453 . 
[10] F.A. Bykovskii , S.A. Zhdan , E.F. Vedernikov , Con- 
tinuous detonation of the liquid kerosene—air  mix- 
ture with addition of hydrogen or syngas, Combust. 
Exp. Shock Waves 55 (5) (2019) 589–598 . 
[11] J. Kindracki , K. Wacko , P. Wozniak , S. Siatkowski , 
L. Mezyk , Influence of gaseous hydrogen addition 
on initiation of rotating detonation in liquid fuel–air 
mixtures, Energies 13 (19) (2020) 5101 . 
[12] H. Meng , Q. Zheng , C. Weng , Y. Wu , W. Feng , G. Xu , 
F. Wang , Propagation mode analysis of rotating det- 
onation waves fueled by liquid kerosene, Acta Astro- 
nautica 187 (2021) 248–258 . 
[13] Q. Zheng , H. long Meng , C. sheng Weng , Y. wen 
Wu , W. kang Feng , M. liang Wu , Experimental re- 
search on the instability propagation characteristics 
of liquid kerosene rotating detonation wave, Defence 
Technol. 16 (6) (2020) 1106–1115 . 
[14] A.K. Hayashi , N. Tsuboi , E. Dzieminska , Nu- 
merical study on JP-10/air detonation and rotat- 
ing detonation engine, AIAA J. 58 (12) (2020) 
5078–5094 . 
[15] Q. Meng , N. Zhao , H. Zhang , On the distributions 
of fuel droplets and in situ vapor in rotating det- 
onation combustion with prevaporized n-heptane 
sprays, Phys. Fluids 33 (4) (2021) 043307 . 
[16] M. Zhao , H. Zhang , Rotating detonative com- 
bustion in partially pre-vaporized dilute n-heptane 
sprays: Droplet size and equivalence ratio effects, 
Fuel 304 (2021) 121481 . 
[17] I.B. Dunn , V. Malik , W. Flores , A. Morales , 
K.A. Ahmed , Experimental and theoretical analy- 
sis of carbon driven detonation waves in a hetero- 
geneously premixed rotating detonation engine, Fuel 
302 (2021) 121128 . 
[18] J. Kindracki , Study of detonation initiation in 
kerosene–oxidizer mixtures in short tubes, Shock 
Waves 24 (6) (2014) 603–618 . 
[19] K.C. Gottiparthi , S. Menon , A study of interaction 
of clouds of inert particles with detonation in gases, 
Combust. Sci. Technol. 184 (3) (2012) 406–433 . 
[20] A. Panchal , S. Menon , A hybrid eulerian-eule- 
rian/eulerian-lagrangian method for dense-to-dilute 
dispersed phase flows, J. Comp. Phys. 439 (2021) 
110339 . 
[21] R.D. Reitz , Modeling atomization processes in high- 
pressure vaporizing sprays, Atom. Spray Tech. 3 
(1987) 309–337 . 
[22] A. Panchal , S. Menon , Large eddy simulation of 
fuel sensitivity in a realistic spray combustor I. 
Near blowout analysis, Combust. Flame 240 (2022) 
112162 .

<!-- PDF_PAGE: 10 -->

3072 M. Salvadori, A. Panchal and S. Menon / Proceedings of the Combustion Institute 39 (2023) 3063–3072 
[23] G. Faeth , Mixing, transport and combustion in 
sprays, Prog. Energy Combust. Sci. 13 (4) (1987) 
293–345 . 
[24] S. Srinivasan , A.G. Smith , S. Menon , Accuracy, reli- 
ability and performance of spray combustion mod- 
els in LES, in: Quality and Reliability of Large-Eddy 
Simulations II, Springer, 2011, pp. 211–220 . 
[25] T. Poinsot , Boundary conditions for direct simula- 
tions of compressible viscous flows, J. Comp. Phys. 
99 (2) (1992) 352 . 
[26] B. Franzelli , E. Riber , M. Sanjosé, T. Poinsot , A 
two-step chemical scheme for kerosene–air premixed 
flames, Combust. Flame 157 (7) (2010) 1364–1373 . 
[27] R.A. Baurle , G.A. Alexopoulos , H.A. Hassan , As- 
sumed joint probability density function approach 
for supersonic turbulent combustion, J. Prop. Power 
10 (4) (1994) 473–484 . 
[28] J. Kindracki , P. Wola ´nski , Z. Gut , Experimental re- 
search on the rotating detonation in gaseous fuels–
oxygen mixtures, Shock Waves 21 (2) (2011) 75–84 . 
[29] B.A. Rankin , D.R. Richardson , A.W. Caswell , 
A.G. Naples , J.L. Hoke , F.R. Schauer , Chemi- 
luminescence imaging of an optically accessible 
non-premixed rotating detonation engine, Combust. 
Flame 176 (2017) 12–22 . 
[30] V. Anand , E. Gutmark , Rotating detonation com- 
bustors and their similarities to rocket instabilities, 
Prog. Energy Combust. Sci. 73 (2019) 182–234 . 
[31] P. Dagaut , M. Cathonnet , The ignition, oxidation, 
and combustion of kerosene: A review of experimen- 
tal and kinetic modeling, Prog. Energy. Comb. Sci. 32 
(2006) 48–92 .
