<!-- PDF_PAGE: 1 -->

Email address for correspondence: meredith.xs@163.com; wbing@tsinghua.edu.cn. 
Investigation on the dynamic characteristics of a droplet 
subjected to a divergent shock wave 
Haotian Chen (陈浩天)1, Xin Jin (靳鑫)1, Wei Wang (王威)2, Sheng Xu (徐胜)1* and Bing Wang (王兵)1* 
1School of Aerospace Engineering, Tsinghua University, Beijing, China 
2Senior Department of Orthopedics, Fourth Medical Center of PLA General Hospital, Beijing, China 
The present study numerically inv estigates the dynamic characte ristics of a cylindrical droplet impinged by a 
divergent shock wave, focusing on deformation morphology, the o nset of Kelvin-Helmholtz  (K-H) instability, and 
g l o b a l  d y n a m i c s .  K e y  f e a t u r e s  o f droplet deformation, including  general flattening, interface instabilities, the 
formation and spanwise elongation of liquid ligaments, are capt ured and analyzed. Comparisons with the planar 
shock case indicate the significant role of shock wave curvature in droplet deformation. Ligaments form closer to the 
front stagnation point and experience further spanwise extension in the divergent shock case. Moreover, the inception 
location of the windward K-H instability is found to almost coi ncide with the windward fixed-point, which forms 
and migrates as a result of the combined effects of external an d internal flow before resting. A theoretical analysis 
reveals that the initial location of the fixed-point coincides with the critical contact point of the transmitted shock. 
This location will move downstream with increasing shock curvature radius. This study is expected to provide new 
insights into shock-droplet interaction problem, contributing t o a better understanding of fuel atomization in 
supersonic propulsion systems. 
Keywords: shock wave, curvature, droplet deformation, interface instability 
 Introduction 
Hypersonic propulsion technology1-4 leads a cutting-edge in modern aerospace science and engineeri ng. Various 
shock waves occur in supersonic combustors where liquid fuels a re generally utilized 5-8. The behavior of these 
atomized fuels, encompassing deformation, fragmentation, atomization, and evaporation under intricate shock waves, 
as well as their mixing character istics with oxidizers, directl y affects the engine performance 9, 10. That is why , in 
recent decades, numerous experime ntal and numerical studies hav e been conducted on shock-droplet interactions. 
Previous studies11-16 summarized the deformation behaviors of liquid droplets with t he low-speed airflow erosions 
by extensive experimental studies . They classified the droplet breakup phenomena into f ive regimes based on the 
Weber number (We): vibrational, bag, bag and stamen, stripping, and catastrophic. However, considerable academic 
controversies regarding the mech anisms governing the droplet de formation behaviors with the high-speed airflow 
erosions still remain. Based on a large number of experiments, Theofanous et al. 17 pointed that shear-induced 
entrainment (SIE) is the predominant mechanism of droplet breakup, casting doubt on the independent existence of 
the catastrophic mode. Subsequently, Theofanous and Li18 employed the laser-induced fluorescence (LIF) technique 
to assert again that SIE become s the dominant mechanism when We exceeds 10 2. Nagy et al. 19 numerically 
highlighted the turbulence effect surpassing the viscosity effe ct in dominating droplet breakup behavior for We 
exceeding 10 3. Klein et al. 20 emphasized the influence of thermodynamic effects, specificall y due to changes in 
upstream pressure and temperature, on droplet deformation phenomena. Boyd et al.21 systematically studied the effect

<!-- PDF_PAGE: 2 -->

of vaporization on droplet aerodynamic breakup at a low Weber number (We = 10.5). It is found that the Stefan flow 
is the dominant reason for the breakup suppression and drag enhancement. 
In the review of Theofanous22, the aerodynamic breakup modes of Newtonian and non-Newtonian droplets under 
shock wave conditions were systematically summarized and reclas sified into two regimes. At a low We, the droplet 
deformation is dominated by the Rayleigh-Taylor (R-T) instability; thus, the aerobreakup of the droplet is defined as 
the Rayleigh-Taylor piercing (RTP) mode. At a high We, as the strong shear erosion from the high-speed airflow and 
Kelvin-Helmholtz (K-H) instability on the droplet surface, the peeling off of liquid mist occurs at the equatorial edge 
of the droplet corresponding to the SIE mode. Dorschner et al. 23 elucidated the ligament formation process of the 
shocked droplet and the effect of surface tension. They found the ligament formation and shedding to be a recurrent 
process. The first ligament shedding weakly depends on We, while subsequent shedding processes seem to be driven 
primarily by inertia and the vortex shedding in the wake of the  deformed droplet. Sharma et al. 24 e x t e n s i v e l y  
investigated shock-interaction phenomena for a planar shock across a wide range of We and Reynolds numbers (Re), 
detailing interaction characteristics through wave dynamics and droplet breakup behaviors. Their study established a 
transition criterion between SIE and RTP modes, which successfu lly explains the observation of the RTP mode of 
droplet breakup at We ∼ 800. Then the shock-induced atomization of a liquid metal droplet was also investigated by 
them25. Chandra et al.26 conducted experiments on polymeric droplet under planar shock impingements, discerning 
three stages in aerobreakup: droplet deformation, appearance an d growth of interface instability, and evolution of 
liquid mass morphology. They found that viscoelasticity plays a minor role in the first two stages but dominates the 
third stage of the droplet br eakup behavior. Subsequently, Guo et al. 27 specifically investigated the deformation 
mechanisms of wall-attached droplets impinged by planar shocks,  focusing on investigating the effects of different 
wettabilities: hydrophobic, hemispherical, and hydrophilic. It was found that the wall inhibits the deformation and 
fragmentation of droplets in the flow direction. Furthermore, Yi28 studied droplet deformation mechanisms by 
decoupling the outer gas flow and the in-drop liquid flow, theo retically deriving expressions for radial acceleration 
under "shear induced mass accumulation" and "normal pressure induced radial flowing" mechanisms, corroborating 
that the uneven distribution of surface pressure is a major fac tor in generating circumferential protrusions, such as 
liquid bulges and lips. 
Besides numerous experiments, numerical simulation has also eme rged as another significant technique for 
investigating interactions between shock waves and droplets, ac hieving considerable advancements in recent years. 
Meng and Colonius29 and Meng and Colonius30 pioneered the use of high-fidelity simulations, both two-dimensional 
and three-dimensional, to study the dynamic behavior of shocked droplets under varying shock intensities and droplet 
diameters, neglecting viscosity and surface tension effects. Th eir works revealed the f ormation of two counter-
rotating vortices near the droplet equator, resulting in a "pan cake" shape and inducing oscillations in droplet 
acceleration and drag coefficients. Subsequently, Xiang and Wang 31 employed an improved WENO scheme 32 t o  
numerically simulate the deformation of shocked water droplets with/without air cavity, analyzing the influence of 
shock intensity and embedded cavity size on droplet deformation  behavior. Guan et al. 33 combined numerical 
simulations with theoretical analysis to study the establishmen t of internal flow fields within shocked droplets, 
observing the saddle point and re vealing the correlation betwee n its steady position and the incident shock wave 
intensity. Liu et al.34 investigated interactions between supersonic airflows and drop lets at different Mach numbers,

<!-- PDF_PAGE: 3 -->

identifying shear-induced instabilities on the droplet windward  side and vortex-induced instabilities on the leeward 
side. Moreover, considering the extreme thermodynamic environme nt inside the supersonic engines, Boyd and 
Jarrahbashi35 investigated the dynamic behavior of sub-, trans-, and super-c ritical shocked droplets, and analyzed 
how droplet temperature influences the dynamic behavior of the shocked droplet. Also, several researchers 36-39 
numerically studied the deformation behavior of high-temperatur e aluminum droplets under planar shock waves, 
accounting for evaporation and combustion effects. The numerical simulations clearly captured the evaporation and 
combustion phenomena of shocked aluminum droplets, elucidating the mechanisms by which combustion promotes 
the evaporation behavior of the droplets. Zhu et al.40 numerically discussed the phys ical mechanisms for variations 
of multiple recirculation zones and the development of K-H instability in wave formation. Particularly, they detailed 
sub-droplet size distributions in the droplet deformation and breakup stage. Dworzanczyk et al.41 studied the droplet 
aerobreakup in the stagnation region of high-Mach-number flow o ver a bluff body with experiments and 
computations. They found that the acceleration term dominates the shear term at the stagnation point and accentuated 
as the droplet flattens, while the characteristic inverts close to the droplet equator. 
Over the last few decades, signif icant progress has been made i n understanding the defor mation and breakup of 
droplets under planar shock or high-speed airflow. However, pre vious researchers mainly focus on shock-droplet 
interaction problem under the conditions of ideal planar shock waves or unidirectional incoming airflows, but paid 
little attention on the effects of  shock wave curvature. Actual ly, in real supersonic combustors where high-speed 
airflows and intense chemical reactions are highly coupled, the geometric structures of shock waves are considerably 
complex42-45 and almost no ideal planar shock wave exists. Compared with pl anar shock waves, the flow 
nonuniformity behind curved shock waves may introduce additiona l influence on the deformation and breakup 
behaviors of droplets, particularly when the shock curvature is  comparable to the droplet size. Nevertheless, the 
underlying physical mechanisms of curved shock-droplet interaction have not yet been fully understood. 
The present study aims to use high-resolution, high-fidelity nu merical simulations to investigate curved shock-
droplet interaction problem, with the shock curvature on the or der of the droplet size. We hope the research can 
provide insights for optimizing injectors and atomizers in supe rsonic engines to improve thermal efficiency. This 
paper is organized as follows. In §2, the physical model of curved shock-droplet interaction is described. Subsequently, 
the governing equations and numerical treatment are presented in §3, and the grid sensitivity analysis, experimental 
comparisons and verification of the simplified model are also c arried out. In § 4, the results of droplet’s dynamic 
characteristics, including the dr oplet deformation morphologies , the generation of K-H instability and the droplet 
global dynamics, are discussed. H ere, we mainly investigate the  influence of the shock wave’s curvature by 
comparison. Finally, the conclusions are presented in §5. 
 Physical model 
