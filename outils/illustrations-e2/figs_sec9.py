"""Schémas remplaçant les dessins en texte (Seconde S03, S09, S10 ; Première S01-S02)."""
from hl import *
from figs_sec5 import f_schema_parallele_iec


def f_ex1():
    L, Tp, B, J, X1, X2 = 150, 130, 330, 470, 690, 900
    o = vrun(L, Tp, B, [(230, "BAT", "9 V", {})], -1) + hrun(Tp, L, J, [(320, "R", "R1 = 470 Ω", {})]) + dot(J, Tp)
    o += s_wire([(J, Tp), (X2, Tp)]) + dot(X1, Tp)
    for x, nm in ((X1, "D1 (rouge)"), (X2, "D2 (verte)")): o += vrun(x, Tp, B, [(230, "LED", nm, {})], 1, 60)
    o += s_wire([(L, B), (X2, B)]) + dot(X1, B) + gnd(L + 250, B) + T(L + 250, B + 60, "GND", 17, 800, INK)
    return figure(W, 440, o)


def f_cablage_lm35():
    o = '<g filter="url(#sh)"><rect x="60" y="80" width="330" height="330" rx="16" fill="#1c6c9a"/></g>' + T(225, 125, "Arduino Uno", 22, 800, "#fff")
    for y, t in ((200, "5V"), (280, "GND"), (360, "A0")): o += f'<rect x="372" y="{y-10}" width="30" height="20" fill="#c0c6cf"/>' + T(350, y + 6, t, 18, 800, "#fff", "end")
    o += '<g filter="url(#sh)"><path d="M780,120 L780,170 Q780,120 850,120 Q920,120 920,170 L920,200 L780,200 Z" fill="#222"/></g>' + T(850, 168, "LM35", 20, 800, "#fff")
    for x, n, t, c in ((800, "1", "VCC (+5 V)", RED), (850, "2", "OUT → A0", AMBER), (900, "3", "GND", "#222")):
        pass
    pins = [(800, "1", "VCC", RED, 200), (850, "2", "OUT", AMBER, 360), (900, "3", "GND", "#444", 280)]
    for x, n, t, c, ya in pins:
        o += f'<rect x="{x-4}" y="200" width="8" height="70" fill="#c0c6cf"/>' + T(x, 300, n, 15, 800, MUTED) + T(x, 322, t, 15, 800, INK)
        o += f'<path d="M402,{ya} C560,{ya} 640,{270} {x},270" stroke="{c}" stroke-width="6" fill="none" stroke-linecap="round"/>'
    o += T(850, 100, "face plate vers vous", 15, 700, MUTED) + chip(600, 440, "5V → broche 1 · A0 → broche 2 (OUT) · GND → broche 3", INK, w=760, size=16)
    return figure(W, 480, o)


def f_l293d():
    o = '<rect x="470" y="40" width="260" height="420" rx="10" fill="#25282e"/><path d="M570,40 a30,30 0 0 0 60,0" fill="#fff"/>' + T(600, 270, "L293D", 28, 800, "#fff") + T(600, 305, "vue de dessus", 14, 600, "#9aa4b2")
    L = ["EN1", "IN1", "OUT1", "GND", "GND", "OUT2", "IN2", "VCC2"]; R = ["VCC1 (5 V Arduino)", "IN4", "OUT4", "GND", "GND", "OUT3", "IN3", "EN2"]
    for i in range(8):
        y = 88 + i * 48
        o += f'<rect x="440" y="{y-8}" width="30" height="16" fill="#c0c6cf"/><rect x="730" y="{y-8}" width="30" height="16" fill="#c0c6cf"/>' + T(430, y + 6, L[i], 16, 700, INK, "end") + T(770, y + 6, R[i], 16, 700, INK, "start") + T(488, y + 5, str(i + 1), 13, 700, "#9aa4b2", "start") + T(712, y + 5, str(16 - i), 13, 700, "#9aa4b2", "end")
    return figure(W, 500, o)


def f_kicad_main():
    o = f'<g filter="url(#sh)"><rect x="60" y="30" width="1080" height="450" rx="10" fill="#f6f7fa" stroke="#aab3c5" stroke-width="2"/></g><rect x="60" y="30" width="1080" height="36" rx="10" fill="#e3e6ee"/>' + T(600, 55, "KiCad — Gestionnaire de projet", 16, 700, INK)
    o += f'<rect x="80" y="86" width="300" height="372" rx="6" fill="#fff" stroke="#d5dce8"/>' + T(100, 116, "Arborescence du projet", 15, 800, INK, "start") + "".join(T(110, 152 + i * 34, t, 15, 600, INK if i else BLUE, "start") for i, t in enumerate(("▾ projet", "   projet.kicad_pro", "   projet.kicad_sch", "   projet.kicad_pcb", "   projet.kicad_prl")))
    tools = [("Éditeur de schéma", "dessiner le schéma", BLUE), ("Éditeur de symboles", "créer des symboles", GREEN), ("Éditeur de PCB", "placer et router", AMBER), ("Éditeur d'empreintes", "créer des empreintes", "#8a56d0"), ("Visionneuse Gerber", "contrôler la fabrication", RED), ("Calculatrice", "outils de calcul", MUTED)]
    for i, (t, s, c) in enumerate(tools):
        x = 410 + (i % 3) * 235; y = 100 + (i // 3) * 170
        o += f'<rect x="{x}" y="{y}" width="215" height="150" rx="12" fill="#fff" stroke="{c}" stroke-width="3"/><rect x="{x+68}" y="{y+22}" width="80" height="56" rx="8" fill="{c}" opacity=".18"/><rect x="{x+82}" y="{y+34}" width="52" height="32" rx="4" fill="none" stroke="{c}" stroke-width="3"/>' + T(x + 107, y + 110, t, 16, 800, INK) + T(x + 107, y + 132, s, 13, 500, MUTED)
    o += T(790, 440, "Chaque outil s'ouvre depuis le gestionnaire", 15, 700, MUTED)
    return figure(W, 510, o)


FIGS = {"schema_exercice_lire": f_ex1, "cablage_lm35": f_cablage_lm35, "brochage_l293d": f_l293d, "kicad_fenetre_principale": f_kicad_main}
