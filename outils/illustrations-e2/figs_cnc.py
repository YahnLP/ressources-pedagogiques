"""Seconde S11 : fraisage CNC 3018 (chaîne KiCad -> fraise, isolation, miroir)."""
from lib import *
from figs07 import block
import math

W = 1200
CU = "#d9a066"
FR4 = "#2f9e5e"


def f_cnc_chaine():
    o = ""
    items = [("KiCad", "circuit imprimé", BLUE), ("Gerber", ".gbr + .drl", BLUE), ("FlatCAM", "trajets d'outil", AMBER), ("G-code", "fichier .nc", AMBER), ("Candle", "pilotage GRBL", GREEN), ("CNC 3018", "fraisage", GREEN)]
    for i, (t, sub, c) in enumerate(items):
        x = 30 + i * 190
        o += block(x, 90, 150, 120, t, sub, c) + badge(x + 14, 90, i + 1, c, 14)
        if i < len(items) - 1:
            o += arrow(x + 154, 150, x + 186, 150, INK, 3)
    o += T(600, 60, "De KiCad à la fraiseuse : la chaîne complète", 24, 800, INK)
    o += T(205, 250, "CONCEVOIR", 16, 800, BLUE) + T(585, 250, "PRÉPARER (CAM)", 16, 800, AMBER) + T(965, 250, "FRAISER", 16, 800, GREEN)
    o += chip(205, 320, "Fraise en V 30° · pointe 0,1 mm : pistes", BLUE, w=340, size=15) + chip(585, 320, "Foret 0,8 mm : trous", AMBER, w=340, size=15) + chip(965, 320, "Fraise Ø 1 mm : contour", GREEN, w=340, size=15)
    o += T(600, 390, "1  isolation des pistes   →   2  perçage   →   3  découpe du contour", 20, 800, INK)
    o += chip(600, 450, "La fraise ne grave pas les pistes : elle ENLÈVE le cuivre tout autour (isolation).", RED, w=1000, size=17)
    return figure(W, 500, o)


def f_cnc_isolation():
    o = panel(30, 40, 540, 440, "Vue de dessus : la fraise isole les pistes", accent=BLUE)
    o += f'<rect x="60" y="110" width="480" height="340" rx="10" fill="{CU}" stroke="#a8743d" stroke-width="3"/>'
    gv = "#1f4d34"
    o += f'<rect x="100" y="170" width="340" height="64" rx="32" fill="none" stroke="{gv}" stroke-width="10"/>'
    o += f'<circle cx="130" cy="202" r="12" fill="#2b2b2b"/>' + T(270, 210, "piste (reliée au circuit)", 17, 800, "#5a3a14")
    o += f'<circle cx="440" cy="340" r="46" fill="none" stroke="{gv}" stroke-width="10"/><circle cx="440" cy="340" r="12" fill="#2b2b2b"/>' + T(440, 410, "pastille", 16, 800, "#5a3a14")
    o += f'<path d="M300,262 V340 H394" fill="none" stroke="{gv}" stroke-width="10"/>' if False else ""
    o += T(150, 340, "cuivre inutile", 17, 800, "#5a3a14") + T(150, 364, "(isolé, relié à rien)", 15, 600, "#5a3a14")
    o += T(300, 470, "rainure fraisée (sombre) = isolation", 15, 700, gv)
    o += panel(600, 40, 570, 440, "Coupe : largeur de la rainure", accent=GREEN)
    # coupe (échelle : 1 mm = 450 px)
    cx, ytop = 885, 330
    o += f'<rect x="630" y="{ytop+14}" width="510" height="70" fill="{FR4}"/>' + T(1085, ytop + 66, "FR4 1,6 mm", 14, 700, "#fff", "end")
    gl, gr = cx - 34.5, cx + 34.5
    o += f'<rect x="630" y="{ytop}" width="{gl-630:.0f}" height="14" fill="{CU}"/><rect x="{gr:.0f}" y="{ytop}" width="{1140-gr:.0f}" height="14" fill="{CU}"/>'
    o += f'<polygon points="{gl:.1f},{ytop} {gr:.1f},{ytop} {cx+22.5},{ytop+59} {cx-22.5},{ytop+59}" fill="#f4f7fb"/>'
    o += f'<polygon points="{cx-22.5},{ytop+59} {cx+22.5},{ytop+59} {cx+54.9:.1f},{ytop-82} {cx-54.9:.1f},{ytop-82}" fill="#9aa7b8" stroke="#6b7a90" stroke-width="2"/>'
    o += f'<rect x="{cx-54.9:.0f}" y="{ytop-130}" width="110" height="48" fill="#b9c3d1" stroke="#6b7a90" stroke-width="2"/>' + T(cx + 80, ytop - 98, "fraise en V 30°", 16, 800, INK, "start")
    o += T(cx + 80, ytop - 76, "(angle total 30°)", 14, 600, MUTED, "start")
    o += f'<line x1="{gl:.0f}" y1="{ytop+80}" x2="{gl:.0f}" y2="{ytop+110}" stroke="{INK}" stroke-width="2"/><line x1="{gr:.0f}" y1="{ytop+80}" x2="{gr:.0f}" y2="{ytop+110}" stroke="{INK}" stroke-width="2"/>'
    o += arrow(gl, ytop + 100, gr, ytop + 100, RED, 3) + arrow(gr, ytop + 100, gl, ytop + 100, RED, 3) + T(cx, ytop + 132, "D ≈ 0,15 mm", 18, 800, RED)
    o += T(1000, ytop + 36, "p = 0,1 mm", 16, 800, GREEN, "start") + arrow(985, ytop + 14, 985, ytop + 59, GREEN, 3) if False else ""
    o += T(1010, ytop + 32, "p", 18, 800, GREEN) + f'<line x1="1000" y1="{ytop}" x2="1000" y2="{ytop+59}" stroke="{GREEN}" stroke-width="3"/>' + T(1020, ytop + 36, "= profondeur", 14, 700, GREEN, "start") if False else ""
    o += T(gl - 20, ytop + 40, "p = 0,1 mm", 15, 800, "#fff", "end") + f'<line x1="{gl-12:.0f}" y1="{ytop}" x2="{gl-12:.0f}" y2="{ytop+59}" stroke="#fff" stroke-width="3"/>'
    o += chip(885, 450, "D = pointe + 2 × p × tan(15°) = 0,1 + 2 × 0,1 × 0,27 ≈ 0,15 mm", INK, w=540, size=15)
    return figure(W, 520, o)


