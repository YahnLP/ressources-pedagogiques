"""Maquettes de logiciels et figures complémentaires (Première / Terminale)."""
from lib import *
from figs07 import block
from figs_prem import chain

W = 1200
MONO = 'font-family="DejaVu Sans Mono, monospace"'


def win(x, y, w, h, title, dark=False, bar="#e9ecf3"):
    c = "#1e2127" if dark else "#f3f4f8"
    o = f'<g filter="url(#sh)"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{c}" stroke="#aab3c5" stroke-width="2"/></g>'
    o += f'<rect x="{x}" y="{y}" width="{w}" height="34" rx="10" fill="{"#2c313a" if dark else bar}"/><rect x="{x}" y="{y+20}" width="{w}" height="14" fill="{"#2c313a" if dark else bar}"/>'
    o += ''.join(f'<circle cx="{x+20+i*20}" cy="{y+17}" r="6" fill="{c_}"/>' for i, c_ in enumerate(("#ff5f57", "#febc2e", "#28c840")))
    return o + T(x + w / 2, y + 23, title, 15, 700, "#cfd5e2" if dark else INK)


def icon(x, y, kind, s=34, fg=INK, bg="#fff"):
    o = f'<rect x="{x}" y="{y}" width="{s}" height="{s}" rx="5" fill="{bg}" stroke="#b9c2d4" stroke-width="1.5"/>'
    cx, cy = x + s / 2, y + s / 2
    if kind == "arrow": o += f'<path d="M{cx-6},{cy-9} L{cx+8},{cy+3} L{cx+1},{cy+4} L{cx+4},{cy+11} L{cx},{cy+12} L{cx-3},{cy+5} L{cx-8},{cy+9}Z" fill="{fg}"/>'
    elif kind == "wire": o += f'<path d="M{cx-10},{cy+8} L{cx-10},{cy-6} L{cx+10},{cy-6}" stroke="#1f9d4a" stroke-width="3" fill="none"/>'
    elif kind == "bus": o += f'<path d="M{cx-11},{cy+7} L{cx+11},{cy-7}" stroke="#1d5fd1" stroke-width="5"/>'
    elif kind == "label": o += T(cx, cy + 6, "A", 17, 800, fg)
    elif kind == "power": o += f'<path d="M{cx},{cy+9} V{cy-6} M{cx-8},{cy-6} H{cx+8}" stroke="{fg}" stroke-width="2.5"/>'
    elif kind == "symbol": o += f'<path d="M{cx-7},{cy-9} L{cx+8},{cy} L{cx-7},{cy+9}Z" fill="none" stroke="{fg}" stroke-width="2.5"/>'
    elif kind == "text": o += T(cx, cy + 7, "T", 19, 700, fg)
    elif kind == "erc": o += f'<path d="M{cx},{cy-10} L{cx+9},{cy-6} V{cy+3} Q{cx+9},{cy+9} {cx},{cy+12} Q{cx-9},{cy+9} {cx-9},{cy+3} V{cy-6}Z" fill="none" stroke="#c0392b" stroke-width="2"/><path d="M{cx-4},{cy+1} L{cx-1},{cy+5} L{cx+5},{cy-3}" stroke="#1f9d4a" stroke-width="2.5" fill="none"/>'
    return o


def grid(x, y, w, h, step=22, col="#c9cfdc"):
    return ''.join(f'<circle cx="{xx}" cy="{yy}" r="1.3" fill="{col}"/>' for xx in range(int(x), int(x + w), step) for yy in range(int(y), int(y + h), step))


def f_kicad_editor():
    o = win(30, 30, 860, 580, "Éditeur de schéma — projet.kicad_sch")
    o += f'<rect x="30" y="64" width="860" height="26" fill="#e3e6ee"/>' + "".join(T(60 + i * 105, 83, m, 14, 600, INK, "start") for i, m in enumerate(("Fichier", "Édition", "Affichage", "Placer", "Inspecter", "Outils", "Aide")))
    o += "".join(f'<rect x="{44+i*34}" y="96" width="26" height="26" rx="4" fill="#fff" stroke="#b9c2d4"/>' for i in range(12))
    o += f'<rect x="70" y="132" width="730" height="426" fill="#fdfcf3" stroke="#9aa4b8" stroke-width="2"/>' + grid(76, 138, 720, 416) + f'<rect x="110" y="165" width="650" height="360" fill="none" stroke="#a33" stroke-width="2"/>'
    o += T(435, 345, "Zone de dessin (grille visible)", 20, 600, "#9aa4b8")
    o += "".join(icon(44, 150 + i * 44, k) for i, k in enumerate(("arrow", "wire", "bus", "label")) if False)
    names = ["Outil de sélection", "Fil", "Bus", "Étiquette (label)", "Symbole d'alimentation", "Ajouter un symbole", "Texte", "Contrôle des règles (ERC)"]
    kinds = ["arrow", "wire", "bus", "label", "power", "symbol", "text", "erc"]
    for i, (k, nm) in enumerate(zip(kinds, names)):
        y = 140 + i * 50
        o += icon(822, y, k) + badge(868, y + 6, i + 1, BLUE, 12) + T(930, y + 24, f"{i+1}  {nm}", 16, 700, INK, "start")
    o += f'<rect x="30" y="570" width="860" height="40" fill="#e3e6ee"/>' + T(50, 596, "X 0,00  Y 0,00 mm", 14, 700, MUTED, "start") + T(450, 596, "Grille : 1,27 mm", 14, 700, MUTED) + T(860, 596, "Zoom 100 %", 14, 700, MUTED, "end")
    o += T(1040, 70, "Barre d'outils de droite", 17, 800, BLUE)
    return figure(W, 640, o)


