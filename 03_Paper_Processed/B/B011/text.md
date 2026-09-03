<!-- PDF_PAGE: 1 -->

Gas dynamics and ﬂow characteristics of highly
turbulent under-expanded hydrogen and methane
jets under various nozzle pressure ratios and
ambient pressures
A. Hamzehloo, P.G. Aleiferis *,1
Department of Mechanical Engineering, University College London, UK
article info
Article history:
Received 1 December 2015
Received in revised form
25 January 2016
Accepted 3 February 2016
Available online 24 March 2016
Keywords:
Under-expanded jets
Mach disk
Vortex ring
Tip vortices
Shear layer
Turbulent mixing
abstract
The current study used large eddy simulations to investigate the sonic and mixing char-
acteristics of turbulent under-expanded hydrogen and methane jets with various nozzle
pressure ratios issued into various ambient pressures including elevated conditions rele-
vant to applications in direct injection gaseous-fuelled internal combustion engines. Due to
the relatively low density of most gaseous fuels such as hydrogen and methane, DI requires
high injection pressures to achieve suitable mass ﬂow rates for fast in-cylinder fuel de-
livery and rapid fuel-air mixing. Such pressures typically form an under-expanded fuel jet
past the nozzle exit. Test cases of hydrogen injection with nozzle pressure ratio (NPR) of 10
issued into quiescent air with pressure P
∞ z 1, 5 and 10 bar were simulated. Direct com-
parison between hydrogen and methane jets with NPR ¼ 8.5 and P ∞ z 1 was also made.
The effect of ambient pressure on features of transient development of the near-nozzle
shock structure and tip vortices (vortex ring) was investigated. It was observed that at
constant NPR, higher ambient pressure resulted in slightly faster formation of the Mach
reﬂection and shorter Mach disk settlement time. Different mechanisms were observed
between hydrogen and methane with regards to transient formation of their initial tip
vortex rings. It was found that the initial transient tip vortices of hydrogen jets may also
contribute to the ﬂow instabilities at the boundary of the intercepting shock and, unlike for
methane, promote fuel-air mixing before the Mach reﬂection. It was also shown that the
near-nozzle shock structure was only affected by NPR regardless of the ambient pressure.
Furthermore, no ﬂow recirculation zone was found just downstream of the Mach disk, a
ﬁnding comparable to all previous experimental investigations. Also, it was observed that a
locally richer mixture was created for jets with higher NPR or with higher ambient pressure
at constant NPR. Based on the results of the current study, correlations were proposed for
the shock cell spacing and jet tip penetration of highly under-expanded jets issued from
millimetre-size circular nozzles.
Copyright © 2016, Hydrogen Energy Publications, LLC. Published by Elsevier Ltd. All rights
reserved.
* Corresponding author . University College London, Department of Mechanical Engineering, Torrington Place, London WC1E 7JE, UK.
Tel.: þ44 (0)20 76793862.
E-mail addresses: p.aleiferis@ucl.ac.uk, p.aleiferis@imperial.ac.uk (P.G. Aleiferis).
1 Currently: Imperial College London, Department of Mechanical Engineering, Exhibition Road, London SW7 2AZ, UK. Tel.: þ44 (0)20
75947032.
Available online at www.sciencedirect.com
ScienceDirect
journal homepage: www.elsevier.com/locate/he
international journal of hydrogen energy 41 (2016) 6544 e6566
http://dx.doi.org/10.1016/j.ijhydene.2016.02.017
0360-3199/Copyright © 2016, Hydrogen Energy Publications, LLC. Published by Elsevier Ltd. All rights reserved.

<!-- PDF_PAGE: 2 -->

Introduction
Gaseous fuelling
One of the proposed solutions to strengthen security of fuel
supply and comply with international obligations for reduc-
tion of carbon-based emissions is to diversify towards use of
more sustainable fuels and cleaner energy sources. More than
a few alternative liquid and gaseous fuels have been recom-
mended for spark-ignition internal-combustion engines.
Gaseous hydrogen (H
2) has been proposed as, ideally, the most
promising carbon-free alternative particularly for road trans-
portation if produced in a sustainable manner. Development
of hydrogen-fuelled spark-ignition engines has been investi-
gated experimentally and computationally by various
research groups predominantly since the beginning of the
past decade [1]. However, the technology of hydrogen-fuelled
IC engines has not yet been commercialized due to various
technical and political obstacles including: absence of fully
developed high-pressure hydrogen injectors with the neces-
sary degree of durability, issues with on-board hydrogen
storage and high-pressure fuel delivery systems with suitable
crashworthiness characteristics, difﬁculties in mass produc-
tion of hydrogen in clean and sustainable ways, the need for
signiﬁcant infrastructural investments for worldwide
hydrogen distribution networks, etc. For the past twenty years
or so the use of hydrogen has also been widely researched for
fuel-cell powered vehicles. However, despite the relatively
high efﬁciency of fuel cells, their manufacturing cost is still
expensive and there are also several remaining technical
challenges related to their performance under a range of
conditions, condensation issues, etc. Therefore, the concept of
a hydrogen-fuelled combustion engine is still quite appealing
for future application on a commercial scale. On the other
hand, methane, in the form of compressed natural gas (CNG),
has been used on a commercial scale as a relatively cleaner
and cheaper alternative fuel for road transportation and
power generation [2].
Nomenclature
Latin symbols and abbreviations
A shock upstream condition
AMG algebraic multigrid
B shock downstream condition
AUSM advection upstream splitting method
C
A coefﬁcient of the new correlation of the jet tip
penetration
C
W constant of Mach disk height correlation
Cf coefﬁcient in jet penetration correlation
Cp speciﬁc heat
Ct coefﬁcient in jet penetration correlation
CH Constant of Mach disk width correlation
CFD computational ﬂuid dynamics
CNG compressed natural gas
D nozzle exit diameter
D
i coefﬁcient of molecular diffusivity
DI direct injection
DNS direct numerical simulation
H
2 hydrogen
Hdisk Mach disk height
IC internal combustion
K coefﬁcient in shock spacing correlation
K
m kinematic momentum ﬂux
LES large eddy simulation
L
s shock cell spacing
_M momentum ﬂux
Ma Mach number
Ma1 Mach member at the nozzle exit
Madisk Mach number at the Mach reﬂection
MaA shock upstream Mach number
Maj jet fully expanded Mach number
NPR nozzle pressure ratio
P pressure
P
0 upstream (nozzle) total pressure; injection
pressure
P∞ static ambient pressure
PA shock upstream pressure
PB shock downstream pressure
PIV particle image velocimetry
SGS sub-grid scale
t time after start of injection
t
0 nominal integral time scale
T temperature
T0 upstream total temperature
T∞ ambient temperature
U1 nozzle exit velocity
UA shock upstream velocity
Wdisk Mach disk width
WALE wall-adapting local eddy-viscosity
X mole fraction
Y
c scalar mass fraction
Yi mass fraction of the i th species
Z axial distance from the nozzle exit
Ztip jet tip penetration
Greek symbols
b angle of inclination in shock
G scaling constant
g ratio of speciﬁc heats
hg Taylor microscale
hk Kolmogorov length scale
hL integral length scale
q shock deﬂection angle
r density
r∞ ambient density
l jet wavelength
m dynamic viscosity
u vorticity magnitude
international journal of hydrogen energy 41 (2016) 6544 e6566 6545

<!-- PDF_PAGE: 3 -->

