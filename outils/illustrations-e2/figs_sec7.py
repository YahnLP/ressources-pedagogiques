"""Seconde S07, S08, S13 : figures manquantes."""
from hl import *
from figs_sec6 import grid_
import math


def f_uno():
    o = '<g filter="url(#sh)"><rect x="40" y="60" width="640" height="420" rx="20" fill="#1c6c9a"/></g>'
    o += '<rect x="40" y="130" width="90" height="90" rx="4" fill="#cfd6df" stroke="#8a95a5" stroke-width="2"/><rect x="40" y="350" width="80" height="80" rx="6" fill="#25282e"/>'
    o += '<rect x="270" y="230" width="220" height="64" rx="4" fill="#25282e"/>' + T(380, 270, "ATmega328P", 20, 800, "#fff")
    o += '<rect x="230" y="68" width="400" height="26" fill="#25282e"/>' + ''.join(f'<rect x="{238+i*24}" y="72" width="14" height="18" fill="#6a7384"/>' for i in range(16))
    o += '<rect x="290" y="446" width="170" height="26" fill="#25282e"/>' + ''.join(f'<rect x="{298+i*20}" y="450" width="14" height="18" fill="#6a7384"/>' for i in range(8)) + '<rect x="480" y="446" width="170" height="26" fill="#25282e"/>' + ''.join(f'<rect x="{488+i*20}" y="450" width="14" height="18" fill="#6a7384"/>' for i in range(8))
    o += '<circle cx="190" cy="150" r="22" fill="#d63f3f" stroke="#fff" stroke-width="3"/>' + '<circle cx="570" cy="140" r="9" fill="#ffb300"/><circle cx="545" cy="140" r="9" fill="#ffb300"/><circle cx="520" cy="140" r="9" fill="#ffb300"/><circle cx="595" cy="140" r="9" fill="#2ecc71"/>'
    o += '<rect x="150" y="360" width="60" height="40" rx="4" fill="#cfd6df"/>' + T(350, 330, "UNO", 28, 800, "#ffffffaa") + '<rect x="300" y="150" width="60" height="26" rx="4" fill="#2a2d33"/>'
    items = [(75, 175, "Connecteur USB type B"), (80, 390, "Jack d'alimentation 5,5/2,1 mm"), (290, 262, "Microcontrôleur ATmega328P"), (520, 140, "LED « L » reliée à D13 (celle de Blink)"), (545, 140, "LED TX (orange)"), (570, 140, "LED RX (orange)"), (595, 140, "LED PWR (verte)"), (190, 150, "Bouton Reset"), (420, 80, "Broches numériques D0 à D13"), (380, 459, "Broches analogiques A0 à A5"), (560, 459, "Alimentation : 3,3 V, 5 V, GND, Vin"), (180, 380, "Régulateur de tension 5 V")]
    for n, (px, py, t) in enumerate(items, 1):
        y = 70 + (n - 1) * 36; o += badge(720, y, n, BLUE, 14) + T(745, y + 6, t, 15, 700, INK, "start") + f'<line x1="{px}" y1="{py}" x2="706" y2="{y}" stroke="{BLUE}" stroke-width="1.3" opacity=".35"/>' + badge(px, py, n, BLUE, 11)
    return figure(W, 540, o)


