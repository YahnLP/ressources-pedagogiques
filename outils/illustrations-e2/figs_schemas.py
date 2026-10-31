"""Schémas « manuel premium » remplaçant des dessins en caractères (Première S05, S07, S08, S10, S12, S13)."""
from hl import *
from figs07 import block
from figs_final import grid
import math

W = 1200


def _i2c_wave():
    """SCL, SDA pour START + adresse 0x68 + W + ACK + STOP (x normalisés 0..1)."""
    bits = [0, 1, 1, 0, 1, 0, 0, 0, 0, 0]  # 0x68 = 0110 1000 ; R/W=0 (W) ; ACK=0
    bits = [0, 1, 1, 0, 1, 0, 0, 0] + [0, 0]
    n = len(bits) + 1
    scl, sda, t = [(0, 1)], [(0, 1)], 0
    # idle puis START (SDA descend alors que SCL haut)
    seg = lambda a: a / (n + 3)
    scl = [(0, 1), (seg(1), 1), (seg(1), 0)]
    sda = [(0, 1), (seg(0.6), 1), (seg(0.6), 0), (seg(1.0), 0)]
    cur = 0
    for k, b in enumerate(bits[:9]):
        t0 = 1 + k
        scl += [(seg(t0), 0), (seg(t0 + 0.25), 0), (seg(t0 + 0.25), 1), (seg(t0 + 0.75), 1), (seg(t0 + 0.75), 0)]
        if b != cur:
            sda += [(seg(t0), cur), (seg(t0), b)]
            cur = b
    tend = 1 + 9
    sda += [(seg(tend), cur), (seg(tend), 0), (seg(tend + 0.75), 0), (seg(tend + 0.75), 1), (seg(n + 3), 1)]
    scl += [(seg(tend), 0), (seg(tend + 0.25), 0), (seg(tend + 0.25), 1), (seg(n + 3), 1)]
    return scl, sda, seg, tend


def f_saleae():
    o = ui_win(40, 24, 1120, 460, "", bar="#2b2f3a")
    o = o.replace('fill="#fbfcfe"', 'fill="#161a22"', 1) + T(600, 47, "Logic 2 — Saleae (analyseur logique professionnel)", 15, 700, "#cbd5e1")
    # barre d'outils
    o += '<rect x="40" y="58" width="1120" height="52" fill="#1f2430"/>'
    o += f'<circle cx="84" cy="84" r="17" fill="#22c55e"/><path d="M78,75 L93,84 L78,93 Z" fill="#fff"/>' + T(112, 90, "Start", 16, 800, "#e8ecf4", "start")
    o += f'<rect x="180" y="68" width="34" height="32" rx="6" fill="#3a2020"/><rect x="190" y="78" width="14" height="14" fill="#ef4444"/>' + T(226, 90, "Stop", 16, 800, "#e8ecf4", "start")
    o += chip(520, 84, "Échantillonnage : 8 MS/s", "#3b4560", w=290, size=14) + chip(780, 84, "Durée : 100 ms", "#3b4560", w=170, size=14)
    # panneau canaux
    o += '<rect x="40" y="110" width="150" height="374" fill="#1a1f2a"/>' + T(115, 138, "Canaux", 14, 800, "#9fb0d0")
    for k, (nm, sub, col) in enumerate((("CH0", "(SCL)", "#fbbf24"), ("CH1", "(SDA)", "#38bdf8"))):
        y = 190 + k * 110
        o += f'<rect x="52" y="{y-26}" width="126" height="64" rx="8" fill="#232a38"/><rect x="52" y="{y-26}" width="7" height="64" rx="3" fill="{col}"/>' + T(115, y, nm, 18, 800, col) + T(115, y + 24, sub, 15, 700, "#cbd5e1")
    # chronogrammes
    o += '<rect x="190" y="110" width="700" height="360" fill="#0f131a"/>'
    for gx in range(1, 7): o += f'<line x1="{190+gx*100}" y1="110" x2="{190+gx*100}" y2="470" stroke="#1d2433"/>'
    scl, sda, seg, tend = _i2c_wave()
    X0, X1 = 215, 870
    def pl(pts, y0, h, col):
        return f'<polyline points="{" ".join(f"{X0+px*(X1-X0):.0f},{y0+h-py*h:.0f}" for px, py in pts)}" fill="none" stroke="{col}" stroke-width="3" stroke-linejoin="miter"/>'
    o += pl(scl, 160, 60, "#fbbf24") + pl(sda, 270, 60, "#38bdf8")
    # annotations décodées
    def ann(t0, t1, txt, col="#16a34a"):
        xa, xb = X0 + seg(t0) * (X1 - X0), X0 + seg(t1) * (X1 - X0)
        return f'<rect x="{xa:.0f}" y="352" width="{xb-xa:.0f}" height="34" rx="8" fill="{col}"/>' + T((xa + xb) / 2, 375, txt, 14, 800, "#fff")
    o += ann(0.6, 1.0, "S", "#a855f7") + ann(1.0, 8.9, "Adresse 0x68 · W", "#2563eb") + ann(8.9, 9.95, "ACK", "#16a34a") + ann(9.95, 10.75, "P", "#a855f7")
    o += T(540, 420, "Trame décodée : [0x68 W] [ACK] …", 17, 800, "#e8ecf4")
    o += T(540, 448, "START (S)  ·  octet adresse + bit d'écriture  ·  acquittement (ACK)  ·  STOP (P)", 13, 600, "#9fb0d0")
    # panneau analyseurs
    o += '<rect x="890" y="110" width="270" height="360" fill="#1a1f2a"/>' + T(1025, 138, "Analyseurs", 14, 800, "#9fb0d0")
    o += '<rect x="904" y="154" width="242" height="70" rx="8" fill="#232a38"/>' + T(1025, 180, "I2C", 17, 800, "#e8ecf4") + T(1025, 204, "SCL : CH0 · SDA : CH1", 13, 600, "#cbd5e1")
    o += f'<rect x="904" y="240" width="242" height="38" rx="8" fill="none" stroke="#475569" stroke-width="2" stroke-dasharray="5 4"/>' + T(1025, 265, "+  Ajouter un analyseur", 14, 700, "#9fb0d0")
    for k, nm in enumerate(("SPI", "UART asynchrone", "1-Wire", "CAN…")):
        o += f'<rect x="904" y="{296+k*40}" width="242" height="32" rx="6" fill="#1f2735"/>' + T(920, 318 + k * 40, nm, 14, 700, "#cbd5e1", "start")
    for n, (bx, by) in enumerate(((56, 84), (168, 134), (790, 205), (1140, 134)), 1):
        o += badge(bx, by, n, RED, 14)
    return figure(W, 550, o + T(600, 520, "1  barre d'outils    2  canaux    3  chronogrammes et trame décodée    4  panneau des analyseurs", 16, 800, INK))


