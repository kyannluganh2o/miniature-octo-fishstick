<!-- PDF_PAGE: 1 -->

A Review of the Fundamental Understanding of Hydrogen−Diesel
Direct Injection Combustion: Recent Advances and Future Outlook
Patrick Rorimpandey, Kirtan Aryal, Guanxiong Zhai, Shijie Xu, Kar Mun Pang, Guan Heng Yeoh,
Sanghoon Kook, and Qing Nian Chan*
Cite This: Energy Fuels 2025, 39, 16538−16560
 Read Online
ACCESS
Metrics & More
 Article Recommendations
ABSTRACT: Hydrogen−diesel dual-fuel direct injection (DI)
combustion has emerged as a promising strategy for integrating
hydrogen into compression-ignition engines, offering potential
benefits in terms of efficiency, emissions reduction, and fuel
flexibility. Driven by the potential to decarbonize hard-to-electrify
sectors while leveraging existing engine platforms, there is
increasing interest in hydrogen utilization in heavy-duty
applications. This review examines recent advances in the
fundamental understanding of hydrogen−diesel dual-fuel DI
combustion under compression-ignition engine relevant condi-
tions. It focuses on key factors influencing ignition, jet interactions,
and combustion development, addressing a critical knowledge gap
in dual-fuel DI technology with hydrogen, where recent advance-
ments have provided new insights. Studies indicate that injection timing and sequence play a crucial role in determining combustion
mode, transitioning between premixed and mixing-controlled regimes depending on hydrogen−diesel interactions. Early hydrogen
injection promotes premixed combustion but can induce pressure oscillations, whereas later injection favors a mixing-controlled
mode with lower peak heat release. Jet−jet interactions further complicate combustion, with converging injection configurations
facilitating flame propagation but extending ignition delay due to increased preignition mixing. Experimental investigations have
shown that injection duration influences jet momentum balance, affecting the entrainment of pilot combustion products into the
hydrogen jet and, consequently, flame stabilization and heat release characteristics. Ambient conditions also have a significant effect
on dual-fuel combustion. Lower ambient temperatures extend the ignition delay and fuel−air mixing time before ignition, leading to
higher peak heat release rates. Reduced oxygen concentrations shift flame stabilization downstream and increase lift-off distance
variability. Forced laser-induced ignition studies, supported by simplified numerical analysis, suggest that edge-flame deflagration
mechanisms explain flame recession and stabilization under low-oxygen and low-temperature conditions. Injection parameters,
including the pressure and nozzle diameter, also influence hydrogen jet development. Higher injection pressure enhances jet
penetration and mixing but may extend the diffusion flame length, increasing heat transfer losses. Similarly, larger nozzle diameters
increase the mass flow rate and heat release but also increase the hydrogen flame length. Overall, hydrogen−diesel dual-fuel DI
combustion presents a viable pathway toward cleaner and more efficient engine operation. However, further research is required to
optimize combustion processes and fully realize its potential.
1. INTRODUCTION
1.1. Motivation for Hydrogen. Hydrogen has garnered
significant interest as an energy carrier for stationary and mobile
power generation for several reasons. First, hydrogen can be
produced from a wide variety of energy sources, including
renewable sources
1,2
such as wind, solar, and hydroelectric
power. Renewable energy sources are particularly attractive due
to their sustainability and the potential for zero carbon dioxide
emissions during hydrogen production, aligning with global
decarbonization goals.
3,4
Second, when hydrogen is utilized to generate power through
processes like combustion or fuel cells, the primary reaction
product is water vapor.
5
This characteristic enables a carbon-free
energy cycle when hydrogen is produced by using renewable
energy, thus creating a closed-loop system that avoids carbon
dioxide emissions throughout the entire energy production and
Received: April 28, 2025
Revised: July 24, 2025
Accepted: August 6, 2025
Published: August 21, 2025
Reviewpubs.acs.org/EF
© 2025 American Chemical Society
16538
https://doi.org/10.1021/acs.energyfuels.5c02216
Energy Fuels 2025, 39, 16538−16560
Downloaded from pubs.​acs.​org/​enfuem/​article-pdf/​39/​35/​16538/​41340814/​ef5c02216.​pdf by SHANDONG UNIV user on 26 August 2026

<!-- PDF_PAGE: 2 -->

consumption pathway. This feature is particularly advantageous
in the pursuit of decarbonization.
Third, advances in electrolyzer technologies, such as their
capability to dynamically respond to grid fluctuations, enhance
hydrogen’s viability as an energy carrier.
6,7
For example,
electrolyzers can be used to convert surplus renewable energy
into hydrogen through power-to-gas processes, allowing for
energy buffering and storing. The hydrogen can be stored for
stationary power generation applications,
6
or onboard when
used for mobile applications. The potential for storing hydrogen
in onboard vehicle systems is appealing given the vast global
scale of transportation,
5
offering energy buffering and storage
options.
Furthermore, hydrogen’s adaptability to various applications,
from industrial processes to fuel cell vehicles, highlights its
potential as a cornerstone of the energy transition. By enabling
energy storage, reducing reliance on fossil fuels, and offering
solutions for stationary and mobile applications, hydrogen holds
promise as a key enabler for a sustainable and resilient energy
future.
8
1.2. Motivation for Hydrogen-Fueled Internal Com-
bustion Engines. Previous research into hydrogen as a vehicle
energy source has primarily focused on internal combustion
engines (ICEs) and fuel cells, two technologies that
fundamentally differ in how they convert hydrogen’s chemical
energy into propulsion. Fuel cells generate electrical energy
through electrochemical reactions in an electrolyte, which is
then used to power an electric motor.
9
In contrast, hydrogen-
fueled ICEs combust hydrogen within cylinders, converting the
resulting thermal energy into mechanical energy typically via
piston motion and a crankshaft.
10,11
In mobile applications, fuel cell vehicles generally exhibit
higher fuel efficiency than ICEs.
12,13
Moreover, fuel cells
produce zero tailpipe emissions and operate with less noise,
making them particularly attractive for applications where
environmental impact and noise reduction are critical
considerations.
14
However, fuel cells currently have higher
production and recycling costs due to their reliance on rare-earth
materials, such as platinum.
12
Moreover, fuel cell systems are less
durable in environments with strong vibrations, thermal cycles,
shocks, and humidity and are more sensitive to hydrogen fuel
and air impurities.
15,16
In contrast, ICEs offer greater robustness
and impurity tolerance while also benefiting from existing
infrastructure and well-established manufacturing capabilities,
providing them with a competitive advantage.
Given the distinct advantages and limitations of both
technologies, fuel cells and hydrogen-fueled ICEs are likely to
coexist in a future hydrogen economy. The preference for ICEs
over fuel cells may be driven by lower costs and higher durability,
the ability to leverage existing resources and infrastructure, ease
of retrofitting, and resilience to fuel impurities.
16,17
Additionally,
from a sustainability perspective, modern ICEs are predom-
inantly constructed from recyclable materials, such as common
metals.
5
1.3. Motivation for Hydrogen-Fueled Compression-
Ignition Engines. The interest in hydrogen use in
compression-ignition engines stems from their prevalence in
sectors difficult to electrify, such as heavy-duty transportation,
18
marine, and off-road applications. These sectors typically require
high energy outputs, higher up-time operations, and rapid
refueling, challenges that current battery electric solutions
struggle to meet due to limitations in energy density, charging
times, and infrastructure.
19
Consequently, compression-ignition
engines represent a promising, yet relatively unexplored, market
for hydrogen, especially compared with the more rapidly
electrifying light-duty vehicle sector.
A key advantage of transitioning existing compression-
ignition engines to hydrogen is that it avoids complete vehicle
redesign, allowing the continued use of current fleets and
reducing the costs associated with premature vehicle replace-
ment. Effective hydrogen integration could thus not only
conserve resources but also expedite the adoption of cleaner fuel
technologies by minimizing transition costs and time, facilitating
immediate decarbonization in these traditionally hard-to-abate
sectors, and thereby contributing to global emissions reduction
efforts.
20
Compression-ignition engines also offer inherently higher
thermal efficiency compared to alternative engine types,
primarily due to their ability to operate at higher compression
ratios.
10,21
This efficiency advantage is further enhanced by
lower pumping losses, as these engines typically operate without
intake air throttling.
22,23
Given these characteristics, integrating
hydrogen into compression-ignition engines presents a compel-
ling pathway for efficient hydrogen utilization, supporting the
transition to a more sustainable energy future.
1.4. Hydrogen Properties and Implications for
Integration into Internal Combustion Engines. The
distinct properties of hydrogen, compared to conventional
carbon-based fuels, such as diesel and natural gas, present several
challenges for its application in ICEs. Table 1 provides a
comparison of hydrogen’s key physical and thermal properties
with conventional energy carriers, including methane (a
surrogate for natural gas) and diesel.
Hydrogen’s wide flammability limits and high laminar flame
speed offer advantages by enabling combustion under lean
conditions and facilitating short combustion durations, thereby
improving thermal efficiency.
11,30−32
However, these same
properties, along with its short quenching distance, increase
the risk of backfire in ICEs with external mixture formation,
where unburnt hydrogen can ignite prematurely in the intake
manifold. Backfire can disrupt engine operation and, in severe
cases, cause significant mechanical damage.
Hydrogen’s low volumetric energy density necessitates the
injection of larger fuel volumes to meet power demands. In port
injection systems, this increased fuel volume can displace
incoming air, negatively affecting engine performance and
reducing the power output. This issue is well-documented in
ICEs using external mixture formation with gaseous fuels.
31
Table 1. Combustion Properties of Hydrogen, Methane
(Approximation for Natural Gas), and Conventional
Diesel
17,21,24−29
Property Hydrogen Methane Diesel
Adiabatic flame temperature
a . c . d
(K) 2318 2190 2559
Autoignition temperature (K) 858 813 483
Density
a . b
(kg/m
3
) 0.082 0.717 840
Flammability limits
e
(vol %) 4−76 5.3−15.0 0.7−5.0
Laminar flame speed
a . c . d . e
(m/s) 1.85 0.38 0.87
Lower heating value (MJ/kg) 120.0 46.7 43.2
Minimum ignition energy
e
(mJ) 0.02 0.28 0.24
Quenching distance
a . c . e
(mm) 0.64 2.1 -
Volumetric energy content
a . b
(MJ/m
3
) 10.7 33 34,600
a
At 1 bar.
b
At 273 K.
c
at 298 K.
d
At stoichiometry,
e
In air.
Energy & Fuels pubs.acs.org/EF Review
https://doi.org/10.1021/acs.energyfuels.5c02216
Energy Fuels 2025, 39, 16538−16560
16539
Downloaded from pubs.​acs.​org/​enfuem/​article-pdf/​39/​35/​16538/​41340814/​ef5c02216.​pdf by SHANDONG UNIV user on 26 August 2026

<!-- PDF_PAGE: 3 -->

Despite its high autoignition temperature, hydrogen’s low
ignition energy makes it highly susceptible to preignition,
triggered by hot spots or residual deposits within the
combustion chamber.
17,33
Preignition refers to the spontaneous
initiation of combustion before the intended ignition timing,
potentially leading to excessively high in-cylinder pressure and/
or combustion knock.
34,35
Knocking occurs when the unburnt
end-gas near the cylinder walls or hot spots autoignites
uncontrollably, which can disrupt combustion phasing and
damage the engine in severe cases.
Additionally, hydrogen’s small molecular size presents
challenges in maintaining leak-tight fuel delivery systems,
requiring stringent design and operational safeguards.
31
Furthermore, hydrogen combustion generates steep temper-
ature gradients near the cylinder walls due to its high adiabatic
flame temperature, leading to increased heat transfer losses and
accelerated engine oil degradation. These effects can com-
promise the engine durability and efficiency over time.
Addressing these challenges is essential for the successful
integration of hydrogen into ICEs.
1.5. Motivation for Adopting Dual-Fuel Direct
Injection to Address Hydrogen Integration Challenges.
Numerous strategies have been explored to address the
challenges associated with hydrogen utilization in ICEs.
17
This
review focuses on fuel delivery and ignition strategies,
specifically the dual-fuel direct injection (DI) approach, which
shows considerable potential to mitigate some of hydrogen’s
inherent challenges.
The fuel injection and intake valve operation are decoupled in
DI, which introduces flexibility in the timing and feeding control
of fuel and air.
36,37
This offers critical advantages in managing
hydrogen’s unique properties.
38
By injecting hydrogen after
intake valve closure, DI minimizes the air displacement issue
observed with port injection. Furthermore, the in-cylinder
injection location mitigates the risk of backfires in the intake
manifold, a concern with external mixture formation. Precise
control over injection timing allows for minimization of the
hydrogen−air mixture’s residence time in the cylinder, reducing
exposure to potential ignition sources such as hot spots or
residual deposits and mitigating preignition risks. Additionally,
DI can help manage compression work losses associated with
the use of gaseous fuels.
The dual-fuel strategy,
39
combined with DI, involves
introducing a pilot fuel, such as diesel, with a shorter ignition
delay time (i.e., lower autoignition resistance) to assist in
igniting hydrogen. This configuration, referred to as hydrogen−
diesel dual-fuel DI (H
2
DDI) in some of the recent literature, has
garnered research interest due to its practical advantages.
40,41
One key benefit of H
2
DDI is the potential for retrofitting
existing diesel engines, offering a cost-effective pathway for
transitioning to hydrogen-fueled systems.
6
Additionally, the
dual-fuel approach provides operational flexibility, allowing for
dynamic adjustment of the energy contribution from each fuel to
meet varying engine demands.
42
1.6. Scope. This review begins by discussing hydrogen’s
unique physical and combustion properties and their
implications for ICE performance. It then examines various
approaches and findings related to the challenges of integrating
hydrogen into ICEs, with a particular focus on advancements in
H
2
DDI technology, which is the central theme of this review.
Emphasis is placed on the fundamental aspects of dual-fuel DI
engine operation.
While engine-level studies provide valuable insights into the
practical feasibility of dual-fuel direct injection systems, they
often offer a limited understanding of the underlying
mechanisms influencing performance. This is because engine-
level results reflect the combined effects of multiple interacting
parameters and operational factors. Without a clear under-
standing of these fundamental processes, optimizing system
performance remains largely empirical, relying on trial-and-error
methods rather than predictive, data driven strategies. This
limits the ability to generalize findings across different engine
platforms. Advancing fundamental knowledge of in-cylinder
processes is therefore essential for developing more accurate
models and control strategies, which are crucial for accelerating
the development and deployment of this technology. To address
this gap, this review prioritizes fundamental experimental
investigations while incorporating relevant engine and numer-
ical studies where appropriate.
A previous review by this group
17
discussed hydrogen’s
properties and the challenges associated with its implementation
in ICEs. Key points from that work are summarized here for
context and completeness. While that review identified dual-fuel
DI as a promising approach, it lacked detailed exploration due to
limited research at the time. This review addresses this gap by
incorporating recent advances in the fundamental under-
standing of dual-fuel DI technology with hydrogen.
This paper is structured as follows: Section 1 provides an
introduction. Section 2 compares various injection and ignition
methods, focusing specifically on the dual-fuel strategy of using a
pilot diesel jet to ignite a directly injected hydrogen jet, which is
the primary subject of this review. Section 3 presents an in-depth
discussion on the factors influencing hydrogen−diesel dual-fuel
combustion processes. Section 4 addresses the challenges and
opportunities for extending the fundamental findings. Finally,
Section 5 offers a conclusion.
2. HYDROGEN INTERNAL COMBUSTION ENGINE
CATEGORIZATION
ICE designs can be categorized based on the strategies employed
for mixing and combusting the fuel−air mixture. These
strategies include the method of fuel injection, the process of
mixture formation, and the approach used for ignition.
For hydrogen ICEs, the two primary methods of mixture
formation studied are
• Port-Fuel Injection (PFI): Hydrogen is injected into the
intake air stream before entering the cylinder.
• Direct Injection (DI): Hydrogen is injected directly into
the cylinder during the compression stroke.
The widely studied ignition strategies are
• Spark Ignition: An external electrical discharge, produced
by a spark plug,
43
ignites the fuel−air mixture within the
combustion chamber.
• Compression Ignition: The fuel−air mixture autoignites
due to the high pressure and temperature achieved
through compression in the cylinder.
Injection and ignition strategies for hydrogen ICEs are shaped
by considerations such as ease of implementation, mitigation of
combustion anomalies, and the goal of enhancing the efficiency
and performance. This section examines these strategies within
the context of hydrogen ICEs, evaluating the advantages and
limitations of different approaches, with a focus on their ability
Energy & Fuels pubs.acs.org/EF Review
https://doi.org/10.1021/acs.energyfuels.5c02216
Energy Fuels 2025, 39, 16538−16560
16540
Downloaded from pubs.​acs.​org/​enfuem/​article-pdf/​39/​35/​16538/​41340814/​ef5c02216.​pdf by SHANDONG UNIV user on 26 August 2026

<!-- PDF_PAGE: 4 -->

