<!-- PDF_PAGE: 1 -->

Ignitability and mixing of underexpanded hydrogen jets
A.J. Ruggles* , I.W. Ekoto
Sandia National Laboratories, 7011 East Avenue, Bidg 905, Livermore, CA 94551-0969, USA
article info
Article history:
Received 15 December 2011
Received in revised form
24 February 2012
Accepted 12 March 2012
Available online 21 April 2012
Keywords:
Hydrogen
Choked
Notional nozzle
Ignition
Mach disc
Dispersion characteristics
abstract
Reliable methods are needed to predict ignition boundaries that result from compressed
hydrogen bulk storage leaks without complex modeling. To support the development of
these methods, a new high-pressure stagnation chamber has been integrated into Sandia
National Laboratories’ Turbulent Combustion Laboratory so that relevant compressed gas
release scenarios can be replicated. For the present study, a jet with a 10:1 pressure ratio
issuing from a small 0.75 mm radius nozzle has been examined. Jet exit shock structure
was imaged by Schlieren photography, while quantitative Planar Laser Rayleigh Scatter
imaging was used to measure instantaneous hydrogen mole fractions downstream of the
Mach disk. Measured concentration statistics and ignitable boundary predictions
compared favorably to analytic reconstructions of downstream jet dispersion behavior.
Model results were produced from subsonic jet dispersion models and by invoking self-
similarity jet scaling arguments with length scaling by experimentally measured effec-
tive source radii. Similar far ﬁeld reconstructions that relied on various notional nozzle
models to account for complex jet exit shock phenomena failed to satisfactorily predict the
experimental ﬁndings. These results indicate further notional nozzle reﬁnement is needed
to improve the prediction ﬁdelity. Moreover, further investigation is required to understand
the effect of different pressure ratios on measured virtual origins used in the jet dispersion
model.
Copyright ª 2012, Hydrogen Energy Publications, LLC. Published by Elsevier Ltd. All rights
reserved.
1. Introduction
Due to the rapid growth of hydrogen as an alternative fuel,
particularly within the material handling sector, signiﬁcant
infrastructure upgrades are needed to accommodate the
increased demand for transport to, storage of, and delivery
from compressed gas bulk container systems. A prerequisite
for large-scale infrastructure development is the imple-
mentation of science based safety codes and standards that
rely on effective quantitative risk analysis (QRA) tools [1].
Validated consequence models for planned and unintended
hydrogen release ignitable boundaries are a necessary QRA
requirement needed to establish suitable separation distances
and risk mitigation features. Research into natural gas
turbulent jet ignition has led to the development of the
ﬂammability factor (FF) concept, which is the integration of
the conditional mole fraction probability density function
(PDF) between the fuel ﬂammability limits, and has been
found to be an accurate predictor of ignition probability given
an ignition source [2e4]. The advantage of the FF is that it can
be easily modeled using mole fraction statistics that are
readily determined from application of well-known jet simi-
larity arguments [5e8], provided an appropriate jet intermit-
tency model is used [9,10]. Schefer et al. [11] veriﬁed the FF
concept is similarly applicable for hydrogen releases from un-
choked jets.
* Corresponding author .
E-mail address: ajruggl@sandia.gov (A.J. Ruggles).
Available online at www.sciencedirect.com
journal homepage: www.elsevier.com/locate/he
international journal of hydrogen energy 37 (2012) 17549 e17560
0360-3199/$ e see front matter Copyright ª 2012, Hydrogen Energy Publications, LLC. Published by Elsevier Ltd. All rights reserved.
doi:10.1016/j.ijhydene.2012.03.063

<!-- PDF_PAGE: 2 -->

For releases where the storage pressure is above the critical
ratio (w1.9 for hydrogen), however, the exit ﬂow chokes and an
underexpanded jet forms that is characterized by a complex
shock structure and a non-uniform velocity distribution. A
Mach disk, which serves as the boundary between the super-
sonic and subsonic portions of the jet, forms at the end of the
underexpanded jet. It is often several factors wider than the jet
exit diameter depending on the pressure ratio. Furthermore,
elevated near ﬁeld Mach numbers and entropy changes across
shocks may result in jet temperature deviations from ambient.
Notional nozzle (or pseudo source) models[5,12e15] have been
used to account for the jet exit shock structure by predicting
effective nozzle radii and thermodynamic state variables.
Downstream from the effective Mach disk, traditional subsonic
dispersion models have been employed to reconstruct the
mean and ﬂuctuating scalar ﬁelds. An example is Birch et al.
[13] where the dispersion model of Chen and Rodi[16] has been
modiﬁed to include a modeled term that represented the
effective nozzle radius, which was a function of the pressure
ratio. Ignition probabilities were then represented by FF values
computed from the reconstructed scalar statistics. The
concept of replacing the compressible shock structures with an
atmospheric pseudo source is also advantageous for CFD
modeling. Traditional RANS calculations struggle to reconcile
both compressible and incompressible ﬂows simultaneously.
Thus, the pseudo source model accounts for compressible jet
exit shock structures thereby establishing incompressible
boundary conditions for conventional RANS calculations [17].
Agreement between the various notional models, however, is
poor and limited validation data of necessary downstream
concentration statistics currently exists for general heteroge-
neous underexpanded jets, with none available for hydrogen.
For the present study, downstream concentration statistics
from an underexpanded hydrogen jet with a nominal 10:1
pressure ratio and 0.75 mm jet exit radius have been collected
using Planar Laser Raleigh Scatter (PLRS) imaging. Jet exit
shock structure was qualitatively imaged using schlieren
photography. These data allow a direct comparison of
observed jet behavior and ignition boundaries against
incompressible model predictions of dispersion statistics and
ignition probabilities with notional nozzle models used to
account for jet exit boundary conditions.
2. Experimental description
To create the desired underexpanded hydrogen jets, a new
high-pressure stagnation chamber capable of operating at
pressure ratios of up to 60:1 has been designed and integrated
within Sandia/CA’s Turbulent Combustion Laboratory burner
facility. The chamber, illustrated in Fig. 1, is 345 mm long and
B127 mm in diameter, with 12.7 mm thick walls and a 1.24 l
internal volume. To produce a uniform stagnation ﬂow ﬁeld,
fuel gas was fed from below through a six-hole injector with
B3 mm diameter holes evenly spaced around the circumfer-
ence and angled 45
/C14 downwards from the chamber center
axis. Easily interchangeable nozzles with machined proﬁles
were manufactured from blanks that were then securely
attached to a Swagelok one inch VCO ﬁtting (SS-16-VCO-1-16)
at the chamber outlet and sealed using its O-ring. Long Radius
nozzle proﬁles from ASME MFC-3M-2004 were selected over
a simple oriﬁce since they tend to produce fairly uniform (top-
hat) velocity proﬁles at the nozzle exit [18] and the pressure
ratios required to generate an underexpanded jet were lower
for a given exit diameter [19]. Chamber temperature and
pressure were respectively monitored via a type K thermo-
couple and TESCOM series 100 pressure transducer. Dynamic
feedback was used to maintain a steady pressure ratio. The
Nomenclature
b Hydrogen excluded volume constant,
7.6921 /C2 10/C0 3 m3/kg
BG(x,y) Image background scatter
EB(x,y) Electronic image bias
FF Flammability Factor
I(x,y) Corrected image intensity
KTS Kurtosis
LFL Lower ﬂammability limit
M Molar mass
n(x,y) Number of valid samples at each location
O
R(x,y) Image optical response
p Pressure, kPa
pF Laser power ﬂuctuation correction
r Nozzle radius, mm
R(x,y) Raw experimental image
RFL Upper ﬂammability limit
Ru Universal gas constant, 8314.5 J/kmole
S
B(x,y) Image scattering background
SKW Skewness
S
T( y) Laser sheet intensity distribution
T Temperature, K
Y Mass fraction
z0,j Momentum ﬂux virtual origin, mm
z0,Y Mass ﬂux virtual origin, mm
h Non-dimensional radial coordinate, ¼r/(z /C0 z0,j)
r Density, kg/m3
c Mole fraction
Sub and superscripts
0 Stagnation condition
a Atmospheric conditions
air Conditions for standard air
CL Centerline
eff Effective
H
2 Conditions for hydrogen
j Jet exit condition
mix Combined mixture conditions
ε Model density weighted condition
ε,ideal Experimental density weighted condition
Mean
0 Root-mean-square
international journal of hydrogen energy 37 (2012) 17549 e1756017550

