"""Seconde S02 à S05 : figures manquantes."""
from hl import *
import math


def f_led_serie():
    L, R, Tp, B = 170, 1030, 120, 330
    o = vrun(L, Tp, B, [((Tp + B) / 2, "BAT", "12 V", {})], -1)
    o = o.replace("", "")
    o += s_wire([(L, Tp), (R, Tp)]) if False else ""
    o += hrun(Tp, L, R, [(430, "R", "R", {}), (680, "LED", "LED 1", {"below": True}), (900, "LED", "LED 2", {"below": True})]) + s_wire([(R, Tp), (R, B)]) + s_wire([(R, B), (L, B)])
    o += arrow(220, Tp - 30, 360, Tp - 30, RED, 5) + T(290, Tp - 40, "I", 20, 800, RED) + arrow(R + 40, 170, R + 40, 280, RED, 5) if False else i_arrow(250, Tp, 360, Tp, "I", off=(0, -26), size=22)
    o += T(600, 235, "le même courant I traverse tous les composants", 20, 700, RED)
    o += f'<rect x="130" y="370" width="940" height="130" rx="14" fill="{PANEL}" stroke="#d9e0ec" stroke-width="2"/>'
    o += T(600, 412, "Les tensions s'additionnent : 12 V = U_R + V_F1 + V_F2", 21, 700, INK) + T(600, 452, "R = (12 − 2 − 2) / 0,020 = 400 Ω", 24, 800, BLUE) + T(600, 484, "avec V_F = 2 V par LED rouge et I = 20 mA", 16, 500, MUTED)
    return figure(W, 530, o)


def f_led_parallele():
    L, Tp, B, J, X1, X2 = 150, 120, 340, 480, 700, 950
    o = vrun(L, Tp, B, [(230, "BAT", "9 V", {})], -1) + hrun(Tp, L, X2, [(330, "R", "R", {})]) + s_wire([(X2, Tp), (X2, 140)]) + dot(J, Tp)
    for x, nm in ((X1, "LED 1"), (X2, "LED 2")):
        o += s_wire([(J, Tp), (x, Tp)]) + vrun(x, Tp, B, [(230, "LED", nm, {})], 1, 60) + (dot(x, Tp) if x == X1 else "") + (dot(x, B) if x == X1 else "")
    o += s_wire([(L, B), (X2, B)])
    o += i_arrow(195, Tp, 265, Tp, "I total", off=(0, -26), size=19)
    o += i_arrow(X1, 150, X1, 190, "I1", off=(-14, 0), size=18, w=4) + i_arrow(X2, 150, X2, 190, "I2", off=(-14, 0), size=18, w=4)
    o += f'<rect x="130" y="385" width="940" height="125" rx="14" fill="{PANEL}" stroke="#d9e0ec" stroke-width="2"/>'
    o += T(600, 425, "Même tension V_F aux bornes de chaque branche · I total = I1 + I2", 20, 700, INK) + T(600, 465, "R = (9 − 2) / (2 × 0,020) = 175 Ω", 24, 800, BLUE) + T(600, 495, "la résistance commune supporte le courant des deux LED", 16, 500, MUTED)
    return figure(W, 540, o)


def room(x, y, w, h, c): return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{c}"/>'


