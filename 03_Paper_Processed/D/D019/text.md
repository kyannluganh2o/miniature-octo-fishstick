<!-- PDF_PAGE: 1 -->

PHYSICAL REVIEW FLUIDS 11, 034303 (2026)
Comparative analysis of detonation and shock waves interacting
with droplets: Characteristics and mechanisms
Hanbing Zou ,1 Xin Jin ,1 Haotian Chen ,1 Wei Wang,2 Sheng Xu ,1,* and Bing Wang 1,3,†
1School of Aerospace Engineering, Tsinghua University, Beijing, People’s Republic of China
2Senior Department of Orthopedics, F ourth Medical Center of
PLA General Hospital, Beijing, People’s Republic of China
3Institute for Aero Engine, Tsinghua University, Beijing, People’s Republic of China
(Received 6 May 2025; accepted 18 February 2026; published 18 March 2026)
The interaction mechanisms among detonation waves, shock waves, and liquid droplets
play a critical role in advancing propulsion technologies such as rotating detonation en-
gines. This study conducts a detailed comparison of wave dynamics, cavitation phenomena,
and droplet deformation during the detonation wave and the shock-wave interactions with
a water droplet, employing a high-resolution numerical model that integrates multicom-
ponent compressible ﬂuid dynamics, chemical reactions, and phase transition effects.
Numerical simulations reveal distinct characteristics between detonation and shock-
induced phenomena. Unlike the shock wave, detonation-induced reﬂected shock waves
exhibit signiﬁcantly higher propagation velocities while maintaining nearly identical wave
conﬁgurations, a phenomenon this study mechanistically explains by the unique postwave
conditions. A fundamental distinction arises in cavitation dynamics between the detonation
wave and the shock wave, with the detonation-wave triggering cavitation zone collapse at
signiﬁcantly higher rates compared with the shock wave. This difference is attributed to
the shorter persistence of low-pressure regions behind the detonation front, where rapid
attenuation of postwave pressure and ﬂow velocity occurs. Moreover, detonation-induced
ﬂow interactions create unique droplet fragmentation patterns. The rapid postwave velocity
reduction prevents Rayleigh-Taylor instability-driven forward jet formation, instead caus-
ing leeward-side ﬂattening of the droplet through the vortex in the recirculation zone.
DOI: 10.1103/mp9z-tlk3
I. INTRODUCTION
As a novel propulsion system, the rotating detonation engine, demonstrates signiﬁcant theoret-
ical performance advantages over conventional propulsion systems and has emerged as a critical
research direction in future aerospace propulsion technologies [1]. In gas-liquid two-phase combus-
tion environments, dynamic interaction processes among detonation waves, shock waves, and fuel
droplets are ubiquitous. However, signiﬁcant knowledge gaps remain in the comparative analysis of
the microscopic mechanisms underlying the evolution of wave conﬁgurations, phase transitions, and
atomization characteristics of droplets subjected to both detonation waves and shock waves [ 2,3].
Therefore, conducting in-depth investigations into the interactions between detonation and shock
waves and droplets carries substantial scientiﬁc merit.
Compared with the complex interactions between detonation waves and droplets, signiﬁ-
cant breakthroughs have been achieved in recent years through experimental and computational
*Contact author: meredith.xs@163.com
†Contact author: wbing@tsinghua.edu.cn
2469-990X/2026/11(3)/034303(28) 034303-1 ©2026 American Physical Society

<!-- PDF_PAGE: 2 -->

ZOU, JIN, CHEN, W ANG, XU, AND W ANG
investigations into the interaction mechanisms between shock waves and droplets. Systematic
investigation on breakup processes in liquid columns and droplets, along with the dynamic evolution
of wave structures, have been conducted using shock tube facilities [ 4,5] and exploding wire [ 6].
The study not only proposed a theoretical model for boundary-layer stripping [ 4] but also estab-
lished a benchmark case for validating numerical simulations [ 5], while revealing that expansion
wave focusing could potentially induce cavitation phenomena [ 6,7]. In numerical simulations, the
two-phase multicomponent compressible ﬂuid model plays a pivotal role, governing the model’s ca-
pability for high-precision resolution of gas-liquid interface identiﬁcation [8] and cavitation location
prediction [9], both of which are critical to determining the accuracy of simulation results. Through
experimental and numerical approaches, the phenomenon of shock-induced droplet breakup has
been systematically investigated. Classical theories categorize droplet breakup regimes based on the
Weber number into vibrational breakup, bag breakup, bag-and-stamen breakup, shear and stripping
breakup, and catastrophic and shattering breakup [10]. Employing laser-induced ﬂuorescence tech-
nology, the Theofanous research team revealed two distinct breakup mechanisms in high-speed gas
ﬂows from a physics-based classiﬁcation perspective: Rayleigh-Taylor (RT) instability-dominated
fragmentation and shear-induced entrainment mode [ 11], thereby complementing conventional
theories of breakup regimes. Furthermore, apart from studies on planar shock waves, as recent
works have highlighted, different postwave characteristics, such as rapid attenuation of pressure and
ﬂow velocity, can be observed in ﬂows induced by conical shocks [12,13]. Similarly, investigations
into divergent shock waves have demonstrated that shock curvature plays a signiﬁcant role, altering
the formation location of liquid ligaments and the inception point of Kelvin-Helmholtz instabilities
compared with the planar case [14].
In the ﬁeld of detonation wave-droplet interactions, detonation tube facilities have been used
to examine the interactions between detonation waves and liquid droplets of diethylcyclohexane
[15], water [ 16], JP-10 jet propellant [ 2], and RP-2 rocket propellant [ 17]. The results indicate
that detonation wave–induced droplet breakup can be divided into two distinct stages: a Kelvin-
Helmholtz instability-dominated stage and a Rayleigh-Taylor instability-dominated stage [16]. The
detonation wave suppresses small-scale breakup processes of droplets, thereby altering the dominant
breakup mechanism [17]. In numerical simulations, Xuet al. [18] conducted high-resolution numer-
ical simulations to analyze the transient interaction process between detonation waves and liquid
droplets. Their study revealed that multidimensional detonation structures induce the formation of
distinct concave features on the windward side of droplets during shock interaction.
Although the dynamic behaviors of the interactions between shock and detonation waves and
droplets have been extensively investigated, detailed comparisons between these scenarios remain
unexplored in existing literature. Huang and Lin conducted a preliminary investigation into the
differences in droplet dynamics under detonation versus shock waves. However, limitations in
numerical methods and computing power have hindered consensus on the fundamental differences
between these two high-speed ﬂuid-structure interaction mechanisms [19]. The comparative inves-
tigation of shock or detonation-droplet interactions is crucial for elucidating the inﬂuence of heat
release, which holds signiﬁcant engineering implications for combustor design optimization. The
present work employs an enhanced numerical model to analyze multiphysics coupling mechanisms
and is organized as follows. In Sec. II, the physical model for the interaction of a planar detonation
and shock wave with a water droplet is described. The two-phase three-component governing model
coupling with the phase transition and chemical reaction models is presented in Sec. III,a sw e l la s
the grid independence validated in this section. Section IV compares wave evolution and cavitation
dynamics under detonation and shock waves. Section V reveals differential droplet deformation
mechanisms between these wave types. Finally, conclusions are given in Sec.VI.
II. PHYSICAL MODEL
The interaction between the detonation and shock waves and the droplet, as illustrated in
Fig. 1(a), is a strong compressible gas-liquid hydrodynamics problem [18], which involves complex
034303-2

<!-- PDF_PAGE: 3 -->

COMPARATIVE ANALYSIS OF DETONATION AND SHOCK …
FIG. 1. (a) The interaction diagram between a planar detonation or shock wave and a water droplet. (b)
The schematic diagram of the planar detonation wave.
factors such as large-density-ratio discontinuities, strong shock waves, and vigorous combustions.
Previous studies [20–22] have demonstrated that two-dimensional simulations can accurately cap-
ture the qualitative interaction characteristics observed in three-dimensional droplet simulations,
while offering signiﬁcantly higher computational efﬁciency. Consequently, to balance the resolution
of ﬁne-scale wave structures with computational costs, the two-dimensional conﬁguration is adopted
in this work. However, it should be noted that the two-dimensional (2D) approximation lacks the
three-dimensional ﬂow-relieving effects. As indicated by experimental comparisons between cylin-
drical and spherical bodies [ 23], the 2D conﬁguration typically experiences higher aerodynamic
drag and exhibits stronger vortex coherence. Therefore, the 2D simulations in this study serve as
an upper-bound estimation of the interaction intensity and deformation rates. Crucially, since this
geometric bias applies systematically to both the detonation and shock-wave scenarios, it does not
compromise the validity of the comparative analysis. Besides that, the estimation of Weber number
(We) and Reynolds number (Re) for planar detonation wave and planar shock wave is presented in
Table I. The diameter of the droplet D
0 is 4.8 mm. From the table it is easy to know that the neglect
of the viscosity and capillary effects are reasonable due to the high Weber number (exceeding 1000)
and high Reynolds number (exceeding 40 000). It should be noted that this assumption is reasonable
for the droplet scale but becomes increasingly approximate as the deformation generates some
microstructures such as ligamentous liquid threads and child droplets due to their smaller scales
[24].
To ensure the wave-front stability of the planar detonation wave during its propagation, the sto-
ichiometric H
2/O2 premixture with 70% argon dilution within a normal-temperature (T0 = 300 K)
and low-pressure (p0 = 50 kPa) environment is adopted [25]. As shown in Fig. 1(b), the schematic
proﬁle of a 1D detonation wave consists of the induction and exothermic zones [ 26]. Within
the induction zone, the leading shock wave compresses the reactant mixture intensely, activating
it thermodynamically and chemically reaching the von-Neumann state. In the exothermic zone,
intensive chemical reactions occur with the pressure and density decreasing and the temperature in-
creasing. After the heat release, the ﬂow parameters remain constant, reaching the Chapman-Jouguet
state. Furthermore, in this study, the planar shock wave is modeled as a theoretically zero-reaction
TABLE I. Weber number and Reynolds number for two types of incident waves.
Wave type Weber number (We) Reynolds number (Re)
Detonation wave 5 .42 × 104 4.80 × 104
Shock wave 3 .18 × 105 2.00 × 105
034303-3

