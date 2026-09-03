<!-- PDF_PAGE: 1 -->

Free underexpanded jets in a quiescent medium: A review
Erwin Franquet a,b,n, Vincent Perrier b,c, Stéphane Gibout a, Pascal Bruel d,b
a LaTEP-ENSGTI, Univ. Pau & Pays Adour, Bâtiment d 'Alembert, rue Jules Ferry, 64 075 Pau Cedex, France
b Inria C AGIRE team, 200 rue Vieille Tour, 33 405 Talence Cedex, France
c LMAP, UMR CNRS 5142, Univ. Pau & Pays Adour, France
d CNRS, Univ. Pau & Pays Adour, LMAP, UMR CNRS 5142, France
article info
Article history:
Received 29 April 2015
Received in revised form
24 June 2015
Accepted 25 June 2015
Available online 14 July 2015
Keywords:
Underexpanded jet
Singular re ﬂection
Potential core
Mach disk
Farﬁeld zone
Asymptotic zone
Similarity laws
Equivalent diameter
Notional nozzle
abstract
When dealing with high-pressure releases, be it needed by some operating conditions or due to an
emergency protocol or even to the occurrence of an accident, one has to consider the relevant risks
associated to this leakage. Indeed, in addition to the mechanical and blast effects, the dispersion of the
released ﬂuid is of primary importance if it is hazardous, as an example for toxic gases or ﬂammable ones
(where explosions or ﬁres may be expected).
In fact, despite the numerous studies dealing with underexpanded jets, many aspects of their
structure are not clearly described, particularly when one seeks for quantitative predictions. By per-
forming an exhaustive overview of the main experimental papers dealing with underexpanded jets, the
present paper aims at clarifying the characteristics which are well known, from those where there is
clearly a lack of con ﬁdence. Indeed, and curiously enough, such a work has never been done and no
review is available on such a topic.
Two particular regions have drawn most of the attention so far: the near ﬁeld zone, where the shocks/
rarefaction pattern that governs the structure of the jet is encountered, and the far ﬁeld zone, where the
ﬂow is fully developed and often approximated by an equivalent ﬂow.
Finally, some clues are given on the numerical methods that may be used if one wants to study such
jets numerically, together with an emphasis on the speci ﬁc thermodynamical dif ﬁculties associated to
this kind of extreme conditions.
& 2015 Elsevier Ltd. All rights reserved.
Contents
1. Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
2. Forewords . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
3. Structure of the jet . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
3.1. General features. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
3.2. Near ﬁeld zone . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
3.3. Far ﬁeld zone . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
4. Potential core of a highly underexpanded jet . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
4.1. The Mach disk . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30
4.1.1. Position . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
4.1.2. Diameter. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33
4.1.3. Apparition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33
4.1.4. Conclusion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35
4.2. Spatial extension of the jet . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35
4.2.1. Initial divergence angle . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35
4.2.2. Diameter. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35
4.2.3. Length of the ﬁrst cell . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38
Contents lists available at ScienceDirect
journal homepage: www.elsevier.com/locate/paerosci
Progress in Aerospace Sciences
http://dx.doi.org/10.1016/j.paerosci.2015.06.006
0376-0421/& 2015 Elsevier Ltd. All rights reserved.
n Corresponding author at: LaTEP-ENSGTI, Univ. Pau & Pays Adour, Bâtiment d'Alembert, rue Jules Ferry, 64 075 Pau Cedex, France. Fax: þ33 559407725.
E-mail address: erwin.franquet@univ-pau.fr (E. Franquet).
Progress in Aerospace Sciences 77 (2015) 25 –53

<!-- PDF_PAGE: 2 -->

4.2.4. Wavelength of the cell structures . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38
4.2.5. Length of the potential core . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38
4.2.6. Mixing layer . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39
4.3. Evolution of the ﬂow variables . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39
5. Far ﬁeld zone of a highly underexpanded jet . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40
5.1. Notional or ﬁctional or equivalent nozzle . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40
5.1.1. Equivalent diameter [250] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40
5.1.2. Pseudo-diameter approach [224] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40
5.1.3. Sonic jet approach [57] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40
5.1.4. Momentum-velocity approach [227] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40
5.1.5. Improved pseudo-diameter approach [225] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41
5.1.6. Adiabatic expansion approach [238,207,248] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41
5.1.7. Mach disk approach [197,241] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42
5.1.8. Underexpanded jet theory [251] . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42
5.1.9. Comparison of the various approaches. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42
5.2. Evolution of the variables . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42
5.3. Conclusion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45
6. Modeling approaches . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46
7. Thermodynamical behavior of the ﬂu i d ................................................................................... 4 7
8. Conclusion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 48
Appendix A. Isentropic relations for a perfect gas . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 48
A.1. Expressions in function of the Mach number and the stagnation state . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 48
A.2. Expressions in function of the Mach number and the critical state . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 48
A.3. Relations between stagnation and critical state . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 48
Appendix B. Normal shock relations for a perfect gas . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 48
B.1. Expressions in function of the Mach number before and after the shock . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 48
B.2. Expressions in function of the Mach number before the shock . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 48
Appendix C. Discharge coef ﬁcient . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49
Appendix D. Overview of the various studies dealing with the structure of underexpanded jets . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49
References . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49
1. Introduction
Historically, the underexpanded jets have long been studied,
particularly by some of the most famous scientists [1–8]. They are
involved in practical engineering and challenging situations, such
as exhaust and plumes of aircrafts and rockets (where the thermal
signature, jet noise and screech or ﬂow behavior were studied),
and mixing issues in supersonic combustors or parallel injection,
and accidental leakage of pressurized ﬂuid, etc. In each of these
situations, the main features concerning the risk prediction and
control are linked to the overall structure of the jet, that is to say
the pressure (or temperature, or velocity) levels attained in its
surrounding, and to the knowledge of the concentration evolution,
which permits a comparison with some physical criterion (such as
the permissible exposure limits or the in ﬂammability limits).
Generally, one distinguishes between the free jets and the im-
pacting ones, and the exhausted ﬂuid may be released either in a
quiet medium or in a moving one (i.e. a co ﬂow jet or a jet in cross-
ﬂow). Besides, the jet may be either axi-symmetric or present an
asymmetry. The present review will concentrate on the former
conﬁguration.
Nowadays, thanks to all the associated papers, the overall
structure of underexpanded jets is very well known. Yet, in spite of
the large amount of studies that has been published, many char-
acteristic features or quantitative aspects are still ill-known or
even ignored by those numerous publications, e.g. the curvature of
the Mach disk, the characteristic lengths of the jet in the super-
sonic case or with various jet/ambient ﬂuids, the position where
entrainment arises, the turbulent transition in the mixing layer,
the interactions between hydrodynamic instabilities and the shock
waves pattern, the ﬁne and complete structure of turbulent vor-
tices, the method to correctly approximate the ﬂow in the far ﬁeld
region, etc. Moreover, there sometimes exists a large scattering
between the different measurements, which are even sometimes
occasionally in contradiction.
In order to have a fair view of the reliable results among all the
available studies, the goal of this paper is thus to propose an ex-
haustive analysis of the open literature on axi-symmetric free
underexpanded jets by comparing the qualitative and also quan-
titative predictions proposed therein. Thereby, the aim is to know
exactly in which characteristics and associated correlations we
may have con ﬁdence in. Let us mention here that we are mainly
considering experimental studies.
The paper is organized as follows: in Section 2, a brief summary
is given on the physical appearance of axi-symmetric under-ex-
panded jets, and their global structure is presented in Section 3 .
Then, a deeper description of the potential zone (near ﬁeld region)
and of the fully developed one (far ﬁeld zone) is given in Sections
4 and 5. Finally, an overview of the numerical models and methods
that may be used to further improve our knowledge of the under-
expanded jets is proposed in Section 6 . The possible issues raised
by the thermodynamical behavior of the ﬂuid are addressed in
Section 7 .
2. Forewords
An underexpanded jet may occur whenever a ﬂuid is released
from a device at a pressure greater than the ambient pressure. It is
known from a long time that such a behavior arises with con-
vergent and convergent –
divergent nozzles (holes being a parti-
cular case of these ones), as recalled in [9–11 ].
For a convergent nozzle, two main situations may be en-
countered, depending on the initial pressure of the ﬂuid or, more
precisely, on the ratio between the total pressure of the ﬂuid and
that of the ambient atmosphere. Thus, two different regimes with
different evolutions of the pressure inside the device are en-
countered, as depicted in Fig. 1 . The associated evolutions of the
E. Franquet et al. / Progress in Aerospace Sciences 77 (2015) 25 –5326

<!-- PDF_PAGE: 3 -->

mass ﬂow and exit pressure are also shown in Fig. 2(a) and (b). The
ﬁrst regime corresponds to the subsonic case, where the exit
pressure is equal to the ambient pressure and the mass ﬂow in-
creases with the initial pressure (cases a and b). In the second one,
the critical state where the ﬂow becomes sonic (case c) is attained,
the nozzle is now choked: the exit pressure is equal to the critical
pressure and the mass ﬂow is maximal. Except for the marginal
effects due to the presence of the boundary layer, the ﬂow now
mainly depends on the total conditions. Above this point, all the
variables have the same behavior inside the nozzle (case d) yet the
exit pressure is now greater than the ambient pressure: pressure
equilibrium will occur outside the device and therefore it gives rise
to an underexpanded jet.
For a convergent –divergent nozzle, the longitudinal pressure
evolution, the mass ﬂow and the exit pressure are also presented
in Figs. 3 and 4. As in the previous case, the ﬂow is ﬁrst subsonic
(case b) where the exit pressure equals the ambient pressure and
the mass ﬂow is governed by the ratio between the total pressure
and the ambient pressure. Then, the choked state (cases c –g) is
attained: the ﬂow is sonic at the throat and the mass ﬂow only
depends on the total conditions (ignoring once more the small
effects due to viscous phenomena). From now, except for the de-
sign operating conditions (case e), the exit pressure will be dif-
ferent from the ambient pressure: if it is lower (case f) it corres-
ponds to an overexpanded jet, otherwise (case g) it is an under-
expanded jet.
To quantitatively assess the appearance of an underexpanded
jet, the following pressure ratios are de ﬁned
P
P 10
0η =
()∞
P
P 2e
eη =
()∞
From the above discussion, underexpansion appears only if
P
P 30
0η ≥ ()⋆
When dealing with CV –DV nozzles, a supplementary condition is
required:
1 4eη > ()
Fig. 1. Longitudinal pressure evolution in a convergent nozzle for various pressure
ratios.
Notation
Latin Letters
a virtual origin (m)
A area (m 2)
c sound velocity (m s /C0 1)
cp speciﬁc heat capacity (J K /C0 1 kg/C0 1)
CD discharge coef ﬁcient ( –)
D diameter (m)
h speciﬁc enthalpy (J kg /C0 1)
Kn Knudsen number ( –)
L length (m)
M Mach number ( –)
P pressure (Pa)
lR universal ideal gas constant (J K /C0 1 mol/C0 1)
R relative ideal gas constant (J K /C0 1 kg/C0 1)
r radial position (m)
Re Reynolds number ( –)
T temperature (K)
V velocity (m s /C0 1)
v speciﬁc volume (m 3 kg/C0 1)
x longitudinal position (m)
Y mass fraction ( –)
Greek Letters
α volume fraction ( –)
β nozzle angle ( °)
γ polytropic coef ﬁcient ( –)
ζ decay constant ( –)
κ decay constant ( –)
λ wavelength (m)
η pressure ratio ( –)
ρ density (kg m /C0 3)
ν Prandtl–Meyer angle ( °)
θ divergence angle of the jet ( °)
Superscripts and subscripts
0 stagnation (or total) state
∞ ambient conditions
n critical state (i.e. sonic ﬂow)
¢ cell
c critical point (thermodynamical de ﬁnition)
e exit plane
eq equivalent
id ideally expanded
t throat
Abbreviations
CV convergent
CV–DV convergent –divergent
KH Kelvin –Helmholtz
MD Mach disk
NZ near ﬁeld zone
RR regular re ﬂection
SR singular re ﬂection
TZ transition zone
TP triple point
TG Taylor –Goertler
FZ far ﬁeld zone
E. Franquet et al. / Progress in Aerospace Sciences 77 (2015) 25 –53 27

<!-- PDF_PAGE: 4 -->

Generally, the differences between various gases are quite small
[12–14] and the previous method gives reliable results. None-
theless, the perfect gas equation of state is not able to deal with all
the situations or ﬂuids and may not perfectly describe the
thermodynamical behavior of the ﬂow in such a case. To improve
the results, and better describe the real behavior of the ﬂuid, one
may incorporate a discharge coef ﬁcient CD (detailed in Appendix
C) to better estimate the mass- ﬂow rate or study the in ﬂuence of
the equation of state on the properties of the ﬂuid at the throat
and/or at the exit of the nozzle (see Section 7 for further
information).
3. Structure of the jet
3.1. General features
As mentioned previously, an underexpanded jet occurs when
the pressure at the end of a device, may it a nozzle or a hole, is
greater than the ambient pressure. The transient behavior of the
ﬂuid has not focused attention of many studies, be it theoretical
[15] or experimental [16–19] or numerical [17,18,20–26] ones. On
the contrary, the steady state of the ﬂow has been largely studied
in the past [27–53] , since it corresponded to the most often en-
countered situations. To brieﬂy summarize its main characteristics,
the compressible and viscous effects compete together to impose
the overall structure of the jet. Generally, it is usual to distinguish
three zones inside the jet:
1. the near ﬁeld zone;
2. the transition zone;
3. the far ﬁeld zone.
The nearﬁeld zone is divided into two parts: the core part and
the mixing layer. In the ﬁrst one, the ﬂow is isolated from the am-
bient ﬂuid and its behavior is mainly dominated by compressible
effects (which explains why this zone is sometimes called the gas-
dynamic region). The ﬂuid undergoes an isentropic expansion, up to
recompression through shock waves (described farther down-
stream). In the other part, turbulence effects induce an exchange
Fig. 2. Evolution of the variables in a convergent nozzle for various pressure ratios: (a) mass ﬂow and (b) exit pressure.
Fig. 3. Longitudinal pressure evolution in a convergent –divergent nozzle for var-
ious pressure ratios.
Fig. 4. Evolution of the variables in a convergent –divergent nozzle for various pressure ratios: (a) mass ﬂow and (b) exit pressure.
E. Franquet et al. / Progress in Aerospace Sciences 77 (2015) 25 –5328

<!-- PDF_PAGE: 5 -->

between the ejected ﬂuid and the surrounding one, characterized by
large turbulent structures (vortex) which grow regularly down-
stream of the ﬂow. In this shearing zone, a supersonic part, between
the frontier of the jet and the constant pressure line, and a subsonic
one, between this line and the potential core, may be distinguished.
At the end of the near ﬁeld zone, the sonic line attains the axis and
therefore the mixing layer has completely replaced the inner part.
Then, it corresponds to the beginning of the transition zone where
the variations of the variables are small, be it longitudinally or ra-
dially. This permits a better mixing of the two ﬂuids, the ejected one
and the ambient one, leading to a homogenization of the pressure
ﬁeld since the entrainment now takes place everywhere.
Eventually, in the far ﬁeld zone, the jet is perfectly expanded,
the ﬂow is developed and its characteristics (mean pressure,
temperature and velocity) are self-similar. The longitudinal velo-
city and the temperature on the axis are inversely proportional to
the distance from the exit plane, and their radial evolution may be
described by a gaussian pro ﬁle centered on the axis. Let us men-
tion here that depending on the various communities, and espe-
cially those involved in hydrogen (or combustible gas) safety or
those from the turbulence ﬁeld, one sometimes split this zone into
two others: a momentum-dominated one followed by a buoyancy-
controlled regime which are characterized by different Froude
number.
3.2. Near ﬁeld zone
In this region, the ﬂow is mainly governed by the compressible
effects and is rather steady. Practically, the relevant parameter is
the pressure ratio. Moreover, the exit Mach number and the di-
vergence angle of the jet in the exit plane may have some in ﬂu-
ence. Thus, four different situations are possible:
1. under-expansion of the ﬂuid is low, a normal shock is present
in the exit plane. Typically, for air, it corresponds to 1 1.1eη≤≤
[34] or to 1 1.90η≤≤ [38].
2. the jet has a “diamond” or “X” structure, depicted in Fig. 5 ,
which corresponds to a moderately underexpanded jet detailed
hereafter.
3. the jet has a “barrel” or “bottle” structure, shown in Fig. 6 ,
meaning a Mach disk appears (due to a singular re ﬂection). It
corresponds now to a highly underexpanded jet also described
below.
4. the structure is dominated by a unique barrel, as depicted in
Fig. 7 , and the jet is said to be very highly (or extremely)
underexpanded.
Moderately underexpanded jet (see Fig. 5 ): In the exit plane
(marker 0), a Prandtl –Meyer expansion fan (marker 2) expands the
ﬂuid downstream of the lips of the device up to the jet boundary
corresponding to the external surface of the mixing layer (marker
JB). When these acoustic waves attain the constant pressure
streamline (marker 3), where the pressure equals the ambient
pressure, they are re ﬂected into compression waves. Then, these
ones converge towards the inner jet and coalesce to form an ob-
lique shock (marker 4), usually called the intercepting shock. On
the axis, this incident shock itself re ﬂects in a new oblique shock,
the re ﬂected shock (marker 5), facing the outer jet. Eventually,
when this shock wave encounters the constant pressure stream-
line it gives birth to a new expansion fan (marker 6) which permits
us to replicate the cell structure further downstream. In the case of
air, this situation is achieved for an exit pressure ratio
1.1 3 eη≲≲
[34,38,54] or for a total pressure ratio 2 40η≲≲ [38,13,55].
Highly underexpanded jet (see Fig. 6 ): When the pressure ratio
increases, the regular re ﬂection of the intercepting shock can no
longer happen on the axis. Consequently, above a critical angle,
this re ﬂection becomes singular and leads to the apparition of a
normal shock, called the Mach disk (marker 5). There, the point
where the intercepting shock, the Mach disk and the re ﬂected
shock intersect themselves (marker 6) is called the triple point. A
slipstream (marker 7) then emanates from this point: this is an
embedded shear layer separating the ﬂow behind the Mach disk
(which is subsonic) from the ﬂow downstream of the re ﬂected
shock (which is supersonic). Typically, this corresponds to an exit
pressure ratio
2 4eη≲≲ [30,34,38,56–61,43,54] or to a total
pressure ratio 4 5 70η−≲ ≲ [62–65,35,38,59,13].
Very highly (extremely) underexpanded jet (see Fig. 7 ): With a
further increase of the pressure ratio, the number of shock cells
diminishes up to a point where the potential core is dominated by
the ﬁrst cell, this one being unique and no other structures being
formed. In such a case, the Mach disk can no longer be considered
as a normal shock and its curvature has to be taken into account.
The total diameter of the jet will diminish due to momentum
exchange, caused by the entrainment of the ambient ﬂuid, leading
to a very long plume. Typically, this corresponds to an exit pres-
sure ratio
3 4 eη−≲ [57,43] or to a total pressure ratio 70η ≥ [35].
3.3. Far ﬁeld zone
In this region, the jet has achieved a self-similarity, yet com-
pressible effects may still be present since the Mach number may
be greater than 0.3 (or even supersonic). From a qualitative point
of view, the normalized radial pro ﬁles of the mean variables obey
the same law (usually given by a Gaussian pro ﬁle).
Nevertheless, it appears that in this region one may describe
the ﬂow as a classical jet, i.e. as an ideally expanded jet, by scaling
some of the basic ﬂow parameters. Indeed, it does not matter
anymore here how exactly the ﬂuid comes to this state, which
means that it is not mandatory to have a perfect description of the
nearﬁeld zone and of the associated structure (shock wave pattern,
number of Mach disks, etc.). The point is that one has to deal with
a supersonic jet, behaving as classical jets but apparently coming
from a larger source than the real one. This is the only testimony of
its original underexpanded feature. In Section 5 , this zone will be
further described along with the various description approaches of
the jet behavior.
4. Potential core of a highly underexpanded jet
The main goal of this section is to detail the characteristics of
highly and extremely underexpanded jets, where a singular re ﬂex-
ion occurs. In particular, to have a fair view of the different features,
Fig. 5. Structure of a moderately underexpanded jet.
E. Franquet et al. / Progress in Aerospace Sciences 77 (2015) 25 –53 29

