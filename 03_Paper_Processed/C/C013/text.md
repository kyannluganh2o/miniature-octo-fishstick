<!-- PDF_PAGE: 1 -->

J. Fluid Mech. (2020), vol. 904, A20. © The Author(s), 2020.
Published by Cambridge University Press
904 A20-1
doi:10.1017/jfm.2020.699
On the formation and recurrent shedding of
ligaments in droplet aerobreakup
Benedikt Dorschner1,†, Luc Biasiori-Poulanges2, Kevin Schmidmayer1,
Hazem El-Rabii2,† and Tim Colonius1
1Division of Engineering and Applied Science, California Institute of Technology, 1200 E. California
Blvd., Pasadena, CA 91125, USA
2Institut Pprime, CNRS UPR 3346 – Université de Poitiers – ISAE-ENSMA, 1 avenue Clément Ader,
86961 Futuroscope, France
(Received 2 March 2020; revised 13 May 2020; accepted 14 August 2020)
The breakup of water droplets when exposed to high-speed gas ﬂows is investigated using
both high-magniﬁcation shadowgraphy experiments as well as fully three-dimensional
numerical simulations, which account for viscous as well as capillary effects. After
thorough validation of the simulations with respect to the experiments, we elucidate the
ligament formation process and the effect of surface tension. By Fourier decomposition of
the ﬂow ﬁeld, we observe the development of speciﬁc azimuthal modes, which destabilize
the liquid sheet surrounding the droplet. Eventually, the liquid sheet is ruptured, which
leads to the formation of ligaments. We further observe the ligament formation and
shedding to be a recurrent process. While the ﬁrst ligament shedding weakly depends on
the Weber number, subsequent shedding processes seem to be driven primarily by inertia
and the vortex shedding in the wake of the deformed droplet.
Key words: high-speed ﬂow, breakup/coalescence, aerosols/atomization
1. Introduction
The interaction of a droplet with a gas stream involves a complex synergy of
aerodynamic forces and hydrodynamic instabilities that results in deformation and
fragmentation. This phenomenon occurs naturally during the fall of rain drops, as well as
in
a variety of technical applications including fuel injection (Allison, McManus & Sutton
2016), pharmaceutical sprays (Bolleddula, Berchielli & Aliseda 2010) and explosion
hazards (Eckhoff 2016). Over the last decades, the aerobreakup phenomenology has been
studied using experimental and numerical diagnostics, providing mostly two-dimensional
(2-D) data. As a result, a comprehensive understanding of the three-dimensional ( 3-D)
droplet fragmentation mechanisms remains elusive (Chen & Liang 2008;M e n g&
Colonius 2018). In particular, the ligament formation process and its subsequent breakup
is still poorly understood (Jalaal & Mehravaran 2014).
Early studies of droplet aerobreakup have identiﬁed various droplet morphologies by
varying the ﬂow conditions and droplet ﬂuid properties and the underlying deformation
mechanisms have been classiﬁed. For high density ratios and Reynolds numbers, Hinze
† Email addresses for correspondence: bdorschn@caltech.edu, hazem.elrabii@cnrs.pprime.fr
https://doi.org/10.1017/jfm.2020.699
 Published online by Cambridge University Press

<!-- PDF_PAGE: 2 -->

904 A20-2 B. Dorschner and others
(1955) ﬁrst deﬁned breakup modes and their transition based on the Weber number and
the Ohnesorge number. Subsequently, Krzeczkowski (1980) proposed mapping transitions
of the various breakup regimes on a We–Oh diagram, and by now a large number
of studies have contributed to this map (see reviews of Hinze 1955; Pilch & Erdman
1987; Faeth, Hsiang & Wu 1995; Guildenbecher, López-Rivera & Sojka 2009, 2011;
Lefebvre & McDonell 2017). Although there is a good agreement on the description of
the various morphologies of the deformed droplet, regime transitions (in terms of We
and Oh) and the mechanisms involved in the breakup process have been subjects of
debate.
Before the past two decades, the prevailing view was that the mode of droplet
breakup can be classiﬁed in ﬁve regimes for low Ohnesorge numbers ( Oh < 0.1), namely
vibrational, bag, multimode, stripping and catastrophic breakup. The vibrational regime
occurs for We < 11 due to the unstable development of oscillations at the natural frequency
(Pilch & Erdman 1987;W i e r z b a1990; Shraiber, Podvysotsky & Dubrovsky 1996)o ft h e
droplet causing its breakup into large fragments. Increasing the Weber number up to 80,
the aerobreakup is driven by the Rayleigh–Taylor instability (RTI) and breakup modes are
distinguished by their wavenumber. The one-wave conﬁguration corresponds to the bag
breakup regime (Lane 1951; Magarvey & Taylor 1956; Fishburn 1974; Gel’fand, Gubin
&K o g a r k o1974; Jalaal & Mehravaran 2012; Kulkarni & Sojka 2014;W a n get al. 2014)
where the droplet is ﬁrst deformed into a disc shape and then a thin hollow bag attached
to a toroidal rim, which is blown downstream and ﬁnally bursts. Later, the toroidal rim
breaks up due to
Rayleigh–Plateau instability (Jain et al. 2015). When the wavenumber
increases, more complex bag structures (including stamen Hanson, Domich & Adams
1963; Hirahara & Kawahashi 1992;G e l f a n d1996; Zhao et al. 2010, 2013 and multiple bags
Krzeczkowski 1980;H s i a n g&F a e t h1992, 1993, 1995;C a o et al. 2007) are formed and
fragmented, following a similar process. These structures are referred to as the multimode
breakup regime. For We < 350, capillary forces are overcome by shear effects and thus the
breakup occurs due to the stretching of ligaments at the droplet periphery. Literature relates
two competing modes for this Weber range known as shear-stripping regime (Ranger &
Nicholls 1969; Simpkins & Bales 1972;H s i a n g&F a e t h1992; Chou, Hsiang & Faeth 1997)
and shear-thinning regime (Liu & Reitz 1997; Han & Tryggvason 1999;L e e&R e i t z1999,
2000, 2001; Han & Tryggvason2001). Finally, forWe > 350,
the literature reports a highly
contested regime called catastrophic breakup (Harper, Grube & Chang 1972;R e i n e c k e&
Waldman 1975; Hwang, Liu & Reitz 1996; Joseph, Belanger & Beavers 1999; Theofanous
&L i 2008), related to the unstable growth of waves on the droplet upstream side (owing
to RTI). It is suggested that the droplet breaks up when the amplitude of the waves reaches
the size of the drop.
Recently, the experimental work of Theofanous, Li & Dinh ( 2004) and Theofanous
&L i( 2008) on aerobreakup in rareﬁed supersonic ﬂows, which was addressed
by means of shadowgraphs and laser-induced ﬂuorescence, showed that corrugations
attributed to Kelvin–Helmholtz instability (KHI) persist to higher Weber numbers. These
authors showed that the catastrophic breakup regime is an
artefact associated with the
line-integrated nature of shadowgraph visualizations of the 3-D complex ﬂow ﬁeld at the
upstream area of the droplet. As a result, they suggested a reclassiﬁcation of breakup
modes based on the hydrodynamic instabilities driving the aerobreakup. T wo regimes
are then proposed: Rayleigh–Taylor piercing (RTP), driven by RTI, combined with
aerodynamic drag forces and shear-induced entrainment (SIE), governed by the combined
action of the Kelvin–Helmholtz instabilities, shearing and local capillary mechanisms
(Theofanous 2011). Compared to the previous classiﬁcation, the RTP includes bag and
https://doi.org/10.1017/jfm.2020.699
 Published online by Cambridge University Press

<!-- PDF_PAGE: 3 -->

Ligament formation in aerobreakup 904 A20-3
multi-modes regimes while the SIE refers to the sheet-stripping (or sheet-thinning) mode.
The SIE is proposed as the terminal regime for We > 103.
The ligament formation process in the vicinity of the RTP–SIE transition and beyond
(i.e. We > 102) is, in particular, a subject of current investigation (Jalaal & Mehravaran
2014;J a i net al. 2015; Meng & Colonius 2018; Dorschner et al. 2019). This is mostly due
to the large range of spatial and temporal scales combined with the 3-D nature of the
breakup, which surpass the traditional 2-D experimental and numerical diagnostics used
and thus require sophisticated techniques to elucidate the intricate breakup mechanisms
(i.e.
3-D simulations or high-magniﬁcation and frequency optical diagnostics). For We >
102, a liquid sheet is stretched from the droplet periphery forming a cylindrical liquid
curtain around the droplet body. The axial symmetry of the liquid sheet is perturbed by
the development of instabilities arising at the liquid sheet surface. Due to these growing
instabilities, the liquid sheet is then disintegrated into ligaments, which are stretched and
broken up into smaller droplets.
In an attempt to describe the instabilities arising on the liquid sheet, Liu & Reitz
(1997) invoked a sheet-thinning mechanism, initially proposed by Stapper & Samuelsen
(1990). Stapper & Samuelsen ( 1990) showed that a liquid sheet subject to coﬂowing
gases results in cellular breakup patterns (Stapper & Samuelsen 1990) and subsequently
in the formation of ligaments due to growing streamwise and spanwise vortical waves
on the liquid sheet surface. Considering high-speed gas ﬂows, the streamwise waves
dominate and thus streamwise ligaments are formed. Ultimately, ligaments break up into
droplets. This mechanism is qualitatively supported by experimental observations (Lee
& Reitz 1999, 2000, 2001),
2-D numerical simulations (Han & Tryggvason 1999, 2001;
Wadhwa, Magi & Abraham 2007)a n d3-D volume-of-ﬂuid simulations (Khosla, Smith &
Throckmorton 2006;J a i net al. 2015).
Recently, Jalaal & Mehravaran ( 2014) proposed the transverse azimuthal modulation
concept (Marmottant & Villermaux 2004;K i m et al. 2006) as an alternative mechanism
to describe the instabilities growing on the liquid sheet. The authors argued that primary
Kelvin–Helmholtz waves may be subjected to a transverse destabilization owing to RTI.
Growing transverse crests on the Kelvin–Helmholtz waves are dragged with the ﬂow
to form ligaments in the streamwise direction. The authors provided good qualitative
agreement supporting the transverse azimuthal modulation concept by running 3-D
numerical simulations of droplet aerobreakup for Weber numbers up to 200. Due to the
lack of experimental observations of such a destabilization, they attempt to compare
their numerical simulations with theoretical predictions but failed to ﬁnd conclusive
quantitative evidence. The authors suspect the ‘simpliﬁcations in the current theories’ to
be responsible for their mismatch.
Most recent studies on the ligament formation are reported by Meng & Colonius ( 2018)
through
3-D numerical simulations. Comparing the magnitudes of the streamwise and
spanwise vorticities captured, the authors found poor agreement with the sheet-thinning
mechanism proposed by Liu & Reitz ( 1997). They pointed out a loss of symmetry of the
liquid sheet drawn from the periphery, which could support the azimuthal modulation
mechanism proposed by Jalaal & Mehravaran (2014). In an attempt to provide quantitative
evidence, they performed an azimuthal Fourier decomposition of the velocity ﬂow ﬁeld,
which showed only broadband instability growth for all modes and hence did not provide
further evidence of transverse RTI. Noteworthy in this respect is a recent numerical study
of spatially developing liquid jets (Zandian, Sirignano & Hussain 2019) that investigates
the correlation between vortex dynamics and interfacial instabilities and stresses the role
of upstream KHI in the atomization process
occurring downstream.
https://doi.org/10.1017/jfm.2020.699
 Published online by Cambridge University Press

