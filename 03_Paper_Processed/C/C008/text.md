<!-- PDF_PAGE: 1 -->

Shock Waves (2015) 25:399–414
DOI 10.1007/s00193-014-0546-z
ORIGINAL ARTICLE
Numerical simulations of the early stages of high-speed droplet
breakup
J. C. Meng · T. Colonius
Received: 10 March 2014 / Revised: 9 June 2014 / Accepted: 28 November 2014 / Published online: 20 December 2014
© Springer-Verlag Berlin Heidelberg 2014
Abstract Experiments reported in the literature are repro-
duced using numerical simulations to investigate the early
stages of the breakup of water cylinders in the ﬂow behind
normal shocks. Qualitative features of breakup observed in
the numerical results, such as the initial streamwise ﬂatten-
ing of the cylinder and the formation of tips at its periph-
ery, support previous experimental observations of stripping
breakup. Additionally, the presence of a transitory recircula-
tion region at the cylinder’s equator and a persistent upstream
jet in the wake is noted and discussed. Within the uncertain-
ties inherent to the different methods used to extract mea-
surements from experimental and numerical results, com-
parisons with experimental data of various cylinder defor-
mation metrics show good agreement. To study the effects of
the transition between subsonic and supersonic post-shock
ﬂow, we extend the range of incident shock Mach numbers
beyond those investigated by the experiments. Supersonic
post-shock ﬂow velocities are not observed to signiﬁcantly
alter the cylinder’s behavior, i.e., we are able to effectively
collapse the drift, acceleration, and drag curves for all simu-
lated shock Mach numbers. Using a new method that mini-
mizes noise errors, the cylinder’s acceleration is calculated;
acceleration curves for all shock Mach numbers are subse-
quently collapsed by scaling with the pressure ratio across
the incident shock. Furthermore, we ﬁnd that accounting for
the cylinder’s deformed diameter in the calculation of its
Communicated by R. Bonazza.
This paper is based on work that was presented at the 29th
International Symposium on Shock Waves, Madison, Wisconsin,
USA, July 14–19, 2013.
J. C. Meng (B) · T. Colonius
California Institute of Technology, 1200 E. California Blvd., Pasadena,
CA 91125, USA
e-mail: jomela.meng@caltech.edu
unsteady drag coefﬁcient allows the drag coefﬁcient to be
approximated as a constant over the initial breakup period.
Keywords Breakup · Deformation · Droplet · Shock–
cylinder interaction · Stripping · Unsteady drag coefﬁcient
1 Introduction
The study of droplet breakup has applications in the combus-
tion and detonation of multiphase mixtures, liquid jet atom-
ization, and rain erosion damage. The primary motivation for
the current work lies in geothermal waste heat recovery appli-
cations. Within variable phase turbines (VPTs), multiphase
nozzles are used to ﬂash evaporate and accelerate the work-
ing ﬂuid into a high-speed two-phase jet composed mainly
of gas with disperse liquid droplets. Experimental testing has
shown that larger droplets tend to coalesce on the rotor blades
to form a thin ﬁlm that adversely impacts momentum trans-
fer from droplet impacts [ 44]. On the other hand, smaller
droplets are more likely to run off the rotor blade, while
still imparting momentum during impact. A more complete
understanding of the breakup process within the multiphase
nozzle, so as to predict a ﬁnal droplet size distribution, would
allow for optimized nozzle design.
Much of the earlier literature on droplet breakup consists
of experimental work performed in shock tubes and wind tun-
nels. Normal shock waves, by themselves, have little effect on
the droplet. However, they have proven to be a reliable and
repeatable technique to generate a high-speed ﬂow around
the droplet, which is responsible for the deformation and
disintegration [12,31]. Earlier studies focused on droplets of
Newtonian ﬂuids in subsonic streams, and attempted to char-
acterize various breakup modes and mechanisms [ 6,12,15–
17,25,31,32]. Breakup has, classically, been separated into
123

<!-- PDF_PAGE: 2 -->

400 J. C. Meng, T. Colonius
ﬁve distinct regimes (delineated by the Weber number,We ):
vibrational, bag, bag-and-stamen, shear or sheet stripping,
and catastrophic. Descriptions of each regime and their cor-
responding Weber numbers can be found in the reviews of
Pilch and Erdman [ 28] and Guildenbecher et al. [ 9]. More
recently, Theofanous and Li [39] proposed a re-classiﬁcation
into two primary breakup regimes: Rayleigh–Taylor piercing
and shear-induced entrainment. In this new classiﬁcation, the
shear-induced entrainment regime is the terminal regime for
We > 10
3. The classical catastrophic regime was argued
to be an artifact of low-resolution shadowgraph visualiza-
tions [39]. Earlier experimental studies noted the formation
of a mist or spray in the wake of the disintegrating droplet
[31–33]. In her investigation, Engel [ 6] concluded that the
most likely explanation was a combination of breaking wave
crests at the droplet’s equator and the stripping of water by
vortices in the airﬂow. In addition to varying droplet size and
shock Mach number, M
S,[ 6], studies have also calculated
characteristic breakup times [7,15,31,32], and attempted to
quantify the dependence of breakup on parameters such as
the density and viscosity ratios of the ﬂuids [7,12,14,15,40].
Historically, the drag of a deforming droplet has been a
quantity of keen interest for numerous applications. Vari-
ous attempts have been made to determine accurate droplet
velocities and accelerations. Experimental studies often ﬁt a
polynomial to the drift measurements from their visualiza-
tions, and then differentiate to approximate the acceleration
[6,24,31,33,36,37]. Empirical correlations exist in the lit-
erature to predict the drag coefﬁcient of a droplet based on
various non-dimensional groupings (commonly, the Weber,
Ohnesorge, Oh , and Reynolds, Re, numbers) [26].
Due to the high computational cost of three-dimensional
simulations, numerical droplet breakup studies often invoke
two-dimensional [ 3,18–20] or axisymmetric [ 1,10,11]
approximations. Quan and Schmidt [29] studied breakup for
incompressible ﬂuids using three-dimensional simulations.
Their computations were initialized by ﬁrst simulating ﬂow
over a solid sphere. The steady-state velocity ﬁeld around the
sphere was then used as the initial ﬂow condition around the
droplet. The axisymmetric simulations [1,10,11]a l s os o l v e d
the incompressible Navier–Stokes equations, and initialized
droplet breakup by subjecting the droplet to either a body
force [ 10] or a step change to a divergence-free velocity
ﬁeld [1,11]. The two-dimensional simulations of Igra and
Takayama [18–20] were limited by their numerical method,
which was suitable only for the very early stages of breakup,
and could not capture the majority of the deformation and
breakup. The two-dimensional numerical work of Chen [ 3]
also tried to duplicate the experiments of Igra and Takayama.
The simulation results therein provide a, albeit limited, basis
of comparison for the present work.
The goals of the present work are to perform high-ﬁdelity
simulations of the breakup of a water column in the ﬂow
behind a normal shock wave to understand the ﬂow fea-
tures associated with breakup, and extract accurate mea-
surements of the cylinder’s acceleration and unsteady drag
coefﬁcient. Solving the multicomponent, compressible Euler
equations allows our simulations to match the experimental
setup of Igra and Takayama [ 20], and comparisons can be
made with their data. We are also able to accurately calcu-
late the cylinder’s center-of-mass velocity, acceleration, and
unsteady drag coefﬁcient. The present work is organized as
follows. In Sect.2, we present the physical model and relevant
simulation ﬂow parameters. Section 3 brieﬂy describes the
employed numerical method and the calculation of various
ﬂow quantities used in the analysis. Analysis of the compu-
tational results and a discussion of their implications follows
in Sect. 4. The major conclusions are summarized in Sect.5.
2 Physical modeling
2.1 Problem description
Droplet breakup is studied in two dimensions by simulating
the breakup of a water cylinder in the high-speed ﬂow behind
a normal shock wave. We initially focus on the experiments
of Igra and Takayama [ 20], and then extend the range of
simulated shock Mach numbers to include supersonic post-
shock gas velocities. The values of incident shock Mach num-
bers and their corresponding post-shock Mach numbers,M
2,
are shown in Table 1. The Weber and Reynolds numbers,
respectively, characterize the relative importance of inertial-
to-capillary and inertial-to-viscous forces:
We =
ρg u2
g d0
σ , (1)
Re = ρg ug d0
μg
, (2)
where the density, ρg, and velocity, ug, are those of the
shocked gas, σ is the surface tension coefﬁcient, μg is the
dynamic viscosity of the gas, and the characteristic length
scale is the initial cylinder diameter, d
0. Using the experi-
Table 1 Post-shock Mach numbers, M2, in the shock-stationary (SS)
and shock-moving (SM) reference frames
MS M2 (SS) M2 (SM)
1.18 0 .8549 0 .2625
1.30 0 .7860 0 .4056
1.47 0 .7120 0 .5775
1.73 0 .6330 0 .7885
2.00 0 .5774 0 .9622
2.50 0 .5130 1 .1970
123

