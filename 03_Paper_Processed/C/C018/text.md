<!-- PDF_PAGE: 1 -->

J. Fluid Mech. (2024), vol. 988, A46, doi:10.1017/jfm.2024.472
Exploration of shock–droplet interaction based
on high-ﬁdelity simulation and improved
theoretical model
Tianheng Xiong1, Changxiao Shao1,† and Kun Luo2
1School of Mechanical Engineering and Automation, Harbin Institute of Technology, Shenzhen 518000,
PR China
2State Key Laboratory of Clean Energy Utilization, Zhejiang University, Hangzhou 310027, PR China
(Received 29 August 2023; revised 28 March 2024; accepted 6 May 2024)
Shock–droplet interaction in the early stage involves intricate wave structures.
Investigating this phenomenon is inherently challenging due to the ﬁne spatial and
temporal scales involved. Past research has suggested that the occurrence of cavitation,
marked by a negative peak pressure, is linked to the focus of the reﬂected expansion wave.
In this study, a high-ﬁdelity compressible numerical approach is utilized to replicate the
initial phase of
shock–droplet interactions. The location of the negative peak pressure is
meticulously documented and compared with experimental measurement and numerical
results. Results indicate a strong alignment between the negative peak pressure positions
identiﬁed through numerical simulations and the focal points identiﬁed in theoretical
models for low
gas–liquid wave velocity ratios. However, this alignment is notably
disrupted when dealing with higher gas–liquid wave velocity ratios. Further enhancements
are made to the theoretical model, enabling a more precise depiction of internal wave
structures and focus points, particularly under conditions of high gas–liquid wave velocity
ratios. The study delves into the various factors inﬂuencing internal pressure ﬂuctuations
within the liquid droplet, categorizing them into four phases: the shock wave effect,
relaxation effect, ﬂuctuation effect, and expansion wave effect. Analysing the pressure
decrease portion reveals that while the converging of the reﬂected expansion wave leads
to a substantial pressure drop, it accounts for only a fraction of the total pressure
variation. Consequently, any model predicting negative peak pressure positions must
comprehensively consider all contributing factors.
Key words: drops, gas/liquid ﬂow, shock waves
† Email address for correspondence: shaochangxiao@hit.edu.cn
© The Author(s), 2024. Published by Cambridge University Press 988 A46-1
https://doi.org/10.1017/jfm.2024.472
 Published online by Cambridge University Press

<!-- PDF_PAGE: 2 -->

T. Xiong, C. Shao and K. Luo
1. Introduction
Shock–droplet interactions manifest in various scenarios, such as the damage incurred by
aircraft or space vehicles from raindrops (Ando 2010), the secondary breakup of liquid jets
in scramjets (Liu et al. 2018), and applications in ultrasonic therapy (Coralic 2015; Shpak
et al. 2016). Investigating these interactions presents challenges due to their minute spatial
and temporal scales.
Prior studies on shock–droplet interactions have extensively documented droplet
morphology. Investigations have delved into the parameters governing droplet fracture
morphology, including the Reynolds number, Weber number, Ohnesorge number, density
ratio and viscosity ratio (Lane 1951; Engel 1958; Hanson, Domich & Adams 1963;
Nicholls & Ranger 1969; Hsiang & Faeth 1992, 1995; Liu & Reitz 1997; Joseph, Belanger
& Beavers 1999; Lee & Reitz 2000; Aalburg, Van Leer & Faeth 2003; Kékesi, Amberg
& Wittberg 2014; Meng 2016). The dynamic attributes of droplets have been assessed
through parameters such as longitudinal and transverse diameters, drag coefﬁcient and
surface area. Breakup modes have been categorized into bag mode, bag and stamen
mode, multi-bag mode, sheet thinning mode and catastrophic mode (Pilch & Erdman
1987). Corresponding feature numbers for each mode have also been documented
(Guildenbecher, López-Rivera & Sojka 2009; Zhao et al. 2010). Theofanous & Li ( 2008)
utilized laser-induced ﬂuorescence in experiments to offer detailed insights, demonstrating
that the catastrophic breakup mode is an experimental artefact. Breakup modes have been
reclassiﬁed into two categories: the Rayleigh–Taylorpiercing mode for We < 100 based on
Rayleigh–Taylor instability, and the shear-induced entrainment mode for We > 1000 based
on Kelvin–Helmholtz instability (Theofanous & Li 2008; Theofanous 2011; Theofanous
et al. 2012).
Through advances in experimental measurement, the phenomenon of cavitation
or the presence of cavities in droplets has been observed in pertinent experiments
involving early-stage shock–droplet interactions (Sembian et al. 2016)a n d droplet–wall
impingement (Field, Dear & Ogren 1989; Obreschkow et al. 2006, 2011; Field et al.
2012). Any liquid can enter a metastable state by being overheated above its boiling point
temperature or stretched below the saturated vapour pressure. Equilibrium is eventually
restored through nucleation (cavitation) of steam bubbles (Caupin & Herbert 2006). The
present study delves into the cavitation phenomenon induced by stretching (negative
pressure) rather than boiling. When a cavity ruptures, it generates a series of shock waves
(Wu, Xiang & Wang 2018), potentially inﬂuencing subsequent droplet deformation and
breakup (Bhattacharya 2016), thereby possibly hastening equipment damage (Philipp &
Lauterborn 1998; Kodama & Tomita 2000;B r u j a net al. 2002). According to classical
nucleation theory (Debenedetti 1996), pure liquid water should withstand pressures
exceeding − 100 MPa (Caupin 2005; Azouzi et al. 2013).
The initial phase of shock–droplet interaction (prior to the shock wave completely
traversing the droplet) receives limited attention due to the minimal deformation of
droplet shape and the involvement of small time scales. Sembian et al. (2016)w e r e
the ﬁrst to observe cavities within droplets during the early stages of shock–droplet
interaction in experimental settings. Their ﬁndings revealed that transmitted waves within
the droplet reﬂect and concentrate as expansion waves upon reaching the downstream
wall (i.e.
gas–liquid interface) of the droplet, creating a negative peak pressure (NPP)
point that triggers cavitation. Biasiori-Poulanges & Schmidmayer ( 2023) conducted a
phenomenological analysis of shock-induced cavitation in droplets using a multi-phase
modelling approach. The critical pressure relaxation rate crucial to the numerical model
988 A46-2
https://doi.org/10.1017/jfm.2024.472
 Published online by Cambridge University Press

<!-- PDF_PAGE: 3 -->

Exploration of shock–droplet interaction
was ascertained by comparing numerical outcomes with the Keller–Miksis model and
related experiments. Additionally, adjustments were made in predicting the bubble cloud to
factor in the magnitude of the expansion wave. Schmidmayer & Biasiori-Poulanges (2023)
examined the geometrical effects on shock-induced cavitation in droplets, considering
various aspects such as the shape of the transmitted wavefront and the droplet’s geometry
(cylindrical
versus spherical). Determining the critical Mach numbers for cavitation onset
in the column and droplet, two cavitation regimes were identiﬁed based on transmitted
wavefront geometry. Xu et al. (2023) explored the impact of planar shock waves with
varying intensities on liquid droplets using a numerical method capable of resolving
compressible multi-phase ﬂow issues without phase change.
Xiang & Wang (2017) simulated the interaction between a shock wave and a cylindrical
droplet containing an air cavity, investigating the impacts of varying shock wave intensities
and cavity sizes. Liang et al. (2020) conducted a quantitative analysis of how the relative
size and eccentricity of the cavity affect the motion and deformation of hollow droplets
in experiments. Liu ( 2021) observed the deformation processes wherein the
vapour cavity
ﬁrst compresses and then expands during shock tube experiments, deriving an equation
predicting the vapour bubble collapse process. Previous studies examined the effects of
cavities within droplets, assuming a constant-diameter cavity initialization. However, in
reality, the cavity expands as pressure decreases. Evaluating the fundamental reasons
inﬂuencing shock–droplet interactions is challenging, making it difﬁcult to assess cavity
formation, size, location and temporal evolution accurately.
This study focuses primarily on identifying the location of the NPP during the early
stages of shock–droplet interaction, a key driver of cavitation. Research by Sembian et al.
(2016) indicated a constant cavity location approximately 19% of the droplet’s diameter
from the downstream wall. Wu et al. (2018) performed a theoretical examination of
internal wave structures within droplets in droplet–wall impingement studies, suggesting
a consistent cavity position approximately one-third of the diameter from the downstream
wall. Biasiori-Poulanges & El-Rabii ( 2021) conducted a theoretical investigation of
wave structures inside droplets, deriving a formulation for the temporal evolution of
the wavefront within droplets. Numerical simulations under corresponding conditions
reﬂected good agreement with experimental and theoretical analyses.
Few simulations incorporating phase changes have been conducted for current droplet
shock-induced cavitation studies. Kyriazis, Koukouvinis & Gavaises ( 2018) utilized
a thermodynamically rigorous model incorporating phase changes to replicate Field
et al. (1989) high-speed droplet impact experiment. Xu et al. (2022) advanced a
multi-component two-phase compressible ﬂow model with a phase transition procedure
to elucidate wave structure evolution and cavitation
behaviours, encompassing cavity
inception, growth and collapse. Notably, the focusing point’s position is governed by
dimensionless wave speed and aligns closely with numerical simulation outcomes.
High-intensity incident shock waves can delineate the focusing area of the reﬂected
expansion wave as a cavitation zone.
Most prior investigations have focused on scenarios with low
gas–liquid wave
velocity ratios, leaving a gap in research regarding higher ratios. The cases of higher
gas–liquid wave velocity ratios are rarely reported except i nt h ew o r kb yS c h m i d m a y e r
& Biasiori-Poulanges ( 2023) at Mach number up to 6. High gas–liquid wave velocity
ratios are paramount for real-world liquid fuels pivotal in high-speed transport. At lower
gas–liquid wave velocity ratios, internal transmitted waves display outward convex shapes.
Conversely, higher ratios evoke internally concave wave patterns, warranting exploration
into parallels with lower ratio formation mechanisms. Schmidmayer & Biasiori-Poulanges
988 A46-3
https://doi.org/10.1017/jfm.2024.472
 Published online by Cambridge University Press

<!-- PDF_PAGE: 4 -->

T. Xiong, C. Shao and K. Luo
(2023)d e l v e di n t ohigh-Mach-number droplet shock-induced cavitation, deftly avoiding
ionization limits at Mach 6. Their research hints at an ionization threshold, estimated at
approximately Mach 8. A similar maximum shock Mach number is also employed in the
present work to investigate whether there will be any additional phenomena occurring.
The understanding of negative pressure points instigating cavitation remains nebulous,
traditionally linking the focal point of a reﬂected expansion wave to the NPP point,
the apparent site primed for cavitation inception. This study
endeavours to elucidate
distinctions between the NPP and focus points, representing the likely cavity generation
site and the focus inﬂuenced primarily by the reﬂected expansion wave, respectively.
The organization of this paper unfolds as follows . In § 2, we present and validate the
high-ﬁdelity numerical simulation methodology. In § 3, simulation results of the NPP
point and comparison with experimental measurement are presented. The enhancements
to the theoretical model are expounded upon in § 4.I n§ 5,w ed e l v ei n t ounravelling the
NPP formation mechanism through a synergy of numerical analyses and reﬁned theoretical
results. The conclusion is given in § 6.
2. Numerical method
2.1. Problem description
The physical conﬁguration depicted in ﬁgure 1 illustrates a shock wave with the shock
Mach number Ms moving to the right and engaging with a two-dimensional (cylindrical)
droplet of diameter D0. Due to challenges in maintaining a perfectly spherical droplet
during experiments, geometric factors could inﬂuence the shock–droplet interaction
(Xiang & Wang 2017). However, numerical simulations can mitigate this inﬂuence. For
computational efﬁciency, this study focuses solely on the top portion of the physical ﬁeld
in a two-dimensional context, delineated by the blue dashed line within a computational
domain of 14 D0 × 6D0 with 800 grid cells per diameter. A grid-independent test is
detailed in Appendix A. The reﬂective boundary condition (RBC) is applied to the lower
boundary to account for symmetry, while the non-reﬂective boundary condition (NRBC)
is implemented on the upper, left and right boundaries due to the small scale of the droplet
relative to the entire physical spatial scale. Detailed boundary condition deﬁnitions are
available in Thompson ( 1987, 1990). Initial conditions will introduce a starting error,
manifesting as a sound wave opposing the direction of airﬂow due to the shock wave’s
motion, as elaborated by LeVeque (2002). Despite this minor error, the negligible intensity
of the sound wave compared to the shock wave ensures that it does not impact the droplet’s
aerodynamic deformation or downstream effects.
Both the pre-shock air and liquid droplet are initially set at atmospheric pressure.
The shock wave propagates at the Ms shock Mach number, inducing post-shock air
characterized by increased pressure and density. Table 1 presents the pressure and density
ratios ( ppost/ppre and ρpost/ρpre, respectively) between post-shock air and pre-shock air,
alongside the gas–liquid wave velocity ratio ( n) at varied shock Mach numbers for water
and n-hexane phases. The gas–liquid wave velocity ratio is derived as the ratio of shock
wave velocities in the gas and liquid phases, deﬁned by n = ug/ul, where ug and ul
represent the shock wave velocities in the gas and liquid phases. Following the Boyd
& Jarrahbashi ( 2021) methodology, cases with n > 1 are deemed high gas–liquid wave
velocity ratios whereby incident shock waves surpass internal transmitted waves in speed.
Conversely, instances of n < 1 constitute low gas–liquid wave velocity ratios, indicating
shock waves trailing internal transmitted waves in velocity.
988 A46-4
https://doi.org/10.1017/jfm.2024.472
 Published online by Cambridge University Press

