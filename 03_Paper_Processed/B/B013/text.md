<!-- PDF_PAGE: 1 -->

Numerical investigation of a high pressure
hydrogen jet of 82 MPa with adaptive mesh
reﬁnement: The starting transient evolution and
Mach disk stabilization
Xinmeng Tang a,*, Makoto Asahara a, A. Koichi Hayashi b,
Nobuyuki Tsuboi c
a Faculty of Engineering/Graduate School of Engineering, Gifu University, 1-1 Yanagido, Gifu 501-1193, Japan
b Department of Mechanical Engineering, Aoyama Gakuin University, 5-10-1 Fuchinobe, Chuo-ku, Sagamihara,
Kanagawa 229-8558, Japan
c Department of Mechanical and Control Engineering, Kyushu Institute of Technology, 1-1 Sensui-chou, Tobata-ku,
Kitakyushu, Fukuoka 804-8550, Japan
article info
Article history:
Received 18 October 2016
Received in revised form
3 January 2017
Accepted 4 January 2017
Available online 6 March 2017
Keywords:
High pressure hydrogen jet
Adaptive mesh reﬁnement (AMR)
Starting transient
Under expanded
Mach disk stabilization
abstract
A three-dimensional (3D) strongly under expanded hydrogen jet ﬂow is numerically
investigated with a storage pressure of 82 MPa and a tiny jet oriﬁce diameter of 0.2 mm. The
full compressible Navier eStokes equations are utilized in a domain with a size of about
3 /C2 3 /C2 6 m which is discretized by employing adaptive mesh reﬁnement (AMR) technology
to reduce the number of grid cells. The highly under expanded hydrogen jet ﬂow with a
nozzle pressure ratio (NPR) of about 809 is then captured from the very beginning when
hydrogen is ejected out of the jet oriﬁce. The starting transient evolution and Mach disk
stabilization are then discussed in details. It is found that with the AMR technology, the
grid number can be greatly reduced and high resolutions can be easily installed to deal with
the small jet oriﬁce size together with those ﬂow microscales. Jet ﬂow is numerically
captured and discussed. It is found that over expansion occurs in this under expanded jet.
The secondary shock is generated to match the pressure which plays the most important
physics in the starting transient period of an under expanded hydrogen jet. The Mach
shock and the lateral barrel shock which are originated from the secondary shock play
central roles. The jet ﬂow is divided into subsonic and supersonic branches in the near-
nozzle region, which makes the highly under-expanded jets have two annular shear
layers, the inner and outer layer, in this region.
© 2017 Published by Elsevier Ltd on behalf of Hydrogen Energy Publications LLC.
Introduction
The use of hydrogen, which is clean, efﬁcient and versatile, as
a fuel for transportation and stationary applications is
receiving much favorable attention as a technical and policy
issue. Hydrogen gas is being explored for use in many ways
like internal combustion engines and fuel cell electric vehi-
cles. As reported in Ref. [1], for the future of the worldwide
* Corresponding author .
E-mail addresses: simondonxq@gmail.com, shimon@pku.edu.cn (X. Tang).
Available online at www.sciencedirect.com
ScienceDirect
journal homepage: www.elsevier.com/locate/he
international journal of hydrogen energy 42 (2017) 7120 e7134
http://dx.doi.org/10.1016/j.ijhydene.2017.01.016
0360-3199/© 2017 Published by Elsevier Ltd on behalf of Hydrogen Energy Publications LLC.

<!-- PDF_PAGE: 2 -->

energy supply three goals must be fulﬁlled: security in the
energy supply, environmental protection and the utilization
of energy sources that promote the economic growth of so-
cieties. Due to fundamental differences between hydrogen
and other common fuels, such as its wide explosion limits and
high diffusion properties, in case of a leakage, hydrogen can
reveal speciﬁc behaviors and be extremely dangerous. To
better understand and manage the security in the energy
application, the characters of the jet ﬂow ﬁeld on the hypo-
thetical scenario of dispersion and explosion are urgently
needed to persuasively determine the main design parame-
ters of the infra-structures.
The ratio of the nozzle total pressure ( p
0) to the ambient
(in-cylinder) static pressure ( p∞), namely the nozzle pressure
ratio (NPR), has a signiﬁcant effect on the characteristics of a
gaseous jet issuing from a circular nozzle. Because of the high
storage pressure, most researches of the hydrogen leak pat-
terns are faced with under-expanded jet ﬂow, of which NPR is
higher than 4. Most previous studies on under-expanded jets
have considered large diameter nozzles with air/nitrogen as
the working gas. There are very limited data in the literature
on under-expanded hydrogen jets (or other light gases such as
helium), especially for nozzles with small diameters. But as
the hydrogen has been drawing more and more attention,
nowadays both numerical and experimental investigations
are increasingly being worked out on the hydrogen jet with or
without ignition to capture the shock, vortices, mixing,
dispersion and ignition characteristics of hydrogen.
Ruggles and Ekoto [2] noticed that air and hydrogen may
have mixed within the slip region and bypassed the Mach
disk, therefore, notional nozzle theories which assumed that
all gas passed the Mach disk were not accurate enough. It was
suggested that more experimental and computational works
were required in order to clarify the hydrogen air mixing
behavior very close to the nozzle exit. Khaksarfard et al. [3]
investigated numerically the release of high pressure
hydrogen (10 e70 MPa) into ambient through a hole with
diameter d ¼ 5 mm. In Refs. [4e6], Hamzehloo et al. used large
eddy simulation (LES) to investigate the characteristics of
hydrogen under-expanded jets with different NPRs namely
8.5, 10, 30 and 70. They successfully captured the near-nozzle
shock structure, the geometry of the Mach disk and reﬂected
shock angle, the turbulent shear layer as well as hydrogen
penetration and distribution. In the serial studies on ignited
hydrogen jets by Schefer et al. [7,8], they performed experi-
mental measurements to characterize the dimensional and
radiative properties of large-scale, vertical hydrogen jet
ﬂames with different high pressures of 172 bar and 413 bar.
They found that the ﬂame length and radiative heat ﬂux
characteristics of these high-pressure jet ﬂames still obey
scaling laws developed for low-pressure, smaller-scale ﬂames
and a wide variety of fuels. In the experimental study by
Takeno et al. [9], they tested the dispersion and explosion of
high-pressurized hydrogen gas which leaked through a nozzle
of 10 mm diameters with 40 MPa pressure brown down to
atmosphere.
As these previous references note, the process of hydrogen
release from a high pressure vessel is accompanied with the
formation of complex shock structures, interface surface,
energy transport, diffusion and vortices. These ﬂow features
which need to be understood depend on many factors like the
storage pressure, the leakage size, the properties of the
ambient air like the pressure and wind speed, as well as the
space geometries. Sometime, when the storage pressure is
extremely high, it would be difﬁcult, dangerous and expensive
to carry out experiment of such hydrogen leakage test.
In this study, we calculate the full three-dimensional (3D)
NaviereStokes equations on an adaptive mesh using the
adaptive mesh reﬁnement (AMR) technology to capture the
ﬂow patterns of a hydrogen jet with a high storage pressure of
82 MPa. Then the NPR is 809.3 as the back pressure is set to 1.0
atmosphere pressure (atm). This study operates as a part of
the hydrogen security project of which the experimental part
has been performed by the Mitsubishi Heavy Industry (MHI)
company [10]. The pressure 82 MPa is chosen because it is one
of the regular storage pressure for hydrogen gas. A leak is
assumed through a small oriﬁce with a diameter of 0.2 mm.
And then in our study, numerically we get the unsteady ﬂow
from the initial transient start. As the calculation goes on, we
get the fully developed hydrogen jet ﬂow inside which nu-
merical ignition can be arranged to investigate the ignition
behavior of such a hydrogen leakage. These results would be
compared with experiments and theoretical analysis to get
some conclusions which can help the determination of the
safety standard.
This paper is mainly focused on discussion of the near-
nozzle characteristics, as the ﬁrst part of this study. The
Mach disk, reﬂected shocks, expansion fan, triple points,
vortex rings and the upstream of shear layers are located in
this zone. These ﬂow characteristics not only provide impor-
tant information regarding the upstream condition and
effective injection pressure, but also have signiﬁcant effect on
the annular shear layer thickness and consequently on the
mixing characteristics of the under-expanded jet. Meanwhile,
experimentally it is challenging to capture the full instanta-
neous 3D ﬂow patterns with the limited Schlieren-type pho-
tographs or sensors testing technologies. There are many
researches [4e6,11e14] in which the starting transient evolu-
tion and the near-nozzle region in under-expanded jets have
been discussed on many details such as shock series, the jet
structure formation time-scale as well as the spatial scale. Still
it is worth being paid more attention, especially for hydrogen
jet since few of the existing literatures are focused on such a
highly pressurized hydrogen and such a small jet oriﬁce size.
The paper is organized like this: ﬁrstly, the details of the
numerical frameworks will be presented, including the gov-
erning equations, the gas equations and the AMR framework.
Then it will come to the validation of the code by validation of
the height of Mach disk H
m as well as the jet tip penetration 's
linear relationship with the square root of time √t. Also, the
cost of CPU time and the beneﬁt from AMR mesh will be tested
and talked about. Finally, the starting transient evolution will
be discussed with the focus on the ﬂow ﬁeld near the small
oriﬁce, particularly about the shock series and physical
quantity variations around the Mach shock. Temperature
value valley, negative pressure gradient, Mach shock and
pressure oscillations, together with shear and mixing will be
discussed together with comparison with other available data.
After the Mach disk stabilization, the jet ﬂow comes to a new
period. Discussions will be presented on the location of Mach
international journal of hydrogen energy 42 (2017) 7120 e7134 7121

