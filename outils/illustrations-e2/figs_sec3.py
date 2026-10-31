"""Figures complémentaires de Seconde (S14 à S17)."""
from lib import *
from figs07 import block
from figs_sec2 import f_dht11_cablage

W = 1200


def phone(x, y, title, body, col=BLUE):
    o = f'<g filter="url(#sh)"><rect x="{x}" y="{y}" width="250" height="400" rx="26" fill="#1b2130"/></g><rect x="{x+12}" y="{y+22}" width="226" height="356" rx="14" fill="#f4f7fc"/>'
    o += f'<rect x="{x+12}" y="{y+22}" width="226" height="46" rx="14" fill="{col}"/><rect x="{x+12}" y="{y+50}" width="226" height="18" fill="{col}"/>' + T(x + 125, y + 52, title, 16, 800, "#fff")
    return o + body


def f_pairing():
    o = ""
    p1 = "".join(f'<rect x="{{x}}" y="0" width="0" height="0"/>' for _ in range(0))
    pan = [("1 · Bluetooth", [("Bluetooth", "activé ✓", GREEN), ("HC-05", "disponible", BLUE), ("Casque", "disponible", MUTED)], BLUE),
           ("2 · Code PIN", None, AMBER), ("3 · Appareils associés", [("HC-05", "associé ✓", GREEN)], GREEN), ("4 · Terminal série BT", None, INK)]
    for i, (t, rows, c) in enumerate(pan):
        x = 40 + i * 290; y = 40
        body = ""
        if rows:
            for k, (a, b, cc) in enumerate(rows):
                body += f'<rect x="{x+26}" y="{y+90+k*62}" width="198" height="50" rx="8" fill="#fff" stroke="#d5dce8" stroke-width="2"/>' + T(x + 40, y + 112 + k * 62, a, 16, 800, INK, "start") + T(x + 40, y + 132 + k * 62, b, 13, 600, cc, "start")
        elif i == 1:
            body += T(x + 125, y + 130, "Code PIN pour HC-05", 15, 700, INK) + f'<rect x="{x+60}" y="{y+160}" width="130" height="46" rx="8" fill="#fff" stroke="{AMBER}" stroke-width="3"/>' + T(x + 125, y + 192, "1234", 26, 800, INK) + f'<rect x="{x+60}" y="{y+250}" width="130" height="42" rx="21" fill="{AMBER}"/>' + T(x + 125, y + 278, "Associer", 17, 800, "#fff")
        else:
            body += f'<rect x="{x+26}" y="{y+90}" width="198" height="250" rx="8" fill="#0f1729"/>' + "".join(T(x + 38, y + 124 + k * 38, l, 15, 600, cc, "start", extra='font-family="monospace"') for k, (l, cc) in enumerate((("connecté ✓", "#6ee7a5"), ("→ AT", "#8ab4ff"), ("← OK", "#6ee7a5"), ("→ LED_ON", "#8ab4ff"), ("← LED allumée", "#6ee7a5"))))
        o += phone(x, y, t, body, c)
    return figure(W, 480, o)


def f_lcd_curseur():
    o = T(600, 40, "lcd.setCursor(colonne, ligne)", 22, 800, INK, extra='font-family="monospace"')
    x0, y0, cw, ch = 110, 100, 62, 90
    for c in range(16): o += T(x0 + c * cw + cw / 2, y0 - 10, str(c), 16, 800, MUTED)
    for r in range(2): o += T(70, y0 + r * ch + ch / 2 + 6, str(r), 18, 800, MUTED)
    o += T(70, y0 - 10, "col →", 13, 700, MUTED) + T(70, y0 + 2 * ch + 26, "ligne ↓", 13, 700, MUTED)
    txt = ["Temp: 23.4C", "CIEL  OK"]
    hl = {(0, 0): (RED, "setCursor(0,0)"), (8, 0): (BLUE, "setCursor(8,0)"), (0, 1): (GREEN, "setCursor(0,1)")}
    for r in range(2):
        for c in range(16):
            col = hl.get((c, r), (None,))[0]
            o += f'<rect x="{x0+c*cw}" y="{y0+r*ch}" width="{cw}" height="{ch}" fill="{(col+"") if col else "#bfe6a8"}" opacity="{1 if not col else .85}" stroke="#7fb06a" stroke-width="2"/>'
            ch_ = txt[r][c] if c < len(txt[r]) else ""
            if ch_.strip(): o += T(x0 + c * cw + cw / 2, y0 + r * ch + ch / 2 + 11, ch_, 32, 800, "#16301a", extra='font-family="monospace"')
    for k, ((c, r), (col, lab)) in enumerate(hl.items()):
        o += chip(250 + k * 350, y0 + 2 * ch + 50, lab + f"  → colonne {c}, ligne {r}", col, size=16, w=300)
    return figure(W, 400, o)


