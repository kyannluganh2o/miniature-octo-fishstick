<!-- PDF_PAGE: 1 -->

J. Fluid Mech. (2023), vol. 970, A8, doi:10.1017/jfm.2023.603
Gas-dynamic and mixing analysis of
under-expanded hydrogen jets: eﬀect of the cross
section shape
Giuseppe Anaclerio1,†, Tommaso Capurso2 and Marco Torresi1
1Department of Mechanics, Mathematics and Management, Polytechnic University of Bari,
Bari 70125, Italy
2Arts et Metiers Institute of Technology, LIFSE, CNAM, HESAM University, Paris 75013, France
(Received 11 December 2022; revised 9 July 2023; accepted 11 July 2023)
Green hydrogen is expected to have a key role in the transition towards a carbon-neutral
society, particularly in the transportation sector. Exploration of novel solutions for the
direct injection of hydrogen in internal combustion engines (ICEs) is a main topic for both
academia and industry. Here, the authors explore the gas-dynamic and mixing features
of hydrogen under-expanded jets exiting from non-axisymmetric cross-sections, with the
aim to provide guidelines for designing novel generations of ICE hydrogen injectors.
Triangular and star shapes have been compared
with elliptical and rectangular sections
with different aspect ratios. Differences in the shock wave systems are reported, and
explanations of the gas-dynamic mechanisms developed by each section are proposed.
Non-uniformity in the radial expansion of the jet boundary has been noticed in all of
the non-axisymmetric sections, leading to an
axis switching of the jet in some cases.
Differences in the radial mixing and axial jet penetration have been reported too, and a
robust correlation with the vorticity distribution along the jet boundary has been observed.
Key words: gas dynamics, shock waves, jets
1. Introduction
According to the International Energy Agency (IEA), renewable sources are expected to
play a key role in the current energy transition scenario, as they will become the main
source of electricity generation by 2025 (IEA 2020). Through the power-to-gas technology
(Gahleitner 2013), an ever-increasing amount of green hydrogen is expected to be available
in the near future. Green hydrogen will then have a central role in powering turbines,
fuel cells and internal combustion engines (ICEs) (Capurso et al. 2022). Regarding ICEs
fuelled with hydrogen, the mixture formation inside the cylinder is a crucial aspect.
† Email address for correspondence: giuseppe.anaclerio@poliba.it
© The Author(s), 2023. Published by Cambridge University Press 970 A8-1
https://doi.org/10.1017/jfm.2023.603
 Published online by Cambridge University Press

<!-- PDF_PAGE: 2 -->

G. Anaclerio, T. Capurso and M. Torresi
Both academia and industry are concerned in developing novel solutions for a quicker
homogenization of the charge. The direct injection (DI) of H 2 into the engine cylinder
leads to the onset of under-expanded jets whose features affect the mixing process in the
chamber (Wimmer et al. 2005; Y amane2018;Y i pet al. 2019).
Under-expanded jets have been thoroughly investigated in the literature, as reported in
the review by Franquet et al. (2015). Most of the research has focused on jets issuing
from convergent and convergent–divergent ducts with circular cross-sections (Adamson &
Nicholls 1959;L o v eet al. 1959; Crist, Glass & Sherman 1966; Velikorodny & Kudriakov
2012), at different nozzle pressure ratios (NPRs) (Boynton 1967; Abbett 1971). For NPRs
greater than 4, the onset of one or more strong normal shocks, the so-called Mach disks,
has been deeply
analysed. Position (Ashkenas & Sherman 1964; Lewis & Carlson 1964),
diameter (Addy 1981; Hatanaka & Saito 2012) and hysteretic behaviour (Gribben, Badcock
&R i c h a r d s2000;I r i eet al. 2003; Otobe et al. 2009) are among the main features that have
been examined. Conversely, the inﬂuence of the nozzle cross-section shape has received
less attention by the researchers. The available works are generally focused on elliptical
and rectangular sections.
Rajakuperan & Ramaswamy ( 1977) numerically solved the under-expanded structure
of elliptical jets, showing different shock patterns along the minor and major axis planes.
A quicker growth of the boundary along the minor axis of the section was noted, ultimately
leading downstream to the inversion of the axes ( axis switching phenomenon). Menon &
Skews (2005) analysed elliptical nozzles with aspect ratios (ARs) equal to 2 and 4 and
pressure ratios from 4 to 6. They observed different dimensions of the Mach disk along
the minor and major cross-section axes, which conﬁrmed the axis switching of the jet
observed by Rajakuperan. The axis switching was generically attributed to the different
curvature of the exit section in the minor and major axes. Menon & Skews ( 2010) also
observed that the barrel shock originates just after the nozzle exit section in the major
axis plane, and later along the minor axis plane. Such
a trend was further intensiﬁed for
the higher ARs. This behaviour was generically attributed to the variable curvature of the
elliptical section, but a clear mechanism for the quicker onset of the barrel shock along
the major axis plane was not provided. Chauhan, Kumar & Rathakrishnan ( 2016)
analysed
different elliptical jets with ARs of 2, 4 and 6 and pressure ratios from 2 to 5, comparing
results with a circular nozzle of the same area. They found superior levels of mixing for
all the tested NPRs. Interestingly, the inﬂuence of the AR on the mixing level seemed to
be dependent on the under-expansion intensity. At the lower NPRs, jets released from a
section of ARs 4 and 6 featured a superior level of mixing, whereas a more intense mixing
was promoted by the AR 2 nozzle at the higher NPRs. They attributed the higher mixing
of the elliptical sections to the generation of eddies of different size (smaller in the major
axis plane, greater in the minor)
that enhance the different scales of the turbulent mixing.
The same conclusions were drawn by Kumar & Rathakrishnan (2016) to explain the higher
mixing provided by an AR 2 over-expanded elliptical jet issuing at Mach 2.
As reported in the literature, rectangular jets provide an enhanced mixing as well, mainly
due to the higher level of turbulence generated by the shape (Makarov & Molkov 2013).
Teshima (1994) experimentally analysed rectangular under-expanded jets for different ARs
(2, 3, 4, 5, 62) and NPRs up to 500 using the laser induced ﬂuorescence technique.
Attention was paid to the transition from the regular to the Mach reﬂection of the
incident shock waves. He noted that the Mach transition did not depend solely on the
NPR but an inﬂuence of the inlet total pressure was observed. No detailed description of
the shock system was provided. Computational studies have been carried out by Pao &
Abdol-Hamid ( 1996), who reported a quicker growth of the boundary along the minor
970 A8-2
https://doi.org/10.1017/jfm.2023.603
 Published online by Cambridge University Press

<!-- PDF_PAGE: 3 -->

Gas-dynamic and mixing analysis of under-expanded hydrogen jets
axis of the exit section similarly to the elliptical cases, and the rounding of the corners
due to the turbulent mixing. For square sections, a 45 ◦ rotation of the jet boundary was
also noticed. Menon & Skews ( 2010)u s e dt h elaser vapour screen visualization technique
to get ‘slices’ of the ﬂow ﬁeld of under-expanded jets discharged by rectangular and
square nozzles for pressure ratios of 4 and 6. To the authors’ knowledge, he was the
ﬁrst to provide a detailed explanation of the near-ﬁeld structure of such jets. Differently
from circular nozzles, over-expanded conditions were recognized close to the corners of
the outlet section, which caused the onset of four re-compression
shock waves but did
not performed any consideration regarding the effects of the Mach disk features. Along
the radial direction, saddle shape proﬁles in the velocity and mass distributions were
also observed. To the authors’ knowledge, these proﬁles have been mostly investigated
in subsonic ﬂows (see Trentacoste & Sforza 1967;S f e i r1976). Krothapalli, Baganoff
& Karamcheti ( 1981) and Zaman ( 1996) attributed the saddle-shaped proﬁle to the
development of
three-dimensional (3-D) vortex rings shed from the nozzle lips, in synergy
with the streamwise vorticity of the secondary ﬂows developed inside the nozzle.
In this paper, authors have analysed the gas-dynamic and mixing features of hydrogen
under-expanded jets released by elliptical and rectangular jets. As much of the current
research focuses on H 2 DI in ICEs, the authors have considered a convergent duct with
the typical size of an automotive injector. Differently from most of the literature, we have
analysed jets under a NPR of 10, which corresponds to a highly under-expanded condition.
Indeed, H 2 DI feed pressure is expected to increase in the near future. Results observed
in the rectangular cases have prompted the authors to further analyse a triangular-shaped
section and a star one, which have been considered a way to deepen the gas-dynamic
ﬂow features developed by sections characterized by convex and concave angles. To
such a purpose, 3-D Reynolds-averaged Navier–Stokes (RANS) simulations have been
carried out, since the shock system development is mainly an inviscid phenomenon
that does not require more advanced approaches ( large-eddy simulations (LES), direct
numerical simulations). Regarding the mixing analysis, although the LES simulations
would provide closer results to the experiments (see Wang & McGuirk 2013) than RANS,
the latter are still reliable when one wants to perform analyses on a large number of cases.
Numerical Schlieren pictures provide insights of the shock waves development along the
characteristic planes of the jets. For the rectangular and elliptical sections, the dependence
of the Mach disk position on the AR is described, together with an explanation of the
observed shift toward the nozzle exit section. Such information can be useful in safety
applications: in the Mach disk notional nozzle approach – a tool for quick simulations
restricted to the
far-ﬁeld region – the knowledge of the Mach disk position is information
required a priori (Harstad & Bellan 2006; Winters & Evans 2007). Moreover, differences
in the nature of the shock system have been observed between the lower and higher AR
elliptical jets. The jet boundary development and the H 2 distributions are reported as well,
highlighting the dependence on the vorticity ﬁeld settled around the jet. The vorticity
distribution results are found to be well related to the intensity of the mixing and ultimately
drives the deformation of the jet boundary.
2. Case study
In ﬁgure 1 a sketch of the computational domain is shown. It is basically made up of
three zones: a cylindrical body (green) with a sufﬁciently large diameter to minimize
the total pressure losses, a convergent nozzle ending with a constant section duct and
a cylindrical discharging ambient with large dimensions to avoid conﬁnement effects.
970 A8-3
https://doi.org/10.1017/jfm.2023.603
 Published online by Cambridge University Press

