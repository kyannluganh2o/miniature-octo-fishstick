<!-- PDF_PAGE: 1 -->

PHYSICAL REVIEW FLUIDS 6, 084304 (2021)
Droplet aerobreakup under the shear-induced entrainment
regime using a multiscale two-ﬂuid approach
Georgia Nykteri and Manolis Gavaises
School of Mathematics, Computer Science & Engineering, Department of Mechanical Engineering
& Aeronautics, City University of London, Northampton Square EC1V 0HB, United Kingdom
(Received 18 March 2021; accepted 27 July 2021; published 17 August 2021)
A droplet exposed to a high-speed gas ﬂow is subject to a rapid and violent fragmen-
tation, dominated by a widespread mist of multiscale structures that introduce signiﬁcant
complexities in numerical studies. The present work focuses on capturing all stages of
the aerodynamic breakup of a waterlike droplet imposed by three different intensity shock
waves, with Mach numbers of 1.21, 1.46, and 2.64, under the shear-induced entrainment
regime. The numerical investigation is conducted within a physically consistent and com-
putationally efﬁcient multiscale framework, using the /Sigma1-Y two-ﬂuid model with dynamic
local topology detection. Overall, the breakup of the deforming droplet and the subsequent
dispersion of the produced mist show good agreement with available experimental studies
in the literature. The major features and physical mechanisms of breakup, including the
incident shock wave dynamics and the vortices development, are discussed, and veriﬁed
against the experiments and the theory. While the experimental visualizations inside the
dense mist are restricted by the capabilities of the diagnostic methods, the multiscale
two-ﬂuid approach provides insight into the mist dynamics and the distribution of the
secondary droplets under different postshock conditions.
DOI: 10.1103/PhysRevFluids.6.084304
I. INTRODUCTION
The aerodynamic breakup of a liquid droplet imposed by a passing shock wave is a fundamental
problem with a wide spectrum of engineering interest, ranging from fuel injection in both internal
combustion [1–4] and rocket engines [ 5,6] to erosion damage in supersonic ﬂights [ 7,8]. Different
classiﬁcations for the droplet breakup regimes are reported in the literature and deﬁned based on
key dimensionless parameters, namely, the Weber number (We) at free-stream conditions and the
Ohnesorge number (Oh) for the liquid droplet, as follows:
We =
ρ
gu2
gd0
σ , Oh = μl√ ρlσd0
,
with d0 the initial droplet diameter, σ the surface tension coefﬁcient, ρg the postshock gas density,
ug the postshock gas velocity, ρl the liquid density, and μl the liquid dynamic viscosity.
The ﬁve classic breakup modes, known as vibrational, bag, bag-and-stamen (or multimode),
sheet-stripping (or sheet- thinning), and catastrophic regime, are summarized in a We-Oh regime
map for low Ohnesorge numbers (Oh ≪ 1) in the early review studies of Hinze [ 9], Pilch and
Erdman [10], and Faeth et al. [11]. Recently, Stefanitsis et al. [12–14] provided improved breakup
models for diesel droplets within the bag, bag-and-stamen, and sheet-stripping regimes and identi-
ﬁed an additional breakup mode, termed “shuttlecock,” which is observed during the aerodynamic
breakup of droplet clusters at low Mach numbers. On the other hand, Theofanous et al. [15]
2469-990X/2021/6(8)/084304(27) 084304-1 ©2021 American Physical Society

<!-- PDF_PAGE: 2 -->

GEORGIA NYKTERI AND MANOLIS GA V AISES
reclassiﬁed the classic droplet breakup modes into two principal regimes based on the govern-
ing interfacial instabilities, namely, the Rayleigh-Taylor piercing (RTP) and the shear-induced
entrainment (SIE) regime, introducing a broad and uniﬁed classiﬁcation for both Newtonian and
non-Newtonian droplets independent of the liquid viscosity and elasticity. Speciﬁcally, the RTP
regime concerns a moderate droplet fragmentation, driven by a gradual ﬂattening of the deforming
droplet and a subsequent penetration of its accelerating mass by one or more unstable Rayleigh-
Taylor waves. On the contrary, the SIE regime describes a chaotic fragmentation, deﬁned by the
prompt shear stripping from the droplet equator and followed by an extended entrainment of a
multiscale mist. Dominant mechanisms that induce the droplet breakup are the Kelvin-Helmholtz
instabilities, the capillary forces, and the turbulent mixing, as described by Theofanous [ 16]. For
low-viscosity liquids with Ohnesorge numbers Oh ≪ 1, the onset of the SIE regime is established
for Weber numbers above 10
3, while the transition zone between the RTP and SIE regimes occurs
for moderate Weber numbers in the range of 10 2–103.
Early experimental investigations of the SIE regime are focused on shadowgraphy experiments of
water droplets, in a ﬁrst attempt to depict and explain the stripping mechanism. Engel [17] examined
the fragmentation of a large (2.7 mm diameter) and a small (1.4 mm diameter) water droplet imposed
by three different shock waves of Mach numbers, 1.3, 1.5, and 1.7, in order to demonstrate the
inﬂuence of the sizes of rain droplets on high-speed rain-erosion damage. Additionally, Nicholls and
Ranger [18] considered incident shock waves with Mach numbers up to 3.5 and investigated the role
of various parameters in the droplet aerobreakup evolution, such as the droplet diameter, the breakup
time, the relative velocity between the droplet and the gas stream, and the liquid-to-gas density ratio.
Even though the macroscopic features of aerobreakup are revealed in both experimental studies
[17,18], namely, the liquid stripping from the droplet surface and the production of an extended
mist, the shadowgraphy method imposes limitations in displaying details of the internal structure
of the dense water cloud. Alternatively, pulsed laser holographic interferometry is proposed in
the experiments of Wierzba and Takayama [ 19] and Y oshida and Takayama [ 20] and provides
more clear and measurable visualizations of the shock-droplet interaction, the structure of the
disintegrating droplet, and the formation of a wake region behind the droplet under moderate Weber
numbers around 10
3 and Mach numbers between 1.3 and 1.56.
In current research, great emphasis is put on understanding the breakup mechanisms of liquid
droplets, other than water droplets, of both Newtonian and non-Newtonian nature, as shown in the
works of Theofanous and Li [21], Theofanous et al. [22,23], and Mitkin and Theofanous [24]. Using
laser-induced ﬂorescence (LIF), signiﬁcant ﬂow features are elucidated within a vast range of Weber
and Ohnesorge numbers, including the initial Kelvin-Helmholtz waves on the coherent droplet
surface and the development of different scales inside the dense mist at later stages of aerobreakup.
In the case of elastic liquids, it is observed that the SIE regime is not subject to capillary forces;
instead, the breakup initiates with the ruptures of extending liquid ﬁlms and ﬁlaments at signiﬁcantly
higher Weber numbers, referred to as shear-induced entrainment with ruptures (SIER). Furthermore,
recent studies in the literature investigate the effect of the postshock ﬂow on the initiation and
evolution of the aerobreakup. Wang et al. [25] examined the effect of the gas stream conditions
on the macroscopic breakup pattern and the ﬁnal dispersion of the produced secondary structures
for a constant Weber number at 1100 and varied postshock ﬂow Mach numbers in the range of
0.3–1.19. Speciﬁcally, the mist penetration and the fragment sizes show a dependency on the gas
stream conditions and, thus, a narrower mist of less uniform fragments is observed at the advanced
stages of aerobreakup under supersonic postshock conditions. Finally, Hébert et al. [26] presented
experiments for signiﬁcantly high Mach numbers between 4.2 and 4.6 and Weber numbers above
10
5 and deﬁned the three stages and characteristic times of the breakup mechanism in supersonic
postshock ﬂow, namely, the droplet deformation, the extended fragmentation, and the formation of
a ﬁlament from the remaining liquid mass.
An important but little-investigated feature of the shear-induced breakup mechanism concerns
the dynamics of the dense and polydisperse mist, which is forming and disintegrating as a re-
sult of the droplet fragmentation. Even with state-of-the-art laboratory apparatus available, the
084304-2

<!-- PDF_PAGE: 3 -->

DROPLET AEROBREAKUP UNDER THE SHEAR-INDUCED …
access to information about the dimensions of the produced structures within the mist remains
challenging. The attempts to obtain droplet size distributions from high-quality experimental data
visualizations in the up-to-date literature, employed by Hsiang and Faeth [ 27–29], Villermaux
[30], and Xu et al. [31], are restricted to cases with moderate breakup, falling in the transition
zone between the RTP and SIE regimes. Recent experimental studies of the SIE regime, such
as the works of Theofanous [ 16], Theofanous et al. [22], and Wang et al. [25], provide a thor-
ough investigation of the dominant physical mechanisms that inﬂuence the development of the
dispersed mist. However, a quantiﬁcation of the obtained fragment sizes inside the mist is not
available.
A key characteristic of the droplet aerobreakup under the SIE regime is the broad range of
spatial and temporal scales involved, which introduces additional difﬁculties in the accurate cap-
turing of the overall droplet deformation and fragmentation with the available numerical methods.
Two-dimensional simulations are suggested in the literature as a good compromise between the
assumption of a fully symmetric droplet fragmentation and the prohibitive computational cost of
a full-scale analysis. Speciﬁcally, the planar breakup of a cylindrical water column is a commonly
adopted simpliﬁed problem to study the shock-imposed breakup and the shear-stripping mechanism.
In the ﬁrst numerical study of the entire shear-induced breakup process, Chen [ 32] simulated the
aerobreakup of a water column after the impact with two different shock waves with Mach numbers
1.3 and 1.47, using the ﬁve-equation model of Saurel and Abgrall [ 33]. The simulations capture the
macroscale phenomena of the droplet deformation and displacement and show good agreement with
the experimental observations of Igra and Takayama [ 34]; however, the utilized diffuse interface
approach imposes limitations regarding the sharpness of the coherent droplet interface. Similarly,
with the use of the diffuse ﬁve-equation model of Allaire et al. [35], Meng and Colonius [ 36]
provided simulations for the water column aerobreakup within a broader range of conditions
with shock wave Mach numbers between 1.18 and 2.5; for the ﬁrst time, the development of a
recirculation region behind the deforming droplet was investigated. Sembian et al. [37] conducted
new experiments and simulations with the volume of ﬂuid (VOF) method for the early stages of
the shock–water column interaction for shock wave Mach numbers 1.75 and 2.4; details of the
shock wave motion are captured by the VOF method and a resolution of 440 cells per diameter.
Y ang and Peng [ 38] examined the effect of viscosity on the deformation of the liquid column,
using an adaptive mesh reﬁnement (AMR) method for higher spatial resolution. More recently,
Kaiser et al. [39] performed high-resolution simulations with adaptive mesh reﬁnement for the
benchmark case of Mach number 1.47, previously simulated by Chen [32], Meng and Colonius [36],
and Y ang and Peng [38], with an emphasis put on the more accurate prediction of the shock wave
dynamics, observed in the experiments of Igra and Takayama [ 40,41]. Overall, the two-dimensional
simulations of the shear-induced droplet breakup in the literature focus on the capturing of the
early stages of breakup and the shock wave dynamics, without investigating the later stages of
fragmentation and mist development.
Considering the high computational cost of a full-scale analysis, the limitation of the ordinary
numerical methods to accurately model all different-scaled structures remains the main source of
deviation between the simulation results and the experimental observations. Among the reported
three-dimensional simulations in the literature to date, Meng and Colonius [ 42] utilized an interface
capturing method and a moderate mesh resolution of 100 cells per original droplet diameter to
capture the macroscopic droplet deformation and achieved good agreement with the experimental
results of Theofanous et al. [22] for a shock wave Mach number 1.47 and postshock ﬂow Weber
number 780. Additionally, a Fourier analysis was performed to interpret the mechanisms of the
observed surface instabilities and the subsequent ligament breakup. Liu et al. [43] conducted both
axisymmetric and three-dimensional simulations to examine the aerobreakup mechanism under
supersonic conditions and identiﬁed signiﬁcant details of the liquid stripping and the vortices
development at the early stages of aerobreakup. In an attempt to investigate water dispersion,
Stefanitsis et al. [44] proposed a coupled VOF/Lagrangian approach to simulate the coherent
droplet and the produced droplets cloud, respectively. The obtained results predict the detachment of
084304-3

