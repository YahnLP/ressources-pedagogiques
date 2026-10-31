from lib import *

W = 1200


def chain(boxes, H=560, labels=("signal électrique", "ordre de commande"), notes=None):
    """3 blocs reliés par des flèches. boxes = [(titre, couleur, [(svg, s, dx, dy)...], texte)]"""
    o = ""
    bw, gap, x0 = 330, 75, 38
    for i, (t, col, items, txt) in enumerate(boxes):
        x = x0 + i * (bw + gap)
        o += panel(x, 50, bw, H - 100, t, accent=col)
        for svg, s, dx, dy in items:
            o += g(x + bw / 2 + dx, 90 + dy, svg, s)
        o += T(x + bw / 2, H - 125, txt, 18, 500, MUTED)
        if i < 2:
            ax = x + bw + 8
            o += arrow(ax, 230, ax + gap - 16, 230, INK, 5)
            if labels:
                o += T(ax + gap / 2, 205, labels[i].split("\n")[0], 14, 600, MUTED)
    return o


def f_ouvert_ferme():
    o = ""
    for k, (px, closed) in enumerate(((30, False), (610, True))):
        o += panel(px, 40, 560, 390, "Circuit fermé" if closed else "Circuit ouvert", accent=GREEN if closed else RED)
        L, R, Ty, By = px + 70, px + 490, 150, 360
        o += s_wire([(L, 240), (L, Ty), (px + 240, Ty)])
        o += s_wire([(px + 320, Ty), (R, Ty), (R, 210)])
        o += s_wire([(R, 290), (R, By), (L, By), (L, 280)])
        o += sym("BAT", L, 250, 90)
        o += sym("SW", px + 280, Ty, closed=closed)
        if closed:
            o += g(R, 250, '<circle r="46" fill="url(#glow)"/>')
        o += sym("LAMP", R, 250, 90, fill="#ffe36b" if closed else "#fff")
        o += g(px + 280, 300, bulb(closed), 0.8)
        o += T(px + 280, 190 if not closed else 190, "interrupteur " + ("fermé" if closed else "ouvert"), 17, 600, MUTED)
        if closed:
            for (a, b) in (((px + 360, Ty), (px + 420, Ty)), ((px + 320, By), (px + 260, By)), ((L, 215), (L, 175))):
                o += arrow(a[0], a[1] - (14 if a[1] == Ty else -16 if a[1] == By else 0), b[0], b[1] - (14 if b[1] == Ty else -16 if b[1] == By else 0), GREEN, 5)
            o += T(px + 395, Ty - 28, "I", 22, 800, GREEN)
        o += chip(px + 280, 405, "le courant ne circule pas" if not closed else "le courant circule : lampe allumée", RED if not closed else GREEN, size=17)
    return figure(W, 460, o)


def f_resistance():
    o = g(600, 190, resistor(("jaune", "violet", "rouge", "or"), lead=70), 2.1)
    labels = [(400, "1er chiffre : 4", 512), (570, "2e chiffre : 7", 556), (760, "multiplicateur : × 100", 600), (960, "tolérance : ± 5 %", 704)]
    for tx, t, bx in labels:
        o += callout(bx, 160, tx, 80, t, "middle", 18, bold=True)
    o += T(600, 290, "4  7  × 100 Ω = 4 700 Ω = 4,7 kΩ  ± 5 %", 24, 700, INK)
    cols = ["noir", "marron", "rouge", "orange", "jaune", "vert", "bleu", "violet", "gris", "blanc"]
    mult = ["× 1", "× 10", "× 100", "× 1 k", "× 10 k", "× 100 k", "× 1 M", "× 10 M", "× 100 M", "× 1 G"]
    x0, cw, y0 = 175, 98, 330
    o += panel(30, y0 - 20, 1140, 290, fill="#fbfcfe")
    for r, lab in enumerate(("Couleur", "Chiffre", "Multiplicateur")):
        o += T(48, y0 + 36 + r * 74, lab, 18, 700, MUTED, "start")
    for i, c in enumerate(cols):
        x = x0 + i * cw
        o += f'<rect x="{x+6}" y="{y0}" width="{cw-12}" height="46" rx="8" fill="{COLORS[c]}" stroke="#aab4c6" stroke-width="1.5"/>'
        o += T(x + cw / 2, y0 + 70, c, 15, 600, INK)
        o += T(x + cw / 2, y0 + 118, str(i), 24, 800, INK)
        o += T(x + cw / 2, y0 + 194, mult[i], 20, 700, INK)
    o += T(x0 + 3 * cw, y0 + 245, "Tolérance : marron ± 1 %   rouge ± 2 %   or ± 5 %   argent ± 10 %", 18, 600, INK, "middle")
    o += T(x0 + 6.5 * cw, y0 + 245, "", 1)
    o += T(600, y0 + 272, "Multiplicateurs spéciaux : or × 0,1   argent × 0,01      Tolérance en dernière position, séparée des autres bandes", 15, 500, MUTED)
    return figure(W, 640, o)


