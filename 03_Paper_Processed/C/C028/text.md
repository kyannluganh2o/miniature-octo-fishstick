<!-- PDF_PAGE: 1 -->

Journal of Computational Physics 405 (2020) 109005
Contents lists available at ScienceDirect
Journal of Computational Physics
www.elsevier.com/locate/jcp
A sharp-interface method for the simulation of shock-induced 
vaporization of droplets
Pratik Das, H.S. Udaykumar∗
Department of Mechanical Engineering, The University of Iowa, Iowa City, IA 52242, United States of America
a r t i c l e i n f o a b s t r a c t
Article history:
Received 6 March 2019
Received in revised form 14 August 2019
Accepted 1 October 2019
Available online 27 November 2019
Keywords:
Sharp-interface method
Levelset method
Ghost ﬂuid method
Droplet vaporization
Shock-droplet interaction
A sharp-interface method is developed to calculate the vaporization of droplets in high-
speed ﬂows. The levelset method is used to track the liquid-gas interface. A sharp-interface 
approach using an interfacial Riemann solver based ghost ﬂuid method (RS-GFM) is 
developed to couple the liquid and gas ﬂow-ﬁelds  at the interface. The interfacial Riemann 
problem accounts for surface tension and phase change effects, which affect the jump 
in pressure and the normal velocity ﬁelds across the interface. The current RS-GFM also 
accounts for the jump in viscous stresses at the interface caused by the Marangoni effect. 
The resulting sharp-interface approach captures all the ﬁrst-order physical effects at play 
in shock-induced droplet vaporization. The method is validated by comparing the current 
results with benchmark experimental and numerical results. Finally, 2D and 3D simulations 
of shock-droplet interactions are performed to quantify the shock-induced vaporization rate 
of the droplets, under the inﬂuence of viscosity and surface tension.
© 2019 Elsevier Inc. All rights reserved.
1. Introduction
Shock-induced vaporization of droplets plays an important role in various engineering applications such as the com-
bustion of fuel in rocket engines [1], scramjet engines [2], liquid-fueled pulse detonation engines [3], the detonation of 
heterogeneous explosives [4] and others. In such applications, vaporization of the fuel droplets controls the rate of chemical 
reactions and consequently the rate of energy deposition. Studying shock-induced vaporization of droplets through physical 
experiments is challenging because of the short time-scales and the small length-scales involved in such ﬂows. An alterna-
tive route to understand and quantify the physics is through direct numerical simulations of the droplet-shock interaction. 
However, highly resolved simulations of droplet interaction and vaporization in shocked ﬂows are challenging as the shocks 
and interfaces must be captured accurately, and the interfacial conditions must be well represented. The present work seeks 
to meet this challenge by developing a sharp-interface Eulerian approach for shock-droplet interactions that includes the 
primary ﬁrst-order physical effects, viz. viscosity, surface tension, thermal transport, and phase change.
In the past, several numerical frameworks have been developed to model liquid-gas interfaces in the context of droplet 
and bubble dynamics. For example, interfaces have been explicitly tracked in boundary-ﬁtted moving grid methods [5–7], 
arbitrary Lagrangian-Eulerian methods [8,9] and the free-Lagrange methods [10,11]. In these methods, the interfaces are 
treated as boundaries of a computational sub-domain, i.e. the two phases are meshed separately, and the compatibility 
conditions are applied at the sharp interface. The topology of the computational domain changes with the interface as the 
* Corresponding author.
E-mail address:hs-kumar@uiowa.edu (H.S. Udaykumar).
https://doi.org/10.1016/j.jcp.2019.109005
0021-9991/© 2019 Elsevier Inc. All rights reserved.

<!-- PDF_PAGE: 2 -->

2 P. Das, H.S. Udaykumar / Journal of Computational Physics 405 (2020) 109005
ﬂow evolves. In large deformation cases, ﬁtted grids can suffer severe distortion and need to be periodically re-meshed to 
maintain robustness and accuracy. The complexities of managing grids in the moving grid methods are ampliﬁed in 3D 
calculations [12].
The numerical complexities and the computational burden of mesh management are alleviated in the ﬁxed grid, Eu-
lerian methods, which include front-tracking [13–16], diffuse-interface (DIM) [17,18], volume-of-ﬂuid (VoF) [19–21] and 
levelset-based sharp-interface (LS-SIM) [22–27] methods.
Among the ﬁxed-grid methods, the diffuse interface methods (DIM) [17,28]o f f e r s a convenient route to capturing the 
interfaces in multiphase ﬂow simulations. Previous studies of shock-droplet interactions [29–34]s h o w that DIM can ade-
quately handle the large deformation of the material interfaces. However, in DIM, the interface is spread over a ﬁnite number 
of grid points in the computational domain. A mixture-model or artiﬁcial equation of state (EOS) describing the mixture 
of the two phases need to be developed in the thickened interfacial region in the DIM [18,35]. Such mixture equations of 
state lack physical validity. Chinnayya et al. [36]d e r i v e d a mixture model for ﬂows with embedded interfaces which did 
not require a mixture equation of state. However, their model was limited to interfaces without phase-change. Accurately 
modeling phase-change at the droplet surface through DIM still remains an unresolved challenge. Furthermore, in DIM, 
the interface thickens further over time because of numerical diffusion [32]. To mitigate the unphysical thickening of the 
material interface, several interface sharpening schemes have been developed [37,38]. However, often interface sharpening 
schemes are non-conservative in nature [32]. Since the vaporization rate of a droplet is sensitive to the interface deﬁnition 
and the local thermodynamic quantities at the interface, it is challenging to compute the vaporization rate of a droplet using 
DIM approaches.
In contrast to DIM, in sharp-interface methods (SIM), the interface delineates phases sharply using volume fraction track-
ing [39,40]o r levelsets [22,41,42]. Therefore, the thermodynamics of the interface is represented by the EOS of each distinct 
phase instead of the mixture EOS. The rate of phase change at the interface is computed directly from the thermodynamic 
variables in the ﬂowﬁeld.  In an implicit interface representation framework, volume-of-ﬂuid (VoF) [19,20] and levelset (LS) 
[23]a r e two popular ways to track sharp interfaces. In VoF, the local volume fraction of the phases in a computational 
cell is used to track the location of the interface. The interface is reconstructed sharply at the grid cells where both the 
phases exist. The advantage of the VoF method is that the explicit volume tracking ensures the conservation of mass in 
the calculations. However, the reconstruction of the interface from the marker function is numerically challenging [43–45], 
especially in 3D [46]. Inaccurate estimation of local curvature and the surface tension forces at the interface is known to 
cause unphysical perturbations in the ﬂow [45,47]. Such challenges of sharp-interface VoF method are addressed in some 
of the recent works [39,48]. But modeling phase change through the VoF method is not straightforward [40,48,49]. For ex-
ample, an accurate calculation of the Stefan problem requires an iterative solver to ensure volume balance at the interface 
[48]. Furthermore, grid reﬁnement may cause stiffness in the treatment of the phase change at the interface [49]. Therefore, 
solving problems involving vaporizing interface using VoF is not straightforward.
Another way of representing the interfaces sharply is through the levelset method. In the levelset based tracking, the 
signed normal distance is evolved at each cell in the Cartesian grid in a narrow-band surrounding the interface [24], and 
the zero levelset contours represent the embedded sharp interface. The geometrical information, such as local normal and 
curvature of the interface, is computed in a straightforward manner from gradients of the levelset ﬁeld [23]. Unfortunately, 
the levelset based deﬁnition of the interface does not enforce conservation of mass of the phases separated by the interface 
explicitly. The mass conservation error is aggravated due to numerical diffusion. However, it can be mitigated by reducing 
the spatial discretization error [50]. Higher-order numerical treatment using 5th order WENO [51,52] and local mesh re-
ﬁnement has been shown to reduce mass conservation error signiﬁcantly [51,53]. There are also approaches that have been 
developed to impose a mass conservation constraint within the levelset evolution procedure [54,55]. Despite the mass con-
servation issue, the levelset method allows for the robust and numerically stable computation of the interfacial mechanics 
without encountering numerical complexities in tracking complex interfaces. Sharp-interface phase change treatment can 
also be implemented in a straightforward way in the levelset framework.
The major challenges for the levelset-based framework lie in the numerical implementation of the coupling between the 
two phases at the interface. The sharp interface is embedded in a ﬁxed Cartesian mesh; since the mesh is non-boundary 
conforming, special treatment is needed to couple the ﬂow variables in each phase across the interface. This treatment is 
implemented in a layer of grid cells, otherwise known as “ghost cells”, adjoining the interface in each phase. The Ghost 
Fluid Method (GFM) [56,57] provides a way to couple ﬁelds across a sharp interface. In the past, GFM has been developed 
to simulate droplets in compressible ﬂow [16,41,49,57]. Liu et al. [53]s h o w e d that the Riemann solver based GFM (RS-GFM) 
treats wave propagation through multi-material interfaces in a physically consistent manner while minimizing numerical 
artifacts in the solution. The RS-GFM has been successfully used in the inviscid solutions of shock-droplet interactions [37]. 
However, the problem of shock-induced vaporization of droplets calls for further improvement of the previous RS-GFM to 
incorporate the jump conditions for deviatoric stresses and the heat ﬂuxes across the interfaces.
The implementation of the jump-conditions for the deviatoric stresses at the interfaces through the GFM is challenging 
because embedded interfaces do not align with the axis of the Cartesian grid. In several previous works [26,58,59], GFM 
accounting for the jump in deviatoric stresses across the interface has been developed in the context of incompressible 
multiphase ﬂows. However, there have been few efforts towards developing GFM to simulate vaporizing interfaces in viscous, 
compressible ﬂows. Houim et al. [45]m o d i ﬁ e d the RS-GFM for reacting gas-liquid interfaces in compressible viscous ﬂows. 
In their GFM implementation, four simultaneous equations in 2D and six simultaneous equations for 3D are solved at each

<!-- PDF_PAGE: 3 -->

P. Das, H.S. Udaykumar / Journal of Computational Physics 405 (2020) 109005 3
ghost cell to ensure that the jump conditions for deviatoric stresses are respected. Furthermore, Houim et al. [45]r e p o r t e d 
stability issues on ﬁne grids. In their GFM, the stress tensor is rotated along the interface normal direction before imposing 
the jump condition on the stresses at the interface. Rotation of the deviatoric stress tensor leads to numerical instabilities 
at ﬁner grid resolutions [45].
In this work, we couple the levelset interface evolution with a hydrocode to develop a sharp-interface approach for 
shock-induced droplet vaporization. The GFM designed by Houim et al. [45]i s further modiﬁed and a relatively simple 
implementation of the interfacial jump conditions is proposed. In the current GFM, the interfacial jump conditions for the 
deviatoric stresses are imposed by solving explicit algebraic equations. The numerical instabilities on ﬁner grids are avoided 
by rotating the velocity ﬁeld instead of the stress tensor. The robustness of the current GFM is substantiated through the 
results presented in this paper.
The current method is also extended to 3D calculations. Interface-resolved 3D simulations of shocked multiphase ﬂows 
are scarce in the literature. 3D simulations of shock interaction with solid particles [60–63] and droplets [30]w e r e per-
formed in few previous works. However, to the authors’ knowledge, 3D calculation of vaporization of a droplet in shocked 
ﬂow has not been demonstrated before in the open literature. The sharp-interface framework developed in this work is used 
to perform a 3D calculation of shock-induced vaporization of a water droplet
The numerical frame-work used in this work is described in Section 2. Several validation tests of the numerical method 
are presented in section 3.1–3.4. A 1D air-water shock tube problem is solved using the current method and the results 
are compared with the exact solution in section 3.1. Shock interaction with a cylindrical water droplet is simulated and 
the current results are compared with experimental and previous numerical results [16]i n section 3.2 and 3.3 respectively. 
An axisymmetric calculation of shock-induced vaporization of an aluminum droplet is performed to compare the current 
results with Houim et al. [45]i n Section 3.4. 2D and 3D simulations of shock interaction with a vaporizing water droplet 
are demonstrated in sections 3.5 and 3.6. Finally, the conclusions of the current study are presented in Section 4.
2. Methods
The governing equations for compressible ﬂows, cast in Cartesian coordinates, are solved for the gaseous and the liquid 
phase. A levelset-based sharp-interface method implemented on the ﬁxed Cartesian grid is used to represent the interface 
between the two phases. The gas-phase consists of a mixture of air and vapor released from the liquid droplet. Therefore, 
at w o - s p e c i e s mixture model is used in the gaseous phase. The liquid phase is treated as a pure, single-component material. 
The Tait EOS is used to couple the pressure and density in the liquid phase. The governing equations are described in the 
following subsection.
2.1. Governing equation
The governing equations for compressible multicomponent ﬂow are solved in the following form:
∂
∂t (ρYk) + ∂
∂xj
(ρuj Yk) = ∂
∂xj
(− Jj,k) + ˙ωk (1)
∂
∂t (ρui) + ∂
∂xj
(ρuiuj + δij p) = ∂
∂xj
(τij) + Mi (2)
∂
∂t (ρE) + ∂
∂xj
[
uj(ρE + p)
]
= ∂
∂xj
(uiτij − qj) + SE (3)
where ρ, Yk, ui, p and E are the density, species mass fraction, velocity component, pressure, and the speciﬁc total energy, 
respectively. The subscript k is an index identifying species in the multicomponent system. Here, the gaseous phase has two 
components, air (k =1) and vapor (k =2). The liquid phase is treated as a pure material (k =1i n the liquid phase). i, j are 
the coordinate indices of the computational domain.
The viscous stress tensor in Eq. (2)i s given by:
τij = μ
( ∂ui
∂xj
+ ∂uj
∂xi
)
− 2
3μ∂uj
∂xj
δij (4)
The heat-ﬂuxes due to thermal diffusion and species diffusion effects are obtained from:
qj =
N∑
k=1
Jj,khk − ∂(kT )
∂xj
(5)
where N is the total number of species in the gaseous phase. hk is the speciﬁc enthalpy of kth species, μ and k are the 
mixture averaged viscosity and thermal conductivity. The diffusion mass-ﬂux ( Jj,k) of the kth species is obtained from:
Jj,k = ρYk vj,k (6)

<!-- PDF_PAGE: 4 -->