<!-- PDF_PAGE: 4 -->

GEORGIA NYKTERI AND MANOLIS GA V AISES
microscale droplets from the coherent droplet periphery, as depicted in the experimental visualiza-
tions of Theofanous et al. [22] with, however, a lack of physical input for the sizes of the produced
Lagrangian particles. Recently, an improved Eulerian/Lagrangian model was proposed by Kaiser
et al. [45] that allows a preset number of Lagrangian particles to detach from the droplet surface
and, later, evolve in size, following the gas stream ﬂow.
More sophisticated studies in the literature, including the direct numerical simulations (DNS)
performed by Chang et al. [46], demonstrate the developed Kelvin-Helmholtz instabilities on the
coherent droplet surface for a glycerol droplet impacted by a shock wave of Mach numbers 1.2 and
2.67. Additionally, the DNS study of Hébert et al. [26] reveals the characteristic stages and breakup
times of the aerobreakup process for a water droplet under supersonic conditions with a shock
wave Mach number equal to 4.24. The obtained results accurately capture the incident shock wave
propagation and the subsequent bow shock formation, as observed in the experiments conducted
by the same authors. However, despite the efﬁciency in computational resources, both DNS studies
mainly focus on the early-stage dynamics and avoid investigating the dimensions of the secondary
structures inside the dense water mist, which is captured as a detached but continuous ﬁlament in
the simulations by Hébert et al. [26] without any internal structures.
At the same time, thorough interpretations of all the stages of aerobreakup in the current literature
concern only studies with moderate Weber numbers in the transition zone between the RTP and SIE
regimes, namely, with Weber numbers in the range of 10
2–103. Speciﬁcally, Dorschner et al. [47]
presented a comprehensive analysis of the ligament formation and disintegration for the case of
a water droplet exposed to a shock wave of Mach number 1.3 and a subsequent postshock ﬂow
with Weber number 470. The conducted simulations, using a multicomponent model with interface
capturing and a moderate spatial resolution of 140 cells per diameter, accurately predict the recurrent
breakup mechanism of the produced ligaments in consistence with the experimental observations.
Additionally, in the studies of Jalaal and Mehravaran [48] and Jain et al. [49] a thorough quantitative
analysis of the fragments development is demonstrated, along with information for the number of
the fragments produced and secondary droplet size distributions. However, both numerical studies
investigate ﬂows with Weber numbers below 10
3 and, thus, concern the development of a relatively
light mist of distinguishable larger-scaled fragments. A summary of the key numerical studies
of droplet aerobreakup in the literature to date, the utilized numerical methods, the examined
conditions, and the experimental works used for validation is presented in Table I. Overall, ad-
ditional quantitative research is required to reveal all macroscopic and microscopic mechanisms
at the later stages of breakup and provide insight into the dense mist development under the SIE
regime.
Following the limitations and challenges of the commonly adopted numerical methodologies
for the simulation of droplet aerobreakup, there is a gap in the literature to date concerning a
detailed analysis of the dispersed mist development under the SIE regime, due to the dominance
of multiscale structures and the signiﬁcant computational cost of a full-scale analysis. The present
study proposes the multiscale two-ﬂuid approach, as previously developed by Nykteri et al. [50] and
outlined in Sec. II A, in order to investigate the multiscale features of droplet aerobreakup with a
viable computational cost. The multiscale two-ﬂuid approach employs a sharp interface method for
the deforming droplet interface and a physically consistent subgrid scale modeling for the produced
mist, using numerical models for the dominant subgrid scale mechanisms previously validated
and utilized in the literature for similar multiscale ﬂows and conditions [ 50,51]. The proposed
multiscale two-ﬂuid approach is now utilized in the droplet aerobreakup problem and is found
to predict accurately both the early-stage breakup mechanisms and the later-stage dispersion of
the produced fragments imposed by three different shock waves with Mach numbers 1.21, 1.46,
and 2.64, as presented in Sec. III and compared with the experimental observations of Theofanous
[16] and Theofanous et al. [22]. The interesting aspect of the present simulations is the thorough
quantitative analysis of the droplet fragmentation and the produced mist dynamics. Speciﬁcally,
during the early mist development, two stripping mechanisms are identiﬁed and investigated in
consistence with the experimental visualizations. Additionally, the differences in the early and later
084304-4

<!-- PDF_PAGE: 5 -->

DROPLET AEROBREAKUP UNDER THE SHEAR-INDUCED …
TABLE I. Summary of the key numerical studies of droplet aerobreakup in the literature to date.
Y ear Authors Numerical model Simulation Ms We Experiments
2008 Chen [32] Five-equation model [ 33] (diffuse interface method) 2D planar 1.3 3 .7 × 103 Igra and Takayama [34]
1.47 7 .4 × 103
2012 Jalaal and Mehravaran [ 48] AMR VOF method DNS – 38–400 Bremond and Villermaux [ 52]
Cao et al. [53]
2013 Chang et al. [46] MUSIC+ solver (high-order/AMR method) DNS 1.2 5 .2 × 102 Theofanous [16]
2.67 5 .4 × 104
2015 Jain et al. [49] AMR VOF method 3D – 20–120 Own
2015 Meng and Colonius [ 36] Five-equation model [ 35] (diffuse interface method) 2D planar 1.18–2.50 940–1 .9 × 104 Igra and Takayama [40,34]
2016 Sembian et al. [37] VOF method 2D planar 1.75 9 .5 × 104 Own
2.4 3 .8 × 105
2018 Liu et al. [43] Five-equation model [ 35] (antidiffusion method) 2D planar /3D 1.2–1.8 10 3 < We < 105 Sembian et al. [37]
(postshock M)
2018 Meng and Colonius [ 42] Five-equation model [ 35] (interface capturing method) 3D 1.47 780 Theofanous et al. [22]
2019 Y ang and Peng [38] AMR sharp-interface method 2D planar 1.47 7 .4 × 103 Igra and Takayama [41]
2020 Dorschner et al. [47] Multicomponent model with interface capturing 3D 1.3 470 Own
2020 Hébert et al. [26] Eulerian solver 2D axisymmetric / 4.24 1 .2 × 105 Own
DNS
2020 Kaiser et al. [39] AMR level-set method 2D planar 1.47 7 .4 × 103 Igra and Takayama [40,41]
2021 Kaiser et al. [45] Eulerian/Lagrangian method 2D planar 1.47 7 .4 × 103 Igra and Takayama [41]
2021 Stefanitsis et al. [44] VOF/Lagrangian method 2D planar 1.47 7 .4 × 103 Igra and Takayama [40]
3D 1.24 780 Theofanous et al. [22]
084304-5

<!-- PDF_PAGE: 6 -->

GEORGIA NYKTERI AND MANOLIS GA V AISES
mist development under subsonic and supersonic postshock conditions are demonstrated and a
physical interpretation is provided with respect to the evolution of the gas stream ﬂow. Finally,
a characterization of the droplets’ population inside the dense mist is obtained and analyzed
based on the modeled subgrid scale phenomena that govern the mist dynamics within the SIE
regime.
II. NUMERICAL MODELING
A. Numerical method and governing equations
The /Sigma1-Y two-ﬂuid model with dynamic local topology detection, reported by the present
authors [ 50], is utilized for the droplet aerobreakup simulations. The previously developed mul-
tiscale two-ﬂuid approach consists of a broad and numerically stable case-independent multiscale
framework and, thus, no modiﬁcations were required for the present simulations. Therefore, the
individual features of the proposed method allow for a physically consistent and numerically stable
investigation of the multiscale aspects of droplet aerobreakup within the multiscale framework.
Speciﬁcally, the implemented compressible two-ﬂuid approach, introduced by Ishii and Mishima
[54], provides remarkable advantages, due to the consideration of compressibility and slip velocity
effects; both ﬂow phenomena are responsible for inducing the droplet breakup mechanism under
the SIE regime. Additionally, the incorporation of the /Sigma1-Y model, which was initially proposed by
V allet and Borghi [55], contributes to a computationally efﬁcient full-scale analysis, since it provides
modeling solutions for the microscale droplets and the underlying subgrid scale phenomena inside
the widespread mist.
A fundamental feature of the multiscale framework is the topological detection of different
ﬂow regimes based on advanced on-the-ﬂy criteria. As a result, the most appropriate modeling
formulations are applied in each ﬂow region, remaining in coherence with the local mesh resolution.
Particularly in segregated ﬂow regions, which are present on the interface of the deforming but
still coherent droplet, the interface is fully resolved using the VOF sharp interface method [ 56,57].
On the contrary, inside the dispersed water mist with structures smaller than the local grid size,
the methodology applies a diffuse interface approach and incorporates an additional transport
equation for the interface surface area density /Sigma1[58] in order to model the unresolved subgrid
scale phenomena.
The multiscale two-ﬂuid approach has been implemented in
OPENFOAM with further devel-
opments on the TWOPHASEEULERFOAM solver, an available compressible, fully Eulerian implicit
pressure-based solver, in order to incorporate all the additional features of the multiscale framework,
namely, the interface sharpening method, the transport equation for the interface surface area density
/Sigma1, the subgrid scale models, and the switching mechanisms between the two formulations of
the numerical model. In principle, the multiscale two-ﬂuid approach consists of the same set of
governing equations under both formulations, namely, the sharp and the diffuse interface approach,
with speciﬁc source terms to be activated and deactivated depending on the currently operating
formulation of the solver, as it is described below.
1. Two-ﬂuid model governing equations
The volume averaged conservation equations governing the balance of mass, momentum, and
energy for each phase k are
∂
∂t (akρk ) + ∇ · (akρk uk ) = 0, (1)
∂
∂t (akρk uk ) + ∇ · (akρk uk uk ) =− ak ∇ p + ∇ ·
(
ak τeff
k
)
+ akρk g +
2∑
n=1
n̸=k
Mkn, (2)
084304-6

