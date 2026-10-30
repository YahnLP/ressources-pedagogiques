"""Figures des cours de Seconde, séances S09 à S18."""
from lib import *
from figs07 import block

W = 1200


def axes(x, y, w, h, xl="temps", yl="tension (V)"):
    return (f'<line x1="{x}" y1="{y+h}" x2="{x+w}" y2="{y+h}" stroke="{INK}" stroke-width="3" marker-end="url(#arr)"/><line x1="{x}" y1="{y+h}" x2="{x}" y2="{y-10}" stroke="{INK}" stroke-width="3" marker-end="url(#arr)"/>'
            + T(x + w, y + h + 28, xl, 16, 700, INK, "end") + T(x - 8, y - 16, yl, 16, 700, INK, "start"))


def f_analogique():
    o = panel(30, 30, 1140, 340, "Signal analogique : variation CONTINUE", accent=BLUE)
    o += axes(130, 120, 900, 200)
    pts = " ".join(f"{130+i*9:.0f},{320-95-70*math.sin(i/12)-18*math.sin(i/4.3):.1f}" for i in range(0, 100))
    o += f'<polyline points="{pts}" fill="none" stroke="{BLUE}" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>'
    for v, yy in (("5 V", 140), ("3 V", 215), ("0 V", 320)):
        o += T(118, yy + 5, v, 16, 700, INK, "end")
    o += T(600, 355, "toutes les valeurs intermédiaires sont possibles (ex. température, lumière, son)", 17, 600, MUTED)
    return figure(W, 400, o)


def f_numerique():
    o = panel(30, 30, 1140, 340, "Signal numérique : états DISCRETS", accent=GREEN)
    o += axes(130, 120, 900, 200)
    d = "M130,320"
    x = 130
    for hi, w in ((0, 60), (1, 110), (0, 90), (1, 70), (0, 80), (1, 120), (0, 70), (1, 90), (0, 130)):
        y = 140 if hi else 320
        d += f" L{x},{y} L{x+w},{y}"
        x += w
    o += f'<path d="{d}" fill="none" stroke="{GREEN}" stroke-width="6" stroke-linejoin="round"/>'
    o += T(118, 145, "5 V", 16, 700, INK, "end") + T(118, 325, "0 V", 16, 700, INK, "end")
    o += T(1090, 160, "1 (HIGH)", 17, 800, GREEN, "end") + T(1090, 300, "0 (LOW)", 17, 800, GREEN, "end")
    o += T(600, 355, "seulement deux niveaux : 0 ou 1 (ex. bouton, interrupteur, LED)", 17, 600, MUTED)
    return figure(W, 400, o)


def f_adc():
    o = ""
    rows = [("0,0 V", "0"), ("1,0 V", "204"), ("2,5 V", "512"), ("5,0 V", "1023")]
    o += T(180, 50, "Signal analogique", 20, 800, INK) + T(600, 50, "Convertisseur ADC", 20, 800, INK) + T(1020, 50, "Valeur numérique", 20, 800, INK)
    o += block(470, 70, 260, 330, "ADC", "10 bits", AMBER)
    for i, (v, n) in enumerate(rows):
        y = 120 + i * 80
        o += f'<rect x="90" y="{y-26}" width="180" height="52" rx="12" fill="#eaf0ff" stroke="{BLUE}" stroke-width="3"/>' + T(180, y + 9, v, 26, 800, BLUE)
        o += arrow(270, y, 470, y, INK, 4) + arrow(730, y, 930, y, INK, 4)
        o += f'<rect x="930" y="{y-26}" width="180" height="52" rx="12" fill="#e8f7ee" stroke="{GREEN}" stroke-width="3"/>' + T(1020, y + 9, n, 26, 800, GREEN)
    o += T(600, 440, "0 V → 0  ·  5 V → 1023  ·  valeur ≈ U / 5 × 1023", 19, 700, INK)
    return figure(W, 475, o)


