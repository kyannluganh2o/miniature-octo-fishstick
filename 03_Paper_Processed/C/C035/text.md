<!-- PDF_PAGE: 1 -->

ViewOnline
ExportCitation
RESEARCH ARTICLE |  JANUARY 29 2021
Experimental investigation of shock-induced tandem droplet
breakup
Zhaoguang Wang (王召光)  
  ; Thomas Hopfes 
  ; Marcus Giglmaier 
  ; Nikolaus A. Adams
Physics of Fluids 33, 012113 (2021)
https://doi.org/10.1063/5.0039098
Articles You May Be Interested In
Instability mechanisms of the bag-stamen breakup
Physics of Fluids (February 2026)
Temporal properties of secondary drop breakup in the bag-stamen breakup regime
Physics of Fluids (May 2013)
Morphological classification of low viscosity drop bag breakup in a continuous air jet stream
Physics of Fluids (November 2010)
 29 August 2026 10:04:54

<!-- PDF_PAGE: 2 -->

Physics of Fluids ARTICLE scitation.org/journal/phf
Experimental investigation of shock-induced
tandem droplet breakup
Cite as: Phys. Fluids 33, 012113 (2021 ); doi: 10.1063/5.0039098
Submitted: 30 November 2020 • Accepted: 31 December 2020 •
Published Online: 29 January 2021
Zhaoguang Wang ( 王召光),a)
 Thomas Hopfes,
 Marcus Giglmaier,
 and Nikolaus A. Adams
AFFILIATIONS
Chair of Aerodynamics and Fluid Mechanics, Technical University of Munich, 85748 Garching, Germany
a)Author to whom correspondence should be addressed: zg.wang@tum.de
ABSTRACT
For deeper insights into the dynamics of dense sprays, the present experimental work investigates the shock-induced breakup of two identi-
cally sized water droplets in tandem formation. The breakup process is visualized in a shadowgraph system and captured by an ultra-high-
speed camera. The experimental Weber number ranges from 13 to 180, and the separation distance between the droplets is varied between 1.2
and 10.5 times of the droplet diameter. While the tandem formation exerts marginal influence on the lead droplet, the breakup intensity of
the trailing droplet is consistently attenuated as the separation distance falls below critical levels. The time of initial deformation is postponed,
the maximum cross-stream diameter is reduced, and the mean drag coefficient is lowered. These effects are more profound at lower Weber
numbers and closer separation distances. The attenuation of the breakup intensity is also reflected by the formation of smaller bags in bag
and bag-and-stamen morphologies and by the narrower cross-stream dispersion of fragments in multibag and shear stripping morphologies.
When positioned in close proximity to the lead droplet, the trailing droplet fails to follow the conventional breakup morphologies. Instead, it
either punctures or coalesces with the lead droplet.
Published under license by AIP Publishing. https://doi.org/10.1063/5.0039098
I. INTRODUCTION
Droplet breakup is a relevant phenomenon in a variety of appli-
cations, including fuel injection, 1 powder metallurgy, 2 and spray
coatings.3 Previous research has concluded that the droplet breakup
process is mainly governed by the Weber number ( We) and the
Ohnesorge number (Oh),4,5
We= ρgug
2d0/σ, (1)
Oh= μd/
√
ρdd0σ, (2)
where ρg and ug are the density and the velocity of the gas flow and
d0, σ, μd, and ρd are the initial diameter, the surface tension, the
dynamic viscosity, and the density of the liquid droplet. The Weber
number and the Ohnesorge number compare the disruptive aero-
dynamic force and the viscous force against the restorative surface
tension, respectively. When Oh < 0.1, the significance of the liquid
viscosity becomes negligible and We turns to be the sole dominant
factor.6
The aerodynamic breakup of single droplets has been exten-
sively investigated and reviewed in detail by Pilch and Erdman, 7
Faeth et al. ,8 and Guildenbecher et al. 6 As the aerodynamic force
becomes increasingly intense, the corresponding breakup pattern
transitions from bag breakup 9–11 to stripping breakup. 12–14 There
exist several in-between multimode morphologies, 15,16 and the two
covered in the current work are bag-and-stamen breakup 7,17 and
multibag breakup.18,19
However, the conventional understandings of single droplet
breakup do not describe the breakup behavior in dense sprays
accurately. In practical applications such as diesel injections 20 and
agricultural sprays, 21 droplets appear in close proximity instead of
being isolated. The interaction between adjacent droplets has to be
considered to properly estimate the fragment sizes. Therefore, the
arrangement of droplets in tandem formation is more representative
than single droplets, and the initial on-center separation distance
s between the tandem droplets becomes an additional variable of
importance. The associated tandem breakup behavior is investigated
thoroughly in the current work.
Most of the previous research about droplets in tandem for-
mation is dedicated to the evaluation of drag coefficients. Liu
et al. 22 study experimentally the laminar flow field around an infi-
nite droplet chain with the normalized on-center separation distance
Phys. Fluids 33, 012113 (2021); doi: 10.1063/5.0039098 33, 012113-1
Published under license by AIP Publishing
 29 August 2026 10:04:54

<!-- PDF_PAGE: 3 -->

