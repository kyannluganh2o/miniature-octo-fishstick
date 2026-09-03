<!-- PDF_PAGE: 1 -->

rspa.royalsocietypublishing.org
Research
Citethisarticle: JainM,PrakashRS,Tomar
G,RavikrishnaRV.2015Secondarybreakupofa
dropatmoderateWebernumbers. Proc. R.
Soc. A471:20140930.
http://dx.doi.org/10.1098/rspa.2014.0930
Received:3December2014
Accepted:19March2015
SubjectAreas:
fluidmechanics,mechanicalengineering,
computationalphysics
Keywords:
atomization,secondarybreakup,
droplets,highdensityratio
Authorforcorrespondence:
GauravTomar
e-mail:gtom@mecheng.iisc.ernet.in
Secondarybreakupofadropat
moderateWebernumbers
MohitJain1,R.SuryaPrakash 2,GauravTomar1
andR.V.Ravikrishna 1
1DepartmentofMechanicalEngineering,and 2Departmentof
AerospaceEngineering,IndianInstituteofScienceBangalore,
Karnataka560012,India
We present volume of ﬂuid based numerical
simulations of secondary breakup of a drop with
high density ratio (approx. 1000) and also perform
experiments by injecting monodisperse water droplets
in a continuous jet of air and capture the breakup
regimes, namely, bag formation, bag-stamen, multibag
and shear breakup, observed in the moderate Weber
number range (20–120). We observe an interesting
transition regime between bag and shear breakup for
We = 80, in both simulations as well as experiments,
where the formation of multiple lobes, is observed,
instead of a single bag, which are connected to
each other via thicker rim-like threads that hold
them. We show that the transition from bag to
shear breakup occurs owing to the rim dynamics
which shows retraction under capillary forces at
We = 80, whereas the rim is sheared away with ﬂow
at We = 120 thus resulting in a backward facing bag.
The drop characteristics and timescales obtained in
simulations are in good agreement with experiments.
The drop size distribution after the breakup shows
bimodal nature for the single-bag breakup mode and
a unimodal nature following lognormal distribution
for higher Weber numbers.
1. Introduction
A drop subjected to a high-speed stream of gas ﬂow
breaks up into smaller droplets. Similarly, a rain drop
falling under gravitational ﬁeld through air fragments
into smaller droplets which may further undergo
multiple coalescence and breakups [ 1]. In various
industrial applications, a liquid jet issued at a high
speed through thin nozzles (approx. a few hundred
micrometres) breaks up into droplets of sizes smaller
2015TheAuthor(s)PublishedbytheRoyalSociety.Allrightsreserved.
Downloaded from royalsocietypublishing.​org/​rspa/​article-pdf/​doi/​10.​1098/​rspa.​2014.​0930/​366722/​rspa.​2014.​0930.​pdf
by China Institution user
on 31 August 2026

<!-- PDF_PAGE: 2 -->

2rspa.royalsocietypublishing.orgProc. R. Soc. A471:20140930 ...................................................
than the jet diameter. The droplets so formed during primary atomization further undergo
secondary breakup resulting in much smaller droplets. It has been noted earlier by Tryggvason
[2] that merely increasing the liquid /ambient-gas speed does not result in a desired shift in
the size distribution of the droplets at the end of the atomization process. Therefore, although
efﬁcient primary atomization is desired to result in the formation of efﬁcient sprays, in various
applications such as combustion, spray drying and coating, drug delivery and evaporation-based
heat exchangers, secondary atomization is the key rate determining factor and thus has been a
subject of intense research for the past several decades. Taylor [3] in his seminal paper discussed
the deformation of a drop and its acceleration in a high-speed air stream. In particular, Taylor [3]
showed that a drop requires a critical Weber number ( We) for breakup. A similar analysis was
performed by Prandtl [4]. The critical We for breakup from different experimental studies varies
around 11 ± 2( s e e[5–12]).
Although there is reasonable agreement between different experimental studies on the critical
Weber number, the phase boundaries for various regimes and the exact mechanism of breakup
modes have been a subject of debate for the past two decades. Hinze [ 13] showed that for
high density ratios and Reynolds numbers Re = ρ
gD0U∞ /μg (here, ρg and μg are the density
and viscosity of the gas, respectively, and D0 is the diameter of the drop), different modes
and the transitions between them are essentially a function of the aerodynamic Weber number
(We = ρgU2
∞ D0/γ) and liquid Ohnesorge number, Oh = μl/
√
ρlD0γ,w h e r eγ is surface-tension
coefﬁcient and,μl and ρl are the viscosity and density of the liquid, respectively. Krzeczkowski [7]
extended Hinze’s analysis to locate transitions onWe − Oh phase plane and discussed various bag
breakup and shear breakup regimes. The essential modes of breakup at low Ohnesorge numbers
(Oh < 0.1 ) are bag-breakup for We > 11 [8], followed by the multimode breakup, which marks
the transition between bag and shear breakup and, shows formation of a stamen in the centre
of the bag [ 12] or formation of multiple bags [ 14,15]f o r3 0< We < 80. At higher 80 < We < 350,
shear stripping mode is expected and beyond We = 350 a catastrophic breakup of the drop occurs
(see [14,16–22]).
The vast literature on secondary atomization of a drop has been periodically reviewed, for
example, see [12,13,23,24], and more recently by Guildenbecher [25]. Although there has been an
increasing clarity and agreement on the transition between different regimes on aWe − Oh phase-
plane, the exact mechanisms involved are still not clear primarily owing to the lack of access to
velocity and pressure ﬁelds in experiments. Formation of bag and bag-stamen has been explained
to be owing to Rayleigh–Taylor instability (RTI). Based on the ﬂoor integer value of the ratio of
maximum initial drop deformation to RTI wavelength, formation of bag and bag-stamen has been
shown to occur when the ratios are around 1 and 2, respectively (see [19,26]). Rimbert & Castanet
[27] discussed the possibility of crossover between RTI and turbulence-induced mechanism in a
bag breakup regime. Another possible mechanism that has been proposed is owing to internal
ﬂow in the drop. Guildenbecher [25] suggested that owing to drop deformation the internal ﬂow
from the poles to the equator leads to the formation of the rim. However, at high We surface
tension is weak and does not support formation of the rim and the rim is carried away by
the ambient ﬂow. The onset of shear stripping has also been debated primarily between the
two popular theories, namely boundary layer stripping mechanism [ 28] suggesting breakup
owing to boundary layer separation, and another owing to Engel [ 29] and Hinze [13] suggesting
sheet-thinning and formation of ligaments and then streaming of droplets from the ends of the
ligaments (also see [30]).
An important aspect of secondary breakup is the timescale involved. A study of temporal
characteristics, although discussed in earlier studies to some extent, have recently gained
much attention primarily owing to its importance in the estimation of the extent of secondary
atomization for designing more efﬁcient combustion engines and drug-delivery systems. Liu &
Reitz [30] studied the different phases of droplet deformation, from spherical to disc-shaped, and
showed that the rupture of the bag is initiated by formation of holes on the bag sheet and their
subsequent growth leads to its breakup. Chou & Faeth [8] experimentally studied the bag breakup
Downloaded from royalsocietypublishing.​org/​rspa/​article-pdf/​doi/​10.​1098/​rspa.​2014.​0930/​366722/​rspa.​2014.​0930.​pdf
by China Institution user
on 31 August 2026

<!-- PDF_PAGE: 3 -->

3rspa.royalsocietypublishing.orgProc. R. Soc. A471:20140930 ...................................................
regime (We ∼ 13 − 20 and Oh ≪ 1) and showed that the bag breakup requires 5− 6tc for complete
breakup, where,
tc = D0(ρl/ρg)1/2
U∞
, (1.1)
is the characteristic timescale [ 28]. Further, the complete breakup was shown to occur over a
distance of 50–100 droplet diameters. They showed that although bag breakup leads to smallest
droplets, the majority of the volume (approx. 56%) is contained in the basal ring which holds
the bag.
Recent numerical efforts in simulating secondary breakup have also revealed a number of
interesting features of droplet breakup mechanisms for different ambient to drop density and
viscosity ratios (see [ 31–38]). However, most numerical studies simulate low density ratio (less
than <100) drop breakup, for example [ 32,33,39,40], and show backward bag formation at
moderate Weber numbers (20 < We < 80). Xiao et al. [41] simulated a high density ratio using a
CLSVOF algorithm, but their focus was on veriﬁcation of their large Eddy simulation algorithm
for turbulent ﬂows and different bag breakup regimes were not discussed.
In this study, we present three-dimensional volume-of-ﬂuid simulations with density ratio
approximately 1000 for different values of We and capture bag breakup, bag-stamen breakup,
multi-bag breakup and shear breakup of a drop in a uniform ﬂow of gas. The simulation results
are compared with the experiments performed using a continuous jet of gas for the same values of
We, in particular, the drop deformation characteristics, timescales of breakup and breakup modes.
We show that, in contrast to bag formation simulated using low-density ratios, for high density
ratios a forward facing bag is formed for 20 < We < 80. We note here that these are the ﬁrst three-
dimensional simulations of the drop break up phenomenon at 1000 density ratio for a range of
20 < We < 120.
The paper is organized as follows. Section 2 presents problem formulation and numerical and
experimental methods used in this study. In §3, we discuss both numerical and experimental
results. Finally, we present the important conclusions from this study in §4.
2. Problemformulation
Among the several possible setups to study secondary breakup of a drop, the three most popular
are (i) shock tubes, (ii) continuous jets and (iii) free falling droplets. In this study, we use the
continuous air jet setup. A drop of diameter D
0 is placed at t = 0 in a ﬂow with a constant far-
ﬁeld velocity ﬁeld, U∞ . We deﬁne the aerodynamic Weber number based on the relative velocity
between the liquid drop and the gas stream at t = 0, as
We = ρgU2
∞ D0
γ , (2.1)
where ρg is the density of the ambient gas and γ is the surface tension coefﬁcient at the drop
surface. Assuming both the liquid and the ambient gas to be incompressible, the continuity
equation is given by
∇· u = 0, (2.2)
where u is the divergence free velocity ﬁeld. We use a volume of ﬂuid method which is
essentially a one-ﬂuid model for two phase ﬂows. The governing equations for the momentum
are given by the Navier–Stokes equations augmented with surface forces to implicitly account
for the interfacial boundary conditions of continuity of velocity, and normal and tangential
stress balance,
ρ(F)
(∂u
∂t +∇· uu
)
=− ∇p +∇· (μ(F)D) + γκnδs, (2.3)
where F is the volume fraction of liquid and takes values between 0 and 1,ρ(F) = ρlF + (1 − F)ρg,
μ(F) = μlF + (1 − F)μg, with ρl, ρg are liquid and gas densities, respectively, and μl and μg are
liquid and gas viscosities, respectively. The deformation rate tensor is given byD = (∇ u +∇ uT)/2.
Downloaded from royalsocietypublishing.​org/​rspa/​article-pdf/​doi/​10.​1098/​rspa.​2014.​0930/​366722/​rspa.​2014.​0930.​pdf
by China Institution user
on 31 August 2026