<!-- PDF_PAGE: 3 -->

disk, the triple point, the annular shear layer within the jet
volume together with the dispersion of hydrogen.
Numerical frameworks
Governing equations
The governing equation is the full compressible NaviereStokes
equations as
vQ
vt þ vE
vx þ vF
vh þ vG
vz ¼ vEv
vx þ vFv
vh þ vGv
vz þ S (1)
where t is the time, ðx; h; zÞ are the generalized curvilinear
coordinates. The aim of employing the equations in general-
ized coordinates is that we are to ﬁnally do the calculation of
such a jet in the cylindrical coordinates or with some obsta-
cles inside the ﬂow ﬁeld. Temporarily in this paper, the
physical domain is simpliﬁed as a cube and the Cartesian grid
can easily work, which may make the use of generalized co-
ordinates appear superﬂuous. It will play roles in the subse-
quent study. The conservation terms Q, E, F, G, E
v, Fv, Gv and
source term S in Eq. (1) for the generalized curvilinear co-
ordinates are, respectively, as
Subscript v here indicates viscosity terms. Density r is the
sum of densities ri ¼ rYi, where subscript i (i ¼ 1,/,9) indicates
the component i (H2,O 2, O, H, OH, HO 2,H 2O2,H 2O and N 2) and
Yi is the mass fraction of component i. These species are used
because the ignition behavior is also one of the concerns. The
source term from potential reactions is managed by a detailed
chemical model by Hong et al. [15] (it is now close in present
study but open later in this study). The convection term is
dealt in the MUSCL reconstruction together with AUSMDV
schemes [16] and the viscous term is discretized in the second
order central difference.u, v, w are the velocity components of/C13/C13V!/C13/C13in rectangular coordinates ( x, y, z), respectively. Their
resultant velocity is expressed by
/C13/C13V!/C13/C13, which will also be used
in the later discussion. Internal energy e in the equations is
speciﬁc to per unit density as
e ¼
X
9
i¼1
rihi /C0 p þ r
2
/C0
u2 þ v2 þ w2/C1
: (3)
Here hi indicates the enthalpy of component i. For ideal gas,
we have the thermodynamic quantities hi together with en-
tropy s, and speciﬁc heat at constant pressure cp,i expressed by
temperature T as
hi
RiT ¼ a1;i þ a2;i
2 T þ a3;i
3 T2 þ a4;i
4 T3 þ a5;i
5 T4 þ a6;i
T
si
Ri
¼ a1;ilnT þ a2;i T þ a3;i
2 T2 þ a4;i
3 T3 þ a5;i
4 T4 þ a7;i
cp;i
Ri
¼ a1;i þ a2;iT þ a3;i T2 þ a4;iT3 þ a5;iT4:
(4)
The coefﬁcients a1,i,/, a7,i are decided from the JANAF data
library [17] and checked by NIST [18] database.
J in Eq. (2) is the Jacobian determinant and the corre-
sponding Jacobian matrix is
J ¼
0
@
xx
hx
xy
hy
xz
hz
zx zy zz
1
A (5)
where these tensor components are transformation ratios
which are partial derivatives of coordinates belonging to the
computational system with respect to coordinates belonging
Q ¼ 1
J
0
BB
B
BBB
B
B
BB@
r
ru
rv
rw
e
r
i
1
CC
C
CCC
C
C
CCA
; E ¼
1
J
0
BB
B
BBB
B
B
BB@
rU
ruU þ x
x p
rvU þ xy p
rwU þ xzp
ðe þ pÞU
riU
1
CC
C
CCC
C
C
CCA
; F ¼
1
J
0
BB
B
BBB
B
B
BB@
rV
ruV þ h
xp
rvV þ hyp
rwV þ hz p
ðe þ pÞV
ri V
1
CC
C
CCC
C
C
CCA
; G ¼
1
J
0
BB
B
BBB
B
B
BB@
rW
ruW þ z
xp
rvW þ zyp
rwW þ zzp
ðe þ pÞW
riW
1
CC
C
CCC
C
C
CCA
;
E
v ¼ 1
J
0
BB
B
BBB
B
B
BB@
0
t
xx
txh
txz
txxu þ txhv þ txzw /C0 qx
/C0 _mxi
1
CC
C
CCC
C
C
CCA
; F
v ¼ 1
J
0
BB
B
BBB
B
B
BB@
0
t
hx
thh
thz
thxu þ thhv þ thzw /C0 qh
/C0 _mhi
1
CC
C
CCC
C
C
CCA
;
G
v ¼ 1
J
0
BBB
B
B
BBB
B
B@
0
t
zx
tzh
tzz
tzxu þ tzhv þ tzz /C0 qz
/C0 _mzi
1
CCC
C
C
CCC
C
CA
; S ¼
1
J
0
BBB
B
B
BBB
B
B@
0
0
0
0
0
_u
i
1
CCC
C
C
CCC
C
CA
:
(2)
international journal of hydrogen energy 42 (2017) 7120 e71347122

<!-- PDF_PAGE: 4 -->

to the physical system. U, V, W are the contravariant velocity
components in generalized coordinates ( x; h; z)a s
8
<
:
U ¼ xxu þ xyv þ xz w
V ¼ hxu þ hyv þ hzw
W ¼ zxu þ zyv þ zzw
(6)
The generalized shear forces in viscosity terms are
txx ¼ xxtxx þ xytxy þ xztxz
txh ¼ xxtyx þ xy tyy þ xz tyz
txz ¼ xxtzx þ xytzy þ xz tzz
thx ¼ hxtxx þ hytxy þ hz txz
thh ¼ hx tyx þ hytyy þ hztyz
thz ¼ hxtzx þ hytzy þ hz tzz
tzx ¼ zxtxx þ zytxy þ zztxz
tzh ¼ zxtyx þ zytyy þ zz tyz
tzz ¼ zxtzx þ zytzy þ zz tzz
(7)
and the generalized heat ﬂux vector and mass ﬂux vector are
qx ¼ xxqx þ xyqy þ xz qz
qh ¼ hx qx þ hyqy þ hzqz
qz ¼ zxqx þ zyqy þ zz qz
(8)
and
_mxi ¼ xx _mxi þ xy _myi þ xz _mzi
_mhi ¼ hx _mxi þ hy _myi þ hz _mzi
_mzi ¼ zx _mxi þ zy _myi þ zz _mzi
(9)
In Eq. (7) tij (i ¼ x, y, z; j ¼ x, y, z) are the nine components of
the viscous stress tensor
tij ¼ m
/C18vui
vxj
þ vuj
vxi
/C19
/C0 2
3 m
/C18vuk
vxk
/C19
dij (10)
where ui (i ¼ x, y, z) represents u, v, w, respectively. And xi (i ¼ x,
y, z) represents x, y, z, respectively. The viscosity coefﬁcient of
component i mi is expressed as the ﬁrst approximation of the
ChapmaneEnskog expansion of the Boltzmann equation[19] as
mi ¼ 2:6693 /C2 10/C0 6
ﬃﬃﬃﬃﬃﬃﬃﬃﬃ ﬃWi Tp
s2
i Uy
(11)
where Wi the molecular weight, si is the collision diameter,
and Uy is the collision integral obtained from the approximate
formula
Uy ¼ 1:147
/C18T
Tri
/C19/C0 0:145
þ
/C18T
Tri
þ 0:5
/C19/C0 2:0
: (12)
Here Tri is the reduced temperature (not the one which is
nondimensionalized by critical temperature) of component i,
which is related to the Lennard eJones potential well depth εi
together with the Boltzmann constant kB. And Trij can be
expressed
Trij ¼
ﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ
TriTrj
q
(13)
The dynamic viscosity m of the N (N ¼ 9) species mixture is
computed by Sutherland 's law
m ¼
XN
i¼1
mi
1 þ PN
j¼1;jsi 4ij
Xj
Xi
: (14)
Here in Eq. (14), Xj is the mole fraction of component i. 4ij is
a dimensionless constant obtained from the semi-empirical
formula by Wilke etc. [20] as
4
ij ¼
/C20
1 þ
/C16
mi
.
mj
/C171=2/C16
rj
.
ri
/C171=2/C0
Wi
/C14
Wj
/C11=4
/C212
2
ﬃﬃﬃ
2
p /C2
1 þ
/C0
Wi
/C14
Wj
/C1/C31=2 : (15)
These numerical frames of viscosities are adapted better
for low pressure gas. In this study, the gas pressure varies
among a large range from 42 MPa to around 1 atm. However,
the region of gas with high pressure is very small which is
located just next to the jet oriﬁce. The axial size of high
pressure region is only less than 1.0 mm, which will be shown
in details in the below section. What is more, for hydrogen m
H2
does not experience a ﬁerce variation when its pressure
changes. For instance, with a temperature of 250 K, mH2 is
7.9 /C2 10/C0 6 Pa s at 1 atm. As its pressure increases, mH2 presents
an approximately linear increase and slowly rises to
9.4 /C2 10/C0 6 Pa s at 42 MPa [18]. Therefore, through the gas
pressure varies greatly, the viscosity character is globally dealt
with Eqs. (11)e(15).
The second viscosity is not considered in the viscous stress
tensor t
ij.
In Eqs. (8) and (9) , qx, qy, qz are components of the heat ﬂux
vector and _mxi; _myi; _mzi are components of the mass ﬂux vector
in rectangular coordinates. These terms are expressed as
8
>>>
>
>
>
>
>
>>>
<
>>
>
>
>
>
>
>>>
>
:
q
x ¼/C0 k vT
vx /C0 r
X9
i¼1
Di hi
vYi
vx
qy ¼/C0 k vT
vy /C0 r
X9
i¼1
Di hi
vYi
vy
qz ¼/C0 k vT
vz /C0 r
X9
i¼1
Di hi
vYi
vz
(16)
and
8
>>
>
>
>
>><
>>
>
>
>
>
>
:
_m
xi ¼/C0 rDi
vYi
vx
_myi ¼/C0 rDi
vYi
vy
_mzi ¼/C0 rDi
vYi
vz
: (17)
where Yi is the mass fraction of component i, Di is diffusion
coefﬁcient of component i and k is mixture 's thermal con-
ductivity. Here Chapman and Cowling 's diffusion coefﬁcient
[21] frames are used which are
Dij ¼ 1:8829 /C2 10/C0 2
ﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ ﬃ
mijT3
p
ps2
ijUD
(18)
Di ¼ 1 /C0 Yi
P9
j¼1
Xj
Dij
(19)
where mij is the molar reduced mass, sij is the collision
diameter and UD is the diffusion collision integral [22e24].
The thermal conductivity k is obtained from the Wassil-
jewa equation [25].
k ¼
XN
i¼1
ki
1 þ PN
j¼1;jsi jij
Xj
Xi
; jij ¼ 1:0654ij (20)
where ki is dealt with Euken correction [26].
international journal of hydrogen energy 42 (2017) 7120 e7134 7123

