<!-- PDF_PAGE: 1 -->

Numerical Study on Liquid Droplet Internal Flow Under
Shock Impact
Ben Guan,∗ Yao Liu,† and Chih-Y ung Wen‡
Hong Kong Polytechnic University, Hung Hom, Kowloon, Hong Kong, People’s Republic of China
and
Hua Shen§
King Abdullah University of Science and Technology (KAUST), Thuwal 23955-6900, Saudi Arabia
DOI: 10.2514/1.J057134
The establishment of an internal flowfield inside a single water droplet subjected to shock-wave impact is
numerically and theoretically investigated. The main focus is on the description of the droplet internal flow pattern,
which is believed to be one of the dominant factors in initial droplet deformation. The droplet internal flow pattern
holds steady for quite a long time after the incident shock passage, and a saddle point is observed for the first time.
Accordingly, the saddle point inside the droplet flow is used as a characteristic point to describe the internal flow.
Cases of different incident shock strengths are tested, and a theoretical prediction is proposed to delineate the
correlation between the saddle point steady position and the strength of the incident shock wave. The numerical cases
are found to be in good agreement with the prediction. The present study helps to complete the understanding of the
overall droplet aerobreakup phenomenon.
Nomenclature
A, B = constants used in the correlation
a0 = sound speed in air
d0 = initial droplet diameter
lsp = displacement of the saddle point
l∗sp = nondimensional displacement of the saddle point
Ms = incident shock Mach number
Oh = Ohnesorge number
Re = Reynolds number
t = dimensional time
t∗ = nondimensional time (initiates when the incident shock
impacts)
ts = duration in which the shock in air influences the leeward
area
t∗sp = nondimensional time (initiates when the saddle point
appears)
ug = postshock airflow velocity
ul = liquid flow velocity
us = shock velocity in air
usp = velocity of the saddle point
We = Weber number
x∗ = nondimensional position at the x coordinate
γ = ratio of the specific heats of air
ρg = postshock air density
ρl = density of liquid
ρ0 = density of quiescent air
I. Introduction
T
HE shock-wave-induced aerobreakup of a liquid droplet occurs
in many high-speed flow scenarios and is a fundamental and
challenging two-phase flow problem. Extensive studies have been
conducted on this fascinating phenomenon for more than half a
century because of its wide applications in chemical processing,
Space Shuttle protection, high-speed vehicle propulsion, and the
delivery of bulk chemical weapons. Knowledge of the deformation
and fragmentation of a water droplet is of interest in establishing the
mechanism of the breakup process. Comprehensive reviews of
droplet breakup were written by Wierzba and Takayama [1],
Guildenbecher et al. [2], Joseph et al. [3], and Theofanous [4].
However, these reviews mainly focused on the external airflow and
the interface evolution induced by the shock wave because of the
difficulty of visualizing the droplet internal flow.
The first experimental attempt to disclose the internal flow pattern
of droplet breakup under shock impingement was conducted by Igra
and Takayama [5] using a cylindrical water column. Although the
qualitative breakup process and internal variation were discussed in
their research, the internal flow pattern remained obscure. A recent
experimental study was conducted by Sembian et al. [6], in which the
internal wave system evolution and cavitation inside a cylindrical
water column were visualized after the shock impact. However, the
details of the internal flow and the initial deformation of the water
column were still difficult to illustrate. Besides, nearly all of the
studies involving droplet internal flow were conducted by numerical
methods. Although several researchers [7–10] elucidated the internal
flow pattern, they concentrated on cases with low Weber numbers
We. In shock-induced droplet breakup cases, where the inertial effect
dominates the flow, the droplet internal flowfield has been totally
overlooked. The deformation of droplet configuration, however, is
determined essentially by both the liquid flow inside the droplet and
the external airflow. Also, in the study by Boiko and Poplavski [11],
the authors inferred that the internal flow could be extremely
important for constructing a unified physical model of drop breakup
in a gas flow. It will be instructive to build the connections between
the flow parameters and the droplet internal flow.
II. Numerical Methods
For the case of liquid droplet breakup, the dominant dimensionless
parameters are the Weber number We, Ohnesorge number Oh, and
Reynolds number Re. The definitions of these parameters are
Received 6 February 2018; revision received 21 May 2018; accepted for
publication 1 June 2018; published online 30 July 2018. Copyright © 2018 by
the American Institute of Aeronautics and Astronautics, Inc. All rights
reserved. All requests for copying and permission to reprint should be
submitted to CCC at www.copyright.com; employ the ISSN 0001-1452
(print) or 1533-385X (online) to initiate your request. See also AIAA Rights
and Permissions www.aiaa.org/randp.
*Research Associate, Department of Mechanical Engineering, Hong Kong
Special Administrative Region.
†Ph.D. Candidate, Department of Mechanical Engineering, Hong Kong
Special Administrative Region.
‡Professor, Department of Mechanical Engineering, Hong Kong Special
Administrative Region.
§Research Associate, Applied Mathematics and Computational Science,
Computer Electrical and Mathematical Science and Engineering Division
(CEMSE), Extreme Computing Research Center (ECRC).
3382
AIAA JOURNAL
V ol. 56, No. 9, September 2018
Downloaded by Dalian University of Technology on August 31, 2026 | http://arc.aiaa.org | DOI: 10.2514/1.J057134

