<!-- PDF_PAGE: 1 -->

Citation: Duronio, F.; Villante, C.;
De Vita, A. Under-Expanded Jets in
Advanced Propulsion Systems—A
Review of Latest Theoretical and
Experimental Research Activities.
Energies 2023, 16, 6471. https://
doi.org/10.3390/en16186471
Academic Editors: Vasily Novozhilov
and Cunlu Zhao
Received: 29 July 2023
Revised: 27 August 2023
Accepted: 4 September 2023
Published: 7 September 2023
Copyright: © 2023 by the authors.
Licensee MDPI, Basel, Switzerland.
This article is an open access article
distributed under the terms and
conditions of the Creative Commons
Attribution (CC BY) license (https://
creativecommons.org/licenses/by/
4.0/).
energies
Review
Under-Expanded Jets in Advanced Propulsion
Systems—A Review of Latest Theoretical and Experimental
Research Activities
Francesco Duronio 1
 , Carlo Villante 1,*
 and Angelo De Vita 1,2
1 Department of Industrial Engineering, Information and Economics, Università degli Studi dell’Aquila,
Piazzale Ernesto Pontieri, Monteluco di Roio, 67100 L’Aquila, Italy; francesco.duronio@univaq.it (F.D.);
angelo.devita@univaq.it (A.D.V .)
2 Consiglio Nazionale delle Ricerche, Istituto di Scienze e Tecnologie per l’Energia e la Mobilità Sostenibili
(STEMS), Via G. Marconi 4, 80125 Napoli, Italy
* Correspondence: carlo.villante@univaq.it; Tel.: +39-0862434302
Abstract: The current ongoing rise in environmental pollution is leading research efforts toward
the adoption of propulsion systems powered by gaseous fuels like hydrogen, methane, e-fuels,
etc. Although gaseous fuels have been used in several types of propulsion systems, there are still
many aspects that can be improved and require further study. For this reason, we considered it
important to provide a review of the latest research topics, with a particular focus on the injection
process. In advanced engine systems, fuel supply is achieved via enhanced direct injection into the
combustion chamber. The latter involves the presence of under-expanded jets. Under-expanded
jets are a particular kind of compressible ﬂow. For this reason, the review initially provides a brief
physical explanation of them. Next, experimental and numerical CFD investigation techniques
are discussed. The last section of this manuscript presents an analysis of the jet’s structure. The
injection parameters commonly used are examined; next, the characteristics of the near-nozzle ﬁeld
are reviewed and ﬁnally, the far-ﬁeld turbulent mixing, which strongly affects the air–fuel mixture
formation process, is discussed.
Keywords: under-expanded; CFD; compressible ﬂow; supersonic ﬂow; gaseous injection
1. Introduction
One of the essential actions for mitigating current climate change risks is to signiﬁ-
cantly reduce transport sector emissions [1–4]. As a consequence, over the last few years, an
increasing number of researchers have focused on the development of advanced propulsion
systems [5]. In particular, powering Internal Combustion engines (ICEs) with gaseous or
strong evaporative fuels (like hydrogen, propane or methane gas) may be introduced in the
near future and also maintained for a longer period (especially if equipping heavy-duty
long-range transport applications) to achieve the aforementioned goal [6]. Furthermore,
these fuels may also be completely renewable and/or have zero emissions on a WTW (well-
to-wheel) evaluation approach, therefore leading to zero-impact transportation solutions to
be compared with all those based on pure electric traction [7].
When using gaseous fuels, the injection process plays the most crucial role in deﬁning
ICE environmental performance, affecting mixture formation, its combustion, and, there-
fore, production of pollution. Moreover, in advanced ICEs, the fuel is Directly Injected
(DI) inside the cylinder, calling for more rapid, controlled and efﬁcient mixture formation
processes [8–10].
High-injection pressures are typically used for gaseous fuelling in order to achieve
the required mass ﬂow rates and promote air/fuel mixing [ 11–17], typically leading to the
formation of highly under-expanded jets (UEJ) at the injector outlet, when the fuel jet faces
surrounding airﬂow.
Energies 2023, 16, 6471. https://doi.org/10.3390/en16186471 https://www.mdpi.com/journal/energies

<!-- PDF_PAGE: 2 -->

Energies 2023, 16, 6471 2 of 21
Under-expanded jets are complex high-speed ﬂows, which are also formed in many
other engineering applications and devices such as exhaust aircraft plumes (rockets and
missiles), supersonic combustion chambers, actuators, etc. [ 18–20]. This type of jet can
also be observed in geophysical systems (volcanic eruption) and in the accidental release
of hazardous gases (such as hydrogen) from tiny cracks in high-pressure pipelines and
reservoirs [21–23]. For these reasons, under-expanded jets were historically investigated,
especially for aerospace applications. At the same time, there are a paucity of studies
examining their presence and inﬂuence in automotive advanced propulsion systems, being
a newer topic in ﬂuid-dynamic and engine-related research.
However, in recent years, following the great interest shown by political institutions in
fuels like hydrogen, a multitude of scientiﬁc studies were conducted [24–28]. The authors
propose that it could be important to provide researchers with a quick and, as far as possible,
complete reference guide to under-expanded jets in ICEs, highlighting the most interesting
topics and the most relevant works undertaken in recent years.
To this aim, this review paper ﬁrstly focuses on a brief physical and phenomenolog-
ical discussion of these complex ﬂows and then reports on the main literature results in
the sector, subsequently dividing them into two main sections concerning, respectively,
experimental and mathematical investigation methodologies usually adopted for studying
UEJ. Each cited research study will be introduced and brieﬂy discussed, highlighting the
most important outcomes from a ﬂuid-dynamic perspective and ﬁnal engine application.
2. Physics of Under-Expanded Jets
An under-expanded jet may appear when a high-pressure ﬂuid is connected through
a convergent or a convergent–divergent nozzle within an environment where much lower
pressure conditions are created. As well known, two possible scenarios can be identiﬁed
depending on the total pressure ratio between the inlet and outlet of the nozzle.
η0 = P0
P∞
(1)
Figures 1 and 2 report the pressure ratio and the mass ﬂow rate evolution as a function
of the axial distance for a convergent nozzle.
The ﬁrst regime depicts a subsonic ﬂow (cases a and b); the mass ﬂow increases as the
downstream pressure decreases, and the exit pressure is equal to the ambient one. Critical
conditions are reached if the upstream pressure increases and the nozzle is choked (cases c
and d). The outﬂow pressure is equal to the critical pressure ( P∗), and the mass ﬂow cannot
increase more; it is called indeed choked as reported in Figure 2.
Figure 1. Pressure evolution along nozzle axis for various pressure ratios.

<!-- PDF_PAGE: 3 -->

Energies 2023, 16, 6471 3 of 21
Figure 2. Mass ﬂow rate for various pressure ratios.
It follows that, an the exit section, the pressure is greater than the ambient one and to
achieve pressure equilibrium, under-expanded jets arise.
In choked conditions, the pressure waves cannot travel back upstream, and the mass
ﬂow rate is no longer dependent on downstream conditions ( ˙m∗). The ﬂow characteristics
inside the nozzle, in fact, only depend only on the upstream boundary conditions.
As represented in Figure 3, it is common practice to divide the jet into three zones [29]:
• the near-nozzle zone;
• the transition zone;
• the far-ﬁeld zone;
Figure 3. Under-expanded jet zones.

<!-- PDF_PAGE: 4 -->

Energies 2023, 16, 6471 4 of 21
The near-nozzle zone is split into two sections: the core and the mixing layer. In the
former, also called the gas-dynamic area, the ﬂow is separated from the environment, and
its behaviour is governed mostly by compressible effects and is rather steady. The ﬂuid
expands iso-entropically until it is re-compressed by shock waves.
In the mixing layer, turbulence causes an interaction between the injected ﬂuid and the
surrounding environment, which is characterized by huge turbulent structures (vortices)
that are formed within the ﬂuid ﬂow downstream of the nozzle outlet. A shearing zone
between the frontier of the potential core of the jet and the constant pressure line can
be distinguished.
Depending on the pressure ratio, different under-expanded jet conﬁgurations can be
observed in the near-nozzle zone:
• The jet is weakly under-expanded, a normal shock appears in the exit plane.
• The jet is moderately under-expanded and has a “diamond” or “X” structure, depicted
in Figure 4, 2 < η0 < 4 [30,31]. In the exit plane (marker A), a Prandtl–Meyer
expansion fan (marker C) expands the ﬂuid downstream of the device’s edges up to
the jet boundary that corresponds to the external surface of the mixing layer (marked
JB). The expansion waves are reﬂected as compression waves when they reach the
constant pressure streamline (marker D), where the pressure matches the ambient
pressure. They converge on the inner jet and merge to produce an oblique shock
(marker E), commonly referred to as the intercepting shock.
• The jet is highly under-expanded, 4 < η0 < 7 [32,33]. It has a “barrel” or “bottle”
structure, shown in Figure 5, Mach disc appears (due to a singular reﬂection). When
the pressure ratio grows, the regular reﬂection of the intercepting shock on the axis is
no longer possible. As a result, above the critical angle, this reﬂection becomes singular,
resulting in the appearance of a normal shock-denominated Mach disc (marker F). The
triple point is deﬁned as the intersection of the intercepting shock, the Mach disc and
the reﬂected shock (marker G). A slipstream (marker H) develops at this point: this is
an embedded shear layer that divides the ﬂow upstream of the Mach disc (subsonic)
from the ﬂow downstream of the reﬂected shock (supersonic).
• The jet is extremely (or very highly) under-expanded, η0 > 7 [34,35]. As depicted in
Figure 6, the structure is dominated by a unique barrel. In this case, the Mach disc is
no longer considered as a normal shock, and its curvature must be considered. Due
to the momentum exchange generated by the ambient ﬂuid’s entrainment, the jet’s
overall diameter will decrease, resulting in an extremely long plume.
Figure 4. Structure of a moderately under-expanded jet.