to address the implementation challenges posed by hydrogen’s
unique properties.
2.1. Port-Fuel Injection with Spark Ignition. PFI is a
widely investigated fueling strategy for hydrogen ICEs due to its
relatively straightforward implementation, requiring only the
addition of an injection system to the intake port.
11
PFI operates
at relatively low pressures, typically ranging from 2 to 8 bar.
11
This approach is frequently paired with spark ignition to ignite
the mixture and has been extensively studied and demonstrated
in early hydrogen ICE research.
11,44
Notable examples include the Ford P2000 test vehicle, which
featured a modified 2 L four-cylinder engine and achieved a peak
brake thermal efficiency of 38% at a 0.5 equivalence ratio and
2000 rpm.
45,46
Another example is the BMW Hydrogen 7, a
bifuel vehicle based on a modified 6 L V12 engine capable of
operating on either gasoline or hydrogen.
31,47
Recent advance-
ments in spark ignition-PFI strategies for hydrogen ICEs have
been reported, with companies such as Daimler and Volvo
developing engines with efficiencies of up to 44.5%.
16
H2Deutz
and Keyou have employed the spark ignition-PFI approach with
modified Deutz 7.8 L six-cylinder engines, with production
planned by 2024.
16
Research indicates that NO
x
emissions in hydrogen ICEs
increase when the equivalence ratio exceeds 0.5, peak around
0.75, and decline with richer mixtures.
11,46,48
This trend
influenced the design of the BMW Hydrogen 7, which operated
at equivalence ratios of approximately 0.55 (lean, minimizing
NO
x
emissions without requiring exhaust after-treatment) or
1.03 (slightly rich, using a three-way catalytic converter, where
unburned hydrogen in the exhaust aided NO
x
reduction).
Intermediate equivalence ratios were avoided due to the absence
of effective NO
x
after-treatment systems in that range.
31
Lean
operation in hydrogen ICEs also mitigates abnormal combus-
tion phenomena such as preignition and knocking.
11,46
By
lowering combustion temperatures and pressures, lean con-
ditions reduce the likelihood of these events. Additionally,
limiting the compression ratio serves as another strategy to
minimize preignition and knocking risks.
31
As previously noted, hydrogen PFI presents challenges,
including backfiring and reduced power density.
11,17,31
While
tailored approaches can address some of these issues�such as
strategically positioning hydrogen injection to allow initial air
entry, as implemented in the bifuel 12-cylinder hydrogen engine
of the BMW 7 Series,
31
or employing turbocharging to boost
specific power output�other challenges remain and need
addressing. Hydrogen PFI was also studied numerically, as in the
work of Menaa et al.,
49
which explored the potential
optimization of a hydrogen-timed manifold injection system
by adjusting valve lift profiles and hydrogen injection
parameters. The objective was to prevent backfire, improve
volumetric efficiency, and enhance mixture formation quality in
a dual-fuel diesel engine operating at a high load and high
hydrogen energy share. Using computational simulations in
ANSYS Fluent, the study evaluated operating conditions to
mitigate backfire and preignition risks while improving
volumetric efficiency. It also examined the influence of hydrogen
start-of-injection timing on precooling effects, which could
reduce preignition sources and quench residual hot combustion
products. However, experimental validation is required.
2.2. Direct Injection with Spark Ignition. Hydrogen DI
offers an alternative to PFI, where only air is inducted during the
intake stroke, maximizing the cylinder’s volumetric efficiency. As
previously noted, DI provides flexibility in the start of injection
(SOI) timing, allowing for tailored fuel−air mixture stratifica-
tion. However, this flexibility necessitates DI systems to operate
across a broader injection pressure range (5−300 bar) compared
to PFI systems, depending on injection timing and cylinder back
pressure. Early injection, which promotes a more homogeneous
mixture at ignition, typically requires lower pressures (5−20
bar). In contrast, late injection near top dead center (TDC),
used to create stratified mixtures, requires higher pressures
(100−300 bar) to overcome elevated cylinder pressures at that
point in the cycle.
5
Previous studies have explored the impact of DI timing on
mixture distribution, emissions, and efficiency. Wallner et al.,
50
for example, investigated these effects using a single-cylinder
research engine equipped with a Westport high-pressure
injector. The injector featured a 13-hole nozzle with a 60°
included angle and operated at a constant injection pressure of
100 bar. Optical endoscope measurements were used to assess
mixture stratification with different injection settings. The study
reported that, at low loads, an early injection time produced a
homogeneous fuel−air mixture with a low equivalence ratio at
spark ignition, resulting in lower NO
x
emissions. Conversely,
later SOI timings led to localized rich zones at spark ignition,
increasing NO
x
emissions. However, at high loads, the trend
reversed with early SOI timings producing homogeneous
mixtures nearing stoichiometry, resulting in higher NO
x
emissions. In contrast, late SOI timings facilitated stratification,
creating locally rich zones along with lean regions. The study
attributed the reduction of overall NO
x
emissions to charge
stratification, avoiding the forming of air−fuel ratio regimes
associated with NO
x
formation. These findings highlight the
complex interplay among SOI timing, mixture distribution, and
other factors that influence the performance of DI hydrogen
engines.
50
Knocking can be a challenge in spark-ignition DI combustion,
particularly with premixed charges where unburned end-gas can
autoignite ahead of the flame front.
51
This issue is more
pronounced in larger engines, where increased cylinder
displacement and lower engine speeds lead to longer flame
travel times, increasing the likelihood of end-gas autoignition.
One mitigation strategy involves limiting the compression ratio
in certain engine designs to reduce this risk. Alternatively, non-
premixed compression-ignition strategies offer a potential
solution. Hydrogen DI can be implemented with near-TDC
injection to promote mixing-controlled combustion, charac-
terized by a slower burning rate. This approach reduces the risk
of rapid pressure rises and subsequent pressure oscillations (e.g.,
pressure ringing or knocking).
DI also enables more flexible injection strategies compared to
PFI. For example, multiple-injection approaches, such as two-
pulse injection, have been investigated to optimize combustion
and reduce emissions. Studies by Wallner et al.
52
and Wimmer et
al.
53
examined this strategy using single-cylinder research
engines. In two-pulse injection, the first pulse introduces a
lean, homogeneous mixture with an equivalence ratio below the
critical threshold for significant NO
x
formation. A second
injection during the combustion phase achieves the desired load,
combusting near the rich ignition limit due to a limited mixing
time. This strategy effectively reduces NO
x
emissions.
53
2.3. Port-Fuel/Direct Injection with Compression
Ignition. As noted, utilizing hydrogen in compression-ignition
engines offers an efficient pathway for hydrogen application.
Additionally, near-TDC hydrogen DI can be used to address
challenges such as preignition risk and compression losses. In
Energy & Fuels pubs.acs.org/EF Review
https://doi.org/10.1021/acs.energyfuels.5c02216
Energy Fuels 2025, 39, 16538−16560
16541
Downloaded from pubs.​acs.​org/​enfuem/​article-pdf/​39/​35/​16538/​41340814/​ef5c02216.​pdf by SHANDONG UNIV user on 26 August 2026

<!-- PDF_PAGE: 5 -->

conventional compression-ignition engines fueled with diesel,
power generation relies on the fuel’s autoignition under high
pressure and temperature. However, this approach is challenging
with hydrogen due to its high autoignition temperature, which
can particularly affect cold-start performance. As a result,
alternative strategies, such as higher compression ratios,
preheating of intake air, and hydrogen multiple-injection, are
required to achieve reliable ignition. For instance, in a previous
study, under ambient conditions without ignition aids, a
homogeneous hydrogen−air mixture at an equivalence ratio of
0.22 requires a compression ratio of 26 in a 0.5 L single-cylinder
engine, while a leaner equivalence ratio of 0.11 requires an
impractical compression ratio of 42.
54
The preheating intake air
to temperatures of up to 100 °C and utilizing high exhaust gas
recirculation (EGR) rates have also been explored in other
studies.
21,55,56
However, these measures are often considered
impractical for widespread application due to controllability
issues and their effectiveness being limited to low-load
conditions.
5
It is noteworthy that a recent study
57
performed a
targeted evaluation of multiple hydrogen injections to achieve
robust ignition, an approach widely explored for conventional
fuels like diesel
58
and gasoline
59,60
but not for hydrogen.
Conducted in an optically accessible chamber simulating
engine-like conditions, the study demonstrated that a first
injection significantly advanced the ignition of a subsequent
injection, reducing ignition delay times at higher temperatures
(exceeding 1000 K). However, less robust ignition was observed
at 970 K, necessitating varied injection parameters, such as
increasing the first injection quantity and the dwell time (the
interval between the first and second injections) between
injections to still attain robust ignition. These findings highlight
the potential of double injection strategies for robust hydrogen
ignition but also emphasize the need for further research to
understand the tuning required to ensure robust ignition across
all operating conditions.
The dual-fuel approach, which coinjects hydrogen with a
lower autoignition temperature fuel like diesel, presents a
promising ignition strategy for hydrogen compression-ignition
engines. Diesel autoignition generates a high-temperature
environment that facilitates hydrogen ignition, addressing
hydrogen’s high autoignition resistance. This method also offers
operational flexibility by allowing fuel ratio adjustments based
on availability.
40,61
Additionally, the wider dispersion of pilot
diesel in the cylinder reportedly promote robust ignition by
creating multiple ignition sites, enhancing flame propagation,
reducing unburnt hydrogen, and lowering the risk of end-gas
autoignition and knocking.
62,63
However, the interaction
between the pilot fuel and hydrogen may change the
autoignition characteristics of the former, complicating the
dual-fuel approach.
The dual-fuel concept can be implemented with PFI or DI,
while the pilot diesel is conventionally directly injected.
64
Traditional dual-fuel engine configurations involving gaseous
fuels have predominantly used natural gas, with the gaseous fuel
introduced via PFI.
65,66
In such systems, the gaseous fuel forms a
homogeneous charge with the intake air, which is then ignited by
the pilot diesel. Research on stratified combustion under engine-
relevant conditions, where fuels are injected near TDC, is also
increasing (e.g., ref 67). This approach promotes diffusion
combustion, limiting fuel−air mixtures beyond flammability
thresholds and reducing incomplete combustion and methane
slip�a critical concern due to methane’s high global warming
potential.
68,69
Optical engine research by Daimler AG and the
Technical University of Munich, using 2.13 and 4.8 L engines
with Westport and Woodward L’Orange injectors, respectively,
exemplifies this trend.
69,70
There have been increasing efforts in recent years to explore
hydrogen−diesel dual-fuel approaches for internal combustion
engines. Given the recency of these developments, press releases
are referenced below, as they offer the most up-to-date insights
into ongoing industrial initiatives and technological demon-
strations, which are not yet captured in the academic literature.
In the domain of four-stroke engines, MAN Engines developed
the D2862 LE448, a V12 diesel engine adapted for dual-fuel
operation with hydrogen and diesel, powering the Hydrocat 48
crew transfer vessel.
71
Using an adaptor to introduce hydrogen
into the charge air and DI for a diesel pilot, this engine achieves
CO
2
reductions averaging 50%, with peaks up to 80%, compared
to pure diesel operation while retaining full diesel functionality.
Similarly, Yanmar Power Technology Co., Ltd. conducted a
land-based test of a pilot-ignition hydrogen four-stroke high-
speed engine for coastal vessel power generation, achieving a
rated output of 500 kW as part of the Nippon Foundation’s zero-
emission ship project.
72
This system employs a pilot fuel to burn
a premixture of hydrogen and air, though the pilot fuel quantity
across operating conditions are not publicly disclosed. In
contrast, within two-stroke engine applications, MAN Energy
Solutions and MITSUI E&S Co. Ltd. tested a 50 cm-bore MAN
B&W engine (4S50ME-T, 7 MW), operating one cylinder on
hydrogen up to 100% load.
73−75
Adapted from the liquefied
natural gas-fired ME-GI design with DI for both hydrogen and
diesel pilots, it achieved stable combustion, supplying 95% of the
heat value from hydrogen at full load, with cylinder pressure
curves matching those of diesel-operated cylinders and reducing
greenhouse gas emissions by up to 95%, the remainder from the
pilot fuel. For heavy-duty applications, Westport Fuel Systems’
hydrogen high pressure direct injection (HPDI) system,
demonstrated with Scania AB on the 13 L CBE1 platform,
reportedly attained a peak brake thermal efficiency of 51.5%,
complemented with 48.7% at road load, with engine-out NO
x
levels comparable to the base diesel engine.
76
This system uses
high-pressure DI for both hydrogen and diesel pilot. Exact
operational parameters, such as injection pressures and fuel
ratios, are not publicly detailed. However, it is noted that
Westport’s natural gas HPDI technology employing a dual
concentric needle injector for late-cycle injection and diffusion
combustion, can operate at 300−600 bar.
77
These recent
developments highlight the growing interest in dual-fuel
strategies. Operational safety, specifically the ability to run on
diesel only to ensure uninterrupted engine operation upon
hydrogen depletion, was cited as a factor in the industry
initiative’s decision to test the dual-fuel approach.
71
2.4. Hydrogen−Diesel Direct-Injection Compression-
Ignition Engine Studies. There is an increasing number of
studies exploring the use of dual-fuel DI in hydrogen ICE to
address the challenges associated with PFI. For example, Liu et
al.
41
compared hydrogen PFI and DI at TDC in a hydrogen−
diesel engine at intermediate load with a fixed total energy input
of 820 J and a 50% hydrogen energy fraction. Their results
showed that the DI enabled mixing-controlled hydrogen
combustion produced lower in-cylinder pressures, leading to
reduced engine efficiency compared to PFI under the test
settings used. However, with the PFI approach, the engine
exhibited pressure ringing.
Further engines studies by Liu et al. provided additional
insights into H
2
DDI engine technologies.
40,78
These studies,
Energy & Fuels pubs.acs.org/EF Review
https://doi.org/10.1021/acs.energyfuels.5c02216
Energy Fuels 2025, 39, 16538−16560
16542
Downloaded from pubs.​acs.​org/​enfuem/​article-pdf/​39/​35/​16538/​41340814/​ef5c02216.​pdf by SHANDONG UNIV user on 26 August 2026

<!-- PDF_PAGE: 6 -->

along with the aforementioned PFI versus DI study,
41
used an
existing four-cylinder production engine (Hyundai D4EA
series) modified to operate only as a single cylinder, with the
addition of a modified gasoline DI injector placed within the
existing glow-plug hole that was 45° relative to the engine head
plane, for hydrogen injection. The modified naturally aspirated
engine has a bore diameter of 83 mm, stroke length of 92 mm, a
displacement of 497.8 cm
3
and a compression ratio of up to 17.7.
Power output was evaluated by using the indicated mean
effective pressure (IMEP) as the primary comparative
parameter. For these studies, a seven-hole diesel injector was
positioned perpendicular to the engine head plane, with fuel jets
exiting at an included angle of 150°. For hydrogen injection, the
injector was modified to a single-hole configuration by applying
a slide-on cap with a 1 mm orifice diameter over the original
injector.
79
Figure 1 shows a schematic of the injector
configuration used.
The experiments were conducted across a range of hydrogen
and diesel energy shares while maintaining a fixed total energy
output. The energy share from hydrogen was varied between
10% and 90%, depending on the study,
40,78
with diesel providing
the remainder of the energy input. The tests included a hydrogen
SOI timing range from 180° CA bTDC to TDC. In the
studies,
40,78
diesel SOI timings were individually adjusted for
each energy share to ensure that the crank angle at which 50% of
the total heat release occurs (CA50) was consistently
maintained between cases. Diesel-only operation was used as a
baseline for comparison with dual-fuel configurations. The
results of the studies indicate that earlier hydrogen injection
timings were associated with combustion modes dominated by
premixed combustion, while later injection timings transitioned
to mixing-controlled combustion.
40
In ref 40, the earliest hydrogen injection timing was adjusted
based on the hydrogen energy share, as earlier injections
promote premixed combustion, which, at higher hydrogen
fractions, can result in excessive pressure rise rates, knocking,
and audible noise.
40
By limiting the earliest hydrogen injection
timing to 90° CA bTDC, the study achieved hydrogen energy
fractions of up to 90% without combustion anomalies. This
approach significantly reduced carbon dioxide emissions due to
the corresponding decrease in the diesel energy contribution.
The results from ref 40 highlighted a trade-off between engine
performance, indicated by IMEP and efficiency, and NO
x
emissions. For example, increasing hydrogen energy shares
improved indicated efficiency, reaching 57.2% at a 90%
hydrogen share�representing a 27% improvement over the
diesel baseline�while maintaining the coefficient of variation
within acceptable limits
40
when hydrogen injection timing was
set at 90° CA bTDC. However, this efficiency gain was
accompanied by NO
x
emissions up to three times the diesel
baseline. At a hydrogen injection timing of 40° CA bTDC, the
hydrogen charge distribution, which was intermediate between
well-mixed and stratified, provided a balanced trade-off. This led
to a maximum IMEP 13.3% above the diesel baseline, while
reducing NO
x
emissions to approximately 60% above the diesel
baseline. Very late injection timings, combined with high
hydrogen energy fractions (80−90%), reduced NO
x
emissions
below the diesel baseline but at the expense of IMEP and
efficiency. This reduction was attributed to hydrogen injection
occurring past the TDC and into the expansion stroke,
impacting combustion phasing control.
To provide complementary insights, Wang et al.
80
used
CONVERGE 3.0 to perform three-dimensional numerical
simulations of in-cylinder processes in Liu et al.’s engine.
81
Their study employed a multihole injector within a recessed
glow plug duct, similar to Figure 1 but without the slide-on cap,
for direct hydrogen injection. This configuration simulated a
minimally modified engine to assess its viability for hydrogen−
diesel operation. The in-cylinder flow was modeled using
unsteady Reynolds-averaged Navier−Stokes (RANS) equations
within a three-dimensional domain. The study examined the
effects of varying hydrogen injection timing (from 180° CA
bTDC to 40° CA bTDC) on emissions and efficiency, while
adjusting diesel injection timing near TDC to maintain
consistent combustion phasing. In their study, the fuel energy
share was maintained at 50% for both diesel and hydrogen. The
numerical results showed that early hydrogen injection
produced a near-homogeneous, fuel−lean mixture, resulting in
primarily premixed combustion. Intermediate injection timings
led to a moderately stratified mixture with hydrogen under near
stoichiometric conditions, yielding the highest engine efficiency
but also elevated NO
x
emissions. Late injection created a highly
stratified charge with predominantly fuel-rich hydrogen
mixtures, leading to mixing-controlled combustion. Importantly,
the simulations revealed that while late injection minimized wall
heat loss and NO
x
emissions, it also resulted in a high fraction of
unburnt hydrogen, causing an efficiency penalty. This penalty
was primarily due to incomplete combustion, with unburnt
hydrogen trapped in crevices and within the injector duct. These
findings highlight injector placement consideration when
retrofitting engines for hydrogen−diesel operation.
The dual-fuel DI approach, employing a multiple-injection
strategy, was recently investigated.
78
Hydrogen was injected in
two distinct pulses: an initial injection followed by a secondary
injection. Injection proportions and timings were varied to
optimize the in-cylinder fuel−air mixture and influence engine
performance. The study examined multiple-injection strategies
under varying dwell times and different energy distributions
between the two hydrogen injections. Pilot diesel injection
timing was adjusted to maintain consistent combustion phasing
across different cases, facilitating a comparison. Experiments
were conducted using the same modified experimental engine
and DI injector configuration as ref 40 (see Figure 1). The study
reported a transition between injection modes by adjusting the
energy ratios between the first and second injections, with a
higher hydrogen fraction in the first injection promoting
premixed combustion, while a higher hydrogen fraction in the
second injection led the combustion toward a mixing-controlled
dominant mode. This latter mode was characterized by late-
cycle combustion but reduced NO
x
emissions. The findings
Figure 1. Schematic diagram of the injector configuration used in the
studies by Liu et al.,
40,78
featuring a capped single-hole gasoline direct-
injection injector alongside a diesel injector. Reproduced with
permission from ref 78. Copyright 2024 Elsevier.
Energy & Fuels pubs.acs.org/EF Review
https://doi.org/10.1021/acs.energyfuels.5c02216
Energy Fuels 2025, 39, 16538−16560
16543
Downloaded from pubs.​acs.​org/​enfuem/​article-pdf/​39/​35/​16538/​41340814/​ef5c02216.​pdf by SHANDONG UNIV user on 26 August 2026