def f_kicad_led():
    o = f'<g filter="url(#sh)"><rect x="40" y="30" width="1120" height="500" rx="10" fill="#14161a"/></g>' + grid(60, 50, 1080, 460, 24, "#2b3038")
    G, Y = "#3ecf5e", "#f0d36a"
    o += f'<path d="M330,160 V220 M330,300 V350 M330,430 V470" stroke="{G}" stroke-width="3"/>'
    o += f'<path d="M330,100 V160 M312,100 H348" stroke="{Y}" stroke-width="3"/>' + T(330, 85, "+5V", 20, 700, Y)
    o += f'<rect x="312" y="220" width="36" height="80" fill="none" stroke="{Y}" stroke-width="3"/>' + T(375, 255, "R1", 20, 700, "#f08a6a", "start") + T(375, 282, "150Ω", 18, 600, "#f08a6a", "start")
    o += f'<path d="M312,350 H348 M330,350 L330,350" stroke="{Y}" stroke-width="3"/><path d="M312,350 L348,350 L330,382 Z" fill="none" stroke="{Y}" stroke-width="3"/><path d="M312,382 H348" stroke="{Y}" stroke-width="3"/>'
    o += f'<path d="M352,358 L372,340 M360,372 L380,354" stroke="{Y}" stroke-width="2.5" marker-end="url(#arr)"/>' + T(400, 372, "D1", 20, 700, "#f08a6a", "start")
    o += f'<path d="M330,382 V430" stroke="{G}" stroke-width="3"/><path d="M330,470 V480 M308,480 H352 M318,490 H342 M326,500 H334" stroke="{Y}" stroke-width="3"/>' + T(330, 520, "GND", 18, 700, Y)
    for (x, y, t, c, ax, ay) in ((560, 215, "R1 · pin 1 (haut)", "#4fc3f7", 330, 225), (560, 300, "R1 · pin 2 (bas)", "#4fc3f7", 330, 297), (560, 355, "D1 · A (anode)", "#ff8a65", 336, 352), (560, 400, "D1 · K (cathode)", "#ff8a65", 336, 382)):
        o += f'<path d="M{x-8},{y+4} L{ax+22},{ay}" stroke="{c}" stroke-width="2.5" marker-end="url(#arr)"/>' + T(x, y + 10, t, 18, 700, c, "start")
    o += chip(850, 120, "fil (vert)", "#2e8b4a", w=130, size=15) + chip(850, 170, "symbole d'alimentation", "#b0902a", w=240, size=15)
    return figure(W, 560, o)


def f_kicad_drc():
    o = win(30, 30, 520, 470, "Contrôle des règles de conception (DRC)", dark=True)
    rows = [("✖", RED, "Violation de clearance", "Piste F.Cu ↔ Piste F.Cu : 0,10 mm < 0,20 mm"), ("⚠", AMBER, "Éléments non connectés", "Pad R1-2 ↔ pad Q1-B (ratsnest)"), ("✖", "#ff9d3c", "Chevauchement de courtyard", "R2 et D1 se recouvrent")]
    for i, (ic, c, t, d) in enumerate(rows):
        y = 90 + i * 110; o += f'<rect x="50" y="{y}" width="480" height="92" rx="8" fill="#2a2f39"/>' + T(75, y + 40, ic, 28, 800, c) + T(110, y + 36, t, 19, 800, "#e8ecf4", "start") + T(110, y + 66, d, 15, 600, "#9fb0d0", "start")
    o += T(290, 450, "3 erreurs · 0 avertissement ignoré", 15, 700, "#9fb0d0")
    o += f'<g filter="url(#sh)"><rect x="590" y="30" width="580" height="470" rx="10" fill="#101214"/></g>'
    o += f'<path d="M640,150 H900" stroke="{RED}" stroke-width="10"/><path d="M640,172 H900" stroke="{RED}" stroke-width="10"/>' + f'<path d="M770,100 V135 M770,215 V180" stroke="{RED}" stroke-width="3" marker-end="url(#arr)"/>' + chip(770, 90, "clearance", RED, w=130, size=14)
    o += f'<circle cx="680" cy="300" r="22" fill="#d9a441"/><circle cx="880" cy="380" r="22" fill="#d9a441"/><path d="M680,300 L880,380" stroke="#f0d36a" stroke-width="3" stroke-dasharray="8 6"/>' + chip(780, 330, "non connecté", AMBER, w=150, size=14)
    o += f'<rect x="990" y="260" width="120" height="70" fill="#ff9d3c" opacity=".5" stroke="#ff9d3c" stroke-width="3"/><rect x="1040" y="300" width="100" height="70" fill="#ff9d3c" opacity=".5" stroke="#ff9d3c" stroke-width="3"/>' + chip(1070, 400, "courtyard", "#ff9d3c", w=130, size=14)
    return figure(W, 530, o)


