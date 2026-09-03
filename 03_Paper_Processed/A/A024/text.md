<!-- PDF_PAGE: 1 -->

Numerical modelling of a heavy-duty
diesel-hydrogen dual-fuel engine with late high
pressure hydrogen direct injection and diesel pilot
C.J. Ramsay, K.K.J. Ranga Dinesh *
Energy Technology Research Group, School of Engineering, Faculty of Engineering and Physical Sciences, University
of Southampton, SO17 1BJ, Southampton, UK
highlights graphical abstract
/C15 Combustion performance of a
diesel-hydrogen dual direct injec-
tion engine is investigated.
/C15 Four distinct phases of combus-
tion are identiﬁed.
/C15 Very high hydrogen energy share
works well at high load.
/C15 Very high hydrogen energy share
requires improvement at low load.
article info
Article history:
Received 29 June 2023
Received in revised form
18 August 2023
Accepted 2 September 2023
Available online 22 September 2023
Keywords:
Hydrogen direct injection
Diesel pilot injection
Dual direct injection
Dual-fuel engine
abstract
Direct gaseous fuel injection in internal combustion engines is a potential strategy for
improving in-cylinder combustion processes and performance while reducing emissions
and increasing hydrogen energy share (HES). Through use of numerical modelling, the
current study explores combustion in a compression ignition engine utilising a late
compression/early power stroke direct gaseous hydrogen injection ignited by a diesel pilot
at up to 99% HES. The combustion process of hydrogen in this type of engine is mapped out
and compared to that of the same engine using methane direct injection. Four distinct
phases of combustion are found which differ from that of pure diesel operation. Interaction
of the injected gas jet with the chamber walls is found to have a considerable impact on
performance and emission characteristics and is a factor which needs to be explored in
greater detail in future studies. Considerable performance increase and carbon-based
emission reductions are identiﬁed at up to 99% HES at high load but low load
* Corresponding author .
E-mail address: dinesh.kahanda-koralage@soton.ac.uk (K.K.J.R. Dinesh).
Available online at www.sciencedirect.com
ScienceDirect
journal homepage: www.elsevier.com/locate/he
international journal of hydrogen energy 49 (2024) 674 e696
https://doi.org/10.1016/j.ijhydene.2023.09.019
0360-3199/Crown Copyright © 2023 Published by Elsevier Ltd on behalf of Hydrogen Energy Publications LLC. This is an open access article
under the CC BY license ( http://creativecommons.org/licenses/by/4.0/).

<!-- PDF_PAGE: 2 -->

Performance and emissions
Modelling and simulation
performance greatly deteriorated when 95% HES was exceeded due to a much reduced
diesel pilot struggling to ignite the main hydrogen injection.
Crown Copyright © 2023 Published by Elsevier Ltd on behalf of Hydrogen Energy Publica-
tions LLC. This is an open access article under the CC BY license ( http://creativecommons.
org/licenses/by/4.0/).
1. Introduction
Renewable energy has been thrust into the spotlight in recent
years due to rising global awareness of the environmental
impacts of fossil fuel combustion in conjunction with growing
energy demands [ 1]. Hydrogen ( H
2) has a promising future as
both a clean energy carrier and fuel source but ﬁrst a number
of factors such as production, transport, storage and uti-
lisation must be addressed before it can be adopted.
This study focuses on utilisation in vehicles, in which there
are two main potential avenues, namely hydrogen fuel cells
and hydrogen powered internal combustion engines (ICEs).
Signiﬁcant research and development has been carried out on
hydrogen fuel cells where electrochemical reactions of
hydrogen and an oxidiser are used to produce electricity which
is then used to power the vehicle [2]. While fuel cell vehicles are
likely the future in terms of near-zero emissions, production
costs are prohibitive while also requiring very high purity
hydrogen to prevent system degradation [3] and thus a bridging
technology which can help improve infrastructure and drive
down costs is required [ 4]. ICEs have the potential to achieve
this goal as conversion of a conventional spark ignition (SI) or
compression ignition (CI) engine to being fuelled by a gas such
as hydrogen is relatively straightforwards and thus costs a
fraction of a fuel cell vehicles current price of production while
also not requiring as high a purity fuel [ 5]. Therefore, if
hydrogen fuelled ICEs were to become an attractive option in
terms of performance, emissions and price comparative to
conventional ICEs, then any infrastructure developed would
also facilitate an eventual transition to fuel cell vehicles.
Currently, CI engines fuelled by diesel play a vital role in
many heavy-duty transport, power generation, agricultural
and industrial applications due to the various beneﬁts of CI
engine combustion and its operating cycle. These beneﬁts
include superior torque, greater power output, higher thermal
efﬁciency, better fuel economy and reliability when compared
with SI engines [ 6]. Unfortunately however, diesel engines
generally emit higher levels of harmful pollutant emissions
such as nitric oxides ( NO
x), unburned hydrocarbons (UHC),
carbon monoxide ( CO) and soot. Utilisation of hydrogen in
heavy-duty CI engines can lead to a reduction in carbon-based
emissions while maintaining or even improving performance
[7,8]. However, efﬁcient utilisation is not a trivial task and thus
improvements and optimisation of the various strategies used
for hydrogen combustion in CI engines is required.
Generally utilisation of hydrogen in CI engines will require
operation in a dual-fuel mode where a more reactive fuel such
as diesel is used as a pilot fuel to ignite the high autoigniton
temperature hydrogen fuel. The inherent complexity of dual-
fuel engine design and operation in terms of both engine
fuelling and combustion modes means that both experi-
mental and numerical investigation is required to gain in-
sights on the various physical phenomena which occur such
as the ﬂow induced by fuel injection, ignition, ﬂame propa-
gation, heat release and formation of pollutant emissions.
Gaining insight into the processes occurring during dual
direct injection diesel-hydrogen CI engine operation is
essential for the advancement of heavy-duty hydrogen in-
ternal combustion engine technology. High pressure direct
injection (HPDI) of the gaseous fuel close to top dead centre
(TDC) aiming for non-premixed combustion should allow for
greater power output and higher hydrogen substitution rates
across all load conditions when compared to either early
compression stroke direct injection or intake induction oper-
ation [ 8,9]. Fig. 1 illustrates the general combustion process
present in a late hydrogen HPDI engine utilising a diesel pilot
as an ignition source for the injected hydrogen jet. Unlike
premixed operation, late HPDI of hydrogen completely avoids
any potential pre-ignition or backﬁre so the likes of load and
compression ratio do not need to be lowered allowing for
maximum power output, which is especially important for
heavy-duty applications. Another beneﬁt is the potential for
higher hydrogen substitution rates across all load conditions
as the diesel pilot volume can be reduced because it 's much
easier to ignite the incoming hydrogen jet than the lean ho-
mogeneous mixtures used in premixed operation. Currently
investigations into late compression/early power stroke
hydrogen HPDI with diesel pilot ignition are scarce and further
experimental and modelling studies are required to assess the
impacts of the strategy on engine combustion, performance
and emissions outputs.
The majority of the hydrogen HPDI investigations in the
literature have been in SI [ 10e14], glow plug [ 15e18] or HCCI
[8,19e22] type engines so there lies many unknowns with
regards to utilisation in dual-fuel CI engines aiming for a non-
premixed mode of combustion [ 8]. Hydrogen HPDI aiming for
non-premixed combustion modes have only recently begun to
gain traction. Rottengruber et al. [ 23] aimed for non-premixed
combustion similar to diesel operation and investigated pure
hydrogen direct injection in a compression ignition engine,
however, inlet pre-heating to 343 K was required to allow for
reasonable autoignition delay timings which led to a reduc-
tion in performance. Similarly, Gomes Antunes et al. [ 24] also
investigated a pure hydrogen direct injection CI engine and
required pre-heating to 353 K for reasonable ignition delay.
While this mode of operation may be reasonable the required
high in-cylinder temperatures and reduction to intake air
density are likely to both increase NO
x emissions and reduce
performance.
international journal of hydrogen energy 49 (2024) 674 e696 675

<!-- PDF_PAGE: 3 -->

With regard to dual-fuel engines, only a handful of studies
were found in the literature directly addressing pilot ignited
non-premixed hydrogen direct injection operation which are
recent CFD studies carried out by Babayev et al. [25e27], Frankl
et al. [ 28], Munshi et al. [ 9] and Liu et al. [ 29] as well as exper-
imental studies by Liu et al. [ 30] and Rorimpandey et al. [ 31].
Babayev et al. [ 25, 26] have published a number of studies and
validated a CFD model, comparing the combustion character-
istics of a pure diesel CI engine to that of a pure hydrogen direct
injection CI engine utilising a hydrogen pilot and hydrogen
main injection. Distinct combustion phases were found which
differ somewhat from the standard diesel combustion process.
An optimisation study was also performed [ 27] which noted
optimisation of the likes of piston bowl design and injection
parameters such that more combustion occurs before the gas
jet contacts the chamber walls can lead to improved combus-
tion quality. Frankl et al. [ 28] also validated a CFD model and
compared the combustion process of diesel pilot ignited direct
hydrogen injection with direct ammonia injection. Again a
similar combustion process with minimal premixing and a
non-premixed ﬂame surrounding the rich hydrogen core is
noted, however, less jet-jet interaction is observed due to what
appears to be a much shorter injection event and ﬂat/square
piston bowl which doesn 't allow for the same type of move-
ment of the jet along the walls as was observed in the engine
studied by Babayev et al. [ 25]. Frankl et al. also found that the
gaseous jet caused increased convection of the pilot combus-
tion products into the piston bowl area. Munshi et al. [ 9]p e r -
formed a numerical analysis which compared pure diesel
operation to hydrogen intake induction, early cycle direct
hydrogen injection and late compression/early power stroke
hydrogen HPDI all operating with a diesel pilot. It was found
that HPDI engine torque and efﬁciency was equal to or excee-
ded diesel operation and far exceeded possible torque and ef-
ﬁciency of the two premixed hydrogen cases while not
suffering from knocking or unstable combustion. Liu et al. [ 29]
carried out a CFD study which compared diesel pilot ignited
late hydrogen HPDI to three types of premixed hydrogen
combustion, namely port-fuelled SI, port-fuelled diesel pilot
ignited and port-fuelled pre-chamber ignited. It was found that
Fig. 1 e Example schematic of the combustion process in a late high pressure dual direct injection hydrogen-diesel dual-fuel
engine.
international journal of hydrogen energy 49 (2024) 674 e696676

<!-- PDF_PAGE: 4 -->

the HPDI case could run at much higher compression ratios
than the other types of operation which allowed for high
thermal efﬁciency and power output. However, owing to the
high temperatures of the diffusion ﬂame at the jets periphery
high NO
x levels and wall heat losses were also found, especially
in comparison to the pre-chamber and SI engines as they could
run at ultra-lean conditions where chamber temperatures
remain low throughout. Liu et al. [ 30] carried out an experi-
mental study on a compression ignition engine utilising HPDI
of hydrogen with a diesel pilot at varying hydrogen energy
shares (0e90%) and compared start of injection timings (180-
0
/C14 CA before TDC). Primarily mixing controlled combustion was
observed for SOI timings later than 20 /C14 CA before TDC, with
lower peak in-cylinder pressures when compared to the earlier
SOI cases which exhibited much higher levels of premixed
combustion. The late HPDI cases generally led to lower NO
x
emissions but also lower power outputs which was mostly due
to the later combustion phasing in comparison to the premixed
cases. Rorimpandey et al. [ 31] investigated the combustion
process of pilot ignited hydrogen HPDI in an optical constant
volume combustion chamber. They found that hydrogen
ignition is delayed when the dwell time between pilot and
main hydrogen injection is increased as the pilot combustion
products begin to cool before the hydrogen is injected. Similar
hydrogen ignition delay increases were also observed when
ambient temperatures were lowered. In addition, they found
that cycle-cycle variability increased greatly if the pilot fuel
ignition occurred towards the end of or after the hydrogen
injection, leading to inconsistent heat release rates and ﬂame
evolution.
To this authors knowledge no other CFD or experimental
studies on this form of hydrogen CI engine combustion are
present in the literature, and thus further investigations are
required. For the most part pilot ignited non-premixed HPDI
studies have utilised methane/natural gas rather than
hydrogen with the likes of injection pressure [ 32,33], relative
angle between injections [ 34], nozzle diameter [ 35,35,36],
relative injection timings/strategies [ 35e39], etc. all being
investigated. However, due to hydrogen 's disparate fuel
properties conclusions cannot be drawn from the studies on
methane/natural-gas. Table 1 compares said properties to
methane and various other fuels.
This study aims to map out the general combustion pro-
cess of diesel pilot ignited late compression/early power
stroke direct hydrogen injection CI engine operation while
also identifying the beneﬁts of late hydrogen HPDI and areas
in which the combustion process can be optimised. Further-
more, comparisons are made between hydrogen and methane
as the two gaseous fuels are both suitable candidates for
emissions reductions in CI engines.
2. Numerical methodology and modelling
setup
Three-dimensional unsteady Reynolds averaged Navier-
Stokes (URANS) CFD simulations were performed using
ANSYS Fluent 19.1 on the University of Southampton high
performance computing cluster IRIDIS 4.
2.1. Governing equations
Simulations were carried out by solving compressible URANS
equations for mass, momentum, energy and N /C0 1 species
transport equations, where N is the total number of species for
a chemically reacting mixture using ﬁnite volume method.
Mass:
vr
vt þ vruj
vxj
¼ Sm; (1)
Momentum:
vrui
vt þ vrui uj
vxj
¼/C0 vP
vxi
þ v
vxj
/C18
m
/C18vuj
vxi
þ vui
vxj
/C0 2
3dij
vuk
vxk
/C19/C19
/C0
vru0
i u0
j
vxj
þ Si :
(2)
Energy:
vrH
vt þ vrujH
vxj
¼ v
vxj
/C18keff
Cp
vH
vxj
/C19
þ Sh; (3)
Species:
vrYn
vt þ vruiYn
vxj
¼/C0 vJn
vxj
þ Rn þ Sn (4)
Table 1 e Properties of hydrogen, methane, gasoline, diesel, n-heptane and ammonia [ 6, 40e47] (diesel and gasoline are
generally blended fuels so properties will vary from those listed).
Properties Hydrogen Methane Gasoline Diesel n-Heptane Ammonia
Chemical formula H2 CH4 CnH2nC nH2n nC7H16 NH3
Molecular weight (g/mol) 2.016 16.043 107 170 100.16 17.031
Density(kg/m3) 0.08 0.65 750 840 692 0.73
Mass diffusivity in air (cm 2/s) 0.61 0.16 ee e 0.23
Flammability limits in air (vol%) 4 e75 5 e15 1 e7.6 0.7 e7.5 1.05 e6.7 15 e28
Burning velocity (m/s) 2.65 e3.25 0.37 e0.43 0.45 0.3 0.2 e0.6 0.07
Quenching distance (mm) 0.61 2.00 2.00 ee 8.95
Autoignition temperature (K) 858 813 523 483 479 930
Minimum ignition energy (mJ) 0.02 0.28 0.24 0.24 0.24 8
Adiabatic ﬂame temperature (K) 2390 2226 2275 2275 2275 2080
Stoichiometric air/fuel ratio by mass 34.3 17.2 14.5 14.5 15.1 6.1
Lower heating value (MJ/kg) 120 50 43.4 42.6 44.6 18.6
international journal of hydrogen energy 49 (2024) 674 e696 677

<!-- PDF_PAGE: 5 -->

Three further transport equations for pollutant emissions
are solved post-time step for computational efﬁciency. NOx
emissions are calculated using the following transport equa-
tion for the NOx mass fraction, YNOx , accounting for thermal
[48] and prompt [ 49] mechanisms
vrYNOx
vt þ vrujYNOx
vxj
¼ v
vxj
/C18
rD vYNOx
vxj
/C19
þ SNOx (5)
Soot emissions are calculated using the Moss-Brookes soot
model [ 50] using acetlyene as the inception species. Two
additional transport equation are solved for the soot mass
fraction, Ysoot, given by
vrYsoot
vt þ vrujYsoot
vxj
¼ v
vxj
/C18mt
ssoot
vYsoot
vxj
/C19
þ dM
dt (6)
and the normalised radical nuclei concentration b*nuc
vrb* nuc
vt þ vrujb* nuc
vxj
¼ v
vxj
/C18mt
snuc
vb* nuc
vxj
/C19
þ 1
N*
norm
dN*
dt ; (7)
where r is the density of the ﬂuid, t is time, uj a component of
the mean velocity vector, u0
j a component of the ﬂuctuating
velocity vector, xj a component of the position vector, Sm the
source term accounting for mass added by fuel spray, P is
pressure, m is molecular viscosity, Si a component of the body
forces, dij the Kronecker delta, H the mean total enthalpy, keff
the effective conductivity, Cp the speciﬁc heat capacity of the
ﬂuid, Sh the source term accounting for any further heat los-
ses, Yn is the mass fraction of species n, Jn is the diffusion ﬂux
of the given species, Rn the net rate of production of the given
species by chemical reaction, Sn the rate of creation of the
species by the discrete phase injection and any other sources,
D is the effective diffusion coefﬁcient, S
NO is the source term
for any other NOx production due to thermal or prompt
mechanisms, mt is the turbulent viscosity, ssoot is the turbulent
Prandtl number for soot transport, M is the soot mass con-
centration, snuc is the turbulent Prandtl number for radical
nuclei transport, N* is the soot particle number density and
N*
norm is 1015 particles.
2.2. Numerical models and methods
Gaseous injections are dealt with using a modiﬁed gaseous
sphere injection (GSI) model [ 51,52] which is implemented
through use of user-deﬁned functions (UDFs) which modify
Fluent's Lagrangian discrete phase model (DPM). The GSI
model is a computationally efﬁcient method for simulating
gaseous direct injection and further details of the model
development and implementation can be found in [ 51]. Diesel
injection is also handled by the DPM employing KHRT primary
and secondary breakup [ 53], stochastic collision [ 54],
dynamic-drag [ 55] and an impingement/splashing wall-ﬁlm
model [ 56,57]. In both types of injection, the DPM analyti-
cally tracks the injected droplets, grouped into parcels, with
the ﬂuid ﬂow time step and models their coupled interactions
with the continuous phase. The discrete random walk (DRW)
stochastic tracking model [ 58] is used to predict turbulent
dispersion of the particles. Realizable k-e model [ 59] with
standard wall functions is employed to model turbulent ﬂow
characteristics due to the models improvements over the
standard k-e model with regards to the round-jet anomaly [59].
Two additional transport equations for turbulent kinetic en-
ergy, k, and turbulent dissipation rate, e, are solved. Com-
bustion is modelled through use of the ﬁnite rate combustion
model, with an adequately ﬁne mesh such that the majority of
the RANS scales are resolved, which couples the ﬂow and
chemical kinetics. The Chemkin-CFD solver along with Flu-
ent's in situ adaptive tabulation (ISAT) algorithm [ 60]i s
employed to integrate reaction rates. The reduced Chalmers
n-heptane mechanism [ 61] is supplemented with the GRI
mech 3.0 [ 62] and a detailed hydrogen mechanism [ 63]t o
represent diesel, natural gas and hydrogen fuel chemistry
leading to a chemical mechanism containing 48 species and
273 reactions. The nitrogen mechanism was removed from
the GRI mech to reduce computational time and instead
pollutant emissions are modelled post-process at the end of
each time step. The Moss-Brookes soot model [ 50] is used to
predict soot emissions and thermal and prompt NO
x devel-
opment are accounted for to predict NOx emissions. Dynamic
mesh layering and smoothing is used to simulate the piston
movement and keygrids are utilised which allow for a coarse
mesh to be used during initial compression and a ﬁne mesh
during injection and combustion. Table 2 summarises the
numerical models used.
A 3-D double precision analysis is carried out using Fluent's
pressure based solver. The PISO pressure-velocity coupling
algorithm is used to reformat the continuity equation and
obtain a pressure ﬁeld. Second order upwind schemes are
used for the spatial discretisation. Least squares cell-based
method is used to compute gradients. First-order implicit
time-stepping is employed due to the variable time step pro-
ﬁles used in the simulations during fuel injection and com-
bustion. Convergence criteria are set to converge at residuals
of 10
/C0 3 apart from energy and post-processed scalars which
are set to 10 /C0 6. In all cases injected mass is also monitored to
ensure the correct intended mass is delivered. Max iterations
per time step are set to 50 with up to 10 post-time step itera-
tions for the pollutant calculations. Table 3 outlines a sum-
mary of numerical discretisation methods employed during
calculations.
2.3. Model validation
The engine model is based on an experimental study carried
out by Faghani [ 39] for a dual direct injection diesel-natural
gas engine and the parameters are summarised in Table 4 .
As there are 7 evenly spaced diesel and gas injectors in the
engine a sector geometry representing 1/7th of the combus-
tion chamber is created in ANSYS SpaceClaim and meshed
using ANSYS meshing, Fig. 2. The sector contains one gas and
one diesel injector both with an included spray angle of 140
/C14
and an interlace angle of 0 /C14 . Gaseous injection pressure is set
at 25 MPa and diesel injection pressure at 27 MPa. Periodic
boundary conditions are set at the side faces of the sector and
constant temperature boundary conditions of 600 K and 650 K
are set at the sector top face and piston bowl walls
international journal of hydrogen energy 49 (2024) 674 e696678

<!-- PDF_PAGE: 6 -->

respectively and 500 K at the remainder of the chamber walls.
Exhaust gas recirculation (EGR) level is adjusted by varying the
initial charge composition, temperature and pressure using
values measured in the experimental reference. Simulations
are run from inlet valve close (IVC) to exhaust valve open
(EVO) and layering is used to compute piston motion during
the compression and expansion strokes. Results are then
compared to the experimental measurements. Throughout
this analysis the convention that 720
/C14 CA is TDC of the
compression stroke is followed.
A mesh sensitivity study is carried out using 4 different grid
resolutions; coarse, medium, ﬁne and very ﬁne with
maximum cell sizes of 1 mm, 0.4 mm, 0.35 mm and 0.3 mm
respectively, see Table 5. To allow for reasonable computation
times keygrids are used in all but the coarse mesh simulation.
In the medium, ﬁne and very ﬁne cases the coarse grid is used
from IVC to 700
/C14 CA (3 /C14 before pilot injection starts) before
being replaced by a ﬁner mesh, Fig. 2 . This ﬁne mesh is then
used throughout both injections and the power stroke until
EVO with a variable layering height which begins to coarsen
after injections have ﬁnished. A variable time step size is used
with 0.25
/C14 CA steps from IVC to 702 /C14 CA followed by 0.025 /C14 CA
steps until 755 /C14 CA then 0.25 /C14 CA again until EVO.
As can be seen in Fig. 3 all grids apart from the most coarse
predict in-cylinder pressure and heat release fairly well for the
18% EGR test case. The coarse grid predicts a slightly later
ignition of the methane injection compared to the other grids
and generally underpredicts the rate of combustion until
around the time that the gaseous injection ﬁnishes, leading to
a lower pressure than desired. Only small variation between
the medium and ﬁne grid is observed. The variation is largely
Table 2 e Summary of the numerical models employed during the simulations.
Description Model
Viscous Realizable k-e
Energy/Species Species transport ﬁnite-rate combustion
Chemkin CFD solver with ISAT
Fuel oxidation mechanism representing n-heptane [61], methane [62] and hydrogen [63]
NO
x Thermal and prompt
Soot Moss-Brookes
Dynamic mesh Smoothing and layering
Discrete Phase GSI Liquid
Droplet particle Droplet particle
No breakup KHRT primary & secondary breakup
No collision Stochastic collision
Constant high Re spherical drag Dynamic drag
DRW turbulent dispersion DRW turbulent dispersion
Wall-reﬂection Wall-ﬁlm
Laws: density-drag adjustment, core length transition Laws: inert heating, vapourisation, boiling
Table 3 e Summary of numerical methods employed during simulations.
Description Parameter Method/model/value
Software ANSYS Fluent 19.1 Finite volume method
Solver General Pressure-based
Pressure-velocity coupling Flux type Rhie-Chow
Scheme PISO
Spatial discretisation Gradient Least squares cell based
Density Second order upwind
Momentum Second order upwind
Energy Second order upwind
k Second order upwind
e Second order upwind
Species (N-1 equations) Second order upwind
Pollutant NO
x Second order upwind
Pollutant soot mass Second order upwind
Pollutant soot nuclei Second order upwind
Temporal discretisation Time First order implicit
Table 4 e Summary of engine parameters based on
experimental study by Faghani [ 39].
Engine Parameters Value
Bore x stroke (mm) 137 x 169
Connecting rod (mm) 262
Swirl ratio 1.5
Compression ratio 17
Engine speed (RPM) 1500
IVC-EVO (CA) 630
/C14 e860/C14
Number of pilot injectors 7
Number of gas injectors 7
Pilot start of injection (CA) 703
/C14
Gas start of injection (CA) 712 /C14
international journal of hydrogen energy 49 (2024) 674 e696 679

<!-- PDF_PAGE: 7 -->

during the diesel injection where the medium grid has a
similar peak HRR but lower level of mixing controlled diesel
combustion than the ﬁne grid which leads to lower pressures.
The difference between the ﬁne and very ﬁne grids is even
smaller with the only signiﬁcant change being a slightly
earlier diesel ignition which leads to a lower peak diesel HRR
in the very ﬁne grid. This could be due to grid effects but may
simply be due to the cycle to cycle variation which the discrete
Fig. 2 e Sector mesh at 700 /C14 CA used in combustion simulations. Left shows the “coarse” grid used to compute the
compression stroke prior to injection and right shows the “ﬁne” keygrid, with a maximum mesh size of 0.35 mm, used
during injection and combustion.
Table 5 e Mesh densities for the mesh independence study.
Mesh Cell count at TDC Max cell size (mm) Run time
Coarse 50k 1 z7h
Medium 300k 0.4 z29h
Fine 400k 0.35 z51h
Very Fine 550k 0.3 z69h
Fig. 3 e Pressure and heat release rate predictions and mesh sensitivity study for the 18% EGR test case with comparison to
experimental data.
international journal of hydrogen energy 49 (2024) 674 e696680

<!-- PDF_PAGE: 8 -->

phase model can cause. Results indicate that the RANS scales
are adequately resolved when using a maximum cell size of
0.35 mm, in line with the expected 0.1e1 mm minimum length
scale discussed in the literature [ 64e67], so for the remainder
of this study the 0.35 mm ﬁne mesh is used and deemed
insensitive to further mesh reﬁnement.
Assessing the CFD modelling framework's ability to predict
pollutant emissions under differing conditions is important
for gaining insight into various engine operating strategies. As
pollutant soot and NO
x predictions are decoupled from the
main ﬂow solution the absolute values predicted are not of
much importance, but the trends predicted should still follow
those of the experimental data. As can be seen in Fig. 4 , the
overall trends of both NO
x and soot emission as EGR rate is
increased are predicted fairly well with NOx showing a
decrease between 0% and 25% EGR rates and soot showing an
increase. The percentage decrease in NOx is also well pre-
dicted with simulations showing a decrease of 82% between
0% and 25% EGR rates and experiments showing a decrease of
80%. The ﬁndings are in line with the expected effect of EGR on
NO
x development, whereby reduction in oxidiser leads to
lower combustion temperatures which is further aided by the
dissociation of H
2O and CO2 during combustion and the higher
heat capacity of the exhaust gases acting as heat sinks. The
percentage increase in soot is underpredicted in comparison
to experiments which likely indicates a need to tune model
parameters, include a soot mechanism in the chemical ki-
netics, improve initial charge composition as EGR rate is
increased or various other factors. However, the general
increasing trend of soot emissions being captured is deemed
Fig. 4 e Pollutant trend predictions of a) NOx and b) soot at EVO for increasing levels of EGR compared with experimental
measurement.
international journal of hydrogen energy 49 (2024) 674 e696 681

