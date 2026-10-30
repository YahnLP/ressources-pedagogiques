"""Figures des cours de Première (E2)."""
from lib import *
from figs07 import block
from figs_sec import mtext

W = 1200


def chain(items, y=120, h=130, w=None, gap=50, x0=40, col=BLUE, labels=None):
    n = len(items); w = w or (W - 2 * x0 - (n - 1) * gap) / n
    o = ""
    for i, it in enumerate(items):
        t, s = (it, None) if isinstance(it, str) else it
        c = col[i] if isinstance(col, list) else col
        x = x0 + i * (w + gap); o += block(x, y, w, h, t, s, c)
        if i < n - 1: o += arrow(x + w + 4, y + h / 2, x + w + gap - 4, y + h / 2, INK, 4)
        if labels and labels[i]: o += T(x + w / 2, y + h + 34, labels[i], 15, 700, MUTED)
    return o


def f_bathtub():
    o = panel(30, 30, 1140, 460, "Courbe en baignoire : λ en fonction du temps", accent=BLUE)
    ax, ay, aw, ah = 130, 120, 960, 300
    o += f'<line x1="{ax}" y1="{ay+ah}" x2="{ax+aw}" y2="{ay+ah}" stroke="{INK}" stroke-width="3" marker-end="url(#arr)"/><line x1="{ax}" y1="{ay+ah}" x2="{ax}" y2="{ay-10}" stroke="{INK}" stroke-width="3" marker-end="url(#arr)"/>'
    o += T(ax + aw, ay + ah + 30, "temps", 16, 700, INK, "end") + T(ax + 6, ay - 16, "taux de panne λ", 16, 700, INK, "start")
    pts = []
    for i in range(0, 101):
        t = i / 100; x = ax + 20 + t * (aw - 40)
        y = ay + ah - 40 - (200 * math.exp(-t * 14) + 12 + 220 * max(0, (t - 0.72) / 0.28) ** 2.2)
        pts.append((x, max(y, ay + 10)))
    o += "<polyline points='" + " ".join(f"{x:.0f},{y:.0f}" for x, y in pts) + f"' fill='none' stroke='{BLUE}' stroke-width='6' stroke-linecap='round'/>"
    for (a, b, c, t, d) in ((ax + 20, ax + 20 + 0.2 * (aw - 40), RED, "1 · Mortalité infantile", "λ décroissant : défauts de fabrication"), (ax + 20 + 0.2 * (aw - 40), ax + 20 + 0.72 * (aw - 40), GREEN, "2 · Vie utile", "λ constant : pannes aléatoires (MTBF valable)"), (ax + 20 + 0.72 * (aw - 40), ax + aw - 20, AMBER, "3 · Vieillissement", "λ croissant : usure")):
        o += f'<rect x="{a}" y="{ay}" width="{b-a}" height="{ah}" fill="{c}" opacity=".10"/>' + T((a + b) / 2, ay + 30, t, 18, 800, c) + T((a + b) / 2, ay + 56, d, 13, 600, INK)
    return figure(W, 520, o)


def rbd(par, ser, parlab=None, cy=130):
    """par : liste de blocs en parallèle (peut être vide) ; ser : blocs en série ensuite."""
    o = ""; x = 40
    if par:
        n = len(par); hh = 66; gap = 22; total = n * hh + (n - 1) * gap; y0 = cy - total / 2
        o += s_wire([(x, cy), (x + 40, cy)])
        xb = x + 40
        for i, (t, s) in enumerate(par):
            yy = y0 + i * (hh + gap)
            o += block(xb + 40, yy, 230, hh, t, s, GREEN) + s_wire([(xb, yy + hh / 2), (xb + 40, yy + hh / 2)]) + s_wire([(xb + 270, yy + hh / 2), (xb + 310, yy + hh / 2)])
        o += s_wire([(xb, y0 + hh / 2), (xb, y0 + total - hh / 2)]) + s_wire([(xb + 310, y0 + hh / 2), (xb + 310, y0 + total - hh / 2)])
        x = xb + 310; o += s_wire([(x, cy), (x + 40, cy)]); x += 40
    else:
        o += s_wire([(x, cy), (x + 30, cy)]); x += 30
    for t, s in ser:
        o += block(x, cy - 40, 170, 80, t, s, BLUE) + s_wire([(x + 170, cy), (x + 205, cy)]); x += 205
    return o, x


def mk_rbd(par, ser, H=270, label=None):
    def f():
        o, x = rbd(par, ser)
        if label: o += T(W / 2, H - 28, label, 17, 700, MUTED)
        return figure(max(W, int(x + 40)), H, o)
    return f


