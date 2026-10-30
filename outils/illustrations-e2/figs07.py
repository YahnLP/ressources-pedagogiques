from lib import *

W = 1200


def block(x, y, w, h, t, sub=None, col=BLUE):
    o = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="#fff" stroke="{col}" stroke-width="3"/>'
    o += f'<rect x="{x}" y="{y}" width="{w}" height="8" rx="4" fill="{col}"/>'
    o += T(x + w / 2, y + h / 2 + (2 if sub else 8), t, 21, 800, INK)
    if sub:
        o += T(x + w / 2, y + h / 2 + 26, sub, 15, 500, MUTED)
    return o


def f_mcu():
    o = f'<rect x="30" y="30" width="900" height="520" rx="22" fill="{PANEL}" stroke="#cdd7e8" stroke-width="3"/>'
    o += T(60, 70, "MICROCONTRÔLEUR", 22, 800, MUTED, "start") + T(900, 70, "ex. ATmega328P (Arduino UNO)", 16, 600, MUTED, "end")
    o += f'<rect x="478" y="95" width="26" height="440" rx="8" fill="{INK}"/>' + T(491, 520, "BUS", 14, 800, "#fff", extra='transform="rotate(-90 491 520)"') if False else f'<rect x="478" y="95" width="26" height="440" rx="8" fill="{INK}"/>'
    left = [("CPU", "exécute les instructions", AMBER), ("Mémoire FLASH", "programme (32 Ko)", BLUE), ("Mémoire SRAM", "variables (2 Ko)", BLUE), ("EEPROM", "données conservées (1 Ko)", BLUE)]
    right = [("Entrées / sorties numériques", "GPIO : 0 ou 1", GREEN), ("Convertisseur ADC", "analogique → 0…1023", GREEN), ("Timers / PWM", "temps, signaux MLI", GREEN), ("Communication", "UART · I²C · SPI", GREEN)]
    for i, (t, sub, c) in enumerate(left):
        y = 110 + i * 105
        o += block(70, y, 360, 84, t, sub, c) + f'<line x1="430" y1="{y+42}" x2="478" y2="{y+42}" stroke="{INK}" stroke-width="5"/>'
    for i, (t, sub, c) in enumerate(right):
        y = 110 + i * 105
        o += block(552, y, 360, 84, t, sub, c) + f'<line x1="504" y1="{y+42}" x2="552" y2="{y+42}" stroke="{INK}" stroke-width="5"/>'
    for i in range(4):
        y = 152 + i * 105
        o += arrow(912, y, 1010, y, INK, 5)
    o += T(1090, 110, "broches\ndu composant", 17, 700, INK)
    return figure(W, 585, o)


def f_chaine():
    steps = [("CAPTEUR", "LDR", BLUE, "mesure la lumière"), ("LECTURE", "analogRead(A0)", AMBER, "valeur 0…1023"), ("DÉCISION", "if (val < seuil)", AMBER, "compare au seuil"), ("ACTIONNEUR", "digitalWrite(13, HIGH)", GREEN, "allume la LED")]
    o = ""
    for i, (t, code, col, d) in enumerate(steps):
        x = 36 + i * 292
        o += panel(x, 40, 255, 300, t, accent=col)
        if i == 0:
            o += g(x + 128, 190, ldr(), 1.1)
        elif i == 1:
            o += g(x + 128, 150, '<rect x="-60" y="-34" width="120" height="68" rx="10" fill="#1b2742"/>' + T(0, 8, "A0", 32, 800, "#fff") + '<path d="M-60,0 H-90 M60,0 H90" stroke="#9aa4b2" stroke-width="4"/>', 1.0)
            o += T(x + 128, 235, "tension → nombre", 16, 600, MUTED)
        elif i == 2:
            o += g(x + 128, 170, '<path d="M0,-60 L70,0 L0,60 L-70,0 Z" fill="#fff4dc" stroke="#e99a14" stroke-width="4"/>' + T(0, 8, "val < 300 ?", 18, 800, INK), 1.0)
        else:
            o += g(x + 128, 165, led(lit=True), .8)
        o += T(x + 128, 290, code, 17, 700, INK, extra='font-family="monospace"')
        o += T(x + 128, 318, d, 15, 500, MUTED)
        if i < 3:
            o += arrow(x + 258, 190, x + 288, 190, INK, 5)
    return figure(W, 380, o)


def f_analogread():
    o = panel(30, 40, 1140, 450, fill="#fff")
    o += g(130, 240, potentiometer(), .9)
    o += s_wire([(170, 255), (250, 255)], INK, 4) + T(210, 240, "curseur", 14, 600, MUTED)
    o += '<rect x="250" y="190" width="170" height="130" rx="14" fill="#1b2742"/>' + T(335, 245, "CAN", 28, 800, "#fff") + T(335, 280, "10 bits", 17, 600, "#cfd8ea") + T(335, 175, "broche A0", 16, 700, INK)
    o += arrow(420, 255, 500, 255, INK, 5)
    # jauge
    x0, x1, y = 540, 1120, 210
    o += f'<rect x="{x0}" y="{y}" width="{x1-x0}" height="56" rx="10" fill="#eaf0fb" stroke="#c4d0e6" stroke-width="2"/>'
    o += f'<rect x="{x0}" y="{y}" width="{(x1-x0)*0.5}" height="56" rx="10" fill="{BLUE}" opacity=".85"/>'
    for v, t, vt in ((0, "0", "0 V"), (0.5, "512", "2,5 V"), (1, "1023", "5 V")):
        xx = x0 + (x1 - x0) * v
        o += f'<line x1="{xx}" y1="{y-12}" x2="{xx}" y2="{y+68}" stroke="{INK}" stroke-width="3"/>' + T(xx, y - 24, t, 24, 800, INK) + T(xx, y + 98, vt, 20, 700, BLUE)
    o += T(830, 120, "analogRead(A0) renvoie un entier de 0 à 1023", 21, 800, INK)
    o += T(830, 400, "valeur ≈ U / 5 × 1023", 26, 800, BLUE)
    o += T(830, 440, "pas de mesure ≈ 4,9 mV  (5 V / 1023)", 17, 600, MUTED)
    return figure(W, 530, o)