<!-- PDF_PAGE: 4 -->

ZOU, JIN, CHEN, W ANG, XU, AND W ANG
detonation wave characterized by an inﬁnitely extended induction zone and a negligible exothermic
zone. In other words, the planar shock intensity is maintained equivalent to the leading shock
intensity of the planar detonation.
III. NUMERICAL METHODOLOGY
A. Governing equations
In the present study, the three-component compressible two-phase model considering the phase
transition effect, which is extended from the classical ﬁve-equation model [ 27,28], is employed
to solve the aforementioned hydrodynamic problem. The two-step chemical reaction model [ 25],
which is widely adopted in previous gaseous detonation studies [ 29], is employed to characterize
the detonation characteristics, speciﬁcally capturing the coupled effects of the heat release and the
leading shock wave inherent to Zeldovich-von Neumann-Döring (ZND) theory. The ﬁnal governing
equations are constituted as follows:
∂(α
kρk )
∂t + ∇ · (αkρk u) = Sρ,k (k = l, v, g), (1)
∂(ρu)
∂t + ∇ · (ρu2 + pI) = 0, (2)
∂(ρE )
∂t + ∇ · [(ρE + p)u] = 0, (3)
∂αk
∂t + u · ∇αk = Sα,k (k = l, v), (4)
∂(αgρgξ)
∂t + ∇ · (αgρgξu) = ωξ, (5)
∂(αgρgλ)
∂t + ∇ · (αgρgλu) = ωλ, (6)
where αk and ρk are the volume fraction and density of the kth component, respectively. The
subscripts “l,” “v,” and “ g” denote the liquid, vapor, and phase transition inert gas, respectively;
ξand λ are two reaction parameters related to the two-step reaction model. Sρ,k and Sα,k are source
terms of the phase transition effect.ωξ and ωλ are source terms of the detonation combustion effect.
ρ, u, p, and E = 0.5u2 + e are the density, velocity vector, pressure, and speciﬁc total energy of the
mixture, respectively. e is the speciﬁc internal energy,
ρ =
∑
k=l,v,g
αkρk,ρ e =
∑
k=l,v,g
αkρk ek − αgρgλQ, (7)
where ek is the speciﬁc internal energy of the components k and Q is the speciﬁc reaction heat
release. The volume fraction of the inert gas, from the perspective of the phase transition effect, αg
is constrained by
αl + αv + αg ≡ 1. (8)
Moreover, in this work, the stiffened-gas equation of state (SG-EOS) [ 30] for describing the
thermal properties of all components is adopted to close the governing equations,
ek (p,ρk ) = p + γk p∞ ,k
ρk (γk − 1) + e∞ ,k, (9)
ρk (p, T ) = p + p∞ ,k
Cv,k T (γk − 1), (10)
ck =
√
γk (p + p∞ ,k )
ρk
, (11)
034303-4

<!-- PDF_PAGE: 5 -->

COMPARATIVE ANALYSIS OF DETONATION AND SHOCK …
TABLE II. The parameters involved in the SG-EOS [30].
Phases γk p∞ ,k [Pa] Cv,k [J/(kg K)] s∞ ,k [J/kg] e∞ ,k [J/(kg K)]
Water [l] 2.057 1.066 × 109 3449.0 −1.995 × 106 3.578 × 104
Water [v] 1.327 0.0 1200.0 1.995 × 106 2.41 × 103
2H2−O2−7Ar 1.493 0.0 557.7 0.0 0.0
gk (p, T ) = (γkCv,k − s∞ ,k )T + Cv,k T ln Tγk
(p + p∞ ,k )γk−1 + e∞ ,k, (12)
μv (T, gv,αl,αv ) = gv + (γv − 1)Cv,1T ln αv
1 − αl
, (13)
where γk, Cv,k, p∞ ,k, e∞ ,k, and s∞ ,k are speciﬁc heat ratio, speciﬁc heat capacity at constant volume,
reference pressure, reference energy, and reference entropy of the kth component, respectively.
ck and gk are soundspeed and speciﬁc Gibbs free energy of the components k. μv represents the
chemical potential of the vapor component. The corresponding values of these parameters are listed
in Table II.
Here the mixture soundspeed is clariﬁed as [31,32]
ρc
2 =
p
(∑
k=l,v,g
αk
γk−1 + 1
)
+ ∑
k=l,v,g
αk
γk
p∞ ,kγk − 1
∑
k=l,v,g
αk
γk−1
. (14)
To capture the cavitation behavior inside the droplet, the chemical potential relaxation phase
transition model [ 33–35] is adopted in this work. Hence, the phase transition terms Sρ,k and Sα,k,
shown in governing equations, can be respectively expressed as
Sρ,l = η(μv − gl ), Sρ,v =− Sρ,l = η(gl − μv ), Sρ,g = 0, (15)
Sα,l = Sρ,l
σl
= η
σl
(μv − gl ), Sα,v = Sρ,v
σv
= η
σv
(gl − μv ), Sα,g = Sρ,g
σg
= 0, (16)
where η (⩾ 0) is the relaxation parameter for the chemical potential. The parameters σk have the
same physical dimension as the density [ 35]. Furthermore, building upon the operator splitting
method [36] that decouples the advancing of the ﬂow, phase transition and chemical reaction terms,
the transient relaxation equilibrium assumption [ 9] to mitigate the signiﬁcant numerical stiffness,
encountered in phase transition advancing, is implemented in this study. To determine the criterion
for triggering the phase transition, a parameter, f
μ, is deﬁned as the difference between the Gibbs
free energy of the vapor and liquid phases,
fμ = gv + (γv − 1)Cv,v T ln
( αv
1 − αl
)
− gl, (17)
where gv and gl are the speciﬁc Gibbs free energies of the vapor and liquid, respectively.
The value of fμ in each computational cell governs the phase transition process. Speciﬁcally,
condensation is initiated if fμ > 0, the system is in phase equilibrium whenfμ = 0, and evaporation
is triggered if fμ < 0. Speciﬁcally, when the phase transition is triggered, the parameter η is
set to inﬁnity; otherwise, it remains zero. The chemical potential relaxation method is adopted
from Han et al. [37], where a comprehensive description is provided. It should be noted that
thermal conduction is explicitly neglected in the present numerical framework. This simpliﬁcation is
justiﬁed by a timescale analysis. According to Refs. [38,39], the characteristic timescale of thermal
conduction within the droplet is given by t
HC = ρwCv,w R2
D/κ, where ρw, Cv,w, and κ respectively
denote the density, isochoric speciﬁc heat capacity, and thermal conductivity of liquid water.
Substituting the relevant physical properties yields a thermal conduction timescale on the order
034303-5

<!-- PDF_PAGE: 6 -->

