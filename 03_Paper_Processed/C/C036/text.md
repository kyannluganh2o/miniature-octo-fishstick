<!-- PDF_PAGE: 1 -->

PHYSICAL REVIEW FLUIDS 11, 023604 (2026)
Shock-induced aerobreakup of parallel-arranged droplets
Jianfeng Guo
Shanghai New Tobacco Products Research Institute Co., Ltd., Shanghai 201315, People’s Republic of China
and Department of Modern Mechanics, University of Science and Technology of China ,
Hefei 230026, People’s Republic of China
Peng Kang ,K a iM u ,* and Ting Si
State Key Laboratory of High Temperature Gas Dynamics/Department of Modern Mechanics,
University of Science and Technology of China , Hefei 230026, People’s Republic of China
(Received 31 October 2025; accepted 23 January 2026; published 17 February 2026;
corrected 6 March 2026)
The aerobreakup dynamics of parallel droplets subjected to shock-induced airﬂow is
investigated through experiments, in which the parallel-arranged droplets with controllable
size and spacing are generated through forced breakup of a free liquid jet. Utilizing
high-speed photography, the breakup process of parallel droplets over wide ranges of
spacing ratio and Weber number can be captured. At low Weber numbers, the droplet
fragmentation mode shifts gradually from the traditional bag breakup to the trailing and
shuttlecock modes as the spacing ratio decreases. At relatively high Weber numbers, the
breakup mode changes from an open to a closed conﬁguration, depending on whether the
channel between adjacent droplets closes during the deformation process. A phase diagram
of droplet fragmentation modes is constructed in the parametric region of Weber number
versus spacing ratio, with the boundaries between different modes clariﬁed theoretically.
Quantitative analyses on droplet deformation further demonstrate that reducing the spacing
ratio could accelerate ﬁlament formation and facilitate channel closure. Overall, this work
offers insights into the interaction dynamics of droplet clusters, thereby providing useful
guidance for applications such as fuel atomization.
DOI: 10.1103/5398-z2gf
I. INTRODUCTION
The deformation and subsequent fragmentation of droplets under gas ﬂow is referred to as droplet
aerobreakup. This is an archetypal interfacial ﬂow phenomenon that has been widely observed in
a variety of contexts, including natural phenomena, industrial applications, and defense industries
[1–3]. Thoroughly analyzing this issue can advance understanding of the evolutionary patterns of
related natural phenomena and furnish technical support and theoretical guidance for industrial and
defense applications.
Previous studies have conducted extensive research on the aerobreakup of a single droplet. Hinze
[4] was the ﬁrst to point out that the Weber number is the key parameter determining the aerobreakup
of droplets. He also noted that liquid viscosity inhibits the aerobreakup of droplets. Previous
researchers classiﬁed the aerobreakup modes of a single droplet into ﬁve categories based on
the different evolutionary morphologies of droplets: vibrational breakup, bag breakup, bag-stamen
breakup (multimode breakup), sheet stripping breakup, and catastrophic breakup [ 5,6]. Chou et al.
[7] plotted a phase diagram and provided the transition boundaries for each mode based on the
*Contact author: mukai@ustc.edu.cn
2469-990X/2026/11(2)/023604(19) 023604-1 ©2026 American Physical Society

<!-- PDF_PAGE: 2 -->

JIANFENG GUO, PENG KANG, KAI MU, AND TING SI
Weber number and the Ohnesorge number. The early-stage dynamics of droplets across various
breakup modes exhibit similarities, starting with surface ﬂattening due to high pressure on the
windward and leeward sides and low pressure at the equator. V ariations in aerodynamic forces then
lead to diverse morphologies. In the vibrational breakup mode, droplets undergo vibrations caused
by airﬂow that gradually intensify, leading to fragmentation at their center into subdroplets [8,9]. For
the bag and bag-stamen breakup modes, ﬂattened droplets form bags due to pressure differences,
which subsequently break into small droplets under the inﬂuence of surface tension and airﬂow
[10–12]. In the sheet stripping breakup mode, a thin liquid layer forms along the edges of ﬂattened
droplets, and this layer subsequently fragments into secondary droplets due to impingement by the
gas ﬂow [ 7,13]. In the catastrophic breakup, surface waves induced by airﬂow lead to eventual
fragmentation into subdroplets [ 8,14]. Theofanous [15] has also classiﬁed breakup modes based on
the dominant instability mechanism. At low Weber numbers (e.g., less than 100), Rayleigh-Taylor
(R-T) instability dominates, and this breakup mode is referred to as Rayleigh-Taylor piercing (RTP)
mode; at high Weber numbers (e.g., more than 1000), the gas ﬂow around the droplets induces
strong shear effects, and the Kelvin-Helmholtz (K-H) instability plays a primary role, resulting in
the breakup mode known as the shear-induced entrainment (SIE) mode [ 16–19]. Overall, the R-T
instability primarily occurs on the windward side of the droplet, while the K-H instability typically
occurs at the equatorial region of the droplet.
In practical applications such as fuel atomization, droplet clusters frequently experience aero-
breakup in the airﬂow [ 20,21]. Studying the aerobreakup mechanisms of droplet clusters can help
to improve fuel atomization devices and enhance atomization efﬁciency [ 3]. Typical droplet cluster
arrangements include tandem and parallel conﬁgurations. In the tandem droplet arrangement, the
centerline of the droplet chains lies parallel to the direction of the gas ﬂow. Theofanous et al. [22]
experimentally investigated the aerobreakup process of tandem droplets under low-Weber-number
conditions. They found that the breakup behavior of trailing droplets varies signiﬁcantly due to
the disturbance brought by leading droplets, and the presence of trailing droplets alters the critical
Weber number for mode transition of leading droplets. Wang et al. [23] conducted the experimental
studies on the aerobreakup of tandem droplets within a wide range of Weber numbers and droplet
spacing. Based on experimental results, a phase diagram of breakup modes was plotted, showing that
the critical spacing at which tandem droplets cease to inﬂuence each other decreases as the Weber
number increases. By employing large-eddy simulation to study the three-dimensional deformation
dynamics of tandem droplets in uniform airﬂow, Peng et al. [24] investigated how Reynolds
number, Weber number, density ratio, and initial spacing affect droplet interaction and perturbation
development. Furthermore, they developed a predictive model for droplet radius evolution, which
was validated against numerical and experimental data.
In the parallel droplet arrangement, the centerline of the parallel-arranged droplets is perpendicu-
lar to the direction of the gas ﬂow. Most experiments on aerobreakup of droplets utilize the dripping
faucet to generate droplets [ 25,26]. Nevertheless, the dripping faucet exhibits nonlinear dynamics,
which complicate the generation of parallel-arranged droplets with tunable spacing and uniform
size, thereby constraining experiments that require well-controlled parallel-arranged droplets. Due
to the experimental difﬁculty, current research primarily relies on numerical simulation. Stefanitsis
et al. [27] studied the aerobreakup process of parallel-arranged droplets under low-Weber-number
conditions using the Fluent platform. They found that when the distance between parallel-arranged
droplets is small, thin liquid ﬁlaments are drawn out from the droplets’ equatorial edges, which
is signiﬁcantly different from the typical aerobreakup mode of a single droplet. Further studies
indicated that the parallel-arranged droplets only interact with each other when the ratio of the
center-to-center distance to the diameter is less than 5. Using numerical simulations, Wu et al.
[28] investigated the early evolution of the shock wave system and the mid-to-late-stage dynamics
of parallel-arranged droplets under shock impact. They found that parallel-arranged droplets with
smaller droplet spacing ratios exhibit higher pressure peaks within the channel. Taglialatela et al.
[29] examined shock-induced breakup of parallel-arranged droplets using a compressible multi-
phase solver. Wave reﬂections from a neighboring droplet are found to weaken internal pressure
023604-2

