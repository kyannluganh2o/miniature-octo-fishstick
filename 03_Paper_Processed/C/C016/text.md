<!-- PDF_PAGE: 1 -->

J. Fluid Mech. (2021), vol. 929, A27, doi:10.1017/jfm.2021.860
Shock induced aerobreakup of a droplet
Shubham Sharma1, Awanish Pratap Singh1,S .S r i n i v a sR a o1, Aloke Kumar1
and Saptarshi Basu1,2,†
1Department of Mechanical Engineering, Indian Institute of Science, Bangalore 560012, India
2Interdisciplinary Center for Energy Research (ICER), Indian Institute of Science, Bangalore 560012,
India
(Received 3 July 2021; revised 27 August 2021; accepted 27 September 2021)
The multiscale dynamics of a shock–droplet interaction is crucial in understanding the
atomisation of droplets due to external airﬂow. The interaction phenomena are classiﬁed
into wave dynamics (stage I) and droplet breakup dynamics (stage II). Stage I involves the
formation of different wave structures after an incident shock impacts the droplet surface.
These waves momentarily change the droplet’s ambient conditions, while in later times
they are mainly inﬂuenced by shock-induced airﬂow. Stage II involves induced airﬂow
interaction with the droplet that leads to its deformation and breakup. Primarily, two modes
of droplet breakup, i.e. shear-induced entrainment
and Rayleigh–Taylor piercing (RTP)
(based on the modes of surface instabilities) were observed for the studied range of Weber
numbers (We ∼ 30–15 000). A criterion for the transition between two breakup modes is
obtained, which successfully explains the observation of RTP mode of droplet breakup at
high Weber numbers (We ∼ 800).F o r We > 1000, the breakup dynamics is governed by
the shear-induced surface waves. After formation, the Kelvin–Helmholtz waves travel on
the droplet surface and merge to form a liquid sheet near the droplet equator. Henceforth,
the liquid sheet undergoes breakup processes via nucleation of several holes. The breakup
process is recurrent until the complete droplet disintegrates or external drag acting on
the droplet is insufﬁcient for further disintegration. At lower Weber numbers, the droplet
undergoes complete deformation like a ﬂattened disk, and a multibag mode of breakup
based on RTP is observed.
Key words: drops and bubbles
1. Introduction
The atomisation of liquid droplets by aerodynamic forces is of great importance in many
engineering and industrial applications. This process is widely exploited in the ﬁelds of
† Email address for correspondence: sbasu@iisc.ac.in
© The Author(s), 2021. Published by Cambridge University Press. This is an Open Access article,
distributed under the terms of the Creative Commons Attribution licence ( http://creativecommons.org/
licenses/by/4.0/), which permits unrestricted re-use, distribution, and reproduction in any medium,
provided the original work is properly cited. 929 A27-1
https://doi.org/10.1017/jfm.2021.860
 Published online by Cambridge University Press

<!-- PDF_PAGE: 2 -->

S. Sharma, A.P . Singh, S.S. Rao, A. Kumar and S. Basu
liquid jet atomisation, agricultural spraying, combustion engines, energy systems, nuclear
fusion processes and aerospace applications (Bayvel 1993; Eggers & Villermaux 2008;
Shinjo & Umemura 2011; Lefebvre & McDonell 2017). This topic has been extensively
studied by researchers from incompressible to compressible ﬂow regimes through the
application of air-jet ﬂow (Cao et al. 2007; Zhao et al. 2013) and shock tubes ﬂow (Sun
et al. 2005;L i a n get al. 2020) for varying viscosities of Newtonian (Chang, Deng &
Theofanous 2013;K e s h a v a r zet al. 2016;Y a n g&P e n g2019) and non-Newtonian ﬂuids
(Joseph, Belanger & Beavers 1999; Theofanous et al. 2012; Zhao et al. 2012). The varying
morphologies in the droplet breakup process for shock tube studies are generally presented
by means of deformation, breakup and secondary atomisation , depending on the droplet
size and ﬂow conditions (subsonic to supersonic). In this context, understanding the
dynamic behaviour and breakup methodologies for different conditions is essential.
A wide range of experimental and numerical studies in the literature has investigated
the droplet breakup mechanisms using the shock tube method. However, limited studies
have emphasised the importance of early-stage shock wave interaction in the breakup
analysis (Meng & Colonius 2015; Sembian et al. 2016; Tanno et al. 2003;S u n et al.
2005). Sembian et al. (2016) used experimental and numerical techniques to explain the
evolution dynamics of reﬂected, transmitted and diffracted waves during the interaction of
an incident shock wave with a cylindrical water column. The possibility of cavitation in the
droplet due to the expansion wave focusing at higher shock Mach numbers was observed.
A numerical simulation by Meng & Colonius ( 2015) and Guan et al. (2018) illustrated the
development of recirculating ﬂow near the equator region and an upstream jet at the droplet
wake, which eventually assists in droplet deformation and breakup. Similar wave and ﬂow
dynamics were observed in the numerical simulation by Das & Udaykumar ( 2020). In
addition to deformable dispersions, several works were focused on understanding the wave
dynamics of a planar shock wave interaction with solid dispersions (Tanno et al. 2003;
Sridharan et al. 2015; Mehta et al. 2016, 2018). Tanno et al. (2003) studied the interaction
with a solid sphere and used holographic double exposure interferometry to show that
the sphere experiences the maximum drag force during the transition of reﬂection wave
from regular to Mach reﬂection. The work of Sridharan et al. (2015), Mehta et al. (2016)
and Mehta et al. (2018) was focused on understanding the variation of drag coefﬁcient
experienced by a particle with varying interparticle distances in a random (Mehta et al.
2018), inline (Sridharan et al. 2015) and transverse orientation (Mehta et al. 2016).
Subsequently, the dependence of droplet breakup mode with Ohnesorge number (Oh =
μl/√ ρlσDi) and Weber number (We = ρaV2
i Di/σ) w a ss p e c i ﬁ e db yH i n z e(1955) which
was further extended by Krzeczkowski ( 1980) to mark the transition points on the
We− Oh regime. Here, μl and ρl are dynamic viscosity and density of droplet, σ is
the surface tension of the air–liquid interface, Di is the initial droplet diameter before
shock interaction, ρa and Vi are the density and velocity of airﬂow post shock conditions.
The Weber number accounts for relative dominance of aerodynamic/inertial force to the
surface tension force, while the Ohnesorge number accommodates the effect of liquid
viscosity on breakup dynamics. For viscoelastic ﬂuids and viscous Newtonian ﬂuids, the
deformation and breakup of a droplet through bag and stamen process at higher Weber
numbers is reported in the study of Joseph et al. (1999). The increasing Oh values lead to
retardation in the deformation and breakup process, while negligible inﬂuence of viscosity
was observed for Oh < 0.1 (Hsiang & Faeth 1992). Numerous reviews consolidated
the droplet fragmentation modes and corresponding breakup transition criteria (Pilch &
Erdman 1987; Guildenbecher, López-Rivera & Sojka 2009; Theofanous 2011). Primarily
,
ﬁve modes of aerodynamic breakup of a droplet , i.e. bag breakup (24 > We > 11),
929 A27-2
https://doi.org/10.1017/jfm.2021.860
 Published online by Cambridge University Press

<!-- PDF_PAGE: 3 -->

Shock induced aerobreakup of a droplet
bag-stamen/plume breakup (65 > We > 24), multibag breakup (85 > We > 65), sheet
thinning/stripping breakup (120 > We > 85) (Jain et al. 2015) and catastrophic breakup
(We > 350) (Guildenbecher et al. 2009) are obtained for Oh < 0.1 based on different ﬂow
Weber number values. The breakup phenomenon in the direction of air-jet ﬂows with
the formation of multimode structures due to Rayleigh–Taylor instability (RTI) at lower
We of 15–40 was studied by Cao et al. (2007) and Zhao et al. (2013). The transition of
various breakup modes to the shear breakup regime with the formation of liquid sheets
at the equator along with the effect of viscosity and density ratios were presented by
Chou, Hsiang & Faeth ( 1997), Han & Tryggvason (2001)
and Jain et al. (2015). Similarly,
shear stripping of the secondary droplets with the impact of a shock wave was visualised
by Nicholls & Ranger ( 1969), Chou et al. (1997), Theofanous & Li ( 2008), Jalaal &
Mehravaran (2014), Meng & Colonius ( 2015), Biasiori-Poulanges & El-Rabii ( 2019)a n d
more recently by Wanget al. (2020) and Dorschner et al. (2020). Nicholls & Ranger (1969)
showed that the droplets ’ breakup mainly occurs due to the induced airﬂow behind the
shock wave, while Chou et al. (1997) focused on identifying size and velocity distribution
of fragmented droplets.
Theofanous & Li ( 2008) briefed that the previously identiﬁed catastrophic breakup
regime was an artefact of experimental techniques used in such works. Biasiori-Poulanges
&E l - R a b i i(2019) used high-magniﬁcation and high-speed breakup images of interaction
to demonstrate the evolution dynamics of
the breakup process at a higher Weber number
of 540–1350. Further, subsonic to supersonic velocity of induced ﬂow was considered
by Wang et al. (2020) for identifying the individual effects of shock Mach number ( M
s)
and Reynolds number ( Re) on breakup dynamics while holding the Weber number as a
constant. Recently, Dorschner et al. (2020) carried out a three-dimensional simulation on
a droplet exposed to high-speed airﬂow to show the ligament formation and shedding as
functions of Weber number and vortex shedding at the droplet wake. The above discussed
different breakup modes were further reclassiﬁed (Theofanous & Li 2008; Theofanous
2011; Theofanous et al. 2012) based on hydrodynamics instabilities responsible for such
breakups. In this context, for We < 100, the previously identiﬁed bag, bag-stamen and
multibag breakup modes, were consolidated as the Rayleigh–Taylorpiercing (RTP) mode
(based on RTI). Similarly, at higher Weber numbers (We > 1000) previously identiﬁed
sheet thinning/stripping and catastrophic modes were consolidated as a shear-induced
entrainment (SIE) mode (based on Kelvin–Helmholtz instability (KHI)). The same
description for the two modes is used in the present work.
The hydrodynamic instabilities, primarily the RTI, KHI and Rayleigh–Plateau
instability (RPI) play a crucial role in predicting the droplet morphology during
aerodynamic atomisation of a droplet. Historically RTI is shown to be the driving
cause for the breakup modes involving bag formation (Zhao et al. 2010; Theofanous
2011;J a i n et al. 2015), where different bag-type breakups are predicted based on the
dimensionless parameter (N = D
i/λRT). Here, λRT is the Rayleigh–Taylor (RT)-based
instability wavelength. The existing literature shows the existence of bag-breakup for
N = 1/
√
3–1, bag-stamen for N = 1–2 and multibag mode of breakup for N > 2 (Zhao
et al. 2010;J a i net al. 2015), where the RTI wavelength is predicted from conventional
RT analysis (Rayleigh 1879). Recently, Theofanous ( 2011) and Theofanous et al. (2012)
used ﬁnite thickness RTI analysis for a two-phase system to identify the condition
for the ﬁrst criticality, i.e. bag formation process. In contrast to the bag-type mode
of droplet breakup, the shear-induced breakup of a droplet is driven by the KHI
on the droplet surface (Theofanous & Li 2008; Theofanous et al. 2012; Jalaal &
Mehravaran 2014;L i uet al. 2018; Biasiori-Poulanges & El-Rabii 2019;W a n get al. 2020).
929 A27-3
https://doi.org/10.1017/jfm.2021.860
 Published online by Cambridge University Press

<!-- PDF_PAGE: 4 -->