<!-- PDF_PAGE: 5 -->

The 3-rd Runge-Kutta scheme [27] is adopted in the time
integration from Qn to Qnþ1:
Q1 ¼ Qn þ DtLðQnÞ
Q2 ¼ 3
4Qn þ 1
4Q1 þ 1
4 DtL
/C0
Q1/C1
Qnþ1 ¼ 1
3Qn þ 2
3Q2 þ 2
3 DtL
/C0
Q2/C1
(21)
where L is difference operator for spatial discretization.
For ideal gas calculation, simply the equation is
p ¼ rRT ¼
X9
i¼1
ri
R
Wi
T: (22)
where R is the gas constant for a speciﬁed gas and R is the
universal gas constant.
Flow conditions
A storage pressure p0 of 82 MPa is supposed for the hydrogen
jet. The pressurized hydrogen is injected into the atmosphere
air. In the calculation an acoustic injection boundary condi-
tion (BC) is used. It is just applied on the ghost cells in the axial
direction at the jet oriﬁce and then let the ﬂow develop. The
inlet physical parameters are computed assuming an isen-
tropic expansion and are listed in Table 1 together with the
atmosphere conditions.
According to the experimental result by Okabayashi et al.
[10], the maximum of velocity
/C13/C13V!/C13/C13
max in this high pressure jet
approximately has a relationship with the axial position l as
l /C2
/C13/C13V/C131!/C13/C13
maxz9:175 (on the condition that jet pressure is
82 MPa). But near the nozzle this relationship is not applicable.
To estimate the Reynolds number Re, we still have data that
m
airjp ¼ 1atm, T ¼ 287 K is around 17 /C2 10/C0 6 Pa s, rairjp ¼ 1atm, T ¼ 287 K
around 1.17 kg/m 3, mH2 jp ¼ 1atm, T ¼ 287 K around 8.7 /C2 10/C0 6 Pa s,
rH2 jp ¼ 1atm, T ¼ 287 K around 0.084 kg/m 3, mH2 jp ¼ 42 MPa, T ¼ 245 K
around 9.3 /C2 10/C0 6 Pa s, and rH2 jp ¼ 42 MPa, T ¼ 245 K around
31.1 kg/m3. One consideration that the pressure sharply drops
in a very short distance to only several atmosphere pressures,
take l roughly as the integral scale in Re and we can roughly
estimate the Re as
Re ¼
rl
/C13/C13V/C131!/C13/C13
max
m /C24
/C2
2:4 /C2 104 /C24 8:2 /C2 105/C3
: (23)
So the hydrogen jet we are faced with is a high Re ﬂow with
a Re on the order of 10 5. In a small region ( l¼ 0.2 mm) next to
the jet hole, Re is very higher due to the locally high density.
After that Re sharply decreases because of the drop of density
r (which is much faster than the rises of integral length l and
ﬂow speed
/C13/C13V!/C13/C13max). Downstream the Mach disk, Re recovers
slowly and comes to be nearly constant as 9.2 /C2 104 which is
from the global relationship l /C2
/C13/C13V/C131!/C13/C13
max z9:175.
Take Kolmogorov microscale mK and Taylor microscale l,
respectively, as
mK ¼ lRe/C0 3=4; (24)
l ¼
ﬃﬃﬃﬃﬃ ﬃ
10
p
lRe/C0 1=2 (25)
then it can be estimated that mK is as small as 7.34 /C2 10/C0 9 m
near the nozzle ( l ¼ 0.2 mm) while l is about 7 /C2 10/C0 7 m here.
After that these two microscales increase fast as Re decreases
and integral length l increases. At axial position l ¼ 1.0 mm, mK
rises to 5.0 /C2 10/C0 7 m and l to 2.0 /C2 10/C0 5 m.
Adaptive mesh reﬁnement
For this high pressure hydrogen jet, as the physical time t in-
creases, the hydrogen spreads to a large area due to the strong
expansion. The size of domain with a signiﬁcant hydrogen
concentration distribution can be of an order of meter. In the
injection orientation z, the hydrogen concentration isoline of
1% reaches as far as 6.0 m [10]. Accordingly, in our numerical
calculation, the computed domain is set to be around 3 m in x
and y directions, which are perpendicular to the jet direction,
and around 6 m inz direction. For the present ﬂow which is just
in the near-nozzle region in this paper, a size of 6 m is not
necessary. But for the ultimate goal of this hydrogen leakage
study, such a domain is helpful. These parameters exactly are
adjusted into 3.2768 m, 3.2768 m and 6.5536 m, respectively, in
the present calculation. It is really a big domain for 3D jet ﬂow
simulation. Besides, above we have estimated the Kolmogorov
microscale h
K. To capture the ﬂow patterns as accurate as
possible, we need very small mesh resolution at the vortices
zone. On consideration of this microscale, in a 3D big domain
the mesh scale would be too huge to be accepted.
To make the simulation feasible, an AMR technology is
installed on the computational mesh. Adaptive mesh technique
makes numerical simulation code self-conﬁguring by auto-
matically adjusting the accuracy of the simulation to a speciﬁed
level. With the adaptive mesh the set of data points is repeatedly
adapted during a run-time. Points are added or removed
to heuristically minimize the resource utilization while keeping
a required numerical accuracy on the ﬂow area where high
resolution is needed. We manage the adaptive mesh by PARA-
MESH package developed by P. MacNeice and K. M. Olson et al.
[28e30], which is being used in many ﬁelds [31e34] including
Magneto hydrodynamics, hydrodynamics, and so on.
By the AMR technology, the computed domain is divided
into thousands of subzones which are named blocks. These
blocks are of different levels and accordingly of different sizes.
Mesh points are located on these blocks with the same logical
structure. In this study, we set 10 mesh points in each direc-
tion on a block (8 physically working points and 1 layer of
auxiliary mesh at both ends). So for one block there are
1000 mesh points. Then blocks of different levels correspond
to different resolutions. Mesh size of blocks at level n þ 1i s
half that at level n. The higher the level of blocks is, the higher
would the mesh resolution be.
Table 1 e Hydrogen jet boundary condition (BC).
Inlet BC Freestream BC
de F 0.2 mm
Te 249 K T∞ 300 K
pe 43.2 MPa p∞ 1 atm
we 1220 m/s w∞ 0.3 m/s
Mae 1.0
Yi Y1 ¼ 1.0 (H 2) Yi Y2 ¼ 0.244 (O 2)
Y9 ¼ 0.756 (N 2)
international journal of hydrogen energy 42 (2017) 7120 e71347124

<!-- PDF_PAGE: 6 -->

