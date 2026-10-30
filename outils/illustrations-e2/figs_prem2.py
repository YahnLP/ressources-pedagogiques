"""Figures complémentaires de Première et Terminale."""
from lib import *
from figs07 import block
from figs_prem import chain

W = 1200


def cible(cx, cy, r=100, groups=(), title=None):
    o = ""
    for k in (1, .75, .5, .25): o += f'<circle cx="{cx}" cy="{cy}" r="{r*k}" fill="{"#fff" if int(k*4)%2 else "#eef2fa"}" stroke="#b8c3d8" stroke-width="2"/>'
    o += f'<circle cx="{cx}" cy="{cy}" r="4" fill="{INK}"/>'
    for col, pts in groups:
        for dx, dy in pts: o += f'<circle cx="{cx+dx*r}" cy="{cy+dy*r}" r="7" fill="{col}" stroke="#fff" stroke-width="2"/>'
    return o


def f_flux_pcb():
    st = [("Schematic Editor", "symboles R, D, Q"), ("Footprint Assignment", "symbole → empreinte"), ("Update PCB", "composants en vrac + ratsnest"), ("Edge.Cuts", "contour de la carte"), ("Placement", "composants rangés"), ("Routage", "pistes de cuivre"), ("DRC", "règles vérifiées ✓"), ("Vue 3D", "contrôle final")]
    o = ""
    for i, (t, s) in enumerate(st):
        r, c = divmod(i, 4); x = 40 + c * 290; y = 40 + r * 190
        o += block(x, y, 250, 140, t, s, [BLUE, BLUE, AMBER, AMBER, GREEN, GREEN, RED, "#6c63ff"][i]) + badge(x + 28, y + 36, i + 1, INK, 16)
        if c < 3: o += arrow(x + 254, y + 70, x + 286, y + 70, INK, 4)
    o += s_wire([(1165, 110), (1165, 150), (165, 150), (165, 205)], MUTED, 3, "7 6") if False else ""
    return figure(W, 420, o)


def f_pistes():
    o = f'<rect x="40" y="40" width="1120" height="400" rx="16" fill="url(#pcb)"/>'
    o += f'<rect x="80" y="110" width="520" height="14" fill="url(#copper)"/>' + T(340, 96, "Signal 0,35 mm", 18, 800, "#fff") + f'<rect x="80" y="170" width="520" height="14" fill="url(#copper)"/>'
    o += f'<path d="M110,124 V170" stroke="#fff" stroke-width="3" marker-start="url(#arr)" marker-end="url(#arr)"/>' + T(190, 154, "clearance (isolement)", 16, 800, "#fff", "start")
    o += f'<rect x="80" y="300" width="520" height="40" fill="url(#copper)"/>' + T(340, 290, "Alimentation / GND 1,5 mm", 18, 800, "#fff")
    o += f'<rect x="760" y="215" width="150" height="14" fill="url(#copper)"/><circle cx="960" cy="222" r="42" fill="url(#copper)" stroke="#fff" stroke-width="3"/><circle cx="960" cy="222" r="20" fill="#0f1a14"/><rect x="1010" y="215" width="120" height="14" fill="url(#copper)"/>'
    o += T(960, 150, "via entre F.Cu et B.Cu", 18, 800, "#fff") + T(960, 300, "pastille Ø 0,8 mm · perçage Ø 0,4 mm", 15, 700, "#fff") + T(960, 325, "(valeurs courantes)", 13, 600, "#d6ebdd")
    return figure(W, 480, o)