A schematic drawing of the interaction between a cylindrical di vergent shock wave and a cylindrical droplet is 
illustrated in Figure 1. Here, we use RD to represent the radius of the cylindrical droplet. R0 and Ma0 represent the 
curvature radius and shock intensity of the cylindrical diverge nt shock, respectively, at the time it just touches the 
droplet windward surface. The dimensionless radius ω = R0/RD is adopted to normalize the curvature effect of the 
divergent shock. Referring to previous works31, 46, 47, the droplet diameter is taken as 4.8 mm. The droplet and the un-
shocked gas are initially in equilibrium with 300 K temperature and 101,325 Pa pressure.

<!-- PDF_PAGE: 4 -->

Figure 1. The schematic drawing of the interaction between a cy lindrical divergent shock, with R0 radius and Ma0 intensity, and a 
cylindrical droplet with RD radius. 
In the present study, inspired by Zhai et al. 48, a cylindrical divergent shock is generated from a planar shoc k 
transformation within a specially designed shock tube, and the detailed strategy for that expanding-shock tube contour 
design is provided in Appendix A. The key theory underlying the transformation from a planar shock to a curved one 
in the field of shock dynamics is the CCW relation49-53. It describes how the shock intensity Ma varies with the cross-
sectional area A, 
 

2
21 dd ,(1 )
Ma Ma AMa K Ma A   (1.1) 
where, 
  

11 2
22
1212 122 1 1 ,   . 12 1
MaKM a Ma Ma
    

           
 (1.2) 
 Numerical methodology 
3.1. Governing equations 
The interaction between the divergent shock and the droplet is a strong compressible two-phase hydrodynamic 
problem, involving complex factors such as a large density rati o and strong shock waves. In the present study, all 
numerical simulations are carried out by our in-house software (SCP-tran©), which has been previously applied to 
study a variety of compressible multiphase flow problems, inclu ding high-speed droplet impacting on walls54, 55 and 
shock-droplet interactions 31, 46. The classical compressible two-phase flow model 30, 56, 57  is employed to solve the 
aforementioned hydrodynamic problem, and the governing equations consist of two mass conservation equations for 
gas and liquid phases, a mixture momentum conservation equation , a mixture energy conservation equation and a 
volume fraction advection equation of liquid phase.

<!-- PDF_PAGE: 5 -->

 
 

0,
0,
() 0,
()
0,
0,
lljll
j
gg ggj
j
ij i ji
j
j
j
ll
j
j
u
tx
u
tx
uu pu
tx
Ep uE
tx
utx

 


 


 
 
 
 (2.1) 
where, αl (αg) and ρl (ρg) are the volume fraction and density of liquid and gas phases, respectively. uj is the velocity 
in jth direction. ρ, p, T and E = ρujuj/2 + ρe are the density, pressure, temperature and total energy of the mixture, 
respectively. e represents the mixture specific internal energy. 
 
,,
,  .kk kk k
kl g kl g
ee    

  (2.2) 
The stiffened gas equation of state 57 is employed for the governing equation Eq. (2.1) closure, which is able to 
consistently describe the thermodynamic states of both gas and liquid phases. 
 

,
  , .1
k
k
kk
kppek l g 

  ，  (2.3) 
Here, γk and p∞,k are parameters empirically fitted from experimental data, and the speed of sound is calculated as, 
  ,
,  , .
kk
k
k
pp
ck l g



  (2.4) 
For air, p∞ = 0 Pa and the stiffened gas equation of state reduces to the ideal gas equation of state with γ = 1.4 as the 
specific heat ratio. For water, γ = 6.12 and p∞ = 0.343×109 Pa are chosen, referring to previous works46. 
3.2. Numerical treatments 
The key-solver of SCP-tran © uses a finite volume method 58 to discretize the above governing equations in a 
uniform Cartesian grid system. The second-order MUSCL59 and the fifth-order WENO-IS32 is hybridized and applied 
to the spatial reconstruction. The HLLC approximate Riemann sol ver60 is employed to calculate numerical fluxes. 
The third-order total variation diminishing (TVD) Runge-Kutta m ethod61 is adopted in time integration. The same 
Courant–Friedrichs–Lewy (CFL) number, 0.4, is used in present s imulations. Since the two-phase interface is 
captured through a diffuse-interface-method in present simulati ons, the numerical dissipation effect draws an 
excessive non-physical diffusion of the two-phase interface. Th erefore, the THINC interface sharpen method 62 is 
employed in two-phase interface reconstructions. Considering that the curved wall profile, as illustrated in Figure 1, 
does not coincide with the grid-face, a ghost-cell immersed bou ndary method63, 64 for distinguishing geometrically 
complex boundaries is employed in the calculation. The inlet and outlet boundary types of the curved shock tube are 
chosen to be non-reflecting boundaries65, 66.

<!-- PDF_PAGE: 6 -->

3.3. Numerical verification and validation 
Since the uniform Cartesian grid system is employed to capture the curved droplet interface, which cannot be 
accurately described when the curve-fitted grid is unconsidered , numerical verification of the grid sensitivity is 
essential for the follow-up analysis. For the sake of simplicity, the planar shock-droplet interaction is simulated here 
under the Ma0 = 2.4 shock with three grid resolutions, corresponding to 400, 600 and 800 grids per droplet diameter, 
respectively. Note that, in this work, the non-dimensional time t* is employed for universal investigations on droplet 
deformation and kinematic characteristics, and it can be expressed as, 
  0
,
2
g
Dl g
ttut
R 
   (2.5) 
where, ug and ρg are the flow speed and density of the air in the post-shock state, respectively. ρl is the droplet density. 
t0 is the zero-instant defined as the moment the incident shock just touches the droplet windward surface. 
 
Figure 2. Comparison of deformed water droplet interfaces, defined by αl = 0.5, for three gird resolutions of 400, 600 and 800 grids per 
D0 under a Ma0 = 2.4 planar shock wave impingement. 
Figure 2 presents the comparison of the shocked water droplet deformati on under different gird resolutions. It is 
clear that as the grid resolution increases, more details like the surface instabilities, liquid sheets and thin filaments 
are resolved. The overall qualitative features of the droplet d eformation behavior, like flattening and stripping, are 
very similar. The main profiles of the droplet under three grid  resolutions are almost consistent, even though there 
are slight differences in the morphology of liquid filaments near the equator of the shocked droplet. Further, from the 
comparison of the deformed droplet morphologies above, it can b e found that an approximate grid convergence is 
realized between grid resolutions of 600 and 800 grids per droplet diameter, and the former has an enough capability 
to capture the early deformation characteristics of the shocked  droplet. Certainly, employing a finer grid can yield 
more detailed flow structures, such as surface wrinkles induced  by K-H instabilities, though it incurs more 
computational costs. Therefore, for a better numerical resoluti on in capturing flow structures, in the present work, 
subsequent simulations are conducted with 800 grids per droplet diameter. 
Moreover, as illustrated in Figure 3 ,  w e  c o m p a r e  t h e  p r e s e n t  s i m u l a t e d  d r o p l e t  d e f o r m a t i o n  w i t h  p r evious 
experimental67 and numerical30, 68 visualizations. Given the uncertainty of the numerical diffusion of the large density

<!-- PDF_PAGE: 7 -->

ratio interface discontinuity, the exact interface location is hard to be identified. Hence, the present study adopts the 
αl = 0.5 isoline to represent the deformed droplet surface and co mpares it with experimental images. Despite a 
mismatch in a dearth of timing with Theofanous et al.67, it is found that the present simulations are, by and large, i n 
agreement with the experimental results, and better than the other two simulations. Some key features of the shocked 
droplet deformation behavior, especially the flattening phenomenon at the droplet leeward surface, are well captured, 
which sufficiently validates the credibility of present numerical simulations. 
 
Figure 3. Comparison of present simulations, previous simulatio ns and the experimental visualiz ations of water droplet interfa ce 
evolution under a Ma0 = 1.47 planar shock wave impingement. (a) The experimental results from Theofanous et al.67, reproduced from 
T. G. Theofanous, V . V . Mitkin, C. L. Ng, C. H. Chang, X. Deng, and S. Sushchikh, "The physics of aerobreakup. II. Viscous liq uids," 
Phys. Fluids 24, 022104 (2012), with the permission of AIP Publishing. The thr ee-dimensional simulation results from Meng and 
Colonius30: isosurface of αl (b) and isopleths of αl (c), reproduced with permission from J. Fluid Mech. 835, 1108 (2018). Copyright 
2018 Cambridge University Press. ( d) The two-dimensional simulation results from Song et al.68. J. Song, T. Long, and S. Pan, arXiv, 
2306.11255, 2023; licensed under a Creative Commons Attribution (CC BY) license. (e) The present two-dimensional simulation results. 
In this two-dimensional simulation, the droplet is physically a cylindrical water column, impacted by a cylindrical 
curved shock wave, which is different from the real three-dimensional configuration. Here, we justify the rationality 
of the two-dimensional calculation as follows. The comparison i n Figure 3 shows that the present two-dimensional 
deformation patterns (e) are in good agreement with the experimental three-dimensional  results (a), in terms of the 
general shapes, the windward K-H instabilities and the leeward wrinkles. The subsequent deformation behaviors in 
the present two-dimensional, such as the formation and extensio n of liquid ligaments near the droplet equator, the 
flattening of the droplet leeward side, can also be observed in three-dimensional experiments18, 24, 67 and simulations30. 
These results indicate that, although quantitative differences are indeed inevitable, the present two-dimensional 
simulation is still capable of qualitatively exhibit the physical phenomena of shock-droplet interaction problem. Also, 
the present study aims to elabor ate the shock curvature effects  on droplet deformation by comparing droplets 
impinged by planar and divergent shock waves, where all cases a re limited within two-dimensional configuration. 
The corresponding conclusions are still qualitatively valuable and can be naturally extended to understand the three-
dimensional curvature effects. On the other hand, we have to re cognize the fundamental distinctions between three-
dimensional and two-dimensional cases. Certain dimensionality e ffects, such as the three-dimensional relieving 
effect69-72, azimuthal instabilities and symmetry breaking30, cannot be demonstrated by two-dimensional simulations. 
Also, the physical meanings of curvature effects are more complicated in three-dimensional scenarios. A curved shock