<!-- PDF_PAGE: 3 -->

entire assembly was mounted onto a computer controlled
traverse capable of movement in three dimensions, while data
acquisition and system control were handled via a custom
written LabView virtual instrument (VI).
2.1. Jet conditions
For this work, a hydrogen jet with a 10:1 pressure ratio (stag-
nation to ambient pressure) was investigated using a nozzle
with a 0.75 mm radius. Stagnation density, r
0, was calculated
from the stagnation temperature, T0, pressure, p0, hydrogen
molar mass, MH2 , and universal gas constant, Ru, using the
Abel-Noble equation of state, where an excluded volume
constant, b, (7.6921 /C2 10
/C0 3 m3/kg [20]) was used to account for
real gas compressibility effects.
r0 ¼ p0
p0b þ T0
/C0
Ru=MH2
/C1 (1)
Modiﬁed isentropic relationships that incorporate the Abel-
Noble equation of state were used to determine static density,
temperature, choked ﬂow velocity, and mass ﬂow rate at the
nozzle exit [20]. The 0.979 discharge coefﬁcient was deter-
mined from the nozzle exit Reynolds number and relations
obtained from ASME MFC-3M-2004 [18] for the selected nozzle
proﬁle. Atmospheric laboratory pressure and temperature
were 98.37 kPa and 296 K, respectively. Mean conditions and
respective ﬂuctuations during data collection are summarized
in Table 1.
3. Shock structure characterization
3.1. Schlieren Imaging System
Jet exit shock structures were visualized by an in-line lens
based schlieren imaging system using three 50.8 mm
diameter lenses and a custom built light-emitting diode (LED)
light source with a ﬁxed 520 nm (green) wavelength so that
chromatic aberrations were removed. The LED was pulsed
with a custom built driver circuit to achieve pulse durations of
5 ms. The LED light was condensed to a point by an f1.2 NIKON
50 mm camera lens, while a diffuser and iris were mounted at
the focal point to create a point light source. The ﬁrst ﬁeld lens
(plano convex f ¼ 250 mm) was positioned at the focal length
to collimate the light. The second ﬁeld lens (plano convex
f ¼ 500 mm) then focused the light to a point at which a hori-
zontally orientated razor blade was positioned to control the
amount of light cutoff. Finally a third lens was used to focus
the light onto the imaging array of a Princeton Instruments
PIXIS 400B camera. A close up view was obtained through the
use of a plano convex lens of f ¼ 350 mm and a more global
view was acquired with a plano convex lens of f ¼ 150 mm.
Each recorded instantaneous image, R(x,y), was corrected
by subtraction of the electronic bias image, E
B(x,y), and back-
ground image (associated with the exposure time), BG(x,y). To
determine the schlieren system optical response, OR(x,y), 100
images were recorded with no nozzle ﬂow (pure air images).
Electronic bias and background scatter were corrected from
each image, the images were averaged together, and the mean
image was divided by the mean pixel value within the image
Fig. 1 e Left: sectional view of the stagnation chamber and nozzle assembly. Right: illustration of nozzle proﬁle and notional
nozzle concept.
Table 1 e Experimental conditions.
Stagnation chamber
mean (rms)
Nozzle exit
mean (rms)
Pressure (kPa) 983.2 (3)2.77 515.4 (1.4)
Temperature (K) 295.4 (0.4)0.41 244.8 (0.3)
Density (kg/m 3) 0.796 (0.003) 0.504 (0.002)
Velocity (m/s) 1202.7 (0.8)
Mass ﬂow rate (g/s) 1.0 (0.003)
international journal of hydrogen energy 37 (2012) 17549 e17560 17551

<!-- PDF_PAGE: 4 -->

