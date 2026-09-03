<!-- PDF_PAGE: 1 -->

Timescales and Statistics of Shock-induced Droplet Breakup
Michael Ullman, 1 Ral Bielawski, 2 and Venkat Raman 1
1Department of Aerospace Engineering, University of Michigan, Ann Arbor, MI, 48109, USA
2Department of Mechanical and Aerospace Engineering,
University of Central Florida, Orlando, FL, 32816, USA
(Dated: April 15, 2025)
Detonation-based propulsion devices, such as rotating detonation engines (RDEs), must be able
to leverage the higher energy densities of liquid fuels in order for them to be utilized in practical
contexts. This necessitates a comprehensive understanding of the physical processes and timescales
that dictate the shock-induced breakup of liquid droplets. These processes are difficult to probe and
quantify experimentally, often limiting measurements to macroscopic properties. Here, fundamental
mechanisms in such interactions are elucidated through detailed numerical simulation of Mach 2
and 3 shock waves interacting with 100 µm water droplets. Using a thermodynamically consistent
two-phase formulation with adaptive mesh refinement, the simulations capture droplet surface in-
stabilities and atomization into secondary droplets in great detail. The results show that droplet
breakup occurs through a coupled multi-stage process, including droplet flattening, formation of
surface instabilities and piercing, and the shedding of secondary droplets from the ligaments of the
deformed primary droplet. When considering the dimensionless timescale of Ranger and Nicholls
(τ), these processes occur at similar rates for the different shock strengths. The PDFs for the Sauter
mean diameters of secondary droplets are bimodal log-normal distributions at τ = 2. Modest dif-
ferences in the degree and rate of liquid mass transfer into droplets less than 5 µm in diameter are
hypothesized to partially derive from differences in droplet surface piercing modes. These results
are illustrative of the complex multi-scale processes driving droplet breakup and have implications
for the ability of shocks to effectively process liquid fuels.
I. INTRODUCTION
Over the last decade, significant research efforts have
focused on the development of detonation-based propul-
sion and power generation technologies, including ro-
tating detonation engines (RDEs) [1, 2], pulse detona-
tion engines (PDEs) [3, 4], linear or reflective detona-
tion engines [5, 6], and oblique detonation wave engines
(ODWEs) [7–9]. While most studies have focused on
gaseous fueling, practical detonation engines must be
able to leverage the higher energy densities of liquid fuels.
Liquid-fueled detonations require that the fuel atomizes,
evaporates, and reacts with the oxidizer prior to reach-
ing the wave-relative sonic plane in order for the resultant
heat release to support the wave propagation. Therefore,
the timescales associated with droplet breakup and evap-
oration are of critical importance.
In practical detonation engines, the initial atomization
of injected fuel jets is driven by shearing with oxidizer
jets. The interaction of the resulting droplet population
with the passing detonation wave then facilitates further
atomization into smaller droplets and may be responsi-
ble for the generation of the vaporized fuel that supports
the detonation itself [10]. Considering that the impact
of the detonation wave plays a key role in the droplet
breakup, several experimental [11–14] and computational
[15–17] studies have considered canonical shock-droplet
interactions, wherein one or more initially stationary liq-
uid droplets interact with a traveling shock wave. For
shock-droplet interactions relevant to detonations, the
Weber numbers are between 10 3 < W e < 105, which
is within the catastrophic breakup [18] or shear-induced
entrainment (SIE) regime [14, 19]. Previous works have
argued that a combination of Kelvin-Helmholtz (KH)
and Rayleigh-Taylor (RT) instabilities drives the breakup
processes in this regime [18, 20], with KH becoming more
dominant with increasing W e [19, 21]. However, other
breakup pathways, such as ballistic-collision-driven evap-
oration, have also been proposed [10].
Because of limitations in spatiotemporal resolution
and optical access, shock- and detonation-driven droplet
breakup processes are difficult to quantify experimentally
and are often limited to macroscopic properties, such as
line-of-sight droplet morphology, population, and lifetime
[13, 14, 22]. To address this gap, high-fidelity simula-
tions can be leveraged to probe the underlying micro-
scale phenomena in greater detail. One common ap-
proach for simulating shock- and detonation-droplet in-
teractions [23–25], as well as full-scale detonation engines
[26–28], is to use Euler-Lagrangian formulations with em-
pirical breakup and evaporation models. However, in or-
der to examine breakup processes themselves, numerical
approaches that capture or track phasic interfaces are
needed. One such interface-capturing approach is the vol-
ume of fluid (VOF) method, which has been widely used
in simulations of droplet breakup in subsonic and mod-
erate W e flows [17, 29–31]. On the other hand, compa-
rable simulations in the catastrophic breakup regime are
sparse [15] and often performed in two dimensions to alle-
viate significant computational cost [16, 32, 33]. Because
of the inherently three-dimensional interface instabilities
and shock structures in practical shock-droplet interac-
tions, simulations that account for this dimensionality
while capturing both the primary and secondary breakup
arXiv:2504.09007v1  [physics.flu-dyn]  11 Apr 2025

