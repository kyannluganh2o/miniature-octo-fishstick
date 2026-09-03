<!-- PDF_PAGE: 1 -->

Downloaded from www.annualreviews.org.  Guest (guest) IP:  103.151.173.209 On: Sat, 29 Aug 2026 07:53:40
FL58_Art04_Basu ARjats.cls November 28, 2025 12:3
Annual Review of Fluid Mechanics
Secondary Atomization of
Droplets at Extreme Conditions
Saini Jatin Rao and Saptarshi Basu
Department of Mechanical Engineering, Indian Institute of Science, Bengaluru, India;
email: sbasu@iisc.ac.in
Annu. Rev. Fluid Mech. 2026. 58:83–110
First published as a Review in Advance on
August 1, 2025
The Annual Review of Fluid Mechanics is online at
fluid.annualreviews.org
https://doi.org/10.1146/annurev-fluid-112823-
115348
Copyright © 2026 by the author(s). This work is
licensed under a Creative Commons Attribution 4.0
International License, which permits unrestricted
use, distribution, and reproduction in any medium,
provided the original author and source are credited.
See credit lines of images or other third-party
material in this article for license information.
Keywords
secondary atomization, aerobreakup, droplets, multiphase flows, interfacial
instability, catastrophic breakup
Abstract
Droplets, which are ubiquitous in nature, are formed through intriguing
processes, and one such route is air-assisted atomization or aerobreakup.
This review focuses on secondary atomization, particularly the breakup of
an individual droplet subjected to high-speed flows. This process involves
complex interfacial dynamics with multiscale deformations, ranging from
global flattening to local unstable waves. The deformations occur at pro-
gressively smaller scales while interacting with the surrounding gas phase,
forming a nonlinear cascade. Each local undulation serves as a precursor
to a self-similar evolution or subsecondary breakup process that ends with
a ligament-mediated mechanism. In practical scenarios, droplets often en-
counter nonuniform, unsteady, impulsive, or compressible flows, like shock
waves, which pose extreme conditions. The spatiotemporal scales of the
nonuniformity or unsteadiness of the external flow must be comparable
with the drop deformation scales at either global or local levels to influence
aerobreakup that cascades across hierarchical deformation scales. The com-
pressible effects at high Mach numbers are interestingly shown to suppress
the tendency toward breakup.
83

<!-- PDF_PAGE: 2 -->

Downloaded from www.annualreviews.org.  Guest (guest) IP:  103.151.173.209 On: Sat, 29 Aug 2026 07:53:40
FL58_Art04_Basu ARjats.cls November 28, 2025 12:3
Weber number (We):
the ratio of inertial
force imparted by the
airflow and the
resistive surface
tension force
Ohnesorge number
(Oh): represents the
relative dominance of
viscous damping over
surface tension
1. INTRODUCTION
A droplet is ubiquitous in countless applications, ranging from hypersonics to additive manufactur-
ing. Droplet formation has been a subject of investigation since the beginning of scientific inquiry
and continues to be a dynamic area of research. Air-assisted atomization or aerobreakup presents
one such mechanism where the liquid bulk is fragmented into tiny droplets in the presence of
high-speed gas flow. This process is termed primary atomization ( Lin & Reitz 1998 , Lasheras &
Hopfinger 2000, Eggers & Villermaux 2008, Gorokhovski & Herrmann 2008 ), and it generates a
cluster of liquid fragments primarily in the form of droplets and irregular blobs. The droplets can
then undergo further fragmentation under persistent external forcing, and this process is termed
secondary atomization. This phenomenon is prevalent in spray formation processes including nat-
ural events such as rain formation ( Villermaux & Bossa 2009 ), ocean sprays ( V eron 2015, Deike
2022), and sneeze ejecta ( Bourouiba 2021). However, extreme flow conditions are encountered in
a variety of other environments, such as volcanic eruptions ( Jones et al. 2019 ), hypersonic appli-
cations (Virot et al. 2023), metal powder generation ( Mates & Settles 2005 ), and even firefighting
(Capecelatro & Wagner 2024 ), where the size of daughter droplets is of paramount importance.
The physics of secondary atomization has garnered significant attention, and previous reviews
(Villermaux 2007 , 2020; Guildenbecher et al. 2009 ; Theofanous 2011 ; Sharma et al. 2022 ; Ni
2024) provide comprehensive insights into the history, applications, and various models that aim
to predict different facets of this complex issue. Nevertheless, many aspects of the problem remain
unresolved, especially in high-speed flows.
The aerobreakup of a droplet typically involves a few dominant forces, with the balance among
them governing the associated dynamics and evolution of the phenomenon. However, on closer
inspection, aerobreakup inherently also involves multiple spatiotemporal scales, where the forces
engage in a tug-of-war. These forces are depicted in Figure 1 a. They can be broadly classified
as disruptive or resistive. The disruptive or fragmenting force stems primarily from aerodynamic
effects. This can be decomposed into two primary components, namely, the pressure force Fp and
shear force Fs imposed over the liquid interface by the gas flow. The pressure force generally de-
forms the droplet geometry initially into a disc, and the shear force leads to consequences that
are discussed below. The resistive forces associated with the liquid properties generate opposing
forces or damping against the disruptive forces, usually coupled in a nonlinear fashion. This in-
cludes surface tension, which tends to minimize the surface energy of the system and thus resist
interface motion that distorts and increases the surface area. The disruptive forces impart en-
ergy to the droplet system, which is partially dissipated by the viscous effects (typically dependent
on the rate of deformation). Body forces Fb may also exist by virtue of gravity, electromagnetic,
centrifugal, coriolis, or other volumetric actuation.
These forces and their relative strength govern the dynamics of droplet breakup, including the
onset of breakup, morphology of intermediate states, and final fragment size. V arious dimension-
less numbers can be defined to characterize this balance with respect to global flow parameters.
Such relevant numbers include
WeD au2
a d0
 , OhD l√
l d0
, ReD auad0
a
, and Ma D ua
c0
, 1.
where d0 is the initial droplet diameter, ui the fluid velocity, i the density,  the surface tension,
i the viscosity, c0 the speed of sound in the gas phase, and the subscripts a and l indicate the air
(gas) and liquid phase, respectively.
In general, the larger the Weber number (We), the higher the tendency is for the droplet to
break up. We and the Ohnesorge number (Oh), on their own, can be sufficient to describe the
dynamics ( Hinze 1955 , Krzeczkowski 1980 , Pilch & Erdman 1987 , Hsiang & Faeth 1992 ). We
84 Rao  Basu

<!-- PDF_PAGE: 3 -->

Downloaded from www.annualreviews.org.  Guest (guest) IP:  103.151.173.209 On: Sat, 29 Aug 2026 07:53:40
FL58_Art04_Basu ARjats.cls November 28, 2025 12:3
Reynolds number
(Re): the ratio of
inertial force imparted
by the airflow and
viscous resistance,
usually observed near
the liquid surface in
these scenarios
ba
c
Ma = 3
Ma ≈ 1.2 Ma ≈ 0.3
Ma < 0.1
Ma < 0.1
Ma > 1
Oh
We
We ≈ 1,100We ≈ 250We ≈ 50We ≈ 10We ≈ 23
Ma
0.1
1
2
3
Bow shock
Wake
Fb
FPu∞
Fs
Fσ
Fv
DropletGas flow
RTP
Multimode
Bag
Oscillatory
Shear
SIE
SIE
Deformation
>20%
Deformation 5%–10%
Deformation 10%–20%
Deformation
<5%
1'1'
1'
2'
j'
j' j
i' i
3'
3
2
j
2'2'
3'3'
11
22
33
Ma ≈ 3 10–4 10–3 10–2
Hsiang & Faeth (1992, 1995)
Hanson et al. (1963)
Lane (1951)
Loparev (1975)
Hinze (1955)
Theofanous (2011)
Sharma et al. (2021)
Chandra et al. (2023)
Sharma et al. (2023a)
Chandra et al. (2024a)
10–1 100
100
101
102
103
104
105
106
107
101 102 103
Larger fragments
over narrower spread
Larger fragments
over narrower spread
LigamentsLigaments Liquid
sheet
Liquid
sheet
Hsiang & Faeth (1995)
Theofanous (2011)
Sharma et al. (2021, 2023a)
t~0 (ms)
i
ii
Main rimMain rim
First ruptureFirst rupture
Bag filmBag film
Figure 1
(a) Dominant forces acting on an isolated droplet interacting with a gas stream with velocity u1. The disruptive forces are the
aerodynamic shear force Fs and pressure force Fp. The resistive forces are the capillary force F and viscous force F. The body force is
Fb. (b) Weber number (We) and Ohnesorge number (Oh)-based regime map depicting boundaries between various breakup modes.
(i,ii) Evolution of distinct breakup modes at low Oh ( <102), with subpanel i showing bag breakup at We 15 and subpanel ii showing
shear stripping at We 1,500. (c) Extension of the regime map to Mach number (Ma) space. Distinct morphological features are
imposed due to compressible effects. Abbreviations: RTP , Rayleigh–T aylor piercing; SIE, shear-induced entrainment. Panelb adapted
from (i) Sharma et al. (2021) (CC BY 4.0 ) and ( ii) Chandra et al. (2024a) (CC BY 4.0 ). Data in panel b from Lane (1951), Hinze (1955),
Hanson et al. (1963) , Loparev (1975), Hsiang & Faeth (1992 , 1995), Theofanous (2011), Sharma et al. (2021 , 2023a), Chandra et al.
(2023), and Chandra et al. (2024a) . Panel c adapted with permission from Dinh et al. (2003) and Wang et al. (2020) (CC BY 4.0 ).
discuss the various breakup modes and the celebrated regime map based on We and Oh. However,
further research reveals that these numbers and the underlying force balances are insufficient to
explain various observations under extreme flow velocities. The gas phase Reynolds number (Re),
for instance, is necessary to explain the formation of the wake and the local transient boundary
layer (BL) in the inertial dominated regimes. Furthermore, the Mach number (Ma) is essential,
especially if the flow is supersonic with prominent compressible effects. These extreme conditions
are discussed in subsequent sections.
www.annualreviews.org  Secondary Atomization at Extreme Conditions 85

<!-- PDF_PAGE: 4 -->

Downloaded from www.annualreviews.org.  Guest (guest) IP:  103.151.173.209 On: Sat, 29 Aug 2026 07:53:40
FL58_Art04_Basu ARjats.cls November 28, 2025 12:3
Mach number (Ma):
the ratio of gas phase
velocity to speed of
sound, representing
the degree of
compressibility
Machine learning:
its efficient pattern
recognition
capabilities can
identify obscure
modes, e.g.,
catastrophic breakup;
physics-informed
neural networks can
potentially correlate
these modes with final
daughter droplets
1.1. Modes of Breakup
The droplet undergoing aerobreakup starts from a spherical shape and evolves into complex
structures reminiscent of a scuffed jellyfish, involving elements like waves, sheets, and ligaments.
Although the process seems catastrophic, the intermediate geometry displays certain characteris-
tic features or modes. Historically, various names have been proposed following visual cues such
as oscillating blobs, flapping sheets, and growing bags. Consolidating these segments, the breakup
modes were classified as vibrational, bag, multimode, stripping, and catastrophic breakup ( Hsiang
& Faeth 1992, 1995; Guildenbecher et al. 2009). These descriptions are coarsely sufficient to qual-
itatively describe the breakup modes and can be quantitatively delineated using only We, when
viscous and compressible effects are negligible, i.e., Oh < 101 and Ma < 0.3 (see Figure 1b).
In the vibrational regime (We < 11), the droplet oscillates at a resonant frequency and breaks
down into smaller droplets. At higher We, the droplet flattens into a disc due to nonuniform pres-
sure forces. During this process, the gas (lighter medium) accelerates into liquid (denser medium)
at the forward-facing segment of the droplet. This leads to the formation of unstable waves due
to Rayleigh–T aylor instability (RTI). It manifests first as a single wave spanning across the disc,
leading to the formation of a single bag with a toroidal rim in the bag breakup regime (We
< 80). Multimode breakup is realized with shorter RTI waves at even higher We, which leads
to more complicated bag shapes, including stamen and multiple bags. Shear-induced instabilities
also emerge at this stage. If we climb higher on the We ladder, the shear on the interface leads
to the formation of waves originating from a Kelvin–Helmholtz instability (KHI) in the stripping
regime (We < 350). These KHI waves induce liquid transport along the droplet periphery, where
it is stripped off in the form of drops, sheets, or ligaments. Finally, a catastrophic breakup is ob-
served for We > 350 with rapid destabilization and extreme fragmentation reflecting RTI and
KHI signatures. This regime with complex three-dimensional structures and rapid breakup is not
well-defined in the literature. Machine learning techniques may serve as an effective approach for
mode identification.
Later studies realized the prominent role of unstable waves in molding the breakup morphol-
ogy. Hence, RTI and KHI mechanisms were the foundational pillars in reclassifying the breakup
modes into Rayleigh–T aylor piercing (RTP) and shear-induced entrainment (SIE) ( Theofanous
2011). In the above-mentioned breakup hierarchy (with increasing We), multimode breakup marks
the transition between RTP and SIE. At a higher We, KHI was found to be more prominent, pro-
moting SIE modes, with catastrophic breakup a more extreme extension of stripping breakup,
wherein RTI waves were also excited.
These high We events are now of interest, considering their myriad applications. Recent studies
have explored these extreme atomization events with We D 1,000–10,000 ( Sharma et al. 2021 ,
2023a; Chandra et al. 2023 ). The roles of KHI and RTI were identified by considering simplified
models, which are discussed in subsequent sections. Shadow images of various breakup modes are
depicted in Figure 1b. Schematics illustrating RTP (bag breakup) and SIE (shear breakup) can be
found in Figure 2, where a detailed account of deformation scales and characteristic morphologies
is presented.
1.2. Simple but Inadequate Regime Map
It is intuitively expected that the change in the relative balance of dominant forces will alter the
breakup, i.e., the interface evolution. This balance, when framed in terms of the dimensionless
numbers, can act as an indicator demarcating different modes of breakup. If we expect the disrup-
tive aerodynamic forces to be predominantly balanced by the surface tension and viscosity of the
liquid, We and Oh are typically obvious choices to construct a regime map. As consolidated by
86 Rao  Basu

