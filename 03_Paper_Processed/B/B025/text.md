<!-- PDF_PAGE: 1 -->

International Journal of Heat and Fluid Flow 107 (2024) 109381
Available online 16 April 2024
0142-727X/© 2024 The Author(s). Published by Elsevier Inc. This is an open access article under the CC BY-NC-ND license ( http://creativecommons.org/licenses/by-
nc-nd/4.0/).
Contents lists available at ScienceDirect
International Journal of Heat and Fluid Flow
journal homepage: www.elsevier.com/locate/ijhff
CFD analysis of hydrogen and methane turbulent transitional
under-expanded jets
Francesco Duronio ∗, Angelo De Vita
Dipartimento di Ingegneria Industriale Informazione e di Economia - Università degli studi dell’Aquila, Piazzale Ernesto Pontieri, Monteluco di
Roio, 67100, L’Aquila (AQ), Italy
Consiglio Nazionale delle Ricerche, Istituto di Scienze e Tecnologie per l’Energia e la Mobilità Sostenibili (STEMS), Via G. Marconi 4, Napoli, 80125, Napoli
(NA), Italy
A R T I C L E I N F O
Keywords:
Under-expanded jets
OpenFOAM
Hydrogen injection
Methane injection
Flux splitting KNP
DMD decomposition
A B S T R A C T
Under-expanded jets appear in various processes of engineering interest and, among others, during the injection
of gaseous fuels in the combustion chamber. In this context, large eddy simulations of under-expanded
hydrogen jets were carried out adopting a low-numerical-diffusion scheme based on the flux-splitting method.
Pressure ratios ranging from five to twenty and the influence of chemical species injected were considered.
Convergence and uncertainty of the numerical results were preliminarily assessed, and then the comparison
with Schlieren acquisitions was exploited to validate the mathematical methodology adopted. Mach disc
dimensions were found to be in good agreement with the experiments. Dynamic Mode Decomposition (DMD)
was applied to investigate the characteristics of the resultant turbulent flow. A comparison of methane and
hydrogen under-expanded jets reveals that the latter penetrates faster and presents a more developed vortical
structure that enhances air/fuel mixing.
1. Introduction
Under-expanded jets are complex high-speed flows that are present
in various engineering applications, including exhaust plumes from
aircraft like rockets and missiles, combustion chambers, and, among
others, these types of jets can also occur in natural phenomena like
volcanic eruptions (Orescanin et al., 2010; von der Linden et al., 2021;
Carcano et al. , 2013; FOX, 1974; Duronio et al. , 2021b). As a result,
under-expanded jets have a long history of investigation, particularly
in aerospace applications. However, in the last decade, the research has
focused on their impact on the injection process in advanced propulsion
systems, making it a relatively new area of study within fluid dynamics
and engine-related analysis (Duronio et al., 2023).
The adoption in modern propulsion systems of fuels like hydrogen,
propane, methanol and methane involves the injection of the fuel
in gaseous conditions rather than as a liquid. Due to the significant
pressure difference between the injection environment and the injector
rail, supersonic conditions are almost always reached ( Duronio et al. ,
2023; Vuorinen et al., 2014; Hamzehloo and Aleiferis, 2014a, 2016b) .
This results in the development of under-expanded jets downstream of
the injector’s nozzles, creating a particular flow field structure (Allocca
et al., 2020; Samsam-Khayani et al., 2022). Although extensive studies
∗ Corresponding author.
E-mail address: francesco.duronio@univaq.it (F. Duronio).
have investigated the characteristics of gaseous jets for aerospace appli-
cations, it is equally essential to thoroughly understand these processes
for propulsion applications (Onorati et al., 2022).
Numerous scientific research studies were conducted to investigate
methane jets ( Yosri et al. , 2020 ; Banholzer et al. , 2019 ; Bartolucci
et al. , 2020 ; Dong et al. , 2018 ), while comparatively fewer efforts
were dedicated to study hydrogen fuel despite its heightened scientific
interest. Schlieren imaging is usually adopted to record the evolution
of transient under-expanded hydrogen jets issued from gaseous fuel
injectors. The effect of pressure ratio (PR) and nozzle characteristic
were evaluated, as well as the jet tip penetration ( Coratella et al. ,
2024; Yeganeh et al. , 2023a; Lee et al. , 2021; Yeganeh et al. , 2023b,
2022). The experimental investigations are almost completely limited
to qualitative parameters rather than quantitative ones. On the opposite
for jets of other chemical species, density maps and PLIF (Planar Laser
Induced Fluorescence) acquisitions are available and allow to have
local values of fuel concentration as well as of the gas density (Yu et al.,
2013b, 2011; Sakellarakis et al. , 2021; Ni et al. , 2022). These kinds
of investigations are essential to robustly validate CFD simulations of
under-expanded jets.
Indeed, to gain a more detailed understanding of the underlying
physics, scientific research can undoubtedly leverage simulation tools,
https://doi.org/10.1016/j.ijheatfluidflow.2024.109381
Received 5 November 2023; Received in revised form 21 March 2024; Accepted 10 April 2024

<!-- PDF_PAGE: 2 -->

