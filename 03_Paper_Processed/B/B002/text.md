<!-- PDF_PAGE: 1 -->

Evaluation of notional nozzle approaches for CFD simulations
of free-shear under-expanded hydrogen jets
E. Papanikolaou a, D. Baraldi a,*, M. Kuznetsov b, A. Venetsanos c
a European Commission DG-JRC, Institute for Energy e Cleaner Energy Unit, P.O. Box 2, 1755 ZG Petten, The Netherlands
b Karlsruhe Institute for Technology, Campus Nord (KIT-CN), Institute for Nuclear and Energy Technologies, Hermann-von-Helmholtz-Platz 1,
76344 Eggenstein-Leopoldshafen, Germany
c National Centre for Scientiﬁc Research Demokritos (NCSRD), Environmental Research Laboratory, 15310 Aghia Paraskevi, Attikis, Greece
article info
Article history:
Received 23 May 2012
Received in revised form
5 September 2012
Accepted 23 September 2012
Available online 15 October 2012
Keywords:
Hydrogen
Notional nozzle
Under-expanded jet
CFD
abstract
Several approaches are usually applied for modelling the source of high pressure under-
expanded jets, ranging from the computationally expensive resolution of the jet’s shock
structure to simple formulae (pseudo-source or notional nozzle approaches). However, the
assumptions made in each approach introduce inaccuracies in the CFD calculations. The
objective of this work was twofold; to compare and evaluate the performance of both
selected notional nozzle approaches and turbulence models with experimental results of
free-shear high momentum H
2 round jets. The experimental data covered horizontal H 2
releases issuing from small nozzles (0.25 e1 mm diameter). Three two-equation turbulence
models were chosen for the simulations, the popular standard k- ε, the Shear Stress
Transport (SST) and the baseline (BSL) k- u model together with ﬁve notional nozzle
approaches. The numerical results were presented in a systematic way in order to make
general conclusions on the performance of both the approaches and models.
Copyright ª 2012, Hydrogen Energy Publications, LLC. Published by Elsevier Ltd. All rights
reserved.
1. Introduction
The accidental release from high pressure H 2 systems may
lead to a jet of several meters size. Understanding and pre-
dicting the jet behaviour is an essential step in any safety
analysis of high pressure systems. The jet will be under-
expanded close to the release and will rapidly accelerate
and expand to atmospheric pressure through a series of
shocks. Numerical simulations to rigorously resolve the shock
region with a satisfactory grid resolution are demanding.
Together with the need for a long enough computational
domain to encompass the subsonic ﬂow further downstream,
the numerical effort can be intensive. For example, in [1]
a computational mesh of 200.000 nodes was used to model
only ¼ of the shock region of a H
2 release from a 20 MPa vessel.
Also, in HYPER [2] a grid resolution between 1/32 to 1/64 of the
actual leak diameter was necessary to ensure grid indepen-
dence. To overcome the expensive computational demands,
several approaches have been proposed in the past which
replace the actual nozzle by a notional one (often referred to
as ﬁctitious or pseudo-diameter nozzle) that occupies a larger
area but with the same ﬂow rate as the real one and at
ambient pressure and uniform velocity. The approaches have
been implemented in several numerical investigations. In [3]
Birch1984 [4] approach was used to model horizontal H
2
releases of several high pressure experiments. The authors
reported good agreement with the experimental measure-
ments. In [5] the majority of the participants used notional
* Corresponding author .
E-mail addresses: eﬁktm@yahoo.com (E. Papanikolaou), daniele.baraldi@jrc.nl (D. Baraldi), mike.kuznetsov@kit.edu (M. Kuznetsov),
venets@ipta.demokritos.gr (A. Venetsanos).
Available online at www.sciencedirect.com
journal homepage: www.elsevier.com/locate/he
international journal of hydrogen energy 37 (2012) 18563 e18574
0360-3199/$ e see front matter Copyright ª 2012, Hydrogen Energy Publications, LLC. Published by Elsevier Ltd. All rights reserved.
http://dx.doi.org/10.1016/j.ijhydene.2012.09.135

<!-- PDF_PAGE: 2 -->