Direct injection (DI) of gaseous fuels into the engine cyl-
inder after intake valve closure [1e5] is believed to be the most
preferable fuelling approach for advanced gaseous-fuelled
engines. This is because DI can overcome the volumetric ef-
ﬁciency losses that occur with port fuel injection [1e3]. Such
losses are associated with the characteristically low densities
of gaseous fuels and the long injection duration required that
inevitably displaces air during the intake stroke, particularly
with hydrogen port fuel injection. In contrast, it has been
shown that hydrogen DI can lead to the same, or even higher,
volume-speciﬁc power than that of conventional gasoline
engines [1]. Moreover, the degree of in-cylinder mixture ho-
mogeneity or stratiﬁcation at the time of ignition can be
attuned by various DI strategies [3e5]. Typically high pres-
sures are applied for DI fuelling in order to achieve high fuel
mass ﬂow rate and consequently rapid fuel-air mixing,
particularly with late injection strategies [1,3e5]. High injec-
tion pressures result in formation of turbulent under-
expanded fuel jets after the nozzle exit [3e5]. Consequently,
fundamental understanding of the gas dynamics and sonic/
mixing characteristics of under-expanded jets formed upon
hydrogen injection from the mm-size holes of typical injectors
is indispensable for knowledge and technology transfer that
will enable the development of new more efﬁcient high-
pressure DI gaseous-fuelled engines.
Under-expanded jets
Near-nozzle shock structure
The characteristics of a gaseous jet issuing from a circular
nozzle are highly dependent on the ratio of the upstream
(nozzle) total pressure ( P
0) to the ambient static pressure ( P∞),
speciﬁcally the nozzle pressure ratio (NPR). Based on NPR, jets
can be characterised as subsonic, moderately under-
expanded and highly under-expanded [6,7]. Hydrogen and
methane jets with NPR /C21 4 are considered to be highly under-
expanded. As illustrated schematically in Fig. 1 for an under-
expanded jet, Prandtl-Meyer expansion fans form at the
nozzle lip. Weak compression waves are formed by reﬂection
of the Prandtl-Meyer fans from the jet boundary and form the
intercepting shock. The latter shock is ended by a marginally
curved strong normal shock, the Mach disk [6,7], which
together shape the ﬁrst shock cell. On a two dimensional
plane the intercepting oblique shock and the Mach disk merge
at the triple point and produce a reﬂected shock and a slip line
[6e8]. The slip line shows the existence of an annular shear
layer within the jet volume. Highly under-expanded jets have
two annular shear layers, the inner and outer layer [9,10]. The
inner shear layer lies between the high-velocity gas near the
jet boundary and the low-velocity jet core, while the outer
shear layer (or the mixing layer) lies within the jet boundary
and the surrounding medium.
The cause of the Mach disk formation and generally the
complex near-nozzle shock structure can be explained by
solving the gas dynamics conservation equations deriving
‘shock-jump relations’ that relay the downstream conditions
in an oblique shock to its upstream. According to this, there
are two major reﬂections that may occur in all types of ﬂows
(steady, quasi-steady and unsteady), regular and Mach re-
ﬂections [8]. Fig. 1 also includes a schematic of the Mach
reﬂection process. If the angle of inclination b passes a critical
value (that is a function of the upstream Mach number and the
ratio of speciﬁc heats) then the regular reﬂected shock cannot
correct the ﬂow direction downstream of the intercepting
oblique shock and its locus does not reach the pressure axis
[8]. Therefore, a near-normal shock forms which allows the
triple point to move away from the wall or the symmetry
plane. This process is called Mach reﬂection. Similarly to the
ﬂow upstream, the ﬂow after the Mach reﬂection is parallel to
the wall (or a symmetry plane). The Mach disk in highly under-
expanded jets is a Mach reﬂection from the nozzle symmetry
plane. A vortex sheet (slip line) separates the ﬂow stream
processed by the reﬂected and near-normal shocks (which are
supersonic and subsonic, respectively). Density, velocity and
entropy are discontinuous across the slip line but pressure
and streamline deﬂection must be continuous [8]. This may
trigger a turbulent mixing process within the jet core [10]. For
relatively high levels of under-expansion, e.g. NPR /C21 8, the
subsonic core downstream of the Mach disk accelerates
quickly and becomes supersonic again. This then gives rise to
a second shock cell that may be similar to the ﬁrst shock cell
and contains a normal shock similar to the Mach reﬂection [7].
Mach disk dimensions
The dimensions of the Mach disk in under-expanded jets, i.e.
the distance between the disk and the nozzle exit (on the
Fig. 1 e (a) Schematic of the near-nozzle shock structure of under-expanded jets (based on the visualisation presented by
Crist et al. [6]). (b) Schematic of Mach reﬂection and its corresponding shock locus (detail of dashed circle shown in (a)). (c)
Diagram of ( q, P) based on visualisation presented by Hornung [8] and in reference to points A, B, C and D shown in (b).
international journal of hydrogen energy 41 (2016) 6544 e65666546

<!-- PDF_PAGE: 4 -->

nozzle axis), termed the Mach disk height Hdisk,a n dt h e
distance of the two triple points, termed the Mach disk
width Wdisk, have both been the subject of several experi-
mental and computational studies over the past 50 years,
mainly for aeronautical applications. The primary impor-
tance of these parameters comes from the fact that they can
provide signiﬁcant information regarding the location and
size of the annular shear layers and hence mixing charac-
teristics of this type of ﬂow. These parameters may also be
used for direct comparison of various under-expanded jets
and also for validation of their computational predictions.
In an early attempt Crist et al. [6] used a hot-shot wind-
tunnel facility and Schlieren to study the near-nozzle shock
structure and to measure the H
disk for a variety of gases
including Nitrogen, Argon, Helium and CO 2. They concluded
that the relation between NPR and Mach disk height could be
described by:
Hdisk
D ¼ CH
ﬃﬃﬃﬃﬃﬃ
P0
P∞
s
(1)
Several other researchers attempted to estimate the con-
stant of Equation (1). For instance, Ashkenas and Sherman
[11], Velikorodny and Kudriakov [12] and Vuorinen et al. [13]
suggested CH values of 0.67, 0.63 and 0.62, respectively. The
authors of the current work found that for hydrogen jets with
values of NPR up to 10, C
H had a value of ~0.65 [14]. An average
value of CH z 0.71 has been measured for hydrogen jets with
NPR in the range 8.5 e70 [14]. An empirical correlation com-
parable to Equation (1) can also be used to estimate the Mach
disk width with a respective constant CW. Various attempts
have also been made to obtain a generalised value of CW for
under expanded jets [12,13], however, because of the notice-
ably greater non-linearity between Wdisk and NPR in compar-
ison to that of Hdisk and NPR, there is still not a unique
correlation or, at least, a widely accepted value of CW [13].
Core shock cells
The spacing length of the core shock cells is another impor-
tant parameter in under-expanded jets. Depending on NPR, a
number of shock cells may form within the jet core to allow
the static pressure inside the jet to decrease gradually to that
of the surrounding ambient. The shock cells are formed by
reﬂection of radially propagating oblique shocks and expan-
sion fans from the jet boundary. The reﬂection process may be
repeated several times until the associated shocks are dissi-
pated by the highly turbulent mixing region (typically by
merging of the inner and outer shear layers). These frequent
reﬂections have a quasi-periodic nature [15e17]. Studies of the
near-nozzle shock structures have been done primarily to
investigate the aeroacoustics involved in the physics of under-
expanded jets, especially the level of sound emitted (screech
tone) from the expansion process due to the quasi-periodic
nature of the shock cells [16,18]. Similarly to the dimensions
of the Mach disk, the spacing of the shock cells is also useful
for comparison and model validation purposes.
Emden [19] carried out the ﬁrst quantitative experimental
study of the near-nozzle shock cell structures using schlieren
visualisation. He noticed that the jets had a periodic structure
with a speciﬁc wavelength. Using various nozzle designs, he
discovered that the wavelength l could be expressed as a
function of the nozzle exit diameter D and NPR:
l ¼ KD
ﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ
NPR /C0 1:9
p
(2)
The shock cell spacing L
s was found to be the longest
wavelength. This resulted in K values in the range of 0.77e1.02
depending on nozzle type, with a mean value of 0.88. Prandtl
[20] studied theoretically the shock cell spacing by a linear
vortex sheet jet model and by developing an approximate
solution. He considered slight perturbations about a steady
state and estimated a mean value of K of 1.2. This was too high
in comparison to Emden 's one [19]. Finally, after attempts by
various researchers, a complete vortex-sheet shock-cell so-
lution for moderately under-expanded jets was derived by
Pack [18]:
L
s ¼ KD
ﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ
Ma2
j /C0 1
q
(3)
where K is in the range of 1.15 e1.3 and Maj is the fully
expanded jet Mach number. By assuming K ¼ 1.22, g ¼ 1.41 and
using Bernoulli's equation to replace the Mach number by NPR
in Equation (3), Pack [18] derived the following correlation for
shock cell spacing:
Ls ¼ 2:695D
ﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ
NPR0:291 /C0 1:205
p
(4)
The vortex sheet shock-cell model used by Pack [18] is not
valid apart from where the mixing layer is thin, i.e. near the
nozzle exit. Tam and Tana [21] and Tam et al. [22] developed
and extended a linear shock-cell solution for jets with a real-
istic mean ﬂow proﬁle using the method of ‘multiple-scales
expansion’. They concluded that a good approximation to the
spacing of the shock cell structure could be given by:
L
s ¼
pD
ﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ/C16
Ma2
j /C0 1
/C17r
2:405 (5)
For under-expanded jets of relatively low Reynolds number,
as well as for micro jets, smaller cell spacing values than those
derived by Equation (5) have been reported in the literature
[23e25]. Thicker boundary layers due to low Reynolds numbers
and associated viscous effects were suggested as possible
causes for this discrepancy. For instance, using schlieren im-
aging of under-expanded jets issued from micro nozzles with
diameters in the range 100 e1000 mm, Phalnikar et al. [25]
suggested an empirical correlation for shock cell spacing as
follows:
L
s ¼ D
/C16
0:57Ma2
j /C0 0:15
/C17
(6)
This leads to about 10 e30% difference in Ls when
compared to Equation (5).
Jet penetration
The jet 's tip penetration Z tip is the key parameter of under-
expanded fuel jets when it comes to mixture formation in
engines. The jet penetration under conditions similar to those
prevailing in DI gaseous-fuelled engines (under-expanded
with Reynolds number of the order 10
5e106) has been found to
obey a linear dependency on the square root of time [26e28].
Turner [29] developed a model to approximate the geometry of
international journal of hydrogen energy 41 (2016) 6544 e6566 6547

<!-- PDF_PAGE: 5 -->

a gaseous jet as a spherical head vortex and a quasi-steady jet
region that conveys the momentum. Hill and Ouellette [30]
employed this model to develop an analytical relationship
for the tip penetration of under-expanded jets. Speciﬁcally, it
was assumed that momentum is constantly supplied through
the nozzle oriﬁce and is passed between the quasi-steady re-
gion and the head vortex. Hill and Ouellette [30] used formu-
lations derived by Ricou and Spalding [31] for the entrainment
of low momentum ambient air and suggested a correlation for
the jet tip penetration Z
tip as:
Ztip ¼ G
 _M
r∞
!0:25
t0:5 (7)
where _M is the momentum ﬂux supplied by the nozzle and G is
a scaling constant which is a function of the entrainment
coefﬁcient and the ratio of the jet 's head vortex diameter to its
tip penetration [28]. The value of G for turbulent under-
expanded jets issued from round nozzles is about 3 [27].
By assuming self-similar velocity proﬁle and employing
conservation of momentum, Abraham [32] used an expression
for centreline velocity of turbulent jets developed originally by
Schlichting [33] in order to derive an expression for the jet tip
penetration (Z
tip) as follows:
Ztip ¼
ﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ
3Cf
4pCt
/C18
Km
r1
r∞
/C19 0:5
t
s
(8)
where Km ¼ A1U1
2 is the kinematic momentum ﬂux of the
round jet at the nozzle exit, Cf is a certain fraction of the local
steady centreline velocity and Ct is a constant that relates the
jet diffusivity to the jet kinematic momentum [32,33].
Different combinations of Cf and Ct have been suggested in the
literature. For example, Song and Abraham [34] employed
Ct ¼ 0.0113 and Cf ¼ 0.305 and successfully managed to
reproduce the penetration curve of a round jet.
Present contribution
The near-nozzle shock structure and mixing characteristics of
under-expanded jets have been subject to various experi-
mental investigations since the mid-1950s, using predomi-
nantly air or nitrogen issued from relatively large aerospace-
type nozzles. Recently large eddy simulation (LES) was
employed to investigate under-expanded methane and nitro-
gen jets [13,35]. However, very limited experimental and
computational studies are available in the literature on under-
expanded hydrogen and methane jets and speciﬁcally with
respect to applications in DI gaseous engines[36e41]. Recently,
the authors of the present paper used LES to investigate the
near-nozzle shock structure and mixing characteristics of
highly under-expanded hydrogen and methane jets with
NPR ¼ 8.5e70 issuing from a circular nozzle into a low ambient
pressure (P
∞ z 1b a r )[14,42]. The present computational work
aims to extend the previous studies on under-expanded
hydrogen and methane jets by investigating effects of
ambient pressure on the key characteristics of this type of
ﬂow. To the best of the authors’ knowledge the current study is
the ﬁrst to employ LES in order to study sonic and mixing
characteristics of under-expanded hydrogen and methane fuel
jets under various NPR values and ambient pressures
(including elevated engine-like ambient pressures). The main
objectives of the current work can be summarized as follows:
/C15 Investigate the transient formation features of the Mach
disk and the near-nozzle shock structures with hydrogen
and methane fuels in relation to NPR.
/C15 Conduct quantitative and comparative studies on the
initial transient tip vortices (initial vortex ring) and their
effect on the mixing characteristics and shear layer for-
mation in hydrogen and methane under-expanded jets.
/C15 Study the effect of elevated ambient pressure under con-
stant NPR on the near-nozzle and mixing characteristics of
hydrogen jets.
/C15 Formulate empirical correlations for shock cell spacing and
jet tip penetration of under-expanded hydrogen and
methane jets.
Methodology
Numerical approach
The numerical approach employed in order to conduct LES
studies has been described in preceding publications by the
current authors [14,42]. Nevertheless, for the immediate
beneﬁt of the reader, a brief description is also included here.
Preconditioned compressible formulation of the governing
equations of viscous ﬂows (mass, momentum and energy
conservations) as well as a species transport equation were
solved using the ﬁnite-volume methodology within the STAR-
CCMþ
® code [43e45]. A second-order implicit time marching
method was combined with a central differencing scheme for
convective ﬂuxes in order to discretize the aforementioned
partial differential governing equations and produce a line-
arized system of equations [44]. The matrix of the linearized
system of equations was then solved simultaneously (coupled
approach [45]) and by using the Gauss-Seidel iterative tech-
nique in conjunction with an algebraic multigrid (AMG)
method [43e45]. A modiﬁed version of the advection upstream
splitting method (AUSM
þ-up) [46] was applied in order to ex-
press the inviscid ﬂuxes. AUSM þ-up is accurate and robust in
solving ﬂuid ﬂows containing arbitrary range of velocity
magnitude and particularly high speed ﬂows that contain
extreme discontinuities such as shock waves [46]. Since direct
numerical simulation (DNS) is not feasible for the complicated
high-speed ﬂow that is investigated in this work, LES was
employed instead. For LES the governing equations are ﬁltered
so that turbulence scales greater than a ﬁlter size (typically
associated with the grid resolution) are resolved directly and
the effect of scales smaller than that are accounted for by
means of sub-grid scale (SGS) modelling [47]. In the present
study the wall-adapting local-eddy viscosity (WALE) SGS
model which is based on the square of the velocity gradient
tensor (can take into account both shear and rotation) was
applied [48]. In comparison to the classical Smagorinsky model
[47], the WALE model produces zero eddy viscosity in case of a
pure shear (may occur in free jets) that makes it capable of
reproducing turbulent transitional processes more accurately
through the growth of unstable modes [48].
international journal of hydrogen energy 41 (2016) 6544 e65666548