International Journal of Heat and Fluid Flow 107 (2024) 109381
2
F. Duronio and A. De Vita
which can also significantly aid in developing simplified models to
design and optimize injection devices. The methodology commonly
employed includes explicit (Onorati et al., 2022; Buttay et al., 2016;
Hamzehloo and Aleiferis, 2019; Duronio et al., 2022) and implicit algo-
rithms (Yosri et al., 2020; Rahantamialisoa et al., 2022; Hamzehloo and
Aleiferis, 2014b). The density-based approach, incorporating a Large
Eddy Simulation (LES) turbulence framework, was proven to be the
most suitable choice for replicating the characteristic features of under-
expanded jets. Implicit methods, such as the Pressure Implicit Split
Operator (PISO) algorithm, historically employed for solving incom-
pressible fluid flow governing equations, were more recently adapted
for compressible flows. However, as extensively demonstrated in the lit-
erature (Hamzehloo and Aleiferis, 2014a; Vuorinen et al., 2014, 2013),
explicit methods are the optimal choice regarding result accuracy. This
preference arises from inherent aspects of the algorithmic procedure.
High-order integration schemes (e.g., Runge Kutta 4th order) are also
necessitated due to strong fluid-flow discontinuities.
Various works can be found in the literature regarding under-
expanded jets of methane, nitrogen, and air (Yu et al., 2013a; Banholzer
et al., 2017; Traxinger et al., 2018; Banholzer et al., 2019; Xiao et al.,
2019). The interest in hydrogen is growing, in the last years (Anaclerio
et al., 2022, 2023; Ballatore and van Oijen, 2024; Su et al., 2020).
Hamzelhoo et al. studied the near-nozzle structure of different under-
expanded jets (Hamzehloo and Aleiferis, 2016a, 2014a). They used a
CFD code based on the AUSM (advection upstream splitting method)
discretization scheme for compressible flows and they investigated the
jet tip penetration, the shear layer, and the Mach disc (Hamzehloo
and Aleiferis, 2016b). Cryogenic H 2 jets were investigated numerically
and experimentally to understand the effects of the nozzle diameter
and pressure ratio on the under-expanded structures (Ren and Wen,
2020; Hecht and Panda, 2019; Gopal et al., 2020; Loureiro et al.,
2020; Madana Gopal et al., 2023) . The numerical setup used by Ren
et al. features a 2D model to save computational resources and WENO
schemes; it also differs from common approaches because it does not
use a high-pressure reservoir, which is replaced by a total pressure
boundary condition. This approach was also used by Zhang et al.
(2019). Other studies regarded the influence of real-fluid properties
on jet behavior. Both Redlick–Kwong and Peng–Robinson equations of
state were tested, demonstrating how, in certain injection conditions,
the results differ from the ones obtained using the ideal-gas equation
of state (Jin and Yao, 2021; Rahantamialisoa et al., 2023).
So, the simulation and the experimental validation of hydrogen
and methane weakly-to-strongly under-expanded jets with different
pressure ratio and nozzles dimensions were performed. A CFD approach
previously developed in the OpenFOAM environment was adopted.
The methodology was newly validated using hydrogen experimental
images regarding the Mach discs and then applied to compare the
behavior of under-expanded jets of methane and hydrogen. Dynamic
mode decomposition was applied to the flow field to recognize the pres-
ence of coherent turbulent structures and to understand the dynamic
of air/fuel mixing both within and downstream the under-expanded
structures. This topic, the main novelty of the present contribution,
was scarcely deepened in the past, not for hydrogen jets (Saddington
et al., 2004; Vuorinen et al., 2013) and revealed some interesting
outcomes, highlighting how the flow field strongly depends on fluid
characteristics.
Acquiring such a deep understanding of the leading phenomena
that occur when a gaseous pressurized fuel like hydrogen is discharged
in a low-pressure environment is essential for developing reduced
models. These meta-models need to describe the behavior of the under-
expanded jets adequately and, at the same time, guarantee small com-
putational costs, making them implementable in a whole engine model.
2. Mathematical and numerical method
The governing equations of the compressible fluid flow, which
include conservation of mass, momentum, and total energy, were ex-
pressed in their conservative form ( 𝜌, 𝜌𝐮 and 𝜌𝑒):
𝜕𝜌
𝜕𝑡 + ∇ ⋅ (𝐮𝜌) = 0 (1)
𝜕(𝜌𝐮)
𝜕𝑡 + ∇ ⋅ [𝐮(𝜌𝐮) + 𝑝] = ∇ ⋅ 𝜎 (2)
𝜕(𝜌𝑒)
𝜕𝑡 + ∇ ⋅ [𝐮(𝜌𝑒) + 𝑝] = ∇ ⋅ (𝜎 ⋅ 𝐮) + ∇ ⋅ 𝐪 (3)
where:
• 𝑝 represents the pressure connected to density and temperature
through the ideal gas state equation.
• 𝑒 is the total energy, it is calculated as the sum of internal 𝑈𝑖 and
kinetic energy:
𝑒 = 𝑈𝑖 + 1
2 ‖𝐮2‖ (4)
with 𝑈𝑖 being expressed as:
𝑈𝑖 = 𝑐𝑣𝑇 (5)
𝑐𝑣 represents constant volume-specific heat, and 𝑇 is temperature;
• 𝜎 is the stress tensor that, for a Newtonian fluid, is equal to:
𝜎 = 𝜇 [∇𝐮 + (∇𝐮)T]−
(2
3 𝜇∇ ⋅ 𝐮
)
𝐈 = 2𝜇𝑑𝑒𝑣(𝐃) (6)
with 𝜇 viscosity and 𝐃 strain tensor (𝐃 = 1
2
[∇𝐮 + (∇𝐮)T]).
• 𝐪 is the heat flux vector computed as:
𝐪 = 𝜆∇𝑇 (7)
where 𝑇 is the fluid temperature and 𝜆 is the heat conduction
coefficient computed as:
𝜆 =
𝜇𝑐𝑝
𝑃 𝑟 (8)
with 𝑐𝑝 being the constant pressure specific heat and 𝑃 𝑟 = 0 .7 is
the Prandtl number. 𝑐𝑝 is computed as a function of temperature
from JANAF tables (Chase, 1998).
To investigate the mixing of multiple species, the governing equations
are completed by including a transport equation for each species.
𝜕 (𝜌𝑌𝑖
)
𝜕𝑡 + ∇ ⋅ 𝜌𝐮𝑌𝑖 = ∇ ⋅ (𝜌𝐷𝑖∇𝑌𝑖
) (9)
where, for the i-species, 𝑌𝑖 is concentration, and 𝐷𝑖 is the diffusivity,
equal to:
𝐷𝑖 = 𝜇
𝜌𝑆𝑐 (10)
with Schmdit number 𝑆𝑐 = 0 .7, after Vuorinen et al. (2013). The
molecular viscosity is temperature dependent according to Sutherland’s
law specific constants of the single species (White and Frank M. White,
1991).
The governing equations were discretized using the so-called cen-
tral schemes formulations of Kurganov (KNP) and Kurganov and Tad-
mor (KT) (Kurganov and Tadmor, 2000; Kurganov et al., 2001). Flux
splitting methods guarantee low numerical dissipation and, at the
same time, provide improved stability in comparison with central
schemes (Hamzehloo and Aleiferis, 2019; Vuorinen et al., 2013; Duro-
nio et al., 2024; Duronio and Di Mascio, 2024) . These methods are
non-staggered second-order central schemes that compute the fluxes
on the cell faces using a flux-splitting approach. The cell-to-face flow
interpolation is subdivided into an inward and outward direction with
respect to the face owner cell. A complete and detailed description
of KNP and KT central schemes can be found in Greenshields et al.

<!-- PDF_PAGE: 3 -->