def f_condo():
    o = g(400, 350, electrolytic(), 1.8)
    o += callout(430, 118, 480, 78, "Soupape (croix)")
    o += callout(430, 235, 480, 165, "470 µF : capacité\n25 V : tension max.")
    o += callout(325, 240, 255, 175, "Bande blanche « − »\n= borne négative", "end")
    o += callout(430, 520, 480, 520, "Patte longue = « + »")
    o += callout(370, 490, 255, 560, "Patte courte = « − »", "end")
    o += panel(780, 40, 380, 290, "Symboles")
    o += sym("CP", 880, 130, s=1.6)
    o += T(880, 190, "polarisé (chimique)", 17, 600, MUTED)
    o += sym("C", 1050, 130, s=1.6) + T(1050, 190, "non polarisé", 17, 600, MUTED)
    o += g(850, 252, ceramic_cap(), .62) + T(1010, 262, "Céramique :\npas de sens", 16, 600, INK)
    o += f'<rect x="780" y="360" width="380" height="190" rx="16" fill="#fff4f2" stroke="{RED}" stroke-width="2.5"/>'
    o += T(970, 400, "⚠ Attention au montage", 22, 800, RED)
    o += T(970, 440, "Sens inversé ou tension trop élevée :\néchauffement, gonflement,\nrisque d'éclatement.", 19, 600, INK)
    return figure(W, 600, o)


def f_inductances():
    items = [("Bobine torique", inductor_toroid(), 1.3, "noyau en ferrite, fil de cuivre\nfiltrage, alimentations"),
             ("Self moulée (axiale)", inductor_axial(), 1.5, "ressemble à une résistance\nbandes de couleur = valeur"),
             ("Self CMS", smd_inductor(), 1.3, "montage en surface\ncartes compactes")]
    o = ""
    for i, (t, svg, s, d) in enumerate(items):
        x = 30 + i * 390
        o += panel(x, 40, 360, 330, t)
        o += g(x + 180, 200 if i != 0 else 150, svg, s if i != 0 else 1.0)
        o += T(x + 180, 325, d, 17, 500, MUTED)
    o += panel(30, 395, 1140, 130, fill="#fbfcfe")
    o += sym("L", 200, 460, s=1.7)
    o += T(330, 440, "Symbole : L", 21, 800, INK, "start")
    o += T(330, 472, "Unité : henry (H) ; on rencontre le mH et le µH", 18, 500, INK, "start")
    o += T(330, 500, "Stocke l'énergie (champ magnétique) et s'oppose aux variations rapides du courant.", 17, 500, MUTED, "start")
    return figure(W, 555, o)