<!-- PDF_PAGE: 2 -->

2
processes are needed. Interface-capturing schemes, such
as VOF, are well suited to this task; however, they do
often entail limitations in regard to rates of phase transi-
tion. It is common to assume quasi-instantaneous equi-
libration, where mechanical and thermal equilibrium be-
tween the phases are achieved within a given computa-
tional cell during a simulation time step [15, 16, 34]. In
reality, phase transitions occur at finite rates due to in-
teractions across sharp phasic interfaces. As such, quasi-
instantaneous equilibration routines may lead to artifi-
cially accelerated rates of phase transition if the relevant
equilibrium should take place over more than one simu-
lation time step. This can be crucial for simulations of
liquid-fueled detonations, as the rate of evaporation is a
driving parameter for the system. The accuracy and im-
plications of these equilibrium assumptions actively be-
ing investigated and may be best addressed by molecular
dynamics simulations [10].
Noting these points, this work aims to provide fur-
ther insight into shock-droplet interactions by conduct-
ing three-dimensional VOF-based simulations of Mach 2
(W e = 822) and 3 ( W e = 3760) shock waves interact-
ing with water droplets 100 µm in diameter. Droplet
surface instabilities and secondary breakup are captured
using adaptive mesh refinement. The results detail the
instabilities driving droplet breakup and the subsequent
distributions of atomized droplets.
II. NUMERICAL METHODS
The solver is a multi-phase adaptation of an in-house
compressible reacting flow solver [35], which has been
extensively used to simulate high-speed flows [7, 36–40].
Block-structured adaptive mesh refinement is handled by
the AMReX framework [41]. The phases are treated us-
ing the volume of fluid (VOF) approach, whereαl and αg
respectively denote the volume fractions of the immisci-
ble liquid and gas phases. The gaseous phase is governed
by the ideal gas equation of state, while the liquid phase
is governed by the stiffened gas equation of state. As
such, the phasic energies are given by:
el = p + γlΠl,∞
(γl − 1)ρl
+ e0,l (1)
eg =
Z T
T0
CpdT − pg
ρg
+
NsX
k=1
∆h0
f,k Yk (2)
where γl, Πl,∞, and e0,l are the constant stiffened gas pa-
rameters provided by Schmidmayer et al. [42] and listed
in Table I.
The governing equations were developed by Saurel et
al. [43] and extended by Bielawski et al. [15, 16] to ac-
count for viscous effects and surface tension [44]. The
mass transport of the mixture and phases is governed by
∂αl
∂t + uj
∂αl
∂xj
= Rαl(pl − pg, Tl − Tg) (3)
TABLE I: Stiffened gas parameters.
cv,l γl Πl,∞ e0,l
1479.48 2.82798 8.052 ×108 -1.709 ×107
∂αlρl
∂t + ∂αlρluj
∂xj
= Rρlαl(pl − pg, Tl − Tg) (4)
∂αgρg
∂t + ∂αgρguj
∂xj
= Rρgαg(pl − pg, Tl − Tg) (5)
where the mixture density is given by ρ = αlρl + αgρg.
The conservation equations for momentum and energy
are
∂ρui
∂t + ∂ρuiuj
∂xj
+ ∂αlpl
∂xi
+ ∂αgpg
∂xi
− ∂τij
∂xj
+ ∂Ωij
∂xj
= 0 (6)
∂(ρE + ϵσ)
∂t + ∂ρEu j
∂xj
+ ∂ϵσuj
∂xj
+ ∂puj
∂xj
− ∂τijui
∂xj
− ∂
∂xj

λ ∂T
∂xj

+ ∂uiΩij
∂xj
= RρE(pl − pg, Tl − Tg) (7)
where
ρE = ρlαlel + ρgαgeg + 1
2 ρuiui (8)
τij = µ
 ∂ui
∂xj
+ ∂uj
∂xi

− 2
3 µ ∂uk
∂xk
δij (9)
Ωij = −σ


 ∂c
∂xk
∂c
∂xk
 1
2
δij −
∂c
∂xi
∂c
∂xj

∂c
∂xk
∂c
∂xk
 1
2

 (10)
c = α0.1
l
α0.1
l + (1 − αl)0.1 (11)
The mixture viscosity µ and thermal conductivity λ
are computed using volumetric mixture rules (µ = αlµl+
αgµg; λ = αlλl + αgλg), where the gaseous components
are functions of the thermochemical state and the liquid
components are held constant at values taken from NIST
fluid data at 300 K [45]. The surface tension coefficient
σ is also held constant at the reference value for 300 K.
The species conservation within the gas phase is given
by
∂ρgαgYk
∂t + ∂ujρgαgYk
∂xj
− ∂
∂xj