<!-- PDF_PAGE: 7 -->

Table 2. Overview of the Fundamental Oriented Experimental Studies Reviewed in Section 3
Reference
Number
Experimental
Rig Fuel and Other Parameters Parameters Variation
86 Single-cylinder
engine
Fuel: Diesel and natural gas Load: 6−13 bar
Injection strategy: Direct injection IMEP EGR: 0−31%
Compression ratio: 17:1 Speed: 1100 and 1400 rev/min
Injection pressure: 0.7−2.5 MPa
(differential pressure of diesel over gas)
Gas pulse width variation: 3.50−6.80 ms
Relative injection timing: 3.75−17.85 ms
Injection/cycle: Single and double
87 Single-cylinder
engine
Fuel: Diesel and natural gas Equivalence ratio: 0.05−0.22
Injection strategy: Direct injection Gas injection pressure: 21 and 28 MPa
Compression ratio: 17:1 Intake valve temperature: 41 and 65 °C
Injection pressure: 2.5 MPa
(differential pressure of diesel over gas)
Diesel mass flow: 4.5−22.7 mg/injection
Speed: 800 rev/min
Injection/cycle: Single
40 Light-duty CI
engine
Fuel: Hydrogen and diesel Energy fraction:
Injection strategy: Dual fuel direct injection 20−90% hydrogen energy fraction,
Compression ratio: 17.7:1 80−10% diesel energy fraction
Injection pressure: Injection timing: 180−0° CA BTDC for hydrogen
Hydrogen: 20 MPa, Injection duration:
Diesel: 100 MPa Hydrogen: 2.0−5.5 ms,
Speed: 2000 rev/min Diesel: 0.72−0.39 ms
Injection/cycle: Single
37 RCEM study Fuel: Diesel and natural gas (methane) Pilot injection timing:
Injection strategy: Dual fuel direct injection Early −8.0 to −4.8° ATDC,
Compression ratio: Around 8 Normal −6.0 to −1.7° ATDC,
Injection pressure: Late −4.4 to 0.2° ATDC
Methane: 30 MPa, EGR: 21 and 17.5 O
2
concentration vol %
Diesel: 100 MPa
90 RCEM study Fuel: Diesel and natural gas Pressure at top dead center: 75, 88, 100, and 125 bar
Injection strategy: Dual fuel direct injection Core temperature at top dead center: 780, 820, 865, and 920 K
Injection pressure:
Gas injection pressure: 330 bar,
Diesel injection pressure: 2000 bar
91 Single-cylinder
engine
Fuel: Diesel and compressed natural gas (methane) Engine speed: 1320, 1627, and 1933 rev/min
Injection strategy: Dual fuel direct injection Pilot injection rate: 0.6−18.3 kg/h
Compression ratio: 17:1 Gas injection rate: 17.99, 22.2, and 25.55 kg/h
Injection/cycle: Single Injection timing variation: 5−17° CA BTDC
92 Single-cylinder
compression
machine
Fuel: Hydrogen Ambient temperature variation: 350−700 K
Injection strategy: Premixed hydrogen/air mixture Injection pressure variation: 5−45 bar
Injection/cycle: Single Air/fuel equivalence ratio: 0.4−2.8
93 CVCC study Fuel: Hydrogen and diesel Injection sequence: Pilot−main and main−pilot
Injection strategy: Dual fuel direct injection Injection timing: 0, 1, 2, and 3 ms
Ambient O
2
concentration: 21 vol % Ambient temperature: 780−890 K
Ambient gas density: 23.8 kg/m
3
Injection pressure:
Hydrogen: 20 MPa,
n-Heptane: 70 MPa
94 CVCC study Fuel: Hydrogen Ambient O
2
concentration: 10, 15, and 21 vol %
Injection strategy: Direct injection Ambient core temperature: 600, 650, and 800 K
Ambient gas density: 24 kg/m
3
Injection pressure: 116 bar
95 CVCC study Fuel: n-Heptane and #2 diesel jets Ambient O
2
concentration: 8−21 vol %
Injection strategy: Direct injection
Ambient gas density: 14.8 kg/m
3
Injection pressure: 1540 bar
Ambient gas temperature: 1000 K
Energy & Fuels pubs.acs.org/EF Review
https://doi.org/10.1021/acs.energyfuels.5c02216
Energy Fuels 2025, 39, 16538−16560
16544
Downloaded from pubs.​acs.​org/​enfuem/​article-pdf/​39/​35/​16538/​41340814/​ef5c02216.​pdf by SHANDONG UNIV user on 26 August 2026

<!-- PDF_PAGE: 8 -->

suggested the potential for strategically manipulating hydrogen
injections to balance the power output and engine-out
emissions.
In a dual-fuel DI study by the Lund research group and
Scania,
82
a Scania D13 heavy-duty engine equipped with a high-
pressure DI system from Westport Fuel Systems was
investigated experimentally and computationally. The engine
operated at an IMEP of approximately 16 bar and 1200 rpm. A
pilot diesel injection followed by a main hydrogen injection was
examined at three injection timings�early, intermediate, and
late�with a fixed dwell time. The study also varied the
hydrogen injection pressure to assess its impact on engine
performance. Numerical simulations, performed using the
RANS framework in CONVERGE and validated against
experimental data, provided insights into dual-fuel combustion
dynamics. Injection timing was found to significantly influence
in-cylinder pressure, temperature, engine efficiency, and NO
x
emissions by shifting combustion phasing relative to TDC. Late
injection delayed peak pressure into the expansion stroke,
reducing engine efficiency and NO
x
emissions due to lower
Table 2. continued
Reference
Number
Experimental
Rig Fuel and Other Parameters Parameters Variation
Injection duration: 6.8 ms
42 CVCC study Fuel: Hydrogen and diesel Injection duration:
Injection strategy: Dual fuel direct injection Hydrogen: 3.79, 3.35, 2.68, and 2.03 ms,
Ambient gas density: 23.8 kg/m
3
n-Heptane: 0.68, 1.16, 2.62, 3.77 ms
Injection pressure: Ambient O
2
concentration: 10−21 vol %
Hydrogen: 20 MPa,
n-Heptane: 70 MPa
Ambient core gas temperature: 890 K
96 CVCC study Fuel: Hydrogen and diesel Jet interaction angle: 12−19°
Injection strategy: Dual fuel direct injection Ambient O
2
concentration: 10−21 vol %
Ambient gas density: 23.8 kg/m
3
Injection pressure:
Hydrogen: 20 MPa,
n-Heptane: 70 MPa
Ambient core gas temperature: 890 K
97 CVCC study Fuel: Hydrogen Ignition location: Axial or radial position
Injection strategy: Direct injection Ignition timing: 0.42 and 2.08 ms aSOI
Ambient gas density: 24 kg/m
3
Ambient oxygen concentration: 10−21 vol %
Injection pressure: 116 bar
Ambient core gas temperature: 800 K
98 CVCC study Fuel: Gasoline Laser ignition timing: During injection, after injection, between injection
Injection strategy: Direct injection
Ambient gas density: 6.5 kg/m
3
Injection schedule: Single and double injection
Injection pressure: 100 bar
Ambient gas temperature: 700 K
Ambient O
2
concentration: 21 vol %
99 CVCC study Fuel: Iso-octane and n-heptane Ambient gas temperature: 900 and 735 K
Injection strategy: Direct injection
Ambient gas density: 22.8 kg/m
3
Injection pressure: 70 MPa (both fuels)
Ambient O
2
concentration: 21 vol %
100 CVCC study Fuel: Hydrogen Ambient gas density: 6−33 kg/m
3
Injection strategy: Direct injection Injection pressure: 14−28 MPa
Ambient O
2
concentration: 5−21 vol %
Ambient gas temperature: 970−1400 K
Orifice diameter: 0.24−0.5 mm
101 CVCC study Fuel: Phillips #2 diesel fuel Ambient gas density: 7.3−30 kg/m
3
Injection strategy: Direct injection Injection pressure: 43−184 MPa
Ambient O
2
concentration: 0, 10, and 21 vol %
Ambient gas temperature: 600−1200 K
102 CVCC study Fuel: Hydrogen Injection pressure: 84−140 bar
Injection strategy: Direct injection Ambient gas temperature: 1000−1200 K
Ambient gas density: 24 kg/m
3
Ambient O
2
concentration: 21 vol %
103 CVCC study Fuel: Hydrogen Ambient gas density: 12.5−24 kg/m
3
Injection strategy: Direct injection Injection pressure: 100−200 bar
Ambient O
2
concentration: 0 and 10 vol %
Ambient gas temperature: 1000−1140 K
Orifice diameter: 0.31−0.83 mm
Energy & Fuels pubs.acs.org/EF Review
https://doi.org/10.1021/acs.energyfuels.5c02216
Energy Fuels 2025, 39, 16538−16560
16545
Downloaded from pubs.​acs.​org/​enfuem/​article-pdf/​39/​35/​16538/​41340814/​ef5c02216.​pdf by SHANDONG UNIV user on 26 August 2026

<!-- PDF_PAGE: 9 -->

flame temperatures and peak pressures. The simulations further
complemented experimental findings by analyzing jet-wall
impingement, estimating heat loss contributions from the wall
and exhaust, and evaluating the effects of varying injection
pressures and timings.
It is important to note that the reported engine results and
limitations are specific to the hardware and configurations used
in these studies. For instance, the Lund research group
82
found
through simulations that the stepped-lipped piston profile
influenced hydrogen jet distribution, redirecting varying
proportions into the squish and bowl regions depending on
the test conditions. Similarly, Wang et al.
80
demonstrated that
the presence of a channel complicated fuel−air mixture
distribution and engine optimization effort. While both studies
identified similar general trends, these complexities make it
difficult to isolate the effects of individual parameters. Never-
theless, some general conclusions can be drawn. For example, in
the studies by Liu et al.,
40,78
the injectors had a hydrogen
pressure rating of 200 bar, which constrained the injection rate
and the total fuel mass that could be delivered between SOI and
TDC. As a result, for late injection timings, fuel injection
extended into the expansion stroke to meet the required fuel
mass. Increasing the injector pressure rating could help alleviate
challenges associated with lower mass flow rate, however, other
challenges that may arise, such as peak pressure limit, must be
considered.
77
Experience with conventional diesel engine combustion has
shown that combining advanced experimental measurements
with computational modeling in controlled, well-characterized
environments is effective in providing targeted assessments,
addressing the limitations of engine studies.
60
Recent examples
of high-fidelity experimental data and complementary numerical
modeling studies (e.g., ref 83 and 84) are detailed in subsequent
sections.
3. DUAL-FUEL DIRECT-INJECTION ENGINE
PARAMETERS
Previous studies have explored various methods for dual-fuel
delivery.
85
One approach involves coinjecting fuels through
shared channels within a single injector, resulting in a diesel−gas
mixture entering the combustion chamber.
86,87
Another method
utilizes a single injector with separate channels for independent
fuel delivery.
77,88,89
A third approach employs two separate
injectors, each dedicated to a specific fuel.
40,79
With previous
diesel−natural gas coinjection investigations reporting increased
pilot ignition delay compared to pure diesel injection and
knocking issues,
86,87
this review focuses on separate fuel delivery
methods. Dual-fuel DI studies have also examined the effects of
various injector parameters on mixture formation and
subsequent combustion processes. Although some parameters
are more specific to dual-injector systems, the findings have
broad applicability. These parameters include:
• Injection timing, the relative SOI timings between the pilot
and main fuels.
• Energy share, the energy substitution ratio of the main fuel
relative to the total energy output.
• Jet interaction angle, the relative angle between pilot and
main jets during the mixing and combustion process.
This review primarily focuses on parameters that are unique to
dual-fuel combustion, as this allows for a more targeted
contribution to the field. It is noted that many other factors,
such as ambient conditions, injection pressure, and nozzle orifice
geometry, have been extensively studied in the context of single-
fuel injection and still influence dual-fuel processes. Therefore,
while this is not the primary focus, relevant discussions on their
impact within the dual-fuel DI context are also provided.
While this review focuses on hydrogen−diesel DI systems,
relevant findings from natural gas−diesel DI studies are also
referenced. These studies, which examine the interaction
between gaseous fuel and liquid pilot jets, provide insights
into the general behavior of intersecting jets.
Table 2 presents a summary of the fundamental experimental
studies discussed in Section 3.
3.1. Injection Timing. Varying fuel injection timing and
sequence, particularly in conjunction with a converging injection
configuration, enables control over the combustion mode,
facilitating a shift between premixed and mixing-controlled
combustion.
37,90,104
In PFI systems, the gaseous fuel is
introduced externally to the combustion chamber, entering
with the intake air as a premixed charge well before pilot SOI.
This inherently restricts PFI to a primarily premixed combustion
mode at ignition.
82
In contrast, dual-fuel DI offers greater
flexibility, allowing pilot SOI both before and after gaseous fuel
SOI. This, combined with variation in dwell time, directly
impacts the state of the fuel−air mixture at ignition and,
consequently, the associated combustion process.
Previous studies on natural gas−diesel engines have shown
that the fuel injection sequence significantly affects the
combustion stability, peak heat release rate, and combustion
noise. Many dual-fuel engines using early gas−fuel injection
strategies achieve stable combustion by forming a homogeneous
or moderately stratified mixture, which is ignited by a pilot fuel
injected near TDC. In these cases, premixed combustion and
flame propagation dominate,
65,77,91,105
reportedly capable of
delivering high efficiency and low pilot-fuel consumption.
However, the prolonged in-cylinder residence time of the gas
fuel before ignition increases preignition risk, particularly under
the high compression ratios typical of compression-ignition
engines.
105
As discussed earlier, late high-pressure main-fuel injection
provides a more controlled alternative for dual-fuel applications.
In this approach, both the main and pilot fuels are injected near
TDC, with combustion primarily governed by mixing-controlled
processes.
79
This strategy reduces combustion noise and peak
heat release rate by igniting the main fuel shortly after injection,
thereby limiting premixing before ignition,
36,37,105
and also the
risk of preignition.
Fundamental insights into dual-fuel injection processes have
been obtained from previous studies conducted under
controlled conditions. Notable investigations include optical
studies by Fink et al.
90,104
using a rapid compression expansion
machine (RCEM).
92,106
The RCEM is a large-bore system with
an optically accessible piston, pneumatically driven to compress
an air charge to high-temperature and high-pressure conditions.
The temperature and pressure at TDC can be adjusted by
modifying the compression ratio and initial charge pressure.
104
Unlike conventional engines, the RCEM lacks the intake
turbulence typically generated during operation due to its slow
charge-filling process. This results in a more stable ambient
condition at TDC, even with rapid compression.
106
In the
RCEM studies of Fink et al.,
90,104
the diesel injector was
positioned perpendicular to the gas injector. The diesel jet exited
parallel to the injector axis, while the gas jet was discharged from
a separate injector nozzle orifice offset from its injector axis,
ensuring interaction at a similar plane. This configuration
Energy & Fuels pubs.acs.org/EF Review
https://doi.org/10.1021/acs.energyfuels.5c02216
Energy Fuels 2025, 39, 16538−16560
16546
Downloaded from pubs.​acs.​org/​enfuem/​article-pdf/​39/​35/​16538/​41340814/​ef5c02216.​pdf by SHANDONG UNIV user on 26 August 2026

<!-- PDF_PAGE: 10 -->

