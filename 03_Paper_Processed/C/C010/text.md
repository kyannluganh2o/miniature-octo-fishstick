<!-- PDF_PAGE: 1 -->

J. Fluid Mech. (2018), vol. 835, pp. 1108–1135. c⃝ Cambridge University Press 2017
doi:10.1017/jfm.2017.804
1108
Numerical simulation of the aerobreakup of a
water droplet
Jomela C. Meng1,† and Tim Colonius1
1California Institute of Technology, Pasadena, CA 91125, USA
(Received 29 October 2016; revised 28 October 2017; accepted 3 November 2017;
ﬁrst published online 29 November 2017)
We present a three-dimensional numerical simulation of the aerobreakup of a spherical
water droplet in the ﬂow behind a normal shock wave. The droplet and surrounding
gas ﬂow are simulated using the compressible multicomponent Euler equations
in a ﬁnite-volume scheme with shock and interface capturing. The aerobreakup
process is compared with available experimental visualizations. Features of the droplet
deformation and breakup in the stripping breakup regime, as well as descriptions of
the surrounding gas ﬂow, are discussed. Analyses of observed surface instabilities and
a Fourier decomposition of the ﬂow ﬁeld reveal asymmetrical azimuthal modulations
and broadband instability growth that result in chaotic ﬂow within the wake region.
Key words: breakup/coalescence, drops, shock waves
1. Introduction
The study of droplet aerobreakup has historically been motivated by three
applications: bulk dissemination of liquid agents, raindrop damage during supersonic
ﬂight, and secondary atomization of liquid jets in turbomachinery. Much of the
aerobreakup literature has focused research efforts on characterizing and mapping
various breakup regimes (e.g. Lane 1951; Engel 1958; Hanson, Domich & Adams
1963; Ranger & Nicholls 1968; Hsiang & Faeth 1995), calculating characteristic
breakup times (e.g. Ranger & Nicholls 1968; Hsiang & Faeth 1992), quantifying
dependence on parameters such as density and viscosity ratios (e.g. Hanson et al.
1963; Theofanous et al. 2012), predicting ﬁnal drop size distributions (e.g. Ranger
& Nicholls 1968; Pilch & Erdman 1987), and quantifying unsteady drag properties
(e.g. Engel 1958; Simpkins & Bales 1972; Joseph, Belanger & Beavers 1999).
Unfortunately, these experimental and theoretical research efforts have resulted in
many, and often conﬂicting, phenomenological models describing the aerobreakup
process, and to date, a deﬁnitive understanding of aerobreakup remains elusive
(Khosla, Smith & Throckmorton 2006).
Beginning with the work of Hinze (1949), the Weber number, We=ρgu2
gD0/σ , has
been the principal parameter used to delineate the various regimes of aerobreakup.
Traditionally, there exist ﬁve distinct regimes that are well established in the literature
(Pilch & Erdman 1987; Guildenbecher, López-Rivera & Sojka 2009). They are,
† Email address for correspondence: jomela.meng@caltech.edu
https://doi.org/10.1017/jfm.2017.804
 Published online by Cambridge University Press

<!-- PDF_PAGE: 2 -->

Numerical simulation of the aerobreakup of a water droplet 1109
in order of increasing We, the vibrational, bag, bag-and-stamen, stripping, and
catastrophic regimes.
The stripping regime, which is of primary interest in this paper, marks a transition
in breakup physics that fundamentally differs from that of the preceding breakup
regimes. Generally speaking, the stripping regime is characterized by an initial
deformation of the droplet into a disk-like shape. Following the shape change, droplet
ﬂuid is observed to be stripped from the droplet’s periphery in a region near the
droplet equator (deﬁned as a polar, or inclination, angle of ϕ= π/2). Ranger &
Nicholls (1968) postulated the ‘boundary layer stripping’ or ‘shear stripping’ model,
where boundary layers both inside and outside the drop become unstable at the
droplet equator, and are subsequently stripped off by the ambient gas ﬂow. Liu &
Reitz (1997) later proposed an alternate mechanism known as ‘sheet thinning’, where
the droplet is initially ﬂattened by the pressure gradient between the drop’s poles
(ϕ= 0, π) and equator. Once ﬂattened, the strong inertial forces from the surrounding
ﬂow draw a thin sheet of liquid off the periphery. This sheet is accelerated, stretched,
and bent in the direction of ﬂow, and eventually breaks up into streamwise ligaments
that fragment into individual drops. Due to the ﬂattened disk-like shape of the
deformed droplet, ﬂow separation occurs for all practical values of the Reynolds
number, Re=ρgugD0/µg, and the sheet thinning mechanism can be considered an
inviscid phenomenon with no dependence on Re (Guildenbecher et al. 2009).
The instability of the thin liquid sheet that is drawn from the droplet’s periphery in
the sheet thinning model is thought to be responsible for the generation of product
droplets. Liu & Reitz (1997) described a ‘stretched streamwise ligament breakup’
mechanism wherein, for low liquid ﬂow rates of a planar liquid sheet sandwiched
between two shear air layers, streamwise vortical waves, alternating with thin liquid
membranes, would grow along the sheet. The membranes would burst ﬁrst due to the
rotation of the streamwise vortices, leaving streamwise ligaments that subsequently
broke up. More recently, Jalaal & Mehravaran (2014) attributed the breakup to the
rise of Rayleigh–Taylor (RT) instability waves on the sheet. In this mechanism, the
Kelvin–Helmholtz (KH) instability generates axisymmetric waves at the liquid–gas
interface. The transient acceleration of these wave crests or rims (in the case of
the liquid jet) into the downstream air triggers a RT instability, which produces
‘transverse azimuthal modulations.’
Recent work by Theofanous, Li & Dinh (2004) studying aerobreakup in rareﬁed
supersonic ﬂows, and subsequent publications (Theofanous & Li 2008; Theofanous
2011; Theofanous et al. 2012), has substantially changed the overall understanding of
aerobreakup. Theofanous et al. (2004) proposed a reclassiﬁcation into two principal
breakup regimes: Rayleigh–Taylor piercing (RTP) and shear-induced entrainment (SIE).
Theofanous & Li (2008) described SIE as a combination of shear-driven radial motion,
which results in the ﬂattening, as well as instabilities on the stretched liquid sheet.
Perhaps most importantly, this reclassiﬁcation argues that the catastrophic breakup
regime does not exist. Theofanous & Li (2008) contended that the wavy interface
on the upstream side of the droplet was an artefact created by a projected view of a
complex ﬂow ﬁeld, and that no RT waves exist or pierce the drop. Using laser-induced
ﬂuorescence as their experimental visualization technique, SIE was proposed as the
terminal regime for We> 103.
Recently, numerical simulation has emerged as a tool for studying aerobreakup.
Unfortunately, due to the high computational costs of fully three-dimensional (3D)
simulations, numerical aerobreakup studies have often invoked two-dimensional
(2D) (Zaleski, Li & Succi 1995; Igra & Takayama 2001 a,b,c; Chen 2008) or
https://doi.org/10.1017/jfm.2017.804
 Published online by Cambridge University Press

<!-- PDF_PAGE: 3 -->

1110 J. C. Meng and T. Colonius
axisymmetric (Han & Tryggvason 2001; Aalburg, Leer & Faeth 2003; Wadhwa, Magi
& Abraham 2007; Chang, Deng & Theofanous 2013) approximations. Additionally,
ﬂuid density ratios are often assumed to be small, or the ﬂuids are considered to
be incompressible (Han & Tryggvason 2001; Aalburg et al. 2003; Quan & Schmidt
2006; Jalaal & Mehravaran 2014; Xiao, Dianat & McGuirk 2014; Castrillon Escobar
et al. 2015; Jain et al. 2015). Previous work from the authors (Meng & Colonius
2015) simulated the early stages of two-dimensional aerobreakup, with comparison
to the experimental work of Igra & Takayama (2001 c). Qualitative features of the
breakup process, such as the presence of a transitory equatorial recirculation region
and an upstream jet in the wake, were discussed. Additionally, a parametric study
varying incident shock strength was performed to study the effects of the transition
between subsonic and supersonic post-shock ﬂow. A novel method of calculating
the cylinder’s centre-of-mass properties was also utilized to obtain accurate unsteady
acceleration and drag histories.
Using numerical simulation, the purpose of this paper is to elucidate the physical
breakup mechanisms responsible for the fully three-dimensional, compressible
aerobreakup of a single water droplet in air. While a direct numerical simulation
would be ideal for such an investigation, the computational grid required to fully
resolve all scales of the aerobreakup problem is intractable on currently available
computational resources; a compromise must be made. We thus consider the ‘inviscid’
case, which is in turn regularized by artiﬁcial viscosity and numerical diffusion
of the interface. The effects of these approximations are discussed in detail in
§ 3.2. Additionally, we will attempt to interpret the numerical results in a manner
consistent with the uncertainties introduced by the approximations. These results
ﬁll a gap in the current state of droplet aerobreakup knowledge associated with
the underlying fundamental ﬂow physics that dictates the experimentally observed
phenomena. Building upon the computational efforts of Coralic & Colonius (2014),
we utilize a compressible multicomponent ﬂow solver to numerically investigate this
fundamental ﬂuid dynamics problem. The rest of this paper is organized as follows.
In § 2, we describe the problem set-up and introduce the governing equations. The
numerical algorithm is subsequently described in § 3, along with the calculation of
various ﬂow quantities used in the analysis. We describe the evolution of the liquid
droplet, show its centre-of-mass properties, and compare with available experimental
visualizations in §§ 4, 4.1 and 4.2. The ﬂow ﬁeld in the gas phase is investigated in
§ 4.3. The mechanisms of surface instabilities are discussed in § 5.1, and are followed
by a Fourier decomposition analysis in § 5.2. Finally, concluding remarks are made
in § 6.
2. Physical modelling
2.1. Problem description
In the laboratory, shock tubes are most often used to generate large relative velocities
between the liquid droplet and surrounding gas ﬂow. Normal shock waves, in and
of themselves, have little effect on the droplet. Instead, they serve as a reliable and
repeatable way to create a high-speed ﬂow around the droplet, which is responsible
for the droplet’s subsequent deformation and disintegration (Hanson et al. 1963;
Ranger & Nicholls 1968; Joseph et al. 1999). In ﬁgure 1, a schematic is shown of
the initial condition and computational grid. The shock wave of strength Ms= 1.47
(modelled as a step discontinuity in ﬂuid properties) is travelling in air towards
the water droplet, which is initialized as a spherical interface with diameter D0 on
the cylindrical grid. The drop and the ambient air downstream of the shock are
https://doi.org/10.1017/jfm.2017.804
 Published online by Cambridge University Press

