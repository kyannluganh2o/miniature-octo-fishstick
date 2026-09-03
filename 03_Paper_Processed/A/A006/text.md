<!-- PDF_PAGE: 1 -->

Abstract
High-pressure direct-injection (HPDI) in heavy duty engines allows a 
natural gas (NG) engine to maintain diesel-like performance while 
deriving most of its power from NG. A small diesel pilot injection 
(5-10% of the fuel energy) is used to ignite the direct injected gas jet. 
The NG burns in a predominantly mixing-controlled combustion 
mode which can produce particulate matter (PM). Here we study the 
effect of injection strategies on emissions from a HPDI engine in two 
parts. Part-I investigated the effect of late post injection (LPI); the 
current paper (Part-II) reports on the effects of slightly premixed 
combustion (SPC) on emission and engine performance. In SPC 
operation, the diesel injection is delayed, allowing more premixing of 
the natural gas prior to ignition. PM reductions and tradeoffs involved 
with gas slightly premixed combustion was investigated in a 
single-cylinder version of a 6-cylinder, 15 liter HPDI engine. SPC 
operation at a high-load point reduces over 90% of the PM with a 2% 
improvement in fuel efficiency while having almost the same level of 
NOx and methane. The drawback of SPC is cycle-to-cycle variation 
and high pressure rise rate. PM does not increase for SPC with higher 
EGR level, higher EQR (global oxygen based equivalence ratio) or 
higher pilot mass, which normally increases PM in normal (mixing-
controlled) HPDI combustion. Computational Fluid Dynamics (CFD) 
simulation of mixing-controlled HPDI combustion showed that at the 
gas ignition time, there is much fuel in the rich (sooting) 
stoichiometry, while for SPC, the mass of fuel in the rich zone is less 
than 10% of the mixing-controlled HPDI combustion, and therefore 
the potential for soot formation is mainly eliminated. The relative 
timing of ignition, or peak apparent heat release rate (AHRR), and 
end of injection is important for the HPDI engine and it can be used 
to define the SPC thresholds in future. The morphology of particles 
produced by SPC is similar to that from conventional HPDI (and also 
from diesel), but the size and number concentration are reduced.
Introduction
Natural gas (NG) is a leading alternative fuel which is widely 
available internationally, and is usually less expensive than gasoline 
or diesel fuel. Its lower carbon-to-energy ratio offers reduced 
greenhouse gas (GHG) emissions if the fuel is burned as efficiently as 
the equivalent liquid fuel. To match diesel engine performance and 
efficiency while burning NG, Westport Innovations Inc. has 
developed a system for the high-pressure direct-injection (HPDI) of 
NG. A small diesel pilot injection (5-10% of the fuel energy) is used 
to ignite the direct injected gas jet, which burns in a predominantly 
mixing-controlled fashion similar to a conventional diesel engine [1].
The present work makes use of a research-level injector that is a 
common-rail, hydraulically diesel-actuated, and electronically 
controlled. The injector is electronically commanded and uses the 
diesel fuel as the working hydraulic fluid to open and close the 
needles. More background information about the Injector, HPDI 
combustion and soot formation process in direct injection (DI) 
engines can be found in the companion paper [2].
In order to reduce particulate matter (PM) and nitrogen oxides (NOx) 
emissions, low-temperature combustion (LTC) was introduced 
recently in diesel engines. In all LTC strategies premixing is higher 
and the combustion temperatures are reduced, which further slows 
NOx formation kinetics and soot formation [3], [4] while soot 
oxidation rates decrease as well [5], [6].
Low-temperature combustion (LTC) in diesel engines can be divided 
into two categories [7]: those in which the combustion phasing is 
largely decoupled from injection timing, and those in which the control 
of the combustion phasing is closely coupled to the fuel injection event. 
The first category is typically called Homogeneous charge compression 
Effect of Injection Strategies on Emissions from a Pilot-
Ignited Direct-Injection Natural-Gas Engine- Part II: Slightly 
Premixed Combustion
2017-01-0763
Published 03/28/2017
Ehsan Faghani, Pooyan Kheirkhah, and Christopher W.J. Mabson
University of British Columbia
Gordon McTaggart-Cowan
Westport Fuel Systems
Patrick Kirchen and Steve Rogak
University of British Columbia
CITATION: Faghani, E., Kheirkhah, P., Mabson, C., McTaggart-Cowan, G. et al., "Effect of Injection Strategies on Emissions from a 
Pilot-Ignited Direct-Injection Natural-Gas Engine- Part II: Slightly Premixed Combustion," SAE Technical Paper 2017-01-0763, 2017, 
doi:10.4271/2017-01-0763.
Copyright © 2017 SAE International
Downloaded from SAE International by Dalian Univ of Technology, Monday, August 31, 2026

<!-- PDF_PAGE: 2 -->

