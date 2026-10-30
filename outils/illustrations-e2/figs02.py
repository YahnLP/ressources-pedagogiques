from lib import *
from figs01 import chain

W = 1200


def bb_resistor(a, b, bands=("orange", "orange", "marron", "or")):
    (x1, y1), (x2, y2) = a, b
    cx, cy = (x1 + x2) / 2, (y1 + y2) / 2
    o = f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#9aa4b2" stroke-width="3.2"/>'
    o += f'<rect x="{cx-22}" y="{cy-7.5}" width="44" height="15" rx="6" fill="#e9d4a3"/>'
    for i, c in enumerate(bands):
        x = cx - 15 + i * 8 + (6 if i == 3 else 0)
        o += f'<rect x="{x}" y="{cy-7.5}" width="4" height="15" fill="{COLORS[c]}"/>'
    o += f'<rect x="{cx-22}" y="{cy-7.5}" width="44" height="15" rx="6" fill="url(#cylShade)"/>'
    return o


def f_schema_vs_montage():
    o = panel(30, 40, 500, 500, "Schéma électrique", accent=BLUE)
    o += vcc(150, 150, "+5 V") + s_wire([(150, 150), (150, 190)]) + sym("R", 150, 230, 90) + T(190, 236, "330 Ω", 19, 800, INK, "start")
    o += s_wire([(150, 270), (150, 300)]) + dot(150, 285) + sym("LED", 150, 340, 90) + s_wire([(150, 380), (150, 420)]) + gnd(150, 420)
    o += badge(70, 128, 1, BLUE) + badge(200, 290, 2, AMBER) + badge(70, 440, 3, GREEN)
    o += T(280, 515, "symboles normalisés : lisible, universel", 16, 600, MUTED)
    bb = Breadboard(18)
    o += panel(550, 40, 620, 500, "Montage réel sur breadboard", accent=GREEN)
    s_, ox, oy = 1.1, 600, 105
    P = lambda x, y: (ox + x * s_, oy + y * s_)
    inner = bb.draw(numbers=True, letters=True)
    a_, b_ = bb.xy(4, "c"), bb.xy(8, "c")
    inner += bb.wire(bb.rail(3, "T+"), bb.xy(4, "a"), "#d63f3f")
    inner += bb_resistor(a_, b_)
    ax, ay = bb.xy(8, "a")
    kx, ky = bb.xy(9, "a")
    inner += f'<path d="M{ax},{ay} V{ay-4} M{kx},{ky} V{ky-4}" stroke="#9aa4b2" stroke-width="3"/>'
    inner += f'<g transform="translate({(ax+kx)/2},{ay-4}) scale(.5)">{led(lit=True, legs=False)}</g>'
    inner += bb.wire(bb.xy(9, "e"), bb.rail(8, "B-"), "#222", bow=-40)
    o += g(ox, oy, inner, s_)
    x1, y1 = P(*bb.rail(3, "T+")); o += badge(x1 - 6, y1 - 24, 1, BLUE, 15)
    x2, y2 = P(*bb.xy(8, "d")); o += badge(x2 + 22, y2, 2, AMBER, 15)
    x3, y3 = P(*bb.rail(8, "B-")); o += badge(x3 + 24, y3, 3, GREEN, 15)
    o += T(860, 525, "même circuit, deux représentations (repères 1, 2, 3 identiques)", 16, 600, MUTED)
    return figure(W, 570, o)