def f_diode_led():
    o = ""
    # carte diode
    o += panel(30, 40, 560, 400, "Diode de redressement")
    o += g(200, 190, diode_1n4007(), 1.7)
    o += callout(222, 168, 300, 105, "bande = cathode (K)", "start", 17, bold=True)
    o += callout(120, 190, 100, 245, "anode (A)", "middle", 17, bold=True)
    o += sym("D", 440, 190, s=1.1)
    o += T(404, 236, "A", 19, 800, INK) + T(476, 236, "K", 19, 800, INK)
    o += i_arrow(150, 330, 450, 330, "sens passant du courant", off=(0, -22), size=18)
    o += T(300, 380, "Le courant passe de A vers K, jamais en sens inverse.", 17, 500, MUTED)
    # carte LED
    o += panel(610, 40, 560, 400, "LED (diode électroluminescente)")
    o += g(740, 255, led(lit=True, legs=True), 1.3)
    o += callout(757, 380, 800, 410, "patte longue\n= anode (+)", "start", 16, bold=True)
    o += callout(724, 350, 700, 410, "patte courte\n= cathode (−)", "end", 16, bold=True)
    o += T(640, 110, "méplat sur le boîtier\n= côté cathode", 15, 600, MUTED, "start")
    o += sym("LED", 1020, 215, s=1.3)
    o += T(968, 270, "A", 19, 800, INK) + T(1072, 270, "K", 19, 800, INK)
    o += T(1020, 130, "symbole", 17, 600, MUTED)
    o += T(1020, 330, "toujours avec une\nrésistance en série", 17, 700, RED)
    o += chip(600, 495, "Polarisé : une diode ou une LED montée à l'envers ne conduit pas (et peut être détruite).", AMBER, w=1000, size=18)
    return figure(W, 540, o)


def f_transistors():
    o = ""
    cards = [("Bipolaire NPN", lambda x: npn(x, 190, 1.6), ("B", "C", "E"), "courant de base → C vers E"),
             ("Bipolaire PNP", lambda x: npn(x, 190, 1.6, "pnp"), ("B", "E", "C"), "E en haut, C en bas"),
             ("MOSFET canal N", lambda x: nmos(x, 190, 1.6), ("G", "D", "S"), "commandé en tension")]
    for i, (t, fn, lab, d) in enumerate(cards):
        x = 30 + i * 390
        o += panel(x, 40, 360, 300, t)
        cx = x + 190
        o += fn(cx)
        o += T(cx - 108, 198, lab[0], 22, 800, BLUE)
        o += T(cx + 66, 108, lab[1], 22, 800, BLUE)
        o += T(cx + 66, 292, lab[2], 22, 800, BLUE)
        o += T(x + 180, 326, d, 16, 500, MUTED)
    o += panel(30, 365, 560, 250, "Boîtier TO-92")
    o += g(170, 525, to92("2N2222"), .9)
    o += T(380, 500, "3 pattes ; repérer la face plate.\nBrochage (E-B-C ou C-B-E) selon\nla référence : voir la fiche technique.", 16, 500, INK)
    o += panel(610, 365, 560, 250, "Deux rôles")
    o += T(890, 455, "① Interrupteur commandé : ON / OFF", 19, 700, INK)
    o += T(890, 487, "un petit courant de base commande un grand courant C → E", 15, 500, MUTED)
    o += T(890, 540, "② Amplificateur : petit signal → grand signal", 19, 700, INK)
    o += T(890, 572, "IC ≈ β × IB (β : gain en courant)", 15, 500, MUTED)
    return figure(W, 640, o)