def f_kicad_3d():
    o = f'<rect x="40" y="30" width="1120" height="470" rx="12" fill="url(#bg3d)"/><defs><linearGradient id="bg3d" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#9fb4d4"/><stop offset="1" stop-color="#e6edf7"/></linearGradient><linearGradient id="rbody" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f4e7c3"/><stop offset=".55" stop-color="#e2cb93"/><stop offset="1" stop-color="#b79d62"/></linearGradient></defs>'
    # carte (dessus + tranches)
    o += '<polygon points="300,300 760,260 960,360 480,420" fill="#1c7a46" stroke="#0e4a2a" stroke-width="3"/><polygon points="300,300 480,420 480,436 300,316" fill="#115c33"/><polygon points="480,420 960,360 960,376 480,436" fill="#0e4a2a"/>'
    # pistes (cuivre sous masque) et pastilles
    o += '<g opacity=".55"><path d="M440,332 L520,360 L560,372" stroke="#8fd19e" stroke-width="3" fill="none"/><path d="M560,372 L640,345 L690,330" stroke="#8fd19e" stroke-width="3" fill="none"/></g>'
    def hole(x, y): return f'<ellipse cx="{x}" cy="{y}" rx="7" ry="3.6" fill="#d9a441" stroke="#8a6a1c" stroke-width="1"/><ellipse cx="{x}" cy="{y}" rx="3" ry="1.5" fill="#0b2d1a"/>'
    def resistor(cx, cy, ang, c1, c2, c3):
        """résistance traversante : corps cylindrique + 2 pattes plongeant dans les trous"""
        import math as m
        dx, dy = m.cos(m.radians(ang)), m.sin(m.radians(ang))
        L = 62; lift = 22
        x1, y1, x2, y2 = cx - dx * L, cy - dy * L, cx + dx * L, cy + dy * L
        r = hole(x1, y1) + hole(x2, y2)
        r += f'<path d="M{x1},{y1} V{y1-lift} H{x1+dx*24} M{x2},{y2} V{y2-lift} H{x2-dx*24}" stroke="#c9cfd8" stroke-width="3" fill="none" stroke-linejoin="round"/>'
        r += f'<g transform="translate({cx},{cy-lift}) rotate({ang})"><rect x="-38" y="-9" width="76" height="18" rx="9" fill="url(#rbody)" stroke="#7a6a45" stroke-width="1.6"/>'
        for bx, col in ((-20, c1), (-8, c2), (4, c3)): r += f'<rect x="{bx}" y="-9" width="6" height="18" fill="{col}"/>'
        r += '<rect x="24" y="-9" width="5" height="18" fill="#c9a227"/></g>'
        return r
    o += resistor(470, 345, -4, "#7a4320", "#000", "#d32f2f") + resistor(560, 392, -4, "#d32f2f", "#d32f2f", "#7a4320")
    # transistor TO-92 (pattes dans la carte)
    o += g(690, 318, '<path d="M-30,0 L-30,-30 Q-30,-56 0,-56 Q30,-56 30,-30 L30,0 Z" fill="url(#black)"/><rect x="-22" y="0" width="5" height="16" fill="#c9cfd8"/><rect x="-2" y="0" width="5" height="16" fill="#c9cfd8"/><rect x="18" y="0" width="5" height="16" fill="#c9cfd8"/>', 1.1)
    o += hole(668, 337) + hole(691, 337) + hole(713, 337)
    # LED rouge
    o += g(800, 322, '<path d="M-26,0 L-26,-26 A26,26 0 0 1 26,-26 L26,0 Z" fill="#e5353b"/><rect x="-32" y="-4" width="64" height="8" fill="#c22"/><rect x="-14" y="4" width="3" height="12" fill="#c9cfd8"/><rect x="11" y="4" width="3" height="12" fill="#c9cfd8"/>', 1.0)
    # connecteur 4 broches (barrette sécable)
    o += '<polygon points="842,318 928,318 932,333 846,333" fill="#2a2d33"/><polygon points="846,333 932,333 932,345 846,345" fill="#15171b"/>' + "".join(f'<rect x="{854+i*19}" y="{300}" width="5" height="19" fill="#d9a441"/>' for i in range(4))
    # sérigraphie
    o += T(445, 372, "R1", 14, 800, "#e8f5ec") + T(537, 418, "R2", 14, 800, "#e8f5ec") + T(690, 358, "Q1", 14, 800, "#e8f5ec") + T(800, 350, "D1", 14, 800, "#e8f5ec") + T(890, 362, "J1", 14, 800, "#e8f5ec")
    # légendes
    o += callout(470, 328, 150, 150, "Résistances traversantes", "start", 17, bold=True) + callout(690, 262, 940, 130, "Transistor BC547", "start", 17, bold=True) + callout(800, 296, 940, 190, "LED rouge", "start", 17, bold=True) + callout(890, 312, 940, 250, "Connecteur", "start", 17, bold=True)
    o += chip(600, 470, "Vue 3D : masque vert, sérigraphie blanche", INK, w=520, size=16)
    return figure(W, 530, o)


def f_kicad_gerber():
    o = win(30, 30, 640, 470, "Tracer — Fichiers Gerber")
    o += T(60, 85, "Calques à tracer", 17, 800, INK, "start")
    for i, l in enumerate(("F.Cu", "B.Cu", "F.Mask", "B.Mask", "F.Silkscreen", "B.Silkscreen", "Edge.Cuts")):
        y = 105 + i * 33; o += f'<rect x="60" y="{y}" width="20" height="20" rx="3" fill="#fff" stroke="#6b7480" stroke-width="2"/>' + T(70, y + 16, "✓", 16, 800, GREEN) + T(95, y + 16, l, 16, 700, INK, "start")
    o += T(360, 85, "Options", 17, 800, INK, "start")
    for i, l in enumerate(("Extensions Protel", "Générer le fichier de travail", "Inclure le texte du cadre")):
        y = 105 + i * 36; o += f'<rect x="360" y="{y}" width="20" height="20" rx="3" fill="#fff" stroke="#6b7480" stroke-width="2"/>' + (T(370, y + 16, "✓", 16, 800, GREEN) if i < 2 else "") + T(390, y + 16, l, 15, 700, INK, "start")
    o += f'<rect x="440" y="430" width="200" height="44" rx="8" fill="{BLUE}"/>' + T(540, 459, "Tracer", 19, 800, "#fff") + f'<rect x="60" y="430" width="180" height="44" rx="8" fill="#e3e6ee" stroke="#b9c2d4"/>' + T(150, 459, "Fermer", 17, 700, INK)
    o += win(710, 30, 460, 470, "Explorateur de fichiers")
    files = [("projet-F_Cu.gtl", "cuivre face"), ("projet-B_Cu.gbl", "cuivre dessous"), ("projet-F_Mask.gts", "masque face"), ("projet-B_Mask.gbs", "masque dessous"), ("projet-F_Silkscreen.gto", "sérigraphie face"), ("projet-B_Silkscreen.gbo", "sérigraphie dessous"), ("projet-Edge_Cuts.gm1", "contour"), ("projet.drl", "perçages")]
    for i, (f, d) in enumerate(files):
        y = 84 + i * 48; o += f'<rect x="730" y="{y}" width="26" height="30" rx="3" fill="#dfe6f5" stroke="#8d9bb8"/>' + T(768, y + 16, f, 15, 700, INK, "start", extra=MONO) + T(768, y + 34, d, 13, 600, MUTED, "start")
    return figure(W, 530, o)


def nr(x, y, label, col, w=170, ins=True, outs=True):
    o = f'<rect x="{x}" y="{y}" width="{w}" height="36" rx="6" fill="{col}" stroke="#00000033" stroke-width="2"/><rect x="{x}" y="{y}" width="30" height="36" rx="6" fill="#00000022"/>' + T(x + 36 + (w - 36) / 2, y + 24, label, 15, 700, "#1b2742")
    if ins: o += f'<rect x="{x-5}" y="{y+13}" width="10" height="10" rx="2" fill="#fff" stroke="#888"/>'
    if outs: o += f'<rect x="{x+w-5}" y="{y+13}" width="10" height="10" rx="2" fill="#fff" stroke="#888"/>'
    return o


