"""Schémas remplaçant les dessins en texte (Première et Terminale)."""
from hl import *
import math


def driver(vcc_label, rc, rb, led_name, in_label, extra, q="Q1 = BC547"):
    o = vcc(330, 100, vcc_label) + s_wire([(330, 100), (330, 120)])
    o += vrun(330, 120, 195, [(160, "R", f"Rc = {rc}", {})], 1, 52) + vrun(330, 195, 262, [(228, "LED", led_name, {})], 1, 58)
    o += s_wire([(330, 262), (330, 275), (372, 275), (372, 290)]) + npn(350, 335, 1.0) + s_wire([(372, 379), (372, 430)]) + gnd(372, 430) + T(372, 490, "GND", 17, 800, INK)
    o += hrun(335, 100, 300, [(200, "R", f"Rb = {rb}", {})]) + T(100, 380, in_label, 16, 800, BLUE, "start") + T(440, 335, q, 18, 800, INK, "start") + T(440, 296, "C", 18, 800, MUTED, "start") + T(440, 380, "E", 18, 800, MUTED, "start") + T(285, 360, "B", 18, 800, MUTED)
    return o + extra


def f_drv1(): return figure(W, 530, driver("+5 V", "220 Ω", "10 kΩ", "D1", "Signal_IN (label de net)", chip(850, 200, "Rc = (VCC − V_F − V_CE_sat) / I_F", BLUE, w=460, size=17) + chip(850, 255, "Rb = (V_in − V_BE) / I_B", GREEN, w=360, size=17)))
def f_drv3(): return figure(W, 530, driver("+9 V (BT1, pile 9 V)", "150 Ω", "10 kΩ", "D1 rouge", "J1 pin 2 : signal d'entrée", T(100, 410, "J1 pin 1 : GND", 16, 800, MUTED, "start") + chip(850, 220, "R2 = résistance du collecteur", BLUE, w=380, size=17), "Q1 = BC547 (TO-92)"))


def ne555(R1, R2, C1, C3, R3, note=None, nr1="R1", nr2="R2", nc1="C1", nc2="C2"):
    bx, by, bw, bh = 460, 150, 180, 200
    o = f'<rect x="{bx}" y="{by}" width="{bw}" height="{bh}" rx="8" fill="#fff" stroke="{INK}" stroke-width="3.5"/>' + T(562, 262, "NE555", 22, 800, INK) + f'<path d="M{bx+bw/2-18},{by} a18,18 0 0 0 36,0" fill="none" stroke="{INK}" stroke-width="3"/>'
    pins = {"4": (bx + 40, by, "up", "RESET"), "8": (bx + 140, by, "up", "VCC"), "1": (bx + 40, by + bh, "dn", "GND"), "5": (bx + 140, by + bh, "dn", "CTRL"), "3": (bx, by + 50, "l", "OUT"), "2": (bx, by + 100, "l", "TRIG"), "6": (bx, by + 150, "l", "THR"), "7": (bx + bw, by + 150, "r", "DIS")}
    for n, (x, y, d, t) in pins.items():
        tx = {"up": (x, y + 24), "dn": (x, y - 12), "l": (x + 10, y + 6), "r": (x - 10, y + 6)}[d]
        o += T(tx[0], tx[1], f"{n} {t}", 13, 700, MUTED, "start" if d == "l" else "end" if d == "r" else "middle")
    o += s_wire([(150, 70), (900, 70)], RED, 3) + T(120, 76, "+5 V", 17, 800, RED, "end")
    o += s_wire([(pins["4"][0], 150), (pins["4"][0], 70)]) + s_wire([(pins["8"][0], 150), (pins["8"][0], 70)]) + dot(pins["4"][0], 70) + dot(pins["8"][0], 70)
    o += vrun(760, 70, 300, [(160, "R", f"{nr1} = {R1}", {})], 1, 52) + s_wire([(640, 300), (760, 300)]) + dot(760, 300) + vrun(760, 300, 430, [(365, "R", f"{nr2} = {R2}", {})], 1, 52)
    o += s_wire([(760, 430), (400, 430), (400, 250), (460, 250)]) + s_wire([(400, 300), (460, 300)]) + dot(400, 300) + dot(400, 430)
    o += vrun(400, 430, 520, [(485, "C", f"{nc1} = {C1}", {})], -1, 52) + gnd(400, 520)
    o += s_wire([(pins["1"][0], 350), (pins["1"][0], 380)]) + gnd(pins["1"][0], 380) + vrun(pins["5"][0], 350, 450, [(405, "C", f"{nc2} = 100 nF", {})], 1, 52) + gnd(pins["5"][0], 450)
    o += hrun(200, 130, 460, [(300, "R", f"R3 = {R3}", {})]) + vrun(130, 200, 340, [(270, "LED", "LED", {})], -1, 58) + gnd(130, 340)
    if note: o += chip(600, 590, note, INK, w=900, size=15)
    return figure(W, 630, o)