def f_actifs_passifs():
    o = ""
    spec = [("Composants passifs", BLUE, 30,
             [("Résistance", resistor(lead=18), .5, 0), ("Condensateur", electrolytic(), .62, 5), ("Bobine", inductor_toroid(), .68, -8)],
             "Subissent le circuit : limiter, stocker,\nfiltrer. Ne peuvent ni amplifier ni décider."),
            ("Composants actifs", GREEN, 610,
             [("Diode / LED", led(), .7, 0), ("Transistor", to92(), .8, 12), ("Circuit intégré", dip(8, h=70, pitch=26, fs=14, label="CI"), .6, -20)],
             "Contrôlent, orientent, amplifient ou traitent\nl'information. Exigent une alimentation.")]
    for t, col, px, items, txt in spec:
        o += panel(px, 40, 560, 470, t, accent=col)
        for i, (name, svg, s, dy) in enumerate(items):
            tx = px + 22 + i * 178
            o += f'<rect x="{tx}" y="100" width="152" height="230" rx="14" fill="#fff" stroke="#dde4f0" stroke-width="2"/>'
            o += g(tx + 76, 190 + dy * s, svg, s)
            o += T(tx + 76, 312, name, 18, 700, INK)
        o += T(px + 280, 400, txt, 19, 600, INK)
    return figure(W, 540, o)


def f_serie_parallele():
    o = ""
    for k, px in enumerate((30, 610)):
        o += panel(px, 40, 560, 640, "Montage en série" if k == 0 else "Montage en parallèle", accent=BLUE if k == 0 else GREEN)
        o += '<g transform="translate(0,50)">'
        L = px + 80
        o += s_wire([(L, 210), (L, 130), (px + 470 if k == 0 else px + 470, 130)])
        o += s_wire([(L, 290), (L, 370), (px + 470, 370)])
        o += sym("BAT", L, 250, 90)
        o += u_arrow(px + 38, 300, px + 38, 200, "U", off=(-14, 0), size=22)
        if k == 0:
            R = px + 470
            for j in range(3):
                o += sym("R", R, 170 + j * 80, 90)
                o += u_arrow(R - 52, 195 + j * 80, R - 52, 145 + j * 80, f"U{j+1}", off=(-14, 0), size=19)
                o += T(R + 48, 176 + j * 80, f"R{j+1}", 20, 800, INK, "start")
            o += i_arrow(px + 250, 130, px + 330, 130, "I (identique)", off=(0, -26), size=19)
            fm = "Même courant : I = I₁ = I₂ = I₃\nU = U₁ + U₂ + U₃\nR = R₁ + R₂ + R₃"
        else:
            for j, X in enumerate((px + 250, px + 360, px + 470)):
                o += s_wire([(X, 130), (X, 210)]) + s_wire([(X, 290), (X, 370)])
                o += sym("R", X, 250, 90) + T(X + 30, 256, f"R{j+1}", 20, 800, INK, "start")
                o += i_arrow(X, 150, X, 190, f"I{j+1}", off=(-14, 0), size=18)
                if j < 2:
                    o += dot(X, 130) + dot(X, 370)
            o += s_wire([(px + 470, 130), (px + 250, 130)]) + s_wire([(px + 470, 370), (px + 250, 370)])
            o += i_arrow(L + 20, 130, L + 100, 130, "I total", off=(0, -26), size=19)
            fm = "Même tension : U = U₁ = U₂ = U₃\nI = I₁ + I₂ + I₃\n1/R = 1/R₁ + 1/R₂ + 1/R₃"
        o += "</g>"
        o += f'<rect x="{px+40}" y="505" width="480" height="150" rx="14" fill="#fff" stroke="#dde4f0" stroke-width="2"/>'
        o += T(px + 280, 560, fm, 21, 700, INK)
    return figure(W, 710, o)


