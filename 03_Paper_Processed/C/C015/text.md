<!-- PDF_PAGE: 1 -->

International Journal of Multiphase Flow 127 (2020) 103273 
Contents lists available at ScienceDirect 
International Journal of Multiphase Flow 
journal homepage: www.elsevier.com/locate/ijmulflow 
On the interaction of water droplet with a shock wave: Experiment 
and numerical simulation 
Sergey V. Poplavski a , Andrey V. Minakov b , c , ∗, Anna A. Shebeleva b , c , Viktor M. Boyko a 
a Khristianovich Institute of Theoretical and Applied Mechanics SB RAS, Novosibirsk 630090, Russia 
b Siberian Federal University, Krasnoyarsk, 660041, Russia 
c Kutateladze Institute of Thermophysics SB RAS, Novosibirsk 630090, Russia 
a r t i c l e i n f o 
Article history: 
Received 7 June 2019 
Revised 10 March 2020 
Accepted 11 March 2020 
Available online 13 March 2020 
Keywords: 
The aerodynamic breakup of drops 
Shock waves 
Mathematical simulation 
VOF 
LES 
a b s t r a c t 
The work is devoted to experimental and computational studies of the behavior of water drop in a ﬂow 
behind incident shock wave and veriﬁcation of calculations on this basis. High-Speed visualization of the 
water drop interaction with the ﬂow behind incident shock wave was obtained in the experiments at 
shock wave Mach numbers Ms = 1.109–1.34 and Weber numbers We = 208–2260. Conditions consistent 
with the experiments are simulated in the calculations. The numerical approach is based on the use 
of the volume of ﬂuid (VOF) method to resolve the phase interface, large eddy simulation (LES) model 
to describe turbulence, and adapted dynamic grid technology. The structure of the ﬂow near and in the 
wake of a drop, the features of the ﬂow around a drop, the type of the shape evolution, and the character 
of the mass entrainment were studied. Comparison of simulation results with experimental data indicates 
good agreement with the main integral characteristics of the process, i.e. morphology, dynamics, and 
induction time of droplet breakup. 
©2 0 2 0 Elsevier Ltd. All rights reserved. 
1. Introduction 
Aerodynamic dispersal of droplets is widely used in various in- 
dustries, such as energy, aircraft, and rocket engine building, hard- 
ening of materials and coatings, chemical industry, etc. Aerody- 
namic mechanisms are the sum of the processes caused by the 
ﬂow around a drop: deformation, the formation of a conjugated 
boundary layer in a liquid, the development of hydrodynamic in- 
stability in it with the participation of the effects of viscosity and 
surface tension of a liquid. Aerodynamic mechanisms are most ef- 
fective in ﬂows with high gradients of parameters, while the inter- 
action of a droplet with pressure jumps and incident shock waves 
(SW) are the extreme examples of gradient ﬂows. The interaction 
of droplets with SW in such technological systems takes place, for 
example, in close proximity to airframe components of the super- 
sonic aircraft Ranger and Nicholls (1969) . Thunderstorm processes 
in the precipitation zone are also accompanied by the movement 
of shock waves in a gas-droplet medium. 
The study of droplets dynamics and breakup in the ﬂow be- 
hind incident SWs holds a special place in the subject of the 
aerodynamic dispersion of liquids by Boiko et al. (1987) and 
Gelfand et al. (1974) , and has developed in two directions since 
∗ Corresponding author. 
E-mail address: tov-andrey@yandex.ru (A.V. Minakov). 
the early works. First, this issue concerns the problems related 
to the combustion of the hydrocarbon fuel aerosols in relation to 
industrial explosion safety by Boiko et al. (1991) , Gelfand et al. 
(1974 , 1978) and to advanced Pulse Detonation Engines (PDE) by 
Dinh et al. (2003) . The process takes place in two stages: ﬁrst, 
droplets breakup behind the SW; and second, ignition of the mix- 
ture and the movement of the ﬂame front over the spray. The risk 
of explosion increases in the case of supersonic ﬂow behind the 
SW front. Here the conditions arise that accelerate the self-ignition 
of the ﬂammable spray —a n increase in gas pressure and temper- 
ature during braking in the tightness created by the suspension by 
Boiko and Poplavski (1993) . 
Since the atomization proceeds identically for all low-viscosity 
liquids, it can be studied in water, which, as noted, is of inde- 
pendent interest by Boiko et al. (1974, 1991) , Gelfand et al. (1974 , 
1978 , 1996) . Thus, the second direction appeared in the study of 
droplet behavior in SW, namely dynamics by Boiko et al. (2007 , 
2009 ), Ranger and Nicholls (1970) , Ortiz et al. (2004) and drop 
breakup mechanisms at a sudden penetration into the ﬂow Boiko 
and Poplavski (2012) , Gelfand et al. (1974 , 1996) , Theofanous and 
Li (2008 ). This became the most popular statement of the prob- 
lem from the experimental standpoint. This is due to the fact 
that the coordinate and the moment of the drop falling into the 
ﬂow are precisely determined only in SW. At that, the visualiza- 
tion of the droplet deformation and the type of its breakup are 
https://doi.org/10.1016/j.ijmultiphaseﬂow.2020.103273 
0301-9322/© 2020 Elsevier Ltd. All rights reserved.

<!-- PDF_PAGE: 2 -->