def f_blink():
    o = panel(30, 30, 560, 480, fill="#fff")
    o += f'<rect x="50" y="50" width="520" height="440" rx="14" fill="#0f1729"/>'
    code = [("void setup() {", "#8ab4ff"), ("  pinMode(LED_BUILTIN, OUTPUT);", "#e8ecf5"), ("}", "#8ab4ff"), ("", ""),
            ("void loop() {", "#8ab4ff"), ("  digitalWrite(LED_BUILTIN, HIGH);", "#e8ecf5"), ("  delay(1000);", "#e8ecf5"),
            ("  digitalWrite(LED_BUILTIN, LOW);", "#e8ecf5"), ("  delay(1000);", "#e8ecf5"), ("}", "#8ab4ff")]
    for i, (l, c) in enumerate(code):
        o += T(72, 95 + i * 36, l, 21, 500, c, "start", extra='font-family="monospace" xml:space="preserve"')
    o += chip(150, 475, "exécuté 1 fois au démarrage", AMBER, w=270, size=14) if False else ""
    o += f'<rect x="40" y="75" width="8" height="90" rx="4" fill="{AMBER}"/>' + T(560, 100, "1 fois", 16, 800, AMBER, "end") + f'<rect x="40" y="215" width="8" height="215" rx="4" fill="{GREEN}"/>' + T(560, 240, "en boucle", 16, 800, GREEN, "end")
    o += panel(620, 30, 550, 480, "Ce que fait la carte", accent=BLUE)
    X0, X1 = 680, 1130
    for r, (lab, hi) in enumerate((("LED allumée (HIGH)", True),)):
        pass
    y_hi, y_lo = 190, 290
    path = f"M{X0},{y_lo}"
    x = X0
    seg = (X1 - X0) / 4
    state = False
    for i in range(4):
        y_new = y_hi if i % 2 == 0 else y_lo
        path += f" L{x},{y_new} L{x+seg},{y_new}"
        x += seg
    o += f'<path d="{path}" fill="none" stroke="{BLUE}" stroke-width="5" stroke-linejoin="round"/>'
    o += f'<line x1="{X0}" y1="{y_lo}" x2="{X1}" y2="{y_lo}" stroke="{MUTED}" stroke-dasharray="4 6" stroke-width="2"/>'
    o += T(X0 - 8, y_hi + 6, "HIGH", 16, 800, GREEN, "end") + T(X0 - 8, y_lo + 6, "LOW", 16, 800, RED, "end")
    for i in range(3):
        o += T(X0 + seg * (i + .5), 345, "1 s", 17, 800, INK)
    o += g(760, 440, led(lit=True), .55) + T(840, 440, "allumée", 16, 700, GREEN, "start")
    o += g(1020, 440, led(lit=False), .55) + T(1090, 440, "éteinte", 16, 700, MUTED, "start")
    o += T(895, 130, "La LED intégrée (broche 13) clignote\nune seconde sur deux", 18, 700, INK)
    return figure(W, 540, o)


def f_pot_pwm():
    o = ""
    items = [("Potentiomètre", "analogRead(A0)", "valeur 0…1023", BLUE), ("map()", "map(v, 0, 1023, 0, 255)", "ramène à 0…255", AMBER), ("PWM", "analogWrite(9, pwm)", "rapport cyclique", GREEN), ("LED", "luminosité", "variable", GREEN)]
    for i, (t, c, d, col) in enumerate(items):
        x = 36 + i * 292
        o += panel(x, 30, 255, 190, t, accent=col)
        o += T(x + 128, 130, c, 15, 700, INK, extra='font-family="monospace"') + T(x + 128, 165, d, 16, 500, MUTED)
        if i < 3:
            o += arrow(x + 258, 125, x + 288, 125, INK, 5)
    o += panel(30, 250, 1140, 290, "Sortie PWM : même fréquence, rapport cyclique différent", accent=INK)
    for i, (v, d) in enumerate((("pwm = 64", 0.25), ("pwm = 128", 0.5), ("pwm = 255", 1.0))):
        x = 60 + i * 375
        o += T(x + 160, 335, f"{v}  →  {int(d*100)} %", 20, 800, INK)
        base, top = 480, 380
        path = f"M{x},{base}"
        px = x
        for k in range(3):
            w = 100
            hi = w * d
            path += f" L{px},{top} L{px+hi},{top} L{px+hi},{base} L{px+w},{base}" if d < 1 else f" L{px},{top} L{px+w},{top}"
            px += w
        o += f'<path d="{path}" fill="none" stroke="{GREEN}" stroke-width="5" stroke-linejoin="round"/>'
        o += T(x + 160, 520, ["LED peu lumineuse", "luminosité moyenne", "luminosité maximale"][i], 16, 600, MUTED)
    return figure(W, 570, o)


FIGS = {"microcontroleur_blocs": f_mcu, "chaine_information": f_chaine, "analogread": f_analogread, "blink": f_blink, "potentiometre_pwm": f_pot_pwm}
