from lib import *

W = 1200


def graph(x, y, w, h, xlabel, ylabel, color=BLUE):
    return (f'<line x1="{x}" y1="{y+h/2}" x2="{x+w}" y2="{y+h/2}" stroke="{INK}" stroke-width="2.5"/>'
            f'<line x1="{x}" y1="{y}" x2="{x}" y2="{y+h}" stroke="{INK}" stroke-width="2.5"/>'
            + T(x + w, y + h / 2 + 24, xlabel, 15, 700, INK, "end") + T(x + 6, y - 8, ylabel, 15, 700, INK, "start"))


def f_dc_ac():
    o = panel(30, 40, 560, 440, "Courant continu (DC)", accent=GREEN) + panel(610, 40, 560, 440, "Courant alternatif (AC)", accent=BLUE)
    o += g(130, 180, battery_9v(), .9) + T(130, 285, "pile · batterie · USB", 16, 600, MUTED)
    o += graph(230, 110, 310, 220, "t", "U (V)")
    o += f'<line x1="230" y1="165" x2="540" y2="165" stroke="{GREEN}" stroke-width="6" stroke-linecap="round"/>' + T(215, 170, "9 V", 17, 800, GREEN, "end")
    o += T(310, 385, "tension constante :\\nle sens du courant ne change pas".replace("\\n", "\n"), 18, 600, INK)
    o += g(710, 180, wall_socket(), .9) + T(710, 270, "prise secteur", 16, 600, MUTED)
    o += graph(800, 110, 340, 220, "t (ms)", "U (V)")
    o += f'<path d="{sine_path(800, 220, 340, 90, 1.5)}" fill="none" stroke="{BLUE}" stroke-width="5" stroke-linecap="round"/>'
    o += f'<line x1="800" y1="130" x2="1140" y2="130" stroke="{MUTED}" stroke-dasharray="6 6" stroke-width="2"/>' + T(790, 135, "325 V", 16, 800, INK, "end")
    o += arrow(800, 332, 1000, 332, AMBER, 4) + arrow(1000, 332, 800, 332, AMBER, 4) + T(900, 358, "T = 20 ms (f = 50 Hz)", 17, 800, AMBER)
    o += T(890, 395, "Valeur efficace : 230 V (crête ≈ 325 V)", 17, 700, INK)
    o += T(890, 430, "tension qui alterne : le sens du courant change", 18, 600, INK)
    return figure(W, 520, o)


def dial_label(kind, x, y):
    if kind == "OFF":
        return T(x, y + 6, "OFF", 17, 800, "#7a1d1d")
    if kind == "VDC":
        return T(x - 6, y + 7, "V", 20, 800, "#222") + dc_sym(x + 12, y - 5, "#222", 16)
    if kind == "VAC":
        return T(x - 6, y + 7, "V", 20, 800, "#222") + ac_sym(x + 12, y - 2, "#222")
    if kind == "OHM":
        return T(x, y + 7, "Ω", 22, 800, "#222")
    if kind == "BUZ":
        return T(x, y + 6, "•)))", 18, 800, "#222")
    if kind == "ADC":
        return T(x - 6, y + 7, "A", 20, 800, "#222") + dc_sym(x + 12, y - 5, "#222", 16)
    return ""