<!-- PDF_PAGE: 3 -->

Numerical simulations of the early stages 401
r0x
y
23d0
6d0 Planar shock
Fig. 1 Computational domain setup
mental parameters for a water cylinder in air, the approximate
Weber numbers corresponding to the four weaker shocks
range between 940–19,300. The Reynolds numbers corre-
sponding to the same shock Mach numbers range between
39,900 and 237,600. These Weber and Reynolds numbers
suggest that the physical mechanisms of breakup are pri-
marily driven by inertia, and that a reasonable ﬁrst approx-
imation can be made by neglecting the effects of surface
tension and viscosity. With these simpliﬁcations, we do not
capture all the physics of the breakup process. For example,
the absence of surface tension restricts our capability to sim-
ulate the breakup of the thin liquid ﬁlaments that are stripped
off the edge of the cylinder. However, for the early stages
of breakup where the cylinder remains, for the most part, a
coherent body, the roles of viscosity and surface tension are
expected to be relatively minor compared to that of inertia.
Future work will restore these physical effects back into the
model.
The breakup of the water cylinder is simulated using the
computational setup shown in Fig. 1. In addition to the lim-
itations imposed by the absence of viscous and capillary
effects, our analysis is also restricted to the early stages of
breakup since the ﬂow is assumed to be symmetric across
the cylinder’s centerline. Experimental visualizations of both
cylinder and droplet breakup show no signiﬁcant asymme-
tries during the early stages of breakup. We employ a sym-
metric boundary condition along the bottom of the com-
putational domain, and enforce non-reﬂecting characteris-
tic boundary conditions along the three remaining bound-
aries. Implemented following Thompson [41,42], these char-
acteristic boundary conditions do not contaminate the solu-
tion through the reﬂection of outgoing waves. The water
cylinder and the air in front of the planar shock are ini-
tially at rest ( ρ
g = 1.204 kg/m3,ρl = 1,000 kg/m3, and
pg = pl = 1 atm). At the start of the simulation, the shock
is set in motion towards the water cylinder and establishes a
steady freestream ﬂow ﬁeld.
2.2 Equations of motion
In the absence of surface tension and viscosity, the ﬂow is
governed by the multicomponent, compressible Euler equa-
tions. In addition to being compressible and inviscid, each
ﬂuid is considered immiscible and does not undergo phase
change. In the absence of mass transfer and surface tension,
material interfaces are simply advected by the local ﬂow
velocity. Following the ﬁve-equation model of Allaire et al.
[2], interfaces are modeled using volume fractions, α.T h e
governing equations consist of two continuity equations, (3)
and (4), a mixture momentum equation, (5), a mixture energy
equation, (6), and a volume fraction advection equation, (7).
∂(α
gρg)
∂t +∇· (αgρg u) = 0, (3)
∂(αlρl)
∂t +∇· (αlρl u) = 0, (4)
∂(ρu)
∂t +∇· (ρu ⊗ u + pI) = 0, (5)
∂E
∂t +∇·
[
(E + p)u
]
= 0, (6)
∂αg
∂t + u ·∇ αg = 0, (7)
where the subscripts l and g denote, respectively, the liquid
and gas phases. Since phasic continuity equations are solved,
individual ﬂuid masses (and, therefore, total mass) are con-
served by the numerical method. As a consequence of the
shock-capturing nature of the numerical scheme, interfaces
are diffuse (smeared over several grid cells) and a smooth
transition of volume fractions exists in a mixture region
between the two constitutive ﬂuids. These mixture regions
are not indicative of molecular mixing (since the component
ﬂuids are immiscible), but are inherently unphysical and an
artifact of numerical diffusion. The interface model of Allaire
et al. [2] tends to the Euler equations in each of the pure ﬂu-
ids, and recovers the correct sharp interface properties in the
limit of inﬁnite grid resolution.
Non-dimensionalization of all physical ﬂow variables is
accomplished using the original cylinder diameter, and the
nominal density and sound speed of water (c
l = 1,450 m/s).
Time is non-dimensionalized using a scaling, found in
the literature, characteristic of breakup by Rayleigh–Taylor
or Kelvin–Helmholtz instabilities [28,31,33]. The resultant
non-dimensional time is given by
t∗ = t ug
d0
√ρg
ρl
, (8)
where t is the dimensional time, and the gas velocity,ug, and
ﬂuid densities, ρg and ρl , refer to post-shock conditions.
2.3 Equation of state
The stiffened gas equation of state [ 13]i su s e dt oc l o s et h e
system of equations, and models both gases and liquids in
the ﬂow solver.
123

<!-- PDF_PAGE: 4 -->

