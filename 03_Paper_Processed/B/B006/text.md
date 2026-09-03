<!-- PDF_PAGE: 1 -->

400 Commonwealth Drive, Warrendale, PA 15096-0001 U.S.A.   Tel: (724) 776-4841  Fax: (724) 776-5760   Web: www.sae.org
SAE TECHNICAL
PAPER SERIES 2006-01-0652
Transient High-Pressure
Hydrogen Jet Measurements
B.R. Petersen and J.B. Ghandhi
Engine Research Center, University of Wisconsin-Madison
Reprinted From:  Hydrogen IC Engines
(SP-2009)
2006 SAE World Congress
Detroit, Michigan
April 3-6, 2006
Downloaded from SAE International by Dalian Univ of Technology, Monday, August 31, 2026

<!-- PDF_PAGE: 2 -->

The Engineering Meetings Board has approved this paper for publication.  It has successfully completed 
SAE's peer review process under the supervision of the session organizer.  This process requires a 
minimum of three (3) reviews by industry experts.
All rights reserved.  No part of this publication may be reproduced, stored in a retrieval system, or 
transmitted, in any form or by any means, electronic, mechanical, photocopying, recording, or otherwise, 
without the prior written permission of SAE.
For permission and licensing requests contact:
SAE Permissions
400 Commonwealth Drive
Warrendale, PA 15096-0001-USA
Email: permissions@sae.org
Tel: 724-772-4028
Fax: 724-776-3036
For multiple print copies contact:
SAE Customer Service
Tel: 877-606-7323 (inside USA and Canada)
Tel: 724-776-4970 (outside USA)
Fax: 724-776-0790
Email: CustomerService@sae.org 
ISSN 0148-7191
Copyright © 2006 SAE International
Positions and opinions advanced in this paper are those of the author(s) and not necessarily those of SAE.  
The author is solely responsible for the content of the paper.  A process is available by which discussions 
will be printed with the paper if it is published in SAE Transactions.
Persons wishing to submit papers to be considered for presentation or publication by SAE should send the 
manuscript or a 300 word abstract to Secretary, Engineering Meetings Board, SAE.
Printed in USA
Downloaded from SAE International by Dalian Univ of Technology, Monday, August 31, 2026

<!-- PDF_PAGE: 3 -->

2006-01-0652
Transient High-Pressure Hydrogen Jet Measurements  
B.R. Petersen and J.B. Ghandhi
Engine Research Center, University of Wisconsin-Madison 
ABSTRACT
Schlieren visualization was performed to investigate 
hydrogen injection into a quiescent chamber.  The 
injection pressures investigated were 52 and 104 bar, 
and the chamber density ranged from 1.15 to 12.8 
kg/m
3, giving rise to underexpanded jets for all 
conditions.  The expansion waves outside the nozzle 
were clearly visible with hydrogen, and the effect was 
confirmed with studies of nitrogen injected into a 
nitrogen environment.  The distance between the 
expansion wave fronts was found to scale directly with 
the ratio of the exit pressure to the chamber pressure.  
The jet tip penetration rate was measured and was 
found to increase with injection pressure, and decrease 
with chamber density as expected.  A mass- and 
momentum-preserving scheme was developed to relate 
the underexpanded jet to a subsonic jet of larger 
diameter.  The jets were found to exhibit self-similar 
behavior in the far field when the appropriate 
characteristic length and time scales were used for the 
nondimensionalization.
INTRODUCTION
Because emissions from motor vehicles have a 
significant impact on the environment and the overall 
health of society, and fossil fuel supplies are limited, 
alternative renewable fuels that combust cleaner are 
being investigated.  Hydrogen is an attractive alternative 
fuel because its combustion with oxygen is relatively 
clean, the flame speed is high and it has wide 
flammability limits.  Further, hydrogen produced from 
renewable sources can, in principle, eliminate all carbon-
related emissions. But the use of hydrogen to fuel an 
internal combustion engine has some pitfalls, most 
notably a strong tendency to knock and backfire [1].
The limitations associated with port-injected premixed 
hydrogen engines have prompted the investigation of 
direct in-cylinder injection of hydrogen [2,3].  Direct 
injection eliminates the possibility of backfire, reduces 
the propensity for autoignition, and provides a higher 
energy density within the combustion chamber because 
the air charging efficiency is higher.  However, with 
direct injection, NO
x emissions and the quality of 
combustion depend greatly on the mixing that occurs 
between the injected hydrogen and the air within the 
cylinder.  In order to promote proper mixing and to 
supply sufficient amounts of hydrogen to the cylinder, 
high-pressure gaseous injectors are being developed.  
The performance of these injectors is critical to the 
overall performance of the hydrogen engine. 
High-pressure gaseous injectors used in engine 
applications are typically multi-hole plain-orifice injectors 
that create multiple turbulent jets.  The jets are often 
underexpanded upon the exit of the injector nozzle. Hill 
and Ouellette [4] reviewed the self-similar characteristics 
of transient turbulent jets and developed an analytical 
relationship for the penetration.  They employed the 
Turner model [5] to approximate the geometry of a gas 
jet as a spherical head vortex and a quasi-steady jet 
region that feeds the head with momentum.  The jet is 
constantly supplied with momentum through the orifice, 
and the momentum is, in turn, passed between the 
quasi-steady jet and the head vortex.  The entrainment 
of the low momentum ambient fluid was assumed to 
follow the relationship reported by Ricou and Spalding 
[6]
U
U
§·  ¨¸
©¹
12
0
ch
s
n
mx xKKmd d  (1) 
where m is the entrained mass,  m0 is the jet fluid mass, 
d is the orifice diameter, x is distance from the orifice, Uch
and Un are the chamber and nozzle density, and the 
entrainment coefficient K = 0.32 [6]. The jet penetration 
was assumed, based on dimensional grounds, to follow 
the form 
Copyright © 2006 SAE International
Downloaded from SAE International by Dalian Univ of Technology, Monday, August 31, 2026