<!-- PDF_PAGE: 4 -->

4rspa.royalsocietypublishing.orgProc. R. Soc. A471:20140930 ...................................................
The last term in the equation accounts for the surface tension force ( γκ,w h e r eκ is the local
curvature of the interface) on the interface embedded in a Eulerian grid and marked with the
surface Dirac delta function, δs. The direction of the force is along the local normal ( n) at the
interface. The surface tension force is modelled as a volumetric force using the continuum surface
force approach owing to Brackbill et al. [42]. The evolution equation for the interface is given as
an advection equation in terms of the volume fraction, F,
∂F
∂t + u ·∇ F = 0. (2.4)
(a) Numericalmethod
We use an octtree-based adaptive mesh reﬁnement volume of ﬂuid algorithm in Gerris (see
[43–45]) to solve the above equations. Gerris uses a second-order accurate staggered time
discretization for velocity, volume-fraction and pressure ﬁelds. The discretized equations are
written as [43]
ρ
n+1/2
[ u⋆ − un
/Delta1t + un+1/2 ·∇ un+1/2
]
=∇· [μn+1/2(Dn + D⋆)] + (γκδsn)n+1/2, (2.5)
Fn+1/2 − Fn−1/2
/Delta1t +∇· (Fnun) = 0, (2.6)
un+1 = u⋆ − /Delta1t
ρn+1/2
∇ pn+1/2 (2.7)
and ∇· un+1 = 0. (2.8)
Here, the subscripts ( n + 1/2) deﬁne the intermediate time staggered time stepping adopted
for void fraction ﬁeld and thus velocity and density and, subscript ﬁve-pointed star marks the
auxiliary velocity ﬁeld which is corrected using the pressure correction equation, equation (2.7),
to obtain the velocity ﬁeld at the next time step, n + 1. Advection equation for F (equation (2.6))
is solved in Gerris using geometric ﬂuxing. Adaptive mesh reﬁnement is performed using a
cost function based on the local vorticity in the ﬁeld and the gradient of the void-fraction
ﬁeld, thus using a very ﬁne reﬁnement in the regions of high velocity gradient and at the
interface. We use a thin transition region of three cells for smoothing the physical properties
across the interface. To validate the efﬁcacy of the numerical algorithm in capturing high density
ratios, we perform a capillary wave test case and compare with the analytical solution of
Prosperetti [46] (also see [ 47]). The simulation is performed for a density ratio of 1000 : 1.2 and
viscosity ratio 1.003 × 10
−3 : 1.8 × 10−5. The surface tension coefﬁcient is 72 mN m −1. A good
agreement between the numerical and analytical results is obtained (not shown here).
Simulations of drop breakup have been performed for ﬂow in a rectangular channel with slip
boundary conditions employed at all boundaries except at the inlet and outlet for the crossﬂow.
A spherical drop is placed at the centre of the channel at t = 0. The channel width is 10 times the
droplet diameter. A uniform inlet velocity is imposed at the left boundary and outﬂow boundary
conditions of Dirichlet on pressure and Neumann on velocity. The droplet is resolved using the
ﬁnest grid size/Delta1x = D
0/200 (for the 230µm droplets the grid resolution is approx. 1µm). We note
that even with this resolution the ﬁnal rupture of thin liquid ligament/sheet would be essentially
numerical, because the physics that governs the ﬁnal breakup is molecular and would require
multiscale modelling which hopefully would be possible in near future. The error encountered
owing to VOF numerical clipping in the present simulations is of the order of the grid size that
is approximately 1 µm. For all the simulations presented in this study, the liquid to gas density
ratio is ρ
l/ρg = 1000. The liquid and gas Ohnesorge numbers are given by Ohl = μl/
√
ρlD0γ = 0.1
and Ohg = μg/√ρgD0γ = 0.0032. In order to capture the various regimes of droplet break up in a
cross ﬂow, we perform simulations for different values of aerodynamic Weber numbers, namely
We = 20, 40, 80 and 120, to capture the bag breakup, bag breakup with stamen, multi-bag breakup
and shear stripping, respectively.
Downloaded from royalsocietypublishing.​org/​rspa/​article-pdf/​doi/​10.​1098/​rspa.​2014.​0930/​366722/​rspa.​2014.​0930.​pdf
by China Institution user
on 31 August 2026

<!-- PDF_PAGE: 5 -->

5rspa.royalsocietypublishing.orgProc. R. Soc. A471:20140930 ...................................................
nozzle orifice
control/data
acquisition
system
function
generator
control signal
gas line
liquid line
square wave
electric signal
liquid
storage
diffuser
Nd:Y AG pulsed laser zoom lens
air nozzle
~2 mm
CCD camera
compressed air
storage
mono-disperse drop generator
Figure1.Schematicoftheexperimentalset-upusedfortheinvestigationofbreakupofadropinahigh-speedgasflow.
(b) Experimentalset-up
As discussed earlier, we use a continuous jet set-up to study secondary atomization
experimentally. A schematic of the experimental set-up is shown in ﬁgure 1.
A spherical drop of water is made to fall vertically into the horizontal air jet to undergo
breakup. A contoured nozzle with an oriﬁce diameter of 2 mm is used to generate the required
air ﬂow. The internal section of the nozzle is designed so as to obtain a top-hat velocity proﬁle
at the exit which has been veriﬁed with the aid of PIV measurements. Pressure drop across the
nozzle is calibrated and varied to obtain ﬂow velocities up to 300 m s
−1, thus varying the Weber
number. We note that in this study,We = 120 corresponds to a Mach number approximately 0.48,
and thus the incompressible ﬂow assumption in the numerical simulations is not strictly valid.
Nevertheless, we argue that the numerical results presented here would capture the essential
features of deformation and breakup and would in general be valid for bigger-sized drops
approximately 1 mm for the range of non-dimensional parameters studied here. Mono-disperse
drops having diameters of the order of 200 µm are generated with the aid of a mono-disperse
drop generator (MDG). An oriﬁce of diameter 100 µm is used for generation of these droplets.
Flow rate and the forcing frequency are the variables that may be adjusted to generate drops
having different velocities but having the same diameter. Different drop velocities are required to
ensure that the drops penetrate into the potential core of the air jet at every Weber number. Inset in
ﬁgure 1 shows the injected drop and its breakup as it enters the region of gas ﬂow from a nozzle of
diameter 2 mm. The air ﬂow is from left to right from the nozzle shown inﬁgure 1. As the air ﬂow
velocity is increased (thus increasing We), the vertically falling droplet requires higher velocity
to penetrate into the core of the air jet before undergoing breakup. The droplets produced by
mono-disperse drop generator are generated consistently, and there is little variation in breakup
structures (breakup regime) from drop to drop (see ﬁgure 1 of the modiﬁed manuscript). In this
study, we carry out experiments for Weber numbers ranging from 8 to 300.
Images are captured with the help of suitable optics and backlighting arrangements. High-
speed imaging is carried out in order to cover the rapid single drop breakup event with good
Downloaded from royalsocietypublishing.​org/​rspa/​article-pdf/​doi/​10.​1098/​rspa.​2014.​0930/​366722/​rspa.​2014.​0930.​pdf
by China Institution user
on 31 August 2026

<!-- PDF_PAGE: 6 -->

6rspa.royalsocietypublishing.orgProc. R. Soc. A471:20140930 ...................................................
Table1.Differentbreakupregimesasafunctionof We.
breakupregime Pilch&Erdman[12] Krzeczkowski[7] Guildenbecher[25] presentexperiments
vibrationalornobreakup We<12 We<10 We<11 We<12
......................................... ............................................ .......................................... ..................................... ......................................
bag 12 < We<50 10 < We<18 11 < We<35 12 < We<24
......................................... ............................................ .......................................... ..................................... ......................................
bag-stamen 50 < We<100 18 < We<30 35 < We<80 24 < We<45
(multi-mode)
......................................... ............................................ .......................................... ..................................... ......................................
bag/plume 45 < We<65
......................................... ............................................ .......................................... ..................................... ......................................
multi-bag 65 < We<85
......................................... ............................................ .......................................... ..................................... ......................................
shear 80 < We<350 120 > We>85
......................................... ............................................ .......................................... ..................................... ......................................
enough temporal resolution. A high-intensity halogen lamp is used as the backlighting source for
this procedure. The high-resolution images are captured with the aid of a 4MP CCD camera to
obtain magniﬁed images of the droplet structure. Here, an Nd-YAG laser with 10 ns pulse is used
as the backlight source. The shallow depth of focus of the zoom-lens helps in getting images with
good details of the drop structure.
3. Resultsanddiscussion
Table 1 shows the different modes and the corresponding We range observed in the experiments
performed in this study compared with those given in the literature. Although all studies
qualitatively agree on the order of appearance of different regimes with increasing Weber number,
the exact transition We differs. This can been attributed to variation in the viscosity of the ﬂuids
used and the exact experimental set-up employed. We have carried out simulations for Weber
numbers 20, 40, 80 and 120 spanning the bag breakup, stamen breakup, multi-mode breakup and
shear-stripping regimes, respectively. Experiments have also been performed for similar Weber
numbers, and we compare the numerical results with the experimental ﬁndings in terms of
length and timescales of deformation and subsequent breakup. Figure 2 shows the morphology
of the drop during its breakup at various Weber numbers. Figure 2a–d shows the formation of a
single bag at We = 20, bag with a stamen at We = 40, multi-lobed bag (multi-bag) at We = 80 and
shear-thinning mode at We = 120. In what follows, we discuss each of these modes in detail.
(a) Bagmode( We=20)
Chou & Faeth [ 8] showed that the bag-breakup regime of secondary breakup of a droplet can
be divided into four stages. During the initial stage, the spherical droplet deforms into a disc
shape forming an oblate spheroid. In the next stage, a hollow bag is formed which is attached
to a toroidal rim (basal ring). Subsequently, the thin bag breaks up into tiny droplets leaving
behind an intact toroidal rim. In the ﬁnal stage, the rim breaks up into droplets owing to Rayleigh–
Plateau-type instability. We capture all the above-described stages of bag-breakup regime in our
experiment for We = 20 (ﬁgure 3) and the corresponding simulation (shown in ﬁgure 4).
The timescales of breakup are generally measured using the characteristic secondary breakup
time, t
c (equation (1.1)). A typical characteristic timescale for a drop of size 0.5 mm at We = 20
for ρl/ρg = 1000 is 0.56 ms. In the present experiments, the size of the droplet studied is 230 µm
and corresponds to tc ∼ 110 µs. The temporal evolution in our experiments ( ﬁgure 3) shows that
the breakup of the drop occurs at this timescale with initial ﬂattening culminating at t/tc ∼ 1.31,
breakup of the bag occurs at t/tc ∼ 2.6 and ﬁnally the breakup of the toroidal rim at t/tc ∼ 3.6.
Figure 4 shows the temporal evolution of an initially spherical droplet at We = 20 obtained
from the simulations. The sequence clearly shows the different stages of bag-breakup, namely the
ﬂattening of the initially spherical droplet ( ﬁgure 4c at t/tc = 1.34), subsequent formation of the
Downloaded from royalsocietypublishing.​org/​rspa/​article-pdf/​doi/​10.​1098/​rspa.​2014.​0930/​366722/​rspa.​2014.​0930.​pdf
by China Institution user
on 31 August 2026

