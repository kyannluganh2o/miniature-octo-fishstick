<!-- PDF_PAGE: 1 -->

Standard Article
International J of Engine Research
2023, V ol. 24(8) 3342–3358
/C211IMechE 2023
Article reuse guidelines:
sagepub.com/journals-permissions
DOI: 10.1177/14680874221148789
journals.sagepub.com/home/jer
Numerical characterization of
hydrogen under-expanded jets with a
focus on Internal Combustion Engines
applications
Giuseppe Anaclerio1 , T ommaso Capurso1,2, Marco T orresi1
and Sergio Mario Camporeale1
Abstract
In the context of reducing carbon dioxide ( CO2) emissions, hydrogen is gaining momentum as a possible fuel for Internal
Combustion Engines (ICEs). In-cylinder direct injections allow for a higher specific power density while enabling different
levels of charge stratification. The high-pressure injection leads to the onset of under-expanded jets, characterized by
complex patterns of shock waves and expansion fans. In ICEs simulations, such physics needs to be correctly solved to
obtain a reliable assessment of the mixture formation. In this paper, the main features of hydrogen under-expanded jets
are examined under the conditions typically found in turbocharged engines. Improved correlations are provided for the
assessment of the Mach disk height and diameter , up to a Nozzle Pressure Ratio (NPR) equal to 60. The dependency of
the hydrogen-air mixing on the cylinder temperature has been analyzed, and the unsteady jet dynamics has been exam-
ined by continuously varying the combustion chamber pressure. T o the authors’ knowledge, no studies of this kind can
be found in the literature for the specific case of hydrogen. Lastly, a preliminary investigation of the jet-jet interaction
(a Coanda-like effect) is reported. This phenomenon is observable when multi-hole injectors are employed, and it may
have a great impact on the mixture formation.
Keywords
Hydrogen, underexpanded jet, direct injection, ICE, hydrogen safety, Mach disk, computational fluid dynamics
Date received: 18 August 2022; accepted: 14 December 2022
Introduction
The efficient exploitation of eco-friendly energy sources
has become mandatory to decrease greenhouse gas
(GHG) emissions. One of the challenging issues in the
adoption of renewable sources is the lack of synchron-
ism between demand and production. The Power-to-
Gas technology
1 is a feasible solution to store excess of
energy by producing hydrogen, which can then be used
to power Internal Combustion Engines (ICEs), either
pure or blended with conventional fuels.
2 Hydrogen
can thus be considered as one of the possible solutions
to achieve a climate-neutral mobility along with electric
propulsion.
3 Hydrogen shows suitable chemical and
physical properties to be exploited in ICEs. The Lower
Heating Value (LHV) per unit mass is almost three
times higher than gasoline and diesel fuels ( ;120 MJ/
kg vs ;42–46 MJ/kg), and the flammability range is
wide. As a consequence, lean fuel-air mixtures can be
burnt, leading to lower heat losses and unthrottled
operations even at low loads. Hence, high efficiencies
are achievable.
20 In spite of this, the low ignition energy
can lead to pre-ignition, knocking, and backfiring, and
the volumetric efficiency is not sufficient when the Port
Fuel Injection (PFI) architecture is employed.
4 All of
these complications can be overcome by adopting the
Direct Injection (DI) technology. An optimized direct-
injection strategy results in a higher engine efficiency
and lower NOx production. Delaying the Start of
Injection (SOI) produces a stratified mixture,
5 with a
1Department of Mechanics, Mathematics and Management – Politecnico
di Bari, Bari, Italy
2Arts et Metiers Institute of T echnology, LIFSE, CNAM, HESAM
University, Paris, France
Corresponding author:
Giuseppe Anaclerio, Department of Mechanics, Mathematics,
Management, Politecnico di Bari, Via Re David, 200, Bari 70125, Italy.
Email: giuseppe.anaclerio@poliba.it

<!-- PDF_PAGE: 2 -->

rich mixture near the spark and a lean one close to the
walls.6 In this way, wall heat losses and the mean cycle
temperature are reduced, resulting in near-to-zero NOx
emissions. Furthermore, delaying the SOI diminishes
the compression work applied to the in-cylinder gas.
7
However, a very delayed SOI can lead to unstable com-
bustion issues due to a low-quality mixture, particularly
at low loads and medium-high crank speeds.
8 The use
of multi-injection strategies has proven to be another
effective way to minimize NOx production at high
loads, with a slight reduction in engine efficiency at
higher RPM.
9 Due to the short time available to inject
the fuel, DI requires a high feeding pressure (between
100 and 250 bar)
10 at the nozzle inlet, leading to the
onset of an under-expanded hydrogen jet. The main
features of such flows are the subject of this analysis.
Because of the vast number of engineering applications
in which underexpanded jets can be found, literature is
rich in both experimental and numerical studies.
Historically, the first analyses have focused on the near-
field zone of the jet, where the most intense
gas-dynamics phenomena occur.
11,12 Thanks to the
increasing computational power available for research,
numerical simulations have become a reliable tool to
study the main properties of these jets. Banholzer 13 has
numerically characterized underexpanded methane jets
at various Nozzle Pressure Ratios (NPRs), reporting
the different structures observed. Jet-tip penetration
has been studied for several ambient pressures and the
effect of fuel and ambient temperatures on the phases
separation has been analyzed. Concerning fossil fuel
powered ICEs, direct injection of natural gas has been
studied in White and Milton.
14 Here, a CFD code has
been validated against the experimental data regarding
the flow discharged at ambient conditions. Vuorinen
et al.
15 were the first to propose a systematic evaluation
of the NPR influence on the jet structure by means of
LES simulations. An extensive amount of literature
exists concerning underexpanded jets ejected by non-
axisymmetric sections, as well. Elliptical jets have been
examined both numerically and experimentally by
Rajakuperan and Ramaswamy,
16 Menon and Skews, 17
Chauhan,18 and Anaclerio et al. 19 They all reported a
faster level of mixing with respect to circular jets.
Moreover, a faster growth of the jet boundary along
the minor axis plane was observed, together with a
quicker onset of the barrel shock in the major axis
plane. Analyses concerning rectangular nozzles can be
found in Rao and Abdol-Hamid
20 and Menon and
Skews.21 In particular, over-expanded conditions have
been observed at the nozzle corners, leading to the
onset of four re-compression shock waves. Higher mix-
ing has been reported as well, along with distinctive
saddle-shape profiles of the H
2 radial distribution.19,22–25
More recently, as research has shifted toward the devel-
opment of climate-neutral solutions, focus has been
placed on hydrogen underexpanded jets. A LES analysis
is reported in Hamzehloo and Aleiferis 26 for a fixed
NPR equal to 10 and several ambient pressures. For
higher ambient pressures a slightly quicker formation of
the Mach disk has been reported and correlations have
been proposed for the timewise jet-tip penetration. The
promise of a hydrogen-based economy poses relevant
concerns about safety.
27 Since hydrogen is stored at high
pressure and the flammability range is wide, a tank fail-
ure can easily lead to the formation of ignitable jets.
Most of the hazards are related to the farfield zone,
namely the region downstream of the shock structures
where an intense hydrogen-air mixing takes place. The
need of quick tools for the risk assessment cannot be sat-
isfied by time-expensive simulations on detailed meshes
of the whole jet. Thus, several strategies have been tested
and reported in the literature. In Xu et al.,
28 RANS
simulations have been employed on a reduced domain to
solve the nearfield structure, which has been subse-
quently imposed as initial condition to run LES compu-
tations of the farfield zone. Another common approach
is the replacement of the nearfield structure with a
notional nozzle ,
29 according to a pseudo-source
approach. Among the several models to describe the
notional nozzle, the Mach disk approach places the
notional nozzle just after the Mach disk, a jet feature
later described in this paper. To the authors’ opinion,
models describing the Mach disk features are still
affected by uncertainty. Moreover, literature regarding
the complex phenomena of hydrogen jets under the spe-
cific conditions found in inte rnal combustion engines is
scarce. Thus, the goals of this work have been:
/C15 to determine the correct numerical setup for com-
puting the main features of the underexpanded
jets. Attention has been paid to the optimum grid
size to minimize the computational effort
required for ICE simulations;
/C15 to improve literature models regarding the Mach
disk characteristics. Such data can be useful in the
context of the risk assessment too;
/C15 to determine the influence of the ICE conditions
on the jet. Focus has been posed to the variable
in-cylinder pressure, showing that hysteretic phe-
nomena do not occur;
/C15 to analyze the jet-jet interaction. To the authors’
knowledge, this topic has never been analyzed for
hydrogen jets. Nonetheless, it can have a serious
influence on the mixture formation process when
multi-hole nozzles are employed.
The paper is organized as follows. Paragraphs 2, 3, and
4 provide information about the underexpanded jet
structure and the correct way to setup fast and reliable
RANS simulations. The dependency of the underex-
panded structure on the pressure ratio is discussed in
Paragraph 5, and herein new correlations are provided
to estimate the Mach disk height and diameter more
accurately. In Paragraphs 6 and 7 the hydrogen jet fea-
tures are described in the context of ICE direct injection
process. When accurate CFD simulations of the ther-
modynamic cycle are needed, the knowledge of the
Anaclerio et al. 3343