def f_coupe_pcb():
    layers = [("Sérigraphie F (texte blanc)", "#f4f4f4", 40), ("Masque de soudure F (vert)", "#2e9d5a", 44), ("Cuivre F.Cu", "#d9a441", 36), ("Substrat FR4", "#c9a26a", 120), ("Cuivre B.Cu", "#d9a441", 36), ("Masque de soudure B (vert)", "#2e9d5a", 44), ("Sérigraphie B", "#f4f4f4", 40)]
    o = ""; y = 50
    for t, c, h in layers:
        o += f'<rect x="80" y="{y}" width="560" height="{h}" fill="{c}" stroke="#6b7480" stroke-width="2"/>' + T(670, y + h / 2 + 6, t, 19, 700, INK, "start"); y += h
    o += f'<rect x="340" y="94" width="30" height="236" fill="#b87333" stroke="#8a5420" stroke-width="2"/>' + T(355, 395, "via métallisé : relie F.Cu et B.Cu", 18, 800, INK)
    return figure(W, 440, o)


def f_gerber():
    o = ""
    cols = [("F.Cu", "calque cuivre"), ("F.Mask", "ouvertures du masque"), ("F.Silkscreen", "textes R1, D1, IC1"), ("PCB réel", "les 3 couches superposées")]
    for i, (t, s) in enumerate(cols):
        x = 40 + i * 290; o += f'<rect x="{x}" y="60" width="250" height="250" rx="12" fill="{"#1b2130" if i<3 else "#2e9d5a"}"/>' + T(x + 125, 345, t, 20, 800, INK) + T(x + 125, 370, s, 14, 600, MUTED)
        if i in (0, 3): o += f'<path d="M{x+30},120 H{x+220} M{x+30},180 H{x+130} V250 H{x+220}" stroke="{RED if i==0 else "#d9a441"}" stroke-width="8" fill="none"/>'
        if i in (1, 3): o += ''.join(f'<circle cx="{x+cx}" cy="{y}" r="10" fill="{"#000" if i==1 else "#e7e9ee"}"/>' for cx, y in ((30, 120), (220, 120), (30, 180), (130, 180), (220, 250)))
        if i in (2, 3): o += T(x + 70, 110, "R1", 18, 800, "#fff") + T(x + 190, 230, "D1", 18, 800, "#fff") + T(x + 70, 280, "IC1", 18, 800, "#fff")
        if i < 3: o += arrow(x + 125, 395, x + 125 + 0, 395, INK, 1) if False else ""
    o += s_wire([(165, 395), (165, 420), (1035, 420), (1035, 372)], INK, 4) + chip(600, 420, "superposition", AMBER, w=200, size=16)
    return figure(W, 450, o)


def f_wifi_sta():
    o = block(60, 100, 300, 160, "Box Internet", "SSID « MonReseau » · serveur DHCP", AMBER) + block(840, 100, 300, 160, "ESP32", "mode STA", BLUE)
    o += arrow(364, 180, 836, 180, INK, 5) + arrow(836, 180, 364, 180, INK, 5) + T(600, 160, "Wi-Fi", 22, 800, INK) + chip(990, 300, "IP 192.168.1.42 (DHCP)", GREEN, size=17, w=300)
    return figure(W, 340, o)


def f_wifi_modes():
    o = ""
    for i, (t, c, a, b) in enumerate((("Mode STA", BLUE, "ESP32 connecté à la box", "IP fournie par le DHCP de la box"), ("Mode AP", AMBER, "l'ESP32 diffuse son propre SSID", "serveur DHCP : 192.168.4.1"), ("Mode STA + AP", GREEN, "connecté à la box ET réseau local", "Internet + configuration locale"))):
        x = 30 + i * 390; o += panel(x, 30, 360, 430, t, accent=c) + block(x + 110, 200, 140, 80, "ESP32", None, c)
        if i in (0, 2): o += block(x + 110, 90, 140, 56, "Box", "Internet", MUTED) + arrow(x + 180, 150, x + 180, 196, INK, 4) + arrow(x + 180, 196, x + 180, 150, INK, 4)
        if i in (1, 2): o += block(x + 20, 350, 130, 56, "Mobile", None, c) + block(x + 210, 350, 130, 56, "PC", None, c) + arrow(x + 150, 350, x + 140, 284, INK, 3) + arrow(x + 220, 350, x + 230, 284, INK, 3)
        o += T(x + 180, 316 if i == 0 else 322, a if i == 0 else "", 14, 700, INK) if False else ""
        o += T(x + 180, 82 + 0, "", 1) + T(x + 180, 440, b, 14, 700, MUTED)
        o += T(x + 180, 56 + 0, "", 1)
    return figure(W, 490, o)