Physics of Fluids ARTICLE scitation.org/journal/phf
S= s/d0 varied between 2 and 12. They conclude that the drag coeffi-
cient of monodisperse droplets is up to an order of magnitude lower
than the drag coefficient of isolated droplets. Mulholland et al. 23
conduct similar experiments but with S ranging from 1.7 to 1700.
They propose an empirical formulation to model the drag coefficient
and find that the value is significantly diminished as the separation
distance drops below 150. Poo and Ashgriz 24 investigate a stream
of closely spaced droplets with S < 5 in a turbulent flow and state
that the drag coefficient is 4–5 times smaller compared to isolated
droplets. There are other studies with the focus on a finite num-
ber of droplets in tandem formation instead of an infinite stream.
Temkin and Ecker 25 study the interaction between two droplets
with S from 1.5 to 11 and Reynolds numbers below 150. Based
on the quantified changes of drag coefficients, they show that the
upstream droplet is not affected by the tandem formation while the
downstream one experiences reduction up to 50%. The result also
suggests that the region of influence behind the upstream droplet
extends over 15 droplet diameters. Nguyen and Dunn-Rankin 26
examine vertically falling droplet packets composed of 4 droplets
separated by 5.5 diameters with the Reynolds number around 80.
They analyze the trajectory of the first trailing droplet and present
that the drag coefficient is 25% lower than that of the lead droplet.
Chiang and Sirignano 27 investigate numerically the transportation
of three droplets aligned with the flow direction. Their results
indicate that the drag of the first two droplets differs profoundly
while the difference between the downstream two droplets becomes
insignificant.
The amount of research focusing on the deformation and
breakup of tandem droplets is very limited, among which the exper-
imental work is even scarcer. Zhao et al. 28 conduct experiments of
two neighboring droplets at We = 12.3 in the bag breakup regime
with the normalized separation distanceS below 3. For cases with the
two droplets positioned in tandem, they report a coalescence mode
at S < 1.3 and a puncture mode at higher S. Igra and Takayama 29
experimentally investigate the shear stripping breakup of two water
columns separated 5 diameters away at the Weber number of 6900.
The same breakup behavior as single columns is observed for the
front column while the rear one deforms at a much lower rate. Oth-
ers adopt numerical methods for the relevant research. Quan et al.30
employ a finite-volume scheme to investigate the deformation of
tandem droplets spaced within 6 diameters at Weber numbers of 40,
4, and 0.4. They present a mushroom shape formed by the droplet
pair at the two largest Weber numbers with S= 1.6. Simulations of
similar tandem arrangements are carried out by Kékesi et al.,31 with
the Weber number of 20 and the separation distance from 1.5 to
5 droplet diameters. They conclude that the trailing droplet either
shoots through or merges with the lead droplet and its breakup
time is increased significantly. Stefanitsis et al. 32 apply the volume
of fluid method to study the breakup of four diesel droplets in tan-
dem formation at Weber numbers varied between 15 and 64. They
analyze the deformation of the third droplet and present a new
breakup mode termed shuttlecock. Their results show that the inter-
action between tandem droplets becomes important for separation
distances below 9 droplet diameters.
To shed more light on the breakup features of tandem droplets,
the current experimental work intends to assess the significance of
the tandem formation over a wide range of Weber numbers and
separation distances. In contrast to most of the previous works
that focus on the evaluation of drag reduction, we place emphasis
on detailed description of deformation patterns and breakup struc-
tures. The present results can serve as bases for potential numerical
validations and for more accurate modeling of fragment sizes and
dispersion.
II. EXPERIMENTAL SETUP
The layout of the shock tube and the measurement system
employed in the present work is provided in Fig. 1. The setup is the
same as described in our previous work, 33 except for the position of
the cookie-cutter. The square cookie-cutter, which conventionally
locates upstream of the test section to remove boundary layers, is
shifted downstream to achieve a longer period of steady-flow condi-
tions. Figure 2 sketches the propagation of the incident shock inside
the tube, and Fig. 3 plots the corresponding post-shock pressure at
the test point measured by PCB Piezotronics ICP ® fast-response
pressure sensors. When reaching the front of the test section, the
incident shock partially reflects since the cross section contracts to a
190 × 190 mm2 square (t = −0.5 ms in Fig. 2). The reflected shock
leads to a short transition period ( ∼0.2 ms) after the pressure at
the test location experiences a stepwise increase at the arrival of
the incident shock ( t = 0 ms in Fig. 3). As the incident shock exits
from the test section, the increase in the cross-sectional area induces
FIG. 1. Layout of the shock tube and the measurement system.
Phys. Fluids 33, 012113 (2021); doi: 10.1063/5.0039098 33, 012113-2
Published under license by AIP Publishing
 29 August 2026 10:04:54

<!-- PDF_PAGE: 4 -->

Physics of Fluids ARTICLE scitation.org/journal/phf
FIG. 2. Wave dynamics inside the test section. The test section is marked with
gray shades. The incident shock propagates from left to right. IS: incident shock;
RS: reflected shock; EW: expansion wave.
generation of additional expansion waves ( t = 2.2 ms in Fig. 2).
These expansion waves propagate upstream and give rise to pres-
sure drop and velocity increase at the test location ( t = 4.5 ms in
Fig. 3). By shifting the cookie-cutter to the downstream of the test
section, the upstream propagation of the expansion waves is post-
poned, and thus, the steady-flow time window is prolonged from
∼2 ms in the previous setup33 to∼4.5 ms, at the expense of causing a
short transition period and slightly higher flow fluctuations.
In the current work, the steady-flow period covers the entire
breakup process of cases at high Weber numbers. For cases at the
two lowest Weber numbers (We= 13 and 24), the early-stage defor-
mation and the initiation of bag development are within the steady-
flow period, but the onset of bag rupture is beyond. Nevertheless,
although the timing for the bag rupture is altered by the chang-
ing flow conditions, the main deformation patterns are preserved
for these cases. Particularly, the early-stage parameters quantified in
Sec. III E are not affected.
In the current experiments, the velocity of the incident shock
is calculated by measuring the time difference between moments
when the incident shock passes two 0.75 m-separated pressure sen-
sors directly upstream of the test section. Based on this shock speed
and the initial atmospheric conditions, we conduct 2D axisym-
metric numerical simulations to estimate post-shock flow param-
eters. As shown in Fig. 3, the simulated pressure profile at the
test point is in good agreement with that measured experimen-
tally. This justifies the application of the flow velocity and density
obtained from the numerical simulation in the calculation of Weber
numbers.
In terms of flow visualization, shadowgraph images of the
droplet breakup are recorded by a Shimadzu HyperVision HPV-X
ultra-high-speed camera at framing rates of 10–40 kfps. The images
FIG. 3. Post-shock flow pressure and velocity at the test point (We = 13).
TABLE I. Operating flow conditions summarized from repeated experiments.
We Oh avg Re∞avg Breakup morphology
13 (±1.3) 2.4 × 10−3 2.5 × 103 Bag breakup
24 (±2.2) 2.4 × 10−3 3.4 × 103 Bag and stamen
70 (±3.0) 2.3 × 10−3 6.1 × 103 Multibag breakup
180 (±10) 2.4 × 10−3 1.0 × 104 Shear stripping
are processed with background subtraction, contrast adjustment,
and super resolution using MATLAB’s Very Deep Super-Resolution
convolutional neural network.34 The spatial resolution of the resul-
tant images is∼0.05 mm/pixel. By counting the pixels that constitute
the droplet in the shadowgraph image, the cross-sectional area A is
obtained, and the equivalent droplet diameter d0 is calculated as d0
= 2×(A/π)0.5.
To generate droplets in tandem formation, two syringe nee-
dles separated with a defined spacing are inserted into the test
section. After droplets with the diameter of ∼2 mm are produced
at the needle tips, the syringes are withdrawn rapidly detaching
the two droplets simultaneously. The current experimental matrix
covers four flow conditions, of which the parameters are sum-
marized in Table I based on repeated experiments. The average
Weber numbers investigated are 13, 24, 70, and 180, with the corre-
sponding breakup morphology changing from bag breakup to shear
stripping. The Ohnesorge number for all cases is approximately
2.4 × 10−3, making the viscous effect negligible. 6 The d0-based
freestream Reynolds number Re∞,
Re∞= ρgugd0/μg, (3)
increases from 2.5 × 103 to 1.0 × 104. Under each flow condition,
seven on-center separation distances S = s/d0 between 1.2 and 10.5
are studied. In addition, single droplet experiments are conducted as
well for more comprehensive comparisons.
III. RESULTS AND DISCUSSION
In the current study, the experiment time t is normalized
against the characteristic transport time derived by Ranger and
Nicholls12 to yield the non-dimensional time T,
T = t ⋅ug/(d0
√
ρd/ρg). (4)
The time for lead and trailing droplets is zeroed at the instant of the
incident shock impacting on their respective frontal surface. Nev-
ertheless, the time shift between the tandem droplets is less than
0.06 ms for all cases and insignificant compared to the duration of
the breakup process at current conditions. For the sake of consis-
tency and brevity, only the time for the lead droplet is provided in
the following image sequences. As presented in Fig. 3, the freestream
flow condition remains steady until t = 4.5 ms. The corresponding
non-dimensional time instants are approximately T = 1.7, 2.2, 3.6,
and 6.0 for current experiments at Weber numbers of 13, 24, 70, and
180, respectively. The breakup process is completed under constant
flow conditions for high Weber numbers but slightly exceeds the
Phys. Fluids 33, 012113 (2021); doi: 10.1063/5.0039098 33, 012113-3
Published under license by AIP Publishing
 29 August 2026 10:04:54