402 J. C. Meng, T. Colonius
Γ p + /Pi1∞ = E − 1
2ρu · u, (9)
where
Γ = 1
γ − 1 =
2∑
i=1
αi
( 1
γi − 1
)
, (10)
and
Π∞ = γP∞
γ − 1 =
2∑
i=1
αi
( γi P∞ ,i
γi − 1
)
, (11)
are the mixture properties in the diffuse interface region [2].
For air, γ = 1.4 is the ratio of speciﬁc heats, P∞ = 0, and
the stiffened gas equation of state reduces to the ideal gas
equation. The parametersγ and P∞ for water are empirically
determined from shock Hugoniot data. Following Gojani et
al. [8], the properties for water are taken to beγ = 6.12 and
P
∞ = 343.44 MPa.
3 Numerical methods
3.1 Spatial and temporal discretization
The numerical method is based on the work of Johnsen and
Colonius [23], which was shown to be both interface- and
shock-capturing. The original work has since been extended
to three dimensions and includes the effects of viscosity and
nonuniform grids [5]; it has been used to model the shock-
induced collapse of bubbles [4]. Veriﬁcation of the algorithm
via benchmark test cases (e.g., isolated interface advection,
shock–interface interaction, gas–liquid Riemann problem)
is shown by Coralic and Colonius [5] and is not reproduced
here.
The numerical method is based on a ﬁnite-volume
framework. Spatial reconstruction is accomplished with a
third-order, weighted, essentially non-oscillatory (WENO)
scheme coupled with the Harten–Lax–van Leer Contact
(HLLC) approximate Riemann solver [43]. The equations are
advanced in time using a total-variation-diminishing (TVD)
Runge–Kutta scheme. Since the time marching scheme is
explicit, the time step is chosen to limit the Courant–
Friedrichs–Lewy (CFL) condition to CFL ≈ 0.25. For the
production runs, a Cartesian grid of 1 ,200 × 600 cells is
stretched near the boundaries using a hyperbolic tangent
function. The most reﬁned portion of the grid is located near
the initial position of the cylinder and in the region of the
near-ﬁeld wake. In this region, the nominal grid resolution is
100 cells per cylinder diameter. The numerical diffusion of
an initially discontinuous interface can result in unphysical
mixture regions that are particularly vulnerable to computa-
tional failure and affect code stability. Therefore, in order to
avoid such a discontinuous interface, a smoothing function
is applied to the cylindrical geometry as it is initially laid out
on the Cartesian grid.
Without the presence of molecular viscosity to regular-
ize the smallest scales, ever ﬁner ﬂow features are obtained
in the simulation as spatial resolution is improved. There-
fore, traditional grid convergence or independence of the
computational results cannot be deﬁnitively shown; this is
a known issue associated with “inviscid” calculations using
shock- and interface-capturing methods. A grid resolution
study doubling the number of cells in each direction, while
resolving ﬁner ﬂow features, showed little difference in mea-
surements of cylinder deformation and center-of-mass prop-
erties. Further details of this study can be found in Appendix
A. We believe that the present spatial resolution is able to
capture the salient features in the ﬂow without being compu-
tationally cumbersome.
3.2 Numerical viscosity
Since our numerical method is both shock- and interface-
capturing, numerical viscosity is present in the simulation.
Preliminary viscous simulations have been performed in an
attempt to ﬁnd an approximate lower bound for the “appar-
ent” Reynolds number corresponding to the numerical vis-
cosity associated with the present 1 ,200 × 600 grid resolu-
tion. A description of the implementation of viscosity into
our solver can be found in Coralic and Colonius [5], which is
based on the work of Perigaud and Saurel [27]. Our approach
involved running a series of viscous simulations, holding grid
resolution constant, while successively decreasing Reynolds
numbers. At a critical Reynolds number, Re
c, the molecular
viscosity becomes sufﬁcient to inﬂuence the ﬂow physics,
and causes a signiﬁcant deviation from the “inviscid” sim-
ulation results. The analysis is complicated by the fact that
physical ﬂow quantities exhibit varying degrees of sensitiv-
ity to changes in viscosity. For brevity, only representative
results are shown here. Figures 2 and 3 show the results
of a series of runs, at the same 1 ,200 × 600 grid resolu-
tion, varying the Reynolds number between Re = 15 and
Re = 5,000. Note that time and energy in both ﬁgures
have been non-dimensionalized using the original cylinder
diameter, and the nominal density and sound speed of water.
As the incident shock wave moves through the domain, the
energy increases in a linear manner. When the shock exits,
at a non-dimensional time of approximately 50, the energy
in the domain begins to slowly decrease due to a net ﬂux of
energy out of the domain. In Fig.2, the curves for Re ≥ 500
match the inviscid curve indicating that the magnitude of the
molecular viscosity is less than that of the numerical vis-
cosity, which is responsible for the behavior of the curves.
123

<!-- PDF_PAGE: 5 -->

Numerical simulations of the early stages 403
4.5
5.0
5.5
6.0
6.5
7.0
7.5
40 60 80 100 120 140 160
Domain kinetic energy [10− 3]
Non-dimensional time
Inviscid
Re = 15
Re = 75
Re = 150
Re = 500
Re = 3000
Re = 5000
Fig. 2 Kinetic energy in the domain as a function of Reynolds number
0.160
0.162
0.164
0.166
0.168
0.170
0.172
0.174
0.176
0.178
40 60 80 100 120 140 160
Domain total energy
Non-dimensional time
Inviscid
Re = 15
Re = 150
Re = 500
Re = 3000
Fig. 3 Total energy in the domain as a function of Reynolds number
For Reynolds numbers 15 < Re < 150, the magnitude of
the molecular viscosity surpasses that of numerical viscosity,
and changes the overall behavior of the curves. In Fig. 3,a
smaller range of values for the Reynolds number is plotted,
but it can be seen that the curves for Re ≥ 500 are almost
indistinguishable from the inviscid curve. Based on these
viscous simulations, the apparent Reynolds number associ-
ated with the numerical viscosity is believed to be no less
than Re
c = 500 at the level of resolution used in the present
results. For a Mach 1.47 shock wave, this corresponds to a
physical droplet diameter of approximately 18 µm.
3.3 Center-of-mass calculations
The accurate calculation of the cylinder’s center-of-mass
acceleration is a necessary step towards estimating the
cylinder’s unsteady drag. Experimental studies have often
extracted acceleration data by differentiating a polynomial
ﬁt of the cylinder’s trajectory. The measurement of the cylin-
der’s drift from the forward stagnation point is often a neces-
sary simpliﬁcation for extracting meaningful data from pho-
tographic evidence, and has been used in previous experi-
mental work [6,33]. However, acceleration calculations fol-
lowing this methodology are subject to additional error since
the drift of the cylinder front does not accurately represent the
center-of-mass drift. As noted by Theofanous [38] and shown
in our results, the leading edge drift ﬁrst overestimates, then
underestimates, the center-of-mass drift.
In our results, the location of the center of mass (denoted
by an overbar) of the deforming cylinder is calculated using
¯x =
∫
α
lρl x dV∫
αlρl dV , (12)
where the integrated volume (area in 2D) is that of the entire
computational domain. The liquid partial density, αlρl ,i n
(12) is then the parameter that restricts the integration to cells
with non-zero liquid volume fractions. Once the center-of-
mass location is calculated, a few options exist for calculating
the velocity and acceleration. Perhaps the simplest method
is to differentiate the discrete displacement data using ﬁnite
difference approximations. However, this introduces signiﬁ-
cant noise error into the calculations, and makes it difﬁcult to
determine which oscillations (particularly in the acceleration
and drag histories) are physical and which are noise-driven.
Following the experiments, we could use a polynomial ﬁt to
the drift data, and then differentiate the ﬁtted curve to obtain
velocity and acceleration curves. Although preferable over
the ﬁnite difference method, this strategy also has its draw-
backs. Experimental data have shown that the drift history
of the cylinders is well approximated by a quadratic polyno-
mial. Fitting the drift data with a quadratic (or even cubic)
polynomial then restricts the acceleration to, at best, a linear
function. Of course, higher order polynomial ﬁts are possi-
ble, but they are still unable to capture the high-frequency
oscillations that end up characterizing the acceleration. Tak-
ing advantage of the type of quantitative analysis allowed
by numerical simulations, we derive integral expressions for
the center-of-mass velocity and acceleration, which mini-
mize unnecessary noise error in the calculation. Assuming
constant liquid mass in the computational domain (zero mass
ﬂux across volume boundaries), usage of the continuity equa-
tion and the divergence theorem allow simpliﬁcation of the
time derivatives of (12). Taking a derivative with respect to
time through the integral in the numerator of (12) and simpli-
fying yields the following expression for the center-of-mass
velocity:
¯u =
∫
α
lρl u dV∫
αlρl dV . (13)
123