ignition (HCCI [8] [9] [10], [11]).The second category [7], [12], [13], 
[14], [15], [16], [17] is typically called “partially premixed 
compression ignition” (PPCI) where the charge distributions for PPCI 
are more heterogeneous, both fuel-lean and fuel-rich at ignition timing 
than HCCI [16]. These systems typically use a low compression ratio, 
large amounts of cooled exhaust gas recirculation (EGR) or the use of 
retarded injection timing in order to reduce PM and NOx emissions by 
producing more premixing through delaying the ignition.
Although LTC can reduce PM and NOx in diesel engines, this 
strategy still faces challenges including load range limitations, 
transient and cold-start performance, higher pressure rise rates and 
noise at high fuelling rates and increased emissions of CO and 
unburned hydrocarbons (UHC)[14]. According to the experimental 
results [15], for the cases where ignition happens close to the end of 
injection UHC emissions increase due to over-mixing close to the 
injector at end of injection (EOI).
In diesel engines, the ignition delay is tightly related to cylinder 
temperature and pressure. A diesel engine study [12] controlled 
ignition delay in the engine by adjusting the intake air temperature 
while keeping the same charge density at TDC. This permitted the 
study of sooting characteristics at various ignition delays while 
keeping the same diesel jet penetration. A conceptual image for PM 
reduction was introduced in their study. The conceptual figure 
discusses two main ideas. First, the importance of relative timing 
between EOI (where the local EQR in cylinder are abruptly reduced) 
and peak apparent heat release rate (AHRR) (roughly the PM 
formation time) was emphasized. Soot mass in the cylinder starts to 
be significant enough to be captured optically in the experiment’s few 
crank angles after the ignition, which is roughly the peak premixed 
AHRR [12]. The second idea of this conceptual figure discusses the 
soot distributions in the jet for normal and PPCI combustion.
In HPDI engines, ignition timing is controlled by the diesel injection 
timing. Adjusting relative timing between diesel and natural gas 
allows more premixing of the natural gas prior to ignition. This 
injection strategy is called slightly premixed combustion (SPC) [18], 
[19], [20], since it is neither fully premixed nor mixing-controlled.
PPCI diesel and SPC in HPDI engines are fundamentally different 
methods of premixing. PPCI in diesel engines is achieved by slow 
combustion phasing due to lower ambient temperature and oxygen 
concentration, therefore the chemical kinetics of ignition and mixing are 
tightly coupled. Since SPC, EGR and combustion phasing are close to 
conventional HPDI values, ambient temperature and oxygen 
concentration remain almost the same as conventional HPDI 
combustion ([O
2]intake=23-18%). Thus the pilot and NG ignition kinetics 
are essentially unaltered in SPC. By injecting the pilot later, the gas has 
more time for premixing before ignition. The results of the conceptual 
graph will be compared to SPC results in two terms: if the relative 
timing of EOI and peak AHRR is important for SPC injection strategy 
too and if the PM contours in the jet is similar to the conceptual graph.
The effect of different parameters, including relative timing of 
natural gas and pilot, was studied previously [ 18], [19]. Limited 
premixing results in a more rapid and more intense combustion 
event. SPC reduces PM at the expense of higher NOx and 
hydrocarbon emissions, while the indicated fuel consumption was 
slightly reduced for a given EGR fraction. Combining SPC with 
increased EGR [20] can keep NOx emissions at their baseline levels 
while still reducing PM significantly. This elevated EGR point still 
has high total hydrocarbon (tHC) emissions. In an HPDI engine, tHC 
emissions are dominated by methane.
Premixing in the current paper is defined as the lean mixture at the 
time of ignition. The main objective of the present study is to consider 
the following questions related to SPC used in HPDI engines: 
• How can we improve the SPC strategy to control PM, NOx and 
methane together? 
• What is the effect of EGR, EQR and pilot mass on SPC strategy 
on heat release rate, emissions and engine performance? 
• What are the defining characteristics of SPC in terms of ignition 
and injection timing? 
• Can reactive CFD predict heat release rate and PM reduction 
from SPC with accuracy comparable to its predictions for 
conventional HPDI combustion? 
• What physical processes contribute to low PM of SPC in 
HPDI engines?
In addition PM morphology and size distribution is studied using 
Transmission Electron Microscope (TEM) images and scanning 
mobility particle sizer (SMPS) sampling. The objective is to compare 
the PM aggregates, primary particles and number concentration with a 
conventional HPDI combustion regime (referred to in this work as 
“mixing-controlled HPDI”). Finally, an additional goal of this study has 
been to highlight the qualitative similarities and inconsistencies between 
diesel PPCI combustion and HPDI engines in terms of performance.
Experimental Methods
In this section we provide a brief description of the experimental 
method; more information about the engine, injector, fuel and air 
handling systems, cylinder pressure measurements, heat release rate 
calculations and emission measurements can be found in the first 
part of the current paper.
The Single Cylinder Research Engine (SCRE) characteristics are 
summarized in Table 1 and in earlier publications [21], [22], [23], 
[24]. The engine is a standard 6-cylinder Cummins ISX 15L engine, 
modified so that only a single cylinder fires. The diesel fueling system 
was replaced with a custom fuel supply system feeding the HPDI 
research injector. Engine speed is controlled by an eddy-current 
dynamometer and an electric motor, while load is controlled by the 
commanded injection quantity. Figure 1 shows the main features of 
the Single Cylinder Research Engine (SCRE) gas flow system 
including the PM sampling system and the fuel conditioning system.
The injector is a Westport research-level HPDI natural gas and 
diesel injector. The injector is electronically commanded and uses 
the diesel fuel as the working hydraulic fluid to open and close the 
needles. The control parameters are the pilot start of injection 
(PSOI), pilot pulse width (PPW), relative injection timing (RIT)
1, 
gas start of injection (GSOI), gas pulse width (GPW). The Injection 
command signals were controlled using a custom National 
Instruments FPGA board through a LabVIEW interface. One 
injector (termed here “Baseline Injector”) has been used for all the 
experiments presented in this study.
1 RIT (ms) = GSOI-PSOI
Downloaded from SAE International by Dalian Univ of Technology, Monday, August 31, 2026

<!-- PDF_PAGE: 3 -->

A diesel high-pressure pump provides high pressure diesel to the 
research fuel control system. The diesel pressure is regulated to 16-30 
MPa using a manual pressure regulator. The diesel pressure is then 
used to regulate the NG pressure using a dome-loaded pressure 
regulator. The system maintains the NG pressure approximately 1 
MPa below that of the diesel. Both diesel and gas are fed to the HPDI 
injector through the engine’s internal fueling rails. Limits of the 
natural gas fuel supply to the research test cell limit the maximum 
natural gas pressure to approximately 28 MPa, limiting the maximum 
diesel pressure to 29 MPa. The total mass of fuel (m
fuel) is calculated 
on a diesel energy-equivalent energy basis. The mass flowrate of NG 
fuel is measured by a coriolis mass flow meter (Promass 80A) in the 
fuel line. Diesel fuel flow is measured gravimetrically.
Intake air is supplied by an electric air compressor and pneumatic 
regulators are used to set intake pressure and backpressure. Through 
the use of these two pressures and an EGR valve, the intake exhaust 
gas recirculation (EGR) level of the engine can be controlled. Airflow 
rate (mass of fresh air) is measured with a venturi and confirmed by a 
hot film anemometer. Airflow measurements are used in the carbon 
balance and measurements of EGR and EQR (Global oxygen based 
equivalence ratio). EGR mass flow rate is calculated by measuring 
carbon dioxide in the intake system ([CO
2]intake). The global mixture 
is described using oxygen-based equivalence ratio, to ensure that 
oxidizer from both the EGR and the intake air are included.
Figure 1. Single Cylinder Research Engine (SCRE) gas flow, PM sampling 
and fuel conditioning system.
Diesel and gas injection timing, intake and exhaust pressure, EGR 
level, and common rail gas and diesel pressure can be controlled by 
the operator. To monitor the combustion performance, the in-
cylinder pressure is recorded using a flush-mounted, water cooled 
Kistler 6067C piezoelectric transducer, sampled at 0.5° CAD 
resolution. An average of 45 cycles is used to calculate the indicated 
pressure and apparent heat release rate. The indicated pressure is 
used to calculate the gross-indicated mean effective pressure 
(GIMEP) and gross-indicated specific fuel consumption (GISFC). 
The apparent heat release rate is calculated, based on the first-law of 
thermodynamics analysis as described in Heywood [ 25]. The 
integral of the heat release rate (IHR) was used to define the 
combustion phasing, with the principal timing being the crank angle 
of the mid-point of the IHR (CA50).
The gaseous emissions (undiluted exhaust for CO, CO
2, O2, CH4, 
tHC, NOx and intake CO 2 for EGR calculations) were measured 
with an A VL CEBII emissions bench. The PM sampling system 
installed on the SCRE is separate from the gaseous measurement 
system and is based on a 2-stage system using an ejector diluter and 
an aging chamber. The dilution ratio at the first stage is 
approximately 7:1 and the overall dilution ratio is 12:1, determined 
by comparing the exhaust and post-dilution CO
2 concentrations. 
Semi-volatile species are then removed by passing the sample 
through a thermodenuder, as shown in Figure 1 and discussed in 
more detail elsewhere [ 22]. Particle mass concentration is measured 
using a tapered element oscillating microbalance (TEOM) and a 
TSI DustTrak DRX (DRX).
Particle mobility size distributions are measured with a scanning 
mobility particle sizer (SMPS). The DRX measures light scattering, 
which can be correlated with aerosol mass for particles of consistent 
size, morphology, and composition. The DRX is fast and sensitive to 
low concentrations, but it does not give a true mass measurement; the 
TEOM is less sensitive but directly measures total PM mass 
(including black carbon and volatiles). In this work, we present 
results for the DRX measurements and note that all trends discussed 
in this work were apparent in the TEOM measurements as well. The 
DRX has been correlated against both particle size-based 
measurements (SMPS) and direct mass measurement (TEOM). A 
strong correlation was found for most conditions, although at lower 
loads (25% of maximum torque at a given speed), the DRX tended to 
overpredict PM mass. More information is available elsewhere [22], 
[24]. SMPS measurement only applied to the optimized SPC point 
compared to the baseline HPDI point.
Table 1. SCRE engine, injector and fuel specifications
Engine Experiments
The engine experiments, including data acquisition procedure, are 
similar to the companion paper [2]. In this work we consider 
operation at mid-speed and at an indicated power that was 75% of the 
nominal maximum at that speed (mode B75). This load was selected 
as it generates relatively high levels of particulate; at lower loads, PM 
Downloaded from SAE International by Dalian Univ of Technology, Monday, August 31, 2026

