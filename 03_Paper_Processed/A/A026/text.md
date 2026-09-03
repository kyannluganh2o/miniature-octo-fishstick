<!-- PDF_PAGE: 1 -->

The influence of hydrogen injection timing and energy proportion on flame 
developments in a dual direct injection optical diesel engine
Alastar Gordon Heaton
 , Qing Nian Chan , Sanghoon Kook
*
School of Mechanical and Manufacturing Engineering, The University of New South Wales, Room 402E Ainsworth Building J17, Gate 14, Barker Street, Kensington, 
Sydney, NSW 2033, Australia
ARTICLE INFO
Keywords:
Hydrogen
Direct injection
Diesel engine
Dual fuel
Flame
ABSTRACT
This study shows how flame development of hydrogen-diesel dual direct injection combustion is influenced by 
changes in two key parameters: hydrogen injection timing and hydrogen/diesel energy ratio. High-speed imaging 
of the natural combustion luminosity was taken from a heavy-duty optically accessible engine. The engine was 
modified to include a single hole, side mounted injector for 35 MPa hydrogen direct injection into the com -
bustion chamber. The eight-hole diesel injector remained in the original centrally mounted position, serving as a 
pilot flame ignition source. The results showed that reduced hydrogen energy share causes an increase in size and 
intensity of the diesel pilot acting to accelerate the initial combustion reaction, which is not only due to the 
increased diesel quantity but also the shift in diesel flame distribution. However, the combustion transitions into 
a near identical mixing-controlled combustion phase regardless of energy share. For hydrogen injection timing 
variations at fixed 90 % energy share, advanced injection was found to directly impact the hydrogen combustion 
mode altering the proportion of fuel injected prior to ignition of the diesel flame and the extent of mixing that has 
occurred. The longer residence time also increases the overlap of the two fuels prior to ignition resulting in a 
lengthened ignition delay due to dilution of the diesel pilot. The combustion phasing control is however pre -
served as the reaction was faster with a more premixed hydrogen charge at ignition.
1. Introduction
The dual-fuel internal combustion engine has recently gained 
attention as an avenue to introduce hydrogen (H
2
) as a carbon-free fuel. 
Whilst electrification is an available option for decarbonisation, it is 
currently not well suited to heavy-duty applications where the ICE re -
mains the most practical option [ 1 ]. The dual-fuel combustion approach 
leverages a difference in fuel properties using a high reactivity fuel, such 
as diesel, as a pilot to ignite a lower reactivity fuel. Compared to other 
ignition sources, such as spark ignition, pilot-based ignition is able to 
deliver a higher H
2 
energy and more voluminous [ 2 ]. While early 
implementations of the dual-fuel combustion concept use carbon-based 
options such as natural gas (methane) and methanol, H
2 
is a promising 
carbon-free fuel that can be used to convert existing diesel ICEs 
compliant with governmental emissions targets [ 3 ].
Early studies of H
2
-diesel combustion concepts focused on the use of 
port-fuel injection (PFI) to deliver the H
2 
[ 4 ]. Whilst this approach is a 
cost-effective means to modify an existing ICE, it imposes load and en -
ergy fraction limitations to the engine. This stems from the need to 
maintain a lean mixture to supress the formation of thermal NO
x
, and 
also to mitigate the risk of hot-spot ignition of the H
2 
during the 
compression stroke [ 5 , 6 ]. Additionally, the injection of a gaseous fuel 
reduces the engines volumetric efficiency and introduces the risk of 
backfire with excessive H
2 
concentration [ 7 , 8 ]. However, such issues 
may be overcome with the implementation of direct injection (DI), 
allowing for fuel delivery after the intake valve closure and control over 
the mixture preparation by varying the injection parameters. To this 
end, high pressure H
2 
injection with over 20 MPa is used [ 9 , 10 ]. 
Furthermore, optimisation of the H
2
– air mixture preparation using the 
high-pressure H
2 
direct injection is an avenue for minimising the for -
mation of NO
x 
[ 11 ].
This study focuses on the hydrogen-diesel dual direct injection 
Abbreviations: CA, crank angle degrees; aEOI, after end of injection; aHRR, apparent heat release rate; aSOI, after start of injection; aTDC, after top dead centre; 
bEOI, before end of injection; bTDC, before top dead centre; CA10, crank angle after 10% heat release; DF, dual fuel; DI, direct injection; EOI, end of injection; GDI, 
gasoline direct injection; H
2
, hydrogen; H2DDI, hydrogen-diesel dual direct injection; ICE, internal combustion engine; NO
x
, nitrogen oxides; TDC, top dead centre.
* Correspondence author.
E-mail address: s.kook@unsw.edu.au (S. Kook). 
Contents lists available at ScienceDirect
Applications in Energy and Combustion Science
journal homepag e: www.sci encedirect.co m/journal/ applications-i n-energy -and-combus tion-scien ce
https://doi.org/10.1016/j.jaecs.2025.100382
Received 23 July 2025; Received in revised form 1 September 2025; Accepted 4 September 2025  
Applications in Energy and Combustion Science 24 (2025) 100382 
Available online 5 September 2025 
2666-352X/© 2025 The Authors. Published by Elsevier Ltd. This is an open access article under the CC BY-NC license ( http://creativecommons.org/licenses/by- 
nc/4.0/ ).

<!-- PDF_PAGE: 2 -->

