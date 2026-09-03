<!-- PDF_PAGE: 1 -->

PHYSICAL REVIEW FLUIDS 6, 113601 (2021)
Numerical study of the transcritical shock-droplet interaction
Bradley Boyd * and Dorrin Jarrahbashi
J. Mike Walker ’66 Mechanical Engineering Department, Texas A&M University,
College Station, Texas 77843, USA
(Received 3 May 2021; accepted 25 October 2021; published 15 November 2021)
Transcritical shock-droplet interactions (TSDIs) occur in a spectrum of high-speed
propulsion systems involving liquid fuel injection. “Transcritical” behavior refers to a
condition at which the combustion chamber pressure nears the critical pressure of the fuel-
air mixture and, by increasing the temperature, a transition from liquidlike to gaslike state
is observed. Our understanding of TSDI is signiﬁcantly less developed than its gas-phase
(ideal-gas or supercritical) or liquid-phase (subcritical) counterparts, which are referred
to as shock-bubble interactions (SBIs) and shock-droplet interactions (SDIs), respectively.
In this paper, we investigate the interaction of a shockwave with an n-dodecane droplet
at supercritical pressures. A fully conservative diffuse-interface framework coupled with
the Peng-Robinson equation of state is developed to accurately determine the state of the
ﬂuid and the resulting interfacial instabilities as the shock propagates through the droplet.
The inﬂuence of varying the initial temperature of the fuel, the ambient pressure, and the
shockwave strength on the shock structure and the droplet morphological deformation is
delineated. The dynamics of the TSDI cases are then compared to the subcritical SDI and
supercritical or ideal-gas SBI counterparts. It is shown that, depending on the preshock
temperature and pressure, the TSDIs exhibit some common features observed in classical
cases of SDIs and SBIs, bridging the gap between the sub- and supercritical problems.
DOI: 10.1103/PhysRevFluids.6.113601
I. INTRODUCTION
The design of current and future energy conversion systems is shifting toward supercritical
pressures to enable performance gain and lighter and more reliable systems for space [ 1–7], avi-
ation [8–14], ground transportation [15–20], and power generation [21]. Shock-droplet interactions
(SDIs) occur in a spectrum of high-speed propulsion systems involving liquid fuels including
ramjets and scramjets [ 22,23]. In applications such as high-speed diesel injection, shock waves
may be induced and interact with the fuel spray [ 24]. Shock-bubble interactions (SBIs) and SDIs
have been the subject of many studies over the past decades [ 25–37]. The seminal work of Haas
and Sturtevant [ 38] revealed very complex phenomena occurring during shock interaction with
helium and R22 refrigerant bubbles. Later, these cases were numerically modeled highlighting the
features of the shock-bubble interactions [ 39]. Since then, additional cases have been considered,
including the bubble composition of SF6 and krypton [ 40–54]. However, these studies are all
conducted at atmospheric pressure and room temperature where the ﬂuids are in a gaseous state.
Understanding the disintegration of droplets impacted by shocks at supercritical conditions is
relevant to liquid-fueled scramjet engines during low hypersonic, i.e., start-up operations, and will
inform the mixing and combustion behavior of liquid fuel sprays in a spectrum of supercritical
and high-speed propulsion systems, particularly in hypersonic ﬂights [ 22,23,55,56]. Although a
*bradley.boyd@tamu.edu
2469-990X/2021/6(11)/113601(44) 113601-1 ©2021 American Physical Society

<!-- PDF_PAGE: 2 -->

BRADLEY BOYD AND DORRIN JARRAHBASHI
FIG. 1. Representative state diagram showing the “transcritical” state of an injected fuel. The diagram
is in terms of reduced pressure ( pr = p/pc ) and temperature ( Tr = T/Tc ). In the case of fuel injection into a
combustion chamber, the fuel is injected at supercritical pressure and mixes with the hot ambient air, increasing
the temperature of the fuel. As the fuel is heated, it transitions from a liquidlike to a gaslike supercritical ﬂuid as
it crosses the Nishikawa Widom line—this is termedpseudoboiling and is an example of a transcritical problem
[73,84,85]. The depiction also annotates the classic examples of a subcritical droplet (i.e., water droplet) and
ideal gas (i.e., helium bubble).
better understanding of the sub- and supercritical conditions has been obtained by numerical and
experimental efforts, there is still a criticalgap in the knowledgeon the transcritical conditions where
the transition from liquidlike to gaslike behavior occurs by crossing the pseudoboiling line [57,58].
At transcritical conditions, both subcritical (two-phase) and supercritical (diffusion-controlled)
behaviors might emerge [ 18,19]. Classical transcritical cases involve fuel injected at a pressure
above the critical pressure (the reduced pressurepR = p/pC > 1). In the case of fuel injection into a
combustion chamber, the fuel with a temperature initially below the critical temperature (the reduced
temperature T
R = T/TC < 1) is injected at supercritical pressure, mixes with the hot ambient air,
and increases the temperature of the fuel. As the fuel is heated, it transitions from liquidlike to
gaslike supercritical ﬂuid and crosses the Nishikawa Widom line (termed pseudoboiling)a ss h o w n
in Fig. 1. At temperatures above the critical temperature, the fuel will behave as an ideal gas when
the compressibility factor is equal to unity.
To date, studies of supercritical droplets have focused on low-speed convective environments
where droplet vaporization is signiﬁcantly inﬂuenced by viscous effects and heat conduction. For
example, multiple studies have investigated the behavior of liquid oxygen droplets in a supercritical
hydrogen environment at supercritical conditions [59–62]. A more recent study by Crua et al. [63]
experimentally investigated the convection of hydrocarbon fuel droplets, including n-dodecane,
reporting cases of sustained surface tension. All of these supercritical droplet studies report the
formation of a “crescent shape” [64], “backward-facing bag” [8,63], or “skirt” [62] droplet at later
times. These studies, however, lacked insight into the droplet interaction with a shock wave or
113601-2

<!-- PDF_PAGE: 3 -->

NUMERICAL STUDY OF THE TRANSCRITICAL …
high-speed ﬂow, where the inﬂuence of the diffuse effects (i.e., viscosity and thermal diffusion) and
the surface tension force is expected to be negligible, especially in the early stages of the droplet
development.
For the design of high-pressure and high-speed propulsion systems, it is of great interest to
understand the behavior of fuel droplets impacted by shockwaves at pressures above the critical
pressure. The lack of knowledge on multiphase shock-driven instabilities due to the dearth of
detailed experimental data at such high pressure (and temperature) is the main motivation behind
this computational study that focuses on the shock interaction with fuel droplets at near-critical
conditions.
There are many reports on simulations of SDI using sharp-interface and diffuse-interface ap-
proaches at subcritical conditions [ 32,65–69]. However, there are only two reports that simulate
the fuel droplet-shock interaction at transcritical conditions [ 70,71]. To the authors’ knowledge,
the underlying physics behind this problem has not been previously investigated. In our previous
work [71], we brieﬂy considered the shock interaction with an n-dodecane droplet at near-critical
conditions. Here, we consider the shock interaction of droplets above the critical pressure (i.e.,
the reduced pressure p
r > 1) at varying temperatures on either side of the Widom line, i.e., from
subcritical to supercritical temperatures. It is important to note that the physics associated with a
ﬂuid near the critical point is signiﬁcantly different from conventional liquid droplets or ideal-gas
bubbles. For the shock-bubble interaction problem, the sphere of ﬂuid is referred to as a bubble
because it is in a gaseous state, typically an ideal gas, e.g., in a helium gas bubble indicated in Fig.1.
The term droplet is typically associated with a liquid sphere with signiﬁcant surface tension effects,
e.g., the water droplet marked in Fig.1. However, this differentiation breaks down for a supercritical
ﬂuid where gaslike and liquidlike properties better represent the state of the ﬂuid [ 72] (Fig. 1).
Although at supercritical conditions surface tension is typically neglected [ 19,73–83], we use the
term droplet for the fuel sphere at all tested conditions in this paper. The main research questions to
be answered in this paper include (1) how the interfacial hydrodynamic instability mechanisms and
mixing behavior change during the transition between sub- and supercritical regimes and (2) how
the droplet disintegration behavior at transcritical conditions is related to the classical SDI and SBI.
Finally, how does the variation in Mach number, pressure, and temperature affect the physics of the
transcritical SDI (TSDI)?
In the present paper, we ﬁrst describe the numerical methodology (Sec.II). Finally, we investigate
the shock interaction with the supercritical fuel sphere (Sec. III) by analyzing the physics of
the interaction including shock characteristics, instability development, droplet deformation, and
induced vorticity. The results consider the inﬂuence of varying temperature, pressure, and shock
strength on the TSDI.
II. METHODOLOGY
A. Governing equations
We consider a compressible, inviscid, multiphase model. The governing equations for a diffuse-
interface two-species system, including the conservation of mass, species, momentum, and total
energy, are given below:
∂ρ
∂t +∇· (ρu) = 0, (1)
∂(ρYD )
∂t +∇· (ρuYD ) = 0, (2)
∂(ρu)
∂t +∇· (ρu ⊗ u + pI) = 0, (3)
∂E
∂t +∇· [u(E + p)] = 0, (4)
113601-3

<!-- PDF_PAGE: 4 -->

BRADLEY BOYD AND DORRIN JARRAHBASHI
where YD is the mass fraction of the bubble or droplet ﬂuid species,ρ is the density, u is the velocity
vector, p is the pressure, E is the total energy E = ρ(e +| u|2/2), e is the internal energy, and I
is the identity matrix. The mass fraction of the second species of the two-component system ( D
and S representing the droplet or bubble and the surrounding ﬂuids, respectively) is given by the
mixture rule YS = 1 − YD. The system of equations, Eqs. (1)–(4), is closed using the Peng-Robinson
equation of state (PR-EoS) [86]a sf o l l o w s :
p = RU T
Vm − b − a
V 2m + 2bVm − b2 , (5)
where T is the temperature, RU is the universal gas constant, Vm is the molar volume Vm = M/ρ,
M is the molar mass, and a and b are coefﬁcients that depend on the state and composition of the
ﬂuid. The PR-EoS is modiﬁed [ 71] to approximate the state of the ﬂuid in the vapor dome region
to increase the robustness of the numerical method. This is important at the interface where the
binary mixture may result in phase separation in small regions. Because these regions are small, the
approximation has an insigniﬁcant inﬂuence on the shock transmission across the ﬂuid interface.
The parameters for the NASA polynomials that are used to determine the internal energy, enthalpy,
and entropy were adopted from Ref. [87].
The present model neglects surface tension and the diffuse terms including molecular diffusion,
viscous effects, thermal conduction, and chemical reactions. Surface tension is typically neglected
in transcritical ﬂows [19,73–83] as the surface tension coefﬁcient drops dramatically at the critical
point. The viscous effects and thermal conduction may be important for longer duration simulations
or low-speed cases; however, we found that for the cases considered in the present paper the thermal
and viscous terms are insigniﬁcant. For the sake of brevity, we did not include the cases including
thermal and viscous terms. The interested reader is referred to the work of Ma et al. [73,88].
Similarly, the molecular diffusion is expected to be negligible as it has been shown in earlier studies
[88] that the diffuse effects are typically less than the numerical diffusion of the numerical model
and, thus, no additional insight is gained by the inclusion of the diffuse terms.
We consider the TSDI problem in idealized two-dimensional (2D) axisymmetric cylindrical
coordinates to reduce the high computational costs inherited in the three-dimensional model. In
Chen et al. [25], it was stated that interfacial instabilities that arise in cylindrical coordinates
are less physical than in 2D Cartesian coordinates. However, we simulated the cases in both
2D Cartesian coordinates (shock-column interactions) and 2D cylindrical coordinates, and the
comparison showed qualitatively insigniﬁcant changes to the shock-droplet interaction. We adopted
the 2D axisymmetric coordinates for modeling the early stages of the droplet breakup in this
paper.
This paper uses
DIMP-CFD code, which is an in-house, density-based, ﬁnite volume solver in
C++ parallelized using domain decomposition and the message passing interface (MPI), which is
presented in Ref. [ 71]. In the same study, we introduced a hybrid (HY) numerical method, which
hybridizes the fully-conservate (FC) procedure with the double-ﬂux (DF) method [71]. HY method
is chosen for this paper as our earlier study proved that the HY method can signiﬁcantly reduce
the magnitude of pressure oscillation while limiting the loss of energy conservation when a shock
impacts the nitrogen–n-dodecane interface. To avoid the interaction of the characteristic ﬁelds and
increase the robustness and stability of the solver, we reconstruct the primitive variables in the
characteristic space, i.e., characteristicwise (CW) reconstruction [71,89–92].
The temporal discretization of Eqs. ( 1)–(4) uses the third-order total-variation-diminishing
Runge-Kutta scheme (RK3-TVD) [93] with a CFL equal to 0.8. The Harten–Lax–van Leer-contact
(HLLC) approximate Riemann ﬂux is used to determine the Godunov ﬂux at the cell interfaces
[89,94,95]. Additionally, we make use of a maximum-principle-satisfying and positivity-preserving
ﬂux limiter to help ensure the boundness of the mass fraction and the positivity of density and
pressure [94–96].
Weighted essentially non-oscillatory (WENO)5-CW reconstruction is performed in the axisym-
metric cylindrical coordinates–r, z (see AppendixC of Ref. [97] for more details). We also apply the
113601-4

<!-- PDF_PAGE: 5 -->