ρgD ∂Yk
∂xj

− αg ˙ωk
= RρgαgYk(pl − pg, Tl − Tg), k = 1, . . . , Ns (12)
Preprint submitted to Physical Review Fluids

<!-- PDF_PAGE: 3 -->

3
where ˙ωk is the chemical source term for the k-th species.
The relaxation operators R in Eqs. 3-12 are each func-
tions of the pressure ( p) and temperature ( T ) of each of
the phases, which are assumed to be in mechanical and
thermal equilibrium at phasic interfaces. Within each
simulation time step, a relaxation routine is performed
such that the relaxation operators tend toward zero, en-
suring that both phases have identical pressures and tem-
peratures at interfaces. Unlike in previous works with
this solver [15, 46], this relaxation procedure does not
account for phase change. This choice was deliberately
made to more easily account for droplet masses during
breakup. The reader is referred to Ref. [15] for further
details on these relaxation procedures.
The governing equations are solved using a second-
order accurate finite-volume discretization, with the
Harten-Lax-van Leer-Contact (HLLC) scheme being used
for the convective fluxes and central differences being
used for the diffusive fluxes. An explicit two-stage Runge-
Kutta scheme [47] is used for the time integration. In-
terface reconstruction is performed using ρ-THINC [48].
The gas state is handled using the 9 species mechanism
of Mueller et al. [49]. An in-situ post-processing coloring
algorithm, which identifies contiguous regions of liquid, is
used to track droplet number, sizes, and locations. Fur-
ther details on this algorithm and its implementation are
provided in Refs. [15, 16, 50].
III. CASE CONFIGURATIONS
A schematic of the case initialization is provided in
Fig. 1. In both cases, a 100 µm diameter water droplet
is initially suspended in ambient air at 1 atm and 300 K.
The droplet is also initialized at 300 K, but with a pres-
sure that includes the added Laplace pressure of 2 σ/r0.
Upstream of the droplet, the inflow boundary uniformly
supplies air at the analytic post-shock state ( pps, Tps,
Ups) for the desired shock Mach numberMs. This creates
a roughly uniform flow field behind the shock traveling
at the desired speed.
FIG. 1: Schematic of initial and boundary conditions.
The base computational grid has [256 ×64×64], yield-
ing a uniform resolution of 25 µm (0 .25d0). Five AMR
levels are utilized, each of which divides the grid size
along all directions by a factor of 2. This yields a mini-
mum grid resolution of 0.781 µm (0.00781d0). Adaptive
refinement is added using criteria for value and gradi-
ent of the liquid volume fraction ( αl; ∥∇αl|), as well as
the gradient of the mixture pressure ( |∇p|). These allow
the liquid droplets, shocks, and turbulent mixing to be
highly resolved. Due to the tagging of regions exceeding
the αl and ∇αl thresholds, which grow substantially as
the primary droplet atomizes, the maximum cell counts
are roughly 980 million for the Mach 2 shock case and
1.15 billion for the Mach 3 shock case. Prior to significant
atomization, the cell counts for both cases are between
100-200 million. The cell counts then grow steadily with
time as atomization proceeds.
IV. RESULTS
Instantaneous snapshots
Figures 2 and 3 respectively show time sequences of
liquid volume fraction contours colored by temperature
in the Ms = 2 and Ms = 3 cases. Hereafter, time is
expressed using the dimensionless timescale of Ranger
and Nicholls [11], which is useful for comparing breakup
across flow conditions. It is given by
τ = tUr
d0
r ρg
ρl
(13)
where t is the physical time and Ur is the relative speed
between the droplet and the surrounding gas. The rel-
ative speed Ur and gas density ρg are here taken as the
analytic post-shock conditions for the given shock Mach
number Ms. When using this dimensionless time, several
notable similarities can be observed. The shock has fully
traversed the droplet at τ ∼ 0.01, but the droplet has
not yet begun to deform. Waves of surface instabilities
can be seen by τ ∼ 0.275, the formation of which coin-
cide with the flattening of the droplet due to the pressure
gradient across it. The surface instabilities steadily grow,
creating ligaments that start to shed from the primary
droplet surface at τ ∼ 0.38. These ligaments prolifer-
ate and shed small secondary droplets in the wake of the
primary droplet. The growth of the surface instabilities
eventually facilitates the piercing of the windward side
of the droplet at τ ∼ 1. This creates even more complex
ligament structures as the primary droplet begins to shat-
ter, proceeding until τ ∼ 2 when the primary droplet has
largely been atomized into a cloud of secondary droplets.
The deformation and piercing of the droplets can
be seen more clearly in Figs. 4-5, which show two-
dimensional temperature contours along the z-midplane
for the same time sequences. Here, the droplet mor-
phologies are similar to those previously observed in
two-dimensional simulations of shock-droplet interac-
tions [15, 16]. As was seen in Figs. 2-3, secondary lig-
aments and droplets form along the edges of the primary
droplet as it flattens and spreads along its transverse
axes. Differences in the droplet morphologies become
Preprint submitted to Physical Review Fluids