<!-- PDF_PAGE: 6 -->

quantitative and theoretical results (whenever available) are pre-
sented and discussed. A summary of all the available results is
presented in Table 2.
4.1. The Mach disk
This is certainly the most studied feature in the literature, be it
experimentally [12,30,35,40,43,49,51,56–59,62,64,66–94],t h e o r e t i -
cally [13,29,67,76,78,95–109] or numerically [14,20,22,34,41,59,63,75,
81,82,84,91,110–122].Yet, if one tries to understand the reason for
t h ea p p e a r a n c eo faM a c hd i s k ,t h e r ei ss t i l ls o m ed o u b ta b o u tt h e
underlying physical mechanisms. More precisely, in the passage from
ar e g u l a rr eﬂection to a singular re ﬂection, accompanied by the
appearance of the Mack disk, it is well known that the detachment of
t h es h o c kw a v e so c c u r sb e c a u s et h i si st h eo n l yw a yf o rt h eﬂow to
adjust to a subsonic regime [10, Chap. 16] or [1 1, Chap. 7] but
the moment when this phenomenon occurs is quantitatively poorly
known, especially the dependency (and interactions) on the pressure
Fig. 6. Structure of a highly underexpanded jet.
Fig. 7. Structure of a very highly underexpanded jet.
E. Franquet et al. / Progress in Aerospace Sciences 77 (2015) 25 –5330

<!-- PDF_PAGE: 7 -->

range and exit Mach number, on the ﬂuid properties – i.e.
the polytropic coefﬁcient – on the geometry of the nozzle and exit
nozzle angle [96,29,62,30,98–10 0,12,64,123,43,124,84,13,107,90,54].
Nonetheless, among the theoretical studies, the Mach disk location
has been supposed to appear at a position such that
/C15 the conservation equations are satis ﬁed for the section per-
pendicular to the axis [95].
This hypothesis has the advantage to rely on physical back-
grounds, yet some discrepancies appear when compared with
the experiments. They are supposed to come from viscous ef-
fects that are ignored.
/C15 The associated slip line will permit a correct re-acceleration of
the ﬂow downstream [96,106,107].
From [107,108], this leads to the best results when compared
with the experiments.
/C15 It corresponds to a normal shock bringing the static pressure to
the ambient pressure [29].
As mentioned in [100], if true, it will be the case only for the
last Mach disk.
/C15 The Mach disk is a normal shock at the triple point [98].
/C15 The static pressure behind the intercepting shock reaches a
minimum [100].
Furthermore, a large scattering may be noted between some
results, as seen farther. Sometimes, these discrepancies do not per-
mit us to correctly identify a unique relation for some parameters of
the Mach disk. In what follows, we consequently propose to list the
main features and the associated results expressed in function of the
total pressure ratio η
0 or the exit pressure ratio ηe.
4.1.1. Position
Among the huge amount of studies, it appears that the Mach
disk location is
/C15 mainly governed by the pressure ratio [29,30,62,67–70,72,74–
76,124–129,12,57,78,64,81,43,105,83–87,121,89–92,109];
/C15 increased by the exit Mach number (for supersonicﬂow obtained
with convergent–divergent nozzles) [29,30,68,72,78,12,83,43,105,
124,128,89,90];
/C15 independent of the ﬂuid [67,74,78,83,43];
/C15 not clearly inﬂuenced by the exit nozzle angle since some studies
show no noticeable effects [62,68–70,74,78] while others present
some inﬂuence [29,56,30,126,82,43,90],u s u a l l yw e a k ,l e a d i n gt o
a diminution of LMD with the nozzle angle β. Generally, this effect
is mainly attributed to the vena contracta phenomenon detailed
in Appendix C.
As a ﬁnal remark on this point, we will relate it to the discussion
developed in Section 4.1.3concerning the apparition of the Mach
disk and the inﬂuence of the nozzle angle on the pressure ratio at
which theﬂow switches from a regular reﬂection to a singular one.
Finally, in addition to the limits discussed above, we will mention
that some authors observe experimentally an oscillation in the
position of the Mach disk [77] and its thickness seems to increase
with the pressure ratio [88]. Eventually, some numerical studies
seem to underline an hysteresis in this position in function of the
pressure ratio [41,130,21,115 ].
An exhaustive overview has been conducted on all the experi-
mental studies available and, to compare all the results together, the
measurements were non-dimensionalised by the exit diameter De.
We present here the main conclusions, and will refer any interested
reader to [131]for a complete analysis. If oneﬁrst consider the results
g i v e ni nf u n c t i o no fη
0 [62,67,74,64,40,81,103,84,86,87,90,92,109],w e
may see in Fig. 8 that the various measurements collapse on a single
curve. Then it appears that relations of[67,74,64] correlate pretty well
the measures. We will keep that of [74], since it was analytically ob-
tained and validated on the largest pressure ratio range:
L
D 2.4 0.645497
5e
MD 0
0
η η==
()
If we now consider the measurements expressed in function of
ηe [29,56,30,68,69,72,75,76,126,125,12,57,78,82,83,43,105,129,121,
89,91], the behavior of the position is now less clear, as shown in
Fig. 9 . Indeed, there seems to have no in ﬂuence of the ﬂuid (but
there are too few ﬂuids to be sure on that point) and it is not
possible to ﬁnd a unique relation which gives a good ﬁt of the
results, especially concerning the role of the Mach number. Finally,
let us mention that the tested pressure ratio range is shorter than
in the previous case, and secondly that only few measurements
are available for some Mach numbers, and thirdly that dis-
crepancies may attain 50%. Consequently, in order to separate the
wheat from the chaff, using the previous result and supposing that
the exit pressure ratio η
e may be computed from the total pressure
ratio η0 thanks to Eq. (68) (which corresponds to the hypothesis of
a perfect gas behavior), it may be checked that relations proposed
by [12,83] agree very well with Eq. (5) of [74] in the case of a sonic
exit. Therefore, we propose to retain the relation of [83], because it
is based on a larger set of experimental points:
L
D M0.69
6e
e e
MD γη=
()
Conclusion: To summarize, when we have a convergent nozzle,
the best estimation of the position of the Mach disk is given by Eq.
(5), namely:
L
D 2.4 0.645497
7e
MD 0
0
η η==
()
Similar results are also obtained with Eq. (6), which also applies to
convergent–divergent nozzles and consequently the Mach disk for
an underexpanded jet with supersonic exit Mach numbers is
located at
L
D M0.69
8e
e e
MD γη=
()
Fig. 8. Position of the Mach disk in function of the total pressure ratio.
E. Franquet et al. / Progress in Aerospace Sciences 77 (2015) 25 –53 31

<!-- PDF_PAGE: 8 -->

Fig. 9. Position of the Mach disk in function of the exit pressure ratio: (a) results for Me ¼1.0; (b) results for Me ¼1.5; (c) results for Me ¼1.75; (d) results for Me ¼2.0;
(e) results for Me ¼2.5; and (f) results for Me ¼3.0.
E. Franquet et al. / Progress in Aerospace Sciences 77 (2015) 25 –5332

<!-- PDF_PAGE: 9 -->

The in ﬂuence of the nozzle angle, even small, is yet not clearly
understood. Thus, one does not know if it is the same with various
pressure ratios and how it quantitatively affects the position of the
Mach disk.
4.1.2. Diameter
This feature has clearly been less studied than the Mach disk
position, however it appears that it is
/C15 mainly governed by the pressure ratio [62,56,30,67–69,74,
81,43,124,
128,14,85,129];
/C15 apparently decreased when the exit Mach number increases
[30,68,12,114,43,90], as discussed below in Section 4.1.3,y e t
some authors disagree with this conclusion [124,51,52];
/C15 different for various gases [74,125,84,13] and inversely pro-
portional to γ;
/C15 strongly dependent on the nozzle geometry and shape[62,30,67–
69,81,14]. It seems that for convergent nozzles it decreases with
increasing nozzle angle [56] whereas for convergent–divergent
nozzles it increases with the nozzle angle [30].
Similar to what was done in the previous section, we will present
the main results and correlations, in a non-dimensionalised form,
using the same methodology as above. Once more, all the corre-
sponding results and further discussions are available in [131].S o ,
concerning the results in function of η
0 [62,74,64,81,84,14],p r e -
sented in Fig. 10,t h e ﬁrst remark to be done concerns the dis-
crepancies among the measurements, particularly for the low
pressure ratios. Thus, a linear function (depicted in green) could be
preferably used in this range, even if the correlation is not excellent.
On the contrary, for the high pressure ratios, another ﬁtted curve (in
blue) clearly shows a dependency with the square root of η
0,a s
suggested by [7 4]. Eventually, it means that one should take for the
diameter of the Mach disk in function of η0 the relations of [62] for
low pressure ratios 50(≳ ):
⎧
⎨⎪
⎩⎪
D
D
0.36 3.9 for a contoured nozzle
0.31 5 for a conical nozzle or an orifice 9e
MD 0
0
η
η
=
−
− ()
and for higher pressure ratios, either the ﬁtted curves (in black and
blue) or the relation proposed by [74]:
D
L cte if 1
10
MD
MD
0η⟶⪢
()
the corresponding constant being 0.6 or 0.4 for converging and
straight or diverging nozzles respectively [81], which is very close
to the values 0.43 and 0.57 found when using the ﬁtted curves for
the computation.
Concerning the results given in function of ηe [56,30,68,72,76,57,
43,105,129,121,91],p r e s e n t e di nFig. 1 1, it is worth mentioning that
pressure ratios tested are really narrower than before and, in the
same time, discrepancies between the measurements are also more
important. In particular, there is no obvious relation permitting us to
predict the behavior in function of the exit Mach number. If only one
estimation should be kept, with the previous warnings in mind, then
those of [30] for low pressure ratios
100(≳ ) could be retained (al-
though it is valid only for convergent nozzles):
D
D
5
2 log 3
4 11e
e
MD η=−
()
or the one of [68] for larger ratios:
⎛
⎝⎜
⎞
⎠⎟D
D A 1.0
12e
e
MD
3 η=−
()
with A3 a constant depending on the exit Mach number, as shown
in Table 1.
Conclusion: In summary, this feature is relatively well known only
for convergent nozzles but there is still several candidates to re-
present the diameter of the Mach disk, be it Eq. (9) or (10) de-
pending on the pressure ratio involved. Nevertheless, the role of γ is
not described in these relations, although the diameter is inversely
proportional to this parameter. In the case of convergent –divergent
nozzles, and in particular when the exit ﬂow is supersonic, the
measurements do not permit us to retain unambiguously a relation
among the available ones. Furthermore, there is no pertinent argu-
ments to conclude on the role of the Mach number. In addition to
the above-mentioned restrictions, the quantitative effects of the
nozzle angle are still not well understood. Eventually, this means
that there is clearly a lack of knowledge when one wants to compute
the diameter of the Mach disk.
4.1.3. Apparition
Among the available papers, experimental [62,30,12,64,123,
124,90],t h e o r e t i c a l[96,29,98–100,107] or numerical [132,114,41,
115 ] , i t i s d ifﬁcult to ﬁnd quantitative results concerning the passage
between regular and singular reﬂection. However, it seems that the
boundary layer behavior and consequently the velocityﬁeld and the
structure of the ﬁrst cell are in ﬂuenced by the shape of the nozzle
(especially for CV –DV ones) [62,56,30]. Thus, it is usually admitted
that the singular re ﬂection, that is to say the apparition of a Mach
disk, occurs for a wider pressure range if
/C15 the exit Mach number increases [30,12,114,124,90,54];
/C15 γ is increased [84,13].
Concerning the in ﬂuence of the nozzle angle, it seems that it
competes with the in ﬂuence of the exit Mach number. Its increase
leads to a larger regular re ﬂection domain for CV nozzles [62] and
to a reduction of this domain for CV –DV nozzles [30,43]. Based on
these results, Antsupov [30] proposes the following relation for
the limiting nozzle angle above which the Mach disk appears:
Fig. 10. Diameter of the Mach disk in function of the total pressure ratio. (For in-
terpretation of the references to color in this ﬁgure caption, the reader is referred to
the web version of this paper.)
E. Franquet et al. / Progress in Aerospace Sciences 77 (2015) 25 –53 33

<!-- PDF_PAGE: 10 -->

ab
cd
ef
Fig. 1 1. Diameter of the Mach disk in function of the exit pressure ratio: (a) results for Me ¼1.0; (b) results for Me ¼1.5; (c) results for Me ¼2.0; (d) results for Me ¼2.5;
(e) results for Me ¼3.0; and (f) experimental results.
E. Franquet et al. / Progress in Aerospace Sciences 77 (2015) 25 –5334

<!-- PDF_PAGE: 11 -->

Marctan 0.22 1 13eSR ()β =− ()
4.1.4. Conclusion
To have an overall summary, it appears that the only parameter
which is pretty well known, in the sense of a reliable relation
giving acceptable predictions, is solely the Mach disk location. On
the contrary, the corresponding diameter may be computed only
in a few cases and there are still uncertainties on its expression (in
particular, when one wants to identify the role of each parameter,
especially the thermodynamic behavior depicted by γ). Moreover,
the thickening and curving of the Mach disk are rarely considered,
and almost none information is available for these features.
4.2. Spatial extension of the jet
We present here the main features of the other characteristic
quantities of underexpanded jets. Here again, the interested reader
is referred to [131] for the complete set of data and related
discussions.
4.2.1. Initial divergence angle
As the gas emerges from the device, it is known to undergo a
Prandtl–Meyer expansion. In the general case, the angle taken by
the jet depends on the nozzle angle and on the Prandtl –Meyer
angle, which one is dependent on the ambient Mach number and
the exit Mach number (and consequently on the pressure ratio).
Moreover, it appears that the nozzle geometry may modify the
initial jet angle [56,133,117,118,128,14,129,53]. Eventually, the
thermodynamical behavior of the ﬂuid may also play a signi ﬁcant
role since the angle is inversely proportional to γ [74,43,53] and
real gas effects increase the jet divergence [129].
4.2.2. Diameter
When considering this feature, one has to pay attention be-
cause it may be related either to the plume jet boundary or to the
intercepting shock. Therefore, both characteristics are studied se-
parately henceforth.
Diameter of the jet : This feature is not easily studied, and con-
sequently it is uneasy to ﬁnd quantitative results among the few
Table 1
A3 values with Me for the diameter of the Mach disk in Eq. (12).
Me 1234
A3 0.551 0.704 0.447 0.148
Table 2
Experimental studies of the near ﬁeld zone.
Study η0 ηe Me Species Devices Mach disk Jet
LMD DMD θ D L¢
Ref. [29] 2 – 70 1 – 3 Air a 1 CV nozzle þ XX
1t o4C V –DV nozzle
Ref. [62] 3–9 1 Air 5 CV nozzle þ 1 ori ﬁce X X
Ref. [56] 2.04 and 2.56 1 Air 9 CV nozzles X X X X
Ref. [30] 1–40 1 –5.05 Air þ 1 CV nozzle þ XX X X
alcohol-oxygen 16 CV –DV nozzles
Ref. [67] 15–17/C1 103 1 Air, Ar, N 2 1 CV nozzle þ 1 ori ﬁce X X
Ref. [68] 1.0–4 /C1 104 1–6.0 Air a XX X
Ref. [70] 1–104 1–4 Air a XX
Ref. [72] 5–105 1.0–3.0 X
Ref. [151] 2–7 1 Air CV nozzle X
Ref. [74] 10–3 /C1 105 1N 2, Air, He, He-Ar, 2 CV nozzles b XX
CO2, Freon 22
Ref. [35] 2–7 1 Air CV nozzle X
Ref. [75] 1.59–4.53 1 Air, Ar CV nozzle X X
Ref. [76] 97–506 1 burnt products CV nozzle X X
Ref. [125] 8–60 1 NO 2-N2O4 CV nozzle X X
Ref. [12] 29–916 1 –2.99 γ¼1.1, 1.4, 1.67 3 CV nozzles þ X
2C V –DV nozzles
Ref. [39] 6.6 1 Air CV nozzle X
Ref. [57] 2–15 1 Air 2 CV nozzles X
Ref. [78] 10–104 1–4.85 γ¼1.3–1.67 X
Ref. [79] 1–1 10 1 Air slot nozzle X
Ref. [64] 3.52–13 1 Air CV nozzle X X
Ref. [40] 174–4067 1 N2 CV nozzle X
Ref. [81] 5–90 1& 1.26 Air 3 nozzles X X
Ref. [82] 4–20 1.5, 2 N2 4C V –DV nozzles X
Ref. [123] 101–73 /C1 103 1 N2,C O 2 CV nozzle X
Ref. [83] 1–100 1 N 2,C O 2, He 2 CV nozzles X
Ref. [43] 1–120 1 –3 Air 20 CV –DV nozzles X X X
þ 1 CV nozzle
Ref. [84] 3.6–6.4 1 moist Air CV nozzle X X X
Ref. [85] 5–9 1 Air CV nozzle X X
Ref. [129] 2–105 1 Air CV nozzle X X
Ref. [86] 15–90 1 Air a CV nozzle X
Ref. [87] 4–20 1 Air 2 CV nozzles X
Ref. [89] 2–200 1 Air 3 CV nozzles X
Ref. [90] 5–42 1 –3.5 Air 4 CV nozzles X
Ref. [54] 1.6–40 1 N NO2 − 1 CV nozzle X X
a The ﬂuid used is not clearly given.
b In fact, the number of nozzles tested is not very clear. The authors tested several exit diameters, ranging from 0.026 to 0.1 19 in, for a contoured and a c onical nozzle.
E. Franquet et al. / Progress in Aerospace Sciences 77 (2015) 25 –53 35

<!-- PDF_PAGE: 12 -->