ﬁeld of view. The ﬁnal corrected image, I(x,y), was obtained
after normalization by the optical response. The data reduc-
tion algorithm is expressed mathematically in Eq. (2) as:
Iðx; yÞ¼ Rðx; yÞ/C0 EBðx; yÞ/C0 BGðx; yÞ
ORðx; yÞ (2)
3.2. Results
Mean images derived from corrected Schlieren images are
shown in Fig. 2 . Typical underexpanded jet shock structures
are exhibited, including the barrel shock, Mach disk, outer
compression waves, and the diamond shaped reﬂected shock
structure downstream of the Mach disk. The measured Mach
disk diameter was 1.30 mm and was located 3.05 mm down-
stream from the nozzle exit.
For analytic predictions of jet dispersion behavior, the
effect of the complex shock structure was accounted for by
ﬁve separate notional nozzle models that calculated effective
source radii and jet exit density. All models were modiﬁed to
account for compressibility effects by incorporating an Abel-
Noble equation of state into the derivation as previously per-
formed by Schefer et al. [20] using the Birch et al. model [13].
Model complexity was impacted by the assumptions made,
with early models only accounting for mass conservation
[5,12], while later models successively incorporated
momentum conservation [13], energy conservation [14], and
the entropy change across the Mach disk [15]. Nonetheless,
the basis of these models is predicated on the assumption that
all issuing gas passes through the Mach disk, and no ambient
air entrainment occurs through the Mach disk. A more thor-
ough review of each model is given by Perret et al. [17].
Model results for the present operating condition are shown in
Table 2, and demonstrate a large spread in model predictions
with no clear agreement for either the effective source radius
or density.
To justify the use of Abel-Noble over the ideal gas law, the
pressure and density were calculated from both formulations
at three different isothermal conditions, and plotted in Fig. 3.
These values were further compared to curves generated
using the hydrogen state equation from Leachman [21] that is
based on a complex polynomial expression for the Helmholtz
free energy and validated over a broad range of temperatures
and pressures. For all models, the storage and ambient
temperatures were assumed to be atmospheric. A comparison
of the pressure edensity curves at 300 K illustrates that all
equation of state calculations were nearly equivalent until
w1.0 MPa. At higher pressures, Abel-Noble continued to agree
well with Leachman, but the ideal gas density was under-
predicted. For the ﬁrst four models in Table 2 [5,12 e14], the
lowest calculated temperature was immediately downstream
of the Mach disk, with the lowest temperature prediction
produced by the Yu ¨ ceil and O ¨ tu¨ gen model [14] at 170 K.
Isothermal pressure edensity curves in Fig. 3 at this temper-
ature indicate that relative to Leachman, Abel-Noble still
sufﬁciently captured compressibility effects across all pres-
sures. The model by Harstad and Bellan [15] was the most
physically realistic, and incorporated a prediction of the
thermodynamic state within the region upstream of the Mach
disk. Temperatures in this region were predicted to be cryo-
genic (i.e., w65 K) and, as indicated from the isothermal
pressureedensity curve in Fig. 3, both the ideal gas and Abel-
Noble equations of state deviated from Leachman at most
pressures. Nonetheless, Abel-Noble more faithfully matched
the general trends of Leachman, and thus was deemed more
appropriate for this pseudo source model. Since there was no
downside to the use of Abel-Noble with the simpler models, it
was incorporated into all models for consistency.
Fig. 2 e Left: mean image of the Mach disk structure. Right: mean image of the Mach disk and diamond shock structure.
Table 2 e Table of boundary conditions using various
notional nozzle models.
Model Effective nozzle
radius (mm)
Jet density
(kg/m3)
(1) Birch et al. (1984) 1.80 0.0805
(2) Ewan and Moodie (1986) 1.70 0.0971
(3) Yu¨ ceil and O¨ tu¨ gen (2002) 1.15 0.1391
(4) Birch et al. (1987) 1.50 0.0805
(5) Harstad and Bellan (2006) 2.70 0.0837
international journal of hydrogen energy 37 (2012) 17549 e1756017552

<!-- PDF_PAGE: 5 -->

The short pulse duration of the LED meant the instanta-
neous images captured ﬂow variations that otherwise would
have been smoothed out by a continuous wave light source
with a long camera exposure time (ms). Corrected instanta-
neous images were used to create a root-mean-square (rms)
image of these ﬂuctuations, which is shown in Fig. 4 and
illustrates the downstream mixing layers. It should be noted
that the Schlieren image results should be interpreted with
caution. The measurement itself is a path averaged integra-
tion of the refractive index gradient, which may have been
caused by differences in mixture fraction due to scalar mixing,
but also may have been the result of changes in pressure and
temperature. In the region surrounding the barrel shock
structure, however; it is feasible that refractive index gradi-
ents were the result of the air entrainment ahead of the Mach
disk, implying hydrogen and air were mixing outside of the
shock structures and that not all of the hydrogen passed
through the Mach disk. This would then require the inclusion
of an entrainment/shock bypass correction in the current
notional nozzle models.
4. Scalar ﬁeld measurements
4.1. Planar Laser Rayleigh Scattering (PLRS) system
Since elastically scattered light is linearly proportional to the
scattering cross section of the gas in question [8,22e24], Planar
Laser Rayleigh Scatter (PLRS) imaging was used to measure
instantaneous mole fractions within the isothermal portion of
the jet far ﬁeld. Thermocouple measurements were used to
ﬁnd the location where the mean centerline jet temperature
returned to within 1
/C14 C of room temperature. This point was
approximately 80 mm downstream of the nozzle exit and
marks the upstream limit for the Rayleigh measurements. At
each position, 400 images were recorded. A beam from
a Nd:YAG laser (9 ns pulse duration 1 J/pulse) operating at
532 nm was formed into an approximately 40 mm high laser
sheet using a cylindrical plano-concave ( f ¼/C0 200 mm) and
spherical plano convex ( f ¼ 1000 mm) lens pair. Five imaging
areas were sampled, starting at the 80 mm downstream
location, with successive areas imaged by traversing the
chamber downwards in 40 mm increments. To reduce
unwanted scatter, the laser and sheet forming optics were
encased within a light tight enclosure that terminated close to
the experimental apparatus. Once the laser sheet had passed
through the test section, the light was directed into a second,
narrow, enclosure with a built-in beam dump to minimize
back scatter. A Princeton Instruments PIXIS 400B camera was
mounted perpendicular to the laser sheet and used an f1.2
NIKON 50 mm lens with a NIKON 3T close up lens to collect
the Rayleigh scattered light. To improve signal-to-noise, 2 /C2 2
on chip binning and 3 /C2 3 Gaussian smoothing was used. The
system was calibrated by imaging two pure gases; air and
helium. From 800 image ensemble averages of these data the
scattering background, S
B(x,y), camera optical response,
OR(x,y), and camera pixel intensity I(x,y) of pure air, helium,
and hydrogen were all determined.
Once the raw experimental images, R(x,y), were collected,
each image was subjected to a dust ﬁlter algorithm that
automatically detected and masked imaged Mie scatter from
Fig. 3 e Left: isothermal calculations at 300 K. Center: isothermal calculations at 170 K. Right: isothermal calculations at 65 K.
Fig. 4 e Rms image of the Mach disk and diamond
structure.
international journal of hydrogen energy 37 (2012) 17549 e17560 17553