<!-- PDF_PAGE: 3 -->

SHOCK-INDUCED AEROBREAKUP OF …
FIG. 1. (a) Schematic diagram of the shock-tube experimental apparatus. (b) Schematic diagram of the
control jet fragmentation apparatus, where droplets with uniform size and spacing are generated actively.
focusing, suppress secondary shocks from collapse, and modify vortical structures, thereby altering
early interfacial dynamics relative to the single droplet case.
Although the aerobreakup of parallel-arranged droplets has been considered through numerical
simulations, the existing studies are mainly limited to speciﬁc operating conditions (with Weber
numbers below 100 or above 1000). Thus, the droplet aerobreakup mechanisms within wide ranges
of parametric space remain far from understood. Therefore, it is imperative to obtain high-quality ex-
perimental data to ﬁll this critical knowledge gap and advance our understanding of the aerobreakup
behaviors over wide parameter ranges. To address these gaps, this paper develops an experimental
method for investigating the aerobreakup of parallel-arranged droplets, constructs a phase diagram
of aerobreakup modes across Weber numbers ranging from O(10) to O(100), and elucidates the
transition mechanisms between different aerobreakup modes. This paper is organized as follows.
Section II introduces the experimental methodology, encompassing the droplet generation method,
the layout of experimental devices, and the initial conditions for the experiments. In Sec. III,t h e
morphology of the aerobreakup of parallel-arranged droplets is observed at varying breakup modes.
Section IV presents a phase diagram illustrating the breakup modes of parallel-arranged droplets and
identiﬁes the transition boundaries. Section V presents quantitative statistics of parallel-arranged
droplets under various breakup modes, further elucidating the distinctions between these modes.
The conclusions of the study are provided in Sec. VI.
II. EXPERIMENTAL METHODOLOGY
Figure 1(a) shows a schematic diagram of the experimental setup for the aerobreakup of parallel-
arranged droplets. A uniform post-wave ﬂow is generated using a horizontal shock tube, which
effectively ensures the reproducibility of the experiment. The horizontal shock tube consists of four
parts: the driving section, the driven section, the transition section, and the experimental section.
In the experiment, a plastic diaphragm separates the driving and driven sections. Compressed air
is supplied to the driving section until the pressure difference across the diaphragm exceeds its
burst threshold. Once ruptured, rarefaction waves travel upstream into the driving section, while
an incident shock wave propagates downstream through the driven section, passes the transition
section, and reaches the experimental section. The shock wave and its following airﬂow then
interact with the parallel-arranged droplets. The experimental section is equipped with removable
observation windows on all sides, facilitating multi-angle photography of experimental results and
experimental operations. The detailed information of shock tube can be found in our previous work
023604-3

<!-- PDF_PAGE: 4 -->

JIANFENG GUO, PENG KANG, KAI MU, AND TING SI
[30]. Parallel-arranged droplets are formed through continuous jet breakup. Since free breakup
generates droplets with irregular spacing and size, active excitation is introduced. By applying
periodic sinusoidal disturbances to the ﬂuid at the inlet, precise control of jet fragmentation is
achievable, allowing regulation of droplet spacing and size. To achieve either very small or very
large spacing of droplets, the inﬂuence of gravity is additionally introduced. The speciﬁc control
principle and implementation method are shown in Appendix. The droplet generator can be arranged
at the top or bottom of the experimental section of the shock tube according to experimental
requirements. In this study, the diameter of the parallel-arranged droplets is denoted by D, and the
distance between adjacent droplets is represented by L. The droplet spacing ratio, deﬁned as L/D,i s
used to characterize the spacing between neighboring parallel-arranged droplets. Figure 1(b) shows
a schematic diagram of the active excitation and control jet fragmentation apparatus. The liquid
supplied by a syringe pump ﬂows through a membrane inside the pipeline at a constant ﬂow rate.
An oscillator, driven by a sinusoidal signal, imposes a sinusoidal disturbance on the membrane with
amplitude A and frequency f . As a result, the ﬂow rate of the liquid passing through the membrane
is modulated in a sinusoidal manner. Ultimately, this modulated ﬂow is delivered to the needle,
producing a periodically breaking jet.
This study considers the aerobreakup of alcohol droplets under shock wave-induced airﬂow
inside a shock tube, where the thickness of the boundary layer (with the order of 1mm) is much
smaller than the height of the shock tube (=28 cm), thus resulting in negligible inﬂuence brought by
the nonuniform ﬂow caused by the gas boundary layer. The dynamic viscosity and density of alcohol
are μ
l = 10− 3 Pa · s and ρl = 789.3k g/m3, respectively. The dynamic viscosity of the gas behind
the shock wave is μg = 17.9 × 10− 6 Pa · s, and the density ρg of the gas behind the shock wave
can be calculated from the Mach number. The surface tension at the gas-liquid interface, measured
using a surface tension meter, is σ
l = 21 mN/m. In the study of aerobreakup of parallel-arranged
droplets, three key dimensionless parameters are considered: Reynolds number ( Re), indicating the
ratio of inertial to viscous forces; Weber number ( We), expressing the ratio of inertial to surface
tension forces; and Ohnesorge number ( Oh), characterizing the interplay between viscous, inertial,
and surface tension effects. The calculation methods are as follows:
Re = ρgUgD
μg
, (1)
We =
ρgU 2
g D
σl
, (2)
Oh = μl√ ρlσl D, (3)
where the characteristic length is chosen as the diameter D of the parallel-arranged droplets. The gas
velocity Ug and the density ρg behind the wave, which can be calculated using the one-dimensional
gas dynamics equation:
Ug = 2a1
γ1 + 1
(
MS − 1
MS
)
, (4)
ρg
ρ1
= (γ1 + 1)M2
S
2 + (γ1 − 1)M2
S
, (5)
where γ1 is the speciﬁc heat ratio of air, taken asγ1 = 1.4 in this study. a1 is the local speed of sound,
taken as a1 = 340 m/s. ρ1 is the density of air, taken as ρ1 = 1.204 kg/m3. MS is the shock Mach
number. The shock wave velocity is obtained by dividing its displacement (tracked over several
consecutive schlieren or shadowgraph frames) by the corresponding time interval, and the Mach
number can be determined by comparing the shock wave velocity with the local sound speed. The
measurement methods and principles can be found in our previous work [ 30,31]. In the experiment,
023604-4

<!-- PDF_PAGE: 5 -->