ZOU, JIN, CHEN, W ANG, XU, AND W ANG
of O(102 )s. In contrast, the characteristic timescale of the droplet deformation and wave interaction
is deﬁned as tD = D0
√ρw/ρg/ug, which is approximately O(10−4 )s, where ρg and ug respectively
denote the density of gas and the velocity behind the shock wave. A comparison of these two scales
reveals that the time required for signiﬁcant thermal diffusion is roughly 10
6 times longer than the
duration of the shock- and detonation-wave interaction. Consequently, thermal conduction exerts a
negligible inﬂuence on the main droplet during the deformation process. It is acknowledged that
for microscopic child droplets generated during late-stage fragmentation, the signiﬁcantly reduced
radius R
D causes the thermal conduction timescale to decrease quadratically, potentially rendering
thermal effects comparable to the deformation timescale. However, since the primary focus of this
study is the dynamics of the main droplet, the neglect of thermal conductivity constitutes a valid
and robust assumption.
B. Two-step reaction model
As illustrated in the governing equations, the present study employs the two-step reaction model
[25] to characterize the detonation dynamics, which is abstracted into an induction substep and a
heat release substep. Therefore, two additional reaction progress variables are introduced into the
numerical solving framework: one is the induction reaction indexξand the other is the heat release
index λ. The reaction source terms corresponding to those two indexes are separately expressed as
ω
ξ = αgρgH(1 − ξ)kI exp
[
− EI
Rg
( 1
T − 1
TS
)]
, (18)
ωλ = αgρg[1 − H(1 − ξ)]kR(1 − λ)e x p
(
− ER
RgT
)
, (19)
where kI and kR represent the induction and reaction preexponential rate constants, which control
the thickness of the induction and reaction zones, i.e., /Delta1I and /Delta1R, respectively. EI and ER represent
the chemical reaction activation energies of each reaction substep.Rg and TS denote the gas constant
of the combustible mixture (2H 2−O2−7Ar) and the postshock temperature behind the detonation
leading front, respectively. H(1-ξ) is a step function deﬁned as
H(1 − ξ) =
{
1, 0,<ξ ⩽ 1
0,ξ = 0 . (20)
For convenience, the activation energies EI and ER are normalized,
εI = EI
RgTS
,ε R = ER
RgTS
. (21)
Corresponding to the aforementioned combustible mixture and initial conditions, the main pa-
rameters of the two-step reaction model are set to beQ = 1.046 × 106 J/kg, kI =− 2.49 × 106 s−1,
kR = 3.77 × 106 s−1, εI = 4.87, εR = 1.0, Rg = 274.7J /(kg K), and TS = 2012.6K .
C. Numerical treatments
In the present study, all numerical simulations are carried out by our in-house software
(SCP-tran), which has been previously applied to study a variety of compressible multiphase
ﬂow problems [ 9,22,40]. The key-solver of SCP-tran uses a ﬁnite volume method to discretize
the above governing equations in a uniform Cartesian grid system. The second-order monotone
upstream centred scheme for conservation laws [ 41] with a Minmod limiter and the ﬁfth-order
incremental-stencil weighted essentially nonoscillatory scheme [42] are hybridized and applied for
the spatial reconstruction to the primitive variables. As the variant of the ﬁve-equation model is
a type of diffuse interface method, the initial sharpened two-phase interface inherently exhibits
numerical diffusion [43] after several time steps advancing. The tangent of hyperbola for interface
capturing [44] sharpening method is employed in two-phase interface reconstructions to avoid the
034303-6

<!-- PDF_PAGE: 7 -->

COMPARATIVE ANALYSIS OF DETONATION AND SHOCK …
FIG. 2. The numerical simulation results under three different grid resolutions. (a) Grid 2.5 µm, (b) grid 5
µm, and (c) grid 10 µm.
excessive nonphysical diffusion of the two-phase interface. The Godunov-type Harten–Lax–van
Leer contact [ 45] approximate Riemann solver is employed to calculate numerical ﬂuxes. The
third-order total variation diminishing Runge-Kutta scheme [46] is adopted in time integration. The
Courant-Friedrich-Lewis number is set to 0.4 for all simulations.
D. Grid independence veriﬁcation
Since the curved droplet interface cannot be accurately described by a uniform Cartesian grid
system, numerical veriﬁcation of the grid independence is essential for the follow-up analysis. Here
a comparative numerical analysis for detonation wave–droplet interactions under three different
grid resolutions is conducted. It should be noted that, prior to initiating the analysis in this study, we
adopted the nondimensionalization methodology proposed by Ranger and Nicholls [4] to rigorously
deﬁne the nondimensional time parameters relevant to the present investigation,
t
∗ = (t − t0 )ug
2RD
√ρl/ρg
, (22)
where ug and ρg represent the postshock gas velocity and gas density, respectively, while ρl
represents the density of the unperturbed droplet.
Figure 2 presents numerical simulation results of the initial interaction process between the
detonation wave and the droplet ( t∗ = 4.32 × 10−3) obtained under three grid resolutions. The
upper half of the ﬁgure displays density schlieren images, while the lower half shows pressure
contour maps. As evident from the numerical simulation results presented in Fig. 2, the ﬂow ﬁeld
structures including the Mach stem, slip lines, incident detonation wave (IDW), and two-phase
interface are captured in simulations conducted under three distinct grid resolutions. The ﬂow
ﬁeld structures under three different grid resolutions are found to be essentially consistent, and
the numerical simulations capture progressively more detailed ﬂow structures with increased grid
reﬁnement. To investigate the effects of grid resolution on wave conﬁguration intensities in the ﬂow
ﬁeld and two-phase interface distributions, Fig. 3 illustrates the density and pressure distribution
FIG. 3. Density and pressure distributions along the x axis under three different grid resolutions. (a) Density
distribution and (b) pressure distribution.
034303-7

<!-- PDF_PAGE: 8 -->

ZOU, JIN, CHEN, W ANG, XU, AND W ANG
FIG. 4. Comparison of deformed water droplet contour for three grid resolution of 2.5, 5, and 10 µm.
proﬁles along the x axis ( t∗ = 2.4 × 10−3) under three distinct grid resolutions. As depicted in
the curves, the density and pressure distributions under three distinct mesh resolutions exhibit
remarkable consistency. Figure 4 compares the deformation of the shocked water droplet under
different grid resolutions. As the resolution increases, ﬁner details such as surface instabilities, liquid
sheets, and thin ﬁlaments are captured more precisely. Nevertheless, the overall qualitative features,
including ﬂattening and stripping behaviors, remain highly consistent. The primary droplet proﬁles
under the three resolutions show strong agreement, with only minor discrepancies observed in the
liquid ﬁlaments near the equator. This comparison demonstrates that approximate grid convergence
is achieved between the 5- and 2.5-µm grids. Therefore, the 5-µm resolution possesses sufﬁcient
capability to capture the essential deformation characteristics of the shocked droplet. Based on
the aforementioned analysis and coupled with computational resource constraints for subsequent
simulations, the second mesh resolution (characterized by a mesh size of 5 µm) will be adopted for
all following simulation cases in this study.
IV . EVOLUTION CHARACTERISTICS OF W A VE CONFIGURA TIONS
This section investigates the spatiotemporal evolution of wave conﬁgurations and the cavitation
zone during detonation wave– and shock wave–droplet interactions. Speciﬁcally, we focus on the
dynamic coupling between shock front propagation and bubble collapse mechanisms.
A. Wave conﬁgurations topology
The interaction between a planar detonation wave and a water droplet involves a complex
sequence of gas dynamic events, including wave reﬂection, diffraction, and focusing. This process is
inherently a multiphysics problem, characterized by the tight coupling of hydrodynamic phenomena
with exothermic chemical reactions within the detonation front. Therefore, before proceeding to a
comparative analysis with a regular shock wave, it is essential to ﬁrst establish a clear and detailed
understanding of the wave-ﬁeld topology that is speciﬁc to the detonation-droplet interaction. This
section provides a foundational description of these key events. Note that the phase transition model
is disabled for this analysis. This procedure aims to prevent cavitation bubbles from obscuring the
wave conﬁguration topology within the droplet, thereby ensuring a clear visualization.
The evolution of wave conﬁgurations during the initial detonation wave–droplet interaction
process can be divided into three distinct stages. The ﬁrst stage is characterized by the generation
of a transmitted shock wave through the diffraction of the incident shock and the formation of
reﬂection-transmission wave systems. This stage begins when the IDW ﬁrst impacts the droplet’s
frontal stagnation point and ends as the transmitted shock wave (TSW) completes its reﬂection
from the droplet’s leeward surface. The windward surface of the droplet generates the reﬂected
shock wave (RSW) and TSW due to acoustic impedance mismatch ( ρ
l cl ≫ ρgcg). As the incident
034303-8

<!-- PDF_PAGE: 9 -->

COMPARATIVE ANALYSIS OF DETONATION AND SHOCK …
FIG. 5. Detonation wave–droplet interaction: Wave conﬁgurations evolution in ﬁrst stage. Density
schlieren (upper panel) and pressure contour plots (lower panel).
angle increases beyond a critical threshold, the shock-wave reﬂection pattern undergoes a distinct
transition, evolving from regular reﬂection to Mach reﬂection (Fig. 5). Following its formation,
the TSW propagates to the leeward surface of the droplet, where reﬂection generates a reﬂected
expansion wave (REW). The ﬁrst stage of the detonation wave–droplet interaction process ends
when the TSW completes its reﬂection at the droplet’s leeward surface—a state marked by the
reﬂection of the TSW wave front along the droplet’s axial direction at the rear stagnation point.
The second stage corresponds to the periodic reﬂection of expansion waves and formation of
low-pressure regions. After being generated by shock-wave reﬂection and focusing at the leeward
surface, the REW propagates windward while undergoing radial expansion. The droplet’s curved
surface induces convergence of the REW, causing a dramatic pressure reduction in the local region
that leads to negative pressure phenomena, as shown in Fig. 6(b). After convergence, the REW
propagates upstream toward the droplet and undergoes a third reﬂection-transmission process
at the droplet surface, generating the secondary reﬂected shock wave (RSW
2) and transmitted
expansion wave [Fig. 6(d)]. The second stage ends at the complete reﬂection of the REW at
the droplet’s windward surface, forming RSW 2 through wave interaction at the frontal stagnation
point.
The third stage features cyclical interactions between wave system reﬂections and energy
dissipation. As shown in Fig. 7, the third stage commences when the energy of the RSW 2 is
gradually dissipated through the sustained expansive action of the secondary reﬂected expansion
wave (REW
2). Following the reﬂection of the REW 2 at the rear stagnation point of the droplet, a
windward-propagating compressive third reﬂected shock wave (RSW 3) is formed. This sequence
establishes a recurring pattern of internal wave reﬂection and attenuation. As subsequent stages are
essentially repetitions of this cycle with progressively diminishing intensity and do not introduce
new physical phenomena, the analysis of the primary wave interaction is concluded here.
034303-9

<!-- PDF_PAGE: 10 -->

ZOU, JIN, CHEN, W ANG, XU, AND W ANG
FIG. 6. Detonation wave–droplet interaction: Wave conﬁgurations evolution in second stage. Density
schlieren (upper panel) and pressure contour plots (lower panel).
B. The inﬂuence of reaction heat release
Detonation waves, as a type of combustion wave formed by a leading shock wave with
an exothermic reaction zone, exhibit characteristic shock-wave features. To reveal the inﬂuence
of reactive heat release on the wave-droplet interaction dynamics, this study conducts detailed
comparative analyses between planar detonation waves and planar shock waves interacting with
the droplet under identical leading shock Mach number (Ma = 4.8) conditions. The numerical sim-
ulation results demonstrate that the two types of wave conﬁgurations exhibit remarkable similarity
in their structural evolution patterns. Within the three-stage theoretical framework established in
prior sections, a comparative analysis is now conducted on the interaction dynamics between these
wave conﬁgurations. It should be noted that, to isolate the inﬂuence of reaction heat release on wave
conﬁgurations, the phase transition model is deliberately disabled in this section.
FIG. 7. Detonation wave–droplet interaction: Wave conﬁgurations evolution in third stage. Density
schlieren (upper panel) and pressure contour plots (lower panel).
034303-10

<!-- PDF_PAGE: 11 -->

COMPARATIVE ANALYSIS OF DETONATION AND SHOCK …
FIG. 8. Detonation wave– and shock wave–droplet interaction: Wave conﬁgurations evolution in early
phase of ﬁrst stage. Density schlieren (upper panel) and pressure contour plots (lower panel). [(a) and (b)]
Detonation wave and [(c) and (d)] shock wave.
During the initial period of the ﬁrst stage, following the interaction between the incident shock
wave and the droplet’s frontal stagnation point, a RSW and a TSW emerge simultaneously. As
shown in Fig. 8, the planar detonation wave and planar shock wave exhibit negligible differences in
their wave conﬁgurations during the initial period of reﬂection and transmission but differ in their
postwave pressure distributions. As shown in Fig. 8(b), the TSW of the planar detonation wave
generates a pronounced pressure peak at its leading edge, followed by a rapid pressure decline. In
contrast, Fig. 8(d) demonstrates that the TSW of the planar shock wave exhibits no distinct pressure
peak, with the pressure distribution remaining relatively uniform in the region between the TSW
and RSW.
This phenomenon can be attributed to the elevation in temperature and reduction in pressure
within the postdetonation wave region, a consequence of exothermic reactions in the chemically
reactive system. To clearly demonstrate the pressure reduction, the pressure distribution along x
axis at various times t
∗ is plotted in Fig. 9. It is evident from Fig. 9 that at a speciﬁc position x,
the pressure drop following the detonation wave’s TSW is considerably more signiﬁcant than that
of the shock wave. Furthermore, at a speciﬁc time t
∗, the pressure reduction after the TSW front is
more pronounced for the detonation wave compared with the shock wave, a ﬁnding that corroborates
the pressure peak observed in Fig. 8.
As shown in Fig. 10, the key distinction in wave system evolution between planar detonation and
planar shock waves at the end of the ﬁrst stage lies in the disparate axial propagation velocities of
their RSWs. A comparison of Figs.10(a) and 10(b) reveals that the axial propagation velocity of the
RSW in the planar detonation wave is signiﬁcantly greater than that in the planar shock wave. This
phenomenon arises from the variations in sound speed and ﬂow velocity across the detonation wave
front and rear. The speciﬁc reason can be explained through the Mach number relation of a moving
034303-11

<!-- PDF_PAGE: 12 -->

ZOU, JIN, CHEN, W ANG, XU, AND W ANG
FIG. 9. Temporal evolution of the pressure proﬁle along the x axis in ﬁrst stage.
shock. Based on the Mach number relation of a moving shock [ 47], the axial velocity of the RSW
in Fig. 10 can be determined:
Ma2
2 = 1 + γ−1
2 Ma12
γMa12 − γ−1
2
, (23)
Ma1 = u1 + us
c1
, Ma2 = u2 + us
c2
, (24)
where Ma 1 and Ma 2 represent the local Mach numbers upstream and downstream of the RSW,
respectively. u1 and u2 represent the ﬂow velocities at corresponding positions, c1 and c2 represent
the local sound speeds, while us represents the propagation velocity of the shock wave and γ
represents the speciﬁc heat ratio.
The inﬂuence of the parameters u1, u2, c1, c2,o n us can be quantiﬁed by computing the partial
derivatives of us with respect to each of these variables. It should be noted that, given the negligible
variation of γ across the RSWs [26], it is treated as a constant. The detailed derivation is provided
FIG. 10. Detonation wave– and shock wave–droplet interaction: Wave conﬁgurations evolution in end
phase of ﬁrst stage. Density schlieren (upper panel), pressure contour plots (lower panel). (a) Detonation wave
and (b) shock wave.
034303-12

<!-- PDF_PAGE: 13 -->

COMPARATIVE ANALYSIS OF DETONATION AND SHOCK …
FIG. 11. The axial ﬂow velocity and sound speed proﬁles of detonation wave and shock wave (t∗ = 2.09 ×
10− 3
).
in the Appendix for brevity. The ﬁnal expressions for these derivatives are as follows:
∂us
∂u1
< 0, ∂us
∂u2
< 0, ∂us
∂c1
> 0, and ∂us
∂c2
> 0. (25)
To analyze the origin of velocity differences between the RSWs in shock and detonation waves,
we plot the ﬂow velocity and sound speed proﬁles.
Figure 11 compares the RSW structures in detonation and shock waves. The yellow-shaded
region denotes the RSW position in the detonation wave, while the green-shaded region indicates
the RSW in the shock wave. As the RSW propagates upstream against the ﬂow direction, the
subscript “1” denotes upstream states and “2” denotes downstream states relative to the RSW.
Subscripts “D” and “S” distinguish detonation-wave and shock-wave parameters, respectively.
From the ﬁgure, quantitative analysis reveals u
1D < u1S, u2D < u2S, c1D > c1S, and c2D > c2S.B y
the conclusion ( 25) we obtained above, for detonation-wave RSWs, the negative disparities in u1
and u2 and positive disparities in c1 and c2 synergistically enhance ﬂow velocity us. Physically,
these parameter disparities originate from exothermic heat release. In detonation waves, their high-
temperature combustion characteristics induce a signiﬁcant temperature elevation in the postwave
region, thereby causing both c
1 and c2 to surpass the corresponding values observed in planar
shock waves. Furthermore, theoretical analysis based on the Rankine-Hugoniot relations across
detonation waves [26] demonstrates that the detonation postwave velocityu
1D exhibits signiﬁcantly
greater deceleration compared with u1S of shock waves. The synergistic action of these physical
mechanisms ultimately leads to a marked enhancement in the axial propagation velocity of the
detonation-induced RSW relative to the shock-induced RSW.
In the second stage (as shown in Fig. 10), the TSWs generated by the planar detonation wave
and the planar shock wave both produce the REW upon impinging on the rear stagnation point. As
shown in Fig.12, these perturbed wave conﬁgurations, driven by the surface curvature of the droplet,
converge and generate a low-pressure region. During this process, the REW maintains upstream
propagation while undergoing secondary reﬂection and transmission.
As shown in Fig. 13, the REWs generated by both the planar shock and detonation waves
produce pressure minima of approximately –60 MPa, a level sufﬁcient to induce cavitation in water.
However, consistent with the exclusion of the phase transition model in this section, no cavitation is
observed in Fig. 12. Had the cavitation model been included, these large negative pressure regions
034303-13

<!-- PDF_PAGE: 14 -->

ZOU, JIN, CHEN, W ANG, XU, AND W ANG
FIG. 12. Detonation wave– and shock wave–droplet interaction: Wave conﬁgurations evolution in second
stage. Density schlieren (upper panel) and pressure contour plots (lower panel). [(a) and (b)] Detonation wave
and [(c) and (d)] shock wave.
would be replaced by the formation of cavitation zones. Therefore, the simulated negative pressures
serve as a clear indicator of where cavitation would likely occur.
A key distinction arises for the detonation wave. Figure 14 shows that at a speciﬁc location,
the pressure recovery following the negative pressure peak is signiﬁcantly more pronounced for
the detonation wave than for the shock wave. Consequently, the negative pressure ﬁeld created
by the converging REW is sustained for a shorter duration. This implies that in a simulation
FIG. 13. Temporal evolution curves of pressure peaks during the interaction between detonation or shock
waves and the droplet.
034303-14

<!-- PDF_PAGE: 15 -->

COMPARATIVE ANALYSIS OF DETONATION AND SHOCK …
FIG. 14. Temporal evolution of the pressure proﬁle along the x axis in second stage.
incorporating the cavitation model, the cavitation zone induced by the detonation wave would have a
signiﬁcantly shorter lifespan than that generated by the shock wave. More speciﬁcally, the cavitation
zone induced by the detonation wave would collapse earlier than that induced by the shock wave.
This difference in cavitation dynamics will be analyzed in detail in the following section.
During the third stage, both planar shock waves and detonation waves undergo successive wave
reﬂections with progressive dissipation of their wave conﬁgurations. As shown in Fig.15,t h ew a v e
conﬁgurations of REW
2 and RSW3 associated with both planar shock waves and detonation waves
exhibit similar characteristics in their evolutionary dynamics in the third stage. However, following
the third stage, signiﬁcant droplet deformation induced by shock interactions becomes evident, with
the droplet’s shape deviating markedly from cylindrical geometry. This substantial morphological
FIG. 15. Detonation wave– and shock wave–droplet interaction: Wave conﬁgurations evolution in third
stage. Density schlieren (upper panel) and pressure contour plots (lower panel). [(a) and (b)] Detonation wave
and [(c) and (d)] shock wave.
034303-15

<!-- PDF_PAGE: 16 -->

ZOU, JIN, CHEN, W ANG, XU, AND W ANG
FIG. 16. Initiation of the cavitation zone. Density schlieren (upper panel) and pressure contour plots (lower
panel). (a) Detonation wave and (b) shock wave.
alteration leads to pronounced differences in subsequent wave system conﬁgurations. Beyond the
third stage, the alternating reﬂections and attenuation of wave systems intensify signiﬁcantly, ren-
dering speciﬁc wave structures indistinguishable in numerical schlieren images. Consequently, this
study conﬁnes its comparative analysis of wave system characteristics to the ﬁrst three evolutionary
stages.
C. Dynamic characteristics of the cavitation zone
This study investigates the dynamic evolution behavior of the cavitation zone induced by the
interaction of the detonation wave and the shock wave with the droplet under phase-transition
coupling conditions. This study comparatively analyzes the complete growth-collapse cycle of the
cavitation zone using the numerical homogeneous cavitation pressure model developed in Sec. III.
We employ numerical simulations to investigate cavitation dynamics in the droplet interacting with
the planar detonation and the shock wave, focusing speciﬁcally on the interplay between phase
transition phenomena and ﬂuid dynamic interactions.
Numerical simulation results demonstrate that the evolution process of the cavitation zone can
be categorized into four distinct stages: initiation of the cavitation zone, complete formation of the
cavitation zone, collapse of the cavitation zone, and ultimate disintegration of the cavitation zone.
During the interaction between detonation or shock waves and the droplet, cavitation inception
occurs at the terminal period of the ﬁrst stage of wave-droplet interaction. As illustrated in Fig. 16,
when the TSW propagates to the leeward surface of the droplet, a REW is generated. The postwave
pressure reduction induced by the expansion wave causes the local pressure to drop below the cavita-
tion threshold (p
limit), triggering liquid phase transition. The density gradient in the phase transition
region becomes signiﬁcantly steeper than that in the nonphase transition region, manifesting as
darker regions in the density schlieren images.
During the propagation of the TSW toward the rear stagnation point, the convergence of leeward-
moving expansion waves induces a further pressure reduction. In a purely liquid model that neglects
phase transition (as discussed in the preceding section), this tension would manifest as numerically
large, nonphysical negative pressures. In contrast, the phase-transition cavitation model used here
captures the physical response: When this intense tension causes the local pressure to drop to the
critical cavitation threshold ( p
limit), the liquid undergoes a phase transition. This process triggers
the formation of a large-scale cavitation zone, as illustrated in Fig. 17. The elliptical structure and
internal density gradients seen in the numerical schlieren images are representative of this newly
formed gas-vapor mixture, which possesses a distinct local density from the surrounding liquid.
The vapor volume fraction contours in Fig. 18 conﬁrm that the liquid undergoes a phase transition
to vapor during the cavitation process. The formation of this low-density vapor region is responsible
for the corresponding shadow area observed in the density schlieren images.
034303-16

<!-- PDF_PAGE: 17 -->

COMPARATIVE ANALYSIS OF DETONATION AND SHOCK …
FIG. 17. Complete formation of the cavitation zone. Density schlieren (upper panel) and pressure contour
plots (lower panel). (a) Detonation wave and (b) shock wave.
When the REW converges and propagates toward the frontal stagnation point, the postwave
pressure increases. Due to energy conversion during the phase-change cavitation process, the
pressure in the cavitation zone of the droplet gradually recovers. Once the vapor-phase pressure
exceeds the local saturated vapor pressure, the phase-change condensation process is triggered.
This triggers vapor condensation within the cavitation zone, where the cavitation zone progressively
diminishes. As shown in Fig. 19, pressure recovery triggers collapse phenomena in both the planar
detonation and shock-induced cavitation zones, with axial bubble length reduction serving as a
key morphological indicator of this process. As shown in Fig. 20, the lifetime of the cavitation
zone induced by the detonation wave is signiﬁcantly shorter than the one generated by the shock
wave. As revealed by the comparative analysis in Figs.19(a) and 19(b), the cavitation zone induced
by the planar detonation wave exhibits signiﬁcantly higher collapse rates, with its axial diameter
undergoing more pronounced reductions within the same time frame, and demonstrates larger aspect
ratios compared with the one generated by the shock wave.
According to the theoretical analysis based on the ZND detonation model, this discrepancy
stems from the weaker negative pressure-sustaining capability of the detonation-induced REW. The
numerical study by Xu et al. [40] demonstrated that the evolution processes of the TSW and the
REW can be equivalently represented as the superposition of compression wavelet envelopes. As the
planar detonation wave propagates, the pressure ﬁeld behind the wave front immediately undergoes
gradual attenuation due to energy dissipation mechanisms. This directly leads to a continuous
decrease in the intensity of compression wavelets contained within the REW, ultimately resulting in
a signiﬁcant reduction of envelope intensity. In contrast, the planar shock wave maintains stable
pressure distribution behind the wave front during propagation. Consequently, the intensity of
compression wavelets in its REW remains relatively constant, with no substantial attenuation in
envelope intensity. The diminished intensity of compression wavelets shortens the low-pressure
FIG. 18. Contour plot of vapor volume fraction. (a) Detonation wave and (b) shock wave.
034303-17

<!-- PDF_PAGE: 18 -->

ZOU, JIN, CHEN, W ANG, XU, AND W ANG
FIG. 19. Collapse of the cavitation zone. Density schlieren (upper panel) and pressure contour plots (lower
panel). (a) Detonation wave and (b) shock wave.
phase maintained by the detonation-induced REW, explaining the accelerated cavitation zone
collapse. It is important to reiterate that, as justiﬁed in Sec. II, thermal conduction is neglected
due to the disparity in timescales. Consequently, the thermal inﬂuence on the cavitation zone is
excluded, and the collapse process is driven exclusively by mechanical effects.
For a planar detonation wave, the attenuation of the postdetonation pressure ﬁeld along the y
direction exhibits less signiﬁcant decay compared with that in the x direction. This pressure distri-
bution reduces energy loss in the compression wavelet along they axis, allowing ﬂow regions farther
from the x axis to maintain long time low-pressure conditions. Under these conditions, the cavitation
collapse rates decrease with increasing y-axis distance. Notably, the cavitation zone farther from the
x axis exhibits signiﬁcantly delayed collapse compared with that near the x axis. This spatially
heterogeneous collapse process leads to elongated bubble morphologies during cavitation.
The sustained collapse of the cavitation zone ultimately leads to disintegration. Based on the
earlier analysis, the cavitation zone induced by planar detonation waves exhibits signiﬁcantly higher
collapse rates in regions proximal to thex axis compared with distal areas. This differential collapse
behavior leads to the phenomenon illustrated in Figs. 21(a) and 21(b): The detonation-induced
cavitation zone undergoes fragmentation prior to complete collapse, splitting into two secondary
bubbles that subsequently collapse in relatively close proximity to the x axis. In contrast, as shown
in Figs. 21(c) and 21(d), the cavitation zone under the planar shock wave retains its intact structure
during collapse due to uniform surrounding pressure distribution, ultimately collapsing straight
along the x axis.
As the cavitation zone collapse intensiﬁes, compression wavelets generated by the collapse-
released energy converge within the droplet’s cavitation core region. This superposition generates
FIG. 20. Temporal variation of vapor volume fraction within the droplet.
034303-18

<!-- PDF_PAGE: 19 -->

COMPARATIVE ANALYSIS OF DETONATION AND SHOCK …
FIG. 21. Ultimate disintegration of the cavitation zone. Density schlieren (upper panel) and pressure
contour plots (lower panel). [(a) and (b)] Detonation wave and [(c) and (d)] shock wave.
intense collapse-induced shock waves. Figure 22(a) demonstrates that the cavitation bubbles in-
duced by a planar detonation wave generate spherical shock waves on both the upper and lower sides
of the x axis due to the deviation of their collapse center. As shown in Fig. 22(b), these two shock
waves propagate towards the frontal stagnation point in a staggered divergent pattern. In contrast,
the collapse center of the cavitation zone generated by a planar shock wave is positioned along the
x axis, forming only a single spherical shock wave that propagates towards the frontal stagnation
point. Notably, during the propagation of the collapsing shock wave, its interaction with the droplet
interface induces expansion waves. Although these expansion waves can trigger localized cavitation
phenomena on the droplet surface, the absence of wave-front convergence conditions prevents the
formation of the cavitation zone.
V . DROPLET DEFORMA TION BEHA VIOR
The preceding section analyzed the evolution of wave conﬁgurations and the cavitation zone
dynamics in the droplet during interactions with the planar detonation and the shock wave.
Building upon these fundamental insights, this section systematically investigates the deformation
mechanisms and breakup processes of the droplet subjected to these two types of shock impacts.
The investigation speciﬁcally reveals how characteristic shock parameters govern the evolutionary
dynamics of droplet morphology. Given the high Weber and Reynolds numbers characteristic of the
initial interaction, the numerical model neglects viscosity and surface tension. Consequently, this
section focuses on the primary breakup regime characterized by macroscopic topological evolution
and instability growth driven by aerodynamic inertial forces. Although this approximation limits
the resolution of microscopic liquid structures, it effectively captures the dominant hydrodynamic
mechanisms. These mechanisms dictate the global fragmentation patterns and reveal the relative
differences between detonation-wave and shock-wave interactions.
034303-19

<!-- PDF_PAGE: 20 -->

ZOU, JIN, CHEN, W ANG, XU, AND W ANG
FIG. 22. The shock wave generated by the cavitation zone collapse. Density schlieren (upper panel) and
pressure contour plots (lower panel). [(a) and (b)] Detonation wave and [(c) and (d)] shock wave.
Figure 23 illustrates the early-stage deformation processes of the droplet under the planar
detonation-wave and the planar shock-wave impacts. As revealed in previous research, the droplet’s
deformation initiates after the completion of the wave conﬁgurations evolution stage; therefore only
the droplet contour is depicted in subsequent illustrations. The comparative analysis demonstrates
FIG. 23. Early-stage deformation process of the droplet subjected to planar detonation-wave and planar
shock-wave impacts. [(a)–(d)] Detonation wave and [(e)–(h)] shock wave.
034303-20

<!-- PDF_PAGE: 21 -->

COMPARATIVE ANALYSIS OF DETONATION AND SHOCK …
marked differences in deformation characteristics between the planar detonation wave and the planar
shock wave.
For the planar detonation wave, the leeward surface of the droplet exhibits distinct planarization
characteristics during deformation. As illustrated in Fig.23(c), the frontal stagnation point maintains
a relatively stable arc curvature, while the rear stagnation point region displays reduced curvature
with ﬂattened structures. Notably, signiﬁcant liquid stripping emerges near the equator of the
droplet.
For the planar shock wave, the deformation process of the droplet exhibits greater intensity
compared with that induced by the planar detonation wave. As illustrated in Fig. 23(f), under the
action of the planar shock wave, the droplet exhibits pronounced contour deformation near the
frontal stagnation point, while maintaining relatively stable curvature at the rear stagnation point.
In contrast to the pronounced ﬂattening exhibited by planar detonation waves, the rear arc surface
maintains its initial curvature with no signiﬁcant ﬂattening. Compared with that in planar detonation
wave interactions, the shock-affected droplet demonstrates signiﬁcant transverse stretching defor-
mation, accompanied by a prominent material migration trend concentrating towards the equator.
The differential effects of the planar detonation wave and the planar shock wave on droplet
breakup morphology arise from marked differences in their postwave ﬂow ﬁeld characteristics. A
primary distinction between the phenomena of planar detonation and shock waves is the downstream
gas velocity. The exothermic reaction inherent to the detonation process leads to a signiﬁcant release
of heat, causing the gas velocity behind the planar detonation front to be considerably lower than
that behind a planar shock wave. This velocity differential directly inﬂuences the Weber number as
shown in TableI. These varying velocity ﬁelds result in disparate vortex structures in the wake of the
droplet, ultimately causing different droplet deformation progressions. To illustrate the signiﬁcant
inﬂuence of the postwave ﬂow velocity and to qualitatively validate the initial deformation process,
a comparison between our simulation and experimental visualizations is presented in Fig. 24.T h i s
ﬁgure shows the droplet’s initial deformation under conditions of different postwave velocities. As
shown in Figs. 24(a) and 24(b), the inﬂuence of velocity is clearly signiﬁcant: Although one case
involves a shock wave and the other a detonation wave, the similar postwave velocities result in
the droplets exhibiting nearly identical ﬂattened structures on their leeward surfaces. In contrast,
in Figs. 24(c) and 24(d) with a much higher postwave velocity (corresponding to a high Weber
number), both experimental and simulation data show the droplet’s windward surface maintaining
its initial curvature with no signiﬁcant ﬂattening. The reasons for this phenomenon are analyzed
below.
The differences in the leeward-side morphology arise from distinct ﬂow separation patterns.
Under the planar detonation-wave action, the postwave ﬂow velocity exhibits a signiﬁcant decline,
leading to substantial expansion of the recirculation zone in the droplet’s rear stagnation region.
This ﬂow characteristic induces the formation of separated vortex structures at the rear stagnation
point. These vortices exert an upward-directed driving force on the droplet through the leeward
surface, promoting material migration toward the equator. The ﬂow ﬁeld near the rear stagnation
point exhibits distinct planar characteristics during this process, in marked contrast to the ﬂow
morphology associated with the planar shock-wave interactions. In the ﬂow ﬁeld dominated by the
shock wave, the ﬂow characteristics exhibit two critical distinctions compared with detonation-wave
scenarios due to negligible velocity attenuation behind the wave front. First, although a recirculation
zone forms on the leeward side of the droplet, the high-speed ﬂow substantially increases the
distance between the recirculation zone and the rear stagnation point. Second, this condition
weakens the inﬂuence intensity of separated vortices on the leeward surface, allowing the droplet
to maintain approximately arc-shaped curvature characteristics on its leeward side during initial
deformation stages. Additionally, as shown in the ﬁgure, when the planar detonation wave and
the planar shock-wave interact with the droplet, the rear stagnation point regions of the droplet
consistently exhibit concave features. This phenomenon indicates that the presence of recirculation
zones induces both ﬂow velocity reduction and pressure elevation in these regions.
034303-21

<!-- PDF_PAGE: 22 -->

ZOU, JIN, CHEN, W ANG, XU, AND W ANG
FIG. 24. Qualitative comparison of droplet interface evolution between the present simulations and exper-
imental results from the literature. (a) Three-dimensional experimental visualization of a water droplet after
shock wave, from Theofanous et al. [48]. (b) Present 2D simulation of a droplet under the planar detonation
wave at a comparable Weber number to (a). (c) Experimental visualization of a water column interacting with
a shock wave, from Sembian et al. [6]. (d) Present 2D simulation of a droplet under the planar shock wave,
corresponding to the regime in (c).
The deformation discrepancy along the spanwise direction of the droplet primarily stems from the
nonuniform distribution of the pressure differential between the windward and leeward surfaces. For
the planar detonation wave, the attenuation characteristics of postwave pressure and ﬂow velocity
lead to a signiﬁcant pressure reduction at both the frontal stagnation point and rear stagnation
point. This ﬂow characteristic results in a diminished pressure differential between the frontal and
rear stagnation points, consequently attenuating the migration driving force directed toward the
equatorial region. Under the planar shock-wave condition, the total pressure of the gas maintains
a high level due to the absence of decay in postshock pressure and ﬂow velocity. The frontal
stagnation point region exhibits a signiﬁcant increase in static pressure due to ﬂow stagnation, while
the presence of a recirculation zone at the rear stagnation point similarly generates a high-pressure
region. This dual high-pressure effect from both stagnation points enhances the droplet’s dynamic
tendency of equatorward migration. It is important to recall the inherent limitations of the 2D model
discussed in Sec. II. Quantitatively, the observed leeward-side ﬂattening is likely accentuated by the
2D approximation. As indicated by the aerodynamic measurements of Park et al. [23], the higher
drag coefﬁcient in 2D geometries implies a lower base pressure in the recirculation zone compared
to 3D spheres. This enhanced pressure differential drives a more pronounced ﬂattening phenomenon
in the simulation. Crucially, since this geometric bias applies systematically to both detonation- and
shock-wave cases, the relative difference in deformation modes identiﬁed in this study remains
valid.
Figure 25 illustrates the late-stage deformation process of a droplet subjected to the planar
detonation wave and the planar shock wave with the image delineating the deformation contours
of the droplet. As illustrated, during the late-stage deformation phase of the droplet, both the planar
detonation wave and the planar shock wave induce signiﬁcant transverse stretching phenomena.
However, distinct differences emerge in the breakup regimes between the windward and leeward
surfaces under these two waves.
034303-22

<!-- PDF_PAGE: 23 -->

COMPARATIVE ANALYSIS OF DETONATION AND SHOCK …
FIG. 25. Late-stage deformation process of the droplet subjected to planar detonation-wave and planar
shock-wave impacts. [(a)–(d)] Detonation wave and [(e)–(h)] shock wave.
Figure 25(d) demonstrates the ﬁnal-stage deformation patterns induced by planar detonation-
wave impingement. The windward interface retains an arc-shaped curvature while developing
near-ﬂat geometries between the equator and the rear stagnation point, with signiﬁcant ﬂattening
evident in the immediate vicinity of the rear stagnation point. Furthermore, the image demonstrates
signiﬁcant spanwise stretching of the droplet during this stage, accompanied by dynamic material
migration toward the equatorial region.
As illustrated in Figs. 25(e)–25(h), the frontal face of the droplet under planar shock-wave inter-
action exhibits prominent interfacial instability characteristics. Distinct shear-induced entrainment
vortices are observed near the frontal stagnation point, accompanied by progressively developing
spanwise tensile deformation. With the expansion of the windward surface area, ﬁlamentary struc-
tures gradually form and subsequently undergo rupture.
Under the action of the planar detonation wave, the formation mechanism of the planar liquid
surface observed between the equator and rear stagnation point of the droplet can be attributed to
the secondary vortex structures generated posterior to the equator. During droplet lateral stretch-
ing, the ﬂow deceleration downstream from the detonation wave induces ﬂow separation both
behind the rear stagnation point and downstream of the equator. This dual separation effect facili-
tates the formation of a shear-induced vortex structure adhering closely to the liquid surface between
the rear stagnation point and the equator. The resultant airﬂow shear force, directed toward the
equator, persistently interacts with the interface, ultimately producing a planar geometric contour.
For the droplet subjected to the planar shock wave, the high-speed ﬂuid impact induces signiﬁcant
lateral deformation of the droplet. The ﬂow separation phenomena in the equator and the rear
stagnation point region merge into a single structure, leading to the formation of a larger-scale
vortex without the generation of secondary vortices. Due to the elevated postshock ﬂow velocity, this
vortex structure is displaced from the rear stagnation point region, resulting in its relatively limited
inﬂuence on the leeward side. The deformation of the leeward side is predominantly governed by
high-speed ﬂuid impact, failing to develop distinct planar structural features.
034303-23

<!-- PDF_PAGE: 24 -->

ZOU, JIN, CHEN, W ANG, XU, AND W ANG
Under the action of the planar shock wave and the planar detonation wave, the interfacial
instability phenomena on the windward side of the droplet exhibit signiﬁcant differences. Under
the planar shock wave, the droplet exhibits characteristic Rayleigh-Taylor instability features ac-
companied by forward jet ﬂow, whereas the one subjected to the planar detonation wave shows no
such interfacial instability phenomena or jetting structures. Under the action of the planar shock
wave, the signiﬁcant increase in gas ﬂow velocity behind the wave induces substantial acceleration
at the gas-liquid interface, triggering Rayleigh-Taylor instability. This phenomenon generates dense
shear-induced entrainment vortex structures within the frontal stagnation point region. These vortex
structures establish local pressure gradient ﬁelds that drive the liquid surface ﬂuid to form forward
jet ﬂow. Under the action of continuous tangential aerodynamic shear forces, the shear-induced
entrainment vortex and jet structures undergo synergistic evolution, resulting in progressive material
stripping from the droplet. This process ultimately triggers substantial breakup and atomization of
the droplet. Under the action of the planar detonation wave, the substantial decrease in postwave
gas ﬂow velocity maintains the acceleration level at the gas-liquid interface within a low range.
This ﬂow ﬁeld characteristic suppresses the signiﬁcant development of Rayleigh-Taylor instability
while leaving the formation mechanism of the forward liquid jet unactivated, consequently resulting
in a less pronounced droplet breakup process compared with the planar shock-wave conditions. It
is crucial to note that the key distinction highlighted by our simulation is a qualitative one: the
presence of this RT-instability-driven jetting under shock-wave conditions versus its suppression
under detonation-wave conditions. While our model correctly captures this fundamental difference
in the initiation of the instability, we acknowledge that the subsequent elongation and breakup of
the jet would be capped by surface tension, a mechanism not included in this study.
VI. CONCLUSIONS
This study presents a detailed comparative analysis of the wave conﬁguration evolution, cavi-
tation dynamics, and droplet deformation characteristics under the planar detonation-wave and the
shock-wave impacts through a multicomponent two-phase compressible ﬂuid numerical framework
integrating a coupled phase transition cavitation model with a two-step chemical reaction mecha-
nism. In the analysis of wave topology, conducted with the phase transition model disabled for the
ease of wave visualization, the study reveals that despite initial structural similarities, the inherent
heat release from detonation leads to distinct postwave pressure attenuation, temperature elevation,
and sound speed variation compared with the inert shock wave. These factors were found to
substantially enhance the propagation velocity of the reﬂected shock wave, a phenomenon explained
mechanistically through a derived analytical relationship. Conversely, with the phase transition
model enabled, the analysis of cavitation dynamics showed that the unique characteristics of the
detonation wave shorten the lifespan of the cavitation zone and induce an asymmetric collapse.
Finally, the droplet deformation analysis, also conducted with the fully coupled numerical model
and validated against experimental observations, uncovers two fundamentally different mechanisms.
Under detonation, the leeward surface of the droplet develops a distinct ﬂattened structure. In
contrast, the shock wave triggers a strong RT instability on the windward surface, leading to the
formation of a forward jet. The core ﬁnding here is the qualitative distinction between the presence
of this RT-instability-driven jetting under shock impact versus its suppression under detonation,
marking a difference in the windward-side breakup mechanism. These disparities elucidate the
critical inﬂuence of combustion exothermicity on shock-droplet interactions, providing theoretical
foundations for droplet atomization mechanisms in rotating detonation engines. The developed
numerical methodology demonstrates precise resolution of interface deformation, wave system
evolution, and phase transition processes, establishing a reliable simulation tool for gas-liquid
two-phase detonation combustion studies. Future investigations should address three-dimensional
effects, multidroplet interactions, and practical fuel droplet characteristics to advance engineering
applications in propulsion systems.
034303-24

<!-- PDF_PAGE: 25 -->

COMPARATIVE ANALYSIS OF DETONATION AND SHOCK …
ACKNOWLEDGMENTS
We acknowledge the support from the National Natural Science Foundation of China (Grant No.
12441201) and the Young Scientists Fund of the National Natural Science Foundation of China
(Grant No. 52306152).
The authors declare that they have no known competing ﬁnancial interests or personal relation-
ships that could have appeared to inﬂuence the work reported in this paper.
DA TA A V AILABILITY
The data that support the ﬁndings of this article are not publicly available upon publication
because it is not technically feasible and/or the cost of preparing, depositing, and hosting the data
would be prohibitive within the terms of this research project. The data are available from the authors
upon reasonable request.
APPENDIX: CALCULA TION OF THE PARTIAL DERIV A TIVES
To simplify the calculation, it is advisable to ﬁrst compute an intermediate variable. The left-hand
side of Eq. (23) can be regarded as a function of Ma1; thus, ∂f (Ma1 )
∂Ma1
can be computed as follows:
∂f (Ma1 )
∂Ma1
= (γ − 1)Ma1
(
γ(Ma1 )2 − γ−1
2
)
− (2γMa1 )
(
1 + γ−1
2 Ma2
1
)
(
γ(Ma1 )2 − γ−1
2
)2
= −Ma1
(
2γ + 1
2 (γ − 1)2)
(
γ(Ma1 )2 − γ−1
2
)2 < 0. (A1)
The partial derivative with respect to u1 is computed as shown below, with u2, c1, and c2 held
constant.
Compute the partial derivative of the left-hand side of Eq. (23) with respect to u1,
∂
∂u1
(Ma2 )2 = 2Ma2
∂Ma2
∂u1
= 2Ma2
c2
∂us
∂u1
. (A2)
Compute the partial derivative of the right-hand side of Eq. (23) with respect to u1,
∂f (Ma1 )
∂u1
= ∂f (Ma1 )
∂Ma1
∂Ma1
∂u1
= ∂f (Ma1 )
∂Ma1
1
c1
(
1 + ∂us
∂u1
)
. (A3)
Setting the left-hand side equal to the right-hand side gives
2Ma2
c2
∂us
∂u1
= ∂f (Ma1 )
∂Ma1
1
c1
(
1 + ∂us
∂u1
)
. (A4)
The partial derivative with respect to u1 is computed from the previous equation as follows:
∂us
∂u1
=
∂f (Ma1 )
∂Ma1
2 c1
c2
Ma2 − ∂f (Ma1 )
∂Ma1
. (A5)
From Eq. (A1), it is easy to know that ∂f (Ma1 )
∂Ma1
< 0, and c1
c2
Ma2 > 0, so ∂us
∂u1
< 0.
034303-25

<!-- PDF_PAGE: 26 -->

ZOU, JIN, CHEN, W ANG, XU, AND W ANG
Using the same method as above, the partial derivatives of us with respect to u2, c1, and c2 can
be obtained,
∂us
∂u2
= 2Ma2
c2
c1
∂f (Ma1 )
∂Ma1
− 2Ma2
< 0, (A6)
∂us
∂c1
=
Ma1
∂f (Ma1 )
∂Ma1
∂f (Ma1 )
∂Ma1
− 2 c1
c2
Ma2
> 0, (A7)
∂us
∂c2
= 2Ma2
2
2Ma2 − c2
c1
∂f (Ma1 )
∂Ma1
> 0. (A8)
The analysis yields the following conclusion:
∂us
∂u1
< 0, ∂us
∂u2
< 0, ∂us
∂c1
> 0, and ∂us
∂c2
> 0. (A9)
[1] B. Wang and J.-P. Wang, Introduction to the special section on recent progress on rotating detonation and
its application, AIAA J. 58, 4974 (2020).
[2] A. K. Hayashi, N. Tsuboi, and E. Dzieminska, Numerical study on JP-10/air detonation and rotating
detonation engine, AIAA J. 58, 5078 (2020).
[3] H. Wen, W. Fan, S. Xu, and B. Wang, Numerical study on droplet evaporation and propagation stability
in normal-temperature two-phase rotating detonation system, Aerosp. Sci. Technol. 138, 108324 (2023).
[4] J. A. Nicholls and A. A. Ranger, Aerodynamic shattering of liquid drops, AIAA J. 7, 285 (1969).
[5] K. Takayama and D. Igra, Investigation of aerodynamic breakup of a cylindrical water droplet, Atomiz.
Sprays 11, 20 (2001).
[6] S. Sembian, M. Liverts, N. Tillmark, and N. Apazidis, Plane shock wave interaction with a cylindrical
water column, Phys. Fluids 28, 056102 (2016).
[7] J. E. Field, J. P. Dear, and J. E. Ogren, The effects of target compliance on liquid drop impact, J. Appl.
Phys. 65, 533 (1989).
[8] D. Igra and K. Takayama, Numerical simulation of shock wave interaction with a water column, Shock
Waves 11, 219 (2001).
[9] W. Wu, G. Xiang, and B. Wang, On high-speed impingement of cylindrical droplets upon solid wall
considering cavitation effects, J. Fluid Mech. 857, 851 (2018).
[10] T. G. Theofanous, G. J. Li, and T. N. Dinh, Aerobreakup in rareﬁed supersonic gas ﬂows, J. Fluids Eng.
126, 516 (2004).
[11] T. G. Theofanous, Aerobreakup of Newtonian and viscoelastic liquids, Annu. Rev. Fluid Mech 43, 661
(2011).
[12] M. Arienti, E. A. Wenzel, D. R. Guildenbecher, and S. J. Beresh, Simulation and analysis of droplet
aerobreakup in a ballistic wave system, AIAA J. 63, 3309 (2025).
[13] K. A. Daniel, D. R. Guildenbecher, P. M. Delgado, G. E. White, S. M. Reardon, H. L. Stauffacher, and S.
J. Beresh, Drop interactions with the conical shock structure generated by a Mach 4.5 projectile,AIAA J.
61, 2347 (2023).
[14] H. Chen, X. Jin, W. Wang, S. Xu, and B. Wang, Investigation on the dynamic characteristics of a droplet
subjected to a divergent shock wave, Phys. Fluids 37, 086159 (2025).
[15] E. K. Dabora, K. W. Ragland, and J. A. Nicholls, Drop-size effects in spray detonations, Symp. (Int.)
Combust. 12, 19 (1969).
[16] R. Yang, Q. Zhang, Q. Xiao, Q. Chen, Y . Jiang, and W. Fan, Breakup characteristics of droplets induced
by detonation waves under different diameters and Mach numbers, Phys. Fluids 37, 016139 (2025).
034303-26

<!-- PDF_PAGE: 27 -->

COMPARATIVE ANALYSIS OF DETONATION AND SHOCK …
[17] S. Salauddin, A. J. Morales, R. Hytovick, R. Burke, V . Malik, J. Patten, S. Schroeder, and K. A. Ahmed,
Detonation and shock-induced breakup characteristics of RP-2 liquid droplets, Shock Waves 33, 191
(2023).
[18] S. Xu, X. Jin, W. Fan, H. Wen, and B. Wang, Numerical investigation on the interaction characteristics
between the gaseous detonation wave and the water droplet, Combust. Flame 269, 113713 (2024).
[19] X. Huang and Z. Lin, Study of the mechanism of shock-induced and detonation-induced droplet breakup
based on hybrid solvers, Phys. Fluids 36, 086102 (2024).
[20] D. Igra and M. Sun, Shock-water column interaction, from initial impact to fragmentation onset, AIAA J.
48, 2763 (2010).
[21] J. C. Meng and T. Colonius, Numerical simulation of the aerobreakup of a water droplet, J. Fluid Mech.
835, 1108 (2018).
[22] G. Xiang and B. Wang, Numerical study of a planar shock interacting with a cylindrical water column
embedded with an air cavity, J. Fluid Mech. 825, 825 (2017).
[23] S.-H. Park, J. Kim, I. Choi, and G. Park, Experimental study of separation behavior of two bodies in
hypersonic ﬂow, Acta Astronaut. 181, 414 (2021).
[24] J. Eggers and E. Villermaux, Physics of liquid jets, Rep. Prog. Phys. 71, 036601 (2008).
[25] H. D. Ng, M. I. Radulescu, A. J. Higgins, N. Nikiforakis, and J. H. S. Lee, Numerical investigation of the
instability for one-dimensional Chapman–Jouguet detonations with chain-branching kinetics, Combust.
Theor. Model. 9, 385 (2005).
[26] J. H. S. Lee, The Detonation Phenomenon (Cambridge University Press, Cambridge, UK, 2008).
[27] G. Allaire, S. Clerc, and S. Kokh, A ﬁve-equation model for the simulation of interfaces between
compressible ﬂuids, J. Comput. Phys. 181, 577 (2002).
[28] E. Johnsen and T. Colonius, Implementation of WENO schemes in compressible multicomponent ﬂow
problems, J. Comput. Phys. 219, 715 (2006).
[29] P. Yang, H. Teng, Z. Jiang, and H. D. Ng, Effects of inﬂow Mach number on oblique detonation initiation
with a two-step induction-reaction kinetic model, Combust. Flame 193, 246 (2018).
[30] R. Saurel, F. Petitpas, and R. Abgrall, Modelling phase transition in metastable liquids: Application to
cavitating and ﬂashing ﬂows, J. Fluid Mech. 607, 313 (2008).
[31] W. Wu, B. Wang, and G. Xiang, Impingement of high-speed cylindrical droplets embedded with an
air/vapour cavity on a rigid wall: Numerical analysis, J. Fluid Mech. 864, 1058 (2019).
[32] S. Xu, X. Jin, H. Chen, W. Fan, H. Wen, and B. Wang, Modelling and simulation on compressible multi-
component gas-liquid ﬂows with chemical reaction and phase transition effects, Aerosp. Sci. Technol.
153, 109451 (2024).
[33] I. Müller and W. H. Müller, Fundamentals of Thermodynamics and Applications (Springer, Berlin, 2009).
[34] A. Zein, M. Hantke, and G. Warnecke, Modeling phase transition for compressible two-phase ﬂows
applied to metastable liquids, J. Comput. Phys. 229, 2964 (2010).
[35] A. Zein, M. Hantke, and G. Warnecke, On the modeling and simulation of a laser-induced cavitation
bubble, Int. J. Numer. Methods Fluids 73, 172 (2013).
[36] G. Strang, On the construction and comparison of difference schemes, SIAM J. Numer. Anal. 5, 506
(1968).
[37] E. Han, M. Hantke, and S. Müller, Efﬁcient and robust relaxation procedures for multi-component
mixtures including phase transition, J. Comput. Phys. 338, 217 (2017).
[38] H. Chen, H. Zou, S. Xu, and B. Wang, Extended theory of generating the cylindrical underwater shock
wave via the stiffened-gas equation of state, Phys. Rev. Fluids 11, 014302 (2026).
[39] A. K. Kapila, R. Menikoff, J. B. Bdzil, S. F. Son, and D. S. Stewart, Two-phase modeling of deﬂagration-
to-detonation transition in granular materials: Reduced equations, Phys. Fluids 13, 3002 (2001).
[40] S. Xu, W. Fan, W. Wu, H. Wen, and B. Wang, Analysis of wave converging phenomena inside the shocked
two-dimensional cylindrical water column, J. Fluid Mech. 964, A12 (2023).
[41] P. Colella, A direct Eulerian MUSCL scheme for gas dynamics,SIAM J. Sci. Stat. Comput.6, 104 (1985).
[42] B. Wang, G. Xiang, and X. Y . Hu, An incremental-stencil WENO reconstruction for simulation of
compressible two-phase ﬂows, Int. J. Multiphase Flow 104, 20 (2018).
034303-27

<!-- PDF_PAGE: 28 -->

ZOU, JIN, CHEN, W ANG, XU, AND W ANG
[43] W. Zhang, N. Fleischmann, S. Adami, and N. A. Adams, A hybrid WENO5IS-THINC reconstruction
scheme for compressible multiphase ﬂows, J. Comput. Phys. 498, 112672 (2024).
[44] F. Xiao, S. Ii, and C. Chen, Revisit to the THINC scheme: A simple algebraic VOF algorithm,J. Comput.
Phys. 230, 7086 (2011).
[45] E. F. Toro, Riemann Solvers and Numerical Methods for Fluid Dynamics (Springer, Berlin, 2013).
[46] S. Gottlieb and C.-W. Shu, Total variation diminishing Runge-Kutta schemes, Math. Comput. 67,7 3
(1998).
[47] A. I. Ruban, J. S. B. Gajjar, A. I. Ruban, and J. S. B. Gajjar, Fluid Dynamics: Part 1: Classical Fluid
Dynamics (Oxford University Press, Oxford, UK, 2014).
[48] T. G. Theofanous, V . V . Mitkin, C. L. Ng, C. H. Chang, X. Deng, and S. Sushchikh, The physics of
aerobreakup. II. Viscous liquids, Phys. Fluids 24, 022104 (2012).
034303-28