<!-- PDF_PAGE: 4 -->

emissions tend to be very low and hence SPC was expected to 
provide less value [22]. More information about measurement 
variability is included Ref. [24].
Lowering the flame temperature by increasing EGR is an effective 
method to control engine-out NOx level; however, this tends to 
increase the PM level due to the PM-NOx trade-off. In the more 
premixed combustion, the PM-NOx trade-off can be escaped by 
higher EGR; decreasing NOx is not associated with an increase in 
PM emissions [7], [12], [14], [16]. In previous HPDI studies [18], 
[19], [20], it was found that combining SPC with increased EGR can 
keep NOx emissions at their baseline levels, still having significantly 
lower PM. However, these points usually end up with high methane 
emissions [18], [19], [20].
The idea of using higher EQR to control methane emission for SPC 
is tested here. Higher EQR might decrease the potential for over-
mixing since there is less air mass in the cycle to lean the mixture. 
Higher EQR is achieved by reducing the intake pressure while 
keeping GIMEP constant.
For the mixing-controlled HPDI points, the pilot mass has a 
significant effect on the PM engine-out. By increasing pilot mass, 
PM emissions increase significantly [ 18], [19], [22]. Pilot mass 
quantity also affects ignition timing due to the larger ignition 
source, and because the diesel injection duration increases 
(indicated by pilot pulse width, PPW). A preliminary study 
(Appendix E of Ref. [24]) has been performed to find out whether it 
is better to control the separation between the end of diesel and start 
of gas injections (PSEP), or the “relative injection timing” (RIT). 
RIT is the difference between the pilot start of injection (PSOI) and 
gas start of injection (GSOI). It was found that the points with 
constant PSOI and GSOI, (RIT constant) keep the AHRR similar to 
the baseline point while we change PPW. In the current study RIT 
has been used to set the point instead of PSEP.
These considerations led to experiments that focused on the relative 
injection timing, EGR, EQR and the strength of the ignition source 
(indicated by pilot diesel quantity). The operating points are 
summarized in Table 2. All the experiments have been done at mode 
B75 with 1500rpm, GIMEP of 16.5 bar and Gas Rail Pressure 
(GRP) of 25 MPa. The timing was adjusted keeping CA50 at 11° 
ATDC for all the cases. Different sweeps of parameters were 
considered to study the effect of EGR, EQR, combinations of 
EGR-EQR and pilot mass on the results. By changing PPW from 
0.52 ms to 1.02 the ratio of diesel to gas (energy basis) changes 
from 5%-13%; the natural gas mass is set to meet the GIMEP 
requirement. Every test was done at least 2 times.
The [O
2]intake is included in the table for comparison; however, the 
points were not set based on this parameter. The measurement duration, 
after the engine is in steady-state condition, was at least 180 seconds 
for emission measurements. In the steady-state conditions, engine 
power, fuel rate, air flow rate, EGR rate and emissions were monitored.
Although there is no abrupt change between mixing-controlled 
combustion and slightly premixed combustion, for simplicity the 
points where the commanded start of gas injection precedes the 
commanded start of pilot injection are called “slightly premixed 
combustion”. This occurs for the cases with RIT < 0.
Table 2. Summary of SPC engine experiments. Relative Injection timing 
(RIT) sweeps are combined with other conditions1,2.
CFD Modeling and Simulation Cases
Combustion and emissions were simulated using a custom-developed 
reacting flow computational fluid dynamics (CFD) model, developed 
at Westport Innovations Inc. by Huang [26]. It is a three-dimensional 
CFD model built in OpenFOAM that incorporates detailed chemical 
kinetic mechanisms for the combustion of diesel and natural gas in a 
non-premixed turbulent regime. More information about the details 
of the CFD modeling can be found in the first part of the current 
paper. The CFD tool was heavily validated against experimental data 
in the previous studies [27] for mixing-controlled combustions.
CFD will be used in the current study in order to help understanding 
the in-cylinder processes better including combustion, gaseous 
emissions and PM formation process. The soot model only represents 
the simplified physics of soot generation namely local equivalence 
ratio and temperature that lead to PM formation and oxidation. The 
model does not cover different phases in soot formation and oxidation 
as described in the introduction. As a result, it has value as an 
indicator of likelihood of soot formation and oxidation rather than as 
providing an absolute value. . In the current study we model the 
baseline case (RIT=0.9 ms, EGR=18% and EQR=0.6) and some 
combination of relative timing and EGR/EQR.
Table 3. Summary of CFD tests*
For the CFD cases the physical delay, ramp-up and ramp-down are 
assumed to be 0.7 ms, 0.6 ms and 0.6 ms respectively, according to 
Ref. [28], for gas injection. The other details of the CFD simulation 
are mentioned in reference [29].
Results and Discussion
Effect of Delaying Pilot Injection on Combustion
Here, the separation between the start of the diesel injection to the 
start of the gas injection, RIT, is changed from 1.5 to -1.5 ms. The 
apparent heat release rate (AHRR), expected injection rate and 
ignition points are shown in the Figure 2 for RIT=1.5, 0.3, -0.3 and 
- 1.5 ms. As mentioned in the experimental method section, the 
AHRR is the average of 45 cycles and the graph has not been 
Downloaded from SAE International by Dalian Univ of Technology, Monday, August 31, 2026

<!-- PDF_PAGE: 5 -->

