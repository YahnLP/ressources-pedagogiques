"""Bibliothèque de dessin SVG pour les illustrations du cours E2.

Style : planche de manuel scolaire (fond blanc, composants réalistes en dégradés,
schémas normalisés CEI, légendes en français).
"""
import math
import random

INK = "#1b2742"
MUTED = "#5d6b86"
LINE = "#c9d3e3"
PANEL = "#f4f7fc"
BLUE = "#2f5bea"
GREEN = "#17935c"
RED = "#d63f3f"
AMBER = "#e99a14"
COPPER = "#c8773a"

DEFS = """
<defs>
  <linearGradient id="metalV" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#f5f7fa"/><stop offset=".45" stop-color="#b9c1cc"/>
    <stop offset=".55" stop-color="#9aa4b2"/><stop offset="1" stop-color="#d9dee5"/></linearGradient>
  <linearGradient id="metalH" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="#f5f7fa"/><stop offset=".45" stop-color="#b9c1cc"/>
    <stop offset=".55" stop-color="#9aa4b2"/><stop offset="1" stop-color="#d9dee5"/></linearGradient>
  <linearGradient id="cylShade" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#fff" stop-opacity=".6"/><stop offset=".35" stop-color="#fff" stop-opacity="0"/>
    <stop offset=".75" stop-color="#000" stop-opacity=".08"/><stop offset="1" stop-color="#000" stop-opacity=".32"/></linearGradient>
  <linearGradient id="cylShadeH" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="#000" stop-opacity=".38"/><stop offset=".22" stop-color="#fff" stop-opacity=".28"/>
    <stop offset=".5" stop-color="#fff" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".4"/></linearGradient>
  <linearGradient id="black" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#4a4f58"/><stop offset=".5" stop-color="#23262c"/><stop offset="1" stop-color="#101216"/></linearGradient>
  <linearGradient id="blackH" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="#111317"/><stop offset=".3" stop-color="#4b505a"/><stop offset=".6" stop-color="#262a30"/><stop offset="1" stop-color="#0e1013"/></linearGradient>
  <linearGradient id="gold" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="#b8892b"/><stop offset=".4" stop-color="#f6dc86"/><stop offset="1" stop-color="#a37620"/></linearGradient>
  <linearGradient id="copper" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#e59a5b"/><stop offset=".5" stop-color="#c8773a"/><stop offset="1" stop-color="#a95f2b"/></linearGradient>
  <linearGradient id="pcb" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#2f9a68"/><stop offset="1" stop-color="#1d7a50"/></linearGradient>
  <linearGradient id="solder" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#ffffff"/><stop offset=".35" stop-color="#cfd5dd"/><stop offset=".7" stop-color="#8d97a5"/><stop offset="1" stop-color="#d7dce3"/></linearGradient>
  <linearGradient id="solderDull" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#a8a49d"/><stop offset="1" stop-color="#6f6c66"/></linearGradient>
  <linearGradient id="yellow" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#ffd84a"/><stop offset="1" stop-color="#eaa90c"/></linearGradient>
  <linearGradient id="blueSleeve" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="#0f2f6e"/><stop offset=".3" stop-color="#3f74d4"/><stop offset=".6" stop-color="#2557b4"/><stop offset="1" stop-color="#0d2760"/></linearGradient>
  <linearGradient id="redLed" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="#b3141a"/><stop offset=".35" stop-color="#ff6a6a"/><stop offset=".65" stop-color="#e5353b"/><stop offset="1" stop-color="#9d1117"/></linearGradient>
  <linearGradient id="beige" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#f3e2bd"/><stop offset="1" stop-color="#d3b97f"/></linearGradient>
  <linearGradient id="boardBB" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#f7f4ec"/><stop offset="1" stop-color="#e6e0d1"/></linearGradient>
  <linearGradient id="tan" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#d9b77a"/><stop offset="1" stop-color="#c39a58"/></linearGradient>
  <radialGradient id="glow" cx=".5" cy=".5" r=".5">
    <stop offset="0" stop-color="#ffe46b" stop-opacity=".95"/><stop offset=".5" stop-color="#ffd23a" stop-opacity=".45"/>
    <stop offset="1" stop-color="#ffd23a" stop-opacity="0"/></radialGradient>
  <radialGradient id="glowRed" cx=".5" cy=".5" r=".5">
    <stop offset="0" stop-color="#ff5a5a" stop-opacity=".85"/><stop offset="1" stop-color="#ff5a5a" stop-opacity="0"/></radialGradient>
  <radialGradient id="knob" cx=".35" cy=".3" r=".8">
    <stop offset="0" stop-color="#6a707b"/><stop offset="1" stop-color="#16181c"/></radialGradient>
  <filter id="sh" x="-20%" y="-20%" width="150%" height="150%">
    <feDropShadow dx="0" dy="4" stdDeviation="4" flood-color="#1b2742" flood-opacity=".22"/></filter>
  <filter id="shs" x="-20%" y="-20%" width="150%" height="150%">
    <feDropShadow dx="0" dy="2" stdDeviation="2" flood-color="#1b2742" flood-opacity=".25"/></filter>
  <filter id="neon" x="-20%" y="-20%" width="140%" height="140%">
    <feGaussianBlur stdDeviation="2.2" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
  <marker id="arr" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
    <path d="M0,0 L10,5 L0,10 z" fill="context-stroke"/></marker>
</defs>
"""


def figure(w, h, body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" '
            f'font-family="Inter, Helvetica, Arial, sans-serif">{DEFS}'
            f'<rect x="1.5" y="1.5" width="{w-3}" height="{h-3}" rx="20" fill="#fff" stroke="#d9e0ec" stroke-width="3"/>'
            f'{body}</svg>')


def T(x, y, s, size=22, weight=500, fill=INK, anchor="middle", italic=False, extra=""):
    """Texte (peut être multiligne avec \\n)."""
    lines = str(s).split("\n")
    st = ' font-style="italic"' if italic else ""
    if len(lines) == 1:
        return (f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" fill="{fill}" '
                f'text-anchor="{anchor}"{st} {extra}>{esc(lines[0])}</text>')
    out = f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}"{st} {extra}>'
    for i, l in enumerate(lines):
        out += f'<tspan x="{x}" dy="{0 if i == 0 else size*1.28:.1f}">{esc(l)}</tspan>'
    return out + "</text>"