<!-- PDF_PAGE: 5 -->

Exploration of shock–droplet interaction
NRBC
Shock
Ms RBC
Droplet, D0
OutflowInflow
Post-shock air Pre-shock air
Figure 1. Schematic diagram of two-dimensional shock–droplet interaction. The blue dashed line denotes the
computational domain.
Ms ppost/ppre ρpost/ρpre nn-hexane nwater
1.75 3.406 2.279 0.550 0.413
2.4 6.553 3.212 0.755 0.567
3.0 10.333 3.857 0.943 0.708
3.6 14.953 4.330 1.131 0.850
4.2 20.413 4.675 1.320 0.991
4.8 26.713 4.930 1.509 1.133
5.4 33.853 5.122 1.698 1.273
6.0 41.833 5.268 1.886 1.416
6.6 50.653 5.382 2.075 1.558
7.2 60.313 5.472 2.264 1.700
7.8 70.813 5.544 2.452 1.841
8.4 82.153 5.603 2.641 –
Table 1. Simulated cases and relevant shock parameters.
The Reynolds number ( Re) and the Weber number ( We) indicate the signiﬁcance of
viscosity and surface tension, respectively. The deﬁnitions in the Meng ( 2016) research of
shock–droplet interaction are
Re = ρpost upost D0
μ , (2.1)
We =
ρpost u2
post D0
σ , (2.2)
where ρpost, upost, D0, σ and μ are the post-shock air density, post-shock air velocity,
initial droplet diameter, surface tension coefﬁcient and dynamic viscosity coefﬁcient of
the post-shock air, respectively. The ranges considered for Re and We in this study span
from 2.01 × 103 to 1.19× 105, and from 9.42 × 103 to 4.10 × 106, respectively. Notably,
previous research by Meng ( 2016) and Kaiser et al. (2020) indicates that the inﬂuence
of surface tension and viscous forces can be negligibly small compared to inertial forces,
especially during the early stages of shock–droplet interactions.
2.2. Numerical method
This research utilizes the open-source Multi-component Flow Code (MFC), a high-order,
multi-component, multi- phase and multi-scale compressible ﬂow solver developed by
988 A46-5
https://doi.org/10.1017/jfm.2024.472
 Published online by Cambridge University Press

<!-- PDF_PAGE: 6 -->

T. Xiong, C. Shao and K. Luo
Fluid ρ (kg m− 3) γ π∞ (Pa)
n-hexane 657 5.39 1 .45 × 108
Water 1000 6.12 3 .43 × 108
Air 1.204 1.4 0
Table 2. Fluid properties at normal temperature and pressure and the SGEOS parameters.
Bryngelson et al. (2021) for the simulations. The governing equations are represented as
∂α1ρ1
∂t + ∇· (α1ρ1u) = 0, (2.3)
∂α2ρ2
∂t + ∇· (α2ρ2u) = 0, (2.4)
∂ρu
∂t + ∇· (ρu × u + pI) = 0, (2.5)
∂E
∂t + ∇· ((E + p)u) = 0, (2.6)
∂α1
∂t + u ·∇ α1 = 0, (2.7)
where ρ is the density, α is the volume fraction, u is the velocity vector, p is the pressure,
I is the identity matrix, and E is the total energy deﬁned as E = ∑Ni
i=1 αiρiei +∥ u∥2/2,
with Ni the number of involved ﬂuids, which is two in this study. The subscripted variables
represent different ﬂuids. It should be noted that there is an expansion term K ∇· u in (2.3)
and (2.4) for the model of Kapila et al. (2000). The effect of this expansion term is provided
in Appendix B, and it shows that the term has a negligible effect on the result.
The stiffened gas equation of state (SGEOS) is employed to close the ﬁve-equation
model, deﬁned as
pi = (γi − 1)ρiei − γiπ∞ ,i, (2.8)
where γ is the speciﬁc heat ratio ,a n d π∞ is the liquid stiffness (if the component is
gas, then the value equals 0). The SGEOS applies to both components , including gas and
liquid. For liquid, the above two parameters can be ﬁtted by the experimental data, and
the speciﬁc method can be found in Johnsen (2008). The SGEOS parameters of water can
be found in Meng & Colonius ( 2018), while the data for n-hexane are obtained by ﬁtting
the experimental data of Marsh ( 1980). The obtained parameters are listed in table 2 .
A comprehensive selection of SGEOS parameters for liquids is presented, and the original
experimental data of these parameters are assessed in Appendix C.
Finally, the entire governing equations are closed with a series of mixture relationships :
1 = α1 + α2, (2.9)
ρ = α1ρ1 + α2ρ2, (2.10)
ρe = α1ρ1e1 + α2ρ2e2. (2.11)
The governing equations are solved using the ﬁnite-volume method and shock-capturing
schemes, coupled with the Harten–Lax–van Leer–contact Riemann solver. Spatial
discretization employs a ﬁfth-order weighted essentially non-oscillatory scheme for ﬂux
988 A46-6
https://doi.org/10.1017/jfm.2024.472
 Published online by Cambridge University Press

<!-- PDF_PAGE: 7 -->

Exploration of shock–droplet interaction
Reflected
wave
Mach stem
Reflected
expansion
wave
Incident
wave
Transmitted
wave
Incident shock
wave (I)
Focusing
of REx
(FREx)
0.10
0.24
0.38
0.52
0.66
0.10
0.68
–0.70
0.03
0.75
1.48
2.21
0.10
0.57
1.04
1.51
1.98
1.27
1.85
2.43
0.08
0.65
1.21
1.77
2.33
–3.41
–2.02
–0.63
0.75
2.14
P (MPa) P (MPa)
P (MPa) P (MPa)
P (MPa) P (MPa)
t∗ = 0 t∗ = 0.603
t∗ = 0.829 t∗ = 1.055
t∗ = 1.281 t∗ = 1.884
Expansion
wave (REx)Transmitted
wave (T)
Shock wave
(R)
(a)( b)
(c)( d)
(e)( f )
Figure 2. Comparison between the simulation results in the top part of each panel and the experimental
shadowgraphs at bottom left. The pressure contours are also shown, at bottom right.
reconstruction, while time integration utilizes a third-order total variation diminishing
Runge–Kutta scheme. Further insights into the numerical methodologies can be found
in the works of Johnsen & Colonius ( 2009) and Bryngelson et al. (2021).
2.3. Validation
The two-dimensional shock–droplet interaction with Ms = 2.4 is ﬁrst simulated with the
same conditions as in Sembian et al. (2016). Comparisons between the present numerical
simulation results and experiments of Sembian et al. (2016) are shown in the left-hand
sides of each of ﬁgures 2(a–f ). The top image in each panel shows the numerical schlieren,
and the bottom shows the experimental shadowgraph image of Sembian et al. (2016).
The instantaneous pressure contours are also shown on the right-hand sides of each of
ﬁgures 2(a–f ). The non-dimensional time is deﬁned as t∗ = clt/D0, where cl is the sound
speed in the liquid phase, t is the physical time,a n dD0 is the initial diameter of the droplet.
Initially, in ﬁgure 2(a), the shock wave is observed attached to the left pole of the droplet.
On the right-hand side of the shock wave, a stationary droplet and pre-shock air are visible,
with post-shock air located on the left-hand side. As the shock wave progresses to the
right, it generates a reﬂected wave moving in the opposite direction outside the droplet,
creating a transmitted wave moving inward in the same direction within the droplet (as
depicted in ﬁgure 2 b). This transmitted wave inside the droplet continues its rightward
trajectory (ﬁgure 2c), with a Mach stem emerging at the intersection of the incident shock
wave and the reﬂected wave outside the droplet. Some of the transmitted wave near the
988 A46-7
https://doi.org/10.1017/jfm.2024.472
 Published online by Cambridge University Press

<!-- PDF_PAGE: 8 -->

T. Xiong, C. Shao and K. Luo
10
–10
–20
–30
–40
–50
–60
–70
–80
0
012345
Ms 1.75
Ms 2.4
Ms 3.0
Ms 3.6
Ms 4.2
Ms 4.8
Ms 5.4
Ms 6.0
Ms 6.6
Ms 7.2
Ms 7.8
First focus
Pmin (MPa) Second focus
t∗
Figure 3. Temporal evolution of the NPP values inside the water droplet with different shock Mach numbers.
upper and lower boundaries of the droplet is reﬂected back due to the concave shape
of the droplet, leading to a pressure decrease. Eventually, the transmitted wave reaches
the
right-hand boundary of the droplet and reﬂects as an expansion wave ( ﬁgure 2 d). In
ﬁgure 2(e), the reﬂected expansion wave converges at a point, creating a small area with
highly negative pressure on the droplet’s centreline. The expansion wave continues its
propagation until its strength diminishes, as seen in ﬁgure 2 ( f ). Overall, the simulation
results align closely with the experimental observations, which demonstrates the accuracy
of the present method.
3. Results of the NPP point
3.1. Time history of the NPP point
The NPP point represents the minimum pressure during wave transmission within the
droplet. The temporal evolution of NPP values, denoted as Pmin, within the water droplet
for shock Mach numbers ranging from 1.75 to 7.8 ( recording only values with pressures
less than 0) is depicted in ﬁgure 3 . This illustration reveals that the occurrence of NPP
values at t∗ ≈ 1.25 remains consistent across all Mach numbers, with the minimum
pressure declining as the shock Mach number increases (refer to the corresponding contour
in ﬁgure 2 e). Notably, the NPP value for higher Mach numbers emerges slightly earlier
than for lower Mach numbers. Recalling that each time the expansion wave reﬂects and
converges, a local pressure decrease occurs (Xu et al. 2023).
This seems to show that the
expansion wave converges at t∗ ≈ 1.25 for all Mach numbers.
3.2. Location of the NPP point
The NPP point’s location in shock–droplet interaction is illustrated in ﬁgure 4 .I nt h e
ﬁgure, l represents the distance between the NPP point and the droplet’s right- hand
boundary, which can be normalized by the droplet’s initial diameter ( D0) and denoted as
L. Figure 5 displays a comparison of the NPP point’s locations obtained from numerical
988 A46-8
https://doi.org/10.1017/jfm.2024.472
 Published online by Cambridge University Press

<!-- PDF_PAGE: 9 -->

Exploration of shock–droplet interaction
Droplet, D0
NPP point l
L = l/D0
Figure 4. Schematic diagram of the NPP point with the black dot inside the droplet.
simulations, experimental measurements and theoretical results. The blue line represents
the experimental data from Sembian et al. (2016), who studied water with shock Mach
numbers 1.75 and 2, suggesting the ﬁxed position equivalence between NPP and the
focus point. To reﬂect this view across all shock Mach numbers, a line connecting two
points is extended. The black solid line corresponds to the theoretical prediction by
Biasiori-Poulanges & El-Rabii ( 2021)a n dX u et al. (2023), while the red scattered points
depict the numerical outcomes of this study. In ﬁgure 5(a), the NPP point’s location with
water is marked by solid squares, while with n-hexane it is shown with hollow squares
in ﬁgure 5(b). Following Biasiori-Poulanges & Schmidmayer ( 2023), an optimal pressure
relaxation rate of 3.5 for shock-droplet interaction is recommended, along with positioning
the cavitation bubble cloud’s
centre 1.5 times away from the origin than the focus point
(with the right as the positive direction).
Observations indicate that at low gas–liquid wave velocity ratios, with an increase
in shock Mach number, the NPP point moves closer to the droplet’s downstream side,
aligning with theoretical predictions by Biasiori-Poulanges & El-Rabii ( 2021), Xu et al.
(2023) and Biasiori-Poulanges & Schmidmayer ( 2023). Conversely, at higher gas–liquid
wave velocity ratios, the NPP point’s position deviates from the theoretical downward
trend as the shock Mach number rises. In ﬁgure 5(b), as the shock Mach number increases,
the NPP point’s location in n-hexane moves to approximately 0.19, mirroring the ﬁndings
of Sembian et al. (2016).
Our ﬁndings align closely with Biasiori-Poulanges & El-Rabii ( 2021), whereas
Biasiori-Poulanges & Schmidmayer ( 2023) indicate proximity to the droplet’s right-hand
wall. It is crucial to note that the comparison in ﬁgure 5 is based on three different
concepts: the NPP point (our data), the focal point (Biasiori-Poulanges & El-Rabii
2021), and the centre point of the cavitation cloud (Biasiori-Poulanges & Schmidmayer
2023). According to Biasiori-Poulanges & Schmidmayer ( 2023), a speciﬁc position is
identiﬁed where the expansion wave reaches the strength required to induce gas expansion,
suggesting that cavitation should commence before the expansion wave reaches the focus
and negative pressure points. Moreover, a rising relaxation coefﬁcient continually brings
the central area of the cavitation cloud closer to the droplet’s downstream side. In scenarios
with high
gas–liquid wave velocity ratios, our NPP point stabilizes at a constant while the
focal point and cavitation cloud centre shift close to the droplet’s right-hand side.
988 A46-9
https://doi.org/10.1017/jfm.2024.472
 Published online by Cambridge University Press