NUMERICAL STUDY OF THE TRANSCRITICAL …
artiﬁcial interface thickening method as discussed in our earlier study [71] to the initial condition of
the droplet interface in axisymmetric cylindrical coordinates with β = 2, where β is the number of
ﬁnite volume cells the interface is initially smeared over. The interface thickening reduces the jump
in properties between cells, reducing pressure oscillations and increasing the numerical stability
[71]. Additionally, interface thickening reduces the loss in energy conservation when used with a
quasiconservative method like the HY method developed by the authors [ 71]. Because the droplet
is deﬁned on a uniform Cartesian mesh, this interfacial thickening also helps provide the smooth
curvature of the initial droplet shape. For the higher strength shock problems presented later in this
paper, we further increase the stability by reducing the order of reconstruction to WENO3, and for
the Mach 2 shock case we also make use of a minmod ﬂux limiter based on the gradient in the mass
fraction [33].
B. Flow visualization
Computational Schlieren images are used to visualize features involving density gradients: ma-
terial interfaces, shock waves, and rarefaction waves [39,94]. The computational Schlieren images
are generated using a shading function (φ) deﬁned as
φ = exp
(
−k |/Delta1ρ|
|/Delta1ρ|max
)
(6)
where the parameter k is assigned to each ﬂuid component to accentuate the compressible ﬂow
features. For the two-component cases presented (i.e., He-N2 and R22-N2), we use k = 120 for the
denser component (i.e., R22) and k = 600 for the less dense component (i.e., He) as is suggested
in Ref. [ 39]. For example, in the fuel shock-droplet interaction case, k = 120 for the n-dodecane
droplet, and k = 600 for the surrounding nitrogen.
Additionally, vorticity (ω) is visualized by computing the curl of the velocity ﬁeld: ∇× u.T h e
total ﬂow circulation (/Gamma1) is computed by numerical integration of the vorticity in the computational
domain. It was suggested in Ref. [ 48] that in the early stages of a shock-bubble interaction the
primary source of vorticity generation is the baroclinic term. The baroclinicity of the ﬂow is the
misalignment of the local pressure and density gradients as represented by
1
ρ2 (∇ρ×∇ p). For
reference, the vorticity transport equation for an inviscid ﬂow is
Dω
Dt =
baroclinic term  
1
ρ2 (∇ρ×∇ p) + (ω ·∇ )u − ω(∇· u) (7)
C. Validation cases: Shock-bubble interaction and shock-droplet interaction
In Appendix B, the model is validated using the two extensively considered SBI problems: (1)
the helium bubble case and (2) the R22 refrigerant case. To the authors’ knowledge, this is the
ﬁrst time the real-gas equation of state (PR-EoS) has been used to simulate the SBI. The other
numerical studies in the literature that use these validation cases typically use the stiffened EoS
that simpliﬁes to the ideal-gas law for gases [ 39,89,97–106]. Additionally, we brieﬂy consider the
commonly studied SDI involving a water droplet for comparative purposes (Appendix C).
D. Critical parameters
Here, we introduce the important parameters that change the behavior shock-droplet interaction.
The speed of sound (SoS) ratio, that is, the ratio of the SoS between the surrounding ﬂuid and the
bubble or droplet ﬂuid, is
n = c
S
cD
(8)
113601-5

<!-- PDF_PAGE: 6 -->

BRADLEY BOYD AND DORRIN JARRAHBASHI
FIG. 2. Schematic of (a) the classic helium diverging case ( n < 1) and (b) a R22 converging case (n > 1).
The red contour line shows the material interface at αD = 0.95, where α is the volume fraction.
where c is the SoS, and subscripts D and S denote the bubble or droplet and surrounding ﬂuid,
respectively. The ratio of the SoS is an important parameter as it indicates if the refracted shock is
going to diverge or converge upon interaction with the bubble or droplet (Fig. 2). If the SoS with
the bubble or droplet is greater than the surrounding ﬂuid ( n < 1), then the refracted shock within
the bubble moves ahead of the incident shock [Fig. 2(a)]—a situation that is commonly accepted
in the literature as “divergent,” e.g., the helium bubble case [ 38,92] as is shown in Appendix B.
Alternatively, if the SoS within the bubble or droplet is less than the surrounding ﬂuid (n > 1), then
the refracted shock within the bubble lags behind the incident shockwave and causes the incident
shock to focus on the downstream pole of the bubble [Fig. 2(b)] and produce an intense jump in
pressure at the focal point as will be shown later. This conﬁguration is referred to as “convergent”
and reported for the R22 bubble case [38,92] (see Appendix B).
The next parameter that is associated with the shock-bubble interaction is the acoustic impedance
mismatch across the material interface. The acoustic impedance mismatch for a material interface
is represented as
δZ = (ρc)
D − (ρc)S. (9)
Acoustic impedance mismatch inﬂuences the transition of a shock wave across the material in-
terface. When the incident shock reaches the interface, the shock wave is refracted and a rarefaction
or shock wave is reﬂected [48]. If the impedance mismatch is greater than zero ( δZ > 0), then the
reﬂected wave is a shock wave. Otherwise, if the impedance mismatch is less than zero ( δZ < 0)
then the reﬂected wave is a rarefaction wave. Thus, for the helium case, the reﬂected wave is a
rarefaction wave, and for the R22 case the reﬂected wave is a shock wave [ 48]. Once the refracted
shock that is passing through the bubble reaches the downstream interface, the opposite impedance
mismatch is present. As a result, the internally reﬂected wave is a shock wave for the helium case
and a rarefaction wave for the R22 case.
Another parameter that is typically considered in shock-bubble interaction problems is the
Atwood number deﬁned as
A = (ρ
D − ρS )
(ρD + ρS ). (10)
The Atwood number indicates the effect of the density change between the bubble or droplet
and surrounding ﬂuid. It is noted that both the Atwood number ( A) and the acoustic impedance
mismatch (δZ) are typically used in the literature to classify SBI problems involving divergent or
113601-6

<!-- PDF_PAGE: 7 -->

NUMERICAL STUDY OF THE TRANSCRITICAL …
convergent cases; e.g., δZ > 0 is reported as convergent, while δZ < 0 is considered as divergent
[46,48,107]. The Atwood number and impedance mismatch are important parameters in classifying
shock-bubble interaction problems; however, it has been shown that the diverging and converging
behavior can be better deﬁned using the SoS ratio ( n)[ 38,44]. In this paper, we will consider the
inﬂuence of all the key parameters: A, δZ, and n.
E. Computational experiments
Here, we consider the interaction of a shock wave in a nitrogen environment with a sphere of n-
dodecane at supercritical pressure in a liquidlike or gaslike supercritical state to showcase the shock
interaction with a transcritical or near-critical droplet (TSDI). In transcritical injection problems,
a liquid fuel, initially at subcritical temperatures, is injected into an environment at supercritical
pressure and temperatures with respect to the fuel. As the fuel is heated by the ambient environment,
its temperature increases from subcritical to supercritical by crossing the pseudoboiling (Widom)
line. During this transition, the fuel properties vary from a liquidlike to a gaslike state (Fig. 1). We
focus on investigating the shock-droplet interaction state near the Widom line to provide insight
into the behavior of the fuel for transcritical scenarios; hence, the term transcritical shock-droplet
interaction. In this paper, we focus on then-dodecane as the fuel asn-dodecane has been extensively
used as a diesel fuel surrogate in the combustion community [ 19,73,75,108]. The n-dodecane has
a critical temperature of T
C = 658.1 K and critical pressure of pC = 1.82 MPa. The nitrogen has a
critical temperature of TC = 126.2 K and critical pressure of pC = 3.369 MPa.
The key changes to then-dodecane and nitrogen system with respect to temperature and pressure
are depicted in Fig. 3. The SoS of the nitrogen increases [Fig. 3(a)] and its density decreases
[Fig. 3(b)] from 500 and 800 K. The SoS of the n-dodecane drops to a minimum near its critical
temperature (658.1 K) and then begins to rise [Fig. 3(a)]. The density of the n-dodecane also drops
as the temperature increases past the critical temperature [Fig. 3(b)], coinciding with the transition
from a liquidlike to a gaslike supercritical ﬂuid. The transition from liquidlike to gaslike across the
Widom line (Fig. 1) and the point of transition is associated with the peak in the speciﬁc isobaric
heat capacity (c
p) as is evident in Fig. 3.
At the lowest pressure (2 MPa), which is slightly above the critical pressure of n-dodecane
(pC = 1.82 MPa), there is an abrupt change in the SoS and density at the pseudoboiling point by
crossing the Widom line near the critical pressure [ 84,85]. The peak in the speciﬁc isobaric heat
capacity reduces with increasing pressure as shown in Fig. 3(c). Additionally, the minimum SoS of
n-dodecane increases with increasing pressure, and as a result the peak in the SoS ratio ( n) reduces
[Fig. 3(d)]. The change in the SoS near the critical pressure means that, for the preshock pressure of
2 MPa, the SoS ratio reaches a large peak of aboutn ≈ 6 when T ≈ TC = 658.1 K. As the preshock
pressure increases and the changes in properties across the Widom line become less pronounced,
we also see a drop in the peak of the SoS ratio. At preshock pressure of 10 MPa, far above the
critical pressure, there is no apparent peak in n [Fig. 3(d)]. The importance of n for the TSDI will
be discussed next. In Fig. 4, we present all the cases considered in this paper that span a wide range
of pressures and temperatures.
F . Computational model
The shock wave travels from right to left, impacting the droplet, where the initial droplet diameter
is D0 = 5[cm]. The nondimensional variables are in terms of D0: z∗ = z/D0 and r∗ = r/D0.T h e
computational domain /Omega1= [−5D0, 5D0] × [0, 6D0] is shown in Fig. 5. The size of the compu-
tational domain is sufﬁciently large so that potential erroneous reﬂections from the nonreﬂective
boundaries will not interact with the droplet throughout the simulation. The computational domain
consists of a uniform mesh from z
∗ =− 3.2t o 3.2 and from the axis of symmetry to r∗ = 1t o
increase the computational speed of the simulation where the cell dimensions are /Delta1z∗ ≈ /Delta1r∗ ≈
4.6 × 10−3. The mesh then grows at a rate of 10% in the z and r directions to the outer boundaries.
113601-7

<!-- PDF_PAGE: 8 -->

BRADLEY BOYD AND DORRIN JARRAHBASHI
FIG. 3. The change in (a) SoS, (b) density, (c) speciﬁc isobaric heat capacity ( cp), and (d) speed of
sound ratio (n) with respect to temperature at varying pressures. The vertical dotted line indicates the critical
temperature of n-dodecane (658.1 K).
Due to the axis of symmetry boundary condition, only the top half of the depicted computational
domain is required for the simulation (Fig.5). A transmissive boundary condition is used at the other
boundaries (left, right, and outer boundaries). The initial state of the three regions, (1) preshock, (2)
postshock, and (3) the n-dodecane droplet, is summarized below:
(Y
D, uz, p, T,ρ ) =
⎧
⎨
⎩
(0, 0, pPRE, TPRE,ρ PRE ) preshock
(0, uz,POST, pPOST, TPOST,ρ POST ) postshock
(1, 0, pPRE, TPRE,ρ D ) droplet
. (11)
Note that uz is the velocity component in the z direction and the initial velocity in the r direction
(ur ) is zero everywhere. The pre- and postshock conditions are outlined in AppendixA (TablesI–III)
for all test cases.
113601-8

<!-- PDF_PAGE: 9 -->

NUMERICAL STUDY OF THE TRANSCRITICAL …
FIG. 4. State of the shock-droplet computational cases (1–9) on the n-dodecane phase diagram. The green
dotted line indicates the transition line where the speed of sound ratio is n = 1 (Sec. III A 1) and the red dotted
line indicates where n = 1.48, which we later ﬁnd to be the transition from weak to strong convergent behavior
(Sec. III B 1).
The shock wave, which is initially at z∗ = 2, travels to the left towards the droplet. For this
paper, we also make use of the nondimensional breakup time (t∗) derived from the analysis of SDI
considering the droplet displacement assuming a constant acceleration due to drag [32,109]:
t∗ = t uz,POST
D0
√ρPOST
ρD
(12)
where t begins when the shock ﬁrst impacts the droplet interface at z∗ = 1.5. This nondimensional
breakup time is useful for comparing the instability development of the droplet at later times when
the primary shock interactions are complete.
III. RESULTS AND DISCUSSION
First, we show the key features of the TSDI for a special case where n = 1. Consider the
case where TPRE = 545.7K , pPRE = 6 MPa (see Fig. 4), and the incident shock wave is Mach
1.2 (Fig. 6). Note that the time ( t) begins when the leftward traveling incident shock reaches
the droplet interface [Fig. 6(a)]. Once the shock impacts the droplet, the vertical incident shock
above and below the droplet is joined by two shock waves: (1) the refracted shock that lies within
the droplet and (2) the reﬂected shock that is outside the droplet [Fig. 6(b)]. The passage of the
refracted shock across the downstream interface results in a transmitted shock and the reﬂection
113601-9

<!-- PDF_PAGE: 10 -->

BRADLEY BOYD AND DORRIN JARRAHBASHI
FIG. 5. Depiction of the transcritical shock-droplet case. The depicted cell size is ten times larger than
the cell size used in the simulations ( /Delta1z∗ ≈ /Delta1r∗ ≈ 4.6 × 10−3). Due to the axis of the symmetry boundary
condition, only the top half of the depicted computational domain is required for the simulation.
of a rarefaction wave [Fig. 6(c)]. The acoustic impedance mismatch experienced by the incident
shock impacting the droplet isδZ > 0; however, the internal shock experiences the opposite acoustic
impedance mismatch (i.e., δZ < 0) when interacting with the downstream interface of the droplet.
The subsequent acoustic impedance mismatch experienced by the refracted shock results in the
internal reﬂection of a rarefaction wave (see Fig. 3 of Ref. [ 48] for details). As time progresses,
interfacial instabilities begin to grow at the interface between the fuel and the surrounding nitrogen
[Fig. 6(d)].
A. Inﬂuence of the preshock temperature
We investigate the inﬂuence of varying the initial temperature ( TPRE ) of the droplet and the
ambient nitrogen. The cases considered are 500, 545.7, 650, and 800 K (see Fig. 4) and the initial
conditions are presented in Table I. Note that 500, 545.7, 650, and 800 K correspond to the reduced
temperatures with respect to the critical temperature of n-dodecane (TR ), which are approximately
0.76, 0.83, 0.99, and 1.22, respectively.
113601-10

<!-- PDF_PAGE: 11 -->