<!-- PDF_PAGE: 6 -->

404 J. C. Meng, T. Colonius
Note that the integrals in the denominators of ( 12) and (13)
represent the total liquid mass in the domain, and can be
treated as constants with respect to time under the given
assumptions. Taking a time derivative of ( 13) then yields
the following for the acceleration of the center of mass:
¯a =
d
dt
∫
αlρl u dV∫
αlρl dV =
∫ ∂
∂t (αlρl u) dV∫
αlρl dV . (14)
This can be directly calculated from our solver since αlρl u
is known everywhere in the domain at each timestep. It can
be shown that (14) is equivalent to
¯a =
∫
α
lρl a dV∫
αlρl dV , a = Du
Dt = ∂u
∂t + u ·∇ u, (15)
under the same assumptions. Mathematically, (14) and (15)
are equivalent. However, from a computational standpoint,
it is preferable to use (14) since it involves only a ﬁnite dif-
ference approximation in time, whereas ( 15) requires ﬁnite
difference approximations in both time and space. The inte-
gral expressions (13) and (14) allow us to calculate accurate
time histories of the center-of-mass velocity and acceleration,
while minimizing the amount of noise error in the calcula-
tion. Once liquid mass is lost through the volume boundaries,
(13) and (14) do not hold, and we terminate their calculation.
4 Results and discussion
4.1 Qualitative features of breakup
Similar qualitative ﬂow features of the breakup process are
observed over the range of simulated shock Mach numbers,
with the only differences arising when quantifying relevant
length and time scales. Therefore, in describing the ﬂow fea-
tures, we will, in this section, focus solely on the Mach 1.47
case. A time history of the breakup process is shown in Fig.4,
where the shock (and subsequent ﬂow) is moving from left
to right. The incident shock and the subsequent wave system
in the wake of the deforming cylinder are visualized using a
numerical schlieren function
1 As previously mentioned, the
actual traversal of the shock wave over the cylinder does lit-
tle in terms of cylinder deformation. The shock’s inﬂuence,
or lack of it, on the cylinder is attributed to the fact that the
1 Following Quirk and Karni [30], the schlieren function is computed
as the exponential of the negative, normalized density gradient.
φ = exp
(
− k |∇ρ|
max |∇ρ|
)
,
where k is a scaling parameter that allows simultaneous visualization
of waves in both ﬂuids. Following Johnsen [ 22], k = 40 for air and
k = 400 for water.
time scale of the shock is smaller than the relaxation time
of the cylinder [1]. In fact, during the very early stages, the
cylinder can be approximated as a rigid cylinder. The orig-
inal shock and reﬂected wave are seen in Fig. 4b. Behind
the reﬂected wave, there is a high pressure region associated
with the forward stagnation point. At a critical angle preced-
ing the equator of the cylinder, the shock reﬂection transi-
tions from a regular reﬂection to a Mach reﬂection shown
in Fig. 4c. This transition marks the peak drag experienced
by the cylinder. This phenomenon has been studied in the
literature for rigid cylinders and spheres [ 34,35]. The con-
vergence of the Mach stems behind the cylinder results in a
secondary wave system (Fig. 4d) that generates high pres-
sures at the rear stagnation point. The non-uniform pressure
ﬁeld around the cylinder results in an initial ﬂattening that
is reinforced by the pulling of material away from the equa-
tor by the surrounding ﬂow. It has been suggested that the
early time ﬂattening is independent of viscosity or mater-
ial type at large Weber numbers [ 24]. In conjunction with
the lateral elongation, tips are observed to form on the cylin-
der’s periphery (Fig.4e–g), which are thought to be the onset
of the stripping process [ 3]. In time, these tips are drawn
downstream into thin ﬁlaments. Though not captured in these
simulations (due to the absence of surface tension), the rise
of capillary instabilities in these ﬁlaments causes them to
break up downstream. Behind the cylinder, unsteady vortex
shedding drives the formation of a complex wake. Initially,
the wake consists of a single large vortex seen in Fig. 4d–f.
As more vortices are shed, the wake becomes increasingly
chaotic. This vortical structure is observed to entrain down-
stream ﬂuid and jet it upstream to impinge on the back of
the cylinder. This upstream jet persists for the duration of the
simulation. Within the wake, a standing shock can also be
observed (Fig.4e–g), which is associated with the turning of
the locally supersonic ﬂow.
An interesting ﬂow feature to note is the existence of recir-
culation regions near the equator of the deforming cylinder,
which, as far as we are aware, has not been noted before in the
literature. Consider for now the top half of the water cylin-
der. As the normal shock passes over the hemisphere, neg-
ative vorticity is generated by the baroclinic vorticity term,
1
ρ2 ∇ρ ×∇ p, which is transported downstream by the sur-
rounding ﬂow. This stream of negative vorticity is the source
of vortex shedding that creates the wake behind the deform-
ing cylinder. Along the back side of the cylinder, positive
vorticity is generated again by the baroclinic term. The large
vortex in the cylinder’s wake transports this positive vorticity
up along the ﬂattened back of the cylinder until it runs per-
pendicularly into the stream of negative vorticity coming off
the front of the cylinder. These two streams of opposite vor-
ticity interact to form the recirculation region seen in Fig. 5.
The recirculation region is composed of two counter-rotating
vortices that are trapped by the two vorticity streams and the
123

<!-- PDF_PAGE: 7 -->

Numerical simulations of the early stages 405
Fig. 4 Numerical schlieren images ( top) and ﬁlled pressure contours
(bottom) of the breakup of a 4.8 mm cylinder att∗ = a 0.000 b 0.008 c
0.017 d 0.090 e 0.171 f 0.262 g 0.444 h 0.626 i 0.808 j 1.036 behind
a Mach 1.47 shock wave (top to bottom, left to right ). Isocontours are
shown for αl ≥ 0.9
123

<!-- PDF_PAGE: 8 -->