f_rbd_serie = lambda: figure(W, 220, rbd(None, [("C1", None), ("C2", None), ("C3", None), ("…", None), ("Cn", None)])[0].replace("</svg>", "") + T(W / 2, 195, "Si un seul composant tombe en panne, tout le système est en panne", 17, 700, MUTED))
f_rbd_parallele = lambda: figure(W, 330, rbd([("C1", None), ("C2", None), ("C3", None)], [], cy=150)[0] + T(W / 2, 305, "Il suffit qu'un seul composant fonctionne : le système est plus fiable que le meilleur d'entre eux", 17, 700, MUTED))
f_rbd_capteurs = mk_rbd([("Capteur 1", "R = 0,90"), ("Capteur 2", "R = 0,90")], [("CPU", "R = 0,95"), ("Réseau", "R = 0,98"), ("Serveur", "R = 0,99")])
f_rbd_station = mk_rbd([("DHT22", "R = 0,88"), ("MQ-2", "R = 0,85")], [("ESP32", "R = 0,92"), ("Wi-Fi / MQTT", "R = 0,97"), ("Node-RED", "R = 0,99")])
f_rbd_ab = mk_rbd([("A", "R = 0,85"), ("B", "R = 0,80")], [("CPU", "R = 0,95"), ("Réseau", "R = 0,98")])


def f_mqtt():
    o = block(470, 90, 260, 250, "BROKER", "Mosquitto, HiveMQ…", AMBER)
    for i, (t, s) in enumerate((("Capteur de température", "publisher"), ("Capteur de CO₂", "publisher"))):
        y = 110 + i * 120; o += block(40, y, 270, 90, t, s, BLUE) + arrow(314, y + 45, 466, y + 45, INK, 4)
    for i, (t, s) in enumerate((("Dashboard", "subscriber"), ("Alarme SMS", "subscriber"))):
        y = 110 + i * 120; o += block(890, y, 270, 90, t, s, GREEN) + arrow(734, y + 45, 886, y + 45, INK, 4)
    o += T(600, 390, "Point central unique : les publishers et les subscribers ne se connaissent pas", 18, 700, INK)
    return figure(W, 430, o)


def f_mtls():
    o = ""
    for k, (title, col, msgs) in enumerate((("TLS standard (HTTPS)", BLUE, [("→", "Montre-moi ton certificat"), ("←", "Voilà mon certificat (signé par une CA)"), ("→", "OK, je te fais confiance")]),
                                            ("mTLS (AWS IoT)", GREEN, [("→", "Montre-moi ton certificat"), ("←", "Voilà le mien. Et toi, montre le tien"), ("→", "Voilà mon certificat d'appareil")]))):
        px = 30 + k * 590
        o += panel(px, 30, 560, 400, title, accent=col)
        o += block(px + 20, 90, 130, 50, "Client", None, col) + block(px + 410, 90, 130, 50, "Serveur", None, col)
        o += f'<line x1="{px+85}" y1="140" x2="{px+85}" y2="400" stroke="{MUTED}" stroke-width="3" stroke-dasharray="6 5"/><line x1="{px+475}" y1="140" x2="{px+475}" y2="400" stroke="{MUTED}" stroke-width="3" stroke-dasharray="6 5"/>'
        for i, (d, m) in enumerate(msgs):
            y = 190 + i * 70
            o += (arrow(px + 90, y, px + 470, y, INK, 4) if d == "→" else arrow(px + 470, y, px + 90, y, INK, 4)) + T(px + 280, y - 12, m, 14, 700, INK)
        o += T(px + 280, 418, "Seul le SERVEUR s'authentifie" if k == 0 else "Les DEUX s'authentifient mutuellement", 16, 800, col)
    return figure(W, 460, o)


def f_aws():
    o = chain([("ESP32", "publie"), ("Broker AWS IoT", None), ("Rule Engine", "analyse topic / payload")], y=130, h=100, w=230, gap=60, col=[BLUE, AMBER, GREEN])
    o += s_wire([(40 + 2 * 290 + 115, 230), (40 + 2 * 290 + 115, 290)], INK, 4) + s_wire([(485, 290), (815, 290)], INK, 4)
    for i, (a, b, x) in enumerate((("CloudWatch", "graphes", 485), ("DynamoDB", "historique", 815))):
        o += s_wire([(x, 290), (x, 320)], INK, 4) + block(x - 105, 320, 210, 80, a, b, BLUE) + arrow(x, 400, x, 430, INK, 4)
        c, d = (("Lambda", "traitement"), ("S3", "archivage"))[i]
        o += block(x - 105, 430, 210, 80, c, d, AMBER)
    return figure(W, 540, o)