(H2DDI) combustion scheme which uses two discrete injectors, a cen -
trally mounted, multi-hole diesel injector and a side mounted, single- 
hole H
2 
injector [ 12 ]. Previous work [ 13 , 14 ] has examined the impact 
of varied H
2 
injection timing in a metal engine, demonstrating the 
impact on engine efficiency and NO
x 
formation. While a significant 
reduction in CO
2 
emissions was achieved thanks to the use of 
carbon-free H
2 
as a main fuel, a clear relationship was established, 
indicating that later injection timing achieved NO
x 
control, similar with 
other dual-direct injection combustion schemes [ 15 , 16 ]. However, from 
these works, the in-cylinder processes remain unclear regarding the pilot 
diesel flame development, early stages of H
2 
combustion and the com -
bustion mode involving H
2 
diffusion flames. Some works completed in a 
constant volume combustion chamber (CVCC) have examined the igni -
tion and flame characteristics of pilot ignited H
2 
[ 17 , 18 ]. These works 
highlighted the impact that the H
2 
has on the ignition of the pilot fuel 
and the transition through to the later stage of combustion. However, as 
they were completed in a CVCC with only a free jet condition, they do 
not replicate the mixing processes occurring within an engine cylinder. 
Consequently, the present study seeks to examine the H2DDI combus -
tion scheme in a running optical engine. Some similar work has been 
completed however has either utilised natural gas [ 19 , 20 ] or a multi-jet 
dual-fuel injector where injection of each fuel is combined into a single 
centrally mounted injector [ 15 , 21 ].
This study is an extension of a prior work [ 22 ], which reported the 
details of pilot diesel flame development associated with the change in 
pilot injection amount and timing as well as one selected case of diesel 
pilot ignited H
2 
flame development. The present study addresses two key 
control parameters of H
2 
injection, namely, the energy share and direct 
injection timing. A fixed H
2 
injection timing of 10 ∘ CA bTDC was used as 
the H
2 
energy share was varied between 70 and 95 % of a total 1200 J, 
with the remaining energy supplied by diesel. Conversely, a fixed H
2 
energy share of 90 % was selected to examine the influence of varied H
2 
injection timing. Throughout the study the diesel injection timing 
remained at 6 ∘ CA bTDC. The natural combustion luminosity was 
captured with a high-speed imaging arrangement in conjunction with 
crank-angle resolved in-cylinder pressure measurements.
2. Experimental methodology
2.1. Dual-direct injection optical engine
This study used a single-cylinder optical engine based on a produc -
tion cylinder head which has been modified for optical access and 
discrete direct injection of diesel and H
2
. A schematic diagram of the 
engine and imaging arrangement has been included in Fig. 1 . The engine 
has a displacement of 1133 cm
3 
with a bore and stroke of 107 mm and 
126 mm, respectively, and a compression ratio of 17.4. The swirl ratio of 
the production cylinder head is 2 according to the manufacturer speci -
fication. For optical access the engine was modified to include an 
extended piston with a 78 mm cylindrical bowl piston and drop-down 
cylinder liner. Images were captured through the piston bottom quartz 
window with a 45 ∘ mirror located in the centre of the extended piston. 
The field of view available through the bottom window is also shown in 
Fig. 1 . Further details of the engine used in this study have been included 
in Table 1 . The cylinder head was modified to integrate a pressure 
transducer and a side mounted, modified gasoline direct injector (GDI, 
Bosch HDEV6) orientated at a 45 ∘ angle relative to the cylinder head and 
targeted at the piston bowl [ 12 ] as indicated in Fig. 1 . The injector was 
fitted with a single hole cap, converting the 6 × 120 μ m hole nozzles of 
the original injector to a single axially drilled 1 mm hole in order to 
maintain the momentum of the H
2 
jet as it was guided towards the piston 
bowl. The steady-state flow rate of the modified injector was measured 
to be 1.73 g/s at 35 MPa using the Zeuch method [ 10 , 22 ].
H
2 
was supplied to the injector from a pneumatic gas booster pump 
(Protech PBT), with the injection pressure controlled by a high-pressure 
regulator (Pressure Tech LF792). For injector needle lubrication a single 
drop of engine oil was periodically added to the inlet of the injector. The 
addition of oil was not found to impact the recorded frames which was 
confirmed with comparison of the pixel intensity profile after oil addi -
tion. The diesel injector (Denso G4S) remained in the conventional 
centrally located position of the production cylinder head. The injector 
nozzle had 8 equally spaced 120 μ m diameter holes and a nominal hy -
draulic flow rate of 225 mm
3
/stroke at 100 MPa. The injected mass was 
Fig. 1. Schematic diagram of dual-fuel optical engine with imaging setup for natural flame luminosity and cylinder head fuel injection arrangement.
A.G. Heaton et al.                                                                                                                                                                                                                              Applications in Energy and Combustion Science 24 (2025) 100382 
2

<!-- PDF_PAGE: 3 -->