2 S.V. Poplavski, A.V . Minakov and A .A . Shebeleva et al. / International Journal of Multiphase Flow 127 (2020) 103273 
the most informative to analyze the process itself. There are also 
hidden processes inside the drop that are not observable. How- 
ever, all the ideas about the drop breakup are based only on the 
data on the nature of its deformation before beginning erosion 
of liquid surface and during its progression by Boiko et al. (1987 , 
1991 ), Gelfand et al. (1974 , 1978 , 1996 ). The movement of the liq- 
uid boundary relative to the initial surface of the droplet gives rise 
to the most bizarre shapes in different streamlining regimes due 
to the changing distribution of external pressure. Attempts to es- 
tablish a relationship between the droplet deformation and the 
external ﬂow pattern were made in early works by Ranger and 
Nicholls (1970) though, they were based on an essential simpliﬁ- 
cation of the droplet shape considered as an ellipsoid of rotation 
with a small axis along the velocity vector. This type of deforma- 
tion is possible for raindrop type regimes, i.e. freely falling droplet 
with a diameter of d 0 ~ 2–3 mm and steady velocity of ~ 4–5 m/s. 
Though the deformation type in the ﬂow behind the SW is quite 
different, the model of the conjugated boundary layer formation in 
the liquid, proposed in Ranger and Nicholls (1970) , is still relevant 
for liquid jets, ﬁlms, and droplets Gelfand (1996) . 
Thus, crushing mechanisms are determined by processes on 
both sides of the phase interface. Such problems with the reso- 
lution of the small-scale process are available only for numerical 
methods, and this is an important aspect to motivate computer 
simulation of the process. Veriﬁcation of calculations based on ex- 
perimental data will allow us to debug the numerical technique 
and receive the new data, which are inaccessible in experiments. 
An important task of numerical simulation, for both veriﬁcation 
and research purposes, is the droplet morphology as a response of 
the liquid sphere to the change in the pressure distribution over 
the surface during restructuring the ﬁeld of streamlining of the 
body with changing shape. 
Returning to the experiments, we should note that the possibil- 
ity of detecting a droplet regarding the moment of entering the 
ﬂow behind the SW front made shock tubes the most effective 
tool for this kind of research. That is why the experiments with 
droplets in SW have been repeatedly reproduced in many labo- 
ratories around the world for a wide range of regimes and that 
increases the reliability of the data collected in a number of re- 
views by Gelfand (1996) , Theofanous and Li (2008) . There are also 
unsolved problems associated with the development of innovative 
technologies and the creation of new materials with complex rhe- 
ology. Thus, the interaction of droplets with shock waves is one 
of the fundamental problems of physical gas dynamics within the 
framework of the heat and mass transfer in non-equilibrium het- 
erogeneous systems of technogenic and natural origin, while com- 
puter simulation of these processes is the relevant and promising 
research trend. 
2. Physical mechanisms of the droplet breakup in shock wave 
Aerodynamic breakup modes involving liquid droplets with 
strong relative surface-tension forces are determined by criterion 
established using the Weber number. The Weber number is the ra- 
tio of the disturbing ﬂow force ~ρu 2 d 2 and the stabilizing surface 
tension force ~σd , i.e. We = ρu 2 d/ σ Gelfand et al. (1974 , 1996) , 
where ρand u are the density and velocity of the gas, while d and 
σ are the droplet size and surface tension. There are the following 
six modes of drops breakup according to Gelfand et al. (1974) : vi- 
brational breakup (8 < We < 12) (1), bag breakup (12 < We < 50) 
(2), bag-and-stamen breakup (50 < We < 100) (3), sheet stripping 
(100 < We < 250) (4), wave crest stripping (We > 250) (5), and 
catastrophic breakup (We > 250) (6). 
Other classiﬁcations are also known. They differ in types of 
breakup and range in We numbers Boiko et al. (1987) , Gelfand 
et al. (1974) . For example, in Boiko et al. (1987) it is shown that the 
change of mechanisms 4 and 5 in SW occurs at We ~10 0 0, rather 
than We > 250. The nominal differences between the classiﬁca- 
tions would not be important if they were not related to the rele- 
vant physical mechanisms. The point is that the traditional clas- 
siﬁcations are based on the droplet morphology, but in Gelfand 
(1996) , and later in Theofanous and Li (2008) it is proposed to de- 
ﬁne the droplet breakup types depending on the following physical 
mechanisms. 
1) Types 1–3 are combined into one Rayleigh-Lamb-Taylor in- 
stability mode within the expected range of We numbers, 
10 ≤ We ≤ 40; 
2) Types 4 and 5 represent the sheet stripping from the liquid 
surface layer occurring according to the boundary layer forma- 
tion mechanisms (4) and the development of its instability (5) 
within the expected range of We numbers, 40 ≤ We ≤ 10 5 ; 
3) Type 6 is the catastrophic breakup as a consequence of 
Rayleigh-Lamb-Taylor instability development within the ex- 
pected range of We numbers, 10 3 ≤ We ≤ 10 5 . 
Currently, the numerical simulation of these processes is a 
rather challenging task. Here, the only universal tool is a direct 
numerical simulation (DNS) with full resolution of the phase in- 
terface, but because of the huge computational cost, this approach 
can be used only for a very narrow class of model problems. One 
combined approach that can be considered would include, a tech- 
nique based on a combining the volume of ﬂuid (VOF) method for 
resolving the phase interface, large eddy simulation (LES) mod- 
els for describing turbulent ﬂows, and dynamic grid technology 
adapted to the phase interface. This approach is less demanding 
on computing resources and allows describing the behavior of the 
dynamic gas-liquid interface at the main turbulent scales. How- 
ever, it requires further development and testing for the applica- 
tion in applied problems. The most effective testing of numerical 
technology is conducting simulations in the same conditions as in 
the available experiments, and comparing the results by the max- 
imum number of indicators, such as the following integral quanti- 
tative parameters: 
• droplet deformation rate by Boiko and Poplavski (2007 , 2009 ); 
• the breakup induction period by Boiko and Poplavski (2012) ; 
• This may be the structural characteristics of the process: 
• the deformation scenario and peculiarities of droplet streamlin- 
ing; 
• the type of instability of the droplet surface and the nature of 
the mass entrainment by Boiko and Poplavski (2012) ; 
The numerical simulation technique, veriﬁed by such a set of 
characteristics, will allow using calculations for a wide range of 
applications and to obtain new data that are not available in ex- 
periments. 
3. Experiment statement and analysis of observations 
3.1. Experimental setup and diagnostics 
The experiments were carried out using the UT-4 M shock 
tube (Institute of Theoretic and Applied Mechanics of the Siberian 
Branch, Russian Academy of Sciences), which is described in detail 
in Boiko et al. (1987 , 1991 ). The installation diagram is shown in 
Fig. 1 . The installation is characterized by the following main fea- 
tures: the high-pressure chamber - HPC (1) and the low-pressure 
channel - LPC (2) are coaxial in the ﬁrst section of the channel and 
in the initial state they are separated by a light piston (3), pressed 
against the end of channel 2 by the gas pressure equal to the pres- 
sure in the HPC; to run the installation the solenoid valve (4) re- 
lieves pressure from under the piston by the signal from the syn- 
chronization system (5) and the piston is discarded in position 3 in

<!-- PDF_PAGE: 3 -->

S.V. Poplavski, A.V . Minakov and A .A . Shebeleva et al. / International Journal of Multiphase Flow 127 (2020) 103273 3 
Fig. 1. The installation diagram: 1 - high-pressure chamber; 2 - low-pressure channel; 3 - light piston; 4 - solenoid valve; 5 - sync block; 6 – transition section; 7 - 
measuring section; 8 - quartz windows; 9 - drop entry; 10 –r u b y laser stroboscopic light source; 11 – pressure sensors; 12 - Kerr cell; 13 - camera with a rotating mirror 
prism; 14 - parallel beam system; 15 –m i r r o r s ; 16 - receiving lens. 
less than 0.5 ms, opening the push gas (He) outlet to the channel 2 
over the entire cross section of the latter; the low-pressure channel 
5 m long (inner diameter 58 mm) has a transition section (6) from 
circular section to square one with maintaining the cross-sectional 
area for the smooth connection to the measuring section (7), and 
allows obtaining a quasi-stationary ﬂow behind the shock wave 
front during ~5 0 0–60 0 μs; the measuring section has a square 
cross-section of 52 × 52 mm, equipped with quartz windows (8) 
20 × 200 mm in size to carry out shadow visualization, as well as 
a device for entering freely falling droplets (9). The installation is 
started by the synchronization system when a droplet enters the 
measuring section. The same device also sequentially starts laser 
elements (10) with the arrival of the shock wave front to pressure 
sensors (11) - pump lamps, locking the Kerr cell (12), triggering of 
the stroboscopic mode. Registration is carried out by a multi-frame 
shadow system with a laser stroboscopic light source (10). The fol- 
lowing are some details about the visualization system. 
When registering fast processes, the dynamic spatial-temporal 
resolution is one of the main factors determining the choice of 
recording equipment and its operation mode. Despite the rapid de- 
velopment of electronic image registration, in the study of high- 
speed processes ( V > 10 3 m/s), traditional photography still has 
advantages. In such experiments, optical-mechanical equipment is 
still widely used Versluis (2013) . High-speed shooting ( > 10 3 fps) is 
performed on a static photo material, and the displacement of the 
rays along the photosensitive layer is performed by a scanning sys- 
tem with a rotating mirror or mirror prism. Separation of frames 
on a ﬁlm (image switching) in cameras with a mirror scan of the 
constant light ﬂux is performed using lens inserts. 
The disadvantage of this kind of ﬁlming is the long exposure 
time of the frame τe relative to the interval between frames /Delta1t, 
it is estimated at τe / /Delta1t = 0.5–1.0. To reduce τe , it is necessary to 
increase the shooting frequency. But, for example, at a frequency 
of 625,0 0 0 fps and a frame size of 10 mm τe = 1.6 μs. The ob- 
ject displacement during this time is too large ( > 1 mm). For the 
spatial displacement of the image of the process (or object) at a 
speed of ~1 0 3 m/s not to limit the limiting resolution of the opti- 
cal system R о = 1/d ~2  × 10 4 m −1 , it is necessary to provide an 
exposure time of ~5  × 10 −8 s. This is two orders of magnitude less 
than the minimum shutter speeds for optical-mechanical cameras. 
Therefore, cameras with a mirror scan in the normal ﬁlming mode 
do not provide high-quality registration of high-speed two-phase 
ﬂows. 
A more promising method is one that has an exposure time, 
frequency and number of frames set by a pulsed light source, 
and the optical-mechanical camera performs spatial separation of 
frames. The basic element of such a diagnostic complex is the 
stroboscopic ruby laser light source with periodic Q-switching by 
the Kerr cell developed at the Institute of Theoretic and Applied 
Mathematics (Siberian Branch of the Russian Academy of Sciences). 
Based on this source, various imaging methods are implemented, 
including shadow, schlieren, and other methods Boiko et al. (1997 , 
2002 ); Gavrilenko et al. (1986) with a frame rate of more than 
3 × 10 4 fps and exposure time of 30 ns. 
In this work, we used a shadow scheme with the stroboscopic 
ruby laser as a light source. Laser Q-switching is performed by a 
Kerr cell as an optical shutter (12). Images are recorded onto a 
ﬁne-grained ﬁlm by the camera with a rotating mirror prism (13). 
Rotating prism, unlike a mirror, always reﬂects light into the angu- 
lar sector, on which a 15–20 frames segment of the ﬁlm is located, 
therefore the camera does not need synchronization with the pro- 
cess under study and is called a standby camera. The absence of 
the requirement to synchronize the survey with the shock tube 
start is an important feature of the experiment because the arrival 
of the shock wave front occurs with a spread of > 1 ms from the 
moment the installation is started, but the entire process lasts only 
0.5–0.6 ms. Therefore, the start of the light source is performed 
upon the arrival of the shock wave front into the measuring sec- 
tion at the constant readiness of a recorder with a previously un- 
twisted mirror prism. The interval between frames is 30 ± 0.1 μs 
and the exposures of 30 ns are set by the light source. 
3.2. Flow parameters behind a shock wave front 
Shock waves parameters were calculated by the ideal theory of 
shock waves Henshall (1957) ; Lapworth (1970) , which gives high 
accuracy for Mach numbers of the shock wave МS = V S /c ≤ 4, 
where V S is the velocity of the shock wave front, c is the sound 
velocity in front of it. The value of V s was measured twice: dur- 
ing the experiment, V s was determined to synchronize the instal- 
lation systems over the travel time between pressure sensors with 
an accuracy of 2%; when processing shadow images, V s was de- 
termined from the position of the front on adjacent frames with 
a known interval between them with an accuracy of less 1%. In 
the experiments, the interaction of water droplets with shock wave 
was modeled at We numbers ranged from 200 to 2200. Fig. 2 
shows a series of shadow images of the process at Ms = 1.32, 
We = 2 × 10 3 , d 0 = 2.81 mm. Shock wave moves from left to right, 
the front of the shock wave is visible on frame No. 1, and in the 
previous frame the front coincided with the left edge of the frame. 
Flow parameters behind the wavefront: temperature T 2 = 354 K,