<!-- PDF_PAGE: 4 -->

904 A20-4 B. Dorschner and others
In this paper, we perform fully three-dimensional numerical simulations of aerobreakup
events for a moderate Weber number and one without accounting for surface tension
to elucidate the mechanisms responsible for the ligament formation and the role of
surface tension. We also perform matched aerobreakup experiments using a shock-tube
facility. The breakup events are recorded by means of high-magniﬁcation, high-speed
shadowgraphy. Quantitative evidence of the azimuthal modulation
is found and discussed.
Secondly, we report what we believe to be the ﬁrst observation of recurrent shedding of
ligaments. The paper is structured as follows. The numerical model and the experimental
set-up are described in §§ 2 and 3, respectively. The validation of the numerical simulation
with respect to the experiments is presented in § 4. The mechanisms responsible for the
formation of ligaments and their recurrent shedding
behaviour are discussed in § 5.F i n a l l y ,
concluding remarks are made in § 6.
2. Numerical modelling
2.1. Governing equations and numerical method
The numerical simulation of aerobreakup is a computationally demanding task due
to the broad physics occurring at a large range of spatio-temporal scales. In general,
aerobreakup is governed by the compressible Navier–Stokes for the liquid and surround
gas ﬂow, and coupled by continuity and an equality of stresses at the deforming surface.
This can be
modelled by coupling two solvers or, more commonly , by adopting a
volume-of-ﬂuid approach and either explicitly tracking the interface or by capturing a
slightly diffused interface on the grid (Fuster 2019; Saurel & Pantano 2018). Examples
of interface-tracking approaches include free-Lagrange methods (Ball et al. 2000),
level-set/ghost-ﬂuid approaches (Abgrall & Karni 2001;L i u ,K h o o&Y e o2003; Liu, Yuan
&S h u 2011;P a n et al. 2018) or front-tracking schemes (Cocchi & Saurel 1997). While
such interface-tracking approaches have the advantage of a well-deﬁned, sharp interface
between components and thus (potentially) accurate interface dynamics, various issues
ranging from spurious pressure oscillations near the interface to lack of conservation make
these schemes less suitable for shock-dominated ﬂows or aerobreakup (see, e.g.
Fuster
(2019) and Saurel & Pantano ( 2018) for recent reviews on the topic).
Hence, to accurately simulate aerobreakup of a water droplet, we resort to
an interface-capturing scheme, combining a multicomponent ﬂow model with a
shock-capturing ﬁnite-volume method. These schemes are also known as diffuse interface
methods as the interface is not sharp and tracked explicitly but the scheme permits
some numerical diffusion of the interface. This allows for discrete conservation,
consistent thermodynamics in mixture cells and dynamically appearing or vanishing
interfaces. In addition, diffuse interface methods are generally more efﬁcient compared
to their interface-tracking counterpart, which is crucial for multi-scale problems such as
aerobreakup.
While there
exist a variety of multicomponent models, we consider immiscible ﬂuids
in mechanical equilibrium and use the model of Kapila et al. (2001). However, to ensure
robustness and stability of the scheme, a pressure-relaxation method is used to converge
from a pressure-disequilibrium formulation to mechanical equilibrium (Saurel, Petitpas
&B e r r y 2009). While valuable insight has been obtained with numerical studies of
aerobreakup in the past (see, e.g. Jalaal & Mehravaran 2014;G a r r i c k2016;L i uet al. 2018;
Meng & Colonius 2018;L i u et al. 2019; Marcotte & Zaleski 2019), the computational
costs quickly become prohibitive for the large range of scales in aerobreakup. Hence,
most commonly, artiﬁcial symmetries are imposed, which prohibit the formation of truly
https://doi.org/10.1017/jfm.2020.699
 Published online by Cambridge University Press

<!-- PDF_PAGE: 5 -->

Ligament formation in aerobreakup 904 A20-5
three-dimensional instabilities or do not account for any viscous or capillary effects, which
become important at later stages of the breakup. In order to capture these effects, we model
surface tension as proposed in Schmidmayer et al. (2017) and viscous effects are accounted
for by extending the models for mechanical equilibrium (Thévand, Daniel & Loraud 1999;
Périgaud & Saurel 2005; Coralic & Colonius 2014) to the non-equilibrium-pressure model.
For a notable study on the relevance of both viscous and inviscid instability mechanisms
in the context of two-phase mixing layer, we refer to Matas ( 2015).
The viscous, non-equilibrium-pressure multicomponent model with surface-tension
effects for two components reads as
∂α1
∂t + u ·∇ α1 = μ(p1 − p2),
∂α1ρ1
∂t + ∇· (α1ρ1u) = 0,
∂α2ρ2
∂t + ∇· (α2ρ2u) = 0,
∂ρu
∂t + ∇· (ρu ⊗ u + pI + Ω − τ) = 0,
∂α1ρ1e1
∂t + ∇· (α1ρ1e1u) + α1p1∇· u =− μpI(p1 − p2) + α1τ1 : ∇ u,
∂α2ρ2e2
∂t + ∇· (α2ρ2e2u) + α2p2∇· u = μpI(p1 − p2) + α2τ2 : ∇ u,
∂c
∂t + u ·∇ c = 0,
⎫
⎪⎪⎪
⎪
⎪
⎪
⎪
⎪
⎪
⎪
⎪
⎪
⎪
⎪
⎪
⎪
⎪
⎪
⎪
⎪
⎪
⎪
⎬
⎪⎪
⎪
⎪
⎪
⎪
⎪
⎪
⎪
⎪
⎪
⎪
⎪
⎪
⎪
⎪
⎪
⎪
⎪
⎪
⎪
⎪
⎭
(2.1)
where α
k, ρk, ek and pk indicate the volume fraction, the density, the internal energy and
the pressure of component k. Identity is denoted by I. The mixture variables for density,
pressure and velocity are denoted by ρ, p and u, respectively and are given by
ρ =
2∑
k=1
αkρk and p =
2∑
k=1
αkpk. (2.2a,b)
The capillary tensor reads
Ω =− σ
(
∥∇ c∥I − ∇ c ⊗ ∇ c
∥∇ c∥
)
, (2.3)
where σ is the surface-tension coefﬁcient and c is a colour function. The viscous stress
tensor for the mixture is given by
τ = 2η(1
2 (∇ u + (∇ u)T) − 1
3 (∇· u)I), (2.4)
where η is the mixture shear viscosity and the viscous stress tensor for component k
is denoted by τk. The pressure-relaxation coefﬁcient is given by μ and the interfacial
pressure is
pI = z2p1 + z1p2
z1 + z2
, (2.5)
where zk = ρkak is the acoustic impedance of component k. Note that the
pressure-relaxation terms can be obtained from the asymptotic limit of the Baer &
https://doi.org/10.1017/jfm.2020.699
 Published online by Cambridge University Press

<!-- PDF_PAGE: 6 -->

904 A20-6 B. Dorschner and others
Nunziato (1986) model in the limit of stiff velocity relaxation (see also Saurel et al. (2009)
for further details).
Due to p1 /= p2 in this model, the total-energy equation of the mixture is replaced by
the internal-energy equation for each component. Nevertheless, the mixture-total-energy
equation of the system can be written in the usual form
∂ρE + εσ
∂t + ∇· ((ρE + εσ + p)u + Ω · u − τ · u) = 0, (2.6)
where the total energy is
E = e + 1
2 ∥u∥2, (2.7)
and the internal energy is given by
e =
2∑
k=1
Ykek(ρk, pk). (2.8)
The capillary energy reads
εσ = σ∥∇ c∥. (2.9)
Note that (2.6) is redundant when solving internal-energy equations for both components.
However, it is included to ensure total-energy conservation also numerically (see Saurel
et al. (2009) for further details).
In (2.8), ek is deﬁned via an equation of state and Yk are the mass fractions
Yk = αkρk
ρ . (2.10)
Here, we consider a two-phase mixture of gas ( g) and liquid ( l). The gas is modelled by
the ideal-gas equation of state
pg = (γg − 1)ρgeg, (2.11)
with γg = 1.4. The liquid on the other hand is modelled by the stiffened-gas equation of
state
pl = (γl − 1)ρlel − γlπ∞ , (2.12)
where γl = 6.12 and π∞ = 3.43 × 108 Pa (Coralic & Colonius 2014; Meng & Colonius
2014, 2018).
Numerically, this model is solved in three steps, which are outlined below. First, the
hyperbolic non-equilibrium-pressure model is solved by neglecting surface-tension and
viscous effects and relaxation terms. Second, the viscous, surface-tension model is solved
and
, ﬁnally, in the last step, the pressure is relaxed until an equilibrium is reached. In
summary, the model is solved with the following steps:
(i) Solve hyperbolic pressure-disequilibrium model using a Godunov-type method. At
the volume–volume interfaces, the associated Riemann problem is computed using
the HLLC (Harten–Lax–van Leer–Contact) approximate solver.
(ii) Solve the viscous, surface-tension model.
(iii) Inﬁnite pressure relaxation ( μ →+ ∞ ), converging to the thermodynamically
consistent, mechanical-equilibrium model, coupled with a re-initialization
procedure ensuring conservation.
https://doi.org/10.1017/jfm.2020.699
 Published online by Cambridge University Press