def wire_(x1, y1, x2, y2):
    mx = (x1 + x2) / 2
    return f'<path d="M{x1},{y1} C{mx},{y1} {mx},{y2} {x2},{y2}" fill="none" stroke="#999" stroke-width="3"/>'


def nr_frame(title, h):
    o = f'<g filter="url(#sh)"><rect x="30" y="20" width="1140" height="{h}" rx="10" fill="#fff" stroke="#c4c4c4" stroke-width="2"/></g><rect x="30" y="20" width="1140" height="48" rx="10" fill="#8f0000"/><rect x="30" y="48" width="1140" height="20" fill="#8f0000"/>'
    o += T(60, 52, "Node-RED", 20, 800, "#fff", "start") + T(300, 52, title, 15, 700, "#f3d5d5", "start") + f'<rect x="1040" y="30" width="110" height="30" rx="5" fill="#c62828"/>' + T(1095, 51, "Déployer", 15, 800, "#fff")
    o += f'<rect x="30" y="68" width="170" height="{h-48}" fill="#f3f3f3"/>' + f'<rect x="990" y="68" width="180" height="{h-48}" fill="#f7f7f7"/>' + f'<rect x="200" y="68" width="790" height="{h-48}" fill="#fcfcfc"/>' + grid(206, 76, 780, h - 70, 20, "#dcdcdc")
    for i, (c, n) in enumerate((("#a6bbcf", "entrée"), ("#fdd0a2", "fonction"), ("#e2d96e", "dashboard"), ("#87a980", "sortie"))): o += f'<rect x="44" y="{86+i*40}" width="140" height="28" rx="5" fill="{c}"/>' + T(114, 105 + i * 40, n, 14, 700, "#333")
    o += T(1080, 96, "debug", 15, 800, "#333") + "".join(f'<rect x="1002" y="{116+i*30}" width="156" height="22" rx="3" fill="#eee"/>' for i in range(4))
    return o


def f_nr_simple():
    o = nr_frame("Flux 1", 480)
    xs = [(230, 150, "inject", "#a6bbcf"), (420, 110, "Simuler données", "#fdd0a2")]
    o += nr(230, 200, "inject", "#a6bbcf", 130, ins=False) + nr(420, 200, "Simuler données", "#fdd0a2", 180) + nr(690, 130, "gauge", "#e2d96e", 130, outs=False) + nr(690, 200, "chart", "#e2d96e", 130, outs=False) + nr(690, 270, "debug", "#87a980", 130, outs=False)
    o += wire_(360, 218, 420, 218) + wire_(600, 218, 690, 148) + wire_(600, 218, 690, 218) + wire_(600, 218, 690, 288)
    o += callout(295, 236, 295, 340, "déclenchement manuel", "middle", 15, bold=True) + callout(510, 236, 510, 340, "génère une température simulée", "middle", 15, bold=True) + callout(755, 305, 800, 380, "affichage dashboard / console", "middle", 15, bold=True)
    return figure(W, 530, o)


def f_nr_dashboard():
    o = f'<g filter="url(#sh)"><rect x="40" y="20" width="1120" height="440" rx="10" fill="#f4f5f7" stroke="#c4c4c4" stroke-width="2"/></g><rect x="40" y="20" width="1120" height="52" rx="10" fill="#0094ce"/><rect x="40" y="50" width="1120" height="22" fill="#0094ce"/>' + T(70, 54, "Salle E2", 20, 800, "#fff", "start") + T(170, 54, "http://localhost:1880/ui", 14, 600, "#dff3fb", "start")
    cx, cy, r = 330, 300, 150
    def arc(a0, a1, c): 
        import math as m
        x0, y0, x1, y1 = cx + r * m.cos(m.radians(a0)), cy - r * m.sin(m.radians(a0)), cx + r * m.cos(m.radians(a1)), cy - r * m.sin(m.radians(a1)); return f'<path d="M{x0:.0f},{y0:.0f} A{r},{r} 0 0 1 {x1:.0f},{y1:.0f}" fill="none" stroke="{c}" stroke-width="30"/>'
    o += f'<rect x="80" y="100" width="500" height="330" rx="10" fill="#fff" stroke="#dcdcdc"/>' + arc(180, 90, GREEN) + arc(90, 36, AMBER) + arc(36, 0, RED)
    import math as m
    ang = 180 - 24.3 / 50 * 180; o += f'<line x1="{cx}" y1="{cy}" x2="{cx+(r-20)*m.cos(m.radians(ang)):.0f}" y2="{cy-(r-20)*m.sin(m.radians(ang)):.0f}" stroke="{INK}" stroke-width="6" stroke-linecap="round"/><circle cx="{cx}" cy="{cy}" r="12" fill="{INK}"/>'
    o += T(cx, cy + 50, "24,3 °C", 34, 800, INK) + T(cx - r, cy + 28, "0", 14, 700, MUTED) + T(cx + r, cy + 28, "50", 14, 700, MUTED) + T(cx, 135, "Température", 18, 800, INK)
    o += f'<rect x="620" y="100" width="500" height="330" rx="10" fill="#fff" stroke="#dcdcdc"/>' + T(870, 135, "Évolution de la température", 18, 800, INK) + f'<polyline points="{" ".join(f"{650+i*8},{330-60*math.sin(i/9)-i*0.9:.0f}" for i in range(55))}" fill="none" stroke="#1f77b4" stroke-width="4"/>'
    o += f'<line x1="650" y1="380" x2="1090" y2="380" stroke="{INK}" stroke-width="2"/><line x1="650" y1="160" x2="650" y2="380" stroke="{INK}" stroke-width="2"/>' + T(1090, 405, "temps", 14, 700, MUTED, "end")
    return figure(W, 480, o)