<!-- PDF_PAGE: 4 -->

4 S.V. Poplavski, A.V . Minakov and A .A . Shebeleva et al. / International Journal of Multiphase Flow 127 (2020) 103273 
Fig. 2. Shadow images of the water droplet interaction with incident shock 
wave;We = 2 × 10 3 , the frame spacing 30 × 10 −6 s. 
density ρ2 = 2.0 kg/m 3 , and gas velocity u 2 = 162 m/s. Data from 
other experiments in this series are given in Section 5 . 
3.3. Preliminary observation analysis 
In Ranger and Nicholls (1969) it was proposed to describe the 
droplet dynamics in shock wave in terms of dimensionless quanti- 
ties X = x / d 0 and T = t / t 0 , where x is the longitudinal coordi- 
nate, t is the physical time, t 0 = ( d 0 / u 2 ) •( ρl / ρ2 ) 0.5 . According to 
a series of experiments, a universal dependence for the induction 
period of the mass entrainment was found, t i / t 0 ≈ 0.35 ± 0.04. It 
was also argued that the acceleration of the droplet is constant up 
to T ≈ 6–8; then X ≈ kT 2 . Note that this dependence does not re- 
fer to the mass center of the droplet, but the leading edge. More- 
over, this dependence is quite approximate at the ambiguous in- 
ﬂuence of midsection growth and mass entrainment. Because of 
this, the value of k differs markedly by different authors. Thus, ac- 
cording to Ranger and Nicholls (1969) k = 0.71–1.1, according to 
Ortiz et al. (2004) k = 0.8 –1 . 1 . As shown in Boiko and Poplavski 
(20 07 , 20 09 ), the droplet dynamics are much more complicated, 
the acceleration is not constant, and decreases sharply with the 
development of intense mass entrainment within the range T ≈ 1–
3. 
However, for preliminary analysis, we will also use estimates in 
dimensionless parameters. For conditions on Fig. 2 , t 0 = 387 μs, 
taking into account the residence time of the drop in the ﬂow 
on frame No. 1 (22 μs), the total observation time of the droplet 
t N = 412 μs ( t N / t 0 = 1.05). During this time the droplet has moved 
by the distance x = 2.79 mm ( x / d 0 = 0.99), the coeﬃcient k = 0.9. 
Beginning of mass entrainment is seen on frame No. 5, the breakup 
delay (induction period) is t i = 142 ± 15 μs, while in dimension- 
less form, t i / t 0 = 0.36 that, similarly to coeﬃcient k , is close to 
the accepted data on the interaction of the droplets with the shock 
wave. 
The results of experiments conducted according to this tech- 
nique are published in Boiko et al. (1987 , 1991 , 1987 , 2007 , 2012) . 
Analysis of the above experiment, as well as other experiments 
in this series, shows that in the accepted terms, all modes were 
implemented in the right conditions. They can serve a basis for 
veriﬁcation of numerical technology in terms of both quantitative 
data, and, most importantly, graphical data on the morphology of 
droplet interacting with a shock wave. To date, these data are the 
most detailed of those obtained within the range of We numbers 
200 - 2200, known in the literature. 
4. A numerical model of drop breakup in the ﬂow behind an 
incident shock wave 
The most popular method among the algorithms based on con- 
tinuous volume markers is the volume of ﬂuid (VOF) method 
Hirt and Nichols (1981) due to the ease of implementation and ef- 
ﬁciency, and it proved to be good when calculating the free surface 
ﬂow. The idea of the method is that liquid and gas are considered 
as a single two-component medium, in which the spatial distribu- 
tion of phases within the computational domain is determined by 
a special marker function F(x, y, z, t). The volume fraction of the 
liquid phase in the cell under consideration is taken as follows: 
F(x,y,z,t) = 0, if the cell is empty, F(x,y,z,t) = 1, if the cell is com- 
pletely ﬁlled with liquid, and 0 < F(x,y,z,t) < 1, if the phase inter- 
face is within the cell. Tracking the movement of the free interface 
is performed by solving the transfer equation of the liquid volume 
fraction in the cell since the free surface moves with the liquid: 
dF 
dt 
+ V · ∇ F = 0 , (1) 
where V is the velocity vector of the two-phase medium, found 
from the solution of a system of hydrodynamics equations, i.e. the 
mass conservation or continuity equations: 
dρ
dt 
+ ∇(ρ · V ) = 0 , (2) 
and motion equations or the momentum conservation law: 
dρV 
dt 
+ ∇(ρV × V ) = −∇ p + ∇(τ) + F s (3) 
Here τ is the viscous stress tensor, F S is the volumetric force 
vector, p is the static pressure, ρ is the density of the two-phase 
medium. Components of viscous stress tensor τij are written as: 
τij = μ
(
d U i 
d x j 
+ 
d U j 
d x i 
− 2 
3 
δij 
d U k 
d x k 
)
, (4) 
where μ is the dynamic viscosity of a two-phase medium, U ij are 
the velocity vector components. The density and molecular viscos- 
ity of the considered two-component medium are found through

<!-- PDF_PAGE: 5 -->