<!-- PDF_PAGE: 7 -->

DROPLET AEROBREAKUP UNDER THE SHEAR-INDUCED …
∂
∂t [akρk (ek + kk )] + ∇ · [akρk (ek + kk )uk ]
=− ∇ ·
(
ak qeff
k
)
−
[∂ak
∂t p + ∇ · (ak uk p)
]
+ akρk g · uk +
2∑
n=1
n̸=k
Ekn, (3)
where Mkn represents the forces acting on the dispersed phase and depends on local topology; the
surface tension force [ 59] is implemented under the sharp interface regime, while the aerodynamic
drag force [60] is implemented under the diffuse interface regime. Ekn demonstrates the heat transfer
between the liquid and gaseous phases, irrespectively of the ﬂow region. More details regarding the
closure of the interfacial interaction source terms are presented in the Appendix.
2. /Sigma1-Y Model transport equations
The transport equation for the liquid volume fraction in a compressible two-phase ﬂow is
∂al
∂t + ∇ · (al um ) + vtopo{∇ · [al (1 − al )uc]} = al ag
(ψg
ρg
− ψl
ρl
) Dp
Dt + al ∇ · um − (1 − vtopo )Ral ,
(4)
where vtopo distinguishes between the two different interface approaches by taking either the 0 or
1 value under a diffuse or sharp interface formulation, respectively. Interface sharpness is imposed
with the
MULES [61] algorithm in OPENFOAM, which introduces an artiﬁcial compression term in
Eq. (4). Additional modiﬁcations in the governing equations for coupling the VOF method with the
two-ﬂuid framework are presented in detail in the previous work of the authors [ 50]. Finally, as
discussed in the works of V allet et al. [62] and Andreini et al. [51], the term Ral accounts for the
liquid dispersion induced by turbulent velocity ﬂuctuations, which are important in dispersed ﬂows
and smaller scales.
The transport equation for the liquid gas interface surface area density /Sigma1[58] is described as
∂/Sigma1
′
∂t + ∇(/Sigma1′um ) = (1 − vtopo )
[
− R/Sigma1+ CSGS
/Sigma1
τSGS
(
1 − /Sigma1
/Sigma1∗
SGS
)]
, (5)
where the simultaneous existence of liquid and gas on the interface implies the presence of a
minimum interface surface area density, such as /Sigma1= /Sigma1′ + /Sigma1min, as shown by Chesnel et al. [63].
The term R/Sigma1represents the interface surface area diffusion due to turbulent velocity ﬂuctuations,
as derived by Andreini et al. [51]. The subgrid scale (SGS) source term, namely, the term SSGS =
CSGS /Sigma1
τSGS
(1− /Sigma1
/Sigma1∗
SGS
), accounts for all physical mechanisms which are responsible for local interface
formation and fall below the computational mesh resolution. Details regarding the closure of the
SGS source term are presented in the Appendix.
Knowing the interface surface area density, the diameter of a droplet inside the dispersed mist d/Sigma1
is calculated as the equivalent diameter of a spherical particle which has the same volume to surface
area ratio as the examined computational cell, proposed by Chesnel et al. [63]:
d/Sigma1= 6al (1 − al )
/Sigma1 , (6)
where αl represents the liquid volume fraction and /Sigma1the total liquid gas interface surface area
density, calculated in Eq. ( 5).
3. Flow topology detection algorithm
The implemented ﬂow topology detection algorithm identiﬁes instantaneous topological changes
in ﬂow regimes, evaluates the most appropriate numerical treatment for local interfaces, and allows
for a ﬂexible and stable two-way switching between the sharp and diffuse interface approaches. The
topological switching criteria are described in detail in the previous work of the authors [ 50].
084304-7

<!-- PDF_PAGE: 8 -->

GEORGIA NYKTERI AND MANOLIS GA V AISES
TABLE II. Shock wave and postshock conditions for the conducted droplet aerobreakup simulations.
Case Ms ps (Pa) Ts (K) ρs (kg/m3 ) us (m/s) W e Re
1 1.21 156187 340.4 1.6 110.87 1.6 × 103 1.6 × 104
2 1.46 235094 388 2.11 224.97 7 × 103 3.7 × 104
3 2.64 807006 683.9 4.11 654.9 1.23 × 105 1.6 × 105
B. Problem deﬁnition and simulation setup
The droplet aerobreakup is examined for a waterlike droplet with an initial diameter of 1.9 mm,
namely, a tributyl phosphate (TBP) droplet with density ρ = 978 kg/m3 and dynamic viscosity
μ = 4 × 10− 3 Pa s, similar to water properties, but a very low surface tension of σ = 0.027 N/m.
The numerical simulations are conducted for three different shock waves that impact the droplet and
correspond to a subsonic, transonic, and supersonic postshock gas stream. The simulation results are
compared with the experimental observations of Theofanous [ 16] and Theofanous et al. [22]f o rt h e
same aerobreakup cases. The three examined cases comprehensively cover the range of the available
experimental conditions for low-viscosity liquids within the SIE regime in the literature, as depicted
in the regimes map in [ 22]; the onset of the SIE regime is deﬁned for Weber numbers greater
than 10
3 and demonstrates a moderate shear-induced aerobreakup, while the most intense and
violent fragmentation is observed for signiﬁcantly higher Weber numbers above 10 5 and supersonic
postshock ﬂow conditions.
Table II summarizes the Mach numbers of the propagating shock waves, the postshock ﬂow
conditions, and the Weber and Reynolds numbers calculated for the gas properties at postshock
conditions. The postshock gas stream properties are also used for the nondimensionalization of the
ﬂow ﬁelds, as shown in Meng and Colonius [ 42], in order to obtain a direct comparison between the
different cases.
The droplet aerobreakup simulations are performed in a two-dimensional (2D) axisymmetric
geometry with one cell thickness in the azimuthal direction, using two computational meshes with
a resolution of 100 and 200 cells per original droplet diameter around the area of interest. The
computational domain is sufﬁciently large to avoid nonphysical reﬂections on the borders and
Neumann boundary conditions are applied for all the computed ﬂow ﬁelds. The simulations are
initiated with the shock wave being one diameter away from the center of the droplet. Details of the
initial conﬁguration and the computational mesh are illustrated in Fig. 1.
DNS studies in the literature [ 43,46] utilized a computational mesh of more than 1000 cells per
diameter to solve the viscous boundary layer and predict the Kelvin-Helmholtz instabilities. How-
ever, due to the signiﬁcant computational cost, these DNS studies are restricted to the demonstration
of the early-stage instabilities on the coherent droplet surface and do not examine the later-stage
fragmentation and mist development, which is the main objective of the current simulations. On
the contrary, the utilized spatial resolution of 100 and 200 cells per original diameter is commonly
selected in the literature, for instance, in the simulations of [ 26,42,44,47], and is proven to capture
accurately the macroscopic deformation of the coherent droplet surface, while the investigation of
the Kelvin-Helmholtz instabilities remains out of scope in the present study.
The two characteristic scales that determine the onset of the droplet aerobreakup under the
SIE regime are the characteristic viscous velocity u
+
V = νl
d0
∼= 9 × 10− 6 m/s and the characteristic
capillary velocity u+
C =
√
σ
d0ρl
∼= 0.12 m/s, as deﬁned by Theofanous [ 16]. The viscous velocity is
related to the unresolved Kelvin-Helmholtz instabilities inside the viscous boundary layer, while the
capillary velocity balances the stripping actions of the developed wake on the droplet surface and the
surface tension force that restrains the liquid detachment. With respect to the characteristic scales of
turbulence, the Kolmogorov velocity scale is around ∼ 0.1 m/s in subsonic case 1 and it rises to ∼ 1
m/s in supersonic case 3. At the same time, the secondary droplets produced inside the mist have
084304-8

<!-- PDF_PAGE: 9 -->

DROPLET AEROBREAKUP UNDER THE SHEAR-INDUCED …
FIG. 1. Initial conﬁguration and information regarding the computational mesh for the simulation of
droplet aerobreakup.
diameters in the range of 0.01–19 μm, while the Kolmogorov length scale is of the order of ∼ 0.5
μm in the three examined cases. Therefore, turbulence effects are becoming more signiﬁcant under
supersonic postshock conditions and are responsible for the breakup of the smallest-scaled droplets.
In the present simulations, the ﬂow turbulence is considered using Large Eddy Simulations
(LES) with the implementation of the one-equation SGS model of Lahey [ 64]. However, the
utilized 2D axisymmetric geometry with one cell thickness in the azimuthal direction imposes
limitations regarding the accurate capturing of the turbulent state, which corresponds to fully
three-dimensionally (3D) developed phenomena. Speciﬁcally, the simulation is initialized without
turbulence in the ﬂow ﬁeld and, thus, the instantaneous velocity ﬁeld is 2D. Therefore, in the absence
of developed turbulence or a developed turbulent boundary layer at the initial conditions, the LES
approximation can be applied in the present geometry of one cell thickness in the azimuthal direction
without signiﬁcant limitations. Additionally, Stefanitsis et al. [65] depicted that the assumption of
a symmetrical ﬂow ﬁeld around the deforming droplet under the inﬂuence of turbulence and vortex
shedding does not affect the shape of the coherent droplet; however, it can have an inﬂuence on
the trajectory and the breakup time of the fragments. Hence, the present axisymmetric geometry
can adequately predict the coherent droplet deformation and fragmentation with minor limitations
regarding the produced fragments’ motion due to the absence of the stochastic character of a fully
developed turbulent ﬁeld. At the same time, key numerical studies in the literature [ 26,36,42,43,39]
exclude the consideration of turbulence effects, without a limitation in capturing the dominant
macroscopic phenomena of the aerobreakup evolution, while DNS studies [ 26,46] do not report
any signiﬁcant difference or previously unrevealed mechanisms in the ﬂow ﬁeld due to the resolved
turbulence. Consequently, despite the discussed limitations, the utilized 2D axisymmetric geometry
with one cell thickness in the azimuthal direction is an acceptable compromise between an adequate
turbulence model and a viable computational cost.
Regarding the numerical simulation setup, the spatial discretization used is based on second-
order accurate discretization schemes. Time stepping is performed adaptively during the simulation
to respect the selected limit for the convective Courant-Friedrichs-Lewy (CFL) condition of 0.2.
Finally, the thermodynamic closure of the system is achieved by implementing the stiffened gas
equation of state, proposed by Ivings et al. [66], for the liquid phase and the ideal gas equation
084304-9

