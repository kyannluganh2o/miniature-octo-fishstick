from __future__ import annotations

import base64
import csv
import html
import shutil
import subprocess
import textwrap
from dataclasses import dataclass
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "08_Figures_Tables" / "phase14S"
PANELS = OUT / "source_panels"
FIGURES = OUT / "figures"
PREVIEWS = OUT / "figure_previews"
TABLES = OUT / "tables"
RENDERED = ROOT / "tmp" / "pdfs" / "phase14s_final_pages"
for directory in (PANELS, FIGURES, PREVIEWS, TABLES, RENDERED):
    directory.mkdir(parents=True, exist_ok=True)

PDFTOPPM = "pdftoppm"
W, H = 1800, 1100
NAVY = "#17324D"
BLUE = "#2F6B9A"
CYAN = "#DDEFF6"
TEAL = "#2A7F79"
ORANGE = "#D96C2F"
PALE_ORANGE = "#F9E8D8"
RED = "#B33A3A"
GRAY = "#65717D"
LIGHT = "#F5F7F9"
DARK = "#16202A"
WHITE = "#FFFFFF"


def font(size: int, bold: bool = False):
    candidates = [
        Path("C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf"),
        Path("C:/Windows/Fonts/calibrib.ttf" if bold else "C:/Windows/Fonts/calibri.ttf"),
    ]
    for candidate in candidates:
        if candidate.exists():
            return ImageFont.truetype(str(candidate), size)
    return ImageFont.load_default()