SHOCK-INDUCED AEROBREAKUP OF …
FIG. 2. Aerobreakup process of parallel-arranged droplets at We = 16.7 with different spacing ratios,
with the airﬂow direction from left to right. The green solid points, blue solid points, and purple solid
points represent the results of the shuttlecock breakup mode, trailing breakup mode, and bag breakup mode,
respectively. The red solid line delineates the droplet interface and thus indicates the bending direction.
the airﬂow velocity can be adjusted by controlling the Mach number, thereby signiﬁcantly changing
the Weber number.
For the effects of gas and liquid viscosity, calculations show that the Reynolds number is of the
order of O(102 ∼ 103 ) under experimental conditions, and the Ohnesorge number is of the order of
Oh ≪ 0.1, so the viscosity of gas and liquid can be neglected. This study focuses only on the effects
of droplet spacing and Weber number on the aerobreakup of parallel-arranged droplets.
The characteristic time in this study is selected as D
Ug
√ρl
ρg
based on previous work [ 13], and the
dimensionless time t∗ is deﬁned as follows:
t∗ = t · Ug
D
√ρg
ρl
, (6)
where t is the dimensional time. The experimental results are captured by a Phantom V2012 high-
speed camera with a frame rate of 40 000 to approximately 100 000 Hz.
III. AEROBREAKUP PROCESS OF PARALLEL-ARRANGED DROPLETS
Previous studies have indicated that the shock-induced aerobreakup of both single and parallel-
arranged droplets can be treated as a purely aerodynamic problem, as the shock wave itself only
plays a secondary role in droplet interface deformation [ 30,32,33]. Figure 2 shows the results
of the aerobreakup process of parallel-arranged droplets with different spacing ratios under low-
Weber-number conditions ( We = 16.7). The experiments were conducted at a Mach number of
M
S = 1.05, with a post-wave gas density of ρg = 1.284 kg /m3 and a post-wave gas velocity
of Ug = 27.66 m /s, respectively. Droplets with diameter D = 357 µm were generated using a
needle of inner diameter d = 0.2 mm, at a liquid ﬂow rate of Q = 250 mL /h and an excitation
frequency of f = 3100 Hz. The frame corresponding to the dimensionless time is marked at the top
023604-5

<!-- PDF_PAGE: 6 -->

JIANFENG GUO, PENG KANG, KAI MU, AND TING SI
FIG. 3. Comparison of experimental results and schematic diagrams for various breakup modes at low
Weber numbers. (a) Shuttlecock breakup mode. (b) Trailing breakup mode. (c) Bag breakup mode.
of the image, and the droplet spacing ratio ( L/D) is marked on the left. The gas ﬂow direction is
from left to right. The zero time ( t∗ = 0) is selected as the moment when the droplet deformation
starts. It is noteworthy that, although previous studies have classiﬁed the aerobreakup of a single
droplet under low Weber numbers into bag breakup mode, bag-stamen breakup mode, and multibag
breakup mode, this study uniﬁes these three breakup modes as bag breakup mode. This is because
the three modes share similar bag structures and the same underlying physical mechanisms. When
L/D = 2.56, the aerobreakup of parallel-arranged droplets closely resembles that of single droplets.
High pressure differentials across the droplets (from windward surface to leeward surface) cause
them to ﬂatten, leading to the formation of bag and stamen structures. For closer droplet spacings
of L/D = 1.79 and L/D = 1.16, after ﬂattening, the bending directions (the red solid line shown in
the ﬁgure represents the direction of bending) of the droplets are opposite to the ﬂow direction of
gas ﬂow (t
∗ = 0.64; t∗ = 0.96), and the liquid interfaces on the upper and lower surfaces eventually
merge, forming a tail structure on the leeward side of the droplet ( t∗ = 1.43). This process differs
from the existing single-droplet breakup mode and is named the trailing breakup mode. For the
condition L/D = 0.31, the droplet pulls out liquid ﬁlaments from the equatorial position after
being ﬂattened. The pulled-out ﬁlaments continue to bend toward the leeward side ( t
∗ = 1.75),
and eventually break up under the inﬂuence of the airﬂow ( t∗ = 2.07). As the ﬁnal morphology
of the droplet resembles a shuttlecock, this breakup mode is designated as the shuttlecock breakup
mode. It is worth noting that the trailing and shuttlecock breakup modes were ﬁrst identiﬁed in the
numerical simulations of Stefanitsis et al. [27], and in the present work, both modes are observed
experimentally.
To analyze the differences between the three observed modes more accurately, Fig. 3 presents
a comparison of typical experimental results and schematic diagrams for each breakup mode. All
experiments were conducted under an identical shock Mach number of M
S = 1.05, corresponding
to a post-shock gas density of ρg=1.284 kg/m3 and a post-shock gas velocity of Ug = 27.66 m/s,
respectively. For the shuttlecock breakup mode illustrated in Fig. 3(a), the droplet was generated
using a needle with inner diameter d = 0.1 mm at a liquid ﬂow rate of Q = 70 mL/h and excitation
frequency of f = 3000 Hz, resulting in a droplet diameter of D = 230 µm. It is evident that when
the overall shape of the droplet remains unﬂattened, high-speed gas ﬂow in the channel between
droplets rapidly pulls out liquid ﬁlaments from the equatorial region of the droplets. These elongated
ﬁlaments bend and close under the inﬂuence of the gas ﬂow, effectively trapping gas inside the
023604-6

<!-- PDF_PAGE: 7 -->

SHOCK-INDUCED AEROBREAKUP OF …
FIG. 4. Experimental results of aerobreakup of parallel-arranged droplets at We = 351 with different
spacing ratios, with the airﬂow direction from left to right. The pink solid points and orange solid points
represent the results of the closed breakup mode and the open breakup mode, respectively.
droplets, as observed in previous numerical work [ 27]. Ultimately, the liquid ﬁlaments break up.
It is important to note that the deformation time for the shuttlecock breakup mode is signiﬁcantly
longer than that of the other two modes, due to the lower local airﬂow velocity around the ﬁlament,
which results in reduced stress strength. In the trailing breakup mode shown in Fig. 3(b), droplets
with diameter D = 357 µm were produced under the condition of d = 0.2m m , Q = 250 mL/h,
and f = 3100 Hz. The droplets initially become ﬂattened, after which the bending directions of the
droplets are opposite to the ﬂow direction of the gas ﬂow, resembling the behavior observed in the
shuttlecock breakup mode. The shear effect of the gas ﬂow in this mode is less pronounced than in
the shuttlecock breakup mode. As a result, the upward and downward bending of the liquid interface
does not lead to the formation of liquid ﬁlaments under shear stress. Instead, it continues to bend
backward and ultimately converges to create a trailing structure. In the bag breakup mode shown in
Fig. 3(c), droplets with diameter D = 230 µm were produced under the condition of d = 0.1m m ,
Q = 70 mL/h, and f = 3000 Hz. The droplets ﬁrst ﬂatten under the inﬂuence of gas pressure, then
bend in the direction of the ﬂow, pulling out a bag-like structure. Experimental results and schematic
diagrams both clearly demonstrate a key difference between the shuttlecock/trailing breakup modes
and the traditional bag-shaped breakup mode. Speciﬁcally, this difference is manifested in the
bending direction of droplets following their ﬂattening.
The aerobreakup of droplets at high Weber numbers exhibits signiﬁcantly different behaviors
compared to low-Weber-number conditions [ 5,6]. This difference arises because aerodynamic
forces, rather than surface tension, become the dominant force of the breakup process at high Weber
numbers. Figure 4 shows the results of aerobreakup experiments of parallel-arranged droplets with
different spacing ratios under high-Weber-number conditions ( We = 351). The experiments were
conducted at a Mach number of M
S = 1.2, with a post-wave gas density ρg = 1.59 kg/m3 and a
post-wave gas velocity Ug = 103.88 m/s, respectively. Droplets with diameter D = 430 µm were
generated using a needle of inner diameter d = 0.25 mm, at a liquid ﬂow rate of Q = 350 mL/h
and an excitation frequency of f = 2300 Hz. For a single droplet, the droplet is ﬁrst compressed by
the high pressure at the windward/leeward sides and the low pressure at the equatorial position. The
velocity difference at the gas-liquid interface at the equatorial position causes the Kelvin-Helmholtz
023604-7