<!-- PDF_PAGE: 4 -->

U
§· * ¨¸
©¹

14 12
t
ch
MZt  (2) 
where Zt is the tip penetration distance and Mis the 
momentum flow rate supplied by the orifice.  The scaling 
constant * was found to be a function of Ks and s, the 
ratio of the head vortex diameter, D, to the penetration, 
Zt through 

 SS
ªº * *   «» «»¬¼
2
42
33
1 24 022
s
sK ssss
(3)
The value for s was taken as 0.25 ± 0.05 from data of 
Rizk [7].   
Hill and Ouellette [4] investigated jets with downstream 
(beyond the near-nozzle region where a Mach disc can 
form and expansion waves are present) density ratios 
(injection to ambient) of approximately 1.0, which 
corresponds to K
s ~ 0.32. For this Ks value, * was found 
from eq. (3) to be 3.0.  The jet data shown by Hill and 
Ouellette [4] were also found to agree with this value.  
The scaling of eq. (2) was also applied to 
underexpanded methane jet data acquired by Miyake et
al. [8], Chepakovich [9], and Hill and Ouellette [4].  The 
scaling constant 
* was found to remain approximately 
3.0 even with the rapid expansion and the presence of a 
Mach disc at the exit of the orifice. For the 
underexpanded cases the exit momentum flow was 
reduced by 10 percent from choked conditions to 
accommodate for the frictional effects inside the nozzle.
Abraham [10] derived an expression for a transient gas 
jet by integrating the centerline velocity of a steady 
turbulent jet.  The steady centerline velocity relationship 
used was that of Schlichting [11]; 
S
 12
3
16
ei
CL
t
dUU
Cx
 (4) 