<!-- PDF_PAGE: 10 -->

T. Xiong, C. Shao and K. Luo
0.35
0.30
0.25
0.20
0.15
0.10
0.05
0
0123456789
0.35
0.30
0.25
0.20
0.15
0.10
0.05
0
0123456789
Ms
L
L
Biasiori-Poulanges & El-Rabii (2021)
Sembian et al. (2016)
Biasiori-Poulanges & Schmidmayer (2023)
Simulation (water)
Biasiori-Poulanges & El-Rabii (2021)
Biasiori-Poulanges & Schmidmayer (2023)
Simulation (n-hexane)
(a)
(b)
Figure 5. Comparison of the NPP point’s location obtained from the numerical simulation results with
experimental measurements and theoretical results for ( a) water and ( b) n-hexane.
We believe that the key to this issue is whether the reﬂected expansion wave or cavitation
area still maintains upstream movement after cavitation begins. If cavitation continues
to absorb energy from the expansion wave and expands after cavitation onset, then the
cavitation bubble’s location should approach the droplet’s right-hand side. Conversely, if
the cavitation zone or emitted wavelet can move upstream, distanced from the NPP point,
then the cavitation bubble should be farther from the right-hand side of the droplet. The
inconsistency between our NPP point, derived from numerical simulations, and the focus
point from theoretical analysis by Biasiori-Poulanges & El-Rabii ( 2021)a n dX u et al.
(2023), suggests that the reﬂected expansion wave’s focus may not always lead to negative
pressure occurrence. Further details on this discrepancy are discussed in § 5.1.
988 A46-10
https://doi.org/10.1017/jfm.2024.472
 Published online by Cambridge University Press

<!-- PDF_PAGE: 11 -->