def esc(s):
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def title(x, y, s, sub=None):
    o = T(x, y, s, 30, 700, INK, "start")
    if sub:
        o += T(x, y + 28, sub, 18, 400, MUTED, "start")
    return o


def panel(x, y, w, h, head=None, fill=PANEL, accent=BLUE):
    o = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="16" fill="{fill}" stroke="#e1e7f1" stroke-width="2"/>'
    if head:
        o += f'<rect x="{x}" y="{y}" width="{w}" height="44" rx="16" fill="{accent}"/>'
        o += f'<rect x="{x}" y="{y+24}" width="{w}" height="20" fill="{accent}"/>'
        o += T(x + w / 2, y + 30, head, 21, 700, "#fff")
    return o


def g(x, y, inner, s=1.0, rot=0):
    tr = f"translate({x},{y})"
    if rot:
        tr += f" rotate({rot})"
    if s != 1.0:
        tr += f" scale({s})"
    return f'<g transform="{tr}">{inner}</g>'


def callout(px, py, tx, ty, text, anchor="start", size=19, color=INK, bold=False, dot=True):
    """Ligne de repère depuis le point (px,py) vers un texte placé en (tx,ty)."""
    o = f'<line x1="{px}" y1="{py}" x2="{tx}" y2="{ty}" stroke="{MUTED}" stroke-width="2"/>'
    if dot:
        o += f'<circle cx="{px}" cy="{py}" r="5" fill="#fff" stroke="{MUTED}" stroke-width="2.5"/>'
    off = 10 if anchor == "start" else (-10 if anchor == "end" else 0)
    lines = text.split("\n")
    n = len(lines)
    y0 = ty + (6 if n == 1 else -((n - 1) * size * 1.28) / 2 + 6)
    o += T(tx + off, y0, text, size, 700 if bold else 500, color, anchor)
    return o


def badge(x, y, n, color=BLUE, r=17):
    return (f'<circle cx="{x}" cy="{y}" r="{r}" fill="{color}"/>'
            f'<text x="{x}" y="{y+6}" font-size="{r*1.15:.0f}" font-weight="700" fill="#fff" text-anchor="middle">{n}</text>')


def chip(x, y, text, color=GREEN, w=None, size=18):
    w = w or (len(text) * size * 0.58 + 26)
    return (f'<rect x="{x - w/2}" y="{y-17}" width="{w}" height="34" rx="17" fill="{color}"/>'
            f'<text x="{x}" y="{y+6}" font-size="{size}" font-weight="700" fill="#fff" text-anchor="middle">{esc(text)}</text>')


# --------------------------------------------------------------------------
# Composants réalistes
# --------------------------------------------------------------------------
COLORS = {
    "noir": "#1a1a1a", "marron": "#7a4320", "rouge": "#d32f2f", "orange": "#f57c00", "jaune": "#fbc02d",
    "vert": "#2e9d3f", "bleu": "#1e5fd0", "violet": "#7a3cb5", "gris": "#8d9399", "blanc": "#f4f4f4",
    "or": "#c9a227", "argent": "#c0c4c9",
}


def resistor(bands=("jaune", "violet", "rouge", "or"), body="#e9d4a3", lead=110):
    """Résistance axiale (centre en 0,0, corps ~160 px)."""
    L = 82
    o = f'<rect x="{-L-lead}" y="-3.5" width="{2*(L+lead)}" height="7" rx="3" fill="url(#metalV)"/>'
    shape = (f'<rect x="-64" y="-15" width="128" height="30" fill="{body}"/>'
             f'<rect x="-84" y="-22" width="36" height="44" rx="16" fill="{body}"/>'
             f'<rect x="48" y="-22" width="36" height="44" rx="16" fill="{body}"/>')
    o += f'<g filter="url(#shs)">{shape}</g>'
    pos = [-44, -22, 0, 52]
    if len(bands) == 5:
        pos = [-50, -32, -14, 8, 54]
    for x, c in zip(pos, bands):
        wd = 11
        o += f'<rect x="{x-wd/2}" y="-15" width="{wd}" height="30" fill="{COLORS[c]}"/>'
    o += (f'<g><rect x="-64" y="-15" width="128" height="30" fill="url(#cylShade)"/>'
          f'<rect x="-84" y="-22" width="36" height="44" rx="16" fill="url(#cylShade)"/>'
          f'<rect x="48" y="-22" width="36" height="44" rx="16" fill="url(#cylShade)"/></g>')
    return o


def smd_resistor(code="103", w=96, h=48):
    o = f'<g filter="url(#shs)"><rect x="{-w/2}" y="{-h/2}" width="{w}" height="{h}" rx="3" fill="url(#black)"/>'
    o += f'<rect x="{-w/2}" y="{-h/2}" width="{w*0.15}" height="{h}" rx="2" fill="url(#metalH)"/>'
    o += f'<rect x="{w/2-w*0.15}" y="{-h/2}" width="{w*0.15}" height="{h}" rx="2" fill="url(#metalH)"/></g>'
    o += f'<text x="0" y="{h*0.17}" font-size="{h*0.5:.0f}" font-weight="600" fill="#e9e9e9" text-anchor="middle" font-family="Inter">{code}</text>'
    return o


def smd_capacitor(w=96, h=48, color="#b78b52"):
    o = f'<g filter="url(#shs)"><rect x="{-w/2}" y="{-h/2}" width="{w}" height="{h}" rx="3" fill="{color}"/>'
    o += f'<rect x="{-w/2}" y="{-h/2}" width="{w*0.16}" height="{h}" rx="2" fill="url(#metalH)"/>'
    o += f'<rect x="{w/2-w*0.16}" y="{-h/2}" width="{w*0.16}" height="{h}" rx="2" fill="url(#metalH)"/>'
    o += f'<rect x="{-w/2}" y="{-h/2}" width="{w}" height="{h}" rx="3" fill="url(#cylShade)" opacity=".5"/></g>'
    return o