<!-- PDF_PAGE: 3 -->

nearfield structure characteristics can be used to define
the extension of the mesh refinement close to the nozzle.
This leads to a better simulation of the fuel diffusion
during the injection and a more accurate reconstruction
of the mixture formation process. In addition to the
shock structure, hydrogen diffusion is analyzed with
respect to the combustion chamber temperature.
Furthermore, hysteretic phenomena have been assessed
in terms of shock cell and hydrogen distribution under
the Argonne ICE operating conditions.
30 Lastly, a
study of multi-nozzle configurations is reported.
Underexpanded jet structure
Depending on the NPR, literature distinguishes among
moderate (Figure 1(a)), highly (Figure 1(b))
31 and very
highly underexpanded jets (Figure 1(c)). 29 All the three
configurations exhibit a supersonic field just down-
stream of the nozzle exit section, where pressure quickly
drops as a result of the flow acceleration. The expan-
sion waves of the Prandtl–Mayer fan, originating from
the nozzle lips, are reflected by the constant pressure
line and turned into compression waves. These waves
then coalesce into a single oblique shock (the intercept-
ing or barrel shock) pointing to the jet centerline. From
a kinematic point of view, the axis behaves as a wall,
requiring that the flow does not have a radial velocity
component along the centerline. In order to meet this
constraint, in the moderately underexpanded case
(2 \ NPR \ 4), a reflected shock originates from the
axis to fix the flow deviation imposed by the intercept-
ing shock. This new shock will be once again reflected
by the external boundary and turned into a new expan-
sion fan, allowing the pattern to be replicated further
downstream. As it can be observed in Figure 2, for a
given Mach number there exists a maximum value of
the deflection that can be imposed through the forma-
tion of an oblique shock. For 4 \ NPR \ 7, the turn-
ing angle through the intercepting shock exceeds the
maximum deflection which can be imposed by the
reflected shock. In such a situation, the kinematic con-
straint can be met through the formation of the Mach
disk shock, which is locally normal to the axis
location.
32 The point where the intercepting shock, the
reflected shock, and Mach disk meet each other is
defined as the triple point. An embedded shear layer
propagates from this point, dividing the subsonic flow
downstream of the Mach disk and the supersonic flow
behind the reflected shock. The NPR . 7 jet is consid-
ered extremely underexpanded and it is characterized
by a single shock cell downstream of the nozzle exit.
The distance between the Mach disk and the nozzle exit
section (namely the Mach disk height, H
disk) is mainly
determined by the pressure ratio 33–35 and seems to be
independent of the fluid nature 36,37 and the nozzle exit
angle. Thus, its location is usually computed using the
following equation:
Hdisk=Dnozzle = CH
ﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ ﬃ
NPR
p
ð1Þ
Figure 1. Graphical representation of the main under-expanded jet structures: (a) moderately underexpanded jet (2 \ NPR \ 4),
(b) highly underexpanded jet (4 \ NPR \ 7), (c) Very highly (or extremely) underexpanded jet (NPR . 7).
Figure 2. Representation of the Mach reflection on the shock
angle b—flow deflection u plane. For a fixed Mach number
upstream of a shock, a maximum value of the flow deflection
exists. If the maximum deflection relative to the Mach number
downstream of the incident shock is lower than the imposed
deflection, a Mach reflection occurs.
3344 International J of Engine Research 24(8)

<!-- PDF_PAGE: 4 -->

where Dnozzle is the nozzle exit diameter and CH is a
constant. Various authors have proposed different val-
ues for C
H
15,38,39 either numerically or experimentally
assessed. A high level of uncertainty is present in the lit-
erature concerning the Mach disk diameter. It seems to
be dependent on the pressure ratio and the nature of
the fluid, showing an inverse proportionality to the
ratio of specific heats ( k = C
p=Cv).34 Moreover, it
seems to be influenced by the shape of the duct. 40,41
For a contoured nozzle, the following expression is
proposed in Franquet et al. 29
Ddisk=Dnozzle =0 :36
ﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ ﬃ
NPR /C0 3:9
p
ð2Þ
being Ddisk the Mach disk diameter.
Numerical methods
The aim of this work has been to examine the underex-
panded structure of a hydrogen jet under the condi-
tions typically found in internal combustion engines.
For this purpose, steady and unsteady RANS simula-
tions have been carried out by means of the commercial
CFD code ANSYS Fluent
/C210. For ICE analyses, the
RANS approach is still a valuable way to get insights
of the mixture formation process in a short time.
Indeed, Hamzehloo and Aleiferis 42 compared RANS
and LES simulations for a direct-injection test case,
showing that the bulk motion of the injected flow was
reliably captured by the RANS approach. To find the
correct numerical setup, a preliminary numerical
assessment has been performed. Fig. 3(a) shows the 2D
axisymmetric computational domain employed for the
simulations, together with the imposed boundary con-
ditions. At the inlet of the plenum (on the left side), a
total pressure of 10 bar and a total temperature of
300 K are imposed. To fill the plenum with pure hydro-
gen, the inlet mass fractions of O
2 and N 2 are set to
zero. A convergent nozzle, sketched following the
ASME MFC-3 M-2004, has been placed between the
plenum and the following discharging chamber. The
convergent nozzle has been preferred to convergent-
divergent configurations in order to analyze flows at
sonic condition (Mach equal to 1) in the nozzle exit sec-
tion. The nozzle exit diameter has been chosen equal to
1 mm, in order to validate the numerical model against
the experimental data reported in Hecht et al.
43
Keeping the inlet total pressure constant, the desired
NPR is defined by changing the uniform static pressure
at the outlet. Inside the discharging chamber, the mass
fractions of O
2 and N 2 are 0.23 and 0.77, respectively.
A hybrid mesh has been employed, featuring structured
blocks in the jet zone, as shown in Figure 3(b). Here
the cell size has been varied from 6 to 300 mm, in order
to carry out a mesh sensitivity analysis. The length of
the first refinement block just downstream the exit
plane has been set to 15 D
nozzle, while the second (with a
slightly higher cell dimension) has been set to 10 Dnozzle.
For the boundary layer treatment, wall functions have
been employed ensuring a y+ . 30. Steady RANS
equations have been solved using a coupled-pressure
based scheme, and a second order accurate upwind
scheme has been adopted for the spatial derivatives dis-
cretization. Hydrogen—air mixing has been assessed
solving the species transport equations provided by
ANSYS Fluent
/C210and here reported for the i-th chemi-
cal species:
∂rYi
∂t + r/C1 (r~vYi)= r/C1 ~Ji + Ri + Si ð3Þ
where Yi is the local mass fraction for the i-th species,
Ri the rate of production by chemical reactions and Si
a source term. ~Ji is the diffusion flux of species i due to
both concentration and thermal gradients. For a turbu-
lent flow, ANSYS Fluent computes ~J
i as:
Figure 3. (a) View of the computational domain with blocks partition and details of the nozzle geometry; (b) Comparison of three
different mesh refinements in the jet zone.
Anaclerio et al. 3345

<!-- PDF_PAGE: 5 -->