<!-- PDF_PAGE: 5 -->

Physics of Fluids ARTICLE scitation.org/journal/phf
steady-flow period for low Weber numbers. In the following texts,
time instants that exceed this period are marked with T∗instead
of T.
Figure 4 provides an overview of the interactive modes between
the tandem droplets. Considering that the lead droplet breakup is
marginally influenced by the tandem formation, Fig. 4 only cate-
gorizes the change of the breakup pattern for the trailing droplet
at different separation distances S and Weber numbers We. In
the figure, the x-axis S is plotted on the linear scale and the
y-axis We on the logarithmic scale. The entire S–We map is divided
into three regions. The independent breakup region at the top-right
corner represents cases where the trailing droplet undergoes the
same breakup process as the lead droplet. The suppressed breakup
region at the bottom-left corner contains cases where the trailing
droplet fails to follow the breakup morphology of the lead droplet
but exhibits either puncture or coalescence modes instead. For cases
in the transition region, the breakup morphology of the trailing
droplet is the same as that of the lead droplet but the breakup inten-
sity is reduced. The boundary between the independent breakup
region and the transition region is of particular importance because
it represents the critical separation distance below which the interac-
tion of the tandem droplets has to be taken into account. This critical
distance is We-dependent and halved from S = 10.8 at We = 13 to
S= 5.4 at We= 180.
The following presentation of results starts with illustrating the
breakup pattern of the tandem droplets with shadowgraph images
for each breakup morphology individually (Secs. III A–III D). In
each section, representative cases at a certain Weber number in the
transition and the suppressed breakup regions are described in detail
while those in the independent breakup region are omitted for con-
ciseness. The discussion is concluded by quantifying the time of
initial deformation, the maximum cross-stream diameter, and the
mean drag coefficient of the tandem droplets in Sec. III E.
A. Bag breakup
1. Transition region: Smaller bag
for the trailing droplet
For the bag breakup of tandem droplets, the present cases
with separation distances between 4.7 and 10.5 are identified in the
FIG. 4. Change of the breakup pattern of the trailing droplet at different separa-
tion distances and Weber numbers, in comparison to the lead droplet. The map
is divided into three regions (independent breakup region, transition region, and
suppressed breakup region).
transition region. An exemplary case is shown in Fig. 5 with S= 5.8
and We = 13. Here, the lead droplet replicates the breakup process
of single droplets and experiences initial flattening ( T = 1.0), bag
inflation (T = 1.5), bag rupture (T∗= 2.35), and ring disintegration
(T∗= 2.8) sequentially. The trailing droplet exhibits the same
breakup morphology as the lead droplet but is flattened to a lower
cross-stream diameter (dc) in the early stage and develops a smaller
bag at a later time. In all following figures that present breakup
structures, the explanatory notes on the right describe the breakup
progress of the trailing droplet.
As demonstrated by the top row in Fig. 6, the main variation
within the transition region is that the bag formed by the trail-
ing droplet becomes consistently smaller as the separation distance
decreases. The reduction of the bag size is associated with the less
pronounced flattening in the early stage and results from the fact
that the wake flow of the lead droplet shields the trailing droplet and
lowers the pressure imposed on its windward surface. This shield-
ing effect is stronger at closer separation distances. The bottom row
in Fig. 6 compares the ring structure of the trailing droplet after
fragmentation of the bag. On the one hand, smaller bags mean that
less mass is shed off through the bag rupture and more remains
in the toroidal ring. On the other hand, the bag size also deter-
mines the diameter of the ring in a proportional way. Consequently,
under the combined influence of these two factors, the ring is thick-
ened when the trailing droplet is in closer proximity to the lead
FIG. 5. Weaker flattening and smaller bag size for the trailing droplet under the
shielding effect of the lead droplet ( S = 5.8, We = 13). The freestream direction
is from left to right for all presented images. As labeled, s and d c are the initial
on-center separation distance and the cross-stream diameter, respectively.
Phys. Fluids 33, 012113 (2021); doi: 10.1063/5.0039098 33, 012113-4
Published under license by AIP Publishing
 29 August 2026 10:04:54

<!-- PDF_PAGE: 6 -->

