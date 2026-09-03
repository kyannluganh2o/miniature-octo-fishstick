<!-- PDF_PAGE: 1 -->

Abstract
This paper examines the combustion and emissions produced using a 
prototype fuel injector nozzle for pilot-ignited direct-injection natural 
gas engines. In the new geometry, 7 individual equally-spaced gas 
injection holes were replaced by 7 pairs of closely-aligned holes 
(“paired-hole nozzle”). The paired-hole nozzle was intended to 
reduce particulate formation by increasing air entrainment due to jet 
interaction. Tests were performed on a single-cylinder research 
engine at different speeds and loads, and over a range of fuel 
injection and air handling conditions. Emissions were compared to 
those resulting from a reference injector with equally spaced holes 
(“single-hole nozzle”). Contrary to expectations, the CO and PM 
emissions were 3 to 10 times higher when using the paired-hole 
nozzles. Despite the large differences in emissions, the relative 
change in emissions in response to parametric changes was 
remarkably similar for single-hole and paired-hole nozzles. 
Compared to the reference injector, the paired-hole nozzle produced 
larger soot aggregates and larger numbers of particles; interestingly, 
soot primary particle size did not change significantly. In addition to 
the experimental results, select experiments were modelled using 
reacting-flow computational fluid dynamics. These simulations 
suggested that the paired-hole nozzle did enhance air and fuel mixing 
during some stages of the injection and combustion event, but the net 
effect was to increase the total residence time of natural gas in the 
rich, moderate-temperature conditions needed to form soot.
Introduction
Compression-ignition (CI) engines are used in heavy-duty 
applications such as on-road trucking and marine propulsion because 
they offer higher fuel efficiency, power, and reliability than spark-
ignition (SI) engines. However, the non-premixed combustion in the 
CI engine results in higher emissions of particulate matter (PM). 
Engine exhaust PM has detrimental effects on human health [1,2], 
which has led to increasingly stringent emission standards. Replacing 
diesel fuel with natural gas can lead to reduced PM emissions, 
although if the natural gas is burned in a primarily non-premixed 
combustion event, PM is still generated in rich, high-temperature 
parts of the gas jet [3]. Here, we evaluate a technique aimed at 
reducing engine-out PM from a heavy duty engine through the use of 
a novel injector hole geometry. The novel geometry is expected to 
reduce the rich region of a non-premixed natural gas combustion 
event.
The formation of PM occurs in hot, rich regions of the cylinder [4]. 
This is the result of carbon in the fuel reacting in the rich conditions 
to form polycyclic aromatic hydrocarbons (PAHs), which then 
accumulate to form solid nano-particles. As the particles move 
through the combustion event, the local oxygen concentration 
increases, which promotes oxidation of the particles. Higher 
temperatures also promote a net increase in oxidation of the particles, 
given sufficient oxygen. Thus, the net engine-out soot results from a 
delicate balance between formation and oxidation. This process 
applies for all carbon-containing hydrocarbons; the more aromatics 
are present, the easier it is to form PAHs. However, even methane, 
despite its lack of carbon-carbon bonds, reacts under these conditions 
to form ethyl (C
2H5) radicals, which lead to acetylene and 
subsequently to aromatics.
Many approaches have been taken to reduce emissions and fuel costs 
in engines, including the use of alternative fuels. Natural gas is 
relatively inexpensive, widely available, and has low carbon dioxide 
emissions per unit of chemical energy available in the fuel. 
Composed predominantly of methane, natural gas does not reliably 
ignite under typical compression-ignition conditions and timescales 
so a separate ignition source is needed to provide robust combustion. 
Westport’s High-Pressure Direct-Injection (HPDI) of natural gas 
system uses a small diesel pilot injection (typically 5-10% diesel on 
an energy basis) to facilitate ignition of the non-premixed natural gas 
jets. This diesel pilot injection precedes the natural gas injection. The 
end of the main gas injection typically occurs shortly before the 
piston reaches top-dead-centre (TDC) of the compression stroke. 
Combustion and Emissions of Paired-Nozzle Jets in a Pilot-
Ignited Direct-Injection Natural Gas Engine
2016-01-0807
Published 04/05/2016
Christopher W. J. Mabson, Ehsan Faghani, Pooyan Kheirkhah, Patrick Kirchen,  
and Steven N. Rogak
University of British Columbia
Gordon McTaggart-Cowan
Westport Innovations Inc.
CITATION: Mabson, C., Faghani, E., Kheirkhah, P., Kirchen, P. et al., "Combustion and Emissions of Paired-Nozzle Jets in a Pilot-
Ignited Direct-Injection Natural Gas Engine," SAE Technical Paper 2016-01-0807, 2016, doi:10.4271/2016-01-0807.
Copyright © 2016 SAE International
Downloaded from SAE International by Dalian Univ of Technology, Monday, August 31, 2026

<!-- PDF_PAGE: 2 -->