Due to the use of the AMR strategy, the big physical domain
now does not necessarily cost much more for the present
study about the ﬂow in the near-nozzle region. Speciﬁcally,
initially we use 5522 blocks to cover the whole domain. Most
of the blocks are located near the oriﬁce and only about 400
blocks are used to cover the other parts of the domain. As the
ﬂow develops, more and more small blocks are assembled to
simulate the jet ﬂow. For instance, at t ¼ 40 ms, there are nearly
100,000 blocks in the AMR mesh system. Still, most of the
blocks are located in the region where ﬂow exists and only
about 400 blocks cover the other parts of the big 3D domain.
The cost of the mesh on the large parts where ﬂow tempo-
rarily does not exist is only 0.4% at this moment. Therefore, in
this way we can keep this big physical domain due to its small
time consumption (~0.4%). With it, the calculation can be
easily adapted to a long time run and meet the ultimate goal of
this project which is to investigate the transient hydrogen
distribution at 1.0 m or even 2.0 m.
To determine how many level should the adaptive mesh
has, two primary elements are considered in this study. On
one hand, we need to take care about the microscales. In this
respect, it is the near-nozzle zone which requires the highest
resolution among the big 3D physical domain. On the other
hand, we want to still use as few levels as possible since more
levels mean not only a larger amount of grid but also a smaller
time step Dt. In Ref. [11] by M. I. Radulescu and C. K. Law, they
used Euler equations and perfect gas model to perform 2D
numerical simulations to investigate the pressurized
hydrogen jet ﬂow ﬁeld during the initial stages. About the
number of injection grid points, they compared 1 grid point
per radius (/ r), 8 grid points/ r and 32 grid points/ r, where r is
the oriﬁce radius, and the results suggested that more details
could be captured with increasing resolution while a resolu-
tion of 8 grid points/r had already done quite well. In this study
we set the number of injection grid points to 16 grid points/ r.
Then, the resolution here is d/32 which comes to 6.25 mm. The
whole 3D domain of 3.2768 /C2 3.2768 /C2 6.5536 m is treated as
two blocks of level 1. The level of blocks with the resolution
6.25 mm is 17. With such a resolution, the time step now is of
an order of nano-second, which makes this calculation to be
very CPU consuming. It means that even with the AMR
strategy, the mesh still cannot reach the smallest Kolmogorov
microscale m
K which is as small as 7.34 /C2 10/C0 9 m at the jet
oriﬁce. Instead, the mesh can narrowly cover the Taylor
microscale l which is the intermediate length scale at which
ﬂuid viscosity signiﬁcantly affects the dynamics of turbulent
eddies in the ﬂow. In Ref. [11] by M. I. Radulescu and C. K. Law,
for extremely high NPR jet the ﬂuid viscosity was neglected
and they still get a very good result about the transient start
evolution in the near-nozzle region. Variations of basic
physical variables like p and T as well as shock structures were
discussed in details. These above imply that the present mesh
resolution is a compromise which can generally get the pri-
mary ﬂow result. But with such resolutions, the vortices de-
tails cannot be discussed persuasively.
We control the AMR to place blocks of level 17 on the near-
nozzle zone to accomplish the initialization of simulation
mesh. The initial AMR mesh for this 3D calculation is shown in
Fig. 1. The highest resolution is located on the injection oriﬁce
at (0, 0, 0). Since in the beginning there is no ﬂow development
in the other region, only coarse grids on blocks of low level are
installed in these zones. By doing this, in such a big 3D domain
we can do a high resolution simulation with a small amount of
grids. In Fig. 1 (a) there are only about 5000 blocks, as
mentioned above.
As the ﬂow jet develops, the code needs to automatically
adapt the mesh to the resolution requirement according to the
ﬂow ﬁeld situation. To control this process, six reﬁnement
criterions are used to decide the gradients of ﬂow, which are
VY
H2 , V
/C13/C13V!/C13/C13, V /C2 V/C131!, l2 of S2 þ U2, VT and VYH2 O2 . Here S is the
strain tensor of the ﬂow and U is the rotation rate tensor. Q2
can have the same effectiveness as l2 in this study. For V /C2 V/C131!,
one of the three norms of it is used. In our actual run the
inﬁnite norm is used.
If the gradients are big enough, higher levels of blocks will
be installed to satisfy the resolution requirement. There are
many approaches to do gradients test [35e38]. And it signiﬁ-
cantly affects how efﬁcient the code can perform. These six
criterions are used because that in this under-expanded
hydrogen jet, they are the optimal ones to deal with a
certain side of the ﬂow pattern. VY
H2 is the best one to capture
the distribution and mixing of hydrogen. V
/C13/C13V!/C13/C13and VT can
help get the variation of these main physical quantities such
as V/C131!, p, T, Ma. As for V /C2 V/C131! and l2 of S2 þ U2, they are used to
mark the shear layers and mixing zones. As to the last one
VY
H2 O2 , it is assembled to test where the chemical reaction
happens and mark it to assure that a good resolution is used
for the chemical reaction simulation. In the primary stage of
the study, as this paper is focused on the near-nozzle zone,
this reﬁnement criterion is temporarily closed.
The effectiveness of these reﬁnement criterions will be
shown below in Section “Results and discussion ”.
Results and discussion
Veriﬁcation and CPU cost
To verify the program, a serial cases of different scales were
calculated and compared with the available data. Among
them, a 2D jet ﬂow with a jet pressure of 2 MPa is simulated
both on an AMR mesh and on a uniform mesh. Numerical
results are in a good agreement on these two meshes. As the
jet ﬂow develops, the Mach disk forms at a certain location
downstream the jet oriﬁce. The height of Mach disk H
m in the
2D jet comes to be very close to the theoretical position of
Mach disk by R. T. Driftmyer et al. [39] which is expressed as
lM
de
¼ 1
j þ 1
/C18gMaepe
p∞
/C191
jþ1
ðgMaeÞ j/C0 1 ðj ¼ 0 for 2D Þ (26)
where the heat capacity ratio g is taken as 1.4 and Mae as 1.0.
For the 3D jet, the height of Mach disk Hm is also widely
investigated and it is found to be in a direct proportion to the
oriﬁce diameter d and the square root of NPR [40]. According to
the commonly used experimental correlation for H
m proposed
by Ashkenas and Sherman [41], in particular, within the range
15 < p0/p∞< 17,000, Hm is supposed to be at
Hm ¼ d /C2 0:67 /C2
ﬃﬃﬃﬃﬃﬃp0
p∞
r
(27)
international journal of hydrogen energy 42 (2017) 7120 e7134 7125

<!-- PDF_PAGE: 7 -->

From Eq. (27), Hm is supposed to be 3.81 mm when
ﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ
p0=p∞
p
is 809.3 and d is 0.2 mm in this study. A 3D jet was calculated
with the formal conditions. As the solution is advanced, Mach
disk formed at the expected location, as shown in Fig. 2, with a
difference of 1%. The averaged Mach disk height Hm is about
3.78 mm from the numerical results. The slight underestimate
value may be due to the use of the ideal gas EOS, which is also
reported in the research by Bonelli F. et al. [42].
The jet tip penetration ( Z
tip) is one of the key properties of
under-expanded gaseous fuel jets. It characters how far the
hydrogen spreads. There are many data or expressions to be
compared with. By many literatures [43e48] it has been
pointed out that the jet tip penetration Z
tip is supposed to be in
a linear relationship with the square root of time √t. One of
the analysis is expressed by Hill and Ouellette [45] as
Ztip ¼ G
/C18M
r∞
/C190:25 ﬃﬃ
t
p
(28)
where M is the momentum ﬂow rate supplied by the nozzle
and G is a scaling constant related to the entrainment level.
According to the numerical results, Ztip is 0.93 mm at 0.5 ms,
1.50 mm at 1.0 ms, 45.10 mm at 176.0 ms and 70.01 mm at
360.0 ms, etc., as shown in Fig. 3 . Over all, the jet penetration
with the conditions in this study obeys an approximatively
linear dependency on the square root of time √t while in the
initial transient period it experiences a little faster rise than
Fig. 1 e Initial AMR mesh for the present 3D hydrogen jet calculation. (a) The domain sizes in three Cartesian directions are
3.2768 m, 3.2768 m and 6.5536 m, respectively. (b) The blue parts on the mesh denote the injection oriﬁce with a diameter of
0.2 mm. The mesh in the near-nozzle region has been prepared to advance the coming jet and are zoomed in and illustrated
here on planes z ¼ 0 (middle), (c) y ¼ 0 (right upper) and x ¼ 0 (right below). Black lines indicate individual mesh cells while
red lines express numerical block edges. 17 levels AMR are installed. (For interpretation of the references to colour in this
ﬁgure legend, the reader is referred to the web version of this article.)
Fig. 2 e Experimental correlated Mach disk height Hmby
Ashkenas et al. and Hmin this study.
Fig. 3 e The jet tip penetration Ztip variations with the
square root of time √t. Red marks are the numerical Ztip at
different t. the black dotted line is the ﬁtted line of these
data points. (For interpretation of the references to colour
in this ﬁgure legend, the reader is referred to the web
version of this article.)
international journal of hydrogen energy 42 (2017) 7120 e71347126