<!-- PDF_PAGE: 4 -->

4
apparent by τ ∼ 1, where the number of surface insta-
bilities on the windward side plays a driving role. The
odd-numbered instabilities in the Ms = 2 case results in a
central spike morphology with surface piercing on either
side of the spike. On the other hand, the even-numbered
instabilities in the Ms = 3 case results in piercing of the
center of the droplet along with the piercing on either
side. This leads to the differences in droplet morphol-
ogy and ligament formation for τ > 1, which may con-
tribute to the differences in secondary droplet formation
discussed in the following subsections.
FIG. 2: Time sequence of liquid volume fraction
contours (αl > 0.1) colored by temperature in the
Ms = 2 case.
Droplet displacement and deformation
Both the droplet acceleration and deformation have
been identified as key parameters influencing the breakup
processes [22, 51, 52]. To quantify these, Fig. 6 shows the
droplet displacement and spreading as a function nondi-
mensional time. The displacement is computed using the
minimum x-coordinate at which liquid is identified, and
the results are compared to the experimental fit of H´ ebert
et al. [52]. The spreading is computed as the maximum
FIG. 3: Time sequence of liquid volume fraction
contours (αl > 0.1) colored by temperature in the
Ms = 3 case.
Preprint submitted to Physical Review Fluids

<!-- PDF_PAGE: 5 -->

5
FIG. 4: Time sequence of z-midplane temperature
contours in the Ms = 2 case. αl = 1 isoline marked in
white.
radial coordinate at which liquid is identified, and the
results are compared to the Burgers and Reinecke mod-
els presented in Ref. [53]. Following H´ ebert et al. [52],
both quantities are computed by considering computa-
tional cells where αl ≥ 0.99. This allows rmax to be
more closely align with the deformation of the contigu-
ous droplet and its ligaments, rather than the spray of
atomized secondary droplets.
The dashed profiles in Fig. 6 show that the droplet
acceleration is similar in both cases up to τ ∼ 1.4, after
which point the profiles begin to diverge. This divergence
may be expected due to the differences in ligament for-
mation and pierced droplet morphology visible in Figs.
4-5. The close agreement between these profiles and the
experimentally-derived empirical fit of H´ ebert et al. [52]
is an encouraging validation of the current simulations
and provides further confirmation that the initial droplet
acceleration is roughly constant with the nondimensional
time τ [15, 54, 55].
The solid profiles in Fig. 6 show that similar droplet
deformation is observed in both cases up to the conclu-
sion of the Ms = 2 simulation at τ ∼ 2. This self-
similarity in droplet deformation for different shock Mach
numbers has been noted in several previous experimen-
tal works [11, 56–58]. The deformation is initially well-
approximated by the Burgers solution for the flattening
of a sphere subjected to a uniformly distributed stag-
FIG. 5: Time sequence of z-midplane temperature
contours in the Ms = 3 case. αl = 1 isoline marked in
white.
FIG. 6: (Left axis; solid lines) Droplet spreading over
time. (Right axis; dashed lines) Droplet displacement
over time.
nation pressure [59]. Once the pierced droplets begin
to fragment at τ ∼ 1.4, the radial spread of the sec-
ondary droplets is better described as an atomized cloud,
rather than a deformed sphere. Correspondingly, the ra-
dial spread more closely matches the steady-state solu-
tion of Reinecke and Walden for a disk-shaped droplet
[53]. These authors found this solution to be in good
Preprint submitted to Physical Review Fluids

<!-- PDF_PAGE: 6 -->

