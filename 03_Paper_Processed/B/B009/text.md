<!-- PDF_PAGE: 1 -->

Large eddy simulation of highly turbulent
under-expanded hydrogen and methane jets for
gaseous-fuelled internal combustion engines
A. Hamzehloo, P.G. Aleiferis *
Department of Mechanical Engineering, University College London, UK
article info
Article history:
Received 19 May 2014
Received in revised form
7 September 2014
Accepted 3 October 2014
Available online 7 November 2014
Keywords:
Hydrogen injection
Under-expanded jets
Mach disk
Internal combustion engines
abstract
Burning hydrogen in conventional internal combustion (IC) engines is associated with zero
carbon-based tailpipe exhaust emissions. In order to obtain high volumetric efﬁciency and
eliminate abnormal combustion modes such as preignition and backﬁre, in-cylinder direct
injection (DI) of hydrogen is considered preferable for a future generation of hydrogen IC
engines. However, hydrogen 's low density requires high injection pressures for fast
hydrogen penetration and sufﬁcient in-cylinder mixing. Such pressures lead to chocked
ﬂow conditions during the injection process which result in the formation of turbulent
under-expanded hydrogen jets. In this context, fundamental understanding of the under-
expansion process and turbulent mixing just after the nozzle exit is necessary for the
successful design of an efﬁcient hydrogen injection system and associated injection
strategies. The current study used large eddy simulation (LES) to investigate the charac-
teristics of hydrogen under-expanded jets with different nozzle pressure ratios (NPR),
namely 8.5, 10, 30 and 70. A test case of methane injection with NPR ¼ 8.5 was also
simulated for direct comparison with the hydrogen jetting under the same NPR. The near-
nozzle shock structure, the geometry of the Mach disk and reﬂected shock angle, as well as
the turbulent shear layer were all captured in very good agreement with data available in
the literature. Direct comparison between hydrogen and methane fuelling showed that the
ratio of the speciﬁc heats had a noticeable effect on the near-nozzle shock structure and
dimensions of the Mach disk. It was observed that with methane, mixing did not occur
before the Mach disk, whereas with hydrogen high levels of momentum exchange and
mixing appeared at the boundary of the intercepting shock. This was believed to be the
effect of the high turbulence ﬂuctuations at the nozzle exit of the hydrogen jet which
triggered Gortler vortices. Generally, the primary mixing was observed to occur after the
location of the Mach disk and particularly close to the jet boundaries where large-scale
turbulence played a dominant role. It was also found that NPR had signiﬁcant effect on
the mixture 's local fuel richness. Finally, it was noted that applying higher injection
pressure did not essentially increase the penetration length of the hydrogen jets and that
there could be an optimum NPR that would introduce more enhanced mixing whilst
* Corresponding author . University College London, Department of Mechanical Engineering, Torrington Place, London WC1E 7JE, UK.
Tel.: þ44 0 20 76793862; fax: þ44 0 20 73880180.
E-mail address: p.aleiferis@ucl.ac.uk (P.G. Aleiferis).
Available online at www.sciencedirect.com
ScienceDirect
journal homepage: www.elsevier.com/locate/he
international journal of hydrogen energy 39 (2014) 21275 e21296
http://dx.doi.org/10.1016/j.ijhydene.2014.10.016
0360-3199/Copyright © 2014, Hydrogen Energy Publications, LLC. Published by Elsevier Ltd. All rights reserved.

<!-- PDF_PAGE: 2 -->

delivering sufﬁcient fuel in less time. Such an optimum NPR could be in the region of 100
based on the geometry and observations of the current study.
Copyright © 2014, Hydrogen Energy Publications, LLC. Published by Elsevier Ltd. All rights
reserved.
Introduction
Hydrogen-fuelled internal combustion engines
In order to tackle issues related to the ever increasing cost of
conventional fuels and carbon emissions, it is necessary to
diversify towards cleaner and more sustainable fuels.
Accordingly, several liquids and gases have been proposed as
alternative fuels for internal combustion (IC) engines; among
them, gaseous hydrogen (H
2) can offer a promising long-term
solution. The concept of a hydrogen economy has been pro-
posed since the mid-1970s [1,2]. Several experimental and
computational studies have been conducted on the develop-
ment of hydrogen-fuelled IC engines in the past 15 years
[3e22]. Port fuel injection (PFI) [6e12] and in-cylinder direct
injection (DI) [13e22] of hydrogen are the two typical options
for hydrogen-fuelled IC engines. DI offers higher volumetric
efﬁciency and eliminates abnormal combustion modes such
as pre-ignition and backﬁre. These attributes, in conjunction
with the ﬂexibility in possible injection strategies, make DI
preferable for hydrogen IC engines. However, hydrogen 's low
density requires high injection pressures in order to achieve
fast fuel delivery and optimise mixture formation. Such
pressures lead to turbulent under-expanded hydrogen jets
past the nozzle exit [18,22]. Therefore, fundamental under-
standing of the under-expansion process and turbulent mix-
ing just after the nozzle exit is necessary for the design of an
efﬁcient hydrogen injection system and associated injection
strategies for enhanced engine performance.
Under-expanded jets
Deﬁnition
The ratio of the nozzle total pressure ( P0) to the ambient (in-
cylinder) static pressure (P∞), namely the nozzle pressure ratio
(NPR), has a signiﬁcant effect on the characteristics of a
gaseous jet issuing from a circular nozzle. Based on the level of
NPR, jets can be classiﬁed as subsonic, moderately under-
expanded and highly under-expanded [23e25]. Speciﬁcally,
Donaldson and Snedeker [25] categorized the gaseous jets into
three major types based on the NPR ( P
0/P∞) and under-
expansion ratio ( P1/P∞) as subsonic (1 > P∞/P0 > 0.528, P1/
P∞ ¼ 1), moderately under-expanded (0.48 > P∞/P0 /C21 0.26,
1.1 < P1/P∞/C20 2) and highly under-expanded (0.26 /C21 P∞/P0 /C21 0,
2 /C20 P1/P∞/C20 ∞). For NPR above ~4 the jet is considered to be
highly under-expanded. As illustrated in Fig. 1 , at such con-
dition, inﬁnite number of Mach waves, namely the
PrandtleMeyer expansion fan, form at the nozzle lip that
spread out to the jet boundary and reﬂect as weak compres-
sion waves which form the intercepting oblique shock that is
ended by a slightly curved strong normal shock so-called Mach
disk [23]. The intercepting shock and the Mach disk form the
ﬁrst shock cell that is labelled “barrel shape shock” since it has
a cylindrical shape. On a 2-D plane a reﬂected shock and a slip
line is seen at the “triple point” which is the merging location
of the intercepting shock and the Mach disk (see Fig. 1 ). The
ﬂow behind the Mach disk is subsonic, whilst the ﬂow behind
the reﬂected shock is still supersonic [23e25]. For higher de-
grees of under-expansion, e.g. NPR z 8, the subsonic core
behind the Mach disk rapidly accelerates and becomes su-
personic once more, which then shapes a second shock cell
that may resemble the ﬁrst shock cell and even include a
normal shock comparable to the Mach disk [25]. At extremely
high levels of NPR, a very large Mach disk forms at the nozzle
exit, with no additional normal shocks downstream, and the
jet then decays resembling a subsonic jet [25].
Near-nozzle sonic characteristics
The near-nozzle sonic characteristics of under-expanded jets
are quantiﬁed by several important parameters that include
the dimensions of the Mach disk, angle of the reﬂected shock
at the triple point and length of the shear layer thickness
(maximum distance between the slip line and the reﬂected
shock). These, not only provide important information
regarding the upstream condition and effective injection
pressure, but also have signiﬁcant effect on the annular shear
layer thickness and consequently on the mixing characteris-
tics of the under-expanded jet. These parameters can also be
used as fundamental measures for comparing under-
expanded jets with different values of NPR and also for vali-
dating numerical models of these types of jets.
Fig. 1 e Schematic of the near-nozzle structure of under-
expanded jets (based on Crist et al. [23]).
international journal of hydrogen energy 39 (2014) 21275 e2129621276

<!-- PDF_PAGE: 3 -->

The Mach disk's dimensions are typically characterised by
the axial distance of the disk from the nozzle exit, i.e. the Mach
disk height ( Hdisk), and the distance between the two triple
points (see Fig. 1) i.e. the Mach disk width (Wdisk). The reﬂected
shock angle and the shear layer thickness are signiﬁcantly
affected by the Mach disk dimensions and although there is
still not a universal relation available for these two parame-
ters, several correlations have been suggested for predicting
H
disk and Wdisk.
By conducting experimental investigations and with the
assumption of choked condition at the nozzle exit ( Ma ¼ 1),
Crist et al. [23] suggested that the relation between NPR and
the Mach disk height can be given by:
Hdisk
D z 1ﬃﬃﬃﬃﬃﬃﬃ
2:4
p /C2
ﬃﬃﬃﬃﬃﬃ
P0
P∞
s
(1)
By assuming a large Mach number at the location of the
Mach disk ( Madisk >> 1) and by combining equation (1) with
some isentropic relations, Crist et al. [23] also derived a cor-
relation which relates Hdisk to Madisk and the ratio of speciﬁc
heats (g) as follows:
Hdisk
D /C24 Ma1=ðg/C0 1Þ
disk
"
g þ 1
4:8g
/C18 g /C0 1
2
/C19 g=g/C0 1
#1=2
(2)
Ewan and Moodie [26] and Antsupov [27] separately sug-
gested the following correlations in order to predict Hdisk and
Wdisk:
Hdisk ¼ 0:77 /C2 D þ 0:068 /C2 D1:35
/C18 P1
P∞
/C19
(3)
Wdisk
D ¼ log
/C18 P1
P∞
/C19 5 =
2
/C0 3
4 (4)
where P1 is the static pressure at the nozzle exit. Velikorodny
and Kudriakov [28] reported that by using theoretical analysis
based on dimensional groups the following relations can be
derived for the Mach disk:
Hdisk
D ¼ 1
2
ﬃﬃﬃgp
ﬃﬃﬃﬃﬃﬃ
P1
P∞
s /C18 g þ 1
g /C0 1
/C19 1 =
4
(5)
Wdisk
D ¼ z Hdisk
D
ﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ
1 /C0 g þ 1
g
g þ 1
g /C0 1
/C18/C19 /C0 1=2
s
(6)
where z is an empirical constant that accounts for the growth
of the mixing layer. A commonly used experimental correla-
tion for the Mach disk height was proposed by Ashkenas and
Sherman [29] as follows:
Hdisk
D ¼ 0:67
ﬃﬃﬃﬃﬃﬃ
P0
P∞
s
(7)
Mixing characteristics
The jet tip penetration ( Ztip) and its volumetric growth ( Vjet)
are two key properties of under-expanded gaseous fuel jets
when it comes to air/fuel mixing. They have direct effects on
the mechanism of mixture preparation and degree of fuel
stratiﬁcation and can inﬂuence in return the combustion
quality and tailpipe emissions level.
The tip penetration of under-expanded jets has been
subject to many theoretical studies. Turner [30] was the ﬁrst
to develop a mathematical model for the under-expanded
gaseous jets. The model approximates the geometry of a
gaseous jet as a spherical head vortex and a quasi-steady jet
region that conveys the momentum; momentum is
constantly supplied thorough the nozzle oriﬁce and is
passed between the quasi-steady region and the head vor-
tex. Hill and Ouellette [31] employed Turner 'sm o d e lt o
develop an analytical relationship for the tip penetration as
follows:
Z
tip ¼ G
/C18 M
r∞
/C19 1 =
4
t
1 =
2
(8)
where M is the momentum ﬂow rate supplied by the nozzle
and G is a scaling constant related to the entrainment level
(normally has a value of ~3 for jets issued from round nozzles).
As dictated by equation (8) and also as formulated by Abraham
[32], the jet penetration under conditions similar to those
prevailing in DI engines (under-expanded with Reynolds
number in order of 10
5) obeys a linear dependency on the
square root of time. However, experiments have shown that
this linear relation is achieved after an initial non-linear
transient behaviour [33].
Literature survey
Experimental studies of the near-nozzle shock structure and
mixing characteristics of under-expanded jets have been
conducted by several researchers using wind tunnel facilities,
Schlieren and shadowgraph photography, Rayleigh scattering,
Laser Doppler Anemometry (LDA) and planar laser-induced
ﬂuorescence (PLIF) in order to measure the mixing parameters
and visualise the near-ﬁeld shock structure of under-
expanded air/nitrogen jets [23,25,26,29,34e37]. Computa-
tional studies of under-expanded jets have been performed
using compressible Euler equations [38e41], Reynolds averaged
NaviereStokes (RANS) and large eddy simulation (LES) meth-
odologies [42e52], mainly for air jets or by assuming the in-
jection of a passive scalar. Early studies were also conducted
by analytical approaches and the method of characteristics
[24,53]. Prudhomme and Haj-Hariri [38] examined moderate
and highly under-expanded jets by solving the axisymmetric
Euler equations with a ﬁnite element solver and Roe's
approximate method [54]. Their implicit computational
framework was able to predict the location of the Mach disk
and the wave structure inside the jet. However, in order to
study the mixing characteristics of under-expanded jets by
including molecular diffusion effects (that can be signiﬁcant
with hydrogen fuelling), use of the NaviereStokes equations is
necessary rather than Euler's equations. RANS simulations are
low in cost and have been proven accurate at capturing the
shock structure of under-expanded jets [42e46], but their
ability to predict the mixing of highly turbulent jets remains
unclear as results can be quite sensitive to the choice of tur-
bulence model. Therefore, LES is considered more suitable for
modelling the details of highly turbulent under-expanded jets
and the following sub-section presents a brief review of rele-
vant studies.
international journal of hydrogen energy 39 (2014) 21275 e21296 21277