4 P. Das, H.S. Udaykumar / Journal of Computational Physics 405 (2020) 109005
Fig. 1. Calculation of the rate of vaporization at the gas-liquid interface.
where vj,k is the diffusion velocity of the kth species along the jth direction. The diffusion velocities are ﬁrst calculated 
from [64]:
ˆvj,k =− Dk,mix
Xk
( ∂Xk
∂xj
+ (Xk − Yk)∂(ln p)
∂xj
)
(7)
where Xk is the mole fraction of the kth species. The mixture averaged diffusion coeﬃcient, Dk,mix is obtained from binary 
diffusion coeﬃcients, Dkl using:
Dk,mix = 1 − Yk
∑N
l=1,k̸=l Xl/Dkl
(8)
The estimated diffusion velocities of the kth species is then corrected to ensure mass conservation [65]:
vj,k = ˆvj,k −
N∑
k=1
Yk ˆvj,k (9)
The source term in the species transport Eq. (1), ˙ωk, accounts for the vapor added to the gaseous phase at the interface. 
˙ωk is computed from the following equation:
˙ωk =
{0, for k=1
˙m′′ Aint
V , for k =2 (10)
where Aint is the area of the interface within a computational cell. V is the volume occupied by the gaseous phase in a cell. 
The geometrical interpretation of the quantities Aint and V is demonstrated through a representative computational cell in 
Fig. 1. Aint and V are computed using algorithms described in [44,51]. ˙m′′ is the evaporation mas-ﬂux at the gas-liquid 
interface and is computed from the Scharge-Knudsen equation [49]:
˙m′′ = 2C
2 − C
√
Mwk
2πRu
( psat
√
Tl
− pv√
Tg
)
(11)
where
C =
{
1 −
( ρg
ρl
) 1
3
}
exp
(
− 1
2(ρl/ρg)1/3 − 2
)
Ru is the universal gas constant in the above equation. Mwk is the molecular weight of the kth species, in this case, the 
molecular weight of the vapor.
The source terms Mi and SE in the momentum (Eq. (2)) and energy (Eq. (3)) conservation equation represent the mo-
mentum and energy associated with the vapor added to the gaseous phase, respectively. Mi is calculated from:

<!-- PDF_PAGE: 5 -->

P. Das, H.S. Udaykumar / Journal of Computational Physics 405 (2020) 109005 5
Mi =
N∑
k=1
˙ωkui (12)
where ui is the ith component of the velocity vector in the gaseous phases at the interface.
SE is calculated from:
SE =
N∑
k=1
˙ωk ×
[(
hf,k +
T∫
To
Cp,k(τ)dτ
)
− Ru
Mwk
T
]
(13)
where hf,k is the speciﬁc enthalpy of formation of the kth species at the reference state (T0 =298 K). Cp,k(T) is the speciﬁc 
heat capacity at a constant pressure of the kth species, at a temperature T. Cp,k(T) is a polynomial function of temperature 
T in the absolute scale and taken from [66].
Pressure (p) is computed from the EOS. Separate equations of state are used in the gaseous and liquid phases, as speciﬁed 
below.
2.1.1. The EOS in the gaseous phase
The gaseous phase is a mixture of air and vapor released at the liquid-gas interface. The pressure p in the gaseous phase 
is calculated by applying Dalton’s law of partial pressure for the ideal gas:
p =
n∑
k=1
pk = ρRu T
n∑
k=1
Yk
Mwk
(14)
where pk is the partial pressure of the kth component of the gaseous mixture. The temperature (T) of the gaseous phase is 
obtained by solving the following equation for speciﬁc total energy (E) of the system using the Newton-Raphson method:
E(T) =
n∑
k=1
[
Yk
(
hf,k +
T∫
To
Cp,k(τ)dτ
)
− Ru
Mwk
T
]
+ u2 + v2 + w2
2 (15)
2.1.2. The EOS in the liquid phase
The Tait EOS in the following form is used to obtain p in the liquid phase:
p = B
[( ρ
ρ0
) N
− 1
]
+ A (16)
where, A, B, N and ρ0 are physical constants and depend on the material [49,57]. The values of physical constants used in 
this work for water and liquid aluminum are shown in Table 1:
Table 1
Values of the physical parameters in the Tait EOS for water and liquid aluminum.
Material A (Pa) B (Pa) N ρ0 (kg/m3)
Water 105 3.0 ×108 7.0 1000.0
Liquid Aluminum 105 3.36 ×109 8.55 2003.0
The speciﬁc total energy (E) is related to T through the following equation [49]:
E = Eref + Cv(T − Tref) + u2 + v2 + w2
2 (17)
where, Eref and Tref are the reference speciﬁc total energy and temperature of the liquid. Eref is calibrated at Tref =373 K
for water and Tref =2743.0Kf o r liquid aluminum in this work.
Eq. (1)–(3)a r e solved independently for the gaseous and liquid phases in the computational domain. The two phases 
are coupled at the sharp interface using a modiﬁed RS-GFM. The numerical methods adopted to solve the above governing 
equations are discussed in the following subsection.

<!-- PDF_PAGE: 6 -->

6 P. Das, H.S. Udaykumar / Journal of Computational Physics 405 (2020) 109005
2.2. Numerical schemes
As in Houim et al. [49], an operator splitting algorithm is used to perform time integration of the governing equations, 
Eq. (1)–(3). The hyperbolic terms in the governing equations are ﬁrst integrated using a third-order Runge-Kutta (TVD-RK) 
scheme [67]t o obtain an intermediate solution state U∗ at the nth timestep:
U∗ = H/Delta1t (
Un)
(18)
where Un is the solution state at the end of the nth time-step. H/Delta1t( ) is the linearized hyperbolic operator. The parabolic 
terms in the governing equations are integrated using the Runge-Kutta-Chebyshev (RKC) explicit time integration scheme 
[49,68]t o obtain a second intermediate state U∗∗ from U∗:
U∗∗= P/Delta1t (
U∗)
(19)
where P/Delta1t( ) is the parabolic operator. Finally, the source terms are integrated using 4th order Runge-Kutta-Fehlberg scheme 
to obtain the solution at the n +1th time step:
Un+1 = S/Delta1t (
U∗∗)
(20)
The time-step size /Delta1t is dependent on the hyperbolic operator and obtained from the CFL number:
/Delta1t =CFL
[ /Delta1x
u + a
]
min
, where CFL≤ 1, /Delta1xis grid size anda is the wave speed (21)
A 3rd order accurate ENO-LLF [69]s c h e m e is used for spatial discretization of the hyperbolic terms in the governing 
equations. A 4th-order accurate ﬁnite difference scheme [70]i s used to discretize the parabolic terms.
2.3. Interface tracking using levelsets
The levelset method [23,24]i s used in this work to deﬁne the interface between the gaseous and the liquid phases. The 
zero levelset contour deﬁnes the location of the sharp interface between the liquid and the gaseous phases. A narrow-band 
levelset ﬁeld provides the signed normal distance to the nominal interface from any point in a band around the sharp 
interface. The levelset ﬁeld is advected to capture the evolution of the interface as the ﬂow evolves in time:
∂φ
∂t + un ·∇φ =0 (22)
where φ represents the levelset ﬁeld. un is the local velocity of the interface. un is computed from the following equation:
un =− ˙m′′
ρl
n + ul (23)
where ul is the velocity of the liquid phase at the interface, n is the local unit vector normal to the interface and ρl is the 
local density of the liquid.
The levelset ﬁeld is advected at the end of each ﬂow timestep to capture the evolution of the gas-liquid interface. 
The 3rd-order TVD-Runge-Kutta method is used to perform time integration. The 5th-order WENO scheme [52]i s used 
for spatial discretization of Eq. (22). The high-order discretization scheme maintains the accuracy of the levelset advection 
and mitigates the mass-conservation error caused by numerical diffusion. The levelset ﬁeld is reinitialized [71]e v e r y ﬁve 
timesteps to ensure that it remains a signed distance function. The liquid and the gaseous phases separated by the zero 
levelset contours are coupled using a modiﬁed RS-GFM approach, which is described next.
2.4. The ghost ﬂuid method
A modiﬁed RS-GFM approach is developed to couple the gaseous and liquid phases at the surface of the vaporizing 
droplet. The jump conditions at the evaporating gas-liquid interface are given by:
[un]= ˙m′′
[1
ρ
]
(24)
[p]=− γκ− ˙m′′[un]−[ τnn] (25)
[τns]=− dγ
ds (26)
[˙q′′
cond
]
=− ˙m′′[h]+[ τnnun]+[ τnsus] (27)
where the operator [] represents:

<!-- PDF_PAGE: 7 -->

P. Das, H.S. Udaykumar / Journal of Computational Physics 405 (2020) 109005 7
Fig. 2. Categorization of the computational cells with respect to the gaseous phase. (For interpretation of the colors in the ﬁgure(s), the reader is referred 
to the web version of this article.)
[χ]= χg − χl
χ is any ﬂow variable of interest. The subscripts g and l represent the ﬂow variables at the interface in the gaseous and the 
liquid phase respectively. The subscripts n and s represent the directions normal and tangential to the interface. γ is the 
local surface tension at the gas-liquid interface. κ is the local curvature at the interface and is calculated from the levelset 
ﬁeld [71]u s i n g the following equation:
κ=∇ ·
( ∇φ
|∇φ|
)
(28)
Eq. (24) accounts for the jump in the normal velocity of the two phases at the interface caused by vaporization. The 
pressure jump in Eq. (25)a t the interface is due to surface-tension (−γκ), vaporization ( ˙m′′[un]) and jump in the normal 
component of viscous stress (τnn). The jump in the tangential components of the deviatoric stress tensor ([τns]) in the 
Eq. (26)r e p r e s e n t s the effect of Marangoni stresses at the interface. The jump in the heat ﬂux ([˙q′′
cond]) is given by Eq. (27). 
It accounts for the latent heat of evaporation ( ˙m[h]) and the work done by the viscous stresses ([τnn un], [τnsus]).
The jump-conditions are imposed through the RS-GFM. In implementing the current RS-GFM, the computational cells 
are categorized into four different types: the bulk points, the interfacial points, the interfacial ghost points and the interior 
ghost points [41]. Fig. 2 shows the categorization of the computational cells with respect to the gaseous phase. The ﬂow 
variables at the interfacial ghost points are obtained such that Eq. (24)–(27)a r e satisﬁed. Eq. (24)–(27)c a n be solved 
simultaneously to populate the ﬂow variables at the interfacial ghost points for each phase. However, solving Eq. (24), (25)
and (26) simultaneously in conjunction with an interfacial Riemann problem is computationally expensive. To avoid this 
problem, the interfacial jump conditions are decoupled and solved separately during the hyperbolic step and the parabolic 
step within an overall single ﬂow time-step. The methods adopted to obtain the ghost values for the hyperbolic and the 
parabolic steps are described in the following two sub-sections.
2.4.1. Treatment of interface for hyperbolic terms
The values of p, ρ and un at the ghost points (in each phase) are required by the solver during the hyperbolic step. An 
interfacial Riemann problem is solved to obtain p, ρ and un at the interfacial ghost points. The RS-GFM ensures that the 
characteristic waves are transmitted accurately across the interface from one phase to the other [57]. Previously, Sambasivan 
et al. [41]p r e s e n t e d an algorithm for constructing local 1-D Riemann problems normal to the interface to populate the 
ghost ﬂuid region for inviscid shock-droplet interaction simulations in 2D. In the current work, we extend the algorithm to 
incorporate the effects of surface-tension [72] and vaporization [49]a t the interface.
The numerical methods for obtaining the initial conditions for the local interface-normal 1-D Riemann problem is 
presented in Appendix A. The numerical algorithm in Appendix A is used to probe the ﬂow variables in the gaseous 
(ρg, un,g, pg) and the liquid (ρl, un,l, pl) phases at 1.5/Delta1x away from the interface along the interface-normal direction. 
(ρg, un,g, pg) and (ρl, un,l, pl) are used as the initial conditions for the interfacial Riemann problem.
The interfacial Riemann problem incorporates the jump conditions in normal velocity and pressure given by the following 
equations respectively:

<!-- PDF_PAGE: 8 -->

8 P. Das, H.S. Udaykumar / Journal of Computational Physics 405 (2020) 109005
[
u∗
n
]
= u∗
n,g − u∗
n,l = ˙m′′
[1
ρ
]
(29)
[
p∗]
= p∗
g − p∗
l =− γκ− ˙m′′[un] (30)
The form of the interfacial Riemann problem is similar to [49] and discussed in Appendix B. The interfacial Riemann 
problem is solved to obtain the intermediate (∗) states for the gaseous (ρ∗
g , u∗
n,g, p∗
g) and the liquid (ρ∗
l , u∗
n,l, p∗
l ) phases at 
every ghost point. ρ∗
g, u∗
n,g and p∗
g are used as the ghost values at the interfacial ghost points with respect to the gaseous 
phase. Similarly, ρ∗
l , u∗
n,l and p∗
l are used as ghost values at the interfacial ghost points with respect to the liquid phase. 
These ghost values for density, velocity, and pressure at the interfacial ghost points are extrapolated to the interior ghost 
points using a PDE-based multidimensional extrapolation approach [73].
2.4.2. The GFM for the parabolic terms
The velocity, temperature, and species mass fraction values in the ghost ﬂuid region are computed separately to couple 
the contributions from the parabolic terms in the governing equations at the interface. The numerical method for obtaining 
the ghost values during the parabolic step is described in a 2D scenario in the following subsection. Extension to 3D follows 
along similar lines in a dimension-by-dimension approach.
Calculation of the velocity ﬁeld in the ghost ﬂuid region
The velocity ﬁeld in the ghost-ﬂuid region is computed such that the following equations are satisﬁed:
[τnn]= 0 (31)
[τns]=− dγ
ds (32)
The numerical method adopted to impose these stress jump conditions at the interface is described below.
Fig. 3 illus trates  the arrangement of signiﬁcant points in the region near the interface that is used to calculate the value 
of the velocity at a typical ghost point IG. The ghost values of the velocity at IG are obtained by solving Eq. (31) and (32),
which can be written in the following forms:
[τnn]=
[
2μ∂un
∂n − 2
3μ
( ∂un
∂n + ∂us
∂s
)]
=0 (33)
[τns]=
[
μ
( ∂us
∂n + ∂un
∂s
)]
=− dγ
ds (34)
where un and us are the components of velocities along the normal and the tangential direction of the interface. un and us
are obtained by rotating the local velocity ﬁeld using the following equation:
(
un
us
)
=
[
nx ny
ny −nx
](
u
v
)
(35)
where nx and ny are the x and y components of n, respectively.
The derivatives of the un and us are estimated from the ﬂow-ﬁelds  near the interface. To estimate the derivatives of un
and us along n and s, a local Cartesian coordinate system along the local normal to the interface is erected at the normal 
projection of the point IG on the interface. The normal projection of the point IG on the interface, the point I in Fig. 3, is 
obtained from the following equation:
XI = XIG − φIGnIG (36)
where φIG is the magnitude of the levelset ﬁeld at the point IG and nIG is the unit vector normal to the interface computed 
at IG from the levelset ﬁeld [23]. XI and XIG are the locations of the points I and IG, respectively. Following this, two probes, 
G and L, are inserted in the gaseous and the liquid phases respectively. The probes are /Delta1n away from the point I on the 
interface. The locations of the probes are given by the following equations:
XG = XI + /Delta1nnIG (37)
XL = XI − /Delta1nnIG (38)
where XG and XL are the positions of the ends of the probes G and L respectively. A convex hull is formed around G and L
using neighboring grid points in the vicinity, as shown in Fig. 3. The velocity values at the points G and L are interpolated 
from the grid points forming the convex hull using bilinear interpolation [51].
The probe inserted in each phase must be at a suﬃcient distance away from the interface so that the convex-hull for the 
bilinear interpolation consists of bulk points only and does not contain any ghost point. This can be ensured by choosing /Delta1n
such that the interface does not fall inside the convex hull for the bilinear interpolation. The maximum distance between

<!-- PDF_PAGE: 9 -->

P. Das, H.S. Udaykumar / Journal of Computational Physics 405 (2020) 109005 9
Fig. 3. Schematic diagram of the numerical algorithm to calculate the velocity components at the ghost points.
two points in a convex hull formed with four neighboring grid points in Fig. 3 is the diagonal length of the convex hull, √
2/Delta1x. Therefore, choosing /Delta1n =1.5/Delta1x ensures that the convex-hull consists of the bulk points only.
The derivatives of un and us along n are estimated as:
∂un
∂n
⏐⏐⏐⏐
g
= un,G − un,I,g
/Delta1n (39)
∂un
∂n
⏐
⏐⏐⏐
l
=− un,L − un,I,l
/Delta1n (40)
∂us
∂n
⏐⏐⏐⏐
g
= us,G − us,I,g
/Delta1n (41)
∂us
∂n
⏐⏐
⏐⏐
l
=− us,L − us,I,l
/Delta1n (42)
where un,G and us,G are the velocity components along n and s at the point G. un,L and us,L are the velocity components 
along n and s at the point L. un,I,g and us,I,g are the velocity components of the gaseous phase along n and s at the point 
I. un,I,l and us,I,l are the velocity components of the liquid phase along n and s at the point I.
To estimate the gradients of un and us along s, the velocity ﬁelds are probed at two points, to the right and left of G
and L, perpendicular to the lines IG and IL respectively, as shown in Fig. 3. The points to the right and the left of G are 
labeled Gr and Gl respectively, and, points to the right and the left of L are Lr and Ll respectively. The coordinates of Gr, 
Gl, Lr and Ll are obtained from:
XGr = XG + /Delta1s
2 sIG (43)
XGl = XG − /Delta1s
2 sIG (44)
XLr = XL + /Delta1s
2 sIG (45)
XLl = XL − /Delta1s
2 sIG (46)
where sIG is the unit vector along the tangent to the interface at IG and /Delta1s
2 is the distance of Ll and Lr from L and Gl
and Gr from G. /Delta1s =1.5/Delta1x is selected in the current work. The velocity at Gr (un,Gr, us,Gr), Gl (un,Gl, us,Gl), Lr (un,Lr, us,Lr)
and Ll (un,Ll, us,Ll) are obtained from bilinear interpolation of the velocity ﬁeld from the four nearest grid points. With the

<!-- PDF_PAGE: 10 -->

10 P. Das, H.S. Udaykumar / Journal of Computational Physics 405 (2020) 109005
values of un and us available at these four points, the gradients of un and us along the s direction are estimated using the 
following equations:
∂un
∂s
⏐⏐⏐
⏐
g
= un,Gr − un,Gl
/Delta1s (47)
∂us
∂s
⏐⏐⏐⏐
g
= us,Gr − us,Gl
/Delta1s (48)
∂un
∂s
⏐⏐⏐⏐
l
= un,Lr − un,Ll
/Delta1s (49)
∂us
∂s
⏐⏐⏐⏐
l
= us,Lr − us,Ll
/Delta1s (50)
The unknown quantities in Eq. (33)–(50)a r e the velocity components at the interface, un,I,g, us,I,g, un,I,l and us,I,l. The 
derivatives computed using Eq. (39)–(42) and Eq. (47)–(50)a r e substituted in Eq. (33) and Eq. (34). Now, we have two 
equations for the four unknown variables. The other two equations required to close the system are obtained from the jump 
conditions of the normal and tangential components of velocity at the interface, i.e.:
un,I,g − un,I,l =[ un,I]= ˙m′′
[1
ρ
]
(51)
us,I,g − us,I,l =[ us,I] (52)
Eq. (51)r e p r e s e n t s the regression of the interface caused by vaporization and Eq. (52)r e p r e s e n t the slip in the tangential 
velocity of the two phases at the interface. In the current work, a no-slip condition is assumed at the interface, i.e. [us,I] =0.
Eq. (33) and  (51)a r e solved to obtain un,I,g and un,I,l:
un,I,g = β+ μl[un,I]
μg + μl
(53)
un,I,l = un,I,g −[ un,I] (54)
where,
β = (μgun,G + μlun,L) − 3
4/Delta1nα
α= 2
3μg
∂us
∂s
⏐⏐⏐⏐
g
− 2
3μl
∂us
∂s
⏐
⏐⏐⏐
l
μg and μl are the viscosities of the gaseous and the liquid phase, respectively.
Similarly, Eq. (39) and (52)a r e solved to obtain us,I,g and us,I,l:
us,I,g = δ+ μl[us,I]
μg + μl
(55)
us,I,l = us,I,g −[ us,I] (56)
where,
δ= (μgus,L + μlus,L) − /Delta1nη
η=− dγ
ds − μg
∂un
∂s
⏐⏐⏐⏐
g
+ μl
∂un
∂s
⏐
⏐⏐⏐
l
The ghost values of the velocity components at IG ( un,IG
⏐⏐
ghost , us,IG
⏐
⏐
ghost) are extrapolated from the velocity of the 
gaseous phase at the interface and the point G, so that:
un,IG
⏐⏐
ghost = un,I,g(φIG + /Delta1n) − φIGun,G
/Delta1n (57)
us,IG
⏐⏐
ghost = us,I,g(φIG + /Delta1n) − φIGus,G
/Delta1n (58)
The ghost value of the velocity components at IG along the co-ordinate directions (uIG|ghost, vIG|ghost) are obtained from:
(
uIG|ghost
vIG|ghost
)
=
[ −nx −ny
−ny nx
] (
un,IG
⏐⏐
ghost
us,IG
⏐
⏐
ghost
)
(59)

<!-- PDF_PAGE: 11 -->

P. Das, H.S. Udaykumar / Journal of Computational Physics 405 (2020) 109005 11
Calculation of the temperature ﬁeld in the ghost ﬂuid region
The ghost value for the temperature at IG is calculated such that the jump condition in the heat ﬂux given by Eq. (27)i s 
satisﬁed. The jump in heat-ﬂux between the gaseous and the liquid phase is cast in the following form:
−kg
∂T
∂n
⏐⏐⏐⏐
g
+ kl
∂T
∂n
⏐
⏐⏐⏐
l
=
[˙q′′
cond
]
(60)
where kg and kl are the thermal conductivity of the gas and the liquid respectively at the interface. (∂T
∂n )g and (∂T
∂n )l are the 
thermal gradients in the gaseous and the liquid phase at the interface, in the direction normal to the interface. For a typical 
ghost point IG, shown in Fig. 3, (∂T
∂n )g and (∂T
∂n )l are estimated from the following relations:
∂T
∂n
⏐
⏐⏐
⏐
g
= TG − TI,g
/Delta1n (61)
∂T
∂n
⏐
⏐⏐⏐
l
=− TL − TI,l
/Delta1n (62)
where, TG and TL are the temperature at the points G and L in Fig. 3. Similar to the velocity components, TG and TL are 
estimated from the temperature at the nearest four grid points using bilinear interpolation. TI,g and TI,l are the temperature 
of the gaseous and liquid phases respectively, at the interface. The jump in temperature at the interface is given by:
TI,g − TI,l =[ TI] (63)
In this work, the temperature is assumed to be continuous at the interface. Therefore, [TI] =0.
Eq. (61) and  (62)a r e substituted in Eq. (60)t o obtain:
−kg
TG − TI,g
/Delta1n − kl
TL − TI,l
/Delta1n =
[˙q′′
cond
]
(64)
Eq. (63) and (64)a r e solved to obtain TI,g and TI,l as given below:
TI,g =
kg TG + kl TL + kl[TI]+ /Delta1n[˙q′′
cond]
kg + kl
(65)
TI,l =
kg TG + kl TL − kg[TI]+ /Delta1n[˙q′′
cond]
kg + kl
(66)
Once TI,g and TI,l are obtained, the ghost value of the temperature at IG, TG|ghost, is obtained by linear extrapolation:
TIG|ghost = TI,g(φIG + /Delta1n) − φIG TG
/Delta1n (67)
Calculation of the species mass fraction in the ghost ﬂuid region
In the current work, only two non-reacting species are present in the gaseous phase. The liquid phase is treated as a 
pure material. Therefore, boundary conditions for the Yk are required only in the gas phase. Since, Yk has zero gradient at 
the interface along the interface-normal direction, the boundary condition for Yk at the interface is speciﬁed by:
∂Yk
∂n =0 (68)
The boundary condition is applied for the Yk at the interface using the GFM. The ghost values of Yk are obtained by 
extrapolating Yk from the interfacial cells to the ghost region. A PDE-based multidimensional extension algorithm [73]i s 
used to extrapolate the Yk from the interfacial points in the gaseous phase into the ghost points across the interface.
In summary, the above LS-SIM method in conjunction with the RS-GFM constitutes the numerical implementation of the 
interfacial mechanics of vaporizing gas-liquid interfaces. It is worth mentioning that the current method differs from the 
GFM in [49]i n several aspects.
The current implementation of the Riemann solver based GFM ensures that the 1-D Riemann problems constructed 
to populate the ghost points are along the normal direction of the interface. Unique interface-normal Riemann problems 
are constructed at each of the ghost points adjacent to the interface. Whereas, in [45], the interfacial Riemann problems 
constructed to populate the ghost points are not along the interface-normal direction. The initial conditions for the interfa-
cial Riemann problem are obtained from two neighboring computational cells adjacent to the interface in [49]. This leads 
to further ambiguity as multiple Riemann problems can be constructed at a ghost point which has multiple neighboring 
computational cells on the other side of the interface. Under such circumstances, a weighted average of the solutions of 
the multiple Riemann problems was used in [49]. The current implementation circumvents such ambiguity by constructing 
unique interface-normal Riemann problems at every ghost point adjacent to the interface.

<!-- PDF_PAGE: 12 -->

12 P. Das, H.S. Udaykumar / Journal of Computational Physics 405 (2020) 109005
Fig. 4. A ﬂow-chart of the current sharp-interface framework demonstrating the ﬂow of information through the different modules of the sharp-interface 
framework described in Section 2.
The numerical algorithm for solving Eq. (24)–(27)i s also different from [49]. In the current method, the jump in the 
viscous stresses at the interface is imposed through the RS-GFM by calculating un,IG|ghost and us,IG|ghost explicitly from 
Eq. (57) and (58). On the contrary, in Houim and Kuo [49], the jump in the viscous stresses at the interface is imposed by 
solving a set of four simultaneous equations in 2D and six simultaneous equations in 3D to obtain un,IG|ghost and us,IG|ghost. 
The current numerical algorithm makes the treatment at the interface computationally eﬃcient. Furthermore, Houim et al. 
[49]f o u n d that rotating the stress tensor on a ﬁne grid leads to numerical instabilities. In the current RS-GFM, instead of 
the stress tensor, the velocity ﬁeld is rotated from the Cartesian coordinate to an interface-normal coordinate system. This 
approach resolves the issue of the numerical instability on a ﬁner grid originating from the rotation of the stress tensor.
A sharp-interface method for computing vaporization of droplets in shocked ﬂows is presented in this section. A ﬂow-
chart of the current method is shown in Fig. 4 to describe how the different components of the algorithm such as the 
levelset based interface tracking, the time integration schemes, the spatial discretization schemes, and the GFM are as-
sembled together under the umbrella of a massively parallelized framework to solve the problem. The current method is 
validated against experimental measurements, veriﬁed against exact solutions and several benchmark numerical results in 
the sections below. The capabilities of the current sharp-interface method are demonstrated in the results section by solving 
problems involving shock interaction with liquid-gas interfaces in 2D and 3D.
3. Results and discussion
The above numerical framework is validated by comparing the results with several benchmark experimental and numer-
ical solutions to problems involving shock interactions with gas-liquid interfaces.
3.1. 1D air-water shock-tube problem
First, the solution obtained from the ﬂow solver is compared with the exact solution of the Riemann problem to validate 
the implementation of the hyperbolic equation solver and the interface capturing scheme. Fig. 5 shows a schematic of

<!-- PDF_PAGE: 13 -->

P. Das, H.S. Udaykumar / Journal of Computational Physics 405 (2020) 109005 13
Fig. 5. The initial conditions for the 1D air-water shock tube problem.
the initial setup for this study. The length of the shock tube is 1.0 m. Initially, the air-water interface is at x = 0.5m . 
Low-pressure air at 105 Pa is on the left of the interface and high-pressure water at 107 Pa is on the right. The contact 
discontinuity at the air-water interface is tracked using the current sharp-interface method. As the system evolves with 
time, a shock wave will propagate through air, a strong rarefaction wave will propagate through water and the interface will 
move towards the left.
Fig. 6 sho ws  the solution state at 0.2 ms after releasing the system from the initial condition. Fig. 6(a), (b) and (c) show 
the pressure, density and velocity distribution respectively across the length of the shock tube. Results obtained from four 
different grid resolutions corresponding to the grid sizes of 5 mm, 2.5 mm, 1.25 mm and 0.625 mm are shown in Fig. 6. 
The results obtained from the simulations are compared with the exact solution of the Riemann problem [74].
Fig. 6 sho ws  that the solution state predicted by the current solver agrees well with the exact solution. The location 
of the shock wave in air at x =0.425 m and the location of the rarefaction wave in water at x =0.795 m are predicted 
accurately by the current solver. The density distribution in Fig. 6(b) shows that the location of the contact discontinuity at 
the gas-liquid interface is accurately predicted by the LS-SIM coupled with the RS-GFM. The smearing of the solution near 
the shock wave and the rarefaction wave due to numerical diffusion is seen in the results obtained from the coarse mesh 
simulations. However, the thickness of the shock and the rarefaction wave decreases as the grid resolution is increased. The 
results obtained from the current method converge to the exact solution as the resolution of the simulation is increased.
The results obtained from the 1D air-water shock tube problem show that the current solver predicts wave propagation 
through the gaseous and the liquid medium accurately. The results also show that accurate coupling of the ﬂow variables 
in the gas and the liquid phase at the interface is achieved using RS-GFM.
3.2. Mach 2.4 shock interaction with a cylindrical droplet
The current approach is validated against experimental results for a Mach 2.4 shock interaction with a cylindrical water 
droplet in [75]. Fig. 7 shows the initial setup for the 2D simulation of shock-droplet interaction. Neumann boundary condi-
tion is used at the east boundary of the computational domain. A reﬂective boundary condition is used at the west, north, 
and the south domain boundaries. The diameter of the droplet is 22 mm, which is the reference length-scale of the prob-
lem. The grid resolution used in this study corresponds to 400 grid points across the diameter of the droplet. The numerical 
calculations are initiated with a strip of a high-pressure region in the upstream of the droplet to match the characteristics 
of the Mach 2.4 blast-wave interacting with the droplet. The following initial conditions similar to the benchmark study 
[75]a r e used in this simulation (Table 2):
Table 2
Initial conditions for the simulation of Mach 2.4 shock interaction with a cylindrical water 
column.
ρ(kg/m3) p (MPa) u (m/s)
Air ( 3
44 ≥ X
D ≥ 5
44 ) 1.17 0.101 0.0
Air ( 3
44 ≤ X
D ≤ 5
44 ) 580.75 0 0 .0
Water droplet 1000.0 101000.00 .0
ReD of the post-shock ﬂow is 2.75 ×106 and WeD is 3.8 ×105. The high ReD and WeD of the ﬂow suggests that the 
effects of viscous and surface tension forces are negligible in comparison with the inertia forces in this case. Furthermore, 
this study focuses on the initial stages of the shock-droplet interaction, when the droplet is still undeformed. Therefore, an 
inviscid calculation without the effect of surface tension is performed in this study.

<!-- PDF_PAGE: 14 -->

14 P. Das, H.S. Udaykumar / Journal of Computational Physics 405 (2020) 109005
Fig. 6. Comparison of the (a) pressure (b) density and (c) velocity obtained from the exact solution and the simulation result of the air-water shock tube 
problem after 200 μs.
Fig. 7. The initial condition for 2D simulation of Mach 2.4 shock interaction with a water column of 22 mm in diameter.

<!-- PDF_PAGE: 15 -->

P. Das, H.S. Udaykumar / Journal of Computational Physics 405 (2020) 109005 15
Fig. 8. The evolution of the shock and the rarefaction waves during the Mach 2.4 shock interaction with a cylindrical water droplet of 22 mm in diameter. 
The upper half of the images (a)–(f) represent the experimentally obtained Schlieren images [75]a n d the bottom halves are the numerical Schlieren images 
obtained from the current simulations.
Fig. 8 shows the comparison between the numerical Schlieren obtained from the current simulations and the experimen-
tal results [75]a t six different stages of shock-droplet interaction. The corresponding pressure contours are plotted in Fig. 9
to explicitly show the compression and the rarefaction regions within the droplet at the different stages. Fig. 8 (a) shows 
the reﬂected and transmitted shock waves shortly after the incident shock wave has impacted the gas-liquid interface. The 
locations of the incident, reﬂected, and transmitted shock waves are accurately predicted in the current numerical study. 
The transmitted shock wave travels faster in the liquid medium than the incident shock wave in the air. Fig. 8(b) shows that 
the transmitted shock wave reaches the liquid-gas interface at the leeward side of the droplet before the incident shock 
wave has traveled across the droplet. The transmitted shock wave reﬂects back from the liquid-gas interface into the liquid 
medium as a strong rarefaction wave, as seen in Fig. 8 (c). A similar shape of the rarefaction wave is seen in the experi-
mentally and the numerically obtained Schlieren images in Fig. 8 (c). Fig. 9(c) shows the absolute pressure in the rarefaction 
zone drops down to approximately −5bar. Such low pressure in the droplet was also observed in the previous experimental 
and numerical study [75]. As the rarefaction wave within the droplet travels toward the front, it eventually interacts with 
the gas-liquid interface at the front edge of the water droplet. The pressure contours in Fig. 9(d) shows that the rarefaction 
wave in the water droplet reﬂects back as a compression wave from the interface. The comparison of the experimentally 
and numerically obtained Schlieren images in Fig. 8(d) shows that the location and the structure of the compression and the 
rarefaction waves within the droplet are predicted accurately using the current sharp-interface method. As time progresses, 
the transmitted wave keeps reﬂecting back and forth within the droplet. Each time the transmitted shock wave interacts 
with the interface, some part of its energy is transmitted across the interface and the rest is reﬂected into the liquid phase. 
Therefore, the transmitted wave, trapped inside the droplet, loses energy each time it reﬂects into the liquid region from 
the interface. The weakening of the waves within the droplet is seen in the Schlieren images and the pressure contours in 
Fig. 8 and Fig. 9, respectively. The experimental and the numerical Schlieren images in Fig. 8(e) and (f) show that the wave 
structures within the droplet are signiﬁcantly weaker than the snapshots taken at earlier times. Nonetheless, the compari-
son with the experimental study [75]d e m o n s t r a t e s that the current sharp-interface method captures the interactions of the 
non-linear waves with the gas-liquid interface accurately.
This simulation of Mach 2.4 shock interaction with a water droplet shows the wave interactions with the gas-liquid in-
terface during the initial period of the shock-droplet interaction, a scenario in which inertia dominates viscous and capillary 
forces. From the comparisons of the location of the wave structures in Fig. 8 and the smooth transition of the pressure ﬁeld 
across the interface in Fig. 9, it is inferred that the current RS-GFM couples the ﬂow-ﬁelds  across the interface accurately. 
Signiﬁcant deformation of the droplet is not observed in this problem and the ﬂow structures are dominated by shocks and

<!-- PDF_PAGE: 16 -->

16 P. Das, H.S. Udaykumar / Journal of Computational Physics 405 (2020) 109005
Fig. 9. The evolution of the pressure ﬁeld during the Mach 2.4 shock interaction with a cylindrical water droplet of 22 mm in diameter. In the above plots 
the reference pressure, pref =101000.0P a .
Fig. 10. The initial condition for 2D simulation of Mach 1.47 shock interaction with a water column of 4.8 mm in diameter.
rarefactions. The long-term evolution of the gas-liquid interface in shock-droplet interaction and the effect of the surface 
tension on the shape of the droplet is studied next.
3.3. Mach 1.47 shock interaction with a cylindrical droplet
Interface tracking through LS-SIM is veriﬁed by comparing current results with a benchmark study [16]. The evolution 
of the shape of a cylindrical water droplet during the interaction with a Mach 1.47 shock wave is computed and compared 
with the benchmark result [16]. Furthermore, the effect of capillary forces on the droplet shape is studied by comparing the 
results obtained with and without surface tension.
Fig. 10 shows the initial setup for the simulations of a Mach 1.47 shock interaction with a cylindrical droplet of diameter 
D = 4.8 mm. A Neumann boundary condition is used at the four boundaries of the computational domain. Initially, the 
shock is located at x
D =9.5. The initial conditions for the simulation are given in Table 3.
Inviscid simulations are performed to compare the results with the benchmark study [16]. The effect of surface tension 
on the shock-induced deformation of the cylindrical droplet is studied by comparing the results of the simulations with and 
without surface tension. To investigate the stability of the current method, a low Weber number (We) of 10.0 is used in the 
simulation with surface tension.
The drag-coeﬃcient (CD) of the cylindrical droplet, computed from the current simulation, is compared with the bench-
mark study [16]i n Fig. 11. CD is computed as:

<!-- PDF_PAGE: 17 -->

P. Das, H.S. Udaykumar / Journal of Computational Physics 405 (2020) 109005 17
Table 3
Initial conditions for Mach 1.47 shock interaction with a cylindrical water droplet.
ρ(kg/m3) p (Pa) u (m/s)
Pre-shocked air ( X
D ≥ 9.5) 1.0 101000.00 .0
Post-shocked air ( X
D <9.5) 1.81 237792.72 247.47
Droplet 1000 .0 101000.00 0.0
Fig. 11. C D of the cylindrical droplet of 4.8 mm diameter during interaction with the Mach 1.47 shock plotted against nondimensional time.
CD = F
0.5ρpsu2
ps D (69)
where F is the total drag force acting on the droplet [70]. ρps and ups are the density and the velocity of the post-shocked 
air. In Fig. 11, CD is plotted against the nondimensionalized t∗ given by:
t∗ = tus
D (70)
where t is the simulation time in seconds and us is the speed at which the shock-wave is traveling.
Four different grid resolutions corresponding to 50, 100, 200 and 400 grid points across the diameter of the droplet 
is used in this simulation. Fig. 11 shows that the CD calculated using the current method is in good agreement with 
the benchmark result [16]. The comparison of CD indicates that the pressure distribution around the droplet obtained in 
the current calculations agree with the benchmark study [16]. Furthermore, Fig. 11 shows that the CD computed using the 
current sharp-interface framework converge with grid reﬁnement. The CD computed from the grid resolutions corresponding 
to 200 and 400 grid-points per droplet diameter are marginally different. The grid-resolution of 200 grid-points are used in 
results shown in this section.
The shocks and the rarefaction waves in and around the water droplet during the early stages (t∗ = 0.63 to 1.47) of 
the interaction with the incident Mach 1.47 shock are demonstrated in Fig. 12. The numerical Schlierens obtained in the 
benchmark [16] and the current study are vertically juxtaposed in Fig. 12 to provide a thorough comparison of the ﬂow-ﬁeld.  
The key features of the ﬂow-ﬁeld,  such as the locations of the transmitted and the reﬂected shocks in Fig. 12(a) and the 
rarefaction wave within the droplet in Fig. 12(b) obtained in the current study match closely with [16]. Fig. 12 (c) and (d) 
demonstrate the locations of the shock and rarefaction waves in the gas and the liquid phases predicted by the current 
method agree well with the benchmark results in [16].
As the solution progress, the droplet deforms due to the impact of the incident shock and a recirculation region develops 
in the wake of the droplet. The deformation of the droplet and the evolution of the ﬂow-ﬁeld  near the droplet is shown 
through a sequence of four numerically obtained Schlieren images in Fig. 13. The shock structures and the shapes of the 
droplet in the simulation without surface tension agree with the benchmark results shown in Fig. 13(a), (b), (c) and (d). 
Fig. 13(a) shows the location of the incident and reﬂected shocks and the shock triple point are similar in the current and 
the benchmark result [16]. The length and the shape of the wake predicted by the current method are also similar to the 
benchmark results [16]. Relatively sharper rendition of the shocks and acoustic waves are observed in the current study in 
comparison with the benchmark [16]r e s u l t s because of the higher resolution of the current calculation. Fig. 13(d) shows 
that the current high-resolution calculations have produced more intricate vortical structures in the wake of the droplet 
compared to the benchmark results [16].
The shape of the droplet obtained from the current calculation is compared with the benchmark result [16]i n Fig. 14. 
The comparisons in Fig. 14 (a) and (b) show that the shapes of the droplet predicted by the current method agree well with 
the benchmark results [16]d u r i n g the early stages of the shock-droplet interaction. However, the shapes of the droplet in 
the current result differ from the benchmark result [16]d u r i n g the later stages of the simulation, as shown in Fig. 14(c) 
and (d). Nevertheless, from the comparison presented in Fig. 14, it is reasonable to argue that similar droplet shapes are

<!-- PDF_PAGE: 18 -->

18 P. Das, H.S. Udaykumar / Journal of Computational Physics 405 (2020) 109005
Fig. 12. Comparison of the locations of the shock and the rarefaction waves around and within the water droplet of the 4.8 mm diameter during interaction 
with Ms =1.47 shock. The upper half of the numerical Schlieren plots shows the benchmark result [16]a n d the bottom half shows the current result.
produced by the levelset method used in the current study and the front-tracking method used in the benchmark study 
[16].
The results obtained from the simulation with surface tension demonstrate that the LS-SIM and RS-GFM produce a 
stable solution even at low Weber numbers. Large deformation of the droplet is captured without any numerical instability. 
The comparison of the results obtained from the simulations with and without surface tension in the middle and the 
right columns of Fig. 13 shows that the capillary effects result in a smoother droplet surface; capillarity suppresses high 
curvatures at the surface. The pressure difference caused by the surface tension effect at the interface acts as a smoother 
and damps instability at the interface. To quantify the effect of the surface tension on the deformed shape of the droplets, 
an effective mean diameter, Deff. is deﬁned. The Deff. is analogous to the deﬁnition of Sauter Mean Diameter for spherical 
droplets in 3D and is deﬁned as:
Deff. =
D2
A
DP
= 4 Ad
Pd
(71)
where DA and DP are the diameter of the cylinders with the same cross-sectional area and the same length of the cross-
sectional perimeter of the deformed cylindrical droplet, respectively. Ad is the instantaneous cross-sectional area and Pd is 
the cross-sectional perimeter of the deformed cylindrical droplet. Deff. is an “average diameter” of the deformed droplet. 
Deff. of a perfectly circular droplet is same as its diameter. As the droplet deforms, the Pd will increase, subsequently, Deff.
will decrease. Therefore, Deff. quantiﬁes the deformation of the droplet, where, lower Deff. indicates higher deformation of 
the droplet.

<!-- PDF_PAGE: 19 -->

P. Das, H.S. Udaykumar / Journal of Computational Physics 405 (2020) 109005 19
Fig. 13. Sequence of numerical Schlieren plots showing ﬂow ﬁeld around the water column during the interaction with a Mach 1.47 shock. The left column 
shows the results obtained by Terashima and Tryggvason [16]. The middle and the right columns show the results obtained from the current study without 
(We=0) and with the surface-tension effect (We=10).

<!-- PDF_PAGE: 20 -->

20 P. Das, H.S. Udaykumar / Journal of Computational Physics 405 (2020) 109005
Fig. 14. Comparison of the shapes of the cylindrical droplet of 4.8 mm diameter obtained from in the benchmark study [16]a n d the current results during 
interaction with a Mach 1.47 shock. The droplet interface obtained in the benchmark study [16]i s marked using (□) and the straight line denotes the 
shape of the droplet obtained from the current calculations.
Fig. 15. Comparison of the Deff. of the droplets computed from calculations of Mach 1.47 shock-droplet interaction with and without surface-tension.
The Deff. of the 4.8 mm droplets during the interaction with the Mach 1.47 shock for We = 0 and We  = 10.0a r e 
computed and plotted in Fig. 15 to quantify the effect of surface tension on the shape of the droplet. Fig. 15 shows that Deff. 
of the droplets remain close to 4.8 mm for We =0 and We =10.0t i l l t∗ ∼ 10.0. Later, Deff. decrease as the droplets start to 
deform. The capillarity effects on the shape of the droplet become noticeable as the droplet deforms under the inﬂuence of 
the shock-loading, as shown previously in Fig. 13. Fig. 15 shows that the Deff. is higher for We =10.0. Therefore, the effects 
of surface-tension resist the deformation of the droplet under shock-loading.

<!-- PDF_PAGE: 21 -->

P. Das, H.S. Udaykumar / Journal of Computational Physics 405 (2020) 109005 21
Fig. 16. The initial step for the axisymmetric simulation of Mach 2 shock induced evaporation of a heated aluminum droplet of 230 μm in diameter.
The results in the previous sections show that the RS-GFM successfully couples the ﬂow variables at the gas-liquid 
interface. The interface dynamics is also predicted accurately in the presence of surface tension. However, the simulations 
demonstrated in the previous sections are for inviscid non-evaporating cases. Viscous simulations of shock interaction with 
vaporizing droplets are presented next.
3.4. Axisymmetric calculation of shock interaction with a vaporizing droplet
In this section, the shock-induced vaporization rate of a droplet calculated using the current approach is compared with 
a previous study [49]. For this study, an axisymmetric calculation of Mach 2 shock interaction with an aluminum droplet of 
230 μm in diameter is performed (Fig. 16) and the droplet vaporization rate computed from the current study is compared 
with Houim et al. [49].
The initial setup for the simulation is shown in Fig. 16. Neumann boundary conditions are used at the east, west and 
north boundaries of the computational domain. An axisymmetric boundary condition is used at the south boundary of 
the computational domain. The droplet is initially located at x = 0.575 mm and the following initial conditions are used 
(Table 4):
Table 4
Initial conditions for the simulation of Mach 2 shock interaction with a liquid Aluminum droplet.
ρ(kg/m3) p (Pa) u (m/s) T (K)
Pre-shocked air (x ≥ 0.43 mm) 1.177 101325.00 .03 00.0
Post-shocked air (x <0.43 mm) 3.138 455962.47 433.95 507.19
Droplet 2003 .0 105916.81 0.0 2750.0
The grid resolution used in this simulation corresponds to 460 grid point across the diameter of the droplet.
The viscosity of air is calculated from Sutherland’s law given by:
μair =
μref( T
Tref
)
3
2 (Tref + S)
T +S (72)
where μref =1.813 ×10−5 Pa.s, Tref =293.0 K and S =110.4. kair is calculated from:
Pr = Cpμair
kair
=0.72
The material properties for liquid aluminum and the thermal and the transport properties of the aluminum vapor are 
identical to Houim et al. [49,76].
Fig. 17 sho ws a sequence of contours of the numerical Schlieren and aluminum vapor mass fraction, during the interac-
tion of a Mach 2 shock with the aluminum droplet. The simulation is initiated with a heated aluminum droplet immersed 
in a quiescent ﬂow. Fig. 17(a) shows that the droplet starts to vaporize as the calculations proceed and a layer of vaporized 
aluminum is accumulated around the droplet before the shock interacts with the droplet. Furthermore, the thermal con-
duction from the molten aluminum droplet suddenly increases the temperature of the air around the droplet. The sudden 
increase in temperature of the air surrounding the droplet creates the thermally-induced shock wave seen in Fig. 17(a). As 
the shock wave passes over the droplet, the layer of aluminum vapor surrounding the droplet is stripped off its surface. 
Fig. 17(b) and (c) show that the boundary layer detaches from the droplet surface and a recirculation region is formed in 
the wake as the ﬂow evolves. The aluminum vapor is advected downstream into the recirculation region in the wake. The 
shock diffraction patterns seen in the numerical Schlieren images in Fig. 17 are similar to the benchmark results [45]. The 
deformed shape of the droplet and the distribution of the aluminum vapor in Fig. 17(c) are also in agreement with the 
benchmark results [45].

<!-- PDF_PAGE: 22 -->

22 P. Das, H.S. Udaykumar / Journal of Computational Physics 405 (2020) 109005
Fig. 17. Sequence of numerical Schlieren and mass fraction of Al vapor during interaction of a Mach 2 shock wave with an aluminum droplet of 230 μm in 
diameter. The left column shows the numerical Schlieren and the right column shows the column shows the contours of YAl.
Fig. 18. A comparison of the velocity magnitude contour and the streamlines around the aluminum droplet (230 μm in diameter) interacting with a Mach 
2 shock wave at 1.75 μs between the benchmark result [45]a n d the current study.
A snapshot of the magnitude of the velocity ﬁeld, along with the stream-traces at t =1.75 μs obtained from the current 
result is compared with the benchmark result [49]i n Fig. 18. Fig. 18 shows that the boundary layer separates from the 
droplet surface at 81◦ above the axis measured at the droplet center. Two counter-rotating separation bubbles, SB 1 and 
SB 2, form between the detached boundary layer and the droplet surface immediately after ﬂow separation. A recirculation 
region (RR) forms in the wake of the droplet. These key features of the ﬂow ﬁeld obtained from the current calculations 
match with the benchmark results [45]. The boundary layer is found to separate from the droplet surface at a similar 
location as observed in the benchmark study [45]. The locations of SB1 and SB2 observed in the current result are also 
similar to the benchmark study [45]. The length of the recirculation region in the wake of the droplet seen in Fig. 18
matches with Houim et al. [45]. A quantitative comparison of these key ﬂow features are presented in the Table 5.
This comparison shows that the current RS-GFM predicts similar key features of the ﬂow-ﬁeld  as the GFM in the bench-
mark study [45].
The rate of vaporization ( ˙m) of the aluminum droplet computed using the current method is compared with the bench-
mark result [49]i n Fig. 19(a) and (b), respectively. Fig. 19 shows good agreement between the current and the benchmark

<!-- PDF_PAGE: 23 -->

P. Das, H.S. Udaykumar / Journal of Computational Physics 405 (2020) 109005 23
Table 5
Comparison of the primary ﬂow-features around the aluminum droplet of 230 μm in diameter at 1.75 μs after the interaction with the Mach 2 shock.
Benchmark result [45] Current result
Separation point
(measured in angle above the axis, measured at the center of the droplet)
80◦ 81◦
Center of SB 1 (coordinates in mm) 0.65, 0.11 0.64, 0.11
Center of SB 2 (coordinates in mm) 0 .67, 0.10 0.67, 0.09
Length of PR (length in mm) 0.21 0.2
Fig. 19. The vaporization rate of an Aluminum droplet of 230 μm in diameter during interaction with a Mach 2 shock wave. The current results are being 
compared with the benchmark results.
results [49]. However, Fig. 19(a) and (b) show that there is a small discrepancy between the current result and the bench-
mark study [49]a t the early stage (t =0–0.5μ s ) of shock-droplet interaction.
The discrepancy seen in Fig. 19 is because the initial conditions of the current and the benchmark study [49]a r e dif-
ferent. The simulation was initiated with a layer of heated vapor of aluminum around the droplet in the benchmark study 
[49]. However, speciﬁc quantities relevant to the initial distribution of the heated aluminum vapor around the droplet such 
as fin and fout in Eq. (53) of [76]w e r e not mentioned. To avoid any further ambiguity, the presence of heated aluminum 
vapor is not assumed in the current study. As a result, the rate of vaporization is higher during the early stages of shock-
droplet interaction in the current study than the benchmark results. The added aluminum-vapor-layer suppresses the rate 
of vaporization of the droplet in the benchmark study during the early stages. Nevertheless, once the aluminum-vapor over 
the droplet is stripped off the droplet surface by the high-speed ﬂow behind the shock wave, the initial aluminum-vapor 
layer does not inﬂuence the vaporization rate anymore. Therefore, the ˙m of the droplet computed in the current work agree 
well with the benchmark result at the later stages of the shock droplet interaction.
The validation study for the current numerical framework was presented thus far. In the following sections, the current 
method is used to study shock-induced vaporization of a droplet through 2D and 3D simulations.
3.5. 2D simulation of shock interaction with a vaporizing cylindrical droplet
Next, the shock-induced vaporization of a cylindrical droplet is studied. For this study, the interaction of a Mach 1.47 
shock wave with a cylindrical water droplet of 37 μm in diameter is simulated. The initial computational setup for the 
simulation is shown in Fig. 20. Reﬂective boundary condition is used at the north and the south boundaries of the compu-
tational domain. A Neumann boundary condition is used at the east and the west boundaries. The initial conditions for the 
simulation are as in Table 6:
Table 6
The
 initial conditions for the 2D simulation of shock interaction with a vaporizing droplet.
ρ(kg/m3) p (Pa) u (m/s) T (K)
Pre-shocked air ( X
D ≥ 9.0) 1.2 101000 0.0 293.0
Post-shocked air ( X
D <9.0) 2.17 237792.72 225.91 381.0
Droplet 997 .0 104193.05 0.0 373.0
The following material properties for water at 373 K are used in the simulation:
μwater =2.777 ×10−4 Pa.s

<!-- PDF_PAGE: 24 -->

24 P. Das, H.S. Udaykumar / Journal of Computational Physics 405 (2020) 109005
Fig. 20. The initial condition for 2D simulation of Mach 1.47 shock interaction with a water column of 37 μm in diameter.
Fig. 21. Grid convergence study for the calculation of a) CD and b) ˙m of a liquid water droplet during shock interaction. The shock Mach number is 1.47. 
Reynolds number is 1000.
kwater =0.68 W·m−1 ·K−1
γwater =5.89 ×10−2 N/m
With the above values for the material properties and the ﬂow conditions, the non-dimensional numbers are ReD =1000
and WeD =69.56.
A grid convergence study is performed to establish the convergence of the current numerical framework. Five different 
grid resolutions corresponding to 50, 100, 150, 200 and 250 grid points across the diameter of the water are used. The CD
and ˙m of the droplet during shock interaction are plotted against non-dimensionalized time in Fig. 21. Fig. 21 shows that 
the CD and ˙m converge as the grid is reﬁned.
The average drag coeﬃcient (CD) and the vaporization rate ( ˙m) of the water droplet during interaction with the incoming 
shock wave are computed from the following equation:
CD =
∫ t2
t1
CDdt
t2 − t1
(73)
˙m =
∫ t2
t1
˙mdt
t2 − t1
(74)
where, t1 = 0.5D
Us
and t2 = 8.0D
Us
. The relative error in the calculation of CD(ϵCD ) and ˙m(ϵ˙m) are evaluated with respect to the 
results obtained from the ﬁnest grid as follows:
ϵCD =
⏐⏐⏐⏐
(CDGRIDi − CDGRID5)
CDGRID5
⏐
⏐⏐⏐
(75)
ϵ˙m =
⏐
⏐⏐
⏐
(
˙mGRIDi − ˙mGRID5)
˙mGRID5
⏐⏐⏐
⏐
(76)