6
agreement with several experiments that measured the
lateral spread of the atomized secondary droplet cloud
[53, 60]. As such, these results provide further experi-
mental validation for the current simulations.
Droplet size distributions
To quantify the breakup processes, droplet size statis-
tics were computed through time. Following the afore-
mentioned coloring algorithm, a “droplet” here refers to
a contiguous region of liquid. Because of the deforma-
tion of these liquid regions, the diameter of a droplet in
this context refers to its Sauter mean diameter computed
from the volume of the liquid region.
FIG. 7: PDFs of droplet diameters versus
nondimensional time. Normalizations for PDFs are
performed for constant τ.
The probability density functions (PDFs) of droplet
diameter through time are plotted in Fig. 7. Here, the
droplet diameter is normalized by the initial diameter d0,
and the PDF is computed independently at each time τ.
As such, integrating the PDFs along the d axis yields 1
for each τ. The sharp discontinuities in the PDFs for the
smallest d occur due to the smallest grid size, which sets
a minimum bound on the resolvable droplet size.
The persistence of the primary droplets can be sliv-
ers of the PDFs at d/d0 = 1 for τ < 0.15. After this,
secondary droplets with diameters 0.3-1% of the initial
droplet diameter remain the most numerous for the re-
mainder of the simulation durations. However, as the
primary droplets are pierced and larger ligaments break
off, larger secondary droplets between 1-10% of d0 be-
come more plentiful. These larger secondary droplets
themselves break apart with time, facilitating a cascade
of secondary droplet formation and the eventual complete
atomization of the primary droplet.
FIG. 8: PDFs of droplet diameters at selected
nondimensional times.
Constant-τ cross-sections of the PDFs in Fig. 7 are
plotted for selected times in Fig. 8. Here, it is seen
that the PDFs of droplet diameter approach bimodal
log-normal distributions over time. One of these peaks,
centered at d/d0 ∼ 0.004, corresponds to the small-
est secondary droplets, while the other peak, centered
at d/d0 ∼ 0.01, corresponds to the medium-sized sec-
ondary droplets that become more prevalent as the pri-
mary droplet is pierced. It is hypothesized that with fur-
ther simulation time, these medium-sized droplets would
atomize further, yielding a unimodal log-normal distribu-
tion for droplet diameter as has been observed in previous
work [15, 16]. The current simulations were terminated
prior to this point due to the growing computational
Preprint submitted to Physical Review Fluids

<!-- PDF_PAGE: 7 -->

7
cost associated with capturing the cloud of secondary
droplets.
Droplet breakup times
The mean normalized droplet diameters over time are
plotted in Fig. 9, with colored bands indicating the range
of 95% of droplet diameters sampled at any given time.
Both cases show notable similarities, including the per-
sistence of the primary droplet up to τ ∼ 0.15 and
means between 0 .006 < d/d 0 < 0.01 for τ > 0.4. Af-
ter τ ∼ 0.8, the mean droplet diameter steadily in-
creases—likely due to increasing numbers of larger sec-
ondary droplets that are shed from the pierced primary
droplet. This counteracts the prevalence of the smallest
secondary droplets, as seen in Figs. 7-8. Notably, in the
time span 0 .15 < τ < 0.4, the mean droplet diameter
drops more quickly in the Ms = 2 case. This indicates
faster formation of small secondary droplets, which may
be due to the more pronounced ligament formation in the
droplet wake (see τ = 0.386 in Figs. 2-3). However, after
τ ∼ 1.3, the mean droplet diameter is consistently lower
in the Ms = 3 case.
FIG. 9: Mean droplet diameters through time for both
cases. Error bars show the bounds for 95% of droplets
at a given time.
The reason for this can be seen in Fig. 10, which shows
the total liquid mass in droplets of varying sizes through
time. As with the PDFs in Fig. 7, the droplet diameters
are grouped into 40 logarithmically-spaced bins, and the
total mass of all droplets within each bin are computed
at each time. Despite the rapid initial formation of small
secondary droplets, which causes the sharp drops in mean
droplet diameter in Fig. 9, nearly all of the liquid mass
is contained within the primary droplet ( d/d0 = 1) prior
to τ ∼ 0.7. This time of limited mass transfer to smaller
droplets has been referred to as the induction time for
the droplet in previous work [15, 16]. Once the piercing
events illustrated in Figs. 2-5 cause the primary droplet
to break apart, accelerated atomization leads to more
substantial transfer of liquid mass into smaller droplets
on the order of 1-10% of the initial droplet diameter.
This atomization occurs more rapidly in the Ms = 3
case, as can be seen by the higher peaks in the contours
for τ > 1.5.
FIG. 10: Distribution of total droplet mass in various
diameter ranges versus nondimensional time.
This transfer of mass into smaller droplets is critical for
liquid-fueled detonations, as their stable propagation re-
quires a sufficient quantity of small fuel droplets that can
evaporate and react with the surrounding oxidizer prior
to the wave-relative sonic plane. The necessary droplet
diameters for this to occur have been estimated as 5-7.5
µm [61]. Following this metric, Fig. 11 shows the frac-
tion of total liquid mass within droplets less than 5 µm
in diameter over time. This fraction can be interpreted
as the degree of atomization of the primary droplet.
As discussed previously, both cases exhibit an induc-
tion time of τ ∼ 0.7, during which nearly all of the liquid
mass is contained within the primary droplet. The degree
of atomization is slightly greater between 0 .7 < τ < 1.5
in the Ms = 2 case, but following the droplet pierc-
ing events at τ ∼ 1.3, the rate of atomization in the
Ms = 3 case increases more substantially. This produces
a greater degree of atomization at τ = 2 in the Ms = 3
case (71%) than in the Ms = 2 case (61%). By τ = 2.25,
90% atomization is achieved in the Ms = 3 case. The
Preprint submitted to Physical Review Fluids