S.V. Poplavski, A.V . Minakov and A .A . Shebeleva et al. / International Journal of Multiphase Flow 127 (2020) 103273 5 
Fig. 3. . The computational grid near the phase interface using gradient adaptation for the basic mesh (a) and (b) ﬁne mesh. 
the volume fraction of the liquid in the cell according to the mix- 
ture rule: 
ρ = ρ1 F + (1 − F ) ρ2 , (5) 
μ = μ1 F + (1 − F ) μ2 , (6) 
where ρ1 and μ1 are the density and viscosity of the liquid, ρ2 
and μ2 are the density and viscosity of the gas. The obtained 
values of density ρ and viscosity μ are included in the motion 
equations and determine the physical properties of the two-phase 
medium. 
Special attention is paid to the surface tension phenomenon 
when considering ﬂuid ﬂows with a free interface. The study of the 
ﬂows driven by the surface tension forces is a very complex inde- 
pendent task. Therefore, the advantages of the volume of the ﬂuid 
method also include the fact that it allows a relatively simple sim- 
ulation of the effect of surface tension forces. Most often, the con- 
tinuous surface force (CSF) algorithm Brackbill et al. (1992) is used 
to simulate the surface tension in the framework of the volume of 
ﬂuid method, which involves the introduction of an additional vol- 
umetric force, F S into the motion equations, which is determined 
from the correlation: 
F s = σk ∇ F (7) 
where σ is the surface tension coeﬃcient, k is the curvature of 
the free surface, which is deﬁned as the divergence of the normal 
vector: 
k = ∇ 
(
n 
| n | 
)
, (8) 
The normal to the free surface is calculated in its turn as the 
gradient of the volume fraction of the liquid phase in the cell: 
n = ∇ F , (9) 
The simulation of turbulence is another important factor when 
calculating droplet breakup. The development of instabilities and 
turbulence play a key role in the deformation of droplets when 
interacting with a shock wave. Estimates show that the Reynolds 
number during the ﬂow around a drop varies from about 30,0 0 0 to 
70,0 0 0. This corresponds to a turbulent regime. In this paper, we 
used the large eddy simulation (LES) model ( Smagorinsky, 1963) 
for turbulence modeling, according to which the solution of ﬁltered 
Navier-Stokes equations is necessary to describe turbulent ﬂows. 
This model, in this case, is optimal. The use of RANS (Reynolds- 
averaged Navier–Stokes) models gives only averaged characteristics 
of ﬂow and does not correctly describe the development of insta- 
bility in the interaction of a drop with a shock wave. The numerical 
estimates of the Kolmogorov scale for this problem show, that for 
the application of DNS (direct numerical simulation) it is necessary 
to use computational grids with the number of cells over 100 mil- 
lion. Using the large eddy simulation model allowed us to correctly 
use grids with details of 15–25 million nodes. 
Then, the above-mentioned system of hydrodynamics equations 
can be rewritten in the following form: 
− continuity equation: 
∂ρ
∂t 
+ 
∂ 
∂ x i 
( ρ¯u i ) = 0 , (10) 
− momentum conservation equations 
∂ 
∂t 
( ρ¯u i ) + 
∂ 
∂ x j 
(ρ¯u i ¯u j 
)
= 
∂ 
∂ x j 
(
μ∂ σij 
∂ x j 
)
− ∂ ¯ρ
∂ x i 
− ∂ τij 
∂ x j 
, (11) 
where σi, j is the viscous stress tensor, whose components have 
the form: 
σij = 
[
μ
( ∂ ¯u i 
∂ x j 
+ 
∂ ¯u j 
∂ x i 
)]
− 2 
3 
μ∂ ¯u i 
∂ x i 
δij , (12) 
where μi s the molecular viscosity. 
Tensor τi,j is called a subgrid stress tensor, and its components 
are determined by analogy with RANS models from the Boussinesq 
approximation: 
τij − 1 
3 
τkk δij = −2 μt ¯S ij , (13) 
Here ¯S i, j is strain velocity tensor: 
¯S ij = 
1 
2 
( ∂ ¯u i 
∂ x j 
+ 
∂ ¯u j 
∂ x i 
)
, (14) 
The value μt is called the subgrid viscosity. We used the sub- 
grid viscosity model in this paper proposed by Smagorinsky: 
μt = ρL 2 
S 
⏐⏐¯S 
⏐⏐, 
⏐
⏐
¯S 
⏐⏐ ≡
√ 
2 ¯S ij ¯S ij , (15) 
where L S is mixing length of subgrid scales: L S = min (kd, C S V 
1 / 3 )

<!-- PDF_PAGE: 6 -->

6 S.V. Poplavski, A.V . Minakov and A .A . Shebeleva et al. / International Journal of Multiphase Flow 127 (2020) 103273 
Fig. 4. Numerical simulation of the water drop behavior behind the incident shock wave at We = 208; (a) period up to 520 μs, (b) period of 550–900 μs. 
Here k is Karman constant, d is the distance to the nearest wall, 
V is the volume of the computational cell, C S is the Smagorinsky 
constant. C S = 0 . 17 in the present paper. 
The energy conservation equation for a compressible gas is con- 
sidered as follows: 
∂ρE 
∂t 
+ ∇ ( ρv (E + p/ρ) ) = ∇ 
(λef f  ∇ T 
)
, (16) 
E is the total energy here, which is deﬁned as: 
E = h − p/ρ+ v 2 / 2 , (17) 
In this case, the enthalpy is calculated as: 
h = 
T ∫ 
T 0 
C p ( T ) dT (18) 
λef f  = λ+ λt –t h e coeﬃcient of thermal conductivity of the mix- 
ture, λt = μt C p 
Pr t . Pr t is the turbulent Prandtl number equal to 0.85. 
Here the of thermal conductivity and heat capacity are found 
through the volume fraction of the liquid in the cell according to 
the mixture rule: 
λ( T ) = λ1 ( T ) F + ( 1 − F ) λ2 ( T ) (19) 
C p ( T ) = C p1 ( T ) F + ( 1 − F ) · C p2 ( T ) (20) 
where λ1 and С p 1 are the thermal conductivity and heat capacity 
of the liquid, λ2 and С p 2 are the thermal conductivity and heat 
capacity of the gas. 
The methodology of solving Eqs. (1) –(9) and the main features 
of numerical studies are described by Minakov et al. (2012 , 2015 ). 
The difference analog of the convective-diffusion equations was 
found using the ﬁnite volume method for structured multi-block 
grids, whose application ensured the persistence of the obtained 
scheme. The central difference scheme of second-order was used 
to approximate convective terms of the hydrodynamics Eq. (3) . An 
implicit ﬁrst-order scheme was employed to approximate the un-

<!-- PDF_PAGE: 7 -->

