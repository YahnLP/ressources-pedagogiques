"""Seconde S05 et S06 : figures manquantes."""
from hl import *
from figs_sym import relais_body, opto_body
import math


def f_pyr_maint():
    o, h = pyramid([("N4\nRénovation, reconstruction", "Équipe spécialisée ou constructeur", RED), ("N3\nPannes complexes, échange de composant", "Technicien spécialisé", AMBER), ("N2\nDépannage par échange standard", "Technicien habilité", "#c9a400"), ("N1\nRéglages, nettoyage, vérifications visuelles", "Opérateur ou technicien de proximité", GREEN)], w=460, h=104, tx=560, sz=22)
    o += arrow(1160, h - 40, 1160, 50, MUTED, 5) + T(1135, h / 2, "qualification croissante", 16, 700, MUTED, extra=f'transform="rotate(-90 1135 {h/2})"')
    return figure(W, int(h) + 10, o)


def f_prev_corr():
    o = duo(0, 0, "Maintenance préventive — avant la panne", "Maintenance corrective — après la panne", GREEN, RED, h=360)
    for x, items, c in ((60, ["nettoyage périodique", "vérification visuelle programmée", "remplacement préventif des condensateurs", "mise à jour du firmware"], GREEN), (650, ["diagnostic de la panne", "remplacement du composant défaillant", "ressoudure d'une brasure froide", "test après réparation"], RED)):
        for i, t in enumerate(items): o += badge(x + 14, 112 + i * 62, "✓" if c == GREEN else "🔧", c, 14) if False else f'<circle cx="{x+14}" cy="{112+i*62}" r="9" fill="{c}"/>' + T(x + 40, 119 + i * 62, t, 19, 600, INK, "start")
    o += f'<rect x="30" y="410" width="1140" height="150" rx="14" fill="{PANEL}" stroke="#d9e0ec" stroke-width="2"/>' + T(60, 446, "Fréquence des interventions correctives dans le temps", 17, 800, INK, "start")
    o += f'<line x1="70" y1="540" x2="1130" y2="540" stroke="{INK}" stroke-width="2"/>'
    for k, (cx, c) in enumerate((("sans préventif", RED), ("avec préventif", GREEN))):
        y = 480 + k * 36; o += T(260, y + 6, cx, 16, 700, c, "end")
        xs = [300 + i * 70 for i in range(13)] if k == 0 else [300 + i * 160 for i in range(6)]
        o += ''.join(f'<circle cx="{x}" cy="{y}" r="9" fill="{c}"/>' for x in xs)
    o += T(1130, 572, "temps →", 14, 700, MUTED, "end")
    return figure(W, 590, o)


def f_outils_nettoyage():
    o = ""
    for i in range(4): o += panel(30 + i * 292, 30, 276, 440, None)
    o += '<g filter="url(#sh)"><rect x="95" y="150" width="140" height="230" rx="18" fill="#d9ecf5" stroke="#8fb7cc" stroke-width="2"/><rect x="130" y="100" width="70" height="60" rx="8" fill="#fff" stroke="#8a95a5"/><rect x="150" y="70" width="60" height="30" rx="6" fill="#2a2d33"/></g>' + T(165, 250, "IPA", 40, 800, "#1d6e96") + T(165, 285, "isopropanol 99 %", 13, 700, "#1d6e96")
    o += '<g filter="url(#sh)" transform="rotate(-25 460 260)"><rect x="380" y="240" width="120" height="40" rx="10" fill="#2f5bea"/><rect x="496" y="248" width="120" height="24" rx="4" fill="#cfd6df"/></g>' + ''.join(f'<path d="M{590+i*6},{196+i*2} l22,-8" stroke="#8a6a3a" stroke-width="3"/>' for i in range(8))
    o += '<g filter="url(#sh)"><rect x="705" y="130" width="100" height="230" rx="20" fill="#25282e"/><rect x="725" y="100" width="60" height="40" rx="8" fill="#9aa4b2"/></g><rect x="722" y="200" width="66" height="60" rx="6" fill="#ffd54f"/>' + T(755, 238, "ESD", 22, 800, "#222")
    o += '<g filter="url(#sh)"><rect x="935" y="170" width="150" height="150" fill="#fff" stroke="#cfd6df"/><rect x="950" y="185" width="150" height="150" fill="#fbfbfb" stroke="#cfd6df"/></g>'
    for i, (t, s) in enumerate((("Isopropanol 99 %", "dissout flux et saletés"), ("Pinceau antistatique", "dépoussière sans charge"), ("Air comprimé ESD", "souffle la poussière"), ("Chiffons non pelucheux", "essuient sans fibres"))):
        x = 168 + i * 292; o += badge(x - 110, 62, i + 1, BLUE, 16) + T(x, 420, t, 19, 800, INK) + T(x, 446, s, 15, 500, MUTED)
    return figure(W, 500, o)


