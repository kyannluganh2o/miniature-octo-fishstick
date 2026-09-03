<!-- PDF_PAGE: 1 -->

J. Fluid Mech. (2021), vol. 913, A33, doi:10.1017/jfm.2021.7
On aerodynamic droplet breakup
Isaac M. Jackiw1 and Nasser Ashgriz1,†
1Department of Mechanical and Industrial Engineering, University of Toronto, Toronto,
ON M5S 3G8, Canada
(Received 28 August 2020; revised 24 November 2020; accepted 29 December 2020)
The breakup of droplets in a high-speed air stream is investigated experimentally and
theoretically. This study is based on experiments conducted by exposing pendant droplets
to a high-speed air jet, which allowed for imaging of the droplets at high temporal and
spatial resolutions while maintaining a large ﬁeld of view to capture the breakup process.
T wo factors of primary importance in droplet breakup are the breakup morphology and
the resulting child droplet sizes. However, benchmark models have erroneous assumptions
that impede the prediction of both morphology and breakup size and give non-physical
geometries. The present theoretical work focuses on the ‘internal ﬂow’ hypothesis, which
suggests that the droplet’s internal ﬂow governs its breakup. The breakup process is
subdivided into four stages: droplet deformation, rim formation, rim
expansion and rim
breakup. The internal ﬂow mechanism is used to mathematically model the ﬁrst two stages.
The rim expansion is related to the growth of bags, while its breakup is shown to be due to
Rayleigh–Plateau capillary instability. It is found that the breakup morphology is related to
the division of the droplet into a disk that forms on the windward face and the undeformed
droplet core. The amount of the droplet volume contained in the undeformed core decides
the breakup morphology. Using this framework, it is shown that a three-step calculation
can give an improved prediction of child drop sizes and morphology.
Key words: aerosols/atomization, drops, breakup/coalescence
1. Introduction
The study of spray atomization has numerous applications including combustion, surface
coating, pharmaceutical manufacturing and disease transmission modelling. Atomization
is conventionally subdivided into two stages: primary atomization, which describes the
breakup of the bulk liquid into smaller droplets, and secondary atomization , which
describes the further breakup of these droplets. While the study of single-droplet breakup
is directly the study of secondary atomization, it can also be applied in models for
primary atomization (O’Rourke & Amsden 1987; Varga, Lasheras & Hopﬁnger 2003;
† Email address for correspondence: ashgriz@mie.utoronto.ca
© The Author(s), 2021. Published by Cambridge University Press 913 A33-1
https://doi.org/10.1017/jfm.2021.7
 Published online by Cambridge University Press

<!-- PDF_PAGE: 2 -->

I.M. Jackiw and N. Ashgriz
(a)( b)( c)( d)
Figure 1. Images of ( a) Bag, (b) BS, (c) MB and (d) ST breakup modes.
Aliseda et al. 2008). A detailed understanding and accurate modelling of droplet breakup
is therefore crucial in the development of spray atomization applications. However, despite
extensive experimental and theoretical study, there remains disagreement in the literature
as to the underlying physical mechanisms of droplet breakup.
Droplet breakup has been historically categorized into ﬁve breakup morphologies, each
of which occur at increasing relative air velocity: Bag,
bag and stamen (BS), multibag
(MB), sheet thinning (ST) and catastrophic (Pilch & Erdman 1987; Guildenbecher,
López-Rivera & Sojka 2009). In bag breakup, a single bag forms on the leeward side
of the droplet, surrounded by a thick liquid rim. Upon breakup, the bag forms very small
droplets while the rim breaks into larger ones. The BS morphology is similar to Bag,
however
, a stamen forms at the centre of the drop, creating a large additional drop during
breakup. MB breakup is characterized by the formation of multiple bags across the drop.
In ST breakup, the periphery of the drop is deﬂected downstream and forms a sheet, which
breaks into small drops. Images of the characteristic breakup shapes are shown in ﬁgure 1.
Catastrophic breakup is when the droplet appears to explode into a multitude of fragments
and occurs at very high relative velocities.
It has been previously shown that the breakup morphologies can be classiﬁed by the
Weber number and the Ohnesorge number (Pilch & Erdman 1987)g i v e nb y( 1.1)a n d
(1.2), respectively
,
We = ρgU2d0
σ (1.1)
Oh = μl√ ρlσd0
, (1.2)
where ρg and ρl are the gas and liquid phase densities in kg m − 3, μ is the liquid viscosity
in Pa s, σ is the interfacial surface tension in N m − 1, d0 is the initial diameter of the
droplet in ma n d U is the relative velocity between the gas and the droplet in m s − 1.
A critical Weber number, Wec, is established for the transition to each morphology.
Guildenbecher et al. (2009) summarize the morphology transitions as Wec,Bag ≈ 11,
Wec,BS ≈ 18, Wec,MB ≈ 35 and Wec,ST ≈ 80. Comparatively, Zhao et al. (2010)g i v e
values of Wec,Bag ≈ 12, Wec,BS ≈ 16, Wec,MB ≈ 28, and Wec,ST ≈ 80. This highlights that
the morphology transitions are not necessarily discrete and may exist over a small range
of We. Below the limit of Wec,Bag, no breakup (NB) occurs. For Oh < 0.01, the values of
Wec are unaffected by the liquid viscosity (Hsiang & Faeth 1992).
913 A33-2
https://doi.org/10.1017/jfm.2021.7
 Published online by Cambridge University Press

<!-- PDF_PAGE: 3 -->

On aerodynamic droplet breakup
The overall breakup process of droplets can be subdivided into two basic phases: the
initiation phase (sometimes referred to as the deformation phase), and the breakup phase
which consists of the growth and breakup of the bags and rims (Pilch & Erdman 1987).
During the initiation phase, the droplet expands radially and ﬂattens until it forms a disk.
At some point, the disk becomes thin enough to be blown into one or more bags surrounded
by thick rims. The instant that the bags ﬁrst form is termed the ‘initiation time’. After the
initiation time, the bags grow until they break, causing the rims to break with them into
the child droplets. The dimensionless time, T (1.3), which is non-dimensionalized by the
characteristic deformation time, τ (1.4), is conventionally used for scalable analysis of
transient droplet
breakup
T = t
τ (1.3)
τ= d0
U
√ρl
ρg
. (1.4)
Conveniently, the characteristic deformation time deﬁned by Rimbert et al. (2020)i s
identical to the characteristic breakup time due to interfacial instabilities which are
commonly related to liquid breakup (Pilch & Erdman 1987) and thus can be used to
non-dimensionalize many droplet breakup analyses.
Numerical simulations of droplet breakup have been able to provide reasonable
qualitative agreement with experiments, mainly with respect to breakup morphologies;
however, quantitative agreement in the breakup phase is still lacking. One of the key
limitations of these numerical simulations is
mesh-induced breakup, which occurs when
the mesh size is not ﬁne enough to resolve micro-scale phenomenon. A ﬁner grid is
often not feasible due to the computational cost. This causes the simulations to predict a
premature breakup of thin ﬂuid structures such as bags, limiting even qualitative agreement
near the breakup point (Strotos et al. 2016). Consequently, there is still a strong focus on
improving the methods to achieve better quantitative agreement (Strotos et al. 2016;X i a o ,
Dianat & McGuirk 2016). Nevertheless, many works seek to use numerical simulations
to learn more about the breakup process, particularly at high We near the transition of ST
to catastrophic breakup where the underlying physical mechanisms are largely disputed
(Jalaal & Mehravaran 2014; Meng & Colonius 2018; Dorschner et al. 2020).
While numerical simulation is a useful tool with increasing capability for studying
droplet breakup, analytical models are more desirable as they provide a clearer insight
into the important physical phenomena. Additionally, analytical models are better suited
for use in spray modelling where many thousands of droplets must be analysed. The
chief goal of these models is to predict the child droplet sizes resulting from the
breakup, however
, there is also interest in modelling the transitions between the breakup
morphologies. Previous analytical modelling attempts can be divided into three main
categories:
mass–spring–damper analogy models, instability models and internal ﬂow
models.
Mass–spring–damper analogy models assume that the droplet acts as a mass–spring–
damper system, simplifying the problem to a one-dimensional (1-D)e q u a t i o nt h a ti ss o l v e d
analytically. The most well known of these models is the Taylor analogy breakup (TAB)
model (O’Rourke & Amsden 1987). In these analyses, the restoring force of surface tension
acts as the spring and viscosity as the damper to the aerodynamic forces of the gas ﬂow.
The breakup of the droplet is predicted to occur when a critical deformation is attained
(d/d
0 = 1.5 for TAB), where the drop then fragments such that the deformation energy
is transformed to the surface energy of the child droplets. In modelling the breakup in
913 A33-3
https://doi.org/10.1017/jfm.2021.7
 Published online by Cambridge University Press

<!-- PDF_PAGE: 4 -->

I.M. Jackiw and N. Ashgriz
this way, the approach neglects the complex physics of the breakup phase. A signiﬁcant
limitation of the TAB model is that several empirical constants are required to give a
complete prediction of the deformation and breakup sizes. Several improvements on the
TAB model have been presented in the literature. The ‘
enhanced TAB model’ (Tanner
1997) modiﬁes the breakup mechanism to relate the child droplet size to the breakup time.
Park, Y oon & Hwang (2002) proposed an ‘improved TAB model’ where the effect of drag
on the deformation was considered and the breakup criterion was changed to be based on
the pressure distribution across the drop. A notable variant of the mass–spring–damper
model is the dynamic droplet breakup model (Ibrahim, Y ang & Przekwas 1993) which
models the deformation based on an energy approach, however ,L e e et al. (2012)ﬁ n dt h a t
the model’s prediction is inaccurate. Although these models are commonly implemented
in industrial ﬂuid dynamics software for low We breakup (ANSYS Inc. 2011), the original
works are mostly compared against a very small data set from Krzeczkowski (1980), which
has poor temporal and spatial resolution compared to what is possible with current ﬂow
visualization technologies. Furthermore, these models have poor prediction near Wec,Bag
and neglect the various breakup morphologies and the presence of rim and bag geometries
in the breakup.
Instability models apply surface instability theories, mainly the Rayleigh–Taylor inertial
instability, to the face of a ﬂattened droplet. Notable examples of these works include
Harper, Grube & Chang ( 1972), Liu, Mather & Reitz ( 1993), Joseph, Beavers & Funada
(2002), Theofanous, Li & Dinh ( 2004) and Zhao et al. (2010). In these analyses, the
instability is related to the breakup mechanism by the number of wavelengths, λ,o ft h e
most unstable surface wave that ﬁt on the face of the ﬂattened drop of diameter d. NB, Bag,
BS and MB breakup are supposed to occur at λ/d < 1, 1 < λ/d < 2, 2 < λ/d < 3 and
λ/d > 3, respectively (Zhao et al. 2010). For these analyses, it is necessary to determine
d, which is most often taken from empirical correlations such as Hsiang & Faeth ( 1992),
although the mass–spring–damper deformation models described above have also been
used as in Liu et al. (1993). Even in the cases where the deformation models are used
in the prediction, the instability theories largely disregard the importance of the ﬂow
dynamics prior to the formation of the ﬂattened disk as they are only concerned with
determining its critical size. Additionally, in order to determine λ, the acceleration of the
droplet must be found based on the drag coefﬁcient of the droplet, C
d, which changes
throughout the deformation. As a result, an additional assumption must be made about
Cd, which is taken either from empirical correlations, the limiting disk geometry (Zhao
et al. 2011a), or by linear interpolation between a sphere and disk (Liu et al. 1993), which
cyclically depends on the deformation. In the majority of these analyses, the instability
theories were developed for inﬁnite planes of semi-inﬁnite thickness while the droplets
themselves are ﬁnite planes of ﬁnite thickness, bringing into question the validity of their
use. While the ﬁnite-thickness problem has been studied by Keller & Kolodner ( 1954)a n d
implemented by Jain et al. (2015), the effect of the ﬁnite boundary of the droplet periphery
on the instability has not been considered. Since the droplet periphery is of the same order
of magnitude as the instability wavelength, it is plausible that the droplet periphery has a
signiﬁcant effect on the nature of the instability. Although this method has been found to
provide reasonable prediction of We
c for the Bag, BS and MB morphologies, the omittance
of these properties brings into question its applicability to the problem as noted by Jain
et al. (2015). Additionally, the instability theory has not been shown to be able to predict
the relevant geometries of low We breakup such as the rims, or the child droplet sizes that
result from their breakup. Despite these shortcomings, surface instabilities are currently
the prevailing theory in the literature for the dynamics of low We droplet breakup.
913 A33-4
https://doi.org/10.1017/jfm.2021.7
 Published online by Cambridge University Press

<!-- PDF_PAGE: 5 -->

On aerodynamic droplet breakup
The internal ﬂow mechanism suggests that the drop deformation results from the ﬂow
of liquid from the poles of the drop to its equator. The resistance due to surface tension
at the equator then causes the formation of the rim. When the liquid ﬂow becomes strong
enough to resist the surface tension, the equator will thin indeﬁnitely and be susceptible
to being drawn downstream, leading to the ST morphology. Although this mechanism was
ﬁrst qualitatively described by Guildenbecheret al. (2009)i na ne f f o r tt op r o v i d eap h y s i c a l
explanation of the transition to ST, no quantitative analysis was given. Villermaux & Bossa
(2009) modelled the internal ﬂow of a drop in the bag breakup regime by solving the
axisymmetric Euler equation for the 1-D radial ﬂow in the drop due to a stagnation-point
ﬂow on its windward face. This internal ﬂow gave the initial deformation of the drop’s
equator, which was linked to the thinning of the droplet and thus to the growth of the bag
by a force balance. The result is a 1-D equation that can be solved numerically to predict the
deformation of the droplet and the growth of the bag. Although good agreement is shown
for the bag growth model to the small data set presented in Villermaux & Bossa (2009), the
model is limited in that it does not directly relate the droplet deformation and bag growth
phases to the droplet breakup and is applicable only for the Bag morphology. Although
Villermaux & Bossa ( 2009) provide a child droplet size prediction, it is essentially a ﬁt of
a
gamma distribution to breakup size data and neglects the deformation component of the
model. Kulkarni & Sojka ( 2014) carried out the same analysis including viscous effects
in the deformation and surface tension effects in the bag growth portions of the model,
however, these effects were negligible for their experimental range (note that an error
in this model was corrected by Stefanitsis et al. 2019). The model of Kulkarni & Sojka
(2014) provides poor prediction near Wec,Bag = 12, where their model transitions from an
oscillatory solution to one of inﬁnite growth. Mashayek & Ashgriz ( 2009) modelled the
deformation of the droplet surface using the 2-D axisymmetric Navier–Stokes equations.
The pressure distribution on the drop surface was provided using a perturbation analysis
about a trivial zeroth-order solution based on the drag coefﬁcient of a sphere. This method
gives a prediction of the 2-D drop topology which better represents the actual droplet
shape throughout the deformation. Although these models used the internal ﬂow theory
to describe the dynamics of droplet deformation, none were able to link this phase to the
breakup sizes or morphology. Furthermore, the models were only compared against a very
limited dataset within a narrow range of We. Consequently, the internal ﬂow mechanism
has not yet been widely adopted.
Although there have been many attempts to model the breakup of droplets, no analytical
model has been developed that describes and predicts both the breakup morphology
and the child droplet sizes for a wide range of conditions. Models which are capable
of predicting the droplet breakup size can only do so within limited ranges, give poor
prediction near We
c,Bag, and capture neither the effects of breakup morphology nor their
transitions. Conversely, models which predict the breakup morphology are not able to
predict the child droplet sizes from breakup.
The internal ﬂow mechanism is the least-studied theory for the breakup of droplets
and has the greatest potential to give a physically accurate description of the breakup
process. Since this modelling approach relies upon the Navier–Stokes equations, it is not
as constrained as the previous methods to rigid geometric assumptions. Furthermore, this
theory relates the deformation and breakup phases, which in previous works have been
considered to be essentially independent. Therefore, there is signiﬁcant opportunity in this
modelling approach to introduce new concepts that may provide a possible description
both for the child droplet size and the breakup morphology. For this reason, internal ﬂow
modelling is the focus of the present work.
913 A33-5
https://doi.org/10.1017/jfm.2021.7
 Published online by Cambridge University Press