Table 3
Evolution of the variables in the near ﬁeld zone.
Study Work Axial evolution Radial evolution
Velocity Mach Pressure Density Concentration Velocity Mach Pressure Density Concentration
Ref. [191] Num.–Exp. X X X X X
Ref. [1 10] Num. X X
Ref. [66] Exp. X X
Ref. [144] Exp. X
Ref. [145] Exp. X
Ref. [30] Exp. X
Ref. [157] Exp. X
Ref. [67] Exp. X X
Ref. [70] Exp. X X
Ref. [32] Exp. XX
Ref. [132] Num. X
Ref. [134] Num.–Exp. X X
Ref. [135] Exp. X X X X
Ref. [63] Num. X
Ref. [192] Num.–Exp. X
Ref. [138] Num. X
Ref. [1 1 1] Num. X X
Ref. [147] Num. X X X
Ref. [148] Num.–Exp. X X X X
Ref. [151] Exp. X
Ref. [268] Num. X X X X
Ref. [34] Num. X X X
Ref. [35] Exp. X
Ref. [75] Num.–Exp. X X
Ref. [1 75] Num. X
Ref. [1 12] Num. X
Ref. [1 76] Num. X X X
Ref. [215] Num. X
Ref. [193] Exp. X
Ref. [77] Exp. X X X
Ref. [38] Exp. X
Ref. [1 13] Num. X X
Ref. [39] Exp. X X
Ref. [15] Exp. X
Ref. [216] Num. X X X X X
Ref. [195] Exp. X
Ref. [64] Exp. XX
Ref. [142] Exp. X
Ref. [217] Num. X
Ref. [156] Exp. X
Ref. [1 15] Num. X
Ref. [218] Num. X X X
Ref. [288] Exp. X X
Ref. [82] Exp. X
Ref. [159] Exp. X
Ref. [199] Exp. X X
Ref. [123] Exp. X
Ref. [200] Exp. X
Ref. [201] Exp. X X
Ref. [42] Exp. X
Ref. [1 16] Num. X X
Ref. [127] Exp. X X
Ref. [103] Exp. X
Ref. [202] Exp. X X
Ref. [289] Exp. X X
Ref. [205] Num.–Exp. X X X X X
Ref. [163] Exp. X
Ref. [152] Exp. X
Ref. [221] Num. X X
Ref. [14] Num. X
Ref. [21] Num. X
Ref. [210] Exp. X
Ref. [222] Num. X
Ref. [164] Exp. X
Ref. [184] Exp. X X X
Ref. [143] Exp. X
Ref. [120] Num. X
Ref. [55] Num. X X
Ref. [149] Exp. X
Ref. [51] Exp. X X X X
Ref. [52] Exp. X X
Ref. [87] Exp. X
Ref. [121] N u m . XX X X XX X
E. Franquet et al. / Progress in Aerospace Sciences 77 (2015) 25 –5336

<!-- PDF_PAGE: 13 -->

theoretical [29,30,133–136,99,76,10 0,43,128,46,53] and experi-
mental [64] and numerical papers [137,138,112,117,118,84,14]
thereon. To summarize, it is common to describe both the dia-
meter of the jet and its maximum value for which it appears that
/C15 both increase with the pressure ratio [30,68,69,65,43,85,129,53]
until a priori an asymptotic value [30,43];
/C15 they seem to increase with the exit Mach number [68,43,85]
even if some authors disagree on that point [30];
/C15 they increase with the nozzle angle [68,70,43,85];
/C15 they are inversely proportional to γ [30,74,43,85];
/C15 they are inversely proportional to the density ratio [134,135].
From a practical point of view, there are not so many data
permitting us to quantitatively describe this feature, essentially
because it was not so easy to clearly measure it. Thus, let us note
that only Antsupov [30] proposes a relation (for CV –DV nozzles
and for
40 :eη ≤)
⎛
⎝
⎜
⎞
⎠
⎟
⎛
⎝
⎜
⎞
⎠
⎟
D
Dmax 1 0.57
14e
e e
jet 0.6θη=+
()
Diameter of the intercepting shock : More studies have been
dedicated to this feature, both experimentally [56,69–71,123],t h e -
oretically [69,70,72,99,76,139,10 0,102,140,105,128,107] and numeri-
cally [141,137,138,112,117,118,84]. Surprisingly enough, the available
data are quite poor and one may only say that it
/C15 seems to be also dependent on the square root of the pressure
ratio [69,70,123];
/C15 may sometimes depend on the convergence angle [68,70,117 ]
even if it is not the case for some con ﬁgurations [56,70].
As before, if all the useful papers are analyzed [56,68,72,123],i t
may be seen in Fig. 12 that no argument emerges to discriminate
Fig. 12. Maximum value for the diameter of the intercepting shock in function of
the exit pressure ratio.
Table 3 (continued )
Study Work Axial evolution Radial evolution
Velocity Mach Pressure Density Concentration Velocity Mach Pressure Density Concentration
Ref. [223] Num. X X
Ref. [272] Num. X X
Ref. [206] Exp. X X
Ref. [122] Num.–Exp. X X X X
Ref. [150] Exp. X
Table 4
Experimental studies of the far ﬁeld zone.
Study η0 ηe Jeta Devices Species Measurements b
Concentration Velocity
Ref. [224] 2–70 V Nozzle NGc, C H24 X (A)
Ref. [225] 2–75 V Nozzle Air X (A)
Ref. [226] 100 H Ori ﬁce H CH,24 X (A)
Ref. [57] 5.7–20 H Nozzle Air, He X (A)
Ref. [244] 100 H Nozzle H2 X (A)
Ref. [251]
Ref. [290] 20–260 H Nozzle H2 X (A) X (A,R)
Ref. [291] 200–400 H Ori ﬁce H2 X (A)
Ref. [292] 5–25 H Ori ﬁce H2 X (A)
Ref. [230] 52–163 H Nozzle H2 X (A) X (A)
Ref. [231] 40 H Nozzle CH4, H2 X (R) X (A,R)
Ref. [247] 5–60 H Nozzle H2 X (R) X (A,R)
Ref. [248] 17–68.5 H Ori ﬁce H2 X (A) X (A,R)
Ref. [207] 1–20.3 H Nozzle Air X (A,R)
a Horizontal (H) or vertical (V).
b Axial (A) or radial (R).
c Natural gas with 92 –92.4% of CH4.
E. Franquet et al. / Progress in Aerospace Sciences 77 (2015) 25 –53 37

<!-- PDF_PAGE: 14 -->

the relations altogether, which are although very different.
Conclusion: Globally, there is a lack of data concerning this fea-
ture. Even if the dependency with the square root of the pressure
ratio seems reasonable, it is not clearly proven. Moreover, there is a
large scatter of the quantitative results since computations with the
various expressions available evidence a discrepancy of up to 50%.
4.2.3. Length of the ﬁrst cell
This feature is also poorly documented and there are still few
papers that give some insights on this characteristic length, be it
experimentally [56,30,75,64,43,91], theoretically [101,142,46,47,7]
or numerically [75,112,119,91]. The main reason is certainly the
various issues raised by its observation. However, the following
properties for the length of the ﬁrst cell may be retained:
/C15 it increases with the pressure ratio [30,75,64,43,47,121];
/C15 it increases with the exit Mach number [30,43,46,121];
/C15 it depends on the geometry of the nozzle [56,30,43,51].
From a quantitative point of view, the concerned papers
[56,30,75,64,43,47,91] only permit us to consider the case of
converging nozzles. Indeed, only the measurements of [43] are
concerned with supersonic exit Mach numbers. Consequently,
keeping only the sonic cases, a ﬁtted curve may be computed, as
shown in Fig. 13, yet the relation is not very good. If only one es-
timation is to be taken, then we propose to keep the empiric es-
timation of [43] (even if the authors agree themselves that it
seems to overestimate the cell length):
⎛
⎝⎜
⎞
⎠⎟
⎛
⎝⎜
⎞
⎠⎟
L
D MM
M
1.52 1.55 2 1 1 0.55 1
0.5 1
1.55 21 1
15
e
e ee
e e
¢ 0.437 2 2
2
()
η
η
=+ − − − −
+− − −
()
4.2.4. Wavelength of the cell structures
Once more, the behavior of the cell structures is badly known,
be it their exact number or the distance between each Mach disks
in the case of multiple cells, mainly because the ﬂow is not sta-
tionary on average anymore. Therefore, it is hard to determine
exactly the position of each shock. Although quantitative studies
are solely encountered, the number of structures is known to de-
pend on:
/C15 the pressure ratio [5,43,47,143,51,54];
/C15 the exit Mach number [143,51].
First, let us recall that it is not straightforward to compare
measurements obtained either with convergent nozzles or with
convergent–divergent ones. This implicitly raises the question of
the relation between each quantitative results given hereafter.
Furthermore, to the best of our knowledge, there are only a few
quantitative measurements and consequently the degree of con-
ﬁdence is not very high. If, as usual, all these measurements [143–
146,75,5] are compared altogether, which is done in Fig. 14,i ti s
straightforward to note that large discrepancies (up to 100%) exist
between the different measurements. Similarly, no expression
seems to be better than the other ones however the one of [143]
seems to be the most representative of the experimental results:
D M0.57 0.15
16e
id
2λ =−
()
4.2.5. Length of the potential core
Usually, it is admitted that the near ﬁeld zone ends at the point
where the mixing layers around the potential core merge together
on the centerline of the jet. The corresponding distance from the
nozzle is
/C15 greater for compressible jets and particularly for the ones that
are not ideally expanded [147–150,108,51,121];
/C15 increased for larger pressure ratios [143–145,149,121,150];
/C15 increased with the exit Mach number [149];
/C15 reduced when there occurs an enhancement of the turbulence,
and so depends on the Reynolds number, which induces a rapid
mixing of the high-velocity ﬂows with the ambient ﬂuid since
we may have a thicker shear layer [144,148,151–154,38,61].
Unfortunately, the only available quantitative results mainly
deal with the supersonic core length [143–145,149], which differs
Fig. 13. Length of the ﬁrst cell in function of the exit pressure ratio (CV nozzle). Fig. 14. Wavelength in function of the total pressure ratio.
E. Franquet et al. / Progress in Aerospace Sciences 77 (2015) 25 –5338

<!-- PDF_PAGE: 15 -->

from the length we are interested in since this one may be shorter
than the supersonic one that may penetrate in the far ﬁeld zone
[28,155]. Thus, the only papers providing quantitative results for
the length of the potential core [30,156] show a tendency which
reads
LL 4 17NZ RR λ=+ ()
Then, when one turns to the supersonic core length, the only
available relation (obtained for converging micro-nozzles) is
furnished by [143]
L
D 1.81 2.98
18
s
e
0η=+
()
4.2.6. Mixing layer
Ah u g ea m o u n to fp a p e r sh a v eb e e nd e v o t e dt ot h eu n d e r -
standing and analysis of the main features of the mixing layer, which
is shown to contain large-scale eddies (described in detail hereafter).
Most of these studies are experimental ones [30,65,59,135,157–
174,149,122,61,94] yet some numerical papers are also available
[37,59,122,175–181]. These structures play a major and signi ﬁcant
role in the behavior of the jet, especially in its spreading rate and the
associated decay, because of their interaction with the various shock
waves [134,38,158,156,164,52,149,17 8,166,171].C o n t r a r yt ow h a t
happens in the core of the jet, the viscous effects have here a tre-
mendous inﬂuence, particularly because of their impact on the de-
velopment of the ﬂow instabilities and consequently on the width of
the mixing layer and on the diameter of the jet. This has been for-
malized by [69],a n dc o nﬁrmed by [163,152,162],w h od e ﬁned an
initial Reynolds number Re
i for the shear layer, based on the exit
velocity and the distance to the Mach disk and the viscosity of the
ambient ﬂuid, such that for
/C15 Re 10i
4> , the mixing layer is initially turbulent and its width
increases linearly with the distance to the exit plane, leading to
the replication of identical shocks pattern whose characteristic
lengths are governed by the pressure ratio.
Let us note here that this case is the most often encountered in
practical situations.
/C15 10R e 1 0i
3 4<< , the regime is essentially laminar but the tran-
sition to turbulence occurs before the Mach disk, the corre-
sponding transition point being closer to the exit plane as Re i
increases, accompanied by a progressive decrease of the dia-
meter of the suspended shock and a thickening of the mixing
layer.
/C15 10R e 1 0i
2 3<< , the ﬂow is laminar in the mixing layer, whose
width increases with Re i, and the shock waves pattern may be
greatly modi ﬁed (in particular the intercepting shock).
/C15 Re 10i
2< , the ﬂow behaves as in a rare ﬁed regime and the
shocks are extremely diffuse.
Hydrodynamic instabilities:T w ok i n do fﬂow instabilities may be
found in the mixing layer: Kelvin –Helmholttz (KH) instability and
Taylor–Goertler (TG) instability. The ﬁrst one arises because there is
a great shearing between the various streamlines present in the
mixing layer. Indeed, as we have seen previously, the ﬂow has a
great velocity in the core part and passes from a supersonic regime
t oas u b s o n i cr e g i m es i n c et h ea m b i e n tﬂuid is at rest. A shear layer
is present between the intercepting shock and the frontier of the jet,
which permits the appearance of KH type instabilities. These ones
appear as roll-ups and become large eddies, producing vortex rings
which evolve downstream of the ﬂow, mainly by entrainment of the
ambient ﬂuid [59,177,182,183]. Their amplitude evolution may be-
come non-linear. Concerning the TG instability, this is caused by the
curvature of the streamlines in the mixing layer. This curvature is
mainly due to the high expansion of the ﬂuid (the greater the ex-
pansion – the pressure ratio – the stronger the curvature) but it
depends also on the exit Mach number and on the boundary layer of
the jet inside the device which undergoes the under expansion
[170,172,174,180,181]. Consequently, the ﬂuid moves along curvi-
linear trajectories and is in ﬂuenced by centrifugal forces propor-
tional to the square of the velocity and to the inverse of the radius of
curvature [179,174 ]. This, combined with the strong radial velocity
gradient, induces the development of non-uniformities in the ﬂow,
eventually taking the form of pairs of counter-rotating vortices with
axis parallel to the centerline, which are stationary (or quasi-sta-
tionary). Their size is of the order of the boundary-layer thickness
but increases downstream and with the pressure ratio [157,152,
179 ,165,166,181]. Furthermore, these disturbances tend to amplify
initial perturbations due to the nozzle boundary layer or to some
features of the nozzle walls, such as the roughness of their inner side
that can be connected to the streamwise vortex structures
[151,160,162,152,167,169].
Inﬂuence on the ﬂ
ow behavior: The previous instabilities strongly
affect the ﬂow since the shock waves pattern is perturbed, which is
the ﬁrst reason for the unsteady behavior of the jet. Thus, when the
eddies are convected they ﬁnally encounter an oblique shock,
leading to the emission of acoustic waves which may move up-
stream and perturb the jet boundary and structure back to the
nozzle exit. This logically induces a feedback loop, whose coupling
will depend on the pressure ratio [59,164,184].F u r t h e r m o r e ,t h e
counter-rotating vortices modify the azimuthal distributions of the
characteristic variables, which appear to have a petal-like structure.
Hence, one may observe local maxima and minima exhibiting sin-
uous type variation, whose spatially modulated magnitude increases
with the distance from the exit plane as the eddies grow in size
[30,157,65,152,167,94,171,174,181]. Apparently, the maxima of den-
sity and of convective speed coincide together [184]. Eventually,
these vortices play a signi ﬁcant role in the jet noise related me-
chanisms. Indeed, it seems that the vortex pairs are the origin of
Mach-waves which are the most dangerous part of the noise
[182,183,185]. This topic is nonetheless beyond the scope of the
present paper, and therefore we will refer the interested reader to
some of the basic studies dedicated to this issue [146,185–190,
182,183].
Conclusion: Eventually, the phenomena arising inside the
mixing layer are pretty well understood. Nevertheless, there are
still some unknowns concerning the quantitative in ﬂuence of the
interaction between the hydrodynamic instabilities and the shock
waves structure of the jet. In the same way, the role of the ambient
conditions (especially the density) is ill-known. Last but not least,
the structure of the turbulence, its morphology and its dynamics,
still needs some additional thorough investigations regarding the
distance for the turbulent transition or the anisotropy of the tur-
bulence ﬁeld.
4.3. Evolution of the ﬂow variables
Many studies have tried to determinate the evolution of the
variables during the expansion and recompression process as
far as the ﬂuid emerges outside the con ﬁning device. Thus, one
may easily ﬁnd experimental works [66,144,145,30–32,157,70,134,
135,191–207,148,151,35,77,38,39,15,64,40,142,82,123,159,42,127,
59,55,51,87,60,122,150], as well as theoretical ones [133,74,
75,38,78,142,159,127,103,13,208–211,108,129,178,181] or numer-
ical papers [191,110–117,212–223,31,132,63,192,138,147,148,34,
37,196,40,41,82,205,59,119,14,184,120,55,121,122] which provide
axial variation (usually along the centerline) of some variables or
sometimes the radial evolution at different positions along the
centerline. An overview of the various results is given in Table 3.
E. Franquet et al. / Progress in Aerospace Sciences 77 (2015) 25 –53 39

<!-- PDF_PAGE: 16 -->

5. Far ﬁeld zone of a highly underexpanded jet
In comparison with the near ﬁeld zone, this region has focused
less attention in the past (excluding obviously the ideally expanded
jets) however some information may be found concerning the be-
havior of the jet characteristics since both experimental [30,70,
148,39,57,224–232,61,207] and theoretical [28,72,224–226,197,228,
233–241,207] and numerical [34,216,230,242–249,238] papers re-
port thereon. Generally, they deal with risk assessment related to
leakage of ﬂammable material (e.g. natural gas or hydrogen). As
previously explained (see Section 3.3 ), the jet is now in pressure
equilibrium with the ambient ﬂuid although it may still have a high
velocity (i.e. evolve in the compressible regime) which decays far-
ther downstream. In this context, it has been shown that the be-
havior of underexpanded jets may be treated as usual compressible
fully expanded jets, provided that suitable arrangements are done in
order to ﬁnd a characteristic length which permits us to scale all the
variables of the jet [28,68,70,224,243,38,197,150].T h u s ,a sd e p i c t e d
in Fig. 15, one may view the jet in this region as if it were originated
from a pseudo-source with different characteristics than the actual
exit source. When dealing with practical applications, the aim is thus
to feed industrial codes with proper boundary conditions in order to
avoid the resolution of the whole underexpanded jet which would
be cumbersome (and still very complicated even at the present
time). We present hereafter how this pseudo-source, often referred
to as a notional nozzle, may be described ( Fig. 16).
5.1. Notional or ﬁctional or equivalent nozzle
Far downstream from the exit plane, the jet seems to have little
memory of its recent past (the shock wave pattern, the presence of
multiple or a unique Mach disk, etc.). From this observation, it has
long been proposed to replace it by an equivalent ﬂow, whose
characteristics are determined only from stagnation (or exit) state
thanks to some simple physical hypotheses. Let us now present
the available models, in the case of a chocked convergent nozzle
such that the ﬂ
ow is sonic at the exit.
5.1.1. Equivalent diameter [250]
This paper related to reactive jets studies the dimensionless
parameters governing the ﬂame length when there are changes of
jet momentum, and also an excess air ratio. It is generally re-
nowned as the ﬁrst study introducing the concept of an equivalent
diameter (or nozzle), in order to take into account the density
effects in the axial decay of jets. This equivalent nozzle is supposed
to have the same momentum ﬂux and velocity as the actual nozzle
but with the density of the ambient ﬂuid. Then, without the help
of any hypothesis on the equation of state, conservation equations
for the nozzle ﬂuid mass and momentum lead to the following
equivalent diameter:
D
D 19e
eeq ρ
ρ=
()∞
Obviously, for a perfect gas, we may use Eq. (70) to rewrite this
relation:
⎛
⎝⎜
⎞
⎠⎟
⎛
⎝⎜
⎞
⎠⎟
D
D
T
T
2
1
2
1 20e
eq
1/ 1
0
1/ 1
0
0γ
ρ
ργ η= + = + ()
γγ(− )
∞
(− )
∞
5.1.2. Pseudo-diameter approach [224]
It relies on the mass conservation, assuming no entrainment of
ambient air, between the exit plane to an hypothetical state in the
farﬁeld zone where the ﬂow is supposed to be at the same pres-
sure and temperature as the ambient ﬂuid and at a sonic velocity.
This may be summarized as follows:
pp 21eq = ()∞
TT 22eq = ()∞
Vc 23eq eq= ()
From the mass balance, we may obtain
D
D
V
c 24e
e e
eq eq
eq ρ
ρ=
()
For a ﬂuid governed by the perfect gas equation of state, Eqs. (68)
and ( 69) may be used to rewrite the mass balance as follows:
⎛
⎝⎜
⎞
⎠⎟
D
D
T
T
2
1 25e
eq
1/2 1
0
0γ η= + ()
γγ+ ( − )
∞
Remark: in the two previous relations, we voluntary omitted the
discharge coefﬁcient present in the original paper in order to have
the same basis when comparing the various results.
5.1.3. Sonic jet approach [57]
This method is almost the same as the pseudo-diameter ap-
proach [224], since it also relies on the mass conservation and
supposes that the equivalent ﬂow is sonic at the ambient pressure
but at the same temperature as in the exit plane. This summarizes
as follows:
pp 26eq = ()∞
TT 27eq e= ()
Vc 28eq eq= ()
The effective diameter is then easily found, namely:
D
D
V
c 29e
e e
eq eq
eq ρ
ρ=
()
For a ﬂuid governed by the perfect gas equation of state, Eq. (29)
may be written:
⎛
⎝⎜
⎞
⎠⎟
D
D
2
1 30e
e
eq
/1
0η γ η== + ()
γγ(− )
5.1.4. Momentum-velocity approach [227]
In this method, the diameter of the jet is not modi ﬁed but an
equivalent velocity is computed so as to preserve the momentum
balance, leading to the following relations:
Transition
a
Farﬁeld (fully developed)
Fig. 15. Flow behavior in the far ﬁeld zone and notional nozzle concept.
E. Franquet et al. / Progress in Aerospace Sciences 77 (2015) 25 –5340