def f_cablage_ok_ko():
    o = ""
    def board(ox, ok):
        bb = Breadboard(cols=12); s = 1.55
        inner = bb.draw(); P = bb.P
        def xy(c, r): return bb.xy(c, r)
        def wire(p, q, col): return f'<path d="M{p[0]},{p[1]} L{q[0]},{q[1]}" stroke="{col}" stroke-width="5" stroke-linecap="round"/>'
        def res(p, q): return f'<rect x="{p[0]-2}" y="{p[1]-6}" width="{q[0]-p[0]+4}" height="12" rx="4" fill="#e9d4a3" stroke="#a88"/>' + f'<rect x="{p[0]+14}" y="{p[1]-6}" width="4" height="12" fill="#7a4320"/><rect x="{p[0]+24}" y="{p[1]-6}" width="4" height="12" fill="#000"/><rect x="{p[0]+34}" y="{p[1]-6}" width="4" height="12" fill="#7a4320"/>'
        def resv(p, q): return f'<rect x="{p[0]-6}" y="{p[1]-2}" width="12" height="{q[1]-p[1]+4}" rx="4" fill="#e9d4a3" stroke="#a88"/>' + ''.join(f'<rect x="{p[0]-6}" y="{p[1]+10+i*10}" width="12" height="4" fill="{c}"/>' for i, c in enumerate(("#7a4320", "#000", "#7a4320")))
        def led(a, k):
            cx = (a[0] + k[0]) / 2
            by = min(a[1], k[1]) - 26          # base du boîtier
            hw = 10                            # demi-largeur du boîtier
            xa, xk = (cx - 6, cx + 6) if a[0] <= k[0] else (cx + 6, cx - 6)
            ya, yk = a[1] - 8, k[1] - 8
            legs = (f'<path d="M{a[0]},{a[1]} V{ya} L{xa},{by}" fill="none" stroke="#aaa" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>'
                    f'<path d="M{k[0]},{k[1]} V{yk} L{xk},{by}" fill="none" stroke="#aaa" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>')
            body = (f'<path d="M{cx-hw},{by} V{by-6} A{hw},{hw} 0 0 1 {cx+hw},{by-6} V{by} Z" fill="#e5353b" stroke="#a11" stroke-width="1.5"/>'
                    f'<rect x="{cx-hw-2}" y="{by-2}" width="{2*hw+4}" height="4" rx="2" fill="#c42a30" stroke="#a11" stroke-width="1"/>')
            return legs + body
        if ok:
            inner += wire(bb.rail(0, "T+"), xy(2, "a"), RED) + res(xy(2, "c"), xy(6, "c")) + led(xy(6, "a"), xy(9, "a")) + wire(xy(9, "b"), bb.rail(10, "T-"), "#111")
        else:
            inner += wire(bb.rail(0, "T+"), xy(2, "a"), "#111") + resv(xy(2, "b"), xy(2, "e")) + led(xy(6, "a"), xy(6, "b")) + wire(xy(9, "b"), bb.rail(10, "T-"), RED)
        return g(ox + 60, 90, inner, s)
    o += duo(0, 0, "Câblage CORRECT", "Câblage INCORRECT", GREEN, RED, h=770, wa=570)
    o += board(40, True) + board(630, False)
    for x, ok, items in ((60, True, ["fil rouge : bus + → rangée 2", "résistance : 2 rangées différentes", "LED : anode et cathode dans 2 rangées", "fil noir : retour vers le bus −"]), (650, False, ["fil noir sur le + : alimentation inversée", "résistance : 2 broches dans la même rangée (court-circuitée)", "LED : 2 broches dans la même rangée", "fil rouge sur le − : retour au mauvais bus"])):
        for i, t in enumerate(items): o += T(x, 438 + i * 24 + (0), ("✔ " if ok else "✘ ") + t, 15, 600, GREEN if ok else RED, "start") if False else T(x + 4, 650 + i * 26, ("✔  " if ok else "✘  ") + t, 15, 600, GREEN if ok else RED, "start")
    return figure(W, 830, o)


def f_schema_parallele_iec():
    L, Tp, B, J, X1, X2 = 150, 130, 330, 470, 690, 900
    o = vrun(L, Tp, B, [(230, "BAT", "9 V", {})], -1) + hrun(Tp, L, J, [(320, "R", "R1 = 390 Ω", {})]) + dot(J, Tp)
    o += s_wire([(J, Tp), (X2, Tp)]) + dot(X1, Tp)
    for x, nm, col in ((X1, "D1 rouge", RED), (X2, "D2 verte", GREEN)):
        o += vrun(x, Tp, B, [(230, "LED", nm, {})], 1, 60) + T(x + 60, 262, "V_F = 2 V" if col == RED else "V_F = 2,1 V", 15, 600, MUTED, "start")
    o += s_wire([(L, B), (X2, B)]) + dot(X1, B) + gnd(L + 250, B) + T(L + 250, B + 60, "GND", 17, 800, INK)
    o += callout(J, Tp, J + 40, 80, "jonction (point noir)", "start", 17, bold=True) + chip(600, 480, "Courant total = I(D1) + I(D2) · tension V_F identique sur chaque branche", INK, w=760, size=16)
    return figure(W, 530, o)