def f_ide():
    o = ui_win(30, 30, 1140, 580, "Blink | Arduino IDE 2.x")
    o += '<rect x="30" y="64" width="1140" height="48" fill="#00878f"/><circle cx="70" cy="88" r="16" fill="#fff"/>' + T(70, 94, "✓", 18, 800, "#00878f") + '<circle cx="118" cy="88" r="16" fill="#fff"/>' + T(118, 94, "→", 18, 800, "#00878f") + '<rect x="160" y="74" width="230" height="30" rx="6" fill="#fff"/>' + T(275, 95, "Arduino Uno ▾", 15, 700, INK) + '<rect x="410" y="74" width="130" height="30" rx="6" fill="#fff"/>' + T(475, 95, "COM3 ▾", 15, 700, INK)
    o += '<rect x="30" y="112" width="60" height="400" fill="#2c3e4a"/>' + ''.join(f'<rect x="46" y="{130+i*70}" width="28" height="28" rx="6" fill="#4a6272"/>' for i in range(4)) + '<rect x="90" y="112" width="1080" height="400" fill="#1e2a32"/>'
    code = [("void ", "#e67e22", "setup", "#f1c40f", "() {", "#cfd8dc"), ("  pinMode", "#f1c40f", "(13, OUTPUT);", "#cfd8dc", "", ""), ("}", "#cfd8dc", "", "", "", ""), ("void ", "#e67e22", "loop", "#f1c40f", "() {", "#cfd8dc"), ("  digitalWrite", "#f1c40f", "(13, HIGH);", "#cfd8dc", "", ""), ("  delay", "#f1c40f", "(1000);", "#cfd8dc", "", ""), ("  digitalWrite", "#f1c40f", "(13, LOW);", "#cfd8dc", "", ""), ("  delay", "#f1c40f", "(1000);", "#cfd8dc", "", ""), ("}", "#cfd8dc", "", "", "", "")]
    for i, ln in enumerate(code):
        y = 150 + i * 32; o += T(120, y, str(i + 1), 14, 600, "#6d8591", "end", extra='font-family="monospace"') + f'<text x="140" y="{y}" font-size="17" font-family="monospace" xml:space="preserve">' + ''.join(f'<tspan fill="{ln[k+1]}">{ln[k].replace(" ", chr(160))}</tspan>' for k in (0, 2, 4) if ln[k]) + '</text>'
    o += '<rect x="90" y="512" width="1080" height="98" fill="#0f1a20"/>' + T(110, 540, "Compilation terminée.", 15, 700, "#8bd5a0", "start", extra='font-family="monospace"') + T(110, 566, "Le croquis utilise 924 octets (2 %) de l'espace de stockage.", 14, 600, "#9fb0b8", "start", extra='font-family="monospace"')
    for n, (px, py, t, tx, ty) in enumerate([(70, 88, "Vérifier / Compiler", 60, 650), (118, 88, "Téléverser", 280, 650), (275, 88, "Carte", 430, 650), (475, 88, "Port", 530, 650), (60, 300, "Barre latérale", 650, 650), (600, 560, "Messages", 820, 650)], 1) if False else enumerate([]): pass
    for n, (bx, by) in enumerate([(70, 88), (118, 88), (275, 88), (475, 88), (60, 440), (1120, 560)], 1): o += badge(bx, by + (22 if n < 5 else 0), n, RED, 14)
    o += "".join(T(x, 640, f"{n} · {t}", 14, 700, INK, "start") for x, n, t in ((50, 1, "Vérifier / Compiler"), (230, 2, "Téléverser"), (370, 3, "Carte"), (470, 4, "Port COM"), (600, 5, "Sketchbook, bibliothèques, cartes"), (900, 6, "Messages de compilation")))
    return figure(W, 670, o)


def f_setup_loop():
    o = f'<ellipse cx="600" cy="70" rx="190" ry="40" fill="#fff" stroke="{INK}" stroke-width="3"/>' + T(600, 77, "Mise sous tension / Reset", 20, 800, INK)
    o += arrow(600, 112, 600, 168, INK, 4) + f'<rect x="380" y="170" width="440" height="80" rx="12" fill="#e6efff" stroke="{BLUE}" stroke-width="3"/>' + T(600, 205, "setup()", 24, 800, BLUE) + T(600, 234, "exécuté une seule fois", 16, 600, MUTED)
    o += arrow(600, 252, 600, 318, INK, 4) + f'<rect x="380" y="320" width="440" height="100" rx="12" fill="#e3f6ea" stroke="{GREEN}" stroke-width="3"/>' + T(600, 362, "loop()", 24, 800, GREEN) + T(600, 394, "exécuté en boucle, indéfiniment", 16, 600, MUTED)
    o += f'<path d="M820,370 H920 V300 H600 V320" fill="none" stroke="{GREEN}" stroke-width="4" marker-end="url(#arr)"/>' if False else f'<path d="M820,385 H940 V285 H600" fill="none" stroke="{GREEN}" stroke-width="4" stroke-linejoin="round"/>' + arrow(600, 285, 600, 316, GREEN, 4)
    o += chip(1020, 335, "↺ boucle infinie", GREEN, w=200, size=18)
    return figure(W, 470, o)