S.V. Poplavski, A.V . Minakov and A .A . Shebeleva et al. / International Journal of Multiphase Flow 127 (2020) 103273 7 
Fig. 5. Comparison of calculation with experimental data on the droplet shape at We = 208; (a) 240 μs; (b) 360 μs; (c) 420 μs. 
Fig. 6. The transverse deformation rate of a water drop at We = 208 for basic and 
ﬁne computation mesh. 
steady terms of the hydrodynamic equations. Diffusion ﬂuxes and 
source terms were approximated with a second order of accu- 
racy. The connection between the velocity and pressure ﬁelds was 
realized by SIMPLEC (Semi-Implicit Method for Pressure Linked 
Equations-Consistent) procedure on the combined grids. This ap- 
proach made it possible to overcome the described above diﬃcul- 
ties with the resolution of the mobile phase interface. The result- 
ing system of the ﬁnite-difference equation was solved by an itera- 
tive method using a multigrid solver. The staggered grids with the 
PRESTO! discretization scheme for pressure were used. PRESTO! 
discretization gives more accurate results since interpolation errors 
and pressure gradient assumptions on boundaries are avoided. This 
scheme works better for problems with strong body forces (sur- 
face tension) and high-density ratio. The time step is controlled by 
a speciﬁed maximum value for the CFL (Courant–Friedrichs–Lewy), 
CFL = τV/h, where τ, h, and V are the time step, grid size, and 
ﬂuid velocity respectively. A very high CFL value leads to an unsta- 
ble numerical approach while a low CFL value means very small 
time steps and consequently long simulation times. A maximum 
CFL of 2 was adopted in this work. A typical value of the time step 
depending on the ﬂow regime was from 10 −6 to 10 −8 s. The con- 
vergence criteria for velocities and pressure were set to 0.001. The 
absolute values of residuals achieved were found to be suﬃciently 
low, O(10 −7 ) for velocities and O(10 −9 ) for pressure equations. 
The simulation of water droplet breakup in the ﬂow behind the 
shock wave was carried out for different Weber numbers within 
the range of 208 ≤ We ≤ 2260. The calculated area was a par- 
allelepiped with dimensions of 3 × 3 × 5 cm using the described 
technique. The inlet condition with ﬁxed velocity was set on one of 
the faces of the parallelepiped, determined from the Weber num- 
ber. Free exit conditions were set on the other faces of the compu- 
tational domain. A spherical water droplet with a diameter d 0 ~2 –
3 mm was placed at a distance of 5 mm from the inlet to the com- 
putation domain at the initial time point. The droplet was affected 
by the passing shock wave generating the air ﬂow. 
The Cartesian computational grids were used in the calcula- 
tions. For the basic mesh, the total number of grid cells was 6.5 
million. For detailed mesh, the total number of grid cells was about 
13.8 million. In addition to each mesh, the gradient adaptation 
technology was applied. The grid is automatically concentrated in 
the area of large solution gradients with this technology in the 
course of calculations. The gradient of the liquid volume fraction 
was chosen as the control parameter. An example of how the orig- 
inal grid changes during gradient adaptation for a ﬂow velocity of 
60 m/s for basic and ﬁne mesh is shown in Fig. 3 . The total num- 
ber of computational nodes of the optimized grid in the course of 
calculation was approaching 25 million for basic mesh and 47 mil- 
lion for the ﬁne mesh. A comparison of the calculations obtained 
on the basic and detailed grids showed that the results are in good 
agreement with each other and experiment (see Fig. 6 ). Therefore, 
for further calculations, a basic mesh with gradient adaptation was

<!-- PDF_PAGE: 8 -->

8 S.V. Poplavski, A.V . Minakov and A .A . Shebeleva et al. / International Journal of Multiphase Flow 127 (2020) 103273 
Fig. 7. The breakup of water droplets behind the shock wave at Ms = 1.144, We = 360. 
Fig. 8. Comparison of calculation results with experimental data for We = 360 at the following time points: 120 μs (a), 300 μs (b), 390 μs (c). 
chosen. A comparison of the data with the experiments showed 
that such detailing of the mesh is suﬃcient. 
5. Simulation results and comparison with experiments 
The following physical properties of the phases were used in 
the calculations: water density and viscosity 998.2 kg/m 3 and 
1.003 × 10 −3 kg/m •s, surface tension coeﬃcient σ = 0.073 N/m; 
and air viscosity 1.789 × 10 −5 kg/m •s. The ﬂow velocity varied 
from 60 to 170 m/s to simulate the ﬂow regimes within the range 
208 ≤ We ≤ 2260. The ideal gas model was used. 
Fig. 4 shows an example of simulating the behavior of a wa- 
ter drop in the ﬂow at We = 208, the Mach number of the 
shock wave Ms = 1.109, drop size d 0 = 2.73 mm, gas velocity 
and density u 2 = 60 m/s, ρ2 = 1.53 kg/m 3 , and the time constant 
t 0 = ( d 0 / u 2 ) •( ρl / ρ2 ) 0.5 ≈ 1170 μs. Fig. 4 a corresponds to the pe- 
riod of drop’s stay behind the shock wave t N = 520 μs, as it was in 
the experiment, while Fig. 4 b shows the possible evolution of the 
drop during the time up to 900 μs as if the quasi-stationary ﬂow 
behind the shock wave existed for long. 
A comparison of the calculation with the experiment at sim- 
ilar points in time is shown in Fig. 5 . As can be seen, there is 
a good qualitative agreement with photographs from the experi- 
mental data, as in terms of the droplet shape, as in terms of its 
deformation dynamics. In addition to the external similarity of the 
droplet shape, there is a quantitative index of deformation that af- 
fects its dynamics, namely, the growth of the droplet cross-section. 
The dynamics of the droplet midsection growth ( d / d 0 - the ratio 
of the current transverse droplet size to the initial one) is shown 
in Fig. 6 , where a satisfactory agreement between the mean defor- 
mation rate in the experiment and calculations is shown. 
Fig. 7 shows the simulation result of water droplets interac- 
tion with shock wave at We = 360, Ms = 1.144, droplet size 
d 0 = 2.7 mm, gas velocity u 2 = 77 m/s, density ρ2 = 1.53 kg/m 3 , 
time constant t 0 ≈ 865 μs, the droplet residence time in the ﬂow 
t N = 440 μs (T N = t N / t 0 = 0.47). The beginning of mass en- 
trainment is observed on frames No. 9–10 both in the experi- 
ment and the calculations ( Fig. 8 , b), the breakup induction period 
t i ≈ 300 mks, T i = t i / t 0 = 0.35. 
As can be seen, there is a good qualitative agreement between 
the numerical simulation and the experimental data at similar 
time points, but it should not be expected the complete coinci- 
dence of calculations with experiment at a late stage of the pro- 
cess, shown in Fig. 8 c. The point is that there are circumstantial 
factors in the experiment that are diﬃcult to take into account in 
the calculations. First of all, this concerns the nonsphericity of the 
droplet due to ﬂuctuations during the separation from the capil- 
lary. Here the general picture and rate of deformation are more im- 
portant since they inﬂuence the induction period and the nature of 
the mass entrainment. The calculated data well describe not only

<!-- PDF_PAGE: 9 -->

S.V. Poplavski, A.V . Minakov and A .A . Shebeleva et al. / International Journal of Multiphase Flow 127 (2020) 103273 9 
Fig. 9. The water droplet deformation rate at We = 360. 
the average deformation rate but also the wave microstructure of 
the process as it is seen from Fig. 9 . 
The simulation results of the water droplets interaction with 
shock wave at We = 650 are shown in Fig. 10 . This is imple- 
mented at a Mach number of the shock wave Ms = 1.19, gas veloc- 
ity behind the shock wave front 101 m/s, density ρ2 = 1.71 kg/m 3 , 
the time constant t 0 = 657 μs for a droplet with d 0 = 2.73 mm. 
The observation time is t N = 435 μs when the number of frames 
N = 15, while the dimensionless value of T N = t N / t 0 = 0.75 cor- 
responds to the double period induction of mass entertainment. 
That means that the beginning of the mass entrainment should be 
sought on frames No. 7–8, while the time of breakup induction 
t i ≈ 210–240 μs, T i = t i / t 0 = 0.35. 
The possibility of observing the later stage of the process 
(T N = 0.75) allows to see one more feature, namely, the transverse 
stretching of the ﬁlm at the ﬂat bottom of the drop on frames No. 
7–8, which later becomes the mass entrainment ( Fig. 11 c). This 
also happens with the number We = 360, though not so pro- 
nouncedly. The limited observation time T N did not allow observ- 
ing mass entrainment in general in the experiments at We = 208 
and in the bottom region of the droplet in particular. A compari- 
son of the calculation results with the experimental data obtained 
at the We = 650 is shown in Fig. 11 , and it is indicative of good 
qualitative agreement between the simulation results and exper- 
imental data at the characteristic stages of the process in terms 
of droplet shape. The growth rate of the transverse size of the 
droplet in Fig. 12 also shows good quantitative agreement with 
the experiment. It is important to note that not only the average 
growth rates are close to each other, but similarly, the phases of 
surface waves coming to the periphery of the drop coincide as at 
We = 360. They can be seen by the non-monotonic nature of the 
growth of the midsection. 
Fig. 13 shows the numerical simulation result of the interaction 
of water droplet of d 0 = 2.79 mm with shock wave at We = 2260. 
This mode is implemented at the Mach number of the shock 
wave Ms = 1.34, the ﬂow velocity behind the shock wave front 
u 2 = 170 m/s, and the density ρ2 = 2.04 kg/m 3 . In this experi- 
ment, the time constant t 0 ≈ 362 μs, the beginning of the liquid 
breakdown falls within the interval between frames No. 5 and 6, 
i.e. the induction period t i ≈ 135 μs, T i = t i / t 0 = 0.37. 
Fig. 14 presents a comparison of the calculation with the exper- 
iment on droplet shape, which is quite satisfactory as it is seen. It 
is also seen that microdroplets are observed in front of the wind- 
ward surface of the mother droplet at the beginning of the mass 
entrainment ( Fig. 14 b), excluding only the area near the critical 
point. This fact deserves special attention and will be discussed in 
the next section since this type of breakup is signiﬁcantly different 
from the modes at We = 360 and 650, where stripping of the liq- 
uid ﬁlm occurs in the midsection plane and the bottom region of 
the drop. 
Fig. 10. The behavior of the water droplet behind incident shock wave at Ms = 1.19, We = 650.