<!-- PDF_PAGE: 7 -->

7rspa.royalsocietypublishing.orgProc. R. Soc. A471:20140930 ...................................................
(b)(a)
(c) (d)
100 mm
100 mm 100 mm
100 mm
Figure2. Dropmorphologyduringitsbreakupat We=(a)20(bagbreakup),( b)40(bag-stamenbreakup),( c)80(multi-bag
breakup)and( d)120(shearstrippingbreakup).
bag (ﬁgure 4d at t/tc = 1.79) and its breakup ( ﬁgure 4g at t/tc = 2.50). The toroidal rim shown in
ﬁgure 4 breaks up into droplets of sizes much larger than those obtained from the breakup of
the bag sheet. Results from our simulations are in good agreement with those obtained from the
experiments for the same We.
The mechanism of drop deformation and breakup is governed by an interplay of aerodynamic,
capillary and viscous forces. The deformation is essentially caused by the aerodynamic forces,
whereas the capillary and viscous forces, respectively, resist and delay deformation of the droplet.
At low Ohl,g < 0.1, as is the case in this study, the viscous forces play little role in the drop breakup.
Figure 5a shows the drop proﬁles at the centreline plane along the streamwise direction. Proﬁles
have been obtained at equal intervals of /Delta1t/tc = 0.23. The drop starts to deform into a staircase
pyramid (shown by the brown contour) with little motion of the rear end of the drop which
merely ﬂattens (also see ﬁgures 4b and 3a corresponding to t/tc = 0.45). This behaviour is also
in agreement with earlier experimental studies [ 8,48] (also see [ 49]). The ﬂattening is essentially
owing to the high pressure zones at the front and rear stagnation points at the droplet surface.
The pyramid subsequently ﬂattens further resulting into a saucer-shaped structure which shows
a tendency of forming a backward facing bag at the rear end as is the case in rising bubbles (and
also seen in earlier simulations for low density ratios [ 40,50]). The initiation of bag formation
occurs over a streamwise distance of approximately 3 D
0 which is in good agreement with the
Downloaded from royalsocietypublishing.​org/​rspa/​article-pdf/​doi/​10.​1098/​rspa.​2014.​0930/​366722/​rspa.​2014.​0930.​pdf
by China Institution user
on 31 August 2026

<!-- PDF_PAGE: 8 -->

8rspa.royalsocietypublishing.orgProc. R. Soc. A471:20140930 ...................................................
60 ms
240 ms 280 ms
bag rupture
nodes
200 ms
500 mm
Figure3. Experimentalresultsfor We=20.Thesquareboxesinthefigureencircleadropundergoingbreakupatdifferent
instances( a) t/tc =0.55,(b) t/tc =1.82,(c) t/tc =2.18and(d) t/tc =2.55.Here,tc =110µs.Airflowisfromrighttoleft.
(a)
(g)( h)( i)
(b)
bag
rupture
nodes
(c)( d)( e)( f )
Figure 4.Numerical simulation forWe=20 att/tc (a)0 ,(b) 0.45, (c) 0.90, (d)1 . 7 9 ,(e)2 . 2 4 ,(f) 2.50, (g) 2.54, (h) 2.60,
and( i)3.40.Airflowisfromlefttoright.(Onlineversionincolour.)
experiments (ﬁgure 3b,c). The bag membrane gets thinner and thinner as it is stretched out but
remains attached to the toroidal rim. For We = 20, the bag membrane ﬁrst shows formation of
holes as shown in ﬁgure 4 g. The growth of holes leads to formation of thin ligaments on the
surface of the bag which subsequently breakup into tiny droplets owing to Rayleigh–Plateau
instability (ﬁgure 4h). The mechanisms of bag-sheet breakup in different bag-breakup regimes
are discussed later in §3f. The leftover toroidal rim, as also observed in experiments [ 48,51],
Downloaded from royalsocietypublishing.​org/​rspa/​article-pdf/​doi/​10.​1098/​rspa.​2014.​0930/​366722/​rspa.​2014.​0930.​pdf
by China Institution user
on 31 August 2026

<!-- PDF_PAGE: 9 -->

9rspa.royalsocietypublishing.orgProc. R. Soc. A471:20140930 ...................................................
–0.5
–1.5 0.4
0.6
0.8
1.0
1.2
–1.0
0.05
0.10
0.15
–0.5
0
0.5
1.0
1.5
(a) (b)
0 0.5 01
t/t
c
21.0 1.5
X/D
Y/D
Cd
u/U•
2.0 2.5 3.0
Figure5. (a)Initialinterfaceevolutionfor We=20.therimregionand( b)variationindragcoefficient, Cd,andthevelocityof
thedrop, u,withtimefor We=20(Onlineversionincolour.)
shows formations of nodes (ﬁgures 3d and 4i) which result in bigger droplets, and the remaining
connecting segments undergo Rayleigh–Plateau breakup.
Formation of a bag has been argued to be a result of RTI of the saucer-shaped disc formed by
the ﬂattening of the initially spherical droplet as shown inﬁgure 5a. At the maximum deformation
(cross-stream diameter is Dmax), the ﬂattened drop is uniformly thick in the whole region except
for slightly thicker edges where rim formation starts. Once the bag starts forming the rim starts
to draw in more liquid as seen in the images ( ﬁgure 4 f –h) and acts as a support to the bag.
Zhao et al. [48] argued that the bag formation occurs when Dmax is larger than the critical RTI
wavelength, λc. The most dominant wavelength of RTI is given by [52],
λmax =
√
3λc = 2π
√
3γ
ρla , (3.1)
where a is the acceleration of the drop andλc is the critical wavelength beyond which the ﬂattened
drop would be unstable to RTI. Using the position of the centroids at different time instances, the
acceleration of the droplet just before the initiation of bag formation can be estimated [48]. A non-
dimensionalized RTI wavenumber, given by K = Dmax/λmax, takes values between 1 /
√
3–1 for
bag breakup regime [48]. In our simulations, the value of K for the case of We = 20 is 0.988 which
agrees well with the experimental observations of Zhao et al .[ 48]. We note here that for sheets
(ﬂattened drop here) the ﬁnite thickness affects the critical and the dominant mode of Taylor
instability (see [53]). Following reference [53], where stability of thin sheets accelerated in a lighter
medium was studied, we compute the critical wavelength using their equation (30). The critical
wavelength for the We = 20 case is obtained as 1.63 times λ
c. Clearly, there would be substantial
discrepancy in the prediction of the threshold We number for transition from bag to bag-stamen
regime. Also, because the deformed drop is ﬁnite in the transverse direction, the nature of Taylor
instability would be further modiﬁed, and the possibility of other mechanisms governing the
bag formation cannot be ruled out completely. Nevertheless, in our simulations for We = 20 and
We = 40 (shown later), we ﬁnd that the above-deﬁned RTI number K based on λ
max correctly
predicts the bag and bag-stamen formation, respectively.
Further, formation of nodes (or digitations) at the rim are also a result of RTI as the rim
accelerates along with the drop. Thus, in the bag breakup regime, the number of nodes on the
rim is given by, Nn = Lrim/λmax = π/
√
3– π,w h e r eLrim is the length of the rim [ 48,51]. This
suggests that, in the bag-breakup regime, typical number of nodes expected range from one to
four. In our simulations, we obtain formation of two nodes (ﬁgure 4h,i) which agree well with the
corresponding experimental observations (ﬁgure 3d,f ) for the same aerodynamic Weber number
of We = 20.
Downloaded from royalsocietypublishing.​org/​rspa/​article-pdf/​doi/​10.​1098/​rspa.​2014.​0930/​366722/​rspa.​2014.​0930.​pdf
by China Institution user
on 31 August 2026

<!-- PDF_PAGE: 10 -->