<!-- PDF_PAGE: 6 -->

The molecular mixing rate of the species was taken into
account using the Chapman-Enskog theory for gaseous diffu-
sion [49]. Speciﬁcally, a coefﬁcient of molecular diffusivity Di
was deﬁned as the binary diffusivity of an air-hydrogen or air-
methane system [14,49]. The coefﬁcient of molecular diffu-
sivity Di was calculated to be 7.942 $10/C0 5, 1.589 $10/C0 5 and
7.942$10/C0 6 m2/s for hydrogen injection with P∞ ¼ 1, 5 and
10 bar ambient pressure, respectively. For methane, Di was
calculated to be 2.1 $10/C0 5. The dynamic viscosity was obtained
using Sutherland's law [14].
It is also noted that in addition to the present computa-
tional framework the current authors also developed an open-
source solver with fourth-order accurate temporal dis-
cretization accuracy and with the KNP central ﬂux splitting
scheme using OpenFOAM
® libraries [50], speciﬁcally for
modelling under-expanded jets [51]. A basic comparison be-
tween the results of the new open-source solver and the
STAR-CCMþ
® framework is also provided and discussed
brieﬂy in the current paper as means of further validation of
the commercial code. However, due to the very high velocity
at the nozzle exit of the under-expanded hydrogen jets, LES
modelling with the OpenFOAM
® solver required a consider-
ably low constant time step (in the order of nanosecond) to
maintain high accuracy and stability, hence within the ob-
jectives of the current study it was decided to concentrate on
the results obtained with STAR-CCM þ
®.
Simulation setup and validation
The computational setup and its preliminary validation pro-
cess have been discussed in earlier published studies by the
current authors [14,42]. However, a brief description of the
setup and validation are also included here for completeness
with some additional discussion.
Computational setup
Fig. 2 presents the computational domain. This consisted of a
high pressure tank that was linked to a low pressure air-
containing chamber by a converging nozzle with exit diam-
eter D ¼ 1.5 mm. The geometry and dimensions of the
converging nozzle were obtained from an experimental test
case available in the literature [40] to enable validation work.
The current work examined under-expanded hydrogen
(NPR ¼ 8.5, 10) and methane (NPR ¼ 8.5) jets issued into
quiescent air ambient with various pressures. The pressure of
the ambient was kept constant at P
∞ ¼ 98.37 kPa for the cases
with NPR ¼ 8.5. For hydrogen jets with NPR ¼ 10, in addition to
P∞ ¼ 98.37 kPa, two additional elevated ambient pressures,
P∞ ¼ 491.85 and 983.70 kPa were also investigated. For con-
venience, within the rest of this paper, cases with ambient
pressures of P
∞ ¼ 98.37, 491.85 and 983.70 kPa are referred to
as cases with ~1, ~5 and ~10 bar ambient pressure, respec-
tively. For all simulations, an initial constant temperature of
295.4 K and 296 K was employed for the fuel and air containing
volumes, respectively. Following practices in the literature
[13,35,37] and also based on the discussion provided in Ref.
[14], adiabatic slip boundary conditions were assigned to the
nozzle and high-pressure tank boundaries.
A computational mesh with hexahedral elements was
created within STAR-CCM þ
®. The meshing process produced
cubic ﬁnite volume elements with identical size in all di-
mensions as shown in Fig. 2 . This resulted in a grid without
cell stretching which typically provides enhanced numerical
accuracy and also avoids the singularity linked to polar grids.
In order to capture the ﬂow details inside the nozzle, the shock
structure very close to the nozzle exit and the mixing process
downstream of the nozzle, a conical reﬁned area was imple-
mented inside the computational domain. This covered the
nozzle volume and a length of 20 D downstream of the nozzle
exit. The reﬁnement inside the nozzle volume and within a
distance of ~6.7D downstream the nozzle exit had a cell size of
~0.03 mm ( D/50), whilst further downstream it had a cell size
of ~0.06 mm. By employing a four-level grid coarsening, the
spatial resolution expanded to its largest size of 1.0 mm close
to the boundaries of the low pressure ambient. In total ~13.5 M
hexahedral cells ﬁlled the computational domain. According
to previous investigations [13,35,37] the spatial resolution
employed in the present study was considered ﬁne enough to
capture the shock waves embedded in under-expanded jets
and also to resolve adequately the level of turbulent energy of
this kind of ﬂow within reasonable computational power. A
comparison of the spatial resolution of the current study with
key scales of turbulent motion, i.e. integral (h
L), Taylor (hg) and
Kolmogorov (hk), can provide some perspective of the explicitly
resolved scales [47]. A recent experimental study of under-
expanded jets by particle image velocimetry (PIV) [52] quan-
tiﬁed integral length scales in the range hL ¼ 0.1e0.4D for
distances downstream of the nozzle exit in the range 2 De12D.
Using typical estimate processes for Taylor and Kolmogorov
scaling on the basis of hL, turbulent kinetic energy, dissipation
rate and kinematic viscosity ( e.g. see Ref. [47]), under condi-
tions of hydrogen jetting with NPR ¼ 10 ( P∞ ¼ 1 bar,
U1 z 1300 m/s), led to values of hk of the order 2 $10/C0 6 m and hg
of the order 4 $10/C0 5 m. The grid resolution of D/50 and D/25
over the two main reﬁnement volumes of the current study
was 3.0$10/C0 5 and 6.0$10/C0 5 m, respectively. This means that the
current LES framework was nominally able to resolve eddies
down to about Taylor size. Further spatial reﬁnement to
resolve scales close to Kolmogorov would require a spatial
resolution ﬁner by more than one order of magnitude which
would make running times and analysis impractical over
typically available computational resources.
Since modelling transient compressible in-nozzle ﬂows
requires very small time steps (usually of the order of nano-
seconds and mainly because of the existence of high density
gradient inside the nozzle volume) the common practices in
the literature is to omit it by applying an arbitrary pressure
gradient inside the nozzle [13,37]. However, in the present LES
study, the in-nozzle transient process was taken speciﬁcally
into the account. The simulations started from a rest condi-
tion where the entire high-pressure tank and a very small part
of the converging nozzle volume (up to ~1.4 D upstream the
nozzle exit) were ﬁlled by the gaseous fuel. Quiescent air
occupied the low-pressure chamber and the remaining sec-
tion of the nozzle volume. The nominal integral time scale t
0
of an under-expanded gaseous jet was calculated to be
~6.2$10/C0 7 s and ~1.8 $10/C0 6 s for under-expanded hydrogen and
methane jets, respectively [13,14]. A time-step in the range of
1$10/C0 9e5$10/C0 9 s was used at the early stages of the simulation
(for modelling the in-nozzle transient ﬂow); this was then
international journal of hydrogen energy 41 (2016) 6544 e6566 6549

<!-- PDF_PAGE: 7 -->

gradually increased to a value in the range 2 $10/C0 8e5$10/C0 8 s
depending on the injection pressure. For the cases with
elevated ambient pressure (at constant NPR), it was noticed
that a lower time-step had to be used in order to maintain
stability of the solution. This was attributed to the existence of
higher level of momentum gradients inside the nozzle. The
nominal integral time scale of the ﬂow was, in any case, 10
times larger than the aforementioned time steps; this made
them satisfactory for capturing the turbulent temporal ﬂuc-
tuations at the expense of practical computational cost.
Model validation
As discussed comprehensively in Refs. [14,42] in order to vali-
date the current computational framework ﬁrst a simulation of
hydrogen injection with NPR ¼ 10 (P
∞ z 1 bar) was setup based
on the experimental work of [40]. Mach disk dimensions (its
height and width), as well as the reﬂected shock angle, were
predicted by LES very close to values that could be extracted
from the Schlieren images of[40]. The present LES investigation
predicted higher values for the Mach disk height and width by
1.3% and 3.0%, respectively (3.09 mm and 1.34 mm) compared to
those stated in Ref. [40] (3.05 mm and 1.30 mm, respectively). In
further agreement with[40], the present LES study predicted the
reﬂected shock (at the triple point) to be inclined ~28
/C14 against the
nozzle centreline axis. The reﬂected shock angle for the
methane test case (NPR¼ 8.5) was measured to be ~28.5
/C14 , which
in addition to the Mach disk height ( Hdisk z 1.9D) were in
agreement with the recent work of Vuorinen et al. [13,37] on a
nozzle of 1.4 mm dimeter, NPR ¼ 8.5 and under-expanded ni-
trogen and methane jets. Similarly to the experimental obser-
vations of [40], it was also seen that hydrogen and air were
mixing outside of the intercepting shock, before the Mach
reﬂection. This means that not all of the incoming hydrogen
passed through theMach disk surface. For methane, similarly to
[37], mixing did not occur before theMach reﬂection. The mixing
process at the boundary of the intercepting shock in under-
expanded jets is discussed further later in the current paper.
In Refs. [14,42] it was shown that jet tip penetration curves
of the hydrogen and methane under-expanded jets issued into
P
∞ ¼ 1 bar collapsed onto a single trend line by applying an
empirical relationship proposed by Ouellette and Hill [27]
(similarly to the under-expanded nitrogen jet modelled by
Vuorinen et al. [13]). Fig. 3 shows that the penetration curve of
the hydrogen jets issued into the elevated ambient pressures
of P
∞ ¼ 5 bar and 10 bar also collapsed onto a single line using
the relationship of [27].
Results and discussion
Transient shock dynamics and jet development
The early stages of near-nozzle shock development and Mach
disk formation is presented in Fig. 4 for the hydrogen injection
Fig. 2 e Left: The domain conﬁguration and dimensions. Right-top: Zoomed view of the reﬁned areas. Right-bottom: Nozzle
proﬁle and its dimensions based as provided by Ruggles and Ekoto [40].
international journal of hydrogen energy 41 (2016) 6544 e65666550

