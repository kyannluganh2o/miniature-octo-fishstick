<!-- PDF_PAGE: 1 -->

REVIEW ARTICLE
Secondary atomization
D. R. Guildenbecher Æ C. Lo´pez-Rivera Æ
P. E. Sojka
Received: 12 June 2008 / Revised: 27 October 2008 / Accepted: 10 November 2008 / Published online: 22 January 2009
/C211 Springer-Verlag 2009
Abstract When a drop is subjected to a surrounding
dispersed phase that is moving at an initial relative
velocity, aerodynamic forces will cause it to deform and
fragment. This is referred to as secondary atomization. In
this paper, the abundant literature on secondary atomiza-
tion experimental methods, breakup morphology, breakup
times, fragment size and velocity distributions, and mod-
eling efforts is reviewed and discussed. Focus is placed on
experimental and numerical results which clarify the
physical processes that lead to breakup. From this, a con-
sistent theory is presented which explains the observed
behavior. It is concluded that viscous shear plays little role
in the breakup of liquid drops in a gaseous environment.
Correlations are given which will be useful to the designer,
and a number of areas are highlighted where more work is
needed.
List of symbols
Dimensional
a drop acceleration (m/s
2)
c velocity of sound (m/s)
D10 drop or fragment arithmetic mean diameter (m)
D30 drop or fragment volume mean diameter (m)
D32 drop or fragment Sauter mean diameter (m)
D43 drop or fragment de Brouckere mean diameter (m)
d0 drop initial spherical diameter (m)
dcore diameter of drop core at end of sheet-thinning
breakup (m)
d
cro drop cross-stream diameter (m)
dstr drop stream-wise diameter (m)
FD aerodynamic drag force (kg m/s 2)
Fsurf net surface force (kg m/s 2)
Fl shear force (kg m/s 2)
f0(D) fragment number PDF (1/m)
f3(D) fragment volume PDF (1/m)
K power-law ﬂuid consistency index (kg/m s (2-n))
k wave number; 2 p/k (1/m)
MMD drop or fragment mass median diameter (m)
q net electrostatic charge (C)
qRa Rayleigh charge limit (C)
t time (s)
U0 initial relative velocity between drop and ambient
ﬂuid in main ﬂow direction (m/s)
U
core velocity of drop core relative to ambient ﬂuid (m/s)
/C22Uf mean relative velocity of fragments in main ﬂow
direction (m/s)
V0 initial relative velocity between drop and ambient
ﬂuid perpendicular to main ﬂow direction (m/s)
/C22V
f mean relative velocity of fragments in cross-
stream direction (m/s)
d boundary layer thickness (m)
ea electrical permittivity of ambient (C 2/N m2)
k wavelength (m)
k(1) elastic ﬂuid relaxation time (s)
la ambient viscosity (kg/m s)
ld drop viscosity (kg/m s)
leff power-law effective viscosity (kg/m s)
lsol solvent shear viscosity (kg/m s)
qa ambient density (kg/m 3)
This material is based upon work supported under a National Science
Foundation Graduate Research Fellowship.
D. R. Guildenbecher ( &) /C1C. Lo´pez-Rivera /C1P. E. Sojka
Maurice J. Zucrow Laboratories,
School of Mechanical Engineering, Purdue University,
West Lafayette, IN 47907-2014, USA
e-mail: sojka@purdue.edu; sojka@ecn.purdue.edu
123
Exp Fluids (2009) 46:371–402
DOI 10.1007/s00348-008-0593-2

<!-- PDF_PAGE: 2 -->

qd drop density (kg/m 3)
r surface tension (kg/s 2)
Non-dimensional
CD instantaneous coefﬁcient of drag based on drop
cross-stream diameter
/C22CD average coefﬁcient of drag based on initial
spherical diameter
CD-sphere coefﬁcient of drag of a solid sphere at a given
Reynolds number
Eocr Eo¨tvo¨s number at end of sheet-thinning
breakup; a qd /C0 qajj d2
core
/C14
r
La Laplace number; La = Oh-2
Ma Mach number
N viscosity ratio; ld/la
n power-law ﬂuid ﬂow behavior index
Oh Ohnesorge number; ld= ﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃqdd0rp
Re gas-phase Reynolds number; qaU0d0=la
ReNN Reynolds number for a power-law ﬂuid;
qU0
2-nd0
n/K
T dimensionless time; tU0e/C0 1=2d/C0 1
0
Tini breakup initiation time
Ttot total breakup time
We Weber number; qaU2
0 d0
/C14
r
Wec critical Weber number
WecOh?0 critical Weber number at low Ohnesorge
number
Wecore Weber number of drop core at end of sheet-
thinning breakup
Wee- electrostatic Weber number;
qaU0d2
0
/C14
r /C0 q2/C14
8p2ead3
0
/C0/C1
Wi Weissenberg number; kð1ÞU0
.
d0
y non-dimensional displacement of drop equator;
1 - (d0/dcro)2
e density ratio; qd/qa
x exponential growth factor
1 Introduction
Spray formation, or the production of drops, is a common
phenomenon in a variety of scientiﬁc and engineering
applications. When an initially spherical drop encounters
an ambient ﬂow ﬁeld moving at a velocity relative to it,
aerodynamic forces cause the drop to deform and (perhaps)
break apart into fragments. This process is referred to as
secondary atomization.
Secondary atomization is in contrast to primary atom-
ization where bulk ﬂuid, typically in the form of a sheet or
jet, breaks up for the ﬁrst time and forms drops. In spray
formation, primary atomization occurs at or near the nozzle
exit. This may be followed by secondary atomization,
which typically occurs further downstream.
Secondary breakup occurs in a wide variety of systems,
and is desired in applications as diverse as mass spec-
trometry (for homeland security portals), internal
combustion engines (for land-based power production),
injection of gelled hypergolic fuels (for aero-propulsion),
coatings (manufacture of pharmaceutical tablets or painting
of automobiles), materials processing (thermal barrier
coatings), and many more.
Since the goal of many atomization processes is to
control the ﬁnal droplet sizes, one of the most important
reasons to study secondary atomization is to determine the
conditions that lead to appropriate fragment sizes. In
combustion applications, for example, it is desirable to
produce small drops in order to increase evaporation and
mixing rates. Interestingly, as noted by Tryggvason (1997),
the highest ambient velocity does not always lead to the
smallest drop diameters. Therefore, by clearly under-
standing secondary breakup it may be possible to ﬁnd ﬂow
conditions that will produce the desired size drops.
There exists abundant literature on secondary atomiza-
tion. The ﬁrst comprehensive review was provided by Pilch
and Erdman ( 1987) over 20 years ago. The most recent
comprehensive summary was by Faeth et al. ( 1995). There
have been numerous studies published in the intervening
13 years so a new review is warranted. For the sake of
brevity we focus on efforts completed subsequent to the
article by Pilch and Erdman ( 1987).
Another motivation for this review is the number of
scientiﬁc issues that have arisen in the last dozen or so
years. These include the alternative explanations for the
physical mechanism that leads to sheet-thinning breakup,
and the possibility of placing multi-mode breakup at Weber
numbers between those for bag-and-stamen and sheet
thinning modes. Competing hypotheses for both are pre-
sented here and consistent explanations provided to help
resolve disagreements.
This review covers mostly articles published in archival
journals due to their wider availability. Conference pro-
ceedings and other sources are included when they contain
important conclusions.
The work presented here is restricted to secondary
atomization when the continuous phase is a gas. For those
interested, Pilch and Erdman ( 1987) and Gelfand ( 1996)
have reviewed liquid-liquid secondary atomization. They
found that many aspects are similar to gas-liquid secondary
breakup systems at low density ratios.
The article begins by introducing and comparing the
four experimental systems commonly used to investigate
drop breakup. A criterion for determining when data
obtained using the two most widely used techniques are
compatible is then developed.
The experimentally observed characteristics of second-
ary atomization (i.e., the breakup modes) are summarized,
372 Exp Fluids (2009) 46:371–402
123

<!-- PDF_PAGE: 3 -->

and the initiation and breakup times deﬁned. Non-dimen-
sional groups that have been used to quantify those modes
are introduced; the critical Weber number is deﬁned and its
dependence on Ohnesorge number and other dimensionless
groups discussed.
This is followed by a synthesis of previous experimental
work on Newtonian drop breakup. The ﬁve most com-
monly agreed upon breakup modes are then listed. In each
case a qualitative description precedes an outline of the
underlying physical mechanism and breakup behavior.
Breakup times for all modes are deﬁned and discussed.
The few non-Newtonian studies are then evaluated using
the same framework as for the Newtonian ones (mode
identiﬁcation, qualitative description, physical mechanism,
and behavior; breakup times).
Results from studies on fragment size and velocity dis-
tributions are introduced. Focus then shifts to results from
computational studies. Analytical models are discussed
ﬁrst, and then numerical simulations.
This review closes with suggestions for future work.
2 Characteristics of Newtonian drop secondary
atomization
The earliest studies on secondary breakup were experi-
mental. A number of methods emerged. The three most
popular are (1) shock tubes, (2) continuous jets, and (3)
drop towers. Each method differs by the type of aerody-
namic loading on the drop: shock tubes provide a nearly
spatially uniform step change in relative velocity, drop
towers a gradual change, and continuous jets a shearing
effect. These differences are important because they can
lead to variations in observed behavior.
2.1 Shock tube
A shock tube is divided into two sections by a diaphragm,
as shown in Fig. 1. Pressurized gas is released from the
driver section into the driven section, causing a shock
wave to develop and travel down the tube. Droplets are
inserted into the driven section and their breakup
observed.
The shock rapidly passes over the drop and causes
minimal deformation. Rather, it is the convective ﬂow after
the shock which leads to breakup. In most cases, this
convective ﬂow is sufﬁciently slow such that compress-
ibility effects can be neglected.
The major advantage of shock tube experiments is the
ability to subject a drop to a nearly step change in ambient
ﬂow that is essentially uniform over its surface. This results
in a repeatable experiment that is amenable to theoretical
and computational study.
One disadvantage of this approach is that drops in many
practical systems rarely experience this type of perturba-
tion. Two additional disadvantages of this method are the
low data rate, due to the need to reset the experiment after
every run, and a limited range of operating conditions. In
addition, the need for a compressible ambient ﬂuid means a
gas must be used so experimentation at extreme pressures
or temperatures is difﬁcult. For this reason, most experi-
ments are conducted using air at or around ambient
pressure and temperature.
Studies reviewed here that include original shock tube
results are those of Hinze ( 1955), Ranger and Nicholls
(1969), Gelfand et al. ( 1975), Wierzba and Takayama
(1988), Hsiang and Faeth (1992), Hsiang and Faeth (1993),
Hsiang and Faeth ( 1995), Chou et al. ( 1997), Chou and
Faeth ( 1998), Joseph et al. ( 1999), Igra and Takayama
(2001), Joseph et al. ( 2002), Igra et al. ( 2002), Dai and
Faeth (2001), and Theofanous et al. ( 2004).
2.2 Continuous jet
The continuous jet (see Fig. 2) emerged as an alternative to
the shock tube due to its simplicity and ability to operate
continuously. It also allows fragment size measurement
using optical drop sizing techniques such as phase Doppler
anemometry (PDA).
In an attempt to make the results equivalent to shock
tube experiments, authors shape the nozzle in such a way
as to minimize boundary layers in the free jet so that the
drops experience a more spatially uniform, step change in
velocity. Obviously, if the drop enters the jet too slowly a
Driver section Driven section 
Diaphragm 
Observation 
window
Drop generator 
Fig. 1 A shock tube experimental apparatus
Drop generator 
Nozzle
Fig. 2 A continuous jet experimental apparatus
Exp Fluids (2009) 46:371–402 373
123

<!-- PDF_PAGE: 4 -->

portion of it may break up before the remainder enters the
ﬂow ﬁeld. Such a situation is seen in the work of Arcou-
manis et al. ( 1996). This can lead to results at odds with
those from shock tube studies making direct comparison
quite difﬁcult.
To operate a continuous jet in a manner that produces
results which closely match those from shock tube exper-
iments, it is necessary that drop distortion and breakup
occur almost entirely when the drop is in the jet’s uniform
velocity region. Assuming drops are injected at velocity V
0
perpendicular to a jet having centerline axial velocity U0
and boundary layer thickness d, two criteria must be sat-
isﬁed. First, the initial drop velocity must be low enough to
ensure breakup does not occur outside of the jet. This can
be expressed as:
qaV2
0 d0
r ~\Wec ð1Þ
where Wec is the critical Weber number and is deﬁned in a
subsequent section. Second, the time required for the drop
to pass through the boundary layer must be less than the
time required to initiate breakup. This can be expressed as:
d0 þ dðÞ
V0
U0
e0:5d0
\Tini ð2Þ
where Tini is the initiation time as deﬁned by Eq. 30, and e
is the drop to ambient density ratio. When combined:
1 þ d=d0ðÞ
Tinie0:5 \ V0
U0
\
ﬃﬃﬃﬃﬃﬃﬃﬃ
Wec
We
r
ð3Þ
where We is the drop Weber number, also deﬁned in a
subsequent section.
Using the criteria in Eq. 3 it is possible to evaluate
experimental setups. For example, Fig. 4 from Arcoumanis
et al. ( 1996) shows a droplet of diesel oil ( d0 = 2.6 mm)
breaking up in an air jet ( U0 = 86 m/s, e & 700) such that
We = 400. Assuming the nozzle is well designed, d & 0,
using Eq. 30 from below with Tini = 0.43, and Table 2 with
Wec = 11 yields 7.6 \ V0 \ 14 m/s. The actual injection
velocity is unknown. However, Arcoumanis et al. ( 1996)
indicated drops were produced using a syringe tip and then
allowed to fall due to gravity from 20 mm to 1 m.
Assuming zero initial velocity, no drag, and a 1 m fall
yields V
0* 4.4 m/s, which by Eq. 3 is insufﬁcient to
replicate shock tube behavior.
Papers reviewed here that include original continuous jet
results are those of Liu et al. ( 1993), Liu and Reitz ( 1993,
1997), Arcoumanis et al. ( 1996), Hwang et al. ( 1996),
Prevish and Santavicca (1998), Lee and Reitz ( 1999, 2000,
2001), Go¨kalp et al. ( 2000), Park et al. ( 2006), Cao et al.
(2007), Guildenbecher and Sojka (2007), and Lo´pez-Rivera
and Sojka ( 2008).
2.3 Drop tower
Shock tubes and continuous jets attempt to subject drops to
a step change in velocity. Breakup can also occur if drops
are accelerated more slowly, as by a constant body force,
such as rain drops falling due to gravity. Motivated mostly
by applications to atmospheric sciences, many authors have
studied secondary atomization using a drop tower. In it
drops are allowed to fall under gravity into a quiescent
environment and the subsequent breakup is observed.
2.4 Hybrid methods
Many practical applications involve situations which
are best characterized as a combination of nearly step
acceleration, as seen in shock tubes, and continuous
acceleration, as seen in a drop tower. Because of the
complexity of such processes little experimental data is
available. Two notable exceptions are the works of Shrai-
ber et al. ( 1996) and Schmelz and Walzel ( 2003). Shraiber
et al. ( 1996) allowed drops to fall under the action of
gravity through various air nozzles speciﬁcally designed to
produce non-uniform velocity proﬁles. Schmelz and Wal-
zel (2003) studied the breakup of drops as they fell through
a shaped contraction such that the ambient air signiﬁcantly
accelerated during breakup. The results were found to be
different than either shock tube or drop tower experiments,
and some interesting trends are noted. However, most of
the results are presented as a function of the experimental
geometry and the applicability to other ﬂow conﬁgurations
is unclear.
In summary, the drop tower experiment is probably
closest to ‘‘natural’’ secondary atomization processes for
obvious reasons. However, most man made spray appli-
cations are likely best simulated using either the continuous
jet (e.g., gas turbine injection in which the drops enter a
stream of moving gas) or shock tube (e.g., diesel injection
where rapid gas movement can lead to approximate step
changes in velocity). Finally, the shock tube is superior
from a scientiﬁc perspective because it provides repeatable
and well-characterized initial and boundary conditions for
each drop fragmentation process. For that reason this
review concentrates on secondary breakup due to impul-
sive acceleration as seen in shock tube and some
continuous jet experiments. In addition, results will focus
on gas-liquid systems where the ambient phase is gas.
2.5 Description
Despite the choice of at least three different types of
apparatus, experimental results have revealed common
characteristics in all cases of secondary atomization.
374 Exp Fluids (2009) 46:371–402
123

<!-- PDF_PAGE: 5 -->