<!-- PDF_PAGE: 4 -->

LES modelling
For simulations of under-expanded jets for aerospace appli-
cations where massive attached faces ( e.g. nozzle inner wall)
and complex shear ﬂows exist with strong compressibility at
high temperatures, detached eddy simulation (DES) has been
suggested. DES is based on a hybrid RANS/LES methodology
where RANS is employed at regions close to walls (attached)
and LES for the remaining volume of the domain. This is a
more feasible option to LES since the latter requires consid-
erably ﬁner grid close to the walls [47,48]. However, for con-
ditions relevant to injectors of gaseous-fuelled engines, it has
been shown [49e51] that if the injector body has been included
in the computational domain by assigning a slip wall condi-
tion LES can be used with good level of accuracy (more details
discussed later in the current paper). For example, Dauptain
et al. [49,50] used Smagorinsky LES on an unstructured tetra-
hedral grid with an explicit third-order solver that featured a
centred shock capturing algorithm to study free and
impinging under-expanded jets. Different number of cells was
investigated by these authors and it was found that a grid with
D/20 cell size close to the nozzle exit could provide grid
independency of the results. Recently Vourinen et al. [51]
modelled the injection of a passive scalar with NPR in range
of 4.5 e8.5 using an implicit LES (ILES) technique. The near-
nozzle shock structure and the strong compression effects
were taken into account by using a bulk viscosity model in
conjunction with a second-order ﬁlter that was activated at
the location of the strong shocks. Vourinen et al. [51] also
showed that the Mach disk dimensions and shock structure
were in very good agreement with the experimental obser-
vations of Yu et al. [37,52] that included PLIF visualisation.
Important mixing characteristics, e.g. jet tip penetration and
jet volumetric growth of a passive scalar with nitrogen prop-
erties for NPR /C20 8.5 were also investigated by Vourinen et al.
[51] and a new scaling parameter for the volumetric growth of
under-expanded jets was proposed.
Numerical modelling of hydrogen under-expanded jets
Most previous studies on under-expanded jets have consid-
ered large diameter nozzles with air/nitrogen as the working
gas. There are very limited data in the literature on under-
expanded hydrogen jets (or other light gases such as heli-
um), especially for nozzles with diameters relevant to IC en-
gine injectors. Velikorodny and Kurdriakov [28] studied
computationally under-expanded air and helium jets issued
from a circular nozzle with D ¼ 1 mm and NPR ¼ 30. The nu-
merical methodology employed the Advection Upstream
Splitting Method (AUSM
þ) [55] for the convective ﬂuxes and
direct solution of the governing equations without Sub-Grid
Scale (SGS) turbulence models. It was found that the near-
ﬁeld shock structure of the helium jet required more time
than the air jet to reach quasi-steady conditions. Ruggles and
Ekoto [56] used Schlieren photography to visualise the near
nozzle shock structure and Planar Laser Rayleigh Scatter im-
aging in order to measure the instantaneous mole fraction
downstream of the Mach disk in an under-expanded hydrogen
jet issued from a nozzle with diameter D ¼ 1.5 mm and with
NPR ¼ 10. The Mach disk, the reﬂected shocks and the oblique
shock trains after the Mach disk were clearly captured by the
visualisation technique. Ruggles and Ekoto [56] noticed that
air and hydrogen may have mixed within the slip region and
bypassed the Mach disk, therefore, notional nozzle theories
which assumed that all gas passed the Mach disk were not
accurate enough. It was suggested that more experimental
and computational works were required in order to clarify the
hydrogeneair mixing behaviour very close to the nozzle exit.
Gorle et al. [57] and Gorle and Iaccarino [58] conducted
experimental (Schlieren) and computational (RANS and LES)
studies of under-expanded hydrogen jets from a nozzle with
diameter D ¼ 2 mm and NPR ¼ 30. It was noticed that both
RANS and LES were able to capture the near nozzle shock
structure of under-expanded hydrogen jets in good agreement
with experiments. Khaksarfard et al. [59] investigated
numerically the release of high pressure hydrogen
(10e70 MPa) into ambient through a hole with diameter
D ¼ 5 mm. The Able-Noble real gas Equation of State (EoS) was
used by the latter authors and it was found that for very high
injection pressures the ideal gas equation underestimated the
release velocity; e.g. for injection pressure of 70 MPa the ve-
locity was underestimated by 20%. They concluded that for
injection pressures above 10 MPa a real gas equation must be
used in order to obtain accurate results. Recently Bonelli et al.
[60] used k-ε RANS modelling with a special correction in the
dissipation terms (to account for the so called ‘round-jet
anomaly’) in conjunction with three different EoS, namely
ideal gas, van der Waals , and Redlich-Kwong. They studied high
pressure injection of hydrogen ( P
0 ¼ 75 MPa, T0 ¼ 300 K) into
still nitrogen ( P∞ ¼ 5 MPa, T∞¼300 K) through a nozzle with
inner and outer diameters of 0.3 mm and 0.6 mm, respectively.
These authors noticed that the van der Waals and Redlich-
Kwong EoS predicted lower mass ﬂow rate of hydrogen by 10%
and 8.7%, respectively, than the ideal gas EoS. It was also
found that at very high injection pressures ( P
o >> 10 MPa) the
ideal gas underestimated the Mach disk height and over-
estimated the Mach disk width in comparison to real gas EoS
[60].
Present contribution
Very little computational studies have been conducted on
under-expanded hydrogen jets particularly with respect to
conditions of DI for hydrogen-fuelled IC engines. Previous
computational work by the current authors [22] partially
focused on RANS and LES of under-expanded hydrogen jets
where a stepped-shape nozzle was investigated using a
moderately-ﬁne grid size. The current study aimed to inves-
tigate further the near-nozzle shock structure and mixing
characteristics of highly turbulent under-expanded hydrogen
jets by:
/C15 Conducting LES on a very ﬁne unstructured hexahedral
grid and making direct comparisons between hydrogen
and methane gas injection.
/C15 Studying the effect of increasing NPR on the under-
expansion and mixing characteristics of hydrogen jets.
/C15 Investigating the transient ﬂow development upstream of
the nozzle exit, i.e. inside the nozzle volume of high-
pressure gaseous injectors.
international journal of hydrogen energy 39 (2014) 21275 e2129621278

<!-- PDF_PAGE: 5 -->

/C15 Obtaining a set of reference values for the near nozzle
shock structure, namely the Mach disk height and width,
the reﬂected shock angle, the shear layer thickness and the
length of the ﬁrst subsonic core.
/C15 Quantifying and comparing the jet penetration length and
volumetric growth for hydrogen and methane fuelling.
/C15 Studying the effect of hydrogen 's high diffusivity and low
density on the sonic and mixing characteristics.
Computational methodology
Numerical formulation
The viscous ﬂow of a Newtonian multi-component
compressible ﬂuid of N species ( Y
1, Y2, Y3, … Yi, …, YN)i s
governed by the NaviereStokes equations and species trans-
port equations [61,62]. For N species, N /C0 1 transport equations
are solved; the mass fraction of the Nth component is deter-
mined by the restriction that the total mass fraction must be
unity. Pressure is coupled to density and temperature by the
ideal gas EoS. The STAR-CCM þ code was used for the solution
of the governing equations within the objectives of the current
work. The code beneﬁts from a coupled ﬁnite volume method
that discretises and solves the governing equations simulta-
neously using an implicit time marching approach. To provide
efﬁcient solution a preconditioning matrix is integrated into
the set of equations that consequently requires viscous and
inviscid ﬂuxes to be deﬁned [61]. In the present study in order
to express the inviscid ﬂuxes, the AUSM
þ scheme was applied
because it is believed to be accurate and robust in solving ﬂuid
ﬂows that contain discontinuity such as shock waves [55].
AUSM
þ uses a separate splitting for the pressure terms and
also avoids an explicit artiﬁcial dissipation. AUSMþ discretizes
the ﬂuxes directly as follows:
ff ¼ mþ
i ð1; u; v; …; HÞT
o þ m/C0
i ð1; u; v; …; HÞT
1 þ Pi (9)
where mi is the mass ﬂux across a cell interface, mþ
i is deﬁned
as ( mi þj mij)/2, m/C0
i is deﬁned as ( mi e jmij)/2, and Pi is the
pressure ﬂux. The mass ﬂux and pressure ﬂux are calculated
on the basis of local ﬂow characteristics to ensure precise
information propagation inside the ﬂuid for convective and
acoustic processes. The viscous ﬂuxes can be written in terms
of the stress tensor T which is deﬁned using Boussinesq's
approximation as [61]:
T ¼ T
laminar þ Tturbulent (10)
T ¼ð m þ mtÞ
/C20
VV þ VVT /C0 2
3 ðV$VÞI
/C21
(11)
With LES the governing equations are ﬁltered in such a way
that the turbulence scales greater than the grid resolution are
solved directly and the smaller scales are modelled using SGS
models that deﬁne the turbulent viscosity m
t that is used in
equation (11) to calculate the turbulent stress tensor:
TTurbulent ¼ 2mtS 2
3 ðmtV$V þ rkÞI (12)
where S is the strain rate tensor computed from the resolved
velocity ﬁeld as:
S ¼ 1
2
/C0
VV þ VVT /C1
(13)
Wall-adapting local-eddy viscosity (WALE) sub-grid scale
modelling [63] was applied and mt was approximated by:
mt ¼ rD2Sw (14)
where D is the length scale or grid ﬁlter width and Sw is the
deformation parameter that is a function of the strain rate
tensor [63]. It should be noted that the current computational
framework was second-order accurate for both temporal and
spatial discretization.
The molecular diffusivity was deﬁned as the binary diffu-
sivity of an air ehydrogen (or air emethane) system and was
calculated using the ChapmaneEnskong theory for gaseous
diffusion coefﬁcients as follows [64]:
D
i ¼
1:86 /C2 10/C0 3T
3 =
2
/C18
1=M1
þ 1=M2
/C19 1 =
2
Patms2
12U (15)
where Di is the coefﬁcient of molecular diffusivity, T is the
absolute temperature in K, Patm is the pressure in atm, M1 and
M2 are the molecular weights, and Di is in cm 2/s. The quanti-
ties s12 and U are molecular properties; s12 is the collision
diameter, given in angstroms, which is the arithmetic average
of the two species [64]:
s
12 ¼ 0:5ðs1 þ s2Þ (16)
Values ofs1 and s2 can be found in Ref.[65]. The values of the
dimensionless quantity U depend on an integration of the
interaction between the two species which can be described by
the Lennard-Jones 12-6 potential and is usually of order unity
[64,65].
Simulation setup
The simulations were performed by considering a system that
consisted of a high pressure hydrogen tank and a low pressure
air-containing chamber that were linked by a converging
nozzle with exit diameter D ¼ 1.5 mm, as shown in Fig. 2 .
Overall ﬁve simulations were carried out: four were based on
hydrogen injection with four different values of NPR, namely
8.5,10, 30, 70, and one simulation of methane injection with
NPR ¼ 8.5. The low-pressure chamber was kept for all simu-
lations at 98.37 kPa, whereas the temperature of both the high
pressure tank and the low pressure chamber was kept at
295.4 K and 296 K, respectively. The top boundary of the high
pressure tank was considered a stagnation inlet in order to
maintain the injection pressure, while the side and the bottom
boundaries of the low pressure air-containing chamber were
set to pressure outlet.
The mechanics of ﬂow in small size devices may differ
from those in large scale machines. Therefore, as categorized
by Gad-el-Hak [66], various conﬁgurations of the governing
equations and boundary conditions should be applied
depending on the regime of the Knudsen number (Kn):
Kn ¼
l
L ¼
ﬃﬃﬃﬃﬃﬃ ﬃpg
2
r Ma
Re (17)
international journal of hydrogen energy 39 (2014) 21275 e21296 21279