filtered further. The x-axis is crank angle degree (CAD) ATDC. 
The expected NG injection rate, the blue line in the figue, is a 
simplified fuel rate shape (trapezoid shape) based on the previous 
study on the same injector model [ 28] (physical delay, ramp-up and 
ramp-down are assumed to be 0.7 ms, 0.6 ms and 0.6 ms 
respectively). The red and green squares are the commanded diesel 
and NG injections. The y-axis unit for the fuel rate shape and 
commanded signals is irrelevant. The red and green stars are the 
ignition point of diesel and NG respectively, calculated by 
analyzing the AHRR graphs. Note that the baseline RIT for mode 
B75 is 0.9 ms. The AHRR changes correspond to changing from 
more mixing-controlled burn to more premixed burn as we go 
toward negative RIT points. The AHRR for mixing-controlled 
HPDI points is spread over a wider range in crank angle, while by 
moving toward more premixed burning AHRR is limited in narrow 
range of crank angles. This trend has been seen in the diesel engine 
studies by slightly delaying the ignition [ 12], [19].
Figure 2. Apparent heat release rate by changing relative injection timing 
(RIT), for mode B75 from the SCRE experiments. The blue line is a 
qualitative representation of the fuel rate shape, the red line is the diesel 
injection command, the green line is the NG command, the red star is the 
diesel ignition point and the green star is the NG ignition point.
a. Peak AHRR timing after EOI
b. Peak AHRR magnitude
Figure 3. Ignition dwell, and peak AHRR timing and magnitude for different 
RITs from the SCRE experiments.
Here, the green trace is the expected gas injection profile using a 
physical delay (0.7 ms) and expected ramp times (0.6 ms up, 0.6 ms 
down) determined from momentum measurement tests (see reference 
[28]). The vertical “end of injection” (EOI) line occurs at the end of 
the green trace. Red and green stars show pilot and gas ignition points 
determined from the AHRR curve.
For mixing-controlled HPDI points (RIT>0) peak AHRR occurs 
before EOI, corresponding to the first category (AHRR peak before 
EOI) discussed in the introduction. The ignition of NG is before EOI. 
As we move to negative RIT values, the peak AHRR is closer to EOI. 
For SPC points (RIT<0), peak AHRR is after EOI. The AHRR graphs 
for all the RITs can be found in Ref. [24]. The engine-out emission 
and engine performance at different RIT timing will be discussed 
together with the high EGR/EQR points.
Figure 3 (a) and (b) show peak AHRR location, and peak AHRR 
magnitude for different RITs and different EGR-EQR combinations. 
Peak AHRR are delayed by 2-3 degrees by increasing EGR for middle 
RIT points (RIT= -0.3 ms, 0.3 and 0.9 ms). For all the SPC points at 
different EGR/EQR levels, combustion duration (defines as 5-95% of 
NG IHRR) remains almost unchanged; however, the peak AHRR 
changes significantly, about 70 kJ/m
3-deg over the average of 300 kJ/
m3-deg, as it is shown in Figure 3 (b). By increasing EGR, the peak 
AHRR is lower for SPC points, perhaps due to lowering the flame 
temperature by increasing EGR. Increasing EQR will increase the 
peak AHRR for SPC points. This might be due to a lower potential for 
over-mixing at higher EQR. Increasing EGR and EQR together will 
maintain the AHRR peak close to the original case with EGR=18% 
and EQR=0.6. Note that these experiments are done at fixed engine 
load (nearly constant fuelling), so to increase EQR, the airflow and 
cylinder pressure is reduced. This could affect injection behavior 
Downloaded from SAE International by Dalian Univ of Technology, Monday, August 31, 2026

<!-- PDF_PAGE: 6 -->

slightly. As an interesting observation, the peak AHRR magnitude 
decreases for more premixed burn at RIT=-1.5 ms, potentially due to 
mixing the main portion of the fuel below the stoichiometric and 
lowering the flame temperature. Peak AHRR magnitude in normal 
HPDI points does not change significantly with EGR or EQR, 
however, by more premixing, EGR and EQR will affect the AHRR 
peak. More AHRR analysis can be found in Reference [24].
Effect of Parameter Sweeps on Emissions
The effect of pilot mass on PM is shown in Figure 4, along with the 
previous results or EGR, EQR and RIT sweeps. As discussed 
earlier, the relative injection timing (RIT) is a better way of 
characterizing injection timing than PSEP, when pilot pulse width 
changes (Ref. [24]). For the SPC cases, with RIT<0, the pilot mass 
has no measurable effect on the PM emissions. The diesel 
contribution in combustion is only to provide a source of ignition 
and diesel to NG energy ratio is about 6% for the current study. In 
“mixing-controlled” HPDI, the gas combustion is predominantly 
non-premixed. As such, soot formation occurs in the gas jet at some 
modes. In a previous study [30] the contribution of the pilot fuel (a 
biodiesel blend with higher 
14C content than diesel fuel) was 
determined using accelerator mass spectrometry (AMS) 
measurements of 
14C in the exhaust particulate. The pilot fuel 
contributed to 4-40% at different modes. However at the high loads 
(~60% of load, high PM-forming modes), the pilot contribution was 
maximum 6%. In the current experiments by more premixing of 
natural gas injection almost all of the PM is removed as well, while 
the pilot injection occurs in almost the same environment as the 
baseline. This is in general agreement with the previous 
experiments [ 30].
a. Engine-Out PM
b. Peak AHRR locaiton vs EOI
Figure 4. engine-out PM and peak AHRR location for all the SPC experiments
For the negative RIT experiments, engine-out PM is not sensitive to 
engine parameters like EGR, EQR and pilot mass while for positive 
RIT experiments the engine parameters can change engine-out PM by 
a factor or eight. All the points in negative RIT cases have peak 
AHRR after EOI, despite the differences in combustion and PM 
formation process of PPCI and SPC. For the SPC cases (RIT<0), the 
ignition occurs close to EOI, where rich mixture formation will 
abruptly disappear, so the potential for soot formation is mainly 
removed from these cases and inlet condition effects is mitigated. It 
will be discussed more in details in CFD section.
a. NOx
b. Methane (CH4)
c. CO
Figure 5. Engine-out emission as a function of relative injection timing (RIT) 
for different engine environment from the SCRE experiments.
By moving toward negative RIT values (more premixing), PM decreases 
to a value that cannot be measured accurately by the DRX. With respect 
to the conceptual model discussed in the introduction, almost all the PM 
is removed when peak AHRR is after EOI, i.e. RIT≤-0.3 ms. Despite this 
major difference in fuel and how more premixing was achieved, in both 
SPC and PPCI the relative time of EOI and peak AHRR is an important 
factor. This leads us to define a threshold for SPC based on the current 
studies, which will be discussed later.
Downloaded from SAE International by Dalian Univ of Technology, Monday, August 31, 2026

<!-- PDF_PAGE: 7 -->