Physics of Fluids ARTICLE scitation.org/journal/phf
FIG. 6. Variation of the bag size and the ring thickness at different separation dis-
tances for the trailing droplet in the bag breakup regime. The top and bottom rows
correspond to time instants prior and subsequent to the bag rupture, respectively
(We = 13, 12, 13, and 15 from left to right).
droplet. Although the time instants shown in Fig. 6 are beyond the
steady-flow period, all cases still share approximately the same flow
conditions, and thus, the tendency presented here remains valid
qualitatively.
2. Suppressed breakup region: Puncture of the lead
droplet by the trailing droplet
The interaction of the tandem droplets at separation distances
S= 2.1 and 3.8 is identified as the puncture mode in the suppressed
breakup region. The corresponding breakup features are exemplified
by the case at S= 2.1 in Fig. 7. The deformation of the lead droplet
progresses in a conventional manner untilT= 1.7 when the collision
FIG. 7. Puncture of the bag structure of the lead droplet by the trailing droplet ( S
= 2.1, We = 14).
with the trailing droplet triggers an early rupture of the inflating bag.
In terms of the trailing droplet, the deformation starts with weak-
ened flattening (T= 0.7). As the lead droplet deforms into a thin disk,
the trailing droplet suffers from stronger shielding effects and con-
sequently enters a contraction period. The trailing droplet contracts
into a triangular shape pointing upstream atT= 1.2 and further into
an ellipsoid with the major axis aligned with the streamwise direc-
tion at T = 1.7. The ellipsoidal trailing droplet punctures the bag
structure of the lead droplet at T∗= 2.0 and escapes from its shel-
ter. Being exposed to the freestream flow, the trailing droplet gets
flattened at the windward surface and distorted into a “T” shape at
T∗= 2.5. In the following period, the droplet fails to reproduce the
typical bag breakup but tends to disintegrate into several fragments
of comparable sizes to the original.
3. Suppressed breakup region: Coalescence
of the tandem droplets
The case at S = 1.2 in the suppressed breakup region exhibits
new features as presented in Fig. 8 and is categorized as the coales-
cence mode. The most noticeable feature is the absence of bag struc-
tures. The early-stage flattening of the lead droplet is maintained,
while the deformation of the trailing droplet starts with stream-
wise stretching. The disk-shape lead droplet and the teardrop-shape
trailing droplet ( T = 1.0) coalesce into a funnel shape at T = 1.35.
The coalescence is completed around T = 1.7 when the tail of the
trailing droplet is swallowed entirely. In the later stage, the defor-
mation of the merged body becomes highly disordered. Apart from
the formation and fragmentation of ligament structures ( T∗= 2.8),
the main body tends to split into large children droplets. This coa-
lescence mode and the afore-mentioned puncture mode have also
been observed by Zhao et al. 28 for separation distances below and
above 1.3, respectively, with which our present results are in good
consistency.
FIG. 8. Coalescence of lead and trailing droplets (S = 1.2, We = 13).
Phys. Fluids 33, 012113 (2021); doi: 10.1063/5.0039098 33, 012113-5
Published under license by AIP Publishing
 29 August 2026 10:04:54

<!-- PDF_PAGE: 7 -->

Physics of Fluids ARTICLE scitation.org/journal/phf
FIG. 9. Simplified 2D sketch of streamlines around tandem droplets at S = 1.2.
Stagnation points of the highest static pressure are labeled in red and those of low
pressure in blue.
To better explain how the shielding effect changes the early-
stage deformation of the trailing droplet from cross-stream flatten-
ing to streamwise stretching, Fig. 9 presents a simplified 2D sketch
of streamlines around two closely packed droplets. The red circles
represent stagnation points with the highest static pressure along
the droplet surface, and the blue circles correspond to those with
relatively lower pressure. With the presence of the lead droplet, the
highest pressure at the trailing droplet surface appears at locations
near the equator. The resulting pressure imbalance extrudes a sharp
nose at the droplet front ( T = 0.35 in Fig. 8) and results in the
following streamwise stretching (T = 0.7 in Fig. 8).
In summary, the presence of the lead droplet tends to weaken
the bag inflation of the trailing droplet. This reduces the produc-
tion of fine mist through bag rupture and favors the generation of
large fragments. For a more accurate modeling of the fragment size
distribution, special attention needs to be paid to cases where the
trailing droplet fails to follow bag breakup and produces fragments
with sizes comparable to the initial diameter.
B. Bag-and-stamen breakup
1. Transition region: Smaller bag
for the trailing droplet
For the bag-and-stamen breakup, the transition region covers
experiments with separation distances from S= 3.7 to 8.0 in the cur-
rent study. An exemplary case is shown in Fig. 10 with S = 8.0 and
We = 25. During the initial flattening, a bulge forms at the frontal
surface of the lead droplet, marking the development of a stamen
(T = 1.0). After the bag inflates around the stamen to the maximum
size, the bag rupture, the ring fragmentation, and the stamen disin-
tegration take place in succession. The trailing droplet shares similar
breakup features except that it deforms at a slower rate and develops
a smaller bag.
Figure 11 compares the variation of the bag size (top row)
and the ring/stamen thickness (bottom row) of the trailing droplet
among cases in the transition region. Although detailed breakup
structures are considerably distorted by the shielding effect of the
lead droplet, main bag-and-stamen breakup features are still main-
tained. Nevertheless, the bag of the trailing droplet shrinks and
the ring/stamen structures are thickened as the separation distance
decreases, which is similar to the observations for bag breakup in
Fig. 6.
2. Suppressed breakup region: Puncture of the lead
droplet by the trailing droplet
The two cases with the closest separation distances S= 1.2 and
2.0 lie in the suppressed breakup region, where the lead droplet
FIG. 10. Weaker flattening and smaller bag size for the trailing droplet under the
shielding effect of the lead droplet (S = 8.0, We = 25).
collides with the trailing droplet during the early development of
bag structures as shown in Fig. 12. The shielding effect on the trail-
ing droplet is clearly observed at the very beginning of the defor-
mation. In contrast to the conventional cross-stream flattening, the
FIG. 11. Variation of the bag size and the ring/stamen thickness at different sepa-
ration distances for the trailing droplet in the bag-and-stamen breakup regime. The
top and bottom rows correspond to time instants prior and subsequent to the bag
rupture, respectively (We = 25, 22, 25, and 24 from left to right).
Phys. Fluids 33, 012113 (2021); doi: 10.1063/5.0039098 33, 012113-6
Published under license by AIP Publishing
 29 August 2026 10:04:54