def f_pwm():
    o = ""
    lv = [(0, "PWM 0 % : moteur arrêté"), (25, "PWM 25 % : vitesse lente"), (50, "PWM 50 % : vitesse moyenne"), (75, "PWM 75 % : vitesse rapide"), (100, "PWM 100 % : vitesse maximale")]
    for i, (p, lab) in enumerate(lv):
        y = 70 + i * 100
        o += T(40, y - 12, lab, 18, 800, INK, "start") + f'<line x1="520" y1="{y+30}" x2="1160" y2="{y+30}" stroke="#d5dce8" stroke-width="2"/>'
        d = f"M520,{y+30}"; x = 520
        for k in range(5):
            w = 128
            hi = w * p / 100
            if p == 0: d += f" L{x+w},{y+30}"
            elif p == 100: d += f" L{x},{y-20} L{x+w},{y-20}"
            else: d += f" L{x},{y-20} L{x+hi},{y-20} L{x+hi},{y+30} L{x+w},{y+30}"
            x += w
        o += f'<path d="{d}" fill="none" stroke="{GREEN if p else MUTED}" stroke-width="5" stroke-linejoin="round"/>'
        o += g(430, y + 5, f'<rect x="-60" y="-14" width="{120*p/100}" height="28" rx="6" fill="{AMBER}"/><rect x="-60" y="-14" width="120" height="28" rx="6" fill="none" stroke="{INK}" stroke-width="2"/>')
    o += T(1100, 40, "tension moyenne ≈ 5 V × rapport cyclique", 16, 700, MUTED, "end")
    return figure(W, 590, o)


def f_moteur():
    o = g(300, 150, sym("MOTOR", s=2.2)) + g(750, 160, motor(), 1.6)
    o += T(300, 240, "symbole du moteur DC", 19, 700, INK) + T(750, 270, "moteur à courant continu", 19, 700, INK)
    return figure(W, 310, o)


def f_continuite():
    o = sym("D", 300, 130, s=1.8) + g(560, 130, '<path d="M-22,-16 L-22,16 L-6,16 L14,32 L14,-32 L-6,-16 Z" fill="#1b2742"/>' + ''.join(f'<path d="M{26+i*16},{-14-i*6} Q{36+i*16},0 {26+i*16},{14+i*6}" fill="none" stroke="{AMBER}" stroke-width="5" stroke-linecap="round"/>' for i in range(3)), 1.5)
    o += T(300, 215, "symbole « diode »", 19, 700, INK) + T(640, 215, "bip sonore", 19, 700, INK)
    o += chip(600, 270, "Le bip signale que le circuit est continu (résistance proche de 0 Ω)", GREEN, w=860, size=18)
    return figure(W, 320, o)


def f_dht11():
    o = panel(30, 30, 560, 520, "DHT11 nu (4 broches)", accent=BLUE) + panel(610, 30, 560, 520, "Module (3 broches)", accent=GREEN)
    o += f'<g filter="url(#shs)"><rect x="170" y="110" width="180" height="140" rx="8" fill="#3b9bd6"/></g>'
    for i in range(7): o += f'<rect x="{190+i*22}" y="130" width="12" height="90" rx="4" fill="#2878a8"/>'
    for i in range(4): o += f'<rect x="{185+i*45}" y="250" width="8" height="90" fill="url(#metalH)"/>' + badge(189 + i * 45, 365, i + 1, BLUE, 15)
    for i, l in enumerate(("VCC", "DATA", "NC", "GND")): o += T(189 + i * 45, 405, l, 14, 700, INK)
    o += s_wire([(189, 440), (189, 480), (234, 480)]) + sym("R", 270, 480, s=0.6) + T(270, 462, "10 kΩ", 13, 700, INK) + s_wire([(306, 480), (324, 480), (324, 440)], INK, 3)
    o += T(300, 520, "résistance pull-up entre VCC et DATA", 14, 600, MUTED)
    o += f'<g filter="url(#shs)"><rect x="740" y="130" width="300" height="190" rx="8" fill="#2f9a68"/></g><rect x="800" y="150" width="120" height="110" rx="8" fill="#3b9bd6"/>'
    for i in range(5): o += f'<rect x="{818+i*20}" y="165" width="10" height="70" rx="3" fill="#2878a8"/>'
    for i, l in enumerate(("DATA", "VCC", "GND")): o += f'<rect x="{800+i*50}" y="320" width="8" height="60" fill="url(#metalH)"/>' + T(804 + i * 50, 410, l, 16, 700, INK)
    o += T(890, 470, "le module intègre déjà\nla résistance pull-up", 16, 600, MUTED)
    return figure(W, 580, o)


