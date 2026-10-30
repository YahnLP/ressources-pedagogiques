"""Aides communes aux figures complémentaires de Seconde."""
from lib import *
from figs07 import block

W = 1200


def hrun(y, xa, xb, comps):
    """Fil horizontal avec composants [(x, kind, label, kw)]. Étiquette au-dessus."""
    o = ""; cur = xa
    for x, k, lab, kw in sorted(comps, key=lambda c: c[0]):
        o += s_wire([(cur, y), (x - 40, y)]) + sym(k, x, y, **kw)
        if lab: o += T(x, y + 46 if kw.get("below") else y - 36, lab, 18, 700, INK)
        cur = x + 40
    return o + s_wire([(cur, y), (xb, y)])


def vrun(x, ya, yb, comps, side=1, off=30):
    o = ""; cur = ya
    for y, k, lab, kw in sorted(comps, key=lambda c: c[0]):
        kw = {**kw}; kw.pop("below", None)
        o += s_wire([(x, cur), (x, y - 40)]) + sym(k, x, y, rot=90, **kw)
        if lab: o += T(x + side * off, y + 6, lab, 18, 700, INK, "start" if side > 0 else "end")
        cur = y + 40
    return o + s_wire([(x, cur), (x, yb)])


def tbl(x, y, ws, head, rows, rh=54, hcol=INK, fs=16, hs=17, tint=None):
    o = ""; cx = x
    for h, w in zip(head, ws):
        o += f'<rect x="{cx}" y="{y}" width="{w}" height="46" fill="{hcol}"/>' + T(cx + w / 2, y + 29, h, hs, 800, "#fff"); cx += w
    for r, row in enumerate(rows):
        cx = x
        for k, (v, w) in enumerate(zip(row, ws)):
            o += f'<rect x="{cx}" y="{y+46+r*rh}" width="{w}" height="{rh}" fill="{"#fff" if r % 2 == 0 else "#f3f6fb"}" stroke="#d5dce8"/>'
            ls = str(v).split("\n"); 
            for i, l in enumerate(ls): o += T(cx + w / 2, y + 46 + r * rh + rh / 2 + 6 - (len(ls) - 1) * 9 + i * 18, l, fs, 600 if k else 800, INK)
            cx += w
    return o


def pyramid(levels, x=40, y=30, w=520, h=96, gap=8, tx=600, sz=21):
    """levels : du sommet à la base [(titre, sous-titre, couleur)]. Texte à droite."""
    n = len(levels); H = n * (h + gap); o = ""
    for i, (t, s, c) in enumerate(levels):
        y0 = y + i * (h + gap); y1 = y0 + h
        top = 70; a0 = top + (i * (h + gap)) / H * (w / 2 - top); a1 = top + ((i + 1) * (h + gap) - gap) / H * (w / 2 - top); cx = x + w / 2
        o += f'<path d="M{cx-a0},{y0} L{cx+a0},{y0} L{cx+a1},{y1} L{cx-a1},{y1} Z" fill="{c}"/>' + T(cx, y0 + h / 2 + 8, t.split("\n")[0], 20, 800, "#fff")
        o += f'<line x1="{cx+a1+8}" y1="{y0+h/2}" x2="{tx-14}" y2="{y0+h/2}" stroke="#c9d3e3" stroke-width="2" stroke-dasharray="5 5"/>'
        o += T(tx, y0 + h / 2 - 4, t.replace("\n", " "), sz, 800, c, "start") + T(tx, y0 + h / 2 + 24, s, 16, 500, MUTED, "start")
    return o, H + 2 * y - gap


def ui_win(x, y, w, h, title_, bar="#e9ecf3"):
    o = f'<g filter="url(#sh)"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="#fbfcfe" stroke="#aab3c5" stroke-width="2"/></g>'
    o += f'<rect x="{x}" y="{y}" width="{w}" height="34" rx="10" fill="{bar}"/><rect x="{x}" y="{y+20}" width="{w}" height="14" fill="{bar}"/>'
    o += ''.join(f'<circle cx="{x+20+i*20}" cy="{y+17}" r="6" fill="{c}"/>' for i, c in enumerate(("#ff5f57", "#febc2e", "#28c840")))
    return o + T(x + w / 2, y + 23, title_, 15, 700, INK)


def duo(a, b, la, lb, ca=BLUE, cb=GREEN, h=420, wa=570):
    return panel(30, 30, wa, h, la, accent=ca) + panel(30 + wa + 20, 30, 1140 - wa - 20, h, lb, accent=cb)