NUMERICAL STUDY OF THE TRANSCRITICAL …
FIG. 6. Computational Schlieren images for the Mach 1.2 shock interaction with a fuel ( n-dodecane)
droplet (TPRE = 545.7Ka n d pPRE = 6M P a )a t( a )0μs, (b) 36 μs, (c) 96 μs, and (d) 455 μs.
1. The transition from diverging to converging behavior
An important result of varying the temperature, TPRE, is the changes to the SoS. The variations
in the SoS with respect to temperature for nitrogen and n-dodecane are depicted in Fig. 7(a).T h e
SoS for the surrounding ﬂuid (nitrogen) increases with increasing temperature whereas the SoS for
the fuel droplet (n-dodecane) reduces to a minimum near the pseudoboiling point [Fig. 7(a)]. Note
that the pseudoboiling point for n-dodecane at 6 MPa occurs at the peak in the speciﬁc isobaric
heat capacity at 730 K, where the fuel transitions from a liquidlike to a gaslike supercritical ﬂuid
[Fig. 7(c)].
As discussed in Sec.II D in conjunction with Fig.2, the classiﬁcation of diverging [Fig.2(a)] and
converging [Fig. 2(b)] cases is achieved using the ratio between the SoS of the surrounding ﬂuid
and the fuel droplet, n [Eq. (8)]. In Fig. 7(d), we show the change in n with respect to temperature.
When the ratio, n, is less than unity (i.e., 500 K), it becomes a diverging shock-droplet interaction
[Fig. 7(d)] whereas when the ratio, n, is greater than unity (i.e., 650 or 800 K) it implies that the
113601-11

<!-- PDF_PAGE: 12 -->

BRADLEY BOYD AND DORRIN JARRAHBASHI
FIG. 7. (a) SoS and (b) density variation with respect to the temperature for nitrogen and n-dodecane at
6 MPa. (c) Change in speciﬁc isobaric heat capacity for the n-dodecane, where the red dotted line corresponds
to the pseudoboiling point temperature (T∗)o f n-dodecane where the speciﬁc isobaric heat capacity reaches a
peak. The depiction includes the change in (d) the SoS ratio (n), (e) the acoustic impedance mismatch (δZ), and
(f) the Atwood number (A). The blue dotted line is the temperature (545.7 K) where the SoS of then-dodecane
and the nitrogen are equivalent (≈487 m/s, n = 1).
shock-droplet interaction is converging. The transitional point from diverging to converging (n = 1)
occurs at approximately 545.7 K at 6 MPa. Additionally, Fig. 4 shows a green dotted line on the
phase diagram where n = 1.
Figure 8 elucidates the transition from a diverging ( n < 1) to a converging ( n > 1) refracted
shock wave. The 500-K case is an example of a diverging case where the SoS is greater in the droplet
than in the surrounding ﬂuid, resulting in a diverging refracted shock [Fig. 8(a)]. The 650-K case
is an example of a case where the SoS is less in the droplet than in the surrounding ﬂuid, resulting
in a converging refracted shock wave [Fig. 8(c)]. For the 545.7-K case, the refracted shock wave
travels at approximately the same speed as the incident shock and, therefore, is neither diverging
nor converging [Fig. 8(b)].
The TSDI differs signiﬁcantly from classical SDI and SBI interactions. Throughout the following
sections, we make comparisons with these classic SBI and SDI cases that are presented in Appen-
dices B and C.I nF i g .8, the subcritical liquid water SDI (divergent) case [Fig. 8(d)], the classic
divergent SBI case [helium bubble, Fig. 8(e)], and the classic convergent SBI case [R22 bubble,
Fig. 8(f)] are compared. The convergent fuel-droplet case [Fig.8(c)] and the classic convergent SBI
case [Fig. 8(e)] exhibit the same shock-interaction behavior. The key differences are between the
fuel-droplet divergent case [Fig. 8(a)] and the classic divergent SBI case [Fig. 8(d)]. As discussed
previously, in the classic divergent SBI case, the reﬂected wave is a rarefaction wave; however, in
the fuel-droplet divergent case [Fig. 8(a)], the reﬂected wave is a shock wave due to the impedance
113601-12

<!-- PDF_PAGE: 13 -->

NUMERICAL STUDY OF THE TRANSCRITICAL …
FIG. 8. Depiction of the three TSDI cases that differ in temperature: (a) 500 K ( n = 0.78), (b) 545.7 K
(n = 1), and (c) 650 K (n = 1.8). As a result, the refracted shock behavior changes from a diverging shock to a
converging shock case. Additionally, (d) shows the divergent water SDI case, (e) shows the divergent SBI case
(helium bubble), and (f) shows the convergent SBI case (R22 bubble).
mismatch (δZ) [Fig. 7(e)]. This also means that the diverging fuel-droplet case [Fig. 8(a)] does
not exhibit the twin regular reﬂection-refraction (TRR) formation of the classic diverging case
[Fig. 8(e)]—the TRR formation is described in detail in Appendix B and annotated in Fig. 26.T h e
fuel-droplet divergent case [Fig. 8(a)] has more in common with the divergent water droplet SDI
case [Fig. 8(d)]—both cases result in a reﬂected shock wave due to the positive acoustic impedance
mismatch (δZ). The key difference is that the acoustic impedance is much higher in the water droplet
case and, as a result, the refracted shock is far weaker.
The TSDI provides an interesting link between the subcritical liquid SDI and supercritical or
ideal-gas SBI. The diverging TSDI, where the fuel is in aliquidlike state, results in a diverging case
where the shockwave behavior is like the classic subcritical liquid SDI, whereas the converging
TSDI, where the fuel is in a gaslike state, results in similar shock behavior to the classic converging
ideal-gas SBI. We will compare the later-time behavior of TSDI, SBI, and SDI in Fig. 12.
Figure 9 compares the temporal evolution of the TSDI of a converging case ( n = 1.8) and a
diverging case (n = 0.75) depicted using computational Schlieren images. For the diverging cases,
the refracted shock wave moves ahead of the incident shock as it approaches the downstream face
of the droplet [Fig. 9(a)]. The refracted wave is then reﬂected [Fig. 9(b)] and converges to a point
[Figs. 9(c) and 9(d)].
For all the TSDI cases, the initial interaction of the shock wave and the droplet results in a
high-pressure region between the refracted shockwave and the reﬂected shockwave [Figs. 10(a),
10(c), and 10(e)] that exceeds the postshock pressure of the incident normal shock wave (i.e.,
greater than 9 MPa). The focusing of the reﬂected wave within the droplet results in a low-pressure
region where the pressure is well below the critical pressure ofn-dodecane [Fig. 10(b)]. In this case,
113601-13

<!-- PDF_PAGE: 14 -->

BRADLEY BOYD AND DORRIN JARRAHBASHI
FIG. 9. Comparison of the (a)–(c) diverging case (500 K,n = 0.78) and the (d)–(f) converging case (650 K,
n = 1.8).
the low-pressure region reaches a minimum of 0.5 MPa [Fig. 10(b)] which is below the critical
pressure for the n-dodecane (1.82 MPa). This is a unique diverging case because it has a positive
acoustic impedance mismatch [Fig. 8(a)] and, therefore, the internally reﬂected rarefaction wave.
Typically, divergent cases have a negative impedance mismatch which is the case for the helium
bubble validation problem [Fig. 8(d)] which, instead, results in an internally reﬂected shock wave
as is shown in Fig. 26(d).
Conversely, as time progresses for the converging TSDI cases, the lower SoS in the n-dodecane
(i.e., n = 1.8) becomes more apparent as the refracted shock lags further behind the incident shock
as shown in Fig. 9(d). The shock wave dynamics of the convergent TSDI cases are consistent with
the R22 convergent SBI case ( n > 1) [see Figs. 28(a)–28(c) and 29(a)–29(c) or Ref. [ 39]]. The
113601-14

<!-- PDF_PAGE: 15 -->

NUMERICAL STUDY OF THE TRANSCRITICAL …
FIG. 10. Depiction of the diverging case (a), (b) TPRE = 500 K where the reﬂection of the refracted shock
results in a localized low-pressure region compared to the converging cases—(c), (d) TPRE = 650 K and (e),
(f) TPRE = 800 K—when the converging refracted shock wave reaches a focal point, resulting in high localized
pressures. The top half of the frame is the computational Schlieren image, and the bottom half of the frame is
the pressure distribution.
113601-15

<!-- PDF_PAGE: 16 -->

BRADLEY BOYD AND DORRIN JARRAHBASHI
refracted wave converges to a focal point as is annotated in Fig. 9(e) resulting in the emission of a
transmitted shock wave annotated in Fig. 9(f).
The computational Schlieren images and pressure distribution at the time of full convergence to
the focal point are depicted in Figs. 10(d) and 10(f) for the two convergent cases (650- and 800-K
cases). The focal point of the refracted shock convergence results in high localized pressure on the
downstream side of the droplet [Figs.10(d) and 10(f)]. For the 650-K case (n = 1.8), the maximum
pressure is 36 MPa, whereas for the 800-K case (n = 3.1) the maximum pressure is about 45 MPa.
Note that, as n increases, the focal point of the converging shock moves inward [further away from
the downstream interface, Figs. 10(d) and 10(f)]. A peak in n is found to occur at about 800 K [see
Fig. 7(d)]. The localized maximum pressure caused by the convergence of the refracted shock wave
results in the formation of an axial jet that will be illustrated in detail in Fig. 11. If the convergence
occurs within the droplet, this jet is directed outwards [Figs.10(d) and 10(f)]. This phenomenon has
been observed for the convergent R22 SBI case [38,39] [Figs. 28(e)–28(h) and 29(e)–29(h)].
To further investigate the jet formation in converging cases, in Fig.11, we focus on the temporal
variation of the axial pressure for the 650-K case where the refracted shock convergence occurs
just inside the droplet near the downstream interface. Figure 11(a) shows the point in time where
the refracted shock has fully wrapped around the undisturbed droplet region and is near the focal
point. Figure 11(b) shows the axial pressure distribution before the shock wave convergence, where
the leftward traveling shock exhibits a signiﬁcant pressure peak of about 18 MPa. There is no more
undisturbed region once the shock converges [Fig. 11(c)] and the peak pressure at the axis near the
downstream interface reaches about 30 MPa [Fig. 11(d)]. After the shock convergence, the shock
wave is reﬂected as a strong rarefaction wave as seen in Figs. 11(e) and 11(f) where the pressure
drops to below 5 MPa.
In Fig. 12, we compare the fuel droplet shape with the SDI and SBI cases at later times (t
∗ = 0.6).
It is immediately apparent from Fig. 12 that the TSDI droplet shape expands radially like the SDI
case [Fig. 12(b)] and develops interfacial instability comparable to the R22 SBI [Fig. 12(b)]. The
helium SBI results in a very different shape—a kidney-shaped formation [Fig. 12(d)]—due to the
very low density of the helium bubble compared to the surrounding air (see Appendix B for more
details). The primary differences between these cases are related to the density ratio ( ρD/ρS ). At
supercritical pressures, the density ratio between the fuel droplet and the surrounding nitrogen
(ρD/ρS )v a r i e sf r o m≈9t o ≈31 for the cases considered in the present paper, whereas the density
ratio ranges from ≈0.14 (helium) to ≈3.1 (R22) for the SBI cases and ≈831 for the SDI case
(water). Hence, the TSDI droplet shape [Fig. 12(a), ρD/ρS = 14] exhibits similarities with the SDI
[Fig. 12(b), ρD/ρS = 833] and the R22 SBI [Fig.12(c), ρD/ρS = 3.1], and has less in common with
the helium SBI [Fig. 12(d), ρD/ρS = 0.14].
2. V orticity generation and ﬂow circulation
Quantifying the vorticity deposition is of interest when analyzing the physical mechanisms that
occur during SDI or SBI interactions (Appendices B and C). Like the classical SDI and SBI cases,
the hydrodynamic instabilities at the interface in TSDI are initiated by impulsively accelerating
two ﬂuids of different densities—Richtmyer-Meshkov instability (RMI) [ 110,111]. This creates
a baroclinic vorticity deposition on the interface. To better understand the growth of instabilities
at later times, and eventually the breakup process, we start with portraying the evolution of the
baroclinic vorticity in TSDI.
As discussed earlier (Sec. II B), the primary source of vorticity is the baroclinic vorticity due
to the misalignments of local pressure and density gradients of the interface, that is,
1
ρ2 ∇ρ×∇ p
[see Eq. ( 7)], and the passage of the shock across the droplet results in signiﬁcant generation of
baroclinic vorticity. For the three TPRE cases, the shock wave pressure gradients ( ∇ p) are almost
equivalent for the Mach 1.2 shock wave in nitrogen as outlined in Table I. This is because the
pressure jump across a normal shock depends on (1) the shock strength (i.e., Mach 1.2) and the (2)
speciﬁc heat ratio (γ) of the ﬂuid (γ of nitrogen only varies between 1.446 and 1.391 from 500 to
113601-16

<!-- PDF_PAGE: 17 -->

NUMERICAL STUDY OF THE TRANSCRITICAL …
FIG. 11. The computational Schlieren images (a), (c), (e) and the corresponding axial pressure distributions
(b), (d), (f) for TPRE = 650 K, pPRE = 6 MPa, and Mach 1.2. The depiction shows the shock convergence
resulting in a localized high-pressure region inside the downstream droplet interface. The pressure peak in
(d) causes the formation of an axial jet.
800 K). The density gradient, however, varies signiﬁcantly as the droplet, which is at supercritical
pressure, transitions from a liquidlike to a gaslike supercritical ﬂuid [Fig. 3(b)]. The density and
vorticity distributions for the three cases (500, 650, and 800 K) are depicted in Fig. 13 for the
same nondimensional time t∗ = 0.38. The higher density of the droplet compared to the nitrogen
environment results in the generation of positive vorticity as the shock wave propagates through the
droplet as shown in Fig.13. Another unique feature of the TSDI is that the rotational direction of the
generated baroclinic vorticity is the same for both the divergent and convergent cases (Fig. 13). In
the divergent (helium) and convergent (R22) SBI cases, the vorticity rotation direction of the helium
bubble case is in the opposite direction to the vorticity of the R22 case (Fig. 30): this is due to the
low density of the helium bubble case (A< 0) and the high density of the R22 case (A> 0) [48]. For
113601-17