def f_arbre_continuite():
    o = block(430, 20, 340, 62, "Le circuit ne fonctionne pas", None, RED)
    steps = [("1 · Test bus + → fil rouge", "fil rouge mal branché"), ("2 · Test fil rouge → résistance", "résistance mal posée"), ("3 · Test résistance → LED", "LED mal posée"), ("4 · Test LED → bus −", "fil noir mal branché")]
    y = 110
    for i, (t, bad) in enumerate(steps):
        o += s_wire([(600, y - 28 if i else 82), (600, y)], INK, 3) + block(380, y, 440, 62, t, None, BLUE)
        o += s_wire([(820, y + 31), (900, y + 31)], RED, 3) + T(860, y + 22, "pas de BIP", 13, 800, RED) + block(900, y, 270, 62, "→ " + bad, "corriger puis refaire le test" if False else None, RED)
        o += T(405, y + 92, "BIP : on passe au test suivant", 14, 800, GREEN, "start") if False else ""
        o += T(590, y + 90, "BIP ✔", 14, 800, GREEN, "end")
        y += 108
    o += s_wire([(600, y - 28), (600, y)], GREEN, 3) + block(380, y, 440, 62, "Tout est continu : tester l'alimentation", None, GREEN)
    return figure(W, y + 100, o)


def f_station_soudure():
    o = '<g filter="url(#sh)"><rect x="90" y="190" width="330" height="190" rx="18" fill="#3a4250"/></g><rect x="110" y="210" width="150" height="70" rx="8" fill="#10151b"/>' + T(185, 262, "360°C", 40, 700, "#ff5a4a", extra='font-family="monospace"')
    o += '<circle cx="350" cy="250" r="40" fill="#cfd6df" stroke="#8a95a5" stroke-width="3"/><path d="M350,250 L350,220" stroke="#333" stroke-width="5" stroke-linecap="round"/>' + '<rect x="110" y="310" width="300" height="50" rx="6" fill="#2a303b"/>' + T(260, 342, "ON / OFF", 18, 700, "#aab3c5")
    o += '<g filter="url(#sh)"><rect x="560" y="340" width="260" height="60" rx="8" fill="#6a7384"/></g><path d="M600,340 V270 L580,230" stroke="#6a7384" stroke-width="12" fill="none"/>'
    o += '<path d="M640,300 L930,200" stroke="#232831" stroke-width="30" stroke-linecap="round"/><path d="M640,300 L760,258" stroke="#f2c230" stroke-width="30" stroke-linecap="round"/><path d="M930,200 L985,180" stroke="#aeb6c2" stroke-width="12" stroke-linecap="round"/><path d="M985,180 L1010,172" stroke="#d98a3a" stroke-width="6" stroke-linecap="round"/>'
    o += '<path d="M1010,172 q-40,40 20,60" stroke="#d6dbe3" fill="none" stroke-width="0"/><rect x="900" y="410" width="200" height="90" rx="8" fill="#e7d27a" stroke="#b3a050" stroke-width="2"/><rect x="915" y="395" width="170" height="40" rx="6" fill="#c9a45a"/>'
    o += '<g transform="translate(700,400)"><path d="M-60,0 h120 v70 h-120 z" fill="#d7dde6" stroke="#8a95a5" stroke-width="2"/>' + ''.join(f'<path d="M{-50+i*12},6 v58" stroke="#a9b3c1" stroke-width="3"/>' for i in range(9)) + '</g>'
    for n, (px, py, tx, ty, t) in enumerate([(185, 240, 40, 70, "Afficheur (réglé à 360 °C)"), (350, 210, 430, 70, "Bouton de réglage"), (750, 270, 640, 130, "Poignée isolée du fer"), (990, 176, 880, 70, "Panne type crayon"), (700, 425, 560, 540, "Support avec laine de cuivre"), (1000, 450, 940, 540, "Éponge humide")], 1):
        o += callout(px, py, tx, ty, "", "start", 16) + badge(tx, ty, n, BLUE, 15) + T(tx + 24, ty + 6, t, 16, 700, INK, "start")
    return figure(W, 570, o)