<!-- PDF_PAGE: 8 -->

Physics of Fluids ARTICLE scitation.org/journal/phf
FIG. 12. Puncture of the bag structure of the lead droplet and coalescence of the
trailing droplet with the stamen (S = 1.2, We = 24).
trailing droplet deforms into an arrowhead shape at T = 0.8 and
later together with the flattened lead droplet constitutes a mushroom
shape (T= 1.2). This mushroom layout has also been reported in the
numerical work by Quan et al.30 at We between 4 and 40 and S= 1.6,
which falls between the separation distances of the two present cases
in the suppressed breakup region. At T = 2.0, the trailing droplet
punctures the bag structure of the lead droplet and coalesces with its
stamen. The ligament that stretches at the rear of the intact trailing
droplet at T∗= 2.4 resembles the conventional stamen. In the subse-
quent period, apart from formation of small bags, the main body of
the trailing droplet tends to disintegrate into large pieces.
Overall speaking, the influence of the lead droplet on the
breakup behavior of the trailing droplet in the bag-and-stamen mor-
phology is similar to that in the bag breakup morphology. The bag
development of the trailing droplet is weakened, and more mass is
preserved in the ring/stamen structure or in an intact body. Conse-
quently, a larger portion of the trailing droplet is atomized into large
fragments instead of fine mist.
C. Multibag breakup
1. Transition region: Dampened bag formation
For the multibag breakup, the transition region covers the
current cases with separation distances from S = 1.9 to 6.2. The
breakup behavior of the tandem droplets is characterized in Fig. 13
with the case at S = 6.2 and We = 68. The deformation of the lead
droplet starts with the typical flattening ( T = 1.0), followed by a
short period of bending of the thin peripheral sheet (T= 1.45). Then,
consecutive formation and rupture of bags take place around the
periphery, shedding small mist into the flow (T= 1.85). The remain-
ing stamen-like structure at T = 2.6 further fragments through rup-
ture of tiny bags and fracture of thin ligaments. The trailing droplet
follows the breakup morphology of the lead droplet, but the forma-
tion and rupture of bags are noticeably dampened by the shield-
ing effect. Compared to the bag-and-stamen breakup, the multi-
bag mode leaves a thicker stamen-like structure and generates no
toroidal ring.
2. Suppressed breakup region: Coalescence
of the trailing droplet with the stamen-like structure
of the lead droplet
When the separation distance drops to 1.2, the lead droplet
still maintains main features of the multibag morphology, but the
breakup of the trailing droplet is significantly altered as shown in
Fig. 14. The strong shielding effect shapes the front of the trail-
ing droplet into a sharp cone ( T = 0.4). A liquid sheet is subse-
quently developed along the periphery (T= 0.7) and stretched in the
streamwise direction ( T = 1.0). The elongated trailing droplet col-
lides with the flattened lead droplet at T = 1.4 and coalesces into the
stamen-like structure that emerges at T = 2.6.
In the multibag morphology, the burst of bags of the lead
droplet tends to eject fine fragments widely in the cross-stream
direction. However, since the bag inflation of the trailing droplet is
significantly dampened by the shielding effect as shown in Fig. 13,
FIG. 13. Less intense formation of bags for the trailing droplet under the shielding
effect of the lead droplet (S = 6.2, We = 68).
Phys. Fluids 33, 012113 (2021); doi: 10.1063/5.0039098 33, 012113-7
Published under license by AIP Publishing
 29 August 2026 10:04:54

<!-- PDF_PAGE: 9 -->

Physics of Fluids ARTICLE scitation.org/journal/phf
FIG. 14. Coalescence of the trailing droplet into the stamen-like structure of the
lead droplet (S = 1.2, We = 68).
the resultant fragments gain less cross-stream momentum from the
outward splash of the bag rupture, and thus, the spatial distribu-
tion is substantially confined. After the tandem droplets collide and
merge, their fragments are blended together and dispersed in a con-
ical pattern. Figure 15 compares the dispersion angle of the mixed
fragments at T= 3.0 and shows that the dispersion angle is narrowed
from 81○to 59○as the separation distance decreases from 3.8 to 1.2.
D. Shear stripping
1. Transition region: Narrower fragment dispersion
for the trailing droplet
The last morphology covered in the current work is the shear
stripping breakup, which is also conventionally understood as the
FIG. 15. Dispersion angle of the fragments detaching from the merged body of the
tandem droplets in the multibag regime at T = 3.0 (We = 68, 70, and 68 from left
to right).
ultimate breakup regime. 14 The transition region for this breakup
morphology covers all present cases with S≤4.5, and no suppressed
breakup region is identified in the current work. Figure 16 shows
the exemplary case with S = 3.8 and We = 179. The lead and trail-
ing droplets share the same breakup morphology, consisting of ini-
tial flattening ( T = 0.3), bending of the peripheral sheet ( T = 0.6),
and stripping of fine mist along the sheet ( T = 1.2). The breakup
is characterized by the fragmentation of the peripheral sheet into
thin ligaments and further into micro-droplets. Consecutive infla-
tion and burst of tiny bags along the peripheral sheet is observed at
the very beginning of the fragmentation ( T = 0.85) but ceases in a
short time. The main difference between the tandem droplets is that
in the late stage the trailing droplet is less flattened and the resultant
fragments are dispersed less widely in the cross-stream direction.
Igra and Takayama29 have reported similar observations for tandem
water columns separated at S= 5 for a much higher Weber number
of 6900.
It is worth mentioning that at the smallest separation distance
S = 1.3 in the present study, the trailing droplet is shaped with a
sharply tapered front similarly to that shown in Fig. 14 in the early
stage but follows main stripping breakup features afterward. The
corresponding image sequence is omitted for brevity.
Figure 17 compares the dispersion angle of fragments shed off
the merged body of the tandem droplets at T = 3.0 for cases at S
= 3.8, 2.0, and 1.3. The cross-stream span occupied by the fragments
becomes consistently narrower as the separation distance decreases.
FIG. 16. Narrower cross-stream dispersion of the trailing droplet fragments under
the shielding effect of the lead droplet (S = 3.8, We = 179).
Phys. Fluids 33, 012113 (2021); doi: 10.1063/5.0039098 33, 012113-8
Published under license by AIP Publishing
 29 August 2026 10:04:54

