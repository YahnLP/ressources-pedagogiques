"""Figures du parcours autonome « L'essentiel en 1 an »."""
import math
from lib import *
from figs07 import block
from hl import hrun, vrun, tbl

W = 1200


def cl(x, y, text, col=GREEN, w=None, size=17):
    w = w or (len(text) * size * 0.58 + 30)
    return chip(x + w / 2, y, text, col, w=w, size=size)


def grat(x, y, cw, nx=10, ny=8, color="#d5dce8"):
    """Quadrillage d'oscilloscope : nx x ny carreaux de cote cw."""
    o = f'<rect x="{x}" y="{y}" width="{nx*cw}" height="{ny*cw}" fill="#0f1b2f" rx="6"/>'
    for i in range(nx + 1):
        o += f'<line x1="{x+i*cw}" y1="{y}" x2="{x+i*cw}" y2="{y+ny*cw}" stroke="#2a3b57" stroke-width="{2.5 if i==nx//2 else 1.2}"/>'
    for j in range(ny + 1):
        o += f'<line x1="{x}" y1="{y+j*cw}" x2="{x+nx*cw}" y2="{y+j*cw}" stroke="#2a3b57" stroke-width="{2.5 if j==ny//2 else 1.2}"/>'
    return o


def f_oscillo_ecran():
    cw = 58; x0, y0 = 60, 96
    o = T(40, 52, "Lire l'écran d'un oscilloscope", 28, 800, INK, "start")
    o += grat(x0, y0, cw)
    cy = y0 + 4 * cw
    pts = " ".join(f"{x0 + i*3:.1f},{cy - 2*cw*math.sin(2*math.pi*i*3/(5*cw)):.1f}" for i in range(0, int(10*cw/3) + 1))
    o += f'<polyline points="{pts}" fill="none" stroke="#ffd34d" stroke-width="5" stroke-linejoin="round"/>'
    xa, xb = x0, x0 + 5 * cw
    yy = y0 + 8 * cw + 34
    o += arrow(xa, yy, xb, yy, GREEN, 4) + arrow(xb, yy, xa, yy, GREEN, 4)
    o += T((xa + xb) / 2, yy + 34, "1 période T = 5 carreaux", 19, 800, GREEN)
    xv = x0 + 10 * cw + 34
    o += arrow(xv, cy + 2 * cw, xv, cy - 2 * cw, RED, 4) + arrow(xv, cy - 2 * cw, xv, cy + 2 * cw, RED, 4)
    o += T(xv + 14, cy - 8, "Upp", 20, 800, RED, "start") + T(xv + 14, cy + 18, "4 carreaux", 17, 800, RED, "start")
    px = 840
    o += panel(px, 96, 320, 464, "Calcul", accent=BLUE)
    o += T(px + 22, 160, "Réglages lus :", 19, 800, INK, "start")
    o += cl(px + 22, 192, "2 V / DIV  (vertical)", BLUE, w=276, size=17) + cl(px + 22, 238, "2 ms / DIV  (horizontal)", BLUE, w=276, size=17)
    o += T(px + 22, 300, "Tension crête à crête", 19, 800, RED, "start") + T(px + 22, 330, "Upp = 4 × 2 V = 8 V", 20, 700, INK, "start")
    o += T(px + 22, 384, "Période", 19, 800, GREEN, "start") + T(px + 22, 414, "T = 5 × 2 ms = 10 ms", 20, 700, INK, "start")
    o += T(px + 22, 468, "Fréquence", 19, 800, AMBER, "start") + T(px + 22, 498, "f = 1 / T = 100 Hz", 20, 700, INK, "start")
    return figure(W, 650, o)


def front(x, y, w, h, titre, col=INK):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="#e9eef7" stroke="{col}" stroke-width="3"/>' + T(x + w / 2, y + 30, titre, 20, 800, col)


def knob(x, y, r, lab):
    o = f'<circle cx="{x}" cy="{y}" r="{r}" fill="#fff" stroke="{INK}" stroke-width="3"/><line x1="{x}" y1="{y}" x2="{x+r*0.7:.0f}" y2="{y-r*0.7:.0f}" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>'
    return o + T(x, y + r + 24, lab, 16, 700, MUTED)


def display(x, y, w, h, txt, col="#46e08a"):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="#0f1b2f"/>' + T(x + w / 2, y + h / 2 + 12, txt, 34, 800, col)