<!-- PDF_PAGE: 6 -->

where l is the mean free path of gas molecules, L is a char-
acteristic length and the Reynolds number Re can be deﬁned as
Re ¼ UL/n. For laminar boundary layer ﬂows through tiny
ducts, Gad-el-Hak [66] showed that, since d=L /C24 l=
ﬃﬃﬃﬃﬃ ﬃ
Re
p
(where
d is the boundary layer thickness), the Knudsen number is
directly related to the Mach number and inversely related to
the square root of the Reynolds number and can be written as:
Kn /C24 Maﬃﬃﬃﬃﬃ ﬃ
Re
p (18)
Since for turbulent ﬂows it is possible to write d/L ~ 1/(Re)0.2,
it can be concluded that according to (18) Kn ~ Ma/(Re)0.2. In the
current study Re inside the nozzle volume ranged from 10 5 to
106, therefore Kn number was of the order of 10 /C0 2e10/C0 1. Ac-
cording to [66] if 10 /C0 3 /C20 Kn /C20 10/C0 1 then slip boundary condi-
tions should be used on the walls. A slip boundary with
adiabatic condition has been applied in previous studies of
different researchers [49e51], hence the nozzle boundary was
set to adiabatic slip in the current work. In order to avoid the
formation of any artiﬁcial boundary layers and to eliminate
the need of considerably ﬁner grid, the wall boundaries of the
high pressure hydrogen tank were also considered to be of
adiabatic slip type [49e51].
An unstructured hexahedral grid was created by means of
the trimmer facility of STAR-CCM þ that produces cubic cells
with identical size in all directions. As it can be seen in Fig. 2,a
conical reﬁned area was implemented within the computa-
tional grid that covered the nozzle volume and a length of 20 D
downstream of the nozzle exit. The use of such reﬁnement
was necessary to capture the ﬂow details inside the nozzle,
the shock structure very close to the nozzle exit and the
mixing process downstream of the nozzle. The reﬁned area
very close to the nozzle exit (within a distance of ~6.7 D) and
inside the nozzle volume had a cell size of ~0.03 mm ( D/50),
whereas further downstream it had a cell size of ~0.06 mm.
The cell size expanded from the reﬁned area towards the
largest cell size inside the rest of the domain (1.0 mm) through
a four level grid expansion. A total of ~13.5 million cells
occupied the computational domain. The grid resolution used
in the current study was selected to be as dense as possible
according to computational data on under-expanded jets
available in the literature [48e52] and also based on the
computational power available to the authors. Coarser grids
(with D/40 and D/30 uniform cell sizing) were also examined
and the current grid was found to be able to capture near-
nozzle sonic characteristics in very good agreement with
experimental data (as will be discussed later). Moreover, it
should be noted that the grid used in the current work had
uniform cell size within the reﬁnement areas (unlike most
studies available in the literature) in order to eliminate prob-
lems that may occur due to the LES ﬁltering process on non-
uniform grids.
The simulations started from a rest condition where it was
assumed that hydrogen occupied the entire high pressure
tank and a small part of the converging nozzle volume up to
~1.4D upstream the nozzle exit. Air occupied the low pressure
chamber and remaining of the nozzle volume. The length of
the high pressure hydrogen tank was believed to be long
enough (40D) so that the ﬂow could be considered to be almost
at rest at the stagnation inlet within the injection duration.
This assumption eliminated the need for applying any initial
perturbation at the inlet boundary for LES studies.
The molecular diffusivity was calculated using equation
(15) and values of D
i z 7.94 /C2 10/C0 5 m2/s and Di z 2.1 /C2 10/C0 5 m2/
s were obtained for air ehydrogen and air emethane systems,
respectively. The dynamic viscosity ( m) in equation (11) was
calculated using Sutherland's law as follows:
m ¼ ms
Ts þ Cs
T þ Cs
/C18 T
Ts
/C19 3 =
2
(19)
where ms and Ts are reference viscosity and reference tem-
perature values, respectively, and Cs is the Sutherland's con-
stant; those values have been tabulated in Table 1 for air,
hydrogen and methane. For the mixture viscosity, either
mass-weighted mixing or volume-weighted mixing methods
can be used. Both methods were examined and similar results
achieved. However, since for non-ideal gas mixtures a
volume-weighted approach is suggested as good practice by
the code developers, a volume-weighted mixing methodology
was ﬁnally selected in the current work to allow direct com-
parison between the ideal gas results obtained here and non-
ideal gas studies to be conducted in the future.
Table 1 e Sutherland's constants for different gases.
Gas ms [kg/ms] Ts [K] Cs [K]
Air 1.827 /C2 10/C0 5 291.15 120
H2 8.76 /C2 10/C0 6 293.85 72
CH4 1.201 /C2 10/C0 5 273.15 197.8
Fig. 2 e Left: Grid and domain dimensions. Right-top:
Close-up view of reﬁned areas. Right-bottom: Nozzle
proﬁle and dimensions based on Ref. [56].
international journal of hydrogen energy 39 (2014) 21275 e2129621280

<!-- PDF_PAGE: 7 -->

Due
to the
high ve-
locity in
the
near-
ﬁeld of
the
under-
expanded jets, the integral time scale of the ﬂow could be
deﬁned as t
0 ¼ D/2U1 [51]. Assuming chocked condition at the
nozzle exit ( Ma ¼ 1), U1 would be that of the speed of sound
which, with the ideal gas assumption, was calculated as:
U1 ¼ a ¼
ﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ
gRT1
p
(20)
where the temperature at the nozzle exit ( T1) was deﬁned as
[53]:
T1 ¼ T0
1 þ g/C0 1
2 Ma2 (21)
Using equations (20) and (21) with Ma ¼ 1 at the nozzle exit,
the nominal integral time scale for hydrogen ( g z 1.41,
R z 4124 J/kg K) and methane ( g z 1.32, R z 518 J/kg K) jets
was calculated to be t0 z 6.2 /C2 10/C0 7 s and t0 z 1.8 /C2 10/C0 6 s,
respectively. A time-step of 5.0 /C2 10/C0 9 s was used at the
beginning of the simulations to build up the initial pressure
gradient inside the nozzle volume smoothly, which was then
increased to 5.0 /C2 10
/C0 8 s and 1.0 /C2 10/C0 7 s (for the rest of the
simulation time) for hydrogen and methane, respectively.
These values were almost 10 times smaller than the nominal
integral time scale of the ﬂows and were considered adequate
to capture the turbulent temporal ﬂuctuations within feasible
CPU times. A comparison between the settings of the current
work and those of a selection of previous numerical studies of
under-expanded jets is presented in Table 2 for direct com-
parison and completeness.
Results and discussion
Model validation
The current computational framework was validated against
two experimental and numerical test cases available in the
literature. First a computational test case was set up based on
the experimental work of Ruggles and Ekoto [56]; in this
model, hydrogen was injected with NPR ¼ 10 using the
converging nozzle conﬁguration shown earlier in Fig. 2. Fig. 3
compares the current LES results with the mean Schlieren
images of Ruggles and Ekoto [56]. The LES image in Fig. 3 was
Table 2 e Parameters of current study in comparison to previous numerical studies of under-expanded jets.
Authors Year Flow type Gas NPR D [mm] Method Grid type Reﬁned area
Dauptain et al. [49,50] 2010 &
2012
Free &
Impinging Jets
Air ~4 25.4 LES ( Smagorinsky) Unstructured tetrahedral D/35
Khaksarfard et al. [59] 2010 Free Jet H 2 100e700 5.0 Inviscid Euler
equations
Unstructured tetrahedral e
Gorl/C19e et al. [57,58] 2011 Free & Cross
Flow Jets
H2 30 2.0 RANS ( k-u) &
LES (WENO)
Unstructured hexahedral D/100 stretched to D/25
Velikorodny &
Kudriakov [28]
2012 Free Jet He & Air 30 1.0 Monotonically
integrated LES
Structured hexahedral D/36
Chin et al. [46] 2013 Free &
Impinging Jets
Air ~1.95, ~3.6 4.0 RANS ( k-ε, k-u-SST) Structured hexahedral Radial: D/200 stretched to
D/2, Axial: D/20 to D/2.5
Vuorinen et al. [51] 2013 Free Jet Passive
scalar (N 2)
4.5, 5.5, 6.5,
7.5, 8.5
1.4 Implicit LES with
bulk viscosity
Structured hexahedral D/70 Radial & D/35 Axial
Bonelli et al. [60] 2013 Free Jet H 2 15 0.3 RANS ( k-ε) with TVD Structured hexahedral D/30
Current study 2014 Free Jet H 2 & CH4 8.5, 10, 30, 70 1.5 LES (WALE) with AUSM þ Unstructured hexahedral D/50 all directions
Fig. 3 e Near-nozzle shock structure. Left: Schlieren [56].
Right: Current LES study.
international journal of hydrogen energy 39 (2014) 21275 e21296 21281

<!-- PDF_PAGE: 8 -->

