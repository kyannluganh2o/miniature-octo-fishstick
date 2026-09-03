<!-- PDF_PAGE: 1 -->

ViewOnline
ExportCitation
RESEARCH ARTICLE |  SEPTEMBER 14 2021
Shock-induced cavitation and wavefront analysis inside a
water droplet 
Luc Biasiori-Poulanges 
  ; Hazem El-Rabii 
Physics of Fluids 33, 097104 (2021)
https://doi.org/10.1063/5.0063827
Articles You May Be Interested In
A phenomenological analysis of droplet shock-induced cavitation using a multiphase modeling approach
Physics of Fluids (January 2023)
Laser-induced shock inside a cylindrical water column
Physics of Fluids (January 2024)
Geometry effects on the droplet shock-induced cavitation
Physics of Fluids (June 2023)
 29 August 2026 08:24:19

<!-- PDF_PAGE: 2 -->

Shock-induced cavitation and wavefront analysis
inside a water droplet
Cite as: Phys. Fluids 33, 097104 (2021); doi: 10.1063/5.0063827
Submitted: 17 July 2021 . Accepted: 27 August 2021 .
Published Online: 14 September 2021
Luc Biasiori-Poulanges1
 and Hazem El-Rabii2,a)
AFFILIATIONS
1Institute of Fluid Dynamics, Department of Mechanical and Process Engineering, ETH Zurich Sonneggstrasse 3, 8092 Z €urich,
Switzerland
2Institut Pprime, CNRS UPR 3346 – Universit /C19e de Poitiers – ISAE-ENSMA, 1 avenue Cl /C19ement Ader, 86961 Futuroscope, France
a)Author to whom correspondence should be addressed: hazem.elrabii@cnrs.pprime.fr
ABSTRACT
The objective of this study is to develop a basic understanding of the interaction of shock waves with density inhomogeneities. We consider
the particular instance of a planar air shock impinging on a spherical water droplet and discuss to what extent this interaction can lead to the
inception of cavitation inside the droplet. The effort centers on early phases of the interaction, which are analyzed using both ray theory and
a hydrodynamic code. Within the context of ray theory, the occurrence of focusing is examined in detail, and parametric equations are
derived for the transmitted wavefront and its multiple internal reﬂections. It is found that wave patterns predicted by ray calculations
compare extremely well with the more accurate numerical solutions from simulations. In particular, it is shown that the internal wavefront
assumes a complex time-dependent shape whose dominant feature is the existence of cusp singularities. These singular points are shown to
trace out surfaces that are the caustics of the associated system of rays. From the singularities of the energy ﬂux density of the refracted wave,
the parametric equations of the caustic surface associated with the kth reﬂected wavefront are deduced. As a consequence of the focusing
process, simulations show the formation of negative-pressure regions in the internal ﬂow ﬁeld. These low-pressure zones are identiﬁed as
possible spots at which cavitation may occur, depending on the magnitude of pressure reached. Finally, numerical results provide quantita-
tive information on the dependence of negative-pressure peaks upon incident-shock-wave strength.
Published under an exclusive license by AIP Publishing. https://doi.org/10.1063/5.0063827
I. INTRODUCTION
The fundamental mechanisms governing droplet aerobreakup
have been addressed in numerous studies in which the fragmentation
of a single spherical drop suddenly exposed to a uniform high-speed
g a sﬂ o wh a sb e e nc o n s i d e r e d .
1 The relative velocity of the drop with
respect to the ambient ﬂow ﬁeld has often been realized by its injection
into the uniform ﬂow ﬁeld behind a shock wave. Curiously enough,
the question whether the shock wave itself may have any effect on the
deformation and breakup process has not received much attention.
T h eu n d e r l y i n gr e a s o n sa r el i k e l yt w o f o l d :ﬁ r s t ,t h et i m ei tt a k e sf o r
the shock wave to transit the drop is too short to cause any signiﬁcant
drop response during the interaction;
2 second, the large difference in
shock impedance between the ambient gas and the liquid results in
poor energy transfer into the liquid
3 (e.g., the transmission coefﬁcient
from air to water /C25 0:1%). While it is tempting to conclude from the
above that the shock wave has no direct effect on droplet evolution, a
closer consideration of the matter shows that the answer is not that
straightforward.
Indeed, because of the large shock impedance contrast between
air and water, the interface bounding the liquid medium acts as a per-
fect mirror trapping the transmitted wave energy within the droplet.
As a result, the conﬁned shock wave experiences near total reﬂections
and focusing that ampliﬁes its local interaction with the liquid on short
time scales. The important point here is that the reﬂected wave is a
focused expansion wave that can, under some conditions, expose
regions of the liquid to a pulling force. This suggests the possibility for
the liquid to cavitate. Water, for instance, cannot withstand signiﬁcant
tension and starts to cavitate whenever the pressure falls below some
critical value.
4 Given that the presence of vapor cavities inside liquid
droplets alters their interfacial dynamics,5–8 changes in the fragmenta-
tion process are to be expected, especially if high-speed jets develop
during cavity collapse.
7
In this paper, the question we are concerned with is under what
conditions negative pressure that is sufﬁciently low to cause cavitation
can be reached inside a shock-impacted water droplet. We use numer-
ical simulations to identify these conditions by considering that
Phys. Fluids 33, 097104 (2021); doi: 10.1063/5.0063827 33, 097104-1
Published under an exclusive license by AIP Publishing
Physics of Fluids ARTICLE scitation.org/journal/phf
 29 August 2026 08:24:19

<!-- PDF_PAGE: 3 -->