def f_mqtt_seq():
    o = ""
    xs = (200, 600, 1000)
    names = (("ESP32", "capteur de température", BLUE), ("Broker MQTT", "(Mosquitto)", AMBER), ("Tableau de bord", "(abonné)", GREEN))
    for x, (n, sub, c) in zip(xs, names):
        o += block(x - 100, 30, 200, 80, n, sub, c) + f'<line x1="{x}" y1="112" x2="{x}" y2="610" stroke="{c}" stroke-width="3" stroke-dasharray="8 7"/>'
    msgs = [(0, 1, "CONNECT", BLUE, ""), (1, 0, "CONNACK", BLUE, ""), (2, 1, "CONNECT", BLUE, ""), (1, 2, "CONNACK", BLUE, ""),
            (2, 1, "SUBSCRIBE", GREEN, "« je veux maison/salon/temperature »"), (1, 2, "SUBACK", GREEN, ""),
            (0, 1, "PUBLISH 22.5", RED, "topic : maison/salon/temperature"), (1, 2, "PUBLISH 22.5", RED, "le broker redistribue")]
    groups = ((0, 3, "Connexion", BLUE), (4, 5, "Abonnement", GREEN), (6, 7, "Publication", RED))
    for a, b, lab, col in groups:
        y0 = 134 + a * 56 - 24; y1 = 134 + b * 56 + 30
        o += f'<rect x="60" y="{y0}" width="1080" height="{y1-y0}" rx="12" fill="{col}" opacity=".07"/>' + T(80, y0 + 22, lab, 15, 800, col, "start")
    for i, (a, b, lab, col, note) in enumerate(msgs):
        y = 150 + i * 56
        x1, x2 = xs[a], xs[b]
        o += arrow(x1 + (6 if x2 > x1 else -6), y, x2 + (-8 if x2 > x1 else 8), y, col, 4) + T((x1 + x2) / 2, y - 10, lab, 16, 800, col)
        if note: o += T((x1 + x2) / 2, y + 24, note, 13, 600, MUTED)
    o += chip(600, 640, "Un abonnement doit exister AVANT la publication pour recevoir le message en direct", INK, w=900, size=15)
    return figure(W, 690, o)