S. Sharma, A.P . Singh, S.S. Rao, A. Kumar and S. Basu
Here Kelvin–Helmholtz (KH) waves are augmented by the action of shear on the liquid–air
interface. Although this mechanism of droplet breakup at high Weber number ( We >
1000) is discussed in many works, an actual attempt to compare the formed KHI waves
with the theoretical analysis is still limited (Marmottant & Villermaux 2004;K i m et al.
2006; Theofanous et al. 2012; Jalaal & Mehravaran 2014) and most of which are primarily
numerical (Kim et al. 2006; Jalaal & Mehravaran 2014)o r seminumerical (Theofanous
et al. 2012), while the experimental works are related to liquid–air interaction in a coaxial
jet system (Marmottant & Villermaux 2004). Further, the RPI mode of instability was
observed in the secondary atomisation of formed ligaments during the breakup of the
primary droplet (Biasiori-Poulanges & El-Rabii 2019). All these modes of interfacial
instabilities are explained in the context of aerodynamic atomisation in the present work.
The aerodynamic breakup of a liquid droplet is a high-speed phenomenon where
the droplet disintegration is completed within the time scales of several hundred
microseconds, particularly at higher Weber numbers ( We > 1000). A high-speed
interaction dynamics is difﬁcult to perceive through numerical and experimental means
due to short time scales and the multiscale nature of the breakup phenomenon. The
disintegration of a millimetre-sized primary droplet into micron-sized daughter droplets
within a time scale of few microseconds requires high spatiotemporal resolution. Although
numerical advancement in this direction can be achieved by increasing the computational
cost (Poplavski et al. 2020), and has also been attempted much efﬁciently in recent
times (Jalaal & Mehravaran 2014; Meng & Colonius 2015; Guan et al. 2018;L i u et al.
2018; Dorschner et al. 2020), the experimental works pertaining to high spatiotemporal
resolution are still lacking. For example, a high-speed camera’s ﬁeld of view must be
compromised to increase the temporal resolution. In addition to this, the spatial resolution
has to be further compromised to accommodate the possible uncertainties in the falling
droplet and incoming shock wave locations between the experimental runs. The usage
of high exposure times (even within microsecond order) results in the motion blur
of fast-moving atomised droplets, which can lead to a misinterpretation of the actual
phenomenon (as discussed by Theofanous & Li ( 2008)). Correspondingly, the high-speed
breakup dynamics of the liquid droplet is essentially a three-dimensional phenomenon,
thereby necessitating the interaction observations through multiple viewing angles, further
increasing the experimental complexities. Therefore, a highly sophisticated and optimised
experimental arrangement is required for effectively capturing the
multiscale nature of the
droplet’s aerodynamic breakup and involved physical phenomenon. Several experimental
studies in the recent literature have attempted some of these aspects (Theofanous
&L i 2008; Biasiori-Poulanges & El-Rabii 2019; Jackiw & Ashgriz 2021); however,
a more comprehensive study providing benchmark measurement data for numerical
simulation, involving a wide parametric range and covering complete evolution dynamics
of interaction phenomenon is still lacking.
From a physics perspective, earlier works were focused on identifying the various modes
of droplet breakup, primarily at low Weber numbers ( We < 250) (Guildenbecher et al.
2009; Zhao et al. 2010;J a i net al. 2015; Zhao et al. 2018) and predicting various breakup
modes using stability analysis. At higher Weber numbers (We > 1000) observations are
primarily made through numerical simulations (Jalaal & Mehravaran 2014; Guan et al.
2018;L i u et al. 2018; Biasiori-Poulanges & El-Rabii 2019; Dorschner et al. 2020).
However, most of these works lack the accurate prediction of the atomisation stage,
requiring high
spatiotemporal resolutions. Several experimental studies have been reported
in this regime (Theofanous & Li 2008; Theofanous et al. 2012; Biasiori-Poulanges &
El-Rabii 2019; Dorschner et al. 2020;W a n g et al. 2020) which primarily focused on
identifying the evolution of the droplet breakup process in the SIE regime. However, a
929 A27-4
https://doi.org/10.1017/jfm.2021.860
 Published online by Cambridge University Press

<!-- PDF_PAGE: 5 -->

Shock induced aerobreakup of a droplet
clear understanding of the three-dimensional breakup process is still lacking, and limited
attempts have been made (Theofanous et al. 2012; Biasiori-Poulanges & El-Rabii 2019)
for comparing the observed surface instabilities with theoretical analysis. The existing
literature shows a monotonous dependence of breakup mechanism on Weber number, i.e.
breakup mode changes from RTP to SIE with the increase in Weber number. However, in
the present work, by using
submillimetre to millimetre-sized deionised water droplets, we
obtained an essential criterion that shows that RTP can exist at a high Weber number of
∼ 800. Similarly, SIE can exist at lower We ∼ 200, thereby exhibiting
a non-monotonous
dependence on Weber number.
In this context, the present study addresses the full interaction dynamics of a liquid
droplet interacting with a shock wave of varying Mach numbers ( Ms ∼ 1.1 to 1.8). The
effect of aerodynamic breakup on different droplet sizes ( Di = 0.5, 2.5a n d2 .9 mm) is
studied by employing visualisation techniques such as schlieren and shadowgraphy to
understand the signiﬁcant ﬂow features and structural morphologies during the regimes
of deformation and disintegration of the droplet. The experimental set-up of the shock
tube is further simpliﬁed in design for generation of the required shock wave through the
exploding wire technique. The sophisticated and optimised experimental arrangement used
in the present work addressed the concern of high spatial-temporal imaging of interaction
phenomena. The initial shock interaction ﬂow features were quantiﬁed in detail for the
local ﬂow conditions and the possible deformation shapes depending on the size of droplet
and shock Mach numbers. A wide range of Weber number values (We ∼ 30–12 000)
resulted in the observation of both RTP and SIE modes of droplet breakup. An essential
criterion for the transition of breakup modes is also discussed.
This paper is organised as follows
. Section 2 provides the details of experimental
set-up and methodology used, the results and discussion of this work , which involves
explanations on the shock–droplet interaction mechanism (§ 3.1), global observation of
phenomena (§ 3.2), SIE breakup (§ 3.3), KH waves surface instability (§ 3.4) and breakup
mode transition mechanism (§ 3.6),a r es h o w ni n§3. The conclusions of the present study
are provided in § 4.
2. Experimental set-up
The interaction of a freely falling droplet with a shock wave is carried out in a specially
designed shock tube apparatus based on the exploding wire technique, which offered the
possibility to operate at the desirable shock Mach numbers ( Ms) ranging from 1.1 to 1.8.
A detailed overview of the exploding wire technique and its application in shock wave
generation can be found elsewhere (Fedotov-Gefenet al. 2010; Liverts et al. 2015; Sembian
et al. 2016). This technique offers several advantages compared with diaphragm-based
shock tubes, such as small size test facilities, ease of operation, generation of a wide range
of shock strengths ( M
s = 1–6) (Sembian et al. 2016) and high repeatability between tests.
A schematic representation of the experimental test cavity is shown in the ﬁgure 1 (a).
T wo separate ﬂow channels (rectangular) are designed with dimensions of 360 mm ×
50 mm × 20 mm and 400 mm × 50 mm × 10 mm, resulting in a wide range of shock Mach
numbers. The sidewalls of the ﬂow channel and the cover plates of the exploding chamber
are fabricated using polycarbonate due to its high impact strength, while acrylic cover
plates are used on the remaining length ( ﬁgure 1 a). The cover plates are ﬁrmly attached
with screws to prevent compressed air from escaping. The shock tube is attached to the
electrode chamber (by
a nut and bolt arrangement), where the copper wire (of 35 SWG) is
securely placed between two electrodes. A high-voltage power supply is connected to the
two electrodes to accomplish the wire-blast system.
929 A27-5
https://doi.org/10.1017/jfm.2021.860
 Published online by Cambridge University Press

<!-- PDF_PAGE: 6 -->