<!-- PDF_PAGE: 8 -->

case with NPR ¼ 10 issued into air ambient at P∞ z 1 and 5 bar.
Although the transient stages were slightly different, for both
cases the Prandtl-Meyer expansion fans formed at the nozzle
lip just after hydrogen 's entrance into the domain. At the
beginning of the simulation process, a subsonic jet started
issuing from the nozzle exit and soon after it turned into a
moderately under-expanded jet with Ma
1 z 1 (at t z 8 ms for
the case with P∞ z 1 bar). At this condition the expansion fans
reﬂected from the jet boundary and formed the compression
waves (fans) which consequently shaped the curvy inter-
cepting shocks. The initial shock cell formed by the inter-
cepting shocks and the intersecting expansion and
compression fans (see the 8 ms snapshots of Fig. 4 ). The in-
nozzle ﬂow exhibited a noticeable transient behaviour and
when the nozzle exit pressure passed the threshold of P
1/
P∞/C21 2a t t z 12e13 ms (for P∞ z 1 bar) the jet became highly
under-expanded with a tiny Mach disk. This means that the
intersecting fans of the ﬁrst cell were not ‘strong enough ’ to
correct the ﬂow direction and, as discussed earlier, the exis-
tence of a Mach reﬂection was indispensable. The width of the
Mach disk then grew gradually until it reached quasi-steady
dimensions. This is attributed to the gradually increasing
upstream Mach number during the initial transient process. In
fact, increasing Ma
1 would increase the overall deﬂection
angle of the oblique shocks of the ﬁrst cell, therefore a larger
portion of the ﬂow should pass through a Mach reﬂection, i.e. a
wider Mach disk would be formed [8]. The ﬂuctuating nature of
the Mach disk dimensions (before its settlement at a ﬁnal
semi-steady location), has been attributed to the ﬂuctuating
behaviour of the upstream ﬂow of the Mach reﬂection [14,53].
Comparison between jets with different ambient pressures
in Fig. 4 shows that higher ambient pressure resulted in faster
formation of the Mach reﬂection ( Mach disk). A difference of
2e3 ms was observed in the formation of the Mach disk
between the hydrogen jets presented in Fig. 4 . It is worth
mentioning that the transient process of the near-nozzle
shock development for the hydrogen jet with NPR ¼ 10 is-
sued into the ambient with P
∞ z 10 bar (not shown here)
revealed a similar behaviour to the jet with P∞ z 5 bar but
exhibited a Mach reﬂection ~1 ms earlier. Therefore, it can be
concluded that higher ambient pressure under a ﬁxed value of
NPR may result in faster near-nozzle shock development and
shorter Mach disk settlement time. Shorter temporal and
spatial ﬂuctuations around the ﬁnal steady values were found
for the Mach disk dimensions by increasing the ambient
pressure under ﬁxed NPR. The difference between the initial
transient shock formation in jets with similar NPR but
different P
∞ is due to the difference in the aforementioned in-
nozzle transient process [14]. A relatively higher in-nozzle
momentum and density would result in shorter transient
conversion from subsonic to sonic/supersonic ﬂow at the
nozzle exit that would advance the formation of the Mach
reﬂection.
The hydrogen jet with NPR ¼ 10 and P
∞ z 1 bar in Fig. 4
showed similar behaviour to the hydrogen jet of NPR ¼ 8.5
with P∞ z 1 bar in Ref. [14]. However, it is noted that the
methane jet with NPR ¼ 8.5 and P∞ z 1 bar exhibited slightly
different behaviour. Widely spaced initial intercepting shocks
were noticed that did not get close during the transient pro-
cess and formed a wide Mach disk from the very beginning of
the injection process. Moreover, it was observed that for the
hydrogen jet with NPR ¼ 30 and P
∞ z 1 bar the transient shock
development progressed similarly to that of the methane jet
with NPR ¼ 8.5 ( P
∞ z 1 bar), i.e. with the formation of a wide
Mach disk from the very beginning [14]. At a constant incli-
nation angle, jets with higher MaA or lower ratio of speciﬁc
heats ( g) would produce more ﬂow deﬂection which means
that formation of a wider Mach reﬂection is expectable [8].
Methane has a lower g than hydrogen and the hydrogen jet
with NPR ¼ 30 had relatively higher MaA [14]. The transient
evolution of the Mach disk dimensions and the near-nozzle
shock structure of both methane and hydrogen jets are com-
parable with the recently published schlieren observations of
Rogers et al. [54].
Initial jet tip vortices
Figs. 5 and 6 show the initial stages of the hydrogen jet
(NPR ¼ 8.5, 10 respectively) penetrating into the chamber with
P∞ z 1 bar. Speciﬁcally, these ﬁgures present mass fraction
contours and the line integral convolution [55] of velocity
vectors for a period up to t z 16t0. It can be seen that the
spherical bow shock in front of the jet boundary propagated
with relatively high velocity magnitudes ranging
600e1000 m/s. Τhe air in front of the jet boundary (see mass
fraction contours) accelerated because of the pressure waves
emitted from the jet. The speed of the air upstream was higher
than the speed of sound in air with the initial ambient tem-
perature (οf order 300 m/s). This was due to rapid compression
which could increase the temperature of the air ahead to
values of 500 e600 K (H
2 with NPR ¼ 8.5e10, P∞ z 1 bar).
Temperature rise would increase the speed of sound signiﬁ-
cantly. This rapid acceleration resulted in comparable velocity
magnitudes of the jet tip and its adjacent air, as seen in the
Fig. 3 e Variation of a modiﬁed jet tip penetration (based on
relationship of [27]) versus a normalized time parameter.
Comparison between hydrogen and methane jets studied
in the current LES study with a nitrogen jet available in the
literature [13].
international journal of hydrogen energy 41 (2016) 6544 e6566 6551

<!-- PDF_PAGE: 9 -->

Fig. 4 e LES prediction of transient development of the near nozzle shock structure and Mach disk in under-expanded
hydrogen jets with NPR ¼ 10 and P∞ ≈ 1 and 5 bar.
international journal of hydrogen energy 41 (2016) 6544 e65666552

<!-- PDF_PAGE: 10 -->

velocity ﬁelds of Figs. 5 and 6 where the H 2 jet tip cannot be
clearly identiﬁed; at the boundary of the jet and ambient air
there is a contact discontinuity [56]. The ﬂow in front of the
bow shock was almost stationary. This spherically propa-
gating shock could have signiﬁcant inﬂuence on the mixing
process by enhancing air entrainment.
Figs. 5 and 6 also show another important feature of the
transient under-expansion process, the tip vortices. This
type of behaviour normally occurs when a low density gas is
issued into a high density environment or a cold gas is
injected into hot ambient [56,57]. This feature of enhanced
turbulent mixing through developing vortical ﬂows plays an
important role in the mixing process of under-expanded
jets. It is worth mentioning that the tip vortex is a three
dimensional toroidal feature, often called ‘vortex ring ’,a n d
may include various types of vortices [53]. The tip vortex
shown in Figs. 5 and 6 formed in the course of rolling up of
the jet 's turbulent interface close to the edge of the near-
nozzle shock structure; see the snapshots at t z 16.1t
0 of
the integral convolution. The hydrogen jets showed fairly
similar transient behaviour of their tip vortices. However,
the initial sign of tip vortex formation appeared earlier for
the jet with higher NPR. Speciﬁcally, the early tiny tip
vortices appeared at t z 9.6t
0 and t z 11.3t0 for NPR ¼ 10 and
8.5, respectively.
Similarly to those ﬁgures, the transient formation process
of the tip vortices for the hydrogen jet with NPR ¼ 10 issued
into air of P∞ z 10 bar is presented in Fig. 7. It was found that
the jets with analogous NPR exhibited fairly similar initial
transient evolution for their tip vortices. Also comparison of
the initial penetration of jets with similar NPR but different
ambient pressures showed almost identical behaviour in Figs.
6 and 7 . However, slightly higher maximum velocity was
noticed for the jet injected into P
∞ z 1 bar and the tip vortices
recirculated slightly faster compared to the jet injected into
P
∞ z 10 bar, e.g. compare the t z 12.9t0 snapshots in Figs. 6
and 7 . On the other hand, greater hydrogen mass fraction
was observed within the recirculation area of the jet injected
into P
∞ z 10 bar. Therefore, it may be summarised that the
relatively faster tip recirculation of the jet with P∞ z 1 bar was
because of the lower mass within its recirculation area
compared to that of the jet with P
∞ z 10 bar. An important
conclusion from Figs. 5 e7 is that for a particular gas the
transient evolution of the tip vortices is mostly affected by
NPR rather than the level of the incoming momentum ( i.e.
injection pressure).
Fig. 5 e Transient jet development of hydrogen (NPR ¼ 8.5 and P∞ ≈ 1 bar) tip vortices ( t0 ≈ 6.2·10¡7). First and third rows: H 2
mass fraction ( YH2); Second and fourth rows: Line integral convolution of the velocity vectors.
international journal of hydrogen energy 41 (2016) 6544 e6566 6553

<!-- PDF_PAGE: 11 -->