<!-- PDF_PAGE: 25 -->

P. Das, H.S. Udaykumar / Journal of Computational Physics 405 (2020) 109005 25
Fig. 22. Grid convergence study based of the error in the a)C D and b) ˙m of a droplet calculated using the current sharp-interface method.
The CD, ϵCD , ˙m, and ϵ ˙m computed from the different grid resolutions are tabulated below:
Table 7
˙m computed from numerical calculations using different grid resolution.
Grid D
/Delta1x CD ϵCD ˙m (kg·m−2 ·s−1) ϵ˙m
GRID1 50 2.3231 0.0850 17.23 2.27
GRID2 100 2.4415 0.0378 10.93 1.08
GRID3 150 2.5081 0.0116 8.2 0.56
GRID4 200 2.5338 0.0015 6.24 0.18
GRID5 250 2.3376 – 5.26 –
The values of CD and ˙m in Table 7 show that the results obtained from the current sharp-interface method converge 
as the grid resolution of the calculation is increased. ϵCD and ϵ˙m ˙ are plotted against grid resolution in Fig. 22(a) and (b), 
respectively. Fig. 22 shows that the relative error in the current calculations decreases monotonically with grid reﬁnement.
The results obtained from GRID 4 are further analyzed to study the physics captured through the present viscous sim-
ulations. The effect of viscosity on the ﬂow-ﬁeld  during shock-droplet interaction is examined by comparing the velocity 
contours obtained from inviscid and viscous simulations in Fig. 23. Fig. 23(a) shows a comparison between the ﬂow-ﬁelds  
shortly after the shock wave has passed over the droplet, at non-dimensional time t∗ = 3.41. Due to the presence of a 
boundary layer, the ﬂow detaches from the droplet earlier in the viscous simulation than in the inviscid simulation. The 
early ﬂow-separation in the viscous simulation leads to a larger recirculation region in the wake in comparison with the 
inviscid case. Fig. 23(a), (b) and (c) show that a longer recirculation region forms in the wake of the droplet under the 
inﬂuence of viscosity. Furthermore, the results from the viscous simulations in Fig. 23(b) and (c) show two counter-rotating 
separation bubbles near the droplet surface after the ﬂow has separated. Such counter-rotating separation bubbles are absent 
in the inviscid simulation results. The comparison in Fig. 23 shows that the ﬂow-ﬁeld  near the droplet is heavily inﬂuenced 
by viscosity even during the short-period of shock-droplet interaction.
The deformed shape of the droplet is also signiﬁcantly affected by the viscosity. Higher deformation of the droplet is 
observed in the inviscid calculation in Fig. 23(b) and (c). The shape of the deformed droplet is different in the inviscid and 
the viscous cases because the tangential component of velocity of the liquid near the interface is inﬂuenced by the ﬂow 
outside the droplet in the viscous case. The higher diffusion in the viscous calculation also suppresses the density-gradient 
driven instabilities at the interface resulting in a smoother shape of the droplet in the viscous simulation. Deff is plotted 
in Fig. 24 to show the differences in the shapes of the droplet in the inviscid and the viscous simulation. The lower Deff
of the droplet in the inviscid simulation indicates that the droplet deforms more in the absence of viscosity, as observed 
previously in Fig. 23(b) and (c).
The ﬂow-ﬁeld  around the droplet inﬂuences its CD and ˙m. Fig. 25 shows that the CD and ˙m of the droplet calculated 
from the viscous and the inviscid simulations are signiﬁcantly different. Fig. 25(a) shows that the CD of the droplet in the 
viscous calculation is higher than the inviscid calculation because of the early ﬂow-separation from the droplet surface 
and the skin-friction drag till t∗ ∼ 13. The CD of the droplet in the inviscid calculation becomes higher than the viscous 
calculation in the later part of the shock droplet interaction. The droplet in the inviscid calculation experiences higher 
pressure drag than the viscous calculation as the droplet deforms more in the inviscid calculation. The non-monotonicity 
of the CD in inviscid calculation seen in Fig. 25(a) indicates the unsteadiness of the inviscid ﬂow-ﬁeld.  The presence of 
viscosity suppresses ﬂow unsteadiness and CD of the droplet keeps increasing in the viscous calculation as the droplet 
deforms further.