<!-- PDF_PAGE: 6 -->

I.M. Jackiw and N. Ashgriz
2. Experimentation
One of the main challenges in modelling droplet deformation and breakup is the
acquisition of high-quality data, having high temporal and spatial resolution of the process.
Since conventional droplet breakup experiments rely on dropping the droplet across a
high-speed air ﬂow, a very large ﬁeld of view is required in order to capture the droplet
through its trajectory. Such a large ﬁeld of view limits the spatial resolution of the imaging
system. Additionally, high-speed cameras often reduce their effective resolution in order
to achieve high frame rates (above 7 kHz), further exasperating the issue of capturing
these high-speed events in useful detail. Therefore, for the present study, an experimental
apparatus was devised where the droplet is initially held stationary in order to remove the
cross-stream movement of the droplet typical in other experiments. This method allows
the imaging system to be framed tighter to the droplet throughout its breakup while still
achieving both sufﬁcient frame rates to resolve the dynamics of the process and sufﬁcient
spatial resolution to quantify the breakup of the rim.
The present experimental apparatus uses a solenoid valve to suddenly expose a pendant
drop suspended from a thin needle to a high-speed air stream. With this method, the
high-speed video may be framed tighter to the drop allowing higher magniﬁcation than
if the drops fell through a continuous air jet since the falling component of the droplets’
trajectories is negligible and the initial position of the droplet is very well deﬁned. This
also allows the high frame rates which limit the effective ﬁeld of view and resolution of
the camera to be used. An additional advantage of this method is that it is simpler to set
up and less expensive than the previous shock tube or continuous air jet studies, requiring
no specialized components or facilities other than the high-speed camera.
The main drawback of this method is the presence of the needle that suspends the drop,
which can interfere with its deformation. For high We cases, the needle interferes with
the top of the droplet and impedes ideal azimuthal symmetry, however
, the rest of the
droplet appears unaffected. For this reason, the breakup measurements are primarily taken
from the lower half of the drop. The adhesion of the drop to the suspending needle can
result in the formation of a liquid bridge between the drop and needle, which can affect
the later stages of the breakup. This is most signiﬁcant for high-viscosity ﬂuids where
the bridge is less easily broken by capillarity, but does not appear to signiﬁcantly affect
the low viscosity drops in the present work, which detach from the needle early on in the
breakup. A more detailed discussion of the effect of the suspending needle is provided in
appendix A. Despite the presence of the needle, the present experiments are found to agree
well with previous studies (see appendix B).
A schematic of the experimental apparatus used in this study is shown in ﬁgure 2. The
air is supplied via the building’s compressed air system at 100 PSI and is emitted as a
jet from a gauge 5 needle (inner diameter 5.7 mm) 60 mm in length. A needle valve at
the inlet of the rotameter is used to set the
steady-state ﬂow rate of the air jet. The ﬂow
conditions of the jet are maintained such that the issuing air jet is subsonic. Rotameter
and pressure transducer measurements are used to calculate the
air-ﬂow ﬁeld, as described
in § 2.2. The 30 gauge needle (outer diameter 0.305 mm) was fed by a syringe pump
(SyringePump.com NE-1000) to produce and suspend pendant drops close to the tip of the
air needle. The liquid used for the droplets was water with ρ
l = 1000 kg m− 3 and μl = 1.0
mPa s. The air jet was assumed to be at atmospheric conditions, with ρg = 1.2k gm 3. The
surface tension, σ, between the water and air interface was taken as 0.0729 N m − 1.A tt h e
start of the experiment, the solenoid immediately upstream of the air needle is opened,
suddenly forming an air jet
in line with the pendant drops.
High-speed shadowgraphy video of the droplets’ deformation in time as viewed
from the side was captured for 96 experimental conditions. Droplets having an initial
913 A33-6
https://doi.org/10.1017/jfm.2021.7
 Published online by Cambridge University Press

<!-- PDF_PAGE: 7 -->

On aerodynamic droplet breakup
Needle
valve
Building supply
(100 PSI)
5 gauge
air needle
22/30 gauge
drop needle
Rotameter Syringe pump
P
S
Figure 2. Diagram of experimental apparatus. Dashed box shows ﬁeld of view of camera.
Liquid needle We Frame rate (kHz) Shutter speed (ms)
22 7.3–12.4 7 1/30
11.3–36 15 1/79
30 7.6–28 20 1/91
40–167 42 1/89
152 50 1/99
133–200 60 1/150
Table 1. Camera settings.
diameter, d0, of 1.9 mm with a standard deviation of 0.2 mm were generated and exposed
to an air jet having a centreline (CL) gas velocity, ug,CL, ranging from 16.7 to 78.4 m s− 1.
Thus, Oh for these experiments was 0.0027, and the range of We was 7.3–200. In addition
to these experiments, 40 tests were run to capture the ’end-on’ view of the droplets
described in § 2.1. The purpose of these experiments was primarily to provide a better
visualization of the different breakup morphologies, thus fewer tests were run.
2.1. High-speed shadowgraphy and deformation measurement
Shadowgraph images of the droplets were captured using a high-speed camera (Photron
Fastcam SA-5 1000K-M3) with backlighting provided by a constant-source ﬂoodlight
(Dedolight DLHM4-300U). The settings at which the camera were operated were varied
based on the requirements for each set of ﬂow conditions and are tabulated in table 1. The
lenses used provided spatial resolutions of approximately 0.0431 and 0.0390 mm pixel
− 1
for the ‘side-view’ and ‘end-on’ sets, respectively. This was determined by comparing
measurements of both the droplet and air jet needle outer diameters with measurements
of each from the images where both were found to give the same value within the error of
detecting the edges in the image ( ≈ 1 pixel per edge).
T wo independent sets of high-speed shadowgraphy video were captured: the
side view
conventionally shown in similar experiments, and an end-on view. The end-on view has
been shown previously for low viewing angles ( <30
◦ to the side view) and primarily for
the ST and catastrophic regimes by Theofanous et al. (2012)a n da t<45◦ for the BS regime
by Zhao et al. (2013), but has not been published before to the authors’ knowledge for high
913 A33-7
https://doi.org/10.1017/jfm.2021.7
 Published online by Cambridge University Press

<!-- PDF_PAGE: 8 -->

I.M. Jackiw and N. Ashgriz
d0 = 2.3 mm
T0, We = 16.2
d0 = 2.3 mm
T0, We = 15.9
Ti = 0.886 (2.9 ms) Ti = 0.887 (2.8 ms)
Camera
(a)( b)
(c)
Air-flow
Air-flow
Camera
30º
Figure 3. Example shadowgraphy images showing side view ( a) and end-on view ( b). The top row shows
the initial undeformed droplet, while the bottom row shows the deformed droplets at the initiation time, Ti.
(c) Illustrates the camera’s alignment to the air ﬂow for the side-view (top) and end-on (bottom) cases.
viewing angles or the other morphologies of breakup. The side-view set facilitated the
measurement of the cross-stream (CS) and streamwise (SW) deformation of the droplets
in time as has been done by others, while the end-on images allowed for an additional
visualization of the deformation process. For the side-view experiments, the droplets were
held <1 mm from the air-needle tip, with the line-of-sight of the camera at a 90 ◦ angle
to the jet centreline. For the end-on-view experiments, the line-of-sight of the camera was
adjusted to approximately 30◦ from the jet centreline such that the jet was directed towards
the camera. In this case, the droplets were suspended approximately 10 mm from the tip
of the air needle to allow backlighting of the droplet as the air needle would otherwise
interfere. Examples of the images taken from the side and end-on views are shown in
ﬁgure 3.
To ﬁnd the CS and SW deformation of the droplets in time, the extents of the leeward,
windward,
top and bottom of the drop were identiﬁed for each frame of the video from
the side-on experimental set. Image processing was carried out using an in-house Python
code. The shadowgraph contour of the droplet was found using Canny edge detection in
Python’s scikit-image package. For the leeward,
top and bottom extents of the droplet, the
image was scanned from the outer edge of the image towards the droplet contour until the
x-y location of each extent was found. The irregularity of the windward side of the drop in
the late stages of the deformation makes the deﬁnition of the windward extent difﬁcult. To
make the measurement more consistent within each test, the windward extent is found by
tracing straight across the droplet from the leeward extent. Example results of this method
are shown in ﬁgure 4. The SW dimension is then found as the difference in the x locations
of the leeward and windward extents, while the CS dimension is found as the difference
in the y locations of the top and bottom extents. Figure 5 shows an example of the CS and
SW measurement for We = 13. This method has been found to identify the edges of the
droplets within ±1p i x e l(±0.04 mm).
2.2. Flow measurement
Since the instantaneous
air-ﬂow rate is difﬁcult to measure when the solenoid is ﬁrst
opened, the steady-state air ﬂow was measured and used to characterize the ﬂow.
The air-ﬂow rate was measured using a gas-ﬂow rotameter (Matheson FM 1050 E700
913 A33-8
https://doi.org/10.1017/jfm.2021.7
 Published online by Cambridge University Press

<!-- PDF_PAGE: 9 -->

On aerodynamic droplet breakup
Top
Bottom
Leeward
Windward
Figure 4. Example of the deformation measurement for We ≈ 13.
0.5 1.0 1.5 2.0
Time : T=t / τ
0
1
2
3
4
Deformation : L/d0
CS
SW
Ti
CS
SW
Figure 5. Droplet deformation in time for SW and CS directions for We = 13. Insets show measurement axes
(top) and images of the droplet at the approximate deformation times. The initiation time corresponds to the
point at which the droplet has reached its minimal streamwise deformation. Every fourth data point is plotted
for clarity.
for ﬂow rates 13.75 –30 l.p.m., Cole Parmer 03217-34 for ﬂow rates 30–68 l.p.m.) and a
pressure transducer (WIKA A-10). The measured standard air-ﬂow rate was corrected to
real conditions following the manufacturer’s recommended method. The volumetric ﬂow
rate of the jet issuing from the air needle at atmospheric temperature and pressure, Qjet,
was then found by mass conservation and used to solve for the average velocity of the jet
issuing from the air needle by Uave = Qjet/Ag where Ag is the outlet ﬂow area of the gas
jet.
The centreline (CL) velocity of the jet, UCL, which is used as the characteristic gas
speed, U, was found by assuming that the velocity proﬁle of the ﬂow in the needle
follows the power law velocity proﬁle,UCL = Uave(n + 1)(2n + 1)/2n2,w i t hn =− 1.7 +
1.8l o gReCL (Pritchard & Leylegian 2011). The value of the power law exponent n
was found iteratively, using Reave as an initial guess for ReCL. It should be noted that
this equation is valid for ReCL > 20 000 ( n > 6) and that in the present study ReCL =
5200–25 000 (5 < n < 6.2), however, good agreement in We transitions and in various
deformation measurements between previous works and the present experiments suggest
that the approximation holds (see appendix B).
913 A33-9
https://doi.org/10.1017/jfm.2021.7
 Published online by Cambridge University Press

<!-- PDF_PAGE: 10 -->

I.M. Jackiw and N. Ashgriz
For the side-view cases, the pendant drop was positioned close enough to the air needle
that the air jet in the vicinity of the deforming drop is in the near-ﬁeld region, thus the
centreline velocity of the jet does not change downstream (Schlichting & Gersten 2017).
As in previous experiments, it was assumed that the upstream air-ﬂow ﬁeld is unaffected
by the presence of the drop (for example, Flock et al. 2012). Therefore, UCL is the
characteristic air-ﬂow velocity near the drop, U. This was also assumed for the end-on
view experiments where the drop is farther from the nozzle tip, however , it is likely that
the predicted velocities are high as the average velocity in the vicinity of the drop will be
lower than when the drop is closer to the nozzle exit where the velocity proﬁle near the
centreline is ﬂatter. For this reason, the end-on view experiments were used primarily for
qualitative description of the process. The few quantitative measurements that were taken
from the end-on views are indicated separately from the side-view experiments.
3. Initiation topology and breakup morphologies
The initiation period of the breakup describes the time over which the initial deformation
of the droplet occurs. The initiation period ends at the onset of the breakup at the initiation
time, T
i,d e ﬁ n e db yF l o c ket al. (2012) as the time at which the minimal thickness of
the droplet is achieved. This can be found from measurements of the side-view images
as shown in ﬁgure 5 . Previous analyses assumed that the droplet deforms symmetrically
about its equator until it forms a uniformly ﬂattened pancake shape at Ti.H o w e v e r ,t h e
present images, as well as those of Flock et al. (2012), Kulkarni & Sojka ( 2014)a n dt h e
theoretical model of Mashayek & Ashgriz ( 2009), show that this is not the case.
The side-view images show that initially only the windward face of the droplet deforms.
During this ﬁrst phase, the leeward half of the droplet is largely unaffected and no
signiﬁcant radial expansion is apparent. Once the windward face has ﬂattened, it forms
a disk which expands at a constant rate as it moves across and absorbs the leeward half
of the drop. These stages are evident in ﬁgure 5. Although this constant growth rate was
observed and characterized empirically by Hsiang & Faeth (1992) and can be seen in some
numerical simulations such as Stefanitsis et al. (2019), previous analytical models such as
O’Rourke & Amsden (1987) and Villermaux & Bossa ( 2009) have predicted non-constant
CS deformation rate. This is likely the result of a low
frame rate being used which does
not clearly reveal the constant growth rate.
The end-on-view images show that at some point a rim forms around the periphery of
the disk and draws the centre of the disk into a thinning sheet. This thinning sheet is more
susceptible to the air ﬂow and is the part of the drop that blows out into bags. At higher
We,s u c ha si nB S ,
MB and ST morphologies, the rim forms before all of the droplet has
deformed and an undeformed core remains at the centre of the thinned membrane. The
rim,
sheet and undeformed core are highlighted in ﬁgure 6. From the present experiments,
it is proposed that the breakup phase actually begins at the instant that the rim forms, as
this signiﬁes the transition of the governing mechanisms from the uniform expansion of
the windward disk to the thinning and
blowout of the interior that becomes the bag. This
rim formation and undeformed core are also apparent in the numerical simulations of Jain
et al. (2015), which show thickness modulations in the droplet proﬁle at these locations.
If no undeformed core remains when the rim forms, the initiated structure comprises
only of the rim and sheet. Since the sheet is only restricted at its periphery, it forms a
single large bag when blown downstream. This condition describes Bag breakup and is
shown in supplementary movies 1 and 2 available at https://doi.org/10.1017/jfm.2021.7
and in ﬁgure 7 . At higher We, the rim forms earlier in the deformation and the sheet is
blown out while an undeformed core of the droplet remains. As We increases, so does the
913 A33-10
https://doi.org/10.1017/jfm.2021.7
 Published online by Cambridge University Press

<!-- PDF_PAGE: 11 -->

On aerodynamic droplet breakup
1
(a)( b)
2
3
d0 = 2.49 mm, We = 22.5
Ti = 0.832 (2.5 ms)
1 2
3
d0 = 1.91 mm, We = 69.1
Ti = 0.68 (0.8 ms)
Figure 6. Images of the structures formed at the end of the initiation period for BS ( a) and MB
(b) morphologies, showing the rolled rim (1), thinned sheet (2) and core (3).
d0 = 1.88 mm
We =1 1
 T = 0.452