def f_nr_complet():
    o = nr_frame("Flux IoT complet", 560)
    o += nr(220, 110, "mqtt in", "#d8bfd8", 120, ins=False) + nr(380, 110, "json", "#e7e7ae", 90) + nr(510, 110, "Parser JSON", "#fdd0a2", 150) + nr(720, 80, "gauge", "#e2d96e", 110, outs=False) + nr(720, 125, "chart", "#e2d96e", 110, outs=False) + nr(720, 170, "influxdb out", "#d8bfd8", 110, outs=False)
    o += wire_(340, 128, 380, 128) + wire_(470, 128, 510, 128) + wire_(660, 128, 720, 98) + wire_(660, 128, 720, 143) + wire_(660, 128, 720, 188)
    o += T(220, 85, "1 · Acquisition temps réel", 15, 800, "#8f0000", "start")
    o += nr(510, 290, "Parser JSON", "#fdd0a2", 150, ins=True) + nr(700, 290, "switch temp>30", "#e2d96e", 160) + nr(900, 260, "debug « ALERTE »", "#87a980", 80, outs=False) if False else ""
    o += nr(380, 290, "Parser JSON", "#fdd0a2", 140) + nr(560, 290, "switch temp > 30", "#e2d96e", 170) + nr(770, 262, "debug « ALERTE »", "#87a980", 170, outs=False) + nr(770, 320, "mqtt out « alerte »", "#d8bfd8", 170, outs=False)
    o += wire_(520, 308, 560, 308) + wire_(730, 308, 770, 280) + wire_(730, 308, 770, 338) + T(220, 265, "2 · Alertes", 15, 800, "#8f0000", "start")
    o += nr(220, 450, "inject", "#a6bbcf", 110, ins=False) + nr(360, 450, "Requête Flux", "#fdd0a2", 150) + nr(540, 450, "influxdb in", "#d8bfd8", 140) + nr(720, 450, "chart historique", "#e2d96e", 170, outs=False)
    o += wire_(330, 468, 360, 468) + wire_(510, 468, 540, 468) + wire_(680, 468, 720, 468) + T(220, 425, "3 · Historique", 15, 800, "#8f0000", "start")
    return figure(W, 610, o)


def f_deca():
    o = ""
    st = [("D", "Décrire", "tous les symptômes", 1000, BLUE), ("E", "Éliminer", "les hypothèses improbables", 800, AMBER), ("C", "Cibler", "la cause racine", 620, "#c9a400"), ("A", "Agir", "corriger et valider", 460, GREEN)]
    for i, (l, t, s, w, c) in enumerate(st):
        y = 50 + i * 100
        o += f'<path d="M{600-w/2},{y} L{600+w/2},{y} L{600+(w-80)/2},{y+88} L{600-(w-80)/2},{y+88} Z" fill="{c}"/>' + T(600, y + 42, f"{l} — {t}", 28, 800, "#fff") + T(600, y + 70, s, 17, 600, "#fff")
    o += chip(600, 482, "chaque étape réduit le champ des possibles : diagnostic en O(log n) mesures", INK, w=820, size=16)
    return figure(W, 530, o)


def f_logigramme():
    o = block(450, 20, 300, 70, "ESP32 ne publie plus", None, RED)
    o += s_wire([(600, 90), (600, 115)], INK, 4) + f'<path d="M600,115 L760,165 L600,215 L440,165 Z" fill="#fff4dc" stroke="{AMBER}" stroke-width="4"/>' + T(600, 160, "Wi-Fi connecté ?", 17, 800, INK) + T(600, 182, "WiFi.status()", 13, 600, MUTED, extra=MONO)
    o += s_wire([(440, 165), (250, 165)], INK, 4) + T(345, 150, "non", 15, 800, RED) + block(30, 130, 220, 70, "Problème Wi-Fi", "SSID, mot de passe", RED)
    o += s_wire([(600, 215), (600, 250)], INK, 4) + T(618, 238, "oui", 15, 800, GREEN) + block(450, 250, 300, 70, "Lire mqtt.state()", "premier indicateur à lire", BLUE)
    for i, (x, t, s, c) in enumerate(((40, "−4 · −2 · −1", "broker injoignable : IP, port", RED), (330, "1 à 3", "protocole / identifiant client", AMBER), (620, "4 · 5", "identifiants / droits refusés", AMBER), (910, "0 : connecté", "vérifier topic et payload", GREEN))):
        o += s_wire([(600, 320), (600, 350), (x + 130, 350), (x + 130, 375)], INK, 3) + block(x, 375, 260, 90, t, s, c)
    return figure(W, 500, o)


def f_chaine_iot():
    items = [("ESP32 + DHT22", "mesure T° et humidité"), ("JSON", "formate les données"), ("Topic", "maison/salon/data"), ("Broker Mosquitto", "local")]
    o = chain(items, y=60, h=110, w=230, gap=70, col=[BLUE, AMBER, AMBER, GREEN])
    x = 40 + 3 * 300 + 115 - 60
    o += s_wire([(x, 170), (x, 215)], INK, 4) + s_wire([(770, 215), (1050, 215)], INK, 4) + arrow(770, 215, 770, 245, INK, 4) + arrow(1050, 215, 1050, 245, INK, 4)
    o += block(640, 250, 260, 90, "mosquitto_sub", "terminal CLI : débogage", INK) + block(920, 250, 260, 90, "Node-RED", "affichage / dashboard", GREEN)
    return figure(W, 380, o)