allowed for adjustment of the jet interaction angle by rotating
the gas injector to be either directed toward (converging) or
away (diverging) from the pilot diesel.
The studies by Fink et al.
90
demonstrated that injection
timing affects combustion behavior across all jet interaction
angles, with a stronger influence in converging configurations. At
an ambient temperature of 920 K, injecting gas fuel first in a
converging setup promoted premixed combustion, leading to
higher heat release rates, whereas injecting diesel first resulted in
mixing-controlled combustion. Consistent with the findings of
Fink et al.,
104
Ishibashi and Tsuru
37
reported a similar trend in
the ignition of an actively injecting gas jet. Their study on natural
gas−diesel combustion in an RCEM with a fixed converging
configuration showed that while maintaining a fixed gas
injection timing, varying the diesel injection timing (before,
during, or after gas injection) significantly influenced
combustion and heat release rates. Diesel injection before or
simultaneously with gas promoted mixing-controlled combus-
tion, whereas injection after gas facilitated better premixing,
leading to higher heat release rates.
Recent dual-fuel DI studies involving hydrogen and diesel
have shown similar trends. Rorimpandey et al.
93
conducted an
optical investigation on the effects of injection sequence and
timing on the combustion characteristics of intersecting
hydrogen−diesel jets. Using high-speed schlieren imaging and
pressure-trace measurements, the study was performed in a
constant-volume combustion chamber (CVCC) with two
injectors converging at a 12° angle. Hydrogen and n-heptane
(a diesel surrogate) were used as the fuels. A DI injector similar
to that in Liu et al.’s engine studies
40,78
was used, but with a 0.58
mm nozzle cap to ensure jet and combustion processes remained
within the optically accessible region. A schematic diagram of
the CVCC and dual-injector layout is shown in Figure 2.
The study found that at 890 K ambient temperature and 21
vol % oxygen, injecting diesel before hydrogen (pilot−main
strategy) led to predominantly mixing-controlled combustion.
Under these conditions, the pilot fuel ignited outside the
hydrogen jet before the jet interaction. Hydrogen ignition
occurred after mixing with pilot combustion products, with the
reaction front propagating from the interaction zone toward the
jet tip and stabilizing near the hydrogen nozzle.
To understand the hydrogen jet flame recession and
stabilization behavior, a parametric study on hydrogen jet
combustion recession under engine-relevant CVCC condi-
tions
94
showed that even below hydrogen’s autoignition
threshold, forced laser-induced ignition caused upstream
recession of the hydrogen jet’s reaction zone. These
experimental findings, supported by simplified calculations,
suggest that edge-flame deflagration into stratified premixed
fuel−ambient streams explains the observed lift-off character-
istic.
The short lift-off characteristic of the hydrogen jet was also
observed in a high-pressure dual-fuel combustion study on
hydrogen use in an optical engine, as reported by ref 107. In this
study, hydrogen was directly injected and ignited by a small
amount of pilot diesel using a dual-fuel injector from Woodward
L’Orange. The centrally mounted injector featured nine holes
for each fuel type and allowed for independent injection of both
fuels. The experiments tested hydrogen injection pressures of
300 and 500 bar, while diesel was injected at 1000 and 1200 bar.
The independent control of the two fuels enabled different
combustion modes. A computational model was developed
using the commercial software CONVERGE and validated
against experimental data for high-pressure direct-injected
hydrogen. The results showed that hydrogen could be used in
the engine without modifications, exhibiting stable combustion.
Hydrogen was found to burn in non-premixed mode, igniting
immediately upon injection into the chamber. Both exper-
imental and numerical results indicated that the hydrogen flame
remained close to the injector due to its wide flammability limits
and high laminar flame speed. Despite the hydrogen jet entering
at supersonic speeds, the study hypothesized that the flame
could still propagate upstream along the thin shear layer
between the jet and surrounding air, resulting in the observed
short lift-off distance.
The findings of ref 93 showed that dwell time influenced the
preignition jet−jet interaction duration. Longer dwell times
required extended interaction periods for successful hydrogen
ignition, as the pilot combustion products had more time to cool
and lean out before they interacting with the hydrogen jet. The
study also observed increased combustion variability under
lower-temperature, less reactive conditions, which was attrib-
uted to the leaning out of the pilot fuel.
When hydrogen was injected before the pilot diesel (main−
pilot strategy), increasing the dwell time prolonged the interval
between the hydrogen SOI and ignition. This extended interval
allowed more hydrogen to be injected, increasing the peak heat
release rate at ignition.
93
However, when the dwell time was long
enough for hydrogen ignition to occur after injection had ceased,
the study reported slower combustion propagation, lower heat
release rate magnitudes, larger unburned regions within the gas
jet, and increased cyclic variability in the heat release rate. These
Figure 2. Schematic of (a) the optically accessible chamber and (b) the
converging injector configuration used in the studies of Rorimpandey et
al.
96
Reproduced from ref 96. Available under a Creative Commons
CC-BY license. Copyright 2024 Rorimpandey et al.
Energy & Fuels pubs.acs.org/EF Review
https://doi.org/10.1021/acs.energyfuels.5c02216
Energy Fuels 2025, 39, 16538−16560
16547
Downloaded from pubs.​acs.​org/​enfuem/​article-pdf/​39/​35/​16538/​41340814/​ef5c02216.​pdf by SHANDONG UNIV user on 26 August 2026

<!-- PDF_PAGE: 11 -->

instabilities were linked to interactions between the pilot jet and
lean regions of the overly mixed hydrogen jet.
93
Similar trends
were previously observed in natural gas−diesel combustion
studies.
104
Lucchini et al.
83
simulated cases from ref 93 using an Eulerian
Monte Carlo Field (EMCF) transported Probability Density
Function (PDF) combustion model coupled with a Flamelet
Generated Manifold (FGM) approach. This model was used to
predict heat release rates and flame structures for various
injection strategies. For pilot−main injection, the EMCF+FGM
model accurately reproduced the experimentally observed flame
structures and heat release rates, capturing the diffusion-driven
ignition of the hydrogen jet by the pilot fuel and the resulting
pure hydrogen diffusion flame structure. However, simulating
main−pilot injection was more challenging due to the complex
interaction of diffusion, partially premixed, and fully diffusive
combustion regimes. While the model struggled with extreme
injection timings�where hydrogen ignition occurred after
injection ended�it still predicted a greater prevalence of
partially premixed combustion, influencing the heat release rate
profile and accelerating combustion, which aligned with
experimental observations, showing a reduced combustion
duration with an increased dwell time.
93
Additionally, the
simulations predicted greater ignition variability for extreme
injection timings, suggesting the model’s potential in predicting
combustion instability.
The model produced promising results despite not account-
ing for the chemical interactions between the two fuels. This is
likely due to the experimental setup and injector configurations
used in the selected study,
93
where the pilot fuel ignited before
interacting with the hydrogen jet, as observed experimentally.
However, in configurations that promote stronger interaction
between both jets�such as those involving pilot fuel injection
into an ambient premixed fuel−air mixture or cases with more
extensive overlapping of jets before pilot fuel ignition (see
Section 3.3)�chemical effects may need to be considered. For
example, Gu
108
performed direct numerical simulations of n-
dodecane (a diesel surrogate) injecting into a premixed
hydrogen−air mixture under engine-relevant conditions. The
study found that pilot fuel ignition was delayed in the presence
of premixed hydrogen−air compared to cases without, as
hydrogen consumes OH species during the low-temperature
oxidation of n-dodecane. Similar effects have been reported in
other dual-fuel combustion studies using methane,
109
meth-
anol,
110
and ammonia
111
as primary fuels.
3.2. Energy Share. A key advantage of dual-fuel DI is the
ability to control combustion by adjusting injection timing,
sequence (as discussed in Section 3.1), and individual fuel
injection durations,
40
allowing precise regulation of each fuel’s
energy contribution (i.e., energy share). While maximizing the
hydrogen energy share is often a priority for reducing carbon
emissions, the flexibility to adjust this share based on fuel
availability or local emission regulations enhances operational
adaptability. Therefore, understanding how changes in the
injection duration influence fuel jet interactions and combustion
processes is essential.
The impact of injection duration on diesel jet flow and
combustion dynamics, including ignition mechanisms,
112
soot
processes,
95
and postinjection ambient entrainment,
113
is well
established for single-jet cases but less explored for dual-fuel DI.
Rorimpandey et al.
42
investigated how the relative durations of
pilot and main fuel injections influence hydrogen and diesel
combustion in an optically accessible chamber. Using the same
CVCC and converging injector setup described in Section 3.1,
93
they adjusted the injection durations of simultaneously injected
hydrogen and n-heptane to achieve hydrogen energy shares
ranging from 10% to 90%, while maintaining a constant total
energy output of 624 J under varying ambient oxygen
concentrations (10−21 vol %).
The study showed that the interaction between pilot- and
main-fuel jets in the dual-fuel cases can produce flow and
combustion patterns not observed for single-fuel (pilot-only)
cases under the same conditions.
42
To illustrate this point,
Figure 3, which presents schlieren imaging data from a dual-fuel
case with 60% hydrogen energy share, reveals an outward bulge
at the upper periphery of the pilot jet after jet interaction.This
region initially brightened and then diminished as it moved
downstream, displaying counter-rotating motion. The authors
of the study suggested that these interactions locally modify
mixture composition, temperature, and strain, creating regions
temporarily conducive to soot processes before further
interactions between vortical structures and flames occur. In
the paper, jet interactions also affected soot processes.
42
While
soot luminosity initially appeared at similar locations and times
in both dual-fuel and pilot-only cases (because pilot fuel
autoignited before interacting with hydrogen), later differences
emerged. The dual-fuel soot region appeared less uniformly
distributed across the jet head, and longer pilot fuel injections
appeared to extend the soot luminous region further toward the
hydrogen jet tip, exceeding the axial length observed in pilot-
only cases (Figure 4). The results of the study also showed that
when the injection duration of the pilot injection lasted longer
than hydrogen injection, the soot region returned to a length
comparable to the pilot-only case. Although further validation is
Figure 3. Sample schlieren images highlighting the “roll-up”
phenomenon observed with the dual-fuel direct injection configuration
in the region below the cyan-colored arc. (Top) Single-shot image from
a dual-fuel case; (bottom) time-averaged image. In the single-shot
image, the boundaries of the pilot fuel jet (red) and the high-
temperature zone (green) are highlighted. In the averaged image, the
red and yellow arrows indicate the upward movement of the pilot fuel
jet and the counter-rotating motion of the “roll-up” zone, respectively.
The selected dual-fuel case features a 40% hydrogen energy share with
the remaining energy from the pilot fuel. Ambient conditions: 21 vol %
oxygen concentration, 890 K. Reproduced from ref 42. Available under
a Creative Commons CC-BY license. Copyright 2024 Rorimpandey et
al.
Energy & Fuels pubs.acs.org/EF Review
https://doi.org/10.1021/acs.energyfuels.5c02216
Energy Fuels 2025, 39, 16538−16560
16548
Downloaded from pubs.​acs.​org/​enfuem/​article-pdf/​39/​35/​16538/​41340814/​ef5c02216.​pdf by SHANDONG UNIV user on 26 August 2026

<!-- PDF_PAGE: 12 -->

needed, the presence of luminous vortic structures and
variations in soot region length did not necessarily indicate
increased soot emissions, as concurrent photodiode measure-
ments showed slightly lower luminosity in dual-fuel cases than
the single-fuel reference cases.
The study also observed that the pilot jet combustion
products can be entrained into the main hydrogen jet upstream
of the intersection zone (Figure 5), attributed to the jets’
momentum difference.
42
The effect was the most pronounced
when the pilot injection was short and the main injection was
long (high hydrogen energy share). As the lower-momentum
pilot jet ceased injecting, it was drawn into the still-injecting,
higher-momentum hydrogen jet, affecting flame stabilization
and heat release. As noted in Section 3.1, pilot fuel autoignition
initiated outside the hydrogen jet boundary, with the reaction
zone propagating toward the jet tip before stabilizing upstream.
The entrainment of pilot combustion products into the
upstream region, which has not yet undergone high-temperature
ignition, can accelerate flame stabilization and modify the heat
release profile, increasing the premixed burn peak or the heat
release rate during the mixing-controlled phase.
96
Despite the limited literature on this topic, initial findings
already highlight the significant impact of the relative injection
duration on dual-fuel combustion characteristics. The inter-
action between the pilot and main fuel jets influences heat
release, soot processes, and combustion stability. A more
detailed understanding of relative injection durations�beyond
the common assumption that they simply adjust the energy
share between fuels�is essential for optimizing the perform-
ance of dual-fuel DI systems.
3.3. Jet Interaction Angle. Dual-fuel DI systems can use
separate injectors for each fuel
40,78
or a single injector capable of
handling both.
77,88,89
The injector configuration, particularly the
orientation of the fuel jets relative to each other, significantly
influences the jet interaction. This orientation can be broadly
classified as diverging (jet axes directed away from each other),
parallel (jet axes aligned), or converging (jet axes intersect
downstream), as Figure 6 shows.
The impact of jet interaction angles on combustion dynamics
was investigated by Fink et al.
90,104
using an optical natural gas−
diesel setup within a RCEM. As outlined in Section 3.1, this
RCEM setup includes a rotatable gas injector, enabling variation
in jet interaction angles. Their findings indicate that a diverging
Figure 4. Sample high-speed schlieren images of a dual-fuel case (top)
and the corresponding pilot-fuel (n-heptane) only case (bottom) at the
same time instant after the start of injection, showing the extent of axial
soot within the hydrogen jet exceeding that observed with pilot fuel
alone. Highlighted boundaries include pilot fuel (red), high-temper-
ature zone (green), and an averaged single-fuel pilot-fuel-only jet
boundary (yellow, overlaid on the dual-fuel image for comparison). The
selected dual-fuel case features a 60% hydrogen energy share, with the
remaining energy from the pilot fuel. Ambient conditions: 21 vol %
oxygen concentration, 890 K. Reproduced from ref 42. Available under
a Creative Commons CC-BY license. Copyright 2024 Rorimpandey et
al.
Figure 5. Ensemble-averaged high-speed schlieren images comparing
the dual-fuel (left) and single-fuel (right) cases, at identical time
instants (indicated bottom left) and ambient conditions. Red outlines
on the dual-fuel frames show corresponding single-fuel jet trajectories.
Yellow arrows highlight radial shifts in the pilot fuel trajectory after
injection ceased. The dual-fuel case features a 90% hydrogen energy
share, with pilot fuel contributing the rest. Reproduced from ref 42.
Available under a Creative Commons CC-BY license. Copyright 2024
Rorimpandey et al.
Figure 6. Schematic diagrams depicting (a) diverging, (b) parallel, and
(c) converging jet configurations. In each, the gas jet (blue) and diesel
jet (red) are shown, with their axes marked by corresponding dashed
lines. Reproduced from ref 17. Available under a Creative Commons
CC-BY license. Copyright 2019 Yip et al.
Energy & Fuels pubs.acs.org/EF Review
https://doi.org/10.1021/acs.energyfuels.5c02216
Energy Fuels 2025, 39, 16538−16560
16549
Downloaded from pubs.​acs.​org/​enfuem/​article-pdf/​39/​35/​16538/​41340814/​ef5c02216.​pdf by SHANDONG UNIV user on 26 August 2026

<!-- PDF_PAGE: 13 -->

injector configuration facilitates natural gas−air premixing by
allowing pilot diesel to autoignite without a direct jet interaction.
This configuration enhances premixing and, in some cases, leads
to a jet−wall interaction and redirection of the gaseous fuel
before interacting with diesel combustion products and igniting,
resulting in premixed combustion. However, at small diverging
angles, jet interaction remains possible if the spreading angles of
the jets overlap.
104,114
From a robustness perspective, a
converging injector configuration, where jet axes intersect,
may provide more reliable ignition by promoting a direct jet
interaction. This approach still allows for adjustments in
injection timing and dwell periods (see Section 3.1) to control
the combustion mode. However, if not optimized, excessive jet
interaction�induced by convergence angle, injection settings,
and ambient conditions (discussed in Section 3.4)�may delay
or even quench the pilot fuel’s autoignition.
90,104
Previous studies
90,115
reported that misfire likelihood can be
evaluated by comparing the pilot flame lift-off length with the
maximum penetration distance of the diesel jet before it
intersects with the natural gas jet. Due to the converging jet
configuration, the natural gas jet intersected with the pilot diesel
jet, shifting the ignition location downstream and increasing
ignition delay. While a more convergent jet arrangement slightly
increased lift-off length, it also reduced the diesel jet’s maximum
penetration distance before intersection. The study observed
that ignition was inhibited when the diesel jet’s free penetration
distance became shorter than the lift-off length. The authors
proposed maintaining a longer free diesel penetration distance
than the lift-off length as a criterion for stable pilot ignition.
Numerical analyses were conducted to better understand
misfiring events
115
of ref 90. The results suggested that the
overlap between the gaseous and diesel jets could lead to an
insufficient temperature rise, preventing the dissociation of
hydrogen peroxide radicals, which are essential for the second
stage of diesel ignition.
116
This, in turn, delays or inhibits
ignition.
Assuming a converging jet configuration yields optimal
ignition performance, Rorimpandey et al.
96
conducted an
optical study examining this configuration, where hydrogen
and pilot diesel jets were directed toward each other. This study
investigated the impact of varying converging jet interaction
angles (12°, 15°, and 19°) on hydrogen−diesel free-jet
combustion at an ambient temperature of 830 K and varying
oxygen concentrations. Utilizing simultaneous main and pilot
injections, the study examined the effect of jet interaction angle
on pilot fuel ignition characteristics under different interaction
angles and ambient conditions, comparing results to pilot-fuel-
only references. The study reported that hydrogen−pilot jet
interaction influenced pilot ignition, but pilot jet quenching was
not observed. Pilot ignition delay was either advanced or delayed
depending on whether pilot jet ignition occurred before or after
interacting with the hydrogen jet. More converged config-
urations, promoting more immediate and extensive preignition
jet interaction, resulted in increased pilot jet ignition delays
compared to pilot-only references under the same ambient
conditions. However, these configurations also facilitated a more
rapid transition of the reaction front from the pilot jet to the
main jet. This was attributed to the more extensive jet
interaction, which enabled more readily flame propagation
after pilot jet ignition. It is noteworthy that the study only
observed absolute changes in ignition delay and reaction front
transition times in the order of 0.5 ms, suggesting the robustness
of the dual-fuel approach with hydrogen, at least for the tested
configuration. Further tests with more extensive interactions
between the jets are required to establish the trend.
While the study by Rorimpandey et al.
96
revealed various
aspects of jet−jet interactions on ignition and combustion under
engine-relevant conditions, their findings were influenced by
variations in pilot fuel ignition characteristics due to parametric
changes. From a practical perspective, the wider dispersion of
pilot fuel in the cylinder enhances ignition robustness. However,
this introduces challenges in research, where greater control over
ignition location and timing is needed to systematically study
hydrogen ignition, mixing, and flame propagation.
To address this, a forced laser-induced ignition technique was
employed,
97
following methods previously applied in diesel
117
and gasoline
98,99
studies. Figure 7 shows a schematic diagram of
the high-pressure combustion vessel and optical arrangement for
simultaneous high-speed schlieren imaging and the laser ignition
setup used for the hydrogen jet forced ignition study. The
approach enabled precise ignition of directly injected hydrogen
jets under engine-relevant conditions (baseline conditions: 800
K ambient temperature, 45 bar ambient pressure, 15 vol %
oxygen concentration, and 24 kg/m
3
ambient density). Ignition
was initiated at different axial positions along the injector axis
(jet tail, midjet, and jet head) and at radial locations offset from
the centerline (see Figure 8).
The results showed that, as in pilot-fuel ignition studies, a
combustion kernel formed shortly after laser-induced ignition
and propagated downstream, engulfing the jet while also
traveling upstream toward the nozzle. The speed of upstream
flame propagation depended on ignition location. Downstream
or peripheral ignition led to a flame that did not recess to the
same lift-off distance from the nozzle as cases with ignition closer
to the nozzle, even during long injection durations. From an
engine application perspective, as a further downstream lift-off
could increase unburned fuel emissions and reduce combustion
efficiency.
The ignition location also influenced heat release profiles.
Ignition near the jet tip or periphery resulted in a lower peak heat
release followed by a prolonged decay to a quasi-steady state,
compared to ignition at the midjet or jet tail. The lower peak
heat release was attributed to the smaller amount of readily
ignitable fuel−air mixture available downstream, while the
prolonged decay resulted from the extended time required for
the flame to propagate back to the nozzle.
Figure 7. Schematic diagram of the high-pressure combustion vessel
and optical setup for simultaneous high-speed schlieren imaging and
laser ignition of a hydrogen jet. Reproduced from ref 97. Available
under a Creative Commons CC-BY license. Copyright 2024 Yip et al.
Energy & Fuels pubs.acs.org/EF Review
https://doi.org/10.1021/acs.energyfuels.5c02216
Energy Fuels 2025, 39, 16538−16560
16550
Downloaded from pubs.​acs.​org/​enfuem/​article-pdf/​39/​35/​16538/​41340814/​ef5c02216.​pdf by SHANDONG UNIV user on 26 August 2026