def f_dht11_cablage():
    o = block(60, 60, 260, 300, "", None, BLUE) + T(130, 100, "Arduino", 22, 800, INK)
    for i, (l, y) in enumerate((("5V", 120), ("Dx", 210), ("GND", 320))): o += T(300, y + 6, l, 20, 800, INK, "end")
    o += block(820, 60, 300, 300, "", None, GREEN) + T(960, 100, "DHT11", 22, 800, INK)
    for l, y in (("1  VCC", 120), ("2  DATA", 210), ("3  NC", 265), ("4  GND", 320)): o += T(830, y + 6, l, 18, 800, INK, "start")
    o += s_wire([(320, 120), (560, 120)]) + s_wire([(560, 120), (820, 120)]) + dot(560, 120)
    o += s_wire([(320, 210), (820, 210)]) + dot(560, 210)
    o += sym("R", 560, 165, 90, s=1.125)
    o += T(600, 160, "10 kΩ", 18, 800, INK, "start") + T(600, 184, "pull-up", 15, 600, MUTED, "start")
    o += s_wire([(320, 320), (820, 320)]) + T(570, 345, "GND commun", 15, 600, MUTED)
    o += T(940, 290, "(non connectée)", 14, 600, MUTED, "start")
    return figure(W, 400, o)


def f_dht11_chrono():
    o = f'<rect x="60" y="90" width="260" height="260" fill="{BLUE}" opacity=".12"/><rect x="320" y="90" width="300" height="260" fill="{AMBER}" opacity=".16"/><rect x="620" y="90" width="520" height="260" fill="{GREEN}" opacity=".12"/>'
    o += chip(190, 70, "1 · Démarrage", BLUE, w=220) + chip(470, 70, "2 · Réponse du capteur", AMBER, w=270) + chip(880, 70, "3 · 40 bits de données", GREEN, w=300)
    d = "M60,130 L200,130 L200,320 L320,320 L320,130 L350,130 L350,320 L450,320 L450,130 L540,130 L540,320 L620,320"
    x = 620
    import random
    r = random.Random(4)
    for k in range(10):
        hi = 22 if r.random() < .55 else 60
        d += f" L{x},130 L{x+16},130 L{x+16},320 L{x+16+0},320"
        d = d.replace(f" L{x+16},320 L{x+16+0},320", f" L{x+16},320")
        x += 52
    d += " L1140,130"
    o += f'<path d="{d}" fill="none" stroke="{INK}" stroke-width="5" stroke-linejoin="round"/>'
    o += T(130, 380, "Arduino tire DATA\nà l'état bas ≥ 18 ms", 16, 700, INK) + T(470, 380, "DHT11 répond :\n80 µs bas + 80 µs haut", 16, 700, INK) + T(880, 380, "humidité (16 bits) · température (16 bits)\nsomme de contrôle (8 bits)", 16, 700, INK)
    o += T(46, 135, "1", 16, 800, INK, "end") + T(46, 325, "0", 16, 800, INK, "end")
    return figure(W, 440, o)


