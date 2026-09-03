<!-- PDF_PAGE: 1 -->

Contents lists available at ScienceDirect
International Journal of Multiphase Flow
journal homepage: www.elsevier.com/locate/ijmulflow  
Deformation and acceleration of small droplets at high-speed conditions
Vasco O. Duke W. a,b,c, Manoj Paudel a, Jacob Keltz a
 , Jacob A. McFarland a
 ,∗
a Texas A&M University, College Station, TX, USA
b Sandia National Laboratory, Livermore, CA, USA
c Technological University of Panama, Avenida Domingo Diaz, Ciudad de Panama, Panama
A R T I C L E  I N F O
Keywords:
Acceleration
Breakup
And drag coefficient
Deformation
Stripping mechanisms
Unsteady drag coefficient
Droplet and evaporation
 A B S T R A C T
Shock-driven droplet breakup occurs in various physical systems and plays a critical role in emergent high-
speed flight applications such as droplet combustion in rotating detonation engines (RDEs) and droplet impacts 
on hypersonic vehicles. Droplets interact with strong shock waves in these applications, and the high post-shock 
gas velocity and temperature lead to rapid droplet acceleration, evaporation, and breakup through various 
hydrodynamic instabilities. Accurate prediction of the breakup process is essential in these applications and 
theory-based models are required to cover the large parameter space encountered. In order to model the growth 
of hydrodynamic instabilities on the droplet, the acceleration and droplet shape must be known first, requiring 
accurate prediction of both deformation and drag. Previous work has largely focused on large droplets at lower 
shock strengths, where acceleration and evaporation are much slower. Here, the dynamics of small droplets 
accelerated by strong shock waves are explored up to the onset of breakup, focusing on droplet size, Mach 
number, and evaporation effects on the deformation and acceleration.
Shock tube experiments are conducted for a wide range of parameters including droplet size, shock 
strength, and liquid properties. Incident shock wave Mach numbers of 1.35 - 2.1 are used with micron-scale 
droplets with diameters from ∼ 50  to 200[μm]. Various fluids (water, dodecane, and acetone) were studied 
yielding Weber numbers from ∼ 100–6000. Droplet deformation and position are measured with sub-micrometer 
spatial resolution and sub-microsecond temporal resolution. New modifications to the Taylor Analogy Breakup 
model are presented with modified drag correlations accounting for deformation and Mach number effects to 
accurately capture the droplet dynamics. The results are compared with previous millimeter-droplet breakup 
studies, finding that bulk droplet deformation and drag are captured by the new models over a wide range of 
conditions. Evaporation was not observed to effect these processes, even for the smallest droplets. However, 
small droplets are shown to exhibit significantly less hydrodynamic instability growth than large droplets, 
which display a larger departure in trajectory from the model at late times.
1. Introduction
Shock-driven droplet breakup occurs in critical engineering applica-
tions such as hypersonic vehicle droplet impacts (hydrometeor impacts) 
and the combustion of fuel droplets in detonation-driven propulsion ap-
plications such as rotating detonation engines (RDEs). For hydrometeor 
impacts and RDEs, droplets experience comparable conditions (high gas 
velocity and temperature) but are generally concerned with different 
sized droplets. For hydrometeor impacts, most occur with millimeter-
scale (large) droplets while micron-scale (small) droplets are relevant 
for RDEs. A myriad of other applications exist such as detonation mit-
igation and highly energetic combustion applications (Guildenbecher 
et al., 2009). The droplet deformation process is highly transient as the 
droplet deforms rapidly from its initially spherical shape. This in turn 
∗ Corresponding author.
E-mail address: mcfarlandja@tamu.edu (J.A. McFarland).
rapidly increases the drag resulting in an unsteady acceleration that 
alters the growth of the instabilities driving breakup. A wide range of 
conditions arise due to variations in droplet size, liquid properties, and 
shock conditions (e.g. gas velocity, pressure, and temperature) resulting 
in various breakup regimes and time scales. Notably, small droplets, 
≤100 [μm] , experience a higher acceleration and greater evaporation 
potential challenging deformation and drag models.
The droplet deformation and breakup processes are driven by 
the sudden onset of velocity and pressure gradients produced in the 
freestream conditions by the shock wave acting on the surrounding gas. 
Droplet breakup is often characterized by two main parameters. First, 
the Weber number (We = 𝜌𝑔𝑑0𝑣2
𝑝𝑔∕𝜎), defined as the ratio between 
inertial and surface tension forces acting on the droplet’s surface where 
https://doi.org/10.1016/j.ijmultiphaseflow.2025.105372
Received 15 April 2025; Received in revised form 19 June 2025; Accepted 19 July 2025
International Journal of Multiphase Flow 193 (2025) 105372 
Available online 9 August 2025 
0301-9322/© 2025 The Author(s). Published by Elsevier Ltd. This is an open access article under the CC BY-NC license ( http://creativecommons.org/licenses/by- 
nc/4.0/ ).

<!-- PDF_PAGE: 2 -->

V.O.D. W. et al.
Nomenclature
𝐹 𝑂𝑉 Field of view
𝑚𝑑 Droplet mass
𝜖 Ratio of droplet and gas densities
𝛾𝐾𝐻 Growth rate in KH
𝛾𝑅𝑇 Growth rate in RT
𝜆 Distance between perturbation peaks
𝜆𝐾𝐻 The most unstable wavelength in KH
𝜆𝑅𝑇 The most unstable wavelength in RT
𝐚𝑑 Droplet acceleration
𝐅𝑑 Drag force
𝜇𝑔 Dynamic viscosity of the gas
𝜇𝑝 Dynamic viscosity of the liquid droplet
𝜌𝑔 Density of the gas
𝜌𝑑 Density of the droplet
𝜎 Surface tension of the droplet
𝐴𝑓 Frontal area of the droplet
𝐶𝑑 Drag coefficient
𝐶𝑞 Quasi-steady drag
𝐶𝑢 Unsteady drag term
𝐶𝑀 Mach correction coefficient
𝐶𝑞,𝑑 Drag coefficient of a disk
𝐶𝑞,𝑠 Drag coefficient of a sphere
𝑑0 Initial droplet diameter
𝑑𝑗 Orifice jet diameter
𝑑𝑛 Nominal droplet diameter
𝑑𝑦 Current deformed diameter
𝑓 Piezoelectric frequency
𝑀𝑖 Mach Number
𝑂ℎ Ohnesorge number
𝑃𝑔 Pressure of the gas
𝑃𝑠𝑎𝑡 Saturation Pressure
𝑅𝑒 Reynolds number
𝑡 Time
𝑡∗ Dimensionless time
𝑡∗
𝑏,𝑖 Non-dimensional breakup initiation time
𝑡𝑐 Characteristic time
𝑇𝑑 Temperature of the droplet
𝑡𝑒𝑣𝑎𝑝 Evaporation time
𝑡𝑒𝑥𝑝 Exposure time
𝑇𝑔 Temperature of the gas
𝑣𝑑 Velocity of the droplet
𝑣𝑔 Velocity of the gas
𝑣𝑗 Fluid jet velocity
𝑣𝑝𝑔 Relative velocity of the gas to the droplet
𝑊 𝑒 Weber number
𝑥𝑑 Droplet position
𝑌 Droplet deformation
𝜌𝑔 is the gas density, 𝑑0 is the initial droplet diameter, 𝑣𝑝𝑔 = 𝑣𝑔 − 𝑣𝑝 is 
the relative velocity of the gas 𝑔 to the droplet 𝑝, and 𝜎 is the surface 
tension. Second is the Ohnesorge number (Oh = 𝜇𝑝∕√𝜌𝑝𝜎𝑑𝑝) which 
represents the ratio of viscous to inertial and surface effects, where 𝜇𝑝
is the droplet’s dynamic viscosity. Lastly, the Reynolds number (Re =
𝜌𝑔𝑑0𝑣𝑝𝑔∕𝜇𝑔) which is defined by the ratio of inertial to viscous effects 
where 𝜇𝑔 is the dynamic viscosity of the gas. For many applications the 
droplet liquid viscosity is sufficiently low for Oh effects to be neglected, 
as we have here. However, a wide range of We values are observed in 
shock-driven applications, as it varies with the square of 𝑣𝑝𝑔. Pilch and 
Erdman (1987) proposed five regimes for breakup:  vibrational breakup 
(We ≤ 12), bag breakup (12 < 𝑊 𝑒 ≤ 50), bag-and-stamen breakup 
(50 < 𝑊 𝑒 ≤ 100), sheet stripping (100 < 𝑊 𝑒 ≤ 350), and wave crest 
stripping followed by catastrophic breakup (350 < We). In many high-
speed applications, catastrophic breakup is most prevalent due to the 
high velocities present within the system. In addition to parameters de-
scribing the morphological behavior of the droplet, it is also necessary 
to describe the time scale of deformation events. In early experimental 
work by Ranger and Nicholls (1969), an empirical correlation was 
proposed for a characteristic transport time, 𝑡∗ = 𝑡∕𝑡𝑐 and 𝑡𝑐 = 𝜖0.5𝑑0∕𝑣𝑔
where 𝑡∗ is the dimensionless time, 𝑡 is the dimensional time, 𝑡𝑐 is the 
characteristic time and, 𝜖 =
𝜌𝑝
𝜌𝑔
 is the ratio of droplet and gas densities. 
Much of the previous droplet breakup literature focuses on the 
high Weber number regime for large droplets. Poplavski et al. (2020) 
performed experiments at We ∼ 200 − 2300  and velocities of 𝑣𝑝𝑔 ∼
59 − 170  [m/s] generated by a shock wave. The deformation was 
measured and found to compare well with their simulated model. 
Recent experiments from Mizuno et al. (2022) studied droplets at We ∼
100 − 2200  created by a velocity of 𝑣𝑝𝑔 ∼ 52 − 190  [m/s] for 2.33 
[mm] droplets. They explored the wavelengths observed on the droplet 
surface and discussed the role of the Rayleigh–Taylor (RT) and Kelvin–
Helmholtz (KH) instabilities in breakup. Sharma et al. (2021) explored 
droplet breakup for droplets (0.5 [mm] ≤ 𝑑0 ≥ 2.9 [mm]) subjected 
to velocities of 𝑣𝑝𝑔 ∼ 55 − 360  [m/s] resulting in We ∼ 30 − 12000 . 
They suggested that although both RT and KH instabilities play a role 
in breakup, KH dominates if the droplet diameter is large. Both Mizuno 
and Sharma modeled drag and deformation effects but used constant 
drag coefficients (𝐶𝐷 = 0 .45 and 𝐶𝐷 = 1 .2 respectively), neglecting 
transient effects.
While there is abundant literature on high Weber number breakup 
for large droplets, capturing the morphology of small droplets at high 
velocities is difficult due to the small length and times scales in-
volved. For this reason, high-fidelity data for micrometer-scale droplet 
breakup at similarly high Weber numbers have remained elusive. Zhang 
et al. (2023) conducted shock-tube experiments using digital in-line 
holography on an array of 240 [μm] droplets at We ∼ 15 − 696  and 
velocities of 𝑣𝑝𝑔 ∼ 58−289  [m/s]. The authors proposed that the greater 
curvature of small droplets makes them harder to break apart at high 
We conditions, resulting in increased deformation times. Unfortunately, 
the low resolution of individual droplets in this experiment made it 
difficult to resolve deformation and breakup phenomena with high 
confidence. Thus, the role of drag and deformation on KH and RT 
instabilities driving small droplet breakup remains to be determined.
The analytical KH-RT model was proposed by Beale and Reitz 
(1999) to predict the primary atomization of liquid exiting a spray 
nozzle by the KH and RT instabilities. This model has since been 
adapted and applied in the field of droplet breakup. Here the KH 
instability is taken to continuously strip droplets from the periphery of 
the droplet due to shear forces, while the RT instability is responsible 
for a sudden breakup of the core droplet, similar to the catastrophic 
breakup mechanism proposed by Pilch and Erdman (1987). The RT 
mechanism is derived from the work of Bellman and Pennington (1954) 
where the most unstable wavelength, 𝜆𝑅𝑇 , and growth rate, 𝛾𝑅𝑇 are 
found. The KH mechanism was derived by Reitz and Bracco (1979) for 
the capillary instability of a round jet subjected to viscosity and shear 
effects. The most unstable wavelength, 𝜆𝐾𝐻 , and growth rate, 𝛾𝐾𝐻 are 
predicted using theory and curve-fit coefficients. The growth rate and 
wavelength of these instabilities are used to predict the time scales for 
breakup and the resulting child droplet sizes. These quantities depend 
strongly on the relative gas velocity (i.e. We) and droplet acceleration 
(see Eqs. 1–11 in Beale and Reitz (1999)). For this reason, an accurate 
prediction of the acceleration and velocity of the droplet is necessary 
for precise breakup modeling.
To predict the droplet acceleration, accurate modeling of the drag 
forces during deformation and breakup is essential. The drag coefficient 
International Journal of Multiphase Flow 193 (2025) 105372 
2