<!-- PDF_PAGE: 17 -->

VV
pp
V 31
eq e
ee q
e eρ=+
−
()
D
D 1
32e
eq
=
()
5.1.5. Improved pseudo-diameter approach [225]
It is an extension of the method developed in [224], and pre-
viously given in Section 5.1.2, where both mass and momentum
balances are used. The ﬂow is still supposed to be in pressure
equilibrium with the ambient medium but its temperature is equal
to the total one:
pp 33eq = ()∞
TT 34eq 0= ()
By combining the mass and momentum equation, one may have
VV pp
V 35
eq e
e
e eρ=+ −
()
∞
Consequently, the diameter is easily deduced via the mass bal-
ance:
D
D
V
V 36e
e e
eq eq
eq ρ
ρ=
()
These relations are valid for any kind of equation of state, never-
theless in the case of a perfect gas, we may write them:
Vc
1
37eeq
0
γ η
η
γ=
+−
()
⋆
⎛
⎝⎜
⎞
⎠⎟
D
D
2
1 1
38
e
eq
1/ 1
0
0
γ
γη
γ η
η
= + +−
()
γ(− )
⋆
When the pressure ratio is far from its critical value 0ηη(⪢ )⋆ , Eq.
(38) becomes
⎛
⎝⎜
⎞
⎠⎟
D
D 1
2
1 39e
eq
1/ 1
0
γ
γγ η= ++ ()
γ(− )
Remark: here again, we do not put the discharge coef ﬁcient in the
previous relations contrary to what is done in the associated
paper.
5.1.6. Adiabatic expansion approach [238,207,248]
This method has been tried ﬁrst in [238] and completely pre-
sented in [207]. Contrary to others methods, it considers a com-
plete conservative approach which therefore includes the mass,
momentum and energy balances. Supposing that body forces,
entrainment and viscous forces are negligible, a quasi-steady ex-
pansion up to the ambient pressure is assumed, namely:
pp 40eq = ()∞
With such an approach, not only the effective diameter of the
equivalent jet is calculated but also its velocity, enthalpy and
density. Thus, we have
V
V M
1 1 1
41e e
e
e
eq
2γ
η
η=+ −
()
⎛
⎝
⎜
⎜
⎛
⎝
⎜
⎞
⎠
⎟
⎞
⎠
⎟
⎟
h
h
Mc
h
V
V1 1
2 1
42e
ee
ee
eq
22
eq
2
=+ −
()
pT
pT
,
, 43e
eq eq
e e
eqρ
ρ
ρ
ρ=
()
() ()
D
D
V
V 44e
e eeq
eq eq
ρ
ρ=
()
For a perfect gas, these relations may be analytically developed:
ab
Fig. 16. Effective diameter of the equivalent jet in function of the total pressure ratio: (a) low pressure ratios and (b) high pressure ratios.
E. Franquet et al. / Progress in Aerospace Sciences 77 (2015) 25 –53 41

<!-- PDF_PAGE: 18 -->

⎛
⎝
⎜
⎜
⎛
⎝
⎜
⎞
⎠
⎟
⎞
⎠
⎟
⎟
T
T M
V
V1 1
2 1
45e
e
e
eq 2 eq
2
γ=+ − −
()
T
T
1
46ee
eeq
eq
ρ
ρη =
()
5.1.7. Mach disk approach [197,241]
The notional nozzle is supposed to be positioned just after the
Mach disk, whose diameter will be taken as the one of the
equivalent jet. Supposing that the ﬂow undergoes an isentropic
expansion up to the Mach disk, considered as a normal shock
wave, and assuming a post-shock pressure equal to the ambient
one, it is possible to combine the isentropic and normal shock
relations to obtain an equation whose solution provides the Mach
number upstream of the Mach disk. Knowing this latter one, the
equivalent diameter is computed from the exit diameter.
In the case of a perfect gas equation of state, the combination of
Eq. (60) and ( 74) yields to the equation giving the Mach number
before the Mach disk, which permits us to compute the equivalent
diameter thanks to Eq. (67). This summarizes as follows:
⎛
⎝⎜ ⎞
⎠⎟
⎛
⎝⎜
⎞
⎠⎟
M
M
1 1
2
2
1 11
47
0
2
/1
2
η
γ
γ
γ
=
+ −
+ −+
()
γγ(− )
⎛
⎝
⎜
⎜
⎜
⎞
⎠
⎟
⎟
⎟
D
DM
M1 1 1
2
1
2 48
e
eq
2
1/4 1
γ
γ=
+ −
+
()
γγ+ ( − )
5.1.8. Underexpanded jet theory [251]
It is principally based on mass and energy conservations, with
the assumption of no ambient ﬂuid entrainment. Similar to most
existing approaches, the notional nozzle is supposed to be sonic
and the ﬂuid in pressure equilibrium with the ambient ﬂuid:
pp 49eq = ()∞
Vc 50eqeq = ()
The equivalent diameter is still computed from the mass balance:
D
D
V
c 51e
e eeq
eq eq
ρ
ρ=
()
with pT, eqeqρ ρ=( )∞ and cc p T , eqeq =( ) ∞ . Here, the temperature is
obtained via the energy balance:
hh
V
2 520e q
eq
2
=+ ()
As previously, these relations are easily obtained for a perfect gas:
TT 2
1 53eq 0 γ= + ()
⎛
⎝⎜
⎞
⎠⎟
D
D
2
1 54e
e
eq
/1
0η γ η== + ()
γγ(− )
Remark: in such a case, one may note that this leads to the same
expression as with the sonic jet approach of [57] since we obtain
TT eeq = .
5.1.9. Comparison of the various approaches
Given the previous methods to estimate the diameter of the
equivalent jet, we propose to compare them altogether, with the
exception of the approximation of Thring and Newby [250] which
systematically leads to higher values and disagrees with all other
relations [131]. Yet, concerning the other methods, the dis-
crepancies between the results lie between 67% and 80% de-
pending on the pressure ratio. Since the notional nozzle may re-
present a hypothetical state, which does not exist physically, it is
not possible to discriminate the various approaches. Consequently,
we are going to further study the predictions that can be done
using such models.
5.2. Evolution of the variables
Since the ﬂow has a gaussian pro ﬁle in this region, most of the
experimental works, whose conditions and main results are de-
tailed in Table 4 , deal with the axial evolution of some physical
variables, which ones are commonly the velocity and the con-
centration (based either on the volume fraction or on the mass
fraction). Given these measurements, we are now going to present
how the previous models may be used to obtain a quantitative
description of the jet. From a general point of view, there are two
classical ways to handle the dif ﬁculty to model in a simple manner
the evolution of the variables along the centerline. The ﬁrst one
relies on the extension of the work of [252] who studied ideally
expanded supersonic jets and proposed the following expression
for the evolution of any unknown variable U such as the velocity,
the mass fraction or the stagnation enthalpy:
⎛
⎝
⎜
⎜
⎜
⎜⎜
⎞
⎠
⎟
⎟
⎟
⎟⎟
U
U x
D a
1e x p 1
55
e
e eq
ζ ρ
ρ
=− −
+
()
∞
with ζ¼0.037, 0.052 or 0.051 and a 0.7=− respectively.
Concerning the decay of the velocity, one may also ﬁnd the
following expressions:
Ref. [253]:
M0.16 1 0.16 56id()ζ =− ()
Ref [153,154]:
⎧
⎨
⎪
⎪⎪
⎩
⎪
⎪⎪
⎛
⎝
⎜
⎜⎜
⎞
⎠
⎟
⎟⎟
⎛
⎝
⎜⎜
⎞
⎠
⎟⎟
57
MM
MM
0.16 1 0.16 for 0.81
0.126 1 for 1
id
e
id
id id
0.22
2 0.15
() ()
ζ
ρ
ρ=
−≤
−≥
∞
−
−
The second method, far more famous, proposes to extend the
use of the classical relation of [254] based on the observations of
[250]. This one, developed for subsonic jets, states that the axial
evolution of the mass fraction and velocity are given by
U
U
D
xa 58e
e eq
κ
ρ
ρ= + ()∞
with 55 . 4κ =− or 5.8 6.2− for each variable.
Here, it is interesting to remark that far away from the exit, the
denominator in the exponential term of Eq. (55) is huge and
consequently this relation may be rewritten as
U
U
D
x
1
59e
e eq
ζ
ρ
ρ=
()∞
Practically, this means that in the far ﬁeld, the expression of [252]
is equivalent to the hyperbolic decay proposed in [254].
E. Franquet et al. / Progress in Aerospace Sciences 77 (2015) 25 –5342

<!-- PDF_PAGE: 19 -->

Eventually, it is worth mentioning that each of the values given
just now strongly depends on the experimental range used to
obtain the correlation coef ﬁcient. This implies that a fair approach
would be not only to mix all the measurements together (if fea-
sible) but also to consider the in ﬂuence of the range used for the
ﬁtting of the curve on the computed parameters.
At the present time, we thus propose to show how these
methods have been used in order to model the decay of char-
acteristic variables of the jet along the axis:
/C15 In [224], we found some measurements of the volume fraction
along the axis of natural gas and ethylene jets injected into air
through a sonic nozzle operating on a pressure range
27 00η =– . However, the authors propose to use the effective
diameter, computed with Eq. (25), instead of the exit diameter
given by the relation (58) to model the axial evolution of the
mass fraction. When compared with the experiments, shown in
Fig. 17, a pretty good agreement is achieved. The decay constant
κ is found to be independent of the ﬂuid, its value being 4.90.
Concerning the virtual origin a, different values are obtained
(and additional data would be useful) yet they seem to be very
small compared to the length.
/C15 In [225], a similar approach is proposed to model the evolution
of the axial velocity of air jets issued from a convergent nozzle
on the same pressure range 27 50η =– . Yet, the proposed re-
lation does not contain any density term, as the one in Eq. (58),
and not only uses the effective diameter, as de ﬁned by Eq. (38),
but also the equivalent velocity, computed by Eq. (37),a s
scaling parameters for the jet. The corresponding results are
shown in Fig. 18. Here, the decay constant exhibits an increase
with the pressure ratio, and a least square approximation leads
to the value of 4.83. Meanwhile, an asymptotic value seems to
be found at large pressures 500η(> ) for the virtual origin, even
if a large scattering is observed, and consequent values are
obtained. The associated measurements are given in Fig. 19 .
When using this approach for the volume fraction measure-
ments of [224], a value of 5.4 is found for the decay constant,
which is different from the previous result.
/C15 In [57], one may ﬁnd the only use of the model of [252] for
underexpanded jets. Thus, the velocity along the centerline of
air jets and one helium jet issuing from convergent nozzles are
studied on the pressure range 5.7 2 00η =– . As we may see in
Fig. 20 , the measurements may be described this way if one
uses the formulation of [253] for the decay constant ζ and
modiﬁes the abscissa to take into account the virtual origin and
uses the equivalent diameter, calculated via Eq. (30), instead of
the exit diameter. Finally, if the approximation for large ab-
scissa is used, the comparison with the measurements of the
mass fraction given by [224] leads to a value for the decay
constant κ¼ 4.6.
/C15 In [244], a hydrogen tank pressurized at 100 bar is released
through a nozzle and the volume fraction of H2 is measured.
ab
Fig. 17. Axial evolution of the volume fraction from [224]: (a) natural gas. and (b) ethylene 80η(= ) .
Fig. 18. Axial evolution of the velocity from [225].
E. Franquet et al. / Progress in Aerospace Sciences 77 (2015) 25 –53 43

<!-- PDF_PAGE: 20 -->

The corresponding results are furnished in Fig. 21.
/C15 In [251], a very pertinent analysis is done, in particular con-
cerning the limits of some notional nozzle approaches and the
difﬁculties inherent to the perfect gas hypothesis (especially
when H2 is concerned). Then, it is proposed to use Eq. (58) in its
original form and, to do so, to compute the density of the jet
using the underexpanded jet theory for an Abel-Noble equation
of state, used for the dihydrogen. We present in Fig. 22 the
comparison of this model with some measurements, un-
fortunately not available elsewhere.
/C15 In [230], three nozzles are used to produce H2 jets releasing in
still air. The pressure range is one of the largest ever found for
this kind of measurements, since it goes from 52 to 163. The
corresponding results are given in Fig. 23 . It is worth noticing
here that the decay constant κ, for both the mass fraction and
the velocity, is found to vary with the pressure ratio and a
signiﬁcant difference with the previous results is found (up to
34% for the mass fraction and to 160% for the velocity).
/C15 In [231], the mass fractions of methane and hydrogen jets
vented through ori ﬁces from a reservoir at 40 bar are reported.
Using the pseudo-diameter approach of [224], a good agree-
ment is obtained with the experiments as we may see in
Fig. 24 . Nevertheless, when normalizing by the densities ratio,
the authors also found another value for the decay constant of
1/0.27¼ 3.7. Moreover, the virtual origin is indeed different
from one ﬂuid to another but it also cannot be neglected in the
case of H2 jet.
/C15 In [247], the axial velocity of a H2 jet issuing from a nozzle is
ab
Fig. 19. Evolution of the parameters for the model for the velocity from [225]: (a) decay constant and (b) virtual origin.
Fig. 20. Axial evolution of the velocity from [57]. Fig. 21. Axial evolution of the mass fraction from [244].
E. Franquet et al. / Progress in Aerospace Sciences 77 (2015) 25 –5344

<!-- PDF_PAGE: 21 -->

measured. Once more, the hyperbolic evolution well describes
the ﬂow behavior, as we may see in Fig. 25 , yet the constant
decay is found to be κ¼ 5.1 and the exit diameter is used as in
the original relation.
/C15 In [248], hydrogen is still used and released from two ori ﬁces at
pressure ratios ranging from 8.25 to 68.5. Here, it is still proposed
to use the original relation to ﬁt the measurements but using an
adiabatic expansion approach to compute the equivalent density,
using possibly a real gas equation of state. We present in Fig. 26
the evolution of the mass fraction and velocity.
/C15 In [207], a convergent nozzle is used to release dried air at an
exit pressure ratio 12 0 . 3eη =− . The adiabatic expansion
approach (see upper) is then used to de ﬁne scaling parameters.
It then permits us to see that all experiments have a similar
behavior, as shown in Fig. 27 , when proper normalization is
used. The universal decay constant is found to be
1/0.16 6.2 5κ == .
5.3. Conclusion
It is clear from all these experiments that the hyperbolic decay,
predicted by incompressible theory, still holds in the case of un-
der-expanded jets. Furthermore, it appears that the jet may be
Fig. 22. Axial evolution of the mass fraction from [251].
ab
Fig. 23. Axial evolution from [230]: (a) mass fraction and (b) velocity. (For interpretation of the references to color in this ﬁgure caption, the reader is referred to the web
version of this paper.)
Fig. 24. Axial evolution of the mass fraction for a methane (black) and an hydrogen
(red) jet from [231].
E. Franquet et al. / Progress in Aerospace Sciences 77 (2015) 25 –53 45

<!-- PDF_PAGE: 22 -->

approximated by an equivalent jet (notional nozzle approach) and
the relations adapted to this effective jet. Nevertheless, we have
seen that a great discrepancy exists between the results provided
by the various modelings of this effective jet. Moreover, it seems
that we may either use these artifacts or compute more precisely
the state of the jet in this equivalent state (using in particular a
correct thermodynamical modeling of the equation of state of the
ﬂuid) so as to reproduce the behavior of the variables. This implies
that additional work is still needed to see what may be the best
approach among these several ones. Thus, supplementary ex-
periments at larger pressures would permit us to con ﬁrm (or not)
if the decay constants, for the mass fraction and velocity, are really
dependent on the pressure ratio and the associated correlation. By
testing other ﬂuids, we could also check if those constants are
really universal, as they are supposed to be. Eventually, one could
also consider under-expanded jets which are supersonic at the
exit, since to our knowledge this has never been done.
6. Modeling approaches
We propose here to step through the principal available methods
used to quantitatively describe the behavior of an underexpanded
jet. Historically, the ﬁrst approaches were based on theoretical con-
siderations [95–97,29,67,33,136,72,141,137,99–101,208,140,42,127,
103,43,204,105,210,46,47,13,107,211,246,108,255–261,129,178,17 9,53,
165,180,181]. Generally, these studies used the method of character-
istics, whose principle is to decompose the partial differential
Fig. 25. Axial evolution of the velocity from [247].
ab
Fig. 26. Axial evolution from [248]: (a) mass fraction and (b) velocity.
Fig. 27. Axial evolution of the velocity from [207].
E. Franquet et al. / Progress in Aerospace Sciences 77 (2015) 25 –5346

<!-- PDF_PAGE: 23 -->