cavitation starts whenever the pressure falls below some critical value.
The results of these simulations and, in particular, the complex wave-
front patterns generated inside the droplet are interpreted qualitatively
using the classical ray-tracing approach to geometrical acoustics.
The outline of this paper is as follows. Section II provides a brief
introduction of the basis of linear geometrical acoustics. In Sec.III,r a y
calculations are used to examine the wave motion inside a spherical
water droplet following its impact by a plane shock wave. The forma-
tion of caustics, due to internal reﬂection at the droplet surface, is then
discussed in Sec. IV.S e c t i o nV is devoted to evaluate the liquid pres-
sure magnitude for various shock strengths and address the regimes
for which heterogeneous and homogeneous cavitation is likely to
occur. SectionVI presents our concluding remarks.
II. LINEAR GEOMETRICAL ACOUSTICS
The propagation of weak shock waves can be described by geo-
metrical acoustics. A detailed account of the linear theory is given in
the monograph by Friedlander.
9 However, we brieﬂy outline its basis
here, for the sake of completeness. We begin with the acoustic wave
equation for the pressure p at the position r and time t,w i t has p a c e -
dependent wave speed, c; constant density; and no source term as
follows:
Dp ¼
1
c2
@2p
@t2 : (1)
To solve Eq. (1), the ﬁrst step is usually to transform this equation
from the time domain to the frequency domain by the application of a
Fourier transform with respect to time as follows:
^pðr; xÞ¼
ð
þ1
/C01
pðr; tÞ eixt dt; (2)
where x is the angular frequency. With this transform and the usual
decaying conditions on p as t !þ 1, we obtain the transformed
wave equation
D^p þ x2
c2 ^p ¼ 0: (3)
The equations of geometrical acoustics are then constructed by seeking
as o l u t i o nt oE q .(3) in terms of a high-frequency asymptotic expan-
sion as follows:
^pðr; xÞ¼ eixsðrÞ X1
m¼0
PmðrÞðixÞ/C0 m; (4)
where sðrÞ is called the phase function and PmðrÞ are the amplitudes.
These are determined by substituting Eq.(4) into Eq. (3) and equating
like powers of x to zero, yielding the following system of equations for
s and Am:
rs /C1rs ¼ c/C0 2; (5)
r/C1ðP2
0 rsÞ¼ 0; (6)
2rs /C1rPm þ D Pm/C0 1 ¼ 0; m ¼ 1; 2; … ; (7)
In the high-frequency limit, only the leading term in expansion (4)
need be evaluated, that is, Eq. (7) can be ignored. Equations (5) and
(6) are solved by introducing a family of curves (rays) that are orthog-
onal to the phase fronts sðrÞ.T h i sf a m i l yo fr a y sd e ﬁ n e san e w
coordinate system in which both equations reduce to ordinary differ-
ential equations. Consider a ray described by the parametric curve
nðsÞ,w h e r es is the arc length along the ray. Since rs is a vector per-
pendicular to the wavefronts, we can write the following equation for
the ray trajectory:
1
c
dn
ds ¼r s: (8)
It is convenient to recast this equation in a form only involving cðrÞ.
To do so, we differentiate Eq. (8) with respect to s and ﬁnd, after some
manipulations,
d
ds
1
c
dn
ds
/C18/C19
¼r 1
c
/C18/C19
: (9)
To express Eq. (5) in terms of the ray coordinate s,w eu s eE q .(8) in
Eq. (5),y i e l d i n g
ds
ds ¼ 1
c : (10)
The latter form of Eq.(5) is readily solved to give
sðsÞ¼ sð0Þþ
ðs
0
ds0
cðs0Þ ; (11)
where the integral term is the travel time along the ray.
The ﬁnal step in determining the pressure at leading order is to
compute the amplitude P0 from Eq. (6). By a similar calculation that
leads to Eq. (10), it can be shown that Eq. (6) reduces to an ordinary
differential equation which gives, when integrated,
P0ðsÞ¼ P0ð0Þ
ﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ ﬃ
cðsÞ
cð0Þ
dSð0Þ
dSðsÞ
s
: (12)
In this relation, dS denotes the cross-sectional area of an inﬁnitesimal
ray tube10 containing the rayn. From a physical point of view, Eq.(12)
states that the energy density integrated across a ray tube remains
constant.
For a homogeneous medium, c is constant and, according to Eq.
(9), the rays are straight lines, which are determined as normals to a
given initial wavefront. Furthermore, Eq.(11) indicates that the phase
of the wave at the ray coordinate s is delayed by s/c relative to that of
the initial wavefront. In consequence, for waves propagating in a
homogeneous medium, the construction of subsequent wavefronts is a
simple matter of elementary geometry as illustrated in the next
section.
III. CONFINED WAVEFRONT PROPAGATION
We consider a planar shock wave propagating through air and
impinging on a spherical water droplet. The shock–droplet interaction
results in a shock that is transmitted through the interior of the water
droplet while a portion of the incident shock diffracts around the edge
of the droplet. Here, we focus on the transmitted shock and analyze
the wavefront evolution using a ray-tracing method.
11 As mentioned
in Sec. II, this method applies to slightly supersonic shocks. To ascer-
tain whether this condition is satisﬁed for wave propagation inside a
shock-impacted droplet, we can rely on past studies addressing
shock–droplet interactions.
12,13 For example, Sembian et al. 12
Physics of Fluids ARTICLE scitation.org/journal/phf
Phys. Fluids 33, 097104 (2021); doi: 10.1063/5.0063827 33, 097104-2
Published under an exclusive license by AIP Publishing
 29 August 2026 08:24:19

<!-- PDF_PAGE: 4 -->