def f_mqtt_esp32():
    o = block(40, 110, 270, 170, "ESP32", "publisher · capteur de température", BLUE) + block(470, 90, 260, 210, "Broker Mosquitto", "liste des topics actifs", AMBER)
    o += block(890, 70, 270, 100, "Smartphone", "application MQTT", GREEN) + block(890, 230, 270, 100, "PC", "subscriber", GREEN)
    o += arrow(314, 195, 466, 195, INK, 5) + T(390, 175, "publie", 15, 800, INK) + arrow(734, 170, 886, 120, INK, 4) + arrow(734, 230, 886, 280, INK, 4) + T(810, 170, "souscrivent", 15, 800, INK)
    return figure(W, 380, o)


def f_mtbf_timeline():
    o = ""; x = 60
    seq = [(300, GREEN, "TO"), (50, RED, "TA"), (260, GREEN, "TO"), (60, RED, "TA"), (330, GREEN, "TO"), (45, RED, "TA")]
    for w, c, l in seq:
        o += f'<rect x="{x}" y="140" width="{w}" height="70" fill="{c}" opacity=".85"/>' + T(x + w / 2, 183, l, 20, 800, "#fff"); x += w
    o += arrow(60, 110, 1140, 110, INK, 3) + T(1140, 98, "temps", 15, 700, INK, "end")
    o += f'<path d="M60,236 H360" stroke="{GREEN}" stroke-width="4" marker-start="url(#arr)" marker-end="url(#arr)"/>' + T(210, 262, "TO : temps de fonctionnement", 16, 800, GREEN)
    o += f'<path d="M360,290 H410" stroke="{RED}" stroke-width="4" marker-start="url(#arr)" marker-end="url(#arr)"/>' + T(385, 318, "TA : arrêt", 16, 800, RED)
    o += chip(600, 380, "MTBF = moyenne des TO     ·     MTTR = moyenne des TA", INK, w=760, size=18)
    return figure(W, 420, o)


def f_rt():
    o = ""; ax, ay, aw, ah = 140, 60, 900, 320
    o += f'<line x1="{ax}" y1="{ay+ah}" x2="{ax+aw}" y2="{ay+ah}" stroke="{INK}" stroke-width="3" marker-end="url(#arr)"/><line x1="{ax}" y1="{ay+ah}" x2="{ax}" y2="{ay-10}" stroke="{INK}" stroke-width="3" marker-end="url(#arr)"/>'
    pts = [(ax + t / 3 * aw * .95, ay + ah - math.exp(-t) * ah) for t in [i / 60 * 3 for i in range(61)]]
    o += "<polyline points='" + " ".join(f"{x:.0f},{y:.0f}" for x, y in pts) + f"' fill='none' stroke='{BLUE}' stroke-width='6'/>"
    xm = ax + aw * .95 / 3; ym = ay + ah - math.exp(-1) * ah
    o += f'<line x1="{xm}" y1="{ay+ah}" x2="{xm}" y2="{ym}" stroke="{RED}" stroke-width="3" stroke-dasharray="7 6"/><line x1="{ax}" y1="{ym}" x2="{xm}" y2="{ym}" stroke="{RED}" stroke-width="3" stroke-dasharray="7 6"/><circle cx="{xm}" cy="{ym}" r="8" fill="{RED}"/>'
    o += callout(xm, ym, xm + 90, ym - 60, "R(MTBF) = e⁻¹ ≈ 0,368 (36,8 %)", "start", 18, bold=True)
    for k in range(4): o += T(ax + k / 3 * aw * .95, ay + ah + 28, "0" if k == 0 else f"{k}×MTBF", 15, 700, INK)
    o += T(ax - 10, ay + 6, "1", 15, 700, INK, "end") + T(ax - 10, ay + ah + 6, "0", 15, 700, INK, "end") + T(ax + 6, ay - 18, "fiabilité R(t)", 16, 800, INK, "start") + T(ax + aw, ay + ah + 54, "temps", 15, 800, INK, "end")
    return figure(W, 440, o)