<!-- PDF_PAGE: 14 -->

3.4. Diluted Conditions. Concerns over NO
x
emissions in
hydrogen-fueled engines
50,100
have driven interest in dilution
strategies such as EGR. EGR increases the mixture’s heat
capacity by reintroducing exhaust gases, lowering combustion
temperatures and reducing NO
x
emissions.
100,118,119
Widely
used in diesel engines, EGR has been shown to enable soot-free
combustion under specific injection conditions.
95
However, the
reduced oxygen levels associated with EGR can also affect
ignition and overall combustion behavior.
The study by Fink et al.,
90
which utilized an RCEM test rig to
investigate natural gas−diesel dual-fuel ignition and combustion
processes (as introduced in Section 3.1), found that at a lower
ambient temperature of 780 K, misfire occurred across all
converging angles when the gas fuel was injected first. This was
attributed to the failure of the entrained diesel jet to ignite.
90,104
Under the same low-temperature converging conditions,
injecting the main fuel before the pilot fuel led to a decrease
in heat release magnitude and increased cyclic variability,
particularly when the SOI of the pilot jet coincided with or
followed the end of gas injection. The study attributed the
finding to an extended premixing period, which resulted in
overly lean mixtures.
104
In the study by Rorimpandey et al.,
93
which examined the
impact of injection timing and sequence on hydrogen−diesel
dual-fuel ignition and combustion processes (as introduced in
Section 3.1), the authors also investigated the effects of varying
ambient temperature while also investigating the influence of
ambient temperature under constant injection conditions. The
study found that at lower ambient temperatures, the interaction
between the pilot fuel and hydrogen jets was more pronounced
before pilot fuel autoignition. However, ignition delay analysis
showed no statistically significant difference in pilot-fuel ignition
timing compared to pilot-only cases under the same conditions,
suggesting that increased jet interaction did not affect pilot
ignition timing under the tested configuration.
In terms of heat release, the study observed that lower
ambient temperatures extended the ignition delay of the main
fuel, allowing for a longer injection/residence time of the
hydrogen jet before ignition and resulting in a higher peak heat
release rate. Additionally, the mixing-controlled combustion
phase appeared less defined at lower temperatures. The authors
attributed this to increased variability in pilot jet ignition
location under reduced temperature conditions, which
influenced the premixed-burn transient until near the end of
injection.
In another study by Rorimpandey et al.,
42
the effects of
varying relative energy share on hydrogen−diesel dual-fuel
ignition and combustion were investigated (as discussed in
Section 3.2), along with the influence of oxygen concentrations
ranging from 21% to 10% by volume. The experiments
consistently showed that the pilot fuel autoignited outside the
hydrogen jet boundary under all tested conditions. Pilot ignition
delay remained unchanged compared to pilot-only reference
cases under the same ambient conditions.
Hydrogen ignition occurred after interacting with the
combustion products of the pilot fuel, with this interaction
period increasing as oxygen concentrations decreased. Lower
oxygen levels also caused the flame stabilization location to shift
farther from the nozzle. At 10% oxygen, this location became
more variable, though in some instances, the hydrogen flame still
stabilized closer to the nozzle. The findings from the study
suggested that the interactions between the hydrogen jet and
pilot combustion products near the nozzle may have contributed
to these variations in lift-off distance.
Normalized heat release was consistently higher in dual-fuel
cases compared to single-fuel references. At 21% oxygen, dual-
fuel cases exhibited values between 91% and 97%, while single-
Figure 8. Schlieren sequences showing laser-induced forced ignition of hydrogen jets at varying axial distances from the nozzle centerline: (a) baseline
(15 mm), (b) 30 mm (x), (c) 70 mm (x), simulating tail, midjet, and head-jet ignition, respectively. Peripheral head-jet ignition (i.e., 70 mm from
nozzle, 10 mm offset from centerline) was also tested: (d) 70 mm (x)/10 mm (y). Time after start of injection (aSOI) is displayed in the top-left corner
of each image. Blue and orange contours indicate unreacted and reacted hydrogen−air mixtures, respectively. These schlieren images were used to
analyze flame propagation and stabilization trends across different ignition locations. Reproduced from ref 97. Available under a Creative Commons
CC-BY license. Copyright 2024 Yip et al.
Energy & Fuels pubs.acs.org/EF Review
https://doi.org/10.1021/acs.energyfuels.5c02216
Energy Fuels 2025, 39, 16538−16560
16551
Downloaded from pubs.​acs.​org/​enfuem/​article-pdf/​39/​35/​16538/​41340814/​ef5c02216.​pdf by SHANDONG UNIV user on 26 August 2026

<!-- PDF_PAGE: 15 -->

fuel cases ranged from 70% to 79%. The lower efficiency in
single-fuel cases was attributed to suboptimal pilot fuel injection
settings, which were primarily selected to generate small,
repeatable injection amounts for ignition assistance. The higher
heat release in dual-fuel cases suggested more complete
combustion, likely due to hydrogen’s favorable combustion
properties, including its high dispersion rate, effective fuel−air
mixing, wide flammability limits, high flame speed, and lean
operation capability.
17
Dual-fuel cases maintained high
normalized heat release across practical oxygen levels, ranging
from 91%−97% at 21% oxygen and 88%−98% at 15% oxygen.
As discussed in Section 3.2, the interaction between the pilot
and hydrogen jets influenced flow and combustion dynamics,
affecting soot processes.
42
Qualitative flame luminosity
measurements indicated lower luminosity in dual-fuel cases,
suggesting reduced soot concentration compared to single-fuel
references. This reduction was more pronounced at lower
oxygen levels (see Figure 9), aligning with previous diesel
studies on the impact of increased dilution on soot formation.
101
In a study by Rorimpandey et al.,
96
the effects of jet interaction
angles on hydrogen−diesel dual-fuel ignition and combustion
were investigated (as introduced in Section 3.3), alongside the
influence of ambient oxygen concentrations ranging from 21 to
10 vol %. The study found that, under dual-fuel conditions with a
fixed jet interaction angle, pilot ignition delay slightly increased
at lower oxygen levels compared to single-fuel cases. This was
attributed to prolonged interactions between the hydrogen and
diesel jets before ignition, driven by reduced oxygen availability.
Additionally, the transition time of the reaction front from the
pilot to the main jet lengthened as the oxygen concentration
decreased. While lower oxygen levels enhanced preignition
interactions, which would favor reaction front transfer�they
also limited available oxygen for combustion, slowing the
transition from pilot to main ignition.
As discussed in Section 3.2, pilot jet ignition characteristics are
sensitive to ambient conditions, complicating the analysis of
hydrogen jet mixing and combustion. To address this, Yip et al.
94
(introduced in Section 3.1) also conducted a study using laser
ignition fixed at the midjet position of a quasi-steady hydrogen
jet. The study varied ambient temperature (600−800 K) and
oxygen concentration (10−21 vol %), with experiments
conducted below hydrogen’s autoignition temperature thresh-
old. Despite these lower temperatures compared to dual-fuel
studies,
42,93,96
similar flame recession behavior was observed,
suggesting autoignition was not the primary cause. Premixed
flame deflagration analyses were performed to investigate flame
recession and stabilization under different ambient conditions.
The results showed that flame lift-off length increased in less
reactive environments, such as at lower temperatures or reduced
oxygen concentrations.
94
Simplified numerical simulations
indicated that flame deflagration and its sensitivity to ambient
conditions explained the observed flame recession and
stabilization. Reduced flame speeds at lower temperatures and
oxygen concentrations accounted for slower flame recession
rates and more downstream stabilization. Simulations further
suggested that under low oxygen conditions regions where
turbulent flame speeds exceeded jet slipstream velocities were
confined to narrow, fuel−lean zones near the jet periphery. In
these regions, flame recession was highly sensitive to flame speed
and mixture fraction with turbulence−chemistry interactions
playing a dominant role. Notably, the flame base remained stable
in the laser ignition study, unlike the fluctuations observed in
dual-fuel experiments under low oxygen conditions.
42
This
supports the assertion that entrainment of pilot jet combustion
products into the hydrogen jet upstream region (Section 3.3)�
absent in the laser ignition setup�contributes to the observed
fluctuations.
From an engine design perspective, understanding flame
stabilization under varying operating conditions is crucial for
engine design, as it impacts emissions, fuel efficiency, and
component longevity. For example, while fluctuations were
observed, particularly at the lowest tested oxygen level
(representing an impractically high EGR level), the increased
flame standoff distance at lower oxygen concentrations could
help prevent high-temperature flames from reaching the injector
nozzle, improving long-term durability.
107
This strategy may
also aid in mitigating the NO
x
emissions in hydrogen engines.
3.5. Other Injection Parameters. The widespread
adoption of common-rail systems in diesel engines has enabled
significant increases in injection pressure, resulting in improved
power output, thermal efficiency, smoke reduction, and
enhanced NO
x
-particulate matter trade-offs. These improve-
ments are largely attributed to enhanced spray characteristics
under high pressure, including increased spray velocity, greater
penetration, narrower spray angles, and improved atomization.
Efforts are also underway to evaluate whether similar benefits
can be achieved in DI gas engines through elevated gas injection
Figure 9. Photodiode measurements from a constant-volume
combustion chamber showed lower luminosity for dual-fuel (60%
hydrogen energy share) than single-fuel (diesel only) cases, across
ambient oxygen levels of 21%, 15%, and 10%. Reproduced from ref 42.
Available under a Creative Commons CC-BY license. Copyright 2024
Rorimpandey et al.
Energy & Fuels pubs.acs.org/EF Review
https://doi.org/10.1021/acs.energyfuels.5c02216
Energy Fuels 2025, 39, 16538−16560
16552
Downloaded from pubs.​acs.​org/​enfuem/​article-pdf/​39/​35/​16538/​41340814/​ef5c02216.​pdf by SHANDONG UNIV user on 26 August 2026

<!-- PDF_PAGE: 16 -->

pressures, given the differences in spray formation between
gaseous and liquid fuels.
A notable investigation by Westport Innovations Inc.
77
examined the impact of increasing natural gas injection pressure
from 300 to 600 bar in a pilot-ignited DI natural gas engine,
using both experimental and numerical methods. The study also
considered reducing the injector nozzle diameter to preserve the
velocity benefits of higher rail pressure while mitigating
excessive fueling. Engine performance was evaluated across
three scenarios: fixed combustion phasing with constant torque
and EGR, constant NO
x
emissions via adjusted combustion
phasing and EGR and increased torque output with fixed air and
EGR.
The findings from the study
77
demonstrated that a doubling
of injection pressure could yield up to a 7% improvement in
efficiency, a 20% increase in power, or a 90% reduction in
engine-out particulate matter at peak load. However, these
benefits were predominantly observed under full-load con-
ditions. Below 75% load, the advantages diminished due to
already sufficient injection pressure ratios. A key drawback of
higher injection pressures was increased combustion harshness,
characterized by higher heat release rates, louder operation, and
elevated NO
x
emissions. These effects could be mitigated by
reducing the nozzle diameter or increasing EGR to maintain
NO
x
levels while advancing combustion phasing for higher
efficiency without exceeding peak cylinder pressure limits.
Numerical simulations from their study
77
suggested that the
increased combustion rate was mainly due to higher mass
injection rates. While the gas jet mixture distribution remained
relatively consistent during injection, the higher postinjection jet
kinetic energy improved air entrainment and mixing. This
resulted in leaner mixtures, improved fuel conversion efficiency,
and enhanced particulate oxidation. However, increased
cylinder temperatures also led to higher heat transfer losses,
particularly to the piston and cylinder head, due to a greater
impingement area and surface exposure. These losses were
partially offset by reduced heat transfer during the remainder of
the power stroke.
A similar assessment is warranted to determine whether these
injection-pressure-induced effects in natural gas−diesel DI
engines can be observed in direct-injection hydrogen engines.
In dual-fuel combustion engines utilizing a pilot diesel jet and
a hydrogen jet, the hydrogen injector’s design is critical due to
the low volumetric energy density of hydrogen fuel. Current
research efforts primarily concentrate on utilizing the maximum
hydrogen mass flow rate achievable with the existing injection
hardware. This includes employing methods such as increasing
the injection pressure or enlarging the nozzle orifice diameter to
enhance engine load capacity.
First, regarding the effect of injection pressure on hydrogen
reacting and nonreacting jet development, several fundamental
studies have investigated this phenomenon.
102,103
Although
these investigations primarily address autoigniting hydrogen jets
under engine-relevant conditions, their findings offer valuable
implications for dual-fuel hydrogen−diesel DI systems. In a
study by Yip et al.,
102
injection pressure was varied from 84 to
140 bar, with the jet injected into a high-pressure ambient
environment of 60 to 66 bar. This pressure ratio enabled the
simulation of subsonic to moderately under-expanded jets. The
temporal evolution of jet penetration and cone angle was
experimentally measured, revealing a square-root time depend-
ency for jet penetration with slower penetration observed at
lower injection pressures. The jet cone angle initially exhibited a
larger value than in the steady state across all pressure cases, a
transient behavior attributed to the recirculation zone behind
the jet head during its initial development phase.
From a reacting jet perspective, the heat release profile of the
hydrogen jet, ignited at a fixed timing relative to the start of
injection, showed an increase in peak heat release with a higher
injection pressure, likely due to the greater mass flow rate of
hydrogen. A higher steady-state heat release rate was also
observed, consistent with the increased continuous fuel
injection rate. Regarding flame development, the combustion
front receded toward the nozzle, stabilizing either at the nozzle
or a minimal distance downstream. This recession rate appeared
to slightly increase with injection pressure, despite the stronger
counterflow induced by the jet. The downstream extent of the
diffusion flame also increased with a higher injection pressure, an
effect not typically observed in turbulent jet diffusion
combustion. This phenomenon was suggested to result from
reduced air entrainment near the nozzle, particularly in
moderately under-expanded jets where shock waves limit
entrainment in the near-field core.
A subsequent study by Yip et al.
103
investigated the effect of
nozzle orifice diameter, ranging from 0.31 to 0.83 mm. The
results indicated that larger diameters led to higher premixed-
burn heat release peaks and steady heat release rates after
ignition, as expected from the corresponding increase in fuel
mass flow. The downstream extent of the diffusion flame also
increased with the orifice diameter, with longer flames observed
for larger nozzles. As expected, larger nozzle orifices increased
the fuel mass flow and extended the diffusion flame. Conversely,
smaller orifices reduced the mass flow, leading to rapid mixture
leaning and shorter flames. The study proposed a linear
relationship between the diffusion flame length and both the
mass flow rate (proportional to the square of the nozzle diameter
and linearly to the injection pressure) and the orifice diameter
(see Figure 10). This correlation, previously established for
subsonic and sonic hydrogen jets under atmospheric con-
ditions,
120−122
but now also observed under engine-relevant
high-temperature and high-pressure conditions by Yip et al.
103
However, the authors noted that further testing at higher
injection pressures is necessary to validate this relationship
across a wider parameter range.
Given hydrogen’s low volumetric energy density, engine
applications may require large nozzle diameters and high
injection pressures to achieve adequate energy delivery rates.
Higher injection pressures enhance jet penetration, thereby
increasing the air entrainment and combustion rates in diffusion
flames. However, as demonstrated by Yip et al.,
102,103
these
parameters also extend flame length, altering flame−wall
interactions and near-wall flow fields. Considering hydrogen’s
smaller quenching distance compared to hydrocarbon fuels,
17
such configurations could elevate heat losses, potentially
reducing efficiency. It is nonetheless noted that a simulation
study using CONVERGE simulation,
38
focusing on non-
premixed compression-ignition hydrogen engines with hydro-
gen pilots, suggested quenching distance may have less impact
on heat transfer in their setup. However, the study emphasized
the need for further computational and experimental validation.
In contrast, diesel injection in dual-fuel systems benefits from
a well-established knowledge base, with extensive high-fidelity
experimental and computational studies addressing global (e.g.,
ref 123) and microscopic features (e.g., refs 124 and 125) under
various parametric changes. In this context, the pilot diesel jet
primarily facilitates hydrogen ignition. Research has thus
Energy & Fuels pubs.acs.org/EF Review
https://doi.org/10.1021/acs.energyfuels.5c02216
Energy Fuels 2025, 39, 16538−16560
16553
Downloaded from pubs.​acs.​org/​enfuem/​article-pdf/​39/​35/​16538/​41340814/​ef5c02216.​pdf by SHANDONG UNIV user on 26 August 2026