<!-- PDF_PAGE: 10 -->

Physics of Fluids ARTICLE scitation.org/journal/phf
FIG. 17. Dispersion angle of the fragments detaching from the merged body of the
tandem droplets in the shear stripping regime at T = 3.0 (We = 179, 183, and 184
from left to right).
This trend is consistent with that observed in Fig. 15 for the multibag
regime.
E. Quantitative analyses of the early-stage
deformation of the tandem droplets
The early-stage deformation of droplets plays a crucial role
in determining the subsequent breakup morphology, and the asso-
ciated parameters are also of practical importance for numerical
validations. This section quantifies the early-stage behavior of the
tandem droplets and highlights the variation at different Weber
numbers and separations distances. The quantified parameters in
the current work are the time of initial deformation Tini, the max-
imum cross-stream diameter Dcmax, and the mean drag coefficient
Cdmean.
The initial deformation of droplets ends at the time instant of
the minimum streamwise diameter. This time instant Tini marks the
start of the bag inflation for bag and bag-and-stamen morpholo-
gies and the bending of the peripheral sheet over the rear surface
for multibag and shear stripping morphologies. The definition was
proposed by Pilch and Erdman 7 to indicate the breakup initia-
tion and also adopted in other literature. 6,17 The maximum cross-
stream diameter Dcmax is the cross-stream diameter at Tini normal-
ized against the initial diameter. The mean drag coefficient Cdmean is
calculated by fitting the streamwise displacement of the droplet mass
center xmc between T = 0 and Tini into the relation
xmc/d0 = 3/8 ⋅CdmeanT2 (5)
derived by Ranger and Nicholls. 12 For all cases, Tini lies within the
steady-flow time window.
1. Influence of the tandem formation
on the early-stage deformation of the lead droplet
Table II summarizes Tini, Dcmax, and Cdmean of the lead droplet
in different breakup morphologies. The values are averaged from
experiments of which the breakup regime is the same but the sep-
aration distances are varied. The time of initial deformation Tini,lead
decreases consistently from 1.19 atWe= 13 to 0.71 at We= 180. This
tendency is in agreement with the empirical correlation
Tini = 1.9(We − 12)−0.25(1 + 2.2Oh1.6) (6)
TABLE II. The time of initial deformation Tini, the maximum cross-stream diame-
ter Dcmax, and the mean drag coefficient Cdmean of the lead droplet, averaged from
experiments in the same breakup morphology.
We T ini,lead Dcmax,lead Cdmean,lead
13 (±1.3) 1.19 ( ±1.2%) 1.67 ( ±3.6%) 1.40 ( ±1.4%)
24 (±2.2) 1.08 ( ±1.7%) 1.88 ( ±3.9%) 1.58 ( ±2.1%)
70 (±3.0) 0.83 ( ±2.3%) 1.73 ( ±4.2%) 1.25 ( ±3.0%)
180 (±10) 0.71 ( ±2.4%) 1.67 ( ±4.4%) 1.20 ( ±2.3%)
proposed by Pilch and Erdman, 7 except that this correlation pre-
dicts a higher value of 1.9 at We = 13. Meanwhile, the maximum
cross-stream diameter Dcmax,lead peaks with the value of 1.88 for
bag-and-stamen breakup and then declines as We keeps increas-
ing. The data points reported by Zhao et al. 35 show the same
trend but slightly different magnitudes. In terms of the mean drag
coefficient Cdmean,lead, the effect of the droplet flattening is not
excluded in the current calculation. Consequently, in addition to
flow Reynolds numbers, Cdmean,lead is also significantly influenced by
the growth rate of the droplet cross-stream diameter. This explains
the observation that Cdmean,lead follows a similar trend to Dcmax,lead
and that the magnitudes exceed 1.2, which is the drag coefficient
of a circular disk. 36 Overall speaking, the early-stage behavior of
the lead droplet is barely influenced by the tandem formation,
and the quantified parameters are consistent with those of isolated
droplets.
Table II also provides the range of variation for Tini, Dcmax, and
Cdmean. All three parameters vary within the interval of ±4.5%. The
variation is mainly caused by the difference in the flow conditions
(which is also implied by the variation of Weber numbers) and the
irregularity of the initial droplet shapes. Compared to the overall
variation, the measurement uncertainty is relatively low. With cur-
rent framing rates and spatial resolutions of the recorded images,
the uncertainty for temporal and spatial calculations is ±1.3% and
±1.5%, respectively.
2. Influence of the tandem formation
on the early-stage deformation of the trailing droplet
This section is focused on the influence of the tandem for-
mation on the breakup behavior of the trailing droplet. The S–We
maps of the time of initial deformation, the maximum cross-stream
diameter, and the mean drag coefficient are presented sequentially.
Considering that the lead and trailing droplets from one experi-
ment experience identical flow conditions and tend to share simi-
lar initial shapes, the data points presented for the trailing droplet
are normalized against values of the lead droplet, in order to
minimize the uncertainties brought by flow variation and shape
irregularity.
The time of initial deformation of the trailing droplet relative
to the lead droplet Tini,trail/Tini,lead is plotted in Fig. 18 over the S–We
map. Isolines of 1.01, 1.03, 1.06, and 1.09 provided in the figure are
calculated through interpolation of the discrete data points. Cases in
the suppressed breakup region are labeled dark circles and excluded
in the present calculation since the trailing droplet fails to initiate the
breakup independently. Generally speaking, Tini,trail is postponed by
the tandem formation, and the postponement is longer at smaller
Phys. Fluids 33, 012113 (2021); doi: 10.1063/5.0039098 33, 012113-9
Published under license by AIP Publishing
 29 August 2026 10:04:54

<!-- PDF_PAGE: 11 -->