produced by time-averaging the magnitude of the density
gradient ( jVrj) in ~1.6 t0 intervals (50 samples) starting from
t z 403t0. A grey scale legend was used in order to offer better
visualisation of the near-ﬁeld shock structures. It is clear that
the Mach disk height and width, as well as the reﬂected shock
angle, were predicted in very close agreement with the
Schlieren visualisation. Speciﬁcally, according to Ruggles and
Ekoto [56] the Mach disk height and width were
H
disk ¼ 3.05 mm and Wdisk ¼ 1.30 mm, respectively, whereas
the current LES study predicted higher values by just 1.3% and
3.0%, i.e. H
disk ¼ 3.09 mm and Wdisk ¼ 1.34 mm, respectively.
Similarly to the experiments of [56], the current LES study
showed that the reﬂected shock (at the triple point) was in-
clined at ~28
/C14 to the nozzle axis; the slip lines were also pre-
dicted in good agreement with the experiments. LES also
showed that hydrogen and air are mixing outside the
boundaries of the barrel-shape shock which means that not
all the hydrogen passed through the Mach disk; this conﬁrmed
the observations of [56].
Fig. 4 compares the time-averaged and instantaneous (at
t z 484t
0) values of jVrj predicted by LES against the Root Mean
Square (RMS) Schlieren image of the hydrogen jet of Ruggles
and Ekoto [56]. The RMS image was speciﬁcally selected in
order to highlight the ﬂow gradient and mixing layers of the
Schlieren visualisation, therefore, the time-averaged data of
the density gradient (LES) can be safely compared against it.
The jet width was predicted in satisfactory agreement with
the experiments, albeit slightly narrower by about 2 e3% than
in the Schlieren image. This can be considered an effect of
higher level of turbulence at the nozzle exit in the experi-
mental work than in the LES study, e.g. due to the nozzle
surface roughness, back pressure ﬂuctuation, etc. The
instantaneous snapshot of the density gradient in Fig. 4 shows
a noticeable level of momentum exchange at the jet boundary
before the Mach disk which represents the previously
mentioned hydrogen eair mixing. In Fig. 4 , the red dashed
lines separate two regions with different brightness in the
RMS Schlieren image. This brightness difference was noted by
Ruggles and Ekoto [56] where variations in mixture fraction
and/or changes in pressure and temperature were suggested
as the possible reasons for this to occur. The current LES study
veriﬁed that the region between the dashed lines in fact had a
considerable density gradient that can be interpreted as a high
degree of hydrogen eair mixing. This mixing region was
slightly wider in LES than shown by the experiment.
Two more LES test cases of methane and hydrogen, using
NPR ¼ 8.5, were also set up and run in order to make an
informed analysis against the LES work of Vuorinen et al. [51]
(see Table 2 for further speciﬁcations). Although the type of
gas, nozzle diameter and conﬁguration used in the current
study were different from those of [51], using the same NPR of
8.5 provided the opportunity to perform direct comparison of
the near-nozzle shock structure characteristics. Vuorinen
et al. [51] reported that the Mach disk height of their under-
expanded nitrogen jet was H
disk ¼ 1.84D, whereas in the cur-
rent study a Mach disk height of Hdisk ¼ 1.85D and Hdisk ¼ 1.90D
was obtained for hydrogen and methane jets, respectively.
According to equations (2) and (5) , the Mach disk height is
related to the ratio of speciﬁc heats, hence, considering that
hydrogen and nitrogen have very similar values of g (1.41 and
1.40, respectively), the predicted similarity of the Mach disk
height for these two jets is noteworthy.
For under-expanded jets Ouellette and Hill [67] proposed a
scaling relation for the jet tip penetration Z
t and the ratio of
the upstream stagnation density to the ambient density r0/r∞
as Ztip/(r0/r∞)1/4 ~ t1/2. Based on this, Vuorinen et al. [51]
Fig. 4 e (a and b): Comparison between the time-averaged density gradient ( jVrj) of the current LES study (right) and RMS
Schlieren image of [56] (right). (c) Instantaneous LES snapshot of jVrj.
international journal of hydrogen energy 39 (2014) 21275 e2129621282

<!-- PDF_PAGE: 9 -->

suggested a new scaling relation for the jet volume Vjet as Vjet/
(r0/r∞)3/4 ~ t3/2. Figs. 5 and 6 show the tip penetration and
volumetric growth for the different under-expanded jets of
the current study based on those scaling parameters. Specif-
ically, Fig. 5 illustrates that using the scaling expression of
Ouellette and Hill [67] collapsed the penetration lines onto
almost a single line for hydrogen and methane with NPR ¼ 8.5
and hydrogen with NPR ¼ 10. The respective data of the
hydrogen jets with NPR ¼ 30 and 70 are also plotted in Fig. 5
and will be discussed later in this paper. Fig. 6 shows that
the scaling expression of Vuorinen et al. [51] resulted in
volumetric growth lines that have collapsed onto a single line
for the hydrogen jets with NPR ¼ 8.5 and 10. However, the
methane jet with NPR ¼ 8.5 did not show a collapsed behav-
iour onto the same line to that of hydrogen. This can be a
result of the much higher diffusivity of hydrogen in compar-
ison to that of methane which can produce a considerably
bulkier jet for hydrogen.
Transient in-nozzle ﬂow and jet development
The current section investigates the transient formation of
under-expanded jets in addition to the in-nozzle ﬂow devel-
opment within the early stages of injection. Initial transient
stages of the near-nozzle shock expansion, Mach disk forma-
tion and jet development of the under-expanded hydrogen
and methane jets are presented in Fig. 7 . Transient develop-
ment of the in-nozzle (and within a short distance from the
nozzle exit) axial Mach number for the hydrogen jet with
NPR ¼ 10 is also shown in Fig. 8. The shock development and
transient jet formation follow very similar trends for the
hydrogen jets with NPR ¼ 8.5 and 10 in Fig. 7 .A t t z 13t
0 the
PrandtleMeyer expansion fans resulted in formation of a
spherically propagating bow shock, followed by the growth of
the ﬁrst oblique shocks. According to Fig. 8 , during t /C20 11t
0
(t /C20 6.8 /C2 10/C0 3 ms), the issuing jet was subsonic and then at
t z 13t0 (t z 8.1 ms) the ﬂow accelerated and reached Ma ¼ 1a t
the nozzle exit. Soon after that at t z 21t0 (t ¼ 13 ms), when the
nozzle exit pressure P1 reached the threshold of the under-
expansion, i.e. P 1/P∞ > 2, a very small normal shock with
narrowly spaced slip lines formed close to the nozzle exit (see
Fig. 7 ). This small normal shock can be assumed as the ﬁrst
appearance of the Mach disk. As it can be seen in Fig. 8, during
this time, the ﬂow reached Ma ¼ 1 upstream the nozzle exit
(within the nozzle); the ﬂow accelerated to Ma ¼ 1.02 at the
nozzle exit. At t z 23t
0 (t z 14.2 ms) a sudden rise occurred in
the in-nozzle Mach number. Speciﬁcally, it reached Ma z 1.1
and this was followed by a weak shock which caused the ﬂow
to decelerate and reach a value of Ma z 0.98. The ﬂow then
accelerated again and reached a value of Ma ¼ 1.01 at the
nozzle exit. After this point, Fig. 7 shows that as time passed,
the distance between slip lines grew and the width of the Mach
disk increased. Fig. 8 shows that the position of Ma ¼ 1 moved
backwards upstream and was associated with an increase in
the size of the Mach disk. As time passed, the position of
Ma z 1 moved further backwards; the Mach number inside the
nozzle increased and the intensity of the inner nozzle shock
was ampliﬁed (see Fig. 8 ). When the Mach disk and shock
structure close to the nozzle exit reached semi-steady condi-
tions ( t z 80t
0 or t z 49.6 ms), Ma ¼ 1 occurred about 0.5 D
upstream the nozzle exit. A maximum Mach number of
Ma z 1.3 occurred at about 0.2 D upstream of the nozzle exit.
From the time that the location of Ma ¼ 1 started to occur
inside the nozzle, it was noticed that the Mach number at the
nozzle exit ranged from 1.01 at the beginning of the Mach disk
formation to about 1.1 when the Mach disk dimensions had
reached semi-steady conditions.
The observed development of the hydrogen jets with
NPR ¼ 8.5 and 10 is in good agreement with the stages of shock
development presented by Vuorinen et al. [51]. During the
transient process it was noticed that the height and width of
the Mach disk temporarily reached a higher value than their
ﬁnal steady state values. This can be seen for hydrogen jets in
Fig. 7 at t z 32t
0 (t ¼ 20 ms) and at t z 38t0 (t ¼ 25 ms) with NPR of
10 and 8.5, respectively.
Fig. 5 e Scaled jet tip penetration versus normalized time.
Fig. 6 e Scaled jet volumetric growth versus normalized
time.
international journal of hydrogen energy 39 (2014) 21275 e21296 21283

<!-- PDF_PAGE: 10 -->

The transient development of the methane jet with
NPR ¼ 8.5 showed slightly different pattern to what was
observed for hydrogen 's jets with NPR ¼ 8.5 and 10. In
particular, as shown in Fig. 7 , the methane jet contained
strong expansion fans from the very beginning of its forma-
tion which resulted in the formation of a normal shock wider
than the nozzle diameter very similar to a Mach disk. The
distance of this normal shock from the nozzle exit increased
quickly and at t z 10t
0 (t ¼ 18 ms) the shock can be considered
as a Mach disk which in conjunction with the intercepting
shock form the ﬁrst shock cell (barrel-shape shock). The di-
mensions of the barrel-shape shock were greater upon for-
mation than the ﬁnal steady values in the same way to what
was observed earlier for the hydrogen jets. The existence of
the wide Mach disk in the methane jet from the very beginning
resulted in the development of widely-spaced slip lines, wider
than those of the hydrogen jets where a slimmer Mach disk
was formed initially.
Two test cases of hydrogen with NPR ¼ 30 and 70 were also
studied. The transient formation of the hydrogen jet with
NPR ¼ 30 is also presented in Fig. 7 . Due to the high NPR and
strong compression fans the transient formation of the near-
nozzle shock structure in this jet was very similar to what was
described for the methane jet, speciﬁcally the formation of a
wide Mach disk (normal shock) from very begging with widely-
spaced slip lines. The hydrogen jet with NPR ¼ 70 showed a
similar transient behaviour to that of NPR ¼ 30. It is clear form
Fig. 7 that NPR had a considerable effect on the dimensions
and shape of the Mach disk. It was observed that higher NPR
produced more convex Mach disk. The propagation of a bow
shock in front of the under-expanded jets can be seen in Fig. 7
for all test cases.
The in-nozzle transient process described earlier for the
hydrogen jet with NPR ¼ 10 (see Fig. 8 ) was observed for all
under-expanded methane and hydrogen jets of the current
study. For a compressible methane ﬂow in a macro-scale large-
neck Laval nozzle of 2.4 cm throat diameter, Abdi et al. [68]
studied the centreline Mach number and found that the
choked condition of Ma ¼ 1 occurred at the beginning of the
constant area neck just after the converging area. They also
noticed that the ﬂow accelerated within the constant area
throat and reachedMa z 1.35; then it started oscillating around
Ma z 1.2 until it reached the exit plane of the constant area
section (and beginning of the diffuser section). In contrast, the
nozzle of the present study is categorized as a micro-nozzle
and different ﬂow behaviour is expected in comparison to
larger scale counterparts [69e72]. For instance, in a micro-size
convergentedivergent nozzle Hao et al. [72] noticed that, by
scaling down the nozzle size, the Mach number at the throat
and the nozzle exit decreased and the choked condition moved
away from the throat towards the exit. The nozzle used in the
current study had two sections, a converging part and a con-
stant area section with length of 0.6 D (Fig. 2 ). As mentioned
earlier, for all jets of the current study at semi-steady condi-
tions, Ma ¼ 1 occurred at about 0.1 D downstream of the
beginning of the constant area section. This can be explained
by high compressibility effects [70] and high viscosity dissi-
pation due to increased surface-to-volume ratio [72]. Just after
the sonic line, expansion fans started forming and caused the
ﬂow to accelerate and reach a maximumMach
number of about
1.3 at about 0.2 D upstream of the nozzle exit where the re-
ﬂected fans (from the nozzle wall) produced normal-shape
shock which changed the ﬂow condition to subsonic. After
this point, the ﬂow accelerated again through the re-reﬂected
expansion fans and exited the nozzle with Ma z 1.1. A Mach
number higher that unity at the nozzle exit, Ma z 1.2, was also
observed in a study of Khaksarfard et al. [59] where hydrogen
Fig. 7 e Development of under-expanded jet and near-
nozzle shock structure. (a): Methane NPR ¼ 8.5, (b):
Hydrogen NPR ¼ 8.5, (c): Hydrogen NPR ¼ 10, (d): Hydrogen
NPR ¼ 30.
international journal of hydrogen energy 39 (2014) 21275 e2129621284