International Journal of Heat and Fluid Flow 107 (2024) 109381
3
F. Duronio and A. De Vita
Fig. 1. Schematic representation of the computational domain used for the simulations.
(For interpretation of the references to color in this figure legend, the reader is referred
to the web version of this article.)
(2010). VanLeer flux limiter ensures the simulation stability ( Green-
shields et al. , 2010; van Leer , 1974; Versteg and Malalasekera , 2007)
while time integration is performed using explicit Runge–Kutta 4th
(RK4) method in order to correctly reproduce shock-waves present in
flow-field (Hamzehloo and Aleiferis , 2019; Vuorinen et al. , 2013). A
complete description of the method can be found in Duronio et al.
(2021a) and Duronio et al. (2021b).
Large Eddy Simulation (LES) modeling is preferred to reproduce the
air/fuel interaction with great detail following literature Refs. Vuorinen
et al. (2014, 2013) and Hamzehloo and Aleiferis (2019). A one-equation
eddy viscosity model for compressible flows was adopted ( Huang and
Li, 2010; Yoshizawa and Horiuti , 1985). The sub-grid scale eddy vis-
cosity 𝜈𝑡 is calculated using a transport equation for turbulent kinetic
energy 𝑘𝑠𝑔𝑠 field and the filter dimension 𝛥 (usually evaluated from the
grid size) according to the following relation:
𝜈𝑡 = 𝐶𝑘𝛥
√
𝑘𝑠𝑔𝑠 (11)
where 𝐶𝑘 is a model constant whose default value is 0.094.
Finally, using this parameter, the effective dynamic viscosity (𝜇𝑒𝑓 𝑓)
can be computed and used for the solution of the governing equa-
tions ( 1)–(3) ( Hamzehloo and Aleiferis , 2019 ; Greenshields et al. ,
2010; Pope and Pope , 2000). More specifically, the effective viscosity
is the sum of the molecular and of the eddy turbulent viscosity:
𝜇𝑒𝑓 𝑓 = 𝜇 + 𝜇𝑡 (12)
3. Case study
Two nozzles, experimentally investigated by Yip et al. ( 2020) and
Allocca et al. ( 2020), respectively, were considered. In the following,
for brevity, they will be referred to as nozzle 1 (Yip et al.) and 2
(Allocca et al.). Both of them regard round jets issued from single-hole
nozzles. The diameter is equal to 0.58 mm for nozzle 1 and 1 mm for
nozzle 2. Images of the under-expanded jets were acquired using optical
Schlieren and Shadowgraph imaging techniques. They are diagnostic
techniques that visualize optical in-homogeneities of transparent me-
dia, otherwise not visible to the human eye ( Settles, 2001; Panigrahi
and Muralidhar, 2012). These methods are sensitive to changes in the
refractive index of a light beam traveling through a heterogeneous
medium. Fig. 1 shows the general characteristics of the integration
domain used for both the simulated nozzles.
The computational domain consists of a cylindrical reservoir (col-
ored in cyan) initialized with high-pressure fuel. This reservoir is
connected, through the investigated nozzle, to a lower-pressure cham-
ber containing nitrogen (green cylinder) initialized with environmen-
tal pressure conditions. The inflow section of the upstream reservoir
(colored in red) is treated with a total pressure boundary condition.
Table 1
Details of the injection conditions simulated.
Nozzle 1 Nozzle 2
Nozzle diameter [mm] 0.58 1
Nozzle length [mm] 1 0.9
Pressure ratio [–] 5 10 20 9 12
Ambient pressure [bar] 10 1
Ambient temperature [K] 298
Table 2
Uncertainty and grid convergence index evaluation along the jet’s axis.
Average value Uncertainty Grid convergence index
𝜌 1.29 kg m−3 2.77% 1.08%
𝑝 11.76 bar 3.03% 1.29%
𝐔 1525 m/s 2.29% 0.92%
The computational grid is created using cfMesh and includes various
levels of refinement extending in the axial direction for a length equal
to seventy diameters, as depicted in Figs. 2(a) –2(b).
The nozzle diameter was discretized using 40 cells, and the other
zones had cells whose dimensions gradually increased. This meshing
strategy has already been adopted in previous studies with similar flows
where the pressure ratios are in the same range as the cases investigated
here. The strategy exhibits discrete result accuracy, avoiding too exces-
sive usage of computational resources (Bonelli et al., 2013; Khaksarfard
et al., 2010; Rana et al., 2011; Rahantamialisoa et al., 2023; Hamzehloo
and Aleiferis, 2016a; Duronio et al., 2021b).
The test conditions and the nozzle dimensions are detailed in Ta-
ble 1.
The nozzle exit velocity can be estimated with the hypothesis
of having sonic conditions at the exit section as done in previous
works ( Hamzehloo and Aleiferis , 2016b ; Edgington-Mitchell et al. ,
2014). It is equal to U𝑒𝑥𝑖𝑡,𝐻2 = 1190 m s−1 and U𝑒𝑥𝑖𝑡,𝐶𝐻4 = 419 m s−1. The
time-step adopted was variable and depended on the Courant number,
which was set to be lower than 0.8 ( Courant et al. , 1928 ; Duronio
et al., 2021a,b) .
4. Hydrogen jets investigation
4.1. Preliminary discussion. Code accuracy assessment
The aforementioned numerical approach has already been validated
by the authors on methane jets issued by single and multi-hole pat-
terned injectors ( Duronio et al. , 2021b , 2022 , 2021a ); anyway, for
the present contribution, a further verification of the methodology
accuracy was performed for hydrogen injections.
The simulation’s convergence and uncertainty were assessed using
two grid levels (a further coarser grid was explicitly considered for
the purpose). Table 2 reports the average values for the main fields
evaluated along the jet’s axis with the relative uncertainty and the grid
convergence index. The jet issued with PR = 20 was considered.
The grid convergence is defined as:
𝐺𝐶𝐼 = 𝑆𝐹
𝑓1
𝑓2 − 𝑓1
𝑟𝜎 − 1 (13)
where SF is a safety factor, 𝑓2 and 𝑓1 the solutions obtained with the
two grid levels, r the grid dimensions ratio and 𝜎 the order of the
discretization scheme employed.
Fig. 3 shows the plot of density, pressure, velocity, and temperature
fields sampled along the jet axis, together with the uncertainty once the
jet with PR = 20 reached pseudo-stationary conditions.
The uncertainty of the numerical results was assessed as in the
classical paper by Roache (1997), in which the procedures now adopted
by AIAA, ITTC, and IEEE are described and discussed in detail. In this
procedure, the uncertainty is computed exploiting different solutions

<!-- PDF_PAGE: 4 -->

International Journal of Heat and Fluid Flow 107 (2024) 109381
4
F. Duronio and A. De Vita
Fig. 2. (a) Vertical section of the grid with refinement regions and respective grid dimensions. ( b) Near nozzle zoom.
Fig. 3. Temporal averages of density, pressure, velocity and temperature. The blue horizontal lines represent the ambient pressure and a Mach number equal to the unity in the
respective graphs.
obtained with two or three levels of grid where the dimensions are
in a fixed ratio, for example, doubled. The uncertainty bars, being
significantly small, demonstrate the adequacy of the mesh size adopted
to represent the evolution of the under-expanded jet. The classical steep
variation of the flow field can be observed in correspondence with the
first shock at a distance of approximately 1.7 mm from the nozzle exit
section. The jet velocity reaches at the most 3000 m∕s and Ma number
at most equal to 4. Nevertheless these are very high-velocity values,
these findings are in agreement with what obtained by Hamzehloo and
Aleiferis (2016b,a, 2014a), Lacerda (1987) and Jin and Yao (2021).
In order to assess the adequacy of the chosen grid to represent the
turbulence effects, we evaluated the modeled kinetic energy compared
to the total energy. This evaluation followed the methodology outlined
by Di Mascio et al. ( 2022). Fig. 4 illustrates the ratio between the
modeled and total kinetic energy computed once the jet reaches steady

<!-- PDF_PAGE: 5 -->

International Journal of Heat and Fluid Flow 107 (2024) 109381
5
F. Duronio and A. De Vita
Fig. 4. 𝐾𝑚𝑜𝑑 ∕(𝐾𝑚𝑜𝑑 + 𝐾𝑟𝑒𝑠) plotted on an axial section.
Fig. 5. Assessment of quality for LES simulations.
Fig. 6. Comparison of numerical results (left side) and experimental schlieren image (right side) for the jet issued with PR = 5, 10 and 20.
state conditions and the Mach disc is fully developed. These results are
presented on the axial mid-plane for a specific temporal instant.
The modeled kinetic energy is relatively low compared to the re-
solved kinetic energy. The ratio between the modeled and total kinetic
energy consistently remains below 0.3 throughout most of the domain.
This finding aligns with the criteria set forth by Pope and Pope ( 2000)
for adequate resolution in Large-Eddy Simulation (LES). There are
only a few localized regions where this ratio reaches 0.3. They are
located near the shock waves where, due to the presence of relevant
field discontinuities (velocity gradients), the results cannot not be
considered.
The quality of the LES simulation is also confirmed by Figs. 5(a) –
5(b). They report the ratio between effective and molecular viscosity
(
𝜈𝑡,𝑒𝑓 𝑓
𝜈 ) and the LES Quality index computed following the methodology

<!-- PDF_PAGE: 6 -->

International Journal of Heat and Fluid Flow 107 (2024) 109381
6
F. Duronio and A. De Vita
Fig. 7. 3D rendering of the three jets investigated represented by fuel mass fraction volume rendering. (For interpretation of the references to color in this figure legend, the
reader is referred to the web version of this article.)
Fig. 8. Jet volume plotted over time for PR = 5, 10, 20.
 Fig. 9. DMD spectrum. The intensity is normalized to the maximum value.

<!-- PDF_PAGE: 7 -->