(1.3 ms)
Ti = 0.921
(2.65 ms) T = 2.224 (6.4 ms)T0
d0 = 1.69 mm
We = 11.9 T = 0.445
(1.05 ms)
Ti = 0.910
(2.15 ms) T = 2.139 (5.05 ms)T0
(b)
(a)
Figure 7. ( a) Bag breakup sequence from side- (top) and end-on (bottom) views. See movie 1 ( side view) and
movie 2 (end-on view). ( b) Illustration of droplet geometry at Ti (left) and of breakup morphology (right) for
bag breakup. The windward disk is composed of the cross-hatched rim and the white area.
amount of the drop that remains in the undeformed core. The undeformed core, like the
rim, is less susceptible to forces of the air ﬂow and the sheet is blown out between the
undeformed core and the rim.
When the undeformed core is relatively small, the sheet forms a large bag that is pinched
at its centre, which draws out the undeformed core to form the stamen. It is possible that
during the formation of the stamen, air bubbles may be trapped as the navel of the bag
pinches closed behind the stamen. The stamen size grows as the volume of the undeformed
core increases with We. The resulting breakup morphology in this case is BS and is shown
i nm o v i e s3a n d4a n di n ﬁgure 8 . Similar thickness modulations are also seen in the
numerical simulations of Y ang et al. (2017).
913 A33-11
https://doi.org/10.1017/jfm.2021.7
 Published online by Cambridge University Press

<!-- PDF_PAGE: 12 -->

I.M. Jackiw and N. Ashgriz
T = 1.978 (3.7 ms)
T = 1.99 (6.1 ms)Ti = 0.816
(2.65 ms)
Ti = 0.408
(1.25 ms)T0
Ti = 0.829
(1.55 ms)
Ti = 0.401
(0.75 ms)T0
d0 = 2.49 mm, We = 22.5
d0 = 1.79 mm, We = 22.5 (b)
(a)
Figure 8. ( a) BS breakup sequence from side (top) and end-on (bottom) views. See movie 3 ( side view) and
movie 4 (end-on view). ( b) Illustration of droplet geometry at Ti (left) and of breakup morphology (right) for
BS breakup. The windward disk is composed of the cross-hatched rim and the white area, while the undeformed
core is marked by the grey-ﬁlled area.
Near the transition of Bag and BS breakup, evidence of a very small undeformed core
can be seen that only mildly affects the growth of the bag and can form a slight dimple
at the pole rather than a full stamen ( ﬁgure 9 ). This shows the continuous nature of the
transition between the Bag and BS breakup morphologies and how the stamen size changes
with We. This suggests that the topography of the bag thickness depends on the initiated
structure with radial modulations in thickness. This is important in modelling the breakup
of the bag as it is assumed to break ﬁrst at its thinnest point. By comparison, current
models assume a uniform thickness or that the bag is thinnest at its centre.
When the undeformed core is large, the distance between the core and rim is small
relative to the circumference of the rim. Owing to surface tension, a symmetric curvature
is preferred in the bags, and thus multiple bags form along the azimuthal direction of
the sheet. Unlike in BS breakup, the undeformed core in this case is large enough to
continue being deformed and can breakup further as either an additional single bag or as
consecutive waves of multiple bags (movies 5–6 and 7–8 and ﬁgure 10(top) and (bottom),
respectively). The formation of the ﬁrst set of bags as well as these two outcomes are
illustrated in ﬁgure 11. Since multiple bags are formed azimuthally and multiple sequences
of the breakup occur, this condition leads to MB breakup. This repeated breakup of the
periphery was also seen in the experiments and numerical simulations of Dorschner et al.
(2020), who noted that this results in a periphery which appears to be ‘ﬂapping’.
Near the transition of BS and MB, the remaining core may be too small to break
further, but the width of the thinned sheet relative to its radius may be enough to form
multiple bags, usually two, as shown in ﬁgure 12 . Some have referred to this as a
distinct morphology called ‘
twin-bag’, while others have grouped it either with BS or MB
morphologies. The explanation of these breakup modes by the surface instability theory
913 A33-12
https://doi.org/10.1017/jfm.2021.7
 Published online by Cambridge University Press

<!-- PDF_PAGE: 13 -->

On aerodynamic droplet breakup
d0 = 2.04 mm
We = 14.2
T = 1.710 (4.9 ms) T = 2.128 (6.1 ms)
Figure 9. Side view showing the dimple formed at the tip of the bag near the transition from Bag to BS
breakup.
(a) (b)
T = 1.952 (1.733 ms)T = 1.314 (1.167 ms)
Ti = 0.601
(0.533 ms)
T = 2.261 (2.967 ms)T = 1.626 (2.133 ms)
Ti = 0.635
(0.833 ms)
T = 1.581
(1.952 ms)
T = 2.043
(2.524 ms)
T = 1.824
(2.905 ms)
T = 2.451
(3.905 ms)
d0 = 2.13 mm, We ≈ 77d0 = 2.18 mm, We ≈ 180
d0 = 1.96 mm, We ≈ 40.7d0 = 1.74 mm, We ≈ 47.4
Figure 10. ( a) End-on and (b) side-view images of MB breakup showing the condition at which the remaining
core breaks into one bag (top), and by repeated MB (bottom). See movies 5 and 6 (core breakup as single bag,
side and end-on view, respectively), and movies 7 and 8 (core breakup as multiple bags, side and end-on view,
respectively).
does not capture this ‘ twin-bag’ behaviour, as the two stable wavelengths required for
BS would also be required for two bags to form (i.e. it predicts the morphologies to be
identical). The explanation provided here allows for the existence of the ‘ twin-bags’ as a
subset of MB in which the remaining core does not break further and multiple bags ( two)
form azimuthally.
At higher We, the aerodynamic forces of the air stream are dominant over the radial
ﬂow of the droplet. When this occurs, the rim is pushed downstream around the leeward
face of the drop with a thin sheet that connects it to the undeformed core. The thin sheet
913 A33-13
https://doi.org/10.1017/jfm.2021.7
 Published online by Cambridge University Press

<!-- PDF_PAGE: 14 -->

I.M. Jackiw and N. Ashgriz
(a) (b) (c)
Figure 11. Illustration of MB bag formations, showing ( a) the initiation and blowout of the ﬁrst bag set, (b)t h e
initiation and blowout of the core as a single bag, which occurs at lower We,a n d( c) the initiation and blowout
of a second bag set from the core along with the blowout of the core itself as the ﬁnal bag. In ( a), the windward
disk is composed of the cross-hatched rim and the white area, while the undeformed core is marked by the
grey-ﬁlled area.
d0 = 1.96 mm
We = 26
T = 1.956 (3.9 ms)
d0 ≈ 2.05 mm
We ≈ 35.1
T ≈ 1.905 (3.5 ms)
(a)( b)
Figure 12. Images showing the twin-bag structure at side (a) and end-on ( b)v i e w s .
is susceptible to the low-pressure zone at the periphery of the drop and is blown out
radially with multiple bags formed azimuthally. This is shown in movies 9 and 10 and in
ﬁgure 13. The remaining core then breaks as MB which is consistent with the numerical
simulations of Dorschner et al. (2020). This breakup geometry resembles ST breakup, in
that the periphery of the drop is drafted downstream. However, the present images show
that instead of small droplets being stripped directly from the periphery of the drop, bag
and rim structures are formed similar to the other breakup morphologies. Although the
peripheral sheet has been observed in the numerical simulations of Jain et al. (2015)a n d
Meng & Colonius ( 2018), it is likely that this was not evident in previous experiments as
the exposures required to capture the fast-moving structures is very short and the frame rate
required to capture the radial
blowout event is very high. These settings were only easily
achieved with the present experimental set-up due to the ability to frame the video tightly
to the droplet throughout the breakup. Additionally, the radial bag formation has likely not
been seen in simulations due to mesh-induced breakup, which would prematurely ‘burst’
the bags before they are able to grow radially.
Figure 14 shows illustrations of the structures of the droplet at initiation ( T
i)a n dt h e i r
related breakup morphologies. These results highlight the importance of the geometry of
the droplet during its deformation in determining the breakup morphology. Furthermore,
the rims that form hold most of the droplet’s volume during the breakup, thus modelling
913 A33-14
https://doi.org/10.1017/jfm.2021.7
 Published online by Cambridge University Press

<!-- PDF_PAGE: 15 -->

On aerodynamic droplet breakup
T = 0.918 (0.7 ms), /Delta1T = 0.022 (0.017 ms)
d0 = 1.65 mm, We = 133.3
T = 0.602 (0.45 ms), /Delta1T = 0.067 (0.050 ms)
d0 = 2.25 mm, We = 280
(a)
(b)
Figure 13. Sequential images showing the radial bag blowout that occurs in the ST morphology with side (a)
and end-on ( b)v i e w s .T gives the time of the ﬁrst frame, while Δ T gives the incremental time between each
frame. Time moves forward from left to right. Note that the end-on view is at a lower frame rate, which was
required in order to capture the necessary ﬁeld of view. See movie 9 (
side view) and movie 10 (end on).
(a) (b) (c)( d)
Figure 14. Illustration of droplet at Ti (left) and of breakup morphology (right) for ( a)B a g ,(b)B S ,( c) MB
and ( d) ST morphologies. The rim is marked by cross-hatching while the undeformed core is marked by the
grey-ﬁlled area. The initiation disk is composed of the rim and the white area.
the rim dimensions at breakup is integral to determining the resultant breakup sizes of the
drop. This is true even for cases with an undeformed core, as the core continues to deform
and forms additional rim-bag structures until it is fully disintegrated.
Since the simple ellipsoidal geometry that is assumed in previous analyses does not
capture the rim, sheet and undeformed core features, these analyses cannot be expected to
accurately model the transition between droplet deformation and breakup. Consequently,
these models would have limited ability to predict breakup morphology and child droplet
size. It is therefore necessary to develop a model which describes the formation of these
structures, capturing the dimensions of the windward disk and of the rim at the instant of
its formation which can be used to determine the volume that remains in the undeformed
core. These geometries can then be used to determine the breakup sizes of the droplet and
the breakup morphology.
4. Modelling droplet deformation and breakup
The windward disk from which the rim forms is the result of liquid ﬂowing from the
windward pole of the drop to its equator during the initiation period. The stable thickness
of this disk balances the air pressure outside the droplet and the dynamic pressure inside
the droplet, which results from the disk’s constant deformation rate, via the Laplace
pressure jump across the periphery. When the deformation persists past this point, the
periphery of the windward disk forms a rim of the same thickness while the inner
portion of the disk thins. The relationship between the windward disk and undeformed
core volumes at this point dictates the breakup morphology. After this initiation period,
913 A33-15
https://doi.org/10.1017/jfm.2021.7
 Published online by Cambridge University Press

<!-- PDF_PAGE: 16 -->

I.M. Jackiw and N. Ashgriz
InitiationBreakup
2. Rim formation and morphology
prediction
• Rim forms at periphery of WW disk
 Morphology determined by volume
in undeformed core
1.Droplet deformation
 Radial expansion of WW disk
3. Bag blowout, rim expansion and
thinning
 Final rim size related to bag size
through morphology
4. Rim breakup
Figure 15. Flowchart of the present modelling methodology.
ℎ( t)ℎ ( t)
r
z
R (t)
(a)( b)( c)
2R (t)
Figure 16. Illustrations of ( a) the coordinate system of the present analysis, ( b) the actual droplet shape
during the balancing period and ( c) the approximated ellipsoidal geometry during the balancing period.
the breakup period begins as the thinned portion of the windward disk is blown into one
or more bags depending on the morphology, causing the rim to radially expand and thin
until the bag ruptures which sets off the breakup of the rim. A ﬂowchart of this modelling
methodology is given in ﬁgure 15.
Thus, the ﬁrst aim is to model the internal ﬂow of the droplet, forced by the air ﬂow
around it, to determine the constant deformation rate. The constant deformation rate will
then be used to determine the rim thickness at its formation and, by extension, the breakup
morphology. Finally, the growth and breakup of the bag and rim will be modelled to predict
the average child droplet sizes from the breakup of the rims, which contain the majority of
the droplet volume.
4.1. Internal ﬂow
The modelling of the internal droplet ﬂow ﬁrst carried out by Villermaux & Bossa
(2009) is replicated in this section for completeness of the present analysis. However,
no assumptions about the shape of the droplet will be made that constrain the surface
curvatures in the present section as to allow for greater generality of the resulting equation.
These assumptions will be left to later sections. The coordinate system used in the present
analysis is illustrated in ﬁgure 16(a).
913 A33-16
https://doi.org/10.1017/jfm.2021.7
 Published online by Cambridge University Press

<!-- PDF_PAGE: 17 -->

On aerodynamic droplet breakup
The liquid ﬂow ﬁeld inside the drop is found using the Navier–Stokes and conservation
of mass equations in cylindrical coordinates for incompressible, axisymmetric radial ﬂow,
ρl
(∂ur
∂t + ur
∂ur
∂r
)
=− ∂pl
∂r + μl
[1
r
∂
∂r
(
r∂ur
∂r
)
− ur
r2
]
, (4.1)
r∂h
∂t + ∂(rurh)
∂r = 0, (4.2)
where pl(r) is the radial pressure distribution inside the drop and h = h(t) is the SW
thickness of the drop as it ﬂattens.
Deﬁning the droplet’s CS radius as R = R(t) and assuming that its volume is
proportional to R2h (true for either ellipsoidal or cylindrical geometries), ( 4.2)g i v e st h e
radial velocity proﬁle inside the drop as ur(r) = r˙R/R. Upon substitution into ( 4.1), the
viscous terms cancel. Integrating over R leads to (4.3).
R¨R = 2
ρl
( pl(0) − pl(R)) . (4.3)
The liquid pressure inside the drop is related to the surrounding air pressure by the
Laplace pressure at the interface and is given by ( 4.4) where σ is the interfacial surface
tension and κ is the local surface curvature.
pl(r) = pg(r) + σκ. (4.4)
The air-ﬂow ﬁeld is approximated as an inviscid stagnation-point ﬂow against a plane
at the windward pole of the drop with the axial component of the air velocity given by
Uz =− azU/d0, where U is the free-ﬁeld air-ﬂow speed, z is the axial direction measured
from the windward pole of the droplet and a is the stretching rate of the air ﬂow (i.e.
the spacing between the streamlines of the ﬂow). Here, a essentially relaxes the planar
stagnation-point ﬂow assumption to approximate the windward droplet face topology. The
limiting shapes of the deformation process are the initial sphere and a ﬁnal disk, which
correspond to a = 6a n dπ/4, respectively (Villermaux & Bossa 2009). The pressure ﬁeld
in r and z of the surrounding air ﬂow is found by conservation of mass and momentum
assuming inviscid, incompressible, quasi-steady and axisymmetric ﬂow, which is solved
at z = 0 to ﬁnd the pressure at the windward face of the drop given by ( 4.5).
pg(r) = pg(0) − ρg
a2U2
8d2
0
r2. (4.5)
Substituting (4.4)a n d( 4.5)i n t o(4.3) and non-dimensionalizing gives
¨R
R = 1
τ2
(a
2
)2
[
1 − 8
a2We
(κp − κw)d3
0
R2
]
, (4.6)
where κp and κw are the curvatures at the periphery and windward pole of the drop,
respectively. It is clear from ( 4.6) that the deformation rate of the droplet depends on
its shape as it deforms as the aerodynamic forces depend on the stretching rate while
the surface tension forces depend upon the curvature at the windward face and periphery
of the drop, all of which change as the droplet deforms. In order to avoid the cyclical
argument that to solve the deformation of the droplet one must know the deformation of the
droplet, assumptions must be made to describe the droplet’s shape during the deformation
to determine the values of κ
p, κw and a.
913 A33-17
https://doi.org/10.1017/jfm.2021.7
 Published online by Cambridge University Press

<!-- PDF_PAGE: 18 -->