def f_schema_d13():
    o = f'<rect x="90" y="150" width="110" height="130" rx="8" fill="#e6efff" stroke="{BLUE}" stroke-width="3"/>' + T(145, 205, "Arduino", 17, 800, BLUE) + T(145, 230, "D13", 22, 800, INK) + T(145, 262, "GND", 18, 800, INK)
    o += s_wire([(200, 225), (260, 225)]) + hrun(225, 200, 760, [(330, "R", "R1 = 220 Ω", {}), (560, "LED", "D1 rouge · V_F = 2 V", {"below": True})]) + s_wire([(760, 225), (760, 330), (200, 330), (200, 260)]) if False else hrun(225, 200, 760, [(340, "R", "R1 = 220 Ω", {}), (570, "LED", "", {})])
    o += s_wire([(760, 225), (760, 360), (240, 360), (240, 262), (200, 262)]) + gnd(460, 360) + T(460, 420, "GND", 17, 800, INK)
    o += T(570, 290, "D1 rouge : V_F = 2 V", 16, 700, MUTED) + chip(600, 470, "I = (5 − 2) / 220 ≈ 14 mA : la broche D13 supporte 20 mA maximum", INK, w=840, size=16) + badge(160, 225, "+", RED, 12) if False else T(570, 290, "D1 rouge : V_F = 2 V", 16, 700, MUTED) + chip(600, 480, "I = (5 − 2) / 220 ≈ 14 mA : la broche D13 supporte 20 mA maximum", INK, w=840, size=16)
    return figure(W, 520, o)


def f_cablage_uno():
    o = '<g filter="url(#sh)"><rect x="40" y="90" width="300" height="360" rx="16" fill="#1c6c9a"/></g>' + T(190, 140, "Arduino UNO", 22, 800, "#fff") + '<rect x="60" y="200" width="30" height="130" fill="#25282e"/>' + ''.join(f'<rect x="76" y="{206+i*18}" width="10" height="12" fill="#c0c6cf"/>' for i in range(7))
    o += T(115, 230, "D13", 17, 800, "#fff", "start") + T(115, 340, "GND", 17, 800, "#fff", "start")
    bb = Breadboard(cols=14); P = bb.P; s = 1.4; xy = bb.xy
    inner = bb.draw()
    r1, r2 = xy(3, "c"), xy(8, "c")
    inner += f'<rect x="{r1[0]-2}" y="{r1[1]-6}" width="{r2[0]-r1[0]+4}" height="12" rx="4" fill="#e9d4a3" stroke="#a88"/><rect x="{r1[0]+20}" y="{r1[1]-6}" width="4" height="12" fill="#d32f2f"/><rect x="{r1[0]+30}" y="{r1[1]-6}" width="4" height="12" fill="#d32f2f"/><rect x="{r1[0]+40}" y="{r1[1]-6}" width="4" height="12" fill="#7a4320"/>'
    a, k = xy(8, "a"), xy(11, "a")
    inner += f'<path d="M{a[0]},{a[1]} V{a[1]-14} M{k[0]},{k[1]} V{k[1]-10}" stroke="#bbb" stroke-width="3"/><circle cx="{(a[0]+k[0])/2}" cy="{a[1]-20}" r="13" fill="#e5353b" stroke="#a11"/>'
    o += g(520, 60, inner, s)
    def wp(p, q, col): return f'<path d="M{p[0]},{p[1]} C{p[0]+120},{p[1]} {q[0]-120},{q[1]} {q[0]},{q[1]}" stroke="{col}" stroke-width="6" fill="none" stroke-linecap="round"/>'
    P0 = lambda p: (520 + p[0] * s, 60 + p[1] * s)
    o += wp((90, 212), P0(xy(3, "a")), RED) + wp((90, 322), P0(xy(11, "b")), "#222")
    o += callout(*P0(xy(5, "c")), 560, 560, "R = 220 Ω", "start", 17, bold=True) if False else ""
    o += chip(200, 600, "fil rouge : signal D13", RED, w=280, size=15) + chip(480, 600, "fil noir : GND", "#222", w=200, size=15) + T(720, 595, "R = 220 Ω", 18, 800, INK, "start") + T(720, 622, "LED : patte longue = anode (+), courte = cathode (−)", 15, 700, INK, "start")
    return figure(W, 650, o)