International Journal of Heat and Fluid Flow 107 (2024) 109381
7
F. Duronio and A. De Vita
Table 3
Mach disc height measurements.
Pressure Experimental CFD Relative
Ratio height height difference
[–] [ mm] [ mm] [–]
10 1.07 1.11 3.6%
20 1.64 1.69 3.1%
proposed by Celik et al. (2005) :
𝐼𝑄 𝐿𝐸𝑆,𝜈 = 1
1 + 𝛼𝑣(
𝜈𝑒𝑓 𝑓
𝜈 )𝑛
, (14)
where 𝛼𝑣 is a constant with a value of 0.05, 𝑛 = 0 .53 and 𝜈𝑒𝑓 𝑓 and 𝜈
respectively effective and molecular kinematic viscosity.
As discussed by Celik et al. ( 2005) and Lien et al. ( 2024), a ratio
greater than 80% describes an high-quality LES simulation.
Once having verified the result’ convergence and their numerical
accuracy, the validity of the approach adopted was assessed by com-
paring the Schlieren images acquired by Yip et al. ( 2020) against the
logarithm of the density gradient computed from the CFD simulations.
Fig. 6 reports the latter alongside the experiments for the three nozzle
pressure ratios investigated.
The code reproduces correctly the hydrogen jets issued over a
range of pressure ratios ranging from moderately to highly under-
expanded configuration ( Franquet et al. , 2015 ). The position of the
Mach disc, numerically computed, matches the experimental images,
and the under-expanded structures are reproduced accordingly.
With a PR = 5, the jet is moderately under-expanded and has a ‘‘di-
amond’’ or ‘‘X’’ structure. Oblique compression shocks, usually called
intercepting shock, depart from the nozzle edges and converge toward
the jet axis. This structure is repeated multiple times downstream,
demonstrating how expansions and re-compression zones follow one
another.
Mach disc appears as the pressure ratio increases (PR = 10). The
regular reflection of the intercepting shock on the axis is no longer
possible. As a result, above the critical angle, this reflection becomes
singular, resulting in the appearance of a normal shock-denominated
Mach disc. The triple point is clearly recognizable as the intersection
of the intercepting shock, the Mach disc, and the reflected shock that
are well reproduced together with the slipstreams.
The jet becomes very highly under-expanded when the pressure
ratio is equal to 20. The structure is dominated by a unique barrel,
and the Mach disc dimensions increase. The Mach disc height measure-
ments are reported in Table 3 for the pressure ratios investigated.
The agreement is quite satisfactory, as depicted by the slight per-
centage difference computed. It must be noted that the case with PR =
5 was not listed since the Mach disc does not appear.
4.2. Insights about the jet structure
Fig. 7 shows a volumetric rendering, colored according to the fuel
mass fraction (𝐻2), of the jet after 100 μs for the three PR analyzed.
The under-expanded shocks propagate for approximately 10 mm
from the nozzle’s exit section in the axial direction while, further down-
stream, the jet, having loosened momentum, resembles a characteristic
turbulent flow. It can also be observed how, further than the increasing
axial penetration with the injection pressure, the higher the injection
pressure is, the greater the jet’s overall volume becomes. This is also
confirmed by Fig. 8 where the jet volume is plotted over time for PR =
5, 10, 20.
A proficient method to comprehend the essential dynamics of a tur-
bulent flow without the need for detailed physical modeling is Dynamic
Mode Decomposition (DMD) ( Weiner and Semaan, 2021; Rathje et al.,
2022; Vega and Clainche, 2020) . The application of DMD to CFD simu-
lations allows for the identification of dominant flow patterns, coherent
Fig. 10. Real part of the top DMD modes defined for the three frequency range. Density
field.
Fig. 11. Real part of the top four DMD modes computed from the velocity field.

<!-- PDF_PAGE: 8 -->

International Journal of Heat and Fluid Flow 107 (2024) 109381
8
F. Duronio and A. De Vita
Fig. 12. Q-criterion contour colored by total kinetic energy (TKE). (For interpretation of the references to color in this figure legend, the reader is referred to the web version
of this article.)
Fig. 13. Total kinetic energy (TKE) plot in the near nozzle zone.

<!-- PDF_PAGE: 9 -->

International Journal of Heat and Fluid Flow 107 (2024) 109381
9
F. Duronio and A. De Vita
Fig. 14. Temporal evolution of logarithm of the density gradient for the hydrogen and methane jets.
structures, vortex shedding, and flow instabilities. This investigation
is essential to create low-dimensional models, significantly reducing
simulation computational costs.
The idea behind DMD is to decompose a three-dimensional flow
field into two separate parts that describe how flow structures change
in space (but are constant in time) and how these modes evolve over
time. DMD was performed on the velocity and density fields considering
the PR = 20. Fig. 9 presents the resulting DMD frequency spectrum for
the density.
The modes’ frequency is expressed in Hz while the intensity is
normalized with the maximum value. The spectrum reveals that the
dominant mode is the 12th, with a frequency equal to 𝑓 = 38 .7 kHz.
The 9th and the 13th modes have comparable intensity, respectively
the 10% and 20% lower. Their frequencies are 𝑓 = 7531 kHz and
𝑓 = 68 590 kHz, respectively.
To provide a quick and comprehensive representation of all modes
dynamics, the spectrum was divided into three parts:
• Low-frequency modes: frequency range 0–100 kHz. Dominant
mode: 12th.
• Mid-frequency modes: frequency range 10–200 kHz. Dominant
mode: 6th.
• High-frequency modes: frequency range 100–400 kHz. Dominant
mode: 2nd.
For each frequency range, the real part of the dominant mode was
reported on Fig. 10.
In the near nozzle zone, all three modes present alternating pockets
of positive and negative density fluctuations, indicating the mixing
between the streams of varying density. This pattern, which depicts the
shear layer, is axial-symmetric and becomes wider going downstream
the flow. Precisely, after the Mach disc, it regards the whole jet width.
Even if of minor absolute intensity, the higher the frequency, the wider
the fluctuations.
Fig. 11 reports the four dominant modes obtained performing the
velocity decomposition.

<!-- PDF_PAGE: 10 -->