<!-- PDF_PAGE: 6 -->

dust particles. Electronic bias, EB(x,y), and background scatter,
BG(x,y), were then subtracted. Laser power ﬂuctuations were
corrected for by multiplying the entire image by a correction
parameter, pF, which was determined by integrating the ﬁrst
50 columns on the image right-hand-side where only pure air
was sampled and then normalizing by the corresponding
integrated mean from the reference air calibration image. The
resultant image was divided by the optical response image
and the scattering background image was then subtracted.
Finally the image was corrected for by the laser sheet intensity
distribution vector, St( y), created by sampling the same 50
columns used to obtain the power ﬂuctuation correction and
integrating each row. The equation for corrected signal
intensity at each pixel is then as follows:
Iðx; yÞ¼
1
StðyÞ$
/C20/C18Rðx; yÞ/C0 EBðx; yÞ/C0 BG ðx; yÞ
pF $ORðx; yÞ
/C19
/C0 SBðx; yÞ
/C21
(3)
Once corrected, the image intensity was converted to mole
fraction, cH2 ðx; yÞ, using Eq. (4) and the previously recorded
calibration intensity values. A thorough signal-to-noise (SNR)
analysis through the measurement range reveals a conserva-
tive instantaneous measurement uncertainty of /C6 0.6% (mole
fraction) for a 95.4% conﬁdence interval (2 s).
c
H2 ðx; yÞ¼ IAIRðx; yÞ/C0 Iðx; yÞ
IAIRðx; yÞ/C0 IH2 ðx; yÞ (4)
Concentration data is typically expressed in terms of mass
fraction statistics, which inherently account for momentum
differences due to density effects [8] and allow comparisons
with other gases. Thus, a conversion from mole to mass
fractions for the statistical quantities of interest was required.
Previous researchers have used mathematical relations that
were based on estimations for higher order moments to
convert the mean and rms mole fraction measurements [7,8]
into mass fraction statistics. For the present investigation,
however, each instantaneous mole fraction measurement
was converted to mass fraction, Y
H2 ðx; yÞ, using the molar
masses of air Mair and hydrogen MH2 and calculating the
mixture molecular weight Mmix(x, y).
YH2 ðx; yÞ¼ cH2 ðx; yÞ$MH2
MMixðx; yÞ (5)
Mmixðx; yÞ¼
X
ci ðx; yÞ$Mi (6)
Examples of the original raw image, along with the mole
and mass fraction images after all corrections from Eqs. (3)e(6)
Fig. 5 e Top: raw intensity image R(x, y). Middle: corrected mole fraction image cH2 ðx; yÞ. Bottom: converted mass fraction
image YH2 ðx; yÞ.
international journal of hydrogen energy 37 (2012) 17549 e1756017554

<!-- PDF_PAGE: 7 -->

were applied are shown in Fig. 5. From the processed images,
ensemble averaged mean and rms mass fraction turbulent
statistics were computed for each section. Complete recon-
struction of turbulent data from each sectional interrogation
region was then performed.
4.2. Statistical uncertainties
Previous optical investigations of atmospheric jet behavior
utilizing Raman or Rayleigh scattering techniques to measure
the instantaneous mole fraction at singular points in space
made use of continuous wave lasers where very large sample
sizes were obtained at each position ( >35,000). No effort was
made to quantify the statistical uncertainties, and it was
assumed that with such large sample sizes that statistical
convergence occurred. Sample sizes of this size are unrea-
sonable when using two-dimensional imaging; therefore, the
uncertainty must be quantiﬁed. Although the mean and rms
statistics are sufﬁcient to describe the probability distribution
function (PDF) for normally distributed variables, the distri-
bution function within turbulent free jets is generally highly
non-Gaussian. Thus, the statistical variance is not sufﬁcient
by itself to determine the statistical or measurement uncer-
tainties. Instead, statistical uncertainties were quantiﬁed
using the jackknife re-sampling technique [25,26]. For
a sample size of N, each statistic is calculated N-times by
omitting one instantaneous sample and a PDF of values for the
desired statistic is formed. The standard deviation of this PDF
is then multiplied by 2 to give a 95.4% conﬁdence interval. In
addition to providing an estimate of the statistical uncer-
tainty, the mean of the jackknife PDF also provides a more
converged statistic.
4.3. Results
To ascertain if the subsonic portion of the jet can accurately be
described by conventional incompressible dispersion models,
the jet was analyzed to determine if it obeys jet self-similarity.
Images of the mean and rms mass fraction ﬁelds are displayed
in Fig. 6 , and illustrate the nearly seamless sectional
reconstruction.
The inverse mass fraction proﬁle along the centerline
(Fig. 7) conﬁrmed the linear decay rates observed by Xiao et al.
[27] and was consistent with measurements from un-choked
free jets [5e8,11]. The mass ﬂux based virtual origin, z
0,Y,o r
the point where the initial downstream distance of the linear
inverse decay rate intercepts the axis, was found to be
24.74 mm. The jet half-width proﬁle, derived from the mass
fraction data and also shown in Fig. 7 , was similarly a linear
function of axial distance. The gradient of the best ﬁt line
(when plotted against axial distance) was 0.111, which is in
excellent agreement with other reported values [22], although
slightly larger than that reported for the hydrogen study
(0.103) of Schefer et al. [23]. The momentum ﬂux virtual origin,
Fig. 6 e Left: mean jackknife mass fraction image. Right: rms jackknife mass fraction image.
80 130 180 230 280 330
10
20
30
40
50
z/r
80 130 180 230 280 330
6
10
14
18
22
26
z/r
Jet Half Width (mm)
80 130 180 230 280 330
0
0.05
0.1
0.15
0.2
0.25
z/r
Unmixedness
Fig. 7 e Left: reciprocal mean mass fraction along the centerline with jackknife uncertainties. Center: jet half-widths against
normalized axial distance. Right: centerline unmixedness.
international journal of hydrogen energy 37 (2012) 17549 e17560 17555