<!-- PDF_PAGE: 8 -->

JIANFENG GUO, PENG KANG, KAI MU, AND TING SI
FIG. 5. Modes phase diagram of parallel-arranged droplets. The solid points are results obtained by our
experiments, while the hollow points represent the numerical simulation results of a previous study [ 27].
instability. Continuous shear effect from the gas ﬂow pulls liquid at the equatorial position
into ﬁlaments, which subsequently break into numerous small droplets. When L/D = 1.93 and
L/D = 1.33, during the droplet deformation, parallel-arranged droplets behave exactly like a single
droplet. At t∗ = 1.16, the liquid mist generated by the fragmentation of adjacent parallel-arranged
droplets mixes together. Therefore, the advection of the liquid mist is restricted, but the channels
between the droplets remain open. At L/D = 0.5, liquid ﬁlaments formed by the separation of
adjacent droplets near their equatorial positions come into contact at t
∗ = 0.87, causing the channels
to close. However, the channels quickly reopen under the inﬂuence of the gas ﬂow, and the
interfaces atomize into numerous small droplets. At this point, the droplets’ main bodies develop a
mushroom-like shape. For conditions where parallel-arranged droplets are closer, e.g., L/D = 0.1,
droplets near the equatorial position pull out liquid ﬁlaments more quickly to block the channel. At
this point, the channel undergoes its initial opening as a result of the sustained aerodynamic loading.
The liquid ﬁlaments continue to grow, and the ﬁlaments from the upper and lower droplets come
into contact again, causing the channel to close for the second time. Under continuous airﬂow, the
channel opens again. Overall, at high Weber numbers, closely spaced droplets induce the formation
of long liquid ﬁlaments at the equatorial position, causing channel closure, followed by reopening
due to airﬂow. In this work, the mode where the channel between droplets closes is referred to as
the closed breakup mode, while the mode where the droplet channel does not close is referred to as
the open breakup mode.
IV . MODES PHASE DIAGRAM AND TRANSITION BOUNDARIES
Furthermore, Fig. 5 presents the phase diagram of parallel-arranged droplet aerobreakup modes
in the droplet spacing ratio L/D and Weber number We parameter space. In the ﬁgure, the green
solid points, blue solid points, purple solid points, pink solid points, and orange solid points
represent the results of shuttlecock breakup mode, trailing breakup mode, bag breakup mode, closed
breakup mode, and open breakup mode, respectively. The solid points in the ﬁgure are the results
obtained in our experiments. To improve the reliability of the phase diagram and increase the dataset,
hollow points from previous numerical simulations are also incorporated [ 27]. It should be noted
that previous studies have pointed out that the breakup mode close to the critical Weber number
around 100 is the transition zone between bag breakup mode and sheet striping breakup mode,
exhibiting morphological characteristics of both modes [ 5,6]. Therefore, this study only considers
operating conditions where the Weber number is signiﬁcantly greater than or less than 100.
023604-8

<!-- PDF_PAGE: 9 -->

SHOCK-INDUCED AEROBREAKUP OF …
FIG. 6. (a) Uniform ﬂow past an array of unit-diameter cylinders. (b) Boundary value problem for w(z) =
φ + iψ in the cross-ﬂow case.
Figure 5 shows that at low Weber numbers ( We < 100), parallel-arranged droplets with L/D ⩾
2 exhibit bag breakup, while those with L/D < 2 undergo a shuttlecock or trailing breakup
mode. Notably, the Weber number does not alter the transition boundary between the bag and
shuttlecock/trailing modes. To clarify this distinction, the black dashed line denotes the theoretical
transition between the bag and trailing/shuttlecock modes (transition boundary I). It has been
demonstrated in Fig. 3 that the liquid-interface bending direction differs among these modes: in
the bag breakup, the interface bends toward the gas ﬂow relative to the droplet center, while in
the trailing and shuttlecock modes, it bends along the gas ﬂow direction. These opposing bending
directions produce different breakup mechanisms and thus underlie the mode separation at transition
boundary I. Moreover, under low Weber numbers (e.g., We < 30), the shuttlecock breakup mode
occurs only at very close spacing ratios ( L/D < 1), while the trailing mode appears at intermediate
spacing ratios (1 < L/D < 2). The reason lies in the fact that, according to conservation of mass, a
smaller spacing ratio accelerates the airﬂow through the gap between droplets, resulting in a higher
velocity at the equatorial region. Only at sufﬁciently small spacing, the shear stress can be strong
enough to trigger the shuttlecock mode. As the Weber number increases, the equatorial airﬂow
velocity and its associated shear stress intensify. Consequently, the shuttlecock mode becomes
more prevalent, and the parameter region for the trailing mode shrinks until it eventually vanishes.
For high-Weber-number conditions (We > 100), parallel-arranged droplets with L/D ⩾ 0.5 exhibit
open breakup mode, while those with L/D < 0.5 undergo closed breakup mode. The black solid
line represents the theoretical transition boundary between the closed breakup mode and the open
breakup mode, named transition boundary II.
At low Weber numbers, the mode transition is governed by the interface bending direction. This
direction is set by the local pressure distribution. Speciﬁcally, it depends on the relative pressure
difference between the droplet’s equatorial region and the windward stagnation point. The derivation
of the transition boundary I is outlined as follows. Considering the Reynolds number under the
experimental conditions, Re ∼ O(10
2 ∼ 103 ), the gas viscosity can be neglected. Following Khan
et al. [34], who applied the two-dimensional potential ﬂow theory for a transverse row of cylinders
in uniform ﬂow, we derive the velocity ﬁeld around a cylinder conﬁned between parallel plates to
obtain the velocity and pressure distributions on the surfaces of the parallel-arranged cylinders. The
theoretical framework assumes an inviscid, steady, incompressible, and irrotational ﬂuid ﬂowing
around an inﬁnite array of parallel-arranged cylinders.
The schematic diagram and boundary conditions are illustrated in Fig. 6. Speciﬁcally, Fig. 6(a)
shows the uniform ﬂow past an array of unit-diameter cylinders, consistent with our experimental
setup. To facilitate the theoretical analysis, the complex potential w(z) = φ + iψ is considered,
where φ represents the velocity potential and ψ denotes the stream function for irrotational
023604-9

<!-- PDF_PAGE: 10 -->