def f_instruments_labo():
    o = T(40, 52, "Les instruments du poste de mesure", 28, 800, INK, "start")
    # alimentation
    o += front(40, 90, 340, 330, "Alimentation de labo", BLUE)
    o += display(70, 140, 130, 62, "5.00 V") + display(210, 140, 140, 62, "0.021 A", "#ffd34d")
    o += knob(115, 270, 30, "TENSION (V)") + knob(305, 270, 30, "LIMITE (A)")
    o += f'<circle cx="80" cy="350" r="11" fill="{GREEN}"/>' + T(100, 356, "CV", 17, 800, GREEN, "start") + f'<circle cx="170" cy="350" r="11" fill="#e8c1c1"/>' + T(190, 356, "CC", 17, 800, RED, "start")
    o += f'<circle cx="270" cy="360" r="14" fill="{RED}"/><circle cx="330" cy="360" r="14" fill="{INK}"/>' + T(270, 396, "+", 18, 800, RED) + T(330, 396, "−", 18, 800, INK)
    # GBF
    o += front(410, 90, 380, 330, "Générateur de fonctions (GBF)", GREEN)
    o += display(440, 140, 320, 62, "1.000 kHz")
    for i, (nm) in enumerate(("sinus", "carré", "triangle")):
        o += f'<rect x="{445+i*105}" y="225" width="90" height="42" rx="10" fill="#fff" stroke="{GREEN}" stroke-width="3"/>' + T(490 + i * 105, 253, nm, 17, 800, GREEN)
    o += knob(500, 335, 28, "FRÉQUENCE") + knob(610, 335, 28, "AMPLITUDE") + knob(720, 335, 28, "OFFSET")
    # multimètre
    o += front(820, 90, 340, 330, "Multimètre", AMBER)
    o += display(850, 140, 280, 62, "5.02 V")
    o += f'<circle cx="990" cy="310" r="64" fill="#fff" stroke="{AMBER}" stroke-width="4"/>'
    for a, lab in ((-150, "V⎓"), (-90, "mA"), (-30, "Ω"), (30, "•))"), (90, "A"), (150, "V~")):
        r = math.radians(a); o += T(990 + 84 * math.cos(r), 316 + 84 * math.sin(r), lab, 16, 800, INK)
    o += f'<line x1="990" y1="310" x2="1040" y2="260" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>'
    # oscillo
    o += front(40, 450, 1120, 260, "Oscilloscope", INK)
    o += f'<rect x="70" y="490" width="360" height="190" rx="8" fill="#0f1b2f"/>'
    pts = " ".join(f"{70+i*3:.1f},{585-60*math.sin(i/9):.1f}" for i in range(0, 120))
    o += f'<polyline points="{pts}" fill="none" stroke="#ffd34d" stroke-width="4"/>'
    for i, (lab) in enumerate(("VOLT/DIV", "SEC/DIV", "TRIGGER (niveau)", "POSITION")):
        o += knob(520 + i * 150, 560, 30, lab)
    for i, lab in enumerate(("AUTOSET", "RUN/STOP", "MEASURE", "CURSOR")):
        o += f'<rect x="{480+i*140}" y="635" width="120" height="36" rx="8" fill="#fff" stroke="{INK}" stroke-width="2.5"/>' + T(540 + i * 140, 659, lab, 15, 800, INK)
    o += T(1080, 520, "CH1", 20, 800, "#c99a00") + f'<circle cx="1080" cy="560" r="22" fill="#fff" stroke="{INK}" stroke-width="4"/><circle cx="1080" cy="560" r="8" fill="{INK}"/>'
    o += T(1080, 620, "CH2", 20, 800, "#1b9bb5") + f'<circle cx="1080" cy="660" r="22" fill="#fff" stroke="{INK}" stroke-width="4"/><circle cx="1080" cy="660" r="8" fill="{INK}"/>'
    return figure(W, 740, o)


def f_mesure_v_a():
    o = panel(30, 30, 560, 430, "Mesurer une TENSION : en parallèle", accent=BLUE)
    o += hrun(150, 90, 520, [(300, "R", "R1", {})]) + vrun(90, 150, 400, [(275, "BAT", "", {})], 1, 0) + s_wire([(520, 150), (520, 400)]) + s_wire([(90, 400), (520, 400)])
    o += s_wire([(260, 150), (260, 235)]) + s_wire([(340, 150), (340, 235)]) + dot(260, 150) + dot(340, 150) + sym("VM", 300, 235)
    o += s_wire([(260, 235), (260, 235)]) 
    o += cl(140, 320, "voltmètre branché AUX BORNES de R1", BLUE, w=370, size=16)
    o += T(325, 366, "le circuit n'est pas ouvert", 17, 600, MUTED)
    o += panel(610, 30, 560, 430, "Mesurer un COURANT : en série", accent=GREEN)
    o += hrun(150, 670, 1100, [(790, "AM", "", {}), (960, "R", "R1", {})]) + vrun(670, 150, 400, [(275, "BAT", "", {})], 1, 0) + s_wire([(1100, 150), (1100, 400)]) + s_wire([(670, 400), (1100, 400)])
    o += T(790, 100, "ampèremètre", 18, 800, GREEN)
    o += cl(720, 320, "inséré DANS le circuit : on l'ouvre", GREEN, w=370, size=16)
    o += T(905, 366, "jamais en parallèle (court-circuit)", 17, 700, RED)
    return figure(W, 490, o)