For slightly premixed cases, PM does not increase by changing the 
in-cylinder environment, which normally increases PM in mixing-
controlled HPDI points, e.g. higher EGR or EQR level. For all the 
SPC points, ignition happens after EOI. The points with peak 
AHRR after EOI have very low engine-out PM with low sensitivity 
to engine parameters.
Figure 5 shows the engine-out NOx, methane and CO emissions for 
different EGR and EQR levels. Increasing EQR has only a minor effect 
on NOx emission. EGR is increased to reduce the NOx emission (for 
RIT=-0.3 ms) back to the baseline point. For these tests, the inlet 
oxygen concentration is changed from 20.5% to 19%. For mixing-
controlled HPDI points, methane emission increases as we increase 
EGR, in SPC cases this increase in methane emissions is more 
significant. The increase in methane emission at higher EGR rate might 
be due to incomplete combustion by lowering the fuel temperature; 
however, this does not explain higher methane level at the same EGR 
level in SPC cases. Increasing EQR helps to reduce methane at the same 
RIT and same level of EGR. Methane emissions for the high EGR and 
EQR points are close to the level of methane in the baseline point.
Carbon monoxide follows a similar trend but is not reduced to zero 
even for RIT=-1.5 ms. NOx and methane both increase with increasing 
premixing of NG. Methane is constant for RIT≥ -0.3 ms and suddenly 
increases for more premixing; this will be discussed more in Appendix 
B. Evaluation of emissions formation will be reviewed in more detail 
in the φ-T map analysis and the CFD results discussion.
Effect of Parameter Sweeps on Engine Performance
Engine performance for different RIT is shown in the Figure 6. By 
moving toward more premixing, fuel efficiency is generally 
improved, as was found in previous experiments [18], [19], [20]. This 
might be due to the narrow range of AHRR close to TDC. The 
combustion phasing, defined by CA50, is kept constant for all the 
points. The position of peak AHRR for the normal RIT sweeps (see 
Table 2) will be moved even later in the cycle; however, the 
combustion will end earlier as well. Changing EGR and EQR mainly 
changes the AHRR peak magnitude as mentioned before.
Increasing EQR will increase fuel consumption at the same RIT for 
mixing-controlled HPDI points. However, for SPC points increasing 
EQR has an insignificant effect on fuel consumption based on GISFC 
(any changes in pumping work are not incorporated into the GISFC 
results). Combustion harshness (indicated by COV or maximum 
pressure and maximum dP/dθ) increases with more premixing and 
then slightly decrease for RIT=-1.5 ms. Higher combustion harshness 
of these points leads to higher engine noise.
By increasing premixing, the effect of engine parameters, e.g. EGR 
and EQR, on the peak pressure rise rate and variability of maximum 
pressure would be more significant. It might be related to changing 
the combustion process from mixing controlled to slightly premixed 
combustion. Mixing-controlled combustion is mainly controlled by 
fuel injection momentum and it is mainly independent of EQR and 
EGR while the ignition timing is determined by diesel injection 
timing. SPC combustion is a combination of mixing controlled and 
lean charge combustion. For SPC cases, while the mixing controlled 
combustion is mainly independent of EGR and EQR the combustion 
of lean charge is function of EGR and EQR by changing the flame 
speed. The exhaust temperature is within the variability of the results 
(±5°C) for all the points of the parameter sweeps.
a. GISFC
b. (dP/dθ)max
c. COV of Pmax
Figure 6. Engine performance for different engine environment from the 
SCRE experiments.
A potential concern with the SPC results is that injector 
characteristics might have an impact on the results. Therefore, 4 
different injectors of the same model were tested at B75 for a range 
of timings and injection durations. That work, detailed in [24], 
indicated that, the relative reductions in PM match those of the 
baseline injector discussed in the present work. More information is 
included in Appendix A of the current paper.
Optimized Slightly Premixed Combustion and PM 
Characterization from the SCRE Experiments
From the parameter sweeps discussed above, an “optimized point” 
(i.e. best point of the SPC cases in the current parameter sweeps) was 
selected to have the lowest PM with almost the same NOx and CH4 
as the baseline point (RIT=0.9, EGR=18% and EQR=0.6). The high 
EGR-EQR point (EQR = 0.7 EGR = 25%) with RIT of -0.3ms was 
Downloaded from SAE International by Dalian Univ of Technology, Monday, August 31, 2026

<!-- PDF_PAGE: 8 -->

selected due to significant PM reduction and same level of NOx and 
methane as the baseline point (Table 4). The optimized SPC point 
shows a 90% reduction in PM and a 2% improvement in fuel 
economy with almost the same level of NOx, methane and CO 
emissions. The drawback of this point is cycle-to-cycle pressure 
variations and a higher peak pressure rise rate in the cycle; both of 
which are referred to as higher combustion harshness in the current 
study. Higher combustion harshness of the SPC points leads to higher 
engine noise as well.
Table 4. Comparing optimized SPC point with the baseline
The baseline B75 (0.9 ms RIT, 18%EGR, 0.60EQR, the baseline is 
one point from the normal sweeps of Table 2) and optimized SPC 
point were repeated for more detailed analysis of the PM 
characteristics, using an SMPS and collecting PM on TEM grids. 
More information about the TEM analysis can be found in reference 
[24], [31], [32]. The SMPS shows that the SPC condition produces 
much smaller soot aggregates and a much lower concentration of 
particles. The TEM analysis also shows that the SPC point produces 
much smaller soot aggregates with smaller primary particles. Smaller 
aggregates, smaller primary particles and lower total number 
concentration suggest that the SPC strategy reduces soot formation 
rather than enhancing oxidation [24].
Table 5. Summary of the results from SMPS and TEM sampling for SPC and 
baseline points
CFD Results and Discussion of SPC Mechanism
The baseline point and some SPC points (RIT=-0.3 ms with different 
EGR-EQR levels) were simulated. The AHRR graphs of baseline and 
SPC conditions are shown in Appendix C. There is a good agreement 
between CFD and measurement for the baseline condition, but not for 
SPC. For the SPC case, the gas ignition delay was not be predicted 
correctly with the model, possibly because the specific TGLDM 
library used in this work was designed for mixing-controlled HPDI 
combustion. More information about the TGLDM libraries is 
mentioned in reference [26]. Revising these kinetics libraries for 
gas-diesel mixtures is a complicated task [29] outside the scope of 
this work, therefore, in this study we mainly focus on PM based on 
mixture fraction distribution while other emissions and engine 
performance are not reported here.
Since our CFD model did not predict the ignition point correctly, it 
therefore could not be expected to predict PM spatial distribution 
accurately. Therefore, the remainder of the discussion focuses on the 
evolution of the mixture distribution in the cylinder, which is nearly 
independent of the chemistry.
Figure 7 shows the normalized mixture fraction mass in “rich zone”, 
Z
rich (2≤φ≤5), and “lean zone”, Z lean (φ≤1), as a function of crank 
angle (CAD). Zrich and Zlean
2 take values between 0 and 1. Z lean is a 
monotonically increasing function approaching 1 by the end of the 
cycle as the injected fuel is completely mixed with the charge. On 
the other hand, Zrich rises as the injection starts and then drops to 
zero shortly after the end of injection. The gas ignition points are 
shown in the figure by red stars. For the baseline HPDI combustion, 
the ignition point is before development of the rich zone in the cycle 
so it is more likely that soot will be formed by rich zone 
development. For the SPC case (EGR=25%, EQR=0.7), however, 
due to a longer ignition delay, ignition is almost at the end of rich 
zone development so less soot will be formed. The penetration of the 
jet for the SPC case is higher than the baseline point since the gas is 
injected in lower air density for SPC case [ 29]. This higher 
penetration of the SPC cases can be noticed from the lower rich zone 
peak in Figure 7; however, almost all of this reduction in the rich 
zone happens before the ignition point and cannot be the main 
reason for PM reduction in SPC. Delaying the ignition to the end of 
rich zone peak is the main reason for PM reduction of these points 
based on the current graph. For all the SPC cases, independent of 
EGR and ERQ level, ignition occurs at the end of rich zone 
formation so the potential for soot formation is mainly removed for 
all the SPC cases. Therefore changing EGR and EQR would have 
only minor effect on PM level at the end of the cycle.
Figure 7. Development of rich zone and lean zone in the cycle for baseline and 
SPC case from the CFD simulations. The stars are the NG ignition points 
calculated from CFD AHRR curve.
Premixing can be defined by different metrics. It can be defined as the 
level of Zlean at the ignition timing. For this metric a CFD study or a 
phenomenological model is always required. Based on this metric Zlean 
is about 55% for SPC case while it is under 5% for the baseline case. 
The current study suggests the importance of relative timing of 
ignition (or peak AHRR) and end of injection. Related to this finding, 
another metric could be the fuel injected portion at the time of ignition 
(SPC factor=100% when ignition is at the EOI). To define this metric, 
knowledge of injector behavior is required (from injector testing).
An understanding of soot and NOx formation in engines can be aided 
by examination of the combustion process in an equivalence 
ratio-temperature map (φ-T map) [7], [33]. It is a useful qualitative 
2
Downloaded from SAE International by Dalian Univ of Technology, Monday, August 31, 2026