JIANFENG GUO, PENG KANG, KAI MU, AND TING SI
two-dimensional ﬂow. The boundary value problem for w(z) = φ + iψ in the cross-ﬂow geometry
is shown in Fig. 6(b). In the theoretical analysis, since all cylinders have identical diameters and
spacing, the ﬂow state around each cylinder is assumed to be similar. This scenario can therefore be
equivalently modeled as a ﬂow past a single cylinder positioned between two plane channel walls.
The upper and lower walls are symmetric with respect to the cylinder, with each wall located at a
distance of ( L + D)/2 from the cylinder’s center.
In this problem, the ﬂuid’s potential can be expressed as
w(z) = U
∞ z +
∞∑
j=−∞
μ
2π(z − ij (L + D)) = U∞ z + μ
2(L + D) cot h
( πz
L + D
)
, (7)
where j represents the number of cylinders, U∞ represents the velocity of the ﬂuid at inﬁnity, and
μ represents the dynamic viscosity of the ﬂuid, respectively. At the stationary position z =± D
2 ,
w′ (± D
2 ) = 0. Therefore, the complex potential can be further simpliﬁed as
w(z) = φ + iψ = U∞
[
z + C cot h
( πz
L + D
)]
, (8)
where φ and ψ are the stream function and potential function, respectively. C is a constant whose
value is
C = L + D
π sin h2
( πD
2L + 2D
)
. (9)
According to the above equation proposed by Khan et al. [34], the stream function φ and
potential function ψ of the ﬂuid can be obtained. Furthermore, through coordinate transformation,
the velocities in the r and θ directions of the cylindrical surface in the polar coordinate system can
be obtained:
ur =− 1
r
∂ψ
∂θ
⏐⏐
⏐
⏐
r=D/2
= 0,
uθ = ∂ψ
∂r
⏐⏐
⏐
⏐
r=D/2
= U∞ f (θ), (10)
where
f (θ) = sin θ+ 2s i nh2
(C1
2
)
sin (C1 sin θ) sin h(C1 cos θ) cos θ+ sin θsin (C1 cos θ)
[cos h(C1 cos θ) − cos (C1 sin θ)]2
− 2s i nh2
(C1
2
) cos (C1 cos θ) sin θ
cos h(C1 cos θ) − cos (C1 sin θ), (11)
where C1 = πD/(L + D) is a constant. θ= 0 represents the stationary point on the windward side
of the droplet. For a detailed derivation of this theory, please refer to Khan et al. [34].
Finally, the dimensionless ﬂow velocity U∗ around any of the parallel-arranged cylinders can be
obtained as
U∗ = U
U∞
= f (θ). (12)
Substituting the dimensionless velocity distribution on the cylindrical surface [Eq. ( 12)] into the
Bernoulli equation, one can obtain the dimensionless pressure distribution around the cylinder:
P∗ = 1 − U∗2
. (13)
When C1 = 0, the above equation can be reduced to the corresponding formula in the two-
dimensional ﬂow around a single cylinder [ 35], which veriﬁes the accuracy of the derivation.
By using Eqs. ( 13) and ( 12), the distribution of local dimensionless pressure and dimensionless
velocity around the circumference of parallel-arranged cylinders with different spacing ratios can
023604-10

<!-- PDF_PAGE: 11 -->

SHOCK-INDUCED AEROBREAKUP OF …
FIG. 7. (a) Dimensionless pressure distribution around the circumference of parallel-arranged cylinders
with different spacing ratios from 0 ∼π/2. (b) Dimensionless velocity distribution around the circumference
of parallel-arranged cylinders with different spacing ratios from 0 ∼ π/2.
be obtained, as shown in Fig. 7. When the spacing ratio is large (e.g., L/D = 3), the aerodynamic
pressure and ﬂow velocity ﬁelds around the parallel-arranged cylinders closely resemble those of
a single cylinder. Therefore, the dynamics of droplet deformation is similar to that of the single
droplet. As the spacing ratio decreases ( L/D ⩽ 2), the impact of droplet spacing occurs, leading
to substantial variations in both the pressure and velocity distributions compared to the single
cylinder case. Speciﬁcally, as the spacing ratio decreases, the growing pressure difference between
the equator and the stagnation point of the cylinders [see Fig. 7(a)] intensiﬁes the ﬂow from the
windward side to the equator. This intensiﬁed ﬂow is accompanied by a higher local velocity at
the equator under lower spacing ratios [Fig. 7(b)], ultimately driving the reorientation of the ﬂuid’s
bending direction from facing the ﬂow to aligning with it. The differing bending directions result in
distinct breakup modes. As obvious differences of pressure and velocity distributions compared with
the single cylinder case occur under L/D ⩽ 2, a critical spacing ratio of L/D = 2 is considered as
the transition boundary I (see Fig. 5). The boundary I predicts the shift from the shuttlecock/trailing
breakup mode to the bag breakup mode at low Weber numbers. It should be noted that the two-
dimensional cylinder model, adopted for analytical tractability, overestimates the equatorial ﬂow
velocity compared to the three-dimensional spherical droplet model. This overestimation delays
the predicted change of droplet bending direction with the increase of spacing ratio, causing a
higher theoretical boundary between the bag breakup mode and the shuttlecock/trailing modes.
Consequently, the presented theoretical boundary represents an upper limit, with the actual transition
boundary for spheres expected to shift to smaller spacing ratios. Nevertheless, the overall physical
tendency captured by the model remains valid.
The derivation of the transition boundary II is given as follows. For the two breakup modes at
high Weber numbers, the experimental results in Fig. 4 have already shown that whether the channel
can close is the key factor distinguishing the two breakup modes. In single-droplet aerobreakup, the
droplet reaches a maximum deformation height, deﬁned as the highest point attained before liquid
mist detaches. During the aerobreakup of parallel-arranged droplets at high Weber numbers, channel
closure will not occur if a droplet attains this deformation height prior to interacting with adjacent
droplets. Based on previous experiments [ 25], the maximum deformation height of droplets within
the Weber number range of 300 to 1000 can be described by D
max = 1.5D. Thus, the boundary II
can be obtained:
L
D = 0.5. (14)
023604-11

<!-- PDF_PAGE: 12 -->

JIANFENG GUO, PENG KANG, KAI MU, AND TING SI
FIG. 8. Temporal evolutions of the dimensionless parameters reﬂecting the droplet deformation and
breakup at We = 16.7. (a) V ariation of dimensionless height H∗ of liquid droplets. (b) V ariation of dimen-
sionless droplet spacing ratios L∗. (c) V ariation of dimensionless width W∗ of droplets. (d) V ariation of
dimensionless forward distance S∗ of droplets.
This equation corresponds to the transition boundary II in Fig. 5, which effectively predicts the
transition between the closed and open breakup modes.
V . DIMENSIONLESS SPA TIAL PARAMETERS OF DROPLETS
To better compare the changes of droplet morphology under different breakup modes, Figs. 8 and
9 show the temporal evolutions of the dimensionless parameters reﬂecting the droplet deformation
and breakup at We = 16.7 and We = 351, respectively. The four typical dimensionless quantities
selected here are: dimensionless height H∗, dimensionless width W∗, dimensionless forward dis-
tance S∗, and dimensionless distance between adjacent droplets L∗, deﬁned as follows:
H∗ = H/D,
W∗ = W/D,
S∗ = (S − S0 )/D,
L∗ = L/D. (15)
These dimensionless parameters are sketched in the subgraphs of Figs. 8(a) and 9(a).
023604-12

<!-- PDF_PAGE: 13 -->

