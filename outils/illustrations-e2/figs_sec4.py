"""Figures complémentaires de Seconde (S01, S10, S12)."""
from lib import *
from figs04 import multimeter
from figs07 import block

W = 1200


def f_circuit_led():
    o = s_wire([(160, 250), (160, 130), (400, 130)]) + sym("R", 440, 130) + s_wire([(480, 130), (820, 130), (820, 200)])
    o += sym("LED", 820, 250, 90, s=1.2) + s_wire([(820, 298), (820, 370), (160, 370), (160, 330)]) + sym("BAT", 160, 290, 90, s=1.2)
    o += T(120, 292, "9 V", 28, 800, INK, "end") + T(440, 90, "330 Ω", 26, 800, INK) + T(440, 62, "marron · orange · marron", 15, 600, MUTED) + T(880, 252, "LED rouge", 22, 800, RED, "start") + T(880, 280, "2 V · 20 mA", 18, 700, INK, "start")
    o += arrow(560, 108, 720, 108, RED, 6) + T(640, 90, "sens du courant", 17, 800, RED)
    o += T(215, 270, "+", 26, 800, INK) if False else ""
    o += g(440, 210, '<rect x="-60" y="-14" width="120" height="28" rx="14" fill="url(#beige)" stroke="#a88f5a" stroke-width="2"/>' + ''.join(f'<rect x="{x-5}" y="-14" width="10" height="28" fill="{COLORS[c]}"/>' for x, c in ((-34, "marron"), (-8, "orange"), (18, "marron"))) + f'<rect x="38" y="-14" width="8" height="28" fill="{COLORS["or"]}"/>', 1)
    o += T(440, 255, "la résistance réelle", 14, 600, MUTED)
    o += T(500, 410, "I ≈ (9 V − 2 V) / 330 Ω ≈ 21 mA", 18, 700, MUTED)
    return figure(W, 440, o)


def f_unites():
    o = ""
    for k, (title, a, b, c, col, ex) in enumerate((("Courant", "A", "mA", "µA", BLUE, "0,02 A = 20 mA"), ("Résistance", "MΩ", "kΩ", "Ω", GREEN, "2,5 kΩ = 2 500 Ω"))):
        y = 60 + k * 230
        o += f'<rect x="40" y="{y-30}" width="1120" height="190" rx="16" fill="{PANEL}" stroke="#e1e7f1" stroke-width="2"/>' + T(70, y + 10, title, 22, 800, col, "start")
        for i, u in enumerate((a, b, c)):
            x = 250 + i * 330; o += f'<rect x="{x-70}" y="{y+20}" width="140" height="70" rx="14" fill="#fff" stroke="{col}" stroke-width="4"/>' + T(x, y + 66, u, 34, 800, INK)
            if i < 2:
                o += arrow(x + 80, y + 40, x + 250, y + 40, GREEN, 5) + T(x + 165, y + 28, "× 1 000", 17, 800, GREEN)
                o += arrow(x + 250, y + 74, x + 80, y + 74, RED, 5) + T(x + 165, y + 104, "÷ 1 000", 17, 800, RED)
        o += T(1130, y + 135, "Exemple : " + ex, 18, 700, INK, "end")
    return figure(W, 480, o)


def motor_panel(px, cw, label, col):
    o = panel(px, 30, 560, 430, label, accent=col) + '<g transform="translate(0,55)">'
    L = px + 120
    o += s_wire([(L, 250), (L, 150), (px + 280, 150)]) + s_wire([(px + 360, 150), (px + 460, 150), (px + 460, 350), (L, 350), (L, 290)])
    o += sym("BAT", L, 270, 90 if cw else 270, s=1.1) + T(L - 36, 275, "9 V", 18, 800, INK, "end")
    o += T(L + 36, 200 if cw else 345, "+", 26, 800, INK) if False else ""
    o += T(L + 40, 232 if cw else 312, "+", 24, 800, RED, "start") + T(L + 40, 312 if cw else 232, "−", 26, 800, INK, "start")
    o += g(px + 320, 150, '<circle r="34" fill="#fff" stroke="#1b2742" stroke-width="3.2"/><text y="9" font-size="26" font-weight="800" text-anchor="middle" fill="#1b2742">M</text>')
    o += T(px + 280, 128, "fil 1", 14, 800, MUTED) + T(px + 460, 128, "fil 2", 14, 800, MUTED, "end")
    cx, r, sweep = px + 320, 56, (1 if cw else 0)
    o += f'<path d="M{cx-r*0.85},{150-r*0.5} A{r},{r} 0 1 {sweep} {cx+r*0.85},{150-r*0.5}" fill="none" stroke="{col}" stroke-width="5" marker-end="url(#arr)"/>'
    return o + "</g>"