While HPDI generally retains the efficiency and operating 
characteristics of a conventional diesel engine [5], the non-premixed 
combustion of the natural gas can lead to soot formation.
The fuel mixing process has a strong effect on the emissions. Gaseous 
fuel injection forms transient turbulent jets. Two parameters largely 
determine the mixture formation: jet penetration and air entrainment. 
For a single jet, air entrainment can be increased using smaller 
diameter nozzle holes however jet penetration decreases. Another 
method of increasing air entrainment is to locate several nozzle holes 
close together, causing the gaseous jets to interact. The simplest 
version of this concept is to use two holes closely located - this is 
referred to here as a ‘paired-hole’ concept. As the jets develop, they 
merge together, maintaining more momentum and greater total 
penetration length than a single small hole jet. The intention of a 
paired-hole (or ‘group-hole’, in literature) design is to use small holes 
for high entrainment and as the jets merge downstream greater 
penetration is also achieved.
Prior work on liquid diesel injection has shown potential benefits 
from grouped nozzle holes. Using a group-hole design with two jets 
that are closely spaced injecting vertically [6], it was found that the 
mass of entrained air, spray volume, and excess air ratio were greater 
for the group-nozzle than the single-hole nozzle. They found that the 
interaction of the two jets improved penetration for small angles 
compared to a single small nozzle. Further studies [7] showed that the 
group-hole nozzles could maintain penetration and increase 
evaporation of the fuel and that larger angles between the jets could 
entrain more air while penetration would decrease [8]. It is important 
to note that these studies were done in high pressure chambers and 
not in engines.
A study in an engine showed that for liquid diesel the group-hole 
nozzle could improve fuel economy up to 3% under throttled 
stoichiometric diesel conditions, but no benefits were seen for 
globally lean conditions, with high boost and high EGR [9]. This 
suggested that, for diesel engines, the benefits are only found in cases 
where the diesel spray is particularly deprived of oxygen.
Using computational fluid dynamics (CFD) it was found that larger 
angles between jets would reduce the amount of evaporation of the 
diesel jets and that the 10 degree angle was the optimal for balancing 
the total jet penetration and amount of evaporation [10]. Other work 
found that the group-hole nozzle had the same spray tip penetration 
as the conventional nozzle as each group had the same momentum 
[11]. A later study [12] showed that emissions could be improved 
with the group-hole nozzle particularly at higher equivalence ratios 
due to the ability of the spray to retain oxygen. At lower equivalence 
ratios it was no better than the conventional nozzle.
A gaseous jet does not involve the atomization and evaporation 
processes that affect air entrainment in a diesel spray. In a preliminary 
study of high pressure natural gas injection in engines, paired 
non-reacting jets were modelled [13] to study entrainment and 
penetration. Initially, the paired jet would penetrate slowly due to the 
two lower-momentum jets behaving independently and entrain more 
air [14]. A certain distance downstream the two jets merged, after 
which the penetration rate would increase due to the increased 
momentum of the combined jet. This showed that the penetration and 
entrainment of the paired jet was also dependent on whether the jet 
had reached this ‘combined point’. The use of paired jets showed that 
the peak mass fraction in a jet was lower for the pair-hole nozzle, 
which implied that it might be possible to lower soot formation as it 
is strongly affected by the local mixture fraction. However this CFD 
model did not involve real cylinder geometry (effects of 
impingement, etc.) or simulate combustion behaviour and emission 
formation. The modelling study was used to define the injector 
geometries used in the current work.
The overall objective of the present work is to evaluate the effect of 
paired jets on the performance and emissions of an HPDI engine. The 
four specific objectives were as follows: 
1. Evaluate combustion performance and emissions in an HPDI 
engine of various pair-hole nozzle designs at distinct engine 
operating modes and select one nozzle for further examination. 
2. Determine whether the emissions generated using the pair -hole 
nozzle have the same parametric sensitivity as the emissions 
from the conventional single-hole nozzle. 
3. Compare engine-out soot characteristics and morphology 
between the pair-hole nozzle and a baseline, conventional 
reference nozzle. 
4. Use reacting-flow CFD simulations of the experimentally-tested 
conditions as a tool to help explain the observed impacts on PM 
and CO emissions.
Methods
Experimental
The core of the HPDI fuel system is the two-fuel injector. It uses 
concentric gas and diesel needles (Figure 1) that can be controlled 
separately. This permits independent control of the length and timing 
of the pilot and main injection events discussed earlier. The injectors 
used in this work are research-level prototypes derived from 
Westport’s 1st generation HPDI injector, used in the CARB/EPA 
2010-certified 15L HD commercial heavy-duty HPDI engine product. 
A baseline (“reference”) injector was configured with 7 gas holes and 
7 diesel pilot holes, while the paired-hole injectors were configured 
with 7 pilot and 14 gas holes, distributed in pairs. Figure 2 shows the 
end view of the nozzles for the reference and pair-hole injectors 
(diesel pilot hole alignment is indicated by centre dotted line but the 
holes are not shown in this schematic). For all the injectors used in 
this work the angle between the gas and diesel holes and the cylinder 
fire deck was 18 degrees. A dotted line is added to the reference 
nozzle to compare alignment with the pair-hole jets.
Downloaded from SAE International by Dalian Univ of Technology, Monday, August 31, 2026

<!-- PDF_PAGE: 3 -->

Figure 1. Cross section of HPDI injector.
Figure 2. End view of reference and paired-hole nozzle. Not to scale.
The orientation of the nozzle holes is fixed so that the diesel hole has 
a constant angle with the gas holes. It is either centred between the 
two gas holes (pair-hole nozzle) or aligned with the diesel jet 
(reference injector). Table 1 shows the dimensions for the pair-hole 
nozzle designs and the reference injector. The nozzles are identified 
by the size of the gas holes and angle between the gas holes (e.g., 
small-hole-large-angle pair-hole nozzle or SHLA). The small-hole 
(SH) pair-hole nozzles have the same total gas hole flow area as the 
reference injector while the large-hole (LH) nozzles have 20% extra 
total flow area (area is implicit in the standardized flow tests reported 
in Table 1). The increased flow area was selected to achieve total 
penetration similar to that of the reference injector. The angle 
between the holes in each pair was set to be 10 (small angle, SA) or 
18 degrees (large angle, LA). These angles and hole sizes were 
selected based on non-reactive CFD simulations which indicated that 
the jets would merge during the injection period [13]. Larger angles 
were expected to increase entrainment while sacrificing penetration 
due to later merging of the jets.
Table 1. Nozzle specifications
Injection command timing is depicted in Figure 3. Typically, diesel 
fuel is injected before the natural gas. The time of injection is 
specified by the Pilot Start of Injection (PSOI) signal and its duration 
is determined by the Pilot Pulse Width (PPW). The commanded delay 
between the (diesel) end of injection and the gas injection is specified 
by the Pulse Separation (PSEP) and sets the Gas Start of Injection 
(GSOI). Typical (“conventional”) HPDI combustion uses PSEP > 
0ms. The length of the gas injection is defined by the Gas Pulse 
Width (GPW). The fuel injection quantity is a function of GPW, gas 
rail pressure (GRP), and cylinder pressure during the injection.
Figure 3. Typical HPDI injection strategy
All tests performed in this work were on the UBC SCRE (Single 
Cylinder Research Engine, Figure 4). The SCRE is a 6-cylinder 
four-stroke ISX heavy duty diesel engine that has been modified to 
run on one cylinder and in an HPDI configuration. Each cylinder has 
a displacement of 2.5 liters (bore 137mm, stroke 169mm, connecting 
rod length 262mm). The compression ratio is 17:1. The engine uses 
an internal common rail and has dummy injectors installed in the 5 
non-fired cylinders. The valves in the non-firing cylinders are bolted 
shut with the rocker arms removed. Additionally, the deactivated 
pistons are installed with only 1 piston ring to minimize friction.
Figure 4. Single Cylinder Research Engine (SCRE).
An electric motor and water-cooled eddy current dynamometer are 
used to set speed and load. The motor provides additional torque 
when needed due to the increased friction caused by the pistons in the 
deactivated cylinders.
Downloaded from SAE International by Dalian Univ of Technology, Monday, August 31, 2026

<!-- PDF_PAGE: 4 -->