def f_lm35():
    o = panel(30, 30, 520, 440, "Brochage du LM35 (boîtier TO-92)", accent=BLUE)
    o += g(290, 270, to92("LM35"), 1.5)
    for i, (l, c) in enumerate((("+Vs", RED), ("Vout", BLUE), ("GND", INK))): o += T(290 + (i - 1) * 33 * 1.5, 440, l, 18, 800, c) + badge(290 + (i - 1) * 33 * 1.5, 405, i + 1, c, 14) if False else T(290 + (i - 1) * 33, 440, l, 17, 800, c)
    o += T(290, 130, "vue de face (face plate)", 15, 600, MUTED)
    o += panel(570, 30, 600, 440, "Température = tension × 100", accent=GREEN)
    o += f'<rect x="680" y="100" width="380" height="64" rx="10" fill="#fff" stroke="{GREEN}" stroke-width="3"/>' + T(870, 143, "T (°C) = Vout (V) × 100", 26, 800, INK)
    ax, ay, aw, ah = 650, 200, 480, 200
    o += f'<line x1="{ax}" y1="{ay+ah}" x2="{ax+aw}" y2="{ay+ah}" stroke="{INK}" stroke-width="3" marker-end="url(#arr)"/><line x1="{ax}" y1="{ay+ah}" x2="{ax}" y2="{ay-10}" stroke="{INK}" stroke-width="3" marker-end="url(#arr)"/>'
    o += f'<line x1="{ax}" y1="{ay+ah}" x2="{ax+400}" y2="{ay+10}" stroke="{BLUE}" stroke-width="6" stroke-linecap="round"/>'
    o += T(ax + aw, ay + ah + 28, "température (°C)", 15, 700, INK, "end") + T(ax + 8, ay - 16, "Vout (V)", 15, 700, INK, "start")
    o += T(ax + 400, ay + ah + 24, "100 °C", 14, 800, INK) + T(ax - 10, ay + 16, "1 V", 14, 800, INK, "end") + T(ax, ay + ah + 24, "0", 14, 800, INK)
    return figure(W, 500, o)


def f_cablage_lm35():
    o = block(440, 60, 300, 360, "", None, BLUE) + T(590, 100, "Arduino UNO", 22, 800, INK)
    for l, y, side in (("5V", 160, "L"), ("A0", 230, "L"), ("GND", 330, "L"), ("A4 (SDA)", 160, "R"), ("A5 (SCL)", 230, "R"), ("5V", 300, "R"), ("GND", 360, "R")):
        o += T(452 if side == "L" else 728, y + 6, l, 16, 800, INK, "start" if side == "L" else "end")
    o += g(120, 250, to92("LM35"), 1.2) + T(120, 120, "LM35", 20, 800, INK)
    o += s_wire([(87, 345), (87, 380), (360, 380), (360, 160), (440, 160)], RED) + s_wire([(120, 345), (120, 400), (380, 400), (380, 230), (440, 230)], BLUE) + s_wire([(153, 345), (153, 420), (400, 420), (400, 330), (440, 330)], "#222")
    o += T(87, 372, "+Vs", 12, 800, RED, "end") + T(120, 392, "Vout", 12, 800, BLUE, "end") + T(153, 412, "GND", 12, 800, INK, "end")
    o += block(880, 120, 260, 230, "", None, AMBER) + T(1010, 160, "LCD I2C 16×2", 20, 800, INK)
    for l, y, c in (("SDA", 160, "#2f5bea"), ("SCL", 200, "#e99a14"), ("VCC", 250, RED), ("GND", 300, "#222")):
        o += T(892, y + 25, l, 14, 800, INK, "start")
    o += s_wire([(740, 160), (880, 185)], "#2f5bea") + s_wire([(740, 230), (880, 225)], "#e99a14") + s_wire([(740, 300), (880, 275)], RED) + s_wire([(740, 360), (860, 360), (860, 325), (880, 325)], "#222")
    return figure(W, 460, o)