Similar type of tip vortex formation was also noticed in Ref.
[53] for an under-expanded nitrogen jet, albeit with the
vortices shifted noticeably further downstream compared to
the hydrogen jets of the current study. This could be associ-
ated with the higher nozzle exit velocity of hydrogen
(~1300 m/s) compared to that of nitrogen (~330 m/s). In order
to clarify this, the initial transient steps of the methane jet
(NPR ¼ 8.5, P
∞ z 1 bar) were investigated as shown in Fig. 8 .
For this condition the methane jet exited from the nozzle with
a velocity of U
1 z 450 m/s which was much closer to that of
nitrogen in Ref. [53] than hydrogen here. Similarly to [53], Fig. 8
reveals that, unlike hydrogen, the methane jet exhibited a
relatively smaller initial ﬂow recirculation which conse-
quently formed the jet tip vortices after the Mach disk location.
The temporal intervals in Figs. 5e8 are based on t
0 which was
~3 times larger for the methane jet than that of hydrogen.
Therefore, it is clear that the jet tip vortices were formed
considerably earlier for hydrogen than for methane. For the
hydrogen jet with NPR ¼ 8.5 the fully recirculating tip vortices
were observed within 7.0 ms whereas for the respective
methane jet these vortices were noticed within 20 ms. The
mass ﬂow rate of the methane jet with NPR ¼ 8.5 was 2.3 e3.0
times higher than those of the hydrogen jets with NPR ¼ 8.5
and 10. Therefore, the difference in the evolution of the tip
vortices can only be an effect of the signiﬁcant differences in
nozzle exit velocity between the methane and hydrogen jets.
The higher velocity magnitude of hydrogen would also pro-
duce a noticeably higher radial velocity compared to that of
methane. As presented in Fig. 8 for methane, a tiny recircu-
lation was formed at t z 5.5t
0. However, the local velocity was
not high enough to form a dominant vortex and, in turn, this
initial recirculation moved downstream and got linked to the
jet's penetration. However, at t z 11.1e13.8t0, the tip recircu-
lation became relatively strong and formed noticeable tip
vortices downstream of the Mach disk.
The aforementioned difference in the tip vortex evolution
between methane and hydrogen jets may affect signiﬁcantly
the fuel-air mixing upstream of the Mach disk location. The
current authors found previously that, unlike hydrogen,
methane did not exhibit any mixing before the Mach disk (at
the boundary of the intercepting shock) [14]. Based on this and
also some other relevant observations [13,37,40], it may be
concluded that the relatively high level of turbulence at the
nozzle exit of hydrogen jets triggered the G€ortler vortices [58]
and thus increased the instability at the boundary of the
curved intercepting shock. However, the velocity ﬁelds in Figs.
5e8 also show that velocity magnitudes as high as
U z 1600 m/s can exist at the boundary of the intercepting
Fig. 6 e Transient jet development of hydrogen (NPR ¼ 10 and P∞ ≈ 1 bar) tip vortices ( t0 ≈ 6.2·10¡7). First and third rows: H 2
mass fraction ( YH2); Second and fourth rows: Line integral convolution of the velocity vectors.
international journal of hydrogen energy 41 (2016) 6544 e65666554

<!-- PDF_PAGE: 12 -->

shock (upstream of the Mach reﬂection) in hydrogen jets due
to the presence of strong tip vortices. Therefore, it can be
further concluded that, in addition to the G€ortler-vortices-
induced instabilities, the transient tip vortices may also
contribute signiﬁcantly to the ﬂow instabilities at the bound-
ary of the intercepting shock and promote hydrogen-air
mixing before the Mach disk location.
It is noted here that comparable behaviour was found be-
tween the evolution of the transient near-nozzle shock
structure and transient vortex ring of under-expanded jets
between the current second-order accurate STAR-CCM þ
®
framework and the aforementioned newly developed fourth-
order accurate OpenFOAM ® solver [51]. Figures A.1 eA.2 in
the Appendix show a direct comparison between the two
computational frameworks for an under-expanded nitrogen
jet with NPR ¼ 8.5 issued into a nitrogen ambient with
P
∞ ¼ 1 bar. In addition to the order of the temporal dis-
cretization, the turbulence model (one-equation LES model for
the OpenFOAM
® solver) and the ﬂux-splitting method [51]
were also different features between the two simulations.
Although very close jet behaviour was captured by both codes,
the OpenFOAM
® solver with higher order accuracy was able to
provide a sharper representation of the shock structure and
vortex ring rolling-up process.
Quasi-steady shock structure
Near-nozzle shock characteristics
In order to obtain better understanding of the near-nozzle
shock structure in under-expanded jets it is important to
study this region under semi-steady conditions. Fig. 9 shows a
direct comparison between the near-nozzle shock structure of
hydrogen and methane jets (NPR ¼ 8.5 and P
∞ z 1 bar) at
t z 161t0. The near-nozzle structure reached a semi-steady
condition far before this time. The transverse and axial ve-
locity proﬁles of the methane and hydrogen jets on the ver-
tical plane of Fig. 9 are illustrated in Fig. 10 . The red dashed
lines in Fig. 9 show the border of the inner and outer shear
layers. The dashed ovals in the same ﬁgure show the origin
where the outer shear layer starts forming. It is clear that for
hydrogen the origin of the outer shear layer was close to the
boundary of the intercepting shock at about half Mach disk
height downstream of the nozzle exit. For methane, this origin
was located after the Mach disk. Direct comparison between
Fig. 10 and Figs. 5 and 8 revealed that the location of the
centres of the dashed ovals were very similar to the centroids
of the initial strong jet tip vortices.
Based on these observations a mechanism is proposed for
the start of the mixing process in under-expanded jets.
Fig. 7 e Transient jet development of hydrogen (NPR ¼ 10 and P∞ ≈ 10 bar) tip vortices ( t0 ≈ 6.2·10¡7). First and third rows: H 2
mass fraction ( YH2); Second and fourth rows: Line integral convolution of the velocity vectors.
international journal of hydrogen energy 41 (2016) 6544 e6566 6555

<!-- PDF_PAGE: 13 -->

Speciﬁcally, after the formation of a complete recirculation
(see the last velocity frames of Figs. 5 and 8 ) the tip vortices
became almost stationary while the main stream of the jet
continued penetrating. This would cause entrainment of
ambient air into the main stream of the emerging hydrogen jet
and also ‘separation’ of part of the hydrogen jet from its main
axial stream and mixing with the surrounding air. This initial
mixing forms the mixing layer or the outer shear layer in
under-expanded jets. However, the strength of the almost
stationary vortices decreased gradually and after some time
these vortices vanished entirely. The proposed mixing
mechanism can also be linked to an explanation of the mixing
process past this time. Further investigation showed that at
t z 161t
0, within the location of the former tip vortices in the
hydrogen jet ( i.e. those that vanished completely), the jet ve-
locity was as high as U z 150 m/s and remained within this
order for the 0.3 ms injection duration studied. Therefore, the
proposed mixing mechanism can be completed by
Fig. 8 e Transient jet development of methane (NPR ¼ 8.5 and P∞ ≈ 1 bar) tip vortices ( t0 ≈ 1.8·10¡6). First and third rows: CH 4
mass fraction ( YCH4); Second and fourth rows: Line integral convolution of the velocity vectors.
Fig. 9 e Semi-steady near-nozzle shock structure at
t ≈ 161t0 for Methane and Hydrogen jets with NPR ¼ 8.5
and P∞ ≈ 1 bar.
international journal of hydrogen energy 41 (2016) 6544 e65666556

<!-- PDF_PAGE: 14 -->

considering the effect of this high velocity magnitude on the
development of the G€ortler-type instabilities. The G€ortler-type
instabilities contributed signiﬁcantly to the formation of the
outer shear layer in hydrogen jets. In contrast, for methane,
due to the ﬁnal localisation of the tip vortices (after the Mach
disk) the formation of the shear layer was affected by the Mach
reﬂection.
From Fig. 9 it can be observed that for both methane and
hydrogen, just after the Mach disk, the subsonic core of the
jet ( i.e. the volume surrounded by the slip lines) initially
expanded and then contracted rapidly. Since there was no
pressure disparity across the slip line, this expansion and
contraction behaviour did not occur due to pressure-related
mechanisms. This behaviour has been explained in Ref. [10]
through a set of schlieren and PIV images and was attributed
t ot h ed i r e c t i o no ft h et r a n s v e r s ec o m p o n e n to ft h ev e l o c i t y
ﬁeld. Similarly to [10,59], the transverse velocity graphs of
Fig. 10 show that just after the Mach disk location (Z/ D z 1.9
and 1.85 for methane and hydrogen, respectively), at 2.0 D
downstream of the nozzle exit, the ﬂow has a transverse
velocity component towards the jet boundary (positive value
of u/U
1). This was attributed to the relative concavity of the
Mach disk (see Fig. 9 ) due to the initial expansion fans at the
nozzle lip [10]. However, after a radial distance of ~0.55 D,t h e
ﬂow was turned inwards by passing through an oblique
shock which was formed by the reﬂection of the shock at the
triple point. This resulted in a transverse velocity compo-
nent towards the jet centreline. This inward ﬂow became
dominant within the volume of the inner shear layer at a
distance 2.0 De2.2D which then caused the contraction of
the jet core.
The transverse proﬁles of Fig. 10 show that, for both
methane and hydrogen, the jet ﬂow had a transverse ve-
locity component towards the boundary for distances up-
stream of the Mach disk. The normalized values of these
transverse velocities ( u/U
1) were higher for methane than for
hydrogen. Fig. 10 also shows that for distances away from
the nozzle centreline the magnitude of the transverse ve-
locity component increased. Therefore, it may be concluded
that the concavity of the Mach disk is due to gradient of the
transverse velocity component (see the lines of Z/ D ¼ 1.8 for
the transverse proﬁles of Fig. 10 ), not directly by the initial
expansion fans at the nozzle lip as suggested in Ref. [10].I n
fact, by moving away from the nozzle centreline, the direc-
tion of the velocity vector produced by the transverse and
axial velocity components would be more inclined with
respect to the nozzle centreline. This can also explain the
existence of a more concave Mach disk in the methane jet
Fig. 10 e Normalized transverse (top) and axial (bottom) velocity proﬁles upstream and downstream of the Mach disk for
Methane (left) and Hydrogen (right) jets with NPR ¼ 8.5 and P∞ ≈ 1 bar.
international journal of hydrogen energy 41 (2016) 6544 e6566 6557

<!-- PDF_PAGE: 15 -->

