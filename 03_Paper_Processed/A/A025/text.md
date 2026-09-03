<!-- PDF_PAGE: 1 -->

Contents lists available at ScienceDirect
Proceedings of the Combustion Institute
journal homepage: www.elsevier.com/locate/proci
Modeling hydrogen–diesel dual direct injection combustion with FGM and
transported PDF
Tommaso Lucchini a,∗, Andrea Schirrua, Marco Mehlb, Gianluca D’Erricoa,
Patrick Rorimpandey c, Qing Nian Chanc, Sanghoon Kookc, Evatt R. Hawkesc
a Department of Energy, Politecnico di Milano, 20156, Italy
b Department of Chemistry Materials and Chemical Engineering ‘‘G. Natta’’, Politecnico di Milano, 20133, Italy
c School of Mechanical and Manufacturing Engineering, The University of New South Wales, NSW 2052, Australia
A R T I C L E I N F O
Keywords:
Hydrogen Direct Injection Dual-Fuel
Combustion (H2DDI)
Flamelet generated manifold (FGM)
Eulerian Monte–Carlo fields (EMCF)
Tabulated kinetics
A B S T R A C T
This work extends the transported probability density function (PDF) method to model hydrogen–diesel dual
direct injection (H2DDI) combustion, where a H2 jet is ignited by a small pilot diesel jet flame. The work is
motivated by previous H2DDI engine tests where stable compression ignition engine operation was reported
with up to 90 % H2 supply by energy share. To help explain this high performance and provide a tool
to help further engine optimization, the Eulerian Monte Carlo Fields (EMCF) solution method is employed
with which a transported PDF equation is solved in combination with Flamelet Generated Manifold (FGM)
for high accuracy and computational efficiency. In all cases, the pilot fuel ignites before interacting with
the H2 jet and thus reaction rate and chemical composition are computed as the weighted average of the
corresponding values taken for two separated FGM tables generated for the two fuels. Pressure measurements
and high-speed schlieren imaging performed in a preburn-type optical constant volume combustion chamber
(CVCC) with n-heptane ( 𝑛C7H16) pilot fuel were used to validate the EMCF+FGM model. The application
focus is how H2 ignition and combustion is affected when the 𝑛C7H16 is injected prior to or after the main
H2 jet. EMCF+FGM computed heat release rate and flame structure were compared with experimental data
and results from conventional FGM model based on presumed PDF. When applied to H2DDI combustion, the
EMCF+FGM model successfully reproduces flame structures and heat release rate under different injection
strategies, including the transition towards partially-premixed combustion when the 𝑛C7H16 pilot follows the
main H2 injection. Moreover, analysis of heat release rate from different stochastic fields can provide a useful
indication about cyclic variability and combustion stability.
1. Introduction
Direct-injection, dual-fuel combustion (DIDF) represents a promis-
ing solution for achieving high efficiency and reduced greenhouse gas
emissions in compression-ignition (CI) engines. In DIDF engines, a pilot
injection of high Cetane Number (CN) fuel (diesel, HVO, DME) ignites a
jet of high Octane Number (ON) low-carbon energy carrier, which then
burning, presumably, under mixing-controlled or partially-premixed
combustion. DIDF has been successfully tested with hydrogen [ 1],
natural gas (NG) [ 2], methanol [ 3] and ammonia [ 4] as the high
ON energy carrier. Dedicated injection technologies allow the direct
injection of both fuels in liquid or gas state at suitable timings, making
possible to operate the engine under diffusive, partially-premixed and
premixed combustion modes [5,6].
Experimental results indicate that, compared to conventional diesel
combustion, DIDF can increase indicated efficiency while reducing
∗ Corresponding author.
E-mail address: tommaso.lucchini@polimi.it (T. Lucchini).
combustion noise, soot and HC emissions. By employing renewable or
low-carbon fuels, DIDF can contribute to the decarbonization of hard-
to-electrify sectors. Relative to conventional single fuel compression
ignition, dual fuels have been relatively underexplored from a fun-
damental or modeling perspective. A limited number of experimental
studies conducted in constant volume chambers have provided insights
into clarifying how flame structure and heat release rate are affected
by the injection strategy, ambient conditions and amount of energy
released by the high ON fuel [ 7–9]. In [ 10–12], DIDF combustion
was modeled using direct integration of detailed kinetics, without
accounting for turbulence–chemistry interaction.
To overcome the existing limitations and provide a computation-
ally efficient solution for near-term application in the development
of dual-fuel engines, this work combines the transported probability
density function (PDF) method with the Flamelet Generated Manifold
https://doi.org/10.1016/j.proci.2024.105213
Received 2 December 2023; Accepted 29 May 2024
Proceedings of the Combustion Institute 40 (2024) 105213 
Available online 24 July 2024 
1540-7489/© 2024 The Author(s). Published by Elsevier Inc. on behalf of The Combustion Institute. This is an open access article under the CC BY license 
( http://creativecommons.org/licenses/by/4.0/ ).

<!-- PDF_PAGE: 2 -->

T. Lucchini et al.
(FGM) to model DIDF combustion. The Eulerian Monte Carlo Field
(EMCF) method was selected, wherein the PDF is represented by a
set of stochastic fields (ESFs) transported within the Eulerian frame-
work. Each field encompasses both the fuel mixture fractions and the
progress variable, which are then used to access the FGM look-up
table to determine the reaction rate and chemical composition. Recent
works [13–15] have applied the EMCF+FGM approach to simulate
spray combustion, stratified non-premixed flames and non-premixed
bluff-body stabilized CH 4/H2 flames. Two separate look-up tables are
employed for the involved fuels with the local cell composition and
reaction rates computed as the single-fuel mixture fraction weighted
average of the corresponding FGMs. Since no assumptions are made on
the mixture fraction and the progress variable PDF, the proposed novel
approach for the DIDF combustion is expected to predict the variations
in the main fuel flame structure with the injection strategy: from a
pure diffusion flame if the pilot injection happens before the main to a
partially premixed flame in the opposite case. Flow and stochastic field
equations are solved with the RANS approach.
Constant-volume combustion chamber (CVCC) combustion exper-
iments performed with different pilot injection strategies were used
for a comprehensive validation of the proposed EMCF+FGM model for
DIDF combustion [7]. The selected operating conditions, where the
pilot fuel ignites before interacting with the main jet, represent a solid
and simple configuration where it is possible to extensively assess the
proposed combustion model and verify the validity of the assumption
of using two separated FGMs. To further understand the advantages of
EMCF+FGM for H2DDI combustion simulations, computed results were
compared also with conventional FGM with a presumed PDF approach.
The proposed simulation approach has been implemented in the Lib-
ICE code, which is a set of libraries and solvers for IC engines simulation
based on the OpenFOAM ®technology [16,17].
2. Numerical models
2.1. Flamelet Generated Manifolds (FGM) for DIDF combustion
FGM represents a computationally efficient and accurate solution to
incorporate detailed kinetics in CFD simulations. The combined effects
of chemistry and flame structure are incorporated in the progress vari-
able 𝐶 and its reaction rate ̇ 𝜔𝐶. The FGM look-up table stores reaction
rates and chemical compositions from processed calculation results
assuming a pre-defined flame structure (0D homogeneous constant-
pressure reactor, 1D constant-pressure laminar diffusion flame, . . . )
with different values of oxidizer temperature 𝑇𝑜𝑥, mixture fraction 𝑍,
pressure 𝑝 and stoichiometric scalar dissipation rate 𝜒𝑠𝑡. The FGM look-
up table provides the ̇ 𝜔𝐶 and the chemical composition as functions of
the local cell values of 𝑇𝑜𝑥, 𝑍, 𝑝, 𝜒𝑠𝑡 and the normalized progress vari-
able 𝑐 = (𝐶 − 𝐶𝑚𝑖𝑛
)∕ (𝐶𝑚𝑎𝑥 − 𝐶𝑚𝑖𝑛
). 𝐶 is set equal to the heat released
by combustion, computed as the difference between the current and
the initial value of the reactor enthalpy of formation, also known as
ℎ298 [18]. Since in H2DDI combustion the pilot fuel (𝑝) is ignited before
interacting with the main (𝑚) jet, two separate tables are generated for
the two fuels and reaction rates and chemical composition (hereinafter
referred as 𝜓𝑎) are computed as average of the corresponding tabulated
values weighted on the pilot and main fuel mixture fractions 𝑍𝑝 and
𝑍𝑚, respectively:
𝜓𝑎 =
𝑍𝑝
𝑍𝑝 + 𝑍𝑚
⋅ 𝜓𝑎,𝑝 + 𝑍𝑚
𝑍𝑝 + 𝑍𝑚
⋅ 𝜓𝑎,𝑚 (1)
with (𝑍𝑝 + 𝑍𝑚
) being equal to the global mixture fraction 𝑍. The
oxidizer mass fraction 𝑌𝑜𝑥 is assumed to be evenly distributed among
the two fuels in every computational cell:
𝑍𝑝
𝑍𝑚
=
𝑌𝑜𝑥,𝑝
𝑌𝑜𝑥,𝑚
(2)
hence they react under the same A/F ratio identical to the global one.
Consistently, both the tables are accessed with the same values of 𝑇𝑜𝑥
and 𝑍. Transport equations need to be solved for 𝑍𝑝 and 𝑍𝑚 including
evaporation source terms, if liquid, and injection boundary condition,
if in gas phase.
In the simulated H2DDI conditions, featuring the ignition of a H 2
jet by a pilot injection of 𝑛C7H16, two distinct flame structures were
considered. A transient laminar diffusion flame was employed for the
𝑛C7H16 pilot jet to accurately describe the high cetane number (CN)
fuel ignition occurring after the end of injection, during which mixing
is less intense and the mixture becomes leaner. For the H 2 main jet,
auto-igniting homogeneous constant-pressure reactors were used, as
unsteady H 2 flamelets proved unsuitable for auto-ignition under the
conditions encountered in the H2DDI experiments.
A dedicated OpenFOAM solver was developed by the authors to
generate Laminar Diffusion FGM tables, it integrates the Dynamic Load
Balancing (DLB) library for fast and efficient chemistry integration
using a pre-computed analytical Jacobian and an optimized ODE solver
following [19]. Homogeneous reactor FGM tables were produced using
the OpenSMOKE++ [20] library.
The chemical n-heptane mechanism used in this work is a reduced
one from [21,22] with 110 species and 1802 reactions. Mechanism
reduction consists in lumping and eliminating species based on flux
and sensitivity analysis. At each reduction step the model performance
is compared to the one of the parent mechanisms imposing toler-
ances in the 10%–15% range for constant volume ignition delay times.
The reduced mechanism combines a fairly detailed description of the
chemistry of light species (C0-C3) and a lumped mechanism for the
heavier components. This approach allows for an accurate reproduction
of the fuel reactivity over a wide range of conditions with a limited
computational burden.
2.2. Presumed PDF combustion model
The probability density function (PDF) of the principal variables
required to compute 𝜓𝑎 is assumed to be statistically independent. Each
variable follows a prescribed PDF distribution: a 𝛽 distribution for the
mixture fraction and a 𝛿 function for the progress variable [23].
2.3. Eulerian Monte Carlo Fields (EMCF+FGM) transported PDF combus-
tion model
In the EMCF method [24–26], the unresolved scale fluctuations and
the joint-PDF are represented by the 𝑁𝑠𝑓 number of Eulerian stochastic
fields. Each field, 𝜉(𝑗)
𝑎 , does not represent a specific flow realization,
but it is just a mathematical concept. The average of the ESFs yields
the resolved fields. 𝜉(𝑗)
𝑎 includes chemical composition 𝑌 , enthalpy ℎ,
oxidizer enthalpy ℎ𝑜𝑥 (used to estimate the oxidizer temperature, 𝑇𝑜𝑥
under variable pressure conditions), progress variable𝐶, pilot and main
fuel mixture fractions 𝑍𝑝 and 𝑍𝑚, respectively:
𝜉(𝑗) = (𝑌𝑖,1, … , 𝑌𝑛, ℎ, ℎ𝑜𝑥, 𝑍𝑝, 𝑍𝑚, 𝐶) (3)
In the context of the FGM approach, stochastic partial differential
equations (SPDEs) are solved in each stochastic field for 𝑍𝑝, 𝑍𝑚, ℎ, ℎ𝑜𝑥
and 𝑐 in the conservative form [27]:
𝑑 ̄ 𝜌𝜉(𝑗)
𝑎 = − 𝜕 ̄ 𝜌 ̃ 𝑢𝑖𝜉(𝑗)
𝑎
𝜕𝑥𝑖
𝑑𝑡 + 𝜕
𝜕𝑥𝑖
[
(𝛤 + 𝛤𝑡
)𝜕𝜉 (𝑗)
𝑎
𝜕𝑥𝑖
]
𝑑𝑡
+ 1
2 ̄ 𝜌𝐶𝜙
̃ 𝜀
̃𝑘
(𝜉(𝑗)
𝑎 − ̃ 𝜓𝑎
)𝑑𝑡
+ ̄ 𝜌
√
2 (𝛤 + 𝛤𝑡
)𝜕𝜉 (𝑗)
𝑎
𝜕𝑥𝑖
𝑑𝑊𝑖
+ ̇𝑆𝑠𝑝𝑟𝑎𝑦𝑑𝑡 + ̇𝑆𝐹 𝐺𝑀 𝑑𝑡 + ̇𝑆𝑝𝑑𝑡
(4)
The first and second terms on the right-hand side of Eq. (4) repre-
sent diffusion and convection. The third term is micro-mixing, which
is modeled by the Interaction by Exchange with the Mean (IEM) ap-
proach. The fourth term is the stochastic Wiener process, representing
Proceedings of the Combustion Institute 40 (2024) 105213 
2

<!-- PDF_PAGE: 3 -->

T. Lucchini et al.
Fig. 1. View of the hydrogen and diesel injectors layout within the combustion
chamber, representing hydrogen (blue) and n-heptane jet cones (red).
the production of scalar fluctuations due to the turbulent diffusivity.
Additional source terms account for spray evaporation/heat transfer
( ̇𝑆𝑠𝑝𝑟𝑎𝑦, assumed to be the same for every field), pressure material
derivative in enthalpy equation ̇𝑆𝑝 = 𝑑𝑝
𝑑𝑡 and progress variable reaction
rate ̇𝑆𝐹 𝐺𝑀 computed for each stochastic field according to Eq. ( 1).
The averaged thermochemical properties are then calculated from the
ensemble of 𝑁𝑠𝑓 notional fields:
̃ 𝜓𝑎 = 1
𝑁𝑠𝑓
𝑁𝑠𝑓∑
𝑗=1
𝜉(𝑗)
𝑎 (5)
This equation is used for calculation of the fields𝑍𝑝, 𝑍𝑚, 𝑌 , 𝐶, ℎ and
ℎ𝑜𝑥 [27]. 𝑑𝑊𝑖 is computed as 𝜂𝑖
√
𝑑𝑡 where 𝜂𝑖 is a {−1, +1} dichotomic
random vector. To ensure zero-mean of 𝑑𝑊𝑖, only an even number of
stochastic fields 𝑁𝑠𝑓 is considered and 𝜂𝑛
𝑖 = 1 is assigned to a randomly
chosen half of the fields, while 𝜂𝑛
𝑖 = −1 is assigned to the other
half, repeating this for each of the physical dimensions ( 𝑖 = 1 , 2, 3).
Recommendations from [27] were followed for the computation of the
𝜕𝜉 (𝑗)
𝑎
𝜕𝑥𝑖
, using limited gradient schemes and an analytical formulation to
compute the IEM mixing model contribution 1
2 ̄ 𝜌𝐶𝜙
̃ 𝜀
̃𝑘
(
𝜉(𝑗)
𝑎 − ̃ 𝜓𝑎
)
𝑑𝑡.
2.4. Solver details
Both combustion models were implemented into a RANS, compress-
ible solver with Lagrangian spray description, while the PISO algorithm
handles the pressure–velocity coupling. The 𝑘 − 𝜀 model was used to
compute the turbulent viscosity. Details of the spray model setup are
reported in [16] where it was validated for similar ambient conditions,
injection duration and nozzle geometry [ 28].
3. Experimental validation
3.1. Optical constant-volume combustion chamber
H2 and n-heptane were injected into a cubical, high-pressure CVCC
using a modified single-hole gasoline direct injection injector and a
common-rail single-hole diesel fuel injector, respectively. The H 2 and
n-heptane injectors operated at injection pressures of 14 MPa and
70 MPa, respectively. The diesel fuel injector was positioned 12.3 mm
above the H 2 injector, angled at 12 deg towards the H 2 injection
axis. The injection durations were set at 3.3 ms for H 2 and 0.7 ms
for n-heptane, under ambient conditions of 5.2 MPa pressure, 890 K
temperature, and 21 vol.% O2 (see Fig. 1). A z-type high-speed schlieren
imaging setup was used to visualize flame structures and identify
the jet boundary and high-temperature reaction zone. The CVCC was
also equipped with a high-speed pressure transducer for determining
pressure-based ignition delay times [ 7] (see Table 1).
Table 1
Summary of injection conditions [ 7].
Fuel 𝑛C7H16 H2
Nozzle diameter [mm] 0.105 0.58
Fuel reservoir pressure [MPa] 70 20
Hydraulic injection duration [ms] 0.7 3.3
Mass injected [mg] 0.99 5.28
Energy share [%] 6.4 93.6
Table 2
Summary of the simulated cases, settings and corresponding notations. Bold texts are
the reference conditions.
SOI [ms] Injection
𝑛C7H16 H2 strategy
H-0.07 ms-D 0.07 ms 0 Main-pilot
H-2.07 ms-D 2.07 ms 0 Main-pilot
H-3.07 ms-D 3.07 ms 0 Main-pilot
D-1.93 ms-H 0 1.93 ms Pilot-main
Fig. 2. Detail of the computational mesh in the vessel symmetry plane for the H2DDI
combustion simulations.
3.2. Simulated conditions and model setup
The conditions, reported in Table 2 , were selected to evaluate the
combustion model capability to predict the effect of the injection strat-
egy. The first tested condition, assumed as baseline, is characterized
by a quasi simultaneous start of injection for both 𝑛C7H16 and H 2.
Main fuel is injected before the pilot fuel in conditions 1-2-3 while the
opposite happens in 4.
Simulations were carried out in a 3-D mesh reproducing the entire
CVCC geometry of cubical combustion chamber with each side measur-
ing 114 mm. Fig. 2 reports the grid structure in the chamber symmetry
plane cutting the H 2 nozzle. Fixed refinement zones were placed to
predict the evolution of both the jets with minimum sizes which were
selected to be of the order of magnitude of the nozzle diameters,
avoiding too low void fraction values where spray particles evolve and
solving the flow scales that are relevant for fuel–air mixing. The total
number of cells is about 450,000. An injection profile typical of single-
hole sprays was imposed for 𝑛C7H16 [28] while the H 2 injection rate,
assumed to be a top-hat profile, was tuned to match the experimental
evolution of the corresponding jet penetration length. Wall temperature
was set to 500 K, initial turbulence intensity was assumed to be
0.25 m/s. The FGM tables were generated for the 𝑇𝑜𝑥 = 750−1000 K
and 𝑝 = 4−7 MPa intervals, covering the 𝜙 = 0.05−6 range. The latter is
assumed to be the flammability interval for both the fuels. The 𝑛C7H16
FGM tables is based on unsteady flamelets calculations performed with
8 values of the stoichiometric scalar dissipation rate 𝜒𝑠𝑡, spanning the
1 − 200 s−1 interval, to describe the mixing effects on the ignition
process.
3.3. Baseline condition, H-0.07 ms-D
EMCF+FGM simulations were performed using 𝑁𝑠𝑓 = 16 ESFs,
which is twice the suggested value from [ 27]. A sensitivity analysis
was also performed under varied conditions, and it was observed that
increasing 𝑁𝑠𝑓 did not result in discernible impact on the outcomes.
The time-step was dynamically adjusted to keep a constant Courant
Proceedings of the Combustion Institute 40 (2024) 105213 
3

<!-- PDF_PAGE: 4 -->

T. Lucchini et al.
Fig. 3. Baseline condition: main-pilot strategy, SOI Pilot = 0.07 ms. (a): comparison between experimental and computed heat release rate profiles; (b): comparison between
processed schlieren images and temperature field evolution. Schlieren: red line: unreacted n-heptane jet; blue line: unreacted H 2 jet, green line: reacted region. Computational:
blue line: mixture fraction 𝑍 = 0.001 contour; green line: normalized progress variable 𝑐 = 0.5 contour.
Number equal to 2.5. EMCF+FGM simulations take approximately five
times longer than the time required for the PDF+FGM under identical
conditions. In the simulated cases, the maximum discrepancy between
estimated fuel mass from the mixture fraction transport equation and
that computed from EMCF+FGM was less than 3%.
Fig. 3 provides a summary of the combustion process, compar-
ing computed and experimental Heat Release Rate (HRR) profiles (a)
and flame structure (b). Both the PDF+FGM and EMCF+FGM mod-
els predict similar ignition delay values, validating the effectiveness
of the models in describing the auto-ignition process for a diffusion
flame [ 23,29]. The EMCF+FGM model, which also accounts for the
PDF of the progress variable, predicts a lower HRR peak with an
extended duration of the auto-ignition phase. The ignition delay is
overestimated by approximately 0.2 ms, a discrepancy that could be
attributed to the kinetic mechanism. After the ignition of the H 2 jet
by 𝑛C7H16, both models estimate the same HRR during the mixing
controlled combustion phase. Differences between the experiments and
simulation results towards the end of injection phase can be attributed
to the assumed injection profile for the H 2 jet.
Fig. 3(b) presents a comparison between high-speed schlieren im-
ages, showing the flame structure evolution, and the computed image
taken along the chamber’s symmetry plane. The figure also reports
computed temperature distributions, together with the global mixture
fraction 𝑍𝑝 + 𝑍𝑚 = 0 .001 (blue) and normalized progress variable
contour 𝑐 = 0 .5 (green). These are used to consistently track the jet
boundary and flame in alignment with the processed schlieren images.
Both models predict identical ignition delay. However, in the 0.8–
1.0 ms interval, the EMCF+FGM model burns less fuel compared to
PDF+FGM, which explains its reduced HRR peak. During the diffusive
combustion phase (1 and 1.4 ms), the inclusion of the PDF of 𝑍𝑝,
𝑍𝑚 and the progress variable makes the EMCF+FGM flame structure
showing more resemblance to the experimental one. This also leads to
a less intense reaction rate near the point where the pilot jet ignites
the H 2. Both models estimate the stabilization of the H 2 flame at
about 15 mm distance from the nozzle, a phenomenon that was not
observed in the experiments. Possible reasons for such discrepancy
could be related to the adopted kinetic mechanism, which does not
predict relevant H2 reaction rates in very rich equivalence ratio regions.
Results at t = 1.4 ms show also the ECMF+FGM model capability to
describe the complete burning of the 𝑛C7H16 jet, in agreement with the
experimental data.
Fig. 4 reports the computed evolution of chamber temperature as
a function of the global mixture fraction 𝑍 = 𝑍𝑝 + 𝑍𝑚. Markers are
colored with the 𝑍𝑚∕𝑍 ratio, to understand the jet-to-jet interaction.
For both the combustion models, 𝑛C7H16 ignites before interacting with
the H 2 jet at t = 0.8 ms. The main jet is first ignited in its lean side
(𝑍 < 𝑍 𝑠𝑡,H2 ; 𝑍𝑠𝑡,H2 = 0.028) by the already burned pilot fuel by progress
variable diffusion, and then a fully diffusion flame structure is almost
Fig. 4. Computed evolution of temperature as function of global fuel mixture fractions
𝑍 = 𝑍𝑝 + 𝑍𝑚, markers are colored with the 𝑍𝑚∕𝑍 ratio.
established at t = 0.9 ms. Since jet-to-jet interaction does not exist
before pilot ignition and diffusion is the reason for main ignition, the
assumption to linearly interpolate the reaction rates from two separated
tables could be acceptable for this specific H2DDI application. Future
improvements of this approach may include the definition of a non-
linear interpolation function able to characterize more accurately the
blending effects of the two fuels. The EMCF+FGM model that incor-
porates both mixture fractions and progress variable PDFs, exhibits a
prolonged ignition process and a wider range of conditions between the
H2 mixing line and the expected diffusion flame temperature profile.
3.4. Main-pilot strategy
Fig. 5 (a) compares the computed and experimental HRR profiles
for the H-2.07 ms-D case, where the pilot-dwell time was increased
by 2 ms than the baseline condition. Notably, H-2.07 ms-D has an in-
creased HRR peak and a reduced combustion duration, with the exper-
imental HRR profile mainly resembling those of premixed combustion
processes. Consistent with the baseline case, both models predict an
extended ignition delay, which may account for the overestimation of
the computed HRR peaks. Following the initial phase, the EMCF+FGM
model outperforms the PDF+FGM model in terms of both HRR intensity
and combustion duration, despite underestimation by both models.
To understand the quality of the computed results and the effect of
the mail-pilot injection dwell for the H-2.07 ms-D condition, Fig. 5 (b)
compares the computed and experimental flame structures, including
the H2 equivalence ratio 𝜙 contours, to further elucidate the dynamics
of the H 2 jet ignition process. At the time of 𝑛C7H16 ignition, a larger
Proceedings of the Combustion Institute 40 (2024) 105213 
4

<!-- PDF_PAGE: 5 -->

T. Lucchini et al.
Fig. 5. Main-pilot strategy, SOI Pilot = 2.07 ms. (a): experimental and computed heat release rate profiles; (b): comparison between processed schlieren images and temperature
field evolution. Schlieren: red line: unreacted n-heptane jet; blue line: unreacted H 2 jet, green line: reacted region. Computational: blue line: mixture fraction 𝑍 = 0 .001 contour;
green line: normalized progress variable 𝑐 = 0.5 contour; dashed lines report H 2 equivalence ratio contours ( 𝜙 = 0.5 − 1.5).
quantity of H2 is available for combustion, accounting for the increased
HRR peak. Consistent with the baseline condition, at t = 2.9 ms, the
PDF+FGM model exhibits more extensive H 2 combustion, with the
combustion reaching the jet tip in approximately 0.2 ms, showing a
rapid burning rate with flame propagation in all directions. Upon pilot
ignition, the established H2 jet exhibits a non-uniform mixing intensity
(scalar dissipation rate) that decreases along its length from the nozzle
to the tip. This promotes H 2 ignition, primarily governed by diffusion
in the jet radial direction, when the burnt pilot jet interacts with the
main jet at t = 2.8 and 2.9 ms. Post-ignition, schlieren images reveal
that the flame propagates more rapidly along the jet axis, where fuel
concentration is higher. The EMCF+FGM model better captures the
local mixing effects under extended main-pilot injection dwell: the
flame reaches the jet tip more rapidly along the axial direction where
0.5 < 𝜙 < 1.0, while more time is needed for radial flame propagation
where 𝜙 < 0.5. Understanding the ignition differences between baseline
and increased main-pilot dwell time makes it possible to further clarify
the HRR profiles. To this end, Fig. 6 (a)–(b) report the computed flame
indexes 𝜉 for the baseline and H-2.07 ms-D cases.𝜉 (𝑍𝑚, 𝑐)> 0 indicates
a partially premixed flame and it is computed from normalized progress
variable and 𝑍𝑚 mixture fraction gradients, following [ 30]:
𝜉 (𝑍𝑚, 𝑐)= 1
2
(
1 + ∇𝑍𝑚 ⋅ ∇𝑐
|∇𝑍𝑚||∇𝑐|
)
(6)
Immediately post ignition (t = 1.0 ms) and thereafter, the base-
line condition preserves a well consolidated diffusion flame structure
involving the injected H 2, consistent with the HRR profile typical of
mixing controlled combustion. The H-2.07 ms-D case behaves differ-
ently: at t = 2.9 ms, the flame index indicates diffusive ignition from
the burned 𝑛C7H16 in combination with partially premixed combustion
within the H 2 jet. The flame index analysis suggests that as the main-
pilot dwell time increases, partially premixed combustion becomes
increasingly important, affecting the heat release rate profile and ac-
celerating combustion. Mixing controlled combustion characterizes the
latter part of the H-2.07 ms-D, as some fuel is still injected after the
flame reaches the jet tip.
Further extending the main-pilot dwell to H-3.07 ms-D results in
partial burn of the H 2 jet in the experiments, with considerable vari-
ability between different tests. In contrast, the simulations predict
completed combustion. Nevertheless, Fig. 7 shows that the HRR traces
computed using stochastic fields can still provide useful insights into
the combustion stability. Despite ESFs not directly representing flow
realizations, the associated HRR profiles show that the H-3.07 ms-D
case exhibits a stronger variability in the onset of combustion compared
to H-2.07 ms-D, which also aligns with experimental findings of [7]. For
the H-3.07 ms-D condition, the flame index analysis in Fig. 6 (c) shows
that reduced diffusion inside the H 2 jet, following the end of main
injection, hinders ignition from the pilot jet, potentially explaining the
observed combustion instability.
Fig. 6. Computed flame index 𝜉 and temperature contours for the cases H-0.07 ms-D
(a), H-2.07 ms-D (b), H-3.07 ms-D (c) and D-1.93 ms-H (d).
Fig. 7. Comparison between experimental and computed HRR from the 16 ESFs for
H-2.07 ms-D and H-3.07 ms-D conditions.
3.5. Pilot-main strategy
The D-1.93 ms-H was selected for model validation in the pilot-
main strategy, where H 2 is injected 1.93 ms post the pilot jet SOI. The
flame index analysis in Fig. 6 (d) reports that this is a condition which
is primarily characterized by diffusive burning. Fig. 8 (a) compares
computed and experimental HRR profiles, revealing the presence of two
main local peaks: the first associated with the pilot fuel burn and the
second with the H 2 ignition by the 𝑛C7H16 jet. Both EMCF+FGM and
PDF+FGM predict the start of H 2 combustion reasonably well, despite
underestimating the HRR. The flame structure evolution in Fig. 8 (b)
suggests two potential explanations for this discrepancy: (a) ignition
begins very close to the main SOI, and the amount of injected H 2 at
that instant depends on the assumed injection profile, which appears
Proceedings of the Combustion Institute 40 (2024) 105213 
5

<!-- PDF_PAGE: 6 -->

T. Lucchini et al.
Fig. 8. Pilot-main strategy, SOI Main = 1,93 ms. (a): comparison between experimental and computed heat release rate profiles; (b): comparison between processed schlieren
images and temperature field evolution. Schlieren: red line: unreacted n-heptane jet; blue line: unreacted H 2 jet, green line: reacted region. Computational: blue line: mixture
fraction 𝑍 = 0.001 contour; green line: normalized progress variable 𝑐 = 0.5 contour.
to be slightly underestimated in the computed H 2 jet penetration;
(b) in simulations, the rich part of the H 2 jet does not completely
ignite and this could reduce the amount of fuel burning in the jet-
to-jet interaction. Both models predict an arching in the top part of
the main jet interaction with the 𝑛C7H16 flame. At 2.4 ms the flame
morphology prediction from the EMCF+FGM flame appears to show
better alignment with experimental data. However, in a condition
dominated by diffusion combustion, the differences between the two
models are minimal.
3.6. Conclusions
This work was focused on numerical modeling of Direct-Injection
Dual-Fuel combustion with tabulated kinetics and turbulence–chemistry
interaction. In particular, H2DDI combustion was investigated, where
a pilot injection of 𝑛C7H16 ignites a main H 2 jet. The developed
combustion model (EMCF+FGM) combines the Eulerian Monte Carlo
Field transported PDF with Flamelet Generated manifold to be compu-
tationally efficient and general. The EMCF+PDF model was extensively
validated considering different dwell timings between pilot and main
injections via a combined comparison between computed and experi-
mental schlieren images and heat release profiles. EMCF+FGM is able
to predict the diffusion-governed ignition of the main H2 jet by the pilot
𝑛C7H16 injection and the pure H 2 diffusion flame structure when the
pilot fuel is injected first. The main-pilot strategy is more challenging
since it involves a combination of ignition by diffusion, partially
premixed and fully diffusive combustion and the proposed model shows
better performance compared to presumed-PDF in describing the flame
structure and predicting the HRR profile. Computed results show that
the proposed CFD methodology can also be used for diagnostic purposes
since the flame index parameter could help understanding the nature
of the H2DDI combustion process and how it shifts from diffusive to
partially premixed by increasing the dwell time between main and pilot
injection events. Moreover, the analysis of HRR from stochastic field
could provide a useful indication about the variability of the ignition
start. The proposed EMCF+FGM model could represent an effective
solution to design DIDF engines operating with renewable fuels, which
could contribute to the decarbonization of road/maritime transport,
power generation and off-road applications.
Novelty and Significance Statement
The novelty of this research is a combustion model for direct-
injection, dual-fuel (DIDF) combustion which is a promising solution
for high efficient CI engines operating with low-carbon fuels. Despite
being a relevant topic for the engine comminity, DIDF was studied so
far with limited and simplified approaches. The proposed combustion
model, combining Eulerian Monte Carlo Field and Flamelet Generated
Manifold (EMCF+FGM) represents a computationally accurate and effi-
cient solution to study DIDF. The extensive validation carried out in this
work on Hydrogen-Diesel Dual Fuel Direct Injection (H2DDI) combus-
tion demonstrates the model capabilities to correctly describe the flame
structure and heat release rate for different injection strategies. This is
the first paper where EMCF+FGM results are compared to experimental
data both in terms of flame structure and heat release rate, representing
a significant step towards its application to real engine simulations for
hydrogen and other dual-fuel scenarios of significant interest.
CRediT authorship contribution statement
Tommaso Lucchini: Performing research, Writing paper, Devel-
opment of the combustion model, Post-processing results. Andrea
Schirru: Performing simulations. Marco Mehl: Kinetic scheme Devel-
opment. Gianluca D’Errico: Analyzing results, Writing paper. Patrick
Rorimpandey: Performing experiments, Analyzing results. Qing Nian
Chan: Design experiments, Analyzing results. Sanghoon Kook: Design
experiments, Analyzing results, Revising paper. Evatt R. Hawkes:
Revising paper, Analyzing results.
Declaration of competing interest
The authors declare that they have no known competing finan-
cial interests or personal relationships that could have appeared to
influence the work reported in this paper.
Acknowledgments
Part of this research was funded by ‘‘Ecosystem for Sustainable
Transition in Emilia-Romagna’’, project funded by European Union
under the National Recovery and Resilience Plan (NRRP), Mission 04
Component 2 Investment 1.5—NextGenerationEU. Call for tender n.
3277, Award Number: 0001052.
References
[1] L. Liu, Z. Wu, F. Tan, Y. Wang, CFD investigation the combustion characteristic
of ammonia in low-speed marine engine under different combustion modes, Fuel
351 (2023).
[2] M. Li, X. Zheng, Q. Zhang, Z. Li, B. Shen, X. Liu, The effects of partially premixed
combustion mode on the performance and emissions of a direct injection natural
gas engine, Fuel 250 (2019) 218–234.
[3] Y. Dong, O. Kaario, G. Hassan, O. Ranta, M. Larmi, B. Johansson, High-pressure
direct injection of methanol and pilot diesel: A non-premixed dual-fuel engine
concept, Fuel 277 (2020).
[4] A. Yousefi, H. Guo, S. Dev, B. Liko, S. Lafrance, Effects of ammonia en-
ergy fraction and diesel injection timing on combustion and emissions of an
ammonia/diesel dual-fuel engine, Fuel 314 (2022).
[5] B.S. Brown, C.A. Laforet, S.N. Rogak, S.R. Munsh, Comparison of injectors for
compression ignition of natural gas with entrained diesel, Int. J. Engine Res. 12
(2) (2011) 109–122.
Proceedings of the Combustion Institute 40 (2024) 105213 
6

<!-- PDF_PAGE: 7 -->

T. Lucchini et al.
[6] C. Kavuri, S.L. Kokjohn, D.T. Klos, D. Hou, Blending the benefits of reactivity
controlled compression ignition and gasoline compression ignition combustion
using an adaptive fuel injection system, Int. J. Engine Res. 17 (8) (2016)
811–824.
[7] P. Rorimpandey, H. Yip, A. Srna, G. Zhai, A. Wehrfritz, S. Kook, E. Hawkes,
Q. Chan, Hydrogen-diesel dual-fuel direct-injection (H2DDI) combustion under
compression-ignition engine conditions, Int. J. Hydrog. Energy 48 (2) (2023)
766–783.
[8] A. Srna, B. von Rotz, K. Herrmann, K. Boulouchos, G. Bruneaux, Experimental in-
vestigation of pilot-fuel combustion in dual-fuel engines, Part 1: Thermodynamic
analysis of combustion phenomena, Fuel 255 (2019).
[9] Y. Wang, H. Wang, X. Meng, J. Tian, Y. Wang, W. Long, S. Li, Combustion
characteristics of high pressure direct-injected methanol ignited by diesel in a
constant volume combustion chamber, Fuel 254 (2019).
[10] J. Zhu, D. Zhou, W. Yang, Y. Qian, Y. Mao, X. Lu, Investigation on the potential
of using carbon-free ammonia in large two-stroke marine engines by dual-fuel
combustion strategy, Energy 263 (2023).
[11] Y. Wang, A. Evans, A. Srna, A. Wehrfritz, E. Hawkes, X. Liu, S. Kook, Q. Chan,
A Numerical Investigation of Mixture Formation and Combustion Characteristics
of a Hydrogen-Diesel Dual Direct Injection Engine, SAE Technical Papers, 2021.
[12] C. Ramsay, K. Dinesh, Numerical modelling of a heavy-duty diesel-hydrogen
dual-fuel engine with late high pressure hydrogen direct injection and diesel
pilot, Int. J. Hydrog. Energy (2023).
[13] A. Hadadpour, S. Xu, Y. Zhang, X.-S. Bai, M. Jangi, An extended FGM model
with transported PDF for LES of spray combustion, Proc. Combust. Inst. 39 (4)
(2023) 4889–4898.
[14] Y. Duan, Z. Xia, L. Ma, Z. Luo, Numerical simulation of the Sandia Flame D
using the ESF method coupled with FGM model, Cluster Comput. 22 (2019)
15103–15110.
[15] A. Avdic, G. Kuenne, J. Janicka, Flow physics of a bluff-body swirl stabilized
flame and their prediction by means of a joint Eulerian stochastic field and
tabulated chemistry approach, Flow Turbul. Combust. 97 (4) (2016) 1185–1210.
[16] G. D’Errico, T. Lucchini, F. Contino, M. Jangi, X.-S. Bai, Comparison of well-
mixed and multiple representative interactive flamelet approaches for diesel
spray combustion modelling, Combust. Theory Model. 18 (1) (2014) 65–88.
[17] F. Contino, H. Jeanmart, T. Lucchini, G. D’Errico, Coupling of in situ adaptive
tabulation and dynamic adaptive chemistry: An effective method for solving
combustion in engine simulations, Proc. Combust. Inst. 33 (2) (2011) 3057–3064.
[18] H. Lehtiniemi, Y. Zhang, R. Rawat, F. Mauss, Efficient 3-D CFD Combustion
Modeling with Transient Flamelet Models, SAE Technical Papers, 2008.
[19] I. Morev, B. Tekgül, M. Gadalla, A. Shahanaghi, J. Kannan, S. Karimkashi, O.
Kaario, V. Vuorinen, Fast reactive flow simulations using analytical Jacobian and
dynamic load balancing in OpenFOAM, Phys. Fluids 34 (2) (2022).
[20] A. Cuoci, A. Frassoldati, T. Faravelli, E. Ranzi, OpenSMOKE++: An object-
oriented framework for the numerical modeling of reactive systems with detailed
kinetic mechanisms, Comput. Phys. Comm. 192 (2015) 237–264.
[21] A. Stagni, A. Frassoldati, A. Cuoci, T. Faravelli, E. Ranzi, Skeletal mechanism
reduction through species-targeted sensitivity analysis, Combust. Flame 163
(2016) 382–393.
[22] A. Stagni, A. Cuoci, A. Frassoldati, T. Faravelli, E. Ranzi, Lumping and reduction
of detailed kinetic schemes: An effective coupling, Ind. Eng. Chem. 53 (22)
(2014) 9004–9016.
[23] H. Kahila, A. Wehrfritz, O. Kaario, M. Ghaderi Masouleh, N. Maes, B. Somers,
V. Vuorinen, Large-eddy simulation on the influence of injection pressure in
reacting Spray A, Combust. Flame 191 (2018) 142–159.
[24] L. Valino, Field Monte Carlo formulation for calculating the probability density
function of a single scalar in a turbulent flow, Flow Turbul. Combust. 60 (2)
(1998) 157–172.
[25] L. Valino, R. Mustata, K. Ben Letaief, Consistent behavior of Eulerian Monte Carlo
fields at low Reynolds numbers, Flow Turbul. Combust. 96 (2) (2016) 503–512.
[26] V. Sabel’nikov, O. Soulard, Rapidly decorrelating velocity-field model as a tool
for solving one-point Fokker–Planck equations for probability density functions
of turbulent reactive scalars, Phys. Rev. E 72 (1) (2005).
[27] T. Pant, U. Jain, H. Wang, Transported PDF modeling of compressible turbulent
reactive flows by using the Eulerian Monte Carlo fields method, J. Comput. Phys.
425 (2021).
[28] Q. Zhou, T. Lucchini, G. D’Errico, N. Maes, B. Somers, X.-C. Lu, Computational
Modeling of Diesel Spray Combustion with Multiple Injections, SAE Technical
Papers 2020-April, 2020, (April).
[29] B. Naud, R. Novella, J. Pastor, J. Winklinger, RANS modelling of a lifted H2/N2
flame using an unsteady flamelet progress variable approach with presumed PDF,
Combust. Flame 162 (4) (2015) 893–906.
[30] T. Zirwes, F. Zhang, P. Habisreuther, M. Hansinger, H. Bockhorn, M. Pfitzner, D.
Trimis, Identification of flame regimes in partially premixed combustion from a
quasi-DNS dataset, Flow Turbul. Combust. 106 (2) (2021) 373–404.
Proceedings of the Combustion Institute 40 (2024) 105213 
7