SHOCK-INDUCED AEROBREAKUP OF …
FIG. 9. Temporal evolutions of the dimensionless parameters reﬂecting the droplet deformation and
breakup at We = 351. (a) V ariation of dimensionless height H∗ of liquid droplets. (b) V ariation of dimen-
sionless droplet spacing ratios L∗. (c) V ariation of dimensionless width W∗ of droplets. (d) V ariation of
dimensionless forward distance S∗ of droplets.
Figure 8 displays the temporal evolutions of the dimensionless parameters reﬂecting the droplet
deformation and breakup at We = 16.7. At L/D = 2.56, the droplet breakup presents bag breakup
mode; at L/D = 1.79 and L/D = 1.16, the droplet breakup presents trailing breakup mode;
at L/D = 0.31, the droplet breakup presents shuttlecock breakup mode. Figure 8(a) shows the
variation of the dimensionless height of the droplets. When L/D = 2.56, the height variation of
this condition is similar to the single droplet condition. In the trailing breakup mode ( L/D = 1.79
and L/D = 1.16), in the early stage of droplet deformation (0 < t∗ < 0.8), the height of the
droplets develops faster than that of a single droplet. According to Fig. 7(a), the pressure difference
between the equatorial position and the windward/leeward positions of parallel-arranged droplets
is greater than that of a single droplet. The pressure difference dominates the early stage of droplet
deformation; thus, the droplet in trailing breakup mode deforms faster. In the later deformation stage
(t
∗ > 0.8), due to the shear effect of the airﬂow in the channel, the upper and lower boundaries of
the ﬂattened droplets bend toward the leeward side (as shown in Fig. 3), resulting in a decrease in
the height growth. In the shuttlecock breakup mode ( L/D = 0.31), droplet height initially increases
(0 < t∗ < 0.4), reaching its maximum and remaining nearly unchanged before channel blockage
(0.4 < t∗ < 0.7). At t∗ > 0.7, the bending direction of the droplet is opposite to the ﬂow direction
of the gas ﬂow, and the overall droplet height rapidly decreases due to the shear effect of the gas
ﬂow at the droplet’s equator. Figure 8(b) shows the variation of the dimensionless droplet spacing,
023604-13

<!-- PDF_PAGE: 14 -->

JIANFENG GUO, PENG KANG, KAI MU, AND TING SI
which exhibits an inverse relationship with droplet height. This trend is clear in the bag and trailing
breakup modes ( L/D = 2.56, L/D = 1.79, and L/D = 1.16), where channel spacing decreases
progressively. In contrast, the shuttlecock breakup mode ( L/D = 0.31) presents a much slower
channel compression rate. The channels close when droplet height stops growing (0 .4 < t∗ < 0.7)
and subsequently reopen under the shear action of the gas ﬂow. Figures 8(c) and 8(d) present
the variations in the dimensionless width and forward distance, respectively. In the bag breakup
mode, both parameters evolve more slowly than in the trailing and shuttlecock breakup modes.
This difference arises because, according to volume conservation, droplet height increases rapidly
in modes with faster width compression.
Figure 9 shows the temporal evolutions of the dimensionless parameters reﬂecting the droplet
deformation and breakup at We = 351. At L/D = 1.93 and L/D = 1.52, the droplet breakup
presents open breakup mode; at L/D = 0.5 and L/D = 0.1, the droplet breakup presents closed
breakup mode. Figure 9(a) shows the variation of the dimensionless height. In the open breakup
mode (L/D = 1.93 and L/D = 1.52), the variation of the dimensionless height resembles that of a
single droplet. The closed breakup mode ( L/D = 0.5 and L/D = 0.1) is characterized by an initial
period (0 < t
∗ < 0.3) of height evolution that resembles the single droplet case, prior to a period
of slower development compared to the open mode. Notably, for L/D = 0.1, the closed breakup
mode undergoes two reopening events, producing a height pattern that increases, decreases, and then
increases again. As observed in Fig. 4, the late-stage height growth rate is reduced because channels
between droplets slow down its upward growth (e.g., L/D = 0.1). The repeated closure and reopen-
ing of these channels drive the observed rise-fall-rise sequence. Figure 9(b) shows the variation of
the dimensionless droplet spacing. In the open breakup mode ( L/D = 1.93 and L/D = 1.52), both
conditions exhibit a comparable rate of spacing decrease, which is faster than that observed in the
closed breakup mode. In the closed breakup mode ( L/D = 0.5 and L/D = 0.1), spacing decreases
more slowly, and the contact between liquid ﬁlaments shed from the equators of adjacent droplets
can cause one or two channel closures (see Fig. 4). The position where L
∗ = 0 is deﬁned as the
closure line and marked by a red dashed line in the ﬁgure. Under L/D = 0.5, the channel closes
once; under L/D = 0.1, it closes twice, with the ﬁrst closure occurring earlier than in the L/D = 0.5
case. According to potential ﬂow theory [see Fig. 7(b)], a smaller channel spacing ratio (L/D = 0.1)
induces higher airﬂow velocity, thereby generating greater shear stress at the equatorial positions
of the droplets. Figures 9(c) and 9(d) present the variations in the dimensionless width and forward
distance, respectively. The trends of these two parameters under different breakup modes are similar
to those observed in single-droplet scenarios. Under high-Weber-number conditions, shear forces
predominate, leading to rapid stripping and atomization of the droplet, which effectively diminishes
the impact of pressure-difference-induced channel effects.
VI. CONCLUSION
This study experimentally investigates the aerobreakup of parallel-arranged droplets over a wide
Weber number range ( O(10) to O(100)), addressing a gap in previous research that largely relied
on numerical simulations. An experimental approach combining external sinusoidal actuation with
free jet breakup under gravitational inﬂuence enabled precise control of droplet size and spacing,
allowing systematic observation of breakup dynamics using high-speed photography. Apart from
the traditional bag breakup mode, the shuttlecock and trailing modes with the variation of droplet
spacing at low Weber numbers were observed experimentally. Experimental results and potential
ﬂow analysis revealed that the difference between shuttlecock/trailing and bag breakup lies in the
post-ﬂattening bending direction, driven by pressure differentials between the droplet equator and
windward side. The closed breakup mode with the variation of droplet spacing at high Weber num-
bers was also identiﬁed. The transition from open breakup to closed breakup is governed by shear
strength at the droplet equator, with strong shear promoting rapid ﬁlament formation and channel
closure between droplets. A comprehensive phase diagram was developed to map these modes and
their transition boundaries. Subsequent quantitative analysis revealed the pivotal inﬂuence of droplet
023604-14

<!-- PDF_PAGE: 15 -->