def f_serial_monitor():
    o = ui_win(120, 30, 960, 520, "Moniteur série")
    o += f'<rect x="150" y="76" width="900" height="44" rx="6" fill="#fff" stroke="#c5ccd8"/>' + T(165, 105, "Message (Entrée pour envoyer vers l'Arduino)", 15, 500, "#8a95a5", "start") + f'<rect x="920" y="82" width="110" height="32" rx="6" fill="#00878f"/>' + T(975, 104, "Envoyer", 15, 800, "#fff")
    o += f'<rect x="150" y="136" width="900" height="300" rx="6" fill="#0f1a20"/>' + "".join(T(170, 172 + i * 36, t, 18, 600, "#cfe9d4", "start", extra='font-family="monospace"') for i, t in enumerate(("LED : ALLUMEE", "LED : ETEINTE", "Cycle 1 terminé", "LED : ALLUMEE", "LED : ETEINTE", "Cycle 2 terminé")))
    o += f'<rect x="150" y="452" width="900" height="64" rx="6" fill="#eef2f7"/>' + f'<rect x="700" y="466" width="200" height="36" rx="6" fill="#fff" stroke="{RED}" stroke-width="4"/>' + T(800, 491, "9600 bauds ▾", 16, 800, INK) + f'<rect x="920" y="466" width="110" height="36" rx="6" fill="#fff" stroke="#c5ccd8"/>' + T(975, 490, "Effacer", 15, 700, INK)
    for bx, by in ((1070, 280), (800, 484), (1070, 98)): pass
    o += badge(130, 280, 1, BLUE, 15) + badge(682, 484, 2, BLUE, 15) + badge(135, 98, 3, BLUE, 15)
    o += T(120, 590, "1 · Zone d'affichage des messages", 15, 700, INK, "start") + T(430, 590, "2 · La vitesse doit correspondre à Serial.begin()", 15, 700, INK, "start") + T(860, 590, "3 · Saisie pour envoyer vers l'Arduino", 15, 700, INK, "start")
    return figure(W, 620, o)


def f_niveaux():
    o = ""; x0, y0, h = 380, 40, 440; sc = h / 5
    y = lambda v: y0 + h - v * sc
    for lo, hi, c, t in ((0, 0.8, "#f6c9c9", "LOGIQUE 0 — LOW — garanti"), (0.8, 2.0, "#e3e6eb", "ZONE INTERDITE — comportement indéterminé"), (2.0, 5.0, "#cdeedb", "LOGIQUE 1 — HIGH — garanti")):
        o += f'<rect x="{x0}" y="{y(hi)}" width="460" height="{(hi-lo)*sc}" fill="{c}"/>' + T(x0 + 230, y((lo + hi) / 2) + 6, t, 19, 800, {"#f6c9c9": RED, "#e3e6eb": MUTED, "#cdeedb": GREEN}[c])
    o += f'<line x1="{x0}" y1="{y0}" x2="{x0}" y2="{y0+h}" stroke="{INK}" stroke-width="3"/>' + ''.join(T(x0 - 14, y(v) + 6, f"{v} V".replace(".", ","), 17, 700, INK, "end") + f'<line x1="{x0-8}" y1="{y(v)}" x2="{x0}" y2="{y(v)}" stroke="{INK}" stroke-width="3"/>' for v in (0, 0.8, 2.0, 5))
    o += arrow(150, y(0.8), x0 - 70, y(0.8), RED, 4) + T(140, y(0.8) - 12, "Seuil bas = 0,8 V", 17, 800, RED, "start") + arrow(150, y(2.0), x0 - 70, y(2.0), GREEN, 4) + T(140, y(2.0) - 12, "Seuil haut = 2,0 V", 17, 800, GREEN, "start")
    o += T(1000, 140, "Une entrée doit toujours\nêtre franchement à 0 ou à 1.", 18, 700, INK) + T(1000, 330, "Entrée flottante\n= dans la zone interdite", 18, 700, RED)
    return figure(W, 530, o)