def f_diviseur():
    o = vcc(200, 150, "Ue = 5 V")
    o += s_wire([(200, 150), (200, 145)]) + sym("R", 200, 185, 90) + s_wire([(200, 225), (200, 285)]) + sym("R", 200, 325, 90)
    o += s_wire([(200, 365), (200, 420), (440, 420)]) + gnd(310, 420) + dot(310, 420)
    o += T(240, 190, "R1 = 10 kΩ", 20, 800, INK, "start") + T(240, 330, "R2 = 10 kΩ", 20, 800, INK, "start")
    o += dot(200, 255) + s_wire([(200, 255), (440, 255)]) + node(440, 255) + T(470, 262, "Us", 24, 800, INK, "start")
    o += u_arrow(100, 410, 100, 120, "Ue", off=(-16, 0), size=24)
    o += u_arrow(540, 400, 540, 280, "Us", off=(20, 0), size=22)
    o += s_wire([(440, 255), (440, 420)])
    o += g(440, 340, '<circle r="30" fill="#fff" stroke="#1b2742" stroke-width="3.2"/><text y="9" font-size="26" font-weight="800" text-anchor="middle" fill="#1b2742">V</text>')
    o += panel(640, 60, 520, 420)
    o += T(900, 115, "Diviseur de tension", 24, 800, INK)
    o += T(900, 190, "Us = Ue × R2 / (R1 + R2)", 28, 800, BLUE)
    o += T(900, 250, "Exemple : Ue = 5 V ; R1 = R2 = 10 kΩ", 19, 600, INK)
    o += T(900, 285, "Us = 5 × 10 / (10 + 10) = 2,5 V", 22, 800, GREEN)
    o += T(900, 350, "Applications : lire un capteur (LDR, thermistance),\npotentiomètre, adapter 5 V → 3,3 V.", 17, 500, MUTED)
    o += T(900, 420, "On mesure Us avec le voltmètre en parallèle sur R2.", 17, 700, INK)
    return figure(W, 520, o)


def f_filtre():
    o = s_wire([(70, 200), (150, 200)]) + node(70, 200) + T(60, 170, "Ue", 22, 800, BLUE, "middle")
    o += sym("R", 190, 200) + s_wire([(230, 200), (380, 200)]) + dot(320, 200) + node(380, 200) + T(390, 170, "Us", 22, 800, BLUE, "middle")
    o += T(190, 165, "R", 21, 800) + s_wire([(320, 200), (320, 240)]) + sym("C", 320, 280, 90) + s_wire([(320, 320), (320, 345)]) + gnd(320, 345)
    o += T(358, 288, "C", 21, 800, INK, "start")
    o += T(225, 440, "Filtre passe-bas RC", 22, 800, INK)
    o += T(225, 478, "R = 1 kΩ ; C = 100 nF", 18, 500, MUTED)
    # courbe de gain
    X0, X1, Y0, Y1 = 640, 1140, 120, 400
    o += panel(560, 40, 610, 480, "Courbe de gain")
    o += f'<line x1="{X0}" y1="{Y1}" x2="{X1}" y2="{Y1}" stroke="{INK}" stroke-width="2.5"/><line x1="{X0}" y1="{Y0}" x2="{X0}" y2="{Y1}" stroke="{INK}" stroke-width="2.5"/>'
    fc = 1592
    def px_(f): return X0 + (math.log10(f) - 1) / 4 * (X1 - X0)
    def py_(db): return Y0 + (-db) / 40 * (Y1 - Y0)
    pts = []
    for i in range(0, 161):
        f = 10 ** (1 + i * 4 / 160)
        db = -10 * math.log10(1 + (f / fc) ** 2)
        pts.append((px_(f), py_(db)))
    o += f'<rect x="{X0}" y="{Y0}" width="{px_(fc)-X0}" height="{Y1-Y0}" fill="{GREEN}" opacity=".08"/>'
    o += f'<rect x="{px_(fc)}" y="{Y0}" width="{X1-px_(fc)}" height="{Y1-Y0}" fill="{RED}" opacity=".07"/>'
    o += "<path d='M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts) + f"' fill='none' stroke='{BLUE}' stroke-width='5' stroke-linecap='round'/>"
    for db in (0, -10, -20, -30, -40):
        o += f'<line x1="{X0-6}" y1="{py_(db)}" x2="{X0}" y2="{py_(db)}" stroke="{INK}" stroke-width="2"/>' + T(X0 - 12, py_(db) + 5, str(db), 15, 600, MUTED, "end")
    for f, lab in ((10, "10"), (100, "100"), (1000, "1 k"), (10000, "10 k"), (100000, "100 k")):
        o += f'<line x1="{px_(f)}" y1="{Y1}" x2="{px_(f)}" y2="{Y1+7}" stroke="{INK}" stroke-width="2"/>' + T(px_(f), Y1 + 26, lab, 15, 600, MUTED)
    o += T(X1 + 8, Y1 + 46, "f (Hz)", 16, 700, INK, "end") + T(X0 + 8, Y0 - 12, "gain (dB)", 16, 700, INK, "start")
    o += f'<circle cx="{px_(fc)}" cy="{py_(-3)}" r="7" fill="{AMBER}" stroke="#fff" stroke-width="2"/>'
    o += callout(px_(fc), py_(-3), px_(fc) + 40, 195, "fc ≈ 1,6 kHz\n(−3 dB)", "start", 18, bold=True)
    o += T((X0 + px_(fc)) / 2, Y0 + 40, "les basses fréquences\npassent", 17, 700, GREEN)
    o += T((px_(fc) + X1) / 2 + 20, Y0 + 215, "les hautes fréquences\nsont atténuées", 17, 700, RED)
    o += T(865, 495, "fc = 1 / (2π · R · C)", 21, 800, INK)
    return figure(W, 560, o)