considered a plane incident shock traveling in air at a speed of
830 m /C1s/C0 1 and striking a 2D water droplet. On the basis of the images
shown in Figs. 10(b) and 10(c) of this reference, we measure a shock
velocity of 1480 m /C1s/C0 1 for the initial transmitted wave in the droplet.
This value is very close to the sonic speed in water (1450 m /C1s/C0 1)a n d
justiﬁes the ray approach adopted here.
We assume that both air and water are homogeneous, so that
rays are straight lines along which wavefronts propagate at constant
speed. In accordance with the ray formalism, the incident shock wave
propagates along a family of parallel rays incident from the left onto
the droplet. Figure 1 illustrates the geometry of the problem. The
radius of the spherical droplet is denoted by a and its center is at the
origin of the coordinate system. We conveniently choose the x axis in
the direction of the incoming parallel bundle of rays and the time ori-
gin as the instant at which the shock wave reaches x ¼/C0 a.C o n s i d e r
now an arbitrary ray AB striking the droplet surface at pointB with an
incident angle a. The major part of the ray amplitude is reﬂected at B,
while the remaining part of the intensity is transmitted into the drop-
let. The refracted ray makes an angle h with the interface normal at B.
The incident and refracted angles are related by the fundamental law
of refraction
14
sin h ¼ n sin a; (13)
where n is the ratio of the wave velocity in water to that in air. The
transmitted ray is then internally reﬂected at each interaction with the
droplet surface at an angle h to the normal. The typical ray path of the
refracted wavefront therefore consists of many successive segments
separated by reﬂection points Pk at the droplet boundary. Following
standard usage in geometrical optics, we deﬁne a k-ray family to be
rays within the droplet (for all a) that have undergone k –1i n t e r n a l
reﬂections.15 According to this deﬁnition, the transmitted rays that
have not suffered internal reﬂection belong to the 1-ray family. They
become two rays after their ﬁrst reﬂection, and so on. The wavefront
traveling along ak-ray family will be denoted byf
k.
We shall now derive the parametric equations for fk.T ot h a t
end, let us consider an arbitrary point M belonging to a k-ray. The
location of this point is expressed by its position vector as
rM ¼ rPk/C0 1 þ ek‘ Pk/C0 1 M ; (14)
where ek are the unit vectors in the k-ray direction, and ‘ Pk/C0 1 M is the
length of the segment Pk/C0 1M. Elementary geometrical considerations
(Fig. 1) yield the coordinates of the kth internal reﬂection point Pk as
follows:
ðxPk ; yPk Þ¼ð a cos ck; a sin ckÞ; (15)
where ck ¼ 2kh /C0 a /C0ð k /C0 1Þp. P0 corresponds to the entry point
(B)o fr a yAB into the droplet. Using Eq.(15), we can then write down
at once that
ek ¼ ex cos ðck /C0 hÞþ ey sin ðck /C0 hÞ; k /C211; (16)
where ex and ey are the unit vectors in the x and y directions,
respectively.
To determine ‘ Pk/C0 1 M , we note that the time t required for point
M on the k-ray to be reached by the wavefrontfk is
t ¼ a
ua
ð1 /C0 cos aÞþ 2ðk /C0 1Þ a
uw
cos h þ ‘ Pk/C0 1 M
uw
; (17)
where ua and uw denote the wave velocity in air and water, respec-
tively. The ﬁrst term in Eq. (17) is the time for the front to travel along
the ray AB from x ¼/C0 a to B, while the second term represents the
total travel time it takes for the front to go from B to Pk/C0 1 along the
segment rays in between. Consequently, Eq.(17) yields
‘ Pk/C0 1 M ¼ uw t /C0 nað1 /C0 cos aÞ/C0 2ðk /C0 1Þa cos h: (18)
After substituting Eq. (18) into Eq. (14) and expressing the result in
Cartesian components, we ﬁnd
xM ¼ uwt /C0 nað1 /C0 cos aÞ/C0 2ðk /C0 1Þa cos h½/C138 cos ðck /C0 hÞ
/C0 a cos ðck /C0 2hÞ; (19a)
yM ¼ uwt /C0 nað1 /C0 cos aÞ/C0 2ðk /C0 1Þa cos h½/C138 sin ðck /C0 hÞ
/C0 a sin ðck /C0 2hÞ: (19b)
Given that the wavefront shape is deﬁned as the locus of points
reached by a disturbance in a given time along all possible ray paths,
Eqs. (19a) and (19b) represent the parametric equations of the wave-
front fk,w i t ha as parameter.
Since our interest is in the determination of the refracted wave-
front and its internal reﬂections, we need consider only the incident
rays that meet the upstream droplet surface at an angle lower than the
critical angle for total reﬂection, i.e.,jaj < ac ¼ arcsinð1=nÞ.I ts h o u l d
be noted that the range of values of a is not restricted solely by ac.
Indeed, for a k-ray family, two speciﬁc rays ( rl and ru) bound the
region in which the k-rays lie. The ray rl corresponds to the ray
reaching the point Pk/C0 1 at time t, whereas ru is the ray that hits, at
the same instant, the inner droplet surface at Pk. The associated inci-
dent angles al and au are obtained by setting ‘ Pk/C0 1 M equal to 0 and
2a cos h, respectively, in Eq.(18) as follows:
2ðk /C0 1Þa cos hl ¼ uwt /C0 nað1 /C0 cos al Þ; (20)
2ka cos hu ¼ uwt /C0 nað1 /C0 cos auÞ; (21)
where hl and hu are the refraction angles corresponding to al and au,
respectively. Equations(20) and (21) can be solved exactly, since they
FIG. 1. Ray diagram showing the refraction and multiple internal reﬂection of ini-
tially parallel rays incident on and crossing the droplet boundary.
Physics of Fluids ARTICLE scitation.org/journal/phf
Phys. Fluids 33, 097104 (2021); doi: 10.1063/5.0063827 33, 097104-3
Published under an exclusive license by AIP Publishing
 29 August 2026 08:24:19

<!-- PDF_PAGE: 5 -->