<!-- PDF_PAGE: 8 -->

8
similarities in the slopes of the two profiles for τ > 1.7
indicate similar atomization rates during this time frame.
This suggests that the discrepancies in the degree of at-
omization are attributable to differences in the droplet
breakup between 0 .7 < τ < 1.7. As shown in Figs. 4-5,
this time period corresponds to the piercing of the wind-
ward droplet surface and the fracturing of its ligaments.
Thus, the differences in piercing mode and subsequent
droplet morphology may play a role in the increased at-
omization observed in the Ms = 3 case.
FIG. 11: Total mass in droplets with diameter less than
5 µm normalized by initial droplet mass.
These breakup times are shorter than those typically
observed in experiments of catastrophic droplet breakup.
Measurements of nondimensional breakup times include
4 < τ < 6 from Ranger and Nicholls [11], τ = 3.5 from
Reinecke and Walden [53], τ = 5 .5 from H´ ebert et al.
[52], and 2 < τ < 5 from Schroeder et al. [56]. However,
it is worth noting that the discrepancies observed here
may be partially attributable to the definition of droplet
breakup. In experiments, the breakup time is often de-
fined as the instant at which the droplet or the resultant
atomized spray can no longer be distinguished from the
background gas. While the results indicate that the pri-
mary droplets have largely broken up by τ ∼ 2, Figs. 2
and 3 show that the cloud of secondary droplets can still
appear as a cohesive structure when viewed from the side.
As such, the shorter breakup times reported here may be
due to the definition presented in Fig. 11, which is inac-
cessible with current experimental diagnostics. The dis-
crepancies could also be partly due to the assumption of
quasi-instantaneous thermomechanical equilibrium dis-
cussed in the introduction. Finite rate equilibration that
takes place over several simulation time steps could lead
to a slower deposition of momentum and energy into the
droplet, thereby slowing its breakup processes. Further
investigation with different numerical approaches would
be required to assess these hypotheses.
V. CONCLUSIONS
This work presented three-dimensional simulations of
Mach 2 (W e = 822) and 3 ( W e = 3760) shock waves in-
teracting with 100 µm diameter water droplets. Adaptive
mesh refinement was used in a volume of fluid formu-
lation to highly resolve the droplet surface instabilities
and secondary atomization. The results show that the
breakup processes proceed at similar rates when consid-
ering the nondimensional timescale of Range and Nicholls
[11]. Over τ < 0.5, the droplet begins to flatten due to
the pressure differential across it, and instabilities on the
droplet surface form and grow. These instabilities form
ligaments and secondary droplets that are shed from the
primary droplet, along with facilitating the piercing of
the windward droplet surface at τ > 1. Differences in
the modes of these instabilities lead to different droplet
morphologies—a central spike, as in the Ms = 2 case, or
a central piercing, as in the Ms = 3 case. However, in
both cases, the droplet displacement and radial spread-
ing occur at similar rates with respect to τ. Both quanti-
ties align well with experimentally-derived empirical re-
lations.
By τ = 2, both cases yield bimodal log-normal PDFs
for the secondary droplets’ Sauter mean diameters, with
peaks centered at d/d0 ∼ 0.004 and d/d0 ∼ 0.01. It
is hypothesized that with longer simulation times, the
PDFs would evolve into unimodal log-normal distribu-
tions as the secondary atomization proceeded. While
small secondary droplets quickly dominate the droplet
number density, substantial transfer of liquid mass into
smaller droplets is delayed until after the piercing of the
primary droplet. The transfer of mass into droplets less
than 5 µm in diameter is initially faster in the Ms = 2
case, but is surpassed by the Ms = 3 case for τ > 1.5.
This leads to 61% and 71% atomization by τ = 2 in the
Ms = 2 and Ms = 3 cases, respectively, and roughly 90%
atomization in the Ms = 3 case by τ = 2 .25. Similar
rates of mass transfer to small droplets are observed for
τ > 1.7, suggesting that differences in droplet piercing
mode between 0 .7 < τ < 1.7 may play a role in the in-
creased atomization for Ms = 3. Additional simulations
with different shock strengths and droplet sizes would be
required to further ascertain trends in droplet breakup
speeds. These trends could then be used to tune empiri-
cal models for droplet breakup, which in turn be used in
comparatively inexpensive Euler-Lagrangian simulations
of more complex systems. Together, these simulations of
canonical configurations and full-scale systems can play
a valuable role in the development of novel propulsion
and power generation technologies based on liquid-fueled
detonations.
ACKNOWLEDGMENTS
Support for this research was provided by ONR MURI
N00014-22-1-2606, with Dr. Steven Martens as program
Preprint submitted to Physical Review Fluids

<!-- PDF_PAGE: 9 -->