<!-- PDF_PAGE: 9 -->

sufﬁcient for the current work. Increased soot emissions with
increased EGR use is expected due to the decrease of oxygen
availability leading to an increase in fuel rich areas and thus
soot formation as well as the reduced in-cylinder tempera-
tures being better suited for soot development.
Ideally validation would have been carried out using a dual
direct injection diesel-hydrogen engine, however, the litera-
ture is distinctly lacking in this regard as the only suitable
experimental hydrogen study found [ 30] uses a non-matching
diesel-hydrogen injector hole arrangement which largely
targets premixed hydrogen combustion and would increase
computational costs greatly as the domain couldn 't be peri-
odically reduced. The diesel-natural gas engine model vali-
dation should be adequate as the chemical mechanism
contains a detailed hydrogen oxidation mechanism [ 63] and
both the medium and ﬁne mesh showed good agreement with
experimental results indicating that the ﬁne mesh should be
able to adequately resolve the higher velocity and tempera-
ture gradients present during hydrogen injection and com-
bustion. Using this setup also means that an in-depth
comparison of methane and hydrogen HPDI can be made and
key differences identiﬁed. For further details about the full
modelling setup and validation please see the previous work
carried out by the author [ 51].
Some minor modiﬁcation are made to the model in the
upcoming analysis compared to the previous validation. In-
jection pressure is increased to 40 MPa to ensure the nozzle is
choked during all operating points. Conversely, nozzle diam-
eter is reduced to 0.577 mm to keep mass ﬂow rates equivalent
to the validation case (for methane; hydrogen will always be
less due to density differences) as this should keep combus-
tion phasing somewhat similar. This ensures a fairer com-
parison between cases as steady mass ﬂow rate will not
change during a given case due to unchoking of the nozzle and
also represents an injection pressure and nozzle diameter
which should be targeted in practical applications. All HL
cases use a total energy of 1304 J (diesel þ gaseous fuel) and all
LL cases 434 J. While the HL case uses the same initial absolute
pressure (3.82 bar) and temperature (431 K) as the validation
simulations unless stated otherwise, the LL case uses slightly
lower initial absolute pressure (3 bar) and temperature (390 K)
to model what would be expected in a practical engine setup
where turbocharging level is used as a way to control load in
conjunction with smaller fuel injections. At this point it 's
likely good to point out that the IVC provided by the experi-
mental validation study is further into the compression stroke
than is standard (90
/C14 CA after bottom dead centre). So while it
may seem as if the initial turbocharging levels are quite high
they equate to effective compression ratios of 38.7 at HL and
30.4 at LL which are fairly standard for diesel engine opera-
tion. From here on it 's simply assumed that the engine oper-
ates on a late intake valve close cycle similar to some Miller
cycle implementations.
3. Results and discussion
Combustion, performance and emissions characteristics of
the two gaseous fuels are examined across 3 gaseous energy
shares (95%, 97% and 99%) and at high and low load conditions
in a dual-fuel compression ignition engine with late HPDI of
the gaseous fuels and diesel pilot. It 's worth mentioning that
real-world diesel injectors may struggle to properly inject the
small volumes of fuel required at the likes of LL 99% energy
share [ 68], but this problem is outside of the scope of the
current study.
The ﬁrst two tests simulate equivalent injection conditions
(same injection pressure and diameter) for hydrogen and
methane which leads to a slightly lower energy ﬂow rate and
longer duration for the hydrogen injection (case 0 and case 1),
while the second set changes various injection parameters
such that energy ﬂow rate and duration of the hydrogen in-
jections are equivalent to the baseline methane case (case 2, 3
and 4). Table 6 outlines the injection conditions for the test
cases, where P
0 is the upstream injection pressure, De is the
exit nozzle diameter and _m is the choked mass ﬂow rate.
3.1. Combustion trends at high and low load
We ﬁrst compare the combustion of methane and hydrogen at
95% gaseous energy share as consistent and stable combus-
tion is present at both load conditions. From observation of
the 95% energy share heat release rate graphs, top row of
Fig. 5 , it is clear that the diesel pilot adequately ignites the
gaseous injections for both fuels almost instantly upon their
injection into the combustion chamber. Due to hydrogen 's
lower minimum ignition energy this ignition occurs about
0.3
/C14 CA earlier for the hydrogen injections compared to
methane. Peak HRR and in-cylinder pressure is higher for the
hydrogen cases, but the fall-off from peak HRR occurs earlier
and HRR levels remain much lower for the remaining power
stroke compared to methane due to hydrogen 's much shorter
oxidation pathway.
Next we address the change in combustion characteristics
as gaseous energy share is increased. From observing the HRR
and pressure curves presented in Fig. 5 it can be seen that
increasing gaseous energy share makes very little difference to
combustion characteristics at HL for either fuel or at the
varying injection conditions. This is because the reduced vol-
ume diesel pilot continues to produce enough heat to ignite the
gaseous injection. This is evidenced by the very similar ignition
delays of the gaseous jet observed across all HL cases. A
completely different story is told at LL due to the smaller pilot
injection compared to HL. At 95% gaseous energy share the
diesel pilot adequately ignites the jet with very similar jet
ignition delays to the HL cases. However, further decrease of
the pilot volume leads to much longer gaseous jet ignition
delays at 97% energy share leading to high levels of premixed
combustion and high pressure rise rates/HRR peaks. Hydrogen
won't produce soot/ CO/UHCs like diesel during this type of
combustion mode, however, hydrogen 's wide ﬂammability
limits and very high burning velocity mean that too much fuel
is likely to combust over a very short period of time. This type
of combustion is undesirable as the rapid and rich premixed
combustion which occurs generally leads to high engine noise
and possibly damage, while also causing difﬁculties with
controlling engine operation as the ignition timing becomes
unpredictable. NO
x emission during this type of combustion
mode may be lower than the high temperature combustion
which occurs in a non-premixed ﬂame, however, this will only
international journal of hydrogen energy 49 (2024) 674 e696682