def electrolytic(h=130, w=92, sleeve="url(#blueSleeve)", text=("470 µF", "25 V"), bulged=False, leak=False):
    """Condensateur chimique radial. Base en y=0, axe en x=0. Patte + à droite (longue)."""
    r = w / 2
    o = ""
    # pattes
    o += f'<rect x="{r*0.36-3}" y="0" width="6" height="118" rx="3" fill="url(#metalH)"/>'  # +
    o += f'<rect x="{-r*0.36-3}" y="0" width="6" height="92" rx="3" fill="url(#metalH)"/>'  # -
    top = -h - (10 if bulged else 0)
    # corps
    o += f'<g filter="url(#shs)"><rect x="{-r}" y="{-h}" width="{w}" height="{h-9}" fill="{sleeve}"/>'
    o += f'<rect x="{-r}" y="-14" width="{w}" height="14" rx="2" fill="url(#blackH)"/></g>'
    # bande -
    o += f'<rect x="{-r}" y="{-h}" width="{w*0.27}" height="{h-14}" fill="#e9eef6"/>'
    o += f'<rect x="{-r}" y="{-h}" width="{w*0.27}" height="{h-14}" fill="url(#cylShadeH)" opacity=".7"/>'
    for i in range(4):
        o += f'<text x="{-r+w*0.135}" y="{-h+30+i*26}" font-size="22" font-weight="800" fill="#16203a" text-anchor="middle">−</text>'
    o += f'<rect x="{-r}" y="{-h}" width="{w}" height="{h-14}" fill="url(#cylShadeH)" opacity=".55"/>'
    # texte
    o += T(r * 0.24, -h * 0.5 + 6, text[0], 17, 700, "#ffffff")
    o += T(r * 0.24, -h * 0.5 + 28, text[1], 17, 600, "#dbe6ff")
    # dessus
    if bulged:
        o += f'<path d="M{-r},{-h} C{-r},{top-14} {r},{top-14} {r},{-h} Z" fill="url(#metalV)"/>'
        o += f'<path d="M{-r*0.8},{-h-4} C{-r*0.5},{top-4} {r*0.5},{top-4} {r*0.8},{-h-4}" stroke="#7a828f" stroke-width="2.5" fill="none"/>'
        o += f'<path d="M{-r*0.5},{top+2} L{r*0.1},{top-8} L{r*0.55},{top+2}" stroke="#4d535d" stroke-width="3" fill="none" stroke-linejoin="round"/>'
        if leak:
            o += (f'<path d="M{-r*0.2},{top+2} C{-r*0.1},{top+14} {-r*0.4},{top+20} {-r*0.5},{top+40} '
                  f'C{-r*0.55},{top+60} {-r*0.2},{top+66} {-r*0.18},{top+48} C{-r*0.1},{top+30} {r*0.1},{top+10} {-r*0.2},{top+2}Z" '
                  f'fill="#7b4a1b" opacity=".92"/>')
    else:
        o += f'<ellipse cx="0" cy="{-h}" rx="{r}" ry="10" fill="url(#metalV)" stroke="#7a828f" stroke-width="1.5"/>'
        o += f'<path d="M{-r*0.55},{-h-3} L{r*0.55},{-h+3} M{r*0.55},{-h-3} L{-r*0.55},{-h+3}" stroke="#6c7480" stroke-width="2.2"/>'
    return o


def ceramic_cap():
    o = f'<rect x="-14" y="0" width="5" height="70" rx="2.5" fill="url(#metalH)"/><rect x="9" y="0" width="5" height="70" rx="2.5" fill="url(#metalH)"/>'
    o += '<g filter="url(#shs)"><path d="M-34,-8 C-38,-52 -20,-72 0,-72 C20,-72 38,-52 34,-8 Z" fill="#e48a2a"/>'
    o += '<path d="M-34,-8 C-38,-52 -20,-72 0,-72 C20,-72 38,-52 34,-8 Z" fill="url(#cylShadeH)"/></g>'
    o += T(0, -30, "104", 17, 700, "#4a2a07")
    return o


def led(color="red", lit=False, legs=True):
    """LED 5 mm. Base en y=0. Patte longue (anode +) à droite."""
    pal = {"red": ("#ff5757", "#b3141a", "url(#redLed)")}
    o = ""
    if lit:
        o += '<circle cx="0" cy="-48" r="110" fill="url(#glowRed)"/>'
    if legs:
        o += '<rect x="9" y="0" width="6" height="112" rx="3" fill="url(#metalH)"/>'
        o += '<rect x="-15" y="0" width="6" height="86" rx="3" fill="url(#metalH)"/>'
    o += '<g filter="url(#shs)">'
    o += '<path d="M-31,0 L-31,-52 A31,31 0 0 1 31,-52 L31,0 Z" fill="url(#redLed)" opacity=".96"/>'
    o += '<path d="M-37,0 L-37,-9 L37,-9 L37,0 L26,0 L26,2 L-26,2 L-26,0 Z" fill="#d83a3a"/>'
    o += '</g>'
    # intérieur
    o += '<path d="M-15,-9 L-15,-44 L-4,-44 L-4,-9 Z" fill="url(#metalH)" opacity=".9"/>'  # enclume (cathode)
    o += '<path d="M-24,-44 L9,-44 L2,-58 L-17,-58 Z" fill="url(#metalH)" opacity=".9"/>'
    o += '<rect x="9" y="-9" width="5" height="-0" fill="#999"/>'
    o += '<path d="M9,-9 L9,-36" stroke="#9aa4b2" stroke-width="5"/>'
    o += '<path d="M-20,-30 C-20,-62 -10,-76 0,-76" stroke="#fff" stroke-opacity=".55" stroke-width="7" stroke-linecap="round" fill="none"/>'
    return o