<!-- PDF_PAGE: 5 -->

Downloaded from www.annualreviews.org.  Guest (guest) IP:  103.151.173.209 On: Sat, 29 Aug 2026 07:53:40
FL58_Art04_Basu ARjats.cls November 28, 2025 12:3
a
Bag
breakup
e
b c
Shear
breakup
Disc
Cupcake
Bag
d
u∞
d0
ξ ~ d0 ξ ~ λRT0
ξ ~ λKH
ξ ξ
Figure 2
(a) Evolution of distinct modes of breakup, with salient topological features of the interface.  represents length scales associated with
deformation at different stages of breakup. The bag-assisted breakup has a Rayleigh–T aylor instability–type wave mechanism imposed
as a dominant scale  RT0 . (b,c) An experimental shadowgraph image is shown for ( b) single bag and ( c) bag and stamen mode.
(d) The shear-assisted breakup with a Kelvin–Helmholtz instability–type wave mechanism, where  KH. These waves are stripped in
the form of ligaments and eventually droplets through the Rayleigh–Plateau instability wave mechanism. ( e) Shadowgraph image for
the shear stripping mode. Panels b and c adapted with permission from Jackiw & Ashgriz (2021) . Panel e adapted with permission from
Sharma et al. (2021) (CC BY 4.0 ).
Krzeczkowski (1980) and Hsiang & Faeth (1992 , 1995), various studies filled the We–Oh space
up to moderate ranges, but recent studies have explored the higher We regime. The delineat-
ing boundaries between the previously established breakup modes from experiments are marked
in Figure 1 b, along with a corresponding semiempirical fit. Later studies by Theofanous (2011)
tweaked these boundaries based on the reclassified regimes, i.e., RTP and SIE modes, to accommo-
date the extreme We–Oh domain. Studies spanning a moderate Oh range but very high We with
different classes of liquids, including water ( Sharma et al. 2021 ), polymer ( Chandra et al. 2023 ),
and liquid metal ( Sharma et al. 2023a ), also illustrate the transition from RTP to SIE beyond a
certain critical We.
From all these efforts, the first important takeaway is the universal Oh insensitivity of the
regime shift for Oh < 101 across different configurations. However, a discrepancy can be ob-
served in We depicting the transition between regimes across different studies, especially at
extreme flow conditions with high gas phase velocities. This inadequacy is expected if we ac-
count for effects like inertial dominance, represented by Re, and compressibility of the gas phase,
represented by Ma. Hence, a possible extension of the regime map into We–Oh–Ma space might
capture the complete dynamics. Recent endeavors into the effects of Ma on aerobreakup have re-
vealed various modifications of the earlier breakup modes with slight but persistent morphological
differences. Figure 1c shows the impact of Ma on droplet topology, with constant We and Oh to
isolate compressibility effects. The longitudinal extensional geometry, such as elongated bags and
ligaments, is more emphasized in high Ma flows.
Apart from these considerations, one must ponder whether the idea of a sedentary regime map
is sufficient and the consequences of overlooking transient dynamics, where the breakup modes
are bucketed based on intermediate topologies. T o demonstrate this insufficiency, consider the
aerobreakup of polymeric liquids with different rheological properties ( Chandra et al. 2023 ). It
was observed that the early stages of breakup were universal; however, the regime map starts
bifurcating into specific modes as time progresses, and the final regime map emerges with dis-
tinguishable topologies. Similar early universal topological stages of breakup were observed with
Newtonian liquids as well, including water and liquid metal ( Sharma et al. 2023a ), hinting at a
www.annualreviews.org  Secondary Atomization at Extreme Conditions 87

<!-- PDF_PAGE: 6 -->

Downloaded from www.annualreviews.org.  Guest (guest) IP:  103.151.173.209 On: Sat, 29 Aug 2026 07:53:40
FL58_Art04_Basu ARjats.cls November 28, 2025 12:3
common mechanism. Understandably, these shared temporal underpinnings are lost in a static
regime map.
2. INTERFACIAL DYNAMICS
The motion of the liquid–gas interface is an essential aspect in understanding events such as
secondary atomization. The interfacial dynamics are usually modeled by considering waves de-
veloping over the boundary as a precursor to fragmentation ( Joseph et al. 1999 , Guildenbecher
et al. 2009 , Theofanous 2011 ). When exposed to high-speed gas streams, the liquid interface is
destabilized with excitation of specific wave modes (discussed later).
2.1. Multiscale Deformations
Droplets undergoing fragmentation encounter complex intermediate states resulting from desta-
bilization of the liquid interface. First, the droplet flattens due to a nonuniform pressure
distribution over the surface, resembling a bluff body flow with a trailing wake. This leads to
deformation into an ellipsoidal shape, during or after which the onset of interfacial instabilities
occurs. This sequence of events involves multiscale deformation of the droplet surface with dif-
ferent characteristic length scales and timescales. We denote the initial droplet diameter by d0
and the deformation length scale as  , as depicted in Figure 2 a. The initial inertial droplet de-
formation  d0 can be categorized as a global deformation, common to both RTP (bag) and
SIE (stripping) modes. In the SIE mode, it looks more like a cupcake rather than a disc due to the
dominant aerodynamic shear. Additionally, this deformation imparts acceleration on the interface,
imposing an effective pseudobody force misaligned with the density gradient across the interface.
With a lighter fluid pushing into the heavier liquid, RTI is established. The amplitude and wave-
length RT0 associated with this phenomenon represent the length scale of this deformation, where
 RT0 d0 for moderate We, i.e., the RTP mode. This indicates a global deformation, which
can assume a single bag ( Figure 2b) or multibag ( Figure 2c) formation ( Jackiw & Ashgriz 2021 ).
Shear-driven waves form over this droplet interface at higher We, suggesting an SIE mode, depict-
ing KHI, where  KH. This is subsequently or simultaneously superimposed with the previous
deformations, depending on other factors discussed below. For a typical SIE morphology, we have
KH≪ d0; hence, these waves can be regarded as a local deformation. The crest of these waves
accelerates into the lighter medium to form sheet-like structures. These sheets have RTI in the az-
imuthal direction superimposed over the preceding deformations. When the amplitude becomes
large, they elongate and form corrugated ligaments that eventually break down into droplets due
to the Rayleigh–Plateau instability (RPI), as depicted in Figure 2d. This final stage of azimuthal
instability and consecutive deformation/fragmentation can again be considered a local instability,
since the associated length scales are much smaller than the droplet size ( Figure 2e). This shows
us the following:
■ The deformation can be broadly classified as global or local based on the associated length
scale.
■ The deformations happen at multiple spatiotemporal scales with a characteristic offset at
the onset of each kind, so that the successive class of deformation is superimposed over the
predecessors, typically in a nonlinear fashion.
■ The emergent behavior is a complex cascade of deformations with progressively diminishing
length scales and timescales ( Zandian et al. 2019 , Thiesset et al. 2021 ).
The elements associated with these subsequent deformations, i.e., waves, sheets, ligaments,
and droplets in SIE, are illustrated in Figure 3 . Their origins from unstable mechanisms in
88 Rao  Basu

<!-- PDF_PAGE: 7 -->

Downloaded from www.annualreviews.org.  Guest (guest) IP:  103.151.173.209 On: Sat, 29 Aug 2026 07:53:40
FL58_Art04_Basu ARjats.cls November 28, 2025 12:3
Linear stability
analysis: the linear
model, or the
first-order estimate,
effectively predicts the
wavenumber of the
dominant normal
mode of the unstable
waves during the
initial growth phase of
infinitesimally small
perturbations that
generally persist in the
finite-amplitude
regime
Front
View Side
View
a
c
Ligaments
Azimuthal
instabilities
Longitudinal
instabilities
Cupcake
Droplets
Hole
formation
Sheets
Parent
droplet
db
KH waves
Sheets
Ligaments
Droplets
u∞
λRT
λRT0
τ = 0.77τ = 0.58τ = 0.39
1 mm
Figure 3
(a) Numerical results of isolated droplet breakup in shear-induced entrainment mode at Weber number (We) 1,000, illustrating
characteristic topological features, and experimental shadowgraph images for ( b) shear-induced wave evolution over the droplet
periphery representing sheet to ligament transformation, ( c) RTI waves in the azimuthal direction, superimposed over KHI observed as
periodic ligaments, and ( d) longitudinal RTI apparent during catastrophic breakup at higher We. Abbreviations: KHI, Kelvin–
Helmholtz instability; RTI, Rayleigh–T aylor instability. Panela adapted with permission from Dorschner et al. (2020) . Panel c adapted
from Sharma et al. (2021) (CC BY 4.0 ). Panel d adapted from Chandra et al. (2023) .
longitudinal (along the flow) and azimuthal directions are evident from numerical ( Jalaal &
Mehravaran 2014 , Dorschner et al. 2020 ) and experimental observations ( Sharma et al. 2021 ,
2023a; Chandra et al. 2023 ). First RTIs (superimposed over droplet front), KHI, and RPI
(Figure 3 b) appear to act longitudinally, while the second RTI (superimposed over KHI) acts
in the azimuthal direction ( Figure 3 c), setting up a stage for RPI. Although SIE involves
KHI-dominated initiation, the longitudinal RTI typically shows up in catastrophic breakups with
large We, by virtue of extreme accelerations, as depicted in Figure 3 d with  RT≪ d0 (local
deformation).
2.2. Linearized Approach for Wave Mechanisms
After the deformation stage, the liquid interface exhibits waves driven by different mechanisms.
These waves exhibit a characteristic wavelength and growth rate, establishing a spatiotemporal
signature. A dispersion relation can be generated from linear stability analysis (LSA) for infinites-
imal perturbations. The fastest growing wave signatures are expected to be preserved to a certain
extent, even in the nonlinear regime with large wave amplitudes ( Joseph et al. 1999 ). RTI can be
modeled by estimating the acceleration of the fluid interface at the forward-facing part of the de-
forming droplet. The acceleration induces a pseudobody force, which can be substituted into the
canonical dispersion relation for infinite domain geometry (Drazin & Reid 2004) or a semiinfinite
case with finite liquid thickness ( Mikaelian 1996). However, a correct estimate of acceleration is a
challenging task (Theofanous 2011). The shear instability was first considered for a simple inviscid
configuration with a step discontinuity across fluid interfaces. Viscosity is incorporated through
viscous potential flow ( Funada & Joseph 2001 ) or by artificially imposing a BL at the interface.
Several solutions ( Villermaux 1998 , Padrino & Joseph 2006 , Behzad & Ashgriz 2014 ) derived
www.annualreviews.org  Secondary Atomization at Extreme Conditions 89

<!-- PDF_PAGE: 8 -->

Downloaded from www.annualreviews.org.  Guest (guest) IP:  103.151.173.209 On: Sat, 29 Aug 2026 07:53:40
FL58_Art04_Basu ARjats.cls November 28, 2025 12:3
200
100
00 20 40
10–1 100100
101
101 102 103 104 105
We
Air
Liquid
10,000
500
400
300
200
100
0
8,000
6,000
4,000
2,000
20 40 60 80 100 120 140
a b c
d e f
0 2,000 4,000 6,000 8,000 10,000
0
2,000
4,000
6,000
8,000
We
 RTI
 KHI
0
40
80
120
RTP
MM
SIE
0.09 0.12 0.15 0.18 0.21
0.03
0.06
0.09
0.12
 Galinstan - Air
 Galinstan - Nitrogen
 Water - Air