nozzle approaches to model a 35 MPa pressure H 2 release. In
[6] a notional nozzle approach was used to model several H 2
and CH4 releases from compressed gaseous systems at 20, 35
and 70 MPa. In [7] a notional nozzle approach was used to
model the release of CH 4 at pressures ranging from 0.85 to
10 barg inside a mechanically ventilated room and reported
good predictions. In [8] numerical results to evaluate the LFL
extent of vertical free H 2 and CH 4 with Birch1984 [4] and
Schefer 2007 [9] notional nozzle approaches were presented. A
comparison between the results of the actual and a notional
nozzle approach (similar to Birch1984) of a H
2 release at
430 bar was presented in [10] and it was found that the
notional approach produced 25 e30% longer extents of the
ﬂammable cloud. The difference was attributed to the use of
real gas properties in the actual leak modelling in contrast to
the ideal gas properties and the different input sound velocity
of the jet of the notional approach. Finally, the validation of
notional nozzle approaches has been identiﬁed [11,12] as an
issue that needs investigation.
2. Notional nozzle approaches
Some of the most known notional nozzle approaches are
Birch1984 [4], Birch1987 [5], Ewan [13] and Schefer [9]. The
Birch1984 approach is based on conservation of mass only and
the Birch1987 on conservation of both mass and momentum.
Both of them consider that the temperature of the jet is equal
to atmospheric. Ewan’s approach is the same as the Birch1987
but with the assumption that the temperature of the jet is
equal to the one derived from the isentropic expansion of the
jet from stagnant conditions to the actual nozzle. Schefer
approach is analogous to Birch1987, but proposes the use of
the Abel-Noble equation of state for the calculation of real gas
properties instead of the ideal gas law. Attempts to propose
a more accurate modelling of the leak source take also into
account the conservation of energy, assuming that the jet is
either ideal gas [14] or with properties being calculated using
fundamental equations of state [15]. Furthermore, Harstad
[16] proposed the location of the notional nozzle being just
after the Mach disk with an area equal to that of the disk while
keeping the assumption that the pressure is atmospheric.
3. Experimental description
Experiments of horizontal high momentum H 2 releases were
carried out at the HYKA test site of the Institute for Nuclear and
Energy Technologies of the FZK/KIT to evaluate the H 2 distri-
bution and ﬂow ﬁeld in free turbulent jets at different condi-
tions. The release oriﬁce was located 0.9 m from the ground to
avoid surface effects. The jets were released from a bulk vessel
at initial pressures ranging from 20 to 250 bars and from nozzle
diameters ranging from 0.25 mm to 1 mm into still air.
Measurements of radial and centreline distributions of H
2
concentration and ﬂow velocity were taken at 0.75 m, 1.5 m
and 2.25 m from the nozzle. A description of the experiments
can also be found in[17] and [18]. Three experimental sets were
selected for this study, namely HD35-37, HD22-24 and HD00-
02. The conditions of the experiments are shown in Table 1 .
The last column shows the location of the above mentioned
measurements for each experimental condition.
4. Simulations set up
Table 2 presents the release conditions based on the different
notional nozzle approaches. An average stagnation pressure
(53.27 bar) was used for the HD35-37 experimental set, 2
stagnation pressures, i.e. 113.3 bar and the average of
104.8 bar and 99.6 bar (102.2 bar) for the HD00-02 set and
ﬁnally a stagnation pressure equal to 162 bar was used for the
HD22-24 set as initial conditions. The velocity of Birch1984
and Ewan approaches is sonic, the one of Birch1987 and
Schefer is higher as it is assumed that all excess pressure goes
to increasing the jet’s momentum whereas the one of Harstad
is far less than sonic as the conditions after the Mach disk are
considered. The table presents also the momentum ﬂow rate,
the enthalpy ﬂux and the net rate of energy ﬂow (sum of
speciﬁc enthalpy and speciﬁc kinetic energy) through each
notional nozzle. The same parameters are given for the real
nozzle based on the experimental conditions (assuming real
gas properties and isentropic expansion at the nozzle) for
comparison.
The numerical calculations were performed with ANSYS-
CFX version 12.1 [19]. The following set up was applied to all
simulations:
- Simulations were performed for 10 s to ensure steady state.
- The High Resolution scheme was used for discretization of
advection terms (a blending factor allows a switch to 1st
Order Advection scheme based on local variable gradients).
- The 2nd Order Backward Euler discretization scheme was
used for transient terms.
- Total energy option was selected (transport of enthalpy
including kinetic energy effects).
- The ideal gas law was used as equation of state.
- Stagnant conditions were assumed as the initial state with
atmospheric pressure and temperature equal to 14.5
/C14 C.
- The velocity and temperature, as calculated from the
notional nozzle approaches ( Table 2 ), were speciﬁed at the
inlet. All simulations had a common incoming turbulence
intensity (5%) assigned to the inlet. The effect of turbulence
intensity at the source was investigated by increasing
Table 1 e Experimental conditions.
Test No. Nozzle
diameter
(mm)
Pressure
(bar)
Flow
rate
(10/C0 3 kg/s)
Distance
from
nozzle (m)
HD35-37 1 54.6 2.46 0.75
52.1 2.35 1.5
53.1 2.39 2.25
HD00-02 0.75 113.3 2.87 0.75
104.8 2.66 1.5
99.6 2.53 2.25
HD22-24 0.25 162.8 0.46 0.75
160.4 0.45 1.5
162.1 0.46 2.25
international journal of hydrogen energy 37 (2012) 18563 e1857418564

<!-- PDF_PAGE: 3 -->

its value from 5% (the “default” value) to 10% for the experi-
mental set HD22-24 using Schefer approach and all 3 turbu-
lence models and was found insigniﬁcant. The importance of
the turbulence intensity has also been investigated in the
past [20e22].I n [20] for example, the authors concluded that
for moderate grid resolution, the turbulence intensity has
a weak effect on the predictions, provided that its value is less
than 30%. Also in [21] RANS simulations showed small
sensitivity to inlet turbulence intensity
- The dimensions of the computational domain were
15 m /C2 10 m /C2 10 m. Ground was deﬁned as wall (no slip
boundary condition), west and top planes as openings
(relative total pressure for inﬂow and relative static pressure
for outﬂow set to zero, zero gradient for turbulent quanti-
ties), east plane as outlet (averaged relative static pressure
set to zero) and ﬁnally for north and south planes
a symmetry assumption (zero normal velocity component
and zero normal scalar variable gradients) was made.
- The mesh used was unstructured. Information about the
mesh characteristics is given in paragraph “Grid sensitivity
analysis”.
5. Non dimensional features of turbulent
free-shear round jets
The conﬁguration and coordinate system of a turbulent round
jet is shown in Fig. 1.
In the self-similar region ( x=dj > 30) of high-Reynolds-
number turbulent jets (Re > 104, where Re ¼ Ujdj=y), the cen-
treline velocity UoðxÞhhUðx; 0; 0Þi and half width r1=2ðxÞ (such
that hUðx; r1=2ðxÞ; 0Þi ¼ 1
2 U0ðxÞ) vary according to [23]:
U0ðxÞ
Uj
¼ B
ðx /C0 x0Þ
dj
(1)
r1=2ðxÞ¼ Sðx /C0 x0Þ (2)
Where B and S are empirical constants and xo the virtual
origin.
Pope [23] considers that the constants B and S of these laws
are independent of Re and that their values are 5.8 and 0.094
respectively. In the case of fully turbulent ( Re > 3∙104 [24])
buoyant jets the character of the ﬂow is determined by the ratio
of inertial to buoyant forces, the Froude number, which
assuming uniform velocity and density proﬁles at the source is:
Fr ¼
rjU2
j
gdj
/C12/C12rN /C0 rj
/C12
/C12 (3)
A high Fr number leak ( Fr > 1000 according to [25])i s
momentum dominated whereas a low Fr number leak (Fr < 10
according to [25]) is dominated by buoyancy forces. Three
regions can be observed in turbulent buoyant jets: the one
close to the nozzle (momentum-dominated regime), followed
by an intermediate region and the buoyancy-dominated
regime in the far ﬁeld. Similarly to the turbulent non
Table 2 e Conditions at the notional nozzle.
Approach Temperature (K) Density
(kg/m3)
Velocity
(m/s)
Diameter
(10/C0 3 m)
Mass ﬂow
rate (10/C0 3 kg/s)
Momentum
ﬂow rate
(kg m2/s)
Enthalpy
ﬂux (kJ/s)
Net rate
of energy ﬂow
(103 kJ/s)
HD35-37 (1 mm nozzle diameter, 53.27 bar)
Birch1984 287.6 0.0854 1292 5.262 2.4 3.1 10.2 2.01
Birch1987 287.6 0.0854 1984 4.247 2.4 4.76 10.2 4.73
Ewan 238.8 0.1029 1178 5.024 2.4 2.83 8.58 1.67
Schefer 287.6 0.0854 2001 4.228 2.4 4.81 10.2 4.82
Harstad 278.4 0.0882 510 8.241 2.4 1.23 9.92 0.32
Exp. data 237 2.74 1200 1.0 2.4 2.88 57.2 1.78
HD00 (0.75 mm nozzle diameter, 113.3 bar)
Birch1984 287.6 0.0854 1292 5.754 2.87 3.71 12.2 2.41
Birch1987 287.6 0.0854 1999 4.626 2.87 5.74 12.2 5.75
Ewan 238.8 0.1029 1178 5.492 2.87 3.38 10.3 2.00
Schefer 287.6 0.0854 2036 4.584 2.87 5.85 12.2 5.96
Harstad 278.6 0.0882 503 9.079 2.87 1.44 11.9 0.37
Exp. data 235 5.59 1221 0.75 2.87 3.50 133 2.27
HD01-02 (0.75 mm nozzle diameter, 102.2 bar)
Birch1984 287.6 0.0854 1292 5.471 2.59 3.35 11.1 2.18
Birch1987 287.6 0.0854 1998 4.399 2.59 5.19 11.1 5.19
Ewan 238.8 0.1028 1178 5.223 2.59 3.06 9.27 1.81
Schefer 287.6 0.0854 2031 4.363 2.59 5.27 11.1 5.36
Harstad 278.6 0.0882 504 8.626 2.59 1.31 10.7 0.34
Exp. data 235 5.08 1217 0.75 2.59 3.16 110 2.03
HD22-24 (0.25 mm nozzle diameter, 162 bar)
Birch1984 287.6 0.0854 1292 2.303 0.46 0.59 1.96 0.39
Birch1987 287.6 0.0854 2004 1.849 0.46 0.92 1.96 0.93
Ewan 238.8 0.1028 1178 2.199 0.46 0.54 1.64 0.32
Schefer 287.6 0.0854 2055 1.827 0.46 0.95 1.96 0.97
Harstad 278.7 0.0881 500 3.645 0.46 0.23 1.90 0.06
Exp. data 234 7.76 1239 0.25 0.46 0.57 29.4 0.38
international journal of hydrogen energy 37 (2012) 18563 e18574 18565