International Journal of Heat and Fluid Flow 107 (2024) 109381
10
F. Duronio and A. De Vita
Fig. 15. Hydrogen and methane Mach disc comparison.
The transverse component is anti-symmetric and shows positive and
negative velocity fluctuations in the external shear layer. This pattern
provides evidence of helical vortices of varying wavelengths as already
observed by Vuorinen et al. (2013). The presence of axisymmetric shear
layer instabilities, depicted by the axial component of the velocity, acts
as a forcing mechanism for the generation of toroidal modes.
Finally, to better understand the influence of the upstream pressure
on the flow’s turbulent development, the Q-criterion ( 𝐐 = 1
2 (‖Ω‖2 −
‖𝐒‖2), where 𝐒 is the strain tensor and Ω is the vorticity tensor) was
used to capture vortices. Fig. 12 shows Q-criterion iso-surfaces with the
color map representing the turbulent kinetic energy (TKE).
The turbulent kinetic energy increases drastically, moving towards
the jet’s tip. No great vortices appear within the potential core where
the hydrogen is confined while, moving outwardly from the jet’s axis in
the radial direction, small vortices with a reduced amount of TKE can
be easily recognized. On the opposite, larger vortices, with relatively
high TKE, are present on the jet tip, enhancing the mixing process and
creating the conditions for effective air-fuel interaction. Increasing the
PR, TKE values grow significantly, and the vortices become bigger. This
implies an enhanced downstream mixing activity as already observed
by other authors (Vuorinen et al., 2013).
Fig. 13 reports a further axial plot of the turbulent kinetic energy
(TKE) on an axial plane. It is confirmed that the higher the PR is, the
greater the TKE owned by the jet becomes.
5. Hydrogen-methane jets comparison
Once having further verification of the capabilities of the developed
numerical approach in representing under-expanded jets, a comparison
between different fuels, more precisely, H 2 and CH 4, was carried out.
As previously mentioned, the methane CFD simulations were already
experimentally validated and discussed in a previous work ( Duronio
et al., 2021a) while, here, the hydrogen was investigated using the same
setup.
Fig. 14 reports the evolution of the logarithm of the density gradient
in the injection environment obtained by slicing the domain with an
axial plane for the two different pressure ratios and both fuels.
The development of the hydrogen jet is much faster than the
methane; this is a consequence of the smaller dimensions of the
H2 molecule. This behavior was observed also in other researches
(Hamzehloo and Aleiferis , 2016b; Jin and Yao , 2021; Hamzehloo and
Aleiferis, 2016a ). At PR = 9, only methane exhibits the behavior of
a highly under-expanded jet. Intercepting shocks can be distinctly
observed in the hydrogen jet, and only if we increase the PR to 12
we begin to observe the appearance of Mach disc. The dimensions of
the latter are not stable, but as depicted from the snapshots series, it is
clear that we are in a transition state.
Fig. 15 is a zoomed view of the near-nozzle zone proposed to
compare hydrogen and methane Mach discs characteristics.
The Prandtl-Meyer expansion fans, barrel shock, angle of reflected
shock, triple points, and slip lines were all accurately predicted, and
they were all in excellent agreement with other authors’ computational
findings and experimental visualizations as well as with the theory of
under-expanded jet ( Vuorinen et al. , 2011; Yu et al. , 2012; Dauptain
et al. , 2012 ). Upstream the Mach disc, methane and air did not in-
teract. On the other hand, momentum exchange and mixing at the jet
boundary can be observed at the lateral borders of the hydrogen Mach
disc where large oscillations are present. These vortices are known as
Gortler vortices (Saric, 1994; Hall, 1982).
Particular attention deserve the axial plots of the main fluid-
dynamic fields for the two fuels. Fig. 16 reports precisely pressure,
density, velocity magnitude, and temperature along the nozzle axis for
the PR = 12.
The density of hydrogen is way smaller than methane, and so, as a
consequence, differences obviously appear in the graph. The pressure
graph shows comparable oscillations in correspondence to the normal
shocks.
At the opposite, the hydrogen’s jet velocity is significantly higher
than the methane one. The maximum values are approximately 2600
m/s for the first fuel, while the second one reaches at most 900 m/s.
The fluctuations are much higher with the hydrogen jet; more pre-
cisely, crossing the hydrogen Mach disc, the velocity diminishes by
approximately 2000 m/s while with the methane of 700 m/s.
The minimum temperature reached upstream of the Mach disc is
approximately 50 K for the H 2 and 100 K for the CH 4. Downstream
oscillations of the latter fuel are small if compared with the hydrogen
ones. Finally, Fig. 17 reports the Mach number behavior along the jet
axis for the hydrogen and methane jet.
The characteristics of turbulence play an essential role in the for-
mation of the air/fuel mixture and fulfill a primary importance in
combustion efficiency. The temporal evolution of the vortical struc-
tures, depicted by the Q-criterion iso-surfaces, is shown in Fig. 18, with
the color map representing the turbulent kinetic energy (TKE).
The vortical structures are way more developed in the hydrogen
jet, while the methane flow presents smaller and fewer structures
characterized by reduced kinetic energy. The energy cascade, which
creates the multitude of vortices, is more developed with H2, which has
consequences on the mixing activity. A quick and intuitive evaluation
of the mixing activity can be observed in Fig. 19 where maps of the
scalar dissipation rate (SDR) for both fuels are shown.
In the near-nozzle zone, both the jets are bounded by a thin region,
the shear layer. As depicted by the SDR map, the fuel concentration
diminishes abruptly across this boundary in a relatively small space.
Only downstream, where the jets have loosed a significant amount of
momentum, the turbulence intervenes, enabling an intimate interaction
with the ambient gas, even within the jet core, and allowing the mixing,
as depicted by the multitude of string-like structures. The turbulent
mixing zone is significantly more developed on the H 2 jet than the
CH4 one. The potential core is reduced in length, and the interaction
between the species is faster.
A quantitative evaluation of the mixture quality can be provided
by analyzing the development of the average value of the fuel con-
centration (expressed as mass fraction) over time. Fig. 20 shows the
outcomes of such analysis for the hydrogen and methane jets issued
from the nozzle 2 with PR = 9 and 12.
The jet boundaries are defined by a fuel concentration equal to
0.1%. The graph shows how the pressure ratio has a minimum effect
on the mixture quality, slightly decreasing the average concentration

<!-- PDF_PAGE: 11 -->

International Journal of Heat and Fluid Flow 107 (2024) 109381
11
F. Duronio and A. De Vita
Fig. 16. Density, pressure, velocity magnitude and temperature axial plots for PR = 12. Nozzle 2.
Fig. 17. Mach number axial plots for PR = 12. Nozzle 2.
towards lower values. At the opposite, a relevant difference can be
observed by comparing the two fuels investigated. After 130 μs, the
hydrogen jet presents an average concentration equal to approximately
60% while, for the methane, the value is significantly higher, 87%
precisely.
6. Conclusions
The current study investigates near nozzle shock structures and
the mixing activity of under-expanded hydrogen and methane jets.
The mathematical methodology, already validated by the authors on
methane jets, was also verified with hydrogen injections featuring
pressure ratios ranging from weakly to highly under-expanded jets.
Convergence and uncertainty of the computations were preliminary
assessed by adopting the classical Roache theory. The main findings
obtained from analyzing the hydrogen jets are:
• The low-dissipative explicit method adopted properly captures
the under-expanded hydrogen jets over a wide range of pressure
ratios. The measurements of the Mach disc height provide a
quantitative term of comparison.
• Increasing PR results in greater Mach disc dimensions and jet
volume.
• DMD decomposition of the flow reveals that the main mixing
begins downstream of the Mach disc location and also in the
vicinity of the jet boundaries where intense turbulence dominates
the mixing process.
• The transverse velocity component originates anti-symmetric he-
lical vortical structures while the axial component of the velocity
gives toroidal modes.
• Higher turbulent kinetic energy and greater vortices can be ob-
tained with higher PR.
The comparison of hydrogen and methane jets results in the following:
• The near-nozzle shock structure showed different patterns de-
pending on the chemical species injected. Mach disc does not
appear when injecting hydrogen with a PR = 9, while using PR =
12, the hydrogen disc is present.
• For both fuels, the mixing activity does not occur in the potential
core where shock waves are present; only the hydrogen jets
showed a more developed mixing layer at the boundaries of the
jet where an actual mixing takes place.

<!-- PDF_PAGE: 12 -->

International Journal of Heat and Fluid Flow 107 (2024) 109381
12
F. Duronio and A. De Vita
Fig. 18. Q-criterion contour colored by total kinetic energy (TKE). (For interpretation of the references to color in this figure legend, the reader is referred to the web version
of this article.)
Fig. 19. Scalar dissipation rate plot for the two studied fuels.

<!-- PDF_PAGE: 13 -->