<!-- PDF_PAGE: 7 -->

Ligament formation in aerobreakup 904 A20-7
A second-order-accurate MUSCL (monotonic upstream-centred scheme for conservation
laws) scheme with two-step time integration is used, where the ﬁrst step is a predictor
step for the second and the usual piecewise linear MUSCL reconstruction (Toro 1997)
is used for the primitive variables. In addition, the monotonized central ( Van Leer 1977)
slope limiter is combined with the THINC (tangent of hyperbola for interface capturing)
interface-sharpening technique to minimize interface diffusion (Shyue & Xiao 2014).
In order to resolve the wide range of spatial and temporal scales of
shock fronts and
interfaces, an adaptive mesh reﬁnement technique is employed (Schmidmayer, Petitpas &
Daniel 2019). The reﬁnement criteria are based on variations of volume fraction, density,
pressure and velocity.
This methodology is implemented in the open-source code ECOGEN (Schmidmayer
et al. 2020b), which has been validated, veriﬁed and tested in various set-ups ranging
from gas bubble dynamics problems, including free-space and wall-attached bubble
collapses, liquid–gas shock tubes, surface-tension problems and water-column breakup
due to high-speed ﬂow (see, e.g. Schmidmayer et al. 2017, 2019; Pishchalnikov et al. 2019;
Schmidmayer, Bryngelson & Colonius 2020a).
2.2. Problem deﬁnition
Aerobreakup occurs when a liquid drop is suddenly exposed to a high-speed gas ﬂow.
These initial conditions are typically generated using a planar shock due to its simplicity,
robustness and repeatability in both experiments and simulations without signiﬁcantly
interfering with the droplet or the evolution of the subsequent stages of the aerobreakup.
In the simulation, we match the experimentally measured mean
shock strength Ms ∼ 1.3,
the Reynolds number Re = usD0/ν and the Weber number We = ρgu2
s D0/σ,w h e r eD0,
us, ν and σ denote the initial droplet diameter, the post-shock gas velocity, the kinematic
viscosity of the gas and the surface-tension coefﬁcient. In the experiments we mainly
focus on the piercing regime with mean Weber numbers in the range of We = [200, 700].
Numerically, we conduct two simulations, where one matches a mean experimental Weber
number of We ∼ 470 and one
does not have any surface-tension effects, which is denoted
in the following as We →∞ . Note that We →∞ is purely nomenclature and does not
indicate the limiting process to inﬁnite Weber number. In both cases the Reynolds number
is set to Re ∼ 7000. Hence, we numerically probe and compare both the piercing and the
stripping
regimes.
The simulations are carried out in rectangular computational domain, which is given
by [− 7D0, 15D0] × [− 6D0, 6D0] × [− 6D0, 6D0]. The domain size was chosen based on
sensitivity studies, which aim to both minimize the inﬂuence of the domain boundary
conditions and the computational effort. Our results are in line with previous studies
(Meng & Colonius 2018). To capture the non-axisymmetric, three-dimensional modulation
of the droplet and its surrounding ﬂow ﬁeld, we refrain from imposing any symmetries
or simpliﬁcations and carry out full three-dimensional simulations for which the initial
computational mesh and the set-up are shown in ﬁgure 1 . The droplet is initially at rest
and placed at the origin. On all domain boundaries, non-reﬂective boundary conditions
(NRBC) are imposed. To ensure high spatial and temporal accuracy at reasonable
computational costs, the adaptive mesh is composed out of four grid levels, which are
adapted to follow the shocks, the interface and the turbulence. Here, we follow the
methodology established and validated in Schmidmayer et al. (2019), and reﬁne
cell i
for which the following criterion is fulﬁlled:
|XNb(i,j) − Xi|
min(XNb(i,j) − Xi) >ε , (2.13)
https://doi.org/10.1017/jfm.2020.699
 Published online by Cambridge University Press

<!-- PDF_PAGE: 8 -->

904 A20-8 B. Dorschner and others
12D0
12D0
NRBC
NRBC
NRBC
22D0
Pre-shock flow
Post-shock flow
Droplet, D0
Shock, 
M
s
NRBC
y
x
z
FIGURE 1. Initial computational mesh and set-up for the numerical simulation of aerobreakup.
y
x
z
FIGURE 2. Snapshot of the adaptively reﬁned mesh, coloured by mixture pressure.
where X indicates a given ﬂow variable and the criterion is tested for all neighbouring
cells, indicated by the subscript Nb(i, j), where the jth cell is the corresponding neighbour
of cell i. The threshold is conservatively set to ε= 0.04. For this set-up, we test the above
reﬁnement criterion for the ﬂow variables density, velocity, pressure and volume fraction
and reﬁne the cell if the criterion is
fulﬁlled for any of these variables. As a result, the
initial droplet is resolved by Dp = 140 points per diameter, which was increased compared
to Meng & Colonius ( 2018) in order to capture capillary effects such as the formation of
https://doi.org/10.1017/jfm.2020.699
 Published online by Cambridge University Press

<!-- PDF_PAGE: 9 -->

Ligament formation in aerobreakup 904 A20-9
Gas supply
Driver section
Purge tank Acoustic levitation
system
WindowUpstream
transition
Static pressure jauge
Thermometer
Vaccum pump
Solenoid valve
Double-membrane section
NI PXIe-1073
module
Instantaneous pressure
Downstream
transition
A1 A3 A4A2
C2C1 C3 C4
FIGURE 3. Shock-tube facility (side view).
ligaments during the course of the breakup. Note , however, that the selected resolution
is by no means able to capture all ﬁne-scale effects and the resolution required to do
so would far exceed currently available computational resources, even on the largest of
supercomputers (see, e.g. Meng & Colonius ( 2018) for estimates). However, as shown in
§ 4, the good agreement of the simulation with our experiments suggest that the resolution
is indeed sufﬁcient to capture most pertinent effects of aerobreakup and all phenomena
discussed here are observed both numerically and experimentally. The mesh adaptivity,
following both the droplet interface and the shock is exempliﬁed by a snapshot in ﬁgure 2
during the initial phase of the simulation. In addition, a conservative grid stretching
towards the domain boundaries ,a ss h o w ni nﬁgure 1, is used to further aid efﬁciency of
the computations. Finally, to avoid spurious symmetries originating from the artiﬁcially
symmetric initial conditions, we impose an initial velocity ﬁeld with random perturbations
of maximum O(10
− 4us). For the adaptive time marching scheme we maintain a maximum
Courant–Friedrichs–Lewy number of 0.3.
3. Experimental set-up
The shock tube is manufactured from several stainless steel pipes with shell thickness
of 5 mm and a circular cross-section of 52 mm diameter. The facility consists of three
components (ﬁgure 3): a driver section, a double membrane section and a driven section
which includes a test section of square cross-section of 46 mm × 46 mm. Both membranes
have the same burst pressure. The test section is connected on the driven section by
means of circular-to-square transitions. Transitions are smooth and designed to preserve
the area. The upstream transition is placed 1000 mm ahead from the
centre of the test
section to insure a sharp and planar front wave proﬁle. The test section is ﬁtted with two
oblong BK7 windows mounted opposite one another on its lateral sides to allow for optical
diagnostics (shadowgraph or laser-sheet visualization). The double-membrane section and
the driver section are pressurized with air at 75 % and 125 % of the burst pressure of the
membranes (Mylar sheets), respectively. The shock wave is initiated by abruptly purging
the double-membrane section through an extraction gas port. The driven section is ﬁlled
with ambient air at controlled temperature.
https://doi.org/10.1017/jfm.2020.699
 Published online by Cambridge University Press

<!-- PDF_PAGE: 10 -->

904 A20-10 B. Dorschner and others
To monitor the shock propagation, the instantaneous test section pressure is measured at
four lateral positions by dynamic high-speed pressure transducers ( denoted C in ﬁgure 3)
with acceleration compensation (Kistler 603B). They allow us to measure pressure
ﬂuctuations over a range from vacuum to 200 bar with a rise time of 1 μs. Each sensor
is coupled to a Kistler 5018A charge ampliﬁer ( denoted A in ﬁgure 3) with a bandwidth
of 200 kHz which converts the mechanical stress into an electrical signal (0–10 V). The
electrical signal is acquired using a National Instruments NI PXIe-1073 module with 16
input channels with a frequency sample of 60 MHz. The sensors have an active area of 5
mm diameter and are mounted in Pom-C
® holders. The active surface of the sensors is
installed ﬂush to the test section wall. These sensors are used to measure the shock-wave
velocity and the pressure jump, and are also exploited for the triggering of the high-speed
camera. Synchronization of the high-speed camera with the light source emission and the
breakup event is performed with a DG535 Digital Delay and Pulse Generator (Stanford
Research system).
During the experiments, the water drop is held in a stable equilibrium at the
cent r eo ft h e
test section by the sound radiation pressure of an ultrasonic standing wave generated by the
single-axis acoustic levitator. The levitator consists of a Langevin-type transducer coupled
to a mechanical ampliﬁer with a radiating surface 35 mm in diameter. The transducer
operates at a resonant frequency of 20 kHz and is driven by a 1.5 kHz ultrasonic power
supply. The radiating surface is mounted ﬂush with the inside bottom surface of the
chamber. Opposite to it, the upper surface of the chamber acts as a reﬂector of the acoustic
waves for standing wave generation. To avoid disturbing the aerobreakup process with the
sound radiation pressure, the levitation system is turned off following a voltage setpoint
from a pressure transducer monitoring the shock propagation.
Aerobreakup experiments are captured with a high-magniﬁcation shadowgraphy system.
The backlight illumination is provided by the laser-induced ﬂuorescence of a Rhodamine
6G dye solution ( ﬁgure 4 ). A high-power dual oscillator/single head diode-pumped
Nd:YAG laser (Mesa PIV , Continuum) delivering short pulses in the 120–180 ns range at
repetition rate up to 80 kHz is used to induce the ﬂuorescence. Visualization is performed
with a high-speed Fastcam Photron SA-Z equipped with a Maksutov–Cassegrain
catadioptric microscope (QM1 Questar). The maximum optical resolution is 1.6 μmw i t h
a magniﬁcation up to 125 : 1. The depth of focus is approximately 0.6 mm. The high-speed
camera and the dual-cavity laser are synchronized by a digital delay generator. More
details on the optical diagnostic are available in Biasiori-Poulanges & El-Rabii ( 2019).
Sequences of the images displayed are captured with camera settings adjusted to record
frames at 512 × 904 pixel resolution with a sampling frequency of 40 kHz. The average
laser output power is 30 W and the pulse width is 174 ns. The measured spatial resolution
of the imaging system was 6 .5 μm per pixel. The time of the shock-wave interaction
with the droplet ( t = 0) is determined by laser beam deﬂection with a continuous-wave
laser beam perpendicular to the ﬂow direction and tangent to the droplet front side. The
deﬂection is recorded with a photodiode with a 0 .9n s rise time.
4. Comparison of simulations and experiments
4.1. Droplet morphology
In order to compare the numerical simulation with images obtained from shadowgraphy
in the following sections, we extract isosurfaces of volume fraction αl = 0.01 from the
simulation, and colour them by velocity magnitude (see, also ﬁgures 5 and 7). Note
that diffuse interface methods, as employed here, can only provide a range in which
https://doi.org/10.1017/jfm.2020.699
 Published online by Cambridge University Press