<!-- PDF_PAGE: 4 -->

buoyant round jet, Chen and Rodi [26] by reviewing experi-
mental data of steady low Mach number vertical buoyant jets
suggested that two distinct forms of self-similarity are
possible, one in each of the momentum- and buoyancy-
dominated regimes. In these similarity regions the variation
of velocity and excess temperature (or concentration) along
the centreline is different.
Chen and Rodi [26] proposed a scaled distance x
b to esti-
mate the distance from the release at which buoyancy forces
become important:
x
b ¼ Fr/C0 1 =
2
/C18rj
rN
/C19/C0 1 =
4/C18x
dj
/C19
(4)
They suggested that the ﬂow is momentum-dominated
when xb < 0.53. However, Papanicolaou and List [27] showed
that momentum dominance holds for longer distances from
the leak ( xb < 1). Chen and Rodi [26] proposed the following
decay laws for centreline velocity and volumetric concentra-
tion in a round buoyant jet (in the non-buoyant region):
Uc
Uj
¼ 6:2
/C18rj
rN
/C191 =
2/C18x
dj
/C19/C0 1
(5)
Cc
Cj
¼ 5
/C18rj
rN
/C19/C0 1 =
2/C18x
dj
/C19/C0 1
(6)
It is interesting to mention that the constant in eq. (5) has
been reported by a recent review on turbulent jets [28] to vary
from 5 to 6.7. Also, in [29] a similar formula to eq. (6) was
proposed for mass fraction decay law for compressible H 2
ﬂows but with a constant equal to 5.4 instead of 5. In [14] an
analysis and experimental data to study the spreading and
centreline property decay laws of under expanded supersonic
jets (dried air with jet exit-to-ambient pressure ratios ranging
from 1 to 20.3) was presented. The authors proposed the axial
distance and velocity to be normalized by ðr
2=rNÞ
1 =
2
d/C3 and U2
respectively (where r2, d* and U2 are the density, “ﬁctitious”
diameter and velocity after the expansion region). In [14],i ti s
stated that a closer grouping of velocity decay data of several
sonic jets was achieved when they used the normalization
strategy with ðr
2=rNÞ
1 =
2
d/C3 and U2. For the same reason, the same
type of normalization has been also used by other authors
[15,17,18,21,30]. Because of the above reasons, we followed
Yu¨ ceil and O ¨ tu¨ gen’ approach for the calculations of the
normalized centreline ﬂow velocity and H 2 mass fraction in
the following paragraphs. In [14], the average value of the
slope of the centreline velocity decay law was found equal to
6.25 whereas the total relative spread between the minimum
and maximum slope of their experimental data was about
18%. They also noticed that the value of the slope is decreasing
with increasing jet exit-to-ambient pressure ratios. However,
they argued that no further decrease should be expected for
higher than 20.3 ratios.
In Tables 3 and 4 the exit Re and Fr numbers of the experi-
ments (assuming isentropic expansion from stagnant condi-
tions to the nozzle, allowing for H
2 real gas behaviour) and
notional nozzle approaches, together with the conservative
distance of the momentum-dominated regime (i.e. for x
b < 0.5,
from formula (4) ) are shown. The table shows that the
Table 3 e Jet exit characteristics: Froude and Reynolds number at the nozzle/exit, distance x at which buoyancy becomes
dominant.
Exp. Birch 1984 Birch 1987 Ewan Schefer Harstad
HD35-37 (1 mm) Re 1.16$104 6.69$104 8.29$104 5.82$104 8.33$104 4.14$104
Fr 2.45$108 2.48$106 7.25$106 2.64$106 7.41$106 2.56$105
x (m) 9.71 2.14 2.95 2.21 2.97 1.09
HD00 (0.75 mm) Re 8.70$103 7.32$104 9.11$104 6.37$104 9.19$104 4.49$104
Fr 2.35$108 2.27$106 6.76$106 2.42$106 7.07$106 2.26$105
x (m) 8.63 2.24 3.11 2.31 3.15 1.12
HD01-02 (0.75 mm) Re 8.70$103 6.96$104 8.65$104 6.06$104 8.73$104 4.28$104
Fr 2.47$108 2.39$106 7.10$106 2.54$106 7.40$106 2.38$105
x (m) 8.46 2.18 3.03 2.25 3.07 1.10
HD22-24 (0.25 mm) Re 2.90$103 2.93$104 3.65$104 2.55$104 3.70$104 1.79$104
Fr 6.57$108 5.67$106 1.70$107 6.03$106 1.81$107 5.55$105
x (m) 5.26 1.42 1.97 1.46 2.01 0.707
Fig. 1 e Schematic of a round-jet, showing the coordinate
system (source).
international journal of hydrogen energy 37 (2012) 18563 e1857418566