def f_ne555_a(): return ne555("10 kΩ", "47 kΩ", "10 µF", "", "330 Ω", "f ≈ 1 / (0,693 × (R1 + 2 × R2) × C1) ≈ 0,5 Hz : la LED clignote toutes les 2 s environ")
def f_ne555_b(): return ne555("10 kΩ", "68 kΩ", "10 µF", "", "150 Ω", "7805 : 12 V → 5 V (C1 100 nF, C2 10 µF hors schéma) · PWR_FLAG sur +5 V et GND", nr1="Ra", nr2="Rb", nc1="C3", nc2="C4")


def f_bus():
    o = block(60, 150, 260, 230, "Arduino Uno", "alimentation par USB (5 V)", BLUE) + block(760, 40, 380, 190, "MPU-6050", "accéléromètre / gyroscope (I²C)", GREEN) + block(760, 280, 380, 220, "W25Q32", "mémoire flash ou carte SD (SPI)", AMBER)
    for i, (t, y) in enumerate((("SDA = A4 (broche 18)", 100), ("SCL = A5 (broche 19)", 150))): o += s_wire([(320, 215 + i * 30), (540, 215 + i * 30), (540, y + 20), (760, y + 20)], GREEN, 4) + T(550, y + 10, t, 15, 700, GREEN, "start")
    for i, (t, y) in enumerate((("MOSI = D11", 340), ("MISO = D12", 385), ("SCLK = D13", 430), ("CS = D10", 475))): o += s_wire([(320, 290 + i * 22), (480 + i * 0, 290 + i * 22), (480, y), (760, y)], AMBER, 4) + T(500, y - 6, t, 15, 700, "#a8700b", "start")
    o += chip(540, 560, "pull-up 4,7 kΩ vers +3,3 V ou +5 V sur SDA et SCL", INK, w=600, size=15)
    return figure(W, 600, o)


def f_esp32():
    o = ""
    rows = [("Xtensa LX6 double cœur · 240 MHz", "520 Ko de RAM · 4 Mo de Flash SPI", BLUE), ("Wi-Fi 802.11 b/g/n · 2,4 GHz", "Bluetooth 4.2 : BLE et Classic", GREEN), ("34 GPIO · 18 ADC · 2 DAC", "UART · SPI · I²C · PWM · capteurs tactiles", AMBER)]
    o += f'<rect x="60" y="30" width="700" height="360" rx="22" fill="{PANEL}" stroke="#cdd7e8" stroke-width="3"/>' + T(410, 70, "ESP32 DevKit v1", 24, 800, INK)
    for i, (a, b, c) in enumerate(rows): o += f'<rect x="90" y="{95+i*95}" width="640" height="82" rx="12" fill="#fff" stroke="{c}" stroke-width="3"/>' + T(410, 130 + i * 95, a, 20, 800, INK) + T(410, 158 + i * 95, b, 16, 600, MUTED)
    o += chip(1000, 140, "GPIO : 3,3 V", GREEN, w=240, size=18) + chip(1000, 200, "USB : 5 V", AMBER, w=240, size=18) + T(1000, 275, "Les GPIO ne supportent\npas le 5 V direct", 17, 800, RED)
    return figure(W, 420, o)


def f_archi_tp():
    o = panel(60, 80, 360, 230, "ESP32 DevKit", accent=BLUE) + panel(780, 80, 360, 230, "PC (Ubuntu / Windows)", accent=GREEN)
    o += T(240, 170, "DHT22 → broche 4", 17, 700, INK) + T(240, 205, "LED → broche 2", 17, 700, INK) + T(960, 170, "Mosquitto 2.x : broker local", 17, 700, INK) + T(960, 205, "mosquitto_pub", 17, 700, INK) + T(960, 235, "mosquitto_sub", 17, 700, INK)
    o += arrow(420, 175, 780, 175, BLUE, 5) + arrow(780, 235, 420, 235, GREEN, 5) + T(600, 160, "MQTT · port 1883", 17, 800, BLUE) + T(600, 262, "abonnement LED", 16, 700, GREEN) + T(600, 60, "Wi-Fi 2,4 GHz", 18, 800, MUTED)
    for i, (t, d) in enumerate((("ciel/[nom]/capteur", "l'ESP32 publie température et humidité"), ("ciel/[nom]/led", "l'ESP32 s'abonne et reçoit ON / OFF"), ("ciel/[nom]/status", "l'ESP32 publie son état (LWT)"))): o += chip(220, 360 + i * 46, t, INK, w=300, size=15) + T(400, 366 + i * 46, d, 16, 600, MUTED, "start")
    return figure(W, 520, o)