def diode_1n4007():
    o = '<rect x="-84" y="-3" width="168" height="6" rx="3" fill="url(#metalV)"/>'
    o += '<g filter="url(#shs)"><rect x="-38" y="-17" width="76" height="34" rx="8" fill="url(#black)"/></g>'
    o += '<rect x="16" y="-17" width="13" height="34" fill="url(#metalV)"/>'
    o += '<rect x="-38" y="-17" width="76" height="34" rx="8" fill="url(#cylShade)" opacity=".5"/>'
    o += T(-9, 5, "1N4007", 12, 700, "#d8dde5")
    return o


def to92(label="2N2222"):
    """Transistor TO-92 vu de face (face plate), 3 pattes. Base y=0."""
    o = ''.join(f'<rect x="{x-3}" y="0" width="6" height="88" rx="3" fill="url(#metalH)"/>' for x in (-22, 0, 22))
    o += '<g filter="url(#shs)"><path d="M-36,0 L-36,-52 Q-36,-92 0,-92 Q36,-92 36,-52 L36,0 Z" fill="url(#black)"/></g>'
    o += '<path d="M-36,0 L-36,-52 Q-36,-92 0,-92 Q36,-92 36,-52 L36,0 Z" fill="url(#cylShadeH)" opacity=".35"/>'
    o += T(0, -40, label, 15, 700, "#d8dde5")
    return o


def dip(pins=8, w=None, h=96, label="NE555", pitch=36, soic=False, fs=20):
    """Circuit intégré DIP/SOIC horizontal, encoche à gauche. Coin haut-gauche du corps en (0,0)."""
    n = pins // 2
    w = w or n * pitch + 10
    pw = pitch * 0.36
    o = ""
    for i in range(n):
        x = 5 + i * pitch + (pitch - pw) / 2
        if soic:
            o += f'<rect x="{x}" y="{-pw*1.4}" width="{pw}" height="{pw*1.4+2}" rx="1.2" fill="url(#metalH)"/>'
            o += f'<rect x="{x}" y="{h-2}" width="{pw}" height="{pw*1.4+2}" rx="1.2" fill="url(#metalH)"/>'
        else:
            o += f'<rect x="{x}" y="-26" width="{pw}" height="28" rx="2" fill="url(#metalH)"/>'
            o += f'<rect x="{x}" y="{h-2}" width="{pw}" height="28" rx="2" fill="url(#metalH)"/>'
    o += f'<g filter="url(#shs)"><rect x="0" y="0" width="{w}" height="{h}" rx="5" fill="url(#black)"/></g>'
    o += f'<path d="M0,{h/2-11} A11,11 0 0 1 0,{h/2+11} Z" fill="#fff" fill-opacity=".92"/>'
    o += f'<circle cx="{18 if not soic else 14}" cy="{h-16}" r="{5 if not soic else 3.5}" fill="#0a0c0f" stroke="#555a63" stroke-width="2"/>'
    o += T(w / 2 + 6, h / 2 + fs*0.3, label, fs, 700, "#c9cfd8")
    return o


def dip_pin_xy(i, pins=8, pitch=36, h=96, soic=False):
    """Centre (x, y_bas/haut) de la broche i (1..pins) et côté ('b' ou 't')."""
    n = pins // 2
    pw = pitch * 0.36
    if i <= n:
        k, side = i - 1, "b"
    else:
        k, side = pins - i, "t"
    x = 5 + k * pitch + pitch / 2
    return x, side


def inductor_toroid():
    o = '<g filter="url(#shs)">'
    o += '<ellipse cx="0" cy="0" rx="62" ry="50" fill="#3a3d44"/><ellipse cx="0" cy="0" rx="26" ry="19" fill="#fff"/>'
    o += '</g>'
    for i in range(34):
        a = i / 34 * 2 * math.pi
        x1, y1 = 28 * math.cos(a), 20 * math.sin(a)
        x2, y2 = 66 * math.cos(a), 54 * math.sin(a)
        o += f'<path d="M{x1:.1f},{y1:.1f} L{x2:.1f},{y2:.1f}" stroke="url(#copper)" stroke-width="7" stroke-linecap="round"/>'
        o += f'<path d="M{x1:.1f},{y1:.1f} L{x2:.1f},{y2:.1f}" stroke="#f3b27a" stroke-width="2" stroke-linecap="round" opacity=".7"/>'
    o += '<ellipse cx="0" cy="0" rx="26" ry="19" fill="#fff" opacity=".0"/>'
    o += '<path d="M-14,50 C-20,90 -28,100 -30,118" stroke="url(#metalH)" stroke-width="5" fill="none" stroke-linecap="round"/>'
    o += '<path d="M14,50 C20,90 28,100 30,118" stroke="url(#metalH)" stroke-width="5" fill="none" stroke-linecap="round"/>'
    return o


def inductor_axial():
    """Self moulée type 'résistance' (bandes)."""
    o = '<rect x="-110" y="-3.5" width="220" height="7" rx="3" fill="url(#metalV)"/>'
    o += '<g filter="url(#shs)"><rect x="-52" y="-17" width="104" height="34" rx="14" fill="#2c6f8e"/></g>'
    for x, c in ((-32, "marron"), (-14, "noir"), (4, "rouge"), (36, "or")):
        o += f'<rect x="{x-5}" y="-17" width="10" height="34" fill="{COLORS[c]}"/>'
    o += '<rect x="-52" y="-17" width="104" height="34" rx="14" fill="url(#cylShade)"/>'
    return o


def smd_inductor():
    o = '<g filter="url(#shs)"><rect x="-44" y="-44" width="88" height="88" rx="6" fill="#3a3a3f"/>'
    o += '<rect x="-34" y="-34" width="68" height="68" rx="34" fill="#a2602f"/></g>'
    for i in range(8):
        o += f'<path d="M-34,{-24+i*7} Q0,{-18+i*7} 34,{-24+i*7}" stroke="#e9a56b" stroke-width="2" fill="none" opacity=".8"/>'
    o += '<rect x="-44" y="-44" width="18" height="88" rx="3" fill="url(#metalH)"/><rect x="26" y="-44" width="18" height="88" rx="3" fill="url(#metalH)"/>'
    return o