def f_portees():
    o = ""
    for i, (nom, d, c, ic) in enumerate((("Bluetooth", "≈ 10 m", BLUE, "Arduino + smartphone"), ("Wi-Fi", "≈ 50 m", GREEN, "routeur"), ("NFC", "quelques cm", RED, "deux téléphones"))):
        cx = 220 + i * 380
        rad = (150, 170, 70)[i]
        o += f'<circle cx="{cx}" cy="200" r="{rad}" fill="{c}" opacity=".13" stroke="{c}" stroke-width="4" stroke-dasharray="10 8"/>'
        if i == 0: o += g(cx - 40, 200, f'<rect x="-26" y="-18" width="52" height="36" rx="5" fill="#1b2742"/>' + T(0, 6, "UNO", 12, 800, "#fff")) + g(cx + 45, 200, '<rect x="-16" y="-30" width="32" height="60" rx="6" fill="#2a2d33"/><rect x="-12" y="-24" width="24" height="44" rx="2" fill="#7cc4f0"/>')
        if i == 1: o += g(cx, 205, f'<rect x="-34" y="-8" width="68" height="22" rx="5" fill="#2a2d33"/><path d="M-20,-8 L-24,-34 M20,-8 L24,-34" stroke="#2a2d33" stroke-width="4"/>')
        if i == 2: o += g(cx - 18, 200, '<rect x="-14" y="-26" width="28" height="52" rx="5" fill="#2a2d33"/>', 1) + g(cx + 18, 200, '<rect x="-14" y="-26" width="28" height="52" rx="5" fill="#2a2d33"/>')
        o += T(cx, 400, nom, 26, 800, c) + T(cx, 436, d, 22, 700, INK) + T(cx, 466, ic, 16, 500, MUTED)
    return figure(W, 500, o)


def f_hc05():
    o = f'<g filter="url(#sh)"><rect x="320" y="70" width="560" height="260" rx="12" fill="#1f6fb0"/></g><rect x="400" y="110" width="150" height="120" rx="6" fill="#0f2a44"/>' + T(475, 178, "HC-05", 26, 800, "#cfe3f5")
    o += f'<circle cx="760" cy="150" r="12" fill="{RED}"/>' + T(760, 195, "LED d'état", 15, 700, "#fff")
    for i, (l, d) in enumerate((("STATE", "état de connexion"), ("RXD", "réception"), ("TXD", "émission"), ("GND", "masse"), ("VCC", "alimentation 5 V"), ("EN / KEY", "mode AT"))):
        x = 370 + i * 90
        o += f'<rect x="{x-5}" y="330" width="10" height="46" fill="url(#metalH)"/>' + f'<g transform="translate({x},392) rotate(60)">{T(0,0,l,17,800,INK,"start")}</g>'
        o += f'<g transform="translate({x},392) rotate(60)">{T(0,20,d,13,500,MUTED,"start")}</g>' if False else ""
    o += callout(760, 150, 960, 120, "LED de statut", "start", 17, bold=True)
    return figure(W, 560, o)


def f_chaine_bt():
    items = [("Smartphone", "application BT", BLUE), ("Module HC-05", "Bluetooth 2,4 GHz", AMBER), ("Arduino UNO", "RX / TX (UART)", GREEN), ("LED / actionneur", "commandé", RED)]
    o = ""
    for i, (t, s, c) in enumerate(items):
        x = 40 + i * 290
        o += block(x, 90, 240, 150, t, s, c)
        if i < 3: o += arrow(x + 248, 165, x + 282, 165, INK, 4) + arrow(x + 282, 165, x + 248, 165, INK, 4) if i < 2 else arrow(x + 248, 165, x + 282, 165, INK, 4)
    o += T(40 + 250 + 140 - 130 + 120, 75, "ondes radio", 15, 700, BLUE) if False else ""
    o += T(300, 285, "liaison Bluetooth (sans fil)", 16, 700, BLUE) + T(590, 285, "liaison série UART (filaire)", 16, 700, AMBER) + T(880, 285, "broche de sortie", 16, 700, GREEN)
    return figure(W, 330, o)


def f_moniteur():
    o = f'<g filter="url(#sh)"><rect x="60" y="30" width="1080" height="360" rx="14" fill="#0f1729"/></g><rect x="60" y="30" width="1080" height="46" rx="14" fill="#232d4a"/>' + T(100, 62, "Moniteur série — 9600 baud", 18, 700, "#cfd8ea", "start")
    lines = [("→ AT", "#8ab4ff"), ("← OK", "#6ee7a5"), ("→ AT+NAME=CIEL_BT", "#8ab4ff"), ("← OK", "#6ee7a5"), ("→ AT+PSWD=1234", "#8ab4ff"), ("← OK", "#6ee7a5")]
    for i, (l, c) in enumerate(lines): o += T(100, 130 + i * 46, l, 26, 600, c, "start", extra='font-family="monospace"')
    o += T(1100, 370, "→ envoyé par l'utilisateur   ← réponse du module", 15, 600, "#9fb0d0", "end")
    return figure(W, 420, o)


