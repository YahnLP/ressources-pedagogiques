"""Figures des cours de Seconde (nouveaux cours E2)."""
from lib import *

W = 1200
SERIF = 'font-family="Liberation Serif, DejaVu Serif, Times New Roman, serif" font-style="italic"'


def mtext(x, y, s, size=40, anchor="middle", fill=INK, italic=True):
    st = SERIF if italic else 'font-family="Liberation Serif, DejaVu Serif, serif"'
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{fill}" text-anchor="{anchor}" {st}>{esc(s)}</text>'


def frac(x, y, num, den, size=40, fill=INK):
    w = max(len(num), len(den)) * size * 0.55 + 14
    return (mtext(x, y - size * 0.32, num, size, fill=fill) + f'<line x1="{x-w/2}" y1="{y-size*0.22}" x2="{x+w/2}" y2="{y-size*0.22}" stroke="{fill}" stroke-width="3"/>'
            + mtext(x, y + size * 0.72, den, size, fill=fill)), w


def formula(cx, y, lhs, rhs, size=42):
    """lhs = rhs  où rhs est 'A × B' ou ('A','B') pour une fraction. Retourne le svg centré."""
    if isinstance(rhs, tuple):
        fr, fw = frac(0, 0, rhs[0], rhs[1], size)
        lw = len(lhs) * size * 0.6 + 20
        total = lw + 40 + 28 + fw
        x0 = cx - total / 2
        return (mtext(x0 + lw / 2, y, lhs, size) + mtext(x0 + lw + 20, y, "=", size, "middle", italic=False) + f'<g transform="translate({x0 + lw + 20 + 28 + fw/2},{y})">{fr}</g>')
    return mtext(cx, y, f"{lhs} = {rhs}", size)


def wheel(cx, cy, r, top, left, right, hide, colors):
    """Triangle mnémotechnique : lettre 'top' en haut, 'left' en bas à gauche, 'right' en bas à droite ; 'hide' = lettre cachée."""
    o = ""
    w, H = r * 1.25, r * 2.0
    A = (cx, cy - H * 0.55); BL = (cx - w, cy + H * 0.45); BR = (cx + w, cy + H * 0.45)
    ML = ((A[0] + BL[0]) / 2, (A[1] + BL[1]) / 2); MR = ((A[0] + BR[0]) / 2, (A[1] + BR[1]) / 2)
    M = (cx, ML[1]); MB = (cx, BL[1])
    def sector(pts, key, lab, tx, ty):
        c = "#cfd5df" if key == hide else colors[key]
        p = "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts) + " Z"
        s = f'<path d="{p}" fill="{c}" stroke="#fff" stroke-width="5" stroke-linejoin="round"/>'
        s += mtext(tx, ty, "?" if key == hide else lab, 52, fill="#6b7587" if key == hide else INK, italic=False if key == hide else True)
        return s
    o += f'<path d="M{A[0]},{A[1]} L{BR[0]},{BR[1]} L{BL[0]},{BL[1]} Z" fill="#000" opacity=".05" transform="translate(0,3)"/>'
    o += sector([A, MR, ML], top, top, cx, A[1] + (ML[1] - A[1]) * 0.78)
    o += sector([ML, M, MB, BL], left, left, cx - w * 0.5, ML[1] + (BL[1] - ML[1]) * 0.62)
    o += sector([M, MR, BR, MB], right, right, cx + w * 0.5, ML[1] + (BL[1] - ML[1]) * 0.62)
    return o


def f_wheels(letters, names, units, ttl, fname_forms):
    top, left, right = letters
    colors = {top: "#ef6a73", left: "#8fd0ea", right: "#f6de6a"}
    o = ""
    order = [(top, f"Chercher {names[top]}"), (right, f"Chercher {names[right]}"), (left, f"Chercher {names[left]}")]
    chipcol = {top: "#e0525c", right: "#e8c53a", left: "#59b6dc"}
    for i, (h, label) in enumerate(order):
        x = 30 + i * 390
        o += f'<rect x="{x}" y="30" width="360" height="520" rx="18" fill="#fff" stroke="#dde4f0" stroke-width="2.5"/>'
        o += f'<rect x="{x}" y="30" width="360" height="56" rx="18" fill="{colors[h]}"/><rect x="{x}" y="60" width="360" height="26" fill="{colors[h]}"/>'
        o += T(x + 180, 66, label, 24, 800, INK)
        o += wheel(x + 180, 220, 120, top, left, right, h, colors)
        lhs, rhs = fname_forms[h]
        o += formula(x + 180, 440, lhs, rhs, 44)
        o += T(x + 180, 515, units[h], 17, 600, MUTED)
    return figure(W, 580, o)