def f_nodered_ui():
    o = ui_win(30, 24, 1140, 520, "Node-RED — http://localhost:1880", bar="#e9ecf3")
    o += '<rect x="30" y="58" width="1140" height="44" fill="#8f0000"/>' + T(60, 87, "Node-RED", 19, 800, "#fff", "start") + f'<rect x="1030" y="66" width="120" height="28" rx="6" fill="#d9232d" stroke="#fff" stroke-width="2"/>' + T(1090, 86, "Déployer", 15, 800, "#fff")
    # palette
    o += '<rect x="30" y="102" width="220" height="442" fill="#f3f4f6"/>' + T(140, 126, "Palette de nœuds", 14, 800, MUTED)
    for k, (nm, c) in enumerate((("inject", "#a6bbcf"), ("debug", "#87a980"), ("function", "#fdd0a2"), ("mqtt in", "#d8bfd8"), ("mqtt out", "#d8bfd8"), ("http in", "#e7e7ae"), ("json", "#e2d96e"))):
        y = 144 + k * 40
        o += f'<rect x="46" y="{y}" width="186" height="30" rx="5" fill="{c}" stroke="#8b9ab0" stroke-width="1.5"/>' + T(139, y + 20, nm, 14, 700, "#1b2742")
    o += T(140, 440, "…", 20, 800, MUTED)
    # zone de flow
    o += '<rect x="250" y="102" width="650" height="442" fill="#fff"/>' + grid(250, 102, 650, 442, 22, "#e6e9f0")
    o += f'<rect x="250" y="102" width="650" height="30" fill="#eef1f6"/>' + T(300, 123, "Flow 1", 14, 800, INK, "start")
    def nd(x, y, nm, c, w=110): return f'<rect x="{x}" y="{y}" width="{w}" height="34" rx="6" fill="{c}" stroke="#7b8aa0" stroke-width="1.6"/><circle cx="{x-1}" cy="{y+17}" r="4" fill="#fff" stroke="#7b8aa0" stroke-width="1.5"/><circle cx="{x+w+1}" cy="{y+17}" r="4" fill="#fff" stroke="#7b8aa0" stroke-width="1.5"/>' + T(x + w / 2, y + 22, nm, 14, 700, "#1b2742")
    o += nd(290, 190, "inject", "#a6bbcf") + nd(450, 190, "function", "#fdd0a2") + nd(610, 190, "debug", "#87a980")
    o += s_wire([(401, 207), (449, 207)], "#7b8aa0", 3) + s_wire([(561, 207), (609, 207)], "#7b8aa0", 3)
    o += nd(290, 300, "mqtt in", "#d8bfd8") + nd(450, 300, "json", "#e2d96e") + nd(610, 300, "gauge", "#b7e0ee")
    o += s_wire([(401, 317), (449, 317)], "#7b8aa0", 3) + s_wire([(561, 317), (609, 317)], "#7b8aa0", 3)
    o += T(345, 175, "Flux 1 : déclencher, transformer, afficher", 13, 600, MUTED, "start") + T(345, 285, "Flux 2 : recevoir en MQTT, décoder, jauge", 13, 600, MUTED, "start")
    o += f'<rect x="700" y="470" width="180" height="40" rx="8" fill="#d9232d"/>' + T(790, 496, "Déployer ✓", 16, 800, "#fff") + T(560, 496, "valide les flux →", 14, 700, MUTED, "end")
    # panneau info/debug
    o += '<rect x="900" y="102" width="270" height="442" fill="#f8fafc"/><rect x="900" y="102" width="270" height="30" fill="#e9ecf3"/>' + T(1035, 123, "Info  ·  Débogage", 14, 800, INK)
    for k, l in enumerate(('22:14:03  msg.payload : 22.5', '22:14:08  msg.payload : 22.6', '22:14:13  msg.payload : 22.6')):
        o += T(914, 160 + k * 30, l, 12, 600, "#475569", "start", extra='font-family="monospace"')
    o += T(1035, 270, "(les messages arrivent ici)", 13, 600, MUTED)
    for n, (bx, by) in enumerate(((232, 118), (860, 118), (600, 400), (884, 478), (1145, 118)), 1): o += badge(bx, by + (0), n, RED, 13)
    o += T(600, 570, "① palette des nœuds   ② zone de flow   ③ un flux = nœuds reliés   ④ Déployer pour valider   ⑤ panneau Débogage", 15, 800, INK)
    return figure(W, 610, o)


def f_climasens_archi():
    o = T(600, 42, "ARCHITECTURE CLIMASENS", 22, 800, INK)
    sens = (("DHT22", "température + humidité", BLUE), ("MQ-2", "air / fumée", AMBER), ("LDR", "luminosité", GREEN))
    for k, (n, sub, c) in enumerate(sens):
        o += block(40, 80 + k * 130, 200, 100, n, sub, c)
        o += arrow(244, 130 + k * 130, 330, 255, INK, 3)
    o += block(330, 170, 270, 170, "ESP32 DevKit v1", "WiFi · PubSubClient (MQTT)", RED) + T(465, 330, "DHTesp + ArduinoJson", 14, 600, MUTED)
    o += arrow(604, 255, 690, 255, INK, 5) + T(647, 236, "WiFi", 15, 800, INK) + T(647, 282, "MQTT", 13, 700, MUTED)
    o += block(690, 190, 190, 130, "Broker MQTT", "Mosquitto", AMBER)
    o += arrow(884, 255, 940, 255, INK, 5)
    o += block(940, 190, 220, 130, "Node-RED", "orchestration", RED)
    o += arrow(1050, 324, 1050, 380, INK, 5)
    o += block(940, 384, 220, 90, "InfluxDB", "stockage", BLUE) + arrow(940, 430, 880, 430, INK, 5) + block(690, 384, 190, 90, "Historique", "courbes dans le temps", GREEN)
    o += arrow(1050, 186, 1050, 140, INK, 5) + block(940, 70, 220, 66, "Dashboard web", None, GREEN)
    o += chip(790, 520, "Alertes (seuils dépassés)", RED, w=330, size=15) + arrow(1000, 520, 1000, 486, RED, 3) if False else ""
    o += chip(800, 540, "+ Alertes lorsque un seuil est dépassé (Node-RED)", RED, w=520, size=15)
    o += chip(250, 540, "capteurs → ESP32 → réseau → serveur → affichage", INK, w=470, size=15)
    return figure(W, 590, o)


def _pwr(x, y, label):
    return f'<line x1="{x-16}" y1="{y}" x2="{x+16}" y2="{y}" stroke="{RED}" stroke-width="4"/>' + T(x, y - 9, label, 15, 800, RED)