Physics of Fluids ARTICLE scitation.org/journal/phf
FIG. 18. Time of initial deformation of the trailing droplet at different separation
distances and Weber numbers, normalized by values of the lead droplet.
S and lower We. For low- We bag and bag-and-stamen morpholo-
gies, Tini is marked by the end of droplet flattening. The flattening
is caused by the pressure imbalance around the droplet and highly
sensitive to the shielding effect, which significantly reduces the pres-
sure imposed on the front of the trailing droplet as illustrated in
Fig. 9. For high- We multibag and shear stripping morphologies,
however, Tini is indicated by the bending of the peripheral sheet
over the droplet rear. As demonstrated by the experimental work of
Theofanous et al. 37 and Wang et al. ,33 development of the periph-
eral sheet is dominated by the local shear flow around the equa-
tor, which is much less influenced by the shielding effect than the
pressure imbalance around the droplet. Consequently, the postpone-
ment of Tini,trail is strongly reduced as the Weber number increases.
Particularly, the influence is negligible in the shear stripping
regime.
Figure 19 presents the maximum cross-stream diameter of
the trailing droplet normalized against values of the lead droplet
Dcmax,trail/Dcmax,lead. Interpolated isolines of 0.99, 0.97, 0.94, and 0.91
are also displayed. The general tendency is that Dcmax,trail is reduced
by the presence of the lead droplet, and the reduction is higher at
closer S and lower We. For all breakup morphologies, the growth of
the cross-stream diameter is dominated by the flattening of the main
body. As discussed before, the shielding effect of the lead droplet
reduces the pressure at the front of the trailing droplet and, thus,
FIG. 19. Maximum cross-stream diameter of the trailing droplet at different
separation distances and Weber numbers, normalized by values of the lead
droplet.
FIG. 20. Mean drag coefficient of the trailing droplet at different separation
distances and Weber numbers, normalized by values of the lead droplet.
results in lower Dcmax,trail. The strength of the shielding effect dif-
fers from case to case. The lead droplet deforms into a flat disk
at low We (T = 1.0 in Fig. 5) and into an ellipsoid at high We
(T = 0.6 in Fig. 16). Ellipsoidal shapes induce weaker flow sepa-
ration in the wake than flat disks, and the corresponding shield-
ing is less effective. In addition, the cross-stream diameter of the
deformed lead droplet tends to be smaller at higher We, which fur-
ther alleviates the shielding effect on the trailing droplet. Conse-
quently, the reduction of Dcmax,trail is lowered as the Weber number
increases.
The variation of the mean drag coefficient of the trailing droplet
over the S–We map is shown in Fig. 20. For cases where the trailing
droplet fails to initiate the breakup independently, Cdmean,trail is cal-
culated by fitting into Eq. (5), the data prior to the collision with the
lead droplet. The change of Cdmean,trail with S and We follows similar
patterns to Dcmax,trail. Again, the shielding effect is stronger at smaller
S and lower We and accounts for the reduction of Cdmean,trail.
IV. SUMMARY AND CONCLUSION
The present work experimentally investigates the breakup of
two identically sized droplets in tandem formation. The breakup is
triggered by a planar shock wave and recorded by an ultra-high-
speed camera integrated into a shadowgraph system. The experi-
mental matrix consists of seven separation distances S ranging from
1.2 to 10.5 times of the droplet diameter and four Weber num-
bers We between 13 and 180 covering bag, bag-and-stamen, multi-
bag, and shear stripping breakup morphologies. The influences of
the tandem formation on the breakup behavior are summarized as
follows:
(a) The presence of the trailing droplet exerts marginal effects
on the lead droplet. The lead droplet replicates the breakup
morphology of isolated droplets in all cases, except for the
bag breakup at S = 1.2 where the tandem droplets coalesce
with no further bag formation.
(b) When the separation distance falls below critical levels, the
breakup intensity of the trailing droplet is consistently weak-
ened although the conventional breakup morphology is pre-
served. In the early stage, the tandem formation postpones
the time of initial deformation for the trailing droplet, low-
ers the maximum cross-stream diameter, and reduces the
mean drag coefficient. These effects are stronger at lower
Phys. Fluids 33, 012113 (2021); doi: 10.1063/5.0039098 33, 012113-10
Published under license by AIP Publishing
 29 August 2026 10:04:54

<!-- PDF_PAGE: 12 -->

