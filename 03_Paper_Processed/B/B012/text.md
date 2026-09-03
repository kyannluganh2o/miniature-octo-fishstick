<!-- PDF_PAGE: 1 -->

International Journal of Heat and Fluid Flow 61 (2016) 711–729 
Contents lists available at ScienceDirect 
International Journal of Heat and Fluid Flow 
journal homepage: www.elsevier.com/locate/ijhff 
Numerical modelling of transient under-expanded jets under different 
ambient thermodynamic conditions with adaptive mesh reﬁnement 
A. Hamzehloo, P.G. Aleiferis ∗
Department of Mechanical Engineering, Imperial College London, Exhibition Road, London SW7 2AZ, UK 
a r t i c l e i n f o 
Article history: 
Received 1 December 2015 
Revised 21 May 2016 
Accepted 27 July 2016 
Available online 4 August 2016 
Keywords: 
Under-expanded jet 
Vortex ring 
Shear layer 
Mach disk 
Reﬂected shock 
Turbulent mixing 
Adaptive mesh 
a b s t r a c t 
The mixing characteristics of highly turbulent under-expanded gaseous fuel jets issued from millimeter- 
size circular nozzles are important for developing advanced direct injection gaseous-fuelled internal 
combustion engines. In the present study high-resolution large eddy simulation in conjunction with an 
adaptive mesh reﬁnement technique was used in order to investigate key mixing characteristics of under- 
expanded hydrogen and methane jets under various ambient thermodynamics. Penetration rate, volumet- 
ric growth and initial transient vortex ring behaviour were investigated under near atmospheric and el- 
evated ambient pressures and temperatures, P ∞  ≈ 1 bar and 10 bar, T ∞  =296 K and 600 K, using a nozzle 
pressure ratio of 10. The conditions corresponded to injection strategies ranging from late intake stroke 
around inlet valve closure to late compression. It was observed that increasing the ambient temperature 
at constant pressure resulted in increase in both tip penetration and volumetric growth of the under- 
expanded jets. It was also found that the effect of diffusivity, ratio of speciﬁc heats and ambient density 
must be considered when scaling volumetric growth of under-expanded jets of different gases and/or 
when issued into different ambient temperatures. Moreover, substantial differences were observed be- 
tween the transient jet formation of hydrogen and methane fuels. It was found that the embedded shock 
structures and supersonic annular shear layers played a signiﬁcant role in the formation and evolution of 
the transient preliminary and secondary vortex rings. It was also noted that the evolution of the vortex 
ring inﬂuenced signiﬁcantly the volumetric growth and hence mixing quality of under-expanded jets. 
©2 0 1 6 Elsevier Inc. All rights reserved. 
1. Introduction 
Powering internal combustion (IC) engines with hydrogen or 
methane gas is one of the proposed resolutions to diversify pro- 
gressively towards use of cleaner energy carriers particularly for 
the transportation sector ( Cho and He, 2007; Verhelst, 2014 ). Direct 
injection (DI) of fuels into the combustion chamber is believed to 
be the most appropriate fuelling approach for advanced gaseous- 
fuelled IC engines. This is because DI can deliver relatively high 
volumetric eﬃciency when compared to port fuel injection and 
also provides extensive ﬂexibility in controlling the air/fuel mix- 
ture homogeneity and stratiﬁcation through a broad range of in- 
jection strategies ( Scarcelli et al., 2011; Hamzehloo and Aleiferis, 
2013; Hamzehloo and Aleiferis, 2014a ). High injection pressures are 
typically used for gaseous DI fuelling in order to achieve the re- 
quired mass ﬂow rates and promote air/fuel mixing ( Hamzehloo 
and Aleiferis, 2013; Hamzehloo and Aleiferis, 2014a ). 
∗ Corresponding author. 
E-mail address: p.aleiferis@imperial.ac.uk (P.G. Aleiferis). 
High injection pressures normally lead to the formation of 
highly under-expanded jets past the nozzle exit of gaseous fuel in- 
jectors ( Scarcelli et al., 2011; Hamzehloo and Aleiferis, 2013 ). The 
main characteristics of a gaseous jet injected from a circular noz- 
zle are mainly affected by the ratio of the upstream (nozzle) to- 
tal pressure ( P 0 ) to the ambient (combustion chamber) static pres- 
sure ( P ∞  ), the nozzle pressure ratio NPR = P 0 / P ∞  . Gaseous jets are 
normally categorized as subsonic, moderately under-expanded and 
highly under-expanded depending on their NPR level ( Donaldson 
and Snedeker, 1971 ). The jets are typically considered to be highly 
under-expanded for NPR ≥ 4 ( Donaldson and Snedeker, 1971 ). At 
such conditions, Mach reﬂection occurs a few diameters down- 
stream of the nozzle exit and forms a slightly curved strong nor- 
mal shock, called the Mach disk ( Donaldson and Snedeker, 1971; 
Vuorinen et al., 2013; Hamzehloo and Aleiferis, 2014b ). The dis- 
tance of the Mach disk from the nozzle exit, i.e. the Mach disk 
height, and its respective width, are both strongly affected by NPR. 
A transient under-expanded jet contains a three-dimensional vor- 
tex ring which in addition to the Mach reﬂection contributes to the 
formation of three-dimensional annular shear layers ( Golub, 1994; 
Edgington-Mitchell et al., 2014 ). Vortex breakdown and/or vortex 
merging within these shear layers promotes mixing of the jet with 
http://dx.doi.org/10.1016/j.ijheatﬂuidﬂow.2016.07.015 
0142-727X/© 2016 Elsevier Inc. All rights reserved.

<!-- PDF_PAGE: 2 -->

712 A. Hamzehloo, P.G. Aleiferis / International Journal of Heat and Fluid Flow 61 (2016) 71 1–729 
the ambient medium ( Krothapalli et al., 1998 ). As a result, funda- 
mental understanding of the aforementioned vortical structures of 
transient hydrogen and methane under-expanded jets is necessary 
in order to shed more light on the mixing characteristics of alter- 
native gaseous fuels. 
Various experimental and computational works have been de- 
voted to under-expanded jets, using predominantly air or nitro- 
gen issued from large diameter nozzles, mainly for aerospace ap- 
plications. Recently, studies were conducted on under-expanded 
jets injecting from comparable nozzle diameters to those of typi- 
cal gaseous IC engine injectors ( D ≤ 2.0 mm) ( Vuorinen et al., 2013; 
Yu et al., 2013; Vuorinen et al., 2014 ). The latter studies used 
large eddy simulation (LES) but were mainly limited to relatively 
low NPR values (NPR ≤ 8) and to gases with fairly low diffusivity 
and/or speed of sound such as air, nitrogen and methane. This is 
due to the fact that high NPR values and/or gases with high dif- 
fusivity and speed of sound (such as hydrogen or helium) form 
relatively wide transient vortex rings and ‘bulky’ jets that require 
a fairly large number of computational elements for high-ﬁdelity 
LES. Adaptive mesh reﬁnement (AMR) is a possible solution to 
control the number of computational cells over the solution do- 
main and has been employed successfully for various applications. 
However, with respect to under-expanded jets, very limited com- 
putational studies are available on the basis of AMR ( Prudhomme 
and Haj-Hariri, 1994; Zhang et al., 2014 ). The present work aims 
to extend the previous studies of the current authors on under- 
expanded jets ( Hamzehloo and Aleiferis, 2014b, c ) by: 
• Reporting on the development of a fully automated adaptive 
mesh reﬁnement technique within the computational frame- 
work of STAR-CCM + using Java user coding speciﬁcally for 
under-expanded jets. 
• Performing direct comparison between the key mixing charac- 
teristics of under-expanded hydrogen and methane jets under 
near atmospheric and elevated ambient pressures and temper- 
atures, P ∞  ≈ 1bar and 10bar, T ∞  = 296K and 600K. The con- 
ditions corresponded to injection strategies ranging from late 
intake stroke around inlet valve closure to late compression. 
To the author’s best knowledge the present work is the ﬁrst to 
use LES with AMR in order to discuss the characteristic behaviour 
of hydrogen and methane fuel jets under engine-like conditions of 
ambient pressure and temperature. 
2. Methodology 
2.1. Computational framework 
The main aspects of the numerical methodology employed in 
order to conduct the present LES study within STAR-CCM + have 
been discussed previously by the current authors ( Hamzehloo and 
Aleiferis, 2014b, c, 2016 ). Nevertheless, for the immediate beneﬁt 
of the reader, a brief description is also included here. 
The governing equations of a multi-species viscous compress- 
ible ﬂow, i.e. the equations that describe the conservation of mass, 
momentum and energy ( Eqs. (1) –(3) ), as well as an equation to 
model the transport of species ( Eq. (4) ), are listed as follows 
( Ferziger and Peric, 2002 ): 
∂ρ
∂t 
+ ∇ • ( ρU ) = 0 (1) 
∂ ( ρU ) 
∂t 
+ ∇ • [ U ( ρU ) ] + ∇ p − ∇ • σ = 0 (2) 
∂ ( ρE ) 
∂t 
+ ∇ • [ U ( ρE ) ] + ∇ • ( U p ) − ∇ • ( σ • U ) + ∇ • q = 0 (3) 
∂ ( ρY i ) 
∂t 
+ ∇ • ρU Y i = ∇ • ( ρD i ∇ Y i ) (4) 
where ρ is density, U represents the velocity vector U ( u i , u j , u k ), 
p is pressure, σ is the Cauchy stress tensor that if the ﬂuid is 
assumed to obey Newton’s law of viscosity can be written as: 
σ = μ[ ∇ U + ( ∇ U ) T ] − ( 2 
3 μ∇ • U ) I where T is the matrix transpose 
operator, μ is the dynamic viscosity and I is the identity tensor. In 
a Cartesian coordinate σ can be written as: 
σij = 2 μS ij − 2 
3 
μδij S kk (5) 
where S ij = 1 
2 ( ∂ u i 
∂ x j + 
∂ u j 
∂ x i ) and δij is the Kronecker’s delta. E = e + 
1 
2 | U | 2 is the total speciﬁc energy ( e = e ( T , p ) is the internal en- 
ergy per unit mass, | U | = ( U • U ) 1 / 2 is the magnitude of the veloc- 
ity vector), q = λ∇ T is the heat ﬂux vector ( T is the ﬂuid temper- 
ature and λis a heat conduction coeﬃcient based on the Fourier 
law of heat conduction). For a calorically perfect compressible gas 
pressure and density are coupled using an equation of state as 
p = ρRT , where R is the speciﬁc gas constant. Moreover, e = C v T and 
R = C p − C v , where C v and C p are the speciﬁc heat coeﬃcients for 
constant volume and pressure, respectively. The aforementioned 
heat conduction coeﬃcient may be deﬁned using the molecular 
Prandtl number ( Pr ) as λ= C p μ/P r. The mass fraction of species i th 
is denoted by Y i with a molecular diffusion coeﬃcients of D i . For N 
species, N -1 transport equations are solved and the mass fraction 
of the N th component is calculated from the restriction that the 
total mass fraction must sum to unity. 
In a turbulent ﬂow (like an under-expanded jet) Eqs. (1) –(4) 
are only valid within the Kolmogorov scales ( i.e. direct numerical 
simulation (DNS) limit) in which the spatial and temporal reso- 
lutions are ﬁne enough to capture all scales of the ﬂow ( Pope, 
20 0 0 ). However, at the present time conducting DNS on complex 
ﬂuid ﬂows and speciﬁcally on complex computational domains is 
not computationally practical due to the technological restriction 
(high computational costs). In the current study LES was employed 
in which the governing equations are ﬁltered so that turbulence 
scales greater than a ﬁlter size (typically associated with the grid 
resolution but not necessarily) are resolved directly and the ef- 
fect of scales smaller than that are accounted for by means of a 
subgrid-scale (SGS) modelling approach ( Pope, 20 0 0 ). Using the 
Favre averaging and applying the LES ﬁltering to the momentum 
and energy conservation equations results in formation of residual- 
stress tensor due to the existence of non-liner terms ( Pope, 20 0 0 ). 
The residual-stress tensor τR 
ij is deﬁned as: 
τR 
ij = ρ (
˜ u i u j − ˜ u i ˜ u j 
)
(6) 
where ρ denotes the ﬁltered density and ∼ represents a Favre - 
averaged quantity. The anisotropic part of the residual-stress tensor 
is deﬁned as: 
τr 
ij = τR 
ij − 2 
3 
k r δij (7) 
where k r is the residual kinetic energy deﬁned as k r ≡ 1 
2 τR 
ii . 
In order to form a determined set of governing equations a 
Boussinesq type hypothesis may be used in order to model the 
anisotropic part of the residual stress tensor as ( Pope, 20 0 0 ): 
τr 
ij = −2 ρνsgs 
(
˜ S ij − 1 
3 
δij ˜ S kk 
)
(8) 
In compressible ﬂows ρνsgs in Eq. (8) is called turbulent vis- 
cosity μt . It is clear that Eqs. (5) and (8) have the same struc- 
ture and it is possible to write σ = μef f  [ ∇ U + ( ∇ U ) T ] − ( 2 
3 ∇ • U ) I 
after LES ﬁltering of Eqs. (2) and (3) where μeff is called effec- 
tive viscosity and calculated as μef f  = μ + μt . In order to add