def f_materiaux_soudure():
    o = panel(30, 30, 370, 470, "1 · Fil d'étain", accent=BLUE) + panel(415, 30, 370, 470, "2 · Flux (gel)", accent=AMBER) + panel(800, 30, 370, 470, "3 · Tresse à dessouder", accent=GREEN)
    o += '<g filter="url(#sh)"><ellipse cx="215" cy="220" rx="115" ry="38" fill="#b9c1cc"/><rect x="100" y="140" width="230" height="80" fill="#cfd6df"/><ellipse cx="215" cy="140" rx="115" ry="38" fill="#e3e8ef"/></g><rect x="160" y="165" width="110" height="50" rx="4" fill="#fff"/>' + T(215, 186, "SAC305", 15, 800, INK) + T(215, 205, "Sn96,5 Ag3 Cu0,5", 11, 600, MUTED)
    o += '<path d="M330,205 q60,20 20,70" stroke="#c0c6cf" stroke-width="5" fill="none"/>'
    o += '<g filter="url(#sh)"><path d="M520,150 h150 l12,200 h-174 z" fill="#f7da6b" opacity=".9"/><rect x="540" y="110" width="110" height="40" rx="6" fill="#b3b9c4"/><path d="M572,350 l8,50 h10 l8,-50" fill="#f2d25a"/></g>' + T(600, 250, "FLUX", 24, 800, "#8a6a00")
    o += '<g filter="url(#sh)"><circle cx="985" cy="230" r="85" fill="#d99c52"/><circle cx="985" cy="230" r="30" fill="#fff" stroke="#b5732e" stroke-width="3"/></g>' + ''.join(f'<circle cx="985" cy="230" r="{40+i*9}" fill="none" stroke="#b5732e" stroke-width="2"/>' for i in range(5)) + '<rect x="985" y="262" width="150" height="18" rx="4" fill="#d99c52" transform="rotate(20 985 262)"/>'
    for x, a, b in ((215, "Fil d'étain 0,8 mm", "alliage sans plomb SAC305\nassemble les pièces"), (600, "Flux en gel", "désoxyde le cuivre\nl'étain mouille mieux"), (985, "Tresse 2,5 mm", "absorbe l'étain fondu\npour dessouder")):
        o += T(x, 420, a, 20, 800, INK) + T(x, 448, b, 15, 500, MUTED)
    return figure(W, 530, o)


def f_etapes_soudure():
    o = ""
    st = [("1", "Insérer", "pattes qui dépassent"), ("2", "Chauffer", "panne sur patte + pastille"), ("3", "Apporter l'étain", "côté opposé à la panne"), ("4", "Retirer l'étain", "puis le fer, sans bouger"), ("5", "Refroidir", "2 à 3 secondes")]
    for i, (n, t, s) in enumerate(st):
        x = 20 + i * 232; o += f'<rect x="{x}" y="30" width="216" height="360" rx="14" fill="{PANEL}" stroke="#d9e0ec" stroke-width="2"/>' + badge(x + 28, 62, n, BLUE)
        cx = x + 108; o += f'<rect x="{x+16}" y="230" width="184" height="16" fill="#1c7a46"/><rect x="{cx-26}" y="226" width="52" height="8" fill="{COPPER}"/><rect x="{cx-26}" y="244" width="52" height="8" fill="{COPPER}"/>'
        up = 130 if i else 120; lead = f'<rect x="{cx-3}" y="{up}" width="6" height="{262-up}" fill="#c0c6cf"/>'
        o += f'<rect x="{cx-22}" y="150" width="44" height="76" rx="6" fill="#222" opacity="0"/>' + lead
        if i == 0: o += f'<rect x="{cx-30}" y="100" width="60" height="30" rx="6" fill="#333"/>'
        if i in (1, 2): o += f'<path d="M{cx-42},180 L{cx-6},242" stroke="#232831" stroke-width="14" stroke-linecap="round"/>'
        if i == 2: o += f'<path d="M{cx+50},170 L{cx+8},236" stroke="#cfd6df" stroke-width="5" stroke-linecap="round"/><path d="M{cx-10},226 q10,-22 20,0 z" fill="#d9dee5"/>'
        if i == 3: o += f'<path d="M{cx-12},226 q12,-34 24,0 z" fill="#d9dee5"/><path d="M{cx-60},160 L{cx-14},200" stroke="#232831" stroke-width="14" stroke-linecap="round" opacity=".5"/>'
        if i == 4: o += f'<path d="M{cx-14},226 q14,-40 28,0 z" fill="#e5e9ef"/>' + T(cx, 190, "❄", 40, 700, "#6fa8dc")
        o += T(cx, 300, t, 20, 800, INK) + T(cx, 326, s, 14, 500, MUTED)
    o += chip(600, 440, "Temps total : 2 à 4 secondes — pas plus, sinon la pastille se décolle", INK, w=820, size=17)
    return figure(W, 480, o)


def f_pyramide_ipc():
    o, h = pyramid([("Classe 3", "Haute fiabilité : médical, aéronautique, militaire", RED), ("Classe 2", "Électronique industrielle et professionnelle : notre référence", BLUE), ("Classe 1", "Grand public : jouets, télécommandes, électroménager", GREEN)], h=104)
    return figure(W, int(h), o)