<!-- PDF_PAGE: 10 -->

GEORGIA NYKTERI AND MANOLIS GA V AISES
FIG. 2. Droplet aerobreakup in case 1. (i) Comparison between the experimental visualizations of Theo-
fanous et al. [22]( t∗ = 0.20, 0.38) and Theofanous [ 16]( t∗ = 0.53), the simulation results of the deforming
coherent droplet (red isoline for water volume fraction value 0.5), and the produced water mist (yellow
isosurface for water volume fraction values higher than 10
–5). (ii) 3D reconstructed results. (iii) Dimensions
of the secondary droplets inside the mist. (iv) Air and water velocity magnitudes (top) and vorticity streams
(bottom).
of the state for the gaseous phase, which can perform adequately even under supersonic postshock
conditions, as shown in Hébert et al. [26].
III. RESULTS AND DISCUSSION
The numerical investigations of the droplet aerobreakup using the proposed multiscale two-ﬂuid
approach are presented for the three cases of Table II in Figs. 2–4, respectively, and compared
with the corresponding experimental observations of Theofanous [ 16] and Theofanous et al. [22].
Following the pass of the shock wave, the small-scale interfacial instabilities on the droplet surface
and the pressure differences between the upstream and downstream side of the droplet impose
a gradual deformation of the initially spherical droplet into a ﬂattened shape. The deforming
coherent droplet interface is captured using the VOF method and illustrated with red isolines in
Figs. 2(i), 3(i), and 4(i). As can be observed for the three simulated cases, the macroscopic defor-
mation of the coherent droplet interface shows a good qualitative agreement with the experimental
results, following satisfactorily the spanwise expansion and the ﬂattening of the back side of the
droplet.
084304-10

<!-- PDF_PAGE: 11 -->

DROPLET AEROBREAKUP UNDER THE SHEAR-INDUCED …
FIG. 3. Droplet aerobreakup in case 2. (i) Comparison between the experimental visualizations of Theo-
fanous et al. [22]( t∗ = 0.23) and Theofanous [ 16]( t∗ = 0.29, 0.43), the simulation results of the deforming
coherent droplet (red isoline for water volume fraction value 0.5), and the produced water mist (yellow
isosurface for water volume fraction values higher than 10
–5). (ii) 3D reconstructed results. (iii) Dimensions
of the secondary droplets inside the mist. (iv) Air and water velocity magnitudes (top) and vorticity streams
(bottom).
At the same time, the large-scale droplet deformation is followed by an extended fragmentation,
which initiates due to liquid stripping from the droplet surface and results in the formation of a
dispersed mist of microscale structures. The produced mist is simulated within the diffuse interface
formulation of the multiscale framework, while numerical models are introduced for consideration
of the unresolved subgrid scale phenomena. Speciﬁcally, during the early stages of aerobreakup,
liquid stripping is observed initially from the droplet equator and later from the back side of the
droplet with the two streams colliding into a primary stream and forming a widespread mist, as
shown in Figs. 2(i), 3(i), and 4(i) and previously discussed in the study of Liu et al. [43]. The main
stripping mechanism, which is responsible for the production of the primary stream, is enhanced
by the growing vortices formed on the back side of the droplet; the vortices interact with the
droplet surface and enhance the existing mist with additional fragments, as illustrated in Figs. 2(iv),
3(iv), and 4(iv). Even though the near-stagnation region remains relatively ﬂat, as observed in the
experimental visualizations of Theofanous [ 16] and Theofanous et al. [22], a secondary stream of
fragments is detached from the front side of the droplet. Unlike the main stripping mechanism,
which is dominated by the local ﬂow vorticity, the secondary stripping mechanism is acting on the
high-pressure side of the droplet and is driven by the interfacial instabilities on the droplet surface,
the strong shear, and the aerodynamic conditions around the droplet. As a result, the produced
084304-11

<!-- PDF_PAGE: 12 -->

GEORGIA NYKTERI AND MANOLIS GA V AISES
FIG. 4. Droplet aerobreakup in case 3. (i) Comparison between the experimental visualizations of Theo-
fanous et al. [22]( t∗ = 0.18, 0.29) and Theofanous [ 16]( t∗ = 0.52), the simulation results of the deforming
coherent droplet (red isoline for water volume fraction value 0.5), and the produced water mist (yellow
isosurface for water volume fraction values higher than 10
–5). (ii) 3D reconstructed results. (iii) Dimensions
of the secondary droplets inside the mist. (iv) Air and water velocity magnitudes (top) and vorticity streams
(bottom).
secondary stream is more pronounced with an increase of the incident shock wave Mach number, as
observed in Fig. 4(i), since the supersonic postshock conditions impose higher local pressure and gas
stream velocities and, thus, amplify the aerodynamic forces on the front side of the droplet. Finally,
the primary and secondary streams of fragments merge, following the free-stream gas ﬂow and the
aerodynamic force imposed by the upstream and downstream pressure differences, and create a
dense mist layer around the deforming droplet in consistence with the experimental observations.
At the late stages of fragmentation, secondary structures continue to detach from the surface of the
elongated but still coherent body of the deformed droplet, while the penetration and dispersion of
the produced mist dominate the breakup mechanism.
The dimensions of the produced droplets inside the dense mist are obtained in coherence with the
evolution of the interface surface area, considering turbulence, droplet collision and coalescence,
and secondary breakup effects within the multiscale framework. The largest secondary droplets
with a maximum diameter of 19 μm are detected close to the coherent droplet and on average
around the droplet equator and the droplet ﬂattened back side, as illustrated in Figs. 2(iii), 3(iii),
and 4(iii). Thus, based on the liquid stripping mechanism, the largest captured secondary droplets
are detached from the coherent droplet under the inﬂuence of the main stripping mechanism and are
embedded in the primary stream of fragments. Additionally, in the supersonic case 3 in Fig. 4(iii),
084304-12

<!-- PDF_PAGE: 13 -->

DROPLET AEROBREAKUP UNDER THE SHEAR-INDUCED …
signiﬁcantly large droplets close to the maximum diameter are also observed on the droplet front
side during the later stages of fragmentation, when the secondary stripping mechanism contribution
to the overall droplet aerobreakup is remarkable. The maximum diameter is correlated with the local
mesh resolution for a mesh of 100 cells per initial diameter and, thus, the size limit for structures
that can be resolved with the VOF method. Details about the upper limit of the subgrid diameters
with respect to the local grid resolution are presented in the Appendix. In the review study of Pilch
and Erdman [ 10], the largest fragments detached from the droplet equation are approximately one
to two orders of magnitude smaller than the original droplet, which is in agreement with the newly
detached fragments captured by the multiscale two-ﬂuid approach. At the same time, the smallest
subgrid scale droplets observed downstream have diameters in the range of 0.01–0.1 μm, without
the numerical model to impose a lower diameter limit. These microscale droplets are visible as
a cloud but cannot be quantiﬁed in the experiment and, thus, there is no experimental input for
the smallest droplet sizes. However, the signiﬁcant extent of the secondary droplets’ interactions
inside the dense mist can justify the production of the detected smallest sizes, while the exclusion
of vaporization effects from the performed simulations can be related with the possible longer-
term presence of the smallest secondary droplets inside the dense mist. During the earlier stages of
aerobreakup, the small-scale secondary droplets with diameters below 1 μm are mostly observed
downstream at the edges of the forming mist. Later, these are trapped inside the extended mist that
continuously increases in volume and recirculates behind the deforming droplet.
A driving mechanism for the aerodynamically imposed breakup and characteristic feature of
the water dispersion evolution is the recirculation of the produced secondary droplets within the
water mist. As depicted in Figs. 2(iv), 3(iv), and 4(iv) and discussed in the simulations of Meng
and Colonius [ 42], the interaction of two counter-rotating vortices is the key mechanism for the
formation of a dominant wake recirculation region behind the deforming droplet. In the course of
fragmentation, more secondary vortices with varying length scales and spatial arrangement form
in the wake between the convex front side and the ﬂattened back side of the coherent droplet and
are responsible for its deforming shape. Focusing on the effect of the propagating shock wave on
the dynamics of the produced water mist, an increased Mach number results in a postshock ﬂow
with an extended streamwise but relatively limited spanwise recirculation zone behind the droplet,
as illustrated in Figs. 2(iv), 3(iv), and 4(iv). The free-stream gas velocity shows similar behavior
irrespectively of the Mach number with maximum values up to 1.5 times the initial postshock
velocity, observed in the region above the droplet equator and extending downstream along the
negative vorticity side of the primary wake. At the same time, the secondary droplets that are
subject to a vortical ﬂow show maximum and minimum velocity values in antidiametrical positions
along the primary recirculation region independent of the underlying droplet sizes. As highlighted
in Figs. 2(iv), 3(iv), and 4(iv), the maximum velocity values are observed for the secondary droplets
located along the upper and lower side of the primary wake, while the minimum velocity values
are found above the droplet back side and downstream on the right side of the primary wake.
Following the dominance of the vortical mechanism over time, the maximum velocity values among
the secondary droplets gradually increase, until they reach or even slightly exceed the gas steam
velocity values at the initial postshock conditions, namely, 110.87, 224.97, and 654.9 m /s, for
cases 1, 2, and 3, respectively. While the minimum velocity values in the droplets’ recirculation
region approach zero, the newly detached fragments from the back side of the droplet do not remain
stagnant. Nevertheless, they are embedded in the primary stream of fragments that is continuously
enhanced and governed by the developed ﬂow vorticity.
Focusing on the early-stage deformation in Fig. 5, the droplet surface isolines, obtained from the
experimental results in the work of Theofanous et al. [22], are compared against the numerical
isolines for two different mesh resolutions of 100 and 200 cells per initial droplet diameter.
The droplet surface deformation is adequately predicted by the conducted simulations and only
minor deviations from the experimental isolines are observed on the tip of the ﬂattened back side
of the droplet, where the numerical method already detects detached fragments, as depicted in
Figures 2–4. Additionally, the good agreement between the simulation results with the utilization
084304-13

<!-- PDF_PAGE: 14 -->