def multimeter(highlight=None, probes=True):
    o = '<g filter="url(#sh)"><rect x="-125" y="-250" width="250" height="500" rx="30" fill="url(#yellow)" stroke="#b78300" stroke-width="3"/></g>'
    o += '<rect x="-108" y="-232" width="216" height="122" rx="14" fill="#2a2d33"/>'
    o += '<rect x="-92" y="-218" width="184" height="84" rx="6" fill="#cfe3c4"/>'
    o += T(70, -165, "12.34", 54, 700, "#1d2a1a", "end", extra='font-family="monospace"')
    o += T(-84, -196, "DC", 14, 800, "#1d2a1a", "start") + T(88, -196, "V", 16, 800, "#1d2a1a", "end")
    o += '<circle cx="0" cy="-8" r="62" fill="url(#knob)" stroke="#111" stroke-width="3"/>'
    o += '<path d="M0,-8 L-34,-40" stroke="#fff" stroke-width="6" stroke-linecap="round"/><circle cx="0" cy="-8" r="9" fill="#e9eaee"/>'
    for kind, ang in (("OFF", -140), ("VAC", -100), ("VDC", -57), ("OHM", -15), ("BUZ", 28), ("ADC", 75)):
        a = math.radians(ang)
        o += dial_label(kind, 100 * math.sin(a), -8 - 100 * math.cos(a)) if False else dial_label(kind, 96 * math.sin(a), -8 - 96 * math.cos(a))
    jacks = [(-85, "10A", "#c0392b"), (-28, "mA", "#c0392b"), (28, "COM", "#222"), (85, "VΩ", "#c0392b")]
    for x, lab, col in jacks:
        glow = f'<circle cx="{x}" cy="170" r="28" fill="{GREEN}" opacity=".35"/>' if highlight and lab in highlight else ""
        o += glow + f'<circle cx="{x}" cy="170" r="19" fill="#1a1c20" stroke="{col}" stroke-width="5"/><circle cx="{x}" cy="170" r="7" fill="#000"/>'
        o += T(x, 215, lab, 16, 800, "#222")
    return o


def f_multimetre():
    o = g(330, 290, multimeter(), 1.0)
    cx, cy = 330, 290
    o += callout(cx + 70, cy - 190, 560, 90, "Écran (afficheur)", "start", 19, bold=True)
    o += callout(cx + 30, cy - 50, 560, 190, "Sélecteur rotatif : grandeur\net calibre (V, A, Ω…)", "start", 19, bold=True)
    o += callout(cx + 28, cy + 170, 560, 330, "Borne COM (noire) :\ntoujours le cordon noir", "start", 19, bold=True)
    o += callout(cx + 85, cy + 170, 560, 420, "Borne VΩ (rouge) :\ntension, résistance, continuité", "start", 19, bold=True)
    o += callout(cx - 28, cy + 170, 560, 505, "Borne mA (rouge) : petits courants", "start", 19, bold=True)
    o += callout(cx - 85, cy + 170, 560, 565, "Borne 10 A (rouge) : gros courants", "start", 19, bold=True)
    o += panel(900, 60, 270, 340, "Repères", accent=AMBER)
    o += dc_sym(930, 120, INK, 22) + T(950, 128, "continu (DC)", 16, 700, INK, "start")
    o += ac_sym(930, 168, INK) + T(950, 174, "alternatif (AC)", 16, 700, INK, "start")
    o += T(930, 226, "Ω : résistance", 16, 700, INK, "start") + T(930, 266, "•))) : continuité (bip)", 16, 700, INK, "start")
    o += T(1035, 340, "Disposition variable\nselon les modèles", 15, 500, MUTED)
    return figure(W, 640, o)


def loop_bat(L, R, T_, B_, bx=None):
    o = s_wire([(L, 210), (L, T_)]) + s_wire([(L, 290), (L, B_)])
    o += sym("BAT", L, 250, 90)
    return o