def f_ohm():
    names = {"U": "la tension", "I": "l'intensité", "R": "la résistance"}
    forms = {"U": ("U", "R × I"), "I": ("I", ("U", "R")), "R": ("R", ("U", "I"))}
    units = {"U": "U : tension en volts (V)", "I": "I : intensité en ampères (A)", "R": "R : résistance en ohms (Ω)"}
    return f_wheels(("U", "R", "I"), names, units, "Loi d'Ohm", forms)


def f_puissance():
    names = {"P": "la puissance", "U": "la tension", "I": "l'intensité"}
    forms = {"P": ("P", "U × I"), "U": ("U", ("P", "I")), "I": ("I", ("P", "U"))}
    units = {"P": "P : puissance en watts (W)", "U": "U : tension en volts (V)", "I": "I : intensité en ampères (A)"}
    return f_wheels(("P", "U", "I"), names, units, "Puissance", forms)


def f_eau():
    BL = "#2b8fd6"
    o = panel(30, 30, 520, 540, "Circuit d'eau", accent=BL) + panel(650, 30, 520, 540, "Circuit électrique", accent=AMBER)
    # --- eau : boucle fermée
    pipe = lambda d, w=12: f'<path d="{d}" fill="none" stroke="{BL}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"/>'
    o += pipe("M110,320 V230 H210", 12) + pipe("M210,230 H320", 4) + pipe("M320,230 H470 V320", 12) + pipe("M470,400 V490 H110 V370", 12)
    o += f'<g transform="translate(110,170)"><path d="M-44,-42 H44 L36,28 H-36Z" fill="#7cc4f0" stroke="{BL}" stroke-width="4"/><path d="M-37,-6 Q-18,-16 0,-6 T37,-6 V28 H-36Z" fill="#4aa8e3" opacity=".7"/></g>'
    o += T(110, 112, "Château d'eau", 17, 700, INK)
    o += f'<circle cx="110" cy="345" r="30" fill="#e9f3fb" stroke="{BL}" stroke-width="4"/>' + arrow(95, 345, 126, 345, BL, 5) + T(110, 405, "Pompe", 17, 700, INK)
    o += T(265, 205, "tuyau étroit", 16, 700, INK) + T(265, 258, "(frein à l'écoulement)", 14, 500, MUTED)
    o += f'<g transform="translate(470,360)"><circle r="40" fill="#fff" stroke="{BL}" stroke-width="4"/><path d="M0,-28 L11,0 L0,28 L-11,0Z M-28,0 L0,-11 L28,0 L0,11Z" fill="#7cc4f0" stroke="{BL}" stroke-width="2"/></g>'
    o += T(400, 360, "Turbine", 17, 700, INK, "end") + T(400, 382, "(charge)", 14, 500, MUTED, "end")
    o += arrow(350, 200, 420, 200, BL, 5) + T(385, 180, "débit", 17, 700, BL)
    # --- électricité
    o += s_wire([(730, 310), (730, 230), (830, 230)]) + sym("R", 870, 230) + s_wire([(910, 230), (1090, 230), (1090, 320)])
    o += sym("LAMP", 1090, 360, 90, fill="#ffe36b") + s_wire([(1090, 400), (1090, 490), (730, 490), (730, 390)])
    o += sym("BAT", 730, 350, 90)
    o += T(730, 112, "Pile = générateur", 17, 700, INK) + g(730, 170, '<rect x="-24" y="-38" width="48" height="76" rx="8" fill="#2d9a4a"/><rect x="-24" y="-38" width="48" height="26" rx="8" fill="#1a1a1a"/><rect x="-11" y="-48" width="22" height="10" rx="3" fill="url(#metalH)"/>' + T(0, -17, "+", 20, 800, "#fff"))
    o += T(870, 195, "résistance R", 16, 700, INK) + T(1030, 360, "lampe", 17, 700, INK, "end") + T(1030, 382, "(charge)", 14, 500, MUTED, "end")
    o += i_arrow(940, 230, 1010, 230, "courant I", off=(0, -24), size=17)
    o += u_arrow(772, 385, 772, 315) + T(786, 355, "tension U", 15, 700, GREEN, "start")
    o += chip(600, 600, "Hauteur d'eau = tension U  ·  Débit = intensité I  ·  Tuyau étroit = résistance R  ·  Pompe = générateur", INK, w=1130, size=17)
    return figure(W, 640, o)


FIGS = {"loi_ohm_cercle": f_ohm, "puissance_cercle": f_puissance, "analogie_eau": f_eau}
