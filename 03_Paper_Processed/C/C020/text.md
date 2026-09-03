<!-- PDF_PAGE: 1 -->

Contents lists available at ScienceDirect
International Journal of Multiphase Flow
journal homepage: www.elsevier.com/locate/ijmulflow  
Express Track Article
Droplet breakup by multimodal nonlinear Rayleigh Taylor instability
Calvin J. Young a, Andrew W. Cook b
 , Jacob A. McFarland a
 ,∗
a Texas A& M Department of Mechanical Engineering, College Station, 77843, TX, USA
b Design Physics Division, Lawrence Livermore National Laboratory, Livermore, 94550, CA, USA
A R T I C L E  I N F O
Keywords:
Droplet breakup
Hydrodynamic instability
Rayleigh–Taylor
Kelvin–Helmholtz
 A B S T R A C T
A droplet impacted by a shock wave will undergo a process of fragmentation due to the development of 
interfacial hydrodynamic instabilities. The interface experiences variable acceleration and shear that result 
in the development of both inertial (Rayleigh–Taylor) and shear (Kelvin–Helmholtz) instabilities. These 
perturbations grow in time and drive the fragmentation and breakup of the deformed droplet. Experiments 
are performed on nominally 0.86 mm water droplet subjected to a Mach 7.6 detonation wave, resulting in 
a high Weber number (∼ 36 , 000) breakup event. Perturbation growth is measured from a series of high-
speed (> 1 MHz ) shadowgraph images. It is proposed that, given the size of the large-scale perturbations 
observed in experiments, these instabilities are growing in the non-linear regime and can be described by 
bubble-merger models for nonlinear mixing. Calculations are performed for the growth rates and size of these 
instabilities using deformation and external flow models to establish the time-dependent boundary conditions. 
The concurrence of the measured perturbation widths and the predictions of the simple model lend credence 
to the theory. This novel approach serves to open a new avenue in the characterization of droplet breakup via 
hydrodynamic instabilities.
1. Introduction
In the interaction of a shock wave with a droplet, the high-speed, 
high-temperature post-shock flow leads to the concurrent development 
of interfacial instabilities, heating and vaporization, and subsequent 
mixing of the two phases. A high pressure region forms on the wind-
ward interface, accelerating low density gas into the high density 
liquid, creating Rayleigh–Taylor (RT) instability. Simultaneously, the 
gas accelerates around the droplet surface, resulting in shear and gen-
erating Kelvin–Helmholtz (KH) instabilities. These instabilities work in 
concert to break down the droplet interface into ever smaller structures 
which may be acted on by further instability or evaporated. Bulk 
droplet deformation occurs simultaneous to these processes, resulting 
in transient acceleration and shear across the surface. Droplet breakup 
has been observed to scale with the characteristic time given by Ranger 
and Nicholls (1968), 𝜏 = 𝑡𝑣𝑔∕𝑑0
√𝜌𝑔∕𝜌𝑙, where 𝜌𝑔, 𝑣𝑔, 𝑑0, and 𝜌𝑙 are the 
gas density, gas velocity relative to the droplet, initial droplet diameter, 
and droplet liquid density. Breakup characteristics are often described 
by the Weber number, the ratio of inertial to surface tension forces, 
𝑊 𝑒 = 𝜌𝑔𝑣2
𝑔𝑑0∕𝜎, where 𝜎 is the droplet surface tension. The Weber 
number does not directly describe the growth rates of the RT and KH 
instabilities, and each may be dominant at various 𝑊 𝑒.
High 𝑊 𝑒 conditions arise in the interaction of hypersonic vehicles 
∗ Corresponding author.
E-mail address: mcfarlandja@tamu.edu (J.A. McFarland).
and atmospheric droplets, where flight Mach numbers 𝑀 > 5 generate 
strong bow shocks. Hypersonic vehicles must be capable of surviving 
droplets interactions and accurate prediction of the breakup and evap-
oration rate is essential for their design. Atmospheric water droplets 
can vary drastically in size, 1 μm ⪅ 𝑑 ⪅ 3 mm (Willis and Tattleman, 
1989), leading to 𝑊 𝑒 ≈ 1𝐸3 − 1𝐸5. Under these high-speed conditions, 
droplets experience high acceleration rates ((1𝐸6 𝑔)), promoting the 
growth of the RT instability. Similarly high acceleration rates are also 
found in liquid-fueled detonations, where small ((10𝜇𝑚) fuel droplets 
are broken up, evaporated, and reacted by detonation waves (5 ⪅ 𝑀 ⪅
10) (Young et al., 2025).
Reinecke and McKay (1969) studied 3 < 𝑀 < 12 shock interactions 
with large (0.5 < 𝑑 < 2.5 mm ) water droplets, observing rapid droplet 
disintegration with large-amplitude, RT-like perturbation growth. This 
breakup mechanisms came to be termed catastrophic (Pilch and Erd-
man, 1987). Later Theofanous et al. (2007, 2012), without similar 
evidence at high 𝑀 accelerations, cast doubt on this work, noting that 
the waves observed ‘‘are at least an order of magnitude longer than 
the most rapidly growing RT waves under the relevant accelerations’’. 
Recently, Dworzanczyk et al. (2025) used a high Mach number (𝑀 > 5) 
bow shock from a hypersonic projectile to accelerate water droplets, 
observing similar RT features to Reinecke and McKay (1969).
https://doi.org/10.1016/j.ijmultiphaseflow.2025.105490
Received 31 August 2025; Received in revised form 14 October 2025; Accepted 17 October 2025
International Journal of Multiphase Flow 194 (2026) 105490 
Available online 21 October 2025 
0301-9322/© 2025 The Authors. Published by Elsevier Ltd. This is an open access article under the CC BY-NC license ( http://creativecommons.org/licenses/by- 
nc/4.0/ ).

<!-- PDF_PAGE: 2 -->

C.J. Young et al.
2. Modeling hydrodynamic instability
Linear stability theory predicts perturbation amplitude (𝜂(𝑡)) growth 
for RT and KH instability, Eq. (1) where 𝜂0 is the initial amplitude. 
Assuming negligible droplet velocity (𝑣𝑝 ≈ 0 ), gas density (𝜌𝑔 ≪ 𝜌 𝑙), 
and viscous effects, 𝛺 (the growth rate constant) is found for a 2D 
perturbation as in Eq. (2), where  = (𝜌𝑙−𝜌𝑔)∕(𝜌𝑙+𝜌𝑔) ≈ 1 is the Atwood 
number, 𝑘 = 2 𝜋∕𝜆 is the wavenumber, and 𝑎𝑛 the acceleration normal 
to the interface. Surface tension has the effect of damping small modes 
(perturbations of similar size) such that a fastest growing mode exists at 
some wavenumber 𝑘𝑚𝑎𝑥. A theoretical model for both KH (primary) and 
RT (secondary) breakup of sprays derived from linear stability theory is 
given by Beale and Reitz (1999), Liu et al. (1993). This KHRT model has 
been applied to droplet breakup but is limited by the lack of physical 
breakup length and time scales. 
𝜂(𝑡) = 𝜂0 exp 𝛺𝑡 (1)
𝛺 = 𝑖𝑘𝑢𝑔
𝜌𝑔
𝜌𝑙
±
[𝑘2𝜌𝑔𝑢2
𝑔
𝜌𝑙
+ 𝑘𝑎𝑛 − 𝑘3𝜎
𝜌𝑙
]1
2
(2)
The incoming freestream flow is deflected by the deforming droplet, 
resulting in variable acceleration and shear forces on the windward 
surface. The mode size and growth rate vary with position on the 
droplet surface, from the windward stagnation point (𝜃 = 0), where RT 
instability is dominant, to the equator (𝜃 = ± 𝜋∕2), where KH growth 
is dominant. The resultant instability develops initially at the local 
fastest growing 𝑘, beginning from small initial perturbations (𝜂0𝑘 =
(1𝐸-3 − 10𝐸-6)) and growing in time into ‘spikes’ of heavy fluid and 
‘bubbles’ of light fluid. It is important to note that linear stability theory 
is only applicable up to a perturbation amplitude of 𝜂𝑘 ∼ 1, after which 
the instability becomes nonlinear and different behaviors are observed.
RT breakup occurs when the perturbations grow to a sufficient 
height to pierce the droplet interface. The thickness of the droplet in the 
axial direction 𝛿 is reduced by large-scale droplet deformation, which 
acts to deform the droplet into an oblate spheroid. This deformation has 
been successfully predicted using the Taylor Analogy Breakup (TAB) 
model (O’Rourke and Amsden, 1986), which treats the droplet as a 
spring, mass, and damper system. The deformation can be predicted 
by solving an ordinary differential equation with coefficients 𝐶𝛿, 𝐶𝑘, 
𝐶𝑓 . This deformation also affects the droplet drag coefficient 𝐶𝐷 and 
cross-sectional area, increasing 𝑎𝑛 and modifying the external flow 
characteristics and shear velocity 𝑢𝑡 (Duke-Walker et al., 2025).
Under flow conditions encountered in high Mach number flight, 
the fastest growing modes are much smaller than the droplet thick-
ness throughout its lifetime. Thus the modes are likely growing into 
the nonlinear regime. Dworzanczyk et al. (2025) applied a nonlinear 
RT growth model to successfully describe the breakup time observed 
in their 𝑀 ∼ 5  experiments. While a significant step forward, the 
model does not describe the emergence of large modes observed in the 
experiment.
Experimental observations show a broad range of structures devel-
oping, termed a multimodal perturbation in hydrodynamic theory. On a 
multimodal KHRT interface with surface tension, the initial growth rate 
will increase with 𝑘, up to 𝑘𝑚𝑎𝑥, but the growth of each mode will sat-
urate (plateau) in time as a mode reaches the non-linear regime. Over 
time successively larger (smaller 𝑘) modes will emerge as the fastest 
growing, then saturate (Layzer, 1955). This results in broad-spectrum 
turbulence with the onset of mixing.
One potential description for the emergence of larger modes in the 
RT instability is provided by the bubble merger model (Ramaprabhu 
et al., 2013; Dimonte et al., 2005). In this description, as small-mode 
bubbles saturate they merge together to form larger modes that con-
tinue to grow. The bubble height ℎ𝑏,𝑅𝑇 is the distance the RT bubbles 
have penetrated into the heavy fluid and is predicted as in Eq.  (3), 
where 𝛼𝑏 is a function of the Froude number (𝐹 𝑟), the bubble 𝑘, 
and initial amplitude (⟨ℎ0,𝑘⟩) and typically lies between 0.02 < 𝛼 𝑏 <
0.08 (Eq. (4)). The effect of an unsteady acceleration has also been 
considered (Mikaelian, 2010; Ramaprabhu et al., 2016), where the 
variable 𝑆𝑛(𝑡) (Eq.  (5)) takes the places of the quantity 𝑎𝑛𝑡2 in Eq.  (3). 
For multimode perturbations the bubble diameter, 𝐷𝑏, can be used in 
place of 𝜆 as the mode size and here we use them interchangeably. The 
exact value of the ratio 𝐷𝑏∕ℎ𝑏 is debated, but it is typically accepted 
that 𝐷𝑏 ≈ ℎ𝑏 (Dimonte et al., 2004). 
ℎ𝑏,𝑅𝑇 (𝑡) = 𝛼𝑏𝑎𝑛𝑡2 (3)
𝛼𝑏 = 𝐹 𝑟
4
√
2𝜋
1 + 
[
𝑙𝑛
( 2𝐹 𝑟
√
2𝜋∕(1 + )
𝑘ℎ0,𝑘
)
− 1
]−1
(4)
𝑆𝑛(𝑡) =
[
∫
𝑡
0
√
𝑎𝑛(𝑡′)𝑑𝑡′
]2
(5)
A simplified relation for the mixing width (ℎ𝐾𝐻 ) of a time depen-
dent KH instability is provided by Smalyuk et al. (2012), citing Dimo-
takis (1991), in Eq.  (6), where 𝑣𝑔(𝑡′) is the instantaneous velocity of the 
gas relative to the droplet. 
ℎ𝐾𝐻 (𝑡) =  ∫
𝑡
0
𝑣𝑔(𝑡′)𝑑𝑡′ (6)
Olson et al. (2011) proposed a model to find the combined growth 
rate of KH and RT instability ( ̇ℎ𝐾𝐻𝑅𝑇 = 𝑉𝐾𝐻𝑅𝑇 𝑓 (𝛽, )) in the early 
nonlinear regime. Here, 𝑉𝐾𝐻𝑅𝑇  is the combined velocity scale (Eq.  (7)) 
and 𝛽 = 𝑉𝑅𝑇 ∕𝑉𝐾𝐻𝑅𝑇  is a ratio of the RT to combined velocity scales 
(𝛽 = 0 for pure KH and 𝛽 = 1 for pure RT growth). The factor 𝑓 is a 
weak function of  and primarily describes the relative contribution 
of KH and RT components on perturbation growth rate. While trends 
were observed in their data, no explicit or general form of 𝑓 was given.
To define 𝑓 we consider pure KH and RT cases. For a pure KH 
case (𝑉𝑅𝑇 = 0 ) with 𝐴 ≈ 0 .995 (the conditions reported here), √
𝜋(1 − 2)∕2 = 0 .13 in Eq.  (7). Taking 𝑓 as a constant with 𝑉𝐾𝐻 = 𝑣𝑔(𝑡)
and integrating ̇ℎ𝐾𝐻𝑅𝑇 , we find ℎ𝐾𝐻𝑅𝑇 = ℎ𝐾𝐻 if  = 0 .13𝑓 . Smalyuk 
et al. (2012) proposed that  = 0.18 for high  KH experiments, which 
provides 𝑓 ≈ 1 .4. Similarly, for the pure RT case (𝑉𝐾𝐻 = 0 ) we take 
𝑉𝑅𝑇 = 𝛼𝑏(𝑑𝑆𝑛∕𝑑𝑡) and find ℎ𝐾𝐻𝑅𝑇 = ℎ𝑏,𝑅𝑇 if 𝑓 = 1 . Thus, we take 
𝑓 = 1 as the simplest approximate solution. The bubble height can then 
be predicted as in Eq.  (8). 
𝑉𝐾𝐻𝑅𝑇 ≈
√
𝜋
2 (1 − 2)𝑉 2
𝐾𝐻 + 𝑉 2
𝑅𝑇 (7)
ℎ𝑏,𝐾𝐻𝑅𝑇 = ∫
𝑡
0
( 𝜋(1 − 2)
2
( 𝑣𝑝𝑔(𝑡′)) 2 +
(
𝛼𝑏 𝑑𝑆𝑛
𝑑𝑡′
) 2)
𝑑𝑡′ (8)
The flow variables about the surface are calculated in a similar 
way to Dworzanczyk et al. (2025), utilizing a modification of Newton’s 
inclination method for blunt bodies. Note that the post-detonation gas 
conditions are not supersonic in our case, thus the equations simplify 
further. The normal vector to the surface can be described as 𝑡𝑎𝑛(𝜃𝑛) =
( 𝑏
𝑐 )2 𝑡𝑎𝑛(𝜃), where 𝜃𝑛 describes the angle of the normal vector from 
the free-stream at angular position 𝜃 on the droplet surface (Fig.  1). 
The normal acceleration is given by 𝑎𝑛 = 𝑎𝑐𝑜𝑠(𝜃𝑛), where 𝑎 is the 
bulk acceleration of the droplet. The pressure along the surface 𝑝(𝜃) is 
calculated from the total pressure 𝑝0 at the stagnation point by Eq. (9), 
where 𝑝𝑔, is the gas pressure. Taking the flow along the surface to be 
isentropic, Eq.  (10) provides the density 𝜌𝑔(𝜃) along the surface. The 
local gas velocity is found from the local dynamic pressure, 𝑣(𝜃) =√2(𝑝(𝜃) − 𝑝𝑔)∕𝜌(𝜃). 
𝐶𝑝(𝜃) =
2(𝑝(𝜃) − 𝑝𝑔)
𝜌𝑔𝑣2
𝑔
= 𝑐𝑜𝑠2(𝜃𝑛) (9)
𝜌0,2
𝜌(𝜃) =
( 𝑝0,2
𝑝(𝜃)
) 1
𝛾2
(10)
International Journal of Multiphase Flow 194 (2026) 105490 
2

<!-- PDF_PAGE: 3 -->

C.J. Young et al.
Fig. 1. Diagram of droplet and flow conditions.
Fig. 2. Diagram of Shadowgraphy Setup. Left: As viewed from above. Right: 
Center cross section in the camera’s viewing plane.
3. Results
Experiments were performed in the vertical detonation tube facility 
detailed in Young et al. (2025). A stream of 0.86 ± 0 .061 mm  water 
droplets were generated with a piezoelectric device and deposited 
in the tube from the side (see Fig.  2, right). Shadowgraph images 
were taken by a SIMX-16 camera paired with a K-2 Distamax lens, 
illuminated by a 400 W Cavilux laser. The resultant resolution was 
approx. 3 μm/pixel and exposures were 35 ns. A diagram of the imaging 
setup is provided in Fig.  2. The droplets were accelerated by a stoi-
chiometric propane-oxygen detonation with wave speeds within 5% of 
those calculated from 1D gas dynamics (Browne et al., 2018), nominally 
2350  m/s or M∼ 7.6. Post-detonation gas properties were calculated as 
𝜌𝑔 = 2.5873 𝑘𝑔∕𝑚3, 𝑝𝑔 = 3.67 MPa, 𝑣𝑔 = 1086.7  m/s, and 𝑀𝑔 ≈ 0.86. 
For these conditions 𝑊 𝑒 ∼ 36, 000.
Image acquisition was triggered using the SIMX-16’s velocity trap 
and pressure transducers mounted ahead of the test section. Image 
timings were prescribed such that the detonation interacted with the 
droplet in the second frame, providing a reference time and image 
of the initial droplet shape. The resultant shadowgraph images for 
one experimental trial are presented in Fig.  3. The detonation front 
is visible as a dark region traveling from right to left in the second 
and third frames. KH features are visible on the leeward side of the 
droplet at 𝜏 = 0.16, with a mist of small child droplets growing in time. 
RT features are visible at this time on the windward surface. The KH 
features evolve into distinct axial streams of small droplets, similar in 
appearance to ligaments observed in lower 𝑊 𝑒 breakup. KH modes are 
also visible on the sides of the droplets, continuing to evolve in the R-Z 
plane. The RT-like features grow in time, with three large modes visible 
on the lower droplet at 𝜏 = 0 .65. Smaller modes also evolve on top of 
these large modes as seen at 𝜏 = 0.83.
To model the growth of the hydrodynamic instabilities, the droplet 
deformation and drag are first modeled using the drag model of Duke-
Walker et al. (2025) with the standard TAB coefficients (𝐶𝛿 = 5, 𝐶𝑘 = 8, 
𝐶𝑓 = 1∕3 ) from O’Rourke and Amsden (1986) and the modified TAB 
coefficients (𝐶𝛿 = 5 , 𝐶𝑘 = 8 , 𝐶𝑓 = 1 ) given in Duke-Walker et al. 
(2025) (Fig.  4). The shape of the droplet is estimated by fitting an 
ellipsoid to the upstream edge position and the maximum radial extents 
of the deformed shape. The mist of child droplet obscures the extents 
of the parent droplet after 𝜏 ∼ 0 .2, likely inflating the deformation. 
The droplet position also becomes sensitive to the formation of spikes 
which become the upstream-most edge (see Fig.  5, left), likely causing 
the droplet distance traveled to be underpredicted. Thus, the predicted 
droplet deformation (lower) and trajectory (slower) showed reasonable 
agreement with the original TAB model (used from here on) given the 
limitations of the shadowgraph images.
From the deformation and drag model the predicted droplet velocity 
and acceleration were found (Fig.  6). The droplet acceleration peaks 
initially (𝜏 < 0.1) due to unsteady drag before dropping and then 
climbing to a peak at 𝜏 ∼ 1 .6. The acceleration reaches a value of 
∼ 1 .3𝐸6𝑔 at 𝜏 = 1 , before the windward interface begins to breakup. 
The local normal acceleration 𝑎𝑛(𝜃), density 𝜌(𝜃), and velocity 𝑣(𝜃) are 
calculated using Eqs. (9) and (10). Eq.  (7) is then used to calculate 
ℎ𝑏,𝐾𝐻𝑅𝑇  as a function of 𝑟∗ = 2𝑟𝑖∕𝑑0, the ratio of initial radial position, 
𝑟𝑖, to initial droplet radius.
The mode sizes were identified for each image time over a total of 
20 trials. Each image provided a range of 𝐷𝑏 measured, representing 
the multimode perturbation. The images were contrast enhanced and 
the modes identified manually. The minimum wavelength recorded was 
limited to 5 pixels, ∼ 15𝜇𝑚. This manual method was necessary as the 
modes sizes and shapes were not periodic in the radial direction, 𝑟, such 
that Fourier analysis could produce a reliable spectrum. The associated 
uncertainty for this method was estimated to be ±2𝑝𝑖𝑥𝑒𝑙𝑠 or ±6𝜇𝑚. Fig. 
5 shows an example image with highlighting the boundaries of some 
of the larger modes measured.
The non-nondimensionalized mode sizes recorded over time are 
presented in Fig.  7. Here we assume the 3D bubble diameter is the 
same as the 2D mode width (𝜆) measured and that ℎ𝑏 = 𝐷𝑏. The 
blue shaded region bounds the maximum and minimum sizes over 
time. The perturbation widths increase in time with a maximum value 
of 𝐷𝑏∕𝑑0 ∼ 0 .65. Even as large modes emerge at late times, small 
modes continue to form at larger 𝑟 (KH modes) and on top of the large 
modes. After 𝜏 ∼ 0 .9 − 1 .3 the windward droplet interface begins to 
break down and the deformed droplet cloud intersects with neighboring 
droplets. Structures, potentially RT modes, remain visible and continue 
to grow at later times, however, they could not be measured due to the 
interference of adjacent droplets.
The bubble size, 𝐷𝑏 = ℎ𝑏, gives a length scale for predicting child 
droplet diameter (e.g. 𝑑𝑐 ∼ 𝐷𝑏), and for predicting the breakup time 
(e.g. when ℎ𝑏 = 𝛿). Thus, using Eq.  (8) with the local flow conditions 
the length scales for breakup and the droplet breakup time a can be 
predicted. Fig.  7 shows the predicted 𝐷𝑏 for several 𝑟∗ values. The 
predicted range of bubble diameters matches the experimental data 
well. Here, the lines at 𝑟∗ = 1 .0 and 0.8 show the fastest growth, 
but since these modes are near the periphery of the droplet, their 
growth cannot penetrate and breakup the core of the droplet. The 
modes from 𝑟∗ = 0 .0 to 0.4 represent mode growth over the core of 
the droplet. Their growth is aligned with the deformation reducing 
the thickness of the droplet interface (𝛿). Thus, when these modes 
reach the approaching leeward interface the core of the droplet will be 
shattered. The black dashed line marks the width necessary to penetrate 
the interface based on the TAB model predictions. From this we can see 
that the RT modes penetrate the interface from 𝜏 ≈ 0 .6 − 1.1. We take 
𝜏 = 1.1 as an estimated time for total core breakup. While this indicates 
that the core droplet may no longer behave as a single interface, it does 
not mean that the droplet breakup process is complete, as these large 
International Journal of Multiphase Flow 194 (2026) 105490 
3

<!-- PDF_PAGE: 4 -->

C.J. Young et al.
Fig. 3. Shadowgraph image set from experiments.
 
(a) 
  
(b) 
 
Fig. 4. Left: Measured droplet deformation compared to the standard TAB model O’Rourke and Amsden (1986) and the modified TAB model Duke-Walker et al. 
(2025). Right: Droplet position compared to predictions from the drag models Duke-Walker et al. (2025) using droplet deformation from the standard and modified 
TAB models. The lines transition from solid to dashed at the estimated time of core breakup, 𝜏 = 1.1.
features (0.2𝑑0 ⪅ 𝐷𝑏 ⪅ 0.5𝑑0) will continue to break down until the size 
and velocity are such that a stable 𝑊 𝑒 is reached.
High Weber number (𝑊 𝑒 ∼36,000) breakup of 850 μm  water 
droplets was recorded by high speed shadowgraph images. Measure-
ments of the droplet deformation and trajectory agreed well with 
the Taylor Analogy Breakup model and the droplet trajectory by the 
model of Duke-Walker et al. (2025). Hydrodynamic instabilities were 
observed on the windward surface and their sizes measured over 
time. These measurements showed that mode sizes increased in time, 
suggesting that the initially fastest growing modes were not responsible 
for the ultimate droplet breakup. Following previous works, a model for 
simultaneous KH and RT nonlinear growth was developed for droplets 
in high-speed flows. The model predicts the local growth rates of KH 
and RT instabilities over the surface of the droplet as it deforms. The 
modeled droplet acceleration and velocity are used to predict the time 
dependent growth rate and mode size of the RT instability using the 
bubble merger model. Overall, the growth rates of the combined non-
linear KH and RT instabilities are shown to bound the experimentally 
observed mode sizes. Using the deformation model and RT mode 
growth rates, the droplet core is predicted to undergo a first breakup 
event at nondimensional breakup times from 0.6 to 1.1, far earlier 
than predicted by previous models, leading to the formation of large 
fragments (0.2 − 0.5𝑑0).
4. Conclusions
The multimode model described here represents a new understand-
ing of droplet breakup from KH and RT instabilities. With sufficient 
International Journal of Multiphase Flow 194 (2026) 105490 
4

<!-- PDF_PAGE: 5 -->

C.J. Young et al.
Fig. 5. Schematic of the droplet measurements. Left: Schematic highlighting 
measured droplet quantities. Right: A sample late time image illustrating the 
ellipsoid fit and measurement of bubble widths, 𝐷𝑏. For simplicity, only the 
largest modes identified are shown.
Fig. 6. Predicted droplet velocity and acceleration. The lines transition from 
solid to dashed at the estimated time of core breakup, 𝜏 = 1.1.
Fig. 7. Perturbation width predictions (solid lines) overlaid with experimental 
observations (blue dots/shaded regions).The magenta line shows the predicted 
linear growth rate (Eq.  (1)) taking 𝜂 ∼ ℎ𝑏. The magenta dot shows the predicted 
breakup time from Beale and Reitz (1999). The black dashed line shows the 
predicted droplet thickness. Note that the 𝑦 axis represents both 𝐷𝑏∕𝑑0 and 
ℎ𝑏∕𝑑0, since we take 𝐷𝑏 = ℎ𝑏. (For interpretation of the references to color in 
this figure legend, the reader is referred to the web version of this article.)
gas inertia, droplet acceleration will be significant, leading to substan-
tial RT growth. The RT and KH instabilities evolve simultaneously, 
with contributions from acceleration and shear forces varying over the 
surface of the droplets. While surface tension creates a local fastest 
growing mode size, these modes have a finite lifetime before their 
growth saturates. For the KH instability, the modes are unable to 
penetrate the droplet thickness. Instead they advect to edge of the 
droplet and are shed as small child droplets. For RT growth, smaller 
modes will be overtaken by larger modes as they saturate leading to a 
cycle of successively larger modes emerging. As the droplet continues to 
deform, the RT modes grow to a size sufficient to penetrate the droplet 
interface, creating large fragments that take on their own trajectory. 
The growth rate of these predominantly RT modes is enhanced by shear 
(KH contributions), and modes further from the droplet center are pre-
dicted to penetrate the droplet interface first, at 𝜏 ∼ 0.6. RT modes near 
the center will complete the first breakup of the droplet core late, at 
𝜏 ∼ 1.1. These first breakup events are not terminal however, and subse-
quent hydrodynamic instabilities will drive a breakup cascade until the 
child droplets reach a stable size or are evaporated. Subsequent work 
will seek to determine the KH mass loss rate, model for the secondary 
and tertiary breakup events, and provide more accurate measurements 
of the droplet dynamics using new measurement techniques.
CRediT authorship contribution statement
Calvin J. Young: Writing – review & editing, Writing – original 
draft, Validation, Methodology, Investigation, Formal analysis, Data 
curation, Conceptualization. Andrew W. Cook: Writing – review & 
editing, Supervision, Project administration, Methodology, Funding ac-
quisition, Conceptualization. Jacob A. McFarland: Writing – review & 
editing, Writing – original draft, Project administration, Methodology, 
Formal analysis, Conceptualization.
Funding
This work was performed under the auspices of the U.S. Department 
of Energy by Lawrence Livermore National Security under contract 
DE-AC52-07NA27344 subcontract B662744.
Declaration of competing interest
The authors declare the following financial interests/personal rela-
tionships which may be considered as potential competing interests: 
Jacob McFarland reports financial support was provided by Lawrence 
Livermore National Laboratory. If there are other authors, they declare 
that they have no known competing financial interests or personal 
relationships that could have appeared to influence the work reported 
in this paper.
Data availability
Data will be made available on request.
References
Beale, J.C., Reitz, R.D., 1999. Modeling spray atomization with the Kelvin-
Helmholtz/Rayleigh-Taylor hybrid model. At. Sprays 9 (6), 623–650.
Browne, S., Ziegler, J., Shepherd, J.E., 2018. Numerical Solution Methods for Shock 
and Detonation Jump Conditions. GALCIT Report FM2006.006 - R3.
Dimonte, G., Ramaprabhu, P., Youngs, D., Andrews, M., Rosnder, R., 2005. Recent 
advances in the turbulent Rayleigh–Taylor instability. Phys. Plasmas 18.
Dimonte, G., et al., 2004. A comparative study of the turbulent Rayleigh–Taylor instabil-
ity using high-resolution three-dimensional numerical simulations: The Alpha-Group 
collaboration. Phys. Fluids 16, 1668–1693.
Dimotakis, P.E., 1991. Turbulent free shear layer mixing and combustion. Prog. 
Astronaut. Aeronaut. 137, 265–340.
Duke-Walker, V.O., Paudel, M., Keltz, J., McFarland, J.A., 2025. Deformation and 
acceleration of small droplets at high-speed conditions. Int. J. Multiph. Flows 193, 
105372.
Dworzanczyk, A., Viqueira-Moreira, M., Langhorn, J., Libeau, M., Brehm, C., 
Parziale, N., 2025. On aerobreakup in the stagnation region of high-Mach-number 
flow over a bluff body. J. Fluid Mech. 1002.
International Journal of Multiphase Flow 194 (2026) 105490 
5

<!-- PDF_PAGE: 6 -->

C.J. Young et al.
Layzer, D., 1955. On the instability of superposed fluids in a gravitational field. 
Astrophys. J. 122, 1–12.
Liu, A., Mather, D., Reitz, R., 1993. Modeling the effects of drop drag and breakup on 
fuel sprays. In: SAE Technical Paper 930072. p. 17.
Mikaelian, K.O., 2010. Analytic approach to nonlinear hydrodynamic instabilities 
driven by time-dependent accelerations. Phys. Rev. E 81, 016325. http://
dx.doi.org/10.1103/PhysRevE.81.016325, URL: https://link.aps.org/doi/10.1103/
PhysRevE.81.016325.
Olson, B.J., Larsson, J., Lele, S.K., Cook, A.W., 2011. Nonlinear effects in the combined 
Rayleigh-Taylor/Kelvin-Helmholtz instability. Phys. Fluids 23 (11), 114107.
O’Rourke, P.J., Amsden, A.A., 1986. The TAB Method for Numerical Calculation of 
Spray Droplet Breakup. Technical Report, Los Alamos National Lab., NM (USA).
Pilch, M., Erdman, C.A., 1987. Use of breakup time data and velocity history data to 
predict the maximum size of stable fragments for acceleration-induced breakup of 
a liquid drop. Int. J. Multiph. Flow 13 (6), 741–757.
Ramaprabhu, P., Karkhanis, V., Banerjee, R., Varshochi, H., Khan, M., Lawrie, A.G., 
2016. Evolution of the single-mode Rayleigh-Taylor instability under the influence 
of time-dependent accelerations. Phys. Rev. E 93 (1), 013118.
Ramaprabhu, P., Karkhanis, V., Lawrie, A.G.W., 2013. The Rayleigh–Taylor instability 
driven by an accel-decel-accel profile. Phys. Fluids 25 (11).
Ranger, A.A., Nicholls, J.A., 1968. Aerodynamic shattering of liquid drops. In: 6th 
Aerospace Sciences Meeting.
Reinecke, W.G., McKay, W.L., 1969. Experiments on Water Drop Breakup Behind Mach 
3 to 12 Shocks. Technical Report, AVCO.
Smalyuk, V.A., et al., 2012. Experimental observations of turbulent mixing due to 
Kelvin–Helmholtz instability on the OMEGA laser facility. Phys. Plasmas 19 (9), 
092702.
Theofanous, T.G., Li, G.J., Dinh, T.N., Chang, C.-H., 2007. Aerobreakup in disturbed 
subsonic and supersonic flow fields. J. Fluid Mech. 593, 131–170. http://dx.doi.
org/10.1017/S0022112007008853.
Theofanous, T.G., Mitkin, V.V., Ng, C.L., Chang, C.-H., Deng, X., Sushchikh, S., 2012. 
The physics of aerobreakup. II. Viscous liquids. Phys. Fluids 24 (2).
Willis, P.T., Tattleman, P., 1989. Droplet size distributions associated with intense 
rainfall. App. Meteorol. 
Young, C.J., Duke-Walker, V.O., McFarland, J.A., 2025. Droplet breakup and 
evaporation in liquid-fueled detonations. Exp. Therm. Fluid Sci. 160, 111324.
International Journal of Multiphase Flow 194 (2026) 105490 
6