I.M. Jackiw and N. Ashgriz
1.6(a)( b) 1.10
1.05
1.00
0.95
0.90 CS, We = 9.6
SW
CS, We = 22.5
SW
0.85
0.80
1.4
1.2
1.0
0.8
0.6
Deformation : L/d0
0.4
0 0.2
Time : T = t/τ
Tbal = 1/8
0.4 0.6 0.8 0 0.05
Time : T = t/τ
0.10 0.15 0.20 0.25 0.30
Figure 17. ( a) CS and SW droplet deformation L/d0 vs. time T for We = 9.6( B a g )a n dWe = 22.5( B S )o v e r
the initiation period. ( b) Magniﬁcation of the region given by the box in (a). The constant SW deformation rate
occurs at Tbal ≈ 1/8 for both cases, indicated by the vertical dashed line.
Equation ( 4.6) is the most general form of the model for the internal liquid ﬂow of
a droplet in a high-speed air stream. Similar approaches have been taken by Villermaux
& Bossa ( 2009) and Kulkarni & Sojka ( 2014), however, these attempts did not predict
the constant radial growth rate that is found here. These analyses are discussed further in
appendix C.
4.2. Droplet deformation
Using the equations for the internal ﬂow of the droplet, the problem now turns to
determining the constant radial growth rate that is observed during the initiation period
of the breakup.
Upon inspection of ( 4.6), a constant radial growth rate would occur when the term in
square brackets becomes zero, i.e. the aerodynamic and surface tension forces balance.
This is expected as the deformation causes the droplet’s windward face to ﬂatten, thus
a decreases from 6 towards π/4 while κ
w tends towards zero as the windward face
ﬂattens and κp increases as the periphery thins, as illustrated in ﬁgure 16(b). This process
is described as ‘ﬂow balancing’ as the forces acting on the droplet change through
the deformation until they balance resulting in the constant growth rate ( ¨R = 0). This
description is consistent with the division of the deformation stage into two periods;
the initial windward pole ﬂattening period and the constant radial expansion period as
described in § 3.
The constant radial expansion rate is achieved once the ﬂows have balanced, which
occurs at the ﬂow balancing time, T
bal. Since the radial ﬂow near the pole at early T
does not greatly affect the ﬂow at the periphery of the drop where the CS deformation
measurement is taken, Tbal is deﬁned by the point at which the SW deformation becomes
approximately constant. From the present experiments, Tbal ≈ 1/8 appears to be a good
estimate as shown in ﬁgure 17 where the constant SW deformation rate begins at T ≈ 1/8.
In other words, Tbal is taken as the time at which the disk ﬁrst begins to form on the
windward face of the drop.
Initially, the droplet is spherical, therefore κw = κp and the surface tension
terms cancel. However, as the windward face ﬂattens, κw rapidly diminishes and
913 A33-18
https://doi.org/10.1017/jfm.2021.7
 Published online by Cambridge University Press

<!-- PDF_PAGE: 19 -->

On aerodynamic droplet breakup
101 Ellipsoid
Disk
Curvature ratio : κh/κθ
100
1.0 1.2 1.4
CS deformation : 2R/d0
1.6 1.8 2.0
Figure 18. Ratio of the thickness curvature to the azimuthal curvature vs. extent of deformation for ellipsoid
and disk geometries ( h/d0 = (d0/2R)2 and h/d0 = 2/3(d0/2R)2, respectively).
becomes negligible. The curvature of the periphery is composed of two curvatures:
the thickness curvature, κh = 2/h, and the azimuthal curvature, κθ = 1/R. In previous
analyses, κθ was neglected as it was assumed to be much smaller than κh (see appendix C).
However, this is not the case for the levels of deformation that occur up to Ti where
2R/d0 < 1.6, as shown in ﬁgure 18 where the ratio between the curvatures is less than
an order of magnitude for deformations less than 2 R/d0 ≈ 2. This is likely a signiﬁcant
reason that 2-D numerical simulations, which neglect this curvature, perform poorly
compared to their 3-D equivalents (Strotos et al. 2016). In ﬁgure 18 , h/d0 is found by
conservation of mass for both ellipsoidal and cylindrical geometries ( h/d0 = (d0/2R)2
and h/d0 = 2/3(d0/2R)2, respectively). The azimuthal curvature therefore cannot be
neglected in the analysis of the droplet deformation for T < Ti, including over Tbal.
Equation (4.6) is then,
¨R
R = 1
τ2
(a
2
)2
[
1 − 64
a2We
((d0
h
)( d0
2R
)2
+
( d0
2R
)3)]
. (4.7)
To ﬁnalize the deﬁnition of the curvatures, an assumption must be made about the
geometry of the droplet during the ﬂow balancing such that h and R can be related. It
is assumed that during the ﬂow balancing period the droplet can be approximated by an
ellipsoid as illustrated in ﬁgure 16(c) such that, by conservation of mass with the initially
spherical droplet, h/d0 = (d0/2R)2 (this assumption is discussed further in appendix C).
This simpliﬁes (4.7)t o 4.8, where the only remaining unknown is a
¨R
R = 1
τ2
(a
2
)2
[
1 − 64
a2We
(
1 +
( d0
2R
)3)]
, (4.8)
where a relates to the approximation of the ﬂow around the deforming object as a planar
stagnation-point ﬂow. While its limits are deﬁned as a = 6 for the initial sphere and a =
π/4 for a disk, the relationship between a and the extent of deformation (i.e. the path of a
from 6 to π/4) is unknown. While it is possible that a relationship between a and the shape
913 A33-19
https://doi.org/10.1017/jfm.2021.7
 Published online by Cambridge University Press

<!-- PDF_PAGE: 20 -->

I.M. Jackiw and N. Ashgriz
2.5(a)( b)
Pred. expansion rate : 2R/d0 (ms–1)
Exp. expansion rate : 2R/d0 (ms–1) Exp. expansion rate : 2 R/d0 (ms–1)
2.0
1.5
1.0
0.5
0
0.7
NB
Bag
BS
NB
Bag
BS
MB
ST
0.6
0.4
0.3
0.5
0.2
0.1
0
2.52.01.51.00.50 0.60.2 0.40
Figure 19. Comparison of predicted expansion rate from ( 4.9) to all experiments ( a) and to NB, Bag and BS
morphologies only (b). The box in ( a) shows the region that is magniﬁed in ( b).
of the droplet could be determined from numerical simulation or by highly detailed particle
image velocimetry (PIV) measurements, it will be assumed that the dominant value of a
over the deformation period is its initial value as this results in the highest ¨R during the
balancing period. Additionally, it is observed that the shape of the droplet as a whole is
more spherical than disk like during the balancing period. Thus, over the balancing period,
it is assumed that a takes a constant value of a = 6. The constant radial expansion rate is
then found by integrating ( 4.8) over the ﬂow balancing time. As described earlier in this
section, the CS dimension of the drop remains roughly constant during the ﬂow balancing,
thus R(T < Tbal) ≈ d0/2. This integration leads to ( 4.9)
˙R
d0/2 = 1
τ
(a
2
)2 (
1 − 128
a2We
)
Tbal. (4.9)
The prediction of ( 4.9) is compared to the experiments in ﬁgure 19, where the constant
radial growth rate is measured by performing a linear ﬁt to the cross-sectional diameter
measurements over the period 0 .25 < T < Ti for all cases. Good agreement between the
theory and experiments is found for Bag and BS breakup morphologies ( ﬁgure 19b). MB
and ST morphologies exhibit greater deviation due to the early breakup as described in § 3,
in particular the breakup of the liquid fragment at the top of the drop which results from
the suspending needle which becomes the windward most point of the drop which affects
the measurement as in § 2. This has a greater effect on the ﬁtting procedure as there are
fewer data points during the deformation phase which are undisturbed owing to the faster
progression of the deformation relative to the frame rate used.
Figure 20 compares the present deformation prediction as well as the previous
deformation models (the TAB model of O’Rourke & Amsden ( 1987) and the models of
Villermaux & Bossa 2009;K u l k a r n i&S o j k a2014) to the present experiments for a range
of We covering Bag and BS morphologies. Note that the present model does not rely on
exactly predicting the temporal deformation and instead focuses only on predicting the
constant deformation rate. As such, for ﬁgure 20 , the present model is plotted assuming
that the CS expansion ﬁrst passes the periphery of the drop at T ≈ 0.25, with the slope
given by ( 4.9). Excellent prediction of the present model is shown, while the previous
models show signiﬁcant deviation and indeed a misrepresentation of the constant trend.
913 A33-20
https://doi.org/10.1017/jfm.2021.7
 Published online by Cambridge University Press

<!-- PDF_PAGE: 21 -->

On aerodynamic droplet breakup
1.8(a)( b)
(c)( d)
CS
TAB
Villermaux (2009)
Kulkarni (2014)
Present
We = 10.9 (Bag)
We = 15.3 (BS) We = 24.4 (BS)
We = 14.2 (Bag)
1.6
1.4
1.2
CS deformation : 2R/d0
1.0
1.8
1.6
1.4
1.2
1.0
1.8
1.6
1.4
1.2
CS deformation : 2R/d0
1.0
1.8
1.6
1.4
1.2
1.0
0.80.60.40.20 0.80.60.40.20
0.80.60.40.2
Time : T = t/τ Time : T = t/τ
0 0.80.60.40.20
Figure 20. Comparison of TAB (O’Rourke & Amsden 1987), Villermaux & Bossa ( 2009) and Kulkarni &
Sojka (2014) models and ( 4.9)t o the CS measurement of the present experiments during initial deformation.
The present prediction also agrees with the numerical results of Jain et al. (2018), who
studied the effect of density ratio, ρ∗ = ρl/ρg, on the breakup. In their work, ˙R(T = 1) =
4.8, 2.0 and 0.8f o rρ∗ = 10, 150, and 1000, respectively, at We = 20. The corresponding
values using the present analysis are ˙R(T = 1) = 5.9, 1.5, and 0 .6. The prediction of the
present analysis is higher than that of Jain et al. (2018)a t ρ∗ = 10 as the resistance due
to the gas phase density on the expanding periphery is not accounted for. The present
prediction is lower for the other cases as the measurements of Jain et al. (2018)a r et a k e n
after Ti (Ti < 1), when the ﬂow dynamics begins to change, as will be described in § 4.4.
Chou & Faeth ( 1998) empirically found the growth rate to be 2 ˙R/d0 = 1.06 and 1 .22 for
their water experiments at We = 13 and 20, respectively (2 ˙R/d0τ= 0.5, with τ= 0.472
and 0.41 ms for We = 13 and 20, respectively). This result is low compared to the present
predictions of 1 .8a n d2 .26; however, several high-viscosity cases were included in the
results of Chou & Faeth ( 1998). Adjusting their analysis for their water experiments only
gives 2˙R/d0 = 1.31 and 1.95. These results agree relatively well with those of the present
study considering the much lower time resolution of Chou & Faeth ( 1998), which may
cause a higher uncertainty in the linear ﬁt.
913 A33-21
https://doi.org/10.1017/jfm.2021.7
 Published online by Cambridge University Press

<!-- PDF_PAGE: 22 -->

I.M. Jackiw and N. Ashgriz
d0
2Ri 2Ri 2Ri
hi hi hi
(a)( b)( c)( d)
Figure 21. Illustration of the ( a) initial droplet and the deformed droplet geometry at Ti for (b)B a g ,(c)B S ,(d)
MB and ST morphologies, indicating measurement locations of hi and Ri. The rim is marked by cross-hatching
while the undeformed core is marked by grey ﬁll.
4.3. Rim formation and prediction of initiation geometry
The majority of the child droplets that form from the breakup of the drops come from the
rim geometries described in § 3. Furthermore, the rim size can be used to ﬁnd the initiation
geometry in order to determine the breakup morphology. It is therefore necessary to predict
the rim size when it forms, which can be found by solving for the internal ﬂow inside the
windward disk.
As the droplet’s windward face expands radially, the disk that forms has thickness h.A t
the instant of initiation, the periphery of the disk ‘rolls’ as the surface tension pinches the
sides of the disk periphery to form a thick rim of major and minor diameters 2 R
i/d0 and
di ≈ hi, respectively. This geometry is illustrated for all breakup morphologies inﬁgure 21.
The pressure balance across the peripheral interface ( 4.4) can be used to ﬁnd hi, giving
(4.10)
di = hi =
[
1
4σ
(
ρl ˙R2 + ρa
(a
2
)2
U2
( Ri
d0
)2)
− 1
2Ri
]− 1
. (4.10)
While 2 Ri/d0 and hi both serve to balance the pressure across the interface, one must
be known in order to uniquely determine the other. At this time, the mechanism which
determines the unique values is unknown, therefore
, an assumption will be made for
2Ri/d0 based on the present experiments so that hi may be determined. Figure 22(a)s h o w s
the measured CS diameter of the droplets at Ti, which for all breakup modes is determined
from the average of the Bag and BS morphologies as 2 Ri/d0 ≈ 1.6. This value agrees
with the breakup criterion for the TAB model, 2 R/d0 = 1.5, as well as the experimental
ﬁndings of Zhao et al. (2011a), 2 R/d0 = 1.8, who used the older deﬁnition of Ti that
is slightly later than the deﬁnition presently used, resulting in a slightly higher value as
discussed in § 3.
In this late stage of deformation, a will satisfy the balancing of ( 4.3) for the initiated
geometry and is found to be a ≈ √ 80/We. This suggests a shift in dominance of the
aerodynamic forces over the inertia of the expanding rim when We > 80, which coincides
with the transition to the ST morphology as described by Guildenbecher et al. (2009).
This then gives that Wec,ST = 80, which agrees with the present experiments as well as
with Guildenbecher et al. (2009) and Zhao et al. (2010). Using these assumptions, ( 4.10)
simpliﬁes to
di
d0
= hi
d0
≈
[1
4
(ρl ˙R2d0
σ
)
+ 2.6
]− 1
= 4
(Werim + 10.4), (4.11)
where the term ρl ˙R2d0/σ is grouped as a ‘rim Weber number’, Werim, which describes
the competition between the radial momentum induced at the droplet periphery and the
913 A33-22
https://doi.org/10.1017/jfm.2021.7
 Published online by Cambridge University Press

<!-- PDF_PAGE: 23 -->

On aerodynamic droplet breakup
2.4(a)( b)
NB
Bag
BS
MB
Present
ST
2R
i/d0 = 1.6
Weber number : We Weber number : We
0.40
0.35
0.30
0.25
0.20
0.15
0.10
0.05
0
2.2
2.0
Initiatin diameter : 2Ri/d0
Initiation thickness : hi/d0
1.8
1.6
1.4
1.2
1.0
10
1 102 101 102
Figure 22. Measurements of droplet periphery thickness ( a) and diameter ( b)a t Ti. Periphery thickness
measurement is compared to the present model ( 4.11). Droplet CS diameter reaches a value of 2 Ri/d0 ≈ 1.6
for all breakup modes.
(b)(a) 0.40
0.35
0.30
0.25
0.20
0.15
0.10
0.05
0
Initiatin thickness : hi/d0
Rim Weber number : Werim
Rim Weber number : Werim
101
100
10–1
102
10110010–1 102
Weber number : We
101 102
NB
Bag
BS
MB
ST
Present
Present
We
rim = 1
Wec,Bag ≈ 8.8
Figure 23. Measurements of Werim vs. We (a) and periphery thickness vs. Werim (b) compared to the prediction
of (4.11). The criticality Werim = 1 agrees with the transition to the Bag morphology and deﬁnes Wec,Bag ≈ 8.8
(a), and periphery thickness vs. Werim compared to the prediction of ( 4.11)( b).
restoring surface tension of the stable droplet. For Werim < 1, the radial ﬂow momentum
is not strong enough to signiﬁcantly overcome surface tension and the drop will oscillate
with NB occurring. However, forWerim > 1, the radial momentum of the drop’s periphery
is great enough to overcome this restoring force, allowing the periphery to continuously
extend, facilitating the thinning and
blowout of the interior. This criticality deﬁnes the
onset of the Bag morphology, where Werim = 1a n d( 4.9) lead to Wec,Bag ≈ 8.8, which
agrees well with the present experiments, as shown in ﬁgure 23 (a), and to the previous
results discussed in § 1. Since the derivation of ( 4.11) does not account for any slowing in
˙R, which results from the thinning periphery, the present prediction is slightly high near
Wec,Bag where Werim is low.
913 A33-23
https://doi.org/10.1017/jfm.2021.7
 Published online by Cambridge University Press