def f_grille_diag():
    items = [("1", "État général", "poussière · propre", "dust"), ("2", "Composants", "droits · penchés · manquants", "comp"), ("3", "Brasures", "brillantes · froides · ponts", "sold"), ("4", "Condensateurs", "normaux · gonflés", "cap"), ("5", "Pistes", "intactes · corrodées · coupées", "trace"), ("6", "Connecteurs", "propres · oxydés", "conn"), ("7", "Traces thermiques", "absence · brûlures", "burn"), ("8", "Corps des composants", "intacts · fissurés · brûlés", "body"), ("9", "Repères sérigraphiés", "lisibles · effacés", "silk")]
    o = ""
    for i, (n, t, s, k) in enumerate(items):
        x = 25 + (i % 3) * 387; y = 25 + (i // 3) * 220; cx, cy = x + 190, y + 80
        o += f'<rect x="{x}" y="{y}" width="372" height="205" rx="14" fill="{PANEL}" stroke="#d9e0ec" stroke-width="2"/>' + badge(x + 30, y + 34, n, BLUE, 17)
        if k == "dust": o += f'<rect x="{cx-60}" y="{cy-30}" width="120" height="60" rx="6" fill="#1c7a46"/>' + ''.join(f'<circle cx="{cx-50+(j*37)%100}" cy="{cy-22+(j*23)%44}" r="3" fill="#b9b2a4"/>' for j in range(14))
        elif k == "comp": o += ''.join(f'<rect x="{cx-50+j*40}" y="{cy-26}" width="16" height="50" rx="3" fill="#d9a441" transform="rotate({a} {cx-42+j*40} {cy})"/>' for j, a in enumerate((0, 22, 0)))
        elif k == "sold": o += ''.join(f'<circle cx="{cx-50+j*50}" cy="{cy}" r="17" fill="{c}" stroke="#8a95a5" stroke-width="2"/>' for j, c in enumerate(("#e3e8ef", "#9aa0a8", "#e3e8ef"))) + f'<rect x="{cx+8}" y="{cy-6}" width="34" height="12" rx="6" fill="#d6dbe3"/>'
        elif k == "cap": o += f'<rect x="{cx-70}" y="{cy-30}" width="50" height="60" rx="8" fill="#2b4a8a"/><rect x="{cx+20}" y="{cy-42}" width="50" height="72" rx="10" fill="#2b4a8a"/><ellipse cx="{cx+45}" cy="{cy-42}" rx="25" ry="8" fill="#6a85c4"/>' + T(cx + 45, cy + 54, "gonflé", 13, 800, RED) if False else f'<rect x="{cx-70}" y="{cy-30}" width="50" height="60" rx="8" fill="#2b4a8a"/><rect x="{cx+20}" y="{cy-42}" width="50" height="72" rx="10" fill="#2b4a8a"/><ellipse cx="{cx+45}" cy="{cy-42}" rx="25" ry="8" fill="#6a85c4"/>'
        elif k == "trace": o += f'<path d="M{cx-80},{cy} H{cx-20} M{cx+20},{cy} H{cx+80}" stroke="{COPPER}" stroke-width="10"/><path d="M{cx-14},{cy-14} l28,28 M{cx+14},{cy-14} l-28,28" stroke="{RED}" stroke-width="5"/>'
        elif k == "conn": o += f'<rect x="{cx-70}" y="{cy-24}" width="140" height="48" rx="6" fill="#333"/>' + ''.join(f'<rect x="{cx-60+j*24}" y="{cy-14}" width="12" height="28" fill="{c}"/>' for j, c in enumerate(("#d9a441", "#d9a441", "#5aa17f", "#d9a441", "#d9a441")))
        elif k == "burn": o += f'<rect x="{cx-50}" y="{cy-30}" width="100" height="60" rx="6" fill="#1c7a46"/><circle cx="{cx+10}" cy="{cy}" r="24" fill="#4a3220" opacity=".85"/><circle cx="{cx+10}" cy="{cy}" r="12" fill="#1a1a1a"/>'
        elif k == "body": o += f'<rect x="{cx-50}" y="{cy-26}" width="100" height="52" rx="6" fill="#222"/><path d="M{cx-10},{cy-26} l10,22 l-8,10 l14,20" stroke="#aaa" stroke-width="3" fill="none"/>'
        else: o += f'<rect x="{cx-60}" y="{cy-30}" width="120" height="60" rx="6" fill="#1c7a46"/>' + T(cx - 20, cy + 6, "R12", 22, 800, "#e8f5ec") + T(cx + 30, cy + 6, "C3", 22, 800, "#6a9a7a")
        o += T(cx, y + 152, t, 20, 800, INK) + T(cx, y + 180, s, 14, 500, MUTED)
    return figure(W, 705, o)


def person(x, y, c="#5d6b86"):
    return f'<circle cx="{x}" cy="{y-100}" r="20" fill="{c}"/><rect x="{x-24}" y="{y-76}" width="48" height="90" rx="14" fill="{c}"/><path d="M{x-12},{y+14} V{y+80} M{x+12},{y+14} V{y+80}" stroke="{c}" stroke-width="14" stroke-linecap="round"/><path d="M{x-24},{y-62} L{x-48},{y-8} M{x+24},{y-62} L{x+50},{y-20}" stroke="{c}" stroke-width="12" stroke-linecap="round"/>'


def f_esd():
    o = duo(0, 0, "1 · Accumulation de charges", "2 · Décharge dans le composant", AMBER, RED, h=470)
    o += f'<line x1="70" y1="410" x2="540" y2="410" stroke="{INK}" stroke-width="4"/>' + person(300, 320)
    o += ''.join(f'<path d="M{300+int(70*math.cos(a))},{250+int(95*math.sin(a))} q8,-8 0,-16" stroke="#d6a419" stroke-width="3" fill="none"/>' for a in [i * 0.8 for i in range(8)]) + ''.join(T(300 + int(88 * math.cos(a)), 255 + int(110 * math.sin(a)), "+", 20, 800, "#d6a419") for a in [i * 0.8 + .4 for i in range(8)])
    o += chip(300, 460, "5 000 à 35 000 V accumulés", AMBER, w=360, size=17)
    o += f'<line x1="640" y1="410" x2="1120" y2="410" stroke="{INK}" stroke-width="4"/>' + person(740, 320)
    o += dip(8, 150, 40, "CI", 20, 12) if False else f'<rect x="900" y="360" width="130" height="50" rx="6" fill="#222"/>' + ''.join(f'<rect x="{910+i*28}" y="410" width="8" height="18" fill="#c0c6cf"/>' for i in range(4)) + T(965, 392, "CI", 22, 800, "#fff")
    o += f'<path d="M790,300 L830,330 L850,300 L890,340 L915,355" stroke="#ff8a00" stroke-width="7" fill="none" stroke-linejoin="round"/>' + T(955, 320, "💥", 44, 500, RED) + T(965, 455, "jonction détruite en quelques ns", 16, 700, RED) if False else f'<path d="M790,300 L830,330 L850,300 L890,340 L915,358" stroke="#ff8a00" stroke-width="7" fill="none" stroke-linejoin="round"/>' + f'<circle cx="965" cy="385" r="26" fill="none" stroke="{RED}" stroke-width="5"/><path d="M949,369 L981,401 M981,369 L949,401" stroke="{RED}" stroke-width="5"/>'
    o += T(850, 460, "courant de pointe : quelques ampères en quelques nanosecondes", 15, 700, RED) + T(850, 100 + 30, "→ destruction de la jonction semi-conductrice", 15, 700, INK) if False else T(870, 480, "pointe de courant : quelques ampères en quelques nanosecondes", 15, 700, RED) + T(870, 450, "", 10)
    return figure(W, 520, o)


def f_esd_dommage():
    o = duo(0, 0, "Dommage immédiat", "Dommage latent", RED, AMBER, h=470)
    for x0, kind in ((70, 0), (660, 1)):
        o += f'<line x1="{x0}" y1="380" x2="{x0+470}" y2="380" stroke="{INK}" stroke-width="2.5"/><line x1="{x0}" y1="110" x2="{x0}" y2="380" stroke="{INK}" stroke-width="2.5"/>' + T(x0 + 470, 405, "temps", 14, 700, MUTED, "end") + T(x0 - 8, 105, "performance", 14, 700, MUTED, "start")
        o += f'<line x1="{x0+120}" y1="110" x2="{x0+120}" y2="380" stroke="{RED}" stroke-width="2" stroke-dasharray="6 6"/>' + T(x0 + 190, 100, "décharge ESD", 14, 800, RED)
    o += f'<path d="M70,150 H190 V378 H540" stroke="{RED}" stroke-width="5" fill="none"/>' + chip(380, 440, "HS immédiatement : facile à repérer", RED, w=400, size=16)
    o += f'<path d="M660,150 H780 q60,2 120,20 q80,40 130,120 q40,60 70,88" stroke="{AMBER}" stroke-width="5" fill="none"/>' + T(1000, 280, "panne\naléatoire", 16, 800, RED) + chip(910, 440, "Panne aléatoire, difficile à diagnostiquer : coût bien supérieur", AMBER, w=520, size=15)
    return figure(W, 520, o)


def f_poste_esd():
    o = f'<rect x="30" y="30" width="1140" height="520" rx="14" fill="{PANEL}" stroke="#d9e0ec" stroke-width="2"/>'
    o += f'<rect x="150" y="330" width="720" height="26" fill="#9aa4b2"/><rect x="170" y="356" width="14" height="150" fill="#6a7384"/><rect x="836" y="356" width="14" height="150" fill="#6a7384"/><rect x="200" y="312" width="480" height="18" rx="4" fill="#5d6b86"/>'
    o += person(300, 420, "#7d8aa5").replace('y="', 'y="') if False else ""
    o += f'<circle cx="300" cy="170" r="22" fill="#7d8aa5"/><rect x="274" y="196" width="52" height="100" rx="14" fill="#7d8aa5"/><path d="M326,230 Q380,260 420,312" stroke="#7d8aa5" stroke-width="14" fill="none" stroke-linecap="round"/><path d="M290,296 V470 M310,296 V470" stroke="#7d8aa5" stroke-width="16" stroke-linecap="round"/><rect x="270" y="470" width="60" height="14" rx="4" fill="#25282e"/>'
    o += f'<rect x="404" y="302" width="40" height="10" rx="4" fill="{GREEN}"/><path d="M424,306 Q500,260 560,312" stroke="{GREEN}" stroke-width="4" fill="none"/>'
    o += f'<path d="M600,321 H740 V440" stroke="{GREEN}" stroke-width="4" stroke-dasharray="8 6" fill="none"/>' + f'<rect x="715" y="440" width="50" height="60" rx="6" fill="#fff" stroke="{INK}" stroke-width="3"/>' + gnd(740, 470) if False else f'<path d="M640,321 H760 V420" stroke="{GREEN}" stroke-width="4" stroke-dasharray="8 6" fill="none"/><rect x="725" y="420" width="70" height="60" rx="6" fill="#fff" stroke="{INK}" stroke-width="3"/>' + gnd(760, 436)
    o += f'<rect x="690" y="262" width="110" height="50" rx="4" fill="#cfd6df" stroke="#8a95a5"/><rect x="520" y="270" width="130" height="42" rx="6" fill="#2f3440"/>' + f'<path d="M960,320 l50,0 v-20 h-50 z" fill="#d3dae3"/><rect x="940" y="276" width="110" height="52" rx="4" fill="#bfc7d3" stroke="#8a95a5"/>'
    for n, (px, py, tx, ty, t) in enumerate([(340, 262, 150, 80, "Bracelet ESD relié au tapis"), (560, 322, 460, 80, "Tapis antistatique relié à la terre"), (760, 440, 900, 130, "Prise de terre murale"), (1000, 296, 900, 80, "Sachet antistatique argenté"), (590, 290, 610, 225, "Bac ESD pour les pièces"), (300, 478, 150, 520, "Chaussures ou semelles ESD")], 1):
        o += callout(px, py, tx, ty, "", "start") + badge(tx, ty, n, BLUE, 15) + T(tx + 24, ty + 6, t, 16, 700, INK, "start")
    return figure(W, 580, o)


def f_outils_techno():
    tools = [("Brucelle droite", "saisir les petits composants"), ("Brucelle coudée", "accéder aux zones étroites"), ("Pince à bec fin", "plier et tenir les fils"), ("Tournevis cruciforme", "vis isolées, manche jaune"), ("Tournevis plat", "vis et bornes à ressort"), ("Pince coupante", "couper les pattes au ras"), ("Extracteur de CI", "retirer un circuit DIP"), ("Loupe ×5", "inspecter les brasures"), ("Multimètre compact", "tests de continuité"), ("Bracelet ESD", "relier le poignet à la terre")]
    o = ""
    for i, (t, s) in enumerate(tools):
        x = 22 + (i % 5) * 235; y = 25 + (i // 5) * 255; cx, cy = x + 107, y + 95
        o += f'<rect x="{x}" y="{y}" width="222" height="240" rx="14" fill="{PANEL}" stroke="#d9e0ec" stroke-width="2"/>' + badge(x + 28, y + 30, i + 1, BLUE, 16)
        if i in (0, 1): o += f'<path d="M{cx-60},{cy+50} L{cx+55 if i==0 else cx+40},{cy-50 if i==0 else cy-20} L{cx+65},{cy-50 if i==0 else cy-10}" stroke="#aeb6c2" stroke-width="9" fill="none" stroke-linecap="round"/><path d="M{cx-48},{cy+50} L{cx+60 if i==0 else cx+48},{cy-50 if i==0 else cy-20}" stroke="#8a95a5" stroke-width="7" fill="none" stroke-linecap="round"/>' if False else f'<path d="M{cx-60},{cy+55} L{cx+50},{cy-55}" stroke="#aeb6c2" stroke-width="9" stroke-linecap="round"/><path d="M{cx-40},{cy+55} L{cx+60},{cy-45 if i==0 else cy-30}" stroke="#8a95a5" stroke-width="9" stroke-linecap="round"/>'
        elif i == 2 or i == 5: o += f'<path d="M{cx-50},{cy+55} L{cx},{cy-10} L{cx-12},{cy-52} M{cx+50},{cy+55} L{cx},{cy-10} L{cx+12},{cy-52}" stroke="{"#aeb6c2" if i==2 else RED}" stroke-width="12" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'
        elif i in (3, 4): o += f'<rect x="{cx-12}" y="{cy-30}" width="24" height="70" rx="10" fill="#f2c230"/><rect x="{cx-3}" y="{cy+38}" width="6" height="40" fill="#aeb6c2"/><path d="M{cx-8},{cy+78} h16" stroke="#8a95a5" stroke-width="{4 if i==3 else 10}"/>' + (f'<path d="M{cx-8},{cy+74} v8 M{cx+8},{cy+74} v8" stroke="#8a95a5" stroke-width="2"/>' if i == 3 else "")
        elif i == 6: o += f'<path d="M{cx-50},{cy+50} V{cy-10} H{cx+50} V{cy+50}" stroke="#aeb6c2" stroke-width="9" fill="none" stroke-linejoin="round"/><path d="M{cx-50},{cy+50} l-8,14 M{cx+50},{cy+50} l8,14" stroke="#8a95a5" stroke-width="5"/>'
        elif i == 7: o += f'<circle cx="{cx}" cy="{cy-8}" r="42" fill="#e7f2fb" stroke="#5d6b86" stroke-width="7"/><path d="M{cx+30},{cy+24} L{cx+62},{cy+60}" stroke="#25282e" stroke-width="12" stroke-linecap="round"/>'
        elif i == 8: o += f'<rect x="{cx-30}" y="{cy-52}" width="60" height="108" rx="10" fill="url(#yellow)" stroke="#b78300" stroke-width="2"/><rect x="{cx-22}" y="{cy-44}" width="44" height="26" rx="3" fill="#cfe3c4"/><circle cx="{cx}" cy="{cy+14}" r="16" fill="#333"/>'
        else: o += f'<rect x="{cx-45}" y="{cy-10}" width="90" height="24" rx="12" fill="#5d6b86"/><circle cx="{cx}" cy="{cy+2}" r="12" fill="#aeb6c2"/><path d="M{cx+45},{cy+2} q40,10 20,50" stroke="{GREEN}" stroke-width="3" fill="none"/>'
        o += T(cx, y + 190, t, 17, 800, INK) + T(cx, y + 214, s, 12.5, 500, MUTED)
    return figure(W, 555, o)


def sym_cell(x, y, kind, name, note, **kw):
    return f'<rect x="{x}" y="{y}" width="272" height="170" rx="12" fill="{PANEL}" stroke="#d9e0ec" stroke-width="2"/>' + g(x + 136, y + 70, kind if kind.startswith("<") else sym(kind, 0, 0, **kw)) + T(x + 136, y + 134, name, 18, 800, INK) + T(x + 136, y + 156, note, 13, 500, MUTED)


def f_sym_avances():
    o = ""
    cells = [(npn(0, 0, 0.85), "Transistor NPN", "B, C, E · flèche sortante"), (npn(0, 0, 0.85, "pnp"), "Transistor PNP", "flèche entrante"), (sym("FUSE", 0, 0), "Fusible", "protège contre les surintensités"),
             ('<rect x="-44" y="-30" width="88" height="60" fill="#fff" stroke="#1b2742" stroke-width="3"/><path d="M-70,-12 H-44 M44,-12 H70 M0,30 V52" stroke="#1b2742" stroke-width="3"/>' + T(-30, -8, "IN", 14, 800) + T(30, -8, "OUT", 14, 800) + T(0, 20, "ADJ", 12, 700, MUTED, extra=""), "Régulateur de tension", "IN, OUT, ADJ/GND"),
             (sym("CP", 0, 0), "Condensateur polarisé", "+ côté barre droite"), (g(0, 0, g(-130, -50, relais_body(), 1), 0.62), "Relais", "bobine + contact commandé"),
             (g(0, 0, g(-130, -50, opto_body(), 1), 0.62), "Optocoupleur", "LED + phototransistor"),
             ('<rect x="-34" y="-46" width="68" height="92" rx="6" fill="#fff" stroke="#1b2742" stroke-width="3"/><path d="M-18,-30 H18 M-18,-30 V-2 M18,-30 V-2 M-18,0 H18 M-18,0 V28 M18,0 V28 M-18,28 H18" stroke="#c0392b" stroke-width="5" stroke-linecap="round"/>', "Afficheur 7 segments", "7 segments commandés")]
    for i, (k, n, s) in enumerate(cells):
        x = 25 + (i % 4) * 292; y = 25 + (i // 4) * 185
        o += f'<rect x="{x}" y="{y}" width="272" height="170" rx="12" fill="{PANEL}" stroke="#d9e0ec" stroke-width="2"/>' + g(x + 136, y + 70, k) + T(x + 136, y + 138, n, 18, 800, INK) + T(x + 136, y + 160, s, 13, 500, MUTED)
    return figure(W, 400, o)


def f_schema_bp_led():
    L, Tp, B = 130, 110, 400
    o = vrun(L, Tp, B, [(255, "BAT", "5 V", {})], -1) + s_wire([(L, Tp), (900, Tp)]) + dot(300, Tp) + dot(520, Tp)
    o += vrun(300, Tp, 255, [(180, "R", "R1 10 kΩ", {})], 1, 60) + dot(300, 255) if False else ""
    o += vrun(300, Tp, 255, [(180, "R", "R1 10 kΩ", {})], 1, 52) + dot(300, 255) + s_wire([(300, 255), (300, 255)])
    o += s_wire([(300, 255), (330, 255)]) if False else ""
    o += hrun(255, 300, 520, [(410, "BP", "S1 (NO)", {"below": True})]) + dot(520, 255)
    o += vrun(520, 255, 400, [(330, "R", "R3 10 kΩ", {})], 1, 52) if False else vrun(520, 255, B, [(330, "R", "R3 10 kΩ", {})], 1, 52)
    o += hrun(255, 520, 880, [(660, "R", "R2 390 Ω", {}), (820, "LED", "D1", {"below": True})]) if False else hrun(255, 520, 900, [(650, "R", "R2 390 Ω", {}), (820, "LED", "D1 rouge", {"below": True})])
    o += s_wire([(900, 255), (900, B)]) + s_wire([(L, B), (900, B)]) + dot(520, B) + gnd(520, B) if False else s_wire([(900, 255), (900, B)]) + s_wire([(L, B), (900, B)]) + gnd(L + 300, B) + T(L + 300, B + 60, "GND", 17, 800, INK)
    o += T(300, 90, "+5 V", 17, 800, RED) + T(520, 214, "nœud", 14, 600, MUTED) + chip(600, 490, "R1 : tirage vers +5 V · R3 : pull-down vers GND · R2 limite le courant de la LED", INK, w=900, size=15)
    return figure(W, 530, o)


def f_tinkercad():
    o = ui_win(30, 30, 1140, 520, "Tinkercad Circuits — Mon circuit LED", bar="#2e8fd6")
    o = o.replace('fill="#fbfcfe"', 'fill="#f7f9fc"')
    o += f'<rect x="30" y="64" width="1140" height="48" fill="#eef2f7"/>' + f'<path d="M74,78 L74,98 L92,88 Z" fill="{GREEN}"/>' + T(104, 94, "Démarrer la simulation", 15, 700, INK, "start") + f'<rect x="300" y="78" width="20" height="20" fill="{RED}"/>' + T(330, 94, "Arrêter", 15, 700, INK, "start") + f'<rect x="970" y="74" width="130" height="32" rx="6" fill="#2e8fd6"/>' + T(1035, 95, "Partager", 15, 800, "#fff")
    o += f'<rect x="50" y="130" width="750" height="400" rx="8" fill="#fff" stroke="#d5dce8"/>' + grid_(50, 130, 750, 400)
    o += hrun(300, 150, 700, [(300, "R", "220 Ω", {}), (500, "LED", "", {})]) + s_wire([(150, 300), (150, 420), (700, 420), (700, 300)]) + g(150, 360, sym("BAT", 0, 0, rot=90))
    o += f'<rect x="820" y="130" width="330" height="400" rx="8" fill="#fff" stroke="#d5dce8"/>' + T(985, 160, "Composants", 17, 800, INK)
    for i, t in enumerate(("Basiques", "Arduino", "Instruments", "Alimentation", "Circuits intégrés")): o += f'<rect x="840" y="{180+i*44}" width="290" height="34" rx="6" fill="#eef2f7"/>' + T(860, 203 + i * 44, t, 15, 700, INK, "start") + T(1115, 203 + i * 44, "▾", 15, 700, MUTED, "end")
    o += "".join(T(x, 584, f"{n} · {t}", 14, 700, INK, "start") for x, n, t in ((60, 1, "Zone de travail"), (260, 2, "Panneau composants"), (490, 3, "Bouton simulation"), (720, 4, "Instruments"), (880, 5, "Zoom"), (990, 6, "Partager")))
    o += badge(425, 470, 1, RED, 15) + badge(1128, 160, 2, RED, 15) + badge(48, 88, 3, RED, 15) + badge(1140, 285, 4, RED, 15) + badge(770, 505, 5, RED, 15) + badge(1130, 90, 6, RED, 15)
    return figure(W, 620, o)


def grid_(x, y, w, h, st=24): return ''.join(f'<circle cx="{xx}" cy="{yy}" r="1.3" fill="#c9cfdc"/>' for xx in range(int(x + 12), int(x + w), st) for yy in range(int(y + 12), int(y + h), st))


def f_tinker_multi():
    o = ""
    for k, (x, head, disp, note, c) in enumerate(((30, "Mode voltmètre", "1,98 V", "brancher en PARALLÈLE", BLUE), (620, "Mode ampèremètre", "20,2 mA", "brancher en SÉRIE", GREEN))):
        o += panel(x, 30, 550, 420, head, accent=c) + f'<g filter="url(#sh)"><rect x="{x+190}" y="90" width="170" height="130" rx="14" fill="#2b2f36" stroke="#e2762a" stroke-width="6"/></g><rect x="{x+205}" y="105" width="140" height="56" rx="6" fill="#cfe3c4"/>' + T(x + 275, 148, disp, 34, 700, "#1d2a1a", extra='font-family="monospace"') + f'<circle cx="{x+245}" cy="190" r="9" fill="{RED}"/><circle cx="{x+305}" cy="190" r="9" fill="#111"/>'
        if k == 0:
            o += s_wire([(x + 60, 330), (x + 120, 330)]) + sym("R", x + 160, 330) + s_wire([(x + 200, 330), (x + 330, 330)]) + sym("LED", x + 370, 330) + s_wire([(x + 410, 330), (x + 490, 330)])
            o += s_wire([(x + 245, 199), (x + 245, 280), (x + 330, 280), (x + 330, 330)], RED, 4) + s_wire([(x + 305, 199), (x + 305, 250), (x + 410, 250), (x + 410, 330)], "#111", 4) + dot(x + 330, 330, 7, RED) + dot(x + 410, 330, 7, "#111")
        else:
            o += s_wire([(x + 60, 330), (x + 120, 330)]) + sym("R", x + 160, 330) + s_wire([(x + 200, 330), (x + 245, 330), (x + 245, 199)], RED, 4) + s_wire([(x + 305, 199), (x + 305, 330), (x + 330, 330)], "#111", 4) + sym("LED", x + 370, 330) + s_wire([(x + 410, 330), (x + 490, 330)])
            o += dot(x + 245, 330, 7, RED) + dot(x + 305, 330, 7, "#111") + T(x + 275, 372, "le courant passe par l'ampèremètre", 14, 700, MUTED)
        o += chip(x + 275, 410, note, c, w=360, size=17)
    return figure(W, 480, o)


def f_datasheet_annotee():
    o = f'<g filter="url(#sh)"><rect x="60" y="25" width="620" height="660" rx="6" fill="#fff" stroke="#b9c2d4" stroke-width="2"/></g>'
    o += f'<rect x="80" y="45" width="580" height="50" fill="#e8ecf5"/>' + T(100, 78, "BC547 / BC548 / BC549", 24, 800, INK, "start") + T(640, 78, "FAIRCHILD", 16, 800, MUTED, "end")
    o += T(80, 125, "NPN Epitaxial Silicon Transistor", 16, 700, INK, "start") + ''.join(f'<rect x="80" y="{140+i*10}" width="{560-i*60}" height="5" fill="#e3e8ef"/>' for i in range(3))
    o += T(80, 200, "Features", 15, 800, INK, "start") + ''.join(f'<circle cx="90" cy="{222+i*22}" r="3" fill="{INK}"/><rect x="104" y="{218+i*22}" width="{240-i*30}" height="6" fill="#e3e8ef"/>' for i in range(3))
    o += f'<rect x="80" y="300" width="360" height="110" fill="#fde8e8" stroke="{RED}"/>' + T(95, 322, "Absolute Maximum Ratings", 15, 800, RED, "start") + ''.join(f'<rect x="95" y="{336+i*16}" width="320" height="6" fill="#f3b5b5"/>' for i in range(4))
    o += f'<rect x="80" y="425" width="360" height="110" fill="#e6f5ec" stroke="{GREEN}"/>' + T(95, 447, "Electrical Characteristics", 15, 800, GREEN, "start") + ''.join(f'<rect x="95" y="{461+i*16}" width="320" height="6" fill="#b5dfc6"/>' for i in range(4))
    o += f'<rect x="460" y="195" width="180" height="150" fill="#f3f6fb" stroke="#b9c2d4"/>' + g(550, 275, '<path d="M-30,0 L-30,-30 Q-30,-56 0,-56 Q30,-56 30,-30 L30,0 Z" fill="#222"/><rect x="-22" y="0" width="5" height="26" fill="#c9cfd8"/><rect x="-2" y="0" width="5" height="26" fill="#c9cfd8"/><rect x="18" y="0" width="5" height="26" fill="#c9cfd8"/>', 1.1) + T(550, 335, "TO-92 : brochage", 12, 700, MUTED)
    o += f'<rect x="460" y="360" width="180" height="175" fill="#f3f6fb" stroke="#b9c2d4"/><polyline points="475,520 520,470 560,420 600,395 630,385" stroke="{BLUE}" stroke-width="3" fill="none"/>' + T(550, 380, "courbes", 12, 700, MUTED)
    o += f'<rect x="80" y="555" width="560" height="110" fill="#f6f8fc"/>' + ''.join(f'<rect x="90" y="{570+i*20}" width="{520-i*40}" height="6" fill="#e3e8ef"/>' for i in range(4))
    marks = [(120, 70, "En-tête : référence, fabricant"), (120, 130, "Description générale"), (120, 225, "Caractéristiques clés"), (420, 330, "Absolute Maximum Ratings : limites à ne jamais dépasser"), (420, 455, "Electrical Characteristics : valeurs typiques"), (620, 270, "Brochage du boîtier"), (620, 440, "Courbes caractéristiques")]
    ys = [60, 130, 215, 335, 470, 270, 400]
    for n, ((px, py, t), y) in enumerate(zip(marks, ys), 1):
        o += badge(710, y, n, BLUE, 15) + T(738, y + 6, t, 15, 700, INK, "start") + f'<line x1="{px if n < 6 else 640}" y1="{py}" x2="695" y2="{y}" stroke="{BLUE}" stroke-width="1.5" opacity=".6"/>'
    return figure(W, 710, o)


def f_ratings():
    rows = [("Collector-Base Voltage", "V_CBO", "50", "V", "tension collecteur–base maximale"), ("Collector-Emitter Voltage", "V_CEO", "45", "V", "tension collecteur–émetteur maximale"), ("Emitter-Base Voltage", "V_EBO", "6", "V", "tension émetteur–base maximale"), ("Collector Current", "I_C", "100", "mA", "courant maximal dans le collecteur"), ("Power Dissipation", "P_D", "500", "mW", "puissance maximale dissipée"), ("Junction Temperature", "T_J", "150", "°C", "température maximale de jonction")]
    o = f'<rect x="30" y="30" width="1140" height="50" fill="#d9534f"/>' + T(60, 63, "Absolute Maximum Ratings — BC547", 21, 800, "#fff", "start")
    ws = [330, 120, 110, 100]; x0 = 30; cx = x0
    for h, w in zip(("Parameter", "Symbol", "Value", "Unit"), ws): o += f'<rect x="{cx}" y="80" width="{w}" height="40" fill="#f3d3d1" stroke="#e1b6b3"/>' + T(cx + w / 2, 107, h, 16, 800, "#8a2a27"); cx += w
    o += f'<rect x="{x0+sum(ws)}" y="80" width="{1140-sum(ws)}" height="40" fill="#e8f0ff"/>' + T(x0 + sum(ws) + (1140 - sum(ws)) / 2, 107, "En français", 16, 800, BLUE)
    for r, row in enumerate(rows):
        y = 120 + r * 62; cx = x0
        for k, (v, w) in enumerate(zip(row[:4], ws)):
            o += f'<rect x="{cx}" y="{y}" width="{w}" height="62" fill="{"#fff" if r%2==0 else "#f1f3f7"}" stroke="#d5dce8"/>' + T(cx + w / 2 if k else cx + 14, y + 38, v.replace("_", ""), 16, 700 if k else 600, INK, "middle" if k else "start"); cx += w
        o += f'<rect x="{x0+sum(ws)}" y="{y}" width="{1140-sum(ws)}" height="62" fill="#f4f8ff" stroke="#d5dce8"/>' + arrow(x0 + sum(ws) + 18, y + 31, x0 + sum(ws) + 70, y + 31, BLUE, 3) + T(x0 + sum(ws) + 90, y + 38, row[4], 16, 600, BLUE, "start")
    o += chip(600, 535, "À ne jamais dépasser : au-delà, le composant est détruit", RED, w=640, size=17)
    return figure(W, 575, o)


def f_schema_transistor():
    o = vcc(330, 120, "+5 V") + s_wire([(330, 120), (330, 130), (330, 150)]) + vrun(330, 150, 262, [(205, "R", "", {})], 1, 0) + ""
    o = vcc(330, 100, "+5 V") + s_wire([(330, 100), (330, 120)])
    o += vrun(330, 120, 195, [(160, "R", "R_C = 150 Ω", {})], 1, 52)
    o += vrun(330, 195, 250, [(230, "LED", "D1 rouge", {})], 1, 58) if False else vrun(330, 195, 262, [(228, "LED", "D1 rouge", {})], 1, 58)
    o += npn(330 + 50 + 0, 330, 1.0) if False else ""
    o += s_wire([(330, 262), (330, 275), (372, 275), (372, 290)])
    o += npn(330, 335, 1.0) if False else npn(350, 335, 1.0)
    # collecteur de Q1 en (372, 291), émetteur en (372, 379), base en (300, 335)
    o += s_wire([(372, 379), (372, 430)]) + gnd(372, 430) + T(372, 490, "GND", 17, 800, INK)
    o += hrun(335, 80, 300, [(190, "R", "R_B = 10 kΩ", {})]) + T(80, 380, "Entrée Arduino (5 V)", 16, 700, INK, "start")
    o += T(440, 335, "Q1 = BC547 (NPN)", 18, 800, INK, "start") + T(440, 296, "C", 18, 800, MUTED, "start") + T(440, 380, "E", 18, 800, MUTED, "start") + T(285, 360, "B", 18, 800, MUTED)
    o += chip(900, 160, "I_C = (5 − 2) / 150 = 20 mA", BLUE, w=380, size=17) + chip(900, 215, "I_B = (5 − 0,7) / 10 000 ≈ 0,43 mA", GREEN, w=420, size=17) + chip(900, 270, "Le transistor commande un courant 47 fois plus grand", INK, w=520, size=15)
    return figure(W, 530, o)


FIGS = {"pyramide_maintenance": f_pyr_maint, "preventive_corrective": f_prev_corr, "outils_nettoyage": f_outils_nettoyage, "grille_diagnostic_visuel": f_grille_diag, "esd_phenomene": f_esd,
        "esd_dommage": f_esd_dommage, "poste_esd": f_poste_esd, "outils_technicien": f_outils_techno, "symboles_avances": f_sym_avances, "schema_bp_led": f_schema_bp_led,
        "tinkercad_interface": f_tinkercad, "tinkercad_multimetre": f_tinker_multi, "datasheet_annotee": f_datasheet_annotee, "ratings_bc547": f_ratings, "schema_transistor_led": f_schema_transistor}