def f_mesure_tension():
    o = panel(30, 30, 1140, 440, fill="#fff")
    o += s_wire([(130, 220), (130, 140), (290, 140)]) + sym("R", 330, 140) + T(330, 105, "R1", 20, 800, INK)
    o += s_wire([(370, 140), (600, 140), (600, 220)]) + sym("R", 600, 260, 90) + T(640, 266, "R2", 20, 800, INK, "start")
    o += s_wire([(600, 300), (600, 400), (130, 400), (130, 280)]) + sym("BAT", 130, 250, 90)
    o += dot(600, 180) + s_wire([(600, 180), (760, 180), (760, 225)]) + g(760, 265, '<circle r="34" fill="#fff" stroke="#1b2742" stroke-width="3.2"/><text y="10" font-size="30" font-weight="800" text-anchor="middle" fill="#1b2742">V</text>')
    o += s_wire([(760, 300), (760, 340), (600, 340)]) + dot(600, 340)
    o += f'<rect x="570" y="165" width="220" height="190" rx="14" fill="none" stroke="{GREEN}" stroke-width="3" stroke-dasharray="8 6"/>'
    o += T(680, 395, "branché EN PARALLÈLE", 18, 800, GREEN)
    o += panel(850, 60, 300, 380, "Mesure de tension", accent=BLUE)
    o += T(1000, 130, "1  circuit sous tension,\non ne le coupe pas", 17, 600, INK)
    o += T(1000, 215, "2  cordon noir sur COM,\nrouge sur VΩ", 17, 600, INK)
    o += T(1000, 300, "3  sélecteur sur V continu\n(V ⎓ pour une pile)".replace("⎓", "DC"), 17, 600, INK)
    o += T(1000, 385, "4  pointes de chaque côté\ndu composant", 17, 600, INK)
    return figure(W, 500, o)


def f_mesure_courant():
    o = panel(30, 30, 1140, 440, fill="#fff")
    o += s_wire([(130, 220), (130, 140), (290, 140)]) + sym("AM", 330, 140) + T(330, 100, "A", 20, 800, GREEN)
    o += s_wire([(370, 140), (600, 140), (600, 210)]) + g(600, 250, sym("LAMP", 0, 0, 90))
    o += s_wire([(600, 290), (600, 400), (130, 400), (130, 280)]) + sym("BAT", 130, 250, 90)
    o += f'<rect x="270" y="105" width="120" height="70" rx="14" fill="none" stroke="{GREEN}" stroke-width="3" stroke-dasharray="8 6"/>'
    o += T(330, 215, "ampèremètre EN SÉRIE", 18, 800, GREEN)
    o += arrow(420, 124, 520, 124, GREEN, 5) + T(470, 100, "I", 22, 800, GREEN)
    o += panel(850, 60, 300, 380, "Mesure de courant", accent=GREEN)
    o += T(1000, 130, "1  ouvrir le circuit\npuis insérer l'appareil", 17, 600, INK)
    o += T(1000, 215, "2  cordon noir sur COM,\nrouge sur mA (ou 10 A)", 17, 600, INK)
    o += T(1000, 300, "3  sélecteur sur A continu,\ncalibre le plus grand", 17, 600, INK)
    o += T(1000, 385, "⚠ jamais en parallèle :\ncourt-circuit !", 17, 800, RED)
    return figure(W, 500, o)


def scope(x, y, w, h, path_fn, label):
    o = f'<g filter="url(#sh)"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="16" fill="#24282f"/></g>'
    ix, iy, iw, ih = x + 18, y + 18, w - 36, h - 60
    o += f'<rect x="{ix}" y="{iy}" width="{iw}" height="{ih}" rx="6" fill="#06130c"/>'
    for i in range(1, 10):
        o += f'<line x1="{ix+iw*i/10}" y1="{iy}" x2="{ix+iw*i/10}" y2="{iy+ih}" stroke="#1e5c3a" stroke-width="{2 if i==5 else 1}" opacity=".7"/>'
    for i in range(1, 8):
        o += f'<line x1="{ix}" y1="{iy+ih*i/8}" x2="{ix+iw}" y2="{iy+ih*i/8}" stroke="#1e5c3a" stroke-width="{2 if i==4 else 1}" opacity=".7"/>'
    o += f'<path d="{path_fn(ix, iy + ih/2, iw)}" fill="none" stroke="#55ff9c" stroke-width="3" stroke-linejoin="round" filter="url(#neon)"/>'
    o += T(x + 24, y + h - 14, "CH1  1 V/div   1 ms/div", 14, 600, "#9fd8b8", "start")
    return o