<!-- PDF_PAGE: 2 -->

We /.0136 ρgu2gd0
σ ;O h /.0136 μl/.0129/.0129/.0129/.0129/.0129/.0129/.0129/.0129/.0129/.0129/.0129 /.0129ρlσd0
p ;R e /.0136 ρgugd0
μg
(1)
where ρ is the density;u is the velocity;d0 is the diameter of the liquid
droplet; σ is the surface tension;μ is the viscosity; and subscriptsl and
g represent the liquid and gas behind the shock, respectively. Weber
number is the ratio of the fluid ’s inertial force to its surface tension
force, Ohnesorge number is the ratio of the viscous force to the
surface tension force, and Reynolds number is the ratio of the inertial
force to the viscous force.
In the present study, in which an air shock wave impacting a single
liquid droplet is simulated, Weber number and Reynolds number
reached orders of ×103 and ×104, respectively. These results indicate
that the surface tension effect and the viscosity effect are both
much smaller than the inertial force. As a result, the compressible
axisymmetric Euler equations are solved to simulate the shock –
droplet interaction:
∂α
∂t /.0135 V ⋅∇α /.0136 0 (2)
∂ρsαs
∂t /.0135 ∇⋅ /.0133 ρsαsV/.0134/.0136 − ρsαsV
y ;s /.0136 1; 2 (3)
∂ρV
∂t /.0135 ∇⋅ /.0133 ρV ⊗ V /.0135 p/.0134/.0136 − ρV ⊗ V
y (4)
∂E
∂t /.0135 ∇⋅ /.0133 V/.0133 E /.0135 p/.0134/.0134 /.0136 − V/.0133 E /.0135 p/.0134
y (5)
where α denotes the air volume fraction; ρs the density of the
component fluid s; ρ the density of the mixture;V the velocity vector;
p the pressure; and E the total energy.
The stiffened gas equation of state (EOS) is adopted to close this
system:
p /.0136/.0133 γ − 1/.0134
/.0018
E − 1
2 ρV ⋅V
/.0019
− γπ (6)
where
1
γ − 1 /.0136 Σ αi
γi − 1 and γπ
γ − 1 /.0136 Σ αiγiπi
γi − 1 (7)
The total density and the sound speed of the mixture can be
respectively calculated as
ρ /.0136 Σαiρi and c /.0136
/.0129/.0129/.0129/.0129/.0129/.0129/.0129/.0129/.0129/.0129/.0129/.0129/.0129/.0129/.0129/.0129/.0129/.0129/.0129/.0129/.0129/.0129/.0129/.0129
γ/.0133 p /.0135 π/.0134 ∕ρ
p
(8)
For air, the ratio of specific heat γ /.0136 1.4 and π /.0136 0P a reduce the
stiffened gas EOS to the ideal gas equation. For water, empirical
parameters are adopted, where γ /.0136 7.15 and π /.0136 3.31 × 10
8 Pa.
The volume-fraction-based five-equation model is solved using a
maximum-principle-satisfying upwind conservation element and
solution element scheme. An Harten-Lax-van Leer-Contact
approximate Riemann solver is employed to get the numerical fluxes
between the conservation elements. The present method has shown
great performance in the numerical conservative properties in both
space and time, and it has proven accurate in capturing shock and
simulating contact discontinuities. Numerical validation and error
analysis of the present numerical methods can be found in Shen et al.’s
studies [12–14].
The numerical method is first used to simulate the experiment
conducted by Yi et al. [15] using a droplet diameter d
0 of 3.03 mm
and an incident shock Mach number Ms of 1.39. The corresponding
dimensionless numbers of their experiment were We /.0136 3075,
Re /.0136 6.41 × 104, and Oh /.0136 2.14 × 10−3. A rectangular computa-
tional domain is used within which an initially quiescent water
droplet with a diameter d0 and a right-moving planar incident shock
are defined. The upper boundary of the domain is defined as a
symmetric axis, and the left boundary is defined as a constant inflow
condition, where the postshock state is calculated by Rankine –
Hugoniot relations. The outflow conditions are enforced on the lower
and right boundaries by applying a zeroth-order extrapolation. To
avoid the influence of the computational boundaries, a large
computational domain is arranged, where the length of the domain in
the x direction is 18 times the droplet radius, and the width of the
domain in the y direction is six times the droplet radius. A spatially
fixed Cartesian coordinate system is used in the present study, and the
center of the droplet is located at (0, 0) for convenience of the initial
settings. A planar incident shock is located initially at 1.2 times the
droplet radius upstream of coordinates (0, 0).
The grid convergence was first tested according to the density
distributions lg/.0133 ρ/.0134 along the axis of symmetry, as shown in Fig. 1,
where four different numbers of grids were arranged within the length
of the droplet radius. The terms R140 ∼ R200 denote that there were
140 ∼ 200 grids arranged per droplet radius. The left inset presents a
sketch of the droplet/shock-wave system after the shock-wave
impact, within which RS denotes the reflected shock, IS is the
incident shock, MS is the Mach stem, WS is the windward stagnation
point, and LS is the leeward stagnation point. The dotted line
indicates the axis of symmetry. The right inset presents an enlarged
MS area (dashed square area). It can be seen that the larger the grid
number is, the sharper the pressure change across the MS shock front
is. The shock fronts of cases R160, R180, and R200 nearly collapse
with each other, which indicates good grid convergence. Throughout
this study, a mesh size of 200 grids per droplet radius was adopted.
The comparison between the numerical results and the
experimental images is shown in Fig. 2, in which three distinct
instants after the shock impact (t /.0136 0) are selected. At t /.0136 40 μs, the
experimental image shows tiny corrugation (C) at the leeward surface
RS IS
MS
droplet
WS LS
RS
WS LS
MS
Fig. 1 Grid convergence test showing density distributions at 20 μs
after the incident shock touches the droplet with four different grid sizes
(140, 160, 180, and 200 grids per droplet radius).
lip
LSWS
EQ KHI AT
x
y
(0, 0)
C
C
Fig. 2 Comparison of the numerical and experimental results at
different instants (upper part: experimental images, lower part:
numerical results).
GUAN ET AL. 3383
Downloaded by Dalian University of Technology on August 31, 2026 | http://arc.aiaa.org | DOI: 10.2514/1.J057134