~Ji = /C0 rDi, m + mt
Sc
/C16/C17
rYi /C0 DT, i
rT
T ð4Þ
where Di, m is the mass diffusion coefficient, mt the tur-
bulent viscosity, Sc the Schmidt number (depending on
the turbulent diffusivity Dt) and DT, i is the thermal dif-
fusion coefficient, accounting for the Soret effect. 44 To
close the RANS equations, the k- v SST turbulence
model has been adopted, being able to efficiently cap-
ture shocks and expansions, as referred by the litera-
ture.13,45 Turbulence equations have been discretized
by means of a second-order accurate upwind scheme.
In addition to the ideal gas law, real gas assumptions
have been tested using the Redlich–Kwong and Peng–
Robinson models for the Equation of State (EoS).
These are both cubic models, whose general form is:
p = RT
v /C0 b + c /C0 a
v2 + vd + e ð5Þ
being a, b, c, d, and e constants related to the fluid criti-
cal pressure pc, critical temperature Tc, and acentric
factor v. In Appendix A, the equations to compute
these constants are reported for both the models. When
dealing with real-gas mixtures, ANSYS Fluent uses the
pseudo-critical method, by which the generic critical
constant of the mixture C
cm is computed on the basis
of the mass fractions and the critical constants of each
i-th component:
Ccm =
XN
i =1
xiCci ð6Þ
A mass-weighted mixing law has been enabled to com-
pute the local viscosity, where the i-th component visc-
osity has been modeled by the Sutherland’s law with
three parameters.
Validation
Before analyzing hydrogen jets under ICE conditions,
the numerical setup has been validated both from the
point of view of the gas-dynamics and the H
2 distribu-
tion. The validation has been carried out imposing a
total pressure of 10 bar in the plenum and 1 bar in the
ambient. In this way, the capability to reconstruct the
underexpanded structure has been tested against the
experimental results reported in Hecht et al.
43 At such
a level of underexpansion, the Mach disk height has
been considered a valuable benchmark for validation.
As it can be seen in the Schlieren picture reported in
Figure 4, for a NPR of 10 and a nozzle exit diameter of
1 mm, the Mach disk height is about 2 mm. A mesh
sensitivity analysis has been carried out by varying the
cell size in the nearfield zone of the jet according to the
values reported in Table 1.
The numerical Mach disk height is plotted in Figure 5
as a function of the number of cells. It is interesting to
note that when the coarsest mesh has been employed, it
has not been possible to identify the Mach disk.
Therefore, this can be seen as a threshold under which
the computed jet structure is not physically correct. As
expected, an asymptotic behavior can be observed when
the mesh density increases. Considering ;2m m a s t h e
experimental value of the disk height, an error band of
1% has been applied to Figure 5 in order to evaluate the
acceptable mesh sizing. The reader can observe that,
starting from a grid size of 33,000 cells, all the solutions
fall within the error band.
Figure 6 shows the Mach number contours varying
the mesh density. The occurrence of the Mach disk
starts when imposing a cell size of 0.1 mm near the noz-
zle exit plane, as visible in Figure 6(b). Nonetheless, the
T able 1. Mesh sensitivity data.
Cell dimension [ mm] Number of cells
300 3000
100 5000
30 18,000
20 33,000
10 70,000
6 130,000
Figure 4. Schlieren picture of the H 2 underexpanded jet for
NPR = 10 and nozzle exit diameter of 1 mm. 43 The Mach disk is
placed at 2 mm from the nozzle exit section.
Figure 5. Numerical Mach disk position as a function of the
number of cells, NPR = 10. The red straight line represents the
experimental disk position (2 mm).
43 An error band of 61% is
delimited by the dashed lines. Meshes between ;30,000 and
;130,000 cells provide results inside the error band.
3346 International J of Engine Research 24(8)

<!-- PDF_PAGE: 6 -->

reflected shock, the shear layer and the region down-
stream of the Mach disk are not clearly defined.
Meshes from 18,000 to 130,000 are instead fully able to
reconstruct the underexpanded jet according to the
structures previously described and reported in the lit-
erature. For ICEs analysis, another key feature to con-
sider is the hydrogen-air mixing along the jet. The
numerical H
2 axial distribution is reported in Figure 7,
while Figure 8 shows the radial distribution at 5, 15,
and 25 mm from the nozzle exit plane. The coarser the
mesh, the quicker the mass fraction drops along the
axis: at 15 mm from the exit plane, the difference in the
H
2 mass fraction is almost 100% between the coarsest
and the finest mesh. A good agreement in the resolu-
tion of the mass fraction is found for the meshes from
33,000 to 130,000 cells. Differences are significant in
the radial plots as well: the coarser meshes underesti-
mate the mass fraction in the inner zone and overesti-
mate it in the outer zone. This means that a wider jet
spread results when coarser meshes are employed. For
all the reasons mentioned above, the grid with 70,000
cells has been considered a good candidate to achieve a
reliable solution of the underexpanded jet in acceptable
computational time. As a final validation step, this grid
density and the numerical model have been tested
against the experimental results reported in Ruggles
and Ekoto
46 with respect to the hydrogen axial distri-
bution. Data refer to an underexpanded hydrogen jet
discharged by a rectangular nozzle for a NPR of 10.
This test case has been chosen because of the lack of
data regarding the mass fraction distribution for circu-
lar jets at NPR = 10. In Figure 9, the reciprocal of the
mass fraction is plotted along the non-dimensional
Figure 6. Mesh sensitivity analysis: contours of the Mach number , NPR 10: (a) Mesh with 3000 cells: jet structure is not well
solved, since flow is still supersonic after the Mach disk. (b) Mesh with 5000 cells: a better reconstruction of the Mach disk can be
observed, but the other major jet features are not well defined. (c) Mesh with 70,000 cells and (d) mesh with 130,000 cells: the
barrel shock, Mach disk and reflected shocks are properly resolved.
Figure 7. Mesh sensitivity analysis: axial distribution of the H 2
mass fraction for different mesh densities, NPR 10. Coarser
meshes result in a quicker drop of the mass fraction.
Figure 8. Mesh sensitivity analysis: radial distribution of the H 2 mass fraction at different axial distances from the nozzle exit plane:
(a) 5 mm, (b) 15 mm, and (c) 25 mm, NPR 10.
Anaclerio et al. 3347

<!-- PDF_PAGE: 7 -->

axial position (being req the equivalent circular section
radius). As it can be observed, a good agreement is
found between the experimental and numerical values,
as the experimental trend is well captured by the
simulations.
In Figure 10 the results obtained by using the three
different equations of state are compared in terms of
Mach number evolution along the axis. The shock
position is fully comparable, while shock intensity is
slightly higher for the real-gas models, as also reported
by Bonelli et al.
47 The Redlich-Kwong model has been
adopted for the subsequent simulations, in which the
general higher nozzle pressure can require a more rea-
listic equation of state.
NPR variation
Once the correct numerical setup and the mesh resolu-
tion have been determined, steady RANS simulations
have been performed by keeping the inlet conditions
constant while varying the pressure outlet. In this way,
differences in the jet structure have been analyzed for
NPR values ranging from 2.5 to 60. As it will be dis-
cussed later, for ICE analyses RANS and URANS are
able to capture the main jet features at a specific NPR
with good accordance.
A shock diamond structure occurs when the
NPR \ 4, since the regular reflection of the incident
shock can take place along the axis. An example of the
diamond structure is reported in Figure 11(a), which
shows the Mach numbers contours for a NPR = 3. For
a4 \ NPR \ 7, the Mach disk forms and multiple
shock cells appear, as visible in Figure 11(b) for a
NPR = 5. When NPR . 7, the underexpanded jet is
characterized by a singular shock cell as discussed in the
previous paragraphs (see Figure 6). The axial position
of the first reflecting point ( L
RR) in the diamond struc-
ture is reported as a function of NPR in Figure 12. This
trend can be accurately approximated by the linear
function the authors propose here, being the coefficient
of determination (R
2) equal to 0.997:
LRR =0 :4549NPR /C0 0:6347 ð7Þ
The Mach disk diameter and height have been assessed
in the NPR range 5–60. These results are reported in
Tables 2 and 3. Mach disk diameters measured from
the numerical results have been compared to the values
determined by using equation (2), resulting in a maxi-
mum difference of about 21% at NPR 60. This can be
considered a satisfactory result when the high level of
uncertainty affecting the model for the disk diameter is
taken into account. Exploiting the numerical results, a
Figure 9. Comparison of the experimental data in Ruggles and
Ekoto,46 namely, the reciprocal of the H 2 axial mass fraction
relative to the jet discharged by the rectangular nozzle (NPR 10,
aspect ratio 8) and the numerical results plotted along the non-
dimensional axial position (being r
eq the equivalent-area circular
section radius). The experimental trend is well captured by the
proposed numerical setup.
Figure 10. Comparison among different equations of state:
ideal gas, Peng-Robinson, and Redlich-Kwong. This plot shows
the evolution of the Mach number along the jet axis, NPR 10.
The Mach disk position is the same for all the three models
(;2 mm), whereas shock intensity is higher for the real gas
models, according to the results presented in the literature.
47
Figure 11. Contours of the Mach number for two different levels of jet under-expansion conditions: (a) shock diamond structure,
NPR 3; (b) multiple shock cells structure, NPR 5.
3348 International J of Engine Research 24(8)