def f_serie_para():
    o = panel(30, 30, 560, 380, "Série", accent=RED) + panel(610, 30, 560, 380, "Parallèle", accent=GREEN)
    for i in range(3):
        o += block(60 + i * 170, 110, 130, 80, "R = 0,9", None, RED) + (arrow(194 + i * 170, 150, 226 + i * 170, 150, INK, 3) if i < 2 else "")
        o += block(780, 90 + i * 74, 200, 60, "R = 0,9", None, GREEN)
    o += s_wire([(740, 120), (740, 254)], INK, 3) + s_wire([(1020, 120), (1020, 254)], INK, 3) + "".join(s_wire([(740, 120 + i * 74), (780, 120 + i * 74)], INK, 3) + s_wire([(980, 120 + i * 74), (1020, 120 + i * 74)], INK, 3) for i in range(3))
    o += chip(310, 370, "Rs = 0,9³ = 0,729 (72,9 %)", RED, w=380, size=18) + chip(890, 370, "Rs = 1 − 0,1³ = 0,999 (99,9 %)", GREEN, w=400, size=18)
    o += chip(600, 440, "Série = plus fragile  ·  Parallèle = plus fiable", INK, w=640, size=19)
    return figure(W, 480, o)


def f_couplages():
    o = ""
    spec = [("Résistif", "impédance commune (fil GND partagé)", RED), ("Capacitif", "capacité parasite entre deux pistes", AMBER), ("Inductif", "champ magnétique d'une boucle de courant", BLUE), ("Rayonné", "ondes dans l'air vers l'antenne Wi-Fi", GREEN)]
    for i, (t, d, c) in enumerate(spec):
        x = 30 + i * 295; o += panel(x, 30, 270, 360, t, accent=c) + block(x + 20, 100, 110, 60, "Variateur", None, c) + block(x + 140, 270, 110, 60, "Capteur", None, c)
        if i == 0: o += s_wire([(x + 75, 160), (x + 75, 230), (x + 195, 230), (x + 195, 270)], c, 5) + T(x + 135, 218, "GND commun", 13, 800, c)
        if i == 1: o += s_wire([(x + 90, 160), (x + 90, 200)], INK, 5) + s_wire([(x + 190, 270), (x + 190, 215)], INK, 5) + sym("C", x + 140, 207, 0, s=0.6)
        if i == 2: o += f'<ellipse cx="{x+75}" cy="200" rx="50" ry="30" fill="none" stroke="{c}" stroke-width="4"/><ellipse cx="{x+75}" cy="200" rx="28" ry="16" fill="none" stroke="{c}" stroke-width="3"/>' + s_wire([(x + 195, 270), (x + 195, 235)], c, 4)
        if i == 3: o += f'<path d="{sine_path(x+40, 230, 190, 14, 3)}" fill="none" stroke="{c}" stroke-width="4"/>'
        o += T(x + 135, 365, d, 13, 700, INK) if len(d) < 36 else T(x + 135, 365, d, 12, 700, INK)
    return figure(W, 420, o)


