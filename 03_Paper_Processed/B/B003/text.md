<!-- PDF_PAGE: 1 -->

ViewOnline
ExportCitation
RESEARCH ARTICLE |  JANUARY 08 2013
Large-eddy simulation of highly underexpanded transient
gas jets
V. Vuorinen; J. Yu; S. Tirunagari; O. Kaario; M. Larmi; C. Duwig; B. J. Boersma
Physics of Fluids 25, 016101 (2013)
https://doi.org/10.1063/1.4772192
Articles You May Be Interested In
Large eddy simulation of highly underexpanded sonic jets from elliptical nozzles
Physics of Fluids (October 2024)
Experimental study of flight effects on screech in underexpanded jets
Physics of Fluids (December 2011)
Numerical simulations of inert and reactive highly underexpanded jets
Physics of Fluids (March 2020)
 29 August 2026 06:16:57

<!-- PDF_PAGE: 2 -->

PHYSICS OF FLUIDS 25, 016101 (2013)
Large-eddy simulation of highly underexpanded transient
gas jets
V. Vuorinen,1 J. Yu,1 S. Tirunagari,1 O. Kaario,1 M. Larmi,1 C. Duwig,2
and B. J. Boersma3
1Department of Energy Technology, Aalto University School of Engineering, Finland
2Department of Energy Sciences, Lund University, Sweden
3Department of Energy Technology, Delft University of Technology, The Netherlands
(Received 21 June 2012; accepted 9 November 2012; published online 8 January 2013)
Large-eddy simulations (LES) based on scale-selective implicit ﬁltering are carried
out in order to study the effect of nozzle pressure ratios on the characteristics of highly
underexpanded jets. Pressure ratios ranging from 4.5 to 8.5 with Reynolds numbers
of the order 75 000–140 000 are considered. The studied conﬁguration agrees well
with the classical picture of the structure of highly underexpanded jets. Similarities
and differences between simulation and experiments are discussed by comparing
the concentration ﬁeld structures from LES and planar laser induced ﬂuorescence
data. The transient stages, leading eventually to the highly underexpanded state, are
visualized and investigated in terms of a phase diagram revealing the shock speeds
and duration of the transient stages. For the studied nozzle pressure ratio range, the
Mach disk dimensions are found to be in good agreement with literature data and
experimental observations. It is observed how the nozzle pressure ratio inﬂuences the
Mach disk width, and thereby the slip line separation, which leads to co-annular jets
with inner and outer shear layers at higher pressure ratios. The improved mixing with
increasing pressure ratio is demonstrated by the probability density functions of the
concentration. The coherent structures downstream of the Mach disk are identiﬁed
using proper orthogonal decomposition (POD). The structures indicate a helical mode
originating from the shear layers of the jet. Despite the relatively low energy content
of the dominant POD modes, the frequencies of the POD time coefﬁcients explain the
dominant frequencies in the pressure ﬂuctuation spectra.
C⃝ 2013 American Institute
of Physics.[ http://dx.doi.org/10.1063/1.4772192]
I. INTRODUCTION
Compressible jets are encountered in a vast number of applications of which perhaps the best
known lie within aerospace and aeronautics ﬁelds involving propulsion and aircraft design. 1–7 Such
high speed jets can also be observed in geophysical applications, for example, volcano eruptions
release large amounts of gas in the atmosphere featuring weak shocks, compression waves and Mach-
disks.
8 Other examples are jet formation during accidental release of pressurized hydrogen through a
small hole or a crack.9 Jets are present also in direct injection (DI) natural gas (NG) powered internal
combustion engines where compressed natural gas is injected into the cylinder. 10–12 Although the
physics in all these examples is similar, the shape of the nozzles varies signiﬁcantly from smoothly
contoured, well designed nozzles for optimizing thrust in rocket engines to elongated and sharp holes
in volcano and reservoir cracks. For example, the jet engine is designed to allow ﬂexibility of ﬂight
operation, leading potentially to “double diamond” shock patterns.
4 The fuel injection nozzles and
jet engine exhaust lie somewhere in between the two extreme cases. 13, 14 Also the nozzle operating
conditions, nozzle pressure ratio (NPR), depend on the application.
The literature implies that the driving motivation for studying jets varies from application to
application. The background interest for this study lies in DI gas engines where the purpose is to
design the injection conditions properly in order allow rapid mixing within some milliseconds prior
1070-6631/2013/25(1)/016101/22/$30.00 C⃝ 2013 American Institute of Physics25, 016101-1
 29 August 2026 06:16:57

<!-- PDF_PAGE: 3 -->

016101-2 Vuorinen et al. Phys. Fluids 25, 016101 (2013)
FIG. 1. The classical picture on the structure of a highly underexpanded jet. The picture is based on the visualization
presented by Donaldson and Sneedeker. 1
to ignition. In DI gas engines, ﬂow expansion, turbulent mixing downstream of the nozzle exit, and
jet penetration are vital for the combustion process and emissions. 10–14 Thereby, there is a need to
better understand and to reliably predict supersonic jet formation from the viewpoint of (1) shock
structures in the jet core, (2) turbulent mixing, and (3) coherent structures. In the present paper
supersonic jets are studied using large-eddy simulations (LES). One of the general objectives of the
paper are to enrich the present day views on transient, high Reynolds/Mach number jets encountered
in DI gas engines.
The classical picture on the structure of a highly underexpanded jet is shown in Fig. 1 showing
the Mach disk, the barrel shock, and the slip lines. At higher NPR, when NPR > 10, the empirical
formula H/D = C√
po/ p∞ can be used to predict the Mach disk height. 10, 11 As H/D increases,
also the distance between the slip lines increases. When NPR ≈ 4 the Mach disk is very narrow
and the slip lines are very close to one another. 4–7 In the present paper we investigate the regime
4.5 ≤ NPR ≤ 8.5 in order to gain further understanding into the effect of Mach disk width to the
physics of highly underexpanded jets.
Donaldson and Snedeker1 have reviewed the previous experimental observations on the behavior
of compressible jets issuing from convergent nozzles. The jets can be characterized by deﬁning three
reference pressures: (1) far upstream “reservoir” pressure po, (2) pressure at the nozzle exit p1, and
(3) far downstream pressure p∞ at ambient conditions where a free jet develops. The analysis 1
indicates three major jet ﬂow regimes: (1) subsonic jet: p1/p∞ = 1, 1 < po/p∞ < 1.893,
(2) moderately underexpanded jet: 1.1 < p1/p∞ ≤ 2, 2.08 < po/p∞ < 3.8, and (3) highly un-
derexpanded jet: 2 < p1/p∞ ,3 . 8 4< po/p∞ . In moderately underexpanded conditions the jet exhibits
the familiar oblique shock pattern (“shock diamonds”). In highly underexpanded conditions a normal
shock, i.e., the Mach disk, forms. In particular, as p
o/p∞ further increases the Mach disk increases in
size.1, 4, 10–14 The presence of the Mach disk has also been reported for conditions which are relevant
for combustion engines by White and Milton. 12
The numerical framework for LES of subsonic and incompressible turbulent jets is well
established15–22 and the recent studies have focused on supersonic conditions. 23–30 Ar e v i e wo n
the classical and the state-of-the-art numerical methods for high-speed ﬂows can be found in the
review article by Pirozzoli.
31 The challenges in LES of supersonic ﬂows concern the simultaneous
treatment of shocks and turbulence. One aims at capturing the discontinuity with simultaneously
using accurate, centered schemes for the turbulent ﬂow. 31 LES subgrid scale (SGS) models for
compressible ﬂow with various levels of complexity have been discussed in the literature.17 A rather
common model for turbulent dissipation is to apply a low-pass ﬁlter to the conservative variables
as done by Bogey and Bailly. 21 This approach has become rather popular in supersonic ﬂows and
it has been successfully applied by various authors. 23–26, 28–31 Typically the ﬁlter is chosen to be at
least of the same order as the underlying numerical method in order to not decrease the order of the
discretization. Even in direct numerical simulation (DNS), low-pass ﬁltering is often employed for
removal of dispersive and aliasing errors. 32
A common observation is that higher than second order ﬁlters are not sufﬁcient for removing
the Gibbs ringing near the shock discontinuities. 31 Bogey et al. 23 proposed a method based on
localized second order spatial ﬁltering of the conservative variables at shock positions. They modeled
turbulent dissipation with explicit high order ﬁlters. 21 Cacqueray et al. 24 used a similar approach
 29 August 2026 06:16:57

<!-- PDF_PAGE: 4 -->

016101-3 Vuorinen et al. Phys. Fluids 25, 016101 (2013)
for simulating the turbulent dynamics and shock cell structure of over-expanded jets. A few years
ago, hyperviscosity for LES of shock-turbulence interactions was introduced by Cook and Cabot
(CC).28 The CC-model is based on augmenting the viscous stress tensor σij = μ(∂ui
∂x j
+ ∂u j
∂xi
) + (μb
− 2
3 μ)∂ui
∂x j
δij , with a modeled bulk viscosity μb. The approach28 is appealing since it affects the ﬂow
only via the dilational part of the viscous stress. Thereby, the CC-model activates at shock fronts and
deactivates in turbulent parts of the ﬂow. A vast number of modiﬁcations to this model in the context
of ﬁnite difference solvers have been proposed by, e.g., Kawai et al.
25 and Bhagatwala et al. ,29
Kawai and Lele26 used the CC-model and explicit ﬁltering for LES of a jet in supersonic cross-ﬂow
ﬁnding good agreement with experiments. They also demonstrated the presence of the Mach disk
alongside with the strong presence of turbulence and acoustic ﬁelds. Mani et al.
30 showed how ﬂow
over a cylinder can be captured with a similar simulation method.
The previous examples23–26, 28–31 are based on a high order ﬁnite difference framework. However,
in more complex geometries ﬁnite volume methods (FVM) would be preferred. As mentioned
by Pirozzoli, 31 further studies on supersonic ﬂows with unstructured FVM-codes are required.
Recently, FVM was used in LES of a blunt body opposing a supersonic jet by Chen et al. 33 The
dissipative elements in their simulations were: (1) central/upwind scheme for shock capturing and
(2) explicit closure model for turbulence. LES of an impinging supersonic jet was carried out by
Dauptain et al.5 using a third order accurate FVM code. The dissipative elements in their study were:
(1) the CC-hyperviscosity for shock capturing, (2) explicit Smagorinsky model for turbulence
closure, (3) upwind biased discretization of the convective terms, and (4) usage of tetrahedral mesh
for the simulations. The observations
5, 33 motivate further developments and application of FVM for
compressible jet ﬂows.
In the present work large-eddy simulation (LES) of supersonic gas jets is carried out. The
objectives are to (1) develop a gas jet injection model for LES of fuel jets, (2) use FVM for high
speed ﬂows31 and use the scale-selective discretization approach by Vuorinen et al.34 for accounting
for the turbulent dissipation, (3) better understand the physical consequences of the effect of jet
injection pressure on shock formation, and (4) use proper orthogonal decomposition (POD) to
characterize the dominant modes of the jets. As a numerical tool, we have implemented a density
based 4th-order Runge-Kutta ﬁnite volume (FV) solver using the OpenFOAM
R⃝ library.16 The FV -
method on an unstructured grid framework is chosen since the method should be eventually applied
in complex geometries. The results are qualitatively compared with planar laser induced ﬂuorescence
(PLIF) experiments.13, 14 The organization of the paper is as follows: in Sec. II the numerical method
is explained, and in Sec. III LES results from jet development and mixing are presented. Finally, in
Sec. IV conclusions of the work are discussed.
II. NUMERICAL PROCEDURE
A. Governing equations
The dynamics of compressible ﬂows are governed by the full Navier-Stokes equations
NS = NS(ρ, ui, ...) = 0 describing the conservation of mass, momentum, and energy 17
∂ρ
∂t + ∂ρu j
∂x j
= 0, (1)
∂ρui
∂t + ∂(ρui u j )
∂x j
= ∂
∂x j
(− pδij + σij ), (2)
∂ρe
∂t + ∂((ρe + p)u j )
∂x j
= ∂
∂x j
(σij ui ) + ∂
∂x j
(
λ∂T
∂x j
)
, (3)
where the quantities ρ, ui, p, and T are respectively the density, velocity, pressure, and temperature
of the gas. The pressure is explicitly coupled to the density and the temperature via the equation of
 29 August 2026 06:16:57

<!-- PDF_PAGE: 5 -->

016101-4 Vuorinen et al. Phys. Fluids 25, 016101 (2013)
state
p = ρRT . (4)
Furthermore, the internal energy of the ﬂow is deﬁned as the sum of thermodynamic and kinetic
energy
e = cv T + 1/2ui ui . (5)
In Eq. (2) the viscous stress tensor is deﬁned as follows:
σij = μ(∂ui
∂x j
+ ∂u j
∂xi
) + (μb − 2
3μ)∂ui
∂x j
δij , (6)
where μb is the bulk viscosity of the gas and μ is the dynamic viscosity computed by Sutherland’s
law
μ(T ) = μs
Ts + Cs
T + Cs
(T/Ts )1.5. (7)
In Eq. (7) μs = 1.781 × 10− 5 kg/ms, Ts = 300.55 K, and Cs = 111.0 K corresponding to the
properties of nitrogen.
An additional equation for a passive scalar c = c(x, y, z, t) is solved in order to study mixing:
∂ρc
∂t + ∂ρcu j
∂x j
= ∂
∂x j
ρDc
∂c
∂x j
, (8)
where Dc is the species diffusivity. The Schmidt number of the ﬂow is Sc = 0.7. Also the Prandtl
number is set to Pr = 0.7.
B. LES based on scale selective discretization
Equations (1)–(3) are valid in the limit of DNS where the grid is ﬁne enough to represent all the
scales of the ﬂow. 17 In LES, the resolution is coarser than in DNS and Eqs. (1)–(3) are solved for
the spatially ﬁltered variables with additional SGS terms appearing as source terms in the equations.
In other words, the LES equations
17 can be written in form NS (˜ρ, ˆui , ...) = τsgs . The SGS vector
τsgs requires modeling. V arious SGS closure models have been discussed in the literature. 17 Here
we choose the scale selective discretization (SSD) approach by Vuorinen et al.34 which belongs to
the so-called implicit LES (ILES) modeling category 4, 17, 27, 35–40 with one important difference. In
contrast to ILES, the SSD approach targets the dissipative effects only to the smallest scales of a
ﬂow via a scale separation procedure. The scale separation is achieved using a Laplacian ﬁlter which
splits the convection term into low and high frequency parts for which centered and upwind-biased
schemes can be separately employed. In the present, unstructured code the SSD scheme is second
order accurate. Vuorinen et al.
34 presented a modiﬁed wavenumber ( kmod) analysis of the SSD
scheme and showed that the SSD scheme is always less dissipative than the standard third order
upwind scheme which has been used in previous LES.5, 35 To summarize, Eqs. (1)–(3) are solved for
the grid ﬁltered conservative variables on an unstructured computational grid using centered, second
order accurate discretization with SSD scheme applied on the convection term. We set τsgs = 0 and
model the SGS effects by the diffusive truncation error of the SSD scheme which is of third order
O(/Delta1x
3). An explicit, density based approach is employed along with the classical 4th-order accurate
Runge-Kutta time integration scheme. Among other validation studies (e.g., turbulent channel ﬂow),
the solver was validated by Vuorinen et al.16 for turbulent subsonic jets and also laminar ﬂows.
C. Shock capturing
The strong compression effects of the gas are taken into account using a model for the bulk
viscosity μb which affects the dilational part of the viscous stress tensor in Eq. (6).H e r ew eu s et h e
 29 August 2026 06:16:57

<!-- PDF_PAGE: 6 -->

016101-5 Vuorinen et al. Phys. Fluids 25, 016101 (2013)
CC-model by Cook and Cabot 28 where μb is computed as follows:
μb = Cbρ/Delta1r+2|∇r Sij |, r = 2, 4, 6, .... (9)
In Eq. (9) r = 2 so that ∇ 2Sij corresponds to the Laplacian of the rate of strain tensor with a
high wavenumber bias. The value Cb = 5 is used as recommended in the literature 5, 28, 29 and the
length scale /Delta1is computed from a cell volume Vcell as /Delta1= V 1/3
cell .F i g .6(d) shows that the bulk
viscosity activates at the Mach disk, reﬂected oblique shocks and along the shear layers of the jet. It
is important to note that the inﬂuence of μb becomes local when it is multiplied with the divergence
(ﬂow dilation) (see Eq. (6)). It is known that at a shock position ∥Sij ∥∼| ∇· u| but in a turbulent
ﬂow ∇· u ≈ 0. Thereby, as seen in Eq. (6), μb only affects the trace of the stress tensor. 28 We note
that the range of μb is in line with the previous studies. 5, 25
According to our numerical experiments the CC-model 28 as such is not enough for capturing
strong normal shocks using FVM since μb does not inﬂuence the continuity equation. However,
Dauptain et al.5 managed to deal also the normal shocks with the CC-model in LES of supersonic
impinging jets since in their simulations the Smagorinsky turbulence model viscosity worked as an
adaptive second order ﬁlter providing further stabilization at the normal shocks. Here, in addition to
the CC-model, we apply a second order ﬁlter to the conservative variables locally in the immediate
vicinity of the Mach disk at the end of each timestep. The ﬁlter is activated in the regions of extreme
compressibility using the indicator function of Bhagatwala and Lele
29
γ = 1
2 (1 − tanh((0.25 + ∇· u
c//Delta1)/0.1)), (10)
which activates at the location of strong shocks. In Eq. (10) c is the local speed of sound. After 0
≤ γ ≤ 1 has been calculated, the local low pass ﬁltering of the conservative variables is carried out
at the end of each timestep using a Laplacian ﬁlter with coefﬁcient γ
(
/Delta1
π
)2
which damps the Gibbs
oscillation close to the highest wavenumber kmax ≈ π
/Delta1.F i g .6(c) shows that γ is non-zero only at the
Mach disk vanishing elsewhere. It should be noted that γ is suitable for indicating the normal shock
position since ∇· (uρ) = ρ∇· u + u ·∇ ρ ≈ ρ∇· u because the density gradient becomes aligned
with the velocity. With these arrangements the simulations become stable, the shock structures
become resolved, and the turbulence can be maintained.
D. Simulation setup
In the present study simulations of highly underexpanded jets are carried out in a wall-bounded,
closed system as seen in Fig. 2. The system consists of a high-pressure tank at pressure po and a
low-pressure tank at pressure p∞ = 1 bar. Altogether ﬁve simulations are carried out for po = 4.5,
5.5, 6.5, 7.5, and 8.5 bars. Initially the gas temperature is uniform T = 293 K. The two tanks are
connected by a converging nozzle and the ﬂow is driven through this nozzle by the pressure gradient.
The nozzle exit is located at z = 0. Between − 10D < z < 0 the nozzle does not practically converge
anymore and the gas ﬂows through a straight pipe having a diameter D = 0.0014 m. The nozzle
diameter is the same as in the PLIF experiments 14 but the nozzle pipe itself is only a simpliﬁcation
of the real, converging nozzle. At the nozzle exit, a sonic jet with diameter D is formed with exit
velocity U1 ≈ 330 m/s and exit Mach number Ma = 1. The integral timescale is deﬁned using D and
the maximum propagation speed of information at the nozzle exit (2U1)a s To = D
2U1
≈ 2.0 × 10− 6s.
This deﬁnition differs from the usual deﬁnition by the factor 1/2 but the present choice for the
velocity scale also reﬂects the typical high speed velocities in the near-ﬁeld of the jet. The total
simulation duration is 0.5m s = 243To.
The boundary conditions are modeled using the standard Dirichlet-Neumann conditions for the
primitive variables p, ρ, T, and ui. The conservative variables are constructed on the boundary based
on the primitive variables. In the low-pressure tank the no-slip boundary condition is enforced for
velocity and the walls are set to T = 293 K. Inside the nozzle and the high-pressure tank a slip
 29 August 2026 06:16:57

<!-- PDF_PAGE: 7 -->

016101-6 Vuorinen et al. Phys. Fluids 25, 016101 (2013)
FIG. 2. (a) The simulation geometry shown from the outside. The setup consists of a high-pressure reservoir, a converging
nozzle and a large cylinder. (b) An underexpanded jet is formed through a nozzle exit. The nozzle inner and outer diameters
are D and 2 D respectively. (c) The classical picture on shock wave structures in underexpanded jets
1 is reproduced by the
present LES.
condition for velocity is employed in order to avoid formation of artiﬁcial boundary layers. 5 Inside
the nozzle the zero-gradient condition for temperature needs to be employed due to cooling of the
gas while accelerating inside the nozzle. The wall normal gradients of pressure and passive scalar
vanish on the walls.
According to previous studies, the spatial resolution in LES of supersonic jet needs to be
rather high. Table I gathers some estimates of previously used grid resolutions in the core region of
supersonic jets. For example, Dauptainet al.5 concluded that a resolution of order D/30 in the jet core
is adequate for obtaining reliable results for a wall impinging jet. Munday et al.4 used a resolution of
order D/50 in the cross streamwise direction for a free jet. Rana et al.27 applied a resolution of order
D/30 as well for a jet in supersonic cross ﬂow. The previous studies form a guideline for constructing
the present mesh as will be explained in what follows.
TABLE I. Comparison of near-nozzle resolution in present and previous LES of supersonic jets. Resolution is expressed in
terms of estimated radial resolution /Delta1r and streamwise resolution /Delta1z.
Author /Delta1rmin.../Delta1rmax /Delta1zmin.../Delta1zmax Cell type Re
Present study D/70...D/50 D/35...D/25 Hexahedral ∼ 105
Munday et al.4 D/50...D/35 D/50...D/35 Hexahedral ∼ 106
Dauptain et al.5 D/35...D/30 D/35...D/30 Tetrahedral ∼ 106
Rana et al.27 D/33 D/33 Hexahedral ∼ 2.4 × 104
 29 August 2026 06:16:57

<!-- PDF_PAGE: 8 -->

016101-7 Vuorinen et al. Phys. Fluids 25, 016101 (2013)
FIG. 3. Grid topology viewed from the cross streamwise and streamwise perspectives. The reﬁnement region extends until
z/D = 22.5 and it is created into the background grid by splitting the hexahedral cells into 8 parts.
The hexahedral, block-structured grid topology of the present study is presented in Fig. 3.
Altogether the mesh contains 12M computational cells. The jet core is meshed with ﬁne resolution
by adding a reﬁnement region which covers the jet core and the developing shear layers. The
reﬁnement region extends until z/D = 22.5 thereby covering the main region of interest in this study.
Inside the reﬁnement region the hexahedral cells of the background mesh are split into 8 parts.
Despite slight stretching of the grid, the present mesh allows good control over the grid quality and
the control volume dimensions are typically always within D/35 ≤ /Delta1z ≤ D/25 in the streamwise
and D/70 ≤ /Delta1r ≤ D/50 in the cross streamwise directions within the region of interest. Note that
/Delta1z = D/35 until z/D = 12 covering the transitional region where we carry out for example the POD
analysis. After z/D = 22.5 the background resolution is recovered and the grid stretching becomes
more pronounced in order to damp the downstream propagating waves before they interact with the
bottom wall of the cylinder which is located at z/D = 70. With these arrangements the resolution
requirements presented in the previous studies
4, 5, 27 are met in large portion of the jet core region.
E. Initial conditions and ﬂow rate in highly underexpanded conditions
Yu et al.13 have explained the ﬂow development stages in highly underexpanded jets: (1) initial
delay time due to opening of the solenoid valve or injector needle, (2) ﬂow development in the nozzle
and building up of the pressure gradient in the nozzle, and (3) fully developed ﬂow. In particular,
stage 2 inﬂuences the nozzle exit pressure p
1 and it is usual to observe all the standard jet conditions
in practice including subsonic, moderately underexpanded and highly underexpanded ﬂow. 14 In DI
NG-engines the development times can be comparable to the total injection duration ( ∼ 1m s )10–14
due to the delay in opening of the injector needle and rather large physical size of typical injectors
in comparison to the nozzle diameters.
In the present paper, the simulation is considered to begin from the end part of stage 2. Since
the pressure proﬁle at that stage is unknown, it has to be modeled. We initialize the pressure ﬁeld
using a hyperbolic tangent function which varies smoothly from value po to p1 at the nozzle exit,
see Fig. 4.A t t = 0w es e t p1 > p∞ to allow fast jet development. The pressure in the chamber is
set to p∞ = 1 bar. In the fully developed state, p1 > 2 since the jet is highly underexpanded 1 and
the ﬂow is not assumed to be dependent on the initial condition anymore. It is considered important,
that the nozzle exit pressure p1 builds up solely due to the nozzle ﬂow and, for example, linking po
and p1 with analytical relationships is avoided. At the start of injection (SOI) the upstream traveling
expansion wave is noted in Fig. 4. Around time t = 90To the system has reached a steady state which
can be seen from the pressure proﬁles and steady mass ﬂow which is noted to vary linearly with the
nozzle pressure ratio.
III. RESULTS
A. Steady state jets
First, we present visualization of the instantaneous jets in steady state conditions by considering
the contour plots of log 10(|∇ρ|). Fig. 5 shows how NPR affects the shock cell patterns. The present
 29 August 2026 06:16:57

<!-- PDF_PAGE: 9 -->

016101-8 Vuorinen et al. Phys. Fluids 25, 016101 (2013)
−40 −30 −20 −10 00
1
2
3
4
5Pressure (bar)
z/D
 
 
po = 4.5 bar
p1/p∞ > 2
p1/p∞ < 2
(a)
Expansion wave
t=0
t=45To
t=90To
t=140To
4 5 6 7 8 91.5
2
2.5
3
3.5
4
4.5
5
po/p∞
Nozzle Pressure/Massflow
 
 
(b)
Pressure (bar) at z/D=−10D
Massflow (g/s) at z/D=−10D
FIG. 4. (a) Time development of pressure proﬁle along the z-axis. The steady state is reached by t ≈ 90To. (b) The steady
state nozzle pressure and mass ﬂow rate at the monitoring point z/D =− 10 located on the jet axis are conﬁrmed to scale
linearly with po/p∞ .
jets feature a barrel shock terminating at a ﬁrst normal shock, the Mach disk, in the near nozzle
region z/D < 3. The parallel slip lines start from the Mach disk and they continue until turbulence
develops in the shear layers via growing instabilities which eventually reach the jet core between
4.5 ≤ z/D ≤ 7 depending on NPR. In between the slip lines a train of shock cells forms due to
reﬂection of shocks from the shear layers of the jet. Similarities between the present visualization
and previous experimental Schlieren experiments
1, 4, 6, 7, 12, 13 arise, in particular, from the viewpoint
of shock structure- NPR dependency. To our knowledge the effect of NPR on jet structure has
not been systematically studied by LES previously but, nevertheless, the present LES compares
favorably with the previous “numerical Schlieren” visualization by Munday et al. 4 and Dauptain
et al.5 in terms of shock patterns (reﬂection, slip line position, shock cells after the Mach disk). In
particular, it is very clear that the height ( Hdisk) and the width ( Wdisk ) of the Mach disk increase
with increasing NPR as seen in Fig. 5. Also, the jet tip penetration and the jet volume increase with
increasing NPR.
In the present LES turbulence starts to develop after the Mach disk and we observe no ﬂow
outside the ﬁrst shock cell. Potentially, it would be possible to observe G¨ortler vortices (GVs) outside
FIG. 5. Density gradient (log 10(|∇ρ|)) at time To = 90 for (a) po/p∞ = 4.5, (b) po/p∞ = 6.5, and (c) po/p∞ = 8.5. The size
of the view extends to z/D = 25.
 29 August 2026 06:16:57

<!-- PDF_PAGE: 10 -->

016101-9 Vuorinen et al. Phys. Fluids 25, 016101 (2013)
FIG. 6. Instantaneous snapshots of various ﬂow quantities for po/p∞ = 6.5. (a) Temperature, (b) Mach number, (c) the strong
shock sensor (γ), and (d) CC bulk viscosity ( μb/μ∞ ).
the ﬁrst cell if the G ¨ortler number ( G) exceeds 0.3 ( G = Uθ
ν
(
θ
R
)1/2
, where U = velocity scale, θ
= incoming boundary layer thickness, ν= kinematic viscosity, and R = radius of curvature of the
shock cell boundary). 48 Here the onset of the instability depends mostly on θ and R. For example,
Dauptain et al.5 have reported LES where GVs were observed outside the barrel shock. The LES by
Dauptain et al. posed several sources of asymmetry (tetrahedral grid and wall-jet interactions) which
could rapidly trigger the GVs. Here, the grid is very symmetric and the instability is likely to grow
slower. In fact, literature has shown that development of the gas motion outside the barrel shock
and jet boundary when z/D < 3 depends on the nozzle conﬁguration (e.g., possible asymmetries)
and on the level of turbulence development at the nozzle exit. 1, 4, 6, 7, 12, 13 For example, Panda et al.7
and Munday et al. 4 have reported experiments where almost no visible turbulence was observed
at the boundary or outside the barrel shock. We conclude that in reality the growth rate of G ¨ortler
instabilities is likely to depend on the turbulence development at the nozzle exit.
Fig. 6 demonstrates the spatial variation of the gas temperature, Mach number, artiﬁcial bulk
viscosity (μb) and the normal shock sensor (γ) in the fully developed state. In the near nozzle region
the jet is characterized by the barrel shock and the Mach disk. At the nozzle exit the ﬂow velocities
are very close to sonic velocities ( Ma ≈ 1). The very rapid expansion leads to high Mach numbers
close to 3 in the vicinity of the Mach disk. At the barrel shock position the ﬂow compresses which
increases the gas density and concentration. The Mach disk itself is characterized by temperature
minima and discontinuity in the primitive variables. 5 It is observed that the gas undergoes strong
cooling by factor 0.3 from the reservoir temperature levels leading to temperatures of order 100 K
at the Mach disk. Immediately after the Mach disk the ﬂow becomes again subsonic as expected. 1
The subsonic regions are seen to occur in the shock cells where the thermodynamic conditions are
close to the ambient values T∞ , p∞ , ρ∞ . The panel (c) of Fig. 6 shows how the indicator function γ
(Eq. (10)) activates the low pass ﬁlter only in the immediate vicinity of the normal shock. The
activation of the bulk viscosity (Eq. (9)) is noted at the shocks and the jet shear layers as anticipated
based on previous studies 5, 29
B. Volumetric growth
The jet tip penetration S(t) is a very important property of fuel jets since it determines also
the volumetric growth rate of the jet. The volumetric growth can be further linked to mixing and
entrainment which are two vital processes for fuel jets inﬂuencing the level of emissions in chemically
reacting ﬂow. For underexpanded sonic jets Ouellette and Hill11 have found that S/(ρo/ρ∞ )1/4 ∼ t1/2.
 29 August 2026 06:16:57

<!-- PDF_PAGE: 11 -->

016101-10 Vuorinen et al. Phys. Fluids 25, 016101 (2013)
0 2 4 6 8 10 120
0.005
0.01
0.015
0.02
0.025
0.03
(t/To)1/2
Stip/(ρo/ρ∞)1/4
 
 
(a)po/p∞=4.5
po/p∞=5.5
po/p∞=6.5
po/p∞=7.5
po/p∞=8.5
10
2
10
3
10
−3
10
−2
10
−1
10
0
(t/To)3/2
Vjet/(ρo/ρ∞)3/4
 
 
(b)
po/p∞ = 4.5
po/p∞ = 5.5
po/p∞ = 6.5
po/p∞ = 7.5
po/p∞ = 8.5
FIG. 7. (a) Tip penetration of the jet. (b) In normalized variables the data collapses onto a single line.
The present LES, see Fig. 7(a), clearly conﬁrms this behavior after the initial transients have passed
by and the pressure gradient has fully developed across the nozzle for the jet to be underexpanded.
The link between the tip penetration and jet volume has been given little attention in the literature.
Experimental measurement of jet volume is difﬁcult since the data are typically 2d. Y et, in LES the
jet volume can be evaluated from 3d data. Here, we deﬁne the jet volume as the set of cells where
the concentration exceeds the threshold value ρc = 0.001, that is, V (t) =
∫
ρc>0.001 δV .F r o mt h e
cone-like geometry of the jets it is anticipated that V ∼ S3 ∼ t3/2 if S is taken to be the “height” of
the cone and the “tip” of the cone is located atz = 0. Indeed, Fig. 7 conﬁrms that the jet volume scales
quite well with t3/2. After normalization a data collapse is noted implying a V/(ρo/ρ∞ )3/4 ∼ t3/2
scaling for the volumetric jet growth. This will be further discussed in the end of the paper.
C. Development of the shock cells
We investigate the early stage of the jet injection, focusing on the density history and shock
establishment. This information is not accessible using experimental techniques. Fig. 8 shows
transient formation of a jet at injection pressure po/p∞ = 6.5. At an early time t = 14To a tip-vortex
characteristic to subsonic jets is observed (a). Soon, at time t = 18To, the Prandtl-Meyer expansion
FIG. 8. A close-up to the nozzle exit showing how an initially subsonic jet (a) turns its character in the Prandtl-Meyer
expansion around time t = 16 − 18To (b). The process is followed by growth of the Mach disk (c) and (d).
 29 August 2026 06:16:57

<!-- PDF_PAGE: 12 -->

016101-11 Vuorinen et al. Phys. Fluids 25, 016101 (2013)
0 5 10 15 20 25 300
1
2
3
4
5
6
z/D
ρ
 
 
(a)
LES: po/p∞ = 4.5
LES: po/p∞ = 5.5
LES: po/p∞ = 6.5
LES: po/p∞ = 7.5
LES: po/p∞ = 8.5
Ambient density ρ∞
0 5 10 15 20 25 300
0.05
0.1
0.15
0.2
0.25
z/D
ρrms
 
 
(b)
LES: po/p∞ = 4.5
LES: po/p∞ = 5.5
LES: po/p∞ = 6.5
LES: po/p∞ = 7.5
LES: po/p∞ = 8.5
FIG. 9. (a) Axial density ([ ρ] = kg/m3). (b) Axial RMS density ([ ρrms ] = kg/m3).
leads to formation of spherically propagating bow shock followed by the development of oblique
shocks (diamond shocks) near the nozzle exit. When the nozzle exit pressure p1 has increased above
the threshold level for highly underexpanded ﬂow ( p1 = 2p∞ ), the Mach disk begins to develop. 1
For NPR = 6.5, p1 exceeds 2 when t = 40 − 50To.F i g .4 shows that for NPR = 4.5 the ﬂow develops
almost as quickly as for NPR = 6.5 but p1 exceeds p∞ only slightly since the NPR = 4.5 case is
almost at the limit of highly underexpanded ﬂow. Typically, in all the studied cases the Mach disk
is initially very narrow but in 10 − 20To the slip lines become more separated from one another as
the disk width grows. Based on Fig. 8 these stages take altogether about 50 − 70To after which the
Mach disk is fully developed.
The shock cells can be observed from a plot of axial density proﬁles as seen in Fig. 9(a).T h e
density decreases sharply from the high nozzle exit value, oscillates around a low level, increases to
a maximum at z/D ∼ 8 and decreases asymptotically towards ρ
∞ . The lower the NPR the faster the
rate of decay. For the highestNPR the axial density is still about 10% aboveρ∞ at z/D = 25. Also the
axial density ﬂuctuations show interesting behavior as noted in Fig. 9(b). The density ﬂuctuations
peak around z/D ∼ 7–10 after which the ﬂuctuations decay slowly towards zero. The peak is shifted
more downstream with increasing NPR since the turbulence transition process is slower for higher
NPR. The peak location occurs after the shear layers have reached the jet axis. In absolute (and also
normalized) terms the peak of ρrms is the highest for the highest NPR. The large density variations
imply high compressibility effects until at least z/D = 30.
Fig. 10 shows the time development of axial density for NPR = 4.5 and 6.5. The diagram of
Fig. 10 is constructed by plotting the axial density proﬁles as a function of time in ( z/D, t/To) plane.
A line pattern (I) appears at t = 0 corresponding to a very weak, hardly visible initial pressure
FIG. 10. Phase portrait of normalized density ( ρ/ρmax) along the z-axis in ( z/D, t/To)-plane. (a) NPR = 4.5 and (b) NPR
= 6.5. The dashed lines work as a guide to the eye for pointing out wave propagation speed.
 29 August 2026 06:16:57

<!-- PDF_PAGE: 13 -->

016101-12 Vuorinen et al. Phys. Fluids 25, 016101 (2013)
wave that originates form the nozzle and propagates at the speed of sound ( U1). A clear line pattern
(II) is noted for all NPR starting from z/D = 0 at time t ≈ 17To. It features a local pressure peak
followed by a pressure minimum corresponding to the bow shock in Fig. 8. The bow shock moves
at velocity 0.6U1. After passage of the bow shock, density gradients form in region III while the jet
undergoes the Prandtl-Meyer expansion. From Fig. 8(c), it is seen that this transition corresponds
to a cone shaped shock cell evolving towards the Mach disk. At the stabilization time, it consists
of a region of high density downstream of the nozzle followed by a smooth density decrease (over
2D) ended by a sudden increase. This feature is highlighted as region IV and corresponds to the
part starting at the nozzle and extending up to the Mach disk. In region III a faint density minimum
is noted for NPR = 4.5 which moves downstream and becomes stronger in region IV around time
t/T
o = 60. For NPR = 6.5 the similar minimum is stronger in region III and it moves dowstream to
region IV without changing its intensity. This indicates more rapid establishment of the Mach disk
for higher NPR. Further downstream of the Mach disk, two diamond shapes cells (region V) are seen
but not appearing before t = 75To. After that, a collection of periodic, horizontal lines are noted in
region VI.
D. Time averaged concentration and velocity ﬁelds
The cross-sectional concentration ﬁeld images from LES are next compared with their experi-
mental counterparts based on the PLIF technique. The present measurements have been described
in detail in the previous work by Y u et al.
13, 14 In the present PLIF, nitrogen jets are injected into
ambient conditions with various injection pressures. Acetone vapor is used as a ﬂuorescent tracer.
PLIF is well suited for ﬂow visualization with the particular advantage of offering cross-sectional
information of the jets. PLIF has been previously used to gain further conﬁdence to LES by various
authors.
25, 27
In PLIF signiﬁcant pressure losses occur inside the nozzle. 13, 14 Therefore, the LES and PLIF
need to be compared by choosing cases where the Mach disk heights are similar and the experimental
jets can be considered to be operated at the same effective NPR as the present LES. Based on
Fig. 11 the average ρc distribution of the present LES compares well with the structures obtained in
PLIF. In particular, the region z/D < 5 is qualitatively well captured. Also the observed number of
shock cells in LES and PLIF is the same. The jets pose strong localization of mass and concentration
in the co-annular shear layers of the jet. Fig. 12 shows that increased ρc implies the momentum
to be channeled into the annular shear layers. For example, after the Mach disk, when z/D < 10
supersonic velocities are noted in the shear layers whereas the shock cell centers correspond to the
low speed subsonic regions where the stagnation conditions are met. The axial mean velocities reach
supersonic values until z/D = 20. Also the jet core is long in contrast to subsonic jets where the
potential core length is typically 4 − 6D. The shock cell pattern dictates the velocity relaxation until
z/D ∼ 10–14.
The highest NPR shows a clear inner and a clear outer shear-layer as seen from Figs. 11 and
12. The shear-layers extend downstream more and more when increasing NPR. Fig. 12 shows that
also the RMS of velocity has high values in the shear layer. The RMS also shows a clear inﬂuence
of the NPR on the ﬂuctuation pattern. At low NPR, the two peak RMS or shear-layers merge at z/D
= 10 while they extend much longer for the other cases. For instance at high NPR, the RMS level
remains large at z/D = 20 while it has already decreased for low NPR. The peak of ρ
rms around z/D
∼ 8i nF i g .9 is related to Fig. 12 and the collapse of the annular jet in the respective location. The
structure of the shear layer will be further analyzed with POD in the end of the paper.
One primary difference between the present PLIF and LES is that turbulence is observed outside
the barrel shock in PLIF in contrast to LES. Additionally, the experimental jet shear layers develop
faster than those in LES. This difference is understandable due to differences in the setups. For
example, in LES the nozzle wall boundary layers and turbulence are not modeled and we use the
slip velocity boundary condition inside the nozzle. This explains already most of the discrepancies
between LES and PLIF since in the experiments the nozzle ﬂow probably poses turbulent boundary
layers. The experimental jets have also developed for several milliseconds and thereby the turbulence
had time to develop. In the experiments, also the injector poses some asymmetric features which
 29 August 2026 06:16:57

<!-- PDF_PAGE: 14 -->

016101-13 Vuorinen et al. Phys. Fluids 25, 016101 (2013)
FIG. 11. Average concentration ( ρc) and a comparison of LES (a)–(d) and PLIF (e)–(h). (a) po/p∞ = 5.5, (b) po/p∞ = 6.5,
(c) po/p∞ = 7.5, and (d) po/p∞ = 8.5.
FIG. 12. V elocity statistics from LES. Average streamwise velocity (a)–(c) and RMS velocity (d)–(f) normalized by nozzle
exit velocity (U1 ≈ 330 m/s). ((a) and (d)) po/p∞ = 4.5, ((b) and (e)) po/p∞ = 6.5, and ((c) and (f)) po/p∞ = 8.5.
 29 August 2026 06:16:57

<!-- PDF_PAGE: 15 -->

016101-14 Vuorinen et al. Phys. Fluids 25, 016101 (2013)
FIG. 13. Comparison between concentration ﬁelds obtained from LES (upper half) and PLIF (lower half). Also the shear
layer thickness (δ) and the shock reﬂection angle ( α) are deﬁned. (a) po/p∞ = 5.5 and (b) po/p∞ = 7.5.
produces clearly noticable deviation from symmetry in reality. The same explanation holds true
further downstream where differences in the shock cell structures are observed.
E. The Mach disk
Fig. 13 shows a close-up to the jet inlet. As can be seen, PLIF and LES both show how the
injection pressure inﬂuences the Mach disk height ( Hdisk) and width ( Wdisk ). In particular, Wdisk
determines also the separation between the slip lines and it thereby has an integral role in the
formation of the annular shear layers. As can be seen from Fig. 13, shocks are reﬂected from the
triple point located at the edge of the Mach disk. The triple point (see Fig. 1) is the intersection
point of the barrel shock, the Mach disk and the ﬁrst reﬂected shock. The angle of the ﬁrst reﬂection
(α) is affected by NPR so that α decreases with increasing NPR.F o r NPR = 5.5 we measure
α ≈ 34
◦ whereas for NPR = 7.5 the value α ≈ 29◦ is observed. Both angles are close to the
estimated values measured with PLIF. We also note that the thickness of the shear layer ( δ)v a r i e s
with NPR so that δ≈ 0.44D for NPR = 4.5 but falls to approximately a constant value δ≈ 0.35D
for NPR ≥ 5.5. The reﬂection angles as well as the shear layer thickness for all NPR are tabulated
in Table II.
The height of the Mach disk Hdisk increases as a function of the injection pressure. Ashkenaz
and Sherman45 have derived the following formula for the NPR-Hdisk relationship:
Hdisk /D = C
√ po
p∞
. (11)
The derivation by Ashkenaz and Sherman 45 leads to the constant C = 0.67. The result seems
to be valid only for higher injection pressures since for NPR < 10 Ewan and Moodie 46 observed
experimentally a smaller value C ≈ 0.55 but with C approaching 0.67 with increasing NPR.T h e
TABLE II. Summary of results for highly underexpanded jets. Frequencies expressed as Strouhal number ( St = fD/2U1),
length scales normalized with D and the shock reﬂection angles expressed in degrees. Epeak/Etot denotes the fraction of sound
energy contained in the dominant pressure ﬂuctuation peak.
po/p∞ Hdisk Wdisk δshear αshock fpeak (p′) fpeak (a1(t)) Epeak/Etot (p′)
4.5 1.30 0.14 0.44 40.3 0.463 0.168 10.1%
5.5 1.43 0.36 0.36 34.2 0.462 0.462 7.1%
6.5 1.59 0.46 0.35 31.2 0.388 0.388 3.1%
7.5 1.72 0.55 0.35 29.3 0.381 0.381 5.9%
8.5 1.84 0.68 0.35 28.5 0.368 0.368 6.4%
 29 August 2026 06:16:57

<!-- PDF_PAGE: 16 -->

016101-15 Vuorinen et al. Phys. Fluids 25, 016101 (2013)
2 2.2 2.4 2.6 2.8 31
1.1
1.2
1.3
1.4
1.5
1.6
1.7
1.8
1.9
2
(po/p∞)0.5
Hdisk/D
 
 
(a)
Present LES
Slope: C = 0.62
Ashkenaz & Sherman (1966): C = 0.67
Ewan & Moodle (1986): C ≈ 0.55
2 2.2 2.4 2.6 2.8 30.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
Clear slip line separation
between NPR=4.5...5.5
(po/p∞)0.5
Wdisk/D
 
 
(b)
Present LES
Ewan & Moodle (1986)
FIG. 14. (a) Dependence of the Mach disk height on the pressure ratio po/p∞ . (b) Dependence of the Mach disk width on
the pressure ratio po/p∞ .
validity of Eq. (11) is investigated in Fig. 14. It is seen that the present LES produces an approximate
slope 0.62 which is in between the earlier predictions. 45, 46 Ewan and Moodie have also investigated
Wdisk and noted that at low NPR the Mach disk width scales with Wdisk /D = Cw
√ po/ p∞ where Cw
is a strong function of NPR.46 A major observation is that the slip lines are very close to each other for
NPR = 4.5 but they become strongly separated when NPR increases to NPR = 5.5. Simultaneously
with increasing Wdisk , the shear layer thickness δand the angle α decrease. Thereby, the jet strongly
changes its character around NPR = 5 into a co-annular jet. The values of Hdisk and Wdisk are also
tabulated in Table II.
F. Mixture quality
Two matters need to be distinguished from each other: (1) injection of a real fuel (e.g., natural gas)
and (2) injection of a passive scalar. First, in a “real” DI NG engine a higher nozzle pressure ratio can
produce a richer mixture on average. A way to argue this is discussed below. We showed previously
that, in line with previous studies, the jet volume evolves as V (t) ∼ (ρo/ρ∞ )3/4t3/2. On the other
hand, the mass ﬂow scales linearly with NPR, i.e., ˙m ∼ ρo/ρ∞ ∼ po/ p∞ (see Fig. 4). The analysis
leads to the conclusion that the global average mixture level cave ∼ (ρo/ρ∞ )1− 3/4 ∼ (ρo/ρ∞ )1/4
indicating that the average concentration levels stay higher when the NPR is higher. However, the
scaling exponent 1/4 is small and, in practical situations with rather narrow pressure operating
conditions, the given analysis implies that NPR has little effect on the mixture richness due to the
favorable scaling of jet volume with exponent 3/4.
In the present LES mixing of a passive scalar is simulated instead of NG. The injection rate
of ρc is kept constant. In fact, this situation is also similar to the PLIF measurements. 13, 14 It is
expected that in such a conﬁguration higher NPR leads to faster mixing of the scalar since the jet
penetrates also faster. In PLIF this is seen as weaker signal levels at high NPR despite the fact
that approximately the same amount of acetone enters the chamber. The global probability density
function (PDF) of ρc over the whole jet volume ( ρc > 0.001) shows the better mixing as seen in
Fig. 15. It is noted that when time proceeds the higher NPR leads to lower concentrations thanks to
rapid volumetric growth. At low NPR the ﬂatter peaks are related to unmixingness and lower RMS.
The peak location gives an idea of how much gas/air has entrained while the peak height relates to
the mixing between the jet and the entrained volume. As is seen, the high NPR have both a higher
and narrower peak so both the entrainment and the mixing are better.
G. Proper orthogonal decomposition
In proper orthogonal decomposition (POD) the aim is to project the turbulent ﬂow ﬁeld on basis
functions that maximize the turbulent kinetic energy content for any subset of the base. 41–44 The
 29 August 2026 06:16:57

<!-- PDF_PAGE: 17 -->

016101-16 Vuorinen et al. Phys. Fluids 25, 016101 (2013)
0.2 0.4 0.6 0.8 10
0.005
0.01
0.015
0.02
ρ c
PDF
 
 
(a) t=85To
po/p∞ = 4.5
po/p∞ = 5.5
po/p∞ = 6.5
po/p∞ = 7.5
po/p∞ = 8.5
0.2 0.4 0.6 0.8 10
0.005
0.01
0.015
0.02
ρ c
PDF
 
 
(b) t=175To
po/p∞ = 4.5
po/p∞ = 5.5
po/p∞ = 6.5
po/p∞ = 7.5
po/p∞ = 8.5
FIG. 15. Time evolution of the probability density of ρc. It is observed that for all times the higher the NPR, the lower the
concentration levels and the better the mixing.
pioneering work on applying POD on turbulent data was carried out by Lumley. 42 Next, we apply
POD on LES data 41–44 to extract information on the coherent ﬂow structures. We apply the POD
method of snapshots by Sirovich 43 in which time snapshots (ρ,ρu,ρv,ρw )s, s = 1, ..., N, where N
= number of snapshots are made zero-mean by subtracting the average and also normalized withρ∞
and U1. Here, the snapshots are 2d cutplanes of the 3d ﬂow ﬁeld. After normalization, the snapshots
are collected as the columns of the snapshot matrix M. The eigenvalue analysis of the autocovariance
matrix C = MTM results in the construction of a basis {ψs}N
s=1 ={ (ϕs
ρ,ϕ s
ρu,ϕ s
ρv,ϕ s
ρw)}N
s=1 which is
arranged in the decreasing order of eigenvalues of C so that λ1 ≥ λ2 ≥ ... ≥ λN. Any snapshot can
be expressed as
(ρ,ρu,ρv,ρw ) =
N∑
i=1
ai (t)ψi , (12)
where the time coefﬁcients ai(t) are computed as inner products (projections) between the snap-
shot and the basis function. 43, 47 The orthogonal modes correspond to the energetic, coherent ﬂow
structures and they are used to extract deterministic features from turbulent data.
Figs. 16(a), 16(c), and 16(d) present mode 1 for three NPRs. For reasons to be explained later,
mode 2 would look visually the same as mode 1 but it would pose a spatial phase shift to ensure
FIG. 16. The shock structures shown together with the non-vanishing part of the density mode ( ϕρ) superposed with the
velocity vectors of the momentum mode ( ϕρw,ϕρu ). (a) po/p∞ = 4.5, mode 1, (b) po/p∞ = 4.5, mode 5, (c) po/p∞ = 6.5,
mode 1, and (d) po/p∞ = 8.5, mode 1.
 29 August 2026 06:16:57

<!-- PDF_PAGE: 18 -->

016101-17 Vuorinen et al. Phys. Fluids 25, 016101 (2013)
orthogonality between modes 1 and 2. In addition to mode 1, Fig. 16(b) also presents mode 5 for
NPR = 4.5. We show the modes after the Mach disk only, since the related modes vanish near
the nozzle exit where the variance content is very small as seen also from the RMS of velocity in
Fig. 12. Instead, this part is replaced with the ﬁrst shock cell in order to better relate the mode
location with the shock structures. As is seen in Fig. 16, increasing the NPR changes the shape and
extent of the modes. At NPR = 4.5, mode 1 shows anti-symmetric alternating pockets of positive
and negative density ﬂuctuations. As the vectors show, these structures correspond to a collection
of aligned vortices: any vortex is a counter-rotation with respect to the previous or the following
vortex. The observed vortex size is approximately D. The vortices are positioned within the slip lines
explaining the vortex dimension. For NPR = 4.5, mode 5 shows a similar pattern but the wavelength
is shorter.
Previously it was shown that increasingNPR channels momentum to the shear layer which gives
the jets a co-annular character. As is seen in Fig. 16, also the dominant mode changes shape: small
vortex structures appear in the inner and outer shear layers. The axial wavelength of repeating pattern
decreases to ∼ D and the vortex size becomes ∼ D/2. For NPR = 6.5 and 8.5, the modes look similar
but they start further downstream with increasing NPR (z/D ∼ 4a t NPR = 8.5 compared to z/D ∼ 3.5
at NPR = 6.5). At NPR = 6.5 and 8.5, the dominant mode is concentrated in the annular jet created
by the slip lines until the opposite sides of the jet meet on z-axis. For all NPR, the development of
the dominant mode is constrained by the ﬂow topology. The location of the shear-layer, as seen in
Fig. 16, inﬂuences the mode shape and associated vortex size and location. In general, the results
indicate that for all the NPR mode 1 begins after the second normal shock (Mach disk being the ﬁrst
normal shock).
Fig. 19(a) shows the POD eigenvalue spectrum (λ
i//Sigma1jλj) for different NPR. Modes 1 and 2 cover
about 6% –12% of the variance content and it is noted that λ1 is very close to λ2. Visual inspection of
modes 1 and 2 conﬁrms that they look structurally very similar and pose the same spatial wavelength.
However, a spatial phase shift is observed ensuring orthogonality between the modes. The presence
of mode pairs is common in swirling ﬂows and they can be related to a rotational ﬂow component. 36
Mode pairs were also reported for systems without swirl 36, 47 but without lower relative intensity
(in terms of fraction of variance covered by the pair alone). The fraction of variance covered by
mode pair (1,2) is function of the NPR with higher NPR exhibiting about 10% –12 % of the variance
of the variable vector. As can be seen from Fig. 17(b), the variance distribution is relatively ﬂat
unlike in swirling ﬂows. In fact with the present sampling ensembles, about 50 modes are needed
to reproduce 50% of the variance. Subsequent modes of the pair (1,2) may also present a deﬁned
coherent structure and appear as a pair, e.g., modes 5 and 6 at NPR = 4.5 and 8.5. However, they
contain a smaller fraction of the variance.
Next, the time variation of the POD modes is analyzed. Fig. 18(a) shows the time coefﬁ-
cients indicating that a
1(t) and a2(t) are harmonic functions with a phase shift. Both have the
0 5 10 15 200
0.01
0.02
0.03
0.04
0.05
0.06
0.07
Eigenvalue
λi/Σi λi
 
 
(a) Pairing of modes 1 and 2
for all po/p∞
Pairing of modes 5 and 6
for po/p∞=4.5
Pairing of modes 5 and 6
for po/p∞=8.5
po/p∞=4.5
po/p∞=5.5
po/p∞=6.5
po/p∞=7.5
po/p∞=8.5
0 20 40 60 80 1000
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
Total Energy in N First Modes
N
 
 
(b)
po/p∞=4.5
po/p∞=5.5
po/p∞=6.5
po/p∞=7.5
po/p∞=8.5
FIG. 17. (a) POD eigenvalue spectrum. (b) Cumulative energy in the ﬁrst N POD modes.
 29 August 2026 06:16:57

<!-- PDF_PAGE: 19 -->

016101-18 Vuorinen et al. Phys. Fluids 25, 016101 (2013)
50 60 70 80 90 100−1
−0.5
0
0.5
1
Time
(a)
POD Time Coefficient
 
 
a1(t)
a2(t)
−1 −0.5 0 0.5 1−1
−0.5
0
0.5
1
a1(t)
a2(t)
(b)
FIG. 18. (a) POD time coefﬁcients a1(t)a n d a2(t) showing the coupling between mode pair (1, 2) for po/p∞ = 8.5. (b) Plot
of a1(t)v s a2(t) revealing the pairing for po/p∞ = 8.5.
same characteristic frequency and they undergo the same amplitude modulation. Lissajous’ plot in
Fig. 18(b) indicates circular trajectory giving a phase shift of π/2. The same observation holds
true for all the mode pairs (1,2) in the investigated NPR range. The temporal phase shift en-
sures orthogonality of the time terms and is common for POD modes that appear in pairs. 36, 37 In
Fig. 19, frequency analysis in Fourier space is carried out. In line with the deﬁnition of the integral
timescale, frequencies are normalized by 1/ To and the Strouhal number is deﬁned as St = fD/2U1.
This deﬁnition is directly linked to the standard deﬁnition of Strouhal number by the factor 1/2 due
to different deﬁnition of the characteristic velocity. In Fig. 19(a) the POD time coefﬁcients evidence
characteristic frequencies as distinct peaks as expected also from Fig. 18.F i g .19(b) reveals similar
peaks in the spectrum of pressure ﬂuctuation probed at z/D = 10, r/D = 3 in the far ﬁeld of the jet. To
complement Fig. 19, Table II summarizes the frequencies of the dominant peaks. For NPR > 4.5, the
peak frequency matches the dominant peak frequency in the power spectra of pressure ﬂuctuation.
This indicates that the coherent structures are a powerful acoustic source. In fact, although the mode
pair (1,2) accounts for only 6%–12% of the variance, it is clearly a strong source for the pressure
ﬂuctuation. This is explained by the location of the coherent structures right downstream of the
Mach disk in a region of high shear and relatively strong density gradient. Obviously, this region is
a strong source of noise.
For NPR = 4.5, the characteristic frequency of a
1 and a2 is about three times lower than the
dominant pressure frequency. However, the measured pressure frequency matches the characteristic
0 0.2 0.4 0.6 0.80
0.2
0.4
0.6
0.8
1
1.2
(a)
St
PSD of POD Time Coefficient
 
 
Acoustic modes (1,2) for po/p∞ > 4.5
Acoustic modes (5,6) for po/p∞ = 4.5
Non−acoustic mode (1,2)
for po/p∞ = 4.5
po/p∞=4.5
po/p∞=5.5
po/p∞=6.5
po/p∞=7.5
po/p∞=8.5
0 0.2 0.4 0.6 0.80
0.2
0.4
0.6
0.8
1
1.2
St
PSD of Pressure Fluctuation (b)
 
 
Acoustic peaks due to mode pair (1,2) for po/p∞ > 4.5
Acoustic peak due to mode pair (5,6) for po/p∞ = 4.5
po/p∞=4.5
po/p∞=5.5
po/p∞=6.5
po/p∞=7.5
po/p∞=8.5
FIG. 19. (a) The spectra of POD time coefﬁcients. (b) The spectra of pressure ﬂuctuation sampled outside of the turbulent
region at z/D = 10, r/D = 3.
 29 August 2026 06:16:57

<!-- PDF_PAGE: 20 -->

016101-19 Vuorinen et al. Phys. Fluids 25, 016101 (2013)
FIG. 20. The helical density modes in 3d constructed from the 2d mode pair (1,2) using the phase function. (a) po/p∞ = 4.5,
|m|= 1, (b) po/p∞ = 6.5, |m|= 1, (c) po/p∞ = 8.5, |m|= 1, and (d) po/p∞ = 8.5, |m|= 2.
frequency of mode pair (5,6) indicating that this mode pair strongly inﬂuences sound emission. It
should be noted that in this case, mode pair (5,6) contributes to approximately 4% of the variance
but despite of their relatively low intensity, they have a clear link to the sound emission. We note that
the observed peak frequency range is in line with the literature data4 from the viewpoint of dominant
ﬂow generated Strouhal numbers decreasing with NPR. For the present converging nozzle, also the
range of the ﬂow generated peak Strouhal numbers is close to the experimentally observed range
reported by Munday et al. for converging-diverging nozzles.4
The spatial structure of the dominant POD modes corresponds to a helical mode. Combining
the harmonic behavior of a rotation and the axial motion gives a phase function P(kzz +| m|θ− ωt)
where θ is the azimuthal angle, kz is the axial wavenumber, |m| is the azimuthal wave number and
ω is the pulsation angular frequency. The pulsation is related to St ∼ ω/2π and from Fig. 16,w e
have k ∼ π/D for NPR = 4.5 and k ∼ 2π/D otherwise. The antisymmetry shown earlier for mode
pair (1,2) gives an azimuthal wavenumber |m|= 1 and characterizes the helical mode. Gutmark
et al.49 reported that the dominant mode in a similar conﬁguration satisﬁed |m|= 1, supporting the
present ﬁnding. However, they did not reveal the helical nature of the mode nor characterize the
spatial extent. It is noted that the phase velocity
ω
k ≈ 0.8U1 for all the cases. Since the pulsation
frequency was found to be a constant, the group velocity dω
dk ≈ 0, indicating an absolute instability.
These ﬁndings are well in line with helical modes appearing in swirling ﬂows. 36
At a ﬁxed instant of time t, the phase function can be used to construct a 3d visualization out
of the 2d mode in ( z, r, θ) space. In particular, the angular location and time are related. The ﬁeld
can then be converted from cylindrical into Cartesian coordinates. Fig. 20 shows a 3d view of the
helical modes as an iso-surface of the density component constructed using the mode pair (1,2). The
blue and red iso-surfaces show the same iso-level but with opposite signs. The double helix shape of
opposite sign is common to all cases for mode pair (1,2). For NPR = 4.5, the envelope of the helices
expands to reach a maximum of about 3 D at z/D ≈ 5. The axial extent of the helix is about 8 D.F o r
higher NPR, the envelop shows a rather constant diameter of ≈ 2D. In these cases, the helices start
after the second normal shock at the slip lines and the helices follow closely the density gradient and
the annular shear-layers. The helices show a well characterized absolute instability with two leading
branches being always located at the same axial location and rotating. In addition to the observed
azimuthal modes |m|= 1, an example construction of the harmonic mode featuring |m|= 2i ss h o w n
for NPR = 8 . 5i nF i g .20(d). Similar to the dominant modes |m|= 1, helices of opposite sign (2+2i n
this case) issue at the slip lines. The four leading branches rotate but stay at the same axial location
in time. The present ﬁndings give strong support to previous ﬁndings by for example Munday et al.
4
who concluded that the pressure ﬂuctuations in the region 5 ≤ z/D ≤ 10 form the source for the
shock-associated noise. The location of the POD modes and the provided link between the dominant
frequencies evidence the signiﬁcance of the helical mode in the noise production.
 29 August 2026 06:16:57

<!-- PDF_PAGE: 21 -->

016101-20 Vuorinen et al. Phys. Fluids 25, 016101 (2013)
IV . CONCLUSIONS
The present work had four objectives. First, a LES gas jet injection model was to be developed for
fuel jet studies. To our best knowledge, the present study provides the ﬁrst systematic assessment on
the pressure ratio dependency of highly underexpanded jet structure using LES. Second, we wanted to
further assess the recommendations by Pirozzoli
31 in developing low-dissipative numerical methods
for LES of high speed ﬂows on unstructured grids. We applied the new SSD scheme by Vuorinen
et al.34 in supersonic ﬂows. Third, we wanted to reproduce the classical structures of high pressure
jets including the Mach disk, the barrel shock, reﬂected shock waves and a sequence of shock cells.
The dimensions of the Mach disk were in close agreement with previous literature. 45, 46 Fourth,
our aim was to use POD in supersonic jets and link the dominant jet structures and frequencies
with NPR and to the dominant acoustic peaks in the pressure spectra. To our knowledge POD of
underexpanded jets has not been carried out previously.
The main quantitative ﬁndings of this work are summarized in Table II where the Mach disk
dimensions, annular shear layer thickness, shock reﬂection angle and peak Strouhal numbers are
reported. The new physics in the present study involves the POD modes and the investigation of
transient development of the shocks. Also LES of highly underexpanded jets is a rather new topic
itself and many of the results reported herein have not been investigated with such detail in previous
experimental studies.
Other new ﬁndings of the work are summarized as follows: (1) A scaling law V (t)
∼ ( p
o/ p∞ )3/4t3/2 is proposed for the timewise volumetric expansion of the jets. This result is
in agreement with the tip penetration scaling with t1/2. (2) From global perspective, the penetration
of the jet dictates the dilution of the concentration. (3) The Mach disk width Wdisk = Wdisk (NPR )
was noted to increase rapidly around NPR ≈ 5. The consequent increase of slip line separation
distinguishes highly underexpanded jets from lower pressure jets when the co-annular nature of the
shear layers becomes emphasized. (4) The co-annular shear layers at higher NPR induce smaller
vortex structures than seen for lower NPR as seen in POD. (5) The dominant structures indicate
a helical mode. The spatial location and shown dynamics of the mode strongly complements the
previously existing picture on noise production.
4 (6) The peak frequencies of the POD coefﬁ-
cients explain the peak frequencies of the pressure ﬂuctuation. The decrease of the observed peak
Strouhal numbers with NPR as well as the St range of the peaks matches well the picture from the
literature.4
As the present study showed, orthogonal decompositions can shed signiﬁcant light to the physics
of supersonic jets. Our future research will involve studies on mixing of cold high speed jets in hot
environments which is a situation close to reality in DI NG engines. POD will certainly be used also
in the upcoming studies.
ACKNOWLEDGMENTS
The study has been funded by the postdoctoral program of the Aalto University. The computa-
tional resources for this study were provided by CSC, the Finnish IT Center for Science Ltd. The
study has beneﬁted from three travel grants provided by the HPC-Europa2 project.
1 C. D. Donaldson and R. S. Snedeker, “A study of free jet impingment. Part 1. Mean properties of free and impinging jets,”
J. Fluid Mech. 45, 281–319 (1971).
2 K. B ¨ulent and M. V . ¨Ot¨ugen, “Scaling parameters of underexpanded supersonic jets,” Phys. Fluids 14, 4206–4215 (2002).
3 S. G. Chuech, M.-C. Lai, and G. M. Faeth, “Structure of turbulent sonic underexpanded free jets,” AIAA 26th Aerospace
Sciences Meeting, Reno, Nevada, 1988.
4 D. Munday, E. Gutmark, J. Liu, and K. Kailasanath, “Flow structure and acoustics of supersonic jets from conical
convergent-divergent nozzles,” Phys. Fluids 23, 116102 (2011).
5 A. Dauptain, B. Cuenot, and Y . M. Gicquel, “Large-eddy simulation of a stable supersonic jet impinging on ﬂat plate,”
AIAA J. 48(10), 2325–2337 (2010).
6 T. J. S. Jothi and K. Srinivasan, “Role of initial conditions on noise from underexpanded pipe jets,”Phys. Fluids 21, 066103
(2009).
7 J. Panda and G. Seasholtz, “Measurement of shock structure and shock-vortex interaction in underexpanded jets using
Rayleigh scattering,” Phys. Fluids 11, 3761 (1999).
8 K. Wohletz and G. Heiken, V olcanology and Geothermal Energy (University of California Press, Berkeley, 1992),
C h a p .1 ,p .2 9 .
 29 August 2026 06:16:57

<!-- PDF_PAGE: 22 -->

016101-21 Vuorinen et al. Phys. Fluids 25, 016101 (2013)
9 V . V . Golub, D. I. Baklanov, T. V . Bazhenova, M. V . Bragin, S. V . Golovastov, M. F. Ivanov, and V . V . V olodin, “Shock-
induced ignition of hydrogen gas during accidental or technical opening of high-pressure tanks,” J. Loss Prev. Process Ind.
20(4–6), 439–446 (2007).
10 P . G. Hill and P . Ouellette, “Transient turbulent gaseous fuel jets for diesel engines,” J. Fluids Eng. 121, 93–101
(1999).
11 P . Ouellette and P . G. Hill, “Turbulent transient gas injections,”J. Fluids Eng. 122, 743–753 (2000).
12 T. R. White and B. E. Milton, “Shock wave calibration of underexpanded natural gas fuel jets,” Shock Waves 18, 353–364
(2008).
13 J. Y u, V . Vuorinen, H. Hillamo, O. Kaario, and M. Larmi, “An experimental investigation on the ﬂow structure and
mixture formation of low pressure ratio wall-impinging jets by a natural gas injector,” J. Nat. Gas Sci. Eng. 9, 1–10
(2012).
14 J. Y u, V . Vuorinen, H. Hillamo, O. Kaario, and M. Larmi, “An experimental investigation on high pressure pulsed jets for
DI gas engine using planar laser-induced ﬂuorescence (PLIF),” SAE Technical Paper Series, 2012-01-1655, 2012.
15 V . Vuorinen, H. Hillamo, O. Kaario, M. Nuutinen, M. Larmi, and L. Fuchs, “Large-eddy simulation of droplet stokes
number effects on mixture quality in fuel sprays,” Atomization Sprays 20, 435–451 (2010).
16 V . Vuorinen, A. Wehrfritz, J. Y u, O. Kaario, M. Larmi, and B. Boersma, “Large-eddy simulation of subsonic jets,”J. Phys.:
Conf. Ser. 318, 032052 (2011).
17 E. Garnier, N. Adams, and P . Sagaut, Large Eddy Simulation for Compressible Flows (Springer, 2009).
18 J. Kim and H. Choi, “Large eddy simulation of a circular jet: effect of inﬂow conditions on the near ﬁeld,” J. Fluid Mech.
620, 383–411 (2009).
19 M. Olsson and L. Fuchs, “Large eddy simulation of the proximal region of a spatially developing circular jet,” Phys. Fluids
8, 2125–2137 (1996).
20 B. J. Boersma, G. Brethouwer, and F. T. M. Nieuwstadt, “A numerical investigation on the effect of the inﬂow conditions
on the self-similar region of a round jet,” Phys. Fluids 10, 899–909 (1998).
21 C. Bogey and C. Bailly, “A family of low dispersive and low dissipative explicit schemes for ﬂow and noise computations,”
J. Comput. Phys. 194, 481–491 (2004).
22 B. J. Boersma, “A staggered compact ﬁnite difference formulation for the compressible Navier-Stokes equations,” J.
Comput. Phys. 208, 2 (2005).
23 C. Bogey, N. de Cacqueray, and C. Bailly, “A shock-capturing methodology based on adaptive spatial ﬁltering for
high-order non-linear computations,” J. Comput. Phys. 228, 1447–1465 (2009).
24 N. de Cacqueray, C. Bogey, and C. Bailly, “Investigation of a high Mach number overexpanded jet using large-eddy
simulation,” AIAA J. 49, 10 (2011).
25 S. Kawai, S. Shankar, and K. Lele, “Assessment of localized artiﬁcial diffusivity scheme for large-eddy simulation of
compressible turbulent ﬂows,” J. Comput. Phys. 229, 1739–1762 (2010).
26 S. Kawai and K. Lele, “Large-eddy simulation of jet mixing in supersonic crossﬂows,” AIAA J. 48, 2063–2083
(2010).
27 Z. A. Rana, B. Thornber, and D. Drikakis, “Transverse jet injection into a supersonic turbulent cross-ﬂow,” Phys. Fluids
23, 046103 (2011).
28 A. Cook and W. Cabot, “Hyperviscosity for shock-turbulence interactions,” J. Comput. Phys. 203(2), 379–385
(2005).
29 A. Bhagatwala and S. Lele, “A modiﬁed artiﬁcial viscosity approach for compressible turbulence simulations,” J. Comput.
Phys. 228, 4965–4969 (2009).
30 A. Mani, J. Larsson, and P . Moin, “Suitability of artiﬁcial bulk viscosity for large-eddy simulation of turbulent ﬂows with
shocks,” J. Comput. Phys. 228, 7368–7374 (2009).
31 S. Pirozzoli, “Numerical methods for high-speed ﬂows,” Annu. Rev. Fluid Mech. 43, 163–194 (2011).
32 Z. Pouransari, G. Brethouwer, and A. V . Johansson, “Direct numerical simulation of an isothermal reacting turbulent
wall-jet,” Phys. Fluids 23, 085104 (2011).
33 L.-W. Chen, G.-L. Wang, and X.-Y . Lu, “Numerical investigation of a jet from a blunt body opposing a supersonic ﬂow,”
J. Fluid Mech. 684, 85–110 (2011).
34 V . Vuorinen, P . Schlatter, L. Fuchs, M. Larmi, and B. Boersma, “A low-dissipative, scale-selective discretization scheme
for the Navier-Stokes equations,” Comput. Fluids 70, 195–205 (2012).
35 C. Duwig, M. Salewski, and L. Fuchs, “Large eddy simulation of a turbulent ﬂow past two symmetric backward-facing
steps: a sensitivity analysis,” AIAA J. 46(2), 408–419 (2008).
36 C. Duwig and E. Gutmark, “Large scale rotating motions in a multiple jets,” Phys. Fluids 20, 041705
(2008).
37 C. Duwig and L. Fuchs, “Large eddy simulation of vortex breakdown/ﬂame interaction,” Phys. Fluids 19, 075103
(2007).
38 C. Fureby and F. F. Grinstein, “Large eddy simulation of high-Reynolds-number free and wall-bounded ﬂows,” J. Comput.
Phys. 181, 1, 68–97 (2002).
39 F. F. Grinstein and C. Fureby, “Recent progress on MILES for high Reynolds number ﬂows,” J. Fluids Eng. 124, 848
(2002).
40 L. G. Margolin, P . K. Smolarkiewicz, and A. A. Wyszgrodzki, “Implicit turbulence modeling for high Reynolds number
ﬂows,” J. Fluids Eng. 124, 862 (2002).
41 A. Chatterjee, “An introduction to the proper orthogonal decomposition,” Curr. Sci. 78(7), 808–817 (2000).
42 G. Berkooz, P . Holmes, and J. L. Lumley, “The proper orthogonal decomposition in the analysis of turbulent ﬂows,”Annu.
Rev. Fluid Mech. 25, 539–575 (1993).
43 L. Sirovich, “Turbulence and the dynamics of coherent structures. Part 1: Coherent structures,” Quart. Appl. Math.XLV(3),
561–571 (1987).
 29 August 2026 06:16:57

<!-- PDF_PAGE: 23 -->

016101-22 Vuorinen et al. Phys. Fluids 25, 016101 (2013)
44 J. Bor ´ee, “Extended proper orthogonal decomposition: a tool to analyse correlated events in turbulent ﬂows,” Exp. Fluids
35, 188–192 (2003).
45 H. Ashkenaz and F. S. Sherman, Rareﬁed Gas Dynamics, edited by J. H. de Leeuw (Academic, New Y ork, 1966), V ol. 1,
p. 84.
46 B. C. R. Ewan and K. Moodie, “Structure and velocity measurements in underexpanded jets,” Combust. Sci. Technol. 45,
275–288 (1986).
47 K. E. Meyer, J. M. Pedersen, and O. ¨Ozcan, “A turbulent jet in crossﬂow analyzed with proper orthogonal decomposition,”
J. Fluid Mech. 583, 199–227 (2007).
48 H. G ¨ortler, “Dreidimensionales zur stabilittstheorie laminarer grenzschichten,” J. Appl. Math. 35, 362–363 (1955).
49 E. Gutmark, K. C. Schadow, and C. J. Bicker, “Mode switching in supersonic circular jets,” Phys. Fluids A 1, 868 (1989).
 29 August 2026 06:16:57