<!-- PDF_PAGE: 8 -->

better agreement is found replacing the constant value
0.36 in equation (2) with a function of NPR:
Ddisk=Dnozzle = ½3 /C1 10/C0 6NPR3 /C0 3 /C1 10/C0 4NPR2 +
+0 :0112NPR +0 :2734/C138
ﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ ﬃ
NPR /C0 3:9
p
ð8Þ
By this tuning, a maximum error of about 12% is found
at NPR 60. In Table 3, the Mach disk height resulting
from the CFD simulations is compared against the val-
ues computed using equation (1), for CH =0 :62. A
good agreement is found at the medium-low NPRs,
worsening at the higher NPRs. An opposite trend, not
reported for the sake of brevity, is found for C
H =0 :67.
This suggests that defining CH as a function of the
NPR, as shown in Figure 13, can be a better approach.
Results reported in Paragraph 7 will confirm the valid-
ity of this idea. Moreover, the C
H trend shown in
Figure 13 suggests the presence of an asymptotic value
of about 0.69. This result is coherent with the value of
0.67 suggested by Ashkenas and Sherman 38 in the range
15 \ NPR \ 17,000.
In Figure 14, the H 2 mass fraction and the turbulent
kinetic energy can be observed for NPRs equal to 5 and
20. Since the total conditions at the inlet are equal in
both cases, the H
2 jets are characterized by the same
chocked mass flow and the same momentum at the noz-
zle exit section. Consequently, the higher jet penetration
observed for the NPR equal to 20 can be attributed to
the higher rarefaction of the air in the discharging
chamber. Looking at the H
2 mass fraction distribution,
two zones are clearly distinguishable: the inner core,
dominated by the gas-dynamics phenomena, where the
flow is isolated from the ambient fluid, and the external
mixing layer, characterized by an intense mixing pro-
moted by turbulence, as confirmed by the turbulent
kinetic energy contours in Figure 14. The axial and
radial extents of both the zones increase with NPR.
T able 2. Mach disk diameter ( Ddisk) resulting from RANS
simulations and comparison with the correlation provided by
the literature (equation (2)).
NPR Disk diameter
CFD [mm]
Disk diameter from
equation (2) [mm]
Difference %
5 0.337 0.377 12.04
10 0.886 0.889 0.35
15 1.258 1.199 24.65
20 1.586 1.444 28.92
40 2.434 2.163 211.13
60 3.425 2.696 221.27
T able 3. Mach disk height ( Hdisk) resulting from RANS
simulations and comparison with the correlation provided by
the literature (equation (1), CH =0 :62).
NPR Disk height
CFD [mm]
Disk height from
equation (1) [mm]
(CH =0 :62)
Difference (%)
5 1.299 1.389 6.30
10 2.009 1.961 22.47
15 2.522 2.401 25.02
20 2.981 2.772 27.51
40 4.350 3.921 210.93
60 5.362 4.802 211.65
Figure 12. Axial position of the regular reflection as a function
of the NPR in the range of moderately underexpanded jets.
Numerical data are well approximated by a linear regression.
Figure 13. Evolution of the parameter C H which links the
Mach disk height and the exit nozzle diameter to the NPR (see
equation (1))
Figure 14. Contours of the H 2 mass fraction, Y H2 , and
turbulent kinetic energy, K, for two underexpanded flow
conditions: NPR 5 (top) and NPR 20 (bottom). The inner core
of the jet, where mixing does not occur, is characterized by
negligible levels of turbulent kinetic energy. Conversely, high
values of the turbulent kinetic energy are observed in the
external mixing layer .
Anaclerio et al. 3349

<!-- PDF_PAGE: 9 -->

This is shown in Figure 15 where L0:3 is plotted against
NPR. L0:3 is defined as the axial position where the H 2
mass fraction drops to 30%, which is roughly the end-
ing point of the mixing layer. Beyond this point, the far-
field zone of the jet starts. In this last zone of the jet, the
radial distribution of the major variables of the flow
(pressure, velocity) can be described by gaussian pro-
files, and self-similarity hypothesis is expected to be
valid.
29,48 For this specific set of simulations, with both
the discharging chamber temperature and the inlet total
temperature set to 300 K, the best regression curve for
the non-dimensional L
0:3=Dnozzle is the following:
L0:3=Dnozzle =8 :9096(NPR)0:4677 ð9Þ
T est case
In this paper, the evolution of a hydrogen jet through-
out the injection inside an ICE cylinder has been inves-
tigated. Data reported in Matthias et al.
30 have been
exploited to assess the NPR variation from the start of
injection (SOI) to the end. The research engine is
equipped with a 5-hole nozzle, with a single hole dia-
meter of 0.61 mm and an upstream hydrogen pressure
of 100 bar. Although the injection pressure is one-order
magnitude higher than the one used in the previous
analyses, it should be pointed out that the jet features
depend on the NPR rather than the injection pressure.
Using a turbocharger that is able to deliver up to
2.5 bar, and employing a compression ratio of 12.9,
Matthias et al.
30 have exceeded the DOE light duty effi-
ciency targets. A rotational speed of 1700 RPM has
been considered, with the optimum SOI 80 /C176before the
top dead center (BTDC) and the injection span of 50 /C176.
The optimum SOI has been determined in order to
maximize the engine efficiency while ensuring the for-
mation of a mixture that is able to burn in a stable
manner. The change in the static pressure during the
compression stroke has been computed under the
hypothesis of an isentropic transformation ( k =1 :4),
using the following equation:
p
pin
= Vin
V
/C18/C19 k
ð10Þ
where Vin is the volume at Bottom Dead Center (BDC)
and pin the pressure at the beginning of the compres-
sion stroke. This pressure has been set at 2.5 bar, which
means that fluid dynamics losses have not been taken
into account for the sake of simplicity. V has been cal-
culated as a function of the crank angle u by using the
following equation:
V=Vcyl
1
(r/C0 1) +
/C20
1
2 1+ 1
l/C0 cos(u)/C0 1
l
ﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ ﬃ
1/C0 l2 sin2 (u)
q/C18/C19 /C21 ð11Þ
being r the compression ratio, Vcyl the swept volume
and l the crank to connection rod length ratio, set
equal to 0.3. Figure 16(b) shows the static pressure rise
throughout the injection, starting from 6.15 bar up to
32.94 bar when the piston is at 30 /C176BTDC. Therefore,
as reported in Figure 16(a), the nozzle pressure ratio
progressively decreases from 16.24 to 2.97. As a conse-
quence, the hydrogen jet evolves from a very highly to
a moderately underexpanded state during the injection.
At 1700 RPM, the injection process lasts 4.9 ms, thus
Figure 15. Evolution of L0:3, that is the axial distance where
the H2 mass fraction is equal to 0.3, as a function of the NPR.
Figure 16. Depiction of the evolution of (a) NPR and (b) static pressure level that reigns inside the cylinder as a function of the
crank angle throughout the injection phase. ICE test case reported in Matthias et al. 30 The vertical line in (a) delimits the transition
between a jet structure featured by a Mach reflection and a structure characterized by the regular reflection of the barrel shock.
3350 International J of Engine Research 24(8)

<!-- PDF_PAGE: 10 -->