def f_blindage():
    o = ""
    for i, (t, c, att) in enumerate((("Blindage efficace", GREEN, "60 dB"), ("Fente = antenne", RED, "20 dB"))):
        x = 60 + i * 570; o += panel(x, 30, 510, 440, t, accent=c)
        o += f'<rect x="{x+150}" y="150" width="210" height="130" fill="#e6e9ef" stroke="{INK}" stroke-width="5"/>'
        if i == 1: o += f'<rect x="{x+150}" y="205" width="10" height="26" fill="#fff"/>' + arrow(x + 70, 218, x + 220, 218, RED, 5)
        else: o += f'<path d="{sine_path(x+40, 215, 90, 12, 2)}" fill="none" stroke="{GREEN}" stroke-width="4"/><g stroke="{RED}" stroke-width="5"><line x1="{x+150}" y1="200" x2="{x+130}" y2="230"/><line x1="{x+130}" y1="200" x2="{x+150}" y2="230"/></g>'
        o += f'<rect x="{x+60}" y="330" width="{(60 if i==0 else 20)*5.4}" height="40" rx="6" fill="{c}"/>' + T(x + 255, 395, f"atténuation : {att}" + ("" if i == 0 else " (à la fréquence de résonance)"), 15, 800, INK)
    return figure(W, 510, o)


def f_decouplage():
    o = f'<rect x="40" y="40" width="1120" height="400" rx="16" fill="url(#pcb)"/>' + g(440, 190, dip(8, h=100, pitch=40, soic=True, label="MCU", fs=22), 2.0)
    o += T(380, 130, "VCC", 20, 800, "#fff") + T(380, 355, "GND", 20, 800, "#fff")
    for x in (560, 640): o += f'<rect x="{x}" y="285" width="46" height="26" rx="3" fill="#b78b52"/><rect x="{x}" y="285" width="9" height="26" fill="url(#metalH)"/><rect x="{x+37}" y="285" width="9" height="26" fill="url(#metalH)"/>'
    o += callout(583, 298, 800, 250, "100 nF (0402) collés aux broches VCC / GND", "start", 17, bold=True) + chip(900, 400, "boucle de courant courte = moins de bruit", GREEN, w=500, size=16)
    return figure(W, 480, o)


def f_hysteresis():
    o = ""; ax, ay, aw, ah = 140, 60, 920, 300
    def Y(T_): return ay + ah - (T_ - 26) / 7 * ah
    o += f'<rect x="{ax}" y="{ay}" width="{aw}" height="{Y(30)-ay}" fill="{RED}" opacity=".10"/><rect x="{ax}" y="{Y(30)}" width="{aw}" height="{Y(28)-Y(30)}" fill="{AMBER}" opacity=".16"/><rect x="{ax}" y="{Y(28)}" width="{aw}" height="{ay+ah-Y(28)}" fill="{GREEN}" opacity=".10"/>'
    o += f'<line x1="{ax}" y1="{ay+ah}" x2="{ax+aw}" y2="{ay+ah}" stroke="{INK}" stroke-width="3"/><line x1="{ax}" y1="{ay+ah}" x2="{ax}" y2="{ay-10}" stroke="{INK}" stroke-width="3"/>'
    pts = [(ax + i / 100 * aw, Y(29.5 + 2.5 * math.sin(i / 100 * 2 * math.pi * 1.6 - 1.2))) for i in range(101)]
    o += "<polyline points='" + " ".join(f"{x:.0f},{y:.0f}" for x, y in pts) + f"' fill='none' stroke='{BLUE}' stroke-width='5'/>"
    o += f'<line x1="{ax}" y1="{Y(30)}" x2="{ax+aw}" y2="{Y(30)}" stroke="{RED}" stroke-width="3" stroke-dasharray="9 7"/><line x1="{ax}" y1="{Y(28)}" x2="{ax+aw}" y2="{Y(28)}" stroke="{AMBER}" stroke-width="3" stroke-dasharray="9 7"/>'
    o += T(ax + aw + 8, Y(30) + 5, "Seuil haut 30 °C", 15, 800, RED, "start") if False else T(ax + 10, Y(30) - 8, "Seuil haut = 30 °C", 15, 800, RED, "start") + T(ax + 10, Y(28) + 20, "Seuil bas = 28 °C", 15, 800, AMBER, "start")
    o += chip(ax + 130, ay + 20, "🔴 ALERTE", RED, size=14, w=110) + chip(ax + 450, Y(29), "alerte maintenue", AMBER, size=14, w=170) + chip(ax + 760, ay + ah - 24, "🟢 OK", GREEN, size=14, w=90)
    o += T(ax + 6, ay - 18, "température (°C)", 15, 800, INK, "start") + T(ax + aw, ay + ah + 28, "temps (min)", 15, 800, INK, "end") + chip(600, 405, "L'hystérésis évite le clignotement de l'alerte autour du seuil", INK, w=760, size=16)
    return figure(W, 440, o)


