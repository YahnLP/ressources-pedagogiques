"""Icônes de symboles normalisés CEI pour les tableaux (fond transparent)."""
from lib import *

IW, IH = 260, 100


def icon(body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{IW}" height="{IH}" viewBox="0 0 {IW} {IH}" font-family="Inter, Helvetica, Arial, sans-serif">{DEFS}{body}</svg>')


def S(kind, s=1.3, **kw): return sym(kind, 130, 50, s=s, **kw)


def i_fil(): return icon(s_wire([(70, 50), (190, 50)]))
def i_jonction(): return icon(s_wire([(70, 50), (190, 50)]) + s_wire([(130, 12), (130, 88)]) + dot(130, 50, 8))
def i_croisement(): return icon(f'<path d="M70,50 H118 A12,12 0 0 1 142,50 H190" fill="none" stroke="{INK}" stroke-width="3.2" stroke-linecap="round"/>' + s_wire([(130, 12), (130, 88)]))
def i_masse(): return icon(gnd(130, 14))
def i_pile():
    o = s_wire([(60, 50), (96, 50)]) + s_wire([(164, 50), (200, 50)])
    for k, x in enumerate((96, 114, 132, 150)):
        o += f'<path d="M{x},{50-(22 if k%2==0 else 12)} V{50+(22 if k%2==0 else 12)}" stroke="{INK}" stroke-width="{3.8 if k%2==0 else 6}"/>'
    o += s_wire([(150, 50), (164, 50)]) + T(82, 36, "+", 20, 800) + T(178, 36, "−", 22, 800)
    return icon(o)
def i_ci():
    o = f'<rect x="85" y="14" width="90" height="72" fill="#fff" stroke="{INK}" stroke-width="3.2"/>'
    for k in range(3):
        y = 30 + k * 20
        o += s_wire([(60, y), (85, y)]) + s_wire([(175, y), (200, y)]) + T(95, y + 5, str(k + 1), 13, 700, MUTED, "start")
    return icon(o + T(130, 56, "CI", 22, 800))
def i_connecteur(): return icon(s_wire([(90, 50), (190, 50)]) + f'<circle cx="82" cy="50" r="9" fill="#fff" stroke="{INK}" stroke-width="3.2"/>')
def i_capteur():
    o = s_wire([(60, 50), (90, 50)]) + s_wire([(170, 50), (200, 50)]) + f'<rect x="90" y="22" width="80" height="56" fill="#fff" stroke="{INK}" stroke-width="3.2"/>'
    return icon(o + T(130, 62, "θ", 32, 700, INK, extra='font-family="serif" font-style="italic"'))
def i_regulateur():
    o = f'<rect x="85" y="14" width="90" height="56" fill="#fff" stroke="{INK}" stroke-width="3.2"/>' + s_wire([(60, 32), (85, 32)]) + s_wire([(175, 32), (200, 32)]) + s_wire([(130, 70), (130, 90)])
    return icon(o + T(95, 38, "IN", 13, 800, INK, "start") + T(165, 38, "OUT", 13, 800, INK, "end") + T(130, 62, "78xx", 15, 800, MUTED) + T(142, 88, "GND", 11, 800, INK, "start"))
def i_relais():
    o = s_wire([(40, 50), (62, 50)]) + f'<rect x="62" y="36" width="56" height="28" fill="#fff" stroke="{INK}" stroke-width="3.2"/>' + s_wire([(118, 50), (140, 50)])
    o += f'<path d="M90,36 V22 H168 V32" stroke="{MUTED}" stroke-width="2.5" stroke-dasharray="5 4" fill="none"/>'
    o += s_wire([(156, 80), (180, 80)]) + s_wire([(210, 80), (234, 80)]) + s_wire([(180, 80), (206, 56)]) + f'<circle cx="180" cy="80" r="4" fill="#fff" stroke="{INK}" stroke-width="2.5"/><circle cx="210" cy="80" r="4" fill="#fff" stroke="{INK}" stroke-width="2.5"/>'
    return icon(o)
def i_opto():
    o = f'<rect x="50" y="10" width="160" height="80" fill="none" stroke="{INK}" stroke-width="2.5" stroke-dasharray="7 5"/>'
    o += g(105, 50, '<path d="M0,-22 V22" stroke="#1b2742" stroke-width="3.5"/><path d="M0,-18 L0,18 L-22,0Z" fill="none" stroke="#1b2742" stroke-width="0"/><path d="M-20,-18 L-20,18 L0,0 Z" fill="#fff" stroke="#1b2742" stroke-width="3" transform="rotate(0)"/>', 0.9)
    o += f'<path d="M122,38 L140,28 M122,52 L140,42" stroke="{INK}" stroke-width="2.5" marker-end="url(#arr)"/>'
    o += g(170, 50, f'<path d="M-4,-18 V18" stroke="{INK}" stroke-width="4"/><path d="M-4,-8 L16,-20 M-4,8 L16,20" stroke="{INK}" stroke-width="3"/><path d="M12,16 L4,15 L9,8Z" fill="{INK}"/>', 1)
    return icon(o)


ICONS = {
    "source-continue": lambda: icon(S("BAT")), "pile": i_pile, "resistance": lambda: icon(S("R")), "diode": lambda: icon(S("D")), "led": lambda: icon(sym("LED", 130, 58, s=1.3)),
    "condo": lambda: icon(S("C")), "condo-polarise": lambda: icon(S("CP")), "inter-no": lambda: icon(sym("SW", 130, 62, s=1.3)), "inter-nf": lambda: icon(S("SW", closed=True)),
    "poussoir-no": lambda: icon(sym("BP", 130, 64, s=1.2)), "fil": i_fil, "jonction": i_jonction, "croisement": i_croisement, "masse": i_masse, "lampe": lambda: icon(S("LAMP")),
    "npn": lambda: icon(npn(130, 50, 0.95)), "pnp": lambda: icon(npn(130, 50, 0.95, "pnp")), "ci": i_ci, "connecteur": i_connecteur, "capteur": i_capteur, "moteur": lambda: icon(S("MOTOR")),
    "fusible": lambda: icon(S("FUSE")), "regulateur": i_regulateur, "relais": i_relais, "optocoupleur": i_opto,
}
FIGS = {f"sym-{k}": v for k, v in ICONS.items()}