The process starts when the drop enters the disruptive
ﬂow ﬁeld. This marks the beginning of the deformation
phase. An unequal pressure distribution, due to accelera-
tion of the ambient ﬂuid around the drop, leads to
deformation from the initial spherical shape. This defor-
mation is resisted by the interfacial tension and viscous
forces. However, if the aerodynamic forces are large
enough the drop will enter the fragmentation phase.
Since fragmentation results from ambient/drop interac-
tions, it is a function of the ﬂow conditions. Differing ﬂow
conditions lead to differing breakup modes, which are often
illustrated by renditions such as those shown in Fig. 3 for
Newtonian drops in shock tube experiments. From top
to bottom the modes are termed vibrational, bag, multi-
mode (often called bag-and-stamen), sheet-thinning, and
catastrophic.
Vibrational breakup is not always observed. It consists
of oscillations at the natural frequency of the drop and
produces only a few fragments whose sizes are comparable
to those of the parent drop.
The bag breakup geometry is composed of a thin hollow
bag attached to a thicker toroidal rim. The bag disintegrates
ﬁrst, followed by the toroidal rim. The former results in a
larger number of small fragments; the latter a smaller
number of large fragments.
Multi-mode (also called bag-and-stamen) breakup is
similar to bag breakup, but with the addition of a stamen
oriented anti-parallel to the direction of the drop motion.
Like bag breakup, the bag is the ﬁrst to disintegrate, fol-
lowed by the rim and the stamen. Fragments of multiple
sizes are produced.
In sheet stripping (or sheet-thinning), a ﬁlm is continu-
ously eroded from the drop surface. It disintegrates rapidly
after being removed. This results in a plethora of small
droplets and, in some cases, a core whose size is compa-
rable to that of the parent drop.
Finally, during catastrophic breakup the drop surface is
corrugated by waves of large amplitude and long wave-
lengths. They form a small number of large fragments that
in turn break up into even smaller units. Some authors
sub-divide this region into wave-crest stripping and cata-
strophic. They attribute mass removal from the drop surface
via large amplitude-small wavelength waves.
Note that both Pilch and Erdman ( 1987) and Hsiang and
Faeth (1992) provide thorough reviews of early investiga-
tions into secondary atomization. Here we adopt the
breakup morphology given by Hsiang and Faeth (1992); the
morphology of Pilch and Erdman (1987) is nearly identical,
differing primarily by the names assigned to each mode.
While the chosen morphology is well established in the
literature, a few exceptions exist. Most notably, Theofa-
nous et al. ( 2004) used a shock tube to study breakup in
highly rareﬁed, supersonic ambient ﬂows and found the
breakup morphology to differ signiﬁcantly from that shown
in Fig. 3 (which is derived mostly from experiments at
subsonic ambient velocities). Additional testing is needed
to conﬁrm their results. Nevertheless, this is an indication
that extrapolation of the experimental results should be
done with caution.
Renditions such as Fig. 3 give the impression that sec-
ondary breakup is an instantaneous process. In reality, mass
is ﬁrst removed from the drop at some time after it is ﬁrst
exposed to the moving ambient ﬂuid. Fragmentation con-
tinues until aerodynamic drag has reduced the relative
velocity between the drop/fragments and the surrounding
ﬂow to a level where disruptive forces are no longer large
enough to overcome the restorative forces. The time when
all fragmentation has ceased is referred to as the total
breakup time, T
tot (Pilch and Erdman 1987).
Figure 4 illustrates some of the breakup modes that are
typically observed in experiments and highlights the fact
that secondary breakup is a rate process that occurs over a
ﬁnite time.
2.6 Non-dimensional groups
In general, multiple physical processes and ﬂuid properties
are important in secondary breakup phenomena. This is
demonstrated in Figs. 3 and 4 by the variety of breakup
modes that have been reported.
In addition, the breakup geometries can be highly
complicated with multiple entities, re-entrant and other
topologically complex surfaces, plus multiple length and
time scales. This makes mathematical and numerical
analysis very challenging, especially in the early days of
this ﬁeld.
Fig. 3 Newtonian drop breakup morphology
Exp Fluids (2009) 46:371–402 375
123

<!-- PDF_PAGE: 6 -->

Past researchers therefore described their ﬁndings in
terms of a number of non-dimensional groups. They are
still in use today, and most authors make use of one or
more of those listed in Table 1. The logic behind their
choice is as follows.
In secondary atomization the aerodynamic forces deform
a drop causing it to fragment. This deformation is resisted
by the surface tension, which tends to restore the drop to a
spherical shape. As a result the Weber number, We, deﬁned
as the ratio of the disrupting aerodynamic forces to the
restorative surface tension forces, is the most important
parameter when describing secondary atomization. A larger
We indicates a higher tendency toward fragmentation.
Drop viscosity hinders deformation and also dissipates
energy supplied by aerodynamic forces. Both factors
reduce the likelihood of fragmentation. To account for this,
many authors make use of the Ohnesorge number, Oh,
which represents the ratio of drop viscous forces to surface
tension forces. A higher Oh indicates a lower tendency
toward fragmentation. The Laplace number, La, is used in
some works ( La = Oh
-2).
Other important dimensionless groups are the Reyonlds
number, Re, which is the ratio of aerodynamic forces to
ambient viscous forces, the drop phase-to-ambient phase
density ratio, e, and drop phase-to-ambient phase viscosity
ratio, M. Note that Re is equal to We0.5Oh-1e-0.5 N.
Finally, the Mach number, Ma, is important when consid-
ering compressibility effects.
As pointed out by Shraiber et al. (1996) this list does not
encompass all physical processes that may play a role in
secondary atomization. Turbulence within the two ﬂuids
may create additional forces that destabilize drops. In
addition, unsteady ambient ﬂow could be considered by
accounting for the time that the disruptive forces act on the
drop and/or accounting for the rate of change of these
forces. Gelfand (1996) cited experimental evidence that the
duration of the disruptive ﬂow must be sufﬁcient to lead to
breakup. Furthermore, as noted by Clift et al. ( 1978), one
could consider impurities and particulates that may serve as
initiation points for breakup.
When studying temporal phenomena, experimentally
observed times are typically made non-dimensional using
the characteristic transport time given by Ranger and
Nicholls (1969), which is derived from analysis of the drop
displacement assuming constant acceleration due to drag:
T ¼ t
U0
e0:5d0
ð4Þ
Here T is the dimensionless time, t is the dimensional time,
U0 is the initial relative velocity between drop and ambient,
Fig. 4 Shadowgraphs of
Newtonian drop secondary
breakup. Time increases from
left to right, disruptive forces
increase from top to bottom
Table 1 Dimensionless groups important in secondary breakup
Weber number We qaU2
0 d0
r
Ohnesorge number Oh ldﬃﬃﬃﬃﬃﬃﬃﬃ ﬃ
qdd0r
p
Reynolds number Re qaU0d0
la
Density ratio e qd
qa
Viscosity ratio M ld
la
Mach number Ma U0
c
376 Exp Fluids (2009) 46:371–402
123

<!-- PDF_PAGE: 7 -->