<!-- PDF_PAGE: 4 -->

G. Anaclerio, T. Capurso and M. Torresi
p static
Discharging ambient
Nozzle detail
Constant
section
duct
p static
p static
p0
T0
Figure 1. Section of the numerical domain used in this work with the boundary conditions applied to the
domain boundaries. On the right is a detailed view of the nozzle exit.
L
S S
S
AA
B
AR = A/B
B
L
L
Figure 2. Sketch of the nozzle section shapes analysed in this work. Here L, S, A and B indicate the
dimensions of the different cross-sections; AR is the aspect ratio.
Such a conﬁguration creates a radial velocity ﬁeld in the convergent section, which tends to
zero in the constant section duct. Hence , ﬂow can be considered axial at the outlet section.
For a generic cross-section shape, Dnozzle,eq has been deﬁned as the diameter of the circular
section with the same area. The length of the discharging chamber has been set equal to
35Dnozzle,eq. The position of the Mach disk is expected to be around 2 Dnozzle,eq and the
length of the potential core about 26 Dnozzle,eq (see Franquet et al. 2015). Consequently, the
length of the discharging chamber has been deemed sufﬁcient to solve the near-ﬁeld zone
of the jet. The diameter of the chamber has been set to 14 Dnozzle,eq, enough to avoid the
interaction with the boundary condition along the lateral surface. The convergent nozzle
has been preferred to
convergent–divergent conﬁgurations in order toanalyse ﬂows at sonic
condition (Mach equal to 1) in the exit section. Moreover, a geometrical conﬁguration of
this kind can be considered an acceptable approximation of DI gaseous injectors for ICE
applications (Yip et al. 2019).
The choice of the cross-section area is coherent with benchmark experiments on H
2
DI ICE. All the nozzles have the same outlet area of 1.67 mm 2, which is the exit area
of the circular injector equipping the H 2 optical engine tested at the Sandia National
Laboratories (Wallner et al. 2013). Sketches of the sections are reported in ﬁgure 2 .F o r
the rectangular and elliptical sections, ARs (deﬁned as the ratio between the major, A,
to minor, B, sides for the rectangular section, and between the major to the minor axes
for the elliptical one) equal to 1.5, 5.0 and 8.0 have been taken into account. The AR 8.0
has been selected on the basis of manufacturing considerations: for the chosen outlet area,
970 A8-4
https://doi.org/10.1017/jfm.2023.603
 Published online by Cambridge University Press

<!-- PDF_PAGE: 5 -->

Gas-dynamic and mixing analysis of under-expanded hydrogen jets
100 µm
(b)(a)
50 µm
Figure 3. ( a) Representation of the numerical grid on a section plane. ( b) Detail of the mesh reﬁnement on
two boxes downstream of the nozzle exit section.
an elliptical section featuring an even higher AR would result in an excessive curvature
along the minor axis plane. The minimum AR has been chosen to be close to one, while
the AR 5 has been selected as a middle value between the maximum and minimum ARs.
The triangular section is equilateral, while the star is composed of an inner central square
sharing sides with four equilateral triangles. By examining this set of shapes, insights
regarding the inﬂuence of constant curvature (circular section), continuously varying
curvature (elliptical section), convex and concave angles (rectangular,
triangular and star
section) can be obtained.
3. Numerical model and validation
In ﬁgure 3 a cut plane of the mesh employed in this work is reported, along with an
enlargement downstream of the nozzle exit section. The mesh is made up of tetrahedral
elements, which is a useful feature at such a stage of the study, in which no information
about the orientation of the main eddies is available. T wo levels of reﬁnement can be
observed in the enlargement. A mean cell size of 50 µm has been applied in the near-ﬁeld
zone of the jet, where intense gas-dynamic phenomena are expected to occur. Externally to
the near-ﬁeld zone, an average cell size of 100µm has been deemed sufﬁcient to effectively
capture the
mixing layer of the jet, responsible for the diffusion of the H 2 into the ambient
ﬂuid (see Anaclerio et al. 2023). The general physics behaviour of the ﬂow is described
by the following mass, momentum and energy equations:
∂ρ
∂t + ∇· (ρv) = 0,
∂(ρv)
∂t + ∇· (ρvv) =− ∇ p + ∇· τ+ ρf ,
∂
∂t
(
ρ
(
e + v2
2
))
+ ∇·
(
ρv
(
h + v2
2
))
= ∇·
(
k∇ T −
∑
i
hiJi + τ· v
)
.
⎫
⎪⎪⎪
⎪⎪⎪
⎬
⎪⎪⎪
⎪⎪⎪
⎭
(3.1)
Here ρ is the local ﬂow density, v the velocity vector, p the static pressure, τ the deviatoric
stress tensor, f the mass forces vector, e the internal energy, h the enthalpy, k the thermal
conductivity, T the temperature, hi the enthalpy of the ith species and Ji the diffusion ﬂux
of the ith species (see ( 3.5)). In this work the steady form of the conservation equations
has been solved. Indeed, as previously veriﬁed by the authors (see Anaclerio et al. 2023),
the characteristic variation of the NPR during the injection in ICE applications is too small
to produce hysteretic effects. Therefore, features of the shock system can be analysed by
means of a steady computation. The coupled pressure-based algorithm has been used to
solve the conservation equations. In the pressure-based solvers, the mass conservation
970 A8-5
https://doi.org/10.1017/jfm.2023.603
 Published online by Cambridge University Press

<!-- PDF_PAGE: 6 -->

G. Anaclerio, T. Capurso and M. Torresi
equation is replaced by a pressure-corrected continuity equation, in such a way that the
velocity ﬁeld satisﬁes the continuity. In the coupled formulation the momentum and
pressure-corrected continuity equations are solved simultaneously. Energy, turbulence and
all of the other transport equations are solved successively. Even though the pressure-based
formulation has been conceived for incompressible ﬂows, its applicability has been
extended to compressible regimes too (see Denner 2018). Moreover, because of the
coupling between the momentum equation and pressure-corrected continuity, the coupled
scheme is closest to the density-based solver.
The mixture has been modelled as a real
gas, using the Redlich–Kwong equation of state (EoS). According to Bonelli, Viggiano
& Magi ( 2013), this model is suitable for hydrogen numerical computations, because of
the ability to closely match the experimental data of the National Institute of Standards
and
Technology in terms of compressibility factor. When comparing the ideal-gas model
with the real-gas models for a high pressure injection (750 bar), Bonelli observed a
higher intensity of the Mach disk shock when using the real-gas models. The same
conclusion has been drawn by the authors for a 10 bar injection in a previous work (see
Anaclerio et al. 2023)
and, thus, the Redlich–Kwong EoS has been here adopted. The
Redlich–Kwong EoS is one of the cubic EoS available in ANSYS Fluent ®, whose general
form is
p = RT
v − b + c − a
v2 + vδ+ ϵ , (3.2)
where a, b, c, δ and ϵ are parameters related to the ﬂuid critical pressure and critical
temperature ( pc, Tc), to the acentric factor ω and speciﬁc volume v. The acentric factor
ω is deﬁned as ω =− log10( psat/pc), where the saturation pressure psat is evaluated for
T = 0.7Tc. It is a measure of the non-sphericity of molecules, and inﬂuences the boiling
point of the species. ANSYS Fluent ® computes the generic critical constant Ccm of the
mixture (i.e. the critical pressure and critical temperature of the mixture) on the basis of
the mass fractions xi and critical constants Cci of each ith component (i.e. the critical
pressure and critical temperature of each component in the mixture) as
Ccm =
N∑
i=1
xiCci. (3.3)
In addition to the conservation of mass, momentum and energy, the injection process for
a mixture of N chemical species is captured by solving N − 1 transport equations in the
form
∂ρYi
∂t + ∇· (ρvYi) =− ∇· Ji + Ri + Si, (3.4)
where ρ and v are the local density and velocity, Yi is the mass fraction for the ith species,
Ri is the rate of production by chemical reactions and Si is a user-deﬁned source term.
Here Ji is the diffusion ﬂux of the ith species due to concentration and thermal gradients.
For turbulent ﬂows, it is computed as
Ji =−
(
ρDi,m + μt
Sct
)
∇ Yi − DT,i
∇ T
T , (3.5)
where Di,m is the mass diffusion coefﬁcient, μt the turbulent viscosity, Sct the turbulent
Schmidt number and DT,i the thermal diffusion coefﬁcient of the ith species, accounting
970 A8-6
https://doi.org/10.1017/jfm.2023.603
 Published online by Cambridge University Press

<!-- PDF_PAGE: 7 -->