10rspa.royalsocietypublishing.orgProc. R. Soc. A471:20140930 ...................................................
Drag coefﬁcient can be estimated from the streamwise acceleration, a, of the drop,
Cd = 4D0
3
ρla
ρa(U∞ − u)2 , (3.2)
where u is the velocity of the centre of mass of the drop. Figure 5b shows the variation of drag
coefﬁcient with time along with the variation in velocity of the drop.
The drag coefﬁcient initially increases owing to the ﬂattening of the drop and peaks (Cd ∼ 1.3)
when the drop has ﬂattened to Dmax and at this instant it starts forming the bag ( ﬁgure 5 b).
During this period, the mean velocity of the droplet continues to increase but is still only
5% of U∞ (see curve with open squares with readings on the right-hand-side axis). Upon the
formation of the bag, the drag coefﬁcient progressively decreases. Figure 5b shows that the drop
velocities, even after the bag formation, are only approximately 10% of the ambient gas velocity.
The drag coefﬁcient for the initially spherical droplet is Cd = 0.46 which is in agreement with
the empirical value of approximately 0.45 (see [54]) for the Reynolds numbers used here. For the
ﬂattened disc conﬁguration at around t/tc = 1.3, Cd ∼ 1.3 which is also in good agreement with
the corresponding drag coefﬁcient of CD = 1.2 for disc-shaped solids (cf. [55]). The initial increase
and subsequent decrease in the drag coefﬁcient is also in agreement with earlier experimental
results of [8].
The left-over rim upon bag breakup eventually breaks up into droplets larger than the ones
produced by bag rupture. This results in a bimodal distribution as also observed in experiments
[8]. We discuss the variation in maximum cross-stream diameter of the droplet, Dmax, with time
and the droplet size and velocity distributions, together with other bag-breakup regimes, later
in §3e–f.
(b) Bag-and-stamenmode( We=40)
For higher magnitudes of We (24 < We < 85; table 1 ), attained by increasing the free stream
velocity, the drop disintegration transitions from the single bag breakup mode into multimode
breakup. Multimode breakup regime can be further categorized into several different breakup
modes of which bag-stamen mode has been observed to occur at the lower end of Weber numbers
((24 < We < 45; see [ 48]). As observed for the single bag-breakup regime, the drop initially
ﬂattens on encountering the stream of uniform high-speed air ﬂow (see ﬁgure 6 a–f showing
drop ﬂattening captured in simulations and ﬁgure 7 a, showing experimental observations)
and subsequently a bag starts forming as shown in ﬁgure 6g and corresponding experimental
observations shown in ﬁgure 7b. Also, fromﬁgure 6g (and ﬁgure 7c), it is clear that the bag surface
undergoes a bulge in the centre which eventually leads to the formation of stamen. In contrast to
the bag-breakup regime discussed above for We = 20 where rupture of the bag is initiated by hole
formation, the bag membrane rupture at We = 40 is initiated by formation of slits as shown in
ﬁgure 6h. Interestingly, the bag undergoes slight folding near the rim (ﬁgure 6) where we observe
formation of ﬁrst slits. As the gap between the slit widens, the sheet splits up into multiple threads
which eventually breakup into smaller droplets owing to Rayleigh–Plateau instability as shown
in ﬁgure 6 i. Finally, the whole of bag undergoes breakup fragmenting into a large number of
small droplets and leaving behind a toroidal rim and a stamen at the centre ( ﬁgure 6 h). This
slit-like hole formation could be numerical as well owing to the representation of the interface
using a ﬁnite grid size. Nevertheless, the effect of thinning of the bag on rupture dynamics for
higher We is clearly indicated. At lower We = 20, we note that the hole formation agrees well with
experimental observations. The stamen is an elongated cylindrical ligament, as also observed in
experiments (ﬁgure 7d), and is roughly of the same size as that of the rim. It is also characterized
by a bigger nodal droplet at its windward tip. As the breakup proceeds, the nodal droplets both
from the rim and the stamen get pinched off. Both the stamen and the rim result in droplets much
larger than the ones produced by bag rupture as shown in ﬁgure 6k. We also observe a couple of
thread-like structures which connect the stamen with the rim. The features captured in the present
simulations are in good agreement with the experimental results shown in ﬁgure 7.
Downloaded from royalsocietypublishing.​org/​rspa/​article-pdf/​doi/​10.​1098/​rspa.​2014.​0930/​366722/​rspa.​2014.​0930.​pdf
by China Institution user
on 31 August 2026

<!-- PDF_PAGE: 11 -->

11rspa.royalsocietypublishing.orgProc. R. Soc. A471:20140930 ...................................................
bag rupture
(a)
(h)( i)( j)( k)
(b)( c)( e)( g)( f )(d)
nodes stamen
Figure6. Numericalsimulationofdropbreakupfor We=40att/tc (a)0,( b)0.25,(c)0.63,(d)0.89,(e)1.33,(f)1.52,(g)1.9,
(h)1.96,(i)2.03,(j)2.22,and(k)2.75.Airflowisfromlefttoright.(Onlineversionincolour.)
60 ms
500 mm
stamen
260 ms
220 ms
280 ms
Figure 7.Experimental results forWe=40. The square boxes encircle a drop undergoing breakup at different instances
(a) t/tc =0.65,(b) t/tc =2.39,(c) t/tc =2.83and(d) t/tc =3.04.Heretc =92µs.Airflowisfromrighttoleft.
Figure 11a shows the evolution of drop shape up to bag formation. It can be observed that
owing to the high stagnation pressure, the leeward side of the drop moves little and shows
formation of a depression towards the windward side. This is in contrast with the We = 20 case
where the leeward side of the droplet merely stagnates and its movement is essentially in the
downstream direction (ﬁgure 5a). Figure 11a clearly shows that in the drop reference frame there
are two stages in which the leeward side of the drop has negative displacement: one is during
ﬂattening and second is in the later stages of bag formation where the centre of the ﬂattened
drop forms a bulge towards the windward side. Subsequently, owing to RTI, this perturbation
grows and draws liquid from the bag sheet to form a stamen (see [ 22,48]). Because RTI plays
a major role in the bag and stamen formation, we argue that the RT wavenumber dictates the
Downloaded from royalsocietypublishing.​org/​rspa/​article-pdf/​doi/​10.​1098/​rspa.​2014.​0930/​366722/​rspa.​2014.​0930.​pdf
by China Institution user
on 31 August 2026

<!-- PDF_PAGE: 12 -->

12rspa.royalsocietypublishing.orgProc. R. Soc. A471:20140930 ...................................................
X/D0 X/D0
Y/D0
3.0
1.0
0.1
0
0.2
0.3
0.4
0.5
1.1
1.2
1.3
1.4
1.5(a)( b)
3.1 3.2 3.3 3.3 3.4 3.5 3.6 3.7 3.83.4 3.5
Figure8. Velocityvectorsinthereferenceframemovingwiththevelocityofthedropcentroidshowingflowin( a)therim
regionand( b)nearthecentreofthedropat t/tc =1.90.
mode of breakup. The value of non-dimensionalized wavenumber, K, for the We = 40 case is 2.05
suggesting formation and growth of two crests, one corresponding to the rim deformation and
another corresponding to the bulge in the centre leading to formation of stamen ( ﬁgure 11a). We
note here that according to Zhao et al. [48], the bag-stamen breakup regime occurs for K ∈ (1 − 2).
To verify further if the exact mechanism of stamen is indeed RTI, we plot the velocity vectors
drawn in the reference frame of the moving droplet ( ﬁgure 8). Figure 8a shows the rim portion
receiving ﬂuid from the bag region, and similarly, ﬁgure 8b shows that the central region of the
bag receives ﬂuid from the bag region. This suggests that the central region and the rim of the
drop are two nodes of RTI and receive progressively more ﬂuid from the thinning bag which is
the anti-node of RTI.
The number of nodes expected to form at the rim in the bag-stamen regime, as predicted in
reference [48], is between π to 2π (i.e. 3–6). In our simulations as well as experiments, we observe
formation of four nodes (ﬁgures 6j and 7d). The mechanism of formation of nodes at the rim is
similar to the We = 20 case discussed in the previous section.
(c) Multi-bagmode( We=80)
As We is increased further there is a transition into the next regime of breakup termed as the
multi-bag breakup. While the initial development of the bag (captured in simulations as shown
in ﬁgure 9 a–e and in experiments as shown in ﬁgure 10 a,b) looks very similar to the single-
bag and bag-stamen breakup, the differentiating part is the formation of multiple lobes on the
bag membrane (see ﬁgure 9h,i and in experiments ﬁgure 10c). This particular regime, involving
formation of multiple lobes, has been a recent observation even in the experimental studies
[14,51]. The fewer observations of this regime in the literature may be due to the fact that this
regime is observed only for a narrow range ofWe falling between the transitions of well-identiﬁed
regimes of bag-stamen and shear breakup. The formation of multiple bags is due to the Rayleigh–
Taylor-like instability in large liquid drops as shown for falling drops in [ 51]. The events that
follow from the initial ﬂattening of the drop are as follows. As the ﬂattened region starts to bulge
out, the precursors to the lobes may readily be observed in the form of multiple dents on the bag.
The interconnections between these lobes form thread-like structures (marked in ﬁgure 9i and in
experiments in ﬁgure 10d) holding the lobes together. In our simulation for We = 80, we observe
formation of four such lobes, and subsequently, each bag-shaped lobe continues to disintegrate
similar to breakup of the bag in the bag-stamen breakup regime. The interconnecting thread-
like structures that hold the lobes together, upon breakup of the lobes into tiny droplets, form
Downloaded from royalsocietypublishing.​org/​rspa/​article-pdf/​doi/​10.​1098/​rspa.​2014.​0930/​366722/​rspa.​2014.​0930.​pdf
by China Institution user
on 31 August 2026

<!-- PDF_PAGE: 13 -->

13rspa.royalsocietypublishing.orgProc. R. Soc. A471:20140930 ...................................................
rim
retraction
bag
rupture
threads joining
multiple bags
(a)( b)( c)( e)( g)( f )(d)
(h)( i)( j)
Figure9. Numericalsimulationfor We=80att/tc (a)0,( b)0.54,(c)0.71,(d)0.89,(e)1.20,(f)1.38,(g)1.65,(h)1.74,(i)1.96,
and( j)2.77.Airflowisfromlefttoright.(Onlineversionincolour.)
40 ms8 0 ms
500 mm
160 ms140 ms
multiple
bags
Figure10.Experimentalresultsfor We=80.Thesquareboxesinthefigureencircleadropundergoingbreakupatdifferent
instances( a) t/tc =0.75,(b) t/tc =1.50,(c) t/tc =2.64and(d) t/tc =3.02.Here,tc =53µs.Airflowisfromrighttoleft.
ligaments and nodes similar to that of the rim. The rim itself exhibits behaviour similar to that
observed in the single-bag and bag-stamen regimes discussed earlier.
Figure 11 b shows the evolution of drop proﬁles at the centre-plane in the simulations. The
initial deformation of the drop is similar to that seen for We = 40. However, few features
especially in the later stages of droplet deformation are different from the We = 40 case. The
drop deformation was very symmetric for We = 20 and We = 40 (ﬁgures 5a and 11a). For We = 80,
the undulations appear on the droplet surface owing to RTI ( K = 2.2) and their growth leads to
Downloaded from royalsocietypublishing.​org/​rspa/​article-pdf/​doi/​10.​1098/​rspa.​2014.​0930/​366722/​rspa.​2014.​0930.​pdf
by China Institution user
on 31 August 2026

<!-- PDF_PAGE: 14 -->

14rspa.royalsocietypublishing.orgProc. R. Soc. A471:20140930 ...................................................
X/D
Y/D
–0.5
–1.5
0.5
1.0
0
–0.5
–1.0
–1.0
–0.5
0
1.5
1.0
0.5
(a)( b)
0.50 1.0 1.5 2.0 2.5 3.0
X/D
–0.5 0.5 0 1.0 1.5 2.0
Figure11.Initialinterfaceevolutionfor( a) We=40(b) We=80.(Onlineversionincolour.)
thickening of rims and the central region as the bag sheet thins. During the formation of the
bag, the asymmetric undulations lead to a thicker rim in the top portion of the drop. The initial
tendency of the rim is to deform in the streamwise direction owing to the shearing caused by
the high-speed gas stream. As it progressively thins, owing to shearing, the local surface tension
forces increase and overcome the shearing forces. Subsequently, the rim retracts back forming
a visibly thicker rim in the top region of the drop. Owing to asymmetry the drop experiences
a moment and rotates slightly with the thicker region advancing ahead. Moreover, the thicker
region is fed with more liquid from the thinner region owing to RTI. Therefore, the thicker region
continues to grow thicker ( ﬁgure 11 b) as the drop continues to deform into bag-shaped lobes
as discussed above. We argue that the multi-bag regime is characterized by the RTI similar to
the bag-stamen breakup, but the nonlinear dynamical structures are different and instead of
formation of a single bag with a thin stamen at the centre, four connected lobes are formed.
We note that the multi-bag mode discussed above is different from the dual bag breakup
mode observed in [ 15] which occurs at relatively lower We. In our experiments, we consistently
observed the multi-bag regime in the narrow range of We ∼ 65–85.
(d) Shear-strippingregime( We=120)
Shear-stripping regime is observed at high aerodynamic Weber numbers ( table 1 ). Although
the initial ﬂattening is similar to previous cases, the high-speed ﬂow over the periphery of
the drop initiates the formation of ligaments owing to RTI even before the drop has ﬂattened
completely (see ﬁgures 12c–e and 13 showing simulation results and experimental observations,
respectively). Owing to stripping of the liquid from the periphery, the formation of a rim which
could have supported a possible bag is hindered. In contrast to We = 80, where the retraction
of the rim was observed, for We = 120 the high inertial forces overcome the restoring effect of
surface tension ( ﬁgure 12 a–c). The ligaments formed subsequently owing to RTI are stretched
in the streamwise direction and ﬁne droplets are continuously pinched-off from their free ends
owing to Rayleigh–Plateau instability as shown in ﬁgure 12d–h. A considerable volume of the
initial drop is stripped-off through this process, and the size of the residual drop rapidly reduces
and the effective Weber number decreases, and thus further breakup of the drop may transition to
bag or vibration mode. In the present simulations, although bulk of the droplet undergoes shear
stripping, formation of a smaller bag is observed forWe = 120 case (ﬁgure 12e–f ). The drop sizes in
the shear stripping regime, owing to rapid breakup of the droplet by formation of ligaments and
their Rayleigh–Plateau breakup, are not expected to exhibit bi-modal distribution as observed in
the bag-breakup regimes but a lognormal distribution (shown later in §3f). Figure 13 shows the
Downloaded from royalsocietypublishing.​org/​rspa/​article-pdf/​doi/​10.​1098/​rspa.​2014.​0930/​366722/​rspa.​2014.​0930.​pdf
by China Institution user
on 31 August 2026

<!-- PDF_PAGE: 15 -->

15rspa.royalsocietypublishing.orgProc. R. Soc. A471:20140930 ...................................................
ligaments
bag rupture
backward facing
bag
(a)( b)( c)( e)
(g)( f )
(d)
(h)
Figure12.Numericalsimulationfor We=120att/tc (a)0,( b)0.33,(c)0.66,(d)1.21,(e)1.43,(f)1.81,(g)2.23,and(h)2.53.
Airflowisfromlefttoright.(Onlineversionincolour.)
corresponding experimental observations of the breakup of a drop at We = 120. The simulations
are in agreement with the experimental observations, and we observe that the drop initially
ﬂattens and subsequently undergoes a shear stripping breakup. As observed in the experiments
(ﬁgure 13d), simulations show that as the drop undergoes a shear breakup, some remnants are
left which remain intact for 15 − 20D
0 downstream of the drop injection point ( ﬁgure 12i). We
note that, both in the experiments as well in simulations presented here, the breakup of the bulk
of drop volume occurs within x ∼ 5–10 D
0. Figure 14a,b shows velocity vectors and the contours
of the streamwise component of velocity at t/tc = 0.66 and 0.8, respectively. The contours have
been plotted only inside the droplet. The ﬁgure shows that the periphery of the droplet has
maximum streamwise velocity and a boundary layer formation in the drop is clearly visible with
the rear end of the drop having lower velocities, and the velocity on the windward side increases
progressively from the central region to the periphery. The shearing of the periphery in the
streamwise region leads to a completely different morphological evolution when compared with
the bag-breakup regimes discussed previously in this study. Figure 14a shows that although the
velocity ﬁeld during the initial ﬂattening is similar to the bag-breakup regime, the rim retraction
is not observed in the shear-stripping regime and owing to higher aerodynamic forces, the drop
periphery continues to gain velocity (ﬁgure 14b) and eventually breaks up owing to RTI.
We showed above that the different regimes of drop breakup observed in experiments are
captured well in the numerical simulations presented in this study. In what follows, we discuss
in detail the various features observed in the bag breakup regime, namely initial ﬂattening of the
drop into a disc, subsequent formation of the bag and its breakup, and the formation of the rim.
Drop size and velocity distributions for drop breakup at different We have also been discussed.
(e) Disccharacteristicsandrimformation
As discussed earlier, at higher Weber numbers ( We ≥ 20), surface tension forces are weaker
compared with aerodynamic forces and thus the drop initially, for a short duration, merely
deforms without gaining momentum from the ambient uniform ﬂow. This is primarily because,
for the low Ohnesorge values ( Oh < 0.1) studied here, the viscous effects are negligible in
comparison with the inertial forces and therefore, the momentum does not diffuse through the
drop at such short timescales. Moreover, owing to the high density ratio, the momentum transfer
at the windward side results in smaller velocities in the drop. The drop deforms from a spherical
Downloaded from royalsocietypublishing.​org/​rspa/​article-pdf/​doi/​10.​1098/​rspa.​2014.​0930/​366722/​rspa.​2014.​0930.​pdf
by China Institution user
on 31 August 2026

<!-- PDF_PAGE: 16 -->

16rspa.royalsocietypublishing.orgProc. R. Soc. A471:20140930 ...................................................
40 ms
500 mm
onset of
shear-stripping
20 ms
120 ms60 ms
Figure 13.Experimental resultsfor We=120. The squareboxes encircle a dropundergoingbreakupat differentinstances
(a) t/tc =0.54,(b) t/tc =1.08,(c) t/tc =1.62and(d) t/tc =3.24.Here,tc =37µs.Airflowisfromrighttoleft.
0.1
0.50
0.55
0.60
0.65
0.09
0.06
0.05
0.04
0.03
0.01
0 0.03
0.04
0.05
0.05
0.06
0.07
0.07
0.07
0.08
0.10
0
0.70
0.75
0.80
0.85
(a)( b)
0.2
X/D0
U/U•
U/U•
Y/D0
Y/D0
0.65
0.70
0.75
0.80
0.85
0.90
0.60
0.35 0.40 0.45 0.50 0.55 0.60 0.65 0.70
X/D0
0.3 0.4
Figure14.Velocityvectorsneartherimregionat( a) t/tc =0.66and(b) t/tc =1.32.Contoursshowtheaxialvelocity, u/U∞ .
(Onlineversionincolour.)
shape into a stair-cased pyramid and ﬁnally into a disc. During the pyramid formation, the
drop ﬂattens at both the upstream and downstream ends owing to sandwiching effect caused
by high pressures at both upstream and downstream ends of the drop. For We = 40 and 80, the
sandwiching effect is more pronounced thus resulting in a signiﬁcant upstream motion of the
rear end of the droplet ( ﬁgure 11a,b). Nevertheless, the maximum cross-stream diameter of the
drop attains a value of around approximately 2 in all the bag breakup regimes. Figure 15 shows
variation in the maximum cross-stream diameter,Dmax, of the drop with time for We = 20, 40 and
80. Initially, the cross-stream diameter increases linearly with time and formation of the bag, at
around t/t∗= 1.7, is marked by a change over to a steeper slope. The increased growth rate of
D
max for all the regimes is essentially owing to the higher pressure caused by the stagnation of
the gas in the bag which results in a radial outward force on the rim [8]. The change in the growth
rate of D for different We has been attributed to higher RT instability growth rates corresponding
to higher values of drop acceleration, a, with increasing We [56]. Chou & Faeth [8] suggested the
following empirical relation for the bag breakup regime,
D
D0
= 1.0 + 0.5 t
tc
0 ≤ t
tc
≤ 2 (3.3)
Downloaded from royalsocietypublishing.​org/​rspa/​article-pdf/​doi/​10.​1098/​rspa.​2014.​0930/​366722/​rspa.​2014.​0930.​pdf
by China Institution user
on 31 August 2026

<!-- PDF_PAGE: 17 -->

17rspa.royalsocietypublishing.orgProc. R. Soc. A471:20140930 ...................................................
0
Dmax/D0
1
2
3
4
12
t/tc
34
We=2 0
We=4 0
We=8 0
present experiment (bag)
present experiment (bag-stamen)
present experiment (multi-bag)
Chou and Feath (1998)
Zhao et al. (2013)
Cao et al. (2007)
Figure15.Variationinthemaximumcross-streamdiameterofthedropwithtime.Filledsymbolsshowsimulationresults,open
symbolsshowexperimentalresults,andthesolidandbrokenlinesaretheexperimentalcorrelationsfrompreviousstudies.
and Zhao et al. [56] suggested the following for the bag-stamen breakup mode:
D
D0
= 1.0 + 0.55
( t
tc
)5/3
0 ≤ t
tc
≤ 1.5. (3.4)
Cao et al. [15] presented an empirical relation for the dual-bag breakup regime given by,
D
D0
=
⎧
⎪⎨
⎪⎩
1.0 0 ≤ t
tc
≤ 0.3
0.59 + 1.34 t
tc
0.3 ≤ t
tc
≤ 0.99
(3.5)
Figure 15 shows that the bag-breakup regimes observed in our simulations as well as experiments
fall within the different empirical relations given by equations (3.3)–(3.5) for bag and dual-bag
breakup regimes with that for bag-stamen (equation (3.4)) between them.
A theoretical estimate of the extent of maximum deformation can be obtained by performing
a balance between the capillary and pressure forces on the drop. By performing a pressure
balance between the drop and the ambient ﬂow in an approximated oblate deformation of the
drop at the stagnation point and the drop periphery:P
B − PA = γκA and Pdrop − PB = γκB,w h e r e
subscripts A and B denote quantities evaluated at the stagnation and periphery locations of the
drop, respectively, P is the pressure and curvatures κA = 2Ds/D2
max and κB = Dmax/D2
s + 1/Dmax,
we obtain ( Dmax
D0
)5
+
( D0
Dmax
)
− 2
( D0
Dmax
)4
= C We
2 . (3.6)
Here, Dmax and Ds are the cross-stream diameter and minor-axis, respectively. Equation (3.6) uses
volume constraint D2
maxDs = D3
0 and PA − PB = CρgU2
∞ /2. The coefﬁcient, C, can be assumed
to be approximately 2 for ﬂow past a sphere. For We = 20, 40 and 80, equation (3.6) predicts
Dmax/D0 = 1.81, 2.09 and 2.40, respectively. This expression was derived without the use of any
empirical coefﬁcients, in contrast to reference [57], where Dmax/D0 = 1 + 0.19We1/2 was obtained
by using similar arguments but eventually an experimental ﬁt was performed to obtain the
correlation. The above correlation due to [57] yields similar values for a range of We, for example,
Downloaded from royalsocietypublishing.​org/​rspa/​article-pdf/​doi/​10.​1098/​rspa.​2014.​0930/​366722/​rspa.​2014.​0930.​pdf
by China Institution user
on 31 August 2026

<!-- PDF_PAGE: 18 -->

18rspa.royalsocietypublishing.orgProc. R. Soc. A471:20140930 ...................................................
1.4
0.6
0.7
0.8
0.9
(a)( b)
1.5 1.6
X/D
Y/D
1.7 1.7 1.8 1.9
X/D
2.0
Figure16.Rimdynamicsfor We=80.Shapeoftherimat( a) t/tc =1.43and(b) t/tc =1.52.Thisinitialforwarddeformation
isobservedinexperimentsin figure10bwhereairflowisfromrighttoleft(alsoseeinsimulationsin figure9d).(Onlineversion
incolour.)
for We = 20, we obtain 1.85 which is close to the value estimated using equation (3.6). The estimate
from equation (3.6) is also in good agreement with the maximum deformationDmax ∼ 1.8 and 2.15
observed in the simulations presented here and also in previous experimental studies of Chou &
Faeth [8] (approx. 1.8 for bag mode) and [ 48] (2.15 for bag-stamen mode). For We = 80, Dmax/D0
obtained in simulations is approximately 2.2 and the above theoretical and empirical expressions
(equation (3.6) yields 2.4 and the correlation owing to Hsiang & Faeth [57] gives 2.7) overpredict.
Bag formation critically depends on the formation of a torus rim which supports the bag
during its further growth and eventual breakup. Previous numerical studies for low drop to
ambient density ratios show the formation of ﬂatter rims and a backward facing bag (see
[40,50,58]). However, in this study, we simulate drop breakup for a higher density ratio (approx.
1000) and obtain a forward facing bag, forWe = 20, 40 and 80, with thicker and circular torus rims.
The retraction velocity of a rim attached to a planar sheet is given by [59] (also see [51]) as,
vret =
( 2γ
ρlh
)1/2
. (3.7)
Here, h is the thickness of the ﬁlm, which for the case of bag breakup corresponds to the thickness
of the bag. Because the retraction velocity of the rim is inversely proportional to the ﬁlm /bag
thickness, it increasingly counters the effect of shear on the rim, owing to the ambient gas
ﬂow, that drags it forward and eventually the rim retracts. Non-dimensionalizing the retraction
velocity with the characteristic liquid velocity in the bag, D0/tc, we obtain
v∗
ret =
( 2
h∗ We
)1/2
, (3.8)
where h∗ = h/D0 and v∗
ret = vrettc/D0. This expression indicates that with increasing We, the
retraction velocity would decrease and beyond a criticalWe, rim retraction shown in the ﬁgure 16
would not occur. Figure 16 shows the ﬁlm retraction phenomenon for We = 80 at time t/tc = 1.43
and t/tc = 1.52, respectively. Figure 16 shows the cross section of the drop taken at z = 0 (central)
plane. The rim moves from x/D0 = 0.93 to x/D0 = 0.89 in 0.089tc, thus giving a retraction velocity
of approximately 0.44D0/tc. For the bag breakup atWe = 80, h∗ = 0.15 and the estimatedv∗
ret (from
equation (3.8)) is 0.41 which is in close agreement with the observed rim velocity ofv∗
ret = 0.44 for
We = 80 in the simulations presented here. The rim retraction velocity can also be predicted by
coupling the equations (3.6) and (3.8) using the fact that the rim thickness ( h) will be of the order
of the thickness of the disc formed by the initial deformation of the droplet i.e.πD2
maxh/4 = π/6D3
0.
Downloaded from royalsocietypublishing.​org/​rspa/​article-pdf/​doi/​10.​1098/​rspa.​2014.​0930/​366722/​rspa.​2014.​0930.​pdf
by China Institution user
on 31 August 2026

<!-- PDF_PAGE: 19 -->

19rspa.royalsocietypublishing.orgProc. R. Soc. A471:20140930 ...................................................
Figure17.Ruptureofthebagfor We=20att/tc =(a)2.5(b)2.53.(Onlineversionincolour.)
The dependence of rim formation on We can also be understood by estimating the local
Weber number at the rim, Werim. Considering the local value of We at the rim surface, Werim ∼
We drim/D0 (where the diameter of the rim, drim is obtained from the simulations), for We = 120
results in Werim = 12 which is above the critical drop breakup Weber number, whereas forWe = 80,
we obtain Werim = 4 which is substantially smaller than the criticalWe and therefore rim retraction
is expected for We = 80. Experimentally, it has been observed that the drop transitions from bag
breakup regime to shear-stripping in the range of We ∼ 80–120.
A prominent feature of rim morphology is the presence of digitations (or node-like structures)
in the bag-breakup regime. Similar structures have been observed during the high-speed gas-
assisted atomization of a liquid jet [ 60]. Beyond a critical speed of gas, undulations on the liquid
jet become non-axisymmetric and form nodes with spacing λ
max (equation (3.1)). Therefore, the
number of nodes expected are given by N = Lring/λmax,w h e r eLring is the total length of the rim.
Similar observations were made in [ 48] for the breakup of a drop in gas crossﬂow. Zhao et al.
[48] assumed, to estimate the number of nodes, that the perturbations on the drop periphery
(rim or basal ring) appear just before the initiation of the bag formation, however, we argue
(ﬁgure 4e) that the perturbations can be seen on the drop periphery as soon as the windward
side of the drop has ﬂattened. These perturbations grow into varicose undulations and eventually
lead to the formation of nodes (as also shown in [ 61] for the breakup of Kelvin–Helmholtz rolls
during the gas-assisted atomization of a liquid jet). The bi-modality of the PDF of size distribution
of fragmented droplets observed during bag breakup is essentially because of the presence of
the large size droplets caused by node formation. These droplets contain a substantial fraction
(approx. 89% for We = 20) of the volume of the unfragmented drop.
(f) Bagfragmentationandtimescales
The mechanism of fragmentation of bag has been much debated and is still not well understood
[25]. Although it is clear that the fragmentation is caused by the continuous stretching of the thin
bag, the exact nature of the instability is still not known essentially owing to the associated small
timescales which limit the experimental observations. Jalaal & Mehravaran [ 58] and also Khare
et al. [50], in their simulations for low density ratios, show that the breakup of the bag is initiated
by the formation of holes and their further growth leads to the formation of ligaments. Figure 17
shows the formation of holes and their growth for bag breakup at We = 20. The formation of hole
and their subsequent expansion leading to bag rupture are similar to those observed in bursting
of thin ﬁlms (see ﬁg. 5ao f[ 62]). These features are difﬁcult to observe in experiments of drop
breakups owing to the extremely small timescales.
Downloaded from royalsocietypublishing.​org/​rspa/​article-pdf/​doi/​10.​1098/​rspa.​2014.​0930/​366722/​rspa.​2014.​0930.​pdf
by China Institution user
on 31 August 2026

<!-- PDF_PAGE: 20 -->

20rspa.royalsocietypublishing.orgProc. R. Soc. A471:20140930 ...................................................
(a)( b)
(b)
(d)
(c)
(c)( d)
Figure18.Fragmenteddropfor We=80shownat t/tc =2.07.Zoomedinviewofdifferentregionsmarkedwithopenboxes
areshownin( b–d).(Onlineversionincolour.)
Figure 18 shows the ruptured lobes for We = 80 and the details of the progress of the breakup
near the rim. The four connecting threads are still intact even after the breakup of the bag and
are clearly visible in ﬁgure 18 a. The rupture of the bag shows interesting features of the rim
behaviour for We = 80. The formation of nodes of the rim is inﬂuenced by the breakup of the
lobes (ﬁgure 18b) and a section of the rim appears to breakup into threads (ﬁgure 18c). Figure 18d
shows that the thread, that was supporting a pair of lobes, is intact and is attached to the rim.
The rupture of the bag can be explained by sheet instability mechanism proposed in [ 63]a n d
further extended in [ 53] by accounting for surface tension and using ﬁrst-order perturbations.
Bremond & Villermaux [62] used the analytic solution of [53] for comparing the rate of growth of
perturbations in the instability of vanishingly thin layers of capillary number ≪1. The dominant
wavenumber predicted in [ 53] is given by Kmax = (ρla/3γ)1/2. Because the whole of the bag
surface can be assumed to move with nearly the same acceleration, the instability during breakup
would correspond to a thin band of wavenumbers (∼ K
max) and therefore result in a narrow band
of drop size distribution (shown later). During the destabilization stage, the ﬁlm is ﬁrst perforated
with tiny holes which grow to form thin liquid threads at their respective boundaries.
Liu & Reitz [ 30] argued, based on their experimental observations, that the bag breakup
mechanism essentially occurs by the stretching of the bag in the streamwise direction and leads
to formation of the ligaments aligned along the direction of the gas ﬂow. Stapper & Samuelsen
[64] proposed the above ‘stretched streamwise ligament breakup’ mechanism for ﬂat liquid
sheets exposed to high speed co-ﬂowing gas. Strapper & Samuelsen [ 64] showed that although
the streamwise breakup mode is present, the dominant mode is still the spanwise breakup
mode. Nevertheless, the ligaments so formed by either modes, subsequently align along the
streamwise direction owing to the high velocity of the co-ﬂowing gas which is also observed
in our simulations as well as in experiments.
Figure 19a–d shows drop size distributions for We = 20, 40, 80 and 120, respectively. Because
both the left and right arms of the distributions are smooth, we believe the distributions have
been appropriately captured in the simulations. Sauter mean diameter (SMD) is a measure of
the quality of spray. The SMD /D
0 for We = 20, 40, 80 and 120 are 0.082, 0.064, 0.033 and 0.03,
respectively. As expected, the SMD reduces with increase in We. Figure 19a shows the bimodal
Downloaded from royalsocietypublishing.​org/​rspa/​article-pdf/​doi/​10.​1098/​rspa.​2014.​0930/​366722/​rspa.​2014.​0930.​pdf
by China Institution user
on 31 August 2026

<!-- PDF_PAGE: 21 -->

21rspa.royalsocietypublishing.orgProc. R. Soc. A471:20140930 ...................................................
700
600
500
400
300
200
100
0
0
d/D0d/D0
1000
2000
3000
4000
5000
6000
70003500
3000
2500
2000
1500
1000
500
0
0
0.05 0.10
0.0050.0100.0150.0200.0250.0300.0350.040 0.01 0.02 0.03 0.04 0.05 0.06 0.07
0
0.02 0.04 0.06 0.08 0.10 0.12
0
0
N
N
10
20
30
40
50
60(a)( b)
(c)( d)
Figure19.Dropletsizedistributionfor We=(a)20(b)40( c)80and( d)120.Correspondingcurvesdrawnarethelognormal
fit(1/(xσ
√
2π)e−(ln x−μ)2/(2σ2),where x = d/D0.)withtheparameters( a) μ =− 3.35(forthehigherpeakinthedash-
dotcurve)and −2.801(fortheshorterpeakinthedash-dottedcurve),bothwithsame σ =0.5842.Theselognormalfits
arederivedusingBayesianinformationcriterion.Thedashcurve,obtainedusingkernel-basedfitting,indicatesthebimodal
distribution.( b)μ =− 3.42,σ =0.45(c)μ =− 4.34,σ =0.34(d)μ =− 3.76,σ =0.31.(Onlineversionincolour.)
behaviour for bag breakup at We = 20 with two distinct peaks in the PDF, one at approximately
0.02D0 and another at 0.05–0.06D0.G e l f a n d[9] also showed bimodal behaviour of the distribution
which is essentially due to the droplets formed during rim breakup. With increase in We to 40,
the second peak subsides and the peak at approximately 0.02 D0 becomes more prominent. For
higher We, 80 and 120, the number of smaller droplets corresponding to the peak at 0.02 D0
increases substantially and the larger fragments are nearly absent. The lognormal distributions
show a good ﬁt with parameters μ =− 3.19,−3.42, −4.34, −3.76 and σ = 0.58, 0.45, 0.34, 0.31 for
We = 20, 40, 80 and 120, respectively. Hsiang & Faeth [ 57] motivated by the results of Ruff et al.
[65] for densely atomized sprays suggested a lognormal distribution function with the mass mean
diameter (MMD) to SMD ratio of 1.2. Their experimental results, for a range of We and Oh < 0.1,
were scattered in a thin band of MMD/SMD ∈ (1.1–1.5). In the simulations presented in this study,
the MMD/SMD ratio for We = 20, 40, 80 and 120 are 1.2, 1.33, 1.47 and 1.49, respectively, which
are in good agreement with the previous studies.
The initial deformation timescale, Tini, of approximately 1.3–1.6 tc compares well with the
experimental correlation of [ 57], Tini = 1.6tc/(1 − Oh/7) ∼ 1.6tc,p r o p o s e df o rWe < 103.I no u r
experiments, we observe that initial ﬂattening of the drop, for We = 20, completes at t/tc = 1.32
and for We = 120 at t/tc = 1.05. Timescales of initial ﬂattening and subsequent breakup of the bag
for different We show good agreement between the simulations and the experiments presented in
this study.
Downloaded from royalsocietypublishing.​org/​rspa/​article-pdf/​doi/​10.​1098/​rspa.​2014.​0930/​366722/​rspa.​2014.​0930.​pdf
by China Institution user
on 31 August 2026

<!-- PDF_PAGE: 22 -->

22rspa.royalsocietypublishing.orgProc. R. Soc. A471:20140930 ...................................................
4. Conclusion
In this study, we investigate the breakup of a drop by performing volume of ﬂuid based
simulations for moderate aerodynamic Weber numbers (20 < We < 120) and compare the
results with the experiments performed using a continuous jet setup. Simulations have been
performed with water–air density ratio of 1000 : 1 and therefore compare quantitatively well
with experiments for corresponding values of We. These are the ﬁrst three-dimensional drop
breakup simulations for high-density ratios spanning all the bag breakup regimes. The bag
breakup regimes, viz. the bag breakup, bag-and-stamen breakup, multibag breakup and shear
breakup regimes, are well captured in the present simulations and the breakup processes agree
well with the observations made experimentally in this study as well as in earlier experiments
[8,15,48,56]. The deformation timescales as well as breakup structures are also in close quantitative
agreement with the experiments. The variation of D
max/D0 is in agreement with the previous
studies for all the values of We.
We observe an interesting transition regime between bag and shear breakup forWe = 80 where
we observed formation of multiple lobes, instead of a single bag, which are connected to each
other via thicker rim-like threads that hold them. In our experiments, we observed such a multi-
bag breakup in a thin band of Weber number, 65 < We < 85, and occurs in the multi-mode (bag
to shear breakup transition) regime. Such a breakup has not been studied sufﬁciently previously.
We show that the formation of multiple bags, like the formation of stamen in bag-stamen mode,
is also due to RTI.
From our simulations, we identify the rim dynamics which results in the transition between
the bag breakup and shear breakup, for We = 80 and We = 120, respectively. The velocity of the
rim retraction in the simulations agree well with the theoretical values of the Culick velocity
obtained for an average ﬁlm thickness of the bag. We show that for highWe = 120 the shear forces
drag along the rim and lead to stretching of the periphery of the drop in the streamwise direction
thus resulting in a backward facing bag with streaming of drop from the periphery. On the other
hand, for We = 80, rim shows a tendency of getting sheared by the ﬂow but upon subsequent
deformation retracts back leading to the formation of a more circular and stable rim.
The resultant drop sizes obtained in the simulations follow lognormal distributions with
SMD/MMD ratio approximately 1.2 which is in agreement with the previous experimental
studies. The bimodal behaviour is seen for drop breakup at lower We = 20 and unimodal PDFs
are obtained for higher We. A complete understanding of the size distribution of droplets from
secondary atomization would be immensely important for developing more accurate secondary
breakup models for dense sprays [66].
Data accessibility.
The corresponding author may be contacted for the details on the Gerris implementation
(http://gfs.sourceforge.net) of the computational work and also the experimental set up.
Acknowledgements. The authors acknowledge the support rendered by B.V .S.S.U Prasad (Research Scholar,
Combustion and Spray Laboratory, Department of Mechanical Engineering, Indian Institute of Science,
Bangalore) in conducting the experimental work presented in this article.
Fundingstatement. No direct funding was used to perform this work.
Author contributions. G.T. and R.V .R. designed the study. M.J. and S.P .R performed the simulations. S.P .R
performed the experiments. G.T. drafted the manuscript. All authors gave ﬁnal approval for publication.
Conflictofinterests. The authors have no competing interests.
References
1. Villermaux E, Bossa B. 2009 Single-drop fragmentation determines size distribution of
raindrops. Nat. Phys. 5, 697–702. (doi:10.1038/nphys1340)
2. Tryggvason G. 1997 Computational investigation of atomization . AD-a353 519. Michigan
University.
3. Taylor G. 1963 The shape and acceleration of a drop in a high speed air stream. The Scientiﬁc
Papers of G.I. T aylor3, 457–464.
Downloaded from royalsocietypublishing.​org/​rspa/​article-pdf/​doi/​10.​1098/​rspa.​2014.​0930/​366722/​rspa.​2014.​0930.​pdf
by China Institution user
on 31 August 2026

<!-- PDF_PAGE: 23 -->

23rspa.royalsocietypublishing.orgProc. R. Soc. A471:20140930 ...................................................
4. Prandtl L. 1952 Essentials of ﬂuid dynamics: with applications to hydraulics aeronautics, meteorology,
and other subjects. New York, NY: Hafner Pub. Co..
5. Lefebvre A. 1988 Atomization and sprays . New York, NY: Taylor & Francis. Combustion
(Hemisphere Publishing Corporation).
6. Dai Z, Faeth G. 2001 Temporal properties of secondary drop breakup in the multimode
breakup regime. Int. J. Multiphase Flow 27, 217–236. (doi:10.1016/S0301-9322(00)00015-X)
7. Krzeczkowski SA. 1980 Measurement of liquid droplet disintegration mechanisms. Int. J.
Multiphase Flow 6, 227–239. (doi:10.1016/0301-9322(80)90013-0)
8. Chou W-H, Faeth G. 1998 Temporal properties of secondary drop breakup in the bag breakup
regime. Int. J. Multiphase Flow 24, 889–912. (doi:10.1016/S0301-9322(98)00015-9)
9. Gelfand B. 1996 Droplet breakup phenomena in ﬂows with velocity lag.Prog. Energy Combust.
Sci. 22, 201–265. (doi:10.1016/S0360-1285(96)00005-6)
10. Hanson A, Domich E, Adams H. 1963 Shock tube investigation of the breakup of drops by air
blasts. Phys. Fluids (1958–1988) 6, 1070–1080.
11. Hsiang L-P, Faeth G. 1995 Drop deformation and breakup due to shock wave and steady
disturbances. Int. J. Multiphase Flow 21, 545–560. (doi:10.1016/0301-9322(94)00095-2)
12. Pilch M, Erdman C. 1987 Use of breakup time data and velocity history data to predict the
maximum size of stable fragments for acceleration-induced breakup of a liquid drop. Int. J.
Multiphase Flow 13, 741–757. (doi:10.1016/0301-9322(87)90063-2)
13. Hinze J. 1955 Fundamentals of the hydrodynamic mechanism of splitting in dispersion
processes. AIChE J. 1, 289–295. (doi:10.1002/aic.690010303)
14. Theofanous T, Li G, Dinh T-N. 2004 Aerobreakup in rareﬁed supersonic gas ﬂows. J. Fluid
Eng.-T ASME 126, 516–527. (doi:10.1115/1.1777234)
15. Cao X-K, Sun Z-G, Li W-F, Liu H-F, Yu Z-H. 2007 A new breakup regime of liquid drops
identiﬁed in a continuous and uniform air jet ﬂow. Phys. Fluids 19, 057103. ( doi:10.1063/
1.2723154)
16. Liu AB, Reitz RD. 1993 Mechanisms of air-assisted liquid atomization. Atomization Spray 3,
55–75. (doi:10.1615/AtomizSpr.v3.i1.30)
17. Reinecke W, Waldman G. 1970 A study of drop breakup behind strong shocks with
applications to ﬂight. Tech. Report, SAMSO-TR-70-142, DTIC Document.
18. Wierzba A, Takayama K. 1988 Experimental investigation of the aerodynamic breakup of
liquid drops. AIAA J. 26, 1329–1335. (doi:10.2514/3.10044)
19. Joseph DD, Belanger J, Beavers G. 1999 Breakup of a liquid drop suddenly exposed to a high-
speed airstream. Int. J. Multiphase Flow 25, 1263–1303. (doi:10.1016/S0301-9322(99)00043-9)
20. Hwang SS, Liu Z, Reitz RD. 1996 Breakup mechanisms and drag coefﬁcients of high-speed
vaporizing liquid drops. Atomization Spray 6, 353–376. (doi:10.1615/AtomizSpr.v6.i3.60)
21. Theofanous T, Li G, Dinh T-N, Chang C-H. 2007 Aerobreakup in disturbed subsonic and
supersonic ﬂow ﬁelds. J. Fluid Mech. 593, 131–170.
22. Theofanous T, Li G. 2008 On the physics of aerobreakup. Phys. Fluids 20, 052103.
(doi:10.1063/1.2907989)
23. Giffen E, Muraszew A. 1953 The atomisation of liquid fuels . London, UK: Chapman & Hall.
24. Faeth G, Hsiang L-P, Wu P-K. 1995 Structure and breakup properties of sprays. Int. J.
Multiphase Flow 21, 99–127. (doi:10.1016/0301-9322(95)00059-7)
25. Guildenbecher D, Lopez-Rivera C, Sojka P. 2009 Secondary atomization. Exp. Fluids 46,
371–402. (doi:10.1007/s00348-008-0593-2)
26. Joseph D, Beavers G, Funada T. 2002 Rayleigh–Taylor instability of viscoelastic drops at high
weber numbers. J. Fluid Mech. 453, 109–132.
27. Rimbert N, Castanet G. 2011 Crossover between Rayleigh-Taylor instability and turbulent
cascading atomization mechanism in the bag-breakup regime. Phys. Rev. E 84, 016318.
(doi:10.1103/PhysRevE.84.016318)
28. Ranger AA, Nicholls J. 1969 Aerodynamic shattering of liquid drops. AIAA J. 7, 285–290.
(doi:10.2514/3.5087)
29. Engel OG. 1958 Erosion damage to solids caused by high speed collision with rain.J. Res. NBS
61, 47. (doi:10.6028/jres.061.006)
30. Liu Z, Reitz R. 1997 An analysis of the distortion and breakup mechanisms of high speed
liquid drops. Int. J. Multiphase Flow 23, 631–650. (doi:10.1016/S0301-9322(96)00086-9)
31. Zaleski S, Li J, Succi S. 1995 Two-dimensional Navier–Stokes simulation of deformation and
breakup of liquid patches. Phys. Rev. Lett. 75, 244–247. (doi:10.1103/PhysRevLett.75.244)
Downloaded from royalsocietypublishing.​org/​rspa/​article-pdf/​doi/​10.​1098/​rspa.​2014.​0930/​366722/​rspa.​2014.​0930.​pdf
by China Institution user
on 31 August 2026

<!-- PDF_PAGE: 24 -->

24rspa.royalsocietypublishing.orgProc. R. Soc. A471:20140930 ...................................................
32. Han J, Tryggvason G. 1999 Secondary breakup of axisymmetric liquid drops. i. acceleration
by a constant body force. Phys. Fluids 11, 3650–3667. (doi:10.1063/1.870229)
33. Khare P, Yang V. 2012 Phenomenology of secondary breakup of newtonian liquid droplets. In
50th AIAA Aerospace Sciences Meeting, Nashville, TN, 9–12 January .
34. Kékesi T, Amberg G, Wittberg LP. 2014 Drop deformation and breakup.Int. J. Multiphase Flow
66, 1–10. (doi:10.1016/j.ijmultiphaseﬂow.2014.06.006)
35. Feng JQ. 2010 A deformable liquid drop falling through a quiescent gas at terminal velocity.
J. Fluid Mech. 658, 438–462. (doi:10.1017/S0022112010001825)
36. Premnath K, Abraham J. 2005 Simulations of binary drop collisions with a multiple-relaxation-
time lattice-Boltzmann model. Phys. Fluids 17, 122105. (doi:10.1063/1.2148987)
37. Chang C-H, Deng X, Theofanous TG. 2013 Direct numerical simulation of interfacial
instabilities: a consistent, conservative, all-speed, sharp-interface method.J. Comput. Phys. 242,
946–990. (doi:10.1016/j.jcp.2013.01.014)
38. Theofanous T, Mitkin VV, Ng CL, Chang C-H, Deng X, Sushchikh S. 2012 The physics of
aerobreakup. II. viscous liquids. Phys. Fluids 24, 022104. (doi:10.1063/1.3680867)
39. Han J, Tryggvason G. 2001 Secondary breakup of axisymmetric liquid drops. ii. impulsive
acceleration. Phys. Fluids 13, 1554–1565. (doi:10.1063/1.1370389)
40. Khosla S, Smith CE, Throckmorton RP 2006 Detailed understanding of drop atomization by
gas crossﬂow using the volume of ﬂuid method. InILASS Americas, 19th Annual Conf. on Liquid
Atomization and Spray Systems, T oronto, Canada, 23–26 May.
41. Xiao F, Dianat M, McGuirk JJ. 2014 Large eddy simulation of single droplet and liquid jet
primary breakup using a coupled level set/volume of ﬂuid method. Atomization Spray 24,
281–302. (doi:10.1615/AtomizSpr.2014007885)
42. Brackbill JU, Kothe D, Zemach C. 1992 A continuum method for modeling surface tension.
J. Comput. Phys. 100, 335–354. (doi:10.1016/0021-9991(92)90240-Y)
43. Popinet S. 2003 Gerris: a tree-based adaptive solver for the incompressible euler equations in
complex geometries. J. Comput. Phys. 190, 572–600. (doi:10.1016/S0021-9991(03)00298-5)
44. Popinet S. 2009 An accurate adaptive solver for surface-tension-driven interfacial ﬂows.
J. Comput. Phys. 228, 5838–5866. (doi:10.1016/j.jcp.2009.04.042)
45. Tomar G, Fuster D, Zaleski S, Popinet S. 2010 Multiscale simulations of primary atomization
using gerris. Comput. Fluids 39, 1864–1874. (doi:10.1016/j.compﬂuid.2010.06.018)
46. Prosperetti A. 1981 Motion of two superposed viscous ﬂuids. Phys. Fluids 24, 1217–1223.
(doi:10.1063/1.863522)
47. Chen X, Ma D, Yang V, Popinet S. 2013 High-ﬁdelity simulations of impinging jet simulations.
Atomization Spray 23, 1079–1101. (doi:10.1615/AtomizSpr.2013007619)
48. Zhao H, Liu H-F, Li W-F, Xu J-L. 2010 Morphological classiﬁcation of low viscosity drop bag
breakup in a continuous air jet stream. Phys. Fluids 22, 114103. (doi:10.1063/1.3490408)
49. Renardy Y et al. 2003 Pyramidal and toroidal water drops after impact on a solid surface.
J. Fluid Mech. 484, 69–83. (doi:10.1017/S0022112003004142)
50. Khare P, Ma D, Chen X, Yang V. 2013 Drag coefﬁcients of deforming and fragmenting liquid
droplets. In ILASS-Americas, Pittsburgh, P A.
51. Reyssat E, Chevy F, Biance A-L, Petitjean L, Quéré D. 2007 Shape and instability of free-falling
liquid globules. Eur. Phys. Lett. 80, 34005. (doi:10.1209/0295-5075/80/34005)
52. Taylor G. 1950 The instability of liquid surfaces when accelerated in a direction perpendicular
to their planes. Proc. R. Soc. Lond. A 201, 192–196. (doi:10.1098/rspa.1950.0052)
53. Keller JB, Kolodner I. 1954 Instability of liquid surfaces and the formation of drops. J. Appl.
Phys. 25, 918–921. (doi:10.1063/1.1721770)
54. Kürten H, Raasch J, Rumpf H. 1966 Beschleunigung eines kugelförmigen feststoffteilchens
im strömungsfall konstanter geschwindigkeit. Chem. Ing. T ech. 38, 941–948. ( doi:10.1002/
cite.330380905)
55. Clift R, Grace J, Weber M. 1978 Bubbles, drops, and particles . New York, NY: Dover Publication.
56. Zhao H, Liu H-F, Xu J-L, Li W-F, Lin K-F. 2013 Temporal properties of secondary drop breakup
in the bag-stamen breakup regime. Phys. Fluids 25, 054102. (doi:10.1063/1.4803154)
57. Hsiang L-P, Faeth GM. 1992 Near-limit drop deformation and secondary breakup. Int. J.
Multiphase Flow 18, 635–652. (doi:10.1016/0301-9322(92)90036-G)
58. Jalaal M, Mehravaran K. 2012 Fragmentation of falling liquid droplets in bag breakup mode.
Int. J. Multiphase Flow 47, 115–132. (doi:10.1016/j.ijmultiphaseﬂow.2012.07.011)
59. Culick FEC. 1960 Comments on a ruptured soap ﬁlm. J. Appl. Phys. 31, 1128–1129.
(doi:10.1063/1.1735765)
Downloaded from royalsocietypublishing.​org/​rspa/​article-pdf/​doi/​10.​1098/​rspa.​2014.​0930/​366722/​rspa.​2014.​0930.​pdf
by China Institution user
on 31 August 2026

<!-- PDF_PAGE: 25 -->

25rspa.royalsocietypublishing.orgProc. R. Soc. A471:20140930 ...................................................
60. Marmottant P, Villermaux E. 2004 On spray formation. J. Fluid Mech. 498, 73–111.
(doi:10.1017/S0022112003006529)
61. Fuster D, Bague A, Boeck T, Moyne LL, Leboissetier A, Popinet S, Ray P, Scardovelli S, Zaleski
S. 2009 Simulation of primary atomization with an octree adaptive mesh reﬁnement and vof
method. Int. J. Multiphase Flow 35, 550–565. (doi:10.1016/j.ijmultiphaseﬂow.2009.02.014)
62. Bremond N, Villermaux E. 2005 Bursting thin liquid ﬁlms. J. Fluid Mech. 524, 121–130.
(doi:10.1017/S0022112004002411)
63. Taylor GI. 1959 The dynamics of thin sheets of ﬂuid ii. waves of ﬂuid sheets.P r o c .R .S o c .L o n d .
A 253, 296–312. (doi:10.1098/rspa.1959.0195)
64. Stapper B, Samuelsen G. 1990 An experimental study of the breakup of a two-dimensional
liquid sheet in the presence of co-ﬂow air shear. In28th AIAA Aerospace Sciences Meeting, Reno,
NV , 8–11 January.
65. Ruff GA, Wu P-K, Bernal LP, Faeth GM. 1992 Continuous- and dispersed-phase structure of
dense nonevaporating pressure-atomized sprays. J. Propul. Power 8, 280–289. ( doi:10.2514/
3.23475)
66. Apte S, Gorokhovski M, Moin P. 2003 LES of atomizing spray with stochastic modeling of
secondary breakup. Int. J. Multiphase Flow 29, 1503–1522. (doi:10.1016/S0301-9322(03)00111-3)
Downloaded from royalsocietypublishing.​org/​rspa/​article-pdf/​doi/​10.​1098/​rspa.​2014.​0930/​366722/​rspa.​2014.​0930.​pdf
by China Institution user
on 31 August 2026