<!-- PDF_PAGE: 18 -->

BRADLEY BOYD AND DORRIN JARRAHBASHI
FIG. 12. (a) The droplet shape for the TSDI after the shock interaction compared to (b) the SDI where the
droplet is water and the SBI cases: (c) R22 and (d) helium. Note that the nondimensional breakup time is less
relevant for the helium SBI case, hence the greater value of t∗ = 1.5i n( d ) .
the n-dodecane droplet, the Atwood number is always positive [Fig.7(f)] and, therefore, the bulk of
the vorticity generation is positive for a shock wave traveling from right to left past the droplet.
The total ﬂow circulation for the same cases (i.e., TPRE = 500, 650, and 800 K) is shown in
Fig. 14(a).I nF i g .14, the beginning of the shock crossover is indicated by the plus symbols (+) and
the ﬁrst appearance of the transmitted shock is indicated by a closed circle symbol ( •). Figure 14
includes the computational Schlieren images when the crossover shock ﬁrst appears [Fig. 14(b),
800 K; Fig.14(e), 500 K] and when the transmitted shock ﬁrst appears [Fig.14(c), 800 K; Fig.14(d),
500 K]. In the divergent case (500 K), the transmitted shock appears before the crossover begins
because the refracted shock reaches the downstream interface long before the incident shock is
diffracted around the droplet. In the convergent cases (650 and 800 K), where the transmitted shock
appears after the crossover point, there is a drop in ﬂow circulation after the appearance of the
transmitted shock due to the transmitted shock interacting strongly with the droplet interface. This
behavior is consistent with the R22 convergent SBI case (Fig. 31).
Figure 14(a) demonstrates that the ﬂow circulation increases rapidly as the incident shock passes
over the droplet and interacts with the n-dodecane and nitrogen interface until the shock crossover.
It is also interesting to note that this initial rate of circulation increases with increasing temperature
[Fig. 14(a)]. After the primary shock interactions are complete, the circulation more gradually
increases (Fig. 14) due to the development of the interfacial instabilities as the droplet is accelerated
by the postshock ﬂow.
113601-18

<!-- PDF_PAGE: 19 -->

NUMERICAL STUDY OF THE TRANSCRITICAL …
FIG. 13. The vorticity (top half) and density (bottom half) distributions for the three TSDI temperature
cases (TPRE: (a) 500 K, (b) 650 K, and (c) 800 K) when t∗ = 0.38.
3. Droplet breakup and instability
In Ref. [ 71], we made a conservative approximation of the surface tension σ ∼ 1 × 10−3N/m
for the fuel TSDI case near the critical temperature. In Ref. [ 112], the Weber number for an SDI is
deﬁned as
We = ρPOSTu2
POSTD0
σ . (13)
For the Mach 1.2 case where TPRE = 650 K and pPRE = 6 MPa, the postshock state is provided
in Table I. In this case, the approximate Weber number is We ∼ 5 × 107. This very large Weber
number is due to the almost negligible surface tension near the critical point. As a result, the
Weber number is We > 10
3, which means the TSDI cases are in the shear-induced entrainment
breakup regime [ 112]. The resultant interfacial instability is shown in Fig. 13. By increasing the
temperature at supercritical pressure, the fuel state changes signiﬁcantly from a liquidlike to a
gaslike supercritical ﬂuid. As a result, the density changes signiﬁcantly as shown in Fig. 13.A l l
three cases show signiﬁcant interfacial instability at the material interface and vorticity at the outer
interface (away from the axis of symmetry).
An interesting feature of the higher temperature case (800 K) is the increase in the interface
instability, especially at the downstream interface near the axis [Fig. 13(c)]. Because n is large, the
shock convergent focal point occurs further from the downstream interface inside the droplet as is
shown in Fig. 10(f). The stronger shock convergence (n = 3.1) results in a transmitted shockwave
that interacts with a larger portion of the downstream interface. The more signiﬁcant interaction of
the transmitted shock wave with the downstream interface promotes interfacial instability.
B. Inﬂuence of the preshock pressure
Here, we consider how the preshock pressure ( pPRE ) may change the TSDI. In Fig. 3,t h e
inﬂuence of the pressure on the key properties of then-dodecane and nitrogen system was presented.
The important ﬁnding is that by changing the pressure we change the SoS ratio [see Fig. 3(c)]. The
three cases we consider vary pPRE from 2 to 6 and 10 MPa, keeping TPRE = 650 K and the shock
wave strength of Mach 1.2 constant. We choseTPRE = 650 K for this paper because it is close to the
critical temperature ofn-dodecane (Fig. 4). It is important to note that the fuel in these pressure cases
is below the pseudoboiling point, so it is in a supercritical liquidlike state (Fig. 3). The SoS ratio
for all the cases discussed in this subsection remains above 1 (n > 1) and, thus, they all represent a
convergent case.
113601-19

<!-- PDF_PAGE: 20 -->

BRADLEY BOYD AND DORRIN JARRAHBASHI
FIG. 14. Circulation of the ﬂow with respect to (a) time ( t ) for the three temperature ( TPRE ) cases (500,
650, and 800 K). The plus symbol ( +) indicates the start of the shockwave crossover and the closed circle
symbol (•) corresponds to the point in time when the transmitted shock ﬁrst appears. The depiction includes
the computational Schlieren images of the appearance of the crossover and transmitted shock for the 800-K
case (b), (c) and the 500-K case (d), (e).
1. Weak and strong converging cases
Figure 15 illustrates the computational Schlieren images of the shock structures for two cases
with a preshock pressure of 6 MPa ( n = 1.8) and 10 MPa ( n = 1.43). In both cases, the refracted
shock travels slower within the droplet and the general shock wave pattern is found to be consistent
with the convergent cases identiﬁed earlier for n > 1. However, the key difference between the
6-MPa (n = 1.8) and 10-MPa ( n = 1.43) cases occurs at the later stages when the refracted shock
nears the downstream interface [Figs. 15(b)–15(d)]. In the 6-MPa ( n = 1.8) case, the outer shock
crossover occurs before the refracted shock reaches the downstream interface, resulting in the
refracted wave convergence to a focal point within the droplet [Fig. 15(d)]. Figure 15(b) shows
that for a lower SoS ratio (n = 1.43) the focal point of the refracted shock doesnot occur within the
droplet because the refracted shock wave reaches the downstream interface of the droplet before the
incident shock has traveled around the droplet Fig. 15(b).
113601-20

<!-- PDF_PAGE: 21 -->

NUMERICAL STUDY OF THE TRANSCRITICAL …
FIG. 15. Computational Schlieren images showing the evolution of the shock convergence for (a), (b) weak
convergence (pPRE = 10 MPa, n = 1.43) and (c), (d) strong convergence (pPRE = 6M P a ,n = 1.8).
Figure 16 shows the pressure variation within the droplet along with the computational Schlieren
images for n = 1.43. Figures 16(a) and 16(b) show that no focal point occurs within the droplet:
instead, the refracted shock reaches the downstream pole. At a higher SoS ratio (i.e., n = 1.8),
however, the incident shock wave travels faster around the outside of the droplet than the axial speed
of the refracted shock speed—this results in a focal convergence point and the peak in pressure at the
downstream interface of the droplet shown in Fig. 11(d). Consequently, instead of an outward axial
jet that was a prominent feature of the convergent case with n = 1.8 (Fig. 11), an inward axial jet
forms for n = 1.43 because of the low pressure of the reﬂected rarefaction wave [Figs.16(c)–16(f)]
and higher downstream pressure of the transmitted shock results in the slight inward deformation of
the downstream interface at the axis of symmetry [Fig. 16(g)]. We are conﬁdent that this behavior
is not a numerical artifact because this inward jet has been experimentally observed for a krypton
SBI case that represents a case where the SoS ratio is about 1.5 ( n ∼ 1.5) (see Fig. 9 of Ref. [52]).
Thus, we refer to the cases with a prominent outward axial jet as strongly convergent and weakly
convergent if the axial jet is directed inward.
Here, we estimate the SoS ratio at which the shock interaction transitions from weakly convergent
[Figs. 15(a) and 15(b)] to strongly convergent [Figs. 15(c) and 15(d)]. The transition case occurs
when the incident shock wave outside the droplet reaches the downstream pole at the same time as
the (internal) refracted shock as is schematically shown in Fig. 17. Assuming the Mach numbers of
the shocks are equivalent (i.e., both Mach 1.2 in this case) and using the radius of the droplet (R)a s
an approximation to the shock curvature, the external shock wave will travel a distance of 3R and the
refracted shock wave will travel 2R to reach the downstream pole (Fig. 17). Therefore, an SoS ratio
of n = 1.5 that would result in the case where the external and internal shocks simultaneously reach
113601-21

<!-- PDF_PAGE: 22 -->

BRADLEY BOYD AND DORRIN JARRAHBASHI
FIG. 16. The computational Schlieren images (a), (c), (e), (g) and the axial pressure distributions (b), (d),
(f), (h) for the pPRE = 10 MPa case which is considered as a weak convergent case wheren = 1.43.
113601-22

<!-- PDF_PAGE: 23 -->

NUMERICAL STUDY OF THE TRANSCRITICAL …
FIG. 17. Schematic of the approximate distance traveled by the incident shock ( D2 = 3R) and refracted
shock (D1 = 2R) to reach the downstream pole, where R is the droplet radius.
the downstream pole is the transitional SoS ratio from weakly convergent to strongly convergent.
Thus, we hypothesize that the predicted transition SoS ratio from weakly convergent to strongly
convergent occurs at n = 1.5. To test this hypothesis, we changed the ambient pressure to 9.8 MPa
to mimic a condition at which the SoS ratio (n = 1.48) is close to the predicted value ofn = 1.5. The
shock pattern depicted in Figs.18(a) and 18(b) shows that the incident shock and the refracted shock
simultaneously reach the downstream pole. The incident shock far from the droplet approachesz
∗ =
0 when it reaches the downstream pole that corresponds to theD2 = 3R assumption made in Fig.17.
The discrepancy between the predicted transitional SoS ratio (i.e.,n = 1.5) and the calculated value
of n = 1.48 stems from the simpliﬁed assumptions made in this analysis. However, this simpliﬁed
analysis proves our earlier assertion that transition from a weakly to a strongly convergent case, i.e.,
outward to inward axial jet, is related to the location at which the incident shock wave outside of
the droplet and the refracted shockwave inside the droplet meet in relation to the downstream pole.
Note that Fig. 4 includes a red dotted line on the phase diagram where n = 1.48.
FIG. 18. Depiction of the convergence of the incident shock and the refracted shock on the downstream
pole. This pPRE = 9.2 MPa case (n = 1.48) is the transitional case from weakly convergent (1 < n < 1.48) to
strongly convergent (n > 1.48).
113601-23

<!-- PDF_PAGE: 24 -->

BRADLEY BOYD AND DORRIN JARRAHBASHI
FIG. 19. The vorticity (top half) and density (bottom half) distributions for the three pPRE cases (a) 2 MPa,
(b) 6 MPa, and (c) 10 MPa att∗ = 0.3. Note that the numerical reconstruction is lowered to WENO3 to enable
a direct comparison.
2. V orticity generation and ﬂow circulation
The vorticity and density distributions for three cases of varying preshock pressures ( pPRE ) −
2, 6, and 10 MPa—are depicted in Fig. 19 where TPRE = 650 K. One critical difference between
these cases is that then-dodecane and nitrogen density changes signiﬁcantly approaching the critical
pressure of n-dodecane (Table II). The temporal development of the total ﬂow circulation depicted
in Fig. 20 shows that the total ﬂow circulation decreases with an increase in pressure. Again, this is
likely due to the change in the baroclinic vorticity generation term 1
ρ2 ∇ρ×∇ p [see Eq. (7)] which
FIG. 20. Temporal evolution of the ﬂow circulation for pPRE = 2, 6, and 10 MPa. The plus symbol ( +)
indicates the start of the shock wave crossover and the closed circle symbol ( •) corresponds to the point in
time when the transmitted shock ﬁrst appears (see Fig. 14).
113601-24

<!-- PDF_PAGE: 25 -->