def f_boitier_dessus():
    o = '<g filter="url(#sh)"><rect x="120" y="50" width="760" height="360" rx="20" fill="#e9edf3" stroke="#8a95a5" stroke-width="4"/></g>'
    o += '<rect x="300" y="150" width="280" height="150" rx="8" fill="#1c7a46"/>' + T(440, 232, "ESP32 (PCB)", 20, 800, "#fff") + '<circle cx="760" cy="95" r="14" fill="#d63f3f"/>' + T(760, 130, "LED", 15, 800, INK) + '<rect x="670" y="82" width="46" height="26" rx="6" fill="#8a95a5"/>' + T(693, 126, "RESET", 13, 800, INK)
    o += '<rect x="660" y="190" width="150" height="90" rx="6" fill="#2b4a8a"/>' + T(735, 242, "Batterie", 17, 800, "#fff") + '<rect x="360" y="340" width="90" height="46" rx="6" fill="#5d6b86"/>' + T(405, 368, "DHT22", 15, 800, "#fff") + '<rect x="640" y="372" width="90" height="30" rx="6" fill="#222"/>' + T(685, 393, "USB-C", 14, 800, "#fff")
    o += T(190, 100, "Antenne ↑", 17, 800, INK, "start") + arrow(820, 330, 940, 330, MUTED, 4) + T(950, 336, "côté accès au câble USB", 16, 700, MUTED, "start")
    return figure(W, 450, o)


def f_developpe():
    o = ""
    for x, y, w, h, tx, c in ((480, 15, 240, 110, "Couvercle (L × l)", BLUE), (480, 125, 240, 80, "Côté 4 (L × h)", "#8a56d0"), (480, 205, 240, 130, "Fond (L × l)", GREEN), (480, 335, 240, 80, "Côté 2 (L × h)", "#8a56d0"), (300, 205, 180, 130, "Côté 1 (l × h)", AMBER), (720, 205, 180, 130, "Côté 3 (l × h)", AMBER)):
        o += f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{c}" opacity=".18" stroke="{c}" stroke-width="3"/>' + T(x + w / 2, y + h / 2 + 6, tx, 17, 800, INK)
    o += T(60, 120, "Boîte : 6 faces\nà découper puis plier", 18, 800, MUTED, "start") + T(940, 120, "traits pleins : découpe\nlignes de jonction : pli", 15, 700, MUTED, "start")
    return figure(W, 440, o)


def f_filtre_lc():
    o = T(120, 190, "Signal", 18, 800, INK, "end") + hrun(200, 130, 800, [(300, "L", "L = 100 µH", {})]) + dot(500, 200) + s_wire([(500, 200), (500, 250)]) + sym("C", 500, 290, rot=90) + T(540, 296, "C = 100 nF", 18, 700, INK, "start") + s_wire([(500, 330), (500, 360)]) + gnd(500, 360)
    o = o.replace('hrun', 'hrun') + s_wire([(500, 200), (800, 200)]) + T(830, 206, "Signal filtré", 18, 800, GREEN, "start")
    o += chip(600, 470, "fc = 1 / (2π √(L C)) ≈ 50 kHz : tout ce qui dépasse 50 kHz est atténué", INK, w=800, size=17)
    return figure(W, 520, o)