International Journal of Heat and Fluid Flow 107 (2024) 109381
13
F. Duronio and A. De Vita
Fig. 20. Temporal development of average fuel concentration for hydrogen and
methane jets issued with PR = 9 and 12.
• The main mixing zone grows downstream of the Mach disc loca-
tion, particularly where intense turbulence plays a dominant role
in the mixing process.
• The hydrogen jet, reaching higher velocities, penetrates faster
than the methane jet; thus, it exhibits the presence of more
developed vortical structures. This can be observed plotting the Q-
criterion iso-surfaces and looking at the turbulent kinetic energy
field.
• The characterization of the mixing process highlights that hydro-
gen mixes with the air faster than the methane. Scalar dissipation
rate plot shows the presence of more extended string like struc-
tures and at the end of the simulated period the average concen-
tration of the hydrogen present in the injection environment is
the half of the methane one.
CRediT authorship contribution statement
Francesco Duronio: Writing – original draft, Visualization, Valida-
tion, Software, Methodology, Investigation, Formal analysis, Concep-
tualization. Angelo De Vita: Writing – review & editing, Supervision,
Resources.
Declaration of competing interest
The authors declare that they have no known competing finan-
cial interests or personal relationships that could have appeared to
influence the work reported in this paper.
Data availability
Data will be made available on request.
Acknowledgments
This work has been funded by the European Union - NextGenera-
tionEU under the Italian Ministry of University and Research (MUR)
National Innovation Ecosystem grant ECS00000041 - VITALITY - CUP
E13C22001060006
The CFD simulations were performed on the CINECA’s Galileo100
cluster within the agreement between DIIIE—Università degli Studi
dell’Aquila and CINECA.
References
Allocca, L., Montanaro, A., Meccariello, G., Duronio, F., Ranieri, S., De Vita, A., 2020.
Under-expanded gaseous jets characterization for application in direct injection
engines: Experimental and numerical approach. SAE Tech. Pap. 2020-April (April),
1–15. http://dx.doi.org/10.4271/2020-01-0325.
Anaclerio, G., Capurso, T., Torresi, M., 2023. Gas-dynamic and mixing analysis of under-
expanded hydrogen jets: effect of the cross section shape. J. Fluid Mech. 970, A8.
http://dx.doi.org/10.1017/jfm.2023.603.
Anaclerio, G., Capurso, T., Torresi, M., Camporeale, S.M., 2022. Numerical characteri-
zation of hydrogen under-expanded jets: Influence of the nozzle cross-section shape.
2385, Institute of Physics, http://dx.doi.org/10.1088/1742-6596/2385/1/012046,
Ballatore, A., van Oijen, J., 2024. Pressure-based large-eddy simulation of under-
expanded hydrogen jets for engine applications. Int. J. Hydrogen Energy 49,
771–783. http://dx.doi.org/10.1016/j.ijhydene.2023.09.062.
Banholzer, M., Müller, H., Pfitznery, M., 2017. Numerical investigation of the flow
structure of underexpanded jets in quiescent air using real-gas thermodynamics. In:
23rd AIAA Computational Fluid Dynamics Conference, 2017. American Institute of
Aeronautics and Astronautics Inc, AIAA, http://dx.doi.org/10.2514/6.2017-4289.
Banholzer, M., Vera-Tudela, W., Traxinger, C., Pfitzner, M., Wright, Y., Boulou-
chos, K., 2019. Numerical investigation of the flow characteristics of underexpanded
methane jets. Phys. Fluids 31 (5), 056105. http://dx.doi.org/10.1063/1.5092776.
Bartolucci, L., Cordiner, S., Mulone, V., Scarcelli, R., Wallner, T., Swantek, A.,
Powell, C., Kastengren, A., 2020. Gaseous jet through an outward opening injector:
Details of mixing characteristic and turbulence scales. Int. J. Heat Fluid Flow 85,
108660. http://dx.doi.org/10.1016/j.ijheatfluidflow.2020.108660.
Bonelli, F., Viggiano, A., Magi, V., 2013. A numerical analysis of hydrogen under-
expanded jets under real gas assumption. J. Fluids Eng. Trans. ASME 135, http:
//dx.doi.org/10.1115/1.4025253.
Buttay, R., Lehnasch, G., Mura, A., 2016. Analysis of small-scale scalar mixing processes
in highly under-expanded jets. Shock Waves 26, 193–212. http://dx.doi.org/10.
1007/s00193-015-0599-7.
Carcano, S., Bonaventura, L., Esposti Ongaro, T., Neri, A., 2013. A semi-implicit,
second-order-accurate numerical model for multiphase underexpanded volcanic
jets. Geosci. Model Dev. 6 (6), 1905–1924. http://dx.doi.org/10.5194/gmd-6-1905-
2013.
Celik, I.B., Cehreli, Z.N., Yavuz, I., 2005. Index of resolution quality for large
eddy simulations. J. Fluids Eng. 127 (5), 949–958. http://dx.doi.org/10.1115/1.
1990201.
Chase, M., 1998. NIST-JANAF Thermochemical Tables, fourth ed. p. 1952,
doi:citeulike-article-id:12140840.
Coratella, C., Tinchon, A., Oung, R., Doradoux, L., Foucher, F., 2024. Experimental
investigation of the combined impact of backpressure with the pintle dynamic on
the hydrogen spray exiting a medium pressure DI outward-opening injector. Int. J.
Hydrogen Energy 49, 432–449. http://dx.doi.org/10.1016/j.ijhydene.2023.08.124.
Courant, R., Friedrichs, K., Lewy, H., 1928. Über die partiellen differenzengleichungen
der mathematischen physik. Math. Ann. 100, 32–74. http://dx.doi.org/10.1007/
BF01448839.
Dauptain, A., Gicquel, L.Y.M., Moreau, S., 2012. Large eddy simulation of supersonic
impinging jets. AIAA J. 50 (7), 1560–1574. http://dx.doi.org/10.2514/1.J051470.
Di Mascio, A., Dubbioso, G., Muscari, R., 2022. Vortex structures in the wake of
a marine propeller operating close to a free surface. J. Fluid Mech. 949, A33.
http://dx.doi.org/10.1017/jfm.2022.772.
Dong, Q., Li, Y., Song, E., Fan, L., Yao, C., Sun, J., 2018. Visualization research on
injection characteristics of high-pressure gas jets for natural gas engine. Appl.
Therm. Eng. 132, 165–173. http://dx.doi.org/10.1016/j.applthermaleng.2017.12.
093.
Duronio, F., Battistoni, M., Di Mascio, A., De Vita, A., Rahantamialisoa, F.N.Z.,
Zembi, J., 2024. A real-fluid low-dissipative solver for flash boiling simulations
of non-equilibrium mixtures. Int. J. Heat Mass Transfer 225, 125391. http://dx.
doi.org/10.1016/j.ijheatmasstransfer.2024.125391, URL https://www.sciencedirect.
com/science/article/pii/S0017931024002229.
Duronio, F., Di Mascio, A., 2024. Implementation and assessment of a low-dissipative
openfoam solver for compressible multi-species flows. Comput. & Fluids 274,
106240. http://dx.doi.org/10.1016/j.compfluid.2024.106240, URL https://www.
sciencedirect.com/science/article/pii/S0045793024000720.
Duronio, F., Montanaro, A., Allocca, L., Ranieri, S., De Vita, A., 2022. Effects of
thermodynamic conditions and nozzle geometry in gaseous fuels direct injection
process for advanced propulsion systems. In: WCX SAE World Congress Experience.
SAE International, http://dx.doi.org/10.4271/2022-01-0505.
Duronio, F., Montanaro, A., Ranieri, S., Allocca, L., De Vita, A., 2021a. Under-expanded
jets characterization by means of CFD numerical simulation using an open FOAM
density-based solver. In: 15th International Conference on Engines & Vehicles. SAE
International, http://dx.doi.org/10.4271/2021-24-0057.
Duronio, F., Ranieri, S., Mascio, A.D., Vita, A.D., 2021b. Simulation of high pressure,
direct injection processes of gaseous fuels by a density-based OpenFOAM solver.
Phys. Fluids 33 (6), 066104. http://dx.doi.org/10.1063/5.0054098.
Duronio, F., Villante, C., De Vita, A., 2023. Under-expanded jets in advanced propul-
sion systems: A review of latest theoretical and experimental research activities.
Energies 16 (18), http://dx.doi.org/10.3390/en16186471, URL https://www.mdpi.
com/1996-1073/16/18/6471.

<!-- PDF_PAGE: 14 -->