<!-- PDF_PAGE: 24 -->

I.M. Jackiw and N. Ashgriz
d0 = 2.05 mm, We = 13.1
Ti = 0.8676 (2.6 ms)
d0 = 1.97 mm, We = 79.8
Ti = 0.582 (0.667 ms)
hi
hi
(a)( b)
Figure 24. Example of hi measurement from droplet periphery for low ( a) and high ( b) We.
The prediction of ( 4.11) is compared to the experiments with We and Werim in
ﬁgures 22 (b)a n d 23(b), respectively. The measurements shown in these ﬁgures are
taken at the periphery of the droplet in order to measure the thickness of the rim, as
measurements taken across the centre of the drop result in larger values due to the
undeformed core. Examples of this measurement are shown in ﬁgure 24 . Although the
trend agrees well with the experiments, the prediction of ( 4.11) consistently over-predicts
the measurements by ≈ 0.05 (note that a conservative measurement error of ±1p i x e l
results in ±0.025). A possible cause of this overprediction is that the present analysis
neglects ﬂow separation around the periphery of the windward disk. Flow separation
would cause a lower pressure at the periphery than is presently modelled, especially near
T
i when the windward disk is at its thinnest. This affects the balance of the surface tension
and pressure terms that govern the rim’s formation and would cause it to be thinner than
predicted.
With a good prediction of the dimensions of the initiation geometry, the core volume can
be determined and used to predict the initiation geometry. The windward disk is modelled
as a ﬂat disk with rounded edges having a radius of Ri and a thickness of hi (i.e. the
intersection of a short cylinder and a torus). The leading coefﬁcient of the h3
i term in
the volume equation for this geometry is very small compared to the other coefﬁcients
and can therefore be neglected. The volume of the disk, V
d, is thus given by ( 4.12). The
undeformed core is then the volume that remains from the initially spherical droplet ( V0 =
4/3π(d0/2)3), given by Vc = V0 − Vd (4.13)
Vd
V0
= 3
2
[(2Ri
d0
)2 ( hi
d0
)
− 2
(
1 − π
4
)(2Ri
d0
)( hi
d0
)2]
(4.12)
Vc
V0
= 1 − 3
2
[(2Ri
d0
)2 ( hi
d0
)
− 2
(
1 − π
4
)(2Ri
d0
)( hi
d0
)2]
. (4.13)
Figure 25 plots Vd (a)a n d Vc (b) for the present experiments with the predictions.
As with the prediction of di (4.11), the trend matches well; however, Vd is slightly
overpredicted resulting in the underprediction of Vc, delivering nonsensical results such
as Vd > V0 for low We. The over/underprediction of these volumes is the consequence
of the overprediction of di, therefore , to improve the model for the volume distribution
at initiation, the prediction of di must be further improved. However, the experimental
results can still be used to deﬁne the criterion for the transition between the various
913 A33-24
https://doi.org/10.1017/jfm.2021.7
 Published online by Cambridge University Press

<!-- PDF_PAGE: 25 -->

On aerodynamic droplet breakup
1.2
(a)( b)
Disk volume fraction : Vd /V0
Core volume fraction : Vc/V0
1.0
0.8
0.6
0.4
0.2
10
1
Weber number : We
102 101
Weber number : We
102
0
1.0
Bag
BS
MB
ST
Present
0.8
0.6
0.4
0.2
0
–0.2
Figure 25. Volume of initiation disk ( a) and undeformed core (b)v s. We. Dashed and dash-dotted lines indicate
where all and half of the droplet volume is contained in the disk, respectively. Solid lines give the predictions
of (4.12)( a)a n d 4.13 (b).
breakup morphologies. These trends also agree reasonably well with the experimental
results of Dai & Faeth ( 2001), considering the potential errors of their measurement
method (i.e. measuring the volume of the drops after the breakup, as well as relatively
low
spatial resolution).
For Bag breakup, it is expected that there is no undeformed core, therefore this
morphology will occur when Vd/V0 ≈ 1( Vc/V0 ≈ 0), which matches the experiments
as indicated by the dashed line in ﬁgure 25.
As described in § 3,B S ,MB and ST morphologies occur when Vc/V0 > 0( Vd/V0 < 1),
however, the criterion for Vc/V0 required for the transition from BS to MB is not as obvious
as the transition from Bag to BS. From ﬁgure 25 it can be seen that this transition occurs at
Vc/V0 ≈ 0.5 (indicated by the dash-dotted line), i.e. exactly half of the drop is undeformed.
The mass per unit frontal surface area of the undeformed core is maximal at this point
(assuming it takes roughly the shape of a spherical cap). This gives the core the greatest
resistance to being pushed downstream by the air ﬂow and allows the sheet to be blown out
before the core deforms signiﬁcantly. This explanation agrees with the physical description
of the MB breakup process in § 3.
The transition to ST from MB is governed by the aerodynamic forces and not V
c,
therefore there is no expected insight into the ST transition from this volume-based
analysis.
With this rough prediction of the breakup morphology and of the rim dimensions at
initiation, a prediction for the child drop sizes which result from the breakup of the rim
can now be formulated.
4.4. Rim expansion and bag blowout
The breakup sizes from the rim will be proportional to its diameter at breakup. It is
therefore necessary to ﬁnd the rim diameter after it has grown to the breakup size. From
conservation of mass on the rim, which formed at T
i with an initial minor and major
diameter ( di,a n d2 Ri, respectively) and the ﬁnal rim minor and major diameter ( df and
913 A33-25
https://doi.org/10.1017/jfm.2021.7
 Published online by Cambridge University Press

<!-- PDF_PAGE: 26 -->

I.M. Jackiw and N. Ashgriz
(a)
d0
2Ri
2Rf
df
βf2Ri – hi
(b)( c)
(d)
hi
hi ≈ di
h
Figure 26. Illustration of droplet geometry at ( a) T0,( b) Ti,( c) T+
i and (d) Tf for bag breakup with the relevant
dimensions for the rim expansion and bag growth indicated. The rim is marked by cross-hatching, while the
remainder of the windward disk is marked by the white area.
2Rf ), df is found by (4.14)
df = di
√
Ri
Rf
(4.14)
Since the initiation geometry,Ri and di, have already been deﬁned in §4.3, the remaining
factor to be determined is Rf , i.e. the extent of the rim’s expansion. The formation of the
rim coincides with the formation of the sheet between the rim and the undeformed core
which becomes the bag structures after Ti. The initial stage of the rim’s growth continues
at the constant ˙R found by ( 4.9). During this stage, the bag size, β, is smaller in the SW
direction than in the CS. Once the bag grows to and past the size of the rim, it pulls on the
rim and accelerates its growth until the bag breaks, after which the rim continues to grow
at a constant rate. This is seen in ﬁgure 5, and the geometries of interest are illustrated in
ﬁgure 26.
When the bag eventually ruptures, it quickly recedes around the bag (as described by
Lhuissier & Villermaux 2012) and collides with the droplet’s rim, instigating its breakup.
Therefore, it is assumed that the ﬁnal size of the rim is proportional to the ﬁnal size of
the bag when it breaks. In the cases of BS and MB breakup, the bag is conﬁned further
by the undeformed core. By determining the bag size at burst, β
f , one can approximate
Rf and thus determine the child drop size, dc. Vledouts et al. (2016) modelled the
breakup of accelerating liquid shells by supposing that the interface is susceptible to the
Rayleigh–Taylor instability with a growth rate, ω,g i v e nb y(4.15),
ω(t∗) =
√
ρl ¨β2(t∗)h(t∗)
2σ , (4.15)
where β(t∗) is the SW dimension of the bag and h(t∗) is the membrane thickness at time
t∗ = t − ti, as illustrated in ﬁgure 26(c). The breakup time was estimated by ( 4.16) where
C is a constant of O(1)
∫ t∗
b
0
ω(t∗) dt∗ = C. (4.16)
913 A33-26
https://doi.org/10.1017/jfm.2021.7
 Published online by Cambridge University Press

<!-- PDF_PAGE: 27 -->

On aerodynamic droplet breakup
Performing a force balance on the tip of the bag as in Villermaux & Bossa ( 2009), the
bag tip acceleration is found as
¨β(t∗) = p0
ρlh(t∗). (4.17)
Although Kulkarni & Sojka ( 2014) included surface tension in the force balance, its
effect is negligible. At its largest value (when the bag size is the size of the rim), it
effectively lowers the pressure by σ/2 << p0 for all cases.
The value of h(t∗) is determined by conservation of mass of the expanding disk,
approximating it as a cylinder of radius R − hi and thickness h, giving h(t∗) ≈ Vb/π(R −
hi)2 where Vb is the volume of the bag. The volume of the bag is the volume of the
windward disk that is not in the rim ( Vb = Vd − Vr). Vd was given earlier by ( 4.12). The
rim is modelled as a torus of major and minor diameters 2Ri and hi,w i t hVr given by (4.18).
It is worthwhile to note that for the Bag morphology, ( 4.18) estimates that the rim contains
50 %–80 % of the droplet volume which agrees with the ﬁndings of previous works (see
appendix B ), and is thus a good approximation of the droplet geometry. Since the disk
expands at a constant rate, the radius can be estimated by R = Ri + ˙Rt∗
Vr
V0
= 3π
2
[(2Ri
d0
)( hi
d0
)2
−
( hi
d0
)3]
(4.18)
Vb
V0
= 3
2
[(2Ri
d0
)2 ( hi
d0
)
−
(2Ri
d0
)( hi
d0
)2 (
2 + π
2
)
+ π
( hi
d0
)3]
(4.19)
The breakup time, t∗
b , is then found by substituting h into (4.15) and performing the integral
in ( 4.16), leading to ( 4.20) where the only term that remains to be determined in the
constant C
t∗
b =
[(2Ri
d0
)
− 2
( hi
d0
)]
(2˙R
d0
)
⎡
⎢⎢⎢
⎢⎣
− 1 +

√
1 + C 8τ√
3We
√
Vb
V0
(2˙R
d0
)
[(2Ri
d0
)
− 2
( hi
d0
)]
⎤
⎥⎥⎥
⎥⎦
. (4.20)
A much more detailed analysis of the instability growth in the bag is required in order
to determine C analytically, however
, the present data are not well suited for this as the
instability cannot be resolved on the bag. To determine C,( 4.20) is ﬁt to the breakup time
data of the present experiments and is found to be C ≈ 9.0, as shown in ﬁgure 27 (b).
In Vledouts et al. (2016), ( 4.16) was applied directly to an already thin shell where the
instability grows for the entire duration of t∗
b , thus the breakup time is relatively short and
C = O(1). In the present analysis, the deﬁnition of t∗
b to which ( 4.20) is ﬁt includes the
initial formation of the bag after Ti when ¨β is small and h is relatively large. In this case,
the instability does not develop appreciably for much of t∗
b ,a n dC > O(1). The bag size at
time t∗, β(t∗), is found by integrating ( 4.17) with the substitution of h,l e a d i n gt o(4.21)
β(t∗)
d0
= 3
4
(V0
Vb
) 1
τ2
{[(2Ri
d0
)
− 2
( hi
d0
)]2 t∗2
2
+
(2˙R
d0
)[ (2Ri
d0
)
− 2
( hi
d0
)] t∗3
3 +
(2˙R
d0
)2 t∗4
12
}
. (4.21)
913 A33-27
https://doi.org/10.1017/jfm.2021.7
 Published online by Cambridge University Press

<!-- PDF_PAGE: 28 -->

I.M. Jackiw and N. Ashgriz
101
Weber number : We
Bag size at burst : βf /d0
Burst time : Tb
∗ = tb
∗/τ
102 101
Weber number : We
102
PresentPresent, C ≈ 9.0
Bag
BS
MB
1.8 6
(b)(a)
5
4
3
2
1
0
1.6
1.4
1.2
1.0
0.8
0.6
0.4
Figure 27. Breakup time ( a) and bag size at burst ( b)v s .We. The solid lines are ( 4.20)w h i c hi sﬁ tt ot h ed a t a
giving C ≈ 9( a), and ( 4.21) evaluated at t∗
b (b).
Solution of (4.21) at time t∗
b (4.20) gives the bag size at the time it ruptures, βf , which is
compared to the experiments in ﬁgure 27(b). Although the prediction of β and βf match
the experiments within the errors typical of these experiments (see appendix B), it is clear
that the model does not capture all of the dynamics of the bag. In particular, the model
underpredicts βf at the higher We range of the BS morphology (20 < We < 30). It is likely
that this is the result of the shape of the bag around the stamen. This shape causes the bag
to be thicker between the stamen and the tip of the bag, thus the thinnest point of the bag
is between the bag tip and the rim. This would result in a slightly longer breakup time, as
the most susceptible point on the bag is farther away from the tip where the acceleration
is expected to be the greatest.
Equation ( 4.21) evaluated over 0 < t
∗ < t∗
b is compared to experiments in ﬁgure 28 ,
showing excellent agreement over a range of We for each morphology, with the exception
of the upper We limit for MB ( f ). In this case, the SW measurement appears to grow faster
than the prediction. At the high We limit of the MB morphology, the ST mechanics which
draw the periphery downstream begin to become signiﬁcant. As a result, the rim is drawn
somewhat downstream during this phase and dominates the SW measurement in the early
stages of the bag growth, causing apparent disagreement between the present model and
experiments. Even though this partial
ST occurs, the breakup ultimately persists as in MB.
The relationship between βf and 2Rf depends on the morphology of the breakup. The
breakup geometries are illustrated in ﬁgure 29, showing the assumed relationships between
βf and 2 Rf . For Bag breakup, the bag is only constrained by the rim, and since in the
late stage of the bag growth the bag size matches the rim diameter, the relationship
2R
f ≈ βf is suitable ( a)( s e e ﬁgure 7 ). For BS, the stamen causes a central fold of the
bag, thus 2 Rf ≈ 2βf (b)( s e eﬁgure 8). This is similar for the MB morphology, however ,
the undeformed core plays a more signiﬁcant role, and 2 Rf ≈ d0 + 2βf (c)( s e eﬁgures 10
and 11). Finally, for ST, the rim of the droplet is pulled downstream right after it forms at
diameter 2Ri/d0 (d)( s e eﬁgure 13). The ratio of 2Rf to βf is plotted for all morphologies in
ﬁgure 30(a). Figure 30 generally agrees with the above assumptions, showing that for Bag
breakup 2Rf /βf ≈ 1a n df o rM B2Rf /βf > 2, however, it is clear that there is a continuous
transition between the Bag and BS morphologies which is not captured here. As with the
prediction of βf , this is expected to be the result of the thickness modulations which occur
913 A33-28
https://doi.org/10.1017/jfm.2021.7
 Published online by Cambridge University Press

<!-- PDF_PAGE: 29 -->

On aerodynamic droplet breakup
6(a)( b)
(c)( d)
(e)( f )
5
4
3
2
1
0 0.5 1.0 1.5 2.0 2.5 0.5 1.0 1.5 2.0 2.5
6
5
4
3
2
1
0
6
5
4
3
2
1
0
4
3
2
1
0
4
3
2
1
0
0.5 1.0 1.5 2.0 2.5 0.5 1.0 1.5 2.0 2.5
0.5
Time : T = t/τ Time : T = t/τ
1.0 1.5 0.5 1.0 1.5
6
5
4
3
2
1
0
Deformation : L/d0Deformation : L/d0Deformation : L/d0
CS
SW
Present
We = 10.9 (Bag) We = 14.2 (Bag)
We = 15.3 (BS) We = 24.4 (BS)
We = 42.0 (MB) We = 72.1 (MB)
Figure 28. Experimental CS and SW droplet deformation L/d0 vs. time T for various We and morphologies
(annotated in ﬁgure). Equation (4.21) is given by the solid black lines, where the solid black dots indicated the
breakup point as calculated from ( 4.20). Every fourth data point is plotted for clarity.
due to the Bundt cake shape of the bag in the BS morphology. The prediction of 2 Rf
is shown in ﬁgure 30 (b). While the prediction generally agrees with the average of each
morphology, it is again clear that a derivation which takes into account the effect of the
continuity in the change of the core size as a result of the growing undeformed core on
2R
f /βf will provide better agreement across the Bag and BS morphologies.
The prediction of the rim expansion ratio, Ri/Rf , can now be substituted into ( 4.14),
which is compared with the experiments in ﬁgure 31 (a), showing good agreement
913 A33-29
https://doi.org/10.1017/jfm.2021.7
 Published online by Cambridge University Press