<!-- PDF_PAGE: 10 -->

be the case if the amount of premixing is somewhat controlled
to not allow for the majority of the fuel volume to burn in a
much shorter period. The inconsistent and difﬁcult to control
engine operation is highlighted by the wide variance in ignition
delays observed between cases at LL 97% energy share with the
likes of C3, which is still a similar setup to the other cases,
essentially showing no combustion of the hydrogen jet. Similar
to this case, all 99% LL cases show almost no hydrogen com-
bustion due to the much reduced diesel injection providing too
little energy for ignition of the injected gaseous jet.
Clearly considerable improvements need to be made at
very high gaseous substitution levels when load is reduced but
the results at HL are promising and show the potential of this
type of engine operation.
3.2. Combustion process in a late gaseous HPDI
compression ignition engine with diesel pilot
Fig. 6 provides a breakdown of the general combustion process
in the engine when the diesel pilot adequately ignites the
hydrogen injection and the following discussion provides a
detailed explanation of the processes occurring.
The time series temperature contours shown in Fig. 7
highlight the differences in the combustion process at HL
95% energy share between the two fuels (C0 and C1
compared). Clearly the diesel injection provides an adequately
high temperature region in the vicinity of the injected gases
trajectory close to the injectors (715
/C14 CA contours). Upon con-
tact with this region the gas jet quickly ignites with little to no
premixed combustion present, the rich lower temperature
core stays intact throughout, 716
/C14 CA - 717 /C14 CA contours, with
no early HRR spike and a non-premixed diffusion ﬂame forms.
The lack of premixed combustion is mostly due to the lack of
air entrainment because of the underexpanded ﬂow struc-
tures close to the injector and rapid ignition once entrainment
begins.
The formation of a ﬂame indicates the end of the ignition
delay phase and beginning of the free-jet combustion phase
(716e721
/C14 CA contours). The higher injection velocity of the
hydrogen (higher speed of sound) leads to a much faster
penetration rate than the methane which likely contributes to
the faster ignition and is certainly a factor in the higher
pressure rise rate, and climb to peak HRR, due to the rate of
mixing with oxidiser being much higher as the ﬂame pene-
trates the chamber. The non-premixed ﬂame is also thicker in
the hydrogen case as evidenced by the reduced low temper-
ature core width and wider high temperature region
surrounding it on either side and in-front (721
/C14 CA contours).
This is partly due to hydrogen 's higher mass diffusivity and
thus further reach with regard to mixing but is mostly due to
its much wider ﬂammability limit allowing for far richer
combustion towards the core and leaner combustion towards
the outer edge of the jet. This is also the reason for the higher
peak HRR value in the hydrogen cases which occurs just
before the jets contact with the chamber wall. The peak HRR
correlates with the point at which the non-premixed ﬂame is
largest, i.e. before the leading edge is quenched by the
chamber wall (721
/C14 CA vs. 724 /C14 CA contours), and as noted
hydrogen's ﬂame is much wider than its methane counter-
parts. This peak in HRR also occurs earlier for the hydrogen
cases due to the increased penetration rate and thus earlier
contact with the chamber wall.
Upon contacting the wall the front of the ﬂame quenches
and HRR begins to fall due to a smaller ﬂame volume and an
accumulation of fuel which is too rich to combust at the rate it
was previously, indicating the end of the free-jet combustion
phase and beginning of the wall-jet combustion phase
(724
/C14 CA-735/C14 CA contours). This process is very pronounced
for the methane case where a clear low temperature region
forms around the piston bowl walls. However, due to hydro-
gen's far lower quenching distance and wider ﬂammability
limit combustion is still occurring along the wall, although at a
reduced rate compared to the free-jet combustion. The
impinging jets momentum forces fuel along the walls in all
directions; into the piston bowl and back towards the in-
jectors, laterally towards other sectors of the chamber and
towards the top cylinder and liner walls. This spreading of the
fuel allows for adequate mixing of fuel and oxidiser which
leads to a levelling off in HRR at a moderate level, and is best
shown in the HL HRR graphs as the injection ends too early to
see this at LL. As combustion is focussed within the piston
bowl a high temperature area develops which is especially
apparent for hydrogen due to its ability to burn at much higher
fuel-air equivalence ratios, and can be clearly seen in the
735
/C14 CA contours. This increase in fuel utilisation leads to
higher HRR levels during the wall-jet combustion for the
hydrogen cases compared to methane. During this phase, and
later after the end of injection, spreading out of the fuel and
ﬂame front is apparent and interaction with fuel from other
injectors is likely and may enhance the combustion rate in
some cases. This can be seen somewhat in the climbing HRR
towards the end of the phase. This process is more likely for
hydrogen which spreads faster because of the increased jet
velocity and thus increases the chance of meeting fuel from
Table 6 e Injection conditions for methane-hydrogen comparisons.
Case Fuel P 0 (MPa) D e (mm) _m (kg/s) Energy ﬂow rate (MJ/s) Energy per gaseous injection (J)
95% 97% 99%
HL r LL HL r LL HL r LL
0 CH4 40 0.577 0.013900 0.695 1236 r 412 1265 r 422 1291 r 430
1 H2 40 0.577 0.005042 0.605 1236 r 412 1265 r 422 1291 r 430
2 H2 46 0.577 0.005792 0.695 1236 r 412 1265 r 422 1291 r 430
3 H2 40 0.619 0.005792 0.695 1236 r 412 1265 r 422 1291 r 430
4 H2 80 0.437 0.005792 0.695 1236 r 412 1265 r 422 1291 r 430
international journal of hydrogen energy 49 (2024) 674 e696 683