<!-- PDF_PAGE: 11 -->

was injected with P0 ¼ 34.5 MPa into atmospheric ambient.
However, in their work the presented injection duration was
not long enough (25 ms) to show the Mach number peak and the
transient in-nozzle ﬂow in the same way that was captured in
the current study. In another study, where high pressure ﬂow
of nitrogen through an ejector device (vacuum jet) was inves-
tigated [73], the in-nozzle Mach number showed similar vari-
ations to those of the current study, as well as an exit Mach
number higher than unity. Certainly further work is required in
order to study in detail the characteristics of the transient in-
nozzle compressible ﬂow in tiny-sized nozzles. The effects of
nozzle design and its dimensions form a part of work in
progress by the current authors and will be discussed in a
future publication.
Near-nozzle shock structure
Instantaneous snapshots of both methane and hydrogen jets
with NPR ¼ 8.5 are shown in Fig. 9 . The grey-scaling corre-
sponds to density gradients as discussed earlier. Fig. 9 also
shows a close-up view of the near-nozzle shock structure of
both jets at a semi-steady condition. The PrandtleMeyer
expansion fans, barrel-shape shock, Mach disk dimensions, as
well as angle of reﬂected shock, triple points and slip lines,
were all captured in very good agreement with the classic
deﬁnition of an under-expanded jet [23e26] and also with
computational results [49e51] and experimental visual-
isations [37] presented by other authors. Fig. 9 also illustrates
how the upper range of the legend in the grey-scaled images of
jVrj can have signiﬁcant effect on visualising details of the
ﬂow's characteristics. Speciﬁcally, decreasing the upper limit
of the legend from jVrj¼ 2000 to jVrj¼ 500 intensiﬁes the
clarity of the acoustic pressure waves emitted by the under-
expanded jets. The pictures of Fig. 9 are in great agreement
with the LES visualisation of the under-expanded air jets of
Dauptain et al. [49,50]. Table 3 presents quantitatively a
comparison of the important near-ﬁeld shock characteristics
of the different under-expanded jets of the current study.
As mentioned earlier, the Mach disk height can be esti-
mated using the empirical equations (1), (3), (5) and (7) . For a
speciﬁc substance these empirical relations can be adapted to:
Hdisk
D ¼ CH /C2
ﬃﬃﬃﬃﬃﬃ
P0
P∞
s
(22)
in which CH is an empirical constant that can be deﬁned by the
slope of the lines in Fig. 10. Those lines are based on the results
of the current study and on previously mentioned empirical
relations. Fig. 10 shows that the Mach disk height predicted by
the current LES study is in agreement with the empirical
relation of Ashkenaz and Sherman [29], i.e. equation (7), for
(P
0/P∞)0.5 /C20 5. For higher values of ( P0/P∞)0.5 though, the dif-
ference between the Hdisk of the current study and that of
equation (7) increased and at ( P0/P∞)0.5 z 8.4 a difference of
about 3.8% was quantiﬁed. The current study suggested a
value of C
H ¼ 0.71 for the empirical constant of equation (22),
particularly for under-expanded hydrogen jets. According to
[59], C
H z 0.67 may not be accurate enough for injection
pressures above P0 ¼ 10 MPa. The current study suggests that
in addition to the injection pressure, NPR is also important
and for nozzle pressure ratios greater than about 70 the linear
relation between H
disk/D and (P0/P∞)0.5 may not be valid.
As shown in Table 3, by increasing NPR from 8.5 to 10, the
Mach disk height and width of the under-expanded hydrogen
jet increased by ~11% and ~23%, respectively. Then by
increasing NPR from 10 to 30 an increase of ~83% and ~151%
could be seen for the height and width of the Mach disk,
Fig. 8 e Development of the axial Mach number in the hydrogen jet with NPR ¼ 10.
international journal of hydrogen energy 39 (2014) 21275 e21296 21285

<!-- PDF_PAGE: 12 -->

respectively. This showed a considerably higher level of
sensitivity of the width of the Mach disk to NPR in comparison
to its height. The correlation suggested by Antsupov [27], i.e.
equation (4), was also used to estimate the width of Mach disk
and values of 1.065, 1.33, and 3.12 were obtained for NPR of 8.5,
10 and 30, respectively. According to Table 3 , the current LES
study predicted Mach disk width very close to equation (4) for
NPR ¼ 8.5 and 10, whilst for NPR ¼ 30 a value higher by ~8%
was predicted by LES. Reordering equation (6) for the coefﬁ-
cient z and using values of Mach disk height and width ob-
tained from the current LES work, z was estimated to be ~0.72,
~0.80 and ~1.1 for NPR of 8.5, 10, and 30, respectively.
Examining more nozzle pressure ratios could provide the
opportunity to plot z versus NPR and consequently estimate
the Mach disk width based on its height.
Direct comparison between the methane and hydrogen
jets at NPR ¼ 8.5 (see Fig. 9 ) reveals that the height of meth-
ane's Mach disk is ~2.5% larger than that of hydrogen 's. Ac-
cording to equations (2) and (5) the Mach disk height is weakly
related to the ratio of speciﬁc heats. If the ratio of speciﬁc
heats for hydrogen and methane is used to calculate the Mach
disk height by equation (5) (g z 1.41 and 1.32, respectively), a
difference of 2.1% is calculated between the two jets which is
very close to the 2.5% predicted by LES. It was also found that
Fig. 9 e Methane and hydrogen jets with NPR ¼ 8.5. Left: Turbulent and mixing structure. Right: Close-up view of the near-
nozzle shock structure.
Table 3 e Characteristics of the under-expanded jets under study.
Gas NPR Mach disk
height [mm]
Mach disk
width [mm]
Reﬂected shock
angle [deg]
Shear layer
thickness [mm]
Subsonic length
(Ma < 0.9) [mm]
Acceleration
length [mm]
CH4 8.5 2.85 1.218 ~28.5 ~0.7 4.05 1.67
H2 8.5 2.78 1.091 ~28.5 ~0.327 2.03 2.03
H2 10 3.09 1.34 ~28.0 ~0.318 4.035 1.87
H2 30 5.65 3.37 ~28.0 ~0.266 5.75 5.75
H2 70 8.72 NA ~28.0 NA No Cell No Cell
international journal of hydrogen energy 39 (2014) 21275 e2129621286

<!-- PDF_PAGE: 13 -->

the Mach disk width with NPR ¼ 8.5 was ~12% wider for
methane than for hydrogen (see Table 3).
The angle of the reﬂected shock at the triple point was
found to be b ¼ 28.5/C14 for both methane and hydrogen jets with
NPR ¼ 8.5, the same to that reported by Vuorinen et al. [51].
Increasing the NPR from 8.5 to 10 reduced the reﬂected shock
angle slightly to b ¼ 28/C14 . It was noticed that further increase in
NPR did not have any noticeable effect on the reﬂected shock
angle and for NPR ¼ 30 this was also 28
/C14 . For NPR ¼ 70, the
value of b could not be measured with sufﬁcient accuracy
because the reﬂected shock was located outside of the reﬁned
area of the computational grid; however, based on observa-
tions of the present work and previous studies [51] it is
believed that for NPR ¼ 70 the reﬂected shock angle would also
be about 28
/C14 , i.e. beyond NPR ¼ 10 the value of b remains
almost constant.
From Fig. 9 it is evident that the shear layer thickness d was
wider for methane than for hydrogen. Speciﬁcally, for
NPR ¼ 8.5, the methane jet had d z 0.47D in comparison to
d z 0.22D for hydrogen, i.e. the shear layer was wider by about
115% for methane. The value of d for hydrogen is in satisfac-
tory agreement with the value of d z 0.25D for the under-
expanded nitrogen jet with NPR ¼ 8.5 of [51]. It was also
noticed that by increasing the NPR from 8.5 to 10 and then to
30 the shear layer thickness reduced by about 3% and 19%,
respectively (see Table 3).
Flow characteristics of under-expanded jets
Instantaneous snapshots of fuel mole fraction (H 2 or CH 4),
temperature, velocity and Mach number are presented at
t ¼ 0.2 ms after the start of injection in Fig. 11 for various
values of NPR. A semi opaque mask has been applied on these
snapshots to highlight the main region of interest in the core
of the jets. Hydrogen eair mixing prior to the location of the
Mach disk is evident. It is also clear that for the same NPR of
8.5, the hydrogen jet was more voluminous than the methane
jet. This can be explained by the lower density and higher
diffusivity of hydrogen which speed up the mixing process
and increase the radial penetration rate of hydrogen in com-
parison to methane. Furthermore, it is also clear that the fuel
core with X z 1 penetrated further in the axial direction with
hydrogen than with methane. Very similar spatial variation of
mole fraction was noticed between hydrogen jets with
NPR ¼ 8.5 and NPR ¼ 10. For NPR ¼ 30 the hydrogen mole
fraction snapshot of Fig. 11 displays clearly a wider jet in
which the majority of the highlighted area had X /C21 0.7 and the
core with X z 1 penetrated beyond the area shown in the
snapshots.
The temperature snapshot in Fig. 11 shows that the tem-
perature of the methane jet with NPR ¼ 8.5 dropped to
T z 103 K just upstream of the Mach disk, whereas it dropped
to T z 77 K for hydrogen at the same NPR. It was also found
that for hydrogen with NPR of 10 and 30 the temperature at the
vicinity of the Mach disk dropped to T z 71 K and T z 41 K,
respectively. It is worth noting here that for the simulated
hydrogen jets, the near-nozzle temperature distribution may
not be accurate due to the negative JouleeThomson coefﬁcient
of hydrogen which cannot be captured by employing ideal gas
assumptions. However, according to [59,60], even use of a real
gas EoS, temperatures near to cryogenic conditions (similar to
those of the present work) would be measured upstream of
the Mach disk for under-expanded hydrogen jets. Fig. 12 pre-
sents the axial temperature ( i.e. on the centre-line of the
chamber) normalized by the nozzle exit temperature calcu-
lated by LES ( T
1 z 248 K and T1 z 235 K for methane and
hydrogen, respectively) is presented. It is noted that the axial
temperature did not exceed the ambient temperature for both
methane and hydrogen fuels, whilst [60] has shown that a real
gas EoS would predict a higher temperature than the ambient
temperature just after the Mach disk by ~15%.
The corresponding instantaneous snapshot of the spatial
distribution of the velocity magnitude is also shown in Fig. 11.
It was found that the velocity in the methane jet with
NPR ¼ 8.5 reached a maximum value of U ¼ 927 m/s at the
vicinity of the Mach disk, whereas for the same NPR the
hydrogen jet reached a maximum velocity of U ¼ 2493 m/s. For
under-expanded hydrogen jets with NPR ¼ 10 and NPR ¼ 30 a
maximum velocity of U ¼ 2531 m/s and U ¼ 2695 m/s was
observed, respectively. The nozzle exit velocity ( U
1) was
calculated by LES to be U1 ¼ 458 m/s for methane, U1 z 1305 for
hydrogen with NPR ¼ 8.5, 10 and 30 and U1 ¼ 1311 for hydrogen
with NPR ¼ 70. It was noted that the maximum value of
normalized axial velocity ( U/U1) for the methane jet was 2.02
and for the hydrogen jets with NPR ¼ 8.5, 10, 30, and 70 this
was 1.90, 1.93, 2.06 and 2.11, respectively. This is in satisfac-
tory agreement with the U/U
1 graph presented in Ref. [28] for
an under-expanded air jet with NPR ¼ 30.
Instantaneous snapshots of Ma are also included in Fig. 11.
Several shock cells and high velocity ( Ma > 1) slip regions after
the Mach disk can be seen clearly. Fig. 13 shows the variation
of the axial Mach number on the centre-line. Cross-analysis of
Fig. 11 with Fig. 13 revealed that the maximum centre-line Ma
was not necessary the maximum Mach number within the
under-expanded jet. As shown in Fig. 11, the maximum Mach
Fig. 10 e Mach disk height ( Hdisk) as a function of NPR.
Comparison between the current LES study and available
empirical relations.
international journal of hydrogen energy 39 (2014) 21275 e21296 21287