e is the drop-to-ambient density ratio, and d0 is the initial
spherical diameter. As ﬁrst noted by Ranger and Nicholls
(1969) this choice of characteristic time is not appropri-
ate to describe all temporal phenomena in secondary
atomization and authors have proposed alternatives. As
examples, Shraiber et al. ( 1996) suggested non-dimen-
sionalizing by the drop oscillation period while Faeth et al.
(1995) suggested using a viscous timescale for drops at
high Oh. Scaling by liquid relaxation or retardation time
might be more appropriate for non-Newtonian ﬂuids
exhibiting elasticity.
2.7 Transition We (low Oh)
For a given drop size and ﬂuid properties, experiments
conducted at increased relative velocities result in a con-
tinuous transition between breakup modes. However, for
simpliﬁcation most authors have assumed transition occurs
abruptly.
Most investigators have found the transition between
two modes to be a function of We and Oh and independent
of other parameters such as the density ratio ( e) or Re.
However, it is important to note that this may be due to the
limited ranges of such parameters that can easily be
achieved in experiments.
Regardless, numerous experiments have shown that the
transition We between pairs of breakup modes are essen-
tially constant for Oh\ 0.1 and can be approximated by
the values provided in Table 2.
As noted in the discussion of Fig. 4, regime transition is
actually a continuous process, so the values of the transi-
tion We are subjective and different authors have reported
different magnitudes. For example Pilch and Erdman
(1987) reported transition between multimode and sheet-
thinning at We = 100, while Hsiang and Faeth ( 1992)
choose We = 80, and Gelfand ( 1996) found We = 40.
In Table 2 the values of Hsiang and Faeth ( 1992) are
reported with the exception of the transition between sheet-
thinning and catastrophic, which was taken from the work
of Pilch and Erdman ( 1987), and the transition between
vibrational and bag, which is an average of numerous
authors. Reasons for these choices will be discussed in a
subsequent section.
2.8 Dependency on Oh
While it is true that Weber numbers demarking breakup
mode boundaries are independent of Oh for Oh\ 0.1, that
is not true for higher Oh conditions. As noted by Faeth
et al. ( 1995), in many high-pressure spray applications the
drop phase approaches the thermodynamic critical point
where Oh increases rapidly as the surface tension approa-
ches zero and the density ratio decreases. At these elevated
Oh, the observed breakup modes remain the same, but
experiments have shown an increase in the transitional We
values listed in Table 2. According to Hsiang and Faeth
(1992) this is because the increased drop viscosity dissi-
pates energy, which slows drop distortion and allows more
time for aerodynamic drag to reduce the relative velocity.
No Oh has been observed for which breakup is impos-
sible. Take, for example, the extreme case of Joseph et al.
(1999) who performed shock tube experiments at some of
the highest recorded values of We and Oh. Bag breakup
was observed at We = 160,000 and Oh = 26.6. In contrast,
for Oh\ 0.1 bag breakup is expected to end at We = 35.
The relation between transitional We and Oh is often
plotted as shown in Fig. 5 (Hsiang and Faeth 1995). A
number of experimental correlations have been proposed to
describe this behavior. Most have focused on the critical
Weber number, We
c, deﬁned as the We at the start of bag
breakup. However, as can be seen in Fig. 5 the behavior for
other transitional We is similar.
To describe Wec, Brodkey ( 1967) proposed the follow-
ing correlation, which Pilch and Erdman ( 1987) conﬁrmed
for Oh\ 10:
Wec ¼ WecOh!0 1 þ 1:077Oh1:6/C0/C1
Oh\10 ð5Þ
Here WecOh?0 is the critical We at low Oh, as given in
Table 2. Similarly, Gelfand ( 1996) reviewed mostly
Russian works and proposed:
Wec ¼ WecOh!0 1 þ 1:5Oh0:74/C0/C1
Oh\4:0 ð6Þ
These correlations are compared in Fig. 6. Clearly at
Oh[ 3 they do not agree with one another.
The inaccuracies in experimentally determined correla-
tions have led many to seek relations based at least
partially on the assumed underlying physical mechanisms.
For example, Cohen ( 1994) assumed that in the absence of
drop viscosity the kinetic energy imparted by the ambient
ﬂow to the drop is equal to the surface energy. An extra
energy term was added to account for the drop viscosity,
therefore increasing the kinetic energy needed to cause
breakup. The result was:
We ¼ We
cOh!0 1 þ C /C1OhðÞ ð 7Þ
where C has a value between 1.0 and 1.8 that is theorized
to be dependent on the breakup regime.
Table 2 Transition We for Newtonian drops with Oh\ 0.1
Vibrational 0 \ We\ *11
Bag *11\ We\ *35
Multimode *35\ We\ *80
Sheet-thinning *80\ We\ *350
Catastrophic We[ *350
Exp Fluids (2009) 46:371–402 377
123

<!-- PDF_PAGE: 8 -->

Similar to Cohen ( 1994), Hsiang and Faeth ( 1995)
performed a phenomenological analysis in which they
assumed the instantaneous We must reach a certain critical
value for regime transition to occur. They also determined
that the transition We are approximately linear functions of
Oh for high Oh values.
Going further, Aalburg et al. ( 2003) noted that at very
high Oh the effect of surface tension becomes negligible,
and at the critical condition drop viscous forces balance
aerodynamic forces. They suggested a new regime map
complimentary to Fig. 5 where the ratio We
1/2/Oh (equiv-
alent to Re based on drop phase viscosity) becomes
constant for Oh /C29 1.
Despite these works, no published correlation is known
to be accurate at Oh[ 1, so more work is needed.
2.9 Dependency on other non-dimensional parameters
Some authors have observed a dependence of Wec on other
quantities. For example, an increase in Wec as the drop
density approaches the ambient density was observed in the
direct numerical simulations of Han and Tryggvason
(1999, 2001) and Aalburg et al. (2003), who also noted that
many properties of secondary atomization became essen-
tially independent of density ratio for e[ 32. Gelfand
(1996) reviewed liquid–liquid systems where the density
ratio is nearly unity and reported a We
c of 17, somewhat
higher than the value of 11 for gas–liquid systems given in
Table 2. This indicates that gas–liquid systems may behave
similarly to liquid–liquid systems at extremely low density
ratios. Such density ratios may be found in direct diesel
injection. However, no experimental gas-liquid results are
known to exist for e\ 32.
In addition, Aalburg et al. ( 2003) used numerical sim-
ulation to study drop deformation at low Re. They found a
signiﬁcant change in We
c in the Stokes ﬂow regime
(Re\ 100) and almost no dependence on Re for Re [ 100.
Fig. 5 We at transition.
Reprinted from Hsiang LP,
Faeth GM ( 1995) Drop
deformation and breakup due to
shock wave and steady
disturbances. International
Journal of Muliphase Flow, vol
21(4):545–560, with permission
from Elsevier
10
-3
10
-2
10
-1
10
0
10
1
Ohnesorge number, Oh
0
10
20
30
40
50
Wec /Wec Oh 0
Brodkey (1967)
Gelfand (1996)
Fig. 6 Wec, from Eqs. 5 and 6
378 Exp Fluids (2009) 46:371–402
123

<!-- PDF_PAGE: 9 -->

Hsiang and Faeth ( 1995) state that some dependence of
Wec on Re has been seen for liquid-liquid drop tower
experiments. However, no shock tube data is known to
exist for such low Re. Consequently, more work is needed
to simulate low Re drop motion in gas-liquid systems.
3 Drop deformation and vibrational breakup
3.1 Qualitative description
The earliest stage of secondary atomization is drop defor-
mation into a shape that can be approximated as an oblate
ellipsoid. This is illustrated in Fig. 7. Here d
str is the
deformed drop diameter in the stream-wise direction and
d
cro is the deformed drop diameter in the cross-stream
direction.
If the aerodynamic forces are large enough the drop will
continuously deform until it begins to fragment via one of
the modes illustrated in Fig. 3 (Hsiang and Faeth 1992).
However, if the aerodynamic forces are insufﬁcient then
surface tension may lead to oscillation at the drop natural
frequency, which depending on ﬂow conditions may be
either stable or unstable (Hsiang and Faeth 1992). When it
is unstable the drop eventually breaks apart into a few large
fragments. This is referred to as vibrational breakup. As
noted by Pilch and Erdman ( 1987), this breakup mode
proceeds much more slowly than other modes and does not
lead to small ﬁnal fragment sizes. As a result, most authors
ignore vibrational breakup and consider bag breakup to be
the ﬁrst secondary atomization mode. For that reason few
authors have studied virbrational breakup in detail.
Nevertheless, the study of deformation is important
because it is the ﬁrst stage of all aerodynamically induced
fragmentation. Also, drop deformation has been shown to
signiﬁcantly affect the drag and hence the trajectory.
Therefore, a thorough understanding of the process is
necessary to create accurate secondary atomization models.
3.2 Physical mechanism
Deformation is caused by an unequal static pressure dis-
tribution over the drop surface. Assuming an inviscid ﬂuid,
the forward and rear stagnation points on the drop are at a
higher static pressure compared to ﬂow around the drop
periphery. This causes the drop to expand laterally and
compress in the gas ﬂow direction. The presence of a wake
will alter the static pressure distribution; nevertheless,
qualitatively similar deformation has been observed.
3.3 Behavior
Early attempts to model the deformation process approxi-
mated the changes in drop shape and drag using an average
drag coefﬁcient based on the initial spherical diameter, /C22C
D;
such that the average drag force was given by:
FD ¼ 1
2qaU2
0 /C22CD
pd2
0
4 ð8Þ
The reviews of Pilch and Erdman ( 1987) and Gelfand
(1996) report various values of /C22CD that are applicable
throughout given ranges of We, Re, and Ma. Ortiz et al.
(2004) used such data to create the following correlation:
/C22CD ¼ 1:6 þ 0:4Oh0:08We0:01 ð9Þ
1000\We\162000; Oh\0:44; 0:95\Ma\1:63
Correlations for /C22CD such as Eq.9 may be useful to predict
the drop velocity and position at the end of the deformation
stage. However, as ﬁrst noted by Pilch and Erdman ( 1987)
they do a poor job of predicting the instantaneous
acceleration, knowledge of which is needed for some of
the instability models used to predict secondary atomization.
3.4 Deformation
To improve accuracy many authors have deﬁned the drag
coefﬁcient as a function of deformation, such that the
instantaneous drag is given by:
F
D ¼ 1
2qaU2
0 CD
pd2
cro
4 ð10Þ
where CD is the instantaneous drag coefﬁcient. However,
doing so also requires knowledge of the deformation versus
time.
Hsiang and Faeth ( 1992) measured d
cro and found it to
increase approximately linearly as a function of time until
fragmentation begins at T
ini. A phenomenological analysis
which considered the interaction between surface tension
and pressure forces resulted in the following:
dcro
dstr
Ambient flow 
direction
d0
Fig. 7 Rendition of a deformed/vibrating drop
Exp Fluids (2009) 46:371–402 379
123

<!-- PDF_PAGE: 10 -->

dcro=d0ðÞ max¼ 1 þ 0:19We1=2 We\102; Oh\0:1; ð11Þ
Here ( dcro/d0)max is the maximum deformation, which
occurs at Tini.
At higher Oh the authors found that the maximum
deformation at a given We decreased. It was postulated this
was due to the slowing of the rate of deformation which
reduces the relative velocity and hence the maximum
deformation.
Helenbrook and Edwards ( 2002) used computational
ﬂuid dynamics to simulate over 3000 drops at their ter-
minal velocity and reported the following relation between
deformation and ﬂow conditions:
d
str=dcroðÞ max¼ 1 /C0 0:11We0:82 þ 0:013e0:5N/C0 1Oh0:55We1:1
ð12Þ
We\10; Oh\10; 5\e\500; 5\N\15; Re\200;
Unfortunately their work is more applicable to drop
tower than shock tube experiments. A similar analysis for
impulsively accelerated drops is therefore warranted.
Finally, compared to the actual fragmentation event, the
physics involved in drop deformation are relatively simple.
This has led many to develop analytic predictive models
for drop deformation that are widely used in spray simu-
lations. Examples include the Taylor analogy breakup
(TAB) model of O’Rourke and Amsden ( 1987) and the
droplet deformation and breakup (DDB) model of Ibrahim
et al. (1993). These and other such models are discussed in
a subsequent section.
3.5 Drag
No matter how droplet deformation is found, a relation
between deformation and drag is needed to determine the
acceleration. The literature has identiﬁed three main factors
that affect overall drag: (1) geometry, (2) internal circula-
tion, and (3) unsteady effects. Here we will assume
e /C29 1 such that the unsteady effects of virtual mass and
Basset history forces can be neglected.
Hsiang and Faeth ( 1992, 1995) performed shock tube
experiments and found that the instantaneous coefﬁcient of
drag, C
D, can be approximated by a linear interpolation
between the steady state value for a solid sphere and for a
solid disk with both evaluated at equal Re. For the range of
properties considered in their experiment, this indicates
that internal circulation effects are minimal.
Liu et al. ( 1993) proposed:
CD
/C14
CD/C0 sphere ¼ 1 þ 2:632yðÞ ð 13Þ
which gives the coefﬁcient of drag as a linear function
of deformation. Here y is the non-dimensional dis-
placement of the drop equator, which can be written as
y = 1 - (d0/dcro)2, and CD-sphere is the coefﬁcient of drag
for a sphere at the same Reynolds number. Note that for no
deformation (y = 0) the coefﬁcient of drag of a sphere is
recovered, and for a fully deformed drop ( y = 1) the
coefﬁcient of drag of a disk is recovered.
Equation 13 can be improved by incorporating results
from actual ellipsoidal shapes. A recent example is that
of O’Donnell and Helenbrook ( 2005) who performed
numerical calculations for drag over a solid ellipsoid. They
proposed a correlation based on interpolation between drag
on a sphere, ellipsoid with d
cro = 2dstr, and a disk, which
was shown to be accurate within 1.5% for Re\ 200. The
interested reader is referred to O’Donnell and Helenbrook
(2005) for the complete correlation. Further experimental
or numerical results are needed to extend this correlation to
Reynolds numbers on the order of 10
2 to 10 4, which are
present in many spray applications.
Some attempts have been made to quantify the second
order effects of internal circulation and unsteady ﬂow on
drag. Helenbrook and Edwards ( 2002) used numerical
analysis to divide the deviation from solid sphere drag into
the effects of deformation and those of internal circulation.
In the limit of low We, the effects of deformation were
negligible resulting in the following correlation for the
change in coefﬁcient of drag due to internal circulation:
C
D
/C14
CD/C0 sphere ¼ 2 þ 3N
3 þ 3N
/C18/C19
1 /C0 0:03N/C0 1Re0:65/C0/C1
ð14Þ
5\e\500; 5\N\15; Re\200
Because this equation was derived for a spherical drop,
its applicability to a highly deformed drop is unclear.
Finally, it is important to emphasize that the above
correlations are for steady ﬂow while in reality a drop is
continuously accelerating and deforming. Clift et al. (1978)
discuss virtual mass and Basset history effects for ellip-
soidal shapes, but do not include the effects of transient
deformation. Recently these effects were included in
numerical simulations such as those by Quan and Schmidt
(2006), which have shown that the unsteady drag is higher
than the steady drag. To date, no correlations exist to
predict this phenomenon and more work is needed.
4 Bag breakup (and critical We)
4.1 Qualitative description
Chou and Faeth ( 1998) divided bag breakup into four
stages: (1) deformation, during which the drop evolves
from its initial spherical shape into an oblate spheroid, (2)
bag growth, during which the center of the drop gets blown
downstream and forms a hollow bag attached to a toroidal
ring, (3) bag breakup, where the bag bursts forming a large
380 Exp Fluids (2009) 46:371–402
123

<!-- PDF_PAGE: 11 -->

number of small fragments, and ﬁnally (4) ring breakup,
where the toroidal ring forms a small number of large
fragments. The ﬁrst row in Fig. 4 illustrates typical bag
breakup.
4.2 Physical mechanism
As in all cases of secondary atomization, bag breakup
involves times on the order of ms, spatial dimensions on
the order of lm, and unsteady, accelerating ﬂows. There-
fore no experimental investigations have been capable of
measuring the local drop and ambient ﬂow ﬁelds that lead
to the formation and disintegration of the bag structure.
However, recent developments in direct numerical simu-
lation (DNS) of multiphase ﬂows have provided some
insight.
Han and Tryggvason (1999, 2001) used DNS to observe
the formation of the bag structure due to separation in the
ambient ﬂow which leads to a pressure differential
between the front stagnation point and the wake (see
Fig. 8). This indicates that bag development has some
dependency on Re and may not be observed under very
low Re conditions.
In another study, Chou and Faeth (1998) discovered that
after the bag formed the toroidal ring continued to grow at
an expanding rate. This is a result of the outward force
exerted on the bag and ring from the high pressure stag-
nation ﬂow within the bag. After the bag ruptures, the ring
continues to grow, but at a constant rate until it is no longer
stable and breaks apart.
The mechanism leading to fragmentation of the bag is
not well understood. Hwang et al. ( 1996) noted that the
bag ﬁrst breaks into ligaments that are aligned with the
ﬂow direction. For this reason the breakup of the bag
cannot be explained as a capillary instability, which
would predict ligaments perpendicular to the ﬂow direc-
tion. Liu and Reitz ( 1997) postulated that small holes
form in the bag due either to local disturbances in the
ambient ﬂow ﬁeld or particulate impurities in the drop
ﬂuid. These holes would serve as inception sites for
breakup.
4.3 Critical Weber number
Experimental evidence has consistently shown that once a
given drop size and ﬂuid properties are speciﬁed bag
breakup occurs at a lower ambient velocity than any other
breakup mode. As a result the study of bag breakup is
especially important because it establishes the criteria for
the onset of secondary atomization. For this reason the We
value marking the beginning of bag breakup is typically
referred to as the critical We, We
c.
As noted in the discussion of breakup morphology, the
determination of regime transitions is somewhat arbitrary
and different authors have reported different values.
However, an important exception is the critical Weber
number. For shock tube experiments in the limit of
Oh\ 0.1 all authors have reported a value of We
c =
11 ± 2. This, along with the fact that Wec marks the start
of secondary breakup, is an important means of checking
atomization models and direct numerical simulations. Any
model or simulation that is unable to reproduce We
c is
unlikely to correctly represent the physical mechanisms
involved in drop breakup.
Attempts have been made to calculate We
c.
Tarnogrodzki (1993) assumed the drop deforms into a ﬂat
disk with rounded ends. A duct ﬂow solution was used to
estimate the pressure within the ﬂat part of the drop, and
the surface tension force was used to ﬁnd the pressure
within the rounded part. Drag coefﬁcients for a disk and
sphere were used to approximate the dynamic pressure
acting on the drop, which resulted in a solution of defor-
mation versus time. Finally, breakup was assumed to
occur when the radial motion of the drop ceased. While
the model was able to calculate We
c to within the correct
order of magnitude, it predicted that Wec continuously
decreased with Oh, even for Oh\ 0.1. This is in stark
contrast to the experimental observation of constant Wec
for Oh\ 0.1 and an increase in Wec with an increase in
Oh for higher Oh values.
Analyses, such as this, that involve a number of untested
assumptions, in general do a poor job of predicting the
complicated physics of secondary atomization. At this
time, direct numerical simulation of the Navier-Stokes
equations is the best known method of theoretically
studying the process.
Fig. 8 Bag breakup mechanism, based on the ﬁndings of Han and
Tryggvason (1999, 2001)
Exp Fluids (2009) 46:371–402 381
123

<!-- PDF_PAGE: 12 -->

4.4 Behavior
Chou and Faeth (1998) studied the behavior of bag breakup
in detail and found the four periods of bag breakup occur
within the approximate non-dimensional times given in
Table 3.
In addition they measured the cross stream diameter,
d
cro, of the expanding toroidal ring resulting in the fol-
lowing correlations.
Study of the properties of the toroidal ring is crucial
because it contains approximately 60% of the original
volume, as reported by Chou and Faeth ( 1998). Also, the
fragments formed from the toroidal ring are much larger
than those formed from breakup of the bag; Chou and
Faeth (1998) reported the diameter of the fragments formed
from ring breakup are on average 30% of the original drop
diameter while the mean diameter of the fragments formed
from breakup of the bag is approximately 4% of the ori-
ginal drop diameter. The larger fragments dominate
subsequent evaporation rates which are crucial to the per-
formance of many spray-related systems.
5 Sheet-thinning breakup
5.1 Qualitative description
Sheet-thinning breakup occurs at higher initial relative
velocities than bag breakup, and proceeds in a markedly
different fashion. Following initial deformation, ligaments
are stripped from the periphery of the drop where they
break up into a multitude of small fragments. The process
continues until the drop is completely fragmented, or until
it has accelerated to the point at which aerodynamic forces
are negligible. In the latter case, Hsiang and Faeth ( 1992)
note that a drop core may remain at the completion of
secondary atomization. The second row in Fig. 4 illustrates
typical sheet-thinning breakup.
5.2 Physical mechanism (shear vs. sheet-thinning)
The physical process responsible for this mode is a point
of controversy. Two distinct mechanisms have been put
forth: (1) the ‘‘shear stripping’’ mechanism of Ranger and
Nicholls (1969) and (2) the ‘‘sheet-thinning’’ mechanism of
Liu and Reitz ( 1997).
Ranger and Nicholls ( 1969) postulated that shear from
the ambient ﬂow over the deformed drop results in the
formation of a boundary layer inside its surface. This
boundary layer becomes unstable at the drop periphery
resulting in stripping of mass. The mechanism is typically
referred to as ‘‘boundary-layer stripping’’ or ‘‘shear strip-
ping’’ and is illustrated in Fig. 9.
Chou et al. ( 1997) performed shock tube measurements
of breakup and noted that drop viscosity signiﬁcantly
increased fragment sizes (ligaments and micro-drops), even
in the range of Oh\ 0.1. They considered this to be evi-
dence in support of the shear stripping mechanism. In
addition, they noted a transient period for drops of low
viscosity in which the diameter of the fragments increased
Table 3 Temporal evolution of bag breakup for Oh \ 0.1 (Chou and
Faeth 1998)
Deformation 0 \ T\ 2
Bag growth 2 \ T\ 3
Bag breakup 3 \ T\ 4
Ring breakup 4 \ T\ 5
Fig. 9 Shear stripping breakup mechanism
dcro=d0 ¼ 1:0 þ 0:5T 0\T\21 3 \We\20;
dcro=d0 ¼ 0:25T2 /C0 0:18T þ 1:43 2 \T\40 :0043\Oh\0:0427;
dcro=d0 ¼ 1:79T /C0 2:51 4 \T\5 633 \e\893;
1550\Re\2150
ð15Þ
382 Exp Fluids (2009) 46:371–402
123

<!-- PDF_PAGE: 13 -->

with time due to temporal growth of the boundary-layer. A
phenomenological analysis was conducted which was able
to predict the observed dependence on viscosity.
Igra and Takayama (2001) and Igra et al. ( 2002) studied
breakup of a cylindrical water column in a shock tube.
Their experimental setup allowed for visualization of
density changes inside the liquid column using interfer-
ometeric fringes. After the initial deformation stage, no
fringes were seen in the liquid column, which the authors
interpreted as a uniform pressure ﬁeld within the drop.
They also observed breakup to be qualitatively similar to
shear breakup of a spherical drop. These ﬁndings lead them
to conclude that the drop must be fragmenting due to some
effect other than pressure variations, thereby supporting the
boundary layer stripping hypothesis. It is important to note
that the fringe resolution of their systems was limited;
therefore, the validity of these conclusions is questionable.
Using a model of boundary layer development attributed
to Taylor ( 1963), Ranger and Nicholls ( 1969) proposed a
model for the rate of liquid removal from a drop. Using a
similar analysis, it is possible to compare the magnitude of
the viscous force (shear) to the aerodynamic drag force
(sheet-thinning). Here it is assumed that (1) the drop
remains spherical, (2) there is zero internal circulation
within the drop, (3) the size of the boundary layer is much
less than the drop diameter so the drop curvature can be
neglected in the momentum integral equations, (4) the
pressure gradient term is neglected in the momentum
integral equations, (5) the ambient velocity perpendicular
to the surface is given by potential ﬂow over a sphere, and
(6) shear stripping occurs at the drop periphery. Conse-
quently, only a half drop will be considered.
Figure 10 illustrates the problem. Boundary layer
development is assumed to be symmetric such that
r = d
0 sin (2x/d0)/2. ud(y) and ua(y) are the drop and
ambient phase boundary layer velocities, which Taylor
(1963) approximated as:
ud
U ¼ Ae/C0 y=ad
ﬃﬃxp
ð16Þ
ua
U ¼ 1 /C0ð 1 /C0 AÞe/C0 y=aa
ﬃﬃxp
ð17Þ
U is the ambient velocity perpendicular to the drop surface
and is given by U = 3U0 sin (2x/d0)/2.
In this case the momentum integral equations reduce to:
qa
o
ox
Z1
0
uaðU /C0 uaÞdy ¼ la
oua
oy
/C18/C19
y¼0
ð18Þ
qd
o
ox
Z1
0
u2
ddy ¼/C0 ld
oud
oy
/C18/C19
y¼0
ð19Þ
Equating the shear stress at the boundary and assuming
A /C28 1, Taylor ( 1963) showed A3 = (Ne)-1 and ad ¼ﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ ﬃ
ld=AqdU
p
: Finally the shear force on the drop surface is
given by:
Fl ¼
Z
A
swdA ð20Þ
where A is the half drop surface area and sw =- ld( qud/
qy)y=0. Performing the integration and dividing into the
drag force given by Equ. 8:
FD
Fl
¼ 0:1375 /C22Cd
ﬃﬃﬃﬃﬃ ﬃ
Re
p
ð21Þ
Reﬁnement of the model to include the effects of the
pressure gradient, drop deformation, and internal circulation
are expected to affect the leading coefﬁcient in Eq. 21
without altering the functional dependence on Re.
As in the analysis of Ranger and Nicholls ( 1969), the
boundary layer stripping model is found to be a function of
Re and can be expected to dominate the aerodynamic
forces as Re decreases. However, this contradicts experi-
mental data which indicate this breakup mode is essentially
independent of Re.
Most experimental data are reported in terms of We and
Oh. For that reason it can be shown that:
FD
Fl
¼ 0:1375 /C22CdWe1=4Oh/C0 1=2e/C0 1=4N1=2 ð22Þ
Assuming constant material properties, the role of the
viscous force will increase with decreasing We and
increasing Oh. This is opposite to the experimentally
observed trends, which indicate this breakup mode occurs
at higher values of We and lower values of Oh.
Liu and Reitz ( 1997) noted the discrepancy between
experimentally observed trends and those given in Eqs. 21
U0
y
y x
r
d0
ud (y)
ua (y)
Fig. 10 Boundary layer breakup model
Exp Fluids (2009) 46:371–402 383
123

<!-- PDF_PAGE: 14 -->

and 22. As an alternative, they proposed the ‘‘sheet-thin-
ning’’ mechanism in which the ambient phase inertia
causes the periphery of the deformed drop to be deﬂected
in the direction of the ﬂow thereby forming a sheet.
Following this, the sheet breaks into ligaments and then
individual fragments. As in bag type breakup ambient
phase viscosity must be present to cause ﬂow separation
and the formation of a wake. However, because the drop
is deformed into a disk-like shape ﬂow separation is
expected to occur at all practical values of Re. Conse-
quently, the sheet-thinning mechanism is considered an
inviscid phenomenon with no dependence on Re.T h i s
mechanism is consistent with their experimental obser-
vations and is further discussed in the works of Lee and
Reitz (1999) and Lee and Reitz ( 2001). It is illustrated in
Fig. 11.
In addition to being supported by the experimental
observation that this breakup mode does not depend on Re
(Liu and Reitz 1997, Lee and Reitz, 2000), the sheet-
thinning mechanism is supported by a number of recent
numerical simulations.
Han and Tryggvason ( 1999, 2001) observed ﬂow
structures similar to sheet-thinning type breakup, even in
the limit of zero drop viscosity. Furthermore, they pro-
posed that strong vorticity and backﬂow in the wake
prevents the formation of the bag structure and the drop
edge is eventually pulled back by the ﬂow.
Khosla et al. (2006) performed a volume of ﬂuid (VOF)
simulation in which the spatial resolution was ﬁne enough
to resolve the drop phase boundary layer so the actual
breakup event was simulated. The results were very similar
to the sheet-thinning mechanism.
Wadhwa et al. ( 2007) performed numerical simulation
of drop deformation at We = 100. Although the actual
breakup event was not simulated, ﬁgures provided in the
paper seem to show the thin deformed edge of the drop
being pinched off as it becomes entrained in the recircu-
lation behind the drop. This interpretation of numerical
results supports the sheet-thinning mechanism.
Given the recent insight provided by accurate DNS, it
can be concluded that the shear stripping model is incor-
rect, and this breakup regime is actually the result of sheet-
thinning. The dependence of fragment sizes on drop phase
viscosity as observed by Chou et al. ( 1997), which was
originally explained using the shear stripping model, can
also be attributed to instabilities which lead to the breakup
of the sheet into ligaments and fragments and therefore can
also be explained using the sheet-thinning mechanism. In
addition, the sheet-thinning mechanism may better explain
breakup in the transitional multimode regime, a detailed
discussion of which is given in the section on multimode
breakup.
5.3 Behavior
Hsiang and Faeth ( 1993) performed a phenomenological
analysis to relate the relative velocity of the core drop after
breakup, U
core, to experimental conditions:
U0 /C0 Ucore
U0
e1=2 1 þ 3CðÞ ¼ 3
4
/C22CDTtot ð23Þ
where C ¼ 3 /C22CDTtot
/C14
4e1=2 and /C22CD is an average coefﬁcient
of drag, which Hsiang and Faeth ( 1993) suggested be
approximately 5. In addition, Chou et al. ( 1997) gave a
correlation for the mean relative velocity of the fragments
that is based on the velocity of the core drop:
/C22Uf ¼ Ucore þ 9:5e/C0 1=2 U0 /C0 UcoreðÞ /C22Vf ¼ 0 ð24Þ
125\We\375; 0:003\Oh\0:04; 3000\Re\12000;
670\e\990
Here /C22Uf is the mean relative velocity of the fragments in
the stream-wise direction and /C22Vf is the mean relative
velocity of the fragments in the cross-stream direction.
Finally, Hsiang and Faeth ( 1993) noted that the drop
core has a ﬁnal We greater than Wec for the onset of sec-
ondary atomization in shock tube experiments. Assuming
the criteria for the end of sheet-thinning is more closely
related to that for gradually accelerating drops, such as
those in a drop tower, Hsiang and Faeth ( 1993) derived an
expression for the drop core We at the end of sheet-thinning
breakup:
We
core ¼ 4EocrWe=3 /C22CDðÞ 1=2
1 þ C ð25Þ
where Eocr is the Eo¨tvo¨s number ðEocr ¼ a qd /C0 qajj d2
core
/C14
rÞ
at the end of sheet-thinning breakup, which Hsiang and
Faeth (1993) suggested could be taken to be 16. Combining
Fig. 11 Sheet-thinning breakup mechanism
384 Exp Fluids (2009) 46:371–402
123

<!-- PDF_PAGE: 15 -->

Eqs. 23 to 25 with knowledge of the drag coefﬁcient
and total breakup time, it is possible to calculate the
velocity of the fragments and drop core along with the core
diameter after sheet-thinning type breakup. Discussion of
the size distribution of fragments is deferred to a later
section.
6 Multimode
6.1 Qualitative description
Figure 12 illustrates the transition between bag breakup
and sheet-thinning breakup. Here We increases from left to
right.
A number of authors have proposed different modes to
describe this transition. Pilch and Erdman ( 1987) term it
‘‘bag-and-stamen’’ mode. Cao et al. (2007) deﬁned a ‘‘dual-
bag breakup regime’’, which they identiﬁed as unique, but
can easily be considered one stage of the transition between
bag and sheet-thinning breakup. Here the term ‘‘multi-
mode’’ breakup, due to Hsiang and Faeth ( 1992), will be
used.
Dai and Faeth ( 2001) divided the multimode breakup
regime into ‘‘bag/plume’’ breakup and ‘‘plume/shear’’
breakup, which will be referred to here as ‘‘plume/sheet-
thinning’’ breakup. During bag/plume breakup a bag forms
as in bag breakup. However, the center core is blown
downstream more slowly resulting in the formation of a so
called plume. This is similar to the bag-and-stamen
breakup regime originally described by Pilch and Erdman
(1987). Figure 13 shows typical bag/plume breakup.
Plume/sheet-thinning breakup differs from bag/plume
breakup in that no bag is formed. Rather drops are stripped
continuously from the plume in a manner similar to sheet-
thinning breakup. Figure 14 shows typical plume/sheet-
thinning breakup.
Dai and Faeth ( 2001) suggest that bag/plume breakup
occurs for *18\ We\ *40, and plume/sheet-thinning
occurs for *40\ We\ *80, both with Oh\ 0.1. These
choices provide signiﬁcant overlap with transition We for
bag breakup, as given in Table 2. This again highlights the
fact that the transition between breakup modes is actually a
continuous process and a single transition We value is an
over-simpliﬁcation.
6.2 Physical mechanism
Given the historically accepted descriptions of shear
breakup due to boundary layer growth and bag breakup due
to aerodynamic drag, little consideration has been given to
the mechanism leading to multimode breakup. Rather it has
been assumed to occur when both aerodynamic effects and
shear effects are signiﬁcant.
In contrast, if one adopts the sheet-thinning description,
both sheet-thinning and bag breakup result from aero-
dynamic forces. In this case, a new explanation for the
transition regime is needed. In addition, one must address
why bag type breakup is seen at low levels of aerodynamic
forces and sheet-thinning is seen at higher levels. Currently
two theories exist: ‘‘the combined Rayleigh–Taylor/aero-
dynamic drag’’ mechanism and the ‘‘internal ﬂow’’
mechanism.
Theofanous et al. (2004) studied Rayleigh–Taylor (R–T)
instabilities which form on the leading surface of the
deformed drop where a heavy ﬂuid is accelerated into a
lighter ﬂuid. Assuming that both ﬂuids are inviscid and the
density ratio is large, the classical R–T analysis results in
the following:
k
max ¼ 2p
ﬃﬃﬃﬃﬃﬃﬃ
3r
aqd
s
ð26Þ
Here kmax is the wavelength of the most destructive wave.
More details on the R–T analysis are given in the section
on catastrophic breakup. Theofanous et al. ( 2004) further
assumed that at the initiation of breakup the drop is
deformed into a ﬂat disk of diameter, d
cro. Therefore the
simpliﬁed R–T analysis predicts dcro/kmax wavelengths will
form on the leading surface of a deformed drop. Combining
Eqs. 26 and 10:
dcro
kmax
¼ 1
4p
dcro
d0
/C18/C19 2 ﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ ﬃ
CD /C1We
p
ð27Þ
In this theory, growth of R–T instabilities creates an initial
surface disturbance which is intensiﬁed by aerodynamic
(1) bag
 (2) Bag/plume 
 (3) Plume/sheet-
thinning
(4) Sheet-thinning
Fig. 12 Transition from bag
to sheet-thinning breakup
(We increases from left to right)
Exp Fluids (2009) 46:371–402 385
123

<!-- PDF_PAGE: 16 -->

effects; this results in the breakup modes. We call this ‘‘the
combined R-T/aerodynamic drag’’ mechanism. Theofanous
et al. (2004) used this theory to show good agreement with
breakup of drops in rareﬁed, supersonic ﬂow. Joseph et al.
(1999) used a similar analysis to show good agreement with
breakup of highly viscous drops.
Figure 15 illustrates breakup when d
cro/kmax =3 .T h i s
resembles the bag/plume mode observed by Dai and Faeth
(2001) for 18 \ We\ 40. Similarly, bag breakup is
expected when dcro/kmax = 1 and more complicated modes
are expected for large dcro/kmax.
In Fig. 16,E q . 27 is used to predict the number of
wavelengths on a deformed drop as a function of We.
Equation 11 is used to predict the cross-stream diameter at
breakup, and Eq. 13 is used to predict the instantaneous
drag coefﬁcient, where CD-sphere is taken to be 0.4. Rea-
sonable agreement between the predictions and the
experimentally observed ranges of Dai and Faeth ( 2001)i s
seen, especially in the bag regime where the predicted
number of wavelengths is approximately 1 and in the bag/
plume range where the predicted number of wavelengths is
between 2 and 3.
Despite the agreement seen in Fig. 16 a few ﬂaws exist
in this theory. First, unstable surface waves are not com-
monly observed at low We. Also, in the most detailed
numerical study known to exist, Khosla et al. ( 2006) suc-
cessfully simulated bag, multimode, and sheet-thinning
breakup. In all cases, surface waves did form. However, the
wavelengths did not appear to control the breakup mode as
proposed in the combined R-T/aerodynamic drag mecha-
nism; rather the results of Khosla et al. ( 2006) are better
supported by the ‘‘internal ﬂow’’ mechanism, which is
proposed here.
In this mechanism drop deformation leads to internal
ﬂow from the poles to the equator. In bag breakup the
surface tension is sufﬁcient to resist this ﬂow resulting in
the formation of the toroidal ring. However, as the rate of
deformation increases with We a critical point is reached
Fig. 13 Shadowgraph of
multimode breakup (bag/plume)
Fig. 14 Shadowgraph of
multimode breakup (plume/
sheet-thinning)
dcro
λmax 
λmax 
λmax 
Fig. 15 Breakup due to
combined Rayleigh–Taylor
(R–T)/aerodynamic drag
mechanism
386 Exp Fluids (2009) 46:371–402
123

<!-- PDF_PAGE: 17 -->

where surface tension is insufﬁcient and the drop con-
tinuously elongates. Eventually the edges of the drop
become so thin that they are carried away by the ambient
ﬂow.
Based on this hypothesis, the multimode regime occurs
when the effect of the pressure difference across the drop
(which tends to result in the formation of the bag structure)
and the effect of the rapid deformation (which tends to
result in the formation of the sheet-thinning structure) are
comparable.
Based on the available experimental and numerical
evidence, this mechanism appears to provide the best
description of the physics that determine whether a drop
deforms into a bag like or sheet-thinning like structure.
There is no reliance on phenomena (such as surface wave
growth) that has not been observed in experiments. Further
numerical or experimental work that focuses on the
deformation rate and internal ﬂow may conﬁrm this
explanation.
6.3 Behavior
As discussed above, most authors have assumed multimode
breakup to have properties which are some combination of
those seen in bag and shear type breakup. For this reason,
few experiments have been performed that target this
regime.
Dai and Faeth ( 2001) measured the volume fraction of
the bag, ring, plume and drop core and found that the
volume fraction of the bag and ring decrease with
increasing We. The volume fraction of the plume reaches a
local maximum at approximately the transition between
bag/plume and plume/shear breakup. Finally as We
approaches that of the sheet-thinning regime the volume
fraction of the drop core dominates.
7 Catastrophic breakup
7.1 Qualitative description
As noted by Faeth et al. (1995) the velocities and drop sizes
involved in typical dense sprays are such that catastrophic
breakup is not seen. Therefore, this is one of the least
studied breakup regimes. Nevertheless, the study of cata-
strophic breakup is important because this limiting breakup
regime occurs at the highest relative velocities. For this
reason, analysis of this regime can shed light on the
breakup mechanisms.
Unlike other breakup modes, the growth of unstable
surface waves on the leading surface of the drop dominates
breakup. The disruptive waves grow rapidly with time and
eventually penetrate the drop, leading to fragmentation.
To study this phenomenon, Wierzba and Takayama
(1988) used holographic interferometry to eliminate the
cloud of small fragments that are typically seen in shad-
owgraphy. They could then observe stripping of drops from
a large portion of the surface early on in the breakup
process, rather than just the drop periphery as is seen in the
sheet-thinning regime. At later times they observed the
drop core to break up into large fragments, which in turn
underwent stripping breakup.
7.2 Physical mechanism
Liu and Reitz ( 1993) noted that the wave growth may be
described as either a Rayleigh–Taylor (R–T) or Kelvin–
Helmholtz (K–H) instability. R–T instabilities occur when
a density discontinuity is accelerated toward the lower
density, while K–H instabilities occur when high relative
velocities exist at an interface.
In secondary atomization R–T instabilities are typically
assumed to occur at the front or rear stagnation points
while K–H instabilities occur at the drop periphery where
the relative velocity between the drop and ambient is the
largest. However, because of the extremely large acceler-
ations experienced by small drops, most authors have
assumed R-T instabilities dominate. The relevant geometry
is provided as Fig. 17.
Taylor ( 1950) showed that the acceleration of a heavy
ﬂuid into a light ﬂuid will result in the growth of cata-
strophic surface waves at the interface. Chandrasekhar
(1961) expanded Taylor’s analysis to include restorative
surface tension effects. If an inﬁnite planar surface is
assumed, as shown in Fig. 17, along with a surface dis-
turbance of the form:
f ðx; y; tÞ¼ Ae
ik xxþkyyðÞ þxt ð28Þ
where A is an unknown constant, the wavenumber k is
k ¼
ﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ ﬃ
k2
x þ k2
y
q
and is related to the wavelength, k,b y
02 0 4 0 6 0 8 0 1 0 0
Weber Number, We (Oh<0.1)
0
2
4
6
8
10
dcro / λ max
Bag/
plume
Plume/sheet
-thinning
Bag
Fig. 16 Number of wavelengths on deformed drop as predicted by
combined Rayleigh–Taylor (R–T)/aerodynamic drag mechanism
Exp Fluids (2009) 46:371–402 387
123

<!-- PDF_PAGE: 18 -->

k = 2p/k, and x is the exponential growth constant,
Chandrasekhar (1961) showed that the x and k are related:
/C0 ak
x2 a1 /C0 a2ðÞ þ k2r
a q1 þq2ðÞ
/C20/C21
þ1
/C26/C27
a2q1 þa1q2 /C0 kðÞ
/C0 4ka1a2 þ4k2
x a1
l1
q1
/C0 a2
l2
q2
/C18/C19
a2q1 /C0 a1q2ðÞ þ k a1 /C0 a2ðÞfg
þ4k3
x2 a1
l1
q1
þa2
l2
q2
/C18/C19 2
q1 /C0 kðÞ q2 /C0 kðÞ ¼ 0 ð29Þ
Here a is the initial acceleration, a1 = q1/(q1 ? q2),
a2 = q2/(q1 ? q2), q1 ¼
ﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ
k2 þxq1=l1
p
; and q2 ¼ﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ
k2 þxq2=l2
p
: Of foremost importance is the wave
number kmax for which the growth rate is maximum,
xmax. Because it grows the quickest, this wave number
(and its corresponding wavelength, kmax) is expected to
dominant the instability.
In secondary atomization a drop of higher density is
accelerated into the lower density ambient by aerodynamic
drag. As a result, the interface is susceptible to R-T
instabilities. The above analysis assumes that both ﬂuids
are initially at rest. However, in secondary atomization
either the drop, the ambient, or both are initially in motion.
As pointed out by Hwang et al. ( 1996) a stationary refer-
ence frame would indicate that the ﬂow situation shown in
Fig. 17 is expected to occur on the trailing surface of the
drop. However, a reference frame ﬁxed on the drop would
indicate R–T instabilities should occur on the leading
surface of the drop. Most experimental evidence points to
the formation of wave like structures on the leading sur-
face; therefore, most authors have assumed R–T waves
form there.
R–T instability theory is typically used to characterize
breakup in the catastrophic regime. Joseph et al. ( 1999)
considered drops of low viscosity, as well as highly viscous
drops. Nitrogen and helium were used as the ambient ﬂuid
so Eq. 29 was simpliﬁed by neglecting the ambient phase
density and viscosity. The predicted wavelengths were
compared to highly magniﬁed views of the leading surface
of the drop. Surface corrugations were observed that
appeared to match the predictions.
Experimental evidence such as this, and similar results
by Hwang et al. ( 1996), indicate that the catastrophic
breakup mode is controlled by R–T instabilities.
8 Newtonian drop breakup times
In a review of spray structures, Faeth et al. ( 1995) noted
that during the time they break apart drops may travel as
much as 30 to 40 times their initial diameter, and due to the
effects of aerodynamic drag, the largest and smallest
fragments may be separated by more than 100 initial drop
diameters. For this reason, knowledge of the characteristic
times of secondary atomization is needed when attempting
to create any model of that process. Numerous authors have
proposed various characteristic times; not all agree. They
are summarized below.
8.1 Initiation time ( T
ini)
Pilch and Erdman ( 1987) deﬁned the initiation time as the
time required for a drop to deform beyond the oblate
ellipsoid shape. For example, the initiation time for bag
breakup would be marked by the ﬁrst sign of the formation
of the bag. This time is important because it marks the time
when the models of a deforming ellipsoid discussed in the
section on deformation and vibration are no longer valid.
The correlation proposed by Pilch and Erdman ( 1987)i s
given in Eq. 30.
T
ini ¼ 1:9 We /C0 WecðÞ /C0 0:25 1 þ 2:2Oh1:6/C0/C1
We\104;
Oh\1:5
ð30Þ
Hsiang and Faeth ( 1992) have also proposed a
correlation for Tini:
Tini ¼ 1:6= 1 /C0 Oh=7ðÞ We\103; Oh\3:5 ð31Þ
as has Gelfand et al. ( 1975):
Tini ¼ 1:4ð1 þ 1:5Oh0:74Þ We /C25 Wec; Oh\4:0 ð32Þ
All three expressions are plotted in Fig. 18. Reasonable
agreement is seen at low Oh where Tini & 1.5. Clearly at
Oh[ 2 the correlations do not mach one another. It is
unknown which correlation is most accurate and more
work is obviously needed.
ρ2, µ2ρ1, µ1
a>0
x
y
z
f(x,y,t)
Fig. 17 Rayleigh–Taylor instability breakup mechanism
388 Exp Fluids (2009) 46:371–402
123

<!-- PDF_PAGE: 19 -->

8.2 Total breakup time ( Ttot)
Pilch and Erdman ( 1987) deﬁned the total breakup time,
Ttot, as the time when all fragmentation has ceased. In
the limit of low viscosity ( Oh\ 0.1) they proposed the
following correlation to the experimental data that is con-
tained in Fig. 19. [Note that the third equation has been
corrected for a typographical error in the Pilch and Erdman
(1987) publication.]
Ttot ¼ 6 We /C0 12ðÞ /C0 0:25 12\We\18
Ttot ¼ 2:45 We /C0 12ðÞ 0:25 18\We\45
Ttot ¼ 14:1 We /C0 12ðÞ /C0 0:25 45\We\351
Ttot ¼ 0:766 We /C0 12ðÞ 0:25 351\We\2670
Ttot ¼ 5:5 2670 \We ~\105
ð33Þ
Note how the transitional Weber numbers for Eq. 33
roughly correspond to the transitional Weber numbers of
the breakup morphology given in Table 2. This suggests
that the physics governing breakup times is different
for each breakup mode, and is further support for
dividing secondary atomization into numerous breakup
morphologies.
Dai and Faeth ( 2001) studied the total breakup time in
the multimode regime and, like Pilch and Erdman ( 1987),
noticed a local maximum near We = 40 similar to that
given in Eq. 33. This local maximum occurs at the tran-
sition of bag/plume and plume/sheet-thinning breakup, as
deﬁned in the discussion of the multimode breakup regime.
For the case of viscous drops Pilch and Erdman ( 1987)
cited the correlation given by Gelfand et al. ( 1975).
However, they noted that Eq. 33 is more accurate than Eq.
34 for drops of low viscosity ( Oh \ 0.1). Note that Pilch
and Erdman ( 1987) have a typographical error in their
republication of Eq. 34; it has been corrected here.
T
tot ¼ 4:51 þ 1:2Oh0:74/C0/C1
We /C25 Wec; Oh\0:3 ð34Þ
Similarly, Hsiang and Faeth ( 1992) proposed the
following relation:
Ttot ¼ 5= 1 /C0 Oh=7ðÞ We\103; Oh\3:5 ð35Þ
Both equations are presented in Fig. 20. Reasonable
agreement is seen at low Oh where Ttot & 5.0. At
Oh[ 0.5 the correlations do not match one another. It is
unknown which correlation is most accurate and more
work is needed.
9 Non-Newtonian drop studies
As mentioned in the previous sections, a vast number of
efforts have been made to investigate secondary breakup of
Newtonian drops. Here we focus on the far fewer studies
where non-Newtonian drop breakup was considered. Our
discussion follows the same format as for Newtonian
drops.
9.1 Description
A non-Newtonian liquid does not exhibit a linear rela-
tionship between shear stress and rate of strain. This feature
has made their use popular in a variety of applications
where the liquid should have a low effective viscosity
10
-3
10
-2
10
-1
10
0
10
1
0
2
4
6
8
10
initiation time, Tini
Gelfand (1975)
Pilch and Erdman (1987) (We=14)
Hsiang and Faeth (1992)
Ohnesorge number, Oh
Fig. 18 Initiation time ( Tini) from Eqs. 30 to 32
101 102 103 104 105
Weber number, We
0
2
4
6
8
10total breakup time, Ttot
Fig. 19 Total breakup time ( Ttot) from Eq. 33 (Oh\ 0.1)
Exp Fluids (2009) 46:371–402 389
123

<!-- PDF_PAGE: 20 -->

during spray formation (high rate of strain) and a higher
effective viscosity when on a target (low rate of strain).
Examples of non-Newtonian liquids frequently encoun-
tered in daily tasks are paints and hair care products.
Additional examples include thermal barrier coatings and,
most recently, gelled fuels.
It is important to note that this oft-times desirable
rheological characteristic causes the secondary breakup
behavior of non-Newtonian drops to differ from that of
Newtonian liquids. This has been shown by Wilcox et al.
(1961), Matta and Tytus ( 1982), Matta et al. ( 1983),
Arcoumanis et al. ( 1994, 1996), Joseph et al. ( 1999,
2002), and most recently by Lo ´pez-Rivera and Sojka
(2008).
In contrast to the Newtonian case, there is not enough
data to provide a clear consensus as to either common
characteristics or processes for non-Newtonian drop sec-
ondary breakup. However, all authors observe bag breakup.
Bag-and-stamen breakup has been reported by Joseph et al.
(2002). In marked contrast to the Newtonian case is the
rupture of the bag into a net of ﬁlaments that may or may
not break up subsequently. In addition, all groups report
some form of stripping/shearing. However, in yet another
clear departure from Newtonian drop breakup a ﬁlament
net forms from mass that is stripped/sheared off the drop
perimeter. This feature has been observed by all groups,
and demonstrates why non-Newtonian secondary atom-
ization is considerably more complex—several stages of
breakup are observed instead of ligaments being continu-
ously eroded from the drop surface and then rapidly
disintegrating into small droplets.
9.2 Non-dimensional groups
More physical processes and ﬂuid properties are important
in the secondary breakup of non-Newtonian drops than for
the Newtonian case because of the increased rheological
complexity. Non-Newtonian drop breakup geometries are
also complicated, as evidenced by the net of ﬁlaments that
forms when a bag breaks up and the multi-stage ligament
breakup during stripping/shearing. These features make
mathematical and numerical analysis even more challeng-
ing than for the already difﬁcult Newtonian case.
Surprisingly, while previous researchers studying New-
tonian drops typically describe their ﬁndings in terms of
non-dimensional groups ( We, Oh, Re, Ma, N and e), that
approach has been rejected by many of those investigating
non-Newtonian secondary breakup. As examples, Arcou-
manis et al. ( 1994, 1996) declined to correlate their
secondary breakup data using We because they argue that
We
c cannot be easily deﬁned due to the shear-dependent
viscosity. This is certainly true for the liquids they used
since the diffusion coefﬁcient for their polymer (K125) in
their solvent (triethyl phosphate) is such that the polymer
surface concentration would not be uniform over the drop
at any instant in time. However, polymers with molecular
weights much lower than that of K125 ( *4 9 10
6) may
diffuse rapidly enough to remove surface tension variations
from consideration and allow separate investigation of
elastic effects. This topic should therefore be investigated.
Perhaps because of concerns about surface tension vari-
ations, the possibility of aWe versus elastic-Oh regime plot,
analogous to the one by Hsiang and Faeth ( 1995) that is
shown here as Fig. 5, has not been mentioned. In fact, only
recently has non-Newtonian breakup behavior been related
to We (Joseph et al. 1999;L o´pez-Rivera and Sojka 2008).
Results are preliminary and much work remains to be done.
A list of dimensionless groups that might be expected to
play roles in non-Newtonian drop secondary breakup is
provided in Table 4. Logic for their choices follows that
presented in the discussion after Table 2.
The same aerodynamic forces deform a non-Newtonian
drop and can cause it to fragment. They are resisted by the
same surface tension force so We is again an important
parameter (under restrictions mentioned above).
As for Newtonian drops, ‘‘viscosity’’ hinders deformation
and also dissipates (or stores) energy supplied by aerody-
namic forces so Oh should be included. In the case of non-
Newtonian liquids, there are at least two possible expres-
sions for Oh—one for purely viscous, such as power law
liquids and one for visco-elastic, such as Oldroyd B, liquids.
One must again consider the gas Re because it is still the
ratio of aerodynamic forces to ambient viscous forces, the
drop phase-to-ambient phase density ratio, e, because
inertial effects are present, and the drop phase-to-ambient
10 -3 10 -2 10 -1 10 0 10 1
Ohnesorge number, Oh
0
2
4
6
8
10
total breakup time, Ttot
Gelfand (1975)
Hsiang and Faeth (1992)
Fig. 20 Total breakup time ( Ttot) from Eq. 34 and Eq. 35
390 Exp Fluids (2009) 46:371–402
123

<!-- PDF_PAGE: 21 -->

phase ‘‘viscosity’’ ratio, M. There is a different form of N
for viscous and visco-elastic non-Newtonian liquids.
Finally, the Mach number, Ma, is important when consid-
ering compressibility effects.
As was done for Newtonian liquids, experimentally
observed times might also be made dimensionless through
the scaling given by Eq.4. It might also be more appropriate
to use relaxation or retardation times for elastic liquids.
9.3 Transition We (low Oh), dependency on Oh,
and dependency on other non-dimensional
parameters
Transition boundaries between breakup modes have yet to
be quantiﬁed as functions of We, Oh or other parameters
such as the density ratio ( e), Wi, ReNN, or gas-phase Re.I n
fact, at this time it is unclear as to which dimensionless
groups play dominant roles in the purely viscous and visco-
elastic cases. As such, dependence of transition We on
other non-dimensional parameters has yet to be reported.
Work on this topic is clearly required.
9.3.1 Inﬂuence of polymer concentration
Wilcox et al. ( 1961) found that increasing polymer con-
centration from values as low as 0.1% retards breakup
in high-velocity airstreams at relative velocities up to
Ma = 1. Inhibition was not always observed at Ma =1 ,
but the authors predict it would be seen if concentration
was increased to more than 2%. As expected, higher
retardation was obtained for lower velocities.
9.4 Drop deformation and vibrational breakup
9.4.1 Qualitative description and physical mechanism
Oscillation has not been observed for non-Newtonian
drops, probably because experiments have yet to be per-
formed at We low enough to observe such behavior.
Oscillatory breakup has not been observed either, for the
same reason.
While low We drop deformation has not been observed
for non-Newtonian liquids, Joseph et al. (1999) did observe
that behavior at the start of their high We tests. Their data
lead them to propose the same physical mechanism that is
accepted for Newtonian drop deformation—an unequal
static pressure distribution across the drop.
9.4.2 Behavior
Data from Joseph et al. ( 1999) demonstrate that early drop
core motion obeys a constant acceleration model. As such
Eq. 8 could be applied if /C22C
D was known. Joseph et al.
(1999) do not provide /C22CD values. The authors state that the
drop acceleration magnitude falls off as complete breakup
approaches.
9.4.3 Deformation and drag
Experimental deformation data are currently unavailable
for non-Newtonian drops. Analytical models, such as the
TAB-model or its derivatives, could be modiﬁed to include
purely viscous or visco-elastic non-Newtonian effects. This
has yet to be done.
Non-Newtonian drop drag coefﬁcient magnitudes have
not been reported. Values might be extracted from the
Joseph et al. ( 1999) acceleration data (their Table 2) and
initial condition data (their Table 1), although those authors
did not do so.
9.5 Bag breakup
9.5.1 Qualitative description
Like Newtonian liquids, non-Newtonian drops also exhibit
bag breakup. The drop deforms with the same thin hollow
bag attached to a thicker toroidal rim. The bag is blown
downstream and disintegrates ﬁrst, forming a net of
Table 4 Dimensionless groups
that might be important in non-
Newtonian drop secondary
breakup
Inelastic liquid Elastic liquid
Weber number We
qaU2
0 d0
r
qaU2
0 d0
r
Ohnesorge number Oh We =Re1=2
NN We=Re1=2
NN
Liquid Reynolds or Weissenberg number ReNN ¼ qaU2/C0 n
0 d0
K Wi ¼ k 1ðÞ U0
d0
Ambient phase Reynolds number Re qaU0d0
la
qaU0d0
la
Density ratio e qd
qa
qd
qa
Viscosity ratio M leff
la
lelastic
la
Mach number Ma U0
c
U0
c
Exp Fluids (2009) 46:371–402 391
123

<!-- PDF_PAGE: 22 -->

ﬁlaments. The ﬁlaments undergo breakup, as does the
toroidal rim. This behavior has been reported by Arcou-
manis et al. (1996). However, Joseph et al. (1999) found this
mechanism at very high We for very viscous Newtonian
ﬂuids, but not for non-Newtonian liquids. Finally, Joseph
et al. (2002) observed bag breakup of visco-elastic drops.
9.5.2 Physical mechanism
Joseph et al. ( 1999) attribute bag formation to a R–T
instability whose wavelength is comparable to or larger
than the diameter of the drop. This explanation is similar to
that proposed by Theofanous et al. ( 2004), who also used a
shock tube when performing their experiments. Arcou-
manis et al. ( 1996) agree with this interpretation and note
the presence of small amplitude short wavelength distur-
bances on their drops.
All groups report that bag breakup for non-Newtonian
drops results in a net of ligaments that form as the bag
disintegrates. The ligaments may then undergo breakup.
9.5.3 We
c and behavior
Unlike for Newtonian drops, there is scant information
available for non-Newtonian drop Wec. Deformation and
breakup time data, plus deformation magnitude results are
also largely missing. The exception is the visco-elastic
liquid data from Joseph et al. (1999), although these results
must be viewed with caution for two reasons. First, com-
bining the characteristic time expression from Bird et al.
(1987) with the polyethylene oxide (PEO)-water intrinsic
viscosity relationship from Kalashnikov and Askarov
(1989), and inserting the very high PEO molecular weights
(4 9 10
6) and concentrations (2%) Joseph et al. ( 1999)
used demonstrates that liquid characteristic times ( *1s )
will be several orders of magnitude greater than the
experimentally measured breakup times ( \1 ms). As such
these liquids may exhibit little, if any, elastic behavior.
Second, the Oh values provided for these liquids are so
high ([80) that viscous effects will almost certainly dom-
inate. Consequently, the Joseph et al. ( 1999) results are
probably more indicative of purely viscous liquid behavior
than that for visco-elastic ones.
9.6 Sheet-thinning breakup (critical speed)
9.6.1 Qualitative description
The thinning/stripping mechanism observed for non-New-
tonian drops resembles that observed for Newtonian ones
in some respects. Ligaments are continuously eroded from
the drop surface, which disintegrate rapidly thereafter
resulting in numerous small fragments.
9.6.2 Physical mechanism
Arcoumanis et al. ( 1994) studied the initial stages of
weakly visco-elastic drop breakup. Their results showed
that drops entering the air ﬂow had a wave appear on their
surface, as reported previously by Liu and Reitz ( 1993),
which then peeled away and broke up into ligaments that
were joined by a thin sheet. The sheet expanded and the
ligaments stretched in the downstream direction where they
fragmented.
For more strongly visco-elastic liquids, Arcoumanis
et al. (1994) did not observe breakup, although a wave did
begin to form on the drop surface and was peeled back. The
drop stretched downstream, ligaments were formed and
were again joined by a sheet, with the sheet being thicker
than for the less visco-elastic drops. Breakup could be
prevented by giving the liquids sufﬁcient elastic character.
This behavior is in marked contrast to that reported for
Newtonian systems. It is likely due to the elastic nature of
the liquids since raising the concentration of polymer
increased the number of ligaments formed and the thick-
ness of the sheet. Wilcox et al. ( 1961) also observed that
non-Newtonian liquids form ligaments that break up into
larger particles than those produced by Newtonian ones
that seem to experience a stripping process leading to very
small particles.
There may be additional differences between visco-
elastic and Newtonian liquid secondary breakup. Arcou-
manis et al. ( 1994) state that only the initial stages of
breakup are shown in their photographs and it is possible
that (1) drops are forming in later stages or (2) the resolution
of their ﬁlm is not sufﬁcient to record small fragments.
In a further study, Arcoumanis et al. ( 1996) extended
their previous work (Arcoumanis et al. 1994) to remove
uncertainty about the existence of drops as a result of
breakup. Their results showed fragments being formed at a
distance 20 times the diameter of the original drop. The
breakup process that they observed was very similar to that
found in their previous work. However, the ligaments were
observed to form droplets. The distance from the main
droplet over which ligaments are linked was also found to
increase with increases in polymer concentration, and to
decrease with air velocity.
Finally, Joseph et al. ( 1999) studied the breakup of
viscous and visco-elastic drops (1 mm) in the high speed
airstream produced by a shock tube at very high We
(11,700–169,000) and Oh (0.002–82.3). These authors also
observed that threads and ligaments of liquid arise imme-
diately after breakup, in contrast to Newtonian liquids, for
which droplets were seen at Ma as high as 3. Joseph et al.
(1999) observed no breakup of some of these threads even
at high Ma. In addition, no drops were seen as a result of
their breakup.
392 Exp Fluids (2009) 46:371–402
123

<!-- PDF_PAGE: 23 -->

9.6.3 Critical speed
Arcoumanis et al. ( 1994) declined to correlate their data in
terms of We because they claim that Wec cannot be easily
deﬁned due to the shear-dependent viscosity of their ﬂuids.
Instead, the authors considered a critical velocity above
which there is no further breakup. Since Arcoumanis et al.
(1994) observed no drops as a result of breakup, they
deﬁned the critical speed as the air jet speed at which many
marks were observed on an impaction card (and immedi-
ately below which only a few were seen).
These authors also showed that increases in polymer
concentration lead to increases in the critical speed of
breakup. This supports the retardation in the breakup pro-
cess reported by Wilcox et al. ( 1961).
9.7 Multimode breakup
9.7.1 Qualitative description
For the case of non-Newtonian drops, only the ﬁrst phase
of this breakup mechanism, the bag/plume, has been
observed. It is qualitatively similar to that seen for New-
tonian drops.
One of the ﬁrst groups of researchers to report it was
Joseph et al. (1999), who observed this mode at a very high
We (*42,000) for very viscous liquids, but not for visco-
elastic drops. This regime was also observed by Joseph
et al. ( 2002), who did observe it for viscoelastic drops.
9.7.2 Physical mechanism
The physical mechanism leading to the multimode breakup
is believed by Joseph et al. ( 1999, 2002) to be the devel-
opment of R–T instabilities on the surface of the drops.
9.8 Catastrophic breakup
9.8.1 Qualitative description
In contrast to Newtonian liquids, catastrophic breakup is
particularly important for non-Newtonian drops because
extremely high relative velocities are often required for
their fragmentation to occur. This mode has been investi-
gated by Joseph et al. ( 1999). It may also have been
investigated by Matta and Tytus ( 1982) and Matta et al.
(1983).
9.8.2 Physical mechanism
Joseph et al. ( 1999) argue that R–T instabilities are the
cause of non-Newtonian drop catastrophic breakup. Sup-
port for their conclusions comes from comparison of
experimental results with predictions from a (purely vis-
cous) R–T analysis for both the critical wavelength and its
growth rate (Joseph et al. 2002). Agreement is within a few
percent.
The Joseph et al. ( 1999, 2002) agreement between
theory and experiment is perhaps surprising since their
analysis is purely viscous (in the limit of very short retar-
dation times). This also suggests that their non-Newtonian
liquids had characteristic times much greater than those of
the breakup events and so should not be categorized as
elastic for the purposes of secondary breakup.
9.9 Non-Newtonian drop breakup times
9.9.1 Initiation time (T
ini) and total breakup time (T tot)
Arcoumanis et al. ( 1994) provide total breakup time data
and report Ttot rises with an increase in polymer concen-
tration. They do not provide a relationship between Ttot and
We or any more suitable dimensionless group.
Joseph et al. ( 1999) report Tini for visco-elastic drops. It
is deﬁned as the time at which disintegration starts. They
observe no, or minimal, variation in Tini throughout the
range of rheologies considered.
Joseph et al. ( 2002) performed an R-T analysis for an
Oldroyd-B ﬂuid and used the results to provide a correla-
tion for the Joseph et al. (1999) data. In a manner similar to
that of Weber (1931), they deﬁned breakup to occur when a
disturbance reached a multiple (10) of its initial amplitude.
This lead to Tini = ln (10)/x where x is the R–T distur-
bance growth rate.
9.10 Non-Newtonian fragment size and velocity
distributions
One of the few studies supplying non-Newtonian liquid
fragment sizes is that performed by Wilcox et al. ( 1961).
These authors observed that fragments of solutions with
polymers added were 1.5 orders of magnitude larger than
fragments produced by Newtonian liquids.
Matta and Tytus ( 1982) also studied the breakup of vis-
coelastic ﬂuids ( \0.5 cm) injected into the high velocity
airstream (200 m/s) of a wind tunnel. Their experimental
results showed that the measured fragment MMD was an
order of magnitude larger than values predicted for a New-
tonian ﬂuid of similar viscosity magnitude. Their results
were found to correlate with the relaxation time obtained
from a die swell experiment. From this, it was thought that
breakup does not follow a shear mechanism, but an elon-
gational one instead. The ﬁrst normal stress difference was
also found to correlate the breakup results. However, since
the breakup deformation rate was unclear, the relaxation
time was preferable for predicting particle size.
Exp Fluids (2009) 46:371–402 393
123

<!-- PDF_PAGE: 24 -->

In a subsequent investigation, Matta et al. ( 1983)
extended their previous work (Matta and Tytus 1982), to
identify the proper variable for drop size predictions. For
this purpose, heated ﬂuids were considered, since the ﬁrst
normal stress difference is known to decrease more rapidly
than the relaxation time with increases in temperature.
Instead of a wind tunnel, a helium activated ﬁring device
was used. The test conditions were comparable ( Ma = 1),
although larger diameter (7.6 cm) viscoelastic slugs were
employed. It was found that increasing the polymer con-
centration increased the average drop size, supporting
previous ﬁndings. Furthermore, results from the tests per-
formed at ambient temperature were observed to correlate
with both the relative relaxation time and the ﬁrst normal
stress difference. However, the results of the tests with
heated ﬂuids were only correlated using the relative
relaxation time, making this parameter the more conve-
nient for drop size predictions.
This concludes the discussion of non-Newtonian drop
breakup.
10 Fragment size and velocity distributions
Fragment size distributions are one of the most important
but difﬁcult to measure properties of secondary atomiza-
tion. Historically, techniques to measure fragment sizes
have been limited in their accuracy. Among the viable
methods were rapid solidiﬁcation of the fragments and
holography. Both methods are time consuming, difﬁcult to
set up, and results are hard to analyze.
Recently, the commercial availability of PDA and other
optical drop sizing methods have resulted in more rapid
and accurate measurements. However, these devices
require a continuous process and cannot be easily used in
shock tube experiments because their measurement vol-
umes are typically small compared to the region through
which fragments pass. As a result, only limited experi-
mental data exist and more research is warranted.
Drop size distributions are often described by two or
more characteristic diameters. Here the nomenclature of
Mugele and Evans ( 1951) will be used.
A representative diameter is given by:
D
pq ¼
R 1
0 Dpf0ðDÞdD
R1
0
Dqf0ðDÞdD
2
664
3
775
1=p /C0 q
ð36Þ
where p and q are positive integers and f0(D) is the number
PDF. Common examples include the arithmetic mean
diameter, D10, the volume mean diameter, D30, and the
Sauter mean diameter, D32.
Simmons (1977a, b) studied the drop size distribution for
sprays formed using a large number of aircraft and industrial
gas turbine nozzles where secondary atomization was
thought to play a crucial role in determining the ﬁnal size
distribution. The fragment mass median diameter (equal to
MMD for constant density) andD
32 were found to be related
by MMD/D32 * 1.2. In addition, given either MMD orD32
the fragment volume PDF, f3(D), could be approximated as
root/normal. Finally Simmons ( 1977a, b) found the maxi-
mum fragment size to be approximately three times MMD.
Following the work of Simmons ( 1977a, b), Hsiang
and Faeth ( 1992, 1993) used holography to measure drop
size distributions for Oh\ 0.1. In the bag and multi-
mode regimes, the root normal distribution with MMD/
D32 * 1.2 proposed by Simmons ( 1977a, b) was found to
ﬁt the data reasonably well. Furthermore, after removal of
the drop core, this same distribution was found to be
applicable in the sheet-thinning regime. The complete
fragment size distribution can be found by using Eqs. 23 to
25 to ﬁnd the drop core size and velocity.
Having conﬁrmed that the approach of Simmons (1977a,
b) is applicable to secondary atomization, the last piece of
knowledge needed to determine drop size distributions
a priori is either D
32 or MMD. To this end Hsiang and
Faeth ( 1992) conducted a phenomenological analysis by
considering the size of the drop phase boundary layer,
which is thought to determine the size of the fragments in
shear breakup. This yielded:
We
D32 ¼ Ce1=4Oh1=2We3=4 ð37Þ
We\1000; Oh\0:1; 580\e\1000
where WeD32 ¼ qaD32U2
0
/C14
r and C is a constant of pro-
portionality. For the range of parameters considered,
Hsiang and Faeth ( 1992) used C = 6.2 and Eq. 37 was
found to reasonably predict fragment D32. However, they
noted that the range of the density ratio was relatively
narrow and further testing was needed.
Equation 37 was derived from the assumed physics of
shear type breakup; therefore, its applicability to bag and
multimode regimes is limited. For this reason, Wert ( 1995)
proposed a new correlation for D32 based on the physics of
bag breakup. Because a large portion of the original drop
mass is contained in the toroidal rim, D32 was assumed to
be governed by the growth of capillary instability waves on
this rim. This resulted in the following:
We
D32 ¼ CW eT tot /C0 TiniðÞ½/C138 2=3 12\We\80; Oh\0:1
ð38Þ
where C is a constant of proportionality. Tini and Ttot can be
found using Eqs. 30 and 33, respectively.
Based on available data in the bag and multimode
regime, Wert (1995) suggested C = 0.32 and stated that Eq.
394 Exp Fluids (2009) 46:371–402
123

<!-- PDF_PAGE: 25 -->

38 outperforms Eq. 37 in these regimes. The authors noted
that Eq. 38 may be applicable for Oh[ 0.1. However, this
has yet to be tested.
The above mentioned distributions were determined
experimentally. However, the goal of many researchers has
been the determination of drop size (and velocity) distri-
butions from theory. One possibility is the maximum
entropy formalism (MEF). Here constraints are placed on
the fragment size and velocity distributions. Examples
include all drops being spherical, mass being conserved,
and estimates for momentum and energy transferred to the
drops from the surrounding gas. From this a least biased
PDF is computed. Babinsky and Sojka ( 2002) provide a
thorough discussion of the development and application of
the MEF to sprays applications. Signiﬁcant ﬁndings will be
discussed here, along with works completed subsequent to
that review.
MEF has the capability of predicting both fragment size
and velocity distributions. However, knowledge of at least
two characteristic diameters is required a priori. The
requirement of at least two characteristic diameters proves
problematical.
Cousin et al. ( 1996) proposed the use of linear stability
theory to predict one characteristic fragment diameter.
However, no theoretical method exists to predict the sec-
ond characteristic diameter so either experimental results
or an ad hoc assumption are required.
Dumouchel and Boyaval ( 1999) expanded on the work
of Cousin et al. ( 1996) by noting that the choice of rep-
resentative diameter is paramount to the accuracy of the
ﬁnal distribution. For example, D
43 is the best choice for
determining the volume based distribution because it is
very close to the mean of the distribution. Having made
these observations, Dumouchel and Boyaval ( 1999) pro-
vide a recommended method to determine the best choice
of model constraints based on the distribution being sought.
Li et al. ( 2005) noted that the MEF is applicable to
isolated systems in thermodynamic equilibrium. However,
many sprays do not meet these requirements. Therefore,
Li et al. ( 2005) proposed a new model with additional
constraints to track the degree of deviation from the equi-
librium assumption. The result was a better ﬁt to
experimental data. However, this introduced the need for
more characteristic diameters which are not easy to predict
a priori. This study helps to understand some of the reasons
for inaccuracies in the MEF; however, the practical
application of this method is limited.
Dumouchel ( 2006) included an ad hoc physical mini-
mum and maximum drop diameter in their MEF analysis.
They were based on the observation that inﬁnitesimally
small drops are impossible due to the presence of surface
tension, as are inﬁnitely large drops due to instabilities.
Their results show that a minimum of three parameters
must now be known a priori. This only exacerbates the
problem.
In summary, MEF can be used to correlate the fragment
size and velocity distributions. However, MEF cannot be
considered predictive in practice because constraints are
needed a priori, at least some of which must be determined
using experimental measurements or come from ad hoc
assumptions.
A few other methods have been proposed to predict
fragment size distributions. Zhou et al. ( 2000) studied
the fractal characteristics of sprays both theoretically
and experimentally. Their model showed some predictive
capability. However, some measurements were needed
a priori, and more work is needed.
Babinsky and Sojka ( 2002) discussed the application of
the discrete probability function (DPF) approach which
uses stability analyses to model the (primary) breakup
process coupled with an assumed probability distribution of
the input parameters. The DPF method is unlikely to work
for secondary atomization because stability analyses, or
other closed form predictions of fragment size, are
unavailable.
10.1 Non-Newtonian fragment size
The only studies reporting fragment size distributions for
non-Newtonian drops are those performed by Matta and
coworkers. Their results are contradictory.
In their original study, Matta and Tytus ( 1982) stated
that non-Newtonian fragment diameters followed a normal
distribution, although there was some evidence of bi-
modality. This was in contrast to their Newtonian liquid
data which were log-normally distributed.
In their second investigation, Matta et al. ( 1983) used
the same liquids and claimed that fragment sizes obeyed a
log-normal distribution. They did not comment on the
contradiction.
A possible explanation for the inconsistency is that
fragments formed in their ﬁrst study were the result of both
primary and secondary breakup, since they were injecting a
coherent liquid jet into their airstream. This would also
explain the evidence of a bi-modal distribution.
It is obvious that much work remains to be done in this
area.
11 Modeling efforts
To date no single model has been created that describes all
aspects of secondary atomization accurately. Gelfand
(1996) considered droplet deformation and breakup with
regard to aerodynamic loading, liquid stripping, and sta-
bility analyses. None of those models were found to
Exp Fluids (2009) 46:371–402 395
123

<!-- PDF_PAGE: 26 -->

completely explain breakup, and the author surmised that
all must be considered in parallel.
Berthoumieu et al. ( 1999) created a secondary atom-
ization model based entirely on experimentally determined
correlations such as those given in the above sections. It
did a poor job of predicting the actual distribution of
fragments.
Chryssakis and Assanis ( 2005) had more success by
combining experimental correlations for deformation and
drag with some theoretical wave growth and boundary
layer stripping models. Nevertheless, the model is still only
applicable within the range of parameters covered by
experiments. To overcome these difﬁculties much focus
has been placed on models based on the assumed under-
lying physics.
11.1 Analytical
Compared to the fragmentation process seen in other
modes of breakup, drop distortion and oscillation is gov-
erned by relatively simple physics and therefore lends itself
to analytical modeling. One of the ﬁrst such models was
the Taylor analogy breakup (TAB) model proposed by
O’Rourke and Amsden ( 1987). Their model is based on an
analogy by Taylor ( 1963) between an oscillating and dis-
torting droplet and a spring-mass system in which the
spring force, external force and dampening are respectively
analogous to surface tension, aerodynamic forces, and drop
viscosity. Breakup is assumed to occur when d
str ? 0.
Finally, energy conservation is used to determine the
fragment sizes after breakup with the distribution assumed
to be v-squared.
The literature contains many studies in which the TAB
model is used to simulate secondary atomization and
sprays, including O’Rourke and Amsden ( 1987), Liu and
Reitz ( 1993), Hwang et al. ( 1996), Tanner ( 1997), Lee
and Reitz ( 1999), Park et al. ( 2002), Apte et al. ( 2003),
Park and Lee ( 2004), Lee et al. ( 2004), Trinh and Chen
(2006), and Trinh et al. ( 2007) among others. These
studies have pointed to a number of shortcomings in the
TAB model.
Hwang et al. ( 1996) showed that the predicted breakup
time most closely matches the initiation time, at which
point breakup is assumed to occur instantaneously. How-
ever, experimental evidence has shown that breakup
actually occurs over a ﬁnite time.
Park and Lee ( 2004) have shown that the accuracy of
ﬁnal fragment size predictions may be a function of oper-
ating conditions. In applications to diesel sprays the
fragment sizes are typically over predicted for low pressure
simulations and under predicted at high pressures.
Hwang et al. ( 1996) pointed out that the TAB model
does not accurately predict the frontal area of the distorted
drop. For this reason the calculation of drag may be
incorrect leading to poor prediction of drop trajectory.
Finally, the breakup criterion is somewhat arbitrary and
experimental data, such as Eq. 11, indicate that the critical
deformation is actually a function of We.
An alternative to the TAB model is the droplet defor-
mation and breakup (DDB) model proposed by Ibrahim
et al. ( 1993). In this model drop deformation is calculated
by equating the rate of change in kinetic and potential
energies to the work done on the drop due to pressure and
viscous forces. Breakup is assumed to occur when both
kinetic and viscous forces are negligible, resulting in a
relation between critical deformation and We. Mass is
conserved, therefore an accurate calculation of the drop
frontal area is possible.
Again, the literature contains many studies in which the
DDB model was used to simulate secondary atomization.
These include Ibrahim et al. ( 1993), Hwang et al. ( 1996),
Liu and Reitz ( 1997), Park et al. ( 2002), Pham and Heister
(2002), Park and Lee ( 2004), and Lee et al. ( 2004) among
others.
The DDB model does have shortcomings. Park et al.
(2002) noted that the DDB model breakup criterion pre-
dicts instantaneous breakup without deformation when We
is less than 19. This is clearly unrealistic, so the DDB
model as originally proposed by Ibrahim et al. ( 1993)
cannot be applied to low We drops.
Hwang et al. ( 1996) calculated drop trajectories using
both the TAB and DDB models. For the DDB model the
drag was calculated using Eq. 13. In this case the DDB
model was shown to be superior. In other instances, such as
the work of Park et al. ( 2002), the TAB model has been
shown to outperform the DDB model. Currently, both
models are used in industrial spray simulations, each with
their own advantages and limitations.
A number of authors have proposed improvements to
the TAB and DDB models. Tanner ( 1997) proposed the
enhanced TAB (ETAB) model to address two common
problems in the original version, namely the instantaneous
breakup of the drop at the initiation time and the under
prediction of fragment sizes. The breakup criterion
remained the same as the original TAB model, but for-
mation of fragments was assumed to occur at a rate
proportional to the number of fragments where the constant
of proportionality is a function of the breakup regime. For a
diesel spray, Tanner ( 1997) showed that ETAB model
predictions better represented the experimental data than
those from the TAB model.
Park et al. ( 2002) proposed an improved TAB model in
which the effect of droplet deformation on drag is simu-
lated in a manner similar to the DDB model. Also, a new
breakup criterion was proposed that was based on a con-
sideration of both the ambient and drop phase pressure
396 Exp Fluids (2009) 46:371–402
123

<!-- PDF_PAGE: 27 -->

distributions and the surface tension. The result was a more
reasonable relation between We and the amount of defor-
mation leading to breakup. Comparison to experimental
results showed that the improved TAB model of Park et al.
(2002) outperformed both the TAB and DDB model.
Nevertheless, all models were shown to be inaccurate near
We
c and more work is needed.
Others have used wave instability models as the breakup
criteria, rather than a critical deformation level. One
example is the breakup model of Lee and Reitz ( 1999)i n
which a K–H instability model is used (with limited suc-
cess). Still others have used hybrid models to simulate the
simultaneous effect of breakup due to unstable wave
growth and breakup due to aerodynamic deformation, such
as is expected in the catastrophic breakup regime. An
example is the K–H/DDB competition model of Park and
Lee ( 2004). Finally, Gorokhovski ( 2001), Apte et al.
(2003), and Gorokhovski and Saveliev ( 2003) used sto-
chastic principles to predict drop breakup and found
reasonable agreement with measured spray properties.
These secondary breakup models are combined with
primary breakup models and simulation of the ambient
phase ﬂow to create complete spray models. Examples
include Tanner ( 1997), Gorokhovski ( 2001), Pham and
Heister ( 2002), Apte et al. ( 2003), Gorokhovski and
Saveliev (2003), Lee et al. ( 2004), Trinh and Chen ( 2006),
and Trinh et al. ( 2007) among others.
11.2 Direct numerical simulation
Direct numerical simulation (DNS) promises the ability to
resolve both the drop and ambient phase ﬂow ﬁelds and
may help answer a number of outstanding questions about
secondary breakup. Such a simulation requires solutions to
multiphase, unsteady, 3D ﬂow with pinch off of small
fragments. This necessitates resolution over a large range
of length scales. To date, few simulations have been per-
formed which meet all of these requirements.
Zaleski et al. ( 1995) performed a 2D simulation of the
Navier-Stokes equation with constant density and viscosity
in each phase. Their conﬁguration corresponds to the
breakup of an inﬁnite cylinder, rather than of a spherical
drop. However, Igra and Takayama ( 2001) and Igra et al.
(2002) showed experimentally that the breakup is qualita-
tively similar. A volume of ﬂuid (VOF) method was used
to track the interface, and surface tension effects were
included. Fragmentation was simulated at We = 10, 20, and
100. All simulations were performed for e = 10 and
Oh\ 0.1. The We = 100 results were qualitatively similar
to sheet-thinning regime behavior while the We = 10 and
20 results showed the formation of bag structure. However,
the bag formed in the upstream direction rather than
downstream as seen in experiments. The authors comment
that the discrepancy in the bag regime may be due to the
initial conditions they used.
In a series of two papers, Han and Tryggvason ( 1999,
2001) addressed many of the shortcomings of the Zaleski
et al. ( 1995) study. A front tracking/ﬁnite difference
method was used to solve the axi-symmetric Navier–Stokes
equations. The axi-symmetric assumption allowed for the
simulation of a spherical drop rather than a 2D cylinder.
Simulations were performed for steady loading, such as
seen in a drop tower, as well as impulsively accelerated
loading, such as seen in shock tube experiments. Both bag
and sheet-thinning type structures were observed, but
transitional We values did not match those seen in exper-
iments. This may be due to the fact that calculations were
performed for e\ 10. Such a low density ratio was nec-
essary to reduce computational cost, but most experiments
are performed for liquid drops in ambient gas environments
where the density ratio is much higher. Further experi-
mental data are needed to address the accuracy of these
simulations.
Aalburg et al. ( 2003) expanded the work of Han and
Tryggvason (1999, 2001) to simulate drop deformation at
much higher density ratios. The level set method of Suss-
man et al. (1994) was used to track the interface. Although
Aalburg et al. (2003) did not have sufﬁcient grid resolution
to simulate the breakup event, Sussman et al. ( 1994) has
previously shown that the level set method is capable of
resolving such events.. For e [ 128, the predicted trend of
We
c versus Oh matched the experimental results of Hsiang
and Faeth ( 1995).
Quan and Schmidt (2006) developed a 3D, ﬁnite volume
scheme that uses a moving mesh. Again, due to computa-
tional cost, simulations were performed at relatively low
values of Re and e, and the actual breakup event was not
simulated. Nevertheless, images of the deforming droplet
appear to qualitatively match those seen in experiments.
Wadhwa et al. (2005, 2007) developed a code capable of
3D simulations including compressibility effects in the
ambient. Due to computational cost, the ﬁnal simulation of
drop deformation was done assuming axi-symmetry. Nev-
ertheless, their results for drop deformation at We up to 100
and Oh up to 0.1 show good agreement with experimental
results.
In what is thought to be the most accurate study per-
formed to date, Khosla et al. ( 2006) used the VOF method
to simulate breakup of an ethanol drop in air. Special care
was taken to ensure that the grid was ﬁne enough to resolve
the internal ﬂow including the drop phase boundary layer.
In addition, 3D, reduced 3D, and 2D axi-symmetric cases
were analyzed. The 2D axi-symmetric case was shown to
be sufﬁcient to resolve the breakup mechanism, although a
full 3D case may be needed to accurately determine the
ﬁnal fragment sizes. Finally, unlike moving mesh schemes,
Exp Fluids (2009) 46:371–402 397
123

<!-- PDF_PAGE: 28 -->

VOF was capable of simulating the pinch off and formation
of fragments. The results of Khosla et al. ( 2006) showed
excellent agreement with experimental results.
Finally, Chang and Liou ( 2007) developed a stratiﬁed
ﬂow model which is capable of incorporating compressible
liquids and gases. Therefore, the code can simulate the
interaction of a shock wave and liquid drop. Initial results
indicate very good agreement with the experimental results
of Theofanous et al. ( 2004) at high Ma.
The above mentioned results assume that the ﬂuids are
continuous. Some success has been had using particle
methods where ﬂuid packets are tracked via a Lagrangian
scheme. One example is the moving-particle semi-implicit
(MPS) method, originally proposed by Koshizuka and Oka
(1996) and improved by Nomura et al. ( 2001) with the
addition of surface tension. Nomura et al. ( 2001) and Duan
et al. ( 2003a, b) used the MPS method to simulate sec-
ondary atomization. Although their simulations were 2D,
they showed good qualitative agreement with experimental
results and solutions for large density ratios were possible.
Nomura et al. (2001) indicate that they have used the MPS
method to perform a 3D simulation of drop breakup,
although they give no further details. Finally, Shibata et al.
(2004) successfully used the MPS method to simulate
primary atomization.
An additional particle method is the Lattice-Boltzmann
approach as presented by Sehgal et al. ( 1999). In this case
methodologies from molecular gas dynamics are used to
simulate ﬂuid ﬂow. According to Sehgal et al. ( 1999), the
Lattice-Boltzmann method can be shown to be equivalent
to solving the incompressible Navier–Stokes equations.
The results presented by Sehgal et al. ( 1999) are qualita-
tively similar to experimentally observed breakup, but the
transition We do not match experimental data so more work
is needed.
At this time VOF and the level set method are among
the most widely accepted. More work is needed to simulate
the entire breakup process including accurately predicting
the ﬁnal fragment sizes.
12 Areas for future research
12.1 Non-Newtonian liquids
This topic has received only cursory attention, despite the
fact that non-Newtonian sprays play a key role in so many
practical processes, that there are so many interesting
physical phenomena to explore, and that the breakup
behavior is clearly different than for Newtonian liquids.
The limitations of available information have been docu-
mented above:
• Consensus on something as basic as the breakup modes
has not been achieved. This is due to a scarcity of
studies.
• Even information as fundamental as which dimension-
less groups should be used to describe non-Newtonian
drop secondary breakup results is lacking. Again, this is
due to a scarcity of studies.
• The critical Weber number for breakup has not been
identiﬁed, nor have values that separate regime bound-
aries. Ohnesorge (and Wiesenberg) number dependencies
have yet to be investigated. Valuable ﬁgures such as that
from Hsiang and Faeth (1985) cannot be constructed until
this information has been published.
• Bag and stripping breakup exhibit a net-like structure
that has yet to be studied in detail. It may lead to
bi-modal fragment size distributions.
• Drag expressions are absent.
• There are no estimates for initiation and total breakup
times.
• There is contradictory information about fragment size
distributions.
12.2 Experiments near the thermodynamic
critical point
In modern diesel and gas turbine engines the compression
ratio is such that the injected fuel may approach the ther-
modynamic critical point. In such cases, one can expect
very low density ratios (on the order of unity) and We and
Oh to approach inﬁnity as the surface tension goes to zero.
Currently no experimental secondary breakup data
exists at or near the critical point. The only known results
come from DNS studies, such as the work of Han and
Tryggvason (2001) and Aalburg et al. ( 2003). These sim-
ulations indicate markedly different breakup characteristics
at very high We and Oh numbers and very low e.I n
addition, current experimentally determined correlations
involving high Oh are limited and poor agreement is seen
between researchers. Additional experimental and numer-
ical work is needed to fully characterize breakup near the
thermodynamic critical point.
12.3 Turbulence
Drops in a turbulent ﬂow ﬁeld which are larger than the
Kolmogorov length scale will be subjected to irregular ﬂow
patterns. Hinze (1955) was the ﬁrst to study such a situation
and observed what he described as ‘‘bulgy’’ deformation.
Rather than deforming into an oblate ellipsoid as in the
case of laminar ﬂow, drop deformation and fragmentation
was irregular. Later Prevish and Santavicca ( 1998) found
that We
cr decreased as the turbulence intensity of the
398 Exp Fluids (2009) 46:371–402
123

<!-- PDF_PAGE: 29 -->

ambient ﬂow increased. Also, it appears that turbulence
adds randomness to the breakup process. Some drops
experience low local velocities and therefore break up
slowly, or do not break up at all. Other drops experience
local velocities higher than the average and therefore break
up faster and at lower We (based on the mean velocity).
Drop phase turbulence may also exist and result from
either turbulence generated prior to primary atomization that
has not had sufﬁcient time to dissipate or as the result of rapid
internal circulation caused by deformation and/or shear from
the ambient phase. Trinh and Chen ( 2006) and Trinh et al.
(2007) considered the effects of such a ﬂow situation using
modiﬁed analytic models and found that drop phase turbu-
lence results in smaller fragment sizes and reduced breakup
times. However, due to the difﬁculties of measuring drop
phase ﬂow, no known experimental works exist.
Despite these and a few other works discussed by
Lasheras et al. ( 1998), very little is known about the
inﬂuence of turbulence on secondary atomization.
12.4 Charged drops
In electrostatic sprays a charge is applied to the liquid to be
atomized in order to promote fragmentation and assist in
directing the atomized liquid toward a target. Industrial
applications include painting, agricultural sprays, internal
combustion engines, and others.
In a conductive ﬂuid, electrostatic charge will migrate to
the drop surface resulting in a repulsive force that coun-
teracts surface tension. As shown by Shrimpton and
Laoonual (2006) the net surface force, F
surf, thus becomes:
Fsurf ¼ 4prd0 /C0 q2
2pead2
0
ð39Þ
where q is the net charge and ea is the permittivity of the
surrounding ﬂuid. The net surface force goes to zero when
q = q
Ra, where qRa is the Rayleigh charge limit:
qRa ¼
ﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ
8p2read3
0
q
ð40Þ
Rayleigh (1882) showed that an isolated, stationary drop
is unstable at this limit and spontaneously breaks apart.
In processes involving secondary atomization the pres-
ence of electrostatic charge will reduce the effective
surface tension making the drops more likely to fragment.
As ﬁrst suggested by Shrimpton and Laoonual ( 2006), an
electrostatic Weber number, We
e-, can be deﬁned to
account for the effective reduction in surface tension:
Wee/C0 ¼ qaU0d2
0
r /C0 q2/C14
8p2e0d3
0
ð41Þ
Early experimental results from Guildenbecher and
Sojka (2007) indicate that Wee- should be used to deﬁne
the properties of secondary atomization. Nevertheless,
more work is needed to conﬁrm these results and better
characterize the properties of secondary breakup of
charged drops. Especially important is the determination
of ﬁnal fragment sizes and fragment charge distribution.
Also, more work is needed to determine the effect of
charge movement on the breakup process. For example,
during the atomization of highly conductive drops
electrostatic repulsion may lead to locations of high
charge concentration. The spatially varying distribution
of charge will give rise to a non-uniform surface stress.
This may lead to breakup behavior that has not been
observed for un-charged drops. Such behavior warrants
investigation.
12.5 Others
As discussed in previous sections there are a number of
other aspects of secondary atomization where additional
research is warranted. Notable examples include: (1) the
many outstanding issues related to the breakup of non-
Newtonian drops, (2) improving DNS to help answer many
of the questions concerning the physical mechanisms
leading to breakup, (3) advancing drop deformation and
breakup analyses with the goal of creating a model that is
accurate for a wide range of applications, (4) improving
drop size measurement techniques to better characterize
ﬁnal fragment size, and (5) addressing breakup due to a
combination of impulsive and continuous acceleration.
13 Summary and conclusions
The available literature on secondary atomization due to
impulsive acceleration has been reviewed with emphasis
placed on work completed subsequent to reviews by
Pilch and Erdman ( 1987) and Faeth et al. ( 1995). For
Newtonian liquids, breakup is characterized by a mor-
phology consisting of the following modes: vibrational,
bag, multimode, sheet-thinning, and catastrophic. The
process is a strong function of Weber number and relatively
independent of other parameters such as the Ohnesorge
number, Reynolds number, and the density and viscosity
ratios. Each mode has been discussed in detail and experi-
mental correlations are reported which are useful for
designers of spray systems.
Unfortunately, most of these correlations are purely
empirical. As a result, extrapolation outside of the experi-
mental ranges is not advised. To overcome this, models are
needed which are based on the underlying physics.
A thorough review of the many mechanisms that have
been proposed reveals the following: Bag breakup occurs
at the lowest values of Weber number and is the result of
Exp Fluids (2009) 46:371–402 399
123

<!-- PDF_PAGE: 30 -->

the positive pressure difference between the front stagna-
tion point and the wake. This tends to draw the center of
the deformed drop downstream faster than the periphery.
Contrary to this, sheet-thinning breakup occurs at high
values of Weber number when the drop rapidly deforms
into a disk with thin edges. These thin edges are blown
downstream and the drop fragments before the pressure
difference can form the bag structure. At intermediate
values of Weber number, a multimode regime is observed
in which bag and sheet-thinning structures are seen
simultaneously. Finally, at very high values of Weber
number unstable surface waves grow rapidly and dominate
the breakup mechanism. This is referred to as catastrophic
breakup.
A consistent description of the physical mechanisms has
been proposed which is supported by experimental obser-
vation. No dependence on non-dimensional groups is
predicted that has not been observed in experiment. The
previous explanation of shear stripping has been disproven
and was replaced by the more physically correct descrip-
tion of sheet-thinning. More experimental and numerical
results are needed to conﬁrm these mechanisms and create
new correlations based on the underlying physics which
will be useful to future designers of spray systems.
In addition to the above, this paper highlights a number
of other areas in which more experimental and/or numerical
results are needed. Surprisingly, despite the fundamental
nature of the problem and its many important applications, a
thorough understanding of secondary atomization and its
outcomes is elusive.
Acknowledgments The authors would like to thank Prof. Stephen
Heister of Purdue University, Dr. Sachin Khosla of the CFD Research
Corporation, Prof. Rolf Reitz of the University of Wisconsin, and
Prof. David Schmidt of the University of Massachusetts-Amherst for
their stimulating discussions and guidance during the preparation of
this review.
References
Aalburg C, van Leer B, Faeth GM (2003) Deformation and drag
properties of round drops subjected to shock-wave disturbances.
AIAA J 41(12):2371–2378
Apte SV, Gorokhovski M, Moin P (2003) LES of atomizing spray
with stochastic modeling of secondary breakup. Int J Multiphase
Flow 29:1503–1522
Arcoumanis C, Khezzar L, Whitelaw DS, Warren BCH (1994)
Breakup of Newtonian and non-Newtonian Fluids in air jets. Exp
Fluids 17(6):405–414
Arcoumanis C, Whitelaw DS, Whitelaw JH (1996) Breakup of
droplets of Newtonian and non-Newtonian ﬂuids. Atomization
Spray 6:245–256
Babinsky E, Sojka PE (2002) Modeling drop size distributions. Prog
Energ Combust 28:303–329
Berthoumieu P, Carentz H, Villedieu P, Lavergne G (1999) Contri-
bution to droplet breakup analysis. Int J Heat Fluid 20:492–498
Bird RB, Armstrong RRC, Hasseger O (1987) Dynamics of polymeric
liquids. Wiley, New York
Brodkey, RS (1967) Formation of drops and bubbles. In: The
phenomena of ﬂuid motions. Addison-Wesley, Reading
Cao XK, Sun ZG, Li WF, Liu HF, Yu ZH (2007) A new breakup
regime for liquid drops identiﬁed in a continuous and uniform air
jet ﬂow. Phys Fluids 19(5):057103
Chandrasekhar S (1961) Hydrodynamic and hydromagnetic stability.
Oxford University Press, London
Chang CH, Liou MS (2007) A Robust and accurate approach to
computing compressible multiphase ﬂow: stratiﬁed ﬂow model
and AUSM
?-up scheme. J Comput Phys 225:840–873
Chou WH, Faeth GM (1998) Temporal properties of secondary drop
breakup in the bag breakup regime. Int J Multiphase Flow
24:889–912
Chou WH, Hsiang LP, Faeth GM (1997) Temporal properties of drop
breakup in the shear breakup regime. Int J Multiphas Flow
23(4):651–669
Chryssakis CA, Assanis DN (2005) A secondary atomization model
for liquid droplet deformation and breakup under high weber
number conditions. In: ILASS Americas 18th annual conference
on liquid atomization and spray systems, Irvine, CA, USA
Clift R, Grace JR, Weber ME (1978) Bubbles, drops, and particles.
Academic Press, New York
Cohen RD (1994) Effect of viscosity on drop breakup. Int J
Multiphase Flow 20(1):211–216
Cousin J, Yoon SJ, Dumouchel C (1996) Coupling of classical linear
theory and maximum entropy formalism for prediction of drop
size distribution in sprays: application to pressure-swirl atomiz-
ers. Atomization Spray 6:601–622
Dai Z, Faeth GM (2001) Temporal properties of secondary drop
breakup in the multimode breakup regime. Int J Multiphase Flow
27:217–236
Duan RQ, Koshizuka S, Oka Y (2003a) Numerical and theoretical
investigation of effect of density ratio on the critical weber
number of droplet breakup. J Nucl Sci Technol 40(7):501–508
Duan RQ, Koshizuka S, Oka Y (2003b) Two-dimensional simulation
of drop deformation and breakup at around the critical Weber
number. Nucl Eng Des 225:37–48
Dumouchel C (2006) A new formulation of the maximum entropy
formalism to model liquid spray drop-size distribution. Part Part
Syst Char 23:468–479
Dumouchel C, Boyaval S (1999) Use of the maximum entropy
formalism to determine drop size characteristics. Part Part Syst
Char 16:177–184
Faeth GM, Hsiang LP, Wu PK (1995) Structure and breakup
properties of sprays. Int J Multiphase Flow 21(Suppl): 99–127
Gelfand BE (1996) Droplet breakup phenomena in ﬂows with
velocity lag. Prog Energ Combust 22:201–265
Gelfand BE, Gubin SA, Kogarko SM, Komar SP (1975) Singularities
of the breakup of viscous liquid droplets in shock waves. J Eng
Phys 25(3):1140–1142
Go¨kalp I, Chauveau C, Morin C, Vieille B, Birouk M (2000)
Improving droplet breakup and vaporization models by including
high pressure and turbulence effects. Atomization Spray 10:475–
510
Gorokhovski M (2001) The stochastic Lagrangian model of drop
breakup in the computation of liquid sprays. Atomization Spray
11:505–519
Gorokhovski MA, Saveliev VL (2003) Analyses of Kolmogorov’s
model of breakup and its application into Lagrangian computa-
tion of liquid sprays under air-blast atomization. Phys Fluids
15(1):184–192
Guildenbecher DR, Sojka PE (2007) Secondary breakup of electri-
cally charged Newtonian drops. In: Proceedings of IMECE2007,
IMECE2007–4189
400 Exp Fluids (2009) 46:371–402
123

<!-- PDF_PAGE: 31 -->

Han J, Tryggvason G (1999) Secondary breakup of axisymmetric
liquid drops. I. Acceleration by a constant body force. Phys
Fluids 11(12):3650–3667
Han J, Tryggvason G (2001) Secondary breakup of axisymmetric
liquid drops. II. Impulsive acceleration. Phys Fluids 13(6):1554–
1565
Helenbrook BT, Edwards CF (2002) Quasi-steady deformation and
drag of uncontaminated liquid drops. Int J of Multiphas Flow
28(10):1631–1657
Hinze JO (1955) Fundamentals of the hydrodynamic mechanism of
splitting in dispersion processes. AIChE J 1(3):289–295
Hsiang LP, Faeth GM (1992) Near-limit drop deformation and
secondary breakup. Int J Multiphas Flow 18(5):635–652
Hsiang LP, Faeth GM (1993) Drop properties after secondary
breakup. Int J Multiphase Flow 19(5):721–735
Hsiang LP, Faeth GM (1995) Drop deformation and breakup due to
shock wave and steady disturbances. Int J Multiphase Flow
21(4):545–560
Hwang SS, Liu Z, Reitz RD (1996) Breakup mechanisms and drag
coefﬁcients of high-speed vaporizing liquid drops. Atomization
Spray 6:353–376
Ibrahim EA, Yang HQ, Przekwas AJ (1993) Modeling of spray
droplets deformation and breakup. J Propul Power 9(4):651–
654
Igra D, Ogawa T, Takayama K (2002) A parametric study of water
column deformation resulting from shock wave loading. Atom-
ization Spray 12:577–591
Igra D, Takayama K (2001) Investigation of aerodynamic breakup of
a cylindrical water droplet. Atomization Spray 11(2):167–185
Joseph DD, Beavers GS, Funada T (2002) Rayleigh–Taylor instability
of viscoelastic drops at high Weber numbers. J Fluid Mech
453:109–132
Joseph DD, Belanger J, Beavers GS (1999) Breakup of a liquid drop
suddenly exposed to a high-speed airstream. Int J Multiphase
Flow 25:1263–1303
Kalashnikov VN, Askarov AN (1989) Relaxation time of elastic
stresses in liquids with small additions of soluble polymers of
high molecular weights. J Eng Phys Thermophys 57:874–878
Khosla S, Smith CE, Throckmorton RP (2006) Detailed understand-
ing of drop atomization by gas crossﬂow using the volume of
ﬂuid method. Inl: ILASS Americas, 19th annual conference on
liquid atomization and spray systems, Toronto, Canada
Koshizuka A, Oka Y (1996) Moving-particle semi-implicit method
for fragmentation of incompressible ﬂuid. Nucl Sci Eng 123:421
Lasheras JC, Villermaux E, Hopﬁnger EJ (1998) Break-up and
atomization of a round water jet by a high-speed annular air jet.
J Fluid Mech 357:351–379
Lee CH, Reitz RD (1999) Modeling the effects of gas density on the
drop trajectory and breakup size of high-speed liquid drops.
Atomization Spray 9:497–517
Lee CH, Reitz RD (2000) An experimental study of the effect of gas
density on the distortion and breakup mechanism of drops in
high speed gas stream. Int J Multiphase Flow 26:229–244
Lee CS, Kim HJ, Park SW (2004) Atomization characteristics and
prediction accuracies of hybrid break-up models for a gasoline
direct injection spray. P I Mech Eng D-J Aut 218(D9):1041–
1053
Lee CS, Reitz RD (2001) Effect of liquid properties on the breakup
mechanism of high-speed liquid drops. Atomization Spray
11:1–19
Li X, Li M, Fu H (2005) Modeling the initial droplet size distribution
in sprays based on the maximization of entropy generation.
Atomization Spray 15:295–321
Liu AB, Mather D, Reitz RD (1993) Modeling the effect of drop drag
and breakup on fuel sprays. In: SAE International congress and
exposition, SAE 930072
Liu AB, Reitz RD (1993) Mechanisms of air-assisted liquid
atomization. Atomization Spray 3:55–75
Liu Z, Reitz RD (1997) An analysis of the distortion and breakup
mechanisms of high speed liquid drops. Int J Multiphas Flow
23(4):631–650
Lo´pez-Rivera C, Sojka PE (2008) Secondary breakup of non-
Newtonian liquid drops. In: ILASS Europe 22nd European
conference on liquid atomization and spray dystems, Como
Lake, Italy
Matta JE, Tytus RP (1982) Viscoelastic breakup in a high velocity
airstream. J Appl Polymer Sci 27:397–405
Matta JE, Tytus RP, Harris JL (1983) Aerodynamic atomization of
polymeric solutions. Chem Eng Commun 19:191–204
Mugele RA, Evans HD (1951) Droplet size distribution in sprays. Ind
Eng Chem 43:1317–1324
Nomura K, Koshizuka S, Oka Y, Obata H (2001) Numerical analysis
of droplet breakup behavior using particle method. J Nucl Sci
Technol 38(12):1057–1064
O’Donnell BJ, Helenbrook BT (2005) Drag on ellipsoids at ﬁnite
Reynolds numbers. Atomization Spray 15:363–375
O’Rourke PJ, Amsden AA (1987) The TAB method for numerical
calculation of spray droplet breakup. SAE Paper No 872089
Ortiz C, Joseph DD, Beavers GS (2004) Acceleration of a liquid drop
suddenly exposed to a high-speed airstream. Int J Multiphas
Flow 30:217–224
Park JH, Yoon Y, Hwang SS (2002) Improved TAB model for
prediction of spray droplet deformation and breakup. Atomiza-
tion Spray 12:387–401
Park SW, Kim S, Lee CS (2006) Effect of mixing ratio of biodiesel on
breakup mechanisms of monodispersed droplets. Energy Fuels
20(4):1709–1715
Park SW, Lee CS (2004) Investigation of atomization and evaporation
characteristics of high-pressure injection diesel spray using
Kelvin–Helmholtz instability/droplet deformation and break-up
competition model. P I Mech Eng D-J Aut 218:767–777
Pham TL, Heister SD (2002) Spray modeling using Lagrangian
droplet tracking in a homogeneous ﬂow model. Atomization
Spray 12:687–707
Pilch M, Erdman CA (1987) Use of breakup time data and velocity
history data to predict the maximum size of stable fragments for
acceleration-induced breakup of a liquid drop. Int J Multiphase
Flow 13(6):741–757
Prevish TD, Santavicca DA (1998) Turbulent breakup of hydrocarbon
droplets at elevated pressures. In: ILASS Americas, 11th annual
conference on liquid atomization and spray systems, Sacra-
mento, CA, USA
Quan S, Schmidt DP (2006) Direct numerical study of a liquid droplet
impulsively accelerated by gaseous ﬂow. Phy Fluids 18(10):
102103
Ranger AA, Nicholls JA (1969) Aerodynamic shattering of liquid
drops. AIAA J 7(2):285–290
Rayleigh L (1882) On the equilibrium of liquid conducting masses
charged with electricity. Philos Magaz 14:184–186
Schmelz F, Walzel P (2003) Breakup of liquid droplets in accelerated
gas ﬂows. Atomization Spray 13:357–372
Sehgal BR, Nourgaliev RR, Dinh TN (1999) Numerical simulation of
droplet deformation and break-up by Lattice–Boltzmann
method. Prog Nucl Energ 34(4):471–488
Shibata K, Koshizuka S, Oka Y (2004) Numerical analysis of jet
breakup behavior using particle method. J Nucl Sci Technol
41(7):715–722
Shraiber AA, Podvysotsky AM, Dubrovsky VV (1996) Deformation
and breakup of drops by aerodynamic forces. Atomization Spray
6:667–692
Shrimpton JS, Laoonual Y (2006) Dynamics of electrically charged
transient evaporating sprays. I J Numer Meth Eng 67:1063–1081
Exp Fluids (2009) 46:371–402 401
123

<!-- PDF_PAGE: 32 -->

Simmons HC (1977a) The correlation of drop-size distributions in
fuel nozzle sprays part I: the drop-size/volume-fraction distri-
bution. J Eng Power-T ASME 99(3):309–314
Simmons HC (1977b) The correlation of drop-size distributions in
fuel nozzle sprays part II: the drop-size/number distribution.
J Eng Power-T ASME 99(3):315–319
Sussman M, Smereka P, Osher S (1994) A level set approach for
computing solutions to incompressible two-phase ﬂow. J Comp
Phys 114:146–159
Tanner FX (1997) Liquid jet atomization and droplet breakup
modeling of non-evaporating diesel fuel sprays. SAE Trans J
Eng 106:127–140
Tarnogrodzki A (1993) Theoretical prediction of the critical Weber
number. Int J Multiphase Flow 19(2):329–336
Taylor GI (1950) The The instability of liquid surfaces when
accelerated in a direction perpendicular to their planes. I. P
Royal Soc A Math Phys 201:192–196
Taylor GI (1963) The shape and acceleration of a drop in a high-speed
air stream. In: Batchelor GK (ed) The scientiﬁc papers of GI
Taylor, vol III. University Press, Cambridge
Theofanous TG, Li GJ, Dinh TN (2004) Aerobreakup in rareﬁed
supersonic gas ﬂows. J Fluid Eng T ASME 126:516–527
Trinh HP, Chen CP (2006) Development of liquid jet atomization and
breakup models including turbulence effects. Atomization Spray
16:907–932
Trinh HP, Chen CP, Balasubramanyam MS (2007) Numerical
simulation of liquid jet atomization including turbulence effects.
J Eng Gas Turb Power 129:920–928
Tryggvason G (1997) Computational investigation of atomization.
Contract Number F49620-96-1-0356, Report Number A915353
Wadhwa AR, Abraham J, Magi V (2005) Hybrid compressible-
incompressible numerical method for transient drop-gas ﬂows.
AIAA J 43(9):1974–1983
Wadhwa AR, Magi V, Abraham J (2007) Transient deformation and
drag of decelerating drops in axisymmetric ﬂows. Phys Fluids 19
Weber C (1931) The breakup of liquid jets. Zeits Angew Math Mech
11:136–154
Wert KL (1995) A rationally-based correlation of mean fragment size
for drop secondary breakup. Int J Multiphase Flow 21(6):1063–
1071
Wierzba A, Takayama K (1988) Experimental investigation of the
aerodynamic breakup of liquid drops. AAIA J 26(11):1329–1335
Wilcox JD, June RK, Brown HA, Kelley RC (1961) The retardation
of drop breakup in high-velocity airstreams by polymeric
modiﬁers. J Appl Polymer Sci 5(13):1–6
Zaleski S, Li J, Succi S (1995) Two-dimensional Navier–Stokes
simulation of deformation and breakup of liquid patches. Phys
Rev Lett 75(2):244–247
Zhou W, Zhao T, Wu T, Yu Z (2000) Application of fractal geometry
to atomization process. Chem Eng J 78:193–197
402 Exp Fluids (2009) 46:371–402
123
