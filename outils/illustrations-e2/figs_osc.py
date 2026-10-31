"""Figures des fiches oscilloscopes (schémas : Rigol DS1104Z, déclenchement)."""
import math
from lib import *
from figs_essentiel import cl, grat, _wave, knob

W = 1200


def key(x, y, w, h, txt, fill="#e9eef7", col=INK, size=15):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{fill}" stroke="{col}" stroke-width="2.5"/>' + T(x + w / 2, y + h / 2 + size * 0.35, txt, size, 800, col)


def f_declenchement():
    o = panel(30, 30, 1140, 520, "Le déclenchement : où l'écran « démarre » le tracé", accent=RED)
    x0, y0, w, h = 70, 110, 620, 300
    o += f'<rect x="{x0}" y="{y0}" width="{w}" height="{h}" rx="10" fill="#0f1b2f"/>'
    sine = lambda t: math.sin(2 * math.pi * 3.1 * t)
    o += _wave(x0 + 10, y0 + 10, w - 20, h - 20, sine, "#ffd34d")
    yl = y0 + h / 2 - 0.45 * (h - 20) / 2
    o += f'<line x1="{x0}" y1="{yl}" x2="{x0+w}" y2="{yl}" stroke="{RED}" stroke-width="3.5" stroke-dasharray="10 7"/>' + f'<rect x="{x0+w-220}" y="{y0+h-44}" width="206" height="30" rx="8" fill="#16253f"/>' + T(x0 + w - 117, y0 + h - 23, "niveau de déclenchement", 15, 800, "#ff8a8a")
    # points de déclenchement (montée)
    for k in range(3):
        t = (k + 0.0 + math.asin(0.45) / (2 * math.pi)) / 3.1
        xp = x0 + 10 + (w - 20) * t
        o += f'<circle cx="{xp:.0f}" cy="{yl:.0f}" r="8" fill="{GREEN}" stroke="#fff" stroke-width="2.5"/>'
    o += T(x0 + w / 2, y0 + h + 34, "Le tracé démarre à chaque franchissement du niveau", 17, 800, INK) + T(x0 + w / 2, y0 + h + 62, "dans le sens choisi (ici : pente montante ↗)", 17, 700, INK)
    # panneau pédagogique
    o += T(740, 130, "Les 4 réglages à connaître", 22, 800, INK, "start")
    items = [("Source", "la voie dont on surveille le signal"), ("Niveau", "la tension à franchir (bouton LEVEL)"), ("Pente", "montante ↗ ou descendante ↘"), ("Mode", "Auto, Normal ou Single")]
    for i, (a, b) in enumerate(items):
        yy = 175 + i * 62
        o += cl(740, yy, a, [BLUE, RED, GREEN, AMBER][i], w=110, size=17) + T(868, yy + 6, b, 17, 600, INK, "start")
    o += T(740, 440, "Image qui défile ou tremble ?", 19, 800, RED, "start") + T(740, 470, "Niveau hors du signal, mauvaise source,", 17, 600, INK, "start") + T(740, 494, "ou mode Normal sans déclenchement.", 17, 600, INK, "start")
    return figure(W, 570, o)


FIGS = {"osc_declenchement": f_declenchement}