<!-- PDF_PAGE: 10 -->

10 S.V. Poplavski, A.V . Minakov and A .A . Shebeleva et al. / International Journal of Multiphase Flow 127 (2020) 103273 
Fig. 11. Comparison of the droplet shape in the calculation and experiment at We = 650; (a) 120 μs; (b) 150 μs; (c) 240 μs; (d) 390 μs. 
Fig. 12. The deformation rate of water droplet behind the shock wave at We = 650. 
A comparison of the lateral deformation rate of a droplet in the 
calculations and the experiment in this mode has shown a good 
agreement up to the interaction time between 100 and 120 mi- 
croseconds. The uncertainty of the drop border against the back- 
ground of a dense spray does not allow to correctly determine the 
size of an integral part of the drop in shadow shots and to verify 
the calculations by the strain rate at the stage of developed mass 
breakdown. 
6. Results and discussion 
Table 1 shows the gas-dynamic and other characteristics of the 
regimes considered, two of which deserve special attention. First, 
it is the breakup induction period t i , because it is one of the quan- 
titative indicators to compare calculations with experiments, and 
secondly, it is the time constant t 0 = ( d 0 / u 2 ) •( ρl / ρ2 ) 0.5 as a 
generalized parameter of the mode of the drop - gas interaction. 
The peculiarity of the experiments in shock tubes is the lim- 
itation of the observation time t N due to the limited duration of 
the quasi-stationary ﬂow behind the shock wave, in present exper- 
iments t N ≈ 50 0–60 0 μs. The Table shows that the dimensionless 
time T N = t N / t 0 increases and covers progressively the later stages 
of the process with the increase in the Weber number, but the 
observation time appeared to be insuﬃcient to detect the droplet 
breakup in the mode with We = 208. Therefore, the "observation" 
time was extended to 900 μs in the calculations ( Fig. 4 b). The time 
t i ≈ 600 μs is obtained from the calculated "visualization", while 
the dimensionless time T i = t i / t 0 appears to be slightly overstated 
in comparison with other modes. This is due to the fact that the 
regime with We ≈200 is in the transition region between Rayleigh- 
Taylor instability and stripping mechanisms, while the breakup de- 
lay increases and reaches the value of T i ≈ 2 at We < 200 by Dai 
et al. ( 2001 ). The transition region is characterized by the simulta- 
neous development of several breakup mechanisms, and thus the 
process is called a mixed or multimode regime Dai et al. ( 2001 ). 
This type of deformation is typical for the “sheet stripping” mecha- 
nism at an early stage of interaction ( Fig. 4 a) and the development 
of Rayleigh-Taylor waves at a late stage ( Fig. 4 b) in this example. 
As for the other modes, the calculations have shown a good 
agreement between the induction period t i and the experiments. 
The dimensionless induction time is independent of the We num-

<!-- PDF_PAGE: 11 -->

S.V. Poplavski, A.V . Minakov and A .A . Shebeleva et al. / International Journal of Multiphase Flow 127 (2020) 103273 11 
Table. 1 
The characteristic parameters of regimes. 
We MS u 2 , m/s ρ2 , kg/m 3 t 0 , μs T N = t N / t 0 t i , μs T i = t i / t 0 
208 1.109 59.8 1.53 1168 0.4 600 0.5 
360 1.144 77.9 1.61 865 0.47 330 0.36 
653 1.19 101 1.71 657 0.96 220 0.35 
2000 1.32 162 2.0 387 1 142 0.36 
2260 1.34 170 2.04 362 1 135 0.37 
Fig. 13. Water droplet breakup dynamics behind the shock wave at We = 2260. 
Fig. 14. Comparison of calculation with experiment in the form of drop at We = 2260; (a) 60 μs, (b) 90 μs, (c) 270 μs.

<!-- PDF_PAGE: 12 -->

12 S.V. Poplavski, A.V . Minakov and A .A . Shebeleva et al. / International Journal of Multiphase Flow 127 (2020) 103273 
Fig. 15. The ﬂow ﬁeld near a drop and in its wake at different time points, We = 208;1 – toroidal vortex in the ﬂow separation region; 2 – solitary toroidal vortex;3 –
return ﬂow near the wake axis; 4 –f r a c t u r e of generatrix at the point of ﬂow separation; 5 –f r a c t u r e of generatrix in the bottom of the drop. 
ber and equals to T i = const ≈ 0.36. Then, an empirical formula 
can be used t i = 0.36 •(d 0 / u 2 ) •( ρl / ρ2 ) 0. 5 for estimates of the 
drop breakup delay at We > 250, the velocity u 2 and density ρ2 
of the gas is computed as a function of Mach number of the shock 
wave Ms in Henshall (1957) ; Lapworth (1970) . 
The second quantitative factor to verify the calculation is de- 
formation dynamics. The average growth rate of the drops mid- 
section is very close in calculations and experiments, and its non- 
monotonic character is noted. In Boiko et al. (2012) this was ex- 
plained by the arrival of concentric surface waves to the equator 
of a droplet, though there is a divergence of the wave phase at 
We = 208 ( Fig. 6 ). This may be due to the initial non-sphericity of 
the droplet at the time of impact by the shock wave. The phases 
of surface waves in the calculations and experiments coincide with 
high accuracy in other modes ( Figs. 9 and 12 ). Thus, the compari- 
son of numerical simulation with the experiment has shown good 
agreement in terms of the droplet shape, deformation dynamics, 
and breakup delay that indicates a high-resolution capability of the 
computational algorithm. 
Taking into account the time of complete breakup of the droplet 
t / t 0 = Т ≈ 5 by Gelfand et al. (1974) ; Dai and Faeth (2001) we 
note that in this paper, only the early stage (T i < T N < Т ) is consid- 
ered, though it is very important for understanding the processes 
occurring inside and outside the droplet. Although the problem 
of internal processes is not set here, it is useful to highlight the 
main issues: these are "macroscopic" movement of the liquid dur- 
ing drop deformation, the development of the conjugated bound- 
ary layer, and surface instability. These are hidden processes that 
are not observable and can be judged only indirectly by the nature 
of the drop deformation and picture of it ﬂow around. 
The relationship between the droplet shape and the stream- 
lining pattern is seen in the response of the liquid sphere to the 
change in the velocity ﬁeld near it. That is, a general picture of 
the ﬂow pattern is necessary to understand the evolution of the

<!-- PDF_PAGE: 13 -->

