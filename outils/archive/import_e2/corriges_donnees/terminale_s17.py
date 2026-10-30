"""Terminale S17 : réponses du sprint TP (stations 1 et 2) — calculs vérifiés."""
F = '02-tp.md'
E = lambda t, l: ('terminale', 'S17', F, t, l)
ENTREES = [
    E('### Calcul 1', [
        "$I_{LED} = \\dfrac{3{,}3 - 2{,}0}{330} \\approx 3{,}94\\,\\mathrm{mA}$ ; $I_{charge} = \\dfrac{3{,}3}{56} \\approx 58{,}9\\,\\mathrm{mA}$ ; $I_{LDO} = 80 + 1{,}5 + 3{,}94 + 58{,}9 \\approx 144{,}4\\,\\mathrm{mA}$.  ",
        "$P_{diss} = 1{,}7 \\times 0{,}1444 \\approx 0{,}245\\,\\mathrm{W}$ ; $T_j = 28 + 0{,}245 \\times 44 \\approx 38{,}8\\,°\\mathrm{C}$ ; marge $= 105 - 38{,}8 \\approx 66\\,°\\mathrm{C}$ (par rapport à $T_j$ max exploitable de 105 °C)."]),
    E('### Calcul 2', [
        "$I_{charge} = \\dfrac{3{,}3}{47} \\approx 70{,}2\\,\\mathrm{mA}$ ; $I_{moy,ESP32} = \\dfrac{180 \\times 15 + 0{,}05 \\times 285}{300} \\approx 9{,}05\\,\\mathrm{mA}$.  ",
        "$I_{moy,total} = 9{,}05 + 1{,}5 + 70{,}2 \\approx 80{,}8\\,\\mathrm{mA}$ ; $I_{batterie} = \\dfrac{80{,}8}{0{,}90} \\approx 89{,}7\\,\\mathrm{mA}$.  ",
        "Autonomie $= \\dfrac{1500}{89{,}7} \\times 0{,}80 \\approx 13{,}4\\,\\mathrm{h} \\approx 0{,}56$ jour. La résistance de charge consomme presque tout : c'est elle qu'il faut revoir pour tenir plusieurs jours."]),
    E('### Calcul 3', [
        "$R_{capteurs} = 1 - 0{,}12 \\times 0{,}18 = 0{,}9784$ ; $R_s = 0{,}9784 \\times 0{,}96 \\times 0{,}99 \\approx 0{,}930 = 93{,}0\\,\\%$.  ",
        "$\\sigma_{EV} = \\dfrac{0{,}12 + 0{,}09}{2} = 0{,}105\\,°\\mathrm{C}$ ; $\\sigma_{AV} \\approx \\dfrac{0{,}3}{\\sqrt{8}} \\approx 0{,}106\\,°\\mathrm{C}$ ; $\\sigma_{GRR} = \\sqrt{0{,}105^2 + 0{,}106^2} \\approx 0{,}149\\,°\\mathrm{C}$.  ",
        "$\\%GRR = \\dfrac{5{,}15 \\times 0{,}149}{1{,}0} \\times 100 \\approx 77\\,\\%$ : **inacceptable** (> 30 %)."]),
    E('### PV à compléter', [
        "| Paramètre | Plage | Mesuré | Conforme ? |", "|---|---|---|---|",
        "| R_LED | [209 ; 231] Ω | 390 Ω | **KO** |",
        "| C1 | [80 ; 120] µF | 95 µF | OK |",
        "| Vcc | [3,267 ; 3,333] V | 3,29 V | OK |",
        "| Vf LED | [1,8 ; 2,2] V | 1,95 V | OK |",
        "| DHT22 | ≤ 0,5 °C | 0,53 °C ($0{,}35 + 0{,}18$) | **KO** |",
        "| Tj LDO | < 105 °C | 32 °C | OK |",
        "",
        "**NC 1** — $R_{LED} = 390\\,\\Omega$ : écart de $+77\\,\\%$ pour une tolérance de 5 %. Le courant dans la LED tombe à $\\dfrac{3{,}3 - 1{,}95}{390} \\approx 3{,}5\\,\\mathrm{mA}$ au lieu de $\\approx 6\\,\\mathrm{mA}$ : la LED éclaire moins. Probable erreur de composant (390 Ω posé à la place de 220 Ω) : le remplacer.  ",
        "**NC 2** — DHT22 : $|\\bar{e}| + U = 0{,}35 + 0{,}18 = 0{,}53\\,°\\mathrm{C}$, légèrement au-dessus de 0,5 °C. Hors spécification de peu : recalibrer (correction de +0,35 °C) ou refaire la mesure.  ",
        "**Synthèse puissance** : $P_{diss} = 1{,}7 \\times 0{,}107 \\approx 0{,}182\\,\\mathrm{W}$ ; $T_j = 24 + 0{,}182 \\times 44 \\approx 32\\,°\\mathrm{C}$ ; marge $\\approx 73\\,°\\mathrm{C}$. Autonomie : 2,1 jours pour un objectif de 3 : **non atteint**.  ",
        "**Décision** : **REFUSÉE** (proposition). Motif : R_LED hors tolérance de façon importante ; DHT22 hors spécification ; autonomie inférieure à l'objectif. Les points électriques critiques (Vcc, Tj) sont conformes ; après remplacement de R_LED, recalibrage du DHT22 et optimisation de la consommation, une nouvelle recette est nécessaire."]),
]