equations describing the ﬂow into ordinary differential equations
which
are easily integrated along particular directions. Since the develop-
ment of modern computers, and jointly of the numerical methods,
it has become more and more useful to rely on numerical studies.
These trends are now the main ones for three or four decades. The
earlier works start to deal with simpli ﬁed computations, such as
the parabolized Navier–Stokes equations [27,148,17 5,112,37,215,222]
or the thin-layer approximation [223]. Then, one may ﬁnd some
papers dealing with the Euler equations[138,111,147,75,36,214,17,81,
115 ,82,20,119,219,14,120,23,262–266,177 ].M o s to f t e n ,t h e ya r eb a s e d
on ﬁnite difference schemes [147,36,214,115,82,14,264,265,177 ]even
if now new ones used the ﬁnite volume method [138,75,81,
20,263,120,
23] or even the ﬁnite element method[ 111 ].I ti ss e e nt h a t
this kind of computations may give v ery accurate predictions of the
variable in the core part of the ﬂow, and a relatively good description
of the shock wave pattern. Given the low computation cost associated
with the inviscid hypothesis, it is clearly a boon if these features are
t h eo n e sw ea r ei n t e r e s t e di n .S h o u l dt h es t u d yc o n c e r nt h eb e h a v i o r
of the far ﬁe l dz o n eo rt h em i x i n gl a y e ro ra n yo t h e rf e a t u r eo ft h e
ﬂow where the viscous effects play a signi ﬁcant role, the modeling
must now be based on the Navier –Stokes equations. Since the ﬁrst
numerical studies, and even now, the easiest way and the less ex-
pensive from a computational point of view is to consider the Rey-
nolds Averaged Navier –Stokes equations (if obviously the ﬂow is
turbulent). Logically, this approach has been largely tested [1 10,31,
132,63,138,243,34,216,218,116,45,220,84,21,22,55,267–271,122,249],
with the
k ε− model in an overwhelming majority of papers (be it its
incompressible formulation or some of the proposed compressibility
corrections of the k CCε−− class model). Even if this approach is
acceptable to obtain the mean behavior of the ﬂow, there are still
some discrepancies between the r esults obtained with the various
turbulence models ( k ε− , k Realizableε−− , k RNGε−− ,
k CCε−− , k ω− , k SSTω−− , k kl− , k R− ,R e y n o l d sS t r e s sM o d e l ,
etc.). More importantly, this forb ids the study of any unsteadiness
related phenomenon. In such a case, there is no other choice than
considering the use of Large-Eddy Simulation or Direct Numerical
Simulation. Currently the latter one is still unaffordable for entire si-
mulation of underexpanded jets despite the huge progress in high
performance computing, since the classical Reynolds number in such
situations is of the order of
101 04 5– and the mesh length
proportional to Re9/4 in any spatial direction. Actually, this
also means that in the near ﬁeld zone or at the initial stages of a
release, DNS is the most powerful and reliable method. That is the
spirit of the main studies dealing with such a method [191,212,
138,113,196,41,217,59,117,118,121,272,273,24,25]. Eventually, in all the
other cases (that is to say in most cases), the LES seems to be the ideal
compromise, be it ILES or classical LES methods using standard sub-
grid scale modelings. Surprisingly, as far as we know, there are not so
much free jets simulations and the scarce ones mainly deal with
moderately underexpanded jets [274–278,26].T h i si sp a r t i c u l a r l y
amazing since lots of these deal with such situations, and moreover
we may ﬁnd numerous studies dealing with impinging jets or jets in
crossﬂows [279–282].
7. Thermodynamical behavior of the ﬂuid
When one wants to model the release of a pressurized ﬂuid, the
equation of state has to be well chosen so as to correctly describe
the behavior of the ﬂuid. The main points this modeling must be
able to predict unambiguously are the properties in the exit plane
(pressure, temperature, density and velocity), the evolution of
some characteristic parameters with the reducing pressure and
temperature (sound velocity for example) and ﬁnally the potential
appearance of another phase (liquid or solid).
Globally, the ideal gas equation of state is the most used. When
dealing with air or relatively low pressure range, this does not
raise any major problems and the use of an average polytropic
coefﬁcient may be suf ﬁcient enough. If not, a simple variation of γ
with temperature or pressure may improve the results. However,
it appears that the validity of the ideal gas does not hold with
some species for high pressures, e.g. hydrogen or other super-
critical ﬂuid. Thus, the compressibility factor is far from unity and
the real densities are very different from the ones computed with
perfect gas equation of state and consequently the sound velocity
is not well estimated [242,20,234,263,239,121,92].
Last but not least, it appears that the expansion of the ﬂuid is
inducing a high decrease in temperature and pressure which may
drive the ﬂuid into a metastable state [133
,68,74,269,77,114,40,
203,283,238,121]. Logically, this may hypothetically allow the dy-
namic appearance of a phase, either liquid or even solid, as illu-
strated in Fig. 28 . Depending on the initial conditions, the ﬂuid
undergoing the expansion may attain aﬁnal state which stays in the
gas phase (blue path) or on the contrary lies in the liquid (green
path) or solid phase (red path). In such a case, the apparition of this
new phase will depend on the degree of supersaturation and on the
time elapsed in this state, implying that this may also not happen
even if feasible. Experimentally, condensation has been observed in
underexpanded jets [157,267,74,15,284,130,123,65,205,184,92] and
the appearance of a solid phase is well documented in the RESS (for
Rapid Expansion of Supercritical Solution) process where a super-
critical ﬂuid is used as a solvent containing a solute which is seen to
precipitate during the expansion. However, there is no overall study
concerning the appearance of these new phases, as a function of the
initial conditions or depending on the ﬂu i di n v o l v e di nt h ej e t ,a n d
so this point is still unclear. To highlight why these kind of studies
may have some interest, from a practical point of view, it appears
that the role of condensation in the properties of the Mach disk are
ambiguous since [68] reported no noticeable effect while [74] noted
a probable decrease of the Mach disk diameter and ﬁnally [285]
noticed a strong inﬂuence on both the diameter and the location of
the Mach disk. In the same way, injection of solid particles has
shown to shorten the Mach disk location and to increase its curva-
ture [83,259,86]. Since the Mach disk is composing the main part of
the nearﬁeld zone, which then serves as a starting point for reduced
models in the far ﬁeld zone, one would appreciate to have a better
description of this kind of phenomena.
100 150 200 250
10−2
10−1
100
101
102
T (K)
P (bar)
Fig. 28. Illustration of the possible appearance of a phase transition in a P–T dia-
gram where various underexpanded jets conditions are considered.
E. Franquet et al. / Progress in Aerospace Sciences 77 (2015) 25 –53 47

<!-- PDF_PAGE: 24 -->

8. Conclusion
This paper has been devoted to the analysis of the experimental
results available for axisymmetric free underexpanded jets ejected
in a ﬂuid at rest. It appears that even if the global structure of such
jets is perfectly known nowadays, there are still many features
either ill-known or completely ignored. These shortcomings arise
from the uncertainties of the available measurements on one
hand, and from a lack of studies on the other hand. Along with this
study, the various numerical methods and the associated ther-
modynamical issues have been brie ﬂy discussed, emphasizing on
the global strengths and weaknesses of both.
T os u m m a r i z et h em a i nc o n c l u s i o n sd r a w ni nt h ep r e s e n tp a p e r ,i t
has been shown that, for the nearﬁeld zone, the position of the Mach
disk is pretty well described. However there remains some doubt
concerning its diameter and the exact conditions leading to its ap-
pearance. Furthermore, there is clearly a lack of information when one
seeks for a quantitative expression of the diameter of the jet and of the
wave-length of the cells structure and of the total length of the po-
tential core. When dealing with the farﬁeld zone, one may be pretty
conﬁdent about the hyperbolic decay for all the variables, similar to
the incompressible case. Moreover, the notional nozzle is clearly a
well-suited approach to represent the behavior of such jets. None-
theless, there is still some work to do in order to discriminate the best
model among the several ones available and also to determineﬁrst if
the decay constants are really universal and second their corre-
sponding values. Furthermore, all these studies have been developed
only for sonic jets at the exit, and so the inﬂuence of the Mach number
is not visible. Finally, we would like to point out the various phe-
nomenon which are badly managed: the curvature of the Mach disk
and disappearance of the cells when the pressure ratio increases, the
characteristic lengths of the jets, the importance and beginning of the
entrainment of the external ﬂuid, the viscous effects in the mixing
layer (transition to turbulence, interactions with the hydrodynamic
instabilities, etc.). To our opinion, the two last points may be of im-
portance for the pollution and the dilution of hot gases of combustible
species.
Eventually, once the above features could be better known, it
would be interesting to consider the in ﬂuence of the ambient ﬂuid,
particularly when it is also moving, i.e. to perform the same analysis
for underexpanded jets in a co- or cross- ﬂow. On the other hand,
although the results are qualitatively the same for non-symmetric
jets, a quantitative review of associated results remains undone.
Appendix A. Isentropic relations for a perfect gas
A.1. Expressions in function of the Mach number and the stagnation
state
⎛
⎝⎜ ⎞
⎠⎟P
P M1 1
26 0
0 2
/1
γ=+ −
()
γγ(− )
T
T M1 1
2 61
0 2γ=+ −
()
⎛
⎝⎜ ⎞
⎠⎟M1 1
2 62
0 2
1/ 1ρ
ρ
γ=+ −
()
γ(− )
Remark: for an underexpanded jet, the ideally expanded state is
deﬁned as the one where the pressure in the ﬂow would be the
same as the ambient one. Using Eq. (60), it implies that the ideally
expanded Mach number is
⎛
⎝⎜
⎞
⎠⎟M 2
1 1
63
id 0
1/
γ η= − −
()
γγ(− )
A.2. Expressions in function of the Mach number and the critical
state
⎛
⎝
⎜
⎜
⎜
⎞
⎠
⎟
⎟
⎟
P
P
M1 1
2
1
2 64
2
/1
γ
γ=
+ −
+
()
γγ
⋆
(− )
T
T
M1 1
2
1
2 65
2γ
γ=
+ −
+
()
⋆
⎛
⎝
⎜
⎜
⎜
⎞
⎠
⎟
⎟
⎟
M1 1
2
1
2 66
2
1/ 1
ρ
ρ
γ
γ=
+ −
+
()
γ
⋆
(− )
⎛
⎝
⎜
⎜
⎜
⎞
⎠
⎟
⎟
⎟
A
A M
M1 1 1
2
1
2 67
2
1/2 1 / 1
γ
γ=
+ −
+
()
γγ
⋆
() ( + ) ( − )
A.3. Relations between stagnation and critical state
⎛
⎝⎜
⎞
⎠⎟P
P
2
1 680
/1
γ= + ()
γγ⋆ (− )
T
T
2
1 690 γ= + ()
⋆
⎛
⎝⎜
⎞
⎠⎟2
1 700
1/ 1
ρ
ργ = + ()
γ⋆ (− )
Appendix B. Normal shock relations for a perfect gas
B.1. Expressions in function of the Mach number before and after the
shock
PM
T
PM
T 71
11
1
22
2
=
()
P
P
M
M
1
1 72
2
1
1
2
2
2
γ
γ
= +
+ ()
T
T
M
M
1 1
2
1 1
2 73
2
1
1
2
2
2
γ
γ=
+ −
+ −
()
B.2. Expressions in function of the Mach number before the shock
⎛
⎝⎜
⎞
⎠⎟P
P MM2
1
1
1
2
1 11
74
2
1
1
2
1
2γ
γ
γ
γ
γ
γ= + − −
+ = + −+
()
E. Franquet et al. / Progress in Aerospace Sciences 77 (2015) 25 –5348

<!-- PDF_PAGE: 25 -->

⎛
⎝⎜
⎞
⎠⎟
⎛
⎝⎜
⎞
⎠⎟T
T
MM
M
21
1
1 1
2
2
1 1
75
2
1
2
1
2
1
2
1
2
γ
γ
γγ
γ= ( − )
( + )
+ −
− −
()
M
M
1
2 1 1
2 76
2
1
1
2
1
2
ρ
ρ
γ
γ= +
+ −
()
Appendix C. Discharge coef ﬁcient
We have seen that some authors choose to introduce the dis-
charge coef ﬁcient in order to take into account what is known as
the vena contracta effect. Inasmuch as this phenomenon may
modify the exit conditions, compared to the isentropic ones, it
may be worth considering it, be it for the study of the near ﬁeld
zone (particularly the position and diameter of the Mach disk) or
for the far ﬁeld zone (since the equivalent jet is determined from
the exit conditions). Yet, we will not detail here how to compute
this coef ﬁcient since it is a huge task which is largely studied in
the literature. Instead, we will just recall the main reasons for such
a behavior and their consequences in order to highlight the si-
tuations where it may be useful to insert such a detail in the
computations. The interested reader is referred to the 9300 ISO
Standard or to the Euromet works, and associated papers, if sup-
plementary information is required or to the discussions available
in [62,56,224,286,287,81,117,14,53,261,170,172] in the case of un-
derexpanded jets.
To brie ﬂy recall the major points, the discharge coef ﬁcient is
introduced so as to better describe the real mass ﬂow of any de-
vice, since this one may vary from the ideally isentropic one. Thus
it is de ﬁned as follows:
C m
m 77
D
real
isent.
= ̇
̇ ()
In the case of perfect gas, the ideal mass ﬂow rate at choked
conditions is easy to compute and consequently we may write
m
A CC P
RT 78
D
real 0
0
̇ =
()
⋆
with C 2
1
1/ 1
()γ= γ
γγ⋆
+
(+ )(− )
.
As we may see, the discharge coef ﬁcient CD thus permits us to
take into account the various effects that may modify the mass
ﬂow rate. Among these ones, one may cite
/C15 the curvature of the streamlines (in particular with convergent
nozzles or ori ﬁces) since they are often still converging when
attaining the exit and therefore they become parallel only
downstream of the exit.
/C15 the viscous effects, especially the apparition of a transition in
the boundary layer.
/C15 the real gas effects, in particular at extreme pressure or tem-
perature where the ﬂuid may have a behavior far from that of
an ideal gas.
Appendix D. Overview of the various studies dealing with the
structure of underexpanded jets
See Tables 2–4.
References
[1] A.J.C. de Saint-Venant, P.L. Wantzel, Mémoire et expériences sur l ’écoulement de
l’air, J. Ecole Polytech. (Paris) 16 (1839) 85 –122.
[2] P. Salcher, J. Whitelaw, Uber den aus ﬂuss stark verdichteter luft, Sitz. Akad. Wiss.
Wien 98 (1889) 267 –287.
[3] E. Mach, P. Salcher, Photographische Fixierung der durch Projectile in der Luft
eingeleiteten Vorgänge, Sitz. Akad. Wiss. Wien 2 (1887) 764 –787.
[4] E. Mach, P. Salcher, Optische Untersuchungen der Luftstrahlen, Sitz. Akad. Wiss.
Wien 98 (1889) 1303 –1309.
[5] R. Emden, Flow phenomena in permanent gases, Ann. D Phys. U Chem. 69 (1899)
426.
[6] L. Prandtl, Uber die stationären wellen in einem gasstrahl, Phys. Z. 5 (1904)
599–601.
[7] L. Prandtl, Beiträge zur theorie der dampfströmung durch düsen, VDI-Z 48 (1904)
348–350.
[8] L. Prandtl, Neue untersuchungen über die strömende bewegung der gase und
dämpfe, Phys. Z. 8 (1907) 23 –30.
[9] R. Courant, K.O. Friedrichs, Supersonic Flow and Shock Waves, Interscience,
Springer, New York, 1956 .
[10] A. Shapiro, The Dynamics and Thermodynamics of Compressible Fluid Flow, vol. 1,
The Ronald Press Company, New York, 1953.
[1 1] R.D. Zucker, O. Biblarz, Fundamentals of Gas Dynamics, second edition,. John Wiley
& Sons, Ltd, Hoboken, New Jersey, 2002 .
[12] R.T. Driftmyer, A correlation of freejet data, AIAA J. 10 (1972) 1093 –1095.
[13] J.L. Palmer, R.K. Hanson, Application of method of characteristics to under-
expanded, freejet ﬂows with vibrational nonequilibrium, AIAA J. 36 (2) (1998)
193–200.
[14] Y. Otobe, H. Kashimura, S. Matsuo, T. Setoguchi, H.-D. Kim, In ﬂuence of nozzle
geometry on the near- ﬁeld structure of a highly underexpanded sonic jet, J. Fluids
Struct. 24 (2) (2008) 281 –293.
[15] A.V. Eremin, V.A. Kochnev, A.A. Kulikovskii, I.M. Naboko, Nonstationary processes
in starting strongly underexpanded jets, J. Appl. Mech. Tech. Phys. 19 (1978) 27 –31.
[16] V.V. Golub, Development of shock wave and vortex structures in unsteady jets,
Shock Waves 3 (4) (1994) 279 –285.
[1 7] V.V. Golub, D.I. Baklanov, T.V. Bazhenova, M.V. Bragin, S.V. Golovastov, M.F. Ivanov,
V.V. Volodin, Shock-induced ignition of hydrogen gas during accidental or tech-
nical opening of high-pressure tanks, J. Loss Prev. Process Ind. 20 (4 –6) (2007)
439–446.
[18] R. Ishii, H. Fujimoto, N. Hatta, Y. Umeda, Experimental and numerical analysis of
circular pulse jets, J. Fluid Mech. 392 (1999) 129 –153.
[19] N.G. Korobeishchikov, A.E. Zarvin, V.Zh. Madirbaev, Hydrodynamics of pulsed
supersonic underexpanded jets: spatiotemporal characteristics, Tech. Phys. 49 (8)
(2004) 973 –981.
[20] R. Khaksarfard, M.R. Kameshi, M. Paraschivoiu, Numerical simulation of high
pressure release and dispersion of hydrogen into air with real gas model, Shock
Waves 20 (2010) 205 –216.
[21] Yumiko Otobe, Tsuyoshi Yasunobu, Hideo Kashimura, Shigeru Matsuo,
Toshiaki Setoguchi, Heuy Dong Kim, Hysteretic phenomenon of underexpanded
moist air jet, AIAA J. 47 (12) (2009) 2792 –2799.
[22] F. Péneau, G. Pedro, P. Oshkai, P. Bénard, N. Djilali, Transient supersonic release of
hydrogen from a high pressure vessel: a computational analysis, Int. J. Hydrog.
Energy 34 (14) (2009) 5817 –5827 (2nd International Conference on Hydrogen
Safety).
[23] M.I. Radulescu, C.K. Law, The transient start of supersonic jets, J. Fluid Mech. 578
(2007) 331 –369.
[24] B.P. Xu, L. el Hima, J.X. Wen, S. Dembele, V.H.Y. Tam, T. Donchev, Numerical study
on the spontaneous ignition of pressurized hydrogen release through a tube into
air, J. Loss Prev. Process Ind. 21 (2) (2008) 205 –213 (Hydrogen Safety) .
[25] B.P. Xu, L. EL Hima, J.X. Wen, V.H.Y. Tam, Numerical study of spontaneous ignition
of pressurized hydrogen release into air, Int. J. Hydrog. Energy 34 (14) (2009)
5954–5960.
[26] B.P. Xu, J.X. Wen, S. Dembele, V.H.Y. Tam, S.J. Hawksworth, The effect of pressure
boundary rupture rate on spontaneous ignition of pressurized hydrogen release,
J. Loss Prev. Process Ind. 22 (3) (2009) 279 –287.
[27] K. Abdol-Hamid, R. Wilmoth, Multiscale turbulence effects in underexpanded
supersonic jets, AIAA J. 27 (1989) 315 –322.
[28] G.N. Abramovich, The Theory of Turbulent Jets, MIT Press, Cambridge, Mass, 1963 .
[29] T.C. Adamson, J.A. Nicholls, On the structure of jets from highly underexpanded
nozzles into still air, J. Aerosp. Sci. 26 (1959) 16 –24.
[30] A.V. Antsupov, General properties of underexpanded and overexpanded super-
sonic gas jets, Sov. Phys. Tech. Phys. 19 (2) (1974) 234 –238.
[31] Y. Avital, G. Cohen, L. Gamss, Y. Kanelbaum, J. Macales, B. Trieman, S. Yaniv, M. Lev,
J. Stricker, A. Sternlieb, Experimental and computational study of infrared emis-
sion from underexpanded rocket exhaust plumes, J. Thermophys. Heat Transf. 15
(1) (2001) 377 –383.
[32] L.H. Back, R.B. Cuffel, Viscous slipstream ﬂow downstream of a centerline Mach
reﬂection, AIAA J. 9 (1971) 2107 –2109.
[33] A.B. Bauer, Normal shock location of underexpanded gas-particle jets, AIAA J. 3 (6)
(1965) 1 187–118 9.
[34] P.S. Cumber, M. Fairweather, S.A.E.G. Falle, J.R. Giddings, Predictions of the struc-
ture of turbulent, highly underexpanded jets, J. Fluids Eng. 1 1 7 (4) (1995) 599–604.
[35] N.J. Dam, M. Rodenburg, R.A.L. Tolboom, G.G.M. Stoffels, P.M. Huisman Kleinher-
enbrink, J.J. Ter Meulen, Imaging of an underexpanded nozzle ﬂow by UV laser
Rayleigh scattering, Exp. Fluids 24 (2) (1998) 93 –101.
[36] S.M. Dash, P.D. Del Guidice, Analysis of three-dimensional ducted and exhaust
plume ﬂowﬁelds, AIAA J. 16 (1979) 823 –830.
[37] S.M. Dash, D.E. Wolf, Interactive phenomena in supersonic jet mixing problems.
Part I: phenomenology and numerical modeling techniques, AIAA J. 22 (7) (1984)
905–913.
[38] C.D. Donaldson, R.S. Snedeker, A study of free jet impingement. Part 1. Mean
properties of free and impinging jets, J. Fluid Mech. 45 (2) (1971) 281 –319.
E. Franquet et al. / Progress in Aerospace Sciences 77 (2015) 25 –53 49