where de is the effective diameter U
U{ n
e
ch
dd , Ui is 
the injection velocity and Ct is a parameter that relates 
the turbulent diffusivity to the kinematic momentum flux.  
By defining the tip position as the location where the 
velocity is a fraction, C
f, of the steady centerline velocity, 
the following expression for the location of the tip of the 
jet as a function of time was developed 
S
§·§·  ¨¸¨¸ §·©¹ ©¹ ¨¸©¹
2
12
3
8
t f
ee t
i
Z C t
dd C
U
. (5) 
The entrainment constant, K, of eq. (2) can be related to 
the constant Ct by
S 
1216 tKC  (6) 
Many values have been proposed for the constants Ct
and K [10] for the fully developed region, and the value 
varies from 0.26 to 0.142 and, therefore, is only known 
within a factor of 2. 
The expression for jet tip penetration reported by 
Abraham [10] is equivalent to the relation developed by 
Hill and Ouellette [4] where *can be expressed as 
123
4
f
t
C
CS
§·* ¨¸
©¹
. (7) 
A *value of 3.0 and a Ct of 0.0113, which corresponds 
to a K value of 0.32, results in a Cf  value of 0.142. The
other reported entrainment values result in * varying
between 3.6 and 2.11 for the same value of Cf.
The objective of this paper is to investigate transient, 
underexpanded hydrogen jets in a constant volume 
chamber. The structure of the jet and the overall 
penetration are investigated using a schlieren system 
combined with a high-speed digital camera to image the 
injection event both normal to and along the injector 
axis.  The images allowed for a clear representation of 
the jet pattern, including underexpanded jet features 
such as the Mach disc and expansion waves.
EXPERIMENTAL APPARATUS 
Z-TYPE SCHLIEREN SYSTEM 
The Z-type schlieren system used to visualize the 
gaseous jets is shown in Fig 1 a).  An f/1.4 condenser 
lens imaged the light source onto a 1 mm pinhole to 
create a well defined source.  Light from the pinhole was 
collimated by a 1140 mm focal length f/10.5 parabolic 
mirror before passing through the test section.  A 
matching parabolic mirror then produced an image of the 
source onto an adjustable knife edge, which was 
oriented so as to enhance the contrast of the jet leading 
edge.
Downloaded from SAE International by Dalian Univ of Technology, Monday, August 31, 2026

<!-- PDF_PAGE: 5 -->

The hydrogen jets caused the parallel light to bend by an 
angle, İ, given by [12] 
H w w0
Ln
ny  (8) 
where n0 is the refractive index of the surrounding 
medium, L is the extent of the object to be imaged, and 
wn/wy is the gradient in the index of refraction. The index 
of refraction gradient was a result of both the difference 
of index between the injected and chamber gases and 
density nonuniformities in the field.  The knife edge 
blocks a portion of the original light source and light that 
was deflected inside the test chamber.   A Phantom v7.1 
high-speed camera was used to capture the images 
downstream of the knife edge.  Images were acquired at 
4800 and 10000 frames per second.
An important measure of a schlieren system is its 
contrast sensitivity [12], which describes the rate of 
change of image contrast with respect to refraction angle 
and is given by S:
H  2fdCS da  (9) 
where f2 is the focal length of the mirror or lens following 
the test section and a is the length of the source image 
that is not blocked by the knife edge.  A large value of 
contrast sensitivity allows small refractive index 
gradients to be seen in an image.  The large focal length 
mirrors, 1143 mm, and a small-unblocked length of 
approximately 1 mm, resulted in a contrast sensitivity of 
1143 for the system shown.  This was found to be a 
sufficient value for detecting the density gradients 
between the injected hydrogen and the chamber gases.
Utilizing parabolic mirrors in an off-axis manner can 
result in coma and astigmatism, which causes the light 
to not be properly focused to a point by the parabolic 
mirrors.  The astigmatism is worse at large off-axis 
angles. To reduce the effects, the angles used in this 
system were kept small. Further, by bending the system 
in a “z” shape at equal and opposite angles, coma was 
eliminated all together. 
DOUBLE PASS SCHLIEREN SYSTEM 
A double pass schlieren system was used to image the 
jet patterns “end-on”, or directly towards the tip of the 
injector. The injector was mounted horizontally in the 
back wall of the test chamber through a circular mirror 
with a hole to accommodate the injector tip.  This mirror 
reflected the parallel light back through the test section, 
out the initial window and back towards the parabolic 
mirror.  This system is shown in Fig. 1 b).
a)
Parabolic
Mirror
Knife edge
1 mm 
aperture
Condensing Lens      
TestSection
Parabolic
Mirror
Light 
Source
-
High speed 
camera
Parabolic
Mirror
Parabolic
Mirror
Knife edge
1 mm 
aperture
Condensing Lens      
TestSection
Parabolic
Mirror
Parabolic
Mirror
Light 
Source
-
High speed 
camera
High speed 
camera
b)
Parabolic
Mirror
Knife edge
1 mm 
aperture
TestSection
Mirrored 
Surface
Light
Source
High speed 
camera
Flat Mirror
Injector
Parabolic
Mirror
Parabolic
Mirror
Knife edge
1 mm 
aperture
TestSection
Mirrored 
Surface
Mirrored 
Surface
Light
Source
High speed 
camera
Flat Mirror
Injector
Figure 1. a) Z-type schlieren system, b) double-pass schlieren system.
Downloaded from SAE International by Dalian Univ of Technology, Monday, August 31, 2026