compared to the hydrogen jet as presented in Fig. 9 .D u et o
the higher gradient of the transverse velocity component
just before the Mach disk in the methane jet when compared
to that of hydrogen jet (see Z/ D ¼ 1.8 in Fig. 10 ), the afore-
mentioned vector was more inclined away from the nozzle
centreline of the methane jet (particularly close to the triple
points), which consequently resulted in relatively more
concave Mach disk. The axial velocity proﬁle of Fig. 10 shows
how the ﬂow accelerated and decelerated (axial component
of velocity increased and decreased) upstream and down-
stream of the Mach reﬂection. Also, the aforementioned axial
proﬁles can be used to approximate the thickness of inner
and outer shear layers. Each axial proﬁle of Fig. 10 has a
section with almost constant w/U
1 (almost vertical lines for
w/U1 > 1a n dZ /D > 1.8). It was found that the length of these
almost vertical sections represented practically 80 e90% of
thickness of the inner shear layer (depending on jet condi-
tion and downstream location). On the other hand the
thickness of the outer shear layer can be estimated as the
distance between the highest X/ D of the aforementioned
vertical section of the axial velocity proﬁles ( Fig. 10 )a n d
where w/U
1 turns into nil.
Mach reﬂection recirculation zone
To date all numerical studies based on the NaviereStokes
equations have detected recirculation zones immediately
downstream of the Mach disk [10,60,61]. However, numerical
modelling studies using Monte Carlo methods [62] and also
experimental observations [10, 63] have shown no evidence
for such ﬂow behaviour. For instance, in PIV measurements
conducted by Edgington-Mitchell et al. [10] on an under-
expanded air jet with NPR ¼ 4.2 ( D ¼ 15 mm) no recircula-
tion zone behind the Mach disk was recorded. Breakdown of
the continuum assumption of NaviereStokes equations in the
vicinity of strong shocks like the Mach disk has been sug-
gested as a possible reason for previously observed ﬂow
recirculation just downstream of the Mach disk [10].I th a s
been shown [63] that Mach reﬂection could not produce the
recirculation zone and only a ‘cap-shock ’ pattern with
adequate curvature might be able to produce a trapped vor-
tex or recirculation behind a small normal shock. As shown
in Fig. 11 the current LES study, in excellent agreement with
previous experimental observations [10, 63], did not capture
any kind of ﬂow recirculation downstream of the Mach disk
in under-expanded jets. However, in all previous numerical
studies [60,61] ﬂow recirculation was observed within the
area surrounded by the red oval in Fig. 11 .I ti sw o r t h
mentioning that all hydrogen and methane under-expanded
jets of the current study exhibited similar behaviour to what
presented in Fig. 11 . As further conﬁrmation to what was
concluded in Ref. [10], and based on the current high ﬁdelity
study, the ﬂow recirculation downstream of the Mach disk is
believed to be almost certainly an artefact of the types of
numerical approach previously used to study under-
expanded jets by other authors. It is also noted that in
agreement with the current STAR-CCM þ
® framework the
aforementioned high order accurate OpenFOAM ® solver also
did not produce any kind of ﬂow recirculation zone down-
stream of the Mach reﬂection [51].
Flow characteristics
Fig. 12 compares contours of density gradients in hydrogen
jets with NPR ¼ 10 issued into ambient with pressures
P∞ z 1 bar, 5 bar and 10 bar.
The greyscale legend of Fig. 12 is similar to that of Fig. 9 but
with different upper scales for visualisation enhancement.
Speciﬁcally, the upper limit for the jet with P
∞ z 1 bar is
jVrj¼ 2000 and for the other jets is jVrj¼ 6000. This is due to
the higher level of density gradient for the cases with higher
ambient pressures which would be masked if the same scale
was used as (existence of large zones with extremely dark
scales was avoided). The effect of the legend limits on the
visualisation quality of density gradient contours in under-
expanded jets has been discussed comprehensively earlier
and not repeated here for brevity [14,35].
Fig. 12 shows that with constant NPR and regardless of
ambient pressure, hydrogen exhibited almost identical shock
characteristics, particularly in terms of Mach disk di-
mensions. A value of C
H z 0.65 for the constant of Equation
(1) was calculated for the jets with NPR ¼ 10 under elevated
ambient pressures ( P∞ z 5 bar and 10 bar), similarly to the H 2
jet with NPR ¼ 10 and P∞ z 1 bar. Signiﬁcantly higher level of
momentum exchange (density gradient) was observed for the
jets injected into elevated ambient pressure. This can be seen
from the extremely dark regions in the contours of density
gradient presented in Fig. 12 . This was attributed to the fact
that the under-expanded jets injected into the elevated
ambient pressures had fairly higher level of momentum
(density) at the nozzle exit (to maintain a constant NPR).
Therefore, although the diffusivity of hydrogen decreased
noticeably under elevated pressures, the higher level of
incoming momentum enhanced the hydrogen-air mixing
particularly at the jet boundary after the location of the Mach
disk. The jet with P
∞ z 5 bar showed slightly wider half cone
angle (~3 /C14 wider) and ~4% lower penetration (at t z 161t0)
compared to its counterpart injected into P∞ z 1 bar with the
same NPR of 10. This can be explained by the relatively higher
level of radial momentum and hence radial mixing for the jet
Fig. 11 e Velocity vectors and shock structure at the
vicinity of the triple point in under-expanded methane jet
with NPR ¼ 8.5 and P∞ ≈ 1.0 bar.
international journal of hydrogen energy 41 (2016) 6544 e65666558

<!-- PDF_PAGE: 16 -->

issued into elevated pressure conditions. As discussed earlier
(see Figs. 6 and 7 ), relatively similar jet tip vortices in terms of
velocity characteristics can exist for under-expanded jets
under various ambient pressures but at ﬁxed NPR. However,
the tip vortices of the jet issued into elevated pressure
conveyed more mass because of the higher injection pres-
sure. Therefore, this jet transports relatively greater level of
radial momentum which can result in fairly larger radial
penetration and jet cone angle. For the same NPR, the
hydrogen jet injected into the ambient with P
∞ z 10 bar
penetrated ~3% less than that of the jet issued into P∞ z 5b a r
(at t z 161t0).
Instantaneous snapshots of spatial variations of various
ﬂow quantities at t z 161t0, including H 2 mole fraction, tem-
perature, velocity, Mach number and vorticity for the
hydrogen jets with NPR ¼ 10 are presented in Fig. 13 for all
ambient pressures of 1, 5 and 10 bar. From this ﬁgure it is clear
that due to the rapid expansion of the jet, the velocity and the
Mach number reached maximum values of 2540 m/s and 3.98,
respectively, in the vicinity of the Mach reﬂection. The values
of centreline Mach number and density at t z 161t
0 for the
hydrogen jet with NPR ¼ 10 are plotted in Figs. 14 and 15 and
are compared to those with NPR ¼ 30 and 70 with P∞ z 1 bar
studied previously in Ref. [14]. It is clear from Fig. 14 that for all
values of NPR, the Mach number at the nozzle exit was ~1.1.
The maximum value of Ma occurred in the vicinity of the Mach
disk and was 3.94, 5.36 and 6.60 for NPR values of 10, 30 and 70,
respectively. In Fig. 14 it can be seen quantitatively that the
NPR is the only inﬂuential factor on the Mach number distri-
bution and, in general, on the sonic characteristics of under-
expanded jets. The nozzle exit velocity for all values of NPR
was about 1310 m/s. Values of the nozzle exit density in Fig. 15
show that the jets issued into elevated air pressures had
signiﬁcantly greater density at the nozzle exit compared to
that issued into P
∞ z 1 bar ambient. The values of density at
the nozzle exit for the H 2 jets injected into P∞ z 1 bar ambient
led to mass ﬂow rates of 1.07, 3.21 and 7.50 g/s for NPR values
of 10, 30 and 70, respectively. The calculated mass ﬂow rate for
NPR ¼ 10 is in good agreement with the value of ~1.0 g/s re-
ported by Ruggles and Ekoto [40]; their experimental data were
obtained at the same conditions of the current LES study. Figs.
12e15 show that the near-nozzle shock structure and sonic
characteristics, i.e. Mach disk dimensions, reﬂected shock
angle, velocity and Mach number at the Mach reﬂection and
shock cell spacing for the under-expanded jets with the same
NPR are almost identical.
It can be seen in the temperature snapshots of Fig. 13 that
the predicted values just upstream and downstream of the
Mach disk were ~70 K and ~296 K, respectively (with the latter
very close to but lower than the ambient temperature). It is
believed that due to the negative Joule-Thomson coefﬁcient of
hydrogen, the temperature proﬁle very close to the nozzle exit
may not be predicted accurately by the ideal gas equation of
state (EoS) employed here. As it has been presented by some
Fig. 12 e Density gradient jVrj ﬁeld of the under-expanded H 2 jets with NPR ¼ 10 and (a): P∞ ≈ 1 bar, (b): P∞ ≈ 5 bar and (c):
P∞ ≈ 10 bar ( t ≈ 161t0).
international journal of hydrogen energy 41 (2016) 6544 e6566 6559

<!-- PDF_PAGE: 17 -->

researchers [38,41], for hydrogen jets with extremely high in-
jection pressures ( P0>>100 bar) using a real gas EoS like Red-
lich-Kwong, resulted in capturing a higher temperature than
that of ambient just after the Mach disk. The speciﬁc effect of a
real gas EoS for the current ﬂow is under on-going study by the
current authors and it will be discussed in a future publica-
tion. Nevertheless, it has been shown by Ref. [38] that for
P
0 < 100 bar (i.e. relevant to the current study) an ideal gas EoS
would produce acceptable temperatures in under-expanded
hydrogen jets.
Shock cell spacing
As discussed in the introduction, shock cell spacing is an
important parameter in under-expanded jets and may be used
for various purposes. According to Fig. 14 , the length of the
second shock cell was ~4.04 mm and ~5.78 mm for hydrogen
jets with NPR ¼ 10 and 30, respectively. Also, Fig. 13 showed
that the maximum Mach number at the Mach disk location was
3.94 and 5.36 for jets with NPR ¼ 10 and 30, respectively. If Ma
j
in Equation (3) is assumed to be the Mach number just
Fig. 13 e Instantaneous snapshots of various ﬂow quantities in the H 2 jets with NPR ¼ 10 under various ambient pressures
at t ≈ 161t0.
international journal of hydrogen energy 41 (2016) 6544 e65666560

<!-- PDF_PAGE: 18 -->

upstream of the Mach reﬂection, by rearranging Equation (3),
the constant K can be deﬁned as:
K ¼ Ls
D
ﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ
Ma2
disk /C0 1
q (9)
If the correlation presented in Equation (9) is solved using
data of the hydrogen jets with NPR ¼ 10, then a value of
K z 0.71 is achieved. Interestingly, this value can also predict
the shock cell length of the hydrogen jet with NPR ¼ 8.5, 30 and
also methane jet with NPR ¼ 8.5 with a good accuracy.
Therefore, the current work suggests a correlation for the
shock cell spacing of under-expanded jets with 8.5 /C20 NPR /C20 30
as follows:
L
sz 0:71D
ﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ
Ma2
disk /C0 1
q
(10)
As discussed earlier, correlations proposed in the literature
based on Equation (3) may not be extended as a general
formulation for all types of under-expanded jets [23e25].
Therefore, Equation (10) should be considered only for highly
under-expanded jets under comparable NPR and nozzle scale
to those used in the present study.
Mixing characteristics
Mixture quality
Under constant NPR, higher ambient pressure results in
slightly wider jet (see Fig. 12 ). Moreover, the mole fraction
snapshots of Fig. 13 showed that the portion of lean mixture
(within the grid reﬁnement area) was reduced gradually by
increasing the ambient pressure (and, hence, injection pres-
sure for the same NPR). However, an under-expanded jet has a
highly turbulent three-dimensional structure, therefore, the
hydrogen-air mixture formation cannot be simply studied by
analysis of 2D contours similar to Fig. 13 . In this context, the
global mixing characteristics of the under-expanded
hydrogen jets were examined quantitatively by calculating
the probability of a mass weighted function based on the
hydrogen mass fraction ( Y
H2). The probability of
f(YH2) ¼ rYH2dV was calculated over the computational domain
in the reﬁned volume with grid resolution of D/50 and pre-
sented in Fig. 16 . It was found that the hydrogen jet with
NPR ¼ 8.5 had the lowest probability. It was also found that at
constant NPR ¼ 10, for hydrogen mass fraction in the range
YH2 ¼ 0.73e0.93 ( i.e. very rich mixture), higher ambient pres-
sure had higher probability values. Moreover, the integral of
f(Y
H2) over the full range of mass fraction (0.0 e1.0) was higher
for the jets with higher NPR and/or higher ambient pressure.
All these observations conﬁrm the existence of locally richer
mixture for jets with higher NPR or higher ambient pressure at
constant NPR.
Fig. 17 compares instantaneous snapshots of hydrogen
mole fraction at t z 322t
0 for jets with NPR ¼ 10 under ~1 bar
and ~5 bar ambient pressure. Fig. 17 also shows mole fraction
proﬁles at Z ¼ 15D and 17 D downstream of the nozzle exit.
From these plots it is now even clearer than in Fig. 13 that a
generally richer mixture was formed under elevated ambient
pressure. Both jets exhibited similar width of their hydrogen-
rich core ( X
H2 z 100%) up to about 5 D downstream of the
nozzle exit. However, the jet under ~5 bar ambient pressure
showed slightly wider cone angle from the beginning. Past
Z z 5D downstream of the nozzle exit, the rich hydrogen core
of both jets started diffusing more in the radial direction. Due
to the higher momentum at the nozzle exit of the jet that was
issued into the higher ambient pressure, the Kelvin-Helmholtz
instabilities induced by the supersonic shear layer were rela-
tively stronger, therefore, the radial expansion of this jet (and
thus its cone angle) became wider. It can also be seen that,
although both jets exhibited almost identical X
H2 in the vi-
cinity of the nozzle 's centreline, the jet issued into ~5 bar
pressure had signiﬁcantly higher values of XH2 in the radial
direction, especially for distances larger than Y/ D z 2.
Jet tip penetration
Fig. 18 shows the jet tip penetration for both hydrogen and
methane jets under various NPR and ambient pressure values.
The injection ‘delay’ time, i.e. the time it took the fuel to travel
inside the nozzle to the nozzle 's exit, was subtracted for
Fig. 14 e Variation of Mach number in under-expanded H 2
jets along the nozzle centreline at t ≈ 161t0.
Fig. 15 e Variation of Density in under-expanded H 2 jets
along the nozzle centreline at t ≈ 161t0.
international journal of hydrogen energy 41 (2016) 6544 e6566 6561