<!-- PDF_PAGE: 5 -->

experimental measurements, taken at 0.75 m, 1.5 m and 2.25 m
from the leak, fall well within the momentum-dominated
regime. The extent of this region is not the same for the
notional nozzle approaches. Obviously, Harstad approach
creates a region much smaller than the rest, whereas Schefer
followed by Birch1987 approach create the longer regions.
6. Results and discussion
The evaluation of the notional nozzle approaches, together
with the 3 turbulence models, was mainly based on their
ability to predict the centreline H
2 mass fraction and ﬂow
velocity at the three measurement points. Another param-
eter that was also taken into account was the ability to
predict the experimental spreading rates of both centreline
velocity and H
2 mass fraction. The spreading rate is an
indicator of the width of the mixing region and is also often
used to assess the turbulence models’ accuracy (for example
[31,32], and [33]). However, as stated in [30], it is only one
parameter and it does not provide information about the
shape of the proﬁle. Concentration and ﬂow velocity in both
experiments and simulations were ﬁtted by Gaussian proﬁles
at the distances from the release that lie within the
momentum-dominated regimes and their spreading rates
were calculated from the Gaussian ﬁts. The spreading rates
were deﬁned as the value of the radial distance from the
centreline where H
2 mass fraction and velocity are half their
centreline value.
6.1. Grid sensitivity analysis
Before evaluating the notional nozzle approaches with the
turbulence models, a grid sensitivity analysis was carried out
with 4 different mesh resolutions by varying the number of
grid points and therefore the grid spacing of a conical geom-
etry starting near the release and extending 2.3 m far from it.
The rest of the grid was kept the same for all 4 meshes. The
grid resolution at the source was always ¼ of the diameter of
the notional nozzle of each approach. The grid characteristics
of the 4 meshes, namely coarse, ﬁne, ﬁner and ﬁnest are given
in the following table. The size of the domain was kept
constant (15 m /C2 10 m /C2 10 m).
The HD22-24 set was chosen for the sensitivity analysis. All
5 approaches with the 3 turbulence models were simulated
using the 4 different grids. A grid independent numerical
solution was found with the ﬁner grid, as the difference
between the ﬂow velocity and H
2 concentration with the ones
of the ﬁnest grid was between 2% and 5% for most cases
whereas the maximum discrepancy was less than 10%. The
same strategy that was used to generate the ﬁner grid for
HD22-24 was adopted for the computational meshes for
HD35-37 and HD00-01.
6.2. Simulation results and comparison with
experimental data
Two statistical performance indicators were used to evaluate
the approaches, as a direct comparison between the results of
the experimental data and simulations was not practical due
to the large number of simulations. These statistical indica-
tors were recommended by Chang and Hanna [34] for evalu-
ating air dispersion models. However, they have been used
often in different types of scenarios, such as subsonic H
2 jet
releases in conﬁned spaces [35],H 2 deﬂagrations in a tunnel
[36], bonﬁre tests on thermally insulated LPG tanks [37].
Geometric Mean Bias (MG): measures relative mean bias
and indicates only systematic errors based on a logarithmic
scale. Values of 0.5 and 2.0 can be thought of as ‘factor of two’
over- and under-predictions in the mean, respectively. It has
a value of 1 for an ideal model performance.
MG ¼ exp
/C16
ln Vo /C0 ln Vp
/C17
(7)
Geometric Mean Variance (VG): measures relative scatter. It
has a value of 1 for an ideal model performance.
VG ¼ exp
/C20/C0
ln Vo /C0 ln Vp
/C12
/C21
(8)
where Vo is the observed (experimental) value and Vp is the
predicted (numerical) value.
The values of the statistical indicators are aggregated for
all 3 measurement points along the centreline (0.75 m, 1.5 m
and 2.21 m from the release) for each notional nozzle
approach and turbulence model. A graph of MG versus VG is
Fig. 2 e Geometric mean bias (MG) versus geometric mean
variance (VG) for HD35-37, centreline ﬂow velocity (green:
SST, blue: BSL and red: k- ε). (For interpretation of the
references to colour in this ﬁgure legend, the reader is
referred to the web version of this article.)
Table 4 e Grid characteristics.
Coarse Fine Finer Finest
Total number of nodes 47.500 68.800 179.300 533.300
Number of nodes in
the conical geometry
5.500 19.300 72.100 344.600
Minimum (10 /C04 m) and
maximum (10 /C01 m) grid
size in the conical
geometry
4.8 4.8 4.8 4.8
1.56 1.1 0.69 0.3
international journal of hydrogen energy 37 (2012) 18563 e18574 18567

<!-- PDF_PAGE: 6 -->

used for a systematic evaluation. This type of graph shows
a parabola which represents the minimum possible VG value
corresponding to a particular MG value due to systematic bias.
All points must lie either on the parabola or inside. Any point
located close to the parabola, indicates results with system-
atic error. The ones close to the central axis ( x ¼ 1) indicate
dispersion of results. Points on the left hand side of the central
axis show a tendency to over prediction. The opposite holds
for points on the right hand side. For a perfect agreement
between numerical results and experimental data, the points
should be located on the parabola vertex (1,1).
6.2.1. Case HD35-37 (H 2 release from 1 mm pipe diameter at
53 bar)
Fig. 2 shows the values of MG versus VG of the centreline ﬂow
velocity of the experimental set HD35-37. In general, most of
simulations under predict the experimental value of the
centreline velocity except Birch1987 and Schefer with k- ε
model. A direct comparison between each simulation and
experimental data showed that there is a tendency to under
predict the centreline velocity at 1.0 m and 2.25 m except
Birch1987 and Schefer with k- ε model which gave results
slightly higher than the experimental (the same approaches
with the other 2 models produced results slightly lower than
the experimental). At the closest point (0.75 m) Birch1984 and
Ewan approaches with k- ε model predicted values very close
to the experimental whereas the other 2 models showed
under prediction. Also, Birch1987 and Schefer with BSL and
SST gave results very close to the experimental close to the
release. The same approaches with k- ε model overpredicted
the data. Harstad approach showed generally the largest
under prediction, with BSL and SST being less accurate
whereas all three proﬁles were not symmetrical about the
centreline at 2.25 m due to buoyancy effects. Finally, the
comparison showed that irrespective of the approach, k- ε
model produces the highest centreline values (which is inti-
mately linked to the narrower radial proﬁles). The other two
models had a similar performance with BSL producing always
either slightly or moderately higher values at the centreline.
As Fig. 2 shows, the under prediction (MG value) is less than 2
for all cases apart from Harstad approach with BSL and SST
models which though higher, did not exceed a factor of 3. The
fact that all points lie very close, or on the parabola, shows
that all simulations have only a mean bias with respect to
experimental data, i.e. for each simulation, the ratio C
o/Cp is
nearly constant for all 3 measurement points. This is clearly
shown in Fig. 3 (left) where the normalized centreline ﬂow
velocity is plotted against the equivalent jet initial conditions
following the approach of Yu ¨ ceil and O ¨ tu¨ gen [14],a si ti s
explained in paragraph 5. The slope of the straight line ﬁtting
the experimental data is only 1.2% lower than the proposed by
Chen and Rodi [25]. The slope of Birch1984 approach was 28%,
5% and 54% higher than the one of experimental data for BSL,
k-ε and SST models respectively. Birch1987, Ewan and Schefer
showed the same tendency, i.e. the closest value of the slope
was produced by k- ε (between 5% and 8% overprediction). The
other two models produced values by 28% e58% higher. Har-
stad approach with all turbulence models deviated from the
Fig. 3 e Normalized centreline ﬂow velocity (left) and H 2 mass fraction (right) for HD35-37 (green: SST, blue: BSL and red: k- ε),
where d* in the x-axis label is the “notional” diameter. (For interpretation of the references to colour in this ﬁgure legend,
the reader is referred to the web version of this article.)
Fig. 4 e Geometric mean bias (MG) versus geometric mean
variance (VG) for HD35-37, centreline H 2 mass fraction
(green: SST, blue: BSL and red: k- ε). (For interpretation of
the references to colour in this ﬁgure legend, the reader is
referred to the web version of this article.)
international journal of hydrogen energy 37 (2012) 18563 e1857418568