are quadratic in cos a.T h ev a l u e so fa that should be considered
for k ¼ 1a r es u c ht h a tjaj is bounded by the lowest value between
ac, al,a n d au.F o r k greater than 1, the absolute value of a is
between al and au.
Figure 2 shows the wavefront pattern generated inside the drop-
let, at different instants, as calculated from Eqs. (19a) and (19b) for
k ¼ 1 and 2. To avoid overloading the ﬁgure with crossed and/or juxta-
posed fronts, the successive wavefront positions are displayed in differ-
ent panels: (a) 50 ns /C20 t /C20 1.3, (b) t ¼ 1.5, (c) t ¼ 1.7, and (d) 1.8
/C20 t /C20 2.5 ls. We observe from Fig. 2(a) that the transmitted front
appears as originating from an external point source located on the
symmetry axis. It does not exhibit any singular point during early
times (t /H113510.6 ls), i.e., the front shape is smooth. Closer examination
of the front shape at t ¼ 0.6 ls reveals that the wavefront folds itself
where it is in contact with the droplet boundary. The fold moves along
the boundary as f propagates and splits f into two subfronts, f
1
and f2. The segment of the front ahead of the fold ( f1)r e m a i n s
smooth all along its propagation and corresponds to the rays that have
experienced only a single refraction. The front segment f
2 starts to
develop simultaneously with the appearance of the fold, near the drop-
let surface [see Fig. 2(a), t ¼ 0.6 ls]. In contrast to f
1; f2 exhibits a
singular point (cusp) that is particularly apparent at t ’ 0.9 lsa n d
grows as the front travels through the droplet.
On reaching the downstream droplet surface, f is completely
reﬂected back. The fronts displayed in Figs. 2(b)–2(d) are thus exclu-
sively once-reﬂected fronts (i.e., f2), which travel from right to left.
As time proceeds, we see from Figs. 2(b) and 2(c) that the cusps from
either side of the symmetry axis become closer to each other. 16 The
front f then passes through itself, developing a self-intersecting swal-
lowtail pattern (not shown here). This cusp motion is accompanied by
a focusing of the front segment connecting the pair of cusps, until we
observe cusp annihilation. Subsequently, f takes on a ﬁshlike shape
before it begins to diverge and becomes smooth again [Fig. 2(d)].
A striking feature of the cusp motion is evidenced by superposing
successive fronts f
2,a ss h o w ni n Fig. 3 . Indeed, as the wavefront
advances, we see that the cusp of f2 traces out a curve, the so-called
caustic, which is shown by a dashed line in Fig. 3.W en o t i c et h a tt h e
caustic has a cusp singularity at C,w h e r ei ti sc l e a r l ys e e nt h a tt h e
front’s cusp cancels.
IV. CAUSTICS INSIDE THE LIQUID DROPLET
It is well known that a caustic corresponds to regions where sev-
eral rays bunch together to form discontinuities at which the intensity
diverges. This means that the front’s cusp is a moving focus, and the
c a u s t i ci st h es u r f a c et r a c e db yi t .
FIG. 2. Propagation of the conﬁned wavefront within the droplet ( n ¼ 2.12). The labels on the contours indicate the physical time in tenths of a microsecond: (a) 0.5–13.0, (b)
14.0, (c) 17.0, and (d) 18.0–25.0. Wavefronts fk¼1;2 are plotted from the parametric Eq. (19). The case k ¼ 3, shown only for t ¼ 1.8 ls, is intended to be illustrative.
FIG. 3. Superposition of successive fronts f2, evidencing the cusp motion and
with the caustic traced out by the black dashed line. The black-to-red color scale
represents physical time.
Physics of Fluids ARTICLE scitation.org/journal/phf
Phys. Fluids 33, 097104 (2021); doi: 10.1063/5.0063827 33, 097104-4
Published under an exclusive license by AIP Publishing
 29 August 2026 08:24:19

<!-- PDF_PAGE: 6 -->