<!-- PDF_PAGE: 5 -->

Energies 2023, 16, 6471 5 of 21
Figure 5. Structure of a highly under-expanded jet.
Figure 6. Structure of a very highly under-expanded jet.
Nevertheless, the Mach disc is undoubtedly one of the most studied features of under-
expanded jets Moreover, there is still signiﬁcant ongoing discussion regarding the transition
from a regular reﬂection to a singular reﬂection, accompanied by the appearance of the
Mach disc. This phenomenon is currently quantitatively not well known, particularly the
dependence (and interactions) on pressure range and exit Mach number, ﬂuid characteris-
tics (i.e., the polytropic coefﬁcient), nozzle shape, and exit nozzle angle [36].
The Mach disc location is primarily governed by the pressure ratio, increases with
the Mach number and, among the many, a good estimation of the position is given by the
following relation:
Hd
D = 0.67√η0 (2)
with Hd Mach disc height, D outlet section diameter [34,36,37].

<!-- PDF_PAGE: 6 -->

Energies 2023, 16, 6471 6 of 21
The Mach disc width or diameter was clearly less investigated than the Mach disc
length. However, it appears that it is also mainly governed by the pressure ratio and
strongly dependent on the nozzle geometry and shape [38–40].
Towards the end of the near-nozzle zone, the sonic line reaches the axis, indicating
that the mixing layer has fully replaced the inner region. This marks the beginning of the
transition zone, where variations in variables, both longitudinally and radially, become
minimal. In this region, a more effective mixing of the two ﬂuids, the ejected ﬂuid and the
ambient ﬂuid, takes place. As a result, the pressure ﬁeld becomes more homogenized as
entrainment occurs throughout the transition zone.
In the far-ﬁeld zone, the jet exhibits self-similarity, but compressible effects may still
be present if the Mach number is above 0.3 and may even be supersonic. Qualitatively,
the normalized radial proﬁles of the mean variables follow the same pattern, typically
characterized by a Gaussian proﬁle.
3. Experimental Observation of Under-Expanded Jets
The observation of under-expanded jets can be performed both with quantitative
and qualitative techniques. Among the first category, schlieren and shadowgraph
imaging surely can be mentioned, adopted for capturing images of both near and far
field zones [13,41–43].
High-speed schlieren imaging is a robust diagnostic technique capable of visualiz-
ing optical in-homogeneities of transparent media, otherwise not visible to the human
eye [44–46]. The method is sensitive to changes in the refractive index of a light beam trav-
elling through a heterogeneous medium. For this reason, Schlieren diagnostic is frequently
adopted for the observation of compressible ﬂows, such as under-expanded jets, in which
the difference in refractive index is caused by the gradient of density between the injected
fuel and the ambient gas [44].
Figure 7 shows the schematic diagram of a typical experimental setup for schlieren imaging.
Figure 7. Experimental optical setup of schlieren technique with z-type conﬁguration (reproduced
with permission from Ref. [47]. Copyright 2020 SAE International).
The Schlieren light source is usually a high-power LED lamp. A series of lenses
and glasses modify the beam characteristics. The main difference between Schlieren
and shadowgraph is the presence of a knife-edge in the first case to regulate the
percent of light cutoff, obtaining the desired contrast for the Schlieren images. High-
speed cameras are adopted for recording images with frame rates of the order of
thousands of frames per second. Depending on the magnification system, different
spatial resolutions can be achieved.
The injection system usually consists of a pressurized fuel tank, a pressure trans-
ducer and a pressure regulator to ensure the desired value for the test conditions. The

<!-- PDF_PAGE: 7 -->

Energies 2023, 16, 6471 7 of 21
transistor–transistor logic (TTL) triggering signal produced by a pulse generator is used by
an Electronic Control Unit (ECU) to control the injection events and to guarantee proper
synchronization and delay between the injection and acquisition chain.
Under-expanded jets are almost always being observed in Constant Volume Cham-
bers (CVC), optically accessible through quartz windows with the injector fixed in a
customized holder.
The images recorded with these techniques provide a proﬁcient visualization of the
near ﬁeld zone, and so of the barrel shocks, the Mach discs, etc., as well as the overall spray
structure, allowing the evaluation of macroscopic parameters such as the Mach disc height,
width, the jet tip penetration, the jet angle, the volumetric growth, the tip speed, radial
expansion, etc. Figure 8 depicts some classical visualization of the under-expanded jets
obtained with schlieren imaging and regarding various jet’s characteristics [48].
Figure 8. Visualization of under-expanded jets by means of schlieren optical technique (reproduced
with permission from Ref. [48]. Copyright 2022 Elsevier).
These information are of relevant importance for verifying and validating CFD simu-
lation codes by comparison of the aforementioned parameters but, at the same time, do not
allow to evaluate microscopic features of the jet or give a quantitative estimation of local
fuel concentration, jet temperature or velocity. To obtain some of these information other
experimental techniques are required. They are Planar Laser-Induced Fluorescence (PLIF)
or Particle Image Velocimetry (PIV) [43,49–53].
The PIV technique is a non-intrusive diagnostic technique that allows the velocity
ﬁeld to be measured on a two-dimensional plane. The measurement principle is based on
determining the distance the tracer particles cover in a known time interval [54,55]. The
typical elements of a PIV system are a laser source (typically a pulsed Nd-YAG laser with a
wavelength of 532 nm), an optical system, a camera and a data acquisition system (DAQ).
The PLIF technique allows the measurement of the concentration of species and the
temperature in the ﬂow ﬁeld of a ﬂuid. It is based on the process of photon absorption–
emission, and therefore, on the phenomenon of natural ﬂuorescence of molecules and atoms.
Through the PLIF technique, it is possible to obtain visualization with high spatio-temporal
resolution. Although the instantaneous (temporally based) quantitative measurement
of the parameters of interest remains complex, it is still possible to obtain quantitative
measurements of concentration, temperature, pressure and speed based on an average of
consecutive sequences (time-averaged).

<!-- PDF_PAGE: 8 -->

Energies 2023, 16, 6471 8 of 21
Figure 9 depicts some results regarding the fuel concentration of under-expanded
jets [53].
Figure 9. Visualization of under-expanded jets by means of PLIF optical technique for different
Pinj /Pamb ratios (reproduced with permission from Ref. [53]. Copyright 2013 SAE International).
Table 1 summarizes the papers regarding experimental investigations of under-
expanded jets.
Table 1. Experimental Techniques Jets Summary Table.
Technique Measurement Zone Fuel NPR Reference
Schlieren
Developed Spray CH 4
Pinj = 300 bar
Pamb = 60, 12, 30 bar [56]
Developed Spray He NPR = 2, 3, 4, 5 [13]
Near-nozzle/
Mach Disc N2 NPR = 20 [57]
Developed Spray CH 4
NPR = 190, 220, 250,
280, 310 [43]
Developed Spray CH 4 NPR = 60, 11, 16, 21, 26 [41]
Developed Spray CH 4
Pinj = 10, 14, 18 bar
Pamb = 3, 5 bar [42]
PLIF
Near-nozzle/Mach Disc N 2 NPR = 10, 20, 30, 40 [50]
Developed Spray N 2 NPR = 10, 40 [53]
Developed Spray CH 4 NPR = 20, 60 [51]
PIV Developed Spray N 2 NPR = 20 [57]
Developed Spray Ar NPR = 12 [58]
4. CFD Simulation of Under-Expanded Jets
Computational ﬂuid dynamic codes (CFD) are undoubtedly the other powerful tool
broadly adopted to investigate under-expanded jets. The advantages of developing a
virtual model of this engineering problem are quite obvious not only to understand the

<!-- PDF_PAGE: 9 -->