<!-- PDF_PAGE: 3 -->

A. Hamzehloo, P.G. Aleiferis / International Journal of Heat and Fluid Flow 61 (2016) 71 1–729 713 
the effect of turbulence on the heat transfer and diffusion in the 
energy and species transport equation μt is also applied to cal- 
culate effective thermal conductivity and diffusion coeﬃcients as 
λef f  = C p μef f  /P r t and D ef f  = D i + μt /S c t , respectively. Pr t and Sc t 
are turbulent Prandtl and turbulent Schmidt numbers, respectively 
and both had a value of 0.7 in the current study. In practice for LES 
modelling, computational ﬂuid dynamics (CFD) codes use the gov- 
erning equations with similar structures as presented in Eqs. (1) –
(4) with μeff replacing μ and U representing the resolved velocity 
ﬁeld. 
The wall-adapting local-eddy viscosity (WALE) SGS model 
( Nicoud and Ducros, 1999 ) was employed in the present study. This 
model is based on the square of the velocity gradient tensor and 
can take into account both shear and rotation. In comparison to the 
classical Smagorinsky model, the WALE model produces zero eddy 
viscosity in the case of a pure shear (may occur in free jets) that 
makes it capable of reproducing turbulent transitional processes 
more accurately through the growth of unstable modes ( Nicoud 
and Ducros, 1999 ). In the WALE model μt is calculated as: 
μt = ρ/Delta12 
(
S d 
ij S d 
ij 
)3 / 2 
(˜ S ij ˜ S ij 
)5 / 2 
+ 
(
S d 
ij S d 
ij 
)5 / 4 (9) 
where S d 
ij is the traceless symmetric part of the square of the ve- 
locity gradient tensor ( Pope, 20 0 0 ). /Delta1in Eq. (9) is the ﬁlter cut-off
size and in the current study is obtained as /Delta1= C w V 1 / 3 in which 
C w is a constant with a value of 0.544 and V denotes the volume 
of the local computational cell. 
The governing equations were discretized spatially and tempo- 
rally and consequently converted to a system of linearized alge- 
braic equations by means of the ﬁnite volume (FV) method. The 
linearized governing equations were solved in a coupled approach 
( i.e. simultaneously) by using the Gauss-Seidel iterative technique 
in conjunction with an algebraic multigrid (AMG) method ( Weiss 
et al., 1999 ). The multigrid method is applied in order to acceler- 
ate the solution of the linearized system. Speciﬁcally, the concept 
is that long wavelength errors on the ﬁne level appear as short 
wavelength errors on the coarser levels and hence can be more ef- 
fectively damped out ( Ferziger and Peric, 2002 ). In low Mach con- 
ditions and particularly within the incompressible limits ( Ma < 0.3) 
the compressible governing equations become stiff. This is because, 
the variation of density becomes minute thus the pressure cal- 
culated using density and the equation of state is not associated 
entirely with the velocity ﬁeld obtained from the conservation of 
momentum. Therefore, extra treatment is required to develop a 
computational framework for arbitrary Mach number from the sub- 
sonic to the supersonic limits. In the current study preconditioning 
of the governing equations in conjunction with dual time-stepping 
( Weiss and Smith, 1995 ) is used in order to overcome the stiff- 
ness of the governing equations within low Mach number lim- 
its that may occur in locations within the volume of an under- 
expanded jet. Preconditioning of the governing equations destroys 
their time accuracy therefore for the second order implicit time 
marching approach used here it is required to perform some num- 
ber of inner iterations to converge the solution for a given time 
step (dual time-stepping). The inner iterations is accomplished us- 
ing implicit spatial integration that marches them using optimal 
pseudo-time steps ( /Delta1τ) which are determined from the Courant–
Friedrichs–Lewy (CFL) condition ( Weiss et al., 1999 ) as: 
/Delta1τ= min 
(
CFL 
| U | 
λmax 
, σ( /Delta1x ) 2 
ν
)
(10) 
where λmax is the maximum eigenvalue of the system of the lin- 
earized equations, σ is the von Neumann number ( σ ≈ 1). For the 
current study a value of CFL as low as 0.2 was employed initially 
which then increased gradually using a linear ramp. 
A modiﬁed version of the advection upstream splitting method 
(AUSM + -up) ( Liou, 2006 ) was applied in order to express the invis- 
cid ﬂuxes. AUSM + -up is accurate and robust in solving ﬂuid ﬂows 
containing any arbitrary range of velocity magnitudes and partic- 
ularly high speed ﬂows that contain extreme ﬂow discontinuities 
such as shock waves ( Liou, 2006 ). AUSM + -up uses a separate split- 
ting for the pressure terms of the governing equations and avoids 
an explicit artiﬁcial dissipation; the mass ﬂux and pressure ﬂux 
are calculated on the basis of local ﬂow characteristics (including 
the speed of sound) to ensure precise information propagation in- 
side the ﬂuid for convective and acoustic processes ( Liou, 2006 ). 
This reduces the numerical dissipation particularly in high velocity 
ﬂows and consequently avoids wiggles at ﬂow discontinuities such 
as shocks. 
For the cases with hydrogen and methane injection in to air 
the molecular diffusivity was calculated using the Chapman–Enskog 
theory for gaseous diffusion coeﬃcients as follows ( Cussler, 2009 ): 
D i = 
1 . 86 ×10 −3 T 3 / 2 ( 1 / M 1 + 1 / M 2 ) 1 / 2 
P at m σ2 
12 /Omega1
(11) 
where D i is the coeﬃcient of molecular diffusivity in cm 2 /s, T is 
the absolute temperature in K, P atm is the pressure in atm, M 1 
and M 2 are the molecular weights. The quantities σ12 and /Omega1are 
molecular properties; σ12 is the collision diameter, given in ˚A, 
which is the arithmetic average of the two species ( Cussler, 2009 ): 
σ12 = 0 . 5 ( σ1 + σ2 ) (12) 
Values of σ1 and σ2 can be found in Cussler (2009 ). The val- 
ues of the dimensionless quantity /Omega1depend on an integration of 
the interaction between the two species which can be described 
by the Lennard–Jones 12-6 potential and is usually of order unity 
( Hirschfelder, 1964 ). 
2.2. Adaptive mesh reﬁnement 
Signiﬁcantly ﬁne spatial resolution is required in order to ac- 
count for strong ﬂow discontinuities (like shock waves) and tur- 
bulent mixing in under-expanded jets ( Vuorinen et al., 2013; 
Hamzehloo and Aleiferis, 2014b ). Depending on the properties of 
the issuing gas and also operating conditions the use of a min- 
imum grid size of at least D /20 is typically required, as widely 
practiced in the literature ( White and Milton, 2008; Dauptain et 
al., 2010; Velikorodny and Kudriakov, 2012; Vuorinen et al., 2013; 
Hamzehloo and Aleiferis, 2014b ). The common approach in mod- 
elling this type of ﬂow is to apply a ﬁxed reﬁnement area with 
a varying cell size downstream of the nozzle exit (that would 
cover all or part of the jet volume) ( Vuorinen et al., 2013, 2014 ; 
Hamzehloo and Aleiferis, 2014b ). For NPR values lower than about 
6, and also for gasses with low diffusivity, this approach has been 
shown to be able to resolve completely the jet volume with rea- 
sonable cell count for quantifying the jet tip penetration ( Vuorinen 
et al., 2013, 2014 ). However, for high NPR values and/or highly dif- 
fusive gases such as hydrogen, this method would require a sig- 
niﬁcant larger number of cells in order to resolve the entire jet 
volume accurately. A solution to this is to resolve with a ﬁne grid 
only a portion of the jet core, as also practiced previously by the 
current authors ( Hamzehloo and Aleiferis, 2014b, c ). This practice 
has been found to offer the ability to resolve shock structures em- 
bedded in the jet core and also resolve a valuable portion of the 
mixing process in hydrogen and methane jets with NPR up to 10 
within a reasonably practical cell count ( ∼13.5 M cells). However, 
parts of the initial transient vortex rings of the under-expanded

<!-- PDF_PAGE: 4 -->

714 A. Hamzehloo, P.G. Aleiferis / International Journal of Heat and Fluid Flow 61 (2016) 71 1–729 
Fig. 1. Adaptive mesh reﬁnement used for modelling initial transient development of a highly under-expanded nitrogen jet with NPR = 8.5. 
jets studied were located outside the reﬁnement zone and conse- 
quently were not resolved in detail. Also, it was noticed that for 
NPR > 20, a much larger reﬁnement area was required, especially 
in the radial direction, in order to model accurately the Mach disk 
dimensions, core shock cells and turbulent mixing in the vicinity 
of the jet boundaries within a useful penetration length of the jet 
( ∼30 D ) ( Hamzehloo and Aleiferis, 2014b , c ). 
In order to address the aforementioned issues of spatial reso- 
lution and to achieve a more accurate solution of under-expanded 
jets within still practical CPU times, a fully automatic AMR tech- 
nique was developed by the user coding capability of STAR-CC + 
based on Java programming. The AMR method was developed and 
tested on Cartesian grids but it can also be used for other types of 
cell types. The STAR-CCM + version 9.02.007 used for the present 
study did not include a default AMR facility and the entire AMR 
procedure was developed purely by the current authors. The rest 
of this subsection is devoted to describing the implementation of 
the AMR technique. 
Initially a simulation with AMR starts on a relatively coarse grid 
with only limited initial reﬁnement zones created upfront. A re- 
ﬁning parameter is then deﬁned on the basis of a ﬂow variable 
such as fuel mole fraction, density gradient, etc. The AMR process 
is triggered for a certain time interval depending on the growth 
rate of the ﬂow. For the present study, AMR was based on the jet’s 
scalar concentration ( ρc) or mole fraction of fuel. The use of den- 
sity gradient was avoided because this would result in signiﬁcantly 
larger number of cells due to the propagation of spherical pressure 
waves ahead of the jet volume. Additionally, the use of the density 
gradient alone may result in the formation of fairly coarse spatial 
resolution within the jet volume where the density gradient is not 
large enough to satisfy the predetermined reﬁning threshold. 
When the AMR is triggered with the mole fraction as reﬁning 
parameter, all the cells with mole fraction equal or larger than the 
threshold are automatically detected. Then the computational grid 
is regenerated (by means of the trimmer facility of STAR-CCM + ) 
using a table that contains the coordinates of those cells detected 
for reﬁnement. The ﬂow is automatically interpolated to the new 
cells using a distance-weighted, least-square interpolation (the so- 
lution data is mapped using a stencil of cells and faces on the orig- 
inal mesh). With this approach, the vertices/coordinates of the cells 
that are not reﬁned (either because they were ﬁne enough or were 
outside of the volume of interest) are kept intact. Transition from 
the ﬁnest to the coarsest grid resolution is designed through a 5- 
stage grid coarsening. This, in addition to a suitable AMR trigger 
timing, can ensure all the jet volume and some adjacent cell layers 
(see Fig. 1 ) are being solved constantly within the ﬁnest uniform 
spatial resolution, typically considered to be D /50 for the jets stud- 
ied in the current study. Therefore, some typical issues of AMR-LES 
with respect to treating the SGS kinetic energy by introducing a 
proper level of turbulent ﬂuctuation to a newly reﬁned cell and 
maintaining the conservation of kinetic energy through coarse-ﬁne 
cell interfaces ( Mitran, 20 01; Pope, 20 04; Pantano et al., 2007; An- 
tepara et al., 2015 ) were avoided within the areas of interest, i.e. 
the jet and its adjoining volumes. 
Fig. 1 shows the performance of the AMR technique in mod- 
elling the initial stages of formation of an under-expanded nitrogen 
jet with NPR = 8.5 (issued into a nitrogen-ﬁlled ambient). This test 
case will be discussed later in this paper and the focus here is only 
on the AMR procedure. The reﬁnement parameter was the scalar 
concentration ( ρc) with an AMR trigger threshold of ρc = 0.01. As 
shown at t = 13.5 t 0 in Fig. 1 , the computational domain included 
a ﬁxed initial reﬁnement zone covering a distance of 0.8 D down- 
stream of the nozzle exit. This was applied in order to capture 
smoothly the initial pressure waves emitted from the nozzle exit. 
It can be seen that by using a suitable AMR interval (here this was 
set to 2 μs) and a ﬁve level grid reﬁnement, the entire jet volume 
was solved continuously with a D /50 spatial resolution. This means 
that during each reﬁnement interval, cells covering the jet volume 
remained intact while their surrounding cells were gradually re- 
ﬁned. Comparison between t = 22.5 t 0 and t = 24.0 t 0 in Fig. 1 shows