def _board(x, y, mirror):
    w, h = 260, 150
    cx = x + w / 2
    b = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{FR4}" stroke="#1f6b3f" stroke-width="3"/>'
    b += f'<rect x="{x+22}" y="{y+22}" width="70" height="40" rx="4" fill="{CU}"/><circle cx="{x+34}" cy="{y+34}" r="5" fill="#2b2b2b"/>' + T(x + 57, y + 56, "", 10, 800, INK)
    b += f'<path d="M{x+92},{y+42} H{x+190} V{y+110}" fill="none" stroke="{CU}" stroke-width="10" stroke-linecap="round"/>'
    b += f'<text x="{x+120}" y="{y+128}" font-size="54" font-weight="800" fill="#fff" text-anchor="middle">R</text>'
    if mirror:
        return f'<g transform="translate({2*cx},0) scale(-1,1)">{b}</g>'
    return b


def f_cnc_miroir():
    o = ""
    rows = (("Cuivre sur F.Cu\n(face avant)", False, "PAS de miroir", GREEN, 40), ("Cuivre sur B.Cu\n(face arrière)\ncas du traversant", True, "MIROIR obligatoire", RED, 280))
    for lab, mir, verdict, col, y in rows:
        o += f'<rect x="30" y="{y}" width="1140" height="220" rx="16" fill="{PANEL}" stroke="#d9e0ec" stroke-width="2"/>'
        o += T(50, y + 80, lab, 20, 800, INK, "start")
        o += T(410, y + 40, "dans KiCad (vue de dessus)", 15, 700, MUTED) + _board(280, y + 58, False)
        o += arrow(565, y + 133, 625, y + 133, col, 5)
        o += T(770, y + 40, "sur la fraiseuse, cuivre vers le HAUT", 15, 700, MUTED) + _board(640, y + 58, mir)
        o += chip(1045, y + 133, verdict, col, w=200, size=16)
    return figure(W, 540, o)


FIGS = {"cnc_chaine": f_cnc_chaine, "cnc_isolation": f_cnc_isolation, "cnc_miroir": f_cnc_miroir}