steady RANS simulations have been performed using
NPR values of [16.3, 12.7, 9.5, 6.7, 4.5, 2.3] which cor-
responds to injection times of [0, 1, 2, 3, 4.9] ms.
Results
The methodology discussed in the previous paragraphs,
both in terms of mesh and numerical setup, has been
employed to characterize the hydrogen jet for the test
case in Matthias et al.
30 The Mach disk features are
reported in the next subsection, together with the L0:3
parameter. Afterward, the influence of hysteresis and
discharging chamber temperature on the gas-dynamics
and H
2 distribution is discussed. In the last subsection,
a preliminary assessment of the jet-jet interaction is
shown for a fixed NPR while varying the number of
nozzles and their inter-axes.
One jet: Steady
In Table 4, the Mach disk height is reported along with
the percentage error with respect to the values com-
puted using equation (1), setting C
H equal to 0.62 as
suggested in Vuorinen et al. 15 In the last column, the
variable CH = CH(NPR) reported in Figure 13 has been
employed, achieving a better agreement with the
numerical results. Regarding the Mach disk diameter,
the same approach is used in Table 5, in which a closer
match with the numerical results is shown when equa-
tion (8) is employed instead of equation (2). The
improved prediction of the Mach disk features provided
by the new correlations, along with the mesh sensitivity
analysis reported in the previous paragraphs, can be
used to optimize the creation of a mesh refinement box
in the nearfield zone of the jet. Capturing the expansion
and shock phenomena leads to a better assessment of
the velocity field. As it can be observed from the trans-
port equation (3), a convective term depending on the
velocity field is present to calculate the mass fraction
distribution of the hydrogen. Consequently, the evolu-
tion of the air-fuel mixture can be correctly computed
only when the gas-dynamics phenomena are properly
solved. The high momentum of the jet during the injec-
tion makes the buoyancy effects negligible, as it can be
observed by computing the Froude number:
Fr = ueﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ
gDnozzle(r‘ /C0 re)=re
p ð12Þ
where ue and re are the hydrogen velocity and density at
the nozzle exit and r‘ the discharging ambient density.
Since the jet is choked throughout the injection, ue and
re are constant for all the cases, and consequently Fr
only depends on r‘ . As it can be observed in Table 6,
the Froude number is always higher than 1000, which is
the threshold under which buoyancy is not negligible.
Figure 17 compares the evolution of the L
0:3 para-
meter, projected over the cylinder axis, with the cham-
ber height variation during the whole injection process.
The two curves do not intersect, but their distance
reduces to less than 1 cm at the end of the injection.
T able 5. Mach disk diameter ( Ddisk) for the test case in Matthias
et al.30 Equation (8) provides a better prediction of the disk
diameter.
NPR Injection
time [ms]
Mach Disk
diameter
(CFD) [mm]
% error with
equation (2)
% error with
equation (8)
16.3 0 1.60 20.7 14.3
12.7 1 1.27 16.0 12.9
9.5 2 1.00 14.8 15.9
6.7 3 0.63 3.9 10.4
4.5 4 0.25 9.7 3.2
T able 6. Froude number throughout the injection process.
Buoyancy is negligible since Froude number is greater than 1000.
NPR Froude number
16.3 115,120
12.7 36,320
9.5 23,940
6.7 17,650
4.5 13,570
2.9 10,900
T able 4. Mach disk height (Hdisk) for the test case in Matthias
et al.30 Employing the variable CH in Figure 13, a better prediction
of the disk height is obtained.
NPR Injection
time [ms]
Mach Disk
height (CFD)
[mm]
% error
for CH = 0.62
in eq. 1
% error for
variable CH
in equation (1)
16.3 0 1.65 8.3 2.5
12.7 1 1.44 6.8 2.0
9.5 2 1.21 4.8 3.2
6.7 3 0.97 0.2 3.2
4.5 4 0.74 7.9 0.8
Figure 17. Axial projection of L0:3 versus cylinder height
throughout the injection process.
Anaclerio et al. 3351

<!-- PDF_PAGE: 11 -->

Consequently, piston head impingement is not negligi-
ble and confinement effects might be relevant on the
underexpanded jet.
One jet: Unsteady
Unsteady simulations have been performed starting
from the solution characterized by a NPR equal to
16.3, which corresponds to the start of injection. For
these simulations, a first-order implicit formulation has
been adopted for the temporal discretization. Keeping
the injection pressure constant, the discharging ambient
pressure has been progressively increased following the
profile in Figure 16(b). Consequently, the overall simu-
lated process lasts 4.9 ms, and a timestep of 10
/C0 6 s has
been adopted. Thirty iterations per timestep have been
set, ensuring at least a fourth orders drop for all resi-
duals. The aim of this step has been the analysis of the
differences between the steady and unsteady structure
of the underexpanded jet under ICE conditions.
Indeed, as reported in Gribben et al.,
49 Otobe et al., 50
and Irie et al. 51 a hysteretic behavior can be observed
in the jet structure when NPR changes with time. The
nature of this phenomenon has not been clarified, but
it is known that it affects the underexpanded structure
in two ways. Firstly, for a given NPR, position and dia-
meter of the Mach disk can show a marked difference
between the steady and the unsteady solution.
Secondly, hysteresis determines a mismatch in the
threshold NPR for which the regular reflection is
replaced by the Mach reflection. This difference arises
when comparing increasing and decreasing NPR his-
tories. Figure 18 shows the result of this analysis: no
particular discrepancies have been found regarding the
Mach disk position, since the maximum error is about
2%. In Irie et al.
51 higher differences, around 10%, are
reported. This can be explained by considering that this
kind of hysteresis depends on the NPR variation rate.
The results shown by Irie et al.
51 refer to a dimension-
less velocity d(NPR)=dt0 =0 :835, being t0 defined as:
t0 = ta1ﬃﬃ ﬃ
k
p
dexit
ð13Þ
The ICE injection process is characterized by a mean
NPR variation rate of about 0.0015, hence almost 500
times slower. For this reason, the authors believe that
no differences can be visible between steady and
unsteady solutions at such a slow characteristic NPR
rate. Similarly, no differences are found when compar-
ing the H
2 mass fraction distributions, either in the
axial and radial direction. As an example, Figure 19
shows the radial distribution in the NPR 12.7 case at
10 and 20 mm from the nozzle exit plane. For all these
reasons, the authors state that the hydrogen jet evolu-
tion in ICE conditions can be captured by steady solu-
tions and vice-versa, given the low dimensionless
velocity of the injection process. Moreover, the validity
of the correlations previously provided regarding the
Mach disk features are still valid for ICE applications
and the correlations can be confidently used in the
mesh definition process. To complete the assessment of
the hysteresis, an unsteady simulation has been carried
out reversing the direction of travel in Figure 16(a).
Indeed, another kind of hysteresis exists, due to which
the threshold NPR of the regular to Mach reflection
Figure 18. Comparison of the Mach disk position between
steady and unsteady RANS simulations. For the characteristic
variation rate of the NPR inside the ICE cylinder, no differences
are observed regarding the Mach disk position.
Figure 19. Comparison of the H 2 mass fraction radial distribution between steady and unsteady solution for NPR = 12.7: (a) at
10 mm and (b) at 20 mm from nozzle exit plane. As for the Mach disk position, because of the low NPR variation rate (defined in
Matthias et al.
30), no remarkable differences are observed between the steady and unsteady solutions.
3352 International J of Engine Research 24(8)

<!-- PDF_PAGE: 12 -->