SHOCK-INDUCED AEROBREAKUP OF …
spacing on the breakup dynamics. Speciﬁcally, the channels between parallel-arranged droplets sig-
niﬁcantly suppressed the development of droplets in the height direction. In the low-Weber-number
shuttlecock breakup and trailing breakup modes, smaller droplet spacings result in faster stretching
of the droplet ﬁlaments. In the high-Weber-number closed breakup mode, smaller droplet spacing
results in earlier closure of the channels between droplets. Overall, this work provides experimental
evidence and theoretical insight into parallel-arranged droplets aerobreakup, clariﬁes the role of
droplet spacing in regulating breakup dynamics, and presents a phase diagram that maps the regimes
of different breakup modes under varying operating conditions. These ﬁndings contribute to a deeper
understanding of droplet interaction mechanisms relevant to applications, including fuel atomization
and multiphase ﬂow control.
ACKNOWLEDGMENTS
This work was supported by the National Natural Science Foundation of China (Grants
No. 12272372, No. 12472228 and No. 12027801), Y outh Innovation Promotion Association CAS
(Grants No. 2018491 and No. 2023477), Strategic Priority Research Program of the Chinese
Academy of Sciences (Grant No. XDB0910100), the New Cornerstone Science Foundation through
the XPLORER PRIZE, USTC Tang Scholar and USTC Research Funds of the Double First-Class
Initiative (Grant No. YD2090002020).
DA TA A V AILABILITY
The data that support the ﬁndings of this article are openly available [ 36].
APPENDIX: METHODOLOGY FOR CONTROLLED GENERA TION OF PARALLEL DROPLETS
Here, the physical mechanism of active excitation control of jet fragmentation will be further
revealed through experimental results and theoretical derivations. The effects of liquid ﬂow rate and
excitation frequency on the size and spacing of parallel droplets will also be investigated.
Figure 10(a) shows the breakup of an alcohol jet under different excitation frequencies, where the
needle inner diameter is 0.2 mm, and the liquid ﬂow rate is Q = 250 mL/h. The experimental results
indicate that excitation must be applied within a certain frequency range to control the breakup of
the jet. When a jet is not subjected to any external periodic forcing, it can break up spontaneously
under the combined effects of Rayleigh–Plateau instability and ambient perturbations. The dominant
frequency associated with this self-induced breakup is known as the natural breakup frequency
of the jet. At lower excitation frequencies (e.g., f = 1000 Hz), the disturbances applied by the
piezoelectric stack have little effect on the jet fragmentation, and the jet fragmentation frequency
remains at the natural breakup frequency, resulting in droplets of nonuniform size and nonuniform
spacing. As the excitation frequency increases beyond a critical threshold, the jet fragmentation
frequency synchronizes with the excitation frequency, resulting in uniform droplet size and spacing.
Continuing to increase the excitation frequency, when the excitation frequency exceeds a certain
upper limit, the jet fragmentation frequency becomes smaller than the excitation frequency, exhibit-
ing a state similar to natural fragmentation. The frequency range where the excitation frequency is
equal to the jet fragmentation frequency is referred to as the synchronized region.
The lower limit of the synchronized region depends on factors such as the initial disturbance am-
plitude and its development time, making it difﬁcult to derive theoretically. The classical instability
theory of inviscid cylindrical jets [ 37] predicts that for disturbances which cause jet breakup, their
wavelength must be greater than the jet’s circumference. Consequently, there exists a theoretical
upper bound on the breakup frequency:
f
up = v0
πd j
, (A1)
where v0 is the velocity of the jet at the outlet of needle, and d j is the diameter of the jet.
023604-15

<!-- PDF_PAGE: 16 -->

JIANFENG GUO, PENG KANG, KAI MU, AND TING SI
FIG. 10. (a) Alcohol jet fragmentation process under different excitation frequencies f . (c) Comparison
of theoretical predictions and experimental measurements of droplet diameters, where d = 0.2m m a n d
Q = 250 mL/h. (c) Comparison of theoretical predictions and experimental measurements of droplet spacing
ratios, where d = 0.2m m a n d Q = 250 mL /h. (d) Synchronous region of alcohol jet fragmentation under
different ﬂow rates as d = 0.2 mm.
When the constant ﬂow rate Q and the excitation frequency f are within the synchronization
range, the theoretical droplet diameter D can be calculated using the following equation [ 38]:
D =
( 6Q
π f
)1/3
. (A2)
Figure 10(b) shows very good agreement between the experimental and theoretical results, where
the dotted line represents the theoretical results and the hollow dots represent the experimental
results. As the frequency increases, the droplet diameter decreases. The distance between adjacent
droplets L can be calculated using the following equation:
L = v
0
f − D = 4
πd2
j
Q
f −
( 6
π
)1/3( Q
f
)1/3
. (A3)
Combining Eqs. (A2) and (A3), the droplet spacing ratio L∗ can be calculated using the following
equation:
L∗ = L
D = v0
Df − 1 =
(
32
3π2d6
j
)1/3( Q
f
)2/3
− 1. (A4)
Figure 10(c) shows a comparison between the theoretical and experimental results, where the
dotted line represents the theoretical results and the hollow dots represent the experimental results.
The theoretical and experimental values agree well, and the spacing ratio L
∗ gradually decreases
with increasing excitation frequency.
Figure 10(d) shows the synchronized region of jet breakup for different liquid ﬂow rates. It can
be seen that both the upper and lower limits of the synchronized region increase with increasing
liquid ﬂow rate. When the excitation frequency exceeds either the upper or lower critical frequencies
of the synchronization interval, the droplet spacing ratio L
∗ no longer conforms to the theoretical
prediction results. Based on Eqs. ( A1) and ( A4), the droplet spacing ratio L∗ has a theoretical
minimum value, which is approximately 0.8 times the droplet diameter. The experimental results
023604-16

<!-- PDF_PAGE: 17 -->

SHOCK-INDUCED AEROBREAKUP OF …
FIG. 11. Method for generating droplets with extremely close and distant spacing. The experimental liquid
is alcohol, with d = 0.2m m , f = 2000 Hz, Q = 250 mL /h as examples, and the direction of gravity is
downward. (a) Method for generating extremely distant spacing, with the liquid ﬂowing downward. (b) Method
for generating extremely close spacing, with the liquid ﬂowing upward.
show that the parallel droplets generated by active excitation jet fragmentation can only achieve
droplet spacing control within a limited range. Therefore, it is necessary to employ alternative
methods to expand the control range of droplet spacing.
The inﬂuence of gravity can be utilized to broaden the range of droplet spacing ratios, enabling
the formation of either extremely close or widely spaced parallel droplets. It is worth noting that the
above analysis is based on ignoring gravity, and the experimental results in Fig. 10(a) also focus on
droplets near the end of the jet fragmentation. Under practical conditions, gravitational forces may
act on droplets situated far from the termination of jet fragmentation, even when their diameters are
considerably less than the capillary length ( ∼ 1.7 mm for glycerol).
Figure 11 shows the change in droplet spacing under active jet excitation with d = 0.2m m ,
f = 2000 Hz, Q = 250 mL/h. Figure 11(a) shows the jet ﬂow direction from top to bottom, and
Fig. 11(b) shows the jet ﬂow direction from bottom to top, with the direction of gravity in both cases
pointing downward. In the upward conﬁguration, absorbent paper was placed above the jet to collect
detached droplets and prevent their fallback. From the experimental results, it can be seen that when
the jet ﬂow direction is the same as the gravitational direction, the droplet spacing increases with
the distance from the nozzle; when the jet ﬂow direction is opposite to the gravitational direction,
the droplet spacing decreases with the distance from the nozzle opening until two or more droplets
coalesce into larger droplets. The experimental results prove the feasibility of using gravity to further
regulate the droplet spacing. It should be noted that the droplet velocity along the jet direction
(∼ 1m /s) is almost negligible compared to the post-shock ﬂow velocity (O(10) to approximately
O(100) m/s), so gravity is not expected to affect droplet morphology. Furthermore, as shown in
023604-17

<!-- PDF_PAGE: 18 -->