406 J. C. Meng, T. Colonius
Negative vorticity stream
Positive vorticity stream
Clockwise vortex
Fig. 5 Positive (red) and negative (blue) vorticity streams interacting
to form a recirculation region at t∗ = 0.171
cylinder body. This recirculation region persists through the
early deformation times of the cylinder, and appears to con-
tribute to the stripping mechanism at the edge of the cylinder.
This would support Engel’s theory that stripping of water by
vortices contributes to the formation of mist in the wake [6].
In time, as pressure forces ﬂatten the cylinder, the two vortic-
ity streams are bent parallel to the ﬂow, and the recirculation
region disappears.
Another interesting ﬂow feature observed in the numerical
simulations is the aforementioned upstream jet in the wake
behind the cylinder. It is a possibility that the jet is an artifact
of assuming symmetry in the simulation. It is well known that
for a large range of Reynolds numbers (45 < Re < 10
5),
ﬂow around a rigid cylinder will generate a von Kármán vor-
tex street. The symmetry assumption is acceptable for early
times since a ﬁnite time is required to establish the vortex
street. For the Reynolds numbers corresponding to the sim-
ulations, it is conceivable that, if the symmetry assumption
were to be relaxed, a vortex street may develop in the wake
of the deforming water cylinder. If, indeed, a vortex street
is established, the upstream jet may decrease in strength, or
cease to exist altogether. Finally, we note that the jet would
most likely change in three-dimensional simulations of a
deforming spherical droplet due to the “ﬂow-relieving effect”
of the third dimension.
4.2 Comparison with experimental visualizations
Qualitative comparisons with experimental visualizations of
the breakup process are shown in Fig. 6 for the passage of a
Mach 1.47 shock over a 4.8 mm diameter cylinder. At these
early times in the breakup process, it is hard to make any
comparisons regarding the cylinder’s deformation. Instead,
one can compare the primary and secondary wave systems
that are generated as the shock interacts with the water cylin-
der. The locations of the primary wave system, consisting of
the incident and reﬂected shock, coincide between the exper-
iment and the numerical simulations for both time instances
shown. The secondary wave system, generated when the
Mach stems on both sides of the cylinder converge on the
rear stagnation point, looks qualitatively similar between the
experiment and simulation. A closer comparison reveals that
the secondary waves in the simulation are slower than those
of the experiment; pending further analysis, the exact cause
of this discrepancy is difﬁcult to identify.
4.3 Comparison of subsonic and supersonic post-shock gas
velocities
Numerical schlieren images of the breakup of the water cylin-
ders behind Mach 1.30 and Mach 2.50 shocks are shown in
Fig. 7. The supersonic gas velocity behind the Mach 2.50
shock is evidenced by the detached bow shock preceding
the deforming water cylinder. Cylinder wakes for supersonic
post-shock ﬂow appear to be narrower than their subsonic
counterparts, and standing shocks are visible along the length
of the wake.
4.4 Deformation
Using holographic interferograms, Igra and Takayama [ 20]
quantiﬁed the cylinder’s deformation by measuring its span-
wise diameter, d, centerline width, w, and coherent body
area, A. In the following plots, we compare our numerical
results with the experimental measurements for the above
deformation metrics. There exists, in our comparison, an
inherent uncertainty associated with the methodology or cri-
teria used to deﬁne the boundary of the deforming body.
The ﬁrst part of the uncertainty arises from the experimental
data itself. From Igra and Takayama’s discussion, it is not
possible to unambiguously identify the criteria they used to
determine the boundaries of the deforming body. Further-
more, they provide no quantiﬁcation of the error associated
with their measurements of deformation.
Additional uncertainty in the comparison stems from our
numerical method, which has diffuse interfaces in ﬁnite grid
resolution. To deﬁne a nominal interface location, we choose
a threshold liquid volume fraction, α
T , to bound the cylin-
der, i.e., any computational cell with a liquid volume fraction
αl ≥ αT is considered part of the cylinder. Because of the
uncertainty in the experimental measurements, it is unclear
what valueα
T should take to best match the data. Therefore,
instead of specifying a single value, a range is chosen in an
attempt to bound the experimental data. This is demonstrated
in Fig. 8, which plots the cylinder’s centerline width for the
MS = 1.47 case (the stepped nature of the curves is an arti-
fact of approximating to the nearest grid cell). The curves
in the plot represent four distinct values of αT that range
between 0.25 ≤ αT ≤ 0.99. Since the following comparison
plots will show a range of shock Mach numbers, which are
differentiated by color, only two αT curves will be plotted
for each MS.
123

<!-- PDF_PAGE: 9 -->

Numerical simulations of the early stages 407
Fig. 6 Holographic interferograms (left)[ 19] and numerical schlieren images ( right)a t t = a 16.18 µs b 32.14 µs. Note that the values of time
have been adjusted from the original work as described in Appendix B. Reprinted from [19] with permission from Springer
Fig. 7 Numerical schlieren images of the breakup behind Mach 1.30 ( top) and Mach 2.50 ( bottom) shock waves at t∗ = a 0.3543 b 0.5117
c 0.7479 d 0.9053
Figures 9, 10, and 11 show, respectively, the centerline
width, spanwise diameter, and coherent body area for four
MS cases. After the passage of the shock wave, the cylinder’s
deformation is characterized by ﬂattening in the streamwise
direction, which is quantiﬁed here as an increase in spanwise
diameter and decrease in centerline width. As material is
stripped off the cylinder’s periphery by the surrounding high-
speed ﬂow, the area of the cylinder monotonically decreases.
Additional comparison data from the numerical work of Chen
[3] are shown in Fig.11. Though not a rigorous validation of
our solver due to the aforementioned ambiguities, compar-
ison with the experimental data provides conﬁdence in the
accuracy of the numerical results.
4.5 Cylinder drift and velocity
Before analyzing the unsteady acceleration and drag of the
deforming cylinder, it is informative to ﬁrst look at the
123

<!-- PDF_PAGE: 10 -->