def f_brasure_coupe():
    cx = 360; o = f'<rect x="120" y="230" width="480" height="44" fill="#1c7a46"/><rect x="{cx-22}" y="230" width="44" height="44" fill="#0e4a2a"/>'
    o += f'<rect x="{cx-70}" y="222" width="140" height="8" fill="{COPPER}"/><rect x="{cx-70}" y="274" width="140" height="8" fill="{COPPER}"/><rect x="{cx-24}" y="230" width="3" height="44" fill="{COPPER}"/><rect x="{cx+21}" y="230" width="3" height="44" fill="{COPPER}"/>'
    o += f'<rect x="{cx-9}" y="90" width="18" height="260" fill="#c0c6cf" stroke="#8a95a5"/>'
    o += f'<path d="M{cx-9},222 C{cx-20},205 {cx-60},215 {cx-72},222 Z" fill="#d6dbe3" stroke="#8a95a5"/><path d="M{cx+9},222 C{cx+20},205 {cx+60},215 {cx+72},222 Z" fill="#d6dbe3" stroke="#8a95a5"/><path d="M{cx-9},282 C{cx-20},300 {cx-60},292 {cx-72},282 L{cx-72},282 Z" fill="#d6dbe3" stroke="#8a95a5"/><path d="M{cx+9},282 C{cx+20},300 {cx+60},292 {cx+72},282 Z" fill="#d6dbe3" stroke="#8a95a5"/>'
    o += f'<rect x="{cx-22}" y="222" width="44" height="60" fill="#d6dbe3" opacity=".9"/><rect x="{cx-9}" y="90" width="18" height="260" fill="#c0c6cf" stroke="#8a95a5"/>'
    items = [(cx + 60, 212, 620, 90, "Brasure brillante, lisse, en forme de cône concave"), (cx + 70, 226, 620, 160, "Mouillage complet sur la pastille (≥ 75 %)"), (cx + 23, 250, 620, 230, "Trou métallisé rempli d'étain (≥ 75 % de la hauteur)"), (cx - 60, 290, 40, 420, "Pastille côté soudure bien recouverte"), (cx + 80, 345, 620, 340, "Patte dépassant de 0,5 à 1,5 mm (côté soudure)")]
    for n, (px, py, tx, ty, t) in enumerate(items, 1): o += callout(px, py, tx, ty, "", "start") + badge(tx, ty, n, BLUE, 15) + T(tx + 24, ty + 6, t, 16, 700, INK, "start") if False else callout(px, py, tx, ty, "", "start") + badge(tx, ty, n, BLUE, 15) + T(tx + 24 if tx > 400 else tx + 24, ty + 6, t, 16, 700, INK, "start")
    o += chip(360, 40, "Brasure traversante IPC classe 2 acceptable", GREEN, w=520, size=18)
    return figure(W, 460, o)