<!-- PDF_PAGE: 3 -->

V.O.D. W. et al.
of a droplet evolves over time as it deforms from a spheroid to a 
disk-like shape. Hsiang and Faeth (1995) found that this evolution 
is relatively independent of disturbance type, including We, Oh, Re, 
and 𝜖. Currently, the drag experienced by droplets is either estimated 
through empirical correlations or assumed to be constant, as discussed 
previously. For low Weber numbers (We ≤ 375), Chou and Faeth (1998) 
developed a correlation to determine the average drag coefficient (𝐶𝑑 ) 
of a droplet, which aligns well with experimental results. For all their 
test cases, 𝐶𝑑 increased during the deformation process, peaks just 
before bag formation at 𝑡∗ ≈ 2 , and then decreases rapidly as breakup 
progresses.
Simulations have also been used to study 𝐶𝑑 under unsteady con-
ditions. Meng and Colonius (2015) studied the early stages of breakup 
for water cylinders measuring acceleration and unsteady 𝐶𝑑 at We =
940 − 19 , 300+. They found that 𝐶𝑑 will increase for the duration of 
the deformation process when computed based on the initial column 
diameter, but remained approximately constant when the deformed 
diameter at each time step was used. Kékesi et al. (2014) conducted a 
study of the intermediate regime of droplet breakup using the Volume 
of Fluid (VOF) method for We = 20 , Re = 20 − 200  and 𝜖 = 0 .5 − 50 . 
They found that for all cases the droplet approached a maximum 𝐶𝑑
right before breakup, after which it decreased rapidly. From this, it was 
concluded that 𝐶𝑑 could be a useful parameter to predict breakup.
Since both the drag coefficient and droplet cross-sectional area 
depend on deformation, it is crucial to understand the deformation 
rate of the droplet. In contrast to breakup effects, droplet deforma-
tion is more predictable, and various models have been successful 
in predicting droplet deformation for large droplets over various We
ranges. Modeling of droplet breakup has been undertaken by various 
researchers using both empirical (Chou and Faeth, 1998; Hsiang and 
Faeth, 1992) and analytical methods (O’Rourke and Amsden, 1987). 
The TAB model is an analytical model originally proposed by O’Rourke 
and Amsden (1987). The droplet deformation process is considered 
a spring-mass system acted upon by external forces. In this paper, 
the original TAB model is referred to as OTAB. Several researchers 
have proposed improved versions of the OTAB model which can be 
found in the review paper by Stefanitsis et al. (2019). This paper also 
proposed an updated TAB model, validated at We < 350, by making the 
coefficients Weber number dependent, identified here as the improved 
TAB (ITAB) model.
Several factors differentiate deformation and breakup of small
droplets at high Weber numbers from the large droplet case. First, small 
droplets experience a higher acceleration and equilibrate with the gas 
flow more rapidly. The higher acceleration promotes RT breakup by 
increasing the growth rate and reducing the size of the most unstable 
wavelength. While previous work observed a KH dominated breakup 
process for millimeter-scale droplets (Sharma et al., 2021), the most 
unstable KH wavelength is only weakly dependent on the droplet size. 
It remains to be seen if the low ratio of droplet size to 𝜆𝐾𝐻 can affect 
KH growth for small droplets (e.g. 𝑑0 ∼ 𝜆𝐾𝐻 ). Evaporation is also 
usually neglected for larger drops, but may become significant for small 
droplets as their mass and thermal capacity is orders of magnitude 
less. To date, the effect of evaporation on droplet morphology and 
hydrodynamic instability has not been explored, but it is known that 
a diffuse interface density gradient will reduce hydrodynamic growth 
rates (Morgan et al., 2016). Micron-scale droplet breakup is also 
very sensitive to discrepancies in droplet drag due to deformation 
and this can have a large impact on lag times and trajectories for 
Euler–Lagrange simulations in this regime.
Table  1 summarizes some of the recent droplet breakup data avail-
able in the literature including what is presented in this paper. The vast 
majority of previously available experimental data is on the millimeter-
scale droplet regimes and covers a wide range of Weber numbers. 
While this provides ample data for applications where larger droplets 
are present, applications employing small droplets such as detonation-
driven combustion are largely unexplored. Similarly, little work has 
been presented to describe the unsteady 𝐶𝑑 of deforming droplets, and 
the constant values used vary widely, which will result in inconsistent 
prediction of acceleration and droplet velocity for breakup models.
This paper aims to advance the understanding of the physics of 
small droplets up to the onset of breakup. High-fidelity experiments 
have been conducted using state-of-the-art high-speed-shadowgraph-
microscopy to capture the spatial (0.5 <  FOV > 1 [mm] ) and temporal 
(10 [MHz]) evolution of droplet morphology from the initial shock 
interaction up to breakup. To do so, a range of droplet sizes (50 <
𝑑0 < 200 [μm] ) and a range of initial shock Mach numbers (𝑀𝑖) (1.3 <
𝑀𝑖 < 2.1) were used with three different fluids (water, acetone and 
dodecane) to measure the effects of evaporation, droplet deformation, 
and drag for a wide range of Weber numbers 100 < 𝑊 𝑒 < 6000. 
Experimental results are used to tune the TAB model and construct a 
drag model for unsteady conditions. Together these models accurately 
predict deformation, acceleration, and breakup initiation time. Finally, 
the results have been compared to the experimental data for millimeter-
droplets from Mizuno et al. (2022) at similar Weber number regimes 
to highlight the similarities and differences between micron-scale and 
millimeter-scale droplet deformation and acceleration.
2. Experimental facility and methodology
The following section describes the facility, equipment, and method-
ology used. In addition, the uncertainty in experimental initial condi-
tions is presented.
2.1. Experimental facility and equipment
Experiments were conducted at the Fluids Mixing at Extreme Con-
ditions Laboratory in the multiphase shock tube facility. This facility 
consists of three main sections, the driver, driven, and test sections. 
The driver section consists of a round carbon steel tube (1.67 [m], 254 
[mm] diameter, 25.4 [mm] walls) and is designed to withstand gauge 
pressures up to 15.2 [MPa]. Gas is pumped into the driver up to the 
pressure required to generate the desired shock. Diaphragms of various 
strengths are clamped between the driver and driven section via dual 
∼200 [kN] hydraulic rams. Stronger galvanized steel diaphragms drive 
the Mach 2.0+ shock waves, while polycarbonate diaphragms are used 
for lower Mach numbers, as seen in Table  2. A cross-shaped knife edge 
is set into the end of the driven section immediately downstream of the 
diaphragm to ensure a consistent rupture, increasing the repeatability 
of the experiment.
The driven section consists of a long square tube (190 [mm] width, 
19 [mm] wall thickness) fitted with pressure transducers just ahead of 
the test section to determine the shock velocity. The driven section’s 
main purpose is to develop the shock wave by providing enough 
distance for the influx of high-pressure gas from the driver to stabi-
lize and become planar. The test section is located after the driven 
section. Here a stream of droplets is introduced through a 1.5 [mm] 
orifice which restricts the outflow of gases after passage of the shock. 
The droplets are aligned using translation stages allowing micrometer-
accurate positioning of the droplets. Optical access is provided by 
round, 61 [mm] diameter acrylic windows mounted on each side of 
the test section, allowing a full view of the shock-droplet interaction 
via back-lit illumination.
The shock tube is outfitted with solenoid valves to control the 
initial conditions and shock initiation. Dynamic pressure transducers 
(PCB Piezotronics 113B26) are mounted in the side walls at various 
locations along the tube to record shock strength. Automated control 
and data acquisition is recorded utilizing a National Instruments data 
acquisition system (NI PXIe-1073) and a LabView program. This system 
enables the use of an automated shock firing sequence, providing 
highly accurate and repeatable (shock strengths varying by less than 
1 percent) experimental conditions, with rapid turn-around times (less 
than three minutes between trials). The interested reader can find more 
International Journal of Multiphase Flow 193 (2025) 105372 
3

<!-- PDF_PAGE: 4 -->

V.O.D. W. et al.
Table 1
Recent work on droplet breakup.
 Reference We Oh Re 𝑀 𝑉𝑔 𝑑0 [μm] 𝐶𝑑  
 Hsiang and Faeth (1995) 0.5–236 .0038 340–8250 1.01–1.24 5.3–123.5 1000 0.9–1.2 
 Poplavski et al. (2020) 200–2300 <0.002 9e3–26e3 1.1–1.34 59.8–170 2700 N/A  
 Sharma et al. (2021) 30–12 000 <0.002 3e3–10e4 1.1–1.85 55–360 500–2900 1.2  
 Mizuno et al. (2022) 120–2335 <0.003 7e3–20e3 1.1−1.39 51.9–190.1 2180–2350 0.45  
 This work. (2025) 100–6000 <0.03 7e2–10e3 1.35–2.00 180–480 50–200 Eq. (6) 
Table 2
Diaphragm and shock wave properties.
 𝑀𝑖 𝑣𝑔 [m∕s] 𝑃 [kPa] 𝑇 [K] Material Thickness [mm] Rupture [kPa-gauge] 
 1.37 ± 0.015 186 ± 6.9 202.2 ± 5.0 368.45 ± 2.9 Polycarbonate 0.254 207  
 1.58 ± 0.029 275.3 ± 11.6 274.5 ± 10.7 410.0 ± 6.0 Polycarbonate 0.762 690  
 2.08 ± 0.017 465.1 ± 6.0 488.3 ± 8.1 535.6 ± 4.0 Galvanized steel 0.610 4150  
