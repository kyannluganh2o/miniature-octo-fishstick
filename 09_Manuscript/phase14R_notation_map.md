# Phase 14R Notation Map

This map governs the Phase 14R manuscript, figures, tables, and captions. Bold symbols denote vectors; unbold symbols denote scalars or vector magnitudes.

| Symbol | Type | Definition | Required qualifier / usage |
|---|---|---|---|
| \(p_{\mathrm{inj}}(t)\) | scalar history | injector or rail pressure history | State measurement location, absolute basis, and event-time origin. |
| \(\mathrm{NPR}(t)\) | scalar history | instantaneous upstream-to-downstream pressure ratio | State numerator and denominator roles, total/static type, and absolute basis. |
| \(x_{\mathrm{MD}}/D\) | scalar ratio | Mach-disk axial position normalized by nozzle diameter | State Mach-disk definition, diameter basis, and transient stage. |
| \(\mathbf{x}_d(t)\) | vector history | droplet or fragment centroid position | State coordinate system and tracked object. |
| \(\mathbf{u}_d(t)\) | vector history | droplet or fragment velocity | Same frame as \(\mathbf{u}_g\). |
| \(\mathbf{u}_g(\mathbf{x},t)\) | vector field | gas velocity | State thermodynamic region and reference frame. |
| \(\mathbf{u}_{\mathrm{rel}}(t)=\mathbf{u}_g[\mathbf{x}_d(t),t]-\mathbf{u}_d(t)\) | vector history | local droplet-relative gas velocity | Use \(|\mathbf{u}_{\mathrm{rel}}|\) for the scalar magnitude in dimensionless groups. |
| \(\rho_g\) | scalar | gas density | State pre-wave, post-wave, local, or averaged condition. |
| \(M_s\) | scalar | incident-shock Mach number | Incident shock relative to the preshock sound speed. |
| \(M_{\mathrm{rel}}\) | scalar | droplet-relative Mach number | Use \(|\mathbf{u}_{\mathrm{rel}}|\) and the stated local sound speed. |
| \(\mathrm{We}=\rho_g|\mathbf{u}_{\mathrm{rel}}|^2d/\sigma\) | scalar | Weber number | State density, velocity, length \(d\), surface tension \(\sigma\), frame, and thermodynamic state. |
| \(\mathrm{Re}=\rho_g|\mathbf{u}_{\mathrm{rel}}|d/\mu_g\) | scalar | gas-side Reynolds number | State viscosity, phase, frame, and thermodynamic state. |
| \(\mathrm{Oh}=\mu_l/\sqrt{\rho_l\sigma d}\) | scalar | Ohnesorge number | State liquid properties, temperature, and length scale. |
| \(\tau_{\mathrm{load}}\) | scalar duration | duration of a named pressure or slip load | Define start and end events; distinguish front transit from post-wave residence. |
| \(\tau_{\mathrm{response}}\) | scalar duration | time to a named liquid-response event | Name onset, shedding, rupture, or completion event and any normalization. |
| \(L_E/L_D\) | scalar ratio | evaporation distance divided by a named strong-wave/device length | Retain the source-specific definition of \(L_D\); not an HPDI ignition predictor. |
| signed \(\Delta\mathrm{SOI}\) | scalar interval | target SOI minus reference SOI | Name both fuels/events, fuel order, electronic/hydraulic/actual event type, sign convention, and unit. |

## Consistency rules

- Pressure \(p\), density \(\rho\), Mach number, dimensionless groups, characteristic lengths, and time intervals are scalars.
- Position and velocities are vectors: \(\mathbf{x}_d\), \(\mathbf{u}_d\), \(\mathbf{u}_g\), and \(\mathbf{u}_{\mathrm{rel}}\).
- Dynamic loading uses the velocity magnitude, \(\rho_g|\mathbf{u}_{\mathrm{rel}}|^2\), not a signed vector square.
- Subscript \(g\) denotes gas and \(l\) liquid; subscript \(d\) identifies a tracked droplet or fragment.
- \(D\) denotes nozzle diameter only in \(x_{\mathrm{MD}}/D\); droplet or fragment size is written \(d_0\) or \(d\) and defined locally.
- \(\tau_{\mathrm{load}}/\tau_{\mathrm{response}}\) is an organizing hypothesis, not a universal response criterion.
- Plain-text CSV and figure labels use typography-neutral aliases (`x_d`, `u_d`, `u_g`, `u_rel`); these retain the vector meanings defined above, while scalar speed terms are written with magnitude bars, for example `|u_rel|`.