Energies 2023, 16, 6471 9 of 21
underlying physics of these ﬂows but also with the perspective of the application to the
propulsion system.
This paragraph aims to illustrate, in a synthetic but also organized fashion, the main
characteristics of the CFD codes used by researchers to study the aforementioned problem.
Further than in-house developed codes, basically three ﬁnite volume CFD codes were
used. They are OpenFOAM, CONVERGE and STAR-CCM+ [ 59–61]. It should also be
mentioned that some studies use the Lattice Boltzmann method [62,63]. The following two
sub-sections report the main characteristics of the discretization schemes adopted and of
the turbulence modelling selected.
4.1. Discretization Schemes and Solution Algorithms
The simulation of under-expanded jets requires the adoption of high-order numer-
ical schemes able to describe flow-field discontinuities along with avoiding undesired
oscillations. High-order schemes are required both for spatial discretization and tem-
poral integration.
Methodologies, based on Riemann solvers, such as the Weighted Essentially Non-
Oscillatory schemes (WENO) or the Piecewise Parabolic Method (PPM), give the best
reproduction of compressible ﬂow but have relevant limitations. These approaches involve
characteristic decomposition and Jacobian evaluation, and so they were implemented
only for structured grids. The adaptive central-upwind sixth-order weighted essentially
non-oscillatory (WENO-CU6) scheme with low dissipation was used by Ren Z et al. [64] to
achieve a proper resolution of the ﬂow properties around the shock waves. Seventh-order
accurate weighted essentially non-oscillatory (WENO7) reconstruction of the characteristic
ﬂuxes was also adopted for simulating under-expanded jets. The shocks and discontinuities
can be resolved using highly accurate and low-dissipation hybrid ENO schemes with shock
detectors [65–67].
Contrarily, unstructured grids are far more ﬂexible than structured grids and can
easily discretize complex geometries [68–70]. One of the principal methods developed for
unstructured grids uses the so-called central schemes formulations of Kurganov (KNP) and
Kurganov and Tadmor (KT) [71,72]. These are non-staggered second-order central methods
that use the cell centres’ values to evaluate the cell faces’ ﬂuxes. The cell-to-face ﬂow
interpolation is divided into inward and outward directions with respect to the face owner
cell. An extensive and detailed description can be found in [68]. Considering the intrinsic
geometrical complexity of the injector’s nozzles, these schemes are broadly adopted for this
kind of simulation in union with ﬂux limiters of Minmod or of Van Leer to ensure stability
and convergence of the computation [68,73]. This discretization method, initially imple-
mented in OpenFOAM’s solver rhoCentralFoam , was exploited in various other solvers
purposely developed to study under-expanded jets [ 74–80]. Another proﬁcient scheme
used is the Advection Upstream Splitting Method (AUSM+-up). AUSM+-up is accurate
and reliable in solving ﬂuid ﬂows with any arbitrary range of velocities, but it excels
at high-velocity ﬂows with strong discontinuities like shock waves [ 81,82]. AUSM+-up
avoids explicit artiﬁcial dissipation by using a separate splitting for the pressure terms of
the governing equations; the mass ﬂux and pressure ﬂux are calculated on the basis of local
ﬂow characteristics (including the speed of sound) to ensure precise information propaga-
tion inside the ﬂuid for convective and acoustic processes [ 83]. This minimizes numerical
dissipation, especially in high-velocity ﬂows, and prevents wiggles at ﬂow discontinuities
like shocks.
The solution methods commonly used involve both explicit (density-based) [84–86]
and Pressure Implicit Split Operator (PISO) algorithms [ 56,87–90]. The density-based
approach proved to be the best choice for reproducing under-expanded jet features. Implicit
(or pressure-based) methods for solving ﬂuid-ﬂow governing equations were historically
employed for incompressible ﬂows and only recently adapted to account for compressible
ﬂows. However, as broadly demonstrated in the literature [ 84–86,89], the best choice in
terms of results accuracy is represented by explicit methods (or density-based). The reason

<!-- PDF_PAGE: 10 -->

Energies 2023, 16, 6471 10 of 21
for that is intrinsically contained in the algorithm procedure. The temporal integration is
usually performed using high-order schemes such as explicit Runge–Kutta 4th (RK4) [84].
Another relevant aspect of under-expanded jet simulation is the computation of the
thermo-physical properties for the species involved in the ﬂuid ﬂow. The equation of
state (EoS) (for a description of the pressure–volume–temperature (P-V-T) relationship) is
crucial to the accuracy of the solution. Further than the ideal-gas EoS, Cubic EoS such as
Soave–Redlich–Kwong (SRK) and Peng–Robinson (PR) were widely applied due to their
simplicity and reasonable accuracy [56,61,76,77,91–94].
4.2. Turbulence Modelling
The numerical solution of the ﬂuid-dynamic problem is valid when the computational
grid is ﬁne enough to resolve all the ﬂow scales [ 85]. This would be a Direct Numerical
Simulation (DNS) of the ﬂow, which is now unaffordable due to its complexity and re-
source demands. So, turbulence modelling techniques, such as Reynolds Averaged Navier
Stokes (RANS) or Large Eddy Simulation (LES), are preferred for under-expanded jet
simulations [78,85,86,95].
Among the many simulation approaches regarding under-expanded jets, just a few
use RANS, while most adopt LES models. The LES technique is based on modelling the
lower scales, which are universal and unaffected by ﬂow geometry, while explicitly solving
the larger ones. This is done by mathematically ﬁltering the governing equations and
introducing the Sub-Grid Stress (SGS) tensor (τsgs) [96]. The SGS term modelling involves
an eddy viscosity approximation. Various SGS closure models can be found in the literature.
In some cases, LES WALE model is used, both without wall functions or applying global
damping functions. The model produces an efﬁcient and fast-solving scheme due to its
algebraic formulation. This approach also showed some promising results in predicting the
transition from laminar to turbulent regimes [97].
The Yoshizawa model is another common choice. It is a one-equation eddy viscosity
model for compressible ﬂows [ 98,99], which is different from zero equation models such
as the Smagorisky model. It exploits a transport equation to compute the local SGS
kinetic energy ksgs. Then, the sub-grid scale eddy viscosity νsgs is calculated using the ksgs
ﬁeld and the ﬁlter dimension ∆ (usually evaluated from the grid size) according to the
following relation:
νsgs = Ck∆
√
ksgs (3)
where Ck is a model constant whose default value is 0.094.
The scale selective discretization (SSD) technique proposed by Vuorinen et al. relates
to the so-called implicit LES (ILES) modelling category [ 84,100–102]. However, unlike
ILES, the SSD approach targets the dissipative effects exclusively to the ﬂow’s smallest
scales via scale separation procedure. A Laplacian ﬁlter separates the scales by splitting
the convection term into low and high-frequency components for which centred and
upwind-biased techniques can be used individually.
Table 2 summarizes the papers regarding CFD simulations of under-expanded jets.
Table 2. CFD Simulations Summary Table.
Numerical Approach Code T urbulence Modeling Fuel Reference
WENO/ENO
In-house LES Air [65]
In-house LES Air [66]
In-house/Finite
Differences LES Reactive jet [67]
In-house LES H 2 [64]
AUSM STAR CCM+
LES WALE H 2 [60,82,89,103]
LES WALE N 2 [60,103]
LES WALE CH 4 [89,103]

<!-- PDF_PAGE: 11 -->

Energies 2023, 16, 6471 11 of 21
Table 2. Cont.
Numerical Approach Code T urbulence Modeling Fuel Reference
KNP/KT
OpenFOAM LES, RANS k- ω H2 [74,86]
OpenFOAM LES k-Eqn N 2 [77,86]
OpenFOAM LES k-Eqn CH 4 [47,75,104,105]
Bulk Viscosity Method OpenFOAM LES Scale Selective Method
N2 [53,85]
CH4 [84]
H2 [53]
Hybrid KNP/KT OpenFOAM LES CH 4 [56,106,107]
OpenFOAM LES, RANS H 2 [61,108]
MUSCL CONVERGE LES CH 4 [61,109]
Lattice Boltzmann In-house LES N.A. [62,63]
5. Jet Structure Analysis
Although we are considering pure experimental research or a CFD investigation, the
information provided can be classiﬁed and subdivided in the following paragraphs.
First of all, the main parameters of the injection process are reviewed and discussed;
then, the features of the Mach discs and, generally, of the near ﬁeld ﬂow are presented
accordingly with the outcomes of the works considered. Finally, the characterization of the
turbulent mixing zone and of the far-ﬁeld zone are discussed being of central importance
in propulsion systems applications.
5.1. Characteristics and Parameters of the Injection
The injectors investigated in the literature are mainly single-hole prototype de-
vices. These usually have round holes with a diameter of about 1 mm [ 41,60,78]. Some
other authors investigated hollow cone outwardly opening devices [ 52,88,109,110].
One of these is produced by Continental (Figure 10), and it was characterized both
numerically and experimentally.
Commercially available injectors were also modiﬁed to inject gaseous fuels generating
multi-hole patterned sprays [13,43,57].
Very few works were found concerning multi-hole injectors purposely designed for
gaseous injection. A 50 bar maximum injection pressure device with inter-changeable noz-
zles was investigated experimentally and numerically in a series of publications [104,105].
When working with gaseous injection, typically, Net Pressure Ratio (NPR), the ratio
between the injection and the environment pressure, is conveniently used as a reference
to classify the resulting jets, more so than using injection pressure. In particular, common
NPR values range from 4 to 5 to around 40–50 [42,43,104]. The ambient pressure is usually
kept equal to 1 bar. Some works explore injection pressures up to 200 bar [51].
Figure 10. Outwardly opening injector for gaseous injections (reproduced with permission from
Ref. [109]. Copyright 2020 The University of Queensland).