def f_cablage_hc05():
    o = block(60, 50, 280, 480, "", None, BLUE) + block(860, 50, 280, 480, "", None, AMBER) + T(130, 90, "Arduino UNO", 22, 800, INK) + T(1070, 90, "HC-05", 22, 800, INK)
    for l, y in (("5V", 120), ("GND", 200), ("D11 (TX)", 290), ("D10 (RX)", 460)): o += T(330, y + 6, l, 20, 800, INK, "end")
    for l, y in (("VCC", 120), ("GND", 200), ("RXD", 290), ("TXD", 460), ("EN / KEY", 510)): o += T(870, y + 6, l, 20, 800, INK, "start")
    o += s_wire([(340, 120), (860, 120)], RED) + s_wire([(340, 200), (860, 200)], "#222")
    o += s_wire([(340, 290), (460, 290)]) + sym("R", 500, 290, s=0.8) + s_wire([(540, 290), (860, 290)]) + dot(640, 290) + T(500, 262, "1 kΩ", 16, 800, INK)
    o += s_wire([(640, 290), (640, 320)]) + sym("R", 640, 360, 90, s=0.8) + s_wire([(640, 400), (640, 410)]) + gnd(640, 410) + T(680, 366, "2 kΩ", 16, 800, INK, "start")
    o += s_wire([(860, 460), (340, 460)], GREEN)
    o += T(1000, 560, "EN / KEY laissée non connectée (mode normal)", 15, 600, MUTED)
    o += T(600, 40, "pont diviseur 1 kΩ / 2 kΩ : 5 V → 3,3 V", 17, 800, INK)
    return figure(W, 590, o)


def f_lcd_cmp():
    o = panel(30, 30, 560, 470, "LCD classique : 10 fils", accent=RED) + panel(610, 30, 560, 470, "LCD I2C : 4 fils", accent=GREEN)
    o += block(60, 130, 130, 190, "Arduino", None, BLUE) + f'<rect x="420" y="170" width="150" height="110" rx="8" fill="#2a8f6a"/>' + T(495, 232, "LCD 16×2", 17, 800, "#fff")
    import random
    r = random.Random(2)
    for k in range(10): o += f'<path d="M190,{140+k*17} C300,{130+r.random()*160} 330,{150+r.random()*140} 420,{175+k*10}" fill="none" stroke="{["#d63f3f","#2f5bea","#e99a14","#222","#17935c"][k%5]}" stroke-width="3"/>'
    o += T(310, 470, "câblage encombré, risque d'erreurs", 16, 600, MUTED)
    o += block(640, 130, 130, 190, "Arduino", None, BLUE) + f'<rect x="1000" y="170" width="150" height="110" rx="8" fill="#2a8f6a"/>' + T(1075, 232, "LCD 16×2", 17, 800, "#fff") + f'<rect x="960" y="285" width="190" height="34" rx="5" fill="#1b2742"/>' + T(1055, 308, "module I2C", 15, 700, "#fff")
    for k, (l, c) in enumerate((("VCC", "#d63f3f"), ("GND", "#222"), ("SDA", "#2f5bea"), ("SCL", "#e99a14"))):
        o += s_wire([(770, 160 + k * 38), (960, 160 + k * 38)], c) + T(865, 152 + k * 38, l, 14, 800, c)
    o += T(890, 470, "4 fils seulement : propre et simple", 16, 700, GREEN)
    return figure(W, 530, o)