def ldr():
    o = '<rect x="-14" y="0" width="5" height="62" fill="url(#metalH)"/><rect x="9" y="0" width="5" height="62" fill="url(#metalH)"/>'
    o += '<g filter="url(#shs)"><circle cx="0" cy="-36" r="38" fill="#b87c3c"/></g>'
    o += '<circle cx="0" cy="-36" r="32" fill="#d9a35e"/>'
    o += '<path d="M-26,-48 H26 M-26,-48 Q-28,-42 -24,-40 H24 Q28,-34 24,-32 H-24 Q-28,-26 -22,-24 H22" stroke="#6b3d12" stroke-width="5" fill="none" stroke-linejoin="round"/>'
    o += '<circle cx="0" cy="-36" r="38" fill="url(#cylShade)" opacity=".5"/>'
    return o


def potentiometer():
    o = ''.join(f'<rect x="{x-3}" y="0" width="6" height="64" fill="url(#metalH)"/>' for x in (-26, 0, 26))
    o += '<g filter="url(#shs)"><rect x="-48" y="-62" width="96" height="62" rx="8" fill="#2f5aa8"/></g>'
    o += '<rect x="-48" y="-62" width="96" height="62" rx="8" fill="url(#cylShade)"/>'
    o += '<rect x="-14" y="-92" width="28" height="32" fill="url(#metalH)"/>'
    o += '<g filter="url(#shs)"><circle cx="0" cy="-118" r="36" fill="url(#knob)"/></g>'
    for i in range(24):
        a = i / 24 * 2 * math.pi
        o += f'<line x1="{30*math.cos(a):.1f}" y1="{-118+30*math.sin(a):.1f}" x2="{36*math.cos(a):.1f}" y2="{-118+36*math.sin(a):.1f}" stroke="#000" stroke-opacity=".5" stroke-width="2"/>'
    o += '<line x1="0" y1="-118" x2="0" y2="-148" stroke="#fff" stroke-width="5" stroke-linecap="round"/>'
    return o


def motor():
    o = '<g filter="url(#shs)"><rect x="-44" y="-34" width="76" height="68" rx="10" fill="url(#metalV)"/>'
    o += '<rect x="32" y="-6" width="30" height="12" fill="url(#metalV)"/><rect x="-54" y="-30" width="12" height="60" rx="5" fill="#c9ced6"/></g>'
    o += '<circle cx="-3" cy="0" r="22" fill="#e9edf3" stroke="#8993a2" stroke-width="3"/>'
    o += T(-3, 9, "M", 26, 800, INK)
    o += '<rect x="-30" y="34" width="5" height="26" fill="url(#metalH)"/><rect x="2" y="34" width="5" height="26" fill="url(#metalH)"/>'
    return o


def buzzer():
    o = '<g filter="url(#shs)"><circle cx="0" cy="-36" r="42" fill="url(#black)"/></g>'
    o += '<circle cx="0" cy="-36" r="9" fill="#050607"/><circle cx="0" cy="-36" r="42" fill="url(#cylShade)" opacity=".4"/>'
    o += T(26, -66, "+", 22, 800, "#fff")
    o += '<rect x="-24" y="4" width="5" height="52" fill="url(#metalH)"/><rect x="19" y="4" width="5" height="52" fill="url(#metalH)"/>'
    return o


def push_button():
    o = '<g filter="url(#shs)"><rect x="-38" y="-38" width="76" height="76" rx="8" fill="#2a2d33"/></g>'
    o += '<circle cx="0" cy="0" r="22" fill="url(#knob)"/><circle cx="0" cy="0" r="22" fill="none" stroke="#000" stroke-opacity=".4" stroke-width="2"/>'
    for sx in (-1, 1):
        for sy in (-1, 1):
            o += f'<circle cx="{sx*28}" cy="{sy*28}" r="3.5" fill="#8a929e"/>'
    return o


def battery_9v():
    o = '<g filter="url(#sh)"><rect x="-44" y="-70" width="88" height="140" rx="8" fill="#1b1d22"/></g>'
    o += '<rect x="-44" y="-70" width="88" height="62" rx="8" fill="#c9ced6"/>'
    o += '<rect x="-44" y="-12" width="88" height="82" fill="#202a54" opacity=".0"/>'
    o += T(0, -30, "9V", 34, 800, "#222")
    o += '<circle cx="-18" cy="-86" r="13" fill="url(#metalV)"/><path d="M12,-96 L36,-96 L36,-76 L12,-76 Z" fill="url(#metalV)"/>'
    o += T(-18, -80, "+", 18, 800, "#222")
    return o


def aa_cell():
    o = '<g filter="url(#shs)"><rect x="-26" y="-70" width="52" height="140" rx="8" fill="#2d9a4a"/></g>'
    o += '<rect x="-26" y="-70" width="52" height="140" rx="8" fill="url(#cylShadeH)"/>'
    o += '<rect x="-12" y="-80" width="24" height="12" rx="3" fill="url(#metalH)"/>'
    o += '<rect x="-26" y="-70" width="52" height="34" rx="8" fill="#1a1a1a"/>'
    o += T(0, -48, "+", 22, 800, "#fff") + T(0, 36, "1,5 V", 18, 700, "#fff")
    return o


def bulb(lit=False):
    o = ""
    if lit:
        o += '<circle cx="0" cy="-34" r="90" fill="url(#glow)"/>'
    o += '<path d="M-26,-12 C-60,-30 -44,-84 0,-84 C44,-84 60,-30 26,-12 Z" fill="#fffdf2" fill-opacity="%s" stroke="#98a3b5" stroke-width="3"/>' % (".95" if lit else ".55")
    o += '<path d="M-10,-12 L-10,-44 L-4,-54 L4,-44 L10,-54 L10,-12" stroke="%s" stroke-width="3" fill="none"/>' % ("#ff9d00" if lit else "#7b8494")
    o += '<rect x="-26" y="-12" width="52" height="34" rx="4" fill="url(#metalH)"/>'
    for i in range(3):
        o += f'<line x1="-26" y1="{-4+i*10}" x2="26" y2="{-4+i*10}" stroke="#7a828f" stroke-width="2.5"/>'
    o += '<path d="M-14,22 L14,22 L8,34 L-8,34 Z" fill="#2a2d33"/>'
    return o