A compressor and dryer supply air to the intake manifold at pressures 
comparable to those of a turbocharged engine. Airflow rate is 
measured with a venturi and confirmed with a hot film anemometer. 
Cooled exhaust gas recirculation (EGR) is used to dilute the intake 
charge. The charge passes through an intake surge tank to dampen 
pressure pulses. Fuel is supplied to the HPDI injectors through the 
engine’s internal fuel rails. Diesel flow is measured gravimetrically 
while natural gas flow is measured using a Coriolis flow-meter. The 
pressure in the diesel rail is fixed at approximately 5-10 bar above the 
pressure in the gas rail for all operating conditions. The flow rates of 
diesel, natural gas, air and EGR, along with the oxygen concentration 
in the EGR, are used to calculate the bulk-average equivalence ratio 
(EQR).
Engine load (characterized by gross indicated mean effective 
pressure, GIMEP) and apparent heat release rates [15] are based on 
measurements from a Kistler 6067C water-cooled piezoelectric 
pressure transducer that is pegged to intake pressure at intake valve 
closing. The heat-release rate is also integrated to provide a 
cumulative heat release; the mid-point of the integrated heat release 
(50% IHR) is used to define combustion phasing. Engine load is 
characterized using GIMEP due to the non-firing cylinders. Further 
details to the engine and test cell setup are provided elsewhere 
[16,17].
The gaseous emissions are measured with an A VL CEB II Emissions 
Bench. Hydrocarbon emissions are measured using a flame ionization 
detector. NO
x emissions are measured with a chemiluminescent 
detector. CO and CO2 are measured with a non-dispersive infrared 
gas analyzer. For measuring PM emissions, the sample exhaust is 
diluted using a 2-stage ejector diluter and aging chamber. The 
dilution ratio is found by comparing the CO2 concentration in the 
exhaust stream and that measured after dilution using a California 
Analytical Instruments Infrared Analyzer (Model 100); dilutions of 
10-15:1 were used in this work.
The diluted sample is fed to a series of instruments for PM 
measurement. Total mass is measured using a tapered element 
oscillating microbalance (TEOM). The volatile content is then 
removed in a thermodenuder [16] and measured with a DustTrak 
DRX. For this work, the DRX is the primary instrument for PM 
measurement and the trends are confirmed with the TEOM.
More detailed analysis of the particulate sizing and structure was 
conducted using a long-column TSI 3080 long-column scanning 
mobility particle spectrometer (SMPS), [18] and Transmission 
Electron Microscopy (TEM). For the size distributions, the mode was 
determined by fitting a lognormal curve to the data, and using the TSI 
software AIM (with multiple charge correction). A UBC-developed 
thermophoretic sampler (TPS) was used to collect PM onto copper 
TEM grids. The samples were imaged using with a Hitachi H7600 
TEM. An image processing code was used to measure the primary 
particles [19]. SMPS and TEM samples were taken from the denuded 
stream (i.e. after volatile species were removed).
Computational Fluid Dynamics
Reacting CFD simulation was used to model specific operating 
conditions and injectors, with the principal objective of better 
understanding the experimental results.
Modelling of the paired-jet combustion was done with a 
Westportdeveloped CFD package [20,21]. This package is built on 
the OpenFOAM fluid dynamics solver with additional features to 
model the natural gas and diesel combustion and high-pressure gas 
injection. Particulate formation and oxidation is estimated by a 2-step 
empirical model based on the Hiroyasu model [22]. The gas phase 
chemical kinetic mechanisms were implemented with a trajectory-
generated low-dimensional manifold method [23]. The manifolds 
were generated using detailed chemical kinetic mechanisms for 
natural gas and heptane. A 71-species, 379-reaction modified GRI 
mechanism was used for natural gas accounting for methane, ethane, 
and propane. For heptane, the 170-species, 1500-reaction Lawrence 
Livermore National Lab mechanism was used. The chemistry-
turbulence interactions were modelled using the Chemical Source-
term Estimation (CSE) method [24]. The flow-turbulence interactions 
were modelled using large-eddy-simulation (LES) with an extra 
equation for the sub-grid scale kinetic energy. This software has been 
used extensively by Westport to predict in-cylinder pressure, heat 
release rates, and gaseous and PM emissions in various studies 
[20,21,25].
To reduce the computational time, only 1/7 of the combustion 
chamber and one set of injector holes (out of 7) were simulated. A 
periodic boundary condition at the left and right edges of the slice 
were used to model the effect of neighbouring slices assuming that all 
slices were similar. The number of CFD cells changed during the 
piston motion to maintain a reasonable cell aspect ratio and Courant 
number. For the current study, the simulations started with 
approximately 130,000 cells at -90° aTDC.
Description of Tests and Simulations Performed
Multi-Mode
All injectors were tested twice on 5 combinations of speed and load 
(Table 2). These conditions were defined specifically for the SCRE to 
be representative of points from the European Stationary Cycle. They 
were selected to be similar to multi-cylinder engine conditions but are 
not specifically matched to any specific multi-cylinder engine 
operating mode. The modes are labelled by speed (low to high A, B, 
C) and the load (approx. % of full load).
Table 2. Multi-mode test matrix. Reference single-hole nozzle and 4 
paired-hole nozzle injectors.
Downloaded from SAE International by Dalian Univ of Technology, Monday, August 31, 2026

<!-- PDF_PAGE: 5 -->

Parameter Sweeps
Sweeps of engine parameters were performed around the B75 point 
(Table 3). Each parameter sweep was run twice for the reference 
injector and the paired hole nozzle selected for detailed evaluation 
(this was the LHSA pair-hole nozzle, as will be discussed).
Table 3. Parameter sweeps test matrix. Reference single hole nozzle and 
LHSA paired nozzle. Parentheses note baseline points. GRP was 25.4MPa for 
these points.
B75 Response Surfaces
Interactions between key parameters were also compared between the 
reference injector and the pair-hole nozzle injector selected for 
detailed analysis. The parameter sweeps shown in Table 3 focused on 
individual responses. To develop an understanding between the 
interactions of key parameters, a full factorial test (Table 4) was 
conducted. This involved 108 test conditions. Due to the size of the 
test matrix, individual test conditions were not replicated. Response 
surfaces were then generated by combining the parameter sweep test 
results and the full factorial tests.
Table 4. B75 full factorial matrix (EGR, GRP, 50% IHR, PSEP). Reference 
single hole nozzle and LHSA paired nozzle.
The response surface is similar to ones produced earlier for this 
engine [16,26]. The method is based on a first order system [27] that 
uses second order terms for some pairs of the parameters.
The dependent variables were the PM and CO emissions. All 
parameters were assumed to have linear responses with the emissions 
except for PSEP and 50% IHR which assumed second order 
dependence. This is due to the parabolic response seen on these 
parameter sweeps for PM emissions. The model is evaluated based on 
the R
2 value and its response over the dataset. The Appendix provides 
details.
CFD Cases
The reacting-flow CFD model was used to predict the heat release 
rates (HRR) and emissions in mode B75 for the reference and the 
paired-hole injectors. After confirming that the predicted trends 
matched the measurements [28], the CFD simulation was used to 
provide estimates of the different injectors. Table 5 includes the 
experimental data that was used for the simulations taken from the 
B75 baseline engine points. The delay between sending the injection 
command pulses and the actual injection of fuel were assumed based 
on prior work with different injectors in a high-pressure chamber 
[29]. However, further adjustments, such as interlace angle between 
gas and diesel jets (based on magnified injector tip images), were 
needed to match the 50% IHR with experimental data [30].
Table 5. Inputs for the reacting-flow CFD simulations
Results and Discussion
The apparent heat release rates (HRR) for the pair-hole nozzle and 
reference injector are presented (average of 45 cycles) for mode B75 
in Figure 5. The initial spike in the apparent heat release is the 
ignition and combustion of the pilot diesel (-15 to -5 CA degrees after 
TDC); this is similar for all injectors. Initial combustion of the natural 
gas is seen at about -2 to 5 CA degrees aTDC. The coefficient of 
variation of the maximum cylinder pressure for the 45 cycles was less 
than 1%, which is typical of B75 for the reference injector. The 
differences resulting from the different nozzle geometry are thus 
significant.
Downloaded from SAE International by Dalian Univ of Technology, Monday, August 31, 2026

<!-- PDF_PAGE: 6 -->