def render_page(pdf: Path, page: int, dpi: int = 300) -> Path:
    target = RENDERED / f"{pdf.stem}_p{page}_{dpi}.png"
    if target.exists():
        return target
    prefix = target.with_suffix("")
    subprocess.run(
        [PDFTOPPM, "-f", str(page), "-l", str(page), "-r", str(dpi), "-png", "-singlefile", str(pdf), str(prefix)],
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    return target


@dataclass
class PanelSpec:
    panel_id: str
    paper_id: str
    pdf: str
    page: int
    figure: str
    original_panel: str
    crop: tuple[float, float, float, float]
    phenomenon: str
    condition: str
    section: str
    new_figure: str
    crop_notes: str
    source_locator: str


PANEL_SPECS = [
    PanelSpec("SP02-01", "B009", "02_PDF_Raw/B/B-H2-04_2014_Hamzehloo_LES_Underexpanded_Hydrogen_MethaneJets.pdf", 11, "Fig. 8", "sequence", (0.160, 0.077, 0.850, 0.390), "Axial-Mach evolution and Mach-disk formation", "Hydrogen; NPR 10; transient LES", "S06", "FIG-02", "Exact figure crop; time labels and contour scale retained", "LOC-B009-0005"),
    PanelSpec("SP02-02", "B021", "02_PDF_Raw/B/B-E-01_2023_Anaclerio_Numerical_Underexpanded_HydrogenJets_ICE.pdf", 11, "Fig. 18", "plot", (0.075, 0.082, 0.462, 0.237), "Steady/unsteady Mach-disk comparison", "Hydrogen; representative NPR 12.7 case", "S06", "FIG-02", "Fig. 18 plot only; caption and body text excluded", "LOC-B021-0006"),
    PanelSpec("SP02-03", "B029", "02_PDF_Raw/B/B-E-09_2026_Sang_InjectorPressureBuildUp_Underexpanded_HydrogenJet.pdf", 8, "Fig. 11", "velocity contours", (0.48, 0.22, 0.94, 0.50), "Velocity-contour and shock-cell evolution during injector build-up", "Hydrogen injector; transient pressure-build case", "S06", "FIG-02", "Fig. 11 image sequence; time labels and color bar retained", "LOC-B029-0008"),
    PanelSpec("SP04-01", "C016", "02_PDF_Raw/C/C-SD-09_2021_Sharma_ShockInduced_DropletAerobreakup.pdf", 13, "Fig. 6", "d", (0.492, 0.258, 0.837, 0.383), "Acceleration-dominated RTP morphology", "Water; M_s 1.45; We 795; d0 0.5 mm", "S10", "FIG-04", "Fig. 6(d) pair only; scale bars retained", "LOC-C016-0004"),
    PanelSpec("SP04-02", "C016", "02_PDF_Raw/C/C-SD-09_2021_Sharma_ShockInduced_DropletAerobreakup.pdf", 13, "Fig. 6", "b", (0.492, 0.105, 0.837, 0.230), "Shear-induced entrainment morphology", "Water; M_s 1.30; We 1600; d0 2.9 mm", "S10", "FIG-04", "Fig. 6(b) pair only; scale bars retained", "LOC-C016-0004"),
    PanelSpec("SP04-03", "C013", "02_PDF_Raw/C/C-SD-06_2020_Dorschner_LigamentFormation_Shedding_DropletAerobreakup.pdf", 22, "Fig. 15", "sequence", (0.10, 0.09, 0.53, 0.74), "Recurrent ligament formation and shedding", "Water; We 295", "S10", "FIG-04", "Exact figure sequence; annotations retained; caption excluded", "PDF p.22, Fig. 15"),
    PanelSpec("SP04-04", "D018", "02_PDF_Raw/D/D-DW-03_2026_Yang_RP3_Droplet_DeformationBreakup_Detonation.pdf", 10, "Fig. 15", "sequence", (0.12, 0.06, 0.91, 0.14), "KHI-dominant to coupled KHI-RTI fragmentation", "RP-3; d0 530 um; detonation Ma 7.03", "S10", "FIG-04", "Fig. 15 strip only; times and stage brackets retained", "LOC-D018-0008"),
    PanelSpec("SP04A-01", "C029", "02_PDF_Raw/C/C-PC-03_2021_Boyd_Transcritical_ShockDroplet_Interaction.pdf", 14, "Fig. 9", "a-f", (0.20, 0.09, 0.80, 0.70), "Diverging and converging refracted-wave histories", "n-dodecane in nitrogen; 500 K n=0.78 vs 650 K n=1.8", "S11", "FIG-04A", "Full Fig. 9 comparison; annotations and axes retained; caption excluded", "PDF p.14, Fig. 9"),
    PanelSpec("SP05-01", "C035", "02_PDF_Raw/C/C-MD-03_2021_Wang_ShockInduced_TandemDroplet_Breakup.pdf", 5, "Fig. 5", "sequence", (0.521, 0.470, 0.902, 0.823), "Tandem-droplet wake shielding and differential deformation", "Water; tandem pair; S/D and We case-specific", "S14", "FIG-05", "Exact sequence; dimensional labels retained", "LOC-C035-0004"),
    PanelSpec("SP05-02", "C036", "02_PDF_Raw/C/C-MD-04_2026_Guo_ShockInduced_ParallelDroplets_Aerobreakup.pdf", 5, "Fig. 2", "sequence", (0.275, 0.098, 0.850, 0.420), "Parallel-droplet channel opening and closure", "Parallel droplets; We 16.7; multiple L/D", "S14", "FIG-05", "Exact image sequence; spacing labels retained", "LOC-C036-0003"),
    PanelSpec("SP05-03", "C033", "02_PDF_Raw/C/C-MD-01_2011_Chauvin_PlanarShock_TwoPhase_GasLiquid_Medium.pdf", 5, "Fig. 2", "sequence and traces", (0.20, 0.50, 0.66, 0.94), "Shock propagation and pressure attenuation through a droplet cloud", "Water-droplet cloud; planar shock", "S14", "FIG-05", "Fig. 2 sequence and pressure traces; caption excluded", "PDF p.5, Fig. 2"),
    PanelSpec("SP06-01", "C024", "02_PDF_Raw/C/C-ST-04_2023_DukeWalker_SmallDroplet_BreakupEvaporation_HighWeber.pdf", 7, "Fig. 7", "a-d", (0.114, 0.050, 0.886, 0.382), "Fragment-cloud formation and optical disappearance", "Acetone droplets; M about 2.09; high We", "S18", "FIG-06", "Exact figure crop; time labels and flow direction retained", "LOC-C024-0005"),
    PanelSpec("SP06-02", "C026", "02_PDF_Raw/C/C-ST-06_2025_DukeWalker_SmallDroplet_DeformationAcceleration_HighSpeed.pdf", 6, "Fig. 2", "A-D", (0.46, 0.095, 0.767, 0.536), "Size- and loading-dependent early droplet evolution", "Acetone; about 55-200 um; case-specific Mach/We", "S18", "FIG-06", "Selected rows A-D; scale and time labels retained", "PDF p.6, Fig. 2"),
    PanelSpec("SP06-03", "C031", "02_PDF_Raw/C/C-PC-05_2025_Song_3D_PhaseChange_ShockDroplet_Interaction.pdf", 11, "Fig. 7", "a-c", (0.178, 0.115, 0.833, 0.493), "No-phase-change, evaporation, and condensation morphologies", "n-dodecane; modeled Mach 1.47 family", "S18", "FIG-06", "Exact comparison; branch labels and times retained", "LOC-C031-0008"),
    PanelSpec("SP06-04", "C032", "02_PDF_Raw/C/C-PC-06_2016_Strotos_NDecane_DropletBreakup_HighTemperatureGas.pdf", 5, "Figs. 3-4", "800 and 1000 K", (0.08, 0.03, 0.96, 0.80), "Heating-dependent deformation and breakup", "n-decane; 800 and 1000 K; We 15-90", "S18", "FIG-06", "Both source figures retained for direct thermal comparison", "PDF p.5, Figs. 3-4"),
    PanelSpec("SP07-01", "A022", "02_PDF_Raw/A/A-H2-05_2024_Rorimpandey_JetInteractionAngle_H2DDI.pdf", 3, "Fig. 2", "a-c", (0.502, 0.051, 0.868, 0.706), "Hydrogen-pilot jet intersection geometry", "H2/diesel DDI; 12, 15, and 19 deg arrangements", "S22", "FIG-07", "Geometry panels only; dimensions retained", "LOC-A022-0006"),
    PanelSpec("SP07-02", "A026", "02_PDF_Raw/A/A-H2-09_2025_Heaton_HydrogenInjectionTiming_EnergyProportion_Flame.pdf", 10, "Fig. 10", "sequence", (0.068, 0.055, 0.932, 0.476), "Timing-conditioned diesel-pilot and early hydrogen flame development", "H2/diesel optical engine; timing sweep", "S22", "FIG-07", "Exact matrix; crank-angle and timing labels retained", "LOC-A026-0005"),
    PanelSpec("SP07-03", "A007", "02_PDF_Raw/A/A-NG-07_2018_Fink_DieselPilot_NGJet_SpatialTemporalInteraction.pdf", 6, "Fig. 10", "map", (0.095, 0.681, 0.457, 0.882), "Spatial-temporal natural-gas ignition-delay map", "Diesel pilot/natural gas; RCEM", "S22", "FIG-07", "Plot only; axes and color scale retained", "LOC-A007-0005"),
    PanelSpec("SP08-01", "D018", "02_PDF_Raw/D/D-DW-03_2026_Yang_RP3_Droplet_DeformationBreakup_Detonation.pdf", 5, "Fig. 5", "a-f", (0.13, 0.18, 0.865, 0.420), "Water/RP-3 detonation-driven breakup comparison", "Detonation Ma about 6-7; water and RP-3", "S26", "FIG-08", "Exact figure; time and liquid labels retained", "LOC-D018-0005"),
    PanelSpec("SP08-02", "D019", "02_PDF_Raw/D/D-DW-04_2026_Zou_DetonationShock_DropletInteraction_Mechanisms.pdf", 11, "Fig. 8", "a-d", (0.20, 0.08, 0.76, 0.46), "Reacting detonation versus inert-shock wave configurations", "Water; d0 4.8 mm; matched incident Mach 4.8", "S26", "FIG-08", "Fig. 8 only; contours and scales retained", "LOC-D019-0006"),
    PanelSpec("SP08-03", "D014", "02_PDF_Raw/D/D-RDE-09_2025_Li_DropletKinematics_Distribution_Ethanol_RDE.pdf", 10, "Fig. 16", "a-b", (0.11, 0.065, 0.79, 0.37), "Wave-relative droplet position and thermal/evaporation history", "Two-phase ethanol RDE; grouped histories", "S26", "FIG-08", "Fig. 16 only; axes and position markers retained", "PDF p.10, Fig. 16"),
    PanelSpec("SP08-04", "D019", "02_PDF_Raw/D/D-DW-04_2026_Zou_DetonationShock_DropletInteraction_Mechanisms.pdf", 14, "Fig. 12", "a-d", (0.20, 0.08, 0.79, 0.46), "Reacting/inert post-wave pressure-field divergence", "Water; matched incident Mach 4.8", "S26", "FIG-08", "Fig. 12 only; contours and scales retained", "LOC-D019-0008"),
]


def make_panel(spec: PanelSpec) -> Path:
    pdf = ROOT / spec.pdf
    page_png = render_page(pdf, spec.page)
    image = Image.open(page_png).convert("RGB")
    if spec.panel_id == "SP06-04":
        def crop_norm(box):
            x0, y0, x1, y1 = box
            return image.crop((int(x0 * image.width), int(y0 * image.height), int(x1 * image.width), int(y1 * image.height)))
        upper = crop_norm((0.10, 0.045, 0.90, 0.37))
        lower = crop_norm((0.10, 0.445, 0.90, 0.77))
        width = max(upper.width, lower.width)
        crop = Image.new("RGB", (width, upper.height + lower.height + 24), "white")
        crop.paste(upper, ((width - upper.width) // 2, 0))
        crop.paste(lower, ((width - lower.width) // 2, upper.height + 24))
    else:
        x0, y0, x1, y1 = spec.crop
        box = (int(x0 * image.width), int(y0 * image.height), int(x1 * image.width), int(y1 * image.height))
        crop = image.crop(box)
    target = PANELS / f"{spec.panel_id}_{spec.paper_id}_{spec.figure.replace(' ', '').replace('.', '').replace('-', '_')}.png"
    crop.save(target, optimize=True)
    return target


PANEL_PATHS = {spec.panel_id: make_panel(spec) for spec in PANEL_SPECS}


class Canvas:
    def __init__(self, title: str, subtitle: str = ""):
        self.im = Image.new("RGB", (W, H), WHITE)
        self.draw = ImageDraw.Draw(self.im)
        self.svg = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">', '<rect width="100%" height="100%" fill="#FFFFFF"/>']
        self.rect(0, 0, W, 92, fill=NAVY)
        self.text(55, 24, title, 36, WHITE, bold=True)
        if subtitle:
            self.text(55, 100, subtitle, 22, GRAY)

    def rect(self, x, y, w, h, fill=WHITE, outline=None, width=2, radius=0, dash=False):
        pil_fill = None if fill in (None, "none") else fill
        self.draw.rounded_rectangle((x, y, x + w, y + h), radius=radius, fill=pil_fill, outline=outline, width=width)
        stroke = outline or "none"
        dash_attr = ' stroke-dasharray="12,10"' if dash else ""
        self.svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" fill="{fill}" stroke="{stroke}" stroke-width="{width}"{dash_attr}/>' )

    def line(self, points, fill=NAVY, width=4, dash=False):
        self.draw.line(points, fill=fill, width=width)
        pts = " ".join(f"{x},{y}" for x, y in points)
        dash_attr = ' stroke-dasharray="12,10"' if dash else ""
        self.svg.append(f'<polyline points="{pts}" fill="none" stroke="{fill}" stroke-width="{width}"{dash_attr}/>' )

    def arrow(self, x0, y0, x1, y1, fill=NAVY, width=4, dash=False):
        self.line([(x0, y0), (x1, y1)], fill, width, dash)
        import math
        angle = math.atan2(y1 - y0, x1 - x0)
        size = 16
        pts = [(x1, y1), (x1 - size * math.cos(angle - 0.55), y1 - size * math.sin(angle - 0.55)), (x1 - size * math.cos(angle + 0.55), y1 - size * math.sin(angle + 0.55))]
        self.draw.polygon(pts, fill=fill)
        self.svg.append('<polygon points="' + " ".join(f"{x},{y}" for x, y in pts) + f'" fill="{fill}"/>')

    def text(self, x, y, text, size=24, fill=DARK, bold=False, anchor="la"):
        f = font(size, bold)
        self.draw.text((x, y), text, font=f, fill=fill, anchor=anchor)
        weight = "700" if bold else "400"
        anchor_svg = {"la": "start", "ma": "middle", "ra": "end"}.get(anchor, "start")
        self.svg.append(f'<text x="{x}" y="{y + size}" font-family="Arial" font-size="{size}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor_svg}">{html.escape(text)}</text>')

    def wrapped(self, x, y, text, width_chars, size=24, fill=DARK, bold=False, line_gap=6, anchor="la"):
        lines = []
        for paragraph in str(text).split("\n"):
            lines.extend(textwrap.wrap(paragraph, width=width_chars, break_long_words=False, break_on_hyphens=False) or [""])
        for i, line in enumerate(lines):
            self.text(x, y + i * (size + line_gap), line, size, fill, bold, anchor)
        return len(lines) * (size + line_gap)

    def panel(self, panel_id, x, y, w, h, label, caption=""):
        path = PANEL_PATHS[panel_id]
        img = Image.open(path).convert("RGB")
        ratio = min(w / img.width, h / img.height)
        resized = img.resize((max(1, int(img.width * ratio)), max(1, int(img.height * ratio))), Image.Resampling.LANCZOS)
        px = int(x + (w - resized.width) / 2)
        py = int(y + (h - resized.height) / 2)
        self.im.paste(resized, (px, py))
        href = "../source_panels/" + path.name
        self.svg.append(f'<image href="{html.escape(href)}" x="{px}" y="{py}" width="{resized.width}" height="{resized.height}" preserveAspectRatio="xMidYMid meet"/>')
        self.rect(x, y, w, h, fill="none", outline="#B8C2CC", width=2)
        self.rect(x, y + h - 40, w, 40, fill="#FFFFFF", outline=None, width=0)
        self.text(x + 12, y + h - 35, label, 19, NAVY, bold=True)
        if caption:
            self.text(x + w - 12, y + h - 35, caption, 17, GRAY, anchor="ra")

    def box_text(self, x, y, w, h, title, body="", fill=LIGHT, outline=BLUE, dash=False, title_size=None, body_size=20):
        self.rect(x, y, w, h, fill=fill, outline=outline, width=3, radius=16, dash=dash)
        if title_size is None:
            title_size = 20 if w < 260 else 24
        title_height = self.wrapped(x + w / 2, y + 16, title, max(12, int(w / (title_size * 0.58))), title_size, NAVY, bold=True, line_gap=2, anchor="ma")
        if body:
            self.wrapped(x + w / 2, y + 22 + title_height, body, max(15, int(w / (body_size * 0.58))), body_size, DARK, anchor="ma")

    def save(self, figure_id: str):
        self.svg.append("</svg>")
        self.im.save(PREVIEWS / f"{figure_id}.png", optimize=True)
        (FIGURES / f"{figure_id}.svg").write_text("\n".join(self.svg), encoding="utf-8")


def fig01():
    c = Canvas("FIG-01 | Injector-to-ignition physical chain", "Transient forcing, liquid response, transport, and ignition")
    labels = [
        ("Injector dynamics", "needle motion; p_inj(t)"),
        ("Transient wave field", "shocks; expansion; vortices"),
        ("Local droplet loading", "p[x_d,t]; rho_g[x_d,t]; u_rel"),
        ("Liquid response", "deformation; instability"),
        ("Fragment population", "size; velocity; temperature"),
        ("Transport / phase change", "residence; vaporization"),
        ("Mixture", "vapor and pilot-product field"),
        ("Ignition", "kernel; heat release"),
    ]
    x0, y, bw, bh, gap = 35, 360, 205, 190, 14
    for i, (title, body) in enumerate(labels):
        x = x0 + i * (bw + gap)
        c.box_text(x, y, bw, bh, title, body, fill=CYAN if i < 3 else (PALE_ORANGE if i < 6 else LIGHT))
        if i < len(labels) - 1:
            open_gate = i in (1, 3, 5, 6)
            c.arrow(x + bw, y + bh / 2, x + bw + gap - 5, y + bh / 2, RED if open_gate else NAVY, 4, open_gate)
    c.rect(560, 730, 680, 105, fill="#FFF8F0", outline=RED, width=3, radius=16, dash=True)
    c.text(900, 750, "Open connectors = interface quantities not yet measured together", 22, RED, bold=True, anchor="ma")
    c.text(900, 795, "physical sequence shown; causal closure remains conditional", 20, DARK, anchor="ma")
    c.save("FIG-01")


def fig02():
    c = Canvas("FIG-02 | Transient injector and underexpanded-wave evolution", "Event-aligned literature observations and a compact chronology")
    c.panel("SP02-01", 45, 150, 560, 650, "(a) B009 · Fig. 8", "axial Mach evolution")
    c.panel("SP02-02", 620, 150, 560, 650, "(b) B021 · Fig. 18", "steady / unsteady topology")
    c.panel("SP02-03", 1195, 150, 560, 650, "(c) B029 · Fig. 11", "velocity / shock-cell evolution")
    y = 900
    events = ["opening", "pressure build-up", "choking", "shock cells", "Mach disk", "overshoot", "semi-steady"]
    xs = [100 + i * 255 for i in range(len(events))]
    c.arrow(xs[0], y, xs[-1] + 100, y, NAVY, 5)
    for x, event in zip(xs, events):
        c.draw.ellipse((x - 8, y - 8, x + 8, y + 8), fill=ORANGE)
        c.svg.append(f'<circle cx="{x}" cy="{y}" r="8" fill="{ORANGE}"/>')
        c.text(x, y + 28, event, 20, DARK, anchor="ma")
    c.save("FIG-02")


def fig03():
    c = Canvas("FIG-03 | Eulerian field to Lagrangian droplet loading", "Visible wave topology is not the load sampled by a moving pilot droplet")
    boxes = [
        (45, "Eulerian gas field", "p(x,t); rho_g(x,t); u_g(x,t)\nshocks; expansions; vortices", CYAN, BLUE),
        (485, "Droplet trajectory", "x_d(t); u_d(t)\nposition and velocity through the field", PALE_ORANGE, ORANGE),
        (925, "Sampled loading", "p[x_d(t),t]\nrho_g[x_d(t),t]\nu_rel(t)", "#EEF6ED", TEAL),
        (1365, "Liquid response", "acceleration; deformation\ninstability; breakup", PALE_ORANGE, ORANGE),
    ]
    for x, title, body, fill, outline in boxes:
        c.box_text(x, 180, 390, 260, title, body, fill=fill, outline=outline)
    for x in (435, 875, 1315):
        c.arrow(x, 310, x + 50, 310)
    c.box_text(870, 610, 400, 190, "Loading clock", "tau_load\namplitude; direction; duration", fill=LIGHT, outline=TEAL)
    c.box_text(1335, 610, 400, 190, "Liquid-response clock", "tau_response\nresponse event and normalization", fill=LIGHT, outline=ORANGE)
    c.arrow(1120, 440, 1070, 610, TEAL, 4)
    c.arrow(1560, 440, 1535, 610, ORANGE, 4)
    c.box_text(285, 640, 440, 180, "Organizing ratio", "tau_load / tau_response\nhypothesis only", fill="#FFF8F0", outline=RED, dash=True)
    c.arrow(870, 705, 725, 720, RED, 4, True)
    c.arrow(1335, 705, 725, 740, RED, 4, True)
    c.text(900, 960, "Actual HPDI pilot-droplet histories remain unresolved.", 30, RED, bold=True, anchor="ma")
    c.save("FIG-03")


def fig04():
    c = Canvas("FIG-04 | Distinct breakup structures under compressible loading", "Panels are mechanism examples, not a universal regime progression")
    c.panel("SP04-03", 40, 150, 520, 820, "(c) C013 · Fig. 15", "recurrent ligament shedding")
    c.panel("SP04-01", 610, 150, 550, 340, "(a) C016 · Fig. 6(d)", "acceleration-dominated RTP")
    c.panel("SP04-02", 1210, 150, 550, 340, "(b) C016 · Fig. 6(b)", "shear-dominated SIE")
    c.text(885, 515, "Piercing / bag response", 21, NAVY, bold=True, anchor="ma")
    c.text(1485, 515, "Entrainment / fine mist", 21, NAVY, bold=True, anchor="ma")
    c.panel("SP04-04", 610, 620, 1150, 300, "(d) D018 · Fig. 15", "KHI -> coupled KHI-RTI")
    c.text(300, 995, "First shedding ≠ breakup completion", 20, NAVY, bold=True, anchor="ma")
    c.text(1185, 955, "Reacting strong-wave analogue only", 21, RED, bold=True, anchor="ma")
    c.save("FIG-04")


def fig04a():
    c = Canvas("FIG-04A | Internal-wave refraction changes with thermodynamic state", "C029 Fig. 9: direct comparison of diverging and converging refracted-wave histories")
    c.panel("SP04A-01", 90, 145, 1120, 830, "(a-f) C029 · Fig. 9", "n < 1 diverging | n > 1 converging")
    c.box_text(1270, 220, 440, 250, "Diverging branch", "500 K; n = 0.78\nrefracted shock advances\ninternal reflections follow", fill=CYAN)
    c.box_text(1270, 560, 440, 250, "Converging branch", "650 K; n = 1.8\nrefracted shock lags\nfocus emits a transmitted wave", fill=PALE_ORANGE, outline=ORANGE)
    c.text(1490, 905, "2-D transcritical calculation; not a breakup-regime map", 20, RED, bold=True, anchor="ma")
    c.save("FIG-04A")


def fig05():
    c = Canvas("FIG-05 | Configuration-dependent collective mechanisms", "Comparison of isolated, ordered-pair, and cloud responses; columns are not a temporal sequence")
    cols = [(30, "Isolated droplet"), (365, "Tandem pair"), (700, "Parallel pair"), (1035, "Droplet cloud")]
    for x, title in cols:
        c.text(x + 150, 150, title, 25, NAVY, bold=True, anchor="ma")
    c.box_text(30, 200, 300, 600, "(a) Canonical local response", "author schematic\nincident shock + post-wave flow\nno shielding\nno population feedback", fill=CYAN)
    c.panel("SP05-01", 365, 200, 300, 600, "(b) C035 · Fig. 5", "wake shielding")
    c.panel("SP05-02", 700, 200, 300, 600, "(c) C036 · Fig. 2", "squeeze / closure")
    c.panel("SP05-03", 1035, 200, 300, 600, "(d) C033 · Fig. 2", "cloud attenuation")
    c.box_text(1450, 250, 300, 500, "Dense polydisperse reacting HPDI spray", "joint size, spacing, velocity, temperature, vapor, and reaction statistics", fill="#FFF8F0", outline=RED, dash=True, title_size=20, body_size=19)
    c.arrow(1340, 500, 1450, 500, RED, 5, True)
    c.text(1378, 440, "open transfer", 20, RED, bold=True, anchor="ma")
    for x, body in [(180, "single-body load"), (515, "wake shielding"), (850, "channel closure"), (1185, "wave attenuation")]:
        c.text(x, 860, body, 22, DARK, anchor="ma")
    c.text(1600, 860, "Direct dense-HPDI validation absent", 22, RED, bold=True, anchor="ma")
    c.save("FIG-05")


def fig06():
    c = Canvas("FIG-06 | Fragmentation and phase-change competition", "Source observations above; conditional physical branches below")
    for pid, x, label, cap in [
        ("SP06-01", 30, "(a) C024 · Fig. 7", "fragment cloud"),
        ("SP06-02", 465, "(b) C026 · Fig. 2", "size / loading"),
        ("SP06-03", 900, "(c) C031 · Fig. 7", "phase-change branch"),
        ("SP06-04", 1335, "(d) C032 · Figs. 3-4", "thermal-property branch"),
    ]:
        c.panel(pid, x, 145, 405, 500, label, cap)
    c.box_text(40, 735, 300, 180, "Thermal state", "temperature; volatility; local pressure", fill=LIGHT)
    c.box_text(410, 700, 480, 210, "Branch A | vapor layer / blowing", "reduced interfacial shear → suppressed KH growth", fill=CYAN, outline=BLUE)
    c.box_text(410, 930, 480, 125, "Branch B | heated liquid", "lower surface tension → promoted deformation", fill=PALE_ORANGE, outline=ORANGE, body_size=18)
    c.box_text(1050, 760, 690, 230, "Conditional downstream state", "fragment distribution → transport → evaporation → vapor redistribution", fill="#FFF8F0", outline=RED, dash=True, title_size=22, body_size=20)
    c.arrow(340, 825, 410, 805, BLUE, 4)
    c.arrow(340, 825, 410, 990, ORANGE, 4)
    c.arrow(890, 805, 1050, 840, BLUE, 4)
    c.arrow(890, 990, 1050, 910, ORANGE, 4)
    c.text(1395, 1015, "Breakup ≠ faster evaporation without state + residence", 18, RED, bold=True, anchor="ma")
    c.save("FIG-06")


def fig07():
    c = Canvas("FIG-07 | Relative injection chronology and ignition response", "Signed timing and geometry are direct controls; wave-mediated fragment effects remain hypothetical")
    c.text(120, 160, "Pilot SOI", 24, NAVY, bold=True)
    c.text(120, 235, "Main-fuel SOI", 24, NAVY, bold=True)
    c.arrow(300, 175, 800, 175, NAVY, 4)
    c.arrow(300, 250, 800, 250, ORANGE, 4)
    c.line([(550, 145), (550, 275)], GRAY, 3, True)
    c.text(550, 285, "signed Delta SOI", 22, DARK, bold=True, anchor="ma")
    c.box_text(890, 145, 350, 160, "Geometry + chronology", "fuel order; actual event; jet intersection", fill=LIGHT)
    c.arrow(800, 212, 890, 212)
    c.box_text(1320, 145, 390, 160, "Interaction state", "pilot products; mixture; ignition kernel", fill=PALE_ORANGE, outline=ORANGE)
    c.arrow(1240, 225, 1320, 225)
    c.panel("SP07-01", 40, 385, 540, 510, "(a) A022 · Fig. 2", "jet geometry")
    c.panel("SP07-02", 630, 385, 540, 510, "(b) A026 · Fig. 10", "timing / flame")
    c.panel("SP07-03", 1220, 385, 540, 510, "(c) A007 · Fig. 10", "ignition-delay map")
    c.rect(80, 955, 760, 85, fill="#EEF6ED", outline=TEAL, width=3, radius=14)
    c.text(460, 977, "Direct pathway: timing + geometry -> interaction / mixture / ignition", 22, TEAL, bold=True, anchor="ma")
    c.rect(960, 955, 760, 85, fill="#FFF8F0", outline=RED, width=3, radius=14, dash=True)
    c.text(1340, 977, "Hypothesized pathway: wave -> fragments -> mixture -> ignition", 22, RED, bold=True, anchor="ma")
    c.save("FIG-07")


def fig08():
    c = Canvas("FIG-08 | Strong-wave comparison domain", "Direct detonation/RDE observations identify transferable local variables and non-transferable device scales")
    c.panel("SP08-01", 35, 145, 540, 390, "(a) D018 · Fig. 5", "liquid-dependent breakup")
    c.panel("SP08-02", 600, 145, 540, 390, "(b) D019 · Fig. 8", "matched leading Mach")
    c.panel("SP08-03", 35, 560, 540, 390, "(c) D014 · Fig. 16", "wave-relative thermal history")
    c.panel("SP08-04", 600, 560, 540, 390, "(d) D019 · Fig. 12", "later field divergence")
    c.box_text(1200, 190, 540, 310, "Shared local variables", "post-wave p; rho_g; u_rel\nd0; fragment state; residence", fill=CYAN)
    c.box_text(1200, 570, 540, 310, "Domain-specific scales", "reaction zone; RDE refill/front\nthermochemistry; device geometry; HPDI ignition chronology", fill=PALE_ORANGE, outline=ORANGE)
    c.text(1450, 980, "Strong-wave comparison only - no direct HPDI transfer closure.", 20, RED, bold=True, anchor="ma")
    c.save("FIG-08")


def fig09():
    c = Canvas("FIG-09 | Aligned clocks, state transfer, and missing interfaces", "Columns follow physical stages; rows show what must be synchronized")
    stages = ["Wave / load", "Liquid response", "Fragments", "Vapor transport", "Mixture", "Ignition"]
    clocks = ["tau_load", "tau_response", "tau_breakup", "tau_evap", "tau_mix", "tau_ign"]
    states = ["p, rho_g, u_rel", "shape / instability", "d_f, v_f, T_f", "vapor / species", "phi, T, O2", "radicals / heat release"]
    x0, bw, gap = 120, 250, 28
    c.text(35, 205, "Stage", 22, NAVY, bold=True)
    c.text(35, 370, "Clock", 22, NAVY, bold=True)
    c.text(35, 540, "State", 22, NAVY, bold=True)
    for i, stage in enumerate(stages):
        x = x0 + i * (bw + gap)
        c.box_text(x, 160, bw, 115, stage, fill=CYAN if i < 2 else (PALE_ORANGE if i < 4 else LIGHT), title_size=22)
        c.box_text(x, 330, bw, 115, clocks[i], fill=WHITE, outline=BLUE, title_size=23)
        c.box_text(x, 500, bw, 115, states[i], fill=WHITE, outline=TEAL, title_size=20)
        if i < len(stages) - 1:
            c.arrow(x + bw, 218, x + bw + gap - 4, 218, GRAY, 3)
    c.text(35, 750, "Missing", 22, RED, bold=True)
    missing = [(120, 420, "trajectory-resolved load"), (568, 390, "dense collective response"), (986, 390, "fragment → mixture"), (1404, 390, "mixture → ignition")]
    for x, w, label in missing:
        c.box_text(x, 710, w, 170, label, "synchronized evidence absent", fill="#FFF8F0", outline=RED, dash=True, title_size=21, body_size=18)
    c.text(900, 980, "No row is a universal scalar; each interface carries a state and a clock.", 25, RED, bold=True, anchor="ma")
    c.save("FIG-09")


for fn in (fig01, fig02, fig03, fig04, fig04a, fig05, fig06, fig07, fig08, fig09):
    fn()


def write_csv(path: Path, rows: list[dict], fieldnames: list[str]):
    with path.open("w", encoding="utf-8-sig", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


registry_fields = ["source_panel_id", "paper_id", "pdf_file", "pdf_page", "original_figure", "original_panel", "phenomenon", "condition_summary", "manuscript_section", "new_figure_id", "crop_notes", "source_locator", "notes"]
registry_rows = []
for spec in PANEL_SPECS:
    registry_rows.append({
        "source_panel_id": spec.panel_id,
        "paper_id": spec.paper_id,
        "pdf_file": spec.pdf,
        "pdf_page": spec.page,
        "original_figure": spec.figure,
        "original_panel": spec.original_panel,
        "phenomenon": spec.phenomenon,
        "condition_summary": spec.condition,
        "manuscript_section": spec.section,
        "new_figure_id": spec.new_figure,
        "crop_notes": spec.crop_notes,
        "source_locator": spec.source_locator,
        "notes": "Direct crop from canonical local PDF; scientific content unaltered.",
    })
write_csv(OUT / "source_panel_registry.csv", registry_rows, registry_fields)

revision_rows = [
    {"figure_id": "FIG-01", "phase14_role": "Author synthesis", "phase14R_action": "retain and simplify", "phase14R_type": "author-generated synthesis", "source_panels": 0, "scientific_change": "Compact physical sequence; four open couplings retained."},
    {"figure_id": "FIG-02", "phase14_role": "Hybrid placeholders", "phase14R_action": "replace", "phase14R_type": "literature-image-dominant hybrid", "source_panels": 3, "scientific_change": "Actual transient jet panels plus compact event timeline."},
    {"figure_id": "FIG-03", "phase14_role": "Author synthesis", "phase14R_action": "retain and simplify", "phase14R_type": "author-generated synthesis", "source_panels": 0, "scientific_change": "Unified vector notation and explicit sampled loading."},
    {"figure_id": "FIG-04", "phase14_role": "Mechanism-flow hybrid", "phase14R_action": "replace", "phase14R_type": "literature-observation montage", "source_panels": 4, "scientific_change": "Morphology sequence replaces box-dominant mechanism flow."},
    {"figure_id": "FIG-05", "phase14_role": "Progression hybrid", "phase14R_action": "major redesign", "phase14R_type": "configuration comparison", "source_panels": 3, "scientific_change": "No isolated-to-cloud progression; dense HPDI target remains open."},
    {"figure_id": "FIG-06", "phase14_role": "Author-synthesis hybrid", "phase14R_action": "major redesign", "phase14R_type": "source observations plus conditional synthesis", "source_panels": 4, "scientific_change": "Vapor-layer suppression and heating promotion remain distinct."},
    {"figure_id": "FIG-07", "phase14_role": "Fixed-order chronology hybrid", "phase14R_action": "major redesign", "phase14R_type": "relative chronology plus source observations", "source_panels": 3, "scientific_change": "Signed timing and fuel order replace fixed sequence; hypothetical path separated."},
    {"figure_id": "FIG-08", "phase14_role": "Strong-wave flow hybrid", "phase14R_action": "replace", "phase14R_type": "strong-wave literature comparison", "source_panels": 4, "scientific_change": "Source observations carry the comparison; transfer boundary explicit."},
    {"figure_id": "FIG-09", "phase14_role": "Author synthesis", "phase14R_action": "retain and simplify", "phase14R_type": "author-generated synthesis", "source_panels": 0, "scientific_change": "Competing clocks separated from article-level sequence."},
]
write_csv(OUT / "figure_revision_map.csv", revision_rows, ["figure_id", "phase14_role", "phase14R_action", "phase14R_type", "source_panels", "scientific_change"])


figure_captions = r"""# Phase 14R Working Figure Captions

## FIG-01

Injector-to-ignition physical map. Injector dynamics generate a transient wave field; pilot droplets sample local pressure, density, and relative-velocity histories; liquid response produces a fragment population whose transport and thermal state condition mixture preparation and ignition. Dashed connections retain four unresolved couplings: actual pilot-droplet loading, canonical-to-dense-spray transfer, fragment-to-mixture contribution, and mixture-to-ignition response. Author synthesis based on [[CITE:B009]] [[CITE:B021]] [[CITE:C016]] [[CITE:C035]] [[CITE:C024]] [[CITE:A007]] [[CITE:A022]].

## FIG-02

Transient injector and underexpanded-wave evolution. The source panels show axial-Mach development and Mach-disk formation in B009 Fig. 8 [[CITE:B009]], steady/unsteady Mach-disk and scalar-field comparisons in B021 Figs. 18-19 [[CITE:B021]], and injector pressure build-up with jet-field response in B029 Figs. 9-11 [[CITE:B029]]. The event line is qualitative and aligns opening, pressure build-up, choking, shock-cell formation, Mach-disk appearance, overshoot, and semi-steady behavior without assigning universal times.

## FIG-03

Eulerian wave field and Lagrangian pilot-droplet loading. The relevant forcing histories are \(p[\mathbf{x}_d(t),t]\), \(\rho_g[\mathbf{x}_d(t),t]\), and \(\mathbf{u}_{\mathrm{rel}}(t)=\mathbf{u}_g[\mathbf{x}_d(t),t]-\mathbf{u}_d(t)\), together with load direction and duration. The ratio \(\tau_{\mathrm{load}}/\tau_{\mathrm{response}}\) is an organizing hypothesis rather than a universal criterion. Author synthesis based on [[CITE:B009]] [[CITE:B021]] [[CITE:C007]] [[CITE:C016]]; actual HPDI pilot-droplet histories remain unresolved.

## FIG-04

Compressible droplet morphology and breakup. High-magnification shadowgraphy resolves sheet, rim, ligament, and fine-fragment evolution (C012 Fig. 3 [[CITE:C012]]); recurrent ligament shedding is shown by C013 Fig. 15 [[CITE:C013]]; SIE and RTP morphologies are compared in C016 Fig. 6 [[CITE:C016]]; and the KHI-dominant to coupled KHI-RTI sequence in D018 Fig. 15 provides a reacting strong-wave analogue [[CITE:D018]]. These observations distinguish acceleration-driven piercing, shear-driven stripping, and capillary sheet/ligament response without implying a universal regime boundary.

## FIG-05

Configuration-dependent collective mechanisms. Tandem-droplet wake shielding is represented by C035 Fig. 5 [[CITE:C035]], parallel-droplet squeeze flow and channel closure by C036 Fig. 2 [[CITE:C036]], and shock attenuation through a droplet cloud by C033 Fig. 2 [[CITE:C033]]. The columns compare configurations and are not a temporal progression. The dashed connection to a dense polydisperse reacting HPDI spray remains open because direct validation is absent.

## FIG-06

Fragmentation and phase-change competition. C024 Fig. 7 shows fragment-cloud growth and optical disappearance [[CITE:C024]]; C026 Fig. 2 compares size- and loading-dependent small-droplet evolution [[CITE:C026]]; C031 Fig. 7 separates no-phase-change, evaporation, and condensation morphologies [[CITE:C031]]; and C032 Figs. 3-4 show temperature-dependent deformation [[CITE:C032]]. Vapor-layer or blowing effects can reduce interfacial shear, whereas heating-induced surface-tension reduction can promote deformation. Downstream transport, evaporation, and vapor redistribution remain conditional on the fragment state and residence history.

## FIG-07

Relative injection chronology and ignition response. Signed \(\Delta\mathrm{SOI}\) is defined from named pilot and main-fuel events, with fuel order and jet geometry retained. A022 Fig. 2 shows direct-injection geometry [[CITE:A022]], A026 Fig. 10 shows timing-conditioned pilot and hydrogen flame development [[CITE:A026]], and A007 Fig. 10 maps spatial-temporal interaction against natural-gas ignition delay [[CITE:A007]]. Direct timing/geometry effects are distinguished from the hypothesized wave-mediated fragment pathway.

## FIG-08

Strong-wave comparison domain. D018 Fig. 5 compares water and RP-3 breakup under detonation loading [[CITE:D018]]; D019 Figs. 8 and 12 contrast reacting detonation and matched-leading-Mach inert-shock fields [[CITE:D019]]; and D014 Fig. 16 relates wave-relative droplet groups to thermal and evaporation histories [[CITE:D014]]. Local pressure, density, slip, diameter, fragment state, and residence are transferable comparison variables, whereas reaction-zone, RDE refill, thermochemical, and device scales are domain-specific.

## FIG-09

Competing clocks and transported quantities. Injection, wave, loading, liquid-response, breakup, evaporation, mixing, and ignition clocks organize cross-scale comparisons, while pressure/density history, relative velocity, fragment state, thermal/vapor state, and mixture chemistry are the quantities transported across interfaces. Four synchronized measurements remain unresolved: actual pilot-droplet load, dense-spray collective response, fragment-to-mixture contribution, and mixture-to-ignition response. Author synthesis based on [[CITE:B009]] [[CITE:C016]] [[CITE:C035]] [[CITE:C024]] [[CITE:A007]] [[CITE:D009]].
"""
(OUT / "working_figure_captions.md").write_text(figure_captions, encoding="utf-8")


def finalize_phase14s_bundle():
    source_tables = ROOT / "08_Figures_Tables" / "phase14R" / "tables"
    for source in sorted(source_tables.glob("TAB-*.csv")):
        shutil.copy2(source, TABLES / source.name)

    # Compress grammar, not physics, in the two deliberately restructured tables.
    tab05_rows = list(csv.DictReader((TABLES / "TAB-05.csv").open(encoding="utf-8-sig")))
    tab05_fields = ["Source / domain", "Liquid / size", "Thermal state", "Loading", "Phase-change mechanism", "Dominant physical effect", "Observed response", "Applicability boundary"]
    compact05 = []
    for row in tab05_rows:
        compact05.append({
            "Source / domain": row["Source / domain"], "Liquid / size": row["Liquid / size"],
            "Thermal state": row["Thermal state"], "Loading": row["Loading"],
            "Phase-change mechanism": row["Phase-change mechanism"],
            "Dominant physical effect": f'{row["Aerodynamic effect"]}; {row["Liquid-property effect"]}',
            "Observed response": row["Observed response"], "Applicability boundary": row["Applicability boundary"],
        })
    write_csv(TABLES / "TAB-05.csv", compact05, tab05_fields)

    tab08_rows = list(csv.DictReader((TABLES / "TAB-08.csv").open(encoding="utf-8-sig")))
    tab08_fields = ["Coupling problem", "Missing observable", "Required diagnostics", "Required model capability", "Scientific significance"]
    compact08 = [{
        "Coupling problem": row["Coupling problem"], "Missing observable": row["Missing quantity"],
        "Required diagnostics": row["Required diagnostics"], "Required model capability": row["Model requirement"],
        "Scientific significance": row["Scientific significance"],
    } for row in tab08_rows]
    write_csv(TABLES / "TAB-08.csv", compact08, tab08_fields)

    integration_fields = ["item_id", "item_type", "chapter", "section_ids", "scientific_question", "what_reader_should_observe", "cross_panel_or_row_pattern", "mechanistic_interpretation", "boundary", "transition_to_next_topic", "manuscript_edit_required", "notes"]
    rows = [
        ("FIG-01","figure","CH01","S03","What is the full physical chain reviewed?","Eight linked stages from injector dynamics to ignition","Each stage passes a state to the next; open connectors mark unmeasured interfaces","Causality depends on whether transferred states persist across competing clocks","Four major couplings remain unresolved","From review scope to injector boundary conditions","yes","Author synthesis; research-gap detail moved to FIG-09"),
        ("TAB-01","table","CH01","S02","Which definitions permit valid cross-study comparison?","Pressure roles, frames, reference states, endpoints, and sign conventions","Identical symbols often encode different physical quantities","Definition completeness precedes numerical pooling","No new normalization or inferred missing values","From scope to state-specific jet evolution","yes","Placement retained after comparability problem"),
        ("FIG-02","figure","CH02","S05-S06","What does transient injector/shock adjustment look like?","Mach-disk development, steady/unsteady topology, and velocity-field evolution","The panels observe complementary stages of one adjustment, not one common nominal-pressure series","Injector area and local pressure history control downstream topology","Different nozzles, pressure definitions, and event origins prevent pooling","From transient formation to quantitative topology comparison","yes","Three exact literature panels"),
        ("TAB-02","table","CH02","S06","Why cannot the underexpanded-jet cases be pooled directly?","Pressure definition, nozzle scale, ambient state, transient stage, and available metric differ","B009 supports within-study NPR trend; B021 topology contrast; B029 event alignment","The valid comparison coordinate changes with the observable","Only definition-complete within-study values support numerical trends","From topology metrics to local liquid loading","yes","Moved after transient/semi-steady distinction"),
        ("FIG-03","figure","CH03","S08","Why does visible wave topology not equal droplet load?","Eulerian field sampled along a moving trajectory produces p[xd,t], rho[xd,t], and urel(t)","Sampled load maps to tau_load; liquid response maps to tau_response","Response depends on amplitude, direction, and duration along the trajectory","Actual HPDI pilot trajectories remain unmeasured","From forcing description to liquid response scales","yes","Core author synthesis retained"),
        ("FIG-04","figure","CH04","S10-S12","What visually distinguishes major compressible breakup mechanisms?","RTP penetration, SIE stripping, recurrent ligaments, and strong-wave fragmentation","Acceleration-, shear-, and capillary-mediated structures differ visibly","Morphology is state-conditioned and stage-dependent","Strong-wave panel is an analogue only","From governing groups to internal and interfacial mechanisms","yes","Panel/mechanism alignment corrected"),
        ("FIG-04A","figure","CH04","S11","How can thermodynamic state redirect internal wave motion?","Diverging versus converging refracted-wave histories","Changing sound-speed ratio reverses the internal-wave trajectory and focusing behavior","Thermodynamic state sets the early pressure/circulation initial condition","2-D transcritical calculation; no direct late-breakup prediction","From internal-wave initial condition to aerodynamic deformation","yes","New figure justified by frozen-corpus source"),
        ("TAB-03","table","CH04","S10","Why can response not be organized by We or Mach alone?","Mach frame, d0, Re/Oh, load duration, and endpoints vary","We co-varies with size/Re/M; Mach frames and endpoints differ","Breakup is a state-conditioned response, not a universal We-only map","Cross-domain strong-wave rows remain analogues","From parameter comparison to mechanism-specific response","yes","Moved after first Mach/We/d0 comparisons"),
        ("FIG-05","figure","CH05","S14-S16","What do distinct collective configurations look like?","Isolated, tandem, parallel, and cloud responses are configuration comparisons","Wake shielding, channel closure, and attenuation are different mechanisms","Neighbor topology changes local slip and wave momentum exchange","No direct dense reacting HPDI validation","From pair/cloud mechanisms to transfer limits","yes","Explicitly non-temporal"),
        ("TAB-04","table","CH05","S16","Which condition space belongs to each collective mechanism?","Orientation, S/D or L/D, We, cloud descriptors, and load differ","Pair spacing is not convertible to volume fraction or number density","Collective response requires configuration-specific descriptors","Dense spray joint statistics remain unresolved","From canonical configurations to dense-spray requirements","yes","Placement retained after transfer problem"),
        ("FIG-06","figure","CH06","S18-S20","How can thermal state alter breakup in opposite directions?","Overlap, weak early influence, vapor-layer suppression, and heating promotion","Branches A and B are parallel conditional routes","Vapor/blowing reduces shear while heating can weaken capillarity","No universal sign of phase-change influence","From liquid response to conditional fragment transport","yes","Branch topology corrected"),
        ("TAB-05","table","CH06","S19","Which phase-change pattern applies under which state?","Five distinct patterns across size, pressure, volatility, vapor layer, and heating","Weak early effect; volatility control; shear suppression; capillary weakening; overlap","Thermal influence depends on state and response clock","Optical disappearance is not vapor mass; models are domain-specific","From thermal mechanism to downstream fragment/vapor state","yes","Moved after thermal mechanisms; columns compressed"),
        ("FIG-07","figure","CH07","S21","How do chronology and geometry condition ignition response?","Geometry sets intersection; timing sets pilot state; maps show joint response","Where and when the streams meet jointly determine ignition","Direct controls dominate interpretation before hypothesized wave-mediated effects","No panel isolates shock-created fragments as cause","From local interaction examples to application classes","yes","Three source panels linked explicitly"),
        ("TAB-06","table","CH07","S21-S25","Which control classes organize HPDI observations?","Chronology/geometry, pressure/momentum, and local arrangement form distinct classes","Different classes govern contact state, later mixing, and rich-zone residence","No single Delta-SOI or mixing-intensity coordinate spans all cases","Platform, fuel order, oxygen, and pilot energy remain attached","From application classes to causal ignition test","yes","Moved after chronology/geometry framework"),
        ("FIG-08","figure","CH08","S26-S28","Why does leading Mach not define droplet loading?","Liquid chronology, matched-Mach contrast, thermal histories, and later divergence","Similar early wave topology leads to different post-wave p, rho, urel, gradients, and chemistry","Post-wave state and residence govern later response","Detonation/RDE remain comparison domains","From local strong-wave physics to transfer boundaries","yes","Four exact source panels"),
        ("TAB-07","table","CH08","S28","What is locally transferable and what is device-specific?","Local state variables separate from reaction-zone and refill/front scales","D009 persistence ratio and D017 closure jointly govern survival","Survival reflects product generation relative to device residence","No validated quantitative HPDI mapping","From analogue lessons to multiscale closure","yes","Moved after shared/domain-specific distinction"),
        ("FIG-09","figure","CH09","S29","Why is the physical chain not quantitatively closed?","Aligned stages, clocks, transferred states, and missing interfaces","Each missing interface aligns with a state and a clock","Closure requires synchronized measurements across successive interfaces","No universal scalar or completed causal chain","From physical gaps to research actions","yes","Role separated from FIG-01"),
        ("TAB-08","table","CH09","S30","What measurement and model resolves each missing interface?","Each coupling maps to an observable, diagnostic, capability, and significance","Priorities group into trajectory load; population/fragment/vapor; causal ignition","Research action must validate each interface before end-to-end prediction","Timescale and strong-wave mapping are supporting priorities","From prioritized research actions to conclusions","yes","Restructured to five-column action table"),
    ]
    write_csv(OUT / "scientific_integration_map.csv", [dict(zip(integration_fields, r)) for r in rows], integration_fields)

    fig_link_fields = ["figure_id","panel_id","source_panel","manuscript_section","manuscript_paragraph","observation_described","mechanistic_interpretation","citation_ids","status"]
    fig_links = []
    panel_paragraph = {"FIG-02":"S05-P2","FIG-04":"S12-P2","FIG-04A":"S11-P3","FIG-05":"S14-P4","FIG-06":"S19-P4","FIG-07":"S21-P5","FIG-08":"S28-P2"}
    for spec in PANEL_SPECS:
        panel = spec.original_panel if spec.new_figure == "FIG-04A" else chr(97 + [s for s in PANEL_SPECS if s.new_figure == spec.new_figure].index(spec))
        fig_links.append({"figure_id":spec.new_figure,"panel_id":panel,"source_panel":spec.panel_id,"manuscript_section":spec.section,"manuscript_paragraph":panel_paragraph[spec.new_figure],"observation_described":spec.phenomenon,"mechanistic_interpretation":"State- and configuration-specific evidence used in the cross-panel synthesis","citation_ids":spec.paper_id,"status":"integrated"})
    for fid, sec, para, obs in [("FIG-01","S03","S03-P1","Physical chain and open interfaces"),("FIG-03","S08","S08-P2","Trajectory sampling and paired clocks"),("FIG-09","S29","S29-P1","Aligned clocks, states, and missing interfaces")]:
        fig_links.append({"figure_id":fid,"panel_id":"whole","source_panel":"author synthesis","manuscript_section":sec,"manuscript_paragraph":para,"observation_described":obs,"mechanistic_interpretation":"Cross-scale synthesis within frozen evidence boundary","citation_ids":"see caption","status":"integrated"})
    write_csv(OUT / "figure_text_link_map.csv", fig_links, fig_link_fields)

    table_fields = ["table_id","section_id","cross_row_pattern","supporting_rows","manuscript_paragraph","scientific_conclusion","boundary","status"]
    table_rows = [
        ("TAB-01","S02","Definitions differ across pressure, Mach, dimensionless, timing, and length scales","all rows","S02-P2","Numerical comparison requires common physical roles and frames","No inferred definitions","integrated"),
        ("TAB-02","S06","Within-study NPR trend vs topology contrast vs event alignment","B009; B021; B029","S06-P3","Studies cannot share one nominal-pressure coordinate","Cross-paper pooling prohibited","integrated"),
        ("TAB-03","S10","We co-variation; Mach-frame mismatch; endpoint mismatch","C016; C025; C014; D018; D019","S10-P5","Response is state-conditioned, not We-only","Strong-wave rows are analogues","integrated"),
        ("TAB-04","S16","Pair geometry and cloud population use non-convertible descriptors","C016; C035; C036; C033/C034","S16-P3","Different collective mechanisms require different coordinates","Dense HPDI transfer unresolved","integrated"),
        ("TAB-05","S19","Five phase-change influence patterns","C026; C027; C031; C032; C024/D017","S19-P5","No universal sign of phase-change influence","Optical loss and model results remain qualified","integrated"),
        ("TAB-06","S21","Three application control classes","A007/A009/A011/A013/A020/A022/A026; A001/A002; A005","S21-P7","No single Delta-SOI or mixing coordinate organizes HPDI ignition","Fuel order and platform retained","integrated"),
        ("TAB-07","S28","Local transfer variables vs device-specific scales","D009; D014; D017; D018; D019","S28-P4","Survival couples product-generation physics to residence scale","No validated HPDI mapping","integrated"),
        ("TAB-08","S30","Three primary and two supporting research-priority tiers","rows 1-6","S30-P2-S30-P4","Measurements and models must resolve each interface in order","Causal closure remains absent","integrated"),
    ]
    write_csv(OUT / "table_text_link_map.csv", [dict(zip(table_fields, r)) for r in table_rows], table_fields)

    captions = r'''# Phase 14S Working Figure Captions

## FIG-01
Injector-to-ignition physical chain. Injector dynamics create a transient wave field; moving droplets sample local loading; liquid response creates fragments whose transport and phase change condition the mixture presented to ignition. Open connectors mark interfaces not yet measured together. Author synthesis based on [[CITE:B009]] [[CITE:B021]] [[CITE:C016]] [[CITE:C035]] [[CITE:C024]] [[CITE:A007]] [[CITE:A022]].

## FIG-02
Transient injector and shock-system evolution. (a) Axial-Mach and Mach-disk development in B009 Fig. 8 [[CITE:B009]]. (b) Steady/unsteady topology in B021 Fig. 18 [[CITE:B021]]. (c) Velocity-contour and shock-cell evolution during an injector pressure-build case in B029 Fig. 11 [[CITE:B029]]. The qualitative event line aligns complementary observations without assigning universal times.

## FIG-03
Eulerian field to Lagrangian droplet loading. The sampled histories are \(p[\mathbf{x}_d(t),t]\), \(\rho_g[\mathbf{x}_d(t),t]\), and \(\mathbf{u}_{\mathrm{rel}}(t)\). Sampled loading sets \(\tau_{\mathrm{load}}\); liquid dynamics set \(\tau_{\mathrm{response}}\). Their ratio is an organizing hypothesis only. Author synthesis based on [[CITE:B009]] [[CITE:B021]] [[CITE:C007]] [[CITE:C016]].

## FIG-04
Distinct structures under compressible droplet loading. (a) RTP morphology in C016 Fig. 6(d) and (b) SIE morphology in C016 Fig. 6(b) [[CITE:C016]]. (c) Recurrent ligament shedding in C013 Fig. 15 [[CITE:C013]]. (d) KHI-dominant to coupled KHI-RTI fragmentation in D018 Fig. 15 [[CITE:D018]]. The panels distinguish mechanism examples, not a universal regime progression.

## FIG-04A
Internal-wave refraction under two thermodynamic states. C029 Fig. 9 compares (a-c) a diverging case at 500 K and \(n=0.78\) with (d-f) a converging case at 650 K and \(n=1.8\) [[CITE:C029]]. The 2-D transcritical calculation visualizes state-dependent refraction and focusing; it is not a late-breakup regime map.

## FIG-05
Configuration-dependent collective interactions. (a) Author schematic of isolated loading. (b) Tandem-droplet response in C035 Fig. 5 [[CITE:C035]]. (c) Parallel-droplet response in C036 Fig. 2 [[CITE:C036]]. (d) Cloud transmission and pressure traces in C033 Fig. 2 [[CITE:C033]]. The columns compare configurations rather than successive times; transfer to a dense reacting HPDI spray remains open.

## FIG-06
Fragmentation and phase-change competition. (a) Fragment-cloud development in C024 Fig. 7 [[CITE:C024]]. (b) Size/loading-dependent early response in C026 Fig. 2 [[CITE:C026]]. (c) No-phase-change, evaporation, and condensation branches in C031 Fig. 7 [[CITE:C031]]. (d) Thermal response at 800 and 1000 K in C032 Figs. 3-4 [[CITE:C032]]. Vapor-layer shear suppression and heating-induced capillary weakening are parallel conditional routes.

## FIG-07
Chronology and geometry in pilot-assisted ignition. (a) H2-pilot intersection geometry in A022 Fig. 2 [[CITE:A022]]. (b) Timing-conditioned pilot and hydrogen flame development in A026 Fig. 10 [[CITE:A026]]. (c) Spatial-temporal ignition-delay response in A007 Fig. 10 [[CITE:A007]]. Together, the panels show that geometry sets where streams meet and timing sets their state at contact.

## FIG-08
Strong-wave comparison domain. (a) Liquid-dependent breakup in D018 Fig. 5 [[CITE:D018]]. (b) Matched-leading-Mach reacting/inert wave fields in D019 Fig. 8 [[CITE:D019]]. (c) Wave-relative thermal histories in D014 Fig. 16 [[CITE:D014]]. (d) Later post-wave divergence in D019 Fig. 12 [[CITE:D019]]. Local state variables support comparison; device and thermochemical scales do not transfer directly to HPDI.

## FIG-09
Aligned cross-scale closure map. Columns align physical stages with \(\tau_{\mathrm{load}}\), \(\tau_{\mathrm{response}}\), \(\tau_{\mathrm{breakup}}\), \(\tau_{\mathrm{evap}}\), \(\tau_{\mathrm{mix}}\), and \(\tau_{\mathrm{ign}}\), the states transferred between them, and four unresolved interfaces. Author synthesis based on [[CITE:B009]] [[CITE:C016]] [[CITE:C035]] [[CITE:C024]] [[CITE:A007]] [[CITE:D009]].
'''
    (OUT / "working_figure_captions.md").write_text(captions, encoding="utf-8")
    table_captions = (ROOT / "08_Figures_Tables" / "phase14R" / "working_table_captions.md").read_text(encoding="utf-8").replace("Phase 14R", "Phase 14S")
    table_captions = table_captions.replace("Phase-change competition across liquid size, thermal state, loading, interfacial aerodynamics, and temperature-dependent liquid properties.", "Phase-change competition across liquid size, thermal state, loading, dominant physical effect, and applicability boundary.")
    table_captions = table_captions.replace("Unresolved physical couplings, missing quantities, synchronized diagnostics, and model requirements for connecting transient loading to ignition response.", "Research-action table linking each unresolved coupling to its missing observable, required diagnostics, model capability, and scientific significance.")
    (OUT / "working_table_captions.md").write_text(table_captions, encoding="utf-8")


finalize_phase14s_bundle()
print(f"Generated Phase 14S integration bundle under {OUT}")