def f_defauts_brasures():
    d = [("Brasure froide", "mate, granuleuse", "gran"), ("Pont d'étain", "relie deux pastilles", "bridge"), ("Excès d'étain", "boule convexe", "ball"), ("Manque d'étain", "mouillage insuffisant", "less"), ("Brasure perturbée", "stries de mouvement", "stri"), ("Soufflure", "cratère dans l'étain", "void"), ("Délaminage", "pastille décollée", "lift")]
    o = ""
    for i, (t, s, k) in enumerate(d):
        x = 25 + (i % 4) * 292; y = 25 + (i // 4) * 270
        o += f'<rect x="{x}" y="{y}" width="276" height="250" rx="14" fill="{PANEL}" stroke="#d9e0ec" stroke-width="2"/>'
        cx, cy = x + 138, y + 100
        pad = lambda px, r=40: f'<circle cx="{px}" cy="{cy}" r="{r}" fill="{COPPER}"/><circle cx="{px}" cy="{cy}" r="9" fill="#2b2b2b"/>'
        if k == "bridge": o += pad(cx - 45, 34) + pad(cx + 45, 34) + f'<rect x="{cx-45}" y="{cy-10}" width="90" height="20" rx="10" fill="#d6dbe3"/>'
        elif k == "lift": o += f'<circle cx="{cx+6}" cy="{cy-8}" r="40" fill="#d99a60" transform="rotate(8 {cx} {cy})"/><circle cx="{cx}" cy="{cy}" r="40" fill="{COPPER}" opacity=".5"/><circle cx="{cx}" cy="{cy}" r="9" fill="#2b2b2b"/><path d="M{cx+20},{cy-36} q30,10 22,40" stroke="#b45d1c" stroke-width="3" fill="none"/>'
        else:
            col = {"gran": "#9aa0a8", "ball": "#e3e8ef", "less": "#d6dbe3", "stri": "#c3c8d0", "void": "#d6dbe3"}[k]; r = {"ball": 42, "less": 20}.get(k, 36)
            o += pad(cx) + f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{col}" stroke="#8a95a5" stroke-width="2"/>' + f'<circle cx="{cx}" cy="{cy}" r="7" fill="#444"/>'
            if k == "gran": o += ''.join(f'<circle cx="{cx+int(18*math.cos(a))}" cy="{cy+int(18*math.sin(a))}" r="3" fill="#7e848c"/>' for a in [i * 0.9 for i in range(7)])
            if k == "ball": o += f'<ellipse cx="{cx-10}" cy="{cy-14}" rx="12" ry="7" fill="#fff" opacity=".8"/>'
            if k == "stri": o += ''.join(f'<path d="M{cx-26},{cy-14+j*10} h52" stroke="#8a95a5" stroke-width="2"/>' for j in range(4))
            if k == "void": o += f'<circle cx="{cx+12}" cy="{cy-8}" r="10" fill="#2b2b2b" opacity=".8"/><circle cx="{cx-14}" cy="{cy+10}" r="6" fill="#2b2b2b" opacity=".8"/>'
        o += T(cx, y + 182, t, 19, 800, INK) + T(cx, y + 206, s, 14, 500, MUTED) + chip(cx, y + 232, "IPC : REFUS", RED, w=120, size=13) if False else T(cx, y + 182, t, 19, 800, INK) + T(cx, y + 206, s, 14, 500, MUTED) + chip(cx, y + 230, "IPC : REFUS", RED, w=120, size=13)
    o += f'<rect x="{25+3*292}" y="295" width="276" height="250" rx="14" fill="#fff4f4" stroke="{RED}" stroke-width="2"/>' + T(25 + 3 * 292 + 138, 380, "Règle", 22, 800, RED) + T(25 + 3 * 292 + 138, 420, "tout défaut est refusé", 17, 700, INK) + T(25 + 3 * 292 + 138, 446, "par la norme IPC :", 17, 700, INK) + T(25 + 3 * 292 + 138, 472, "dessouder et refaire", 17, 700, INK)
    return figure(W, 570, o)


def f_sequence_insertion():
    o = f'<rect x="60" y="350" width="1080" height="40" fill="#1c7a46"/><rect x="60" y="390" width="1080" height="10" fill="#0e4a2a"/>'
    parts = [("1", "Straps", "fil, hauteur nulle", 6, "#9aa0a8"), ("2", "Résistances", "couchées", 14, "#e9d4a3"), ("3", "Diodes", "faibles", 22, "#222"), ("4", "Condensateurs\ncéramiques", "petits", 36, "#d9a441"), ("5", "Supports de CI", "moyens", 46, "#333"), ("6", "Condensateurs\nélectrolytiques", "hauts", 90, "#2b4a8a"), ("7", "Connecteurs", "les plus hauts", 120, "#1b6a3a")]
    for i, (n, t, s, h, c) in enumerate(parts):
        x = 110 + i * 150
        o += f'<rect x="{x}" y="{350-h}" width="90" height="{h}" rx="5" fill="{c}" stroke="#0003"/>' + f'<rect x="{x+20}" y="350" width="6" height="30" fill="#c0c6cf"/><rect x="{x+64}" y="350" width="6" height="30" fill="#c0c6cf"/>'
        o += badge(x + 45, 350 - h - 30, n, BLUE, 18) + T(x + 45, 430, t, 15, 800, INK) + T(x + 45, 478, s, 14, 500, MUTED)
    o += arrow(100, 80, 1080, 80, MUTED, 4) + T(590, 62, "ordre d'insertion : du plus bas au plus haut", 20, 800, MUTED) + T(590, 520, "Les pièces basses d'abord : la carte posée à l'envers reste stable pendant la soudure", 16, 600, INK)
    return figure(W, 550, o)


FIGS = {"led_serie": f_led_serie, "led_parallele": f_led_parallele, "cablage_ok_ko": f_cablage_ok_ko, "schema_parallele_iec": f_schema_parallele_iec, "arbre_continuite": f_arbre_continuite,
        "station_soudure": f_station_soudure, "materiaux_soudure": f_materiaux_soudure, "etapes_soudure": f_etapes_soudure, "pyramide_ipc": f_pyramide_ipc, "brasure_coupe": f_brasure_coupe,
        "defauts_brasures": f_defauts_brasures, "sequence_insertion": f_sequence_insertion}