<!-- PDF_PAGE: 14 -->

Fig. 11 e Contour snapshots of various ﬂow parameters at t ¼ 0.2 ms. (a): Methane NPR ¼ 8.5, (b): Hydrogen NPR ¼ 8.5, (c):
Hydrogen NPR ¼ 10, (d): Hydrogen NPR ¼ 30.
international journal of hydrogen energy 39 (2014) 21275 e2129621288

<!-- PDF_PAGE: 15 -->

number in the vicinity of the Mach disk for methane with
NPR ¼ 8.5 was Ma ¼ 3.51, whilst for hydrogen with NPR ¼ 8.5,
10, and 30 this was Ma ¼ 3.72, 3.96, and 5.53, respectively.
Fig. 13 shows slightly lower values for the axial Mach number
speciﬁcally Ma ¼ 3.48 for methane and Ma ¼ 3.68, 3.89, and
5.44 for hydrogen with NPR ¼ 8.5, 10 and 30, respectively. The
maximum axial Mach number for the under-expanded
hydrogen jet with NPR ¼ 70 was Ma ¼ 6.73.
As explained earlier in the current work (and also described
in detail in Ref. [25]), after the Mach disk and depending on the
level of NPR, the ﬂow can accelerate and reach Ma z 1 several
times. In the present work for methane at NPR ¼ 8.5 and
Fig. 12 e Normalized axial temperature at t ¼ 0.2 ms (Horizontal lines: d ∙ d normalized ambient temperature based on
methane's exit temperature, d ∙∙ d normalized ambient temperature based on hydrogen 's exit temperature).
Fig. 13 e Axial Mach number at t ¼ 0.2 ms.
international journal of hydrogen energy 39 (2014) 21275 e21296 21289

<!-- PDF_PAGE: 16 -->

hydrogen at NPR ¼ 8.5 and 10 it was noticed that just after the
Mach disk the subsonic ﬂow started accelerating and after a
speciﬁc distance ( z/D ¼ 3.016, 3.205 and 3.306, respectively) it
started slowing down. For the hydrogen jet with NPR ¼ 8.5 the
acceleration process caused the jet to reach Ma z 1.01
therefore the acceleration length and the length of the
subsonic core just after the Mach disk were the same and
equal to lsub z 1.35D. The Mach number in the methane jet of
NPR ¼ 8.5 and the hydrogen jet of NPR ¼ 10 reached the
maximum values of Ma z 0.74 and Ma z 0.82, respectively.
Then, further downstream, a second acceleration process led
to Ma > 0.9, i.e. to the sonic threshold. For the hydrogen jet
Fig. 14 e Axial absolute pressure at t ¼ 0.2 ms.
Fig. 15 e Normalized axial density at t ¼ 0.2 ms.
international journal of hydrogen energy 39 (2014) 21275 e2129621290

<!-- PDF_PAGE: 17 -->

with NPR ¼ 30, past the Mach disk, the jet started ﬂuctuating in
the range of Ma ¼ 0.6e0.7. At z/D z 5.1 the jest reached
Ma ¼ 0.91 which created a subsonic length of lsub z 3.8D. For
the hydrogen jet with NPR ¼ 70 no major ﬂow acceleration was
noticed past the Mach disk and the jet continued decaying in a
subsonic manner, similarly to what has been described in Ref.
[25].
Figs. 14 and 15 illustrate the axial pressure ( P) and
normalized axial density ( r/r
1)( i.e. on the centre-line of the
chamber) for the methane and hydrogen jets. A higher tran-
sient ﬂuctuation of both axial pressure and normalized axial
density was seen for hydrogen with NPR ¼ 8.5 in comparison
to the methane jet at the same NPR; this indicated higher
compressibility effects for the hydrogen jet. In the vicinity of
the Mach disk for the methane jet and hydrogen jets with
NPR ¼ 8.5, 10 and 30, the pressure reached a value higher than
the ambient pressure and then started ﬂuctuating around the
ambient value. For hydrogen with NPR ¼ 70, the pressure
jumped to a value lower than the ambient just after the Mach
disk and then increased, but with a lower level of ﬂuctuation
in comparison to the other test cases. Hydrogen 's density
dropped to values as low as ~0.02 kg/m
3 and then increased
almost instantly past the Mach disk due to the normal shock
recompression. After the Mach disk location, density
increased towards the ambient value via a ﬂuctuating pattern.
It was noticed that a lower NPR would result in higher density
ﬂuctuations and, consequently, a faster growth rate of the jet's
axial density. The nozzle exit density ( r
1) for the methane jet
with NPR ¼ 8.5 and for the hydrogen jets with NPR ¼ 8.5, 10, 30
and 70 was 3.04, 0.39, 0.46, 1.37 and 3.23 kg/m 3, respectively.
These values resulted in respective mass ﬂow rates of 2.46,
0.90, 1.06, 3.16 and 7.49 g/s.
As seen in Fig. 16 , the nozzle exit pressure and mass ﬂow
rate of the under-expanded hydrogen jets were linearly
related to the NPR; a similar linear relationship has been re-
ported by Vuorinen et al. [51]. In comparison to the LES studies
of nitrogen jets of [51], the current LES study of under-
expanded hydrogen jets predicted lower variation rates for
the nozzle exit pressure and nozzle exit mass ﬂow rate versus
NPR. This is believed to be due to differences in nozzle design
and also different compressibility effects of the two different
working gases. It is also worth mentioning that both the cur-
rent study and the work presented in Ref. [51] conﬁrmed that
in high-pressure gaseous injectors the actual nozzle exit
conditions, such as exit pressure, may not follow isotropic
relations [53] such as P
1 ¼ 0.528P0. Therefore, simulating the
in-nozzle ﬂow of under-expanded jets is necessary to obtain
accurate conditions at the nozzle exit.
Mixing characteristics
As seen in Figs. 7 and 9 , methane eair mixing did not occur
before the Mach disk. In contrast, the strong ﬂuctuations at the
jet boundary before the Mach disk of the hydrogen jet repre-
sented considerable level of momentum exchange and mixing
just by the border of the barrel-shape shock. This mixing is
associated with Gortler vortices that are characterized by the
Gortler number deﬁned as [51,74,75]:
G ¼
Us q
n
/C18 q
r
/C19 1 =
2
(23)
where Us is a velocity scale, q is the momentum thickness of
incoming boundary layer, r is the radius of the shock cell
curvature and n is the kinematic viscosity. According to Ref.
[51],i f G exceeds ~0.3 in under-expanded jets, Gortler vortices
(i.e. mixing) may occur outside the barrel-shape shock before
the Mach disk location. Us is considerably greater for hydrogen
than for methane (by about 3 times) due to the faster rate of
acoustic waves propagation in hydrogen; see equation (20).
Fig. 9 also illustrates that for hydrogen jetting, q is consider-
ably larger than for methane. The radius of the barrel-shape
Fig. 16 e Nozzle exit pressure and mass ﬂow of hydrogen jets as a function of NPR.
international journal of hydrogen energy 39 (2014) 21275 e21296 21291

<!-- PDF_PAGE: 18 -->

shock curvature was almost similar for both jets. Therefore,
the high kinematic viscosity of hydrogen, nH2 ¼ 110 /C2 10/C0 6 m2/s
vs. nCH4 ¼ 17.2 /C2 10/C0 6 m2/s [15] at atmospheric conditions,
cannot overcome the effect of Us and q, thus a noticeable
higher Gorlter number is expected for hydrogen jet than for
methane.
The jet tip penetration for the methane and hydrogen jets
with various nozzle pressure ratios is plotted in Fig. 17 . For
NPR ¼ 8.5, after the initial transient process ( t z 0.075 ms), the
hydrogen jet penetrated ~40% more than the methane jet,
thus faster mixing is expected in an engine with hydrogen
fuelling. As shown earlier in the mole fraction snapshot of
Fig. 11 , hydrogen produced a wider jet that methane did.
Therefore, a higher value of NPR is required for methane in-
jection in order to deliver comparable mixing characteristics
to hydrogen with NPR ¼ 8.5. For both methane and hydrogen,
the primary mixing started after the Mach disk location,
particularly closer to the jet boundaries where intense tur-
bulence seemed to play a dominant role in the mixing process.
It was also observed that the hydrogen jet with NPR ¼ 10
had longer penetration by ~5% in comparison to the hydrogen
jet with NPR ¼ 8.5. On the other hand, within the initial in-
jection duration (typically up to t z 0.065 ms), the hydrogen
jets with NPR ¼ 30 and 70 penetrated more than the hydrogen
jet with NPR ¼ 10 (longer penetration observed for NPR ¼ 70).
After the initial transient period, the jet with NPR ¼ 70
continued to penetrate with a rate similar to the hydrogen jet
with NPR ¼ 8.5, whereas the hydrogen jet with NPR ¼ 30
continued to penetrate with even lower rate (~8% less). This
behaviour of the hydrogen jets with NPR ¼ 30 and 70 can be
regarded as the result of the noticeably wider jet in compari-
son to NPR ¼ 8.5 and 10. A similar trend was noticed by
Owston et al. [76] where for hydrogen jets with similar mass
ﬂow rates, NPR z 20 produced lower penetration than
NPR z 10. They concluded that inadequate grid resolution
caused this to occur [76]. However, in the current study where
according to the literature [49e51] the grid resolution has been
ﬁne enough to capture details of under-expanded jets, a
similar trend was observed, even for jets with different mass
ﬂow rates. Therefore, it can be assumed that there could be a
trade-off between the width and penetration of hydrogen and
that there should be an optimum NPR that can provide
desirable penetration (which can enhance mixing), whilst also
delivering enough fuel within an appropriate injection
duration.
As discussed earlier in the validation section, Vuorinen
et al. [51] reported that NPR is proportional to the jet volume
with an exponent of 3/4; consequently, they concluded that
NPR had little effect on the mixture richness. This may be
valid for less diffusive jets and for low level of nozzle pressure
ratios (e.g. NPR < 10), as well as when comparing jets with NPR
varied over a narrow range ( e.g. NPR ¼ 4e9 examined by the
latter authors). The current study suggests that for under-
expanded hydrogen jets, considerably richer mixture could
be produced if high NPR values, like 30 and 70, were applied
instead of NPR /C20 10. This can be observed in the mole fraction
contours of
Fig. 11 where for hydrogen with NPR ¼ 30 the
reﬁned area had almost X > 0.75, whereas the hydrogen jets
with NPR ¼ 8.5 and 10 demonstrated considerably leaner
mixtures within the reﬁned area and a similar spatial varia-
tion of mole fraction to each other.
Higher NPR leads to more enhanced mixing and entrain-
ment [51] and according to the present study it can also supply
richer mixture in less time. Hence, based on the mole fraction
contours of Fig. 11 and the penetration lengths of Fig. 17 ,a
value of NPR in the region of 100 could be an optimum strategy
for hydrogen DI since it would produce a richer jet with higher
penetration compared to NPR ¼ 10 and deliver more fuel in
less time. Certainly further investigation is necessary in order
to make a solid conclusion, especially for hydrogen jets with
NPR > 70 and in smaller scale nozzles. It is worth mentioning
here that in DI hydrogen-fuelled IC engines, the main air efuel
mixing occurs after the hydrogen jet 's wall impingement, e.g.
see Refs. [18,22]. In the present work a penetration length of
~3.5 cm (the length of the reﬁned area) was studied; this falls
within the range of 2 e5 cm that a hydrogen jet needs to
penetrate in a typical IC engine geometry before impinging
onto a surface of the cylinder liner or piston crown (depending
on injection strategy and injector position). Further study is
needed to investigate the characteristics of hydrogen pene-
tration with longer injection durations (thus over longer dis-
tances), e.g. for hydrogen safety considerations.
Summary and conclusions
The current computational study used LES to investigate the
near-nozzle shock structure and mixing characteristics of
under-expanded hydrogen jets. Direct comparison was con-
ducted between hydrogen and methane jets with NPR ¼ 8.5.
The effects of increasing NPR on under-expanded hydrogen
jets were further examined by enabling use of various values
of NPR, namely 8.5, 10, 30 and 70. The computational
framework was initially validated against experimental and
computational test cases available in the literature. Reference
parameters of the near-ﬁeld shock structure, i.e. Mach disk
height and width, reﬂected shock angle, length of subsonic
core after the Mach disk and shear layer thickness were
Fig. 17 e Jet tip penetration.
international journal of hydrogen energy 39 (2014) 21275 e2129621292