<!-- PDF_PAGE: 8 -->

the linear dependency on √t. This former linear dependency
on √t is just as the reported relationship in these literatures
[43e45]. As to the nonlinear part in the initial transient period,
the experiments have also shown this initial non-linear
transient behavior [49].
As mentioned above in Section “Numerical frameworks ”,
the computed domain is divided by the AMR technology into
tens of thousands of blocks and on each block there are
10 /C2 10 /C2 10 mesh points, of which 8 layers are physically
working points and 2 layers are auxiliary points. Because of
this mesh structure, some communication processes are
needed to make the AMR mesh works. Firstly, we need set the
values of these 2 layers of auxiliary points according to the
neighboring blocks. Secondly, the gradients needed to be
tested to adapt the mesh to the ﬂow. Thirdly, the information
between old and new mesh should be transferred. All of these
three operations add an additional CPU cost to the calculation
on this AMR mesh.
When the time advance begins, as the ﬂow develops, more
mesh points are gradually arranged on the AMR mesh. For
example, at t ¼ 10 ms, the amount of blocks comes from initial
5000 to around 50,000 which is 50 million mesh cells. At this
point we measured the CPU costs of these procedures. If we
mark the regular advance on the ﬁxed mesh as I, the advance on
AMR mesh as II, and the additional CPU cost for AMR mesh III as
shown inFig. 4, then in the case of serial run, on Fujitsu SPARC64
XIfx (2.2 GHz) processor the process III totally costs 145 ms
(guardcell ﬁlling 100 ms, gradient test 18 ms and grid restruction
27 ms) while II costs 1280 ms. The test suggests that cost of III is
only 12% of that of II. The cost of I depends on the amount of
ﬁxed mesh. Usually with AMR the mesh points number can be
reduced to around 20% or even 1% of the number with ﬁxed
mesh, which means the cost of II can be much smaller than that
of I. In general, though additional operation III is needed, AMR is
still beneﬁcial for speeding up calculation, especially for those
problems in which the main physical variations are centralized,
like shocks or detonations, so that AMR can use much less mesh
points than the ﬁxed mesh.
The program is run with a ﬂat MPI mode on Nagoya FX100.
As for the scaling of the speed-up ratio of MPI with different
numbers of processors, as reported by D. M. Kelly et al. [50],i t
is initially almost ideal (linear) but gradually deteriorates for a
larger number of processors. For instance, when 1024 and 320
processors are used (the ratio of CPU numbers is 3.2), the ratio
of the simulation speeds is 2.583. The scaling is not 1.0 but
0.807. It has some loss but is still substantial. Mainly the
program is now computed with 1024 processors.
Starting transient evolution
The details of the initial transient for large pressure ratios and
strong shocks, which are still poorly understood since exper-
imental investigations are usually limited to phenomenolog-
ical descriptions based on Schlieren-type photographs and
have difﬁcult to make an accurate appraisal of the 3D ﬂow
ﬁeld, are numerically captured by the calculations here. When
the pressurized hydrogen jets out from the small oriﬁce, it
develops into a supersonic jet with a leading shock which is
marked as ① in Fig. 5(a), (b) and (c). The leading shock spreads
downstream and as it passes by, local T, r, as shown in Fig. 5(b)
and (c), and p increase due to its compression. In the very
beginning of the jet the leading shock is very strong. The
temperature spike can rise to over 1500 K. As the leading
shock continues spreading, due to the spatial weakening ef-
fect from the quick rise of its volume, it becomes weaker as it
propagates. Accordingly, it shows smaller rises on T, r and p.
In Fig. 5(c), temperature is increased to 547 K, which is not very
high, by the leading shock at t ¼ 2.4 ms.
Besides the leading shock, there are other shocks which in
many respects are more important for the ﬂow patterns of this
under-expanded jet. When the jet starts and the pressurized
hydrogen sprays out, the Prandtl-Meyer expansion fan
strongly affects the jet ﬂow at the nozzle lip. Both pressure
and temperature dramatically fall while
/C13/C13V!/C13/C13and Ma sharply
increase. The static pressurized hydrogen sprays out from the
oriﬁce with a static pressure of over 40 MPa and immediately it
experiences a sharp decrease and the front pressure changes
to p
expons. In the very beginning (of nanosecond order in this
study) pexpons is still not too small and the pressure gap at the
expansion front is not so large. In a short instantaneous time
p
expons continues to fall sharply. Axially in less than 1 mm
downstream the nozzle exit, about 0.7 mm as shown in Fig. 6,
the pressure falls to be even below 1 atm. This geometrically
imploding expansion wave reduces the pressure at a faster
rate than a corresponding diverging curved shock, hence an
inward moving weak shock wave is required to match the
pressures [51]. This is the secondary shock wave, which pre-
sents as the boundary of the main expansion region and can
be clearly seen in Fig. 5 (a), (b) and (c), marked by the sharp
gradients of T, r and p. It is the origin of the Mach shock and
the lateral barrel shock, marked as ③ and ④ in Fig. 5 . The
secondary shock initially appears near the nozzle lip, where
the gases are expanding in multiple dimensions. The inward-
facing Mach shock is converted outwards by the supersonic
outﬂow while the barrel shock remains attached to the
expansion corner (nozzle borderline).
As the calculations are advanced, the over expansion core
with the Mach shock and the lateral barrel shock as its
signature continue developing. The pressure of the ambient
gases works as a compression fan and pushes the jet espe-
cially the lateral barrel shock back toward the z-axis. As
shown in Fig. 5 (a) and (b). The results, especially Fig. 5 (d),
suggest that the ﬂow structure can be simply divided into two
parts: the ﬂow branch which goes through the Mach shock
and the other gas which bypasses the Mach shock. The later
one makes the barrel shock cannot be used to represent the
lateral boundary of hydrogen species. In different ﬂow periods
Fig. 4 e Schematic of the CPU hour costs of using ﬁxed
mesh and AMR mesh. I: cost of ﬁxed mesh cells; II: cost of
reduced AMR mesh cells; III: additional cost with AMR.
international journal of hydrogen energy 42 (2017) 7120 e7134 7127

<!-- PDF_PAGE: 9 -->

these two ﬂow branches play different roles. With such a
partition it can be easier to discuss the evolution of the ﬂow
from the initial transient start.
Similar structures at the transient start of a highly under-
expanded jet are numerically and experimentally presented
in many other literatures like [11,14,52e54]. These results
show the formation of the Mach shock and the lateral barrel
shock well in details which are in good agreements with the
above discussion, for instance Fig. 5 (a), which is originated
from the experimental result of Naboko et al. [54].
Hydrogen species spreads with the jet. Most of the
hydrogen axially passes through the Mach shock, as shown in
Fig. 5 (a) and (b). Hydrogen that crosses the Mach shock is
compressed and heated while its velocity is reduced from
highly supersonic to subsonic, as shown in Fig. 5(c) and (d). At
the jet interface marked as ②, a mixing occurs, but primarily
Fig. 5 e Sketch of the transient start of the under-expanded jet based on H 2 distribution, shocks and vortex adapted from
Ref. [11] and YH2 , T,
/C13/C13V!/C13/C13contours together with p, r, Ma isolines on x ¼ 0 plane at t ¼ 2.4 ms. (a) sketch of the transient start of
the under-expanded jet; (b) YH2 contours together with p isolines; (c) T contours together with r isolines; (d)
/C13/C13V!/C13/C13contours
together with Ma isolines. ①: leading shock; ②: Jet interface; ③: Mach shock; ④: barrel shock; ⑤: shocklets; ⑥: Vortex ring.
Isolines are in the dotted shape. Black dash lines in (b) and (c) indicate the sonic lines.
international journal of hydrogen energy 42 (2017) 7120 e71347128

<!-- PDF_PAGE: 10 -->