Gas-dynamic and mixing analysis of under-expanded hydrogen jets
100
80
60
1/YH2
40
20
050 100 150 200 250
k-ϵ
k-ω SST
RSM
Experimental
z/req
Figure 4. Comparison between the experimental (Ruggles & Ekoto 2014) and numerical results of the
reciprocal H2 mass fraction (YH2 ) along the axial direction ( z) for an AR 8.0 rectangular jet, NPR = 10.
for the Soret effect. To better estimate the diffusion of the chemical species, the kinetic
theory model provided by ANSYS Fluent ® has been exploited to compute the mass
diffusion coefﬁcient Di,m. The nth species is computed by difference, since ∑N
i=1 Yi = 1
must hold. At the inlet of the domain, a ﬂow of pure hydrogen has been applied by setting
the H
2 mass fraction to 1. Total conditions of 10 bar and 300 K have been imposed too.
Both the right face and the lateral surfaces of the discharging cylinder have been treated as
pressure outlet boundaries (see ﬁgure 1), setting a static pressure equal to 1 bar. To reduce
the computational time, water vapour in the air has not been taken into account, thus
solving transport equations only for H2 and O2. This choice is reasonable since the volume
fraction of water vapour in both pressurized hydrogen and ambient air is negligible. For
the aforementioned boundary conditions, the NPR results equal 10; hence, extremely
under-expanded conditions are expected to be achieved. Therefore, signiﬁcant variations of
the temperature inside the jet are expected, leading to the adoption of the three parameters
Sutherland law to model the local viscosity. Spatial derivatives have been discretized
by means of a second-order accurate upwind scheme. Several studies are present in
the literature to assess the most suitable turbulence model for RANS equations closure.
According to Senesh & Babu ( 2012), for round compressible jets
, the Spalart–Allmaras
model over-predicts the axial velocity decay rate and under-predicts the potential core
length (i.e. the near-ﬁeld zone where the gas-dynamic effects are predominant). The
re-normalisation group (RNG) k-ε better captures the potential core length, but the axial
decay rate is again over-predicted. The standard k-εcomputes an axial decay rate slightly
slower than the RNG model, but under-predicts the potential core length. Tide & Babu
(2008) compared the Wilcox k-ω model against the shear stress transport (SST) k-ω using
a jet at Mach number 0.9 as a benchmark. Both the models showed acceptable agreement
with the experimental data, but the SST k-ω was found to be less sensitive to the mesh
density, which is a favourable characteristic to exploit when
3-D simulations have to be
carried out. To deﬁne the most suitable turbulence model, and to test the validity of the
set-up previously described, a validation step has been deemed necessary. T wo benchmarks
have been carried out. In the ﬁrst one, the experimental data provided by Ruggles & Ekoto
(2014) have been exploited to assess the validity of the numerical results in terms of H 2
axial penetration. In this case, a rectangular nozzle (AR = 8) has been tested applying a
NPR equal to 10. In ﬁgure 4 the reciprocal of the H 2 axial mass fraction has been plotted
against the non-dimensional axial position (being req the radius of the circular area with
970 A8-7
https://doi.org/10.1017/jfm.2023.603
 Published online by Cambridge University Press

<!-- PDF_PAGE: 8 -->

G. Anaclerio, T. Capurso and M. Torresi
8
6
4
2
0
(mm)
10 bar
Experimental Numerical (b)(a)
Figure 5. ( a) Experimental Schlieren provided by Hecht et al. (2015). (b) Numerical Schlieren computed
with a near-ﬁeld cell size of 10 µm.
Near-ﬁeld cell size (µm )5 1 02 03 05 0 1 0 0
Disk position (mm) 2.02 2.00 1.99 1.96 1.95 1.89
Table 1. Mesh sensitivity analysis. Comparison of the Mach disk position for different grid reﬁnements.
the same area). The k-ε,S S T k-ω and Reynolds stress model (RSM) closures have been
examined using the default conﬁgurations set by ANSYS Fluent ®. As it can be observed,
the SST k-ω provides the closest outcomes to the experimental data, and consequently ,
it has been chosen for the RANS closure. As a secondary step, the ability to capture the
gas-dynamic features of the under-expanded jets has been
analysed. In particular, a circular
nozzle of 1 mm diameter under a NPR of 10 has been taken into account. As can be seen in
the experimental Schlieren picture reported in ﬁgure 5 (see Hecht, Li & Ekoto 2015), the
Mach disk is located at about 2 mm from the nozzle exit section, which is coherent with
the theoretical position computed by the following correlation (see Franquet et al. 2015):
Hdisk
Dnozzle
= 0.63
√
NPR. (3.6)
Here Hdisk is the Mach disk position and Dnozzle the nozzle exit diameter. In this case
Hdisk = 1.99 mm. As reported in table 1, the numerical position of the shock is correctly
captured by the simulations. The cell size of 50 µm in the near-ﬁeld zone of the jet has
been considered a good compromise between the accuracy of the results and the required
computational time. Hence, this level of reﬁnement and the discussed numerical set-up
have been considered suitable for the further studies proposed in this work.
4. Results
4.1. Inﬂuence of the section shape
Comparisons among the different shapes have been performed applying identical total
conditions at the inlet, in order to have the same choked mass ﬂow rate. The Reynolds
number, computed choosing Dnozzle,eq as a reference length, is equal to 1 .1 × 105 at the
outlet section. In ﬁgure 6 the longitudinal numerical Schlieren of the jet issuing from the
970 A8-8
https://doi.org/10.1017/jfm.2023.603
 Published online by Cambridge University Press

<!-- PDF_PAGE: 9 -->

Gas-dynamic and mixing analysis of under-expanded hydrogen jets
1920
(kg m–4)
1680
1440
1200
960
720
480
240
0
Density
gradient
Shear layer Barrel shock
Mach disk
Reflected shock Expansion fan
Figure 6. Numerical Schlieren picture of the under-expanded jet obtained from the circular section,
NPR = 10, T0 = 300 K, on a longitudinal section plane.
–15
0
0.5
1.0
1.5
2.0Mach number
2.5
3.0
Expansion
Mach disk
Mach number–circular section
Flow re-acceleration
Nozzle
acceleration
3.5
4.0
–10 –5 0 5 10 15 20
Position (mm)
25 30 35 40
Figure 7. Mach number along the axis of the circular jet, NPR = 10.
circular section nozzle is shown. The distinctive features widely described in the literature
are visible. An expansion fan occurs at the nozzle exit (the white v-shaped area starting
at the nozzle exit section), due to the pressure difference between the exit section and the
surrounding ambient. The weak waves of the fan reﬂect at the jet boundary and turn into
compression waves, whose coalescence leads to the formation of the barrel shock. This
feature begins to be visible slightly downstream of the exit section and is characterized
by a convergent shape. At NPR = 10 the regular reﬂection of the barrel shock at the axis
is no longer possible. Hence, a Mach disk normal to the ﬂow is formed. In ﬁgure 6
it
appears to have a negligible curvature, conversely to other cases shown in the following.
The Mach reﬂection is completed by the formation of a reﬂected shock emanating from
the point shared by the Mach disk and the barrel shock. Flow just downstream of the Mach
disk is subsonic, while it is still supersonic after passing through the reﬂected shock. As a
consequence, a shear layer is needed to divide the two ﬂows. It appears to be convergent,
resulting in a subsequent ﬂow acceleration after the Mach disk (see ﬁgure 7 ), which is
however not sufﬁcient to repeat the pattern.
970 A8-9
https://doi.org/10.1017/jfm.2023.603
 Published online by Cambridge University Press

<!-- PDF_PAGE: 10 -->

G. Anaclerio, T. Capurso and M. Torresi
Density
gradient
0
240
480
720
960
1200
1440
1680
1920
3.2 mm
2.7 mm
1.5 mm
1.0 mm
0.5 mm
(kg m–4)
(a)( b)
Figure 8. Longitudinal numerical Schlieren picture of the under-expanded jet from the triangular section:
(a) in the symmetry plane ,a n d( b) in a plane parallel to the triangle base passing for the centre of the triangle.
Static
pressure Over-expansion
0.71 1.78 2.84 3.91 4.98
Corner shock
Mach disk
Reflected shock
(bar)
(a)( b)
Figure 9. ( a) Contours of the static pressure at the nominal exit section of the triangular nozzle ,a n d( b) 3-D
shock structure of the jet by means of the shock detection method proposed by Lovely & Haimes ( 1999).
The above-mentioned ﬂow pattern is perfectly axisymmetric and easy to describe.
Moreover, it is characterized by an axisymmetric H 2 penetration and distribution
along either the radial and axial directions. Signiﬁcant differences from the classical
shock-expansion structure of circular jets have been observed in the non-circular sections.
4.1.1. Triangular section
The equilateral triangular section has been selected to investigate the inﬂuence of acute
angles on the shock-expansion system. In ﬁgure 8 the longitudinal Schlieren pictures are
reported. Here, some major differences with respect to the classical circular nozzle are
present. As it can be observed along the symmetry plane in ﬁgure 8(a), the barrel shock
forms almost immediately from the upper vertex, while the onset is delayed from the edge
of the triangle. The reasons behind the shock formation are indeed quite different. At the
vertex (convex zone), the interaction between the fans originating from two consecutive
sides leads to a locally over-expanded ﬂow: pressure drops below the ambient pressure,
and consequently
, a shock wave quickly forms to re-compress the ﬂow. The over-expanded
condition is visible in ﬁgure 9(a), reporting the static pressure contours at the exit section
of the nozzle: while the static pressure is equal to 284 000 Pa along the edges, a minimum
of about 70 000 Pa is reached at the corners, which is below the ambient pressure of
100 000 Pa. The re-compression shock wave is the barrel shock visible in ﬁgure 8(a). At
the basis, the classical formation of the barrel shock takes place. However, coalescence of
970 A8-10
https://doi.org/10.1017/jfm.2023.603
 Published online by Cambridge University Press

<!-- PDF_PAGE: 11 -->