To determine the parametric equation of the caustic, we note
that the loci of points of high ray concentration can be obtained from
the singularities of the energy ﬂux density of the transmitted wave. Ifr
denotes the ﬂux density associated with the plane incident wave, then
the ﬂux incident upon an element of area dS
d on the droplet surface is
dU ¼ r cos a dSd. Owing to axial symmetry about the x axis, we have
dSd ¼ 2pa2 sin a da. The fraction of dU that survives k –1i n t e r n a l
reﬂections is thus given by
dUM ¼ TðaÞRk/C0 1ðaÞ dU
¼ 2pa2rTðaÞRk/C0 1ðaÞ sin a cos a da; (22)
where TðaÞ and RðaÞ are the transmission and reﬂection coefﬁcients,
respectively. The ﬂux density over the transmitted wavefront is equal
to dUM divided by the element of area dS mapped out by the rays that
have crosseddSd as follows:
dUM
dS ¼ a2rTðaÞRk/C0 1ðaÞ sin a cos a
yM ð _x2
M þ _y2
M Þ1=2 : (23)
The superposed dot indicates the derivative with respect to a.
Inserting(19a) and (19b) into Eq. (23),w eﬁ n dt h a t
dUM
dS ¼ a2rTðaÞRk/C0 1ðaÞsinacosa
‘ Pk/C0 1 M sinðck /C0 hÞþ asinck/C0 1
/C2/C3
jð_ck /C0 _hÞ‘ Pk/C0 1 M /C0 a_ck/C0 1 coshj
:
(24)
The parametric equations for the caustic surfaces are obtained from
the condition that the denominator of the expression on the right-
hand side of Eq. (24) be zero. Thus,
ð_ck /C0 _hÞ‘ Pk/C0 1 M /C0 a_ck/C0 1 cos h ¼ 0; (25)
‘ Pk/C0 1 M sin ðck /C0 hÞþ a sin ck/C0 1 ¼ 0: (26)
The condition (25) gives a relation for the value of the angle corre-
sponding to the front cusp at time t,w h i c h ,a f t e rs o m ea l g e b r a ,c a nb e
recast as
n sin2 a
2
/C18/C19
þ f ðaÞþ k /C0 1½/C138 cos h ¼ uw t
2a ; (27)
where
2f ðaÞ¼ 2n2ðk /C0 1Þ sin 2a /C0 sin 2h
n2ð2k /C0 1Þ sin 2a /C0 sin 2h :
If we eliminate t from Eqs. (19a) and (19b) by means of condition
(27), we obtain the following for the caustic of orderk:
xc ¼ af ðaÞ cos ck þ af ðaÞ/C0 1½/C138 cos ðck /C0 2hÞ; (28a)
yc ¼ af ðaÞ sin ck þ af ðaÞ/C0 1½/C138 sin ðck /C0 2hÞ: (28b)
Since the ﬂux density (24) becomes inﬁnite at the caustic c,i tc a n -
not be used to quantify the density of rays at the caustic. Therefore,
following Burkhard and Shealy, 17 we compute the density of rays
tangent to the caustic, which gives a relative measure of the focus-
ing strength over the caustic. This quantity is obtained by dividing
an element of incident ﬂux by the area of the caustic formed by
the associated rays, dS
c. For the caustic of singly reﬂected rays, we
ﬁnd
dU
dSc
¼ 2arTðaÞRðaÞ cos hðcos h /C0 3n cos aÞ2
3n2ð6 þ 5n2 þ 11n2 cos 2a /C0 18n cos a cos hÞjycj : (29)
It is apparent from this expression that the concentration of tangent
rays is highest at the intersection of the caustic and the symmetry axis
(y
c ¼ 0), i.e., at the caustic’s cusp. This is because the degree of focus-
i n ga tt h ec a u s t i c ’ sc u s pi sh i g h e rt h a nt h a to v e ras m a l le l e m e n to ft h e
caustic’s surface area. As exempliﬁed in Fig. 4 (for k ¼ 2), the concen-
tration increases when a decreases, becoming inﬁnite for a ¼ 0. The
location of the cuspidal point of the caustic can readily be found by
setting a ¼ 0i nE q .(28a), which gives for the horizontal coordinate
x
cusp ¼ ð/C0 1Þkn
ð2k /C0 1Þn /C0 1 a ¼
k ¼ 2 n
3n /C0 1 a: (30)
Equation (30) shows that the sign of the abscissa xcusp is determined
by the parity of k, and the position of the caustic’s cusp gradually
approaches the pointO with increasingk.
It is also interesting to consider the time tf at which focusing at
this point occurs. As shown in Fig. 3(b), tf coincides with the instant
when the two cusps of the once-reﬂected front merge. This time can
be determined from condition (27). As the left-hand side of the latter
is symmetric in a, with a maximum at a ¼ 0, the time sought is
obtained by evaluating(27) at a ¼ 0, yielding
t
f ¼ 4kðk /C0 1Þn þ 1 /C0 2k
ð2k /C0 1Þn /C0 1
a
uw
¼
k ¼ 2 8n /C0 3
3n /C0 1
a
uw
: (31)
As well as the cusp trajectory described by Eqs. (28a) and (28b),
there exists another region where the ﬂux density(24) is singular. The
equations of the loci of these singularities can be determined by using
Eq. (26) to eliminate the time t from Eqs. (19a) and (19b). In doing so,
we ﬁnd
xa ¼/C0 a sin h
sin ðck /C0 hÞ ; ya ¼ 0; (32)
which are parametric equations of a straight line segment along the x
axis. This high-density region results from the focusing on the x axis
of incident rays that enter the droplet over a ring of constant a.I ti s
FIG. 4. Variation of the density of rays tangent to the caustic (for k ¼ 2 and
n ¼ 2.12) over the incident angle a. The concentration increases when a
decreases, becoming inﬁnite for a ¼ 0.
Physics of Fluids ARTICLE scitation.org/journal/phf
Phys. Fluids 33, 097104 (2021); doi: 10.1063/5.0063827 33, 097104-5
Published under an exclusive license by AIP Publishing
 29 August 2026 08:24:19

<!-- PDF_PAGE: 7 -->