<!-- PDF_PAGE: 6 -->

The reflected light was slightly misaligned so that a small 
flat mirror could be used to redirect the light away from 
the original light source.  The knife edge and camera 
were the same as above.  Since the light passes through 
the test section twice and is, therefore, deflected by the 
density gradients twice, the sensitivity of this type of 
system is naturally greater than that of a z-type system.  
Coma and astigmatism aberrations are also present with 
this system and can only be reduced by using the 
parabolic mirror as close to on-axis as possible.  Some 
blurring or “ghosting” will always be present.
OPERATING CONDITIONS 
The injector used in this investigation had three equally 
spaced, 0.8 mm diameter holes in its nozzle tip.  
Injections were made into a 3.7 liter quiescent chamber 
filled with either nitrogen or carbon dioxide. The injection 
and chamber densities and pressures investigated are 
shown in Table 1. Note that the pressures and densities 
are all absolute stagnation values, excepting 
p* and U*.
Carbon dioxide was used as a chamber gas to provide a 
higher density that would more closely simulate the 
conditions inside the cylinder of an engine. The densities 
for nitrogen and carbon dioxide were also matched for 
two conditions to show that the density ratio and not 
pressure ratio or chamber gas specific heat ratio were 
important to the morphology and penetration of turbulent 
jets. Nitrogen was also injected into nitrogen in order to 
test the sensitivity limits of the schlieren system, and to 
investigate the density variations due to the expansion 
process independent of composition.
End-on imaging utilizing the double-pass schlieren 
system provided another view of the jet pattern 
produced by each injector.  Looking directly towards the 
tip of the injector allowed for a qualitative analysis of the 
ability of each injector to fill a volume and also look into 
the possible interaction of the jets from each hole of the 
injector.
RESULTS
VERTICAL IMAGING 
Figure 2 shows sequences of images acquired for the 
three hole injector with H 2 as the injected fluid and CO 2
at 12.8 kg/m 3 as the chamber fluid.  The data were 
acquired at 10,000 fps, giving 100 Ps between images.  
Figure 2 a) had an injection pressure of 104 bar, and 
Fig. 2 b) had an injection pressure of 52 bar. The injector 
was oriented such that the central plume was injected 
into the light propagation direction, and the two outer 
plumes are oriented slightly in the direction of the light 
propagation.  The angle of inclination was the same for 
all of the jets.  The horizontal white line represents the 
tip penetration distance determined by the method 
described below.  The schlieren images were 
normalized by the image acquired just before injection in 
order to remove optical system imperfections from the 
images.  Not visible in the images is the window 
aperture, which is just above the nozzle tip and limits the 
field of view in the lateral direction at later times. 
The effect of higher injection pressure in Fig. 2 is to 
increase the penetration rate of the jets, with little 
apparent change in the jet structure.  It is clear in the 
figures, however, that there is a significant variation in 
the tip penetration between the three holes.  In 
particular, the central plume is seen to penetrate slower 
than the two outer plumes in Fig. 2 a) and the leftmost 
plume appears to penetrate the fastest in Fig. 2 b).  The 
central plume consistently shows the lowest penetration 
rate.
Under the high chamber density conditions, such as 
shown in Fig. 2, the expansion waves in the chamber 
gas can be clearly seen.  The expansion waves originate 
at the start of injection as the injection begins, and 
radiate spherically outward.  The interaction of the 
reflected waves from the chambers surfaces can be 
seen later in the injection event. 
End-on imaging results are shown in Fig. 3 for helium 
injected into nitrogen at two densities.  The plume in the 
lower left region of the image can be seen to be 
Table 1. Operating conditions for experiment.  The ‘S’ indicates side-view imaging and the ‘E’ indicates end-on 
imaging.
     Chamber Density [kg/m3]
(Chamber pressure [bar]) 
     1.15 
(1.0)
3.8
(3.3)
8.2
(7.2)
8.2
(4.6)
12.8
(7.2)
   p* 