<!-- PDF_PAGE: 8 -->

z0,j, or the location where the jet half-width becomes zero was
found to be 7.14 mm downstream of the nozzle exit. Both
virtual origins are summarized in Table 3.
It is important to note that reported virtual origins in the
present work were derived using only the subsonic concen-
tration statistics, and thus do not explicitly account for the
existence of downstream reﬂected shock structures that
likely alter downstream centerline decay rates in the region
just beyond the Mach disk. The behavior of both virtual
origins has been observed in previous investigations
[22,28e30], and general trends have been identiﬁed. For
example, the momentum ﬂux virtual origin, z
0,j, was found to
have a Reynolds number dependence, with higher Reynolds
numbers resulting in downstream movement of the origin as
observed by Richards and Pitts [22]. The mass ﬂux virtual
origin, z
0,Y, likewise moved downstream as Reynolds
numbers increased [22,29]. However, this origin also depen-
ded on the jet exit gas density, with increased values
resulting in upstream movement [22,28,30]. To the best of the
authors’ knowledge, no suitable model has been proposed
that predicts the position of either origin. Since the under-
expanded jets had both elevated density and Reynolds
number relative to un-choked releases, the origin z
0,j was
expected to move downstream. The second origin is not as
straightforward since there was competition between the
increased jet exit density and higher Reynolds numbers.
Although the results in Table 3 indicate both virtual origins
extend several jet diameters downstream from the nozzle
exit, the contribution from the downstream shock structure
on the virtual origin position is unknown. It should be noted
that the portion of the shear layer immediately downstream
of the barrel shock was likely highly compressible, which
inﬂuences air entrainment behavior, and hence centerline
decay rates in the near ﬁeld [31].
Fig. 7 also displays a proﬁle of centerline unmixedness,
which is deﬁned as the ratio of rms to mean mass fraction,
and has been shown to converge to a steady asymptotic value
between 0.21 and 0.24 for self-preserving jets [22,28,30]. The
measured value, 0.222 /C6 0.009, was in good agreement with
these studies and further supports the assertion that down-
stream of the nozzle exit shock structure the jet is self-
similar.
5. Jet reconstruction
Richards and Pitts [22] have demonstrated that atmospheric
jet dispersion behavior for a variety of gases (methane,
propane and helium) can be described by the following
equations for the mean and rms ﬁelds respectively:
Yðz; hÞ¼ 9:52rε
z /C0 z0;Y
exp
/C0
/C0 59h2/C1
(7)
Y0 ðz; hÞ ¼ 9:52rε
z /C0 z0;Y
/C2
0:23 þ 0:35h þ 9:09h2 /C0 116:48h3 þ 240:81h4/C3
(8)
where h ¼ r/(z /C0 z0,j) was a non-dimensional radial coordinate
and rε ¼ r0/(rj/ra)1/2 was a weighted nozzle radius used to
account for density changes between the jet at the nozzle exit
and the ambient gas (both at atmospheric pressure). Here, r
0
was the jet exit radius. A universal jet decay constant, K (1/
K ¼ 0.105 when evaluating for inverse mass fraction) was used
in both expressions. In addition to the present study, other
researchers have found a small spread in the reported
constant values among the different gases [5e8,11]. Therefore,
it is common to use either a gas speciﬁc value reported from
literature or the generalized one proposed by Richards and
Pitts.
For the remainder of this work the above expressions will
be used and compared with the collected data to judge their
suitability. Schefer et al. [23], found for an un-choked, high-
momentum hydrogen jet that the inverse mean centerline
decay constant was nearly equivalent to those of other gases
(0.104). For the present work, however, the decay constant
could not be independently determined as r
ε depended on an
unknown effective jet exit diameter and density. Instead, r0
and rj were replaced with the effective nozzle radius, reff,
and jet nozzle exit density, reff, derived from the notional
nozzle models described in Section 3.2 and tabulated in
Table 2 . The suitability of the values from each model was
determined by computing the gradient of reciprocal mass
fraction against axial distance. Eq. (7) was evaluated at the
centerline ( h ¼ 0), the generalized K value given by Richards
and Pitts was assumed and r
ε,ideal (i.e., the measured rε value)
was calculated from a linear ﬁt to the measured 1 =YCL values
from Fig. 7 . Different values from the notional nozzle model
predictions of effective radius and jet exit density are
summarized in Table 4 along with a comparison of the
deviation from r
ε,ideal. Although most modeled values were
within /C6 10%, the differences in all cases were non-
negligible.
Measured mean and rms mass fractions radials are plotted
as a function of h in Fig. 8 . Since normalized mean and rms
data each collapse to single curves, it was concluded that the
jet was self-similar downstream of the Mach disk, and mass
fraction statistics can be accurately described by incom-
pressible dispersion models. The curve from Eq. (7) was
Table 3 e Summary of the mass and momentum ﬂux
virtual origins.
Virtual origin Length
z0,Y/r 32.0
z0,j/r 9.52
Table 4 e Table of density weighted nozzle radii ( rε).
Target value rε,ideal [ 0.438 mm.
Model rε (mm) rε/rε,ideal
(1) Birch et al. (1984) 0.475 1.084
(2) Ewan and Moodie (1986) 0.492 1.123
(3) Yu¨ ceil and O¨ tu¨ gen (2002) 0.399 0.911
(4) Birch et al. (1987) 0.396 0.904
(5) Harstad and Bellan (2006) 0.726 1.658
international journal of hydrogen energy 37 (2012) 17549 e1756017556

<!-- PDF_PAGE: 9 -->

overlaid on the data and compared with a best ﬁt curve to the
exponential constant in Eq. (7) (C ¼/C0 57.7). The differences
between the two ﬁtted curves were so slight that the original
formulation was assumed to hold without any loss of
prediction ﬁdelity. It should be noted that both curves slightly
overestimated
Y at the tail region beyond h ¼ 0.2.
The rms ﬁeld was similarly reconstructed using Eq. (8), and
plotted in Fig. 8 as a function of h. A best ﬁt radial curve to the
measured data was matched to a fourth order polynomial and
was also overlaid for comparison; the curve ﬁt is displayed in
Eq. (9).
Y
0ðz; hÞ¼ 9:52rε
z /C0 z0;Y
/C2
0:218 þ 0:541h þ 4:570h2 /C0 86:388h3
þ 192:51h4/C3
ð9Þ
The difference between the two curves was more substan-
tial than for the mean mass fraction curve ﬁts. The impact of
the difference on ignitability predictions will be discussed
further in the next section.
Higher order skewness and kurtosis statistics (corrected for
sample size bias), which describe the general PDF shape, are
plotted for all radials against h in Fig. 9.
SKW ¼
ﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ
nðn /C0 1Þ
p
n /C0 2 s where s ¼
1
n
Xn
i¼1
ðxi /C0 xÞ3
 ﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ
1
n
Xn
i¼1
ðxi /C0 xÞ2
s !3 (10)
KTS ¼ n /C0 1
ðn /C0 2Þðn /C0 3Þ ððn þ 1Þk /C0 3ðn /C0 1ÞÞ þ 3
where k ¼
1
n
Xn
i¼1
ðxi /C0 xÞ4
 
1
n
Xn
i/C0 1
ðxi /C0 xÞ2
!2 (11)
Skewness was marginally negative on the centerline and
initially increased gently before rapidly rising towards the
jet edge. The kurtosis is approximately equal to 3 on the
Fig. 8 e Left: plot of normalized radial mass concentration including the corresponding best ﬁt curve and Eq. (5) [22] . Right:
plot of normalized rms radial data including the corresponding best ﬁt curve and Eq. (6) [22] .
Fig. 9 e Left: plot of collapsed skewness values including the corresponding best ﬁt curve. Right: plot of collapsed kurtosis
values including the corresponding best ﬁt curve.
international journal of hydrogen energy 37 (2012) 17549 e17560 17557

<!-- PDF_PAGE: 10 -->

centerline. A small decrease is observed moving through
the jet until a drastic increase at the jet boundary. These
observations are consistent with both Birch [7] and Pitts [8],
which further reinforces the assertion that the downstream
incompressible ﬂow region can be represented by atmo-
spheric jet arguments. Curve ﬁts for these two statistics
are:
SKWðhÞ¼/C0 0:0879 /C0 10:42h þ 357:4h
2 /C0 5725h3 þ 6:692 /C2 104h4
/C0 4:540 /C2 105h5 þ 1:540 /C2 106h6 /C0 1:945 /C2 106h7
(12)
KTSðhÞ¼ 3:109 /C0 15:53h þ 766:7h2 /C0 2:263 /C2 104h3 þ 2:838
/C2 105h4 /C0 1:541 /C2 106h5 þ 3:061 /C2 106h6 (13)
Uncertainty estimates from the jackknife re-sampling
technique of all four statistics indicated that the uncertainty
was collapsible. The mean and rms uncertainties when
normalized by the respective statistic and plotted against h
collapsed to a common curve implying that the normalized
uncertainties are independent of axial distance. Normalized
uncertainty and its variation increased with radial distance as
the variance of the PDF increased and the bimodal nature of
the PDF became dominant. The uncertainties of skewness and
kurtosis when plotted against h exhibited a reasonable
collapse, once again indicating axial distance independence.
As previously observed the uncertainty and variation of
uncertainty both increase with radial distance rather
dramatically for the higher order statistics. For all four
statistics the values of the collapsed data can be improved by
increasing the sample size.
6. Ignition probabilities
To estimate ignition probabilities, the validated Flammability
Factor concept (FF) was utilized [2,11], which is expressed in
Eq. (15). Here c
H2 ðx; yÞ corresponds to a fully corrected
instantaneous mole fraction image (see Fig. 5 ) and n(x, y) the
number of valid samples at each pixel. For hydrogen, the
lower and upper ﬂammability limits used were 0.04 and 0.75
respectively.
FFðx; yÞ¼
X
0
@
Z
RFL
LFL
cH2 ðx; yÞ¼ 1
1
A /C2
1
nðx; yÞ (14)
Fig. 10 shows the calculated FF and the corresponding
jackknife uncertainties. The rms image of Fig. 10 shows
a maximum rms value of 0.025 in ignition probability either
side of the centerline corresponding to the 0.5 FF contours.
These regions experience the largest mole fraction variation
in and out of the ﬂammable range. On the jet centerline and at
large radial extents, the rms image shows low variation as the
variation of mole fraction is consistently between or below the
ﬂammable limits respectively.
In Fig. 11 , measured FF contours, acquired from direct
application of Eq. (14) to the collected instantaneous mole
fraction measurements, were compared with those derived
from the reconstructed mean and rms statistics derived from
Eqs. (7) and (9) and the intermittency model described by [10].
Although the comparison was very good for all of the
contours, better agreement was obtained for higher FF values
(i.e., 0.9) closer to the centerline, which was attributed to the
slight overestimation of the mean mass fractions at large
radial distances ( Fig. 8).
To demonstrate the utility of this approach a 10% ignit-
ability contour was predicted in the far ﬁeld with the respec-
tive effective radius and density from each notional nozzle
model along with Eqs. (7) and (8) to model dispersion char-
acteristics. Additionally, this contour was created using the
ideal r
ε,ideal values obtained from Eqs. (7) and (8) (‘Ideal (2)’) or
Eqs. (7) and (9) (‘Ideal’) to highlight the impact of the different
coefﬁcients for the fourth order polynomial. All ignitability
contours are compared in Fig. 11. The maximum axial extent
for both the Ideal and Ideal (2) 10% FF contours was 1888 mm
and 1911 mm respectively; thus the impact of selecting Eq. (8)
or (9) to model mass fraction rms values appears to be negli-
gible. Predictions of the maximum FF axial extent by the
Yu¨ ceil and O¨ tu¨ gen [14] and Birch et al. [13] models under-
estimated the contour location by around 200 mm relative to
the Ideal conditions, while the Birch et al. [5] and Ewan and
Moodie [12] model predictions overestimated the location by
a similar spread. Although the Hardstad and Bellan model [15]
has the most realistic physical basis, it vastly overestimated
the 10% FF contour by more than a meter. It should be recalled
Fig. 10 e Left: FF jackknife image. Right: rms FF jackknife image.
international journal of hydrogen energy 37 (2012) 17549 e1756017558

<!-- PDF_PAGE: 11 -->

that the incorporated Abel-Noble equation of state was not
capable of capturing real gas effects in the cryogenic regime
upstream of the Mach disk, as shown in Fig. 3 , which ulti-
mately impacted the prediction of effective Mach disk velocity
and diameter. Furthermore, this model was likely overly
sensitive to the assumption that all hydrogen passed through
the Mach disk while neglecting entrained air in the adjacent
slip region. This assumption, however, seems to be contra-
dicted by the rms Schlieren image in Fig. 2 . The predicted
percentage differences in FF contour distance were propor-
tional to the differences in r
ε values reported in Table 4.
It should be cautioned that these contours only correspond
to the 10% probability that an ignition kernel will form.
Determination of whether the ignition kernel will transition to
sustained jet light-up or will be subsequently extinguished,
however, is beyond current predictive capabilities of simpli-
ﬁed engineering models. Swain et al. [32] and Schefer et al. [11]
observed centerline ﬂame light-up boundaries near the 10%
mole fraction contour; however, no explanation was given for
why it occurred in this region and it is possible that the
agreement was serendipitous. For the present study, the
centerline jet light-up position was determined using a similar
laser spark ignition apparatus to that described by Schefer
et al. [11]. Sparks were formed on the chamber centerline
using the second harmonic of an Nd:YAG laser operating at
10 Hz with 100 mJ/pulse. The chamber was slowly traversed
upwards until a sustained ﬂame was achieved. The test was
repeated 10 times to ensure consistency. The average height
above the nozzle where sustained combustion occurred was
found to be 367 mm, which roughly correlates with the 15%
mean mole fraction contour. This result demonstrates that
neither the FF nor the mean concentration alone is sufﬁcient
to predict the downstream light-up location.
7. Conclusions and future work
To support the development of reliable ignition boundary
prediction methods for releases from compressed hydrogen
bulk storage releases, a new high-pressure stagnation
chamber has been designed and integrated into Sandia
National Laboratories’ Turbulent Combustion Laboratory. For
the present study, a hydrogen jet with a 10:1 pressure ratio
that issued from a 0.75 mm radius nozzle was examined using
a combination of shock imaging via Schlieren photography
and quantitative downstream concentration measurements
by Planar Laser Rayleigh Scatter imaging. The present results
demonstrate that once an underexpanded jet has returned to
subsonic ﬂow conditions downstream of the release, the
scalar ﬁeld follows canonical jet similarity laws and can
accurately be described by empirical jet dispersion relations
provided an appropriate effective source nozzle radius and
density is used. Mean mass fraction statistics agreed very well
with reported subsonic values in the literature, while the rms
mass fraction ﬁeld exhibited small deviations. More work is
needed to ascertain if these coefﬁcients signiﬁcantly change
with different pressure ratios, jet diameters or gas types.
Good agreement was observed between experimental and
reconstructed ignition probability boundaries regardless of
the correlation used to predict ﬂuctuating statistics, so long as
the density weighted effective radius derived from concen-
tration decay measurements was used. Pseudo source models
based on different combinations of mass, momentum, and
energy conservation were combined with the Abel-Noble
equation of state and used to predict density weighted effec-
tive radii; however, the results were off by /C6 10% relative to
measured values. A more physically realistic source model
proposed by Harstad and Bellan overestimated the density
weighted effective radius by more than 60%, which suggests
certain physical processes such as the thermodynamics
before the shock were poorly reconstructed. An rms image
produced from a sequence of Schlieren images also indicated
entrained air and issuing hydrogen may have mixed within
the slip region and bypassed the Mach disk. Further experi-
mental and computational research is needed to conﬁrm this.
If found to be true the effect of the slip region upon the
predictions of notional nozzle boundary conditions (such as
diameter) using pseudo source models needs to be assessed
Fig. 11 e Left: comparison of experimental (black) and reconstructed (red) FF contours. Right: comparison of the 10% (0.1) FF
based on notional nozzle models predictions for rε (Table 4), along with experimentally determined values of rε,ideal and rms
mass fractions predicted using either Eq. (8) (Ideal (2)) or Eq. (9) (Ideal).
international journal of hydrogen energy 37 (2012) 17549 e17560 17559

<!-- PDF_PAGE: 12 -->

and ultimately accounted for. Since the error in ignition
probability boundaries was proportional to the error in density
weighted effective radii, better source model performance is
needed to improve the agreement between predictions and
measurements. The present results also demonstrate that
non-negligible downstream movement of the mass and
momentum ﬂux based virtual origins has occurred, and these
values likewise must be accounted for.
Future models with improved thermodynamics e incor-
porating a better performing equation of state where needed,
near ﬁeld jet entrainment, and a more comprehensive
account of downstream reﬂected shock structures are under
development, and will be validated against data generated
from different conditions at higher pressure ratios and
different nozzle radii. Furthermore, methane will be investi-
gated to ascertain model applicability for other ﬂammable
gases. Ultimately it should be noted that the present models
are applicable only for ignition probability and further
research is needed to develop the scientiﬁc underpinnings for
engineering models that can accurately predict the transition
to sustained ﬂame light-up.
references
[1] LaChance J, Tchouvelev A, Ohi J. Risk-informed process and
tools for permitting hydrogen fueling stations. Int J Hydrogen
Energy 2009;34:5855 e61.
[2] Birch AD, Brown DR, Dodson MG. Ignition probabilities in
turbulent mixing ﬂows. In: Proceedings of 18th international
symposium on combustion. The Combustion Institute; 1981.
p. 1775e 80.
[3] Birch AD, Brown DR, Cook DK, Hargrave GK. Flame stability
in underexpanded natural-gas jets. Combust Sci Technol
1988;58:267e80.
[4] Birch AD, Brown DR, DM G, Thomas JR. Studies of
ﬂammability in turbulent ﬂows using laser Raman
spectroscopy. In: Proceedings of 17th international
symposium on combustion. The Combustion Institute; 1979.
p. 307 e14.
[5] Birch AD, Brown DR, Dodson MG, Swafﬁeld F. The structure
and concentration decay of high-pressure jets of natural-gas.
Combust Sci Technol 1984;36:249 e61.
[6] Becker HA, Hottel HC, Williams GC. Nozzle-ﬂuid
concentration ﬁeld of the round turbulent free jet. J Fluid
Mech 1967;30:285 e303.
[7] Birch AD, Brown DR, Dodson MG, Thomas JR. Turbulent
concentration ﬁeld of a methane jet. J Fluid Mech 1978;88:
431e49.
[8] Pitts WM, Kashiwagi T. The application of laser-induced
Rayleigh light-scattering to the study of turbulent mixing.
J Fluid Mech 1984;141:391 e429.
[9] Effelsberg E, Peters N. A composite model for the conserved
scalar Pdf. Combust Flame 1983;50:351 e60.
[10] Cho JR, Chung MK. A Kappa eEpsiloneGamma equation
turbulence model. J Fluid Mech 1992;237:301 e22.
[11] Schefer RW, Evans GH, Zhang J, Ruggles AJ, Greif R.
Ignitability limits for combustion of unintended hydrogen
releases: Experimental and theoretical results. Int J Hydrogen
Energy 2011;36:2426 e35.
[12] Ewan BCR, Moodie K. Structure and velocity-measurements
in underexpanded jets. Combust Sci Technol 1986;45:275 e88.
[13] Birch AD, Hughes DJ, Swafﬁeld F. Velocity decay of high-
pressure jets. Combust Sci Technol 1987;52:161 e71.
[14] Yuceil KB, Otugen MV. Scaling parameters for underexpanded
supersonic jets. Phys Fluids 2002;14:4206 e15.
[15] Harstad K, Bellan J. Global analysis and parametric
dependencies for potential unintended hydrogen-fuel
releases. Combust Flame 2006;144:89 e102.
[16] Chen CJ, Rodi W. Vertical turbulent bouynant jets e a review
of experimental data, The science and applications of heat
and mass transfer. Pergamon Press; 1980.
[17] Perret C, Chaudourne S, Pitre C. Simulation of accidental
hydrogen releases in a refuelling station. HyApproval 04-
01449. CEA; 2007.
[18] Measurement of ﬂuid ﬂow in pipes using oriﬁce nozzle and
venturi. ASME; 2004. MFC-3M.
[19] Addy AL. Effects of axisymmetric sonic nozzle geometry on
Mach disk characteristics. AIAA Journal e Technical Notes
1981;19:121e2.
[20] Schefer RW, Houf WG, Williams TC, Bourne B, Colton J.
Characterization of high-pressure, underexpanded
hydrogen-jet ﬂames. Int J Hydrogen Energy 2007;32:2081 e93.
[21] Leachman JW, Jacobsen RT, Penoncello SG, Lemmon EW.
Fundamental equations of state for parahydrogen, normal
hydrogen, and orthohydrogen. J Phys Chem Ref Data 2009;38:
721e48.
[22] Richards CD, Pitts WM. Global density effects on the self-
preservation behavior of turbulent free jets. J Fluid Mech
1993;254:417e35.
[23] Schefer RW, Houf WG, Williams TC. Investigation of small-
scale unintended releases of hydrogen: momentum-
dominated regime. Int J Hydrogen Energy 2008;33:6373 e84.
[2
4] Schefer RW, Houf WG, Williams TC. Investigation of small-
scale unintended releases of hydrogen: buoyancy effects. Int
J Hydrogen Energy 2008;33:4702 e12.
[25] Tukey JW. Bias and conﬁdence in not-quite large samples.
Ann Math Stat 1958;29:614.
[26] Benedict LH, Gould RD. Towards better uncertainty estimates
for turbulence statistics. Exp Fluids 1996;22:129 e36.
[27] Xiao J, Travis JR, Breitung W. Hydrogen release from a high
pressure gaseous hydrogen reservoir in case of a small leak.
Int J Hydrogen Energy 2011;36:2545 e54.
[28] Pitts WM. Effects of global density ratio on the centerline
mixing behavior of axisymmetrical turbulent jets. Exp Fluids
1991;11:125e34.
[29] Pitts WM. Reynolds-number effects on the mixing behavior
of axisymmetrical turbulent jets. Exp Fluids 1991;11:135 e41.
[30] Schefer RW, Dibble RW. Mixture fraction measurements in
a turbulent nonreacting propane jet. AIAA; 1986. AIAA Paper
86-0278.
[31] Papamoschou D, Roshko A. The compressible turbulent
shear-layer e an experimental-study. J Fluid Mech 1988;197:
453e77.
[32] Swain MR, Filoso PA, Swain MN. An experimental
investigation into the ignition of leaking hydrogen. Int J
Hydrogen Energy 2007;32:287 e95.
international journal of hydrogen energy 37 (2012) 17549 e1756017560