def f_chemin():
    items = [("Capteur", "mesure"), ("Code Arduino", "log série"), ("Wi-Fi", "ping"), ("Réseau", "traceroute"), ("Broker", "console"), ("Subscriber", "logs broker")]
    o = chain(items, y=70, h=110, w=150, gap=44, col=BLUE)
    o += panel(60, 240, 1080, 150, fill="#fff")
    o += T(600, 280, "Dichotomie : tester au milieu de la chaîne", 19, 800, INK) + T(600, 320, "« Le broker reçoit-il quelque chose ? »", 18, 700, MUTED)
    o += chip(330, 365, "OUI → problème en aval (subscriber, topic, format)", GREEN, w=520, size=15) + chip(880, 365, "NON → problème en amont (code, Wi-Fi, réseau, broker)", RED, w=540, size=15)
    return figure(W, 420, o)


def f_chaine_aws():
    o = chain([("Capteur(s)", "vibration, courant, niveau…"), ("ESP32", None), ("AWS IoT Core", "règle IoT SQL"), ("CloudWatch", "dashboard + alarmes")], y=70, h=120, w=230, gap=70, col=[BLUE, AMBER, GREEN, GREEN])
    o += T(40 + 230 + 35 + 230 + 35 - 18 + 36, 60, "Wi-Fi", 16, 800, INK) if False else T(605, 112, "Wi-Fi", 15, 800, INK)
    x = 40 + 2 * 300 + 115
    o += s_wire([(x, 190), (x, 250)], INK, 4) + arrow(x, 250, x, 270, INK, 4) + block(x - 115, 270, 230, 100, "Notification SMS", "si seuil dépassé", RED)
    return figure(W, 400, o)


def f_cem():
    o = chain([("SOURCE", "perturbateur"), ("COUPLAGE", "conduit · rayonné"), ("VICTIME", "circuit perturbé")], y=60, h=130, w=300, gap=80, col=[RED, AMBER, BLUE])
    o += chip(600, 245, "Agir sur le COUPLAGE : la solution la plus simple", GREEN, w=640, size=18) + T(600, 300, "CEM = ne pas perturber + ne pas être perturbé (marquage CE, directive 2014/30/UE)", 16, 600, MUTED)
    return figure(W, 330, o)


def f_filtre_cem():
    o = s_wire([(160, 150), (240, 150)]) + node(160, 150) + T(160, 120, "Signal", 18, 800, INK) + sym("R", 280, 150) + s_wire([(320, 150), (560, 150)]) + dot(440, 150) + node(560, 150) + T(560, 120, "Sortie filtrée", 18, 800, INK)
    o += T(280, 118, "R", 20, 800, INK) + s_wire([(440, 150), (440, 180)]) + sym("C", 440, 220, 90) + s_wire([(440, 260), (440, 280)]) + gnd(440, 280) + T(480, 228, "C", 20, 800, INK, "start")
    o += chip(600, 350, "Exemple : R = 10 kΩ ; C = 330 nF", INK, w=420, size=17)
    return figure(W, 400, o)


def f_analyseur():
    o = block(60, 60, 280, 380, "", None, BLUE) + T(200, 100, "Analyseur logique USB", 18, 800, INK)
    chs = [("CH0", "Signal 1 (ex. SCL)"), ("CH1", "Signal 2 (ex. SDA)"), ("CH2", "Signal 3 (ex. SCLK SPI)"), ("…", ""), ("GND", "Masse du circuit")]
    for i, (c, s) in enumerate(chs):
        y = 130 + i * 62; col = RED if c == "GND" else INK
        o += T(330, y + 6, c, 18, 800, col, "end") + s_wire([(340, y), (640, y)], RED if c == "GND" else "#2f5bea", 4) + T(660, y + 6, s, 18, 700, col, "start")
    o += block(640, 60, 1, 1, "", None, BLUE) if False else ""
    o += chip(600, 480, "⚠ GND toujours connecté en premier", RED, w=520, size=18)
    return figure(W, 520, o)


def wave(x, y, bits, bw, hi=40, col=INK, w=4):
    d = f"M{x},{y+(0 if bits[0] else hi)}"; cur = bits[0]
    for i, b in enumerate(bits):
        if b != cur: d += f" L{x+i*bw},{y+(0 if b else hi)}"; cur = b
        d += f" L{x+(i+1)*bw},{y+(0 if b else hi)}"
    return f'<path d="{d}" fill="none" stroke="{col}" stroke-width="{w}" stroke-linejoin="round"/>'