def wall_socket():
    o = '<g filter="url(#shs)"><rect x="-60" y="-60" width="120" height="120" rx="16" fill="#f4f4f1" stroke="#d3d3cc" stroke-width="3"/></g>'
    o += '<circle cx="0" cy="0" r="40" fill="#e7e7e2" stroke="#c4c4bc" stroke-width="3"/>'
    o += '<circle cx="-16" cy="0" r="6.5" fill="#222"/><circle cx="16" cy="0" r="6.5" fill="#222"/>'
    o += '<rect x="-3" y="-44" width="6" height="14" rx="2" fill="#9a9a92"/>'
    return o


def usb_cable_note():
    return ""


# --------------------------------------------------------------------------
# Symboles normalisés (CEI) — horizontaux, bornes en (-40,0) et (40,0)
# --------------------------------------------------------------------------
SW = 3.2


def s_wire(pts, color=INK, w=SW, dash=None):
    d = "M" + " L".join(f"{x},{y}" for x, y in pts)
    da = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{w}" stroke-linejoin="round" stroke-linecap="round"{da}/>'


def dot(x, y, r=6, color=INK):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{color}"/>'


def node(x, y, label=None):
    o = f'<circle cx="{x}" cy="{y}" r="6" fill="#fff" stroke="{INK}" stroke-width="{SW}"/>'
    return o


def sym(kind, x=0, y=0, rot=0, color=INK, s=1.0, **kw):
    w = SW
    c = color
    o = ""
    if kind == "R":
        o = (f'<path d="M-40,0 H-26 M26,0 H40" stroke="{c}" stroke-width="{w}" fill="none"/>'
             f'<rect x="-26" y="-11" width="52" height="22" fill="#fff" stroke="{c}" stroke-width="{w}"/>')
    elif kind == "C":
        o = (f'<path d="M-40,0 H-6 M6,0 H40" stroke="{c}" stroke-width="{w}"/>'
             f'<path d="M-6,-20 V20 M6,-20 V20" stroke="{c}" stroke-width="{w+0.6}"/>')
    elif kind == "CP":  # polarisé : + à gauche
        o = (f'<path d="M-40,0 H-6 M8,0 H40" stroke="{c}" stroke-width="{w}"/>'
             f'<path d="M-6,-20 V20" stroke="{c}" stroke-width="{w+0.6}"/>'
             f'<path d="M8,-20 Q2,0 8,20" stroke="{c}" stroke-width="{w+0.6}" fill="none"/>'
             f'<text x="-22" y="-12" font-size="19" font-weight="800" fill="{c}" text-anchor="middle">+</text>')
    elif kind == "L":
        o = f'<path d="M-40,0 H-28' + ''.join(' a7,7 0 0 1 14,0' for _ in range(4)) + ' H40" stroke="' + c + f'" stroke-width="{w}" fill="none"/>'
    elif kind == "D":  # anode à gauche, cathode à droite
        o = (f'<path d="M-40,0 H-14 M14,0 H40" stroke="{c}" stroke-width="{w}"/>'
             f'<path d="M-14,-17 L14,0 L-14,17 Z" fill="{c}" stroke="{c}" stroke-width="2" stroke-linejoin="round"/>'
             f'<path d="M14,-17 V17" stroke="{c}" stroke-width="{w+0.6}"/>')
    elif kind == "LED":
        o = (f'<path d="M-40,0 H-14 M14,0 H40" stroke="{c}" stroke-width="{w}"/>'
             f'<path d="M-14,-17 L14,0 L-14,17 Z" fill="#fff" stroke="{c}" stroke-width="{w}" stroke-linejoin="round"/>'
             f'<path d="M14,-17 V17" stroke="{c}" stroke-width="{w+0.6}"/>'
             f'<path d="M-4,-26 L8,-42 M8,-26 L20,-42" stroke="{c}" stroke-width="2.6" marker-end="url(#arr)"/>')
    elif kind == "BAT":  # pile : + à gauche
        o = (f'<path d="M-40,0 H-8 M8,0 H40" stroke="{c}" stroke-width="{w}"/>'
             f'<path d="M-8,-22 V22" stroke="{c}" stroke-width="{w+0.8}"/><path d="M8,-12 V12" stroke="{c}" stroke-width="{w+3}"/>'
             f'<text x="-22" y="-14" font-size="18" font-weight="800" fill="{c}" text-anchor="middle">+</text>')
    elif kind == "LAMP":
        o = (f'<path d="M-40,0 H-18 M18,0 H40" stroke="{c}" stroke-width="{w}"/>'
             f'<circle cx="0" cy="0" r="18" fill="{kw.get("fill","#fff")}" stroke="{c}" stroke-width="{w}"/>'
             f'<path d="M-12.7,-12.7 L12.7,12.7 M12.7,-12.7 L-12.7,12.7" stroke="{c}" stroke-width="{w}"/>')
    elif kind == "SW":  # interrupteur ouvert / fermé
        if kw.get("closed"):
            o = (f'<path d="M-40,0 H-22 M22,0 H40 M-22,0 L22,0" stroke="{c}" stroke-width="{w}"/>'
                 f'<circle cx="-22" cy="0" r="4.5" fill="#fff" stroke="{c}" stroke-width="{w-0.4}"/><circle cx="22" cy="0" r="4.5" fill="#fff" stroke="{c}" stroke-width="{w-0.4}"/>')
        else:
            o = (f'<path d="M-40,0 H-22 M22,0 H40 M-22,0 L18,-24" stroke="{c}" stroke-width="{w}"/>'
                 f'<circle cx="-22" cy="0" r="4.5" fill="#fff" stroke="{c}" stroke-width="{w-0.4}"/><circle cx="22" cy="0" r="4.5" fill="#fff" stroke="{c}" stroke-width="{w-0.4}"/>')
    elif kind == "BP":  # bouton poussoir
        o = (f'<path d="M-40,0 H-22 M22,0 H40" stroke="{c}" stroke-width="{w}"/>'
             f'<circle cx="-22" cy="0" r="4.5" fill="#fff" stroke="{c}" stroke-width="{w-0.4}"/><circle cx="22" cy="0" r="4.5" fill="#fff" stroke="{c}" stroke-width="{w-0.4}"/>'
             f'<path d="M-24,-14 H24 M0,-14 V-30 M-10,-30 H10" stroke="{c}" stroke-width="{w}"/>')
    elif kind == "POT":
        o = (f'<path d="M-40,0 H-26 M26,0 H40" stroke="{c}" stroke-width="{w}"/>'
             f'<rect x="-26" y="-11" width="52" height="22" fill="#fff" stroke="{c}" stroke-width="{w}"/>'
             f'<path d="M0,-40 V-12" stroke="{c}" stroke-width="{w}" marker-end="url(#arr)"/>')
    elif kind == "LDR":
        o = (f'<path d="M-40,0 H-26 M26,0 H40" stroke="{c}" stroke-width="{w}"/>'
             f'<rect x="-26" y="-11" width="52" height="22" fill="#fff" stroke="{c}" stroke-width="{w}"/>'
             f'<path d="M-30,-40 L-14,-24 M-16,-44 L0,-28" stroke="{c}" stroke-width="2.6" marker-end="url(#arr)"/>')
    elif kind == "MOTOR":
        o = (f'<path d="M-40,0 H-18 M18,0 H40" stroke="{c}" stroke-width="{w}"/>'
             f'<circle cx="0" cy="0" r="18" fill="#fff" stroke="{c}" stroke-width="{w}"/>'
             f'<text x="0" y="7" font-size="21" font-weight="800" fill="{c}" text-anchor="middle">M</text>')
    elif kind in ("VM", "AM"):
        letter = "V" if kind == "VM" else "A"
        o = (f'<path d="M-40,0 H-20 M20,0 H40" stroke="{c}" stroke-width="{w}"/>'
             f'<circle cx="0" cy="0" r="20" fill="#fff" stroke="{c}" stroke-width="{w}"/>'
             f'<text x="0" y="8" font-size="23" font-weight="800" fill="{c}" text-anchor="middle">{letter}</text>')
    elif kind == "BUZ":
        o = (f'<path d="M-40,0 H-18 M18,0 H40" stroke="{c}" stroke-width="{w}"/>'
             f'<circle cx="0" cy="0" r="18" fill="#fff" stroke="{c}" stroke-width="{w}"/>'
             f'<path d="M-6,-8 L-6,8 L2,8 L10,14 L10,-14 L2,-8 Z" fill="{c}"/>')
    elif kind == "FUSE":
        o = (f'<path d="M-40,0 H-26 M26,0 H40" stroke="{c}" stroke-width="{w}"/>'
             f'<rect x="-26" y="-9" width="52" height="18" fill="#fff" stroke="{c}" stroke-width="{w}"/><path d="M-26,0 H26" stroke="{c}" stroke-width="2"/>')
    return g(x, y, o, s, rot)