Gas-dynamic and mixing analysis of under-expanded hydrogen jets
Density
gradient
240
480
720
960
1200
1440
1680
1920
(kg m–4)
Corner
shock
Mach
reflection
Reflected
shock
Shear
layer
(a)( b)
(c)( d)( e)
Figure 10. Normal numerical Schlieren pictures of the jet issuing from the triangular section on ﬁve different
planes normal to the jet axis: at (a) 0.5 mm, ( b) 1.0 mm, ( c) 1.5 mm, ( d) 2.7 mm and at (e) 3 . 2m mf r o mt h e
exit section.
the expansion waves is quicker for higher curvatures (i.e. for smaller radii of the osculating
circles): in this case, the edge curvature equal to zero leads to a very delayed formation
of the barrel shock. Such a trend is visible in ﬁgure 8 (b), in which the shock-expansion
system is symmetrical. To clarify the structure of the shock system, the shock detection
method proposed by Lovely and Haimes (see Lovely & Haimes 1999) has been exploited
to produce ﬁgure 9 (b). Here, the three corner shocks are clearly visible. They result to
point towards the axis, eventually reﬂecting and forming a Mach disk normal to the axis,
followed by a reﬂected shock. In ﬁgure 10 the numerical Schlieren pictures relative to
ﬁve planes normal to the axis are shown to further draw insights of the shock system. At
0.5 mm from the nozzle exit, it can be observed that the over-expansion condition leads
to the onset of the corner shock waves. Moving further downstream, the shock waves
become wider (see ﬁgure 10b,c) and eventually reﬂect ( ﬁgure 10d). In this speciﬁc case,
the reﬂection is irregular
; hence, a lateral Mach disk and the related reﬂected waves form.
The incident shock system is then made up of the three corner shocks, their Mach disks
and the lateral reﬂected waves. The incident shock system points towards the jet axis,
causing the onset of a strong normal Mach disk. After this, the shear layer and the reﬂected
shock propagate downstream (both shown in ﬁgure 10(e) ). Another distinctive feature
observable in the Schlieren pictures is the growth of the jet boundary. The boundary
expands faster from the
centre of the edges and slower from the vertices, resulting in a
deformation that leads to a three-lobe jet. This behaviour is related to the higher level of
the vorticity magnitude (i.e. the vorticity module) at the cent r eo ft h ee d g e s .I nﬁgure 11(a)
the vorticity magnitude distribution along the jet perimeter immediately downstream of
the exit section is superimposed to the jet boundary of ﬁgure 10(e). As can be observed,
the higher vorticity leads to a faster deformation of the boundary from the middle of the
sides, ultimately generating the three-lobe shape observed at 3.2 mm from the exit section.
970 A8-11
https://doi.org/10.1017/jfm.2023.603
 Published online by Cambridge University Press

<!-- PDF_PAGE: 12 -->

G. Anaclerio, T. Capurso and M. Torresi
V orticity
magnitude 1.6 23 427 851 1280 1700 2120
Minimum
distance
Velocity
magnitude
(m s–1)2.4 3.2 4.0 (s ∙107)
(a) (b)
Figure 11. ( a) Vorticity magnitude contours at the triangular nozzle exit section superimposed to the jet
boundary developed further downstream. The high vorticity zones behave as traction points, driving the
deformation of the boundary. ( b) Velocity magnitude immediately downstream of the exit section: higher
velocity is observed along the perimeter due to the earlier expansion of the outer ﬂow.
Thus, the high vorticity magnitude zones behave as traction points governing the
deformation of the boundary. In ﬁgure 11(b) the velocity magnitude is shown immediately
downstream of the exit section. Higher velocities are found along the jet boundary, because
the ﬂow, ejected in the proximity of the wall, meets the expansion fan earlier with respect
to the ﬂow released from the inner section. As the velocity module must be unique at the
centre of the shape, higher velocity gradients are expected where the distance between
the shape centre and the triangle side is minimum (see ﬁgure 11b). This can be considered
the reason why a higher vorticity module has been observed in the middle of the side
edges.
4.1.2. Star-shaped section
The triangular section has a convex shape. Consequently, it has been deemed interesting
to analyse the jet structure developed by a nozzle section with convex and concave
features: the star-shaped section. This shape has eight vertices: four equal to 60 ◦ and
four equal to 210 ◦, alternatively arranged. Figure 12 (a) reports the numerical Schlieren
along a plane passing through two opposite convex vertices. As already observed in the
triangular nozzle, the onset of shock waves just downstream of the exit section is found.
Conversely, in the plane passing through two opposite concave vertices, see ﬁgure 12(b),
the occurrence of the barrel shock is delayed. As already discussed for the triangular
section, the onset of the shock waves emanating from the convex vertices is due to the
over-expanded condition occurring when the angle is acute, as shown in the pressure
contours reported in ﬁgure 13 (a). In the same picture, it can be observed that concave
vertices (obtuse angles) are not subject to the over-expanded condition, since the expansion
fans do not cross in the proximity of concave vertices. The
3-D shock system is reported in
ﬁgure 13(b), where it can be observed that the re-compression corner shocks reﬂect along
the axis forming a normal Mach disk, followed by its reﬂected shock. Schlieren pictures
normal to the jet axis are reported in ﬁgure 14. At the exit section the jet holds the same
970 A8-12
https://doi.org/10.1017/jfm.2023.603
 Published online by Cambridge University Press

<!-- PDF_PAGE: 13 -->

Gas-dynamic and mixing analysis of under-expanded hydrogen jets
Density
gradient
0
240
480
720
960
1200
1440
1680
1920
2.8 mm
2.1 mm
1.4 mm
0.7 mm
Exit
(kg m–4)
(a)( b)
Figure 12. Longitudinal numerical Schlieren picture of the under-expanded jet from the star nozzle: ( a)i na
plane passing through the vertices of the triangles ,a n d( b) in a plane along the diagonal of the inner square.
(a)
 (b)
Static
pressure Over-expansion
0.56 1.56 2.56 3.56 4.56 Corner shock
Corner shock
Mach disk
Reflected shock
(bar)
Figure 13. ( a) Contours of static pressure at the exit section of the star shaped nozzle and ( b) 3-D visualization
of the shock system developed by the star nozzle, reconstructed by means of the shock detection method
proposed by Lovely & Haimes ( 1999).
shape of the nozzle. At 0.7 mm, the corner shock waves propagating from the convex
vertices are visible. Further downstream, they expand (1.4 mm) and reﬂect each against
the other in an irregular way (note, in the picture at 2.1 mm, the formation of the lateral
Mach disks and reﬂected shocks). At 2.8 mm the Mach disk normal to the jet axis has
already formed, and consequently, the shear layer and the reﬂected shocks can be observed.
Regarding the jet boundary, it can be noted that the growth is faster along the diagonals
of the inner square with respect to the tip vertices of the triangles. This behaviour can
be justiﬁed observing the vorticity contours immediately downstream of the nominal exit
section (ﬁgure 15): the higher values are found at the concave vertices, where the enhanced
turbulent diffusion leads to a much quicker growth of the boundary along the diagonals
of the square. Thus, as already discussed for the triangular case, zones characterized by
a higher vorticity magnitude behave as
traction points, more quickly stretching the jet
boundary towards the surrounding ambient. Such zones are once again the closest points
to the shape centre, conﬁrming that greater vorticity levels are due to the higher velocity
gradients.
4.1.3. Elliptical section
In ﬁgure 16 the numerical Schlieren pictures are reported for a jet issuing from the AR
1.5 elliptical nozzle. It can be observed that the occurrence of the barrel shock is quicker
along the major axis plane, whereas it has a lower intensity along the minor axis plane.
970 A8-13
https://doi.org/10.1017/jfm.2023.603
 Published online by Cambridge University Press

<!-- PDF_PAGE: 14 -->

G. Anaclerio, T. Capurso and M. Torresi
(a)( b)
(c)( d)( e)
Density
gradient
240
0
480
720
960
1200
1440
1680
1920
(kg m
–4) Corner shocks
Corner shocks Mach reflection Reflected shock
Shear layer
Figure 14. Normal numerical Schlieren pictures of the jet issuing from the star section on ﬁve different planes
normal to the jet axis: ( a) at the nozzle exit, and at (b) 0.7 mm, ( c) 1.4 mm, ( d) 2.1 mm and (e) 2.8 mm from
the exit section.
V orticity
magnitude
2.2 2.8 3.4 4.0 (s ∙ 107)
Figure 15. Vorticity magnitude contours at the star nozzle exit section superimposed to the jet boundary
developed further downstream. Also in this case the high vorticity zones behave as traction points, driving
the deformation of the boundary.
This behaviour can be explained looking at ﬁgure 17, which reports a sketch of the leading
waves of the fans originating at the endpoints of the major and minor axes. Since the
pressure ¯p just after the expansion fans at the axis location must be unique, the inclination
of the fan from the major axis must be lower (i.e. α<θ in ﬁgure 17). As a consequence,
970 A8-14
https://doi.org/10.1017/jfm.2023.603
 Published online by Cambridge University Press

<!-- PDF_PAGE: 15 -->

Gas-dynamic and mixing analysis of under-expanded hydrogen jets
Density
gradient
0
240
480
720
960
1200
1440
1680
1920
3.5 mm
2.1 mm
0.7 mm
(kg m–4)
(a)( b)
Figure 16. Longitudinal numerical Schlieren pictures of the jet issuing from the elliptical nozzle with
AR = 1.5: (a) major axis plane and ( b) minor axis plane.
Major axis
Minor axis
Expansion fan
leading wavepˉθα
Figure 17. Sketch of the expansion fans leading waves emanating from the major and minor axes of the
elliptical section. Here α and θ represent the wave inclination from the major and minor axes, whereas ¯p
stands for the pressure level at the axis just after the fans.
reﬂection of the expansion waves and coalescence of the compression ones is quicker
along the major axis plane, resulting in an earlier formation of barrel shock. Hence, it can
be concluded that the coalescence is faster for higher curvatures, and vice versa.W h a th a s
been described is conﬁrmed by both the 3-D shock system in ﬁgure 18 and the normal
Schlieren reported in ﬁgure 19. At 0.7 mm from the nozzle exit, the incident barrel shock
is only visible at the extremes of the major axis, whereas it begins to be observable along
the minor axis at 2.1 mm from the exit section. At the imposed NPR of 10, the incident
shock system reﬂects in an irregular way, forming a normal Mach disk followed by its
shear layer and the reﬂected shock, both visible at 3.5 mm downstream of the exit section.
In the sequence reported in ﬁgure 19, the axis switching phenomenon can be observed: the
boundary expands faster along the minor axis plane as an effect of the higher level of the
vorticity magnitude (whose distribution has not been reported for the sake of brevity).
4.1.4. Rectangular section
The shock system developed by a rectangular nozzle of AR 1.5 is reported in the
longitudinal planes in ﬁgure 20 . Also in this case, the barrel shock forms earlier along
the major axis plane, resulting in the barrel shock being more intense in the major
axis plane and less intense in the minor axis plane. Differently from the elliptical case
previously analysed, such a trend cannot be justiﬁed by different curvatures along the
section perimeter. What has been observed can be explained by looking at ﬁgure 21 ,
which reports the static pressure contours at the nozzle exit section along with the 3-D
shock system, and ﬁgure 22 , which shows the normal Schlieren pictures. Similarly to
970 A8-15
https://doi.org/10.1017/jfm.2023.603
 Published online by Cambridge University Press