Exploration of shock–droplet interaction
Incident
shock wave
Q1
Q2
θ
θ
θ
β
M
r
Q0
λ1
Figure 6. Schematic diagram of the original theoretical model (refer to Biasiori-Poulanges & El-Rabii 2021).
To unravel diverse trends under varying gas–liquid wave velocity ratios, the next
subsection enhances and employs a theoretical model founded on the ray-tracing method.
4. Improvement to the theoretical model
4.1. The original theoretical model
The theoretical analysis proposed in Cerven `y( 2001) and subsequently utilized by
Biasiori-Poulanges & El-Rabii (2021)a n dX uet al. (2023) employs the ray-tracing method
to elucidate the wave transmission within the droplet. Figure 6 illustrates the schematic
diagram of the initial theoretical model based on the ray-tracing method. This model
operates under four fundamental assumptions (Biasiori-Poulanges & El-Rabii 2021;X u
et al. 2023):
Assumption 1. As shock waves engage with a droplet, the droplet’s corresponding
location initiates
a disturbance. The wavelet will spread at the speed of sound with the
disturbance, and the effect of the wavelet on the wavefront can be simpliﬁed as rays
according to Biasiori-Poulanges & El-Rabii ( 2021)a n dX u et al. (2023). The location
of the disturbance β and the direction of ray propagation θ should follow
sinθ= sin β/n. (4.1)
Assumption 2. Only rays with a generation speed exceeding the propagation speed will
impact the envelope of the transmitted wave within the droplet :
β<β c = arcsin(n), (4.2)
where βc is the critical angle used to distinguish the areas that can affect the envelope.
It should be noted that the critical angle differs from the limiting angle. The limiting
angle is deﬁned as the angle from the shock regular reﬂection to the occurrence of Mach
stem according to Vijayashankar, Kutler & Anderson ( 1976). The limiting angle obtained
in our numerical simulation results is approximately 48
◦, similar to the 46 ◦ given by
988 A46-11
https://doi.org/10.1017/jfm.2024.472
 Published online by Cambridge University Press

<!-- PDF_PAGE: 12 -->

T. Xiong, C. Shao and K. Luo
G e v a ,R a m&S a d o t(2018). The critical angle mentioned in the present work is a variable
that varies with the gas–liquid wave velocity ratio.
Assumption 3. The positions where the internal rays reach the droplet boundary ﬁrst and
second, denoted as Q1 and Q2, are
λ1 = 2θ− β, (4.3)
λ2 = π + 4θ− β, (4.4)
where θrepresents the initial direction of the rays upon entering the droplet, also signifying
the angle at each reﬂection.
Assumption 4. The correlation between the trajectory of rays and time has been studied
by Biasiori-Poulanges & El-Rabii ( 2021)a n dX u et al. (2023):
t = tS(β) + 2( j − 1) r
ul
cos θ+
lQj− 1M
ul
, (4.5)
tS(β) = r
ul
(1 − cosβ), (4.6)
where j represents the number of reﬂections within the liquid droplet, lQj− 1M indicates
the distance between the point where the liquid droplet reﬂects j − 1 times, Qj− 1,a n dt h e
current location , M. Equation ( 4.5) features three components: tS(β) signiﬁes the time
necessary for the incident shock wave to reach a location β on the droplet boundary; the
second component involves the time for ray propagation along the path Qj− 2Qj− 1;a n d
the third component reﬂects the time for ray propagation from the initial contact with the
droplet boundary to the current point M. By determining and connecting the positions M
of all rays at a chosen time t, the envelope of the wave is established. Furthermore, the
disparity in expressions for ul between (4.5) and (4.6) is expounded upon in Appendix D.
4.2. The limitation of the original theoretical model
The numerical schlieren images under varying shock Mach numbers are displayed in
ﬁgure 7, illustrating the progression of the Mach stem as the incident shock wave traverses
from left to right. The interaction with the droplet surface triggers disturbance at speciﬁc
points, distinguished by a blue line (disturbed)
versus a red line (undisturbed). These
disturbances extend to form the shock envelope (wavefront) indicated as the transmitted
wave in ﬁgure 7 .I n ﬁgure 7 (a), due to a low gas–liquid wave velocity ratio, the critical
angle, as per ( 4.2) in Assumption 2, governing the transmitted wave’s formation is
relatively minimal. Here, a distinct separation exists between the Mach stem or the incident
shock wave and the transmitted wave, indicating that disturbances beyond the critical angle
do not signiﬁcantly impact the wavefront’s construction. Consequently, at low gas–liquid
wave velocity ratios, whether it be the incident shock wave or the Mach stem dictating
disturbance onset, the internal wave structure within the droplet remains largely consistent.
With an escalation in the gas–liquid wave velocity ratio, the concavity of the transmitted
wave intensiﬁes gradually, and the gap between the incident shock wave and the Mach
stem, reaching the droplet, widens. The Mach stem assumes a pivotal role in triggering
disturbances. In ﬁgure 7 (d), the incident shock wave has moved to the right of the
right pole of the droplet, underscoring the Mach stem’s continued connection to the
droplet, with select points yet to experience any disturbance. The original theoretical
988 A46-12
https://doi.org/10.1017/jfm.2024.472
 Published online by Cambridge University Press

<!-- PDF_PAGE: 13 -->

Exploration of shock–droplet interaction
With
disturbance
Without
disturbance
(b)(a)
(c)( d )
Figure 7. Comparison of the numerical schlieren between low and high velocity ratios with n-hexane as liquid
phase. The blue and red lines denote the interfacial regions with disturbance by waves and without disturbance,
respectively. (a) Ms 2.4, n = 0.755, t
∗ = 0.848, ( b) Ms 3.0, n = 0.943, t∗ = 0.810, (c) Ms 4.8, n = 1.509,
t∗ = 0.504, (d) Ms 4.8, n = 1.509, t∗ = 0.756.
model utilizing solely the incident shock wave as the disturbance initiator is incongruent
with scenarios involving high gas–liquid wave velocity ratios. Consequently, the factor
governing disturbance onset ought to transition from the incident shock wave to the Mach
stem.
4.3. Improvement to the original theoretical model
The subsequent discussion will elaborate on the replacement of the controlling factor for
the onset of disturbance from the incident shock wave with the Mach stem. The core
concept involves substituting the ﬁrst term of (4.5) in Assumption 4 as delineated in § 4.1,
denoted as tS(β), representing the time necessary for the incident shock wave to reach
point β on the droplet, with tM(β), denoting the time required for the Mach stem to reach
the same point on the droplet. Insight into the Mach stem’s behaviour can be gleaned
through post-processing of numerical simulation results, enabling the ﬁtting of the Mach
stem trajectory β(t
M) and the derivation of the inverse function to determine tM(β).
Observing ﬁgure 8 , the trajectories of the Mach stem closely align with temporal
variations at various Mach numbers. In ﬁgure 8 (a), the spatial positioning of the Mach
stem trajectory within the Cartesian coordinate framework is presented. The spatial
coordinates are non-dimensionalized by the initial droplet diameter D0,s ot h es h a p ei s
roughly like a circular shape enveloping the liquid droplet. The start of observation of the
988 A46-13
https://doi.org/10.1017/jfm.2024.472
 Published online by Cambridge University Press

<!-- PDF_PAGE: 14 -->

T. Xiong, C. Shao and K. Luo
0 200
60
90
120
β (deg.)
150
180
400 600
T
800 1000
Fitting
Shock
1.21.00.8
x/D0
y/D0
0.60.40.2–0.2–0.4
0
0.2
0.4
0.6
0.8 Ms 2.4
Ms 3.0
Ms 3.6
Ms 4.2
Ms 4.8
Ms 5.4
Ms 6.0
Ms 6.6
Ms 7.2
Ms 7.8
Ms 8.4
Ms 2.4
Ms 3.0
Ms 3.6
Ms 4.2
Ms 4.8
Ms 5.4
Ms 6.0
Ms 6.6
Ms 7.2
Ms 7.8
Ms 8.4
1.0
1.2
0
(b)
(a)
Figure 8. Trajectory of Mach stem with different Ms,i n( a) Cartesian coordinate system, ( b) polar coordinate
system. The black line is the ﬁtting expression for the improved model. The red line is the shock trajectory used
in the original model for comparison here.
Mach stem is represented by the leftmost point, while detachment occurs as it reaches the
droplet’s right extremity, illustrated as the rightmost point in ﬁgure 8(b).
The Mach stem’s trajectory is estimated by multiplying speed by time. In numerical
simulations, time t equates to the product of the time step N and the time step size d t,
leading to the representation of the Mach stem’s trajectory as L = uN dt. The time step
size d t in this analysis is inferred to be inversely related to the shock Mach number Ms,
denoted as dt ≈ O(Ms− 1),w i t ht h ederivation
dt = CFL × dx√1.4ppost/ρair
, (4.7)
988 A46-14
https://doi.org/10.1017/jfm.2024.472
 Published online by Cambridge University Press

<!-- PDF_PAGE: 15 -->

Exploration of shock–droplet interaction
where CFL,d x, ppost and ρair are the CFL number, grid spatial resolution, pressure of
post-shock air and density of pre-shock air, respectively. They are all constants except
ppost, which has expression
ppost
ppre
= 2γair(M2
s − 1)
γair + 1 + 1, (4.8)
where ppre and γair are constant pressure of pre-shock air, and speciﬁc heat ratio of air in
table 2, respectively. Now ppost can be taken into d t to get
dt = 1.810× 10− 7
√
2.8M2s − 0.4
. (4.9)
Due to the phenomenon that the Mach stem always stays close to the incident shock wave
that has velocity Ms, the motion speed of the Mach stem is believed to be proportional
to the shock Mach number, which is u ≈ O(Ms). Therefore, in the present numerical
simulation, the inﬂuence of the shock Mach number on the motion trajectory of the
Mach stem can be eliminated due to the multiplication of the time step and the motion
speed, resulting in the phenomenon that the motion trajectory of the Mach stem at
different shock Mach numbers is approximately at the same spatial position at the same
time step. Therefore, only a set of Mach stem is needed to ﬁt the β(t
M) function. The
non-dimensional time TM can be expressed as
TM = tM
dt . (4.10)
By ﬁtting the Mach stem trajectory in ﬁgure 8(b), we obtain the scaling law for all Mach
numbers as
β = f(TM) =− 8 × 10− 5(TM)2 + 0.2337TM + 30.531. (4.11)
After obtaining the motion trajectory of the Mach stem β = f(TM), take its inverse
function
TM = f− 1(β) = 1458.75−
√
2.51× 106 − 1.25 × 104β, (4.12)
and take (4.9) and (4.10) into (4.12)t o get
tM = 2.64 × 10− 4 −
√
8.223 × 10− 8 − 4.095 × 10− 10β√
2.8M2s − 0.4
. (4.13)
Replace the ﬁrst term of (4.5) in Assumption 4 to obtain
t = 2.64 × 10− 4 −
√
8.223 × 10− 8 − 4.095 × 10− 10β√
2.8M2s − 0.4
+ 2(k − 1) r
ul
cos θ+ lQK− 1M
ul
. (4.14)
By applying (4.14) to determine the ending rays for wavefront formation, the consideration
of the Mach stem’s impact is included. Appendix E addresses the implications of
employing various trajectory ﬁtting functions for the Mach stem.
988 A46-15
https://doi.org/10.1017/jfm.2024.472
 Published online by Cambridge University Press

<!-- PDF_PAGE: 16 -->

T. Xiong, C. Shao and K. Luo
(b)(a)
(c)( d )
Figure 9. Comparison of numerical schlieren results (top part of image) and the theoretical results (bottom
part) in the same instant, for Ms = 4.8, in (a,b) the original model and ( c,d) the improved model. The blue line
denotes the wave structure predicted by the theoretical model, and the red dashed line denotes the Mach stem
location at the droplet surface. Times are ( a,c) t
∗ = 0.630, (b,d) t∗ = 0.840.
Figure 8 (b) contrasts the reﬁned expression (shown as the black line) with the initial
expression (depicted in red, derived from ( 4.6)). The discrepancy is minimal until β
approaches approximately 110◦, indicating that disregarding the Mach stem’s effect has
negligible consequences on theoretical analyses when the angle deﬁned by ( 4.2) in
Assumption 2 is below 110◦, particularly at low wave velocity ratios. Subsequently, the
disparity between the two models widens notably due to curvature effects. The enhanced
model aligns more closely with real-world scenarios compared to the original version, a
topic elaborated on in the next subsection.
4.4. Results of the improved theoretical model
Figure 9 presents a comparison between the original model and the enhanced model
alongside the numerical simulation results in two snapshots. The top section displays
the numerical schlieren, while the theoretical analysis results from the original model
(
ﬁgures 9a,b) and the improved model ( ﬁgures 9c,d) are shown below. In the theoretical
analysis, the blue line inside the droplet denotes the location of the transmitted shock
wave, derived from the disturbances’ ray ends. The blue line outside the droplet indicates
988 A46-16
https://doi.org/10.1017/jfm.2024.472
 Published online by Cambridge University Press

<!-- PDF_PAGE: 17 -->

Exploration of shock–droplet interaction
the location of the incident shock wave. The red dashed line marks the current position of
the starting disturbance, with the blue dashed line serving as an extension of the incident
shock wave to highlight the inadequacy of solely employing it to trigger disturbances. The
black circle signiﬁes the droplet.
In ﬁgure 9 , it is important to highlight that the current numerical schlieren results
demonstrate the presence of the carbuncle phenomenon. This type of shock facility,
aligned with the grid, can be addressed effectively by employing the approaches proposed
by Fleischmann, Adami & Adams ( 2020).
The incorporation of the Mach stem factor in the theoretical model markedly enhances
its alignment with the numerical simulation results in ﬁgures 9 (c,d). For instance,
comparing ﬁgures 9(b,d), when using the incident shock wave as the disturbance initiation
control factor in the previous model, the entire droplet exhibits disturbance at the selected
moment, as depicted in the bottom of ﬁgure 9(b). In contrast, numerical simulation results
in the top of ﬁgure 9 (b) reveal some undisturbed points on the droplet. By employing
the Mach stem as the governing factor in the improved model, illustrated in ﬁgure 9 (d),
the distribution state of the disturbance in the droplet at the chosen moment can be
reconstructed accurately.
As shown in ﬁgure 10 , the internal wave structures of the droplet at the time of the
NPP obtained through the improved model closely align with the numerical simulation
results. Here, βref,k represents the disturbance angle with k reﬂections of the ray. Previous
research (Wu et al. 2018; Biasiori-Poulanges & El-Rabii 2021;X u et al. 2023) indicates
that the one-time reﬂected rays are responsible for generating negative pressure; therefore,
other rays are not considered in this ﬁgure.
Figures 10(a,c) depict a lower gas–liquid wave velocity ratio using air as the gas and
n-hexane as the liquid with Ms = 2.4, while ﬁgures 10(b,d) display a higher gas–liquid
wave velocity ratio with Ms = 4.8. For instance, comparing ﬁgures 10 (b,d), where
ﬁgure 10(b) showcases the numerical simulation result of the numerical schlieren at the
onset of the NPP, the theoretical result from the enhanced model at the same instance is
illustrated in ﬁgure 10(d). In ﬁgure 10(d), the red dot signiﬁes the NPP point’s location
derived from numerical simulation, while the blue line represents the shock envelope
formed by each disturbance derived through the improved model. Notably, many rays that
underwent once reﬂection converge at the NPP point’s location. The agreement between
the numerical simulation’s NPP point’s location and the theoretical analysis at the speciﬁc
instant is apparent.
Although the focus of the expansion wave indeed induces pressure reduction and is
closely linked to the NPP, the reasons for the divergence in the NPP point’s location trend
compared to that of Biasiori-Poulanges & El-Rabii ( 2021)a n dX u et al. (2023) remain
unidentiﬁed.
5. Mechanism of the NPP formation
5.1. Difference between the NPP and focus points
Figure 5 illustrates that the NPP point’s locations indicated by numerical simulations
align with the theoretical results from Biasiori-Poulanges & El-Rabii ( 2021) under
low gas–liquid wave velocity ratios. However, a substantial variance emerges at higher
gas–liquid wave velocity ratios. To analyse the reasons for this distinction, an improved
theoretical model is employed to deduce the focus points at varying gas–liquid wave
velocity ratios. This study deﬁnes the focus point obtained through theoretical analysis
as the instant when the quantity of reﬂected waves traversing the central axis peaks within
988 A46-17
https://doi.org/10.1017/jfm.2024.472
 Published online by Cambridge University Press

<!-- PDF_PAGE: 18 -->

T. Xiong, C. Shao and K. Luo
(b)(a)
(c)
βref,2
βref,0βref,1βref,1
(d )
Figure 10. Comparison of the NPP point between ( a,b) numerical schlieren and ( c,d) theoretical analysis, for
Ms = 4.8. The red dot is the NPP point obtained through numerical results, the blue line is the wavefront, and
the yellow lines are the rays from disturbance inside the droplet. Only the rays within the angle βref,1 are drawn.
Times are (a,c) t∗ = 1.25, (b,d) t∗ = 1.14.
a speciﬁc range. At this moment, the location of the central axis wavefront is termed the
focus point. As depicted in ﬁgure 11, the focus point is identiﬁed as the leftmost position
of the wavefront (denoted by the blue line) within a range selected from one-fortieth to
one-twentieth of the diameter, i.e. R = D0/a, a ∈ [20, 40].
The temporal evolution of the number of reﬂected waves (the time scale is equivalent to
(4.10)) is portrayed in ﬁgure 12, with the dashed line indicating the instant when the NPP
emerges, as determined by numerical simulations. For shock Mach number 2.4, regardless
of the range size a, the focusing time – marked by the maximum number of reﬂected
waves – aligns closely with the NPP moment, suggesting congruence between the NPP
and focus points in scenarios with lower wave velocity ratios. This ﬁnding supports the
inference that the convergence of expansion waves can lead to pressure reduction under
lower
gas–liquid wave velocity ratios. Conversely, with shock wave Mach number 3.6,
discrepancies between the focusing and NPP times grow; better alignment is observed with
smaller ranges. At shock wave Mach numbers 5.4 and 8.4, signiﬁcant deviations between
988 A46-18
https://doi.org/10.1017/jfm.2024.472
 Published online by Cambridge University Press

<!-- PDF_PAGE: 19 -->

Exploration of shock–droplet interaction
(b)
D0/40
D0/20
(a)
Wavefront
Figure 11. The deﬁnition of focus in the selected region in the theoretical model.
1.0
0
0
0.1
0.2
0.2
0.4
0.6
0.8
0.3
0.4
0.5
0
0.1
0.2
0.3
0.4
0.5
a = 20 a = 25 a = 30 a = 35 a = 40 t
∗NPP
kinc/Kk inc/K
1.2 1.4 1.6 1.8
1.2 1.4 1.6 1.8 2.0 1.2 1.0 1.4 1.6 1.8 2.0
1.00.8
0.20
0.15
0.10
0.05
0
1.2 1.4 1.6 1.8
(b)(a)
(c)( d )
t∗t∗
Figure 12. Comparison of the NPP and focus points for three selected shock Mach numbers with n-hexane
as the liquid. The black dashed line is the instant when the NPP happens, kinc is the number of reﬂected
waves in the selected region, and K is the total number of reﬂected waves. Here, ( a) Ms = 2.4, (b) Ms = 3.6,
(c) Ms = 5.4, (d) Ms = 8.4.
focusing and NPP times occur across all selected range sizes, indicating non-coincidence
of the NPP and focus points for elevated gas–liquid wave velocity ratios. Notably, at
Ms = 8.4, the ray promptly focuses near the right-hand wall of the droplet post-reﬂection,
inducing a sudden shift in the focus degree ( kinc/K)f r o m0, as illustrated in ﬁgure 12(d).
This observation demonstrates that the pressure decline at the focus point instigated by
expansion waves fails to drive the pressure to its minimum, i.e. the NPP value.
Figure 13 contrasts the focus point locations derived from the improved theoretical
model with the NPP point location from numerical simulations, the theoretical predictions
by Biasiori-Poulanges & El-Rabii ( 2021)a n dX u et al. (2023), and the experimental
988 A46-19
https://doi.org/10.1017/jfm.2024.472
 Published online by Cambridge University Press

<!-- PDF_PAGE: 20 -->

T. Xiong, C. Shao and K. Luo
1.0 1.5
n
L
2.0 2.5 3.00.50
0
0.05
0.10
0.15
0.20
0.25
0.30
0.35
Focus
Simulation (n-hexane)
Simulation (water)
Biasiori-Poulanges & Schmidmayer (2023)
Biasiori-Poulanges & El-Rabii (2021)
Sembian et al. (2016)
Figure 13. Comparison of the focus point, the NPP point with water and n-hexane as liquid phase, the
theoretical results by Biasiori-Poulanges & El-Rabii ( 2021), and the experimental results by Sembian et al.
(2016).
ﬁndings of Sembian et al. (2016). The horizontal axis replaces the shock Mach number
Ms with the gas–liquid wave velocity ratio n. It unveils that our improved theoretical
forecast of the focus point’s position aligns closely with the theoretical prediction by
Biasiori-Poulanges & El-Rabii ( 2021)a tt h el o wn region.
Our focus locations, along with data from Biasiori-Poulanges & El-Rabii ( 2021)a n d
Biasiori-Poulanges & Schmidmayer ( 2023), exhibit a consistent downward trend with
increasing gas–liquid wave velocity ratios. Observably, under lower gas–liquid wave
velocity ratios, the NPP point lies between our focus spot and the Biasiori-Poulanges
&E l - R a b i i(2021) estimate, emphasizing its dependence solely on the gas–liquid wave
velocity ratio rather than the liquid phase (water or n-hexane) selected. As the gas–liquid
wave velocity ratio escalates, disparities between focus point and NPP point’s location
emerge. High gas–liquid wave velocity ratios prompt numerical simulations to revert
to a constant NPP point’s location, aligning with the observations of Sembian et al.
(2016).
In conclusion, the convergence of expansion waves contributes to pressure reduction at
lower gas–liquid wave velocity ratios. However, at elevatedgas–liquid wave velocity ratios,
the pressure decrease arising from the expansion wave’s focus point fails to reach the
minimum necessary to designate this spot as an NPP point. Understanding the mechanism
behind the generation of minimum pressure at NPP points entails comprehensive scrutiny
of pressure-altering factors beyond solely expansion waves at the NPP and focus points.
5.2. Factors of the pressure variation
Initially, the pressure variation within the droplet during the early stages of
shock–droplet
interaction is categorized into four phases: the shock wave effect, relaxation effect,
ﬂuctuation effect and expansion wave effect, as illustrated in ﬁgure 14. As the transmitted
988 A46-20
https://doi.org/10.1017/jfm.2024.472
 Published online by Cambridge University Press

<!-- PDF_PAGE: 21 -->

Exploration of shock–droplet interaction
0
0
–1.1
1.1
Pressure (MPa)
2.2
0.5 1.0 1.5
Shock wave effect
Expansion wave effect
Relaxation effect
&
Fluctuation effect
2.0
t∗
Figure 14. The typical variation of pressure and its classiﬁcation at point (− D0/8, 0) inside the droplet.
0 1.8
P (MPa)
01 5
P (MPa)
(b)(a)
Figure 15. Fluctuation effect in ( a) low wave velocity ratio (Ms = 2.4) and (b) high wave velocity ratio (Ms =
4.). The numerical schlieren is shown in the upper part of the image, and the pressure contour is shown in the
lower part.
wave traverses a point inside the droplet, for example, slightly to the left of the origin at
− D0/8, the pressure sharply escalates at that speciﬁc location, as observed in the studies
by Sembian et al. (2016), Biasiori-Poulanges & El-Rabii (2021), Xu et al. (2023) and Xiang
&W a n g(2017). Subsequently, owing to uneven pressure distribution within the droplet,
this point gradually aligns with the neighbouring pressure, characterizing what we term
the relaxation effect in this investigation.
Demonstrated in ﬁgure 15, the ﬂuctuation effect arises from sustained high pressure on
the droplet’s upstream side, exempliﬁed by Ms = 2.4 and 4.8 for low and high gas–liquid
wave velocity ratios, respectively. Following the interaction of the external incident shock
wave with the droplet, a region of heightened pressure forms diametrically opposite to
the incident direction, inducing periodic pressure surges downstream, particularly at the
droplet’s
centre. This ﬂuctuation phenomenon is also noted in the experimental studies of
988 A46-21
https://doi.org/10.1017/jfm.2024.472
 Published online by Cambridge University Press

<!-- PDF_PAGE: 22 -->

T. Xiong, C. Shao and K. Luo
0 0.5 1.0 1.5 2.0
t∗
0 0.5 1.0 1.5 2.0
0
–4
–2
2
–D/4 – D/8 D/8 D/4 NPP Focus0
10
–10
–20
00
20
Pressure (MPa) Pressure (MPa)
10
–10
20
40
–40
0
–20 –20
–30
0
0.5 1.0 1.5 2.0 0 0.5 1.0 1.5 2.0
t∗
(b)(a)
(c)( d )
Figure 16. Temporal pressure variation at different points ( x =− D0/4, − D0/8, 0, D0/8, D0/4, NPP point,
focus point) in the n-hexane droplet at different cases, with ( a) Ms = 2.4, ( b) Ms = 4.2, ( c) Ms = 4.8,
(d) Ms = 5.4.
Sembian et al. (2016). In the research by Schmidmayer & Biasiori-Poulanges ( 2023), the
existence of the ﬂuctuation effect is observable irrespective of whether the droplets are
cylindrical or spherical.
Nevertheless, the ﬂuctuation effect is relatively minor in contrast to the impact of the
shock wave. Subsequently, reaching this point, the expansion wave triggers a substantial
pressure decrease. What follows is the natural evolution, encompassing ﬂuctuation
pressure inﬂuences, eventually stabilizing the pressure from its negative peak value.
This marks the completion of a cycle. When the expansion wave strikes the wall
edge and reﬂects, the subsequent traversal through that point initializes the ensuing
cycle.
Figure 16 provides a depiction of the pressure distribution over time at various
points along the central axis at different shock Mach numbers. Each selected point
experiences the four delineated processes before the second convergence of the wave
system: shock effect, ﬂuctuation effect, relaxation effect and expansion wave effect.
Notably, in ﬁgure 16(a), as the point nears the droplet’s downstream side, the pressure
increment from the shock wave’s impact diminishes. Conversely, with an escalation in
the shock Mach number, as demonstrated in ﬁgure 16(d), when the point approaches the
droplet’s downstream region, the pressure surge induced by the shock wave intensiﬁes
considerably.
5.2.1. Shock effect
The shock wave effect phenomenon can be elucidated through theoretical analysis models
to derive the internal wave system structure corresponding to the scenarios depicted
in
ﬁgures 16(a,d). In ﬁgure 17, two observation points are selected, − D0/4a n d D0/4f r o m
the droplet’s origin, to exemplify the comparison between shock Mach numbers 2.4 and
5.4. The internal wave structure is illustrated when the ray from the droplet’s left pole
reaches the observation point. For a lower gas–liquid wave velocity ratio ( ﬁgures 17a,b),
988 A46-22
https://doi.org/10.1017/jfm.2024.472
 Published online by Cambridge University Press

<!-- PDF_PAGE: 23 -->

Exploration of shock–droplet interaction
(b)(a)
(c) (d )
Figure 17. Theoretical analysis of shock effect at the points ( a,c) x =− D0/4, (b,d) x = D0/4, with shock
Mach numbers (a,b) Ms = 2.4, (c,d) Ms = 5.4.
the rays emitted from the disturbed part of the droplet, impacting the envelope surface of
the internal waves (now a transmitted wave), exhibit an outward propagation angle.
Consequently, the envelope surface shows a convex shape, termed diverging cases by
Boyd & Jarrahbashi ( 2021). Since the selected points in ﬁgure 16 lie on the central
axis, moving downstream results in the surrounding rays propagating outwards, gradually
moving away from the central axis, reducing the impact from the rays. Hence in instances
of lower gas–liquid wave velocity ratios, as depicted in ﬁgure 16(a), the pressure increase
caused by the shock wave effect decreases as the point moves closer to the downstream
wall of the droplet.
Conversely, when considering higher
gas–liquid wave velocity ratios (ﬁgures 17c,d), the
inward propagation angle of emitted radiation from the disturbance creates a concave shape
on the envelope surface, termed converging cases by Boyd & Jarrahbashi ( 2021). As the
observation point shifts to the right, the inﬂuence of each ray intensiﬁes. Consequently,
under a high
gas–liquid wave velocity ratio illustrated in ﬁgure 16 (d), points near the
downstream wall experience a more pronounced pressure increase due to the shock wave
effect.
5.2.2. Fluctuation effect
Observing ﬁgure 15 reveals that the source of ﬂuctuation is the high-pressure region
upstream of the droplet. Examination of ﬁgure 16 shows that when focusing on a speciﬁc
shock Mach number, the amplitude of pressure ﬂuctuations caused by the ﬂuctuation effect
increases as the chosen point approaches the high-pressure region near the upstream wall.
The shorter propagation distance and weaker attenuation of high-pressure compression
waves near the left point lead to a longer and stronger ﬂuctuation effect due to the time gap
between the shock wave and reﬂected expansion wave effects. Therefore, if the relaxation
988 A46-23
https://doi.org/10.1017/jfm.2024.472
 Published online by Cambridge University Press

<!-- PDF_PAGE: 24 -->

T. Xiong, C. Shao and K. Luo
effect remains constant, then the point being closer to the upstream wall results in a
lower pressure drop caused by the combined effects of ﬂuctuation and relaxation at that
speciﬁc point. Conversely, distancing the selected point from the high-pressure region of
the upstream wall shortens the duration and intensity of experienced ﬂuctuation effects,
leading to a more rapid decline in pressure.
In considering the phenomenon where pressure ﬂuctuations are not observable
following a sudden pressure drop due to the expansion wave effect on a droplet, we can
explain that the ﬂuctuation effect operates by periodically emitting compression waves
near the droplet’s upstream wall. These waves sweep across the chosen point, inducing
a pressure increase. While the droplet undergoes a rapid decline, the selected point is
within the expansion wave’s inﬂuence. The downstream transmission of the ﬂuctuation
effect from the high-pressure zone upstream of the droplet does not directly impact the
point because it ﬁrst encounters the expanding wave. Consequently, during the period of
pressure decline and recovery at the chosen point, signiﬁcant ﬂuctuations are not visually
discernible.
With the same liquid phase, as the shock Mach number increases, the
gas–liquid velocity
ratio increases, and the pressure change caused by the ﬂuctuation effect weakens relative
to other factors. Notably in ﬁgure 16(d), the intensity of the ﬂuctuation effect weakens in
contrast to instances with lower gas–liquid wave velocity ratios, with noticeable pressure
ﬂuctuation changes limited to points near the high-pressure area of the droplet’s upstream
wall. Particularly for the point along the droplet’s downstream wall, due to its distance
from the source of ﬂuctuation in the high-pressure region and exposure to expansion
wave effects shortly after encountering shock waves, the impact of upstream ﬂuctuation
is constrained. This limitation occurs because the effect weakens over distance
,a n d
the barrier between shock and expansion waves prevents direct inﬂuence on the point,
emphasizing that higher shock Mach
numbers reveal ﬂuctuation impacts only near the
high-pressure source region.
5.2.3. Relaxation effect
The relaxation effect can be understood as a downward trend within the droplet when the
internal point experiences relatively high pressure or an upward trend in the presence of
lower pressure. Focusing on a single research point within the droplet, the initial exposure
to a shock wave results in maximum pressure at that location. Given the high-pressure
environment around the speciﬁc point, the relaxation effect prompts pressure reduction,
counteracted intermittently by the upstream ﬂuctuation effect
that makes the pressure raise.
In this scenario, the ﬂuctuation effect impedes the relaxation effect’s pressure reduction.
When the point inside the droplet is impacted by the reﬂected expansion wave, the
pressure reaches a minimum value. The low pressure leads to a relatively small pressure
at the speciﬁc point compared to other points, resulting in the relaxation effect acting as
a pressure booster. At the same time, the ﬂuctuation effect, affecting points signiﬁcantly
impacted by it, drives further pressure increase. Consequently, the ﬂuctuation effect fosters
the rise of the relaxation effect.
Upon reaching the maximum pressure at the discussed point, the opposing forces of
relaxation
(causing pressure reduction ) and ﬂuctuation (driving pressure elevation )c o m e
into play. During this phase, the rate of pressure decline slows down. Conversely, once the
minimum pressure is reached at the discussed point, both effects contributing to pressure
elevation align, resulting in a swifter increase in pressure.
Thus in ﬁgure 16, the duration
required for pressure to return from the maximum value to a steady state exceeds the time
needed for the pressure to rise from the minimum value to equilibrium.
988 A46-24
https://doi.org/10.1017/jfm.2024.472
 Published online by Cambridge University Press

<!-- PDF_PAGE: 25 -->

Exploration of shock–droplet interaction
In scenarios where different points experience the same shock Mach number, such
as the case under discussion, when points near the upstream of the droplet undergo
the shock wave effects, the surrounding points often remain unaffected by the shock
waves, maintaining extremely low pressure levels. This condition accentuates the pressure
disparity, enhancing the impact of the relaxation effect signiﬁcantly. In contrast, when
the shock effects reach downstream points, the surrounding area typically sustains a
high-pressure state, resulting in a diminished pressure gap and weaker relaxation effects.
In summary, prior to a pronounced decrease in pressure following the peak impact
of the shock wave within the droplet, a comprehensive evaluation of the ﬂuctuation
and relaxation effects becomes imperative. During this phase, the pressure drop ( /Delta1P =
/Delta1P
ﬂu − /Delta1Prel) comes into focus. Comparing the upstream and downstream points, the
ﬂuctuation effect is more pronounced at the upstream location, with a longer duration
of impact ( /Delta1Pﬂu is larger). Additionally, owing to the heightened pressure discrepancy
with neighbouring points, the relaxation effect is also more pronounced ( /Delta1Prel is larger).
While the ﬂuctuation effect drives pressure elevation, the relaxation effect leads to
pressure reduction. Hence establishing the pressure differential between upstream and
downstream points under the amalgamated inﬂuence of both effects proves challenging
through simplistic reasoning.
Nevertheless, as depicted in ﬁgure 16 (c), the analysis of several points at
x =− D0/4, − D0/8, 0, D0/8, D0/4 indicates an upward trend in the combined impact
of ﬂuctuation and relaxation effects (pressure drop /Delta1P) within the upstream section
delineated by x = D0/4 as the selected point progresses rightwards. That is, as the selected
point shifts towards the right, the pressure signiﬁcantly diminishes. Furthermore, from the
comparison of x = NPP, Focus, it can be seen that as the discussed point shifts to the
right, the pressure drop is smaller.
Therefore, it can be considered that at the right of a critical point, due to the rapid
alternation of shock waves and expansion waves, the upstream high-pressure ﬂuctuations
cannot be directly contacted, and the ﬂuctuation effect can be ignored. Despite this, the
persistence of low pressure downstream maintains a pressure differential, sustaining the
impact of the relaxation effect. At the right of the critical point, the upstream point has a
stronger relaxation effect than the downstream point, and the ﬂuctuation effect is ignored,
resulting in a stronger pressure drop.
5.3. Decreasing pressure caused by the reﬂected expansion wave
In the preceding
subsection, it was observed that the focus of the reﬂected expansion
wave does not inevitably result in the formation of NPP points in high gas–liquid wave
velocity ratios, thus suggesting that it may not be the cause of cavitation. Furthermore, it
is proposed that during the initial stage of shock–droplet interaction, the pressure variation
within the droplet can be delineated into four phases: shock wave effect, ﬂuctuation effect,
relaxation effect and expansion wave effect.
What follows
ﬁrst deﬁnes the pressure decrease contribution caused by expansion waves
in the pressure variation curve, /Delta1Pexp, and compares it with the number of reﬂected
waves obtained from the improved theoretical model. This comparison is employed to
illustrate quantitatively that the pressure reduction attributed to reﬂected expansion waves
constitutes just one component of the overall pressure decline. Noteworthy is the fact that
focusing represents only the maximum pressure drop caused by the reﬂected expansion
wave at that point, and it may not necessarily lead to the NPP considering the pressure
variation with the four parts of the factors.
988 A46-25
https://doi.org/10.1017/jfm.2024.472
 Published online by Cambridge University Press

<!-- PDF_PAGE: 26 -->

T. Xiong, C. Shao and K. Luo
0
–5
–4
–3
–2
First derivative of pressure (Pa s–1)
–1
1
2
3
(×1013)
0
0.5
NPP
0
–D0/4
D0/4
1.0 1.5 2.0 2.5
t1 t2 t3
t∗
Figure 18. First derivative of pressure and the deﬁnition of decreasing pressure caused by a reﬂected
expansion wave for Ms = 4.2.
Upon scrutinizing the pressure trend depicted in ﬁgures 14 and 16, the straightforward
approach to discern whether the pressure descent stems from the relaxation effect or the
expansion wave is by evaluating its rate of decline. A prominent slope in the pressure trend
indicates the impact of the expansion wave , as illustrated by the ﬁrst-order derivative plot
of pressure against time for the case Ms = 4.2 displayed in ﬁgure 18.
After being subjected to the shock wave and increasing signiﬁcantly, the pressure
decreases at a relatively stable speed under the inﬂuence of relaxation and ﬂuctuation. For
a more reﬁned differentiation between the effects of expansion waves and relaxation, this
study introduces the deﬁnitions of the initiation time t1 and cessation time t3 of expansion
wave inﬂuence. Here, the initiation time marks the instance when the initial trough
preceding the minimum value of the ﬁrst pressure derivative (t2) transpires. Conversely, the
cessation time denotes the moment when the ﬁrst derivative of pressure ﬁrst attains zero
subsequent to reaching its minimum ( t2). The pressure drop between t1 and t3 attributed to
the reﬂection of expansion waves is denoted as /Delta1Pexp.
In ﬁgure 19, the comparison between the pressure drop /Delta1Pexp from reﬂected expansion
waves at speciﬁc points and the total pressure drop /Delta1Ptotal from the maximum pressure
post-shock wave to the minimum pressure post-expansion wave is depicted. The ratio of
reﬂected waves k
inc/K is illustrated as well. Here, kinc represents the reﬂected waves at
the selected point, indicating the strength of focusing, while K denotes the total number
of waves, including those with multiple reﬂections or no reﬂection. Notably, as the point
approaches the right-hand boundary of the droplet, both the number of reﬂected waves
(k
inc) and the pressure drop from the expansion wave ( /Delta1Pexp) become more pronounced.
Particularly in ﬁgures 19 (a,b), the variations in kinc and /Delta1Pexp across all locations
are closely aligned, suggesting that the reﬂected expansion wave signiﬁcantly inﬂuences
/Delta1Pexp. In the study by Schmidmayer & Biasiori-Poulanges ( 2023), it is posited that the
focus level of the reﬂected expansion wave becomes ﬁxed once the shape of the transmitted
988 A46-26
https://doi.org/10.1017/jfm.2024.472
 Published online by Cambridge University Press

<!-- PDF_PAGE: 27 -->

Exploration of shock–droplet interaction
(d)(c)
(b)(a)
–0.3
0
0.2
0.4
0.6
–0.2 –0.1 0 0.1 0.2 0.3
NPP
Focus
0.4
/Delta1P (MPa)
5
10
15
20
25
30
35
40
45
0
10
20
30
40
50
60
x/D0
–0.3
0
0.2
0.3
0.1
0.4
0.6
0.5
–0.2 –0.1 0 0.1 0.2 0.3
NPP
Focus
0.4 0.5
x/D0
kinc/K
–0.3
0
0.2
0.4
0.6
–0.2 –0.1 0 0.1 0.2 0.3
NPP (focus)
/Delta1P (MPa)
1
2
3
4
5
6
0
5
10
15
20
25
30
35
–0.3
0
0.2
0.4
0.6
–0.2 –0.1 0 0.1 0.2 0.3
NPP
Focus
0.4
kinc/K
a = 20
/Delta1Pexp /Delta1Ptotal
a = 25 a = 30 a = 35 a = 40
Figure 19. Reﬂected rays kinc/K with different range a (dashed lines), decreasing pressure caused by
expansion wave /Delta1Pexp and total decreasing pressure /Delta1Ptotal (solid lines) at different cases, with ( a) Ms = 2.4,
(b) Ms = 4.2, (c) Ms = 4.8, (d) Ms = 5.4.
wave and reﬂector is established, aligning with our ﬁnding that the reduction in pressure
caused by the expansion wave (/Delta1Pexp) and the focus level kinc/K exhibit parallel trends.
Nevertheless, the total pressure drop (/Delta1Ptotal) at the NPP point surpasses that at the focal
point, notably with higher shock Mach numbers. Given the increased distance between
the NPP and the droplet’s
right-hand boundary compared to the focus point, the NPP
experiences extended durations of ﬂuctuation and relaxation effects. This underscores
the importance of considering all factors inﬂuencing pressure variations, particularly the
impact of transmitted shock waves and relaxation effects when determining the NPP
point’s location. Consequently, the negative pressure recorded at the NPP is the most
extreme within the droplet, indicating a heightened likelihood of cavitation occurrence.
In this section, focus is deﬁned using the improved theoretical model, determining the
proportion of reﬂected waves at points along the central axis of the droplet. Comparison
between the focus from theoretical analysis and the NPP point from numerical simulation
reveals a close alignment under low
gas–liquid wave velocity ratios. However, at higher
wave velocity ratios, the focus point shifts nearer to the droplet’s downstream compared
to the negative pressure point.
For the exploration of the phenomenon that the NPP value can still be reached when
the number proportion of reﬂected waves is not the maximum, four factors are used to
explain the total pressure variation in the shock–droplet interaction. Finally, by comparing
988 A46-27
https://doi.org/10.1017/jfm.2024.472
 Published online by Cambridge University Press

<!-- PDF_PAGE: 28 -->

T. Xiong, C. Shao and K. Luo
the pressure decrease caused by the expansion wave ( /Delta1Pexp) with the total pressure
drop (/Delta1Ptotal) and the number of reﬂected waves ( kinc), it is found that the number of
reﬂected waves kinc affects the pressure drop caused by the expansion wave /Delta1Pexp,a n d
the /Delta1Pexp at the focus is indeed the largest among all points inside the droplet. However,
the /Delta1Ptotal of the NPP point is the highest among the points inside the droplet ,a n dt h e
/Delta1Ptotal is the consequence of considering all the four factors. Hence integrating these four
pressure variation elements results in a more pronounced negative pressure at the NPP
point compared to the focus point.
6. Conclusion
This study explores the interaction between shock waves and droplets through high-ﬁdelity
simulations and an improved theoretical model. The results align well with recent ﬁndings
for lower
gas–liquid wave velocity ratios, indicating a consistent NPP point. However,
for higher ratios, the NPP point’s location tends to remain constant, deviating from the
decreasing trend projected by Biasiori-Poulanges & El-Rabii ( 2021)a n dX u et al. (2023).
To elucidate this phenomenon, the theoretical model is reﬁned and applied, incorporating
information on the Mach stem through ray-tracing methods.
The existing theoretical model is inadequate for scenarios with high
gas–liquid wave
velocity ratios. In instances with low ratios, the speed of the incident shock wave external
to the droplet is slower than the transmitted shock wave within. The incident shock
wave detaches from the envelope of the transmitted shock wave at the close time of the
appearance of the Mach stem, leading to the neglect of the role of the Mach stem. In
contrast, at higher ratios, the external wave velocity surpasses the internal transmission
speed. After its appearance, the Mach stem constantly adheres to the boundary of
the droplet
, and exerts a continuous impact on the envelope inside the droplet. Hence
the theoretical model is enhanced to encompass the Mach stem’s role, ensuring its
applicability across a broader range of gas–liquid wave velocity ratios.
The improved theoretical model is used to obtain the information of the focus point.
It is found that it has the same decreasing trend as the expression of Biasiori-Poulanges
&E l - R a b i i(2021), but has a signiﬁcant deviation from the NPP point location obtained
by numerical simulation under high gas–liquid wave velocity ratios. Consequently, a
distinction is proposed between the focus point, where the reﬂected expansion wave
converges, and the NPP point, where the maximum negative pressure might induce
cavitation in the initial stages of
shock–droplet interaction.
The discussion further delves into the relationship between the convergence of reﬂected
expansion waves and the emergence of the NPP point. The pressure variation at a point
within the droplet is attributed to four key factors, namely, the pressure rise caused by
the shock wave, the relaxation effect that makes the pressure tend to be constant, the
pulse pressure from the high-pressure part upstream of the droplet to increase the pressure
intermittently, and the pressure drop caused by the expansion wave. Comparisons are made
among the proportion of reﬂected waves ( k
inc), the pressure drop from expansion waves
(/Delta1Pexp), and the overall pressure drop ( /Delta1Ptotal). Results illustrate that across various
shock Mach number scenarios, as the distance between the point on the central axis
and the right-hand boundary of the droplet decreases, both the number of reﬂected wave
convergences (kinc) and the pressure decrease from expansion waves ( /Delta1Pexp) increase,
signifying a direct correlation between the two. Nonetheless, the total pressure drop at the
NPP point surpasses that at the focus point. The NPP, which potentially triggers cavitation,
shows the most substantial pressure drop, while the expansion wave focus contributes
988 A46-28
https://doi.org/10.1017/jfm.2024.472
 Published online by Cambridge University Press

<!-- PDF_PAGE: 29 -->

Exploration of shock–droplet interaction
0
0
0.05
0.10
0.15
0.20
0.25
0.30
0.35
0.5 1.0 1.5 2.0 2.5 3.0
n
L
Biasiori-Poulanges & El-Rabii (2021)
Sembian et al. (2016)
Biasiori-Poulanges & Schmidmayer (2023)
Simulation (water)
Simulation (n-hexane)
Ms = 2.4
100
200
400
800
100
200
400800
100
200
400
800
1600
Ms = 4.8
Ms = 8.4
Figure 20. The effect of grid resolution on the NPP point’s locations with ND = 100, 200, 400, 800, 1600. The
NPP point with water and n-hexane as liquid phase with ND = 800, the theoretical results by Biasiori-Poulanges
& El-Rabii (2021), and the experimental results by Sembian et al. (2016), are also shown for comparison.
only partially. Any occurrence of NPP necessitates a meticulous consideration of these
four inﬂuential factors.
This research employs a ﬁve-equation model; however, the absence of phase transition
renders the cavitation process invisible. Future endeavours should focus on validating the
probable cavitation sites identiﬁed in this study through numerical methods incorporating
phase transitions. Subsequently, extensive investigations are warranted to elucidate the
manifestation of the four pressure variation factors.
Funding. This research is ﬁnancially supported by the National Natural Science Foundation of China (no.
52276151), the Talent Recruitment Project of Guangdong (2021QN020231), the Guangdong Basic and Applied
Basic Research Foundation (2023A1515012990), and the Foundation of Shenzhen Science and Technology
Committee (GXWD20231130201948001).
Declaration of interests. The authors report no conﬂict of interest.
Author ORCID.
Changxiao Shao https://orcid.org/0000-0002-1356-2796.
Appendix A
In this appendix, we analyse the impact of grid resolution on the locations of the
NPP, a crucial factor discussed in § 3. Figure 20 displays the NPP point’s locations for
different gas–liquid wave velocity ratios ( n): small Ms = 2.4 (water), moderate Ms = 4.8
(n-hexane), and large Ms = 8.4( n-hexane). The grid cell per diameter ( ND)v a l u e su s e d
are 100, 200, 400 and 800, respectively. We also consider ND = 1600 speciﬁcally for the
case Ms = 2.4 due to its lack of convergence trend at the aforementioned grid resolution.
From ﬁgure 20 , it is evident that the NPP point’s location remains similar for grid
resolutions 800 and 1600 in the case Ms = 2.4. Furthermore, for Ms = 4.8( n-hexane)
and Ms = 8.4( n-hexane), the NPP point’s location converges at ND = 400 and 800.
988 A46-29
https://doi.org/10.1017/jfm.2024.472
 Published online by Cambridge University Press

<!-- PDF_PAGE: 30 -->

T. Xiong, C. Shao and K. Luo
0.50 0.75
ND = 100
ND = 200
ND = 400
ND = 800
ND = 1600
1.00 1.25 1.50
–10
–8
–6
–4
–2
0
Pressure (MPa)
2
t∗
Figure 21. Temporal evolution of pressure at x = D0/4 with different grid resolutions ( Ms = 2.4, ND = 100,
200, 400, 800, 1600).
Hence we conclude that ND = 800 provides sufﬁcient resolution for determining the NPP
point’s location. Notably, recent research by Schmidmayer & Biasiori-Poulanges ( 2023)
employed ND = 400, Biasiori-Poulanges & Schmidmayer ( 2023)u s e d ND = 800, and
Xu et al. (2023)e m p l o y e dND = 800. Xu et al. (2023) investigated shock–water column
interaction and found no notable differences among ND = 800, 1200 and 1600. Therefore,
our chosen mesh resolution aligns with these studies, and we opt for ND = 800 for the
present investigation.
Next, we explore the impact of grid resolution on the temporal evolution of pressure, a
signiﬁcant aspect discussed in § 5. Figure 21 illustrates the temporal variation of pressure
at position x = D0/4f o r ND values of 100, 200, 400, 800, and 1600, respectively. As
the resolution increases, we observe that the overall temporal trend and ﬂuctuations
in pressure remain almost unchanged. The moment of minimum pressure, occurring at
t
⋆ = 1.28, remains consistent across all resolutions. However, it is important to note that
the speciﬁc pressure values are not the focus of our study as we do not fully resolve the
cavitation process. Based on these observations, we can conclude that the grid resolution
of N
D = 800 accurately captures the temporal evolution of
Appendix B
The difference between the model of Kapila et al. (2000) and the model of Allaire,
Clerc & Kokh ( 2002) lies in whether the convection equation for volume fraction has
the expansion term K ∇· u. The convection equation for volume fraction in the model of
Kapila et al. (2000) is
∂α1
∂t + u ·∇ α1 = K ∇· u, (B1)
where the K term represents expansion and compression in mixture regions. For a
two-component model, it is expressed as
988 A46-30
https://doi.org/10.1017/jfm.2024.472
 Published online by Cambridge University Press

<!-- PDF_PAGE: 31 -->

Exploration of shock–droplet interaction
0
–1
0
0
–D0/8
–D0/4
0 (K)
–D0/8 (K)
–D0/4 (K)
Pressure (MPa)
1
2
3
0.5 1.0 1.5 2.0 2.5
t∗
Figure 22. The pressure variation of the internal points of a droplet with or without the K term.
K = ρ2c2
2 − ρ1c2
1
ρ2c2
2
α2
+ ρ1c2
1
α1
, (B2)
where ρ, c and α represent the density, sound speed and volume fraction of the mixture
region, respectively. Subscripts represent different components.
To evaluate the expansion term K ∇· u, we conducted numerical simulations both with
and without the K term. The results are depicted in ﬁgure 22.
In general, the comparative analysis reveals that the K term has minimal impact on the
initial stages of the shock–droplet interaction investigated in our study.Figure 22 illustrates
that when the model incorporates the K term, the pressure surge induced by shock waves
is enhanced, while the ﬂuctuation effect is reduced compared to the model without the
K term. However, there is no notable disparity in the minimum pressure, indicating that
the NPP point remains unchanged. Additionally, the pressure trends remain consistent,
encompassing the effects of shock waves, wave propagation,
relaxation and expansion
waves as discussed in the mechanism analysis.
Moreover, since our research does not speciﬁcally address the cavitation process, gas
expansion is not considered. As demonstrated by Schmidmayer, Bryngelson & Colonius
(2020), the non-conservative nature of the K term can lead to numerical instabilities in
regions with intense compression or expansion in mixtures. To ensure the stability of our
simulation, we opt to disregard the expansion term.
Appendix C
The SGEOS parameters for water were selected based on the work of Gojani et al.
(2016) and Meng & Colonius ( 2018), speciﬁcally γ = 6.12 and π∞ = 3.43 × 108. These
parameters have been utilized widely in the study of shock–droplet interaction, as indicated
by Coralic (2014), Meng & Colonius ( 2015) and Dorschner et al. (2020).
Furthermore, the SGEOS parameters for water have been documented or derived
from various experimental data sources, such as Marsh ( 1980) and Cocchi, Saurel &
988 A46-31
https://doi.org/10.1017/jfm.2024.472
 Published online by Cambridge University Press

<!-- PDF_PAGE: 32 -->

T. Xiong, C. Shao and K. Luo
Experimental data Ms γ π∞ (Pa) α co (m s− 1)
Gojani et al. (2016)1 6 .12 3 .43 × 108 1.78 1450
Cocchi et al. (1996)16 .684 4 .06 × 108 1.924 1647
Marsh (1980)1 5 .548 3 .94 × 108 1.637 1480
Marsh (1980)2 3 .911 5 .59 × 108 1.637 1480
Table 3. The SGEOS parameters in different experimental data sets.
0
–3.5
–3.0
–2.5 Gojani et al. (2016)
Cocchi et al. (1996)
Marsh (1980) Ms = 1
Marsh (1980) Ms = 2
–2.0
–1.5
Pmin (MPa)
–1.0
–0.5
0.5
0
1 2
t∗
Figure 23. The NPP proﬁles using different SGEOS parameters.
Loraud (1996). Three sets of distinct experimental data were employed to ﬁt the SGEOS
parameters, including data from Gojani et al. (2016) used in the simulations, as well as
data from Marsh ( 1980) and Cocchi et al. (1996). The corresponding parameters obtained
from these sources are presented in table 3.
Figure 23 displays the NPP proﬁles generated using different SGEOS parameters. It
is evident that the proﬁles derived from Gojani et al. (2016) and Marsh ( 1980) resemble
each other closely, suggesting the validity of the SGEOS parameters obtained from these
experimental data sources. Moreover, when comparing the case ‘Marsh ( 1980) Ms = 1’
with ‘Marsh ( 1980) Ms = 2’, it is observed that the value of Ms has minimal impact on
the NPP proﬁles when the slope α and intercept c0 from the experimental data remain
constant. Therefore, the experimental data from Marsh ( 1980) can also be considered a
reliable source for obtaining the SGEOS parameters.
As for n-hexane, we determined its SGEOS parameters based on the experiments
conducted by Marsh ( 1980) due to the limited availability of experimental sources. The
expressions used to derive the SGEOS parameters were based on Johnsen ( 2008):
γ = 2α
(
1 + 1
Ms
)
− 1, (C1)
π∞ = ρoc2
o
γ − po, (C2)
988 A46-32
https://doi.org/10.1017/jfm.2024.472
 Published online by Cambridge University Press

<!-- PDF_PAGE: 33 -->

Exploration of shock–droplet interaction
Ms up,water up,n-hexane
1.75 1 .37 3 .39
2.4 4 .70 17 .84
3.0 9 .66 24 .47
3.6 16 .83 28 .60
4.2 21 .57 45 .24
4.8 28 .05 52 .50
5.4 35 .06 67 .85
6.0 42 .61 63 .65
6.6 50 .69 77 .67
7.2 59 .32 92 .77
7.8 68 .78 111 .37
8.4 – 101 .44
Table 4. The velocity of the liquid inside the water column behind the transmitted shock wave up.
where α and co are the slope and intercept of the ﬁtted line, respectively, Ms is the shock
Mach number, po is taken to be the ambient atmospheric pressure, and γ and π∞ are
the SGEOS parameters. The slope of the ﬁtted line α obtained through the Marsh ( 1980)
experiment is 1.5985, and the intercept co is 1090 m s − 1.B y substituting into the above
equation, we can obtain γ = 5.394 and π∞ = 1.45 × 108 for n-hexane.
Appendix D
In Xu et al. (2023), the transmitted shock wave speed ul is obtained following the
Rankine–Hugoniot relation (Haller et al. 2002, 2003; Nagayama et al. 2006) and can be
expressed as
ul = γl + 1
4
(
up +
√
u2p + 16 1
(γl + 1)2 c2
l
)
, (D1)
where γl represents the speciﬁc heat ratio of liquid (6.12 for water , and 5.39 for n-hexane),
cl represents the sound speed of the liquid at the initial state (1450 m s − 1 for water,a n d
1090 m s− 1 for n-hexane),a n d up represents the velocity of the liquid inside the water
column behind the transmitted shock wave.
The shock wave Mach number discussed in the study by Xu et al. (2023) is 2.4, which
indicates a low shock intensity. Consequently, the propagation velocity ul of the wave
conﬁgurations inside the droplet can be approximated as cl, where cl represents the wave
velocity. In our research, which focuses on high shock intensities, we ﬁrst evaluate the
velocity up using our simulation results. We determine the maximum velocity of the liquid
inside the water column behind the transmitted shock wave at x = D0/8a s up. The values
of up for both phases in all cases are presented in table 4.
Next, we conduct curve ﬁtting to establish a relationship between up and Ms, as shown
in ﬁgure 24. By incorporating up(Ms) into (D1) we calculate the wave velocity ul(Ms).W e
then apply this wave velocity to our theoretical analysis model to determine the focus point.
In ﬁgure 25, we compare our current ﬁndings with previous results that utilized a constant
wave velocity. Notably, when selecting ul = ul(Ms), we also update the corresponding
gas–liquid wave velocity ratio n. It is evident from ﬁgure 25 that regardless of whether a
constant cl or the realistic ul(Ms) is employed as ul, and regardless of whether the liquid
988 A46-33
https://doi.org/10.1017/jfm.2024.472
 Published online by Cambridge University Press

<!-- PDF_PAGE: 34 -->

T. Xiong, C. Shao and K. Luo
1
0
20
40
60
80
100
120 Water
n-hexane
u
p,water = a1Ms2 + b1Ms + c1
up,n-hexane = a2Ms2 + b2Ms + c2
2345
Ms
6789
up (m s–1)
Figure 24. The ﬁtting relationship between up and Ms.
0.5
0
0.05
0.10
0.15
0.20
0.25
0.30
1.0 1.5 2.0 2.5 3.0
n
L
ul,water = cl,water
ul,water = ul,water (Ms)
ul,n-hexane = cl,n-hexane
ul,n-hexane = ul,n-hexane (Ms)
Figure 25. The location of the focus point with different ul calculations.
phase is n-hexane or water, the position of the focus point follows a universal line that is
solely dependent on the gas–liquid wave velocity ratio n.
Therefore, as the Mach number of the shock wave increases, any increase in liquid
compressibility resulting in a higher sound velocity does not impact the focusing of the
reﬂected expansion wave.
Appendix E
We compare the trajectory of the Mach stem using different mesh resolutions, as illustrated
in ﬁgure 26. There are no signiﬁcant differences in the trajectory of the Mach stem when
varying the mesh resolution.
988 A46-34
https://doi.org/10.1017/jfm.2024.472
 Published online by Cambridge University Press

<!-- PDF_PAGE: 35 -->

Exploration of shock–droplet interaction
0.2 0.4 0.6 0.8 1.0 1.2 1.4 1.6 1.8 2.0
ND = 100
ND = 200
ND = 400
ND = 800
2.2
60
80
100
120
140
160
180
β (deg.)
t∗
Figure 26. Comparison of the trajectory of the Mach stem with different mesh resolutions.
200 300 400 500 600 700
Original fitting
Fitting by Ms = 8.4
800 900 1000
80
100
120
140
160
180
β (deg.)
T
Figure 27. Comparison of different Mach stem ﬁtting curves.
Next, we analyse the impact of different ﬁtting functions. The original curve ﬁtting for
the Mach stem trajectory is depicted in ﬁgure 8 (b). Notably, the Mach stem trajectory
corresponding to Ms = 8.4i n ﬁgure 8 (b) appears to have the most downward offset
compared to the current ﬁtted curve. We perform curve ﬁtting for the Mach stem trajectory
Ms = 8.4, and compare it with the original ﬁtting in ﬁgure 27 . The two curves exhibit
minimal discrepancies.
To assess the inﬂuence of the ﬁtting function on theoretical analysis, we quantitatively
compare the focus point values. The ﬁtting formula β(tM) is used to obtain its inverse
function tM(β). Subsequently, based on ( 4.6), we calculate the length of each ray at the
current time. The meaning of β(tM) is that at time tM , the Mach stem, which affects
the generation of rays, has reached the β location. Conversely, the meaning of tM(β) is
the time required for the Mach stem to reach the β location. Rays at the β location will
988 A46-35
https://doi.org/10.1017/jfm.2024.472
 Published online by Cambridge University Press

<!-- PDF_PAGE: 36 -->

T. Xiong, C. Shao and K. Luo
Focus (Ms = 5.4 case) Focus ( Ms = 7.8 case)
Original ﬁtting 0.007190 0.009701
Fitting by Ms = 8.4 0.007228 0.009765
Table 5. Focus predicted by different ﬁtting expressions.
commence generation upon the arrival of the Mach stem. Consequently, the selection of
ﬁtting formulas inevitably inﬂuences the results of the theoretical analysis. To illustrate this
effect, we compare the focus values using different ﬁtting curves, as depicted in ﬁgure 27.
The obtained expression, β = f(TM) =− 9 × 10− 5(TM)2 + 0.2442TM + 27.132, is used
to replace ( 4.11) for the liquid phase. Theoretical analysis is then conducted to determine
the focus for cases with Ms = 5.4 and 7.8, with water as the liquid phase. The comparison
is provided in table 5 , revealing that the focus point values exhibit negligible differences
across different ﬁtting curves.
REFERENCES
AALBURG ,C . ,V AN LEER ,B .&F AETH , G.M. 2003 Deformation and drag properties of round drops
subjected to shock-wave disturbances. AIAA J. 41 (12), 2371–2378.
ALLAIRE ,G . ,C LERC ,S .&K OKH , S. 2002 A ﬁve-equation model for the simulation of interfaces between
compressible ﬂuids. J. Comput. Phys. 181 (2), 577–616.
ANDO , K. 2010 Effects of polydispersity in bubbly ﬂows. PhD thesis, California Institute of Technology.
AZOUZI , M.E.M., R AMBOZ ,C . ,L ENAIN ,J . F .&C AUPIN , F. 2013 A coherent picture of water at extreme
negative pressure. Nat. Phys. 9 (1), 38–41.
BHATTACHARYA , S. 2016 Interfacial wave dynamics of a drop with an embedded bubble. Phys. Rev. E 93 (2),
023119.
BIASIORI -POULANGES ,L .&E L-RABII , H. 2021 Shock-induced cavitation and wavefront analysis inside a
water droplet. Phys. Fluids 33 (9), 097104.
BIASIORI -POULANGES ,L .&S CHMIDMAYER , K. 2023 A phenomenological analysis of droplet
shock-induced cavitation using a multiphase modeling approach. Phys. Fluids 35 (1), 013312.
BOYD ,B .&J ARRAHBASHI , D. 2021 Numerical study of the transcritical shock–droplet interaction. Phys.
Rev. Fluids 6 (11), 113601.
BRUJAN , E.A., K EEN , G.S., V OGEL ,A .&B LAKE , J.R. 2002 The ﬁnal stage of the collapse of a cavitation
bubble close to a rigid boundary. Phys. Fluids 14 (1), 85–92.
BRYNGELSON , S.H., S CHMIDMAYER ,K . ,C ORALIC ,V . ,M ENG , J.C., M AEDA ,K .&C OLONIUS , T. 2021
MFC: an open-source high-order multi-component, multi-phase, and multi-scale compressible ﬂow solver.
Comput. Phys. Commun. 266, 107396.
CAUPIN , F. 2005 Liquid–vapor interface, cavitation, and the phase diagram of water. Phys. Rev. E 71 (5),
051605.
CAUPIN ,F .&H ERBERT , E. 2006 Cavitation in water: a review. C. R. Phys. 7 (9–10), 1000–1017.
CERVEN `Y, V. 2001 Seismic Ray Theory . Cambridge University Press.
COCCHI , J.P ., S AUREL ,R .&L ORAUD , J.C. 1996 Treatment of interface problems with Godunov-type
schemes. Shock Waves 5, 347–357.
COLONIUS ,V .&C ORALIC , T. 2014 Finite-volume WENO scheme for viscous compressible multicomponent
ﬂows. J. Comput. Phys. 274, 95–121.
CORALIC , V. 2015 Simulation of shock-induced bubble collapse with application to vascular injury in
shockwave lithotripsy. PhD thesis, California Institute of Technology.
DEBENEDETTI , P.G. 1996 Metastable Liquids: Concepts and Principles . Princeton University Press.
DORSCHNER ,B . ,B IASIORI -POULANGES , L., S CHMIDMAYER ,K . ,E L-RABII ,H .&C OLONIUS , T. 2020
On the formation and recurrent shedding of ligaments in droplet aerobreakup. J. Fluid Mech. 904, A20.
ENGEL , O.G. 1958 Fragmentation of waterdrops in the zone behind an air shock. J. Res. Natl Bur. Stand.
60 (3), 245–280.
FIELD , J.E., C AMUS , J.J., T INGUEL Y,M . ,O BRESCHKOW ,D .&F ARHAT , M. 2012 Cavitation in impacted
drops and jets and the effect on erosion damage thresholds. Wear 290, 154–160.
988 A46-36
https://doi.org/10.1017/jfm.2024.472
 Published online by Cambridge University Press