Physics of Fluids ARTICLE scitation.org/journal/phf
Weber numbers and are intensified as the separation dis-
tance decreases. In the late stage, the bag structure is inflated
to a smaller size for bag and bag-and-stamen morpholo-
gies, and the fragments are less widely dispersed in the
cross-stream direction for multibag and shear stripping mor-
phologies. Notably, the critical separation distance is We-
dependent and halved from S= 10.8 at We= 13 to S= 5.4 at
We= 180.
(c) For cases where the tandem droplets are in very close proxim-
ity, the trailing droplet exhibits streamwise stretching instead
of flattening during the initial deformation and either punc-
tures or coalesces with the lead droplet in the later period.
To the best of our knowledge, the current study is the first
work that experimentally investigates tandem droplet breakup over a
wide range of Weber numbers and separation distances. The present
results can be particularly helpful for accurate modeling of frag-
ment sizes and breakup timings in applications related with dense
sprays.
ACKNOWLEDGMENTS
The authors acknowledge funding from the European Research
Council (ERC) under the European Union’s Horizon 2020 research
and innovation program (Grant Agreement No. 667483).
DATA AVAILABILITY
The data that support the findings of this study are openly
available in mediaTUM.
REFERENCES
1R. D. Reitz and R. Diwakar, “Effect of drop breakup on fuel sprays,” SAE
Tech. Pap. Ser. 1 95(3), 218–227 (1986), available at https://www.jstor.org/stable/
44725372.
2S. Lagutkin, L. Achelis, S. Sheikhaliev, V. Uhlenwinkel, and V. Srivastava,
“Atomization process for metal powder,” Mater. Sci. Eng. A 383(1), 1–6 (2004).
3J. Mostaghimi, M. Pasandideh-Fard, and S. Chandra, “Dynamics of splat forma-
tion in plasma spray coating process,” Plasma Chem. Plasma Process.22(1), 59–84
(2002).
4W. R. Lane, “Shatter of drops in streams of air,” Ind. Eng. Chem. 43(6),
1312–1317 (1951).
5J. O. Hinze, “Fundamentals of the hydrodynamic mechanism of splitting in
dispersion processes,” AIChE J. 1(3), 289–295 (1955).
6D. R. Guildenbecher, C. López-Rivera, and P. E. Sojka, “Secondary atomization,”
Exp. Fluids 46(3), 371–402 (2009).
7M. Pilch and C. A. Erdman, “Use of breakup time data and velocity history data
to predict the maximum size of stable fragments for acceleration-induced breakup
of a liquid drop,” Int. J. Multiphase Flow 13(6), 741–757 (1987).
8G. M. Faeth, L.-P. Hsiang, and P.-K. Wu, “Structure and breakup properties of
sprays,” Int. J. Multiphase Flow 21, 99–127 (1995).
9W.-H. Chou and G. M. Faeth, “Temporal properties of secondary drop breakup
in the bag breakup regime,” Int. J. Multiphase Flow 24(6), 889–912 (1998).
10D. D. Joseph, J. Belanger, and G. S. Beavers, “Breakup of a liquid drop sud-
denly exposed to a high-speed airstream,” Int. J. Multiphase Flow 25, 1263–1303
(1999).
11J. Han and G. Tryggvason, “Secondary breakup of axisymmetric liquid drops. I.
Acceleration by a constant body force,” Phys. Fluids 11(12), 3650–3667 (1999).
12A. A. Ranger and J. A. Nicholls, “Aerodynamic shattering of liquid drops,”
AIAA J. 7(2), 285–290 (1969).
13Z. Liu and R. D. Reitz, “An analysis of the distortion and breakup mechanisms
of high speed liquid drops,” Int. J. Multiphase Flow 23(4), 631–650 (1997).
14T. G. Theofanous and G. J. Li, “On the physics of aerobreakup,” Phys. Fluids
20(5), 052103 (2008).
15Z. Dai and G. M. Faeth, “Temporal properties of secondary drop breakup in the
multimode breakup regime,” Int. J. Multiphase Flow 27(2), 217–236 (2001).
16Y. Chen, E. P. DeMauro, J. L. Wagner, M. Arienti, D. R. Guildenbecher, P.
Farias, T. W. Grasser, P. Sanderson, S. Albert, A. Turpin, W. Sealy, and R. S.
Ketchum, “Aerodynamic breakup and secondary drop formation for a liquid
metal column in a shock-induced cross-flow,” in 55th AIAA Aerospace Sciences
Meeting (AIAA, 2017), p. 1892.
17L.-P. Hsiang and G. M. Faeth, “Near-limit drop deformation and secondary
breakup,” Int. J. Multiphase Flow 18(5), 635–652 (1992).
18T. G. Theofanous, G. J. Li, and T. N. Dinh, “Aerobreakup in rarefied supersonic
gas flows,” J. Fluids Eng. 126(4), 516 (2004).
19M. Jain, R. S. Prakash, G. Tomar, and R. V. Ravikrishna, “Secondary breakup of
a drop at moderate Weber numbers,” Proc. R. Soc. A471(2177), 20140930 (2015).
20N. Ashgriz, Handbook of Atomization and Sprays: Theory and Applications
(Springer Science & Business Media, 2011).
21G. J. Dorr, A. J. Hewitt, S. W. Adkins, J. Hanan, H. Zhang, and B. Noller, “A
comparison of initial spray characteristics produced by agricultural nozzles,” Crop
Prot. 53, 109–117 (2013).
22D. Y. Liu, K. Anders, and A. Frohn, “Drag coefficients of single droplets moving
in an infinite droplet chain on the axis of a tube,” Int. J. Multiphase Flow 14(2),
217–232 (1988).
23J. A. Mulholland, R. K. Srivastava, and J. O. L. Wendt, “Influence of droplet
spacing on drag coefficient in nonevaporating, monodisperse streams,” AIAA J.
26(10), 1231–1237 (1988).
24J. Y. Poo and N. Ashgriz, “Variation of drag coefficients in an interacting drop
stream,” Exp. Fluids 11(1), 1–8 (1991).
25S. Temkin and G. Z. Ecker, “Droplet pair interactions in a shock-wave flow
field,” J. Fluid Mech. 202, 467–497 (1989).
26Q. V. Nguyen and D. Dunn-Rankin, “Experiments examining drag in linear
droplet packets,” Exp. Fluids 12, 157–165 (1992).
27C. H. Chiang and W. A. Sirignano, “Axisymmetric calculations of three-droplet
interactions,” Atomization Sprays 3(1), 91–107 (1993).
28H. Zhao, Z. Wu, W. Li, J. Xu, and H. Liu, “Interaction of two drops in the bag
breakup regime by a continuous air jet,” Fuel 236, 843–850 (2019).
29D. Igra and K. Takayama, “Experimental investigation of two cylindrical water
columns subjected to planar shock wave loading,” J. Fluids Eng. 125(2), 325
(2003).
30S. Quan, J. Lou, and H. A. Stone, “Interactions between two deformable droplets
in tandem subjected to impulsive acceleration by surrounding flows,” J. Fluid
Mech. 684, 384–406 (2011).
31T. Kékesi, M. Altimira, G. Amberg, and L. Prahl Wittberg, “Interaction between
two deforming liquid drops in tandem and various off-axis arrangements subject
to uniform flow,” Int. J. Multiphase Flow 112, 193–218 (2019).
32D. Stefanitsis, I. Malgarinos, G. Strotos, N. Nikolopoulos, E. Kakaras, and
M. Gavaises, “Numerical investigation of the aerodynamic breakup of droplets in
tandem,” Int. J. Multiphase Flow 113, 289–303 (2019).
33Z. Wang, T. Hopfes, M. Giglmaier, and N. A. Adams, “Effect of Mach num-
ber on droplet aerobreakup in shear stripping regime,” Exp. Fluids 61(9), 1–17
(2020).
34J. Kim, J. K. Lee, and K. M. Lee, “Accurate image super-resolution using very
deep convolutional networks,” in 2016 IEEE Conference on Computer Vision and
Pattern Recognition (CVPR) (IEEE, 2016), pp. 1646–1654.
35H. Zhao, H.-F. Liu, W.-F. Li, and J.-L. Xu, “Morphological classification of low
viscosity drop bag breakup in a continuous air jet stream,” Phys. Fluids 22(11),
114103 (2010).
36F. W. Roos and W. W. Willmarth, “Some experimental results on sphere and
disk drag,” AIAA J. 9(2), 285–291 (1971).
37T. G. Theofanous, V. V. Mitkin, C. L. Ng, C.-H. Chang, X. Deng, and
S. Sushchikh, “The physics of aerobreakup. II. Viscous liquids,” Phys. Fluids24(2),
022104 (2012).
Phys. Fluids 33, 012113 (2021); doi: 10.1063/5.0039098 33, 012113-11
Published under license by AIP Publishing
 29 August 2026 10:04:54