def f_alim_cv_cc():
    o = panel(30, 30, 1140, 450, "Alimentation de labo : modes CV et CC", accent=BLUE)
    x0, y0, w, h = 150, 130, 640, 280
    o += f'<line x1="{x0}" y1="{y0+h}" x2="{x0+w}" y2="{y0+h}" stroke="{INK}" stroke-width="3" marker-end="url(#arr)"/><line x1="{x0}" y1="{y0+h}" x2="{x0}" y2="{y0-10}" stroke="{INK}" stroke-width="3" marker-end="url(#arr)"/>'
    o += T(x0 + w, y0 + h + 32, "courant demandé I", 17, 700, INK, "end") + T(x0 + 12, y0 - 22, "tension de sortie U", 17, 700, INK, "start")
    ilim = 430
    o += f'<path d="M{x0},{y0+40} H{ilim} L{ilim+55},{y0+h}" fill="none" stroke="{BLUE}" stroke-width="7" stroke-linejoin="round"/>'
    o += f'<line x1="{ilim}" y1="{y0+10}" x2="{ilim}" y2="{y0+h}" stroke="{RED}" stroke-width="3" stroke-dasharray="8 6"/>' + T(ilim, y0 - 2, "limite de courant", 17, 800, RED)
    o += cl(x0 + 30, y0 + 85, "CV : tension constante", GREEN, w=250, size=17) + cl(ilim + 70, y0 + 160, "CC : courant limité", RED, w=210, size=17) + T(ilim + 175, y0 + 198, "la tension chute", 16, 700, RED)
    o += T(850, 190, "Exemple : 5 V, limite 30 mA", 20, 800, INK, "start")
    o += T(850, 240, "R = 220 Ω : 22,7 mA", 18, 600, INK, "start") + T(850, 266, "→ mode CV, U = 5 V", 18, 800, GREEN, "start")
    o += T(850, 320, "R = 100 Ω : 50 mA demandés", 18, 600, INK, "start") + T(850, 346, "→ mode CC, 30 mA, U = 3 V", 18, 800, RED, "start")
    return figure(W, 510, o)


def f_serie_parallele():
    o = panel(30, 30, 560, 400, "Résistances en SÉRIE", accent=BLUE)
    o += hrun(160, 70, 550, [(230, "R", "R1", {}), (400, "R", "R2", {})])
    o += T(310, 250, "même courant dans toutes", 19, 600, MUTED) + T(310, 310, "Rₑq = R1 + R2", 30, 800, INK)
    o += T(310, 360, "100 Ω + 220 Ω = 320 Ω", 20, 700, BLUE)
    o += panel(610, 30, 560, 400, "Résistances en PARALLÈLE", accent=GREEN)
    o += s_wire([(650, 230), (700, 230), (700, 150), (1090, 150)]) + s_wire([(700, 230), (700, 310), (1090, 310)]) + dot(700, 230)
    o += sym("R", 880, 150) + sym("R", 880, 310)
    o += s_wire([(1090, 150), (1090, 310)]) + s_wire([(1090, 230), (1140, 230)]) + dot(1090, 230)
    o += T(880, 112, "R1", 20, 800, INK) + T(880, 272, "R2", 20, 800, INK)
    o += T(890, 355, "même tension aux bornes", 19, 600, MUTED) + T(890, 392, "1/Rₑq = 1/R1 + 1/R2 ;  100 ∥ 220 ≈ 68,8 Ω", 19, 800, GREEN)
    return figure(W, 460, o)


def f_diviseur():
    o = panel(30, 30, 1140, 430, "Le pont diviseur de tension", accent=BLUE)
    o += T(320, 112, "+12 V", 22, 800, RED) + s_wire([(320, 124), (320, 150)], RED)
    o += vrun(320, 150, 390, [(210, "R", "R1 = 10 kΩ", {}), (320, "R", "R2 = 4,7 kΩ", {})], 1, 56)
    o += gnd(320, 390)
    o += dot(320, 265) + s_wire([(320, 265), (520, 265)], BLUE) + chip(565, 265, "Vs", BLUE, w=90, size=22)
    o += T(760, 190, "Vs = Vcc × R2 / (R1 + R2)", 26, 800, INK, "start")
    o += T(760, 240, "Vs = 12 × 4,7 / (10 + 4,7)", 22, 700, MUTED, "start") + T(760, 290, "Vs ≈ 3,84 V", 28, 800, GREEN, "start")
    o += cl(760, 350, "Usage : abaisser une tension (5 V → 3,3 V)", AMBER, w=380, size=17)
    return figure(W, 490, o)