information on the shock tube facility in Duke-Walker et al. (2020, 
2021, 2023) and Duke-Walker and McFarland (2024).
High-speed shadowgraph microscopy is employed to image the 
droplet development using a Specialized Imaging SIMX 16 high-speed 
camera equipped with a Distamax K-2 long-distance microscope lens. 
The magnification of the Distamax K-2 is adjusted and teleconverter 
lenses are equipped as needed to produce high-resolution images of 
micron-scale droplets, see Table  3. The camera is mounted to a custom 
aluminum frame equipped with a compound milling table to enable 
easy positioning through the use of manual lead screws with 25 [μm]
precision in the X and Z axes 1. Illumination is provided by a 400 
[W] Specialized Imaging SI-LUX640 laser at 643 [nm] equipped with 
collimating optics (50 [mm] condenser lens). The SIMX 16 camera 
captures 16 images using an array of individual intensified charge-
coupled devices (CCDs) with modular delay and exposure times down 
to 1 [ns]  (Specialised Imaging, 2024). Triggering is accomplished a 
built-in velocity trap. This system receives a voltage signal from two 
pressure transducers mounted 31.75 [mm] apart ∼118 [mm] ahead 
of the test section. This system allows the image timing to adapt to 
variations in the shock velocity, and provides accurate imaging of the 
shock-droplet intersection (±5 [ns]).
Droplets are generated using MicroFAB droplet dispensers (Mi-
croFAB, 2024). The droplet generation system consists of four main 
components: a waveform generator (CT-M5-01 JetDrive V), a pneu-
matic controller (CT-PT-21-0), a reservoir (C-04x-20-FC), and a low-
temperature piezoelectrically-controlled orifice (MJ-ATP-01). The dis-
penser is glass orifice with a diameter (𝑑𝑗 ) of 20, 40, or 60 [μm]
and is capable of dispensing fluids with viscosity less than 20 [cPs] 
and surface tensions ranging from 20 to 70 [mN/m]. The pneumatic 
controller features a three-state circuit, including pressure fill/purge, 
vacuum purge, and operating pressure control (MicroFAB, 2024). The 
dispenser is controlled by pressure from the pneumatic controller and 
the waveform generator at a maximum voltage of ±140 [V] and a 
frequency of 30 [kHz]. As explained in Section 2.2 these parameters 
are tuned to control the droplet size, velocity, and spacing. Lastly, the 
droplet dispenser is mounted on the camera frame to isolate it from 
vibration when the shock tube is fired. Positioning along the X and Z 
axes is accomplished using a micrometer stage (Thorlabs LX30) with a 
precision of 500 [μm∕rev] . This allows us to maintain consistent droplet 
positioning relative to the camera.
2.2. Methodology
To ensure proper operation of the droplet generator, it is imperative 
to maintain a high degree of cleanliness in and around the nozzle. High-
purity fluids are used to ensure the nozzle does not clog. The nozzle is 
thoroughly cleaned via back-flushing before installation into the system 
or if it is clogged during operation. All tubing and glassware supplying 
the nozzle are rinsed with the filtered liquid or appropriate cleaning 
solution. An in-line filter for the dispenser is swapped after switching 
fluids to maintain cleanliness.
After preparing the droplet generator, the camera system was cal-
ibrated. For each droplet size tested, different magnifications were 
required. The camera was focused and the imaging software calibrated 
by placing a calibration target into the focal plane located in the center 
of the shock tube (Fig.  1.) The camera and laser were adjusted using 
the camera positioning stage to ensure proper alignment. The exposure 
of each camera frame (16 CCDs) was adjusted until they registered an 
intensity of 3000–3200 (the maximum is 4095) evenly over the whole 
image.
Once the optical equipment was aligned, the droplet dispenser’s 
position is adjusted using the micrometer stage so the droplets are 
in the camera’s focal plane. Two preliminary images are taken before 
the shock tube is fired, a background image to assist in image post-
processing, and an image of the unperturbed droplets to confirm initial 
conditions (size and location). A diaphragm is then loaded to run an 
experiment, after which all procedures are controlled by the automated 
LabVIEW program. The driver is pressurized with nitrogen gas until 
right before the diaphragm’s rupture pressure. A fast-acting solenoid 
valve then releases high-pressure nitrogen gas, breaking the diaphragm 
and initiating the shock wave. The LabView system records the shock 
wave’s pressure history from the transducers at a rate of 1.25 [MHz]. 
The high-speed camera’s velocity trap, functioning at 25 [MHz], records 
the shock wave velocity from two the pressure signals and triggers the 
image acquisition.
2.3. Experimental conditions and uncertainty
This section provides the measured experimental initial conditions 
and describes the uncertainty associated with these quantities. The 
shock tube was initially filled with atmospheric air at 293 ± 1 [K] and 
100.3 ± 1 [kPa]. Temperatures were measured following the methods 
detailed in Duke-Walker and McFarland (2024) while pressure is taken 
from local weather data including typical variations. The post-shock gas 
properties are calculated from 1D gas dynamics using the shock velocity 
and initial conditions. The mean and standard deviation for the shock 
wave velocity and associate post-shock gas properties are presented in 
Table  2.
The shock velocity was estimated from the shock arrival time found 
at the pressure transducers (0–700 [kPa] delivering a signal of 0–5 [V]) 
mounted along the top of the driven section. The voltage threshold for 
shock detection was set to 0.75, 1.25, and 2 [V], for the three respective 
nominal shock strengths (𝑀𝑖 = 1 .3, 1.5, and 2). When this threshold is 
exceeded, the camera calculates the velocity of the shock and triggers 
imaging at the predicted shock/droplet interaction time.
Three liquids, Acetone (C3H6O), Dodecane (C12H26), and Water 
(H2O), were selected to explore the effects of both surface tension and 
vapor pressure (evaporation rate) on droplet dynamics. The properties 
for these fluids at their initial temperature (293 K), including the 
saturation pressure (𝑃𝑠𝑎𝑡), are given in Table  4 along with the prescribed 
nominal droplet size (𝑑𝑛) range.
International Journal of Multiphase Flow 193 (2025) 105372 
4

<!-- PDF_PAGE: 5 -->

V.O.D. W. et al.
Table 3
Data acquisition accuracy.
 𝑑0 [μm] [μm∕Pix] K2-lens FOV [mm × mm] Mag Gain 𝑡𝑒𝑥𝑝 [ns] 
 50 0.69/0.54 CF3+4X 0.88 × 0.66 & 0.68 × 0.51 9.2–12 6 9–13  
 100 0.78 CF3+2X 0.99 × 0.74 8.32 5 9–12  
 150/200 1.03 CF3+1.66X 1.32 × 0.98 6.25 4 8–10  
Fig. 1. Droplet imaging and generation.
Table 4
Fluid properties.
 Fluid 𝜌𝑝 [kg∕m3] 𝜎 [N∕m] 𝜇𝑝 [mPa s] 𝑃𝑠𝑎𝑡 [kPa] 𝑑𝑛 [μm]  
 C3H6O 790 0.0234 0.32 36.96 50–200  
 C12H26 750 0.0254 1.50 0.025 100–150 
 H2O 998 0.0720 1.00 3.17 150–200 
The characterization of the droplet involves three primary sources of 
uncertainty: (1) image resolution, (2) DDT algorithm uncertainty, and 
(3) experimental repeatability. The algorithm uncertainty encompasses 
the time approximation based on the droplet’s edge, the center of 
the shock thickness, and image resolution. These uncertainties were 
estimated using the binary algorithm, resulting in an approximate error 
of ±2 pixels. With this in mind, the initial droplet sizes (𝑑0) were 
measured from calibrated camera images prior to shock interaction. 
The uncertainty in size measurement was estimated, with a maximum 
uncertainty of ±4.1 [μm]  for 𝑑𝑛 values of 150 and 200 [μm], and a 
maximum uncertainty of ±2.2 [μm]  for 𝑑𝑛 = 50 [μm] . This error was 
attributed to both the edge detection algorithm and the maximum 
resolution of the camera.
When considering experimental repeatability, for each nominal 
droplet size, variations in the nozzle settings between runs resulted 
in additional small systematic errors in 𝑑0. That is, for each trial 
the droplet size was uniform, but variations in the droplet generator 
parameters (e.g. the pressure driving the liquid velocity) could result 
in variations in 𝑑0. Additionally, the Mach number attained in each 
trial could vary over a small range due to variations in the diaphragm 
material properties. The resulting droplet sizes produced and Mach 
numbers attained for each case are shown in Table  5. This table 
provides the estimated range of We, Oh, and the number of trials used 
for each case. Multiple trials were used to provide a data ensemble 
with increased temporal. More details of the individuals cases will be 
presented on Section 3.2.
3. Results
This section presents the experimental measurements of the droplet 
deformation, acceleration, and breakup initiation time. The qualitative 
evolution of the droplet morphology leading up to breakup is discussed 
first. The effects of droplet size and shock strength, and evaporation are 
then examined from the experimental measurements.
3.1. Droplet morphology evolution
Droplet deformation begins when the shock traverses the droplet, 
initiating momentum exchange between the droplet and gas. Due to 
the response time, the droplet initially remains stagnant. As a result, 
the droplet experiences a higher pressure and temperature on the 
windward face, while the velocity reaches a maximum at the equatorial 
region of the droplet. As the droplet accelerates, it deforms and its 
cross-sectional area increases, resulting in greater drag force until the 
breakup process initiates. During this time the hot post-shock gases heat 
the droplet and lead to simultaneous evaporation.
Fig.  2 shows a time series of images for acetone droplets at various 
conditions, increasing from We ∼ 110  (A) to We ∼ 6050  (F). As the 
We increases the size of the hydrodynamic structures shed from the 
droplet decreases. Image series (A) shows no ligament formation as 
the onset of breakup is delayed for lower We. Image series B shows 
larger more coherent ligament structures are shed from the droplet at 
late times. These structures become smaller and increasingly difficult to 
resolve as the We increases (C). At higher velocities, the ligaments are 
International Journal of Multiphase Flow 193 (2025) 105372 
5

<!-- PDF_PAGE: 6 -->

V.O.D. W. et al.
Fig. 2. Images of acetone droplet evolution: (A) 𝑑0 ∼ 55 [μm] − 𝑊 𝑒 ∼ 110 − 𝑀𝑖 ∼ 1 .32 (B) 𝑑0 ∼ 150 [μm] − 𝑊 𝑒 ∼ 458 − 𝑀𝑖 ∼ 1 .40 (C) 𝑑0 ∼ 150 [μm] − 𝑊 𝑒 ∼ 1090 − 𝑀𝑖 ∼ 1 .57 (D) 
𝑑0 ∼ 100 [μm] − 𝑊 𝑒 ∼ 2820 − 𝑀𝑖 ∼ 2.08 (E) 𝑑0 ∼ 150 [μm] − 𝑊 𝑒 ∼ 4350 − 𝑀𝑖 ∼ 2.06 (F) 𝑑0 ∼ 202 [μm] − 𝑊 𝑒 ∼ 6050 − 𝑀𝑖 ∼ 2.08.
International Journal of Multiphase Flow 193 (2025) 105372 
6

<!-- PDF_PAGE: 7 -->

V.O.D. W. et al.
Table 5
Initial conditions of all the experimental runs.
 Liquid Size [μm] 𝑀𝑖 𝑑0 [μm] range Mach range We range Re range Oh range  
 
Acetone
50
1.3 54.2–54.2 1.31–1.31 102.2–106.5 723.3–739.8 0.0102–0.0102 
 1.5 54.9–56.9 1.56–1.58 376.0–421.7 1442.3–1556.4 0.0100–0.0101 
 2.0 57.4–59.5 2.00–2.02 1489.5–1505.1 2954.7–2997.7 0.0097–0.0099 
 
100
1.3 94.6–96.9 1.35–1.39 235.1–300.4 1460.7–1672.4 0.0076–0.0077 
 1.5 92.3–98.8 1.55–1.58 611.0–737.6 2384.0–2699.1 0.0076–0.0078 
 2.0 93.0–101.7 2.06–2.10 2744.6–3126.4 5133.6–5642.4 0.0075–0.0078 
 
150
1.3 143.3–148.5 1.40–1.40 464.1–496.2 2543.8–2669.8 0.0062–0.0063 
 1.5 140.8–154.8 1.52–1.58 832.8–1111.6 3427.4–4145.5 0.0060–0.0063 
 2.0 149.7–155.4 2.06–2.08 4307.2–4505.1 8054.7–8388.8 0.0060–0.0061 
 
200
1.3 190.2–204.4 1.34–1.38 438.11–609.71 2821.8–3439.1 0.0053–0.0054 
 1.5 190.2–197.8 1.56–1.58 1327.9–1474.3 5081.6–5429.6 0.0053–0.0054 
 2.0 200.0–204.4 2.07–2.09 5797.3–6111.6 11 043.3–11 162.7 0.0053–0.0053 
 
Dodecane
100 2.0 98.45–98.45 2.08–2.09 2680.8–2760.9 5363.9–5439.1 0.0347–0.0347 
 
150
1.3 140.2–147.4 1.39–1.40 410.1–454.3 2463.3–2661.7 0.0283–0.0291 
 1.5 145.4–156.5 1.52–1.60 822.8–1085.4 3694.0–4209.6 0.0275–0.0285 
 2.0 146.4–155.9 2.06–2.10 3856.4–4438.0 7866.8–8672.6 0.0275–0.0284 
 
Water
150
1.4 153.3–162.0 1.41–1.43 170.78–187.4 2854.8–2988.2 0.0092–0.0095 
 1.6 154.3–157.6 1.60–1.61 400.6–416.2 4427.1–4560.5 0.0094–0.0095 
 2.1 150.0–157.6 2.09–2.13 1460.8–1595.3 8287.1–8775.5 0.0094–0.0096 
 
200
1.3 190.2–197.8 1.31–1.33 119.7–138.4 2639.0–2848.7 0.0084–0.0085 
 1.6 196.7–200.0 1.60–1.61 497.3–515.1 5566.5–5709.1 0.0083–0.0084 
 2.1 189.1–197.8 2.09–2.12 1896.1–2021.1 10 590.8–11 172.1 0.0084–0.0085 