<!-- PDF_PAGE: 26 -->

26 P. Das, H.S. Udaykumar / Journal of Computational Physics 405 (2020) 109005
Fig. 23. Evolution of ﬂow around a water droplet of 37 μm in diameter during interaction with a Mach 1.47 shock wave. The left column shows the results 
obtained from the inviscid simulations. The right column shows the results obtained from viscous simulations.
Fig. 24. AC o m p a r i s o no fDeff obtained from the inviscid and viscous simulation of Mach 1.47 shock interaction with the 37 μm droplet.
Fig. 25(b) compares the ˙m of the droplet computed from the inviscid and the viscous calculations. The ˙m of the droplet 
is over predicted in the inviscid calculation during the initial period of the shock-droplet interaction. The absence of the 
boundary-layer around the droplet enhances the convective transport of the vapor from the droplet surface in the inviscid 
calculation. The lower vapor pressure around the droplet increases the ˙m of the droplet. However, the ˙m of the droplet in 
the inviscid simulation decreases at a higher rate than the viscous simulation as the droplet starts to deform. Therefore, 
viscosity plays a signiﬁcant role in modulating the ˙m of the droplet during shock-interaction. The comparison between the

<!-- PDF_PAGE: 27 -->

P. Das, H.S. Udaykumar / Journal of Computational Physics 405 (2020) 109005 27
Fig. 25. Comparison of a) CD and b) ˙m obtained from the inviscid and viscous simulation of Mach 1.47 shock interaction with the 37 μm droplet.
viscous and the inviscid calculations Fig. 23, 25 and 26 show that viscosity has signiﬁcant effects on the ﬂow-ﬁeld  around 
the droplet and the viscous simulation captures important ﬂow physics that are absent in the inviscid study.
The pressure-gradient driven viscous ﬂow-ﬁeld  has a signiﬁcant inﬂuence on the distribution and mixing of the resulting 
vapor in the near wake of the droplet during the interaction with the shock. The vaporization of the water droplet is shown 
through multiple snapshots of numerical Schlieren, pressure and vapor mass fraction contours in Fig. 26. As the shock-wave 
passes over the droplet, a high-pressure region is created in front of the droplet due to the reﬂected shock wave. On the 
other hand, the leeward portion of the droplet surface experiences low pressures caused by expansion waves. Pressurization 
of the vapor suppresses the rate of vaporization of the droplet from the front surface of the droplet. The local vaporization 
rate is higher on the leeward side due to the lower pressure, as seen in Fig. 26(a). The local vaporization rate of the 
droplet is highest in the region of the droplet surface where the expansion waves emerge. The resulting vapor is advected 
downstream and accumulates in the recirculation region behind the droplet.
As the droplet deforms, the boundary layer separates from the droplet surface and counter-rotating separation bubbles 
form between the separated boundary layer and the droplet surface. The vapor is accumulated in those separation bubbles. 
This high concentration of vapor between the separated boundary layer and the droplet surface is seen in Fig. 26(b)–(d). The 
high concentration of the vapor suppresses vaporization from the droplet surface behind the point of separation. The vapor 
accumulated in the separation bubble then ﬂows into the growing recirculation regions. At later times, the shear layer at the 
boundary of the recirculation region starts to become unstable. The mixing of the water vapor trapped in the recirculation 
bubble and the outer ﬂow is enhanced by the shear layer instabilities seen in Fig. 26(e).
The results in Fig. 23 and Fig. 26 imply that the ﬂow physics, in particular, the effect of viscosity, has a signiﬁcant 
impact on the rate of formation and distribution of vapor from the liquid droplets during shock interaction. The current 
viscous simulations can capture several features of the ﬂow physics which govern the rate of vaporization of the droplets 
and the mixing of the vapor in the gaseous phase. Combined with capillarity effects which modify the overall shape of the 
vaporizing liquid droplet, the current sharp-interface approach provides the ability to accurately model the shock-induced 
vaporization of a cylindrical water droplet in 2D. Due to the dimension-by-dimension implementation of the numerical 
approach, the calculations can be extended in a straightforward manner to 3D, as demonstrated below.
3.6. 3D simulation of shock interaction with a vaporizing droplet
To demonstrate capabilities, a 3D simulation of shock interaction with a vaporizing droplet is performed for the case of a 
Mach 1.47 shock impinging on a spherical water droplet of 37 microns in diameter. ReD of the post-shock ﬂow with respect 
to the droplet is 1000.
Fig. 27 sho ws the schematic diagram of the initial setup for the numerical calculation. The initial conditions are given in 
the Table 8:
Table 8
Initial conditions for the 3D simulation of shock interaction with a vaporizing droplet.
ρ(kg/m3) p (Pa) u (m/s) T (K)
Pre-shocked air ( X
D ≥ 1.8) 1.2 101000 0.0 293.0
Post-shocked air ( X
D <1.8) 2.17 237792.72 225.91 381.0
Droplet 997 .0 104193.05 0.0 373.0