<!-- PDF_PAGE: 26 -->

[39] P.L. Eggins, D.A. Jackson, Laser-doppler velocity measurements in an under-ex-
panded free jet, J. Phys. D: Appl. Phys. 7 (14) (1974) 1894 .
[40] I.A. Graur, T.G. Elizarova, A. Ramos, G. Tejeda, J.M. Fernández, S. Montero, A study
of shock waves in expanding ﬂows on the basis of spectroscopic experiments and
quasi-gasdynamic equations, J. Fluid Mech. 504 (2004) 239 –270.
[41] B.J. Gribben, K.J. Badcock, B.E. Richards, Numerical study of shock-re ﬂection hys-
teresis in an underexpanded jet, AIAA J. 38 (2) (2000) 275 –283.
[42] R. Ladenburg, C.C. Van Voorhis, J. Winckler, Interferometric studies of faster than
sound phenomena. Part II. Analysis of supersonic air jets, Phys. Rev. 76 (1949)
662–677.
[43] E.S. Love, C.E. Grigsby, L.P. Lee, J.M. Woodling, Experimental and theoretical studies
of axisymmetric free jets, Technical Report R-6, NASA, 1959.
[44] N. Menon, B.W. Skews, Rectangular underexpanded gas jets: effect of pressure
ratio, aspect ratio and mach number, in: Klaus Hannemann, Friedrich Seiler (Eds.),
Shock Waves, Springer, Berlin, Heidelberg, 2009, pp. 991 –996.
[45] N. Menon, B.W. Skews, Shock wave con ﬁgurations and ﬂow structures in non-
axisymmetric underexpanded sonic jets, Shock Waves 20 (3) (2010) 1 75 –190.
[46] D.C. Pack, On the formation of shock-waves in supersonic gas jets, Q. J. Mech. Appl.
Math. 1 (1) (1948) 1 –17.
[47] D.C. Pack, A note on Prandtl's formula for the wavelength of a supersonic gas jet,
Q. J. Mech. Appl. Math. 3 (2) (1950) 1 73 –181.
[48] E. Rajakuperan, M.A. Ramaswamy, An experimental investigation of under-
expanded jets from oval sonic nozzles, Exp. Fluids 24 (4) (1998) 291 –299.
[49] M. Rasi, R. Saintola, K. Valli, Visualizing the expanding ﬂow of gas from helium-jet
and ion-guide nozzles, Nucl. Instrum. Methods Phys. Res. Sect. A: Accel. Spectrom.
Detect. Assoc. Equip. 378 (1 –2) (1996) 251 –257.
[50] J. Reid, R.C. Hastings, The effect of central jet on the base pressure of a cylindrical
after-body in a supersonic stream, Technical Report, Ministry of Aviation, 1959.
[51] J.M. Seiner, T.D. Norum, Experiments of shock associated noise of supersonic jets,
AIAA Paper, 1979, p. 1526.
[52] J.M. Seiner, T.D. Norum, Aerodynamic aspects of shock containing jet plumes, AIAA
Paper, 1980, p. 0965.
[53] A.R. Vick, E.H. Andrews, J.S. Dennard, C.B. Craidon, Comparisons of experimental
free-jet boundaries with theoretical results obtained with the method of char-
acteristics, Technical Note D-2327, NASA, 1964.
[54] J.A. Wilkes, P.M. Danehy, R.J. Nowak, D.W. Alberfert, Fluorescence imaging study of
impinging underexpanded jets, in: 46th AIAA Aerospace Sciences Meeting and
Exhibit, 2008.
[55] A.J. Saddington, N.J. Lawson, K. Knowles, An experimental and numerical in-
vestigation of under-expanded turbulent jets, Aeronaut. J. 108 (1081) (2004)
145–152.
[56] A.P. Aleshin, I.N. Denisov, N.M. Rogachev, V.F. Sivirkin, Effect of the cone angle and
the degree of contraction of a sonic nozzle on the geometrical structure of the ﬁrst
roll of an underexpanded jet, J. Eng. Phys. Thermophys. 28 (1975) 207 –
210.
[57] B.C.R. Ewan, K. Moodie, Structure and velocity measurements in underexpanded
jets, Combust. Sci. Technol. 45 (5 –6) (1986) 275 –288.
[58] Andrea G. Hsu, Ravi Srinivasan, Rodney D. Bowersox, Simon W. North, Molecular
tagging using vibrationally excited nitric oxide in an underexpanded jet ﬂowﬁeld,
AIAA J. 47 (1 1) (2009) .
[59] T. Matsuda, Y. Umeda, R. Ishii, A. Yasuda, K. Sawada, Numerical and experimental
studies on choked underexpanded jets, vol. 49, Memoirs of the Faculty of En-
gineering, Kyoto University, 1987, pp. 84 –110 .
[60] L.N. Ung, G.K. Hargrave, An investigation of underexpanded free jets from straight
nozzles, in: 1st International Conference on Optical and Laser Diagnostics, vol. 177 ,
2003, pp. 39 –44.
[61] J.A. Wilkes, P.M. Danehy, R.J. Nowak, Fluorescence imaging study of transition in
underexpanded jets, in: 21st International Congress on Instrumentation in Aero-
space Simulation Facilities, 2005, iciasf '05, 2005, pp. 1 –8.
[62] A.L. Addy, Effects of axisymmetric sonic nozzle geometry on Mach disk char-
acteristics, AIAA J. 19 (1) (1981) 121 –122.
[63] P. Birkby, G.J. Page, Numerical predictions of turbulent underexpanded sonic jets
using a pressure-based methodology, Proc. Inst. Mech. Eng. Part G: J. Aerosp. Eng.
215 (3) (2001) 165 –173.
[64] J.C. Gibbings, J. Ingham, D. Johnson, Flow in a supersonic jet expanding from a
convergent nozzle, Technical Report, Aeronautical Research Council, 1972.
[65] A. Krothapalli, G. Buzyna, L. Lourenco, Streamwise vortices in an underexpanded
axisymmetric jet, Phys. Fluids A 3 (8) (1991) 1848 –1851.
[66] B. André, T. Castelain, C. Bailly, Experimental exploration of underexpanded su-
personic jets, Shock Waves 24 (2014) 21 –32.
[67] H. Ashkenas, F.S. Sherman, The structure and utilization of supersonic free jets in
low density wind tunnels, in: Proceedings of the 4th International Symposium on
Rareﬁed Gas Dynamics, vol. 2(7), 1964, pp. 84 –105.
[68] V.S. Avduevskii, A.V. Ivanov, I.M. Karpman, V.D. Traskovskii, M.Ya. Yudelovich,
Flow in supersonic viscous underexpanded jet, Fluid Dyn. 5 (1970) 409 –414.
[69] V.S. Avduevskii, A.V. Ivanov, I.M. Karpman, V.D. Traskovskii, M.Ya. Yudelovich,
Effect of viscosity on the ﬂow in the initial part of a highly underexpanded jets,
Sov. Phys. Dokl. Fluid Mech. 16 (3) (1971) 186 –189.
[70] V.S. Avduevskii, A.V. Ivanov, I.M. Karpman, V.D. Traskovskii, M.Ya. Yudelovich,
Structure of turbulent underexpanded jets issuing into an immersed space and
coﬂow, Fluid Dyn. 7 (3) (1972) 380 –391.
[71] K. Bier, B. Schmidt, Form of compression shocks in freely expanding gas jets, Zeit.
Angew. Phys. 13 (1961) 493 –500.
[72] F.S. Billig, R.C. Orth, M. Lasky, Uni ﬁed analysis of gaseous jet penetration, AIAA J. 9
(6) (1971).
[73] F.I. Buckley Jr, Mach disk location in jets in co- ﬂowing airstreams, AIAA J. 13 (1975)
105–106.
[74] S. Crist, P.M. Sherman, D.R. Glass, Study of the highly underexpanded sonic jet,
AIAA J. 4 (1966) 68 –71.
[75] D. D'Ambrosio, L.M. De Socio, G. Gaffuri, Physical and numerical experiments on
an under-expanded jet, Meccanica 34 (1999) 267 –280, http://dx.doi.org/10.1023/
A:1004799204306.
[76] L. D'Attore, F. Harshbarger, Further experimental and theoretical studies of un-
derexpanded jets near the Mach disc, Technical Report, Defense Documentation
Center, 1964.
[77] M.D. Di Rosa, A.Y. Chang, R.K. Hanson, Continuous wave dye-laser technique for
simultaneous, spatially resolved measurements of temperature, pressure, and
velocity of NO in an underexpanded free jet, Appl. Opt. 32 (21) (1993) 4074 –4087.
[78] Yu.P. Finat'ev, L.A. Shcherbakov, N.M. Gorskaya, Mach number distribution over
the axis of supersonic underexpanded jets, J. Eng. Phys. 15 (1968) 1 153 –1157.
[79] G.I. Gannochenko, L.S. Ermolayev, N.A. Zadorozhnyi, On the position of the central
compression shock in an underexpanded sonic jet issuing from a slot nozzle,
J. Appl. Mech. Tech. Phys. 4 (1986) (89 þ91).
[80] Yu.A. Gostintsev, V.V. Zelentsov, V.S. Ilyukhin, P.F. Pokhil, Structure of under-
expanded supersonic swirling gas jet, Fluid Dyn. 4 (5) (1969) 105 –107.
[81] K. Hatanaka, T. Saito, In ﬂuence of nozzle geometry on underexpanded axisym-
metric free jet characteristics, Shock Waves 22 (2012) 427 –434.
[82] H. Katanoda, Y. Miyazato, M. Masuda, K. Matsuo, Pitot pressures of correctly-ex-
panded and underexpanded free jets from axisymmetric supersonic nozzles,
Shock Waves 10 (2) (2000) 95 –101.
[83] C.H. Lewis Jr, D.J. Carlson, Normal shock location in underexpanded gas and gas-
particle jets, AIAA J. 2 (4) (1964) 776 –777.
[84] Y. Otobe, S. Matsuo, M. Tanaka, H. Kashimura, T. Setoguchi, A study on char-
acteristics of under-expanded condensing jet, JSME Int. J. Ser. B Fluids Therm. Eng.
49 (4) (2006) 1 165 –1172.
[85] W.J. Sheeran, D.S. Dosanjh, Observations on jet ﬂows from a two-dimensional,
underexpanded, sonic nozzle, AIAA J. 6 (1968) 540 –542.
[86] M. Sommerfeld, The structure of particle-laden, underexpanded free jets, Shock
Waves 3 (1994) 299 –311.
[87] Katsu'ine Tabei, Hiroyuki Shirai, Fumio Takakusagi, Density measurements of
underexpanded free jets of air from circular and square nozzles by means of
Moiré–Schlieren method, JSME Int. J. 35 (2) (1992) 212 –217.
[88] V.V. Volchkov, A.V. Ivanov, Thickness and internal structure of a normal shock
formed by discharge of a highly underexpanded jet into a low-density space, Fluid
Dyn. 4 (1969) 1 13–115 ,http://dx.doi.org/10.1007/BF01025156.
[89] M.J. Werle, D.G. Shaffer, R.T. Driftmyer, On freejet terminal shocks, AIAA J. 8 (1970)
2295–2297.
[90] Donald E. Wilcox, Alexander Weir Jr, J.A. Nicholls, Roger Dunlap, Location of Mach
discs and diamonds in supersonic air jets, J. Aeronaut. Sci. 24 (2) (1957) 145 –160.
[91] J.A. Wilkes, C.E. Glass, P.M. Danehy, R.J. Nowak, Fluorescence imaging of under-
expanded jets and comparison with CFD, Technical Report, NASA, 2007 , AIAA.
[92] P.-K. Wu, T.H. Chen, Injection of supercritical ethylene in nitrogen, J. Propuls.
Power 12 (4) (1996) 770 –777.
[93] B. Yip, K. Lyons, M. Long, Visualization of a supersonic underexpanded jet by
planar Rayleigh scattering, Phys. Fluids A 1 (9) (1989) 1449 –1450.
[94] V.I. Zapryagaev, V.I. Kornilov, A.V. Lokotko, Experimental investigation of shock
wave structure and streamwise vortices in supersonic jet, in: 4th European
Symposium on Aerothermodynamics for Space Applications, 2002.
[95] A.N. Abdelhamid, D.S. Dosanjh, Mach disk and Riemann wave in underexpanded
jet ﬂows, AIAA J. 6 (1969) 69 –665.
[96] M. Abbett, Mach disk in underexpanded exhaust plumes, AIAA J. 9 (3) (1971)
512–514.
[97] F. Albini, Approximate computation of underexpanded jet structure, AIAA J. 3 (8)
(1965) 1535–1537.
[98] J. Bowyer, L. D'Attore, H. Yoshihara, Transonic aspects of hypervelocity rocket
plumes, in Supersonic Flow, Chemical Processes and Radiative Transfer, Pergamon
Press, London, 1964, pp. 201 –210.
[99] I.S. Chang, W.L. Chow, Mach disc from underexpanded axisymmetric nozzle ﬂow,
AIAA J. 12 (8) (1974) 1079 –1082.
[100] D.W. Eastman, L.P. Radtke, Location of the normal shock wave in the exhaust
plume of a jet, AIAA J. 1 (1963) 918 –919.
[101] J.H. Fox, On the structure of jet plumes, AIAA J. 12 (1974) 105 –107.
[102] C.N. Kelber, S. Jarvis Jr, An analysis of the gas ﬂow from a very high pressure nozzle.
Technical Report, Frankford Arsenal, 1952.
[103] J.C. Lengrand, J. Allègre, M. Raf ﬁn, Underexpanded free jets and their interaction
with adjacent surfaces, AIAA J. 14 (1982) 401 1 .
[104] J.P. Moran, Similarity in high-altitude jets, AIAA J. 5 (7) (1967) 1343 –1345.
[105] I.N. Murzinov, Similarity parameters for the escape of a strongly underexpanded
jet into a ﬂooded space, Fluid Dyn. 6 (1971) 675 –680.
[106] C.E. Peters, W.J. Phares, The structure of plumes from moderately underexpanded
supersonic nozzle, AIAA Paper 70-229, 1970.
[107] C.E. Peters, W.J. Phares, An approximate analysis of the shock structure in under-
expanded plumes, Technical Report, Defense Documentation Center, 1976.
[108] M.D. Salas, The numerical calculation of inviscid plume ﬂow ﬁelds, AIAA Paper 74
(523) (197 4).
[109] Wen S. Young, Derivation of the free-jet Mach-disk location using the entropy-
balance principle, Phys. Fluids 18 (1 1) (1975) 1421 –1425.
[1 10] A. Alam, T. Setoguchi, Effect of in ﬂow conditions on under-expanded supersonic
jets, Int. J. Eng. Appl. Sci. 4 (1) (2012) 1 7 –30.
[1 1 1]Er-yun Chen, Da-wei Ma, Gui-gao Le, Kai Wang, Gai-ping Zhao, Numerical simu-
lation of highly underexpanded axisymmetric jet with Runge –Kutta discontinuous
Galerkin ﬁnite element method, J. Hydrodyn. Ser. B 20 (5) (2008) 617 –623.
[1 12] S.M. Dash, R.D. Thorpe, Shock-capturing model for one- and two-phase supersonic
exhaust ﬂow, AIAA J. 19 (7) (1981) 842 –851.
[1 13] P. Dubs, M. Khalij, R. Benelmir, A. Tazibt, Study on the dynamical characteristics of a
supersonic high pressure ratio underexpanded impinging ideal gas jet through
numerical simulations, Mech. Res. Commun. 38 (3) (201 1) 267 –273.
[1 14] I.A. Graur, T.G. Elizarova, J.C. Lengrand, Numerical computation of shock wave
conﬁgurations in underexpanded viscous jets, in: 22nd International Symposium
on Shock Wave, 1999, pp. 1 –25.
[1 15] T. Irie, T. Yasunobu, H. Kashimura, T. Setogushi, Characteristics of the Mach disk in
the underexpanded jet in which the back pressure continuously changes with
time, J. Therm. Sci. 12 (2) (2003) 132 –137.
[1 16] G. Lehnasch, P. Bruel, A robust methodology for RANS simulations of highly un-
derexpanded jets, Int. J. Numer. Methods Fluids 56 (12) (2008) 21 79 –2205.
[1 1 7]S. Matsuo, M. Tanaka, Y. Otobe, H. Kashimura, H.-D. Kim, T. Setoguchi, Effect of
axisymmetric sonic nozzle geometry on characteristics of supersonic air jet,
E. Franquet et al. / Progress in Aerospace Sciences 77 (2015) 25 –5350

<!-- PDF_PAGE: 27 -->