def f_plan_masse():
    o = panel(30, 30, 570, 440, "Plan de masse continu (recommandé)", accent=GREEN) + panel(620, 30, 550, 440, "Plan de masse fendu (à éviter)", accent=RED)
    for x0, slot in ((60, False), (650, True)):
        o += f'<rect x="{x0}" y="150" width="500" height="14" fill="{COPPER}"/>' + T(x0 + 250, 135, "F.Cu : piste de signal →", 15, 800, INK) + f'<rect x="{x0}" y="164" width="500" height="22" fill="#7d8a74"/>'
        if not slot: o += f'<rect x="{x0}" y="186" width="500" height="22" fill="#4a5a3a"/>' + T(x0 + 250, 228, "B.Cu : plan GND continu", 15, 800, "#2a3a2a") + f'<path d="M{x0+470},176 H{x0+30}" stroke="{GREEN}" stroke-width="5" marker-end="url(#arr)"/>' + T(x0 + 250, 270, "le courant de retour passe juste sous la piste", 16, 700, GREEN) + T(x0 + 250, 300, "→ boucle minimale → rayonnement minimal ✓", 17, 800, GREEN)
        else: o += f'<rect x="{x0}" y="186" width="230" height="22" fill="#4a5a3a"/><rect x="{x0+270}" y="186" width="230" height="22" fill="#4a5a3a"/>' + T(x0 + 250, 228, "B.Cu : plan GND avec une fente", 15, 800, "#2a3a2a") + f'<path d="M{x0+470},176 L{x0+470},300 H{x0+30} V176" fill="none" stroke="{RED}" stroke-width="5" marker-end="url(#arr)"/>' + f'<rect x="{x0+230}" y="186" width="40" height="22" fill="#fff"/>' + T(x0 + 250, 340, "la fente impose un long détour au courant de retour", 16, 700, RED) + T(x0 + 250, 370, "→ grande boucle, grande antenne, diaphonie ✗", 17, 800, RED)
    return figure(W, 500, o)