<!-- PDF_PAGE: 37 -->

Exploration of shock–droplet interaction
FIELD , J.E., D EAR ,J . P .&O GREN , J.E. 1989 The effects of target compliance on liquid drop impact. J. Appl.
Phys. 65 (2), 533–540.
FLEISCHMANN ,N . ,A DAMI ,S .&A DAMS , N.A. 2020 A shock-stable modiﬁcation of the HLLC Riemann
solver with reduced numerical dissipation. J. Comput. Phys. 423, 109762.
GEV A,M . ,R AM ,O .&S ADOT , O. 2018 The regular reﬂection → Mach reﬂection transition in unsteady ﬂow
over convex surfaces. J. Fluid Mech. 837, 48–79.
GOJANI , A.B., O HTANI ,K . ,T AKAYAMA ,K .&H OSSEINI , S.H.R. 2016 Shock Hugoniot and equations of
states of water, castor oil, and aqueous solutions of sodium chloride, sucrose and gelatin. Shock Waves 26,
63–68.
GUILDENBECHER , D.R., L ÓPEZ -RIVERA ,C .&S OJKA , P.E. 2009 Secondary atomization. Exp. Fluids
46 (3), 371–402.
HALLER , K.K., P OULIKAKOS ,D . ,V ENTIKOS ,Y .&M ONKEWITZ , P. 2003 Shock wave formation in droplet
impact on a rigid surface: lateral liquid motion and multiple wave structure in the contact line region.
J. Fluid Mech. 490, 1–14.
H
ALLER , K.K., V ENTIKOS ,Y . ,P OULIKAKOS ,D .&M ONKEWITZ , P. 2002 Computational study of
high-speed liquid droplet impact. J. Appl. Phys. 92 (5), 2821–2828.
HANSON , A.R., D OMICH , E.G. & A DAMS , H.S. 1963 Shock tube investigation of the breakup of drops by
air blasts. Phys. Fluids 6 (8), 1070–1080.
HSIANG , L.P . & F AETH , G.M. 1992 Near-limit drop deformation and secondary breakup. Intl J. Multiphase
Flow 18 (5), 635–652.
HSIANG , L.P . & F AETH , G.M. 1995 Drop deformation and breakup due to shock wave and steady
disturbances. Intl J. Multiphase Flow 21 (4), 545–560.
JOHNSEN , E. 2008 Numerical simulations of non-spherical bubble collapse: with applications to shockwave
lithotripsy. PhD thesis, California Institute of Technology.
JOHNSEN ,E .&C OLONIUS , T. 2009 Numerical simulations of non-spherical bubble collapse. J. Fluid Mech.
629, 231–262.
JOSEPH , D.D., B ELANGER ,J .&B EA VERS, G.S. 1999 Breakup of a liquid drop suddenly exposed to a
high-speed airstream. Intl J. Multiphase Flow 25 (6–7), 1263–1303.
KAISER , J.W .J., W INTER , J.M., A DAMI ,S .&A DAMS , N.A. 2020 Investigation of interface deformation
dynamics during high-Weber number cylindrical droplet breakup. Intl J. Multiphase Flow 132, 103409.
KAPILA , A.K., M ENIKOFF ,R . ,B DZIL , J.B., S ON ,S . F .&S TEW ART, D.S. 2000 T wo-phase modeling
of DDT in granular materials: reduced equations. Tech. Rep. LA-UR-99-3329. Los Alamos National
Laboratory.
KÉKESI ,T . ,A MBERG ,G .&W ITTBERG , L.P. 2014 Drop deformation and breakup. Intl J. Multiphase Flow
66, 1–10.
KODAMA ,T .&T OMITA , Y. 2000 Cavitation bubble behavior and bubble–shock wave interaction near a
gelatin surface as a study of in vivo bubble dynamics. Appl. Phys. B 70, 139–149.
KYRIAZIS ,N . ,K OUKOUVINIS ,P .&G AVA I S E S, M. 2018 Modelling cavitation during drop impact on solid
surfaces. Adv. Colloid Interface Sci. 260, 46–64.
LANE , W.R. 1951 Shatter of drops in streams of air. Ind. Engng Chem. 43 (6), 1312–1317.
LEE ,C . H .&R EITZ , R.D. 2000 An experimental study of the effect of gas density on the distortion and
breakup mechanism of drops in high speed gas stream. Intl J. Multiphase Flow 26 (2), 229–244.
LEVEQUE , R.J. 2002 Finite Volume Methods for Hyperbolic Problems. Cambridge University Press.
LIANG ,Y . ,J IANG , Y .Z., W EN ,C . Y .&L IU, Y. 2020 Interaction of a planar shock wave and a water droplet
embedded with a vapour cavity. J. Fluid Mech. 885,R 6 .
LIU,N . ,W ANG , Z.G., S UN , M.B., W ANG ,H . B .&W ANG , B. 2018 Numerical simulation of liquid droplet
breakup in supersonic ﬂows. Acta Astronaut. 145, 116–130.
LIU, Y. 2021 Investigation on the interaction of a shock and a liquid droplet with and without a vapor cavity
inside. PhD thesis, Hong Kong Polytechnic University.
LIU,Z .&R EITZ , R.D. 1997 An analysis of the distortion and breakup mechanisms of high speed liquid drops.
Intl J. Multiphase Flow 23 (4), 631–650.
MARSH , S.P. 1980 LASL Shock Hugoniot Data . University of California Press.
MENG , J.C. 2016 Numerical simulations of droplet aerobreakup. PhD thesis, California Institute of
Technology.
MENG ,J . C .&C OLONIUS , T. 2015 Numerical simulations of the early stages of high-speed droplet breakup.
Shock Waves 25, 399–414.
MENG ,J . C .&C OLONIUS , T. 2018 Numerical simulation of the aerobreakup of a water droplet. J. Fluid Mech.
835, 1108–1135.
988 A46-37
https://doi.org/10.1017/jfm.2024.472
 Published online by Cambridge University Press