GEORGIA NYKTERI AND MANOLIS GA V AISES
FIG. 5. Coherent droplet isolines. Comparison between the experimental isolines of Theofanous et al. [22]
(black dashed line) and the simulation isolines for volume fraction value 0.5 using a computational mesh with
100 (red solid line) and 200 (blue solid line) cells per initial droplet diameter. The arrows point to the small
deviations between the experimental and simulation isolines.
of a coarse and a ﬁne computational mesh demonstrates that a moderate mesh resolution of 100
cells per initial diameter is sufﬁcient to resolve the large-scale droplet deformation. The sharpness
of the numerical solution is examined in Fig. 6, obtaining the droplet surface isolines from different
values of the liquid volume fraction and considering more advanced droplet deformation. As
illustrated in Fig. 6, the coherent droplet interface remains sufﬁciently sharp even at the late stages
of aerobreakup. Some minor differences are observed on the upper tip of the deformed droplet
interface and the detached large-scale secondary droplets.
The intensity of the incident shock wave imposes the occurring postshock ﬂow conditions and is
crucial for the droplet deformation and the consequent water dispersion. In the subsonic case, shown
in Fig. 7(a), when the shock wave with Mach number 1.21 impacts the stagnant droplet, the local
pressure increases at approximately 2 bars. At the same time, the incident shock wave continues to
084304-14

<!-- PDF_PAGE: 15 -->

DROPLET AEROBREAKUP UNDER THE SHEAR-INDUCED …
FIG. 6. Coherent droplet isolines for different water volume fraction values, using a computational mesh
with 100 cells per initial droplet diameter. Produced water mist isosurface for water volume fraction values
higher than 10
–5 (gray). Comparison between cases 1, 2, and 3 at time instances that correspond to a decrease
for the width of the deforming droplet by 10%, 25%, and 50%. The arrows point to the small deviations in
interface sharpness with different volume fraction values.
propagate downstream, and a reﬂected shock wave is established on the front side of the droplet and
initiates its upstream propagation. The developed postshock ﬂow conditions are characterized by
moderate pressure difference around the droplet and maximum local Mach number values at about
0.45. The transonic case of Fig. 7(b) shows similar behavior; however, the slower propagation of the
reﬂected shock wave and the higher local Mach numbers lead to a more widespread fragmentation.
On the contrary, in the supersonic case of Fig. 7(c) the strong shock wave with Mach number
2.64 results in a signiﬁcant increase of the local pressure at 35 bars after impact. The subsequent
reﬂected shock wave stabilizes close to the droplet as a detached bow shock. As a result, the ﬂow
084304-15

<!-- PDF_PAGE: 16 -->

GEORGIA NYKTERI AND MANOLIS GA V AISES
FIG. 7. Gas stream conditions during the droplet aerobreakup, while the incident shock wave lies at the
same distance from the center of the droplet. Pressure ﬁeld and produced water mist evolution (top). Numerical
schlieren images and Mach number isolines (bottom).
conditions around the droplet remain supersonic with maximum local Mach number values above
2 that impose a signiﬁcantly faster and more violent droplet fragmentation, which appears as a very
dense and extensive dispersed mist downstream, also observed in the experiments of Hébert et al.
[26] for similar Weber numbers.
The widespread water dispersion in the form of a dense mist is the major fragmentation pattern
under the SIE regime. An insight into the dimensions of the produced secondary droplets within
the mist is presented in Fig. 8, depicting the volume concentration of different droplet classes over
the total volume of the dispersed region, as captured by the numerical model for the three cases
in Table II. A signiﬁcant advantage of the conducted numerical simulations is the consideration
of every ﬂuid structure that forms as part of the ﬂow development without excluding small sizes,
thus providing information for sizes below the 5 μm/pixel resolution of the camera utilized in
the reported experiments and illustrated in gray in Fig. 8. The ﬁrst secondary droplets produced
in all three cases are small structures, with more than 60% of the diameters in the total volume
being below 1 μm; these droplets are forming due to the initial liquid stripping from the droplet
equator, as observed in the experiments at the very early stages of aerobreakup. Shortly after, the
large-scale fragmentation is established when droplets with diameters above 5 μm are detached
084304-16

<!-- PDF_PAGE: 17 -->

DROPLET AEROBREAKUP UNDER THE SHEAR-INDUCED …
FIG. 8. V olume concentration of the secondary droplets with diameters between 5 and 19 μm( g r a y ) ,1
and 5 μm (blue), and lower than 1 μm (yellow) over the total volume of the dispersed region. The volume
concentration of the dispersed region over the total volume of the water phase is plotted in red. The green
vertical lines correspond to a decrease for the width of the deforming droplet by 10%, 25%, and 50%.
from the coherent droplet surface and, thus, an additional class of larger droplets, colored in gray, is
included in the distributions of Fig. 8 at 42, 20, and 7.1 μs for cases 1, 2, and 3, respectively.
Considering the evolution of the population of secondary droplets over time, larger droplet sizes
above 1 μm become more signiﬁcant in the population with increasing Mach number, as observed
in Fig. 8 for cases 2 and 3. There are two crucial parameters that inﬂuence the secondary droplets’
distribution—ﬁrst, the sizes of the newly detached fragments from the coherent droplet surface and,
second, the subgrid scale droplet interactions inside the existing dispersed mist. Speciﬁcally, an
increase of the incident shock wave Mach number imposes a violent droplet fragmentation with
extended liquid stripping from the droplet surface due to severe aerodynamic conditions around
the droplet and the dominance of the secondary stripping mechanism. As a result, large-scale
droplets continue to fragment from the coherent droplet surface and enhance the secondary droplets
population even during advanced stages of the aerobreakup process, as depicted in the distributions
of Figs. 8(ii) and 8(iii) for the class of the largest droplets with diameters between 5 and 19 μm and
also illustrated in Figs. 3 and 4 for the indicated time instances.
Following the production of the new fragments, the subgrid scale droplet interactions are
responsible for the further evolution of the secondary droplet sizes inside the dispersed mist. The
required subgrid scale modeling is performed within the multiscale framework using the transport
equation for the interface surface area, Eq. ( 5); the mechanisms that determine the local interface
formation, namely, turbulent mixing, droplet collision and coalescence, and secondary breakup
effects, are modeled as individual source terms S
SGS. A positive contribution of the SGS source
term corresponds to an increase of the local interface surface area and physically correlates with
the evolution of the underlying subgrid scale droplets into smaller diameters, while a negative SGS
source term value describes a decrease of the local interface surface area due to the creation of
subgrid scale droplets with larger diameters. The secondary breakup mechanism can only result in
the further breakup of the existing secondary droplets inside the mist and, thus, has only a positive
contribution in the SGS source term. Details regarding the calculation of the SGS source term are
presented in the Appendix.
Figure 9 represents the volume concentration of the three subgrid scale mechanisms that con-
tribute positively to the local interface surface area production and the creation of smaller-scaled
droplets, namely, the ﬂow turbulence, droplet collision, and secondary breakup effects, over the
total volume of the dispersed region, as calculated in Eq. ( 5) for the three examined cases. In
case 1, the subgrid scale turbulence and collision effects contribute to the production of the local
interface surface area by above 90%, already at the early stages of aerobreakup, while the secondary
breakup effects, governed by the relative velocity between the liquid and gaseous phases, are absent
under the subsonic postshock conditions. Overall, the predominant pattern is the further decrease
084304-17

<!-- PDF_PAGE: 18 -->

GEORGIA NYKTERI AND MANOLIS GA V AISES
FIG. 9. V olume concentration of the subgrid scale mechanisms, namely, turbulence, droplet collision, and
secondary breakup, that contribute positively to the local interface surface area production and the creation of
smaller-scaled droplets over the total volume of the dispersed region. The green vertical lines correspond to a
decrease for the width of the deforming droplet by 10%, 25%, and 50%.
of the secondary droplets’ sizes inside the dispersed mist, which is also reﬂected in the droplet
population in Fig. 8(i), highlighting an increase and dominance of the smallest scales over time. A
distribution of uniformly small-scaled fragments is also demonstrated in the experiments of Wang
et al. [25] at subsonic postshock ﬂows. In case 2, shown in Fig. 9(ii), the creation of smaller-scaled
droplets, driven by the local turbulence and collision, remains dominant for the mist evolution
with a minor decrease compared to case 1. Additionally, the secondary breakup mechanism is not
completely absent and has a small contribution in the mist dynamics. Therefore, the slightly reduced
concentration of the class of droplets with the smallest diameters below 1 μm, as depicted in the
distribution in Fig. 8(ii), is a combination of the enhancement of the larger-scaled new fragments
under the transonic postshock conditions and the small decrease of the subgrid scale interface
surface area production.
Finally, case 3, presented in Fig. 9(iii), demonstrates the signiﬁcant inﬂuence of the supersonic
postshock conditions on the subgrid scale mechanisms. Speciﬁcally, even though the ﬂow turbulence
maintains a major positive contribution to the production of smaller-scaled droplets, the collision
effects are remarkably reduced by coalescence that becomes signiﬁcant after the early stages of
aerobreakup, even before the width of the deforming droplet is decreased by 10%. The coalescence
of the secondary droplets enhances the droplet population with larger-scaled droplets and explains
the decreased concentration of the droplet class with the smallest diameters, observed approximately
after 10 μsi nF i g . 8(iii). As illustrated in Fig. 10, coalescence effects are present in the region
of the main stripping mechanism, namely, close to the droplet equator and the back side of the
deforming droplet. During the evolution of aerobreakup, the coalescence region expands, driven by
the increasing local ﬂow vorticity. Similarly, in the study of Wang et al. [25], the presence of larger
fragments among the dominant microdroplets is observed at the advanced stages of aerobreakup
under supersonic postshock conditions. As discussed in [ 25] and in agreement with the present
subgrid scale analysis, these nonuniform fragments coalesce into larger secondary droplets, as
imposed by the local ﬂow conditions and the limited spanwise spread on the produced dense mist. At
the same time, the secondary breakup shows a considerable and gradually increasing contribution to
the mist evolution over time, as depicted in Fig. 9(iii). The secondary breakup mechanism is mainly
established on the droplet front side, shown in Fig. 10, where the secondary stripping mechanism
dominates and the relative velocity between the newly detached droplets and the supersonic gas
ﬂow locally exceeds the value of 200 m /s. However, the secondary breakup of subgrid scale
droplets is not contributing signiﬁcantly to the increase of the population of the smallest droplets,
since it involves, on average, the breakup of large-scaled droplets with diameters above 2 μm, as
084304-18

<!-- PDF_PAGE: 19 -->