9
manager. Computational resources were provided by the
United States Department of Defense High-Performance
Computing Modernization Program (DoD HPCMP).
The authors would like to acknowledge the efforts of Shiv-
ank Sharma and Lorenzo Angelilli in developing the mul-
tiphase solver.
[1] V. Raman, S. Prakash, and M. Gamba, Annual Review
of Fluid Mechanics 55 (2022).
[2] V. Anand and E. Gutmark, Progress in Energy and Com-
bustion Science 73, 182 (2019).
[3] K. Kailasanath, AIAA Journal 41, 145 (2003).
[4] P. Wola´ nski, Proceedings of the Combustion Institute34,
125 (2013).
[5] M. Ullman, S. Prakash, D. Jackson, V. Raman,
C. Slabaugh, and J. Bennewitz, Combustion and Flame
257, 113044 (2023).
[6] K. Schwinn, R. Gejji, B. Kan, S. Sardeshmukh, S. Heis-
ter, and C. Slabaugh, Combustion and Flame 193, 384
(2018).
[7] S. Abisleiman, V. Sharma, R. Bielawski, and V. Raman,
Combustion and Flame 274, 113971 (2025).
[8] K. Kailasanath, AIAA Journal 38, 1698 (2000).
[9] R. Dunlap, R. L. Brehm, and J. A. Nicholls, Journal of
Jet Propulsion 28, 451 (1958).
[10] N. Kateris, E. S. Genter, and H. Wang, in 29th Inter-
national Colloquium on the Dynamics of Explosions and
Reactive Systems (2023).
[11] J. A. Nicholls and A. Ranger, AIAA Journal 7, 285
(1969).
[12] V. Duke-Walker, B. J. Musick, and J. A. McFarland,
International Journal of Multiphase Flow 161, 104389
(2023).
[13] S. Salauddin, A. Morales, R. Hytovick, R. Burke, V. Ma-
lik, J. Patten, S. Schroeder, and K. Ahmed, Shock Waves
33, 191 (2023).
[14] S. Sharma, A. P. Singh, S. S. Rao, A. Kumar, and
S. Basu, Journal of Fluid Mechanics 929, A27 (2021).
[15] R. Bielawski, Shock and Detonation Driven Breakup of
Liquid Droplets , Ph.D. thesis, University of Michigan
(2024).
[16] R. Bielawski and V. Raman, in AIAA SciTech 2024 Fo-
rum (2024) p. 1639.
[17] B. Dorschner, L. Biasiori-Poulanges, K. Schmidmayer,
H. El-Rabii, and T. Colonius, Journal of Fluid Mechanics
904, A20 (2020).
[18] M. Pilch and C. Erdman, International Journal of Mul-
tiphase Flow 13, 741 (1987).
[19] T. Theofanous and G. Li, Physics of Fluids 20 (2008).
[20] D. Guildenbecher, C. L´ opez-Rivera, and P. Sojka, Exper-
iments in Fluids 46, 371 (2009).
[21] T. Theofanous, V. Mitkin, C. Ng, C. Chang, X. Deng,
and S. Sushchikh, Physics of Fluids 24 (2012).
[22] J. Burr, M. Maybee, B. Bigler, S. Beard, P. Rugel,
R. Dave, A. Kastengren, and J. Bennewitz, ILASS-
AMERICAS 2024 (2024).
[23] B. J. Musick, M. Paudel, P. K. Ramaprabhu, and J. A.
McFarland, Combustion and Flame 257, 113035 (2023).
[24] S. S. Dammati, A. Poludnenko, N. Kateris, W. Dong,
H. Wang, and T. Lu, in AIAA SciTech 2025 Forum
(2025) p. 0388.
[25] A. Batista, M. Ross, C. Lietz, J. R. Burr, and J. W.
Bennewitz, in AIAA SciTech 2023 Forum (2023) p. 0562.
[26] S. Prakash, R. Bielawski, V. Raman, K. Ahmed, and
J. Bennewitz, Combustion and Flame 259, 113097
(2024).
[27] Q. Meng, M. Zhao, H. Zheng, and H. Zhang, Fuel 290,
119808 (2021).
[28] J. Wang, W. Lin, W. Huang, Q. Shi, and J. Zhao, Applied
Thermal Engineering 203, 117920 (2022).
[29] M. Jain, R. S. Prakash, G. Tomar, and R. Ravikrishna,
Proceedings of the Royal Society A: Mathematical, Phys-
ical and Engineering Sciences 471, 20140930 (2015).
[30] G. Strotos, I. Malgarinos, N. Nikolopoulos, and
M. Gavaises, International Journal of Multiphase Flow
85, 96 (2016).
[31] S. V. Poplavski, A. V. Minakov, A. A. Shebeleva, and
V. M. Boyko, International Journal of Multiphase Flow
127, 103273 (2020).
[32] P. Tarey, P. Ramaprabhu, and J. McFarland, in AIAA
SciTech 2024 Forum (2024) p. 2237.
[33] N. Srinivasan and S. Yang, in AIAA SciTech 2025 Forum
(2025) p. 1173.
[34] M. B. Kuhn and O. Desjardins, International Journal of
Multiphase Flow 156, 104195 (2022).
[35] S. Sharma, R. Bielawski, O. Gibson, S. Zhang,
V. Sharma, A. H. Rauch, J. Singh, S. Abisleiman,
M. Ullman, S. Barwey, and V. Raman, arXiv preprint
arXiv:2412.00900 (2024).
[36] M. Ullman, S. Prakash, S. Barwey, and V. Raman, Com-
bustion and Flame 264, 113427 (2024).
[37] M. Ullman and V. Raman, Applications in Energy and
Combustion Science 20, 100289 (2024).
[38] S. Sharma, R. Bielawski, A. H. Rauch, and V. Raman,
in AIAA SciTech 2024 Forum (2024) p. 2596.
[39] S. Sharma, J. Singh, L. Angelilli, and V. Raman, Pro-
ceedings of the Combustion Institute 40, 105295 (2024).
[40] A. H. Rauch, M. J. Ullman, S. Sharma, R. Bielawski,
V. Raman, C. E. Dedic, A. J. Metro, and R. D. Rockwell,
in AIAA SciTech 2024 Forum (2024) p. 2593.
[41] W. Zhang, A. Almgren, V. Beckner, J. Bell, J. Blaschke,
C. Chan, M. Day, B. Friesen, K. Gott, D. Graves,
M. Katz, A. Myers, T. Nguyen, A. Nonaka, M. Rosso,
S. Williams, and M. Zingale, Journal of Open Source
Software 4, 1370 (2019).
[42] K. Schmidmayer, F. Petitpas, S. Le Martelot, and
´E. Daniel, Computer Physics Communications 251,
107093 (2020).
[43] R. Saurel, F. Petitpas, and R. A. Berry, Journal of Com-
putational Physics 228, 1678 (2009).
[44] K. Schmidmayer, F. Petitpas, E. Daniel, N. Favrie, and
S. Gavrilyuk, Journal of Computational Physics334, 468
(2017).
[45] National Institute of Standards and Technology, Thermo-
physical properties of fluid systems, https://webbook.
nist.gov/chemistry/fluid/ (2023).
[46] S. Sharma, R. Bielawski, and V. Raman, in AIAA
SciTech 2025 Forum (2025) p. 1582.
[47] S. Gottlieb and C.-W. Shu, Mathematics of Computation
Preprint submitted to Physical Review Fluids