def f_boitiers():
    o = ""
    spec = [("DIP-8 (traversant)", 30, 36, 96, False, "pas 2,54 mm", 1.75), ("SOIC-8 (CMS)", 610, 20, 62, True, "pas 1,27 mm", 3.0)]
    for t, px, pitch, h, soic, pas, s in spec:
        o += panel(px, 40, 560, 430, t, accent=BLUE if not soic else GREEN)
        w = 4 * pitch + 10
        ext = 26 if not soic else pitch * 0.36 * 1.4
        ox, oy = px + 300 - w * s / 2, 255 - h * s / 2
        o += g(ox, oy, dip(8, h=h, pitch=pitch, soic=soic, label="NE555", fs=22 if not soic else 15), s)
        for i in range(1, 9):
            x, side = dip_pin_xy(i, 8, pitch, h, soic)
            yy = oy + (h + ext) * s + 24 if side == "b" else oy - ext * s - 10
            o += T(ox + x * s, yy, str(i), 19, 800, BLUE if i == 1 else INK)
        o += callout(ox + 2, oy + h * s / 2, px + 40, oy + h * s / 2 - 50, "encoche\n(détrompeur)", "start", 16, bold=True)
        o += callout(ox + (18 if not soic else 14) * s, oy + (h - 16) * s, px + 40, oy + h * s - 10, "repère\nbroche 1", "start", 16, bold=True)
        o += T(px + 280, 455, pas, 18, 700, MUTED)
    o += chip(600, 510, "Vu de dessus, encoche à gauche : broche 1 en bas à gauche, on compte dans le sens inverse des aiguilles d'une montre.", AMBER, w=1110, size=16)
    return figure(W, 550, o)


def f_chaine_01():
    o = chain([("CAPTEUR", BLUE, [(ldr(), .9, -80, 85), (push_button(), .6, 70, 60)], "grandeur physique → signal électrique\n(lumière, appui, température…)"),
               ("TRAITEMENT", AMBER, [(dip(8, h=84, pitch=30, label="µC", fs=22), 1.5, -88, 40)], "lit le signal, décide,\nenvoie une commande"),
               ("ACTIONNEUR", GREEN, [(led(lit=True), .8, -95, 85), (motor(), .75, 20, 60)], "convertit l'ordre en action\n(lumière, mouvement, son)")], 440, labels=None)
    return figure(W, 440, o)