def f_exactitude():
    o = panel(30, 30, 560, 420, "Exact mais non fidèle", accent=BLUE) + panel(610, 30, 560, 420, "Fidèle mais non exact", accent=RED)
    o += cible(310, 240, 120, [(BLUE, [(.6, .1), (-.5, .4), (-.2, -.6), (.3, .55), (-.6, -.2), (.1, -.1)])]) + cible(890, 240, 120, [(RED, [(.55, .35), (.6, .4), (.5, .3), (.62, .28), (.52, .42), (.58, .36)])])
    o += T(310, 410, "mesures dispersées, centrées sur la valeur vraie", 15, 700, INK) + T(890, 410, "mesures groupées, mais décalées de la valeur vraie", 15, 700, INK)
    return figure(W, 480, o)


def f_cibles_grr():
    o = ""
    A, B, C = "#2f5bea", "#d63f3f", "#17935c"
    def grp(c, cx, cy, s): return (c, [(cx + s * dx, cy + s * dy) for dx, dy in ((0, 0), (.4, .3), (-.3, .4), (.2, -.4))])
    cases = [("Répétabilité ✓ · reproductibilité ✓", [grp(A, .0, .0, .06), grp(B, .05, .0, .06), grp(C, -.03, .04, .06)]),
             ("Répétabilité ✓ · reproductibilité ✗", [grp(A, -.6, -.4, .06), grp(B, .6, -.3, .06), grp(C, .0, .65, .06)]),
             ("Répétabilité ✗ · reproductibilité ✓", [grp(A, 0, 0, .55), grp(B, 0, 0, .6), grp(C, 0, 0, .5)]),
             ("Répétabilité ✗ · reproductibilité ✗", [grp(A, -.3, -.2, .55), grp(B, .35, .2, .6), grp(C, .0, -.4, .55)])]
    for i, (t, gs) in enumerate(cases):
        x = 30 + i * 295; o += panel(x, 30, 270, 340, "") + cible(x + 135, 170, 100, [(c, [(px, py) for px, py in pts]) for c, pts in gs]) + T(x + 135, 330, t, 14, 800, INK)
    o += "".join(f'<circle cx="{450+i*120}" cy="410" r="8" fill="{c}"/>' + T(465 + i * 120, 416, l, 16, 700, INK, "start") for i, (c, l) in enumerate(((A, "opérateur A"), (B, "opérateur B"), (C, "opérateur C"))))
    return figure(W, 440, o)


def f_grr():
    o = ""
    cas = [("%GRR = 8 %", .08, GREEN, "EXCELLENT"), ("%GRR = 20 %", .20, AMBER, "ACCEPTABLE"), ("%GRR = 40 %", .40, RED, "INACCEPTABLE")]
    x0, w = 220, 740
    for i, (t, p, c, v) in enumerate(cas):
        y = 90 + i * 110
        o += T(200, y + 38, t, 20, 800, INK, "end") + f'<rect x="{x0}" y="{y}" width="{w}" height="56" fill="#cfe0ff" stroke="{INK}" stroke-width="2"/><rect x="{x0}" y="{y}" width="{w*p}" height="56" fill="{c}"/>' + T(x0 + w + 20, y + 38, v, 20, 800, c, "start")
    o += T(x0, 55, "−Tol", 17, 800, INK) + T(x0 + w, 55, "+Tol", 17, 800, INK) + T(x0 + w / 2, 55, "intervalle de tolérance", 16, 700, MUTED)
    o += chip(500, 430, "zone colorée = part consommée par le GRR (5,15 × σGRR)", INK, w=560, size=16) + chip(960, 430, "zone bleue = ce qui reste pour distinguer les pièces", BLUE, w=420, size=14)
    return figure(W, 470, o)