def f_climasens_cablage():
    o = f'<rect x="60" y="50" width="240" height="700" rx="14" fill="#fff" stroke="{RED}" stroke-width="4"/><rect x="60" y="50" width="240" height="40" rx="14" fill="{RED}"/>' + T(180, 78, "ESP32 DevKit v1", 18, 800, "#fff")
    for nm, y in (("GPIO4", 150), ("GPIO34 (ADC)", 250), ("GPIO35 (ADC)", 440), ("GPIO2", 690)):
        o += s_wire([(300, y), (360, y)], INK, 4) + T(290, y + 5, nm, 15, 800, INK, "end")
    # DHT22 : rappel 10 kΩ vers 3V3
    o += s_wire([(360, 150), (700, 150)]) + dot(450, 150) + s_wire([(450, 150), (450, 130)]) + sym("R", 450, 90, 90) + s_wire([(450, 50), (450, 40)], RED) + _pwr(450, 40, "3V3") + T(485, 96, "R1 10 kΩ (rappel)", 14, 800, INK, "start")
    o += block(700, 112, 200, 76, "DHT22", "broche DATA", BLUE)
    # MQ-2
    o += s_wire([(360, 250), (700, 250)]) + T(530, 236, "signal analogique", 13, 600, MUTED) + block(700, 212, 200, 76, "MQ-2", "sortie AO", AMBER)
    o += T(930, 242, "VCC → 5 V", 14, 800, INK, "start") + T(930, 266, "GND → GND", 14, 800, INK, "start")
    # LDR + R2 (pont diviseur)
    o += s_wire([(360, 440), (520, 440)]) + dot(520, 440) + s_wire([(520, 440), (520, 400)]) + sym("LDR", 520, 360, 90) + T(560, 366, "LDR", 14, 800, INK, "start") + s_wire([(520, 320), (520, 300)], RED) + _pwr(520, 300, "3V3")
    o += s_wire([(520, 440), (520, 480)]) + sym("R", 520, 520, 90) + T(560, 526, "R2 10 kΩ", 14, 800, INK, "start") + s_wire([(520, 560), (520, 572)]) + gnd(520, 572)
    o += T(700, 440, "pont diviseur : la tension du point", 14, 600, MUTED, "start") + T(700, 462, "sur GPIO35 dépend de la lumière", 14, 600, MUTED, "start")
    # LED d'état
    o += s_wire([(360, 690), (420, 690)]) + sym("R", 460, 690) + T(460, 664, "R3 220 Ω", 14, 800, INK) + s_wire([(500, 690), (600, 690)]) + sym("LED", 640, 690, s=1.1) + T(640, 740, "LED d'état", 14, 800, INK) + s_wire([(684, 690), (780, 690), (780, 710)]) + gnd(780, 710)
    return figure(W, 820, f'<g transform="translate(0,34)">{o}</g>')


def f_cem_pcb_defaillant():
    cu = "#d9a441"; lbl = "#e8f5ec"
    o = f'<rect x="60" y="50" width="1080" height="470" rx="14" fill="#1c7a46" stroke="#0e4a2a" stroke-width="4"/>' + T(100, 84, "PCB — vue de dessus (couche F.Cu)", 17, 800, lbl, "start")
    # circuit intégré
    o += f'<rect x="560" y="140" width="170" height="120" rx="8" fill="#15171b"/>' + T(645, 208, "ESP32", 22, 800, "#fff") + "".join(f'<rect x="{548}" y="{160+k*22}" width="14" height="8" fill="{cu}"/><rect x="{728}" y="{160+k*22}" width="14" height="8" fill="{cu}"/>' for k in range(5))
    # alimentation
    o += f'<path d="M110,164 H550" stroke="{cu}" stroke-width="12" fill="none"/>' + T(130, 146, "VCC", 16, 800, lbl, "start")
    # LED CMS entre le CI et la masse (pastilles + corps)
    o += f'<path d="M742,164 H880" stroke="{cu}" stroke-width="9" fill="none"/>'
    o += f'<rect x="866" y="150" width="36" height="34" rx="4" fill="{cu}"/><rect x="866" y="236" width="36" height="34" rx="4" fill="{cu}"/>'
    o += f'<rect x="868" y="178" width="32" height="64" rx="5" fill="#e5353b" stroke="#a11" stroke-width="2"/><rect x="873" y="186" width="22" height="10" rx="3" fill="#fff" opacity=".4"/>' + T(920, 214, "LED", 15, 800, lbl, "start")
    o += f'<path d="M884,270 V300 H1090" stroke="{cu}" stroke-width="9" fill="none"/>' + T(1090, 288, "GND", 16, 800, lbl, "end")
    # entrée capteur ADC : piste en U
    o += f'<path d="M110,330 H250 V430 H430 V330 H560 V268" stroke="{cu}" stroke-width="8" fill="none" stroke-linejoin="round"/>' + T(110, 318, "Capteur ADC", 15, 800, lbl, "start") + T(560, 296, "GPIO34", 14, 800, lbl, "start")
    o += T(340, 462, "longueur de la piste : 15 cm", 15, 800, "#fff7d6")
    # condensateur de découplage, éloigné
    o += f'<rect x="610" y="400" width="70" height="34" rx="6" fill="#4a90e2" stroke="#2b5fa3" stroke-width="2"/>' + T(645, 423, "100 µF", 15, 800, "#fff")
    o += f'<path d="M645,400 V292" stroke="{cu}" stroke-width="3" stroke-dasharray="5 5"/><path d="M590,262 H700" stroke="none"/>'
    o += T(645, 458, "distance au CI : 5 cm", 15, 800, "#fff7d6")
    # plan de masse (B.Cu) vu en transparence, avec une coupure
    o += f'<rect x="760" y="340" width="150" height="130" fill="#8a6a1c" opacity=".55"/><rect x="930" y="340" width="150" height="130" fill="#8a6a1c" opacity=".55"/>' + T(920, 332, "plan de masse (couche B.Cu)", 14, 700, "#ffe9a8")
    o += f'<path d="M920,340 V470" stroke="#fff" stroke-width="2" stroke-dasharray="3 5" opacity=".6"/>'
    # échelle
    o += f'<line x1="100" y1="500" x2="260" y2="500" stroke="#fff" stroke-width="3"/><line x1="100" y1="494" x2="100" y2="506" stroke="#fff" stroke-width="3"/><line x1="260" y1="494" x2="260" y2="506" stroke="#fff" stroke-width="3"/>' + T(180, 490, "5 cm", 13, 800, "#fff")
    return figure(W, 570, o)