Figure 5. B75 apparent heat release rates for 4 paired-hole nozzles compared 
to reference HPDI injector nozzle.
The HRR for the reference injector appears similar to classic 
non-premixed combustion [15]. There is a smooth transition from 
initial combustion of natural gas that has premixed prior to being 
ignited, through the later combustion, which is mainly mixing 
controlled. The paired injectors look considerably different during 
this transition and this can be attributed to the different mixing 
phenomena of the paired nozzle. For SHLA, LHSA, and LHLA the 
HRR drops more quickly from the peak value than did the reference 
injector. This indicates a more distinct transition between premixed 
and mixing-controlled combustion phases for these nozzles. The 
SHSA produces a double peak in its HRR. This phenomenon occurs 
every engine cycle and at other engine modes and could indicate that 
the mixing process for this nozzle is quite different from the reference 
nozzle. At approximately 10 CA degrees aTDC the HRR for all the 
injectors falls onto the same curve. This indicates that very late 
combustion events are not significantly influenced by the nozzle 
geometry.
Multi-Mode Tests
The emissions for the multi-mode tests are in Table 6. Each value 
represents an average of 2 engine tests.
All of the pair-hole nozzles result in more PM than the reference 
injector. At B25, post-denuder PM concentrations for all injectors are 
very low and are close to the DRX’s lower detection limit.
The relative ranking of the injectors based on PM emissions is 
surprisingly consistent across operating modes. Given that the modes 
are drastically different from each other (different GRP, PSEP, 50% 
IHR, speed, and load), it appears that the high PM emissions from the 
pair-hole nozzles are caused by fundamental aspects of the nozzle 
geometry and not, for example, the manner in which the jets interact 
with the piston bowl walls.
Table 6. Multi-mode emissions for all paired-hole nozzles and reference 
nozzle, note all work is reported as gross. Emissions are in [mg/kWh]g for PM 
and [g/kWh]g otherwise.
CO emissions for the pair-hole nozzle are also significantly higher 
than the reference injector, especially for the SHSA injector. As 
discussed in the Appendix, CO and PM are tightly correlated for a 
wide range of conditions, despite the much higher values from the 
pair-hole nozzles.
Unlike CO and PM, NO
x and methane emissions are affected much 
less by the pair-hole design. However all paired nozzle designs seem 
to reduce NOx formation across all modes, suggesting lower 
temperatures in the reaction zones or shorter residence times in the 
post-combustion gases. These effects could align with reduced 
oxidation rates of PM, however this is speculative at this point. Of the 
injector nozzle geometries tested, the LHSA and SHLA PM 
emissions were significantly lower than the LHLA and SHSA 
nozzles. Of these, the LHSA nozzle was selected for further analysis 
due to its PM emissions being low and more repeatable than the 
SHLA.
Emissions Characterization with Parameter Sweeps
Parameter sweeps changing 50% IHR, EGR %, EQR, diesel pilot 
mass, and PSEP were studied for the reference and LHSA injectors at 
mode B75. The results for all sweeps except the pilot sweep are 
included in Figure 6.
The parabolic trend in PM with timing has been frequently observed 
with this engine at moderate and high-load operating conditions 
[16,31]. The parabolic result has been attributed to the relative timing 
of the impingement of the gas jet on the piston bowl wall, and 
corresponding ‘splitting’ of the reacting gas jet between the bowl and 
the squish region. As the figure shows, there is no timing where PM 
emissions for the pair-hole nozzle become comparable to the 
reference nozzle. In fact the relative trends are remarkably similar for 
the different injectors, with simply a significant increase for the 
pair-hole cases.
Downloaded from SAE International by Dalian Univ of Technology, Monday, August 31, 2026

<!-- PDF_PAGE: 7 -->

Figure 6. 50% IHR sweep (top left), PSEP sweep (top right), EGR Sweep 
(bottom left), EQR sweep (bottom right) for LHSA and reference nozzle. 
Sweeps around B75 parameters from Table 2.
Adjusting the relative timing between the natural gas and pilot 
injection (PSEP) gives the gaseous fuel time to mix with air before it 
is ignited; this can greatly reduce PM in HPDI, as has been shown 
previously [21]. Based on the present work, the benefits are most 
evident for PSEP values less than -0.4ms. Interestingly, PM levels for 
the pair-hole nozzle become comparable to the reference injector 
once the PSEP is less than -1.1ms. For PSEP values earlier than this, 
PM levels are extremely low (<10 mg/kWh). This is attributed to the 
bulk of the gas jet having mixed to local equivalence ratios below 
those needed to form soot prior to ignition occurring. This optimal 
timing is the same for both injectors.
The sensitivity of other emissions and performance parameters to 
PSEP are not shown here, but in general the trends for both base and 
paired-hole nozzles were equivalent to those reported in previous 
studies [21]. For all injectors tested, NO
x emissions increase with 
reduced PSEP but remain comparable to the reference nozzle over the 
entire sweep. Methane emissions increase for the pair-hole nozzle 
more than the reference nozzle. This may indicate that more mixing 
may be occurring due to the paired jets. The nozzle geometry did not 
significantly influence peak rate of pressure rise, which generally 
increases with more negative PSEP values. Similarly, improvements 
in GISFC with more negative PSEP values were equivalent for the 
different injectors studied.
EGR tends to increase PM as oxygen is displaced with an inert gas; 
this has been shown widely for both diesel and HPDI of natural gas 
engines [32, 33, 34]. As expected lower EGR results in lower PM 
from the pair-hole nozzle. The PM at 0% EGR is on the same order 
as the PM levels at 25% EGR level tested with the reference nozzle.
PM emissions are reduced by 50% for both injectors as oxygen 
equivalence ratio (EQR) is reduced from 0.75 to 0.5. CO emissions 
show the same reduction. NO
x drops as the global equivalence ratio 
becomes richer due to a drop in oxygen concentration that reduces 
NOx formation. The tight coupling of CO and PM for all injectors is 
shown graphically in the Appendix. This is interesting because CO 
and PM form from different chemical mechanisms and it is possible 
to break this correlation (for example, at negative PSEP, PM is 
reduced far more than CO).
As diesel pilot quantity is increased PM and CO emissions increase 
for both injectors. An explanation for this phenomenon is due to the 
importance of how the pilot affects the distribution of the ignition 
event and this can affect the amount of mixing of natural gas with air 
prior to ignition. The same increased emissions for the LHSA but 
similar behaviour was seen in this sweep.
The mobility size distribution, projected area, and primary particle 
size of PM resulting from the LHSA paired-hole nozzle and reference 
injector were compared at the B75 condition. Sample TEM images 
produced for both nozzles are illustrated in Figure 7. The LHSA 
injector has larger aggregates than the reference injector at the B75 
point with a geometric mean mobility diameter of approximately 
125nm vs. 85nm for the reference injector. The primary particle size 
for both nozzles is approximately the same at about 18nm in 
diameter, as calculated using an automated optical analysis procedure 
for particle sizing (PCM code) [19]. This similarity suggests that the 
local soot formation conditions resulting from the two nozzles are 
actually similar, despite the very large difference in exhaust 
emissions.
Based on the SMPS measurements, the LHSA nozzle produces higher 
number concentrations of particles. Higher concentrations result in 
faster coagulation (assuming identical dilution history) which is 
consistent with our observation that the mobility diameter and 
aggregate areas are higher for particles from the LHSA injector. The 
mobility size distributions for the two injectors are broad and 
overlapping, so it is not surprising that the two sample particles in 
Figure 7 appear to have similar size. A conceptual model that 
reconciles the nearly constant primary particle size with changed 
aggregate size is that both injectors produce similar soot forming 
zones but the pair-hole nozzle produces more of these zones, or zones 
of greater size.
Figure 7. Soot aggregates from reference nozzle and LHSA paired-hole 
nozzle.
Response Surfaces for Mid-Speed High-Load
Response surfaces for emissions were produced from the B75 
measurements, combining the parameter sweeps discussed previously 
and the full-factorial test described in Table 4. To analyze the 
sensitivity of the 2 injectors, 6 engine parameters were adjusted to 
show the dependency of each individual parameter and when 
changing 2 parameters together.
Downloaded from SAE International by Dalian Univ of Technology, Monday, August 31, 2026