<!-- PDF_PAGE: 5 -->

A. Hamzehloo, P.G. Aleiferis / International Journal of Heat and Fluid Flow 61 (2016) 71 1–729 715 
Fig. 2. Variations of the total number of cells and the jet tip penetration (normal- 
ized with the nozzle exit diameter) versus time after start of injection normalized 
by t 0 =2 μs. 
how AMR coarsened the spatial resolution of the grid with re- 
gards to the outline of the jet. It should be noted that in the cur- 
rent study the initial reﬁnement zone was kept untouched during 
the simulations and AMR procedure. However, if required, any ini- 
tial reﬁnement zone(s) can be easily adjusted to the shape of the 
emerging jet. 
The change in the total number of cells after the nozzle exit 
and a normalized jet tip penetration are both shown in Fig. 2 
against a normalized time after the start of injection for the jet 
of Fig. 1 . In this ﬁgure t ≤ 12 t 0 is associated with the development 
of an initial subsonic jet that was also noticed in previous stud- 
ies of under-expanded jets ( Vuorinen et al., 2013; Hamzehloo and 
Aleiferis, 2014b ). Within the time frame of 12 t 0 ≤ t ≤ 15 t 0 the noz- 
zle exit became gradually choked with Ma ≈ 1.0. At around t ≈ 15 t 0 
the jet penetrated for almost 0.8 D and reached the boundaries of 
the initial ﬁxed reﬁnement zone; the AMR was triggered after this 
time. At t ≈ 35 t 0 the increased rate of cell count overtook the pene- 
tration rate. This is because the cell count was affected by both tip 
penetration and volumetric growth of the jet. After the initial tran- 
sient stages, the rate of the jet’s penetration exhibited a decreasing 
trend while the total number of cells showed an almost constant 
increasing rate. According to Fig. 2 at almost 9 D jet tip penetra- 
tion ( D = 1.5 mm) a total number of ∼10 M cells were required in 
order to resolve the entire jet volume with D /50 spatial resolution. 
This indicates that although AMR could reduce the computational 
costs when modelling the initial development stages of under- 
expanded jets, it may result in signiﬁcantly large cell count if ap- 
plied throughout a much longer jet presentation process and/or for 
highly diffusive ‘bulky’ jets. Therefore, within the concept of under- 
expanded jets, AMR should be treated as a technique for achieving 
a more accurate representation of the ﬂow at speciﬁc stages rather 
than a tool aimed at reducing computational costs throughout the 
whole injection process. 
2.3. Simulation setup 
In Hamzehloo and Aleiferis (2014b, c ), the ability of the cur- 
rent LES framework to model under-expanded jets without the 
AMR technique was discussed in detail and validated both quanti- 
tatively and qualitatively against the experimental data of Ruggles 
and Ekoto (2012) and other computational results ( Vuorinen et al., 
2013; Yu et al., 2013 ). In the present paper the AMR-based com- 
putational framework was validated against those previous studies 
but also using additional data in the literature ( Edgington-Mitchell 
et al., 2014; Vuorinen et al., 2014 ). The remaining subsections de- 
scribe the validation cases that were used. 
Fig. 3. Domain conﬁguration and dimensions with nozzle proﬁle based on Ruggles 
and Ekoto (2012) . 
2.3.1. Validation cases 
Three test cases were prepared based on some recent experi- 
mental data of under-expanded jets available in the literature in 
order to validate the present AMR-LES framework. Some key de- 
tails of these test cases are provided in Table 1 . In all test cases, 
simulations of under-expanded jets were performed by considering 
systems consisted of a high pressure fuel tank and a low pressure 
air(nitrogen)-containing chamber that were linked by a converging 
nozzle. The conﬁguration of these test cases are shown in Figs. 3–5 . 
The length of the high pressure tank was long enough so that the 
ﬂow could be considered to be almost at rest at the inlet within 
the injection duration. This assumption which has also been used 
by other researchers ( Dauptain et al., 2010; Vourinen et al., 2013, 
2014 ) eliminated the need for applying any artiﬁcial perturbation 
for LES studies. It is worth mentioning that in under-expanded jets 
the dominant turbulent structures are created after the Mach re- 
ﬂection ( i.e. the ﬁrst shock cell) and the turbulence level at the 
nozzle exit do not play a signiﬁcant role in main turbulent struc- 
tures of the jet ( Edgington-Mitchell et al., 2014; André et al., 2014 ). 
This is discussed further in the current paper (see Fig. 13 ). In val- 
idation cases 1 and 3 ( Figs. 3 and 5 ) A stagnation pressure inlet 
condition was applied at the top boundary of the high-pressure 
tank in order to maintain the injection pressure, while the side 
and the bottom boundaries of the low pressure chamber were set 
to pressure outlet. However, in test case 2 ( Fig. 4 ) the conﬁguration 
is entirely wall-bounded similarly to the conﬁguration reported in 
the literature ( Vourinen et al., 2013, 2014 ). Following practices in 
the literature ( Dauptain et al., 2010; Vuorinen et al., 2013, 2014 ), 
the wall of the converging nozzle and the high pressure reservoir 
were set to adiabatic slip in order to avoid formation of any arti- 
ﬁcial boundary layer. Computational grids consisting of cubic ele- 
ments were created by using the trimmer facility of STAR-CCM + . 
This produced cells with identical size in all dimensions and re- 
sulted in a grid without cell stretching which typically provides 
enhanced numerical accuracy and avoids singularity issues linked 
to polar grids. 
For the all simulations a ﬁxed reﬁnement area was imple- 
mented inside the computational domain. For the test case with 
conﬁguration shown in Fig. 3 the initial reﬁnement area was 
stretched just ∼2.5 D downstream of the nozzle exit. In total about

<!-- PDF_PAGE: 6 -->

716 A. Hamzehloo, P.G. Aleiferis / International Journal of Heat and Fluid Flow 61 (2016) 71 1–729 
Table 1 
Test cases of under-expanded jets investigated in this study. 
Case Experimental data Geometry Gas, 
ambient 
D [mm] NPR P ∞  [bar] T ∞  [K] T o [K] Diffusivity AMR 
threshold 
AMR interval 
[μs] 
Validation 1 Ruggles and Ekoto 
(2012) 
Fig. 3 H 2 , air 1 .5 10 0 .9837 296 295 .4 D i = 7.94 ×10 −5 m 2 /s X = 0.01 0 .1 
Validation 2 Vuorinen et al. 
(2013, 2014) 
Fig. 4 N 2 , N 2 1 .4 8 .5 1 .0 293 293 Sc = 0.7 ρc = 0.01 2 .0 
Validation 3 Edgington-Mitchell 
et al. (2014) 
Fig. 5 Air, air 15 4 .2 1 .0140 297 293 Sc = 0.7 ρc = 0.01 10 
Elevated P ∞  N/A Fig. 3 H 2 , air 1 .5 10 9 .837 296 295 .4 D i = 7.94 ×10 −6 m 2 /s X = 0.01 0 .1 
Elevated P ∞  , T ∞  N/A Fig. 3 H 2 , air 1 .5 10 9 .837 600 295 .4 D i = 2.29 ×10 −5 m 2 /s X = 0.01 0 .1 
Elevated P ∞  , T ∞  N/A Fig. 3 CH 4 , air 1 .5 10 9 .837 600 295 .4 D i = 6.1 ×10 −6 m 2 /s X = 0.01 0 .1 
Fig. 4. Left: Domain conﬁguration and dimensions; geometry based on Vourinen et al. (2013) . Right: Zoomed view of the AMR reﬁned area. 
3.5 M calls ﬁlled initially the computational domain. This was ∼4 
times smaller than when a ﬁxed grid without AMR was used to 
model a similar jet ( Hamzehloo and Aleiferis, 2014b ). The sim- 
ulation started from rest conditions where it was assumed that 
hydrogen (methane) occupied the entire high pressure reservoir 
and a tiny part of the converging nozzle volume up to ∼1.4 D up- 
stream the nozzle exit. Air occupied the low pressure ambient and 
the remaining of the in-nozzle volume. The nominal integral time 
scale of an under-expanded gaseous jet issued from a circular noz- 
zle can be deﬁned as t 0 = D /2U e ( Vuorinen et al., 2013 ). Assum- 
ing choked conditions at the nozzle exit ( Ma = 1), t 0 was calcu- 
lated to be ∼6.2 ×10 −7 s for the hydrogen jet. A time-step in the 
range of /2206t = 1 ×10 −9 –5  ×10 −9 was used with lower values at the 
early stages of the simulation for modelling the in-nozzle tran- 
sient ﬂow. Molecular diffusivity was considered according to the 
Chapman-Enskog theory with values tabulated in Table 1 . In the 
current study the dynamic viscosity was calculated using Suther- 
land’s law with Sutherland’s constant ( C s ), reference value ( μs ) and 
reference temperature ( T s ) given in Table 2. 
Table 2 
Sutherland’s constants for different gases. 
Gas C s [K] μs [Pa.s] T s [K] 
H 2 72 .0 8.76 ×10 −6 293 .9 
CH 4 197 .8 1.2 ×10 −5 273 .15 
N 2 111 .0 1.781 ×10 −5 300 .55 
Air 120 1.827 ×10 −5 291 .15 
For the test case shown in Fig. 5 the use of no-slip wall con- 
dition was inevitable due to the relatively large diameter of the 
nozzle. The initial grid had a conical reﬁnement area that occupied 
a region from 2 D upstream of the nozzle exit to 0.5 D downstream 
of the nozzle exit. The rest of the nozzle volume was ﬁlled with 
a resolution of D /25 which then stretched to a maximum cell size 
of 1.0 mm through a 5-level grid expansion. 25 prism layers with 
0.15 mm thickness and a stretching rate of 1.5 were applied in or- 
der to resolve the viscous boundary layer for the converging nozzle 
and the bottom wall of the high pressure tank. This guaranteed a