def f_aop():
    o = panel(30, 30, 1140, 470, "Amplificateur opérationnel : montage non inverseur", accent=BLUE)
    o += f'<polygon points="470,160 470,340 640,250" fill="#fff" stroke="{INK}" stroke-width="4" stroke-linejoin="round"/>'
    o += T(488, 210, "+", 30, 800, INK, "start") + T(488, 316, "−", 32, 800, INK, "start")
    o += s_wire([(260, 200), (470, 200)]) + T(240, 207, "Ve", 22, 800, BLUE, "end")
    o += s_wire([(640, 250), (820, 250)]) + dot(720, 250) + T(836, 257, "Vs", 22, 800, GREEN, "start")
    o += s_wire([(470, 300), (390, 300)]) + dot(390, 300)
    o += s_wire([(390, 300), (390, 120), (500, 120)]) + sym("R", 540, 120) + s_wire([(580, 120), (720, 120), (720, 250)])
    o += T(540, 168, "Rf = 10 kΩ", 19, 800, INK)
    o += s_wire([(390, 300), (390, 350)]) + vrun(390, 300, 450, [(390, "R", "Rg = 1 kΩ", {})], 1, 56)[0:0] + sym("R", 390, 390, rot=90) + T(430, 396, "Rg = 1 kΩ", 19, 800, INK, "start") + s_wire([(390, 430), (390, 450)]) + gnd(390, 450)
    o += T(900, 150, "Gain  G = 1 + Rf / Rg", 26, 800, INK, "start") + T(900, 200, "G = 1 + 10 / 1 = 11", 24, 800, GREEN, "start")
    o += T(900, 280, "Ve = 100 mV → Vs = 1,1 V", 20, 700, INK, "start")
    o += T(900, 330, "La sortie ne dépasse", 18, 700, RED, "start") + T(900, 356, "jamais l'alimentation.", 18, 700, RED, "start")
    return figure(W, 520, o)


def f_relais_transistor():
    o = panel(30, 30, 1140, 500, "Commander un relais avec un transistor", accent=BLUE)
    o += T(420, 112, "+5 V", 22, 800, RED) + s_wire([(420, 124), (420, 170)], RED)
    o += f'<rect x="385" y="170" width="70" height="100" rx="8" fill="#fff" stroke="{INK}" stroke-width="3.5"/>' + T(420, 228, "K1", 22, 800, INK)
    o += T(360, 215, "bobine du relais", 16, 600, MUTED, "end")
    o += s_wire([(420, 270), (420, 320)])
    o += s_wire([(420, 170), (540, 170), (540, 210)]) + sym("D", 540, 250, rot=270) + s_wire([(540, 290), (540, 320), (420, 320)])
    o += dot(420, 320) + T(590, 255, "diode de roue libre", 18, 800, RED, "start")
    o += npn(398, 380, 1.0) + s_wire([(420, 320), (420, 336)])
    o += s_wire([(420, 424), (420, 470)]) + gnd(420, 470)
    o += s_wire([(348, 380), (310, 380)]) + sym("R", 270, 380) + s_wire([(230, 380), (190, 380)])
    o += T(270, 342, "Rb = 560 Ω", 18, 800, INK) + T(180, 387, "5 V", 20, 800, BLUE, "end")
    o += T(760, 170, "Pourquoi la diode ?", 24, 800, INK, "start")
    o += T(760, 212, "À la coupure, la bobine produit un pic", 18, 600, MUTED, "start") + T(760, 238, "de tension qui détruirait le transistor.", 18, 600, MUTED, "start")
    o += T(760, 284, "La diode absorbe ce pic.", 18, 800, GREEN, "start")
    o += cl(760, 350, "Rb = (5 − 0,7) / (I_C / 10)", BLUE, w=340, size=18) + cl(760, 402, "Bobine 70 mA → BC337 (800 mA max)", AMBER, w=360, size=16)
    return figure(W, 560, o)


def f_rc_bode():
    o = panel(30, 30, 1140, 440, "Filtre RC passe-bas : gain en fonction de la fréquence", accent=BLUE)
    x0, y0, w, h = 150, 100, 700, 280
    o += f'<line x1="{x0}" y1="{y0+h}" x2="{x0+w}" y2="{y0+h}" stroke="{INK}" stroke-width="3" marker-end="url(#arr)"/><line x1="{x0}" y1="{y0+h}" x2="{x0}" y2="{y0-6}" stroke="{INK}" stroke-width="3" marker-end="url(#arr)"/>'
    o += T(x0 + w, y0 + h + 32, "fréquence (échelle logarithmique)", 16, 700, INK, "end") + T(x0 - 8, y0 - 14, "Us / Ue", 17, 700, INK, "start")
    pts = []
    for i in range(0, 141):
        lf = -1 + i * 0.03 * 1.0  # log10(f/fc) de -1 à 3.2
        r = 10 ** lf; g = 1 / math.sqrt(1 + r * r)
        pts.append(f"{x0 + 20 + i*4.6:.1f},{y0 + h - g*(h-20):.1f}")
    o += f'<polyline points="{" ".join(pts)}" fill="none" stroke="{BLUE}" stroke-width="6" stroke-linejoin="round"/>'
    xc = x0 + 20 + 33 * 4.6; yc = y0 + h - 0.707 * (h - 20)
    o += f'<circle cx="{xc}" cy="{yc}" r="9" fill="{RED}"/>' + T(xc + 16, yc - 16, "fc : 70,7 %", 18, 800, RED, "start")
    for yv, lab in ((1.0, "1"), (0.707, "0,707"), (0.1, "0,1")):
        o += T(x0 - 10, y0 + h - yv * (h - 20) + 6, lab, 15, 700, MUTED, "end") + f'<line x1="{x0}" y1="{y0+h-yv*(h-20):.0f}" x2="{x0+w}" y2="{y0+h-yv*(h-20):.0f}" stroke="#d5dce8" stroke-dasharray="6 6"/>'
    o += T(900, 150, "fc = 1 / (2π R C)", 26, 800, INK, "start") + T(900, 196, "R = 10 kΩ, C = 100 nF", 19, 600, MUTED, "start") + T(900, 238, "fc ≈ 159 Hz", 26, 800, GREEN, "start")
    o += T(900, 300, "Les basses fréquences passent,", 18, 600, INK, "start") + T(900, 326, "les hautes sont atténuées.", 18, 600, INK, "start")
    return figure(W, 500, o)