<!-- PDF_PAGE: 7 -->

experimental value considerably (approximately by /C0 94%),
however this was partly expected as the extent of the
momentum-dominated regime included only the ﬁrst
measurement point at x ¼ 0.25 m (see Table 3).
The results of the centreline H
2 mass fraction showed in
general a tendency to overprediction ( Fig. 4 ). Simulations
with Birch1984 and Ewan overpredicted at all 3 points irre-
spective of the model used with k- ε performing the worst.
Birch1987 and Schefer performed very well with BSL,
underpredicted slightly with SST and clearly overpredicted
with k- ε which deviated from the data the most, at all 3
points. Harstad approach overpredicted considerably at all
three points and with all models, with k- ε performing the
worst. The proﬁle is again not symmetrical about the cen-
treline at 2.25 m due to buoyancy. As with the ﬂow velocity
results, irrespective of the approach used, k- ε model
produces the highest centreline values followed by BSL and
SST (the last two models performed similarly in most cases).
As Fig. 4 shows, the over prediction is in general less than 0.5,
apart from Harstad approach which especially with k- ε
model was close to 0.3. Again, all points being located on the
parabola show that simulations have only a mean bias with
respect to experimental data. Fig. 3 (right) shows the
normalized centreline H
2 mass fraction. The slope of the
straight line ﬁtting the experimental data was 2.5% lower
than that proposed in [29]. The slope of Birch1984 approach
was 1% and 6% higher than the one ﬁtting the experimental
data for BSL and SST and 25% lower for k- ε. Birch1987, Ewan
and Schefer showed the same tendency, i.e. the closest value
of the slope was produced by BSL and SST models whereas
k-ε under predicted the value by approximately 25%. Again,
Harstad approach deviated the most irrespective of the
model used ( /C0 50% to /C0 66%).
Generally, most of the approaches performed well for this
experimental set, with Birch1987 and Schefer approaches
performing the best when BSL or SST model was used and
Harstad approach performing the worst among all (the
proﬁles were again off y-axis at 2.25 m). The k- ε model
produced higher centreline values (therefore narrower radial
proﬁles) than the other two models.
Another parameter that was investigated was the ability of
the approaches and models to predict the experimental
spreading rates of velocity and H
2 mass fraction. Fig. 5 (left)
shows that the spreading rate of velocity is predicted more
accurately when the BSL model is applied irrespective of the
approach, whereas SST clearly over predicts the rate and k- ε
clearly under predicts it. However, all points are located close
to the parabola’s vertex, so all performed rather well. The
performance was also good for the H
2 concentration
spreading rate ( Fig. 5 , right). This time both BSL and SST per-
formed very well, whereas k- ε under predicted by a factor not
higher than 1.5 (MG). Simulations with Harstad approach were
not included as, based on the scaled distance xb, only the
nearest to the release point was located within the
momentum-dominated regime (see Table 3 where x < 1.2 m)
and therefore a Gaussian ﬁt wouldn’t be appropriate for ﬁtting
the proﬁles at the other 2 measurement points.
Fig. 5 e Geometric mean bias (MG) versus geometric mean variance (VG) of velocity spreading rate (left) and H 2 mass fraction
(right) for HD35-37 (green: SST, blue: BSL and red: k- ε). (For interpretation of the references to colour in this ﬁgure legend, the
reader is referred to the web version of this article.)
Fig. 6 e Geometric mean bias (MG) versus geometric mean
variance (VG) for HD00-02, centreline ﬂow velocity (green:
SST, blue: BSL and red: k- ε). (For interpretation of the
references to colour in this ﬁgure legend, the reader is
referred to the web version of this article.)
international journal of hydrogen energy 37 (2012) 18563 e18574 18569

<!-- PDF_PAGE: 8 -->