<!-- PDF_PAGE: 16 -->

G. Anaclerio, T. Capurso and M. Torresi
Reflected shock
Mach disk
Barrel shock
Figure 18. Shock system developed by the elliptical section, reconstructed by means of the shock detection
method proposed by Lovely & Haimes ( 1999).
(a)( b)( c)
Density
gradient
240
0
480
720
960
1200
1440
1680
1920
(kg m
–4)
Reflected shockBarrel shock
Barrel shock
Shear layer
Figure 19. Normal numerical Schlieren pictures of the jet issuing from the elliptical nozzle with AR = 1.5,
on three different planes normal to the jet axis: at (a) 0.7 mm, (b) 2.1 mm and (c) 3.5 mm from the exit section.
Density
gradient
0
240
480
720
960
1200
1440
1680
1920
3.0 mm
2.5 mm
2.1 mm
0.7 mm
(kg m–4)
(a)( b)
Figure 20. Longitudinal numerical Schlieren pictures of the jet issuing from the rectangular nozzle with
AR = 1.5: (a) major axis plane and ( b) minor axis plane.
970 A8-16
https://doi.org/10.1017/jfm.2023.603
 Published online by Cambridge University Press

<!-- PDF_PAGE: 17 -->

Gas-dynamic and mixing analysis of under-expanded hydrogen jets
Static
pressure Over-expansion
0.6 1.4 2.2 3.0 3.8 Corner shock
Corner shock
Reflected shock
Mach disk(bar)
(b)(a)
Figure 21. ( a) Static pressure contours at the nominal exit section for the AR 1.5 rectangular nozzle and ( b)
visualization of the 3-D shock system, reconstructed by means of the shock detection method proposed by
Lovely & Haimes (1999).
Corner shocks
Corner shocks
Lateral mach reflection Reflected shock
Shear layer
(kg m–4)
1920
1680
1440
1200
960
720
480
240
0
Density
gradient
(b)(a)
(d)(c)
Figure 22. Normal numerical Schlieren pictures of the jet issuing from the rectangular nozzle with AR = 1.5
on four different planes normal to the jet axis: at (a) 0.7 mm, ( b) 2.1 mm, (c) 2.5 mm and (d) 3 . 0m mf r o mt h e
exit section.
the triangular and star-shaped sections, the coexistence of the expansion fans at the
vertices of the exit section leads to an over-expanded condition. As a consequence, four
re-compression shock waves occur at the vertices, as visible in ﬁgures 21(b)a n d 22(a).
At 2.1 mm from the exit section, the re-compression waves have met along the major axis
plane, resulting in the barrel shock visible in ﬁgure 20(a). Along the minor axis plane, the
barrel shock is still not visible because the shock waves have not met yet. At 2.5 mm the
reﬂection of the shock waves is irregular, leading to the formation of a lateral Mach disk
and the related reﬂected waves. Similarly to the triangular and star sections, the incident
shock system is then made of the four corner shocks, the lateral Mach disk and the reﬂected
970 A8-17
https://doi.org/10.1017/jfm.2023.603
 Published online by Cambridge University Press

<!-- PDF_PAGE: 18 -->

G. Anaclerio, T. Capurso and M. Torresi
(kg m–4)
1920
1680
1440
1200
960
720
480
240
0
Density
gradient
AR 5.0 AR 5.0
AR 8.0 AR 8.0
2.1 mm
0.7 mm
(b)(a)
(d)(c)
Figure 23. Longitudinal numerical Schlieren pictures for the elliptical nozzles: ( a)A R5 . 0 –m a j o ra x i s
plane, (b) AR 5.0 – minor axis plane, (c) AR 8.0 – major axis plane, ( b)A R8 . 0 – minor axis plane.
(kg m–4)
1920 AR 5.0 AR 5.0
Compression shock waves Lateral mach reflection
1680
1440
1200
960
720
480
240
0
Density
gradient
(b)(a)
Figure 24. Normal numerical Schlieren pictures for the jet issuing from the elliptical nozzle with AR = 5.0
on two different planes normal to the jet axis: at (a) 0.7 mm and ( b) 2.1 mm from the nozzle exit section.
shocks. The incident system points towards the axis and reﬂects forming a normal Mach
disk, followed by the shear layer and the reﬂected shock, both visible at 3.0 mm from the
exit section. The growth of the jet boundary is very slow at the corners and faster from the
centre of the sides. As in the previous cases, higher values of the vorticity magnitude have
been observed in the centre of the longer sides, which are once again the closest points to
the section centre (a picture of the vorticity distribution has not been reported for the sake
of brevity). Such high vorticity zones lead to a faster growth along the minor axis plane,
resulting in the four-lobe boundary at 3.0 mm from the exit plane ( ﬁgure 22d).
970 A8-18
https://doi.org/10.1017/jfm.2023.603
 Published online by Cambridge University Press

<!-- PDF_PAGE: 19 -->

Gas-dynamic and mixing analysis of under-expanded hydrogen jets
3.3 4.7 6.0 7.3 8.7 10.0 2.0 3.6 5.2 6.8 8.4 10.0
(×104 Pa)Static pressure Static pressure
Over-expansionOver-expansion
(×104 Pa)
(b)(a)
Figure 25. Static pressure contours at the nozzle exit section for ( a) the AR 5.0 elliptical nozzle and ( b)t h e
AR 8.0 elliptical nozzle.
(kg m–4)
1920
1680
1440
1200
960
720
480
240
0
Density
gradient
AR 5.0 AR 5.0
AR 8.0 AR 8.0
2.0 mm
0.5 mm
(b)(a)
(d)(c)
Figure 26. Longitudinal numerical Schlieren pictures for the rectangular nozzles: ( a)A R5 . 0 –m a j o ra x i s
plane, (b)A R5 . 0 – minor axis plane, ( c)A R8 . 0 – major axis plane, ( b)A R8 . 0 – minor axis plane.
4.2. Inﬂuence of the AR
The rectangular and elliptical sections previously described have been further analysed.
Holding the same total conditions and the same nozzle exit area, the AR has been varied
to get insights of the inﬂuence on the structure and mixing characteristics of the jets. The
results of the AR 1.5 cases have been compared with the outcomes relative to nozzles with
ARs equal to 5.0 and 8.0. In ﬁgure 23 the longitudinal Schlieren of the elliptical sections
are reported. The ﬁrst row refers to the AR 5.0 case, while the second one to the AR 8.0
case. In both the cases, the barrel shock along the minor axis plane is not well deﬁned,
looking like a band rather than a thin shock. This can be attributed to the progressively
970 A8-19
https://doi.org/10.1017/jfm.2023.603
 Published online by Cambridge University Press

<!-- PDF_PAGE: 20 -->

G. Anaclerio, T. Capurso and M. Torresi
(a)( b)
Density
gradient
240
0
480
720
960
1200
1440
1680
1920
(kg m
–4)
Lateral mach reflectionCompression shock waves
AR 5.0AR 5.0
Figure 27. Normal numerical Schlieren pictures for the jet issuing from the rectangular nozzle with AR = 5.0
on two different planes normal to the jet axis: at (a) 0.5 mm and ( b) 2.0 mm from the nozzle exit section.
lower curvature of the section perimeter along the minor axis plane, as a result of which the
weak compression waves are not able to coalesce. For both sections, however, the barrel
shock along the major axis plane is well deﬁned, forming just downstream of the exit
section. While the normal Mach disk looks like a thin ﬂat discontinuity for the elliptical
section with an AR of 1.5, a rising curvature can be observed as the AR increases. The
shear layer in the AR 5.0 case constitutes a convergent duct on the major axis plane (as
already observed for the circular nozzle), whilst it looks straight along the minor
axis. In
the AR 8.0 case the normal Mach disk and the barrel shocks form a single curve without
any angular point along the major axis plane. Moreover, the subsequent shear layer does
not look as a continuous surface, since it is not visible in the major axis plane. Hence, it can
be imagined as formed by two surfaces
that do not meet in the major axis plane. Looking
at the normal Schlieren pictures reported in ﬁgure 24, the onset of re-compression shock
waves along the major axis can be appreciated, followed by a lateral Mach reﬂection as
previously described for the rectangular sections. From the pictures of the static pressure
contours reported in ﬁgure 25 , the origin of the shock waves can be attributed once
again to an over-expanded condition, similarly to what was already described for sections
characterized by convex angles. For the AR 5.0 case, the minimum pressure is found along
the major axis and is equal to 33 000 Pa. For the AR of 8.0, the drop is even greater,
reaching a minimum of 20000 Pa. Hence, when increasing the ARs , the high curvature
proﬁle at the extremes of the major axis acts like a convex angle, with an interaction
between the fans that lowers the static pressure below the ambient pressure. Similarly
to the elliptical cases, the AR has been found to deeply inﬂuence the ﬂow ﬁeld of the
rectangular jets. The longitudinal and normal Schlieren of the jets issuing from rectangular
nozzles with
an AR equal to 5.0 and 8.0 are reported in ﬁgures 26 and 27, respectively.
The genesis of the incident shock system is similar to the AR 1.5 case, formerly described,
with an over-expanded condition at the four corners of the exit section. For the AR 5.0
case, the minimum pressure is equal to 55 000 Pa, dropping to 33 000 Pa in the AR 8.0
case. Consequently, the barrel shock in the major axis plane forms as a consequence of the
interaction of the re-compression corner shock waves, while the curvature equal to zero of
the sides does not guarantee the coalescence of the weak compression waves in the minor
axis plane. A slight curvature of the normal Mach disk is visible in the major plane in the
AR 5.0 case. For the AR 8.0 case, the structure of the shock system in the same plane
is quite different. As shown in ﬁgure 26 (c), the Mach disk is divided into three parts: a
central outward curved disk and two lateral inward curved disks. Such
a condition might
be dependent on the speciﬁc geometry employed in this work, and the authors are willing
to deepen the causes in a future work.
970 A8-20
https://doi.org/10.1017/jfm.2023.603
 Published online by Cambridge University Press