<!-- PDF_PAGE: 11 -->

other sectors injectors before the end of the injection event
while the jets still have a high momentum.
As the injection ends HRR falls off rapidly signalling the
end of the wall-jet combustion phase and start of the late
combustion phase (740 /C14 CA-760/C14 CA contours continuing until
EVO). Even though the hydrogen injection ends later, the fall
off in HRR occurs earlier and is much more rapid than the
methane case. This is due to the oxidation of the remaining
UHCs producing heat when methane is used, whereas
comparatively almost all of the hydrogen has been oxidised
due its much shorter and simpler chemical breakdown
pathway. In general, the rich core stays intact for a short while
after the end of injection for both fuels but over time it begins
to decay until eventually being engulfed by the remaining
ﬂame (740
/C14 CA contours). There is often a secondary peak right
before the fall off in HRR which is due to the rapid combustion
that occurs when the jet core collapses which is enhanced by
the wall-jet/combined injector jets convection into this
Fig. 5 e Calculated pressure and HRR trends for methane-hydrogen comparisons at 95%, 97% and 99% gaseous energy
shares.
international journal of hydrogen energy 49 (2024) 674 e696684

<!-- PDF_PAGE: 12 -->

region. Small amounts of combustion continue for the
remainder of the power stroke, as evidenced by the fairly high
temperature regions. It 's clear however that both from the
quickly reducing temperatures in the hydrogen cases (760
/C14 CA
contours), and much lower HRR that greater amounts of
combustion are occurring in the methane cases at this stage
due to the aforementioned oxidation of UHCs. There is how-
ever still a low temperature region formed in the piston bowl
region for the methane case, where there is a rich pooling of
UHCs where combustion cannot reach, which is not present
for the hydrogen case (760
/C14 CA contours). Minimal interaction
of the hydrogen close to the cylinder liner and the hydrogen in
the piston bowl/injection region is observed after the injection
event ends, with two clear separate zones of recirculation
forming.
Fig. 8 depicts the impact of the impinging hydrogen jet on
the ﬂow ﬁeld during and after the gaseous injection event.
Initially, prior to impingement, the free-jet displaces the air
around it, pushing air both ahead of itself towards the piston
bowl/chamber liner and also around itself and back towards
the injectors. This is partly attributed to the minimal air
entertainment in the early development of the jet, as evi-
denced by the lack of premixed combustion and rich core.
Upon impingement, the jet curls up in the piston bowl,
spreading out as it impinges on the wall. The momentum of
the jet pushes hydrogen along the wall in all directions.
Recirculation zones form in the piston bowl and towards the
top of the chamber near the liner which slows the rate of
combustion as fuel rich areas form. After a time the outward
spreading leads to contact of the jet with those from other
injectors, and this interaction slows the lateral movement but
further propels the jet back up the slope towards the injectors.
Finally the injection event ends and the lack of momentum
and decaying core leads to high levels of recirculation along
the trajectory of the jet which combines with the fuel which
was pushed back towards the injectors. This process en-
hances the combustion rate somewhat and also leads to the
formation of a large high temperature zone as can be seen in
the 740
/C14 CA/750/C14 CA contours in Fig. 7.
The temperature contours shown in Fig. 9 show the stark
contrast between the ignition and combustion process as
gaseous energy share is increased at LL (C0 and C1 compared).
At 99% the diesel injection offers so little temperature rise that
by the time the gaseous injection begins there is essentially no
hot products combusting (top right 720
/C14 CA) leading to no
ignition for either fuel. At 97% operation improves a lot
compared to 99% as the pilot provides enough energy to ignite
the jet. However, the ignition is delayed as shown by the
720
/C14 CA methane contour (same is observed for hydrogen at
earlier crank angles than shown) which also reduces initial jet
Fig. 6 e Description of the general combustion process in a dual direct injection hydrogen-diesel dual-fuel compression
ignition engine (high load 95% HES case 1 shown).
international journal of hydrogen energy 49 (2024) 674 e696 685