<!-- PDF_PAGE: 8 -->

A table with the coefficients for all the surfaces is provided in the 
Appendix for reference. The R2 value for the LHSA PM surface was 
found to be 0.75, which indicates that a significant part of the overall 
variability in the results is not explained by the terms in the model. 
This may be due to excluded interactions, or by systematic variables 
that were controlled but not included in the model. The model 
incorporates all the control parameters used in the testing, and as 
higher-order interactions are generally found to be small, this 
suggests that most of the uncertainty can be attributed to 
measurement and day-to-day engine performance variability.
Interactions between parameters were only considered for the timing 
variables (50% IHR, PSEP). Table 7 shows the percent emission 
change when the input variables are increased by 10% from the 
baseline B75 value. The entries on the diagonal consider one variable 
at time; off-diagonal entries show the effects of changing two 
parameters at a time. For the pairs whose interactions are modeled, 
the number in the table is the % change above the simple sum of the 
diagonals. For example, a 10% change in EQR and 50% IHR results 
in an increase of 76%-7%+23%=92%.
Table 7. Change (%) in PM (by DRX) to a 10% change in parameters. 
Off-diagonal entries indicate the interaction effect (beyond a simple additive 
effect).
a) Reference injector R2=0.65
b). LHSA injector R2=0.75
EQR and GRP have the strongest influences for both nozzles, 
unsurprisingly. PSEP has a stronger influence for the paired nozzle, 
probably due to the larger difference between the baseline PM and 
PM from most negative PSEP. In both models, an important 
interaction indicated by the model is that between 50% IHR and 
EQR. For the reference nozzle, increasing both parameters results in 
a greater increase in total PM than would be expected from the 
factors individually. For the LHSA model, however, the opposite 
effect is seen, where the combined effect results in lower emissions 
than what would be expected from a summation of the individual 
effects alone.
P-Values were generated for the coefficients determined in this model 
and for the CO models. They were generated using an analysis of 
variance (ANOV A) method to isolate the important interactions 
between PSEP and IHR with the other parameters. This is included 
with the coefficients in Table A2 in the Appendix. PValues represent 
the likelihood that the null hypothesis can be rejected. In this case the 
null hypothesis is whether a coefficient is 0. Using this test at 95% 
confidence, most of the linear terms can be included in this model 
with the exception of the linear IHR term which is sensitive to the x
2 
term. The interaction of PSEP and IHR with the other parameters is 
explored and many of the interactions can be dismissed by this model 
except notably for the EGR*PSEP term which is significant for the 
CO models as well. For many of the less statistically significant 
parameters, the size of the dataset changing these variables alone is 
small.
With 18 fitted parameters for 108 test points, the results of the fit 
must be considered with caution, but the sensitivities are consistent 
with the parametric sweep tests shown earlier. Furthermore, the 
response surfaces for CO are very similar to those for PM (see 
Appendix for more information), indicating that the regression is not 
solely sensitive to PM measurement noise [28].
Computational Fluid Dynamics (CFD) Results
The B75 baseline condition was simulated using the conditions 
shown in Table 5 for the reference and LHSA paired-hole nozzles. 
Figure 8 shows the predicted HRR and corresponding engine 
measurements. The start of combustion, the initial peak in the HRR, 
and the overall combustion event are well predicted. The higher 1
st 
peak for the reference injector and the predicted 2nd peak for the 
LHSA injector may be a result of simulating only 1/7th of the 
combustion chamber. In the real engine, slight differences in the 
timing of the 7 jets would blur the peaks of the HRR - a possible 
reason that the CFD model predictions for the reference injector show 
sharper spikes than measured in the SCRE. The predicted changes in 
CO and PM emissions (Appendix) are smaller than measured, hence 
the remainder of the discussion focusses on jet mixing and 
penetration - aspects of the process that are less sensitive to the 
chemical mechanisms and closure.
The intention of the paired-hole nozzle concept was to increase air 
entrainment into the gas jet. This can be evaluated from the CFD 
results by comparing the penetration and air entrained into the jets, as 
shown in Figure 9. The overall mixing process is dominated by two 
effects: the axial penetration of the gas jet and the amount of air 
entrained into the jet. Here, penetration is defined as the distance 
from the injector to the centerline stoichiometric contour, while the 
entrainment is characterized by the mass of air within the 
stoichiometric envelope normalized by the total injected fuel mass.
Downloaded from SAE International by Dalian Univ of Technology, Monday, August 31, 2026

<!-- PDF_PAGE: 9 -->

Figure 8. Comparison of CFD model HRR with SCRE measurement for the 
reference nozzle (top) and LHSA (bottom).
Figure 9. Normalized air entrainment as a function of jet penetration from B75 
CFD simulations. The jet penetration as a function of time after injection is 
indicated by the labels (in crank angle degrees).
The simulations indicated that the rate of penetration of the jet from 
the pair-hole nozzle is slower than for the reference injector (Figure 
9, comparing equal values of CAD). However, if the entrainment is 
plotted relative to penetration distance it is clear that the LHSA has 
entrained more air for an equal amount of penetration. In this sense, 
the objective of enhancing early entrainment of air was achieved.
As the experimental results showed, total PM emissions increased. 
This can be explained by looking at the mass of fuel atoms (mixture 
fraction) as a function of time at a local equivalence ratio, ϕ
g, that 
would be conducive to soot formation. The local equivalence ratio is 
defined on a natural gas basis, hence the subscript “g”. The soot 
forming zone is defined as 2<ϕg<6, based on the Equivalence 
ratio-Temperature map for methane combustion discussed in the 
Appendix. Figure 10 shows the amount of natural gas atoms 
(normalized by total injected mass of gas) in three ϕg ranges: very 
rich (ϕg>6), soot-forming (2<ϕg<6), and lean (ϕg<2). The enhanced 
air entrainment of the LHSA injector exhibited in Figure 9 is 
associated with larger quantities of fuel at local ϕg’s that are 
conducive to soot formation. The normalized mixture is defined with 
the subscripts “l” and “u” denoting the lower and upper ϕ
g limits and 
mg is the mass of gas at each CFD cell.
The mixture of fuel in the very rich zone and lean zone shows only 
small differences between the two nozzles. This seems to result from 
the slightly lower penetration rates of the LHSA jets and from the 
geometry of the merging jets, which produces large volumes of 
partially mixed fuel.
Figure 10. Distribution of cylinder composition through the combustion cycle.
Conclusions
Soot formation is typically highest in the rich burning regions of a 
non-premixed flame, so we expected that an injector nozzle designed 
to increase early air entrainment into the jet should reduce soot 
emissions. To increase air entrainment, a conventional single hole 
was replaced by a pair of smaller, closely aligned holes. Engine tests 
were conducted to evaluate this strategy in a heavy duty, non-
premixed, direct injection of natural gas engine with pilot ignition. 
These results were then further evaluated using reacting CFD 
simulation of the specific conditions tested.
It was found that non-volatile PM emissions were increased by a 
factor of 3 to 10 for different paired-hole nozzle geometries, relative 
to a single-hole reference injector, over a range of moderate and 
high-load operating conditions. For the four paired-hole injectors 
tested, the increases in PM relative to the reference injector were 
lowest and PM levels were most consistent for the injector with larger 
holes that were closer together (LHSA).
A study of injection and air handling system parameters indicated that 
the percent changes in PM in response to these parameters were very 
similar for all injectors despite the large differences in absolute 
emissions. Carbon monoxide followed similar trends to PM 
emissions and followed the same trajectory for all injectors. The only 
condition where paired-hole PM emissions were similar to those of 
the base injector case was when the gas injection preceded the diesel 
pilot. In this case, the gas premixed to such an extent that PM 
emissions were extremely low. As a result, for this case the sensitivity 
to the local gas jet dynamics was substantially reduced.
Downloaded from SAE International by Dalian Univ of Technology, Monday, August 31, 2026