def gnd(x, y, color=INK):
    return (f'<path d="M{x},{y} V{y+14}" stroke="{color}" stroke-width="{SW}"/>'
            f'<path d="M{x-20},{y+14} H{x+20} M{x-13},{y+23} H{x+13} M{x-6},{y+32} H{x+6}" stroke="{color}" stroke-width="{SW}" stroke-linecap="round"/>')


def vcc(x, y, label="+5 V", color=INK):
    return (f'<path d="M{x},{y} V{y-22} M{x-14},{y-22} H{x+14}" stroke="{color}" stroke-width="{SW}" stroke-linecap="round"/>'
            + T(x, y - 34, label, 21, 700, color))


def npn(x=0, y=0, s=1.0, kind="npn"):
    """Transistor bipolaire. NPN : B à gauche (-50,0), C en haut (22,-44), E en bas (22,44).
    PNP : E en haut, C en bas."""
    o = (f'<circle cx="0" cy="0" r="36" fill="#fff" stroke="{INK}" stroke-width="{SW-0.6}"/>'
         f'<path d="M-50,0 H-10" stroke="{INK}" stroke-width="{SW}"/>'
         f'<path d="M-10,-20 V20" stroke="{INK}" stroke-width="{SW+2.5}"/>')
    o += f'<path d="M-10,-9 L22,-30 V-44" stroke="{INK}" stroke-width="{SW}" fill="none" stroke-linejoin="round"/>'
    o += f'<path d="M-10,9 L22,30 V44" stroke="{INK}" stroke-width="{SW}" fill="none" stroke-linejoin="round"/>'
    if kind == "npn":
        o += f'<path d="M13,24.1 L0.8,22.7 L6.8,13.5 Z" fill="{INK}"/>'
    else:
        o += f'<path d="M-3.6,-13.2 L8.6,-14.6 L2.6,-23.8 Z" fill="{INK}"/>'
    return g(x, y, o, s)


def nmos(x=0, y=0, s=1.0):
    """MOSFET canal N : G à gauche, D haut, S bas."""
    o = (f'<path d="M-50,0 H-18" stroke="{INK}" stroke-width="{SW}"/>'
         f'<path d="M-18,-22 V22" stroke="{INK}" stroke-width="{SW+0.5}"/>'
         f'<path d="M-8,-26 V-12 M-8,-8 V8 M-8,12 V26" stroke="{INK}" stroke-width="{SW+2}"/>'
         f'<path d="M-8,-19 H26 V-44 M-8,19 H26 V44 M-8,0 H26 V19" stroke="{INK}" stroke-width="{SW}" fill="none" stroke-linejoin="round"/>'
         f'<path d="M-8,0 L6,-6 V6 Z" fill="{INK}"/>')
    return g(x, y, o, s)