<!-- PDF_PAGE: 10 -->

10
67, 73 (1998).
[48] D. P. Garrick, W. A. Hagen, and J. D. Regele, Journal
of Computational Physics 344, 260 (2017).
[49] M. Mueller, T. Kim, R. Yetter, and F. Dryer, Interna-
tional Journal of Chemical Kinetics 31, 113 (1999).
[50] M. Heinrich and R. Schwarze, SoftwareX 11, 100483
(2020).
[51] M. Pilch, Acceleration induced fragmentation of liquid
drops, Ph.D. thesis, University of Virginia (1981).
[52] D. H´ ebert, J.-L. Rullier, J.-M. Chevalier, I. Bertron,
E. Lescoute, F. Virot, and H. El-Rabii, SN Applied Sci-
ences 2, 1 (2020).
[53] W. Reinecke and G. Waldman, in 13th Aerospace Sci-
ences Meeting (1975) p. 152.
[54] K. Mizuno, T. Yada, T. Kamiya, M. Asahara, and
T. Miyasaka, International Journal of Multiphase Flow
155, 104141 (2022).
[55] J. Meng and T. Colonius, Shock Waves 25, 399 (2015).
[56] S. Schroeder, S. Salauddin, A. Morales, M. Moran,
R. Hytovick, E. Rigney, and K. Ahmed, Proceedings of
the Combustion Institute 40, 105338 (2024).
[57] W. Reinecke and W. McKay, Experiments on water drop
breakup behind Mach 3 to 12 shocks , Tech. Rep. (Avco
Government Products Group, 1969) sC-CR-70-6063.
[58] A. Wierzba and K. Takayama, AIAA Journal 26, 1329
(1988).
[59] O. G. Engel, Journal of Research of the National Bureau
of Standards 60, 19 (1958).
[60] W. Reinecke and G. Waldman, A study of drop breakup
behind strong shocks with applications to flight , Tech.
Rep. (AVCO Government Products Group, 1970) aVSD-
0110-70-77.
[61] D. A. Schwer, E. O’Fallon Jr, and D. Kessler, Liquid-
fueled detonation modeling at the US Naval Research Lab-
oratory, Tech. Rep. (Naval Research Laboratory, 2018).
Preprint submitted to Physical Review Fluids