<!-- PDF_PAGE: 30 -->

I.M. Jackiw and N. Ashgriz
2Rf
2Rf 2Rf
2Rfβf
βf βf
2Rf ≈ βf 2Rf ≈ 2βf 2Rf ≈ 2Ri2Rf ≈ d0 + 2βf
(a) (b)( c)
(d)
Figure 29. Illustration of the breakup geometry for ( a)B a g ,( b)B S ,( c) MB and ( d) ST morphologies.
Measurements of and relationships between Rf and βf are indicated. The rim is marked by cross-hatching
while the undeformed core is marked by grey ﬁll.
5(a)( b)
Bag
BS
MB
ST
Bag
BS
MB
ST
Rim vs bag size at burst : 2Rf /βf
Rim major diameter at burst : 2Rf /d0
4
3
2
1
10
1 102
Weber number : We
101 102
Weber number : We
5
6
7
4
3
2
1
Figure 30. ( a)R i mv s. bag size at burst (2 Rf /βf ) for all breakup morphologies. The solid black line gives
2Rf /βf = 1 and the dashed black line gives 2 Rf /βf = 2, indicating the assumed value of 2 Rf /βf for Bag and
BS morphologies, respectively. (b) Rim major diameter at burst (2 Rf /d0) with prediction of ( 4.14).
with the results despite not fully capturing the continuous transitions as described
previously.
In the interest of formulating a continuous prediction, the median rim thinning ratio,
dr/di ≈ 0.64, is estimated from the experiments ( ﬁgure 31b) to be used as a comparison in
the next section. Note that the spread of the rim-thinning ratio in ﬁgure 31 is fairly large,
thus this term will only be used as a rough estimation in order to assess the effects of the
prior assumptions on the breakup prediction without the complexity of the morphology
variation.
Chou & Faeth (1998) performed a similar analysis using several simpliﬁcations. In their
analysis, the growth of the rim was determined directly by performing the momentum
balance between the rim and bag assuming the rim and bag thicknesses to be constant
and the rim volume to be V
r/V0 = 0.65. This was then ﬁt to their results using a
coefﬁcient analogous to Cd, which accounts for variations in the relationship of the
stagnation pressure and rim expansion. The expansion was then related to the rim thinning
by conservation of mass as was done in the present work, although the terminal rim
913 A33-30
https://doi.org/10.1017/jfm.2021.7
 Published online by Cambridge University Press

<!-- PDF_PAGE: 31 -->

On aerodynamic droplet breakup
0.25(a)( b)
Rim minor diameter at burst : df /d0
Rim thinning ratio : df /di
0.20
0.15
0.10
0.05
0
1.2
1.0
0.8
0.6
0.4
Median : 0.64
0.2
10
1 102
Weber number : We
101 102
Weber number : We
Bag
BS
MB
ST
Bag
BS
MB
ST
Figure 31. Measured rim minor diameter ( a)a n drim-thinning ratio (b)v s .We. Solid and open markers are for
side and end-on experiments, respectively. Lines give the prediction of ( 4.14)( a) and the median rim-thinning
ratio (b).
size was determined empirically. The rim was also assumed to continue growing after
the breakup of the bag, with bag and rim breakup times determined empirically. The
rim breakup was modelled by Rayleigh–Plateau instability, as in § 4.5. Due to these
simplifying assumptions, as well as a relatively small data set with which to ﬁt, their work
was not able to predict beyond the narrow range of 15 < We < 20. Essentially, the work of
the present section accounts for the variations in these assumptions, allowing it to achieve
good prediction across a range of We and morphologies.
4.5. Rim breakup
Confounding factors such as the number and location of the rupture sites and collisions of
the rupture fronts with each other and with the main rim of the droplet are numerous (see,
for example, ﬁgure 32 ). While many of these phenomena have been studied previously
(Bremond & Villermaux 2005; Lhuissier & Villermaux 2012; Vledouts et al. 2016;
Poulain, Villermaux & Bourouiba 2018), predictions of when each mechanism will be
preferred in the breakup are still illusive. The present experiments cannot be compared
directly to these works due to the limitations of the high-speed camera. The bag breakup
period occurs on a very short
time scale (T < 0.2) and at a very small spatial scale (db of
the order of μm). Since it is not possible to achieve the desired time and spatial resolution
while maintaining the wide ﬁeld of view that is necessary to capture the entire breakup
process, the present experiments are unable to provide insights into the breakup of the
bags formed in droplet breakup.
As mentioned previously, the rims that form in droplet breakup contain much more of
the droplet’s mass than the bags. Additionally, much of the volume of the bag merges with
the rim of the droplet once the bag recedes. The result is that most of the droplet’s volume
ends up being part of the rim breakup process and
the droplets formed from the bag are far
less important in terms of volume than those formed by the rim. It is therefore of higher
importance to model the breakup of the rim.
Once the bag has completed its breakup, the rim of major and minor diameters 2 Rf and
dr,f corrugates and breaks into many child droplets of size dc, as shown and illustrated in
ﬁgure 33. The rim is given a signiﬁcant initial perturbation when the receding bag collides
913 A33-31
https://doi.org/10.1017/jfm.2021.7
 Published online by Cambridge University Press

<!-- PDF_PAGE: 32 -->

I.M. Jackiw and N. Ashgriz
(a)
(b)
T = 2.467 (7.10 ms), /Delta1T = 0.017 (0.05 ms)
We =1 1, d0 = 1.88 mm
T = 1.826 (6.10 ms), /Delta1T = 0.015 (0.05 ms)
We = 10.9, d0 = 2.07 mm
Figure 32. Time-series images of the breakup of the bag showing ( a) a single rupture and (b) multiple ruptures.
Here, T gives the time of the ﬁrst frame, while Δ T gives the incremental time between each frame ; T increases
from left to right and continues in the bottom row.
with it, thus the instability grows and fractures the rim very quickly and the change in
the diameters of the rim during its breakup can be neglected. The rim, approximated by a
slender column of diameter dr,f , is unstable by the capillary Rayleigh–Plateau instability
which results in a child droplet size given by ( 4.22) (Ashgriz 2011)
dc
d0
= 1.89 df
d0
. (4.22)
The validity of this mechanism is established by comparing its prediction of the breakup
size given the experimental rim size just before its corrugation and the experimental ﬁnal
breakup sizes, shown in ﬁgure 34. The child droplet sizes were measured from regions of
the images where droplets from the breakup of the rims could be clearly identiﬁed using
the ImageJ particle size measurement tool. The reported sizes are the geometric mean
of the measured child droplets for each experimental condition. Droplets from the large
nodes such as those seen in ﬁgure 33 were excluded as their size does not directly relate
t ot h eﬁ n a ls i z eo ft h er i m .Figure 34 shows good agreement between the theory and the
experiments given the potential measurement error for these small geometries. However,
it can be seen that the prediction is somewhat higher than the measurements. This is likely
the result of neglecting the formation of larger nodes on the rim during the rim and bag
growth phase which would result in less mass in the ligament portions of the rim between
the nodes, and thus a smaller breakup size.
The overall prediction of the model is compared to experiments in ﬁgure 35(a). As with
the prediction of d
f /d0 in ﬁgures 30 and 31, the breakup prediction generally agrees with
the average behaviour for each breakup morphology, however, the breakup size for the Bag
morphology is overpredicted. This is because the model does not account for the beading
913 A33-32
https://doi.org/10.1017/jfm.2021.7
 Published online by Cambridge University Press

<!-- PDF_PAGE: 33 -->

On aerodynamic droplet breakup
df
d0 = 1.69 mm, We = 119
T = 2.689 (6.35 ms)
dc
2Rf
T = 3.324 (7.85 ms)
(b)
(a)
Figure 33. Illustration ( a) and end-on images ( b) of rim breakup.
0.5
Bag
BS
MB0.4
0.3
0.2
Rayleigh-Plateau theo. : dc/d0
0.1
0 0.5 0.40.30.20.1
Exp. rim child drop size : dc/d0
Figure 34. Rayleigh–Plateau breakup prediction (4.22) based on experimental rim minor diameter vs.
experimental rim child drop size. Solid and open markers are for side and end-on experiments, respectively.
that occurs on the rim which causes large nodes to accumulate in equal intervals around
the rim, which can be seen in ﬁgure 33. Zhao et al. (2010) suggest that these nodes are the
result of a Rayleigh–Taylor instability acting on the liquid rim. The instability results in a
preferential distribution of the droplet’s volume near the peak of the waves and as the rim
expands the segments in between the nodes are drawn thin while the nodes remain largely
intact. Since some of the rim volume is stored in these nodes, the ligament portions of
the rim grow thinner than the prediction as the mass conservation which led to ( 4.14)n o
longer holds. As the beading effect is much more prominent for the thicker rims, it has a
much greater effect on the Bag morphology than the others.
Other causes of the overprediction of dc/d0 in ﬁgure 35 (a) are the overprediction of
di/d0 from ( 4.10)( s e eﬁgure 22 ), and the slight overprediction of the Rayleigh–Plateau
breakup mechanism (( 4.22)a n d ﬁgure 34 ). The effects of these overpredictions are
913 A33-33
https://doi.org/10.1017/jfm.2021.7
 Published online by Cambridge University Press

<!-- PDF_PAGE: 34 -->

I.M. Jackiw and N. Ashgriz
Bag Present (df /di ≈ 0.64)
Present (di/d0 – 0.05)BS
MB
Bag
Rim child droplet size : dc/d0
BS
MB
ST
101
Weber number : We
102 101
Weber number : We
102
(b)(a) 0.5
0.4
0.3
0.2
0.1
0
0.5
0.4
0.3
0.2
0.1
0
Figure 35. Measured rim child droplet size vs. We. Solid and open markers are for side and end-on
experiments, respectively. Lines give the prediction of ( 4.22).
illustrated in ﬁgure 35 (b), where the prediction using the median rim-thinning ratio (see
ﬁgure 31b) is compared to the same using a shift of − 0.05 in di/d0 which accounts for
the overprediction of ( 4.10), as discussed in § 4.3. The shifted result better predicts the
experiments, however, there is still a slight overprediction which is similar to that of the
Rayleigh–Plateau mechanism seen in ﬁgure 34.
5. Conclusions
Although there have been many attempts to model the breakup of droplets, no analytical
model has been developed which describes and predicts both the breakup morphology
and the child droplet sizes for a wide range of conditions. Models which are capable
of predicting the droplet breakup size can only do so within limited ranges, give poor
prediction near We
c,Bag and do not capture the effects of breakup morphology, nor
do they predict their transitions. A key example of this is the TAB model (O’Rourke
&A m s d e n1987), which despite these shortcomings is widely used in industrial ﬂuid
dynamics software for relatively low We breakup (ANSYS Inc. 2011). Conversely, surface
instabilities, which are widely regarded in the literature to be the prevailing mechanism
of low We breakup (Guildenbecher et al. 2009), are able to predict only the breakup
morphology and have not been shown to be able to predict the child droplet sizes from
breakup; a prediction of signiﬁcant practical interest.
The model developed here expands on the internal ﬂow hypothesis, providing a
physically realistic mathematical description of the process including the various breakup
morphologies. As opposed to previous works, which modelled the deforming droplet as
a single ﬂattening ellipsoid, the present work considered the formation of a disk on the
windward surface of the drop during the deformation and the potential for a remaining
undeformed core at the onset of the bag
blowout which causes the BS, MB and ST
morphologies.
It was shown that the transition to the Bag morphology occurs when Werim = 1, which
gives Wec,Bag ≈ 8.8, while the transitions for BS, and MB can be predicted by determining
the distribution of the droplet volume between the windward disk and the undeformed
core. BS occurs when 0 < Vc/V0 < 0.5 where the undeformed core is small enough to be
913 A33-34
https://doi.org/10.1017/jfm.2021.7
 Published online by Cambridge University Press

<!-- PDF_PAGE: 35 -->