def scope_(x, y, w, h, pts, col):
    o = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="#10151b"/>' + ''.join(f'<line x1="{x}" y1="{y+h*i/4}" x2="{x+w}" y2="{y+h*i/4}" stroke="#1f2a33"/>' for i in range(1, 4))
    return o + f'<polyline points="{" ".join(f"{x+px*w:.0f},{y+h-py*h*0.8-h*0.1:.0f}" for px, py in pts)}" fill="none" stroke="{col}" stroke-width="3"/>'


def f_flottant():
    import random
    rnd = random.Random(7)
    o = duo(0, 0, "SANS résistance (entrée flottante)", "AVEC résistance pull-down 10 kΩ", RED, GREEN, h=450)
    o += f'<rect x="60" y="120" width="120" height="70" rx="8" fill="#e6efff" stroke="{BLUE}" stroke-width="3"/>' + T(120, 162, "D4", 22, 800, INK) + s_wire([(180, 155), (300, 155)]) + f'<circle cx="306" cy="155" r="6" fill="#fff" stroke="{INK}" stroke-width="3"/>' + T(240, 122, "broche en l'air", 16, 700, MUTED) \
        + ''.join(f'<path d="M{470-r*0.9:.0f},{155-r*0.55:.0f} A{r},{r} 0 0 0 {470-r*0.9:.0f},{155+r*0.55:.0f}" stroke="{RED}" stroke-width="3" fill="none" stroke-linecap="round"/>' for r in (34, 58, 82)) \
        + f'<path d="M488,128 L470,158 L484,158 L470,186 L506,148 L490,148 L504,128 Z" fill="{RED}"/>' + T(440, 105, "parasites (50 Hz, radio, main…)", 15, 700, RED)
    o += scope_(60, 230, 480, 150, [(i / 40, rnd.random()) for i in range(41)], "#ff6b6b") + T(300, 420, "IMPRÉVISIBLE", 24, 800, RED)
    o += f'<rect x="650" y="120" width="120" height="70" rx="8" fill="#e6efff" stroke="{BLUE}" stroke-width="3"/>' + T(710, 162, "D4", 22, 800, INK) + hrun(155, 770, 1000, [(880, "BP", "S1", {})]) + s_wire([(840, 155), (840, 215)]) + sym("R", 840, 235, rot=90) + gnd(840, 275) + T(870, 240, "10 kΩ", 17, 800, INK, "start")
    pts = [(0, 0), (.45, 0), (.45, 1), (.8, 1), (.8, 0), (1, 0)]
    o += scope_(650, 320, 480, 80, pts, "#4ade80") + T(890, 428, "STABLE : 0 V relâché · 5 V appuyé", 20, 800, GREEN)
    return figure(W, 500, o)


def f_pulldown_etats():
    o = duo(0, 0, "Bouton RELÂCHÉ", "Bouton APPUYÉ", BLUE, GREEN, h=470)
    d = 50
    for x0, closed in ((50, False), (640, True)):
        o += vrun(x0 + 40, 100 + d, 330, [(215 + 10, "BAT", "5 V", {})], -1) + hrun(100 + d, x0 + 40, x0 + 480, [(x0 + 220, "SW", "S1", {"closed": closed, "below": True})]) + s_wire([(x0 + 480, 100 + d), (x0 + 480, 190 + d - 20)])
        o += dot(x0 + 480, 190 + d - 20) + s_wire([(x0 + 480, 170 + d), (x0 + 430, 170 + d)]) + T(x0 + 420, 176 + d, "D4", 20, 800, INK, "end") + vrun(x0 + 480, 170 + d, 330, [(255, "R", "R_PD 10 kΩ", {})], -1, 52) + s_wire([(x0 + 40, 330), (x0 + 480, 330)]) + gnd(x0 + 260, 330)
        o += T(x0 + 270, 415, "D4 = 5 V : digitalRead = 1 (HIGH)" if closed else "D4 = 0 V : digitalRead = 0 (LOW)", 18, 800, GREEN if closed else RED) + T(x0 + 270, 442, "courant dans R_PD : 5 V / 10 kΩ = 0,5 mA" if closed else "courant nul : le bouton est ouvert", 15, 600, MUTED)
    return figure(W, 530, o)