[bar]
U*
[kg/m3] N2 N 2 N 2 CO 2 CO 2
52 H 2 27.8 2.8 S S S S S 
104 H 2 55.0 5.5 S S S S S 
52 He 25.7 5.5 S,E S,E S,E S S 
104 He 51.1 10.6 S,E S,E S,E S S 
52 N 2 27.5 37.3 S S S S S 
Injection
Pressure 
[bar]
69 N 2 36.5 49.5 S S S S S 
Downloaded from SAE International by Dalian Univ of Technology, Monday, August 31, 2026

<!-- PDF_PAGE: 7 -->

a)
b)
Figure 2  Time sequence of injection of hydrogen at a) 104 bar, and b) 52 bar into a CO2 environment at 12.8 kg/m3.  The time between images is 100 Ps.
Downloaded from SAE International by Dalian Univ of Technology, Monday, August 31, 2026

<!-- PDF_PAGE: 8 -->

penetrating at a lower rate than the other two plumes.  
This is the same plume that was the slowest to 
penetrate in Fig. 2.  The jets appear to be slightly 
different diameters in Fig. 3, but this is an artifact of the 
schlieren imaging system and the orientation of the knife 
edge.  In general, for this injector there is very little 
plume-to-plume interaction. 
Figure 4 a) – c) show individual images of hydrogen 
injected into a nitrogen environment of increasing 
density.  At the low chamber density the structure of the 
expansion waves can clearly be seen, with a strong 
density gradient normal to the jet axis at some distance 
downstream from the nozzle, and periodic structures of 
decreasing intensity as you move downstream.  The 
structures are still visible in Fig. 4 b) at 3.8 kg/m
3, but the 
spacing is smaller.  At the highest density shown for 
hydrogen injection in Fig. 4, this structure is not seen.
In order to isolate the density field independent of the 
mixing process, nitrogen was injected into a nitrogen 
atmosphere, and the results are shown in Figs. 4 d) – f).  
The magnification in the nitrogen injection cases was 
also increased.  The presence of the density gradients 
associated with the expansion process is very clearly 
seen in Figs 4 d) – f).  Further the spacing of the 
structures is seen to decrease with increasing chamber 
density as was seen for hydrogen.  It should be noted 
that the specific heat ratio, 
J, for both hydrogen and 
nitrogen is ~1.4. 
a)
b)
Figure 3  End view of helium at 104 bar injected into 
a nitrogen-filled chamber at a) 1.15 kg/m3
and b) 3.8 kg/m3.
a)
 b)
 c)
d)
 e)
 f)
Figure 4  Expansion wave structure for hydrogen injected at 104 bar into nitrogen at a density of a) 1.15, b) 3.8 and c) 
8.2 kg/m3; and nitrogen injected at 69 bar into nitrogen at a density of d) 1.15, e) 3.8 and f) 8.2 kg/m3.
Downloaded from SAE International by Dalian Univ of Technology, Monday, August 31, 2026

<!-- PDF_PAGE: 9 -->

The distance from the nozzle exit to the first normal 
expansion wave, which will be termed the barrel length, 
was measured for a range of conditions, and the results 
are shown in Fig. 5.  The barrel length when normalized 
by the jet diameter was found to scale linearly with the 
exit pressure ratio.  The slope for the nitrogen and 
hydrogen cases were nearly identical because 
J is the 
same.  This linear relationship is in agreement with the 
measurements of Ewan and Moodie [13].
MEASUREMENTS
PENETRATION
The jet tip penetration distance was measured for every 
frame of the vertically imaged data.  The tip was defined 
as the location along the centerline of the injector where 
the intensity fell below a specified value.  Because the 
central plume for this injector was angled out of the 
effective image plane, the measured axial penetration 
was corrected by the cosine of the angle (45
q) to get the 
actual jet tip penetration.  The orientation of the knife 
edge was chosen to accentuate the jet tip, and Fig. 6 
illustrates the methodology.
3.0
2.5
2.0
1.5
1.0
0.5
0.0
Barrel Length / Diameter
6050403020100
Pe / Pc
 H2 into N2
 N2 into N2