<!-- PDF_PAGE: 12 -->

Energies 2023, 16, 6471 12 of 21
In the investigation of under-expanded jets, the characteristics of the injected ﬂuid
play a very important role, strongly inﬂuencing resulting jet conditions. However, due
to security issues, experimental investigations are normally realized with inert gases like
N2, argon or helium [52,58,92,111]. Moreover, some papers examine methane or hydrogen
injections, the latter especially considering the latest interest in this fuel shown by many
research groups. From the perspective of potential application in propulsion systems,
testing inert gas is mainly used to validate and calibrate numerical CFD approaches, which
can afterwards be extended to ﬂammable ﬂuid injections and mixture formation processes.
5.2. Near Field—Mach Disc Features
The investigation of the near nozzle ﬂow ﬁeld of under-expanded jets is mainly
focused on Mach discs, barrel shocks or converging shocks that appear in this ﬂow just
downstream of the injector nozzle. Schlieren imaging is undoubtedly the most adopted
technique to record them. The pictures obtained are a powerful tool to validate the CFD
codes. Further than a visual comparison of the Schlieren measurements with the gradient
of the density ﬁeld computed with CFD, the Mach disc’s height and width represent
quantitative parameters that can be used for an actual comparison. An investigation using
the PLIF technique was instead performed by Yu et al. [50]. The following Figure 11 depicts
a comparison between LES simulation and PLIF visualization of the Mach disc issued from
a methane injection.
Figure 11. Mach disc: comparison of experimental PLIF images with LES CFD simulation (reproduced
with permission from Ref. [50]. Copyright 2013 Elsevier).
The computational requirements for under-expanded jets simulations are very high.
Grid sensitivity analysis performed by various authors demonstrated that to have a proﬁ-
cient representation of the near nozzle shocks mesh dimensions must be of the order of
D/20–D/50 or, in dimensional terms, of tens of micro-meter [84,85,89,103]. This, together
with the time step of the order of 10−8 s, requires relevant computational resources.
From a modelling point of view interesting comparisons between different CFD
codes (such as OpenFOAM, Star CCM+ and CONVERGE) were carried out by various
authors [61,112].
The equation of state was also investigated. Redwlich-Kwong and Peng-Robinson
real gas EoS give different conﬁgurations of under-expanded jets with respect to ideal
gas EoS especially when the jets are issued in critical conditions [ 106,107]. Other ﬂuid
properties, such as speciﬁc heat or viscosity are also objects of interest. Chung relation and
Chapman–Enskog theory were used for the viscosity while the Janaf pressure-corrected
relation for Cp and Cv [58,113].

<!-- PDF_PAGE: 13 -->

Energies 2023, 16, 6471 13 of 21
The effect of the NPR on the characteristics of the Mach disc is one of the most
investigated physical parameters demonstrating how, depending on the value assumed,
the jet conﬁguration signiﬁcantly changes. Figure 12 shows the different shock structures
obtainable accordingly with the net pressure ratio.
Figure 12. Mach discs: comparison of different pressure ratios. ( a1,a2) NPR = 5.60, ( b1,b2)
NPR = 7.47, (c1,c2) NPR = 9.34, and (d1,d2) NPR = 11.2 (reproduced with permission from Ref. [77].
Copyright 2016 American Institute of Aeronautics and Astronautics).
The effect of the fuel characteristics was also an important research topic treated by
Hamzehloo et al. comparing mach discs produced with hydrogen and methane [89,103].
The near-nozzle shock structure of the methane jet displayed a slightly different pattern
compared to the hydrogen jets. The methane jet exhibited intense expansion fans right
from the early stages of its formation, resulting in a normal shock that was wider than the
nozzle diameter and resembled a Mach disc. On the other hand, the hydrogen jets were
associated with a slim Mach disc. For methane, mixing occurs only downstream of the
Mach disc while, for hydrogen, high momentum exchange and mixing was observed at the
boundaries of the jet.
5.3. Far Field—Turbulent Mixing
Jet area, volumetric growth and tip penetration are the main parameters used to
describe the characteristics of the far ﬁeld and especially to validate the CFD approach
exploiting schlieren images [43,53,56].
PLIF and PIV measurements also make it possible to characterize the mixing process,
providing detailed information about the local fuel concentration and about the velocity
ﬁeld [49,53]. Axial and transverse density concentration proﬁles are also common plots
produced from both simulation results and experimental measurements.
Two main approaches are used to characterize the mixing process: Scalar Dissipation
Rate (SDR) and the development of a Probability density function (PDF).

<!-- PDF_PAGE: 14 -->

Energies 2023, 16, 6471 14 of 21
The SDR is a measure of the mixing activity. Higher SDR values indicate more
signiﬁcant fuel concentration gradients. Low SDR values, on the other hand, indicate a very
homogeneous spatial distribution of the fuel. This means that good mixing has already
occurred (because the gradients have faded) or, even more, that no mixing is occurring.
The potential core of the jet, which extends averagely for 10/20 diameters downstream,
is surrounded by a mixing layer where, in the radial direction, the fuel concentration
decreases quickly. CFD simulations show that mixing does not occur in the central core
where the jet is supersonic. Only downstream, when the ﬂow becomes subsonic, turbulent
air-fuel mixing begins. String-like structures highlight the edges between high and low-
concentration regions.
Figure 13 reports an example of SDR computed for an under-expanded methane jet.
Figure 13. Scalar dissipation rate plot for two different injected fuels: N2 top and CH4 bottom.
The isolines delimit zones where the fuel concentration is within the ﬂammability limits or in
stoichiometric conditions (reproduced with permission from Ref. [84]. Copyright 2014 Elsevier).
Some research used an SDR approach, concluding that a higher NPR favours a better
and quicker air/fuel mixing [ 53,65,75]. This shows that NPR may substantially modify
the mixing processes, which is not good news considering that high gaseous fuel injection
pressures are typically not easily reachable due to intrinsic limitations in on-board gaseous
fuel storage systems [114].
Achieving a quantitative estimation of the global mixture quality has relevant impor-
tance, especially with regard to the combustion process. Therefore, a statistical approach
is commonly adopted to characterize the mixture obtained from the injection process. A
mass-weighted probability density function ( PDF ) is usually calculated from the CFD
results providing plots like the one in Figure 14.

<!-- PDF_PAGE: 15 -->

Energies 2023, 16, 6471 15 of 21
Figure 14. Probability density function computed to evaluate hydrogen mixture quality (reproduced
with permission from Ref. [103]. Copyright 2016 Elsevier).
If the PDF function is integrated over different ranges of fuel concentration, it allows to
estimate the percentage of lean, ﬂammable and rich mixture [ 51,85,103]. This is important
for evaluating the dynamics of the combustion process that follows the injection.
Turbulence effects are relevant in describing the structure of under-expanded jets far
ﬁeld. The common way to describe turbulence characteristics is to plot Q-criterion iso-
surfaces or vorticity vectors; various authors did this on different kinds of jets [57,104,105].
Proper orthogonal decomposition (POD) was exploited by Vuorinen et al. [ 85] to
project the turbulent ﬂow ﬁeld on basis functions that maximize the turbulent kinetic
energy content for any subset of the base. The dominant structures indicate a helical mode
and the spatial location and shown dynamics of the mode matches the previously existing
picture of noise production.
The compressible vorticity transport equation rules vorticity evolution. Analysis of the
driving forces to distort the streamwise vortices was performed by Li X et al. because it helps
to understand the turbulent transition mechanisms [77]. The authors demonstrated that the
dilatational and baroclinic terms, generally negligible in incompressible flows, are critical
and play a key role in current under-expanded jets. The vorticity transport is not exclusively
driven by vortex stretching but also by the compressibility and baroclinic effects.
The jets’ self-similarity properties were also assessed. They can be estimated with the
ratio of the radial penetration to the axial penetration. When the ratio is stable, it indicates
that the jets reach a self-similarity [63].
Finally , Wu K. et al. focus on the simulation of the acoustic field of highly under-expanded
jets to gain a deeper physical understanding of the noise generation mechanism [76].
6. Conclusions
In this review, a quick and, as far as possible, complete reference guide was pre-
sented in relation to the latest theoretical and experimental research activities regarding the
investigation of under-expanded jets for application in advanced propulsion system.
Under-expanded jets are ﬂuid ﬂows that occur when a high-pressure ﬂuid is suddenly
released through a nozzle into a region of lower pressure. The term “under-expanded”
speciﬁcally describes a condition where the ﬂuid jet does not fully expand to match the
surrounding pressure resulting in the formation of shock waves. Under-expanded jets
are commonly encountered in various engineering applications, including rocket nozzles,
gas and steam releases, supersonic exhaust from jet engines and during the injection of
gaseous fuels in engine systems. Understanding the behaviour of under-expanded jets is
now becoming crucial to develop clean and efﬁcient combustion systems. For this reason,
the most innovative experimental and numerical methods are used to study these jets.
Schlieren imaging is a broadly adopted technique for visualizing the overall jet devel-
opment, and provides macroscopic information like jet penetration, cone angle, volume