On aerodynamic droplet breakup
pulled into a stamen which does not break further. MB and ST morphologies occur when
Vc/V0 > 0.5 where the undeformed core is massive enough to undergo further breakup.
The ST transition arises in the estimation of the windward disk thickness where it was
shown that the air-ﬂow effects become more signiﬁcant than the rim’s radial inertia at
Wec,ST ≈ 80. Additionally, breakup sizes were successfully predicted for 9 < We < 80,
covering Bag, BS and MB breakup morphologies. A prediction was also made for the
ST morphology, however, the child drop sizes were not measurable for this range in the
present experiments.
While all of the relevant equations could be combined to formulate a set of three
predictive equations for the rim child drop size ( i. prediction of initiation geometry, ii.
prediction of morphology, iii. prediction of breakup), such an exercise would obscure
the importance of the individual steps on the ﬁnal results, as well as the effects of the
assumptions. The present model is therefore summarized in ﬂowchart form in ﬁgure 36.
The present model offers several notable improvements over previous works. Firstly,
the present model provides a physically realistic description of the process whereas
the past works have neglected the importance of the dynamics of both the initiation
and breakup phases, neglecting one or the other. This has allowed the present model
to be comprehensively veriﬁed against intermediate stages of breakup in addition to
the validation of the child droplet sizes and morphology. By comparison, past models
have only been able to validate against very limited deformation data in the initiation
phase, child droplet
sizes and/or breakup morphology transitions with no comparison
to the intermediate stages. The present model is also less dependent on empiricisms
which encapsulate either
physically unrealistic or dynamically complex physics such as
oscillation or cyclical deformation and drag relationships which are unlikely to yield
veriﬁable analytical replacements. The few empiricisms used in the present work ( a, Tbal,
2Ri/d0 and C) simplify the analysis to account for physical and fundamental underlying
phenomenon, such as the transient development of the surrounding air-ﬂow ﬁeld, which
can be studied more or less independently of the global breakup process and thus have
the potential to be determined analytically and veriﬁed against experiments or numerical
simulations. Furthermore, the developed model does not require numerical solution such
that these predictions can be made with three calculations per droplet to predict the
breakup morphology and the child drop size. This allows for much faster computation than
previous methods that required numerical solution, especially when considering the large
number of droplets which must be modelled in sprays. These improvements support the
hypothesis that internal ﬂow is the dominant mechanism in Bag,
BS and MB morphologies
and plays a signiﬁcant role in the ST morphology.
Supplementary movies. Supplementary movies are available at https://doi.org/10.1017/jfm.2021.7.
Funding. The authors acknowledge the ﬁnancial support of the International Fine Particle Research Institute
(IFPRI).
Declaration of interests. The authors report no conﬂict of interest.
Author ORCIDs.
Isaac M. Jackiw https://orcid.org/0000-0002-8552-1723;
Nasser Ashgriz https://orcid.org/0000-0002-5661-4453.
Appendix A. Eﬀect of the suspending needle
The obvious physical difference between this experimental method and the previous
methods ( shock tube Hanson, Domich & Adams ( 1963)a n d continuous air jet
913 A33-35
https://doi.org/10.1017/jfm.2021.7
 Published online by Cambridge University Press

<!-- PDF_PAGE: 36 -->

I.M. Jackiw and N. Ashgriz
InitiationBreakup
2. Rim formation
Rim forms at periphery of WW disk
• (4.10)
• Assumption: 2R
i/d0 ≈ 1.6
i/d0
2.1 Morphology prediction
• (4.13)
Based on volume remaining in
undeformed core, Vc/V0
Bag
BS
MB
ST
1. Droplet deformation
Radial expansion rate of WW disk
• (4.9)
• Assumptions: a = 6, T
bal =1/8
2R/d0
Due to bag growth over
the bag breakup time
3.Rim expansion and
bag blow-out
3.2 Rim expansion
Final rim size, 2Rf , related to
bag size, βf , through
morphology
Bag
BS
MB
ST
3.1 Bag blow-out
Bag breakup time, tb
∗
• (4.20)
Bag size at burst, β(tb
∗)
• (4.21)
3.3 Rim thinning
Conservation of mass
• (4.14)
4. Rim breakup
Rayleigh-Plateau capillary
breakup
• (4.22)
Bag BS
ST
Calculations:
• 1
• 2
• 3
MB
Vc/V0 < 0, Werim > 1
Vc/V0 > 0.5
0 < Vc/V0 < 0.5
We > 80
βf /d0
df /d0
dc/d0
2Rf ≈ βf
2Rf ≈ 2βf
2Rf ≈ 2Ri
2Rf ≈ d0 + 2βf
dc
df
df
2Rf
2Rf
2Ri
βf
hi ≈ di
d0
2R
d0
Figure 36. Flowchart of present model. There are three calculations: prediction of the initiation geometry
(1–2), the morphology (2.1) and the breakup ( 3–4). ‘Windward’ is abbreviated as ‘WW’.
913 A33-36
https://doi.org/10.1017/jfm.2021.7
 Published online by Cambridge University Press

<!-- PDF_PAGE: 37 -->

On aerodynamic droplet breakup
T = 0.668 (1.25 ms) T = 0.635 (0.83 ms)
T = 0.947 (2.6 ms) T = 0.670 (0.95 ms)
Figure 37. Effect of needle for low (left) and high (right) We, as seen from side-view (top) and end-on view
(bottom). In low We case, the droplet is clear of the needle for much of the ﬂattening period. In the high We
case, the radial expansion of drop is inhibited in the vicinity of the needle. Top left We = 22.5, bottom left
We = 21 (BS). Top right We = 50.4, bottom right We = 51 (MB).
Flock et al. 2012) is that the droplet is being suspended by a needle rather than being
dropped into an air ﬂow. This may interfere with the dynamics of the droplet deformation
and breakup. Based on the results of the present study, the needle has two main effects on
the droplet deformation and breakup; the two effects being the interference of the needle
with the radial expansion of the droplet, and the adhesion between the droplet and the
needle.
Figure 37 shows the interference of the needle on the radial expansion of droplets subject
to low (left) and high (right) We in the side (top) and end-on (bottom) views. When
the We is low, the rate of expansion of the droplet is low and the deforming droplet is
pushed downstream of the needle before much of the expansion occurs. As a result, the
expanding rim of the droplet is clear of the needle and minimal interference occurs in
the radial expansion. In this case, the droplet shape at initiation has good axial symmetry
as seen from the end-on view. At high We, however, the radial expansion rate is high
and the droplet is not pushed downstream of the needle before the needle interferes with
the expanding rim. This results in the top of the expanding rim being pushed away, and
the ﬂattening drop does not maintain ideal axial symmetry. Despite this, the experiments
compare favourably to previous results which did not use a needle to initially place the
drops (see appendix B).
Figure 38 compares the deformation measurements taken using a 22 gauge needle
(OD 0.71 mm) to the experiments using the 30 gauge needles used in the present study
for We ≈ 16. The size of the needle does not appear to have an effect on the initiation
period of the droplet deformation, suggesting that the measurement is unaffected by the
needle despite its interference with the droplets’ deformation. During the later stages of
deformation (bag growth and breakup), the experiments with the larger (22 gauge) needle
show a more rapid CS growth rate. This is because a liquid bridge forms between the
top extent of the droplets and the suspending needle, which can be seen in the examples
given in ﬁgure 39 . The liquid bridge is the result of the capillary adhesion of the liquid
to the needle, thus the size of the liquid bridge will be proportional to the size of
913 A33-37
https://doi.org/10.1017/jfm.2021.7
 Published online by Cambridge University Press

<!-- PDF_PAGE: 38 -->

I.M. Jackiw and N. Ashgriz
4
22 gauge - CS
22 gauge - SW
30 gauge - CS
30 gauge - SW
3
2
1
0 0.5 1.0
Time : T = t/τ
Extent of deformation : L/d0
1.5 2.0
Figure 38. Comparison of deformation using 22 and 30 gauge needle for suspending pendant drops. Initial
ﬂattening stage is unaffected, however, the deformation is different after the initiation of the bag. Every fourth
data point is plotted for clarity.
T = 2.285 (3.8 ms) T = 2.095 (3.9 ms)
T = 1.251
(1.643 ms)
(a)( b)( c)
Figure 39. Effect of needle on breakup in Bag ( a), BS (b) and MB ( c) regimes. In Bag and BS morphologies,
liquid bridge pulls top of rim which prematurely thins. In MB, the liquid strand prematurely blows out as a bag ;
(a–c) We = 14.2, 22.5, 50.4.
the needle. Since the liquid bridge breaks by capillary instability, the larger the liquid
bridge is, the longer it will persist into the deformation. Once the bridge separates, the
portion of the bridge connected to the droplet remains and is blown above the droplet,
possibly forming a bag. This interferes with the identiﬁcation of the top extent of the
droplet which is used in the CS measurement. The example of the effect of the liquid
bridge on bag breakup shown in ﬁgure 39 is an extreme example, and in most cases
the effect is not as signiﬁcant. Furthermore, the liquid bridge only appears to have a
signiﬁcant effect on the top of droplet, thus measurements based on the lower half of
the drop are not expected to be signiﬁcantly affected. Nevertheless, only the small (30
gauge) needle experiments are used in the present analysis as they give the best agreement
with the experimental measurements of others throughout the entire breakup process (see
appendix B).
Since
the liquid viscosity damps the effect of the capillary breaking of the liquid bridge,
the liquid bridge persists for longer and has a much greater effect on the overall droplet
breakup of high-viscosity ﬂuids. Figure 40 shows this for a 99.7 % glycerin drop ( μl =
913 A33-38
https://doi.org/10.1017/jfm.2021.7
 Published online by Cambridge University Press

<!-- PDF_PAGE: 39 -->

On aerodynamic droplet breakup
T = 1.089
(1.95 ms)
 T = 1.564 (2.8 ms) T = 2.123 (3.8 ms)
Figure 40. Image from experiment conducted with 99.7 % glycerine ( d0 = 1.95 mm, We = 46, Oh = 3.8).
Liquid strand between deforming droplet and suspending needle persists into late stages of deformation, having
a signiﬁcant effect on the droplet’s deformation. Movie available upon request.
1499 Pa s, ρl = 1264 kg m− 3, σ = 0.0634 N m− 1), where the liquid bridge pulls back on
the drop such that it tilts relative to the air ﬂow. Because of these adverse effects for high
viscosity ﬂuids, the experimental method is not capable of producing acceptable results
for high-viscosity ﬂuids.
Appendix B. Comparison of experimental results to others
The benchmark data which are compared to the present experiments are t h o s eo fF l o c k
et al. (2012), who dropped ethyl alcohol droplets ( D0 = 2.3 mm, Oh = 0.0059) through a
continuous air jet and recorded the deformation with a high-speed camera operating at 4
kHz. Previous studies have shown that Oh does not affect the transitional Wec nor the rate
of deformation when Oh < 0.01 (Hsiang & Faeth 1992), thus the difference in viscosity
to the present study is negligible. For both operating conditions studied ( We = 13, 32),
200 sets of experiments were conducted and the reported deformation data are the average
of each set as deviations in the ﬂow ﬁeld were observed, especially for the late stages of
droplet deformation. These deviations were attributed to the ‘random turbulent ﬂuctuations
and the stochastic nature of the fragmentation process’. The extents of the droplets in the x
and y directions were used to measure the droplets’ deformation in time. These data were
chosen to compare to the present experiments as they are the only published deformation
data with a comparable frame rate to that used in the present study. Furthermore, since
the nature of the experiment has a high degree of uncertainty, the averaged data offer a
consistent baseline with which to compare.
The present experimental method using the smaller 30 gauge needle for suspending the
droplets is compared to the experiments of Flock et al. (2012)i n ﬁgure 41. Reasonable
agreement is found between the two methods considering the amount of uncertainty
typical of droplet deformation, suggesting that the experiment and the ﬂow measurement
technique are consistent with previous studies. The large deviation in the present
experiment that occurs after initiation in the We = 28 case ( ﬁgure 41 b) is due to the
breakup process where bags are progressively blown out of the back of the ﬂattened droplet
as a result of the MB breakup morphology. Interestingly, the present measurements agree
exceptionally well with those of Flock et al. (2012) during the initiation period despite the
presence of the needle. This conﬁrms the observation made in appendix A that the needle
has little effect on the deformation of the drop during the initiation period.
In addition to the transient deformation data, measurements for which there are
well-established correlations can also be compared to prove the efﬁcacy of the
experimental method. Figure 42 compares the estimated initiation time T
i with the
913 A33-39
https://doi.org/10.1017/jfm.2021.7
 Published online by Cambridge University Press

<!-- PDF_PAGE: 40 -->

I.M. Jackiw and N. Ashgriz
4
5(a)( b)
3
2
1
0
4
3
2
1
0
Extent of deformation : L/d0
0.5 1.0
Time : T = t/τ
1.5 2.0 0.5 1.0
Time : T = t/τ
1.5 2.0
Present - CS
Present - SW
Flock et al. (2012) - CS
Flock et al. (2012) - SW
Figure 41. Comparison of present study with measurements of Flock et al. (2012)f o rWe ≈ 13 (a)a n d
We ≈ 30 (b). For the present experiments, every fourth data point is plotted for clarity.
1.2 Pilch & Erman (1987)
Initiation time : Ti
1.0
0.8
0.6
0.4
0.2
10
1 102
Weber number : We
NB
Bag
BS
MB
ST
0
Figure 42. Estimated Ti vs. We for present measurements (markers) compared with empirical correlation of
Pilch & Erdman ( 1987) (dashed line).
correlation of Pilch & Erdman ( 1987), showing good agreement for all morphologies
except for Bag, which is slightly below the correlation. This is due to the slight difference
in the deﬁnition of Ti, as the correlation of Pilch & Erdman ( 1987) deﬁnes it as the time
at which the bag ﬁrst forms, whereas the present deﬁnition is that of Flock et al. (2012)
in which it is the time at which the minimal SW dimension is achieved. These correspond
well for BS, MB and ST morphologies, however, since there is no undeformed core in the
Bag morphology the minimal thickness endures for longer, corresponding to the formation
of the rim before the bag.
Figure 43 compares the CS deformation ( a) and initiation thickness ( b) of the present
experiments to the experimental correlations of Hsiang & Faeth ( 1992) and Zhao et al.
(2010). Rigorously, these correlations are for the maximal CS deformation, and associated
minimal SW thickness, before bag formation, however , the deﬁnitions are comparable.
913 A33-40
https://doi.org/10.1017/jfm.2021.7
 Published online by Cambridge University Press

<!-- PDF_PAGE: 41 -->

On aerodynamic droplet breakup
101 102 101 102
0.5 0
0.05
0.10
0.15
0.20
0.25
0.30
0.35
0.40
Hsiang & Faeth (1992)
NB
Bag
BS
MB
ST
Hsiang & Faeth (1992)
Zhao et al. (2011)
1.0
1.5
2.0
2.5
Weber number: We Weber number: We
Initiation diameter: 2Ri/d0
Initiation thickness: hi/d0
(a)( b)
Figure 43. Initiation diameter ( a) and thickness ( b)v s .We for present experiments (markers) compared with
empirical correlations of Hsiang & Faeth ( 1992)a n dZ h a oet al. (2011a).
Furthermore, no correlations are available based on the initiation deﬁnition of Flock
et al. (2012) despite it being easier to measure. These correlations expect the maximal
deformation to increase as We increases, however, the present experiments show that
the deformation is roughly constant at 2 Ri/d0 ≈ 1.6. This is largely due to the previous
deﬁnition of Ti being difﬁcult to establish exactly, especially for the poor time-resolved
data that were available at the time and, late in the deformation , small deviations in
T translate to potentially large deviations in 2 Ri. The correlation for the minimal SW
thickness of Hsiang & Faeth (1992) is derived directly from the correlation for the maximal
CS deformation assuming conservation of mass via an ellipsoidal geometry and is not
ﬁt directly to data, as SW measurements were not possible at the time due to camera
resolution constraints. It is therefore understandable that this correlation would overpredict
the present experiments as it does not account for the thinning of the interior of the disk;
nevertheless, the trend agrees well.
Figure 44 compares the measurement of the child drop sizes from the rim of the present
experiments to the correlation Zhao et al. (2011b), which was also established for the rim
breakup sizes. Excellent agreement is seen within the ±0.025 error in the experiments.
Figure 45 shows the rim volume estimated by ( 4.18) for the present experiments for
the Bag and BS morphologies at low We. These are compared to the experimental
approximations of Lane ( 1951)( Vr/V0 ≈ 0.7) and of Chou & Faeth ( 1998)( Vr/V0 ≈
0.55). T wo conclusions are evident. Firstly, ﬁgure 45 shows that the approximation of the
rim as a torus of major and minor diameters of 2 Ri and hi is good. Second, it shows that
the estimations of Lane ( 1951) and Chou & Faeth ( 1998) are not in contradiction to each
other as was previously thought, but are simply based on slightly different We data which
is enough to alter the volume contained in the rim.
Further validation of the experiments is found by comparing the transitional critical
Weber number criteria, Wec, between the observed breakup morphologies with those
published in the literature. While the reported values of Wec suggest discrete transition
points, the transitions are actually continuous (Guildenbecher et al. 2009). As a result,
reported values of Wec approximate the transition regions and seldom match all
experiments exactly. Guildenbecher et al. (2009) summarize the morphology transitions
913 A33-41
https://doi.org/10.1017/jfm.2021.7
 Published online by Cambridge University Press

<!-- PDF_PAGE: 42 -->

I.M. Jackiw and N. Ashgriz
101
0
0.1
0.2
0.3
0.4
0.5
Weber number: We
MB
BS
Bag
Zhao et al. (2011)
Rim child droplet size: dc/d0
102
Figure 44. Measured rim child drop size vs. We compared to the empirical correlation of Zhao et al. (2011a).
Solid and open markers are for side and end-on experiments, respectively.
10
Weber number: We
Rim volume fraction: Vr/V0
0
0.2
0.4
0.6
0.8
1.0
15 20
Bag
BS
Lane (1951)
Chou & Faeth (1998)
Figure 45. Comparison of estimated rim volume ( 4.18) to previous experiments of Lane ( 1951) and Chou &
Faeth (1998) for Bag and BS morphologies.
as Wec,Bag ≈ 11, Wec,BS ≈ 18, Wec,MB ≈ 35 and Wec,ST ≈ 80, which is representative of
both shock-tube and continuous-air-jet studies. Comparatively, Zhao et al. (2010)g i v e
experimental Wec values of Wec,Bag ≈ 12, Wec,BS ≈ 16, Wec,MB ≈ 28 and Wec,ST ≈ 80 for
the continuous-air-jet method. Zhao et al. (2010) had the additional deﬁnition of ‘dual-bag
breakup’, which is found to be the transition between BS and MB, as described in § 3. The
present experiments show Wec,Bag ≈ 10, Wec,BS ≈ 15, Wec,MB ≈ 30 and Wec,ST ≈ 80).
The present data of morphology breakup are plotted in terms of We and Oh in ﬁgure 46
with comparison to the Wec boundaries of both Guildenbecher et al. and Zhao et al. given
by dashed lines. The results of the present method appear to agree well with the published
transitions given the degree of uncertainty in the literature as to the exact locations of the
regime transitions. The transition which compares the least favourably with the presented
literature is We
c,Bag,h o w e v e r, this value agrees well with the results of Krzeczkowski
(1980) who give Wec,Bag ≈ 10.
913 A33-42
https://doi.org/10.1017/jfm.2021.7
 Published online by Cambridge University Press