JIANFENG GUO, PENG KANG, KAI MU, AND TING SI
Eqs. (A2) and ( A3), changing the excitation frequency not only alters the droplet spacing ratio but
also changes the droplet diameter. Another advantage of utilizing gravity is that, without changing
the excitation frequency, the same droplet diameter but different droplet spacing can be achieved by
adjusting the position of the high-speed camera, enabling the capture of parallel droplet aerobreakup
experiments. Therefore, in formal experiments, for cases where the droplet spacing is large ( L >
0.8D), the jet ﬂow direction is aligned with the gravitational direction; for cases where the droplet
spacing is small ( L < 0.8D), the jet ﬂow direction is opposite to the gravitational direction. It is
important to note that the experiments can exhibit random variation in the alignment and spacing of
droplets. Consequently, the quantitative analysis presented in this study is based on data selectively
extracted from multiple trials, focusing on those results where the droplets adequately satisﬁed the
conditions of linear alignment and consistent spacing, thereby allowing a clear examination of the
underlying physical mechanisms.
[1] J. Eggers and E. Villermaux, Physics of liquid jets, Rep. Prog. Phys. 71, 036601 (2008) .
[2] A. Lefebvre and V . McDonell, Atomization and Sprays (CRC Press, Boca Raton, 2017).
[3] E. Villermaux, Fragmentation versus cohesion, J. Fluid Mech. 898, P1 (2020) .
[4] J. Hinze, Fundamentals of the hydrodynamic mechanism of splitting in dispersion processes, AIChE J. 1,
289 (1955).
[5] M. Pilch and C. Erdman, Use of breakup time data and velocity history data to predict the maximum size
of stable fragments for acceleration-induced breakup of a liquid drop, Int. J. Multiphase Flow 13, 741
(1987).
[6] D. Guildenbecher, C. López-Rivera, and P . Sojka, Secondary atomization, Exp. Fluids 46, 371 (2009) .
[7] W. Chou, L. Hsiang, and G. Faeth, Temporal properties of drop breakup in the shear breakup regime,
Int. J. Multiphase Flow 23, 651 (1997) .
[8] A. Wierzba, Deformation and breakup of liquid drops in a gas stream at nearly critical Weber numbers,
Exp. Fluids 9, 59 (1990).
[9] B. Gelfand, Droplet breakup phenomena in ﬂows with velocity lag, Prog. Energy Combust. Sci. 22, 201
(1996).
[10] W. Lane, Shatter of drops in streams of air, Industrial & Engineering Chemistry 43, 1312 (1951).
[11] I. Jackiw and N. Ashgriz, On aerodynamic droplet breakup, J. Fluid Mech. 913, A33 (2021) .
[12] I. Jackiw and N. Ashgriz, Prediction of the droplet size distribution in aerodynamic droplet breakup,
J. Fluid Mech. 940, A17 (2022) .
[13] J. Meng and T. Colonius, Numerical simulation of the aerobreakup of a water droplet, J. Fluid Mech. 835,
1108 (2018).
[14] P . Simpkins, On the distortion and breakup of suddenly accelerated droplets, in 12th Structures,
Structural Dynamics and Materials Conference (1971), p. 325.
[15] T. Theofanous, Aerobreakup of Newtonian and viscoelastic liquids, Annu. Rev. Fluid Mech. 43, 661
(2011).
[16] T. Theofanous and G. Li, On the physics of aerobreakup, Phys. Fluids 20, 052103 (2008).
[17] T. Theofanous, V . Mitkin, C. Ng, C. Chang, X. Deng, and S. Sushchikh, The physics of aerobreakup. II.
Viscous liquids, Phys. Fluids 24, 022104 (2012).
[18] T. Theofanous, V . Mitkin, and C. Ng, The physics of aerobreakup. III. Viscoelastic liquids, Phys. Fluids
25, 032101 (2013).
[19] V . Mitkin and T. Theofanous, The physics of aerobreakup. IV . Strain-thickening liquids, Phys. Fluids 29,
122101 (2017).
[20] N. Ashgriz, Handbook of Atomization and Sprays: Theory and Applications (Springer Science & Business
Media, New Y ork, 2011).
023604-18

<!-- PDF_PAGE: 19 -->

SHOCK-INDUCED AEROBREAKUP OF …
[21] S. J. Rao and S. Basu, Secondary atomization of droplets at extreme conditions, Annu. Rev. Fluid Mech.
58, 83 (2025) .
[22] T. Theofanous, G. Li, T. Dinh, and C. Chang, Aerobreakup in disturbed subsonic and supersonic ﬂow
ﬁelds, J. Fluid Mech. 593, 131 (2007) .
[23] Z. Wang, T. Hopfes, M. Giglmaier, and N. Adams, Experimental investigation of shock-induced tandem
droplet breakup, Phys. Fluids 33, 012113 (2021) .
[24] S. Peng, F. Chen, H. Y an, and F. Liu, Three-dimensional numerical simulation of tandem droplets
accelerated by continuous uniform airﬂow, Phys. Rev. Fluids 10, 024304 (2025) .
[25] S. Shen, J. Li, C. Tang, J. Liu, X. Ma, and W. Fan, The viscous effect on the transient droplet deformation
process under the action of shock wave, Atomization Sprays 29, 105 (2019) .
[26] Y . Liang, Y . Jiang, C. Wen, and Y . Liu, Interaction of a planar shock wave and a water droplet embedded
with a vapour cavity, J. Fluid Mech. 885, R6 (2020) .
[27] D. Stefanitsis, G. Strotos, N. Nikolopoulos, and M. Gavaises, Numerical investigation of the aerodynamic
breakup of a parallel moving droplet cluster, Int. J. Multiphase Flow 121, 103123 (2019) .
[28] R. Wu, Z. Li, and H. Ding, Impact of a planar shock onto side-by-side droplets: A 3D numerical study,
Chin. J. Theor. Appl. Mech. 54, 2958 (2022).
[29] F. E. Taglialatela and G. De Stefano, Numerical study of cavitation effects in shock-induced tandem
droplet breakup, Phys. Fluids 37, 092129 (2025) .
[30] J. Guo, P . Kang, K. Mu, J. Li, and T. Si, On shock induced aerobreakup of a wall-attached droplet, J. Fluid
Mech. 971, A31 (2023) .
[31] P . Kang, J. Guo, K. Mu, J. Li, and T. Si, Aerodynamic deformation and breakup of wall-attached droplets
in axisymmetric stagnation airﬂow, J. Fluid Mech. 1007, A48 (2025) .
[32] J. Meng and T. Colonius, Numerical simulations of the early stages of high-speed droplet breakup, Shock
Waves 25, 399 (2015) .
[33] H. Chen and S. Liang, Flow visualization of shock/water column interactions, Shock Waves 17, 309
(2008).
[34] W. Khan, J. Culham, and M. Y ovanovich, Fluid ﬂow and heat transfer from a cylinder between parallel
planes, J. Thermophys. Heat Transfer 18, 395 (2004) .
[35] P . Kundu, I. Cohen, and D. Dowling, Fluid Mechanics (Academic Press, San Diego, 2015).
[36] https://pan.quark.cn/s/61b1d91f8c37.
[37] L. Rayleigh, XVI. On the instability of a cylinder of viscous liquid under capillary force, London,
Edinburgh, Dublin Philos. Mag. J. Sci. 34, 145 (1892).
[38] C. Y ang, R. Qiao, K. Mu, Z. Zhu, R. Xu, and T. Si, Manipulation of jet breakup length and droplet size in
axisymmetric ﬂow focusing upon actuation, Phys. Fluids 31, 091702 (2019).
Correction: Author surnames in Ref. [ 29] and an in-text citation in the Introduction were displayed
incorrectly and have been ﬁxed.
023604-19