NUMERICAL STUDY OF THE TRANSCRITICAL …
is highly dependent on the density. At higher pressures, the densities of both the n-dodecane and
nitrogen increase, thus reducing the magnitude of the 1/ρ2 term.
Before the shockwave crossover occurs (indicated by the dots in Fig. 20), the ﬂow circulation
increases at a similar rate. Because the SoS ratio is much greater for the 2-MPa case ( n = 3.5), the
transmitted shock appears much later than in the 6-MPa case (Fig. 20). For the 10-MPa case, the
transmitted shock appears before the crossover point (Fig. 20) due to the weak convergent behavior
discussed previously in Sec. III B 1.
3. Droplet breakup and instability
Figure 19 shows the droplet shape and the unstable structures at t∗ = 0.3 for different pressure
conditions. It is noted that since the preshock temperature ( TPRE ) is the same for all these cases the
state of the ﬂuid is considered liquidlike, and thus increasing the pressure does not drastically affect
the droplet instability and the consequent droplet breakup. We showed in Sec. III A 3 that a more
drastic change in the droplet behavior was observed by crossing the pseudoboiling temperature
or the Widom line as the ﬂuid transformed from a liquidlike to a gaslike state. Therefore, the
preshock temperature imposes a more pronounced effect on the shock structure, and consequently
the droplet deformation. Although the overall unstable structures are not signiﬁcantly different for
various pressures shown in Fig. 19, the physical time to reach this nondimensional breakup time
is signiﬁcantly longer, 447 μs, for the 2-MPa case, compared to 301 and 247 μs for the 6- and
10-MPa cases, respectively. The growth of interfacial instabilities is faster for fuel droplets at higher
pressures because the ratio of the postshock ambient density to the droplet density (i.e.,√
ρPOST/ρD)
increases with an increase in the preshock pressure, that is, √ ρPOST/ρD equals 0.21, 0.31, and 0.37
for 2, 6, and 10 MPa, respectively.
The 2-MPa case is strongly convergent (n = 3.5) and results in ampliﬁed interfacial instabilities
[Fig. 19(a)] compared to the higher-pressure cases, 6 and 10 MPa, where n = 1.8 and 1.43, respec-
tively [Figs. 19(b) and 19(c)]. This behavior is consistent with the strongly convergent behavior
depicted in Fig. 13 and discussed in Sec. III A 3for the cases that vary in temperature. The increase
in interfacial instability is, again, due to the shock transmitted from the convergence focal point
interacting more signiﬁcantly with the downstream interface.
C. Inﬂuence of shock strength
We investigate the inﬂuence of varying the shock strength at a transcritical condition where
TPRE = 650 K and pPRE = 6 MPa. Similar to Sec. A, we chose the TPRE = 650 K case because the
temperature is the closest to the critical temperature of n-dodecane (Fig. 4), and it results in a
converging case ( n = 1.8) that has more complex transmitted shock behavior than the diverging
cases (n < 1.0, i.e., TPRE = 500 K). The three shock strengths considered here are Mach 1.2, 1.6,
and 2.0, where n = 1.8 for all cases (Fig. 4). The initial conditions, which are determined using
the normal shock calculations and the PR-EoS, are provided in Table III. Note that n, δZ, and A
are independent of the shock strength— n = 1.8, R = 107 400 kg m−2 s−1, and A = 0.865 for the
conditions TPRE = 650 K and pPRE = 6 MPa (TableIII).
Figure 21 compares the temporal evolution of the interface alongside the pressure contours
for the three shock strengths (Mach 1.2, 1.6, and 2.0). This ﬁgure shows that by increasing the
shock strength the transmitted shock wave and crossover shock wave shapes change signiﬁcantly,
inﬂuencing the shape of the droplet at later times [Figs. 21(c), 21(f), and 21(i)]. The transmitted
shock wave and the crossover shock are annotated in Figs. 21(a) and 21(b). The position of the
crossover point is marked by the vertical blue dotted line and the maximum radial distance traveled
by the transmitted shock is depicted by the green dotted line. As the shock strength is increased, the
transmitted shock travels less radially relative to the distance traveled axially (Fig.21). For example,
in Figs. 21(c), 21(f), and 21(i), the transmitted shock wave has traveled to z∗=− 1.1 for all cases,
113601-25

<!-- PDF_PAGE: 26 -->

BRADLEY BOYD AND DORRIN JARRAHBASHI
FIG. 21. The computational Schlieren images (top half) and pressure contours (bottom half) comparing
downstream shock evolution for the various shock strengths (top row, Mach 1.2; middle row, Mach 1.6; and
bottom row, Mach 2.0). The blue dotted line marks the shock crossover location and the maximum radial
distance traveled by the transmitted shock is depicted by the green dotted line.
but radially the shock wave has reached a maximum distance of r∗ = 1.02, 0.74, and 0.56 for the
Mach 1.2, 1.6, and 2 cases, respectively.
Another consideration is the average speed of the crossover shock in the radial direction relative
to the axial speed. The crossover point moves downstream fromz∗ = 0t o −1.1 at Mach 1.21, 1.71,
and 2.12 for the incident shock wave speeds of Mach 1.2, 1.6, and 2.0, respectively. So, the axial
speed of the crossover point is close in magnitude to the incident shock speed. The radial expansion
speed of the crossover shock for these cases decreases from Mach 0.9 to Mach 0.73 with an increase
in incident shock speed from 1.2 to 2.0. This reduction in radial speed and increase in axial speed
results in the narrowing of the crossover and transmitted shock formations observed by comparing
the distance between the dotted green lines in Figs. 21(c), 21(f), and 21(i). Later in this section, we
will show the effect of shock structures and speed on the geometry of the deformed droplet.
The downstream pressure distributions shown in the bottom half of Fig. 21 illustrate that the
structure of the crossover shock wave and the transmitted shock wave changes with an increase in
the shock strength. In the Mach 1.2 case, the high-pressure region associated with the evolution
of the transmitted shock expands with almost the same rate in the radial and axial directions, as
is implied by the distance between the dotted green lines in Figs. 21(a)–21(c). As a result, the
droplet aspect ratio (radial to axial width) does change signiﬁcantly in this case during the early
development phase. Comparing Figs. 21(a) and 21(d) shows that by increasing the incident shock
113601-26

<!-- PDF_PAGE: 27 -->

NUMERICAL STUDY OF THE TRANSCRITICAL …
FIG. 22. The vorticity (top half) and density (bottom half) distributions for the three shock speed cases (a)
Mach 1.2, (b) Mach 1.6, and (c) Mach 2.0 att∗ = 0.6. Note that TPRE = 650 K, pPRE = 6M P a ,a n dn = 1.8f o r
all cases. Note that the numerical reconstruction is lowered to WENO3 with the minmod ﬂux limiter to enable
a direct comparison.
strength to Mach 1.6 the pressure increase downstream of the transmitted shock is higher (about
double in magnitude) and this high-pressure region is narrower in the radial direction compared
with the Mach 1.2 case. The subsequent pressure distribution results in the axial squeezing of the
droplet, forcing it to elongate radially to the low-pressure regions as shown in Fig.21(e), increasing
the droplet aspect ratio. This results in a pancake shape droplet at later times for the Mach 1.6
case [Fig. 21(f)], consistent with the experimental observation and computational results of SDI at
subcritical conditions [25,32,36].
With a further increase in shock strength to Mach 2.0, the transmitted shock imposes a higher
pressure distributed within a radially narrower region compared to lower incident shock speeds.
This is evident by comparing the distance between the dotted green lines in Figs. 21(g)–21(i) with
Figs. 21(d)–21(f). Like the Mach 1.6 case, the high downstream pressure behind the transmitted
shock for the Mach 2.0 case results in the squeezing of the droplet; however, because this high-
pressure region is radially less extended the droplet is not forced to elongate as far radially. Figure22
compares the droplet shapes at the same nondimensional time of t
∗ = 0.6 to better represent the
changes in the droplet aspect ratio for different tested incident shock strengths. This behavior is
consistent with the results of increasing the shock strength when considering the shock interaction
with a water column: the ﬂattening or radial elongating of the water droplet is also found to reduce
with shock strength due to the changes in the pressure distribution [68].
As previously stated, the three shock speed cases (Mach 1.2, 1.6, and 2.0) are all strongly
convergent as n = 1.8 for all cases and exhibit slight outward jetting along the axis as indicated
in Fig. 22. However, the downstream interface distortion varies signiﬁcantly with increasing shock
strength. It is observed in Fig.22 that by increasing the shock speed the interface at the downstream
pole is pushed inward (into the droplet) and this effect becomes more noticeable at later times. To
better understand this phenomenon, Fig. 23 illustrates the pressure contours and the axial pressure
distribution near the downstream interface after the transmitted shock appears for the three shock
strength cases. Figure23 shows that a high-pressure region is formed within the transmitted shock as
it leaves the downstream interface, and a low-pressure region is generated within the droplet due to
the reﬂected rarefaction wave. The subsequent pressure gradient at the downstream interface drives
the interface inwards. Comparing the axial pressure distributions in Figs. 23(b), 23(d), and 23(f)
reveals that the pressure gradient at the downstream pole of the droplet increases signiﬁcantly with
the shock strength, resulting in more noticeable interface indentation for the Mach 1.6 and the Mach
2 cases (Fig. 22). This inward deformation of the TSDI is not observed in the water SDI case—this
113601-27

<!-- PDF_PAGE: 28 -->

BRADLEY BOYD AND DORRIN JARRAHBASHI
FIG. 23. Comparison of the pressure distributions after the transmitted shock appears downstream for the
three shock strength cases: (a), (b) Mach 1.2, (c), (d) Mach 1.6, and (e), (f) Mach 2.0. The top half of (a),
(c), and (e) shows the computational Schlieren images, and the bottom half shows the pressure contours. The
corresponding axial pressure distributions for the three cases are depicted in (b), (d), and (f), respectively.
is because in the SDI case (1) the refracted shock is weak, (2) the refracted shock is divergent, and
(3) the transmitted shock is insigniﬁcant (Fig. 32). Thus, the TSDI exhibits features that have not
been observed in SDI cases.
V orticity generation and ﬂow circulation
The vorticity and density distributions for Mach 1.2, 1.6, and 2.0 at t∗ = 0.6 are depicted in
Fig. 22. As the density contours illustrate, the passage of the shock wave results in signiﬁcant
113601-28

<!-- PDF_PAGE: 29 -->

NUMERICAL STUDY OF THE TRANSCRITICAL …
FIG. 24. Temporal evolution of the circulation for the three shock wave strengths (Mach 1.2, 1.6, and 2.0)
at a preshock temperature of 650 K and preshock pressure of 6 MPa. The plus symbol ( +) indicates the start
of the shockwave crossover and the closed circle symbol (•) corresponds to the point in time when transmitted
shock ﬁrst appears (Fig. 14).
compression of the droplet that increases with the shock strength (Fig. 22). The vorticity contours
illustrate that the deposition of the positive baroclinic vorticity at the interface creates a recirculation
region behind the droplet that ampliﬁes with an increase in shock strength. In the recirculation
region behind the droplet, there is also negative vorticity generation which is consistent with the
ﬁndings from the shock interaction with a water column presented in Ref. [ 68]. A large increase
in the pressure jump across the normal shock is achieved with an increase in shock wave strength
(Table III)—/Delta1p = 3.1, 11.0, and 21.1 MPa for Mach 1.2, 1.6, and 2, respectively. This increase
in pressure jump results in the increased generation of baroclinic vorticity during the TSDI that is
more evident by increasing the shock speed from Mach 1.2 to 1.6 [Figs.22(a) and 22(b)]. This is also
reﬂected in the evolution of the ﬂow circulation for the three shock strength cases depicted in Fig.24.
This is consistent with the ﬁndings in Ref. [113] where researchers conducted an experimental study
on the RMI mixing of an SF6 gas layer, where the vorticity and ﬂow circulation increased with shock
wave strength. The baroclinic vorticity deposition and ﬂow circulation are expected to increase with
Mach number for all shock-interface interaction cases—SBI, SDI, and TSDI.
To better disclose the early development of the circulation that is critical for understanding
the TSDI at later stages, we presented the temporal variation of circulation. Figure 24 shows that
the ﬂow circulation increases more rapidly with increasing shock speed during the primary shock
interaction (before the shock transmission and crossover) due to the increased pressure jump across
the shock front and the fact that the shock travels faster past the droplet. As a result, the increase in
shock strength directly leads to an increase in ﬂow circulation (Fig. 24). Even after the shockwave
interaction phase is complete, the ﬂow circulation continues to increase at a higher rate for higher
shock strengths. The increase in the postshock ﬂow speed with increasing Mach number (TableIII)
increases the ﬂow circulation and is expected to further amplify the interfacial instabilities.
In summary, increasing the shock strength at transcritical conditions does not signiﬁcantly
change the TSDI features as the SoS ratio (n) is independent of the shock strength. We showed that
the increase in shock speed mainly affects the droplet morphology and its aspect ratio. Speciﬁcally,
113601-29

<!-- PDF_PAGE: 30 -->

BRADLEY BOYD AND DORRIN JARRAHBASHI
the reduction in the fuel-droplet ﬂattening with an increase in shock strength is consistent with the
ﬁndings from the SDI case presented in Ref. [ 68]. The unique feature of the TSDI at higher shock
strengths is the inward deformation of the fuel droplet at the downstream interface, which is not
observed in the water SDI case.
IV . CONCLUSIONS
In this paper, we simulated the shock wave interaction with a fuel droplet at supercritical pressure
(TSDI) and compared the shock and ﬂow features with the classical SBI and classical SDI. The
TSDI resulted in various interesting ﬂow features including axial jetting and the formation of
interfacial instabilities. Many of the ﬂow features observed were consistent with the extensively
studied SBI. However, we observed a transition from diverging to converging behavior due to the
liquidlike to the gaslike transition of the fuel at transcritical conditions. This resulted in a unique
case when the refracted shock diverges but the density of the fuel is higher than the surrounding
ﬂuid—this is more like a classic SDI case (i.e., shock interaction with a water droplet). SBI cases
usually have a lower SoS for a dense gas (slower molecules), i.e., R22, whereas dense liquids
typically have a higher SoS.
What makes the TSDI different from classic SDI is that the acoustic impedance mismatch is
low enough for a signiﬁcant refracted shock to be transmitted through the droplet—in the classic
SDI case, the acoustic impedance is so high that only a very weak refracted shock is apparent.
Subsequently, the TSDI behavior results in a transmitted shockwave and an internally reﬂected
rarefaction wave that signiﬁcantly changes the ﬂow features, i.e., high-pressure, and low-pressure
focal points within the droplet.
The TSDI differs from the classic SBI cases because the acoustic impedance mismatch is always
positive while exhibiting both convergent and divergent behavior. SBI cases typically have negative
acoustic impedance mismatch for diverging cases (i.e., helium) or positive acoustic impedance
mismatch for converging cases (i.e., R22) due to the behavior of ideal gases. As a result, the
diverging SBI results in (1) a reﬂected rarefaction wave, (2) a TRR formation, and (3) an internally
reﬂected shock wave, whereas the diverging TSDI case involves (1) a reﬂected shock wave,( 2 )no
TRR formation, and (3) an internally reﬂected rarefaction wave. Thus, the TSDI diverging case
differs dramatically from a diverging SBI case.
The result showed the importance of the SoS ratio (n) on the interaction behavior with a transition
from diverging to converging behavior at n = 1. Additionally, we observed a new transition point
from a weakly convergent case to a strongly convergent case at n ∼ 1.48. The strongly convergent
behavior (n > 1.48) is where the refracted shock converges to a focal point within the bubble, often
resulting in axial jetting. The weakly convergent behavior ( n < 1.48) is where the refracted shock
is too fast to converge to a point within the droplet, resulting in either insigniﬁcant axial jetting or
inward jetting behavior.
Another consideration was the inﬂuence of shock strength on the TSDI behavior. As the shock
strength was increased, the amount of droplet ﬂattening reduced, which is consistent with the classic
SDI behavior. A unique feature that appeared with increasing the shock strength is the inward
deformation of the downstream interface. This inward deformation is found to be a result of the high
pressure within the transmitted shock that has not been observed in classical SDI. Consequently, the
TSDI cases have features in common with both SBI and SDI cases, providing an important link
between these two widely studied problems.
The results presented in this paper provide important information about the early development of
droplet breakup behavior and mixing efﬁciency for transcritical problems arising in high-pressure
fuel injection. The model presented here will be used to simulate more speciﬁc transcritical
problems, i.e., scramjets, ramjets, and liquid rocket engines. In future work, we plan on extending
this model to three dimensions to further investigate the interfacial instability development and
droplet breakup behavior at later times.
113601-30