<!-- PDF_PAGE: 8 -->

wave should be described as a spatial curved surface, whose curvature is defined by its first and second fundamental 
forms73 instead of a single scalar quantity. These three-dimensional factors can be investigated in future works. 
It should also be noted that, in the current simulations, the c apillary and viscous effects are neglected, which is 
primarily motivated by two factors: the high Mach number and th e coarse grid resolution. Firstly, in the present 
simulations, the post-shock flow for Ma0 = 1.47 has a velocity of 225.83 m/s, corresponding to We = 7334 and Re = 
130626. These two dimensionless numbers will be larger when the shock intensity is further increased. This suggests 
that the early-stage deformation behaviors of the shocked dropl et, including the early interface instabilities, are 
mainly driven by inertia forces over capillary and viscous forces. Therefore, the effects of capillary and viscous forces 
can be reasonably neglected. To verify the rationality of this simplified approximation, Song and Pan74 have compared 
the numerical images of the Ma0 = 3.0 shock-droplet interaction with and without effects of su rface tension and 
viscosity, as shown in Figure 4. The comparison evidently shows that, at such high Mach number s, the influence of 
surface tension and viscosity on the droplet deformation behavi ors is minimal, observable  solely within the fully 
developed region of the wake vortices. That standpoint has also  been validated by Das and Udaykumar 38, who 
intentionally simulated the Ma0 = 1.47 shock-droplet interaction at a low Weber number (We = 10) by fabricating the 
surface tension coefficient. Moreover, in terms of interface instabilities, Dworzanczyk et al.41 analyzed the physical 
mechanisms of the instability growth rate in the shock-droplet interaction problem with Ma0 ranging from 3.03 to 
5.12, through viscous potential flow theory on K-H instability75. Their calculation results indicate that the influences 
of surface tension and viscous forces on the growth rate of dro plet interface instabilities can be neglected compared 
with that of shear forces and su rface acceleration. All of these evidences confirm that the conclusions drawn by the 
present study are still valid even if the capillary and viscous forces are excluded from calculation. Besides the above 
explanation, the insufficient grid resolution is another reason why the present study neglects the viscous and capillary 
effects. Generally, a spatial re solution of at least 4000 grids  per diameter 76 is required to sufficiently resolve the 
viscous boundary layer. As for accurately precising the capilla ry force, it requires a much finer grid resolution with 
an additional body-fitted structured conformal grid strategy. Obviously, realizing the above spatial resolutions is not 
feasible for present simulations. 
 
Figure 4. Effects of capillary and viscous forces on numerical schlieren images of Ma0 = 3.0 shock-droplet simulations. The red line in 
schlieren images represents the αl isoline of the deformed water droplet. These two simulations a re conducted by Song and Pan 74. 
Reproduced with permission from Chin. J. Theor. Appl. Mech. 54, 2419 (2022). Copyright 2022 Editorial Office of Chinese Journ al of 
Theoretical and Applied Mechanics.

<!-- PDF_PAGE: 9 -->

Results and discussions 
In the present study, the interaction details between a diverge nt shock and a cylindrical droplet are investigated, 
including wave configurations evolution, droplet deformation and kinematics characteristics. Shock intensity Ma0 is 
chosen to 2.4, and the dimensionless radius is set to ω = 6.0. 
4.1. Shock-droplet interaction dynamics 
Figure 5  illustrates the numerical pressure evolutions inside/outside t he shocked water droplet with above 
numerical settings. After the incident divergent shock (IS) imp inges the droplet windward surface, it is reflected, 
forming the reflected shock (RS). Generally, depending on the acoustic impedance (Z = ρc) of the medium on either 
side of the interface, the reflected wave can be a shock wave or an expansion wave. For the current case, the acoustic 
impedance of liquid phase is much larger than that of air. Hence, the reflected wave is still a shock wave. Within the 
initial stage of the interaction, the reflection type of the IS  on the droplet windward surface is regular. However, as 
the impingement progresses, the r eflection type evolves into an  irregular Mach reflection form, forming the Mach 
stem (MS). Once IS propagates over the droplet equator point, it diffracts on the leeward side of the droplet, causing 
a gradual decrease in shock intensity. The Mach wave is formed symmetrically around the droplet surface and focuses 
at a point near the rear stagnation point. Furthermore, in the present work, since the shock-droplet interacts within a 
confined shock tube, RS is reflected by the wall, forming a wal l-reflected shock (RS w) with an irregular Mach 
reflection. Simultaneously, due to the impingement of IS, a cur ved transmitted shock (TS) is generated inside the 
droplet. As TS propagates inside the droplet, it is gradually r eflected by the curved internal surface of the droplet, 
producing a first reflected wave. Due to the significant acoust ic impedance mismatch between the gas and liquid 
phases, the first reflected wave is an expansion wave (REW). As the stretching effect of REW, the liquid experiences 
a pronounced negative pressure effect, which is significantly amplified when REW is completely focused. Similarly, 
REW is also reflected by the droplet internal surface, forming the second reflected wave. Different from REW, the 
second reflected wave branches into two distinctly different ty pes: the second reflected compression wave (RCW 2) 
and the second reflected rarefaction wave (RRW2). This special phenomenon was experimentally found by Sembian 
et al.77 and has been detailly discussed in our previous work 46 and will not be elaborated further here. Additionally, 
the reflection of the transmitted shock from the windward and leeward side of the droplet continues with some energy 
loss after every collision until it completely decays. 
The initial stage of wave dynamics, corresponding to the format ion of different wave structures and the changes 
of pressure distribution, is short-lived (approximately t* ≤ 0.10). The droplet remains its coherent circular shape 
during this stage. After this initial stage, the pressure distr ibution outside the droplet and the streamline distribution 
both inside and outside the droplet become basically steady. Th e droplet thus deforms under the effects of the flow 
field established by this initial short stage, as presented by Figure 5 (g-i). The following sections will provide a 
detailed discussion on the flow field characteristics, the corr esponding macroscopic deformation behaviors of the 
shocked droplet and the underlying physical mechanisms. It shou ld be noted that, although wave propagation and 
reflections inside the droplet still exist after t* ~ 0.10, as presented by Figure 5 (g-i), they have neglectable effects on 
the internal and external streamline distributions. The pressur e distribution outside the droplet will not be changed 
significantly either. Consequen tly, these reflected waves can b e thought to have almost no effects on the general 
characteristics of droplet deformation.

<!-- PDF_PAGE: 10 -->

Figure 5. Numerical pressure contours at different time intervals for the interaction between the divergent shock and the water droplet in 
the case of ω = 6.0 and Ma0 = 2.4. Note that the black line in contours represents the αl = 0.5 isoline of the deformed water droplet. 
Characteristic times are (a) 0.0060, (b) 0.0150, (c) 0.0239, (d) 0.0358, (e) 0.0535, (f) 0.0711, (g) 0.1321, (h) 0.1895, (i) 0.2922. 
4.2. Deformed droplet morphologies 
The morphologies of the deformed droplet in the post-shock airf low are investigated in this section. Previous 
studies on droplet deformation behavior24, 27, 30, 40, 78, 79 have mostly focused on uniform supersonic airflow or planar 
shock waves. For a more intuitive demonstration of the influenc e of the shock wave curvature on the droplet 
deformation characteristics, here we first analyze the deformation morphology of the droplet impinged by a divergent 
shock wave (Ma0 = 2.4, ω = 6.0) and then compare it with that of the droplet impinged by a planar shock wave (Ma0 
= 2.4, ω = ∞). 
Figure 6 presents the early-stage deformation (t* ≤ 0.40) of the droplet shocked by the divergent shock wave, an d 
the significant characteristics, such as the generation of surface wrinkles and the overall flattening of the droplet, can 
be clearly observed. Before the analysis of these characteristics, it is necessary to first elucidate the flow field features 
of the droplet’s interior and exterior. After the shock-droplet  interaction discussed above, the flow field outside the 
windward surface is basically steady, where the incident airflow deflects along the droplet surface with a small portion 
of streamlines penetrating the windward surface. Flow separatio n  o c c u r s  n e a r  t h e  d r o p l e t ’ s  e q u a t o r  a n d  t h u s  a  
recirculation zone forms outside the leeward surface with two l arge axisymmetric vortices. On the other hand, after 
the propagation and several reflections of the transmitted shoc k wave inside the droplet, the internal streamline 
distribution is also completely established, where the streamli nes are directed from the windward surface to the 
equator and leeward surface on the whole, as illustrated in Figure 6 (e).

<!-- PDF_PAGE: 11 -->