408 J. C. Meng, T. Colonius
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1.0
1.1
w/d0
t∗
αT = 0.25
αT = 0.50
αT = 0.90
αT = 0.99
0.0 0.2 0.4 0.6 0.8 1.0 1.2
Fig. 8 Centerline width of the deforming water cylinder for various
αT .T h einset contour plot shows the cylinder boundary as deﬁned by
the values of αT at t∗ = 0.810
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1.0
1.1
0.0 0.2 0.4 0.6 0.8 1.0 1.2 1.4
w/d0 0.25 ≤ αT ≤ 0.99
MS = 1. )
MS = 1. )
MS = 1. )
MS = 1.
18 (
30 (
47 (
73 ( )
t∗
Fig. 9 Cylinder centerline width from Igra and Takayama’s [20] exper-
iments (discrete), and our simulations (continuous). Thearrowindicates
the direction of increasing αT
1.0
1.5
2.0
2.5
3.0
3.5
d/d0
t∗
0.25 ≤ αT ≤ 0.99
() MS = 1.18
() MS = 1.30
() MS = 1.47
() MS = 1.73
0.0 0.2 0.4 0.6 0.8 1.0 1.2
Fig. 10 Cylinder spanwise diameter from Igra and Takayama’s [ 20]
experiments (discrete), and our simulations ( continuous). The arrow
indicates the direction of increasing αT
0.3
0.4
0.5
0.6
0.7
0.8
0.9
1.0
1.1
1.2
0.0 0.2 0.4 0.6 0.8 1.0 1.2 1.4
A/A0
t∗
0.25 ≤ αT ≤ 0.99
() MS = 1.18
(, ) MS = 1.30
(,
---
--- ) MS = 1.47
() MS = 1.73
Fig. 11 Cylinder coherent body area from Igra and Takayama’s [ 20]
experiments (discrete), and our simulations ( continuous). The arrow
indicates the direction of increasingαT . The numerical results of Chen
[3]( dashed)a r es h o w nf o rαT = 0.9
0.0
0.2
0.4
0.6
0.8
1.0
1.2
1.4
1.6
1.8Δ x/d0
t∗
0.25 ≤ αT ≤ 0.99
() MS = 1.18
(,) MS = 1.30
(,) MS = 1.47
() MS = 1.73
0.0 0.2 0.4 0.6 0.8 1.0 1.2 1.4
Fig. 12 Cylinder leading edge drift from Igra and Takayama’s [ 20]
experiments (discrete), and our simulations ( continuous). The arrow
indicates the direction of increasingαT . The numerical results of Chen
[3]( inverted ﬁlled triangle)a r es h o w nf o rαT = 0.9
detailed drift and velocity histories of the cylinder. The cylin-
der’s drift, as measured off the forward stagnation point, is
shown in Fig.12. For shock Mach numbers up toMS = 1.47,
our numerical results coincide well with the experimental
measurements, falling within the error bounds, and show a
slight improvement over the results from Chen [3]. For rea-
sons not yet understood, our comparison appears to deteri-
orate with increasing shock Mach number (as evidenced by
the discrepancy in the M
S = 1.73 case).
As noted by Theofanous [ 38], the stagnation point drift
of the cylinder is an inaccurate representation of the center-
of-mass drift. To evaluate the signiﬁcance of the error, we
compute both the location of the cylinder’s center of mass
[using (12)] and its leading edge (using α
T = 0.50), and
plot both in Fig. 13 for the full range of simulated shock
123

<!-- PDF_PAGE: 11 -->

Numerical simulations of the early stages 409
0.0
0.2
0.4
0.6
0.8
1.0
1.2
1.4
1.6
1.8
2.0Δ x/d0
t∗
MS = 1.18
MS = 1.30
MS = 1.47
MS = 1.73
MS = 2.00
MS = 2.50
0.0 0.2 0.4 0.6 0.8 1.0 1.2 1.4 1.6
Fig. 13 Drift as measured from the center of mass (solid) and forward
stagnation point (dashed), and normalized by the original diameter
Mach numbers. The intersection of the center-of-mass and
leading edge curves can be seen for the MS = 2.00 and
MS = 2.50 cases. Although both sets of drift curves exhibit
similar overall behavior, it is obvious to see that signiﬁcant
errors are incurred in the acceleration calculation if the ﬁtted
polynomial is based on the leading edge trajectory. It is noted
that the appropriate non-dimensionalization of time using the
characteristic breakup time shown in (8) appears to collapse
the cylinder trajectories across all simulated M
S.
The cylinder’s streamwise center-of-mass velocity, ¯u,i s
computed using ( 13) and shown in Fig. 14. Though scaled
using the same characteristic breakup time, t∗, as the drift
curves, the velocity curves do not appear to collapse, and
clearly show that stronger shocks induce higher cylinder
velocities. This is expected since, in the shock-moving ref-
erence frame, post-shock air velocity increases with shock
Mach number. From these velocity curves, it can also be seen
that the transition from subsonic to supersonic freestream
ﬂow does not seem to signiﬁcantly alter the cylinder’s behav-
ior.
4.6 Unsteady acceleration and drag coefﬁcient
The unsteady acceleration of a droplet suddenly exposed to
a high-speed ﬂow, and speciﬁcally, its unsteady drag coefﬁ-
cient, is of interest in many applications. For example, when
modeling ﬂows with particle or droplet clouds, the drag coef-
ﬁcient is often the parameter used to model the dynamics of
the disperse phase. Attempts to calculate the drag coefﬁcient
of a deforming body have often assumed constant acceler-
ation [21,31,33]. Indeed, the acceleration data reported by
Chen [3] are derived from the drift data under this assump-
tion. Despite the ubiquity of this simpliﬁcation in the litera-
ture, our numerical results lead us to believe that this is not
an accurate representation of the underlying physics. For this
0.00
0.02
0.04
0.06
0.08
0.10
0.12
0.14
0.16
0.18
0.20
0.0 0.2 0.4 0.6 0.8 1.0 1.2 1.4 1.6
¯u/ug
t∗
MS = 1.18
MS = 1.30
MS = 1.47
MS = 1.73
MS = 2.00
MS = 2.50
Fig. 14 Center-of-mass velocity normalized by the post-shock air
velocity
reason, we do not make comparisons with Chen [ 3]f o rt h e
cylinder acceleration and drag coefﬁcient.
Using (14), we compute the acceleration in the stream-
wise direction experienced by the cylinder’s center of mass,
¯a. The results are plotted in Fig. 15, where acceleration has
been non-dimensionalized by the original cylinder diameter
and post-shock air velocity. The initial spike in acceleration
is the passage of the shock wave over the cylinder. As men-
tioned in Sect. 4.1, the maximum acceleration occurs when
the shock reﬂection on the cylinder’s surface transitions from
a regular reﬂection to a Mach reﬂection. Once the shock has
passed, the surrounding high-speed air begins to accelerate
the cylinder. The oscillations in the acceleration curves are
believed to be related to the vortex shedding process in the
cylinder’s wake. It is observed that oscillation frequency and
amplitude increase and decrease, respectively, as the incident
shock Mach number is increased. These changes in frequency
and amplitude can be attributed to differences in the devel-
opment of the wake behind the deforming cylinder.
In the course of our numerical analysis, we found that scal-
ing the non-dimensional acceleration by the pressure ratio
across the incident shock wave resulted in collapse of the
acceleration curves across all simulated shock Mach num-
bers. As far as we are aware, this has not been noted before
in the literature. The rescaled non-dimensional acceleration,
plotted in Fig. 16, is given by
¯a
∗ =¯a
( d0
u2g
)( p1
p2
)
, (16)
where p2
p1 is the pressure ratio across the incident shock.
Now that we have an accurate acceleration history for
the deforming cylinder, we can calculate its unsteady drag
coefﬁcient. The drag coefﬁcient is deﬁned as:
123

<!-- PDF_PAGE: 12 -->

410 J. C. Meng, T. Colonius
0
2
4
6
8
10
12
14
16
18
0.0 0.2 0.4 0.6 0.8 1.0 1.2 1.4 1.6
¯a(d0/u2
g)[ 10− 3]
t∗
MS = 1.18
MS = 1.30
MS = 1.47
MS = 1.73
MS = 2.00
MS = 2.50
Fig. 15 Center-of-mass acceleration normalized by the original diam-
eter and the post-shock air velocity
0
1
2
3
4
5
6
7
8
9
¯a∗ [10− 3]
t∗
MS = 1.18
MS = 1.30
MS = 1.47
MS = 1.73
MS = 2.00
MS = 2.50
0.0 0.2 0.4 0.6 0.8 1.0 1.2 1.4 1.6
Fig. 16 Center-of-mass acceleration rescaled by the pressure ratio
across the incident shock
CD = D
1
2ρu2 S
= m ¯a
1
2ρg(ug −¯u)2d
, (17)
where ρg and ug are the post-shock air density and velocity,
¯u and ¯a are the velocity and acceleration of the cylinder’s
center of mass calculated using (13) and (14), m is the con-
stant liquid mass in the computational domain, and d is a
characteristic spanwise diameter. If we take the characteris-
tic spanwise diameter to be the original cylinder diameter,
d
0, the computed drag coefﬁcients, shown in Fig. 17, col-
lapse across the range of simulated MS, and all exhibit an
upward trend.
Though a time-dependent drag coefﬁcient can be used to
model the dynamics of particles or droplets, an improvement
can be made by realizing that the drag coefﬁcient calcula-
tion should account for the changing spanwise diameter of
the deforming cylinder. If we re-calculate the drag coefﬁ-
cient using the cylinder’s deformed diameter,d
def , it is found
that the resultant CD, shown in Fig. 18, can be reasonably
0
2
4
6
8
10
12d0-based CD
t∗
MS = 1.18
MS = 1.30
MS = 1.47
MS = 1.73
MS = 2.00
MS = 2.50
0.0 0.2 0.4 0.6 0.8 1.0 1.2 1.4 1.6
Fig. 17 Unsteady drag coefﬁcient based on the original diameter
0
2
4
6
8
10
12
0.0 0.2 0.4 0.6 0.8 1.0 1.2 1.4 1.6
ddef-based CD
t∗
MS = 1.18
MS = 1.30
MS = 1.47
MS = 1.73
MS = 2.00
MS = 2.50
Fig. 18 Unsteady drag coefﬁcient based on the deformed diameter
approximated as a constant over the initial breakup period.
It is notable that wave drag (in the case of supersonic post-
shock ﬂow) does not signiﬁcantly alter the drag coefﬁcient
(as would be expected in the rigid body case). Not only is this
drag coefﬁcient more physically correct than the one based on
the original cylinder diameter, it also simpliﬁes the modeling
of particle and drop dynamics since it can be approximated
as a constant for the early times of breakup.
5 Conclusions
The breakup of water cylinders in the ﬂow behind normal
shock waves has been simulated and is compared to pub-
lished experimental and numerical data. Our results sup-
port previous experimental observations regarding the strip-
ping breakup of the cylinders. Speciﬁcally, the water cylin-
der is initially compressed in the streamwise direction and
extended in its spanwise dimension. Tips are formed at the
cylinder’s periphery, which are drawn downstream by the
123

<!-- PDF_PAGE: 13 -->

Numerical simulations of the early stages 411
surrounding ﬂow. The stripping of material at the cylinder
periphery is partly attributed to the presence of a recircu-
lation region at the equator. The recirculation regions, not
noted before in the literature, are observed to result from the
interaction of two streams of opposite vorticity generated by
baroclinic torque on the cylinder surface. Engel [6] hypothe-
sized the existence of such vortices in the ﬂow, which would
contribute to the formation of mist in the wake. An upstream
jet in the wake of the deforming cylinder is also observed to
persist for long times. The strength of this jet is expected to
be mitigated if either the symmetry assumption or the two-
dimensional approximation is relaxed.
Comparison with experimental data for metrics of the
cylinder’s deformation is hampered by uncertainties asso-
ciated with the experimental measurements and the numer-
ical method. However, reasonable agreement is shown to
the extent that the numerical results are able to bound,
and exhibit similar behavior to, the experimental results.
The transition from subsonic to supersonic freestream ﬂow
does not alter the similarity of the solutions, and collapse
is shown for the unsteady acceleration and drag coefﬁcients
for the range of simulated shock Mach numbers. The accel-
eration time histories of the deforming cylinders for dif-
ferent incident shock Mach numbers are shown to scale
with the pressure ratio across the incident shock wave. Fur-
thermore, the unsteady drag coefﬁcient is seen to increase
with time when computed using the constant original cylin-
der diameter. However, when computed using the cylinder’s
deformed diameter, the unsteady drag coefﬁcient can be
approximated as a constant over the initial breakup period.
Three-dimensional simulations and the inclusion of viscous
and capillary effects in future simulations will facilitate com-
parison with droplet experiments, and capture even more of
the multiscale and multiphase ﬂow physics present in the
breakup process.
Acknowledgments We are indebted to Vedran Coralic who devel-
oped the ﬂow solver and graciously shared the source code with us.
Also, our gratitude to Guillaume Blanquart for his insight and guidance
in many useful discussions.
Appendix A: Grid resolution
As part of the grid resolution study, we simulated the Mach
1.47 shock wave case at three different resolutions. A time
history of these simulations is shown in Fig. 19. Though the
wake structure becomes more detailed as the grid is reﬁned,
the overall qualitative features of the breakup process remain
similar. Features characteristic of stripping breakup, such as
the initial ﬂattening of the cylinder and the formation of tips
at the cylinder’s periphery, are present at all three grid resolu-
tions. The recirculation regions at the cylinder’s equator and
the presence of an upstream jet in the wake are also observ-
able at all levels of grid reﬁnement. Quantitative measure-
ments of cylinder deformation and center-of-mass properties,
used in the comparison with experimental data, do not show
signiﬁcant differences between the original and doubled res-
olution. As an example, Fig.20 plots the center-of-mass drift
calculated at the three different grid resolutions, and shows
negligible differences between the two ﬁnest grid sizes.
123

<!-- PDF_PAGE: 14 -->

412 J. C. Meng, T. Colonius
Fig. 19 Numerical schlieren images (top) and ﬁlled pressure contours
(bottom) of the breakup of a 4.8 mm cylinder at t∗ = a 0.017 b 0.171
c 0.262 d 0.444 e 0.626 f 0.808 g 1.036 behind a Mach 1.47 shock.
Isocontours are shown for αl ≥ 0.9. Grid resolutions correspond to
600x300 (left), 1,200 × 600 (middle), and 2,400 × 1,200 (right) cells
123

<!-- PDF_PAGE: 15 -->

Numerical simulations of the early stages 413
-0.1
0.0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
0.0 0.2 0.4 0.6 0.8 1.0 1.2
Δ x/d0
t∗
600x300
1200x600
2400x1200
Fig. 20 Center-of-mass drift measurements at three grid resolutions
Appendix B: Experimental visualization comparison
The holographic interferograms of [ 19]u s e di nF i g .6 were
originally stated to be at t = 23 µs and t = 43 µs after “the
interaction between the incident shock wave and the water
column” [19]. We interpret this to mean the time after the
shock reaches the leading edge of the water cylinder. A com-
parison of the experimental interferograms and the numeri-
cal schlieren images from our simulations at these times is
shown in Fig. 21. It is clear from the ﬁgure that any compar-
ison is difﬁcult to make since the images appear to be taken
at different times. In an attempt to reconcile the discrepancy,
digital measurements of the distance traversed by the inci-
dent shock were taken from the interferograms. Our mea-
surements indicate that the times should perhaps be closer
to 16 and 32µs, respectively. Numerical schlieren images at
these modiﬁed times are compared to the experimental inter-
ferograms in Fig. 6, and are seen to match the incident and
reﬂected shock locations. There is an inherent uncertainty
in the exact location of the boundary of the water cylinder,
owing to the thick ring on the holographic interferograms.
Measurements to obtain times of 16 and 32 µs were taken
by assuming the boundary to be located in the middle of the
thick ring. Measurements taken from the edge of the ring
resulted in alternate times of approximately 22 and 42 µs,
respectively, which are closer to the reported times in [ 19].
It is unclear whether this discrepancy in time is a result of a
reporting error in the original work, or a misinterpretation,
on our part, of what is meant by “the interaction between the
incident shock wave and the water column” [19].
References
1. Aalburg, C., Leer, B.V ., Faeth, G.M.: Deformation and drag prop-
erties of round drops subjected to shock-wave disturbances. AIAA
J. 41(12), 2371–2378 (2003)
2. Allaire, G., Clerc, S., Kokh, S.: A ﬁve-equation model for the sim-
ulation of interfaces between compressible ﬂuids. J. Comput. Phys.
181, 577–616 (2002)
3. Chen, H.: Two-dimensional simulation of stripping breakup of a
water droplet. AIAA J. 46(5), 1135–1143 (2008)
4. Coralic, V ., Colonius, T.: Shock-induced collapse of a bubble inside
a deformable vessel. Eur. J. Mech. B-Fluid 40, 64–74 (2013)
5. Coralic, V ., Colonius, T.: Finite-volume WENO scheme for viscous
compressible multicomponent ﬂows. J. Comput. Phys.274, 95–121
(2014)
6. Engel, O.G.: Fragmentation of waterdrops in the zone behind an
air shock. J. Res. Nat. Bur. Stand. 60(3), 245–280 (1958)
7. Gel’fand, B.E., Gubin, S.A., Kogarko, S.M., Komar, S.P.: Singu-
larities of the breakup of viscous liquid droplets in shock waves. J.
Eng. Phys. Thermophys. 25(3), 1140–1142 (1973)
8. Gojani, A.B., Ohtani, K., Takayama, K., Hosseini, S.H.R.: Shock
Hugoniot and equations of states of water, castor oil, and aqueous
solutions of sodium chloride, sucrose, and gelatin. Shock Waves
1–6 (2009). doi:10.1007/s00193-009-0195-9
9. Guildenbecher, D.R., López-Rivera, C., Sojka, P.E.: Secondary
atomization. Exp. Fluids 46, 371–402 (2009)
10. Han, J., Tryggvason, G.: Secondary breakup of axisymmetric liquid
drops. I. Acceleration by a constant body force. Phys. Fluids11(12),
3650–3667 (1999)
Fig. 21 Holographic interferograms (left)[ 19] and numerical schlieren images (right)a t t = a 23 µs b 43 µs. Reprinted from [19] with permission
from Springer
123

<!-- PDF_PAGE: 16 -->

414 J. C. Meng, T. Colonius
11. Han, J., Tryggvason, G.: Secondary breakup of axisymmetric liquid
drops. II. impulsive acceleration. Phys. Fluids 13(6), 1554–1565
(2001)
12. Hanson, A.R., Domich, E.G., Adams, H.S.: Shock tube investi-
gation of the breakup of drops by air blasts. Phys. Fluids 6(8),
1070–1080 (1963)
13. Harlow, F.H., Amsden, A.A.: Fluid dynamics. Tech. Rep. LA-4700,
LASL (1971)
14. Hirahara, H., Kawahashi, M.: Experimental investigation of vis-
cous effects upon a breakup of droplets in high-speed air ﬂow.
Exp. Fluids 13, 423–428 (1992)
15. Hsiang, L.P., Faeth, G.M.: Near-limit drop deformation and sec-
ondary breakup. Int. J. Multiphase Flow 18(5), 635–652 (1992)
16. Hsiang, L.P., Faeth, G.M.: Drop properties after secondary breakup.
Int. J. Multiphase Flow 19(5), 721–735 (1993)
17. Hsiang, L.P., Faeth, G.M.: Drop deformation and breakup due to
shock wave and steady disturbances. Int. J. Multiphase Flow21(4),
545–560 (1995)
18. Igra, D., Takayama, K.: Experimental and numerical study of the
initial stages in the interaction process between a planar shock
wave and a water column. In: Proc. 23rd Int. Symposium on Shock
Waves, 5071. The University of Texas at Arlington, Arlington,
Texas, USA., Fort Worth, Texas (2001)
19. Igra, D., Takayama, K.: Numerical simulation of shock wave inter-
action with a water column. Shock Waves 11, 219–228 (2001)
20. Igra, D., Takayama, K.: A study of shock wave loading on a cylin-
drical water column. Tech. Rep. V ol. 13, pp. 19–36, Institute of
Fluid Science, Tohoku University (2001)
21. Igra, D., Takayama, K.: Experimental investigation of two cylin-
drical water columns subjected to planar shock wave loading. J.
Fluid Eng. T. ASME 125, 325–331 (2003)
22. Johnsen, E.: Numerical simulations of non-spherical bubble col-
lapse with applications to shockwave lithotripsy. Ph.D. thesis, Cal-
ifornia Institute of Technology, Pasadena, CA (2007)
23. Johnsen, E., Colonius, T.: Implementation of WENO schemes in
compressible multicomponent ﬂow problems. J. Comput. Phys.
219, 715–732 (2006)
24. Joseph, D.D., Belanger, J., Beavers, G.S.: Breakup of a liquid drop
suddenly exposed to a high-speed airstream. Int. J. Multiphase Flow
25, 1263–1303 (1999)
25. Lane, W.R.: Shatter of drops in streams of air. Ind. Eng. Chem.
43(6), 1312–1317 (1951)
26. Ortiz, C., Joseph, D.D., Beavers, G.S.: Acceleration of a liquid drop
suddenly exposed to a high-speed airstream. Int. J. Multiphase Flow
Brief Commun. 30, 217–224 (2004)
27. Perigaud, G., Saurel, R.: A compressible ﬂow model with capillary
effects. J. Comput. Phys. 209, 139–178 (2005)
28. Pilch, M., Erdman, C.A.: Use of breakup time data and velocity
history data to predict the maximum size of stable fragments for
acceleration-induced breakup of a liquid drop. Int. J. Multiphase
Flow 13(6), 741–757 (1987)
29. Quan, S., Schmidt, D.P.: Direct numerical study of a liquid droplet
impulsively accelerated by gaseous ﬂow. Phys. Fluids 18, 102103
(2006)
30. Quirk, J.J., Karni, S.: On the dynamics of a shock-bubble interac-
tion. J. Fluid Mech. 318, 129–163 (1996)
31. Ranger, A.A., Nicholls, J.A.: Aerodynamic shattering of liquid
drops. In: Proc. AIAA 6th Aerospace Sciences Meeting, 68–83.
AIAA, New York, New York (1968)
32. Reinecke, W.G., Waldman, G.D.: A study of drop breakup behind
strong shocks with applications to ﬂight. Tech. Rep. SAMSO-TR-
70-142, Air Force Systems Command (1970)
33. Simpkins, P.G., Bales, E.L.: Water-drop response to sudden accel-
erations. J. Fluid Mech. 55, 629–639 (1972)
34. Takayama, K., Itoh, K.: Unsteady drag over cylinders and aerofoils
in transonic shock tube ﬂows. Tech. Rep. V ol. 51, Institute of High
Speed Mechanics, Tohoku University, Sendai, Japan (1986)
35. Tanno, H., Itoh, K., Saito, T., Abe, A., Takayama, K.: Interaction
of a shock with a sphere suspended in a vertical shock tube. Shock
Waves 13, 191–200 (2003). doi:10.1007/s00193-003-0209-y
36. Temkin, S., Kim, S.S.: Droplet motion induced by weak shock
waves. J. Fluid Mech. 96, 133–157 (1980)
37. Temkin, S., Mehta, H.K.: Droplet drag in an accelerating and decel-
erating ﬂow. J. Fluid Mech. 116, 297–313 (1982)
38. Theofanous, T.G.: Aerobreakup of Newtonian and viscoelastic liq-
uids. Annu. Rev. Fluid Mech.
43, 661–690 (2011)
39. Theofanous, T.G., Li, G.J.: On the physics of aerobreakup. Phys.
Fluids 20, 052103 (2008)
40. Theofanous, T.G., Mitkin, V .V ., Ng, C.L., Chang, C.H., Deng, X.,
Sushchikh, S.: The physics of aerobreakup. II. viscous liquids.
Phys. Fluids 24, 022104 (2012)
41. Thompson, K.W.: Time dependent boundary conditions for hyper-
bolic systems. J. Comput. Phys. 68, 1–24 (1987)
42. Thompson, K.W.: Time dependent boundary conditions for hyper-
bolic systems. II. J. Comput. Phys. 89, 439–461 (1990)
43. Toro, E.F., Spruce, M., Speares, W.: Restoration of the contact
surface in the HLL-Riemann solver. Shock Waves4, 25–34 (1994)
44. Welch, P., Boyle, P.: New turbines to enable efﬁcient geothermal
power plants. GRC Trans. 33, 765–772 (2009)
123