def f_lin_dec():
    o = panel(30, 30, 560, 380, "Régulateur linéaire", accent=RED) + panel(610, 30, 560, 380, "Convertisseur à découpage", accent=GREEN)
    o += chain([("9 V", "entrée"), ("TO-220", "dissipe en chaleur"), ("5 V", "sortie")], y=120, h=100, w=140, gap=32, x0=60, col=[BLUE, RED, GREEN])
    o += chain([("9 V", "entrée"), ("Buck", "découpage"), ("5 V", "sortie")], y=120, h=100, w=140, gap=32, x0=640, col=[BLUE, GREEN, GREEN])
    o += chip(310, 290, "rendement = 5 / 9 ≈ 55 %", RED, w=340, size=17) + T(310, 335, "≈ 45 % de l'énergie est perdue en chaleur", 16, 700, INK) + chip(890, 290, "rendement élevé (≈ 85 à 95 %)", GREEN, w=360, size=17) + T(890, 335, "peu de chaleur, mais plus de parasites (CEM)", 16, 700, INK)
    return figure(W, 440, o)


def f_thermique():
    o = block(40, 100, 190, 110, "Pdiss", "source de chaleur (W)", RED)
    nodes = [("Tj", "jonction", 330), ("Tb", "boîtier", 570), ("Ts", "radiateur", 810), ("Tamb", "air", 1050)]
    for i, (t, s, x) in enumerate(nodes): o += f'<circle cx="{x}" cy="155" r="26" fill="#fff" stroke="{INK}" stroke-width="4"/>' + T(x, 161, t, 15, 800, INK) + T(x, 205, s, 14, 700, MUTED)
    o += s_wire([(230, 155), (304, 155)], INK, 4)
    for i, (r, d) in enumerate((("Rθjc", "jonction → boîtier"), ("Rθcs", "boîtier → radiateur (graisse)"), ("Rθsa", "radiateur → air"))):
        xa, xb = nodes[i][2] + 26, nodes[i + 1][2] - 26
        o += s_wire([(xa, 155), (xa + 40, 155)], INK, 4) + sym("R", (xa + xb) / 2, 155, s=0.9) + s_wire([(xb - 40, 155), (xb, 155)], INK, 4) + T((xa + xb) / 2, 110, r, 19, 800, BLUE) + T((xa + xb) / 2, 250, d, 13, 700, MUTED)
    o += chip(600, 330, "Tj = Tamb + Pdiss × (Rθjc + Rθcs + Rθsa)", INK, w=760, size=19)
    return figure(W, 380, o)


FIGS = {"flux_schema_pcb": f_flux_pcb, "pistes_vias_clearance": f_pistes, "coupe_pcb_double_face": f_coupe_pcb, "gerber_couches": f_gerber, "wifi_sta": f_wifi_sta, "wifi_modes": f_wifi_modes,
        "mqtt_esp32": f_mqtt_esp32, "chronologie_mtbf": f_mtbf_timeline, "courbe_fiabilite": f_rt, "serie_parallele_fiabilite": f_serie_para, "couplages_cem": f_couplages, "blindage_fente": f_blindage,
        "decouplage_pcb": f_decouplage, "hysteresis_alerte": f_hysteresis, "exactitude_fidelite": f_exactitude, "cibles_repetabilite": f_cibles_grr, "grr_interpretation": f_grr, "lineaire_decoupage": f_lin_dec, "modele_thermique": f_thermique}