Figure 6. Early-stage deformation (t* ≤ 0.40) of the droplet shocked by divergent shock (Ma0 = 2.4, ω = 6.0). 
Under the influence of the flow field discussed above, the liquid is directed towards the droplet’s equator, resulting 
in the deformation of the coherent droplet into a flattened "cu pcake" shape. The flow structures within the 
recirculation zone, including the two axisymmetric vortices and the inverse flow near the droplet’s horizontal axis as 
mentioned above, prompts the emer gence of the pit at the rear s tagnation point and enhances the flattening 
deformation of the droplet. Also, perturbation waves of the K-H  instability, which is caused by the large tangential 
velocity difference between the internal and external sides of droplet surface, appear midway between the droplet’s 
front stagnation point and the equator at t* ~  0. 15 .  U po n e m e r ge nc e ,  t he  K - H  w a ve s  gr ow  i n  a m pl i t u de  a n d  get 
deflected towards the streamwise due to the entrainment effect of the post-shock flow. That shear-induced entrainment 
results in the K-H waves moving downstream along the droplet wi ndward periphery. Subsequently, the local liquid 
carried out by these amplified K-H waves gets accumulated as liquid ligaments, as presented in Figure 6 (t* ~ 0.35). 
It is also worth noting that, besides the accumulation effect c aused by the K-H waves, the internal liquid transport 
towards the droplet equator also contributes to the formation a nd growth of ligaments, a mechanism presented by 
streamlines in Figure 6 (e). 
As the dimensionless time advances ( t* ≥ 0.50), the deformation process enters a stage characterized by the 
spanwise elongation of the droplet and its aerobreakup into separated mist, as illustrated in Figure 7. The magnitudes 
of the internal streamwise velocities experience continuous inc rease due to corresponding pressure gradients, thus 
strengthening the internal flows to balance the recirculation flows. Consequently, the leeward wrinkles, including the 
obvious pit at the rear stagnation point, are smoothened gradua lly as the dimensionless time approaching 1.00 and 
finally disappear. During the same stage, the droplet is continuously stretched along the spanwise direction due to the

<!-- PDF_PAGE: 12 -->

spanwise components of internal velocities, characterized by the elongation of the liquid ligaments near the droplet’s 
equator. With the decrease in its thickness, the ligament tip i s incapable of withstanding the airflow impingement, 
thus deflecting and subsequently breaking apart into separated mist, as presented in Figure 7 (g). On the other hand, 
R-T instability emerges and gradually develops on the windward surface, due to the huge acceleration directed from 
low-density air to high-density liquid near the stagnation poin t. Under the action of local shear flows, these R-T  
perturbation waves are entrained downstream along the droplet s urface, with their tips continuously detaching from 
the main droplet. The mechanisms above govern the aerobreakup p rocess of the droplet shocked by incident shock 
wave. According to the previous works18, 31, this aerobreakup mode of the droplet impinged by the divergen t shock 
wave (Ma0 = 2.4, ω = 6.0) is shear-induced entrainment mode. 
 
Figure 7. Late-stage deformation and aerobreakup (0.50 ≤ t* ≤ 1.00) of the droplet shocked by a divergent shock (Ma0 = 2.4, ω = 6.0).

<!-- PDF_PAGE: 13 -->

Figure 8. A comparison of the deformation and aerobreaup behaviors of the droplets shocked by a divergent shock wave and (Ma0 = 2.4, 
ω = 6.0) and a planar shock wave (Ma0 = 2.4, ω = ∞). 
N e x t ,  w e  w i l l  a n a l y z e  t h e  d i f f e r ences of deformation and aerobr eakup behaviors of the droplets under the 
impingement of the divergent shock wave and the planar shock wave. A comparison of the deformation morphologies 
under the two conditions are presented in Figure 8. The two droplets share a similar deformation process with several 
common characteristics, such as the flattening of the droplet, the growth of K-H and R-T instability, the formation of 
liquid ligaments near the equator and the shear-induced entrainment mode of aerobreakup. However, they also have 
significant differences. In the planar shock case, these K-H wa ves can quickly amplify and develop into noticeable 
liquid ligaments, which in turn create a prominent aerodynamic concavity nearby. In contrast, in the divergent shock 
case, the K-H waves on droplet windward side are short-lived and the aerodynamic concavity thus disappears rapidly, 
as illustrated in Figure 8 (t* ~ 0.40). Additionally, the ligaments in the divergent shock ca se appear closer to the 
droplet’s front stagnation point and undergo a stronger stretch ing effect along the spanwise direction, which results 
in a further spanwise extension from the droplet’s center without significant deflection or aerobreakup until t* ~ 0.80. 
Whereas, the elongation of the ligaments in the planar shock case stagnates at t* ~ 0.50 and then they rapidly undergo 
obvious streamwise deflection and stripping. This distinction i s due to the fact that compared with the planar shock 
wave of the same intensity, the divergent shock wave establishe s a flow field with larger magnitudes of spanwise

<!-- PDF_PAGE: 14 -->

velocities and smaller magnitudes of streamwise velocities. Als o, the curvature effect of the divergent shock wave 
weakens the normal impingements but strengthens the shear effects on the droplet, as will be analyzed in next section. 
Furthermore, the deformation on the leeward surface is also dif ferent under the two conditions. It is pronounced 
that under the planar shock case, the leeward surface of the sh ocked droplet experiences a continuous flattening, 
eventually taking on an almost planar shape. Conversely, under the divergent shock case, the flattening of the droplet 
occurs rapidly in the early-stage  deformation but then stagnate s, resulting in the leeward side of the droplet 
maintaining a "cupcake" shape. Notably, compared with the early "cupcake" shape, the leeward surface of the shocked 
droplet in the late-stage deformation resembles a "shallow, wid e-mouthed porcelain dish" shape. However, in both 
cases, the leeward surface of the droplet exhibits nearly perfect smoothness, since the recirculation flow is incapable 
of generating enough aero-erosions during the droplet’s late-stage deformation. 
4.3. Analysis of the starting point of K-H instability 
In this section, we mainly analyze the generation of K-H instab ility on the droplet windward surface. Figure 9 
shows the early-stage deformation of the droplet as well as the  internal and surrounding flow field under the 
impingement of the divergent shock wave. The surface wrinkle on the windward side, induced by K-H instability of 
gas-liquid interface, is also observable at the same time. The starting point of K-H instability is almost consistent 
with the fixed-point on the windward surface (that is, the inte rsection point of the present droplet surface and initial 
droplet surface). From the perspe ctive of flow field, there is only tangential flow on both sides of interface at this 
point, with a nearly zero velocity of normal movement. The drop let surface upstream of the  fixed-point is moving 
inward while the surface downstream of the fixed-point is moving outward. 
 
Figure 9. The deformed droplet surface as well as the distributions of streamlines and pressure at t* = 0.16225 under the impingement of 
Ma0 = 2.4 and ω = 6.0 divergent shock wave. The black solid line denotes the droplet surface at the moment; The black dotted line is the 
initial droplet surface.

<!-- PDF_PAGE: 15 -->

To understand the formation of the fixed-point and the correspo nding generation of K-H instability, we need to 
gain a deep insight into the establishment of the flow field and its influence on the motion of droplet surface. Firstly,  
the inward movement of the droplet surface is mainly caused by the impingement of shock wave outside. During the 
early-stage interaction of the divergent shock wave with the dr oplet, as illustrated in Figure 10, the contact point is 
denoted as Pθ and the angle θ represents the angle between the line P C  and the horizontal axis of the droplet. The 
radius of the divergent shock wave is denoted as  Rθ . The angle between the tangent line of the droplet surface and  
that of the shock wave surface at the point Pθ is denoted as χθ , 
 
Figure 10. A schematic diagram of the divergent shock wave interacting with a cylindrical droplet. 
 21 ( 1) 2( 1)cos ,DRR       (4.1) 
 
2
1 .
1(
s
1) 2( 1)c
() s i nn
os
i 




 
  
 (4.2) 
Here, we define the contact point as the diffraction point Pθdp and the corresponding angle θ as the diffraction angle 
θdp when χθ = 90°, which can be calculated by θdp = arccos[1/(ω+1)]. At the diffraction point, the shock wave changes 
from impinging the droplet surface inwards to a state of diffraction. Therefore, the diffraction point can be considered 
as the effective equator of the droplet, relative to the geometric equator (θ = 90°). At the contact point Pθ within the 
range 0 ≤ θ ≤ θdp , the post-shock velocity VS can be decomposed into a tangential component Vτ , which quantifies 
the intensity of the shear effect of external high-speed flow on the droplet surface, and a normal component Vn , which 
represents the intensity of the normal impingement exerted on the droplet surface. To determine these two components, 
we formulate the shock intensity Maθ at the contact point Pθ as, 
 
00
2
2d d .
1( )
Ma R
Ma R
Ma Ma R
RMa K Ma


  (4.3) 
Integrating the Eq. (4.3) by numerical iteration, the  value of shock intensity Maθ can be obtained. Then, the two 
components of the post-shock velocity at the contact point can be calculated as, 
 
2
,1,
1( 1
() s i n()
)2 ( 1 ) c o s
Vu

 

  
  (4.4)

<!-- PDF_PAGE: 16 -->

21
() c o s() , 11,
1( ) 2 ( 1 ) c o s
nVu 

 



 
 (4.5) 
where uθ denotes the magnitude of post-shock velocity and can be expressed as a function of the shock intensity Maθ . 
 
021 .1g
cuM a Ma


  
 (4.6) 
Here, c0 is the speed of sound ahead of the shock front and γg is the specific heat ratio of air. 
Figure 11 presents the theoretical distribution of the two components of  post-shock velocity at the contact point 
Pθ , under the planar and divergent shock conditions. This distribution indicates that on the droplet windward surface, 
the position closer to the front stagnation point experiences w eaker shear effect but stronger normal impingement, 
while the position closer to the effective equator is subjected to stronger shear effect but weaker normal impingement. 
Additionally, it is obvious that on the droplet windward surface, the shear effect caused by divergent shock wave has 
a larger intensity than that caused by planar shock wave on the  whole, whereas the normal impingement caused by 
divergent shock wave is consistently weaker. This difference contributes to the stronger elongation of equator liquid 
ligaments in the divergent shock case, as presented in Figure 8. Besides, it is worth noting that, the diffraction point 
is located upstream of the geometric equator in the divergent shock case, while the two coincide in the planar shock 
case. That leads to a relatively upstream location of the ligaments in the former case, as mentioned above. 
 