<!-- PDF_PAGE: 28 -->

28 P. Das, H.S. Udaykumar / Journal of Computational Physics 405 (2020) 109005
Fig. 26. Sequence of contour plot obtained from the simulation of Mach 1.47 shock induced vaporization of a droplet (ReD =1000). The left column shows 
the numerical schlieren images. Pressure contours are shown in the middle column. The contours of mass fraction of the water vapor are shown in the 
right column. In the above plots, the reference pressure, pref =101000.0P a .

<!-- PDF_PAGE: 29 -->

P. Das, H.S. Udaykumar / Journal of Computational Physics 405 (2020) 109005 29
Fig. 27. The initial condition for 3D simulation of Mach 1.47 shock interaction with a water droplet of 37 μm in diameter.
Neuman boundary conditions are used on all sides of the computational domain. The grid resolution is limited to 50 grid 
points across the diameter of the droplet to facilitate calculations at a reasonable computational cost for this 3D simulation.
The simulation was performed using 448 processors on the Argon cluster at the University of Iowa. The calculations 
were done till t∗ =28. Total 31000 CPU-hours were consumed in this calculation. 3D simulations are computationally more 
expensive than the 2D simulations, because, one more governing equation for the momentum conservation in z-direction 
is solved in the 3D simulations along with the convective and the diffusive terms along the z-direction in the species, 
momentum and the energy conservation equations. Furthermore, the communication of data across the processors also 
become more expensive 3D. The volume to the surface area ratio of the computational domain, partitioned and distributed 
among the different processors, increase in 3D calculation. Therefore, more data is required to be communicated among the 
processors at every timestep of the simulation. Hence, 3D calculations become signiﬁcantly more expensive than the 2D 
calculations.
The current grid-resolution of 50 points per droplet diameter is inadequate to realize fully grid-independent solutions 
for the problem and the present simulation only demonstrates the broad features of the 3D dynamics. A fully resolved 3D 
simulation will require approximately 200 grid points across the diameter; such expensive simulations are impractical with 
the currently available computational resources to the authors. The present simulation is, therefore, to be viewed only as a 
demonstration of the capability.
Fig. 28 sho ws the sequence of temperature and vapor mass fraction contours as the shock wave interacts with the 
droplet. In Fig. 28, the 2D slices of data from y/D =1.5 and z/D =1.5 planes of the solution domain are extracted and 
projected on the ﬂoor and the backdrop of the computational domain. The iso-surface of the zero levelset ﬁelds is plotted 
in 3D to demonstrate the shape of the droplet. The results presented in Fig. 28 show that the deformed shape of the 
spherical droplet is similar to the shapes seen in the 2D calculation. The Ywater contours in Fig. 28 show that the water 
vapor accumulates in the recirculation region behind the droplet, as seen in the 2D simulations.
Fig. 29 sho ws  the comparison of the ˙m of the droplet computed from 2D and 3D simulations for the same grid resolution. 
The spherical droplet vaporizes at a higher rate than the 2D cylindrical droplet. This is because the spherical droplet in 3D 
has a higher fraction of the surface area exposed to the low-pressure zone behind the droplet, as compared to the cylindrical 
droplet in 2D. It is worth reiterating that the rate of vaporization of the droplet calculated from the current 3D simulations is 
not a grid converged solution. However, the results shown in Fig. 28 and Fig. 29 demonstrate that, even with low resolution, 
the current 3D simulations lead to the reasonable overall behavior of the droplet surface and ﬂuid ﬂow and the results 
are within the range of the grid converged results obtained from the 2D simulations. This demonstrates that the current 
sharp-interface method is capable of solving 3D problems as well.
4. Conclusions
A sharp-interface method is presented for resolved simulations of shock-droplet interactions. A modiﬁed GFM approach 
(RS-GFM) is developed to account for the jump-conditions across vaporizing liquid-gas interfaces. The method is used to 
calculate the transient physics of shock-induced vaporization of droplets.
Comparison with previous experimental and numerical studies show that the current method can predict the detailed 
physics of shock-droplet interaction with good accuracy. The interfacial mechanics of a droplet during shock interaction