<!-- PDF_PAGE: 9 -->

approach for visualization of the cylinder state at each time step and 
soot and NOx formation in DI engines. This type of analysis consists 
of a background image where relevant emission contours are 
generated based on a perfectly stirred reactor (PSR) calculation for an 
engine relevant resident time. The foreground of these figures shows 
the instantaneous location of fuel packets on the map. Figure 8, is a 
φ-T map generated for natural gas combustion. The contours show 
the location where acetylene (a soot precursor) and NOx formation 
occur for NG. The acetylene and NOx are calculated based on the 
Cantera Perfectly Stirred Reactor model [34] using the GRI3.0 
mechanism for NG (taken as 95.1% of CH
4, 3.7% of C2H6 and 1.2% 
C3H8 by mass). The selection of the pressure and residence time is 
based on previous analysis of φ-T map in the literature [7]; residence 
time was 2ms and pressure (140 bar) was close to the maximum 
pressure of cylinder. The chemical kinetics was solved at constant 
temperature in order to generate contours for C
2H2, CO, and NO. The 
numbers in the φ-T map are concentrations of each species in the 
combustion mixture of PSR calculations. The numbers are only 
presented to show the relative position of high and low concentrations 
of the species. The green dashed line shows the non-reacting 
adiabatic mixing of fuel with ambient air. The fuel temperature is 
assumed 370 K with an ambient temperature of 1000K (roughly the 
temperature at TDC). The red lines on the map are the adiabatic flame 
temperature calculated for these fuel/air temperatures and oxygen 
mass fraction of 20.5% (intake oxygen of the baseline point) and 19% 
(intake oxygen of the SPC point).
CO formation based on high temperature zones is shown in this 
figure; however, CO also can be formed in the lean zone at a lower 
temperature as well [7], [16]. Based on the SPC experiment the 
engine-out CO does not reach to zero for more negative RIT cases; 
the reminding CO might be the CO generated in the premixed zone.
The fuel will be mixed with air according to the adiabatic mixing 
line before the ignition point. Two different combustion processes 
have been added to the plot for comparison of baseline and SPC 
case; shown in Figure 8. In this conceptual graph, the dark blue 
arrows approximate the baseline (mixing-controlled HPDI) case. 
The location of the premixed burning (horizontal lines) in the 
graph is estimated based on the CFD results presented in Reference 
[24]. The average EQR at the ignition time for baseline case is 
about 3, while for SPC it is slightly above stoichiometric mixture. 
The real premixed burning is a cloud rather than a single line; 
however, for simplicity the line is shown based on average EQR at 
the ignition time from CFD. The orange arrows show the cases 
with later ignition and higher EGR. More charge is premixed 
before ignition so the premixed burning would be a governing part 
of the combustion. Premixed combustion is followed by mixing-
controlled combustion. It should be noted that for the range of 
EGR changes in these experiments, the inlet oxygen concentration 
is changed from 20.5% to 19% and accordingly, the adiabatic flame 
temperature will be reduced by less than 100 K. In the LTC in 
diesel engines the adiabatic flame temperature will be reduced by 
300-700 K by reducing the inlet oxygen concentration to 10-15% 
[7]. On the other hand, LTC is achieving ultra-low NOx emissions, 
while SPC is maintaining NOx at the same level as the baseline. 
The EGR in our experiments increased just slightly to maintain the 
NOx level of the baseline point, while for diesel LTC is used to 
control the ignition point as well.
For the baseline combustion, the mixing-controlled combustion 
passes from the PM formation zone and later moves to the NOx 
formation zones. For the SPC case, the average local EQR is below 
the PM forming zone therefore the soot formation of SPC points is 
minimal. As it is shown in this figure changing EGR would not 
change the low potential of soot formation in SPC cases. The 
experiments on SCRE also showed the same results; for negative 
RIT cases the PM level was independent of EGR or EQR level. In 
reality, since the premixed burning is not a single line, some 
packets of fuel will still pass the PM formation zone. The lower 
flame temperature due to higher EGR generates less NOx 
compared to an SPC case with lower EGR.
Figure 8. φ-T map computed for 2 ms residence time at 140 bar. The fuel temperature is 370 K and ambient temperature is 1000K. The simulation is based on GRI3.0 
mechanism. The contour numbers show the concentration of each species based on a PSR simulation. The blue combustion path line is the conceptual baseline 
combustion while the orange line is the SPC conceptual combustion line.
Downloaded from SAE International by Dalian Univ of Technology, Monday, August 31, 2026

<!-- PDF_PAGE: 10 -->