Figure 11. The distribution of the tangential component Vτ and the normal component Vn of post-shock velocity versus the angle θ. 
It’s worth noting that the diffraction point ( θ = θdp), where the shear ef fect caused by external flow attains its 
maximum intensity, does not coincide with the starting point of  K-H instability. For example, in the case of Ma0 = 
2.4 and ω = 6.0 divergent shock wave, K-H instability is first triggered in the vicinity of the point θ = 48.46° < θdp = 
81.79°. To explain the phenomenon, it is essential to consider the fact that the deformation behaviors of the droplet 
surface is also influenced by the evolution of the internal flo w field within the droplet, especially the impingement 
of the transmitted shock wave as well as its reflection wave. A fter the generation of the t ransmitted shock wave, its 
wave front initially stays attached to the external divergent s hock wave, until a critical instant when the movement 
of contact point Pθ is unable to catch up with the propagation of the transmitted shock wave, as presented in Figure 
12. Referring to our previous work46, the instant the transmitted shock just detaches from the incident shock is defined

<!-- PDF_PAGE: 17 -->

as the critical time ( tcr) and the corresponding contact a ngle is defined as the critica l contact angle ( θcr). θcr can be 
determined through the following expression, where cl,0 and cg,0 are initial speed of sound of liquid and gas phase, 
respectively. 
 
2
,0cr
cr ,0 cr
1 .(1 ) 2 (1 s
()
)
s
co
1i n
l
g
c
cM a 
 

     (4.7) 
It must be noted that, during the propagation of the transmitte d shock wave, it continuously impinges the droplet 
surface outwards and thus induces  an outward velocity of surfac e movement. Actually, this process acts as a 
competitive mechanism of the inward impingement caused by external airflow. 
 
Figure 12. Schematic diagram of the generation of the transmitted shock wave (TS) induced by the impingement of external diver gent 
shock wave. (a) the schematic diagram at critical time tcr; (b) the schematic diagram at the time t1 after critical time tcr. 
Subsequently, we can analyze the essential mechanisms underlyin g the formation of the fixed-point and the 
corresponding generation of K-H instability on droplet windward  surface. The following discussion will show that 
the fixed-point first emerges at the critical contact point at the critical time. We first consider the surface deformation 
induced by the incident divergent shock wave and the transmitted shock wave nearby the critical contact point at t = 
tcr and t = t1 (t1 → tcr
+), as illustrated in Figure 13. Define a function r(θ, t) as the radial distance of the position θ 
relative to the initial center C at the time t. The contact positions of the incident shock wave and the transmitted shock 
wave at the time t are defined as θIS, t and θTS, t , respectively. By the time t1 , the surface segment immediately upstream 
of θcr has experienced the strong normal impingement induced by exter nal airflow and relatively neglectable 
impingement from inside the droplet. Therefore, there exists an angle θ1 such that r(θ, tcr) < RD , θ1 ≤ θ < θcr; r(θ, tcr) 
= RD , θ ≥ θcr; r(θ, t1) < RD, θ1 ≤ θ ≤ θcr. Besides, due to the aforementioned detachment, the surface se gment θIS, t1 ≤ 
θ < θTS, t1 has been subjected to solely the internal impingement. Therefore, r(θ, t1) > RD, θIS, t1 ≤ θ < θTS, t1. Considering 
the continuity of the droplet surface, there definitely exits a t least one fixed-point θf, t1 within the interval (θcr , θIS, t1) 
at t1. If the fixed-point is not unique, then any one of them can be  selected to ensure the validity of the subsequent 
discussion. Noting that θcr < θf, t1 < θIS, t1 and the limit relation θIS, t1 → θcr
+, t1 → tcr
+, the following relation also holds, 
 
1f, c r 1 c r ,  .t tt   (4.8)

<!-- PDF_PAGE: 18 -->

Physically, it implies that the critical contact point θcr serves as the inception location for the formation of the fixed-
point and the fixed-point initially advances downstream upon its emergence. 
 
Figure 13. Schematic diagram of the local deformation induced b y the propagation of the incident shock wave (IS) and the transmitted 
shock wave (TS) surrounding the critical contact point at (a) t = tcr and (b) t = t1 (t1 → tcr
+). 
After its generation at the critical contact point, the fixed-p oint undergoes continuous migration on the windward 
surface due to the alterations o f the surrounding flow field. T hese alterations are attributed to complex factors, 
particularly the subsequent reflections of the transmitted shock wave. Nevertheless, along with the attenuation of the 
internal wave systems and the stabilization of the external flo w field, the streamline distribution surrounding the 
windward surface evolves towards a stabilized state at t* ~ 0.15, resulting in a special position on the windward 
surface which is subjected to solely shear effect with nearly zero normal velocity, as illustrated in Figure 9. Therefore, 
the fixed-point ultimately migrates to the special position above and becomes relatively immobile at t* ~ 0.15. Under 
the action of strong shear effect, the K-H instability of the droplet surface is thus triggered at nearly the same position 
and the same time. 
Table 1. The critical contact point θcr , the finally-resting position of the fixed-point θf and the diffraction point θdp under different 
intensities and curvature radii of incident divergent shock wave. 
  θcr θf θdp 
Ma0 = 2.40 
ω = 4.0 28.12° 43.71° 78.46° 
ω = 6.0 30.22° 48.46° 81.79° 
ω = 8.0 31.30° 50.36° 83.62° 
ω = ∞ 35.08° 52.24° 90.00° 
Ma0 = 3.20 
ω = 4.0 40.47° 43.24° 78.46° 
ω = 6.0 43.19° 49.32° 81.79° 
ω = 8.0 44.69° 49.81° 83.62° 
ω = ∞ 50.03° 50.37° 90.00°

<!-- PDF_PAGE: 19 -->

The finally-resting position of the fixed-point, which coincide s with the generation site of K-H instability, is 
determined by the equilibrium between the impingements of exter nal airflow and internal waves. In Table 1, the 
critical contact point θcr, the finally-resting posi tion of the fixed-point θf observed in numerical cases and the 
diffraction point under different intensities and curvature radii of incident shock wave, are listed. Notably, the increase 
of the shock curvature radius results in all of the three angles increasing but each to its own extent. This phenomenon 
is attributed to the fact that the entire flow field becomes more parallel to streamwise direction for a larger curvature 
radius. On the other hand, the variation of intensity Ma0 has significant influence only on θcr. It has little effect on θf 
and definitely no effect on θdp. This also implies that the generation position of K-H instability on windward surface 
will not be significantly influenced by the intensity Ma0. 
Also, we can explain qualitatively why the K-H instability is f irst triggered near the fix ed-point instead of other 
positions. For the positions on the surface segment 0 ≤ θ < θf, especially those close to the front stagnation point, the 
intensity of the shear effect is insufficient to induce K-H ins tability. Nevertheless, these positions are subjected to 
normal acceleration directed inwards, which is a mechanism trig gering the R-T instability observed in Figure 8. As 
for the positions on the surface segment θf < θ ≤ θdp, particularly those close to the diffraction point, they are subjected 
to relatively strong shear effect but simultaneously the normal acceleration directed outwards caused by local pressure 
gradient. This acceleration, d irected from the high-density liq uid to the low-density gas , serves as an interface-
stabilizing mechanism and effect ively inhibits the growth of K- H instability. Additionally, the shear effect on the 
leeward surface, mainly caused by the recirculating flow, is also insufficient to generate K-H instability. 
4.4. Global dynamics of the droplets 
As discussed above, the droplet undergoes significant deformation and aerobreakup under the impingement of the 
incident shock wave, and the deformation process influenced by the shock wave’s curvature. In this section, we will 
analyze the global dynamics of the droplets shocked by the divergent and planar shock wave and it can be represented 
by the kinetic properties of the droplet center-of-mass. These kinetic properties, including the displacement ∆ xc, 
velocity uc and acceleration ac of the droplet’s center-of-mass, are obtained by the following expressions. 
 
up
up
,0
,0
,0
d
,
d
ll
cc c
ccc c
cc c ll
A
x x
y y
x
y A




        

 


x
xxx x  (4.9) 
 
up up
up up
2
2
dd
dd ,,d ddd
ll ll
cc
cc
l
x
y ll
x
l y
A A
ua
uat tA A
 
 


      
 


ua
xxua  (4.10) 
where, the subscript "0" represents the initial state of the dr oplet. For a better analysis on the spanwise deformation 
and aerobreakup behavior of the shocked droplet, only the upper half of the droplet’s main body is considered as the 
integral region Ωup. Here, the droplet’s main body is defined as the maximum-area simply connected domain within 
the liquid region. 
As presented in Figure 14, these kinetic quantities are normalized by the droplet’s initial diameter D0 and the post-
shock airflow velocity ug. It is obvious that in both cases, the streamwise displacement  increases nonlinearly upon 
the impingement of the incident shock wave, with a continuously  increasing streamwise velocity. However, the

<!-- PDF_PAGE: 20 -->

variation of streamwise acceleration is non-monotonic, as prese nted in Figure 14(e). The transient impingement of 
the incident shock wave leads to a substantial peak of the stre amwise acceleration within a short time. This 
acceleration subsequently decreases due to the pressure drop on  the windward surface and the pressure rise on the 
leeward surface until t* ~ 0.20, based on the pressure field illustrated in Figure 5. The following increase of the 
streamwise acceleration is governed by the area enlargement of the windward surface caused by the spanwise 
elongation of the droplet. The streamwise deflection and aerobreakup of the liquid ligaments result in the stagnation 
of the droplet’s elongation and thus the end of streamwise acceleration increase, at t* ~ 0.50 in the planar shock case 
and t* ~ 0.80 in the divergent shock case. In addition, it is also obvious in comparison that the streamwise acceleration 
induced by the planar shock wave is generally greater than that  induced by the divergent shock wave, since the 
impingement in the latter case is relatively weak, as presented  i n Figure 11. That results in a slower streamwise 
velocity in the divergent shock case. 
 