<!-- PDF_PAGE: 11 -->

Ligament formation in aerobreakup 904 A20-11
Laser cavity 1
Diverging
lens
Pump
Rh6G/C2H6O
Fluorescent
cell
Test chamber
with
BK7 windows
Long-pass
filter
Acoustic
levitator
QM1 Questar
microscope
High-speed
cameraLaser cavity 2
Flow direction
FIGURE 4. High-magniﬁcation shadowgraphy system (axial view).
the interface is likely to be found and by construction cannot provide an exact or
deterministic location of the interface. While this leads to an ambiguous representation
of the droplet surface, a sensitivity study in Meng & Colonius ( 2018) led to the conclusion
that isosurfaces of a volume fraction α
l = 0.01 are believed to be fair for comparison
with experiments, considering the obscuring mist of the experiment, generated during the
course of the breakup.
Although this might seem a rather low volume fraction, it should
be pointed out that this still corresponds to a mass fraction of Yl ≈ 0.9. For comparison of
the numerical results with the experiment, we use, unless stated otherwise, the following
non-dimensionalization
x
∗ = x
D0
,τ = t us
D0
√ρs
ρ , (4.1a,b)
where x and t denote the dimensional location and time, respectively.
4.1.1. Finite Weber number case
At the ﬁrst stages of the aerobreakup process ( τ= 0.27 − 0.91), the numerical results
show the typical droplet shapes that experimental visualizations ( ﬁgure 5 )a n d the
literature report, with a good qualitative agreement with our experiment. First, the initial
droplet deforms into a mufﬁn-like shape, described by a spherical upstream side with lips
growing in the spanwise direction. The droplet core takes the shape of a conic cylinder
and the downstream side is ﬂattened into a planar interface (τ= 0.27). While the droplet is
continuously ﬂattened, the stretching of lips in the streamwise direction results in a toroidal
liquid rim ( τ= 0.47). Simultaneously, rear lips raise in the downstream side. Owing to
inertial forces, the rim at the droplet periphery is stretched, which deforms the droplet
into a crescent-like shape ( τ= 0.72). The rim begins to disintegrate into ligaments and
subsequently into fragments. For characteristic times from 0.00 to 0.72, contours, extracted
from the isosurfaces of the volume fraction α
l = 0.01 of the droplet, are overlaid on the
experimental visualizations in ﬁgure 6. The contours are initially in good agreement with
the experimental images. At later stages ( τ= 0.72 − 1.16), the numerical results and the
experimental visualizations both show a periodic distribution of ligaments, although there
are discrepancies in the precise shape. However, the ligament distribution in the numerical
simulation is consistent with the distribution experimentally observed , as detailed below
in § 5. Figure 5 shows that the toroidal rim is continuously sheared away with the ﬂow
for times τ= 0.72 − 1.16, which leads to a cylindrical curtain surrounding the droplet
core and a cavity behind. This results in a backward facing bag. The downstream end
of the bag bends in the spanwise direction , forming a second rim, hindering the ﬂow.
Subsequently, the rim is subject to the development of multiple bags in the streamwise
direction. Finally, bags are pierced by the ﬂow, similar to the bag and multimode breakup
regimes. The ligaments resulting from this piercing process are tied up to their ends by
https://doi.org/10.1017/jfm.2020.699
 Published online by Cambridge University Press

<!-- PDF_PAGE: 12 -->

904 A20-12 B. Dorschner and others
Lip
1 mm
Rim
Backward
facing bag
Backward
facing bag
Rim
Second rim
Rear lip
(e)(b)(a)( c)( d )
FIGURE 5. Numerical simulation of a water droplet aerobreakup (top two rows) and
experimental visualizations (bottom rows). Characteristic times are ( a) 0.00, ( b)0 . 2 7 ,(c)0 . 4 7 ,
(d)0 . 7 2a n d(e) 1.16. The timing information is for both experimental and numerical results
expected for the numerical image ( e) which corresponds to τ= 1.01. For the simulations, an
isosurface of volume fraction αl = 0.01 coloured by velocity magnitude is depicted from two
different perspectives. The scale bar refers to experimental results. The Weber numbers in the
simulation and the experiment are 470 and 492, respectively.
the annular ring. The periodic nature of the ligament distribution is further discussed
in § 5.1. The droplet core develops a square-like shape (see, e.g. ﬁgure 5 e). We believe
this is a physical instability that results from preferred ampliﬁcation of certain (even)
azimuthal wavenumbers. While ampliﬁcation of these same wavenumbers is also evident
in the We →∞ simulation, the droplet in that case does not evolve into a coherent square
shape. Therefore, as surface tension plays a role in the instability process, we speculate
that it could be related to
the polygonal instability (Labousse & Bush 2015) observed
in other vortical-interfacial ﬂows, but a deﬁnitive analysis awaits future work. In any
simulation, available physical instabilities have to be seeded by disturbances that break
the relevant symmetries, whether they are intentional (added to the initial conditions) or
unintentional (seeded by discretization artifacts). As was observed previously by Meng
(2016), an underlying Cartesian mesh appears to be capable, in the presence of a diffuse
interface, to provide sufﬁcient perturbation to axisymmetry to excite instabilities in a
grid-aligned fashion, even though the instability itself is physical. In that study, cylindrical
coordinates were preferred to eliminate this effect, especially because those simulations
https://doi.org/10.1017/jfm.2020.699
 Published online by Cambridge University Press

<!-- PDF_PAGE: 13 -->

Ligament formation in aerobreakup 904 A20-13
1 mm
(b)(a) (c) (d )
FIGURE 6. Overlaying of droplet contours from numerical results (red lines) on experimental
images at the early stages of the aerobreakup. Characteristic times are ( a) 0.00, ( b)0 . 2 7 ,
(c)0 . 4 7a n d( d) 0.72. The Weber number in the simulation and the experiment are 470 and
492, respectively.
lacked physical viscosity to otherwise regularize the singularities associated with inviscid,
interfacial ﬂow (e.g. Kelvin–Helmholtz). With the present limits on resolution, we are
therefore unable to offer a deﬁnitive conclusion on whether the ultimate square shape is
independent of the numerics. While the present results qualitatively compare well with
experimental images when viewing the droplet from the side, we are unable to view the
droplet from upstream as would be required to directly view the square shape and directly
validate the result.
4.1.2. Simulation without surface tension
Next, in order to isolate the effect of surface tension during the breakup, we conduct
an additional numerical simulation and set the surface tension to zero with Ms = 1.3a n d
D0 = 0.804 mm and compare the results with experiments at a high Weber number of
We = 1100 (Ms = 1.3, d0 = 1.68 mm).
Figure 7 shows that the droplet morphology and the mechanisms observed bear
resemblance to the ﬁnite Weber number case, especially in the early stages. The droplet
is ﬁrst deformed into a mufﬁn-like shape with lips growing in the spanwise direction.
Lips are rapidly sheared away with the ﬂow by forming a liquid rim surrounding the
droplet body. The rim stretches in the streamwise direction and forms a cylindrical
curtain, which eventually results in a backward facing bag. Finally
, and in contrast to the
morphology previously observed in ﬁgure 5, much less distinct ligaments are formed and
the liquid curtain breaks up directly into ﬁne-scale structures due to a lack of the restoring
surface-tension forces.
4.2. Centre-of-mass evolution
Further validation is provided in ﬁgure 8 where the droplet centre-of-mass drift from
the numerical simulation is compared with that measured in the experiments. From the
numerical simulation the
centre-of-mass is computed as in Meng & Colonius ( 2018) using
xc =
∫
Ω D
αlρl xdV
∫
Ω D
αlρldV
, (4.2)
https://doi.org/10.1017/jfm.2020.699
 Published online by Cambridge University Press

<!-- PDF_PAGE: 14 -->

904 A20-14 B. Dorschner and others
1 mm
(e)(b)(a)( c)( d )( f )
FIGURE 7. Numerical simulation of a water droplet aerobreakup and experimental
visualizations. Characteristic times are (a) 0.00, (b) 0.20, (c) 0.52, (d)0 . 7 3 ,(e)0 . 8 6a n d(f ) 0.96.
The scale bar refers to experimental results. In the experiment, the Weber number is We = 1100,
whereas the simulation does not account for surface-tension effects, i.e. We →∞ .
where Ω D is the entire computational domain. On the experimental side, the evolution
of the centre-of-mass is computed from 2-D planar images, due to the line-integrated
nature of the images recorded by the shadowgraph. The centre-of-mass is determined by
calculating the ﬁrst-order spatial moment which is the intensity-weighted average of the
pixel coordinates constituting the droplet. This requires a binary image. The binarization
is performed by setting an intensity threshold to the image separating the droplet from the
background. Despite a slight deviation due to the 2-D planar assumption and the threshold
sensitivity, ﬁgure 8 shows a good quantitative agreement between numerical results and
the experiments. It can be noticed that the surface tension has no discernible effect on the
drift in the simulations. This observation is consistent with the similar droplet morphology
observed in both simulations at We = 470 and We →∞ .
5. Formation of ligaments
For We > 102, the process of ligament formation is traditionally described by the
sheet-thinning mechanism proposed by Liu & Reitz ( 1997) on the basis of the work of
Stapper & Samuelsen ( 1990) for the breakup of a two-dimensional liquid sheet. Recently,
the formation of ligaments has been re-evaluated (Jalaal & Mehravaran 2014;M e n g&
Colonius 2018) through 3-D numerical simulations and an alternative driving mechanism
has been proposed , namely, the transverse azimuthal modulation. To date, no consensus
has been found, and the ligament formation process has yet to be understood.
https://doi.org/10.1017/jfm.2020.699
 Published online by Cambridge University Press