def f_cms():
    o = ""
    o += panel(30, 40, 560, 270, "Composant traversant (THT)")
    o += f'<rect x="60" y="215" width="500" height="26" fill="url(#pcb)"/><rect x="60" y="210" width="500" height="6" fill="url(#copper)"/><rect x="60" y="241" width="500" height="6" fill="url(#copper)"/>'
    o += ''.join(f'<rect x="{x-6}" y="210" width="12" height="37" fill="#1c1d21"/>' for x in (240, 400))
    o += g(320, 170, resistor(lead=0).replace('<rect x="-84" y="-3.5"', '<rect x="0" y="0"'), 1.0) if False else ""
    o += f'<g transform="translate(320,170)">{resistor(lead=0)}</g>'
    o += f'<rect x="237" y="170" width="6" height="98" fill="url(#metalH)"/><rect x="397" y="170" width="6" height="98" fill="url(#metalH)"/>'
    o += ''.join(f'<path d="M{x-16},249 Q{x-3},249 {x-3},268 L{x+3},268 Q{x+3},249 {x+16},249 Z" fill="url(#solder)"/>' for x in (240, 400))
    o += callout(330, 152, 380, 100, "corps du composant", "start", 16)
    o += callout(240, 262, 70, 285, "pattes dans les trous, soudées dessous", "start", 15)
    o += panel(610, 40, 560, 270, "Composant monté en surface (CMS)", accent=GREEN)
    o += f'<rect x="640" y="215" width="500" height="26" fill="url(#pcb)"/><rect x="640" y="209" width="500" height="6" fill="url(#copper)" opacity="0"/>'
    o += f'<rect x="740" y="206" width="70" height="9" fill="url(#copper)"/><rect x="830" y="206" width="70" height="9" fill="url(#copper)"/>'
    o += f'<g transform="translate(820,180)">{smd_resistor("103", 116, 46)}</g>'
    o += f'<path d="M742,212 Q770,212 770,196 L772,206Z M900,212 Q872,212 868,196Z" fill="url(#solder)"/>'
    o += callout(820, 160, 960, 100, "posé sur des pastilles", "start", 16)
    o += callout(756, 212, 650, 285, "soudé du même côté de la carte", "start", 15)
    # tailles réelles (20 px / mm)
    o += panel(30, 335, 1140, 190, "Tailles comparées (échelle réelle : 20 px = 1 mm)", accent=MUTED)
    s = 20
    items = [("Résistance 1/4 W\n6,3 × 2,3 mm", 6.3, 2.3, "#e9d4a3"), ("CMS 0805\n2,0 × 1,25 mm", 2.0, 1.25, "#222"), ("CMS 0603\n1,6 × 0,8 mm", 1.6, .8, "#222"), ("CMS 0402\n1,0 × 0,5 mm", 1.0, .5, "#222")]
    xs = [140, 460, 660, 860]
    for (lab, wmm, hmm, col), x in zip(items, xs):
        o += f'<rect x="{x - wmm*s/2}" y="{430 - hmm*s/2}" width="{wmm*s}" height="{hmm*s}" rx="2" fill="{col}" stroke="#777" stroke-width="1"/>'
        o += T(x, 482, lab, 15, 600, INK)
    o += f'<line x1="1020" y1="432" x2="1120" y2="432" stroke="{INK}" stroke-width="3"/><line x1="1020" y1="424" x2="1020" y2="440" stroke="{INK}" stroke-width="3"/><line x1="1120" y1="424" x2="1120" y2="440" stroke="{INK}" stroke-width="3"/>'
    o += T(1070, 412, "5 mm", 16, 700, INK)
    return figure(W, 555, o)


FIGS = {
    "circuit_ouvert_ferme": f_ouvert_ferme, "resistance_code_couleurs": f_resistance, "condensateur_electrolytique": f_condo,
    "inductances": f_inductances, "diode_led": f_diode_led, "transistors": f_transistors, "passifs_actifs": f_actifs_passifs,
    "serie_parallele": f_serie_parallele, "diviseur_tension": f_diviseur, "filtre_rc": f_filtre, "boitiers_ci": f_boitiers,
    "chaine_capteur_actionneur": f_chaine_01, "cms_traversant": f_cms,
}