def f_cablage_pro():
    o = block(60, 50, 250, 340, "", None, BLUE) + T(185, 90, "ESP32 DevKit", 20, 800, INK) + block(900, 50, 240, 150, "", None, GREEN) + T(1020, 90, "DHT22", 20, 800, INK) + block(900, 240, 240, 150, "", None, RED) + T(1020, 280, "LED + R", 20, 800, INK)
    wires = [("ESP32-DHT22-VCC", 3.3, 120, RED, "W01"), ("ESP32-DHT22-DATA", 4, 160, "#e8c53a", "W02"), ("ESP32-DHT22-GND", 0, 200, "#222", "W03"), ("ESP32-LED-ANODE", 2, 290, "#2f5bea", "W04"), ("ESP32-LED-GND", 0, 340, "#222", "W05")]
    pins = ["3V3", "GPIO4", "GND", "GPIO2", "GND"]
    for (nm, _, y, c, w), pn in zip(wires, pins):
        yy = y + 20 if y < 250 else y
        o += T(300, y + 6, pn, 14, 800, INK, "end") + s_wire([(310, y), (900, y if y < 250 else y)], c, 5) + T(600, y - 8, f"{nm} · {w}", 13, 700, INK)
    o += f'<rect x="760" y="420" width="400" height="130" fill="#fff" stroke="{INK}" stroke-width="3"/>' + f'<line x1="760" y1="460" x2="1160" y2="460" stroke="{INK}" stroke-width="2"/><line x1="960" y1="460" x2="960" y2="550" stroke="{INK}" stroke-width="2"/>'
    o += T(960, 448, "CARTOUCHE", 15, 800, INK) + T(776, 486, "Titre : Station IoT", 14, 700, INK, "start") + T(776, 512, "Auteur : ___________", 14, 600, MUTED, "start") + T(976, 486, "Date : ___/___/___", 14, 700, INK, "start") + T(976, 512, "Version : 1.0", 14, 600, MUTED, "start")
    o += T(60, 430, "Chaque fil est identifié à ses deux extrémités : Source-Destination-Numéro", 16, 700, INK, "start") + T(60, 458, "Couleurs des conducteurs : IEC 60446", 15, 600, MUTED, "start")
    return figure(W, 580, o)


def f_dat():
    o = panel(30, 30, 560, 440, "DAT amateur", accent=RED) + panel(610, 30, 560, 440, "DAT professionnel", accent=GREEN)
    for i, t in enumerate(("photo floue du montage", "aucune référence des composants", "pas de nomenclature (BOM)", "pas de version ni de date", "il faut appeler l'auteur")): o += T(70, 120 + i * 62, "✗  " + t, 20, 700, INK, "start") + f'<line x1="60" y1="{140+i*62}" x2="570" y2="{140+i*62}" stroke="#eee" stroke-width="2"/>'
    for i, t in enumerate(("schéma normalisé et référencé", "nomenclature (BOM) complète", "procédures d'installation et de test", "version, date, auteur, signatures", "un technicien peut agir seul")): o += T(650, 120 + i * 62, "✓  " + t, 20, 700, INK, "start") + f'<line x1="640" y1="{140+i*62}" x2="1150" y2="{140+i*62}" stroke="#eee" stroke-width="2"/>'
    return figure(W, 500, o)


def f_cloudwatch():
    o = f'<g filter="url(#sh)"><rect x="40" y="20" width="1120" height="440" rx="10" fill="#f2f3f3" stroke="#c4c8cc" stroke-width="2"/></g><rect x="40" y="20" width="1120" height="50" rx="10" fill="#232f3e"/><rect x="40" y="48" width="1120" height="22" fill="#232f3e"/>' + T(70, 53, "Tableau de bord CloudWatch — IoT-ESP32", 19, 800, "#fff", "start")
    o += f'<rect x="70" y="100" width="680" height="330" rx="6" fill="#fff" stroke="#d5dbdb"/>' + T(100, 130, "Température (°C) — 30 dernières minutes", 17, 800, INK, "start")
    pts = " ".join(f"{110+i*10:.0f},{360-50*math.sin(i/7)-i*1.2:.0f}" for i in range(61))
    o += f'<line x1="110" y1="390" x2="720" y2="390" stroke="{INK}" stroke-width="2"/><line x1="110" y1="150" x2="110" y2="390" stroke="{INK}" stroke-width="2"/><polyline points="{pts}" fill="none" stroke="#ec7211" stroke-width="4"/>'
    o += f'<rect x="780" y="100" width="350" height="330" rx="6" fill="#fff" stroke="#d5dbdb"/>' + T(955, 130, "Valeur instantanée", 17, 800, INK) + f'<path d="M850,350 A105,105 0 0 1 1060,350" fill="none" stroke="#d5dbdb" stroke-width="26"/><path d="M850,350 A105,105 0 0 1 984,252" fill="none" stroke="#1d8102" stroke-width="26"/>' + T(955, 340, "24,3 °C", 32, 800, INK) + T(955, 400, "ESP32 → MQTT TLS → AWS IoT Core → IoT Rule → CloudWatch", 12, 600, MUTED)
    return figure(W, 480, o)


def f_eeschema():
    o = f'<g filter="url(#sh)"><rect x="40" y="20" width="1120" height="470" rx="10" fill="#fdfcf3" stroke="#9aa4b8" stroke-width="2"/></g>' + grid(60, 40, 1080, 430)
    Gc, Rc = "#1f9d4a", "#a33"
    o += f'<path d="M300,120 V180 M300,260 V300 M300,340 V360 H410" fill="none" stroke="{Gc}" stroke-width="4"/>'
    o += f'<rect x="282" y="180" width="36" height="80" fill="none" stroke="{Rc}" stroke-width="3"/>' + T(335, 222, "R1  150Ω", 17, 700, "#7a2a2a", "start")
    o += f'<path d="M280,300 H320 L300,336 Z M280,340 H320" fill="none" stroke="{Rc}" stroke-width="3"/><path d="M324,308 L344,290 M332,324 L352,306" stroke="{Rc}" stroke-width="2.5" marker-end="url(#arr)"/>' + T(365, 332, "D1", 17, 700, "#7a2a2a", "start")
    o += f'<path d="M300,60 V120 M282,60 H318" stroke="{Rc}" stroke-width="3"/>' + T(300, 48, "VCC", 17, 800, "#1d5fd1") + f'<path d="M410,360 V400 M388,400 H432 M398,410 H422" stroke="{Rc}" stroke-width="3"/>' + T(410, 440, "GND", 17, 800, "#1d5fd1")
    o += callout(300, 90, 700, 90, "VCC : nœud global", "start", 17, bold=True) + callout(410, 405, 700, 400, "GND : nœud global", "start", 17, bold=True) + callout(410, 360, 700, 300, "fils verts (connexions)", "start", 17, bold=True)
    o += chip(900, 450, "même nom = même nœud, même sans fil", INK, w=470, size=15)
    return figure(W, 520, o)