def arch(sensor, sub, label, alerts):
    o = block(470, 190, 260, 140, "Arduino UNO", "cerveau du système", BLUE)
    for t, sub, x, y, c in (("DHT11", "D2 · 1-Wire", 60, 90, GREEN), ("LCD I2C 16×2", "A4 / A5", 470, 20, AMBER), ("HC-05", "D10 / D11", 880, 190, AMBER), ("Smartphone", "données reçues", 900, 360, BLUE)):
        pass
    o += block(60, 190, 240, 120, sensor, sub, GREEN) + arrow(300, 250, 470, 250, INK, 5) + arrow(470, 250, 300, 250, INK, 5) + T(385, 230, label, 16, 800, GREEN)
    o += block(470, 20, 260, 100, "LCD I2C 16×2", "A4 / A5", AMBER) + arrow(600, 190, 600, 126, INK, 5) + T(690, 160, "affichage local", 16, 800, AMBER, "start")
    o += block(900, 190, 240, 120, "HC-05", "Bluetooth · D10 / D11", AMBER) + arrow(730, 250, 900, 250, INK, 5)
    o += block(900, 380, 240, 100, "Smartphone", "données reçues", BLUE) + arrow(1020, 316, 1020, 380, INK, 5) + T(1030, 350, "sans fil", 15, 700, BLUE, "start")
    if alerts: o += f'<path d="M600,330 V470" stroke="{MUTED}" stroke-width="3" stroke-dasharray="6 5"/>' + chip(600, 480, "Alertes : T > 30 °C · HR > 80 %", RED, size=17)
    return figure(W, 520, o)


def f_architecture(): return arch("DHT11", "capteur · D2", "T° + humidité", True)


def f_architecture_proto(): return arch("LM35", "entrée analogique A0", "donnée de température", False)


def f_svarc():
    steps = [("S", "Symptôme", "observer et décrire", BLUE), ("V", "Vérification", "mesurer et tester", AMBER), ("A", "Analyse", "attendu ≠ obtenu ?", "#c9a400"), ("R", "Remède", "corriger", GREEN), ("C", "Contrôle", "vérifier que ça marche", RED)]
    o = ""
    for i, (l, t, d, c) in enumerate(steps):
        x = 40 + i * 230
        o += f'<rect x="{x}" y="100" width="200" height="190" rx="16" fill="{c}"/>' + T(x + 100, 170, l, 56, 800, "#fff") + T(x + 100, 212, t, 21, 800, "#fff") + T(x + 100, 244, d, 15, 600, "#fff")
        if i < 4: o += arrow(x + 204, 195, x + 226, 195, INK, 5)
    o += T(600, 60, "Méthode SVARC : un ordre à respecter", 22, 800, INK)
    return figure(W, 330, o)