6.2.2. Case HD00-02 (H 2 release from 0.75 mm pipe diameter
at approximately 110 bar)
Fig. 6 shows the values of MG versus VG of the centreline ﬂow
velocity for the HD00-02 set. As in previous experimental set,
there is generally a tendency to underprediction. Speciﬁcally,
Birch1984 and Ewan underpredicted with BSL and SST at all
measurement points. The same approaches with k- ε over-
predicted close to the release and underpredicted moderately
at the other two measurement points. Birch1987 and Schefer
approaches performed well at all points especially when BSL or
SST model was used (the approaches overpredicted the
data with k- ε). Harstad approach underpredicted the data
irrespective of the turbulence model applied with BSL and
SST producing the lowest values. As in the previous set, most
of the simulations produced MG values well within the
range 0.5 < MG < 2. Fig. 7 shows the values of MG versus VG of
the centreline H
2 mass fraction. As in previous set, there is a
general tendency to over-prediction. Again, Harstad approach
performed the worst, overpredicting irrespective of the model
applied. The same holds for Birch1984 and Ewan approaches,
with k- ε performing the worst whereas the results with BSL
and SST were close to the experimental. Birch1987 and Schefer
performed again rather well, especially when BSL and SST
models were applied. The over-prediction (MG) was not below
0.5 with the exception of Harstad approach (the highest over-
prediction was produced with k- ε, see Fig. 7).
Generally, the results of ﬂow velocity and H
2 mass fraction
had the same trend as in the previous experimental set:
Birch1987 and Schefer approaches performed the best when
BSL or SST model was used and Harstad performed the worst.
Concerning the turbulence models used, all simulations with
k-ε produced the highest values, followed by BSL and SST.
Fig. 8 (left) shows the normalized centreline ﬂow velocity.
The slope of the straight line ﬁtting the experimental data is
42% higher than the proposed in [26]. The slope of Birch1984
approach deviated from the experimental by /C0 11%, /C0 27% and
6% for BSL, k- ε and SST respectively. Birch1987, Ewan and
Schefer approaches showed the same tendency, i.e. approxi-
mately /C0 10% to /C0 14%, /C0 26% to /C0 28% and 4% e7% for BSL, k- ε
and SST respectively. Harstad approach produced lower
slopes by 41% e66%. Fig. 8 (right) shows the normalized cen-
treline H
2 mass fraction. The slope from the experimental
data is 10% lower than the theoretical [29]. The slope of the
approaches deviated by /C0 3% to /C0 5%, /C0 28% to /C0 30% and /C0 0.3%
to 5% for BSL, k- ε and SST respectively. Harstad approach
produced lower, than the experimental, slopes by 52% e71%.
Fig. 9 shows the MG versus VG plots for the spreading rate
of velocity (left) and H 2 mass fraction (right). Concerning the
velocity spreading rate, it seems that k- ε model performs
better than the other two which over predict the rate.
However, the over prediction is not less than 0.6. The perfor-
mance was also good for the H
2 concentration spreading rate
with the k- ε model under predicting the rate by a factor not
higher than 1.5 and BSL and SST models over predicting by
a factor not less than 0.85.
6.2.3. Case set HD22-24 (H 2 release from 0.25 mm pipe
diameter at approximately 160 bar)
Fig. 10 and Fig. 11 show the values of MG versus VG of the
centreline ﬂow velocity and H 2 mass fraction of HD22-24 set
respectively. This time all simulations overpredicted the
Fig. 7 e Geometric mean bias (MG) versus geometric mean
variance (VG) for HD00-02, centreline H 2 mass fraction
(green: SST, blue: BSL and red: k- ε). (For interpretation of
the references to colour in this ﬁgure legend, the reader is
referred to the web version of this article.)
Fig. 8 e Normalized centreline ﬂow velocity (left) and H 2 mass fraction (right) for HD00-02 (green: SST, blue: BSL and red: k- ε);
where d*is the “ﬁctitious” diameter. (For interpretation of the references to colour in this ﬁgure legend, the reader is referred
to the web version of this article.)
international journal of hydrogen energy 37 (2012) 18563 e1857418570

<!-- PDF_PAGE: 9 -->

velocity at the closest point. Concerning the other two points,
Birch1987 and Schefer overpredicted irrespective of the model
used with k- ε performing the worst whereas Birch1984 and
Ewan overpredicted with k-ε, slightly underpredicted with BSL
and ST. Concerning the H 2 mass fraction predictions, all
simulations overpredicted with Birch1984 and Ewan per-
forming the worst (especially with k- ε).
Fig. 12 shows the normalized centreline velocity and H 2
mass fraction. The slope of the lines ﬁtting the experimental
data is 160% and 34% higher than the theoretical ( [26] and [29])
for velocity and H
2 mass fraction respectively. The slopes from
simulations were lower than the experimental by 34% e57%
and 20% e48% for velocity and H 2 mass fraction. Harstad
approach produced proﬁles that were off the release axis at
both 1.5 m and 2.25 m.
6.3. Discussion
The results are mainly discussed and assessed in terms of the
physical (real) nozzle diameter, the notional nozzle approach
and the turbulence model applied. Also, both simulations and
experimental data are compared with the centreline decay
laws proposed in literature.
A comparison of simulations with the three different
nozzle diameters applying the same notional nozzle approach
and turbulence model showed that the performance is getting
moderately worse with decreasing nozzle diameter. Also,
there was a clear tendency of H
2 mass fraction overprediction
in all experimental sets (with results of HD22-24 set -smallest
physical diameter- deviating 1.3 e3 times from the data). On
the other hand, the ﬂow velocity of HD35-37 (1 mm diameter)
and HD00-02 (0.75 mm diameter) sets was underpredicted but
Fig. 9 e Geometric mean bias (MG) versus geometric mean variance (VG) of velocity spreading rate (left) and H2 mass fraction
(right) for HD00-02 (green: SST, blue: BSL and red: k- ε). (For interpretation of the references to colour in this ﬁgure legend, the
reader is referred to the web version of this article.)
Fig. 10 e Geometric mean bias (MG) versus geometric mean
variance (VG) for HD22-24, centreline ﬂow velocity (green:
SST, blue: BSL and red: k- ε). (For interpretation of the
references to colour in this ﬁgure legend, the reader is
referred to the web version of this article.)
Fig. 11 e Geometric mean bias (MG) versus geometric mean
variance (VG) for HD22-24, centreline H 2 mass fraction
(green: SST, blue: BSL and red: k- ε). (For interpretation of
the references to colour in this ﬁgure legend, the reader is
referred to the web version of this article.)
international journal of hydrogen energy 37 (2012) 18563 e18574 18571

<!-- PDF_PAGE: 10 -->