<!-- PDF_PAGE: 16 -->

Energies 2023, 16, 6471 16 of 21
and morphology. Local measurements of the jet velocity and fuel density are also possible
via exploiting other techniques like PLIF and PIV .
Fluid-dynamic simulation of under-expanded jets is an important ﬁeld of research. In
dealing with a compressible ﬂow, special attention must be paid to choosing discretization
schemes with low numerical diffusion while ensuring computational stability. High-order
schemes, like ENO or WENO, provide a proﬁcient representation of these ﬂows types but
require structured grids that offer little versatility. On the contrary, ﬂux splitting methods
(like KNP/KT or AUSM+), together with high-order integration schemes, are widely used
with unstructured grids and provide very good results. However, the high-computational
demands represent a signiﬁcant drawback of these approaches. Grids on the order of
magnitude of 10–50 µm are required. Depending on the thermodynamic conditions, a real
gas equation of state may be required to adequately represent critical conditions or, more
generally, deviation from the ideal gas behaviour.
Both outwardly and inwardly injection devices have been the topic of scientiﬁc re-
search. The former category seems to be the best choice due to the amount of fuel they can
supply in a relatively short period.
Injection pressure is usually of the order of tens of bar due to an evident limitation
related to the fuel storage on-board. The injection usually occurs at ambient pressure, while
nozzle holes are of the order of the millimetre.
The Mach disc is undoubtedly the most studied feature of under-expanded jets. It
strongly affects the ﬂow ﬁeld, the air–fuel entrainment, and its geometrical features (width
and height) are related to the pressure ratio. The Mach disc dimensions are usually of the
order of magnitude of a few millimetres.
Turbulent mixing only occurs downstream of the Mach disc and the so-called potential
core, typically extending 10/20 diameters downstream.
POD decomposition, Q-criterion surfaces and vorticity plots help understand turbu-
lence characteristics, while scalar dissipation rate theory and statistical evaluation of the
mixing activity provide relevant information regarding the air–fuel mixture formation.
Finally, it can be stated that the research efforts in investigating under-expanded jets in
advanced propulsion systems will be further directed towards developing injection devices
capable of supplying the required fuel amount in the strict timings available during the
engine cycle. Experimental observations should deepen the jet morphology, providing
further visualisations depicting especially quantitative parameters for comparison with
CFD simulations. The numerical methods adopted for studying under-expanded jets
are resource-demanding. So, optimised approaches should be developed to reduce the
associated computational cost, mainly because these models are expected to be embedded
in whole engine simulations.
Author Contributions: Conceptualization, F.D.; methodology, F.D.; data curation, F.D.;
writing—original draft preparation, F.D.; supervision, C.V . and A.D.V .; writing—review and editing,
C.V . and A.D.V . All authors have read and agreed to the published version of the manuscript.
Funding: This research received no external funding
Data Availability Statement: No new data were created or analyzed in this study. Data sharing is
not applicable to this article.
Conﬂicts of Interest: The authors declare no conﬂicts of interest.
Abbreviations
The following abbreviations are used in this manuscript:
CFD Computational Fluid Dynamics
CNG Compressed Natural Gas
CVC Constant Volume Chamber

<!-- PDF_PAGE: 17 -->

Energies 2023, 16, 6471 17 of 21
DI Direct Injection
DNS Direct Numerical Simulation
fps frames per second
ICE Internal Combustion Engines
KNP Kurganov
KT Kurganov and Tadmor
LED Light Emitting Diode
LES Large Eddy Simulation
˙m∗ critical mass ﬂow
NPR Net Pressure Ratio
PDF Probability Density Function
PECU Programmable Electronic Control Unit
PFI Port Fuel Injected
Pinj injection pressure
p∞ ambient pressure
P∗ critical pressure
PISO Pressure Implicit Split Operator
PPM Piecewise Parabolic Method
RANS Reynolds-Averaged Navier–Stokes
TKE Turbulent Kinetic Energy
TTL Transistor–Transistor Logic
WENO Weighted Essentially Non-Oscillatory
References
1. Joshi, A. Review of Vehicle Engine Efﬁciency and Emissions; SAE Technical Papers; SAE International: Warrendale, PA, USA, 2020;
Volume 2020; pp. 1–29. [CrossRef]
2. IPCC. Climate Change 2021: The Physical Science Basis. Contribution of Working Group I to the Sixth Assessment Report of the
Intergovernmental Panel on Climate Change; Masson-Delmotte, V ., Zhai, P ., Pirani, A., Connors, S.L., Péan, C., Berger, S., Caud, N.,
Chen, Y., Eds.; Cambridge University Press: Cambridge, UK, 2021; p. 3949.
3. International Energy Agency. Tracking Transport 2020; IEA: Paris, France, 2021.
4. International Energy Agency. Net Zero by 2050: A Roadmap for the Global Energy Sector; IEA: Paris, France, 2021; p. 224.
5. Li, F.; Wang, Z.; Wang, Y.; Wang, B. High-Efﬁciency and Clean Combustion Natural Gas Engines for Vehicles.Automot. Innov.
2019, 2, 284–304. [CrossRef]
6. Senecal, K.; Leach, F. Racing Toward Zero: The Untold Story of Driving Green; SAE International: Warrendale, PA, USA, 2021.
7. Sankesh, D.; Lappas, P .Natural-Gas Direct-Injection for Spark-Ignition Engines—A Review on Late-Injection Studies; SAE International:
Warrendale, PA, USA, 2018. [CrossRef]
8. Nocivelli, L.; Sforzo, B.A.; Tekawade, A.; Yan, J.; Powell, C.F.; Chang, W.; Lee, C.F.; Som, S.Analysis of the Spray Numerical Injection
Modeling for Gasoline Applications; SAE Technical Papers; SAE International: Warrendale, PA, USA, 2020. [CrossRef]
9. Zembi, J.; Mariani, F.; Battistoni, M.; Irimescu, A.; Merola, S. Numerical Investigation of Water Injection Effects on Flame
Wrinkling and Combustion Development in a GDI Spark Ignition Optical Engine. In Proceedings of the SAE WCX Digital
Summit, Virtual, 12–15 April 2021; SAE International: Warrendale, PA, USA, 2021. [CrossRef]
10. Oh, H.; Hwang, J.; Pickett, L.M.; Han, D. Machine-learning based prediction of injection rate and solenoid voltage characteristics
in GDI injectors. Fuel 2022, 311, 122569. [CrossRef]
11. Allocca, L.; Montanaro, A.; Meccariello, G.; Duronio, F.; Ranieri, S.; De Vita, A. Under-Expanded Gaseous Jets Characterization for
Application in Direct Injection Engines: Experimental and Numerical Approach; SAE Technical Papers; SAE International: Warrendale,
PA, USA, 2020; Volume 2020; pp. 1–15. [CrossRef]
12. Yip, H.L.; Srna, A.; Chun, A.; Yuen, A.C.Y.; Kook, S.; Taylor, R.; Yeoh, G.; Medwell, P .; Chan, Q. A Review of Hydrogen Direct
Injection for Internal Combustion Engines: Towards Carbon-Free Combustion. Appl. Sci. 2019, 9, 4842. [CrossRef]
13. Hajialimohammadi, A.; Honnery, D.; Abdullah, A.; Mirsalim, M.A. Time resolved characteristics of gaseous jet injected by a
group-hole nozzle. Fuel 2013, 113, 497–505. [CrossRef]
14. Chiodi, M.; Berner, H.J.; Bargende, M. Investigation on Different Injection Strategies in a Direct-Injected Turbocharged Cng-Engine; SAE
Technical Papers; SAE International: Warrendale, PA, USA, 2006. [CrossRef]
15. Yadollahi, B.; Boroomand, M. The effect of combustion chamber geometry on injection and mixture preparation in a CNG direct
injection SI engine. Fuel 2013, 107, 52–62. [CrossRef]
16. Erfan, I.; Hajialimohammadi, A.; Chitsaz, I.; Ziabasharhagh, M.; Martinuzzi, R.J. Inﬂuence of chamber pressure on CNG jet
characteristics of a multi-hole high pressure injector. Fuel 2017, 197, 186–193. [CrossRef]
17. Duronio, F.; Ranieri, S.; Montanaro, A.; Allocca, L.; De Vita, A. ECN Spray G injector: Numerical modelling of ﬂash-boiling
breakup and spray collapse. Int. J. Multiph. Flow 2021, 145, 103817. [CrossRef]
18. Fox, J.H. On the Structure of Jet Plumes. AIAA J. 1974, 12, 105–107. [CrossRef]