Figure 5  Measured expansion wave spacing as a 
function of the nozzle exit pressure ratio. 
Penetration
45
o
Figure 6  Penetration measurement approach. 
This method of measuring penetration over-predicts the 
true penetration due to the shape of each individual jet, 
and its projection onto the plane.  The head of the jet 
causes the measured vertical distance to be slightly 
greater than the actual penetration as shown in Fig. 7.  
Additional error is induced by the choice of the centerline 
position for measuring the penetration, which was done 
for convenience for the automated processing of the 
images.
45
o
Measurement Error
Correct 
Measurement
Measurement
Figure 7  Measurement error associated with the 
projection of the head vortex. 
Figure 8 shows the jet tip penetration for injection 
pressures of 52 and 104 bar into different chamber 
densities, where nitrogen was the chamber gas for all 
cases except the 12.8 kg/m
3 density.  Two individual 
runs are shown for each condition to give an indication 
of the system repeatability.  In part, the repeatability 
could be improved by averaging along several radial 
paths to reduce the susceptibility to turbulent structures 
on the jet axis.  The jet penetration rate increases with 
increasing injection pressure as would be expected.  For 
both injection pressures, the effect of increasing the 
chamber density is to decrease the penetration rate, as 
expected.
Downloaded from SAE International by Dalian Univ of Technology, Monday, August 31, 2026

<!-- PDF_PAGE: 10 -->

NORMALIZATION OF DATA 
The jet penetration data can be normalized to 
investigate whether the underexpanded jets observe a 
self-similar behavior as described above.  The methods 
of Hill and Ouellette [4] and Abraham [10] rely on the 
invariance of the axial momentum, 
Uu2A, in the flow.  
However, as seen above, the pressure field is not 
constant for underexpanded jets at the exit pressures 
investigated in this work.  Thus, while the scaling 
described above is valid in the downstream section of 
the jet it may fail near the nozzle, and the momentum 
flux from the nozzle must include the contribution from 
the nozzle exit pressure (
p*).
After exiting the nozzle and when a Mach disc is 
present, the flow continues to expand supersonically 
until passing through a normal shock at the Mach disc.  
Ewan and Moodie [13] and Birch 
et al . [14] have 
proposed an effective or pseudo-diameter of a sonic 
(M=1) jet that has the same mass flux as the 
underexpanded jet.  For both cases the momentum flux 
of the sonic jet of the larger diameter does not balance 
the pressure force correction to the nozzle exit 
momentum flux. 
In this work a simple model of the jet expansion was 
used.  The jet was assumed to expanded supersonically 
outside of the nozzle with a concomitant decrease in 
pressure.  The flow then undergoes a normal shock to 
reach the chamber pressure.  The necessary equations 
and their solution are outlined in the Appendix.  In this 
approach both the mass and momentum flux of the 
original jet are preserved at the pseudo-Mach disc 
location, which is referred to by the subscript PMD.  The 
result is a subsonic jet of diameter 
dPMD, subsonic 
velocity UPMD and density UPMD, where the density is very 
close to the jet fluid at the chamber temperature and 
pressure.
The presumed subsonic jet can then be described by the 
incompressible scaling relations described above.  The 
method employed here is a slight modification to the eq. 
(5).  A characteristic length, 
x+, and time, t+, scale are 
defined as 
 U U
PMD
PMD
c
xd  (10) 

U
U 
PMD
PMD
c
PMD
d
t U  (11) 
from which a nondimensional length {x xx  and 
nondimensional time {tt t  can be formed.  Equation 
(5) can then be written as 
§· ¨¸S©¹

12
12
3
8
f
t
t
CZt C . (12) 
Figure 9 shows all of the data from Fig. 8 recast in these 
nondimensional variables.  Late in the injection process 
the curves are seen to follow an approximately linear 
relationship between 
Z and t, showing that a self-
similar state has been achieved.  The deviation from 
linearity for a given curve is comparable to the variability 
seen in Fig. 8.
There are two unexplained trends in Fig. 9.  First, there 
appears to be a slight trend for the lower injection 
pressure data to lie towards the right of the high injection 
pressure data.  Secondly, there appears to be a change 
a)
100
80
60
40
20
0
Jet Penetration [mm]
3000200010000
Time [µs]
Uch [kg/m
3
] =1.15 
3.8
8.2
12.8
b)
100
80
60
40
20
0
Jet Penetration [mm]
3000200010000
Time [µs]
Uch [kg/m
3
] =1.15 
3.8
8.2
12.8
Figure 8  Jet tip penetration data for a) 52 bar injection 
pressure and b) 104 bar injection pressure. 
Downloaded from SAE International by Dalian Univ of Technology, Monday, August 31, 2026