Conclusions
For HPDI, slightly premixing the natural gas by delaying the pilot 
injection until after the natural gas injection reduces PM at the 
expense of NOx and CH4 penalties. The current study demonstrated, 
that by increasing the EQR, the CH4 penalty from SPC could be 
eliminated without impacting the reduction in PM or causing an 
increase in NOx. The PM/NOx trade-off is escaped for the SPC 
strategy. PM does not increase for SPC cases by changing in-cylinder 
environment e.g. higher EGR level, higher EQR or higher pilot mass, 
which normally increases PM in mixing-controlled combustion.
The “optimized SPC point” (i.e. best point of the SPC cases with 
maximum PM reduction and same NOx and methane level as the 
baseline in the parameter sweeps at mode B75) removed over 90% of 
the PM with a 2% improvement in fuel efficiency while having 
almost the same level of NOx and methane. The drawback of this 
point is cycle to cycle variations and higher peak pressure rise rate in 
the cycle which leads to higher engine noise.
The relative location of ignition (or peak AHRR) and end of injection 
relative timing is important for the HPDI engine and can be used to 
define the SPC thresholds in future. Related to this finding, a metric 
could be defined as the fuel injected portion at the time of ignition 
(SPC factor=100% when ignition is at the EOI). For defining this 
metric, knowledge of injector behavior is required (momentum 
measurement or fuel rate shape). Defining premixing by other metrics 
rather than RIT might help to generalize the results of the research 
and make it independent of engine or injector specific parameters. 
More experiments might be required to confirm this for a wide range 
of parameters e.g. different modes, gas rail pressures and CA50. The 
conceptual LTC for diesel combustion also suggests that LTC results 
in a distinctive spatial pattern of PM formation, but whether or not 
this applies to SPC could not be determined in this work.
Although the reacting-flow CFD code used in this work did not 
correctly predict the ignition of the premixed natural gas, CFD 
captured the main trends in PM emissions. For SPC cases, much less 
PM is formed in the cylinder and the PM will be oxidized quickly in 
the cylinder after EOI. Higher EGR or EQR will increase the peak 
PM formed in-cylinder slightly, but have almost no effect on PM by 
the end of cycle. This trend has been noticed in the engine-out PM 
from the experiments as well. The EQR distribution of the jet at the 
ignition point for the baseline case and the SPC case were compared. 
At the gas ignition time, there is still significant fuel in the rich zone 
for the baseline point; over 50% of the fuel is within 2<EQR<5 
(defined as Z
rich). For the SPC point, the Zrich is less than 10%, 
therefore the potential for soot formation is mainly eliminated.
The main goal of this study was to consider the slightly premixed 
combustion as a solution for PM reduction in high loads. The 
study showed that this solution can be used to reduce PM majorly 
from this mode; considering the side effects. For the low loads, 
PM is not a major issue and using slightly premixed combustion 
has fewer justifications, although lower fuel consumption is still 
very interesting. Since the injector can be controlled in different 
modes by ECU, there is no need to select a single strategy for the 
entire engine map.
References
1. Harrington J., Munshi S., Nedelcu C., Ouellette P ., Thompson 
J., and Whitfield S., “Direct Injection of Natural Gas in a 
Heavy-Duty Diesel Engine Reprinted From?: Diesel Engine 
Experiments,” in International Spring Fuels & Lubricants 
Meeting & Exhibition Reno, Nevada May 6-9, 2002, 2002.
2. Faghani, E., Kheirkhah, P ., Mabson, C., McTaggart-Cowan, 
G., et al., “Effect of Injection Strategies on Emissions from 
a Pilot-Ignited Direct-Injection Natural-Gas Engine- Part I: 
Late Post Injection,” SAE Tech. Paper 2017-01-0774, 2017, 
doi:10.4271/2017-01-0774.
3. Kellerer H., Koch R., and Wittig S., “Measurements of the 
growth and coagulation of soot particles in a high-pressure shock 
tube,” Combust. Flame, vol. 120, no. 1, pp. 188-199, 2000.
4. Dobbins R., “Soot inception temperature and the carbonization 
rate of precursor particles,” Combust. Flame, vol. 130, no. 3, pp. 
204-214, 2002.
5. Park C. and Appleton J., “Shock-tube measurements of soot 
oxidation rates,” Combust. Flame, vol. 20, no. 3, pp. 369-379, 
1973.
6. Huestis, E., Erickson, P ., and Musculus, M., "In-Cylinder and 
Exhaust Soot in Low-Temperature Combustion Using a Wide-
Range of EGR in a Heavy-Duty Diesel Engine," SAE Technical 
Paper 2007-01-4017, 2007, doi:10.4271/2007-01-4017.
7. Kook, S., Bae, C., Miles, P ., Choi, D. et al., "The Influence of 
Charge Dilution and Injection Timing on Low-Temperature 
Diesel Combustion and Emissions," SAE Technical Paper 2005-
01-3837, 2005, doi:10.4271/2005-01-3837.
8. Zhao F ., “Homogeneous charge compression ignition (HCCI) 
engines: key research and development issues,” Soc. Automot. 
Eng., 2003.
9. Kimura, S., Aoki, O., Ogawa, H., Muranaka, S. et al., "New 
Combustion Concept for Ultra-Clean and High-Efficiency Small 
DI Diesel Engines," SAE Technical Paper 1999-01-3681, 1999, 
doi:10.4271/1999-01-3681.
10. Kanda, T., Hakozaki, T., Uchimoto, T., Hatano, J. et al., "PCCI 
Operation with Early Injection of Conventional Diesel Fuel," SAE 
Technical Paper 2005-01-0378, 2005, doi:10.4271/2005-01-0378.
11. Okude, K., Mori, K., Shiino, S., and Moriya, T., "Premixed 
Compression Ignition (PCI) Combustion for Simultaneous 
Reduction of NOx and Soot in Diesel Engine," SAE Technical 
Paper 2004-01-1907, 2004, doi:10.4271/2004-01-1907.
12. Bobba, M., Genzale, C., and Musculus, M., "Ef fect of Ignition 
Delay on In-Cylinder Soot Characteristics of a Heavy Duty 
Diesel Engine Operating at Low Temperature Conditions," SAE 
Int. J. Engines 2(1):911-924, 2009, doi:10.4271/2009-01-0946.
13. Lachaux T. and Musculus M. P. B., “In-cylinder unburned 
hydrocarbon visualization during low-temperature compression-
ignition engine combustion using formaldehyde PLIF,” Proc. 
Combust. Inst., vol. 31, no. 2, pp. 2921-2929, Jan. 2007.
14. Musculus, M., "Multiple Simultaneous Optical Diagnostic 
Imaging of Early-Injection Low-Temperature Combustion in 
a Heavy-Duty Diesel Engine," SAE Technical Paper 2006-01-
0079, 2006, doi:10.4271/2006-01-0079.
Downloaded from SAE International by Dalian Univ of Technology, Monday, August 31, 2026

<!-- PDF_PAGE: 11 -->