<!-- PDF_PAGE: 3 -->

of the droplet between the equator (EQ) and the LS, whereas the rest
of the surface remains intact. At this moment, a Kelvin –Helmholtz
instability (KHI) develops at the windward surface in the numerical
result but not in the experimental result. The reason for this difference
derives from the neglect of the surface tension term in the present
numerical method. In the experimental images, the first tiny
corrugation grows at t /.0136 60 μs and turns into the “lip”. Also
developed is the KHI amplitude. The KHI amplitude is a direct
response to the shear velocity distribution, which increases from the
WS to the EQ. At t /.0136 100 μs, although the main body of the droplet
remains spherical to a certain extent, the protrusions are distinct, and
atomization (A T) occurs obviously at the tips of these protrusions.
The capability of the present numerical method, according to this
comparison, is proved to be fairly good.
III. Numerical Results
A. Internal Flowfield Description
The flowfield build-up process of this shock–droplet interaction is
depicted in Fig. 3 by the air density contours. The white solid lines
with arrows illustrate the temporal streamlines. These streamlines are
truncated to focus only on the liquid flow inside the droplet rather
than on the outer airflow and the interfacial boundary flow. After the
IS impacts the windward surface of the droplet at t /.0136 2 μs, the RS is
formed and propagates upstream, whereas a transmitted shock (TS,
shown by the white dash line) propagates inside the droplet, which is
much faster than the incident shock in air. Before the diffracted shock
(DS) collides at the droplet LS point, the droplet internal flow keeps
developing induced by the internal diverging TS (t /.0136 6 μs) when all
of the streamlines within the droplet are pointing in the downstream
direction. At t /.0136 14 μs, high pressure is formed in the LS area
because of the DS collision. Accordingly, the LS and the part of the
internal liquid close to the LS are motivated by this high pressure to
flow upstream. As a result, there must be a point inside the droplet on
the axis of symmetry where the velocity is zero to balance the
downstream and upstream liquid flow momentums. Observed for
the first time, a saddle point (SP , labeled as the white dot) is formed. In
the following instants, although the shedding vortex (SV), KHI, and
chaotic recirculation zone (RZ) form in sequence ( t /.0136 20, 60, and
100 μs), the SP keeps its position nearly unchanged. This shock –
droplet interaction process shows that the internal flowfield is
established in quite a short time soon after the incident shock sweeps
over the droplet. The existence of an SP suggests that the droplet is
suspended in air with respect to the SP before the droplet is torn apart
and blown downstream.
Late-stage images at t /.0136 200 and 250 μs are shown, where the
droplet is severely deformed into a crescent shape. At 200 μs,
although the droplet experiences severe deformation, the internal
flowfield maintains the same pattern as before. The distance between
the WS and LS decreases, and the SP nearly touches the LS. At
250 μs, the SP disappears, and all of the streamlines point in the
downstream direction. No longer suspended, the whole droplet drifts
downstream. To delineate the relative positions of the WS, the LS,
and the SP , the trajectories of these three points are recorded in Fig. 4.
The distance between the WS and LS illustrates that the droplet
becomes narrow in the streamwise direction. Interestingly, the SP
trajectory remains steady after the internal flowfield is established
(at t /.0136 25 μs) and moves toward the LS when the droplet deforms
severely (at t /.0136 180 μs). After the trajectories of the LS and the SP
intersect, the LS trajectory stops moving upstream and turns
downstream instead.
More numerical cases were conducted to examine if this internal
flow pattern is universal in a larger parameter space. The focus was on
the droplet diameter and density differences. On the droplet diameter,
additional simulations with d
0 /.0136 2.5 and 3.5 mm were conducted.
On the density difference, while maintaining the incident shock
strength at Ms /.0136 2.4, three different kinds of droplets were adopted:
gelatin (heavier than water), fat (lighter that water), and dodecane
(much lighter than water). The corresponding densities and stiffened
gas EOS parameters are listed in Table 1.
Dimensionless trajectories of the WS, LS, and SP are extracted
from the numerical results mentioned previously (see Fig. 5).
The quantities are nondimensionalized as t∗ /.0136 t∕/.0137/.0133 d0∕ug/.0134 /.0129/.0129/.0129/.0129/.0129/.0129/.0129/.0129/.0129/.0129/.0129 /.0129ρl∕ρg
p /.0138 ,
x∗ /.0136 x∕d0,a n d t∗sp /.0136/.0133 t − t0sp/.0134 ∕/.0137/.0133 d0∕ug/.0134 /.0129/.0129/.0129/.0129/.0129/.0129/.0129/.0129/.0129/.0129/.0129 /.0129ρl∕ρg
p /.0138 ,w h e r et∗ is the
dimensionless time of the droplet evolution, ug is the postshock
air velocity, ρl is the liquid density, ρg is the postshock air density,
2 µs
IS
RS
TS
DS
SP
6 µs
20 µs14 µs
60 µs 100 µs
SV
RZ
KHI
250 µs
RZ
200 µs
RZ
ρg
Fig. 3 Numerical airstream density distribution and the internal flow
streamlines of Yi et al. ’s case [15].
LS
WS
SP
Fig. 4 Trajectories of windward stagnation point (WS), leeward
stagnation point (LS), and saddle point (SP) of Yi et al. ’s case [15].
Table 1 Parameters used for the
different liquids
ργ π
Gelatin 1061.0 4.04 6.1 × 108
Fat 920.0 4.18 4.74 × 108
Dodecane 749.5 2.35 4.0 × 108
3384 GUAN ET AL.
Downloaded by Dalian University of Technology on August 31, 2026 | http://arc.aiaa.org | DOI: 10.2514/1.J057134