Fig. 3. Images showing droplets near breakup initiation. Breakup initiation is marked with a star: (A) C3H6O–𝑑0 ∼ 95 [μm] − 𝑊 𝑒 ∼ 235 − 𝑀𝑖 ∼ 1.35 (B) C3H6O–𝑑0 ∼ 147 [μm] − 𝑊 𝑒 ∼
451 − 𝑀𝑖 ∼ 1.40 (C) C3H6O–𝑑0 ∼ 198 [μm] − 𝑊 𝑒 ∼ 1468 − 𝑀𝑖 ∼ 1.58 (D) C12H26–𝑑0 ∼ 147 [μm] − 𝑊 𝑒 ∼ 4134 − 𝑀𝑖 ∼ 2.09.
broken up into small droplets at formation and advected downstream 
rapidly (D-F). Additionally, faint bow shocks are observed when 𝑀𝑖 > 2
(highlighted in D&E), altering the fluid dynamics around the droplet.
The onset of breakup is difficult to measure quantitatively. Pilch and 
Erdman (1987) proposed that it can be marked when the first ‘‘mist’’ 
or child droplet is stripped from the parent droplet. This can be more 
challenging to determine at high We as child droplets are very small 
compared to the parent droplet. This has led to some uncertainty in 
the measure of breakup initiation time. Fig.  3 shows the evolution of 
several droplets near the onset of breakup where we mark the breakup 
time, as interpreted from the definition of Pilch and Erdman (1987), 
with a star. Here it can be seen that the morphology of breakup can 
be substantially different for low (Fig.  3(a) and (b)) and high (Fig. 
3(c) and (d)) We, making a more exact definition challenging. As 
We increases the non-dimensional breakup initiation time, 𝑡∗
𝑏,𝑖, was 
observed to decrease as discussed in Section 4.1 and with it the rate 
of deformation. In all following data plots, data obtained after the 
estimated breakup initiation time is designated with open markers, 
while data points before use closed markers.
Fig.  4 illustrates the morphology of breakup for high and low 
We droplets. At low-to-moderate Weber numbers, a bag-like structure 
is formed which leads to the formation of long coherent filaments. 
At this condition, droplet deformation has reached almost twice the 
droplet’s initial diameter. Small perturbations are observed on the 
droplet surface allowing a smoother transition to the flow field to 
strip the droplets. At moderate-to-high We, it is unclear if bag-like 
structures are formed and only short ligaments form, leading to the 
rapid formation of many small droplets. This is due to a high relative 
velocity between the droplet and the flow field, the generated mist is 
swept into the droplet wake, appearing cloud-like in the shadowgraph 
images. Shorter wavelengths are observed with higher growth rates, 
promoting an early formation of the child droplet mist.
3.2. Overall deformation rate
The overall cross-stream diameter is the result (sum) of the surface 
radial motion caused by stream-wise compression and outward growth 
of surface (KH) instabilities. At low We the KH instability produces 
a coherent liquid sheet that over time becomes thinner axially, folds 
towards the downstream direction, and eventually gets broken up by 
further instabilities. As the bulk liquid moves in the flow direction, the 
windward surface accelerates much faster than the center of mass and 
the leeward surface recedes at early times. The drag force that causes 
the bulk acceleration of the droplet is proportional to the frontal area, 
however, the influence of the stretched-out liquid sheet on the drag is 
unclear and it is difficult to ascertain the physically relevant effective 
International Journal of Multiphase Flow 193 (2025) 105372 
7

<!-- PDF_PAGE: 8 -->

V.O.D. W. et al.
Fig. 4. Schematic of droplet breakup morphology: (a) undisturbed droplet, (b-c) Low/moderate-Weber number, (d-e) Moderate/High-Weber number.
Table 6
Estimated uncertainty in measured parameters for each experimental case.
 Liquid Nominal size Nominal Mach [μm∕Pix] 𝛿𝑌 [±] 𝛿𝑥𝑑 [±μm] NRuns 
 
Acetone
50
1.3 0.69 0.12 1.39 2  
 1.5 0.66 0.18 1.39 5  
 2.0 0.54 0.09 1.07 2  
 
100
1.3 0.78 0.11 1.55 7  
 1.5 0.71 0.10 1.55 13  
 2.0 0.70 0.08 1.55 8  
 
150
1.3 1.03 0.08 2.06 6  
 1.5 0.84 0.08 2.06 13  
 2.0 0.66 0.06 2.06 5  
 
200
1.3 1.09 0.07 2.17 10  
 1.5 1.09 0.06 2.17 7  
 2.0 1.09 0.04 2.17 4  
 
Dodecane
100 2.0 0.78 0.07 1.55 2  
 
150
1.3 1.03 0.09 2.06 5  
 1.5 0.88 0.08 2.06 9  
 2.0 0.97 0.06 2.06 7  
 
Water
150
1.4 1.09 0.06 2.17 4  
 1.6 1.09 0.07 2.17 5  
 2.1 0.91 0.05 2.17 5  
 
200
1.3 1.09 0.05 2.17 5  
 1.6 1.09 0.06 2.17 4  
 2.1 1.09 0.05 2.17 3  
cross-stream diameter (𝑑𝑦). In the current study, 𝑑𝑦 is defined as the 
maximum spanwise distance of the contour obtained through image 
processing and is presented in non-dimensional form as 𝑌 . Beyond the 
breakup initiation time, the magnitude of 𝑌 is uncertain and should be 
taken with caution as it is heavily influenced by the ligaments captured 
by the binarization scheme and contour finding algorithm.
By utilizing error propagation we can find the error in deformation, 
𝛿𝑌 , for each frame assuming a maximum uncertainty of ±4 pixels in 𝑑𝑦. 
Then the uncertainty for a particular droplet size is given by Eqs. (1) 
and (2). The x-position of the center of mass, 𝑥𝑑 is taken as the centroid 
of the contour found. The uncertainty in 𝑥𝑑 is then approximately equal 
to 𝛿𝑑0∕2. The 𝑥𝑑 calculated from a 2D image may over-predict the 
actual center of mass of the droplet after breakup initiation, due to 
ligaments and child droplets captured by the contour finding algorithm. 
Table  6 shows the max uncertainty among different runs in 𝑌 , and 𝑥𝑑
for different size droplets. Since the initial time (time when the shock 
wave first intersects with the droplet) is estimated using the shock wave 
speed and distance between the wave and droplet edge, the velocity 
and position errors contribute to the uncertainty in time. The camera’s 
time resolution was less than 1 [ns], while the rise time of the pressure 
transducers was <1 [μs]  and thus dominated the uncertainty in time. 
The error in the wave speed measurements was found as a function 
of the uncertainty in position of the dynamic pressure transducers and 
their rise time and resulted in a maximum error of <2 [%] for the fastest 
shock waves. The uncertainty in droplet position was <0.5 [%] and 
combined with the velocity uncertainty to produce a total uncertainty 
in shock droplet interaction time of <2%, with the greatest uncertainties 
occurring for the highest shock wave Mach numbers. Here we have 
omitted the resulting error bars on plots where they cause the data 
points to overlap and obscure the results. They are included in later 
International Journal of Multiphase Flow 193 (2025) 105372 
8

<!-- PDF_PAGE: 9 -->

V.O.D. W. et al.
Fig. 5. Deformation of acetone droplets with increasing Weber number.
Fig. 6. Deformation of different sized Acetone droplets at similar shock strengths, Left: M ≈ 1.37, Center: M ≈ 1.56, Right: M ≈ 2.07.
plots of single cases, where data points are fewer, and serve to illustrate 
the predictable error bar ranges for other plots. 
𝛿𝑑 = 𝛿𝑑0 = 𝛿𝑑𝑦 = ±4 × micron per pixel (1)
𝛿𝑌 = 𝑌
√√√√
( 𝛿𝑑0
𝑑0
) 2
+
( 𝛿𝑑𝑦
𝑑𝑦
) 2
= 𝑌 𝛿𝐷
√
1
𝑑2
0
+ 1
𝑑2
𝑦
(2)
Previously, in the case of larger droplets (Mizuno et al., 2022; 
Poplavski et al., 2020), a higher We has been shown to produce an 
increase in deformation rate. This does not seem to be the case for small 
droplets. The deformation rate for the We ranging from 104 to 6000 
is plotted in Fig.  5. The general trend of higher deformation rate with 
increasing We for We < 300 is observed. Above We > 300, the influence 
of We on the deformation rate is seen to be weak. In the same way, 
it is important to note that the case with We = 2823  shows a slower 
deformation rate than We = 1470. This diminished influence of the We
suggests the greater impact of droplet size and/or shock strength at 
larger We.
With this in mind, we examine the increase in the Weber number 
while keeping the particle size and shock strength constant. When or-
ganized by common shock strength (Fig.  6), the data demonstrates that 
the deformation rate increases with the Weber number (droplet size). 
However, when organized by common sizes (Fig.  7), the trends are less 
clear with high Mach number cases showing slightly faster deformation 
at early times, particularly for larger sizes. This suggests that both shock 
strength and droplet size may have an impact on the deformation rate. 
Therefore, the next section will further investigate this relationship 
while maintaining consistent Weber number conditions.
3.3. Effect of droplet size and shock strength
To further explore the effect of the droplet size and shock strength, 
this section will quantitatively present the deformation characteristics 
of the droplets at similar Weber numbers. Since 𝑊𝑒 is a function of 
the liquid’s surface tension (𝜎), droplet size (𝑑0), gas density (𝜌𝑔), and 
the gas-droplet relative velocity (𝑣𝑝𝑔), similar We can be achieved by 
varying two of the three controlling parameters.
Fig.  8 shows the deformation of acetone droplets at similar We. The 
data at high We (Fig.  8 right) shows a clear difference between small 
droplets at high shock Mach number and large droplet ad low shock 
Mach number. To achieve these We there is also a shock Mach number. 
This suggests that the deformation dynamics are not only governed 
by We but also significantly influenced by the distribution of forces 
at varying scales and velocities. The extent to which this reduction 
is associated with the reduced droplet size or increased shock Mach 
number is not evident from this data.
Smaller droplets are accelerated more rapidly decreasing the inertia 
of the gas relative to the parent droplet, and decreasing the deformation 
International Journal of Multiphase Flow 193 (2025) 105372 
9

<!-- PDF_PAGE: 10 -->

V.O.D. W. et al.
Fig. 7. Deformation of different sized acetone droplets at different shock strengths. Left: 𝑑𝑛 = 100 [μm] , Center: 𝑑𝑛 = 150 [μm] , Right: 𝑑𝑛 = 200 [μm] .
Fig. 8. Deformation of different sized acetone droplets at similar We.
Fig. 9. Deformation of different sized acetone and water droplets at similar Mach and Weber Number.
rate. The surface hydrodynamics of small droplets are also reduced as 
the most unstable wavelengths for the gas and liquid conditions may 
be too large to form on the droplet surface (e.g. wavelengths larger 
than the droplet radius are prohibited). The lack of surface instabilities 
may reduce the deformation measured by the techniques used here. To 
examine the droplet size dependence a comparison of smaller acetone 
droplets with larger water droplets at similar We and incident Mach is 
presented in Fig.  9. For these conditions the deformation rate seems to 
have a smaller decrease with droplet size at high We (Fig.  9 right). As 
before, the deformation rate is more similar for the lower We cases.
As shock Mach numbers increase, the corresponding rise in gas 
velocity enhances compressibility effects within the droplet’s flow dy-
namics impacting the deformation rate. This observation aligns with 
the findings of Wang et al. (2020), which reported experiments on 
millimeter-sized water droplets at constant Weber numbers. These ex-
periments demonstrated that higher flow Mach numbers led to reduced 
deformation rates, a counterintuitive behavior due to the suppression 
of KH instability growth (Karimi and Girimaji, 2016), which plays a 
crucial role in the dynamics of droplet deformation.
To analyze the influence of shock strength on droplet deformation 
with similar We values, the behavior of same-sized acetone and water 
droplets at varying 𝑀𝑖 (incident Mach numbers) is presented in Fig. 
10. It can be observed that a small increase in shock strength results 
in a decrease in the deformation rate for the low-We case. However, as 
the We increases further, the deformation behavior becomes harder to 
distinguish. A similar deformation history is seen for cases with We =
586 and We = 1942  (Fig.  10, right) and suggest that, for small sized 
droplets interacting with strong shock waves, the Weber number is not 
sufficient for complete characterization of the deformation behavior.
It should be noted that the surface instabilities on the droplet 
are smaller at higher shock Mach numbers (e.g. the most unstable 
wavelength is smaller at higher velocities) leading to a reduced droplet 
International Journal of Multiphase Flow 193 (2025) 105372 
10

