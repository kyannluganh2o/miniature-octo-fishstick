<!-- PDF_PAGE: 1 -->

Heliyon 9 (2023) e13645
Available online 10 February 2023
2405-8440/© 2023 Published by Elsevier Ltd. This is an open access article under the CC BY-NC-ND license
(http://creativecommons.org/licenses/by-nc-nd/4.0/).
Research article 
Experimental investigation on high-pressure methane jet 
characteristic single-hole injector 
Yan Lei a,**, Xiaofeng Wang a, Dingwu Zhou b,*, Tao Qiu a, Wenbo Jin a, Chao Qin a, 
Dan Zhou c 
a Department of Automotive Engineering, Beijing University of Technology, 100124 Beijing, China 
b Department of Automotive Application, Hunan Automotive Engineering Vocational College, 412001 Zhuzhou, China 
c Art Design Institute, Hunan Women’s University, Changsha 41000, China   
ARTICLE INFO  
Keywords: 
Gas jet 
Methane 
Jet impact force 
Jet impulse 
High pressure 
ABSTRACT  
High-pressure gas direct injection (DI) technology benefits engines with high efficiency and clean 
emissions, and the gas jet process causes crucial effects especially inside an mm-size space. This 
study presents an investigation on the high-pressure methane jet characteristics from a single-hole 
injector by analysing jet performance parameters including jet impact force, gas jet impulse, and 
jet mass flow rate. The results show that the methane jet exhibited a two-zone behaviour along 
the jet direction in the spatial dimension induced by high-speed jet flow from the nozzle: zone 1 
near the nozzle—the jet impact force and jet impulse increased consistently except for a fluctu
-
ation due to shock wave effects induced by the sonic jet and no entrainment occurs, and zone II 
farther away from the nozzle—the jet impact force and jet impulse became stable when the shock 
wave effects became weak and the jet impulse was conserved with a linear conservation 
boundary. The Mach disk height was exactly the turning point of two zones. Moreover, the 
methane jet parameters, such as the methane jet mass flow rate, jet initial jet impact force, jet 
impulse, and Reynolds number had a monotonous and linearly increasing correlation with in
-
jection pressure.   
1. Introduction 
Natural gas (NG) is widely used in power plants, vehicles, and marine engines because of its favourable physical and chemical 
properties, such as low carbon numbers and harmful emissions [1,2]. The NG direction injection (DI) technique enables high thermal 
efficiency and clean exhaust emissions in modern engines [3]. Moreover, researchers have focussed on the highly efficient direct 
injection compression ignition engines because of their low emissions [4]. In a NG direct injection engine, the NG jets directly into the 
cylinder within a limited time of approximately 2–3 ms per cycle. Thus, the gas fuel needs to be mixed with air inside the combustion 
chamber rapidly before combustion. Moreover, the high-pressure gas fuel jets as the piston moving up to the top dead centre (TDC), 
and the gas jet may impact on the piston head since there are very small distance between the nozzle outlet and the piston head, 
generally within serval millimetres. Therefore, the high-pressure NG jet inside this mm-size limited cylinder space is critical for the 
mixing of air and gas fuel within limited time and space. Controlling the NG injection is necessary to obtain a combustible air-fuel 
* Corresponding author. 
** Corresponding author. 
E-mail addresses: leiyan@bjut.edu.cn (Y. Lei), 1336058289@qq.com (D. Zhou).  
Contents lists available at ScienceDirect 
Heliyon 
journal homepage: www.cell.com/heliyon 
https://doi.org/10.1016/j.heliyon.2023.e13645 
Received 21 March 2022; Received in revised form 1 February 2023; Accepted 6 February 2023

<!-- PDF_PAGE: 2 -->

Heliyon 9 (2023) e13645
2
mixture for efficient combustion. Li et al. [5] studied the direct injection NG engine emission and observed that the optimisation of the 
NG injection timing substantially reduced soot and CO emissions without compromising on thermal efficiency and increasing NOx 
emissions. Melaika et al. [6] tested a DI-CNG injection system on a baseline single-cylinder gasoline engine and established that the NG 
direction injection increased turbulence in the cylinder, producing a stable combustion process and lower HC, CO, CO 2, NOx, and 
particulate emissions that those from a baseline gasoline engine. Moreover, in NG direct injection engines, NG injection occurs at the 
end of compression stroke when the cylinder pressure becomes high enough for ignition. This extremely high backpressure during 
direct injection results in the demand for a high injection pressure, causing a high-pressure and high-speed gas fuel jet [7]. Huang et al. 
[8] studied the NG direction combustion process based on a rapid compression machine and observed that the direct injection 
high-speed fuel jet results in faster flame propagation. These above literatures reveal that the high-pressure gas fuel jet causes great 
effects on the engine combustion and emissions. Thus, we need to analyse the influence of high gas injection pressures (greater than 10 
MPa) on the gas fuel injection and mixing process in engines in real-life situations. 
Numerous researchers have studied gas fuel injection from nozzles. Shuja et al. [9] studied a gas jet from a conical nozzle and 
established that the injector nozzle had a significant influence on the gas jet impingement. Mirzabe et al. [10] analyzed the impact of 
the air jet impingent parameter on the removal of sunflower seeds and observed that the area of the removed regions increased 
corresponding to an increase in the nozzle diameter and pressure. Sankesh et al. [11] observed the growth of a transient NG jet flow 
from an outward-opening conical nozzle using a high-speed Schlieren optical system and proposed a new method for calculating the 
combined penetration of radially spreading gas jets. Ishibashi et al. [12] optically tested a NG jet and dual-fuel combustion progress in 
a rapid compression and expansion machine and observed that NG injection parameters, such as the injection time delay and injection 
angle, have a significant impact on jet entrainment. Researchers in the past have focussed on the progress of high-pressure gas fuel jets 
and demonstrated the impact high-pressure gas injection may have on the macro and micro characteristics of the engine. However, few 
researchers have studied the upstream source of the gas jet flow, which is the gas injector. Moreover, these literatures investigates the 
free NG jet ignoring the limited effects of the wall during the injection process. 
In practical application, the DI technique for NG (methane) requires high injection pressures to achieve suitable mass flow rates for 
fast in-cylinder fuel delivery and rapid fuel-air mixing because of the relatively low density of methane. Moreover, the methane jet flow 
is a dynamic process due to the jet flow inside the injector nozzle. The gas fuel jets into the cylinder just before the piston moves to TDC 
in a NG DI engine when the clearance of the cylinder is small, and the gas jet is very close (a few millimetres) to the moving piston head. 
Thus, the high-pressure gas jet has a chance to impact on the piston head, which may induce great influence on the gas jet penetration 
and mixing process with the environmental air. In addition, the characteristics of a gas jet from a circular nozzle are highly dependent 
on the ratio of the upstream (nozzle) total pressure to the environmental back pressure. This ratio is called the nozzle pressure ratio 
(NPR). Jets can be categorised into subsonic, moderately under-expanded, and highly under-expanded based on NPR. NG (methane) 
jets with an NPR ≥4 are highly under-expanded [13]. For NG DI engines, high-pressure gas fuel from the mm-sized holes of a typical 
injector nozzle is highly under-expanded, which may result in complex near-nozzle shock structures [14]. We [15] analyzed the 
macroscopic structure of an under-expanded methane jet using the Schlieren imaging technique and observed the occurrence of Mach 
disks. Moreover, the methane jet flow was a dynamic process due to the jet flow inside the injector nozzle. The high-pressure NG direct 
injection process is an under-expanded jet that induces shock waves. Dong et al. [16] studied the high-pressure methane gas jet in
-
jection process with the application of Schlieren imaging, and observed that a shock wave structure had its own evolution law under 
different NPRs and orifice diameters. The complex under-expanded methane jet and its energy transfer progress remain unexplained. 
The gas jet characteristics, such as, injector structure and location are very critical for the gas jet flow. Thus, it is essential to thoroughly 
understand the complex high-pressure NG jet flow characteristics and its impact function on the piston head on the air-fuel mixing 
process and final combustion. 
The gas injector is the energy source of the gas injection. Thus, the gas flow and gas energy parameters, such as the jet momentum 
or impulse, have a significant impact on the jet process. Numerous researchers have studied the gas jet from an injector. Some re -
searchers adopted test devices to directly measure the jet mass flow rate. Ridout et al. [17] built a test rig with a porous-walled cy -
lindrical chamber around the nozzle to directly measure the axial mass flow rate in a turbulent jet. However, this chamber could 
change the jet boundary and measurement results. Azad et al. [18] used a hot-wire anemometer and pitot tube to measure the axial 
velocity and entrainment rate of the air jet under different nozzle sizes. The nozzle is mm-sized and the gas flow is complex for the 
high-pressure methane jet of the DI engine. Thus, the gas jet mass flow rate along the jet direction is small and unevenly distributed in 
the cross section. Therefore, this direct measurement using a measurement device could not accurately measure the mass flow rate of 
the jet in different sections. Deng et al. [19] conducted an optical test on the injection and mixing characteristics of a high-pressure 
hydrogen and oxygen jet in an argon atmosphere in a constant volume device to study the gas jet mass flow and entrainment char -
acteristics. However, this method assumes that the gas jet density is constant when the pressure gradient is small. Therefore, the 
method is not suitable for analysing high-pressure methane gas jets with a large pressure difference. Moreover, some researchers have 
used trace gases or particles mixed with a gas jet to measure the gas jet characteristics. Wang et al. [20] used CO
2 as a tracer gas in an 
air jet. Prashanth et al. [21] used titanium dioxide as tracer particles to detect the velocity of a methane jet using Schlieren images and 
PIV in a constant volume bomb. Bruneaux et al. [22] utilised the laser-induced fluorescence and PIV technologies by adopting glycerol 
as the tracer particle to test the methane jet into nitrogen in a constant volume bomb to calculate the entrainment mass based on the 
concentration and velocity data. However, the added trace gas or particles change the properties of the jet gas and the test results for 
the gas impact test. Moreover, this method is complex, and the test devices are complicated and expensive. These above literatures 
focus on the high-pressure gas free jet, however the high-pressure gas jet front impact on a wall, which is not free jet due to the confined 
space, was seldom reported. 
In this work, we aimed to investigate the high-pressure NG jet flow impingent characteristics especially in the mm-size limited 
Y. Lei et al.

<!-- PDF_PAGE: 3 -->

Heliyon 9 (2023) e13645
3
space between the injector nozzle and a plate, and here adopted methane as the test gas since the main component of natural gas is 
methane CH4. We investigated the high-pressure methane jet impact force near the single-hole injector nozzle by testing the gas jet 
directly on a plate. We designed a test rig with a spring set to test the gas jet impact force as well as the jet impulse derived by the jet 
impact force, which was to simulate the situation of gas jet on the piston head. In addition, we detected the jet initial parameters such 
as the gas jet mass flow rate and gas jet velocity at the nozzle outlet, and conducted model simulation to analyse the flow fields near the 
nozzle outlet. The jet flow characteristics of the high-pressure methane injection near injector field were discussed based on the results. 
2. Experimental setup 
The injection performance of a gas injector is critical for direct gas injection. We designed a test rig to detect high-pressure injector 
features, such as the jet impact force, jet mass rate, and gas jet impulse. 
2.1. Single-hole gas injector 
As shown in Fig. 1, we used a single-hole injector in our research. The baseline injector was a six-hole injector, which was a gasoline 
injector and it could maintain a maximum injection pressure up to 30 MPa. Moreover, we designed a cover and matched it to adjust the 
injector nozzle to one hole. This injector cover was connected to the injector so that the gas injector became a single hole with 0.5 mm 
diameter. We used a single-hole injector shown in Fig. 1 for the two tests described in sections 2.2 and 2.3. 
2.2. Test of methane jet impact force 
Fig. 2 illustrates the methane gas jet impact force test system. We detected the gas jet impact force named F
jet using a spring set. To 
measure the gas jet impact force Fjet, a spring set with a thin plate was adopted. This plate was made of plastic with a very small mass, 
and thus the plate weight might be ignored in this work. One side of the spring was fixed in a spring seat which was always fastened, 
and the other one was mounted with a thin plate. The distance between the plate and the injector outlet is defined as the initial distance 
x
0, which can be adjusted by a micro-meter platform. The spring seat was mounted on a micro-meter platform with a set of sliding rail, 
and the high precise micro-meter mechanism adjusted the spring seat location along the sliding rail with high accuracy. Together with 
the spring seat, the initial plate position was also adjusted to change the initial distance. 
During the experiment, the high-pressure methane gas injected vertically from the injector nozzle impacted directly onto the plate, 
the plate moved and compressed the spring. We adjusted the gas injector using a solenoid valve. Moreover, certain amount of time was 
required to open and close the nozzle owing to its structure and operation principle. 
For a gas jet, it usually maintain an outer contour of cone, as shown in the enlarged window in Fig. 2. At the different vertical 
position along the jet direction, the gas jet cone has an outer edge which is a circle with a radius of r
jet. For the plate initial location, the 
distance from the injector outlet to the plate is defined as the initial distance x0. As for different initial distance x0, the gas jet cone has a 
circle of different radius rjet. 
To guarantee all the methane gas may impact on the plate, the diameter of the plate should be larger than the maximum outer circle 
diameter of the gas jet cone. At the different vertical position x along the jet direction, the maximum radius of the jet cone outer circle 
rjet may be derived by Equation (1) [23]. 
rjet =3.4 × (ax +0.294r nozzle ) (1) 
Here, rjet is the maximum radius of the jet cone outer circle; rnozzle is the radius of the injector nozzle; a is a coefficient of turbulence, 
which is an empirical value. For this work, we assume the maximum test position x is 60 mm, and a is 0.08. Then, the maximum radius 
of the jet cone outer circle is derived based on equation (1), i.e. rjet = 19 mm Thus, in this work, the plate was designed with a radius of 
50 mm which is far larger than the maximum rjet = 19 mm. This plate has larger diameter (here 100 mm) than the gas jet cover area, 
and it may receive all the gas jet. 
As all the gas jet impacted on the plate, the spring was compressed and its displacement was recorded by a displacement sensor. 
Fig. 1. Single-hole gas injector.  
Y. Lei et al.

<!-- PDF_PAGE: 4 -->

Heliyon 9 (2023) e13645
4
Based on the spring compression displacement, the impact force Fjet on the spring can be derived. The jet impact force Fjet is equal to the 
spring force Fspring, i.e. Fjet = Fspring. The spring force Fspring is the product of the spring compression displacement x times the elastic 
coefficient k, as shown in Equation (2). 
F jet = F spring = kx (2)  
Here, the elastic coefficient k of the spring is usually a constant. Thus, we observed that the jet impact force Fjet was directly pro-
portional to the jet plate displacement x, that is, Fjet = f(x). 
During the short impingent process Δt, the impact impulse received by the spring plate Isp can be sourced by the jet energy of the 
methane gas jet that is the gas jet momentum Ijet. The impact impulse of the spring plate Isp represents the variation of the gas jet 
momentum Ijet and it is proportion to Ijet. Therefore, in this work we tested the gas impact force to further analyse the high-pressure 
methane gas jet energy i.e. the gas jet impulse. 
The impact impulse of the spring plate Isp is determined by testing the jet impact force Fjet and its action time, as shown in Equation 
3 
Isp = F jet Δt (3)  
Where Isp is the impact impulse, Fjet is the jet impact force, and Δt is the injector injection pulse, that is the time of methane gas jet 
process. 
We conducted experiments with varying initial plate position x0 for our research. For each test, the injector was controlled to 
operate on the same short injection duration (Δt). Thus, the impact impulse of the spring plate Isp was determined by testing the jet 
impact force Fjet. 
Fig. 2. Jet impact force test of gas injector.  
Fig. 3. Gas injector test rig.  
Y. Lei et al.

<!-- PDF_PAGE: 5 -->

Heliyon 9 (2023) e13645
5
2.3. Test of methane gas jet at the nozzle outlet 
The methane gas jet impact energy was derived from the gas flowing out of the injector nozzle. Therefore, analysing the jet flow at 
the nozzle outlet was necessary. We measured the gas injection mass of the single-hole gas injector using the weight method by testing 
the water displacement by the methane gas jet. Because the methane doesn’t dissolve in the water, the water is displaced due to the 
methane jet into the water. The displaced water mass is relative with the methane jet mass. 
Fig. 3 illustrates a schematic diagram of the gas injection mass test. The high-pressure gas injector was mounted on the top of a 
water tank with a total volume of 18.9 L. This volume was much greater than the jet gas volume. We used a small pipe extending from 
the lower part of the water tank to adjust the water level at the outlet of the pipe without any drop out resulting in a balance between 
the water and the environment to maintain the gas pressure of the water tank at atmospheric pressure. The high pressure of the gas jet 
decreases sharply to the pressure of the tank, that is, atmospheric pressure when the gas jets into the tank. The tank was filled with 
water before the injection test. The upper part of the tank was filled with gas sealed between the tank head and water after the gas 
injection because methane is insoluble in water. The methane gas pushed water out through the pipe when the high-pressure methane 
gas was injected into the sealed space, and the discharged water from the pipe is collected by the metering cylinder. 
We deduced the methane gas jet mass based on the discharged water mass for this test. Moreover, the methane gas injection volume 
Vch4 was equal to the discharge water volume Vwater according to this test method as shown in Equation (4). 
V ch4 = V water = m water
ρ water
(4)  
where mwater is the water mass and ρ water is the water density. 
The density of methane ρ ch4 varied corresponding to the changes in the methane gas pressure pch4. The relationship between the air 
density and air pressure was defined by the gas state equation (Equation (5)): 
ρ ch4 = p ch4
zR g T ch4
= p in
zR g T 0
(5)  
where Tch4 is the methane temperature (here equal to the environmental temperature T0), Rg is the gas constant of methane, and z is the 
real gas compression coefficient. According to real gas thermodynamics, z is a function of pressure and temperature. However, the gas 
jets into the surrounding environment and quickly mixes with air in the weight test method. The total weighting test process required 
longer time (a few seconds) than the injection duration (a few milliseconds). Rg and z are considered constant for constant atmospheric 
pressure and temperature. 
The methane injection mass mch4 is defined by Equation (6). 
m ch4 = ρ ch4 V ch4 (6)  
Consequently, the methane injection mass flow rate ˙mch4 is given as shown in Equation (7): 
˙m ch4 = m ch4
t = ρ ch4 V ch4
t (7) 
Table 1 
Test apparatus.  
Type Specification 
Displacement sensor μ -ε optoNCDT 1700-50 Range 
Sensitivity 
Operating temperature 
0–50 mm 
0.001 mm 
0–50 
◦C 
Pressure gauge R01.4311 Range 
Accuracy 
Operating temperature 
0–10 MPa 
1% full scale 
 40–60 
◦C 
Electronic scale RMPUT Range 
Accuracy 
Operating voltage 
0.0005–7.5 kg 
0.0001 kg 
220 V 
Gas pressure booster pump OLF-2530 Rated outlet pressure 
Rated rotation 
Volume flow 
Boost ratio 
Gas inlet pressure 
Driving gas pressure 
0.7 MPa 
1400 r/min 
165 L/min 
60:1 
0.01–1 MPa 
≤0.8 MPa 
Micro meter platform LX40 Range 
Accuracy 
Maximum load 
±6.5 mm 
1.1 mm 
29.4 N 
Air pump W0.9/8 Rated outlet pressure 
Rated rotation 
Volume flow 
0.8 MPa 
930 r/min 
0.9 m
3/min  
Y. Lei et al.

<!-- PDF_PAGE: 6 -->

Heliyon 9 (2023) e13645
6
where t is the jet pulse time. 
Thus, the methane injection mass flow rate ˙mch4 is calculated as follows: 
˙m ch4 = ρ ch4
m water
tρ water
= p in
zRT 0
m water
tρwater
(8) 
Furthermore, we deduced the methane jet velocity uch4 at the injector outlet based on the test results in Equation (9). 
uch4 = ˙m ch4
ρch4 A nozzle
= 4 ˙m ch4
ρch4 π D 2
nozzle
(9) 
From Equation (9), we calculated the average jet velocity at the outlet of the injector nozzle. Here, Anozzle and Dnozzle are the area 
and diameter of the injector nozzle, respectively. 
The average methane gas jet mass flow rate and the average methane jet velocity could be deduced based on the discharged water 
mass mwater from Equations (8) and (9). We weighed the water collected in the cylinder on an electronic scale. Moreover, we performed 
the experiments of gas injection and the weight five times for each test condition. Furthermore, we calculated the average discharged 
water mass based on the water mass measured for the five experiments. 
All the specifications of the gas jet test devices are listed in Table 1, and the operating conditions are listed in Table 2. 
For the high-pressure methane gas jet through a small nozzle, the nozzle pressure ratio NPR between the injection pressure pinjection 
and the pressure at the nozzle outlet pb (i.e. pressure ratio = pinjection/pb) is important. Equation (10) gives the critical pressure ratio for 
the choked gas flow. 
1
NPR ∗ = pb
p injection
=
( 2
γ +1
) γ
γ 1
(10)  
Here, NPR* is the critical pressure ratio, and γ is the specific heat ratio. As for methane gas, γ is set to 1.32, and then we gain 1/NPR* =
0.542, and NPR* = 1.845. Thus, for methane, the critical pressure ratio is about 1.845. 
As for the injection conditions in this work, the injection pressure was high (respectively 5 MPa, 8 MPa, 10 MPa, 15 MPa, and 20 
MPa) and the back pressure was set to the atmosphere pressure (0.1 MPa). Therefore, the nozzle pressure ratio NPR was respectively 
50, 80, 100, 150 and 200, and it was much greater than the critical pressure ratio, i.e. NPR >> R*. As a result, the choked flow may 
occur for the high-pressure methane jet flow, and the choked gas flow velocity at the nozzle outlet maintains stable. 
2.4. Experimental data post process 
The spring plate began to move along the gas jet direction due to the gas jet impact force during the jet impact force test. However, 
the spring plate vibrated several times before it attains a stable position as shown in Fig. 4. This vibration was induced by the spring 
force. Fig. 4 illustrates the details of the test displacement data. The first farthest position was the effective displacement because of the 
vibration of the spring plate, and the maximum displacement position due to the first impact was considered as the test distance. The 
gas injection and displacement sensor tests were repeated five times for each test condition. We calculated the spring plate 
displacement as the arithmetic mean of the optimum test data. Moreover, we used the standard deviation method for the uncertainty 
analysis of high-pressure methane jet characteristics. 
3. Results and discussions 
We analyzed the high-pressure methane gas jet characteristics at the nozzle outlet and after-nozzle field based on the experimental 
results. 
The high-pressure gas injection process was dynamic, and the gas jet flow required certain time to become stable because the valve 
was completely open. Fig. 5 demonstrates the test data of the spring plate displacement under various injection pulse conditions. The 
injection pulse had a significant impact on the test data. Different injection pulses resulted in different spring displacements. Initially, 
the spring displacement increased corresponding to an increase in injection pulse. However, the rate of the increase in spring 
displacement decreased and eventually became zero when the injection pulse crossed a specific value. The displacement curves 
coincided with each other when then injection pulse reached 14 ms. Therefore, we used 14 ms as the injector injection pulse in our 
Table 2 
Test conditions.  
Test type Operation parameters Unit Value 
Test description Test gas: methane Operation temperature: 298 K 
Gas jet mass flow rate test Injection pressure [MPa] 5, 8, 10, 15, 20 
Back pressure [MPa] 0.1 
Gas jet impact force test Injection pressure [MPa] 5, 8, 10, 15, 20 
Back pressure [MPa] 0.1 
Initial plate position x0 [mm] 0.2, 0.5, 0.8, 1, 1.5, 2, 3, 4, 5, 8, 10, 12, 15, 20  
Y. Lei et al.

<!-- PDF_PAGE: 7 -->

Heliyon 9 (2023) e13645
7
research and collected all the following test data for an injection pulse of 14 ms. 
Fig. 6 demonstrates the tested spring plate displacement for the plate’s initial position under different injection pressure and a 
constant back pressure of 0.1 MPa, and the error bars indicate the standard deviation. Fig. 6 (a) illustrates the spring displacement 
curves under different injection pressures at constant back pressure (pb = 0.1 MPa), and Fig. 6 (b) illustrates the standard deviation of 
the spring displacement. The standard deviation was small (no more than 0.01) for the total test conditions of varied spring plate initial 
position x0. The tested results had a small standard deviation (marked by a short red line). 
The results show that all the curves of the spring displacement experienced two zones. In zone I, the spring displacement increased 
corresponding to an increase in the initial plate position. However, spring displacement exhibited certain fluctuations in zone I close to 
the injector nozzle. In zone II, the spring distance attained its maximum value and became stable. Zone I was the rising zone, and all the 
spring displacement curves exhibited an overall upward trend. Zone II was stable zone, and all curves exhibited a flat trend. 
Furthermore, all curves exhibited an increase in fluctuations in close-to-nozzle zone I. 
For each curve, there was a turning point as the dependent variable of y axis increases with the increase in the independent variable 
of x axis. Here, the turning point was defined based on the changing rate of the dependent variable of y axis. The absolute changing rate 
of y was set to be |(yi+1-yi)/yi|. Once it became no more than 2% (i.e. |(yi+1-yi)/yi|<0.02), then xi was the turning point. The turning 
points of the two zones marked by red points were different for different injection pressures. The turning point of each curve changed 
with an increase in the injection pressure. The turning point went farther away from the nozzle corresponding to an increase in in -
jection pressure. 
The high-pressure methane jet originated from the gas flow inside the injector. Moreover, analysing the gas flow at the injector 
nozzle was necessary because it was the start of the gas jet. Figs. 7 and 8 demonstrate the test results of the methane gas jet at the nozzle 
outlet. 
Fig. 7 demonstrates the results of the discharged water mass at various injection pressures for 0.1 MPa back pressure. We measured 
the discharged water mass from the experiments and deduced the methane mass using Equation (5). Thus, we observed that the 
discharged water mass increased linearly corresponding to an increase in injection pressure. Based on the theoretical analysis in 
Section 2.2, the methane jet parameters at the nozzle outlet were deduced based on the tested discharged water mass. 
Fig. 8 demonstrates the test results for the methane jet characteristics of the injector. The methane jet mass flow rate and methane 
jet velocity were derived as shown in Fig. 8 (a). We observed that the methane mass flow rate increased linearly corresponding to an 
increase in the injection pressure. However, the methane jet velocity at the nozzle outlet remained almost unchanged, which reveals 
Fig. 4. Displacement data.  
Fig. 5. Effect of methane injection pulse.  
Y. Lei et al.

<!-- PDF_PAGE: 8 -->

Heliyon 9 (2023) e13645
8
that the high-pressure methane gas jet is the choked flow at the nozzle outlet. For this choked methane jet flow, the velocity at the 
nozzle outlet becomes saturated, even the injection pressure rises. The experimental results reveals the saturation phenomenon of the 
methane jet velocity at the nozzle outlet when the injection pressure increased. Thus, the methane gas jets at a constant speed (the 
dashed line is the average gas jet velocity). Therefore, the jet velocity at the nozzle outlet remained stable for high-pressure gas 
Fig. 6. Spring displacement along jet direction.  
Fig. 7. The injector jet mass test result.  
Y. Lei et al.

<!-- PDF_PAGE: 9 -->

Heliyon 9 (2023) e13645
9
Fig. 8. Gas jet characteristics at injector nozzle outlet.  
Fig. 9. Methane jet impact force along jet direction after the nozzle.  
Y. Lei et al.

<!-- PDF_PAGE: 10 -->

Heliyon 9 (2023) e13645
10
injection (where the injection pressure is higher than 5 MPa at pb = 0.1 MPa with a nozzle pressure ratio NPR = 50). Fig. 8(b) 
demonstrates the methane jet momentum and Mach number of the methane jet at the nozzle outlet. The Mach number Ma is a 
dimensionless quantity representing the ratio of the flow velocity to the local sonic speed. We observed that the Mach number Ma at the 
injector outlet remained stable irrespective of the changes in injection pressure. Here, Ma is approximately equal 1. This proves that the 
high-pressure methane jet is a sonic speed injection (for methane gas, the local sonic speed is approximately equal to 450 m/s). 
Moreover, the jet momentum of methane gas is given by the methane gas jet mass multiplied by the jet velocity at the nozzle outlet. For 
the gas injector, the methane jet momentum at the nozzle outlet is equal to the initial jet momentum. This is the initial energy source of 
the jet out of the nozzle. The methane jet momentum increased linearly corresponding to an increase in the methane injection pressure 
pinjection. Therefore, high pinjection resulted in high gas initial jet energy of the methane jet flow. 
These results reveal that the high-pressure methane gas jet is an under-expanded jet with sonic velocity at the nozzle outlet. Our 
previous research of methane jet (Lei et al., 2019, literature [15]) revealed that the high-pressure methane jet flow from the nozzle is 
an under-expanded jet and Mach disks may appear in the close-to-nozzle zone. The shock wave induced by the high-pressure methane 
jet results in high local gas flow speed but low gas pressure. This pressure drop causes the spring plate to move backward to the plate 
and thus its displacement decreases. However, this shock wave influence becomes weak as the plate move far from the nozzle. Finally, 
the plate moves forward by the continuous jet. 
The methane jet impact force Fjet along the jet axial direction after the nozzle were obtained based on the analysis in Section 2.2 as 
shown in Fig. 9. The Fjet curve exhibited a two-zone feature similar to the two-zone feature of spring distance. In zone I (close to the jet 
nozzle), the methane gas jet impact force increased corresponding to an increase in the initial plate distance x0. In zone II, the jet 
impact force remained unchanged even when the initial plate distance varied. We observed that the turning point (marked by red 
points) of the jet impact force changed corresponding to the increase in injection pressure. Moreover, all the curves fluctuated in zone I. 
This fluctuation in the methane jet impact force was induced by the high velocity gas flow from the nozzle. Fig. 10 demonstrates the 
Reynolds number, Re, at the nozzle outlet. Reynolds number has a linear relationship with the velocity at the nozzle outlet (shown in 
Fig. 8), and Re is can be derived based on the velocity result which is obtained by the test method in section 2.3. The Reynolds number 
increased corresponding to the increase in injection pressure. The Reynolds number was high (Re > 8000) for all different injection 
pressures. This established that the high-pressure methane jet had a high-Re turbulent flow that induced shock waves. 
The strong turbulent flow from the nozzle induced shock waves in the near-nozzle region. Fig. 10 illustrates the high-pressure gas 
jet from the nozzle. The methane gas penetrated forward and sucked background air into the jet during the jet process. High-pressure 
injection induced shock waves to form a barrel shock and a Mach disk. The Mach disk location was predicted using Equation (11) [24]. 
H =1.34R nozzle
̅̅̅̅̅ ̅pin
p b
√
= 0.67
̅̅̅̅̅ ̅pin
p b
√
D nozzle (11)  
where, H is the Mach disk height; Rnozzle and Dnozzle are the nozzle radiator and diameter, respectively, pin is the absolute pressure at the 
nozzle inlet, and pb is the back pressure, that is, the outlet pressure of the nozzle. 
We used Equation (11) to predict the Mach disk height of a high-pressure gas jet. Fig. 10 illustrates the Mach disk height H deduced 
based on Equation (11). The deduced Mach disk height, H, and its fitted curve (red line) and fitting equation are presented in the figure. 
The fitting equation reveals that H curve has an exponential relationship with the injection pressure, i.e., H∝p in0.5054. This indicates 
Fig. 10. Reynolds number Re at nozzle outlet and Mach disk height.  
Y. Lei et al.

<!-- PDF_PAGE: 11 -->

Heliyon 9 (2023) e13645
11
that H is directly proportional to the square root of the injection pressure, as indicated in Equation (11). 
Furthermore, Fig. 10 also demonstrates the relationship between the Mach disk height (marked by green solid points) and the 
turning point (marked by red solid points). The Mach disk heights do not exactly coincide with the turning points. This deviation 
occurred because the absolute pressure at the nozzle inlet was not equal to the methane injection pressure. However, the real inlet 
pressure of the nozzle could not be easily determined. Hence, we measured the injection pressure from the gas tank. The Mach disk 
heights in Fig. 10 were calculated using the approximate injection pressure. Furthermore, Equation (11) was derived from the ex -
periments of the CO2 jet into the background gas of an approximately 1:1 mixture of CO 2 and air. This is an important factor to be 
considered when comparing the experimental results of our research with the results of the methane jet injection into air. Moreover, we 
did not measure the methane jet impact force directly. It was derived based on the spring plate displacement values from the test. 
Hence, the calculated values (green points) deviated from and experimental values (red points). 
The two-zone behaviour of the high-pressure methane jet was due to the shock wave. In zone I, the shock wave caused the local 
pressure and impact force to decrease close to the nozzle. In zone II, the impact of the shock wave weakened farther downstream from 
the Mach disk resulting in stable impact force. Moreover, the first Mach disk location, that is, the Mach disk height, was the turning 
point of the two zones. In addition, the turning points of the two zones increased linearly corresponding to an increase in injection 
pressure. 
The methane jet impulse on the spring plate at different initial spring plate positions was derived from the methane jet impact force 
based on the relation Isp = FjetΔt. Fig. 11 illustrates the methane jet impulse based on the test results for various injection pressures. 
Thus, the jet impulse curves had a two-zone feature, and the turning points were the same as the impact force for different injection 
pressures. In zone I, the jet impulse curve exhibited a general upward trend. However, we could observe fluctuation near the nozzle. 
The jet impulse curve became stable farther away from the nozzle in zone II indicating the conservation of methane jet impulse in zone 
II. These stable methane jet impulse in zone II presents the average methane jet impulse. The jet impulse curve moved upwards linearly 
when the injection pressure increased. 
Fig. 12 illustrates the methane jet impulse at different x
0 positions with respect to the injection pressure. These methane jet impulse 
Fig. 11. Methane jet impulse along axial direction after the nozzle.  
Y. Lei et al.

<!-- PDF_PAGE: 12 -->

Heliyon 9 (2023) e13645
12
points located in the grey region. In this grey region, the distribution of the methane jet impulse were messy and scattered. However, 
the jet impulse points at same injection pressures coincided with each other near the upper boundary of the grey region. The boundary 
of the grey region represents the exact jet impulse conservation line. This establishes that the methane jet impulse conservation 
boundary is linear. 
4. Conclusions 
We analyzed the important jet parameters, such as the jet impact force, jet mass flow rate, and jet impulse of a high-pressure 
methane jet from a single-hole injector. The high-pressure methane jet characteristics were due to the gas flow inside the nozzle. 
Moreover, the characteristics of the methane jet were significantly different in the near-nozzle region and the region farther away from 
the nozzle. In the near-nozzle region, the gas jet velocity was much higher than sonic speed and no entrainment occurred because of 
high jet energy. The gas fuel could not suck the surrounding air into the gas fuel jet in the near-nozzle field resulting in a poor air-fuel 
mixture that hindered for efficient ignition in real-life gas fuel DI engines. Thus, the structure and location of the gas fuel injector are 
critical for engine design to avoid ignition in the near-nozzle region. 
The methane gas jet exhibited a two-zone behaviour along the jet direction in the spatial dimension. In zone I (near field close to the 
nozzle outlet), the jet characteristic parameters curve (jet impact force and jet impulse) exhibited a fluctuation, and zone I was a 
dynamic zone. In zone II (main jet region, far from the nozzle outlet), the parameters curve became flat, and zone II was a stable zone. 
Moreover, the Mach disk height was the turning point of the two zones. Furthermore, the turning points of the two zones increased 
linearly corresponding to an increase in injection pressure. 
This two-zone feature of the high-pressure methane jet flow was induced due to the high-speed jet flow from the nozzle. The high- 
pressure methane jet flow reached its sonic speed at the nozzle outlet causing shock waves. In zone I, the shock waves caused high local 
gas flow speed but resulting in a decrease in impact force as well as jet impulse close to the nozzle. In zone II, far from the nozzle 
downstream of the Mach disk, the impact of shock waves weakened resulting in constant the impact force, and the jet impulse was 
conserved with a linear conservation boundary. 
The methane injection pressure had a significant impact on the gas jet. The methane jet parameters, such as the methane jet mass 
flow rate, jet initial jet impact force, jet impulse, and Reynolds number all increased corresponding to an increase in injection pressure. 
Moreover, the jet parameters had a monotonous and linearly increasing correlation with injection pressure. These results prove that 
the shock wave effect becomes much stronger so that the no-entrainment field tends to be enlarged. It is more important for the high- 
pressure DI NG engine to design the injector to avoid the direction impact on the piston head or wall. 
Author contribution statement 
Yan Lei: Conceived and designed the experiments; Performed the experiments; Wrote the paper. 
Xiaofeng Wang, Chao Qin: Performed the experiments. 
Dingwu Zhou, Dan Zhou: Contributed reagents, materials, analysis tools or data. 
Tao Qiu: Conceived and designed the experiments. 
Wenbo Jin: Analyzed and interpreted the data. 
Funding statement 
Professor Yan Lei was supported by State Key Laboratory of Engine Reliability Foundations [skler-201913]. 
Fig. 12. Jet impulse along axial direction.  
Y. Lei et al.

<!-- PDF_PAGE: 13 -->

Heliyon 9 (2023) e13645
13
Data availability statement 
Data will be made available on request. 
Declaration of interest’s statement 
The authors declare no conflict of interest. 
Nomenclature 
Anozzle area of the nozzle 
Fjet Jet impact force 
I0 initial jet momentum 
k spring elastic coefficient 
mch4 methane mass 
n measurement number 
pin absolute pressure at the nozzle inlet 
pinjection jet pressure 
SD standard deviation 
t jet time 
T0 environmental temperature 
u jet velocity 
Vwater discharge water volume 
x0 spring plate initial position 
z real gas compression coefficient 
ρ ch4 density of the methane 
Dnozzle nozzle diameter 
H Mach disk height 
Isp gas jet impulse 
˙m gas mass flow rate 
mwater water mass 
NPR nozzle pressure ratio 
pb back pressure 
R conventional gas constant 
Δt time of the methane jet stage 
Tch4 methane temperature 
uch4 methane jet velocity at nozzle outlet 
Vch4 methane gas injection volume 
Xi measurement result 
x spring plate displacement 
γ specific heat ratio 
ρ water water density 
References 
[1] Z. Chen, J. He, H. Chen, L. Geng, P. Zhang, Experimental study on cycle-to-cycle variations in natural gas/methanol bi-fueled engine under excess air/fuel ratio 
at 1.6, Energy 224 (2021), 120233. 
[2] J. Hall, B. Hibberd, S. Streng, M. Bassett, Compressed-natural-gas optimized downsized demonstrator engine, Proc IMechE Part D: J Automobile Eng. 232 (1) 
(2018) 75–89. 
[3] M.H. Li, H.M. Wu, T.C. Zhang, B.X. Shen, Q. Zhang, Z.G. Li, A comprehensive review of pilot ignited high pressure direct injection natural gas engines: factors 
affecting combustion, emissions and performance, Renew. Sustain. Energy Rev. 119 (2020), 109653. 
[4] I.M. Gogolev, J.S. Wallace, Performance and emissions of a compression-ignition direct-injected natural gas engine with shielded glow plug ignition assist, 
Energy Convers. Manag. 164 (2018) 70–82. 
[5] M.H. Li, X.L. Zheng, Q. Zhang, Z.G. Li, B.X. Shen, X.R. Liu, The effects of partially premixed combustion mode on the performance and emissions of a direct 
injection natural gas engine, Fuel 250 (2019) 218–234. 
[6] M. Melaika, G. Herbillon, P. Dahlander, Spark ignition engine performance, standard emissions and particulates using GDI, PFI-CNG and DI-CNG systems, Fuel 
293 (2021), 120454. 
[7] Y. Lei, Y. Li, T. Qiu, Y. Li, Y. Wang, C. Zhang, J. Liu, M. Ding, X. Liu, G. Peng, Effects of high-pressure methane jet on premixed ignited flame in constant-volume 
bomb, Energy 220 (2021), 119695. 
[8] Z. Huang, S. Shiga, T. Ueda, H. Nakamura, T. Ishima, T. Obokata, M. Tsue, M. Kono, Study of cycle-by-cycle variations of natural gas direct injection combustion 
using a rapid compression machine, Proc. Inst. Mech. Eng. - Part D J. Automob. Eng. 217 (1) (2003) 53–61. 
[9] S.Z. Shuja, B.S. Yilbas, Flow impingement onto a conical cavity at elevated wall temperature: effects of conical nozzle cone angle and flow velocities on heat 
transfer rates, J. Enhanc. Heat Transf. 17 (1) (2010) 23–43. 
Y. Lei et al.

<!-- PDF_PAGE: 14 -->

Heliyon 9 (2023) e13645
14
[10] A.H. Mirzabe, G.R. Chegini, Effect of air-jet impingement parameters on the removing of sunflower seeds from the heads in static conditions, Agri. Eng. Int.: 
CIGR J. 18 (2) (2016) 43–59. 
[11] D. Sankesh, P. Petersen, P. Lappas, Flow characteristics of natural-gas from an outward-opening nozzle for direct injection engines, Fuel 218 (2018) 188–202. 
[12] R. Ishibashi, D. Tsuru, An optical investigation of combustion process of a direct high-pressure injection of natural gas, J. Mar. Sci. Technol. 22 (2017) 447–458. 
[13] A. Hamzehloo, P.G. Aleiferis, Gas dynamics and flow characteristics of highly turbulent under-expanded hydrogen and methane jets under various nozzle 
pressure ratios and ambient pressures, Int. J. Hydrogen Energy 41 (2016) 6544–6566. 
[14] D. Edgington-Mitchell, R.D. Honnery, J. Soria, The underexpanded jet Mach disk and its associated shear layer, Phys. Fluids 26 (2014), 096101. 
[15] Y. Lei, J.X. Liu, T. Qiu, Y.Q. Li, Y.P. Wang, B. Wan, X.W. Liu, Gas jet flow characteristic of high-pressure methane pulsed injection of single-hole cylindrical 
nozzle, Fuel 257 (2019), 116081. 
[16] Q. Dong, Y. Li, E.Z. Song, C. Yao, L.Y. Fan, J. Sun, The characteristic analysis of high-pressure gas jets for natural gas engine based on shock wave structure, 
Energy Convers. Manag. 149 (2017) 26–38. 
[17] F.P. Ricout, D.B. Spalding, Measurements of entrainment by axisymmetrical jets, J. Fluid Mech. 11 (1) (1961) 21–32. 
[18] M. Azad, W.R. Quinn, D. Groulx, Mean streamwise centreline velocity decay and entrainment in triangular and circular jets, in: 41st AIAA Fluid Dynamics 
Conference and Exhibit 27 - 30 June 2011, Honolulu, Hawaii, 2023. AIAA 2011-3087. 
[19] J. Deng, H.P. Zhong, Y.C. Gong, Studies on injection and mixing characteristics of high pressure hydrogen and oxygen jet in argon atmosphere, Fuel 226 (2018) 
454–461. 
[20] X. Wang, L.F. Ye, Y.Q. Liu, J.S. Ma, Experiment on entrainment movement of non-isothermal cold jet of circular nozzle based on tracer gas concentration, 
J. Water Res. Water Eng. (2014) 1672, 643X:05-0093-05. 
[21] P. Karra, T. Rogers, P. Lappas, Air entrainment in gaseous fuel jets using particle image velocimetry and high speed schlieren photography in a constant volume 
chamber, in: SAE Technique Paper, 2023. SAE 2015-01-0938. 
[22] G. Bruneaux, M. Causse, A. Omrane, Air Entrainment in diesel-like gas jet by simultaneous flow velocity and fuel concentration measurements, comparison of 
free and wall Impinging jet Configurations, SAE International Journal of Engines 5 (2) (2012) 76–93. 
[23] Tiqian Luo, Fluid Dynamics, second ed., China Machine Press, Beijing, 2003. 
[24] B. Mate, I.A. Graur, T. Elizarova, I. Chirokov, G. Tejeda, J.M. Fernandez, S. Montero, Experimental and numerical investigation on an axisymmetric supersonic 
jet, J. Fluid Mech. 426 (2001) 177–197. 
Y. Lei et al.
