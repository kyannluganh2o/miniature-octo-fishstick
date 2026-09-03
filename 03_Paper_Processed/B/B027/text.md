<!-- PDF_PAGE: 1 -->

Turbulent mixing dynamics of under-expanded
hydrogen jets in propulsion systems
Cite as: Phys. Fluids 37, 086158 (2025); doi: 10.1063/5.0277887
Submitted: 26 April 2025 . Accepted: 24 July 2025 .
Published Online: 20 August 2025
Francesco Duronioa),b)
 and Andrea Di Mascio
AFFILIATIONS
Dipartimento di Ingegneria Industriale Informazione e di Economia - Universit /C18a degli Studi dell ’Aquila Piazzale Ernesto Pontieri,
Monteluco di Roio, 67100 L ’Aquila (AQ), Italy
a)Author to whom correspondence should be addressed: francesco.duronio@univaq.it
b)Also at Consiglio Nazionale delle Ricerche, Istituto di Scienze e Tecnologie per l ’Energia e la Mobilit /C18a Sostenibili (STEMS),
Via G. Marconi 4, 80125 Napoli, Italy
ABSTRACT
Underexpanded jets are present in various engineering applications; in recent years, they have gained special attention because of the
development of gas-fueled propulsion systems. In these apparatuses, the direct injection of fuels such as hydrogen in innovative low-emission
engines’ chambers induces turbulent under-expanded jets. In this study, we performed high-fidelity large eddy simulations of under-
expanded hydrogen jets to investigate mixing characteristics and provide valuable insights for developing injectors suitable for hydrogen and,
more generally, gaseous-fueled propulsion systems. We initially assessed the method ’s accuracy, evaluating the convergence and uncertainty
of the numerical results and validating them against experimental particle image velocimetry and Schlieren data. The simulated jets, the
Mach disk dimensions, and the resulting velocity field align closely with the experimental observations. Then, we analyzed the jet structure
for pressure ratios of 4 to 25 and examined the effects of the geometrical configuration of the nozzle on the characteristics of the air-fuel mix-
ture obtained. We compared the jets resulting from a round-hole nozzle with annular ones resembling outward-opening injectors.
VC 2025 Author(s). All article content, except where otherwise noted, is licensed under a Creative Commons Attribution-NonCommercial-
NoDerivs 4.0 International (CC BY-NC-ND) license ( https://creativecommons.org/licenses/by-nc-nd/4.0/). https://doi.org/10.1063/5.0277887
I. INTRODUCTION
Under-expanded jets are complex high-speed flows in multiple
engineering applications, such as aircraft engine exhaust plumes,
rocket discharge, and combustion chamber injectors. Additionally,
these jets can occur in natural phenomena, like volcanic eruptions.
1–4
Consequently, under-expanded jets have been extensively studied, par-
ticularly in aerospace applications. However, in the past decade,
research has increasingly focused on their role in the injection process
of advanced propulsion systems, positioning this as an emerging field
within fluid dynamics and engine simulations.
5,6 Although gas jets
have been extensively studied for aerospace applications, it is equally
crucial to develop a comprehensive understanding of these processes
for propulsion systems.
7
In modern propulsion systems, fuels such as hydrogen, propane,
ammonia, and methane are often injected as gases rather than liquids.
Because of the substantial pressure difference between the injector rail
and the injection environment, supersonic conditions are generally
achieved.
5,8–10 This leads to the formation of under-expanded jets
downstream of the injector nozzles, resulting in a distinctive flow field
structure.11,12 Among the different combustibles, hydrogen is gaining
attention and research efforts. Direct injection into the combustion
chamber is one of the most promising technologies that will likely be
chosen for developing hydrogen combustion. In this context, it follows
that the injection process plays a relevant role in the chain of events
that takes place in the propulsion system. The injectors and the result-
ing under-expanded jets must be deeply investigated to obtain the
desired air–fuel mixture, efficient combustion, and reduced tailpipe
emissions.
Extensive research has been conducted on methane jets,
13–16 but
comparatively less focus has been given to hydrogen fuel despite its
growing scientific relevance. Schlieren imaging is commonly used to
capture the evolution of transient under-expanded hydrogen jets from
gaseous fuel injectors, evaluating factors like pressure ratio (PR), nozzle
characteristics, and jet tip penetration.
17–21 However, experimental
studies on hydrogen jets are often limited to qualitative observations.
In contrast, jets of other species are examined using density maps and
planar laser induced fluorescence, providing local values of fuel con-
centration and gas density.
22–25 Such detailed investigations are crucial
Phys. Fluids 37, 086158 (2025); doi: 10.1063/5.0277887 37, 086158-1
VC Author(s) 2025
Physics of Fluids ARTICLE pubs.aip.org/aip/pof

<!-- PDF_PAGE: 2 -->

for robust validation of new methods and CFD simulations of under-
expanded jets.
Considering the intrinsic characteristics of the physical process
under attention, simulation tools play a crucial role in gaining deeper
insights into the physics of under-expanded jets and supporting the
development of simplified models for designing and optimizing injec-
tion devices. Common methodologies employ both explicit
7,26–28 and
implicit time integration algorithms.13,29,30 Among these, using a large
eddy simulation (LES) turbulence framework and high-order integra-
tion schemes with low numerical dissipation has proven to be particu-
larly effective for replicating the characteristics of under-expanded jets
and the mixture formation.
8,9,31
The literature covers extensive studies on under-expanded jets for
gases like methane, nitrogen, and air, 14,32–35 with increasing recent
interest in hydrogen. 36–39 Hamzehloo and Aleiferis 9,10,40 explored
near-nozzle characteristics of various under-expanded jets using a
CFD code based on the advection upstream splitting method (AUSM)
discretization for compressible flows, focusing on jet tip penetration,
shear layers, and Mach disk structures. Cryogenic hydrogen (H
2)j e t s
were also experimentally and numerically investigated to examine the
nozzle diameter and pressure ratio effects on jet expansion struc-
tures.
41,42 The numerical setup of Ren and Wen 41 used a 2D model
with WENO schemes to optimize computational efficiency; their sim-
ulation differs from other typical setups because it uses a total pressure
boundary condition instead of a high-pressure reservoir; the same
approach was also adopted by Zhang et al.
43 Further research has
examined how real-fluid properties influence jet behavior. Studies
comparing the Redlich–Kwong and Peng–Robinson equations of state
revealed that, under certain injection conditions, results differ signifi-
cantly from those based on the ideal-gas law.
44,45 In particular, adopt-
ing the real fluid model, the Mach number results in higher values
within the first shock-cell, while temperature achieves lower values
downstream of the Mach disk using the ideal gas equation. This last
difference, in turn, affects the mass flow predicted. However, the most
important limitation of all these studies is the computational resources
required. Historically, injection processes have been studied relying on
Eulerian-Lagrangian CFD codes because they involve liquid fuels. So,
the minimum size of the grid is approximately equal to the diameter of
the nozzle.
46,47 In contrast, with gaseous fuels, a correct grid size, capa-
ble of correctly representing the under-expanded jets, is of the order of
magnitude of D=ð30 /C4 50Þ,9 w h e r eDi st h en o z z l ed i a m e t e r .T h i s
completely changes the requirements regarding resources needed and
p o s e si m p o r t a n tl i m i t a t i o n so nt h es i m u l a t i o n’s feasibility. Different
meshing strategies have been adopted to reduce the computational
load. However, the common approach is to use multiple refinement
regions with the grid size gradually increasing downstream of the exit
section of the nozzle.
28,40 This allowed researchers to perform the sim-
ulations in a reasonable time, but reduced the quality of the results, not
correctly predicting the characteristics of the air/fuel mixture, espe-
cially when using RANS turbulence models.
48 Other studies even sim-
plify the problem of running 2D simulations. 36,41,43 All these
approaches are unreliable for developing propulsion systems and also
for the simulation of the complete engine cycle. 5,38,49 The present
paper shows a CFD investigation of hydrogen under-expanded jets
related to propulsion applications. Unlike in the past, we studied these
hydrogen jets focusing on turbulent mixing; the investigation provides
information for the optimal design of injection devices suitable for
gaseous-fuelled propulsion systems. We ran high-fidelity GPU-acceler-
ated simulations adopting high-resolution grid sizing for the jet vol-
ume. We initially validate our simulations by relying on quantitative
particle image velocimetry (PIV) and Schlieren images of under-
expanded jets; then, we investigate different injection configurations
with different pressure ratios and evaluate the jet’s structure as well as
the mixture formation process. We also analyze the nozzle characteris-
tics, showing how the flow drastically changes with annular nozzles
and hollow cone jets, enhancing the mixing process.
II. MATHEMATICAL MODELS AND NUMERICAL
METHODS
A. Mathematical models
The numerical simulation of the compressible multi-species flow
is performed by the integration of the following governing equations:
@q
@t þr/C1ð quÞ¼ 0
@ðquÞ
@t þr/C1ð qu /C10 uÞ¼/C0 r p þr/C1 P
@ðqEÞ
@t þr/C1ð quEÞ¼r/C1ð P /C1 u /C0 puÞþr/C1 Q
@ qYkðÞ
@t þr/C1 quYkðÞ ¼r /C1 F k:
8
>>
>
>
>
>
>
>
>
>
>
<
>>
>>>
>
>
>
>
>
>
:
(1)
In the above equations,q; u,a n dp are the density, velocity vector,
and pressure, respectively. E ¼ e þ u /C1 u=2 is the specific total energy
with e representing the specific internal energy;Y
k is the mass fraction
of the kth species. The viscous stress tensor, P, under the Newtonian
assumption, is given by
TABLE I. Test cases details. PR: pressure ratio; pinj: injection pressure; pamb: ambient pressure; Tamb: ambient temperature; D: nozzle diameter; ð/C3 Þ : External diameter.
Case N/C14 Nozzle Gas/amb PR p inj [bar] pamb [bar] Tamb [K] D[mm] Jet cone angle [ /C14 ]
Validation 1 Round H 2/Air 10 9.976 0.9976 292 1.5 N/A
Validation 2 Round Air/Air 4.2 4.25 1 288 15 N/A
R1 Round H
2/Air 4.2 4.25 1 288 15 N/A
R2 Round H 2/Air 12.6 12.8 1 288 15 N/A
R3 Round H 2/Air 25.2 25.6 1 288 15 N/A
A4 Annular H 2/Air 12.6 12.8 1 288 15
ﬃﬃ ﬃ
2
p
ð/C3 Þ 90
A5 Annular H 2/Air 12.6 12.8 1 288 15
ﬃﬃ ﬃ
2
p
ð/C3 Þ 135
Physics of Fluids ARTICLE pubs.aip.org/aip/pof
Phys. Fluids 37, 086158 (2025); doi: 10.1063/5.0277887 37, 086158-2
VC Author(s) 2025

<!-- PDF_PAGE: 3 -->

P ¼ l½ru þð ruÞT/C138þ kI r/C1 uðÞ ; (2)
where l and k are dynamic viscosity and the Lam /C18e constant
(k ¼/C0 2=3l), respectively.Q is conduction heat flux
Q ¼ jrT; (3)
where j is the thermal conductivity. F k is the diffusive transport flux
of the k-th species
F k ¼ qYkDk;jrYk; (4)
where Dk;j is the binary diffusivity coefficient between the species. We
modeled the fluid with the perfect gas equation of state. In all the simu-
lations shown in the paper, we adopted the dynamic Smagorinsky LES
model
50,51 to accurately resolve the turbulent structures of the jet. This
model has already been used in the past to simulate under-expanded
jets.
52–54 For the sake of brevity, we are not reporting full details; the
reader is referred to the original papers for a complete description. We
set the Schmidt and Prandtl numbers equal to 0.7, following previous
works.
8,27,28
B. Numerical method
The numerical integration of the governing equation (1) is per-
formed using the AmRex PeleC solver, 55 which supports block-
structured adaptive mesh refinement (AMR) and GPU paralleliza-
tion.
56 In the code, the inviscid fluxes in (1) are Discretized using the
unsplit piecewise parabolic method (PPM) with hybrid PPM WENO
variants.57,58 The WENO reconstruction is performed with the
FIG. 1. Nozzle configuration investigated and jet cone angle definition Fig. 1(a) .
Overview of the computational domain Fig. 1(b).
TABLE II. Average values on the jet axis and grid convergence index evaluation for
validation cases 1 and 2.
Case 1 Case 2
Average value GCI Average value GCI
q=qexit 0.25 1.54% 0.47 1.47%
p=pexit 0.19 1.27% 0.43 1.27%
Ux =Uexit 1.10 2.52% 1.17 2.84%
FIG. 2. Kmod =ðKmod þ KresÞ plotted on an axial section of validation cases 1 and 2.
Physics of Fluids ARTICLE pubs.aip.org/aip/pof
Phys. Fluids 37, 086158 (2025); doi: 10.1063/5.0277887 37, 086158-3
VC Author(s) 2025

<!-- PDF_PAGE: 4 -->

seventh-order WENO-Z scheme of Ref. 59. The diffusion fluxes are
discretized in space with second-order centered differences. Temporal
integration relies on a standard predictor-corrector approach. 55,60
Transport coefficients are evaluated from the CHEMKIN transport
library and depend on temperature.
61,62 Thermodynamic properties
are evaluated using the NASA7 polynomial parametrisation.63
III. TEST CASES: CHARACTERISTICS AND NUMERICAL
SETUP
We investigated seven different case studies covering different
morphologies of the under-expanded jets. Table I reports their main
characteristics.
FIG. 3. Validation case 1. Comparison of an elaboration of the Schlieren images
acquired by Ruggles and Ekoto 64 and the CFD simulation performed in the current
work. Reproduced with permission from Ruggles and Ekoto, “Ignitability and mixing
of underexpanded hydrogen jets, ” Int. J. Hydrogen Energy 37, 17549 –17560
(2012). Copyright 2012 Elsevier.
FIG. 4. Validation case 2. Comparison of @q=@x and @q=@y from Ref. 65 and the
present numerical simulation. Reproduced with permission from Edgington-Mitchell
et al. , “The underexpanded jet Mach disk and its associated shear layer, ” Phys.
Fluids 26, 096101 (2014), Copyright 2014 AIP Publishing.
FIG. 5. Validation case 2. Comparison of experimental 65 and numerical non-
dimensional axial velocities ( Ux ) color maps. Uexit is the speed of sound computed
at the nozzle exit section under thermodynamic conditions. Reproduced with per-
mission from Edgington-Mitchell et al. , “The underexpanded jet Mach disk and its
associated shear layer, ” Phys. Fluids 26, 096101 (2014), Copyright 2014 AIP
Publishing.
Physics of Fluids ARTICLE pubs.aip.org/aip/pof
Phys. Fluids 37, 086158 (2025); doi: 10.1063/5.0277887 37, 086158-4
VC Author(s) 2025

<!-- PDF_PAGE: 5 -->

For verification and validation of the simulations, we considered
the jets experimentally investigated by Ruggles and Ekoto 64 and
Edgington-Mitchell et al. 65 Both are round jets issued from circular
nozzles. The diameter is equal to 1.5 mm for nozzle 1 and 15 mm for
nozzle 2. After these first verification cases, we performed other simu-
lations in which we replicated case 2 by replacing air with hydrogen
and then varied the pressure ratio PR from 4.2 to 25. The last two test
cases A4 and A5 deal with annular nozzles, as shown in Fig. 1(a).W e
defined them by maintaining the same inner diameter of cases R1-R3
and computing the outer diameter by imposing the same nozzle exit
area. These configurations represent hollow cone injectors where the
velocity of the gaseous fuel exhibits a radial component (u
r), drastically
changing the mixing process with the surrounding air. We studied two
different values of the cone angle, representative of real prototypal
devices.66
We implemented the discrete equations on the 3D computational
domain reported inFig. 1(b).
The injection environment is a cubic box with sides equal to 30D.
Table I summarizes inflow and initial conditions. Validation cases 1
and 2 replicate the test conditions of Ruggles and Ekoto 64 and
Edgington-Mitchellet al.65 We also imposed nonreflecting boundary
conditions at the sides of the box, while on the bottom, we enforced a
zero-gradient boundary condition. We refined the mesh using fixed
region refinements and adaptive mesh refinement (AMR). In each
region, the grid size obeys the law
Di ¼ Db
2RL
; (5)
where Di is the dimension of the grid in the generic refinement region,
Db is the base grid dimension, and RL is the refinement level. In all the
simulations reported, we used RL ¼ 6a n d Db ¼ D; the size gradually
decreases from the maximum to the minimum dimension (placed
around the nozzle) D6 ¼ D=64 with intermediate buffer levels. The
region of maximum refinement around the nozzle has size
8Dðjet axisÞ/C2 3D /C2 3D.
We activated grid adaptation to guarantee the finest discretization
of the whole jet and turned it on when one of the following conditions
was verified:
1. the velocity magnitude exceeds a threshold value Vthr ¼ 3:5ms /C0 1,
i.e., juji;j;k /C21 Vthr;
2. the maximum difference of the density in adjacent
locations exceeds a threshold value equal to 10 /C0 1Kg m /C0 3,
i.e.
FIG. 6. Validation case 2. Comparison of experimental 65 and numerical non-
dimensional transverse ( Uy ) velocities color maps. Uexit is the speed of sound com-
puted at the nozzle exit section under thermodynamic conditions. Reproduced with
permission from Edgington-Mitchell et al. , “The underexpanded jet Mach disk and
its associated shear layer, ” Phys. Fluids 26, 096101 (2014), Copyright 2014 AIP
Publishing.
FIG. 7. Validation case 2. Time-averaged axial velocity profiles. CFD results and
experiments performed by Edgington-Mitchell et al.65
Physics of Fluids ARTICLE pubs.aip.org/aip/pof
Phys. Fluids 37, 086158 (2025); doi: 10.1063/5.0277887 37, 086158-5
VC Author(s) 2025

<!-- PDF_PAGE: 6 -->

maxðj qiþ1;j;k /C0 qi;j;kj; jqi;j;k /C0 qi/C0 1;j;kj;
jqi;jþ1;k /C0 qi;j;kj; jqi;j;k /C0 qi;j/C0 1;kj;
jqi;j;kþ1 /C0 qi;j;kj; jqi;j;k /C0 qi;j;k/C0 1jÞ /C21 10/C0 1Kg m /C0 3:
(6)
The integration interval depends on the time the jet takes to reach
the domain bottom, which is Oð80 /C4 240ÞD=Uexit. As also discussed
in various previous papers,27,31 this duration guarantees that the struc-
tures and dimensions in the main jet body (width and height, shock
positions, and so on) oscillate around fixed values. We then computed
the running averages by sampling the simulation’s data after the onset
of this almost steady-state phase. Finally, we built two coarser meshes
for grid-dependence verification by doublingDb.
IV. VERIFICATION AND VALIDATION
We assessed the convergence and uncertainty of the simulations
using three grid levels, obtained as described at the end of Sec.III.T h e
number of points in the grid for the finest level at the start of the simu-
lation is around 12 /C2 106, while the maximum number of points
FIG. 8. Transient evolution of the jets of the validation case 2 and R1. Early stages.
 FIG. 9. Transient evolution of the jets of the validation case 2 and R1. Late stages.
Physics of Fluids ARTICLE pubs.aip.org/aip/pof
Phys. Fluids 37, 086158 (2025); doi: 10.1063/5.0277887 37, 086158-6
VC Author(s) 2025

<!-- PDF_PAGE: 7 -->

during dynamic refinement is around 187/C2 106. We followed the pro-
cedure outlined in the classical paper by Roache,67 in which the proce-
dures now adopted by AIAA, ITTC, and IEEE are described and
discussed in detail.
Table II reports the average values for the main fields evaluated
along the jet ’s axis and the relative Grid Convergence Index (GCI)
based on L2 norms of the field variations, evaluated in the whole field
at the end of the simulations.
To assess the adequacy of the chosen grid for large eddy simu-
lation, we evaluated the modeled kinetic energy and compared it to
the total kinetic energy. This evaluation follows the methodology
outlined by Di Mascio et al.
68 Figure 2 illustrates the instantaneous
ratio between the modeled and total kinetic energy computed once
the jet reaches statistically quasi-steady conditions on the axial
midplane.
The model kinetic energy is significantly lower than the resolved
one, and the modeled-to-total kinetic energy ratio is less than 0.2 for
most of the domain (the highest values appear in the shear layer). The
ratio, therefore, is below the limit of 0.3, which guarantees adequate
grid resolution for large eddy simulation.69
Next, we compared the numerical results with experimental data.
Figure 3 shows the time-averaged shape of the hydrogen jet and the
Mach disk recorded using Schlieren imaging by Ruggles and Ekoto 64
and the numerical results in terms of time-averaged density gradient
for validation case 1.
As can be observed, the numerical simulation captures both the
morphology of the hydrogen jet and the dimensions of the Mach disk.
The jet has a peculiar conical shape bounded by a relevant mixing
layer.
Figure 4 compares the partial derivatives for the density @q=@x
and @q=@y, relative to validation case 2.
The overall agreement is good, and small differences are present
only near the jet boundary in the oblique shocks downstream of the
Mach disk. The jet is highly under-expanded, being the 4< PR < 7.
70
It has a “barrel” or “bottle” structure, and a Mach disk appears (due to
a singular reflection). The regular reflection of the intercepting shock
on the axis is no longer possible. As a result, this reflection becomes
singular, resulting in the appearance of a normal shock-denominated
Mach disk. The oblique shocks, slip-lines, the normal shock, and
Prandtl–Mayer expansion fan features are well represented. As dis-
cussed in the paper by Edgington-Mitchell et al.,
65 the white stripes
that appear in the shear layer of the experimental images are represen-
tative of zones of high standard deviation and so fluctuations of
@q=@y.
Figures 5 and 6 report the contours of mean axial and transverse
flow velocities measured by Edgington-Mitchellet al.
65 and computed
in the present paper.
We normalized all velocities with the value at the nozzle exit
in the hypothesis of sonic conditions at the exit. The simulations
correctly reproduce the morphology of the velocity field for both
the axial and transverse components. Moreover, the computed
Mach disk matches the PIV data, and the magnitude of the velocity
is correctly estimated.
Figure 7 compares the time-averaged velocity profiles along the
jet axis and several transverse sections. The agreement between the
experimental data and the simulation is satisfactory.
FIG. 10. Coanda effect for hydrogen jet.
FIG. 11. Non-dimensional z component of the baroclinic term in the vorticity equa-
tion on the plane z ¼ 0. Left: air-in-air jet; right: H 2-in-air jet.
FIG. 12. Validation case 2 (top) and R1 (bottom). The logarithm of the non-
dimensional density gradient.
Physics of Fluids ARTICLE pubs.aip.org/aip/pof
Phys. Fluids 37, 086158 (2025); doi: 10.1063/5.0277887 37, 086158-7
VC Author(s) 2025

<!-- PDF_PAGE: 8 -->

V. DISCUSSION OF THE RESULTS
We split the discussion into three parts. The first compares H 2
and air under-expanded jets. Then, we investigate the pressure ratios’
effects on the hydrogen jets’ mixing process with the surrounding air.
Finally, we examine the impact of the nozzle design (test cases A4 and
A5) by varying the jet angle from 90
/C14 to 135/C14 .
A. Under-expanded H 2 and air jets
With this section, we aim to investigate the differences in the flow
structures of an under-expanded jet (and, consequently, mixing char-
acteristics) depending on the chemical species injected.Figures 8 and 9
report the transient evolution of logðq=qambÞ for Validation 2 and R1
cases. The conditions for the two test cases are identical, except that
hydrogen is injected instead of air for test R1.
More precisely, in both cases, we observe the classical structures
of under-expanded jets, such as barrel shock, cap flow discontinuity,
FIG. 13. Magnitude of vorticity vector for the air and hydrogen jet with pressure
ratio ¼ 4.2.
FIG. 14. Density, pressure, Mach number axial plots for air and H 2 jets with
PR ¼ 4.2.
Physics of Fluids ARTICLE pubs.aip.org/aip/pof
Phys. Fluids 37, 086158 (2025); doi: 10.1063/5.0277887 37, 086158-8
VC Author(s) 2025

<!-- PDF_PAGE: 9 -->

oblique shock waves, slipstream, reflected shocks, and so on (see, e.g.,
Duronio et al.,28 Zhang et al.43) .I tc a nb es e e ni nt h et¼ 0.1 ms snap-
shot of Fig. 8 that a spherical propagating shock, the so-called bow
shock. Vortex-induced shock pairs appear on the sides of the jet.
After 0.3 ms, we can observe a fully developed shock cell and the
appearance of a normal shock. The triple point can be recognized at
the intersection of the intercepting, normal, and reflected/oblique
shocks. Slipstreams develop at this point: this is an embedded shear
layer that divides the flow upstream of the Mach disk (subsonic) from
the flow downstream of the reflected shock (supersonic). Moving
ahead in time, we can notice how this shock cell-based structure devel-
ops more and, at 1.3 ms, we can count two shock cells for the air jet
while three shock cells for the H
2 jet.
Nevertheless, we can underline several differences in the flow.
First, the density of the H2 jet is lower than the ambient one. This will
have a strong influence on the development of the jet. The initial vor-
tex ring entraps much more surrounding fluid in the case of a hydro-
gen jet than with an air jet. A relevant amount of hydrogen moves
aside on the exit section, producing remarkable vortical structures that
create a hydrogen-enriched region in the radial direction (a sort of
“Coanda effect”). Figure 10 highlights this phenomenon by showing
the hydrogen mass fraction in the near nozzle zone for two different
time steps. This phenomenon is observed only with hydrogen and not
air; experimental and CFD studies confirm this behavior.
71–73
As the hydrogen jet evolves, we can observe the development and
the evolution of a complex pattern of vortices (see Fig. 8 at t ¼ 0:3 ms
and t ¼ 0:5 ms), which is absent with air jets, with the presence of a
FIG. 15. Transient evolution of the hydrogen jets R1, R2, and R3.
FIG. 16. Transient evolution of the hydrogen jets R1, R2, and R3, t ¼ 1:2 ms.
TABLE III. Mach disk’s width and height measurements. Cases R1, R2, and R3.
Jet # R1 R2 R3
Height [-] 1.17D 2.25D 3.3D
Width [-] 0.2D 1.06D 1.5D
Physics of Fluids ARTICLE pubs.aip.org/aip/pof
Phys. Fluids 37, 086158 (2025); doi: 10.1063/5.0277887 37, 086158-9
VC Author(s) 2025

<!-- PDF_PAGE: 10 -->

strong shear layer. This complex mixing layer is essential in chemically
reactive flow since it promotes interaction with the environmental gas.
We can explain the differences between the two jets by examining
the vorticity equation
@~x
@t þ ~u /C1r ~x ¼ ~x /C1r ~u /C0 ~xðr /C1 ~uÞþ 1
q2 rq /C2r p þ /C23 r2~x; (7)
where we have the material derivative of the vorticity on the left-hand
side of Eq. (7), stretching and tilting in the first two terms on the right-
hand side, the baroclinic term (the third term on the right), and the
diffusion by viscosity in the last term. The baroclinic term produces
vorticity when the density gradient is not aligned with the pressure
gradient; this term is always present in compressible flows, but we
expect strong effects when injecting light gas (hydrogen, in the present
simulations) into a heavy gas environment, like air-in-air or methane-
in-air jets.
74 Figure 11 reports the z component of this term in non-
dimensional form for the validation case 2 and R1 jets.
For the H 2-in-air jet, the pressure gradient rp is almost parallel
to the x axis and directed to the left, while the density gradient is point-
ing outward because the jet core is occupied by (the lighter) hydrogen,
as shown by the arrows on the right of Fig. 11; therefore, the baroclinic
term in the vorticity equation induces counterclockwise rotation in the
upper part of the figure and clockwise rotation in the lower portion (as
shown by the circular arrows in the picture) that push the hydrogen
outward. On the contrary, in the air-in-air flow, the density gradient
points toward the axis; consequently, the induced rotation is opposite
to the one observed with the hydrogen flow. In addition, the magni-
tude of this term is much lower. This baroclinic term justifies
the completely different morphology of the outer jet between the
FIG. 17. Hydrogen mass fraction for jets R1, R2, and R3, t ¼ 1:1 ms.
FIG. 18. Magnitude of the vorticity vector for cases R1, R2, and R3.
Physics of Fluids ARTICLE pubs.aip.org/aip/pof
Phys. Fluids 37, 086158 (2025); doi: 10.1063/5.0277887 37, 086158-10
VC Author(s) 2025

<!-- PDF_PAGE: 11 -->

single-species and the two-species flow. Nonetheless, the shock struc-
ture in the core is remarkably similar. Figure 12 is a zoomed view of
the Mach disk for the two investigated cases performed after 1.3 ms.
The figure shows that the structure of the primary shock cell is
not affected by the species injected, as both the converging shocks and
the normal shock have a similar morphology. As previously reported,
the two-species jet exhibits a broader shear layer outside the jet core,
where the hydrogen quickly mixes with the surrounding air. To quan-
tify this aspect, we reported in Fig. 13 the magnitude of the vorticity
vector after 1.3 ms.
The plot is a volumetric rendering where we removed a quarter
of the jet to show its internal structure. The vorticity is higher for the
hydrogen jet. In the near nozzle zone, both the jets present streamwise
vortices outside the potential core in the shear layer with small-scale
vortices downstream. As already underlined, the vorticity field pro-
vides an overview of the turbulence which is relevant in chemically
reactive flows since it drives the mixing of the air with the fuel and so
the efficiency of the subsequent combustion process. 40,75 Am o r e
detailed quantitative comparison of the two jets is reported in Fig. 14,
where the axial plots of non-dimensional density, pressure, and Mach
number fields are reported.
As already discussed, relevant differences can be recognized in
the density field.
B. Effects of the pressure ratio on the H
2 jets
Figure 15 reports the early stages of the jets R1, R2, and R3 evolu-
tion, where the pressure ratio equals 4.2, 12.6, and 25.2, respectively.
The early stages of the jets significantly differ when increasing the
pressure ratio. The jet with the lower pressure ratio shows two con-
verging shocks that merge at a point on the jet’s axis and a pronounced
primary vortex ring. When increasing the upstream pressure, the clas-
sical Mach disk shock appears, and the structure of the vortex rings
changes. We can observe a primary vortex ring and a significant sec-
ondary vortex ring. A cap flow discontinuity delimits a distinguishable
zone downstream of the Mach disk shock. The pressure ratio also has
a significant effect on the shear layer. Indeed, looking at the snapshots
in Fig. 15, it can be concluded that a higher injection pressure pro-
motes a broader shear layer, enhances the Coanda effect, and, as dis-
cussed below, helps form an ignitable air/fuel mixture. At t ¼ 1.2 ms
(Fig. 16), the final under-expanded structures that characterized the jet
can be observed.
Following the classification proposed by Franquet et al.
70 and
Duronio et al.,5 the jet of case R1 is highly under-expanded, while the
jets R2 and R3 are extremely (or very highly) under-expanded. Indeed,
in the first case, the jet has a “barrel” structure that repeats three times
downstream. The triple point can be recognized as the intersection of
the intercepting shock, the Mach disk, and the reflected shock. When
increasing the injection pressure, the structure of the jet is dominated
by a single barrel shock. A normal shock no longer characterizes the
Mach disk, but a relevant curvature appears. The Mach disk ’sw i d t h
FIG. 19. Probability distribution of H2 mass fraction at 1.2 ms and hydrogen mass
injected in dimensional terms.
FIG. 20. Early stages of the transient evolution for the jets A4 and A5. Plot of the
logarithm of the non-dimensional density gradient.
Physics of Fluids ARTICLE pubs.aip.org/aip/pof
Phys. Fluids 37, 086158 (2025); doi: 10.1063/5.0277887 37, 086158-11
VC Author(s) 2025

<!-- PDF_PAGE: 12 -->

and height measurements are reported in Table III for the three pres-
sure ratios investigated.
The lack of a normal shock sequence promotes jet penetration
and reduces the so-called potential core’s length, increasing the mixing
between hydrogen and air; this aspect is shown inFig. 17,w h e r ei tc a n
be observed that the zone of the jet characterized by the sequence of
barrel shocks does not show any mixing activity, which is completely
inhibited. The increase in the pressure ratio reduces the length of this
zone.
Figure 18 shows a volumetric rendering of the vorticity magni-
tude for the three cases.
Vorticity is an important parameter in assessing the mixing activ-
ity: the higher the pressure ratio, the stronger the vorticity.
Obtaining a quantitative evaluation of the overall quality of
the mixture is essential when dealing with combustion processes.
Thus, we defined a discrete mass-weighted probability density
function as
PDF
kðYH2 Þ
¼ 1
Mtot
XN
i¼1
qi dVi YH2;i for k=K /C20 YH2;i /C20ð k þ 1Þ=K
0 otherwise ;
(
(8)
where
 PDFkð/C1Þ is the probability density function;
 N is the total cell count;
 K is the number of partitions; in this case, K ¼100;
 0 /C20 k < 100;
 dVi is the cell volume;
 qi is the mixture density;
 YH2;i is the hydrogen mass fraction in the i-th cell;
 Mtot is the total injected mass at a certain instant;
Figure 19 reports the probability density function distribution
and the mass injected for the three cases investigated at 1.2 ms.
The PDFs for the three cases are very similar, showing a peak
around YH2 ¼ 0:2; the amount of hydrogen mass injected grows with
the injection pressure.
C. Effects of the nozzle shape
The nozzle design for gaseous injectors is essential to developing
efficient injection devices. For this reason, we investigate two annular
nozzles characterized by jet angles equal to 90 /C14 (case A4) and 135 /C14
(case A5). Figure 20 compares the jet’s transient evolution for the early
stages of the simulated transient. As before, we plotted the
logðq=qexitÞ.
The evolution is very different when compared with the round
jet. At t ¼0.2 /C4 0.5 ms, the hollow-cone jets present a conical structure
characterized by the angle imposed. The pressure inside the cone
becomes gradually lower than the external pressure. The jet continues
its evolution by contracting toward the x-axis, as shown in Fig. 21 ,
where we reported the time-averaged velocity vectors and the pressure
field over 0 /C20 t /C20 2:4 ms on the axial plane.
Outside the core, in the near nozzle zone, air cannot enter within
the jet due to a series of shock cells. On the other hand, we can observe
a series of vortices rotating toward the central axis that drag the
FIG. 21. Time averaged pressure field
and velocity vectors.
FIG. 22. Pressure profiles along the jet ’s axis for cases A4 and A5.
Physics of Fluids ARTICLE pubs.aip.org/aip/pof
Phys. Fluids 37, 086158 (2025); doi: 10.1063/5.0277887 37, 086158-12
VC Author(s) 2025

<!-- PDF_PAGE: 13 -->

hydrogen into the jet’s core. This flow path extends for approximately
4D downstream of the nozzle exit section. The intensity of this phe-
nomenon increases with the jet cone angle.Figure 22 reports a quanti-
tative evaluation of the pressure diminishing.
T h ep r e s s u r er e d u c t i o nr e a c h e s3 0 %i nt h ec a s eA 5 ,w h i l ei nt h e
case A4 it is at most 20%. As illustrated by Fig. 23, these vortical struc-
tures remain active until the jet spreads in the surroundings.
The subsequent injection stages are characterized by the jet
advancing toward the right boundary of the domain with a velocity
greater for jet A4 because of the smaller cone angle. Although the
shape of the jet is similar, the cone angle modifies the hydrogen con-
centration, as shown in the figure by logðq=q
exitÞ. Various experimen-
tal investigations confirm this evolution mechanism, and it is
characteristic of hollow cone jets.17,19,66
Figure 24 shows the Mach number for the two jets at t¼ 2.4 ms.
The hollow conical structure of the jet determines a ring-shaped
spatial arrangement of the shock waves. The single Mach disk observed
with the circular nozzle disappears, but barrel shocks also appear in
test cases in A4 and A5; moreover, their size diminishes with the
increasing jet angle. The number of these shock cells is larger for case
A5. We can conclude that, when performing a hollow cone injection,
the increase in the jet angle reduces the Mach number and the hydro-
gen velocity; therefore, with the same nozzle area, the injection of the
same amount of H2 requires a longer time.
Figure 25 shows a volumetric rendering of the vorticity magni-
tude for the cases A4 and A5 at t¼ 2.4 ms.
To quantitatively assess the mixture quality obtainable with a hol-
low cone injection, in Fig. 26 we plotted the PDF and the spatial aver-
age H2 concentration over the domain as a function of time for the
cases R2, A4, and A5. To have comparable results, we plotted the PDF
FIG. 23. Transient evolution of the jets A4
and A5. Late stages.
FIG. 24. Mach number plot for cases A4
and A5, t ¼ 2.4 ms.
Physics of Fluids ARTICLE pubs.aip.org/aip/pof
Phys. Fluids 37, 086158 (2025); doi: 10.1063/5.0277887 37, 086158-13
VC Author(s) 2025

<!-- PDF_PAGE: 14 -->

at the time instant required to have the injected mass equal for all the
cases.
The improvement obtainable with the hollow-cone configura-
tions, particularly with the one in test case A5, is remarkable. In the
latter configuration, the high-concentration areas where the hydrogen
is not flammable are almost entirely removed, and the average concen-
tration decreases significantly. This is confirmed by Fig. 27,w h e r ew e
reported the hydrogen mass fraction at the time instant when the
injected mass is the same.
For all the jets, we can observe a peak of the average Y
H2 during
the first phases of the injection. Almost all the hydrogen in the poten-
tial core remains within a few diameters downstream of the exit sec-
tion, and no mixing occurs despite the intense expansion.
The increased jet angle promotes the mixing with the surround-
ing air and almost completely removes the hydrogen-rich potential
core. The region where the hydrogen mass fraction is close to one is
shrunk, for case A5, to a hollow cone around the annular inflow
section.
VI. CONCLUSIONS
We investigated hydrogen under-expanded jets using large eddy
simulations of round and annular nozzles, focusing on the turbulent
FIG. 25. Magnitude of the vorticity vector for cases A4 and A5, t ¼ 2.4 ms.
FIG. 26. Probability distribution of H2 mass fraction and average H2 mass fraction
as a function of time.
Physics of Fluids ARTICLE pubs.aip.org/aip/pof
Phys. Fluids 37, 086158 (2025); doi: 10.1063/5.0277887 37, 086158-14
VC Author(s) 2025

<!-- PDF_PAGE: 15 -->

mixing of the hydrogen jets to provide insights and valuable indica-
tions to optimize the mixture formation process in low-emission pro-
pulsion systems.
We verified and validated the simulations against experimental
particle image velocimetry and Schlieren images when available.
The analyses cover different injection pressure ratios and nozzle
geometrical configurations. The main outcomes are:
 Transient evolution of hydrogen under-expanded jets radically
differs from that observed for air. The mixing outside the jet core
is enhanced by the baroclinic effect. The structure of the jet core
is similar for the two flows in terms of shock structures.
 Hydrogen’s physical properties trigger an intense interaction
with the surrounding air. The hydrogen jet develops very high
vorticity and engulfs a large air volume.
 When increasing the pressure ratio, the repeated shock cells dis-
appear, we have a unique Mach disk, and the potential core
becomes smaller. The mixture quality slightly improves.
 Hollow cone jets have a drastically different morphology when
compared to the classical round jets. Ring-shaped shock cells sub-
stitute the Mach disk, the jet from highly under-expanded
becomes weakly under-expanded, and injecting the same amount
of hydrogen requires longer.
 The recirculation zone developing downstream of the nozzle for
approximately 4D significantly enhances the mixing activity, removes
the hydrogen-rich core, and gives a higher quality mixture.
 Large jet cone angles (i.e., 135 /C14 ) improve the mixture quality
from the combustion point of view, quickly reducing the average
hydrogen concentration already in the first phase of the injection.
ACKNOWLEDGMENTS
This work has been funded by the European Union – Next
Generation EU, Mission 4, Component 1, under the Italian Ministry of
University and Research (MUR) National Innovation Ecosystem Grant
ECS00000041 - VITALITY - CUP E13C22001060006.
AUTHOR DECLARATIONS
Conflict of Interest
The authors have no conflicts to disclose.
Author Contributions
Francesco Duronio:Conceptualization (equal); Data curation (equal);
Formal analysis (equal); Investigation (equal); Methodology (equal);
Software (equal); Validation (equal); Writing – original draft (equal).
Andrea Di Mascio: Conceptualization (equal); Methodology (equal);
Resources (equal); Supervision (equal); Writing – review & editing
(equal).
DATA AVAILABILITY
The data that support the findings of this study are available
within the article.
REFERENCES
1M. M. Orescanin, J. M. Austin, and S. W. Kieffer, “Unsteady high-pressure flow
experiments with applications to explosive volcanic eruptions, ” J. Geophys.
Res.: Solid Earth 115, B06206, https://doi.org/10.1029/2009JB006985 (2010).
2J. von der Linden, C. Kimblin, I. McKenna, S. Bagley, H.-C. Li, R. Houim, C. S.
Kueny, A. Kuhl, D. Grote, M. Converse, C. E. J. Vossen, S. Stern, C. Cimarelli,
and J. Sears, “Standing shock prevents propagation of sparks in supersonic
explosive flows,” Commun. Earth Environ. 2, 195 (2021).
3S. Carcano, L. Bonaventura, T. Esposti Ongaro, and A. Neri, “A semi-implicit,
second-order-accurate numerical model for multiphase underexpanded volca-
nic jets,” Geosci. Model Dev. 6, 1905–1924 (2013).
4J. H. Fox, “On the structure of jet plumes, ” AIAA J. 12,1 0 5–107 (1974).
5F. Duronio, C. Villante, and A. De Vita, “Under-expanded jets in advanced
propulsion systems: A review of latest theoretical and experimental research
activities,” Energies 16, 6471 (2023).
6F. Duronio, S. Ranieri, A. D. Mascio, and A. D. Vita, “Simulation of high pres-
sure, direct injection processes of gaseous fuels by a density-based openfoam
solver,” Phys. Fluids 33, 066104 (2021).
7A. Onorati, R. Payri, B. Vaglieco, A. Agarwal, C. Bae, G. Bruneaux, M. Canakci,
M. Gavaises, M. G €unthner, C. Hasse, S. Kokjohn, S.-C. Kong, Y. Moriyoshi, R.
FIG. 27. Hydrogen mass fraction for the
jets R2, A4, and A5. Time is relative to a
non-dimensional mass equal to 100
injected in the computational domain.
Physics of Fluids ARTICLE pubs.aip.org/aip/pof
Phys. Fluids 37, 086158 (2025); doi: 10.1063/5.0277887 37, 086158-15
VC Author(s) 2025

<!-- PDF_PAGE: 16 -->

Novella, A. Pesyridis, R. Reitz, T. Ryan, R. Wagner, and H. Zhao, “The role of
hydrogen for future internal combustion engines, ” Int. J. Engine Res. 23, 529 –
540 (2022).
8V. Vuorinen, A. Wehrfritz, C. Duwig, and B. J. Boersma, “Large-eddy simula-
tion on the effect of injection pressure and density on fuel jet mixing in gas
engines,” Fuel 130, 241–250 (2014).
9A. Hamzehloo and P. G. Aleiferis, “Large eddy simulation of highly turbulent
under-expanded hydrogen and methane jets for gaseous-fuelled internal com-
bustion engines,” Int. J. Hydrogen Energy 39, 21275–21296 (2014).
10A. Hamzehloo and P. G. Aleiferis, “Numerical modelling of transient under-
expanded jets under different ambient thermodynamic conditions with adap-
tive mesh refinement, ” Int. J. Heat Fluid Flow 61, 711–729 (2016).
11L. Allocca, A. Montanaro, G. Meccariello, F. Duronio, S. Ranieri, and A. D. Vita,
“Under-expanded gaseous jets characterization for application in direct injec-
tion engines: Experimental and numerical approach, ” SAE Technical Paper
2020-01-0325, 2020.
12H. Samsam-Khayani, B. Chen, M. Kim, and K. C. Kim, “Visualization of super-
sonic free jet flow structures subjected to various temperature and pressure ratio
conditions,” Opt. Lasers Eng. 158, 107144 (2022).
13M. R. Yosri, M. Talei, R. Gordon, M. Brear, and J. Lacey, “A numerical simula-
tion of an under-expanded jet issued from a prototype injector, ” in Proceedings
of the 22nd Australasian Fluid Mechanics Conference AFMC2020 (The
University of Queensland, 2020).
14M. Banholzer, W. Vera-Tudela, C. Traxinger, M. Pfitzner, Y. Wright, and K.
Boulouchos, “Numerical investigation of the flow characteristics of underex-
panded methane jets, ” Phys. Fluids 31, 056105 (2019).
15L. Bartolucci, S. Cordiner, V. Mulone, R. Scarcelli, T. Wallner, A. Swantek, C.
Powell, and A. Kastengren, “Gaseous jet through an outward opening injector:
Details of mixing characteristic and turbulence scales, ” Int. J. Heat Fluid Flow
85, 108660 (2020).
16Q. Dong, Y. Li, E. Song, L. Fan, C. Yao, and J. Sun, “Visualization research on
injection characteristics of high-pressure gas jets for natural gas engine, ” Appl.
Therm. Eng. 132, 165–173 (2018).
17C. Coratella, A. Tinchon, R. Oung, L. Doradoux, and F. Foucher, “Experimental
investigation of the combined impact of backpressure with the pintle dynamic
on the hydrogen spray exiting a medium pressure di outward-opening injector, ”
Int. J. Hydrogen Energy 49, 432–449 (2024).
18M. Yeganeh, Q. Cheng, A. Dharamsi, S. Karimkashi, J. Kuusela-Opas, O.
Kaario, and M. Larmi, “Visualization and comparison of methane and hydro-
gen jet dynamics using schlieren imaging, ” Fuel 331, 125762 (2023).
19S. Lee, G. Kim, and C. Bae, “Behavior of hydrogen hollow-cone spray depend-
ing on the ambient pressure, ” Int. J. Hydrogen Energy 46, 4538–4554 (2021).
20M. Yeganeh, S. Rabensteiner, S. Karimkashi, Q. Cheng, O. Kaario, and M.
Larmi, “Experimental and numerical study of a low-pressure hydrogen jet
under the effect of nozzle geometry and pressure ratio, ” SAE Technical Paper
2023-01-0320, 2023.
21M. Yeganeh, S. Rabensteiner, Q. Cheng, O. Ranta, S. Karimkashi, O. Kaario,
and M. Larmi, “Experimental and numerical investigation of hydrogen jet-wall
impingement,” SAE Technical Paper 2022-01-1009 , 2022.
22J. Yu, V. Vuorinen, O. Kaario, T. Sarjovaara, and M. Larmi, “Visualization and
analysis of the characteristics of transitional underexpanded jets, ” Int. J. Heat
Fluid Flow 44, 140–154 (2013).
23J. Yu, H. Hillamo, V. Vuorinen, T. Sarjovaara, O. Kaario, and M. Larmi,
“Experimental investigation of characteristics of transient low pressure wall-
impinging gas jet, ” J. Phys. Conf. Ser. 318, 032047 (2011).
24V. D. Sakellarakis, W. Vera-Tudela, U. Doll, D. Ebi, Y. M. Wright, and K.
Boulouchos, “The effect of high-pressure injection variations on the mixing
state of underexpanded methane jets, ” Int. J. Engine Res. 22, 2900–2918 (2021).
25Z. Ni, Q. Dong, D. Wang, and X. Yang, “Visualization research of natural gas
jet characteristics with ultra-high injection pressure, ” Int. J. Hydrogen Energy
47, 32473–32492 (2022).
26R. Buttay, G. Lehnasch, and A. Mura, “Analysis of small-scale scalar mixing
processes in highly under-expanded jets, ” Shock Waves 26, 193–212 (2016).
27A. Hamzehloo and P. G. Aleiferis, “LES and RANS modelling of under-
expanded jets with application to gaseous fuel direct injection for advanced
propulsion systems,” Int. J. Heat Fluid Flow 76, 309–334 (2019).
28F. Duronio, A. Montanaro, L. Allocca, S. Ranieri, and A. D. Vita, “Effects of
thermodynamic conditions and nozzle geometry in gaseous fuels direct injec-
tion process for advanced propulsion systems, ” SAE Technical Paper 2022-01-
0505, 2022.
29F. N. Rahantamialisoa, J. Zembi, A. Miliozzi, N. Sahranavardfard, and M.
Battistoni, “CFD simulations of under-expanded hydrogen jets under
high-pressure injection conditions, ” J. Phys. Conf. Ser. 2385,0 1 2 0 5 1
(2022).
30H. A. A. PG, “Large eddy simulation of near-nozzle shock structure and mixing
characteristics of hydrogen jets for direct-injection spark-ignition engines, ” in
10th International Conference on Heat Transfer, Fluid Mechanics and
Thermodynamics (HEFAT2014), Orlando, Florida, USA, 2014.
31V. Vuorinen, J. Yu, S. Tirunagari, O. Kaario, M. Larmi, C. Duwig, and B. J.
Boersma, “Large-eddy simulation of highly underexpanded transient gas jets, ”
Phys. Fluids 25, 016101 (2013).
32J. Yu, V. Vuorinen, O. Kaario, T. Sarjovaara, and M. Larmi, “Characteristics of
high pressure jets for direct injection gas engine, ” SAE Int. J. Fuels Lubr. 6,
149–156 (2013).
33M. Banholzer, H. M €uller, and M. Pfitznery, “Numerical investigation of the
flow structure of underexpanded jets in quiescent air using real-gas thermody-
namics,” AIAA Paper No. 2017-4289, 2017.
34C. Traxinger, M. Banholzer, and M. Pfitzner, “Real-gas effects and phase sepa-
ration in underexpanded jets at engine-relevant conditions, ” AIAA Paper No.
2018-1815, 2018.
35C. N. Xiao, B. Fond, F. Beyrau, C. T ’Joen, R. Henkes, P. Veenstra, and B. van
Wachem, “Numerical investigation and experimental comparison of the gas
dynamics in a highly underexpanded confined real gas jet, ” Flow Turbul.
Combust. 103, 141–173 (2019).
36G. Anaclerio, T. Capurso, M. Torresi, and S. M. Camporeale, “Numerical char-
acterization of hydrogen under-expanded jets: Influence of the nozzle cross-
section shape,” J. Phys. Conf. Ser. 2385, 012046 (2022).
37G. Anaclerio, T. Capurso, and M. Torresi, “Gas-dynamic and mixing analysis
of under-expanded hydrogen jets: Effect of the cross section shape, ” J. Fluid
Mech. 970, A8 (2023).
38A. Ballatore and J. van Oijen, “Pressure-based large-eddy simulation of under-
expanded hydrogen jets for engine applications, ” Int. J. Hydrogen Energy 49,
771–783 (2024).
39H. Su, J. Cai, K. Qu, and S. Pan, “Numerical simulations of inert and reactive
highly underexpanded jets, ” Phys. Fluids 32, 036104 (2020).
40A. Hamzehloo and P. G. Aleiferis, “Gas dynamics and flow characteristics of
highly turbulent under-expanded hydrogen and methane jets under various
nozzle pressure ratios and ambient pressures, ” Int. J. Hydrogen Energy 41,
6544–6566 (2016).
41Z. Ren and J. X. Wen, “Numerical characterization of under-expanded cryo-
genic hydrogen gas jets, ” AIP Adv. 10, 095303 (2020).
42E. S. Hecht and P. P. Panda, “Mixing and warming of cryogenic hydrogen
releases,” Int. J. Hydrogen Energy 44, 8960–8970 (2019).
43H.-H. Zhang, N. Aubry, Z.-H. Chen, W.-T. Wu, and S. Sha, “The evolution of
the initial flow structures of a highly under-expanded circular jet, ” J. Fluid
Mech. 871, 305–331 (2019).
44Y. Jin and W. Yao, “LES investigation of real-fluid effect on underexpanded
jets,” AIAA Paper No. 2021-3542, 2021.
45F. Rahantamialisoa, M. Battistoni, A. Miliozzi, N. Sahranavardfard, and J.
Zembi, “Investigations on hydrogen injections using a real-fluid approach, ”
SAE Technical Paper 2023-01-0312 , 2023.
46F. Duronio, H.-P. Lien, and A. De Vita, “Cfd unified approach under Eulerian –
Lagrangian framework for methanol and gasoline direct injection sprays in
evaporative and flash boiling conditions, ” Int. J. Multiphase Flow 182, 105048
(2025).
47F. Duronio, A. Zhang, L. Zhao, and A. De Vita, “Assessment of an effervescent
breakup model for Lagrangian simulations of real fuel sprays, ” Int. J.
Thermofluids 25, 100991 (2025).
48Y. Wang, R. Scarcelli, D. Bestel, S. Demir, and A. Srna, “Multi-dimensional
modeling of mixture formation in a hydrogen-fueled heavy-duty optical engine
with direct injection, ” in ASME 2024 ICE Forward Conference, San Antonio,
Texas, USA, October 20 –23, 2024.
Physics of Fluids ARTICLE pubs.aip.org/aip/pof
Phys. Fluids 37, 086158 (2025); doi: 10.1063/5.0277887 37, 086158-16
VC Author(s) 2025

<!-- PDF_PAGE: 17 -->

49X. Luan, B. Zhang, M. Short, and T. Chen, “Calibration and sensitivity analysis
of under-expanded hydrogen jet cfd simulation based on surrogate modeling, ”
J. Loss Prev. Process Ind. 94, 105535 (2025).
50M. Germano, U. Piomelli, P. Moin, and W. H. Cabot, “A dynamic subgrid-
scale eddy viscosity model, ” Phys. Fluids A 3, 1760 –1765 (1991). https://pub-
s.aip.org/aip/pof/article-pdf/3/7/1760/12459782/1760_1_online.pdf.
51J. Smagorinsky, “General circulation experiments with the primitive equations:
I. The basic experiment, ” Mon. Weather Rev. 91,9 9–164 (1963).
52A. Dauptain, L. Y. M. Gicquel, and S. Moreau, “Large eddy simulation of super-
sonic impinging jets, ” AIAA J. 50, 1560–1574 (2012).
53A. Dauptain, B. Cuenot, and L. Y. M. Gicquel, “Large eddy simulation of stable
supersonic jet impinging on flat plate, ” AIAA J. 48, 2325–2338 (2010).
54X. Li, W. Yao, and X. Fan, “Large-eddy simulation of time evolution and insta-
bility of highly underexpanded sonic jets, ” AIAA J. 54, 3191–3211 (2016).
55M. T. Henry de Frahan, L. Esclapez, J. Rood, N. T. Wimer, P. Mullowney, B. A.
Perry, L. Owen, H. Sitaraman, S. Yellapantula, M. Hassanaly, M. J. Rahimi, M.
J. Martin, O. A. Doronina, S. N. A. M. Rieth, W. Ge, R. Sankaran, A. S.
Almgren, W. Zhang, J. B. Bell, R. Grout, M. S. Day, and J. H. Chen, “The pele
simulation suite for reacting flows at exascale, ” in Proceedings of the 2024
SIAM Conference on Parallel Processing for Scientific Computing, 2024, pp.
13–25 https://epubs.siam.org/doi/pdf/10.1137/1.9781611977967.2.
56W. Zhang, A. Almgren, V. Beckner, J. Bell, J. Blaschke, C. Chan, M. Day, B.
Friesen, K. Gott, D. Graves, M. P. Katz, A. Myers, T. Nguyen, A. Nonaka, M.
Rosso, S. Williams, and M. Zingale, “Amrex: A framework for block-structured
adaptive mesh refinement, ” J. Open Source Software 4, 1370 (2019).
57P. Colella and P. R. Woodward, “The piecewise parabolic method (PPM) for
gas-dynamical simulations,” J. Comput. Phys. 54, 174–201 (1984).
58E. Motheau and J. Wakefield, “Investigation of finite-volume methods to cap-
ture shocks and turbulence spectra in compressible flows, ” Commun. Appl.
Math. Comput. Sci. 15,1 –36 (2020).
59D. S. Balsara and C.-W. Shu, “Monotonicity preserving weighted essentially
non-oscillatory schemes with increasingly high order of accuracy, ” J. Comput.
Phys. 160, 405–452 (2000).
60M. T. Henry de Frahan, J. S. Rood, M. S. Day, H. Sitaraman, S. Yellapantula, B.
A. Perry, R. W. Grout, A. Almgren, W. Zhang, J. B. Bell, and J. H. Chen,
“PeleC: An adaptive mesh refinement solver for compressible reacting flows, ”
Int. J. High Perform. Comput. Appl. 37, 115–131 (2023).
61R. J. Kee, G. Dixon-Lewis, J. Warnatz, M. E. Coltrin, and J. A. Miller, “A
Fortran computer code package for the evaluation of gas-phase
multicomponent transport properties, ” Technical Report No. SAND-86-8246
(Sandia National Laboratories, Livermore, CA, USA, 1986).
62A. Ern and V. Giovangigli, “Fast and accurate multicomponent transport prop-
erty evaluation,” J. Comput. Phys. 120, 105–116 (1995).
63B. J. McBride, M. J. Zehe, and S. Gordon, “NASA Glenn coefficients for calcu-
lating thermodynamic properties of individual species, ” Technical Report No.
NASA/TP-2002-211556 (National Aeronautics and Space Administration,
John H. Glenn Research Center, 2002).
64A. Ruggles and I. Ekoto, “Ignitability and mixing of underexpanded hydrogen
jets,” Int. J. Hydrogen Energy 37, 17549–17560 (2012).
65D. Edgington-Mitchell, D. R. Honnery, and J. Soria, “The underexpanded jet
Mach disk and its associated shear layer, ” Phys. Fluids 26, 096101 (2014).
66A. Montanaro, L. Allocca, and G. Meccariello, “High-pressure hydrogen jet
behavior: Flow rate and inner morphology investigation, ” SAE Technical Paper
2024-01-2617, 2024.
67P. J. Roache, “Quantification of uncertainty in computational fluid dynamics, ”
Annu. Rev. Fluid Mech . 29, 123–160 (1997).
68A. Di Mascio, G. Dubbioso, and R. Muscari, “Vortex structures in the wake of a
marine propeller operating close to a free surface,” J. Fluid Mech.949, A33 (2022).
69S. B. Pope and S. B. Pope, Turbulent Flows (Cambridge University Press, 2000).
70E. Franquet, V. Perrier, S. Gibout, and P. Bruel, “Free underexpanded jets in a
quiescent medium: A review, ” Prog. Aerosp. Sci. 77,2 5–53 (2015).
71P. Leick and K. Bartole, “Experimental investigation into the shift of GDI sprays
towards nearby walls via the Coand /C21a effect using detailed shadow imaging, par-
ticle and structure image velocimetry, ” Exp. Fluids 64, 144 (2023).
72L. Merotto, M. Balmelli, and P. Soltic, “Hydrogen direct injection: Optical
investigation of premixed and jet-guided combustion modes, ” Int. J. Hydrogen
Energy 61, 284–295 (2024).
73D. Lejsek, D. Seboldt, P. Leick, R. Grzeszik, M. Frank, and K. G. Stapf,
“Experimental toolchain for evaluation of mixture formation and combustion
in hydrogen engines for light duty applications, ” in 2024 Stuttgart International
Symposium on Automotive and Engine Technology , edited by A. C. Kulzer, H.-
C. Reuss, and A. Wagner (Springer Fachmedien Wiesbaden GmbH,
Wiesbaden, 2024), pp. 102 –129.
74F. Duronio and A. De Vita, “CFD analysis of hydrogen and methane turbulent
transitional under-expanded jets, ” Int. J. Heat Fluid Flow 107, 109381 (2024).
75R. Buttay, G. Lehnasch, and A. Mura, “Turbulent mixing and molecular trans-
port in highly under-expanded hydrogen jets, ” Int. J. Hydrogen Energy 43,
8488–8505 (2018).
Physics of Fluids ARTICLE pubs.aip.org/aip/pof
Phys. Fluids 37, 086158 (2025); doi: 10.1063/5.0277887 37, 086158-17
VC Author(s) 2025