<!-- PDF_PAGE: 18 -->

Energies 2023, 16, 6471 18 of 21
19. Doroudi, S. Ansys Fluent Modelling of an Underexpanded Supersonic Sootblower Jet Impinging into Recovery Boiler Tube Geometries;
University of Toronto (Canada): Toronto, ON, Canada, 2015.
20. Knowles, K.; Saddington, A.J. A review of jet mixing enhancement for aircraft propulsion applications. Proc. Inst. Mech. Eng.
Part G J. Aerosp. Eng. 2006, 220, 103–127. [CrossRef]
21. Orescanin, M.M.; Austin, J.M.; Kieffer, S.W. Unsteady high-pressure ﬂow experiments with applications to explosive volcanic
eruptions. J. Geophys. Res. Solid Earth 2010, 115. [CrossRef].
22. Von der Linden, J.; Kimblin, C.; McKenna, I.; Bagley, S.; Li, H.C.; Houim, R.; Kueny, C.S.; Kuhl, A.; Grote, D.; Converse, M.; et al.
Standing shock prevents propagation of sparks in supersonic explosive ﬂows. Commun. Earth Environ. 2021, 2, 195. [CrossRef]
23. Carcano, S.; Bonaventura, L.; Esposti Ongaro, T.; Neri, A. A semi-implicit, second-order-accurate numerical model for multiphase
underexpanded volcanic jets. Geosci. Model Dev. 2013, 6, 1905–1924. [CrossRef]
24. Verhelst, S. Recent progress in the use of hydrogen as a fuel for internal combustion engines. Int. J. Hydrogen Energy 2014,
39, 1071–1085. . [CrossRef]
25. Onorati, A.; Payri, R.; Vaglieco, B.; Agarwal, A.; Bae, C.; Bruneaux, G.; Canakci, M.; Gavaises, M.; Günthner, M.; Hasse, C.; et al.
The role of hydrogen for future internal combustion engines. Int. J. Engine Res. 2022, 23, 529–540. [CrossRef]
26. Kurnia, J.C.; Sasmito, A.P ., Hydrogen Fuel Cell in Vehicle Propulsion: Performance, Efﬁciency, and Challenge. InEnergy Efﬁciency
in Mobility Systems; Sulaiman, S.A., Ed.; Springer: Singapore, 2020; pp. 9–26. [CrossRef]
27. Petrescu, R.V .V .; Machín, A.; Fontánez, K.; Arango, J.C.; Márquez, F.M.; Petrescu, F.I.T. Hydrogen for aircraft power and
propulsion. Int. J. Hydrogen Energy 2020, 45, 20740–20764. [CrossRef]
28. Depcik, C.; Cassady, T.; Collicott, B.; Burugupally, S.P .; Li, X.; Alam, S.S.; Arandia, J.R.; Hobeck, J. Comparison of lithium ion
Batteries, hydrogen fueled combustion Engines, and a hydrogen fuel cell in powering a small Unmanned Aerial Vehicle. Energy
Convers. Manag. 2020, 207, 112514. [CrossRef]
29. Abdel-Rahman, A. A review of effects of initial and boundary conditions on turbulent jets. WSEAS Trans. Fluid Mech. 2010,
4, 257–275.
30. Donaldsion, C.; Snedeker, R. A study of free jet impingement. J. Fluid Mech. 1971, 45, 281–319. [CrossRef]
31. Saddington, A.J.; Lawson, N.J.; Knowles, K. An experimental and numerical investigation of under-expanded turbulent jets.
Aeronaut. J. 2004, 108, 145–152. [CrossRef]
32. John, J. Gas Dynamics; Prentice Hall PTR: Hoboken, NJ, USA, 1984.
33. Dam, N.J.; Rodenburg, M.; Tolboom, R.A.L.; Stoffels, G.G.M.; Huisman-Kleinherenbrink, P .M.; ter Meulen, J.J. Imaging of an
underexpanded nozzle flow by UV laser Rayleigh scattering.Exp. Fluids 1998, 24, 93–101. [CrossRef]
34. Saad, M. Compressible Fluid Flow; Prentice-Hall: Hoboken, NJ, USA, 1985.
35. EWAN, B.C.R.; MOODIE, K. Structure and Velocity Measurements in Underexpanded Jets. Combust. Sci. Technol. 1986,
45, 275–288. [CrossRef]
36. Keith, T.G.; John, J.E. Gas Dynamics; Pearson Education, Inc.: Upper Saddle River, NJ, USA, 2006.
37. Zucker, R.D.; Biblarz, O. Fundamentals of Gas Dynamics; John Wiley & Sons: Hoboken, NJ, USA, 2002.
38. Antsupov, A. Properties of Underexpanded and Overexpanded Supersonic Gas Jets. Sov. Phys. Tech. Phys. 1974, 19, 234 – 238.
39. Hatanaka, K.; Saito, T. Inﬂuence of nozzle geometry on underexpanded axisymmetric free jet characteristics. Shock Waves 2012,
22, 427–434. [CrossRef]
40. Addy, A.L. Effects of axisymmetric sonic nozzle geometry on Mach disk characteristics. AIAA J. 1981, 19, 121–122. [CrossRef]
41. Dong, Q.; Li, Y.; Song, E.; Fan, L.; Yao, C.; Sun, J. Visualization research on injection characteristics of high-pressure gas jets for
natural gas engine. Appl. Therm. Eng. 2018, 132, 165–173. [CrossRef]
42. Zhao, J.; Liu, W.; Liu, Y. Experimental investigation on the microscopic characteristics of underexpanded transient hydrogen jets.
Int. J. Hydrogen Energy 2020, 45, 16865–16873. [CrossRef]
43. Ni, Z.; Dong, Q.; Wang, D.; Yang, X. Visualization research of natural gas jet characteristics with ultra-high injection pressure. Int.
J. Hydrogen Energy 2022, 47, 32473–32492. [CrossRef]
44. Settles, G.S. Schlieren and Shadowgraph Techniques: Visualizing Phenomena in Transparent Media; Springer Science & Business Media:
Berlin/Heidelberg, Germany, 2001.
45. Panigrahi, P .K.; Muralidhar, K.Schlieren and Shadowgraph Methods in Heat and Mass Transfer; Springer: Berlin/Heidelberg, Germany,
2012; Volume 2.
46. Kook, S.; Le, M.K.; Padala, S.; Hawkes, E.R. Z-type Schlieren Setup and its Application to High-Speed Imaging of Gasoline Sprays.
In Proceedings of the SAE International Powertrains, Fuels and Lubricants Meeting, Kyoto, Japan, 30 August–2 September 2011;
SAE International: Warrendale, PA, USA, 2011. [CrossRef]
47. Montanaro, A.; Allocca, L.; De Vita, A.; Ranieri, S.; Duronio, F.; Meccariello, G. Experimental and Numerical Characterization of
High-Pressure Methane Jets for Direct Injection in Internal Combustion Engines. In Proceedings of the SAE Powertrains, Fuels &
Lubricants Meeting, Kraków, Poland, 22–24 September, 2020; SAE International: Warrendale, PA, USA, 2020. [CrossRef]
48. Samsam-Khayani, H.; Chen, B.; Kim, M.; Kim, K.C. Visualization of supersonic free jet ﬂow structures subjected to various
temperature and pressure ratio conditions. Opt. Lasers Eng. 2022, 158, 107144. [CrossRef]
49. Yu, J.; Hillamo, H.; Vuorinen, V .; Sarjovaara, T.; Kaario, O.; Larmi, M.Experimental Investigation of Characteristics of Transient Low
Pressure Wall-Impinging Gas Jet; Institute of Physics Publishing: Bristol, UK, 2011; Volume 318. [CrossRef]

<!-- PDF_PAGE: 19 -->