<!-- PDF_PAGE: 31 -->

NUMERICAL STUDY OF THE TRANSCRITICAL …
TABLE I. The changes to initial conditions for the four cases that changeTPRE : 500, 545.7, 650, and 800 K.
The normal shock is Mach 1.2 and PPRE = 6M P a .
TPRE (K) 500 545.7 650 800
ρDROP (kg/m3 ) 567 .2 531.5 419 .9 223 .5
ρPRE (kg/m3 )3 9 .65 36.3 30 .46 24 .79
ρPOST [kg/m3]5 2 .86 48.44 40 .38 33 .30
uz,POST [m/s] −140.3 −146.7 −160.3 −178.0
pPOST [MPa] 9 .1211 9.113 9 .096 9 .072
TPOST [K] 570 .2 621.0 736 .2 900 .4
n 0.78 1.0 1.8 3.1
δZ [kg m−2 s−1] 320116 241314 107400 27913
A 0.869 0.872 0.865 0.80
ACKNOWLEDGMENT
Portions of this research were conducted with the advanced computing resources provided by
Texas A&M High-Performance Research Computing.
APPENDIX A: CASE PARAMETERS
Here, we present all the parameters for the TSDI simulations. The normal shock wave relations
[114] are used to approximate the postshock Mach number, pressure, and temperature:
MPOST =
√
(γ∗ − 1)M2 + 2
2γM2 − (γ∗ − 1), (A1)
pPOST = pPRE
(2γ∗M2 − (γ∗ − 1)
γ∗ + 1
)
, (A2)
TPOST = TPRE
[2γ∗M2 − (γ∗ − 1)][(γ∗ − 1)M2 + 2]
(γ∗ + 1)2M2 , (A3)
TABLE II. The changes to initial conditions for the four cases that change PPRE : 2, 6, 9.2, and 10 MPa.
The normal shock is Mach 1.2 and TPRE = 650 K.
TPRE [K] 2 MPa 6 MPa 9.2 MPa 10 MPa
ρD [kg/m3] 310.7 419.9 455.1 461.9
ρPRE [kg/m3] 10.3 30.46 46.18 50.05
ρPOST [kg/m3] 13.83 40.38 61.62 66.74
uz,POST [m/s] –159.4 –160.3 –161.0 –161.2
pPOST [MPa] 3.034 9.096 14.0 15.2
TPOST [K] 731.4 736 .2 740.0 741.0
n 3.5 1.8 1.48 1.43
δZ [kg m−2 s−1] 40450.4 107400 139572 146617
A 0.936 0.865 0.816 0.804√ ρPOST/ρD 0.21 0.31 0.37 0.38
113601-31

<!-- PDF_PAGE: 32 -->

BRADLEY BOYD AND DORRIN JARRAHBASHI
TABLE III. The changes to initial conditions (postshock properties) for the three cases that change in shock
wave strength: Mach 1.2, Mach 1.6, and Mach 2.0. For these cases TPRE = 650 K and PPRE = 6M P a (n =
1.8,∂Z = 107 400, kg m−2 s−1, A = 0.866).
Shock strength Mach 1.2 Mach 1.6 Mach 2.0
pPOST [MPa] 9.096 16.975 27.106
uz,POST [m/s] –160.3 –426.2 –655.8
TPOST [K] 736.2 911.7 1114.1
ρPOST [kg/m3] 40.38 61.44 80.28
where the speciﬁc heat ratio (γ∗) is approximated using the PR-EoS [71,73]. We can then determine
the postshock density of the nitrogen using the PR-EoS and the postshock velocity given by
uPOST = uS
(
1 − MPOST
M
√
TPOST
TPRE
)
, (A4)
where uS is the shock velocity.
APPENDIX B: SHOCK-BUBBLE INTERACTION
To validate the numerical model and understand the SBI at ideal-gas conditions (see Fig. 1), we
consider two SBI problems that are commonly used in the literature. These problems involve the
interaction of a Mach 1.2 shock with a bubble in an air environment: in this paper, we approximate
the air using the properties of nitrogen. The two cases vary in the contents of the bubble: (1) helium
(He) and (2) refrigerant R22 (CHClF
2). The key parameters for the validation cases that involve
a leftward traveling Mach 1.2 shock wave that impacts a bubble (helium or R22) are outlined in
Table IV.
1. Computational model
For the two shock-bubble validation cases, He-N2 (Appendix B2 ) and R22-N2 (Appendix B3 ),
the 2D axisymmetric cylindrical computational domain is extended from −25 to 25 cm in the axial
direction and 0 to 4.5 cm in the vertical direction as depicted in Fig. 25. Only the top half of the
depicted computational domain is required for the simulation due to the axis of symmetry boundary
condition at r = 0. The initial condition consists of a bubble (He or R22) atz = 5 cm and a leftward
traveling normal shock (Mach 1.2) at z = 10 cm. The left and right boundaries use a transmissive
boundary condition and the outer radial boundary at r = 4.5 is a reﬂective boundary, representing
the rigid shock tube (Fig. 25). A uniform mesh is used between −16 and 16 cm where the cell
dimensions are /Delta1z ≈ /Delta1r ≈ 0.23 mm. The mesh then grows in the z direction at approximately
10% to reach the ends of the domain.
TABLE IV . Key parameters for the validation cases involving a leftward traveling Mach 1.2 shock wave
that impacts a bubble (helium or R22) with a diameter of 5 cm in a shock tube with a diameter of 9 cm.
Validation cases Helium/nitrogen R22/nitrogen
SoS ratio (n) 0.4 (divergent) 1.95 (convergent)
Acoustic impedance mismatch 245.9
(δZ)( k gm−2s−1) –215.7 (reﬂected rarefaction) (reﬂected shock)
Atwood number (A) –0.684 0.516
113601-32

<!-- PDF_PAGE: 33 -->

NUMERICAL STUDY OF THE TRANSCRITICAL …
FIG. 25. Schematic of the shock-bubble interaction validation cases used for the helium bubble case and
the R22 bubble case. The depicted cell size is ten times larger than the cell size used in the simulations
(/Delta1z ≈ /Delta1r ≈ 0.23 mm). Due to the axis of the symmetry boundary condition, only the top half of the depicted
computational domain is required for the simulation.
2. Helium shock-bubble interaction: A divergent case
The ﬁrst case is the helium bubble which is used as a validation case in numerous numerical
studies [39,89,97–106]. Here, we use the helium case to qualitatively and quantitively validate our
model. Figure 26 shows the numerical results which can be directly compared to the experimental
results in Fig. 27 adopted from Ref. [38]. Note that throughout this paper t = 0 μs is considered as
the instant the incident shockwave ﬁrst reaches the bubble interface—in this case,t = 0 μsi sw h e n
the incident shock reaches z = 7.5 cm and t =− 60 μs corresponds to the start of the simulations.
The red contour line shows the material interface where the volume fraction of the helium is 0.95.
After the leftward traveling Mach 1.2 shock (see Fig. 25) impacts the bubble, the refracted shock
wave travels faster in the helium bubble due to the increased SoS ( n < 1), resulting in a diverging
refracted shock within the bubble, referred to as a divergent case as shown in Figs. 26(a), 26(b),
27(a), and 27(b). Due to the negative impedance mismatch, the reﬂected shock wave is a rarefaction
wave as annotated in Fig. 26(a) and observed in Figs. 27(a)–27(e). The interaction of the incident
shock wave with the bubble interface, in this case, results in a four-shock formation termed the
TRR [39]—this is annotated in Fig. 26(c) and observed in Figs. 27(b) and 27(c). The TRR involves
the formation of a side shock that connects the refracted shock to the incident and reﬂected shock
wave with the development of an expansion wave (see Fig. 11 of Ref. [ 39] for a schematic of
the phenomenon). The refracted shock later reaches the downstream bubble interface [Figs. 26(d)
and 27(d)], resulting in the internally reﬂected shock and the transmitted shock [Fig. 26(e)]. Note
that the deﬁnition of the transmitted shock in the literature is varied. In this paper, we refer to the
shock formation that leaves the downstream interface as the transmitted shock [Fig. 26(e)] and the
shock refracted within the bubble as the refracted shock [Fig. 26(a)]. The passage of the shock
also induces baroclinic vorticity at the interface due to the density gradient of the interface and the
pressure gradient of the shock wave [39] [see Eq. (7)]. In time, the vorticity from the shock passage
induces a large jet that forms near the bubble axis of symmetry and deforms the bubble to a kidney
shape [Figs. 26(g)–26(i) and 27(g)–27(i)].
To quantitatively validate the model, the speed of the incident shock ( uI ), the speed of the
refracted shock ( uR ), and the speed of the transmitted shock ( uT ) are calculated at the axis of
symmetry and compared to the experimental results of Ref. [ 38] and the numerical results in
Ref. [ 94]. Table V contains the quantitative validation results. The ﬂow features of interest are
annotated in Fig. 26. The shock speed measurements from the simulation for the incident shock
speed (uI ) and transmitted shock speed ( uT ) are all within the experimental range determined in
Ref. [38], demonstrating acceptable quantitative agreement with less than 5% error. The refracted
shock speed was found to be slightly higher ( uR ), with an error of 9 and 13% compared to the
benchmark results and the experimental results, respectively.
113601-33

<!-- PDF_PAGE: 34 -->

BRADLEY BOYD AND DORRIN JARRAHBASHI
FIG. 26. Computational Schlieren images of the interaction of a Mach 1.2 shock with a helium bubble in
a nitrogen environment at times (a) 23, (b) 34, (c) 45, (d) 49, (e) 68, (f) 101, (g) 244, (h) 425, and (i) 672 μs.
The red contour line shows the material interface where αD = 0.95.
3. Shock-bubble interaction: A convergent case
The second validation case we consider in this section is the shock interaction of a Mach 1.2
shockwave with an R22 bubble in a nitrogen environment. This case is of interest because it exhibits
a convergent refracted shock (n > 1) and the bubble is of a higher density than the surrounding ﬂuid;
thus, δZ > 0 and A > 0 (TableIV). In this case, the reﬂected wave in Figs.28(a) and 29(a) is a shock
wave becauseδZ > 0. The refracted shockwave that is shown in Figs.28(a) and 29(a) is convergent
due to the lower SoS of the bubble ﬂuid ( n > 1). The computational Schlieren images depict a
key feature of the convergent case in Figs. 28(g), 28(h), 29(g), and 29(h) that is the formation of
an axial jet as illustrated in Fig. 28(d) and experimentally captured in Fig. 29(d) [39,52–54]. The
axial jet is created as the refracted shock converges to a focal point within the bubble near the
113601-34

<!-- PDF_PAGE: 35 -->

NUMERICAL STUDY OF THE TRANSCRITICAL …
FIG. 27. Experimental Schlieren images of the interaction of a Mach 1.2 shock with a helium bubble in
an air environment at times (a) 32, (b) 52, (c) 62, (d) 72, (e) 82, (f) 102, (g) 245, (h) 427, and (i) 674 μs.
Experimental images reprinted with permission of the Cambridge University Press from Fig. 7 of Ref. [38].
downstream interface and creates a higher-pressure region. The red contour line shows the material
interface at αD = 0.95, where αD is the volume fraction of the bubble. Additionally, the refracted
shock convergence to the focal point results in the formation of a transmitted shock annotated in
Figs. 28(e) and 28(f) and observed in Figs. 29(e) and 29(f). The crossover shock, annotated in
Fig. 28(d) and observed in Figs. 29(d) and 29(f), is due to the bubble changing the direction of
the incident shock around the bubble resulting in the shock crossover. In general, a very good
qualitative agreement is observed between the shock features and interface deformation between
the simulations and experiments as well as acceptable quantitative results as outlined in TableV.
TABLE V . The quantitative validation of the shock speeds. The shock speed was determined by averaging
the shock velocity along the axis of symmetry over the speciﬁed time interval. The table also includes the error
(%) of our recorded shock speeds compared to the benchmark results and the experiment.
Shock speeds (m/s) uI uR uT
Time interval for averaging the shock speeds (μs) –60 to 0 0 to 53 53 to 240
Simulation results from the present paper 426 1020 380
Benchmark [94] 420 (1.4%) 933 (9%) 362 (5%)
Experiment [38] 410 ± 41 (3.9%) 900 ± 90 (13%) 393 ± 39 (3.3%)
113601-35

<!-- PDF_PAGE: 36 -->

BRADLEY BOYD AND DORRIN JARRAHBASHI
FIG. 28. Computational Schlieren images of the interaction of a Mach 1.2 shock with an R22 bubble in a
nitrogen environment at times (a) 55, (b) 114, (c) 134, (d) 188, (e) 247, (f) 320, (g) 345, (h) 418, and (i) 913μs.
The red contour line shows the material interface where αD = 0.95.
Figure 30 shows the density and vorticity distributions for the helium and R22 cases during the
shock interaction. The passage of the shock induces baroclinic vorticity at the interface due to the
density gradient of the interface and the pressure gradient [Eq. (7)] [39] in both cases; however, the
rotation in the helium case is in the opposite direction compared to the R22 case due to the change
in density gradient direction at the material interface [ 48]. As a result, vorticity is predominantly
negative in the helium case [Fig. 30(a)] and positive in the R22 case [Fig. 30(b)]. The generation
of vorticity can be further interpreted by the total ﬂow circulation shown in Fig. 31(a).I nt h eR 2 2
case where the refracted shock converges, the ﬂow circulation increases to a maximum that occurs
between the shock crossover indicated with a plus symbol (+)i nF i g .31(b) and shock transmission
shown in Fig. 31(c). The closed circle symbol (•) corresponds to the point in time when transmitted
shock ﬁrst appears.
113601-36