<!-- PDF_PAGE: 11 -->

in the slope at the early times for all of the curves.  One 
possible explanation is the fact that the virtual origin has 
not been corrected in these data because of the difficulty 
in assigning the origin to the data when they are related 
to the pseudo-Mach disc location.  A possible cause for 
the change in slope is the use of the far-field 
entrainment relations.  An approach such as employed 
by Naber and Siebers [15] that accounts for the near-
field region and allows for the variable jet spreading 
angle may accommodate these effects better. 
100
80
60
40
20
0
Z
50403020100
t
½
~
~
Figure 9  Nondimensional form of the jet penetration for 
all of the data of Fig. 8.  The dashed and solid 
lines correspond to an injection pressure of 52 
and 104 bar respectively.
CONCLUSIONS
Hydrogen injection into a constant volume chamber was 
visualized using a high frame rate schlieren system.  A 
Z-type schlieren system was used to investigate the jet 
structure and the jet morphology, most importantly the 
penetration rate.  A double-pass schlieren system was 
used to investigate the interaction between the jets and 
provide more information about the jet structure.  Under 
all conditions tested the jets were underexpanded. 
The schlieren system had sufficient sensitivity to allow 
the expansion wave structure outside of the nozzle to be 
visualized both with hydrogen injection into a nitrogen 
ambient, and with nitrogen injection into nitrogen.  The 
latter was performed to confirm that the observed 
structure was independent of the mixing process.  The 
spacing of the structures was found to scale directly with 
the ratio of the nozzle exit pressure to the chamber 
pressure.  A similar scaling has been observed 
previously for the barrel shock length. 
The jet tip penetration rate was measured and  found to 
increase with injection pressure and decrease with 
increasing chamber density.  A new method for 
determining the post expansion wave jet properties was 
described, and used to investigate the far-field jet 
behavior.  Nondimensional length and time coordinates 
were formed, and all of the data were found to follow a 
linear relationship between the nondimensional length 
and the square root of the nondimensional time.  This 
agrees with incompressible jet theory. 
ACKNOWLEDGMENTS
Support for this work was provided by the Ford Motor 
Company.  The authors would also like to acknowledge 
insightful conversations with Prof. R.D. Reitz and Dr. Y. 
Ra.
REFERENCES
1. Tang, X., Kabat, D. M., Natkin, R. J., Stockhausen, 
W. F. and Heffel, J., “Ford P2000 Hydrogen Engine 
Dynamometer Development,” SAE Paper 2002-01-
0242, 2002. 
2. Wimmer, A., Wallner, T., Ringler, J. and Gerbig, F., 
“H2-Direct Injection~A Highly Promising Combustion 
Concept,” SAE Paper 2005-01-0108, 2005. 
3. DeRisi, A., Gajdeczko, B.F. and Bracco, F.V., “A 
study of H2, CH4, C2H6 mixing and combustion in a 
direct-injection stratified-charge engine,” SAE Paper 
971710, 1997. 
4. Hill, P.G.. and Ouellette, P., “Transient turbulent 
gaseous fuel jets for diesel engines,” 
Journal of 
Fluids Engineering, 121, pp. 93-101, 1999. 
5. Turner, J.S., “The starting plume in neutral 
surroundings, J. Fluid Mech,, 13, pp.356-368, 1962. 
6. Ricou, F.P. and Spalding, D.B., “Measurements of 
entrainment by axisymmetrical turbulent jets, J. Fluid 
Mech., 11, pp. 21-32, 1961. 
7. Rizk, W., “Experimental studies of the mixing 
processes and flow configurations in two-cycle 
engine scavenging,” 
Proceedings of the IMECHE, 
Series E, 172, pp.417-424, 1958. 
8. Miyake, M., Biwa, T., Endoh, Y., Shimotsu, M., 
Murakami, S. and Komoda, T, “The development of 
high output, highly efficient gas burning diesel 
engines,” Paper D11.2, CIMAC Conference, Paris, 
1983.
9. Chepakovich, A., “Visualization of transient single- 
and two-phase jets created by diesel engine 
injectors,” M.A.Sc. thes is, University of British 
Columbia, 1993. 
10. Abraham, J., “Entrainment characteristics of 
transient gas jets,” 
Numerical Heat Transfer, Part A.,
30, pp. 3478-364. 1996. 
11. Schlichting, H., Boundary Layer Theory , McGraw-
Hill, New York, 1976. 
12. Settles, G., Schlieren and shadowgraph techniques : 
visualizing phenomena in transparent media , New 
York, Springer, 2001. 
Downloaded from SAE International by Dalian Univ of Technology, Monday, August 31, 2026