15. Musculus, M., Lachaux, T., Pickett, L., and Idicheria, C., "End-of-
Injection Over-Mixing and Unburned Hydrocarbon Emissions in 
Low-Temperature-Combustion Diesel Engines," SAE Technical 
Paper 2007-01-0907, 2007, doi:10.4271/2007-01-0907.
16. Musculus M. P . B., Miles P. C., and Pickett L. M., “Conceptual 
models for partially premixed low-temperature diesel 
combustion,” Prog. Energy Combust. Sci., vol. 39, no. 2-3, pp. 
246-283, Apr. 2013.
17. O'Connor , J. and Musculus, M., "Optical Investigation of 
the Reduction of Unburned Hydrocarbons Using Close-
Coupled Post Injections at LTC Conditions in a Heavy-Duty 
Diesel Engine," SAE Int. J. Engines 6(1):379-399, 2013, 
doi:10.4271/2013-01-0910.
18. McT aggart-Cowan, G., Bushe, W., Rogak, S., Hill, P. et al., 
"Injection Parameter Effects on a Direct Injected, Pilot Ignited, 
Heavy Duty Natural Gas Engine with EGR," SAE Technical 
Paper 2003-01-3089, 2003, doi:10.4271/2003-01-3089.
19. McT aggart-Cowan, G., Bushe, W., Rogak, S., Hill, P. et al., 
"PM and NOx Reduction by Injection Parameter Alterations in 
a Direct Injected, Pilot Ignited, Heavy Duty Natural Gas Engine 
With EGR at Various Operating Conditions," SAE Technical 
Paper 2005-01-1733, 2005, doi:10.4271/2005-01-1733.
20. McT aggart-Cowan G. P., Mann K., Wu N., Huang J., and 
Munshi S. R., “Particulate Matter Reduction from a Pilot-
Ignited, Direct Injection of Natural Gas Engine,” in Proceedings 
of the ASME Internal Combustion Engine Division’s 2012 Fall 
Technical Conference (ICEF2012), 2012.
21. Faghani, E., Patychuk, B., McT aggart-Cowan, G., and Rogak, 
S., "Soot Emission Reduction from Post Injection Strategies 
in a High Pressure Direct-Injection Natural Gas Engine," SAE 
Technical Paper 2013-24-0114, 2013, doi:10.4271/2013-24-0114.
22. Patychuk B. D., “Particulate Matter Emission Characterization 
From a Natural Gas High-Pressure Direct-Injection Engine,” 
MASc Thesis, The University Of British Columbia, 2013.
23. McT aggart-Cowan G. P., “Pollutant Formation in a Gaseous-
Fuelled, Direct Injection Engine,” Doctoral Thesis, The 
University of British Columbia, 2006.
24. Faghani E., “Ef fect of injection strategies on particulate matter 
emissions from HPDI natural-gas engine,” PhD Thesis, The 
University of British Columbia, 2015.
25. Heywood J. B., Internal Combustion Engine Fundamentals. 
New York: Mcgraw-hill, 1988.
26. Huang J., “Natural gas combustion under engine-relevant 
conditions,” Doctoral Thesis, The University of British 
Columbia, 2006.
27. Kheirkhah P ., “CFD Modelling of Non-Conventional Injection 
Strategies in a High-Pressure Direct-Injection (HPDI) Natural 
Gas Engine,” The University of British Columbia, 2015.
28. Faghani, E., Kirchen, P ., and Rogak, S., "Application of Fuel 
Momentum Measurement Device for Direct Injection Natural 
Gas Engines," SAE Technical Paper 2015-01-0915, 2015, 
doi:10.4271/2015-01-0915.
29. Kheirkhah P ., “CFD modeling of injection strategies in a High-
Pressure Direct- Injection (HPDI) natural gas engine,” MASc 
Thesis, The University of British Columbia, 2015.
30. Jones H. L., “Source and Characterization of Particulate Matter 
from a Pilot-Ignited Natural Gas Fuelled Engine,” MASc 
Thesis, The University of British Columbia, 2004.
31. Mabson C. W. J., “Emissions Characterization of Paired 
Gaseous Jets in a Pilot-Ignited Natural -Gas Engine,” MASc 
Thesis, The University Of British Columbia, 2015.
32. Dastanpour R. and Rogak S. N., “Observations of a Correlation  
between Primary Particle and Aggregate Size for Soot Particles,” 
Aerosol Sci. Technol., vol. 48, no. 10, pp. 1043-1049, Aug. 2014.
33. Kamimoto, T. and Bae, M., "High Combustion Temperature for 
the Reduction of Particulate in Diesel Engines," SAE Technical 
Paper 880423, 1988, doi:10.4271/880423.
34. Goodwin G., “An open source, extensible software suite for 
CVD process simulation,” in Proceedings of CVD XVI and 
EuroCVD Fourteenl, 2003, 2003.
Contact Information
Ehsan Faghani
ehsan.faghani@volvo.com
Engine Testing and Laboratories, V olvo Penta, V olvo AB, 
Gothenburg, Sweden
Acknowledgments
The work reported here was funded by the Natural Sciences and 
Engineering Research Council of Canada and Westport Innovations 
Inc. through the Automotive Partnerships Canada program. The 
authors wish to thank UBC engine technician Mr. Bob Parry. We 
would also like to acknowledge the support and technical guidance 
from Westport, especially Sandeep Munshi, Jim Huang, Ning Wu, 
and Bronson Patychuck.
Definitions/Abbreviations
AHRR - Apparent heat release rate
CAD - Crank angle
CA50 - 50% of total heat release rate (° ATDC)
DI - Direct-injection
DRX - TSI DustTrak DRX
EGR - Exhaust gas recirculation
EQR - Global oxygen based equivalence ratio
GIMEP - Gross-indicated mean effective pressure
GPW - Gas pulse width
GRP - Gas Rail Pressure
GSOI - Gas start of injection, command signal
HPDI - High-pressure direct-injection natural gas engine
NG - Natural gas
PM - Particulate matter
Downloaded from SAE International by Dalian Univ of Technology, Monday, August 31, 2026

<!-- PDF_PAGE: 12 -->

PPW - Pilot pulse width
PSOI - Pilot start of injection
RIT - Relative injection timing
SCRE - Single cylinder research engine
SMPS - Scanning mobility particle spectrometer
TEM - Transmission electron microscope
TEOM - Tapered element oscillating microbalance
Greek Letters
φ - Local Oxygen based equivalence ratio
Downloaded from SAE International by Dalian Univ of Technology, Monday, August 31, 2026

<!-- PDF_PAGE: 13 -->

APPENDIX
APPENDIX A: MULTI-INJECTOR TESTS
The robustness of the SPC strategy is studied here for five different injectors of the same model of experimental prototype injector. No attempt was 
made to adjust or assess the performance of these injectors prior to being tested on the SCRE. Beside the baseline injector, UBC default injector, 
which controlled and quality checked frequently; the status of the other injectors were unknown and the injectors were not in use for a long time. The 
objective of the current set of experiments was to test the robustness of the SPC tests for a rather random set of injectors. More information about the 
tests, including the test matrix, is included in Reference [24]. In this appendix we only discuss the results of “perfectly trimmed” injector durations to 
deliver same amount of fuel.
The PM reduction is 75-88% variable between the injectors compared to their baseline values. This study here is only a preliminary investigation and 
more controlled investigations are required in future to answer the questions regarding the performance of the injectors.
Table A1. Normalized Emission and injector performance for SPC points for different injectors.
APPENDIX B: METHANE EMISSION AND IGNITION DWELL
Figure B1 shows the engine-out methane as a function of ignition dwell. Ignition dwell is defined as the time from gas ignition to end of injection 
(Gign-EOI). This is the same information shown in Figure 4 (b), but here it is repotted based on ignition dwell. The same trend in UHC has been 
reported in the diesel engine literature [15] for a wide range of diesel operating conditions by Cummins Inc. Based on the optical measurement, long 
ignition dwells and long mixing times leave very lean, over-mixed regions close to the nozzle due to the end of injection rapid mixing and this 
contributes significantly to UHC emissions for LTC diesel engines [13], [15]. We cannot verify the source of methane in our experiments; however, 
the significance of EOI in methane increase is reported here as an interesting observation.
Figure B1. Engine-out methane versus ignition dwell from the SCRE experiments.
APPENDIX C: CFD PREDICTION OF AHRR FOR BASELINE AND SPC CONDITIONS
The baseline point and some SPC points (RIT=-0.3 ms with different EGR-EQR levels) were simulated. The AHRR graphs of baseline and SPC 
conditions are shown in Figure C1. There is good agreement between CFD and measurement for the baseline condition, but not for SPC.
Downloaded from SAE International by Dalian Univ of Technology, Monday, August 31, 2026

<!-- PDF_PAGE: 14 -->

Figure C1. Predicted (CFD) apparent heat release rate of baseline and SPC case compared with the experiments. The green dashed line is the NG fuel rate shape and the 
red dashed line is the pilot fuel rate shape.
The Engineering Meetings Board has approved this paper for publication. It has successfully completed SAE’s peer review process under the supervision of the session organizer. The process 
requires a minimum of three (3) reviews by industry experts. 
All rights reserved. No part of this publication may be reproduced, stored in a retrieval system, or transmitted, in any form or by any means, electronic, mechanical, photocopying, recording, or 
otherwise, without the prior written permission of SAE International.
Positions and opinions advanced in this paper are those of the author(s) and not necessarily those of SAE International. The author is solely responsible for the content of the paper.
ISSN 0148-7191
http://papers.sae.org/2017-01-0763
Downloaded from SAE International by Dalian Univ of Technology, Monday, August 31, 2026
