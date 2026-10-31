"""Première S02 : schémas KiCad (trois moyens de connexion...)."""
from lib import *

W = 1200
WG, SY = "#1f9d4a", "#a33"   # fil vert, symboles rouge brique (palette KiCad)


def _ic(x, y, w, h, name, pins):
    """Boîtier simple : rectangle rouge brique, broches (nom, côté, y)."""
    o = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="4" fill="#fff8e6" stroke="{SY}" stroke-width="3"/>' + T(x + w / 2, y + 22, name, 16, 800, "#7a2a2a")
    for nm, side, py in pins:
        px = x if side == "L" else x + w
        o += f'<line x1="{px-14 if side=="L" else px}" y1="{py}" x2="{px if side=="L" else px+14}" y2="{py}" stroke="{SY}" stroke-width="3"/>'
        o += T(px + (10 if side == "L" else -10), py + 5, nm, 13, 700, "#7a2a2a", "start" if side == "L" else "end")
    return o


def f_kicad_connexions():
    o = ""
    heads = (("1 · Le fil (Wire)", "touche W", BLUE), ("2 · Étiquette (Net Label)", "touche L", GREEN), ("3 · Symbole d'alimentation", "touche P", AMBER))
    for k, (h, key, col) in enumerate(heads):
        ox = 30 + k * 390
        o += panel(ox, 40, 360, 440, h, accent=col)
        o += chip(ox + 180, 108, key, col, w=130, size=15)
    # 1 : fil
    ox = 30
    o += _ic(ox + 20, 190, 100, 90, "U1", [("1", "R", 235)]) + _ic(ox + 240, 190, 100, 90, "U2", [("2", "L", 235)])
    o += f'<path d="M{ox+134},235 H{ox+226}" stroke="{WG}" stroke-width="5"/><circle cx="{ox+134}" cy="235" r="5" fill="#fff" stroke="{WG}" stroke-width="3"/><circle cx="{ox+226}" cy="235" r="5" fill="#fff" stroke="{WG}" stroke-width="3"/>'
    o += T(ox + 180, 215, "fil (vert)", 15, 800, WG)
    o += T(ox + 180, 330, "Connexion visible entre", 16, 700, INK) + T(ox + 180, 352, "deux broches proches", 16, 700, INK)
    o += chip(ox + 180, 420, "Le fil se termine EXACTEMENT sur une broche", RED, w=320, size=13)
    # 2 : étiquette
    ox = 420
    o += _ic(ox + 20, 170, 90, 70, "U1", [("1", "R", 205)]) + _ic(ox + 250, 330, 90, 70, "U2", [("2", "L", 365)])
    o += f'<path d="M{ox+124},205 H{ox+200}" stroke="{WG}" stroke-width="5"/>' + T(ox + 205, 199, "NET_SIGNAL", 14, 800, "#0a6a8a", "start")
    o += f'<path d="M{ox+236},365 H{ox+160}" stroke="{WG}" stroke-width="5"/>' + T(ox + 155, 359, "NET_SIGNAL", 14, 800, "#0a6a8a", "end")
    o += f'<path d="M{ox+250},230 V300" stroke="{INK}" stroke-width="2" stroke-dasharray="3 7" opacity=".0"/>'
    o += T(ox + 180, 290, "… ailleurs sur le schéma …", 15, 600, MUTED)
    o += chip(ox + 180, 440, "Même nom = même nœud, sans fil", GREEN, w=320, size=14)
    # 3 : alimentation
    ox = 810
    for x in (ox + 100, ox + 260):
        o += f'<path d="M{x-24},170 H{x+24}" stroke="{SY}" stroke-width="4"/><path d="M{x},170 V190" stroke="{SY}" stroke-width="3"/>' + T(x, 158, "+5V", 16, 800, "#1d5fd1")
        o += s_wire([(x, 190), (x, 210)]) + sym("R", x, 250, 90) + s_wire([(x, 290), (x, 330)]) + gnd(x, 330) + T(x + 36, 256, "R1" if x < ox + 200 else "R2", 15, 800, INK, "start")
    o += T(ox + 180, 380, "Tous les composants reliés au même", 15, 700, INK) + T(ox + 180, 402, "symbole sont reliés ensemble", 15, 700, INK)
    o += chip(ox + 180, 446, "Pas besoin de fil entre les deux +5V", AMBER, w=320, size=13)
    return figure(W, 520, o)


FIGS = {"kicad_trois_connexions": f_kicad_connexions}
