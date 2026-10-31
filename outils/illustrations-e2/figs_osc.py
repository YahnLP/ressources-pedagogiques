"""Figures des fiches oscilloscopes (schémas : Rigol DS1104Z, déclenchement)."""
import math
from lib import *
from figs_essentiel import cl, grat, _wave, knob

W = 1200


def key(x, y, w, h, txt, fill="#e9eef7", col=INK, size=15):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{fill}" stroke="{col}" stroke-width="2.5"/>' + T(x + w / 2, y + h / 2 + size * 0.35, txt, size, 800, col)


def f_rigol_panneau():
    o = panel(30, 30, 1140, 640, "RIGOL DS1104Z Plus : les zones de la face avant (schéma)", accent=BLUE)
    # écran
    o += f'<rect x="60" y="100" width="500" height="340" rx="10" fill="#0f1b2f" stroke="{INK}" stroke-width="4"/>'
    o += T(310, 280, "Écran", 30, 800, "#9fb3d1")
    o += T(310, 318, "affichage des voies, des mesures et des menus", 17, 600, "#7f95b8")
    for i in range(6):
        o += key(70 + i * 80, 458, 68, 34, f"F{i+1}", fill="#fff", size=15)
    o += T(310, 520, "Touches de menu (sous l'écran) : leur rôle change à chaque menu", 17, 700, MUTED)
    # multifonction
    o += knob(190, 585, 34, "Bouton multifonction")
    o += key(300, 560, 120, 40, "Menu off", fill="#fff")
    # menus de fonction
    o += panel(600, 90, 540, 130, "Menus", accent=AMBER)
    for i, n in enumerate(["Measure", "Acquire", "Storage", "Cursor", "Display", "Utility"]):
        o += key(615 + (i % 3) * 175, 140 + (i // 3) * 40, 160, 34, n)
    # commandes d'exécution
    o += panel(600, 235, 540, 90, "Exécution", accent=GREEN)
    for i, (n, c) in enumerate([("CLEAR", "#fff"), ("AUTO", "#d6f5e3"), ("RUN/STOP", "#ffd9d9"), ("SINGLE", "#fff")]):
        o += key(615 + i * 131, 275, 120, 38, n, fill=c)
    # vertical
    o += panel(600, 340, 300, 320, "Vertical", accent=BLUE)
    for i, (n, c) in enumerate([("CH1", "#ffe68a"), ("CH2", "#a8ecf2"), ("CH3", "#f2b4e6"), ("CH4", "#b5ccff")]):
        o += key(615 + i * 68, 395, 60, 36, n, fill=c)
    o += key(615, 440, 90, 32, "MATH") + key(715, 440, 90, 32, "REF") + key(815, 440, 70, 32, "LA*")
    o += knob(690, 545, 38, "POSITION") + knob(820, 545, 38, "SCALE")
    o += T(750, 645, "Un seul jeu de boutons : il agit sur la voie choisie", 14, 700, MUTED)
    # horizontal
    o += panel(915, 340, 225, 165, "Horizontal", accent=BLUE)
    o += key(930, 392, 80, 30, "MENU") + knob(965, 450, 22, "POSITION") + knob(1075, 440, 28, "SCALE")
    # trigger
    o += panel(915, 515, 225, 145, "Déclenchement", accent=RED)
    o += key(930, 565, 64, 30, "MODE", size=13) + key(1004, 565, 64, 30, "MENU", size=13) + key(930, 607, 80, 30, "FORCE", size=13) + knob(1100, 598, 22, "LEVEL")
    o += T(1000, 648, "50 % : Trigger > Menu", 12, 700, MUTED, "middle") if False else ""
    o += T(310, 655, "* LA : voies logiques (modèles MSO ou option)", 14, 600, MUTED) if False else ""
    return figure(W, 700, o)


def f_rigol_ecran():
    o = panel(30, 30, 1140, 620, "RIGOL DS1000Z : lire l'écran (schéma d'après le manuel)", accent=BLUE)
    x0, y0, cw = 60, 120, 54
    o += grat(x0, y0, cw, 12, 8)
    cy = y0 + 4 * cw
    pts = " ".join(f"{x0 + i*3:.1f},{cy - 1.4*cw*math.sin(2*math.pi*i*3/(4*cw)):.1f}" for i in range(0, int(12*cw/3) + 1))
    o += f'<polyline points="{pts}" fill="none" stroke="#ffd34d" stroke-width="5"/>'
    # barre du haut
    o += f'<rect x="{x0}" y="{y0-34}" width="{12*cw}" height="30" rx="6" fill="#16253f"/>'
    o += T(x0 + 12, y0 - 13, "RIGOL", 15, 800, "#fff", "start") + f'<rect x="{x0+80}" y="{y0-29}" width="62" height="22" rx="4" fill="#2bb673"/>' + T(x0 + 111, y0 - 13, "AUTO", 14, 800, "#fff")
    o += T(x0 + 175, y0 - 13, "H 500 µs", 14, 800, "#9fd4ff", "start") + T(x0 + 290, y0 - 13, "1GSa/s  24kpts", 14, 800, "#9fd4ff", "start") + T(x0 + 460, y0 - 13, "T⊕ 0,00 s", 14, 800, "#9fd4ff", "start") + T(x0 + 12*cw - 12, y0 - 13, "f 1,000 kHz", 14, 800, "#ffd34d", "end")
    # bas : voies
    o += f'<rect x="{x0}" y="{y0+8*cw+6}" width="{12*cw}" height="34" rx="6" fill="#16253f"/>'
    o += f'<rect x="{x0+10}" y="{y0+8*cw+12}" width="130" height="22" rx="4" fill="#ffd34d"/>' + T(x0 + 75, y0 + 8 * cw + 28, "1  DC  1,00 V", 14, 800, "#16253f")
    o += f'<rect x="{x0+160}" y="{y0+8*cw+12}" width="130" height="22" rx="4" fill="#3fc8d6"/>' + T(x0 + 225, y0 + 8 * cw + 28, "2  AC  500 mV", 14, 800, "#16253f")
    o += f'<rect x="{x0+12*cw-190}" y="{y0+8*cw+12}" width="180" height="22" rx="4" fill="#fff"/>' + T(x0 + 12 * cw - 100, y0 + 8 * cw + 28, "Edge  1 ↗  0,00 V", 14, 800, "#16253f")
    # marqueurs
    o += f'<polygon points="{x0-14},{cy-8} {x0},{cy} {x0-14},{cy+8}" fill="#ffd34d"/>' + T(x0 - 22, cy + 5, "1", 14, 800, "#ffd34d", "end")
    xc = x0 + 6 * cw
    o += f'<polygon points="{xc-8},{y0-2} {xc+8},{y0-2} {xc},{y0+12}" fill="#ff8a3d"/>'
    # légendes
    def lg(n, x, y, text):
        return badge(x, y, n, RED, 14) + T(x + 22, y + 6, text, 17, 700, INK, "start")
    o += lg(1, 868, 150, "État du déclenchement")
    o += lg(2, 868, 195, "Base de temps (H)")
    o += lg(3, 868, 240, "Échantillonnage et mémoire")
    o += lg(4, 868, 285, "Décalage du déclenchement")
    o += lg(5, 868, 330, "Voie, couplage et sensibilité")
    o += lg(6, 868, 375, "Type, source, pente, niveau")
    o += lg(7, 868, 420, "Repère du zéro de la voie")
    o += lg(8, 868, 465, "Fréquence du signal")
    o += "".join(badge(x, y, n, RED, 14) for x, y, n in [(x0 + 100, y0 - 44, 1), (x0 + 232, y0 - 44, 2), (x0 + 360, y0 - 44, 3), (x0 + 480, y0 - 44, 4), (x0 + 12 * cw - 12, y0 - 44, 8)])
    o += badge(x0 + 75, y0 + 8 * cw + 60, 5, RED, 14) + badge(x0 + 12 * cw - 100, y0 + 8 * cw + 60, 6, RED, 14) + badge(x0 - 28, cy - 24, 7, RED, 14)
    o += T(310, 560, "Aspect indicatif : vérifie la disposition exacte sur ton appareil.", 15, 600, MUTED) if False else ""
    return figure(W, 690, o)


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


FIGS = {"osc_rigol_panneau": f_rigol_panneau, "osc_rigol_ecran": f_rigol_ecran, "osc_declenchement": f_declenchement}