def arrow(x1, y1, x2, y2, color=BLUE, w=4, dash=None):
    da = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{w}" stroke-linecap="round" marker-end="url(#arr)"{da}/>'


def varrow_path(d, color=BLUE, w=4, dash=None):
    da = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round" marker-end="url(#arr)"{da}/>'


# --------------------------------------------------------------------------
# Breadboard
# --------------------------------------------------------------------------
class Breadboard:
    """Platine d'essai. Origine locale = coin haut-gauche. pas = 16 px."""
    P = 16

    def __init__(self, cols=30):
        self.cols = cols
        self.x0 = 44            # abscisse de la colonne 1
        self.W = self.x0 + (cols - 1) * self.P + 44
        # y des rangées
        self.rails_top = {"T+": 22, "T-": 40}
        self.top_rows = {r: 86 + i * self.P for i, r in enumerate("abcde")}
        self.bot_rows = {r: 86 + 5 * self.P + 34 + i * self.P for i, r in enumerate("fghij")}
        self.rails_bot = {"B+": 86 + 10 * self.P + 34 + 28, "B-": 86 + 10 * self.P + 34 + 46}
        self.H = self.rails_bot["B-"] + 24

    def xy(self, col, row):
        if row in self.rails_top or row in self.rails_bot:
            raise ValueError
        y = {**self.top_rows, **self.bot_rows}[row]
        return (self.x0 + (col - 1) * self.P, y)

    def rail(self, k, name):
        """k-ième trou de rail (0..), groupes de 5."""
        x = self.x0 + 6 + k * self.P + (k // 5) * 8
        y = {**self.rails_top, **self.rails_bot}[name]
        return (x, y)

    def draw(self, numbers=True, letters=True, rails_labels=True):
        o = f'<g filter="url(#sh)"><rect x="0" y="0" width="{self.W}" height="{self.H}" rx="12" fill="url(#boardBB)" stroke="#cfc8b6" stroke-width="2"/></g>'
        # canal central
        cy = 86 + 5 * self.P + 4
        o += f'<rect x="14" y="{cy}" width="{self.W-28}" height="{22}" rx="3" fill="#d9d2bf"/>'
        o += f'<rect x="14" y="{cy+8}" width="{self.W-28}" height="6" fill="#c3bba5"/>'
        # filets de rail
        for name, col in (("T+", RED), ("T-", BLUE), ("B+", RED), ("B-", BLUE)):
            y = {**self.rails_top, **self.rails_bot}[name]
            yy = y - 12 if name in ("T+", "B+") else y + 12
            o += f'<line x1="22" y1="{yy}" x2="{self.W-22}" y2="{yy}" stroke="{col}" stroke-width="2.6"/>'
            if rails_labels:
                o += T(14, y + 5, "+" if "+" in name else "−", 15, 800, col, "middle")
        # trous
        def hole(x, y):
            return f'<rect x="{x-3.4}" y="{y-3.4}" width="6.8" height="6.8" rx="1.4" fill="#2a2a2e"/>'
        for name in list(self.rails_top) + list(self.rails_bot):
            k = 0
            while True:
                x, y = self.rail(k, name)
                if x > self.W - 30:
                    break
                o += hole(x, y)
                k += 1
        for r in "abcde":
            for c in range(1, self.cols + 1):
                x, y = self.xy(c, r)
                o += hole(x, y)
        for r in "fghij":
            for c in range(1, self.cols + 1):
                x, y = self.xy(c, r)
                o += hole(x, y)
        if numbers:
            for c in range(1, self.cols + 1):
                if c == 1 or c % 5 == 0:
                    x, _ = self.xy(c, "a")
                    o += T(x, 72, str(c), 12, 600, "#7d7767")
        if letters:
            for r in "abcde":
                o += T(22, self.top_rows[r] + 4, r, 12, 600, "#7d7767")
            for r in "fghij":
                o += T(22, self.bot_rows[r] + 4, r, 12, 600, "#7d7767")
        return o

    def wire(self, a, b, color="#d63f3f", bow=0):
        (x1, y1), (x2, y2) = a, b
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2 - 14 - bow
        o = (f'<path d="M{x1},{y1} Q{mx},{my} {x2},{y2}" fill="none" stroke="#000" stroke-opacity=".18" stroke-width="7" stroke-linecap="round" transform="translate(1.5,2.5)"/>'
             f'<path d="M{x1},{y1} Q{mx},{my} {x2},{y2}" fill="none" stroke="{color}" stroke-width="5.5" stroke-linecap="round"/>'
             f'<path d="M{x1},{y1} Q{mx},{my} {x2},{y2}" fill="none" stroke="#fff" stroke-opacity=".35" stroke-width="1.6" stroke-linecap="round" transform="translate(0,-1.5)"/>'
             f'<circle cx="{x1}" cy="{y1}" r="4.6" fill="{color}"/><circle cx="{x2}" cy="{y2}" r="4.6" fill="{color}"/>')
        return o


def noisy_path(x0, y0, w, amp, cycles, noise, n=400, seed=3, phase=0.0, sx=1.0):
    rnd = random.Random(seed)
    pts = []
    for i in range(n + 1):
        t = i / n
        y = y0 - amp * math.sin(2 * math.pi * cycles * t + phase) + rnd.uniform(-noise, noise)
        pts.append((x0 + w * t, y))
    return "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts)


def sine_path(x0, y0, w, amp, cycles, n=240, phase=0.0):
    pts = []
    for i in range(n + 1):
        t = i / n
        pts.append((x0 + w * t, y0 - amp * math.sin(2 * math.pi * cycles * t + phase)))
    return "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts)


def dc_sym(x, y, color=INK, w=22):
    return (f'<line x1="{x-w/2}" y1="{y}" x2="{x+w/2}" y2="{y}" stroke="{color}" stroke-width="3"/>'
            f'<path d="M{x-w/2},{y+6} h5 M{x-3},{y+6} h6 M{x+w/2-5},{y+6} h5" stroke="{color}" stroke-width="3"/>')


def ac_sym(x, y, color=INK):
    return f'<path d="M{x-11},{y} q5.5,-9 11,0 t11,0" fill="none" stroke="{color}" stroke-width="3" stroke-linecap="round"/>'