<!-- PDF_PAGE: 15 -->

Ligament formation in aerobreakup 904 A20-15
1.0
0.8
0.6
We = 470
We →  ∞
τ
/Delta1x∗
Exp.
0.4
0.2
0 0.2 0.4 0.6 0.8 1.0 1.2
FIGURE 8. Evolution of the centre-of-mass from numerical results and experimental
observations. Error bars display the sensitivity of the centre-of-mass detection to the intensity
threshold used in the binarization process.
5.1. Ligament formation and azimuthal modulation
Exposing the water droplet to a high-speed gas ﬂow can induce a large difference in
the velocities between the two ﬂuids and thus destabilize their interface. Depending
on the ﬂow conditions, the interface may be more susceptible to Rayleigh–Taylor or
Kelvin–Helmholtz instabilities. The canonical
RTI occurs when a heavy ﬂuid is suspended
above a lighter ﬂuid and both are subjected to acceleration. The interface begins to oscillate
with alternating acceleration directions and is unstable when the acceleration is oriented
towards the heavier ﬂuid (Rayleigh1882). On the other hand,
KHI arises due to either shear
in a single ﬂuid system or due to a velocity difference across the interface of two ﬂuids,
which results in propagating waves
that typically rollup into vortices along the interface
(Chandrasekhar 1961).
For low Weber numbers ( We ∼ 20), it is thought that the RTI is responsible for the
bag-shape structure, which is attached to a thicker toroidal rim. Increasing the Weber
number up to 80, the standard bag morphology evolves to more complex bag structures,
namely the bag-and-stamen and multi-bag modes, still believed to be driven by RTI (Jain
et al. 2015). Ultimately, bags undergo a piercing mechanism (Guildenbecher et al. 2009).
For higher Weber numbers there is less of a consensus but the markedly different droplet
morphologies are also attributed to mechanisms other than RTI piercing. In the work
of Jain et al. (2015) on secondary atomization, the authors numerically investigate the
shear-stripping regime, i.e. sheet-thinning regime, by running simulations at We = 120.
Arguing that high inertial forces overcome the restoring effect of the surface tension,
the authors state that the development of a potential bag on the rim is hampered by
the stripping process occurring at the droplet equatorial plane. This indirectly exonerates
the Rayleigh–Taylor piercing mechanism in the ligament formation. The authors suggest
that the ligament formation
is due to the high-speed gas ﬂow over the droplet periphery,
which results in transverse RTI. The crests of the transverse instability are deformed into
ligaments by being stretched with the ﬂow
, as described by Marmottant & Villermaux
(2004). Following the work of Marmottant & Villermaux ( 2004) on the atomization of
a liquid jet in coaxial ﬂow, the recent work of Jalaal & Mehravaran ( 2014) suggests that
axisymmetric waves propagating on the droplet surface are the result of KHI and that their
acceleration leads to a transverse azimuthal modulation, which can be viewed as RTI. As a
result of such a KHI–RTI combination, streamwise ligaments are formed and subsequently
https://doi.org/10.1017/jfm.2020.699
 Published online by Cambridge University Press

<!-- PDF_PAGE: 16 -->

904 A20-16 B. Dorschner and others
(b)(a)
(c) (d )
FIGURE 9. Transverse azimuthal modulation for We = 470 (front view). Characteristic times
are (a) 0.79, (b) 0.82, (c)0 . 8 4a n d(d) 0.86. Panels (a–d) are cropped views.
fragmented into droplets. In addition, their 3-D numerical simulations for Weber numbers
up to 200 show a good qualitative agreement with their conjecture of an azimuthal
modulation due to RTI. In a attempt to provide quantitative evidence, they compared the
most ampliﬁed wavenumbers, deduced from their simulations with theoretical predictions
but failed to ﬁnd any conclusive quantitative agreement. In another attempt to ﬁnd
quantitative evidence of azimuthal RTI, Meng & Colonius ( 2018) performed a 3-D
simulation for We →∞ . In line with Jalaal & Mehravaran ( 2014), these simulations
show a loss of axisymmetry, but a Fourier analysis of the velocity ﬁeld reveals broadband
instability growth for all modes and hence does not provide further evidence of transverse
RTI.
In the present numerical simulations for We = 470, we also observe a loss of
axisymmetry of the liquid sheet propagating on the droplet rim before transverse
corrugations arise at the interface. In particular, as apparent from ﬁgure 9 , we can
see a non-uniform growth rate of the transverse corrugations, which results in variable
crest amplitudes, indicating a transverse azimuthal modulation of the droplet. However,
concerning the relation of the transverse instability with the ligament formation, a
mismatch between the wavelength and the number of crests and ligaments does not seem
to conﬁrm the mechanism proposed by Jalaal & Mehravaran ( 2014) .A c c o r d i n gt ot h e i r
conjecture, ligaments arise from the stretching of the interface corrugation crests due to
aerodynamic forces. This implies that the number of ligaments is equal to the number of
crests. As shown in ﬁgure 9 , the number of crests observed in our simulation does not
directly correspond to the eight ligaments, which are ultimately forming in the course of
the breakup.
For further investigation of the observed azimuthal modulation and to identify the
modes which lead to the formation of the ligaments as well as to determine the effect
of surface tension on these modes, we decompose the ﬂow ﬁeld around the droplet into
azimuthal Fourier modes. To that end, the Cartesian mesh is interpolated onto a cylindrical
mesh, where the resolutions in azimuthal direction θ, radial direction r and streamwise
direction x are kept similar to the Cartesian mesh. Subsequently, the azimuthal Fourier
coefﬁcients for each mode ˆu(x, r, t) are obtained by Fourier transforms in
the θ direction.
https://doi.org/10.1017/jfm.2020.699
 Published online by Cambridge University Press

<!-- PDF_PAGE: 17 -->

Ligament formation in aerobreakup 904 A20-17
(a)( b)( c)
(d)( e)( f )
(g)( h)( i)
FIGURE 10. Isosurfaces of the mth azimuthal mode κm (red) and isosurfaces of the volume
fraction αl = 0.01 (grey) for We = 470. (a) m = 4, τ≈ 0.85, ( b) m = 4, τ≈ 0.97, ( c) m = 4,
τ≈ 1.05, (d) m = 6, τ≈ 0.85, (e) m = 6, τ≈ 0.97, ( f ) m = 6, τ≈ 1.05, (g) m = 8, τ≈ 0.85,
(h) m = 8, τ≈ 0.97 and (i) m = 8, τ≈ 1.05.
We use an energy metric of the velocity for each mode, which is given by
ˆκm =| ˆux,m|2 +|ˆur,m|2 +|ˆuθ,m|2. (5.1)
Transforming ˆκm back into physical space yields the azimuthal Fourier mode κm.
Isosurfaces of selected azimuthal modes are superimposed with the isosurfaces of the
volume fraction in ﬁgure 10, which shows that the azimuthal wavenumber m = 4 and its
harmonic m = 8 are most pronounced on the droplet surface. Modes corresponding to
wavenumbers other than m = 4o r m = 8, develop in the wake on the back of the droplet
and do not appear to be responsible for the azimuthal modulation and deformation of the
droplet itself. This is exemplarily shown form = 6i n ﬁgure 10(d–f ) but similarly observed
for all other wavenumbers but m = 4a n d m = 8. Strikingly, the wavenumbers m = 4a n d
its harmonic m = 8 do correspond to the wavenumber of the ligaments and thus directly
relate the azimuthal modulation of the ﬂow ﬁeld to the formation of the ligaments.
https://doi.org/10.1017/jfm.2020.699
 Published online by Cambridge University Press

<!-- PDF_PAGE: 18 -->

904 A20-18 B. Dorschner and others
λRT
FIGURE 11. Measurement of ligament wavenumber.
Experimentally, we measure the mean wavenumber of the ligaments by manual
post-processing of the shadowgraphs and measuring the distance between ligaments,
where a ligament is deﬁned as a coherent column of liquid as exempliﬁed in ﬁgure 11. This
procedure eventually yields a mean wavenumber of the ligaments of mexp ∼ 8.5, which is
in excellent agreement with what is observed in our simulations. This further establishes
validity of both our experiments and the numerical simulations.
When studying the evolution of the azimuthal structures of m = 4a n d m = 8i no u r
numerical simulations, one can observe that these structures are formed at relatively early
stages of the breakup and develop on the droplet surface. Subsequently, the azimuthal
modes appear to deform the droplet surface, which leads to azimuthally distributed
bag-like structures with wavenumber m = 8. At later stages, these bag-like structures
develop further and grow as they are subjected to the high-speed gas ﬂow surrounding
the droplet. Eventually, the aerodynamic forces are able to overcome the restoring effect
of surface tension and pierce or rupture the bag-like structures, yielding ligaments, which,
in
the ﬁrst instance, remain attached to the circular rim before they detach at later stages.
This piercing mechanism is illustrated by the detailed snapshots in ﬁgure 12,w h i c hs h o w
the evolution and rupture of the bag-like structures. It is also evident that eventually these
ruptured pockets form the ligaments.
It is interesting to compare this picture to the Weσ=0 case, which is shown in ﬁgure 13.
We can again observe that, as in the case of a ﬁnite Weber number, the only modes that
are acting on the droplet surface correspond to the wavenumbers m = 4a n d m = 8. This
suggests that the cause and origin of these structures are independent of capillary effects.
However, there are obvious differences in the subsequent evolution. In particular, it is
apparent that the azimuthal disturbances are less ampliﬁed, and less able to modulate
the cylindrical liquid curtain that is formed around the droplet core during the course
of the breakup. Hence, in contrast to the ﬁnite Weber number case, there are no
prominent bag-like structures, and the liquid curtain remains unruptured and intact, before
it eventually disintegrates into ﬁne-scale structures. This observation is also in good
qualitative agreement with what was observed by others (Marmottant & Villermaux
2004; Jalaal & Mehravaran 2014) who conjecture that
the transverse destabilization of
the liquid rim is due to the Rayleigh–Taylor instability, which leads to an inﬁnitesimally
small wavelength for negligible surface-tension values ( σ → 0) as the RTI wavelength is
proportional to the square root of the surface tension.
https://doi.org/10.1017/jfm.2020.699
 Published online by Cambridge University Press