def f_bruit():
    o = scope(40, 60, 540, 360, lambda x, y, w: sine_path(x, y, w, 90, 3), "")
    o += scope(620, 60, 540, 360, lambda x, y, w: noisy_path(x, y, w, 90, 3, 22, 500), "")
    o += chip(310, 450, "Signal propre", GREEN, size=20) + chip(890, 450, "Signal bruité (parasites)", RED, size=20)
    return figure(W, 495, o)


def f_diagnostic():
    o = panel(30, 30, 640, 520, fill="#fff")
    o += vcc(260, 130, "+5 V") + s_wire([(260, 130), (260, 160)]) + sym("R", 260, 200, 90) + T(300, 206, "R = 220 Ω", 19, 800, INK, "start")
    o += s_wire([(260, 240), (260, 310)]) + dot(260, 275) + sym("LED", 260, 350, 90) + T(300, 356, "LED rouge", 19, 800, INK, "start")
    o += s_wire([(260, 390), (260, 450)]) + gnd(260, 450)
    for y, n, col in ((142, "TP1", RED), (275, "TP2", AMBER), (450, "TP3", BLUE)):
        o += chip(130, y, n, col, w=70, size=17) + s_wire([(165, y), (250, y)], col, 2.5, "5 5")
    o += panel(700, 30, 470, 520, "Valeurs attendues (par rapport à GND)", accent=BLUE)
    rows = [("TP1", RED, "5 V", "alimentation présente"), ("TP2", AMBER, "≈ 2 V", "tension de la LED rouge allumée"), ("TP3", BLUE, "0 V", "la masse (référence)")]
    for i, (n, c, v, d) in enumerate(rows):
        y = 130 + i * 110
        o += chip(770, y, n, c, w=70, size=17) + T(840, y + 8, v, 30, 800, INK, "start") + T(770, y + 44, d, 16, 500, MUTED, "start")
    o += T(935, 470, "Cordon noir sur GND, cordon rouge\nsur le point à tester.", 17, 700, INK)
    o += T(935, 525, "Écart avec l'attendu → piste de la panne.", 16, 600, MUTED)
    return figure(W, 580, o)


def f_condo_gonfle():
    o = panel(30, 40, 560, 470, "Condensateur sain", accent=GREEN) + panel(610, 40, 560, 470, "Condensateur défaillant", accent=RED)
    for x, bad in ((310, False), (890, True)):
        o += f'<rect x="{x-200}" y="350" width="400" height="22" fill="url(#pcb)" rx="3"/>'
        o += g(x, 395, electrolytic(h=150, bulged=bad, leak=bad), 1.35).replace("</g>", "</g>") if False else g(x, 350, electrolytic(h=150, bulged=bad, leak=bad), 1.2)
        if bad:
            o += '<ellipse cx="920" cy="355" rx="70" ry="10" fill="#7b4a1b" opacity=".75"/>'
    o += chip(310, 465, "dessus plat, aucune trace", GREEN, size=17)
    o += callout(890, 158, 1000, 105, "sommet bombé", "start", 19, bold=True)
    o += callout(870, 182, 1000, 175, "soupape déformée\nou éclatée", "start", 19, bold=True)
    o += callout(925, 356, 1020, 300, "fuite d'électrolyte\n(traces brunes)", "start", 19, bold=True)
    o += chip(890, 465, "à remplacer : capacité en baisse", RED, size=17)
    return figure(W, 545, o)


FIGS = {
    "courant_continu_alternatif": f_dc_ac, "multimetre": f_multimetre, "mesure_tension": f_mesure_tension, "mesure_courant": f_mesure_courant,
    "signal_propre_bruit": f_bruit, "diagnostic_points_de_mesure": f_diagnostic, "condensateur_gonfle": f_condo_gonfle,
}