straightforward to see that the highest degree of focusing in this case is
also achieved at the point with coordinatesðxcusp; 0Þ and at time tf.
The determination of the pressure amplitude on caustic surfaces
will be described in the next section.
V. CAVITATION INSIDE A WATER DROPLET
As we have seen in the preceding section, the ray theory provides
a direct physical interpretation of the wave patterns observed within
the droplet. Furthermore, it enables us to determine regions of the
pressure ﬁeld where the wave is focused (i.e., caustics). A quantitative
prediction of pressures at caustics is, however, beyond the scope of ray
calculations, which indicate inﬁnite pressure in caustic regions [see Eq.
(24)]. To identify conditions inducing cavitation inside a droplet hit by
a shock wave, it is therefore necessary to complement the ray approach
with numerical simulations to determine the pressure on caustic surfa-
ces. Before proceeding, however, it is useful to say a few words on the
cavitation threshold.
It is well known that a liquid will rupture (or cavitate) when sub-
jected to tension in excess of some critical value that depends on the
nature of the liquid and its purity. For pure liquids, cavitation arises
from microscopic voids caused by random thermal motions of mole-
cules.
18 The process of vapor bubble formation by this mechanism is
referred to in the literature as homogeneous nucleation. By contrast,
when liquids contain impurities, the maximum tension they can with-
stand drastically decreases. This process, termed heterogeneous nucle-
ation, results from the expansion of submicroscopic gas pockets
trapped at the solid/liquid interface on the wall of the container or on
particles present in the liquid. Water, in particular, has a wide range of
measured tensile limits. The maximum tension that pure water can
withstand is 134 MPa at 300 K, according to vapor nucleation theory.
19
Such a high tension has been achieved experimentally. 20 For unpuri-
ﬁed water, the tensile limit becomes less speciﬁc and is found to be a
few orders of magnitude lower, 0.1–1 MPa.21 Given such a disparity in
tensile limits for water, a pressure cavitation threshold has to be cho-
sen, somewhat arbitrarily, within the range of data reported in the sci-
entiﬁc literature. We have opted to consider two different values. As
far as pure water is concerned, a natural choice is the above-
mentioned theoretical limit of /C0 134 MPa, which will be denoted by
p
c;1. To address the case of unpuriﬁed water, it is also necessary to con-
sider a higher value as a threshold, pc;2. We set this value to /C0 2.3 MPa
on the basis of the experimental results reported by Sembianet al.12
We simulate the interaction of a planar air shock wave with a
spherical water drop using the open-source hydrodynamics code
ECOGEN.22 In this code, the dynamics of water and air are modeled
using compressible multicomponent ﬂows in which ﬂuid components
are assumed immiscible.23 The water obeys the stiffened gas equation
of state with the parameters given in Ref. 24, whereas air follows the
ideal gas law. Viscous and capillary effects are accounted for according
to Schmidmayer et al. ,
25 while phase changes are not modeled. An
interface-capturing scheme is used, combining the ﬂow model with a
shock-capturing ﬁnite-volume method. Additionally, three levels of
reﬁnement are used in order to resolve the ﬂow discontinuities. We
refer the reader to Refs. 22 and 24 and references therein for more
details.
The problem at hand is treated using a two-dimensional, axisym-
metric formulation. A schematic of the computational domain is pre-
sented in Fig. 5, where the x axis is the symmetry axis on which the
center of the spherical droplet of radius a is located. A symmetric
boundary condition is applied to the bottom side of the computational
domain, and nonreﬂective boundary conditions are used for the remain-
ing boundaries to avoid contamination of calculations by the reﬂected
outgoing waves.
26–28 Shock is initialized inside the domain and travels
from left to right. For a given incident shock Mach numberMs,t h ei n i -
tial ﬂow ﬁeld is determined from the Rankine–Hugoniot jump relations
f o ra ni d e a lg a su s i n gad o w n s t r e a md e n s i t yo f1:204 kg /C1m/C0 3,ap r e s -
sure of 1 atm, and a water density of 103 kg /C1m/C0 3. The surface tension
between air and water is 72 mN/C1m/C0 1. The water drop is assumed to be
in mechanical equilibrium with the surrounding air. The excess of pres-
sure inside the droplet over the ambient pressure was computed by
employing the Laplace–Young equation.
Figure 6 displays the time evolution of the wavefront during a
few round-trips. The upper half of each panel in the ﬁgure shows
numerical schlieren images (magnitude of density gradient) from the
simulations, whereas the lower half displays the corresponding fronts
as predicted by ray theory [see Eqs. (19a) and (19b)]. Note that a non-
linear scale has been applied to the schlieren images to enhance the
visualization of the wave pattern.
28–30 The sequence runs from left to
right and then top to bottom, and is not uniformly spaced in time (see
the caption for details). The time steps are selected so as to exhibit the
principal features of front evolution. It is clear from the comparison
offered here that, with regard to both the shape and location of the
wavefront, we have a remarkable agreement between the theoretical
and numerical results. We point out that such an excellent agreement
is obtained with no adjustable parameters.
In Fig. 7 , we plot the caustic associated with rays reﬂected
once at the boundary of the droplet (red line in the ﬁgure), as
expressed by Eqs. (28a) and (28b).A sw eh a v ea l r e a d ym e n t i o n e d ,
this surface is the locus of points where the ray intensity is the
highest. Since upon reﬂection at the droplet interface the compres-
sive wave is transformed into an expansion wave, it means that this
caustic corresponds to the region of lowest pressure. The color-
tinted circles represent the lowest pressure as obtained from the
simulation: the darker the color, the lower the pressure (see the
color bar to the right of the ﬁgure). Each circle corresponds to
the position of the front’s cusp at different time instants, which are
indicated by the same color code as for pressure, from white
(1.07 ls) to black (1.75 ls). We note, in accordance with ray calcu-
lations, that the caustic’s cusp is the point of lowest pressure. A
slight shift between the caustic and the trajectory described by the
front’s cusp is observed. The shift is largest on the x axis. Equation
(30) gives x
cusp ¼ 0:40a, which agrees reasonably well with the
simulation result of 0 :51a.F r o mE q . (31), the time at which the
FIG. 5. Setup of the two-dimensional axisymmetric computational domain. States 1
and 2 refer to the pre-shock and post-shock conditions, respectively.
Physics of Fluids ARTICLE scitation.org/journal/phf
Phys. Fluids 33, 097104 (2021); doi: 10.1063/5.0063827 33, 097104-6
Published under an exclusive license by AIP Publishing
 29 August 2026 08:24:19

<!-- PDF_PAGE: 8 -->

caustic’s cusp is reached is 1.78 ls, which is very close to the value
of 1.75 ls obtained from the simulation.
As already mentioned, our simulations do not take into account
phase changes and interactions. This implies that we ignore the effects
relevant to the dynamics of bubble formation and their feedbacks to
the droplet evolution. Because these effects are expected to signiﬁcantly
alter the droplet dynamics, our simulation results can only be consid-
ered as valid up to the instant at which the ﬁrst inception of cavitation
is observed. Our concern here nevertheless is in determining incident
shock conditions leading to cavitation inside a spherical droplet. For
such a purpose, it seems reasonable to consider that cavitation events
occur in regions where the pressure has dropped below some thresh-
old value.
31
To identify conditions conducive to the advent of cavitation
zones, we have performed simulations for incident-shock Mach num-
bers M
s varying from 1.1 to 6.0. In Fig. 8(a),w ep l o ta g a i n s tMs the
lowest pressure reached inside the droplet, Pmin,d o w n s t r e a mo f
the ﬁrst-reﬂected wave. The location of the minimum pressure
corresponds approximately to that of the caustic’s cusp. A few trends
stand out from Fig. 8(a).O n ei st h a tPmin is negative for allMs,w i t ha n
exception at Ms ¼ 1.1, for which it is nearly zero. Additionally, Pmin is
ad e c r e a s i n gf u n c t i o no fMs, as should be expected. We note that Pmin
decreases slowly from 0 at Ms ¼ 1:1t o /C0 5M P a a tMs ¼ 2:0. When
Ms is increased beyond this latter point, Pmin decreases at a higher
pace. The most interesting aspect of this graph is the linear depen-
dence of Pmin on Ms, which is observed over the range 3 :5 /H11351Ms
/C20 6:0. At this stage, we cannot offer any explanation for this behavior.
If we compare Pmin with the pressure threshold pc;1,w h o s el o c a t i o ni s
displayed in Fig. 8(a) as the horizontal red line, we see that the regimes
in which a liquid–gas phase transition is likely to develop correspond
to Ms > 5. Figure 8(b) is a zoom-in of Fig. 8(a) covering a much
smaller Ms range between 1.0 and 2.5. The horizontal red line indicates
the location of pc;2. In this case, we see that cavitation is likely to occur
whenever Ms exceeds 1.7. Such a critical value is almost three times
smaller than that obtained for pure water. As a ﬁnal word, it can be
mentioned that, in their study of shock–water column interaction,
FIG. 6. Comparison of the conﬁned wavefront spatiotemporal dynamics theoretically predicted (lower half-space) with numerical schlieren computed from s imulations (upper
half-space). Theoretical wavefronts are given by Eq. (19) for n ¼ 2.12 and displayed by a red dotted line when they overlap the schlieren visualization. Times in microseconds
are given in the labels, where the arrow in parentheses indicates the direction of wave propagation.
Physics of Fluids ARTICLE scitation.org/journal/phf
Phys. Fluids 33, 097104 (2021); doi: 10.1063/5.0063827 33, 097104-7
Published under an exclusive license by AIP Publishing
 29 August 2026 08:24:19