the hydrogen gas is spreading downstream. Also, there is a
certain distance between the leading shock and the contact
surface. The leading shock heats the gas as it passes by and at
the very beginning when it is very strong temperature can rise
to over 1500 K. Nevertheless, the mass convection is slower
than the shock speed and therefore the region with this high
temperature has no hydrogen species. Besides, as shown in
Fig. 5(c), temperature experiences a valley value just at the jet
interface ②. When we go back to the very beginning of the jet,
it can be found that this low temperature surface originates
from the very moment when the secondary shock forms. The
secondary shock does not recover all the expansion region but
just the core. The outer part of the expansion region keeps
developing in front of the secondary shock at a relatively low
temperature. As the hydrogen spreads, gradually this region
will be covered by the heated hydrogen and this small tem-
perature valley will be no more. But in the starting transient it
is notable as shown in Fig. 5(c) where temperature is relatively
low just near the contact surface. Besides, the instability on
the contact surface causes a lateral velocity of about 20 m/s,
which also affects the temperature. These discussions above
imply that for jets in an open space the heating of the leading
shock cannot directly affect the hydrogen eair mixture and
cannot cause any auto-ignition.
In this early stage, there is no other ﬂow branch in the re-
gion between the Mach shock and the leading shock except
the main one which goes through the Mach stock. Besides,
now the leading shock is relatively strong. Therefore, there is
an axially negative pressure gradient, as shown in Fig. 6 ,i n
this zone. The local speed here gradually decreases spatially
as hydrogen expands. The same process can be concluded in
the 2D jet simulation in Ref. [11] by M. I. Radulescu and C. K.
Law. It can be also explained in the following way: the Mach
shock adjusts the ﬂows on its two sides. The stream gets a
new pressure together with a new ﬂow velocity (pressure
varies together with ﬂow velocity) after it goes through the
Mach shock. Because of the different sonic speeds in hydrogen
and air, here just behind the Mach shock the new velocity is
higher than that of the ﬂow ﬁeld downstream where the
leading shock just passes. Correspondingly, the new pressure
is smaller. In this respect, the total pressure loss is very large
in this ﬂow branch which goes through the Mach shock.
In the next stage after the Mach disk forms at a semi-steady
location (with a slight oscillation back and forth along the z
axis), this phenomenon is no more, as shown in Fig. 6 with
the pressure variations at 37 ms, 40 msa n d4 2 ms, since the ve-
locity ﬁeld at that period is greatly changed by the other ﬂow
branch. At that stage the supersonic ﬂow bypasses the Mach
disk and ﬂows into the region which is located axially down-
stream the Mach disk, which will be discussed below.
The dashed line in Fig. 6 marks the locations of the contact
surface at each time. Pressure oscillations can be seen on
these pressure lines upstream the contact surface and
downstream the Mach shock before Mach shock stands as the
Mach disk. Above we have mentioned the instability on the
contact surface which causes a lateral velocity of about 20 m/
s. The tip of the hydrogen jet spreads into the cold air and it
causes some slight instability oscillations on the pressure as
shown in Fig. 7 (while it causes big jumps on temperature,
mass fraction of H
2, and velocity together with density). The
curvature effect of these pressure isosurfaces strengthens the
oscillation. Beside this cause, there is another important issue
that appends to the pressure oscillation. As the jet gas espe-
cially the lateral barrel shock bends toward the z-axis, the
ﬂuctuant pressure in its ﬂow directions affects the region
marked as c in Fig. 7 (b). After this bend ends when the Mach
disk forms, this effect is no more and consequently the pres-
sure oscillation minimizes as what the pressure variations at
37 ms, 40 ms and 42 ms show in Fig. 6.
Important vortices occur in this ﬂow branch as shown in
Fig. 7(a). On the tip there are counter rotating vortices marked
as b due to the velocity push from the jet which goes through
the Mach shock. Similar structures are reported in Ref. [6]. But
as mentioned above, the ﬂow speed is subsonic here. Hence
the vortices here become slower than the primary vortex ring
a on the tip of the supersonic ﬂow branch which originates
from the bend of the lateral barrel shock toward the z-axis.
Later vortices b will be covered by a. This causes that in a
period of time the maximum tip penetration will not be on the
centerline. In this study this deviation of the maximum tip
penetration from that on the centerline happens from 17 mst o
43 ms This deviation is also reported by Hamzehloo et al. [6] in
a hydrogen jet with a NPR as 10. With this NPR and d ¼ 1.5 mm,
the deviation begins at 12 ms.
The barrel shock cannot be used to represent the lateral
boundary of hydrogen species, as mentioned above. Besides
the hydrogen proﬁle which axially passes through the Mach
shock, there is the other part of hydrogen which ﬂows in the
region between the lateral barrel shock and the jet boundary
(named as slip region in some literatures like Ref. [4]). The
sonic lines marked by black dash lines in Fig. 5(b) and (c) can
approximatively indicate the lateral hydrogen boundary in the
near-nozzle region. Ruggles and Ekoto [2] have noticed the
importance of the ﬂow of this part when they tried to do far
ﬁeld reconstructions with various notional nozzle models to
account for complex jet exit shock phenomena and found
Fig. 6 e Axial pressure variations between the Mach shock
and the leading shock at different times. MS: Mach shock;
LS: leading shock; MD: Mach disk.
international journal of hydrogen energy 42 (2017) 7120 e7134 7129

<!-- PDF_PAGE: 11 -->

signiﬁcant mismatching with experimental ﬁndings. They
tried to explain this mismatching and found that in the
hydrogen jet, air and hydrogen may have mixed within the
slip region and bypassed the Mach disk, and therefore,
notional nozzle theories which assumed that all gases passed
the Mach disk were not accurate enough. It suggests that it is
important and needy to do further clariﬁcation of the
hydrogen-air mixing behavior very close to the nozzle exit.
In the early stage, the ﬂow of hydrogen of this part also play
a signiﬁcant role. Here some shocklets exist which have the
same origin with the barrel shock and Mach shock. The ﬂow is
supersonic in this region since no more shock is included here
except the shocklets downstream. That is why previously it
has been mentioned that the sonic lines can roughly indicate
the lateral hydrogen boundary in the near-nozzle region. The
ﬂow shear is strong here due to the velocity gradients. Its
absolute vortex magnitudes are signiﬁcant, as shown in Fig. 8,
on this shear layer as well as on the primary vortex ring. A
certain degree of mixing happens here. But because of the
high Re, such mixing is very limited. As the lateral barrel shock
bends toward the z-axis, the vortex ring marked as ⑥ in Fig. 5
occurs and greatly advances the mixing here. It plays a main
role in the early transient stage for mixing.
Mach disk stabilization
In the previous section the transient start of the jet has been
discussed. It can be seen that the secondary shock plays the
most important role in this period. The Mach shock and the
lateral barrel shock, which are originated from the secondary
shock, play central roles in the evolution of the jet and the
ﬂow is divided into subsonic and supersonic branches.
Consequently, the primary vortex appears to demonstrate
some vortices behavior together with shear and mixing.
After the Mach disk forms, the evolution of the ﬂow pat-
terns in the near-nozzle exit almost ﬁnishes and the jet ﬂow
comes to a new era during which the vortices instead of
shocks become the main character.
As mentioned previously, the barrel shocks converge due
to the compression fan originated from the jet boundary.
Because of the high jet pressure and accordingly the strong
incident shocks with small reﬂection angle q, Mach reﬂection
instead of regular reﬂection occurs [55]. At about t ¼ 20 ms, the
evolution of jet has come to a dynamically stable state, as
shown in Fig. 9 . Because of the high NPR, the Mach disk be-
comes convex. From Fig. 6 , which shows the axial pressure
variations at different times, it can be seen that at t ¼ 37 ms,
40 ms and 42 ms the Mach disk comes out at the expected po-
sition around 3.8 mm while it slightly oscillates back and forth
along the z axis in a small range. This oscillation is also
observed in the experiment performed by MHI company [10].
The elapsed time t
disk, which is the time from the hydro-
gen's entrance into the domain to the Mach disk stabilization,
obtained numerically here for this jet is of the same order
with the reported t
disk of under-expanded hydrogen jets. In
Fig. 7 e Hydrogen distribution and pressure contours at t ¼ 8.9 mso n x ¼ 0 plane. a: primary vortex ring; b: counter rotating
vortices. Black lines illustrate the AMR block edges.
Fig. 8 e Absolute vortex contours at t ¼ 2.4 ms.
international journal of hydrogen energy 42 (2017) 7120 e71347130

<!-- PDF_PAGE: 12 -->