<!-- PDF_PAGE: 19 -->

Ligament formation in aerobreakup 904 A20-19
(a)( b)
(c)( d)
(a)( b)
(c)( d)
(e)( f )( e)( f )
Back viewFront view
FIGURE 12. Piercing mechanisms for We = 470 (front and back views). Characteristic times
are (a) 0.88, (b) 0.90, (c) 0.92, (d)0 . 9 4 ,(e)0 . 9 6a n d(f ) 0.98.
While we have not been able to infer a direct relation to RTI from our simulations, our
observations do suggest that transverse azimuthal modulation plays a crucial role in the
formation and subsequent shedding of ligaments.
5.2. Recurrent breakup and vortex shedding
While the stages of the breakup and the formation of the ligaments are well described
by the above mechanisms, our simulations and experiments suggest that the pattern of
events occurs repeatably at different scales throughout the course of the breakup. In
particular, when considering the breakup for a Weber number of We = 470,a ss h o w n
in ﬁgure 14 (a,b), we can qualitatively observe a very similar droplet morphology and
breakup behaviour for times τ= 0.94 and τ= 1.33. Hence, the process repeats after the
initial breakup or ligament formation process. An analogous process can also be observed
in our simulations for We →∞ as demonstrated in ﬁgure 14(c,d), where the breakups are
observed at τ= 0.91 and τ= 1.25. This suggests a negligible effect of capillary forces on
such recurrent shedding
behaviour.
Consulting our experiments, we can investigate this effect for a longer time span than
possible with the numerical simulations. To that end, the snapshots are post-processed
manually and the breakup times are deﬁned as the time between subsequent snapshots in
which the ligaments are still attached to the main droplet core and when they have been
shed from the droplet. This has been done for 29 independent experiments with varying
Weber numbers. Starting from the formation of the ﬁrst ligaments, we can observe a total
of four breakups until the droplet is entirely disintegrated. A typical sequence of four
breakups as captured by the experiments is shown in ﬁgure 15 . Clearly visible are the
ligaments and their subsequent fragmentation. Recording the breakup times as a function
of the Weber number ( ﬁgure 16) reveals that, while 4 breakups are recorded for all Weber
numbers, capillary effects have an impact on the breakup times, reaching
nearly constant
values beyond We > 400. The error bars indicate the time difference between subsequent
snapshots before and after the breakup of the ligaments.
A comparison with our simulations in ﬁgure 16 shows that the ﬁrst and second breakup
times in the simulation agree well with the experimental observations for the second and
third breakup for both the We = 470 and We →∞ simulations. Hence, it appears that our
simulation cannot capture the ﬁrst breakup in the experiment. This is due to the ﬁne-scale
https://doi.org/10.1017/jfm.2020.699
 Published online by Cambridge University Press

<!-- PDF_PAGE: 20 -->

904 A20-20 B. Dorschner and others
(a)( b)( c)
(d ) ( e)( f )
( g)( h)( i)
FIGURE 13. Isosurfaces of the mth azimuthal mode κm (red) and isosurfaces of the volume
fraction αl = 0.01 (grey) for We →∞ .( a) m = 4, τ≈ 0.85, ( b) m = 4, τ≈ 0.97, ( c) m = 4,
τ≈ 1.05, (d) m = 6, τ≈ 0.85, (e) m = 6, τ≈ 0.97, ( f ) m = 6, τ≈ 1.05, (g) m = 8, τ≈ 0.85,
(h) m = 8, τ≈ 0.97 and (i) m = 8, τ≈ 1.05.
nature of the ﬁrst breakup, which our simulations are not able to resolve. In fact, from our
experiments we measure ligament thicknesses during the ﬁrst breakup ranging from 10 to
40 μm, which corresponds to a resolution between ∼ 2–7 grid cells for these ligaments in
our simulations. Nonetheless, the agreement of subsequent breakup times further validates
both the simulations as well as the post-processing methodology for the experiments.
The functional dependence of the breakup onset on the Weber number is estimated
using a nonlinear least-square ﬁt of the experimental data of the form τ≈ aWeb + c and
plotted alongside the measurements in ﬁgure 16. The ﬁtting coefﬁcients are reported in
table 1, which reveal a similar functional dependence for all breakup times. In particular,
the similar exponents a and constant difference between the offsets c for all breakups
reveal an approximately constant frequency between the breakups. This suggests that only
the initial onset of the breakup is a function of the Weber number, whereas the breakup and
https://doi.org/10.1017/jfm.2020.699
 Published online by Cambridge University Press

<!-- PDF_PAGE: 21 -->

Ligament formation in aerobreakup 904 A20-21
(a)( b)
(c)( d )
FIGURE 14. Recurrent breakups for both simulations at We = 470 and We →∞ .( a) Second
breakup at τ= 0.94 for We = 470.( b) Third breakup at τ= 1.33 for We = 470.( c) Second
breakup at τ= 0.91 for We →∞ .( d) Third breakup at τ= 1.25 for We →∞ .
its frequency are independent of capillary effects. Put differently, surface tension seems
to delay the onset of the initial ligament shedding but does not affect the frequency of
the recurrent shedding. Hence, these curves can be collapsed when shifted by c,w h i c hi s
reported in ﬁgure 17. The ﬁt suggests that the breakup onset scales with τ∼ We− 4.
We conjecture that the breakup frequency is dominated by aerodynamic effects only.
Such effects are dominant in the initial stages of the droplet deformation and previous
studies of aerobreakup have shown a similar drag coefﬁcient to that of a ﬂow past a sphere
(see, e.g. Meng & Colonius 2018). In our case, it is instructive to evaluate the Strouhal
number St = fD/U for the observed breakups. However, the characteristic length scale,
associated with the deforming and disintegrating droplet and its wake, is a priori not
clear.To that end, inﬁgure 18, we plot the evolution of the droplet core diameter throughout
the breakup process for all experimental runs with Weber numbers in the range of We =
[200, 700]. The diameter is measured directly from the shadowgraphs and deﬁned as the
maximum extent of the coherent liquid body of the droplet. Remarkably, the diameter
https://doi.org/10.1017/jfm.2020.699
 Published online by Cambridge University Press

<!-- PDF_PAGE: 22 -->

904 A20-22 B. Dorschner and others
First ligaments
observed
First breakupSecond breakup
Fourth breakup Third breakup
First fragments
observed
U-shape
ligaments
Fragmented
U-shape
ligaments
Lips
Lips
Lips
FIGURE 15. Experimental snapshots of the recurrent breakup mechanism for a typical case at
We = 295.
evolution is independent of the Weber number and the droplet expands up to twice the
size of its initial diameter for all experiments. Note that , at later stages for τ> 1, the core
diameter decreases due to shedding and D < 2D0 but the small-scale structures and mist
shed form the droplet, yielding an effective diameter which is larger than the diameter of
the droplet core as plotted on ﬁgure 18. Hence, the maximum droplet diameter Dm = 2D0
as a characteristic length scale seems to be the natural choice for reduction of the breakup
https://doi.org/10.1017/jfm.2020.699
 Published online by Cambridge University Press

<!-- PDF_PAGE: 23 -->

Ligament formation in aerobreakup 904 A20-23
τ
Exp. fit
Simulation
Simulation, We → ∞
Exp.
Exp. fit
Exp.
2.0(a)( b)
(c)( d )
1.5
1.0
0.5
0
τ
3.0
2.5
2.0
1.5
1.0
3.5
3.0
2.5
2.0
1.5
200 300 400 500 600 700 200 300 400 500 600 700
200 300 400
We
500 600 700 200 300 400
We
500 600 700
2.5
2.0
1.5
1.0
0.5
FIGURE 16. Breakup time dependence on the Weber number. The error bars indicate the time
difference between subsequent snapshots before and after the breakup of the ligaments. ( a)F i r s t
breakup.( b) Second breakup .( c) Third breakup .( d) Fourth breakup.
Breakup no. ab c
14 .07 × 105 − 2.47 0 .51
25 .22 × 1012 − 5.36 0 .99
38 .58 × 1011 − 4.93 1 .41
41 .34 × 1012 − 4.92 2 .00
All 5 .41× 109 − 4.08 0
TABLE 1. Fitting coefﬁcients for a nonlinear least-square ﬁt of the form τ≈ aWeb + c.T h e
conﬁdence interval for all ﬁtting coefﬁcients is 0.95.
frequency. This yields a mean Strouhal number of St ≈ 0.217 when using all experimental
data. Using the ﬁtted data, one similarly obtains St ≈ 0.18. Both frequencies agree well
with what is observed for the ﬂow past a rigid sphere (see, e.g. Achenbach 1974;K i m&
Durbin 1988; Sakamoto & Haniu 1990). This suggests that the recurrent breakup is indeed
induced by classical vortex shedding.
https://doi.org/10.1017/jfm.2020.699
 Published online by Cambridge University Press

<!-- PDF_PAGE: 24 -->