def f_pulldown_pullup():
    o = duo(0, 0, "Pull-down EXTERNE", "INPUT_PULLUP interne", BLUE, AMBER, h=470)
    o += f'<rect x="60" y="100" width="140" height="150" rx="8" fill="#e6efff" stroke="{BLUE}" stroke-width="3"/>' + T(130, 140, "Arduino", 18, 800, BLUE) + T(130, 178, "D4", 22, 800, INK)
    o += s_wire([(200, 175), (300, 175)]) + vrun(300, 175, 330, [(250, "R", "10 kΩ", {})], 1, 50) + gnd(300, 330) + dot(300, 175) + hrun(175, 300, 470, [(380, "BP", "S1", {})]) + s_wire([(470, 175), (470, 150)]) + vcc(470, 150, "+5 V") + T(60, 400, "3 fils + 1 résistance", 16, 700, MUTED, "start") + chip(300, 440, "APPUYÉ = HIGH · RELÂCHÉ = LOW", BLUE, w=420, size=16)
    o += f'<rect x="650" y="100" width="140" height="150" rx="8" fill="#fff4dc" stroke="{AMBER}" stroke-width="3"/>' + T(720, 138, "Arduino", 18, 800, AMBER) + T(720, 178, "D4", 22, 800, INK) + sym("R", 760, 222, s=.5, color="#aaa") if False else f'<rect x="650" y="100" width="140" height="150" rx="8" fill="#fff4dc" stroke="{AMBER}" stroke-width="3"/>' + T(720, 138, "Arduino", 18, 800, AMBER) + T(720, 178, "D4", 22, 800, INK) + f'<rect x="745" y="195" width="26" height="46" fill="#fff" stroke="#999" stroke-width="2" stroke-dasharray="5 4"/>' + T(758, 262, "R interne", 12, 700, "#999") + f'<path d="M758,195 V160 H790" stroke="#999" stroke-width="2" stroke-dasharray="5 4" fill="none"/>'
    o += hrun(175, 790, 1000, [(900, "BP", "S1", {})]) + s_wire([(1000, 175), (1000, 300)]) + gnd(1000, 300) + T(660, 400, "2 fils seulement", 16, 700, MUTED, "start") + chip(880, 440, "APPUYÉ = LOW · RELÂCHÉ = HIGH  (logique inversée)", RED, w=470, size=16)
    return figure(W, 530, o)


def f_pyr_debug():
    o, h = pyramid([("4", "Niveau 4 : débogage avancé — temps, compteurs, états mémorisés", "#b3192b"), ("3", "Niveau 3 : débogage ciblé — afficher les valeurs utiles", AMBER), ("2", "Niveau 2 : débogage conditionnel — seulement lors d'un changement", "#c9a400"), ("1", "Niveau 1 : débogage de base — Serial.println() à chaque état", GREEN)], w=420, h=100, tx=540, sz=18)
    return figure(W, int(h), o.replace('font-size="18"', 'font-size="18"'))


def f_bugs():
    rows = [("1 · Entrée flottante", "LED aléatoire", "0 et 1 en alternance", "ajouter un pull-down"), ("2 · Logique inversée INPUT_PULLUP", "LED allumée au repos", "1 = relâché, 0 = appuyé", "inverser la condition du if"), ("3 · Variable d'état dans loop()", "la bascule ne marche pas", "etatLED toujours false", "déclarer la variable hors de loop()"), ("4 · Rebond du bouton", "LED qui clignote", "transitions multiples rapides", "ajouter un delay(50)"), ("5 · Mauvais port COM", "rien ne se passe", "aucune réception", "vérifier le port sélectionné")]
    return figure(W, 420, tbl(30, 30, [310, 250, 290, 290], ("Bug", "Symptôme visuel", "Symptôme Serial Monitor", "Correction"), rows, rh=66, hcol=INK, fs=16))