<!-- PDF_PAGE: 19 -->

quantiﬁed. The development of the transient under-
expanded jets, in addition to the transient behaviour of in-
nozzle compressible ﬂow, was investigated. Important mix-
ing characteristics of under-expanded jets with respect to IC
engine applications, e.g. jet tip penetration and volumetric
growth, were examined for both hydrogen and methane jets.
The main conclusions of this work can be summarised as
follows:
/C15 The near-ﬁeld shock structure, i.e. Prandtl eMeyer expan-
sion fans, barrel-shape shock, Mach disk dimensions, re-
ﬂected shock at the triple point and slip line were all
predicted in very good agreement with the classic deﬁni-
tion of under-expanded jets and with data available in the
literature.
/C15 During the initial transient process the height and width of
the Mach disk of both methane and hydrogen jets tempo-
rarily reached higher values than those observed at steady
state.
/C15 The near-nozzle shock structure of the methane jet with
NPR ¼ 8.5 showed slightly different pattern to the hydrogen
jets of NPR ¼ 8.5 and 10. The methane jet contained strong
expansion fans from the very beginning of its formation
and resulted in a normal shock wider than the nozzle
diameter that was very similar to a Mach disk. In turn, this
led to widely-spaced slip lines in comparison to those of
the hydrogen jets which were associated with a slim Mach
disk.
/C15 For hydrogen with NPR ¼ 30, the transient formation of the
near-nozzle shock structure was comparable to that of the
methane jet with NPR ¼ 8.5, i.e. with presence of a wide
Mach disk (normal shock) from the very beginning and
widely-spaced slip lines.
/C15 The height and width of the Mach disk were very sensitive
to NPR. A higher degree of sensitivity was noticed for the
width of the disk than for its height. Increasing NPR from
10 to 30 for hydrogen resulted in an increase of 83% and
150% in the height and width of the Mach disk, respectively.
/C15 The methane jet with NPR ¼ 8.5 had larger height and
width by 2.5% and 12%, respectively, than the corre-
sponding hydrogen jet, potentially due to the lower ratio of
speciﬁc heats ( g) of methane.
/C15 For methane, mixing did not occur before the Mach disk,
whereas for hydrogen high level of momentum exchange
and mixing was observed at the boundaries of the jet. This
is believed to be related to the effect of higher turbulent
ﬂuctuations at the nozzle exit and the larger Gortler num-
ber for hydrogen which triggered the presence of Gortler
vortices and initiated the mixing process.
/C15 For all under-expanded jets at semi-steady conditions,
chocked ﬂow of Ma z 1 occurred inside the nozzle volume
at about 0.5 D upstream of the nozzle exit. A maximum Ma
of about 1.3 was calculated about 0.2 D upstream of the
nozzle exit whilst the nozzle exit Ma was about 1.1.
Considering the small scale of the nozzle, high viscosity
dissipation due to large surface-to-volume ratio and also
exceptional compressible effects are potential reasons for
this behaviour. However, more work is required in order to
clarify the in-nozzle transient hydrogen ﬂow behaviour of
small-size nozzles.
/C15 The angle of the reﬂected shock at the triple point was 28.5
/C14
for both methane and hydrogen fuelling with NPR ¼ 8.5.
Increasing NPR from 8.5 to 10 reduced slightly the reﬂected
shock angle to 28
/C14 , whilst further increase in NPR did not
have any noticeable effect on this angle.
/C15 For NPR ¼ 8.5 the shear layer thickness was wider for
methane than for hydrogen by 114%. Increasing NPR for
hydrogen from 8.5 to 10 and then 30 led to a narrower shear
layer by 3% and 19%, respectively.
/C15 The difference between methane and hydrogen jets in
terms of the penetration length and volumetric growth was
found to come from differences in both sonic characteris-
tics and diffusivity. The sonic characteristics of the two jets
were different due to differences in the ratio of speciﬁc
heats and density. This resulted in hydrogen reaching
higher supersonic velocities than methane and consider-
ably higher penetration. Additionally, the higher diffusivity
of hydrogen resulted in the formation of a bulkier jet (due
to accelerated radial mixing) compared to methane
fuelling.
/C15 It was conﬁrmed that both the nozzle exit pressure and
nozzle mass ﬂow rate of under-expanded hydrogen jets
were linearly related to NPR. For NPR ¼ 8.5 the hydrogen jet
penetrated about 40% more than the methane jet, thus
faster in-cylinder mixing is expected for hydrogen. Higher
NPR was required for methane in order to deliver compa-
rable mixing characteristics to those of a hydrogen jet.
/C15 Higher NPR did not necessarily increase the hydrogen jet 's
penetration. After the initial transient process of ~0.1 ms,
the jet with NPR ¼ 70 showed a penetration length com-
parable to that with NPR ¼ 8.5. NPR ¼ 30 produced even
lower penetration by about 8%. NPR ¼ 100 could be the
optimum for hydrogen injection with the current geometry
but further study is needed for a widely applicable
conclusion.
/C15 Values of NPR in excess of 30 can have signiﬁcant effect on
the mixture richness within under-expanded hydrogen
jets and can provide richer mixture in less time.
/C15 For all methane and hydrogen jets studied in the current
work, the main mixing was observed to start after the Mach
disk location and particularly close to the jet boundaries
where intense turbulence was noticed to play a dominant
role in the mixing process.
Finally it should be noted that the in-cylinder operating
conditions of hydrogen-fuelled engines can be signiﬁcantly
different from the ambient conditions used within the objec-
tives of the current study, i.e. elevated pressures and tem-
peratures, depending on injection timing. However, although
the conditions used here are representative primarily of pro-
cesses with early injection strategies ( i.e. intake stroke and
early compression stroke injection timings), the different NPR
values used in the current study provided signiﬁcant infor-
mation regarding characteristics of under-expanded transient
jets and in-nozzle gaseous ﬂow behaviour which can be used
to design advanced high pressure gaseous injection systems
including high-pressure hydrogen injectors. Additionally, it is
noted that for under-expanded jets the sonic characteristics
do not depend on the downstream condition (in-cylinder) and
are primarily affected by the level of NPR. For instance let 's
international journal of hydrogen energy 39 (2014) 21275 e21296 21293

<!-- PDF_PAGE: 20 -->

consider two jets with NPR ¼ 10 which the ﬁrst one is injected
with 10 bar into 1 bar ambient and the other one is injected
into a 10 bar ambient with 100 bar injection pressure. The
near-nozzle shock structure for both jets would be expected to
be quite similar. However, mixing characteristics particularly
downstream of the Mach disk would be different. The char-
acteristics of under-expanded hydrogen and methane jets
under elevated conditions of ambient pressure and tempera-
ture are also being investigated by the current authors and will
be discussed in a future publication.
Acknowledgements
The authors acknowledge the use of University College Lon-
don's Legion High Performance Computing Facility (Legio-
n@UCL) and associated support services in the completion of
this work. The authors would also like to thank all members of
the UCL Internal Combustion Engines Group for their assis-
tance and many valuable discussions.
Nomenclature
AUSM Advection Upstream Splitting Method
C
p speciﬁc heat
Cs Sutherland's constant
CH4 methane
D nozzle exit diameter
Di diffusion coefﬁcient
DES detached eddy simulation
DNS direct numerical simulation
DI direct injection
f
f inviscid ﬂuxes
FV ﬁnite volume
g
f viscous ﬂuxes
G Gortler number
H2 hydrogen
Hdisk Mach disk height
I identity matrix
IC internal combustion
ILES implicit large eddy simulation
k turbulent kinetic energy
Kn Knudsen number
l
sub subsonic length after the Mach disk
LDA Laser Doppler Anemometry
LES large eddy simulation
M
i molecular weight
Ma Mach number
Ma1 nozzle exit Mach number
NPR nozzle pressure ratio
P ﬂuid pressure
P
0 stagnation pressure
P1 nozzle exit pressure
P∞ ambient pressure
PFI port fuel injection
PLIF planar laser-induced ﬂuorescence
R gas constant
r radius of the shock cell curvature
RANS Reynolds averaged NaviereStokes
Re Reynolds number
S strain tensor
t simulation time
t
0 integral time scale
T transpose sign
T temperature
T
0 stagnation temperature
T1 nozzle exit temperature
Ts reference temperature in Sutherland's law
T viscous stress tensor
U velocity magnitude
U1 nozzle exit velocity
Us velocity scale in Gortler number
V velocity vector
V computational cell volume
Vjet under-expanded jet volume
Wdisk Mach disk width
WENO weighted essentially non-oscillatory
X mole fraction
Y
i mixture species
z axial distance from the nozzle exit
Ztip jet tip penetration
Special characters
b reﬂected shock angle
g ratio of speciﬁc heats
ε turbulent dissipation rate
D length scale (LES grid ﬁlter)
d shear layer thickness in under-expanded jets
d boundary layer thickness
q thickness of incoming boundary layer
m dynamic viscosity
ms reference viscosity in Sutherland's law
mt turbulent viscosity
n kinematic viscosity
r density
r1 nozzle exit density
s molecular Schmidt number
s12 collision diameter
u speciﬁc dissipation rate
U molecular property in ChapmaneEnskong
formulation
V gradient operator
references
[1] Bokris JO’M. The origin of ideas on a hydrogen economy and
its solution to the decay of the environment. Int J Hydrog
Energy 2002;27:731 e40.
[2] Lattin WC, Utgikar VP. Transition to hydrogen economy in
the United States: a 2006 status report. Int J Hydrog Energy
2007;32:3230e7.
[3] White CM, Steeper RR, Lutz AE. The hydrogen-fueled internal
combustion engine: a technical review. Int J Hydrog Energy
2006;31:1292e305.
[4] Verhelst S, Wallner T. Hydrogen-fueled internal combustion
engines. Prog Energy Combust Sci 2009;35:490 e527.
[5] Al-Baghdadi M, Al-Janabi HA. A prediction study of a spark
ignition supercharged hydrogen engine. Energy Convers
Manag 2003;44:3143 e50.
international journal of hydrogen energy 39 (2014) 21275 e2129621294

<!-- PDF_PAGE: 21 -->

