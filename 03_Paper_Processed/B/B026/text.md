<!-- PDF_PAGE: 1 -->

Contents lists available at ScienceDirect
International Journal of Hydrogen Energy
journal homepage: www.elsevier.com/locate/he
Unsteady RANS simulations of under-expanded hydrogen jets for internal
combustion engines
Giovanni Caramia ∗, Riccardo Amirante, Pietro De Palma
Politecnico di Bari, Department of Mechanics, Mathematics and Management, via Re David 200, Bari, 70125, Italy
A R T I C L E I N F O
Keywords:
Hydrogen direct injection
Hydrogen–air mixing
Mach disk
WENO schemes
A B S T R A C T
Hydrogen can be considered a suitable fuel for heavy-duty reciprocating internal combustion engines (ICEs) in
order to limit carbon dioxide emissions. The low volumetric power density of hydrogen and the backfire
problem suggest to employing the direct injection technology with relatively high nozzle pressure ratios
(NPRs). This paper provides the analysis of under-expanded hydrogen jet dynamics using an open-source high-
fidelity simulation tool based on the OpenFOAM framework. The unsteady Reynolds-averaged Navier–Stokes
(URANS) equations are solved by an efficient pressure-based solver for compressible flow. URANS equations
are attractive for fast engineering analysis of 3D engine cycle and optimization, where large eddy simulation
(LES) is too computationally expensive. The accuracy of the simulations is enhanced by employing the weighted
essentially non-oscillatory (WENO) approach for the spatial discretization, considering schemes from second-
order to fourth-order accuracy. Those schemes are embedded in a pressure-implicit with splitting of operators
(PISO) algorithm, obtaining a very robust and accurate numerical method for compressible multi-species flows,
which can be shared in an open access framework. Hydrogen injection in air is simulated, with several values
of the NPR typical of direct injection ICE in the low-medium range, 8.5 ≤ 𝑁𝑃 𝑅 ≤ 30. The main features of the
developing jet are analyzed, such as barrel shock dimensions, cone angle and hydrogen–air mixing. The results
are validated with respect to experimental and LES data available in the recent literature, demonstrating the
efficiency and the accuracy of the employed URANS approach and evaluating its limits.
1. Introduction
Since the 19th century, hydrogen has been considered an alternative
fuel for internal combustion engines. The first attempts to develop a
hydrogen-fueled engine date back to the work of W. Cecil in 1820 [1,2].
However, over the past two centuries, hydrogen has primarily been
used for space launch propulsion due to its 30% higher specific impulse
compared to conventional hydrocarbon propellants [3,4]. Hydrogen
was notably used during the Apollo 11 mission as fuel for the Saturn
V rocket, which brought the first men to the Moon. NASA utilized
cryogenic liquid hydrogen to increase the power density of the fuel
and employed hydrogen both for propulsion and in fuel cells to provide
electricity and water during the mission. Hydrogen was also used in all
Space Shuttle missions for propulsion, electrical system powering, and
water supply.
Historically, hydrogen was not considered convenient for use in
reciprocating Internal Combustion Engine (ICE) compared to standard
fossil fuels. This was due to several factors, including high production
costs, storage difficulties, and lower volumetric specific heat. However,
the context is now changing. Increased awareness of environmental
∗ Corresponding author.
E-mail address: giovanni.caramia@poliba.it (G. Caramia).
issues and the need to reduce or eliminate greenhouse gas emissions
have motivated the exploration of new technical solutions for using
hydrogen derived from renewable energy sources in ICEs [5,6]. The use
of hydrogen in this context avoids the production of carbon dioxide.
Advancements in renewable hydrogen technologies have been made,
including improved hydrogen storage (in liquid form at cryogenic
temperatures or in gaseous form up to 700 bar), hydrogen production
(e.g., solar thermochemical processes), and usage (e.g., high-pressure
direct injection of gas). These developments have renewed interest in
using hydrogen as an energy carrier in ICE powertrains.
In particular, during the 1990s, hydrogen was considered to en-
hance the performance of spark ignition [7] and compression igni-
tion [8] engines using a dual fuel approach [9].
Hydrogen has been employed in various modes, such as port fuel
injection spark ignition systems [10,11] and dual fuel compression
ignition systems [12,13], to improve the performance of ICEs. However,
its use was complicated by hydrogen’s very low combustion activation
energy, which could lead to backfire and pre-ignition problems [14–
16]. In the first decade of the new millennium, the concept of using
https://doi.org/10.1016/j.ijhydene.2024.11.242
Received 18 June 2024; Received in revised form 26 October 2024; Accepted 13 November 2024
International Journal of Hydrogen Energy 96 (2024) 849–859 
Available online 28 November 2024 
0360-3199/© 2024 The Authors. Published by Elsevier Ltd on behalf of Hydrogen Energy Publications LLC. This is an open access article under the CC BY license 
( http://creativecommons.org/licenses/by/4.0/ ).

<!-- PDF_PAGE: 2 -->

G. Caramia et al.
Acronyms
CFD Computational Fluid Dynamics
CU Cubic reconstruction
DI Direct Injection
ICE Internal Combustion Engine
LES Large Eddy Simulation
LU Linear Upwind
NPR Nozzle Pressure Ratio
PLIF Planar Laser Induced Fluorescence
SOI Start Of Injection
URANS Unsteady Reynolds-Averaged Navier–Stokes
WENO Weighted Essentially Non-Oscillatory
hydrogen fuel in ICEs emerged as a bridging solution towards battery
and fuel cell-operated vehicles [17]. Despite this interest, the adoption
of hydrogen engines faced practical challenges, including the lack of
commercially viable Direct Injection (DI) gaseous fuel systems, limited
power density, inadequate hydrogen distribution infrastructure, and the
absence of low-cost storage systems.
Very recently, hydrogen has been gaining credibility as a zero-
carbon fuel for ICEs from both a tank-to-wheel perspective, due to the
absence of CO2 emissions, and from a well-to-wheel perspective, par-
ticularly when its production is based on renewable energy sources [6].
This view is especially compelling for heavy-duty applications, where
the use of battery electric engines is not yet feasible. Such a scenario has
prompted the development of high-pressure storage systems [18] and
DI technologies, as these promise to address the issue of hydrogen’s low
volumetric energy density.
Given these motivations, there is abundant literature on the use
of hydrogen in ICEs [19]. Many aspects of hydrogen-fueled engines
have been studied using both experimental and numerical approaches.
These studies include fundamental analyses using high-fidelity numer-
ical simulations of hydrogen jets [20–25], mixture formation [26–
28], combustion and performance [29–36], and heat transfer in DI
engines [37–39].
1.1. Under-expanded jets
Donaldson and Snedeker [40] have reviewed the previous experi-
mental studies on the behavior of compressible jets of cold air issuing
from convergent nozzles. The jets can be characterized by defining
three reference pressures: the upstream total pressure 𝑝0, the pressure
at the nozzle exit 𝑝1, and the pressure 𝑝∞, which represents the ambient
pressure in which the free jet develops. Their analysis indicates three
major jet flow regimes for cold air, corresponding to specific intervals
of pressure ratios: the subsonic jet regime for which 𝑝1∕𝑝∞ = 1 and
1 < 𝑝0∕𝑝∞ < 1.894; the moderately under-expanded jet regime for which
1.1 < 𝑝1∕𝑝∞ ≤ 2 and 2.083 < 𝑝0∕𝑝∞ ≤ 3.846; and the highly under-
expanded jet regime for which 𝑝1∕𝑝∞ > 2 and 𝑝0∕𝑝∞ > 3.846. The
quantity 𝑝0∕𝑝∞ defines the Nozzle Pressure Ratio (NPR). In moderately
under-expanded conditions, the jet exhibits the familiar oblique shock
pattern (‘‘shock diamonds’’), with regular reflections of the shock waves
on the symmetry axis. In such a flow regime, Mach waves depart
from the lip of the nozzle, creating the Prandtl–Meyer expansion fan.
They then reflect onto the jet boundary and collapse, originating weak
compression waves, which form the intercepting shocks and reflect on
the axis generating the reflected shocks. The classical picture of the
structure of a highly under-expanded jet (𝑁 𝑃 𝑅 > 3.846) is shown
in Fig. 1, providing the main structural elements typical of this phe-
nomenon, namely, the Mach disk, the barrel shock, the slip lines, the
reflected shocks.
Fig. 1. Diagram of highly under-expanded jet.
In such a flow regime, Mach waves depart from the lip of the nozzle,
creating the Prandtl–Meyer expansion fan. They then reflect onto the
jet boundary and collapse originating weak compression waves which
form the intercepting shocks that are ended by a slightly curved strong
normal shock called Mach disk, as shown in Fig. 1. The formation
of the Mach disk is explained as follows. If the angle of deflection
of the supersonic flow at the axis of symmetry of the jet is greater
than a critical value (depending on the upstream Mach number and
the ratio of specific heats), the regular oblique shock reflection of the
intercepting shock cannot correct the flow direction. As a consequence,
a quasi-normal shock forms (the Mach disk), which allows the triple
point to detach from the symmetry line. This process is called Mach
reflection. In this process, the flow upstream and downstream of the
Mach disk is nearly parallel to the symmetry line. The intercepting
shock and the Mach disk form the first shock cell, known as the barrel
shock, due to its cylindrical shape. On a 2-D plane, a reflected shock
and a slip line can be seen at the triple point, which is the merging
location of the intercepting shock and the Mach disk. The flow behind
the Mach disk is subsonic, whereas the flow behind the reflected shock
remains supersonic. A slip line separates the subsonic flow stream past
the Mach disk from the supersonic flow stream through the reflected
shock, triggering a turbulent mixing process within the jet core.
For highly under-expanded jets, in the range of 3.846 < 𝑁 𝑃 𝑅 < 7,
the subsonic core behind the Mach disk accelerates again and becomes
supersonic, originating a second shock cell that may resemble the
first shock cell and even include a normal shock comparable to the
Mach disk. At higher levels of NPR, 𝑁 𝑃 𝑅 > 7, a large Mach disk
forms at the nozzle exit, with no additional normal shocks downstream,
and the jet then decays resembling a subsonic jet [21,40]. The near-
nozzle configuration of under-expanded jets is quantified by several
parameters that include the dimensions of the Mach disk, the angle of
the reflected shock at the triple point and the length of the shear layer
thickness (maximum distance between the slip line and the reflected
shock). These quantities have a significant effect on the annular shear
layer thickness and on the mixing characteristics of the under-expanded
flow. They can be used as fundamental measures for comparing under-
expanded jets with different values of NPR and also for validating
numerical models. The Mach disk is characterized by the axial distance
of the disk from the nozzle exit, i.e. the Mach disk height, 𝐻𝑑 𝑖𝑠𝑘, and
the distance between the two triple points in a meridional section of the
jet, called the Mach disk width, 𝑊𝑑 𝑖𝑠𝑘 (see Fig. 1). The reflected shock
angle and the shear layer thickness are significantly affected by the
Mach disk dimensions and several correlations have been suggested for
predicting 𝐻𝑑 𝑖𝑠𝑘 and 𝑊𝑑 𝑖𝑠𝑘. For instance, by carrying on experimental
investigations, and with the assumption of choked condition at the
nozzle exit, Crist et al. [41] suggested that the relation between NPR
and the Mach disk height is 𝐻𝑑 𝑖𝑠𝑘∕𝐷 =
√
1∕2.4
√
𝑝0∕𝑝∞, where D is the
nozzle diameter. As 𝐻𝑑 𝑖𝑠𝑘∕𝐷 increases, also the distance between the
slip lines increases.
International Journal of Hydrogen Energy 96 (2024) 849–859 
850

<!-- PDF_PAGE: 3 -->

G. Caramia et al.
1.2. Review of hydrogen jet study and modeling
Several experimental studies have been carried on to study the
physics and the dynamics of hydrogen under-expanded jets. Salazar
and Kaiser [27] used particle image velocimetry and Planar Laser
Induced Fluorescence (PLIF) techniques to study hydrogen DI in a
single-cylinder optical research engine. The experiments were carried
out for several injection pressures and with different number of nozzle
holes and intake port configurations in order to study the dynamics of
mixture formation. Salazar and Kaiser [29] visualized the flame prop-
agation in an optically accessible hydrogen-fueled internal combustion
engine by high-speed Schlieren imaging. Two intake configurations
were evaluated with different tumble ratio. The flame location was
correlated with pressure measurements on a single-cycle basis. Scarcelli
et al. [42] studied experimentally the hydrogen DI in a cylinder with
optical access typical of a spark-ignited engines, with a centrally located
injector. A single hole and a 13-hole nozzle were used with 100 bar and
25 bar injection pressure. Quantitative PLIF was employed to obtain
phase-locked images of the fuel mole-fraction, while visualization of the
early jet penetration was achieved by a high-speed Schlieren technique.
Ruggles and Ekoto [43] studied experimentally a hydrogen jet with a
10:1 pressure ratio issuing from a small nozzle with 0.75 mm radius.
Jet exit shock structure was visualized by Schlieren photography, while
quantitative planar laser Rayleigh scatter imaging was used to mea-
sure instantaneous hydrogen mole fractions downstream of the Mach
disk. Measured concentration statistics and ignitable boundary predic-
tions compared favorably to analytic reconstructions of downstream jet
dispersion behavior.
On the other hand, considering the complex nature of the dy-
namics of under-expanded hydrogen injection, many research groups
have studied its details by a numerical approach, applying several
methodologies with different levels of accuracy.
Scarcelli et al. [42] proposed the validation of a Computational
Fluid Dynamics (CFD) code for the study of the mixture formation in
a DI hydrogen-fueled engine with different types of nozzles. Numerical
results from the commercial code Fluent (v6.3.35) were compared to
experimental data. The influence of the computational grids was dis-
cussed, especially for the near-nozzle region, where the jets were under-
expanded. Simulation of injection from a single-hole nozzle provided a
good agreement with experimental results in terms of jet penetration
and overall evolution. Concerning the multi-hole nozzle, intense jet-to-
jet interaction was observed, with all jets merging downstream of the
under-expanded region. This phenomenon (usually referred as Coanda
Effect) resulted to be very challenging and required high levels of
accuracy and grid resolution.
Hamzehloo and Aleiferis [20] focused on the computational study of
hydrogen jets with the aim of analyzing the results obtained by solv-
ing the RANS equations and by the LES approach. The computations
were carried on by the STAR-CCM+ code considering different nozzle
geometries and injection pressures. They concluded that LES provides a
better resolution of the shock structures close to the nozzle compared to
RANS solutions obtained using the same computational grid. Moreover,
they found that LES is capable of providing predictions of hydrogen–
air mixing qualitatively comparable with experimental results available
in the literature for other gases. Hamzehloo and Aleiferis [21] studied
by Large Eddy Simulation (LES) the characteristics of hydrogen under-
expanded jets with different NPRs, namely 8.5, 10, 30 and 70. The
results of the simulations in terms of near-nozzle shock structure, geom-
etry of the Mach disk, reflected shock angle, and turbulent shear layer
were all in very good agreement with experimental data available in the
literature. Moreover, the comparison between hydrogen and methane
jets showed that the ratio of the specific heats had a remarkable effect
on the near-nozzle shock structure. It was observed that using methane,
mixing did not occur before the Mach disk, as usual, the primary mixing
being observed to occur behind the Mach disk and close to the jet
boundaries where large-scale turbulence structures develop. Whereas,
when employing hydrogen, high levels of momentum exchange and
mixing appeared at the boundary of the intercepting shock. This is
probably due to the higher level of hydrogen turbulence intensity
already at the nozzle exit which triggers Gortler vortices. It was also
found that NPR had a significant effect on the mixture’s local fuel
richness. Finally, applying higher injection pressure did not increase
the penetration length of the hydrogen jets. There could be an optimum
value of the NPR, around 100, that would maximize mixing and mass
fuel injection in a given time.
LeMoine et al. [44] reported the validation of a three-dimensional
numerical simulation of the mixture formation in a DI hydrogen-
fueled engine. The simulations were carried on by the commercial code
CONVERGE, comparing the results to the experimental data from an
optically accessible engine. Hydrogen was supplied at 100 bar from a
centrally located injector with a single-hole nozzle. The comparison was
carried on in terms of fuel mole concentration and flow field during the
early stage of the compression stroke. The penetration of the jet and the
interaction with the cylinder walls were correctly predicted, whereas
the fuel spreading was underpredicted.
Tang et al. [45] investigated numerically an under-expanded hy-
drogen jet flow from a small jet orifice with a diameter of 0.2 mm
and with total pressure equal to 82 MPa. They solved the 3D Navier–
Stokes equations, employing an adaptive mesh refinement approach.
Instantaneous and mean hydrogen concentration distributions in the
jet were discussed. The centerline intensity of the concentration fluc-
tuation asymptotically achieved a constant value, which was in a good
agreement with the experimental results. It corroborated the conclusion
that the asymptotic centerline value of the concentration is independent
of the jet density ratio. The probability distribution function of the
instantaneous axial concentration was close to the Gaussian distribution
while skewing a little to the higher range. The time averaged concen-
tration along the radial directions could also be described as a Gaussian
distribution, whereas, the jet velocity half-width approximately showed
a linear behavior with the axial coordinate.
Ye et al. [46] studied numerically the effect of injection timing on
knock phenomenon in a DI hydrogen engine. The authors found that
both mixture uniformity and the flame speed increase with the advance
of injection timing. The intensity of the knock was non-monotonic with
the injection timing: delaying injection, knock intensity first decreases
and then increases, so that there is a minimum value. Another problem
was the occurrence of auto-ignition spots either near the cylinder wall
or at the bottom of the piston pit. Finally, the numerical results showed
that heavy pressure oscillations could be generated by the coupling
between pressure wave and flame front oscillations.
Babayev et al. [47] carried on a computational study to assess the
characteristics of DICI H2 engines using the CONVERGE CFD solver.
A grid sensitivity study was performed to assess the convergence of
the numerical results with respect to experimental data. Unlike the
common behavior of diesel sprays, hydrogen jets do not exhibit a
significant flame lift-off and entrainment of air close to the injector.
Moreover, fuel–air premixing is rather scarce, the fuel–air interface
being well stratified. It was found that the DICI H2 combustion was
mainly characterized by a free turbulent jet mixing phase and then
by an in-cylinder global mixing phase, the former being dominant
compared to diesel engines. This indicates the need to re-design the
optimization strategies when using H2 as fuel.
Addepalli et al. [28] carried on a numerical study of the mixture
formation in a hydrogen DI spark-ignition engine, considering a single
hole injector with 100 bar injection pressure. The numerical results
were obtained with different degrees of tumble and were validated
versus optical data acquired by PLIF measurements. A sensitivity mesh
analysis was carried on to study the effect of nozzle geometry and mesh
orientation near the wall. The prediction of the mixture distribution
in the cylinder agreed reasonably well with the experimental data,
especially when a mesh aligned with the flow direction was employed.
International Journal of Hydrogen Energy 96 (2024) 849–859 
851

<!-- PDF_PAGE: 4 -->

G. Caramia et al.
Ballatore and van Oijen [48] presented an assessment of Large
Eddy Simulation (LES) of non-reactive under-expanded hydrogen jets
by using a pressure-based algorithm. They evaluated the suitability
of the pressure-based solver to correctly describe the flow field of
gaseous hydrogen jets for engine applications. Hydrogen jets in an
argon atmosphere at three different injection pressures were simulated,
comparing the results to experimental data available in the literature.
In particular, jet tip penetration and cone angle were investigated.
Different LES sub-grid scale models and discretization schemes were
employed in order to find the best approach in terms of accuracy and
required computational cost. In particular, the authors found that the
WALE model coupled with a 4th-order-accurate cubic scheme for the
convective terms yields the most accurate results among the considered
numerical approaches.
Yosri et al. [49] presented Unsteady Reynolds-Averaged Navier–
Stokes (URANS) simulations of a large bore, hydrogen-fueled DI spark-
ignition engine with different spark and Start Of Injection (SOI) tim-
ings. The numerical simulations were validated versus experimental
data. It was shown that the auto-ignition occurs with advanced spark
timing due to high in-cylinder pressure and unburnt-gas temperature.
For different SOIs, it was demonstrated that flame propagation involves
a spark-initiated flame combined with another flame generated by
auto-ignition. The case with late injection timing showed poor mixing
and slower combustion due to the presence of lean mixtures near
the spark plug. In all considered cases, both mixture and temperature
stratification were observed. Simulations of zero-dimensional chemical
reactors demonstrated that the correct prediction of such a stratification
is mandatory for an accurate estimate of auto-ignition timing.
In the present work, URANS simulations of under-expanded hy-
drogen jets are carried on with the following objectives: (1) provide
an efficient and accurate open-source numerical tool suitable for fast
engine simulations; (2) investigating the capability of the URANS model
to predict the physical mechanism of jet injection and air–fuel mixing;
(3) assessing the influence of the spatial order of accuracy of the
numerical scheme on the solution, considering schemes from second-
to fourth-order of accuracy. In particular, we have considered two
schemes already implemented in the standard distribution of Open-
FOAM, namely, the linear-upwind scheme and the cubic scheme, for
comparison purpose. Then, we have considered the class of weighted
essentially non-oscillatory schemes (WENO), which is a class of scheme
particularly suited for compressible flows with shocks [50,51]. These
schemes have been implemented in a ad-hoc library [52] which is not
contained in the standard distribution of OpenFOAM and has been
adapted to the present test case during the present work. Among
the WENO schemes, we have chosen to employ three schemes with
second-, third- and fourth-order accuracy in space. Previous works in
the literature do not analyze the performance of high-order-accurate
schemes for solving the RANS equations in the case of under-expanded
hydrogen jets.
The organization of the paper is the following: in Section 2, the com-
putational approach is described. Section 3 provides the details of the
simulation set-up. In Section 4, the results are discussed in comparison
to experimental and numerical data available in the literature. Finally,
in Section 5 some conclusions are drawn, and future work is discussed.
2. Computational approach
2.1. Governing equations
The Favre–Reynolds averaged Navier–Stokes equations for a multi-
component non-reacting gas mixture have been solved, with 𝑘 − 𝜔
SST [53] turbulence closure model involving the solution of two ad-
ditional transport equations for the turbulent kinetic energy, 𝑘, and the
specific dissipation rate, 𝜔:
𝜕𝜌
𝜕 𝑡 +
𝜕𝜌 ̃ 𝑢𝑗
𝜕 𝑥𝑗
=0, (1)
𝜕𝜌 ̃ 𝑢𝑖
𝜕 𝑡 +
𝜕𝜌 ̃ 𝑢𝑗 ̃ 𝑢𝑖
𝜕 𝑥𝑗
= − 𝜕𝑝
𝜕 𝑥𝑖
− 𝜕
𝜕 𝑥𝑗
[
𝜏𝑖𝑗 + 𝜏𝑅
𝑖𝑗
]
, (2)
𝜕𝜌 ̃𝐻
𝜕 𝑡 +
𝜕𝜌 ̃ 𝑢𝑗 ̃𝐻
𝜕 𝑥𝑗
= 𝜕𝑝
𝜕 𝑡 + 𝜕
𝜕 𝑥𝑗
[( ̃𝜆
𝑐𝑝
+ 𝜇𝑡
𝑃 𝑟𝑡
)
𝜕 ̃ℎ
𝜕 𝑥𝑗
]
+ (3)
+ 𝜕
𝜕 𝑥𝑗
[
+ ̃ 𝑢𝑖
(
𝜏𝑖𝑗 + 𝜏𝑅
𝑖𝑗
)]
,
𝜕𝜌 ̃𝑌𝑘
𝜕 𝑡 +
𝜕𝜌 ̃ 𝑢𝑗 ̃𝑌𝑘
𝜕 𝑥𝑗
= 𝜕
𝜕 𝑥𝑗
[(
𝜌 ̃𝐷𝑘 + ̃ 𝜇𝑡
𝑆 𝑐𝑡
) 𝜕 ̃𝑌𝑘
𝜕 𝑥𝑗
]
, (4)
𝜕𝜌̃𝑘
𝜕 𝑡 +
𝜕𝜌 ̃ 𝑢𝑗 ̃𝑘
𝜕 𝑥𝑗
=𝑘 + 𝑃 +
𝑘 − 𝑃 −
𝑘 , (5)
𝜕𝜌 ̃ 𝜔
𝜕 𝑡 +
𝜕𝜌 ̃ 𝑢𝑗 ̃ 𝜔
𝜕 𝑥𝑗
=𝜔 + 𝑃 +
𝜔 − 𝑃 −
𝜔 . (6)
The viscous and Reynolds stress tensors are computed as
𝜏𝑖𝑗 + 𝜏𝑅
𝑖𝑗 = ( ̃ 𝜇+ 𝜇𝑡)
( 𝜕 ̃ 𝑢𝑖
𝜕 𝑥𝑗
+
𝜕 ̃ 𝑢𝑗
𝜕 𝑥𝑖
− 2
3 𝛿𝑖𝑗
𝜕 ̃ 𝑢𝑘
𝜕 𝑥𝑘
)
− 2
3 𝜌̃𝑘𝛿𝑖𝑗 . (7)
𝐻 indicates the total enthalpy, whereas the enthalpy ℎ is computed
as ℎ =
𝑁𝑠∑
𝑘=1
𝑌𝑘ℎ0
𝑘 +
𝑁𝑠∑
𝑘=1 ∫
𝑇
𝑇0
𝑌𝑘 𝑐𝑝,𝑘(𝑇 )𝑑 𝑇 , being 𝑌𝑘 the mass fraction of
species 𝑘 with 𝑘 = 1, … 𝑁𝑠 − 1. The function 𝑐𝑝,𝑘(𝑇 ) is obtained from
the JANAF tables [54] and the equation of state of perfect gases has
been employed. 𝑃 𝑟 and 𝑆 𝑐 indicate the Prandtl and Schmidt numbers,
respectively. 𝜆𝑘 = (𝑐𝑝𝜇∕𝑃 𝑟)𝑘 is the thermal conductivity of species 𝑘;
𝐷𝑘 = (𝜈∕𝑆 𝑐)𝑘 is the mass diffusivity of species 𝑘. ,  +,  −, repre-
sent the diffusion, production and destruction terms in the transport
equations of 𝑘 and 𝜔 as described by [53].
Three species are considered in the present work, namely, hydrogen,
oxygen and nitrogen. Pure hydrogen is injected in air, which is com-
posed of a mixture of oxygen and nitrogen with 22% and 78% molar
fraction, respectively.
The dynamic viscosity, 𝜇𝑘, for each species 𝑘 is evaluated using
Sutherland’s law,
𝜇𝑘 = 𝐴𝑆 ,𝑘
𝑇
1 + 𝑇𝑆 ,𝑘∕𝑇 , (8)
where 𝐴𝑆 ,𝑘 is the Sutherland coefficient, 𝑇𝑆 ,𝑘 is the Sutherland tem-
perature and the dynamic viscosity of the mixture is computed as 𝜇 =∑𝑁𝑠
𝑘=1 𝑌𝑘 𝜇𝑘.
The thermal conductivity of the mixture is computed using the
Eucken approximation [55],
𝜆 = 𝜇 𝑐𝑣(1.32 + 1.37 𝑅∕𝑐𝑣), (9)
where 𝑐𝑣 is the mixture heat coefficient at constant volume computed as
𝑐𝑣 = 𝑐𝑝 −𝑅, where 𝑅 = ∑𝑁𝑠
𝑘=1 𝑌𝑘 𝑅𝑘 and 𝑐𝑝 = ∑𝑁𝑠
𝑘=1 𝑌𝑘 𝑐𝑝,𝑘. Assuming unity
Lewis number for each species (𝑃 𝑟𝑘 = 𝑆 𝑐𝑘), the species mass diffusivity
𝐷𝑘 is computed using the thermal conductivity as 𝐷𝑘 = 𝐷 = 𝜆∕(𝜌𝑐𝑝).
2.2. WENO schemes
Weighted Essentially Non-Oscillatory (WENO) schemes [50,51] are
based on a polynomial reconstruction of any variable 𝛷 over each cell
𝑖 of the computational domain, having volume 𝑉𝑖, 𝛷𝑖 = 𝑝𝑖(⃗𝜉). In order
to obtain a robust scheme with the desired order of accuracy, scaling
effects due to the different size and shape of the cells must be reduced.
This can be done by mapping the reconstruction from the Cartesian
coordinates (𝑥, 𝑦, 𝑧) system into a scaled local reference space described
by ⃗𝜉 = ⃗𝜉(𝑥, 𝑦, 𝑧) for each cell 𝑖. The cell average value is computed as:
𝛷𝑖 = 1
𝑉 ′
𝑖 ∫𝑉 ′
𝑖
𝑝𝑖(⃗𝜉)𝑑 ⃗𝜉 , (10)
where 𝑉 ′ is the volume of the cell in reference space. Each polynomial
can be expressed as a combination of 𝐾 local basis functions 𝛺𝑘, 𝐾
depending on the degree 𝑟 of the polynomial 𝑝𝑖, as
𝑝𝑖(⃗𝜉) = 𝛷𝑖 +
𝐾∑
𝑘=1
𝑎𝑘 𝛺𝑘(⃗𝜉), (11)
International Journal of Hydrogen Energy 96 (2024) 849–859 
852

<!-- PDF_PAGE: 5 -->

G. Caramia et al.
where, for the d-dimensional space
𝐾 = 1
𝑑!
𝑑∏
𝑛=1
(𝑟 + 𝑛) − 1. (12)
The basis functions 𝛺𝑘 have to be suitably chosen in order to satisfy
Eq. (10), which means that the basis functions must have null mean
value over 𝑉𝑖. Such a condition is satisfied by the following definition
of the basis functions,
𝛺𝑘(⃗𝜉) = 𝛹𝑘(⃗𝜉) − 1
𝑉 ′
𝑖 ∫𝑉 ′
𝑖
𝛹𝑘(⃗𝜉)𝑑 ⃗𝜉 , 𝑘 = 1, … ..., 𝐾 , (13)
where 𝛹𝑘 is a basis of orthogonal polynomials. which can be obtained
by a Taylor series expansion around the center of 𝑉 ′
𝑖 [56].
For each cell 𝑖, WENO schemes employ 𝑁𝑠𝑡 stencils, 𝑆𝑚, 𝑚 =
1, … ..𝑁𝑠𝑡, to compute, by a weighted convex non-linear combination,
the polynomial reconstruction [57],
𝑝𝑖,𝑤𝑒𝑛𝑜(⃗𝜉) =
𝑁𝑠𝑡∑
𝑚=1
𝜔𝑚 𝑝𝑖,𝑚(⃗𝜉). (14)
For each stencil 𝑆𝑚, appropriate neighboring cells 𝑉𝑗 , 𝑗 = 0, … , 𝐽𝑚𝑎𝑥
are considered to construct the polynomial 𝑝𝑚. The details of the
computation of the weights 𝜔𝑚 can be found in [57,58].
The final WENO formulation is obtained by substituting Eq. ( 11)
in Eq. (14):
𝑝𝑖,𝑤𝑒𝑛𝑜(⃗𝜉) = 𝛷𝑖 +
𝐾∑
𝑘=1
( 𝑁𝑠𝑡∑
𝑚=1
𝜔𝑚𝑎(𝑚)
𝑘
)
𝛺𝑘(⃗𝜉). (15)
The coefficients 𝑎(𝑚)
𝑘 are computed by imposing that the averaged
values 𝛷𝑗 in all cells 𝑉𝑗 of the stencil 𝑆𝑚 are recovered by the corre-
sponding cell averages of the polynomial 𝑝𝑚,
𝛷𝑗 = 1
𝑉 ′
𝑗 ∫𝑉 ′
𝑗
𝑝𝑚(⃗𝜉)𝑑 ⃗𝜉 , 𝑗 = 1...., 𝐽𝑚𝑎𝑥. (16)
From this constraint an overdetermined system of equations is
obtained,
𝛷𝑗 − 𝛷𝑖 =
𝐾∑
𝑘=1
𝑗 𝑘𝑎(𝑚)
𝑘 , 𝑗 = 1...., 𝐽𝑚𝑎𝑥. (17)
The matrix  can be evaluated only once at the beginning of the
computation. Since 𝐽𝑚𝑎𝑥 > 𝐾 for stability reasons, the matrix  is (slim)
rectangular and the system in Eq. (17) is overdetermined. Therefore,
the coefficients 𝑎(𝑚)
𝑘 are obtained solving a least-square minimization
problem by computing the Moore–Penrose pseudo-inverse matrix of ,
†, by a singular value decomposition. The pseudo-inverse matrices
is computed for each stencil in the pre-processing stage because the
matrix  is independent of the solution. Then, at each time step and
for each stencil, † is employed to compute the coefficients 𝐚(𝑚) =
†
(
𝛷𝑗 − 𝛷𝑖
)
.
2.3. Semi-implicit WENO-based convection schemes
In the finite volume method, convective terms are discretized by
integrating over the volume of each cell and using Gauss’s theorem
for transforming the volume integrals in a sum of surface integrals
extended to all 𝐹𝑖 faces of the cell 𝑉𝑖, having area 𝐴𝑙. Considering the
generic transported variable 𝛷, one has
∫𝑉𝑖
∇ ⋅ ⃗ 𝑢 𝛷 =
𝐹𝑖∑
𝑙=1 ∫𝐴𝑙
⃗ 𝑛𝑙 ⋅ ⃗ 𝑢 𝛷 𝑑 𝐴𝑙 =
𝐹𝑖∑
𝑙=1 ∫𝐴𝑙
𝐹𝑙 𝑑 𝐴𝑙, (18)
where 𝐹𝑙 represents the numerical flux through each cell face with unit
normal ⃗ 𝑛𝑙.
For high-order schemes, the surface integrals in the above equation
needs to be evaluated with a Gaussian integration of higher order.
An average value for the velocity at the face is considered, which is
equivalent to a linearization of Eq. (18). Substituting the polynomial
expressions for 𝛷 in Eq. (18) gives for any face 𝐴𝑙 of cell 𝑖 the numerical
flux.
The surface integrals of the basis functions, employed to obtain
such fluxes, are pre-computed by decomposing the faces into triangles
and using Gaussian quadrature rules of appropriate order. Then, the
evaluation of convective terms at run-time consists only of a sum of
products extended over the WENO stencils.
For a high-order upwind reconstruction, the numerical flux at each
face 𝑙 shared by two cells 𝑖 and 𝑗 is computed as follows:
𝐹𝑙 = ⃗ 𝑛𝑙 ⋅ ⃗ 𝑢 𝛷 =
⎧
⎪
⎨
⎪⎩
𝛷−, if ⃗ 𝑛𝑙 ⋅ ⃗ 𝑢 > 0,
𝛷+, if ⃗ 𝑛𝑙 ⋅ ⃗ 𝑢 < 0,
(19)
with
𝛷− = 𝛷𝑖 +
𝐾∑
𝑘=1
⎛
⎜
⎜⎝
𝑁𝑠𝑡,𝑖∑
𝑚=1
𝜔𝑚𝑎(𝑚)
𝑘
⎞
⎟
⎟⎠ ∫𝐴′
𝑙
𝛺𝑘,𝑖(⃗𝜉−) 𝑑 𝐴′
𝑙, (20a)
𝛷+ = 𝛷𝑗 +
𝐾∑
𝑘=1
⎛
⎜
⎜⎝
𝑁𝑠𝑡,𝑗∑
𝑚=1
𝜔𝑚𝑎(𝑚)
𝑘
⎞
⎟
⎟⎠ ∫𝐴′
𝑙
𝛺𝑘,𝑗 (⃗𝜉+) 𝑑 𝐴′
𝑙, (20b)
where ⃗𝜉+ and ⃗𝜉− represent the reference frames relative to the upwind
cell.
The WENO method is implemented in OpenFoam using a deferred
correction approach [52] by combining an implicit first-order upwind
scheme with an explicit high-order correction term. The first-order part
of the scheme, represented by the first term at the right-hand-side of
equations ((20a), ( b)), provides stability to the algorithm due to its
diagonal dominance. Finally, WENO schemes are not strictly bounded,
so that the explicit high-order correction term can induce spurious
oscillations in the solution, especially in the presence of high flow
gradients. In order to overcome this problem, a flux limiting strategy
can be adopted [59] to render the scheme total variation diminishing
for the scalar conservation law, introducing the limiter function 𝜃𝑖 ∈
[0, 1] (see [52] for details), which multiplies the second term at right-
hand-side of equations ((20a), (b)). This semi-implicit WENO scheme
has been adapted to the PIMPLE algorithm in OpenFOAM (see [52]
for details on implementation). PIMPLE pressure–momentum coupling
procedure results from the merging of SIMPLE [60,61] and PISO [62]
algorithms to leverage the strengths of both PISO and SIMPLE methods
ensuring robustness in handling unsteady transonic flows.
3. Simulation set-up
The simulated injection system consists of a high-pressure hydrogen
tank and a low pressure chamber containing air, linked by a converging
nozzle with exit diameter 𝐷 = 1.5 mm, as shown in Fig. 2. The height
of the low pressure chamber, equal to 15 diameters, has been chosen in
order to be far enough from the nozzle so that the numerical influence
of the boundary on the jet dynamics is negligible. The nozzle geometry,
provided in Fig. 3, is that employed by [43] for their experimental
measurements, considered also by [33] for numerical simulations.
The low-pressure chamber is kept for all simulations at 98.37 kPa,
whereas the initial temperature of the high pressure tank and of the
low pressure chamber is equal to 295.4 K and 296 K, respectively,
and the initial velocity is zero. The injection system has a cylindrical
symmetry, so that the computations have been performed using an
axisymmetric model. The left boundary of the high pressure tank is
considered as a (normal) flow inlet with given stagnation pressure and
stagnation temperature. The top and the right boundaries of the low
pressure chamber are treated as flow outlet with a prescribed pressure.
A slip boundary with adiabatic-wall condition has been applied at the
nozzle boundary in order to avoid solving the boundary layer . Such a
condition has been applied in previous studies for similar nozzle flow
configurations and is allowed by the value of the Knudsen number
inside the nozzle being 10−3 < 𝐾 𝑛 < 10−2 [33]. Finally, in order
International Journal of Hydrogen Energy 96 (2024) 849–859 
853

<!-- PDF_PAGE: 6 -->

G. Caramia et al.
Fig. 2. Geometry of the injection system.
to avoid the formation of any artificial boundary layers, the top and
right boundaries of the pressure tank and the left boundary of the air
chamber are considered as slip adiabatic walls.
4. Results
4.1. Solution sensitivity to grid and polynomial degree
The sensitivity of the numerical solution to the grid resolution and
to the degree of the polynomial reconstruction has been studied by
simulating the case with 𝑁 𝑃 𝑅 = 10 and considering four grids and five
polynomial degrees. A set of four grids, composed of quadrilateral cells,
with different size has been considered for the simulations. The grids
are categorized by the number of square cells employed to discretize
the exit section of the nozzle: 10, 20, 40, and 80, respectively; they
will be referred to as D10, D20, D40, and D80, respectively. In the air
chamber, starting from the nozzle exit, the cells are stretched in the
axial direction by a factor 1.02 and are stretched in the radial direction
by a factor 1.13. In the pressure tank, starting from the nozzle inlet,
the cells are stretched in the axial direction by a factor 1.13 and are
stretched in the radial direction by a factor 1.11. The overall number of
cells for each grid is the following: D10, 4755; D20, 13596; D40, 50905;
D80, 452491. The minimum grid size, in the region of the nozzle exit,
ranges from 0.15 mm of the D10 grid to 18.75 μm of the D80 grid. The
lower grid size (D40 and D80) used in this study are comparable to
those employed for computing under-expanded jets by LES [33,63].
Concerning the spatial discretion schemes, three WENO schemes
have been employed, with degree of the polynomial reconstruction
equal to 1 (WENO1), 2 (WENO2), and 3 (WENO3), which correspond to
second-, third- and fourth-order accuracy in space, respectively. The re-
sults obtained by these schemes are compared with the Linear Upwind
(LU) and Cubic reconstruction (CU) schemes available in the standard
distribution of the OpenFOAM solver for the URANS equations, which
are second- and fourth-order-accurate in space, respectively.
4.1.1. Flow field analysis
Fig. 4(a)–4(e) provide a local view of the Mach number contours
and of the temperature contours obtained using the D40 grid for all
the spatial discretization schemes presented above. For the considered
value of 𝑁 𝑃 𝑅 = 10, the jet features a single barrel shock terminating
with a normal shock, the Mach disk, in the near nozzle region.
The comparison among the figures shows the effect of increasing
the accuracy for the numerical scheme. In particular, the Mach number
contours show a higher acceleration of the flow inside the barrel
shock between the LU scheme and the WENO1 scheme (which are
both second-order-accurate). The acceleration is slightly higher for
WENO2 and WENO3 schemes inside the barrel shock and, especially
for WENO3 scheme, is higher in the region following the Mach disk.
The comparison among the temperature contours confirms that the
standard LU scheme has higher numerical dissipation. The CU scheme
provides a higher accuracy (fourth-order accuracy in theory) but shows
Fig. 3. Geometry of the nozzle [43].
some spurious oscillations in the supersonic acceleration region inside
the barrel shock. Only the WENO2 and WENO3 schemes are capable
of capturing the instability of the slip lines with sufficient accuracy,
while capturing the discontinuities without an evident dispersion error.
Moreover, the CU scheme and the WENO3 scheme can capture the
coherent structures in the central part of the jet, as shown by the
temperature contours in Fig. 4(b) and 4(e).
Fig. 5 provides the density gradient contours, ∣ ∇𝜌 ∣, which are
in good qualitative agreement with the Schlieren image of Ref. [43]
and with the time-averaged contours of the LES shown in Fig. 4b
of Ref. [33]. Using WENO2 and WENO3 schemes, the jet width is
predicted in satisfactory agreement with the experiments (see Sec-
tion 4.1.2) for further details. The density gradient results show that
the reflected shock at the triple point is inclined at about 28◦ with
respect to the nozzle axis, close to the values reported in Refs. [33,63].
Using WENO2 and WENO3 schemes the structure of the barrel shock
is well captured; in particular, the intercepting shock, the Mach disk,
the oblique shock and their interaction at the triple point are captured
without spurious oscillations. The separation between the two slip
lines at the extrema of the reflected shock is clearly evident in Fig. 5,
originating the co-annular structure of the jet, which is typical of high
NPRs [63]. The snapshots show that the instability mechanism of the
these slip lines, outside the barrel shock, is captured by the WENO2
and WENO3, in good agreement with the experimental [43] and LES
results [33,63]. Coarser grids (not shown) cannot capture the vortex
shedding even using these two schemes.
The high density gradient, shown in Fig. 5, at the jet boundary
between the nozzle exit and the Mach disk, reveals a strong momentum
exchange between hydrogen and air. This region corresponds to a high
concentration gradient, as shown in Fig. 9 (center), which indicates that
air is entrained by the hydrogen jet ahead of the Mach disk. The mixing
region extends downstream along the jet boundary. It develops in a
supersonic flow region, by-passing the Mach disk. This phenomenon
was observed by Ruggles and Ekoto [43], who noticed brightness
differences (density gradient) in their Schlieren images and suggested
that they were due to gradients of the mixture fraction. The LES study
in Ref. [33] also interpreted the high density gradient in this region as a
high level of hydrogen–air mixing. Therefore, our simulations confirm
that hydrogen and air mix outside the boundaries of the barrel-shock,
clearly showing that part of the hydrogen does not flow through the
Mach disk.
For the considered value of 𝑁 𝑃 𝑅 = 10, only one shock cells is
observed in the flow. Fig. 6 shows the Mach number distribution along
the axis of the jet computed by the WENO2 and WENO3 schemes,
the axial distance for the nozzle exit (z) being non-dimensionalized by
the radius of the nozzle (r). The maximum value of the Mach number
within the under-expanded jet is equal to 3.96. This value is in good
agreement with the results of Hamzehloo [21]. Downstream of the
Mach disk, the flow accelerate and decelerates several times. It achieves
a first peak value of about 𝑀 = 0.9 and a second peak value of about
𝑀 = 0.8. Then, there is a smooth acceleration to supersonic values till
𝑧∕𝑟 ≈ 20 followed by a deceleration. This trend is consistent with the
LES results of Hamzehloo [21].
International Journal of Hydrogen Energy 96 (2024) 849–859 
854

<!-- PDF_PAGE: 7 -->

G. Caramia et al.
Fig. 4. Mach number contours (top) and temperature [K] contours (bottom) computed
by different numerical schemes (𝑁 𝑃 𝑅 = 10).
4.1.2. Mach disk height and width
Tables 1 and 2 provide the Mach disk height and width, respec-
tively, for twenty combinations of grids and schemes.
Fig. 5. Density gradient contours computed by the WENO2 (top) and WENO3 (bottom)
schemes (𝑁 𝑃 𝑅 = 10).
Fig. 6. Mach number distribution along the axis of the jet computed by the WENO2
and WENO3 schemes (𝑁 𝑃 𝑅 = 10).
Table 1
Mach disk height for different grids and schemes [mm].
𝐷10 𝐷20 𝐷40 𝐷80
LU 3.62 3.62 3.23 3.07
CU 3.67 3.51 3.23 3.11
WENO1 3.65 3.31 3.18 3.27
WENO2 3.74 3.33 3.14 3.17
WENO3 3.79 3.28 3.10 3.13
It appears that when the height increases (decreases), the width
decreases (increases). The data show a good convergence of the results
when increasing the grid resolution and the accuracy of the numerical
scheme. The two finer grids (D40 and D80) and the three more accurate
schemes (CU, WENO2 and WENO3) estimate the height of the Mach
disk between 3.10 and 3.23 mm and the Mach disk width in the range
1.10–1.33 mm. These numerical results are in good agreement with
the experimental data of Ref. [43] for the case with 𝑁 𝑃 𝑅 = 10, who
measured a Mach disk height equal to 3.05 mm and a Mach disk width
of 1.30 mm using mean Schlieren images. Using the grid D40 with
WENO3, the average Mach disk height is 𝐻𝑑 = 3.10 mm, which is very
close to the value obtained using LES in Ref. [33], 𝐻𝑑 = 3.09 mm, and
corresponds to 𝐻𝑑 ∕𝐷 = 2.06. Concerning the value of the Mach disk
width, 𝑊𝑑, using the grid D40 with WENO3, we obtain 𝑊𝑑 = 1.27 mm,
which is close to the experimental value of [43], 𝑊𝑑 = 1.30 mm, but
smaller than the value obtained using LES by [21], 𝑊𝑑 = 1.34 mm.
𝑊𝑑 determines the separation between the slip lines and characterizes
the structure of highly under-expanded jets with the presence of two
co-annular shear layers.
Based on the results presented in this section, we decided to employ
the D40 grid resolution for the computations discussed in the following
sections, combined with either the WENO2 or the WENO3 scheme.
4.2. Varying the NPR
Fig. 7 shows the height of the Mach disk versus the square root of
the nozzle pressure ratio. The present results (blue line) are computed
International Journal of Hydrogen Energy 96 (2024) 849–859 
855

<!-- PDF_PAGE: 8 -->

G. Caramia et al.
Table 2
Mach disk width for different grids and schemes [mm].
𝐷10 𝐷20 𝐷40 𝐷80
LU 0.72 0.58 1.08 1.25
CU 0.80 0.70 1.10 1.16
WENO1 0.78 0.89 1.25 1.36
WENO2 0.80 0.99 1.25 1.18
WENO3 1.09 1.15 1.27 1.33
Fig. 7. Mach disk height versus the nozzle pressure ratio. (For interpretation of the
references to color in this figure legend, the reader is referred to the web version of
this article.)
for five values of 𝑁 𝑃 𝑅 = 3.5, 6.5, 8.5, 10, 30. The corresponding
computed values of 𝐻𝑑 = 1.57 mm, 2.42 mm, 2.82 mm, 3.10 mm, 5.85 mm,
respectively, are compared to the experimental data of Ruggles and
Ekoto [43] (cross symbol) for 𝑁 𝑃 𝑅 = 10 and to the numerical results
of Refs. [33] (orange line) and [64] (gray line). All data are very
close and the slope of the lines are also in very good agreement. The
present numerical results confirm the linear correlation expressed by
the following equation
𝐻𝑑 ∕𝐷 = 𝐶𝐻
√
𝑁 𝑃 𝑅, (21)
with a coefficient 𝐶𝐻 ≈ 0.72, which is in good agreement with the
data available in the literature. The value of the coefficient 𝐶𝐻 has
been determined experimentally or numerically by several authors.
According to the experimental analysis of Ref. [65], 𝐶𝐻 = 0.67. By
using LESs, Hamzehloo and Aleiferis [33] find that 𝐶𝐻 = 0.67 can be
employed for 10 ≤ 𝑝0∕𝑝∞ ≤ 25, whereas, for hydrogen jets with higher
NPR they suggest a higher value of the coefficient 𝐶𝐻 = 0.71. According
to Vuorinen et al. [63], for 𝑝0∕𝑝∞ ≤ 10, 𝐶𝐻 = 0.62 should is a more
accurate value. These data indicate that the coefficient 𝐶𝐻 probably is
an increasing function of NPR.
Fig. 8 shows the Mach number distribution along the axis of the
jet for the five values of the NPR. As well-known, see for example
Ref. [40], depending on the value of NPR, after the Mach disk, the flow
can accelerate and decelerate several times, generating several shock
cells. For the present hydrogen injection in air, three shock cells are
obtained for the case of 𝑁 𝑃 𝑅 = 3.5, two shock cells are obtained for
𝑁 𝑃 𝑅 = 6.5 and 𝑁 𝑃 𝑅 = 8.5, and one shock cell for higher values of the
NPR.
Considering the Mach disk width, the results indicate a higher level
of sensitivity to NPR in comparison to its height. The computed values
of 𝑊𝑑 for the above five values of the 𝑁 𝑃 𝑅 are 0.075 mm, 0.648 mm,
0.986 mm, 1.270 mm, 3.06 mm, respectively. The correlation suggested
by Antsupov [66], namely,
𝑊𝑑
𝐷 = 𝑙 𝑜𝑔
( 𝑝1
𝑝∞
)5∕2
− 3
4 , (22)
where 𝑝1 is the pressure at the nozzle exit, provides the following
results: 𝑊𝑑 = 1.135 mm, 1.377 mm, 3.173 mm, for 𝑁 𝑃 𝑅 = 8.5, 10, 30,
respectively. These values are in good agreement with those predicted
by the present numerical method. Moreover, for the same three values
of NPR, using the numerical results obtained by the present URANS
simulation, the values of the constant 𝜁 of the correlation proposed by
Velikorodny and Kudriakov [67],
𝑊𝑑 = 𝜁 𝐻𝑑
√
1 − 𝛾 + 1
𝛾
(𝛾 + 1
𝛾 − 1
)−1∕2
, (23)
where 𝛾 = 1.41 is the specific heat ratio, are estimated to be equal
to 0.644, 0.702, 0.963, respectively, for the above three values of the
NPR. A similar trend is reported by Hamzehloo et al. [21] for the 𝜁
coefficient.
Snapshots of the hydrogen mass fraction contours are shown in
Fig. 9 for three values of 𝑁 𝑃 𝑅 = 8.5, 10, 30. Streamlines in the core
region are superposed to the contours. It appears that hydrogen and air
begin to mix before the location of the Mach disk along the shear layer
separating the two fluids, which is close to the jet boundary. Due to the
high diffusivity of the hydrogen, the jet is quite voluminous. The spatial
distribution of the hydrogen mass fraction is very similar between the
two jets with 𝑁 𝑃 𝑅 = 8.5 and 𝑁 𝑃 𝑅 = 10. On the other hand, for 𝑁 𝑃 𝑅 =
30, the hydrogen mass fraction distribution clearly shows a wider jet
with a more extended region in which the hydrogen concentration is
close to one. In this last case, the jet penetration is also remarkably
higher than that of the two lower NPRs. Our computations confirm
that the shear layer thickness, 𝛿, namely, the distance between the
two slip lines departing from the edge of the reflected shock, reduces
for increasing NPR. The values of 𝛿 are about 0.341 mm, 0.320 mm,
0.250 mm, respectively. For the case 𝑁 𝑃 𝑅 = 8.5, the value of 𝛿 is in
satisfactory agreement with the one reported by Hamzehloo et al. [21]
and with the value of 0.25 𝐷 obtained by Vouroinenet al. [63] for
under-expanded nitrogen jets.
4.3. Structure of the jet in the far field (self-similarity)
The structure of the jet in the far-field is investigated for the case
with 𝑁 𝑃 𝑅 = 10, for which experimental data are available, using
a larger computational domain extended to 150 𝐷 in the streamwise
direction. The maximum grid resolution corresponds to that of the D40
grid. The mesh is locally refined in the jet region and is made of about
217000 cells. Fig. 10 shows the inverse mass fraction distribution along
the centerline of the jet versus the axial abscissa divided by the radius
of the nozzle.
The solid red line represents the numerical results obtained by the
present WENO3 scheme, whereas the dashed black line corresponds
to the numerical results obtained by Anaclerio et al. [64] solving the
RANS equations. The blue circles are the experimental data of Ruggles
and Ekoto [43] for the same nozzle geometry, whereas, the pink
rhombuses indicate the experimental data of Ruggles and Ekoto [68]
for a rectangular nozzle with aspect ratio equal to eight, for the same
value of the NPR. The present numerical results confirm the linear
decay rates observed by Xiao et al. [69] and Ruggles and Ekoto [43] but
they underestimate the hydrogen mass fraction along the centerline of
the jet with respect to the experimental data with a maximum error of
30%. Very similar results are obtained by the RANS solver of Anaclerio
et al. [64]. This behavior probably indicates a limit of the considered
RANS model linked to the diffusion process model. Fig. 11 shows the
jet half width versus the axial abscissa.
The jet half width is defined as the full width at half-maximum
for the hydrogen concentration radial profiles at each axial location.
The filled circles represent the present numerical results and the empty
circles are the experimental data of Ruggles and Ekoto [43]. The
numerical data correctly provide the linear behavior. The dotted lines
indicate the corresponding best fit lines, whose slopes, 0.096 for the
numerical data and 0.0833 for the experimental data, are in reasonable
agreement. However, the numerical data overestimate the jet width
with a maximum error of 30%.
International Journal of Hydrogen Energy 96 (2024) 849–859 
856

<!-- PDF_PAGE: 9 -->

G. Caramia et al.
Fig. 8. Mach number distribution along the axis of the jet for several values of the NPR.
Fig. 9. Hydrogen mass fraction contours: 𝑁 𝑃 𝑅 = 8.5 (top); 𝑁 𝑃 𝑅 = 10 (middle);
𝑁 𝑃 𝑅 = 30 (bottom).
Fig. 10. Reciprocal mean mass fraction distribution at the centerline versus normalized
axial distance.
Richards and Pitts [70] have found experimentally that the atmo-
spheric jet diffusion for several of gases obeys Gaussian self-similarity
that can be modeled by the following equation for the mean mass
concentration
𝑌 (𝑧, 𝜂) = 1
𝐾𝑐
𝑟𝜖
(𝑧 − 𝑧0,𝑗 ) 𝑒𝑥𝑝(−59 𝜂2), (24)
Fig. 11. Jet half width versus the normalized axial distance from the nozzle exit.
where 𝜂 = 𝑟∕(𝑧 − 𝑧0,𝑗 ); 𝑧0,𝑗 is the location where the jet half-width
becomes zero (momentum flux virtual origin). 𝑟𝜖 is the effective radius,
namely, the radius of a hypothetical jet with ambient density and
the same mass flux and momentum flux of the jet under considera-
tion [70]. The centerline decay-rate constant, 𝐾𝑐 = 0.105, as measured
by Richards and Pitts [70], has been used for the present comparison.
Fig. 12 shows the normalized mass concentration radial distribu-
tions at eleven axial locations from 𝑧 = 37.5 mm to 𝑧 = 187.5 mm.
The hydrogen concentration is normalized with respect to its centerline
value at each axial location. On the abscissa, the non-dimensional
radial distance 𝜂 is reported. The empty circles represent the numerical
data, which reasonably collapse over each other, as expected due to
the normalization [70]. The solid lines indicate the normalized radial
experimental data of Ruggles and Ekoto [43] coinciding with the
correlation (24) of Richards and Pitts [70]. The green region represents
the dispersion of the experimental data. Numerical data are in overall
good agreement with experimental one. However, the data indicate that
the computed hydrogen concentration distributions are slightly more
flat than the experimental one.
5. Conclusions
In the present study, a very robust and accurate multi-species
URANS solver is proposed to investigate turbulent under-expanded
hydrogen jets for engine applications. Robustness is achieved by the use
of the PIMPLE approach, which allows one to handle flows with a wide
range of variation of the Mach number, as the one considered here. Nu-
merical accuracy is enhanced by using third- and fourth-order-accurate
WENO scheme, which guarantees excellent shock-capturing capabili-
ties. Two-dimensional axisymmetric computations are performed with
different values of the nozzle pressure ratio using the nozzle config-
uration proposed by Ruggles and Ekoto [43] for their experimental
International Journal of Hydrogen Energy 96 (2024) 849–859 
857

<!-- PDF_PAGE: 10 -->

G. Caramia et al.
Fig. 12. Normalized radial mass concentration distributions at different axial locations.
(For interpretation of the references to color in this figure legend, the reader is referred
to the web version of this article.)
study. The results are validated versus the experimental data and the
LES results available in the literature (Hamzehloo et al. [21]). The
axisymmetric URANS solver is shown to be very efficient compared
to LES as a design approach of under-expanded injection systems. The
details of the under-expanded jet structure close to the nozzle exit, such
as the dimensions of barrel shock and the of the reflecting shock, are
predicted with very good accuracy with respect to experimental data.
The results obtained in our study show that third- and fourth-order-
accurate WENO schemes are capable of providing clear advantages in
capturing flow instabilities of the shear layers with respect to second-
order-accurate schemes, improving the prediction of the jet diffusion.
The present study indicates also that the characteristic geometry of
the Mach disk and the relevant average properties of the air–fuel
mixing dynamics are consistent with respect to LES predictions and are
obtained with a remarkable saving of computational time compared to
LES due to the two-dimensional axisymmetric approach. The numerical
results reproduce the correct linear distribution of the reciprocal mean
hydrogen mass fraction and of the jet half width versus the normalized
axial distance from the nozzle exit along the centerline of the jet.
Numerical results concerning the hydrogen concentration distributions
and the auto-similarity properties of the jet are discussed. The analysis
of these data, which are rarely available in the literature, revealed some
quantitative discrepancies compared to the experimental data. Among
the possible causes of these discrepancies, there is the assumption of
unity Lewis number.
This analysis enabled us to accurately evaluate the error margins of
the numerical model in relation to the hydrogen–air mixing process.
In fact, these features are of fundamental relevance towards the de-
velopment of an accurate model of the combustion process, useful to
investigate the use of hydrogen in clean DI engines for future mobility.
Future work will be firstly devoted to the implementation of more
accurate diffusion models to assess their impact on results and compu-
tational cost. Moreover, we shall investigate an improved turbulence
modeling approach using data assimilation techniques to match in an
optimal way those experimental data which cannot be predicted with
high quantitative fidelity using standard turbulence model.
CRediT authorship contribution statement
Giovanni Caramia: Writing – review & editing, Visualization, Val-
idation, Software, Methodology, Investigation. Riccardo Amirante:
Funding acquisition. Pietro De Palma: Writing – original draft, Vali-
dation, Supervision, Methodology, Investigation, Formal analysis, Con-
ceptualization.
Declaration of competing interest
The authors declare that they have no known competing finan-
cial interests or personal relationships that could have appeared to
influence the work reported in this paper.
Acknowledgments
This work has been partly supported by: (1) the grant PRIN
2022W2FEZ8 DHyCE-HD of the Italian Ministry of University and
Research (MUR); (2) the project NEST - Network 4 Energy Sustainable
Transition (D.D. 1243 02/08/2022, PE00000021) and received funding
under the National Recovery and Resilience Plan (PNRR), Mission
4 Component 2 Investment 1.3, funded from the European Union
- NextGenerationEU; (3) the National Recovery and Resilience Plan
(NRRP), Mission 4 Component 2 Investment 1.4 - Call for ‘‘National
Centres’’ from research to business, funded by the European Union
– NextGenerationEU. Project code CN00000023, Concession Decree
No. 1033 adopted by Ministero dell’Università e della Ricerca (MUR),
Italy, CUP - D93C22000410001, Project title ‘‘MOST - National Center
for Sustainable Mobility’’. This manuscript reflects only the authors’
views and opinions, neither the European Union nor the European
Commission can be considered responsible for them.
Appendix A. Supplementary data
Supplementary material related to this article can be found online
at https://doi.org/10.1016/j.ijhydene.2024.11.242.
References
[1] Jervis-Smith FJ. Cecil’s gas engine. Nature 1904;70(6):553.
[2] Das L. Hydrogen engines: A view of the past and a look into the future. Int J
Hydrog Energy 1990;15(6):425–43.
[3] Das L. Development trend of liquid hydrogen-fueled rocket engines (part 1:
Performance and operation). Int J Aeronauti Space Sci 2023;24(1):131–45.
[4] Distaso E, Cassone E, Tamburrano P, Amirante R, Palma PD. Characterization
of the hydrogen combustion process in a scramjet engine. Int J Hydrog Energy
2024;71:651–60.
[5] Berry GD, Pasternak AD, Rambach GD, Ray Smith J, Schock RN. Hydrogen as a
future transportation fuel. Energy 1996;21(4):289–303.
[6] Sharma S, Ghoshal SK. Hydrogen the future transportation fuel: From production
to applications. Renew Sustain Energy Rev 2015;43:1151–8.
[7] Mathur H, Das L. Performance characteristics of a hydrogen fuelled S.I. engine
using timed manifold injection. Int J Hydrog Energy 1991;16(2):115–27.
[8] Lambe S, Watson H. Low polluting, energy efficient C.I. hydrogen engine. Int J
Hydrog Energy 1992;17(7):513–25.
[9] Giannotta A, Cherubini S, Palma PD. The effect of hydrogen enrichment on
thermoacoustic instabilities in laminar conical premixed methane/air flames. Int
J Hydrog Energy 2023;48:37654–65.
[10] Lee S, Yi H, Kim E. Combustion characteristics of intake port injection type
hydrogen fueled engine. Int J Hydrog Energy 1995;20(4):317–22.
[11] Khalid AH, Muhamad Said MF, Veza I, Abas MA, Roslan MF, Abubakar S,
Jalal M. Hydrogen port fuel injection: Review of fuel injection control strategies
to mitigate backfire in internal combustion engine fuelled with hydrogen. Int J
Hydrog Energy 2024;66:571–81. http://dx.doi.org/10.1016/j.ijhydene.2024.04.
087.
[12] Abd Alla G, Soliman H, Badr O, Abd Rabbo M. Effect of pilot fuel quantity on the
performance of a dual fuel engine. Energy Convers Manage 2000;41(6):559–72.
[13] Ramsay C, Dinesh KR. Numerical modelling of a heavy-duty diesel-hydrogen
dual-fuel engine with late high pressure hydrogen direct injection and diesel pi-
lot. Int J Hydrog Energy 2024;49:674–96. http://dx.doi.org/10.1016/j.ijhydene.
2023.09.019.
[14] Koyanagi K, Hiruma M, Furuhama S. Study on mechanism of backfire in
hydrogen engines. SAE Technical Paper 942035, 1994.
[15] Guo L, Lu H, Li J. A hydrogen injection system with solenoid valves for a
four-cylinder hydrogen-fuelled enginefn2fn2this paper is based on L.S. Guos
Ph.D. dissertation in the Department of Energy Engineering, Zhejiang University,
Hangzhou, 310027, P.R. China.. Int J Hydrog Energy 1999;24(4):377–82.
[16] Distaso E, Calo‘ G, Amirante R, Palma PD, Mehl M, Pelucchi M, Stagni A. Linking
lubricant oil contamination to pre-ignition events in hydrogen engines–The
HyLube mechanism. Fuel 2025;379:133041.
International Journal of Hydrogen Energy 96 (2024) 849–859 
858

<!-- PDF_PAGE: 11 -->

G. Caramia et al.
[17] Dong X, Wang B, Yip HL, Chan QN. CO2 emission of electric and gasoline
vehicles under various road conditions for China, Japan, Europe and World
average—Prediction through year 2040. Appl Sci 2019;9(11).
[18] Yip HL, Srna A, Yuen ACY, Kook S, Taylor RA, Yeoh GH, Medwell PR, Chan QN.
A review of hydrogen direct injection for internal combustion engines: Towards
carbon-free combustion. Appl Sci 2019;9(22).
[19] Abubakar S, Muhamad Said MF, Abas MA, Ismail NA, Khalid AH, Roslan MF,
Kaisan MU. Hydrogen-fuelled internal combustion engines - Bibliometric anal-
ysis on research trends, hotspots, and challenges. Int J Hydrog Energy
2024;61:623–38. http://dx.doi.org/10.1016/j.ijhydene.2024.02.280.
[20] Hamzehloo A, Aleiferis P. Computational Study of Hydrogen Direct Injection for
Internal Combustion Engines. SAE Technical Paper 2013-01-2524, 2013.
[21] Hamzehloo A, Aleiferis P. Large eddy simulation of highly turbulent under-
expanded hydrogen and methane jets for gaseous-fuelled internal combustion
engines. Int J Hydrog Energy 2014;39(36):21275–96.
[22] Hamzehloo A, Aleiferis P. Numerical modelling of transient under-expanded
jets under different ambient thermodynamic conditions with adaptive mesh
refinement. Int J Heat Fluid Flow 2016;61:711–29.
[23] Hamzehloo A, Aleiferis P. Gas dynamics and flow characteristics of highly turbu-
lent under-expanded hydrogen and methane jets under various nozzle pressure
ratios and ambient pressures. Int J Hydrog Energy 2016;41(15):6544–66.
[24] Hamzehloo A, Aleiferis PG. LES and RANS modelling of under-expanded jets with
application to gaseous fuel direct injection for advanced propulsion systems. Int
J Heat Fluid Flow 2019;76:309–34.
[25] Yip HL, Srna A, Liu X, Kook S, Hawkes ER, Chan QN. Visualiza-
tion of hydrogen jet evolution and combustion under simulated direct-
injection compression-ignition engine conditions. Int J Hydrog Energy
2020;45(56):32562–78.
[26] Wang Y, Evans A, Srna A, Wehrfritz A, Hawkes E, Liu X, Kook S, Chan QN.
A Numerical Investigation of Mixture Formation and Combustion Characteristics
of a Hydrogen-Diesel Dual Direct Injection Engine. SAE Technical Paper 0526,
2021.
[27] Salazar VM, Kaiser SA. An optical study of mixture preparation in a hydrogen-
fueled engine with direct injection using different nozzle designs. SAE Int J
Engines 2010;2(2):119–31.
[28] Addepalli SK, Pei Y, Zhang Y, Scarcelli R. Multi-dimensional modeling of mixture
preparation in a direct injection engine fueled with gaseous hydrogen. Int J
Hydrog Energy 2022;47(67):29085–101.
[29] Salazar VM, Kaiser SA. Influence of the flow field on flame propagation in a
hydrogen-fueled internal combustion engine. SAE Technical Paper 2011-24-0098,
2011.
[30] Wallner T, Matthias NS, Scarcelli R. Influence of injection strategy in a high-
efficiency hydrogen direct injection engine. SAE Technical Paper 2011-01-2001,
2011.
[31] Obermair H, Scarcelli R, Wallner T. Efficiency improved combustion system for
hydrogen direct injection operation. SAE Technical Paper 2010-01-2170, 2010.
[32] Pavlos G, Aleiferis P, Rosati MF. Controlled autoignition of hydrogen in a
direct-injection optical engine. Combust Flame 2012;159(7):2500–15.
[33] Hamzehloo A, Aleiferis P. Numerical modelling of mixture formation and
combustion in DISI hydrogen engines with various injection strategies. SAE
Technical Paper 2014-01-2577, 2014.
[34] Liu X, Srna A, Yip HL, Kook S, Chan QN, Hawkes ER. Performance and
emissions of hydrogen-diesel dual direct injection (H2DDI) in a single-cylinder
compression-ignition engine. Int J Hydrog Energy 2021;46(1):1302–14.
[35] Sierens R, Verhelst S. Experimental study of a hydrogen-fueled engine. J Eng
Gas Turb Power 2000;123(1):211–6.
[36] Yadav VS, Soni S, Sharma D. Engine performance of optimized hydrogen-fueled
direct injection engine. Energy 2014;65:116–22.
[37] Rahman M, Hamada KI, Aziz ARA. Characterization of the time-averaged overall
heat transfer in a direct-injection hydrogen-fueled engine. Int J Hydrog Energy
2013;38(11):4816–30.
[38] Kosmadakis G, Pariotis E, Rakopoulos C. Heat transfer and crevice flow in a
hydrogen-fueled spark-ignition engine: Effect on the engine performance and NO
exhaust emissions. Int J Hydrog Energy 2013;38(18):7477–89.
[39] Sfriso S, Berni F, Fontanesi S, d’Adamo A, Frigo S, Antonelli M, Borghi M.
Proposal and validation of a numerical framework for 3D-CFD in-cylinder
simulations of hydrogen spark-ignition internal combustion engines. Int J Hydrog
Energy 2024;53:114–30. http://dx.doi.org/10.1016/j.ijhydene.2023.12.027.
[40] Donaldson Cd, Snedeker RS. A study of free jet impingement. Part 1. Mean
properties of free and impinging jets. J Fluid Mech 1971;45(2):281–319. http:
//dx.doi.org/10.1017/S0022112071000053.
[41] Crist S, Glass DR, Sherman PM. Study of the highly underexpanded sonic jet.
AIAA J 1966;4(1):68–71. http://dx.doi.org/10.2514/3.3386.
[42] Scarcelli R, Wallner T, Matthias N, Salazar V, Kaiser S. Mixture formation
in direct injection hydrogen engines: CFD and optical analysis of single- and
multi-hole nozzles. SAE Int J Engines 2011;4(2):2361–75.
[43] Ruggles A, Ekoto I. Ignitability and mixing of underexpanded hydrogen jets. Int
J Hydrog Energy 2012;37(22):17549–60.
[44] Le Moine J, Senecal PK, Kaiser SA, Salazar VM, Anders JW, Svensson KI,
Gehrke CR. A Computational Study of the Mixture Preparation in a Direct–
Injection Hydrogen Engine. J Eng Gas Turb Power 2015;137(11):111508. http:
//dx.doi.org/10.1115/1.4030397.
[45] Tang X, Dzieminska E, Asahara M, Hayashi AK, Tsuboi N. Numerical in-
vestigation of a high pressure hydrogen jet of 82 MPa with adaptive mesh
refinement: Concentration and velocity distributions. Int J Hydrog Energy
2018;43(18):9094–109.
[46] Ye Y, Gao W, Li Y, Zhang P, Cao X. Numerical study of the effect of injection
timing on the knock combustion in a direct-injection hydrogen engine. Int J
Hydrog Energy 2020;45(51):27904–19.
[47] Babayev R, Andersson A, Dalmau AS, Im HG, Johansson B. Computational
characterization of hydrogen direct injection and nonpremixed combustion in
a compression-ignition engine. Int J Hydrog Energy 2021;46(35):18678–96.
[48] Ballatore A, van Oijen J. Pressure-based large-eddy simulation of under-expanded
hydrogen jets for engine applications. Int J Hydrog Energy 2024;49:771–83.
[49] Yosri M, Palulli R, Talei M, Mortimer J, Poursadegh F, Yang Y, Brear M. Numeri-
cal investigation of a large bore, direct injection, spark ignition, hydrogen-fuelled
engine. Int J Hydrog Energy 2023;48(46):17689–702.
[50] Shu C-W, Osher S. Efficient implementation of essentially non-oscillatory
shock-capturing schemes. J Comput Phys 1988;77:439–71.
[51] Jiang GS, Shu C-W. Efficient implementation of weighted ENO schemes. J
Comput Phys 1996;126:202–28.
[52] Martin T, Shevchuk I. Implementation and validation of semi-implicit WENO
schemes using OpenFOAM. Computation 2018;6.
[53] Menter FR, Martin K, Robin L. Ten years of industrial experience with the SST
turbulence model. Turbulence Heat Mass Transfer 2003;4:625–32.
[54] Malcolm WC. NIST-JANAF thermochemical tables. American Institute of Physics
for the National Institute of Standards and Technology; 1998.
[55] Poling BE, Prausnitz JM, O’Connell JP. The properties of gases and liquids, vol.
1. McGraw-Hill; 2000.
[56] Ollivier-Gooch C. Quasi-ENO schemes for unstructured meshes based on umlim-
ited data-dependent least-squares reconstruction. J Comput Phys 1997;133:6–17.
[57] Dumbser M, Käser M. Arbitrary high order non-oscillatory finite volume
schemes on unstructured meshes for linear hyperbolic systems. J Comput Phys
2007;221:693–723.
[58] Henrick AK, Aslam TD, Powers JM. Arbitrary high order non-oscillatory finite
volume schemes on unstructured meshes for linear hyperbolic systems. J Comput
Phys 2005;207:542–67.
[59] Zhang X, Shu C-W. On maximum-principle-satisfying high order schemes for
scalar conservation laws. J Comput Phys 2010;229:3091–120.
[60] Patankar S, Spalding D. A calculation procedure for heat, mass and momen-
tum transfer in three-dimensional parabolic flows. Int J Heat Mass Transfer
1972;15(10):1787–806. http://dx.doi.org/10.1016/0017-9310(72)90054-3 .
[61] Patankar S. Numerical heat transfer and fluid. Flow 1980.
[62] Issa R. Solution of the implicitly discretised fluid flow equations by operator-
splitting. J Comput Phys 1986;62(1):40–65. http://dx.doi.org/10.1016/0021-
9991(86)90099-9.
[63] Vuorinen V, Yu J, Tirunagari S, Kaario O, Larmi M, Duwig C, Boersma BJ. Large
eddy simulation of highly turbulent under-expanded hydrogen and methane jets
for gaseous-fuelled internal combustion engines. Phys Fluids 2013;25:016101.
[64] Anaclerio G, Capurso T, Torresi M, Camporeale SM. Numerical characterization
of hydrogen under-expanded jets with a focus on Internal Combustion Engines
applications. Int J Engine Res 2023;24(8):3342–58.
[65] Ashkenas H, Sherman FS. The structure and utilization of supersonic free jets
in low density wind tunnel. In: Advances in applied mechanics-rarefied gas
dynamics. Academic Press; 1965, p. 84–105.
[66] Antsupov AV. Properties of underexpanded and overexpanded supersonic gas
jets. Sov Phys Techn Phys 1974;19.
[67] Velikorodny A, Kudriakov S. Numerical study of the near-field of highly
underexpanded turbulent gas jets. Int J Hydrog Energy 2012;37(22):17390–9.
[68] Ruggles A, Ekoto I. Experimental investigation of nozzle aspect ratio effects
on underexpanded hydrogen jet release characteristics. Int J Hydrog Energy
2014;39(35):20331–8.
[69] Xiao J, Travis J, Breitung W. Hydrogen release from a high pressure
gaseous hydrogen reservoir in case of a small leak. Int J Hydrog Energy
2011;36(3):2545–54.
[70] Richards CD, Pitts WM. Global density effects on the self-preservation behaviour
of turbulent free jets. J Fluid Mech 1993;254:417–35.
International Journal of Hydrogen Energy 96 (2024) 849–859 
859