<!-- PDF_PAGE: 4 -->

x∗ is the dimensionless time, t∗sp is the dimensionless time of SP
development, and t0sp is the instant when the SP appears. It is seen
from Fig. 5a that the dimensionless trajectories of the WS and LS
collapse perfectly to each other. The SP trajectories, as shown in
Fig. 5b, hold steady at around x
∗ /.0136 0.3 after t∗sp /.0136 0.05, which
indicates that this internal flow pattern is universal in similar shock/
droplet interaction phenomena.
B. Internal Flowfield with Different Shock Strengths
To correlateMs with water droplet internal flow pattern, cases with
different shock strengths are simulated, and comparisons are made at
the same dimensionless time. Figure 6 presents the droplet internal
flow pattern at the instant whent
∗ /.0136 0.3 for four different Ms values.
It is seen that with the increase of shock strength, the SP locates itself
closer and closer to the LS, and the droplet morphology varies
accordingly.
The position of the SP is obviously subjected to the momentum
transportation from the high-pressure zones at the WS and the LS.
This momentum transportation presents itself by the movement
of the positions of the stagnation points. The trajectories of the WS
and LS of the preceding five different M
s cases are extracted and
comparisons among them are shown in Fig. 7. It is interesting to see
that both the WS and LS trajectories collapse perfectly to the potential
theory prediction [16] at the early stage.
Because the internal flowfield is simple at the early stage, an easy
way to describe the internal flow pattern is to record the position of
the SP , which remains stationary in space after the initial flow
development process. Trajectories of the SPs for different incident
shock strengths are presented in Fig. 8. As shown, SPs form very
close to the LS initially and move upstream. Although oscillations
exist in all five cases because of the repeated internal wave reflection,
the positions of the SPs hold relatively steady after t
∗sp /.0136 0.05.
Furthermore, the trend shown in Fig. 6 is well reflected in Fig. 8 in
that the SP position drifts farther downstream (largerx coordinate) for
the relatively strong shock cases. The trajectories of the SPs before
Fig. 5 Trajectories of a) WS/LS, and b) SP, for different droplets at Ms /.01362.4 in their dimensionless form.
Ms1.89 Ms2.4 Ms3.0 Ms3.9
ρg
Fig. 6 Water droplet morphologies at t∗ /.01360.3 for cases with different incident shock strengths.
Fig. 7 Trajectories of WS (open symbols) and LS (solid symbols) of
cases with different incident shock Mach numbers.
GUAN ET AL. 3385
Downloaded by Dalian University of Technology on August 31, 2026 | http://arc.aiaa.org | DOI: 10.2514/1.J057134