Figure 14. The kinetic properties of the droplet center-of-mass under the impingement of the divergent shock ( Ma0 = 2.4, ω = 6.0) and 
the planar one ( Ma0 = 2.4, ω = ∞). ( a) streamwise displacement ∆ xc, (b) spanwise displacement ∆ yc, (c) streamwise velocity ux, (d) 
spanwise velocity uy, (e) streamwise acceleration ax, (f) spanwise acceleration ay.

<!-- PDF_PAGE: 21 -->

The spanwise motion of the shocked droplets also exhibits diffe rences in the two cases. It is worth noting that 
within the early-stage deformation period (t* ≤ 0.40), the spanwise kinetic properties in the two cases are similar, with 
almost identical trends in spanwise displacement and velocity. During this time period, the droplet deformation is 
mainly characterized by the continuous flattening instead of the spanwise elongation and the curvature of the incident 
shock wave is thus incapable of exerting a significant influenc e. The differences emerge mainly during late-stage 
deformation period (t* ≥ 0.50). The spanwise velocity in the planar shock case finall y stops increasing and become 
steady around a constant at t* ~ 0.50. This behavior just corresponds to the streamwise deflection and aerobreakup of 
the liquid ligaments near the droplet’s equator at nearly the s ame time, as presented in Figure 8. Whereas, in the 
divergent shock case, the spanwise elongation length of the liquid ligaments is significantly larger, which is attributed 
to the stronger spanwise shear effect exerted by the post-shock  airflow. Consequently, in this case, the spanwise 
velocity maintains its increasing trend until it finally become steady around a relatively large constant at t* ~ 0.80. As 
a result, in comparison, the global spanwise motion in the dive rgent shock case is more significant than that in the 
planar shock case, as demonstrated in Figure 14(b) and (d). 
In order to quantify the global characteristics of the deformat ion morphologies, the four physical quantities, 
including the streamwise width Lst, spanwise width Lsp, central width Lc and equivalent degree of stripping ms, are 
investigated, as illustrated in Figure 15. Noting that the equivalent degree of stripping ms is defined as the difference 
between the initial mass and the present mass of the droplet’s upper main body. 
 
Figure 15. The variation of the streamwise width Lst (a), the spanwise width Lsp (b), the central width Lc (c) and the equivalent degree of 
stripping ms (d) in the divergent shock case (Ma0 = 2.4, ω = 6.0) and the planar shock case (Ma0 = 2.4, ω = ∞).

<!-- PDF_PAGE: 22 -->

The general droplet will be continuously compressed along the s treamwise direction by the impingement of the 
incident shock wave, which results in the decreasing trends of the streamwise width Lst and the central width Lc. It is 
noticeable in Figure 15(c) that the decreasing trends of Lc in the two cases are almost identical within the time range 
0 ≤ t* ≤ 0.80. This phenomenon suggests that the compression effect on the droplet’s main body is almost unaffected 
by the shock wave curvature. The early-stage decreasing trends of Lst are also similar in the two cases, until t* ~ 0.60 
when Lst in the planar shock case undergoes a rapid recovery. The latte r phenomenon in the planar shock case is 
attributed to the streamwise deflection of the liquid ligaments near the droplet’s equator, as showed in Figure 8. The 
same reason also causes the stagnation in the increase of the spanwise width Lsp at t* ~ 0.60 in the planar shock case, 
when Lsp in the divergent shock case is still increasing. The above ana lysis implies that the main influence of the 
shock wave curvature lies in the deformation behaviors near the droplet’s equator instead of those near the droplet’s 
central axis. 
Additionally, compared with the planar shock case, the fragmentation of the droplet shocked by the divergent shock 
wave within the range 0 ≤ t* ≤ 0.80 is less significant, whi ch can be characterized by the smaller equivalent degree 
of stripping ms. This phenomenon is also associat ed with the droplet’s deforma tion morphologies, especially the 
stripping of liquid ligaments, as showed in Figure 8. The aerodynamic cutting effect induced by the divergent shock 
wave is weaker than that induced by the planar shock wave. Cons equently, in this case, the liquid ligaments cannot 
be destructed by the post-shock airflow within a short time, which results in a relatively weak fragmentation effect. 
 Conclusion 
In this study, we conduct a numerical simulation on the dynamic characteristics of a cylindrical droplet impinged 
by a divergent shock wave. The deformation morphologies, the inception of K-H instability on windward surface and 
the droplet’s global dynamics are analyzed and compared with the planar shock case. 
Several significant characteristics of the deformation morphology can be observed, such as the general flattening 
deformation, the generation of K -H instability on the windward surface, the emergence and spanwise elongation of 
the liquid ligaments near the droplet’s equator. The ligaments subsequently get deflected streamwise and break apart. 
The effect of the shock wave’s curvature mainly lies in the lig ament deformation behavior. Compared to the planar 
shock case, the ligaments in the divergent shock case appear cl oser to the droplet’s front, undergoing a further and 
more persistent spanwise extension before streamwise deflection and breakup. 
Subsequently, we concentrate on the inception location of the K-H instability on the droplet windward surface. It 
is found that the starting point of the K-H instability is almost consistent with a windward fixed-point. The formation 
of the fixed-point is a result of the local surface movement in duced by the combined impingement of external and 
internal flow. A simplified theoretical analysis indicates that the fixed-point first emerges at the critical contact point 
of the precursor transmitted shock, and it undergoes continuous  migration on the windward surface until finally 
resting at a special position s ubjected to solely shear effect.  The finally-resting position is also the most favorable 
location for the growth of K-H instability without other interf ace-stabilizing mechanism, which explains the above 
consistency. And the increase of the shock curvature radius results in the position moving downstream. 
The global dynamics of the deformed droplet is also analyzed in  this paper. The non-monotonic variation of the 
streamwise acceleration is related to early-stage shock-droplet  interaction as well as the late-stage deflection and 
aerobreakup of the liquid ligaments. It is observed that in the divergent shock case, the streamwise velocity is slower

<!-- PDF_PAGE: 23 -->

while the spanwise motion is more significant, compared to the planar shock case. This phenomenon is also 
demonstrated in the quantified analysis of the deformed droplet . Additionally, the fragmentation of the droplet 
impinged by the divergent shock wave is less prominent than that in the planar shock case. 
Synthetically, this study mainly analyzes the curved shock-drop let interaction characteristics and clarify the 
curvature effect on the droplet deformation behaviors. It contr ibutes to researchers' better understanding of fuel 
injection and atomization processes in supersonic propulsion systems where complex curved shock waves inherently 
exist, although the present work is just a primary exploration.  In the future, we will further investigate the three-
dimensional curved shock-droplet interaction and corresponding deformation mechanisms, considering the viscosity, 
capillary effect and even phase transition. 
Acknowledgements 
The present work would like to acknowledge the support from the  Natural Science Foundation of China (NSFC, 
Grant No. 52306152) and China Postdoctoral Science Foundation (No. 2023M731912). 
Author Declarations 
Conflict of Interest 
The authors have no conflicts to disclose. 
Author Contributions 
Haotian Chen: Conceptualization (equal); Formal analysis (lead); Investigat ion (equal); Visualization (equal); 
Writing – original draft (lead). Xin Jin: Conceptualization (supporting); Investigation (equal); Methodology (equal); 
Writing – review & editing (equal). Wei Wang: Conceptualization (supporting); Investigation (equal); Methodology 
(supporting); Writing – review & editing (supporting). Sheng Xu: Conceptualization (lead); Formal analysis (equal); 
Investigation (lead); Methodology (lead); Software (lead). Bing Wang : Conceptualization (equal); Funding 
acquisition (lead); Investigation (equal); Supervision (lead); Writing – review & editing (lead). 
Data Availability 
The data that support the findings of this study are available from the corresponding author upon reasonable request. 
Appendix A. The generation of a divergent shock wave 
Figure 16 shows the schematic of the wall profile, which transforms the planar shock into a cylindrical divergent 
one. The shock tube consists of three parts: the planar wall se ction (A1A2B2B1), the convex wall section (B1B2D2D1) 
and the oblique wall section (D1D2E2E1). A1A2 is the shock tube inlet, and an incident planar shock with MaA intensity 
is initially placed here. When the incident shock propagates wi thin A1A2B2B1, the shock profile remains planar, and 
the shock intensity keeps MaA, that is, MaB = MaA. While the incident shock propagates into B1B2D2D1, the planar 
shock will be gradually transformed into a curved one and evolv e into a cylindrical divergent shock at D1D2 with 
MaD intensity and RD curvature radius. The oblique wall section weakens the cylindrical divergent shock but keeps 
the shock profile cylindrical when the shock wave propagates inside this section. In the present study, the cylindrical 
divergent shock at D1D2 is expected; hence, it is urgent to design the convex wall section to achieve our desire. 
Firstly, a brief overview of the fundamental theoretical principles of shock dynamics is required. According to the 
shock dynamics theory80, the characteristic relations are written as,

<!-- PDF_PAGE: 24 -->

for the upward wave 
 dd  a l o n g t a n , d
Ma y JcA x      ( A . 1 )  
for the downward wave 
 dd  a l o n g t a n , d
Ma y JcA x      ( A . 2 )  
where, 
 

 
2 11 ,2
Ma K MaMac AM a A A

    ( A . 3 )  
  
2
2
1
arctan arctan . 2
Ma K MacA
Ma Ma

  ( A . 4 )  