<!-- PDF_PAGE: 21 -->

Gas-dynamic and mixing analysis of under-expanded hydrogen jets
4.0
3.5
3.0
2.5
Mach number
2.0
1.5
1.0
0.5
0
4.0
3.5
3.0
2.5
Mach number
2.0
1.5
1.0
0.5
0 0.5
1.0 1.5 2.0 2.5
AR
AR
Circular
Elliptical AR 1.5
Elliptical AR 5
Elliptical AR 8
Circular
Rectangular AR 1.5
Rectangular AR 5
Rectangular AR 8
3.0 3.5
1.0 1.5 2.0 2.5 3.0 3.5
Position (mm)
0.5
(b)
(a)
Figure 28. Mach number evolution along the jet axis for the ( a) elliptical and ( b) rectangular nozzles, and its
dependency on the AR.
In ﬁgure 28 (a,b) the evolution of the Mach number along the axis is reported for the
elliptical and rectangular cases, respectively. The circular case is shown for comparison
too. For both
shapes, as the AR increases, the expansion process is faster and the position
of the Mach disk progressively moves towards the nozzle exit section. Hence, the equation
commonly reported in the literature to assess the position of the Mach disk (Franquet et al.
2015) is here corrected as
Hdisk
Dnozzle,eq
= C(AR)CH
√
NPR, (4.1)
with C(AR) being a corrective coefﬁcient depending on the AR. In ﬁgure 29 we report
the C(AR) for three different NPRs (10, 15, 20). Whatever the NPR, C(AR) is well
970 A8-21
https://doi.org/10.1017/jfm.2023.603
 Published online by Cambridge University Press

<!-- PDF_PAGE: 22 -->

G. Anaclerio, T. Capurso and M. Torresi
(a)( b)
2
0.8
1.0
1.2
0.6
0.4
C(AR)
0.2
0.8
1.0
1.2
0.6
0.4
0.2
04 6 8 1 0
NPR 10
NPR 15
NPR 20
Aspect ratio
204 6 8 1 0
Aspect ratio
Figure 29. Plot of C(AR) for the (a) elliptical sections and ( b) rectangular sections at three different NPRs
(10, 15, 20).
Section NPR mq R 2
Elliptical 10 − 0.0389 1.0439 0.967
15 − 0.0402 1.0929 0.995
20 − 0.0350 1.0992 0.995
Rectangular 10 − 0.0403 1.0003 0.987
15 − 0.0326 1.0132 0.989
20 − 0.0277 1.0168 0.991
Table 2. Coefﬁcients of the linear interpolation (and related coefﬁcient of determination R2)f o rt h e
corrective factor C(AR) = m(AR) + q.
Nozzle exit section
Pressure isosurface (200.000 Pa)
Figure 30. Example of an isosurface pressure contour at the exit section of a rectangular nozzle (NPR = 10,
AR = 5).
approximated by a linear regression, whose coefﬁcients are reported in table 2 along with
the coefﬁcient of determination R2. An explanation for the drift of the Mach disk can be
drawn looking at the shape of the static pressure isosurfaces downstream the nozzle exit,
which look like ‘domes’ centred along the jet axis ( ﬁgure 30 ). The dome shape is the
result of the different tilt of the expansion fans along the two axes, as previously shown in
ﬁgure 17. In the rectangular sections, for all the ARs considered, it has been observed that
the fans originating from the major sides have the same inclination. Hence, as visible in
ﬁgure 31, when increasing the AR
, the distance between the major sides lowers, leading
to a quicker pressure drop along the axis. As a result, the expansion fans from the minor
sides must have a higher tilt angle (with respect to the streamwise direction), and the
970 A8-22
https://doi.org/10.1017/jfm.2023.603
 Published online by Cambridge University Press

<!-- PDF_PAGE: 23 -->

Gas-dynamic and mixing analysis of under-expanded hydrogen jets
AR 1.5
(a)( b)
α
α
AR 5.0
Major axis
Flattening of the pressure isosurface
Minor axis
Figure 31. Sketch illustrating the inﬂuence of the area ratio over the expansion fans geometry.
1.0
0.8
0.6
0.4
H2 mass fraction
0.2
05 1 0
Position (mm)
15 20 25 30 35
Circular
Elliptical AR 1.5
Elliptical AR 5
Elliptical AR 8
Star
Figure 32. Hydrogen axial distribution for the circular, elliptical and star nozzles.
pressure isosurfaces are progressively ﬂattened towards the nozzle exit section. This can be
considered the reason why a progressively higher pressure drop is found at the corners of
the exit section. Because of this, the re-compression corner shocks must be more intense as
the AR increases, therefore being more inclined with respect to the streamwise direction.
The higher tilt of the re-compression corner shocks can then be considered the reason
why the Mach disk moves towards the exit section. A similar mechanism takes place
for the elliptical sections too. Fans from the minor axis are found to incrementally have
a higher tilt as the AR increases, eventually reaching the same inclination found in the
rectangular section when the AR is 8.0, because
the curvature tends to zero. Consequently,
pressure isosurfaces are ﬂattened towards the exit section, leading to a higher level of
over-expansion along the major axis. Also in this case, then, the re-compression shock
waves must be more intense, resulting in a higher inclination and eventually shifting the
Mach disk towards the nozzle exit section.
In ﬁgures 32 and 33 the H 2 axial mass fractions are reported. For both shapes, the
axial decay is similar to the circular section case when AR = 1.5. Conversely, as the AR
increases, the axial decay is faster, suggesting a higher radial spread due to a quicker
H2–air mixing in the external layer of the jet. The same trend is conﬁrmed by the radial
plots at ten equivalent diameters from the exit section, reported in ﬁgure 34. In particular,
a saddle-shaped proﬁle is observed in the AR 8.0 rectangular nozzle, which is indicative
970 A8-23
https://doi.org/10.1017/jfm.2023.603
 Published online by Cambridge University Press

<!-- PDF_PAGE: 24 -->

G. Anaclerio, T. Capurso and M. Torresi
1.0
0.8
0.6
0.4
H2 mass fraction
0.2
05 1 0
Position (mm)
15 20 25 30 35
Circular
Rectangular AR 1.5
Rectangular AR 5
Rectangular AR 8
Triangular
Figure 33. Hydrogen axial distribution for the circular, rectangular and triangular nozzles.
of a ‘split’ of the jet into two parts. The saddle-shaped proﬁle has been analysed by several
authors in the literature, and it has been mostly ascribed to the vorticity developed by the
rectangular section (Van der Hegge Zijnen 1958; Grinstein 2001; Vouros et al. 2015). At
the same AR, the axial decay is faster for the rectangular section than the elliptical. The
triangular and star-shaped sections show an axial decay similar to the AR 1.5 rectangular
case and to the AR 5.0 elliptical case, respectively (see ﬁgures 32 and 33). The faster
mixing and the axial decay rate can be linked to
a lower hydraulic diameter, i.e. to the larger
perimeter of the section. At the same time, they can be associated to the level of vorticity
magnitude generated in the mixing layer. In table 3 the mean levels of vorticity magnitude,
computed on the isosurface characterized by a H 2 mass fraction of 0.1, are reported. For
the elliptical and rectangular sections, it can be seen that the vorticity increases with the
AR, suggesting a more intense mass exchange promoted by the turbulent eddies. Moreover,
at a ﬁxed AR, vorticity is higher for the rectangular section with respect to the elliptical
one, reﬂecting the faster axial decay of the rectangular sections. The triangular section
has a level of vorticity close to
the AR 1.5 rectangular section, and the star to the AR 5.0
elliptical section. Hence, the authors believe vorticity can be the basic parameter to explain
the different levels of mixing shown in ﬁgures 32–34.
Another analysis is herein presented to provide the reader with quantitative information
about the mixing process determined by the different sections. To such a purpose, an
analysis based on the normalized standard deviation of the H 2 mass fraction (σ(YH2)/¯YH2 )
has been carried out. Starting from the nozzle exit plane, nine sections normal to the
jet axis have been considered, evenly spaced at two equivalent diameters. Along these
planes, the standard deviation of the H 2 mass fraction has been computed together with
its mean value. In ﬁgures 35 –37 the outcomes of the analysis are reported. In all of
the cases, the evolution of the aforementioned parameter σ(YH2)/¯YH2 shows an almost
constant level with a marked reduction along the streamwise direction. This behaviour
might be due to air entertainment phenomena, which will be discussed in a future work.
In the end, a progressive homogenization of the mass distribution is achieved. Having
said that, each section is characterized by a different evolution. The circular section,
which is reported in all the plots as a benchmark, shows the highest level of the
parameter and the slowest tendency to produce a uniform H
2 distribution, coherently
970 A8-24
https://doi.org/10.1017/jfm.2023.603
 Published online by Cambridge University Press