<!-- PDF_PAGE: 43 -->

On aerodynamic droplet breakup
101
102
2.62.4 2.8
Ohnesorge number: Oh × 10–3Ohnesorge number: Oh × 10–3
Weber number: We
3.0 3.2 2.4 2.6 2.8 3.0 3.2
NB
Bag
BS
MB
ST
NB
Bag
BS
MB
ST
NB
Bag
BS
MB
ST
(a)( b)
Figure 46. Plot of We vs. Oh for present experiments. Dashed lines are the approximate transition Wec
boundaries of previous studies. ( a) Compares the present experiments with the boundaries of Guildenbecher
et al. (2009), (b) compares with the boundaries of Zhao et al. (2010).
Appendix C. Discussion of other internal ﬂow modelling attempts
As discussed in the introduction (§ 1), there were two prior modelling attempts which
essentially sought to model the internal ﬂow of the drop, Villermaux & Bossa ( 2009)a n d
Kulkarni & Sojka ( 2014). The difference between these past analyses and the present one
is in the three main assumptions that are required for ( 4.6) to predict droplet deformation.
The ﬁrst of these assumptions is the selection of the windward and peripheral curvatures,
κw and κp. Villermaux & Bossa ( 2009) and Kulkarni & Sojka ( 2014) assumed that κw is
negligible, as was done in the present analysis. However, these analyses also neglected the
azimuthal curvature, giving κ = 2/h.I tw a ss h o w ni n§4.2 that the azimuthal curvature’s
effect on κp cannot be neglected (see ﬁgure 18), and was included in the present analysis.
The next requirement for the analysis is the relationship between h and R, which
comes from the assumption of the shape of the droplet during the deformation. The
previous analyses simpliﬁed the shape of the droplet as a cylindrical disk, which
by conservation of mass with the initially spherical droplet gives h/d0 = 2/3(d0/2R)2.
However, this is inaccurate for small deformations as a cylinder is a poor approximation
of a nearly spherical shape. Good agreement for small deformations is important as much
of the deformation period occurs while the deformations are small. A variation on this
assumption is that the droplet deforms as an ellipsoid with h/d
0 = (d0/2R)2, which gives
better agreement for small deformations. These two assumptions are compared in ﬁgure 47
where the error in the estimated volume at Ti, Vi, relative to the initial droplet volume, V0,
for the experiments is shown. Perfect agreement of the assumed geometry corresponds to
a value of (Vi − V0)/V0 = 1. The ellipsoidal geometry gives a better approximation of the
droplet shape at initiation than the cylindrical geometry, however ,i ti sn o te x a c td u et o
the fact that the droplet is not perfectly ellipsoidal as the rim, membrane, and undeformed
core geometries form through the deformation as described in § 3.
These assumptions simplify ( 4.6)a s( C1). Kulkarni & Sojka ( 2014) included a viscous
term in the pressure balance across interface, however , for the range of Oh studied (Oh <
0.054) the effect of this term was less than the uncertainty in their measurements and is
neglected from the present discussion. The effect of high Oh on the analysis remains to be
913 A33-43
https://doi.org/10.1017/jfm.2021.7
 Published online by Cambridge University Press

<!-- PDF_PAGE: 44 -->

I.M. Jackiw and N. Ashgriz
101 102 101 102
0
0.5
1.0
1.5
2.0
Weber number: We
Ellipsoid Disk
Weber number: We
NB
Bag
BS
MB
ST
V olume est. error: (Vi –V0 )/V0 
(a)( b)
Figure 47. Comparison of error in conservation of volume assumption from measurements at Ti for ellipsoid
and cylindrical geometries; (Vi − V0)/V0 = 1 (dash-dot line) indicates perfect agreement.
studied
¨R
R = 1
τ2
(a
2
)2 [
1 − 96
a2We
]
. (C1)
The ﬁnal assumption in this part of the analysis is the value of the stretching
constant, a. Villermaux & Bossa ( 2009) and Kulkarni & Sojka ( 2014) assumed constant
values for a, thus for We < 96/a2,( C1) is the solution to an oscillating droplet similar to
the TAB model (O’Rourke & Amsden 1987), while for We > 96/a2 the solution becomes
one of exponential and unbounded growth in time. Both suggested that this deﬁnes the
transition to bag breakup, assuming that the droplet will only break if it is permitted to
deform exponentially. Villermaux & Bossa ( 2009) interpolated between the limits of a
to a constant value of a = 4 giving Wec,Bag = 6 which does not agree with any of the
reported values, including those cited by Villermaux & Bossa ( 2009), Hinze ( 1955)a n d
Hanson et al. (1963). This error may be the result of comparing the We based on the radius
(We = ρlU2R0/σ)w i t ht h eWe based on the diameter ( 1.1) in the cited sources. Kulkarni
&S o j k a(2014) choose a value of a = 2
√
2, leading to Wec,Bag = 12 which agrees much
better with the reported values (Guildenbecher et al. 2009; Zhao et al. 2010). While the
model of Kulkarni & Sojka ( 2014) was compared to a small set of their own deformation
data, the model of Villermaux & Bossa ( 2009) was primarily used to determine h(t) and
was not validated against deformation data. Both were proposed only for the bag-type
morphology. In both cases, the constant value of a was essentially chosen to agree with the
reported Wec,Bag. The constant value of a leads to exponential growth when We > 96/a2.
However, this is not the trend seen in the experiments which show a constant growth rate
after an initial non-constant period until the initiation point (as described in §§ 3 and 4.2).
REFERENCES
ALISEDA ,A . ,H OPFINGER , E.J., L ASHERAS , J.C., K REMER , D.M., B ERCHIELLI ,A .&C ONNOLL Y, E.K.
2008 Atomization of viscous and non-newtonian liquids by a coaxial, high-speed gas jet. Experiments and
droplet size modeling. Intl J. Multiphase Flow 34 (2), 161–175.
ANSYS I
NC .2 0 1 1ANSYS FLUENT User’s Guide Release 14.0 . Canonsburg, PA.
ASHGRIZ ,N .2 0 1 1Handbook of Atomization and Sprays: Theory and Applications .S p r i n g e r .
913 A33-44
https://doi.org/10.1017/jfm.2021.7
 Published online by Cambridge University Press

<!-- PDF_PAGE: 45 -->

On aerodynamic droplet breakup
BREMOND ,N .&V ILLERMAUX , E. 2005 Bursting thin liquid ﬁlms. J. Fluid Mech. 524, 121–130.
CHOU ,W . H .&F AETH , G.M. 1998 Temporal properties of secondary drop breakup in the bag breakup regime.
Intl J. Multiphase Flow 24 (6), 889–912.
DAI ,Z .&F AETH , G.M. 2001 Temporal properties of secondary drop breakup in the multimode breakup
regime. Intl J. Multiphase Flow 27, 217–236.
DORSCHNER ,B . ,B IASIORI -POULANGES , L., S CHMIDMAYER ,K . ,E L-RABII ,H .&C OLONIUS , T. 2020
On the formation and recurrent shedding of ligaments in droplet aerobreakup. J. Fluid Mech. 904, A20.
FLOCK , A.K., G UILDENBECHER , D.R., C HEN ,J . ,S OJKA , P .E. & B AUER , H.-J. 2012 Experimental
statistics of droplet trajectory and air ﬂow during aerodynamic fragmentation of liquid drops. Intl
J. Multiphase Flow 47, 37–49.
GUILDENBECHER , D.R., L ÓPEZ -RIVERA ,C .&S OJKA , P.E. 2009 Secondary atomization. Exp. Fluids 46
(3), 371–402.
HANSON , A.R., D OMICH , E.G. & A DAMS , H.S. 1963 Shock tube investigation of the breakup of drops by
air blasts. Phys. Fluids 6 (8), 1070–1080.
HARPER , E.Y ., G RUBE ,G . W .&C HANG , I.-D. 1972 On the breakup of accelerating liquid drops. J. Fluid
Mech. 52 (3), 565–591.
HINZE , J.O. 1955 Fundamentals of the hydrodynamic mechanism of splitting in dispersion processes. AIChE
J. 1 (3), 289–295.
HSIANG , L.P . & F AETH , G.M. 1992 Near-limit drop deformation and secondary breakup. Intl J. Multiphase
Flow 18 (5), 635–652.
IBRAHIM , E.A., Y ANG ,H . Q .&P RZEKW AS , A.J. 1993 Modeling of spray droplets deformation and breakup.
J. Propul. Power 9 (4), 651–654.
JAIN ,M . ,P RAKASH , R.S., T OMAR ,G .&R AV I K R I S H N A, R.V. 2015 Secondary breakup of a drop at
moderate Weber numbers. Proc. R. Soc. Lond. A 471, 20140930.
JAIN , S.S., T YAGI ,N . ,P RAKASH , R.S., R AV I K R I S H N A,R . V .&T OMAR , G. 2018 Secondary breakup of
drops at moderate Weber numbers: effect of Density ratio and Reynolds number. Intl J. Multiphase Flow
117, 25–41.
JALAAL ,M .&M EHRA V ARAN, K. 2014 Transient growth of droplet instabilities in a stream. Phys. Fluids
26, 012101.
JOSEPH , D.D., B EA VERS,G . S .&F UNADA , T. 2002 Rayleigh–Taylor instability of viscoelastic drops at high
Weber numbers. J. Fluid Mech. 453, 109–132.
KELLER ,J . B .&K OLODNER , I. 1954 Instability of liquid surfaces and the formation of drops. J. Appl. Phys.
25 (7), 918–921.
KRZECZKOWSKI , S.A. 1980 Measurement of liquid droplet disintegration mechanisms. Intl J. Multiphase
Flow 6 (3), 227–239.
KULKARNI ,V .&S OJKA , P.E. 2014 Bag breakup of low viscosity drops in the presence of a continuous air
jet. Phys. Fluids 26, 072103.
LANE , W.R. 1951 Shatter of drops in streams of air. Ind. Engng Chem. 43 (6), 1312–1317.
LEE , M.W ., P ARK , J.J., F ARID ,M . M .&Y OON , S.S. 2012 Comparison and correction of the drop breakup
models for stochastic dilute spray ﬂow. Appl. Math. Model. 36 (9), 4512–4520.
LHUISSIER ,H .&V ILLERMAUX , E. 2012 Bursting bubble aerosols. J. Fluid Mech. 696, 5–44.
LIU, A.B., M ATHER ,D .&R EITZ , R.D. 1993 Modeling the effects of drop drag and breakup on fuel sprays.
SAE Tech. Paper Series 930072.
MASHAYEK ,A .&A SHGRIZ , N. 2009 Model for deformation of drops and liquid jets in gaseous crossﬂows.
AIAA J. 47 (2), 303–313.
MENG ,J . C .&C OLONIUS , T. 2018 Numerical simulation of the aerobreakup of a water droplet. J. Fluid Mech.
835, 1108–1135.
O’R OURKE ,P . J .&A MSDEN , A.A. 1987 The tab method for numerical calculation of spray droplet breakup.
SAE Tech. Paper Series 872089.
PARK , J.-H., Y OON ,Y .&H WA NG, S.-S. 2002 Improved tab model for prediction of spray droplet
deformation and breakup. Atomiz. Sprays 12, 387–401.
PILCH ,M .&E RDMAN , C.A. 1987 Use of breakup time data and velocity history data to predict the maximum
size of stable fragments for acceleration-induced breakup of a liquid drop. Intl J. Multiphase Flow 13 (6),
741–757.
POULAIN ,S . ,V ILLERMAUX ,E .&B OUROUIBA , L. 2018 Ageing and burst of surface bubbles. J. Fluid Mech.
851, 636–671.
PRITCHARD ,P . J .&L EYLEGIAN ,J . C .2 0 1 1Introduction to Fluid Mechanics. John Wiley and Sons.
RIMBERT ,N . ,C ASTRILLON ESCOBAR ,S . ,M EIGNEN ,R . ,H ADJ -ACHOUR ,M .&G RADECK , M. 2020
Spheroidal droplet deformation, oscillation and breakup in uniform outer ﬂow. J. Fluid Mech. 904,A 1 5 .
913 A33-45
https://doi.org/10.1017/jfm.2021.7
 Published online by Cambridge University Press

<!-- PDF_PAGE: 46 -->

I.M. Jackiw and N. Ashgriz
SCHLICHTING ,H .&G ERSTEN ,K .2 0 1 7Boundary-Layer Theory ,S p r i n g e r .
STEFANITSIS ,D . ,S TROTOS ,G . ,N IKOLOPOULOS ,N . ,K AKARAS ,E .&G AVA I S E S,M .2 0 1 9I m p r o v e d
droplet breakup models for spray applications. Intl J. Heat Fluid Flow 76, 274–286.
STROTOS ,G . ,M ALGARINOS ,I . ,N IKOLOPOULOS ,N .&G AVA I S E S, M. 2016 Predicting droplet deformation
and breakup for moderate Weber numbers. Intl J. Multiphase Flow 85, 96–109.
TANNER , F.X. 1997 Liquid jet atomization and droplet breakup modeling of non-evaporating diesel fuel
sprays. SAE Tech. Papers 970050.
THEOFANOUS , T.G., L I,G . J .&D INH , T.N. 2004 Aerobreakup in rareﬁed supersonic gas ﬂows. Trans.
ASME: J. Fluids Engng 126 (4), 516–527.
THEOFANOUS , T.G., M ITKIN , V .V ., NG, C.L., C HANG , C.-H., D ENG ,X .&S USHCHIKH ,S .2 0 1 2T h e
physics of aerobreakup. II. Viscous liquids. Phys. Fluids 24, 022104.
VARGA , C.M., L ASHERAS ,J . C .&H OPFINGER , E.J. 2003 Initial breakup of a small-diameter liquid jet by a
high-speed gas stream. J. Fluid Mech. 497 (497), 405–434.
VILLERMAUX ,E .&B OSSA , B. 2009 Single-drop fragmentation determines size distribution of raindrops.
Nat. Phys. 5 (9), 697–702.
VLEDOUTS ,A . ,Q UINARD ,J . ,V ANDENBERGHE ,N .&V ILLERMAUX , E. 2016 Explosive fragmentation of
liquid shells. J. Fluid Mech. 788, 246–273.
XIAO ,F . ,D IANAT ,M .&M CGUIRK , J.J. 2016 A robust interface method for drop formation and breakup
simulation at high density ratio using an extrapolated liquid velocity. Comput. Fluids 136, 402–420.
YANG ,W . ,J IA ,M . ,C HE , Z., S UN ,K .&W ANG , T. 2017 Transitions of deformation to bag breakup and
bag to bag-stamen breakup for droplets subjected to a continuous gas ﬂow. Intl J. Heat Mass Transfer 111,
884–894.
ZHAO ,H . ,L IU,H . - F . ,CAO, X.-K., L I,W . - F .&X U, J.-L. 20 1 1a Breakup characteristics of liquid drops in
bag regime by a continuous and uniform air jet ﬂow. Intl J. Multiphase Flow 37 (5), 530–534.
ZHAO ,H . ,L IU,H . - F . ,LI,W . - F .&X U, J.-L. 2010 Morphological classiﬁcation of low viscosity drop bag
breakup in a continuous air jet stream. Phys. Fluids 22, 114103.
ZHAO ,H . ,L IU,H . - F . ,XU, J.-L. & L I,W . - F .2 0 1 1b Experimental study of drop size distribution in the bag
breakup regime. Ind. Engng Chem. Res. 50 (16), 9767–9773.
ZHAO ,H . ,L IU,H . - F . ,X U, J.-L., L I,W . - F .&L IN , K.-F. 2013 Temporal properties of secondary drop
breakup in the bag-stamen breakup regime. Phys. Fluids 25, 054102.
913 A33-46
https://doi.org/10.1017/jfm.2021.7
 Published online by Cambridge University Press