DROPLET AEROBREAKUP UNDER THE SHEAR-INDUCED …
FIG. 10. Droplet aerobreakup in case 3 at time instances that correspond to a decrease for the width of
the deforming droplet by 10%, 25%, and 50%. Regions in the dispersed mist where the droplet coalescence
(purple) and secondary breakup (red) are present (top). Dimensions of the secondary droplets inside the mist
(bottom).
demonstrated in Fig. 10 for the time instances that correspond to a decrease for the width of the
deforming droplet by 10%, 25%, and 50%.
Lastly, the volume concentration of the water mist over the total volume of the water phase
is reduced by approximately 10% in case 3 compared to the lower Mach number cases 1 and 2
for the same width deformation, as shown in Fig. 8(iii). At the early stages of aerobreakup, the
limited mist concentration is related with the postponed breakup initiation, also observed in the
experiments of Wang et al. [25] at supersonic postshock conditions. However, at the later stages
of aerobreakup, the stripping mechanism becomes more signiﬁcant under the inﬂuence of both
the main and the secondary stripping mechanisms, depicted in Fig. 6 in comparison with cases
1 and 2, leading to an extended and violent stripping from the coherent droplet surface. On the
contrary, during the later stages of the aerobreakup process, the mist dynamics, governed by the
modeled subgrid scale mechanisms, play a major role in the evolution of the dispersed mist. In
particular, as highlighted in Fig. 9(iii) and discussed previously, the remarkable coalescence effects
result in the destruction of the local interface surface area and, thus, act against the further expansion
of the existing mist. At the same time, the violent fragmentation under the supersonic postshock
conditions along with the increasing ﬂow vorticity behind the deforming droplet impose the mist
into a rapid downstream penetration. Therefore, the expansion of the dispersed mist in the spanwise
direction is restricted compared to the cases with lower Mach numbers due to the severe gas stream
conditions. Likewise, in the experiments of Wang et al. [25] a signiﬁcantly narrower mist expansion
is observed at supersonic conditions. In conclusion, the supersonic postshock conditions impose the
development of a relatively reduced mist with the signiﬁcant presence of larger-scaled droplets until
the advanced stages of aerobreakup.
IV . CONCLUSION
The aerodynamic breakup of a waterlike droplet under the SIE regime, imposed by three different
shock waves with Mach numbers 1.21, 1.46, and 2.64, has been investigated using the proposed
multiscale two-ﬂuid approach. The present numerical study provided the opportunity to verify the
physical mechanisms of aerobreakup and scrutinize aspects of the process that were not evident in
the experimental visualizations of Theofanous [ 16] and Theofanous et al. [22], using a physically
consistent methodology with a viable computational cost. Speciﬁcally, the deformation of the
coherent droplet interface was fully resolved by the local mesh resolution using the VOF sharp
interface method, while the produced mist of secondary fragments was modeled under the diffuse
interface approach with consideration of subgrid scale phenomena, namely, turbulent mixing,
droplet collision and coalescence, and secondary breakup effects.
084304-19

<!-- PDF_PAGE: 20 -->

GEORGIA NYKTERI AND MANOLIS GA V AISES
During the early-stage mist development, two stripping mechanisms were identiﬁed to act on
the coherent droplet surface. The main stripping mechanism is responsible for the formation of the
primary stream of fragments, detached from the droplet equator and the droplet ﬂattened back side,
while the secondary stripping mechanism is present on the droplet front side and becomes more
signiﬁcant at supersonic postshock conditions. The largest detached fragments were observed, on
average, on the locations of the local liquid stripping and, subsequently, the fragment sizes evolve
inside the mist, following the gas stream ﬂow evolution. The postshock ﬂow conditions and the
development of a dominant recirculation region behind the deforming droplet play a major role in
the formation and expansion of the produced mist. In a supersonic postshock ﬂow, the dispersed mist
appears relatively narrower, due to severe aerodynamic conditions that establish a rapid downstream
penetration.
Details for the secondary droplets’ population and the evolution of the droplets sizes inside the
mist were obtained and analyzed based on the modeled subgrid scale phenomena and the local
ﬂow development. At supersonic postshock conditions, the coalescence and secondary breakup
mechanisms become more pronounced. Additionally, the droplet size distribution is enhanced
with larger-scaled droplets even at the later stages of aerobreakup. As a result, the limited mist
concentration under supersonic postshock conditions is an outcome of the restricted spanwise
expansion of the produced mist and the enhancement of the subgrid scale interface destruction
mechanisms inside the mist.
Future research of DNS simulations, which includes the investigation of the produced fragments,
can provide a valuable quantitative validation for the present droplet population. Additionally, three-
dimensional simulations, using the proposed multiscale two-ﬂuid approach, could be appropriate
to reveal more details and mechanisms of the mist dynamics and to consider the signiﬁcance of
three-dimensional phenomena, such as turbulence and vortex shedding, in the droplet aerobreakup.
ACKNOWLEDGMENTS
The research leading to these results has received funding from the European Union’s Horizon
2020 Research and Innovation program under the Marie Skłodowska-Curie Grant Agreement No.
675676. The authors gratefully acknowledge the valuable suggestions and help by Dr. Phoevos
Koukouvinis during the development of the numerical methodology and the fruitful discussions
with Professor Detlef Lohse about the physics of droplet breakup.
APPENDIX: V ALIDITY OF CLOSURE MODELS AND NUMERICAL METHOD LIMITA TIONS
Modeling limitations may arise in the developed numerical method due to the introduction of
closure relations for the source terms in the governing equations, the subgrid scale modeling, the
switching criteria within the multiscale framework, and the absence of a quantitative validation for
the produced mist. The validity of the utilized models and the imposed assumptions is discussed
below, considering speciﬁcally the present simulations of droplet aerobreakup and the examined
ﬂow conditions.
(1) The closure of the interfacial interaction terms , which appear in Navier-Stokes equations
after the imposed averaging procedure and consider the mass, momentum, and energy exchange
phenomena between the interacting phases, is an inherent modeling requirement of the two-ﬂuid
model formulation. In the present simulations, the applied closure relations are consistent with the
examined ﬂow conditions, as discussed below.
(i) In continuity equation ( 1), the interfacial mass source term, which models the mass transfer
due to phase-change phenomena, namely, cavitation and vaporization, is neglected.
(a) Cavitation plays a minor role at the early stages of aerobreakup in the examined cases.
Speciﬁcally, as depicted in Fig. 11, in cases 1 and 2 the shock wave propagation evolves smoothly
downstream without any signiﬁcant decrease in the local pressure inside the droplet, which can
be related to the development of cavitation regions. On the contrary, in the supersonic case 3,
084304-20

<!-- PDF_PAGE: 21 -->

DROPLET AEROBREAKUP UNDER THE SHEAR-INDUCED …
FIG. 11. Compressibility effects at the early stages of aerobreakup, namely, the incident shock wave
downstream propagation, the reﬂected shock wave in the free gas stream, and the transmitted shock wave
into the liquid droplet. Pressure ﬁeld (top) and numerical schlieren images (bottom).
the strong shock wave with Mach number 2.64 results in an increase of the local pressure at 35
bars after impact. At 1.5 μs the propagating shock wave inside the droplet is reﬂected normal
to the droplet outer surface and an expansion wave is created. When the shock wave reaches
the back side of the droplet, it partially reﬂects backwards, and a low-pressure region is formed
at 2.5 μs. Similarly, the experimental observations of Sembian et al. [37] depict the creation of
cavitation bubbles and the subsequent decrease of the low-pressure region in the aerobreakup
of a water column under supersonic conditions. Despite the cavitation development, an early
fragmentation, initiating from the back side of the droplet due to cavitation bubbles’ collapse, is
not observed in the simulation results; the experimental visualizations of Theofanous et al. [22]
also conﬁrm the absence of any distinguishable surface oscillations or breakup on the back side
of the droplet that can be related to signiﬁcant cavitation effects.
Since the early stages of the droplet aerobreakup evolution are not driven by cavitation and
the minor cavitation region has no macroscopic effect on the droplet fragmentation under the
examined conditions, a model for nucleation and subsequent growth of the cavitating bubbles
has not been implemented in the numerical framework. Instead, in the supersonic case 3, a very
small volume fraction of air of the order of 10
− 6, which corresponds to a typical nucleation
volume fraction [67], is introduced in the initial droplet volume fraction. Under this assumption,
the small gaseous volumes inside the droplet will expand after the signiﬁcant pressure drop,
producing expansion similar to those that would occur with cavitation; with the subsequent
pressure increase, the gaseous volume gradually collapses, although any condensation and the
pressure overshoot effects due to complete vapor collapse (which is not the case with the gas
content) are not considered.
(b) V aporization modeling is neglected since the local liquid temperature does not increase
more than 10 K during the shock wave impact on the droplet in the examined cases. However,
vaporization effects can be responsible for the extended water dispersion observed at the later
084304-21

<!-- PDF_PAGE: 22 -->

GEORGIA NYKTERI AND MANOLIS GA V AISES
TABLE III. Closure relations for the SGS terms in Eq. ( 5) related to interface surface area production and
destruction.
SGS mechanism τSGS /Sigma1∗
SGS
Turbulence k
ε
αl (1−αl )ρm km
σWe∗
turb
with We∗
turb = 1 at equilibrium
Collision and coalescence 1
/Sigma1
√ 2
3 km
6αl (1−αl )
d∗
/Sigma1
with d∗
/Sigma1= d/Sigma1
1+
WeN
coll
6
1+ Wecoll
6
• Critical We for coalescence: We N
coll = 12
• Relevant We for collision: Wecoll = 4αl (1−αl )ρl km
σ/Sigma1
Secondary breakup f (WeBU ) d/Sigma1
ur
√ρl
ρg
6ρgu2r αl (1−αl )
σWe∗
BU
with WeBU = 6ρgu2r αl (1−αl )
σ/Sigma1 with We∗
BU = 12(1 + 1.077Oh1.6 ) ∼= 12 for Oh ≪ 1
stages of aerobreakup under the supersonic postshock conditions of case 3; thus vaporization
could be considered in future research of aerobreakup imposed by high Mach number shock
waves.
(c) Other mass exchange contributions with an effect on interface formation are considered
in the transport equation for the interface surface area density /Sigma1,E q .(5).
(ii) In momentum equation ( 2), the interfacial momentum source term accounts for the aerody-
namic drag force, which dominates among the other interfacial forces acting between the dispersed
droplets and the free-stream gas ﬂow during the aerobreakup process, due to the severe aerodynamic
conditions imposed by the upstream and downstream pressure differences. The aerodynamic drag
force is deﬁned as F
D = 1
2 CDρgasur|ur|Adroplet . The calculated drag coefﬁcient CD [60] is validated
for a vast range of Reynolds numbers and here it is deﬁned based on the local ﬂow properties. The
reference area of the droplet A
droplet is calculated based on the local interface surface area density
/Sigma1. The velocity ﬁelds are accurately predicted in the performed simulations, since good agreement
between the simulation and experimental results is observed with respect to the overall aerobreakup
evolution and the liquid penetration; thus the relative velocity u
r can be precisely extracted from the
two-ﬂuid model.
(iii) In energy equation ( 3), the interfacial energy source term is modeled via a standard heat
transfer law [ 68] for the calculated temperature ﬁelds of the liquid and gaseous phases. In the
present simulations, the observed temperature differences between the liquid and gaseous phases
on interfacial regions can locally reach the absolute value of 35 K in subsonic case 1, almost 90 K
in transonic case 2, and can even exceed the absolute value of 500 K in the bow shock region
in supersonic case 3. Therefore, the modeling of thermal effects becomes crucial for the accurate
capturing of aerobreakup under high Mach numbers.
(2) A fundamental principle of the multiscale two-ﬂuid approach is the subgrid scale modelingof
unresolved ﬂow structures via the transport equation for the interface surface area density/Sigma1,E q .(5).
The physical mechanisms, which are responsible for the interface production and destruction, and
which fall below the local mesh resolution, are considered in Eq. (5) as the subgrid scale source term
S
SGS. Speciﬁcally, the contributions of turbulent ﬂow stretching and wrinkling, along with the sub-
grid scale droplet interactions, involving droplet collision and coalescence, and secondary breakup
effects, are taken into account with the appropriate closure relations, summarized in Table III.T h e
SGS models are a function of the characteristic timescale τ
SGS and the critical interface surface area
density /Sigma1∗
SGS at an equilibrium state between interface production and destruction. The modeling
assumptions and the validity of the SGS models are discussed below.
(i) The turbulence term utilizes the Kolmogorov timescale. The accurate closure of the critical
Weber number We∗
turb [58], which expresses the balance between the liquid kinetic energy and the
liquid surface energy at equilibrium state, requires a case-dependent calibration using DNS results.
However, considering the signiﬁcant computational cost, a viable compromise is to set the critical
084304-22