<!-- PDF_PAGE: 10 -->

Aggregate and primary particle sizing through TEM and SMPS 
measurements indicated that the pair-hole nozzle generated larger 
soot aggregates and larger numbers of aggregates. This agrees with 
the larger PM mass for the pair-hole nozzles seen in the rest of this 
work. The primary particle sizes were found to be similar for the 
single and paired-hole nozzles for the conditions evaluated.
Reacting CFD simulations were run to compare the LHSA paired-
hole nozzles with the reference injector. The results indicated that the 
paired-hole geometry resulted in more of the fuel in the gas jets 
spending a longer period of time at local equivalence ratios between 
2 and 6 that are most conducive to PM precursor formation. This is a 
result of the trade-off between increased air entrainment and slower 
gas jet penetration with the paired-hole nozzles.
Our observation that all injectors responded similarly to parametric 
changes, showed similar patterns of PM and CO emissions, and 
produced soot aggregates of similar structure (albeit different size) 
suggests that soot is formed in similar conditions for all injectors. The 
large differences in the magnitude of emissions might arise from the 
different extent of the soot forming zones resulting from different 
injectors. This is borne out by the CFD simulations, which showed 
shifts in entrainment and jet penetration. As desired, the pair-hole 
nozzles increased early air entrainment, but this had the undesirable 
effect of putting more of the fuel into the soot-forming mixture ratio, 
producing more soot. Although this study considered only high 
pressure gas injectors, the consistency of the results - through 
emission patterns and CFD - suggest that the lessons here may be 
transferable to other types of combustion systems.
References
1. Silverman, D.T ., Samanic, C.M., Lubin, J.H., and Blair, A.E., 
“The Diesel Exhaust in Miners study: a nested case-control 
study of lung cancer and diesel exhaust.,” J. Natl. Cancer Inst. 
104(11):855-68, 2012, doi:10.1093/jnci/djs034.
2. Giechaskiel, B., Alföldy, B., and Drossinos, Y ., “A metric for 
health effects studies of diesel exhaust particles,” J. Aerosol Sci. 
40(8):639-651, 2009, doi:10.1016/j.jaerosci.2009.04.008.
3. Jones, H., McT aggart-Cowan, G., Rogak, S., Bushe, W. et al., 
"Source Apportionment of Particulate Matter from a Diesel 
Pilot-Ignited Natural Gas Fuelled Heavy Duty DI Engine," SAE 
Technical Paper 2005-01-2149, 2005, doi:10.4271/2005-01-
2149.
4. T ree, D.R. and Svensson, K.I., “Soot processes in compression 
ignition engines,” Prog. Energy Combust. Sci. 33(3):272-309, 
2007, doi:10.1016/j.pecs.2006.03.002.
5. McT aggart-Cowan, G.P., “Pollutant Formation in a Gaseous-
Fuelled, Direct Injection Engine,” PhD Thesis, The University 
of British Columbia, 2006.
6. Zhang, Y ., Nishida, K., Nomura, S., and Ito, T., "Spray 
Characteristics of Group-hole Nozzle for D.I. Diesel Engine," 
SAE Technical Paper 2003-01-3115, 2003, doi:10.4271/2003-
01-3115.
7. Gao, J., Matsumoto, Y ., Namba, M., and Nishida, K., "Group-
Hole Nozzle Effects on Mixture Formation and In-cylinder 
Combustion Processes in Direct-Injection Diesel Engines," SAE 
Technical Paper 2007-01-4050, 2007, doi:10.4271/2007-01-
4050.
8. Moon, S., Gao, J., Nishida, K., Matsumoto, Y . et al., "Ignition 
and Combustion Characteristics of Wall-Impinging Sprays 
Injected by Group-Hole Nozzles for Direct-Injection Diesel 
Engines," SAE Int. J. Engines 1(1):1205-1219, 2009, 
doi:10.4271/2008-01-2469.
9. Kim, J., Park, S., Andrie, M., Reitz, R. et al., "Experimental 
Investigation of Intake Condition and Group-Hole Nozzle 
Effects on Fuel Economy and Combustion Noise for 
Stoichiometric Diesel Combustion in an HSDI Diesel Engine," 
SAE Int. J. Engines 2(1):1054-1067, 2009, doi:10.4271/2009-
01-1123.
10. Nishida, K., Tian, J., Sumoto, Y ., and Long, W., “An 
experimental and numerical study on sprays injected from two-
hole nozzles for DISI engines,” Fuel 88(9):1634-1642, 2009, 
doi:10.1016/j.fuel.2009.01.003.
11. Park, S. and Reitz, R., “Modeling the ef fect of injector 
nozzle-hole layout on diesel engine fuel consumption and 
emissions,” J. Eng. Gas Turbines Power 130(3):032805, 2008, 
doi:10.1115/1.2835352.
12. Park, S. and Reitz, R., “Optimization of fuel/air mixture 
formation for stoichiometric diesel combustion using a 
2-sprayangle group-hole nozzle,” Fuel 88(5):843-852, 2009, 
doi:10.1016/j.fuel.2008.10.028.
13. Faghani, E. and Rogak, S.N., “Penetration and Flow Field 
Characteristics of Dual-Hole Transient Gas Jets,” Proceedings 
of Combustion Institute Canadian Section Spring Technical 
Meeting (CICS 2011), Winnipeg, Canada, 2011.
14. Nasr , A. and Lai, J.C.S., “Two parallel plane jets: mean flow and 
effects of acoustic excitation,” Exp. Fluids 22(3):251-260, 1997, 
doi:10.1007/s003480050044.
15. Heywood, J.B., “Internal Combustion Engine Fundamentals,” 
McGraw-Hill, New York, ISBN 007028637X, 1988.
16. Patychuk, B., “Particulate matter emission characterization from 
a natural-gas high-pressure direct-injection engine,” MASc. 
Thesis, The University of British Columbia, 2013.
17. Brown, S., “High-pressure Direct-Injection of Natural Gas with 
Entrained Diesel into a Compression-Ignition Engine,” MASc. 
Thesis, The University of British Columbia, 2008.
18. W ang, S.C. and Flagan, R.C., “Spectrometer Scanning 
Electrical Mobility Spectrometer,” (July 2014):37-41, 2007, 
doi:10.1080/02786829008959441.
19. Dastanpour , R., Boone, J., and Rogak, S., “Automated Primary 
Particle Sizing of Nanoparticle Aggregates by TEM Image 
Analysis,” Submitt. to J. Powder Technol, 2015.
20. Munshi, S.R., McT aggart-Cowan, G., Huang, J., and Hill, P.G., 
“Development of a Partially-Premixed Combustion Strategy for 
a Low-Emission, Direct Injection High Efficiency Natural Gas 
Engine,” Proceedings of the ASME 2011 Internal Combustion 
Engine Division Fall Technical Conference, 1-14, 2011.
Downloaded from SAE International by Dalian Univ of Technology, Monday, August 31, 2026