<!-- PDF_PAGE: 9 -->

Sembian et al.12 found that cavitation may arise for an incident shock
wave Mach number greater than 2.4. This value is 50% higher than
what we found. The difference with our value of 1.7 can obviously be
attributed to the higher degree of rarefaction wave focusing achieved
in a spherical droplet. In Table I , we report the shock wave Mach
numbers for which homogeneous and heterogeneous cavitation is
likely to occur according to our simulations.
VI. CONCLUDING REMARKS
In this paper, we have examined the initial phases of interaction
between a planar shock wave in air and a spherical water droplet. The
analysis was conducted using ray theory, which provides analytical
results that were compared with and complemented by numerical
simulations. There are several remarks and conclusions that we con-
sider of particular relevance concerning the results reported here. First,
w es a wt h a tt h ew a v e f r o n ti n s i d et h ed r o p l e ta s s u m e sac o m p l e x
time-dependent shape whose dominant feature is the existence of
cusp singularities. From ray calculations, it was clearly shown that
these singular points result from the focusing process. Second, we
derived parametric equations for the surface of the conﬁned wave-
front. Comparisons with simulations showed that the front shape
and its evolution are perfectly well described by these equations.
This result offers a simple description of the geometry and the pro-
cess of focusing of the wavefront during the interaction. Third, it
was proved that each wavefront cusp traces out a surface, which is
the caustic of the associated system of rays. The energy ﬂux density
turns out to be singular over these caustic surfaces. Although phys-
ically unrealistic, this singular behavior may be interpreted as
revealing regions of highest ray density. Furthermore, we showed
that caustics exhibit cusps where the concentration of rays forming
t h ec a u s t i c si st h es t r o n g e s t .F i n a l l y ,a sac o n s e q u e n c eo ft h ew a v e
impedance, the compression wave inside the water droplet reﬂects
at the interface as an expansion wave, thereby forming low-
pressure regions in the internal ﬂow ﬁeld. On the basis of cavita-
tion pressure thresholds from the literature, we obtained the
incident-shock-strength conditions under which a planar shock
wave can cause cavitation within a droplet.
FIG. 7. The black solid line displays the droplet boundary ( n ¼ 2.12). The red solid
line is the caustic traced out by the f2 wavefront cusp. Circle markers are
extracted from numerical simulations and refer to the spatial location of the peak
negative pressure over time, with the color indicating the pressure magnitude.
FIG. 8. Peak minimum pressure compared with (a) the cavitation pressure threshold pc;1 as predicted by classical nucleation theory and (b) the pressure threshold pc;2
reported by Sembian et al.12
TABLE I. Shock wave Mach numbers for which homogeneous and heterogeneous
cavitation is likely to occur.
Cavitation
Shock wave Mach number Ms
Threshold Sembian et al.12 Present simulations
pc;1 /C1/C1/C1 /C25 5.0
pc;2 2.4 1.7
Physics of Fluids ARTICLE scitation.org/journal/phf
Phys. Fluids 33, 097104 (2021); doi: 10.1063/5.0063827 33, 097104-8
Published under an exclusive license by AIP Publishing
 29 August 2026 08:24:19

<!-- PDF_PAGE: 10 -->