u∞
ua
δa
δl
ul
We
κ κ
(ω)
(ω)
(ω)(ω)
10,000
8,000
6,000
6,000
5,000
4,000
3,000
2,000
1,000
0
4,000
2,000
50 100 150 200
We 2,000
1,000
00 50 100κ κ
ωmax
κmax
1/ΛKH = d0/λKH
ΛKH = λKH/d0
ρl
Red
1
ρa
ωmax)(κmax,
Figure 4
(a) A schematic illustrating a shear flow imposed on the liquid interface with local velocities in liquid ul and gas ua. Dispersion relation
relating normalized wavenumber ¯  and growth rateℑ( ¯!) (imaginary part) is shown at different Weber numbers (We) for ( b)
longitudinal RTI and ( c) KHI. The insets depict the explicit curve for We D 2,000. (d) Properties of the fastest growing wave,
illustrating that KHI waves grow faster with higher wavenumbers compared to RTI. For panels b–d, d0D 2 mm and Ohnesorge number
(Oh)D 0.002. (e) Breakup mode classification based on length scale compatibility conditions d0=KH O(1). The theoretical KH is
calculated from prior data depicted in Figure 1b (same symbols) with Oh <1. ( f ) Experimental KH for different fluids illustrating
Reynolds number (Re)-dependent scaling or inertial dominance. Abbreviations: KHI, Kelvin–Helmholtz instability; MM, multimode;
RTI, Rayleigh–T aylor instability; RTP , Rayleigh–T aylor piercing; SIE, shear-induced entrainment. Panelf adapted from Sharma et al.
(2023a).
inspiration from Rayleigh’ s effort for instability across shear layers of finite thickness ( Rayleigh
1880). A model with a linear BL profile was proposed for liquid jets, explaining the primary at-
omization with sufficient accuracy ( Marmottant & Villermaux 2004). The error-function velocity
profile serves as a better physical approximation for the BL and has been extensively studied in
the context of mixing layers and liquid jets ( Boeck & Zaleski 2005 , Otto et al. 2013 ). A solution
for jets ( Marmottant & Villermaux 2004 ) was implemented for a droplet undergoing secondary
atomization ( Figure 4 a) without significant modifications ( Jalaal & Mehravaran 2014 , Sharma
et al. 2021 ). Existing models for an infinite geometry were used without accounting for droplet
curvature, yielding reasonably good results for early-stage wave formation, despite simplifying
assumptions.
T o closely resemble the actual scenario, BLs are considered on both sides of the liquid interface
with suitable interface matching conditions. For high density and viscosity contrast, the liquid
side BL can be neglected, while the air side BL with a linear velocity profile approximation is
considered. The relations for wavenumber  and growth rate ! are depicted below, following the
modified dimensionless parameters:
¯D d0D 2
( d0

)
, ¯!D !
√
ld3
0
 , ¯D a
l
: 2.
90 Rao  Basu

<!-- PDF_PAGE: 9 -->

Downloaded from www.annualreviews.org.  Guest (guest) IP:  103.151.173.209 On: Sat, 29 Aug 2026 07:53:40
FL58_Art04_Basu ARjats.cls November 28, 2025 12:3
The time t, in general, is normalized using the inertial timescale tiD d0=ua(l=a)1=2 such that
D t=ti (Nicholls & Ranger 1969). This ti can also be used to normalize !, instead of the capillary
scale tD (ld3
0 = )1=2 used in Equation 2 (t =tiD We1=2). A dimensionless dispersion relation for
a primary RTI wave (RT 0) is given by Sharma et al. (2021) :
¯!2D ¯
√
1C ¯
{ 3
4 WeCd (1 ¯ ) ¯ 2
}
, 3.
where Cd is the drag coefficient. A dimensionless dispersion relation for KHI waves (for We ≫ 1
and ul! 0) is written as ( Marmottant & Villermaux 2004 )
e2
Df1 (2C )g
1C 1
2
(
1
¯C 1
)
(2 )
1C 1
2
(
1
¯ 1
)
(2 )
, 4.
D ¯qp
Re
, D ¯!q
√
¯
WeRe , D  2, 5.
where q is a parameter relevant to the air BL thickness aD qd0=Re1=2 (Sharma et al. 2021 ). !
is complex with the imaginary part ℑ(!) contributing to the wave growth. The contour plots in
Figure 4 b,c illustrate a shift to faster growth rates and smaller wavelengths as We is increased
for both the mechanisms. A comparison of growth rates of the fastest growing wave [ ¯!maxD
max(ℑ( ¯!))] at every We reveals that KHI dominates (see Figure 4 d) and is expected to be ob-
served more prominently for high We and is much smaller in wavelength when compared to the
RTI. These waves (or deformations) establish a platform for successive waves, manifesting a com-
plex cascade. Marmottant & Villermaux (2004) also deduced the dispersion relations for azimuthal
RTI and ligament RPI. As illustrated recently ( Behzad et al. 2015 , Dworzanczyk et al. 2025 ), the
curved interface affects the instabilities, and accounting for this effect is essential for more accurate
representations.
2.3. Competing Scales and Compatibility Conditions
The waves originating from different mechanisms compete, strongly influencing the morphology
of the breakup. T o emphasize this, consider the length scales associated with the deformations, as
discussed earlier,  . For deformations to physically manifest, it is a geometric necessity that
 < d0. This implies that a transition is expected when 3D  =d0 1. As observed earlier, KHI is
typically a faster growing wave at high We, constituting the SIE regime. This, for instance, will
occur only for We with 3KHD KH=d0≪ 1. If 3KH is large, the droplet flattens into a disc in the
absence of KHI waves. Corresponding to the instantaneous gas flow around this deformed state,
the disc/droplet typically supports the formation of RTI waves (as3RTD RT0 =d0 1), promoting
RTP modes. Here, 3RT determines the number of bags ( Zhao et al. 2010 , Jain et al. 2015 ).
Thus, the length scale plays an important role in predicting breakup morphology. This per-
spective illustrates the complex spatiotemporal dynamics, with various features competing in time
to grow. However, their occurrence also depends on the availability of space, i.e., spatial compati-
bility. This transition criterion can be employed to predict the changeover between SIE and RTP
modes. It is expected that 3KH O(100–101) will mark the boundary in the regime map. V ari-
ous experimental observations where 3KH is theoretically determined based on a suitable model
(here linear BL is considered for simplicity) are plotted in a regime map in Figure 4e. The mode
transition is apparent at 1 =3KH 6 O(1), which validates the proposed criterion. This hypoth-
esis holds well even though these models involve crude approximations, including LSA, which is
expected to be violated with inherent nonlinear effects.
www.annualreviews.org  Secondary Atomization at Extreme Conditions 91

<!-- PDF_PAGE: 10 -->

Downloaded from www.annualreviews.org.  Guest (guest) IP:  103.151.173.209 On: Sat, 29 Aug 2026 07:53:40
FL58_Art04_Basu ARjats.cls November 28, 2025 12:3
2.4. Extreme Flow Conditions
Extreme flow conditions in the present context refer to airflows with very high velocities, which
lead to extremely large We and Re values. Apart from this, there can be other flow configura-
tions presenting extrema, like high-temperature gas or liquid, a transcritical condition near the
triple point, supersonic or hypersonic flows, high-speed turbulent flows, and impulsive shock-
driven flows. While some of these cases will be addressed later, the simplest case with high-speed,
uniform, steady airflow is considered first for a glimpse into the complexities.
2.4.1. Inertial aerodynamic dominance. For extremely high-speed flows (large We and Re), it
is important to consider the dominance of the inertial contribution toward fragmentation (aua2)
(Sultanov & Y arin 1990). This dominance might lead to the ineffectiveness of surface tension to
represent certain features of the interfacial dynamics. This is also evident from the dispersion rela-
tion presented by Marmottant & Villermaux (2004) , where the terms involving (1/We) diminish.
The simulations incorporate this effect by disregarding surface tension at high We ( Dorschner
et al. 2020 ). Figure 3 a illustrates these results for We D 1,100, showing qualitative agreement
with experimental data. However, the inertia is still counteracted by the viscous resistance to the
airflow near the fluid interface, leading to the formation of a BL, with Re representing this bal-
ance. In this particular extremity, the BL plays a significant role in shaping the dispersion relation.
Consequently, it is anticipated that the initial wave dynamics are more accurately represented
by Re rather than by We. This is further supported by experimental observations ( Sharma et al.
2023a) that examined various fluid pairs at high We flow conditions, as illustrated in Figure 4 f.
The normalization of axes follows that of Marmottant & Villermaux (2004) .
2.4.2. Catastrophic breakup. The catastrophic breakup is widely misunderstood to be an in-
stantaneous and random phenomenon. The deformation cascades, as discussed earlier, indicate an
associated cycle time dependent on the growth rates tc 1=ℑ(!). As some of these wave mecha-
nisms occur simultaneously, the overall breakup time is expected to be a nonlinear combination
of these cycle times. For a catastrophic breakup, the cycle time of these deformations or waves
is extremely small; hence, the cascade is not visually apparent. The final morphology comprises
features associated with waves exhibiting the fastest growth rates. Hence, the initial growth rate
of global RTI deformations is comparable to or even higher than KHI beyond certain We or Re
(Mizuno et al. 2022 ). We see the periodic signature of RTI waves on the fragmenting droplet in-
terface and daughter droplet clusters in a catastrophic breakup event ( Chandra et al. 2023 ) (see
Figure 3 d). The limited spatiotemporal resolution in experiments or simulations makes it dif-
ficult to capture these transient intricacies. Experiments involving shadowgraphy typically focus
on imaging the two-dimensional or line-integrated projections of the events. Hence, experiments
are unable to adequately capture the random, nonlinear, minuscule wave cascades occurring over
very short timescales. Recent advancements in X-ray technology promise an effective method for
interface visualization ( Aliseda & Heindel 2021 ).
3. INHERENT NONLINEARITIES
The flow associated with the two phases is coupled, where both evolve intricately. Even for a
uniform airflow in the far field, the geometry of the undeformed droplet leads to nonuniform
conditions in the vicinity, as illustrated in Figure 5. Due to obstruction, the flow accelerates spa-
tially in the forward part of the droplet. In the downstream, flow separation behind the droplet
leads to wake formation and vortex shedding (Meng & Colonius 2015). The resultant nonuniform
shear and pressure on the interface initiates a chain of transient deformations and waves. These
deformations modulate the base flow, which in turn modulates the deformations, leading to an
92 Rao  Basu

<!-- PDF_PAGE: 11 -->

Downloaded from www.annualreviews.org.  Guest (guest) IP:  103.151.173.209 On: Sat, 29 Aug 2026 07:53:40
FL58_Art04_Basu ARjats.cls November 28, 2025 12:3
d
e
Generation 1 deformation
Generation 2 deformation
Generation 3 deformation Generation 4 deformation
Nonlinear KH evolution
Drag-induced
deformation
Finite KH crest
Local undulation
Liquid sheet
formation
RTI over
KHI crest
a
b
c
RPI over
RTI crest or bag rims
Bags over
KHI crest
or
Bag
Bag rupture
Rim
Ligaments
from rim
Sheet
Ligaments
RT crests
u∞
d0
ua = 0
ua2
ua2
U0 + Uε'
+Ud' +ΣUλ'
ua1ua1
ua1
ua3ua3
uai
uar
∂/uni03A90
∂/uni03A90 + ∂/uni03A9d
+∂ξd
+∂ξλ1
+∂ξλ1 +∂ξλ2 +∂ξλ2 +∂ξλ3
∂ξui
∂ξui
∂ξui+1
∂ξui+1
∂ξui+2
ua ≈ 1.5u∞
λKH
λRT
λRP
λRT
(x, t)
(x, t)
λ1
a
λ2
λi
λn
t'
Wed(t + t')
md(t + t')
pi(d)
WeiuWeiu Wei+2u
Wei+1uWei+1u
Wed(t)
md(t)
f g
Figure 5
(a) Deformation at a global scale /2202  d involving coupled droplet–wake evolution. ( b) Formation of KHI waves or local deformation @ 1
over a deformed droplet interface with transient longitudinal curvature R∥. This is followed by drag-induced (from U′
) wave crest
evolution, leading to sheet formation. ( c) RTI-induced deformation @ 2 of the curved wave crest with longitudinal curvature R?. The
sheets evolve either through RTI into crests that form corrugated ligaments ( @ 2) or into bags, depending on the direction of the
predominant acceleration. The bag ruptures eventually, also leaving behind ligaments (from the rim). These break into droplets
through the RPI. ( d) Schematic illustrating the droplet breakup as an inherently nonlinear, two-way coupled system with a cascade of
perturbations in gas flow and interface, occurring at different scales. Free stream uniform flow U0 is superimposed with perturbations
U′
". This flow evolves over the global curvilinear geometry superimposed as U′
d and wave-level geometry as U′
. (e) Illustration of
two-way coupling at small scales where the local undulation  i
u and the effective Weber number (We i
u) are transient and evolve until the
undulation breaks down into droplets with the probability distribution pi(d). ( f ) Shadowgraph images depicting subsecondary
atomization events from sheet to ligament and ( g) sheet to bag, which ruptures leaving ligaments. Abbreviations: KHI, Kelvin–
Helmholtz instability; RPI, Rayleigh–Plateau instability; RTI, Rayleigh–T aylor instability. Panels f and g adapted from Rao & Basu
(2025).
interplay between airflow and interfacial dynamics. This leads to an inherent nonlinearity. Com-
plexities are also imposed by the type of fluid, such as viscoelastic polymers ( Theofanous 2011 ;
Chandra et al. 2023 , 2024a,b) and suspension with complex rheology ( Xu et al. 2023 ) or even liq-
uid metals with an outer oxide layer ( Sharma et al. 2023a ). However, in this review, the influence
of these factors on aerobreakup is not addressed.
www.annualreviews.org  Secondary Atomization at Extreme Conditions 93

<!-- PDF_PAGE: 12 -->

Downloaded from www.annualreviews.org.  Guest (guest) IP:  103.151.173.209 On: Sat, 29 Aug 2026 07:53:40
FL58_Art04_Basu ARjats.cls November 28, 2025 12:3
3.1. Evolving Geometry and Flow Perturbations
The coupled stages of the droplet deformation and trailing wake evolution are depicted in
Figure 5 a. This can be treated as a global deformation or perturbation /2202 3d superimposed on
the base droplet shape /2202 0. The KHI waves hence develop over an interface with varying lon-
gitudinal curvatures R∥. This subsequent deformation /2202  1 is superimposed on the predecessors,
as shown in Figure 5b. On a closer look, the wave crest of a finite-amplitude KHI wave obstructs
the local airflow significantly (with ua2 > ua1, ua3), forming a mini wake region, thereby causing
drag along the flow direction ( Hoepffner et al. 2011 ). The local flow separation and recircula-
tion zones behind the crest further aggravate this catapulting phenomenon ( Jerome et al. 2013 ).
When viewed from the top (see Figure 5c), these wave crests are curved and form sheets as they
accelerate into the lighter medium, with RTI waves in the azimuthal direction (RTI /22a5 ). The cur-
vature R? in the azimuthal direction is again a function of space and time. The catapulting effect
immediately transforms these RTI crests into ligaments. These corrugated ligaments are sheared
by the already perturbed airflow, where air-assisted capillary action leads to RPI and fragmenta-
tion. Subsequent wave mechanisms impose next-generation deformations 6/2202  . The nonlinear
dynamics, i.e., the interplay between the two phases, can be represented as
@ !U , 6.
and the superimposed cascade of modulations to the airflow and interface geometry are then
perceived as
@D @ 0C @ dC 6@ C @ "
UD U0C U′
dC 6U′
C U′
" , 7.
where /2202  denotes the droplet interface/topology, /2202  depicts deformation or perturbation to base
topology, and U denotes the surrounding airflow with prime depicting fluctuations or perturba-
tions. The subscripts have the following significance: 0 for base state when undeformed, d for
perturbations due to global deformations,  for perturbations due to local deformations arising
from various wave mechanisms, and " for perturbations arising from external forcing or turbu-
lence. For an instantaneous snapshot, these elements of perturbation are illustrated in Figure 5d.
As the flow in the vicinity is nonuniform ( uai), the local unstable waves are also modulated ( i).
The components of Equation 7 are systematically illustrated in Figure 5a–d.
The internal flow of the liquid within the droplet can also be decomposed in a similar fashion,
but it is typical to rely on the interface topology and the relevant boundary conditions imposed
by external aerodynamic forcing. The internal redistribution of liquid within the droplet during
fragmentation, however, is crucial for a better understanding. Recent works ( Opfer et al. 2014 ;
Jackiw & Ashgriz 2021 , 2022; Obenauf & Sojka 2021 ; Kulkarni et al. 2023 ) in the moderate We
regime considered internal flow to predict bag/rim dynamics and droplet sizes.
3.2. Wave Cascade
The droplet undergoes a chain of deformations, most of them originating from an unstable wave
mechanism (KHI, RTI, or RPI). As depicted in Figure 5a–c, the wave cascade can be expressed as
generations. The zeroth generation corresponds to the global deformation /2202  d or /2202  0, and the ith
generation is depicted as /2202  i (we are omitting  here onward for conciseness), which represents
unstable waves. The subsequent generations observed in the SIE breakup at high We follow:
j@ 0j d0, 8.
j@ ij≪ d0, 9.
94 Rao  Basu

<!-- PDF_PAGE: 13 -->

Downloaded from www.annualreviews.org.  Guest (guest) IP:  103.151.173.209 On: Sat, 29 Aug 2026 07:53:40
FL58_Art04_Basu ARjats.cls November 28, 2025 12:3
Subsecondary
breakup process:
Breakup of an
undulation or a smaller
protrusion on the
surface of a deforming
droplet. This localized
phenomenon
demonstrates a
self-similar behavior
(qualitatively) akin to
that of secondary
atomization
wherejj represents the scale of the deformation topology /2202  i; withj/2202  ij  i, conforming to
previous definitions, Equation 9 is synonymous with the compatibility criterion discussed earlier.
It is typical to observe that for a given generation of wave or deformation, say in the longitudinal
direction, the next generation is superimposed over it in the azimuthal direction, and this alter-
nate pattern is repeated (longitudinal KHI, azimuthal RTI, and longitudinal RPI wave cascade).
In addition, recent developments by Zandian et al. (2018) suggest vortex dynamics as an interest-
ing mechanism for cascade evolution in primary atomization, with the potential for extension to
secondary atomization.
3.2.1. Effective local Weber number. The recurring cascades originate from, say, each KHI
wave crest and terminate into daughter droplets as depicted in Figure 5e. At each generation, the
effective We and Oh can be defined based on deformation length scale j/2202  ij and local effective
gas flow velocity u′
a as
We′
i au′2
aj@ ij
 , 10.
Oh′
i l
plj@ ij : 11.
This is based on a hypothesis postulating a similarity between primary and secondary atom-
ization, where the local undulation formed over a liquid jet during breakup can be equivalently
treated as a segment of a droplet (Wang et al. 2008). Based on the scales of the undulation and local
effective We, the breakup dynamics were predicted locally, drawing inspiration from secondary
atomization. The same philosophy is extended, and the local breakup dynamics of the undula-
tion over a droplet are treated as a subsecondary breakup process ( Rao & Basu 2025 ). Although
Zandian et al. (2017) mapped potential modes of undulation evolution (for primary atomization)
based on global parameters, a local parameter presents a self-similar approach suitable for this mul-
tiscale cascade ( Rao & Basu 2025 ). After a particular generation, say ic, the aerodynamic effects
may not significantly affect the breakup dynamics when the effective We drops below a critical
value We′
ic < Wec. Since the undulations are small, the local Oh will be much larger than the
global definition, and viscous effects might resist the breakup. Hence We′
i and Oh′
i can be used to
predict the evolution of undulation into a sheet or a ligament and the subsequent breakup ( Rao
& Basu 2025 ). Figure 5e illustrates these local definitions of flow parameters and their evolution
in time. Apart from this, the effective global We and Re are also transient as the droplet shape
evolves. The effective mass md of the system is continuously depleted due to stripping, along with
simultaneous deformation, affecting the topology and associated aerodynamic parameters of the
remnant parent body (see Figure 5e).
3.2.2. Recurrent behavior with associated timescales. As discussed earlier, there is an asso-
ciated cycle time (tc,i) with each generation ( i) of the wave cascade. This timescale is dependent on
the growth rate of the fastest growing wave mode !i (imaginary part) as
tc,i 2
!i
: 12.
The dominant mode prescribes a specific subsecondary atomization process. Usually, these com-
peting waves evolve simultaneously. The nonlinear superposition of waves determines the cycle
time of a cascade. This mechanism facilitates stripping of liquid from the undulated liquid surface,
thereby exposing a new liquid front. The subsequent cascade on this fresh interface depends on
the current topology and effective We, as depicted in Figure 5 e. This recurrent shedding or
www.annualreviews.org  Secondary Atomization at Extreme Conditions 95

<!-- PDF_PAGE: 14 -->

Downloaded from www.annualreviews.org.  Guest (guest) IP:  103.151.173.209 On: Sat, 29 Aug 2026 07:53:40
FL58_Art04_Basu ARjats.cls November 28, 2025 12:3
First ligaments
observed
First fragments
observed Lips
U-shape
ligaments
First breakup : B1 Second breakup : B2
Third breakup : B3 Fourth breakup : B4
b
200 300 400 500 600 700
0.0
0.5
1.0
1.5
2.0
We
τc = tc/ti
B1
B2
B3
B4
KHI
RTI T
RPI
St
Lips
a
Fragmented
U-shape
ligaments
Fragmented
U-shape
ligaments
Figure 6
(a) Recurrent shedding of the ligaments during aerobreakup. ( b) Comparison of individual shedding period
of ligaments with normalized timescales associated with various instabilities and wake vortex shedding,
where St is the Strouhal number–based period and We is the Weber number. Abbreviations: KHI,
Kelvin–Helmholtz instability; RPI, Rayleigh–Plateau instability; RTI, Rayleigh–T aylor instability.
Figure adapted and data reproduced with permission from Dorschner et al. (2020) .
stripping behavior was discussed in experiments and simulation at moderate We by Dorschner
et al. (2020) , where repeatedly formed ligaments break down into droplets. The same has been
illustrated in Figure 6 a where the ligament sheddings are marked as breakup events (B1–B4).
The cycle time of each is clocked from the previous shedding. The empirical fits are presented
in Figure 6 b. The cycle times of various wave modes are determined from the corresponding
growth rates ( Marmottant & Villermaux 2004 ) and are overlaid with experimentally observed
shedding cycle times. These timescales depict a similar order of magnitude. This includes the
vortex shedding timescale, associated with an effective sphere (bluff body) corresponding to a
deformed droplet ( Dorschner et al. 2020 ). It was observed that the deformed state spans a space
twice the initial diameter, irrespective of We. The authors presumed airflow vortex shedding as
the driving mechanism for the recurrence, as presented by the Strouhal number (St). However,
the wave mechanism occurs over similar timescales. While the droplet interaction with its wake
during the aerobreakup facilitates a two-way coupling, the wave cascade mechanism also emerges
as a significant contender for predicting this recurring behavior.
96 Rao  Basu

<!-- PDF_PAGE: 15 -->

Downloaded from www.annualreviews.org.  Guest (guest) IP:  103.151.173.209 On: Sat, 29 Aug 2026 07:53:40
FL58_Art04_Basu ARjats.cls November 28, 2025 12:3
3.2.3. Ligament-mediated cascade termination. The capillary-dominated breakup mecha-
nism is observed to terminate the wave cascade. A similar idea has been presented for the primary
atomization of liquid jets ( Villermaux et al. 2004 , Ling et al. 2017 ) where the corrugated liga-
ments act as the final entity that creates daughter droplets through RPI (see Figure 3 b). It is
typically observed in SIE that the wave crest of azimuthal RTI superimposed over KHI grows and
enables ligament formation (see Figure 5 c,f ). If the growth is insufficient to support an immi-
nent ligament formation through the RTI mechanism, then the KHI crest may grow into a sheet
bound by a rim undergoing a sheet-mediated breakup ( Wang et al. 2008 ). A canonical study in-
volving the unsteady sheet evolution presented an unstable rim formation, where the mass is shed
as droplets from the rims by a ligament-mediated mechanism ( Wang et al. 2018 ). This dynam-
ics is yet to be extended here in the context of sheets to ligament to droplet transition. Another
possible mechanism involves formation of bags on these sheets by virtue of the aerodynamic drag
induced acceleration and RTI, which disintegrates into fine droplets, leaving behind a rim rem-
iniscent of a thick ligament ( Zandian et al. 2017 , Oshima & Sou 2024 , Rao & Basu 2025 ) (see
Figure 5c,g). Furthermore, holes spontaneously form in these sheets, a phenomenon common to
various atomization processes that led to numerous models for nucleation ( Vrij & Overbeek 1968,
Néel & Villermaux 2018 , Stumpf et al. 2023 ). In the present situation, however, the aerodynamic
disturbance on the liquid film is overwhelming; hence, multiple holes are expected. The central
flattened part of the parent droplet is also topologically similar to a sheet, where these holes have
been observed as well ( Sharma et al. 2021 ). Multiple hole mergers also lead to the formation of
intermediate rims or ligaments ( Néel et al. 2020 , Agbaglah 2021 ), generating a separate class of
droplets. Some of these ligament-mediated mechanisms are documented in the context of bag
breakups ( Jackiw & Ashgriz 2021, T ang et al. 2023) and ocean spray formation ( V eron et al. 2012,
T roitskaya et al. 2017). However, observing these in SIE aerobreakup requires high-fidelity ex-
periments and simulations. In summary, ligaments are the sinews of aerobreakup, and their role
in daughter droplet sizes is discussed in subsequent sections.
4. BREAKUP IN NONIDEAL FLOW FIELDS
A uniform far-field flow interacting with a droplet is extremely rare. However, it serves as a suitable
isolated event to be considered as a canonical problem. In an actual scenario, nonuniformity and
unsteady effects are expected in the external flow. These effects further impose nonlinearity in the
fragmentation process. For instance, the droplets typically appear as groups in a spray through
primary atomization. In such cases, a typical droplet will face a nonuniform unsteady flow (as the
surrounding droplets interact with the incoming air), leading to strong two-way coupling between
the two phases, especially in dense spray systems. Hence, a droplet at the spray plume boundary will
see a shear flow, a wake near the proximity of another upstream droplet, and turbulent or unsteady
flow in the far-field domain downstream, as the spray spreads. The shear, wake, or turbulence-
dominated effects can exist in the upstream airflow as well due to other external factors such as
shock waves.
4.1. Nonuniform Effects: Shear and Wake
The imposed effects will alter the aerodynamic forcing sensed by individual droplets affecting the
breakup mechanism and morphologies. A strong shear layer (two-dimensional) interacting with a
droplet (Figure 7a) presents an asymmetric flow field (Xu et al. 2022). The side and bottom views
(Figure 7b) depict the asymmetric droplet deformation, leading to a sheet-like feature in the flow
(longitudinal) direction and fragmentation through a ligament-mediated mechanism prominent
at the trailing edge or rim. A flapping behavior is also observed, reminiscent of a flag, due to the
www.annualreviews.org  Secondary Atomization at Extreme Conditions 97

<!-- PDF_PAGE: 16 -->

Downloaded from www.annualreviews.org.  Guest (guest) IP:  103.151.173.209 On: Sat, 29 Aug 2026 07:53:40
FL58_Art04_Basu ARjats.cls November 28, 2025 12:3
Eddies: Coherent flow
structures typically
observed in turbulent
flows; large eddies may
have sufficient energy
to induce breakup if
spatiotemporal scales
are matched, while
small-scale eddies may
not be energetic
enough
Shear layer Wake
 Turbulent or
unsteady flow
a c e
b d
f
g
Bag
Top view
Side view
Eddy
Sheet
bending
Stripping around
periphery
Eddy interaction
Droplet
Bag-stamen
U0(r)
U0
d0 d0
d0
+Uε(r, t)'  U0 + Uε(r, t)'
ξf
ξf
ξf
tf
~t res
T = 0T = 0
T = 0.6T = 0.6
T = 0.85T = 0.85
T = 1.2T = 1.2
T = 1.8T = 1.8
Figure 7
(a) Schematic illustrating shear layer interaction with an isolated droplet.  f represents the characteristic length scale associated with
flow disturbance, in this case the layer thickness. ( b) Shadow images of the top and side views of a shear layer–droplet interaction. Panel
adapted with permission from Xu et al. (2022) . (c) Droplet–wake interaction with the wake having a flow deficit U′
" and width f.
(d) Shadow images of the aerobreakup of tandem droplets, with wake effects visible on the trailing droplet breakup. Panel adapted with
permission from Wang et al. (2021). (e) Droplet breakup in unsteady turbulent flows, with timescale tf and the eddies spanning f. tres
represents the droplet response time. ( f ) Laser-induced fluorescence images of the aerobreakup of droplets in a turbulent gas stream.
Panel adapted with permission from Zhao et al. (2019) . (g) Eddy–droplet interaction during aerobreakup in turbulent flows. Panel
adapted from T ang et al. (2025)(CC BY 4.0 ).
two-way coupling. A similar nonuniform but symmetric imposition is expected in droplet aero-
breakup in the wake of another neighboring droplet (Figure 7c). The deficit in the free stream flow
field modulates the effective We and a radial velocity gradient confines the span of aerobreakup
(similar to longitudinal sheet formation in the shear). Hence, the aerobreakup in the trailing
droplet spans a smaller region, as illustrated in Figure 7 d (Wang et al. 2021 ). The asymmetric
positioning of the second droplet within the wake reveals even more intriguing characteristics
(Theofanous et al. 2007 ). For turbulent or unsteady cases, the flow structures are represented by
eddies (see Figure 7 e). These pseudodiscrete flow elements can be associated with a strength
(say circulation), length scale, and turnaround time. Figure 7 f,g depicts altered aerobreakup
modes with modulations imposed by eddies in the presence of turbulent upstream flow ( Zhao
et al. 2019 ). Such modulations with unique breakup modes are observed in swirling flows as
well ( Rajamanickam & Basu 2017a ,b; Kirar et al. 2022 ) and are relevant to numerous industrial
processes.
Earlier, we introduced a deformation length scale  , which, when compared with the parent
droplet size, offers valuable insights. Similarly, we can define a length scale  f characteristic to the
flow nonuniformity and compare it with d0, indicating the span of the nonuniformity. As illustrated
in Figure 7, for shear and wake flow, this scales with the width of the shear layer and with eddy sizes
for a turbulent flow. For  f=d0≫ 1, the flow is uniform locally, and for  f=d0≪ 1, the droplet as a
whole might not be able to sense the nonuniformity; hence, the global deformations are virtually
98 Rao  Basu

<!-- PDF_PAGE: 17 -->

Downloaded from www.annualreviews.org.  Guest (guest) IP:  103.151.173.209 On: Sat, 29 Aug 2026 07:53:40
FL58_Art04_Basu ARjats.cls November 28, 2025 12:3
unaffected. However, there is a possibility that local deformations  (subsecondary processes) will
be affected if  f=  1. Thus, comparing length scales is an effective way to make preliminary
predictions.
4.2. Unsteady Effects: Shocks and Blasts
Unsteadiness in the upstream flow is another important factor for imposing additional nonlin-
earity. A uniform but unsteady upstream flow is still an open problem, and very few studies have
investigated transient dynamics. An unsteady canonical case of the shear-driven wave dynamics
resulting from oscillating upstream flow was modeled to estimate the parametric instability ( Kelly
1965). Recently, this analysis was expanded to include a decaying flow field ( Shen & Bourouiba
2023); however, a dispersion relation or a similar evolution metric is yet to be estimated.
The turbulent flow would involve an underlying energetic spatiotemporal signature that is
expected to modulate breakup ( Ni 2024 , T ang et al. 2025). A case study in primary atomization
involving a mixing layer where a periodically pulsed jet was introduced to the air upstream ( Matas
et al. 2015 ) demonstrated the same peak in the frequency spectrum of interfacial waves. These
perturbations or eddies should, however, be energetic enough to induce or modulate breakup. This
unsteadiness is marked by a characteristic timescale that can be impulsive as well. The timescales
associated with inertial droplet deformation or wave mechanisms should be compatible with the
flow fluctuation for the droplet to respond to this disturbance. In some cases, one can even expect
resonance to occur.
Shock waves are a special category of impulsive flow perturbations that typically occur in high-
speed flows. An ideal shock will exhibit a steady flow behind it, albeit with a jump in velocity.
The ramp-up in flow properties across a shock is almost instantaneous; i.e., the characteristic
timescales for the jump are very small (see Figure 8 a,b). Hence, the droplet interface is barely
affected by shock impulse alone, as shown in Figure 8 c,d. The aerobreakup is mostly due to the
induced flow behaving like a step function with similar dynamics, as discussed earlier. The wave
dynamics of shock propagation through the droplet can lead to regions of extreme low pressure
inside the liquid, due to shock transmission, reflection, and focusing of the expansion fan ( Xiong
et al. 2024 ) (Figure 8d). However, this phenomenon is dominant only for certain fluid pairs and
shock strengths ( Sembian et al. 2016 ) and is not considered further. The compressibility effects
must also be accounted for in such flows. There is a class of unsteady shock waves, called blast
waves, which exhibit approximately an exponential decay in strength of the shock as well as the
induced gas motion. The blast wave can be characterized by a timescale representing the decay of
a
(1)
(2)
(3)
b
 c
Shock
d
Incident
wave
Reflected
wave
Mach stem
+Uε(r, t)'
U0(r)
Ms
Pa
tt(3)
b t(3)
f
t(2)
b
P
(MPa)
0.10
0.57
1.04
1.51
1.98
Figure 8
(a) Droplet interacting with an impulsive flow such as a shock wave. ( b) T ypical impulse pressure profile and associated timescales:
(1) shock wave, (2) blast wave, and (3) shock or blast wave issued from a nozzle opening. ( c) Schlieren image depicting a shock wave
interacting with a droplet over a very short timescale. ( d) Numerical simulation depicting the pressure distribution around a droplet
during a shock wave interaction. Panel d adapted with permission from Xiong et al. (2024) .
www.annualreviews.org  Secondary Atomization at Extreme Conditions 99

<!-- PDF_PAGE: 18 -->

Downloaded from www.annualreviews.org.  Guest (guest) IP:  103.151.173.209 On: Sat, 29 Aug 2026 07:53:40
FL58_Art04_Basu ARjats.cls November 28, 2025 12:3
the pressure pulse to ambient levels [ t (2)
b in Figure 8b], measured at a fixed location. The droplet
is affected if this timescale is comparable to its response time. The breakup occurs beyond a cer-
tain characteristic energy. However, there is another possible configuration where a lag effect is
introduced between the blast pulse and induced bulk flow when the blast exits the open end of a
shock tube or nozzle. The blast wave propagates almost independently with a very short time sig-
nature due to an added degree of freedom outside the tube exit. However, the induced flow faces
additional viscous resistance from the surrounding stagnant fluid, leading to roll up and formation
of a compressible starting jet/vortex ring ( V adlamudi et al. 2024). This jet front appears as a sec-
ond peak in the pressure signal [ t (3)
b in Figure 8 b]. When a droplet resides outside the tube exit,
the first disturbance pulse associated with the blast wave is very short compared to its response
times (the droplet is barely affected). Subsequently, the second pulse associated with a compatible
flow timescale [tf(3) in Figure 8b] actually disrupts and fragments the droplet. This flow is locally
uniform, considering the droplet to be small but unsteady. Hence, the breakup dynamics will be
altered if this decay timescale is of the same order as the droplet breakup time.
5. BREAKUP IN COMPRESSIBLE FLOW FIELDS
Compressible effects become increasingly apparent with increase in airflow velocities and can-
not be neglected beyond a certain threshold. Ma is a definitive representation of these effects,
as discussed earlier, where we discussed the extension of the regime map into We–Oh–Ma space
(Figure 1 c). The compressible effects establish additional modes of nonuniformity around the
droplet. Figure 9a is an exemplary case of supersonic flow (MaD 3), where a standing bow shock
ahead of the droplet modulates the pressure (and density) distribution, hence, the deformation
dynamics (Xiao et al. 2017 ).
The droplet on the verge of deformation can be assumed as a solid sphere. The pressure dis-
tribution and local shear imposed over this seemingly solid surface represent the initial condition
for aerobreakup. The distribution is illustrated in Figure 9b,c for different upstream Ma ( Nagata
et al. 2020 ). In Figure 9 b, the maximum shear occurs at D 60°–80°, where the KHI is usually
observed. In addition, the pressure is highest at the forward stagnation point, imposing a defor-
mation into an oblate shape. These effects combine to generate a cupcake shape. Compressibility
affects these distributions, along with shape modulation. The flow mechanics associated with the
gas phase are fundamentally altered when the flow transits from subsonic (Ma < 1) to supersonic
(Ma > 1). A detached bow shock forms ahead of the droplet, the curvature of which modulates
the external nonuniform flow over the surface.
The compressibility effects also alter the BL dynamics and momentum transfer to the inter-
face. For shear instabilities, Nayfeh & Saric (1971 , 1973) presented a nonlinear analysis, showing
that compressibility-induced pressure perturbations in the supersonic gas phase are typically not
in sync with the perturbed liquid interface. This out-of-phase effect suppresses wave growth over
the interface for these nonlinear KHIs and is expected to dampen the shear-induced breakup
in the supersonic regime ( Chawla 1975 ). However, in the subsonic regimes, the compressibility
effects tend to enhance the growth rates as Ma is increased, with extremity observed in the tran-
sonic regime ( Li & Kelly 1992 ). Thus, compressibility switches its nature from destabilizing to
stabilizing when gas phase flow transitions from subsonic to supersonic.
Compressibility effects also dampen RTI. Using LSA, Livescu (2004) showed that the com-
pressibility (for a given ratio of specific heats  ) suppressed the growth rates, with a minimal effect
of viscosity and surface tension on the most unstable mode, especially at high Atwood numbers
AtD la
lCa
. The compressible effects are pronounced at significant accelerations, affecting lower
wavenumbers. Additionally, the background stratification significantly modulates this behavior. In
100 Rao  Basu

<!-- PDF_PAGE: 19 -->

Downloaded from www.annualreviews.org.  Guest (guest) IP:  103.151.173.209 On: Sat, 29 Aug 2026 07:53:40
FL58_Art04_Basu ARjats.cls November 28, 2025 12:3
Folding of the liquid sheet
Ligaments connected by
thin membranes
Bow
shock
a b c
d
e
f
Constant We  (~1,000)
-
3    2    1
Ligament
extension
Bags and
rims
Sheet
extension
Bow shock
Modified
airflow
0 30 60 90 120 150 180
0.00
0.05
0.10
0.15
θ
θ
Cf Cp
P
−0.5
0.0
0.5
1.0
1.5
2.0
T = 0.48T = 0.48 T = 0.53T = 0.53 T = 0.59T = 0.59 T = 0.65T = 0.65 T = 0.69T = 0.69
We'
ρ1
ρ2
ρ3
ps /p0
ρ∞
Ma∞ ≈ 1.2
Ma∞ = 3
Ma∞ = 3 Ma∞ = 0.8Ma = 0.8
Ma = 2
Ma∞ 0.3 0.83 1.2
1.0
0.8
0.6
0.4
0.2
0
Oblique
shock
Oblique
shock
Less flatteningLess flattening
Kinks shifted downstreamKinks shifted downstream
LigamentsLigaments
Larger fragments over
narrower spread
Larger fragments over
narrower spread
Normal shockNormal shock
Multiple bagsMultiple bags
Separation zoneSeparation zone
Liquid sheetLiquid sheet
Figure 9
(a) Flow field around a deforming droplet in a supersonic air stream at Mach number (Ma) D3. (b) Coefficient of friction Cf and
coefficient of pressure Cp around a solid sphere at different Ma. ( c) Pressure distribution around a solid sphere at different Ma.
(d) Schematic illustrating droplet breakup in a supersonic flow field in the presence of a bow shock, depicting extensional features.
(e) Shadow image of droplet breakup in a supersonic flow field. ( f ) Effect of Ma on droplet aerobreakup at constant Weber number
(We)1,000. The length scale of images in the last row is half of that in the first three rows. Panel a adapted with permission from Xiao
et al. (2017). Panels b and c adapted from Nagata et al. (2020) (CC BY 4.0 ). Panels e and f adapted from Wang et al. (2020) (CC BY 4.0 ).
the case of a droplet in a compressible flow field, the flow at the forward-facing segment can be per-
ceived as a stagnation point flow, stratified normal to the interface. For supersonic flows, a detached
bow shock appears, presenting even stronger gradients. Depending on the nature of this stratifi-
cation of density, pressure, temperature, or entropy, the RTI mechanism can be either enhanced
or suppressed ( Wieland et al. 2017 , Luo & Wang 2021 ). The wave growth involves a baroclinic
torque production mechanism and is influenced by the background gradients. The compressible
flow at the droplet front presents negative gradients of density, pressure, and temperature along
a normal pointing outward (upstream) on the droplet interface ( Xiao et al. 2017 ), modulating the
RTI mechanism in a sense that is yet to be explored. The curvature effects further complicate
the dynamics. A more holistic model is required, especially in the context of aerobreakup where
At 1 and the acceleration is very large (impulsive and unsteady).
The exact interfacial dynamics accounting for compressibility have not been pursued experi-
mentally, but the droplet breakup event in high Ma flows supports this prediction of a suppression
mechanism (Dinh et al. 2003, Theofanous et al. 2004, Kim & Hermanson 2012, Wang et al. 2020),
as depicted in Figure 9d–f. At higher Ma with moderate We ( 103) in the SIE regime, the periph-
ery of the cupcake shape conforms to a sheet topology. These sheets undergo a folding process and
www.annualreviews.org  Secondary Atomization at Extreme Conditions 101

<!-- PDF_PAGE: 20 -->

Downloaded from www.annualreviews.org.  Guest (guest) IP:  103.151.173.209 On: Sat, 29 Aug 2026 07:53:40
FL58_Art04_Basu ARjats.cls November 28, 2025 12:3
are dragged in the flow direction, as shown in Figure 9d,e, causing extension ( Wang et al. 2020).
This extensional process is more prominent compared to aerobreakup in the incompressible coun-
terpart. This sheet supports the formation of bags bound by rims or ligaments, reminiscent of
multibag or multimode breakup. These eventually undergo a ligament-mediated breakup mech-
anism. If Ma is increased, preserving the We, difference in breakup morphology is observed in
Figure 9 f, with more ligament-like features that exhibit viscous-like effects, even for very small
Oh. The elongation is augmented along the flow direction, while the cross-directional spread is
suppressed. At lower We (high Ma), pulling modes are supported rather than the usual bag forma-
tion (Dinh et al. 2003 , Theofanous et al. 2004 ) (see Figure 1 c). The events are less catastrophic
in this regime, even though the flow velocities are supersonic.
A higher We flow at elevated Ma presents more extreme impositions. Earlier studies spanned
this regime, imposing severe conditions through shock waves having shock Ma as high as 12 with
We O(105) (Nicholls & Ranger 1969 , Reinecke & McKay 1969 , Hébert et al. 2019 , Salauddin
et al. 2023 , Virot et al. 2023 ). The intense stripping reappears over and above the restricted
transverse spread and elongational behavior associated with compressible effects. The resultant
topology resembles a rugged teardrop or tadpole shape ( Salauddin et al. 2023 ). The precise
mechanism underlying this phenomenon remains speculative, and shear stripping alone is insuf-
ficient to account for the observed behavior ( Dworzanczyk et al. 2025 ). A rigorous explanation
is necessary, including the large perturbation evolution in the nonlinear regime. Contrary to
the general notion, increasing flow velocities indefinitely will not guarantee a more catastrophic
breakup.
Additionally, the postshock thermodynamic conditions, including elevated temperatures and
pressures, induce compressive heating, droplet evaporation, and even chemical reactions with re-
active liquids like fuels ( T arey et al. 2024, V adlamudi et al. 2024, Song et al. 2025 ). This can also
be imposed via external heating or pressurization emulating a combustion chamber, potentially
reaching the transcritical threshold (Boyd & Jarrahbashi 2021). The phase change and accompany-
ing vapor layer interaction with the gas phase flow affect the interfacial waves and wake structures
in a coupled fashion. The evaporative flux is a stabilizing agent ( Hsieh 1978 , Boyd et al. 2024 ).
Furthermore, the timescales associated with heat and mass transfer should be compatible with
the droplet (or wave mechanism) response time for the effect to be prominent. Compressibility
also affects the evaporation and dispersion of daughter droplets ( Duke-Walker et al. 2021 , Virot
et al. 2023 , Capecelatro & Wagner 2024 ). The extremities featuring heat transfer, phase change,
combustion, detonation, and hypersonic flows remain areas of active research.
6. DAUGHTER DROPLET SIZE DISTRIBUTION AND SELF-SIMILARITY
The outcome of practical interest expected from any secondary atomization event is daughter
droplet generation and control over associated parameters, such as size distribution, number
density, and velocities. Higher We aerobreakup leads to extremely small, high-velocity droplets.
However, a few studies managed to measure the size distributions that closely aligned with a log-
normal or gamma distribution ( Guildenbecher et al. 2017 , Kamiya et al. 2022 , Sharma et al.
2023b). The droplet generation mechanism is not typically straightforward since droplets are
generated continuously with wave cascades over different undulations occurring simultaneously.
Internal redistribution of fluid to different parts of the droplet, as the liquid mass is continuously
stripped away, is necessary to assess the favored wave mechanisms. At lower We, there is a preferen-
tial redistribution of liquid to a few particular modes (say rim and bag film in bag breakup), leading
to multimodal breakup and a broader size distribution ( Jackiw & Ashgriz 2021 , 2022; Kulkarni
et al. 2023 ). This effect can be modeled to predict the distribution even in extended complicated
102 Rao  Basu

<!-- PDF_PAGE: 21 -->

Downloaded from www.annualreviews.org.  Guest (guest) IP:  103.151.173.209 On: Sat, 29 Aug 2026 07:53:40
FL58_Art04_Basu ARjats.cls November 28, 2025 12:3
a b
c d e
0 40 80 120 160 200 240 280 320
0.000
0.006
0.012
0.018
0.024
0.030 We ~ 900 We ~ 900 We ~ 900 We ~ 900
0.000
0.006
0.012
0.018
0.024
0.000
0.008
0.016
0.024
0.032
0 50 100 150 200 250 300 350 400
0.000
0.008
0.016
0.024
0.032
0 50 100 150 200 250 300 350 400 0 50 100 150 200 250 300 350 400
0 5 1510 20 25
0.00001
0.0001
0.001
0.01
0.1
1
10
Normalized PDF
d/<d>
 We
900
2,000
4,000
900 (T1)
900 (T2)
900 (T3)
2,000 (T1)
2,000 (T2)
2,000 (T3)
4,000 (T1)
4,000 (T2)
4,000 (T3)
 Log-normal
 Compound gamma (m = 3, n = 4)
PDF (1//uni03BCm)PDF (1//uni03BCm)PDF (1//uni03BCm)
PDF (1//uni03BCm)PDF (1//uni03BCm)PDF (1//uni03BCm)
d (/uni03BCm) d (/uni03BCm) d (/uni03BCm) d (/uni03BCm)
dc
0.000
0.008
0.016
0.024
0.032
0.040 We ~ 2,000 We ~ 2,000 We ~ 2,000 We ~ 2,000
0.000
0.008
0.016
0.024
0.032
0.040
0.048
We ~ 4,000 We ~ 4,000 We ~ 4,000 We ~ 4,000
τb = 0 to 0.33 (T1) τb = 0.33 to 0.67 (T2) τb = 0.67 to 1 (T3)
t~0 (ms)
2 mm
2 mm
2 mm
Figure 10
(a) Droplet size distribution showing the number PDFs for fragmentation at different We flows. ( b) T emporal variation of the PDFs
where the breakup event is split into three buckets (T1–T3), illustrating the transient nature of aerobreakup, with  b the time/total
breakup time. (c) Normalized PDFs along with log-normal and compound gamma function fit, depicting self-similar behavior.
(d) Shadow image of a ligament breakup illustrating the droplet generation mechanism. ( e) Schematic of a ligament composed of blobs
with sizes dc matching the local ligament diameter. Abbreviation: PDF , probability distribution function. Panel a and b adapted from
Sharma et al. (2023b) . Panel d adapted with permission from Villermaux et al. (2004). Panels c and e adapted with permission from Rao
& Basu (2025) .
spray systems ( Jackiw & Ashgriz 2023). However, in a catastrophic breakup, it is expected that the
emergence of different cascades or wave mechanisms will be more random, leading to unimodal
distributions (aggregation of processes), as depicted in Figure 10a–c.
A log-normal distribution was observed for blast wave–induced unsteady atomization ( Sharma
et al. 2023b ), as depicted in Figure 10 a. V ery fine droplets are generated at these high We,
where increasing We shifts the distribution toward even smaller droplets. However, the breakup
duration can be bucketed temporally (equal breakup periods T1–T3), as depicted in Figure 10b.
The primary factors contributing to this unsteadiness include decaying airflow and the transient
wave cascade mechanism that continuously generates daughter droplets from the evolving
(deforming and fragmenting) parent droplet. Additionally, the size-dependent dispersion of the
droplets affects their arrival at the measurement zone in the far downstream region. These effects
are evident through early detection of smaller droplets due to higher initial We and lower mass
(inertia), allowing them to be dispersed more rapidly in the measurement area. However, when
www.annualreviews.org  Secondary Atomization at Extreme Conditions 103

<!-- PDF_PAGE: 22 -->

Downloaded from www.annualreviews.org.  Guest (guest) IP:  103.151.173.209 On: Sat, 29 Aug 2026 07:53:40
FL58_Art04_Basu ARjats.cls November 28, 2025 12:3
normalized with the average diameter ⟨d⟩, the distributions overlap, indicating a common un-
derlying mechanism and a self-similar behavior in Figure 10c (Rao & Basu 2025 ). A log-normal
and a compound gamma distribution fit ( Kooij et al. 2018 ) agree, with deviation at the tail (for
d=⟨d⟩ > 10). This may be attributed to decaying airflow and coalescence, which is typically
promoted in the vortical region near the droplet equator, where the dense mist (large number
concentration) is generated through stripping ( Nykteri & Gavaises 2021 ).
The nature of distribution can be fundamentally predicted by examining a random sequen-
tial splitting of the parent droplet. This was assessed considering the maximum-likelihood or
maximum-entropy formalism, drawing inspiration from turbulent cascades and statistical ther-
modynamics ( Sellens & Brzustowski 1986 , Cousin & Dumouchel 1996 , Villermaux 2007 , Kuo
& T rujillo 2022). These approaches involve discrete events where a droplet splits randomly into
smaller droplets, and each of them splits again until the final droplets reach a cutoff size based
on the threshold We. The aerobreakup is mediated by the cascading waves, with the drops be-
ing generated continuously at the termination of each cascade. This viewpoint of droplet breakup
is statistically similar to random splitting (we observe similar distributions) but fundamentally
different in the sense that the events are more continuous than discrete ( Janssen & Meijer
1993).
SIE depicts stripping of liquid as daughter droplets from the parent drop through a ligament-
mediated mechanism, as illustrated in Figure 10d. The corrugated ligament can be modeled con-
sidering it as discrete units (blobs) that correspond to the local ligament diameter (seeFigure 10e),
where the splitting is governed by RPI ( Villermaux et al. 2004 , Keshavarz et al. 2016 , Pal et al.
2024). The shape factor of corrugations on isolated ligaments significantly influences the droplet
size distribution, as illustrated for primary atomization processes. A similar exposition can be made
to predict the subsecondary breakups. The parameter in the compound gamma distribution fit
(Figure 10c) closely follows the limiting values, estimated from the ligament shape factor ( Rao &
Basu 2025). The earlier approaches, involving idealized splitting, need to be extended to the wave
cascade approach proposed here ( Rimbert & Castanet 2011 ). Each cascade event can be modeled
as an equivalent discrete splitting sequence. The distribution parameters can then be predicted
in a nondimensional space. T o support these studies, traditional sizing approaches are inadequate
(T ropea 2011), necessitating the development of the new class of techniques for measurement
(Erinin et al. 2023, Rao et al. 2024) and visualization ( Aliseda & Heindel 2021 ). Machine learning
also offers a promising approach to predict dispersion statistics ( T raverso et al. 2023, Cundy et al.
2024).
SUMMARY POINTS
1. Droplet aerobreakup depicts a prominent wave-mediated mechanism fundamentally
associated with Kelvin–Helmholtz instability (KHI), Rayleigh–T aylor instability, and
Rayleigh–Plateau instability, manifesting as complex waves in shear-induced entrain-
ment (SIE) modes under extreme conditions.
2. A scale-based compatibility criterion predicts the breakup mode transition from
Rayleigh–T aylor piercing to SIE, assessing the available space for the fastest growing
unstable KHI wave to grow.
3. Multiscale deformations ranging from global droplet level morphing to sequential local
deformations associated with wave mechanisms constitute a nonlinear wave cascade, with
coupled modulations with the surrounding gas phase.
104 Rao  Basu

<!-- PDF_PAGE: 23 -->

Downloaded from www.annualreviews.org.  Guest (guest) IP:  103.151.173.209 On: Sat, 29 Aug 2026 07:53:40
FL58_Art04_Basu ARjats.cls November 28, 2025 12:3
4. The cascade depicts recurrence, and the associated timescale relates to the growth rate
of these waves. It terminates eventually with a ligament-mediated mechanism, with each
local undulation as a precursor.
5. For nonideal flow fields, the relative scale for the nonuniformity (perturbation length
scale) and unsteadiness (perturbation timescale) should be compatible with the global
deformations (droplet resonant modes) or local deformations (dominant wave modes)
for aerobreakup to be affected.
6. The compressibility effect modulates the flow field, which promotes elongated fea-
tures like ligaments and sheets stretching in the flow direction, suppressing the breakup
intensity.
FUTURE ISSUES
1. A theoretical framework consisting of nonlinear stability analysis is necessary for a deeper
understanding of the complex wave cascade.
2. A model for droplet internal flow, assimilating the overall deformation and liquid re-
distribution during the stripping process, is essential to recognize the feeding rates
associated with the cascade processes. This treatment of the formation and evolution of
various topological components (global and local) will enable a systematic representation
of the dynamics.
3. A possible self-similar dynamics for the subsecondary breakup of the local undulations
is a viable fractal mechanism that deserves to be explored.
4. The role of imposed complexities that ultimately manifest as nonuniformity, un-
steadiness, compressibility, or other thermodynamic impositions is still required to be
systematically studied.
5. Experiments with better visualization strategies at high spatiotemporal resolutions, such
as X-rays, are needed to accurately quantify the interfacial dynamics.
DISCLOSURE STATEMENT
The authors are not aware of any affiliations, memberships, funding, or financial holdings that
might be perceived as affecting the objectivity of this review.
ACKNOWLEDGMENTS
We sincerely thank Dr. Shubham Sharma for insightful discussions and Professor Cameron
T ropea for his valuable feedback. We also thank Akhil Aravind for his assistance. S.J.R.
acknowledges the support received from the Prime Minister’ s Research Fellowship.
LITERATURE CITED
Agbaglah GG. 2021. Breakup of thin liquid sheets through hole–hole and hole–rim merging. J. Fluid Mech.
911:A23
Aliseda A, Heindel TJ. 2021. X-ray flow visualization in multiphase flows. Annu. Rev. Fluid Mech. 53:543–67
www.annualreviews.org  Secondary Atomization at Extreme Conditions 105

<!-- PDF_PAGE: 24 -->

Downloaded from www.annualreviews.org.  Guest (guest) IP:  103.151.173.209 On: Sat, 29 Aug 2026 07:53:40
FL58_Art04_Basu ARjats.cls November 28, 2025 12:3
Behzad M, Ashgriz N. 2014. The role of density discontinuity in the inviscid instability of two-phase parallel
flows. Phys. Fluids 26(2):024107
Behzad M, Ashgriz N, Mashayek A. 2015. Azimuthal shear instability of a liquid jet injected into a gaseous
cross-flow. J. Fluid Mech. 767:146–72
Boeck T, Zaleski S. 2005. Viscous versus inviscid instability of two-phase mixing layers with continuous
velocity profile. Phys. Fluids 17(3):032106
Bourouiba L. 2021. The fluid dynamics of disease transmission. Annu. Rev. Fluid Mech. 53:473–508
Boyd B, Jarrahbashi D. 2021. Numerical study of the transcritical shock-droplet interaction. Phys. Rev. Fluids
6(11):113601
Boyd B, Becker S, Ling Y. 2024. Impact of vaporization on drop aerobreakup. J. Fluid Mech. 1000:A33
Capecelatro J, Wagner JL. 2024. Gas–particle dynamics in high-speed flows.Annu. Rev. Fluid Mech.56:379–403
Chandra NK, Sharma S, Basu S, Kumar A. 2023. Shock-induced aerobreakup of a polymeric droplet. J. Fluid
Mech. 965:A1
Chandra NK, Sharma S, Basu S, Kumar A. 2024a. Aerodynamic bag breakup of a polymeric droplet. Phys. Rev.
Fluids 9(11):113303
Chandra NK, Sharma S, Basu S, Kumar A. 2024b. Elasticity affects the shock-induced aerobreakup of a
polymeric droplet. Exp. Fluids 65(5):75
Chawla TC. 1975. The Kelvin-Helmholtz instability of the gas-liquid interface of a sonic gas jet submerged
in a liquid. J. Fluid Mech. 67(3):513–37
Cousin J, Dumouchel C. 1996. Coupling of classical linear theory and maximum entropy formalism
for prediction of drop size distribution in sprays: application to pressure-swirl atomizers. At. Sprays
6(5):601–22
Cundy C, Mirjalili S, Laurent C, Ermon S, Iaccarino G, Mani A. 2024. A physics-informed machine learning
model for the prediction of drop breakup in two-phase flows. Int. J. Multiphase Flow 180:104934
Deike L. 2022. Mass transfer at the ocean–atmosphere interface: the role of wave breaking, droplets, and
bubbles. Annu. Rev. Fluid Mech. 54:191–224
Dinh N, Li GJ, Theofanous T . 2003. An investigation of droplet breakup in a high Mach, low Weber number
regime. In 41st Aerospace Sciences Meeting and Exhibit . AIAA
Dorschner B, Biasiori-Poulanges L, Schmidmayer K, El-Rabii H, Colonius T . 2020. On the formation and
recurrent shedding of ligaments in droplet aerobreakup. J. Fluid Mech. 904:A20
Drazin PG, Reid WH. 2004. Hydrodynamic Stability. Cambridge University Press
Duke-Walker V, Maxon WC, Almuhna SR, McFarland JA. 2021. Evaporation and breakup effects in the
shock-driven multiphase instability. J. Fluid Mech. 908:A13
Dworzanczyk AR, Viqueira-Moreira M, Langhorn JD, Libeau MA, Brehm C, Parziale NJ. 2025. On
aerobreakup in the stagnation region of high-Mach-number flow over a bluff body.J. Fluid Mech.1002:A1
Eggers J, Villermaux E. 2008. Physics of liquid jets. Rep. Prog. Phys. 71(3):036601
Erinin MA, Néel B, Mazzatenta MT, Duncan JH, Deike L. 2023. Comparison between shadow imaging and
in-line holography for measuring droplet size distributions. Exp. Fluids 64(5):96
Funada T, Joseph DD. 2001. Viscous potential flow analysis of Kelvin–Helmholtz instability in a channel.
J. Fluid Mech. 445:263–83
Gorokhovski M, Herrmann M. 2008. Modeling primary atomization. Annu. Rev. Fluid Mech. 40:343–66
Guildenbecher DR, Gao J, Chen J, Sojka PE. 2017. Characterization of drop aerodynamic fragmentation in the
bag and sheet-thinning regimes by crossed-beam, two-view, digital in-line holography. Int. J. Multiphase
Flow 94:107–22
Guildenbecher DR, López-Rivera C, Sojka PE. 2009. Secondary atomization. Exp. Fluids 46(3):371–402
Hanson AR, Domich EG, Adams HS. 1963. Shock tube investigation of the breakup of drops by air blasts.
Phys. Fluids 6(8):1070–80
Hébert D, Rullier J-L, Chevalier J-M, Bertron I, Lescoute E, et al. 2019. Investigation of mechanisms leading
to water drop breakup at Mach 4.4 and Weber numbers above 105. SN Appl. Sci. 2(1):69
Hinze JO. 1955. Fundamentals of the hydrodynamic mechanism of splitting in dispersion processes. AIChE J.
1(3):289–95
Hoepffner J, Blumenthal R, Zaleski S. 2011. Self-similar wave produced by local perturbation of the Kelvin-
Helmholtz shear-layer instability. Phys. Rev. Lett. 106(10):104502
106 Rao  Basu

<!-- PDF_PAGE: 25 -->

Downloaded from www.annualreviews.org.  Guest (guest) IP:  103.151.173.209 On: Sat, 29 Aug 2026 07:53:40
FL58_Art04_Basu ARjats.cls November 28, 2025 12:3
Hsiang L-P, Faeth GM. 1992. Near-limit drop deformation and secondary breakup. Int. J. Multiphase Flow
18(5):635–52
Hsiang L-P, Faeth GM. 1995. Drop deformation and breakup due to shock wave and steady disturbances. Int.
J. Multiphase Flow 21(4):545–60
Hsieh DY. 1978. Interfacial stability with mass and heat transfer. Phys. Fluids 21(5):745–48
Jackiw IM, Ashgriz N. 2021. On aerodynamic droplet breakup. J. Fluid Mech. 913:A33
Jackiw IM, Ashgriz N. 2022. Prediction of the droplet size distribution in aerodynamic droplet breakup.
J. Fluid Mech. 940:A17
Jackiw IM, Ashgriz N. 2023. Aerodynamic droplet atomization model (ADAM). J. Fluid Mech. 958:A2
Jain M, Prakash RS, T omar G, Ravikrishna RV . 2015. Secondary breakup of a drop at moderate Weber
numbers. Proc. R. Soc. A 471(2177):20140930
Jalaal M, Mehravaran K. 2014. T ransient growth of droplet instabilities in a stream. Phys. Fluids 26(1):012101
Janssen JMH, Meijer HEH. 1993. Droplet breakup mechanisms: stepwise equilibrium versus transient
dispersion. J. Rheol. 37(4):597–608
Jerome JJS, Marty S, Matas J-P, Zaleski S, Hoepffner J. 2013. V ortices catapult droplets in atomization. Phys.
Fluids 25(11):112109
Jones TJ, Reynolds CD, Boothroyd SC. 2019. Fluid dynamic induced break-up during volcanic eruptions.
Nat. Commun. 10(1):3828
Joseph DD, Belanger J, Beavers GS. 1999. Breakup of a liquid drop suddenly exposed to a high-speed airstream.
Int. J. Multiphase Flow 25(6):1263–303
Kamiya T, Asahara M, Y ada T, Mizuno K, Miyasaka T . 2022. Study on characteristics of fragment size
distribution generated via droplet breakup by high-speed gas flow. Phys. Fluids 34(1):012118
Kelly RE. 1965. The stability of an unsteady Kelvin–Helmholtz flow. J. Fluid Mech. 22(3):547–60
Keshavarz B, Houze EC, Moore JR, Koerner MR, McKinley GH. 2016. Ligament mediated fragmentation
of viscoelastic liquids. Phys. Rev. Lett. 117(15):154502
Kim Y, Hermanson JC. 2012. Breakup and vaporization of droplets under locally supersonic conditions. Phys.
Fluids 24(7):076102
Kirar PK, Soni SK, Kolhe PS, Sahu KC. 2022. An experimental investigation of droplet morphology in swirl
flow. J. Fluid Mech. 938:A6
Kooij S, Sijs R, Denn MM, Villermaux E, Bonn D. 2018. What determines the drop size in sprays? Phys. Rev.
X 8(3):031019
Krzeczkowski SA. 1980. Measurement of liquid droplet disintegration mechanisms. Int. J. Multiphase Flow
6(3):227–39
Kulkarni V, Shirdade N, Rodrigues N, Radhakrishna V, Sojka PE. 2023. On interdependence of instabilities
and average drop sizes in bag breakup. Appl. Phys. Lett. 123(2):024101
Kuo C-W, T rujillo MF . 2022. A maximum entropy formalism model for the breakup of a droplet. Phys. Fluids
34(1):013315
Lane WR. 1951. Shatter of drops in streams of air. Ind. Eng. Chem. 43(6):1312–17
Lasheras JC, Hopfinger EJ. 2000. Liquid jet instability and atomization in a coaxial gas stream. Annu. Rev.
Fluid Mech. 32:275–308
Legendre D. 2024. Fluid dynamics of airtanker firefighting. Annu. Rev. Fluid Mech. 56:577–603
Li HS, Kelly RE. 1992. The instability of a liquid jet in a compressible airstream. Phys. Fluids 4(10):2162–68
Lin SP, Reitz RD. 1998. Drop and spray formation from a liquid jet. Annu. Rev. Fluid Mech. 30:85–105
Ling Y, Fuster D, Zaleski S, T ryggvason G. 2017. Spray formation in a quasiplanar gas-liquid mixing layer at
moderate density ratios: a numerical closeup. Phys. Rev. Fluids 2(1):014005
Livescu D. 2004. Compressibility effects on the Rayleigh–T aylor instability growth between immiscible fluids.
Phys. Fluids 16(1):118–27
Loparev VP . 1975. Experimental investigation of the atomization of drops of liquid under conditions of a
gradual rise in the external forces. Fluid Dyn. 10(3):518–21
Luo T, Wang J. 2021. Effects of Atwood number and stratification parameter on compressible multi-mode
Rayleigh–T aylor instability.Phys. Fluids 33(11):115111
Marmottant P, Villermaux E. 2004. On spray formation. J. Fluid Mech. 498:73–111
www.annualreviews.org  Secondary Atomization at Extreme Conditions 107

<!-- PDF_PAGE: 26 -->

Downloaded from www.annualreviews.org.  Guest (guest) IP:  103.151.173.209 On: Sat, 29 Aug 2026 07:53:40
FL58_Art04_Basu ARjats.cls November 28, 2025 12:3
Matas J-P, Marty S, Dem MS, Cartellier A. 2015. Influence of gas turbulence on the instability of an air-water
mixing layer. Phys. Rev. Lett. 115(7):074501
Mates SP, Settles GS. 2005. A study of liquid metal atomization using close-coupled nozzles. At. Sprays
15(1):19–60
Meng JC, Colonius T . 2015. Numerical simulations of the early stages of high-speed droplet breakup. Shock
W aves25(4):399–414
Mikaelian KO. 1996. Rayleigh-T aylor instability in finite-thickness fluids with viscosity and surface tension.
Phys. Rev. E 54(4):3676–80
Mizuno K, Y ada T, Kamiya T, Asahara M, Miyasaka T . 2022. Deformation behavior of liquid droplet in shock-
induced atomization. Int. J. Multiphase Flow 155:104141
Nagata T, Nonomura T, T akahashi S, Fukuda K. 2020. Direct numerical simulation of subsonic, transonic
and supersonic flow over an isolated sphere up to a Reynolds number of 1000. J. Fluid Mech. 904:A36
Nayfeh AH, Saric WS. 1971. Non-linear Kelvin–Helmholtz instability. J. Fluid Mech. 46(2):209–31
Nayfeh AH, Saric WS. 1973. Nonlinear stability of a liquid film adjacent to a supersonic stream. J. Fluid Mech.
58(1):39–51
Néel B, Lhuissier H, Villermaux E. 2020. ‘Fines’ from the collision of liquid rims. J. Fluid Mech. 893:A16
Néel B, Villermaux E. 2018. The spontaneous puncture of thick liquid films. J. Fluid Mech. 838:192–221
Ni R. 2024. Deformation and breakup of bubbles and drops in turbulence. Annu. Rev. Fluid Mech. 56:319–47
Nicholls JA, Ranger AA. 1969. Aerodynamic shattering of liquid drops. AIAA J. 7(2):285–90
Nykteri G, Gavaises M. 2021. Droplet aerobreakup under the shear-induced entrainment regime using a
multiscale two-fluid approach. Phys. Rev. Fluids 6(8):084304
Obenauf DG, Sojka PE. 2021. Theoretical deformation modeling and drop size prediction in the multimode
breakup regime. Phys. Fluids 33(9):092113
Opfer L, Roisman IV, V enzmer J, Klostermann M, T ropea C. 2014. Droplet-air collision dynamics: evolution
of the film thickness. Phys. Rev. E 89(1):013023
Oshima I, Sou A. 2024. Air-blast atomization of a liquid film. J. Fluid Mech. 985:A36
Otto T, Rossi M, Boeck T . 2013. Viscous instability of a sheared liquid-gas interface: dependence on fluid
properties and basic velocity profile. Phys. Fluids 25(3):032103
Padrino JC, Joseph DD. 2006. Shear instability of a planar liquid jet immersed in a high speed gas stream . Master’ s
Thesis, University of Minnesota
Pal S, Pairetti C, Crialesi-Esposito M, Fuster D, Zaleski S. 2024. Statistics of drops generated from ensembles
of randomly corrugated ligaments. Phys. Fluids 36(11):112116
Pilch M, Erdman CA. 1987. Use of breakup time data and velocity history data to predict the maximum size of
stable fragments for acceleration-induced breakup of a liquid drop. Int. J. Multiphase Flow 13(6):741–57
Rajamanickam K, Basu S. 2017a. Insights into the dynamics of spray–swirl interactions. J. Fluid Mech. 810:82–
126
Rajamanickam K, Basu S. 2017b. On the dynamics of vortex–droplet interactions, dispersion and breakup in
a coaxial swirling flow. J. Fluid Mech. 827:572–613
Rao SJ, Basu S. 2025. Self-similar features in sub-secondary breakup of a droplet and ligament mediated
fragmentation under extreme conditions. Preprint, arXiv:2502.05976v2 [physics.flu-dyn]
Rao SJ, Sharma S, Basu S, T ropea C. 2024. Depth from defocus technique: a simple calibration-free approach
for dispersion size measurement. Exp. Fluids 65(4):55
Rayleigh L. 1880. On the stability, or instability, of certain fluid motions. Proc. Lond. Math. Soc. 11:57–70
Reinecke WG, McKay WL. 1969. Experiments on water drop breakup behind Mach 3 to 12 shocks. T ech. Rep.
SC-CR-70-6063, AVCO Government Products Group
Rimbert N, Castanet G. 2011. Crossover between Rayleigh-T aylor instability and turbulent cascading
atomization mechanism in the bag-breakup regime. Phys. Rev. E 84(1):016318
Salauddin S, Morales AJ, Hytovick R, Burke R, Malik V, et al. 2023. Detonation and shock-induced breakup
characteristics of RP-2 liquid droplets. Shock W aves33(3):191–203
Sellens RW, Brzustowski TA. 1986. A simplified prediction of droplet velocity distributions in a spray.Combust.
Flame 65(3):273–79
Sembian S, Liverts M, Tillmark N, Apazidis N. 2016. Plane shock wave interaction with a cylindrical water
column. Phys. Fluids 28(5):056102
108 Rao  Basu

<!-- PDF_PAGE: 27 -->

Downloaded from www.annualreviews.org.  Guest (guest) IP:  103.151.173.209 On: Sat, 29 Aug 2026 07:53:40
FL58_Art04_Basu ARjats.cls November 28, 2025 12:3
Sharma S, Chandra NK, Basu S, Kumar A. 2022. Advances in droplet aerobreakup. Eur . Phys. J. Spec. T op.
232(6):719–33
Sharma S, Chandra NK, Kumar A, Basu S. 2023a. Shock-induced atomisation of a liquid metal droplet.
J. Fluid Mech. 972:A7
Sharma S, Rao SJ, Chandra NK, Kumar A, Basu S, T ropea C. 2023b. Depth from defocus technique applied
to unsteady shock-drop secondary atomization. Exp. Fluids 64(4):65
Sharma S, Singh AP, Rao SS, Kumar A, Basu S. 2021. Shock induced aerobreakup of a droplet. J. Fluid Mech.
929:A27
Shen N, Bourouiba L. 2023. On the role of unsteadiness in impulsive-flow-driven shear instabilities: precursors
of fragmentation. J. Fluid Mech. 973:A28
Song J, Long T, Pan S. 2025. Three-dimensional numerical simulations of phase change effects on shock-
droplet interactions. Phys. Fluids 37(3):033358
Stumpf B, Roisman IV, Y arin AL, T ropea C. 2023. Drop impact onto a substrate wetted by another liquid:
corona detachment from the wall film. J. Fluid Mech. 956:A10
Sultanov FM, Y arin AL. 1990. Droplet size distribution in a percolation model for explosive liquid dispersal.
J. Appl. Mech. T ech. Phys.31(5):708–13
T ang K, Adcock TAA, Mostert W . 2023. Bag film breakup of droplets in uniform airflows.J. Fluid Mech.970:A9
T ang K, Adcock TAA, Mostert W . 2025. Droplet bag formation in turbulent airflows. Phys. Rev. Fluids
10(3):033604
T arey P, Ramaprabhu P, McFarland JA. 2024. Evolution of a shock-impacted reactive liquid fuel droplet with
evaporation effects: a numerical study. Int. J. Multiphase Flow 174:104744
Theofanous TG. 2011. Aerobreakup of Newtonian and viscoelastic liquids. Annu. Rev. Fluid Mech. 43:661–90
Theofanous TG, Li GJ, Dinh TN. 2004. Aerobreakup in rarefied supersonic gas flows. J. Fluids Eng.
126(4):516–27
Theofanous TG, Li GJ, Dinh TN, Chang CH. 2007. Aerobreakup in disturbed subsonic and supersonic flow
fields. J. Fluid Mech. 593:131–70
Thiesset F, Ménard T, Dumouchel C. 2021. Space-scale-time dynamics of liquid–gas shear flow.J. Fluid Mech.
912:A39
T raverso T, Abadie T, Matar OK, Magri L. 2023. Data-driven modeling for drop size distributions. Phys. Rev.
Fluids 8(10):104302
T roitskaya Y, Kandaurov A, Ermakova O, Kozlov D, Sergeev D, Zilitinkevich S. 2017. Bag-breakup
fragmentation as the dominant mechanism of sea-spray production in high winds. Sci. Rep. 7(1):1614
T ropea C. 2011. Optical particle characterization in flows. Annu. Rev. Fluid Mech. 43:399–426
V adlamudi G, Aravind A, Rao SJ, Basu S. 2024. Insights into spatio-temporal dynamics during shock–droplet
flame interaction. J. Fluid Mech. 999:A22
V eron F . 2015. Ocean spray.Annu. Rev. Fluid Mech. 47:507–38
V eron F, Hopkins C, Harrison EL, Mueller JA. 2012. Sea spray spume droplet production in high wind speeds.
Geophys. Res. Lett. 39(16):L16602
Villermaux E. 1998. Mixing and spray formation in coaxial jets. J. Propuls. Power 14(5):807–17
Villermaux E. 2007. Fragmentation. Annu. Rev. Fluid Mech. 39:419–46
Villermaux E. 2020. Fragmentation versus cohesion. J. Fluid Mech. 898:P1
Villermaux E, Bossa B. 2009. Single-drop fragmentation determines size distribution of raindrops. Nat. Phys.
5(9):697–702
Villermaux E, Marmottant P, Duplat J. 2004. Ligament-mediated spray formation. Phys. Rev. Lett.
92(7):074501
Virot F, T ymen G, Hébert D, Rullier J-L, Lescoute E. 2023. Experimental investigation of the interaction
between a water droplet and a shock wave above Mach 4. Shock W aves33(5):369–83
Vrij A, Overbeek J. 1968. Rupture of thin liquid films due to spontaneous fluctuations in thickness. J. Am.
Chem. Soc. 90(12):3074–78
Wang Y, Dandekar R, Bustos N, Poulain S, Bourouiba L. 2018. Universal rim thickness in unsteady sheet
fragmentation. Phys. Rev. Lett. 120(20):204503
Wang Y, Im KS, Fezzaa K. 2008. Similarity between the primary and secondary air-assisted liquid jet breakup
mechanisms. Phys. Rev. Lett. 100(15):154502
www.annualreviews.org  Secondary Atomization at Extreme Conditions 109

<!-- PDF_PAGE: 28 -->

Downloaded from www.annualreviews.org.  Guest (guest) IP:  103.151.173.209 On: Sat, 29 Aug 2026 07:53:40
FL58_Art04_Basu ARjats.cls November 28, 2025 12:3
Wang Z, Hopfes T, Giglmaier M, Adams NA. 2020. Effect of Mach number on droplet aerobreakup in shear
stripping regime. Exp. Fluids 61(9):193
Wang Z, Hopfes T, Giglmaier M, Adams NA. 2021. Experimental investigation of shock-induced tandem
droplet breakup. Phys. Fluids 33(1):012113
Wieland SA, Reckinger SJ, Hamlington PE, Livescu D. 2017. Effects of background stratification on the
compressible Rayleigh T aylor instability. In47th AIAA Fluid Dynamics Conference . AIAA
Xiao F, Wang ZG, Sun MB, Liu N, Y ang X. 2017. Simulation of drop deformation and breakup in supersonic
flow. Proc. Combust. Inst. 36(2):2417–24
Xiong T, Shao C, Luo K. 2024. Exploration of shock–droplet interaction based on high-fidelity simulation
and improved theoretical model. J. Fluid Mech. 988:A46
Xu Z, Wang T, Che Z. 2022. Droplet breakup in airflow with strong shear effect. J. Fluid Mech. 941:A54
Xu Z, Wang T, Che Z. 2023. Breakup of particle-laden droplets in airflow. J. Fluid Mech. 974:A42
Zandian A, Sirignano WA, Hussain F . 2017. Planar liquid jet: early deformation and atomization cascades.
Phys. Fluids 29(6):062109
Zandian A, Sirignano WA, Hussain F . 2018. Understanding liquid-jet atomization cascades via vortex
dynamics. J. Fluid Mech. 843:293–354
Zandian A, Sirignano WA, Hussain F . 2019. Length-scale cascade and spread rate of atomizing planar liquid
jets. Int. J. Multiphase Flow 113:117–41
Zhao H, Liu H-F, Li W-F, Xu J-L. 2010. Morphological classification of low viscosity drop bag breakup in a
continuous air jet stream. Phys. Fluids 22(11):114103
Zhao H, Nguyen D, Duke DJ, Edgington-Mitchell D, Soria J, et al. 2019. Effect of turbulence on drop breakup
in counter air flow. Int. J. Multiphase Flow 120:103108
110 Rao  Basu