def f_ne555_chrono():
    o = panel(30, 30, 1140, 520, "NE555 en astable : charge, décharge, sortie", accent=BLUE)
    x0 = 190
    ch, dc = 250, 140
    def lvl(y, lab, col): return f'<line x1="{x0}" y1="{y}" x2="{x0+ch*2+dc*2+40}" y2="{y}" stroke="{col}" stroke-dasharray="7 7"/>' + T(x0 - 12, y + 6, lab, 16, 800, col, "end")
    o += T(60, 112, "Tension sur C", 19, 800, BLUE, "start") + lvl(150, "2/3 Vcc", RED) + lvl(260, "1/3 Vcc", GREEN)
    pts = []; x = x0
    for k in range(2):
        for i in range(0, ch + 1, 5): pts.append((x + i, 260 - 110 * (1 - math.exp(-i / 120)) / (1 - math.exp(-ch / 120))))
        x += ch
        for i in range(0, dc + 1, 5): pts.append((x + i, 150 + 110 * (1 - math.exp(-i / 70)) / (1 - math.exp(-dc / 70))))
        x += dc
    o += f'<polyline points="{" ".join(f"{a:.1f},{b:.1f}" for a,b in pts)}" fill="none" stroke="{BLUE}" stroke-width="5" stroke-linejoin="round"/>'
    o += T(60, 332, "Sortie (broche 3)", 19, 800, GREEN, "start")
    d2 = f"M{x0},440"; cur = x0
    for k in range(2):
        d2 += f" L{cur},370 L{cur+ch},370 L{cur+ch},440 L{cur+ch+dc},440"; cur += ch + dc
    o += f'<path d="{d2}" fill="none" stroke="{GREEN}" stroke-width="6" stroke-linejoin="round"/>'
    o += T(x0 + ch / 2, 360, "état haut", 17, 800, GREEN) + T(x0 + ch + dc / 2, 466, "état bas", 17, 800, RED)
    o += cl(60, 500, "t haut = 0,693 (Ra + Rb) C", GREEN, w=330, size=16) + cl(410, 500, "t bas = 0,693 Rb C", RED, w=250, size=16) + cl(680, 500, "f = 1,44 / ((Ra + 2Rb) C)", BLUE, w=320, size=16)
    return figure(W, 580, o)


def f_marges():
    o = panel(30, 30, 1140, 470, "Conformité : on compare TOUTE la plage « valeur ± marge » à la tolérance", accent=BLUE)
    x0, w = 300, 800
    vmin, vmax = 4.6, 5.5
    def X(v): return x0 + (v - vmin) / (vmax - vmin) * w
    o += T((X(4.75) + X(5.25)) / 2, 112, "tolérance : 5 V ± 5 %  →  de 4,75 V à 5,25 V", 18, 800, GREEN)
    cases = [("Conforme", 5.02, 0.05, GREEN), ("Non garanti", 5.20, 0.08, AMBER), ("Non conforme", 5.40, 0.05, RED)]
    for i, (lab, v, m, col) in enumerate(cases):
        y = 190 + i * 100
        o += f'<rect x="{X(4.75)}" y="{y-30}" width="{X(5.25)-X(4.75)}" height="60" rx="8" fill="#e6f5ee" stroke="{GREEN}" stroke-width="2.5" stroke-dasharray="8 6"/>'
        o += f'<line x1="{X(v-m)}" y1="{y}" x2="{X(v+m)}" y2="{y}" stroke="{col}" stroke-width="9" stroke-linecap="round"/><circle cx="{X(v)}" cy="{y}" r="10" fill="{col}"/>'
        o += cl(60, y, lab, col, w=190, size=17)
        o += T(X(v), y - 40, f"({v:.2f} ± {m:.2f}) V".replace(".", ","), 16, 800, col)
    return figure(W, 530, o)