<!-- PDF_PAGE: 25 -->

Gas-dynamic and mixing analysis of under-expanded hydrogen jets
–10
1.0(a)
(b)
(c)
0.8
0.6
0.4
H2 mass fraction
0.2
0
–8 –6 –4 0 –2 2 4 8 61 0
Circular
Elliptical AR 1.5
Rectangular AR 1.5
–10
1.0
0.8
0.6
0.4
H2 mass fraction
0.2
0
–8 –6 –4 0 –2 2 4 861 0
Circular
Elliptical AR 5
Rectangular AR 5
–10
1.0
0.8
0.6
0.4
H2 mass fraction
0.2
0
–8 –6 –4
Radial position (mm)
0–2 24 8 61 0
Circular
Elliptical AR 8
Rectangular AR 8
Figure 34. Hydrogen radial distributions at 10 equivalent diameters from the exit section for the circular,
elliptical and rectangular sections: ( a) AR 1.5 cases,( b) AR 5.0 cases and ( c) AR 8.0 cases.
970 A8-25
https://doi.org/10.1017/jfm.2023.603
 Published online by Cambridge University Press

<!-- PDF_PAGE: 26 -->

G. Anaclerio, T. Capurso and M. Torresi
AR Circular Triangular Star Elliptical Rectangular
— 219 460 238 374 252 046 — —
1.5 — — — 219 731 238 118
5.0 — — — 244 528 264 188
8.0 — — — 266 531 286 428
Table 3. Mean vorticity (s
− 1) computed on the isosurface characterized by a mass fraction of hydrogen equal
to 0.1.
2
1.0
0.8
0.6
0.4
σ(YH2)/Y¯ H2
0.2
0
4 68
Axial position (equivalent diameters)
10 12 14 16 18
Circular
Star
Triangle
Figure 35. Plot of the normalized standard deviation of the H 2 mass fraction distribution along the
streamwise direction for the circular (black), star-shaped (green) and triangular (red) sections.
with the observations previously discussed. In ﬁgure 35 the star-shaped and triangular
jets have been compared. They show a similar behaviour, which might be due to their
close vorticity level, as reported in table 3 . This conﬁrms a correlation between the
vorticity level and the observed mixing. Besides, star-shaped and triangular jets show
a faster homogenization with respect to the circular case. The same analysis has been
performed for the elliptical and rectangular sections. Faster homogenization of the mass
distribution has been observed when increasing the AR for both the elliptical ( ﬁgure 36)
and rectangular ( ﬁgure 37) sections, conﬁrming the enhanced mixing at the higher ARs.
Moreover, as already observed in ﬁgure 32, the circular
and AR 1.5 elliptical sections have
an almost identical inﬂuence over the jet. Indeed, as reported in ﬁgure 37, trends of the
standard deviation are closely overlapped. From a technological point of view, this means
that small deviations of the cross-section from the standard circular one, for example ,
due to uncontrolled manufacturing process or small erosion, do not affect the overall
mixing. On the other hand, narrower shapes (high AR) , as in the case of vessel fractures ,
considerably alter the hydrogen distribution in the proximity of the leakage. Eventually, the
star-shaped and triangular sections show a similar trend as for the elliptical and rectangular
sections with AR = 1.5. This analysis corroborates once more the correlation between the
vorticity level and the hydrogen spreading. In the future new injectors will be investigated
trying to control (limiting or enhancing) the level of ﬂow vorticityand, hence, the evolution
of hydrogen spreading.
970 A8-26
https://doi.org/10.1017/jfm.2023.603
 Published online by Cambridge University Press

<!-- PDF_PAGE: 27 -->

Gas-dynamic and mixing analysis of under-expanded hydrogen jets
2
1.0
0.8
0.6
0.4
0.2
0
4 68
Axial position (equivalent diameters)
10 12 14 16 18
Circular
Elliptical AR 1.5
Elliptical AR 5.0
Elliptical AR 8.0
σ(YH2)/Y¯ H2
Figure 36. Plot of the normalized standard deviation of the H 2 mass fraction distribution along the
streamwise direction for the circular (black) and elliptical (orange) sections.
2
1.0
0.8
0.6
0.4
0.2
0
4 68
Axial position (equivalent diameters)
10 12 14 16 18
Circular
Rectangular AR 1.5
Rectangular AR 5.0
Rectangular AR 8.0
σ(YH2)/Y¯ H2
Figure 37. Plot of the normalized standard deviation of the H 2 mass fraction distribution along the
streamwise direction for the circular (black) and rectangular (blue) sections.
5. Conclusions
In this work, H 2 under-expanded jets have been characterized by means of computational
ﬂuid dynamics simulations, whose numerical model has been validated against the
experimental data provided by Hecht et al. (2015) and Ruggles & Ekoto ( 2014).
Attention has been paid to the inﬂuence of the nozzle cross-section shape on the
gas-dynamic structure of the jets. To such an extent, non-conventional sections like the
triangular and star-shaped sections have been examined. In this way, the effect of convex
and concave angles on the Prandlt–Mayer fans released at the exit section lips have
been assessed. Convex angles have been found to step up the interaction between the
970 A8-27
https://doi.org/10.1017/jfm.2023.603
 Published online by Cambridge University Press

<!-- PDF_PAGE: 28 -->

G. Anaclerio, T. Capurso and M. Torresi
fans, resulting in the formation of over-expanded regions immediately downstream of
the exit section. Differently, no pressure drop has been observed in the proximity of the
concave vertices, suggesting the absence of the fans superposition. The over-expansion
condition quickly promotes the onset of re-compression shock waves, which become
evident immediately downstream of the exit section. This trend can be appreciated in
the symmetry plane of the triangular section as well as in the symmetry plane of the
star-shaped section passing through the convex vertices. For this section, the delayed
formation of the barrel shock along the symmetry plane passing through the concave
angles conﬁrms the absence of the fans interaction. Elliptical and rectangular sections
with different ARs have been studied too. In the elliptical jet characterized by an AR
of 1.5, the coalescence of the weak compression waves depends on the local curvature
of the section proﬁle. Along the major axis plane, the higher curvature promotes the
formation of the barrel shock, whose onset is quicker with respect to the minor axis
plane. At the higher ARs, over-expansion is found along the major axis plane, which
leads to the development of re-compression shock waves as observed in all the rectangular
sections. The corner shock waves interact laterally through a Mach reﬂection, and along
the streamwise direction causing a strong Mach disk. The simple correlation proposed by
the literature to predict the position of the Mach disk in circular jets has been modiﬁed
for the rectangular and elliptical sections, introducing a corrective factor
that, for a ﬁxed
NPR, linearly depends on the AR. An explanation for the drift of the Mach disk towards
the nozzle exit section for increasing ARs has been proposed, based on geometrical
considerations regarding the expansion fans propagating from the nozzle lips. Indeed, as
the AR increases, stronger over-expansions have been observed, which ultimately lead to
higher inclinations of the re-compression shocks with a consequent shift of their reﬂection
along the axis. The growth of the jet boundaries has been reported in Schlieren pictures
normal to the jet axis. Generally, a faster growth has been noted along the minor axis
planes in both the rectangular and elliptical nozzles. In the AR 1.5 elliptical
case the axis
switching has been observed, whereas the AR 1.5 rectangular jet reaches a symmetrical
shape at 3 mm from the nozzle exit section. In the triangular case the different growth
rates along the perimeter lead to a 180 ◦ rotation of the jet boundary with respect to the
nozzle exit section. A 45◦ rotation has been found in the star section case. In all the cases,
the quicker growth is observed in regions characterized by higher levels of the vorticity
magnitude, which correspond to the closest points to the shape centre. Therefore, the
higher vorticity can be attributed to the more intense velocity gradients. All the sections
show different mass fraction decay rates and, consequently, different levels in the intensity
of the radial mixing. In particular, for the rectangular and elliptical sections, a clear trend
between the AR and the axial decay rate has been observed. For the lower AR, penetration
is higher, while higher AR shapes promote a greater radial mixing. Thus, elliptical and
rectangular injectors with a lower AR could be employed when a fast homogenization of
the mixture inside the ICE cylinder is required. Conversely, a higher AR injector could be
a suitable design solution when an axial stratiﬁcation of the charge is desired.
Funding. This work was partly supported by the Italian Ministry of University and Research under the
Programme ‘Department of Excellence’ Legge 232/2016 (grant no. CUP - D93C23000100001) and partly
supported under the National Recovery and Resilience Plan (NRRP), mission 4 component 2 investment
1.3 - call for tender no. 1561 of 11.10.2022 of Ministero dell’Università e della Ricerca (MUR); funded by
the European Union – NextGenerationEU. Project code PE0000021, concession decree no. 1561 of 11.10.2022
adopted by Ministero dell’Università e della Ricerca (MUR), CUP - D93C22000900001, project title ‘Network
4 Energy Sustainable Transition – NEST.’
Declaration of interests. The authors report no conﬂict of interest.
970 A8-28
https://doi.org/10.1017/jfm.2023.603
 Published online by Cambridge University Press

<!-- PDF_PAGE: 29 -->