<!-- PDF_PAGE: 17 -->

focused on optimizing injection settings to deliver the minimal
diesel quantity required for consistent ignition. Studies on
micropilot injectors, such as ref 126, aim to meet stringent
emission standards. A recent dual-fuel DI study
42
reported
efficient combustion despite unoptimized pilot diesel settings,
possibly due to hydrogen’s favorable properties, including high
flame speed and wide flammability limits. This suggests that
while retaining the original diesel injection system may involve
trade-offs regarding minimal fuel delivery, it offers viability for
scenarios demanding fuel share flexibility or diesel-only
operation. Regardless of the injection system used, a more
detailed analysis of jet−jet interactions in dual-fuel combustion
is needed, particularly in understanding how variations in the
injection pressure, nozzle diameter, and other factors influence
reaction front propagation, mixing, and overall combustion
dynamics. Gaining deeper insights into these factors is crucial for
optimizing combustion efficiency, reducing pollutant formation,
and ensuring stable operation across diverse operating
conditions.
4. CHALLENGES AND PERSPECTIVES
Significant progress has been made in understanding the
fundamental combustion processes of fuels under high-pressure
and high-temperature conditions relevant to engine operation.
Nevertheless, several challenges and opportunities remain. This
section outlines these challenges and proposes potential
research directions.
Recent fundamental studies have revealed distinctive ignition
and combustion characteristics of fuel jets under engine-relevant
conditions, with important implications for engine performance.
For example, hydrogen flames stabilize at very short distances
from the nozzle,
93,102,103
influencing heat transfer to the injector
and potentially affecting injector durability. Detailed character-
ization of this heat transfer process is essential to optimize
engine component design and durability.
Dual-fuel technology is garnering attention as a promising
strategy for decarbonizing sectors that are difficult to electrify,
such as marine and heavy-duty transport. Due to hydrogen’s low
volumetric energy density, large nozzle orifice diameters and
high injection pressures are typically required to ensure
adequate energy delivery rates. However, these parameters
tend to increase the flame length, affecting flame−wall
interactions, near-wall flow dynamics, and turbulence. These,
in turn, influence the wall heat transfer and overall engine
performance. A comprehensive understanding of these inter-
actions is therefore critical. Future investigations should explore
advanced injection strategies, such as multiple-injection
strategies,
98
to mitigate the momentum of hydrogen jets.
Effective implementation of such strategies necessitates a
detailed optimization of several parameters, including pilot jet
timing relative to hydrogen injections, interpulse separation,
injection durations, and pressures in the case of multiple-
injection strategies.
To date, many studies have employed single-component
diesel fuel surrogates to reduce chemical complexity and
leverage well-characterized fuel properties. However, commer-
cial diesel fuels vary significantly in formulation, leading to
differences in ignition, combustion, and emission characteristics.
Further research using a broader range of commercial diesel
fuels can yield deeper insights into these variations. In addition,
investigating more sustainable pilot fuel alternatives, such as
biodiesel,
127,128
offers greater potential for decarbonization.
Experience from diesel combustion studies has demonstrated
that integrating multispecies optical diagnostics with high-
fidelity numerical modeling in well-characterized experimental
configurations is critical for advancing understanding of complex
combustion phenomena.
129
A similar integrated approach is
expected to be essential for dual-fuel combustion research, as
evidenced by recent experimental and computational collabo-
rations, despite the recency of some data sets. While conven-
tional diagnostic tools used in fundamental studies, such as high-
speed schlieren imaging, have provided valuable insights into
ignition and flame development, they are inherently limited by
their line-of-sight nature. These techniques integrate informa-
tion along the optical path and are therefore typically used to
yield qualitative rather than quantitative data. Advanced laser-
based diagnostics, such as laser-induced incandescence (LII)
and laser-induced fluorescence (LIF),
130,131
offer the ability to
overcome these limitations. By offering planar or volumetric
slice-based measurements, advanced diagnostics provide spa-
tially resolved, species-specific data on combustion features such
as temperature,
132
intermediate species, and soot. This
quantitative information is essential for validating high-fidelity
numerical models and enables a more comprehensive under-
standing and prediction of the dual-fuel processes.
Fundamental studies are generally conducted under highly
controlled conditions with systematic parametric variation to
uncover detailed insights into combustion mechanisms.
Building on this foundational work, it is crucial to extend
research into application-relevant conditions, where the
technology attracts interest. Additionally, gradually introducing
real-world complexities beyond those explored in idealized
studies can help bridge the gap between laboratory-scale
experiments and practical engine applications.
Figure 10. Normalized flame length plotted against (m ̇ ·D)
1/3
, for 0.31
and 0.58 mm nozzles at three injection pressures. Here, m ̇ represents
the injection mass flow rate, and D is the nozzle orifice diameter. The
ambient temperature, gas density, and O
2
concentration are 1140 K, 24
kg/m
3
, and 21 vol %, respectively. Reproduced from ref 103. The figure
shows a linear relationship between diffusion flame length and both
mass flow rate (which scales with the square of the nozzle diameter and
linearly with injection pressure) and nozzle diameter. This correlation,
previously established for subsonic and sonic hydrogen jets under
atmospheric conditions,
120−122
is now also observed under engine-
relevant high-temperature and high-pressure conditions. Reproduced
from ref 103. Available under a Creative Commons CC-BY license.
Copyright 2022 Yip et al.
Energy & Fuels pubs.acs.org/EF Review
https://doi.org/10.1021/acs.energyfuels.5c02216
Energy Fuels 2025, 39, 16538−16560
16554
Downloaded from pubs.​acs.​org/​enfuem/​article-pdf/​39/​35/​16538/​41340814/​ef5c02216.​pdf by SHANDONG UNIV user on 26 August 2026

<!-- PDF_PAGE: 18 -->

One potential application is the use of hydrogen−diesel
engines to enhance hydrogen transportation logistics in
geographically expansive nations, such as Australia. Given the
country’s abundant renewable energy resources and its distance
from key export markets, converting renewable energy into
hydrogen and transporting it in liquefied form is a promising
pathway. However, due to hydrogen’s low volumetric energy
density, liquefaction is necessary, which introduces boil-off
challenges that must be managed to avoid overpressurization of
storage systems.
133
Hydrogen−diesel engines can utilize boil-off
hydrogen as a supplementary fuel source, reducing diesel
consumption and carbon emissions. This potential underscores
the need for further combustion studies under marine engine-
relevant conditions, where in-cylinder pressures greatly exceed
the pressure range examined in the current fundamentally
oriented studies; thus, research at higher pressures is necessary
to ensure relevance to real-world applications. Moreover, the
thermodynamic state of boiled-off hydrogen may influence
ignition behavior and combustion efficiency, requiring detailed
investigation.
Current experimental efforts are often performed under quasi-
steady-state ambient conditions that do not replicate the in-
cylinder swirl and turbulent flow fields present in real engines.
Even under these idealized settings, jet−jet interactions
significantly influence ignition delay, ignition location, and
flame propagation. To better capture these phenomena,
extending fundamental studies to more realistic test beds, such
as optical engine rigs
134
that replicate in-cylinder swirl and
turbulence, is essential. These facilities offer a platform to
investigate how these affect hydrogen−diesel processes,
including ignition kernel development and flame stabilization,
under more practical engine conditions.
To summarize, fundamental studies have laid a strong
foundation; however, addressing diagnostic limitations, broad-
ening fuel and operating condition ranges, and replicating
practical in-cylinder environments will be essential to unlocking
the full potential of hydrogen−diesel dual-fuel technologies and
supporting their adoption.
5. CONCLUSION
Direct injection (DI) combustion research has highlighted the
complex interplay among fuel injection parameters, ignition
characteristics, and combustion stability. Hydrogen’s high
autoignition resistance and unique properties necessitate careful
ignition and injection strategies. Studies have demonstrated the
effectiveness of combining pilot diesel injection with hydrogen
DI.
Injection timing and sequence significantly influence the
combustion characteristics of hydrogen−diesel dual-fuel DI
systems. Earlier hydrogen injection promotes premixed
combustion, resulting in a higher peak heat release rate.
However, this can lead to increased pressure oscillations,
noise, and knock. Conversely, later hydrogen injection shifts
combustion toward a mixing-controlled mode.
Dual-fuel DI offers operational flexibility by allowing
variations in the hydrogen energy share. Changes in relative
injection durations directly impact the heat release rate and
emissions. Experimental studies have shown that adjusting the
injection durations of pilot and main fuels alters the jet
momentum balance, affecting the entrainment of pilot
combustion products into the hydrogen jet. This interaction
influences flame stabilization and heat release, particularly in
high hydrogen energy share cases where prolonged main
injections entrain pilot combustion products upstream, leading
to varied flame stabilization behavior. Optical diagnostics have
revealed changed flow features in dual-fuel cases that are absent
in single-fuel configurations, including potentially changed soot
processes. These are attributed to varied mixture composition,
temperature, and strain, influencing soot processes and
highlighting the complex interplay between injection parame-
ters, mixture formation, and combustion stability.
Jet−jet interactions in dual-fuel DI systems add further
complexity, with the jet interaction angle playing a role in
ignition dynamics and combustion stability. Optical inves-
tigations have shown that more converged configurations, where
hydrogen and pilot diesel jets intersect at smaller angles, extend
the ignition delay but enhance reaction front propagation once
ignition occurs. This was attributed to increased preignition jet
interactions, which delay pilot autoignition while improving
flame propagation. Studies with varied jet interaction angles
demonstrated that increased convergence enhanced intersection
but slightly prolonged ignition delay compared to pilot-only
reference cases. However, these converged configurations
facilitated a faster reaction front transition from the pilot jet to
the hydrogen jet. Complementary laser-induced ignition studies
further highlighted the sensitivity of ignition location, showing
that downstream or peripheral ignition resulted in slower
upstream flame recession, affecting flame stabilization at the end
of injection, with potential efficiency and emission implications.
Ambient conditions significantly influence ignition and
combustion behavior in dual-fuel DI systems. Lower ambient
temperatures increase the interaction between hydrogen and
pilot fuel jets before ignition, although ignition delay analysis
suggests that pilot ignition timing remains relatively unchanged
compared to pilot-only cases. Lower temperatures also extend
the ignition delay of the main hydrogen fuel, increasing the fuel−
air mixing time before ignition and leading to a higher peak heat
release rate. Additionally, at reduced temperatures, the mixing-
controlled combustion phase becomes less distinct, with greater
variability in pilot ignition location and an extended premixed-
burn transient. Similarly, lower ambient oxygen concentrations
shift flame stabilization further downstream while increasing
variability due to near-nozzle interactions between unreacted
hydrogen and pilot combustion products, intermittently
reducing flame lift-off distances. Laser-induced ignition studies
have further demonstrated that edge-flame deflagration can
explain flame recession and stabilization under low-oxygen and
low-temperature conditions, with reduced flame speeds and
turbulence−chemistry interactions influencing recession and
stabilization behavior.
The roles of injection parameters�specifically injection
pressure and nozzle diameter�in shaping dual-fuel DI
combustion characteristics were reviewed. For hydrogen jets,
higher injection pressures enhance jet penetration and air
entrainment. However, increased injection pressure also extends
the flame length, affecting flame−wall interactions and
potentially increasing heat losses. Similarly, larger nozzle
diameters contribute to higher heat release rates and extended
diffusion flames. While pilot diesel injection benefits from an
established knowledge base, a further understanding of the
interplay between varying injection parameters of both hydro-
gen and diesel injectors in dual-fuel DI combustion remains
necessary.
Finally, recent advancements in optical diagnostics and
numerical modeling have improved our understanding of the
intricate dynamics governing hydrogen−diesel combustion,
Energy & Fuels pubs.acs.org/EF Review
https://doi.org/10.1021/acs.energyfuels.5c02216
Energy Fuels 2025, 39, 16538−16560
16555
Downloaded from pubs.​acs.​org/​enfuem/​article-pdf/​39/​35/​16538/​41340814/​ef5c02216.​pdf by SHANDONG UNIV user on 26 August 2026

<!-- PDF_PAGE: 19 -->

providing valuable insights for optimizing engine operating
strategies to balance efficiency, emissions, and stability.
However, further research is still required, including extending
the investigated conditions and parameter ranges to those more
representative of practical systems, optimizing injection control
strategies, and conducting high-fidelity numerical simulations.
The development of advanced dual-fuel combustion models,
corroborated by additional experimental measurements, will
also be essential to capture the complex interactions involved
and enhance the understanding of the underlying phenomena.
■
AUTHOR INFORMATION
Corresponding Author
Qing Nian Chan − School of Mechanical and Manufacturing
Engineering, The University of New South Wales, Sydney,
NSW 2052, Australia;
 orcid.org/0000-0002-5666-1890;
Email: qing.chan@unsw.edu.au
Authors
Patrick Rorimpandey − School of Mechanical and
Manufacturing Engineering, The University of New South
Wales, Sydney, NSW 2052, Australia
Kirtan Aryal − School of Mechanical and Manufacturing
Engineering, The University of New South Wales, Sydney,
NSW 2052, Australia
Guanxiong Zhai − School of Mechanical and Manufacturing
Engineering, The University of New South Wales, Sydney,
NSW 2052, Australia;
 orcid.org/0000-0001-9307-206X
Shijie Xu − Key Lab of Education Ministry for Power Machinery
and Engineering, School of Mechanical Engineering, Shanghai
Jiao Tong University, Shanghai 200240, China
Kar Mun Pang − Everllence, 2450 Copenhagen, Denmark
Guan Heng Yeoh − School of Mechanical and Manufacturing
Engineering, The University of New South Wales, Sydney,
NSW 2052, Australia
Sanghoon Kook − School of Mechanical and Manufacturing
Engineering, The University of New South Wales, Sydney,
NSW 2052, Australia
Complete contact information is available at:
https://pubs.acs.org/10.1021/acs.energyfuels.5c02216
Notes
The authors declare no competing financial interest.
Biographies
Patrick Rorimpandey is a Project Engineer at Johnstaff in Sydney,
Australia. Before his current role, Dr Rorimpandey was a Research
Assistant for the Trailblazer for Recycling and Clean Energy (TRaCE)
program at UNSW Sydney. He completed his Ph.D. candidature at
UNSW Sydney in 2025, supported by the Australian Government
Research Training Program, and received a Dean’s Award for his
outstanding thesis. Dr Rorimpandey’s research focused on hydrogen-
diesel dual-fuel combustion under compression-ignition engine
conditions.
Kirtan Aryal is a Masters by Research candidate at the School of
Mechanical and Manufacturing Engineering, University of New South
Wales, Sydney, Australia, supported by the Australian Government
Research Training Program. He earned his Master of Mechanical
Engineering at the University of Wollongong, Australia, in 2021. His
research focuses on methanol autoignition and dual-fuel combustion of
methanol and diesel under compression-ignition engine conditions.
Guanxiong Zhai serves as a Technical Officer at the School of
Mechanical and Manufacturing Engineering, UNSW Sydney, Australia.
He earned his Ph.D. from UNSW in 2022, with his thesis focusing on
understanding the ignition, combustion, and flame stabilization for
gasoline-like fuels under engine-relevant conditions. Dr Zhai is an
expert in high-speed imaging and laser diagnostics for turbulent flow
and combustion, possessing advanced image processing and data
analysis skills.
Shijie Xu is an Associate Professor at Shanghai Jiao Tong University
(SJTU), China. Before SJTU, Dr Xu was a Marie Curie Scholar at the
University of Birmingham, UK, and a postdoctoral fellow at Lund
University, Sweden. He received his Ph.D. from Lund University in
2021. His research interests span modeling of turbulent combustion,
encompassing spray and metal particle combustion, swirling flows and
flames, and the utilization of alternative fuels in engines and gas
turbines.
Kar Mun Pang is a Senior Research Engineer in the Department of
Injection and Combustion Simulations at Everllence (formerly MAN
Energy Solutions). In addition to his core responsibilities in daily R&D
activities, he plays a key role in coordinating external research projects
focused on fluid mechanics, combustion chemistry, and numerical
model development. Prior to Everllence, Dr Pang was a Senior Scientist
at the Technical University of Denmark. He earned his Ph.D. from the
University of Nottingham in 2011.
Guan Heng Yeoh is a Professor at the School of Mechanical and
Manufacturing Engineering, UNSW Sydney, Australia, where he directs
the ARC Research Hub for Fire Resilience Infrastructure, Assets and
Safety Advancements. He also holds a position as Principal Research
Scientist and leader of thermal hydraulics at the Australian Nuclear
Science Technology Organisation. Professor Yeoh received his Ph.D. in
Mechanical Engineering from UNSW in 1993 and is an expert in
computational techniques for multiphase flows.
Sanghoon Kook is a Professor of Mechanical Engineering at UNSW
Sydney, Australia, where he directs the Engine Research Laboratory.
His expertise lies in internal combustion engines, optical diagnostics
and alternative fuels including hydrogen, ammonia, ethanol, sustainable
aviation fuel and biodiesel. He was elected Fellow of SAE International
in 2023 and Fellow of The Combustion Institute in 2025.
Qing Nian Chan is an Associate Professor at the School of Mechanical
and Manufacturing Engineering, UNSW Sydney, Australia. He directs
the Advanced Combustion Diagnostics Laboratory. In 2023, he
received a CSIRO Mid-Career Fellowship through the International
Hydrogen Research Program. A/Professor Chan earned his Ph.D. from
The University of Adelaide, Australia, in 2011. His research blends
innovative diagnostics in thermodynamics, fluid dynamics, combustion,
and heat/mass transfer with techno-economic analyses to evaluate real-
world implications.
■
ACKNOWLEDGMENTS
The first author acknowledges the support of the Common-
wealth through the Australian Government Research Training
Program Scholarship. The corresponding author and the SJTU-
affiliated coauthor acknowledge the support of SJTU-UNSW
Collaborative Research Fund (Stage I).
■
REFERENCES
(1) Ursua, A.; Gandia, L. M.; Sanchis, P. Hydrogen production from
water electrolysis: current status and future trends. Proceedings of the
IEEE 2012, 100, 410−426.
(2) Ayers, K.; Danilovic, N.; Ouimet, R.; Carmo, M.; Pivovar, B.;
Bornstein, M. Perspectives on low-temperature electrolysis and
potential for renewable hydrogen at scale. Annu. Rev. Chem. Biomol.
Eng. 2019, 10, 219−239.
Energy & Fuels pubs.acs.org/EF Review
https://doi.org/10.1021/acs.energyfuels.5c02216
Energy Fuels 2025, 39, 16538−16560
16556
Downloaded from pubs.​acs.​org/​enfuem/​article-pdf/​39/​35/​16538/​41340814/​ef5c02216.​pdf by SHANDONG UNIV user on 26 August 2026