def f_i2c():
    o = block(60, 190, 240, 140, "Arduino UNO", "maître", BLUE)
    o += f'<line x1="300" y1="230" x2="1130" y2="230" stroke="{AMBER}" stroke-width="8"/><line x1="300" y1="290" x2="1130" y2="290" stroke="{GREEN}" stroke-width="8"/>' + T(330, 218, "SDA", 17, 800, AMBER, "start") + T(330, 318, "SCL", 17, 800, GREEN, "start")
    for i, (t, a) in enumerate((("LCD I2C", "0x27"), ("Capteur T°", "0x48"), ("Horloge RTC", "0x68"))):
        x = 500 + i * 220
        o += block(x - 90, 60 if False else 380, 180, 100, t, None, GREEN) + s_wire([(x - 20, 380), (x - 20, 230)], AMBER, 4) + s_wire([(x + 20, 380), (x + 20, 290)], GREEN, 4) + dot(x - 20, 230, 7, AMBER) + dot(x + 20, 290, 7, GREEN)
        o += chip(x, 500, "adresse " + a, INK, w=170, size=16)
    o += T(180, 360, "2 fils seulement", 16, 700, INK)
    return figure(W, 540, o)


def f_lcd_annote():
    o = panel(30, 30, 640, 400, "Face avant : 16 colonnes × 2 lignes", accent=BLUE) + panel(690, 30, 480, 400, "Face arrière : module I2C", accent=GREEN)
    o += f'<rect x="70" y="110" width="560" height="140" rx="10" fill="#2a8f6a"/><rect x="95" y="130" width="510" height="100" rx="4" fill="#bfe6a8"/>'
    for r in range(2):
        for c in range(16):
            o += f'<rect x="{100+c*31.5}" y="{136+r*46}" width="27" height="40" rx="2" fill="#a5d18d" stroke="#7fb06a" stroke-width="1"/>'
    o += T(112, 100, "(0,0)", 15, 800, INK, "start") + T(620, 100, "(15,0)", 15, 800, INK, "end") + T(112, 275, "(0,1)", 15, 800, INK, "start") + T(620, 275, "(15,1)", 15, 800, INK, "end")
    o += T(350, 330, "32 emplacements de caractères", 18, 700, INK) + T(350, 362, "lcd.setCursor(colonne, ligne)", 17, 600, MUTED, extra='font-family="monospace"')
    o += f'<rect x="740" y="120" width="380" height="110" rx="8" fill="#2a8f6a"/><rect x="800" y="150" width="200" height="50" rx="4" fill="#1b2742"/>' + T(900, 182, "PCF8574", 18, 800, "#cfd8ea")
    for i, l in enumerate(("GND", "VCC", "SDA", "SCL")): o += f'<rect x="{770+i*60}" y="230" width="9" height="50" fill="url(#metalH)"/>' + T(774 + i * 60, 305, l, 15, 800, INK)
    o += T(930, 370, "4 broches vers l'Arduino\n(+ potentiomètre de contraste)", 16, 600, MUTED)
    return figure(W, 460, o)


def f_pyramide():
    o = ""
    levels = [("Tests système", "produit complet en conditions réelles", RED), ("Tests d'intégration", "sous-ensembles assemblés", AMBER), ("Tests unitaires", "composant par composant", GREEN)]
    for i, (t, sub, c) in enumerate(levels):
        y = 40 + i * 120
        t0, t1 = 340 + i * 160, 340 + (i + 1) * 160
        o += f'<path d="M{600-t0/2},{y} L{600+t0/2},{y} L{600+t1/2},{y+112} L{600-t1/2},{y+112} Z" fill="{c}" stroke="#fff" stroke-width="5"/>'
        o += T(600, y + 54, t, 26, 800, "#fff") + T(600, y + 86, sub, 17, 600, "#fff")
    return figure(W, 410, o)