<!-- PDF_PAGE: 30 -->

30 P. Das, H.S. Udaykumar / Journal of Computational Physics 405 (2020) 109005
Fig. 28. Sequence of temperature (left column) and vapor mass-fraction (right column) contours shown to demonstrate shock-induced evaporation of a
droplet in 3D. In this study, a Mach 1.47 shock wave interacts with a water droplet of 37 μm in diameter. The temperature and vapor mass fraction 
contours at y/D =1.5a n d z/D =1.5p l a n e s are projected on the bottom and the side of the solution domain respectively. The iso-contour of the zero 
levelset ﬁeld is colored with temperature and vapor mass fraction to show distribution of these variable on the air-water interface. In the above plots, the 
reference temperature, Tref =293.0K .

<!-- PDF_PAGE: 31 -->

P. Das, H.S. Udaykumar / Journal of Computational Physics 405 (2020) 109005 31
Fig. 29. Comparison of shock-induced (Mach 1.47) evaporation rate of a 37 micron water droplet computed from 2D and 3D calculation.
predicted using the current method matches well with the benchmark results. The current method is capable of predicting 
important details of the ﬂow-ﬁeld  such as boundary layer separation and formation of the separation bubbles accurately. The 
rate of vaporization of a droplet computed using the current method is in a good agreement with the previous benchmark 
result. The current method is also found to converge with grid reﬁnement.
The results show that the interfacial jump conditions are implemented correctly using the current RS-GFM. The current 
RS-GFM is also less expensive and easier to implement than the previous GFM [49]b e c a u s e the ghost values of the velocity 
ﬁeld are obtained explicitly instead of solving a system of four simultaneous equation in 2D and six simultaneous equations 
in 3D. Furthermore, grid reﬁnement studies show that the numerical stability issues in the previous GFM [49]i s resolved in 
the current RS-GFM by rotating the velocity ﬁeld instead of the viscous stress tensor from the Cartesian grid coordinates to 
the interface-normal direction.
The present sharp-interface method is also extended to 3D. A 3D numerical study of shock-induced vaporization of a 
water droplet is performed. To the authors’ knowledge, the present work has presented the ﬁrst 3D simulations of shock 
interaction with a vaporizing droplet in the open literature.
This study is being further extended through several ongoing works. The framework is being used to develop data-driven 
models for vaporization of droplets in shocked ﬂows using machine learning [63,77–80]. Reactive dynamics of the Aluminum 
droplet in the surrounding air stream, including the formation of a layer of oxide on the droplet surface, is being modeled. 
Furthermore, the current framework is applicable to small droplets of submicron sizes only. In small droplets, the surface 
tension forces are strong enough to prevent cavitation within the droplet during shock interaction. However, larger droplets, 
approaching hundreds of microns in diameter, will be more susceptible to shattering caused by cavitation inside the droplets. 
The current framework is being extended to account for cavitation within the droplets in other ongoing work. Droplet 
merging and breakup during shock interaction is also being studied. Such a numerical framework for direct numerical 
simulation of compressible multiphase ﬂows with reacting interfaces will be useful in understating shock interaction with 
clusters of particles and droplets in greater detail.
Declaration of competing interest
The authors declare that they have no known competing ﬁnancial interests or personal relationships that could have 
appeared to inﬂuence the work reported in this paper.
Acknowledgements
We gratefully acknowledge the ﬁnancial support by the Air Force Oﬃce of Scientiﬁc Research under grant numbers 
FA9550-15-1-0332 (Program Oﬃcer: Dr. Martin Schmidt) and SA0000506 (Program Oﬃcer: Dr. Fariba Fahroo).
Appendix A. Numerical method for constructing the interface-normal 1-D Riemann problem
Fig. 30 sho ws  a schematic to illustrate the numerical method for constructing the interface-normal 1-D Riemann problem 
at a typical interfacial ghost point labeled IG. The initial conditions for the local Riemann problem are obtained from the 
ﬂow variables (ρ, un, p) in the gaseous and the liquid phases near the interface. The ﬂow variables near the interface are 
obtained by probing the ﬂow-ﬁeld  at a distance of 1.5/Delta1x from the interface in each phase. To probe for the values of the 
ﬂow-ﬁeld,  ﬁrst, the normal projection of IG on the interface, (point labeled I in Fig. 23) is obtained. The location of I is 
obtained from the following equation:
XI = XIG − φIGnIG (77)

<!-- PDF_PAGE: 32 -->

32 P. Das, H.S. Udaykumar / Journal of Computational Physics 405 (2020) 109005
Fig. 30. Schematic diagram of the numerical algorithm to construct an interfacial Riemann problem normal to the gas-liquid interface.
where φIG is the magnitude of the levelset ﬁeld at the point IG and nIG is the unit vector normal to the interface computed 
at IG from the levelset ﬁeld [23]. XI and XIG are the locations of the points I and IG, respectively. Following this, two probes, 
G and L, are inserted in the gaseous and the liquid phases respectively. The probes are /Delta1n away from the point I on the 
interface. The locations of the probes are given by the following equations:
XG = XI + /Delta1nnIG (78)
XL = XI − /Delta1nnIG (79)
where XG and XL are the positions of the ends of the probes G and L respectively. A convex hull is formed around G and L
using neighboring grid points in the vicinity, as shown in Fig. 30. The ﬂow variables at G and L are obtained using bilinear 
interpolation from values at the grid points forming the convex hull.
Appendix B. The interfacial Riemann problem
The structure of the interfacial Riemann problem solved to populate the ghost points is shown in Fig. 31. The initial 
conditions for the Riemann problem are obtained by probing the gaseous and the liquid phases at 1.5/Delta1x distance away 
from the interface. Initially, the right-hand side of the interface is chosen as the gaseous phase and the left-hand side is 
the liquid phase. As the system is released from this initial condition and allowed to evolve freely, three wave-structures 
may evolve depending on the initial conditions. The structure of the solution is shown in Fig. 31. A shock or rarefaction 
wave will travel to the right, into the gaseous phase. Another shock or rarefaction wave will travel to the left, into the 
liquid phase. There will a third wave travelling as a contact discontinuity at the gas-liquid interface. The interfacial jump 
conditions given by the Eq. (29) and (30)i n the manuscript are satisﬁed at the contact-discontinuity. The intermediate “∗” 
states are obtained from the Rankine-Hugoniot conditions for the Riemann waves in the respective phases. u∗
n,l and u∗
n,g
are obtained from the Rankine-Hugoniot conditions in the respective phases, such that the jump condition at the interface 
given by Eq. (29)i s satisﬁed. How u∗
n,l and u∗
n,g are obtained for the shock and the rarefactions waves in the liquid and the 
gaseous phases respectively are described below:
A shock travelling to the left in the liquid phase
Let us assume a shock wave is generated in the liquid phase as the system is released from the initial condition. The 
shock is travelling at a speed Sl to the left through the liquid. Fig. 32(a) shows the conditions across the shock from a 
stationary observer’s point of reference. The initial condition (ρl, un,l, pl) to the left of the shock wave remains unperturbed. 
The intermediate states (ρ∗
l , u∗
n,l, p∗
l ) exist to the right side of the shock. Fig. 32(b) shows the conditions across the shock 
from a reference moving along with the shock at the same speed. Therefore, the relative velocities to the left and the right 
of the shock is given by:

<!-- PDF_PAGE: 33 -->

P. Das, H.S. Udaykumar / Journal of Computational Physics 405 (2020) 109005 33
Fig. 31. Structure of the Riemann problem solved at the gas-liquid interface to obtain the ﬂow variables at the ghost ﬂuid points.
Fig. 32. The shock travelling to the left in the liquid phase (a) with respect to a stationary frame of reference (b) with respect to a frame of reference 
travelling with the shock at the same speed.
ˆun,l = un,l − Sl (80)
ˆu∗
n,l = u∗
n,l − Sl (81)
The Rankine-Hugoniot conditions across the shock are:
ρl ˆun,l = ρ∗
l ˆu∗
n,l (82)
ρl ˆu2
n,l + pl = ρl ˆu∗2
n,l + p∗
l (83)
el + pl
ρl
+
ˆu2
n,l
2 = e∗
l +
p∗
l
ρ∗
l
+
ˆu∗2
n,l
2 (84)
where el and e∗
l are the speciﬁc internal energy of the ﬂuid to the left and the right of the shock, respectively. For the Tait 
equation of state, e is related to p and ρ through the following relation in the liquid state [57]:
e = N(p + B)
ρ(N − 1) (85)
where B = B − A. N, B and A are physical constants and are tabulated in Table 1.
Now, eliminating ˆun,l from Eq. (82) and (83) and after rearranging we obtain:
ˆu∗2
n,l = (pl − p∗
l )ρl
(ρl − ρ∗
l )ρ∗
l
(86)
Substituting ˆu∗2
n,l in Eq. (84) and rearranging we get:
e∗
l − el = (pl − p∗
l )(ρl + ρ∗
l )
2ρlρ∗
l
+ pl
ρl
−
p∗
l
ρ∗
l
(87)
Using Eq. (85)i n Eq. (87) and rearranging we get:
ρ∗
l
ρl
=
p∗
l +B
pl+B + N−1
N+1
N−1
N+1
p∗
l +B
pl+B +1
(88)

<!-- PDF_PAGE: 34 -->

34 P. Das, H.S. Udaykumar / Journal of Computational Physics 405 (2020) 109005
Let us deﬁne,
Ql = ρl ˆun,l = ρ∗
l ˆu∗
n,l (89)
Substituting Ql in (83) and rearranging, we get:
Ql =−
pl − p∗
l
ˆun,l − ˆu∗
n,l
(90)
From Eq. (89) and (90)w e obtain:
Q2
l =−
pl − p∗
l
1
ρl
− 1
ρ∗
l
(91)
After eliminating ρ∗
l from Eq. (88) and (91) followed by algebraic manipulation, one can obtain:
Ql =
√
(p∗
l + B) + Bl
Al
(92)
where
Al = 2
(N +1)ρl
, Bl = N − 1
N +1(pl + B)
Again substituting Eq. (80) and (81)i n Eq. (90) and rearranging we obtain:
u∗
n,l = un,l −
p∗
l − pl
Ql
(93)
Now, substituting Ql from Eq. (92)i n Eq. (93), we get:
u∗
n,l = un,l − fl (94)
where
fl =
(
p∗
l − pl
)
√
Al
(p∗
l + B) + Bl
(95)
The above solution of u∗
n,l in Eq. (94)i s valid only for a shock wave traveling in the liquid phases, i.e. when p∗
l > pl. u∗
n,l
for a rarefaction wave in the liquid phase is derived next.
A rarefaction wave travelling to the left in the liquid phase
The expression of fl for a rarefaction wave travelling left in the liquid domain is derived next.
The isentropic law in the liquid is given by:
p + B
ρN =constant (96)
and the speed of sound (a) in the medium is given by:
a =
√
N(p + B)
ρ (97)
Now, the Riemann invariant in the following equation remains constant across the rarefaction wave [74]:
u +
∫ a
ρdρ=constant (98)
Using Eq. (96) and (98), we can obtain:
u + 2a
N − 1 =constant (99)
Therefore, across the rarefaction wave, we can write:
u∗
n,l +
2a∗
l
N − 1 = un,l + 2al
N − 1 (100)

<!-- PDF_PAGE: 35 -->

P. Das, H.S. Udaykumar / Journal of Computational Physics 405 (2020) 109005 35
After algebraic manipulation, the following is obtained from Eq. (100):
u∗
n,l = un,l − 2al
N − 1
( a∗
l
al
− 1
)
(101)
Using Eq. (96) and (97)w e obtain the following expression for u∗
n,l:
u∗
n,l = un,l − fl (102)
where
fl = 2al
N − 1
[( p∗
l + B
pl + B
) N−1
2N
− 1
]
The above expression of fl is valid for p∗
l <pl.
A shock or rarefaction wave travelling to the right in the gaseous phase
The calculation of the intermediate state velocity u∗
n,g for the gaseous phase in the right-hand side of the domain follow 
along the same line of the liquid phase. The expression for u∗
n,g, as derived in [74], is the following:
u∗
n,g = un,g − fg (103)
where
fg =
⎧
⎪⎨
⎪⎩
(p∗
g − pg)
√
Ag
p∗
g+Bg
, when p∗
g > pg
2ag
γ−1 [(
p∗
g
pg
)
γ−1
2γ − 1], when p∗
g < pg
Ag = 2
(γ +1)ρg
Bg = γ − 1
γ +1 pg
ag =
√
γpg
ρg
Now that the expressions for u∗
n,l and u∗
n,g are obtained, they are substituted in Eq. (29)t o obtain the following algebraic 
equation:
fl
(
p∗
l , pl,ρl, un,l
)
+ fg
(
p∗
g, pg,ρg, un,g
)
+ un,g − un,l +[ un]= 0 (104)
The above Riemann problem is solved along with the jump-conditions given by Eq. (29) and (30)i n the manuscript using 
the Newton-Raphson method to obtain p∗
g and p∗
l . ρ∗
g, ρ∗
l , u∗
n,g and u∗
n,l are obtained from the following equations:
ρ∗
g =
⎧
⎪⎪⎪⎨
⎪⎪⎪
⎩
ρg
√
p∗g
pg + γ−1
γ+1
γ−1
γ+1
p∗g
pg +1
, when p∗
g > pg
ρg(
p∗
g
pg
)
1
γ , when p∗
g < pg
(105)
ρ∗
l =
⎧
⎪⎪⎪
⎪⎨
⎪⎪⎪
⎪
⎩
ρl

√
p∗
l +B
pl+B + N−1
N+1
γ−1
γ+1
p∗
l +B
pl+B +1
, when p∗
l > pl
ρl(
p∗
l +B
pl+B )
1
N , when p∗
l < pl
(106)
u∗
g = ug + ul
2 + fg − fl
2 +
˙m′′[1
ρ]
2 (107)
u∗
l = ug + ul
2 + fg − fl
2 −
˙m′′[1
ρ]
2 (108)

<!-- PDF_PAGE: 36 -->

36 P. Das, H.S. Udaykumar / Journal of Computational Physics 405 (2020) 109005
References
[1] W. Mayer, H. Tamura, Propellant injection in a liquid oxygen/gaseous hydrogen rocket engine, J. Propuls. Power 12 (1996) 1137–1147, https://doi .org /
10 .2514 /3 .24154.
[2] O.A. Powell, J.T. Edwards, R.B. Norris, K.E. Numbers, J.A. Pearce, Development of hydrocarbon-fueled scramjet engines: the hypersonic technology 
(HyTech) program, J. Propuls. Power 17 (2001) 1170–1176, https://doi .org /10 .2514 /2 .5891.
[3] W. Fan, C. Yan, X. Huang, Q. Zhang, L. Zheng, Experimental investigation on two-phase pulse detonation engine, Combust. Flame 133 (2003) 441–450, 
https://doi .org /10 .1016 /S0010 -2180(03 )00043 -9.
[4] K. Balakrishnan, A.L. Kuhl, J.B. Bell, V.E. Beckner, An empirical model for the ignition of explosively dispersed aluminum particle clouds, Shock Waves 
22 (2012) 591–603, https://doi .org /10 .1007 /s00193 -012 -0388 -5.
[5] I.S. Kang, L.G. Leal, Numerical solution of axisymmetric, unsteady free-boundary problems at ﬁnite Reynolds number. I. Finite-difference scheme and 
its application to the deformation of a bubble in a uniaxial straining ﬂow, Phys. Fluids 30 (1987) 1929–1940, https://doi .org /10 .1063 /1.866207.
[6] G. Ryskin, L.G. Leal, Numerical solution of free-boundary problems in ﬂuid mechanics. Part 1. The ﬁnite-difference technique, J. Fluid Mech. 148 (1984) 
1, https://doi .org /10 .1017 /S0022112084002214.
[7] J. Fukai, Z. Zhao, D. Poulikakos, C.M. Megaridis, O. Miyatake, Modeling of the deformation of a liquid droplet impinging upon a ﬂat surface, Phys. Fluids, 
Fluid Dyn. 5 (1993) 2588–2599, https://doi .org /10 .1063 /1.858724.
[8] H.H. Hu, N.A. Patankar, M.Y. Zhu, Direct numerical simulations of ﬂuid–solid  systems using the arbitrary Lagrangian–Eulerian technique, J. Comput. 
Phys. 169 (2001) 427–462, https://doi .org /10 .1006 /jcph .2000 .6592.
[9] K. Yang, F. Hong, P. Cheng, A fully coupled numerical simulation of sessile droplet evaporation using arbitrary Lagrangian–Eulerian formulation, Int. J. 
Heat Mass Transf. 70 (2014) 409–420, https://doi .org /10 .1016 /j .ijheatmasstransfer.2013 .11.017.
[10] G.J. Ball, B.P. Howell, T.G. Leighton, M.J. Schoﬁeld, Shock-induced collapse of a cylindrical air cavity in water: a free-Lagrange simulation, Shock Waves 
10 (2000) 265–276, https://doi .org /10 .1007 /s001930000060.
[11] C.K. Turangan, A.R. Jamaluddin, G.J. Ball, T.G. Leighton, Free-Lagrange simulations of the expansion and jetting collapse of air bubbles in water, J. Fluid 
Mech. 598 (2008) 1–25, https://doi .org /10 .1017 /S0022112007009317.
[12] A.A. Johnson, T.E. Tezduyar, 3D simulation of ﬂuid-particle interactions with the number of particles reaching 100, Comput. Methods Appl. Mech. Eng. 
145 (1997) 301–321, https://doi .org /10 .1016 /S0045 -7825(96 )01223 -6.
[13] J. Glimm, M.J. Graham, J. Grove, X.L. Li, T.M. Smith, D. Tan, F. Tangerman, Q. Zhang, Front tracking in two and three dimensions, Comput. Math. Appl. 
35 (1998) 1–11, https://doi .org /10 .1016 /S0898 -1221(98 )00028 -5.
[14] J. Glimm, J. Grove, X. Li, K. Shyue, Y. Zeng, Q. Zhang, Three-dimensional front tracking, SIAM J. Sci. Comput. 19 (1998) 703–727, https://doi .org /10 .1137 /
S1064827595293600.
[15] G. Tryggvason, B. Bunner, A. Esmaeeli, D. Juric, N. Al-Rawahi, W. Tauber, J. Han, S. Nas, Y.-J. Jan, A front-tracking method for the computations of 
multiphase ﬂow, J. Comput. Phys. 169 (2001) 708–759, https://doi .org /10 .1006 /jcph .2001.6726.
[16] H. Terashima, G. Tryggvason, A front-tracking/ghost-ﬂuid method for ﬂuid interfaces in compressible ﬂows, J. Comput. Phys. 228 (2009) 4012–4037, 
https://doi .org /10 .1016 /j .jcp .2009 .02 .023.
[17] D.M. Anderson, G.B. McFadden, A.A. Wheeler, Diffuse-interface methods in ﬂuid mechanics, Annu. Rev. Fluid Mech. 30 (1998) 139–165, https://doi .org /
10 .1146 /annurev.ﬂuid .30 .1.139.
[18] G. Allaire, S. Clerc, S. Kokh, A ﬁve-equation model for the simulation of interfaces between compressible ﬂuids, J. Comput. Phys. 181 (2002) 577–616, 
https://doi .org /10 .1006 /jcph .2002 .7143.
[19] C.W. Hirt, B.D. Nichols, Volume of ﬂuid (VOF) method for the dynamics of free boundaries, J. Comput. Phys. 39 (1981) 201–225, https://doi .org /10 .
1016 /0021 -9991(81 )90145 -5.
[20] B. Lafaurie, C. Nardone, R. Scardovelli, S. Zaleski, G. Zanetti, Modelling merging and fragmentation in multiphase ﬂows with SURFER, J. Comput. Phys. 
113 (1994) 134–147, https://doi .org /10 .1006 /jcph .1994 .1123.
[21] R. Scardovelli, S. Zaleski, Direct numerical simulation of free-surface and interfacial ﬂow, Annu. Rev. Fluid Mech. 31 (1999) 567–603, https://doi .org /10 .
1146 /annurev.ﬂuid .31.1.567.
[22] S. Tanguy, T. Ménard, A. Berlemont, A level set method for vaporizing two-phase ﬂows, J. Comput. Phys. 221 (2007) 837–853, https://doi .org /10 .1016 /
j .jcp .2006 .07.003.
[23] J.A. Sethian, P. Smereka, Level set methods for ﬂuid interfaces, Annu. Rev. Fluid Mech. 35 (2003) 341–372, https://doi .org /10 .1146 /annurev.ﬂuid .35 .
101101.161105.
[24] S. Osher, J.A. Sethian, Fronts propagating with curvature-dependent speed: algorithms based on Hamilton-Jacobi formulations, J. Comput. Phys. 79 
(1988) 12–49, https://doi .org /10 .1016 /0021 -9991(88 )90002 -2.
[25] S. Marella, S. Krishnan, H. Liu, H.S. Udaykumar, Sharp interface Cartesian grid method I: an easily implemented technique for 3D moving boundary 
computations, J. Comput. Phys. 210 (2005) 1–31, https://doi .org /10 .1016 /j .jcp .2005 .03 .031.
[26] H. Liu, S. Krishnan, S. Marella, H.S. Udaykumar, Sharp interface Cartesian grid method II: a technique for simulating droplet interactions with surfaces 
of arbitrary shape, J. Comput. Phys. 210 (2005) 32–54, https://doi .org /10 .1016 /j .jcp .2005 .03 .032.
[27] Y. Yang, H.S. Udaykumar, Sharp interface Cartesian grid method III: solidiﬁcation of pure materials and binary solutions, J. Comput. Phys. 210 (2005) 
55–74, https://doi .org /10 .1016 /j .jcp .2005 .04 .024.
[28] R. Saurel, R. Abgrall, A multiphase Godunov method for compressible multiﬂuid and multiphase ﬂows, J. Comput. Phys. 150 (1999) 425–467, https://
doi .org /10 .1006 /jcph .1999 .6187.
[29] J.C. Meng, T. Colonius, Numerical simulations of the early stages of high-speed droplet breakup, Shock Waves 25 (2015) 399–414, https://doi .org /10 .
1007 /s00193 -014 -0546 -z.
[30] J.C. Meng, T. Colonius, Numerical simulation of the aerobreakup of a water droplet, J. Fluid Mech. 835 (2018) 1108–1135, https://doi .org /10 .1017 /jfm .
2017.804.
[31] D.P. Garrick, M. Owkes, J.D. Regele, A ﬁnite-volume HLLC-based scheme for compressible interfacial ﬂows with surface tension, J. Comput. Phys. 339 
(2017) 46–67, https://doi .org /10 .1016 /j .jcp .2017.03 .007.
[32] D.P. Garrick, W.A. Hagen, J.D. Regele, An interface capturing scheme for modeling atomization in compressible ﬂows, J. Comput. Phys. 344 (2017) 
260–280, https://doi .org /10 .1016 /j .jcp .2017.04 .079.
[33] Q. Wan, H. Jeon, R. Deiterding, V. Eliasson, Numerical and experimental investigation of oblique shock wave reﬂection off a water wedge, J. Fluid Mech. 
826 (2017) 732–758, https://doi .org /10 .1017 /jfm .2017.452.
[34] K. Fujisawa, T.L. Jackson, S. Balachandar, Inﬂuence of baroclinic vorticity production on unsteady drag coeﬃcient in shock–particle interaction, J. Appl. 
Phys. 125 (2019), https://doi .org /10 .1063 /1.5055002.
[35] M.R. Baer, J.W. Nunziato, A two-phase mixture theory for the deﬂagration-to-detonation transition (ddt) in reactive granular materials, Int. J. Multiph. 
Flow 12 (1986) 861–889, https://doi .org /10 .1016 /0301 -9322(86 )90033 -9.
[36] A. Chinnayya, E. Daniel, R. Saurel, Modelling detonation waves in heterogeneous energetic materials, J. Comput. Phys. 192 (2004) 490–538.
[37] R.K. Shukla, C. Pantano, J.B. Freund, An interface capturing method for the simulation of multi-phase compressible ﬂows, J. Comput. Phys. 229 (2010) 
7411–7439, https://doi .org /10 .1016 /j .jcp .2010 .06 .025.