<!-- PDF_PAGE: 23 -->

DROPLET AEROBREAKUP UNDER THE SHEAR-INDUCED …
FIG. 12. Demonstration of the upper limit for the secondary droplets’ diameters modeled within the diffuse
mist, using a computational mesh with a resolution of 100 and 200 cells per original diameter. Illustrated in
blue are the secondary droplets inside the mist, captured with both mesh resolutions. Illustrated in red are the
droplets that are modeled inside the mist with the coarse mesh but are resolved by the mesh resolution with the
ﬁne mesh, shown inside the green box. The arrows point to areas where the coarse mesh detects fragments due
to the unresolved interface sharpness.
Weber number value equal to 1, even though it may result in a minor underestimation of the effect
of turbulence on interface formation, as shown in the DNS study of Duret et al. [69]f o rt h ep r i m a r y
atomization of a subsonic spray.
(ii) The collision and coalescence model is based on the particle collision theory [ 58]. The major
assumption concerns the characteristic velocity of collision between the colliding droplets, which
is described as a function of the turbulent kinetic energy and has been used in subsonic liquid spray
atomization simulations [58,70]. Due to the lack of any sufﬁcient information regarding the subgrid
scale particles and since collision is mainly turbulence driven, the proposed model is acceptable in
the present simulations.
(iii) The secondary breakup model is based on the model of Pilch and Erdman [ 10], developed
for Weber numbers up to 10
4. The secondary breakup effects are driven by the mean relative phase
velocity [58], which is available within the two-ﬂuid model formulation; thus the relative velocity
is directly obtained from the numerical model without the need of further modeling assumptions.
(3) The dynamic switching from a sharp to a diffuse interface approach and vice versa, following
the implemented criteria in the ﬂow topology detection algorithm, is bounded by the local mesh
resolution. In other words, the characteristic dimension, that establishes the resolution capabilities
of the multiscale framework and determines which ﬂow structures will be fully resolved and which
will be modeled as subgrid scale phenomena, is an external user-deﬁned parameter. Speciﬁcally,
in the present aerobreakup simulations, the mesh resolution of 100 cells per initial diameter causes
droplets with diameters greater than 19 μm to be resolved with the sharp interface approach, while
the ﬁner mesh of 200 cells per initial diameter allows for more droplets with a minimum diameter
of 9.5 μm to be captured by the local mesh resolution. However, even though the upper limit for
the secondary droplets’ diameters modeled within the diffuse mist is different for the coarse and the
ﬁne mesh, the droplets with diameters in the range of 9.5–19 μm, which are captured by the ﬁne
mesh resolution, are not excluded in the coarse mesh predictions. As shown in Fig. 12, in the region
where the ﬁne mesh detects mesh-resolvable fragments, detached either from the droplet back side
or the droplet equator, the coarse mesh identiﬁes the largest-scaled secondary droplets within the
diffuse mist.
This switching mechanism operates well with moderate mesh resolutions in multiscale ﬂows
like the droplet aerobreakup problem, in which the sizes of the initial coherent droplet and the
084304-23

<!-- PDF_PAGE: 24 -->

GEORGIA NYKTERI AND MANOLIS GA V AISES
FIG. 13. V olume concentration of the dispersed region over the total volume of the water phase for a mesh
resolution of 100 (red solid line) and 200 (blue solid line) cells per initial droplet diameter. The green vertical
lines correspond to a decrease for the width of the deforming droplet by 10%, 25%, and 50%.
ﬁrstly formed fragments have a difference of approximately two orders of magnitude. However, in
ﬂow ﬁelds with structures, covering the complete range between microscales to millimeter sizes,
the switching mechanisms should be improved. Part of the ongoing research is the coupling of
an adaptive mesh reﬁnement algorithm with the sharp interface formulation in order to accurately
capture the intermediate-scaled structures that are part of the sharp interface formulation, and the
original moderate mesh is insufﬁcient to resolve.
Overall, the mesh dependency of the switching criteria does not imply a mesh-dependent
numerical solution in the aerobreakup simulations. A mesh independence investigation is shown in
Fig. 13, comparing the development of the dispersed region over time for the three examined cases
of Table II, using a computational mesh of 100 and 200 cells per initial diameter. For consistency
between the two mesh resolutions, the coarser simulation of 100 cells per diameter includes droplets
up to 9.5 μm, which corresponds to the local mesh resolution and, thus, the upper limit for the
dispersed region resolution with the ﬁner mesh. In cases 1 and 2 very good agreement between the
different mesh resolutions is observed, while in case 3 a small deviation of about 10% is noticeable
at the early stages of aerobreakup. Considering that any small deviation is enhanced by microscale
droplets below 1 μm, it is safe to conclude that the proposed numerical method is independent of
the computational mesh.
(4) A quantitative validation for the mist dynamics and the sizes of the underlying secondary
droplets is restricted by the visualization capabilities inside the dense mist. In the experiments of
Theofanous [ 16] and Theofanous et al. [22], the utilized camera resolution of 5 μm/pixel does
not allow for the quantiﬁcation of smaller droplet sizes, which are illustrated as a dilute cloud of
undeﬁned and shapeless structures. Thus, the extraction of any information regarding the droplet
sizes inside the dense mist is not feasible in the available experimental visualizations. To the
best of the authors’ knowledge, size distributions for the produced fragments after the droplet
aerobreakup are available in the literature to date, but only in experimental studies of moderate
droplet fragmentation cases [ 27–31] in the transition zone between the RTP and SIE regimes. In
these cases, the fragments form as a part of a distinguishable liquid trace behind the deforming
droplet and not as individual small structures inside a dense and hazy cloud; thus the visualization
of the underlying structures is signiﬁcantly more pronounced, and a quantitative analysis of the
produced fragments is achievable with the use of advanced visualization techniques.
[1] D. R. Guildenbecher, C. Lopez-Rivera, and P . E. Sojka, Secondary atomization, Exp. Fluids 46, 371
(2009).
084304-24

<!-- PDF_PAGE: 25 -->

DROPLET AEROBREAKUP UNDER THE SHEAR-INDUCED …
[2] R. D. Reitz and R. Diwakar, Effect of drop breakup on fuel sprays, SAE Transactions V ol. 95, Section 3
(1986), pp. 218–227.
[3] E. Abo-Serie, C. Arcoumanis, and M. Gavaises, Spray characterisation of swirl pressure atomizers for
G-DI engines: Phase Doppler measurements, in Proceedings of ILASS—Europe , (Darmstadt, Germany,
2000), p. 11.
[4] A. E. S. E. T. Alajmi, N. M. Adam, A. A. Hairuddin, and L. C. Abdullah, Fuel atomization in gas turbines:
A review of novel technology, Int. J. Energy Res. 43, 3166 (2019).
[5] M. A. Benjamin, R. J. Jensen, and M. Arienti, Review of atomization: Current knowledge and future
requirements for propulsion combustors, Atomization Sprays 20, 485 (2010) .
[6] R. N. Dahms and J. C. Oefelein, Atomization and dense-ﬂuid breakup regimes in liquid rocket engines,
J. Propul. Power 31, 1221 (2015).
[7] B. E. Gelfand, Droplet breakup phenomena in ﬂows with velocity lag, Prog. Energy Combust. Sci. 22,
201 (1996).
[8] O. Gohardani, Impact of erosion testing aspects on current and future ﬂight conditions, Prog. Aerosp. Sci.
47, 280 (2011) .
[9] J. O. Hinze, Fundamentals of the hydrodynamic mechanism of splitting in dispersion processes, AIChE
J. 1, 289 (1955) .
[10] M. Pilch and C. A. Erdman, Use of breakup time data and velocity history data to predict the maximum
size of stable fragments for acceleration-induced breakup of a liquid drop, Int. J. Multiphase Flow 13, 741
(1987).
[11] G. M. Faeth, L.-P . Hsiang, and P .-K. Wu, Structure and break-up properties of sprays, Int. J. Multiphase
Flow 21, 99 (1995).
[12] D. Stefanitsis, G. Strotos, N. Nikolopoulos, E. Kakaras, and M. Gavaises, Improved droplet breakup
models for spray applications, Int. J. Heat Fluid Flow 76, 274 (2019).
[13] D. Stefanitsis, G. Strotos, N. Nikolopoulos, and M. Gavaises, Numerical investigation of the aerodynamic
breakup of a parallel moving droplet cluster, Int. J. Multiphase Flow 121, 103123 (2019) .
[14] D. Stefanitsis, I. Malgarinos, G. Strotos, N. Nikolopoulos, E. Kakaras, and M. Gavaises, Numerical
investigation of the aerodynamic breakup of droplets in tandem, Int. J. Multiphase Flow 113, 289 (2019).
[15] T. G. Theofanous, G. J. Li, and T. N. Dinh, Aerobreakup in rareﬁed supersonic gas ﬂows, J. Fluids Eng.
126, 516 (2004) .
[16] T. G. Theofanous, Aerobreakup of Newtonian and viscoelastic liquids, Annu. Rev. Fluid Mech. 43, 661
(2011).
[17] O. G. Engel, Fragmentation of waterdrops in the zone behind an air shock, J. Res. Natl. Bur. Stand. U. S.
60, 245 (1958) .
[18] J. A. Nicholls and A. A. Ranger, Aerodynamic shattering of liquid drops, AIAA J. 7, 285 (1969) .
[19] A. Wierzba and K. Takayama, Experimental investigation of the aerodynamic breakup of liquid drops,
AIAA J. 26, 1329 (1988) .
[20] T. Y oshida and K. Takayama, Interaction of liquid droplets with planar shock waves, J. Fluids Eng. Trans.
ASME 112, 481 (1990) .
[21] T. G. Theofanous and J. G. Li, On the physics of aerobreakup, Phys. Fluids 20, 052103 (2008).
[22] T. G. Theofanous, V . V . Mitkin, C. L. Ng, C. H. Chang, X. Deng, and S. Sushchikh, The physics of
aerobreakup. II. Viscous liquids, Phys. Fluids 24, 022104 (2012) .
[23] T. G. Theofanous, V . V . Mitkin, and C. L. Ng, The physics of aerobreakup. III. Viscoelastic liquids, Phys.
Fluids 25, 032101 (2013).
[24] V . V . Mitkin and T. G. Theofanous, The physics of aerobreakup. IV . Strain-thickening liquids,Phys. Fluids
29, 122101 (2017).
[25] Z. Wang, T. Hopfes, M. Giglmaier, and N. A. Adams, Effect of Mach number on droplet aerobreakup in
shear stripping regime, Exp. Fluids 61, 1 (2020).
[26] D. Hébert, J.-L. Rullier, J.-M. Chevalier, I. Bertron, E. Lescoute, F. Virot, and H. El-Rabii, Investigation
of mechanisms leading to water drop breakup at Mach 4.4 and Weber numbers above 105, SN Appl. Sci.
2, 1 (2020) .
084304-25