def f_grille_boitier():
    o = '<rect x="60" y="40" width="880" height="500" rx="6" fill="#fff" stroke="#9aa4b8" stroke-width="3"/>'
    for i in range(0, 41):
        x = 60 + i * 22
        if x > 940: break
        o += f'<line x1="{x}" y1="40" x2="{x}" y2="540" stroke="#cfd6e4" stroke-width="{2 if i%5==0 else 1}"/>'
    for j in range(0, 24):
        y = 40 + j * 22
        if y > 540: break
        o += f'<line x1="60" y1="{y}" x2="940" y2="{y}" stroke="#cfd6e4" stroke-width="{2 if j%5==0 else 1}"/>'
    o += f'<line x1="60" y1="560" x2="170" y2="560" stroke="{INK}" stroke-width="4"/><line x1="60" y1="552" x2="60" y2="568" stroke="{INK}" stroke-width="3"/><line x1="170" y1="552" x2="170" y2="568" stroke="{INK}" stroke-width="3"/>' + T(115, 586, "5 carreaux = 25 mm", 14, 800, INK) + T(520, 586, "Échelle : 1 carreau = 5 mm", 15, 700, MUTED)
    o += f'<rect x="990" y="40" width="190" height="500" rx="14" fill="{PANEL}" stroke="#d9e0ec" stroke-width="2"/>' + T(1085, 74, "Légende", 17, 800, INK)
    leg = (("PCB", "zone carte ESP32", BLUE), ("DHT", "zone capteur", GREEN), ("BATT", "zone batterie", AMBER), ("USB", "ouverture câble USB", RED), ("LED", "ouverture LED", "#e5353b"), ("▼ ▲", "aérations bas / haut", MUTED))
    for k, (a, b, c) in enumerate(leg):
        y = 110 + k * 70
        o += f'<rect x="1006" y="{y-18}" width="60" height="36" rx="6" fill="{c}" opacity=".9"/>' + T(1036, y + 6, a, 14, 800, "#fff") + T(1076, y + 5, b, 13, 700, INK, "start") if False else f'<rect x="1004" y="{y-16}" width="58" height="34" rx="6" fill="{c}"/>' + T(1033, y + 6, a, 14, 800, "#fff") + T(1070, y - 2, b.split(" ")[0], 12, 700, INK, "start") + T(1070, y + 14, " ".join(b.split(" ")[1:]), 12, 700, INK, "start")
    return figure(W, 610, o)




def f_fiche_maintenance():
    o = f'<rect x="40" y="26" width="1120" height="860" rx="18" fill="#fff" stroke="#c7d0e2" stroke-width="3"/>'
    o += f'<rect x="40" y="26" width="1120" height="74" rx="18" fill="{BLUE}"/><rect x="40" y="70" width="1120" height="30" fill="{BLUE}"/>'
    o += T(70, 74, "FICHE DE MAINTENANCE CORRECTIVE", 26, 800, "#fff", "start") + T(1130, 74, "à remplir à CHAQUE intervention", 16, 600, "#dbe6ff", "end")
    meta = (("Équipement", "esp32-station-météo-01"), ("Date", "2026-03-15"), ("Intervenant", "Alice DUPONT"), ("Durée", "45 min"))
    for k, (a, b) in enumerate(meta):
        x = 70 + k * 270
        o += f'<rect x="{x}" y="116" width="250" height="58" rx="10" fill="#eef2fb"/>' + T(x + 14, 140, a, 13, 700, MUTED, "start") + T(x + 14, 163, b, 17, 800, INK, "start")
    def card(x, y, w, h, n, title, col):
        return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="{col}" opacity=".07"/>'
                f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="none" stroke="{col}" stroke-width="3"/>' + badge(x + 28, y + 30, n, col, 16) + T(x + 56, y + 37, title, 19, 800, col, "start"))
    # 1 symptôme
    o += card(70, 196, 520, 150, 1, "SYMPTÔME(S)", RED)
    o += T(90, 252, "L'ESP32 ne publie plus sur AWS IoT depuis 14 h 00.", 16, 600, INK, "start") + T(90, 278, "LED Wi-Fi allumée : la connexion Wi-Fi est correcte.", 16, 600, INK, "start")
    o += f'<rect x="90" y="298" width="480" height="34" rx="8" fill="#1b2742"/>' + T(104, 321, "Moniteur série :  « Erreur MQTT : 5 »  en boucle", 15, 700, "#fca5a5", "start", extra='font-family="monospace"')
    # 2 démarche
    o += card(70, 362, 520, 330, 2, "DÉMARCHE DE DIAGNOSTIC", BLUE)
    steps = (("Wi-Fi", "OK : LED + log « WiFi OK → 192.168.1.42 »", GREEN, "✓"), ("Broker", "ping OK : le broker est joignable", GREEN, "✓"), ("Certificat", "console AWS : certificat actif ? Oui", GREEN, "✓"), ("Journal AWS", "test MQTT → erreur :  « Policy doesn't allow iot:Publish on this resource »", RED, "✗"))
    o += f'<line x1="106" y1="430" x2="106" y2="640" stroke="#9fb4e8" stroke-width="3" stroke-dasharray="5 5"/>'
    for k, (t, d, c, ic) in enumerate(steps):
        y = 426 + k * 66
        o += f'<circle cx="106" cy="{y+4}" r="15" fill="{c}"/>' + T(106, y + 10, ic, 18, 800, "#fff") + T(136, y - 2, f"Étape {k+1} · {t}", 15, 800, INK, "start")
        if k < 3: o += T(136, y + 22, d, 14, 600, MUTED, "start")
        else: o += T(136, y + 22, "test MQTT → erreur :", 14, 600, MUTED, "start") + T(136, y + 42, "« Policy doesn't allow iot:Publish on this resource »", 13, 700, RED, "start", extra='font-family="monospace"')
    # 3 cause
    o += card(610, 196, 520, 150, 3, "CAUSE IDENTIFIÉE", AMBER)
    o += T(630, 252, "La Policy IoT AWS a été modifiée par erreur :", 16, 600, INK, "start") + T(630, 278, "l'action iot:Publish a été supprimée lors", 16, 600, INK, "start") + T(630, 304, "d'une mise à jour de sécurité.", 16, 600, INK, "start")
    # 4 action
    o += card(610, 362, 520, 110, 4, "ACTION CORRECTIVE", GREEN)
    o += T(630, 420, "Ajout de « iot:Publish » dans la Policy IoT", 16, 600, INK, "start") + T(630, 446, "via la console AWS.", 16, 600, INK, "start")
    # 5 validation
    o += card(610, 488, 520, 150, 5, "VALIDATION", GREEN)
    for k, tx in enumerate(("Messages visibles dans la console AWS (test MQTT)", "CloudWatch : nouvelles métriques de température", "Aucun incident depuis plus de 24 h")):
        y = 548 + k * 30
        o += f'<circle cx="636" cy="{y-5}" r="11" fill="{GREEN}"/>' + T(636, y + 1, "✓", 14, 800, "#fff") + T(658, y, tx, 15, 600, INK, "start")
    # 6 prévention
    o += card(610, 654, 520, 150, 6, "AMÉLIORATION PRÉVENTIVE", "#7c3aed")
    o += T(630, 710, "• Alarme CloudWatch si aucune métrique pendant plus de 15 min", 15, 600, INK, "start") + T(630, 738, "• Validation obligatoire avant toute modification de", 15, 600, INK, "start") + T(644, 762, "Policy IoT en production", 15, 600, INK, "start")
    o += chip(330, 740, "Une fiche bien remplie évite de rechercher deux fois la même panne", INK, w=520, size=14)
    return figure(W, 910, o)