J. Therm. Sci. 13 (2) (2004) 121 –126.
[1 18] S. Matsuo, Y. Otobe, M. Tanaka, H. Kashimura, T. Setoguchi, S. Yu, Effect of non-
equilibrium condensation on axisymmetric under-expanded jet, Int. J. Turbo Jet
Engines 21 (2004) 193 –201.
[1 19] F. Nasuti, R. Niccoli, M. Onofri, A numerical methodology to predict exhaust plumes
of propulsion nozzles, J. Fluids Eng., Trans. ASME 120 (3) (1998) 563 –569.
[120] S.M. Prudhomme, H. Haj-Hariri, Investigation of supersonic underexpanded jets
using adaptive unstructured ﬁnite elements, Finite Elem. Anal. Des. 1 7 (June (1))
(1994) 21–40.
[121] Alexey Velikorodny, Sergey Kudriakov, Numerical study of the near- ﬁeld of highly
underexpanded turbulent gas jets, Int. J. Hydrog. Energy 37 (22) (2012)
1 7390–17399.
[122] M.A. Woodmansee, V. Iyer, J.C. Dutton, R.P. Lucht, Nonintrusive pressure and
temperature measurements in an underexpanded sonic jet ﬂowﬁeld, AIAA J. 42 (6)
(2004) 1 1 70–118 0.
[123] N.I. Kislyakov, A.K. Rebrov, R.G. Sharafutdinov, Structure of high-pressure low-
density jets beyond a supersonic nozzle, J. Appl. Mech. Tech. Phys. 16 (1975)
187–195.
[124] V.I. Nemchenko, N.I. Yushchenkova, Structure of low-density supersonic jet,
J. Appl. Mech. Tech. Phys. 10 (6) (1969) 941 –945.
[125] W. Davidor, S.S. Penner, Shock standoff distances and Mach-disk diameters in
underexpanded sonic jets, AIAA J. 9 (8) (1971) 1651 –1653.
[126] L. D'Attore, F. Harshbarger, Parameters affecting the normal shock location in
underexpanded gas jets, AIAA J. 3 (3) (1965) 530 .
[127] J.C. Lengrand, J. Allègre, M. Raf ﬁn, Experimental investigation of under expanded
exhaust plumes, AIAA J. 14 (1976) 692 –694.
[128] V.I. Nemchenko, Investigation of the closing shock in a supersonic submerged
underexpanded gas jet, J. Eng. Phys. 20 (5) (1971) 648 –654.
[129] B.A. Sodek, ATM optical contamination study, Technical Report, Research Labora-
tories Brown Engineering Company, 1968.
[130] Heuy-Dong Kim, Min-Sung Kang, Yumiko Otobe, Toshiaki Setoguchi, The effect of
nonequilibrium condensation on hysteresis phenomenon of under-expanded jets,
J. Mech. Sci. Technol. 23 (3) (2009) 856 –867.
[131] E. Franquet, V. Perrier, S. Gibout, P. Bruel, Free underexpanded jets in a quiescent
medium: a review, Technical Report, Univ. Pau & Pay Adour, 2015.
[132] K.J. Badcock, B.E. Richards, M.A. Woodgate, Elements of computational ﬂuid dy-
namics on block structured grids using implicit solvers, Prog. Aerosp. Sci. 36 (5 –6)
(2000) 351 –392.
[133] E.H. Andrews, A.R. Vick, C.B. Craidon, Theoretical boundaries and internal char-
acteristics of exhaust plumes from three different supersonic nozzles, Technical
Note D-2650, NASA, 1965.
[134] M. Belan, S. De Ponte, S. Massaglia, D. Tordella, Experiments and numerical si-
mulations on the mid-term evolution of hypersonic jets, Astrophys. Space Sci. 293
(2004) 225 –232.
[135] M. Belan, S. De Ponte, D. Tordella, Determination of density and concentration
from ﬂuorescent images of a gas ﬂow, Exp. Fluids 45 (2008) 501 –511.
[136] I.S. Belotserkovets, V.I. Timoshenko, Calculating the boundaries of a supersonic
nonviscous jet entering a submerged space or a companion supersonic ﬂow, J. Eng.
Phys. 40 (2) (1981) 109 –113.
[137] Frederick Boynton, Alex Thomson, Numerical computation of steady, supersonic,
two-dimensional gas ﬂow in natural coordinates, J. Comput. Phys. 3 (3) (1969)
379–398.
[138] T.T. Bui, CFD analysis of nozzle jet plume effects on sonic boom signature, TM
214650, NASA, 2009.
[139] V.G. Dulov, G.I. Smirnova, Calculation of the principal parameters of free super-
sonic jets of an ideal compressible ﬂuid, J. Appl. Mech. Tech. Phys. 12 (3) (1971)
387–392.
[140] A.V. Ivanov, N.V. Stankus, S.F. Chekmarev, Hypersonic multicycle gas jet with a
high degree of underexpansion at the nozzle exit, Fluid Dyn. 19 (6) (1984)
880–888.
[141] F.P. Boynton, Highly underexpanded jet structure: exact and approximate calcu-
lations, AIAA J. 5 (9) (1967) 1 703 –1 704.
[142] J. Hartmann, F. Lazarus IV, The air-jet with a velocity exceeding that of sound,
Philos. Mag. Ser. 7 31 (204) (1941) 35 –50.
[143] K.A. Phalnikar, R. Kumar, F.S. Alvi, Experiments on free and impinging supersonic
microjets, Exp. Fluids 44 (5) (2008) 819 –830.
[144] V.M. Aniskin, A.A. Maslov, S.G. Mironov, Effect of nozzle size on supersonic mi-
crojet length, Tech. Phys. Lett. 37 (1 1) (201 1) 1046 –1048.
[145] Vladimir Aniskin, Sergey Mironov, Anatoliy Maslov, Investigation of the structure
of supersonic nitrogen microjets, Micro ﬂuid. Nano ﬂuid. 14 (3 –4) (2013) 605 –614.
[146] C.K.W. Tam, H.K. Tanna, Shock associated noise of supersonic jets from con-
vergent–divergent nozzles, J. Sound Vib. 81 (3) (1982) 337 –
358.
[147] T.S. Cheng, K.S. Lee, Numerical simulations of underexpanded supersonic jet and
free shear layer using WENO schemes, Int. J. Heat Fluid Flow 26 (5) (2005)
755–770.
[148] S.G. Chuech, M.-C. Lai, G.M. Faeth, Structure of turbulent sonic underexpanded free
jets, AIAA J. 27 (5) (1989) 549 –559.
[149] S.D. Scroggs, G.S. Settles, An experimental study of supersonic microjets, Exp.
Fluids 21 (6) (1996) 401 –409.
[150] K.B.M.Q. Zaman, Asymptotic spreading rate of initially compressible jets —experi-
ment and analysis, Phys. Fluids 10 (10) (1998) 2652 –2660.
[151] S. Clement, E. Rathakrishnan, Characteristics of sonic jets with tabs, Shock Waves
15 (3–4) (2006) 219 –227.
[152] S.A. Novopashin, A.L. Perepelkin, Axial symmetry loss of a supersonic preturbulent
jet, Phys. Lett. A 135 (1989) 290 –293.
[153] P.O. Witze, A generalised theory for the turbulent mixing of axially symmetric
compressible free jets, in: Fluids Mechanics of Mixing, 1973, pp. 63 –77.
[154] P.O. Witze, Centerline velocity decay of compressible free jets, AIAA J. 12 (4) (1974)
417–418.
[155] J.W. Shirie, J.G. Seubold, Length of supersonic core in high-speed jets, AIAA J. 5 (1 1)
(1967) 2062–2064.
[156] Tieh-Feng Hu, D.K. McLaughlin, Flow and acoustic properties of low Reynolds
number underexpanded supersonic jets, J. Sound Vib. 141 (3) (1990) 485 –505.
[157] S.A. Arnette, M. Samimy, G.S. Elliott, On streamwise vortices in high Reynolds
number supersonic axisymmetric jets, Phys. Fluids A 5 (1) (1993) 187 –202.
[158] E. Gutmark, K.C. Schadow, C.J. Bicker, Mode switching in supersonic circular jets,
Phys. Fluids A: Fluid Dyn. 1 (5) (1989) 868 –873.
[159] V.A. Kochnev, I.M. Naboko, Flat supersonic underexpanded jets using a laser
schlieren method, J. Appl. Mech. Tech. Phys. 24 (1) (1983) 49 –56.
[160] A. Krothapalli, P.J. Strykowski, C.J. King, Origin of streamwise vortices in supersonic
jets, AIAA J. 36 (5) (1998) 869 –872.
[161] V.Ya. Levchenko, V.M. Fomin, Aerogasdynamic investigations at the institute of
theoretical and applied mechanics in the last decade, J. Appl. Mech. Tech. Phys. 38
(4) (1997) 535 –565.
[162] V.A. Mal'tsev, S.A. Novopashin, A.L. Perepelkin, Effect of the plenum-chamber
diameter on the turbulent characteristics of a supersonic jet, J. Appl. Mech. Tech.
Phys. 40 (6) (1999) 1057 –1060.
[163] O.A. Nerushev, S.A. Novopashin, A.L. Perepelkin, Transition to turbulence in su-
personic jets of nitrogen and argon, Fluid Dyn. 33 (3) (1998) 459 –462.
[164] J. Panda, Shock oscillation in underexpanded screeching jets, J. Fluid Mech. 363 (1)
(1998) 173–198.
[165] V.N. Zaikovskii, S.P. Kiselev, V.P. Kiselev, Large-scale streamwise vortices in the
supersonic part of a permeable nozzle, J. Appl. Mech. Tech. Phys. 46 (5) (2005)
670–676.
[166] V.I. Zapryagaev, A.V. Solotchin, Three-dimensional structure of ﬂow in a super-
sonic underexpanded jet, J. Appl. Mech. Tech. Phys. 32 (1991) 503 –507, http://dx.
doi.org/10.1007/BF00851550.
[167] V.I. Zapryagaev, S.G. Mironov, A.V. Solotchin, Spectral composition of wave num-
bers of longitudinal vortices and characteristics of ﬂow structure in a supersonic
jet, J. Appl. Mech. Tech. Phys. 34 (5) (1993) 634 –640.
[168] V.I. Zapryagaev, A.V. Solotchin, Development of streamwise vortices in the initial
section of a supersonic non-isobaric jet in the presence of microroughness of the
inner nozzle surface, Fluid Dyn. 32 (3) (1997) 465 –469.
[169] V.I. Zapryagaev, A.V. Solotchin, An experimental investigation of the nozzle
roughness effect on streamwise vortices in a supersonic jet, J. Appl. Mech. Tech.
Phys. 38 (1) (1997) 78 –86.
[1 70] V.I. Zapryagaev, A.V. Solotchin, N.P. Kiselev, Structure of a supersonic jet with
varied geometry of the nozzle entrance, J. Appl. Mech. Tech. Phys. 43 (4) (2002)
538–543.
[1 71] V. Zapryagaev, V. Pickalov, N. Kiselev, A. Nepomnyashchiy, Combination interac-
tion of Taylor –Goertler vortices in a curved shear layer of a supersonic jet, Theor.
Comput. Fluid Dyn. 18 (2004) 301 –308, http://dx.doi.org/10.1007/
s00162-004-0141-5.
[1 72] V.I. Zapryagaev, N.P. Kiselev, A.A. Pavlov, Effect of streamline curvature on intensity
of streamwise vortices in the mixing layer of supersonic jets, J. Appl. Mech. Tech.
Phys. 45 (3) (2004) 335 –343.
[1 73] V.I. Zapryagaev, A.P. Petrov, A.V. Solotchin, Investigation of nonuniformity of the
velocity distribution in the shear layer of an underexpanded jet by electric dis-
charge tracing of the ﬂow, J. Appl. Mech. Tech. Phys. 45 (6) (2004) 822 –827.
[1 74] V.I. Zapryagaev, A.V. Solotchin, Spectral characteristics of unstable ﬂow in the
mixing layer of supersonic underexpanded jet over its initial region, Thermophys.
Aeromech. 16 (2) (2009) 209 –218.
[1 75] S.M. Dash, R.G. Wilmoth, H.S. Pergament, An overlaid viscous/inviscid model for
the prediction of near ﬁeld jet entrainment, AIAA J. 1 7 (1979) 950 –958.
[1 76] S.M. Dash, D.E. Wolf, Interactive phenomena in supersonic jet mixing problems.
Part II: numerical studies, AIAA J. 22 (10) (1984) 1395 –1404.
[1 77] L.L. Smarr, M.L. Norman, K.-H.A. Winkler, Shocks, interfaces, and patterns in su-
personic jets, Physica D: Nonlinear Phenom. 12 (1 –3) (1984) 83 –106.
[1 78] N.M. Terekhova, Effect of ﬂow nonparallelism on instability of the Taylor –Görtler
waves in supersonic axisymmetric jets, J. Appl. Mech. Tech. Phys. 41 (4) (2000)
604–611.
[1 79] N.M. Terekhova, Nonlinear group interactions of the Taylor –Görtler disturbances in
supersonic axisymmetric jets, J. Appl. Mech. Tech. Phys. 45 (5) (2004) 647 –655.
[180] N.A. Zheltukhin, N.M. Terekhova, Disturbances of high modes in a supersonic jet,
J. Appl. Mech. Tech. Phys. 31 (2) (1990) 232 –239.
[181] N.A. Zheltukhin, N.M. Terekhova, Taylor –Görtler instability in a supersonic jet,
J. Appl. Mech. Tech. Phys. 34 (5) (1993) 640 –647.
[182] H. Oertel Sen, F. Seiler, J. Srulijes, New explanation of noise production by super-
sonic jets with gas dredging, in: Andreas Dillmann, Gerd Heller, Michael Klaas,
Hans-Peter Kreplin, Wolfgang Nitsche, Wolfgang Schröder (Eds.), New Results in
Numerical and Experimental Fluid Mechanics VII, Notes on Numerical Fluid Me-
chanics and Multidisciplinary Design, vol. 1 12, Springer, Berlin, Heidelberg, 2010,
pp. 389 –397 .
[183] H. Oertel Sen, F. Seiler, J. Srulijes, Vortex induced Mach waves in supersonic jets, in:
Konstantinos Kontis (Ed.), 28th International Symposium on Shock Waves,
Springer, Berlin, Heidelberg, 2012, pp. 657 –663.
[184] J. Panda, R.G. Seasholtz, Measurement of shock structure and shock-vortex inter-
action in underexpanded jets using Rayleigh scattering, Phys. Fluids 1 1 (12) (1999)
3761–3777.
[185] H. Oertel Sen, F. Seiler, J. Srulijes, Visualization of Mach waves produced by a su-
personic jet and theoretical explanations, J. Vis. 16 (4) (2013) 303 –312.
[186] C.J. Moore, The role of shear-layer instability waves in jet exhaust noise, J. Fluid
Mech. 80 (321 –367) (1977) 4 .
[187] H.K. Tanna, W.H. Brown, C.K.W. Tam, Shock associated noise of inverted-pro ﬁle
coannular jets, part I: experiments, J. Sound Vib. 98 (1) (1985) 95 –113.
[188] C.K.W. Tam, H.K. Tanna, Shock associated noise of inverted-pro ﬁle coannular jets,
part II: condition for minimum noise, J. Sound Vib. 98 (1) (1985) 1 15 –125.
[189] C.K.W. Tam, H.K. Tanna, Shock associated noise of inverted-pro ﬁle coannular jets,
part III: shock structure and noise characteristics, J. Sound Vib. 98 (1) (1985)
127
–145.
[190] C.K.W. Tam, Supersonic jet noise, Annu. Rev. Fluid Mech. 27 (1) (1995) 17 –43.
[191] N.E. Afonina, S.A. Vasil'evskii, V.G. Gromov, A.F. Kolesnikov, I.S. Pershin, V.
I. Sakharov, M.I. Yakushin, Flow and heat transfer in underexpanded air jets issuing
from the sonic nozzle of a plasma generator, Fluid Dyn. 37 (5) (2002) 803 –814.
[192] I.D. Boyd, P.F. Penko, D.L. Meissner, K.J. Dewitt, Experimental and numerical in-
vestigations of low-density nozzle and plume ﬂows of nitrogen, AIAA J. 30 (10)
E. Franquet et al. / Progress in Aerospace Sciences 77 (2015) 25 –53 51

<!-- PDF_PAGE: 28 -->

