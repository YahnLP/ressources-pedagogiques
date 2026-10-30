"""Ajoute, sous les exercices, les réponses en zones déroulables.

Chaque entrée : (année, séance, fichier, début du titre de l'exercice, lignes de réponse).
Règle de maintenance : tout exercice à compléter doit avoir ses réponses dans une zone déroulable.
"""
import glob, sys
from pathlib import Path

ENTREES = [
    ('seconde', 'S01', '01-cours.md', '### 🧮 Exercice 1', ["1. 12 000 Ω = 12 kΩ  ", "2. 4 700 Ω = 4,7 kΩ  ", "3. 560 Ω = 0,56 kΩ"]),
    ('seconde', 'S01', '01-cours.md', '### 🧮 Exercice 2', ["1. $I = \\dfrac{U}{R} = \\dfrac{12}{600} = 0{,}02\\,\\mathrm{A} = 20\\,\\mathrm{mA}$  ", "2. $U = R \\times I = 200 \\times 0{,}05 = 10\\,\\mathrm{V}$  ", "3. $R = \\dfrac{U}{I} = \\dfrac{9}{0{,}003} = 3\\,000\\,\\Omega = 3\\,\\mathrm{k\\Omega}$"]),
    ('seconde', 'S01', '01-cours.md', '### 🧮 Exercice 3', ["1. 4 700 Ω = 4,7 kΩ  ", "2. 0,025 A = 25 mA  ", "3. 2,2 MΩ = 2 200 000 Ω  ", "4. 150 mA = 0,15 A"]),
    ('seconde', 'S03', '01-cours.md', '### Exercice 1 — Lire un schéma', ["1. D1 et D2 sont en **parallèle** (leurs deux bornes sont reliées aux mêmes points).  ", "2. $U_{R1} = V_{alim} - V_F = 9 - 2 = 7\\,\\mathrm{V}$  ", "3. $I_{total} = \\dfrac{U_{R1}}{R_1} = \\dfrac{7}{470} \\approx 0{,}0149\\,\\mathrm{A} \\approx 14{,}9\\,\\mathrm{mA}$  ", "4. Les deux branches sont identiques en courant : $I_{D1} = \\dfrac{14{,}9}{2} \\approx 7{,}4\\,\\mathrm{mA}$"]),
    ('premiere', 'S11', '03-exercices.md', '### Exercice 1.1', ["**Q1.1.a** : 45 min = 0,75 h · 3 h 20 min ≈ 3,33 h · 1 h 00 = 1 h · 7 h 15 min = 7,25 h  ", "**Q1.1.b** : TA = 0,75 + 3,33 + 1 + 7,25 ≈ 12,33 h · TO = 3 × 8 760 − 12,33 ≈ 26 267,67 h  ", "MTBF = 26 267,67 / 4 ≈ 6 566,9 h · MTTR = 12,33 / 4 ≈ 3,08 h  ", "$D = \\dfrac{6\\,566{,}9}{6\\,566{,}9 + 3{,}08} \\approx 0{,}99953 = 99{,}95\\,\\%$  ", "**Q1.1.c** : 6 566,9 / 730 ≈ 9 mois : une panne tous les 9 mois environ  ", "**Q1.1.d** : 99,95 % ≥ 99,5 % : conforme"]),
    ('premiere', 'S11', '03-exercices.md', '### Exercice 1.2', ["$MTTR \\leq \\dfrac{6\\,566{,}9 \\times 0{,}001}{0{,}999} \\approx 6{,}57\\,\\mathrm{h}$  ", "Le MTTR actuel est de 3,08 h : il est déjà inférieur à 6,57 h, donc l'objectif D ≥ 99,9 % est déjà atteint (D = 99,95 %). Aucune réduction n'est nécessaire ; pour garder cette marge, on peut tenir des pièces de rechange en stock."]),
    ('premiere', 'S11', '03-exercices.md', '### Exercice 1.3', ["**Q1.3.a** : HDD : $D = \\dfrac{300\\,000}{300\\,004} \\approx 99{,}9987\\,\\%$  ", "SSD : $D = \\dfrac{1\\,500\\,000}{1\\,500\\,001} \\approx 99{,}99993\\,\\%$  ", "NVMe : $D = \\dfrac{2\\,000\\,000}{2\\,000\\,000{,}5} \\approx 99{,}999975\\,\\%$  ", "**Q1.3.b** : Faux : le HDD n'atteint pas 99,999 % mais le SSD et le NVMe l'atteignent. La solution la plus proche est le NVMe (99,999975 %), qui dépasse l'objectif d'environ 0,001 point."]),
    ('premiere', 'S11', '03-exercices.md', '### Exercice 2.1', ["**Q2.1.a** : $\\lambda = \\dfrac{1}{50\\,000} = 2 \\times 10^{-5}$ panne/heure  ", "**Q2.1.b** :  ", "- 1 an : $\\lambda t = 0{,}1752$ ; $R = e^{-0{,}1752} \\approx 0{,}839$ soit 83,9 %  ", "- 2 ans : $\\lambda t = 0{,}3504$ ; $R \\approx 0{,}704$ soit 70,4 %  ", "- 5 ans : $\\lambda t = 0{,}876$ ; $R \\approx 0{,}416$ soit 41,6 %  ", "- MTBF : $\\lambda t = 1$ ; $R = 0{,}368$ soit 36,8 %  ", "**Q2.1.c** : R(8 760) ≈ 83,9 % : sur 1 000 capteurs, environ 839 fonctionnent encore et 161 sont en panne.  ", "**Q2.1.d** : $t \\leq \\dfrac{0{,}105}{2 \\times 10^{-5}} \\approx 5\\,268\\,\\mathrm{h} \\approx 7{,}2$ mois"]),
    ('premiere', 'S11', '03-exercices.md', '### Exercice 2.2', ["**Q2.2.a** : $\\lambda_A = 10^{-4}\\,\\mathrm{h^{-1}}$ ; $\\lambda_B = 10^{-5}\\,\\mathrm{h^{-1}}$  ", "**Q2.2.b** :  ", "- 1 000 h : $R_A = 0{,}905$ ; $R_B = 0{,}990$ ; écart 0,085  ", "- 5 000 h : $R_A = 0{,}607$ ; $R_B = 0{,}951$ ; écart 0,344  ", "- 10 000 h : $R_A = 0{,}368$ ; $R_B = 0{,}905$ ; écart 0,537  ", "- 50 000 h : $R_A = 0{,}0067$ ; $R_B = 0{,}607$ ; écart 0,600  ", "**Q2.2.c** : 2 ans = 17 520 h. $R_A = e^{-1{,}752} \\approx 0{,}173$ soit 17,3 % ; $R_B = e^{-0{,}1752} \\approx 0{,}839$ soit 83,9 %.  ", "Conclusion : le composant B (premium) est indispensable, car A n'a que 17 % de chances de tenir 2 ans sans panne."]),
    ('premiere', 'S11', '03-exercices.md', '### Exercice 3.1', ["**Q3.1.a** : $R_{CPU} = 1 - (1 - 0{,}90)(1 - 0{,}90) = 1 - 0{,}10 \\times 0{,}10 = 0{,}99$  ", "**Q3.1.b** : $R_s = 0{,}95 \\times 0{,}99 \\times 0{,}99 \\approx 0{,}931 = 93{,}1\\,\\%$  ", "**Q3.1.c** : sans redondance : $0{,}95 \\times 0{,}90 \\times 0{,}99 \\approx 0{,}846 = 84{,}6\\,\\%$ ; gain de la redondance : 93,1 − 84,6 ≈ 8,5 points"]),
    ('premiere', 'S11', '03-exercices.md', '### Exercice 3.2', ["**Q3.2.a** : $R_{capteurs} = 1 - (1 - 0{,}88)(1 - 0{,}85) = 1 - 0{,}12 \\times 0{,}15 = 0{,}982$  ", "**Q3.2.b** : $R_s = 0{,}982 \\times 0{,}92 \\times 0{,}97 \\times 0{,}99 \\approx 0{,}868 = 86{,}8\\,\\%$  ", "**Q3.2.c** : l'ESP32 (R = 0,92) est le maillon le plus faible de la chaîne en série : on le double en redondance (deux ESP32 en parallèle, $R = 1 - 0{,}08^2 = 0{,}9936$), d'où $R_s = 0{,}982 \\times 0{,}9936 \\times 0{,}97 \\times 0{,}99 \\approx 0{,}937 = 93{,}7\\,\\%$."]),
    ('terminale', 'S03', '02-tp.md', '## 🟢 EXERCICE 1', ["**Q1.a et Q1.b** : $I_{moy}$ ESP32 = (150 × 5 + 10 × 25) / 30 = (750 + 250) / 30 ≈ 33,3 mA, soit 25 mA (actif) + 8,3 mA (veille).", "", "| Composant | $I_{moy}$ (mA) | $P_{moy}$ (mW) |", "|---|---|---|", "| ESP32 actif WiFi | 25 | 82,5 |", "| ESP32 veille | 8,3 | 27,5 |", "| DHT22 | 0,25 | 0,8 |", "| LED (1 s ON / 4 s OFF) | 2 | 6,6 |", "| **TOTAL 3,3 V** | 35,6 (pic : 161,5) | 117 |", "", "**Q1.c** : $I_{moy}$ LED = 10 × (1 / 5) = 2 mA  ", "**Q1.d** : côté 5 V : 35,6 + 150 ≈ 185,6 mA ; courant de pointe : 150 + 1,5 + 10 + 150 = 311,5 mA  ", "**Q1.e** : t = 2 000 / 185,6 ≈ 10,8 h ; $t_{réelle}$ ≈ 10,8 × 0,80 ≈ 8,6 h"]),
    ('terminale', 'S03', '02-tp.md', '## 🟡 EXERCICE 2', ["**Q2.a** : $P_{diss} = 1{,}7 \\times 0{,}0356 \\approx 0{,}060\\,\\mathrm{W}$  ", "**Q2.b** : $T_j = 25 + 0{,}060 \\times 44 \\approx 27{,}7\\,°\\mathrm{C}$  ", "**Q2.c** : $T_j$ ≈ 27,7 °C < 105 °C : aucun radiateur nécessaire.  ", "**Q2.d** : avec $I_{pic}$ = 311,5 mA (valeur de Q1.d) : $P_{diss}$ = 1,7 × 0,3115 ≈ 0,53 W ; $T_j$ = 25 + 0,53 × 44 ≈ 48 °C < 125 °C : le LDO survit au pic. (Le MQ-2 est alimenté directement en 5 V : seul 161,5 mA traverse réellement le LDO, soit 0,27 W et environ 37 °C.)  ", "**Q2.e** : $T_j$ = 60 + 0,060 × 44 ≈ 62,7 °C < 105 °C : conforme, aucune action requise."]),
    ('terminale', 'S03', '02-tp.md', '## 🟠 EXERCICE 3', ["**Application A** : Boost (ou buck-boost), par exemple TPS61200 ou MT3608 : la tension de la pile (3 V) est inférieure aux 3,3 V demandés, seul un convertisseur élévateur convient.  ", "**Application B** : $P_{diss}$ = (12 − 5) × 2 = 14 W. Type recommandé : Buck. Un régulateur linéaire dissiperait 14 W en chaleur ; le découpage a un rendement d'environ 90 % et chauffe très peu.  ", "**Application C** : Linéaire (LM7815 / LM7915). Il ne commute pas : pas de bruit de découpage ni d'émissions CEM sur le signal analogique, la tension reste très propre."]),
]


def main(root):
    for y, s, fn, titre, rep in ENTREES:
        d = Path(glob.glob(f'{root}/docs/{y}/{s}-*')[0]); f = d / fn
        L = f.read_text(encoding='utf-8').split('\n')
        i = next((k for k, l in enumerate(L) if l.startswith(titre)), None)
        if i is None: print('introuvable', y, s, titre); continue
        niv = len(titre) - len(titre.lstrip('#'))
        j = next((k for k in range(i + 1, len(L)) if L[k].strip() == '---' or (L[k].startswith('#') and len(L[k]) - len(L[k].lstrip('#')) <= niv)), len(L))
        if any(l.startswith('??? success') for l in L[i:j]): continue
        L[j:j] = ['??? success "Réponses"'] + ['    ' + x for x in rep] + ['']
        f.write_text('\n'.join(L), encoding='utf-8')


if __name__ == '__main__':
    main(sys.argv[1])