def f_hysteresis():
    import math
    o = panel(30, 30, 560, 480, "SANS hystérésis : un seul seuil à 30 °C", accent=RED) + panel(610, 30, 560, 480, "AVEC hystérésis : haut 30 °C, bas 28 °C", accent=GREEN)
    def graph(x0, hyst):
        gx, gy, gw, gh = x0 + 70, 110, 460, 220
        ty = lambda v: gy + gh - (v - 27) / 5 * gh
        r = f'<rect x="{gx}" y="{gy}" width="{gw}" height="{gh}" fill="#fff" stroke="#c7d0e2" stroke-width="2"/>'
        r += f'<line x1="{gx}" y1="{ty(30):.0f}" x2="{gx+gw}" y2="{ty(30):.0f}" stroke="{RED}" stroke-width="2" stroke-dasharray="7 5"/>' + T(gx + 6, ty(30) - 6, "30 °C", 13, 800, RED, "start")
        if hyst: r += f'<line x1="{gx}" y1="{ty(28):.0f}" x2="{gx+gw}" y2="{ty(28):.0f}" stroke="{GREEN}" stroke-width="2" stroke-dasharray="7 5"/>' + T(gx + 6, ty(28) - 6, "28 °C", 13, 800, GREEN, "start")
        N = 150
        pts = [(i / N, 28.9 + 1.5 * math.sin(math.pi * (i / N)) ** 1.2 - 1.7 * (i / N) ** 4 + 0.32 * math.sin(i * 1.7)) for i in range(N + 1)]
        r += f'<polyline points="{" ".join(f"{gx+t*gw:.0f},{ty(v):.0f}" for t, v in pts)}" fill="none" stroke="{BLUE}" stroke-width="3"/>'
        r += T(gx - 8, gy + 14, "T (°C)", 12, 700, MUTED, "end") + T(gx + gw, gy + gh + 18, "temps →", 12, 700, MUTED, "end")
        st = []; cur = False
        for t, v in pts:
            if not cur and v >= 30: cur = True
            elif cur and v < (28 if hyst else 30): cur = False
            st.append(cur)
        by = gy + gh + 34
        r += T(gx - 8, by + 17, "alerte", 13, 800, INK, "end")
        i = 0
        while i < len(st):
            j = i
            while j + 1 < len(st) and st[j + 1] == st[i]: j += 1
            xa = gx + pts[i][0] * gw; xb = gx + pts[min(j + 1, N)][0] * gw
            r += f'<rect x="{xa:.0f}" y="{by}" width="{max(xb-xa,2):.0f}" height="26" fill="{RED if st[i] else "#d8e3d8"}"/>'
            i = j + 1
        trans = sum(1 for k in range(1, len(st)) if st[k] != st[k - 1])
        r += T(gx + gw / 2, by + 62, f"{trans} changement{'s' if trans>1 else ''} d'état de l'alerte", 17, 800, GREEN if hyst else RED)
        return r
    o += graph(30, False) + graph(610, True)
    o += chip(600, 560, "Hystérésis : on déclenche à un seuil haut, on ne désactive qu'à un seuil plus bas", INK, w=1000, size=17)
    return figure(W, 610, o)