def f_station():
    o = T(40, 52, "Fil rouge n°2 : la station de mesure communicante", 28, 800, INK, "start")
    xs = [40, 270, 500, 730, 960]
    items = [("Capteur", "LM35 : 10 mV/°C", BLUE), ("Microcontrôleur", "ADC 10 bits, programme", GREEN), ("Liaison", "UART, I²C, WiFi", AMBER), ("Broker MQTT", "topic salle1/temperature", "#8a56d0"), ("Supervision", "tableau, alarme", RED)]
    for x, (t, s, c) in zip(xs, items):
        o += block(x, 120, 200, 130, t, s, c)
    for a, b in zip(xs[:-1], xs[1:]):
        o += arrow(a + 205, 185, b - 5, 185, INK, 4)
    o += T(140, 290, "0 à 5 V", 17, 700, MUTED) + T(370, 290, "0 à 1023 → °C", 17, 700, MUTED) + T(600, 290, "trames, JSON", 17, 700, MUTED) + T(830, 290, "publish / subscribe", 17, 700, MUTED)
    return figure(W, 330, o)


def f_parcours():
    o = T(40, 52, "Le parcours : 13 semaines de formation + 1 semaine pour l'épreuve", 28, 800, INK, "start")
    sem = [("1", "Bases : composants,\nloi d'Ohm, sécurité", BLUE), ("2", "Mesurer (1) :\nmultimètre, alimentation", BLUE), ("3", "Mesurer (2) :\ngénérateur, oscilloscope", BLUE),
           ("4", "Schéma, datasheet,\nplaque d'essai", GREEN), ("5", "Souder et contrôler\nla qualité (IPC, ESD)", GREEN), ("6", "Alimenter un\nmontage", AMBER),
           ("7", "Commander des\ncharges", AMBER), ("8", "Microcontrôleur\net capteurs", "#0e9aa7"), ("9", "Filtrer, amplifier,\ndécider", "#0e9aa7"),
           ("10", "Communication\net supervision", "#8a56d0"), ("11", "Du schéma\nau PCB", "#8a56d0"), ("12", "Du PCB à la\ncarte soudée", "#8a56d0"),
           ("13", "Mesurer, valider,\ndépanner, documenter", RED), ("14", "L'épreuve E2 :\ncomprendre et réussir", INK)]
    for i, (n, t, c) in enumerate(sem):
        x = 40 + (i % 3) * 380; y = 100 + (i // 3) * 118
        o += f'<rect x="{x}" y="{y}" width="360" height="100" rx="14" fill="#fff" stroke="{c}" stroke-width="3.5"/><rect x="{x}" y="{y}" width="70" height="100" rx="14" fill="{c}"/>' + T(x + 35, y + 62, n, 32, 800, "#fff")
        for k, ln in enumerate(t.split("\n")):
            o += T(x + 86, y + 42 + k * 28, ln, 18, 800, INK, "start")
    return figure(W, 100 + 5 * 118 + 20, o)


def f_epreuve():
    o = T(40, 52, "L'épreuve E2 : ce qui est évalué", 28, 800, INK, "start")
    comp = [("C03", "Participer à un projet", "planning, documentation,\ntravail en équipe", BLUE), ("C07", "Réaliser maquettes et prototypes", "monter, souder, mesurer,\nrouter, fabriquer", GREEN), ("C11", "Maintenir un système électronique", "diagnostiquer, réparer,\nrenseigner la fiche", RED)]
    for i, (c, t, sub, col) in enumerate(comp):
        x = 40 + i * 380
        o += f'<rect x="{x}" y="100" width="350" height="230" rx="16" fill="#fff" stroke="{col}" stroke-width="4"/><rect x="{x}" y="100" width="350" height="64" rx="16" fill="{col}"/>' + T(x + 175, 142, c, 30, 800, "#fff")
        o += T(x + 175, 205, t, 18, 800, INK) + T(x + 175, 252, sub, 17, 600, MUTED)
    o += cl(40, 375, "Coefficient 5", BLUE, w=170, size=18) + cl(230, 375, "Contrôle en cours de formation ou épreuve pratique de 3 h", GREEN, w=690, size=18)
    return figure(W, 440, o)


def f_tension_panne():
    o = panel(30, 30, 1140, 540, "Dépanner : points de mesure et tensions attendues", accent=RED)
    o += T(520, 112, "+5 V", 22, 800, RED) + s_wire([(520, 124), (520, 150)], RED)
    o += sym("R", 520, 190, rot=90) + T(470, 196, "Rc = 150 Ω", 17, 800, INK, "end") + s_wire([(520, 230), (520, 258)])
    o += sym("LED", 520, 298, rot=90) + T(470, 304, "LED", 17, 800, INK, "end") + s_wire([(520, 338), (520, 366)])
    o += npn(498, 410, 1.0) + s_wire([(520, 454), (520, 490)]) + gnd(520, 490)
    o += s_wire([(448, 410), (390, 410)]) + sym("R", 350, 410) + T(350, 372, "Rb = 10 kΩ", 17, 800, INK) + s_wire([(310, 410), (260, 410)])
    for x, y, l in ((590, 150, "A"), (590, 258, "B"), (590, 366, "C"), (420, 360, "D"), (262, 372, "E")):
        o += f'<circle cx="{x}" cy="{y}" r="17" fill="{RED}"/>' + T(x, y + 7, l, 19, 800, "#fff")
    o += s_wire([(520, 150), (573, 150)], RED) if False else ""
    o += tbl(660, 110, [170, 130, 170], ["Point", "Attendu", "Mesuré (panne)"], [["A  (+5 V)", "5,0 V", "5,0 V"], ["B  (après Rc)", "≈ 2,2 V", "5,0 V"], ["C  (collecteur)", "≈ 0,2 V", "5,0 V"], ["D  (base)", "≈ 0,7 V", "0 V"], ["E  (entrée Rb)", "5,0 V", "5,0 V"]], rh=54, fs=16)
    o += cl(660, 470, "1ʳᵉ valeur anormale : D → Rb coupée", AMBER, w=470, size=17)
    return figure(W, 600, o)


def _wave(x, y, w, h, fn, col, n=120, sw=5):
    """Trace fn(t) (t de 0 a 1, valeur de -1 a 1) dans une boite (x,y,w,h)."""
    pts = " ".join(f"{x + w*i/n:.1f},{y + h/2 - fn(i/n)*h/2:.1f}" for i in range(n + 1))
    return f'<polyline points="{pts}" fill="none" stroke="{col}" stroke-width="{sw}" stroke-linejoin="round"/>'


def f_alim_secteur():
    o = panel(30, 30, 1140, 560, "De la prise de courant au 5 V : la chaîne d'alimentation", accent=BLUE)
    xs = [60, 340, 620, 900]
    noms = [("Transformateur", "230 V → 12 V"), ("Redressement", "pont de 4 diodes"), ("Filtrage", "condensateur"), ("Régulation", "7805")]
    cols = [BLUE, AMBER, GREEN, RED]
    for i, (x, (n, sub)) in enumerate(zip(xs, noms)):
        o += f'<rect x="{x}" y="100" width="220" height="110" rx="14" fill="#fff" stroke="{cols[i]}" stroke-width="4"/>'
        o += T(x + 110, 150, n, 23, 800, cols[i]) + T(x + 110, 182, sub, 17, 600, MUTED)
        if i < 3:
            o += arrow(x + 224, 155, x + 276, 155, INK, 4)
    # formes d'onde sous chaque bloc
    legs = ["Alternatif 12 V (valeur efficace)", "Redressé : que des « bosses »", "Lissé, avec une ondulation", "Continu stable : 5 V"]
    wf = [
        lambda t: math.sin(2 * math.pi * 2 * t),
        lambda t: abs(math.sin(2 * math.pi * 2 * t)) * 2 - 1,
        lambda t: 0.30 + 0.62 * max(abs(math.sin(math.pi * ((t * 4) % 1))), math.exp(-(((t * 4) % 1) - 0.5) * 1.5) if ((t * 4) % 1) > 0.5 else 0),
        lambda t: 0.1,
    ]
    for i, x in enumerate(xs):
        o += f'<rect x="{x}" y="250" width="220" height="190" rx="10" fill="#0f1b2f"/>'
        o += f'<line x1="{x+8}" y1="345" x2="{x+212}" y2="345" stroke="#2a3b57" stroke-width="2"/>'
        o += _wave(x + 10, 262, 200, 166, wf[i], "#ffd34d", sw=4.5)
        o += T(x + 110, 475, legs[i], 15.5, 700, INK)
    o += cl(60, 520, "Tension de crête = 12 × √2 ≈ 17 V", BLUE, w=330, size=16)
    o += cl(420, 520, "Perte dans le pont : environ 1,4 V", AMBER, w=330, size=16)
    o += cl(780, 520, "ΔU ≈ I / (100 Hz × C)", GREEN, w=300, size=16)
    return figure(W, 620, o)


def f_pont_h():
    o = panel(30, 30, 1140, 520, "Pont en H : deux sens de rotation", accent=BLUE)
    def pont(x0, sens, titre, col):
        r = ""
        r += T(x0 + 240, 100, titre, 22, 800, col)
        xl, xr = x0 + 100, x0 + 380
        r += T(x0 + 240, 138, "+V moteur", 17, 800, RED) + s_wire([(xl, 150), (xr, 150)], RED)
        r += s_wire([(xl, 150), (xl, 190)], RED) + s_wire([(xr, 150), (xr, 190)], RED)
        ct = {"S1": (xl, 220), "S2": (xr, 220), "S3": (xl, 380), "S4": (xr, 380)}
        ferm = {"S1", "S4"} if sens == 1 else {"S2", "S3"}
        for k, (cx, cy) in ct.items():
            on = k in ferm
            r += s_wire([(cx, 190), (cx, 220 - 40)] if cy == 220 else [(cx, 340 - 0), (cx, 380 - 40)], INK) if False else ""
            r += sym("SW", cx, cy, rot=90, closed=on, color=(GREEN if on else MUTED))
            r += T(cx - 56 if cx == xl else cx + 56, cy + 7, k, 20, 800, GREEN if on else MUTED)
        r += s_wire([(xl, 190), (xl, 180)]) 
        r += s_wire([(xl, 260), (xl, 300)]) + s_wire([(xr, 260), (xr, 300)])
        r += s_wire([(xl, 300), (xl, 340)]) + s_wire([(xr, 300), (xr, 340)])
        r += s_wire([(xl, 300), (xl + 100, 300)]) + sym("MOTOR", x0 + 240, 300, rot=0, s=1.3) + s_wire([(xr - 100, 300), (xr, 300)])
        r += s_wire([(xl, 420), (xl, 460)]) + s_wire([(xr, 420), (xr, 460)]) + s_wire([(xl, 460), (xr, 460)]) + gnd(x0 + 240, 460)
        # trajet du courant
        if sens == 1:
            path = [(xl, 190), (xl, 300), (xr, 300), (xr, 460)]
        else:
            path = [(xr, 190), (xr, 300), (xl, 300), (xl, 460)]
        pts = " ".join(f"{a},{b}" for a, b in path)
        r += f'<polyline points="{pts}" fill="none" stroke="{col}" stroke-width="7" stroke-dasharray="14 9" stroke-linejoin="round" opacity="0.8"/>'
        return r
    o += pont(60, 1, "Sens 1 : S1 et S4 fermés", GREEN)
    o += pont(600, 2, "Sens 2 : S2 et S3 fermés", BLUE)
    o += T(600, 520, "Jamais S1 et S3 (ou S2 et S4) fermés ensemble : court-circuit de l'alimentation !", 18, 800, RED)
    return figure(W, 580, o)


def f_comparateur():
    o = panel(30, 30, 1140, 520, "Comparateur : la sortie dit « au-dessus » ou « en dessous » du seuil", accent=BLUE)
    o += f'<polygon points="140,220 140,360 260,290" fill="#fff" stroke="{INK}" stroke-width="4" stroke-linejoin="round"/>'
    o += T(155, 252, "+", 26, 800, INK, "start") + T(155, 338, "−", 28, 800, INK, "start")
    o += s_wire([(60, 245), (140, 245)]) + T(52, 252, "Ve", 20, 800, BLUE, "end")
    o += s_wire([(60, 335), (140, 335)]) + T(52, 342, "Vref", 20, 800, RED, "end")
    o += s_wire([(260, 290), (330, 290)]) + T(342, 297, "Vs", 20, 800, GREEN, "start")
    o += T(200, 440, "Vref = 2,5 V (diviseur 2 × 10 kΩ)", 17, 700, MUTED)
    x0, w = 440, 680
    o += f'<rect x="{x0}" y="90" width="{w}" height="190" rx="10" fill="#0f1b2f"/>'
    o += f'<rect x="{x0}" y="310" width="{w}" height="130" rx="10" fill="#0f1b2f"/>'
    tri = lambda t: 1 - 4 * abs(((t * 2) % 1) - 0.5)
    o += _wave(x0 + 10, 100, w - 20, 170, lambda t: tri(t), "#ffd34d")
    o += f'<line x1="{x0}" y1="185" x2="{x0+w}" y2="185" stroke="{RED}" stroke-width="3.5" stroke-dasharray="10 7"/>' + T(x0 + w - 8, 176, "seuil Vref", 17, 800, RED, "end")
    o += T(x0 + 14, 112, "Ve", 18, 800, "#ffd34d", "start")
    sq = lambda t: 0.8 if tri(t) > 0 else -0.8
    o += _wave(x0 + 10, 320, w - 20, 110, sq, "#46e08a")
    o += T(x0 + 14, 340, "Vs", 18, 800, "#46e08a", "start")
    o += T(x0 + w / 2, 490, "Ve > Vref → Vs haut  |  Ve < Vref → Vs bas", 20, 800, INK)
    return figure(W, 580, o)


FIGS = {"ess_oscillo_ecran": f_oscillo_ecran, "ess_instruments_labo": f_instruments_labo, "ess_mesure_v_a": f_mesure_v_a, "ess_alim_cv_cc": f_alim_cv_cc,
        "ess_serie_parallele": f_serie_parallele, "ess_diviseur": f_diviseur, "ess_aop": f_aop, "ess_relais_transistor": f_relais_transistor, "ess_rc_bode": f_rc_bode,
        "ess_ne555_chrono": f_ne555_chrono, "ess_marges": f_marges, "ess_station": f_station, "ess_parcours": f_parcours, "ess_epreuve": f_epreuve, "ess_tension_panne": f_tension_panne,
        "ess_alim_secteur": f_alim_secteur, "ess_pont_h": f_pont_h, "ess_comparateur": f_comparateur}