def f_symboles():
    cells = [("Résistance", "R", "R"), ("Condensateur", "C", "C"), ("Cond. polarisé", "CP", "C"), ("Bobine", "L", "L"), ("Diode", "D", "D"),
             ("LED", "LED", "D / LED"), ("Pile / source", "BAT", "G · E"), ("Interrupteur", "SW", "S"), ("Bouton poussoir", "BP", "BP"), ("Lampe", "LAMP", "H · L"),
             ("Potentiomètre", "POT", "RV"), ("Moteur", "MOTOR", "M"), ("Masse (GND)", "GND", "GND"), ("Alimentation", "VCC", "Vcc"), ("Transistor NPN", "NPN", "Q · T")]
    o = ""
    cw, ch = 226, 178
    for i, (name, k, rep) in enumerate(cells):
        x, y = 30 + (i % 5) * (cw + 3), 30 + (i // 5) * (ch + 6)
        o += f'<rect x="{x}" y="{y}" width="{cw}" height="{ch}" rx="14" fill="{PANEL}" stroke="#e1e7f1" stroke-width="2"/>'
        cx, cy = x + cw / 2, y + 78
        if k == "GND":
            o += s_wire([(cx, cy - 25), (cx, cy - 11)]) + gnd(cx, cy - 11)
        elif k == "VCC":
            o += vcc(cx, cy + 22, "+5 V")
        elif k == "NPN":
            o += npn(cx, cy, .9)
        else:
            o += sym(k, cx, cy, s=1.15, closed=False)
        o += T(cx, y + 138, name, 18, 700, INK)
        o += chip(cx, y + 163, "repère : " + rep, BLUE, size=13, w=130)
    return figure(W, 30 + 3 * (ch + 6) + 6, o)


def f_jonction():
    o = ""
    spec = [("Croisement", 30, False, "pas de point :\nles fils ne sont PAS connectés", RED, "NON connectés"),
            ("Jonction", 410, True, "point noir :\nles fils sont connectés", GREEN, "Connectés"),
            ("Dérivation en T", 790, None, "un fil qui se termine sur un autre :\ntoujours connecté", GREEN, "Connectés")]
    for t, x, dotv, d, col, chp in spec:
        o += panel(x, 40, 380, 400, t, accent=col)
        cx, cy = x + 190, 210
        if dotv is None:
            o += s_wire([(cx - 90, cy), (cx + 90, cy)]) + s_wire([(cx, cy), (cx, cy + 80)]) + dot(cx, cy, 8)
        else:
            o += s_wire([(cx - 90, cy), (cx + 90, cy)]) + s_wire([(cx, cy - 80), (cx, cy + 80)])
            if dotv:
                o += dot(cx, cy, 9)
        o += chip(cx, 330, chp, col, size=19)
        o += T(cx, 380, d, 16, 500, MUTED)
    return figure(W, 480, o)


def f_schema_bloc():
    o = chain([("ENTRÉE : CAPTEUR", BLUE, [(ldr(), 1.0, 0, 95)], "LDR : mesure la lumière\n→ tension variable"),
               ("TRAITEMENT", AMBER, [(dip(8, h=84, pitch=30, label="µC", fs=22), 1.5, -88, 40)], "microcontrôleur :\ncompare à un seuil, décide"),
               ("SORTIE : ACTIONNEUR", GREEN, [(led(lit=True), .95, 0, 85)], "LED : s'allume\nquand il fait sombre")], 440, labels=None)
    return figure(W, 440, o)


def f_polarites():
    o = panel(30, 40, 560, 420, "LED", accent=BLUE) + panel(610, 40, 560, 420, "Condensateur chimique", accent=GREEN)
    o += g(200, 230, led(lit=True), 1.15)
    o += callout(212, 330, 330, 400, "anode (+) : patte longue", "start", 16, bold=True)
    o += callout(186, 300, 60, 420, "cathode (−) :\npatte courte, méplat", "start", 15, bold=True)
    o += sym("LED", 470, 190, s=1.2) + T(422, 245, "A", 19, 800) + T(518, 245, "K", 19, 800)
    o += g(790, 330, electrolytic(h=130), 1.2)
    o += callout(733, 230, 880, 120, "bande « − » = cathode", "start", 16, bold=True)
    o += callout(814, 440, 900, 410, "patte longue = « + »", "start", 16, bold=True)
    o += sym("CP", 1040, 230, s=1.3)
    o += T(1040, 285, "+ du côté de la patte longue", 15, 600, MUTED)
    return figure(W, 490, o)


def f_methode():
    o = ""
    o += panel(30, 30, 700, 450, fill="#fff")
    o += vcc(90, 160, "+5 V") + s_wire([(90, 160), (160, 160)]) + sym("BP", 200, 160) + s_wire([(240, 160), (320, 160)]) + sym("R", 360, 160) + s_wire([(400, 160), (560, 160), (560, 210)])
    o += sym("LED", 560, 250, 90) + s_wire([(560, 290), (560, 360)])
    o += dot(280, 160) + s_wire([(280, 160), (280, 220)]) + sym("CP", 280, 260, 90) + s_wire([(280, 300), (280, 360)])
    o += s_wire([(90, 360), (640, 360)]) + gnd(420, 360) + dot(420, 360) + dot(280, 360) + dot(560, 360)
    o += T(200, 118, "BP", 19, 800, INK) + T(360, 118, "R1", 19, 800, INK) + T(610, 255, "D1", 19, 800, INK, "start") + T(320, 262, "C1", 19, 800, INK, "start")
    o += badge(40, 175, 1, BLUE) + badge(400, 398, 1, BLUE)
    for x1, y1, x2, y2 in ((115, 138, 150, 138), (430, 138, 470, 138)):
        o += arrow(x1, y1, x2, y2, GREEN, 4)
    o += arrow(584, 215, 584, 245, GREEN, 4) + badge(470, 120, 2, GREEN)
    o += badge(280, 128, 3, AMBER) + badge(600, 213, 4, RED) + badge(247, 238, 4, RED)
    items = [("Alimentation", "repérer Vcc (+) et GND (0 V)", BLUE), ("Connexions", "suivre le trajet du courant", GREEN), ("Jonctions", "points noirs = fils reliés", AMBER), ("Polarités", "+ / − , anode / cathode", RED)]
    for i, (a, b, c) in enumerate(items):
        y = 70 + i * 105
        o += f'<rect x="760" y="{y}" width="410" height="90" rx="14" fill="{PANEL}" stroke="#e1e7f1" stroke-width="2"/>'
        o += badge(800, y + 45, i + 1, c, 20) + T(840, y + 40, a, 22, 800, INK, "start") + T(840, y + 68, b, 17, 500, MUTED, "start")
    return figure(W, 510, o)


def f_breadboard():
    bb = Breadboard(30)
    inner = bb.draw()
    # surbrillance : une colonne (5 trous reliés), les rails, le canal
    def band(x, y, w, h, c, op=.22):
        return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="9" fill="{c}" opacity="{op}" stroke="{c}" stroke-width="2.5" stroke-opacity=".8"/>'
    x, y1 = bb.xy(8, "a"); _, y2 = bb.xy(8, "e")
    inner += band(x - 10, y1 - 10, 20, y2 - y1 + 20, GREEN, .25)
    x2, y3 = bb.xy(8, "f"); _, y4 = bb.xy(8, "j")
    inner += band(x - 10, y3 - 10, 20, y4 - y3 + 20, GREEN, .25)
    inner += band(24, bb.rails_top["T+"] - 9, bb.W - 48, 18, RED, .2) + band(24, bb.rails_top["T-"] - 9, bb.W - 48, 18, BLUE, .2)
    # CI à cheval sur le canal
    ix1, _ = bb.xy(15, "e"); ix2, _ = bb.xy(18, "e")
    ey = bb.top_rows["e"]; fy = bb.bot_rows["f"]
    inner += f'<g filter="url(#shs)"><rect x="{ix1-9}" y="{ey+6}" width="{ix2-ix1+18}" height="{fy-ey-12}" rx="4" fill="url(#black)"/></g>'
    inner += f'<path d="M{ix1-9},{(ey+fy)/2-5} a5,5 0 0 1 0,10Z" fill="#fff"/>' + T((ix1 + ix2) / 2, (ey + fy) / 2 + 4, "CI", 12, 700, "#cfd5de")
    for c in range(15, 19):
        px, _ = bb.xy(c, "e")
        inner += f'<rect x="{px-2.5}" y="{ey}" width="5" height="9" fill="url(#metalH)"/><rect x="{px-2.5}" y="{fy-9}" width="5" height="9" fill="url(#metalH)"/>'
    s = 1.7
    o = g(40, 60, inner, s)
    ox, oy = 40, 60
    def P(px, py): return ox + px * s, oy + py * s
    cx, cy = P(*bb.xy(8, "a"))
    o += callout(*P(bb.xy(8, "c")[0] + 10, bb.xy(8, "c")[1]), 995, 175, "5 trous reliés\n(colonne a–e)", "start", 18, bold=True)
    o += callout(*P(bb.xy(8, "h")[0] + 10, bb.xy(8, "h")[1]), 995, 330, "demi-colonne f–j\nreliée aussi", "start", 18, bold=True)
    o += callout(*P(bb.W - 60, bb.rails_top["T+"]), 995, 80, "rail « + » : tout\nrelié sur la longueur", "start", 18, bold=True)
    o += callout(*P(300, bb.rails_top["T-"]), 1010, 130, "", "start", 18) if False else ""
    o += callout(*P(bb.W / 2 - 40, 86 + 5 * 16 + 15), 995, 250, "rainure centrale :\nmoitiés séparées", "start", 18, bold=True)
    o += callout(*P(bb.xy(16, "f")[0], bb.xy(16, "f")[1] + 4), 995, 420, "CI à cheval\nsur la rainure", "start", 18, bold=True)
    o += T(40 + bb.W * s / 2, 700, "Rails d'alimentation : horizontaux (rouge « + », bleu « − »)  ·  Colonnes de composants : verticales par 5 trous", 18, 600, MUTED)
    return figure(W, 740, o)


def f_stripboard():
    o = ""
    P = 30
    cols, rows = 24, 8
    bx, by = 50, 125
    bw, bh = cols * P + 50, rows * P + 40
    o += f'<g filter="url(#sh)"><rect x="{bx}" y="{by}" width="{bw}" height="{bh}" rx="10" fill="url(#tan)"/></g>'
    for r in range(rows):
        y = by + 30 + r * P
        o += f'<rect x="{bx+8}" y="{y-11}" width="{bw-16}" height="22" rx="3" fill="url(#copper)"/>'
        o += f'<rect x="{bx+8}" y="{y-11}" width="{bw-16}" height="6" rx="3" fill="#fff" opacity=".18"/>'
        for c in range(cols):
            x = bx + 25 + c * P
            o += f'<circle cx="{x}" cy="{y}" r="6.5" fill="#3a2a1a"/><circle cx="{x}" cy="{y}" r="6.5" fill="none" stroke="#f0c9a0" stroke-width="1.5" opacity=".5"/>'
    # coupure
    cr, cc = 3, 12
    cx, cy = bx + 25 + cc * P, by + 30 + cr * P
    o += f'<rect x="{cx-14}" y="{cy-15}" width="28" height="30" rx="4" fill="url(#tan)"/><circle cx="{cx}" cy="{cy}" r="9" fill="#3a2a1a"/><circle cx="{cx}" cy="{cy}" r="13" fill="none" stroke="#8a6a3a" stroke-width="2"/>'
    ya = by + 30 + cr * P
    o += f'<rect x="{bx+8}" y="{ya-14}" width="{cc*P+8}" height="28" rx="8" fill="{BLUE}" opacity=".18" stroke="{BLUE}" stroke-width="2.5"/>'
    o += f'<rect x="{cx+16}" y="{ya-14}" width="{bw-16-(cx+16-bx)+8}" height="28" rx="8" fill="{AMBER}" opacity=".2" stroke="{AMBER}" stroke-width="2.5"/>'
    o += chip(bx + 150, 100, "zone A", BLUE, size=16) + chip(bx + bw - 150, 100, "zone B", AMBER, size=16)
    o += callout(bx + 12 * 0 + 90, by + 30 + 6 * P + 3, 870, 330, "bande de cuivre continue :\ntous ses trous sont reliés", "start", 18, bold=True)
    o += callout(cx, cy, 870, 210, "coupure de piste (foret Ø 3 mm) :\nzones A et B isolées", "start", 18, bold=True)
    o += callout(bx + 25 + 2 * P, by + 30 + 1 * P, 880, 440, "trous au pas de 2,54 mm", "start", 18, bold=True) if False else ""
    o += T(bx + bw / 2, 56, "Plaque à bandes (vue côté cuivre)", 24, 800, INK)
    o += T(bx + bw / 2, by + bh + 38, "Les bandes sont horizontales ; on les coupe pour isoler des parties du montage.", 18, 600, MUTED)
    return figure(W, by + bh + 70, o)


def solder_card(x, kind):
    cx = x + 190
    o = ""
    # coupe
    o += f'<rect x="{cx-120}" y="150" width="240" height="26" fill="url(#pcb)"/>'
    pads = [(cx - 110, 50), (cx + 60, 50)] if kind != "pont" else [(cx - 110, 70), (cx + 40, 70)]
    leads = [cx] if kind != "pont" else [cx - 55, cx + 55]
    pad_w = 46
    if kind == "pont":
        pads = [(cx - 55 - 40, 80), (cx + 55 - 40, 80)]
        o += ''.join(f'<rect x="{px}" y="176" width="{w}" height="7" fill="url(#copper)"/>' for px, w in pads)
    else:
        o += f'<rect x="{cx-70}" y="176" width="64" height="7" fill="url(#copper)"/><rect x="{cx+6}" y="176" width="64" height="7" fill="url(#copper)"/>'
    for lx in leads:
        o += f'<rect x="{lx-6}" y="95" width="12" height="125" fill="url(#metalH)"/>'
    if kind == "bonne":
        o += f'<path d="M{cx-68},184 Q{cx-24},186 {cx-7},216 L{cx+7},216 Q{cx+24},186 {cx+68},184 Z" fill="url(#solder)"/>'
        o += f'<path d="M{cx-40},186 Q{cx-18},192 {cx-10},206" stroke="#fff" stroke-width="3" fill="none" opacity=".9"/>'
    elif kind == "froide":
        o += f'<ellipse cx="{cx}" cy="204" rx="30" ry="22" fill="url(#solderDull)"/>'
        o += ''.join(f'<circle cx="{cx + dx}" cy="{204 + dy}" r="1.8" fill="#4d4a45"/>' for dx, dy in ((-12, -6), (6, -10), (14, 2), (-4, 8), (-18, 6), (10, 10), (0, -2)))
        o += f'<path d="M{cx-70},184 L{cx-30},184" stroke="{RED}" stroke-width="3" stroke-dasharray="4 4"/>'
    else:
        o += f'<path d="M{cx-100},184 Q{cx-100},230 {cx},230 Q{cx+100},230 {cx+100},184 Z" fill="url(#solder)"/>'
        o += f'<path d="M{cx-60},190 Q{cx},200 {cx+60},190" stroke="#fff" stroke-width="3" fill="none" opacity=".8"/>'
    # vue de dessus
    ty = 335
    if kind == "pont":
        for px in (cx - 55, cx + 55):
            o += f'<circle cx="{px}" cy="{ty}" r="38" fill="url(#copper)"/><circle cx="{px}" cy="{ty}" r="30" fill="url(#solder)"/>'
        o += f'<rect x="{cx-55}" y="{ty-22}" width="110" height="44" rx="20" fill="url(#solder)"/>'
        o += f'<path d="M{cx-60},{ty-10} Q{cx},{ty-18} {cx+60},{ty-10}" stroke="#fff" stroke-width="3" fill="none" opacity=".8"/>'
    elif kind == "bonne":
        o += f'<circle cx="{cx}" cy="{ty}" r="54" fill="url(#copper)"/><circle cx="{cx}" cy="{ty}" r="44" fill="url(#solder)"/><circle cx="{cx}" cy="{ty}" r="12" fill="#9aa4b2" opacity=".8"/>'
        o += f'<path d="M{cx-30},{ty-20} Q{cx-12},{ty-34} {cx+6},{ty-30}" stroke="#fff" stroke-width="5" fill="none" stroke-linecap="round"/>'
    else:
        o += f'<circle cx="{cx}" cy="{ty}" r="54" fill="url(#copper)"/><path d="M{cx-26},{ty-6} Q{cx-24},{ty-30} {cx+4},{ty-27} Q{cx+30},{ty-20} {cx+27},{ty+8} Q{cx+22},{ty+30} {cx-6},{ty+27} Q{cx-30},{ty+20} {cx-26},{ty-6}Z" fill="url(#solderDull)"/>'
        o += ''.join(f'<circle cx="{cx + dx}" cy="{ty + dy}" r="1.8" fill="#4d4a45"/>' for dx, dy in ((-12, -10), (8, -14), (16, 2), (-6, 12), (-18, 4), (10, 14), (2, -2)))
    return o


def f_soudures():
    o = ""
    spec = [("Soudure correcte", GREEN, "bonne", "brillante, lisse\nforme de cône concave", "✔ à conserver"),
            ("Soudure froide", RED, "froide", "terne, granuleuse, en boule\nne mouille pas la pastille", "✘ à refaire"),
            ("Pont d'étain", RED, "pont", "l'étain relie deux pastilles\n= court-circuit", "✘ à retirer")]
    for i, (t, col, k, d, v) in enumerate(spec):
        x = 30 + i * 390
        o += panel(x, 40, 360, 540, t, accent=col)
        o += T(x + 24, 118, "Coupe", 16, 700, MUTED, "start") + T(x + 24, 275, "Vue de dessus", 16, 700, MUTED, "start")
        o += solder_card(x, k)
        o += T(x + 180, 450, d, 18, 600, INK)
        o += chip(x + 180, 520, v, col, size=19)
    return figure(W, 620, o)


FIGS = {
    "schema_vs_montage": f_schema_vs_montage, "symboles_de_base": f_symboles, "croisement_jonction": f_jonction,
    "schema_de_bloc": f_schema_bloc, "polarites": f_polarites, "methode_lecture_schema": f_methode,
    "breadboard": f_breadboard, "stripboard": f_stripboard, "soudures": f_soudures,
}