S. Sharma, A.P . Singh, S.S. Rao, A. Kumar and S. Basu
Dispensing
needle
(a)( b)
Droplet
Laser
detector
Arduino
board
High-speed
camera
High-speed
laser
High-voltage
trigger unit
Digital delay
generator
Droplet
dispenser
+5 V
trigger
signal
1 kV
trigger signal
Exploding
wire
Variable
spark gap
Charging
voltage
Rectifier VTransformer
Low voltage (max 240 V)
Variable
resistance
Switch
L
N
High-voltage pulse power unit
High voltage (5 kV to 30 kV)
5 µF
capacitor
Test
section
Exploding
chamber
Electrode
chamber
High-voltage electrodes
Figure 1. Exploding-wire based shock tube set-up. ( a) Schematic diagram of shock tube and actual shock
tube tower; and (b) electrical wiring diagram for high-voltage pulse power unit and triggering set-up.
The wiring diagram (simpliﬁed version) for the management of the 2 kJ high-voltage
pulse power system (Zeonics Systech, India (Z/46/12)), which is used for the wire
explosion and synchronisation of the various instruments for the experimentation process,
is shown schematically in ﬁgure 1 (b). For the generation of a high-voltage pulse, the
incoming AC power supply is altered to the required voltage range of 5 kV to 12 kV
through a step-up transformer. The high voltage AC power supply is then converted to
DC power with a rectiﬁer arrangement which is then further used for charging a 5 μF
capacitor. Once the charging of the capacitor to the desired energy level is complete,
the charging circuit is cut off, and the discharging circuit connected to the exploding
wire is closed by providing a 1 kV trigger signal from the high-voltage trigger unit
(which is activated by a trigger signal from the digital delay generator) at the variable
spark-gap switch. Once the unit is triggered, a high-voltage pulse is discharged from
the electrodes and passes through a thin copper wire, which results in rapid Joule’s
heating, vaporisation of the wire and generation of a cylindrical blast wave, which is
called the exploding-wire technique. The induced blast wave inside the rectangular column
is transformed to a planar shock by the narrow geometry of ﬂow channel (Sembian
et al. 2016). The formed shock wave interacts with the water droplet at a distance of
15 mm from the column exit point in open ambient conditions. This conﬁguration is
chosen due to several limitations of doing experiments inside the shock tube channel,
such as the sticking of stripping droplets on cover plates during droplet breakup, which
hinders the visualisation of the interaction phenomena and formation of reﬂected waves
from the inner walls of the shock tube. Further, no signiﬁcant difference is observed in the
shock wave dynamics carried out inside and outside of the shock tube (see supplementary
movie 1 available at https://doi.org/10.1017/jfm.2021.860). The synchronisation of droplet
ejection, its interaction with a shock wave and simultaneous capturing of interaction
phenomena are done within
nanosecond accuracy using a BNC 745 T digital delay
generator.
The deionised water droplet dispensing system is aligned above and at a central position
of the shock tube cavity. The ejected droplet diameter ranges from 2.9 mm to 0.5 mm, in
which a syringe pump (New Era Pump Systems, NE-1010) based droplet ejection is used
for droplet sizes greater than 1 mm, and a Nordson PICO Pμlse dispensing system is used
for sizes less than 1 mm. The syringe pump ejects a precise volume of droplet/ﬂuid during
the infusion of the syringe with precise rotation of the stepper motor, while the Nordson
929 A27-6
https://doi.org/10.1017/jfm.2021.860
 Published online by Cambridge University Press

<!-- PDF_PAGE: 7 -->

Shock induced aerobreakup of a droplet
High-speed
laser beam
High-speed
laser beam
High-speed
laser
Diode
laser
(a)( b)
(c)
Diode
laser
Beam
collimator
Beam
collimator
Ejected
droplet Ejected
droplet
Dispensing
needle
Dispensing
needle
High-speed
camera
High-speed
camera
High-speed
camera
Laser
detector
Laser
detectorShock tube
channel
Shock tube
Shock tube Knife
edge
S
M1 M2
Exploding
wire chamber
High-voltage
electrodes
Figure 2. Experimental arrangement and imaging set-up. ( a) Shadowgraphy imaging and laser interrupter
set-up; (b) inclined top-view imaging set-up; and ( c) schlieren imaging set-up.
PICO Pμlse dispenser uses a piezoelectric-based precise droplet ejection mechanism.
The free-falling droplet is detected at a speciﬁc position from the ejection point by its
obstruction to a
laser detector system, which is placed in the pathline of the falling droplet
as shown in ﬁgure 2(a). Detected obstruction of the laser beam is used as a trigger signal to
the digital delay generator as presented in the schematic view in ﬁgure 1(b). A high-speed
pulse laser system, high-speed camera, high-voltage unit and a droplet dispenser unit are
connected to the digital delay generator to trigger all the components at once with initial
delay time intervals, which is operated from the external source (i.e. a personal computer).
As the experiments are to be operated at microsecond time scales, the integration of all
the components is vital for the experimentation to attain the subsequent droplet breaking
phenomenon from initial drop ejection to shock wave generation, interaction, deformation
and secondary atomisation of the droplet. The phenomenon of the droplet breakup process
are essentially recorded through three imaging techniques such as shadowgraph imaging,
top-view imaging and
schlieren imaging.
Interaction of the shock wave and droplet breakup process for varying droplet sizes are
captured by employing the shadowgraph technique as shown in ﬁgure 2(a). A high-speed
and non-coherent pulse diode laser of 640 nm wavelength (Cavitar Cavilux smart UHS,
400 W power) is used for capturing the droplet breakup process at the laser pulse width
of 10–40 ns. The use of
nanosecond-scale pulse duration of a light source is essential for
freezing the high-speed interaction phenomena. The emitted light beam is transformed into
929 A27-7
https://doi.org/10.1017/jfm.2021.860
 Published online by Cambridge University Press

<!-- PDF_PAGE: 8 -->

S. Sharma, A.P . Singh, S.S. Rao, A. Kumar and S. Basu
a parallel light beam using a collimator lens (Thorlabs, BE20M-A). A high-speed camera
(Photron, SA5) is aligned in line to the beam source as shown in ﬁgure 2(a) which captures
the shadow image of the disintegrating droplet during its interaction with the shock wave.
The high-speed pulse laser source is synchronised with the high-speed camera for all
frame rates ranging from
20 000 to 100 000 frames per second (f.p.s). The experimental
images have been captured using the shadowgraph technique with extensive zoom-in and
zoom-out views of the interaction to study the droplet surface instabilities and whole-ﬁeld
droplet breakup processes at different shock Mach numbers and droplet sizes. Further,
to capture the breakup process in
top view, the high-speed laser and camera system is
aligned at a 20-degree orientation with the vertical axis using the assistance of heavy-duty
tripod stands as shown in ﬁgure 2 (b). The top-view arrangement is essential for an
augmented understanding of the three-dimensional breakup process, as will be discussed
later in § 3.5. The characteristics of the droplet and its breakup process can be assessed
explicitly using shadowgraphy, whereas the initial shock wave interaction phenomenon
and ﬂow ﬁeld dynamics around the droplet are quantiﬁed by using the schlieren
technique.
The alignment of the schlieren system is presented schematically in ﬁgure 2 (c). The
emitted beam from the pulse laser source is transformed to a point light source using
variable round aperture (Holmarc SSID-25). This aperture acts as a point light source
for the concave mirror (M1) oriented at its focal length, forming a parallel light beam.
The test cavity is aligned in the path of a parallel beam for recording the shock–droplet
interaction phenomena. Further, the light beam passes through the second spherical
concave mirror (M2) and is focused to a point at the focal length of the mirror where a
knife edge is positioned to block half of the incoming light in order to attain the variation
of the density gradients during the interaction phenomena. This arrangement facilitates
visualising complicated wave structures and ambient ﬂuid ﬂow features around the droplet
during the initial interaction stages.
In the present work, the experiments are performed on different shock-Mach numbers
(M
s = Vs/c) ranging from 1.1 to 1.85 by the application of 5 to 12 kV of charging
voltage (Vc) to the capacitor and two separate shock tube channels (see ﬁgure 3 a).
Here, Vs is the shock wave velocity, and c is the speed of sound in the medium ahead
of the shock wave. The shock wave velocity is estimated by measuring the distance
travelled by the shock wave in the two consecutive images recorded at 0.1 M f.p.s.
A comparison of this instantaneous shock velocity with the average velocity of the
shock wave measured between two distant locations in the camera ﬁeld is also made,
which shows a negligible difference between the two results, indicating a minimal loss
of shock strength during the studied time duration. Primarily, the shock velocity is a
direct function of the applied charging voltage, as can be seen from ﬁgure 3 (a). On the
basis of obtained shock Mach numbers and the induced ﬂow velocities (Anderson 2003),
Weber number and Reynolds number (Re = ρ
aViDi/μa) for varying droplet diameters
(2.9 mm to 0.5 mm) are estimated (see ﬁgure 3 b,c). Here, μa is the dynamic viscosity
of the induced ﬂow post shock conditions. The Weber number and Reynolds number
in the present work ranges from ∼ 30 to 12 000 and ∼ 3000 to 100 000, respectively.
Droplets are dispensed in such a manner that their spherical shape is maintained.
However, a slight deviation from the sphericity is observed, which was found to be
0.945 ± 0.04, 0.972 ± 0.02
and 0 .911± 0.06 for droplet size of 2.9 mm, 2.5 mm and
0.5 mm, respectively. A completely spherical droplet will have its roundness value of
unity. The results of the observed interaction dynamics are presented in the following
sections.
929 A27-8
https://doi.org/10.1017/jfm.2021.860
 Published online by Cambridge University Press

<!-- PDF_PAGE: 9 -->

Shock induced aerobreakup of a droplet
1.9(a)( b)
(c)
Channel 1
Channel 2
Channel 1 Di ˜ 2.5 mm
Channel 1 Di ˜ 0.5 mm
Channel 2 Di ˜ 2.9 mm
Channel 1 Di ˜ 2.5 mm
Channel 1 Di ˜ 0.5 mm
Channel 2 Di ˜ 2.9 mm
1.8 104
103
102
Weber number (We)
101
105
104
Reynolds number (Re)
103
1.7
1.6
1.5
1.4
Shock mach number (Ms)
1.3
1.2
1.1
1.9 2.01.81.71.61.51.4
Shock mach number (Ms)
1.31.21.1
1.9 2.01.81.71.61.51.4
Shock mach number (Ms)
1.31.21.1
56 78
Charging voltage (Vc, kV)
91 0 1 1
Figure 3. Range of non-dimensional parameters for channel 1 and channel 2. ( a) Shock Mach number ( Ms)
versus charging voltage (Vc) in kilo-Volts; (b) Weber number (We) versus shock Mach number (Ms) for different
droplet sizes ( Di ∼ 2.9, 2.5m ma n d ∼ 0.5 mm); and ( c) Reynolds number ( Re) versus shock Mach number
(Ms) for different droplet sizes ( Di ∼ 2.9, 2.5m ma n d∼ 0.5 mm).
3. Results and discussions
3.1. Shock–droplet interaction mechanism
The interaction of an incident shock wave with a droplet surface leads to different wave
structures like reﬂected wave, transmitted wave, Mach- stem and diffracted wave, which
affects the ﬂow conditions around the droplet periphery. Although these features are
physically present, some features like transmitted wave, external and internal ﬂow ﬁeld
of a droplet are difﬁcult to perceive using currently available experimental techniques.
The transmitted wave cannot be visualised due to the limitation of shadowgraphy and/or
schlieren imaging techniques and due to the spherical shape of the droplet which acts
as a lens during shadowgraphy/schlieren imaging. The ﬂow dynamics could not be
obtained experimentally due to the requirement of a high-resolution and high-frame-rate
particle image velocimetry system (minimum requirement of 20 000–40 000 f.p.s.), which
necessitates the usage of a high-power pulse-burst laser system (Beresh et al. 2015).
In addition, there are several challenges associated with seeding particles in supersonic
and shock tunnel ﬂows (Havermann et al. 2008). However, due to advancements in
numerical methods and existing computational power, it is now possible to observe these
features using numerical techniques as reported recently by several researchers (Chen
2008; Sembian et al. 2016; Sridharan et al. 2016; Guan et al. 2018; Das & Udaykumar
929 A27-9
https://doi.org/10.1017/jfm.2021.860
 Published online by Cambridge University Press

<!-- PDF_PAGE: 10 -->

S. Sharma, A.P . Singh, S.S. Rao, A. Kumar and S. Basu
Droplet
(a)
(e)( f )( g)
(b)( c)( d)
(h)( i)( j)( k)
(l)( m)( n)( o)
   Incident
shock wave
Incident
wave
Incident
wave
Mach
stem
Focusing of reflected
expansion wave
Reflected
wave
Reflected
wave
Slip
surface
Triple
point
Transmitted
wave
Tail of expansion wave
Head of
expansion wave
V1, V2
SP
V1, V2
V3, V4
Mach–Mach collision Recirculation
region
Shock dynamicsFlow dynamics
Transmitted
wave
Figure 4. Shock–droplet interaction mechanism. ( a–g) Shock wave dynamics during different time instances;
and ( h–o) external (red lines) and internal (blue lines) ﬂow streamlines for a droplet at different time
instances.
2020; Poplavski et al. 2020). Therefore, the discussion in the current subsection is
based on the experimental observations of the present work and some ﬂow features
established in the above numerical studies. Figure 4 schematically shows the
shock
dynamics ( ﬁgure 4 a–g) and ﬂow dynamics ( ﬁgure 4 h–o) realised during shock–droplet
interaction. Figure 5 presents the schlieren images recorded at 0.42 M f.p.s. with a pixel
resolution of 64 × 96 pixels and corresponds to the features shown in ﬁgure 4.
The incident shock interaction on the droplet surface creates a reﬂected wave, a
transmitted wave and a diffracted wave. Depending on the acoustic impedance (Z = ρc)
of the medium on either side of the interface, the reﬂected wave can be a shock wave or
an expansion wave (Henderson 1989). It is interesting to note that if the medium through
which the wave has travelled before reﬂection has a lower impedance than the medium
on the other side of the reﬂecting surface, the reﬂected wave will be a shock wave and
vice versa. For the current case, the reﬂected wave will be a shock wave (Zwater > Zair)
(ﬁgures 4b,i and 5b). The reference time (t) is measured from the ﬁrst instance of the shock
interacting with the droplet surface. The reference time is non-dimensionalised using the
inertial time scale (τ= Di/Vi
√ ρl/ρa) as t∗ = t/τ. The planar incident wave will undergo
regular reﬂection until the incidence angle (αi) is greater than the critical detachment
angle (αc) (Ben-Dor 2007). If αi <α c, a regular reﬂection is not possible and transition
to Mach reﬂection occurs ( ﬁgures 4c,j and 5c). A triple point is formed at the intersection
of the incident wave, reﬂected wave and Mach stem. A slip surface is also formed at the
intersection of the Mach wave and droplet surface. A uniform stream of induced airﬂow
929 A27-10
https://doi.org/10.1017/jfm.2021.860
 Published online by Cambridge University Press

<!-- PDF_PAGE: 11 -->

Shock induced aerobreakup of a droplet
Incident
wave
Reflected
wave7 mm
Ms = 1.45 We = 3.9 × 103 Re = 6.5 × 104
t∗ = 0 t∗ = 0.01
t∗ = 0.08 t∗ = 0.36 t∗ = 0.44
t∗ = 0.02 t∗ = 0.04
Recirculating
flow
Mach stem
(e)
(b)(a)( c)( d )
( f )( g)
Figure 5. Schlieren images recorded at 0.42 M f.p.s. with 64 × 96 pixels resolution showing shock–droplet
interaction mechanism. ( a) Falling droplet approaches to the incident shock wave; ( b) formation of reﬂected
wave; (c) Mach reﬂection; ( d) focusing of Mach waves at the leeward side of the droplet; ( e) generation of
primary vortical structure near leeward side of droplet; ( f ) droplet deformation and vortex stripping; and
(g) stripping of daughter droplets from the primary droplet periphery.
follows the incoming incident shock wave (see ﬁgure 4 h). The formed reﬂected shock
wave deﬂects the uniform airﬂow as it pass through it ( ﬁgure 4 i–l). The induced ﬂow
remains subsonic in all the cases studied in this work; therefore, it gets deﬂected during its
motion around the droplet surface without creating any other shock structures. The liquid
motion inside the droplet and a high-pressure region near the droplet’s front stagnation
point prompted windward surface deformation of the droplet.
If the incident wave is a shock wave, the transmitted wave will always be a shock
wave (Henderson 1989; Sembian et al. 2016; Guan et al. 2018; Das & Udaykumar 2020)
(ﬁgure 4 b). The transmitted wave moves inside the droplet, resulting in a high-pressure
region behind it and an induced ﬂuid ﬂow towards the leeward side of the droplet (ﬁgure 4i)
(Guan et al. 2018). As the pressure waves can travel faster in water in comparison
with
air, the transmitted wave gets detached from the incident wave and reaches the droplet’s
leeward side at an earlier instant ( ﬁgure 4 c,j) (Sembian et al. 2016; Das & Udaykumar
2020). On reaching the air–water interface at the leeward side,the transmitted wave reﬂects
as an expansion wave ( Zair < Zwater) (Henderson 1989) which focuses at a point inside
droplet due to the concave proﬁle of reﬂecting surface ( ﬁgure 4d). Following focusing, the
expansion wave propagates towards the windward side, where it is again reﬂected from
the interface. This reﬂection of the transmitted wave from the windward and leeward side
of the droplet continues with some energy loss after every collision until it completely
decays.
929 A27-11
https://doi.org/10.1017/jfm.2021.860
 Published online by Cambridge University Press

<!-- PDF_PAGE: 12 -->

S. Sharma, A.P . Singh, S.S. Rao, A. Kumar and S. Basu
Diffraction of the Mach stem occurs after passing the equator point of the droplet. This
contributes towards the lagging of the Mach wave near its contact point with the droplet
surface ( ﬁgure 4 e,k). The Mach wave is formed axisymmetrically around the droplet
surface and focuses at a point near the rear stagnation point ( ﬁgures 4 f,l and 5d) which
strengthens the shock and creates a local high-pressure region at that location. The internal
ﬂow direction remains unidirectional towards the leeward side of the droplet until the
shock focuses at the droplet’s rear stagnation point ( ﬁgure 4 i–l). A high-pressure region
at the rear stagnation point deforms the droplet surface locally, triggering an upstream
ﬂow inside the droplet. The two counteracting ﬂows, i.e. downstream ﬂow from front
stagnation point and upstream ﬂow from rear stagnation point interact with each other at
the local saddle point inside the droplet, which divert the two ﬂows towards the droplet
equator ( ﬁgure 4 m,n). During the development of external airﬂow around the droplet
periphery, a toroidal vortex (primary vortex) is formed near the ﬂow separation point
(ﬁgure 4m), similar to the external ﬂow around a solid sphere of similar Reynolds number.
In later times, the primary vortex moves downstream and forms a recirculation ﬂow region
and effectuate a jet ﬂow at the rear stagnation point. T wo counter-rotating secondary
vortices V2 and V3, that
interact with the droplet surface are also formed between the
ﬂow separation point and the recirculating ﬂow region. Subsequent to focusing at a point,
Mach waves propagate on the leeward surface, thereby increasing the inﬂuence of the
high-pressure region ( ﬁgures 4 m and 5d,e). The combined effect of recirculated jet ﬂow
and spreading of the high-pressure region ﬂattens the leeward side of the droplet and
deforms it into a cupcake shape ( ﬁgures 4 n and 5 f ). The observed wave dynamics of
droplet interaction with incident shock wave is in accordance with the previous work
on shock–water-column interaction (Igra & Takayama 2003; Sembian et al. 2016)a n d
various two-dimensional numerical simulations using spherical dispersions (Mehta et al.
2016; Sridharan et al. 2016; Guan et al. 2018; Das & Udaykumar 2020), indicating
the axisymmetric nature of the stage I interaction. The continuous deformation of the
droplet increases the projected area for aerodynamic drag, which further enhances the
ﬂattening of the liquid droplet ( ﬁgures 4 o and 5g) and leads to droplet breakup in later
time instants. Figure 6 represents the various droplet breakup morphologies observed
during its interaction with a shock wave of different strengths.
Panels (a,b) correspond
to the bigger droplet size (Di ∼ 2.5m m) and panels (c,d) correspond to smaller droplet
size (Di ∼ 0.5m m ). The left-hand side images correspond to the low Weber number
while the right-hand side corresponds to the high Weber number. Figure 6 essentially
explains that two types of breakup modes (i.e. SIE and RTP) are observed based on
Weber number and droplet sizes, and the interaction becomes more vigorous as the
Weber number increases. The details of these mechanisms are provided in following
subsections.
3.2. Global observation of shock–droplet interaction mechanism
Figure 7 shows the global observation of the shock–droplet interaction mechanism. The
complete interaction dynamics can be divided into two stages : initial shock interaction
(stage I) and droplet breakup dynamics (stage II). As discussed earlier, the initial shock
interaction corresponds to the formation of different wave structures and a local change
of ambient conditions around the droplet. These changes result in droplet deformation;
but the droplet retains its coherent structure during the interaction stage I. The droplet
deformation begins due to high-pressure regions at the front and rear stagnation points
(due to external airﬂow near the front stagnation point, recirculating ﬂow and shock
929 A27-12
https://doi.org/10.1017/jfm.2021.860
 Published online by Cambridge University Press

<!-- PDF_PAGE: 13 -->

Shock induced aerobreakup of a droplet
2 mm 2 mm 2 mm 2 mm
0.5 mm 0.5 mm 0.5 mm 0.5 mm
(a)( b)
(c)( d)
Figure 6. Droplet breakup morphologies for different shock Mach numbers and droplet sizes. ( a) The SIE
droplet breakup at Ms = 1.12, We = 219, Re = 1.3 ∗104, Di = 2.5. (b) The SIE droplet breakup at Ms = 1.3,
We = 1.6 ∗103, Re = 4 ∗104, Di = 2.9. (c) The RTP droplet breakup at Ms = 1.12, We = 44, Re = 2.5 ∗103,
Di = 0.5. (d) The RTP droplet breakup at Ms = 1.45, We = 795, Re = 1.2 ∗104, Di = 0.5.
focusing near the rear stagnation point), which overcomes the restoring surface tension
and viscous forces acting on the droplet. A low-pressure region is formed near the equator
of the droplet where the external ﬂow velocity is comparatively higher, as in the case of
external airﬂow over a cylinder/sphere of similar Reynolds number. T wo high-pressure
regions at the droplet’s front and rear stagnation points and a low-pressure region near
the equator direct the internal ﬂow of liquid towards the droplet equator, resulting in
the deformation of the spherical droplet into a cupcake shape. This pressure difference
is further enhanced due to an increase in aerodynamic drag with deforming droplet
shape. The
shock–droplet interaction mechanism is universal up to this point for all
cases of shock–droplet interaction. Beyond this (stage II interaction), depending on the
relative dominance of pressure force or the shear force acting on the droplet surface, two
modes of droplet breakup, i.e. RTP breakup ( ﬁgure 7 b)o r SIE ( ﬁgure 7 c) breakup are
observed.
The RTP-based droplet breakup is characterised by complete deformation of the droplet
into a ﬂattened disc followed by the formation of single/multiple bags, which grow over
time due to incoming airﬂow and undergoes rupture. The bag rupture is followed by
the breakup of the central undeformed region and outer toroidal rim joining the bags
(Jackiw & Ashgriz 2021). The shear-induced droplet breakup mode is characterised by the
formation of
KH-based surface waves (Theofanouset al. 2012; Guan et al. 2018; Dorschner
et al. 2020) on the windward surface of the droplet. These waves undergo elongation
and rupture, or the formed waves travel along the windward surface and merge to form
a liquid sheet near the equator of the droplet. The external aerodynamic forces acting on
the formed sheet lead to stretching in the cross-stream direction followed by rupture into
ﬁne mist ( ﬁgure 7 c). A detailed discussion on each droplet breakup mode is provided in
the following subsections.
929 A27-13
https://doi.org/10.1017/jfm.2021.860
 Published online by Cambridge University Press

<!-- PDF_PAGE: 14 -->

S. Sharma, A.P . Singh, S.S. Rao, A. Kumar and S. Basu
Droplet Incident shock
Stage I: initial shock interaction
(a)
(b)( c)
Stage II: droplet breakup dynamics
4 mm
1 mm 3 mm
Mode 1: Rayleigh–Taylor piercing Mode 2: shear-induced breakup
Ms = 1.16 We = 458 Re = 1.9 × 104
Ms = 1.16 We = 94 Re = 2.9 × 103 Ms = 1.16 We = 458 Re = 1.9 × 104
t∗ = 0 t∗ = 0.04 t∗ = 0.08
t∗ = 0 t∗ = 0.4 t∗ = 1.2 t∗ = 1.8 t∗ = 2.0 t∗ = 2.1 t∗ = 0 t∗ = 0.21 t∗ = 0.43 t∗ = 0.71 t∗ = 1.35
Reflected shock
Figure 7. Global observation of shock–droplet interaction. ( a) Stage I corresponding to the initial shock
interaction; ( b) breakup dynamics (stage II) of a droplet ( Di ∼ 0.5 mm) undergoing breakup through RTP
mode; and (c) SIE mode of droplet breakup for Di ∼ 2.5 mm.
3.3. Shear-induced droplet breakup
The initial stages of shock–droplet interaction involving wave dynamics and droplet
deformation were discussed in § 3.1. The present subsection strides towards understanding
the breakup dynamics of a droplet through the SIE mode. Figure 8 (also supplementary
movie 2) shows the time sequence images (from left to right) of the breakup dynamics of
a ∼ 2.9 mm diameter droplet for different values of shock Mach numbers. As discussed
earlier, the initial wave interaction and droplet deformation stages are similar for all
experimental cases. The deformed droplet attains a cupcake shape, after which it
undergoes a stripping type of droplet breakup. The stripping of daughter droplets near
the equator of the primary droplet is triggered by the formation of
KH waves (Theofanous
et al. 2012;L i u et al. 2018) near the front stagnation point of the droplet (see ﬁgure 8 ,
third column). These waves are formed midway between the front stagnation point
and droplet equator, along the droplet periphery, which is the region of highest shear
(Liu et al. 2018). The validation of formed surface waves with theoretical predictions
is shown later. For a better understanding of the breakup dynamics, a high-resolution
(8 μmp i x e l− 1) and high-speed (at 50 000 f.p.s.) imaging of interaction phenomena was
done in a pendant drop mode (see ﬁgure 9 ). This conﬁguration will affect the breakup
dynamics at the rear stagnation point ; however, no distinguishable difference between
pendant mode and free-falling conﬁguration could be identiﬁed at the windward side of the
droplet (see supplementary movie 3). This methodology for obtaining high-resolution and
high-speed imaging was also recently employed by Jackiw & Ashgriz (2021). Figure 9(a,b)
corresponds to the shock Mach number of 1.12 and 1.47, respectively. Once formed,
KH waves
grow in amplitude ( ﬁgure 9 at ∗ = 0.37–0.4a n d ﬁgure 9 bt ∗ = 0.1–0.29)
and subsequently get deﬂected towards the ﬂow direction ( ﬁgure 9 at ∗ = 0.47 and
929 A27-14
https://doi.org/10.1017/jfm.2021.860
 Published online by Cambridge University Press

<!-- PDF_PAGE: 15 -->

Shock induced aerobreakup of a droplet
t∗ = 0 t∗ = 0.49 t∗ = 0.86 t∗ = 1.42 t∗ = 4.29 t∗ = 7.19 t∗ = 8.64 t∗ = 10.59
t∗ = 0
3 mm
t∗ = 0.32 t∗ = 0.40 t∗ = 0.45 t∗ = 0.57 t∗ = 0.85 t∗ = 1.13 t∗ = 1.42
t∗ = 0 t∗ = 0.26 t∗ = 0.39 t∗ = 0.46 t∗ = 0.65 t∗ = 1.18 t∗ = 1.84 t∗ = 2.50
t∗ = 0 t∗ = 0.08 t∗ = 0.25 t∗ = 0.34 t∗ = 0.50 t∗ = 1.01 t∗ = 1.68 t∗ = 2.36
t∗ = 0 t∗ = 0.13 t∗ = 0.25 t∗ = 0.38 t∗ = 0.52 t∗ = 1.03 t∗ = 1.55 t∗ = 2.06
t∗ = 0 t∗ = 0–0.17 t∗ = 0.17 t∗ = 0.35 t∗ = 0.71 t∗ = 1.41 t∗ = 2.12 t∗ = 2.83
Ms = 1.17
We = 513
Re = 2.2 × 104
Ms = 1.27
We = 1.3 × 103
Re = 3.4 × 104
Ms = 1.35
We = 2.2 × 103
Re = 4.5 × 104
Ms = 1.47
We = 4.1 × 103
Re = 6.5 × 104
Ms = 1.64
We = 7.9 × 103
Re = 9.5 × 104
Ms = 1.83
We = 1.4 × 104
Re = 1.3 × 105
(e)
( f )
(b)
(a)
(c)
(d )
Figure 8. Droplet breakup dynamics at different Weber numbers for a droplet diameter ( Di)o f ∼ 2.9 mm.
Time sequence images of droplet breakup from the instant of wire explosion to droplet breakup (from left
to right). ( a–f ) The magnitude of non-dimensional numbers ( M
s, We, Re) increases from (a)t o ( f ). See
supplementary movie ﬁle 2 for evolution dynamics of cases in (a,c and e).
ﬁgure 9bt∗ = 0.38) when entrained by the external air ﬂow (see ﬁgure 8, fourth column).
The ﬂow entrainment causes the surface waves to move towards the downstream direction
along the windward surface and after reaching the ﬂow separation point (at the droplet
equator) the liquid carried with these waves gets accumulated as a thin sheet at this location
(ﬁgure 9 at ∗ = 0.47 and ﬁgure 9 bt ∗ = 0.38). The thin sheet undergoes rupture due to
nucleation of multiple holes (shown later through top-view imaging) which expands in
size in a temporal fashion leading to sheet rupture into numerous cylindrical ligaments
(ﬁgure 9 at ∗ = 0.52 and ﬁgure 9 bt ∗ = 0.48). The formed cylindrical ligaments further
undergo secondary atomisation into smaller droplets through Rayleigh–Plateau modes of
instability.
In addition to the accumulation of droplet ﬂuid near the equator due to KH waves
(leading to sheet formation), the effect droplet deformation, which causes an internal ﬂow
directed towards the equator region (discussed in § 3.1) also augments the sheet formation
at the equator (see ﬁgure 4m–o). Here, the ﬂuid transport towards the equator through the
droplet deformation is greater than micron-sized KH waves. Therefore, the sheet formation
with the predominant KH wave mechanism will be thinner than the droplet deformation
mechanism. Subsequently, the droplet sizes stripping from the rupture of the sheet will also
be smaller for the
KH-waves-based liquid accumulation mechanism. Therefore, during the
929 A27-15
https://doi.org/10.1017/jfm.2021.860
 Published online by Cambridge University Press

<!-- PDF_PAGE: 16 -->

S. Sharma, A.P . Singh, S.S. Rao, A. Kumar and S. Basu
t∗ = 0(a)
(b)
t∗ = 0.37 t∗ = 0.40 t∗ = 0.43
t∗ = 0.47 t∗ = 0.52 t∗ = 0.57 t∗ = 0.65
t∗ = 0 t∗ = 0.10 t∗ = 0.19 t∗ = 0.29
t∗ = 0.38 t∗ = 0.48 t∗ = 0.58 t∗ = 0.77
1.5 mm
Figure 9. Zoomed-in view of shear-stripping breakup. ( a) Time-sequence images of droplet breakup at Ms =
1.12 and Di = 2.02 mm; and ( b) time-sequence images of droplet breakup at Ms = 1.47 and Di = 2.24 mm.
For details see supplementary movie ﬁle 3.
early stages of droplet breakup (see ﬁgure 8, fourth and ﬁfth columns), the extent of droplet
deformation is less, and KH waves are the only dominant mechanism for sheet formation
leading to a ﬁne mist of daughter droplets.
Figures 8 and 9 and theoretical analysis shown later (§ 3.4) shows that the number of KH
waves formed on the droplet surface increases with increase in Weber number. Moreover,
the local incubation location of KH waves shifts towards the front stagnation point as the
Weber number increases (see ﬁgure 9). The formed surface waves grow in amplitude and
move towards the equator of the droplet, where they get accumulated at the stripping sheet
and compensate for the liquid mass loss due to sheet rupture. The thin sheet formed due to
KH waves experiences two driving forces leading to its motion: ﬁrst, the entrainment force
due to the shear acting on its surface by external airﬂow; and second, additional pull due to
the induced internal motion by the movement of KH wave formed ahead of it (towards the
equator). Therefore, the translational velocity of the wave formed near the front stagnation
point is higher than the one formed near the equator. This results in merging of two
surface waves as they translate towards the droplet equator, resulting in
an increase of
combined wave sheet thickness. The merging of surface waves can be seen in ﬁgure 9(b)
(t∗ = 0.19–0.48) and is shown more clearly in next subsection. The merged KH waves
on reaching the droplet equator result in the formation of a thicker sheet; thereby the size
of fragmenting daughter droplet increases (see ﬁgure 8 , ﬁfth column). The thickness of
the stripping sheet is further augmented by the deformation of the primary droplet, which
again increases the size of fragmenting droplets. Therefore, the size of daughter droplets
monotonically increases from the beginning of breakup to the end during the SIE breakup
929 A27-16
https://doi.org/10.1017/jfm.2021.860
 Published online by Cambridge University Press

<!-- PDF_PAGE: 17 -->

Shock induced aerobreakup of a droplet
regime (see ﬁgure 8). The breakup mechanism involving sheet formation at droplet equator
due to the combined effect of accumulation of KH waves and droplet deformation occurs
recurrently (discussed later) until the complete droplet disintegrates into daughter droplets
or aerodynamic forces acting on the remaining sheet of the deformed droplet are unable
to overcome the surface tension of the sheet. The stretched sheet in the latter case retracts
back to form a single droplet.
More surface waves are formed at the higher Weber numbers ( ﬁgure 8 ). This implies
that the amount of liquid transported through these waves will also be higher. In addition
to this, the extent of droplet deformation also decreases with increasing Weber number.
Therefore, higher wavenumbers and lower droplet deformations result in the domination
of KH-waves-based liquid transport mechanism at the stripping sheet, which therefore
explains the formation of smaller droplet sizes with increasing shock Mach number (see
ﬁgures 8 and 9). In contrast to this, at lower Mach numbers, the number of KH waves
formed are lower, and the extent of droplet deformation is higher; therefore, the formed
droplet sizes are bigger in such cases. The above explanation of SIE breakup based on the
competing effect of KH waves and droplet-deformation-based liquid transmission towards
the stripping sheet has been reported for the ﬁrst time in this work. This explains both the
temporal increase in the size of daughter droplets and reduction in daughter droplet sizes
with increasing Weber number, observed during SIE-based breakup.
In addition to the surface waves formed at the windward surface of the droplet, a
ﬂattened disc and a lip are also formed on the leeward side of the droplet due to the
internal ﬂow induced inside the droplet by shock focusing and jet ﬂow impinging on the
rear stagnation point of the droplet (discussed in § 3.1). The formed lip interacts with
the secondary vortices formed after external ﬂow stabilisation around droplet ( ﬁgure 4n).
These formed vortices stretch and engulf the droplet lip sheet towards their core, as
explained by Sharma, Singh & Basu ( 2021), leading to its rupture. This mechanism also
contributes to mist formation during
SIE-based droplet breakup; however, it lasts for a
short time interval and has an insigniﬁcant contribution in the total number of daughter
droplet
formations (ﬁgure 8).
3.4. Kelvin–Helmholtz-based surface instabilities
The previous subsection discusses the droplet breakup mechanism based on KH surface
waves. Here, we present the theoretical analysis used to predict the wavelength of the
formed surface waves. Existing models of KH instabilities based on zero and non-zero
vorticity thickness (Marmottant & Villermaux 2004; Jalaal & Mehravaran 2014)a r eu s e d
for the comparison of theoretical and experimental results. Figure 10 (also supplementary
movie ﬁle 4) shows a zoomed-in view of the droplet windward surface which display the
time sequence images of KH waves formation for Weber number values of We = 2095
(ﬁgure 10a)a n d We = 91 667 (ﬁgure 10b), respectively. As can be seen from ﬁgure 10,
instability waves are formed much before the droplet response time (i.e. the beginning of
droplet deformation). As discussed earlier, after formation, these waves move towards the
droplet equator and sometimes
merge to form a combined wave, thereby increasing the
thickness of the liquid sheet carried along with them. Figure 10 shows at t∗ = 0.13–0.19
and t∗ = 0.46–0.52, some KH-wave-induced liquid sheets are unable to sustain further
elongation and undergo rupture before accumulating at the droplet equator. This is an
additional mechanism responsible for mist formation during SIE-based droplet breakup.
Considering an inviscid and incompressible airﬂow on the droplet surface, no gravity
effects and negligible vorticity layer thickness (seeﬁgure 10c), one can apply the ﬁrst-order
929 A27-17
https://doi.org/10.1017/jfm.2021.860
 Published online by Cambridge University Press

<!-- PDF_PAGE: 18 -->

S. Sharma, A.P . Singh, S.S. Rao, A. Kumar and S. Basu
Ms = 1.33
We = 2.0 × 103
Re = 5.1 × 104
Ms = 1.60
We = 7.5 × 103
Re = 9.2 × 104
t∗ = 0 t∗ = 0.27 t∗ = 0.38
λ
t∗ = 0.52
0.5 mm
t∗ = 0.55 t∗ = 0.58
t∗ = 0.46
Vi, ρa
δa
δl
Vl
Droplet
Vi
Vl
ρl
t∗ = 0.52 t∗ = 0.59
Air
Stagnation point
Wake
Shock front
(a)
(b)
(c)( d)
Laminar
separation
Air
x
y
Liquid
t∗ = 0.41 t∗ = 0.44 t∗ = 0.48
t∗ = 0 t∗ = 0.13 t∗ = 0.19 t∗ = 0.26 t∗ = 0.33 t∗ = 0.39
Figure 10. Kelvin– Helmholtz instability near front stagnation point of droplet for Di ∼ 2.5 mm. Time
sequence images of KH waves formation is shown for ( a) Ms ∼ 1.16 and (b) Ms ∼ 1.45 from left to right. For
details see supplementary movie ﬁle 4. Panels (c)a n d( d) show the schematic diagram for zero and non-zero
vorticity thickness models for KH waves, respectively.
linear perturbation analysis to obtain the following dispersion equation (Marmottant &
Villermaux 2004) for the instability growth rate (ωKH):
ωKH = kKH
ρlVl + ρaVi
ρl + ρa
± i kKH
ρa + ρl
√
ρlρa(Vi − Vl)2 − (ρa + ρl)σkKH. (3.1)
Here, kKH is the wavenumber of the instability, Vl is the velocity of the droplet ﬂuid and
subscript KH refers to KH-based instability. In (3.1), surface tension will stabilise all shear
instabilities above critical wavenumber (kKHc), where
kKHc > ρaρl
ρa + ρl
(Vi − Vl)2
σ . (3.2)
929 A27-18
https://doi.org/10.1017/jfm.2021.860
 Published online by Cambridge University Press

<!-- PDF_PAGE: 19 -->

Shock induced aerobreakup of a droplet
Now, considering Vi ≫ Vl and ρl ≫ ρa, which is a valid assumption in our case, one
can obtain the wavenumber (kKHmax ) corresponding to maximum growth rate ( ωKHmax ) as
kKHmax = 2
3
ρlVi2
σ = 2
3
We
Di
, (3.3a)
λKH = 2π
kKHmax
= 3π
WeDi. (3.3b)
Figure 11 shows the comparison of experimental and theoretical prediction of KH-wave
wavelength corresponding to maximum growth rate with different Weber numbers.
As predicted by ( 3.3a), the wavelength of maximum growth rate decreases with an
increase in Weber number. Although the zero-vorticity thickness model predicts the
correct trend of experimental data
, the absolute values were found to be O(10–100) less
than the experimental observation (see table 1 , third column). Similar under-prediction
of wavelength while using the assumption of zero-vorticity layer thickness was also
reported by other researchers (Marmottant & Villermaux 2004;K i m et al. 2006; Jalaal &
Mehravaran 2014). The impractical assumption of zero vorticity layer thickness between
the external airﬂow and internal liquid ﬂow led to this under-prediction of the theoretical
model. Therefore, a modiﬁed model with a ﬁnite thickness of vorticity layer and linear
variation of velocity proﬁle (see ﬁgure 10d) based on the work of Lord Rayleigh ( 1879)
for two different phases in the vorticity layer
were obtained by Villermaux ( 1998) as
λKH = 2π
0.8 F
( ρl
ρa
)
δa, (3.4)
where, δa is the boundary layer thickness of air phase (see ﬁgure 10d)a n d
F
( ρl
ρa
)
= 5
6 − 1
6(ρl/ρa) +
√
5 + 13(ρl/ρa) − 37(ρl/ρa)2 + 27(ρl/ρa)3
6
√
2(ρl/ρa)
. (3.5)
The value of δa for the present work is obtained using boundary layer analysis, where
δa ∼ Lc√
ReLc
= C1
Lc√
ReLc
. (3.6)
Here, Lc is the characteristic length scale, which in the present case is the initial drop
radius (Ri)a n dC1 is constant replacing scaling analysis and its value is chosen as a ﬁtting
parameter for ﬁgure 11 . For the limiting case of (ρl/ρa) ≫ 1,( 3.4) can be written as
(Villermaux 1998)
λKH = 2π
1.5
√ ρl
ρa
δa, (3.7)
and the corresponding dispersion equation is obtained as (Marmottant & Villermaux 2004)
e− 2κ = [1 −{ 2Ω ∗ + κ}] 1 + 0.5(ρl/ρa + 1)(2Ω ∗ − κ)
1 + 0.5(ρl/ρa − 1)(2Ω ∗ − κ). (3.8)
Here, κ = kKHδa and Ω ∗ = ωKHδa/(Vi − Vl) − 2κ((Vi + Vl)/(Vi − Vl)). The ratio of
predicted and experimental wavelength based on ( 3.7)a n d( 3.4) is referred as ‘ non-zero
thickness ratio 1’ and ‘ non-zero thickness ratio 2’ in table 1 and ﬁgure 11. The decreasing
trend of KH wavelength ( λKH ) is well predicted by two models and in comparison with
929 A27-19
https://doi.org/10.1017/jfm.2021.860
 Published online by Cambridge University Press

<!-- PDF_PAGE: 20 -->

S. Sharma, A.P . Singh, S.S. Rao, A. Kumar and S. Basu
300 Experimental
Zero vorticity thickness
Jalal & Mehravaran
Kim et al.250
200
150
Wavelength (λKH)
100
50
0
0 2500 5000
Weber number (We)
7500 10 000 12 500
Figure 11. Wavelength variation of KH waves with shock Mach number ( Ms) for droplet size ( Di)o f
∼ 2.5 mm.
Ms Wavelength(λKH) (μm)
Zero thickness
ratio
Non-zero thickness
ratio 1
Non-zero thickness
ratio 2
1.26 222 .14± 36.6 0.10 1.10 1.33
1.33 145 .18± 20.0 0.09 1.53 1.85
1.45 98 .94 ± 12.3 0.07 1.78 2.17
1.60 72 .35 ± 10.9 0.05 1.94 2.37
1.79 61 .93 ± 12.6 0.03 1.70 2.08
Table 1. Kelvin–Helmholtz instability comparison with theoretical models.
zero thickness model the predicted results based on non-zero vorticity thickness are of
same order of magnitude of experimental data. The observed discrepancy in the absolute
value of wavelength was also reported by Marmottant & Villermaux ( 2004), Kim et al.
(2006) and Jalaal & Mehravaran ( 2014), and is attributed to the linear velocity proﬁle
assumption and error in estimating C1 in ( 3.6). Based on the experimental observations
of the present work, no signiﬁcant trend of KH wavelength variation along the droplet
periphery could be identiﬁed, as the measured wavelengths were found to be distributed
randomly. Qualitatively KH waves are generally formed at an azimuthal location midway
between the front stagnation point and droplet equator (i.e. region of highest shear Liuet al.
2018). The region near the front stagnation point remains smooth/unaffected. However ,a s
the Weber number increases, the starting location of KH instabilities shift towards the
front stagnation point, as can be seen from ﬁgure 9.
3.5. Top-view visualisation and recurrent breakup of liquid sheet
The high-speed shock–droplet interaction is essentially a three-dimensional phenomenon,
which necessitates top-view imaging to acquire relatively more information. The
time-sequence images showing the top view of droplet breakup dynamics is shown
in ﬁgures 12 (a)a n d 12(b) for Weber numbers values of 474 and 4133, respectively.
929 A27-20
https://doi.org/10.1017/jfm.2021.860
 Published online by Cambridge University Press

<!-- PDF_PAGE: 21 -->

Shock induced aerobreakup of a droplet
t∗ = 0 t∗ = 0.29 t∗ = 0.48 t∗ = 0.58 t∗ = 0.73 t∗ = 1.02 t∗ = 1.36 t∗ = 1.80 t∗ = 2.82
t∗ = 0(a)
(b)
t∗ = 0.50
3 mm
t∗ = 0.65 t∗ = 0.84 t∗ = 1.03 t∗ = 1.19 t∗ = 1.31 t∗ = 1.59 t∗ = 1.97
Ms = 1.16 We = 4.7 × 102 Re = 1.9 × 104
Ms = 1.45 We = 4.1 × 103 Re = 6.5 × 104
3m m
Figure 12. Time sequence images showing the top view of shock–droplet interaction for droplet size ( Di)o f
∼ 2.5m ma t( a) Ms ∼ 1.3a n d(b) Ms ∼ 1.46.
As discussed earlier, the breakup dynamics are similar for both cases. However, the
fragmentation of the primary droplet is more intense at a higher Weber number, leading to
much ﬁner daughter droplet sizes after the breakup. The ligaments at the droplet periphery
are formed periodically along the azimuthal direction during the ﬁrst breakup ( ﬁgure 12a
at t∗ = 0.65 and ﬁgure 12b at t∗ = 0.48). The periodic formation of fragmenting ligaments
can be attributed to azimuthal modulation of the RT waves on the existing KH waves
formed due to shear effects. In continuation of the work of Villermaux ( 1998) and
Marmottant & Villermaux ( 2004) involving instability analysis of a liquid jet exposed
to a coaxial airﬂow, Jalaal & Mehravaran ( 2014) carried a similar analysis on a droplet
exposed to external uniform ﬂow and explained RTI-based azimuthal modulations on
axisymmetric KH waves (formed due to shear) due to the acceleration of KH waves
towards the droplet equator. The modulation of RT waves on the KH waves is shown
in ﬁgure 13.H e r eﬁgure 13(a) shows the cross-sectional location on which RT waves are
shown in ﬁgure 13(b). The crest of RT waves get entrained to external airﬂow and
result in
ligament formation. The measurement of the RT wavelength was performed by measuring
the distance between the stripping ligaments (as shown in ﬁgure 13c). An assumption is
made that the formed RT waves stretch to form ligaments whose breakup can be seen
through
top-view imaging, as shown in the third column image of ﬁgures 12(a)a n d12(b).
The measurements are provided for a possible estimation in terms of order of magnitude
basis. The exact values of RT wavelength could not be identiﬁed based on these images as
randomness arises in the measurements due to
the uncertain manner of ligament breakup
under the inﬂuence of induced airﬂow. Therefore, values provided in table 2 must only
be used for order-of-magnitude comparison. Similarly, no trend in the variation of these
wavelengths could be explained with a change in shock Mach numbers using table 2.
A comparison of the experimentally observed RT-waves wavelength is made with an
existing model based on Marmottant & Villermaux ( 2004) analysis as
λRT ∼= 2.8δaWeδa
− 1/3
(ρa
ρl
)− 1/3
. (3.9)
929 A27-21
https://doi.org/10.1017/jfm.2021.860
 Published online by Cambridge University Press

<!-- PDF_PAGE: 22 -->

S. Sharma, A.P . Singh, S.S. Rao, A. Kumar and S. Basu
KH waves
on droplet
surface
(a)( b)( c)
RT waves modulated
over KH waves
Increasing direction of We Top view
λKH
λRT λRT
Figure 13. Azimuthal modulation of RT waves on KH waves. ( a) Kelvin–Helmholtz waves formed near the
front stagnation point of the droplet. Dashed lines show the cross-section of the KH wave on which RT waves
are displayed .( b) Schematic diagram showing RT waves formed on droplet surface and their wavelength
variation (λT ) with Weber number (We).( c) Experimental image showing RT waves leading to droplet stripping
during initial stages of droplet breakup.
Ms
Experimental
wavelength (λTexp )
(mm)
Theoretical
wavelength (λTmodel )
(mm) λTexp /λTmodel
1.12 0 .52 ± 0.20 1.86 3.57
1.16 0 .42 ± 0.15 1.15 2.75
1.30 0 .57 ± 0.23 0.59 1.02
1.45 0 .49 ± 0.16 0.32 0.66
Table 2. Rayleigh–Taylor modulation over KH waves. A comparison of experimental and theoretical
wavelengths.
Here, Weδa is a Weber number based on the vorticity layer thickness. The comparison
of the theoretical prediction with experimental data is shown in table 2 . Although the
predicted results correlate with experimental data with the same order of magnitude,
the absolute magnitudes of predicted wavelengths differ considerably (up to three
times). The observed discrepancy could be due to the linear velocity proﬁle assumption
between the vorticity thickness layer and constant C1, as discussed earlier, and similar
discrepancies were also obtained in the numerical simulations of Jalaal & Mehravaran
(2014). The RT waves measurements were only done for the ﬁrst instance of droplet
breakup, corresponding to the KH waves formed nearest to the droplet equator. This
limitation was due to merging KH waves and additional ligaments formation due to sheet
rupture during later breakup instances.
Jarrahbashi & Sirignano ( 2014) had studied through vorticity
dynamics the instability
mechanisms in round liquid jets. The azimuthal instability on the axisymmetric KH
waves can arise through the baroclinic effect (RTI, as shown above and in Marmottant
& Villermaux ( 2004)) and/or by streamwise vortex generation due to vortex tilting and
stretching
mechanisms (as in isodensity jets (Liepmann & Gharib 1992)) leading to lobe
formation. The baroclinic effects are dominant during atmospheric gas pressures (i.e. at
low gas–liquid density ratios), where the gas–liquid density ratio is O(10− 3).I ns u c h
cases, RT instability is a dominant mode for lobe generation due to the high-density
gradient across the interface (related to baroclinic vorticity). Also, the contribution from
the vortex tilting and stretching mechanism is negligible because of lower gas inertia,
thereby lower vortex strain near the liquid interface. However, at higher gas-density ratios,
929 A27-22
https://doi.org/10.1017/jfm.2021.860
 Published online by Cambridge University Press

<!-- PDF_PAGE: 23 -->

Shock induced aerobreakup of a droplet
vortex–strain interactions are substantial and the contribution of the baroclinic effect
decreases in streamwise vorticity generation. Therefore, stretching and tilting of vortices is
a dominant mechanism in azimuthal modulation on KH waves for such cases (Jarrahbashi
et al. 2016). A similar observation was also obtained for
a liquid sheet exposed to external
airﬂows (Zandian, Sirignano & Hussain 2017, 2019a,b). For the shock Mach number cases
considered in the present work, the gas–liquid density ratio is O(10− 3), and therefore
the baroclinic effect (or RTI) mode of lobe generation will be predominant, as discussed
earlier.
Further, formed lobes undergo a cascade process through three different mechanisms
during ligaments/droplet formation. The involved mechanisms include : (i) lobe stretching
leading to ligament formation ; (ii) corrugation on the lobes leading to multiple ligament
formations during stretching of corrugation ; and (iii) perforation of holes on the lobe
leading to bridge breakup and ligament formation (Zandian et al. 2017, 2019b). The mode
of ligament formation was shown to be dependent on the modiﬁed Ohnesorge number
(Ohm = √(Weg)/Rel) and Reynolds number ( Rel) magnitude (Zandian et al. 2017). In
the present work, we have refrained from determining the exact mechanism of ligament
formation as the time sequence evolution of ligament formation was beyond the spatial
and temporal resolutions. The ligament formation is also obstructed during the top-view
imaging. However, future experimental or numerical works are motivated to uncover the
prevalent mechanism of ligament formation during lobe disintegration. The elongation of
the lobes leading to ligament formation was shown to be a predominant mechanism during
low
gas–liquid density ratio by Jarrahbashi & Sirignano ( 2014). Therefore, the same can
be assumed to be prevalent in the present case while determining the wavelength of RT
waves.
The phenomenon of SIE breakup of a droplet is recurrent, as shown in ﬁgure 14 and
explained schematically using ﬁgure 14( f ). Each breakup cycle involves the formation of
a thin sheet at the droplet periphery. The elongation of the sheet due to its entrainment into
the external airﬂow further decreases the sheet thickness, making it susceptible to surface
instabilities. Any small perturbation on this sheet can result in the nucleation of holes on
its surface (see ﬁgure 14a). After formation, these holes expand in all directions, leading
to the sheet’s rupture into cylindrical ligaments. The formed ligament further undergoes
a secondary atomisation into a daughter droplet through RPI and, thus, completes one
breakup cycle. The second cycles begin with the formation of the thin sheet due to the
accumulation of liquid at the droplet periphery due to the combined effect of KH waves
translation and droplet deformation (as explained earlier) and follow a similar breakup
pattern as discussed above. The three cycles of
SIE-based recurrent breakup of the droplet
are shown in ﬁgure 14. A similar recurrent breakup of the liquid droplet was also shown
by Dorschner et al. (2020) through numerical simulations.
3.6. A shift in droplet breakup dynamics during transition regime (100 < We < 1000)
Previously, the droplet breakup dynamics of low viscosity Newtonian ﬂuids ( Oh <
0.1) were subdivided into ﬁve major regimes (i.e. vibrational breakup ( We < 11), bag
breakup (11 < We < 35), multimode breakup (35 < We < 80), sheet thinning breakup
(80 < We < 350) and catastrophic breakup ( We > 350)) based on Weber number range
(Guildenbecher et al. 2009). These regimes were reclassiﬁed by Theofanous & Li ( 2008)
based on hydrodynamics instabilities, where previously identiﬁed bag and multibag
breakup modes were included in the RTP regime (based on RTI), while sheet thinning
and catastrophic regimes correspond to the SIE mechanism (based on KHI). The RTP
929 A27-23
https://doi.org/10.1017/jfm.2021.860
 Published online by Cambridge University Press

<!-- PDF_PAGE: 24 -->

S. Sharma, A.P . Singh, S.S. Rao, A. Kumar and S. Basu
Holes nucleating at rim
First breakup Second breakup
Initial
droplet
Deformed
droplet
Undeformed
region
Hole nucleation
(first cycle)
Hole nucleation
(second cycle)Ligaments from RT
waves
Hole growth
(first cycle)
Ligament
breakup
Second breakup Third breakup Third breakup
(e)(b)(a)( c)( d )
( f )
Figure 14. Recurrent breakup of the liquid sheet :( a) ﬁrst breakup ;( b,c) second breakup ;a n d( c–e)t h i r d
breakup. The red and blue rectangular regions shows the time-sequence evolution of holes during second and
third breakup
, respectively. All images are of same scale. ( f ) Schematic diagram showing recurrent breakup of
a droplet.
regime ranges up to We < 100, the SIE regime corresponds to We > 1000, and a transition
regime exists between these two regimes (100 < We < 1000). This reclassiﬁcation is also
validated in our experiments for RTP ( ﬁgure 18 a,b)a n dS I E( ﬁgure 8 b–f ) regime. In
the transition regime, through ﬁgure 15 (also see supplementary movie ﬁles 5 and 6)
we explain the dependence of the breakup mode on the size of the primary droplet. In
the existing literature, a unidirectional breakup trend from bag breakup to catastrophic
breakup is reported with increasing Weber number. The sheet thinning or catastrophic
breakup are the only two breakup modes observed for We > 80. Here, using the ratio of
initial drop diameter to the wavelength of KH wave, we explain the existence ofmultimode
droplet breakup for Weber number values up to ∼ 795. Figure 15 (a,b) shows the shear
stripping mechanism, while ﬁgure 15 (c, d)s h o w st h emultimode droplet breakup at a
comparatively higher Weber numbers ( We ∼ 347 795) values predicted from the previous
studies (We < 80). The important features in the evolution of multibag and shear stripping
mode of droplet breakup are shown schematically in ﬁgure 15 (e). The shear stripping
breakup was discussed in detail in § 3.3 and multibag breakup will be discussed later in this
section. The growth rate of KH waves and RT waves on a droplet surface can be obtained
from (3.8)a n d( 3.10), respectively. The results of instability growth rate from dispersion
relation based on KH wave (3.8) and RT wave (discussed later) are plotted in ﬁgure 16 for
two particular cases of low and high Weber numbers. It is clearly observed that the growth
rate of KH waves is always higher than the RT waves of corresponding Weber number,
indicating that the RT waves (which lead to
a bag-type breakup mechanism) based droplet
breakup can only occur during the inability of KH wave formation (Theofanous et al.
2012). Thus, ﬁnding the criterion for this transition becomes important.
Figure 17 shows the ratio of droplet diameter with the predicted wavelength of KH wave
b a s e do n(3.7). Green markers indicate the droplet sizes undergoing SIE-based breakup
mode, while the red markers correspond to the RTP-based droplet breakup mechanism.
It can be seen from ﬁgure 16 that KH waves are only formed if Di ≫ λKH (at least by
an order difference) while the RTP-based droplet breakup mode occurs when both Di
929 A27-24
https://doi.org/10.1017/jfm.2021.860
 Published online by Cambridge University Press

<!-- PDF_PAGE: 25 -->

Shock induced aerobreakup of a droplet
t∗ = 0
3 mm
3 mm
t∗ = 0.29 t∗ = 0.38 t∗ = 0.92 t∗ = 2.04
Ms = 1.12 We = 205 Re = 1.2 × 104
t∗ = 0 t∗ = 0.55 t∗ = 1.39 t∗ = 1.95 t∗ = 2.22 t∗ = 2.50
Ms = 1.30 We = 347 Re = 8 × 103
t∗ = 0 t∗ = 0.31 t∗ = 0.42 t∗ = 0.56 t∗ = 1.22
Ms = 1.16 We = 424 Re = 1.7× 104
t∗ = 0 t∗ = 0.95 t∗ = 1.90 t∗ = 2.37 t∗ = 2.85 t∗ = 3.32
Ms = 1.45 We = 795 Re = 1.2 × 104
Shock droplet
interaction
Initial
deformation
Stripping
initiation
Equator points
Deformation
Droplet
Shock wave
Shock
interaction
Initial
deformation
Flattening
Thin region for bag
nucleation
KHI waves
Sheet formation
near equator
Sheet breakupLip
Peripheral
rim
Central
stamen
BagsCentral undeformed
region
Multibag formation
Rayleigh–Taylor piercing
Shear-induced breakup
Surface waves Stripping
Leeward
Windward
Intense
stripping
Droplet
breakup
1 mm
1 mm
Shock droplet
interaction
Initial
deformation
Droplet
flattening
Bag
formation
Multi-bag
breakup
(c)(a)
(b)
(e)
(d)
Di ∼ 2.5 mm Di ∼ 0.5 mm
Figure 15. A shift of droplet breakup mechanism from SIE to RTP with different droplet sizes and similar
Weber numbers ( We). ( a,b) Time sequence images showing SIE mode of droplet breakup for Di ∼ 2.5 mm.
(c,d) Time sequence images showing RTP mode of droplet breakup for Di ∼ 0.5 mm. For details see
supplementary movie ﬁles 5 and 6. ( e) Schematic diagram showing droplet breakup through RTP and SIE
modes.
and λKH are of a similar order of magnitude. When Di ∼ λKH the size of the fastest
growing wavelength is similar or less than the size of the available area required for its
formation, i.e. droplet windward surface length, which is of the order of the droplet radius.
Therefore, KH waves cannot be formed under such cases (as predicted in ﬁgure 17), which
gives way to the formation of much slower RT waves on the windward surface of the
droplet after its complete deformation into a ﬂattened disc. This explains the observation of
multimode droplet breakup at Weber number values of ∼ 347 and ∼ 795. Thus, the present
article indicates the importance of the Di/λKH ratio in addition to the Weber number for
predicting the breakup mode of the droplet.
Figure 18 shows the RTP-based droplet breakup mechanism (also see supplementary
movie ﬁle 7). In these cases, the primary droplet undergoes complete deformation (unlike
SIE) into a ﬂattened disc. The formed disc becomes unstable due to the acceleration of
low density induced airﬂow on its surface, resulting in RTI. The growth rate ( ωRT )o fR T
929 A27-25
https://doi.org/10.1017/jfm.2021.860
 Published online by Cambridge University Press

<!-- PDF_PAGE: 26 -->

S. Sharma, A.P . Singh, S.S. Rao, A. Kumar and S. Basu
80 000
60 000
40 000
Growth rate (ω )
20 000
0 10 000 20 000
Wavenumber (k)
30 000 40 000
KH, We = 1320, Di = 2.9 mm
RT, We = 1320, Di = 2.9 mm
KH, We = 45, Di = 0.5 mm
RT, We = 45, Di = 0.5 mm
Figure 16. Rayleigh–Taylor andKH instabilities growth rate ( ω) versus wavenumber (k).
50
40
30
20
Di/λKH
10
100 1000
We
10 000
Di ∼ 2.5 mm
Di ∼ 1.0 mm
Di ∼ 3.0 mm
Di ∼ 0.5 mm
Di ∼ 2.5 mm
Di ∼ 1.0 mm
Figure 17. Transition of droplet breakup mode based on Di/λKH and We. Red markers indicates breakup
thorough RTP mode while green markers correspond to the SIE mode. The orange region corresponds to RTP
(We < 100), the green region corresponds to SIE ( We > 1000) and the blue region corresponds to transition
regime (100 < We < 1000).
instability can be expressed as (Drazin & Reid 2004; Zhao et al. 2018)
ωRT 2 = kRT [(ρl − ρa)a − kRT 2σ]
ρl + ρa
. (3.10)
Here, kRT is the wavenumber of RT waves, a is the acceleration of the droplet, which is
deﬁned as
a = Fa
md
= 3ρaV2
i CdD2
m
4D3
i ρl
. (3.11)
929 A27-26
https://doi.org/10.1017/jfm.2021.860
 Published online by Cambridge University Press

<!-- PDF_PAGE: 27 -->

Shock induced aerobreakup of a droplet
t∗ = 0
1 mm
t∗ = 1.46 t∗ = 2.92 t∗ = 3.25 t∗ = 3.59 t∗ = 3.70
Ms = 1.12 We = 44 Re = 2.5 × 103
t∗ = 0 t∗ = 0.55 t∗ = 1.39 t∗ = 1.95 t∗ = 2.22 t∗ = 2.50
Ms = 1.30 We = 347 Re = 8 × 103
t∗ = 0
Shock droplet
interaction
Initial
deformation
Droplet
flattening
Bag
formation Multibag breakup Shock droplet
interaction
Initial
deformation
Droplet
flattening
Bag
formation Multibag breakup
t∗ = 0.45 t∗ = 1.22 t∗ = 1.83 t∗ = 1.98 t∗ = 2.14
Ms = 1.16 We = 90 Re = 4.0 × 103
t∗ = 0 t∗ = 0.95 t∗ = 1.90 t∗ = 2.75 t∗ = 2.85 t∗ = 3.32
Ms = 1.45 We = 795 Re = 1.2 × 104
(c)(a)
(b)( d)
Figure 18. Droplet breakup dynamics at different Weber numbers for a droplet of diameter (Di) ∼ 0.4 mm.
Time sequence images of droplet breakup from the instant of wire explosion to droplet breakup (from left to
right). ( a–d) The magnitude of non-dimensional numbers ( M
s, We, Re) increases from panels (a)t o( d). For
details see supplementary movie ﬁle 7.
2.0
1.8
1.6
1.4
1.2
Aspect ratio (x∗/y∗)
1.0
0 0.1 0.2 0.3
Initial Deformed
0.4 0.5 0.6
t∗
6
5
4
3
2
1
0 0.5 1.0 1.5 2.0 2.5 3.0
t∗
We = 3915
We = 1615
We = 498
We = 219
Do ∼ 2.5 mm
We = 805
We = 332
We = 102
We = 45
Do ∼ 0.5 mm
x∗
y∗
x∗
y∗
(b)
(a)
(c)
Figure 19. Aspect ratio variation with time :( a) schematic diagram;a n d(b,c) aspect ratio variation with time
for droplet size of ∼ 2.5 mm and ∼ 0.5 mm, respectively.
Here, Cd is the drag coefﬁcient whose value is chosen as ∼ 1.2 (Zhao et al. 2018) and
Dm is the maximum droplet diameter during ﬂattened state before the bag formation. The
variation of RT instability growth rate for different wavenumber is shown in ﬁgure 16. The
wavelength corresponding to the maximum growth rate ( λRT ) is obtained as (Drazin &
Reid 2004;J a i net al. 2015)
λRT = 2π
√
3σ
ρla. (3.12)
929 A27-27
https://doi.org/10.1017/jfm.2021.860
 Published online by Cambridge University Press

<!-- PDF_PAGE: 28 -->

S. Sharma, A.P . Singh, S.S. Rao, A. Kumar and S. Basu
4.0
3.5
3.0
2.5
2.0
1.5
1.0
0.5
0
100 1000
We
10 000
Induction time
Breakup end
Breakup start
t∗
Figure 20. Regime map for shock–droplet interaction. Orange region corresponds to RTP (We < 100), green
region corresponds to SIE (We > 1000) and blue region corresponds to transition regime (100 < We < 1000).
Snapshot images corresponds to breakup stage at particular time instant and Weber number.
The wavelength of formed instability determines the number of bags formed during
the droplet breakup process. The mode of droplet breakup is classiﬁed by normalising
the initial droplet diameter with RT wavelength ( N = Di/λRT ) (Zhao et al. 2010). In
the present work, N ∼ 2–3 for all considered cases (see supplementary table 1) which
undergoes breakup through RTI. Therefore , only the multibag mode of droplet breakup
is obtained (see ﬁgure 18) (Zhao et al. 2010;J a i net al. 2015). Several bags are formed
during the multibag mode of droplet breakup on the ﬂattened droplet between the central
undeformed and peripheral rims. The formed bag grows in size along the streamwise
direction, reducing the sheet thickness, making it vulnerable to rupture into secondary
daughter droplets. This is then followed by the rupture of the peripheral rim, which
disintegrates into larger droplet sizes compared
with those formed by bag breakup. The
central region of the deformed droplet takes the form of a stamen-shaped ligament, which
is attached to the formed bag. After bag rupture, the stamen ligament either
contracts back
to form a single droplet (at low Weber numbers) or further undergoes atomisation in a
manner similar to the primary droplet, depending on the external aerodynamic forces.
The usage of
a wide range of Weber numbers ( We ∼ 30–15 000) in the present study
essentially resulted in the observation of both RTP and SIE modes of droplet breakup
and identifying the possible transition mechanism between two modes. Subsequently,
the present experimental study illustrates the aspect ratio variation for different Weber
numbers and droplet sizes of 2.5 mm and 0.5 mm (see ﬁgure 19). The results are shown
up to the beginning of droplets stripping for
the SIE breakup mode and the beginning
of bag formation during the RTP mode. As can be seen from the ﬁgure, the extent of
deformation for smaller droplet size (RTP breakup mode) is greater than the bigger droplet
(SIE breakup). This data could be useful during the validation of future numerical models.
4. Conclusions
The multiscale nature of shock–droplet interaction dynamics was studied through inline
shadowgraphy/schlieren imaging and top view shadowgraphy imaging. A pulsed laser
929 A27-28
https://doi.org/10.1017/jfm.2021.860
 Published online by Cambridge University Press

<!-- PDF_PAGE: 29 -->

Shock induced aerobreakup of a droplet
with nanosecond-order pulse width was used, which effectively freezes the high-speed
phenomena occurring during shock–droplet interaction. The experiments were carried out
for a shock Mach number range of 1 .1–1.8, droplet sizes of ∼ 0.5, 2.5, 2.9 mm, resulting
in a wide range of Weber numbers (∼ 30–15 000) and Reynolds numbers (∼ 3000–110 000).
The usage of high-quality and precise experimental data in this work makes the present
results an ideal benchmark for future numerical studies. The complete regime map of the
droplet morphology at different time instants and Weber numbers is shown in ﬁgure 20.
The interaction dynamics was bifurcated into two stages: initial wave dynamics (stage I)
and droplet breakup dynamics (stage II). Stage I includes the formation of different wave
structures involving reﬂected waves, transmitted waves and refracted waves. The evolution
dynamics of each wave structure was explained along with the local changes imposed
by them on the droplet surface. The formation of high-pressure regions near the front
stagnation point due to ﬂow stagnation and at the rear stagnation point due to Mach
wave focusing and recirculating jet ﬂow results in the deformation of the droplet into
a
cupcake shape, which marks the end of the stage I interaction. Stage I was observed to be
self-similar for all experimental cases considered in this work, irrespective of shock Mach
number.
Stage II of the interaction dynamics corresponds to the droplet breakup. T wo modes
of droplet breakup, i.e. SIE breakup (based on KHI) and RTP breakup (based on RTI),
were observed. The SIE mode is triggered by the formation of KH waves on the windward
surface of the droplet. The formed waves grow in size as they translate after formation
and
merge at the equator, forming a thin sheet that undergoes rupture and results in
daughter droplets/mist generation. The mechanism of daughter droplet formation based on
the relative dominance of droplet deformation and KH wave formation in liquid transport
was used to explain the monotonic increase in droplet size with time. The same argument
was also used for explaining the decrease in the daughter droplet sizes with an increase
in Weber number. The
top view of interaction dynamics shows the periodic distribution
of formed liquid ligament during the initial breakup stage, which was explained using
the transverse modulation of RT waves on the surface of KH waves. The comparison of
theoretical prediction of observed KH waves and transverse modulated waves shows a
qualitatively good agreement. However, quantitatively, the predicted results match only in
orders of magnitude, and possible means for this discrepancy were also discussed. The
droplet breakup through the SIE mechanism was found to be recurrent. The formed sheet
near the droplet equator undergoes holes nucleation at several locations, and the growth of
formed holes leads to
the rupture of the sheet into daughter droplet/mist in later instances.
This cycle of sheet formation and rupture into daughter droplets continues until complete
disintegration of the droplet or if the external aerodynamic forces cannot assistuntil further
breakup.
The RTP-based droplet breakup is characterised by the complete deformation of
the primary droplet into a ﬂattened disc. The windward surface of the formed disc
experiences an acceleration of low density induced airﬂow, making it susceptible to
RT-based instability waves. A comparison of the theoretical model based on RTI predicts
a multibag type of droplet breakup for all considered RTP cases, which matches well with
the experiments. The result shows a KH wave growth rate dominance over RT waves,
indicating KH waves as a primary mechanism for droplet breakup.
The RT waves can
only form when KH wave formation is unfavourable. Therefore, a criterion for breakup
mode transition from KHI to RTP was obtained based on the ratio of droplet diameter to
the wavelength of the KH wave. It was shown that
KH-based SIE exist only if Di ≫ λKH
and transition to RTP occurs when Di ∼ λKH . The experimental results clearly reveal the
929 A27-29
https://doi.org/10.1017/jfm.2021.860
 Published online by Cambridge University Press

<!-- PDF_PAGE: 30 -->

S. Sharma, A.P . Singh, S.S. Rao, A. Kumar and S. Basu
plausible variation in surface ﬂow features. Characterisation of a wide range of Weber
numbers unearths the essential criteria for convenient atomisation of the liquid droplets.
Supplementary material and movies. Supplementary material and movies are available at https://doi.org/
10.1017/jfm.2021.860.
Acknowledgements. The authors gratefully acknowledge Professor C. Tropea (TU Darmstadt, Germany),
Professor S. Chakraborty (IIT KGP, India), Professor I. Roisman (TU Darmstadt, Germany), SMS group
(Germany), Tata steel (India) and IGSTC PPAM group for their insights and discussions during the
development of the present work.
Funding. The support of research by IGSTC (Indo–German Science and Technology Center) through project
no. SP/IGSTC-18-0003 is thankfully acknowledged.
Declaration of interest. The authors report no conﬂict of interest.
Author ORCIDs.
Shubham Sharma https://orcid.org/0000-0002-8704-887X ;
Awanish Pratap Singh https://orcid.org/0000-0003-1374-8176;
S. Srinivas Rao https://orcid.org/0000-0003-1817-5207;
Aloke Kumar https://orcid.org/0000-0002-7797-8336 ;
Saptarshi Basu https://orcid.org/0000-0002-9652-9966 .
REFERENCES
ANDERSON , J.D. 2003 Modern Compressible Flow: With Historical Perspective, 7th edn. McGraw-Hill.
BAYVEL , L.P . 1 993Liquid Atomization, vol. 1040. CRC.
BEN -DOR , G. 2007 Shock Wave Reﬂection Phenomena.S p r i n g e r .
BERESH ,S . , et al. 2015 Pulse-burst PIV in a high-speed wind tunnel. Meas. Sci. Technol. 26 (9), 095305.
BIASIORI -POULANGES ,L .&E L-RABII , H. 2019 High-magniﬁcation shadowgraphy for the study of drop
breakup in a high-speed gas ﬂow. Opt. Lett. 44 (23), 5884–5887.
CAO, X.-K., S UN , Z.-G., L I,W . - F . ,LIU,H . - F .&Y U, Z.-H. 2007 A new breakup regime of liquid drops
identiﬁed in a continuous and uniform air jet ﬂow. Phys. Fluids 19 (5), 057103.
CHANG , C.-H., D ENG ,X .&T HEOFANOUS , T.G. 2013 Direct numerical simulation of interfacial
instabilities: a consistent, conservative, all-speed, sharp-interface method. J. Comput. Phys. 242, 946–990.
CHEN , H. 2008 T wo-dimensional simulation of stripping breakup of a water droplet. AIAA J. 46 (5),
1135–1143.
CHOU ,W . - H . ,H SIANG , L.-P . & F AETH , G.M. 1997 Temporal properties of drop breakup in the shear
breakup regime. Intl J. Multiphase Flow 23 (4), 651–669.
DAS ,P .&U DAYKUMAR , H.S. 2020 A sharp-interface method for the simulation of shock-induced
vaporization of droplets. J. Comput. Phys. 405, 109005.
DORSCHNER ,B . ,B IASIORI -POULANGES , L., S CHMIDMAYER ,K . ,E L-RABII ,H .&C OLONIUS , T. 2020
On the formation and recurrent shedding of ligaments in droplet aerobreakup. J. Fluid Mech. 904, A20.
DRAZIN ,P . G .&R EID , W.H. 2004 Hydrodynamic Stability, 2nd edn. Cambridge University Press.
EGGERS ,J .&V ILLERMAUX , E. 2008 Physics of liquid jets. Rep. Prog. Phys. 71 (3), 036601.
FEDOTOV -GEFEN ,A . ,E FIMOV,S . ,G ILBURD , L., G LEIZER ,S . ,B AZALITSKY ,G . ,G UROVICH ,V . T .&
KRASIK , Y.E. 2010 Extreme water state produced by underwater wire-array electrical explosion. Appl.
Phys. Lett. 96 (22), 221502.
GUAN ,B . ,L IU,Y . ,W EN ,C . - Y .&S HEN , H. 2018 Numerical study on liquid droplet internal ﬂow under
shock impact. AIAA J. 56 (9), 3382–3387.
GUILDENBECHER , D.R., L ÓPEZ -RIVERA ,C .&S OJKA , P.E. 2009 Secondary atomization. Exp. Fluids 46,
371–402.
HAN ,J .&T RYGGVASON , G. 2001 Secondary breakup of axisymmetric liquid drops. II. Impulsive
acceleration. Phys. Fluids 13 (6), 1554–1565.
HA VERMANN ,M . ,H AERTIG ,J . ,R EY,C .&G EORGE , A. 2008 PIV measurements in shock tunnels and
shock tubes. Top. Appl. Phys. 112, 429–443.
HENDERSON , L.F. 1989 On the refraction of shock waves. J. Fluid Mech. 198, 365–386.
HINZE , J.O. 1955 Fundamentals of the hydrodynamic mechanism of splitting in dispersion processes. AIChE J.
1 (3), 289–295.
929 A27-30
https://doi.org/10.1017/jfm.2021.860
 Published online by Cambridge University Press

<!-- PDF_PAGE: 31 -->

Shock induced aerobreakup of a droplet
HSIANG , L.-P . & F AETH , G.M. 1992 Near-limit drop deformation and secondary breakup. Intl J. Multiphase
Flow 18 (5), 635–652.
IGRA ,D .&T AKAYAMA , K. 2003 Experimental investigation of two cylindrical water columns subjected to
planar shock wave loading. Trans. ASME J. Fluids Engng 125, 325–331.
JACKIW ,I . M .&A SHGRIZ , N. 2021 On aerodynamic droplet breakup. J. Fluid Mech. 913, A33.
JAIN ,M . ,P RAKASH , R.S., T OMAR ,G .&R AV I K R I S H N A, R.V. 2015 Secondary breakup of a drop at
moderate Weber numbers. Proc. R. Soc. A: Math. Phys. Engng Sci. 471 (2177), 20140930.
JALAAL ,M .&M EHRA V ARAN, K. 2014 Transient growth of droplet instabilities in a stream. Phys. Fluids 26
(1), 012101.
JARRAHBASHI ,D .&S IRIGNANO , W.A. 2014 Vorticity dynamics for transient high-pressure liquid injection.
Phys. Fluids 26 (10), 101304.
JARRAHBASHI ,D . ,S IRIGNANO , W .A., P OPOV,P . P .&H USSAIN , F. 2016 Early spray development at high
gas density: hole, ligament and bridge formations. J. Fluid Mech. 792, 186–231.
JOSEPH , D.D., B ELANGER ,J .&B EA VERS, G.S. 1999 Breakup of a liquid drop suddenly exposed to a
high-speed airstream. Intl J. Multiphase Flow 25 (6–7), 1263–1303.
KESHA V ARZ,B . ,H OUZE , E.C., M OORE , J.R., K OERNER ,M . R .&M CKINLEY , G.H. 2016 Ligament
mediated fragmentation of viscoelastic liquids. Phys. Rev. Lett. 117 (15), 154502.
KIM ,D . ,D ESJARDINS ,O . ,H ERRMANN ,M .&M OIN , P. 2006 Toward two-phase simulation of the primary
breakup of a round liquid jet by a coaxial ﬂow of gas. In Center for Turbulence Research, Annual Research
Briefs, pp. 185–195. Stanford University.
KRZECZKOWSKI , S.A. 1980 Measurement of liquid droplet disintegration mechanisms. Intl J. Multiphase
Flow 6 (3), 227–239.
LEFEBVRE ,A . H .&M CDONELL ,V . G .2 0 1 7Atomization and Sprays.C R C .
LIANG ,Y . ,J IANG ,Y . ,W EN ,C . - Y .&L IU, Y. 2020 Interaction of a planar shock wave and a water droplet
embedded with a vapour cavity. J. Fluid Mech. 885,R 6 .
LIEPMANN ,D .&G HARIB , M. 1992 The role of streamwise vorticity in the near-ﬁeld entrainment of round
jets. J. Fluid Mech. 245, 643–668.
LIU,N . ,W ANG , Z., S UN ,M . ,W ANG ,H .&W ANG , B. 2018 Numerical simulation of liquid droplet breakup
in supersonic ﬂows. Acta Astron. 145, 116–130.
LIVERTS ,M . ,R AM ,O . ,S ADOT ,O . ,A PAZIDIS ,N .&B EN -DOR , G. 2015 Mitigation of
exploding-wire-generated blast-waves by aqueous foam. Phys. Fluids 27 (7), 076103.
MARMOTTANT ,P .&V ILLERMAUX , E. 2004 On spray formation. J. Fluid Mech. 498, 73–111.
MEHTA ,Y . ,J ACKSON , T.L., Z HANG ,J .&B ALACHANDAR , S. 2016 Numerical investigation of shock
interaction with one-dimensional transverse array of particles in air. J. Appl. Phys. 119 (10), 104901.
MEHTA ,Y . ,N EAL ,C . ,S ALARI ,K . ,J ACKSON , T.L., B ALACHANDAR ,S .&T HAKUR , S. 2018 Propagation
of a strong shock over a random bed of spherical particles. J. Fluid Mech. 839, 157–197.
MENG ,J . C .&C OLONIUS , T. 2015 Numerical simulations of the early stages of high-speed droplet breakup.
Shock Waves 25 (4), 399–414.
NICHOLLS ,J . A .&R ANGER , A.A. 1969 Aerodynamic shattering of liquid drops. AIAA J. 7 (2), 285–290.
PILCH ,M .&E RDMAN , C.A. 1987 Use of breakup time data and velocity history data to predict the maximum
size of stable fragments for acceleration-induced breakup of a liquid drop. Intl J. Multiphase Flow 13 (6),
741–757.
POPLA VSKI , S.V ., M INAKOV , A.V ., S HEBELEV A ,A . A .&B OYKO , V.M. 2020 On the interaction of water
droplet with a shock wave: experiment and numerical simulation. Intl J. Multiphase Flow 127, 103273.
RAYLEIGH ,L ORD 1879 On the stability, or instability, of certain ﬂuid motions. Proc. Lond. Math. Soc.
s1–11 (1), 57–72.
SEMBIAN ,S . ,L IVERTS ,M . ,T ILLMARK ,N .&A PAZIDIS , N. 2016 Plane shock wave interaction with a
cylindrical water column. Phys. Fluids 28 (5), 056102.
SHARMA ,S . ,S INGH ,A . P .&B ASU , S. 2021 On the dynamics of vortex–droplet co-axial interaction: insights
into droplet and vortex dynamics. J. Fluid Mech. 918, 1–36.
SHINJO ,J .&U MEMURA , A. 2011 Surface instability and primary atomization characteristics of straight liquid
jet sprays. Intl J. Multiphase Flow 37 (10), 1294–1304.
SRIDHARAN ,P . ,J ACKSON , T.L., Z HANG ,J .&B ALACHANDAR , S. 2015 Shock interaction with
one-dimensional array of particles in air. J. Appl. Phys. 117 (7), 075902.
SRIDHARAN ,P . ,J ACKSON , T.L., Z HANG ,J . ,B ALACHANDAR ,S .&T HAKUR , S. 2016 Shock interaction
with deformable particles using a constrained interface reinitialization scheme. J. Appl. Phys. 119 (6),
064904.
SUN ,M . ,S AITO ,T . ,T AKAYAMA ,K .&T ANNO , H. 2005 Unsteady drag on a sphere by shock wave loading.
Shock Waves 14 (1), 3–9.
929 A27-31
https://doi.org/10.1017/jfm.2021.860
 Published online by Cambridge University Press

<!-- PDF_PAGE: 32 -->

S. Sharma, A.P . Singh, S.S. Rao, A. Kumar and S. Basu
TANNO ,H . ,I TOH ,K . ,S AITO ,T . ,A BE ,A .&T AKAYAMA , K. 2003 Interaction of a shock with a sphere
suspended in a vertical shock tube. Shock Waves 13, 191–200.
THEOFANOUS , T.G. 2011 Aerobreakup of newtonian and viscoelastic liquids. Annu. Rev. Fluid Mech. 43 (1),
661–690.
THEOFANOUS ,T . G .&L I, G.J. 2008 On the physics of aerobreakup. Phys. Fluids 20 (5), 052103.
THEOFANOUS , T.G., M ITKIN , V .V ., NG, C.L., C HANG ,C - H . ,D ENG ,X .&S USHCHIKH ,S .2 0 1 2T h e
physics of aerobreakup. II. Viscous liquids. Phys. Fluids 24 (2), 022104.
VILLERMAUX , E. 1998 Mixing and spray formation in coaxial jets. J. Propul. Power 14 (5), 807–817.
WANG , Z., H OPFES ,T . ,G IGLMAIER ,M .&A DAMS , N.A. 2020 Effect of mach number on droplet
aerobreakup in shear stripping regime. Exp. Fluids 61, 193.
YANG ,H .&P ENG , J. 2019 Numerical study of the shear-thinning effect on the interaction between a normal
shock wave and a cylindrical liquid column. Phys. Fluids 31 (4), 043101.
ZANDIAN ,A . ,S IRIGNANO ,W . A .&H USSAIN , F. 2017 Planar liquid jet: early deformation and atomization
cascades. Phys. Fluids 29 (6), 062109.
ZANDIAN ,A . ,S IRIGNANO ,W . A .&H USSAIN ,F .2 0 1 9a Length-scale cascade and spread rate of atomizing
planar liquid jets. Intl J. Multiphase Flow 113, 117–141.
ZANDIAN ,A . ,S IRIGNANO ,W . A .&H USSAIN ,F .2 0 1 9b Vorticity dynamics in a spatially developing liquid
jet inside a co-ﬂowing gas. J. Fluid Mech. 877, 429–470.
ZHAO ,H . ,L IU,H . - F . ,LI,W . - F .&X U, J.-L. 2010 Morphological classiﬁcation of low viscosity drop bag
breakup in a continuous air jet stream. Phys. Fluids 22 (11), 114103.
ZHAO ,H . ,L IU,H . - F . ,XU, J.-L., L I,W . - F .&C HENG , W. 2012 Breakup and atomization of a round coal
water slurry jet by an annular air jet. Chem. Engng Sci. 78, 63–74.
ZHAO ,H . ,L IU,H . - F . ,X U, J.-L., L I,W . - F .&L IN , K.-F. 2013 Temporal properties of secondary drop
breakup in the bag-stamen breakup regime. Phys. Fluids 25 (5), 054102.
ZHAO ,H . ,W U, Z.-W ., L I,W . - F . ,X U, J.-L. & L IU, H.-F. 2018 Transition weber number between
surfactant-laden drop bag breakup and shear breakup of secondary atomization. Fuel 221, 138–143.
929 A27-32
https://doi.org/10.1017/jfm.2021.860
 Published online by Cambridge University Press