<!-- PDF_PAGE: 11 -->

V.O.D. W. et al.
Fig. 10. Deformation of similar sized acetone and water droplets at different incident Mach numbers. Note that the rightmost figure shows data at different We, but displays a 
similar deformation.
Table 7
Empirical correlations for breakup initiation time.
 Author Year Model We Range 𝑑0 [μm]  
 Pilch and Erdman (1987) 1987 𝑡∗
𝑏,𝑖 = 1.9(𝑊 𝑒 − 12)−0.25(1 + 2.2𝑂ℎ1.6) 10 < 𝑊 𝑒 < 10 000 500−3000 
 Hsiang and Faeth (1992) 1992 𝑡∗
𝑏,𝑖 = 1.6∕(1 − 𝑂ℎ∕7) We < 103 500−1500 
 Poplavski et al. (2020) 2020 𝑡∗
𝑏,𝑖 = 0.36 𝑊 𝑒 > 250 2700  
 Duke-Walker et al. (2021) 2021 𝑡∗
𝑏,𝑖 = min(3, 3.328𝑊 𝑒−0.1310) We < 80 10−30  
 Current model 2025 𝑡∗
𝑏,𝑖 = 1.9(𝑊 𝑒 − 12)−0.25 + 0.164 100 < 𝑊 𝑒 < 6000 50−200  
deformation rate. These results underscore the intricate interplay be-
tween shock strength and droplet size, and surface instability in in-
fluencing droplet deformation behavior. Since our study was limited 
to smaller droplet sizes, it is hard to decouple the effects of shock 
strength and droplet size. Ultimately, both effects combine to reduce 
the growth of surface instabilities. Further comparisons with much 
larger droplets will be shown in Section 4.3 comparing our results to 
those from Mizuno et al. (2022).
4. Modeling of experimental results
It is essential to correctly predict the droplet deformation and 
acceleration in order to accurately predict the droplet trajectory and 
breakup mechanisms. The droplet acceleration is affected by its chang-
ing shape and subsequent breakup causing a deviation from the tra-
jectory predicted by the models developed for rigid spheres. In this 
section, existing models for breakup initiation time, deformation, and 
droplet acceleration are compared with current experimental data and 
improved models are developed.
4.1. Breakup initiation model
The onset of breakup is either marked by a certain value of 𝑌 or 
non-dimensional time 𝑡∗ in deformation and breakup models. Values 
of 𝑌 in the range of 1.5 to 2 have generally been used in literature as 
the breakup initiation point. For instance, breakup is predicted to start 
once 𝑌 = 1 .5 is reached in the original TAB model. The deformation 
models based on the curve-fit expressions of experimental data tend to 
provide a non-dimensional breakup initiation time, 𝑡∗
𝑏,𝑖 as a function of 
We and/or Oh. A few empirical correlations for the estimation of 𝑡∗
𝑏,𝑖, 
along with their validity range, are tabulated in Table  7.
The variation of 𝑡∗
𝑏,𝑖 with We observed in the current work are 
plotted in Fig.  11 along with the predictions from other We dependent 
correlations. Breakup initiation times in the bag breakup regime (We <
100) tend to be the same order of magnitude as the characteristic 
breakup time, i.e, 𝑡∗
𝑏,𝑖 ≈ 1. The We range of all the current experiments 
are in the shear breakup regime and values of 𝑡∗
𝑏,𝑖 < 1 are observed. 
A sharp logarithmic type decrease in breakup initiation time is seen 
in the early period of the shear breakup regime as the We increases 
from 100 to 1000. However, for We > 1000 the breakup initiation time 
shows a weak dependence on We and goes from ≈0.44 at We ∼ 1000
to ≈0.38 at We ∼ 6000 . This asymptotic value of 𝑡∗
𝑏,𝑖 aligns with the 
findings of Poplavski et al. (2020) at large We, where the authors report 
𝑡∗
𝑏,𝑖 ≈ 0 .36 at We >∼ 250 for millimeter-sized droplets. The correlation 
from Duke-Walker et al. (2021) was found to over predict the breakup 
initiation time for the cases considered here.
4.2. Deformation and trajectory model
The shock-induced motion of a droplet can be modeled by evalu-
ating the drag force, 𝐅𝑑 , experienced by it and is given by Eq.  (3), 
where 𝑚𝑝, 𝐯𝑝 and 𝐚𝑝 are the droplet mass, velocity and acceleration 
vectors; and 𝐯𝑔 is the gas velocity vector. The frontal area of the droplet 
projected in the plane perpendicular to the direction of the flow is 𝐴𝑓
and 𝐶𝑑 is the coefficient of drag. The values of 𝐴𝑓 and 𝐶𝑑 depend on 
the shape of the deforming droplet. Considering the thermodynamic 
properties to be constant until breakup, Eq.  (3) can be rearranged to 
be a function of non-dimensional deformation 𝑌 as presented in Eq. 
(4). 
𝐅𝑑 = 𝑚𝑝𝐚𝑝 = 1
2 𝐴𝑓 𝐶𝑑 𝜌𝑔| 𝐯𝑔 − 𝐯𝑝| (𝐯𝑔 − 𝐯𝑝) (3)
𝑑𝐯𝑝
𝑑𝑡 = 3
4
𝜌𝑔
𝜌𝑝𝑑0
𝑌 2𝐶𝑑 | 𝐯𝑔 − 𝐯𝑝| (𝐯𝑔 − 𝐯𝑝) (4)
If the variation of 𝑌 and 𝐶𝑑 with time is known, Eq.  (4) can 
be integrated to get the velocity and position of the droplet. In an 
attempt to create a predictive model for droplet motion behind a 
shock, the deformation and position of the droplets obtained from the 
experiments are utilized to assess and/or modify existing deformation 
and drag models. For deformation, the OTAB model is utilized in its 
non-dimensional form as presented in Eq.  (5). 
𝑑2𝑌
𝑑𝑡∗2 + 4𝐶𝛿
𝑂ℎ√
𝑊 𝑒
𝑑𝑌
𝑑𝑡∗ + 8𝐶𝑘
𝑊 𝑒 (𝑦 − 1) = 4 𝐶𝑓 (5)
This equation consists of three coefficients, 𝐶𝛿, 𝐶𝑘 and 𝐶𝑓 whose 
values affect the time history of the droplet deformation. Previous re-
searchers have suggested different values for these constants, however 
universal values are not agreed upon. The original constants given by 
O’Rourke and Amsden (1987) and Weber number dependent values 
proposed by Stefanitsis et al. (2019) are tabulated in Table  8.
For the low Ohnesorge (Oh < 0.1) and high Weber numbers 
(We > 100) of the experimental cases in the current work, the effect 
International Journal of Multiphase Flow 193 (2025) 105372 
11

<!-- PDF_PAGE: 12 -->

V.O.D. W. et al.
Fig. 11. Comparison of non-dimensional breakup initiation time given by different models with current experimental data.
Table 8
TAB model constants.
 𝐶𝛿 𝐶𝑘 𝐶𝑓  
 OTAB, O’Rourke and Amsden (1987) 5 8 1/3  
 ITAB, Stefanitsis et al. (2019) 10 − 1.32 + 0.12𝑊 𝑒, 𝑊 𝑒 < 20
7.87 − 0.13𝑊 𝑒, 𝑊 𝑒 < 60
0 𝑊 𝑒 ≥ 60
0.13 + 0.0026𝑊 𝑒, 𝑊 𝑒 < 20
0.46 + 0.0022𝑊 𝑒, 𝑊 𝑒 ≥ 20
 
 MTAB, present work 5 8 1  
of constants 𝐶𝛿 and 𝐶𝑘 is diminished and the deformation rate is 
primarily determined by the value of 𝐶𝑓 , with larger values giving 
faster deformation. In these cases, the 𝐶𝑓 from Stefanitsis et al. (2019) 
monotonically increases with Weber number and will always give a 
faster deformation rate than the OTAB model.
In the current work, different values of 𝐶𝛿, 𝐶𝑘 and 𝐶𝑓 were tested, 
and 𝐶𝑓 = 1 was found to correctly predict the deformation. The effect 
of variation of 𝐶𝛿 and 𝐶𝑘 was negligible hence, the values from OTAB 
were used. Fig.  12 shows the comparison of the three versions of the 
TAB model for We ranging from 127 to 6000. The OTAB model is 
seen to underpredict the deformation for all the cases while the ITAB 
model is able to reasonably predict the deformation until We ∼ 550 , 
beyond which it starts to overpredict the deformation. The deviation 
continues to increase with increasing We. The current modified TAB 
model (MTAB) is seen to accurately represent the deformation until 
breakup initiation for wide range of We.
The MTAB model assumes the shape of the deformed droplet to be 
an ellipsoid. To better understand the under-prediction of the deforma-
tion from the MTAB model, the contour of the droplet shape predicted 
by the model is overlayed on top of the contour of the deforming 
droplet extracted from the experimental images and is compared. Fig. 
13 shows the overlayed contour plots for We ∼ 594 and 1474. The major 
dimension of the ellipse (𝑑𝑦) is seen to align with the experimental 
contour for early times. Around the breakup initiation time (shown 
with red star), radial growth of liquid sheet is seen around the equator 
which grows much faster than the radial elongation of the bulk fluid 
volume due to deformation. The sheet formed from the growth of the 
surface instabilities elongates much further from the ellipse at later 
times, increasing the discrepancy in the predicted deformation. The 
MTAB model under-predicts the total deformation of the droplets at 
later times because it was not formulated to predict the growth rate of 
surface instabilities.
For the prediction of the particle acceleration in an unsteady flow, 
Parmar et al. (2009) suggests decomposition of the particle forces 
experienced into quasi-steady, inviscid unsteady, viscous unsteady, lift 
and gravity terms. Parmar et al. (2009) developed force kernels for 
the inviscid unsteady component of the force containing exponential 
and periodic terms that take into account the changing flow field. 
In the present work, the coefficient of drag is decomposed into an 
unsteady term and a quasi-steady term and a correlation for each is 
used to create a reduced order model for the force in the form of Eq. 
(3). From previous studies (see, Parmar et al. (2009), and Osnes and 
Vartdal (2022)) on the drag coefficient history of a solid sphere under 
shock wave loading, it is known that the 𝐶𝑑 depends on both the Mach 
number of the shock relative to the pre-shock gas (and consequently 
the particle Mach number) and the Reynold’s number of the droplet in 
the post-shock region. 𝐶𝑑 reaches a peak value when the shock wave is 
about halfway through the droplet then decays to a quasi-steady value. 
Thus, it can be modeled as a sum of the unsteady term (𝐶𝑢) that rises 
and drops quickly and a quasi-steady term (𝐶𝑞) as shown in Eq.  (6). 
𝐶𝑑 = 𝐶𝑢(𝑀𝑝, 𝑅𝑒, 𝑡) + 𝐶𝑞(𝑀𝑝, 𝑅𝑒, 𝑌 , 𝑡) (6)
For a deforming droplet, the quasi-steady term, 𝐶𝑞, is modeled as a 
function of droplet relative Mach number, 𝑀𝑝, Reynolds number and 
deformation. Since the droplet starts as a sphere and flattens as it 
evolves, 𝐶𝑞, is taken as the weighted average of the drag coefficient 
of a sphere, 𝐶𝑞,𝑠, and the drag coefficient of a disk, 𝐶𝑞,𝑑 , see Eq.  (7). 
𝐶𝑞 = 𝐶𝑞,𝑠(1 − 𝐹 ) + 𝐹 𝐶𝑞,𝑑 , 𝐹 = 1 − 1∕ 𝑌 6 (7)
The correlation for 𝐶𝑞,𝑠 is taken from Loth et al. (2021) and is pre-
sented in Eqs. (8)–(11). For 𝐶𝑞,𝑑 , first the experimental data from Roos 
and Willmarth (1971) is fit to a form similar to that used by Clift and 
Gauvin (1971) for a sphere, then a Mach correction coefficient, 𝐶𝑀,𝑑
is applied to account for compressibility effects at high Mach numbers. 
Eq.  (12)–(13) give the mach corrected quasi-steady drag coefficient for 
a disk (𝐶𝑞,𝑑 ). 𝐶𝑀,𝑑 is assumed to be equal to the Mach correction factor 
𝐶𝑀 . 𝐶𝑀 captures the effect of Mach numbers at high Reynolds numbers 
for spheres and, since an established model for Mach correction for 
disks is lacking, it is used here for disks too. 
𝐶𝑞,𝑠 = 24
𝑅𝑒 (1 + 0.15𝑅𝑒0.687
𝑝 )𝐻𝑀 + 0.42𝐶𝑀
1 + (42500∕𝑅𝑒1.16𝐶𝑀
𝑝 ) + (𝐺𝑀 ∕𝑅𝑒0.5
𝑝 )
(8)
International Journal of Multiphase Flow 193 (2025) 105372 
12