<!-- PDF_PAGE: 13 -->

penetration as the acceleration of the jet via combustion oc-
curs later than in the 95% cases. This late ignition leads to a
much higher gaseous fuel burning rate early in the injection
and can be observed in the 730
/C14 CA and 740/C14 CA contours where
the temperatures in the centre of the sector are higher than
the same regions at 95% energy share. The reduced penetra-
tion rate also contributes to the more focussed central com-
bustion site as there is greater fuel dispersion which is why
the ﬂame is somewhat wider at 97% energy share. There are
also lower temperatures in the near injector region
throughout at 97% energy share both because the initial
combustion occurs slightly later into the gaseous jets trajec-
tory and also due to the reduction in pilot volume. These
contours highlight the importance of the pilot injection and
the need to optimise its volume and ignition timing to ensure
that an adequately high temperature region is present when
the gaseous injection begins.
3.3. Performance and emission characteristics
At this point we note that thermal efﬁciency is calculated
using the gross indicated work, i.e. integrating only pressure/
volume between IVC and EVO, thus the values are somewhat
higher than would be expected in a practical engine as the
various losses are not accounted for. The engine operating on
an overexpanded cycle (50
/C14 longer expansion stroke compared
to compression) also contributes. However, trends captured
are more important than the absolute value so this should not
be of concern. The same can be said for presenting the likes of
work or power output as the gross indicated version of these
Fig. 7 e Temperature contours for methane and hydrogen at high load 95% gaseous energy share (case 0 & 1).
international journal of hydrogen energy 49 (2024) 674 e696686

<!-- PDF_PAGE: 14 -->

quantities are linearly linked to the gross indicated thermal
efﬁciency.
Fig. 10 presents the calculated emissions and thermal ef-
ﬁciency of each case at HL. Clearly as expected hydrogen leads
to much higher NOx emissions than methane due to the much
faster and higher temperature combustion observed, howev-
er, the reduction of supplied carbon leads to a considerable
decreases in all carbon based emissions. Due to the high fuel
burning efﬁciency at HL this also means hydrogen emissions
are lower in the hydrogen cases as the breakdown of UHCs
ends up outweighing any unburned injected hydrogen fuel
(this could also be an indication that the fuel mechanism
needs to be improved, but nonetheless indicates high fuel
utilisation in the hydrogen cases). Performance also sees a
small uplift across most hydrogen cases compared to
methane. The performance increase is smaller than might be
expected when comparing the pressure graphs but this is due
to the increased late power stroke pressures in the methane
cases as the oxidation of UHCs continues to produce heat, and
therefore work, all the way up to EVO.
There is relatively little change between each hydrogen
case across all the energy shares. The two key points to note
are the injection rate increase leading to increased NO
x
emissions due to the increased rate of burning causing higher
in-cylinder pressures and temperatures, and very similar
performance (in some cases reduced) compared to the original
hydrogen case. This poor performance trend can likely be
somewhat attributed to the reduction in free jet combustion
Fig. 8 e Streamlines and hydrogen isosurface at a mass fraction of 0.001 showing the jet induced ﬂow ﬁeld at HL 95% HES.
international journal of hydrogen energy 49 (2024) 674 e696 687

<!-- PDF_PAGE: 15 -->