It is not difficult to know that in the single-wave region, only one type of characteristic line crosses the region, and 
the shock intensity remains constant. 
 
Figure 16. The schematic of the wall profile which transforms the planar shock into a cylindrical divergent one. H: the half height of the 
tube; MaA = MaB: the incident planar shock intensity; MaD: the intensity of cylindrical divergent shock;  RD: the curvature radius of 
cylindrical divergent shock; θD: the divergent angle of the tube. 
Given the divergent shock (D1D2) intensity MaD, curvature radius RD and divergent angle 2θD, the profile of curved 
wall (B1D1) and (B2D2) can be calculated from the following three steps.  
(1) Calculating the incident planar shock intensity MaB and height 2H. 
 
 2 1
,2 d
DD
AA
Ma Ma
D
Ma Ma
Ma
Mac K
a
Ma
dM
A

   ( A . 5 )

<!-- PDF_PAGE: 25 -->


2
.
2dexp (1 )
D
A
DD
Ma
Ma
RH
Ma Ma
Ma K Ma


 

 ( A . 6 )  
(2) Solving the double-wave (PD1D2) region. 
2N+1 points with well-distributed are selected on the cylindrical  divergent shock front ( D1D2). The position and 
shock divergent angle of the ith point can be expressed as, 
  11 , cos 1  , sin 1 ,ii D D D D
iixy R R NN            
 ( A . 7 )  
 1 1.iD
i
N 
 ( A . 8 )  
According to the characteristic relations, the shock parameters , including shock intensity and divergent angle, at 
any point in the double-wave region can be solved layer by layer from the divergent shock(D1D2). At point Q, there 
are two independent characteristic lines passing through. As the solving procedure is layer by layer, the parameters 
at point F and point S are known. According to Eq.(A.1) a n d  E q .(A.2), the following two equations are satisfied, 
  tan ,QF QF FFyy xx     ( A . 9 )  
  tan .QS QS SSyy xx      (A.10) 
The coordinates of Q can be obtained as, 
     
 
tan tan ,tan tan
FF F SS S F S
Q
FF SS
x xy yx   
  
     ( A . 1 1 )  
     tan tan
.22
QF FF QS SSFS
Q
xx xxyyy
       (A.12) 
According to different conservation properties of characteristic lines QF and QS, 
 dd ,
Q FMa Ma
QF
Ma Ma
MaM a
cA cA    (A.13) 
 dd .
Q SMa Ma
QS
Ma Ma
MaM a
cA cA    (A.14) 
Hence, the shock divergent angle at Q can be expressed as, 
 
 
2
12 d.2 1
F
S
Ma
QF S
Ma
Ma
Ma K Ma
 

 
 
  (A.15) 
Then, the shock intensity at Q can be calculated by, 
 
 
2
2 d.
1
F
Q
Ma
QF
Ma
Ma
Ma K Ma
 
  (A.16)

<!-- PDF_PAGE: 26 -->

After 2N advancing-layers, all of the expected parameters in the double -wave region are well-solved, including 
the coordinates, shock intensity and shock divergent angle at P, which is the intersection point of the single-wave 
and double-wave regions. 
 (  , ) ,  ,  0 .0PP P BPxy a a MM    (A.17) 
(3) Obtaining the profile of the convex wall. 
The coordinates of B1, the starting point of the convex wall profile, is solved based on the characteristic line emitted 
from point P. 
  
11
 ,  , . tan
BB P
PP
Hx yx H 
   
 (A.18) 
In the second procedure, the coordinates, shock intensities and shock divergent angles of 2N+1 discrete points on 
the interface PD1 between single-wave and double-wave regions have been well-obt ained. The intersection 
coordinates of the characteristic line omitted from the ith discrete point with the curved convex wall can be expressed 
as, 
   tan ,ww
ii ii i iyyxx      (A.19) 
   1
11 tan . 2
iiwwww
iiiiyyxx  

   (A.20) 
Here, ξ is a correction parameter, and ξ = 1.0 is initially adopted. Then, the coordinates of the second point, close to 
B1, of the wall B1D1 can approximately be calculated. Repeating this procedure, the coordinates of all the points on 
the wall B1D1 can be obtained, while the last point obtained may not coincide with point D1 since an inappropriate 
guessed value of ξ. Therefore, in the present work, an iteration method is employed to find the suitable value of ξ. 
References 
1. K. Kailasanath, "Review of Propulsion Applications of Detonation Waves," AIAA J. 38, 1698 (2000). 
2. Z. Wang, J. Chang, W. Hou, and D. Yu, "Low-frequency unsteadiness of shock-wave/boundary-layer interaction in an 
isolator with background waves," Phys. Fluids 32, 056105 (2020). 
3. Z. Wang, J. Chang, G. Wu, and D. Yu, "Experimental investiga tion of shock train behavior in a supersonic isolator," 
Phys. Fluids 33, 046103 (2021). 
4. Z. Wang, J. Chang, Y . Li, R. Chen, W. Hou, J. Guo, and L. Yu e, "Oscillation of the shock train under synchronous 
variation of incoming Mach number and backpressure," Phys. Fluids 34, 046104 (2022). 
5. A. K. Hayashi, N. Tsuboi, and E. Dzieminska, "Numerical Stud y on JP-10/Air Detonation and Rotating Detonation 
Engine," AIAA J. 58, 5078 (2020). 
6. M. Salvadori, A. Panchal, and S. Menon, "Simulation of liqui d droplets combustion in a rotating detonation engine," 
Proc. Combust. Inst. 39, (2022). 
7. Y . Xu, and H. Zhang, "Interactions between a propagating det onation wave and circular water cloud in hydrogen/air 
mixture," Combust. Flame 245, 112369 (2022). 
8. M. Wu, J. Zhang, N. Gui, Q. Zou, X. Yang, J. Tu, S. Jiang, and Z. Liu, "Advances in the modeling of multiphase flows 
and their application in nuclear engineering—A review," Exp. Comput. Multiphase Flow 6, 287 (2024). 
9. A. R. Karagozian, "Transverse jets and their control," Progr. Energy Combust. Sci. 36, 531 (2010). 
10. J. Peters, and M. Birouk, "Liquid jet breakup in a subsonic cross airflow: An experimental study of the effect of the gas 
phase turbulence," Exp. Comput. Multiphase Flow 6, 41 (2024). 
11. A. R. Hanson, E. G. Domich, and H. S. Adams, "Shock Tube In vestigation of the Breakup of Drops by Air Blasts," 
Phys. Fluids 6, 1070 (1963). 
12. M. Pilch, and C. A. Erdman, "Use of breakup time data and velocity history data to predict the maximum size of stable 
fragments for acceleration-induced breakup of a liquid drop," Int. J. Multiphase Flow 13, 741 (1987).

<!-- PDF_PAGE: 27 -->

13. D. D. Joseph, J. Belanger, and G. S. Beavers, "Breakup of a liquid drop suddenly exposed to a high-speed airstream," 
Int. J. Multiphase Flow 25, 1263 (1999). 
14. L. P. Hsiang, and G. M. Faeth, Secondary drop breakup in the deformation regime (American Institute of Aeronautics 
and Astronautics, 1992). 
15. L. P. Hsiang, and G. M. Faeth, Deformation and secondary breakup of drops (American Institute of Aeronautics and 
Astronautics, 1993). 
16. L. P. Hsiang, and G. M. Faeth, "Drop deformation and breaku p due to shock wave and steady disturbances," Int. J. 
Multiphase Flow 21, 545 (1995). 
17. T. G. Theofanous, G. J. Li, and T. N. Dinh, "Aerobreakup in Rarefied Supersonic Gas Flows," J. Fluids Eng. 126, 516 
(2004). 
18. T. G. Theofanous, and G. J. Li, "On the physics of aerobreakup," Phys. Fluids 20, 052103 (2008). 
19. J. Nagy, A. Horvath, C. Jordan, and M. Harasek, "Turbulent Phenomena in the Aerobreakup of Liquid Droplets," CFD 
Letters 4, 112 (2012). 
20. A. L. Klein, W. Bouwhuis, C. W. Visser, H. Lhuissier, C. Su n, J. H. Snoeijer, E. Villermaux, D. Lohse, and H. 
Gelderblom, "Drop Shaping by Laser-Pulse Impact," Phys. Rev. Appl. 3, 044018 (2015). 
21. B. Boyd, S. Becker, and Y . Ling, "Impact of vaporization on drop aerobreakup," J. Fluid Mech. 1000, (2024). 
22. T. G. Theofanous, "Aerobreakup of Newtonian and Viscoelastic Liquids," Annu. Rev. Fluid Mech. 43, 661 (2011). 
23. B. Dorschner, L. Biasiori-Poulanges, K. Schmidmayer, H. El-Rabii, and T. Colonius, "On the formation and recurrent 
shedding of ligaments in droplet aerobreakup," J. Fluid Mech. 904, (2020). 
24. S. Sharma, A. Pratap Singh, S. Srinivas Rao, A. Kumar, and S. Basu, "Shock induced aerobreakup of a droplet," J. Fluid 
Mech. 929, A27 (2021). 
25. S. Sharma, N. K. Chandra, A. Kumar, and S. Basu, "Shock-ind uced atomisation of a liquid metal droplet," J. Fluid 
Mech. 972, A7 (2023). 
26. N. K. Chandra, S. Sharma, S. Basu, and A. Kumar, "Shock-induced aerobreakup of a polymeric droplet," J. Fluid Mech. 
965, A1 (2023). 
27. J. Guo, P . Kang, K. Mu, J. Li, and T . Si, "On shock induced aerobreakup of a wall-attach ed droplet," J. Fluid Mech. 
971, A31 (2023). 
28. X. Yi, "Experimental Study of the Deformation and Breakup o f a Liquid Drop in Shock Induced Gas Flow,"  
University of Science and Technology of China, 2018.  
29. J. C. Meng, and T. Colonius, "Numerical simulations of the early stages of high-speed droplet breakup," Shock Waves 
25, 399 (2015). 
30. J. C. Meng, and T. Colonius, "Numerical simulation of the aerobreakup of a water droplet," J. Fluid Mech. 835, 1108 
(2018). 
31. G. Xiang, and B. Wang, "Numerical study of a planar shock interacting with a cylindrical water column embedded with 
an air cavity," J. Fluid Mech. 825, 825 (2017). 
32. B. Wang, G. M. Xiang, and X. Y . Hu, "An incremental-stencil WENO reconstruction for simulation of compressible 
two-phase flows," Int. J. Multiphase Flow 104, 20 (2018). 
33. B. Guan, Y . Liu, C.-Y . Wen, and H. Shen, "Numerical Study on Liquid Droplet Internal Flow Under Shock Impact," 
AIAA J. 56, 3382 (2018). 
34. N. Liu, Z. Wang, M. Sun, H. Wang, and B. Wang, "Numerical simulation of liquid droplet breakup in supersonic flows," 
Acta Astronaut. 145, 116 (2018). 
35. B. Boyd, and D. Jarrahbashi, "Numerical study of the transc ritical shock-droplet inter action," Phys. Rev. Fluids 6, 
(2021). 
36. D. Li, "Numerical Researches o n the interaction between Sho ck Wave and Aluminum Droplet with Evaporation and 
Combustion,"  Harbin Engineering University, 2021.  
37. P. Das, and H. S. Udaykumar, "A simulation-derived surrogat e model for the vaporization rate of aluminum droplets 
heated by a passing shock wave," Int. J. Multiphase Flow 130, 103299 (2020). 
38. P . Das, and H. S. Udaykumar, "A sharp-interface method for the simulation of shock-induced vaporization of droplets," 
J. Comput. Phys. 405, (2020). 
39. P. Das, and H. S. Udaykumar, "Sharp-interface calculations of the vaporization rate of reacting aluminum droplets in 
shocked flows," Int. J. Multiphase Flow 134, 103442 (2021). 
40. W. Zhu, H. Zheng, and N. Zhao, "Numerical investigations on  the deformation and breakup of an n-decane droplet 
induced by a shock wave," Phys. Fluids 34, 063306 (2022). 
41. A. R. Dworzanczyk, M. Viqueira-Moreira, J. D. Langhorn, M. A. Libeau, C. Brehm, and N. J. Parziale, "On aerobreakup 
in the stagnation region of high-Mach-number flow over a bluff body," J. Fluid Mech. 1002, A1 (2025). 
42. S. Xu, X. Jin, W. Fan, H. Wen, and B. Wang, "Numerical inve stigation on the interaction characteristics between the 
gaseous detonation wave and the water droplet," Combust. Flame 269, 113713 (2024). 
43. W. Fan, Y . Shi, H. Wen, H. Hu, H. Chen, and B. Wang, "Analysis of waves dynamics in a rotating detonation combustor