<!-- PDF_PAGE: 13 -->

V.O.D. W. et al.
Fig. 12. Measured deformation of 𝑑0 = 200 μm  droplets compared to models. Top: Water droplets. Bottom: Acetone droplets.
Fig. 13. Overlay of MTAB model predicted contours with deforming acetone droplet contours from experiments keeping the same centroid for both. (a) 𝑑0 ∼ 204, 𝑀 ∼ 1.38, We ∼ 594
(b) 𝑑0 ∼ 198, 𝑀 ∼ 1.58, We ∼ 1474.
𝐶𝑀 =
{
1.65 + 0.65 tanh (4𝑀𝑝 − 3.4) 𝑀𝑝 < 1.5
2.18 − 0.13 tanh (0.9𝑀𝑝 − 2.7) 𝑀𝑝 ≥ 1.5
(9)
𝐺𝑀 =
{
166𝑀 3
𝑝 + 3.29𝑀 2
𝑝 − 10.9𝑀𝑝 + 20 𝑀𝑝 < 0.8
5 + 40𝑀 −3
𝑝 𝑀𝑝 ≥ 0.8
(10)
𝐻𝑀 =
⎧
⎪
⎨
⎪⎩
0.023𝑀 3
𝑝 + 0.212𝑀 2
𝑝 − 0.074𝑀𝑝 + 1 𝑀𝑝 < 1
0.93 + 1
3.5+𝑀 5𝑝
𝑀𝑝 ≥ 1 (11)
𝐶𝑑,𝑑 = 24
𝑅𝑒 (1 + 0.1𝑅𝑒0.814) + 0.86
1 + 13360∕𝑅𝑒1.368 (12)
𝐶𝑞,𝑑 = 𝐶𝑀,𝑑 𝐶𝑑,𝑑 , 𝐶 𝑀,𝑑 = 𝐶𝑀 (13)
For the unsteady term, a new correlation for the unsteady drag 
coefficient for a sphere is formulated as a function of 𝑀𝑝, Re and 
the non-dimensional shock transit time 𝜏𝑠. The correlation consists of 
both exponential decay and periodic terms. The experimental results 
of Sun et al. (2005) and Skews et al. (2007), and the numerical results 
International Journal of Multiphase Flow 193 (2025) 105372 
13

<!-- PDF_PAGE: 14 -->

V.O.D. W. et al.
Fig. 14. Comparison of the drag coefficient calculated using the current correlation at different Reynold’s number to that from Sun et al. (2005)(left), at different Mach numbers 
to that from Osnes and Vartdal (2022) (center), and at low Mach numbers to that from Skews et al. (2007) (right).
reported by Osnes and Vartdal (2022) for different Mach numbers and 
Reynolds numbers are curve fitted to get the correlation as presented 
in Eqs. (14)–(17). 
𝐶𝑢,𝑠 = 𝐴𝑒𝑥𝑝(−3𝜏𝑠)(𝐵sin(𝐵𝜏𝑠) − 3cos(𝐵𝜏𝑠)) + 3𝐴𝑒𝑥𝑝(−𝐶𝜏 𝑠) (14)
𝐴 = (0.1 + 35.438∕(5.6𝑒 − 02 + 18.897𝑀 2
𝑝 + 70.3𝑀 4
𝑝 )) ∗ (1 + 1.2∕𝑅𝑒0.5) (15)
𝐵 = 1.6 + 3.282∕(1. + 𝑒𝑥𝑝(−6.616(𝑀𝑝 − 0.9))) (16)
𝐶 = 0.2 + 3.163∕(1 + 0.838𝑀 2
𝑝 + 8.039𝑀 4
𝑝 ) (17)
For the smooth transition of drag coefficient from 𝐶𝑑 = 0 at 𝜏𝑠 = 0
to 𝐶𝑞 at later time, the quasi-steady term is increased from zero to the 
final value within 𝜏𝑠 = 2. Eq.  (18) represents the final equation for the 
instantaneous 𝐶𝑑 of a deforming droplet. 
𝐶𝑑 = 𝐶𝑢,𝑠 + (1 − 𝐹 )[𝐶𝑞,𝑠(1 − 𝑒𝑥𝑝(−5𝜏𝑠))] + 𝐹 𝐶𝑞,𝑑 (18)
Fig.  14 shows a comparison of 𝐶𝑑 of the rigid sphere obtained 
from the present correlation to that reported in Sun et al. (2005), 
Osnes and Vartdal (2022), and Skews et al. (2007) (digitized from 
published images). The correlation correctly predicts the decreasing 
peak with the Mach number and the increasing peak with the Reynolds 
number. The overall time history of the drag coefficient is very well 
predicted except for the depression observed at around 𝜏𝑠 ∼ 2 .5 for 
the low Mach number (𝑀𝑠 = 1 .22) and high Reynolds number case. 
To evaluate the performance of the correlation at Mach numbers closer 
to 1, the experimental results of Skews et al. (2007) for 𝑀𝑠 = 1 .08 is 
compared with that of the new correlation, and the prediction is found 
to be of sufficient accuracy. It is observed that the peak value of the 
drag coefficient (unsteady part) decreases while the quasi-steady value 
increases with increasing Mach number. It is also seen that the Mach 
number has a greater impact on the unsteady peak value compared to 
the Reynolds number.
Figs.  15 and 16 show the comparison of the predicted x-position 
of the droplets with the experimental values obtained for 200 [μm]
water and acetone droplets respectively. The average We and 𝑑0 for all 
trials of the various cases are used to calculate a single representative 
trajectory. The figures show the different trajectories obtained by using 
the quasi-steady drag coefficient of a rigid sphere (QS-Sphere), quasi-
steady drag coefficient of a deforming droplet (QS-Ellipsoid) and the 
full unsteady drag formulation for deforming droplets (US-Ellipsoid). It 
can be observed that the dynamic drag model that takes into account 
both the deformation and unsteady drag term is able to predict well the 
trajectory of the experiments while the quasi-steady drag correlations 
under-predict the x-position of the droplets. It is worth noting that the 
inclusion of the unsteady term becomes more important as the Mach 
number gets closer to 1. The trend in variation of the instantaneous 
drag coefficient with time is similar in all the cases. A sharp rise and 
fall of 𝐶𝑑 takes place as the shock passes through the droplet which 
is almost spherical at this time. With time the effect of deformation in-
creases and the decreasing 𝐶𝑑 starts to rise up again due to deformation 
and eventually settles to a quasi-steady value.
Fig.  17 shows the deformation and trajectory plots as predicted by 
the new model for Acetone droplets of nominal sizes 50, 100 and 150 
[μm]. The deformation for all the cases is predicted well for early times, 
however the experimental deformation closer to breakup initiation, 
when the ligaments influence the total span-wise diameter value, and 
beyond is larger than the deformation obtained from the model. With 
regards to the position, a similar trend of under-prediction from the 
model is observed after breakup initiation. This discrepancy can be 
attributed to the higher acceleration gained by the droplet as its mass 
is reduced by breakup. A similar trend, not shown here, is seen for 
dodecane and water droplets as well.
The considerable growth of liquid sheets (or longer ligaments) can 
have a contrasting effect on the acceleration. On the one hand, the 
drag force is increased due to the increased frontal area. On the other 
hand, the total inertial force gets divided between elongating the sheet 
and accelerating the bulk mass. Closer agreement of the predicted 
x-location indicates that it might be sufficient to capture the bulk 
deformation of the droplet for sufficiently accurate prediction of the 
drag coefficient and droplet core mass trajectory, even at times when 
the total deformation is under-predicted (see Fig.  17),
4.3. Model comparison with previous large droplet experiments
In order to test the performance of the deformation and trajectory 
model for a wider range of droplet sizes and shock wave Mach numbers, 
the experimental results of shock induced deformation of millimeter 
sized droplets reported in Mizuno et al. (2022) is compared against 
the model predictions. Four representative Weber numbers, spanning 
the range presented (We = 120 − 2335 ) from the eight different cases 
reported in Mizuno et al. (2022) are discussed here. Fig.  18 shows the 
experimental values digitized from the images with the results from 
the model at different Weber numbers. It can be seen that the model 
accurately predicts the deformation at We = 120  and We = 624 , 
however, large under-prediction is seen for higher Weber numbers 
(We = 1441  and 2335). Similarly, the model is able to predict the 
trajectory with accuracy until breakup initiation. Beyond breakup the 
predictions begin to deviate due to several factors. Since the mass 
reduction due to breakup is not taken into account the acceleration 
and consequently the x-position is underpredicted. In addition, once the 
droplet starts to shed mass, there is larger uncertainty in the location 
of the centroid obtained from the shadowgraphy images because the 
parent droplet is obscured by the mist of small child droplets.
To compare the morphological evolution of small micrometer-sized 
droplets from the current experiments to that of millimeter sized 
droplets, the contour of the deforming droplets from Mizuno et al. 
International Journal of Multiphase Flow 193 (2025) 105372 
14

<!-- PDF_PAGE: 15 -->

V.O.D. W. et al.
Fig. 15. Comparison of droplet trajectories with different drag correlations for 200 μm water droplets. Only values before breakup initiation are shown for clarity.
(2022) is scaled and overlaid on top of the contour obtained in this 
work. Fig.  19 shows the overlaid contours at similar 𝑡∗ for the Weber 
numbers ∼120 (200 [μm]  and 2.3 [mm]) and ∼1450 (150 [μm]  and 
2.1 [mm]). It is observed that the contours align almost perfectly for 
We ∼ 120 , however for the case with We ∼ 1450 , the 2 [mm] droplet 
shows a substantial amount of liquid sheet growth compared to the 
150 [μm] droplet. This radial growth is the result of KH instability and 
the shorter protrusions (ligaments) on the 150 [μm] droplet suggests 
lower growth of surface instabilities in small sized droplets subjected 
to a strong shock. This also explains the larger deviation observed 
between experimental deformation and that predicted by the model for 
higher Weber numbers in larger sized droplets. The TAB deformation 
model accounts only for the deformation due to bulk compression 
of the droplet and is agnostic to the increase in total deformation 
brought by the growth of surface instabilities. Hence, for cases where 
the effect of surface instabilities is minimal and the total deformation is 
dominated by bulk compression, the model predictions match well with 
the experimental values but with the increasing influence of surface 
instabilities on total deformation, the degree of deviation rises.
4.4. Model implications for droplet breakup
As previously discussed, small droplets require a larger shock wave 
Mach number to attain the same We as the large sized droplets. 
Hence, small droplets experience an enhanced effect of gaseous phase 
compressibility and this manifests as an increased value of quasi-steady 
drag coefficient. Fig.  20 shows the variation of 𝑀𝑝 and We with shock 
wave Mach number, 𝑀 for small and large sized droplets. For the same 
We, say 5000, the particle Mach number for a 2 mm water droplet 
is less than 0.6 whereas for a 200 μm  acetone droplet, it is above 
0.9. This larger value of 𝑀𝑝 results in an increased drag coefficient 
and decreased growth of KH surface instabilities, especially for small 
droplets. Secondary atomization models based on the growth of surface 
instabilities (like KHRT models (Beale and Reitz, 1999)) require correct 
prediction of the unstable perturbation wavelengths (and their growth 
rates), and the correct representation of the compressibility effects 
becomes essential for these models’ predictive capability.
For deforming droplets, the early time acceleration is not constant 
but changes first due to unsteady effects of shock-droplet interaction 
and then with deformation. Fig.  21 shows the variation of 𝐶𝑑 and 
acceleration with 𝑡∗ until breakup initiation, 𝑡∗
𝑏,𝑖, for ∼50, ∼ 100  and 
∼200 μm acetone droplets. The 50 μm droplet at higher Mach number 
experiences a larger acceleration, not only due to its lower mass but 
also due to the higher 𝐶𝑑 . The RT-unstable wavelengths and their 
growth rates are a strong function of surface acceleration (here, droplet 
acceleration) however most of the analysis on RT induced droplet 
breakup in the previous literature have not considered this variable 
acceleration and the models developed are based on the constant 
quasi-steady acceleration.
Fig.  22 initial acceleration of the same sized rigid sphere with the 
Mach correction applied to 𝐶𝑑 (𝑎𝑝,𝑞𝑠). It is observed that the accelera-
tion before breakup initiation could rise by up to 10 times that of the 
rigid sphere, depending on the shock strength. The instability analysis 
for droplets subjected to a variable acceleration is out of the scope of 
present paper, however, we note that the acceleration strength drives 
both the most unstable wavelength, decreasing with 𝑎𝑝, and the growth 
rate, increasing with 𝑎𝑝. Furthermore, the RT instability is relatively 
long-lived and will depend on the history of acceleration. The trends 
observed in the droplet acceleration history suggest that future breakup 
models based on instability analysis need to consider both the greater 
acceleration due to Mach number, unsteady effects and deformation, 
and the unsteady nature of the acceleration.
International Journal of Multiphase Flow 193 (2025) 105372 
15

<!-- PDF_PAGE: 16 -->

V.O.D. W. et al.
Fig. 16. Comparison of trajectory with different drag correlations for 200 [μm] acetone droplet. Values until breakup initiation are only shown for clarity.
Fig. 17. Figure showing plots of the time history of the deformation and centroid location obtained from experimental images and model for acetone droplets of different sizes 
and shock strengths.
International Journal of Multiphase Flow 193 (2025) 105372 
16

<!-- PDF_PAGE: 17 -->

V.O.D. W. et al.
Fig. 18. Figure showing the comparison of model predicted deformation (top) and trajectory (bottom) for millimeter sized droplets (𝑑0 in mm) at different Weber numbers 
from Mizuno et al. (2022).
Fig. 19. Comparison of millimeter and micrometer sized droplet deformation and morphology. The orange shaded region shows the contours identified for millimeter-sized droplets 
from Mizuno et al. (2022). The blue dashed line shows the contour for micrometer sized droplets at similar We. Top: Orange shows a 𝑑0 = 2330 μm  droplet with We = 120 while 
the blue line shows a 𝑑0 = 158.8 μm droplet also at We = 120. Bottom: Orange shows a 𝑑0 = 2180 μm  droplet with We = 1440 while the blue line shows a 𝑑0 = 150.0 μm droplet at 
We = 1461.
Fig. 20. Variation of Particle Mach number and Weber number with shock wave Mach 
number.
5. Conclusions
Experiments were conducted to examine the deformation, accelera-
tion, evaporation, and initiation of breakup for small droplets at high 
Weber numbers. Droplet sizes ranged from 50 < 𝑑 0 < 200 [μm] using 
water, acetone, and dodecane, and shock wave Mach numbers between 
1.3 < 𝑀 𝑖 < 2.1 generated Weber numbers in the range of 100 < 𝑊 𝑒 <
6000. These conditions resulted in rapid breakup initiation times on 
the order of 2.5 < 𝑡 ∗
𝑏𝑖 < 15 [μs] . Droplet deformation and position 
were measured over time at high temporal and spatial resolution with 
many repeated trials, providing high data fidelity. The effects of shock 
strength, droplet size, and evaporation were examined using experi-
ments at similar Weber numbers using various parameter combinations. 
The effects of small droplet size and high Mach number combined to 
produce significantly lower deformation rates with minimal influence 
observed from the Weber number. Evaporation effects were found to 
be negligible for the deformation process of droplets over 100 μm .
The experimental results were compared with existing theoretical 
models to derive new correlations to predict the droplet deformation, 
acceleration and breakup initiation time, in micron-scale droplets. The 
breakup initiation time was found to follow empirical trends similar 
to those suggested by Pilch and Erdman (1987), but with a prescribed 
offset time. The predicted breakup time asymptotically approaches 
𝑡∗
𝑏,𝑖 ∼ 0 .4 at high Weber numbers similar to the findings reported 
by Poplavski et al. (2020). The droplet deformation rate was estimated 
using a modified version of the Taylor Analogy Breakup model (MTAB), 
which improves the performance of the original model by optimizing 
the 𝐶𝑓 parameter. The MTAB model showed strong agreement with 
the experimental data presented, out performing other deformation 
International Journal of Multiphase Flow 193 (2025) 105372 
17

<!-- PDF_PAGE: 18 -->

V.O.D. W. et al.
Fig. 21. Variation of droplet drag coefficient (top) and acceleration (bottom) until breakup initiation time.
Fig. 22. Ratio of unsteady acceleration of deforming droplets with the initial acceleration of a non-deforming sphere.
models. Additionally, a new drag model was proposed to estimate 
droplet trajectories during the deformation process. This model incor-
porates unsteady forces at the onset of deformation and accounts for 
changes in the frontal area, as predicted by the deformation model, 
throughout the process. The predicted drag coefficient changes signif-
icantly over the droplet deformation time resulting a notably different 
acceleration history. The accurate acceleration and droplet velocity 
history provided by this model are essential to improve modeling 
droplet breakup through Rayleigh–Taylor (RT) and Kelvin–Helmholtz 
(KH) hydrodynamic mechanisms.
The models were also compared to results for larger droplets (𝑑0 ∼
2 [mm] ) presented by Mizuno et al. (2022) in order to examine the 
effect of droplet size further. Smaller droplets exhibit less deformation 
when subjected to similar high Weber number conditions. This differ-
ence results from the reduced growth of surface instabilities on small 
droplets. Small droplets cannot support larger KH modes as those found 
on the millimeter-sized droplets. The smaller modes that form on small 
droplets are more susceptible to surface tension and their growth is 
suppressed by comparison. The MTAB model only captures the bulk 
droplet deformation and thus, it matches the deformation of the large 
droplets well at early times and at low Weber numbers, where surface 
instabilities do not contribute to the observed total deformation.
Experimental results for micrometer-sized droplets, when combine 
with earlier findings for millimeter-sized droplets, provide a more 
complex picture of droplet dynamics leading up to breakup. Lower 
deformation rates were observed for smaller droplets (𝑑0 ∼ 50 μm
vs. 200 μm ) and higher Mach numbers. Both effects can be attributed 
to a reduction in the growth rate of hydrodynamic instabilities. For 
small droplets, the surface is too small to support faster growing larger 
modes and the growth of the smaller modes that form are suppressed 
by surface tension effects. For high shock Mach numbers, the gas flow 
at the droplet surface approaches supersonic velocities and the growth 
rate of KH instabilities is reduced due to compressibility effects. The 
acceleration history was also found to differ significantly from previous, 
constant drag coefficient approaches, and is likely to significantly alter 
the growth of RT instabilities over the droplet lifetime. Ultimately, the 
Weber number alone is insufficient to describe droplet deformation and 
the conditions leading to KH and RT breakup mechanisms.
International Journal of Multiphase Flow 193 (2025) 105372 
18

<!-- PDF_PAGE: 19 -->

V.O.D. W. et al.
Fig. 23. Example of the output estimated from the algorithm.
Fig. 24. Deformation of acetone and dodecane droplets at similar Weber numbers (We ∼ 1000, ∼ 2750, ∼ 4200.).
CRediT authorship contribution statement
Vasco O. Duke W.: Writing – review & editing, Writing – origi-
nal draft, Visualization, Methodology, Investigation, Formal analysis, 
Conceptualization. Manoj Paudel: Writing – review & editing, Writ-
ing – original draft, Visualization, Validation, Investigation, Formal 
analysis. Jacob Keltz: Writing – original draft, Visualization, Investi-
gation. Jacob A. McFarland: Writing – review & editing, Writing – 
original draft, Resources, Project administration, Funding acquisition, 
Conceptualization.
Declaration of competing interest
The authors declare the following financial interests/personal rela-
tionships which may be considered as potential competing interests: 
Jacob A McFarland reports financial support was provided by National 
Science Foundation. Jacob A McFarland reports financial support was 
provided by Office of Naval Research. If there are other authors, they 
declare that they have no known competing financial interests or 
personal relationships that could have appeared to influence the work 
reported in this paper.
Acknowledgments
This work was funded in part by the National Science Founda-
tion, United States under award numbers 2053154 and 2332916, and 
by the Office of Naval Research, United States under award number 
N000142412252.
Appendix
A.1. Droplet generation
The droplet diameter is governed primarily by the orifice diameter 
(𝑑𝑗 ), fluid jet velocity (𝑣𝑗 ), and piezoelectric frequency signal (𝑓 ). 
Maintaining a ratio of 𝜆∕𝑑𝑗 ∼ 4.5 is desirable to produce a stable stream 
of droplets (Berglund and Liu, 1973), where 𝜆 = 𝑣𝑗 ∕𝑓 is the distance 
between perturbation peaks and the fluid jet diameter is assumed to 
be equal to the orifice diameter. The jet velocity is a function of the 
pressure applied and the orifice diameter used. The droplet diameter 
can be related by 𝑑0 = 3
√ ( 1.5𝜆𝑑𝑗
2) . For this work, the stability of the 
droplet was driven beyond the desired 𝜆∕𝑑𝑗 ∼ 4.5 as shown in Table  9 
since increasing the spacing between droplets, which scale with 𝜆, was 
desirable in order to reduce droplet-to-droplet interaction. The stability 
of the droplet stream and the droplet size were verified before firing 
each experiment to maintain a high level of precision.
The MicroFab JetDrive V waveform generator was used to generate 
sinusoidal waveforms up to 30 [kHz]. Higher frequencies, required to 
produce smaller droplets, were generated using a custom waveform, 
with 4 points to approximate a sine wave with two periods. This 
sinusoidal approximation was capable of supplying frequencies up to 
International Journal of Multiphase Flow 193 (2025) 105372 
19

<!-- PDF_PAGE: 20 -->

V.O.D. W. et al.
Table 9
Droplet generation settings.
 𝑑𝑛 [μm] 𝑑𝑗 [μm] 𝑣𝑗 [m/s] P [kPa] 𝑓 [kHz] 𝜆∕𝑑𝑗 Waveform [V] 
 50 20 6.0–7.5 53 29 13 Custom  
 100 40 6.4–7.0 40 18–20 9 Sinusoidal  
 150 60 7.5–8.0 40 12 11 Sinusoidal  
 200 60 7.4–7.6 40 6 22 Sinusoidal  
a value of ∼60 [kHz], beyond which the approximation deteriorates 
resulting in poor performance of the droplet generator 9.
A.2. Image acquisition and processing
Camera settings are adjusted for each experimental condition to 
enhance accuracy and reduce uncertainty for smaller droplet sizes. As 
shown in Table  3, smaller droplets require greater magnification to 
resolve the deformation process within the field of view (FOV). As 
the FOV shrinks, the sensor requires a greater light flux to resolve 
the droplet. To compensate for the reduced light due, the exposure 
time was increased to a maximum of 13 [ns]. Additionally, the sensor’s 
intensifier gain was tuned to ensure sufficient light without introducing 
excessive background noise relative to the droplet. Once the optimal 
balance of magnification, exposure time, and gain were found, the 
experiments could be conducted with minimal uncertainty and high 
resolution.
To analyze the data collected from the experiments, a MATLAB 
algorithm was developed to extract key information from individual 
images. The algorithm sequence can be seen in the code syntax 1. 
The main inputs include image white balance, background correction, 
spatial and size calibration, shock location, shock velocity, original 
time, and the size of the region of interest (ROI). A calibration image 
serves as a reference to correct any frame-to-frame variation in droplet 
location across the field. Each image acquisition is segmented into 16 
individual frames. The first frame, or the initial droplet location, is used 
to identify the droplet within the field of view. This is achieved by 
generating a binary image and applying a boundary tracing algorithm 
to determine the droplet’s center location and edge before shock arrival.
The 16 images are then centered on the droplet and cropped with 
an ROI three times the droplet diameter, following a binary scheme de-
scribed by Duke-Walker et al. (2023). The reference time and position 
are obtained using the initial droplet image, shock velocity, and shock 
position recorded on the reference image frame. Droplet boundaries 
are detected and boxed to measure maximum cross-stream droplet 
deformation. Lastly, a 2D area-projected (Cartesian coordinates) cen-
troid from the binary image is used to find the center of mass during 
deformation providing the particle location in time. This center of mass 
assumes that the contour represents a volume completely filled with 
fluid. As will be discussed later, this could result in some error if 
the droplet develops concavity, regions where mass is absent at lower 
values of 𝑟 (in 𝑟𝑍𝜃 cylindrical coordinates).
The initial droplet diameter is then used to find the deformation, 
defined as 𝑌 = 𝑑𝑦∕𝑑0, where 𝑑𝑦 is the current deformed diameter (major 
diameter). Non-dimensional breakup parameters (We, Oh, Re, and 𝑡𝑐 ) 
are calculated based on the initial shock conditions obtained from the 
velocity trap, as explained in Section 2.3. As shown in Fig.  23, the 
droplet’s metrics are determined by tracing its boundary (Fig.  23(a)). 
The deformation process begins as the shock travels through the droplet 
field (Figs.  23(b) to (d)). The deformed diameter is estimated from the 
maximum cross-stream extents of the droplet.
Algorithm 1 Droplet deformation tracking - DDT algorithm
for 𝑁𝑒𝑥𝑝 do 
Inputs 𝐼1−16, 𝜇𝑚𝑃 𝑖𝑥, 𝑇𝑑 & 𝑇𝑔, 𝑝𝑔, 𝑣𝑔
Initialize Calculate thermodynamic properties of gas and liquid 
STEP 1: Split frames into 16 individual images 
STEP 2: Calibrate droplet size, location and ROI. 
→ Replace pixels per [𝜇𝑚]
→ Estimate the location 
→ Cut ROI at least 3 times bigger droplet size.
STEP 3: Create binary image 
→ Create a binary image 
→ Adjust sensitivity and fudge-factor. 
→ Detect particle edge ’canny’ 
→ Infill edges and clear-borders 
→ Remove with built-in MATLAB function regionprops signal 
above undesired area.
STEP 4: Detect, Trace boundary and area centroid of droplet 
→ Built-in MATLAB function bwboundaries 
→ Obtain the maximum distances from boundary in x and y. 
→ Built-in MATLAB function regionprops
STEP 5: Compute droplet deformation (Y) and droplet 
displacement(𝑥𝑑 ) 
STEP 6: Calculate the time reference from the shock detection and 
droplet edge 
STEP 7: Compute breakup parameters
end for
A.3. Evaporation effects
Evaporation can affect droplet dynamics both by reducing the 
droplet mass and by modifying the gas properties at the droplet surface. 
To estimate the mass loss effects, an estimate of droplet lifetime is 
obtained using the classical 𝐷2 law. The evaporation time, 𝑡𝑒𝑣𝑎𝑝, is 
calculated by assuming a constant rate of evaporation following the 
formulation presented in Duke-Walker et al. (2023) and compared 
with the characteristic breakup time, 𝑡𝑐 , for three different cases (see 
Table  10). The timescale of breakup is found to be shorter than 
the evaporation time by about 4–5 orders of magnitude. While the 
dodecane droplets take about ten times longer to completely evaporate, 
the breakup initiation for both occurs far before the evaporation time, 
implying that mass loss will be insignificant and evaporation effects are 
limited to the modification of the droplet temperature and surrounding 
gas (film layer) temperature and composition.
The recent numerical study by Tarey et al. (2024) reports that high 
evaporation rates have the effect of suppressing the initial growth of 
Kelvin–Helmholtz instability by up to 30 [%]. Since the increase in total 
cross-stream diameter is a combined effect of bulk droplet compression 
and radial growth of surface instabilities, it is expected that evaporation 
will have a similar effect on the overall deformation behavior. To 
explore the impact of evaporation, the deformation behavior of a low 
vapor pressure liquid, Dodecane, is compared with that of Acetone, 
which has high propensity to evaporate. Dodecane and Acetone have 
very similar density, viscosity and surface tension but have a large 
difference (∼1000× at STP) in vapor pressure, thus making it easier to 
isolate the effect of evaporation at similar We and Re. The properties 
of the two liquids are tabulated in Table  4.
Fig.  24 shows a comparison of the deformation for acetone and 
dodecane at large Weber numbers (>900). It can be seen that the 
acetone cases typically have a slightly higher deformation rate, counter 
to the hypothesis that higher evaporation will reduce deformation rates. 
However, considering that the vapor pressure of acetone is 2–3 orders 
of magnitude larger than that of dodecane, the deformation observed is 
very similar, and the slight increase for the acetone droplet may be an 
effect of their slightly higher We. Thus, for droplets above 100 [μm] and 
International Journal of Multiphase Flow 193 (2025) 105372 
20

<!-- PDF_PAGE: 21 -->

V.O.D. W. et al.
Table 10
Time-scales of breakup and evaporation for acetone and dodecane.
 Liquid We M 𝑑0 [μm] 𝑡𝑐 [μs] 𝑡𝑒𝑣𝑎𝑝 [μs] 𝑡𝑒𝑣𝑎𝑝∕𝑡𝑐  
 Acetone 1006.3 1.56 146.5 10.3 5.6E5 ∼(104)  
 Dodecane 983.4 1.57 150.0 10.1 3.2E6 ∼(105)  
 Acetone 2854.5 2.08 96.1 3.3 1.1E5 ∼(104)  
 Dodecane 2720.9 2.09 98.5 3.2 2.9E5 ∼(105)  
 Acetone 4412.8 2.07 152.5 5.2 2.7E5 ∼(104)  
 Dodecane 4103.0 2.09 148.6 4.9 6.6E5 ∼ (105) 
shock wave Mach numbers less than 2.1, evaporation is not a significant 
factor in the droplet dynamics.
Data availability
Data will be made available on request.
References
Beale, J.C., Reitz, R.D., 1999. Modeling spray atomization with the Kelvin-
Helmholtz/Rayleigh-Taylor hybrid model. At. Sprays 9 (6).
Bellman, R., Pennington, R.H., 1954. Effects of surface tension and viscosity on Taylor 
instability. Quart. Appl. Math. 12 (2), 151–162.
Berglund, R.N., Liu, B.Y., 1973. Generation of monodisperse aerosol standards. Environ. 
Sci. Technol. 7 (2), 147–153.
Chou, W.-H., Faeth, G., 1998. Temporal properties of secondary drop breakup in the 
bag breakup regime. Int. J. Multiph. Flow 24 (6), 889–912.
Clift, R., Gauvin, W., 1971. Motion of entrained particles in gas streams. Can. J. Chem. 
Eng. 49 (4), 439–448.
Duke-Walker, V., Allen, R., Maxon, W.C., McFarland, J.A., 2020. A method for 
measuring droplet evaporation in a shock-driven multiphase instability. Int. J. 
Multiph. Flow 133, 103464.
Duke-Walker, V., Maxon, W.C., Almuhna, S.R., McFarland, J.A., 2021. Evaporation and 
breakup effects in the shock-driven multiphase instability. J. Fluid Mech. 908.
Duke-Walker, V., McFarland, J.A., 2024. Vorticity suppression by multiphase effects in 
shock-driven variable density mixing. Int. J. Multiph. Flow 104889.
Duke-Walker, V., Musick, B.J., McFarland, J.A., 2023. Experiments on the breakup and 
evaporation of small droplets at high Weber numbe. Int. J. Multiph. Flow 104389.
Guildenbecher, D., López-Rivera, C., Sojka, P., 2009. Secondary atomization. Exp. Fluids 
46 (3), 371–402.
Hsiang, L.-P., Faeth, G., 1992. Near-limit drop deformation and secondary breakup. Int. 
J. Multiph. Flow 18 (5), 635–652.
Hsiang, L.-P., Faeth, G.M., 1995. Drop deformation and breakup due to shock wave 
and steady disturbances. Int. J. Multiph. Flow 21 (4), 545–560.
Karimi, M., Girimaji, S.S., 2016. Suppression mechanism of Kelvin-Helmholtz instability 
in compressible fluid flows. Phys. Rev. E 93 (4), 041102.
Kékesi, T., Amberg, G., Wittberg, L.P., 2014. Drop deformation and breakup. Int. J. 
Multiph. Flow 66, 1–10.
Loth, E., Tyler Daspit, J., Jeong, M., Nagata, T., Nonomura, T., 2021. Supersonic and 
hypersonic drag coefficients for a sphere. AIAA J. 59 (8), 3261–3274.
Meng, J., Colonius, T., 2015. Numerical simulations of the early stages of high-speed 
droplet breakup. Shock Waves 25 (4), 399–414.
MicroFAB, 2024. Low temperature devices. https://www.microfab.com/products/
dispensing-devices/low-temp-devices.
Mizuno, K., Yada, T., Kamiya, T., Asahara, M., Miyasaka, T., 2022. Deformation 
behavior of liquid droplet in shock-induced atomization. Int. J. Multiph. Flow 155, 
104141.
Morgan, R., Likhachev, O., Jacobs, J., 2016. Rarefaction-driven Rayleigh–Taylor insta-
bility. Part 1. diffuse-interface linear stability measurements and theory. J. Fluid 
Mech. 791, 34–60.
O’Rourke, P.J., Amsden, A.A., 1987. The TAB Method for Numerical Calculation of 
Spray Droplet Breakup. Tech. Rep., Los Alamos National Lab.(LANL), Los Alamos, 
NM (United States).
Osnes, A.N., Vartdal, M., 2022. Mach and Reynolds number dependency of the unsteady 
shock-induced drag force on a sphere. Phys. Fluids 34 (4).
Parmar, M., Haselbacher, A., Balachandar, S., 2009. Modeling of the unsteady force for 
shock–particle interaction. Shock Waves 19 (4), 317–329.
Pilch, M., Erdman, C.A., 1987. Use of breakup time data and velocity history data to 
predict the maximum size of stable fragments for acceleration-induced breakup of 
a liquid drop. Int. J. Multiph. Flow 13 (6), 741–757.
Poplavski, S.V., Minakov, A.V., Shebeleva, A.A., Boyko, V.M., 2020. On the interaction 
of water droplet with a shock wave: Experiment and numerical simulation. Int. J. 
Multiph. Flow 127, 103273.
Ranger, A., Nicholls, J., 1969. Aerodynamic shattering of liquid drops. AIAA J. 7 (2), 
285–290.
Reitz, R.D., Bracco, F., 1979. On the Dependence of Spray Angle and Other Spray 
Parameters on Nozzle Design and Operating Conditions. Tech. Rep., SAE technical 
paper.
Roos, F.W., Willmarth, W.W., 1971. Some experimental results on sphere and disk drag. 
AIAA J. 9 (2), 285–291.
Sharma, S., Singh, A.P., Rao, S.S., Kumar, A., Basu, S., 2021. Shock induced aerobreakup 
of a droplet. J. Fluid Mech. 929, A27.
Skews, B., Bredin, M., Efune, M., 2007. Drag measurement in unsteady compressible 
flow part 2: Shock wave loading of spheres and cones. R D J. 23, 13–19.
Specialised Imaging, 2024. SIMX full technical specification. https://www.specialised-
imaging.com/application/files/2217/1423/3903/SI_SIMX_01_Q03_A4_.pdf.
Stefanitsis, D., Strotos, G., Nikolopoulos, N., Kakaras, E., Gavaises, M., 2019. Improved 
droplet breakup models for spray applications. Int. J. Heat Fluid Flow 76, 274–286.
Sun, M., Saito, T., Takayama, K., Tanno, H., 2005. Unsteady drag on a sphere by shock 
wave loading. Shock Waves 14 (1), 3–9.
Tarey, P., Ramaprabhu, P., McFarland, J.A., 2024. Evolution of a shock-impacted 
reactive liquid fuel droplet with evaporation effects: A numerical study. Int. J. 
Multiph. Flow 174, 104744.
Wang, Z., Hopfes, T., Giglmaier, M., Adams, N.A., 2020. Effect of mach number on 
droplet aerobreakup in shear stripping regime. Exp. Fluids 61 (9), 193.
Zhang, Y., Dong, R., Shi, H., Liu, J., 2023. Experimental investigations on the 
deformation and breakup of hundred-micron droplet driven by shock wave. Appl. 
Sci. 13 (9), 5555.
International Journal of Multiphase Flow 193 (2025) 105372 
21