def f_thermostat_analogie():
    o = panel(30, 30, 370, 400, "1 · Chauffage à seuil unique", accent=RED) + panel(415, 30, 370, 400, "2 · Thermostat à hystérésis", accent=GREEN) + panel(800, 30, 370, 400, "3 · Ce qu'on retient", accent=BLUE)
    def therm(cx, v):
        return (f'<rect x="{cx-14}" y="100" width="28" height="190" rx="14" fill="#fff" stroke="{INK}" stroke-width="3"/><circle cx="{cx}" cy="300" r="26" fill="{RED}" stroke="{INK}" stroke-width="3"/><rect x="{cx-7}" y="{290-v}" width="14" height="{v+10}" fill="{RED}"/>')
    o += therm(85, 110) + T(130, 150, "Chauffage ALLUMÉ", 15, 800, INK, "start") + T(130, 172, "si T < 19 °C", 15, 800, INK, "start") + T(130, 206, "ÉTEINT dès que", 15, 800, INK, "start") + T(130, 228, "T ≥ 19 °C", 15, 800, INK, "start")
    o += T(215, 360, "Il s'allume et s'éteint sans cesse", 15, 800, RED) + T(215, 384, "autour de 19 °C", 15, 700, MUTED)
    o += therm(470, 110) + T(515, 150, "ALLUMÉ si T < 18 °C", 15, 800, GREEN, "start") + T(515, 180, "ÉTEINT si T > 20 °C", 15, 800, GREEN, "start") + T(515, 222, "Entre 18 et 20 °C :", 14, 700, INK, "start") + T(515, 244, "il garde son état", 14, 700, INK, "start")
    o += T(600, 360, "Peu de cycles, fonctionnement stable", 15, 800, GREEN)
    o += T(985, 110, "Hystérésis", 24, 800, BLUE) + T(985, 150, "le système « se souvient »", 16, 700, INK) + T(985, 174, "de son état précédent", 16, 700, INK)
    o += T(985, 230, "Entre les deux seuils,", 15, 600, MUTED) + T(985, 252, "on ne change PAS d'état", 15, 800, INK) + T(985, 306, "Alerte : seuil HAUT pour déclencher,", 15, 600, MUTED) + T(985, 328, "seuil BAS pour désactiver", 15, 800, INK)
    return figure(W, 480, o)


def f_reperage_fils():
    o = T(600, 52, "Repérage d'un fil : une étiquette identique aux deux extrémités", 22, 800, INK)
    # format
    for k, (t, sub, c, x) in enumerate((("SOURCE", "d'où part le fil", BLUE, 90), ("DESTINATION", "où il arrive", GREEN, 450), ("NUMÉRO / SIGNAL", "le distingue des autres", AMBER, 810))):
        o += f'<rect x="{x}" y="90" width="300" height="86" rx="14" fill="#fff" stroke="{c}" stroke-width="4"/><rect x="{x}" y="90" width="300" height="12" rx="6" fill="{c}"/>' + T(x + 150, 138, t, 20, 800, c) + T(x + 150, 162, sub, 14, 600, MUTED)
        if k < 2: o += T(x + 330, 144, "–", 40, 800, INK)
    o += chip(600, 214, "Format : [Source] – [Destination] – [Numéro ou signal]", INK, w=640, size=17)
    # schéma : deux modules reliés par un fil étiqueté
    o += f'<rect x="60" y="270" width="250" height="150" rx="14" fill="#fff" stroke="{RED}" stroke-width="4"/><rect x="60" y="270" width="250" height="38" rx="14" fill="{RED}"/>' + T(185, 296, "ESP32", 19, 800, "#fff") + T(150, 350, "3V3", 17, 800, INK, "start") + T(150, 392, "GND", 17, 800, INK, "start")
    o += f'<rect x="890" y="270" width="250" height="150" rx="14" fill="#fff" stroke="{BLUE}" stroke-width="4"/><rect x="890" y="270" width="250" height="38" rx="14" fill="{BLUE}"/>' + T(1015, 296, "DHT22", 19, 800, "#fff") + T(950, 350, "VCC", 17, 800, INK, "end") + T(950, 392, "GND", 17, 800, INK, "end")
    o += f'<path d="M310,346 H890" stroke="{RED}" stroke-width="8" stroke-linecap="round"/><path d="M310,388 H890" stroke="#222" stroke-width="8" stroke-linecap="round"/>'
    for x in (400, 800):
        o += f'<rect x="{x-65}" y="326" width="130" height="30" rx="6" fill="#fff8d6" stroke="#b59a2c" stroke-width="2"/>' + T(x, 347, "ESP32-DHT22-VCC", 12, 800, INK)
        o += f'<rect x="{x-65}" y="368" width="130" height="30" rx="6" fill="#fff8d6" stroke="#b59a2c" stroke-width="2"/>' + T(x, 389, "ESP32-DHT22-GND", 12, 800, INK)
    o += T(600, 332, "fil ROUGE · 20 cm", 15, 800, RED) + T(600, 416, "fil NOIR · 20 cm", 15, 800, "#222")
    o += arrow(400, 448, 400, 408, MUTED, 2) + T(400, 468, "même étiquette à chaque bout", 14, 700, MUTED) + arrow(800, 448, 800, 408, MUTED, 2) + T(800, 468, "même étiquette à chaque bout", 14, 700, MUTED)
    # exemples
    o += f'<rect x="60" y="500" width="1080" height="190" rx="14" fill="{PANEL}" stroke="#d9e0ec" stroke-width="2"/>' + T(90, 534, "Exemples d'étiquettes", 17, 800, INK, "start")
    ex = (("ESP32-DHT22-VCC", "alimentation 3,3 V de l'ESP32 vers le DHT22"), ("ESP32-DHT22-DATA", "données du DHT22 vers la pin 4 de l'ESP32"), ("BATT-REG-01", "fil n° 01 de la batterie vers le régulateur"), ("REG-ESP32-3V3", "sortie 3,3 V du régulateur vers l'ESP32"))
    for k, (a, b) in enumerate(ex):
        y = 556 + k * 32
        o += f'<rect x="90" y="{y}" width="230" height="26" rx="6" fill="#fff8d6" stroke="#b59a2c" stroke-width="2"/>' + T(205, y + 18, a, 14, 800, INK) + T(340, y + 19, "→  " + b, 15, 600, INK, "start")
    return figure(W, 730, o)