International Journal of Heat and Fluid Flow 107 (2024) 109381
14
F. Duronio and A. De Vita
Edgington-Mitchell, D., Honnery, D.R., Soria, J., 2014. The underexpanded jet Mach
disk and its associated shear layer. Phys. Fluids 26 (9), 096101. http://dx.doi.org/
10.1063/1.4894741.
FOX, J.H., 1974. On the structure of jet plumes. AIAA J. 12 (1), 105–107. http:
//dx.doi.org/10.2514/3.49166.
Franquet, E., Perrier, V., Gibout, S., Bruel, P., 2015. Free underexpanded jets in a
quiescent medium: A review. Prog. Aerosp. Sci. 77, 25–53.
Gopal, J.M., Tretola, G., Morgan, R., de Sercey, G., Atkins, A., Vogiatzaki, K., 2020.
Understanding sub and supercritical cryogenic fluid dynamics in conditions relevant
to novel ultra low emission engines. Energies 13 (12), http://dx.doi.org/10.3390/
en13123038, URL https://www.mdpi.com/1996-1073/13/12/3038.
Greenshields, C.J., Weller, H.G., Gasparini, L., Reese, J.M., 2010. Implementation of
semi-discrete, non-staggered central schemes in a colocated, polyhedral, finite
volume framework, for high-speed viscous flows. Internat. J. Numer. Methods
Fluids 63 (1), 1–21. http://dx.doi.org/10.1002/fld.2069.
Hall, P., 1982. Taylor–Gortler vortices in fully developed or boundary-layer
flows: linear theory. J. Fluid Mech. 124, 475–494. http://dx.doi.org/10.1017/
S0022112082002596.
Hamzehloo, A., Aleiferis, P.G., 2014a. Large eddy simulation of highly turbulent
under-expanded hydrogen and methane jets for gaseous-fuelled internal combustion
engines. Int. J. Hydrogen Energy 39, 21275–21296. http://dx.doi.org/10.1016/j.
ijhydene.2014.10.016.
Hamzehloo, A., Aleiferis, P.G., 2014b. Large eddy simulation of near-nozzle shock struc-
ture and mixing characteristics of hydrogen jets for direct-injection spark-ignition
engines.
Hamzehloo, A., Aleiferis, P.G., 2016a. Gas dynamics and flow characteristics of highly
turbulent under-expanded hydrogen and methane jets under various nozzle pressure
ratios and ambient pressures. Int. J. Hydrogen Energy 41, 6544–6566. http://dx.
doi.org/10.1016/j.ijhydene.2016.02.017.
Hamzehloo, A., Aleiferis, P.G., 2016b. Numerical modelling of transient under-
expanded jets under different ambient thermodynamic conditions with adaptive
mesh refinement. Int. J. Heat Fluid Flow 61, 711–729. http://dx.doi.org/10.1016/
j.ijheatfluidflow.2016.07.015.
Hamzehloo, A., Aleiferis, P.G., 2019. LES and RANS modelling of under-expanded
jets with application to gaseous fuel direct injection for advanced propulsion
systems. Int. J. Heat Fluid Flow 76 (January), 309–334. http://dx.doi.org/10.1016/
j.ijheatfluidflow.2019.01.017.
Hecht, E.S., Panda, P.P., 2019. Mixing and warming of cryogenic hydrogen releases.
Int. J. Hydrogen Energy 44 (17), 8960–8970. http://dx.doi.org/10.1016/j.ijhydene.
2018.07.058, Special issue on The 7th International Conference on Hydrogen Safety
(ICHS 2017), 11-13 September 2017, Hamburg, Germany.
Huang, S., Li, Q.S., 2010. A new dynamic one-equation subgrid-scale model for
large eddy simulations. Internat. J. Numer. Methods Engrg. 81 (7), 835–865.
http://dx.doi.org/10.1002/nme.2715.
Jin, Y., Yao, W., 2021. LES investigation of real-fluid effect on underexpanded jets. In:
AIAA Propulsion and Energy Forum, 2021. American Institute of Aeronautics and
Astronautics Inc, AIAA, http://dx.doi.org/10.2514/6.2021-3542.
Khaksarfard, R., Kameshki, M.R., Paraschivoiu, M., 2010. Numerical simulation of high
pressure release and dispersion of hydrogen into air with real gas model. Shock
Waves 20, 205–216. http://dx.doi.org/10.1007/s00193-010-0260-4.
Kurganov, A., Noelle, S., Petrova, G., 2001. Semidiscrete central-upwind schemes for
hyperbolic conservation laws and Hamilton–Jacobi equations. SIAM J. Sci. Comput.
23 (3), 707–740. http://dx.doi.org/10.1137/S1064827500373413.
Kurganov, A., Tadmor, E., 2000. New high-resolution central schemes for nonlinear
conservation laws and convection-diffusion equations. J. Comput. Phys. 160 (1),
241–282. http://dx.doi.org/10.1006/jcph.2000.6459.
Lacerda, N.L., 1987. On the Start Up of Supersonic Underexpanded Jets (Ph.D. thesis).
California Institute of Technology.
Lee, S., Kim, G., Bae, C., 2021. Behavior of hydrogen hollow-cone spray depending on
the ambient pressure. Int. J. Hydrogen Energy 46 (5), 4538–4554. http://dx.doi.
org/10.1016/j.ijhydene.2020.11.001.
Lien, H.-P., Li, Y., Pati, A., Sadiki, A., Hasse, C., 2024. Numerical studies of gasoline
direct-injection sprays (ECN Spray G) under early- and late-injection conditions
using Large Eddy Simulation and droplets-statistics-based Eulerian–Lagrangian
framework. Fuel 357, 129708. http://dx.doi.org/10.1016/j.fuel.2023.129708, URL
https://linkinghub.elsevier.com/retrieve/pii/S0016236123023220.
Loureiro, D., Reutzsch, J., Kronenburg, A., Weigand, B., Vogiatzaki, K., 2020. Primary
breakup regimes for cryogenic flash atomization. Int. J. Multiph. Flow 132,
103405. http://dx.doi.org/10.1016/j.ijmultiphaseflow.2020.103405, URL https://
www.sciencedirect.com/science/article/pii/S0301932220305140.
Madana Gopal, J.V., Morgan, R., De Sercey, G., Vogiatzaki, K., 2023. Overview
of common thermophysical property modelling approaches for cryogenic fluid
simulations at supercritical conditions. Energies 16 (2), http://dx.doi.org/10.3390/
en16020885, URL https://www.mdpi.com/1996-1073/16/2/885.
Ni, Z., Dong, Q., Wang, D., Yang, X., 2022. Visualization research of natural gas
jet characteristics with ultra-high injection pressure. Int. J. Hydrogen Energy 47,
32473–32492. http://dx.doi.org/10.1016/j.ijhydene.2022.07.132.
Onorati, A., Payri, R., Vaglieco, B., Agarwal, A., Bae, C., Bruneaux, G., Canakci, M.,
Gavaises, M., Günthner, M., Hasse, C., Kokjohn, S., Kong, S.-C., Moriyoshi, Y.,
Novella, R., Pesyridis, A., Reitz, R., Ryan, T., Wagner, R., Zhao, H., 2022. The
role of hydrogen for future internal combustion engines. Int. J. Engine Res. 23 (4),
529–540. http://dx.doi.org/10.1177/14680874221081947.
Orescanin, M.M., Austin, J.M., Kieffer, S.W., 2010. Unsteady high-pressure flow
experiments with applications to explosive volcanic eruptions. J. Geophys. Res.:
Solid Earth 115 (B6), http://dx.doi.org/10.1029/2009JB006985.
Panigrahi, P.K., Muralidhar, K., 2012. Schlieren and Shadowgraph Methods in Heat and
Mass Transfer, vol. 2, Springer.
Pope, S.B., Pope, S.B., 2000. Turbulent Flows. Cambridge University Press.
Rahantamialisoa, F., Battistoni, M., Miliozzi, A., Sahranavardfard, N., Zembi, J., 2023.
Investigations on hydrogen injections using a real-fluid approach. http://dx.doi.
org/10.4271/2023-01-0312.
Rahantamialisoa, F.N., Zembi, J., Miliozzi, A., Sahranavardfard, N., Battistoni, M., 2022.
CFD simulations of under-expanded hydrogen jets under high-pressure injection
conditions. 2385, Institute of Physics, http://dx.doi.org/10.1088/1742-6596/2385/
1/012051,
Rana, Z.A., Thornber, B., Drikakis, D., 2011. Transverse jet injection into a supersonic
turbulent cross-flow. Phys. Fluids 23 (4), 046103. http://dx.doi.org/10.1063/1.
3570692.
Rathje, N., Ströer, P., Weiner, A., Knopp, T., Probst, A., Radespiel, R., 2022. Ex-
perimental analysis of longitudinal vortex dynamics. http://dx.doi.org/10.2514/
6.2022-3305. arXiv:https://arc.aiaa.org/doi/pdf/10.2514/6.2022-3305. URL https:
//arc.aiaa.org/doi/abs/10.2514/6.2022-3305.
Ren, Z., Wen, J.X., 2020. Numerical characterization of under-expanded cryogenic
hydrogen gas jets. AIP Adv. 10, http://dx.doi.org/10.1063/5.0020826.
Roache, P.J., 1997. Quantification of Uncertainty in Computational Fluid Dynamics.
Annual Review of Fluid Mechanics.
Saddington, A.J., Lawson, N.J., Knowles, K., 2004. An experimental and numerical
investigation of under-expanded turbulent jets. Aeronaut. J. 108 (1081), 145–152.
http://dx.doi.org/10.1017/S0001924000151590.
Sakellarakis, V.D., Vera-Tudela, W., Doll, U., Ebi, D., Wright, Y.M., Boulouchos, K.,
2021. The effect of high-pressure injection variations on the mixing state of
underexpanded methane jets. Int. J. Engine Res. 22, 2900–2918. http://dx.doi.org/
10.1177/1468087420960895.
Samsam-Khayani, H., Chen, B., Kim, M., Kim, K.C., 2022. Visualization of supersonic
free jet flow structures subjected to various temperature and pressure ratio
conditions. Opt. Lasers Eng. 158, 107144. http://dx.doi.org/10.1016/j.optlaseng.
2022.107144.
Saric, W.S., 1994. Görtler vortices. Annu. Rev. Fluid Mech. 26 (1), 379–409. http:
//dx.doi.org/10.1146/annurev.fl.26.010194.002115.
Settles, G.S., 2001. Schlieren and Shadowgraph Techniques: Visualizing Phenomena in
Transparent Media. Springer Science & Business Media.
Su, H., Cai, J., Qu, K., Pan, S., 2020. Numerical simulations of inert and reactive
highly underexpanded jets. Phys. Fluids 32 (3), 036104. http://dx.doi.org/10.1063/
1.5144558.
Traxinger, C., Banholzer, M., Pfitzner, M., 2018. Real-gas effects and phase separation
in underexpanded jets at engine-relevant conditions. http://dx.doi.org/10.2514/6.
2018-1815.
van Leer, B., 1974. Towards the ultimate conservative difference scheme. II. Mono-
tonicity and conservation combined in a second-order scheme. J. Comput. Phys.
14 (4), 361–370. http://dx.doi.org/10.1016/0021-9991(74)90019-9.
Vega, J., Clainche, S., 2020. Higher Order Dynamic Mode Decomposition
and its Applications. Elsevier Science, URL https://books.google.it/books?id=
laTgDwAAQBAJ.
Versteg, H., Malalasekera, W., 2007. An Introduction to Computational Fluid Dynamics:
The Finite Volume Method, second ed. Pearson Education Limited, Harlow.
von der Linden, J., Kimblin, C., McKenna, I., Bagley, S., Li, H.-C., Houim, R.,
Kueny, C.S., Kuhl, A., Grote, D., Converse, M., Vossen, C.E.J., Stern, S.,
Cimarelli, C., Sears, J., 2021. Standing shock prevents propagation of sparks in
supersonic explosive flows. Commun. Earth Environ. 2, 195. http://dx.doi.org/10.
1038/s43247-021-00263-y.
Vuorinen, V., Wehrfritz, A., Duwig, C., Boersma, B.J., 2014. Large-eddy simulation on
the effect of injection pressure and density on fuel jet mixing in gas engines. Fuel
130, 241–250. http://dx.doi.org/10.1016/j.fuel.2014.04.045.
Vuorinen, V., Wehrfritz, A., Yu, J., Kaario, O., Larmi, M., Boersma, B.J., 2011. Large-
eddy simulation of subsonic jets. J. Phys. Conf. Ser. 318 (SECTION 3), http:
//dx.doi.org/10.1088/1742-6596/318/3/032052.
Vuorinen, V., Yu, J., Tirunagari, S., Kaario, O., Larmi, M., Duwig, C., Boersma, B.J.,
2013. Large-eddy simulation of highly underexpanded transient gas jets. Phys.
Fluids 25 (1), 016101. http://dx.doi.org/10.1063/1.4772192.
Weiner, A., Semaan, R., 2021. flowTorch - a python library for analysis and reduced-
order modeling of fluid flows. J. Open Source Softw. 6 (68), 3860. http://dx.doi.
org/10.21105/joss.03860.
White, F., Frank M. White, S., 1991. Viscous Fluid Flow. In: McGraw-Hill Series in
Mechanical Engineering, McGraw-Hill.
Xiao, C.N., Fond, B., Beyrau, F., T’Joen, C., Henkes, R., Veenstra, P., van Wachem, B.,
2019. Numerical investigation and experimental comparison of the gas dynamics in
a highly underexpanded confined real gas jet. Flow Turbul. Combust. 103, 141–173.
http://dx.doi.org/10.1007/s10494-019-00014-2.