<!-- PDF_PAGE: 37 -->

P. Das, H.S. Udaykumar / Journal of Computational Physics 405 (2020) 109005 37
[38] A. Tiwari, J.B. Freund, C. Pantano, A diffuse interface model with immiscibility preservation, J. Comput. Phys. 252 (2013) 290–309, https://doi .org /10 .
1016 /j .jcp .2013 .06 .021.
[39] K. Kannan, D. Kedelty, M. Herrmann, An in-cell reconstruction ﬁnite volume method for ﬂows of compressible immiscible ﬂuids, J. Comput. Phys. 373 
(2018) 784–810, https://doi .org /10 .1016 /j .jcp .2018 .07.006.
[40] S.W.J. Welch, J. Wilson, A volume of ﬂuid based method for ﬂuid ﬂows with phase change, J. Comput. Phys. 160 (2000) 662–682, https://doi .org /10 .
1006 /jcph .2000 .6481.
[41] S.K. Sambasivan, H.S. UdayKumar, Ghost ﬂuid method for strong shock interactions Part 1: ﬂuid-ﬂuid  interfaces, AIAA J. 47 (2009) 2907–2922, https://
doi .org /10 .2514 /1.43148.
[42] F. Gibou, L. Chen, D. Nguyen, S. Banerjee, A level set based sharp interface method for the multiphase incompressible Navier–Stokes equations with 
phase change, J. Comput. Phys. 222 (2007) 536–555, https://doi .org /10 .1016 /j .jcp .2006 .07.035.
[43] W.J. Rider, D.B. Kothe, Reconstructing volume tracking, J. Comput. Phys. 141 (1998) 112–152, https://doi .org /10 .1006 /jcph .1998 .5906.
[44] R. Scardovelli, S. Zaleski, Analytical relations connecting linear interfaces and volume fractions in rectangular grids, J. Comput. Phys. 164 (2000) 
228–237, https://doi .org /10 .1006 /jcph .2000 .6567.
[45] Y. Renardy, M. Renardy, PROST: a parabolic reconstruction of surface tension for the volume-of-ﬂuid method, J. Comput. Phys. 183 (2002) 400–421, 
https://doi .org /10 .1006 /jcph .2002 .7190.
[46] T. Ménard, S. Tanguy, A. Berlemont, Coupling level set/VOF/ghost ﬂuid methods: validation and application to 3D simulation of the primary break-up 
of a liquid jet, Int. J. Multiph. Flow 33 (2007) 510–524, https://doi .org /10 .1016 /j .ijmultiphaseﬂow.2006 .11.001.
[47] D.J.E. Harvie, M.R. Davidson, M. Rudman, An analysis of parasitic current generation in volume of ﬂuid simulations, Appl. Math. Model. 30 (2006) 
1056–1066, https://doi .org /10 .1016 /j .apm .2005 .08 .015.
[48] J. Schlottke, B. Weigand, Direct numerical simulation of evaporating droplets, J. Comput. Phys. 227 (2008) 5215–5237, https://doi .org /10 .1016 /j .jcp .2008 .
01.042.
[49] R.W. Houim, K.K. Kuo, A ghost ﬂuid method for compressible reacting ﬂows with phase change, J. Comput. Phys. 235 (2013) 865–900, https://doi .org /
10 .1016 /j .jcp .2012 .09 .022.
[50] R.R. Nourgaliev, S. Wiri, N.T. Dinh, T.G. Theofanous, On improving mass conservation of level set by reducing spatial discretization errors, Int. J. Multiph. 
Flow 31 (2005) 1329–1336, https://doi .org /10 .1016 /j .ijmultiphaseﬂow.2005 .08 .003.
[51] J. Mousel, A Massively Parallel Adaptive Sharp Interface Solver With Application to Mechanical Heart Valve Simulations, Theses Diss., 2012, http://
ir.uiowa .edu /etd /3502.
[52] G.-S. Jiang, C.-W. Shu, Eﬃcient implementation of weighted ENO schemes, J. Comput. Phys. 126 (1996) 202–228, https://doi .org /10 .1006 /jcph .1996 .0130.
[53] S.K. Sambasivan, H.S. UdayKumar, Sharp interface simulations with local mesh reﬁnement for multi-material dynamics in strongly shocked ﬂows, 
Comput. Fluids 39 (2010) 1456–1479, https://doi .org /10 .1016 /j .compﬂuid .2010 .04 .014.
[54] D. Enright, R. Fedkiw, J. Ferziger, I. Mitchell, A hybrid particle level set method for improved interface capturing, J. Comput. Phys. 183 (2002) 83–116, 
https://doi .org /10 .1006 /jcph .2002 .7166.
[55] L. Tran, H.S. Udaykumar, A particle-level set-based sharp interface cartesian grid method for impact, penetration, and void collapse, J. Comput. Phys. 
193 (2004) 469–510.
[56] R.P .  Fedkiw, T. Aslam, B. Merriman, S. Osher, A non-oscillatory Eulerian approach to interfaces in multimaterial ﬂows (the ghost ﬂuid method), J. Com-
put. Phys. 152 (1999) 457–492.
[57] T.G. Liu, B.C. Khoo, C.W. Wang, The ghost ﬂuid method for compressible gas–water simulation, J. Comput. Phys. 204 (2005) 193–221, https://doi .org /
10 .1016 /j .jcp .2004 .10 .012.
[58] M. Kang, R.P. Fedkiw, X.-D. Liu, A boundary condition capturing method for multiphase incompressible ﬂow, J. Sci. Comput. 15 (2000) 323–360, https://
doi .org /10 .1023 /A :1011178417620.
[59] P.M. Carrica, R.V. Wilson, F. Stern, An unsteady single-phase level set method for viscous free surface ﬂows, Int. J. Numer. Methods Fluids 53 (2007) 
229–256, https://doi .org /10 .1002 /ﬂd .1279.
[60] Y. Mehta, K. Salari, T.L. Jackson, S. Balachandar, Effect of Mach number and volume fraction in air-shock interacting with a bed of randomly distributed 
spherical particles, Phys. Rev. Fluids 4 (2019) 014303, https://doi .org /10 .1103 /PhysRevFluids .4 .014303.
[61] Y. Mehta, C. Neal, K. Salari, T.L. Jackson, S. Balachandar, S. Thakur, Propagation of a strong shock over a random bed of spherical particles, J. Fluid Mech. 
839 (2018) 157–197, https://doi .org /10 .1017 /jfm .2017.909.
[62] A.N. Osnes, M. Vartdal, M.G. Omang, B.A.P. Reif, Computational analysis of shock-induced ﬂow through stationary particle clouds, Int. J. Multiph. Flow 
114 (2019) 268–286, https://doi .org /10 .1016 /j .ijmultiphaseﬂow.2019 .03 .010.
[63] P. Das, O. Sen, K.K. Choi, G. Jacobs, H.S. Udaykumar, Strategies for eﬃcient machine learning of surrogate drag models from three-dimensional mesoscale 
computations of shocked particulate ﬂows, Int. J. Multiph. Flow 108 (2018) 51–68, https://doi .org /10 .1016 /j .ijmultiphaseﬂow.2018 .06 .013.
[64] R.J. Kee, M.E. Coltrin, P. Glarborg, Chemically Reacting Flow: Theory and Practice, Wiley, 2003.
[65] T.P. Coffee, J.M. Heimerl, Transport algorithms for premixed, laminar steady-state ﬂames, Combust. Flame 43 (1981) 273–289, https://doi .org /10 .1016 /
0010 -2180(81 )90027 -4.
[66] A. Burcat, Thermochemical data for combustion calculations, in: Combust. Chem., Springer, 1984, pp. 455–473.
[67] S. Gottlieb, C.-W. Shu, Total variation diminishing Runge-Kutta schemes, Math. Comput. Am. Math. Soc. 67 (1998) 73–85, https://doi .org /10 .1090 /S0025 -
5718 -98 -00913 -2.
[68] J.G. Verwer, B.P. Sommeijer, W. Hundsdorfer, RKC time-stepping for advection–diffusion–reaction  problems, J. Comput. Phys. 201 (2004) 61–79, https://
doi .org /10 .1016 /j .jcp .2004 .05 .002.
[69] C.-W. Shu, S. Osher, Eﬃcient implementation of essentially non-oscillatory shock-capturing schemes, II, J. Comput. Phys. 83 (1989) 32–78, https://
doi .org /10 .1016 /0021 -9991(89 )90222 -2.
[70] P. Das, O. Sen, G. Jacobs, H.S. Udaykumar, A sharp interface Cartesian grid method for viscous simulation of shocked particle-laden ﬂows, Int. J. Comput. 
Fluid Dyn. 31 (6–8) (2017) 1–23, https://doi .org /10 .1080 /10618562 .2017.1351610.
[71] M. Sussman, P. Smereka, S. Osher, A level set approach for computing solutions to incompressible two-phase ﬂow, J. Comput. Phys. 114 (1994) 146–159, 
https://doi .org /10 .1006 /jcph .1994 .1155.
[72] W. Bo, X. Liu, J. Glimm, X. Li, A robust front tracking method: veriﬁcation and application to simulation of the primary breakup of a liquid jet, SIAM J. 
Sci. Comput. 33 (2011) 1505–1524, https://doi .org /10 .1137 /10079135X.
[73] T.D. Aslam, A partial differential equation approach to multidimensional extrapolation, J. Comput. Phys. 193 (2004) 349–355, https://doi .org /10 .1016 /j .
jcp .2003 .08 .001.
[74] E.F .  Toro, Riemann Solvers and Numerical Methods for Fluid Dynamics: A Practical Introduction, Springer Science & Business Media, 2013.
[75] S. Sembian, M. Liverts, N. Tillmark, N. Apazidis, Plane shock wave interaction with a cylindrical water column, Phys. Fluids 28 (2016) 056102, https://
doi .org /10 .1063 /1.4948274.
[76] R.W. Houim, Modeling the inﬂuence of shock waves on the combustion of aluminum droplets, https://etda .libraries .psu .edu /catalog /12524, 2011. (Ac-
cessed 25 October 2018).
[77] O. Sen, S. Davis, G. Jacobs, H.S. Udaykumar, Evaluation of convergence behavior of metamodeling techniques for bridging scales in multi-scale multi-
material simulation, J. Comput. Phys. 294 (2015) 585–604, https://doi .org /10 .1016 /j .jcp .2015 .03 .043.

<!-- PDF_PAGE: 38 -->

38 P. Das, H.S. Udaykumar / Journal of Computational Physics 405 (2020) 109005
[78] O. Sen, N.J. Gaul, K.K. Choi, G. Jacobs, H.S. Udaykumar, Evaluation of kriging based surrogate models constructed from mesoscale computations of shock 
interaction with particles, J. Comput. Phys. 336 (2017) 235–260, https://doi .org /10 .1016 /j .jcp .2017.01.046.
[79] O. Sen, N.J. Gaul, K.K. Choi, G. Jacobs, H.S. Udaykumar, Evaluation of multiﬁdelity surrogate modeling techniques to construct closure laws for drag in 
shock–particle interactions, J. Comput. Phys. 371 (2018) 434–451, https://doi .org /10 .1016 /j .jcp .2018 .05 .039.
[80] P. Das, O. Sen, G. Jacobs, H.S. Udaykumar, Metamodels for interphase heat transfer from mesoscale simulations of shock–cylinder interactions, AIAA J. 
56 (2018) 3975–3987, https://doi .org /10 .2514 /1.J056982.