<!-- PDF_PAGE: 37 -->

NUMERICAL STUDY OF THE TRANSCRITICAL …
FIG. 29. Experimental Schlieren images of the interaction of a Mach 1.2 shock with an R22 bubble in an
air environment at times (a) 55, (b) 115, (c) 135, (d) 187. (e) 247, (f) 318, (g) 342, (h) 417, and (i) 1020 μs.
Experimental images reprinted with permission of the Cambridge University Press from Fig. 11 of Ref. [38].
In the helium case where the refracted shock diverges, the circulation sign is opposite to the
R22 case consistent with the sign of the baroclinic vorticity stated above. The circulation reduces
rapidly, reaching a local minimum when the shock transmission occurs as indicated with a closed
circle symbol corresponding to Fig. 31(d).
FIG. 30. The baroclinic vorticity (top half) and density distributions (bottom half) for (a) the helium bubble
case and (b) the R22 bubble case. Panel (a) corresponds to Fig. 26(d) and panel (b) corresponds to Fig. 28(b).
113601-37

<!-- PDF_PAGE: 38 -->

BRADLEY BOYD AND DORRIN JARRAHBASHI
FIG. 31. (a) The temporal evolution of the total ﬂow circulation for the helium and R22 cases. The plus
symbol (+) indicates the start of the shockwave crossover and the closed circle symbol (•) corresponds to the
point in time when transmitted shock ﬁrst appears. The depiction includes the computational Schlieren images
of the appearance of the crossover and transmitted shock for (b), (c) the R22 case and (d), (e) the helium
case.
APPENDIX C: SHOCK-DROPLET INTERACTION
For comparison purposes, we consider here a shock interaction with a subcritical water droplet—
this SDI case is considered in many studies [ 25,26,29,32,37,67,112,115,116]. To better model the
liquid water droplet, we used the commonly used stiffened EoS and the fully conservative 5-Eq
model [32,90,94,95,117]. The simulation was conducted using WENO3 reconstruction, RK3-TVD
time stepping, and the HLLC approximate Riemann ﬂux.
Figure 32 shows the Mach 1.2 shock interaction with the water droplet. Due to the large acoustic
impedance mismatch (δZ ∼ 1.5 × 10
6[kgm−2s−1]), a strong shock is reﬂected, and a weak shock
is refracted within the droplet. Additionally, because of the stiffness of the water, the refracted
shock results in a small density gradient requiring a large Schlieren shading function parameter
(k = 5 × 10
5 for the water andk = 1 × 104 for the air) to visualize the refracted shock transmission
113601-38

<!-- PDF_PAGE: 39 -->

NUMERICAL STUDY OF THE TRANSCRITICAL …
FIG. 32. Computational Schlieren images of the interaction of a Mach 1.2 shock with a water droplet in air
at (a) 9 μs, (b) 22 μs, (c) 30 μs, (d) 43 μs, (e) 52 μs, and (f) 174 μs. The red contour line shows the material
interface where αD = 0.95.
[Figs. 32(a)–32(c)]. As the refracted shock reaches the downstream interface, a weak rarefaction
wave is internally reﬂected, and no signiﬁcant shock is transmitted downstream [Figs. 32(d) and
32(e)].
[1] M. Hersch, E. J. Rice, and Lewis Research Center, Gaseous-Hydrogen-Liquid-Oxygen Rocket Combus-
tion at Supercritical Chamber Pressures, NASA Technical Note (NASA, Washington, DC, 1967).
[2] J. C. Oefelein, Thermophysical characteristics of shear-coaxial LOX–H2 ﬂames at supercritical pressure,
Proc. Combust. Inst. 30, 2929 (2005).
[3] D. T. Harrje and F. H. Reardon,Liquid Propellant Rocket Combustion Instability(Scientiﬁc and Technical
Information Ofﬁce, NASA, Washington, DC, 1972), V ol. 1.
[4] N. Okong’, K. Harstad, and J. Bellan, Direct numerical simulations of O/H temporal mixing layers under
supercritical conditions, AIAA J. 40, 914 (2002).
[5] R. S. Miller, K. G. Harstad, and J. Bellan, Direct numerical simulations of supercritical ﬂuid mixing
layers applied to heptane-nitrogen, J. Fluid Mech. 436, 1 (2001).
[6] R. Miller, K. Harstad, and J. Bellan, Evaluation of equilibrium and non-equilibrium evaporation models
for many-droplet gas-liquid ﬂow simulations, Int. J. Multiphase Flow 24, 1025 (1998).
[7] J. Bellan, Supercritical (and subcritical) ﬂuid behavior and modeling: Drops, streams, shear and mixing
layers, jets and sprays, Prog. Energy Combust. Sci. 26, 329 (2000).
113601-39

<!-- PDF_PAGE: 40 -->

BRADLEY BOYD AND DORRIN JARRAHBASHI
[8] W. O. H. Mayer, A. H. A. Schik, B. Vielle, C. Chauveau, I. Gokalp, D. G. Talley, and R. D. Woodward,
Atomization and Breakup of Cryogenic Propellants Under High-Pressure Subcritical and Supercritical
Conditions, J. Propul. Power 14, 835 (1998).
[9] N. Zong and V . Yang, Cryogenic ﬂuid jets and mixing layers in transcritical and supercritical environ-
ments, Combust. Sci. Technol. 178, 193 (2006).
[10] B. Chehroudi, D. Talley, and E. Coy, Visual characteristics and initial growth rates of round cryogenic
jets at subcritical and supercritical pressures, Phys. Fluids 14, 850 (2002).
[11] D. W. Davis, On the behavior of a shear-coaxial jet, spanning sub-to supercritical pressures, with and
without an externally imposed transverse acoustic ﬁeld, Ph.D. thesis, The Pennsylvania State University,
2006.
[12] B. Chehroudi, Recent experimental efforts on high-pressure supercritical injection for liquid rockets and
their implications, Int. J. Aerosp. Eng. 2012, 121802 (2012).
[13] I. Leyva, B. Chehroudi, and D. Talley, Dark core analysis of coaxial injectors at sub-, near-, and
supercritical conditions in a transverse acoustic ﬁeld, inProceedings of the 43rd AIAA/ASME/SAE/ASEE
Joint Propulsion Conference and Exhibit, 2007 (unpublished), p. 5456.
[14] B. Chehroudi, Physical hypothesis for the combustion instability in cryogenic liquid rocket engines,
J. Propul. Power 26, 1153 (2010).
[15] R. N. Dahms and J. C. Oefelein, On the transition between two-phase and single-phase interface
dynamics in multicomponent ﬂuids at supercritical pressures, Phys. Fluids 25, 092103 (2013).
[16] R. N. Dahms and J. C. Oefelein, Non-equilibrium gas–liquid interface dynamics in high-pressure liquid
injection systems, Proc. Combust. Inst. 35, 1587 (2015).
[17] R. N. Dahms, J. Manin, L. M. Pickett, and J. C. Oefelein, Understanding high-pressure gas-liquid
interface phenomena in Diesel engines, Proc. Combust. Inst. 34, 1667 (2013).
[18] R. N. Dahms, Understanding the breakdown of classic two-phase theory and spray atomization at engine-
relevant conditions, Phys. Fluids 28, 042108 (2016).
[19] J. Oefelein, G. Lacaze, R. Dahms, A. Ruiz, and A. Misdariis, Effects of real-ﬂuid thermodynamics on
high-pressure fuel injection processes, SAE Int. J. Engines 7, 1125 (2014).
[20] R. N. Dahms and J. C. Oefelein, Liquid jet breakup regimes at supercritical pressures, Combust. Flame
162, 3648 (2015).
[21] C. Lettieri, G. Subashki, and Z. Spakovszky, Modeling near critical and supercritical fuel injection and
mixing in gas turbine applications, inASME Turbo Expo (2018): Turbomachinery Technical Conference
and Exposition (American Society of Mechanical Engineers, New York, 2018), p. V04AT04A009.
[22] Z. Ren, B. Wang, L. Zheng, and D. Zhao, Numerical studies on supersonic spray combustion in high-
temperature shear ﬂows in a scramjet combustor, Chin. J. Aeronaut. 31, 1870 (2018).
[23] Z. Ren, B. Wang, G. Xiang, D. Zhao, and L. Zheng, Supersonic spray combustion subject to scramjets:
Progress and challenges, Prog. Aerosp. Sci. 105, 40 (2019).
[24] T.-M. Jia, Y .-S. Yu, and G.-X. Li, Experimental investigation of effects of super high injection pressure
on diesel spray and induced shock waves characteristics, Exp. Therm. Fluid Sci. 85, 399 (2017).
[25] H. Chen, Two-dimensional simulation of stripping breakup of a water droplet,AIAA J. 46, 1135 (2008).
[26] H. Chen and S. M. Liang, Flow visualization of shock/water column interactions, Shock Waves 17, 309
(2007).
[27] B. Dorschner, L. Biasiori-Poulanges, K. Schmidmayer, H. El-Rabii, and T. Colonius, On the formation
and recurrent shedding of ligaments in droplet aerobreakup, J. Fluid Mech. 904, A20 (2020).
[28] B. Guan, Y . Liu, C.-Y . Wen, and H. Shen, Numerical study on liquid droplet internal ﬂow under shock
impact, AIAA J. 56, 3382 (2018).
[29] D. Igra and K. Takayama, Numerical simulation of shock wave interaction with a water column,
Shock Waves 11, 219 (2001).
[30] D. D. Joseph, J. Belanger, and G. S. Beavers, Breakup of a liquid drop suddenly exposed to a high-speed
airstream, Int. J. Multiphase Flow 25, 1263 (1999).
[31] Y . Liang, Y . Jiang, C.-Y . Wen, and Y . Liu, Interaction of a planar shock wave and a water droplet
embedded with a vapour cavity, J. Fluid Mech. 885, R6 (2020).
113601-40

<!-- PDF_PAGE: 41 -->

NUMERICAL STUDY OF THE TRANSCRITICAL …
[32] J. C. Meng and T. Colonius, Numerical simulation of the aerobreakup of a water droplet, J. Fluid Mech.
835, 1108 (2018).
[33] J. C. Meng, Numerical simulations of droplet aerobreakup, Ph.D. thesis, California Institute of Technol-
ogy, 2016.
[34] B. Moylan, B. Landrum, and G. Russell, Investigation of the physical phenomena associated with rain
impacts on supersonic and hypersonic ﬂight vehicles, Proc. Eng. 58, 223 (2013).
[35] B. E. Moylan, Raindrop demise in a high-speed projectile ﬂowﬁeld, Ph.D. thesis, The University of
Alabama in Huntsville, 2010.
[36] Z. Wang, T. Hopfes, M. Giglmaier, and N. A. Adams, Effect of Mach number on droplet aerobreakup in
shear stripping regime, Exp. Fluids 61, 193 (2020).
[37] T. Yoshida and K. Takayama, Interaction of liquid droplets with planar shock waves,J. Fluids Eng. 112,
481 (1990).
[38] J.-F. Haas and B. Sturtevant, Interaction of weak shock waves with cylindrical and spherical gas
inhomogeneities, J. Fluid Mech. 181, 41 (1987).
[39] J. J. Quirk and S. Karni, On the dynamics of a shock-bubble interaction, J. Fluid Mech. 318, 129
(2006).
[40] S. Kumar, G. Orlicz, C. Tomkins, C. Goodenough, K. Prestridge, P. V orobieff, and R. Benjamin,
Stretching of material lines in shock-accelerated gaseous ﬂows, Phys. Fluids 17, 082107 (2005).
[41] S. Kumar, P. V orobieff, G. Orlicz, A. Palekar, C. Tomkins, C. Goodenough, M. Marr-Lyon, K. Prestridge,
and R. Benjamin, Complex ﬂow morphologies in shock-accelerated gaseous ﬂows, Physica D 235,2 1
(2007).
[42] G. Layes, G. Jourdan, and L. Houas, Distortion of a Spherical Gaseous Interface Accelerated by a Plane
Shock Wave, P h y s .R e v .L e t t .91, 174502 (2003).
[43] G. Layes, G. Jourdan, and L. Houas, Experimental investigation of the shock wave interaction with a
spherical gas inhomogeneity, Phys. Fluids 17, 028103 (2005).
[44] G. Layes, G. Jourdan, and L. Houas, Experimental study on a plane shock wave accelerating a gas
bubble, Phys. Fluids 21, 074102 (2009).
[45] K. Levy, O. Sadot, A. Rikanati, D. Kartoon, Y . Srebro, A. Yosef-Hai, G. Ben-Dor, and D. Shvarts,
Scaling in the shock-bubble interaction, Laser Part. Beams 21, 335 (2003).
[46] J. H. J. Niederhaus, A computational parameter study for three-dimensional shock-bubble interactions,
Ph.D. thesis, University of Wisconsin-Madison, 2007.
[47] A. Nowakowski, A. Ballil, and F. Nicolleau, Passage of a shock wave through inhomogeneous media
and its impact on gas-bubble deformation, Phys. Rev. E 92, 023028 (2015).
[48] D. Ranjan, J. Oakley, and R. Bonazza, Shock-bubble interactions, Annu. Rev. Fluid Mech. 43, 117
(2011).
[49] S. Sha, Z.-H. Chen, and Q.-B. Zhang, Numerical investigations on the interaction of shock waves with
spherical SF6 bubbles, Acta Physica Sinica 64, 015201 (2015).
[50] C. Tomkins, S. Kumar, G. Orlicz, and K. Prestridge, An experimental investigation of mixing mecha-
nisms in shock-accelerated ﬂow, J. Fluid Mech. 611, 131 (2008).
[51] C. Tomkins, K. Prestridge, P. Rightley, M. Marr-Lyon, P. V orobieff, and R. Benjamin, A quantitative
study of the interaction of two Richtmyer-Meshkov-unstable gas cylinders,Phys. Fluids 15, 986 (2003).
[52] Z.-G. Zhai, T. Si, L.-Y . Zou, and X.-S. Luo, Jet formation in shock-heavy gas bubble interaction,
Acta Mech. Sin. 29, 24 (2013).
[53] Y . Zhu, Z. Yang, L. Gao, and K. H. Luo, Three-dimensional shock-sulfur hexaﬂuoride bubble interaction,
AIP Adv. 9, 115306 (2019).
[54] Y . Zhu, L. Yu, J. Pan, Z. Pan, and P. Zhang, Jet formation of SF6 bubble induced by incident and reﬂected
shock waves, Phys. Fluids 29, 126105 (2017).
[55] P. Waltrup, M. White, F. Zarlingo, and E. Gravlin, History of US Navy ramjet, scramjet, and mixed-cycle
propulsion development, J. Propul. Power 18, 14 (2002).
[56] M. L. Fotia, Mechanics of combustion mode transition in a direct-connect ramjet–scramjet experiment,
J. Propul. Power 31, 69 (2015).
113601-41