<!-- PDF_PAGE: 15 -->

International Journal of Heat and Fluid Flow 107 (2024) 109381
15
F. Duronio and A. De Vita
Yeganeh, M., Cheng, Q., Dharamsi, A., Karimkashi, S., Kuusela-Opas, J., Kaario, O.,
Larmi, M., 2023a. Visualization and comparison of methane and hydrogen jet
dynamics using schlieren imaging. Fuel 331, 125762. http://dx.doi.org/10.1016/j.
fuel.2022.125762.
Yeganeh, M., Rabensteiner, S., Cheng, Q., Ranta, O., Karimkashi, S., Kaario, O.,
Larmi, M., 2022. Experimental and numerical investigation of hydrogen jet-wall
impingement. In: SAE Powertrains, Fuels & Lubricants Conference & Exhibition.
SAE International, http://dx.doi.org/10.4271/2022-01-1009.
Yeganeh, M., Rabensteiner, S., Karimkashi, S., Cheng, Q., Kaario, O., Larmi, M., 2023b.
Experimental and numerical study of a low-pressure hydrogen jet under the effect
of nozzle geometry and pressure ratio. In: WCX SAE World Congress Experience.
SAE International, http://dx.doi.org/10.4271/2023-01-0320.
Yip, H.L., Srna, A., Liu, X., Kook, S., Hawkes, E.R., Chan, Q.N., 2020. Visu-
alization of hydrogen jet evolution and combustion under simulated direct-
injection compression-ignition engine conditions. Int. J. Hydrogen Energy 45 (56),
32562–32578. http://dx.doi.org/10.1016/j.ijhydene.2020.08.220.
Yoshizawa, A., Horiuti, K., 1985. A statistically-derived subgrid-scale kinetic energy
model for the large-eddy simulation of turbulent flows. J. Phys. Soc. Japan.
Yosri, M.R., Talei, M., Gordon, R., Brear, M., Lacey, J., 2020. A numerical simulation of
an under-expanded jet issued from a prototype injector. In: Proceedings of the 22nd
Australasian Fluid Mechanics Conference AFMC2020. The University of Queensland,
http://dx.doi.org/10.14264/3dc50ae.
Yu, J., Hillamo, H., Vuorinen, V., Sarjovaara, T., Kaario, O., Larmi, M., 2011. Ex-
perimental investigation of characteristics of transient low pressure wall-impinging
gas jet. 318, Institute of Physics Publishing, http://dx.doi.org/10.1088/1742-6596/
318/3/032047,
Yu, J., Vuorinen, V., Hillamo, H., Sarjovaara, T., Kaario, O., Larmi, M., 2012. An
experimental study on high pressure pulsed jets for DI gas engine using planar laser-
induced fluorescence. In: SAE 2012 International Powertrains, Fuels & Lubricants
Meeting. SAE International, http://dx.doi.org/10.4271/2012-01-1655.
Yu, J., Vuorinen, V., Kaario, O., Sarjovaara, T., Larmi, M., 2013a. Characteristics of
high pressure jets for direct injection gas engine. Int. J. Fuels Lubr. 6, 149–156.
http://dx.doi.org/10.2307/26272806.
Yu, J., Vuorinen, V., Kaario, O., Sarjovaara, T., Larmi, M., 2013b. Visualization and
analysis of the characteristics of transitional underexpanded jets. Int. J. Heat Fluid
Flow 44, 140–154. http://dx.doi.org/10.1016/J.IJHEATFLUIDFLOW.2013.05.015.
Zhang, H.-H., Aubry, N., Chen, Z.-H., Wu, W.-T., Sha, S., 2019. The evolution of the
initial flow structures of a highly under-expanded circular jet. J. Fluid Mech. 871,
305–331. http://dx.doi.org/10.1017/jfm.2019.285.