measured in a Bosch-tube type injection rate measurement rig. Con -
ventional ultra-low sulphur diesel with a minimum cetane number of 51 
was supplied by a conventional common-rail pump system (Bosch CP4 
pump). A summary of the injection system used is included in Table 1 .
The engine operating conditions and fuel injection settings used for 
this study are summarised in Table 2 . The engine was connected to an 
AC motor, used to maintain a constant engine speed of 1200 rpm. A 
water heater (ThermalCare Aquatherm RA series) was used to circulate 
363 K coolant (water) through the cylinder liner and engine head to 
provide a stable thermal condition emulating that of a warmed-up en -
gine. The engine operated at a naturally aspirated condition with an 
approximate intake temperature of 303 K. The injection pressure of each 
fuel remained constant for all conditions, with 35 MPa and 75 MPa used 
for H
2 
and diesel, respectively. The H
2 
injection pressure was set for the 
maximum allowable pressure of the injector to deliver gaseous H
2 
within 
a short period. On the other hand, the diesel injection pressure was set 
for the minimum allowable common-rail pressure to keep the diesel 
pilot flames at the centre of the combustion chamber [ 22 ]. The diesel 
common-rail pressure, fuel injection timing and injection duration was 
controlled with a universal engine controller (Zenobalti ZB-9013P) with 
a rotary encoder (Autonics E40S8 series) providing a crank angle 
reference with a 0.2 ∘ CA/sample resolution. A 15-skip firing mode was 
utilised with one firing cycle followed by fourteen motoring cycles with 
a total of 10 firing cycles per engine run. This was to ensure all the 
combustion products from the previous firing cycle were expelled and to 
minimise the thermal stress on the quartz windows.
Throughout this study, the energy input per cycle remained constant 
at 1200 J per cycle with varied proportions of H
2 
and diesel. For the first 
portion of this study, a fixed diesel and H
2 
injection timing of 6 ∘ CA 
bTDC and 10 ∘ CA bTDC were used while the H
2 
energy share was varied 
between 70 % and 95 % of the total fuel energy. For the second part of 
this study the H
2
/diesel energy share was instead fixed at 90 % / 10 % 
whilst the H
2 
injection timing was varied between 0 (TDC) and 30 ∘ CA 
bTDC with again a diesel pilot injection at 6 ∘ CA bTDC. It should also be 
noted that all injection timings and durations referenced in this study 
refer to the electronic signal timing and duration rather than the 
hydraulic.
2.2. Dual-camera imaging diagnostics
In this study, two high-speed imaging arrangements were utilised, 
the first for the H
2 
energy share variation portion of the study and the 
second for the H
2 
injection timing portion to capture the natural com -
bustion luminosity through the piston-top window. The first arrange -
ment is as in the previous work [ 22 ] such that a high-speed 
complementary metal oxide semiconductor (CMOS) camera (Photron 
NOVA S20) was used with a framerate of 60 kHz (0.12 ∘ CA/frame 
equivalent). The exposure and aperture were maintained at ~16.6 μ S 
and f/5.6 throughout the study. Additionally, a 450 nm short pass filter 
(Edmund Optics 15 – 256) was used to reduce the intensity of the diesel 
pilot whilst preserving as much luminosity from the H
2 
signal to mini -
mise the bias created by the high intensity diesel flame. However, 
particularly during the initial stages of the combustion, this bias makes 
segregation of the image into H
2 
and diesel stages impossible. To over -
come this, a two-camera imaging arrangement was implemented 
combining a beam splitter and filtering arrangement with the intention 
of producing a reference image source of the diesel pilot to improve the 
boundary detection. A 30R/70T beamsplitter (Edmund Optics 34 – 415) 
was added to split the light, with the reflected portion of the light 
directed to a second CMOS camera (Phantom v7.3) and the transmitted 
portion directed to the primary camera (Photron NOVA S20). The im -
aging settings for the primary camera remained the same as the original 
single camera setup with the exception of the short pass filter which was 
changed to a higher optical density 425 nm filter (Edmund Optics 
84 – 703). The secondary camera used a framerate of 36 kHz (0.20 ∘ CA 
\frame) at a reduced resolution for the selected region surrounding the 
diesel injector as shown in Fig. 1 . Additionally, the same specification 
200 mm lens (Micro-Nikkor) was used with an aperture of f/4 for each 
camera to minimise the difference in the pixel resolution. Additionally, a 
425 nm long pass filter (Edmund Optics 84 – 743) was used to minimise 
the combustion luminosity from the H
2 
flame. The wavelength of 425 
nm was selected as it allows the image intensity arising from 
carbon-based spectral emissions ( i.e. CH*, CH
2
O and C
2
* [ 23 ] to be 
reduced whilst minimally impacting the near UV emission of the H
2 
flame. The specifications of each imaging setup have been summarised 
in Table 3 .
Concurrent to the high-speed imaging diagnostics, the in-cylinder 
pressure was measured using a piezoelectric pressure transducer (Kis -
tler 6056A) installed to the cylinder head as shown in Fig. 1 . A sampling 
rate of 100 kHz was utilised resulting in a crank angle resolution of 
0.072 
◦
CA/sample at the operating engine speed of 1200 rpm. Apparent 
heat release rate (aHRR) was calculated using the measured in-cylinder 
pressure.
2.3. Image post-processing
The captured natural combustion luminosity images were post- 
processed to extract a frame-wide average pixel intensity profile and 
flame boundary of each fuel. It should be noted that the pixel intensity 
profiles shown in this study are solely from the primary camera. Despite 
this, due to the use of a beamsplitter in one imaging setup it is not 
possible to compare the intensity profiles presented from each setup. A 
similar boundary detection method was applied for both the single and 
Table 1 
Engine specifications and operating conditions.
Displacement volume 
[cc]
1133
Bore [mm] 107
Stroke [mm] 126
Compression ratio 
(geometric)
17.4
Engine speed [rpm] 1200
Intake air pressure 
[kPa]
101.3 (natural aspiration)
Intake air temperature 
[K]
303
Wall (coolant) 
temperature [K]
363
Dual direct injection 
system [ 12 ]
Hydrogen Diesel
Injector Modified Bosch spray-guided GDI 
injector
Denso G4S, diesel 
direct injector
Number of holes 6 x 160 μ m combined with 1 mm 
axially drilled hole injector cap
8 x 120 μ m
Steady state flow rate 1.73 g/s at 350 bar 225 mm3/stroke at 
100 MPa
Pump Protech PBT Gas Booster Bosch CP4, 
common rail
Table 2 
Fuel injection properties and conditions.
Fuel Hydrogen Diesel
Cetane number – ≥ 51
Fuel density at 15 ∘ C and 1 atm [kg/ 
m3]
0.089 848
Lower heating value [MJ/kg] 120 43.4
Fuel injection pressure [bar] 350 750
Total energy input per cycle [J/ 
cycle]
1200
Injection timing [ ∘ CA bTDC] 0, 10, 20, 30 6
Injection duration [ μ s] 4427, 4314, 4087, 
3539
231, 284, 368, 
438
Energy fraction [%] 95, 90, 80, 70 5, 10, 20, 30
Firing mode 15-skip firing
A.G. Heaton et al.                                                                                                                                                                                                                              Applications in Energy and Combustion Science 24 (2025) 100382 
3

<!-- PDF_PAGE: 4 -->

dual camera imaging setup with the goal being to segregate the frame 
into regions containing the H
2 
flame and regions containing the diesel 
pilot flame. For the single camera imaging arrangement, the mono -
chrome frame was segregated based upon the pixel intensity, with high 
pixel intensity regions representing the diesel flame and low pixel in -
tensity the H
2 
flame. Once segregated, a typical boundary detection 
procedure of contrast adjustment, spatial filtering and thresholding 
using Otsu ’ s method was applied [ 24 ]. The detected diesel boundary 
was then used as a mask to remove it from the detected H
2 
flame 
boundary. It should be noted that due to the high intensity of the diesel 
flame a bias is introduced in the detection of the H
2 
boundary as the 
diesel flame produces regions of intensity which overlap with the range 
typical of the H
2 
flame. However, in the dual camera arrangement, the 
secondary camera captured a frame composed of primarily of the diesel 
flame, allowing for it to serve as reference for the location of the diesel 
pilot. The lower intensity region surrounding the diesel pilot flame could 
also be identified from the secondary camera which was used to reduce 
the extent of the bias in detection of the diesel and H
2 
flame regions. The 
threshold value was manually selected to produce a mask that encom -
passed the bias region surrounding the diesel pilot flame, particularly 
during the initial stage of the H
2 
flame development. It should however 
be noted that the disadvantage of this arrangement is the overall 
reduction in light intensity due to the splitting of the light which makes 
detection of the H
2 
flame boundary difficult in scenarios with low flame 
intensity. The image from the secondary camera was scaled to match the 
spatial resolution of the primary camera. Further, since the secondary 
camera was operated at a reduced resolution compared to the primary 
camera, frames were padded so that the distribution of the flame 
matched. Since the secondary camera operated at a lower frame rate, the 
frame used for processing was selected based upon which was closest to 
the timing of the given primary camera frame. A sample of the procedure 
followed has been included in Fig. 2 .
3. Results and discussion
3.1. Effect of hydrogen energy share
Fig. 3 shows the in-cylinder pressure and aHRR traces as the H
2 
energy fraction is varied between 70 % and 95 %. The data is shown for 
both the ensemble average and one standard deviation calculated from 
30 combustion cycles, which confirms the differences observed exceed 
the cyclic variations for all tested conditions. As mentioned previously, a 
fixed diesel and H
2 
injection timing of 6 ∘ CA bTDC and 10 ∘ CA bTDC 
were used and their respective injection durations are annotated in the 
figure. The aHRR traces show a two-stage combustion with an initial 
premixed stage followed by a mixing controlled stage. However, the 
95H/5D case shows a three-stage heat release, with decoupled ignition 
of each fuel prior to the transition into the mixing-controlled phase as 
reported in previous study [ 22 ]. The previous work used a 90H/10D 
energy share with a 6 ∘ CA bTDC diesel pilot injection and a TDC H
2 
injection. This suggests the earlier H
2 
injection timing allowed the H
2 
jet 
to penetrate into the cylinder prior to ignition of the diesel pilot flame. 
The increase in diesel energy share monotonically increases the intensity 
of the premixed phase of the heat release owing to the ability for a larger 
proportion of the total fuel energy being present within the combustion 
chamber at the start of combustion.
Table 3 
High-speed imaging settings.
High-speed camera Primary Camera 
(Photron Fastcam NOVA 
S20)
Secondary Camera 
(VisionResearch Phantom 
v7.3)
Lens AF Micro-Nikkor 200 mm f/4D ED-IF
Aperture f/5.6 f/4
Exposure 1/frame (~16.6 μ s) 25 μ s
Frame rate [kHz] 60 36
Frame interval [ ∘ CA] 0.12 0.20
Imaging resolution 
[pixel]
512 x 512 256 x 256
Pixel resolution [ μ m/ 
pixel]
156 180
Short pass filter OD 2, 450 nm  
(Edmund Optics 15 – 256) 
OD 4, 425 nm  
(Edmund Optics 84 – 703)
–
Long pass filter – OD 4, 425 nm  
(Edmund Optics 84 – 743)
Beamsplitter 30R/70T VIS Beamsplitter (Edmund Optics 34 – 415)
Fig. 2. Sample of image processing procedure applied for detection of hydrogen/diesel flame boundary using images from two cameras.
A.G. Heaton et al.                                                                                                                                                                                                                              Applications in Energy and Combustion Science 24 (2025) 100382 
4

<!-- PDF_PAGE: 5 -->

Fig. 3. Ensemble averaged in-cylinder pressure and apparent heat release rate profile for varied H
2 
energy fraction, 95 % H
2 
/ 5 % diesel to 70 % H
2 
/ 30 % diesel 
with 10 ∘ CA bTDC H
2 
injection timing and diesel pilot injection at 6 ∘ CA bTDC. Injection timing and duration for H
2 
and diesel annotated by solid and dashed lines 
respectively. Shaded region represents one standard deviation from ensemble average. Crank angle timings of images shown in Fig. 4 annotated with circles on 
pressure and aHRR traces.
Fig. 4. Diesel pilot flame and initial H
2 
flame development for varied H
2 
energy share, 95 % H
2 
/ 5 % diesel to 70 % H
2 
/ 30 % diesel with 10 
◦
CA bTDC H
2 
injection 
timing and diesel pilot injection at 6 
◦
CA bTDC. The green and red boundary represents the H
2 
flame and diesel pilot flame respectively with swirl direction rep -
resented in the top left frame. Green arrow on top left frame indicates H
2 
injector location. Crank angle timings for each frame represent engine cycle position (top 
left), timing with respect to diesel injection (orange) and H
2 
injection (green). Crank angle timings of each frame were marked in Fig. 3 using circles on in-cylinder 
pressure and aHRR traces.
A.G. Heaton et al.                                                                                                                                                                                                                              Applications in Energy and Combustion Science 24 (2025) 100382 
5

<!-- PDF_PAGE: 6 -->

For all energy share cases, it is worth noting that the quantity of H
2 
injected prior to ignition remains similar due to the fixed H
2 
injection 
timing (10 ∘ CA bTDC) that was used. This is with the exception of the 
95H/5D case which exhibits a delayed peak heat release and conse -
quently a slight increase in the quantity of H
2 
present within the cylinder 
at the point of ignition. For each case the initial premixed combustion 
phase is characterised by flame propagation from the ignition site up -
stream toward the H
2 
injector and through the H
2 
mixture spread 
clockwise by the in-cylinder swirl flow. This is then followed by a 
transition into a mixing-controlled combustion as indicated by the 
consistent steady heat release rate for each energy fraction. Higher H
2 
energy shares demonstrated a slightly lengthened mixing-controlled 
burning period due to their longer injection duration. However, there 
is no variance in the heat release rate during this phase indicating that 
the diesel fuel does not participate in the later stage of the combustion 
having been consumed during the initial premixed combustion phase.
Fig. 4 shows selected high-speed images for the initial stages of the 
combustion for each H
2/
diesel energy share, namely the diesel pilot 
flame structure and the initial H
2 
flame propagation through the H
2
. Due 
to the variability in the ignition of the diesel and H
2 
not all cases are 
presented at the same crank angle timing. As such, the crank angle 
timing of each frame was annotated to the in-cylinder pressure and 
aHRR traces (see Fig. 3 ). In this work the ignition of the H
2 
flame is 
distinguished visually, with ignition of the diesel flame always preced -
ing H
2 
ignition and occurring in a similar location for each energy share. 
The images show that, as the diesel energy share is increased, the size 
and intensity of the diesel pilot flame steadily increases, with the diesel 
flame spreading farther from the diesel injector. For example, 70 % H
2 
energy (70H/30D) case shows diesel flames present at the centre as well 
as near the piston-bowl wall whereas 95 % H
2 
(95H/5D) case displays all 
the fragmented diesel flames positioned near the injector/centre of the 
combustion chamber. At lower H
2 
energy share, the initial H
2 
combus -
tion is accelerated with a larger diesel pilot able to ignite a larger volume 
of H
2 
during the initial reaction.
It is noted 95H/5D case has a relatively delayed ignition of the H
2 
jet 
(approx. 2 ∘ CA) which in turn delays the flame development. Whilst the 
diesel flame distribution is similar with the 90H/10D case, the reduced 
energy of the pilot flame lengthens the period of interaction required 
before ignition of the H
2 
jet occurs. This, combined with the reduced 
spreading of the diesel fuel, means that there is both a lengthened 
interaction time required in addition to a potential dwell between diesel 
ignition and H
2 
jet interaction. For the cases below 95 % H
2 
energy 
share, the diesel pilot flame is intense enough to cause near simulta -
neous ignition for the selected H
2 
injection timing. Additionally, these 
cases exhibit a monotonically increasing peak heat release rate. This is a 
result of not only the increased diesel energy but also a larger volume of 
the H
2 
jet igniting during the initial interaction between the two fuels. 
Furthermore, comparison of the frames corresponding to the peak heat 
release (4th frame for each case shown in Fig. 4 ) demonstrates the 
accelerated flame development, with a larger H
2 
flame region for higher 
diesel energy fractions. This is despite the similarity in the H
2 
mixture at 
this point in the engine cycle owing to the fixed H
2 
injection timing.
This change in the behaviour of the diesel pilot flame is reflected by 
the location of the apparent ignition sites shown in Fig. 5 which is a 
density plot of the ignition kernel as the H
2 
energy share is varied. The 
location of the apparent ignition sites is detected using a frame wide 
intensity threshold to detect the point of first luminance as outlined in 
previous work [ 22 ]. The apparent ignition site ’ s locations are then 
binned into a 32 × 32 grid for visualisation. As the diesel energy fraction 
is increased the apparent ignition sites is shifted further away from the 
centrally mounted diesel injector due to the increased momentum 
arising from the lengthened injection duration. The 90H/10D emerges 
as the case providing the most consistent ignition location across each of 
the energy shares. The short injection duration ensures that the diesel 
fuel spreads minimally from the injector leading to this consistency. 
However, further reduction to the diesel injection duration ( i.e. the 
95H/5D case) induces increased variability in the ignition location. This 
arises from the variability in the injector needle behaviour with the 
shortened injection duration. Additionally of note is the lack of apparent 
ignition kernel formation on the left-hand side of the cylinder, particu -
larly where the H
2 
jet is present highlighting the suppression effect 
arising from dilution of the diesel fuel.
For quantitative analysis of the flame signals, Fig. 6 shows the image- 
based ignition delay and CA10 (crank angle corresponding to 10 % heat 
release rate) for varied H
2 
energy fraction. The image-based ignition 
delay is determined using the same method outlined for the apparent 
ignition sites detection of Fig. 5 and defines the point of first luminance 
during the combustion. The data is based on 30 combustion cycles with 
the error margin representing one standard deviation from the mean of 
each plotted data point. As mentioned previously the 95H/5D case re -
quires a longer interaction time between the fuels for ignition of the H
2 
occur. This combined with the variability in the injector needle behav -
iour arising from the short injection duration leads to a delayed com -
bustion phasing in addition to ignition kernel formation. Increasing the 
diesel pilot quantity (energy share) acts to stabilise this with a length -
ened duration providing more repeatable injector needle behaviour in 
addition to a higher energy, and more robust ignition source. Addi -
tionally, there is also a slight increase in ignition delay of the diesel pilot. 
This is due to the lengthened mixing time required for the diesel fuel to 
reach a combustible mixture condition. However, as the overall com -
bustion reaction occurs faster this results in no impact to the start of 
combustion phasing control.
Fig. 7 shows the later stage of the H
2 
flame development as the H
2 
energy share is varied, with the crank angle timing for the selected 
frames annotated to the in-cylinder pressure and aHRR traces also 
included at the bottom of Fig. 7 . Once the initial H
2 
flame development 
is completed, propagating through the premixed charge the combustion 
transitions into a mixing controlled combustion mode. This is evident 
Fig. 5. Density plot of apparent ignition site centroid for varied H
2 
energy share, 95 % H
2 
/ 5 % diesel to 70 % H
2 
/ 30 % diesel with 10 
◦
CA bTDC H
2 
injection timing 
and diesel pilot injection at 6 
◦
CA bTDC.
A.G. Heaton et al.                                                                                                                                                                                                                              Applications in Energy and Combustion Science 24 (2025) 100382 
6

<!-- PDF_PAGE: 7 -->

with the reduction in intensity shown within the reaction zone in 
addition to a reduction in the reaction zone area correlating to the 
reduced heat release rate typical of a mixing controlled mode. For each 
energy fraction, the distribution and intensity of the flame region is 
similar, indicating that the varied diesel pilot size has minimal influence 
on the in-cylinder condition. However, it is noted that for higher H
2 
energy shares, the reaction zone spreads below the centreline of the H
2 
injector towards the bottom of the frame with a steady decrease in 
spreading as the H
2 
energy share is reduced. Considering the fixed in -
jection timing, this is likely a combined effect of a reduced initial re -
action rate permitting the H
2 
to spread further before being consumed 
whilst also better preserving the momentum of the H
2 
jet. Additionally, 
the increasing diesel pilot fuel injection may impact the penetration of 
the H
2 
jet, but as the non-reacting jet was not visualised in this work this 
remains unclear. During this phase of the combustion, the high intensity 
diesel region of the flame slowly dissipates as the H
2 
reaction zone is 
spread slowly across the cylinder carried by a combination of the jet 
momentum and swirl flow.
Given significant variations exhibited on selected flame images in 
both the size and intensity, the flame area and pixel intensity have been 
analysed for all recorded movies of 30 combustion cycles. The results are 
shown in Fig. 8 for the flame area of both the H
2 
and diesel regions (top) 
and the image frame-wide mean pixel intensity count (bottom). The data 
is shown for a standard deviation calculated for all individual cycles as 
shaded area and their ensemble average using a solid line for H
2 
and 
dashed line for diesel.
It should be noted that the rapid increase in H
2 
flame area is partially 
contributed to the previously mentioned bias caused by the high in -
tensity diesel flame. As the diesel energy share is decreased, the rate at 
which the maximum flame area, correlating to the peak pixel intensity, 
is delayed. It is reminded that the quantity of the H
2 
is identical during 
the initial phase of the combustion, as the H
2 
injection for all cases ex -
tends beyond the initial premixed reaction phase. Consequently, this 
difference is a direct result of the increased diesel pilot fuel quantity 
which delivers not only a more intense ignition source but also positions 
it closer to the side-mounted H
2 
injector. This accelerates the initial 
growth of the H
2 
flame, as indicated by the earlier peak area and pixel 
intensity.
The more intense initial reaction reduces the quantity of unburnt H
2 
within the cylinder which is able to spread through the cylinder into the 
piston bowl, before the combustion transitions into a mixing controlled 
burning mode. As previously discussed, the 95H/5D case is a clear 
outlier with the flame area remaining larger, for a longer duration. This 
stems from the delayed ignition of the H
2 
which produces an overall 
leaner H
2 
charge reducing the intensity of the initial premixed H
2 
burn. 
The slower initial reaction permits more of the H
2 
to be carried into the 
piston bowl during the later mixing-controlled phase of the combustion 
providing this larger reaction zone. For all cases, an increase in flame 
area is noted following the end of the H
2 
injection due to the increased 
mixing arising from end of injection effects [ 25 ]. Again, this is more 
pronounced for the 95H/5D due to the overall reduced reaction rate of 
the combustion.
3.2. Effect of hydrogen injection timing
Fig. 9 shows the ensemble-averaged in-cylinder pressure and aHRR 
traces as the as the H
2 
injection timing is varied between 0 and 30 ∘ CA 
bTDC with a fixed 90 % / 10 % H
2
/diesel energy share. Also included in 
Fig. 9 , is a diesel-only reference case where only 120 J of diesel was 
injected. This provides a reference against which the contribution from 
the H
2 
may be compared. As the H
2 
injection is advanced, there is an 
increase in TDC pressure as the mass present during the compression 
stroke steadily increases [ 13 ]. Each H
2 
injection timing presents a 
unique combustion mode, with earlier H
2 
injection timings producing a 
higher peak pressure despite the similarity in pressure rise rate. As 
previously reported [ 22 ], the 0 ∘ CA bTDC (TDC) H
2 
timing exhibits in 
typical three stages of combustion, diesel pilot ignition, H
2 
ignition/ -
flame propagation and mixing-controlled H
2 
combustion.
However, advancing the H
2 
injection timing to 10 ∘ CA bTDC results 
in interaction between the H
2 
and diesel prior to ignition as indicated by 
an initial aHRR above that of the diesel baseline. Following this, the 
combustion steadily declines to that typical of a mixing controlled phase 
as shown by the steady heat release rate during the later phase of the 
combustion matching the 0 ∘ CA bTDC case. Further advance of the H
2 
injection timing negates the mixing-controlled combustion phase as the 
H
2 
injection finishes prior to the establishment of a steady state heat 
release. Additionally, the further advance of the H
2 
injection begins to 
impact the diesel ignition and flame development as shown by the de -
parture from the diesel baseline. Crank angle timings of each frame are 
marked by circle on in-cylinder pressure and aHRR traces. For example, 
Fig. 6. Image-based ignition delay and CA10 for varied H
2 
energy share, 95 % H
2 
/ 5 % diesel to 70 % H
2 
/ 30 % diesel with 10 
◦
CA bTDC H
2 
injection timing and 
diesel pilot injection at 6 
◦
CA bTDC.
A.G. Heaton et al.                                                                                                                                                                                                                              Applications in Energy and Combustion Science 24 (2025) 100382 
7

<!-- PDF_PAGE: 8 -->

the 20 ∘ CA bTDC case shows a reduced intensity to the diesel pilot, 
below the baseline value potentially due to interaction with H
2 
prior to 
ignition, resulting in extended interaction time for ignition. Further -
more, the 30 ∘ CA bTDC injection timing delays the diesel fuel ignition 
such that both events occur simultaneously as shown by the single peak 
in the heat release trace. The ignition is delayed substantially compared 
to the other cases, likely because of the diesel pilot becoming diluted by 
the presence of H
2 
lengthening the ignition delay of the diesel. Among 
tested conditions, the maximum pressure and aHRR is measured for the 
most advanced H
2 
injection timing, indicating more premixed H
2 
charge.
All the interpretations made based on the pressure and aHRR profiles 
are re-evaluated using the high-speed flame images. Fig. 10 shows the 
natural flame luminosity corresponding to the initial stages of the 
combustion, namely the diesel pilot flame, ignition of the H
2 
and the 
initial H
2 
flame propagation. Due to the varied crank angle timing of the 
Fig. 7. Late-stage H
2 
flame development for varied H
2 
energy share, 95 % H
2 
/5 % diesel to 70 % H
2 
/ 30 % diesel with 10 
◦
CA bTDC H
2 
injection timing and diesel 
pilot injection at 6 
◦
CA bTDC. The green and red boundary represents the H
2 
flame and diesel pilot flame respectively with swirl direction represented on the top left 
frame. Green arrow on top left frame indicates H
2 
injector location. Crank angle timings for each frame represent engine cycle position (top left), timing with respect 
to diesel injection (orange) and H
2 
injection (green). Crank angle timings of each frame are marked by circle on the in-cylinder pressure and aHRR traces.
A.G. Heaton et al.                                                                                                                                                                                                                              Applications in Energy and Combustion Science 24 (2025) 100382 
8

<!-- PDF_PAGE: 9 -->

Fig. 8. H
2 
and diesel flame area (top) and mean pixel intensity (bottom) for varied H
2 
energy share, 95 % H
2 
/ 5 % diesel to 70 % H
2 
/ 30 % diesel with 10 
◦
CA bTDC 
H
2 
injection timing and diesel pilot injection at 6 
◦
CA bTDC. Shaded region represents one standard deviation from ensemble average.
Fig. 9. Ensemble averaged in-cylinder pressure and apparent heat release rate profile for 90 % H
2 
/ 10 % diesel energy share with varied H
2 
injection timing (0 – 30 
◦
CA bTDC) and diesel pilot injection at 6 
◦
CA bTDC. Comparison to diesel-only pilot injection at 6 
◦
CA bTDC. Injection timing and duration for H
2 
and diesel 
annotated by solid and dashed lines respectively. Shaded region represents one standard deviation from ensemble average.
A.G. Heaton et al.                                                                                                                                                                                                                              Applications in Energy and Combustion Science 24 (2025) 100382 
9

<!-- PDF_PAGE: 10 -->

combustion for each injection timing, frames were selected to represent 
the different phases of the flame development rather than a consistent 
crank angle position. Frames have been selected based upon the aHRR 
traces, with H
2 
ignition frames selected as the first frame at which the 
aHRR exceeds the diesel-only baseline and the 4th frame corresponding 
to the peak aHRR for each injection timing. The crank angle timing of 
the presented frames was annotated onto the corresponding in-cylinder 
pressure and aHRR traces in Fig. 9 .
For each H
2 
injection timing (as shown in Fig. 10 ), the diesel pilot 
flame structure remains similar with an injector centric multi-jet diesel 
flame established. The small variance in this structure was a likely result 
of the variability in the injector needle behaviour with any impact from 
the H
2 
jet unable to be determined with the inability to visualise the fuel 
distributions prior to ignition. However, for the most advanced 30 ∘ CA 
bTDC H
2 
injection case, much of the diesel flame is supressed during the 
initial stages of the combustion, as indicated by the overall delayed 
timing of the ignition. This, due to the overlap between the two fuels, 
dilutes the diesel fuel and delays ignition. However, once the diesel ig -
nites, the H
2 
is ignited almost simultaneously owing to the low minimum 
ignition energy [ 26 ]. The H
2 
flame then propagates quickly through the 
premixed charge towards the injector location, which was spread by a 
combination of the jet momentum and swirl flow.
As the H
2 
injection timing was retarded, the dilution effect was 
lessened, as the H
2 
had not been spread sufficiently to impact the diesel 
flame development. Additionally, with the reduced mixing time, the H
2 
mixture remains more heterogeneous promoting a more intense initial 
reaction. This is exemplified by the increased intensity within the H
2 
reaction zone for the 10 ∘ CA bTDC H
2 
injection timing case during the 
initial stage of the combustion. This injection timing allows for the H
2 
jet 
to penetrate such that the interaction occurred immediately after igni -
tion of the diesel fuel, creating a locally richer H
2 
mixture (compared to 
earlier injection timing cases) for the flame to propagate through. 
Although the later H
2 
injection timing of 0 ∘ CA bTDC does not exhibit 
the same behaviour, the pixel intensity was reduced within the reaction 
zone. This a result of the H
2 
ignition occurring closer to the start of in -
jection (approx. 4 ∘ CA), resulting in less H
2 
having been injected as well 
as the reduced mixing time. Comparatively, for the more advanced 
timing case of 20 ∘ CA bTDC, the H
2 
has mixed further and thereby 
reducing equivalence ratios across the H
2 
charge. As a result, the in -
tensity of the initial reaction is reduced. However, the increased mixing 
time permitted by the earlier injection timing quickly overcomes the 
reduced local equivalence ratio with the flame front able to propagate 
faster through the more premixed H
2
-air mixture [ 27 ].
For quantitative analysis of the flame images, Fig. 11 shows the 
image-based ignition delay and corresponding CA10 as the H
2 
injection 
timing is advanced from 0 to 30 ∘ CA bTDC. The data is based on 30 
combustion cycles with the error margin representing one standard 
deviation from the mean of each plotted data point. The results show 
that between TDC and 20 ∘ CA bTDC H
2 
injection timing, the ignition 
delay does not vary; however, as it is advanced to 30 ∘ CA bTDC, the 
ignition delay lengthened significantly due to dilution of the diesel pilot 
fuel. However, combustion phasing control is maintained with an 
accelerated initial heat release – i.e. more premixed H
2 
mixture com -
bined with increased diesel pilot flame overlap [ 17 ].
Fig. 10. Diesel pilot flame development and initial H
2 
flame propagation for 90 % H
2 
/ 10 % diesel energy share with varied H
2 
injection timing (0 – 30 
◦
CA bTDC) 
and diesel pilot injection at 6 
◦
CA bTDC. Comparison to diesel-only pilot injection at 6 
◦
CA bTDC. The green and red boundary represents the H
2 
flame and diesel 
pilot flame respectively with swirl direction represented on the top left frame. Green arrow on top left frame indicates H
2 
injector location. Crank angle timings for 
each frame represent engine cycle position (top left), timing with respect to diesel injection (orange) and H
2 
injection (green). Crank angle timings of each frame were 
marked in Fig. 9 using circles on in-cylinder pressure and aHRR traces.
A.G. Heaton et al.                                                                                                                                                                                                                              Applications in Energy and Combustion Science 24 (2025) 100382 
10

<!-- PDF_PAGE: 11 -->

For the combustion control evaluated with CA10, the most retarded 
TDC H
2 
injection caused the most delayed CA10. This is related to the 
approximate 10 ∘ CA required after the start of H
2 
injection for the jet to 
reach the centre of the cylinder and being ignited by the diesel pilot 
flames. As the H
2 
charge is more premixed due to earlier injection at 10 
∘ CA bTDC, the CA10 is moved forward. For H
2 
injection timings earlier 
than 10 ∘ CA bTDC, CA10 tends to be delayed again, however, it is within 
the magnitude of cyclic variability. This is consistent with the visual 
impression of flame images shown in Fig. 10 .
For the later stage of the combustion for each of the H
2 
injection 
timings, flame images are shown in Fig. 12 . It is noticeable that the 
distribution of the H
2 
reaction zone remains consistent regardless of the 
H
2 
injection timing, with the reaction zone residing primarily to the left- 
hand side of the cylinder. It is also seen that some further spreading of 
the flame occurs due to the swirl motion of the in-cylinder flow. It should 
be noted that the 0 ∘ CA bTDC case displays a substantially smaller re -
action zone. This was a consequence of the reduced luminosity available 
from the dual camera imaging arrangement (as shown in Fig. 1 ) used 
only for the injection timing variation portion of this study. This, 
coupled with the low flame luminosity of the primarily mixing- 
controlled combustion mode (compared to previous work [ 22 ]), resul -
ted in the reduced reaction zone size. Comparison of the other H
2 
in -
jection timings indicates that later timings allow for the reaction zone to 
spread further towards the right-hand side of the cylinder. Due to the 
fixed injection duration, this is likely a consequence of increased pro -
portion of the injection that occurred following the diesel injection. 
Whilst the H
2 
injection was ongoing, the H
2 
reaction zone for each case 
did not recede completely to the left-hand side of the piston bowl. Whilst 
the reaction was occurring in this region, the reduced luminosity arising 
from the highly diffusive burning mode made it undetectable, with later 
timings demonstrating the effect more strongly. For earlier H
2 
injection 
timings, the reactants were consumed more quickly as indicated by the 
increased aHRR in Fig. 9 , restricting the spreading of the reaction zone 
across the cylinder. On the other hand, later H
2 
injection made the 
mixture spread to the right-hand side of the cylinder, which was driven 
by the jet momentum. Whilst there may be H
2 
present across the piston 
bowl for these injection timings, the luminosity signal produced was 
insufficient to detect.
Fig. 13 shows the quantitative analysis of flame area and pixel in -
tensity based on 30 combustion cycles for each H
2 
injection timing. As 
the H
2 
injection timing is advanced, the initial H
2 
flame development 
rate is reduced as shown by the delayed peak in H
2 
flame area, which 
correlates to the completion of this initial flame development phase. 
Whilst the difference is minimal for each case, it is indicative of the 
varied mixture composition created, with a more heterogenous H
2 
dis -
tribution i.e. later injection timings reduce the spreading of the H
2 
jet 
prior to ignition providing a locally higher equivalence ratio compared 
to earlier injection timings. The similarity in flame propagation speed 
across the injection timing range is a result of more advanced injection 
timings having a larger premixed mixture portion prior to ignition, 
whilst later injection timings instead benefiting from a locally higher H
2 
concentration to promote faster flame propagation. Comparing the 
flame development and intensity of the 10 ∘ CA bTDC and 20 ∘ CA bTDC, 
this distinction is shown clearly, with the more retarded timing (10 ∘ CA 
bTDC) preserving the locally richer H
2 
jet and promoting a more intense 
and faster flame development during the initial stage of the H
2 
com -
bustion. However, when the H
2 
injection timing was advanced further to 
30 ∘ CA bTDC, the charge premixing made a dominant effect on the flame 
intensity. For each of the H
2 
injection timings, it is also noted that the 
peak pixel intensity corresponds with the initial peak in the detected 
flame area, with the exception of the 0 ∘ CA bTDC case. This is a marker 
of the transition from the initial flame propagation into the late-stage 
combustion, which includes a period of mixing controlled combustion 
or simply burnout of the premixed flame.
4. Conclusions
To find flame development process of hydrogen-diesel dual direct 
injection (H2DDI) combustion, dual-camera high-speed imaging has 
been performed in a single cylinder optically accessible engine. Two 
separate injectors were used in the engine with hydrogen delivered by a 
side-mounted, 35-MPa single-hole injector and diesel by a centrally 
mounted multi-hole injector. Two key parameters of interest, H
2 
energy 
proportion and H
2 
injection timing were varied. The H
2 
energy pro -
portion was varied between 70 % and 95 % of the total fuel energy 
whilst the H
2 
injection timing was maintained at 10 ∘ CA bTDC. Further, 
the H
2 
injection timing was varied between 30 and 0 ∘ CA bTDC with a 90 
% / 10 % H
2
/diesel energy proportion. The key findings of this study are 
summarised as follows: 
Fig. 11. Image-based diesel pilot ignition delay and CA10 for 90 % H
2 
/ 10 % diesel energy share with varied H
2 
injection timing (0 – 30 
◦
CA bTDC) and diesel pilot 
injection at 6 
◦
CA bTDC.
A.G. Heaton et al.                                                                                                                                                                                                                              Applications in Energy and Combustion Science 24 (2025) 100382 
11

<!-- PDF_PAGE: 12 -->

1. For over 90 % H
2 
energy proportion, diesel pilot flames show a 
structure of small fragments contained around the centrally mounted 
injector, which cause ignition of a penetrating hydrogen jet. During 
this initial reaction, the hydrogen flame propagates back towards the 
nozzle and downstream as hydrogen-air mixtures are present. This is 
followed by mixing-controlled burn due to the continued hydrogen 
injection and upon the end of injection, the remaining flame signals 
are carried by a swirl flow.
2. Reducing the H
2 
energy share monotonically increased the intensity 
of the initial combustion reaction. This was a result of not only a 
Fig. 12. Late-stage H
2 
flame development for 90 % H
2 
/ 10 % diesel energy share with varied H
2 
injection timing (0 – 30 
◦
CA bTDC) and diesel pilot injection at 6 
◦
CA bTDC. The green and red boundary represents the H
2 
flame and diesel pilot flame respectively with swirl direction represented on the top left frame. Green arrow 
on top left frame indicates H
2 
injector location. Crank angle timings for each frame represent engine cycle position (top left), timing with respect to diesel injection 
(orange) and H
2 
injection (green). Crank angle timings of each frame are marked by circle on in-cylinder pressure and aHRR traces.
A.G. Heaton et al.                                                                                                                                                                                                                              Applications in Energy and Combustion Science 24 (2025) 100382 
12

<!-- PDF_PAGE: 13 -->

larger portion of diesel being present in the cylinder at the start of the 
reaction but also the increased spreading ( i.e. wider spatial distri -
bution) of diesel pilot flames. The increased spreading permits a 
larger volume of the H
2 
to be ignited during the initial interaction 
and consequently reduces the duration of the flame propagation 
phase. Despite this, for all energy shares, the combustion transitions 
to a similar mixing-controlled phase displaying a similar reaction 
zone distribution and steady growth. This also indicates that an 
increased diesel fuel quantity does not disrupt the in-cylinder flow 
with the H
2 
jet momentum dominating the late-stage flame 
development.
3. Advance of the H
2 
injection timing directly influences the intensity of 
the initial reaction and by extension the H
2 
combustion mode. Earlier 
injection timings increase the premixed portion of the H
2 
and exhibit 
a reduced mixing-controlled period. The flame propagation is sen -
sitive also to the local equivalence ratio, later injection timings a 
richer local H
2 
concentration accelerating the recession of the H
2 
flame and the transition into the mixing-controlled phase. However, 
for all H
2 
injection timings the late-stage distribution of the H
2 
reaction zone remains similar, driven by the transition into a mixing- 
controlled burning mode.
4. Ignition delay of the diesel pilot fuel is lengthened proportional to 
the extent of the interaction with H
2 
prior to ignition, ( i.e. earlier H
2 
injection timings). This also introduces some variability to the timing 
of the diesel pilot ignition particularly for earlier H
2 
injection tim -
ings. This effect is likely the result of local dilution by the H
2 
sur -
rounding the diesel fuel. However, despite the delay in ignition 
combustion phasing control is maintained by the better mixed H
2 
charge compensating with a more intense initial heat release.
CRediT authorship contribution statement
Alastar Gordon Heaton: Writing – original draft, Visualization, 
Methodology, Investigation, Data curation. Qing Nian Chan: Writing – 
review & editing, Funding acquisition, Conceptualization. Sanghoon 
Kook: Writing – review & editing, Supervision, Resources, Project 
administration, Conceptualization.
Fig. 13. H
2 
and diesel flame area (top) and mean pixel intensity (bottom) for 90 % H
2 
/ 10 % diesel energy share with varied H
2 
injection timing (0 – 30 
◦
CA bTDC) 
and diesel pilot injection at 6 
◦
CA bTDC. Comparison to diesel-only pilot injection at 6 
◦
CA bTDC. Injection timing and duration for H
2 
and diesel annotated by solid 
and dashed lines respectively. Shaded region represents one standard deviation from ensemble average.
A.G. Heaton et al.                                                                                                                                                                                                                              Applications in Energy and Combustion Science 24 (2025) 100382 
13

<!-- PDF_PAGE: 14 -->

Declaration of competing interest
The author is an Editorial Board Member/Editor-in-Chief/Associate 
Editor/Guest Editor for this journal and was not involved in the edito -
rial review or the decision to publish this article.
The authors declare the following financial interests/personal re -
lationships which may be considered as potential competing interests:
The financial support was provided by the Commonwealth Govern -
ment of Australia ’ s Trailblazer for Recycling and Clean Energy (TRaCE) 
program and Rio Tinto.
Given their role as a member of the Editoral Board, Sanghoon Kook 
had no involvement in the peer-review of this article and has no access to 
information regarding its peer-review. Full responsibility for the edito -
rial process for this article was delegated to another journal editor. If 
there are other authors, they declare that they have no known 
competing financial interests or personal relationships that could have 
appeared to influence the work reported in this paper.
Acknowledgments
The experiments were performed at the UNSW Engine Research 
Laboratory. The authors would like to thank Dr Mark Zhai for his sig -
nificant technical assistance. The financial support was provided by the 
Commonwealth Government of Australia ’ s Trailblazer for Recycling and 
Clean Energy (TRaCE) program and Rio Tinto.
Data availability
Data will be made available on request.
References
[1] Smith D, Ozpineci B, Graves RL, Jones P, Lustbader J, Kelly K, et al. Medium-and 
heavy-duty vehicle electrification: an assessment of technology and knowledge 
gaps. Oak RidgeTN: Oak Ridge National Lab; 2020. https://doi.org/10.2172/ 
1615213 . FebReport No.: ORNL/SPR-2020/7. Contract No.: AC05-00OR22725. 
Sponsored by USDOE Office of Energy Efficiency and Renewable Energy.
[2] Karim GA. The dual fuel engine of the compression ignition type-prospects, 
problems and solutions-a review. SAE Tech Pap 1983:831073. https://doi.org/ 
10.4271/831073 .
[3] Serpa Soares M. de Paris agreement to the United Nations framework convention 
on climate change T.I.A.S. No. 16-1104., (Dec. 12, 2015).
[4] Dennis PA, Dingli RJ, Abbasi Atibeh P, Watson HC, Brear MJ, Voice G. Performance 
of a port fuel injected, spark ignition engine optimised for hydrogen fuel. SAE Tech 
Pap 2012. https://doi.org/10.4271/2012-01-0654 . 2012-01-0654.
[5] Dimitriou P, Tsujimura T. A review of hydrogen as a compression ignition engine 
fuel. Int J Hydrog Energy 2017;42:24470 – 86. https://doi.org/10.1016/j. 
ijhydene.2017.07.232 .
[6] Szwaja S, Naber JD. Dual nature of hydrogen combustion knock. Int J Hydrog 
Energy 2013;38:12489 – 96. https://doi.org/10.1016/j.ijhydene.2013.07.036 .
[7] Yip HL, Srna A, Yuen ACY, Kook S, Taylor RA, Yeoh GH, et al. A review of 
hydrogen direct injection for internal combustion engines: towards carbon-free 
combustion. Appl Sci 2019;9. https://doi.org/10.3390/app9224842 .
[8] Goyal H, Jones P, Bajwa A, Parsons D, Akehurst S, Davy MH, et al. Design trends 
and challenges in hydrogen direct injection (H2DI) internal combustion engines – a 
review. Int J Hydrog Energy 2024;86:1179 – 94. https://doi.org/10.1016/j. 
ijhydene.2024.08.284 .
[9] Bao LZ, Sun BG, Luo QH. Experimental investigation of the achieving methods and 
the working characteristics of a near-zero NOx emission turbocharged direct- 
injection hydrogen engine. Fuel 2022;319. https://doi.org/10.1016/j. 
fuel.2022.123746 .
[10] Liu X, Yang L, Chan QN, Kook S. Split injection strategies for a high-pressure 
hydrogen direct injection in a small-bore dual-fuel diesel engine. Int J Hydrog 
Energy 2024;57:904 – 17. https://doi.org/10.1016/j.ijhydene.2024.01.065 .
[11] Takagi Y, Oikawa M, Sato R, Kojiya Y, Mihara Y. Near-zero emissions with high 
thermal efficiency realized by optimizing jet plume location relative to combustion 
chamber wall, jet geometry and injection timing in a direct-injection hydrogen 
engine. Int J Hydrog Energy 2019;44:9456 – 65. https://doi.org/10.1016/j. 
ijhydene.2019.02.058 .
[12] Kook S., Liu X., Edmonds B. Hydrogen-diesel direct injection dual-fuel system for 
internal combustion engines. 2025 International Application No. PCT/AU2023/ 
050019, US Patent: US2025/0116238A1, 2023.
[13] Liu X, Seberry G, Kook S, Chan QN, Hawkes ER. Direct injection of hydrogen main 
fuel and diesel pilot fuel in a retrofitted single-cylinder compression ignition 
engine. Int J Hydrog Energy 2022;47:35864 – 76. https://doi.org/10.1016/j. 
ijhydene.2022.08.149 .
[14] Liu X, Srna A, Yip HL, Kook S, Chan QN, Hawkes ER. Performance and emissions of 
hydrogen-diesel dual direct injection (H2DDI) in a single-cylinder compression- 
ignition engine. Int J Hydrog Energy 2021;46:1302 – 14. https://doi.org/10.1016/j. 
ijhydene.2020.10.006 .
[15] Mumford D, Baker S, Munshi SR. High performance hydrogen engine applications 
using Westport fuel systems ’ commercially available HPDI technology. In: 
Proceedings of the 43rd international Vienna motor symposium. Vienna, Austria; 
2022. 27 - 29 April .
[16] Frankl S, Gleis S, Karmann S, Prager M, Wachtmeister G. Investigation of ammonia 
and hydrogen as CO2-free fuels for heavy duty engines using a high pressure dual 
fuel combustion process. Int J Engine Res 2020;22:3196 – 208. https://doi.org/ 
10.1177/1468087420967873 .
[17] Rorimpandey P, Zhai G, Kook S, Hawkes ER, Chan QN. Effects of jet interaction 
angle on the ignition and combustion characteristics of hydrogen-diesel dual-fuel 
direct injection. Int J Hydrog Energy 2024;67:172 – 91. https://doi.org/10.1016/j. 
ijhydene.2024.04.166 .
[18] Rorimpandey P, Zhai G, Kook S, Hawkes ER, Chan QN. Effects of energy-share and 
ambient oxygen concentration on hydrogen-diesel dual-fuel direct-injection 
(H2DDI) combustion in compression-ignition conditions. Int J Hydrog Energy 
2024;49:1346 – 61. https://doi.org/10.1016/j.ijhydene.2023.11.106 .
[19] Rochussen J, McTaggart-Cowan G, Kirchen P. Parametric study of pilot-ignited 
direct-injection natural gas combustion in an optically accessible heavy-duty 
engine. Int J Engine Res 2020;21:497 – 513. https://doi.org/10.1177/ 
1468087419836877 .
[20] Rochussen J, McTaggart-Cowan G, Kirchen P. Heat release rate and emissions 
regimes of stratified pilot-ignited direct-injection natural gas combustion. Int J 
Engine Res 2023;24:265 – 85. https://doi.org/10.1177/14680874211046912 .
[21] Gleis S, Frankl S, Prager M, Wachtmeister G. Optical analysis of the combustion of 
potential future E-fuels with a high pressure dual fuel injection system. In: 
Proceedings of the 14th international AVL symposium on propulsion diagnostics. 
Baden-Baden, Germany; 2020. 23-24 June .
[22] Heaton A, Chan QN, Kook S. Flame developments of pilot diesel ignited hydrogen 
jet in an optical dual direct injection engine. SAE Tech Pap 2025. https://doi.org/ 
10.4271/2025-01-0237 . 2025-01-0237.
[23] Hidegh GT, Piz ´ag B, Urbin 
´
A, R ´acz E, J ´ozsa V. Flame emission spectroscopy 
analysis of distributed liquid fuel combustion. Fuel 2023;353:129193. https://doi. 
org/10.1016/j.fuel.2023.129193 .
[24] Otsu N. A threshold selection method from gray-level histograms. IEEE Trans Syst 
Man Cybern 1979;9:62 – 6. https://doi.org/10.1109/TSMC.1979.4310076 .
[25] Musculus MPB, Miles PC, Pickett LM. Conceptual models for partially premixed 
low-temperature diesel combustion. Prog Energy Combust Sci 2013;39:246 – 83. 
https://doi.org/10.1016/j.pecs.2012.09.001 .
[26] Ono R, Nifuku M, Fujiwara S, Horiguchi S, Oda T. Minimum ignition energy of 
hydrogen – air mixture: effects of humidity and spark duration. J Electrost 2007;65: 
87 – 93. https://doi.org/10.1016/j.elstat.2006.07.004 .
[27] Lucchini T, Schirru A, Mehl M, D ’ Errico G, Rorimpandey P, Chan QN, et al. 
Modeling hydrogen – diesel dual direct injection combustion with FGM and 
transported PDF. Proc Combust Inst 2024;40:105213. https://doi.org/10.1016/j. 
proci.2024.105213 .
A.G. Heaton et al.                                                                                                                                                                                                                              Applications in Energy and Combustion Science 24 (2025) 100382 
14