this tendency was not clearly followed in HD22-24 set
(0.25 mm diameter).
Concerning the notional nozzle approaches, the results
can be classiﬁed into three groups having broadly a similar
performance, one group with Birch1984 and Ewan, another
with Birch1987 and Schefer and ﬁnally Harstad alone. Gener-
ally, Birch1987 and Schefer approaches performed better,
followed by Birch1984 and Ewan and lastly Harstad which
deviated from the data the most. This grouping can be asso-
ciated with the conditions at the notional nozzle of each
approach. From Table 2 (which gives the conditions at each
notional nozzle) it can be seen that the momentum ﬂow rate
and net rate of energy ﬂow of Birch1987 and Schefer are
always higher and similar, followed by Birch1984 and then
closely by Ewan and ﬁnally Harstad.
Concerning the overall performance of turbulence models
for H
2 concentration predictions, it seems that SST model is
better followed closely by BSL and lastly k- ε. For the ﬂow
velocity, the conclusions are not as straightforward. It seems
that k- ε performs better with Birch1984 and Ewan (especially
for the larger release diameter) whereas SST and BSL are
closer to the experimental data with Birch1987 and Schefer
approaches.
One could expect SST to perform similar to k-ε as it is widely
known that SST switches to a k-ε model (actually this k-ε model
is transformed back to a set of k- u equations by using
a blending function) in free shear jet calculations. However,
there are differences between the k- ε models that can justify
the different performance found in this study. As mentioned in
[38] the differences between this model and the exact trans-
formation of the ε-equation of the standard k- ε to an u-equa-
tion results in an extra diffusion term that is not included in the
SST model. Also, as reported in [39], the u-equation diffusion
coefﬁcient has a value of s
u2 ¼ 1=sε ¼ 1=1:3 ¼ 0:769, whereas in
SST su20:857 which corresponds to sε ¼ 1:17. Focussing in k- ε,
its performance in round jet calculations has been commented
in the literature. For example in [23] it has been stated that “a
well known deﬁciency of the k- ε model is that it signiﬁcantly
overpredicts the rate of spreading for the round jet”. Also, in
[31] and [40] the authors presented the performance of four
eddy viscosity turbulence models (among them the k- ε of
Launder and Sharma, k- u of Wilcox and SST of Menter). All
models were found to overpredict the thickness of the experi-
mental velocity proﬁle (i.e. wider proﬁles) and this was attrib-
uted to the “classical well known anomaly in these models that
have been ﬁne-tuned with empirical data of mixing layer, plane
jet and/or far wake experiments”. Having in mind the intimate
linkage between half-widths (thickness of proﬁle) and centre-
line decay in the absence of buoyancy [41], the results of this
study show clearly the same tendency for the ﬁrst two exper-
imental sets (systematic under-prediction of centreline
velocity).
Finally, the decay laws of centreline velocity and H
2 mass
fraction of both experimental data and simulations were not
universal. Concerning the experiments, the slopes were very
close to the theoretical value for the experimental set with the
larger diameter pipe and the lower stagnation pressure. The
slopes assumed different values for the other two experi-
ments. Even though there are several experimental studies
that suggest universal asymptotic values for the region sufﬁ-
ciently far downstream the nozzle (such as in [26,42], and [43]),
there are works that suggest that turbulent ﬂows can asymp-
tote to a variety of self-similar states determined by their
initial conditions (for example in [44,45], and [46]). Concerning
the simulations, the slopes deviated from the experimental
values no more than 58% and 25% for velocity and H
2 mass
fraction for the ﬁrst two sets (excluding Harstad approach)
whereas for the one with the smallest diameter pipe the slopes
deviated substantially from the experimental ones.
7. Conclusions
An evaluation of selected notional nozzle approaches
(Birch1984, Birch1987, Ewan, Schefer and Harstad) for CFD
simulations of free-shear under-expanded round jets was
presented. Three turbulence models were applied for each
notional nozzle approach (BSL, k- ε and SST) and the results
were compared with 3 experimental sets of high pressure H
2
releases from small pipes.
Fig. 12 e Normalized centreline ﬂow velocity (left) and H 2 mass fraction (right) for HD22-24 (green: SST, blue: BSL and red:
k-ε). (For interpretation of the references to colour in this ﬁgure legend, the reader is referred to the web version of this
article.)
international journal of hydrogen energy 37 (2012) 18563 e1857418572

<!-- PDF_PAGE: 11 -->