<!-- PDF_PAGE: 4 -->

Numerical simulation of the aerobreakup of a water droplet 1111
Post-shock
air
Pre-shock
air
NRBC
NRBCNRBC
NRBC
r
z
FIGURE 1. (Colour online) Schematic of the 3D initial condition and non-uniform
computational domain at 1:10 of the actual resolution. The grid extends radially outward
for 6 D0, and the axial extents are −7D0 ⩽ z ⩽ 15.5D0.
initialized at rest. The entire 3D ﬂow ﬁeld is simulated with no enforced symmetries.
Non-reﬂective boundary conditions (NRBC), applied at all computational domain
boundaries, approximately extend the surrounding air to inﬁnity. The simulation is
performed on the computational domain Ω=[−7D0, 15.5D0]×[0, 6D0]×[0, 2π]
with a spatial resolution of (Nz, Nr, Nθ)=(800, 600, 320) grid cells. The grid is
stretched towards the axial boundaries using a hyperbolic tangent function. The most
reﬁned portion of the grid is located near the initial location of the droplet and
in the region of the near-ﬁeld wake. In this region, the nominal axial and radial
grid resolution corresponds to 100 cells per original droplet diameter. The azimuthal
resolution is chosen such that the cells near the spherical droplet interface are close
to regular. Previous testing of grid resolution sensitivities in 2D (Meng & Colonius
2015; Meng 2016) suggests the present spatial resolution captures the salient ﬂow
features without being computationally cumbersome. The simulation is performed with
a constant Courant–Friedrichs–Lewy (CFL) number of 0.2. Since the initial condition
is axisymmetric, the gas is initially seeded with small random radial and azimuthal
velocity perturbations, the largest of which have approximate magnitudes of O(10−4us),
where us is the post-shock gas velocity. These white-noise-type perturbations are
generated via the Fortran compiler’s intrinsic random number generator, and are
applied to both the pre-shock and post-shock gas in the initial condition.
2.2. Governing equations
We model the ﬂow with the compressible multicomponent Euler equations. In addition
to being compressible, each ﬂuid is considered immiscible and does not undergo phase
change. In the absence of mass transfer and surface tension, material interfaces are
https://doi.org/10.1017/jfm.2017.804
 Published online by Cambridge University Press

<!-- PDF_PAGE: 5 -->

1112 J. C. Meng and T. Colonius
simply advected by the local ﬂow velocity. For a system of two ﬂuids, this gives
rise to a ﬁve-equation model, introduced in its inviscid form by Allaire, Clerc &
Kokh (2002). Implications of the choice to neglect viscous and capillary effects are
addressed in detail in § 3.2. The ﬁve-equation model, (2.1), consists of individual
continuity equations for each of the ﬂuids, (2.1 a) and (2.1 b), mixture momentum,
(2.1c), and energy, (2.1 d), equations, and a transport equation for the gas volume
fraction, (2.1 e):
∂(αgρg)
∂t +∇· (αgρgu)= 0, (2.1a)
∂(αlρl)
∂t +∇· (αlρlu)= 0, (2.1b)
∂(ρ u)
∂t +∇· (ρu⊗ u+ pI)= 0, (2.1c)
∂E
∂t+∇· ((E+ p)u)= 0, (2.1d)
∂αg
∂t + u·∇αg= 0, (2.1e)
where ρ is the density, α is the volume fraction, u is the velocity vector, p is the
pressure, E is the total energy deﬁned as E=ρε+(1/2)ρ∥u∥2, ε is the speciﬁc
internal energy, and the subscripted g, l represent, respectively, the gas and liquid
ﬂuids. Each equation in the ﬁve-equation model, (2.1), is evolved independently of
all others. While alternate models for multicomponent ﬂows exist within the literature
(e.g. Kapila et al. 2001; Murrone & Guillard 2005; Saurel, Petitpas & Berry 2009;
Pelanti & Shyue 2014), the present model is chosen for its simplicity and desirable
conservation properties. The simpliﬁed interface model theoretically ensures volume
fraction positivity, and does not require regularization to fully specify shock jump
conditions. Though it is not capable of physically handling mixture regions, the model
is sufﬁcient for the immiscible ﬂuids assumed in the multicomponent ﬂows of interest.
The simulation of material interfaces is made possible by the volume-of-ﬂuid
method, which belongs to the broader class of interface-capturing schemes. One
common characteristic of these schemes is the relaxation of the natural sharpness
of material discontinuities. That is, the interfaces are allowed to numerically diffuse,
resulting in an interface region of small, but ﬁnite, thickness. Within this interface
region, a non-physical ﬂuid mixture exists, which is appropriately treated using
mixture rules that are deﬁned in § 2.2.1. For numerical stability purposes, material
interfaces are not initialized as sharp discontinuities, but are smeared over a few grid
cells. Based on previous results (Johnsen 2007; Coralic 2015) and sensitivity testing
by the authors for the speciﬁc problem of aerobreakup, this initial artiﬁcial smearing
over a few cells is known to have negligible impact on the computational results.
2.2.1. Equation of state
The ﬁve-equation model, (2.1), is closed with the speciﬁcation of an appropriate
equation of state (EOS) that relates the ﬂuid densities, pressures, and internal energies.
The stiffened gas EOS (Harlow & Amsden 1971), is used in our ﬂow solver to model
both gases and liquids:
p=(γ− 1)ρε−γ π∞, (2.2)
https://doi.org/10.1017/jfm.2017.804
 Published online by Cambridge University Press

<!-- PDF_PAGE: 6 -->

Numerical simulation of the aerobreakup of a water droplet 1113
Fluid ρ (kg m−3) c (m s−1) γ π∞ (Pa)
Air 1.204 343 1.40 0
Water 1000 1450 6.12 3 .43× 108
TABLE 1. Fluid properties at normal temperature and pressure.
where γ and π∞ are ﬁtting parameters that are empirically derived from ﬂuid shock
Hugoniot data. The consistent EOS sound speed is calculated as
c=
√
γ( p+ π∞)
ρ . (2.3)
Given that the modelled ﬂuids are considered to be immiscible, each ﬂuid in the solver
individually obeys the stiffened gas EOS. The properties for the ﬂuids of interest, air
and water, are tabulated in table 1. For air, π∞= 0 Pa, and the stiffened gas EOS
reduces to the ideal gas law with γ as the speciﬁc heat ratio. The ﬁtting parameters
for water are based on the shock Hugoniot data of Gojani et al. (2016), following the
ﬁtting procedure described in Johnsen (2007).
Within the diffuse interface region, mixture rules must be deﬁned for the properties
of ﬂuid mixtures. These mixture regions are an artefact of numerical diffusion, and
are not representative of mixing on a molecular level. For a system of two ﬂuids,
expressions of the mixture volume fraction, density, and internal energy are commonly
deﬁned as
1=αg+αl, (2.4)
ρ=αgρg+αlρl, (2.5)
ρε=αgρgεg+αlρlεl. (2.6)
We note that (2.4) and (2.5) do not affect the independence of (2.1 a) and (2.1 b).
Equations (2.1 a), (2.1 b) and (2.4) allow for the independent calculations of ρl and
ρg, while (2.5) is used with (2.1 c) to compute the velocity, u. Following previous
work, we deﬁne the following mixture rules for two functions of the stiffened gas
EOS ﬁtting parameters (Allaire et al. 2002):
Γ=αgΓg+αlΓl, Γ = 1
γ− 1, (2.7a,b)
Π∞=αgΠ∞,g+αlΠ∞,l, Π ∞= γ π∞
γ− 1. (2.8a,b)
2.2.2. Non-dimensionalization conventions
In our simulation, the ﬁve-equation model, (2.1), is solved in dimensionless form.
Unless otherwise speciﬁed, non-dimensionalization of the variables is done using the
initial droplet diameter D0, and post-shock gas velocity us, pressure p, and density ρs.
The resulting change in variables is
t∗= t us
D0
√ρs
ρl
, x∗= x
D0
, ρ ∗= ρ
ρs
, u∗= u
us
, p∗= p
ps
, (2.9a−e)
https://doi.org/10.1017/jfm.2017.804
 Published online by Cambridge University Press

<!-- PDF_PAGE: 7 -->