<!-- PDF_PAGE: 12 -->

13. Ewan, B.C.R. and Moodie,K. “Structure and velocity 
measurement in underexpanded jets,” Combustion 
Science and Technology, 45, pp. 175-288, 1986. 
14. Birch, A.D., Brown, M.G., Dodson, M.G. ans 
Swaffield, F., “The structure and concentration 
decay of high pressure jets of natural gas,” 
Combustion Science and Technology , 36, pp. 249-
261, 1984. 
15. Naber, J.D. and Siebers, D.L. “Effects of gas density 
and vaporization on penetration and dispersion of 
diesel sprays,” SAE Paper 960034, 1996. 
APPENDIX A 
Consider the flow from the stagnation condition, 
subscript 0, through an converging-diverging nozzle to a 
supersonic state 3 just upstream of a normal shock.  The 
downstream conditions of the normal shock are the 
pseudo-Mach disc state, subscript PMD, that has 
pressure equal to the chamber pressure, 
Pc.  The 
combination of the isentropic and normal shock relations 
gives the following relation that defines the Mach 
number at state 3, 
M3


2
3
1
0 2
3
21
1
11 2
c
/
M
P
P
M
JJ 
J J 
J 
J§·¨¸©¹
 (A.1) 
Using the isentropic relations, the area ratio can be 
found as 

J
JJ§·¨¸ ¨¸J¨¸
©¹
1
212
3
3
*
3
111 2
1
2
MA
AM  (A.2) 
where the * conditions are the choked conditions that in 
this case corresponds to the nozzle exit.  The density 
relation is given by 


2
3
2
3
1
0 12
3
1
12
11 2
PMD
M
M
M
J
J
J U  U J§·¨¸©¹
. (A.3) 
The results from eq. (A.1) - (A.3) are shown in Fig. A1, 
where the results are normalized to the nozzle exit 
(throat) conditions for convenience.  The pseudo-Mach 
disc diameter and density are found to follow a power-
law scaling with the pressure ratio, with a ½ exponent for 
diameter and -1 exponent for density.  The ½ power 
relation for the diameter agrees with the mass-balancing 
diameter proposed by Ewan and Moodie [13] and Birch 
et al . [14], which may explain the success that those 
authors experienced.  There is, however, a multiplicative 
difference between all of the results.
It is interesting to note that the above scaling for 
diameter and density, and the relatively slight scaling of 
velocity provides a nearly constant momentum flux ratio 
for the pseudo-Mach disc state and the nozzle exit, i.e. 
(
ȡU2A)PMD / ( ȡU2A)n is weakly dependent on P0/Pc.  The 
constant of proportionality is not, however, unity.  Thus, 
scaling arguments based on the nozzle exit momentum 
will be preserved, but the quantitative value of the 
proportionality constant will be incorrect. 
0.01
0.1
1
10
1
2 3 4 5 6
10
2 3 4 5 6
100
P0 / Pc
dPMD / d
UPMD / U*
UPMD / U*
1/2
-1
Figure A1  Diameter, velocity and density ratios for the 
pseudo-Mach disc state as compared to the 
nozzle exit condition. 
NOMENCLATURE
A area
A3 size of normal shock 
A* area of choked condition 
Cf fraction of the steady centerline velocity 
Ct parameter relates the turbulent 
diffusivity to kinematic momentum flux 
de  Effective diameter 
f focal length of a lens divided by a 
diameter of lens 
M Mach number 
M3 Mach number right before the normal 
shock
P0 pressure at reservoir 
Pc chamber pressure 
p* nozzle exit pressure 
PMD Pseudo-Mach Disc 
Downloaded from SAE International by Dalian Univ of Technology, Monday, August 31, 2026

<!-- PDF_PAGE: 13 -->

t time 
u velocity 
Ui injection velocity 
Zt tip location of the jet 
U density
U0 density at reservoir
J specific heat ratio 
Downloaded from SAE International by Dalian Univ of Technology, Monday, August 31, 2026