<!-- PDF_PAGE: 28 -->

fueled by kerosene," Phys. Fluids 36, 106135 (2024). 
44. M. Alicherif, S. B. Rojas Chavez, K. P. Chatelain, T. F. Guiberti, and D. A. Lacoste, "Experimental characterization of 
the cell cycle for multicellular detonations," Combust. Flame 266, 113553 (2024). 
45. Y . Shi, Y . Zhang, X. Jin, H. Wen, and B. Wang, "Parameter influence and calculation model of wall heat flux in kerosene 
two phase rotating detonation combustor," Combust. Flame 273, 113924 (2025). 
46. S. Xu, W. Fan, W. Wu, H. Wen, and B. Wang, "Analysis of wav e converging phenomena inside the shocked two-
dimensional cylindrical water column," J. Fluid Mech. 964, A12 (2023). 
47. D. Igra, and A. Takayama, "Investigation of aerodynamic breakup of a cylindrical water droplet," Atomizat. Sprays 11, 
167 (2001). 
48. Z. Zhai, C. Liu, F. Qin, J. Yang, and X. Luo, "Generation o f cylindrical converging shock waves based on shock 
dynamics theory," Phys. Fluids 22, 041701 (2010). 
49. W. Chester, "The quasi-cylindrical shock tube," Philos. Mag. 45, 1293 (1954). 
50. R. F. Chisnell, "The motion of a shock wave in a channel, with applications to cylindrical and spherical shock waves," 
J. Fluid Mech. 2, 286 (1957). 
51. G. B. Whitham, "A new approach to problems of shock dynamics Part 2. Three-dimensional problems," J. Fluid Mech. 
5, 369 (1959). 
52. G. B. Whitham, "A new approach to problems of shock dynamics Part I Two-dimensional problems," J. Fluid Mech. 2, 
145 (1957). 
53. G. B. Whitham, "On the propagation of shock waves through r egions of non-uniform area or flow," J. Fluid Mech. 4, 
(1958). 
54. W. Wu, G. Xiang, and B. Wang, "On high-speed impingement of  cylindrical droplets upon solid wall considering 
cavitation effects," J. Fluid Mech. 857, 851 (2018). 
55. W. Wu, Q. Liu, and B. Wang, "Curved surface effect on high-speed droplet impingement," J. Fluid Mech. 909, (2020). 
56. G. Allaire, S. Clerc, and S. Kokh, "A five-equation model for the simulation of interfaces between compressible fluids," 
J. Comput. Phys. 181, 577 (2002). 
57. R. Saurel, F. Petitpas, and R. Abgrall, "Modelling phase transition in metastable liquids: application to cavitating and 
flashing flows," J. Fluid Mech. 607, 313 (2008). 
58. V . A. Titarev, and E. F. Toro, "Finite-volume WENO schemes for three-dimensional conservation laws," J. Comput. 
Phys. 201, 238 (2004). 
59. P. Colella, "A Direct Eulerian MUSCL Scheme for Gas Dynamics," SIAM J. Sci. Statist. Comput. 6, 104 (1985). 
60. E. F. Toro, "The HLLC Riemann solver," Shock Waves 29, 1065 (2019). 
61. S. Gottlieb, and C.-W. Shu, "Total variation diminishing Runge-Kutta schemes," Math. Comp. 67, 73 (1998). 
62. K.-M. Shyue, and F. Xiao, "An Eulerian interface sharpening algorithm for compressible two-phase flow: The algebraic 
THINC approach," J. Comput. Phys. 268, 326 (2014). 
63. H. Choung, V . Saravanan, S. Lee, and H. Cho, "Nonlinear weighting process in ghost-cell immersed boundary methods 
for compressible flow," J. Comput. Phys. 433, 110198 (2021). 
64. V . Saravanan, H. Choung, and S. Lee, "Cell-based hybrid adaptive mesh refinement algorithm for immersed boundary 
method," Int. J. Numer. Methods Fluids 
94, 272 (2022). 
65. K. W. Thompson, "Time-Dependent Boundary-Conditions for Hyperbolic Systems," J. Comput. Phys. 68, 1 (1987). 
66. K. W. Thompson, "Time-Dependent Boundary-Conditions for Hyp erbolic Systems .2.," J. Comput. Phys. 89, 439 
(1990). 
67. T. G. Theofanous, V . V . Mitkin, C. L. Ng, C. H. Chang, X. Deng, and S. Sushchikh, "The physics of aerobreakup. II. 
Viscous liquids," Phys. Fluids 24, 022104 (2012). 
68. J. Song, T. Long, and S. Pan, "Effect of phase change on shock wave and n-dodecane droplet interaction with numerical 
investigation," arXiv (2023). 
69. J. D. Anderson, Fundamentals of Aerodynamics (McGraw-Hill, 2011). 
70. B. John, S. Surendranath, G. Natarajan, and V . Kulkarni, "Analysis of dimensionality effect on shock wave boundary 
layer interaction in laminar hypersonic flows," International Journal of Heat and Fluid Flow 62, 375 (2016). 
71. Y . A. Irving Brown, and B. W. Skews, "Three-dimensional effects on regular reflection in steady supersonic flows," 
Shock Waves 13, 339 (2003). 
72. X. Jin, X. Cheng, Q. Wang, and B. Wang, "Numerical analysis of rarefied hypersonic flows over inclined cavities," Int. 
J. Heat Mass Transfer 214, 124401 (2023). 
73. S. Kobayashi, Differential Geometry of Curves and Surfaces (Springer Singapore, 2019). 
74. J. Song, and S. Pan, "Numerical investigation of shock-drop let interaction with high-Mach numbers," Chin. J. Theor. 
Appl. Mech. 54, 2419 (2022). 
75. T. Funada, and D. D. Joseph, "Viscous potential flow analysis of Kelvin–Helmholtz instability in a channel," J. Fluid 
Mech. 445, 263 (2001). 
76. C.-H. Chang, X. Deng, and T. G. Theofanous, "Direct numeric al simulation of interfacial instabilities: A consistent,

<!-- PDF_PAGE: 29 -->

conservative, all-speed, sharp-interface method," J. Comput. Phys. 242, 946 (2013). 
77. S. Sembian, M. Liverts, N. Tillmark, and N. Apazidis, "Plane shock wave interaction with a cylindrical water column," 
Phys. Fluids 28, 056102 (2016). 
78. L. Biasiori-Poulanges, and H. El-Rabii, "High-magnification  shadowgraphy for the study of drop breakup in a high-
speed gas flow," Opt. Lett. 44, 5884 (2019). 
79. J. P. Redding, and P. Khare, "A computational study on shock induced deformation, fragmentation and vaporization of 
volatile liquid fuel droplets," Int. J. Heat Mass Transfer 184, 122345 (2022). 
80. J. P. Best, "A generalisation of the theory of geometrical shock dynamics," Shock Waves 1, 251 (1991).