def f_pwrflag():
    o = ""
    for k, (t, c, ok) in enumerate((("Sans PWR_FLAG", RED, False), ("Avec PWR_FLAG", GREEN, True))):
        px = 30 + k * 590; o += panel(px, 30, 560, 420, t, accent=c) + f'<rect x="{px+30}" y="90" width="500" height="260" rx="6" fill="#fdfcf3" stroke="#9aa4b8"/>'
        x = px + 280
        o += f'<path d="M{x},130 V200" stroke="#1f9d4a" stroke-width="4"/><path d="M{x-18},130 H{x+18}" stroke="#a33" stroke-width="3"/>' + T(x, 118, "+5V", 16, 800, "#1d5fd1") + f'<rect x="{x-18}" y="200" width="36" height="70" fill="none" stroke="#a33" stroke-width="3"/><path d="M{x},270 V310" stroke="#1f9d4a" stroke-width="4"/><path d="M{x-16},310 H{x+16} M{x-10},319 H{x+10}" stroke="#a33" stroke-width="3"/>' + T(x + 40, 244, "R1", 16, 700, "#7a2a2a", "start")
        if ok: o += f'<path d="M{x},160 H{x-70}" stroke="#1f9d4a" stroke-width="3"/><rect x="{x-140}" y="146" width="70" height="28" rx="4" fill="#fff" stroke="#a33" stroke-width="3"/>' + T(x - 105, 166, "PWR_FLAG", 11, 800, "#7a2a2a") + chip(px + 280, 395, "ERC : aucune erreur", GREEN, w=260, size=16)
        else: o += chip(px + 280, 395, "ERC : « pin d'alimentation non pilotée »", RED, w=420, size=15) + f'<circle cx="{x}" cy="130" r="14" fill="none" stroke="{RED}" stroke-width="4"/><circle cx="{x}" cy="310" r="14" fill="none" stroke="{RED}" stroke-width="4"/>'
    return figure(W, 480, o)


def f_boitiers4():
    o = ""
    spec = [("Impression 3D FDM", "grande liberté de forme · coût très faible · pas d'IP certifié", "#9aa4ae"), ("Découpe laser", "rapide, précise (0,1 mm) · formes 2D à assembler", "#d9b77a"), ("Boîtier standard modifié", "certifié IP · robuste · peu personnalisable", "#3d4a5c"), ("Boîtier du commerce", "disponible tout de suite · à percer", "#c9d1dc")]
    for i, (t, d, c) in enumerate(spec):
        x = 30 + i * 295; o += panel(x, 30, 270, 400, t.split(" · ")[0], accent=[BLUE, AMBER, GREEN, MUTED][i])
        o += f'<g filter="url(#sh)"><rect x="{x+45}" y="140" width="180" height="120" rx="10" fill="{c}"/></g>' + f'<rect x="{x+45}" y="140" width="180" height="120" rx="10" fill="url(#cylShade)" opacity=".4"/>'
        if i == 0: o += "".join(f'<line x1="{x+50}" y1="{150+k*12}" x2="{x+220}" y2="{150+k*12}" stroke="#7d8791" stroke-width="2"/>' for k in range(9))
        if i == 1: o += "".join(f'<line x1="{x+45+k*45}" y1="140" x2="{x+45+k*45}" y2="260" stroke="#a88a52" stroke-width="2"/>' for k in range(1, 4))
        if i == 2: o += chip(x + 135, 118, "IP65", GREEN, w=80, size=14)
        o += f'<rect x="{x+60}" y="200" width="34" height="18" rx="3" fill="#222"/><circle cx="{x+190}" cy="215" r="8" fill="{RED}"/>' + T(x + 135, 300, d.split(" · ")[0], 14, 700, INK) + T(x + 135, 325, " · ".join(d.split(" · ")[1:]), 13, 600, MUTED)
    return figure(W, 470, o)


def f_plan_tests():
    cols = ["N°", "Test", "Critère", "Mesuré", "Statut"]; ws = [90, 320, 320, 260, 150]
    rows = [("TC-001", "Alimentation 3,3 V", "3,3 V ± 5 %", "3,31 V", "PASS", GREEN), ("TC-002", "Mesure DHT22", "± 0,5 °C", "± 0,3 °C", "PASS", GREEN), ("TC-003", "Thermique en boîtier fermé", "< 60 °C après 15 min", "64 °C", "FAIL", RED), ("TC-004", "Étanchéité (IP)", "IP44", "conforme", "PASS", GREEN), ("TC-005", "Wi-Fi à 15 m avec murs", "RSSI > −80 dBm", "−79 dBm", "LIMITE", AMBER)]
    o = ""; x = 40
    for c, w in zip(cols, ws): o += f'<rect x="{x}" y="40" width="{w}" height="50" fill="{INK}"/>' + T(x + w / 2, 72, c, 17, 800, "#fff"); x += w
    for r, row in enumerate(rows):
        x = 40; col = row[5]
        for k, (v, w) in enumerate(zip(row[:5], ws)):
            bg = {GREEN: "#e8f6ee", RED: "#fdeaea", AMBER: "#fff3d9"}[col] if k == 4 else ("#fff" if r % 2 == 0 else "#f6f8fc")
            o += f'<rect x="{x}" y="{90+r*58}" width="{w}" height="58" fill="{bg}" stroke="#d5dce8"/>' + T(x + w / 2, 126 + r * 58, v, 16, 800 if k == 4 else 600, col if k == 4 else INK); x += w
    o += T(600, 430, "TC-003 échoue : ajouter des aérations — TC-005 est à la limite : revoir l'antenne", 16, 700, MUTED)
    return figure(W, 460, o)


def f_chaine_s4():
    return figure(W, 330, chain([("Capteur", "grandeur physique"), ("ESP32", "calcul des KPI"), ("Alarme", "avec hystérésis"), ("Courbe", "tendance"), ("Fiche MES", "mise en service signée")], y=100, h=120, w=190, gap=50, col=[BLUE, AMBER, RED, GREEN, "#6c63ff"]) + T(600, 280, "Chaque bloc peut fonctionner seul : c'est leur enchaînement qui fait le système", 17, 700, MUTED))