An attempt to justify and explain the differences found in
the notional nozzle approaches and turbulence models was
presented. It was found that for the same turbulence model
and notional nozzle approach, the performance was gradually
moderately deteriorating with decreasing nozzle diameter.
Comparing the notional nozzle approaches alone, it was
found that these could be grouped based on the momentum
and energy ﬂux at the source with Birch1987 and Schefer
generally performing better, followed by Birch1984 and Ewan
and lastly Harstad. Evaluating the turbulence models, it was
found that the SST performed better followed closely by BSL
and lastly k- ε for prediction of H
2 concentration. For the ﬂow
velocity, the k- ε model performs better with Birch1984 and
Ewan (especially for the larger release diameter) while SST
and BSL are closer to the experimental data with Birch1987
and Schefer approaches.
Experiments of highly under-expanded buoyant jets with
measurements closer to the release and from different release
diameters and pressures should be studied numerically in the
future using notional nozzle approaches together with
different turbulence models in order to make more general
conclusions about their performance. The question about the
universality or the range of applicability of centreline decay
laws and the value of their constants concerning highly
under-expanded buoyant jets should also be addressed.
references
[1] Xu BP, Zhang JP, Wen JX, Dembele S, Karwatzki J. Numerical
study of a highly under-expanded H 2 jet, 1st Int. Conf.
Hydrogen Safety, Pisa, Italy: 2005.
[2] HYPER, Releases, ﬁres and explosions: ﬁnal modelling report,
2008.
[3] Venetsanos AG, Papanikolaou E, Bartzis JG. The ADREA-HF
CFD code for consequence assessment of hydrogen
applications. Int J Hydrogen Energ 2010;35:3908 e39182.
[4] Birch AD, Brown DR, Dodson MG, Swafﬁeld F. The structure
and concentration decay of high pressure jets of natural gas.
Combust Sci Technol 1984;36:249 e61.
[5] Birch AD, Hughes DJ, Swafﬁeld F. Velocity decay of high
pressure jets. Combust Sci Technol 1987;52:161 e71.
[6] Venetsanos AG, Baraldi D, Adams P, Heggem PS,
Wilkening H. CFD modeling of hydrogen release, dispersion
and combustion for automotive scenarios. J Loss Prevent
Proc 2008;21:162e 84.
[7] Ivings MJ, Gant SE, Saunders CJ, Pocock DJ. Flammable gas
cloud build up in a ventilated enclosure. J Hazard Mater 2010;
184:170e6.
[8] Hourri A, Angers B, Be ´ nard P. Surface effects on ﬂammable
extent of hydrogen and methane jets. Int J Hydrogen Energ
2009;34:1569e77.
[9] Schefer RW, Houff WG, Williams TC, Bourne B, Colton J.
Characterization of high-pressure, underexpanded
hydrogen-jet ﬂames. Int J Hydrogen Energ 2007;32:
2081e93.
[10] Tchouvelev A. Hydrogen implementing agreement, task
19 e hydrogen safety, knowl edge gaps in hydrogen
safety e a white paper; January 2008.
[11] Baraldi D, Papanikolaou E, Heitsch M, Moretto P, Cant S,
Roekaerts D, et al. Gap analysis of CFD modelling of
accidental hydrogen release and combustion, JRC. The
Netherlands: Institute for Energy; 2010. EUR 24399 EN.
[12] HySafe, Biennal report on hydrogen safety, chapter III:
accidental phenomena and consequences, June 2007
(http://www.hysafe.org/).
[13] Ewan BCR, Moodie K. Structure and velocity measurements
in underexpanded jets. Combust Sci Technol 1986;45:
275e88.
[14] Yu¨ ceil KB, O¨ tu¨ gen MV. Scaling parameters for under-
expanded supersonic jets. Phys Fluids 2002;14:4206 e15.
[15] Xiao J, Travis JR, Breitung W. Hydrogen release from a high
pressure gaseous hydrogen reservoir in case of a small leak.
Int J Hydrogen Energ 2011;36:2545 e54.
[16] Harstad K, Bellan J. Global analysis and parametric
dependencies for potential unintended hydrogen-fuel
releases. Combust Flame 2006;144:89 e102.
[17] Kuznetsov M, Grune J, Veser A, Friedrich A, Kotchourko N,
Fast G, et al. Optical observation of hydrogen jet structure
and ﬂame propagation in turbulent hydrogen jets; 2010. 14th
International Symposium on Flow Visualization, EXCO
Daegu, Korea.
[18] Veser A, Kuznetsov M, Fast G, Friedrich A, Kotchourko N,
Stern G, et al. The structure and ﬂame propagation regimes
in turbulent hydrogen jets. Int J Hydrogen Energ 2011;36:
2351e9.
[19] CFX-12.0, Documentation, southpointe, 275
technology drive, Canonsburg, PA 15317, USA: ANSYS Inc.
(http://www.ansys.com).
[20] Brennan SL, Makarov DV, Molkov V. LES of high pressure
hydrogen jet ﬁre. J Loss Prevent Proc 2009;22:353 e9.
[21] Houf WG, Evans GH, Schefer RW. Analysis of jet ﬂames and
unignited jets from unintended releases of hydrogen. Int J
Hydrogen Energ 2009;34:5961 e9.
[22]
ALAQS, CFD comparison of buoyant and non-buoyant
turbulent jets, EEC/SE/2007/002, EuroControl Experimental
Centre.
[23] Pope SB. Turbulent ﬂows. Cambridge University Press; 2003.
[24] Spalding DB. Combustion and mass transfer. Oxford:
Pergamon Press Ltd.; 1979.
[25] Hourri A, Gomez F, Angers B, Be ´ nard P. Computational study
of horizontal subsonic free jets of hydrogen: validation and
classical similarity analysis. Int J Hydrogen Energ 2011;36:
15913e8.
[26] Chen CJ, Rodi W. Vertical turbulent buoyant jets, a review of
experimental data. Oxford: Pergamon Press; 1980.
[27] Papanicolaou PN, List EJ. Investigations of round vertical
turbulent buoyant jets. J Fluid Mech 1988;195:341 e91.
[28] Abdel-Rahman A. A review of effects of initial and boundary
conditions on turbulent jets. WSEAS Trans Fluid Mechanics
2010;4(5):257e75.
[29] Makarov D, Molkov V. Structure and concentration decay in
supercritical plane hydrogen jet. 8th ISHPMIE; 2010.
Yokohama Japan.
[30] Schefer RW, Houf WG, Williams TC. Investigation of small-
scale unintended releases of hydrogen: momentum-
dominated regime. Int J Hydrogen Energ 2008;33:6373 e84.
[31] Cebeci T. Analysis of turbulent ﬂows. 2nd revised and
expanded ed. Elsevier Ltd.; 2004.
[32] Wilcox DC. Turbulence modeling for CFD. 2nd ed. DCW
Industries; 1998.
[33] Bardina JE, Huang PG, Coakley TJ. Turbulence modelling
validation, testing and development. Ames Research Centre;
1997.
[34] Chang JC, Hanna SR. Technical description and user’s guide
for the BOOT statistical model evaluation software package,
version 2.0; 2005.
[35] Venetsanos AG, Papanikolaou EA, Delichatsios M, Garcia J,
Hansen OR, Heitsch M, et al. An inter-comparison exercise
on the capabilities of CFD models to predict the short and
long term distribution and mixing of hydrogen in a garage.
Int J Hydrogen Energ 2009;34:5912 e23.
international journal of hydrogen energy 37 (2012) 18563 e18574 18573

<!-- PDF_PAGE: 12 -->

[36] Baraldi D, Kotchourko A, Lelyakin A, Yanez J, Middha P,
Hansen OR, et al. An inter-comparison exercise on
CFD model capabilities to simulate hydrogen
deﬂagrations in a tunnel. Int J Hydrogen Energ 2009;34:
7862e 72.
[37] Landucci G, Molag M, Cozzani V. Modeling the performance
of coated LPG tanks engulfed in ﬁres. J Hazard Mater 2009;
172:447e56.
[38] Georgiadis NJ, Yoder DA. Evaluation of modiﬁed two-
equation turbulence models for jet ﬂow predictions. 44TH
AIAA Aerospace Sciences Meeting and Exhibit. Reno:
Nevada; 2006.
[39] Menter FR. Review of the shear-stress transport turbulence
model experience from an industrial perspective. Int J
Computational Fluid Dyn 2009;23:305 e16.
[40] Wilcox DC. Turbulence modeling for CFD. 2nd printing. La
Can˜ ada, California: DCW Industries, Inc.; 1994.
[41] Sanders JPH, Sarh B, Go ¨ kalp I. Variable density effects in
axisymmetric isothermal turbulent jets: a comparison
between a ﬁrst- and second-order turbulence model. Int J
Heat Mass Transfer 1997;40:823 e42.
[42] Pitts WM. Effects of global density ratio on the centerline
mixing behavior of axisymmetric turbulent jets. Exp Fluids
1991;11:125e34.
[43] Richards CD, Pitts WM. Global density effects on the self-
preservation behavior of turbulent free jets. J Fluid Mech
1993;141:391e429.
[44] George WK. The self-similarity of turbulent ﬂows and its
relation to initial conditions and coherent structures. In:
Arndt REA, George WK, editors. Recent advances in
turbulence; 1989. p. 39 e73.
[45] Mi J, Nobes DS, Nathan GJ. Inﬂuence of jet exit conditions on
the passive scalar ﬁeld of an axisymmetric free jet. J Fluid
Mech 2001;432:91 e125.
[46] Malmstro¨ m TG, Kirkpatrick AT, Christensen B,
Knappmiller KD. Centreline velocity decay measurements in
low-velocity axisymmetric jets. J Fluid Mech 1997;246:
363e77.
international journal of hydrogen energy 37 (2012) 18563 e1857418574