1114 J. C. Meng and T. Colonius
where the superscripted asterisk denotes a non-dimensional quantity. The additional
density ratio in the deﬁnition of t∗ results in a non-dimensional breakup time
ubiquitously found within the aerobreakup literature (e.g. Ranger & Nicholls 1968;
Simpkins & Bales 1972; Guildenbecher et al. 2009). This characteristic transport time
is ‘derived from analysis of the drop displacement assuming constant acceleration
due to drag ... ’ (Guildenbecher et al. 2009) and is ‘characteristic of drop breakup
by Rayleigh–Taylor or Kelvin–Helmholtz instabilities ... ’ (Pilch & Erdman 1987).
3. Numerical method
The Multicomponent Flow Code (MFC) is a research ﬂow solver capable of solving
the compressible Navier–Stokes equations for multicomponent ﬂows. The numerical
method, which is both shock and interface capturing, is based on the work on Johnsen
& Colonius (2006). Since its development, MFC has been used to study non-spherical
bubble collapse (Johnsen 2007; Johnsen & Colonius 2009) and shock-induced collapse
of bubbles inside deformable vessels (Coralic & Colonius 2013). Veriﬁcation of the
algorithm via benchmark test cases and parallel performance metrics have previously
been documented (Coralic & Colonius 2014; Coralic 2015; Meng 2016), and are not
reproduced here. Instead, we present only a high-level overview of the numerical
algorithm, and direct interested readers to the referenced publications for additional
details.
3.1. Spatial and temporal discretizations
The ﬁve-equation model, (2.1), is spatially discretized on a 3D cylindrical grid in the
following form:
∂q
∂t+∂f(q)
∂z +∂g(q)
∂r +∂h(q)
∂θ = s(q), (3.1)
where q is the vector of conservative variables, f(q), g(q), and h(q) are ﬂux vectors
in each of the coordinate directions, and s(q) is a source term vector (see details in
appendix A). In cylindrical coordinates, the divergence operator on an arbitrary vector
v=(vz,v r,vθ)T is
∇· v=∂vz
∂z+∂vr
∂r+vr
r+ 1
r
∂vθ
∂θ . (3.2)
Following Johnsen (2007), all vr/r terms are treated as geometrical source terms in
s(q). By discretizing the governing equations in this manner, the source terms account
for all cylindrical geometry effects. The axis singularity is treated following Mohseni
& Colonius (2000) with the deﬁnition of a new radial coordinate that spans both
positive and negative radius, i.e.
˜r(r,θ)=
{
r if 0 ⩽θ< π,
−r if π ⩽θ< 2π. (3.3)
Additional details of the numerical method, as well as its veriﬁcation and validation,
can be found in Meng (2016). Within the ﬁnite-volume formulation, the reconstruction
of the state variables at the cell boundaries is performed using a third-order weighted
essentially non-oscillatory (WENO) scheme developed for Cartesian coordinates.
Using the Cartesian WENO weights and polynomials, formal order of accuracy is
retained in the axial and radial coordinates, while not guaranteed in the azimuthal
coordinate. Convergence studies of the numerical method, however, show that
second-order accuracy is retained (Meng 2016). Finally, the system of equations
is temporally integrated using a third-order total variation diminishing Runge–Kutta
scheme.
https://doi.org/10.1017/jfm.2017.804
 Published online by Cambridge University Press

<!-- PDF_PAGE: 8 -->

Numerical simulation of the aerobreakup of a water droplet 1115
3.2. Modelling approximations and implications
The governing equations of § 2.2 are notably missing physical models for molecular
viscosity and surface tension. While the algorithms required to implement viscous and
capillary models in the governing equations are known (Meng 2016) (the ﬁve-equation
model of Allaire et al. (2002) was subsequently extended to include viscous effects
by Perigaud & Saurel (2005), and capillary effects can be modelled by including
additional source terms), the computational resources required for such a direct
numerical simulation are well beyond what is currently feasible. The present spatial
resolution of (Nz, Nr, Nθ)=(800, 600, 320) is already a grid with 1 .536× 108 cells.
For the high Reynolds numbers associated with aerobreakup in the SIE regime, the
grid resolution requirements to reach grid convergence would be extraordinary. As
an example, the axisymmetric work of Chang et al. (2013) employed an eight-level
adaptive mesh reﬁnement (AMR) scheme with an equivalent resolution of 800 points
per diameter. In order to sufﬁciently resolve the viscous boundary layer, the AMR
mesh had to be augmented with an additional body-ﬁtted structured conformal mesh
that had a spatial resolution of 4000 points per diameter. Taking even the coarsest
resolution requirement of 800 cells per diameter would be an increase by a factor of
8 from the present resolution. Additionally, while it is more difﬁcult to estimate a
precise grid requirement for capillary effects, a conservative estimate of a factor of 10
in each coordinate direction would result in a requirement of O(1014) grid points to
reach ab initio physical ﬁdelity. Even with AMR savings, we suspect this problem to
be intractable. Therefore, while the physics can be (and has been) implemented with
relative ease, the numerical viscosity would dominate these physical effects unless
the above spatial resolutions were somehow achieved.
Given that a compromise must be made, we consider the ‘inviscid’ case without
surface tension. Firstly, it is generally understood that so-called ‘inviscid’ simulations
using shock- and interface-capturing schemes, i.e. those performed without explicit
molecular viscosity modelling, inherently include numerical viscosity whose magnitude
is dependent on the spatial resolution. This compromise thus precludes providing
evidence of convergence, because such convergence will not exist when the ﬂow
becomes unstable and turbulent – the smallest length scales will be at the scale of
the grid. It is clear that at the present spatial resolution, we are unable to capture
ﬁne-scale instabilities that might arise on the droplet’s surface such as the KH
waves experimentally observed by Theofanous et al. (2012) (recall that Chang et al.
(2013) used a resolution of 4000 nodes per diameter to capture the viscous boundary
layer). It should be noted that an inability to capture these ﬁne-scale instabilities is
solely a consequence of the employed spatial resolution. Interfacial instabilities (at
least KH, RT, Richtmyer–Meshkov, and capillary) are driven by shear, which arises
even in ‘inviscid’ simulations. For a solid surface, the no-slip condition, which of
course requires the existence of viscosity, gives rise to shear, which in turn can drive
both viscous (e.g. Tollmien–Schlichting) and inviscid instabilities. In the interface
between two immiscible ﬂuids, the conservation of momentum requires equality of
the tangential viscous stresses, which in turn leads to a continuity of the velocity. In
the true inviscid limit, the ﬂuids would slip, but in the presence of any viscosity, and,
indeed, any artiﬁcial viscosity, the velocity is again continuous. This leads to shear
and, in turn, interfacial instabilities. With the exception of capillary instabilities, the
ﬁve-equation model can support all the other mentioned surface instabilities, though
they are not always adequately resolved.
The effects of surface tension in the aerobreakup problem become increasingly
important with time. In particular, capillary instabilities are of primary importance
https://doi.org/10.1017/jfm.2017.804
 Published online by Cambridge University Press

<!-- PDF_PAGE: 9 -->

1116 J. C. Meng and T. Colonius
when it comes to the disintegration of the thin sheets of liquid that are stripped
from the droplet’s periphery (discussed in § 4). In the absence of surface tension
modelling, there does not exist a numerical mechanism that approximates capillary
effects, i.e. there is no capillary counterpart to numerical viscosity. Without such a
mechanism, we do not capture the ultimate capillary-driven breakup mechanism of
a droplet undergoing aerobreakup. Instead, the actual mechanism of breakup in the
results is modelled in terms of numerical diffusion effects, i.e. breakup occurs as a
consequence of numerical diffusion and ﬁnite spatial resolution. Given this modelling
approximation, we expect the numerical results to have increasingly large uncertainties
as time progresses. Nevertheless, the agreement we ﬁnd with experimental results
suggests that the important mechanisms are captured; a deﬁnitive quantiﬁcation of
the error awaits future work.
While traditional grid convergence cannot be shown for the present numerical
results, we can estimate an approximate, effective Reynolds number associated
with the numerical viscosity for the given grid. A series of tests using 2D viscous
simulations (Meng & Colonius 2015; Meng 2016) indicate that the effective Reynolds
number is no less than 500 at the spatial resolution of our 3D simulation. While this
estimate is crude, and much lower than the corresponding experiments, it provides
some assurance that we are in the inertia-dominated regime, where we might expect
viscosity to play a small role at the scales of interest, at least at early times before
the ﬂow is fully turbulent and the droplet is disintegrated.
3.3. Droplet diagnostics
As the droplet undergoes aerobreakup, its centre-of-mass properties are of interest.
Taking advantage of the type of quantitative analysis allowed by simulations,
integral expressions have been derived (Meng & Colonius 2015) for the droplet’s
centre-of-mass velocity and acceleration that minimize unnecessary noise that would
be introduced by differentiating position data:
xc=
∫
Ω
αlρlx dV
∫
Ω
αlρl dV
, (3.4)
uc= dxc
dt =
∫
Ω
αlρlu dV
∫
Ω
αlρl dV
, (3.5)
ac= d2xc
dt2 =
∫
Ω
αlρla dV
∫
Ω
αlρl dV
, (3.6)
where the integrated volume is that of the entire computational domain, Ω. The liquid
partial density, αlρl, is then the parameter that restricts the integration to cells with
non-zero liquid volume fractions. Additional details of the derivations of (3.4)–(3.6)
can be found in Meng (2016). It should be noted that (3.5) and (3.6) are valid as
long as the liquid mass in the domain, ml=
∫
Ωαlρl dV, remains a constant; once liquid
mass ﬂux through the domain boundaries is non-zero, we terminate their calculation.
https://doi.org/10.1017/jfm.2017.804
 Published online by Cambridge University Press

<!-- PDF_PAGE: 10 -->

Numerical simulation of the aerobreakup of a water droplet 1117
Given that our volume-of-ﬂuid numerical method involves a diffuse interface that is
smeared across a few grid cells, isopleths and isosurfaces, representing the coherent
droplet body in the following numerical results, are shown for multiple values of the
liquid volume fraction, αl. The impact of various choices of αl on the interpretation
of the numerical results is explicitly discussed in the respective results sections.
Fortunately, the ambiguity in the exact interface location does not adversely impact
the conclusions that are drawn from our results.
4. Droplet morphology
The evolution of the deforming droplet as observed from our simulation is ﬁrst
described with an emphasis on the behaviour of the liquid phase. Figure 2 shows an
isometric view of isosurfaces of the liquid volume fraction. A quarter of the surface
has been removed to reveal the interior isosurfaces. From ﬁgure 2, we observe that
the morphology of the drop follows a distinct progression as the droplet is ﬂattened.
Initially, the deformed sphere takes on a mufﬁn-like shape, with the top of the mufﬁn
oriented upstream. That is, the upstream side of the droplet remains nearly spherical,
but is pushed into the liquid behind it, creating the mufﬁn lip. The downstream side
of the droplet is quickly compressed into a ﬂat plane and remains so for a signiﬁcant
portion of the breakup. Two liquid sheets are observed during this deformation. The
ﬁrst is the established liquid sheet drawn from the droplet equator, while the second
expands from the planar downstream side of the droplet. As the mufﬁn-shaped
droplet is compressed en masse , the liquid sheets eventually merge into a single
sheet emanating from the droplet periphery. From ﬁgure 3, we see that the present
spatial resolution is sufﬁcient to resolve this liquid sheet, even at late times in the
simulation. Since surface tension is not modelled, the disjoint interface is an artefact
of numerical diffusion and ﬁnite resolution. From the sequence of images in ﬁgure 2,
the liquid sheet is observed to radially ﬂap, and the dynamic liquid structure is
reminiscent of a swimming jellyﬁsh. Furthermore, this liquid sheet forms an envelope
for a large cavity that exists directly behind the ﬂattened drop. Theofanous et al.
(2012) experimentally observed this phenomenon (see ﬁgure 7) and described it
as ‘a cylindrical “curtain” around an empty space behind the coherent portion of
the drop.’ In the experiments, the curtain is composed of liquid fragments from the
disintegrating liquid sheet. Our simulation, in the absence of surface tension, is unable
to capture such a disintegration, though the small αl-isovalue needed to visualize the
sheet is indicative of its primarily gaseous composition. At approximately t∗= 0.681,
the axisymmetry of the liquid sheet is lost as instabilities arise on the surface in the
form of transverse azimuthal modulations, which are further discussed in § 5. At late
times in the breakup process, the larger αl-isosurfaces show the coherent droplet body
as a large thin disk-like shape.
4.1. Centre-of-mass properties
The droplet’s centre-of-mass drift, velocity, and acceleration in the streamwise (axial)
direction are plotted in ﬁgure 4. While the drift curve appears to be roughly parabolic,
the subsequent velocity and acceleration curves reveal that a constant acceleration
assumption would be erroneous. Focusing on the acceleration curve, the initial spike
in acceleration is the passage of the shock wave over the droplet. The maximum
acceleration occurs when the shock reﬂection on the droplet’s surface transitions from
a regular reﬂection to a Mach reﬂection. This is further discussed in § 4.3. Following
this initial spike, we note the existence of a brief period immediately following the
https://doi.org/10.1017/jfm.2017.804
 Published online by Cambridge University Press

<!-- PDF_PAGE: 11 -->

1118 J. C. Meng and T. Colonius
(a)( b)
(c)( d)
(e)( f )
(g)( h)
FIGURE 2. (Colour online) Isosurfaces of the liquid volume fraction, αl= 0.99, 0.50, 0.01
(orange, green, white). Flow is from top left to bottom right.
https://doi.org/10.1017/jfm.2017.804
 Published online by Cambridge University Press

<!-- PDF_PAGE: 12 -->

Numerical simulation of the aerobreakup of a water droplet 1119
 0.5
 0
 –0.5
 –1.0
 –1.5
1.0
1.5 0 0.5 1.0 1.5 2.0 2.5–0.5
0.90
0.99
 0.75
0.50
 0.25
0.10
0.01
0.5
0
–
0.5
–
1.0
–
1.5
0
 0.5
 1.0
 1.5
 2.0
 2.5
–
0.5
0.90
0.99
 0.75
0.50
0.25
0.10
0.01
FIGURE 3. (Colour online) Sliced isopleths of αl at t∗= 0.799 shown on the computational
grid at 1 : 5 of the actual resolution.
passage of the shock when the droplet is subject to constant acceleration. During this
time period, the droplet is adjusting to the step change in ambient ﬂow conditions,
and is still well-approximated as a rigid sphere. This delay, which is not observed in
2D simulations (Meng & Colonius 2015) and is, perhaps, related to the ﬂow-relieving
effect of the third dimension, ceases when the droplet begins to pancake and its drag
properties substantially change. Secondly, a dominant low-frequency oscillation is
observed in the droplet’s acceleration curve. In ﬁgure 5, we replot the acceleration
curve using standard convective time units for ﬂow past a rigid sphere, tus/D0, to
check if this low frequency corresponds with wake instability. The vertical gridlines
are spaced 5 D0/us apart to coincide with the expected period of a wake instability
(vortex shedding) which, for ﬂow over a rigid sphere, occurs with Strouhal number
St= fD0/us= 0.2. The largest oscillations in the acceleration are roughly commensurate
with this frequency, but owing to the relatively short data available, it is difﬁcult to
draw a ﬁrm conclusion.
Finally, ﬁgure 5( b) shows the droplet’s unsteady drag coefﬁcient, CD. The frontal
area used in the non-dimensionalization assumes a circular upstream projected area
based on the droplet’s deformed diameter, Dd. From ﬁgure 2, this assumption is seen
to be a reasonable approximation for the times shown in ﬁgure 5. Dd is taken as the
maximal spatial extents in the ˜r-coordinate, which depends on the choice of αl. Thus,
in ﬁgure 5, we show bounds for the CD spanning 0.25 ⩽αl ⩽ 0.99. For t∗< 0.3, the
choice of αl has little impact on the CD. During the period of constant acceleration,
and before the droplet has had sufﬁcient time to signiﬁcantly deform, we observe that
the drag coefﬁcient for a rigid sphere, CD= 0.5, is approximately recovered. As the
droplet begins pancaking, the drag coefﬁcient transitions to be comparable to that for
https://doi.org/10.1017/jfm.2017.804
 Published online by Cambridge University Press

<!-- PDF_PAGE: 13 -->

1120 J. C. Meng and T. Colonius
0.05
 0.10
0.15
 0.20
0.25
0.30
0.35
0 0.2 0.4 0.6 0.8
0.06
 0.01
0.02
0.03
0.04
0.05
5
6
7
8
9
3
2
1
4
0 0.2 0.4 0.6 0.8 0 0.2 0.4 0.6 0.8
(a)( b) (c)
FIGURE 4. Droplet streamwise centre-of-mass ( a) drift, ( b) velocity, and ( c) acceleration.
5
6
7
8
9
3
2
1
4
0 5 10 15
5
3
2
1
4
0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8
(a)( b)
FIGURE 5. (Colour online) Droplet ( a) acceleration in convective time units and ( b)
unsteady drag coefﬁcient for a range of Dd (dependent upon choice of αl).
a ﬂat disk, which has CD≈ 1. For t∗> 0.3, CD depends more strongly on choice
of αl-value, representing the uncertainty in the deformed diameter. Unsteady effects
begin to dominate and the drag coefﬁcient subsequently exhibits ﬂuctuations about an
increasing average value. While it is impossible to state the true value of CD, the
oscillatory behaviour (present also in the acceleration time history) is believed to be
physical, and the plot is thought to reasonably bound the physical values at late times.
4.2. Comparison with experimental visualizations
We now compare the simulated breakup with the experimental visualizations of
Theofanous et al. (2012). They studied the breakup of water droplets (among other
liquids) in a helium shock tube. Given the uncertainty in the exact interface location
and the numerical diffusion of the material discontinuity, we compare the experimental
images to both the αl= 0.01 isosurface and sliced isopleths for various αl-values.
Despite a mismatch in ﬂow conditions and a dearth of timing data, our numerical
https://doi.org/10.1017/jfm.2017.804
 Published online by Cambridge University Press

<!-- PDF_PAGE: 14 -->

Numerical simulation of the aerobreakup of a water droplet 1121
FIGURE 6. (Colour online) Comparisons with experimental visualizations of the
aerobreakup of a water droplet from ﬁgure 33 of Theofanous et al. (2012). Flow is
from right to left. Each frame consists of an experimental image reproduced from the
video stored online (https://doi.org/10.1063/1.3680867.12) (left), the numerical αl= 0.01
isosurface (centre), and sliced isopleths of αl (right) corresponding to the legend in
ﬁgure 3. The timing information is for the numerical results; no experimental timing
information is available.
results show good qualitative agreement with the experimental visualizations of the
SIE phenomenology. The small value of the αl-isosurface is believed to be a fair
comparison for visualization purposes, as the experimental images are also obscured
by the ﬁne mist that is generated during breakup. Additionally, comparisons with the
sliced isopleths conﬁrm a qualitative agreement largely independent of the numerics.
The post-shock ﬂow in the experiment has a Mach number of 0.32, which
corresponds to experimental Reynolds and Weber numbers of Re= 2.2× 104 and
We= 780. The large Reynolds and Weber numbers allow us to make qualitative
comparisons with our numerical results. This comparison is shown in ﬁgure 6. First,
we observe the same initial deformation of the droplet into a mufﬁn-like shape.
The upstream side of the droplet remains spherical, while the downstream side is
ﬂattened into a planar surface. What appears to be a thin liquid sheet coming from
the spherical lip is visible beginning at t∗= 0.162. This sheet quickly disintegrates
into a mist that obscures the coherent part of the droplet. The coherent droplet body
is continually ﬂattened in the streamwise direction, and liquid material is constantly
stripped off near its equator. At late times in the SIE process, the liquid fragments
form a cylindrical curtain around a cavity behind the coherent droplet. In ﬁgure 7,
we compare experimental and numerical images of this liquid sheet. As discussed
in § 3.2, we do not capture the ultimate capillary-driven breakup of the liquid sheet.
https://doi.org/10.1017/jfm.2017.804
 Published online by Cambridge University Press

<!-- PDF_PAGE: 15 -->

1122 J. C. Meng and T. Colonius
(a)( b) (c)
FIGURE 7. (Colour online) Comparison of experimental and numerical liquid ‘curtains.’
The experimental image taken from ﬁgure 17( b) of Theofanous et al. (2012) ( a) is for
Mach 0.59 ﬂow at t∗= 0.81. The numerical isosurface of αl= 0.01 (b) and sliced isopleths
of αl (c) are for Mach 0.5775 ﬂow at t∗= 0.808. Isopleth colours correspond to the legend
in ﬁgure 3.
Though these experimental comparisons are not without uncertainty, we ﬁnd that our
numerical results are, by and large, not far off from the experimental visualizations
of the SIE regime.
4.3. Flow ﬁeld in the gas
From their experimental results, Liu & Reitz (1997) proposed a rough classiﬁcation
of the breakup process into two stages. They experimentally observed the ﬁrst stage
as a pressure-driven shape change of the droplet. This deformation stage, shared
amongst multiple breakup regimes, is characterized by a ﬂattening of the droplet
in the streamwise direction. This pancaking is a consequence of the non-uniform
pressure distribution around the droplet surface. High pressures at the forward and
rear stagnation points, as well as low pressures at the equator due to the acceleration
of the gas, both contribute to the ﬂattening of the droplet. The second stage, as
described by Liu & Reitz (1997), is characterized by droplet disintegration and is
when the phenomenology diverges for the various breakup regimes. For the stripping
regime, they observed the edges of the droplet being drawn out into a thin liquid
sheet by drag forces, and the subsequent breakup of the sheet into ﬁne ligaments.
Contrary to Liu & Reitz’s description of the breakup process as two consecutive
stages, our numerical results suggest that the phenomenology of stripping may be
better described as the simultaneous ﬂattening and stripping of liquid material. In
fact, not only are the ﬂattening and the disintegration processes occurring concurrently
throughout the breakup process, they are also intricately connected by the dynamic
behaviour of the surrounding gas ﬂow.
In order to elucidate why the liquid behaves as it does, we look to the behaviour
of the surrounding gas ﬂow as visualized in ﬁgures 8 and 9 (images are ordered
top to bottom, left to right). Figure 8 shows 2D slices taken through the centre of
the droplet, x∗, y∗= 0, that are offset for unobstructed viewing of both planes. The
vertical plots are coloured by velocity magnitude normalized by the post-shock gas
velocity,∥u∥∗, while the horizontal plots are coloured by pressure, p∗. Isopleths of
the numerical schlieren function, ϕ, reveal the intricate and dynamic ﬂow structures
that develop in the wake. Following Quirk & Karni (1996), the numerical schlieren
function is computed as the exponential of the negative, normalized density gradient
ϕ= exp
(
−β ∥∇ρ∥
∥∇ρ∥max
)
, (4.1)
https://doi.org/10.1017/jfm.2017.804
 Published online by Cambridge University Press

<!-- PDF_PAGE: 16 -->

Numerical simulation of the aerobreakup of a water droplet 1123
0 1.5
(a)( b)
(c)( d)
(e)(  f )
(g)( h)
FIGURE 8. (Colour online) Filled contour slices of velocity magnitude, ∥u∥∗, and pressure,
p∗, and isopleths of the numerical schlieren function. Flow is from bottom left to top right.
Offset 2D slices are taken at x∗= 0, y∗= 0.
whereβ is a scaling parameter that allows simultaneous visualization of waves in both
ﬂuids. Following Johnsen (2007), βair= 40 and βwater= 400. The three-dimensionality
of the aerobreakup process is well captured in ﬁgure 9, which plots various isosurfaces
of azimuthal vorticity, ωθ. Since the innermost regions of the ﬂow are obstructed from
view, slices are again taken through the centre of the drop and offset to both sides.
The transverse slice, offset upstream of the droplet, is taken at z∗= 1.
https://doi.org/10.1017/jfm.2017.804
 Published online by Cambridge University Press

<!-- PDF_PAGE: 17 -->

1124 J. C. Meng and T. Colonius
(a)( b)
(c)( d)
(e)(  f )
(g)( h)
FIGURE 9. (Colour online) Isosurfaces of positive (red) and negative (blue) azimuthal
vorticity, ωθ. Flow is from top left to bottom right. Offset 2D slices are taken at x∗=
0, y∗= 0, z∗= 1.
The incident and reﬂected shock waves, as well as the secondary wave system
generated by the convergence of Mach stems at the rear stagnation point, are visible
in the ﬁrst few snapshots of ﬁgure 8. The peak drag of the droplet is marked by
the transition of the reﬂected shock from a regular reﬂection to a Mach reﬂection
at some inclination angle preceding the droplet equator. This phenomenon has been
studied in the literature for rigid cylinders and spheres (Takayama & Itoh 1986; Tanno
et al. 2003), and is also observed in the case of 2D aerobreakup (Meng & Colonius
2015). Promptly after the passage of the incident shock, the ﬂow is accelerated to
https://doi.org/10.1017/jfm.2017.804
 Published online by Cambridge University Press

<!-- PDF_PAGE: 18 -->

Numerical simulation of the aerobreakup of a water droplet 1125
approximately 1.5us at the droplet’s equator (pink colouring is visible at t∗= 0.044 in
ﬁgure 8), which is the value expected from potential ﬂow theory for ﬂow past a rigid
sphere. In the early stages of droplet deformation, t∗ ⩽ 0.435, the transmitted wave that
propagates into the liquid from the incident shock wave is observed to bounce back
and forth within the droplet. From our numerical results and the aerobreakup literature,
this transmitted wave inside the liquid droplet is not thought to play a signiﬁcant role
in the aerobreakup process.
As discussed earlier, the non-uniform pressure distribution around the droplet is the
principal mechanism driving droplet deformation. This is clearly seen in the ﬁlled
pressure contours of ﬁgure 8. Unlike the case of steady separated ﬂow past a rigid
sphere, the pressure at the rear stagnation point remains, during the initial ﬂattening,
larger than the pressure at the droplet’s equator.
The equatorial recirculation region, visible in ﬁgure 9, is formed by the interaction
of two opposite-sign azimuthal vorticity streams generated by baroclinicity. The
formation of this equatorial recirculation region has previously been observed to also
occur for 2D aerobreakup (Meng & Colonius 2015). Its location coincides with the
sides of the mufﬁn-shaped droplet behind the lip of the spherical upstream droplet
surface. This equatorial recirculation region thus serves as a possible explanation for
the mufﬁn-like shape of the deformed droplet, and, for the duration of its existence,
is at least partially responsible for the liquid sheets that are drawn out from both the
spherical lip and the planar back of the droplet.
Other notable ﬂow features visible in ﬁgure 8 include a wake recirculation region
and two concentric shear layers at the droplet equator. Behind the droplet, the wake
recirculation region is quickly established, as evidenced by the departure of the ﬂow
reversal region (i.e. the white patch in the wake directly behind the droplet where the
streamwise velocity changes direction) from the rear stagnation point at t∗= 0.099
in ﬁgure 8 (at t∗= 0.126 in ﬁgure 9, the wake recirculation region already exists).
The ﬂow reversal patch also serves to demarcate the end of an upstream jet that is
created in the wake. The wake recirculation region is bounded by shear layers that are
subject to KH instability, and the unsteady vortex shedding drives the development
of a complicated wake. KH roll-up and subsequent vortex shedding from the shear
layers can be seen particularly clearly from the numerical schlieren isopleths at t∗=
0.435, 0.544, 0.781 in ﬁgure 8.
For clarity, it would be ideal if the aforementioned ﬂow phenomena could be
discussed separately as distinct ﬂow features. However, in reality, they are so
interconnected that such a disjointed discussion would be both incomplete and overly
simplistic. In the remainder of this section, we attempt a comprehensive examination
and discussion of these ﬂow phenomena.
The formation of the wake recirculation region initiates a strongly coupled,
self-sustaining set of ﬂow phenomena that evolve with ever-increasing complexity.
The wake recirculation region, created by the stream of negative azimuthal vorticity
from the upstream side of the droplet, remains in the near-ﬁeld wake region. It is
perpetually sustained by the same vorticity stream, and entrains the surrounding ﬂuid,
which is pulled into an upstream jet that impinges on the rear stagnation point of the
droplet.
This upstream jet, driven by the recirculation region, preserves high pressure at the
rear stagnation point that contributes to both the pancaking of the coherent droplet,
as well as the generation of positive vorticity along the back of the droplet. The
positive vorticity is transported towards the equator by the recirculation region, and
interacts with the negative vorticity stream to create, at early times, the equatorial
https://doi.org/10.1017/jfm.2017.804
 Published online by Cambridge University Press

<!-- PDF_PAGE: 19 -->

1126 J. C. Meng and T. Colonius
recirculation region. Some positive vorticity is also transported downstream, forming a
parallel stream inside the negative vorticity stream coming from the upstream side of
the droplet. The shear ﬂow that is created when the upstream jet impinges on the back
of the droplet may also contribute to the liquid sheet that arises from the downstream
side.
As the equatorial liquid sheet is blown downstream by inertial forces from the
surrounding gas ﬂow, shear layers are formed on both sides of the sheet. The gas
that is accelerating around the droplet creates shear on the exterior, while the wake
recirculation region, that exists inside the cavity enveloped by the sheet, creates shear
along the interior. Both the interior and exterior shear layers are visible in ﬁgure 8.
As the liquid sheet ﬂaps, generating longitudinal ripples, the shear layers, which are
subject to KH instability, periodically shed vortices that are either entrained by the
wake recirculation region, or are convected downstream. Entrained vortices (of both
signs) by the wake recirculation region result in the upstream jet being characterized
by concentric layers of alternating vorticity sign (visible from t∗= 0.535–0.781 in
ﬁgure 9). Entrainment of shed vortices is also associated with a temporary increase in
upstream jet velocity that results in a cyclic pumping of ﬂuid onto the back side of
the droplet. Downstream-convected vortices, that are not entrained, quickly lose their
initial axisymmetry due to the instability of vortex rings, and subsequently develop
into fully 3D ﬂow features.
In time, as the liquid sheet is drawn downstream and the coherent droplet diameter
expands laterally, the ﬂow within the enveloped cavity at the back of the droplet,
encompassing the wake recirculation region and the upstream jet, correspondingly
grows in size and complexity. Loss of axisymmetry is observed to ﬁrst occur
in the core region of wake, i.e. small r. However, before it radially expands to
encompass the entire wake region, another instability is observed to emerge along
the still-axisymmetric positive vorticity sheet (located just inside the equatorial
liquid sheet). From t∗= 0.754–0.781 in ﬁgure 9, we see what appear to be RT
ﬁngers or mushroom-like features propagating inwards towards the core that cause
azimuthal rippling in the previously axisymmetric vorticity sheet. This instability,
further discussed in § 5, generates the transverse azimuthal modulations observable
on the liquid sheet visible for t∗ ⩾ 0.808 in ﬁgure 2. As the entire wake region
devolves into chaotic, turbulent-like ﬂow, the general coherence of the aforementioned
phenomena is lost, as seen for t∗ ⩾ 1.054 in ﬁgure 9. At these late times, the coherent
droplet body presents an essentially blunt body to the oncoming free-stream ﬂow such
that the highest pressures are found on the upstream side of the ﬂattened disk-like
droplet.
5. Surface instabilities and transition
5.1. Mechanism of instability
The upstream side of a droplet undergoing aerobreakup is susceptible to RT instability
waves that arise from the acceleration of the lighter gas into the denser liquid. In the
classical catastrophic breakup regime, ‘ﬁngers of hot air’ were thought to penetrate
the droplet, leading to an explosive disintegration (Joseph et al. 1999). In contrast
stands the recent of work of Theofanous & Li (2008) who observed that ‘[t]here are
no RT waves piercing the drop ... ’ Indeed, no RT waves are seen on the droplet in
our numerical simulation. This is shown in ﬁgure 10, where the upstream side of the
drop for various isopleths of αl remains smooth for the entirety of the simulation.
Our numerical results thus support Theofanous & Li’s claim of SIE being the
https://doi.org/10.1017/jfm.2017.804
 Published online by Cambridge University Press

<!-- PDF_PAGE: 20 -->

Numerical simulation of the aerobreakup of a water droplet 1127
0.5
0
–0.5
–1.0
–1.5
1.0
1.5
0.5
0
–0.5
–1.0
–1.5
1.0
1.5
0 0.5 1.0 1.5 2.0 2.5–0.5 0 0.5 1.0 1.5 2.0 2.5–0.5 0 0.5 1.0 1.5 2.0 2.5–0.5
0.99
0.90
0.75
0.50
0.10
0.25
0.01
FIGURE 10. (Colour online) Sliced isopleths of αl showing droplet proﬁles.
terminal breakup regime. The suppression of the RT instability waves was initially
explained by Theofanous & Li (2008) to be a consequence of the stability of the
stagnation ﬂow (reminiscent of the lenticular shape of a gas bubble rising through
liquid (Batchelor 1987)). More recently, an analysis of the viscous KH instability by
Theofanous et al. (2012) found that ‘[w]ave numbers and growth factors of [KH]
instability are consistently greater than those of [RT] instability by more than an order
of magnitude... [T]he stretching further contributes to keeping this area molliﬁed and
free of any instability all the way to the end.’
In describing the instabilities that arise on the liquid sheet that lead to its
disintegration, Liu & Reitz (1997) proposed the ‘stretched streamwise ligament
breakup’ mechanism of Stapper & Samuelsen (1990). This breakup mechanism is
characterized by the dominant formation and growth of streamwise vortical waves
on the sheet, with thin membranes formed between them. ‘Breakup occurs as the
membranes are stretched thin by the rotation of the streamwise vortices and burst
into small droplets. The streamwise vortical waves separate as streamwise ligaments,
stretch and spin faster in the presence of the air shear, and eventually break up,
contributing the larger drops to the ﬁnal drop size distribution’ (Stapper & Samuelsen
1990). From ﬁgure 11, which plots transverse slices of the liquid sheet at various
streamwise locations, we see that our numerical results do not support this mechanism
as the reason for sheet disintegration. Instead of a liquid sheet with variable thickness
in the azimuthal coordinate, we observe relatively constant sheet thickness, and a
rippling-type instability. Additionally, isosurfaces of the liquid sheet coloured by axial
and radial vorticity, ω∗
z,r=ωz,rD0/us, (as shown in ﬁgure 12) suggest that streamwise
(axial) vorticity (with its smaller magnitude) does not play a dominant role in the
sheet breakup. It should be noted here that while ﬁgures 11 and 12 are plotted
https://doi.org/10.1017/jfm.2017.804
 Published online by Cambridge University Press

<!-- PDF_PAGE: 21 -->

1128 J. C. Meng and T. Colonius
0.5
0
–0.5
–1.0
–1.5
1.0
1.5
0 0.5 1.0 1.5 2.0
z
r
FIGURE 11. (Colour online) Transverse slices of the liquid sheet at t∗= 0.881, deﬁned
by αl= 0.01, at various streamwise locations.
0
10
–10
FIGURE 12. (Colour online) The liquid sheet coloured by axial and radial vorticity, ω∗
z,r,
at t∗= 0.808.
using the αl= 0.01 isosurface, the sheet thickness is still relatively constant in the
azimuthal coordinate for other values of αl (visible from ﬁgure 10), and the relative
importance of ω∗
z is unchanged by the choice of αl. In addition to the ‘stretched
streamwise ligament’ mechanism of sheet breakup, Liu & Reitz (1997) also proposed
another rippling mechanism based on mass conservation arguments. Though this
remains a possibility, the observed phenomena are most likely the net result of
several mechanisms. Given the modelling approximations and implications discussed
in § 3.2, no physical length scales can be associated with the instabilities that are
observed in the numerical results. Instead, we are limited to qualitatively describing
the observed phenomena.
Jalaal & Mehravaran (2014) proposed the RT instability as the source of the
transverse azimuthal modulations. Arguing that the accelerated liquid sheet is subject
https://doi.org/10.1017/jfm.2017.804
 Published online by Cambridge University Press

<!-- PDF_PAGE: 22 -->

Numerical simulation of the aerobreakup of a water droplet 1129
FIGURE 13. (Colour online) Filled contours and isopleths of gas partial density, αgρg, at
z∗= 1. Darker colours correspond to larger densities (colouring and isopleth values vary
between frames).
to the same instability as that which forms streamwise ligaments in the case of a
round liquid jet in coaxial ﬂow, they attempted a quantitative comparison with theory,
but found only marginal agreement. The general concept, though, of RT instability
on the liquid sheet may, indeed, have merit, and supporting (qualitative) evidence
can be found in our numerical results. As noted at the end of § 4.3, RT ﬁngers or
mushroom-like features are seen emerging along the positive vorticity sheet that lies
just inside the equatorial liquid sheet. To relate these features to the RT instability, we
plot ﬁlled contours and isopleths of the gas partial density for late times in ﬁgure 13.
At t∗= 0.726, the axisymmetry of the outer regions of the wake is still preserved, as
https://doi.org/10.1017/jfm.2017.804
 Published online by Cambridge University Press

<!-- PDF_PAGE: 23 -->

1130 J. C. Meng and T. Colonius
10–2
10–4
10–6
10–8
100
102
104
0 0.2 0.4 0.6 0.8 1.0 1.2
FIGURE 14. (Colour online) L2-norm of the (kinetic) energy (see (5.1)) for each of the
Nθ/2 modes resulting from the azimuthal Fourier decomposition of the velocity ﬁeld.
evidenced by the circular isopleths. From t∗= 0.744–0.790, however, the axisymmetry
is broken by multiple ﬁngers of denser gas propagating towards the axis into the
lighter gas (darker colours correspond to larger densities). These ﬁngers correspond
exactly with the indentations generated on the liquid sheet. Not long after this loss of
outer axisymmetry, the entire wake region degenerates into a chaotic, turbulent-like
ﬂow with complete loss of ﬂow feature coherence.
5.2. Azimuthal Fourier decomposition
Motivated by the observed azimuthal modulations, we perform a Fourier decomposition
of the velocity ﬂow ﬁeld to determine if a particular mode(s) or wavenumber(s) is
associated with the loss of axisymmetry. To do this, we take a Fourier transform in
the θ-coordinate to obtain the Fourier coefﬁcients of each of the azimuthal modes,
ˆum(z, r, t). We then calculate an energy metric for each mode deﬁned as
ˆκm=|ˆuz,m|2+|ˆur,m|2+|ˆuθ,m|2, (5.1)
where the hat denotes the Fourier transform in the θ-coordinate. Taking an L2-norm
of ˆκm over the entire computational domain, we plot the time histories of ∥ˆκm∥2 for
each of the Nθ/2 modes (excluding the mean) in ﬁgure 14. Notably, the frequency
response of the system shows broadband instability growth for all modes. An initial
jolt applied to the system by the passage of the shock wave is mostly stabilized
after approximately t∗= 0.1. This is followed by the exponential growth of nearly all
wavenumbers. If we view the interaction of the incident shock with the droplet as
an impulsive force applied to the system, the broadband instability response is not
surprising. Four of the modes appear to exhibit a different type of behaviour; however,
these unusual curves are actually artefacts of the random velocity perturbations
seeded in the initial condition. Unfortunately, due to the unsteady, non-stationary, and
https://doi.org/10.1017/jfm.2017.804
 Published online by Cambridge University Press

<!-- PDF_PAGE: 24 -->

Numerical simulation of the aerobreakup of a water droplet 1131
FIGURE 15. (Colour online) Isosurfaces of κm, m= 1, 2, 4, 6, 8 at t∗= 0.808, 0.935. Also
shown is a cut isosurface of the liquid sheet visualized using αl= 0.01. Front and side
views are shown, and isosurface values change between frames.
nonlinear nature of the aerobreakup problem, this type of instability analysis is unable
to pick out a dominant mode or wavenumber associated with the loss of axisymmetry.
Despite the broadband response, visualization of the ﬁrst few modes transformed back
into θ-space, κm= u2
z,m+ u2
r,m+ u2
θ,m, reveals some interesting observations about the
development of the wake, and offers some general intuition about the physical spatial
structure of κm. Figure 15 shows the isosurfaces of a few modes at late times in
the simulation, t∗= 0.808, 0.935, when all frequencies have saturated (see ﬁgure 14).
From ﬁgure 15, we see that the structures are initially clustered around the location
https://doi.org/10.1017/jfm.2017.804
 Published online by Cambridge University Press

<!-- PDF_PAGE: 25 -->

1132 J. C. Meng and T. Colonius
of the liquid sheet, and subsequently grow in size and complexity. Even at late times,
the structures remain bounded by the wake region. Streaky streamwise-oriented ﬂow
structures near the wake core, visible for κ6,8 at t∗= 0.808, appear to be related to the
loss of axisymmetry in the upstream jet region, while the outer structures are linked
to the liquid sheet and shear layers. As this broadband instability is not directly
associated with any classical hydrodynamic instability, we are unable to relate these
κm-structures to other recognizable ﬂow features.
6. Conclusions
In this paper, we have presented the ﬁrst detailed description of the underlying
ﬂow physics associated with droplet deformation during stripping aerobreakup. The
droplet morphology is ﬁrst described and compared to experimental visualizations of
the SIE process. Good qualitative agreement is found in terms of the droplet’s initial
deformation into a mufﬁn-like shape, followed by the disintegration of a liquid sheet
that envelops a cavity in the near-ﬁeld wake region.
The droplet’s centre-of-mass properties reveal signiﬁcant unsteadiness in the
droplet’s acceleration, which oscillates with a frequency that roughly matches the
Strouhal number associated with wake instability. Limitations on the available data,
however, make it difﬁcult to draw a ﬁrm conclusion. The droplet’s unsteady drag
coefﬁcient, when normalized using the deformed droplet diameter, brieﬂy recovers
that for a rigid sphere during the very early stages of aerobreakup. Subsequently, the
droplet’s deformation alters its drag properties and unsteady effects become dominant
as the drag coefﬁcient oscillates about an increasing average value.
Numerical visualizations of the surrounding ﬂow behaviour provide insights into
the experimentally observed drop morphology. At early times, the existence of the
equatorial recirculation region, comprised of two counter-rotating vortices, explains
both the mufﬁn-like shape, and the pulling of liquid sheets from both the droplet’s
equator and its ﬂattened back. The enveloped cavity attached to the downstream side
of the deforming droplet is associated with a recirculation region that entrains ﬂuid
and jets it upstream to impinge on the rear stagnation point. The shear layers that
form on both sides of the liquid sheet are subject to KH instability, and shed vortices
that are either convected downstream or entrained by the wake recirculation region. RT
instability waves on the upstream side of the droplet are noticeably absent, providing
support for SIE as the terminal breakup regime.
Analyses of the instabilities arising on the liquid sheet reveal discrepancies with the
proposed ‘stretched streamwise ligament breakup’ mechanism, while some qualitative
evidence for the rise of RT instability along the accelerated sheet can be found. An
attempt is made to ﬁnd particular modes associated with the loss of axisymmetry by
performing an azimuthal Fourier decomposition of the ﬂow ﬁeld. Unfortunately, due to
the unsteady and nonlinear nature of the aerobreakup problem, this analysis is limited
in its efﬁcacy, and instead shows broadband instability growth of all modes, as would
be expected from impulsive forcing of the system.
Acknowledgements
The authors gratefully acknowledge discussions with Professor G. Blanquart, and
Drs V . Coralic and O. Schmidt. We also thank K. Maeda for his many important
suggestions on the numerical algorithm and for help in implementing the code. The
computation presented here utilized the Extreme Science and Engineering Discovery
Environment, which is supported by the National Science Foundation. This work was
partially supported by the National Institutes of Health under grant 2P01-DK043881.
https://doi.org/10.1017/jfm.2017.804
 Published online by Cambridge University Press

<!-- PDF_PAGE: 26 -->

Numerical simulation of the aerobreakup of a water droplet 1133
Appendix A. State variables, ﬂuxes, and source terms
The vector of conservative variables, q:
q=


α1ρ1
α2ρ2
ρuz
ρur
ρuθ
E
α1


. (A 1)
The ﬂux vectors, f(q), g(q) and h(q):
f(q)=


α1ρ1uz
α2ρ2uz
ρu2
z+ p
ρuruz
ρuθuz
(E+ p)uz
α1uz


, g(q)=


α1ρ1ur
α2ρ2ur
ρuzur
ρu2
r+ p
ρuθur
(E+ p)ur
α1ur


, h(q)= 1
r


α1ρ1uθ
α2ρ2uθ
ρuzuθ
ρuruθ
ρu2
θ+ p
(E+ p)uθ
α1uθ


. (A 2a−c)
The source term vector, s(q):
s(q)=− 1
r


α1ρ1ur
α2ρ2ur
ρuzur
ρ(u2
r− u2
θ)
2ρuruθ
(E+ p)ur
α1(ur− r∇· u)


. (A 3)
The velocity divergence term in s(q) is necessary to adapt the non-conservative form
of (2.1 e) to the Riemann solver (Johnsen & Colonius 2006).
REFERENCES
AALBURG , C. , LEER , B. V. & FAETH , G. M. 2003 Deformation and drag properties of round drops
subjected to shock-wave disturbances. AIAA J. 41 (12), 2371–2378.
ALLAIRE , G. , CLERC , S. & KOKH , S. 2002 A ﬁve-equation model for the simulation of interfaces
between compressible ﬂuids. J. Comput. Phys. 181, 577–616.
BATCHELOR , G. K. 1987 The stability of a large gas bubble rising through liquid. J. Fluid Mech.
184, 399–422.
CASTRILLON ESCOBAR , S. , RIMBERT , N. , MEIGNEN , R. , HADJ -ACHOUR , M. & GRADECK , M.
2015 Direct numerical simulations of hydrodynamic fragmentation of liquid metal droplets by
a water ﬂow. In 13th Triennial International Conference on Liquid Atomization and Spray
Systems. ILASS.
CHANG , C. H., D ENG , X. & T HEOFANOUS , T. G. 2013 Direct numerical simulation of interfacial
instabilities: a consistent, conservative, all-speed, sharp-interface method. J. Comput. Phys. 242,
946–990.
CHEN , H. 2008 Two-dimensional simulation of stripping breakup of a water droplet. AIAA J. 46 (5),
1135–1143.
https://doi.org/10.1017/jfm.2017.804
 Published online by Cambridge University Press

<!-- PDF_PAGE: 27 -->

1134 J. C. Meng and T. Colonius
CORALIC , V. 2015 Simulation of shock-induced bubble collapse with application to vascular injury
in shockwave lithotripsy. PhD thesis, California Institute of Technology, Pasadena, CA.
CORALIC , V. & COLONIUS , T. 2013 Shock-induced collapse of a bubble inside a deformable vessel.
Eur. J. Mech. ( B/Fluids) 40, 64–74.
CORALIC , V. & COLONIUS , T. 2014 Finite-volume WENO scheme for viscous compressible
multicomponent ﬂows. J. Comput. Phys. 274, 95–121.
ENGEL , O. G. 1958 Fragmentation of waterdrops in the zone behind an air shock. J. Res. Natl Bur.
Stand. 60 (3), 245–280.
GOJANI , A. B. , OHTANI , K. , TAKAYAMA , K. & HOSSEINI , S. H. R. 2016 Shock Hugoniot and
equations of states of water, castor oil, and aqueous solutions of sodium chloride, sucrose,
and gelatin. Shock Waves 26 (1), 63–68.
GUILDENBECHER , D. R. , LÓPEZ -R IVERA , C. & SOJKA , P. E. 2009 Secondary atomization. Exp.
Fluids 46, 371–402.
HAN, J. & TRYGGVASON , G. 2001 Secondary breakup of axisymmetric liquid drops. Part II. Impulsive
acceleration. Phys. Fluids 13 (6), 1554–1565.
HANSON , A. R. , DOMICH , E. G. & ADAMS , H. S. 1963 Shock tube investigation of the breakup
of drops by air blasts. Phys. Fluids 6 (8), 1070–1080.
HARLOW , F. H. & A MSDEN , A. A. 1971 Fluid dynamics. Tech. Rep. LA-4700. LASL.
HINZE , J. O. 1949 Critical speeds and sizes of liquid globules. Appl. Sci. Res. A1, 273–288.
HSIANG , L. P. & FAETH , G. M. 1992 Near-limit drop deformation and secondary breakup. Intl J.
Multiphase Flow 18 (5), 635–652.
HSIANG , L. P. & FAETH , G. M. 1995 Drop deformation and breakup due to shock wave and steady
disturbances. Intl J. Multiphase Flow 21 (4), 545–560.
IGRA , D. & TAKAYAMA , K. 2001a Experimental and numerical study of the initial stages in the
interaction process between a planar shock wave and a water column. In 23rd International
Symposium on Shock Waves . The University of Texas at Arlington.
IGRA , D. & TAKAYAMA , K. 2001b Numerical simulation of shock wave interaction with a water
column. Shock Waves 11, 219–228.
IGRA , D. & TAKAYAMA , K. 2001c A study of shock wave loading on a cylindrical water column.
Tech. Rep. vol. 13, pp. 19–36. Institute of Fluid Science, Tohoku University.
JAIN , M. , PRAKASH , R. S. , TOMAR , G. & RAVIKRISHNA , R. V. 2015 Secondary breakup of a drop
at moderate Weber numbers. Proc. R. Soc. Lond. A 471, 20140930.
JALAAL , M. & M EHRAVARAN , K. 2014 Transient growth of droplet instabilities in a stream. Phys.
Fluids 26, 012101.
JOHNSEN , E. 2007 Numerical simulations of non-spherical bubble collapse with applications to
shockwave lithotripsy. PhD thesis, California Institute of Technology, Pasadena, CA.
JOHNSEN , E. & COLONIUS , T. 2006 Implementation of WENO schemes in compressible
multicomponent ﬂow problems. J. Comput. Phys. 219, 715–732.
JOHNSEN , E. & COLONIUS , T. 2009 Numerical simulations of non-spherical bubble collapse. J. Fluid
Mech. 629, 231–262.
JOSEPH , D. D. , BELANGER , J. & BEAVERS , G. S. 1999 Breakup of a liquid drop suddenly exposed
to a high-speed airstream. Intl J. Multiphase Flow 25, 1263–1303.
KAPILA , A. K. , MENIKOFF , R. , BDZIL , J. B. , SON, S. F. & STEWART , D. S. 2001 Two-phase
modeling of deﬂagration-to-detonation transition in granular materials: reduced equations. Phys.
Fluids 13 (10), 3002–3024.
KHOSLA , S. , SMITH , C. E. & THROCKMORTON , R. P. 2006 Detailed understanding of drop
atomization by gas crossﬂow using the volume of ﬂuid method. In 19th Annual Conference
on Liquid Atomization and Spray Systems . ILASS.
LANE , W. R. 1951 Shatter of drops in streams of air. Ind. Engng Chem. 43 (6), 1312–1317.
LIU, Z. & REITZ , R. D. 1997 An analysis of the distortion and breakup mechanisms of high speed
liquid drops. Intl J. Multiphase Flow 23 (4), 631–650.
MENG , J. C. 2016 Numerical simulations of droplet aerobreakup. PhD thesis, California Institute of
Technology, Pasadena, CA.
https://doi.org/10.1017/jfm.2017.804
 Published online by Cambridge University Press

<!-- PDF_PAGE: 28 -->

Numerical simulation of the aerobreakup of a water droplet 1135
MENG , J. C. & COLONIUS , T. 2015 Numerical simulations of the early stages of high-speed droplet
breakup. Shock Waves 25 (4), 399–414.
MOHSENI , K. & COLONIUS , T. 2000 Numerical treatment of polar coordinate singularities. J. Comput.
Phys. Note 157, 787–795.
MURRONE , A. & GUILLARD , H. 2005 A ﬁve equation reduced model for compressible two phase
ﬂow problems. J. Comput. Phys. 202, 664–698.
PELANTI , M. & SHYUE , K. M. 2014 A mixture-energy-consistent six-equation two-phase numerical
model for ﬂuids with interfaces, cavitation and evaporation waves. J. Comput. Phys. 259,
331–357.
PERIGAUD , G. & SAUREL , R. 2005 A compressible ﬂow model with capillary effects. J. Comput.
Phys. 209, 139–178.
PILCH , M. & ERDMAN , C. A. 1987 Use of breakup time data and velocity history data to predict
the maximum size of stable fragments for acceleration-induced breakup of a liquid drop. Intl
J. Multiphase Flow 13 (6), 741–757.
QUAN , S. & SCHMIDT , D. P. 2006 Direct numerical study of a liquid droplet impulsively accelerated
by gaseous ﬂow. Phys. Fluids 18, 102103.
QUIRK , J. J. & KARNI , S. 1996 On the dynamics of a shock-bubble interaction. J. Fluid Mech.
318, 129–163.
RANGER , A. A. & NICHOLLS , J. A. 1968 Aerodynamic shattering of liquid drops. In AIAA 6th
Aerospace Sciences Meeting . AIAA.
SAUREL , R. , PETITPAS , F. & BERRY, R. A. 2009 Simple and efﬁcient relaxation methods for
interfaces separating compressible ﬂuids, cavitating ﬂows and shocks in multiphase mixtures.
J. Comput. Phys. 228, 1678–1712.
SIMPKINS , P. G. & BALES , E. L. 1972 Water-drop response to sudden accelerations. J. Fluid Mech.
55, 629–639.
STAPPER , B. E. & SAMUELSEN , G. S. 1990 An experimental study of the breakup of a two-
dimensional liquid sheet in the presence of co-ﬂow air shear. In AIAA 28th Aerospace Sciences
Meeting. AIAA.
TAKAYAMA , K. & ITOH , K. 1986 Unsteady drag over cylinders and aerofoils in transonic shock
tube ﬂows. Tech. Rep. vol. 51. Institute of High Speed Mechanics, Tohoku University, Sendai,
Japan.
TANNO , H. , ITOH , K. , SAITO , T. , ABE, A. & TAKAYAMA , K. 2003 Interaction of a shock with a
sphere suspended in a vertical shock tube. Shock Waves 13, 191–200.
THEOFANOUS , T. G. 2011 Aerobreakup of Newtonian and viscoelastic liquids. Annu. Rev. Fluid
Mech. 43, 661–690.
THEOFANOUS , T. G. & L I, G. J. 2008 On the physics of aerobreakup. Phys. Fluids 20, 052103.
THEOFANOUS , T. G. , LI, G. J. & DINH , T. N. 2004 Aerobreakup in rareﬁed supersonic gas ﬂows.
Trans. ASME J. Fluid Engng 126, 516–527.
THEOFANOUS , T. G. , MITKIN , V. V. , NG, C. L. , CHANG , C. H. , DENG , X. & SUSHCHIKH , S.
2012 The physics of aerobreakup. Part II. Viscous liquids. Phys. Fluids 24, 022104.
WADHWA , A. R. , MAGI , V. & ABRAHAM , J. 2007 Transient deformation and drag of decelerating
drops in axisymmetric ﬂows. Phys. Fluids 19, 113301.
XIAO , F. , DIANAT, M. & MCGUIRK , J. J. 2014 Large eddy simulation of single droplet and liquid
jet primary breakup using a coupled level set/volume of ﬂuid method. Atomiz. Sprays 24 (4),
281–302.
ZALESKI , S. , LI, J. & SUCCI , S. 1995 Two-dimensional Navier–Stokes simulation of deformation
and breakup of liquid patches. Phys. Rev. Lett. 75 (2), 244–247.
https://doi.org/10.1017/jfm.2017.804
 Published online by Cambridge University Press