transition differs between increasing and decreasing
NPR.49,50 Although NPR does not increase during the
ICE injection, authors have considered interesting to
analyze this aspect too. For the decreasing profile of
Figure 16(a), the transition takes place when the NPR
is 4, while in the opposite direction it is visible for a
NPR equal to 3.5. Therefore, the hysteresis associated
to the increasing and decreasing NPR does not seem to
be dependent on the NPR variation rate, in accordance
with Gribben et al.
49and Otobe et al. 50 where no effects
of the variation rate have been reported.
One jet: External temperature impact
Inside an internal combustion engine, the injection
takes place while the piston moves from the BDC to
the TDC, causing not only a pressure rise but an
increase of temperature as well. To assess this effect,
RANS simulations have been performed by varying the
discharging chamber temperature according to its evo-
lution inside the combustion chamber. Numerically,
this analysis has required the switch of the ambient ver-
tical line (see Figure 3(a)) from the wall condition to a
velocity inlet condition. By doing so, it has been possi-
ble to impose different temperatures to the hydrogen
jet and the discharging chamber. Air velocity at the
boundary has been set equal to 0.01 m/s in order to
consider the discharging ambient almost steady. The
temperature evolution during the compression stroke
has been computed using the hypothesis of isentropic
transformation:
T = Tin
p
pin
/C18/C19 k/C0 1
k
ð14Þ
being Tin the temperature at the beginning of the com-
pression stroke. Dealing with a turbocharged engine,
Tin has been roughly considered equal to the exit tem-
perature from the intercooler Tec, assessed as follows:
Tec = Tamb + Tamb
hc
pc
pamb
/C18/C19 k/C0 1
k
/C0 1
"#
/C0 DT ð15Þ
where hc is the isentropic efficiency of the compressor
(supposed equal to 0.86) and DT is the temperature
drop imposed by the intercooler, supposed equal to
50 K. Figure 20 shows the temperature contour for the
case with a NPR equal to 12.7 (1 ms after SOI). An
ambient temperature equal to 491 K has been com-
puted using the previous equations, while the hydrogen
temperature in the tank is still 300 K. In the expansion
zone of the jet, just downstream of the nozzle exit sec-
tion, a significant temperature drop can be observed,
with a minimum of about 70 K before the Mach disk.
Through this shock, the temperature rises up to 290 K.
Surrounding the inner core, a layer where temperature
is around 300 K can be observed, mainly made up of
air cooled by the proximity to the hydrogen jet.
Figure 21 shows the H
2 radial distributions at 3-15-
30 mm from the nozzle exit plane for the cases with the
ambient temperature set at 300 K and 491 K. In all the
plots the higher temperature determines an intensified
diffusion of the hydrogen, particularly far away from
the nozzle exit plane, where jet momentum decreases
and thermal diffusion becomes more relevant (equation
(4)). At 3 mm from the exit, the maximum difference is
about 20%, while at 15 and 30 mm both the percentage
difference profiles show an almost linear increase of up
to 30%–40%, followed by a marked change of the slope
at about 1.8 and 4.2 mm along the radial direction,
respectively. At such radial positions, this trend is due
to the hydrogen diffusion toward zones where almost
only air can be found in the 300 K case. Regarding the
gas-dynamics structure, a perfect match in the Mach
disk position can be observed between the two cases,
further confirming that the position only depends on
the NPR.
Jet-jet interaction
In the studies developed at Argonne National
Laboratories,30,52,53 several injectors have been tested
to evaluate the air-hydrogen mixing and the charge
Figure 21. Impact of the different air temperature in the ICE cylinder (300 vs 491 K): H 2 mass fraction value (light blue) and
percentage difference (orange) in the radial direction at (a) 3 mm, (b) 15 mm, and (c) 30 mm from the nozzle exit plane.
Figure 20. Contours of the static temperature, NPR 12.7. Air
temperature in the ICE cylinder is fixed equal to 491 K.
Anaclerio et al. 3353

<!-- PDF_PAGE: 13 -->

stratification. Comparisons have been performed
between single and multi-hole injectors, the latter being
able to provide a more uniform distribution inside the
combustion chamber. Nonetheless, attention must be
paid to the jet-jet interaction when increasing the num-
ber of holes. Because of this phenomenon, hydrogen
jets divert from their nominal axes, showing the ten-
dency to mutually get closer. If the number of jets is
considerably high
52 they can collapse into a single jet.
Jet-jet interaction is crucial in the hydrogen distribution
process, influencing the interaction with walls, piston
head and the charge motion. For instance, in Otobe
et al.,
40 a 4-hole injector has been compared against a
5-hole configuration, characterized by the addition of a
central jet. When employing the 4-hole injector, the
absence of the central jet resulted in a less significant
jet-jet interaction, contributing to delay the SOI of 10 /C176
with respect to the 5-hole configuration and eventually
gaining higher engine efficiencies. This example points
out the need to take into account the jet-jet interaction
as it pertains to identify the most suitable nozzle con-
figuration. Counter-intuitively, a higher number of
holes does not automatically leads to a better fuel
distribution and better engine performance. Several
studies can be found in the literature regarding the jet-
jet interaction for carbon fossil fuels,
54–56 analyzing the
dependence on the NPR, fuel/ambient temperatures
and superheat level. The reason of the jet-jet interaction
is attributed to the formation of low-pressure regions
among the jets. Not a fully agreement is found in the
literature about the origin of these zones. Heldmann
et al.
54 has proposed the air-entraining effect as the rea-
son of the low-pressure field. More recently, Hengjie
Guo et al. 55 has attributed the low-pressure field to the
expansion waves propagation from the primary cells of
the underexpanded jets toward the inter-axes region.
To the authors’ knowledge, no studies are reported in
the literature to quantify the hydrogen jets deviation as
a function of the holes distance, angle or momentum.
For this reason, a preliminary assessment of the jet-jet
interaction is reported in this paragraph employing
hydrogen parallel jets as a reference for future investi-
gations. A more detailed analysis about the major vari-
ables influencing the phenomenon is indeed planned in
a short future. In this stage, RANS simulations have
been performed in a 3D domain. The NPR has been
set equal to 10 and 4 configurations have been ana-
lyzed: two and three parallel jets with inter-axis of 1
and 2 mm.
As seen in Figure 22, jet-jet interaction is clearly visi-
ble in the cases with 1 mm inter-axis, while it does not
seem to be present for the 2 mm cases. A marked drift
from the nominal axis is visible just downstream of the
Mach disks. This is better seen in the velocity vector
field reported in Figure 23. In this figure, the mean
velocity angle with respect to the axis has been found
to be equal to 12.5 /C176. Figure 24 shows a comparison of
the radial velocity between the 1 and 2 mm configura-
tions. The abscissa coordinates have been normalized
so that 0 indicates the jet axis while 1 indicates the
Figure 22. Contours of the Mach number: (a) two jets with inter-axis 2 mm, (b) three jets with inter-axis 2 mm, (c) two jets with
inter-axis 1 mm (d) three jets with inter-axis 1 mm. (a and b) do not show interactions between the jets, while (c and d) point out
the development of mutual interaction with a clear deviation of the jets.
Figure 23. Velocity field in the two jets with inter-axis 1 mm
case. Downstream of the Mach disk, flow deflection is about
12.5/C176with respect to the axial direction.
3354 International J of Engine Research 24(8)

<!-- PDF_PAGE: 14 -->

symmetry axis. As it can be seen, the radial velocity at
the 1 mm case jet axis is negative, indicating a flow dis-
tortion toward the symmetry line, whilst in the 2 mm a
radial velocity near to zero is found. Figure 25 reports
the H
2 mass fraction for the four cases: the collapse is
once again clearly visible for the 1 mm inter-axis cases.
Moreover, in Figure 26 the L
0:3 parameter measured
along the domain axis has been reported for the cases
analyzed. As it can be observed, higher values of L0:3
have been found when jet-jet interaction occurs, which
might be justified by the less intense radial dispersion
of the H 2.
To establish the origin of the jet-jet interaction,
the pressure field has been reported in Figure 27 for
the 2-nozzle with 1 mm inter-axis configuration,
while Figure 28 compares the pressure trend along
the symmetry line of the domain with the 2-nozzle
with 2 mm inter-axis case. It is possible to observe
that pressure is constant in the 2 mm case and it is
equal to the discharging chamber pressure. In the
1 mm case, an initial pressure increase up to 150 kPa
is visible, which is due to the squeezing effect caused
by the radial expansion of the supersonic zones of
the jets. Downstream of th is region, pressure drops
below the discharging chamber pressure, reaching a
minimum of 39 kPa. According to Guo et al.
55 this
drop is due to the propagation of the expansion
waves from the core of the jets toward the symmetry
line. The low-pressure region which is responsible
for the jets deflection is delimited by a secondary
Mach disk. This is caused by a reflection of the com-
pression waves headed toward the domain axis. The
latter can be observed in Figure 27.
Conclusions
In this paper, H 2 underexpanded jets have been exam-
ined by means of RANS and URANS simulations.
Differing from the majority of the current literature,
focus has been placed on the effect of ICE conditions
on the jet structure and H
2 distribution. In particular:
/C15 The correct numerical setup to get reliable results
has been determined. The proposed mesh sensi-
tivity analysis is a valuable tool to define the opti-
mum cell size, especially for full-cycle ICE
simulations.
/C15 The correlations provided by the literature to
assess the Mach disk features have been improved.
Most of the authors propose constant values for
C
H and CD, while in this work new correlations
depending on NPR have been proposed.
Therefore, the extension of the mesh refinement
Figure 24. Representation of the radial velocity for the cases:
two jets with inter-axis 2 mm (squares) and two jets with inter-
axis 1 mm (circles). In the first case, as no interactions occur
between the jets, radial velocity at the jet axis is equal to zero.
In the 1 mm inter-axis case, a radial component of ;50 m/s is
observed, indicating the onset of the jet-jet interaction.
Figure 25. Contours of the H 2 mass fraction: (a) two jets with inter-axis 2 mm, (b) three jets with inter-axis 2 mm, (c) two jets
with inter-axis 1 mm, and (d) three jets with inter-axis 1 mm.
Anaclerio et al. 3355