[6] Berckmu¨ ller M, Rottengruber H, Eder A, Brehm N, Els €asser G,
Mu¨ ller-Alander G, Schwarz C. Potentials of a charged SI-
hydrogen engine. 2003. SAE Technical Paper 2003-01-3210 .
[7] Verhelst S, Sierens R. Combustion studies for PFI hydrogen IC
engines. 2007. SAE Technical Paper 2007-01-3610 .
[8] Verhelst S, Maesschalck P, Rombaut N, Sierens R. Increasing
the power output of hydrogen internal combustion engines
by means of supercharging and exhaust gas recirculation. Int
J Hydrog Energy 2009;34:4406 e12.
[9] Kawahara N, Tomita E. Visualization of auto-ignition and
pressure wave during knocking in a hydrogen spark-ignition
engine. Int J Hydrog Energy 2009;34:3156 e63.
[10] Rakopoulos CD, Kosmadakis GM, Pariotis EG. Evaluation of a
combustion model for the simulation of hydrogen spark-
ignition engines using a CFD code. Int J Hydrog Energy
2010;35:12545e60.
[11] Rakopoulos CD, Kosmadakis GM, Demuynck J, De Paepe M,
Verhelst S. A combined experimental and numerical study of
thermal processes, performance and nitric oxide emissions
in a hydrogen-fueled spark-ignition engine. Int J Hydrog
Energy 2011;36:5163 e80.
[12] Aleiferis PG, Rosati MF. Flame chemiluminescence and OH
LIF imaging in a hydrogen-fuelled spark-ignition engine. Int J
Hydrog Energy 2012;37:1797 e812.
[13] Kaiser S, White C. PIV and PLIF to evaluate mixture
formation in a direct-injection hydrogen-fuelled engine. SAE
Int J Engines 2009:657 e68.
[14] Wallner T, Nande A, Naber J. Evaluation of injector location
and nozzle design in a direct-injection hydrogen research
engine. 2008. SAE Technical Paper 2008-01-1785 .
[15] Rosati M, Aleiferis PG. Hydrogen SI and HCCI combustion in a
direct-injection optical engine. SAE Int J Engines
2009:1710e36.
[16] Scarcelli R, Wallner T, Salazar V, Kaiser S. Modeling
and experiments on mixture formation in a hydrogen
direct-injection research engine. SAE Int J Engines
2010:530e41.
[17] Salazar V, Kaiser S. An optical study of mixture preparation
in a hydrogen-fueled engine with direct injection using
different nozzle designs. SAE Int J Engines 2010:119 e31.
[18] Scarcelli R, Wallner T, Matthias N, Salazar V, Kaiser S.
Mixture formation in direct injection hydrogen engines: CFD
and optical analysis of single- and multi-hole nozzles. SAE
Int J Engines 2011:2361 e75.
[19] Roy M, Kawahara N, Tomita E, Fujitani T. High-
pressure hydrogen jet and combustion characteristics in a
direct-injection hydrogen engine. SAE Int J Fuels Lubr
2012:1414e25.
[20] Nakagawa K, Yamane K, Ohira T. Potential of large output
power, high thermal efﬁciency, near-zero NO
x emission,
supercharged, lean-burn, hydrogen-fuelled, direct injection
engines. Energy Procedia 2012;29:455 e62.
[21] Aleiferis PG, Rosati MF. Controlled autoignition of hydrogen
in a direct-injection optical engine. Combust Flame
2012;159:2500e15.
[22] Hamzehloo A, Aleiferis PG. Computational study of hydrogen
direct injection for internal combustion engines. 2013. SAE
Technical Paper 2013-01-2524 .
[23] Crist S, Sherman PM, Glass DR. Study of the highly
underexpanded sonic jet. AIAA J 1966;4:68 e71.
[24] Abbett M. The mach disk in underexpanded exhaust plumes.
AIAA J 1971;9:512 e4.
[25] Donaldson CDuP, Snedeker RS. A study of free jet
impingement. Part 1. Mean properties of free and impinging
jets. J Fluid Mech 1971;45:281 e319.
[26] Ewan BCR, Moodie K. Structure and velocity measurements
in underexpanded jets. Combust Sci Technol 1986;45:275 e88.
[27] Antsupov AV. Properties of underexpanded and
overexpanded supersonic gas jets. Soviet Phys Tech Phys
1974;19:234e8.
[28] Velikorodny A, Kudriakov S. Numerical study of the near-
ﬁeld of highly underexpanded turbulent gas jets. Int J Hydrog
Energy 2012;37:17390 e9.
[29] Ashkenas H, Sherman FS. The structure and utilization of
supersonic free jets in low density wind tunnel. In: Advances
in applied mechanics drareﬁed gas dynamics. New York:
Academic Press; 1965. p. 84 e105.
[30] Turner JS. The starting plume in neutral surroundings. J Fluid
Mech 1962;13:356 e68.
[31] Hill PG, Ouellette P. Transient turbulent gaseous fuel jets for
diesel engines. J Fluids Eng 1999;121:93 e101.
[32] Abraham J. Entrainment characteristics of transient gas jets.
Numer Heat Transf 1996;30:3478 e4364.
[33] Petersen B, Ghandhi J. Transient high-pressure hydrogen jet
measurements. 2006. SAE Technical Paper 2006-04-03 .
[34] Chuech SG, Lai MC, Faeth GM. Structure of turbulent sonic
underexpanded free jets. AIAA J 1989;27:549 e56.
[35] Panda J, Seasholtz RG. Measurement of shock structure and
shockevortex interaction in underexpanded jets using
Rayleigh scattering. Phys Fluids 1999;11 .
[36]
Yuceil KB, Otugen MV. Scaling parameters for
underexpanded supersonic jets. Phys Fluids 2002;14 .
[37] Yu J, Vuorinen V, Hillamo H, Sarjovaara T, Kaario O, Larmi M.
An experimental study on high pressure pulsed jets for DI
gas engine using planar laser-induced ﬂuorescence. 2012.
SAE Technical Paper 2012-01-1655 .
[38] Prudhomme SM, Haj-Hariri H. Investigation of supersonic
underexpanded jets using adaptive unstructured ﬁnite
elements. Finite Elem Anal Des 1994;17:21 e40,.
[39] Irie T, Yasunobu T, Kashimura H, Setoguchi T.
Characteristics of the Mack disk in the underexpanded jet in
which the back pressure continuously changes with time. J
Therm Sci 2003;12:132 e7.
[40] Cheng TS, Lee KS. Numerical simulations of underexpanded
supersonic jet and free shear layer using WENO schemes. Int
J Heat Fluid Flow 2005;26:755 e70.
[41] Suzuki H, Endo M, Sakakibara Y. Structure and oscillation of
underexpanded jet. Open J Fluid Dyn 2013;3:85 e91.
[42] Dubs P, Khalij M, Benelmir R, Tazibt A. Study on the
dynamical characteristics of a supersonic high pressure ratio
underexpanded impinging ideal gas jet through numerical
simulations. Mech Res Commun 2011;38:267 e73.
[43] Chauvet N, Deck S, Jacquin L. Numerical study of mixing
enhancement in a supersonic round jet. AIAA J
2007;45:1675e87.
[44] Lehnasch G, Bruel P. A robust methodology for RANS
simulations of highly underexpanded jets. Int J Numer
Methods Fluids 2008;56:2179 e205.
[45] White T, Milton B. Shock wave calibration of under expanded
natural gas fuel jets. Shock Waves 2008;18:353 e64.
[46] Chin C, Li M, Harkin C, Rochwerger T, Chan L, Ooi A.
Investigation of the ﬂow structures in supersonic free and
impinging jet ﬂows. J Fluids Eng 2013;135 .
[47] Chauvet N, Deck S, Jacquin L. Zonal detached eddy
simulation of a controlled propulsive jet. AIAA J
2007;45:2458e73.
[48] Deck S. Delayed detached eddy simulation of the end-effect
regime and side-loads in an overexpanded nozzle ﬂow.
Shock Waves 2009;19:239 e49.
[49] Dauptain A, Cuenot B, Gicquel YM. Large-eddy simulation of
a stable supersonic jet impinging on ﬂat plate. AIAA J
2010;48:2325e37.
[50] Dauptain A, Gicquel YM. Large eddy simulation of supersonic
impinging jets. AIAA J 2012;50:1560 e74.
international journal of hydrogen energy 39 (2014) 21275 e21296 21295

<!-- PDF_PAGE: 22 -->

[51] Vuorinen V, Yu J, Tirunagari S, Kaario O, Larmi M, Duwig C,
et al. Large-eddy simulation of highly underexpanded
transient gas jets. Phys Fluids 2011;23 .
[52] Yu J, Vuorinen V, Kaario O, Sarjovaara T, Larmi M.
Visualization and analysis of the characteristics of
transitional underexpanded jets. Int J Heat Fluid Flow
2013;44:140e54.
[53] Anderson JD. Modern compressible ﬂow: with historical
perspective. 3rd ed. McGraw-Hill; 2003 .
[54] Roe PL. Approximate Riemann solvers, parameter vectors,
and difference schemes. J Comput Phys 1981;43:357 e72.
[55] Liou MS, Steffen CJ. A new ﬂux splitting scheme. J Comput
Phys 1993;107:23 e39.
[56] Ruggles AJ, Ekoto IW. Ignitability and mixing of
underexpanded hydrogen jets. Int J Hydrog Energy
2012;37:17549e60.
[57] Gorl/C19e C, Gamba M, Ham F. Investigation of an
underexpanded hydrogen jet in quiescent air using
numerical simulations and experiments. In: Annual research
briefs. Center for Turbulence Research, Stanford University;
2010.
[58] Gorl/C19e C, Iaccarino G. Large eddy and Reynolds-averaged
Navier-Stokes simulations of an underexpanded sonic jet. In:
7th European symposium on aerothermodynamics.
Netherlands: European Space Agency; 2011 .
[59] Khaksarfard R, Kameshki MR, Paraschivoiu M. Numerical
simulation of high pressure release and dispersion of
hydrogen into air with real gas model. Shock Waves
2010;20:205e16.
[60] Bonelli F, Viggiano A, Magi V. A numerical analysis of
hydrogen underexpanded jets under real gas assumption. J
Fluids Eng 2013;135 .
[61] Weiss JM, Smith WA. Preconditioning applied to variable and
constant density ﬂows. AIAA J 1995;33:2050 e7.
[62] Weiss JM, Maruszewski JP, Smith WA. Implicit solution of
preconditioned Navier eStokes equations using Algebraic
multigrid. AIAA J 1999;37:29 e36.
[63] Nicoud F, Ducros F. Subgrid-scale stress modelling based on
the square of the velocity gradient tensor, ﬂow. Turbul
Combust 1999;62:183 e200.
[64] Cussler EL. Diffusion: mass transfer in ﬂuid systems. 3rd ed.
Cambridge University Press; 2009 .
[65] Hirschfelder JO, Curtiss CF, Bird RB. Molecular theory of
gases and liquids. 2nd ed. John Wiley & Sons; 1964 .
[66] Gad-el-Hak M. The ﬂuid mechanics of microdevices e the
freeman scholar lecture. J Fluids Eng 1999:5 e33.
[67] Ouellette P, Hill PG. Turbulent transient gas injections. J
Fluids Eng 2000:743 e53.
[68] Abdi MA, Jassim E, Haghighi M, Muzychka Y. Applications of
CFD in natural gas processing and transportation. In: Woo
Oh Hyoung, editor. Computational ﬂuid dynamics; 2010 .
[69] Ho C, Tai Y. Micro-electro-mechanical-systems (MEMS) and
ﬂuid ﬂows. Annu Rev Fluid Mech 1998;30:579 e612.
[70] Jie D, Diao X, Cheong KB, Yong LK. Navier eStokes
simulations of gas ﬂow in micro devices. J Micromechanics
Microengineering 2000;10:372 e9.
[71] Rostami AA, Mujumdar AS, Saniei N. Flow and heat transfer
for gas ﬂowing in microchannels: a review. Heat Mass Transf
2002;38:359e67.
[72] Hao PF, Ding Y, Yao Z, He F, Zhu K. Size effect on gas ﬂow in
micro nozzles. J Micromechanics Microengineering
2005;15:2069e73.
[73] Zhu Y, Jiang P. Experimental and numerical investigation of
the effect of shock wave characteristics on the ejector
performance. Int J Refrig 2014;40:31 e42.
[74] Hall P. Taylor-Gortler vortices in fully developed or
boundary-layer ﬂows: linear theory. J Fluid Mech
1982;124:475e94.
[75] Saric WSm. Gortler vortices. Annu Rev Fluid Mech
1994;26:379e409.
[76] Owston R, Magi V, Abraham J. Fuel-air mixing characteristics
of DI hydrogen jets. SAE Int J Engines 2009:693 e712.
international journal of hydrogen energy 39 (2014) 21275 e2129621296