occurring as the jet contacts the chamber wall earlier. This
indicates C2, C3 and C4 are not effective strategies going
forwards.
However, one of the signiﬁcant ﬁndings is the decrease in
UHC emissions as the injection rate is increased at 95% HES.
Not only do the higher temperatures aid in this process but the
increased convection due to the higher jet momentum and
larger mach disk diameters in C2, C3 and C4 improve the
mixing in the near injector area leading to improvements to
the pilot burning. Pilot combustion products also often get
entrained in the jet (also improved by momentum/diameter)
and are burned as it penetrates the chamber further
improving utilisation. This process is shown in Fig. 11 where it
is clear that in C1 more of the UHCs are accumulating in the
near injector region whereas in C3 more UHCs are entrained in
the hydrogen jet and are being pushed into the piston bowl.
The entrained UHCs then burn efﬁciently with the hydrogen
jet as they penetrate the chamber. At higher energy shares,
where the pilot penetration is reduced, poorer pilot burning is
sometimes observed leading to higher UHC emissions due to
the combustion products getting stuck behind the injector.
This is a result of the increased mach disk/core length
reducing gaseous jet combustion close to the injector
compared to lower pressure ratio/nozzle diameter cases and
in some cases the higher momentum jet pushes more air
around itself and back towards the injector area, essentially
trapping the already poorly penetrating pilot products behind
the jet in the injector region (see Fig. 8).
Comparing the contours for C1, C2, C3 and C4 at HL 99%
HES, Fig. 12 , it is clear that simply increasing injection rate
does not necessarily improve combustion and mixing of the
hydrogen with oxidiser. In fact, the jets increased momentum
causes the hydrogen, which in C1 gets caught close to the
liner, to deﬂect off the walls and move back towards the
injector region where there is a lack of oxidiser because of the
combustion which already took place there. The highest NO
x
levels occur close to the top of the chamber along the trajec-
tory of the hydrogen injection and to a lesser extent along the
piston bowl walls. This is ampliﬁed as the injection rate is
increased as the combustion is less spread out compared to C1
with the liner deﬂected hydrogen likely also enhancing the
NO
x production in the region. These contours clearly indicate
that slowing the hydrogen injection rate or increasing the
coverage/mixing of the injection should be an effective way to
Fig. 9 e Temperature contours comparing methane and hydrogen at low load 95%, 97% and 99% gaseous energy share (case
0 & 1).
international journal of hydrogen energy 49 (2024) 674 e696688

<!-- PDF_PAGE: 16 -->

control NOx while also potentially improving hydrogen uti-
lisation. The increased CO2 levels shown at the top left of the
contours are a clear indication of improved pilot utilisation
when jet momentum is increased leading to improved mixing
of the pilot combustion products with higher cylinder tem-
peratures also contributing. This improved mixing and uti-
lisation of UHCs is reﬂected in the soot contours also, where
for the most part soot levels reduce with the increase in jet
momentum due both to less initial formation and greater
oxidation.
Fig. 13 presents the calculated emissions and thermal ef-
ﬁciency of each case at LL. Comparing the 95% methane and
hydrogen cases it is clear that NO
x increases while carbon
based emissions generally decrease similar to the higher load
condition. UHCs do not tend to follow the same trend which is
due to a similar process to the one shown in Fig. 11 . The
reduced LL pilot penetration means pilot combustion products
get caught behind the injector and the reduced penetration of
the gaseous injection means the ﬂame struggles to curl up in
the piston bowl and make it back towards the injector and
burn the pilot fuel in the same way it does at HL (compare
740
/C14 CA contours in Fig. 7 with Fig. 9 ). This means UHC
oxidation is much more reliant on late power stroke com-
bustion which is much poorer for hydrogen cases. Perfor-
mance tends to decrease compared to methane due to the
overall poorer fuel utilisation.
At 97% energy share the unstable combustion leads to far
poorer fuel utilisation which causes high hydrogen and UHC
emissions combined with a reduction in performance when
compared to 95% energy share. NO
x emissions do tend to
Fig. 10 e Calculated HL thermal efﬁciency and NOx, soot, UHC, CO2 and H2 emissions at EVO for 95%, 97% and 99% gaseous
energy shares - methane hydrogen comparisons.
international journal of hydrogen energy 49 (2024) 674 e696 689

<!-- PDF_PAGE: 17 -->

reduce, but this is mostly due to the delayed onset of com-
bustion and lower levels of fuel burning reducing tempera-
tures. This is not the correct way to go about reducing NO
x but
does indicate that a later injection timing should be beneﬁcial
given adequate ignition can be achieved and also implies that
premixed combustion modes may offer some potential for
NOx reduction.
Clearly 99% energy share shows poor combustion all
around and therefore the likes of UHC and H2 emissions in-
crease dramatically while thermal efﬁciency drops to near 0%
Fig. 11 e UHC isosurfaces at 0.05% mass fraction with OH mass fraction contours at 95% HES HL cases 1 and 3.
international journal of hydrogen energy 49 (2024) 674 e696690

<!-- PDF_PAGE: 18 -->

Fig. 12 e Contours of temperature, NOx, CO2, soot and hydrogen at EVO for HL 99% energy share of hydrogen (cases 1, 2, 3
and 4).
international journal of hydrogen energy 49 (2024) 674 e696 691

<!-- PDF_PAGE: 19 -->

levels. Improvements are clearly required for LL operation at
this high an energy share.
Fig. 14 compares contours of temperature and emissions at
EVO for the baseline methane and hydrogen cases (C0 and C1)
at LL 95% and 97% energy share. Methane cases have higher
late power stroke temperatures for both fuels which are higher
at the lower energy share because of the early rapid premixed
combustion in the 97% cases. Hydrogen cases have much
higher NO
x levels which cover a larger area of the chamber due
to the increased penetration and wider ﬂame than methane.
Hydrogen case CO
2 emissions are much lower than methane
and they are conﬁned to the near injector region. Both fuels
show a general decrease of CO2 at increasing energy share as a
result of much poorer fuel utilisation but also due to lower
carbon levels in the chamber in general. Soot is extremely low
in all but the 95% methane case and it is conﬁned to the low
temperature region close to the cylinder liner and along the
chamber walls close to the injector where unburned fuel has
pooled. An area of unburned hydrogen forms at the top of the
cylinder close to the liner in the 97% hydrogen case due to the
unstable combustion meaning some of the unburned fuel gets
trapped above the piston bowl at too low a temperature to burn.
Fig. 13 e Calculated LL thermal efﬁciency and NOx, soot, UHC, CO2 and H2 emissions at EVO for 95%, 97% and 99% gaseous
energy shares - methane hydrogen comparisons.
international journal of hydrogen energy 49 (2024) 674 e696692

<!-- PDF_PAGE: 20 -->

Fig. 14 e Contours of temperature, NOx, CO2, soot and hydrogen at EVO for LL 95% and 97% energy share of hydrogen and
methane (cases 0 and 1).
international journal of hydrogen energy 49 (2024) 674 e696 693

<!-- PDF_PAGE: 21 -->

4. Conclusions
A numerical study using three-dimensional computational
ﬂuid dynamics is performed to investigate a diesel pilot
ignited late high pressure direct gaseous hydrogen injection
engine targeting non-premixed combustion and comparisons
are made with the same engine running on methane. High
and low load conditions are simulated at 95%, 97% and 99%
gaseous energy shares. Some of the key ﬁndings include:
/C15 Four main phases of dual direct-injection non-premixed
combustion are identiﬁed, namely: a) gaseous jet ignition
delay, b) free-jet combustion, c) wall-jet combustion and d)
late combustion phases.
/C15 Ignition is generally rapid with little to no premixed com-
bustion present with hydrogen showing shorter ignition
delay times than methane.
/C15 Free-jet combustion is the phase before the jet contacts the
chamber walls with the end of the phase being signalled by
the quenching of the front of the non-premixed ﬂame at
the chamber walls leading to a reduction in its volume and
thus fall off from peak heat release rate (HRR). Combustion
efﬁciency is high in this phase which is reﬂected in the high
HRR levels observed. Generally hydrogen has a higher peak
HRR due to a wider ﬂame and faster climb to said peak as a
result of faster jet penetration.
/C15 Wall-jet combustion begins with the jets ﬁrst impingement
on the chamber wall. HRR initially falls off then levels out
at a moderate level as fuel begins to pool along the cham-
ber walls. The injected fuel spreads out in all directions and
can come in contact with injections from other sectors of
the chamber. For the most part hydrogen stays at a higher
HRR than methane due to a smaller quenching distance,
greater jet momentum and higher rich ﬂammability limit.
/C15 The late combustion phase begins after the injection event
has ended and HRR begins to fall off rapidly. Hydrogen
tends to have a faster fall off and lower HRR level in the late
power stroke as its short efﬁcient breakdown pathway
means more fuel was utilised early in the power stroke
when compared to methane which still has unburned hy-
drocarbons to oxidise.
/C15 In general, hydrogen combustion leads to higher NO
x levels
than methane but much reduced carbon based emissions.
/C15 Hydrogen performance increases at high load compared to
methane but decreases slightly at low load in the current
setup.
/C15 Increasing injection rate through either injection pressure
or injector diameter increase leads to an increase in NO
x
emissions without a performance gain and in some cases
can lead to a reduction in performance. This trend can be
somewhat attributed to part of the free-jet combustion
phase being shifted into the wall-jet phase and thus
reducing combustion efﬁciency.
/C15 High load operation does not deteriorate at hydrogen en-
ergy shares (HES) up to 99% due to adequate gaseous jet
ignition by the diesel pilot.
/C15 Low load operation however does deteriorate as the diesel
pilot volume reduces too much and combustion begins to
become unstable when 95% HES is exceeded, causing long
gaseous jet ignition delays and high levels of premixed
combustion. Further increase to 99% HES leads to little to
no combustion of the gaseous jet. Similar results were
found for methane.
Four clear problems which need to be addressed with
respect to high HES dual-direct injection operation are
identiﬁed:
1. Poor low load performance at very high HES due to inade-
quate jet ignition by the reduced pilot.
2. Unstable combustion at low load as HES is increased due to
delayed jet ignition by the reduced pilot.
3. Higher NO
x output compared to methane due to hydrogen's
much faster burning rate, wider ﬂammability limit and
higher temperature combustion.
4. Further understanding of how various engine and injection
parameters impact the ﬂow ﬁeld and combustion, emis-
sions and performance characteristics is required.
The above issues will be investigated at multiple load
conditions in a following study via exploration and optimi-
sation of various parameters/approaches pertinent to 99%
HES engine operation such as pilot injection timing, gaseous
injection timing, number of injections, injector diameter, in-
jection angle, EGR rate, turbocharging level and initial oxidiser
charge temperature.
Declaration of competing interest
The authors declare that they have no known competing
ﬁnancial interests or personal relationships that could have
appeared to inﬂuence the work reported in this paper.
references
[1] IEA. Global Energy review 2021. Paris: IEA; 2021. Tech. Rep.
[2] Dicks AL, Rand DAJ. Fuel cell systems explained. John Wiley
& Sons; 2018 .
[3] Murugan A, Brown AS. Review of purity analysis methods for
performing quality assurance of fuel cell hydrogen. Int J
Hydrogen Energy 2015;40(11):4219 e33. https://doi.org/
10.1016/j.ijhydene.2015.01.041.
[4] Acar C, Dincer I. The potential role of hydrogen as a
sustainable transportation fuel to combat global warming.
Int J Hydrogen Energy 2020;45(5):3396 e406. https://doi.org/
10.1016/j.ijhydene.2018.10.149.
[5] Hosseini SE, Butler B. An overview of development and
challenges in hydrogen powered vehicles. Int J Green Energy
2020;17(1):13e37. https://doi.org/10.1080/
15435075.2019.1685999.
[6] Heywood J. Internal combustion engine fundamentals.
McGraw-Hill Education; 1988 .
international journal of hydrogen energy 49 (2024) 674 e696694

