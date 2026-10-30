"""Seconde S11 : figures manquantes (PCB simple face)."""
from hl import *
import math

CU = "#d99a52"


def f_coupe_pcb():
    o = ""
    layers = [("FR4 1,6 mm", "substrat en fibre de verre et époxy", "#7d8a74", 150), ("Cuivre 35 µm = 1 oz", "fine couche conductrice", CU, 24), ("Résine photosensible", "zones exposées / non exposées", "#bfe3a8", 20), ("Masque de soudure", "vert, protège les pistes", "#1c7a46", 22)]
    y = 440
    xs, xe = 120, 760
    for t, s, c, h in layers:
        y -= h
        o += f'<rect x="{xs}" y="{y}" width="{xe-xs}" height="{h}" fill="{c}" stroke="#0003"/>'
    # trou métallisé / pad
    o += f'<rect x="400" y="170" width="70" height="270" fill="#fff"/><rect x="396" y="246" width="5" height="48" fill="{CU}"/><rect x="469" y="246" width="5" height="48" fill="{CU}"/>' if False else f'<rect x="410" y="150" width="60" height="300" fill="#fff"/><rect x="380" y="270" width="30" height="24" fill="{CU}"/><rect x="470" y="270" width="30" height="24" fill="{CU}"/>'
    # zone exposée (hachurée)
    o += f'<rect x="560" y="246" width="120" height="20" fill="#9ed07f"/>' + ''.join(f'<path d="M{566+i*14},266 l10,-20" stroke="#4d8a3a" stroke-width="2"/>' for i in range(8))
    y = 420
    ys = {}
    cy = 440
    for t, s, c, h in layers:
        cy -= h; ys[t] = cy + h / 2
    for i, (t, s, c, h) in enumerate(layers):
        ty = 120 + i * 90
        o += f'<line x1="{xe}" y1="{ys[t]}" x2="830" y2="{ty}" stroke="{MUTED}" stroke-width="2"/><circle cx="{xe}" cy="{ys[t]}" r="5" fill="#fff" stroke="{MUTED}" stroke-width="2.5"/>' + T(840, ty - 2, t, 20, 800, INK, "start") + T(840, ty + 24, s, 15, 500, MUTED, "start")
    o += callout(440, 200, 300, 90, "trou de perçage traversant\navec son pad de cuivre", "middle", 16, bold=True)
    return figure(W, 480, o)