Finally, it should be noted that the approach presented here can
prove useful in a variety of applications in the biomedical ﬁeld, 32–34
aerospace and nuclear engineering,35 where other geometrical conﬁgu-
rations are encountered.
ACKNOWLEDGMENTS
The authors gratefully acknowledge fruitful discussions with
Tim Colonius from the California Institute of Technology. This
work was partially supported by the R /C19egion Nouvelle-Aquitaine as
part of the SEIGLE Project (Grant No. 2017-1R50115) and the
CPER FEDER project. The ﬁrst author acknowledges the support
received from an ETH Zurich Postdoctoral Fellowship.
The authors have no conﬂicts to disclose.
DATA AVAILABILITY
The data that support the ﬁndings of this study are available
from the corresponding author upon reasonable request.
REFERENCES
1D. Guildenbecher, C. L /C19opez-Rivera, and P. Sojka, “Secondary atomization,”
Exp. Fluids 46, 371–402 (2009).
2C. Aalburg, B. Van Leer, and G. M. Faeth, “Deformation and drag properties
of round drops subjected to shock-wave disturbances,” AIAA J. 41, 2371–2378
(2003).
3H. Chen and S. M. Liang, “Flow visualization of shock/water column inter-
actions,” Shock Waves 17, 309–321 (2008).
4K. Ando, A.-Q. Liu, and C.-D. Ohl, “Homogeneous nucleation in water in
microﬂuidic channels,” Phys. Rev. Lett. 109, 044501 (2012).
5S. R. G. Avila and C.-D. Ohl, “Fragmentation of acoustically levitating droplets
by laser-induced cavitation bubbles,” J. Fluid Mech. 805, 551–576 (2016).
6G. Xiang and B. Wang, “Numerical study of a planar shock interacting with a
cylindrical water column embedded with an air cavity,” J. Fluid Mech. 825,
825–852 (2017).
7Y. Liang, Y. Jiang, C.-Y. Wen, and Y. Liu, “Interaction of a planar shock wave
and a water droplet embedded with a vapour cavity,” J. Fluid Mech. 885,R 6
(2020).
8L. Biasiori-Poulanges and H. El-Rabii, “Multimodal imaging for intra-droplet
gas-cavity observation during droplet fragmentation,” Opt. Lett. 45,
3091–3094 (2020).
9F. Friedlander, Sound Pulses (Cambridge University Press, 2009).
10A ray tube is deﬁned as the volume enclosed by a family of rays.
11V. Cerveny, Seismic Ray Theory (Cambridge University Press, 2005).
12S. Sembian, M. Liverts, N. Tillmark, and N. Apazidis, “Plane shock wave inter-
action with a cylindrical water column,” Phys. Fluids 28, 056102 (2016).
13X. Hu, N. A. Adams, and G. Iaccarino, “On the HLLC Riemann solver for inter-
face interaction in compressible multi-ﬂuid ﬂow,” J. Comput. Phys. 228,
6572–6589 (2009).
14L. F. Henderson, “On the refraction of shock waves,” J. Fluid Mech. 198, 365
(1989).
15C. L. Adler, J. A. Lock, B. R. Stone, and C. J. Garcia, “High-order interior caus-
tics produced in scattering of a diagonally incident plane wave by a circular cyl-
inder,” J. Opt. Soc. Am. A 14, 1305–1315 (1997).
16The wave structures displayed in Fig. 2 are similar to those that form inside a
droplet impacting a solid substrate. 36,37
17D. G. Burkhard and D. L. Shealy, “Formula for the density of tangent rays over
a caustic surface,” Appl. Opt. 21, 3299–3306 (1982).
18S. Balibar and F. Caupin, “Metastable liquids,” J. Phys. 15, S75 (2002).
19J. C. Fisher, “The fracture of liquids,” J. Appl. Phys. 19, 1062–1067 (1948).
20Q. Zheng, D. J. Durben, G. H. Wolf, and C. A. Angell, “Liquids at large nega-
tive pressures: Water at the homogeneous nucleation limit,” Science 254,
829–832 (1991).
21F. Caupin and E. Herbert, “Cavitation in water: A review,” C. R. Phys. 7,
1000–1017 (2006).
22K. Schmidmayer, F. Petitpas, S. L. Martelot, and /C19E. Daniel, “ECOGEN: An
open-source tool for multiphase, compressible, multiphysics ﬂows,” Comput.
Phys. Commun. 251, 107093 (2020).
23R. Saurel, F. Petitpas, and R. A. Berry, “Simple and efﬁcient relaxation methods
for interfaces separating compressible ﬂuids, cavitating ﬂows and shocks in
multiphase mixtures,” J. Comput. Phys. 228, 1678–1712 (2009).
24B. Dorschner, L. Biasiori-Poulanges, K. Schmidmayer, H. El-Rabii, and T.
Colonius, “On the formation and recurrent shedding of ligaments in droplet
aerobreakup,” J. Fluid Mech. 904, A20 (2020).
25K. Schmidmayer, F. Petitpas, E. Daniel, N. Favrie, and S. Gavrilyuk, “A model
and numerical method for compressible ﬂows with capillary effects,”
J. Comput. Phys. 334, 468–496 (2017).
26K. W. Thompson, “Time dependent boundary conditions for hyperbolic sys-
tems,” J. Comput. Phys. 68, 1–24 (1987).
27K. W. Thompson, “Time-dependent boundary conditions for hyperbolic sys-
tems, II,” J. Comput. Phys. 89, 439–461 (1990).
28J. C. Meng and T. Colonius, “Numerical simulations of the early stages of high-
speed droplet breakup,” Shock Waves 25, 399–414 (2015).
29J. J. Quirk and S. Karni, “On the dynamics of a shock–bubble interaction,”
J. Fluid Mech. 318, 129 (1996).
30E. Johnsen and T. Colonius, “Numerical simulations of non-spherical bubble
collapse,” J. Fluid Mech. 629, 231–262 (2009).
31This rather simple approach was already exploited by Iakovlev 38 to investigate
the possible inception of shock-induced cavitation in submerged cylindrical
shell systems.
32G. Lajoinie, T. Segers, and M. Versluis, “High-frequency acoustic droplet
vaporization is initiated by resonance,” Phys. Rev. Lett. 126, 034501 (2021).
33T. Po/C20zar et al. , “Cavitation induced by shock wave focusing in eye-like experi-
mental conﬁgurations,” Biomed. Optics Exp. 11, 432–447 (2020).
34W. Wu, B. Wang, and G. Xiang, “Impingement of high-speed cylindrical drop-
lets embedded with an air/vapour cavity on a rigid wall: Numerical analysis,”
J. Fluid Mech. 864, 1058–1087 (2019).
35W. Wu, Q. Liu, and B. Wang, “Curved surface effect on high-speed droplet
impingement,” J. Fluid Mech. 909, A7 (2021).
36J. Field, J. Dear, and J. Ogren, “The effects of target compliance on liquid drop
impact,” J. Appl. Phys. 65, 533–540 (1989).
37T. Kondo and K. Ando, “One-way-coupling simulation of cavitation accompa-
nied by high-speed droplet impact,” Phys. Fluids 28, 033303 (2016).
38S. Iakovlev, “On the possibility of shock-induced cavitation in submerged
cylindrical shell systems,” J. Fluids Struct. 50, 437–460 (2014).
Physics of Fluids ARTICLE scitation.org/journal/phf
Phys. Fluids 33, 097104 (2021); doi: 10.1063/5.0063827 33, 097104-9
Published under an exclusive license by AIP Publishing
 29 August 2026 08:24:19