904 A20-24 B. Dorschner and others
Exp. fit τ ∼ We−4
Exp.
2.5
2.0
1.5
1.0
0.5
0
–0.5
200 300 400 500 600 700
We
τ
FIGURE 17. Collapse of all breakup times when shifted by their asymptotic breakup time. The
least-square ﬁt suggests τ∼ We− 4.
2.5
2.0
1.5
1.0D/D0
0.5
0 0.5 1.0 1.5 2.0 2.5
τ
FIGURE 18. Diameter evolution for Weber numbers in the range We = [200, 700].
6. Conclusion
Three-dimensional simulations and high-magniﬁcation shadowgraphy visualizations
of the aerobreakup of a water droplet have been performed to capture the underlying
mechanisms leading the ligament formation and disintegration. The numerical simulations
are ﬁrst validated with respect to experimental results by comparison of observed
deformation and the evolution of the
centre-of-mass of the droplet, and the number
of ligaments that are formed during breakup. An analysis of the perturbations arising
on the liquid sheet surrounding the droplet shows good qualitative agreement with the
concept of transverse azimuthal modulation. From the numerical results, modes associated
with the transverse destabilization have been found by means of an azimuthal Fourier
decomposition of the ﬂow ﬁeld. These correspond to the wavenumber of ligaments which
form subsequent to the initial growth of azimuthal modulation. Finally, we experimentally
and numerically show what we believe to be the ﬁrst observation of recurrent shedding
of ligaments. The ﬁrst breakup event occurs at a time that depends weakly on the Weber
number and with stronger capillarity the breakup is delayed, whereas subsequent events
https://doi.org/10.1017/jfm.2020.699
 Published online by Cambridge University Press

<!-- PDF_PAGE: 25 -->

Ligament formation in aerobreakup 904 A20-25
occur at the same ﬁxed time interval, independent of We. The frequency of recurrence
of breakup events is therefore driven primarily by inertia. By casting the frequency as
a Strouhal number based on the pancaked droplet diameter, which reached a value of
2D
0 compared to the initial droplet diameter, independent of We,w eﬁ n d St ≈ 0.2, which
supports a hypothesis that this shedding behaviour is related to vortex shedding in the
wake of the deformed droplet.
Acknowledgements
The experimental work (L.B.P . and H.E.R.) was supported by the Région
Nouvelle-Aquitaine as part of the SEIGLE project (2017-1R50115) and the CPER FEDER
project. B.D. acknowledges support from the Swiss National Science Foundation Grant
No. P2EZP2_178436. Computations associated with parallel performance have utilized
the Extreme Science and Engineering Discovery Environment, which is supported by the
National Science Foundation grant number CTS120005.
Declaration of interests
The authors report no conﬂict of interest.
REFERENCES
ABGRALL ,R .&K ARNI , S. 2001 Computations of compressible multiﬂuids. J. Comput. Phys. 169 (2),
594–623.
ACHENBACH , E. 1974 Vortex shedding from spheres. J. Fluid Mech. 62 (2), 209–221.
ALLISON , P . M., M CMANUS ,T .A .&S UTTON , J. A. 2016 Quantitative fuel vapor/air mixing imaging
in droplet/gas regions of an evaporating spray ﬂow using ﬁltered rayleigh scattering. Opt. Lett.
41 (6), 1074–1077.
BAER ,M .R .&N UNZIATO , J. W. 1986 A two-phase mixture theory for the deﬂagration-to-detonation
transition (DDT) in reactive granular materials. Intl J. Multiphase Flows 12, 861–889.
BALL , G. J., H OWELL ,B .P . ,L EIGHTON ,T .G .&S CHOFIELD , M. J. 2000 Shock-induced collapse of a
cylindrical air cavity in water: a free-lagrange simulation. Shock Waves 10 (4), 265–276.
BIASIORI -POULANGES ,L .&E L-RABII , H. 2019 High-magniﬁcation shadowgraphy for the study of drop
breakup in a high-speed gas ﬂow. Opt. Lett. 44 (23), 5884–5887.
BOLLEDDULA ,D .A . ,B ERCHIELLI ,A .&A LISEDA , A. 2010 Impact of a heterogeneous liquid droplet
on a dry surface: application to the pharmaceutical industry. Adv. Colloid Interface Sci. 159 (2),
144–159.
CAO, X. K., S UN , Z. G., L I,W .F . ,L IU,H .F .&Y U, Z. H. 2007 A new breakup regime of liquid drops
identiﬁed in a continuous and uniform air jet ﬂow. Phys. Fluids 19 (5), 057103.
CHANDRASEKHAR , S. 1961 Hydrodynamic and Hydromagnetic Stability. Dover.
CHEN ,H .&L IANG , S. M. 2008 Flow visualization of shock/water column interactions. Shock Waves
17 (5), 309–321.
CHOU , W . H., H SIANG ,L .P .&F AETH , G. M. 1997 Temporal properties of drop breakup in the shear
breakup regime. Intl J. Multiphase Flow 23 (4), 651–669.
COCCHI ,J .P .&S AUREL , R. 1997 A Riemann problem based method for the resolution of compressible
multimaterial ﬂows. J. Comput. Phys. 137 (2), 265–298.
CORALIC ,V .&C OLONIUS , T. 2014 Finite-volume WENO scheme for viscous compressible
multicomponent ﬂows. J. Comput. Phys. 274, 95–121.
DORSCHNER , B., S CHMIDMAYER , K., B IASIORI -POULANGES , L., E L-RABII ,H .&C OLONIUS ,T .
2019 Shock-induced atomization of water droplets. Bull. Am. Phys. Soc. 64.
ECKHOFF ,R .K .2 0 1 6Explosion Hazards in the Process Industries . Gulf Professional Publishing.
FAETH , G. M., H SIANG ,L .P .&W U, P. K. 1995 Structure and breakup properties of sprays.
Intl J. Multiphase Flow 21, 99–127.
https://doi.org/10.1017/jfm.2020.699
 Published online by Cambridge University Press

<!-- PDF_PAGE: 26 -->

904 A20-26 B. Dorschner and others
FISHBURN , B. D. 1974 Boundary layer stripping of liquid drops fragmented by Taylor instability. Acta
Astronaut. 1 (9–10), 1267–1284.
FUSTER , D. 2019 A review of models for bubble clusters in cavitating ﬂows. Flow Turbul. Combust. 102,
497–536.
GARRICK , D. P. 2016 Numerical modeling of atomization in compressible ﬂow. PhD thesis, Iowa State
University.
GELFAND , B. E. 1996 Droplet breakup phenomena in ﬂows with velocity lag. Prog. Energy Combust. Sci.
22 (3), 201–265.
GEL ’FAND , B. E., G UBIN ,S .A .&K OGARKO , S. M. 1974 Various forms of drop fractionation in shock
waves and their special characteristics. J. Engng Phys. 27 (1), 877–882.
GUILDENBECHER , D. R., L ÓPEZ -RIVERA ,C .&S OJKA , P. E. 2009 Secondary atomization. Exp. Fluids
46 (3), 371.
GUILDENBECHER , D. R., L ÓPEZ -RIVERA ,C .&S OJKA , P. E. 2011 Droplet deformation and breakup.
In Handbook of Atomization and Sprays , pp. 145–156. Springer.
HAN ,J .&T RYGGVASON , G. 1999 Secondary breakup of axisymmetric liquid drops. I. Acceleration by a
constant body force. Phys. Fluids 11 (12), 3650–3667.
HAN ,J .&T RYGGVASON , G. 2001 Secondary breakup of axisymmetric liquid drops. II. Impulsive
acceleration. Phys. Fluids 13 (6), 1554–1565.
HANSON , A. R., D OMICH ,E .G .&A DAMS , H. S. 1963 Shock tube investigation of the breakup of drops
by air blasts. Phys. Fluids 6 (8), 1070–1080.
HARPER ,E .Y . ,G RUBE ,G .W .&C HANG , I. D. 1972 On the breakup of accelerating liquid drops.
J. Fluid Mech. 52 (3), 565–591.
HINZE , J. O. 1955 Fundamentals of the hydrodynamic mechanism of splitting in dispersion processes.
AIChE J. 1 (3), 289–295.
HIRAHARA ,H .&K A W AHASHI, M. 1992 Experimental investigation of viscous effects upon a breakup of
droplets in high-speed air ﬂow. Exp. Fluids 13 (6), 423–428.
HSIANG ,L .P .&F AETH , G. M. 1992 Near-limit drop deformation and secondary breakup.
Intl J. Multiphase Flow 18 (5), 635–652.
HSIANG ,L .P .&F AETH , G. M. 1993 Drop properties after secondary breakup. Intl J. Multiphase Flow
19 (5), 721–735.
HSIANG ,L .P .&F AETH , G. M. 1995 Drop deformation and breakup due to shock wave and steady
disturbances. Intl J. Multiphase Flow 21 (4), 545–560.
HWA NG, S. S., L IU,Z .&R EITZ , R. D. 1996 Breakup mechanisms and drag coefﬁcients of high-speed
vaporizing liquid drops. Atomiz. Sprays 6 (3), 353–376.
JAIN , M., P RAKASH , R. S., T OMAR ,G .&R A VIKRISHNA , R. V. 2015 Secondary breakup of a drop at
moderate weber numbers. Proc. R. Soc. Lond. A 471 (2177), 20140930.
JALAAL ,M .&M EHRA V ARAN, K. 2012 Fragmentation of falling liquid droplets in bag breakup mode.
Intl J. Multiphase Flow 47, 115–132.
JALAAL ,M .&M EHRA V ARAN, K. 2014 Transient growth of droplet instabilities in a stream. Phys. Fluids
26 (1), 012101.
JOSEPH , D. D., B ELANGER ,J .&B EA VERS, G. S. 1999 Breakup of a liquid drop suddenly exposed to a
high-speed airstream. Intl J. Multiphase Flow 25 (6), 1263–1303.
KAPILA ,A . ,M ENIKOFF , R., B DZIL , J., S ON ,S .&S TEW ART, D. 2001 T wo-phase modeling of DDT in
granular materials: reduced equations. Phys. Fluids 13, 3002–3024.
KHOSLA , S., S MITH ,C .E .&T HROCKMORTON , R. P. 2006 Detailed understanding of drop atomization
by gas crossﬂow using the volume of ﬂuid method. In19th Annual Conference on Liquid Atomization
and Spray Systems (ILASS-Americas), Toronto, Canada .
KIM , D., D ESJARDINS , O., H ERRMANN ,M .&M OIN , P. 2006 Toward two-phase simulation of the
primary breakup of a round liquid jet by a coaxial ﬂow of gas. In Center for Turbulence Research
Annual Research Briefs, vol. 185. Stanford University.
KIM ,H .J .&D URBIN , P. A. 1988 Observations of the frequencies in a sphere wake and of drag increase
by acoustic excitation. Phys. Fluids 31 (11), 3260–3265.
KRZECZKOWSKI , S. A. 1980 Measurement of liquid droplet disintegration mechanisms. Intl J. Multiphase
Flow 6 (3), 227–239.
https://doi.org/10.1017/jfm.2020.699
 Published online by Cambridge University Press