<!-- PDF_PAGE: 5 -->

they reach their stationary position collapse to the same line (with the
same slope as the black dash line denoted in Fig. 8). This indicates
that the rate of change of the internal flow pattern can be well
correlated using the preceding nondimensionalization method.
C. Theoretical Prediction
Following the preceding discussion, the displacement of the SP ,
lsp, after the initial shock–droplet interaction, can be estimated based
on the velocity at which the SP moves (usp) and the duration in which
the shock influences the LS area ( ts), i.e., lsp ∼ uspts. usp is the
outcome of the change of internal flow, and it can be connected to the
liquid flow velocity u
l (i.e., usp ∼ ul). The term ts is closely related to
the shock propagation outside of the droplet, and it can be connected
to the shock velocity u
s by ts ∼ /.0133 d0∕us/.0134/.0136/.0133 d0∕a0Ms/.0134 , where a0
is the sound speed in quiescent air. In this way, we present the
dimensionless SP displacement l∗sp /.0136 lsp∕d0 by a simple linear
approximation:
l∗sp /.0136 A ults
d0
/.0135 B /.0136 A ts
d0∕ul
/.0135 B /.0136 A ts
~t /.0135 B (9)
where d0 on the right-hand side of the first equals sign is used to
nondimensionalize the termults. The liquid flow velocity is obtained
qualitatively by ul ∼ ug
/.0129/.0129/.0129/.0129/.0129/.0129/.0129/.0129/.0129/.0129/.0129 /.0129ρg∕ρl
p as applied by Nicholls and Ranger
[17], which arises directly from an application of Newton’ss e c o n dl a w
to droplet displacement. The important measure of the intensity of the
interaction is given by the gas-flow dynamic pressure ( /.0133 1∕2/.0134 ρgu2g
behind the shock); the momentum flux changeρlu2
l inside the droplet
is proportional to/.0133 1∕2/.0134 ρgu2g as a prompt consequence of the interfacial
response to this gasdynamic impulse (i.e., ρlu2
l ∼ /.0133 1∕2/.0134 ρgu2g).
Therefore, the liquid velocity ul ∼ ug
/.0129/.0129/.0129/.0129/.0129/.0129/.0129/.0129/.0129/.0129/.0129 /.0129ρg∕ρl
p can be qualitatively
obtained. The term ~t /.0136 d0∕ul can be considered as a characteristic
time. A and B are constants to be determined.
Manipulating Eq. (9) and correlating the dimensionless SP
displacement to the incident shock strength, we have
l∗sp /.0136 A
d0
ug
/.0129/.0129/.0129/.0129/.0129ρg
ρl
r d0
us
/.0135 B
/.0136 A
/.0129/.0129/.0129/.0129/.0129ρ0
ρl
r 2/.0133 M2s − 1/.0134
Ms
/.0129/.0129/.0129/.0129/.0129/.0129/.0129/.0129/.0129/.0129/.0129/.0129/.0129/.0129/.0129/.0129/.0129/.0129/.0129/.0129/.0129/.0129/.0129/.0129/.0129/.0129/.0129/.0129/.0129/.0129/.0129/.0129/.0129/.0129/.0129/.0129/.0129/.0129/.0129/.0129/.0129/.0129/.0129/.0129/.0129/.0129/.0129
M2s /.0133 γ2 − 1/.0134/.0135 2/.0133 γ /.0135 1/.0134
p /.0135 B (10)
where ρ0 is the density in quiescent air, and γ /.0136 1.4 is the ratio of the
specific heats of air. Note that
ρg /.0136 ρ0
/.0133 γ /.0135 1/.0134 M2s
/.0133 γ − 1/.0134 M2s /.0135 2 (11)
ug /.0136
/.0018
1 − ρ0
ρg
/.0019
us (12)
Asymptotic conditions are employed to confine the correlation
between l∗sp and Ms in Eq. (10). When Ms approaches 1, the incident
shock is infinitely weak, and the SP is located at the center of the
droplet (i.e., l∗sp goes to 0.5). However, when Ms approaches infinity,
the SP reaches the LS (i.e., l∗sp goes to zero). From this, constants
A /.0136 −7.14 and B /.0136 0.5 are derived. Equation (10) relates the
stationary SP position solely to the incident shock strength Ms.
Following the preceding discussion, the relationship between l∗sp
and Ms in Eq. (10) is depicted in Fig. 9, together with the numerical
data in Fig. 8. It is seen that the theoretical prediction agrees well with
the numerical simulations. The characteristic internal flowfield
pattern with different incident shock strengths can be quantitatively
predicted, including the stationary SP position and the trajectories of
the WS and LS.
IV. Conclusions
In summary, the internal flow pattern of a single water droplet
under shock impact is investigated numerically and theoretically.
Similar internal flow patterns are found in cases with different
incident shock strengths, in which the SP forms and remains
stationary soon after the passage of the incident shock. With the
increase in the incident shock strength, the SP position varies, and the
droplet presents different morphologies. A simple theory is proposed
to predict the stationary position of SP in accordance with the incident
shock Mach number. This correlation connects the shock strength
with the droplet internal flowfield. It infers that the droplet internal
flow pattern is input into the droplet at the initial impact stage by the
shock rather than following the postshock airstream. Upon this point,
more research should be done in the near future.
Acknowledgments
This research was supported by projects of the Research Grants
Council of Hong Kong, under contracts CRF C5010-14E and GRF
152151/16E, and of the Natural Science Foundation of China,
number 11372265. The authors are very grateful to anonymous
referees for the time spent reading and analyzing the manuscript. The
many insightful remarks helped the authors improve the quality of
the paper.
Fig. 8 SP trajectories for cases with different incident shock strengths.
 Fig. 9 Comparison of numerical results and the theoretical prediction