this respect it is notable that the NPR is much higher while
the elapsed time tdisk for Mach disk formation is similar to
these jets with low NPR. For example, in Ref. [5] by Ham-
zehloo et al., at the hydrogen jets with NPR ¼ 10, p∞ z 5 bar,
d ¼ 1.5 mm, the tdisk for Mach disk formation is about 19 ms
When p∞ becomes to 1 bar, tdisk increases to about 22 msI na
case for methane, tdisk is also reported to be of the similar
order. It can be seen that with such different NPRs, which are
8.5, 10 and 809.3 here, and such different nozzle sizes, which
are 1.5 mm and 0.2 mm, the elapsed time t
disk for Mach disk
formation is similar. Considering the non-dimensional co-
ordinates, the nominal integral time scales issued from a
circular nozzle deﬁned as t
0 ¼ d=2
/C13/C13V!/C13/C13are much different in
these cases mentioned above. It is 2.4 ms in Ref. [5] while
7.7 /C2 10/C0 2 ms in the present study. Hence it is not very helpful
to explain the similarity of tdisk. Since in these cases, they
have a similar Re about 5.0 /C2 105 to 1.0 /C2 106, it can be spec-
ulated that maybe this similarity of tdisk may have a certain
relationship with the ﬂow jet Reynolds number. What the
mechanism is like would be an interesting and important
problem which needs to be further studied.
Fig. 10 shows the quantity variations of T, p,
/C13/C13V!/C13/C13, and Ma
along the z axis correspondingly to Fig. 9. The sharp decrease
of (a) T and (b) p can be found in the potential core where the
boundary is identiﬁed by the Mach disk. The location of Mach
disk is clearly seen. It can be found that the Ma now keeps
rising to as high as 14 while the velocity, in fact, does not
accordingly increase too much after it reaches 2500 m/s. The
rise of Ma is mainly due to the low temperature and its
accompanying low sound speed. Gas in zone B in Fig. 9 ﬂows
with a subsonic speed of around 800 m/s, temperature around
290 K and a normal pressure about 1 bar. The over expansion,
which is recovered by the Mach disk, also can be seen in the
pressure variation in Fig. 10(b).
In this period the ﬂow which bypasses the Mach disk plays
a more important role. The shocklets evolve into the reﬂected
shock and this ﬂow region becomes the peripheral supersonic
jet. Coupling with the Mach disk and the barrel shock, the
reﬂected shock together with the shock triple point is stand-
ing, as shown in Fig. 9, which are marked as 1 and A, respec-
tively. The supersonic ﬂow which bypasses the Mach disk
goes through this reﬂected shock and experiences some
certain physical quantity variations while it still keeps su-
personic. It shears strongly with the subsonic ﬂow in zone B
which passes through the Mach disk and receives some other
physical quantity variations. The extents of variation are
different in these two ﬂow branches. Therefore, downstream
the triple shock point a slip line (surface in 3D) occurs due to
the contact discontinuity, marked as 2 in Fig. 9.
As the time goes on, the jet ﬂow develops and spreads
downstream with both the subsonic and supersonic branches.
They contact at the slip surface, affect and transfer ﬂow pat-
terns to each other. The slip line shows the existence of an
annular shear layer within the jet volume. Therefore, highly
under-expanded jets have two annular shear layers, the inner
and outer layer [56,57]. The inner shear layer lies between the
peripheral high-velocity ﬂow and the low-velocity jet core,
while the outer shear layer (or the mixing layer) lies within the
jet boundary and the surrounding medium. The slip surface
will become weaker and after a certain distance the super-
sonic and subsonic gas branches merge into one ﬂow. During
this time, the
/C13/C13V!/C13/C13along the z-axis increases to a certain value,
say about 1000 m/s, and then decreases. The location of the
position where two gas branches merge into one ﬂow can be
seen in Fig. 11 , marked by the merging of these sonic lines,
which is about 12 mm downstream of the jet nozzle. Inside
this main ﬂow where the interactions of these two ﬂow
branches happen, there is still now no mixing process since
Y
H2 along the z-axis is 1.0. The mixing happens now mainly on
the outside of the ﬂow with a lot of shear vortices.
The AMR blocks are also illustrated in Fig. 11 . In the jet
oriﬁce region, Lv. 17 blocks of which the grid size is 6 mm, are
used and downstream the levels are reduced to Lv. 16, 15 or 14.
Hence mainly the hydrogen mass fraction downstream the
Fig. 9 e The near-nozzle shock structures at t ¼ 20.0 mso n x ¼ 0 cross section. Ma contours are shown on the top half and
below are velocity contours with Ma isolines. ③: Mach disk; ④: barrel shock; 1: reﬂected shock; 2: slip line; A: shock triple
point; B: subsonic zone behind the Mach disk. The black dotted line indicates the z axis.
international journal of hydrogen energy 42 (2017) 7120 e7134 7131

<!-- PDF_PAGE: 13 -->

Mach disk is captured with Lv. 14 blocks with a corresponding
resolution of 48 mm. Even so, for the 3D jet the amount of the
mesh points are still very large. In this respect, the AMR
technology is very necessary to deal with this 3D jet simula-
tion and a good control of the AMR mesh adaption according
to the transient ﬂow patterns would be very helpful and
important to get the detailed calculation faster.
Further calculation is being run to investigate the charac-
teristics of hydrogen penetration with longer injection dura-
tions (thus over longer distances), e.g. for hydrogen safety
considerations and to make a further comparison with the
corresponding experiment performed by MHI company.
Conclusion
The under expanded hydrogen jet ﬂow with a storage pressure
of 82 MPa and an oriﬁce diameter of 0.2 mm is investigated
and discussed from t ¼ 0t o t ¼ 48.0 ms During this time the
hydrogen jet experiences the starting transient evolution and
the Mack disk stabilization period. Many ﬂow patterns are
explained in details including the secondary shock, subsonic
and supersonic ﬂow branches, temperature value valley,
negative pressure gradient, pressure undulations, as well as
Fig. 10 e Primitive quantity variations along the z axis at t ¼ 20.0 ms. (a) T; (b) p; (c)
/C13/C13V!/C13/C13; (d) Ma.
Fig. 11 e Distribution of Hydrogen on x ¼ 0 plane at
t ¼ 48.0 ms. Black squares indicate the AMR mesh blocks.
On each block there are 10 £ 10 £ 10 mesh points. Black
dash lines illustrate the sonic lines.
international journal of hydrogen energy 42 (2017) 7120 e71347132

<!-- PDF_PAGE: 14 -->

annular shears and mixing. Some notable ﬁndings are also
speciﬁed. These main conclusions of this work can be sum-
marised as follows:
C the AMR technology can greatly reduce the number of
grid cells while just causes a small additional procedure
cost. A good control of the AMR mesh adaption ac-
cording to the transient ﬂow patterns would be very
helpful and important to get the calculation faster.
C The extremely high pressure hydrogen is expanded
by intense Prandtl-Meyer expansions. At about 0.7 mm
the pressure falls to be below 1 atm, which means over
expansion occurs in this under expanded jet. The sec-
ondary shock wave is generated to match the pressure
ﬁeld. It is the very origin of Mach shock and the lateral
barrel shock. Mach disk forms at the excepted location.
The jet penetration obeys an approximatively linear
dependency on the square root of time √t while in the
initial transient period it experiences some faster rise
than the linear dependency on √t, which is just as re-
ported in available literatures.
C With such different NPRs, which are 8.5, 10 and 809.3,
and such different nozzle sizes, which are 1.5 mm and
0.2 mm, the elapsed time t
disk for Mach disk formation is
similar. The similarity of ﬂow jet Reynolds number may
help explain this phenomenon. What the mechanism is
like would be an interesting and important problem
which needs to be further speciﬁed.
C Jet ﬂow can be simpliﬁed into two parts: the ﬂow branch
which goes through the Mach shock and the other part
which bypasses the Mach shock. In the ﬂow branch
which goes through the Mach shock, axially there is
a short-term negative pressure gradient, which in-
dicates that the total pressure loss is very large in this
ﬂow branch which goes through the Mach shock. The
supersonic ﬂow which bypasses the Mach disk goes
through this reﬂected shock and gets some certain
physical quantity variations while it still keeps super-
sonic. It shears strongly with the subsonic ﬂow which
passes through the Mach disk and gets some other
physical quantity variations. The variations extents are
different in these two ﬂow branches. So downstream of
the shock triple point there exists an annular shear
layer within the jet volume.
Acknowledgements
This project is under the support of NEDO (the New Energy
and Industrial Technology Development Organization) with
the guidance of JPEC (the Japan Petroleum Energy Center), to
whom we want to express our particular appreciation. The
PARAMESH software used in this work was developed at the
NASA Goddard Space Flight Center and Drexel University
under NASA 's HPCC and ESTO/CT projects and under grant
NNG04GP79G from the NASA/AISR project. We also thank
Cybermedia Center of Osaka University and the Information
Technology Center of Nagoya University for the supercom-
puter supports.
references
[1] Marb/C19an G, Vald /C19es-Solı´s T. Towards the hydrogen economy.
Int J Hydrogen Energy 2007;32:1625 e37.
[2] Ruggles AJ, Ekoto IW. Ignitability and mixing of
underexpanded hydrogen jets. Int J Hydrogen Energy
2012;37:17549e60.
[3] Khaksarfard R, Kameshki MR, Paraschivoiu M. Numerical
simulation of high pressure release and dispersion of
hydrogen into air with real gas model. Shock Waves
2010;20:205e16.
[4] Hamzehloo A, Aleiferis PG. Large eddy simulation of highly
turbulent under-expanded hydrogen and methane jets for
gaseous-fuelled internal combustion engines. Int J Hydrogen
Energy 2014;39:21275 e96.
[5] Hamzehloo A, Aleiferis PG. Gas dynamics and ﬂow
characteristics of highly turbulent under-expanded
hydrogen and methane jets under various nozzle pressure
ratios and ambient pressures. Int J Hydrogen Energy
2016;41:6544e66.
[6] Hamzehloo A, Aleiferis PG. Numerical modelling of transient
under-expanded jets under different ambient
thermodynamic conditions with adaptive mesh reﬁnement.
Int J Heat Fluid Flow 2016;000:1 e19.
[7] Schefer RW, Houf WG, Bourne B, Colton J. Spatial and
radiative properties of an open-ﬂame hydrogen plume. Int J
Hydrogen Energy 2006;31:1331 e40.
[8] Schefer RW, Houf WG, Williams TC, Bourne B, Colton J.
Characterization of high-pressure, underexpanded
hydrogen-jet ﬂames. Int J Hydrogen Energy
2007;32:2081 e93.
[9] Takeno K, Okabayashi K, Ichinose T, Kouchi A, Nonaka T,
Hashiguchi K. Dispersion and explosion ﬁeld tests for 40MPa
pressurized hydrogen. Int J Hydrogen Energy
2007;32:2144e53.
[10] Okabayashi K, Tagashira K, Takeno K, Aasahara M,
Hayashi AK, Komori M. Non-steady characteristics of
dispersion and ignitability for high-pressurized hydrogen jet.
In: The 54th combustion symposium conference; 2016 [in
Japanese].
[11] Radulescu MI, Law CK. The transient start of supersonic jets.
J Fluid Mech 2007;578:331 e69.
[12] Vuorinen V, Yu J, Tirunagari S, Kaario O, Larmi M, Duwig C,
et al. Large-eddy simulation of highly underexpanded
transient gas jets. Phys Fluids 2013;25. 016101 .
[13] Jothi TJS, Srinivasan K. Role of initial conditions on noise
from underexpanded pipe jets. Phys Fluids 2009;21. 066103 .
[14] Orescanin MM, Prisco D, Austin JM. Exhaust of
underexpanded jets from ﬁnite reservoirs. AIAA 2010-5108.
2010.
[15] Hong ZK, Davidson DF, Hanson RK. An improved H
2/O2
mechanism based on recent shock tube/laser absorption
measurements. Combust Flame 2011;158:633 .
[16] Liou MS, Wada Y. A ﬂux splitting scheme with high-
resolution and robustness for discontinuities. AIAA Pap 1994.
94e0083.
[17] Stull DR, Prophet H. JANAF thermochemical tables. 2nd ed,
37. NSRDS-NBS; 1971 .
[18] NIST Chemistry WebBook http://webbook.nist.gov/
chemistry/.
[19] Bird RB, Stewart WE, Lightfoot EN. Transport phenomena.
New York: John Wiley & Sons, Inc.; 1960. p. 22 .
[20] Wilke CR. A viscosity equation for gas mixtures. J Chem Phys
1950;18(4):517e9.
[21] Chapman S, Cowling TG. The mathematical theory of non-
uniform gases: an account of the kinetic theory of viscosity,
international journal of hydrogen energy 42 (2017) 7120 e7134 7133