def f_uart_tx_rx():
    o = block(60, 80, 300, 220, "Arduino Uno", None, BLUE) + block(840, 80, 300, 220, "PC (USB-UART)", None, GREEN)
    for x, c in ((60, BLUE), (840, GREEN)): o += f'<rect x="{x+90}" y="215" width="120" height="50" rx="8" fill="#eef2f7" stroke="{c}" stroke-width="2"/>' + T(x + 150, 246, "horloge", 16, 800, c)
    o += f'<rect x="355" y="130" width="14" height="30" fill="#c0c6cf"/><rect x="831" y="130" width="14" height="30" fill="#c0c6cf"/><rect x="355" y="230" width="14" height="30" fill="#c0c6cf"/><rect x="831" y="230" width="14" height="30" fill="#c0c6cf"/>'
    o += T(335, 150, "TX", 18, 800, INK, "end") + T(335, 250, "RX", 18, 800, INK, "end") + T(865, 150, "RX", 18, 800, INK, "start") + T(865, 250, "TX", 18, 800, INK, "start")
    o += s_wire([(369, 145), (520, 145), (680, 245), (831, 245)], RED, 5) + s_wire([(369, 245), (520, 245), (680, 145), (831, 145)], BLUE, 5)
    o += T(600, 112, "TX → RX (fil rouge)", 18, 800, RED) + T(600, 285, "RX ← TX (fil bleu)", 18, 800, BLUE) + chip(600, 350, "Les fils sont croisés : l'émission d'un côté est la réception de l'autre", INK, w=760, size=16) + T(600, 410, "Pas d'horloge commune : les deux côtés doivent régler la même vitesse (9600 bauds)", 17, 700, MUTED)
    return figure(W, 450, o)


def f_trame_uart():
    o = ""; x0 = 150; bw = 82; y1, y0 = 140, 260
    bits = [("repos", 1), ("start", 0)] + [(f"D{i}", b) for i, b in enumerate((1, 0, 0, 0, 0, 0, 1, 0))] + [("stop", 1), ("repos", 1)]
    pts = []; col = []
    for i, (n, b) in enumerate(bits):
        x = x0 + i * bw; yb = y1 if b else y0
        o += f'<rect x="{x}" y="100" width="{bw}" height="190" fill="{"#fde8e8" if n in ("start","stop") else ("#e8f0ff" if n.startswith("D") else "#f6f8fc")}" stroke="#e1e7f1"/>' + T(x + bw / 2, 320, n if n.startswith("D") else n.upper() if n != "repos" else "repos", 16, 800, RED if n in ("start", "stop") else BLUE if n.startswith("D") else MUTED) + T(x + bw / 2, 348, str(b), 20, 800, INK)
        pts.append((x, yb)); pts.append((x + bw, yb))
    d = "M" + " L".join(f"{x},{y}" for x, y in pts)
    o += f'<path d="{d}" fill="none" stroke="{INK}" stroke-width="5" stroke-linejoin="miter"/>' + T(120, y1 + 6, "1", 18, 800, MUTED, "end") + T(120, y0 + 6, "0", 18, 800, MUTED, "end")
    o += f'<path d="M{x0+bw},82 h{bw}" stroke="{RED}" stroke-width="3"/>' + T(x0 + bw * 1.5, 70, "Start", 17, 800, RED) + f'<path d="M{x0+bw*2},82 h{bw*8}" stroke="{BLUE}" stroke-width="3"/>' + T(x0 + bw * 6, 70, "Data (LSB → MSB) : 'A' = 0x41", 17, 800, BLUE) + f'<path d="M{x0+bw*10},82 h{bw}" stroke="{RED}" stroke-width="3"/>' + T(x0 + bw * 10.5, 70, "Stop", 17, 800, RED)
    o += f'<path d="M{x0+bw*4},378 h{bw}" stroke="{INK}" stroke-width="3"/>' + T(x0 + bw * 4.5, 405, "T = 1/9600 ≈ 104 µs", 16, 800, INK) + T(600, 450, "'A' = 65 = 0100 0001 en binaire : envoyé bit de poids faible en premier (LSB first)", 17, 700, MUTED)
    return figure(W, 480, o)