<!-- PDF_PAGE: 7 -->

A. Hamzehloo, P.G. Aleiferis / International Journal of Heat and Fluid Flow 61 (2016) 71 1–729 717 
Fig. 5. Left: Domain conﬁguration and dimensions; geometry based on Edgington-Mitchell et al. (2014) . Right: Zoomed view of the AMR reﬁned area with some important 
features of an under-expanded jet. 
y + lower than unity which is required for accurate LES work with 
no-slip walls. The nominal integral time step of the ﬂow was cal- 
culated to be t 0 ≈ 2.4 ×10 −5 s (U e = 310 m/s), therefore, a time step 
of /2206t = 1 ×10 −6 s was selected. 
2.3.2. Elevated ambient pressure and temperature cases 
The conﬁguration used for validation case 1 was also used 
to investigate the effect of elevating the ambient pressure and 
temperature on the sonic and mixing characteristics of under- 
expanded hydrogen jets with respect to application in hydrogen- 
fuelled IC engines ( Hamzehloo and Aleiferis, 2014a ). These cases 
have been included in Table 1 . The simulation with T ∞  =296 K 
and P ∞  =98.37 kPa represents an ‘early injection’ strategy occur- 
ring just after intake valve closure in the compression stroke 
of a naturally aspirated direct-injection hydrogen engine and is 
typical for homogeneous mixture formation. The simulation with 
T ∞  =600 K and P ∞  =983.7 kPa represents a ‘late injection’ strategy 
occurring close to ignition timing at the end of the compression 
stroke that is typical for stratiﬁed engine operation. Then a simula- 
tion with T ∞  =296 K and P ∞  =983.7 kPa was also conducted. This 
case was not of immediate reference to a typical in-cylinder op- 
erating condition but was used in order to decouple the effects 
of pressure and temperature. Nevertheless, it may be seen as a 
test case that could provide insights towards heavily boosted en- 
gines. Similarly to validation case 1, the nominal integral time scale 
of those simulations was ∼6.2 ×10 −7 s; however, a time step of 
/2206t = 1 ×10 −9 s was used throughout the simulations in order to ac- 
count for the existence of relatively higher incoming momentum. 
Furthermore, direct comparison was conducted between hydrogen 
and methane jets with NPR = 10 issued into air with P ∞  =983.7 kPa 
and T ∞  =600 K. Although the nominal integral time step for the 
methane jet was fairly larger than that of hydrogen jet (due to the 
considerably lower speed of sound in methane, ( Hamzehloo and 
Aleiferis, 2014b ), a similar time step ( /2206t = 1 ×10 −9 s) to that of the 
aforementioned hydrogen jet was also used for this methane jet. 
3. Results and discussion 
3.1. Model validation 
3.1.1. Validation case 1 
Fig. 6 compares instantaneous ﬁelds of log 10 (| ∇ρ|) for the hy- 
drogen jet under study with AMR and the hydrogen jet investi- 
gated in the study of Hamzehloo and Aleiferis (2014b ) with a ﬁxed 
reﬁnement zone. It has been observed in earlier studies ( Golub, 
1994 ) that the Mach disk of an under-expanded jet exhibits an 
initial ﬂuctuation around its ﬁnal semi-steady dimensions. Previ- 
ously in Hamzehloo and Aleiferis (2014b ) it was noticed that for 
the hydrogen jet of Fig. 6 without AMR the near-nozzle shock 
structure and Mach disk dimensions reached semi-steady condi- 
tions in t = 40 –50  μs. Fig. 6 shows that at t = 35 μs the Mach disk 
dimensions of the hydrogen jet with AMR were almost identical 
to those of jets modelled without AMR at t ≥ 40 μs. An overall 
good agreement was observed between the Mach disk dimensions, 
H disk =3.08 mm and W disk =1.34 mm, and the near-nozzle shock 
structure between the hydrogen jets of the two studies, in accor- 
dance with the experimental investigation of Ruggles and Ekoto 
(2012) . 
Direct comparison between the tip penetration of the hydrogen 
jets with and without AMR is illustrated in the left graph of Fig. 7 . 
It was found that until t ≈ 20 μs both jets exhibited almost iden- 
tical penetration length. However, after this time the jet modelled 
by means of AMR displayed around 8% lower tip penetration com- 
pared to the jet simulated with ﬁxed reﬁnement. Also, at t = 35 μs 
the latter jet showed around 3% higher centreline penetration in 
comparison to the former jet (see (a) and (b) snapshots of Fig. 6 ). 
The relatively smaller penetration of the jet with AMR is attributed 
to its better resolved jet tip vortices i.e. its initial transient vortex 
ring. The earlier investigation of Hamzehloo and Aleiferis (2014b ) 
revealed that for this hydrogen jet at around t = 20 μs (when pen- 
etration differences start to show in Fig. 7 ), tip vortices started

<!-- PDF_PAGE: 8 -->

718 A. Hamzehloo, P.G. Aleiferis / International Journal of Heat and Fluid Flow 61 (2016) 71 1–729 
Fig. 6. Near-nozzle shock structure in under-expanded hydrogen jets with NPR = 10 injected in to an ambient air with P ∞  ≈ 1 bar with AMR (a) in the present study and 
without AMR (b–d) in previous study ( Hamzehloo and Aleiferis, 2014b ). 
Fig. 7. Left: Normalized jet tip penetration with the nozzle diameter ( D = 1.5 mm) of hydrogen jets with NPR = 10 and P ∞  ≈ 1 bar modelled with and without AMR. Right: 
Scaled jet tip penetration of hydrogen and methane jets studied (with and without AMR) versus a normalized time. 
penetrating radially beyond the ﬁxed reﬁnement region and conse- 
quently were resolved with marginal quality. A better resolved vor- 
tex ring with AMR is more dominant and introduces fairly stronger 
radial expansion; hence by considering almost identical hydrogen 
mass ﬂow rate at the nozzle exit for both cases with and without 
AMR, a shorter axial penetration (both tip and centreline) is ex- 
pected for the jet modelled with AMR. Comparison between the 
snapshots (a) and (b) of Fig. 6 clearly shows the enhancement 
achieved in resolving tip vortices by means of AMR. 
As explained in Ouellette and Hill (20 0 0), Vuorinen et al. 
(2013) and Hamzehloo and Aleiferis, (2014b) , for under-expanded 
jets the jet tip penetration Z tip can be scaled with the ratio of 
the upstream stagnation density to the ambient density ρ0 / ρ∞  as 
Z tip /( ρ0 / ρ∞  ) 1/4 ∼ t / t 0 1/2 . The right graph of Fig. 7 shows that the 
penetration curves of hydrogen and methane AMR collapsed on top 
of each other comparably to the previous observations of Vuorinen 
et al. (2013) and Hamzehloo and Aleiferis (2014b ). The discrepancy 
of the penetration of the jet without AMR after t / t 0 1/2 > 6 in this 
ﬁgure originated from the aforementioned resolution inaccuracy of 
the jet tip vortices. 
3.1.2. Validation case 2 
Fig. 8 compares the average near-nozzle density ﬁeld of an 
under-expanded nitrogen jet with NPR = 8.5 modelled by LES in 
Vuorinen et al. (2014) and LES with AMR of the present study. 
The ﬁgure has been scaled in the same way to that presented in 
Vuorinen et al. (2014) . Moreover, Fig. 9 shows a direct comparison 
Fig. 8. Averaged near-nozzle density ﬁeld of an under-expanded nitrogen jet with 
NPR = 8.5. (a): LES of Vuorinen et al. (2014) . (b): LES of the present study with AMR. 
between the current work and the average concentration ﬁeld ( ρc) 
of the same nitrogen jet produced experimentally and computa- 
tionally in Vuorinen et al. (2013) ; snapshots (a)–(d). Snapshot (e) 
of Fig. 9 shows the average ﬁeld of log 10 (| ∇ρ|) with similar leg- 
end to those of Fig. 6 . The Mach disk dimensions were found to 
be H disk = 2.57 mm and W disk =0.97 mm and these are in agree- 
ment with values reported by Vuorinen et al. (2013, 2014) . Specif- 
ically, the current study predicted ∼1% and 3% smaller Mach disk 
dimensions compared to those reported in Vuorinen et al. (2013, 
2014) , respectively. This is attributed to the fact that, unlike the 
present study and Vuorinen et al. (2013) , a temperature depen- 
dent speciﬁc heat capacity at constant pressure ( C p ) was used in

<!-- PDF_PAGE: 9 -->

A. Hamzehloo, P.G. Aleiferis / International Journal of Heat and Fluid Flow 61 (2016) 71 1–729 719 
Fig. 9. (a)–(d): Comparison between average concentration ( ρc) of an under-expanded nitrogen jet with NPR = 8.5 produced (a): experimentally by Vuorinen et al. (2013) , 
(b): computationally by Vuorinen et al. (2013) and (c)–(d): computationally in the present study with different legends. (e): Averaged ﬁeld of log 10 (| ∇ρ|) produced by the 
present study. 
Fig. 10. Scaled jet tip penetration of a nitrogen jet with NPR = 8.5 versus a normal- 
ized time. Comparison between the present LES study with LES of Vuorinen et al. 
(2013) . 
Vuorinen et al. (2014) . The angle of the reﬂected shock at the triple 
point was found to be α≈ 28.5 °, which is comparable to observa- 
tions reported in Vuorinen et al. (2013) . 
Snapshots (c) and (d) of Fig. 9 show the average ρc ﬁeld plot- 
ted with different legend upper value for better visualisation. Di- 
rect comparison between the regions highlighted by dotted white 
ovals in snapshots (a) and (d) of Fig. 9 reveals close similarity with 
regards to the topology of the outer shear layer between the cur- 
rent LES study and the experimental visualisation of Vuorinen et 
al. (2013) . 
Similarly to Fig. 7, Fig. 10 compares the scaled penetration 
length of the nitrogen jet of the current study with that re- 
ported by Vuorinen et al. (2013) . In agreement with the literature 
( Ouellette and Hill, 20 0 0; Vuorinen et al., 2013; Hamzehloo and 
Aleiferis, 2014b ), it is clear that the scaled penetration curves col- 
lapsed on almost a single line. This conﬁrms that in addition to 
the sonic characteristics, the current computational framework was 
also able to reproduce accurately the penetration length. 
3.1.3. Validation case 3 
Fig. 11 is based on an under-expanded air jet with NPR = 4.2 
and compares predictions of the current LES study with experi- 
mental data reported by Edgington-Mitchell et al. (2014) . The cur- 
rent LES framework reproduced the height and width of the Mach 
disk ∼6% and ∼17% smaller compared to the measurements ob- 
tained from Schlieren visualisation. Initially this difference may be 
explained due to the necessary simpliﬁcations applied (see Fig. 5 ) 
when creating the computational model of the quite complex ex- 
perimental apparatus shown in Edgington-Mitchell et al. (2014) . As 
seen previously ( Donaldson and Snedeker, 1971; Vuorinen et al., 
2013 ), the dimensions of the Mach disk and particularly its width 
are a function of NPR. During the experiment, upstream pressure 
and consequently NPR might experience some level of oscillations 
which could affect the Mach disk dimensions noticeably. Another 
contributing factor can be the level of turbulence at the nozzle 
Fig. 11. Near nozzle shock structure and turbulent behaviour of the under- 
expanded air jet with NPR = 4.2 issued from a circular nozzle with D = 15 mm. 
(a): Instantaneous Schlieren image of d ρ/dX ( Edgington-Mitchell et al., 2014 ). (b, 
c): Averaged Schlieren images of d ρ/dZ and d ρ/dX, respectively (80 0 0 samples, 
Edgington-Mitchell et al., 2014 ). (d, e): Instantaneous contours of the magnitude of 
the density gradient (| ∇ρ|) with different legend colours by LES. (f): Averaged con- 
tours of log 10 (| ∇ρ|) by LES (200 samples). (g) Instantaneous contours of log 10 (| ∇ρ|) 
at t= 1.5 ms by LES. (For interpretation of the references to colour in this ﬁgure leg- 
end, the reader is referred to the web version of this article.) 
exit. In fact as also reported in Vuorinen et al. (2013) and Yu et 
al. (2013) , the level of turbulence at the nozzle exit in an experi- 
mental test case can be signiﬁcantly higher than that of its compu- 
tational model. It has been reported ( Golub, 1994 ) that Mach disk 
dimensions of under-expanded jets exhibit slight ﬂuctuations even 
after reaching a semi-steady condition. Higher turbulence level at 
the nozzle exit may intensify these ﬂuctuations and result in larger 
Mach disk dimensions experimentally in comparison to what pre- 
dicted numerically. Similarly to what was discussed for validation 
case 2, the last contributing factor to the difference between LES 
and experiment in Mach disk dimensions can be attributed to the 
lack of temperature dependency of C p in the simulations. Since 
the difference between the computational and experimental Mach 
disk dimensions in the current case is slightly higher than those 
discussed in previous test cases, the authors believe that the rea- 
son for this difference is a combination of the aforementioned fac- 
tors. The previous test cases used simpler experimental appara- 
tuses with almost 10 times smaller nozzle diameters than that of 
test case 3. Therefore, effects of NPR ﬂuctuations and nozzle exit 
turbulence may be less signiﬁcant in the ﬁrst two test cases. 
In general, as presented in snapshots (a)–(f) of Fig. 11 , the 
current LES study was able to reproduce the near nozzle shock

<!-- PDF_PAGE: 10 -->

720 A. Hamzehloo, P.G. Aleiferis / International Journal of Heat and Fluid Flow 61 (2016) 71 1–729 
Fig. 12. Contours of mean in-plane velocity components normalized by the nozzle exit velocity U e ≈ 310 m/s (the under-expanded air jet with NPR = 4.2). Top row: Experi- 
mental data of Edgington-Mitchell et al. (2014) averaged over 80 0 0 samples. Bottom row: The current LES representation averaged over 200 samples. The black line indicates 
an approximation of w/U e ≈ 1 in both experiments and LES. 
structures comparably to those observed in the experiments. The 
reﬂected shock angle with the nozzle centreline was predicted ∼3 °
larger than that of the experiments with also slightly narrower dis- 
tance between the slip lines (the length of the red arrows in snap- 
shots (a), (d) and (e) of Fig. 11 are identical). This was attributed 
to the smaller Mach disk width of the numerical prediction. Simi- 
larly to the Schlieren images, the current LES study predicted the 
expansion and shrinkage of the width of the subsonic core ( i.e. dis- 
tance between the slip lines) just after the Mach reﬂection (dis- 
cussed comprehensively in Edgington-Mitchell et al., 2014 ). A com- 
bination of the shock structures and turbulent behaviours of the 
under-expanded air jet can be seen in snapshot (g) of Fig. 11 which 
is based on instantaneous contours of log 10 (| ∇ρ|) at t = 1.5 ms. 
The general bulk shape of the jet with its turbulent behaviour 
was captured computationally in agreement with earlier observa- 
tions of this kind of jet ( Donaldson and Snedeker, 1971; Dauptain 
et al., 2010; Vuorinen et al., 2013, 2014 ). After the Mach reﬂec- 
tion, several shock cells formed and after a certain distance from 
the nozzle exit viscous forces became dominant and consequently 
the shock cells disappeared (mixing of inner and outer shear 
layers started) and the jet became highly turbulent and exhib- 
ited intense mixing with the ambient medium, particularly at its 
boundary. 
A direct comparison between contours of mean in-plane ve- 
locity components (up to Z = 4 D downstream of the nozzle exit) 
produced by the current LES and planar PIV measurements of 
Edgington-Mitchell et al. (2014 ) is presented in Fig. 12 . The averag- 
ing of experimental data was conducted over 80 0 0 samples while 
for LES the averaging was conducted over 200 samples. This was 
due to the fact that by the time the near-nozzle ﬂow reached a 
semi-steady condition in the LES simulation, AMR had produced 
∼21 M cells and further running of the simulation was not really 
feasible within reasonable CPU timescales. In Fig. 12 the black line 
indicates an approximation of w/U e ≈ 1 in both experimental and 
computational visualisations (U e is the velocity at the nozzle exit). 
Very good agreement was observed with the experimental data in 
some classical characteristics of under-expanded jets such as initial 
formation of the outer shear layer at the nozzle exit (can be clearly 
seen in the w/U e snapshots of Fig. 12 ), Mach reﬂection, oblique 
shocks at the triple point and inner shear layer. Slight differences 
are attributed to the noticeably different number of samples used 
to evaluate the average values for each case. 
Centreline proﬁles of ﬁrst- and second-order statistics of the ve- 
locity are plotted in Fig. 13 for both LES and PIV. With respect to 
the mean axial velocity, the LES-derived curve follows relatively 
closely the trend of the experimental curve. However, compared 
to measurements, the maxima and minima of the LES curve are 
∼2% higher and ∼85% lower, respectively (w/U e =1.89, 0.037 for 
LES compared to w/U e =1.85, 0.28 for PIV). Extremely low values 
of velocity just after the Mach disk of under-expanded jets have 
also been reported by other computational studies in the litera- 
ture ( Velikorodny and Kudriakov, 2012; Owston et al., 2009 ). This 
noticeable difference between experiments and simulations is at- 
tributed to the existence of a strong ﬂow discontinuity due to the 
Mach reﬂection. If very high spatial resolution is used, simulations 
may be able to resolve the ﬂow behaviour in the vicinity of the 
Mach disk more accurately. A similar behaviour between LES and 
PIV comparison has been reported by Dauptain et al. (2010) . The 
effect of the spatial resolution in the prediction of the Mach dis- 
continuity in under-expanded jets has been discussed in Owston 
et al. (2009) where it was shown that a relatively coarse grid may 
not be able to capture precisely the near-nozzle velocity proﬁle of 
under-expanded jets. 
After the Mach reﬂection at Z = 10 D downstream of the nozzle 
exit, LES predicted six peaks i.e. six shock cells, compared to ﬁve 
peaks quantiﬁed by PIV (see Fig. 13 ). This was due to the afore- 
said slight difference in the Mach disk height between computa- 
tions and measurements which produced a small phase lag be- 
tween the curves of velocity in Fig. 13 . This means that the sixth 
peak of the experimental data would probably be located after 
Z = 10 D and was not captured. As discussed by Pack (1950) , the 
spacing of the shock cells after the Mach reﬂection in an under- 
expanded jet should be almost identical. Fig. 13 shows that, despite 
the slight frequency difference, the spacing between the velocity 
peaks (shock cell spacing) in both computational and experimental 
curves remained constant and was ∼22 mm for both curves. This 
was comparable to classical observations ( Donaldson and Snedeker, 
1971 ) and theoretical studies ( Pack, 1950 ) of this kind of ﬂow. It 
is worth mentioning that similarly to the experimental observa- 
tions of Edgington-Mitchell et al. (2014) the current LES did not

<!-- PDF_PAGE: 11 -->

A. Hamzehloo, P.G. Aleiferis / International Journal of Heat and Fluid Flow 61 (2016) 71 1–729 721 
Fig. 13. Axial proﬁles of mean and ﬂuctuating velocity quantities taken along nozzle centreline in the under-expanded air jet with NPR = 4.2. Comparison between the 
current LES study and PIV data reported in Edgington-Mitchell et al. (2014) . 
reproduce a second normal shock after the Mach reﬂection. With 
respect to velocity ﬂuctuations, it is clear from Fig. 13 that both 
the axial and transverse ﬂuctuations experienced modulation by 
the embedded shock structures. At the jet core, similarly to ex- 
perimental observations, LES predicted more modulation for the 
transverse ﬂuctuation than the axial one, mainly due to the rela- 
tively lower effects of the shear layers within this region. Although 
the bulk trend of the ﬂuctuation graphs of Fig. 13 is similar be- 
tween computations and experiments, some differences are ob- 
served. For Z/ D < 1.2, i.e. upstream of the Mach disk, LES predicted 
noticeably lower axial and transverse velocity ﬂuctuations (w ′ /U e 
ranging from 2 ×10 −4 to 10 −3 and u ′ /U e ranging from 8 ×10 −6 to 
1.2 ×10 −4 ) compared to those of PIV (w ′ /U e ranging from 1.2 ×10 −2 
to 3 ×10 −2 and u ′ /U e ranging from 7.5 ×10 −3 to 9 ×10 −3 ). This is 
attributed to the fact that no artiﬁcial perturbation was applied 
in the current LES study. The turbulent characteristics of under- 
expanded jets are greatly ampliﬁed by the Mach reﬂection and re- 
silient shear layers downstream of the Mach disk ( Inman et al., 
2008 ). Different averaging samples between LES and experiments 
(200 and 8000, respectively) may also contribute to the discrep- 
ancy between the velocity ﬂuctuation graphs of Fig. 13 partic- 
ularly for Z > 4 D downstream of the nozzle exit where the jet 
structure exhibited strong turbulent behaviour (see snapshot (g) of 
Fig. 11 ). However, as seen in Fig. 13 and particularly for w ′ /U e , good 
agreement was observed between LES and PIV for 1.2 < Z/D < 4.5. 
Within this range the u ′ /U e graph of Fig. 13 shows larger differ- 
ence in magnitude between LES and PIV when compared to the 
w ′ /U e graph, but still a similar overall trend exists. This can be due 
to the aforementioned difference between the turbulence intensity 
upstream of the Mach disk. Such intensity difference can have a 
greater effect on the transverse velocity ﬂuctuation than on the ax- 
ial mainly due to the stronger effect of the ﬂow discontinuity and 
shear layers on the axial velocity proﬁle. 
3.2. Penetration and volumetric growth 
3.2.1. Various ambient thermodynamic conditions 
The jet tip penetration, volumetric growth and number of cells 
created by AMR within the low pressure ambient are plotted in 
Fig. 14 versus time for hydrogen. It was found that hydrogen jets 
with NPR = 10 and T ∞  = 296 K but with different ambient pressures 
of P ∞  ≈ 1bar and 10bar followed almost identical trends. This may 
be due to the fact that the sonic characteristics of under-expanded 
jets are mainly a function of NPR. Therefore, with identical NPR a 
fairly similar velocity distribution forms downstream of the nozzle 
exit which results in comparable radial and axial penetrations. 
Increasing the ambient temperature at P ∞  =10 bar from 
T ∞  =296 K to T ∞  =600 K resulted in increased jet tip penetra- 
tion and volumetric growth, and consequently increased AMR cell 
count. Speciﬁcally, at t = 30 μs the hydrogen jet with T ∞  =600 K 
exhibited ∼21% longer penetration and ∼30% larger volumetric 
growth in comparison to the jet with identical NPR and P ∞  issued 
into ambient air with T ∞  =296 K. This was attributed to the lower 
density of the ambient at the higher temperature ( ρ∞  ≈ 5.7 and 
11.6 kg/m 3 for 296 and 600 K, respectively). Similar to the present 
LES study, the experimental visualisations of Petersen and Ghandhi, 
(2006) and Rogers et al. (2015) also reported a reduction in the ax- 
ial penetration of under-expanded hydrogen jets as a result of in- 
creased ambient density. About 9% difference in the effect of ambi- 
ent temperature on the axial and radial penetration was attributed 
to the diffusivity difference under different ambient temperatures. 
At P ∞  =10 bar, the diffusivity of hydrogen in an air at T ∞  =600 K is 
∼188% higher than that at T ∞  =296 K. Due to the presence of quite 
high axial velocity magnitude (in excess of 20 0 0 m/s) the effect of 
diffusivity may not be as inﬂuential on the axial jet penetration as 
is on the radial penetration and consequently on the jet’s volumet- 
ric growth. 
Due to the relatively higher penetration and volumetric growth 
of the hydrogen jet with T ∞  =600 K, the AMR produced at t=30 μs 
∼35% more cells ( ∼21 M) for this jet compared to the hydrogen 
jet with T ∞  =296 K ( ∼15.5 M cells). Direct comparison between the 
cell count graphs of Fig. 14 and Fig. 2 shows that at ∼6 D pene- 
tration length, a hydrogen jet with NPR = 10 requires ∼180% more 
cells compared to a nitrogen jet with NPR = 8.5 ( ∼20 and 6.7 M 
cells, respectively). Despite the small difference in their NPR val- 
ues, the signiﬁcant cell count difference between these jets origi- 
nates from the existence of stronger radial expansion of the tran- 
sient vortex ring and higher diffusivity of hydrogen (characteristics 
of transient vortex rings in under-expanded hydrogen jets are dis- 
cussed later in the current paper). 
3.2.2. Hydrogen vs. methane 
Fig. 14 also illustrates a direct comparison between the under- 
expanded jets of hydrogen and methane at NPR = 10 for P ∞  = 10 bar 
and T ∞  =600 K. Hydrogen exhibited signiﬁcantly higher penetra- 
tion and volumetric growth compared to methane. Speciﬁcally, 
at t = 30 μs, hydrogen showed ∼16% and ∼117% higher penetra- 
tion and volumetric growth, respectively compared to methane jet 
(Z tip ≈ 10.62 mm and V jet ≈ 283 mm 3 ). This is in agreement with 
previous experimental observations ( Petersen and Ghandhi, 2006 ) 
and also with the earlier study of Hamzehloo and Aleiferis (2014b ) 
on under-expanded hydrogen and methane jets with NPR = 8.5, 
P ∞  =1 bar and T ∞  =296 K. From Fig. 14 it is also observed that for

<!-- PDF_PAGE: 12 -->

722 A. Hamzehloo, P.G. Aleiferis / International Journal of Heat and Fluid Flow 61 (2016) 71 1–729 
Fig. 14. Variations of normalized tip penetrations, normalized volume and cell 
count of under-expanded hydrogen and methane jets investigated in the current 
study. 
t ≥ 25 μs, the difference between the penetration rate of hydrogen 
and methane remained almost constant, ∼0.35 mm/μs, while the 
rate of volumetric jet growth of hydrogen exhibited a fairly faster 
increase than that of methane ( ∼32 mm 3 /μs and 17 mm 3 /μs for 
hydrogen and methane jets, respectively). This resulted in AMR’s 
creation of more cells for the hydrogen jet; at t = 30 μs ∼23.5 M 
cells were required to resolve the hydrogen jet entirely with D /50 
spatial resolution while with the same criteria only ∼13 M cells 
were required for the methane jet. The difference in the volumet- 
ric growth rate is attributed to the signiﬁcant differences in nozzle 
exit velocity and consequently radial expansion of the jet, as well 
as to the diffusivity differences between hydrogen and methane. 
In general, in comparison to all hydrogen jets studied (with and 
without elevated ambient), methane showed noticeably lower vol- 
umetric growth. However, as shown in Fig. 14 , after t ≈ 24 μs, the 
methane jet showed longer penetration compared to the hydro- 
gen jets with identical NPR when injected into ambient air at 
T ∞  =296 K. This is attributed purely to the difference in ambient 
density and associated reduction in the resistance of the ambient 
medium as discussed earlier. 
3.2.3. Volumetric growth scaling 
Using LES and scaling for the jet tip penetration (as sug- 
gested by Ouellette and Hill, 20 0 0 , and shown earlier in Figs. 
7 and 10 ), Vuorinen et al. (2013) proposed a speciﬁc scaling 
parameter for the volumetric growth of under-expanded jets as 
V jet /( ρ0 / ρ∞  ) 3/4 ∼( t / t 0 ) 3/2 . The volumetric growth of the under- 
expanded jets examined in the current paper is plotted in the left 
graph of Fig. 15 using the aforementioned volumetric scaling cor- 
relation. It is seen that scaling created curves with almost linear 
growth rate. However, only the curves associated with hydrogen 
jets at T ∞  =296 K collapsed on a single line. It was found that by 
introducing a multiplication coeﬃcient β into the scaling param- 
eter of Vuorinen et al. (2013) , with values of 1.35 and 3 for hy- 
drogen and methane, respectively, the curves of elevated ambient 
pressure and temperature collapsed onto the line of hydrogen jets 
with T ∞  =296 K, as shown in the right graph of Fig. 15 (the value 
of β at the reference case of T ∞  =296 K is obviously equal to unity 
for both P ∞  =1 bar and 10 bar). The under-expanded nitrogen jets 
studied by Vuorinen et al. (2013) had similar molecular diffusivity, 
ratio of speciﬁc heats ( i.e. sonic characteristics) and also resistance 
of the ambient medium ( i.e. ambient density) (since they were in- 
jected into a cold nitrogen ambient with molecular diffusivity val- 
ues calculated based on a ﬁxed Schmidt number of 0.7). The under- 
expanded hydrogen and methane jets studied here had noticeably 
different values for the aforementioned quantities, therefore, their 
volumetric growth could not be scaled simply by the correlation 
suggested by Vuorinen et al. (2013) . The β coeﬃcient proposed 
here accounts for the possible effects due to differences in the dif- 
fusivity, sonic characteristics, and ambient density and as shown 
in Fig. 15 it is necessary to use it when comparing jets with quite 
dissimilar values of the mentioned quantities. 
3.3. Transient vortex ring 
3.3.1. Hydrogen vs. methane 
The initial stages of transient penetration of both hydrogen and 
methane injected into ambient with T ∞  =600 K for a period of the 
ﬁrst 30 μs after the start of injection are presented in Fig. 16 by 
means of mole fraction contours on a vertical symmetry plane of 
the nozzle. Due to the higher speed of sound in hydrogen com- 
pared to that of methane, the former jet entered the domain ∼3 μs 
earlier. Therefore, methane’s contours are included from t = 6 μs in 
Fig. 16. 
A concave tip proﬁle can be seen for both hydrogen and 
methane jets just after their initial penetration stage, t = 4 μs and 
6 μs, respectively. A similar concave behaviour has been noticed 
in previous experimental and computational studies that exam- 
ined moderately under-expanded helium jets ( Thangadurai and 
Das, 2010; Zhang, 2014 ). This was attributed to the existence of an 
embedded shock and the difference in velocities of the ﬂow pro- 
cessed by this shock at different radii from the nozzle symmetry

<!-- PDF_PAGE: 13 -->

A. Hamzehloo, P.G. Aleiferis / International Journal of Heat and Fluid Flow 61 (2016) 71 1–729 723 
Fig. 15. Normalized scaling parameter of the volumetric growth of under-expanded jets without (left) and with (right) the effect of parameter β. 
axis. This shock has a slightly convex proﬁle which around the noz- 
zle centreline performs almost similarly to a normal shock. While 
moving radially, the angle of inclination of the ﬂow decreases and 
it can be treated as an inclined, i.e. not normal, shock ( Hornung, 
1986 ). This means that by moving away from the nozzle’s symme- 
try axis, the ﬂow velocity after the embedded shock increased and 
formed a shear layer which consequently created the concave pro- 
ﬁle at the tip of the jet. The ﬂow at small radii after this embedded 
shock accelerated very quickly, reaching supersonic conditions and 
forming a fully convex tip proﬁle in both hydrogen and methane 
jets after t ≈ 6 and 8 μs, respectively. 
Initial complete rolling-up of the tip occurs at t = 5 μs for hy- 
drogen, i.e. around t = 3 μs faster than that of the methane jet. For 
the hydrogen jet, complete tip vortex was formed by t = 8 μs and 
merged rapidly with strong shear layers (inner and outer) of the 
jet, becoming imperceptible at t = 12 –1 5 μs. By formation of the 
shock cells after the Mach reﬂection and formation of counter- 
rotating vortices close to the jet tip around its centreline (the latter 
due to Biot–Savart induction and vortex sheet roll-up, Thangadurai 
and Das, 2010; Zhang, 2014 ) seen clearly for both hydrogen and 
methane in the t = 15 μs snapshots of Fig. 16 , the secondary vortex 
ring was formed at t ≈ 25 μs. This then diffused to the surround- 
ing ambient (and/or merged with the main jet stream) after vortex 
disconnection (or ‘pinch-off’) ( Gharib et al., 1998 ) from the trailing 
jet ( t ≥ 30 μs). In contrast, for methane, the initial vortex ring ex- 
isted up to t = 25 –28  μs and then merged with the shear layers by 
a broadly similar mechanism to that described for hydrogen and 
formed a secondary set of vortices, as shown in the t = 30 μs snap- 
shot of Fig. 16 . Signiﬁcant differences between the two gases in 
Fig. 16 , especially in terms of penetration, volumetric growth and 
shear layer development, were attributed to differences in their 
sonic characteristics and also the higher diffusivity of hydrogen; 
more details can be found in Hamzehloo and Aleiferis (2014b ) as 
the main jet features were similar at low ambient temperature as 
well. 
Further investigation on the basis of velocity vectors can shed 
more light onto the complex formation mechanism of the jets’ vor- 
tex ring and annular shear layers. Snapshots of velocity vectors, hy- 
drogen mass fraction and density gradients were overlapped using 
various degrees of opacity to provide a more complete image of 
the interactions involved. These are presented in Figs. 17 and 18 . 
The initial stages of the tip roll-up of the hydrogen jet are pre- 
sented in Fig. 17 . At t = 4 μs it is evident that the ﬂow separated 
from the edge of the embedded shock, satisfying the Kutta condi- 
tion ( Thangadurai and Das, 2010 ). The directionality of the arrows 
at t = 6 μs demonstrates the tendency of the vortex to expand radi- 
ally. This contributes to the outward expansion of the jet and for- 
mation of the outer shear layer before the location of the Mach 
disk (as also observed in Hamzehloo and Aleiferis, 2014b ). Sudden 
expansion and Prandtl–Meyer expansion fans at the nozzle lip also 
contributed to the high radial velocity and associated behaviour of 
the jet. At t = 6 μs, the tip vortices had signiﬁcant contribution to 
the mechanism of entrainment of ambient air into the main stream 
of the fuel jet. Based on the ﬂow behaviour seen in Fig. 17 it is 
now possible to explain the difference between the preliminary 
vortex rings of methane’s and hydrogen’s jets observed in Fig. 16 . 
Due to the signiﬁcantly lower velocity of the under-expanded jet of 
methane than that hydrogen, relatively weaker separation occurred 
at the edge of the embedded shock in the former jet. Therefore, the 
vortex ring of methane required more time for a complete recircu- 
lation which then resulted in axial translation of the vortex core to 
signiﬁcantly larger distances downstream of the nozzle exit com- 
pared to the maximum axial movement of the initial vortex core 
of the respective hydrogen jet. 
In order to provide further fundamental understanding of the 
formation mechanism of the secondary vortex ring in the hydrogen 
jet, the t = 15 μs snapshot of Fig. 16 was recreated in Fig. 18 using 
the overlapping features of Fig. 17 . A rather complex ﬂow, consist- 
ing of several counter-rotating vortices with different intensities, 
was observed. It was found that the supersonic ﬂow processed by 
the reﬂected shock at the triple point (within the slip region) was 
the main cause of the jet open-up and formation of the secondary 
vortex core. The complex conﬁguration of the embedded shocks, 
followed by the formation of the shock cells (after the Mach disk) 
and also the existence of strong shear layers are believed to be 
the key contributors to this ﬂow structure. The presence of many 
counter rotating vortices in Fig. 18 is believed to be due to Kelvin–
Helmholtz type of instabilities (due to the high levels of shear) 
which promote transition of the vortex ring from laminar to tur- 
bulent ( Thangadurai and Das, 2010 ). 
3.3.2. Three-dimensional structures 
The strongly three-dimensional vortical structures of under- 
expanded jets may not be fully distinguishable by visualisations in 
2D like those of Fig. 16 . Therefore, 3D visualisations of the tran- 
sient development of the vortex ring in the methane and hydrogen 
jets are presented in Figs. 19 and 20 . These are based on the iso- 
surface of methane’s or hydrogen’s mole fraction with a threshold 
value of X = 0.01. It is clear that the vortex ring ahead of the trailing 
jets exhibited a poloidal-toroidal structure. For the methane jet up

<!-- PDF_PAGE: 14 -->

724 A. Hamzehloo, P.G. Aleiferis / International Journal of Heat and Fluid Flow 61 (2016) 71 1–729 
Fig. 16. Transient development of under-expanded hydrogen and methane jets; for- 
mation and evolution of the vortex ring ( P ∞  =10 bar T ∞  =600 K). 
Fig. 17. Flow separation at the edge of the embedded shock structure, rolling-up 
of the jet tip and formation of the initial tip recirculation in the hydrogen jet with 
P ∞  =10 bar T ∞  =600 K. The ﬁgure was made of overlapping velocity vectors, con- 
tours of hydrogen mass fraction and contours of the magnitude of the density gra- 
dient. 
to t = 20 μs a smooth vortex ring existed which in the 2D snapshots 
of Fig. 16 was identiﬁed on the basis of the symmetrical shape 
of the jet. Fig. 19 shows that within the time frame of t = 20 –
25 μs the smooth vortex ring exhibited cellular structures through 
a gradual transient process. The formation of the transient vortex 
ring was the sign of the start of the fuel-ambient mixing process. 
For hydrogen the turbulent vortex ring formed signiﬁcantly ear- 
lier in comparison to methane, at t = 12 μs, and this was associated 
with the faster formation of the shear layers seen in Fig. 16.

<!-- PDF_PAGE: 15 -->

A. Hamzehloo, P.G. Aleiferis / International Journal of Heat and Fluid Flow 61 (2016) 71 1–729 725 
Fig. 18. Flow characteristics of the under-expanded hydrogen jet with P ∞  =10 bar and T ∞  = 600 K at t = 15 μs. This picture is made of overlapping snapshots of the same 
parameters used in Fig. 19.

<!-- PDF_PAGE: 16 -->

726 A. Hamzehloo, P.G. Aleiferis / International Journal of Heat and Fluid Flow 61 (2016) 71 1–729 
Fig. 19. Three-dimensional visualisation of the preliminary vortex ring in the 
under-expanded methane jet with P ∞  =10 bar T ∞  =600 K. 
The iso-surfaces of Fig. 19 clearly show stationary vortical struc- 
tures (streamwise and spanwise vortices Krothapalli et al., 1998 ) 
close to the nozzle exit. These vortical structures exhibited heli- 
cal motion around the circumference of the jet downstream of the 
Mach reﬂection and consequently were found to promote mixing at 
the jet boundary when studied later in their development process 
in Hamzehloo (2015) . The cellular structure of the vortex ring in 
the iso-surface snapshots of Fig. 19 for t = 29 μs demonstrated the 
existence of turbulent mixing between methane gas and ambient 
air. 
Fig. 20. Three-dimensional visualisation of the preliminary vortex ring in the 
under-expanded hydrogen jet with P ∞  =10 bar T ∞  =600 K. 
A vortex ring normally disconnects from its training jet, in a 
pinch-off process, when the vorticity in the shear layer of the trail- 
ing jet ceases to ﬂow into the vortex ring ( Gharib et al., 1998 ). 
The pinch-off process occurs for different reasons in different types 
of vortex rings and in the case of under-expanded jets it may be 
attributed to the high supersonic velocity of the fully developed 
shear layers. After formation of the supersonic slip region (and also 
shock cells), the velocity of the trailing jet becomes greater than 
that of the core of the vortex ring. At this point, pinch-off starts 
and the vortex ring reduces gradually in intensity, diffuses into the 
ambient gas and/or merges with the main stream of the gas jet. On 
the basis of Figs. 16 and 19 it can be concluded that the pinch-off
process started at t ≈ 30 μs for methane. However, for hydrogen, as 
highlighted earlier, the pinch-off process occurred at a later time 
in the jet’s development, and for its secondary vortex ring, hence 
a distinctly different behaviour occurred. 
It was also found that the secondary vortex ring of the hydro- 
gen jet was considerably stronger and wider than its initial prede- 
cessor. This can be attributed to the fact that the secondary ring 
was formed by the high velocity shear layers, as further elaborated 
on later in the paper. On the other hand, the secondary vortex 
ring of methane’s jet was formed due to the pinch-off of its long- 
lasting preliminary vortex ring, therefore, it was relatively weaker 
and may not contribute signiﬁcantly to the mixing process, or at 
least not to the same degree that it contributed for the hydrogen 
jet. These differences in the characteristics of the vortex rings be- 
tween hydrogen and methane contributed to the formation of a 
relatively bulkier jet with wider cone angle for hydrogen compared 
to methane at ﬁxed NPR, as can also be seen in the earlier simu- 
lated data of Hamzehloo and Aleiferis (2014b ) and also in the ex- 
perimental observations of Rogers et al. (2015) . 
Direct comparison between the vortex rings of methane’s and 
hydrogen’s jets ( Figs. 19 and 20 ) revealed that hydrogen’s vortex 
ring started exhibiting a cellular structure much earlier than the 
methane jet, around t = 15 μs. This shows that the fuel-air mix- 
ing started relatively earlier for hydrogen which at this stage is 
attributed to the higher diffusivity of hydrogen compared to that 
of methane. The cellular vortex ring structure of the hydrogen jet 
presented in Fig. 20 is in a very good agreement with the ex- 
perimental visualisations of under-expand hydrogen jets provided 
by Petersen and Ghandhi (2006) and Rogers et al. (2015) . These

<!-- PDF_PAGE: 17 -->

A. Hamzehloo, P.G. Aleiferis / International Journal of Heat and Fluid Flow 61 (2016) 71 1–729 727 
Fig. 21. Maximum tip and centreline penetrations of the under-expanded hydrogen 
and methane jets P ∞  =10 bar T ∞  =600 K. 
cellular structures of 3D visualisations are in fact the tiny counter- 
rotating vortices similar to those shown in Fig. 18. 
3.3.3. Parametric study 
Maximum jet tip and centreline penetrations of both hydrogen 
and methane jets injected into T ∞  =600 K are plotted in Fig. 21 . 
For both jets the deviation of the maximum tip penetration from 
that on the centreline was found to occur almost simultaneously 
with the start of the smooth to cellular transition of the vortex ring 
(see Fig. 16 ). For hydrogen, the deviation of these two penetration 
measures occurred earlier due to faster transition of the vortex ring 
to cellular status. Fig. 21 also shows that the difference between 
the maximum tip penetration and the centreline penetration of the 
hydrogen jet was greater than that quantiﬁed for methane. This 
may be attributed to both relatively higher turbulence and higher 
velocity magnitude within the hydrogen jet that resulted in larger 
levels of ﬂuctuation at the boundaries. 
Fig. 22 shows on the left the change in diameter of the pre- 
liminary vortex rings over time for both methane and hydrogen 
jets. This vortex ring diameter was measured as the distance be- 
tween the left and right vortex cores on a 2D vertical plane simi- 
lar to that of Fig. 16 . It is clear that the diameter increased rapidly 
during the early stages of its formation, i.e. up to t ≈ 10 and 15 μs 
for hydrogen and methane, respectively. This was attributed to the 
high radial velocity magnitude during the early stages of the ex- 
pansion process that consequently resulted in large lateral angles 
between the edge of the embedded shock and the nozzle symme- 
try axis. This angle reduced gradually as the jets penetrated into 
the domain (see Fig. 17 ). As shown in Fig. 22 , for the early stage 
of the vortex ring development, the trade-off between increasing 
circulation of the tip vortex over time and reducing the aforemen- 
tioned lateral angle of the shock edge created a growing trend of 
the vortex diameter with negative rate. The preliminary vortex ring 
of the hydrogen jet vanished before t ≈ 20 μs, while for methane 
it grew in diameter. Within t ≈ 15 –25  μs, the vortex ring diame- 
ter of the methane jet experienced a rapid increase with positive 
rate. The timing of 15 μs may be assumed as an inﬂection point in 
the methane data series of Fig. 22 . This was attributed to the for- 
mation of a strong Mach reﬂection and its consequent supersonic 
shear layers. The vortices of the shear layer fed the vortex ring and 
enhanced its circulation power ( Gharib et al., 1998 ). 
The trajectories of the preliminary vortex cores are plotted in 
Fig. 22 on the right for both hydrogen and methane. Up to a value 
of Z/ D ≈ 1.5 the trajectories of the two gases followed a similar 
trend. This showed the evolution of the initial laminar vortex rings. 
It should be noted that the relatively higher value of X/ D in the 
case of hydrogen was due to its higher radial expansion compared 
to methane. Past the location of Z/ D ≈ 1.5 and until Z/ D ≈ 2.2 the 
vortex ring of the hydrogen jet grew rapidly in both axial and ra- 
dial directions. However, for Z/ D ≈ 2.2 (close to the Mach reﬂection) 
the ring started merging with the shear layer. For methane’s jet, 
past Z/ D ≈ 1.5 and until Z/ D ≈ 4.0, the vortex ring expanded fairly 
smoothly in both Z and X directions with slightly higher gradi- 
ents towards the radial direction (X). Downstream of the location 
Z/ D ≈ 4.0 the vortex core of the methane jet exhibited a ﬂuctuating 
behaviour which was a sign of the start of the pinch-off process. 
4. Conclusions 
The present study used large eddy simulation in conjunc- 
tion with an adaptive mesh reﬁnement technique in order to in- 
vestigate the mixing characteristics and three-dimensionality of 
the vortical structures in transient under-expanded hydrogen and 
methane jets under various ambient thermodynamic conditions, 
including both low and elevated ambient pressures and temper- 
atures resembling in-cylinder states of gaseous-fuelled IC engines 
with early or late injection strategies (NPR = 10, P ∞  ≈ 1 and 10 bar, 
T ∞  =296 and 600 K). Initially, extensive validation studies of the 
computational framework was conducted on the basis of three dif- 
ferent experimental and computational test cases available in the 
literature. Additionally, direct comparison was performed between 
the mixing characteristics and vortical structures of hydrogen and 
methane jets issued into a ﬁxed volume air-ﬁlled ambient with 
P ∞  ≈ 10bar and T ∞  =600 K. The main conclusions of the present 
study can be summarised as follows: 
Fig. 22. Variations of the initial vortex ring diameter with time (left) and trajectories of the preliminary vortex core (right) in the under-expanded hydrogen and methane 
jets with P ∞  =10 bar and T ∞  =600 K.

<!-- PDF_PAGE: 18 -->

728 A. Hamzehloo, P.G. Aleiferis / International Journal of Heat and Fluid Flow 61 (2016) 71 1–729 
• At a constant ambient pressure and NPR, hydrogen jet injected 
into the hot ambient ( T ∞  =600 K) exhibited higher penetration 
length and volumetric growth ( ∼21% and ∼30% at t = 30 μs, re- 
spectively) compared to the jet issued into the cold ambient 
( T ∞  =296 K). This was mainly attributed to the lower density 
(and consequently lower resistance) of the hot ambient. The 
greater inﬂuence of ambient temperature rise on volumetric 
growth than on penetration can be attributed to the threefold 
increase in diffusivity that manifests itself more as an effect in 
the azimuthal direction since the ﬂow is dominated by super- 
sonic velocities axially. 
• Under identical NPR and elevated ambient temperature and 
pressure, hydrogen exhibited signiﬁcantly higher penetration 
length and volumetric growth compared to methane. Speciﬁ- 
cally, at t = 30 μs, the hydrogen jet exhibited ∼16% and ∼117% 
higher penetration and volumetric growth. 
• Methane injected into hot ambient showed noticeably lower 
volumetric growth in comparison to hydrogen jets issued into 
both cold and hot environments at the same ambient pres- 
sure and NPR. This was attributed to the relatively lower ra- 
dial expansion of the methane jet, mainly due to its fairly lower 
molecular diffusivity and weaker vortex ring. 
• A scaling coeﬃcient for the volumetric growth of under- 
expanded jets was proposed. The newly proposed parameter 
takes into account differences in diffusivity, ratio of speciﬁc 
heats and ambient density and consequently can be used for 
direct comparison between under-expanded jets of different 
gases or issued into different ambient thermodynamic states. 
• Flow separation at the edge of the embedded shock (to satisfy 
the Kutta condition) was shown to be the main cause of the 
initial tip rolling-up of the under-expanded jets and formation 
of the preliminary vortex rings. 
• The preliminary vortex ring of both hydrogen and methane jets 
exhibited a smooth structure which turned cellular through a 
complex transient process. The transition from smooth to cellu- 
lar vortex ring started ∼8 μs earlier in the hydrogen jet than in 
the methane jet due to the relatively faster formation of the 
shear layers in the former jet. High level of shear in under- 
expanded jets form counter-rotating vortices within the jet vol- 
ume and at the boundary of the jet with the ambient medium 
due to Kelvin–Helmholtz type instabilities which is believed to 
trigger the mixing and formation of the cellular structures. 
• For under-expanded jets and, in particular, ‘bulky’ jets such as 
those of hydrogen, AMR should be considered as a technique 
for achieving an accurate representation of the entire jet vol- 
ume, practically, only over speciﬁc time periods of the evolu- 
tion of the jet, rather than a tool aimed to reduce computa- 
tional costs in general over long jet penetration runs. This is 
because AMR can create extremely high number of cells within 
very short jet penetration lengths. Speciﬁcally, for a hydrogen 
jet with NPR = 10 issued into an engine-like ambient condition, 
AMR produced over 23.5 M cells for a penetration length of 
Z t ≈ 15 mm (in ∼30 μs of ﬂow time) when solving the ﬂow with 
a spatial resolution of D /50. 
Acknowledgements 
The authors acknowledge the use of University College London’s 
Legion High Performance Computing Facility (Legion@UCL), and as- 
sociated support services, in the completion of this work. 
References 
André, B. , Castelain, T. , Bailly, C. , 2014. Investigation of the mixing layer of underex- 
panded supersonic jets by particle image velocimetry. Int. J. Heat Fluid Flow 50, 
188–200 . 
Antepara, O. , Lehmkuhl, O. , Borrell, R. , Chiva, J. , Oliva, A. , 2015. Parallel adaptive 
mesh reﬁnement for large-eddy simulations of turbulent ﬂows. Comput. Fluids 
110, 48–61 . 
Cho, H.M. , He, B. , 2007. Spark ignition natural gas engines–a review. Energy Convers. 
Manage. 48, 608–618 . 
Cussler, EL , 2009. Diffusion: Mass Transfer in Fluid Systems, third ed. Cambridge 
University Press . 
Dauptain, A. , Cuenot, B. , Gicquel, Y.M. , 2010. Large-eddy simulation of a stable su- 
personic jet impinging on ﬂat plate. AIAA J. 48, 2325–2337 . 
Donaldson, C.DuP. , Snedeker, R.S. , 1971. A study of free jet impingement. Part 1. 
Mean properties of free and impinging jets. J. Fluid Mech. 45, 281–319 . 
Edgington-Mitchell, D. , Honnery, R.D. , Soria, J. , 2014. The underexpanded jet Mach 
disk and its associated shear layer. Phys. Fluids 26, 096101 . 
Ferziger, J.H. , Peric, M. , 2002. Computational Methods for Fluid Dynamics. Springer . 
Gharib, M. , Edmond, R. , Karim, S. , 1998. A universal time scale for vortex ring for- 
mation. J. Fluid Mech. 360, 121–140 . 
Golub, V.V. , 1994. Development of shock wave and vortex structures in unsteady 
jets. Shock Waves 3, 279–285 . 
Hamzehloo A. and Aleiferis, P.G., (2013) Computational study of hydrogen direct in- 
jection for internal combustion engines, SAE Technical Paper 2013-01-2524. 
Hamzehloo A. and Aleiferis, P.G., (2014a) Numerical modelling of mixture and com- 
bustion in DISI hydrogen engines with various injection strategies, SAE Technical 
Paper 2014-01-2577. 
Hamzehloo, A. , Aleiferis, P.G. , 2014b. Large eddy simulation of highly turbulent un- 
der expanded hydrogen and methane jets for gaseous-fuelled internal combus- 
tion engines. Int. J. Hydrogen Energy 39, 21275–21296 . 
Hamzehloo, A. , Aleiferis, P.G. , 2014c. Large eddy simulation of near-nozzle shock 
structure and mixing characteristics of hydrogen jets for direct-injection 
spark-ignition engines. 10th International Conference on Heat Transfer, Fluid 
Mechanics and Thermodynamics (HEFAT2014), Orlando, Florida, USA . 
Hamzehloo, A. , Aleiferis, P.G. , 2016. Gas dynamics and ﬂow characteristics of highly 
turbulent under-expanded hydrogen and methane jets under various nozzle 
pressure ratios and ambient pressures. Int. J. Hydrogen Energy 41, 6544–6566 . 
Hamzehloo, A. , 2015. Computational study of under-expanded jets, mixture forma- 
tion and combustion in direct-injection spark-ignition hydrogen engines. PhD 
Thesis, University College London (UCL), UK . 
Hirschfelder, J.O. , Curtiss, C.F. , Bird, R.B. , 1964. Molecular Theory of Gases and Liq- 
uids, second ed. John Wiley & Sons . 
Hornung, H. , 1986. Regular and mach reﬂection of shock waves. Annu. Rev. Fluid 
Mech. 18, 33–58 . 
Inman, J.A. , Danehy, P.M. , Nowak, R.J. , Alderfer, D.W. , 2008. Identiﬁcation of instabil- 
ity modes of transition in underexpanded jets. 38th Fluid Dynamics Conference 
and Exhibit. AIAA Paper 2008-4389 . 
Krothapalli, A. , Strykowski, P.J. , King, C.J. , 1998. Origin of streamwise vortices in su- 
personic jets. AIAA J. 36, 869–872 . 
Liou, M.S. , 2006. A sequel to AUSM, Part II: AUSM + -up for all speeds. J. Comput. 
Phys. 214, 137–170 . 
Mitran, S.M. , 2001. A Comparison of Adaptive Mesh Reﬁnement Approaches for 
Large Eddy Simulation. Washington University Seattle Department of Applied 
Mathematics, pp. 397–408 . 
Nicoud, F. , Ducros, F. , 1999. Subgrid-scale stress modelling based on the square of 
the velocity gradient tensor. Flow Turbulence Combust. 62, 183–200 . 
Ouellette, P. , Hill, P.G. , 20 0 0. Turbulent transient gas injections. J. Fluid Eng. 122 (4), 
743–753 . 
Owston, R. , Magi, V. , Abraham, J. , 2009. Fuel-air mixing characteristics of DI hydro- 
gen jets. SAE Int J Engines 1 (1), 693–712 . 
Pack, D.C. , 1950. A note on Prandtl’s formula for the wave-length of a supersonic 
gas jet. Q. J. Mech. Appl. Math. 3, 173–181 . 
Pantano, C. , Deiterding, R. , Hill, D.J. , Pullin, D.I. , 2007. A low numerical dissipa- 
tion patch-based adaptive mesh reﬁnement method for large-eddy simulation 
of compressible ﬂows. J. Comput. Phys. 221 (1), 63–87 . 
Petersen B.R. and Ghandhi J.B., (2006) Transient high-pressure hydrogen jet mea- 
surements, SAE Technical Paper 2006-01-0652 . 
Pope, S.B , 20 0 0. Turbulent Flows. Cambridge University Press. . 
Pope, S.B. , 2004. Ten questions concerning the large-eddy simulation of turbulent 
ﬂows. New J. Phys. 6 (35) . 
Prudhomme, S.M. , Haj-Hariri, H. , 1994. Investigation of supersonic underexpanded 
jets using adaptive unstructured ﬁnite elements. Finite Elem. Anal. Des. 17, 
21–40 . 
Rogers, T. , Petersen, P. , Koopmans, L. , Lappas, P. , Boretti, A. , 2015. Structural char- 
acteristics of hydrogen and compressed natural gas fuel jets. Int. J. Hydrogen 
Energy 40, 1584–1597 . 
Ruggles, A.J. , Ekoto, I.W. , 2012. Ignitability and mixing of underexpanded hydrogen 
jets. Int. J. Hydrogen Energy 37, 17549–17560 . 
Scarcelli, R. , Wallner, T. , Matthias, N. , Salazar, V. , et al. , 2011. Mixture formation in 
direct injection hydrogen engines: CFD and optical analysis of single- and mul- 
ti-hole nozzles. SAE Int. J. Engines 4 (2), 2361–2375 . 
Thangadurai, M. , Das, D. , 2010. Characteristics of counter-rotating vortex rings 
formed ahead of a compressible vortex ring. Exp. Fluids 49, 1247–1261 . 
Yu, J. , Vuorinen, V. , Kaario, O. , Sarjovaara, T. , Larmi, M. , 2013. Visualization and anal- 
ysis of the characteristics of transitional underexpanded jets. Int. J. Heat Fluid 
Flow 44, 140–154 . 
Velikorodny, A , Kudriakov, S , 2012. Numerical study of the near-ﬁeld of highly un- 
derexpanded turbulent gas jets. Int. J. Hydrogen Energy 37, 17390–17399 . 
Verhelst, S. , 2014. Recent progress in the use of hydrogen as a fuel for internal com- 
bustion engines. Int. J. Hydrogen Energy 39, 1071–1085 .

<!-- PDF_PAGE: 19 -->

A. Hamzehloo, P.G. Aleiferis / International Journal of Heat and Fluid Flow 61 (2016) 71 1–729 729 
Vuorinen, V. , Yu, J. , Tirunagari, S. , Kaario, O. , Larmi, M. , et al. , 2013. Large-eddy sim- 
ulation of highly underexpanded transient gas jets. Phys. Fluids 25, 016101 . 
Vuorinen, V. , Wehrfritz, A. , Duwig, C. , Boersma, B.J. , 2014. Large-eddy simulation on 
the effect of injection pressure and density on fuel jet mixing in gas engines. 
Fuel 130, 241–250 . 
Weiss, J.M. , Maruszewski, J.P. , Smith, W.A. , 1999. Implicit solution of preconditioned 
Navier–Stokes equations using algebraic multigrid. AIAA J. 37, 29–36 . 
Weiss, J.M. , Smith, W.A. , 1995. Preconditioning applied to variable and constant den- 
sity ﬂows. AIAA J. 33, 2050–2057 . 
White, T , Milton, B , 2008. Shock wave calibration of under expanded natural gas 
fuel jets. Shock Waves 18, 353–364 . 
Zhang, H. , Chen, Z. , Li, B , Jiang, X. , 2014. The secondary vortex rings of a supersonic 
underexpanded circular jet with low pressure ratio. Eur. J. Mech. B/Fluids 46, 
172–180 .