<!-- PDF_PAGE: 11 -->

21. McT aggart-Cowan, G.P., Mann, K., Huang J., Wu, N. et al., 
“Particulate Matter Reduction From a Pilot-Ignited, Direct 
Injection of Natural Gas Engine,” Proceedings of the ASME 
Internal Combustion Engine Division’s 2012 Fall Technical 
Conference, Vancouver, Canada: 1-11, 2012.
22. Nishida, K. and Hiroyasu, H., "Simplified Three-Dimensional 
Modeling of Mixture Formation and Combustion in a 
D.I. Diesel Engine," SAE Technical Paper 890269, 1989, 
doi:10.4271/890269.
23. Maas, U. and Pope, S.B., “Simplifying chemical kinetics: 
Intrinsic low-dimensional manifolds in composition space,” 
Combust. Flame 88(3-4):239-264, 1992, doi:10.1016/0010-
2180(92)90034-M.
24. Steiner , H. and Bushe, W.K., “Large eddy simulation of a 
turbulent reacting jet with conditional source-term estimation,” 
Phys. Fluids 13(3):754, 2001, doi:10.1063/1.1343482.
25. McT aggart-Cowan, G., Mann, K., Huang, J., Singh, A. et al., 
"Direct Injection of Natural Gas at up to 600 Bar in a Pilot-
Ignited Heavy-Duty Engine," SAE Int. J. Engines 8(3):981-996, 
2015, doi:10.4271/2015-01-0865.
26. Laforet, C., “Combustion of Natural Gas with Entrained Diesel 
in a Heavy-Duty Compression-Ignition Engine,” MASc. Thesis, 
The University of British Columbia, 2009.
27. Myers, R.H., Montgomery , D.C., and Anderson-Cook, C., 
“Response Surface Methodology: Process and Product 
Optimization Using Designed Experiments ,” ISBN 
0470174463, 2009.
28. Mabson, C.W .J., “Emissions Characterization of Paired Gaseous 
Jets in a Pilot-Ignited Natural-Gas Compression-Ignition 
Engine,” MASc. Thesis, The University of British Columbia, 
2015.
29. Faghani, E., Kirchen, P ., and Rogak, S., "Application of Fuel 
Momentum Measurement Device for Direct Injection Natural 
Gas Engines," SAE Technical Paper 2015-01-0915, 2015, 
doi:10.4271/2015-01-0915.
30. Kheirkhah, P ., “CFD modeling of injection strategies in a High-
Pressure Direct- Injection (HPDI) natural gas engine,” MASc 
Thesis, The University of British Columbia, 2015.
31. McT aggart-Cowan and Rogak, S., “Effect of operating 
condition on particulate matter and nitrogen oxides emissions 
from a heavy-duty direct injection natural gas engine using 
cooled exhaust gas,” Int. J. Engine Res. 5(6):499-511, 2004, 
doi:10.1177/146808740400500602.
32. McT aggart-Cowan, Bushe, and Rogak, “Injection parameter 
effects on a direct injected, pilot ignited, heavy duty natural gas 
engine with EGR,” SAE Trans. (724), 2003.
33. Kreso, A., Johnson, J., and Gratz, L., “A study of the effects 
of exhaust gas recirculation on heavy-duty diesel engine 
emissions,” (724), 1998.
34. Lee, K.O., Zhu, J., and Song, J., “Ef fects of exhaust gas 
recirculation on diesel particulate matter morphology and NOx 
emissions,” Int. J. Engine Res. 9(2):165-175, 2008, doi:10.1243/
14680874JER02307.
35. Kamimoto, T. and Bae, M., "High Combustion Temperature for 
the Reduction of Particulate in Diesel Engines," SAE Technical 
Paper 880423, 1988, doi:10.4271/880423.
36. Kaario, O., Brink, A., Lehto, K., Keskinen, K. et al., "Studying 
Local Conditions in a Heavy-Duty Diesel Engine by Creating 
Phi-T Maps," SAE Technical Paper 2011-01-0819, 2011, 
doi:10.4271/2011-01-0819.
37. Faghani, E., “Ef fect of Injection Strategies on Particulate Matter 
Emissions in HPDI Natural-Gas Engines,” PhD Thesis, The 
University of British Columbia,University of British Columbia, 
2015.
38. Clark, N., Gautam, M., L yons, D., and Bata, R., “Natural Gas 
and Diesel Transit Bus Emissions: Review and Recent Data,” 
SAE Int. (412), 1997.
39. T aylor, S. and Clark, N., “Diesel emissions prediction from 
dissimilar cycle scaling,” Proceedings of the Institution 
of Mechanical Engineers, Part D: Journal of Automobile 
Engineering, 341-352, 2004.
40. McKain, D., Wayne, S., and Clark, N., "Relationship between 
Carbon Monoxide and Particulate Matter Levels across a Range 
of Engine Technologies," SAE Technical Paper 2012-01-1346, 
2012, doi:10.4271/2012-01-1346.
41. Clark, N.N., Jarrett, R.P ., and Atkinson, C.M., “Field 
Measurements of Particulate Matter Emissions, Carbon 
Monoxide, and Exhaust Opacity from Heavy-Duty Diesel 
Vehicles,” J. Air Waste Manage. Assoc. 49(9):76-84, 1999, doi:1
0.1080/10473289.1999.10463880.
Contact Information
Christopher W. J. Mabson
c.mabson@gmail.com
Steven N. Rogak
rogak@mech.ubc.ca
Acknowledgments
The work reported here was funded by the Natural Sciences and 
Engineering Research Council of Canada and Westport Innovations 
Inc. through the Automotive Partnerships Canada program. The 
authors wish to thank UBC engine technician Mr. Bob Parry, Mr. 
Ramin Dastanpour for the help with TEM image analysis, and 
Westport engineers Dr. Ning Wu, Dr. Jim Huang and Mr. Bronson 
Patychuk for their technical support and guidance.
Definitions/Abbreviations
CFD - Computational Fluid Dynamics
DRX - DustTrak DRX
EQR - Global Equivalence Ratio
GPW - Gas Pulse Width
GSOI - Gas Start of Injection
LHLA - Large Hole Large Angle
LHSA - Large Hole Small Angle
Downloaded from SAE International by Dalian Univ of Technology, Monday, August 31, 2026

<!-- PDF_PAGE: 12 -->

PAH - Polyaromatic Hydrocarbons
PPW - Pilot Pulse Width
PSEP - Pulse Separation
PSOI - Pilot Start of Injection
SHLA - Small Hole Large Angle
SHSA - Small Hole Small Angle
SMPS - Scanning Mobility Particle Sizer
TEM - Transmission Electron Microscopy
TEOM - Tapered Element Oscillating Microbalance
TPS - Thermophoretic Sampler
Downloaded from SAE International by Dalian Univ of Technology, Monday, August 31, 2026

<!-- PDF_PAGE: 13 -->