<!-- PDF_PAGE: 15 -->

downstream of the nozzle can be defined more
accurately.
/C15 The axial position where the H 2 mass fraction
drops to 30%, L0:3, has been introduced as a
parameter to determine the distance where the
farfield zone begins. A deeper analysis of this
parameter might be carried out in a future work,
with the aim to develop a new notional nozzle
approach for safety assessment. Moreover, for
moderately underexpanded jets (2 \ NPR \ 4),
a correlation to determine the first reflection
point has been provided. To the authors’ knowl-
edge such data are not available in the literature.
/C15 The dynamic behavior of the jet has been exam-
ined. Due to the NPR variation rate inside the
combustion chamber, no hysteretic phenomena
have been registered regarding both the Mach
disk position and the hydrogen distribution.
Therefore, in ICE analyses, jet features at a speci-
fied crank angle (i.e. at a specified NPR) can be
directly examined by means of a steady simula-
tion, avoiding the analysis of the whole injection.
/C15 The gas-dynamics features of the jet, such as the
Mach disk height, are not dependent on the ambi-
ent temperature. Conversely, an enhanced H
2 dif-
fusion is observed at higher temperatures, due to
the Soret effect. The phenomenon is more evident
far away from the nozzle exit, as the flow momen-
tum diminishes.
/C15 A preliminary assessment of the jet-jet interaction
has been carried out, showing the dependency of
this effect on the distance between the axes of the
nozzles rather than the number of jets involved.
The expansion waves propagating from the nozzle
exit planes toward the inter-jets region are deemed
to be the trigger of the interaction. The intent of
the authors is to further analyze this topic, since it
significantly influences the mixture formation
inside the combustion chamber and it must be
taken into account for injector optimizations.
Declaration of conflicting interests
The author(s) declared no potential conflicts of interest with
respect to the research, authorship, and/or publication of this
article.
Funding
The author(s) disclosed receipt of the following financial sup-
port for the research, authorship, and/or publication of this
article: This project has received funding from the MIUR
under the programme PON AIM (2014-2020 AIM-1883385
CUPD94I18000180007). This project has received funding
from the MIUR under the programme PON 2014-2020
(CUPD95F21002310006).
ORCID iD
Giuseppe Anaclerio https://orcid.org/0000-0003-2637-4302
References
1. Gahleitner G. Hydrogen from renewable electricity: an
international review of power-to-gas pilot plants for sta-
tionary applications. Int J Hydrogen Energy 2013; 38:
2039–2061.
2. Koch J, Schu ¨rch C, Wright YM and Boulouchos K.
Reactive computational fluid dynamics modelling of
Figure 27. Contours of the static pressure between the
nozzles for the two jets with inter-axis 1 mm case. Secondary
Mach disk is observed along the domain axis, as a result of the
interaction between the reflected shocks.
Figure 28. Static pressure along the domain axis in the two-
jets configurations. Jet-jet interaction does not occur in the
2 mm inter-axis case, and pressure is constant. In the 1 mm case,
interaction is observed. Along the inter-axis, pressure initially
increases due to the squeezing effect produced by the radial
expansion of the jets. After, a marked drop takes place. It is
caused by the expansion waves propagating toward the inter-
axis region, leading to the jet-jet interaction.
Figure 26. Comparison of the L0:3 measured along the domain
axis in the four configurations examined.L0:3 is higher when jet-jet
interaction occurs, indicating a lower radial diffusion of the H2.
3356 International J of Engine Research 24(8)

<!-- PDF_PAGE: 16 -->