(1992) 2453–2461.
[193] C.B. Devaud, J.B. Kelman, J.B. Moss, C.D. Stewart, Stability of underexpanded su-
personic jet ﬂames burning H 2-CO mixtures, Shock Waves 12 (2002) 241 –249.
[194] J. Dubois, M. Amielh, F. Anselmet, O. Gentilhomme, Investigation of axisymmetric
underexpanded air and helium jets by background oriented schlieren, J. Vis. 12
(2009) 192 .
[195] R.E. Foglesong, S.M. Green, R.P. Lucht, J.C. Dutton, Dual-pump coherent anti-stokes
Raman scattering for simultaneous pressure/temperature measurement, AIAA J. 36
(2) (1998) 234 –240.
[196] A.N. Gordeev, A.F. Kolesnikov, V.I. Sakharov, Flow and heat transfer in under-
expanded nonequilibrium jets of an induction plasmatron, Fluid Dyn. 46 (4) (201 1)
623–633.
[197] Kenneth Harstad, Josette Bellan, Global analysis and parametric dependencies for
potential unintended hydrogen-fuel releases, Combust. Flame 144 (1 –2) (2006)
89–102.
[198] V.A. Ivanov, G.A. Luk'yanov, I.V. Shatalov, Effect of rarefaction and the temperature
factor on the structure and parameters of supersonic underexpanded jets of a
monatomic gas, J. Appl. Mech. Tech. Phys. 28 (1987) 859 –863.
[199] N.I. Kislyakov, A.K. Rebrov, R.G. Sharafutdinov, Diffusion processes in the mixing
zone of a supersonic jet of low density, J. Appl. Mech. Tech. Phys. 14 (1) (1973)
99–104.
[200] K. Kurita, T. Okai, K. Ueno, N. Kawada, M. Kato, Velocity and temperature dis-
tributions in an underexpanded supersonic jet by using a laser induced ﬂuores-
cence, Anal. Sci. 7 (1991) 1459 –1462.
[201] L.I. Kuznetsov, A.K. Rebrov, V.N. Yarygin, High-temperature jets of low-density
argon beyond a sonic nozzle, J. Appl. Mech. Tech. Phys. 16 (1975) 378 –382.
[202] P. Lovaraju, E. Rathakrishnan, Effect of cross-wire location on the mixing of un-
derexpanded sonic jets, J. Aerosp. Eng. 20 (3) (2007) 179 –185.
[203] P.V. Marrone, Temperature and density measurements in free jet and shock waves,
Phys. Fluids 10 (1967) 521 –538.
[204] B. Maté, G. Tejeda, S. Montero, Raman spectroscopy of supersonic jets of CO 2:
density, condensation, and translational, rotational, and vibrational temperatures,
J. Chem. Phys. 108 (7) (1998) 2676 –2685.
[205] B. Maté, I.A. Graur, T. Elizarova, I. Chirokov, G. Tejeda, J.M. Fernández, S. Montero,
Experimental and numerical investigation of an axisymmetric supersonic jet,
J. Fluid Mech. 426 (2001) 1 77 –197.
[206] V.V. Volchkov, A.V. Ivanov, N.I. Kislyakov, A.K. Rebrov, V.A. Sukhnev,
R.G. Sharafutdinov, Low-density jets beyond a sonic nozzle at large pressure drops,
Zh. Prikl. Mekh. Tekhn. 2 (64 –73) (1973).
[207] K.B. Yüceil, M.V. Ötügen, Scaling parameters for underexpanded supersonic jets,
Phys. Fluids 14 (12) (2002) 4206 –4215.
[208] V.N. Gusev, T.V. Klimova, V.V. Ryabov, Similarity of ﬂows in strongly under-
expanded jets of viscous gas, Izvetiya Akad. Nauk SSSR, Mekh. Zhidkosti i Gaza 6
(1 17–125) (1977).
[209] A.N. Kraiko, On the free unsteady expansion of an ideal gas, Fluid Dyn. 28 (4)
(1993) 553–559.
[210] P.L. Owen, C.K. Thornhill, The ﬂow in an axially-symmetric supersonic jet from a
nearly sonic ori ﬁce into a vacuum, Technical Report, British Aeronautical Research
Council, 1952.
[21 1] V.V. Riabov, Aerodynamic applications of underexpanded hypersonic viscous jets,
J. Aircr. 32 (3) (1995) 471 –479.
[212] I. Al-Qadi, J.N. Scott, Simulations of unsteady behavior in under-expanded super-
sonic rectangular jets, AIAA Paper, 2001, p. 21 19.
[213] P.S. Cumber, M. Fairweather, S.A.E.G. Falle, J.R. Giddings, Predictions of impacting
sonic and supersonic jets, J. Fluids Eng. 1 19 (1997) 83 –89.
[214] S.M. Dash, B.E. Pearce, H.S. Pergament, E.S. Fishburne, Prediction of rocket plume
ﬂow ﬁelds for infrared signature studies, J. Spacecr. Rockets 1 7 (1960) 190 –199.
[215] S.M. Dash, D.E. Wolf, J.M. Seiner, Analysis of turbulent underexpanded jets, part I:
parabolized Navier –Stokes model, SCIPVIS, AIAA J. 23 (1985) 505 –514.
[216] M. Fairweather, K.R. Ranson, Prediction of underexpanded jets using compressi-
bility-corrected, two-equation turbulence models, Prog. Comput. Fluid Dyn. 6 (1 –
3) (2006) 122 –128.
[217] Andrew T. Hsu, Meng-Sing Liou, A computational analysis of under-expanded jets
in the hypersonic regime, J. Propuls. Power 7 (2) (1991) 297 –299.
[218] S.A. Isaev, Yu.M. Lipnitskii, P.A. Baranov, A.V. Panasenko, A.E. Usachov, Simulation
of a turbulent supersonic underexpanded jet ﬂowing into a submerged space with
the help of a shear stress transfer model, J. Eng. Phys. Thermophys. 85 (2012)
1357–1371.
[219] M.L. Norman, L. Smarr, K.-H.A. Winkler, M.D. Smith, Structure and dynamic of
supersonic jets, Astron. Astrophys. 1 13 (1982) 285 –302.
[220] W.L. Oberkampf, M. Talpallikar, Analysis of a high-velocity oxygen-fuel (HVOF)
thermal spray torch part 1: numerical formulation, J. Therm. Spray Technol. 5 (1)
(1996) 53–61.
[221] W.L. Oberkampf, M. Talpallikar, Analysis of a high-velocity oxygen-fuel (HVOF)
thermal spray torch part 2: computational results, J. Therm. Spray Technol. 5 (1)
(1996) 62–68.
[222] A. Palacio, M.R. Malin, N. Proumen, L. Sanchez, Numerical computations of steady
transonic and supersonic ﬂow ﬁelds, Int. J. Heat Mass Transf. 33 (6) (1990)
119 3–1204.
[223] E. Venkatapathy, W.J. Feiereisen, 3-D plume ﬂow computations with an upwind
solver, AIAA Paper 88 (3158) (1988) .
[224] A.D. Birch, D.R. Brown, M.G. Dodson, F. Swaf ﬁeld, The structure and concentration
decay of high pressure jets of natural gas, Combust. Sci. Technol. 36 (5) (1984)
249–261.
[225] A.D. Birch, D.J. Hughes, F. Swaf ﬁeld, Velocity decay of high pressure jets, Combust.
Sci. Technol. 52 (1987) 161 –171.
[226] J. Chaineaux, G. Mavrothalassitis, J. Pineau, Modelization and validation of the
discharge in air of a vessel pressurized by ﬂammable gas, Prog. Astronaut. Aero-
naut. 134 (1991) 104 –137.
[227] J.P. Gore, G.M. Faeth, Structure and radiation properties of large-scale natural gas/
air diffusion ﬂames, Fire Mater. 10 (1986) 161 –169.
[228] Philip G. Hill, Patric Ouellette, Transient turbulent gaseous fuel jets for diesel en-
gines, J. Fluids Eng. 121 (1) (1999) 93 –101.
[229] G.T. Kalghatgi, Blow-out stability of gaseous jet diffusion ﬂames. Part I: in still air,
Combust. Sci. Technol. 26 (5 –6) (1981) 233 –239.
[230] E. Papanikolaou, D. Baraldi, M. Kuznetsov, A. Venetsanos, Evaluation of notional
nozzle approaches for CFD simulations of free-shear under-expanded hydrogen
jets, Int. J. Hydrog. Energy 37 (23) (2012) 18563 –18574.
[231] E. Ruf ﬁn, Y. Mouilleau, J. Chaineaux, Large scale characterization of the con-
centration ﬁeld of supercritical jets of hydrogen and methane, J. Loss Prev. Process
Ind. 9 (4) (1996) 279 –284.
[232] P.D. Sunavala, C. Hulse, M.W. Thring, Mixing and combustion in free and enclosed
turbulent jet diffusion ﬂames, Combust. Flame 1 (2) (1957) 179 –193.
[233] J.D. Cole, Note on the axisymmetric sonic jet, SIAM J. Appl. Math. 43 (4) (1983)
944–948.
[234] William Houf, Robert Schefer, Predicting radiative heat ﬂuxes and ﬂammability
envelopes from unintended releases of hydrogen, Int. J. Hydrog. Energy 32 (1)
(2007) 136 –151.
[235] W.G. Houf, G.H. Evans, R.W. Schefer, Analysis of jet ﬂames and unignited jets from
unintended releases of hydrogen, Int. J. Hydrog. Energy 34 (14) (2009) 5961 –5969.
[236] Renato Benintendi, Turbulent jet modelling for hazardous area classi ﬁcation,
J. Loss Prev. Process Ind. 23 (3) (2010) 373 –378.
[237] J.-B. Saffers, V.V. Molkov, Towards hydrogen safety engineering for reacting and
non-reacting hydrogen releases, J. Loss Prev. Process Ind. 26 (2) (2013) 344 –350.
[238] Ivar Øyvind Sand, Karl Sjøen, Jan Roar Bakke, Modelling of release of gas from high
pressure pipelines, Int. J. Numer. Methods Fluids 23 (9) (1996) 953 –983.
[239] R.W. Schefer, W.G. Houf, T.C. Williams, B. Bourne, J. Colton, Characterization of
high-pressure, underexpanded hydrogen-jet ﬂames, Int. J. Hydrog. Energy 32 (12)
(2007) 2081 –2093.
[240] D.M. Webber, M.J. Ivings, R.C. Santon, Ventilation theory and dispersion modelling
applied to hazardous area classi ﬁcation, J. Loss Prev. Process Ind. 24 (5) (201 1)
612–621.
[241] W.S. Winters, G.H. Evans, Final report for the ASC gas –powder two-phase ﬂow
modeling project, Technical Report, Sandia National Laboratories Report No.
SAND2006-7579, 2007 .
[242] D. Baraldi, E. Papanikolaou, M. Heitsch, P. Moretto, R.S. Cant, D. Roekaerts,
S. Dorofeev, A. Koutchourko, P. Middha, A.V. Tchouvelev, S. Ledin, J. Wen, A.
Venetsanos, V. Molkov, Gap analysis of CFD modelling of accidental hydrogen
release and gap analysis of CFD modelling of accidental hydrogen release and
combustion, Technical Report, European Commission, Joint Research Centre,
Institute of Energy, 2010.
[243] William H. Calhoon Jr, Computational assessment of afterburning cessation me-
chanisms in fuel rich rocket exhaust plume, J. Propuls. Power 17 (1) (2001)
111–119.
[244] P. Middha, O.R. Hansen, I.E. Storvik, Validation of CFD-model for hydrogen dis-
persion, J. Loss Prev. Process Ind. 22 (6) (2009) 1034 –1038.
[245] P. Ouellette, P.G. Hill, Turbulent transient gas injections, J. Fluids Eng. 122 (4)
(2000) 743 –752.
[246] A. Rusin, K. Stolecka, Modelling the effects of failure of pipelines transporting
hydrogen, Chem. Process Eng. 32 (2) (201 1) 1 1 7–134.
[247] A. Veser, M. Kuznetsov, G. Fast, A. Friedrich, N. Kotchourko, G. Stern, M. Schwall,
W. Breitung, The structure and ﬂame propagation regimes in turbulent hydrogen
jets, Int. J. Hydrog. Energy 36 (3) (201 1) 2351 –2359.
[248] J. Xiao, J.R. Travis, W. Breitung, Hydrogen release from a high pressure gaseous
hydrogen reservoir in case of a small leak, Int. J. Hydrog. Energy 36 (3) (201 1)
2545–2554.
[249] Jinyang Zheng, Haiyan Bie, Ping Xu, Pengfei Liu, Yongzhi Zhao, Honggang Chen,
Xianxin Liu, Lei Zhao, Numerical simulation of high-pressure hydrogen jet ﬂames
during bon ﬁre test, Int. J. Hydrog. Energy 37 (1) (2012) 783 –790.
[250] M.W. Thring, M.P. Newby, Combustion length of enclosed turbulent jet ﬂames, in:
Fourth Symposium (International) on Combustion, vol. 4(1), 1953, pp. 789 –796.
[251] V. Molkov, Hydrogen safety engineering: the state-of-the-art and future progress,
in: Ali Sayigh (Ed.), Compr. Renew. Energy, vol. 4, Elsevier, Oxford, 2012,
pp. 77 –109.
[252] G. Kleinstein, Mixing in turbulent axially symmetric free jets, J. Spacecr. Rockets 1
(1964) 403–408.
[253] W.R. Warren, An Analytical and Experimental Study of Compressible Free Jets,
Report N. 381, University of Princeton, 1957.
[254] C.J. Chen, W. Rodi, Vertical Turbulent Buoyant Jets —A Review of Experimental
Data, Pergamon Press, 1980 .
[255] M.P. Davis, A.C.H. Mace, N.C. Markatos, On numerical modelling of embedded
subsonic ﬂow, Int. J. Numer. Methods Fluids 6 (3) (1986) 103 –112.
[256] B. Emami, M. Bussmann, H.N. Tran, A mean ﬂow ﬁeld solution to a moderately
under/over-expanded turbulent supersonic jet, Comptes Rendus Mécanique 337
(4) (2009) 185 –191.
[257] P.O. Jarvinen, J.S. Draper, Underexpanded gas-particle jets, AIAA J. 5 (4) (1967)
824–825.
[258] Hylton R. Murphy, David R. Miller, Effects of nozzle geometry on kinetics in free-
jet expansions, J. Phys. Chem. 88 (20) (1984) 4474 –4478.
[259] A.D. Rychkov, Flow of a mixture of gas and solid particles in supersonic under-
expanded jets, Fluid Dyn. 9 (1974) 224 –227.
[260] J.A. Schetz, F.S. Billig, Penetration of gaseous jets injected into a supersonic stream,
J. Spacecr. 3 (1 1) (1966) .
[261] Sheldon Weinbaum, Richard W. Garvine, On the two-dimensional viscous coun-
terpart of the one-dimensional sonic throat, J. Fluid Mech. 39 (01) (1969) 57 –85.
[262] R. Ishii, Y. Umeda, M. Yuhi, Numerical analysis of gas-particle two-phase ﬂows,
J. Fluid Mech. 203 (1989) 475 –515.
[263] Kaveh Mohamed, Marius Paraschivoiu, Real gas simulation of hydrogen release
from a high-pressure chamber, Int. J. Hydrog. Energy 30 (8) (2005) 903 –912.
[264] V.I. Pogorelov, G.B. Shcherbanina, Discharge of a supersonic jet from a nozzle with
an inclined rim, Fluid Dyn. 12 (4) (1977) 572 –576.
[265] R. Sinha, V. Zakhay, J. Erdos, Flow ﬁeld analysis of plumes of two dimensional
underexpanded jets by a time dependent method, AIAA J. 9 (1971) 2363 –2370.
[266] V.N. Vetlutsky, V.L. Ganimedov, M.I. Muchnaya, In ﬂuence of the opening angle of a
conical supersonic nozzle on the structure of initial interval of non-isobaric jet,
Thermophys. Aeromech. 15 (2) (2008) 197 –203.
E. Franquet et al. / Progress in Aerospace Sciences 77 (2015) 25 –5352

<!-- PDF_PAGE: 29 -->

[267] Y. Bartosiewicz, Zine Aidoun, P. Desevaux, Yves Mercadier, Numerical and ex-
perimental investigations on supersonic ejectors, Int. J. Heat Fluid Flow 26 (1)
(2005) 56 –70.
[268] P.S. Cumber, M. Fairweather, S.A.E.G. Falle, J.R. Giddings, Predictions of the struc-
ture of turbulent, moderately underexpanded jets, J. Fluids Eng. 1 16 (4) (1994)
707–713.
[269] S. Dembele, J. Zhang, J.X. Wen, Exploratory study of under-expanded sonic hy-
drogen jets and jet ﬂames, in: Proceedings of the 5th International Seminar on Fire
and Explosion Hazards, 2007.
[270] D.A. Dickmann, F.K. Lu, Jet in supersonic cross ﬂow on a ﬂat plate, in: 25th AIAA
Aerodynamic Measurement Technology and Ground Testing Conference, vol. 2,
2006, pp. 981 –992.
[271] Sujith Sukumaran, Song-Charng Kong, Numerical study on mixture formation
characteristics in a direct-injection hydrogen engine, Int. J. Hydrog. Energy 35 (15)
(2010) 7991–8007.
[272] V.N. Vetlutsky, V.L. Ganimedov, M.I. Muchnaya, Flow in a viscous jet escaping
through a supersonic nozzle into a semi-in ﬁnite ambient space, J. Appl. Mech.
Tech. Phys. 50 (6) (2009) 918 –926.
[273] E. Yamada, S. Watanabe, A.K. Hayashi, N. Tsuboi, Numerical analysis on auto-ig-
nition of a high pressure hydrogen jet spouting from a tube, Proc. Combust. Inst. 32
(2) (2009) 2363 –2369.
[274] M.V. Bragin, V.V. Molkov, Physics of spontaneous ignition of high-pressure hy-
drogen release and transition to jet ﬁre, Int. J. Hydrog. Energy 36 (3) (201 1)
2589–2596 (The Third Annual International Conference on Hydrogen Safety) .
[275] G. Lacaze, B. Cuenot, T. Poinsot, M. Oschwald, Large eddy simulation of laser ig-
nition and compressible reacting ﬂow in a rocket-like con ﬁguration, Combust.
Flame 156 (6) (2009) 1 166 –118 0.
[276] D.A. Lyubimov, Development and applications of the ef ﬁcient hydrid RANS/ILES
approach for the calculation of complex turbulent jets, High Temp. 46 (2) (2008)
243–253.
[277] D. Munday, E. Gutmark, J. Liu, K. Kailasanath, Flow structure and acoustic of su-
personic jets from conical convergent –divergent nozzles, Phys. Fluids 23 (1 1)
(2011) 116102.
[278] J.X. Wen, B.P. Xu, V.H.Y. Tam, Numerical study on spontaneous ignition of pres-
surized hydrogen release through a length of tube, Combust. Flame 156 (1 1)
(2009) 21 73–2189.
[279] J.A. Boles, J.R. Edwards, R.A. Bauerle, Large-Eddy/Reynolds-averaged Navier –Stokes
simulations of sonic injection into mach 2 cross ﬂow, AIAA J. 48 (7) (2010)
1444–1456.
[280] D. Cecere, A. Ingenito, E. Giacomazzi, L. Romagnosi, C. Bruno, Hydrogen/air su-
personic combustion for future hypersonic vehicles, Int. J. Hydrog. Energy 36 (18)
(201 1) 1 1969–1 1984.
[281] A. Dauptain, E. Gutmark, J. Liu, K. Kailasanath, Large-Eddy simulation of a stable
supersonic jet impinging on ﬂat plate, AIAA J. 48 (10) (2010) 2325 –2337.
[282] S. Kawai, S.K. Lele, Large-Eddy simulation of jet mixing in supersonic cross ﬂows,
AIAA J. 48 (2010) 2063 –2083.
[283] T. Nakano, M.D. Mahbubul Alam, S. Matsuo, M. Tanaka, T. Setoguchi, Effect of
heterogeneous condensation on axisymmetric supersonic free jets, in: Proceedings
of the International Conference on Mechanical Engineering, 2005.
[284] K.D. Kihm, T.K. Kim, S.Y. Son, Visualization of high-speed gas jets and their airblast
sprays of cross-injected liquid, Exp. Fluids 27 (1) (1999) 102 –106.
[285] Seung-Cheol Baek, Soon-Bum Kwon, Heuy-Dong Kim, Toshiaki Setoguchi,
Shigeru Matsuo, Study of moderately underexpanded supersonic moist air jets,
AIAA J. 44 (7) (2006) 1624 –1627.
[286] P.S. Cumber, Predicting out ﬂow from high pressure vessels, Process Saf. Environ.
Protect. 79 (1) (2001) 13 –22.
[287] M. Epstein, H.K. Fauske, Total ﬂammable mass and volume within a vapor cloud
produced by a continuous fuel-gas or volatile liquid-fuel release, J. Hazard. Mater.
147 (3) (2007) 1037 –1050.
[288] M.S. Ivanov, D. Vandromme, V.M. Fomin, A.N. Kudryavtsev, A. Hadjadj,
D.V. Khotyanovsky, Transition between regular and Mach re ﬂection of shock
waves: new numerical and experimental results, Shock Waves 1 1 (3) (2001)
199–207.
[289] P.V. Marrone, Rotational temperature and density measurements in under-
expanded jets and shock waves using an electron beam probe, Technical Report,
Institute for Aerospace Studies, 1966.
[290] M. Kuznetsov, Hydrogen distribution tests in free turbulent jet. Technical Report,
FZK, SBEP V4, 2006.
[291] K. Okabayashi, T. Nonaka, N. Sakata, K. Takeno, H. Hirashima, K. Chitose, Char-
acteristics of dispersion for leakage of high-pressurized hydrogen gas, Jpn. Soc. Saf.
Eng. 44 (2005) 391 –397.
[292] L.C. Shirvill, P. Roberts, C.J. Butler, T.A. Roberts, M. Royle, Characterisation of the
hazards from jet releases of hydrogen, in: First International Conference on Hy-
drogen Safety, 2005.
E. Franquet et al. / Progress in Aerospace Sciences 77 (2015) 25 –53 53