def clock(x, y, n, bw, hi=40, col=BLUE):
    d = f"M{x},{y+hi}"
    for i in range(n): d += f" L{x+i*bw},{y+hi} L{x+i*bw},{y} L{x+i*bw+bw/2},{y} L{x+i*bw+bw/2},{y+hi}"
    return f'<path d="{d} L{x+n*bw},{y+hi}" fill="none" stroke="{col}" stroke-width="4" stroke-linejoin="round"/>'


def f_i2c():
    o = ""; x0, bw = 150, 70
    o += T(60, 100, "SCL", 20, 800, BLUE, "end") + T(60, 210, "SDA", 20, 800, AMBER, "end")
    o += clock(x0 + bw, 70, 9, bw) + f'<path d="M{x0},110 L{x0+bw},110" stroke="{BLUE}" stroke-width="4"/>'
    bits = [1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1]
    sda = [1, 0] + [1, 0, 1, 1, 0, 1, 0] + [0, 0]
    labs = ["A6", "A5", "A4", "A3", "A2", "A1", "A0", "R/W", "ACK"]
    o += wave(x0, 180, [1, 0, 1, 0, 1, 0, 1, 1, 0, 0], bw, 40, AMBER)
    for i, l in enumerate(labs): o += T(x0 + bw * (i + 1) + bw / 2, 255, l, 16, 800, INK)
    o += T(x0 + bw / 2, 255, "START", 15, 800, RED) + f'<line x1="{x0+bw*9}" y1="60" x2="{x0+bw*9}" y2="260" stroke="{GREEN}" stroke-width="2.5" stroke-dasharray="6 5"/>'
    o += arrow(x0 + bw, 285, x0 + bw * 9, 285, INK, 3) + T(x0 + bw * 5, 310, "8 bits : adresse sur 7 bits + R/W", 15, 700, INK)
    o += T(600, 350, "9ᵉ coup d'horloge : SDA = 0 (ACK) ou SDA = 1 (NACK)", 17, 800, GREEN)
    return figure(W, 390, o)


def f_spi():
    o = ""; x0, bw = 170, 90
    for i, (l, c) in enumerate((("CS", RED), ("SCLK", BLUE), ("MOSI", AMBER), ("MISO", GREEN))):
        y = 60 + i * 95; o += T(130, y + 28, l, 20, 800, c, "end")
    o += wave(x0, 60, [1, 0, 0, 0, 0, 0, 0, 0, 0, 1], bw, 40, RED)
    o += clock(x0 + bw, 155, 8, bw) + wave(x0 + bw, 250, [1, 0, 1, 1, 0, 0, 1, 0], bw, 40, AMBER) + wave(x0 + bw, 345, [0, 1, 1, 0, 1, 0, 0, 1], bw, 40, GREEN)
    for i in range(8): o += T(x0 + bw * (i + 1) + bw / 2, 140, str(i + 1), 14, 800, INK)
    o += T(x0 + bw, 45, "CS bas = début", 14, 800, RED, "start") + T(x0 + 9 * bw, 45, "CS haut = fin", 14, 800, RED, "end") + T(600, 415, "8 coups d'horloge = 8 bits échangés (MOSI et MISO en même temps)", 17, 700, INK)
    return figure(W, 450, o)


def f_oscillo_logique():
    o = ""; x0, bw = 170, 60
    o += T(130, 96, "CH1", 18, 800, INK, "end") + T(130, 112, "analogique", 12, 600, MUTED, "end") + f'<path d="{sine_path(x0, 90, 780, 28, 4)}" fill="none" stroke="{GREEN}" stroke-width="4"/>'
    o += T(130, 230, "D0 (SCL)", 18, 800, BLUE, "end") + clock(x0, 210, 12, bw) + T(130, 330, "D1 (SDA)", 18, 800, AMBER, "end") + wave(x0, 310, [1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1], bw, 40, AMBER)
    o += chip(600, 410, "Forme exacte du signal  +  chronogramme logique  +  trame décodée", INK, w=860, size=17)
    return figure(W, 450, o)