S.V. Poplavski, A.V . Minakov and A .A . Shebeleva et al. / International Journal of Multiphase Flow 127 (2020) 103273 13 
Fig. 16. The ﬂow ﬁeld near and in the wake of a drop at different time points for We = 2260; 1 – toroidal vortex in the ﬂow separation region, 2 – solitary toroidal vortex, 
3 –r e v e r s e ﬂow near the wake axis. 
droplet shape, but panoramic methods of velocity measurements, 
such for example, PIV, are not applicable in shock tube because of 
the operation speed limitation. Therefore, experiments were car- 
ried out in Boiko et al. (2012) with the droplet model in a sta- 
tionary ﬂow at the Reynolds number Re ~1 0 3 –10 4 , equal to that 
in a shock wave. The model had the shape typical to one at the 
initial stage of droplet breakdown ( Figs. 5 b, 8 b, 11 b, and 14 b). The 
features of the ﬂow around such a body will be considered later 
according to PIV data, while here we will focus on the ﬁrst impor- 
tant results of numerical simulation of the ﬂow around the drop at 
different stages of its shape evolution. 
The ﬂow pattern for the mode in Fig. 4 is shown in Fig. 15 for 
We = 208. When the droplet is slightly deformed, the ﬂow around 
it is close to the ﬂow around the sphere at the corresponding 
Reynolds numbers ( Re ~1 0 3 –10 4 ) with a vortex separation near the 
midsection (1). Then, 200 μs after a drop enters the ﬂow, a toroidal 
vortex (2) and a reverse ﬂow (3) are formed simultaneously with 
the generation of two annular waves (4) and (5) on the initially 
spherical droplet. This type of deformation is typical for the entire 
investigated range of Weber numbers. The analysis of the gas ve- 
locity ﬁeld, performed in Boiko et al. (2012) , revealed the features 
of the ﬂow around such a body, which are given below, and it re- 
mains to be noted that all of them can be traced in the results of 
numerical simulation ( Fig. 15 ). 
Thus, the external ﬂow is unsteady, but it contains several con- 
stant gas-dynamic structures, whose behavior and their effect on 
the drop can be interpreted as follows: 
• The ﬁrst higher wave - the generatrix bend (generatrix is the 
curve formed by the intersection of the secant plane with the 
surface of an axisymmetric body to its axis) is generated even 
at the spherical shape of the droplet at the point of ﬂow sep- 
aration, where its velocity is maximal (red region), while the 
pressure is minimal. The recirculation zone with a counter- 
current ﬂow along the droplet surface (area 1 ) is visible behind 
the separation point. The liquid moves to the drop equator in 
the conjugated boundary layer (the boundary layer in the liq- 
uid adjacent to the boundary layer in the gas) that contributes 
to the growth of the ﬁrst wave along with local decreased pres- 
sure above it. 
• The second stationary structure is in the droplet wake and rep- 
resents a second recirculation zone with the intense reverse 
ﬂow along the wake axis (area 3 ). The pressure distribution in 
the bottom of the droplet caused by this impact ﬂow makes 
the surface ﬂat and the nature of the gas movement is radial 
spreading over the bottom surface. 
• The second fracture of the generatrix is formed here, which is 
associated with the radial spreading of the liquid over the bot- 
tom surface. This leads to the formation of a liquid disk as can 
be seen in Figs. 7 , 10 , and 13 , whose edge supplies the droplet 
crushing products to the aerodynamic wake. 
• The gas ﬂow is separated near the second wave ( 5 ) spread- 
ing radially over the bottom surface. At that, part of it pene- 
trates into the ﬁrst separation zone ( 1 ) along the droplet sur- 
face, while the rest of the ﬂow enters the third permanent 
structure ( 2 ) ( Fig. 16 ). 
• The structure ( 2 ) is an isolated toroidal vortex and partially sep- 
arates the ﬁrst two ones. It originates at its bottom part and 
drifts into the aerodynamic track at a speed much less than 
the speed of the oncoming ﬂow without interacting with the 
droplet surface.

<!-- PDF_PAGE: 14 -->