def f_proto_tests():
    cols = ["N°", "Fonctionnalité testée", "Action", "Résultat attendu", "Résultat obtenu", "Statut"]
    ws = [60, 230, 250, 220, 220, 120]
    rows = [("1", "Alimentation 5 V", "Mesurer VCC", "5 V ± 0,25 V", "4,98 V", "✅"), ("2", "LED de statut", "Allumer la LED", "LED allumée", "LED allumée", "✅"), ("3", "Liaison HC-05", "Envoyer « AT »", "Réponse « OK »", "Pas de réponse", "❌")]
    o = ""; x0 = 40; y0 = 60
    x = x0
    for c, w in zip(cols, ws):
        o += f'<rect x="{x}" y="{y0}" width="{w}" height="56" fill="{INK}"/>' + T(x + w / 2, y0 + 35, c, 17, 800, "#fff"); x += w
    for r, row in enumerate(rows):
        x = x0
        for k, (v, w) in enumerate(zip(row, ws)):
            fill = "#fff" if r % 2 == 0 else "#f4f7fc"
            if k == 5: fill = "#e6f6ec" if v == "✅" else "#fdeaea"
            o += f'<rect x="{x}" y="{y0+56+r*64}" width="{w}" height="64" fill="{fill}" stroke="#d5dce8" stroke-width="1.5"/>' + T(x + w / 2, y0 + 56 + r * 64 + 39, v, 18 if k < 5 else 26, 600, INK); x += w
    return figure(W, 330, o)


def f_symboles_projet():
    o = ""
    o += panel(40, 40, 360, 300, "Résistance", accent=BLUE) + sym("R", 220, 190, s=2) + T(220, 290, "rectangle (CEI) ou zigzag (ANSI)", 15, 600, MUTED)
    o += panel(420, 40, 360, 300, "LED", accent=RED) + sym("LED", 600, 200, s=2) + T(600, 290, "anode (A) → cathode (K), flèches de lumière", 15, 600, MUTED)
    o += panel(800, 40, 360, 300, "Blocs (modules)", accent=GREEN)
    o += block(825, 100, 150, 130, "Arduino", "broches", BLUE) + block(1005, 100, 130, 130, "HC-05", "broches", AMBER) + T(980, 290, "bloc rectangulaire + broches", 15, 600, MUTED)
    return figure(W, 380, o)


def f_bom():
    cols = ["Réf.", "Désignation", "Qté", "Valeur / type", "Réf. fournisseur", "Fournisseur", "Prix unit. HT", "Prix total HT"]
    ws = [70, 200, 70, 150, 160, 130, 130, 130]
    rows = [("R1", "Résistance", "1", "220 Ω – 1/4 W", "xxx-220R", "Fournisseur A", "0,05 €", "0,05 €"), ("D1", "LED rouge 5 mm", "1", "rouge, 20 mA", "xxx-LED5R", "Fournisseur A", "0,10 €", "0,10 €")]
    o = ""; x0 = 40; y0 = 60; x = x0
    for c, w in zip(cols, ws):
        o += f'<rect x="{x}" y="{y0}" width="{w}" height="52" fill="#217346"/>' + T(x + w / 2, y0 + 32, c, 14, 800, "#fff"); x += w
    for r, row in enumerate(rows):
        x = x0
        for v, w in zip(row, ws):
            o += f'<rect x="{x}" y="{y0+52+r*52}" width="{w}" height="52" fill="{"#fff" if r%2==0 else "#f1f8f4"}" stroke="#cfd8d2" stroke-width="1.5"/>' + T(x + w / 2, y0 + 52 + r * 52 + 32, v, 15, 600, INK); x += w
    return figure(W, 260, o)


def f_zones():
    o = ""
    for i, (t, d, c) in enumerate((("SAVOIR", "connaissances théoriques\nprotocoles, composants", BLUE), ("SAVOIR-FAIRE", "démonstration en direct\nschéma, BOM", AMBER), ("SAVOIR-ÊTRE", "communication, posture\ngestion des questions", GREEN))):
        x = 40 + i * 390
        o += f'<rect x="{x}" y="50" width="360" height="270" rx="20" fill="{c}" opacity=".13" stroke="{c}" stroke-width="4"/>' + T(x + 180, 120, t, 30, 800, c) + T(x + 180, 190, d, 20, 600, INK)
    return figure(W, 360, o)