<!-- PDF_PAGE: 15 -->

thermal conduction and diffusion in gases. Cambridge
university press; 1970 .
[22] Hishida M, Hayashi AK. Numerical simulation of pulsed jet
plume combustion. Prog Astronaut Aeronaut
1993;152:343e57.
[23] Dziemi/C19nska E, Hayashi AK. Auto-ignition and DDT driven by
shock wave e boundary layer interaction in oxyhydrogen
mixture. Int J Hydrogen Energy 2013;38(10):4185 e93.
[24] Asahara M, Yokoyama A, Hayashi AK, Yamada E, Tsuboi N.
Numerical simulation of auto-ignition induced by high-
pressure hydrogen release with detailed reaction model:
ﬂuid dynamic effect by diaphragm shape and boundary
layer. Int J Hydrogen Energy 2014;39(35):20378 e87.
[25] Wassiljewa A. W €armeleitung in Gasgemischen. Phys Z
1904;5(22):737e42.
[26] Euken A. On the thermal conductivity, the speciﬁc heat and
the viscosity of gases. Phys Z 1913;14:324 e32.
[27] Gottlieb S, Shu CW, Tadmor E. Strong stability-preserving
high-order time discretization methods. SIAM Rev
2001;43(1):89e112.
[28] MacNeice P, Olson KM, Mobarry C, de Fainchtein R,
Paramesh Packer C. A parallel adaptive mesh reﬁnement
community toolkit. Comput Phys Commun 2000;126:330 e54.
[29] Olson K, MacNeice P. An over of the PARAMESH AMR
software and some of its applications. In: Plewa T, Linde T,
Weirs G, editors. Adaptive mesh reﬁnement-theory and
applications, Proceedings of the Chicago Workshop on
adaptive mesh reﬁnement methods, series: lecture notes in
computational science and engineering, 41. Berlin: Springer;
2005.
[30] Olson K. PARAMESH: a parallel adaptive grid tool. In:
Deane A, Ecer A, Brenner G, Emerson D, McDonough J,
Periaux J, et al., editors. Parallel computational ﬂuid
dynamics 2005: theory and applications: Proceedings of the
Parallel CFD Conference, College Park, MD, U.S.A. Elsevier;
2006.
[31] Xiao H, Houim RW, Oran ES. Formation and evolution of
distorted tulip ﬂames. Combust Flame 2015;162:4084 e101.
[32] Xiao H, Houim RW, Oran ES. Effects of pressure waves on the
stability of ﬂames propagating in tubes. Proc Combust Inst
2017;36(1):1577e83.
[33] Jiang CW, Feng X, Zhang J, Zhong D. AMR simulations of
magnetohydrodynamic problems by the CESE method in
curvilinear coordinates. Sol Phys 2010;267:463 e91.
[34] Houim RW, Kuo KK. A low-dissipation and time-accurate
method for compressible multi-component ﬂow with
variable speciﬁc heat ratios. J Comput Phys
2011;230:8527e53.
[35] Jiang CW, Cui S, Feng X. Solving the Euler and Navier eStokes
equations by the AMR e
CESE method. Comput Fluids
2012;54:105e17.
[36] Kahaki AF. Phase-ﬁeld modeling of multiphase ﬂows using
the lattice Boltzmann method with adaptive mesh
reﬁnement. Doctor thesis. the City University of New York;
2015.
[37] Gerris SP. A tree-based adaptive solver for the
incompressible Euler equations in complex geometries. J
Comput Phys 2003;190:572 .
[38] Matsumoto T. Self-gravitational magneto hydrodynamics
with adaptive mesh reﬁnement for protostellar collapse.
Publ Astron Soc Jpn 2007;59:905 .
[39] Driftmyer RT. A correlation of freejet data. AIAA J
1972;10(8):1093e5.
[40] Crist S, Sherman PM, Glass DR. Study of the highly
underexpanded sonic jet. AIAA J 1996;4:68 e71.
[41] Ashkenas H, Sherman FS. The structure and utilization of
supersonic free jets in low density wind tunnel. In: Advances
in applied mechanics-rareﬁed gas dynamics. New York:
Academic Press; 1965. p. 84 e105.
[42] Bonelli F, Viggiano A, Magi V. A numerical analysis of
hydrogen under-expanded jets under real gas assumption. J
Fluids Eng 2013;135 .
[43] Ouellette P. Direct injection of natural gas for diesel engine
fueling [Ph.D. thesis]. Vancouver, Canada: The University of
British Columbia; 1996 .
[44] Turner JS. The ‘starting plume ’ in neutral surroundings. J
Fluid Mech 1962;13:356 e68.
[45] Hill PG, Ouellette P. Transient turbulent gaseous fuel jets for
diesel engines. J Fluids Eng 1999;121:93 e101.
[46] Ouellette P, Hill PG. Turbulent transient gas injections. J
Fluids Eng 2000;122:743 e52.
[47] Petersen BR, Ghandhi JB. Transient high-pressure hydrogen
jet measurements. 2006. SAE Technical Paper 2006-01-0652 .
[48] Abraham J. Entrainment characteristics of transient gas jets.
Heat Transf Part A Appl 1996;30:347 e64.
[49] Petersen B, Ghandhi J. Transient high-pressure hydrogen jet
measurements. Master thesis. University of Wisconsin-
Madison; 2006 .
[50] Kelly DM, Teng YC, Li Y, Zhang K. Validation of the FAST
forecast model for the storm surges due to hurricanes Wilma
and Ike. Nat Hazards 2016:1 e22.
[51] Friedman MP. A simpliﬁed analysis of spherical or cylindrical
blast waves. J Fluid Mech 1961;11:1 e15.
[52] Golub VV, Baklanov DI, Bazhenova TV, Golovastov SV,
Ivanov MF, Laskin IN, et al. Experimental and numerical
investigation of hydrogen gas auto-ignition. Int J Hydrogen
Energy 2009;34(14):5946 e53
.
[53] Xu BP, El Hima L, Wen JX, Dembele S, Tam VHY, Donchev T.
Numerical study on the spontaneous ignition of pressurized
hydrogen release through a tube into air. J Loss Prev Pro
2008;21(2):205e13.
[54] Naboko IM, Bazhenova TV, Opara AI, Belavin VA. Formation
of a jet of shock-heated gas outﬂowing into evacuated space.
Astronaut Acta 1972;17:653 e8.
[55] Hornung H. Regular and Mach reﬂection of shock waves. Ann
Rev Fluid Mech 1986;18:33 e58.
[56] Inman JA, Danehy PM, Nowak RJ, Alderfer DW. Identiﬁcation
of instability modes of transition in underexpanded jets. In:
38th ﬂuid dynamics conference and exhibit. Seattle,
Washington, USA: AIAA Paper; 2008. AIAA 2008 e4389.
[57] Edgington-Mitchell D, Honnery RD, Soria J. The under
expanded jet Mach disk and its associated shear layer. Phys
Fluids 2014;26. 096101 .
international journal of hydrogen energy 42 (2017) 7120 e71347134