14 S.V. Poplavski, A.V . Minakov and A .A . Shebeleva et al. / International Journal of Multiphase Flow 127 (2020) 103273 
• Comparison of shadow images of the droplet at the beginning 
of the breakup with the external ﬂow ﬁeld has shown that the 
mass breakdown occurs from the wave crests, i.e. annular frac- 
tures of the generatrix, while they are formed at the ﬂow sep- 
aration points ( 4 ) and ( 5 ) shown in Fig. 14 . 
This type of drop breakup corresponds to the “sheet strip- 
ping” mechanism, and its features are visible at the modes with 
We = 208, 360, and 650. The droplet morphology is similar to 
the previous examples in the modes with We > 20 0 0, but the 
mass breakdown occurs not only from the edges of the two main 
waves. The presence of breakup products in front of the windward 
surface of the droplet was noted at We = 2260 ( Fig. 14b ). These 
daughter droplets originated due to the wave crest stripping as 
well, though waves were of a different scale and nature. These are 
Kelvin-Helmholtz instability waves on the windward surface of the 
droplet. Perhaps the attributes of their stripping shown in Fig. 14 b 
are the only evidence of the change in breakup mechanism within 
this range of modes described in Boiko et al. (2012 ) and obtained 
in the calculations. Note also that the restriction of the grid size (~
20 μm) does not allow resolving smaller daughter droplets, other- 
wise there would be substantially more of them. 
Fig. 16 presents the calculated velocity ﬁeld near the droplet 
at We = 2260, from which the same structures are visible as at 
We = 208, namely, the ﬂow separation region ( 1 ) at the point with 
maximum velocity (red region) and minimum pressure, an isolated 
solitary toroidal vortex ( 2 ), and the reverse ﬂow on the wake axis 
( 3 ). A scheme of the bottom ﬂow separation into two vortices ( 1 ) 
and ( 2 ) is shown at the time point equal to 70 μs, as was described 
earlier in Boiko et al. (2012) for the solid model. The signs of struc- 
tures (1) and (2) are visible until the interaction time ≈ 120 μs, 
and further, the ﬂow in the wake loses its axial symmetry and dis- 
integrates into small non-stationary structures. They form a large 
stagnant area with a low average velocity comparable to the veloc- 
ity in the ﬂow deceleration zone in front of the windward surface 
of the drop. 
And ﬁnally, the last remark is that the external current lines 
are closed in the far wake of the drop at a greater distance than 
that of the sphere since they cover not only the drop itself but 
also the extensive vortex structures provoked by the breaks of the 
generatrix on the deformable surface. This can be seen in Fig. 16 of 
the ﬂow ﬁeld at instants of 32 μs and 70 μs. Thus, the results 
of the ﬂow ﬁeld simulation near a deformable drop are in many 
ways consistent with the PIV data for a solid model with a similar 
shape and advance in understanding an overall picture of the drop 
behavior in the shock wave and hidden processes inside it. 
Conclusions 
The complex of experimental data and numerical simulation re- 
sults provided the basis for constructing a phenomenological pic- 
ture of water drop behavior in the ﬂow behind the incident shock 
wave. 
1. Experimental and numerical study of the behavior of water 
drops in a ﬂow behind incident shock wave at Weber num- 
ber We = 208–2260 was carried out to verify the mathemati- 
cal model of process and obtain new data based on two ap- 
proaches. 
2. Comparison of calculations performed for real-world experi- 
mental conditions with detailed cinema patterns of the process 
with 30 μs intervals between frames showed high eﬃciency of 
numerical technology to predicting general picture of deforma- 
tion and drop breakup, as well as quantitative characteristics 
of the process. The agreement between calculations and exper- 
iments was established with an accuracy of no worse than 10% 
in all modes. 
3. For the ﬁrst time, a joint analysis of the nature of the deforma- 
tion of the moving surface of the droplet and changing ﬁeld 
of gas ﬂow near it and in its wake was carried out. A sys- 
tem of quasistationary toroidal vortices in gas was discovered 
and it was shown that their position correlates with separation 
zones of gas ﬂow on a droplet at different stages of its defor- 
mation and with the growth of two ring waves on its surface. 
Sharp crests of these waves are centers of erosion and sources 
of spray into the aerodynamic wake of drop at Weber number 
We > 200. 
4. In regime with a Weber number We ≥ 20 0 0, in addition to 
these centers of liquid disruption, calculations show for the ﬁrst 
time the presence of a spray in front of the windward surface 
of drop, which indicates development of small waves here by 
the Kelvin-Helmholtz instability of shear ﬂow in the conjugate 
boundary layer in drop - the “wave crest stripping". 
Decalartion of Competing Intersts 
None. 
CRediT authorship contribution statement 
Sergey V. Poplavski: Conceptualization, Investigation, Writing - 
original draft, Writing - review & editing. Andrey V. Minakov: Con- 
ceptualization, Investigation, Writing - original draft, Formal anal- 
ysis, Writing - review & editing. Anna A. Shebeleva: Investigation, 
Validation, Visualization. Viktor M. Boyko: Investigation, Method- 
ology, Formal analysis, Writing - review & editing. 
Acknowledgments 
The experimental research was carried out within the frame- 
work of the Program of Fundamental Scientiﬁc Research of the 
state academies of sciences in 2013–2020 (project No. АААА- А17- 
117030610137-0 ). The numerical study partly supported by RFBR 
(project No. 18-38-00565 ) and Russian Science Foundation (project 
No. 19-79-30075 ). 
Supplementary materials 
Supplementary material associated with this article can be 
found, in the online version, at doi: 10.1016/j.ijmultiphaseﬂow.2020. 
103273 . 
References 
Boiko, V.M. , Kiselev, V.P. , Kiselev, S.P. , Papyrin, A.N. , Poplavsky, S.V. , Fomin, V.M. , 
1997. Shock wave interaction with a cloud of particles. Shock Waves 7, 275–285 . 
Boiko, V.M. , Lotov, V.V. , Papyrin, A.N. , 1991. Ignition of liquid fuel drops in shock 
waves. Dynamics of deﬂagrations and reactive systems: heterogeneous combus- 
tion. Progress Astron. Aeron. 132, 205–219 . 
Boiko, V.M. , Papyrin, A.N. , Poplavski, S.V. ,1 9 8 7 . Dynamics of droplet breakup in 
shock waves. J. Appl. Mech. Tech. Phys. 28 (2), 263–269 . 
Boiko, V.M. , Papyrin, A.N. , Poplavski, S.V. , 1993. Mechanism of dust ignition in inci- 
dent shock waves. Combust. Explos. Shock Waves 29 (3), 389–394 . 
Boiko, V.M., Poplavski, S.V., 2012. Experimental study of two types of stripping 
breakup of a drop in the ﬂow behind the shock wave. Combust. Explos. Shock 
Waves 48 (4), 4 40–4 45. doi: 10.1134/S0010508212040107 . 
Boiko, V.M., Poplavski, S.V., 2009. On the dynamics of droplet acceleration at the 
early stage of velocity relaxation in the shock wave. Combust. Explos. Shock 
Waves 45 (2), 198–204. doi: 10.1007/s10573- 009- 0026- 4 . 
Boiko, V.M., Poplavskii, S.V., 2007. Particle and drop dynamics in the ﬂow behind a 
shock wave. Fluid Dyn. 42 (3), 433–441. doi: 10.1134/S0015462807030118 . 
Boiko, V.M. , Poplavski, S.V. , 2002. Self-ignition and ignition of aluminum powders 
in shock waves. Shock Waves 11, 289–295 . 
Brackbill, J.U., Kothe, D.B., Zemach, C.A., 1992. Continuum method for modeling sur- 
face tension. J. Comput. Phys. 100, 335–354. doi: 10.1016/0021- 9991(92)90240- Y . 
Dai, Z., Faeth, G.M., 2001. Temporal properties of secondary drop breakup in the 
multimode breakup regime. Int. J. Multiphase Flow 27, 217–236. doi: 10.1016/ 
S0301-9322(0 0)0 0 015-X .

<!-- PDF_PAGE: 15 -->

S.V. Poplavski, A.V . Minakov and A .A . Shebeleva et al. / International Journal of Multiphase Flow 127 (2020) 103273 15 
Dinh, T.N., Li, G.J., Theofanous, T.G., 2003. An investigation of droplet breakup in a 
high Mach, low Weber number regime. In: 41st AIAA Aerospace Sciences Meet- 
ing and Exhibit. Reno, NV, pp. 6–9. doi: 10.2514/6.2003-317 January. 
Gavrilenko, T.P. , Grigoriev, V.V. , Zhdan, S.A. , Nicolaev, Y.A. , Boiko, V.M. , Papyrin, A.N. , 
1986. Acceleration of solid particles by gaseous detonation products. Combust. 
Flames. 66 (2), 121–128 . 
Gelfand, B.E., 1996. Droplet breakup phenomena in ﬂows with velocity lag. Progr. 
Energy Combust. Sci. 22 (3), 201–265. doi: 10.1016/S0360-1285(96)0 0 0 05-6 . 
Gelfand, B.E. , Gubin, S.A. , Kogarko, S.M. , 1974. Main modes of droplet breakup in 
shock waves and their characteristics. J. Eng. Phys. 27 (1), 119–126 . 
Gelfand, B.E. , Gubin, S.A. , Timofeev, I.U. , Sheparnev, S.M. , 1978. Desintagration of liq- 
uid drop aggregation in shock waves. J. Appl. Mech. Tech. Phys. 6, 43–48 . 
Henshall, B.D. , 1957. On Some Aspects of the Use of Shock Tubes in Aerodynamic 
research. ARS Rep. & Memor, 3044. Univ. Bristol, Dept. Aeronaut. Eng, London . 
Hirt, C.W. , Nichols, B.D. , 1981. Volume of ﬂuid (VOF) method for the dynamics of 
free boundaries //. J. Comput. Phys. 39, 201–226 . 
Lapworth K.C., 1970. Normal shock-wave tables for air, argon, carbon dioxide and 
oxygen. London: her majesty’s stationery oﬃce. Current Papers C.P. 1101. 30. 
Minakov, A.V., Pervukhin, M.V., Platonov, D.V., Khatsayuk, M.Y., 2015. Mathemati- 
cal model and numerical simulation of aluminum casting and solidiﬁcation in 
magnetic ﬁelds with allowance for free surface dynamics. Comput. Math. Math. 
Phys. 55 (12), 2066–2079. doi: 10.1134/S096554251512009X . 
Minakov, A.V. , Rudyak, V.Y. , Gavrilov, A .A . , Dekterev, A .A . , 2012. Mixing in a 
T-shaped micromixer at moderate Reynolds numbers. Thermophys. Aeromech. 
19, 385–395 . 
Ortiz, C., Joseph, D.D., Beavers, G.S., 2004. Acceleration of a liquid drop suddenly 
exposed to a high-speed airstream. Int. J. Multiphase Flow 30 (2), 217–224. 
doi: 10.1016/j.ijmultiphaseﬂow.20 03.11.0 04 . 
Ranger, A .A ., Nicholls, J.A ., 1969. The aerodynamic shattering of liquid drops. AIAA 
J. 7 (2), 285–290. doi: 10.2514/3.5087 . 
Ranger, A .A . , Nicholls, J.A . , 1970. Shape and surrounding ﬂowﬁeld of a drop in a 
high-speed gas stream. AIAA J. 8 (9), 1720–1722 . 
Smagorinsky, J. , 1963. General circulation experiments with the primitive equations. 
I. The Basic Experiment. Month. Wea. Rev. 91, 99–164 . 
Theofanous, T.G. , Li, G.J. , 2008. On the physics of aerobreakup. Phys. Fluids 20, 
052103 . 
Versluis, M. , 2013. High-speed imaging in ﬂuids. Exp. Fluids 54 (1458), 1–35 .