Energies 2023, 16, 6471 19 of 21
50. Yu, J.; Vuorinen, V .; Kaario, O.; Sarjovaara, T.; Larmi, M. Visualization and analysis of the characteristics of transitional
underexpanded jets. Int. J. Heat Fluid Flow 2013, 44, 140–154. [CrossRef]
51. Sakellarakis, V .D.; Vera-Tudela, W.; Doll, U.; Ebi, D.; Wright, Y.M.; Boulouchos, K. The effect of high-pressure injection variations
on the mixing state of underexpanded methane jets. Int. J. Engine Res. 2021, 22, 2900–2918. [CrossRef]
52. Deshmukh, A.Y.; Falkenstein, T.; Pitsch, H.; Khosravi, M.; van Bebber, D.; Klaas, M.; Schroeder, W. Numerical Investigation of
Direct Gas Injection in an Optical Internal Combustion Engine. SAE Int. J. Engines 2018, 11, 353–378. [CrossRef]
53. Yu, J.; Vuorinen, V .; Kaario, O.; Sarjovaara, T.; Larmi, M. Characteristics of High Pressure Jets for Direct Injection Gas Engine.Int.
J. Fuels Lubr. 2013, 6, 149–156. [CrossRef]
54. Schulz, C.; Sick, V . Tracer-LIF diagnostics: Quantitative measurement of fuel concentration, temperature and fuel/air ratio in
practical combustion systems. Prog. Energy Combust. Sci. 2005, 31, 75–121. [CrossRef]
55. Kirchweger, W.; Haslacher, R.; Hallmannsegger, M.; Gerke, U. Applications of the LIF method for the diagnostics of the
combustion process of gas-IC-engines. Exp. Fluids 2007, 43, 329–340. [CrossRef]
56. Banholzer, M.; Vera-Tudela, W.; Traxinger, C.; Pﬁtzner, M.; Wright, Y.; Boulouchos, K. Numerical investigation of the ﬂow
characteristics of underexpanded methane jets. Phys. Fluids 2019, 31, 056105. [CrossRef]
57. Thawko, A.; van Hout, R.; Yadav, H.; Tartakovsky, L. Flow ﬁeld characteristics of a conﬁned, underexpanded transient round jet.
Phys. Fluids 2021, 33. [CrossRef]
58. Xiao, C.N.; Fond, B.; Beyrau, F.; T’Joen, C.; Henkes, R.; Veenstra, P .; van Wachem, B. Numerical Investigation and Experimental
Comparison of the Gas Dynamics in a Highly Underexpanded Conﬁned Real Gas Jet. Flow Turbul. Combust. 2019, 103, 141–173.
[CrossRef]
59. Duronio, F.; Mascio, A.D.; Villante, C.; Anatone, M.; Vita, A.D. ECN Spray G: Coupled Eulerian internal nozzle ﬂow and
Lagrangian spray simulation in ﬂash boiling conditions. Int. J. Engine Res. 2023, 24, 1530–1544. [CrossRef]
60. Hamzehloo, A.; Aleiferis, P .G. Large Eddy Simulation of Near-Nozzle Shock Structure and Mixing Characteristics of Hydrogen
Jets for Direct-Injection Spark-Ignition Engines. In Proceedings of the 10th International Conference on Heat Transfer, Fluid
Mechanics and Thermodynamics, Orlando, FL, USA, 14–16 July 2014.
61. Rahantamialisoa, F.N.; Zembi, J.; Miliozzi, A.; Sahranavardfard, N.; Battistoni, M. CFD Simulations of Under-Expanded Hydrogen
Jets under High-Pressure Injection Conditions; Institute of Physics: Bristol, UK, 2022; Volume 2385. [CrossRef]
62. Verrière, J.; Kopriva, J.E. Simulations of an Underexpanded Round Jet Using the Lattice-Boltzmann Method ; American Institute of
Aeronautics and Astronautics Inc.: Reston, VA, USA, 2021. [CrossRef]
63. Kopriva, J.E.; Laskowski, G.M.; Polidoro, F.; Li, Y.; Jammalamadaka, A.; Nardari, C. Lattice-Boltzmann Simulations of an
Underexpanded Jet from a Rectangular Nozzle with and without Aft-Deck; American Institute of Aeronautics and Astronautics Inc.:
Reston, VA, USA, 2019. [CrossRef]
64. Ren, Z.; Wen, J.X. Numerical characterization of under-expanded cryogenic hydrogen gas jets. AIP Adv. 2020, 10. [CrossRef]
65. Buttay, R.; Lehnasch, G.; Mura, A. Analysis of small-scale scalar mixing processes in highly under-expanded jets. Shock Waves
2016, 26, 193–212. [CrossRef]
66. Quimby, D.; Jacobs, G.B. Large Eddy Simulation of a Supersonic Underexpanded Jet with a High-Order Hybrid WENO-Z/central Scheme;
American Institute of Aeronautics and Astronautics Inc.: Reston, VA, USA, 2016. [CrossRef]
67. Su, H.; Cai, J.; Qu, K.; Pan, S. Numerical simulations of inert and reactive highly underexpanded jets. Phys. Fluids 2020, 32.
[CrossRef]
68. Greenshields, C.J.; Weller, H.G.; Gasparini, L.; Reese, J.M. Implementation of semi-discrete, non-staggered central schemes in
a colocated, polyhedral, ﬁnite volume framework, for high-speed viscous ﬂows. Int. J. Numer. Methods Fluids 2010, 63, 1–21.
[CrossRef]
69. Versteg, H.; Malalasekera, W. An introduction to Computational Fluid Dynamics: The Finite Volume Method , 2nd ed.; Pearson
Education: London, UK, 2007.
70. Di Angelo, L.; Duronio, F.; De Vita, A.; Di Mascio, A. Cartesian Mesh Generation with Local Reﬁnement for Immersed Boundary
Approaches. J. Mar. Sci. Eng. 2021, 9, 572. [CrossRef]
71. Kurganov, A.; Tadmor, E. New High-Resolution Central Schemes for Nonlinear Conservation Laws and Convection-Diffusion
Equations. J. Comput. Phys. 2000, 160, 241–282. [CrossRef]
72. Kurganov, A.; Noelle, S.; Petrova, G. Semidiscrete Central-Upwind Schemes for Hyperbolic Conservation Laws and Hamilton–
Jacobi Equations. SIAM J. Sci. Comput. 2001, 23, 707–740. [CrossRef]
73. van Leer, B. Towards the ultimate conservative difference scheme. II. Monotonicity and conservation combined in a second-order
scheme. J. Comput. Phys. 1974, 14, 361–370. [CrossRef]
74. Jin, Y.; Yao, W.LES Investigation of Real-Fluid Effect on Underexpanded Jets; American Institute of Aeronautics and Astronautics Inc.:
Reston, VA, USA, 2021. [CrossRef]
75. Duronio, F.; Montanaro, A.; Ranieri, S.; Allocca, L.; De Vita, A. Under-Expanded Jets Characterization by Means of CFD Numerical
Simulation Using an Open FOAM Density-Based Solver. In Proceedings of the 15th International Conference on Engines & V ehicles,
Napoli, Italy , 12–16 September 2021; SAE International: Warrendale, PA, USA, 2021. [CrossRef]
76. Wu, K.; Li, X.; Yao, W.; Fan, X.Three-Dimensional Numerical Study of the Acoustic Properities of a Highly Underexpanded Jet; AIAA
American Institute of Aeronautics and Astronautics: Reston, VA, USA, 2015. [CrossRef]

<!-- PDF_PAGE: 20 -->