def f_frise():
    o = ""
    for i, (t, d, c, x, w) in enumerate((("Contexte", "0 – 1 min", RED, 40, 260), ("Solution", "1 – 3 min", AMBER, 300, 520), ("Résultats", "3 – 4 min", GREEN, 820, 340))):
        o += f'<rect x="{x}" y="90" width="{w}" height="150" rx="10" fill="{c}" stroke="#fff" stroke-width="4"/>' + T(x + w / 2, 160, t, 30, 800, "#fff") + T(x + w / 2, 198, d, 20, 700, "#fff")
    o += T(170, 275, "client · problème posé", 16, 600, MUTED) + T(560, 275, "montage Arduino · composants · démonstration", 16, 600, MUTED) + T(990, 275, "tests · taux de conformité", 16, 600, MUTED)
    o += arrow(40, 60, 1160, 60, INK, 3) + T(600, 45, "temps de la présentation (4 min)", 16, 700, INK)
    return figure(W, 310, o)


def f_jury():
    o = ""
    st = [("1  Écouter", "Je reformule la question", BLUE), ("2  Réfléchir", "Je prends 5 secondes", AMBER), ("3  Répondre", "Avec mes mots et un exemple concret", GREEN)]
    for i, (t, d, c) in enumerate(st):
        x = 50 + i * 380
        o += block(x, 60, 320, 150, t, d, c)
        if i < 2: o += arrow(x + 326, 135, x + 374, 135, INK, 5)
    o += s_wire([(210, 210), (210, 290), (940, 290), (940, 262)], MUTED, 3, "8 6") + f'<rect x="300" y="268" width="560" height="44" rx="22" fill="#fdeaea" stroke="{RED}" stroke-width="2.5"/>' + T(580, 297, "Si je ne sais pas : je le dis honnêtement et je propose une piste", 17, 700, RED)
    return figure(W, 340, o)


def f_grille():
    o = ""
    o += f'<rect x="40" y="40" width="1120" height="52" fill="{INK}"/>' + T(100, 74, "Compétence", 18, 800, "#fff", "start") + T(480, 74, "Niveau 1", 18, 800, "#fff") + T(760, 74, "Niveau 2", 18, 800, "#fff") + T(1040, 74, "Niveau 3", 18, 800, "#fff")
    lv = [("Non acquis", "l'élève ne peut pas expliquer\nson montage", "#fbd5d5", RED, 480), ("En cours d'acquisition", "explication partielle,\nquelques oublis", "#fde8c4", AMBER, 760), ("Acquis", "explication claire et\ncomplète avec exemples", "#cfeedd", GREEN, 1040)]
    o += f'<rect x="40" y="92" width="280" height="190" fill="#f4f7fc" stroke="#d5dce8" stroke-width="2"/>' + T(180, 180, "Présenter son\nprojet technique", 20, 800, INK)
    for t, d, bg, c, x in lv:
        o += f'<rect x="{x-140}" y="92" width="280" height="190" fill="{bg}" stroke="#fff" stroke-width="3"/>' + chip(x, 125, t, c, size=15, w=240) + T(x, 190, d, 17, 600, INK)
    return figure(W, 320, o)


FIGS = {"signal_analogique": f_analogique, "signal_numerique": f_numerique, "adc_conversion": f_adc, "pwm_rapport_cyclique": f_pwm, "symbole_moteur": f_moteur,
        "continuite_buzzer": f_continuite, "dht11_brochage": f_dht11, "dht11_cablage": f_dht11_cablage, "dht11_chronogramme": f_dht11_chrono,
        "portees_sans_fil": f_portees, "hc05_brochage": f_hc05, "chaine_bluetooth": f_chaine_bt, "moniteur_serie_at": f_moniteur, "cablage_arduino_hc05": f_cablage_hc05,
        "lcd_classique_vs_i2c": f_lcd_cmp, "bus_i2c": f_i2c, "lcd_i2c_annote": f_lcd_annote, "pyramide_tests": f_pyramide, "protocole_tests": f_proto_tests,
        "symboles_projet": f_symboles_projet, "bom_extrait": f_bom, "soutenance_zones": f_zones, "soutenance_frise": f_frise, "jury_organigramme": f_jury, "grille_criteriee": f_grille}