<!-- PDF_PAGE: 22 -->

[7] Dimitriou P, Tsujimura T. A review of hydrogen as a
compression ignition engine fuel. Int J Hydrogen Energy
2017;42(38):24470e86. https://doi.org/10.1016/
j.ijhydene.2017.07.232.
[8] Yip HL, Srna A, Yuen ACY, Kook S, Taylor RA, Yeoh GH,
Medwell PR, Chan QN. A review of hydrogen direct injection
for internal combustion engines: towards carbon-free
combustion. Appl Sci 2019;9(22):4842. https://doi.org/10.3390/
app9224842.
[9] Munshi S, Garner G, Theissl H, Hofer F, Razer B. Total cost of
ownership (TCO) analysis for heavy duty hydrogen fueled
powertrains, Tech. rep., Westport Fuel Systems and AVL List
GmbH (1-10, February 25, 2021).
[10] Mohammadi A, Shioji M, Nakai Y, Ishikura W, Tabo E.
Performance and combustion characteristics of a direct
injection SI hydrogen engine. Int J Hydrogen Energy
2007;32(2):296e304. https://doi.org/10.1016/
j.ijhydene.2006.06.005.
[11] Rottengruber H, Berckmu ¨ ller M, Els €asser G, Brehm N,
Schwarz C. Direct-injection hydrogen SI-engine - operation
strategy and power density potentials, SAE Technical paper
2004-01-2927. Warrendale, PA: SAE International; Oct. 2004.
https://doi.org/10.4271/2004-01-2927.
[12] Kim YY, Lee JT, Choi GH. An investigation on the causes of
cycle variation in direct injection hydrogen fueled engines.
Int J Hydrogen Energy 2005;30(1):69 e76. https://doi.org/
10.1016/j.ijhydene.2004.03.041.
[13] Tsujimura T, Suzuki Y. Development of a large-sized direct
injection hydrogen engine for a stationary power generator.
Int J Hydrogen Energy 2019;44(22):11355 e69. https://doi.org/
10.1016/j.ijhydene.2018.09.178.
[14] Li Y, Gao W, Zhang P, Ye Y, Wei Z. Effects study of injection
strategies on hydrogen-air formation and performance of
hydrogen direct injection internal combustion engine. Int J
Hydrogen Energy 2019;44(47):26000 e11. https://doi.org/
10.1016/j.ijhydene.2019.08.055.
[15] Boretti AA, Watson HC. The lean burn direct injection jet
ignition gas engine. Int J Hydrogen Energy
2009;34(18):7835e41. https://doi.org/10.1016/
j.ijhydene.2009.07.022.
[16] Welch AB, Wallace JS. Performance characteristics of a
hydrogen-fueled diesel engine with ignition assist.
Warrendale, PA: SAE Technical Paper 902070, SAE
International; Oct. 1990. https://doi.org/10.4271/902070.
[17] Homan HS, Reynolds RK, De Boer PCT, McLean WJ.
Hydrogen-fueled diesel engine without timed ignition. Int J
Hydrogen Energy 1979;4(4):315 e25. https://doi.org/10.1016/
0360-3199(79)90006-5.
[18] Furuhama S, Kobayashi Y. Development of a hot-surface-
ignition hydrogen injection two-stroke engine. Int J
Hydrogen Energy 1984;9(3):205 e13. https://doi.org/10.1016/
0360-3199(84)90120-4.
[19] Rosati MF, Aleiferis PG. Hydrogen SI and HCCI combustion in
a direct-injection optical engine. SAE International Journal of
Engines 2009;2(2009 e01-1921):1710e36. https://doi.org/
10.4271/2009-01-1921.
[20] Aleiferis PG, Rosati MF. Controlled autoignition of hydrogen
in a direct-injection optical engine. Combust Flame
2012;159(7):2500e15. https://doi.org/10.1016/
j.combustﬂame.2012.02.021
.
[21] Gomes Antunes JM, Mikalsen R, Roskilly AP. An investigation
of hydrogen-fuelled HCCI engine performance and
operation. Int J Hydrogen Energy 2008;33(20):5823 e8. https://
doi.org/10.1016/j.ijhydene.2008.07.121.
[22] Gowda BD, Echekki T. Complex injection strategies for
hydrogen-fueled HCCI engines. Fuel 2012;97:418 e27. https://
doi.org/10.1016/j.fuel.2012.01.060.
[23] Rottengruber H, Wiebicke U, Woschni G, Zeilinger K.
Wasserstoff-Dieselmotor mit Direkteinspritzung, hoher
Leistungsdichte und geringer Abgasemission. MTZ Mot Z
2000;61(2):122e8. https://doi.org/10.1007/BF03226557.
[24] Gomes Antunes JM, Mikalsen R, Roskilly AP. An experimental
study of a direct injection compression ignition hydrogen
engine. Int J Hydrogen Energy 2009;34(15):6516 e22. https://
doi.org/10.1016/j.ijhydene.2009.05.142.
[25] Babayev R, Andersson A, Dalmau AS, Im HG, Johansson B.
Computational characterization of hydrogen direct injection
and nonpremixed combustion in a compression-ignition
engine. Int J Hydrogen Energy 2021;46(35):18678 e96. https://
doi.org/10.1016/j.ijhydene.2021.02.223.
[26] Babayev R, Andersson A, Serra Dalmau A, Im HG,
Johansson B. Computational comparison of the conventional
diesel and hydrogen direct-injection compression-ignition
combustion engines. Fuel 2022;307:121909. https://doi.org/
10.1016/j.fuel.2021.121909.
[27] Babayev R, Andersson A, Serra Dalmau A, Im HG,
Johansson B. Computational optimization of a hydrogen
direct-injection compression-ignition engine for jet mixing
dominated nonpremixed combustion. Int J Engine Res
2022;23(5):754e68. https://doi.org/10.1177/14680874211053556.
[28] Frankl S, Gleis S, Karmann S, Prager M, Wachtmeister G.
Investigation of ammonia and hydrogen as CO2-free fuels for
heavy duty engines using a high pressure dual fuel
combustion process. Int J Engine Res 2021;22(10):3196 e208.
https://doi.org/10.1177/1468087420967873.
[29] Liu X, Aljabri H, Panthi N, AlRamadan AS, Cenker E,
Alshammari AT, Magnotti G, Im HG. Computational study of
hydrogen engine combustion strategies: dual-Fuel
compression ignition with Port- and Direct-Injection, Pre-
Chamber Combustion, and Spark-Ignition. Fuel
2023;350:128801. https://doi.org/10.1016/j.fuel.2023.128801.
[30] Liu X, Seberry G, Kook S, Chan QN, Hawkes ER. Direct
injection of hydrogen main fuel and diesel pilot fuel in a
retroﬁtted single-cylinder compression ignition engine. Int J
Hydrogen Energy 2022;47(84):35864 e76. https://doi.org/
10.1016/j.ijhydene.2022.08.149.
[31] Rorimpandey P, Yip HL, Srna A, Zhai G, Wehrfritz A, Kook S,
Hawkes ER, Chan QN. Hydrogen-diesel dual-fuel direct-
injection (H2DDI) combustion under compression-ignition
engine conditions. Int J Hydrogen Energy 2023;48(2):766 e83.
https://doi.org/10.1016/j.ijhydene.2022.09.241.
[32] McTaggart-Cowan GP, Jones HL, Rogak SN, Bushe WK,
Hill PG, Munshi SR. The effects of high-pressure injection on
a compression-ignition, direct injection of natural gas
engine. In: ASME 2005 internal combustion engine division
fall technical conference. American Society of Mechanical
Engineers Digital Collection; 2008. p. 161 e73. https://doi.org/
10.1115/ICEF2005-1213.
[33] Barba C, Dyckmans J, F €orster J, Schnekenburger T. Natural
gas-Diesel dual fuel for commercial vehicle engines. In:
Liebl J, Beidl C, editors. Internationaler motorenkongress
2017, proceedings. Wiesbaden: Springer Fachmedien; 2017.
p. 391 e407. https://doi.org/10.1007/978-3-658-17109-4_23.
[34] Dai LM. Study of the injection and mixture process and the
combustion simulation of natural gas/diesel dual-fuel, masters
dissertation. Zhenjiang, China: Jiangsu University; 2016.
[35] Mabson CWJ. Emissions characterization of paired gaseous jets
in a pilot-ignited natural-gas compression-ignition engine.
Vancouver: MSc, The University of British Columbia; 2015.
[36] Kheirkhah P. CFD modelling of injection strategies in a high-
pressure direct-injection (HPDI) natural gas engine.
Vancouver: MSc, The University of British Columbia; 2015 .
[37] Rochussen J, McTaggart-Cowan G, Kirchen P. Parametric
study of pilot-ignited direct-injection natural gas
international journal of hydrogen energy 49 (2024) 674 e696 695