<!-- PDF_PAGE: 38 -->

T. Xiong, C. Shao and K. Luo
NAGAYAMA ,K . ,M ORI ,Y . ,M OTEGI ,Y .&N AKAHARA , M. 2006 Shock Hugoniot for biological materials.
Shock Waves 15, 267–275.
NICHOLLS ,J . A .&R ANGER , A.A. 1969 Aerodynamic shattering of liquid drops. AIAA J. 7 (2), 285–290.
OBRESCHKOW ,D . ,D ORSAZ ,N . ,K OBEL ,P . , DE BOSSET ,A . ,T INGUEL Y,M . ,F IELD ,J .&F ARHAT ,M .
2011 Conﬁned shocks inside isolated liquid volumes: a new path of erosion? Phys. Fluids 23 (10), 101702.
OBRESCHKOW ,D . ,K OBEL ,P . ,D ORSAZ ,N . ,D E BOSSET ,A . ,N ICOLLIER ,C .&F ARHAT , M. 2006
Cavitation bubble dynamics inside liquid drops in microgravity. Phys. Rev. Lett. 97 (9), 094502.
PHILIPP ,A .&L AUTERBORN , W. 1998 Cavitation erosion by single laser-produced bubbles. J. Fluid Mech.
361, 75–116.
PILCH ,M .&E RDMAN , C.A. 1987 Use of breakup time data and velocity history data to predict the maximum
size of stable fragments for acceleration-induced breakup of a liquid drop. Intl J. Multiphase Flow 13 (6),
741–757.
SCHMIDMAYER ,K .&B IASIORI -POULANGES , L. 2023 Geometry effects on the droplet shock-induced
cavitation. Phys. Fluids 35 (6), 063315.
SCHMIDMAYER ,K . ,B RYNGELSON ,S . H .&C OLONIUS , T. 2020 An assessment of multicomponent ﬂow
models and interface capturing schemes for spherical bubble dynamics. J. Comput. Phys. 402, 109080.
SEMBIAN ,S . ,L IVERTS ,M . ,T ILLMARK ,N .&A PAZIDIS , N. 2016 Plane shock wave interaction with a
cylindrical water column. Phys. Fluids 28 (5), 056102.
SHPAK ,O . ,V ERWEIJ ,M . , DE JONG ,N .&V ERSLUIS , M. 2016 Droplets, bubbles and ultrasound interactions.
In Therapeutic Ultrasound (ed. J.-M. Escoffre & A. Bouakaz), pp. 157–174. Springer.
THEOFANOUS , T.G. 2011 Aerobreakup of Newtonian and viscoelastic liquids. Annu. Rev. Fluid Mech. 43,
661–690.
THEOFANOUS ,T . G .&L I, G.J. 2008 On the physics of aerobreakup. Phys. Fluids 20 (5), 052103.
THEOFANOUS , T.G., M ITKIN , V .V ., NG, C.L., C HANG , C.H., D ENG ,X .&S USHCHIKH ,S .2 0 1 2T h e
physics of aerobreakup. II. Viscous liquids. Phys. Fluids 24 (2), 022104.
THOMPSON , K.W. 1987 Time dependent boundary conditions for hyperbolic systems. J. Comput. Phys. 68 (1),
1–24.
THOMPSON , K.W. 1990 Time-dependent boundary conditions for hyperbolic systems, II. J. Comput. Phys.
89 (2), 439–461.
VIJAYASHANKAR , V .S., K UTLER ,P .&A NDERSON ,D .1 9 7 6D i f f r a c t i o no fas h o c kw a v eb yac o m p r e s s i o n
corner; regular and single Mach reﬂection. NASA Tech. Rep. TM X-73178.
WU, W .X., X IANG ,G . M .&W ANG , B. 2018 On high-speed impingement of cylindrical droplets upon solid
wall considering cavitation effects. J. Fluid Mech. 857, 851–877.
XIANG ,G . M .&W ANG , B. 2017 Numerical study of a planar shock interacting with a cylindrical water
column embedded with an air cavity. J. Fluid Mech. 825, 825–852.
XU,S . ,F AN , W .Q., W U, W .X., W ANG ,W .&W ANG , B. 2022 The early stage of the interaction between
a planar shock and a cylindrical droplet considering cavitation effects: theoretical analysis and numerical
simulation. arXiv:2205.00471
X
U,S . ,F AN , W .Q., W U, W .X., W EN ,H . C .&W ANG , B. 2023 Analysis of wave converging phenomena
inside the shocked two-dimensional cylindrical water column. J. Fluid Mech. 964,A 1 2 .
ZHAO ,H . ,L IU, H.F., L I,W . F .&X U, J.L. 2010 Morphological classiﬁcation of low viscosity drop bag
breakup in a continuous air jet stream. Phys. Fluids 22 (11), 114103.
988 A46-38
https://doi.org/10.1017/jfm.2024.472
 Published online by Cambridge University Press