Energies 2023, 16, 6471 20 of 21
77. Li, X.; Yao, W.; Fan, X. Large-eddy simulation of time evolution and instability of highly underexpanded sonic jets. AIAA J. 2016,
54, 3191–3211. [CrossRef]
78. Vuorinen, V .; Wehrfritz, A.; Yu, J.; Kaario, O.; Larmi, M.; Boersma, B.J. Large-eddy simulation of subsonic jets. J. Phys. Conf. Ser.
2011, 318, 032052. [CrossRef]
79. Vuorinen, V .; Keskinen, J.P .; Duwig, C.; Boersma, B.J. On the implementation of low-dissipative Runge–Kutta projection methods for
time dependent flows using OpenFOAM®.Comput. Fluids 2014, 93, 153–163. [CrossRef]
80. Vuorinen, V .; Larmi, M.; Schlatter, P .; Fuchs, L.; Boersma, B.J. A low-dissipative, scale-selective discretization scheme for the
Navier–Stokes equations. Comput. Fluids 2012, 70, 195–205. [CrossRef]
81. Modesti, D.; Pirozzoli, S. A low-dissipative solver for turbulent compressible ﬂows on unstructured meshes, with OpenFOAM
implementation. Comput. Fluids 2017, 152, 14–23. [CrossRef]
82. Hamzehloo, A.; Aleiferis, P .G. Numerical modelling of transient under-expanded jets under different ambient thermodynamic
conditions with adaptive mesh refinement.Int. J. Heat Fluid Flow2016, 61, 711–729. [CrossRef]
83. Sun, G.; Wu, G.; Liu, C.J. Numerical Simulation of Supersonic Flow with Shock Wave using Modiﬁed AUSM Scheme. Int. J.
Nonlinear Sci. Numer. Simul. 2006, 7, 329–332. [CrossRef]
84. Vuorinen, V .; Wehrfritz, A.; Duwig, C.; Boersma, B.J. Large-eddy simulation on the effect of injection pressure and density on fuel
jet mixing in gas engines. Fuel 2014, 130, 241–250. [CrossRef]
85. Vuorinen, V .; Yu, J.; Tirunagari, S.; Kaario, O.; Larmi, M.; Duwig, C.; Boersma, B.J. Large-eddy simulation of highly underexpanded
transient gas jets. Phys. Fluids 2013, 25, 016101. [CrossRef]
86. Hamzehloo, A.; Aleiferis, P .G. LES and RANS modelling of under-expanded jets with application to gaseous fuel direct injection
for advanced propulsion systems. Int. J. Heat Fluid Flow 2019, 76, 309–334. [CrossRef]
87. Deshmukh, A.Y.; Bode, M.; Pitsch, H.; Khosravi, M.; Bebber, D.v.; Vishwanathan, G. Characterization of Hollow Cone Gas Jets in
the Context of Direct Gas Injection in Internal Combustion Engines. SAE Int. J. Fuels Lubr. 2018, 11, 353–377. [CrossRef]
88. Bartolucci, L.; Cordiner, S.; Mulone, V .; Rocco, V . Natural Gas Stable Combustion under Ultra-Lean Operating Conditions in
Internal Combustion Engines. Energy Procedia 2016, 101, 886–892. [CrossRef]
89. Hamzehloo, A.; Aleiferis, P . Large eddy simulation of highly turbulent under-expanded hydrogen and methane jets for gaseous-
fuelled internal combustion engines.Int. J. Hydrogen Energy2014, 39, 21275–21296. [CrossRef]
90. De Vita, M.; Duronio, F.; De Vita, A.; De Berardinis, P . Adaptive Retroﬁt for Adaptive Reuse: Converting an Industrial Chimney
into a Ventilation Duct to Improve Internal Comfort in a Historic Environment gas expansion. Sustainability 2022, 14 3360.
[CrossRef]
91. Zhu, H.; Battistoni, M.; Manjegowda Ningegowda, B.; Nadia Zazaravaka Rahantamialisoa, F.; Yue, Z.; Wang, H.; Yao, M.
Thermodynamic modeling of trans/supercritical fuel sprays in internal combustion engines based on a generalized cubic
equation of state. Fuel 2022, 307, 121894. [CrossRef]
92. Li, X.; Zhou, R.; Yao, W.; Fan, X. Flow characteristic of highly underexpanded jets from various nozzle geometries. Appl. Therm.
Eng. 2017, 125, 240–253. [CrossRef]
93. Anaclerio, G.; Capurso, T.; Torresi, M.; Camporeale, S.M.Numerical Characterization of Hydrogen Under-Expanded Jets: Influence of the
Nozzle Cross-Section Shape; Institute of Physics: Bristol, UK, 2022, V olume 2385. [CrossRef]
94. Bonelli, F.; Viggiano, A.; Magi, V . A numerical analysis of hydrogen underexpanded jets under real gas assumption.J. Fluids Eng.
Trans. ASME 2013, 135. [CrossRef]
95. Kaario, O.; Vuorinen, V .; Hulkkonen, T.; Keskinen, K.; Nuutinen, M.; Larmi, M.; Tanner, F.X. Large eddy simulation of high gas
density effects in fuel sprays. At. Sprays 2013, 23, 297–325. [CrossRef]
96. Pope, S.B. Turbulent Flows; Cambridge University Press: Cambridge, UK, 2001.
97. Weickert, M.; Teike, G.; Schmidt, O.; Sommerfeld, M. Investigation of the LES WALE turbulence model within the lattice
Boltzmann framework. Comput. Math. Appl. 2010, 59, 2200–2214. [CrossRef]
98. Huang, S.; Li, Q.S. A new dynamic one-equation subgrid-scale model for large eddy simulations. Int. J. Numer. Methods Eng.
2010, 81, 835–865.
99. Yoshizawa, A; Horiuti, K. A statistically-derived subgrid-scale kinetic energy model for the large-eddy simulation of turbulent
ﬂows. J. Phys. Soc. Jpn. 1985, 54, 2834–2839. [CrossRef]
100. Munday, D.; Gutmark, E.; Liu, J.; Kailasanath, K. Flow structure and acoustics of supersonic jets from conical convergent-divergent
nozzles. Phys. Fluids 2011, 23, 116102,
101. Garnier, E.; Adams, N.; Sagaut, P . Large Eddy Simulation for Compressible Flows ; Springer Science & Business Media:
Berlin/Heidelberg, Germany, 2009.
102. Rana, Z.A.; Thornber, B.; Drikakis, D. Transverse jet injection into a supersonic turbulent cross-ﬂow. Phys. Fluids 2011, 23, 046103.
103. Hamzehloo, A.; Aleiferis, P .G. Gas dynamics and ﬂow characteristics of highly turbulent under-expanded hydrogen and methane
jets under various nozzle pressure ratios and ambient pressures. Int. J. Hydrogen Energy 2016, 41, 6544–6566. [CrossRef]
104. Duronio, F.; Ranieri, S.; Mascio, A.D.; Vita, A.D. Simulation of high pressure, direct injection processes of gaseous fuels by a
density-based OpenFOAM solver. Phys. Fluids 2021, 33, 066104.
105. Duronio, F.; Montanaro, A.; Allocca, L.; Ranieri, S.; De Vita, A. Effects of Thermodynamic Conditions and Nozzle Geometry
in Gaseous Fuels Direct Injection Process for Advanced Propulsion Systems. In Proceedings of the WCX SAE World Congress
Experience, Detroit, MI, USA, 18–20 April 2020; SAE International: Warrendale, PA, USA, 2022. [CrossRef]

<!-- PDF_PAGE: 21 -->

Energies 2023, 16, 6471 21 of 21
106. Banholzer, M.; Müller, H.; Pﬁtznery, M.Numerical Investigation of the Flow Structure of Underexpanded Jets in Quiescent Air Using
Real-Gas Thermodynamics; American Institute of Aeronautics and Astronautics Inc.: Reston, VA, USA, 2017. [CrossRef]
107. Traxinger, C.; Banholzer, M.; Pﬁtzner, M. Real-Gas Effects and Phase Separation in Underexpanded Jets at Engine-Relevant
Conditions. In Proceedings of the 2018 AIAA Aerospace Sciences Meeting, Kissimmee, FL, USA, 8–12 January 2018. [CrossRef]
108. Rahantamialisoa, F.; Battistoni, M.; Miliozzi, A.; Sahranavardfard, N.; Zembi, J. Investigations on Hydrogen Injections Using a
Real-Fluid Approach; SAE International: Warrendale, PA, USA, 2023. [CrossRef]
109. Yosri, M.R.; Talei, M.; Gordon, R.; Brear, M.; Lacey, J. A Numerical Simulation of an Under-Expanded Jet Issued from a Prototype
Injector; The University of Queensland: Brisbane, Australia, 2020. [CrossRef]
110. Bartolucci, L.; Cordiner, S.; Mulone, V .; Scarcelli, R.; Wallner, T.; Swantek, A.; Powell, C.; Kastengren, A. Gaseous jet through
an outward opening injector: Details of mixing characteristic and turbulence scales. Int. J. Heat Fluid Flow 2020, 85, 108660.
[CrossRef]
111. Cao, W.; Zhou, Z.; Zhou, W.; Xu, S.; Xiao, Q.; Cao, W.; Jiao, F.; Zhang, Y.; Yu, S.; Xu, S. The ﬂow ﬁeld behaviours of under-expansion
jet ﬂame in premixed hydrogen/air explosion venting. Int. J. Hydrogen Energy 2022, 47, 10420–10430. [CrossRef]
112. Duronio, F.; Di Mascio, A.; De Vita, A.; Innocenzi, V .; Prisciandaro, M. Eulerian–Lagrangian modeling of phase transition for
application to cavitation-driven chemical processes. Phys. Fluids 2023, 35, 053305.
113. Förster, F.J.; Baab, S.; Steinhausen, C.; Lamanna, G.; Ewart, P .; Weigand, B. Mixing characterization of highly underexpanded
ﬂuid jets with real gas expansion. Exp. Fluids 2018, 59. [CrossRef]
114. Verhelst, S.; Sierens, R. Hydrogen engine-speciﬁc properties. Int. J. Hydrogen Energy 2001, 26, 987–990. [CrossRef]
Disclaimer/Publisher’s Note: The statements, opinions and data contained in all publications are solely those of the individual
author(s) and contributor(s) and not of MDPI and/or the editor(s). MDPI and/or the editor(s) disclaim responsibility for any injury to
people or property resulting from any ideas, methods, instructions or products referred to in the content.