<!-- PDF_PAGE: 23 -->

combustion in an optically accessible heavy-duty engine. Int
J Engine Res 2020;21(3):497 e513. https://doi.org/10.1177/
1468087419836877.
[38] Jud M, Wieland C, Fink G, Sattelmayer T. Numerical analysis
of the combustion process in dual-fuel engines with direct
injection of natural gas. In: ASME 2018 internal combustion
engine division fall technical conference. American Society
of Mechanical Engineers Digital Collection; 2019. https://
doi.org/10.1115/ICEF2018-9579.
[39] Faghani E. Effect of injection strategies on particulate matter
emissions from HPDI natural-gas engines. Vancouver: Ph.D.
thesis, The University of British Columbia; 2015 .
[40] Chaichan M. The impact of equivalence ratio on
performance and emissions of a hydrogen-diesel dual fuel
engine with cooled exhaust gas recirculation. Int J Sci Eng
Res 2015;6:938 e41.
[41] van Lipzig JPJ, Nilsson EJK, de Goey LPH, Konnov AA. Laminar
burning velocities of n-heptane, iso-octane, ethanol and
their binary and tertiary mixtures. Fuel 2011;90(8):2773 e81.
https://doi.org/10.1016/j.fuel.2011.04.029.
[42] Haynes WM. CRC handbook of chemistry and physics. 95th
ed. CRC Press; 2014 .
[43] Alternative fuels data center. https://www.afdc.energy.gov/
fuels/fuel_properties.php. [Accessed June 2018].
[44] Turns SR. An introduction to combustion: concepts and
applications. 3rd ed. New York: McGraw-Hill Education; 2011 .
[45] Green DW, Perry RH. Perry 's chemical engineers ' handbook.
8th ed. McGraw-Hill Education; 2008 .
[46] Imhoff TB, Gkantonas S, Mastorakos E. Analysing the
performance of ammonia powertrains in the marine
environment. Energies 2021;14(21):7447. https://doi.org/
10.3390/en14217447.
[47] Takizawa K, Igarashi N, Takagi S, Tokuhashi K, Kondo S.
Quenching distance measurement of highly to mildly
ﬂammable compounds. Fire Saf J 2015;71:58 e68. https://
doi.org/10.1016/j.ﬁresaf.2014.11.013.
[48] Zeldovich YB. Selected works of yakov borisovich zeldovich
ch 26. Oxidation of nitrogen in combustion and explosions ”.
of Selected Works of Yakov Borisovich Zeldovich, Princeton
University Press 2014;1 .
[49] Fenimore CP. Formation of nitric oxide in premixed
hydrocarbon ﬂames. Symposium (International) on
Combustion 1971;13(1):373 e80. https://doi.org/10.1016/
S0082-0784(71)80040-1.
[50] Brookes SJ, Moss JB. Predictions of soot and thermal radiation
properties in conﬁned turbulent jet diffusion ﬂames.
Combust Flame 1999;116(4):486 e503. https://doi.org/10.1016/
S0010-2180(98)00056-X.
[51] C. J. Ramsay, K. K. J. R. Dinesh, High pressure direct injection
of gaseous fuels using a discrete phase methodology for
engine simulations, Int J Hydrogen Energy doi:10.1016/
j.ijhydene.2021.10.235.
[52] Hessel RP, Abani N, Aceves SM, Flowers DL. Gaseous fuel
injection modeling using a gaseous sphere injection
methodology, SAE Technical paper 2006-01-3265.
Warrendale, PA: SAE International; Oct. 2006. https://doi.org/
10.4271/2006-01-3265.
[53] J. C. Beale, R. D. Reitz, Modeling spray atomization with the
kelvin-helmholtz/Rayleigh-Taylor hybrid model,
Atomization Sprays 9 (6). doi:10.1615/AtomizSpr.v9.i6.40.
[54]
O'Rourke PJ. Collective drop effects on vaporizing liquid
sprays, Tech. Rep. LA-9069-T. NM (USA: Los Alamos National
Lab.; Nov. 1981 .
[55] Liu AB, Mather D, Reitz RD. Modeling the effects of drop drag
and breakup on fuel sprays. SAE Trans 1993;102:83 e95. arXiv:
44611358.
[56] O'Rourke PJ, Amsden AA. A spray/wall interaction submodel
for the KIVA-3 wall ﬁlm model. SAE Trans 2000;109:281 e98.
arXiv:44634219.
[57] Stanton DW, Rutland CJ. Modeling fuel ﬁlm formation and
wall interaction in diesel engines. SAE Trans
1996;105:808e24. arXiv:44736319 .
[58] Gosman AD, loannides E. Aspects of computer simulation of
liquid-fueled combustors. J Energy 1983;7(6):482 e90. https://
doi.org/10.2514/3.62687.
[59] Shih T-H, Liou WW, Shabbir A, Yang Z, Zhu J. A new k-
epsilon eddy viscosity model for high Reynolds number
turbulent ﬂows. Comput Fluid 1995;24(3):227 e38. https://
doi.org/10.1016/0045-7930(94)00032-T.
[60] Pope SB. Computationally efﬁcient implementation of
combustion chemistry using in situ adaptive tabulation.
Combust Theor Model 1997;1(1):41 e63. https://doi.org/
10.1080/713665229.
[61] Nordin N. Numerical simulations of non-steady spray
combustion using a detailed chemistry approach. Licentiate
of Engineering, Chalmers University of Technology, Dept. of
Thermo and Fluid Dynamics; 1998 .
[62] Smith G, Golden D, Frenklach M, Moriarty N, Eiteneer B,
Goldenberg M, Bowman C, Hanson R, Song S, Gardiner W,
Lissianski VV, Qin Z. GRI-Mech 3.0. http://www.me.berkley.
edu/gri_mech/.
[63] K /C19eromn/C18es A, Metcalfe WK, Heufer KA, Donohoe N, Das AK,
Sung C-J, Herzler J, Naumann C, Griebel P, Mathieu O,
Krejci MC, Petersen EL, Pitz WJ, Curran HJ. An experimental
and detailed chemical kinetic modeling study of hydrogen
and syngas mixture oxidation at elevated pressures.
Combust Flame 2013;160(6):995 e1011. https://doi.org/
10.1016/j.combustﬂame.2013.01.001.
[64] Pomraning E, Richards K, Senecal PK. Modeling turbulent
combustion using a RANS model, detailed chemistry, and
adaptive mesh reﬁnement, SAE Technical paper 2014-01-
1116. Warrendale, PA: SAE International; Apr. 2014. https://
doi.org/10.4271/2014-01-1116.
[65] Senecal PK, Richards KJ, Pomraning E, Yang T, Dai MZ,
McDavid RM, Patterson MA, Hou S, Shethaji T. A new parallel
cut-cell cartesian CFD code for rapid grid generation applied
to in-cylinder diesel engine simulations, SAE Technical
paper 2007-01-0159. Warrendale, PA: SAE International; Apr.
2007. https://doi.org/10.4271/2007-01-0159.
[66] Z. Wang, K. K. Srinivasan, S. R. Krishnan, S. Som, A
computational investigation of diesel and biodiesel
combustion and NOx formation in a light-duty compression
ignition engine, Combustion Institute (GO8602569).
doi:https://www.osti.gov/biblio/1079596.
[67] Wijeyakulasuriya S, Jupudi RS, Givler S, Primus RJ,
Klingbeil AE, Raju M, Raman A. Multidimensional modeling
and validation of dual-fuel combustion in a large bore
medium speed diesel engine. In: ASME 2015 internal
combustion engine division fall technical conference.
American Society of Mechanical Engineers Digital Collection;
2016. https://doi.org/10.1115/ICEF2015-1077.
[68] Hogg T, Stojanovic S, Tebbs A, Samuel S, Durodola J. A
benchmark study on the ﬂow metering systems for the
characterisation of fuel injectors for future heavy duty
commercial vehicles. Measurement 2020;153:107414. https://
doi.org/10.1016/j.measurement.2019.107414.
international journal of hydrogen energy 49 (2024) 674 e696696