Gas-dynamic and mixing analysis of under-expanded hydrogen jets
Author ORCIDs.
Giuseppe Anaclerio https://orcid.org/0000-0003-2637-4302 .
REFERENCES
ABBETT , M. 1971 Mach disk in underexpanded exhaust plumes. AIAA J. 9 (3), 512–514.
ADAMSON ,T . C .&N ICHOLLS , J.A. 1959 On the structure of jets from highly underexpanded nozzles into
still air. J. Aerosp. Sci. 26 (1), 16–24.
ADDY, A.L. 1981 Effects of axisymmetric sonic nozzle geometry on Mach disk characteristics. AIAA J. 19
(1), 121–122.
ANACLERIO ,G . ,C APURSO ,T . ,T ORRESI ,M .&C AMPOREALE , S.M. 2023 Numerical characterization of
hydrogen under-expanded jets with a focus on internal combustion engines applications. Intl J. Engine Res.
doi:10.1177/14680874221148789.
ASHKENAS ,H .&S HERMAN , F.S. 1964 The structure and utilization of supersonic free jets in low density
wind tunnels. Proceedings of the 4th International Symposium on Rareﬁed Gas Dynamics , vol. 2(7),
pp. 84–105. Academic Press.
BONELLI ,F . ,V IGGIANO ,A .&M AGI , V. 2013 A numerical analysis of hydrogen underexpanded jets under
real gas assumption. Trans. ASME J. Fluids Engng 135 (12), 121101.
BOYNTON , F.P. 1967 Highly underexpanded jet structure - exact and approximate calculations. AIAA J. 5 (9),
1703–1704.
CAPURSO ,T . ,S TEFANIZZI ,M . ,T ORRESI ,M .&C AMPOREALE , S.M. 2022 Perspective of the role of
hydrogen in the 21st century energy transition. Energy Convers. Manag. 251, 114898.
CHAUHAN ,V . ,K UMAR , S.M.A. & R ATHAKRISHNAN , E. 2016 Aspect ratio effect on elliptical sonic jet
mixing. Aeronaut. J. 120 (1230), 1197–1214.
CRIST ,S . ,G LASS ,D . R .&S HERMAN , P.M. 1966 Study of the highly underexpanded sonic jet. AIAA J. 4 (1),
68–71.
DENNER , F. 2018 Fully-coupled pressure-based algorithm for compressible ﬂows: linearisation and iterative
solution strategies. Comput. Fluids 175, 53–65.
FRANQUET , E., P ERRIER ,V . ,G IBOUT ,S .&B RUEL , P. 2015 Free underexpanded jets in a quiescent medium:
ar e v i e w .Prog. Aerosp. Sci. 77, 25–53.
GAHLEITNER , G. 2013 Hydrogen from renewable electricity: an international review of power-to-gas pilot
plants for stationary applications. Intl J. Hydrogen Energy 38, 2039–2061.
GRIBBEN , B.J., B ADCOCK ,K . J .&R ICHARDS , B.E. 2000 Numerical study of shock-reﬂection hysteresis in
an underexpanded jet. AIAA J. 38 (2), 275–283.
GRINSTEIN , F.F. 2001 Vortex dynamics and entrainment in rectangular free jets. J. Fluid Mech. 437, 69–101.
HARSTAD ,K .&B ELLAN , J. 2006 Global analysis and parametric dependencies for potential unintended
hydrogen-fuel releases. Combust. Flame 144 (1), 89–102.
HATANAKA ,K .&S AITO , T. 2012 Inﬂuence of nozzle geometry on underexpanded axisymmetric free jet
characteristics. Shock Waves 22 (5), 427–434.
HECHT , E.S., L I,X .&E KOTO , I.W. 2015 Validated equivalent source model for an under-expanded hydrogen
jet. Tech. Rep. SAND2015-3211C. Sandia National Laboratories.
IEA 2020 Renewables 2020 - analysis and forecast to 2050.
I
RIE ,T . ,Y ASUNOBU ,T . ,K ASHIMURA ,H .&S ETOGUCHI , T. 2003 Characteristics of the Mach disk in
the underexpanded jet in which the back pressure continuously changes with time. J. Therm. Sci. 12 (2),
132–137.
KROTHAPALLI ,A . ,B AGANOFF ,D .&K ARAMCHETI , K. 1981 On the mixing of a rectangular jet. J. Fluid
Mech. 107, 201–220.
KUMAR , S.M.A. & R ATHAKRISHNAN , E. 2016 Characteristics of a supersonic elliptic jet. Aeronaut. J.
120 (1225), 495–519.
LEWIS ,C . H .&C ARLSON , D.J. 1964 Normal shock location in underexpanded gas and gas-particle jets. AIAA
J. 2 (4), 776–777.
LOVE , E.S., G RISBY , C.E., L EE , L.P . & W OODLING , M.J. 1959 Experimental and theoretical studies of
axisymmetric free jets. NASA Tech. Rep. NASA-TR-R-6.
LOVELY,D .&H AIMES , R. 1999 Shock detection from computational ﬂuid dynamics results. 14th
Computational Fluid Dynamics Conference.A I A A .
MAKAROV ,D .&M OLKOV, V. 2013 Plane hydrogen jets. Intl J. Hydrogen Energy 38 (19), 8068–8083.
MENON ,N .&S KEWS , B.W. 2005 3-D shock structure in underexpanded supersonic jets from elliptical and
rectangular exits. Shock Waves: Proceedings of the 24th International Symposium on Shock Waves ,v o l .1 .
Springer.
970 A8-29
https://doi.org/10.1017/jfm.2023.603
 Published online by Cambridge University Press

<!-- PDF_PAGE: 30 -->

G. Anaclerio, T. Capurso and M. Torresi
MENON ,N .&S KEWS , B.W. 2010 Shock wave conﬁgurations and ﬂow structures in non-axisymmetric
underexpanded sonic jets. Shock Waves 20, 175–190.
OTOBE ,Y . ,Y ASUNOBU ,T . ,K ASHIMURA ,H . ,M ATSUO ,S . ,S ETOGUCHI ,T .&K IM , H.D. 2009 Hysteretic
phenomenon of underexpanded moist air jet. AIAA J. 47 (12), 2792–2799.
PAO,S . P .&A BDOL -HAMID , K.S. 1996 Numerical simulation of jet aerodynamics using the
three-dimensional Navier–Stokes code PAB3D. NASA Tech. Paper 3596, 158.
RAJAKUPERAN ,E .&R AMASW AMY, M.A. 1977 Computation of the near ﬁeld structure of underexpanded
jets from elliptic sonic nozzle. CFD J. 6 (2), 79–101.
RUGGLES ,A . J .&E KOTO , I.W. 2014 Experimental investigation of nozzle aspect ratio effects on
underexpanded hydrogen jet release characteristics. Intl J. Hydrogen Energy 39 (35), 20331–20338.
SENESH ,K .&B ABU , V. 2012 Numerical simulation of subsonic and supersonic jets. https://arc.aiaa.org/doi/
pdf/10.2514/6.2005-3095.
SFEIR , A.A. 1976 The velocity and temperature ﬁelds of rectangular jets. Intl J. Heat Mass Transfer 19 (11),
1289–1297.
TESHIMA , K. 1994 Structure of supersonic freejets issuing from a rectangular oriﬁce. Prog. Astronaut.
Aeronaut. 158, 375–380.
TIDE ,P . S .&B ABU , V. 2008 A comparison of predictions by SST and Wilcox k-ω models for a Mach 0.9 jet.
https://arc.aiaa.org/doi/pdf/10.2514/6.2008-24.
TRENTACOSTE ,N .&S FORZA , P. 1967 Further experimental results for three- dimensional free jets. AIAA J.
5 (5), 885–891.
VAN DER HEGGE ZIJNEN , B.G. 1958 Measurements of the velocity distribution in a plane turbulent jet of air.
Appl. Sci. Res. A 7 (4), 256–276.
VELIKORODNY ,A .&K UDRIAKOV , S. 2012 Numerical study of the near-ﬁeld of highly underexpanded
turbulent gas jets. Intl J. Hydrogen Energy 37 (22), 17390–17399.
VOUROS , A.P ., P ANIDIS ,T . ,P OLLARD ,A .&S CHW AB, R.R. 2015 Near ﬁeld vorticity distributions from a
sharp-edged rectangular jet. Intl J. Heat Fluid Flow 51, 383–394, theme special issue celebrating the 75th
birthdays of Brian Launder and Kemo Hanjalic.
WALLNER ,T . ,M ATTHIAS , N.S., S CARCELLI ,R .&K WON , J.C. 2013 Evaluation of the efﬁciency and the
drive cycle emissions for a hydrogen direct-injection engine. Proc. Inst. Mech. Engrs D:J 227 (1), 99–109.
WANG ,P . C .&M CGUIRK , J.J. 2013 Large eddy simulation of supersonic jet plumes from rectangular con-di
nozzles. Intl J. Heat Fluid Flow 43, 62–73.
WIMMER ,A . ,W ALLNER ,T . ,R INGLER ,J .&G ERBIG , F. 2005 H 2-direct injection – a highly promising
combustion concept. SAE Tech. Paper 2005-01-0108.
WINTERS ,W . S .&E V ANS, G.H. 2007 Final report for the ASC gas–powder two-phase ﬂow modeling project.
Tech. Rep. SAND2006-7579. Sandia National Laboratories.
YAMANE ,K .2 0 1 8Hydrogen Fueled ice, Successfully Overcoming Challenges Through High Pressure Direct
Injection Technologies: 40 Years of Japanese Hydrogen Ice Research and Development. SAE International.
YIP, H.L., S RNA ,A . ,Y UEN , A.C.Y ., K OOK ,S . ,T AYLOR , R.A., Y EOH , G.H., M EDWELL ,P . R .&
Chan, Q.N. 2019 A review of hydrogen direct injection for internal combustion engines: towards carbon-free
combustion. Appl. Sci. 9 (22), 4842.
Z
AMAN , K.B.M.Q. 1996 Axis switching and spreading of an asymmetric jet: the role of coherent structure
dynamics. J. Fluid Mech. 316, 1–27.
970 A8-30
https://doi.org/10.1017/jfm.2023.603
 Published online by Cambridge University Press