def f_serial_params():
    o = ui_win(70, 30, 1060, 470, "Moniteur série (Arduino IDE 2.x)")
    o += f'<rect x="100" y="76" width="1000" height="44" rx="6" fill="#fff" stroke="#c5ccd8"/>' + T(115, 105, "Message", 15, 500, "#8a95a5", "start") + f'<rect x="990" y="82" width="100" height="32" rx="6" fill="#00878f"/>' + T(1040, 104, "Send", 15, 800, "#fff")
    o += f'<rect x="100" y="136" width="1000" height="250" rx="6" fill="#0f1a20"/>' + "".join(T(120, 172 + i * 34, t, 17, 600, "#cfe9d4", "start", extra='font-family="monospace"') for i, t in enumerate(("12:04:01.223 -> Température : 24.3", "12:04:02.226 -> Température : 24.4", "12:04:03.230 -> Température : 24.4")))
    o += f'<rect x="100" y="402" width="1000" height="70" rx="6" fill="#eef2f7"/>' + f'<rect x="120" y="426" width="22" height="22" rx="4" fill="#fff" stroke="{INK}" stroke-width="2"/>' + T(131, 444, "✓", 16, 800, GREEN) + T(152, 444, "Autoscroll", 15, 700, INK, "start") + f'<rect x="270" y="426" width="22" height="22" rx="4" fill="#fff" stroke="{INK}" stroke-width="2"/>' + T(281, 444, "✓", 16, 800, GREEN) + T(302, 444, "Show timestamp", 15, 700, INK, "start") + f'<rect x="470" y="420" width="130" height="34" rx="6" fill="#fff" stroke="#c5ccd8"/>' + T(535, 443, "Clear output", 14, 700, INK) + f'<rect x="700" y="420" width="190" height="34" rx="6" fill="#fff" stroke="#c5ccd8"/>' + T(795, 443, "Both NL & CR ▾", 14, 700, INK) + f'<rect x="910" y="420" width="170" height="34" rx="6" fill="#fff" stroke="#c5ccd8"/>' + T(995, 443, "9600 baud ▾", 14, 700, INK)
    for n, bx in enumerate((131, 281, 535, 795, 995), 1): o += badge(bx, 402 - 0, n, RED, 14) if False else badge(bx, 490, n, RED, 14)
    o += "".join(T(x, 548, f"{n} · {t}", 14, 700, INK, "start") for x, n, t in ((90, 1, "Autoscroll : défilement automatique"), (400, 2, "Show timestamp : heure de chaque ligne"), (730, 3, "Clear output : efface l'affichage")))
    o += "".join(T(x, 576, f"{n} · {t}", 14, 700, INK, "start") for x, n, t in ((90, 4, "Fin de ligne : Newline, Carriage return ou Both NL & CR"), (730, 5, "Vitesse : égale à Serial.begin()")))
    return figure(W, 610, o)


FIGS = {"arduino_uno_annote": f_uno, "arduino_ide": f_ide, "setup_loop": f_setup_loop, "schema_led_d13": f_schema_d13, "cablage_uno_breadboard": f_cablage_uno, "serial_monitor_ide": f_serial_monitor,
        "niveaux_logiques": f_niveaux, "flottant_pulldown": f_flottant, "pulldown_etats": f_pulldown_etats, "pulldown_pullup": f_pulldown_pullup, "pyramide_debug": f_pyr_debug, "tableau_bugs": f_bugs,
        "uart_tx_rx": f_uart_tx_rx, "trame_uart": f_trame_uart, "serial_monitor_params": f_serial_params}