<!-- PDF_PAGE: 26 -->

GEORGIA NYKTERI AND MANOLIS GA V AISES
[27] L. P . Hsiang and G. M. Faeth, Near-limit drop deformation and secondary breakup, Int. J. Multiphase
Flow 18, 635 (1992).
[28] L. P . Hsiang and G. M. Faeth, Drop properties after secondary breakup, Int. J. Multiphase Flow 19, 721
(1993).
[29] L. P . Hsiang and G. M. Faeth, Droplet deformation due to shock wave and steady disturbances, Int. J.
Multiphase Flow 21, 545 (1995) .
[30] E. Villermaux, Fragmentation, Ann. Rev. Fluid Mech. 39, 419 (2007).
[31] Z. Xu, T. Wang, and Z. Che, Droplet deformation and breakup in shear ﬂow of air, Phys. Fluids 32,
052109 (2020).
[32] H. Chen, Two-dimensional simulation of stripping breakup of a water droplet, AIAA J. 46, 1135 (2008) .
[33] R. Saurel, and R. Abgrall, Simple method for compressible multiﬂuid ﬂows, SIAM J. Sci. Comput. 21,
1115 (1999).
[34] D. Igra and K. Takayama, A study of shock wave loading on a cylindrical water column, Rep. Inst. Fluid
Sci. Tohoku Univ. 13, 19 (2001).
[35] G. Allaire, S. Clerc, and S. Kokh, A ﬁve-equation model for the simulation of interfaces between
compressible Fluids, J. Comput. Phys. 181, 577 (2002) .
[36] J. C. Meng and T. Colonius, Numerical simulations of the early stages of high-speed droplet breakup,
Shock Waves 25, 399 (2015) .
[37] S. Sembian, M. Liverts, N. Tillmark, and N. Apazidis, Plane shock wave interaction with a cylindrical
water column, Phys. Fluids 28, 056102 (2016) .
[38] H. Y ang and J. Peng, Numerical study of the shear-thinning effect on the interaction between a normal
shock wave and a cylindrical liquid column, Phys. Fluids 31, 043101 (2019).
[39] J. W. J. Kaiser, J. M. Winter, S. Adami, and N. A. Adams, Investigation of interface deformation dynamics
during high-Weber number cylindrical droplet breakup, Int. J. Multiphase Flow 132, 103409 (2020).
[40] D. Igra and K. Takayama, Numerical simulation of shock wave interaction with a water column, Shock
Waves 11, 219 (2001) .
[41] D. Igra and K. Takayama, Investigation of aerodynamic breakup of a cylindrical water droplet,
Atomization Sprays 11, 167 (2001) .
[42] J. C. Meng and T. Colonius, Numerical simulation of the aerobreakup of a water droplet, J. Fluid Mech.
835, 1108 (2018) .
[43] N. Liu, Z. Wang, M. Sun, H. Wang, and B. Wang, Numerical simulation of liquid droplet breakup in
supersonic ﬂows, Acta Astronaut. 145, 116 (2018) .
[44] D. Stefanitsis, P . Koukouvinis, N. Nikolopoulos, and M. Gavaises, Numerical investigation of the aerody-
namic droplet breakup at Mach numbers greater than 1, J. Energy Eng. 147, 04020077 (2021) .
[45] J. W. J. Kaiser, D. Appel, F. Fritz, S. Adami, and N. A. Adams, A multiresolution local-timestepping
scheme for particle–laden multiphase ﬂow simulations using a level-set and point-particle approach,
Comput. Methods Appl. Mech. Eng. 384, 113966 (2021).
[46] C. H. Chang, X. Deng, and T. G. Theofanous, Direct numerical simulation of interfacial instabilities: A
consistent, conservative, all-speed, sharp-interface method, J. Comput. Phys. 242, 946 (2013) .
[47] B. Dorschner, L. Biasiori-Poulanges, K. Schmidmayer, H. El-Rabii, and T. Colonius, On the formation
and recurrent shedding of ligaments in droplet aerobreakup, J. Fluid Mech. 904, A20 (2020) .
[48] M. Jalaal and K. Mehravaran, Fragmentation of falling liquid droplets in bag breakup mode, Int. J.
Multiphase Flow 47, 115 (2012) .
[49] M. Jain, R. S. Prakash, G. Tomar, and R. V . Ravikrishna, Secondary breakup of a drop at moderate Weber
numbers, Proc. R. Soc. London, Ser. A 471, 20140930 (2015) .
[50] G. Nykteri, P . Koukouvinis, R. S. Gonzalez Avila, C.-D. Ohl, and M. Gavaises, A /Sigma1-Y two-ﬂuid model
with dynamic local topology detection: Application to high-speed droplet impact, J. Comput. Phys. 408,
109225 (2020).
[51] A. Andreini, C. Bianchini, S. Puggelli, and F. X. Demoulin, Development of a turbulent liquid ﬂux model
for Eulerian-Eulerian multiphase ﬂow simulations, Int. J. Multiphase Flow 81, 88 (2016).
[52] N. Bremond and E. Villermaux, Bursting thin liquid ﬁlms, J. Fluid Mech. 524, 121 (2005) .
084304-26

<!-- PDF_PAGE: 27 -->

DROPLET AEROBREAKUP UNDER THE SHEAR-INDUCED …
[53] X. K. Cao, Z. G. Sun, W. F. Li, H. F. Liu, and Z. H. Y u, A new breakup regime of liquid drops identiﬁed
in a continuous and uniform air jet ﬂow, Phys. Fluids 19, 057103 (2007).
[54] M. Ishii and K. Mishima, Two-ﬂuid model and hydrodynamic constitutive relations, Nucl. Eng. Des. 82,
107 (1984).
[55] A. V allet and R. Borghi, Modelisation eulerienne de l’atomisation d’un jet liquide, C. R. Acad. Sci., Ser.
I I b :M e c . ,P h y s . ,A s t r o n .327, 1015 (1999).
[56] C. W. Hirt and B. D. Nichols, V olume of ﬂuid (VOF) method for the dynamics of free boundaries,
J. Comput. Phys. 39, 201 (1981) .
[57] R. Scardovelli and S. Zaleski, Direct numerical simulation of free-surface and interfacial ﬂow, Annu. Rev.
Fluid Mech. 31, 567 (1999) .
[58] R. Lebas, T. Menard, P . A. Beau, A. Berlemont, and F. X. Demoulin, Numerical simulation of primary
break-up and atomization: DNS and modelling study, Int. J. Multiphase Flow 35, 247 (2009).
[59] J. U. Brackbill, D. B. Kothe, and C. Zemach, A continuum method for modeling surface tension,
J. Comput. Phys. 100, 335 (1992) .
[60] G. I. Kelbaliyev, Drag coefﬁcients of variously shaped solid particles, drops, and bubbles, Theor. Found.
Chem. Eng. 45, 248 (2011) .
[61] S. S. Deshpande, L. Anumolu, and M. F. Trujillo, Evaluating the performance of the two-phase ﬂow solver
INTERFOAM, Comput. Sci. Discovery 5, 014016 (2012).
[62] A. V allet, A. A. Burluka, and R. Borghi, Development of a Eulerian model for the “atomization” of a
liquid jet, Atomization Sprays 11, 619 (2001) .
[63] J. Chesnel, J. Reveillon, T. Menard, and F. X. Demoulin, Large eddy simulation of liquid jet atomization,
Atomization Sprays 21, 711 (2011) .
[64] R. T. Lahey, The simulation of multidimensional multiphase ﬂows, Nucl. Eng. Des. 235, 1043 (2005).
[65] D. Stefanitsis, I. Malgarinos, G. Strotos, N. Nikolopoulos, E. Kakaras, and M. Gavaises, Numerical
investigation of the aerodynamic breakup of diesel and heavy fuel oil droplets, Int. J. Heat Fluid Flow
68, 203 (2017) .
[66] M. J. Ivings, D. M. Causon, and E. F. Toro, On Riemann solvers for compressible liquids, Int. J. Numer.
Methods Fluids 28, 395 (1998) .
[67] S. Karthika, T. K. Radhakrishnan, and P . Kalaichelvi, A review of classical and nonclassical nucleation
theories, Cryst. Growth Des. 16, 6663 (2016) .
[68] W. E. Ranz and W. R. Marshall, Evaporation from drops: Part 1, Chem. Eng. Prog. 48, 141 (1952).
[69] B. Duret, J. Reveillon, T. Menard, and F. X. Demoulin, Improving primary atomization modeling through
DNS of two-phase ﬂows, Int. J. Multiphase Flow 55, 130 (2013).
[70] T. F. Leung, C. P . Groth, and J. Hu, Evaluation of an Eulerian-Lagrangian spray atomization (ELSA)
model for nozzle ﬂow: Modeling of coupling between dense and disperse regions, in Proceedings of 47th
AIAA Thermophysics Conference (AIAA, Reston, V A, 2017), p. 4352.
084304-27