methane–hydrogen admixtures in internal combustion
engines: Part I – RANS. Int. J. Engine Res 2021; 22:
1525–1539.
3. Capurso T, Stefanizzi M, Torresi M and Camporeale
SM. Perspective of the role of hydrogen in the 21st cen-
tury energy transition. Energy Convers Manag 2022; 251:
114898.
4. Yip HL, Srna A, Yuen ACY, et al. A review of hydrogen
direct injection for internal combustion engines: towards
carbon-free combustion. Appl Sci 2019; 9(22): 4842.
5. Sanguk L, Gyeonggon K and Choongsik B. Effect of
injection and ignition timing on a hydrogen-lean strati-
fied charge combustion engine. International Journal of
Engine Research 2022; 23(5): 816–829.
6. Wallner T, Matthias NS, Scarcelli R and Kwon JC. Eva-
luation of the efficiency and the drive cycle emissions for
a hydrogen direct-injection engine. Proc IMechE, Part
D: Journal of Automobile Engineering 2013; 227(1): 99–
109.
7. Wimmer A, Wallner T, Ringler J and Gerbig F. H2-
direct injection – a highly promising combustion concept .
SAE technical paper 2005-01-0108, 2005.
8. Scarcelli R, Wallner T, Salazar VM and Kaiser SA.
Modeling and experiments on mixture formation in a
hydrogen direct-injection research engine. SAE Int J
Engines 2009; 2(2): 530–541.
9. Wallner T, Scarcelli R, Nande AM and Naber J. Assess-
ment of multiple injection strategies in a direct-injection
hydrogen research engine. SAE Int J Engines 2009; 2(1):
1701–1709.
10. Yamane K. Hydrogen fueled ICE, successfully overcoming
challenges through high pressure direct injection technolo-
gies: 40 Years of Japanese Hydrogen ICE research and
development. SAE technical paper 2018-01-1145, 2018.
11. Boynton FP. Highly underexpanded jet structure - exact
and approximate calculations. AIAA J 1967; 5(9):
1703–1704.
12. Abbett M. Mach disk in underexpanded exhaust plumes.
AIAA J 1971; 9(3): 512–514.
13. Banholzer M, Vera-Tudela W, Traxinger C, Pfitzner M,
Wright Y and Boulouchos K. Numerical investigation of
the flow characteristics of underexpanded methane jets.
Phys. Fluids 2019; 31(5): 056105.
14. White TR and Milton BE. Shock wave calibration of
under-expanded natural gas fuel jets. Shock Waves 2008;
18: 353–364.
15. Vuorinen V, Yu J, Tirunagari S, et al. Large-eddy simu-
lation of highly underexpanded transient gas jets. Phys
Fluids 2013; 25: 016101.
16. Rajakuperan E and Ramaswamy M. Computation of the
near field structure of underexpanded jets from elliptic
sonic nozzle. CFD Journal 1977; 6(2): 79–101.
17. Menon N and Skews BW. 3-D shock structure in under-
expanded supersonic jets from elliptical and rectangular
exits. Twenty-fourth International Symposium on Shock
Waves, 2004. DOI: 10.1007/978-3-540-27009-6 79.
18. Chauhan V, Aravindh Kumar SM and Rathakrishnan E.
Aspect ratio effect on elliptical sonic jet mixing. Aeronaut.
J 2016; 120(1230): 1197–1214.
19. Anaclerio G, Capurso T, Torresi M and Camporeale
SM. Numerical characterization of hydrogen under-
expanded jets: influence of the nozzle cross-section shape .
ATI Congress 2022. DOI: 10.1088/1742-6596/2385/1/
012046
20. Rao SP and Abdol-Hamid KS. Numerical simulation of
jet aerodynamics using the three-dimensional Navier-
Stokes code PAB3D . NASA technical paper; Paper no.
3596.
21. Menon N and Skews BW. Shock wave configurations
and flow structures in non-axisymmetric underexpanded
sonic jets. Shock Waves 2010; 20: 175–190.
22. Trentacoste N and Sforza P. Further experimental results
for three-dimensional free jets. AIAA J 1967; 5(5):
885–891.
23. Sfeir AA. The velocity and temperature fields of rectan-
gular jets. Int J Heat Mass Transf 1976; 19(11): 1289–
1297.
24. Krothapalli A, Baganoff D and Karamcheti K. On the
mixing of a rectangular jet. J Fluid Mech 1981; 107:
201–220.
25. Zaman KBMQ. Axis switching and spreading of an
asymmetric jet: the role of coherent structure dynamics.
J Fluid Mech 1996; 316: 1–27.
26. Hamzehloo A and Aleiferis PG. Gas dynamics and flow
characteristics of highly turbulent under-expanded hydro-
gen and methane jets under various nozzle pressure ratios
and ambient pressures. Int J Hydrogen Energy 2016;
41(15): 6544–6566.
27. Yang F, Wang T, Deng X, et al. Review on hydrogen
safety issues: incident statistics, hydrogen diffusion, and
detonation process. Int J Hydrogen Energy 2021; 46(61):
31467–31488.
28. Xu BP, Zhang JP, Wen JX, Dembele S and Karwatzki J.
Numerical study of a highly under-expanded hydrogen jet .
In: International conference of hydrogen safety, Pisa, Italy,
8–10 September 2005.
29. Franquet E, Perrier V, Gibout S and Bruel P. Free under-
expanded jets in a quiescent medium: a review. Prog
Aerosp Sci 2015; 77: 25–53.
30. Matthias NS, Wallner T and Scarcelli R. A hydrogen
direct injection engine concept that exceeds U.S. DOE
light-duty efficiency targets. SAE Int J Engines 2012; 5(3):
838–849.
31. Donaldson CD and Snedeker RS. A study of free jet
impingement. Part 1. Mean properties of free and imping-
ing jets. J Fluid Mech 1971; 45(2): 281–319.
32. Shapiro AH. The dynamics and thermodynamics of com-
pressible fluid flow. New York: John Wiley & Sons, 1953.
33. Adamson TC and Nicholls JA. On the structure of jets
from highly underexpanded nozzles into still air. J Aerosp
Sci 1959; 26(1): 16–24.
34. Crist S, Glass DR and Sherman PM. Study of the highly
underexpanded sonic jet. AIAA J 1966; 4(1): 68–71.
35. Finat’ev YP, Shcherbakov LA and Gorskaya NM. Mach
number distribution over the axis of supersonic underex-
panded jets. J Eng Phys 1968; 15: 1153–1157.
36. Lewis CH and Carlson DJ. Normal shock location in
underexpanded gas and gas-particle jets. AIAA J 1964;
2(4): 776–777.
37. Love ES, Grigsby CE, Lee LP and Woodling JM. Experi-
mental and theoretical studies of axisymmetric free jets.
NASA Technical Report, NASA-TR-R-6, 1959.
38. Ashkenas H and Sherman FS. Structure and utilization
of supersonic free jets in low density wind tunnels. NASA
technical report, NASA-CR-60423, 1965.
39. Velikorodny A and Kudriakov S. Numerical study of the
near-field of highly underexpanded turbulent gas jets. Int
J Hydrogen Energy 2012; 37: 17390–17399.
Anaclerio et al. 3357

<!-- PDF_PAGE: 17 -->

40. Otobe Y, Kashimura H, Matsuo S, Setoguchi T and Kim
HD. Influence of nozzle geometry on the near-field struc-
ture of a highly underexpanded sonic jet. J Fluid Struct
2008; 24(2): 281–293.
41. Aleshin AP, Denisov IN, Rogachev NM and Sivirkin VF.
Effect of the cone angle and the degree of contraction of a
sonic nozzle on the geometrical structure of the first roll of
an underexpanded jet. JE n gP h y s1975; 28: 207–210.
42. Hamzehloo A and Aleiferis P. Computational study of
hydrogen direct injection for internal combustion engines.
SAE technical report 2013-01-2524, 2013.
43. Hecht ES, Li X and Ekoto IW. Validated equivalent
source model for an underexpanded hydrogen jet.
SAND2015-3211C.
44. Grcar JF, Bell JB and Day MS. The Soret effect in natu-
rally propagating, premixed, lean, hydrogen–air flames.
Proc Combust Inst 2009; 32: 1173–1180.
45. Sakellarakis V, Vera-Tudela W, Doll U, Ebi D, Wright Y
and Boulouchos K. The effect of high-pressure injection
variations on the mixing state of underexpanded methane
jets. Int J Engine Res 2021; 22(9): 2900–2918.
46. Ruggles AJ and Ekoto IW. Experimental investigation of
nozzle aspect ratio effects on underexpanded hydrogen
jet release characteristics. Int. J. Hydrogen Energy 2014;
39(35): 20331–20338.
47. Bonelli F, Viggiano A and Magi V. A numerical analysis
of hydrogen underexpanded jets under Real gas Assump-
tion. J Fluid Eng 2013; 135(12): 121101.
48. Belan M, De Ponte S and Tordella D. Determination of
density and concentration from fluorescent images of a
gas flow. Exp Fluids 2008; 45: 501–511.
49. Gribben BJ, Badcock KJ and Richards BE. Numerical
study of shock-reflection hysteresis in an underexpanded
jet. AIAA J 2000; 38(2): 275–283.
50. Otobe Y, Yasunobu T, Kashimura H, Matsuo S, Setogu-
chi T and Kim HD. Hysteretic phenomenon of underex-
panded moist air jet. AIAA J 2009; 47(12): 2792–2799.
51. Irie T, Yasunobu T, Kashimura H and Setoguchi T.
Characteristics of the mach disk in the underexpanded jet
in which the back pressure continuously changes with
time. J Therm Sci 2003; 12(2): 132–137.
52. Salazar VM and Kaiser SA. An optical study of mixture
preparation in a hydrogen-fueled engine with direct injec-
tion using different nozzle designs. SAE Int J Engines
2010; 2(2): 119–131.
53. Wallner T, Matthias NS and Scarcelli R. Influence of
injection strategy in a high-efficiency hydrogen direct
injection engine. SAE Int J Fuel Lubricants 2012; 5(1):
289–300.
54. Heldmann M, Bornschlegel S and Wensing M. Investiga-
tion of jet-to-jet interaction in sprays for DISI engines .
SAE technical paper 2015-01-1899, 2015.
55. Guo H, Li Y, Xu H, Shuai S and Zhang H. Interaction
between under-expanded flashing jets: a numerical study.
Int J Heat Mass Transf 2019; 137: 990–1000.
56. Moustafa GH. Experimental investigation of high-speed
twin jets. AIAA J 1994; 32(11): 2320–2322.
Appendix A
The Redlich–Kwong and Peng–Robinson equations are
both cubic models, whose general form is:
p = RT
v /C0 b + c /C0 a
v2 + vd + e ð16Þ
being a, b, c, d, and e constants related to the fluid criti-
cal pressure pc, critical temperature Tc, and acentric fac-
tor v. In the Redlich–Kwong model these constants are
computed as follows:
a(T)= a0
(T=Tc)0:5
a0 = 0:42747R2Tc2
pc
b = 0:08664RTc
pc
while d is equal to b and both c and e are set to zero.
For the Peng-Robinson model, the following equations
are solved:
a(T)= a0½1+ n(1 /C0 (T=Tc)0:5/C138 2
n =0 :4 8+1 :574v /C0 0:176v2
a0 = 0:45724R2Tc2
pc
v =/C0 log10
pv
pc
/C0 1
b = 0:07780RTc
pc
In the definition of the acentric factor v, computed for
T =0 :7Tc, pv is the saturation vapor pressure.
3358 International J of Engine Research 24(8)