<!-- PDF_PAGE: 19 -->

Fig. 16 e Probability distribution of ( rYH2dV) within the reﬁnement area with D/50 cell resolution.
Fig. 17 e Left: instantaneous snapshots of H 2 mole fraction at t ≈ 322t0, (a): NPR ¼ 10 and P∞ ≈ 1 bar (b): NPR ¼ 10 and
P∞ ≈ 5 bar. Right: H 2 mole fraction probed on horizontal lines located at Z ¼ 15D and 17 D downstream of the nozzle exit.
Fig. 18 e Jet tip penetration of under-expanded methane and hydrogen jets under various NPR and ambient pressures.
international journal of hydrogen energy 41 (2016) 6544 e65666562

<!-- PDF_PAGE: 20 -->

plotting those penetration graphs. In fact, time t ¼ 0i n Fig. 18
is when the issuing gas is at the exit surface of the nozzle. For
hydrogen and methane jets the delay time was observed to be
around 4 and 6 ms, respectively. Methane showed considerably
lower penetration when compared to hydrogen with similar
NPR. Comparable result to what was observed in the current
work for the tip penetration of methane and hydrogen jets at
similar NPR was also reported in Ref. [54]. The shorter pene-
tration of methane is attributed to the relatively higher speed
of sound in hydrogen which resulted in higher nozzle exit
velocity for the latter under-expanded jet. Based on this, since
the nozzle exit velocity and maximum Mach number of the
hydrogen jets with similar NPR were almost identical (see
Fig. 14), not much difference in the tip penetration of these jets
were expected. In fact, it was found that for constant NPR
lower ambient pressure resulted in slightly higher jet tip
penetration. This can be attributed to the higher level of the
radial momentum of the jets issued into higher ambient
pressure. It was found that the greater amount of mass
injected into the elevated ambient pressures got distributed
radially in a stronger manner, hence a wider jet angle was
produced.
As discussed in the introduction, a typical correlation for
the tip penetration of a round jet is given by Equation (8).
However, the values that have been reported for C
t and Cf
relate primarily to subsonic jets [34]. Petersen and Ghandhi
[28] suggested that due to the reliance of Equation (8) on the
invariance of the axial momentum and moreover because of
the interrupted density ﬁeld (see Fig. 15 ) in an under-
expanded jet, the aforementioned equation may fail within
short distances near the nozzle exit of under-expanded jets. It
is still fairly hard to study precisely the initial transient
behaviour of under-expanded jets issuing from a real injector
for automotive applications, e.g. by means of schlieren imag-
ing as conducted by Ref. [28]. However, as shown in the LES
studies of [13,14,42], a correlation derived from Equation (8)
can be used to scale the jet tip penetration for various
under-expanded jets. The current work suggests a new scaling
correlation for the tip penetration of under-expanded jets
based on Equation (8) as:
Z
tip ¼ CA
/C18 r1
r∞
/C19 0:25
ðU1DtÞ0:5 (11)
where CA is a new parameter. The left graph of Fig. 19
shows that a scaled correlation of the form ( r1/r∞)0.25(U1Dt)0.5
produces penetration curves for hydrogen and methane that
have collapsed onto an almost single trend line. However, this
is not telling the story of the simulated penetration curves of
Fig. 18 . Therefore, a graph of C
A versus time can be obtained
from Fig. 18 to correct the left graph of Fig. 19. This is shown in
the right graph of Fig. 19 . CA is a combination of Ct and Cf of
equation (18); Ct is related to the diffusivity and kinematic
momentum of the jet whilst Cf is associated with the jet 's
centreline velocity. Ct and Cf are signiﬁcantly different for the
hydrogen and methane jets which results in larger values of
CA for hydrogen. However, if one used the constants Ct and Cf
of [34], a value of CA of ~2.4 would be obtained which broadly
lies on the horizon of the CA curves shown in Fig. 19. By ﬁtting
second order polynomial trend lines for curves of CA in Fig. 19
it is possible to derive correlations deﬁning variation of CA
versus time in form of CA ¼ At2 þ Bt þ C. Based on Fig. 19 for
the methane jet values of /C0 13.27, 11.09 and 1.12 were calcu-
lated for the coefﬁcient A, B and C, respectively. Due to the
very similar values of C
A for all the hydrogen jets, a single
second order polynomial was ﬁtted on a curve representing
the average of the C
A curve of the hydrogen jets. In this case,
the values of A, B and C were calculated to be /C0 34.65, 18.71 and
1.33, respectively. It should be noted that the aforementioned
C
A correlation and its associated A, B and C coefﬁcient values
are valid for t /C21 4 ms and t /C21 1 ms for methane and hydrogen
jets, respectively.
As it has been discussed in Ref. [14], due to relatively longer
initial transient process and greater radial penetration of
hydrogen jets with NPR ¼ 30 and 70 compared to those with
NPR ¼ 8.5 and 10, the scaled tip penetration did not collapse
onto the curve for NPR ¼ 8.5 and 10. Therefore, C
A may need
further adjustment for under-expanded jets of a speciﬁc gas
with noticeably different NPR levels; this is being investigated
by the current authors and will be reported in a future
publication.
Conclusions
The current study used large eddy simulation in order to
extend the previous work of the current authors [14] by
Fig. 19 e Left: Jet tip penetration in relation to Equation (11). Right: Variation of parameter CA of Equation (11) against time.
international journal of hydrogen energy 41 (2016) 6544 e6566 6563

<!-- PDF_PAGE: 21 -->

looking into the effect of elevating ambient pressure (to
levels relevant to DI engines) on the key sonic and mixing
characteristics of hydrogen jets. Additionally, the transient
formation of the near-nozzle shock structure and initial
vortex ring were studied for hydrogen and methane. The key
conclusions of the present study can be summarised as
follows:
/C15 At constant NPR, higher ambient pressure resulted in
faster formation of the ﬁnal Mach reﬂection (Mach disk) and
shorter Mach disk settlement time. This was attributed to
the relatively faster transient evolution of the in-nozzle
ﬂow and hence fairly faster transformation from sub-
sonic to sonic/supersonic nozzle exit for the jets at elevated
ambient pressure.
/C15 The tip vortices of the jet issued into elevated pressure
conveyed more mass and transported relatively greater
level of radial momentum, resulting in fairly larger radial
penetration and jet cone angle.
/C15 Signiﬁcant difference in the evolution of the tip vortices
was observed between hydrogen and methane at constant
NPR. This was attributed to their majorly different speeds
of sound and hence nozzle exit velocities.
/C15 The initial transient tip vortices (vortex ring) of hydrogen
jets may contribute signiﬁcantly to the ﬂow instabilities at
the boundary of the intercepting shock and promote
hydrogen-air mixing upstream of the Mach reﬂection (un-
like for the methane jet).
/C15 The origin of the outer shear layer for hydrogen was
located about half nozzle diameter downstream of the
nozzle exit very close to the centroid of the initial tip
vortices. For methane, the outer shear layer originated
after the Mach disk and was dominated by the Mach
reﬂection.
/C15 For a particular gas the transient evolution of the tip
vortices (vortex ring) is mostly affected by NPR rather than
the level of incoming momentum ( i.e. injection pressure).
/C15 For methane, due to the higher gradient of the transverse
velocity component just before the Mach reﬂection, a
relatively more concave Mach disk was formed than for
hydrogen.
/C15 The current LES study, in agreement with previous exper-
imental observations, did not capture any kind of ﬂow
recirculation just downstream of the Mach disk. To the best
of the authors' knowledge, this is the ﬁrst time that such an
observation has been made by numerical simulation of the
NaviereStokes equations.
/C15 The near-nozzle shock structure was only affected by NPR.
At constant NPR, identical Mach disk dimensions, reﬂected
shock angles, shock cell spacing and shear layer thickness
were observed for jets issued into different ambient
pressures.
/C15 For constant NPR lower ambient pressure resulted in
slightly higher jet tip penetration. This was attributed to
the higher level of the radial momentum in jets issued into
elevated ambient pressures.
/C15 By calculating the probability of a density-weighted func-
tion based on the mass fraction of hydrogen it was found
that a locally richer mixture existed for jets with higher
NPR or with higher ambient pressure at constant NPR.
/C15 Two correlations were proposed for the core shock cell
spacing and the jet tip penetration of highly under-
expanded jets.
Acknowledgements
The authors acknowledge the use of University College
London's Legion High Performance Computing Facility
(Legion@UCL) and associated support services, in the
completion of this work. The authors would also like to
thank all members of the UCL Internal Combustion Engines
and Fuel Systems Group for their assistance and many
valuable discussions.
Appendix
Fig. A.1 e Transient evolution of the near-nozzle shock
structure in an under-expanded nitrogen jet.
international journal of hydrogen energy 41 (2016) 6544 e65666564

<!-- PDF_PAGE: 22 -->