def f_moteur_sens():
    o = motor_panel(30, True, "Sens horaire : + vers le fil 1", BLUE) + motor_panel(610, False, "Sens antihoraire : + vers le fil 2 (pile inversée)", RED)
    o += T(150, 240, "+", 24, 800, INK, "start") if False else ""
    return figure(W, 490, o)


def f_l293d():
    o = f'<g filter="url(#sh)"><rect x="470" y="70" width="260" height="400" rx="12" fill="url(#black)"/></g>' + T(600, 110, "L293D", 24, 800, "#d8dde5") + T(600, 134, "brochage logique simplifié", 13, 600, "#9fb0d0")
    ins = [("1  EN1", 190, "#e8c53a", "Arduino D9"), ("2  IN1", 260, "#2f5bea", "Arduino D7"), ("7  IN2", 330, "#17935c", "Arduino D6"), ("4-5  GND", 400, "#222", "GND commun")]
    o += block(40, 130, 220, 300, "", None, BLUE) + T(150, 168, "Arduino UNO", 20, 800, INK)
    for lab, y, c, ard in ins:
        o += T(480, y + 6, lab, 16, 800, "#fff", "start") + s_wire([(260, y), (470, y)], c, 4) + T(265, y - 8, ard.replace("Arduino ", ""), 14, 800, INK, "start")
    o += T(600, 62, "", 1) + s_wire([(560, 70), (560, 30), (180, 30), (180, 130)], RED, 4) + T(380, 22, "pin 16  VCC1 = 5 V (Arduino)", 14, 800, RED)
    o += s_wire([(680, 70), (680, 40), (1000, 40), (1000, 330)], "#c0392b", 4) if False else ""
    o += T(740, 200, "OUT1  3", 16, 800, "#fff", "end") if False else ""
    o += T(720, 196, "3  OUT1", 16, 800, "#fff", "end") + T(720, 340, "6  OUT2", 16, 800, "#fff", "end")
    o += s_wire([(730, 190), (900, 190), (900, 220)], INK, 4) + s_wire([(730, 334), (900, 334), (900, 300)], INK, 4)
    o += g(900, 260, '<circle r="38" fill="#fff" stroke="#1b2742" stroke-width="3.2"/><text y="10" font-size="30" font-weight="800" text-anchor="middle" fill="#1b2742">M</text>') + T(960, 266, "moteur DC", 18, 800, INK, "start")
    o += T(720, 480, "8  VCC2 = 9 V (pile externe)", 16, 800, "#fff", "end") if False else ""
    o += s_wire([(600, 470), (600, 520), (1000, 520)], "#c0392b", 4) if False else ""
    o += T(600, 458, "8  VCC2", 16, 800, "#fff") + s_wire([(600, 470), (600, 510)], RED, 4) + sym("BAT", 600, 550, 90, s=0.8) if False else ""
    o += s_wire([(600, 470), (600, 500), (820, 500)], RED, 4) + T(600, 455, "8  VCC2 (moteur)", 15, 800, "#fff") + sym("BAT", 860, 500, s=1.0) + T(960, 506, "pile 9 V externe", 17, 800, INK, "start")
    o += s_wire([(300, 400), (300, 560), (900, 560)], "#222", 3) if False else ""
    o += T(600, 585, "Les GND (Arduino, pile 9 V, broches 4-5) sont reliés ensemble", 16, 800, INK)
    return figure(W, 620, o)


def f_continuite():
    o = ""
    for k, (disp, ok, title) in enumerate(((("0.3"), True, "Fil intact : BIP"), (("OL"), False, "Fil coupé : pas de bip"))):
        px = 30 + k * 590
        o += panel(px, 30, 560, 470, title, accent=GREEN if ok else RED)
        o += g(px + 130, 270, multimeter(display=disp), 0.55)
        o += s_wire([(px + 300, 330), (px + 540, 330)], INK, 8) if ok else s_wire([(px + 300, 330), (px + 400, 330)], INK, 8) + s_wire([(px + 440, 330), (px + 540, 330)], INK, 8)
        o += f'<circle cx="{px+300}" cy="330" r="12" fill="{RED}"/><circle cx="{px+540}" cy="330" r="12" fill="#222"/>'
        if ok: o += T(px + 420, 250, "♪ BIP", 34, 800, GREEN) + T(px + 420, 290, "continuité", 17, 700, MUTED)
        else: o += f'<g stroke="{RED}" stroke-width="8" stroke-linecap="round"><line x1="{px+405}" y1="305" x2="{px+435}" y2="355"/><line x1="{px+435}" y1="305" x2="{px+405}" y2="355"/></g>' + T(px + 420, 250, "pas de son", 22, 800, RED)
    return figure(W, 530, o)


FIGS = {"circuit_led_9v": f_circuit_led, "echelle_unites": f_unites, "moteur_sens": f_moteur_sens, "cablage_l293d": f_l293d, "continuite_multimetre": f_continuite}