of Eq. (10).
3386 GUAN ET AL.
Downloaded by Dalian University of Technology on August 31, 2026 | http://arc.aiaa.org | DOI: 10.2514/1.J057134

<!-- PDF_PAGE: 6 -->

References
[1] Wierzba, A., and Takayama, K., “Experimental Investigation of the
Aerodynamic Breakup of Liquid Drops,” AIAA Journal, V ol. 26, No. 11,
1988, pp. 1329–1335.
doi:10.2514/3.10044
[2] Guildenbecher, D., López-Rivera, C., and Sojka, P ., “Secondary
Atomization,” Experiments in Fluids, V ol. 46, No. 3, 2009, pp. 371–402.
doi:10.1007/s00348-008-0593-2
[3] Joseph, D. D., Belanger, J., and Beavers, G., “Breakup of a Liquid Drop
Suddenly Exposed to a High-Speed Airstream, ” International Journal
of Multiphase Flow, V ol. 25, No. 6, 1999, pp. 1263–1303.
doi:10.1016/S0301-9322(99)00043-9
[4] Theofanous, T., “Aerobreakup of Newtonian and Viscoelastic Liquids,”
Annual Review of Fluid Mechanics , V ol. 43, 2011, pp. 661–690.
doi:10.1146/annurev-fluid-122109-160638
[5] Igra, D., and Takayama, K., “Investigation of Aerodynamic Breakup
of a Cylindrical Water Droplet,” Atomization and Sprays, V ol. 11, No. 2,
2001, p. 20.
[6] Sembian, S., Liverts, M., Tillmark, N., and Apazidis, N., “Plane Shock
Wave Interaction with a Cylindrical Water Column,” Physics of Fluids,
V ol. 28, No. 5, 2016, Paper 056102.
[7] Wadhwa, A. R., Magi, V ., and Abraham, J.,“Transient Deformation and
Drag of Decelerating Drops in Axisymmetric Flows,” Physics of Fluids,
V ol. 19, No. 11, 2007, Paper 113301.
doi:10.1063/1.2800038
[8] Theofanous, T., Mitkin, V ., and Ng, C.,“The Physics of Aerobreakup. 3.
Viscoelastic Liquids,” Physics of Fluids , V ol. 25, No. 3, 2013, Paper
032101.
doi:10.1063/1.4792712
[9] Qu, Q., Ma, P ., Liu, P ., Li, S., and Agarwal, R. K.,“Numerical Study of
Transient Deformation and Drag Characteristics of a Decelerating
Droplet,” AIAA Journal, V ol. 54, No. 2, 2016, pp. 490–505.
[10] Shao, C., Luo, K., and Fan, J., “Detailed Numerical Simulation of
Unsteady Drag Coefficient of Deformable Droplet, ” Chemical
Engineering Journal, V ol. 308, Jan. 2017, pp. 619–631.
doi:10.1016/j.cej.2016.09.062
[11] Boiko, V ., and Poplavski, S.,“On the Dynamics of Drop Acceleration at
the Early Stage of V elocity Relaxation in a Shock Wave,” Combustion,
Explosion, and Shock Waves , V ol. 45, No. 2, 2009, pp. 198–204.
doi:10.1007/s10573-009-0026-4
[12] Shen, H., Wen, C.-Y ., and Zhang, D.-L., “A Characteristic Space–Time
Conservation Element and Solution Element Method for Conservation
Laws,” Journal of Computational Physics , V ol. 288, May 2015,
pp. 101–118.
doi:10.1016/j.jcp.2015.02.018
[13] Shen, H., and Wen, C.-Y ., “A Characteristic Space–Time Conservation
Element and Solution Element Method for Conservation Laws 2.
Multidimensional Extension, ” Journal of Computational Physics ,
V ol. 305, Jan. 2016, pp. 775–792.
doi:10.1016/j.jcp.2015.11.017
[14] Shen, H., Wen, C.-Y ., Parsani, M., and Shu, C.-W., “Maximum-
Principle-Satisfying Space-Time Conservation Element and Solution
Element Scheme Applied to Compressible Multifluids, ” Journal of
Computational Physics, V ol. 330, Feb. 2017, pp. 668–692.
doi:10.1016/j.jcp.2016.10.036
[15] Yi, X., Zhu, Y ., and Y ang, J.,“On the Early-Stage Deformation of Liquid
Drop in Shock-Induced Flow, ” edited by G. Ben-Dor, O. Sadot, and
O. Igra, Proceedings of the 30th International Symposium on Shock
Waves, V ol. 2, Springer, Cham, Switzerland, 2017.
[16] Engel, O. G., “Fragmentation of Waterdrops in the Zone Behind an Air
Shock,” Journal of Research of the National Bureau of Standards ,
V ol. 60, No. 3, 1958, pp. 245–280.
doi:10.6028/jres.060.029
[17] Nicholls, J., and Ranger, A., “Aerodynamic Shattering of Liquid Drops,”
AIAA Journal, V ol. 7, No. 2, 1969, pp. 285–290.
doi:10.2514/3.5087
P . Givi
Associate Editor
GUAN ET AL. 3387
Downloaded by Dalian University of Technology on August 31, 2026 | http://arc.aiaa.org | DOI: 10.2514/1.J057134