def f_isa():
    lv = [("5", "Décision", "Direction : KPI, tendances, rapports", RED), ("4", "Analyse", "Ingénieurs : dashboards, alertes", AMBER), ("3", "SCADA / MES", "Superviseurs : Node-RED, InfluxDB, Grafana", GREEN), ("2", "Contrôle", "Automaticiens : PLC, régulateurs", BLUE), ("1", "Terrain", "Capteurs, actionneurs, ESP32", "#6c63ff")]
    o = ""
    for i, (n, t, d, c) in enumerate(lv):
        y = 40 + i * 84; w = 320 + (4 - i) * 0 + i * 70
        o += f'<rect x="{80}" y="{y}" width="{w}" height="72" rx="10" fill="{c}"/>' + T(110, y + 45, n, 30, 800, "#fff", "start") + T(80 + w / 2 + 20, y + 45, t, 24, 800, "#fff") + T(80 + w + 24, y + 44, d, 17, 700, INK, "start")
    o += chip(600, 480, "Stack CLIMASENS : niveaux 1 (ESP32 + capteurs), 3 (Node-RED + InfluxDB) et 4 (dashboard)", GREEN, w=900, size=16)
    return figure(W, 520, o)


def f_influx():
    o = block(60, 50, 520, 70, "MEASUREMENT (≈ table)", "temperature_salle", BLUE)
    for i, (t, ls, c) in enumerate((("TAGS (étiquettes indexées)", ["location = \"salle_e2\"", "capteur = \"esp32_01\""], AMBER), ("FIELDS (valeurs)", ["temp = 23,5", "humidite = 65,2"], GREEN), ("TIMESTAMP (automatique)", ["2024-05-10T14:35:22Z"], MUTED))):
        x = 60 + i * 380; o += s_wire([(320, 120), (320, 150), (x + 160, 150), (x + 160, 170)], INK, 3) + f'<rect x="{x}" y="170" width="340" height="170" rx="12" fill="#fff" stroke="{c}" stroke-width="4"/>' + T(x + 170, 205, t, 17, 800, c)
        for k, l in enumerate(ls): o += T(x + 170, 255 + k * 36, l, 18, 700, INK, extra='font-family="monospace"')
    o += T(600, 390, "Un POINT = 1 ligne dans InfluxDB = {tags} + {fields} + timestamp", 19, 800, INK)
    return figure(W, 430, o)


def f_stack():
    o = chain([("ESP32", "acquisition"), ("Broker MQTT", "transport"), ("Node-RED", "orchestration"), ("Dashboard web", None)], y=60, h=100, w=220, gap=64, col=[BLUE, AMBER, GREEN, GREEN])
    o += T(330, 55, "MQTT", 14, 800, INK) if False else ""
    xn = 40 + 2 * 284 + 110
    o += s_wire([(xn, 160), (xn, 230)], INK, 4) + arrow(xn, 230, xn, 246, INK, 4) + block(xn - 110, 246, 220, 100, "InfluxDB", "stockage long terme", AMBER) + arrow(xn + 114, 296, xn + 214, 296, INK, 4) + block(xn + 218, 246, 220, 100, "Grafana", "dashboard pro", GREEN)
    o += s_wire([(xn + 100, 160), (xn + 100, 190), (xn + 240, 190), (xn + 240, 206)], INK, 4) + block(xn + 140, 206, 200, 0.1, "", None, GREEN) if False else ""
    o += T(xn + 330, 190, "Email / alerte", 17, 800, RED)
    return figure(W, 380, o)


def f_flux_nodered():
    o = chain([("ESP32", None), ("MQTT", None), ("Node-RED", None)], y=40, h=90, w=200, gap=50, col=[BLUE, AMBER, GREEN])
    x = 40 + 2 * 250 + 100
    o += arrow(x + 104, 70, x + 254, 70, INK, 4) + block(x + 258, 40, 280, 90, "Dashboard", "temps réel", GREEN) + arrow(x + 40, 134, x + 40, 214, INK, 4) + block(x - 60, 220, 240, 90, "InfluxDB", "stockage", AMBER)
    o += arrow(x + 184, 265, x + 254, 265, INK, 4) + T(x + 219, 205, "requête Flux", 14, 800, INK) + block(x + 258, 220, 280, 90, "Chart historique", None, GREEN)
    return figure(W, 350, o)


FIGS = {"courbe_baignoire": f_bathtub, "rbd_serie": f_rbd_serie, "rbd_parallele": f_rbd_parallele, "rbd_capteurs": f_rbd_capteurs, "rbd_station": f_rbd_station, "rbd_exercice": f_rbd_ab,
        "mqtt_broker": f_mqtt, "tls_mtls": f_mtls, "aws_regles": f_aws, "chemin_message_mqtt": f_chemin, "chaine_aws": f_chaine_aws, "cem_couplage": f_cem, "filtre_rc_cem": f_filtre_cem,
        "analyseur_cablage": f_analyseur, "chrono_i2c": f_i2c, "chrono_spi": f_spi, "oscillo_logique": f_oscillo_logique, "niveaux_isa": f_isa, "influx_point": f_influx, "stack_iot": f_stack, "flux_nodered": f_flux_nodered}