def f_pv_mesure():
    o = f'<rect x="40" y="24" width="1120" height="1000" rx="16" fill="#fff" stroke="#c7d0e2" stroke-width="3"/>'
    o += f'<rect x="40" y="24" width="1120" height="80" rx="16" fill="{INK}"/><rect x="40" y="70" width="1120" height="34" fill="{INK}"/>'
    o += T(70, 76, "PROCÈS-VERBAL DE MESURE", 28, 800, "#fff", "start") + T(1130, 70, "Réf. PV-2026-ESP32-001", 17, 700, "#cbd5ff", "end")
    def sec(x, y, w, h, n, title, col, lines, mono=False):
        r = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{col}" opacity=".06"/><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="none" stroke="{col}" stroke-width="2.5"/>'
        r += badge(x + 26, y + 28, n, col, 15) + T(x + 52, y + 34, title, 16, 800, col, "start")
        for k, (a, b) in enumerate(lines):
            yy = y + 66 + k * 25
            if b is None: r += T(x + 18, yy, a, 15, 600, INK, "start")
            else: r += T(x + 18, yy, a, 14, 700, MUTED, "start") + T(x + 170, yy, b, 14, 700, INK, "start")
        return r
    L, R, w = 70, 620, 520
    o += sec(L, 124, w, 168, 1, "EN-TÊTE ET IDENTIFICATION", BLUE, [("Référence PV", "PV-2026-ESP32-001"), ("Date", "2026-03-20"), ("Lieu", "Labo électronique – CFA [Ville]"), ("Donneur d'ordre", "INDUSTECH SAS – M. DUBOIS")])
    o += sec(R, 124, w, 168, 2, "OBJET DE LA MESURE", GREEN, [("Vérification des résistances de pull-up I2C", None), ("sur carte ESP32", None)])
    o += sec(L, 312, w, 168, 3, "ÉQUIPEMENT SOUS TEST (EUT)", AMBER, [("Désignation", "Carte ESP32 IoT AGROSMART"), ("Référence", "ASM-001-REV2"), ("N° de série", "SN20260320-03")])
    o += sec(R, 312, w, 168, 5, "CONDITIONS DE MESURE", "#7c3aed", [("Température", "22 °C ± 2 °C"), ("Hygrométrie", "45 % HR ± 10 %"), ("Réseau électrique", "mesure hors tension (Ω)")])
    o += sec(L, 500, 1070, 168, 4, "INSTRUMENTS UTILISÉS", RED, [("Appareil", "Multimètre numérique Fluke 87V"), ("N° de série", "7435280"), ("Calibration", "2026-01-15 · Certificat n° LAB-2026-0047"), ("Classe · validité", "0,5  ·  valable jusqu'au 2027-01-14")])
    o += f'<rect x="760" y="548" width="360" height="92" rx="10" fill="#fff" stroke="{RED}" stroke-width="2" stroke-dasharray="6 5"/>' + T(940, 584, "L'étalonnage doit être", 15, 700, RED) + T(940, 606, "VALIDE le jour de la mesure", 15, 800, RED)
    o += sec(L, 688, 340, 120, 6, "RÉSULTATS DE MESURE", BLUE, [("voir le tableau de la", None), ("section suivante", None)])
    o += sec(420, 688, 340, 120, 7, "INCERTITUDES", GREEN, [("voir le calcul de la", None), ("section suivante", None)])
    o += sec(770, 688, 370, 120, 8, "CONCLUSION / CONFORMITÉ", AMBER, [("☐ Conforme   ☐ Non conforme", None), ("☐ Sous réserve", None)])
    o += sec(L, 828, 520, 120, 9, "REMARQUES ET OBSERVATIONS", "#7c3aed", [("", None)])
    o += sec(R, 828, 520, 120, 10, "SIGNATURES", RED, [("", None)])
    o += T(640, 900, "Mesureur :", 14, 700, MUTED, "start") + f'<line x1="730" y1="902" x2="1110" y2="902" stroke="#9aa4b8" stroke-width="2"/>' + T(640, 930, "Resp. qualité :", 14, 700, MUTED, "start") + f'<line x1="760" y1="932" x2="1110" y2="932" stroke="#9aa4b8" stroke-width="2"/>'
    o += chip(600, 990, "10 rubriques, toujours dans le même ordre : n'importe qui retrouve l'information en quelques secondes", INK, w=1060, size=15)
    return figure(W, 1050, o)


FIGS = {"saleae_logic2": f_saleae, "mqtt_sequence": f_mqtt_seq, "nodered_interface": f_nodered_ui, "climasens_architecture": f_climasens_archi, "climasens_cablage": f_climasens_cablage, "cem_pcb_defaillant": f_cem_pcb_defaillant, "grille_boitier": f_grille_boitier, "fiche_maintenance": f_fiche_maintenance, "hysteresis_courbes": f_hysteresis, "reperage_fils": f_reperage_fils, "pv_mesure": f_pv_mesure, "hysteresis_thermostat": f_thermostat_analogie}