def f_regles_masse():
    o = ""
    ttl = [("1 · Point de masse unique (étoile)", "pas de courant parasite dans les fils communs", "basse fréquence analogique"), ("2 · Plan de masse (réseau)", "impédance faible partout", "numérique et haute fréquence"), ("3 · Masses séparées", "jonction unique vers la terre", "circuits mixtes"), ("4 · Pas de boucle de masse", "deux chemins = une antenne", "toujours évitée")]
    for i, (t, a, b) in enumerate(ttl):
        x = 25 + (i % 2) * 580; y = 25 + (i // 2) * 290; o += panel(x, y, 570, 270, t, accent=[BLUE, GREEN, AMBER, RED][i]); cx, cy = x + 285, y + 118
        if i == 0: o += ''.join(f'<path d="M{cx},{cy} L{cx+int(120*math.cos(a))},{cy+int(70*math.sin(a))}" stroke="{INK}" stroke-width="3"/><circle cx="{cx+int(120*math.cos(a))}" cy="{cy+int(70*math.sin(a))}" r="9" fill="{BLUE}"/>' for a in (0.4, 1.4, 2.6, 3.7, 5.2)) + f'<circle cx="{cx}" cy="{cy}" r="12" fill="{INK}"/>'
        elif i == 1: o += f'<rect x="{cx-140}" y="{cy-20}" width="280" height="40" fill="#4a5a3a"/>' + ''.join(f'<path d="M{cx-110+k*70},{cy-20} v-35" stroke="{INK}" stroke-width="3"/><circle cx="{cx-110+k*70}" cy="{cy-58}" r="8" fill="{GREEN}"/>' for k in range(4))
        elif i == 2: o += f'<path d="M{cx-140},{cy-30} H{cx} V{cy+10}" stroke="{BLUE}" stroke-width="4" fill="none"/><path d="M{cx-140},{cy+50} H{cx} V{cy+10}" stroke="{AMBER}" stroke-width="4" fill="none"/>' + f'<circle cx="{cx}" cy="{cy+10}" r="10" fill="{INK}"/>' + gnd(cx + 40, cy + 10) + T(cx - 150, cy - 40, "masse analogique", 14, 700, BLUE, "start") + T(cx - 150, cy + 70, "masse numérique", 14, 700, "#a8700b", "start") + s_wire([(cx, cy + 10), (cx + 40, cy + 10)])
        else: o += f'<rect x="{cx-110}" y="{cy-50}" width="70" height="60" fill="#fff" stroke="{INK}" stroke-width="3"/><rect x="{cx+40}" y="{cy-50}" width="70" height="60" fill="#fff" stroke="{INK}" stroke-width="3"/><path d="M{cx-75},{cy+10} V{cy+60} H{cx+75} V{cy+10}" stroke="{RED}" stroke-width="4" fill="none"/><path d="M{cx-40},{cy-20} H{cx+40}" stroke="{RED}" stroke-width="4"/>' + T(cx, cy + 82, "boucle = antenne", 15, 800, RED)
        o += T(x + 285, y + 232, a, 16, 700, INK) + T(x + 285, y + 256, b, 14, 600, MUTED)
    return figure(W, 620, o)


def f_erreurs_erc():
    o = vcc(400, 120, "+5 V") + s_wire([(400, 120), (400, 140)]) + vrun(400, 140, 240, [(190, "R", "R1  (valeur vide)", {})], 1, 52)
    o += s_wire([(400, 240), (400, 260)]) + g(400, 320, sym("D", 0, 0, rot=-90)) + T(440, 326, "D1 (LED à l'envers)", 18, 700, INK, "start") + s_wire([(400, 360), (400, 420)]) + gnd(400, 420) + s_wire([(400, 285), (400, 285)])
    o += f'<circle cx="400" cy="378" r="12" fill="none" stroke="{RED}" stroke-width="4"/>'
    for n, (x, y, t) in enumerate(((620, 190, "R1 sans valeur (champ Value vide)"), (620, 270, "pas de PWR_FLAG sur le net +5 V"), (620, 340, "LED branchée à l'envers : cathode vers +5 V"), (620, 410, "ERC « Pin not connected » sur la broche K")), 1): o += badge(x, y, n, RED, 15) + T(x + 26, y + 6, t, 17, 700, INK, "start")
    o += badge(360, 190, 1, RED, 13) + badge(440, 120, 2, RED, 13) + badge(360, 320, 3, RED, 13) + badge(440, 378, 4, RED, 13)
    return figure(W, 520, o)


def f_carte_sonde():
    o = block(60, 150, 280, 240, "ESP32 DevKit v1", None, BLUE)
    br = [(70, "GPIO 4", "DHT22 : température et humidité", "R1 = 10 kΩ (pull-up DATA ↔ 3V3)", GREEN), (170, "GPIO 2", "LED rouge → R2 = 220 Ω → GND", "", RED), (270, "GPIO 34", "potentiomètre 10 kΩ entre 3V3 et GND", "point milieu sur GPIO 34", AMBER), (370, "3V3", "C1 = 100 µF électrolytique vers GND", "découplage de l'alimentation", "#8a56d0")]
    for y, p, a, b, c in br:
        o += s_wire([(340, 270), (420, 270), (420, y + 30), (480, y + 30)], c, 4) + f'<rect x="480" y="{y}" width="660" height="80" rx="12" fill="#fff" stroke="{c}" stroke-width="3"/>' + T(500, y + 34, p, 17, 800, c, "start") + T(620, y + 34, a, 17, 700, INK, "start") + T(620, y + 62, b, 14, 600, MUTED, "start")
    return figure(W, 480, o)


def f_chaine_alim():
    o = block(380, 30, 440, 76, "Source", "batterie LiPo ou USB 5 V", AMBER)
    st = [("Condensateur d'entrée 10 µF", "céramique : filtre les transitoires", BLUE), ("Régulateur 3,3 V", "LDO AMS1117 ou convertisseur buck MP2315", GREEN), ("Condensateurs de sortie", "10 µF (stabilité) et 100 nF (filtrage HF)", BLUE), ("Alimentation 3,3 V", "vers l'ESP32 et les capteurs", RED)]
    y = 106
    for t, s, c in st: o += arrow(600, y, 600, y + 34, INK, 4) + block(380, y + 36, 440, 76, t, s, c); y += 110
    o += block(850, 30, 300, 100, "Protections (option)", "diode Schottky SS14 (anti-inversion)\nfusible réarmable PTC (surintensité)".split("\n")[0], MUTED) + T(1000, 160, "fusible réarmable PTC (surintensité)", 14, 600, MUTED)
    return figure(W, y + 50, o)


def f_archi_a3():
    o = block(40, 190, 200, 110, "Capteur", None, BLUE) + arrow(240, 245, 300, 245, INK, 4) + block(300, 150, 260, 190, "ESP32", "calcule les KPI, compare aux seuils", GREEN)
    o += arrow(560, 210, 640, 140, RED, 4) + block(640, 60, 520, 110, "Alarme LOCALE", "LED rouge, buzzer ou relais : immédiat, sans réseau", RED) + arrow(560, 285, 640, 350, BLUE, 4) + block(640, 300, 520, 110, "Si le réseau est disponible", "publication JSON sur MQTT / AWS → tableau de bord CloudWatch", BLUE)
    o += chip(600, 450, "Avantage : réaction en moins d'une seconde, même sans Wi-Fi", INK, w=720, size=17)
    return figure(W, 490, o)


def dip_(name, left, right, w=300):
    o = f'<rect x="{500}" y="40" width="{w-60}" height="{len(left)*60+40}" rx="8" fill="#25282e"/><path d="M{500+(w-60)/2-26},40 a26,26 0 0 0 52,0" fill="#fff"/>' + T(500 + (w - 60) / 2, 40 + (len(left) * 60 + 40) / 2 + 10, name, 28, 800, "#fff")
    for i, (l, r) in enumerate(zip(left, right)):
        y = 90 + i * 60; o += f'<rect x="470" y="{y-8}" width="30" height="16" fill="#c0c6cf"/><rect x="{500+w-60}" y="{y-8}" width="30" height="16" fill="#c0c6cf"/>' + T(460, y + 6, l, 17, 700, INK, "end") + T(500 + w - 20 + 20, y + 6, r, 17, 700, INK, "start") + T(512, y + 5, str(i + 1), 13, 700, "#9aa4b2", "start") + T(500 + w - 72, y + 5, str(2 * len(left) - i), 13, 700, "#9aa4b2", "end")
    return o


def f_brochage_ne555(): return figure(W, 340, dip_("NE555", ["GND", "TRIG", "OUTPUT", "RESET"], ["VCC", "DISCHARGE", "THRESHOLD", "CONTROL VOLTAGE"], 320))


def f_brochage_7805():
    o = '<g filter="url(#sh)"><rect x="400" y="60" width="400" height="170" rx="10" fill="#25282e"/><rect x="400" y="30" width="400" height="44" rx="6" fill="#aeb6c2"/><circle cx="600" cy="52" r="10" fill="#fff"/></g>' + T(600, 160, "7805", 34, 800, "#fff")
    for x, n, t, d in ((450, "1", "Vin", "non régulée (12 V)"), (600, "2", "GND", "masse + languette"), (750, "3", "Vout", "régulée (5 V)")):
        o += f'<rect x="{x-6}" y="230" width="12" height="70" fill="#c0c6cf"/>' + T(x, 330, f"({n}) {t}", 19, 800, INK) + T(x, 356, d, 13, 600, MUTED)
    o += chip(200, 150, "C1 = 100 nF sur Vin", BLUE, w=270, size=15) + chip(1000, 150, "C2 = 10 µF sur Vout", GREEN, w=270, size=15)
    return figure(W, 400, o)


def f_familles():
    fam = [("Conception et fabrication de PCB", [("IPC-2221", "conception : pistes, isolements, perçages"), ("IPC-A-610", "acceptabilité des assemblages : classes 1, 2, 3")], BLUE), ("Sécurité et fiabilité", [("CEI 61010-1", "sécurité : isolements, tensions, marquage"), ("CEI 60068-2", "tests d'environnement : 85 °C, −40 °C, 85 % HR")], AMBER), ("Management de la qualité", [("ISO 9001:2015", "processus de validation documentés"), ("ISO/CEI 17025", "laboratoires : accréditation, incertitudes")], GREEN)]
    o = ""
    for i, (t, items, c) in enumerate(fam):
        x = 25 + i * 385; o += panel(x, 25, 370, 330, f"Famille {i+1}", accent=c) + T(x + 185, 95, t, 18, 800, INK)
        for k, (a, b) in enumerate(items): o += f'<rect x="{x+20}" y="{125+k*110}" width="330" height="95" rx="10" fill="#fff" stroke="{c}" stroke-width="2"/>' + T(x + 185, 158 + k * 110, a, 20, 800, c) + T(x + 185, 188 + k * 110, b, 13, 600, MUTED)
    return figure(W, 380, o)


FIGS = {"driver_transistor_s01": f_drv1, "driver_transistor_s03": f_drv3, "ne555_astable_tp": f_ne555_a, "ne555_astable_dossier": f_ne555_b, "bus_arduino_i2c_spi": f_bus, "esp32_caracteristiques": f_esp32, "architecture_mqtt_tp": f_archi_tp,
        "boitier_vue_dessus": f_boitier_dessus, "developpe_boitier": f_developpe, "filtre_lc": f_filtre_lc, "plan_masse_continu_fendu": f_plan_masse, "regles_masse": f_regles_masse, "schema_erreurs_erc": f_erreurs_erc,
        "carte_sonde": f_carte_sonde, "chaine_alimentation_decouplage": f_chaine_alim, "architecture_a3": f_archi_a3, "brochage_ne555": f_brochage_ne555, "brochage_7805": f_brochage_7805, "familles_normes": f_familles}