<!-- PDF_PAGE: 20 -->

(3) Chen, L.; Msigwa, G.; Yang, M.; Osman, A. I.; Fawzy, S.; Rooney,
D. W.; Yap, P.-S. Strategies to achieve a carbon neutral society: a review.
Environmental Chemistry Letters 2022, 20, 2277−2310.
(4) Cheng, Y.; Sinha, A.; Ghosh, V.; Sengupta, T.; Luo, H. Carbon tax
and energy innovation at crossroads of carbon neutrality: Designing a
sustainable decarbonization policy. Journal of Environmental Manage-
ment 2021, 294, 112957.
(5) Verhelst, S.; Wallner, T.; Eichlseder, H.; Naganuma, K.; Gerbig, F.;
Boyer, B.; Tanno, S. Electricity powering combustion: hydrogen
engines. Proceedings of the IEEE 2012, 100, 427−439.
(6) Li, J.; Wang, C.; Zhai, G.; Li, Q.; Lim, S. H.; Abdoli, S.; Kook, S.;
Yeoh, G. H.; Chan, Q. N. Evaluating the techno-economic feasibility of
hydrogen-fuelled reciprocating engines for renewable base-load power
generation. Energy Conversion and Management 2024, 311, 118515.
(7) IEA Global Hydrogen Review 2022. https://www.iea.org/
reports/global-hydrogen-review-2022, Accessed: 2025-04-09.
(8) Sadeq, A. M.; Homod, R. Z.; Hussein, A. K.; Togun, H.;
Mahmoodi, A.; Isleem, H. F.; Patil, A. R.; Moghaddam, A. H. Hydrogen
energy systems: Technologies, trends, and future prospects. Science of
The Total Environment 2024, 939, 173622.
(9) Lucia, U. Overview on fuel cells. Renewable and Sustainable Energy
Reviews 2014, 30, 164−169.
(10) Heywood, J. Internal Combustion Engine Fundamentals 2E;
McGraw-Hill Education: 2018.
(11) Verhelst, S.; Wallner, T. Hydrogen-fueled internal combustion
engines. Prog. Energy Combust. Sci. 2009, 35, 490−527.
(12) Hosseini, S. E.; Butler, B. An overview of development and
challenges in hydrogen powered vehicles. International Journal of Green
Energy 2020, 17, 13−37.
(13) Edwards, R.; Mahieu, V.; Griesemann, J.-C.; Larivé, J.-F.;
Rickeard, D. J. Well-to-Wheels Analysis of Future Automotive Fuels
and Powertrains in the European Context. SAE Transactions 2004, 113,
1072−1084.
(14) Staffell, I.; Scamman, D.; Velazquez Abad, A.; Balcombe, P.;
Dodds, P. E.; Ekins, P.; Shah, N.; Ward, K. R. The role of hydrogen and
fuel cells in the global energy system. Energy Environ. Sci. 2019, 12,
463−491.
(15) Vichard, L.; Petrone, R.; Harel, F.; Ravey, A.; Venet, P.; Hissel, D.
Long term durability test of open-cathode fuel cell system under actual
operating conditions. Energy Conversion and Management 2020, 212,
112813.
(16) Srna, A. Is there a place for H2 internal combustion engines?;
Report, 2022.
(17) Yip, H. L.; Srna, A.; Yuen, A. C. Y.; Kook, S.; Taylor, R. A.; Yeoh,
G. H.; Medwell, P. R.; Chan, Q. N. A review of hydrogen direct
injection for internal combustion engines: towards carbon-free
combustion. Applied Sciences 2019, 9, 4842.
(18) Gross, S. The challenge of decarbonizing heavy transport. Foreign
Policy. Brookings Institution 2020, Accessed: 2025-04-15.
(19) Deng, J.; Bae, C.; Denlinger, A.; Miller, T. Electric vehicles
batteries: requirements and challenges. Joule 2020, 4, 511−515.
(20) Jayachandran, M.; Gatla, R. K.; Flah, A.; Milyani, A. H.; Milyani,
H. M.; Blazek, V.; Prokop, L.; Kraiem, H. Challenges and opportunities
in green hydrogen adoption for decarbonizing hard-to-abate industries:
A comprehensive review. IEEE Access 2024, 12, 23363−23388.
(21) Aleiferis, P. G.; Rosati, M. F. Controlled autoignition of hydrogen
in a direct-injection optical engine. Combust. Flame 2012, 159, 2500−
2515.
(22) Xie, H.; Li, L.; Chen, T.; Yu, W.; Wang, X.; Zhao, H. Study on
spark assisted compression ignition (SACI) combustion with positive
valve overlap at medium−high load. Applied Energy 2013, 101, 622−
633.
(23) Chatlatanagulchai, W.; Rhienprayoon, S.; Yaovaja, K.;
Wannatong, K. Air/Fuel Ratio Control in Diesel-Dual-Fuel Engine
by Varying Throttle, EGR Valve, and Total Fuel. SAE 2010 Powertrains
Fuels & Lubricants Meeting, 2010.
(24) Das, L. M. Hydrogen Engines: A view of the past and a look into the
future; Report, 1990.
(25) Chong, C. T.; Hochgreb, S. Measurements of laminar flame
speeds of liquid fuels: Jet-A1, diesel, palm methyl esters and blends
using particle imaging velocimetry (PIV). Proceedings of the Combustion
Institute 2011, 33, 979−986.
(26) Mazloomi, K.; Gomes, C. Hydrogen as an energy carrier:
Prospects and challenges. Renewable and Sustainable Energy Reviews
2012, 16, 3024−3033.
(27) Bekius, H. Research in flammability limits and deflagration to
detonation transition of ethanol, 2013.
(28) Deb, M.; Sastry, G. R. K.; Bose, P. K.; Banerjee, R. An
experimental study on combustion, performance and emission analysis
of a single cylinder, 4-stroke DI-diesel engine using hydrogen in dual
fuel mode of operation. Int. J. Hydrogen Energy 2015, 40, 8586−8598.
(29) Nitnaware, P. T.; Suryawanshi, J. G. Effects of MBT spark timing
on performance emission and combustion characteristics of S.I engine
using hydrogen-CNG blends. Int. J. Hydrogen Energy 2016, 41, 666−
674.
(30) Beyer, A.; Di Domenico, D.; Beatrice, C.; Kulzer, A. C. High-
pressure direct injection as enabling technology for high-power density
hydrogen SI engines: Experimental analysis of the influence of jet-
guided combustion regimes on efficiency and abnormal combustion.
Energy Conversion and Management 2025, 326, 119497.
(31) Kiesgen, G.; Klu ̈ting, M.; Bock, C.; Fischer, H. The New 12-
Cylinder Hydrogen Engine in the 7 Series: The H2 ICE Age Has Begun.
SAE 2006 World Congress & Exhibition, 2006.
(32) Konnov, A. A.; Mohammad, A.; Kishore, V. R.; Kim, N. I.;
Prathap, C.; Kumar, S. A comprehensive review of measurements and
data analysis of laminar burning velocities for various fuel+air mixtures.
Prog. Energy Combust. Sci. 2018, 68, 197−267.
(33) Kawahara, N.; Tomita, E. Visualization of auto-ignition and
pressure wave during knocking in a hydrogen spark-ignition engine. Int.
J. Hydrogen Energy 2009, 34, 3156−3163.
(34) Rajasegar, R.; Srna, A.; Barbery, I.; Novella, R. On the
phenomenology of hot-spot induced pre-ignition in a direct-injection
hydrogen-fueled, heavy-duty, optical-engine. SAE International Journal
of Advances and Current Practices in Mobility 2024, 6, 1535−1547.
(35) Corrigan, D.; Di Blasio, G.; Ianniello, R.; Silvestri, N.; Breda, S.;
Fontanesi, S.; Beatrice, C. Engine knock detection methods for spark
ignition and prechamber combustion systems in a high-performance
gasoline direct injection engine. SAE International Journal of Engines
2022, 15, 883−897.
(36) Liu, H.; Li, J.; Wang, J.; Wu, C.; Liu, B.; Dong, J.; Liu, T.; Ye, Y.;
Wang, H.; Yao, M. Effects of injection strategies on low-speed marine
engines using the dual fuel of high-pressure direct-injection natural gas
and diesel. Energy Science & Engineering 2019, 7, 1994−2010.
(37) Ishibashi, R.; Tsuru, D. An optical investigation of combustion
process of a direct high-pressure injection of natural gas. Journal of
Marine Science and Technology 2017, 22, 447−458.
(38) Babayev, R.; Andersson, A.; Serra Dalmau, A.; Im, H. G.;
Johansson, B. Computational comparison of the conventional diesel
and hydrogen direct-injection compression-ignition combustion
engines. Fuel 2022, 307, 121909.
(39) Pawlak, G.; Skrzek, T.; Kosiuczenko, K.; Płochocki, P.; Simin ́ski,
P. Premixed dual-fuel combustion of camelina sativa Oil and ethanol.
SAE International Journal of Engines 2024, 18, 995−1015.
(40) Liu, X.; Seberry, G.; Kook, S.; Chan, Q. N.; Hawkes, E. R. Direct
injection of hydrogen main fuel and diesel pilot fuel in a retrofitted
single-cylinder compression ignition engine. Int. J. Hydrogen Energy
2022, 47, 35864−35876.
(41) Liu, X.; Srna, A.; Yip, H. L.; Kook, S.; Nian, Q.; Hawkes, E.
Comparison of hydrogen port injection and direct injection (DI) in a
single-cylinder dual-fuel diesel engine. 22nd Australian Fluid
Mechanics Conference, Brisbane, Australia, 2020.
(42) Rorimpandey, P.; Zhai, G.; Kook, S.; Hawkes, E. R.; Chan, Q. N.
Effects of energy-share and ambient oxygen concentration on
hydrogen-diesel dual-fuel direct-injection (H
2
DDI) combustion in
compression-ignition conditions. Int. J. Hydrogen Energy 2024, 49,
1346−1361.
Energy & Fuels pubs.acs.org/EF Review
https://doi.org/10.1021/acs.energyfuels.5c02216
Energy Fuels 2025, 39, 16538−16560
16557
Downloaded from pubs.​acs.​org/​enfuem/​article-pdf/​39/​35/​16538/​41340814/​ef5c02216.​pdf by SHANDONG UNIV user on 26 August 2026

<!-- PDF_PAGE: 21 -->

(43) Burkardt, P.; Gu ̈nther, M.; Villforth, J.; Pischinger, S. Jet-induced
compression ignition (JICI)�Application of spark-assisted compres-
sion ignition (SACI) in a combustion system with active pre-chamber.
SAE International Journal of Engines 2025, 18, 157−171.
(44) White, C.; Steeper, R.; Lutz, A. The hydrogen-fueled internal
combustion engine: A technical review. Int. J. Hydrogen Energy 2006,
31, 1292−1305.
(45) Stockhausen, W. F.; Natkin, R. J.; Kabat, D. M.; Reams, L.; Tang,
X.; Hashemi, S.; Szwabowski, S. J.; Zanardelli, V. P. Ford P2000
Hydrogen Engine Design and Vehicle Development Program. SAE
2002 World Congress & Exhibition, 2002.
(46) Tang, X.; Kabat, D. M.; Natkin, R. J.; Stockhausen, W. F.; Heffel,
J. Ford P2000 Hydrogen Engine Dynamometer Development. SAE
Transactions 2002, 111, 631−642.
(47) Wallner, T.; Lohse-Busch, H.; Gurski, S.; Duoba, M.; Thiel, W.;
Martin, D.; Korn, T. Fuel economy and emissions evaluation of BMW
Hydrogen 7 mono-fuel demonstration vehicles. Int. J. Hydrogen Energy
2008, 33, 7607−7618.
(48) Wallner, T.; Nande, A. M.; Naber, J. Evaluation of Injector
Location and Nozzle Design in a Direct-Injection Hydrogen Research
Engine. 2008 SAE International Powertrains, Fuels and Lubricants
Congress, 2008.
(49) Menaa, A.; Lounici, M.; Amrouche, F.; Loubar, K.; Kessal, M.
CFD analysis of hydrogen injection pressure and valve profile law
effects on backfire and pre-ignition phenomena in hydrogen-diesel dual
fuel engine. Int. J. Hydrogen Energy 2019, 44, 9408−9422.
(50) Wallner, T.; Ciatti, S.; Bihari, B. Investigation of injection
parameters in a hydrogen DI engine using an endoscopic access to the
combustion chamber. SAE World Congress & Exhibition, 2007.
(51) Wang, Z.; Liu, H.; Reitz, R. D. Knocking combustion in spark-
ignition engines. Prog. Energy Combust. Sci. 2017, 61, 78−112.
(52) Wallner, T.; Scarcelli, R.; Nande, A. M.; Naber, J. D. Assessment
of Multiple Injection Strategies in a Direct-Injection Hydrogen
Research Engine. SAE International Journal of Engines 2009, 2, 1701−
1709.
(53) Wimmer, A.; Wallner, T.; Ringler, J.; Gerbig, F. H2-direct
injection�a highly promising combustion concept; SAE Paper 2005-
01-0108; 2005.
(54) Lee, K.; Kim, Y.; Byun, C.; Lee, J. Feasibility of compression
ignition for hydrogen fueled engine with neat hydrogen-air pre-mixture
by using high compression. Int. J. Hydrogen Energy 2013, 38, 255−264.
(55) Rosati, M. F.; Aleiferis, P. G. Hydrogen SI and HCCI combustion
in a direct-injection optical engine. SAE International Journal of Engines
2009, 2, 1710−1736.
(56) Gomes Antunes, J. M.; Mikalsen, R.; Roskilly, A. P. An
experimental study of a direct injection compression ignition hydrogen
engine. Int. J. Hydrogen Energy 2009, 34, 6516−6522.
(57) Lin, Y.; Hadadpour, A.; Zhai, G.; Kook, S.; Chan, Q. Hydrogen
split injection at replicated compression-ignition engine conditions.
Energy Fuels 2025, 39, 4002−4018.
(58) Skeen, S.; Manin, J.; Pickett, L. M. Visualization of ignition
processes in high-pressure sprays with multiple injections of n-
Dodecane. SAE International Journal of Engines 2015, 8, 696−715.
(59) Xing, S.; Zhai, G.; Mo, H.; Medwell, P. R.; Yuen, A. C.; Kook, S.;
Yeoh, G. H.; Chan, Q. N. Study of ignition and combustion
characteristics of consecutive injections with iso-octane and n-heptane
as fuels. Energy Fuels 2020, 34, 14741−14756.
(60) Zhai, G.; Xing, S.; Yuen, A.; Yeoh, G. H.; Chan, Q. N. Spray and
combustion characteristics of gasoline-like fuel under compression-
ignition conditions. Energy Fuels 2020, 34, 16585−16598.
(61) Rochussen, J.; Yeo, J.; Kirchen, P. Effect of Fueling Control
Parameters on Combustion and Emissions Characteristics of Diesel-
Ignited Methane Dual-Fuel Combustion; 2016.
(62) Xiang, L.; Theotokatos, G.; Cui, H.; Xu, K.; Ben, H.; Ding, Y.
Parametric Knocking Performance Investigation of Spark Ignition
Natural Gas Engines and Dual Fuel Engines. Journal of Marine Science
and Engineering 2020, 8, 459.
(63) Lounici, M.; Benbellil, M.; Loubar, K.; Niculescu, D.; Tazerout,
M. Knock characterization and development of a new knock indicator
for dual-fuel engines. Energy 2017, 141, 2351−2361.
(64) Dimitriou, P.; Tsujimura, T. A review of hydrogen as a
compression ignition engine fuel. Int. J. Hydrogen Energy 2017, 42,
24470−24486.
(65) Woodyard, D. In Pounder’s Marine Diesel Engines and Gas
Turbines, 9th ed.; Woodyard, D., Ed.; Butterworth-Heinemann:
Oxford, 2009; pp 41−60.
(66) Duan, X.; Liu, Y.; Lai, M. C.; Guo, G.; Liu, J.; Chen, Z.; Deng, B.
Effects of natural gas composition and compression ratio on the
thermodynamic and combustion characteristics of a heavy-duty lean-
burn SI engine fueled with liquefied natural gas. Fuel 2019, 254,
115733−115733.
(67) Zhai, G.; Rorimpandey, P.; Pang, K. M.; Kook, S.; Yeoh, G. H.;
Chan, Q. N. Methane-diesel direct-injection combustion under engine-
relevant conditions. Fuel 2025, 399, 135613.
(68) Wan, Q.; Zhai, G.; Wang, C.; Yuen, A. C.; Medwell, P. R.; Kook,
S.; Yeoh, G. H.; Chan, Q. N. A parametric investigation of methane jets
in direct-injection compression-ignition conditions. Fuel 2023, 334,
126521.
(69) Gleis, S.; Frankl, S.; Waligorski, D.; Prager, M.; Wachtmeister, G.
Investigation of the high-pressure-dual-fuel (HPDF) combustion
process of natural gas on a fully optically accessible research engine;
SAE Paper 2019-01-2172; 2019.
(70) Hatzipanagiotou, A.; Marko, F.; Koenig, G.; Krueger, C.; Wenzel,
P.; Koch, T. Numerical and optical analysis of heterogeneous gas
combustion with diesel pilot ignition in a commercial vehicle engine.
International Journal of Engine Research 2018, 19, 109−119.
(71) MAN Truck & Bus, MAN engines: The first dual-fuel hydrogen
engines in use on a work boat. https://press.mantruckandbus.com/
corporate/man-engines-the-first-dual-fuel-hydrogen-engines-in-use-
on-a-work-boat/, Accessed: 2025-04-10.
(72) Yanmar Holdings Co., Ltd., Successful operation at rated output
in the trial of a hydrogen 4-stroke high-speed engine for coastal vessels.
https://www.yanmar.com/global/news/2024/10/30/143738.html,
Accessed: 2025-04-10.
(73) Sjöholm, J.; Ringsted, S. B.; Kryger, M. J.; Ishibashi, R.;
Fukushima, T. Hydrogen based ship propulsion, first ever large two
stroke engine tests with hydrogen. 31st CIMAC World Congress 2025,
Zurich, Switzerland, 2025.
(74) MAN Energy Solutions. MITSUI performs world-first hydrogen
test. https://www.man-es.com/company/press-releases/press-details/
2024/03/07/mitsui-performs-world-first-hydrogen-test, Accessed:
2025-04-08.
(75) MITSUI E&S Co., Ltd. World’s first successful hydrogen
combustion operation with a large marine engine. https://www.mes.co.
jp/english/press/2024/0307_002400.html, Accessed: 2025-04-08.
(76) Westport Fuel Systems Inc. and Scania. Westport and Scania
announce impressive test results of H
2
HPDI fuel system for heavy-duty
transport. https://investors.westport.com/news/news-details/2022/
Westport-and-Scania-Announce-Impressive-Test-Results-of-H-HPDI-
Fuel-System-for-Heavy-Duty-Transport/default.aspx, Accessed: 2025-
04-10.
(77) McTaggart-Cowan, G.; Mann, K.; Huang, J.; Singh, A.; Patychuk,
B.; Zheng, Z. X.; Munshi, S. Direct injection of natural gas at up to 600
bar in a pilot-ignited heavy-duty engine. SAE International Journal of
Engines 2015, 8, 981−996.
(78) Liu, X.; Yang, L.; Chan, Q. N.; Kook, S. Split injection strategies
for a high-pressure hydrogen direct injection in a small-bore dual-fuel
diesel engine. Int. J. Hydrogen Energy 2024, 57, 904−917.
(79) Kook, S.; Liu, X.; Edmonds, B. Hydrogen-diesel direct injection
dual-fuel system for internal combustion engines. Australian Patent
Provisional Application No. 2022900118, filed 21 Jan 2022, Interna-
tional Application No. PCT/AU2023/050019, International Publica-
tion Date 27 Jul 2023.
(80) Wang, Y.; Evans, A.; Srna, A.; Wehrfritz, A.; Hawkes, E.; Liu, X.;
Kook, S.; Chan, Q. N. A numerical investigation of mixture formation
Energy & Fuels pubs.acs.org/EF Review
https://doi.org/10.1021/acs.energyfuels.5c02216
Energy Fuels 2025, 39, 16538−16560
16558
Downloaded from pubs.​acs.​org/​enfuem/​article-pdf/​39/​35/​16538/​41340814/​ef5c02216.​pdf by SHANDONG UNIV user on 26 August 2026