Appendix
Response Surface Methodology
The response surface uses the same concept as [16,26] based on a first order system [27]. The general equation is included here:
(A1)
Where y is the dependant variable (PM or CO), βi are the regression coefficients, xi are the input parameters (EQR, EGR, GRP, diesel, PSEP, 50% 
IHR), and ε is the error from the fit. The dependent variables were the PM or CO emissions. All parameters were assumed to have linear responses 
with the emissions except for PSEP and 50% IHR which assumed second order dependence based on the parabolic response seen on the parameter 
sweeps.
Models were created for each injector to show differences in sensitivity for the PM and CO emissions. The R2 values for each fit are 0.746 and 0.646 
for the LHSA and reference nozzle respectively for PM and 0.72 and 0.823 for CO. The fit for the DRX fit LHSA pair-hole nozzle is in Figure A1. 
The fit is valid over the range of experimental data and the fit consistently predicts the value for the majority of the experimental data.
Figure A1. LHSA DRX Fit R2 = 0.746
Although there is a significant amount of variance that is unexplained by the response surface model, we believe that the sensitivities extracted from 
the model are robust. One indication of this is that the sensitivities of CO to parameters are consistent with those for PM (Table A1). Of course, it is 
possible that both the PM and CO sensitivities are incorrect due to spurious factors that affect both pollutants, but it is exceedingly unlikely that such 
consistency could occur if the response surface was sensitive to measurement noise.
Table A1. Change in CO (% change) at B75 in response to a 10% change in parameters. Off-diagonal entries are the changes in addition to those expected without 
interactions.
 
a). Reference Injector R2=0.823     b). LHSA  Injector R2=0.72
Downloaded from SAE International by Dalian Univ of Technology, Monday, August 31, 2026

<!-- PDF_PAGE: 14 -->

The coefficients and corresponding P-values for the response surfaces are included in Table A2. At 95% confidence P-values below 0.05 cannot reject 
the null hypothesis and are thus significant. The lower confidence in diesel pilot for the reference injector can be attributed to the increases in PM 
emissions for these points being very small and only slightly above experimental error.
Table A2. Coefficients and P-values for models
Evaluation of CFD model Emissions at B75
The engine-out emissions for the SCRE measurements and CFD model predictions are compared in Table A3. As the B75 experimental test point was 
repeated several times, an averaged value is used for the comparison. The uncertainty is expressed as a standard deviation of the repeats.
Table A3. SCRE vs. CFD model emissions
Predictions of NOx, CH4 and fuel consumption are quite good, but the CFD has difficulty estimating the CO and PM emissions. For CO, it is 
important that the model simulation ends at exhaust-valve opening and will under predict oxidation of CO which continues during the blowdown and 
exhaust process. For PM, the relatively crude model being used in this version of the code (2-step Hiroyasu type) does not capture all the nuances of 
the PM formation and oxidation processes.
Downloaded from SAE International by Dalian Univ of Technology, Monday, August 31, 2026

<!-- PDF_PAGE: 15 -->

Equivalence Ratio - Temperature Map
An equivalence ratio-temperature map (or φ-T map) can be used to show differences in combustion for the paired-hole nozzle and the reference 
injector for the same B75 condition [35,36]. Maps were generated using the GRI-3 kinetic mechanism for natural gas at 140 bar and assuming a 2ms 
residence time (see [30,37]). For each point on the map, the formation of CO, NOx and C2H2 are predicted based on local conditions. C2H2 is 
considered as a key precursor for soot formation and is used to indicate likely areas of soot formation. It should be noted that none of the parameters 
shown on the map indicate soot oxidation, which will tend to occur under locally-lean conditions at moderate and elevated temperature.
Figure A2 compares the mass of fuel in the cylinder for the reference and paired-hole LHSA injectors under identical conditions. This is a differential 
mass plot that aims to show where the greatest differences are for the two cases. Specifically, the total amount of fuel for the paired-hole injector at 
each condition (local φ-T) is subtracted from the amount of fuel at that same condition for the reference injector. Regions with more mass for the 
paired-hole nozzle are in red, and more mass for the reference injector are in blue. The axes on this plot are local equivalence ratio and temperature. 
As this is a mass distribution binned with respect to φ and T, the unit becomes 
 .
Figure A2. Local φ-T difference plot 25% IHR B75 adapted from [30].
The φ-T plot shows that the trajectory from high EQR low temperature to high temperature lean regions is largely the same for the paired-hole nozzle 
and reference injector. The main difference is where the fuel is located at this time-step. At 25% IHR, there is much more fuel for the LHSA in high 
CO and PM forming zones. The intention of the pair-hole nozzle was to reduce the local equivalence ratios and avoid much of the soot generation 
process by moving the curve below these areas. However, this map shows that fuel has passed the cold, rich limit where no soot can form and is more 
heavily concentrated in the areas where soot precursors are more likely to form. Further leaning or less leaning would be necessary to prevent this.
CO vs. PM Combustion Map
Carbon monoxide and soot form through very different chemical mechanisms and formation rates peak in different portions of the φ-T map. 
However, we have found that for HPDI combustion, PM and CO are very tightly correlated for changes in timing, EGR and even injector design 
changes. The experimentally measured emissions of CO and PM from the entire B75 dataset are shown in Figure A3. The colours indicate the PSEP 
level, while the different symbols represent the nozzle hole geometry. A fitted curve based on normal operation (PSEP > 0) was fit to the plot for the 
reference injector. As PM increases, CO increases roughly as PM
0.5, suggesting a shift on the φ-T map towards richer conditions and increased PM 
and CO emissions (consistent with Figure A2). Remarkably, this fit also describes the multimode emissions measurements for both the LHSA nozzle 
and the other paired-hole nozzles.
Downloaded from SAE International by Dalian Univ of Technology, Monday, August 31, 2026

<!-- PDF_PAGE: 16 -->

Figure A3. CO vs. PM over entire B75 dataset for LHSA and reference injector.
The close association between PM and CO emissions for the HPDI engine is interesting because the two pollutants are formed by different kinetic 
mechanisms and over different regions of the φ-T map. Only when the premixing is increased dramatically (PSEP < 0) do the points differ from the 
normal PM-CO curve. Again, the response for all injector types is surprisingly similar in that they follow this line, regardless of the operating 
condition. It is important to note the SHSA point produced so much CO that this value may be artificially high as it was above the top range of our 
instruments.
Several studies [38, 39, 40, 41] have characterized the CO/PM ratio of diesel engines, but have found that individual engines follow different and 
highly scattered CO/PM trends, in contrast to our findings for HPDI here. However for the many varied experiments in this paper it is interesting in 
that this ratio holds true for all the injector nozzles tested.
The Engineering Meetings Board has approved this paper for publication. It has successfully completed SAE’s peer review process under the supervision of the session organizer. The process 
requires a minimum of three (3) reviews by industry experts. 
All rights reserved. No part of this publication may be reproduced, stored in a retrieval system, or transmitted, in any form or by any means, electronic, mechanical, photocopying, recording, or 
otherwise, without the prior written permission of SAE International.
Positions and opinions advanced in this paper are those of the author(s) and not necessarily those of SAE International. The author is solely responsible for the content of the paper.
ISSN 0148-7191
http://papers.sae.org/2016-01-0807
Downloaded from SAE International by Dalian Univ of Technology, Monday, August 31, 2026