references
[1] Verhelst S, Wallner T. Hydrogen-fueled internal combustion
engines. Prog Energy Combust Sci 2009;35:490 e527.
[2] Cho HM, He B. Spark ignition natural gas engines ea review.
Energy Convers Manag 2007;48:608 e18.
[3] Scarcelli R, Wallner T, Matthias N, Salazar V, Kaiser S.
Mixture formation in direct injection hydrogen engines: cfd
and optical analysis of single- and multi-hole nozzles. SAE
Int J Engines 2011:2361 e75.
[4] Hamzehloo A, Aleiferis PG. Computational study of hydrogen
direct injection for internal combustion engines. 2013. SAE
Technical Paper 2013-01-2524 .
[5] Hamzehloo A, Aleiferis PG. Numerical modelling of mixture
and combustion in DISI hydrogen engines with various
injection strategies. 2014. SAE Technical Paper 2014-01-
2577.
[6] Crist S, Sherman PM, Glass DR. Study of the highly
underexpanded sonic jet. AIAA J 1996;4:68 e71.
[7] CDuP Donaldson, Snedeker RS. A study of free jet
impingement. part 1. mean properties of free and impinging
jets. J Fluid Mech 1971;45:281 e319.
[8] Hornung H. Regular and Mach reﬂection of shock waves. Ann
Rev Fluid Mech 1986;18:33 e58.
[9] Inman JA, Danehy PM, Nowak RJ, Alderfer DW. Identiﬁcation
of instability modes of transition in underexpanded jets. In:
38th ﬂuid dynamics conference and exhibit. Seattle,
Washington; USA: AIAA Paper; 2008. p. 2008 e4389.
[10] Edgington-Mitchell D, Honnery RD, Soria J. The
underexpanded jet Mach disk and its associated shear layer.
Phys Fluids 2014;26:096101 .
[11] Ashkenas H, Sherman FS. The structure and utilization of
supersonic free jets in low density wind tunnel. In: Advances
in applied mechanics-rareﬁed gas dynamics. New York:
Academic Press; 1965. p. 84 e105.
[12] Velikorodny A, Kudriakov S. Numerical study of the near-
ﬁeld of highly underexpanded turbulent gas jets. Int J Hydrog
Energy 2012;37:17390 e9.
[13] Vuorinen V, Yu J, Tirunagari S, Kaario O, Larmi M, Duwig C,
et al. Large-eddy simulation of highly underexpanded
transient gas jets. Phys Fluids 2013;25:016101 .
[14] Hamzehloo A, Aleiferis PG. Large eddy simulation of highly
turbulent under expanded hydrogen and methane jets for
gaseous-fuelled internal combustion engines. Int J Hydrog
Energy 2014;39:21275 e96.
[15] Tam CKW. Broadband shock-associated noise of moderately
imperfectly expanded supersonic jets. J Sound Vib
1990;140:55e71.
[16] Tam CKW. Supersonic jet noise. Ann Rev Fluid Mech
1995;27:17e43.
[17]
Panda J. Shock oscillation in underexpanded screeching jets.
J Fluid Mech 1998;363:173 e98.
[18] Pack DC. A note on Prandtl 's formula for the wave-length of a
supersonic gas jet. Q J Mech Appl Math 1950;3:173 e81.
[19] Emden R. U¨ ber die ausstr €omungserscheinungen
permanenter gase. Ann Phys 1899;305:264 e89.
[20] Prandtl L. Stationary waves in a gaseous jet. Phys Z
1904;4:599e601.
[21] Tam CKW, Tanna HK. Shock associated noise of supersonic
jets from convergent-divergent nozzles. J Sound Vib
1982;81:337e58.
[22] Tam CKW, Jay AJ, Seiner JM. A multiple-scales model of the
shock-cell structure of imperfectly expanded supersonic jets.
J Fluid Mech 1985;153:123 e49.
[23] Hu TF, McLaughlin DK. Flow and acoustic properties of low
reynolds number underexpanded supersonic jets. J Sound
Vib 1990;141:485 e505.
[24] Scroggs SD, Settles GS. An experimental study of supersonic
microjets. Exp Fluids 1996;21:401 e9.
[25] Phalnikar KA, Kumar R, Alvi FS. Experiments on free and
impinging supersonic m icrojets. Exp Fluids
2008;44:819 e30.
[26] Ouellette P. Direct injection of natural gas for diesel engine
fueling. PhD Thesis. Vancouver, Canada: The University of
British Columbia; 1996 .
[27] Ouellette P, Hill PG. Turbulent transient gas injections. J
Fluids Eng 2000;122:743 e52.
[28] Petersen BR, Ghandhi JB. Transient high-pressure hydrogen
jet measurements. 2006. SAE Technical Paper 2006-01-0652 .
[29] Turner JS. The ‘starting plume ’ in neutral surroundings. J
Fluid Mech 1962;13:356 e68.
[30] Hill PG, Ouellette P. Transient turbulent gaseous fuel jets for
diesel engines. J Fluids Eng 1999;121:93 e101.
[31] Ricou FP, Spalding DB. Measurements of entrainment by
axisymmetrical turbulent jets. J Fluid Mech 1961;11:21 e32.
[32] Abraham J. Entrainment characteristics of transient gas jets.
Heat Transf Part A Appl 1996;30:347
e64.
Fig. A.2 e Transient evolution of the initial tip vortices
(vortex ring) in an under-expanded nitrogen jet (based on
the scalar mass fraction).
international journal of hydrogen energy 41 (2016) 6544 e6566 6565

<!-- PDF_PAGE: 23 -->

[33] Schlichting H. Boundary layer theory. New York: McGraw-
Hill; 1976 .
[34] Song L, Abraham J. Entrainment characteristics of transient
turbulent round, radial and wall-impinging jets: theoretical
deductions. J Fluids Eng 2003;125:605 e12.
[35] Dauptain A, Cuenot B, Gicquel YM. Large-eddy simulation of
a stable supersonic jet impinging on ﬂat plate. AIAA J
2010;48:2325e37.
[36] White T, Milton B. Shock wave calibration of under expanded
natural gas fuel jets. Shock Waves 2008;18:353 e64.
[37] Vuorinen V, Wehrfritz A, Duwig C, Boersma BJ. Large-eddy
simulation on the effect of injection pressure and density on
fuel jet mixing in gas engines. Fuel 2014;130:241 e50.
[38] Khaksarfard R, Kameshki MR, Paraschivoiu M. Numerical
simulation of high pressure release and dispersion of
hydrogen into air with real gas model. Shock Waves
2010;20:205e16.
[39] Gorl/C19e C, Gamba M, Ham F. Investigation of an
underexpanded hydrogen jet in quiescent air using
numerical simulations and experiments. In: Annual research
briefs. Center for Turbulence Research, Stanford University;
2010.
[40] Ruggles AJ, Ekoto IW. Ignitability and mixing of
underexpanded hydrogen jets. Int J Hydrog Energy
2012;37:17549e60.
[41] Bonelli F, Viggiano A, Magi V. A numerical analysis of
hydrogen underexpanded jets under real gas assumption. J
Fluids Eng 2013;135:121101 .
[42] Hamzehloo A, Aleiferis PG. Large eddy simulation of near-
nozzle shock structure and mixing characteristics of
hydrogen jets for direct-injection spark-ignition engines. In:
10th International Conference on Heat Transfer, Fluid
Mechanics and Thermodynamics (HEFAT2014), Orlando,
Florida, USA; 2014 .
[43] Weiss JM, Smith WA. Preconditioning applied to variable and
constant density ﬂows. AIAA J 1995;33:2050 e7.
[44] Weiss JM, Maruszewski JP, Smith WA. Implicit solution of
preconditioned Navier-Stokes equations using algebraic
multigrid. AIAA J 1999;37:29 e36.
[45] Ferziger JH, Peric M. Computational methods for ﬂuid
dynamics. Springer; 2002 .
[46] Liou MS. A sequel to AUSM, part II: AUSM þ-up for all speeds.
J Comput Phys 2006;214:137 e70.
[47] Pope SB. Turbulent ﬂows. Cambridge University Press; 2000 .
[48] Nicoud F, Ducros F. Subgrid-scale stress modelling based on
the square of the velocity gradient tensor. Flow Turbul
Combust 1999;62:183 e200.
[49] Cussler EL. Diffusion: mass transfer in ﬂuid systems. 3rd ed.
Cambridge University Press; 2009 .
[50] Weller HG, Tabor G, Jasak H, Fureby C. A tensorial approach
to computational continuum mechanics using object
orientated techniques. Comp Phys 1998;12:620 e31
.
[51] Hamzehloo A. Computational study of under-expanded jets,
mixture formation and combustion in direct-injection spark-
ignition hydrogen engines. PhD Thesis. UK: University
College London (UCL); 2016 .
[52] Andr/C19e B, Castelain T, Bailly C. Investigation of the mixing
layer of underexpanded supersonic jets by particle image
velocimetry. Int J Heat Fluid Flow 2014;50:188 e200.
[53] Golub VV. Development of shock wave and vortex structures
in unsteady jets. Shock Waves 1994;3:279 e85.
[54] Rogers T, Petersen P, Koopmans L, Lappas P, Boretti A.
Structural characteristics of hydrogen and compressed
natural gas fuel jets. Int J Hydrog Energy 2015;40:1584 e97.
[55] Cabral B, Leedom LC. Imaging vector ﬁelds using line integral
convolution. In: Proceedings of the 20th Annual Conference
on Computer Graphics and Interactive Techniques. ACM;
1993.
[56] Smarr LL, Michael LN, Winkler KA. Shocks, interfaces and
patterns in supersonic jets. Phys D Nonlinear Phenom
1984;12:83e106.
[57] Bulgakov AV, Bulgakova NM. Gas-dynamic effects of the
interaction between a pulsed laser-ablation plume and the
ambient gas: analogy with an underexpanded jet. J Phys D
Appl Phys 1998;31:693 e770.
[58] Saric WSM. G €ortler vortices. Ann Rev Fluid Mech
1994;26:379e409.
[59] Andr/C19e B, Castelain T, Bailly C. Experimental exploration of
underexpanded supersonic jets. Shock Waves 2014;24:21 e32.
[60] Mat/C19e B, Graur IA, Elizarova T, Chirokov I, Tejeda G,
Fernandez JM, et al. Experimental and numerical
investigation of an axisymmetric supersonic jet. J Fluid Mech
2001;426:177e97.
[61] Gribben BJ, Badcock KJ, Richards BE. Numerical study of
shock-reﬂection hysteresis in an underexpanded jet. AIAA J
2000;38:275e83.
[62] Skovorodko PA, Levin DA, Wysong IJ, Garcia AL. About the
nature of the recirculation zone behind a mach disk in an
underexpanded jet. AIP Conf Proceedings-American Inst
Phys 2011;1333:601 e6.
[63] Frey M, Hagemann G. Restricted shock separation in rocket
nozzles. J Prop Power 2000;16:478 e84.
international journal of hydrogen energy 41 (2016) 6544 e65666566