<!-- PDF_PAGE: 27 -->

Ligament formation in aerobreakup 904 A20-27
KULKARNI ,V .&S OJKA , P. E. 2014 Bag breakup of low viscosity drops in the presence of a continuous
air jet. Phys. Fluids 26 (7), 072103.
LABOUSSE ,M .&B USH , J. W. M. 2015 Polygonal instabilities on interfacial vorticities. Eur. Phys. J. E
38 (10), 113.
LANE , W. R. 1951 Shatter of drops in streams of air. Ind. Engng Chem. 43 (6), 1312–1317.
LEE ,C .H .&R EITZ , R. D. 1999 Modeling the effects of gas density on the drop trajectory and breakup
size of high-speed liquid drops. Atomiz. Sprays 9 (5), 497–517.
LEE ,C .H .&R EITZ , R. D. 2000 An experimental study of the effect of gas density on the distortion and
breakup mechanism of drops in high speed gas stream. Intl J. Multiphase Flow 26 (2), 229–244.
LEE ,C .S .&R EITZ , R. D. 2001 Effect of liquid properties on the breakup mechanism of high-speed
liquid drops. Atomiz. Sprays 11 (1), 1–19.
LEFEBVRE ,A .H .&M CDONELL ,V .G .2 0 1 7Atomization and Sprays.C R C .
LIU,T .G . ,K HOO ,B .C .&Y EO , K. S. 2003 Ghost ﬂuid method for strong shock impacting on material
interface. J. Comput. Phys. 190 (2), 651–681.
LIU,Z .&R EITZ , R. D. 1997 An analysis of the distortion and breakup mechanisms of high speed liquid
drops. Intl J. Multiphase Flow 23 (4), 631–650.
LIU,N . ,W ANG , Z., S UN , M., D EITERDING ,R .&W ANG , H. 2019 Simulation of liquid jet primary
breakup in a supersonic crossﬂow under adaptive mesh reﬁnement framework. Aerospace Sci.
Technol. 91, 456–473.
LIU,N . ,W ANG , Z., S UN , M., W ANG ,H .&W ANG , B. 2018 Numerical simulation of liquid droplet
breakup in supersonic ﬂows. Acta Astronaut. 145, 116–130.
LIU,W . ,Y UAN ,L .&S HU, C. W. 2011 A conservative modiﬁcation to the ghost ﬂuid method for
compressible multiphase ﬂows. Commun. Comput. Phys. 10 (4), 785–806.
MAGARVEY ,R .H .&T AYLOR , B. W. 1956 Free fall breakup of large drops. J. Appl. Phys. 27 (10),
1129–1135.
MARCOTTE ,F .&Z ALESKI , S. 2019 Density contrast matters for drop fragmentation thresholds at low
Ohnesorge number. Phys. Rev. Fluids 4 (10), 103604.
MARMOTTANT ,P .&V ILLERMAUX , E. 2004 On spray formation. J. Fluid Mech. 498, 73–111.
MATAS , J.-P . 20 15 Inviscid versus viscous instability mechanism of an air–water mixing layer. J. Fluid
Mech. 768, 375–387.
MENG , J. C. 2016 Numerical simulations of droplet aerobreakup. PhD thesis, California Institute of
Technology.
MENG ,J .C .&C OLONIUS , T. 2014 Numerical simulations of the early stages of high-speed droplet
breakup. Shock Waves 25, 399–414.
MENG ,J .C .&C OLONIUS , T. 2018 Numerical simulation of the aerobreakup of a water droplet. J. Fluid
Mech. 835, 1108–1135.
PAN , S., H AN , L., H U,X .&A DAMS , N. A. 2018 A conservative interface-interaction method for
compressible multi-material ﬂows. J. Comput. Phys. 371, 870–895.
PÉRIGAUD ,G .&S AUREL , R. 2005 A compressible ﬂow model with capillary effects. J. Comp. Phys.
209, 139–178.
PILCH ,M .&E RDMAN , C. A. 1987 Use of breakup time data and velocity history to predict the maximum
size of stable fragments for acceleration-induced breakup of a liquid drop. Intl J. Multiphase Flow
13, 741–757.
PISHCHALNIKOV ,Y .A . ,B EHNKE -PARKS , W . M., S CHMIDMAYER , K., M AEDA , K., C OLONIUS ,T . ,
KENNY ,T .W .&L ASER , D. J. 2019 High-speed video microscopy and numerical modeling of
bubble dynamics near a surface of urinary stone. J. Acoust. Soc. Am. 146, 516–531.
RANGER ,A .A .&N ICHOLLS , J. A. 1969 Aerodynamic shattering of liquid drops. AIAA J. 7 (2), 285–290.
RAYLEIGH ,L ORD 1882 Investigation of the character of the equilibrium of an incompressible heavy ﬂuid
of variable density. Proc. Lond. Math. Soc. s1–14 (1), 170–177.
REINECKE ,W .&W ALDMAN , G. 1975 Shock layer shattering of cloud drops in reentry ﬂight. In 13th
Aerospace Sciences Meeting,p .1 5 2 .
SAKAMOTO ,H .&H ANIU , H. 1990 A study on vortex shedding from spheres in a uniform ﬂow. J. Fluids
Engng 112 (4), 386–392.
https://doi.org/10.1017/jfm.2020.699
 Published online by Cambridge University Press

<!-- PDF_PAGE: 28 -->

904 A20-28 B. Dorschner and others
SAUREL ,R .&P ANTANO , C. 2018 Diffuse-interface capturing methods for compressible two-phase ﬂows.
Annu. Rev. Fluid Mech. 50, 105–130.
SAUREL , R., P ETITPAS ,F .&B ERRY, R. A. 2009 Simple and efﬁcient relaxation methods for interfaces
separating compressible ﬂuids, cavitating ﬂows and shocks in multiphase mixtures. J. Comput. Phys.
228 (5), 1678–1712.
SCHMIDMAYER , K., B RYNGELSON ,S .H .&C OLONIUS , T. 2020 a An assessment of multicomponent
ﬂow models and interface capturing schemes for spherical bubble dynamics. J. Comput. Phys. 402,
109080.
SCHMIDMAYER , K., P ETITPAS ,F .&D ANIEL , E. 2019 Adaptive Mesh reﬁnement algorithm based on
dual trees for cells and faces for multiphase compressible ﬂows. J. Comput. Phys. 388, 252–278.
SCHMIDMAYER , K., P ETITPAS ,F . ,D ANIEL , E., F A VRIE,N .&G A VRIL YUK, S. L. 2017 A model and
numerical method for compressible ﬂows with capillary effects. J. Comput. Phys. 334, 468–496.
SCHMIDMAYER , K., P ETITPAS ,F . ,L E MARTELOT ,S .&D ANIEL , E. 2020 b ECOGEN: an open-source
tool for multiphase, compressible, multiphysics ﬂows. Comput. Phys. Commun. 251, 107093.
SHRAIBER ,A .A . ,P ODVYSOTSKY ,A .M .&D UBROVSKY , V. V. 1996 Deformation and breakup of drops
by aerodynamic forces. Atomiz. Sprays 6 (6), 667–692.
SHYUE ,K .M .&X IAO , F. 2014 An Eulerian interface sharpening algorithm for compressible two-phase
ﬂow: the algebraic THINC approach. J. Comput. Phys. 268, 326–354.
SIMPKINS ,P .G .&B ALES , E. L. 1972 Water-drop response to sudden accelerations. J. Fluid Mech. 55
(04), 629–639.
STAPPER ,B .E .&S AMUELSEN , G. S. 1990 An experimental study of the breakup of a two-dimensional
liquid sheet in the presence of co-ﬂow air shear. In 28th Aerospace Sciences Meeting, p. 461. AIAA.
THEOFANOUS , T. G. 2011 Aerobreakup of Newtonian and viscoelastic liquids. Annu. Rev. Fluid Mech. 43,
661–690.
THEOFANOUS ,T .G .&L I, G. J. 2008 On the physics of aerobreakup. Phys. Fluids 20 (5), 052103.
THEOFANOUS , T. G., L I,G .J .&D INH , T. N. 2004 Aerobreakup in rareﬁed supersonic gas ﬂows.
J. Fluids Engng 126 (4), 516–527.
THÉV AND,N . ,D ANIEL ,E .&L ORAUD , J. C. 1999 On high-resolution schemes for solving unsteady
compressible two-phase dilute viscous ﬂows. Intl J. Numer. Meth. Fluids 31 (4), 681–702.
TORO , E. F. 1997 Riemann Solvers and Numerical Methods for Fluid Dynamics . Springer Verlag.
VAN LEER , B. 1977 Towards the ultimate conservative difference scheme III. Upstream-centered
ﬁnite-difference schemes for ideal compressible ﬂow. J. Comput. Phys. 23 (3), 263–275.
WADHW A, A. R., M AGI ,V .&A BRAHAM , J. 2007 Transient deformation and drag of decelerating drops
in axisymmetric ﬂows. Phys. Fluids 19 (11), 113301.
WANG , C., C HANG , S., W U,H .&X U, J. 2014 Modeling of drop breakup in the bag breakup regime.
Appl. Phys. Lett. 104 (15), 154107.
WIERZBA , A. 1990 Deformation and breakup of liquid drops in a gas stream at nearly critical weber
numbers. Exp. Fluids 9 (1-2), 59–64.
ZANDIAN ,A . ,S IRIGNANO ,W .A .&H USSAIN , F. 2019 Vorticity dynamics in a spatially developing
liquid jet inside a co-ﬂowing gas. J. Fluid Mech. 877, 429–470.
ZHAO , H., L IU,H .F . ,L I,W .F .&X U, J. L. 2010 Morphological classiﬁcation of low viscosity drop bag
breakup in a continuous air jet stream. Phys. Fluids 22 (11), 114103.
ZHAO , H., L IU,H .F . ,X U, J. L., L I,W .F .&L IN , K. F. 2013 Temporal properties of secondary drop
breakup in the bag-stamen breakup regime. Phys. Fluids 25 (5), 054102.
https://doi.org/10.1017/jfm.2020.699
 Published online by Cambridge University Press