def f_pv_structure():
    cols = ["Exigence (CdC)", "Critère", "Mesuré", "Incertitude U [95 %]", "Verdict"]; ws = [270, 230, 190, 270, 160]
    rows = [("E1 · Tension 3,3 V", "3,3 V ± 5 %", "3,31 V", "± 0,02 V", "CONFORME", GREEN), ("E2 · Précision de mesure", "± 0,5 °C", "0,3 °C", "± 0,2 °C", "CONFORME", GREEN), ("E3 · Autonomie", "> 48 h", "45 h", "± 1 h", "NON CONFORME", RED)]
    o = ""; x = 40
    for c, w in zip(cols, ws): o += f'<rect x="{x}" y="40" width="{w}" height="50" fill="{INK}"/>' + T(x + w / 2, 72, c, 16, 800, "#fff"); x += w
    for r, row in enumerate(rows):
        x = 40
        for k, (v, w) in enumerate(zip(row[:5], ws)):
            o += f'<rect x="{x}" y="{90+r*56}" width="{w}" height="56" fill="{"#fff" if r%2==0 else "#f6f8fc"}" stroke="#d5dce8"/>' + T(x + w / 2, 125 + r * 56, v, 16, 800 if k == 4 else 600, row[5] if k == 4 else INK); x += w
    o += f'<rect x="40" y="280" width="1120" height="90" rx="10" fill="#fdeaea" stroke="{RED}" stroke-width="3"/>' + T(70, 318, "Conclusion globale : NON CONFORME (exigence E3)", 22, 800, RED, "start") + T(70, 350, "Décision formelle qui engage le validateur et le fabricant", 16, 600, INK, "start")
    o += T(900, 318, "Date : ___/___/___", 15, 600, MUTED, "start") + T(900, 350, "Signature : ___________", 15, 600, MUTED, "start")
    return figure(W, 410, o)


def f_dossier_livraison():
    o = block(60, 80, 300, 150, "DAT électronique", "mémoire technique de la conception", BLUE) + block(450, 80, 300, 150, "PV de validation", "preuve de conformité", GREEN) + block(840, 80, 300, 150, "Fiche MES", "acte de remise", AMBER)
    o += "".join(s_wire([(x, 230), (x, 270), (600, 270)], INK, 4) for x in (210, 600, 990)) + arrow(600, 270, 600, 310, INK, 5) + block(400, 310, 400, 90, "Dossier de livraison", "remis au client", "#6c63ff")
    o += T(600, 440, "Ensemble : la preuve légale que le produit livré est conforme", 17, 700, INK)
    return figure(W, 470, o)


def f_tracabilite():
    lv = [("BIPM", "étalons internationaux (SI)", "#6c63ff"), ("Laboratoire national", "étalons nationaux", BLUE), ("Laboratoire accrédité COFRAC", "étalons de référence", GREEN), ("Étalon de travail", "de l'entreprise", AMBER), ("Instrument (ex. Fluke)", "étalonné COFRAC en 2026", RED), ("PV de mesure", "valeur légale", INK)]
    o = ""
    for i, (t, s, c) in enumerate(lv):
        x = 60 + i * 180 if False else 60; y = 30 + i * 70
        o += f'<rect x="{80+i*40}" y="{y}" width="{820-i*40}" height="58" rx="10" fill="{c}"/>' + T(100 + i * 40, y + 36, t, 20, 800, "#fff", "start") + T(880, y + 36, s, 16, 600, "#fff", "end")
        if i < 5: o += arrow(600, y + 60, 600, y + 70, INK, 1) if False else ""
    o += "".join(T(1070, 215 + i * 24, t, 16, 700, MUTED) for i, t in enumerate(("raccordement", "successif", "avec incertitude", "connue"))) + arrow(1000, 60, 1000, 420, MUTED, 3)
    return figure(W, 470, o)


def f_incertitude():
    o = ""; x0 = 300
    bars = [("u_A (statistique)", 1.2, BLUE), ("u_B résolution", 0.3, AMBER), ("u_B classe de l'instrument", 13.6, RED)]
    sc = 36
    for i, (t, v, c) in enumerate(bars):
        y = 60 + i * 80; o += T(280, y + 32, t, 18, 700, INK, "end") + f'<rect x="{x0}" y="{y}" width="{max(v*sc,6)}" height="46" rx="6" fill="{c}"/>' + T(x0 + max(v * sc, 6) + 14, y + 32, f"{v} Ω".replace(".", ","), 18, 800, c, "start")
    o += f'<line x1="{x0}" y1="48" x2="{x0}" y2="300" stroke="{INK}" stroke-width="2"/>' + f'<rect x="{x0}" y="290" width="{13.7*sc}" height="46" rx="6" fill="{INK}"/>' + T(280, 322, "u_c combinée", 18, 800, INK, "end") + T(x0 + 13.7 * sc + 14, 322, "13,7 Ω", 18, 800, INK, "start")
    o += chip(600, 410, "La classe de l'instrument domine : améliorer la répétabilité ne sert à rien ici", INK, w=860, size=16)
    return figure(W, 450, o)


FIGS = {"kicad_editeur_schema": f_kicad_editor, "kicad_schema_led": f_kicad_led, "kicad_drc": f_kicad_drc, "kicad_vue_3d": f_kicad_3d, "kicad_export_gerber": f_kicad_gerber,
        "nodered_flow_simple": f_nr_simple, "nodered_dashboard": f_nr_dashboard, "nodered_flow_complet": f_nr_complet, "deca_entonnoir": f_deca, "logigramme_esp32": f_logigramme,
        "chaine_iot_mqtt": f_chaine_iot, "cablage_professionnel": f_cablage_pro, "dat_amateur_pro": f_dat, "cloudwatch_dashboard": f_cloudwatch, "eeschema_vue": f_eeschema, "pwr_flag": f_pwrflag,
        "boitiers_quatre": f_boitiers4, "plan_tests_exemple": f_plan_tests, "chaine_s4": f_chaine_s4, "pv_validation": f_pv_structure, "dossier_livraison": f_dossier_livraison,
        "tracabilite_metrologique": f_tracabilite, "incertitude_composition": f_incertitude}