<!-- PDF_PAGE: 42 -->

BRADLEY BOYD AND DORRIN JARRAHBASHI
[57] D. Banuti, M. Raju, P. C. Ma, M. Ihme, and J.-P. Hickey, Seven questions about supercritical ﬂuids-
towards a new ﬂuid state diagram, in Proceedings of the 55th AIAA Aerospace Sciences Meeting , 2017
(unpublished), p. 1106.
[58] M. Raju, D. T. Banuti, P. C. Ma, and M. Ihme, Widom lines in binary mixtures of supercritical ﬂuids,
Sci. Rep. 7, 3027 (2017).
[59] J. W. Chae, H. S. Yang, and W. S. Yoon, Supercritical droplet dynamics and emission in low speed
cross-ﬂows, J. Mech. Sci. Technol. 22, 1586 (2008).
[60] V . Yang, Modeling of supercritical vaporization, mixing, and combustion processes in liquid-fueled
propulsion systems, Proc. Combust. Inst. 28, 925 (2000).
[61] V . Yang, N. N., and J.-S. Shuen, Vaporization of liquid oxygen (LOX) droplets in supercritical hydrogen
environments, Combust. Sci. Technol. 97, 247 (1994).
[62] K.-C. Hsieh, Droplet behavior at supercritical conditions, Recent Adv. Spray Combust.: Spray Atom.
Drop Burn. Phenom. 1, 413 (1996).
[63] C. Crua, J. Manin, and L. M. Pickett, On the transcritical mixing of fuels at diesel engine conditions,
Fuel 208, 535 (2017).
[64] H. Meng, G. C. Hsiao, V . Yang, and J. S. Shuen, Transport and dynamics of liquid oxygen droplets in
supercritical hydrogen streams, J. Fluid Mech. 527, 115 (2005).
[65] P. Das and H. S. Udaykumar, A sharp-interface method for the simulation of shock-induced vaporization
of droplets, J. Comput. Phys. 405, 109005 (2020).
[66] H. J. Q. Wan, R. Deiterding, and V . Eliasson, Numerical and experimental investigation of oblique shock
wave refection of a water wedge, J. Fluid Mech. 826, 732 (2017).
[67] D. P. Garrick, M. Owkes, and J. D. Regele, A ﬁnite-volume HLLC-based scheme for compressible
interfacial ﬂows with surface tension, J. Comput. Phys. 339, 46 (2017).
[68] J. C. Meng and T. Colonius, Numerical simulations of the early stages of high-speed droplet breakup,
Shock Waves 25, 399 (2014).
[69] D. P. Garrick, W. A. Hagen, and J. D. Regele, An interface capturing scheme for modeling atomization
in compressible ﬂows, J. Comput. Phys. 344, 260 (2017).
[70] P. Tudisco and S. Menon, Numerical investigations of phase-separation during multi-component mixing
at super-critical conditions, Flow, Turbul. Combust. 104, 693 (2020).
[71] B. Boyd and D. Jarrahbashi, A diffuse-interface method for reducing spurious pressure oscillations in
multicomponent transcritical ﬂow simulations, Comput. Fluids 222, 104924 (2021).
[72] R. Abgrall, How to prevent pressure oscillations in multicomponent ﬂow calculations: A quasi conser-
vative approach, J. Comput. Phys. 125, 150 (1996).
[73] P. C. Ma, Y . Lv, and M. Ihme, An entropy-stable hybrid scheme for simulations of transcritical real-ﬂuid
ﬂows, J. Comput. Phys. 340, 330 (2017).
[74] P. C. Ma, H. Wu, T. Jaravel, L. Bravo, and M. Ihme, Large-eddy simulations of transcritical injection
and auto-ignition using diffuse-interface method and ﬁnite-rate chemistry,Proc. Combust. Inst. 37, 3303
(2019).
[75] J. Matheis and S. Hickel, Multi-component vapor-liquid equilibrium model for LES of high-pressure
fuel injection and application to ECN Spray A, Int. J. Multiphase Flow 99, 294 (2018).
[76] A. M. Ruiz, G. Lacaze, J. C. Oefelein, R. Mari, B. Cuenot, L. Selle, and T. Poinsot, Numerical benchmark
for high-Reynolds-number supercritical ﬂows with large density gradients, AIAA J. 54, 1445 (2016).
[77] T. Schmitt, L. Selle, A. Ruiz, and B. Cuenot, Large-eddy simulation of supercritical-pressure round jets,
AIAA J. 48, 2133 (2010).
[78] H. Müller, C. A. Niedermeier, J. Matheis, M. Pﬁtzner, and S. Hickel, Large-eddy simulation of nitrogen
injection at trans-and supercritical conditions, Phys. Fluids 28, 015102 (2016).
[79] J. Oefelein, R. Dahms, and G. Lacaze, Detailed modeling and simulation of high-pressure fuel injection
processes in diesel engines, SAE Int. J. Engines 5, 1410 (2012).
[80] W. Wei, H. Liu, M. Xie, M. Jia, and M. Yue, Large eddy simulation and proper orthogonal decomposition
analysis of fuel injection under trans/supercritical conditions, Comput. Fluids 179, 150 (2019).
113601-42

<!-- PDF_PAGE: 43 -->

NUMERICAL STUDY OF THE TRANSCRITICAL …
[81] D. T. Banuti, P. C. Ma, and M. Ihme, Phase separation analysis in supercritical injection using large-eddy-
simulation and vapor-liquid-equilibrium, in Proceedings of the 53rd AIAA/SAE/ASEE Joint Propulsion
Conference, 2017 (unpublished), p. 4764.
[82] N. Okong’o and J. Bellan, Perturbation and initial Reynolds number effects on transition attainment of
supercritical, binary, temporal mixing layers, Comput. Fluids 33, 1023 (2004).
[83] N. Okong’o and J. Bellan, Small-scale dissipation in binary-species, thermodynamically supercritical,
transitional mixing layers, Comput. Fluids 39, 1112 (2010).
[84] D. T. Banuti, M. Raju, and M. Ihme, Supercritical pseudoboiling for general ﬂuids and its application to
injection, Annual Research Briefs, 211 (2016).
[85] M. Oschwald, J. Smith, R. Branam, J. Hussong, A. Schik, B. Chehroudi, and D. Talley, Injection of
ﬂuids into supercritical environments, Combust. Sci. Technol. 178, 49 (2006).
[86] D.-Y . Peng and D. B. Robinson, A new two-constant equation of state,Indust. Eng. Chem. Fundam. 15,
59 (1976).
[87] B. J. McBride, Coefﬁcients for Calculating Thermodynamic and Transport Properties of Individual
Species (NASA Langley Research Center, Washington, DC, 1993), V ol. 4513.
[88] P. C. Ma, H. Wu, D. T. Banuti, and M. Ihme, On the numerical behavior of diffuse-interface methods for
transcritical real-ﬂuids simulations, Int. J. Multiphase Flow 113, 231 (2019).
[89] E. Johnsen and T. Colonius, Implementation of WENO schemes in compressible multicomponent ﬂow
problems, J. Comput. Phys. 219, 715 (2006).
[90] V . Coralic and T. Colonius, Finite-volume WENO scheme for viscous compressible multicomponent
ﬂows, J. Comput. Phys. 274, 95 (2014).
[91] A. Harten, B. Engquist, S. Osher, and S. R. Chakravarthy, Uniformly high order accurate essentially
non-oscillatory schemes, III, J. Comput. Phys. 131, 3 (1997).
[92] J. Qiu and C.-W. Shu, On the construction, comparison, and local characteristic decomposition for high-
order central WENO schemes, J. Comput. Phys. 183, 187 (2002).
[93] S. Gottlieb and C.-W. Shu, Total variation diminishing Runge-Kutta schemes, Math. Comput. 67,7 3
(1998).
[94] B. Boyd and S. Becker, Numerical modelling of an acoustically-driven bubble collapse near a solid
boundary, Fluid Dyn. Res. 50, 065506 (2018).
[95] B. Boyd and S. Becker, Numerical modeling of the acoustically driven growth and collapse of a
cavitation bubble near a wall, Phys. Fluids 31, 032102 (2019).
[96] X. Zhang and C.-W. Shu, Maximum-principle-satisfying and positivity-preserving high-order schemes
for conservation laws: Survey and new developments,P r o c .R .S o c .A467, 2752 (2011).
[97] B. Boyd, Numerical modelling of an acoustically-driven bubble: The growth and collapse near a wall,
Ph.D. thesis, University of Canterbury, 2018.
[98] R. P. Fedkiw, T. Aslam, B. Merriman, and S. Osher, A non-oscillatory Eulerian approach to interfaces
in multimaterial ﬂows (the ghost ﬂuid method), J. Comput. Phys. 152, 457 (1999).
[99] B. Hejazialhosseini, D. Rossinelli, M. Bergdorf, and P. Koumoutsakos, High order ﬁnite volume methods
on wavelet-adapted grids with local time-stepping on multicore architectures for the simulation of shock-
bubble interactions, J. Comput. Phys. 229
, 8364 (2010).
[100] X. Y . Hu and B. C. Khoo, An interface interaction method for compressible multiﬂuids,J. Comput. Phys.
198, 35 (2004).
[101] W. Liu, L. Yuan, and C.-W. Shu, A conservative modiﬁcation to the ghost ﬂuid method for compressible
multiphase ﬂows, Commun. Comput. Phys. 10, 785 (2015).
[102] A. Marquina and P. Mulet, A ﬂux-split algorithm applied to conservative models for multicomponent
compressible ﬂows, J. Comput. Phys. 185, 120 (2003).
[103] R. K. Shukla, C. Pantano, and J. B. Freund, An interface capturing method for the simulation of multi-
phase compressible ﬂows, J. Comput. Phys. 229, 7411 (2010).
[104] K. K. So, X. Y . Hu, and N. A. Adams, Anti-diffusion interface sharpening technique for two-phase
compressible ﬂow simulations, J. Comput. Phys. 231, 4304 (2012).
[105] H. Terashima and G. Tryggvason, A front-tracking/ghost-ﬂuid method for ﬂuid interfaces in compress-
ible ﬂows, J. Comput. Phys. 228, 4012 (2009).
113601-43

<!-- PDF_PAGE: 44 -->

BRADLEY BOYD AND DORRIN JARRAHBASHI
[106] L. Wang, G. M. D. Currao, F. Han, A. J. Neely, J. Young, and F.-B. Tian, An immersed boundary method
for ﬂuid–structure interaction with compressible multiphase ﬂows, J. Comput. Phys. 346, 131 (2017).
[107] D. Ranjan, J. H. Niederhaus, J. G. Oakley, M. H. Anderson, R. Bonazza, and J. A. Greenough,
Shock-bubble interactions: Features of divergent shock-refraction geometry observed in experiments
and simulations, Phys. Fluids 20, 036101 (2008).
[108] K. Narayanaswamy, P. Pepiot, and H. Pitsch, A chemical mechanism for low to high temperature
oxidation of n-dodecane as a component of transportation fuel surrogates, Combust. Flame 161, 866
(2014).
[109] D. R. Guildenbecher, C. López-Rivera, and P. E. Sojka, Secondary atomization, Exp. Fluids 46, 371
(2009).
[110] E. Meshkov, Instability of the interface of two gases accelerated by a shock wave, Fluid Dyn. 4, 101
(1969).
[111] R. D. Richtmyer, Taylor instability in shock acceleration of compressible ﬂuids, Los Alamos Scientiﬁc
Lab., N. Mex (1954), https://www.osti.gov/biblio/4272289.
[112] T. G. Theofanous and G. J. Li, On the physics of aerobreakup, Phys. Fluids 20, 052103 (2008).
[113] G. C. Orlicz, S. Balasubramanian, and K. P. Prestridge, Incident shock Mach number effects on
Richtmyer-Meshkov mixing in a heavy gas layer, Phys. Fluids 25, 114101 (2013).
[114] A. R. Staff, Equations, tables, and charts for compressible ﬂow, NACA Report No. 1135, 1953 (unpub-
lished).
[115] C.-H. Chang and M.-S. Liou, A robust and accurate approach to computing compressible multiphase
ﬂow: Stratiﬁed ﬂow model and AUSM+-up scheme, J. Comput. Phys. 225, 840 (2007).
[116] A. Wierzba and K. Takayama, Experimental investigation of the aerodynamic breakup of liquid drops,
AIAA J. 26, 1329 (1988).
[117] G. Allaire, S. Clerc, and S. Kokh, A ﬁve-equation model for the simulation of interfaces between
compressible ﬂuids, J. Comput. Phys. 181, 577 (2002).
113601-44