def f_flux_fab():
    steps = [("1", "Schéma et\nrouting KiCad", BLUE), ("2", "Impression\ndu typon", BLUE), ("3", "Transfert du typon\nsur l'époxy", AMBER), ("4", "Révélation\n(NaOH)", AMBER), ("5", "Gravure chimique\n(FeCl₃) ⚠", RED), ("6", "Rinçage et\nneutralisation 💧", RED), ("7", "Retrait du masque\nrésiduel (IPA)", GREEN), ("8", "Perçage", GREEN)]
    o = ""
    for i, (n, t, c) in enumerate(steps):
        x = 40 + (i % 4) * 285; y = 50 + (i // 4) * 200
        o += f'<rect x="{x}" y="{y}" width="250" height="120" rx="14" fill="#fff" stroke="{c}" stroke-width="4"/><rect x="{x}" y="{y}" width="56" height="120" rx="14" fill="{c}"/><rect x="{x+30}" y="{y}" width="26" height="120" fill="{c}"/>' + T(x + 28, y + 70, n, 32, 800, "#fff") + T(x + 155, y + 54 - (6 if "\n" in t else 0), t, 18, 800, INK)
        if i % 4 < 3: o += arrow(x + 252, y + 60, x + 283, y + 60, INK, 4)
    o += s_wire([(165, 172), (165, 200), (1100 - 0, 200)], INK, 3) if False else f'<path d="M1165,170 V210 H165 V250" fill="none" stroke="{INK}" stroke-width="4" marker-end="url(#arr)"/>' if False else f'<path d="M1165,170 V210 H165 V248" fill="none" stroke="{INK}" stroke-width="4" marker-end="url(#arr)"/>'
    o += chip(600, 440, "Étapes 5 et 6 : chimie — gants, lunettes, blouse et local ventilé obligatoires", RED, w=820, size=16)
    return figure(W, 480, o)


def f_gravure_meca():
    o = panel(30, 30, 380, 380, "Avant gravure", accent=BLUE) + panel(425, 30, 350, 380, "Réaction", accent=RED) + panel(790, 30, 380, 380, "Après gravure", accent=GREEN)
    def pcb(x, etched):
        r = f'<rect x="{x}" y="300" width="320" height="50" fill="#7d8a74"/>'
        for i, (cx, w) in enumerate(((x + 20, 80), (x + 140, 60), (x + 240, 60))):
            if etched and i != 1 and False: pass
            r += f'<rect x="{cx}" y="270" width="{w}" height="30" fill="{CU}"/>' + (f'<rect x="{cx}" y="262" width="{w}" height="8" fill="#111"/>' if True else "")
        if not etched: r += f'<rect x="{x+100}" y="270" width="40" height="30" fill="{CU}"/><rect x="{x+200}" y="270" width="40" height="30" fill="{CU}"/>'
        return r
    o += pcb(60, False) + T(220, 395, "toner (noir) protège le cuivre", 14, 700, MUTED) + pcb(830, True) + T(990, 395, "cuivre nu dissous", 14, 700, MUTED)
    o += f'<circle cx="540" cy="150" r="30" fill="#2f5bea"/>' + T(540, 156, "Fe³⁺", 17, 800, "#fff") + ''.join(f'<circle cx="{540+int(52*math.cos(a))}" cy="{150+int(52*math.sin(a))}" r="16" fill="#2ecc71"/>' + T(540 + int(52 * math.cos(a)), 156 + int(52 * math.sin(a)), "Cl⁻", 12, 800, "#fff") for a in (0, 2.1, 4.2)) + T(600, 250, "FeCl₃ attaque le cuivre", 15, 700, INK) + arrow(480, 300, 720, 300, RED, 5) + T(600, 335, "Cu → Cu²⁺ (dissous)", 15, 700, RED)
    o += chip(600, 450, "2 FeCl₃ + Cu → 2 FeCl₂ + CuCl₂", INK, w=560, size=20)
    o += arrow(380, 180, 440, 180, MUTED, 4) + arrow(770, 180, 830, 180, MUTED, 4)
    return figure(W, 490, o)


def f_defauts_gravure():
    o = ""
    ttl = [("SOUS-GRAVURE", "ponts de cuivre → courts-circuits", RED), ("GRAVURE CORRECTE", "pistes nettes, bords réguliers", GREEN), ("SUR-GRAVURE", "pistes trop fines, coupures", RED)]
    for k, (t, s, c) in enumerate(ttl):
        x = 30 + k * 385; o += panel(x, 30, 370, 400, t, accent=c) + f'<rect x="{x+20}" y="90" width="330" height="240" rx="6" fill="#1c7a46"/>'
        for j in range(3):
            y = 120 + j * 70
            if k == 0: o += f'<rect x="{x+40}" y="{y}" width="290" height="22" fill="{CU}"/>' + f'<rect x="{x+40}" y="{y+22}" width="290" height="{40 if j<2 else 0}" fill="{CU}" opacity=".45"/>'
            elif k == 1: o += f'<rect x="{x+40}" y="{y}" width="290" height="22" fill="#e8aa62"/>'
            else:
                o += f'<rect x="{x+40}" y="{y+6}" width="290" height="9" fill="{CU}"/>' + ''.join(f'<rect x="{x+40+m*45}" y="{y+2 if m%2 else y+10}" width="6" height="6" fill="#1c7a46"/>' for m in range(1, 7))
                if j == 1: o += f'<rect x="{x+150}" y="{y+2}" width="40" height="16" fill="#1c7a46"/>'
        o += T(x + 185, 375, s, 16, 800, GREEN if k == 1 else RED) + T(x + 185, 405, "✓ conforme" if k == 1 else "✘ à refaire", 16, 800, GREEN if k == 1 else RED)
    return figure(W, 460, o)


def f_perceuse():
    o = f'<rect x="130" y="90" width="26" height="380" fill="#8a95a5"/><rect x="100" y="470" width="320" height="30" rx="8" fill="#4a5568"/><rect x="130" y="80" width="260" height="90" rx="14" fill="#2f5bea"/><rect x="330" y="60" width="90" height="40" rx="8" fill="#1e3fa8"/>'
    o += f'<rect x="300" y="170" width="40" height="70" fill="#9aa4b2"/><rect x="310" y="240" width="20" height="50" fill="#cfd6df"/><rect x="317" y="290" width="6" height="90" fill="#b8860b"/>'
    o += f'<rect x="170" y="370" width="320" height="22" fill="#6a7384"/><rect x="240" y="392" width="170" height="10" fill="#1c7a46"/><rect x="156" y="380" width="30" height="40" fill="#4a5568"/><rect x="200" y="350" width="40" height="20" rx="4" fill="#d9a441"/>'
    items = [(260, 100, "Moteur et poulie : vitesse élevée"), (143, 250, "Colonne verticale"), (320, 255, "Mandrin de serrage de précision"), (320, 340, "Foret carbure de tungstène Ø 0,8 à 1 mm"), (210, 360, "Butée de profondeur"), (330, 380, "Table réglable (plateau d'appui du PCB)")]
    for n, (px, py, t) in enumerate(items, 1):
        y = 90 + (n - 1) * 62; o += callout(px, py, 640, y, "", "start") + badge(640, y, n, BLUE, 15) + T(666, y + 6, t, 17, 700, INK, "start")
    o += chip(850, 490, "Vitesse élevée, avance lente : le carbure casse si on force", AMBER, w=560, size=15)
    return figure(W, 530, o)


def f_ipc_a600():
    crit = [("1 · Largeur de piste", "uniforme", "rétrécie > 20 %"), ("2 · Espacement", "écart conforme", "pont de cuivre"), ("3 · Anneau de cuivre", "anneau complet ≥ 0,15 mm", "anneau partiel ou absent"), ("4 · Surface de la piste", "lisse, brillante", "piqûres, trous"), ("5 · Trou de perçage", "centré, bords nets", "décalé, ébarbé")]
    o = T(310, 55, "OK", 22, 800, GREEN) + T(870, 55, "NOK", 22, 800, RED)
    for i, (t, a, b) in enumerate(crit):
        y = 80 + i * 108
        o += f'<rect x="30" y="{y}" width="1140" height="96" rx="12" fill="{PANEL}" stroke="#d9e0ec" stroke-width="2"/>' + T(50, y + 55, t, 19, 800, INK, "start")
        for k, (x, ok, lab) in enumerate(((440, True, a), (900, False, b))):
            c = GREEN if ok else RED; cx, cy = x - 110, y + 48
            o += f'<rect x="{cx-70}" y="{cy-34}" width="140" height="68" rx="6" fill="#1c7a46"/>'
            if i == 0: o += f'<rect x="{cx-60}" y="{cy-11}" width="120" height="{22 if ok else 12}" fill="{CU}" transform="translate(0,{0 if ok else 5})"/>'
            elif i == 1: o += f'<rect x="{cx-60}" y="{cy-26}" width="120" height="16" fill="{CU}"/><rect x="{cx-60}" y="{cy+10}" width="120" height="16" fill="{CU}"/>' + ("" if ok else f'<rect x="{cx-10}" y="{cy-12}" width="20" height="24" fill="{CU}"/>')
            elif i == 2: o += f'<circle cx="{cx}" cy="{cy}" r="28" fill="{CU}"/><circle cx="{cx+(0 if ok else 14)}" cy="{cy}" r="13" fill="#222"/>'
            elif i == 3: o += f'<rect x="{cx-60}" y="{cy-16}" width="120" height="32" fill="{CU}"/>' + ("" if ok else ''.join(f'<circle cx="{cx-35+m*28}" cy="{cy-4+(m%2)*8}" r="4" fill="#1c7a46"/>' for m in range(4)))
            else: o += f'<circle cx="{cx}" cy="{cy}" r="28" fill="{CU}"/><circle cx="{cx+(0 if ok else 12)}" cy="{cy+(0 if ok else -8)}" r="11" fill="#222"/>' + ("" if ok else f'<path d="M{cx+20},{cy-12} l8,-4 M{cx+22},{cy+4} l9,2" stroke="{CU}" stroke-width="3"/>')
            o += T(x + 60, y + 54, lab, 17, 700, c, "start") + T(x - 190 + 0, y + 54, "✓" if ok else "✘", 24, 800, c, "end") if False else T(x + 20, y + 54, ("✓ " if ok else "✘ ") + lab, 17, 700, c, "start")
    return figure(W, 640, o)


def f_anneau():
    cx, cy = 360, 250
    o = f'<circle cx="{cx}" cy="{cy}" r="150" fill="{CU}"/><circle cx="{cx}" cy="{cy}" r="83" fill="#fff" stroke="#333" stroke-width="3"/>' + f'<circle cx="{cx}" cy="{cy}" r="150" fill="none" stroke="#a5642a" stroke-width="3"/>'
    o += f'<path d="M{cx},{cy} L{cx+150},{cy}" stroke="{INK}" stroke-width="3"/>' + f'<path d="M{cx-150},{cy+190} H{cx+150}" stroke="{INK}" stroke-width="3" marker-start="url(#arr)" marker-end="url(#arr)"/>' + T(cx, cy + 180, "Ø pad = 1,8 mm", 20, 800, INK) + f'<path d="M{cx-83},{cy+150} H{cx+83}" stroke="{BLUE}" stroke-width="3" marker-start="url(#arr)" marker-end="url(#arr)"/>' + T(cx, cy + 135, "Ø trou = 1,0 mm", 18, 800, BLUE)
    o += f'<path d="M{cx+83},{cy-100} L{cx+150},{cy-100}" stroke="{RED}" stroke-width="0"/>' + f'<path d="M{cx+84},{cy+2} H{cx+148}" stroke="{RED}" stroke-width="5" marker-start="url(#arr)" marker-end="url(#arr)"/>' + T(cx + 118, cy + 30, "0,4", 15, 800, "#fff")
    o += callout(cx + 120, cy + 2, 700, 150, "Anneau de cuivre\n(annular ring)", "start", 22, bold=True)
    o += T(700, 240, "Largeur de l'anneau = (Ø pad − Ø trou) / 2", 20, 800, INK, "start") + T(700, 280, "= (1,8 − 1,0) / 2 = 0,4 mm", 24, 800, BLUE, "start") + chip(880, 350, "Critère IPC : anneau ≥ 0,15 mm  ✔", GREEN, w=440, size=18) + T(700, 400, "0,4 mm ≥ 0,15 mm : l'anneau est conforme", 17, 700, GREEN, "start")
    return figure(W, 530, o)


def f_test_pcb():
    o = f'<rect x="30" y="30" width="700" height="440" rx="12" fill="#1c7a46"/>'
    pads = {"a1": (100, 130), "a2": (360, 130), "b1": (100, 230), "b2": (360, 230), "c1": (100, 340), "c2": (360, 340)}
    for (p, q, y) in (("a1", "a2", 130), ("b1", "b2", 230)): o += f'<path d="M{pads[p][0]},{y} H{pads[q][0]}" stroke="{CU}" stroke-width="14"/>'
    o += f'<path d="M100,340 H250" stroke="{CU}" stroke-width="14"/>'
    for k, (x, y) in pads.items(): o += f'<circle cx="{x}" cy="{y}" r="26" fill="{CU}"/><circle cx="{x}" cy="{y}" r="9" fill="#111"/>' if k != "c2" else f'<circle cx="{x}" cy="{y}" r="26" fill="{CU}"/><circle cx="{x}" cy="{y}" r="9" fill="#111"/>'
    for x, y, c in ((100, 130, RED), (360, 130, "#111")): o += f'<path d="M{x},{y} l{-30 if c==RED else 30},-70" stroke="{c}" stroke-width="5" marker-end="url(#arr)"/>' if False else ""
    o += f'<path d="M100,130 L60,55" stroke="{RED}" stroke-width="5"/><path d="M360,130 L400,55" stroke="#111" stroke-width="5"/>' + badge(60, 52, "A", BLUE, 16) + f'<path d="M100,230 L170,275" stroke="{RED}" stroke-width="5" opacity="0"/>'
    o += f'<path d="M230,230 L190,175" stroke="{RED}" stroke-width="5"/><path d="M230,130 L270,175" stroke="#111" stroke-width="5" opacity="0"/>' + f'<path d="M360,340 L420,420" stroke="{RED}" stroke-width="5"/>' + badge(190, 172, "B", BLUE, 16) + badge(430, 425, "C", BLUE, 16)
    o += f'<path d="M230,130 L230,175" stroke="#111" stroke-width="5"/>'
    tests = [("A", "Continuité d'une piste", "0,2 Ω", "attendu < 1 Ω", GREEN), ("B", "Isolation entre deux pistes voisines", "OL (∞)", "attendu > 1 MΩ", GREEN), ("C", "Pad vers piste (trou percé)", "0,3 Ω", "le pad est bien relié à sa piste", GREEN)]
    for i, (n, t, v, a, c) in enumerate(tests):
        y = 50 + i * 150; o += f'<rect x="770" y="{y}" width="400" height="130" rx="12" fill="{PANEL}" stroke="#d9e0ec" stroke-width="2"/>' + badge(800, y + 30, n, BLUE, 16) + T(826, y + 36, t, 16, 800, INK, "start") + f'<rect x="800" y="{y+54}" width="130" height="50" rx="6" fill="#cfe3c4"/>' + T(865, y + 90, v, 24, 700, "#1d2a1a", extra='font-family="monospace"') + T(950, y + 86, "✔ " + a, 14, 700, c, "start")
    return figure(W, 510, o)


FIGS = {"pcb_coupe_couches": f_coupe_pcb, "flux_fabrication_pcb": f_flux_fab, "gravure_mecanisme": f_gravure_meca, "gravure_defauts": f_defauts_gravure, "perceuse_colonne": f_perceuse, "criteres_ipc_a600": f_ipc_a600, "anneau_cuivre": f_anneau, "test_multimetre_pcb": f_test_pcb}