def f_voltmetre_led():
    o = g(260, 270, __import__('figs04').multimeter(highlight=("VΩ", "COM")), 0.62)
    o += panel(560, 30, 600, 420, "Mesure aux bornes de la LED", accent=BLUE)
    o += s_wire([(600, 130), (700, 130)]) + sym("R", 740, 130) + T(740, 100, "220 Ω", 16, 800, INK) + s_wire([(780, 130), (880, 130), (880, 170)])
    o += sym("LED", 880, 210, 90, s=1.1) + s_wire([(880, 254), (880, 300)]) + gnd(880, 300) + T(600, 125, "pin", 15, 800, MUTED, "end")
    o += f'<g stroke="{RED}" stroke-width="5"><line x1="866" y1="172" x2="896" y2="188"/><line x1="896" y1="172" x2="866" y2="188"/><line x1="866" y1="236" x2="896" y2="252"/><line x1="896" y1="236" x2="866" y2="252"/></g>'
    o += T(960, 180, "anode (+)\nsonde rouge", 15, 800, RED, "start") + T(960, 252, "cathode (−)\nsonde noire", 15, 800, INK, "start")
    o += chip(860, 400, "Valeur attendue : ≈ 2,0 V (LED rouge allumée)", GREEN, w=520, size=17)
    return figure(W, 480, o)


def f_schema_complet():
    o = block(440, 40, 320, 520, "", None, BLUE) + T(600, 80, "Arduino UNO", 24, 800, INK)
    for l, y in (("5V", 140), ("D2", 210), ("GND", 280), ("A4 (SDA)", 360), ("A5 (SCL)", 420)): o += T(452, y + 6, l, 16, 800, INK, "start")
    for l, y in (("D10", 150), ("D11", 230)): o += T(748, y + 6, l, 16, 800, INK, "end")
    o += block(40, 100, 230, 200, "", None, GREEN) + T(155, 140, "DHT11", 20, 800, INK)
    for l, y in (("VCC", 140), ("DATA", 210), ("GND", 280)): o += T(52, y + 6, l, 14, 800, INK, "start")
    o += s_wire([(270, 140), (440, 140)], RED) + s_wire([(270, 210), (440, 210)]) + s_wire([(270, 280), (440, 280)], "#222")
    o += dot(340, 140) + dot(340, 210) + s_wire([(340, 140), (340, 160)]) + sym("R", 340, 175, 90, s=0.4) + s_wire([(340, 190), (340, 210)]) + T(360, 180, "R1 = 10 kΩ (pull-up)", 13, 800, INK, "start")
    o += block(40, 340, 230, 120, "", None, AMBER) + T(155, 380, "LCD I2C", 20, 800, INK) + T(52, 425, "SDA", 13, 800, "#2f5bea", "start") + T(52, 445, "SCL", 13, 800, "#e99a14", "start")
    o += s_wire([(270, 425), (440, 360)], "#2f5bea") + s_wire([(270, 445), (440, 420)], "#e99a14")
    o += block(940, 100, 220, 200, "", None, AMBER) + T(1050, 140, "HC-05", 20, 800, INK) + T(952, 156, "TXD", 14, 800, INK, "start") + T(952, 236, "RXD", 14, 800, INK, "start")
    o += s_wire([(760, 150), (940, 150)], GREEN) + s_wire([(760, 230), (816, 230)]) + sym("R", 840, 230, s=0.6) + s_wire([(864, 230), (940, 230)]) + dot(900, 230) + T(840, 205, "R2 = 1 kΩ", 13, 800, INK)
    o += s_wire([(900, 230), (900, 267)]) + sym("R", 900, 285, 90, s=0.45) + s_wire([(900, 303), (900, 320)]) + gnd(900, 320) + T(925, 291, "R3 = 2 kΩ", 13, 800, INK, "start")
    return figure(W, 600, o)


FIGS = {"pairing_bluetooth": f_pairing, "lcd_curseur": f_lcd_curseur, "lm35_brochage": f_lm35, "cablage_lm35_lcd": f_cablage_lm35, "architecture_domotique": f_architecture, "architecture_proto": f_architecture_proto,
        "svarc_logigramme": f_svarc, "voltmetre_led": f_voltmetre_led, "schema_complet_domotique": f_schema_complet}