<!-- PDF_PAGE: 22 -->

and combustion characteristics of a hydrogen-diesel dual direct
injection engine; SAE Paper 2021-01-0526; 2021.
(81) Liu, X.; Srna, A.; Yip, H. L.; Kook, S.; Chan, Q. N.; Hawkes, E. R.
Performance and emissions of hydrogen-diesel dual direct injection
(H2DDI) in a single-cylinder compression-ignition engine. Int. J.
Hydrogen Energy 2021, 46, 1302−1314.
(82) Treacy, M.; Hadadpour, A.; Bai, X.-S.; Fatehi, H. Performance
and emissions of a novel high-pressure direct injection hydrogen dual-
fuel engine. Fuel 2024, 376, 132639.
(83) Lucchini, T.; Schirru, A.; Mehl, M.; D’Errico, G.; Rorimpandey,
P.; Chan, Q. N.; Kook, S.; Hawkes, E. R. Modeling hydrogen−diesel
dual direct injection combustion with FGM and transported PDF.
Proceedings of the Combustion Institute 2024, 40, 105213.
(84) Treacy, M. Numerical studies of advanced combustion concepts
in hydrogen and methanol compression ignition engines. Ph.D. thesis,
Department of Energy Sciences, Lund University, 2024.
(85) Li, T.; Zhao, P.; He, H.; Wang, C.; Zhang, H.; Chen, Z.; Chen, H.
Dual-fuel dual-direct injection: An efficient and clean combustion
technology for diesel engines. Journal of the Energy Institute 2025, 119,
102006.
(86) Brown, B. S.; Laforet, C. A.; Rogak, S. N.; Munsh, S. R.
Comparison of injectors for compression ignition of natural gas with
entrained diesel. International Journal of Engine Research 2011, 12, 109−
122.
(87) Laforet, C. A.; Brown, B. S.; Rogak, S. N.; Munshi, S. R.
Compression ignition of directly injected natural gas with entrained
diesel. International Journal of Engine Research 2010, 11, 207−218.
(88) Florea, R.; Neely, G. D.; Abidin, Z.; Miwa, J. Efficiency and
emissions characteristics of partially premixed dual-fuel combustion by
co-direct injection of NG and diesel fuel (DI
2
); 2016.
(89) Neely, G. D.; Florea, R.; Miwa, J.; Abidin, Z. Efficiency and
Emissions Characteristics of Partially Premixed Dual-Fuel Combustion
by Co-Direct Injection of NG and Diesel Fuel (DI
2
) - Part 2. WCX 17:
SAE World Congress Experience, 2017.
(90) Fink, G.; Jud, M.; Sattelmayer, T. Fundamental study of diesel-
piloted natural gas direct injection under different operating conditions.
Journal of Engineering for Gas Turbines and Power 2019, 141,
No. 091006.
(91) Liu, J.; Yang, F.; Wang, H.; Ouyang, M.; Hao, S. Effects of pilot
fuel quantity on the emissions characteristics of a CNG/diesel dual fuel
engine with optimized pilot injection timing. Applied Energy 2013, 110,
201−206.
(92) Gerke, U.; Steurs, K.; Rebecchi, P.; Boulouchos, K. Derivation of
burning velocities of premixed hydrogen/air flames at engine-relevant
conditions using a single-cylinder compression machine with optical
access. Int. J. Hydrogen Energy 2010, 35, 2566−2577.
(93) Rorimpandey, P.; Yip, H. L.; Srna, A.; Zhai, G.; Wehrfritz, A.;
Kook, S.; Hawkes, E. R.; Chan, Q. N. Hydrogen-diesel dual-fuel direct-
injection (H2DDI) combustion under compression-ignition engine
conditions. Int. J. Hydrogen Energy 2023, 48, 766−783.
(94) Yip, H. L.; Srna, A.; Zhai, G.; Wehrfritz, A.; Kook, S.; Hawkes, E.
R.; Chan, Q. N. Laser-induced plasma-ignited hydrogen jet combustion
in engine-relevant conditions. Int. J. Hydrogen Energy 2023, 48, 1568−
1581.
(95) Idicheria, C. A.; Pickett, L. M. Ignition, soot formation, and end-
of-combustion transients in diesel combustion under high-EGR
conditions. International Journal of Engine Research 2011, 12, 376−392.
(96) Rorimpandey, P.; Zhai, G.; Kook, S.; Hawkes, E. R.; Chan, Q. N.
Effects of jet interaction angle on the ignition and combustion
characteristics of hydrogen-diesel dual-fuel direct injection. Int. J.
Hydrogen Energy 2024, 67, 172−191.
(97) Yip, H. L.; Zhai, G.; Rorimpandey, P.; Kook, S.; Hawkes, E. R.;
Chan, Q. N. Experimental study of laser-ignited hydrogen jet flame
evolution under simulated direct-injection diesel engine conditions. Int.
J. Hydrogen Energy 2024, 93, 1060−1070.
(98) Genzale, C.; Pickett, L.; Hoops, A.; Headrick, J. Laser ignition of
multi-injection gasoline sprays; SAE Paper 2011-01-0659; 2011.
(99) Zhai, G.; Xing, S.; Yuen, A. C.; Medwell, P. R.; Kook, S.; Yeoh, G.
H.; Chan, Q. N. Laser ignition of iso-octane and n-heptane jets under
compression-ignition conditions. Fuel 2022, 311, 122555.
(100) Naber, J.; Siebers, D. Hydrogen combustion under diesel engine
conditions. Int. J. Hydrogen Energy 1998, 23, 363−371.
(101) Pickett, L. M.; Siebers, D. L. Soot in diesel fuel jets: effects of
ambient temperature, ambient density, and injection pressure. Combust.
Flame 2004, 138, 114−135.
(102) Yip, H. L.; Srna, A.; Liu, X.; Kook, S.; Hawkes, E. R.; Chan, Q.
N. Visualization of hydrogen jet evolution and combustion under
simulated direct-injection compression-ignition engine conditions. Int.
J. Hydrogen Energy 2020, 45, 32562−32578.
(103) Yip, H. L.; Srna, A.; Wehrfritz, A.; Kook, S.; Hawkes, E. R.;
Chan, Q. N. A parametric study of autoigniting hydrogen jets under
compression-ignition engine conditions. Int. J. Hydrogen Energy 2022,
47, 21307−21322.
(104) Fink, G.; Jud, M.; Sattelmayer, T. Influence of the spatial and
temporal interaction between diesel pilot and directly injected natural
gas jet on ignition and combustion characteristics. Journal of Engineering
for Gas Turbines and Power 2018, 140, 102811.
(105) Trusca, B. High pressure direct injection of natural gas and
hydrogen fuel in a diesel engine. Ph.D. thesis, University of British
Columbia, Canada, 2001.
(106) Kammermann, T.; Koch, J.; Wright, Y. M.; Soltic, P.;
Boulouchos, K. Generation of turbulence in a RCEM towards engine
relevant conditions for premixed combustion based on CFD and PIV
investigations. SAE International Journal of Engines 2017, 10, 2176−
2190.
(107) Frankl, S.; Gleis, S.; Karmann, S.; Prager, M.; Wachtmeister, G.
Investigation of ammonia and hydrogen as CO2-free fuels for heavy
duty engines using a high pressure dual fuel combustion process.
International Journal of Engine Research 2021, 22, 3196−3208.
(108) Gu, S. Direct numerical simulation of hydrogen-diesel dual-fuel
combustion. Ph.D. thesis, School of Mechanical and Manufacturing
Engineering, UNSW Sydney, 2023.
(109) Kahila, H.; Wehrfritz, A.; Kaario, O.; Vuorinen, V. Large-eddy
simulation of dual-fuel ignition: Diesel spray injection into a lean
methane-air mixture. Combust. Flame 2019, 199, 131−151.
(110) Xu, S.; Pang, K. M.; Li, Y.; Hadadpour, A.; Yu, S.; Zhong, S.;
Jangi, M.; Bai, X.-s. LES/TPDF investigation of the effects of ambient
methanol concentration on pilot fuel ignition characteristics and
reaction front structures. Fuel 2021, 287, 119502.
(111) Zhou, Y.; Xu, S.; Xu, L.; Bai, X.-S. FGM modeling of ammonia/
n-heptane combustion under RCCI engine conditions. Proceedings of
the Combustion Institute 2024, 40, 105601.
(112) Reitz, R.; Hessel, R.; Musculus, M. A visual investigation of
CFD-predicted in-cylinder mechanisms that control first- and second-
stage ignition in diesel jets; SAE Paper 2019-01-0543; 2019.
(113) Knox, B. W.; Genzale, C. L.; Pickett, L. M.; Garcia-Oliver, J. M.;
Vera-Tudela, W. Combustion recession after end of injection in diesel
sprays. SAE International Journal of Engines 2015, 8, 679−695.
(114) White, T. R. Simultaneous diesel and natural gas injection for
dual-fuelling compression-ignition engines. Ph.D. thesis, University of
New South Wales Sydney, Australia, 2006.
(115) Jud, M.; Wieland, C.; Fink, G.; Sattelmayer, T. Numerical
analysis of the combustion process in dual-fuel engines with direct
injection of natural gas. Internal Combustion Engine Division Fall
Technical Conference, 2018; p V002T06A008.
(116) Musculus, M. P.; Miles, P. C.; Pickett, L. M. Conceptual models
for partially premixed low-temperature diesel combustion. Prog. Energy
Combust. Sci. 2013, 39, 246−283.
(117) Pickett, L. M.; Kook, S.; Persson, H.; Andersson, O. Diesel fuel
jet lift-off stabilization in the presence of laser-induced plasma ignition.
Proceedings of the Combustion Institute 2009, 32, 2793−2800.
(118) Verhelst, S.; Maesschalck, P.; Rombaut, N.; Sierens, R.
Increasing the power output of hydrogen internal combustion engines
by means of supercharging and exhaust gas recirculation. Int. J.
Hydrogen Energy 2009, 34, 4406−4412.
Energy & Fuels pubs.acs.org/EF Review
https://doi.org/10.1021/acs.energyfuels.5c02216
Energy Fuels 2025, 39, 16538−16560
16559
Downloaded from pubs.​acs.​org/​enfuem/​article-pdf/​39/​35/​16538/​41340814/​ef5c02216.​pdf by SHANDONG UNIV user on 26 August 2026

<!-- PDF_PAGE: 23 -->

(119) Saravanan, N.; Nagarajan, G.; Kalaiselvan, K.; Dhanasekaran, C.
An experimental investigation on hydrogen as a dual fuel for diesel
engine system with exhaust gas recirculation technique. Renewable
Energy 2008, 33, 422−427.
(120) T., G. Liftoff heights and visible flame lengths of vertical
turbulent jet diffusion flames in still air. Combust. Sci. Technol. 1984, 41,
17−29.
(121) Molkov, V. Hydrogen non-reacting and reacting jets in stagnant
air: overview and state-of-the-art. Proceedings of the 10th International
Conference on Fluid Control, Measurements, and Visualization,
Moscow, Russia, 2009.
(122) Molkov, V.; Saffers, J. Hydrogen jet flames. Int. J. Hydrogen
Energy 2013, 38, 8141−8158.
(123) Pastor, J. V.; Garcia-Oliver, J. M.; Garcia, A.; Morales López, A.
An experimental investigation on spray mixing and combustion
characteristics for spray C/D nozzles in a constant pressure vessel.
International Powertrains, Fuels & Lubricants Meeting, 2018.
(124) Ong, J. C.; Walther, J. H.; Xu, S.; Zhong, S.; Bai, X.-S.; Pang, K.
M. Effects of ambient pressure and nozzle diameter on ignition
characteristics in diesel spray combustion. Fuel 2021, 290, 119887.
(125) Ong, J. C.; Zhang, Y.; Xu, S.; Walther, J. H.; Bai, X.-S.; Pang, K.
M. Large eddy simulation of n-dodecane spray flame: Effects of
injection pressure on spray combustion characteristics at low ambient
temperature. Proceedings of the Combustion Institute 2023, 39, 2631−
2642.
(126) Park, H.; Wright, Y. M.; Seddik, O.; Srna, A.; Kyrtatos, P.;
Boulouchos, K. Phenomenological micro-pilot ignition model for
medium-speed dual-fuel engines. Fuel 2021, 285, 118955.
(127) Ming, C.; Rizwanul Fattah, I.; Chan, Q. N.; Pham, P. X.;
Medwell, P. R.; Kook, S.; Yeoh, G. H.; Hawkes, E. R.; Masri, A. R.
Combustion characterization of waste cooking oil and canola oil based
biodiesels under simulated engine conditions. Fuel 2018, 224, 167−
177.
(128) Fattah, I. M. R.; Ming, C.; Chan, Q. N.; Wehrfritz, A.; Pham, P.
X.; Yang, W.; Kook, S.; Medwell, P. R.; Yeoh, G. H.; Hawkes, E. R.;
Masri, A. R. Spray and combustion investigation of post injections
under low-temperature combustion conditions with biodiesel. Energy
Fuels 2018, 32, 8727−8742.
(129) Engine Combustion Network. https://ecn.sandia.gov/, Ac-
cessed 2025-06-18.
(130) Deng, S.; Mueller, M. E.; Chan, Q. N.; Qamar, N. H.; Dally, B.
B.; Alwahabi, Z. T.; Nathan, G. J. Hydrodynamic and chemical effects of
hydrogen addition on soot evolution in turbulent nonpremixed bluff
body ethylene flames. Proceedings of the Combustion Institute 2017, 36,
807−814.
(131) Qamar, N. H.; Nathan, G. J.; Alwahabi, Z. T.; Chan, Q. N. Soot
sheet dimensions in turbulent nonpremixed flames. Combust. Flame
2011, 158, 2458−2464.
(132) Medwell, P. R.; Chan, Q. N.; Kalt, P. A. M.; Alwahabi, Z. T.;
Dally, B. B.; Nathan, G. J. Instantaneous temperature imaging of
diffusion flames using two-line atomic fluorescence. Appl. Spectrosc.
2010, 64, 173−176.
(133) Morales-Ospino, R.; Celzard, A.; Fierro, V. Strategies to recover
and minimize boil-off losses during liquid hydrogen storage. Renewable
and Sustainable Energy Reviews 2023, 182, 113360.
(134) Heaton, A.; Chan, Q. N.; Kook, S. Flame developments of pilot
diesel ignited hydrogen jet in an optical dual direct injection engine;
SAE Paper 2025-01-0237; 2025.
Energy & Fuels pubs.acs.org/EF Review
https://doi.org/10.1021/acs.energyfuels.5c02216
Energy Fuels 2025, 39, 16538−16560
16560
Downloaded from pubs.​acs.​org/​enfuem/​article-pdf/​39/​35/​16538/​41340814/​ef5c02216.​pdf by SHANDONG UNIV user on 26 August 2026
