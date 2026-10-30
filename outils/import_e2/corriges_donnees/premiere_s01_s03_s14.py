"""Première S01, S03, S14 : valeurs attendues (calculs, règles) et exemple de fiche de dépannage."""
VA = "Valeurs attendues"
ENTREES = [
    ('premiere', 'S01', '02-tp.md', '## 🟠 NIVEAU 3', [
        "**3.1** — $12 \\times \\dfrac{10}{R_1 + 10} = 5$ donne $R_1 + 10 = \\dfrac{120}{5} = 24$, donc $R_1 = 14\\,\\mathrm{k\\Omega}$. Valeur commerciale la plus proche (série E12) : **15 kΩ**, qui donne $V_m = 12 \\times \\dfrac{10}{25} = 4{,}8\\,\\mathrm{V}$ (écart de 4 %). On peut aussi prendre 12 kΩ + 2,2 kΩ en série (14,2 kΩ) pour 4,95 V."], VA),
    ('premiere', 'S01', '02-tp.md', '## 🔵 NIVEAU 4', [
        "$R_c = \\dfrac{5 - 2 - 0{,}2}{0{,}020} = 140\\,\\Omega$ → valeur normalisée **150 Ω** ($I_F \\approx 18{,}7\\,\\mathrm{mA}$).  ",
        "$I_b = \\dfrac{20\\,\\mathrm{mA}}{200} = 100\\,\\mu\\mathrm{A}$ ; $R_b = \\dfrac{5 - 0{,}7}{100\\,\\mu\\mathrm{A}} = 43\\,\\mathrm{k\\Omega}$.  ",
        "En pratique, on choisit une valeur **plus faible** (par exemple 10 kΩ à 39 kΩ) pour garantir que le transistor sature malgré la dispersion du gain $h_{FE}$.  ",
        "Dans le schéma : R1 (Rb) ≈ 10 à 43 kΩ ; R2 (Rc) = 150 Ω."], VA),
    ('premiere', 'S01', '02-tp.md', '## 🔴 NIVEAU 5', [
        "**5.1** — Reference = `Q1` ; Value = `BC547`.  ",
        "**5.2** — Le schéma contient 4 références différentes (R1, R2, D1, Q1), plus éventuellement l'alimentation si elle est une pile."], VA),
    ('premiere', 'S03', '02-tp.md', '## 🟢 NIVEAU 1', [
        "**1.1** — Empreintes usuelles : R1, R2 : `Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal` ; D1 : `LED_THT:LED_D5.0mm` ; Q1 : `Package_TO_SOT_THT:TO-92_Inline`.  ",
        "**1.3** — Les 6 composants (R1, R2, D1, Q1, BT1, J1) sont visibles : oui ; ratsnest visible : oui ; connexions à relier : **7** (réseau minimal : 2 pour GND, 5 pour les autres liaisons)."], VA),
    ('premiere', 'S03', '02-tp.md', '## 🟡 NIVEAU 2', [
        "Clearance : **0,2 mm** ; largeur de piste signal : **0,35 mm** ; via : **0,8 mm** de diamètre et **0,4 mm** de perçage ; largeur de piste d'alimentation : **0,8 mm**. Contour : rectangle de 60 × 50 mm sur Edge.Cuts."], VA),
    ('premiere', 'S03', '02-tp.md', '## 🔵 NIVEAU 4', [
        "Pistes à router : **7** (réseau minimal). Ratsnest restant après routage : **0**. Pistes d'alimentation visiblement plus larges : **oui** (0,8 mm). Via nécessaires sur un circuit aussi simple : en général **aucun** (tout se route en simple face)."], VA),
    ('premiere', 'S03', '02-tp.md', '## 🔴 NIVEAU 5', [
        "DRC final attendu : **0 erreur** (des avertissements de sérigraphie peuvent subsister et se règlent en déplaçant les textes). Causes d'erreurs fréquentes : clearance insuffisante entre deux pistes, piste trop proche du bord, pads qui se touchent, courtyards qui se recouvrent."], VA),
    ('premiere', 'S14', '02-tp.md', '## ÉTAPE A', [
        "**Exemple de fiche remplie** (panne : l'ESP32 redémarre en boucle quand le WiFi s'active) :  ",
        "- **D** : redémarrage toutes les quelques secondes, LED qui clignote irrégulièrement ; moniteur : `Brownout detector was triggered`.  ",
        "- **E** : hypothèses : alimentation insuffisante (câble USB, régulateur), code qui plante, capteur en court-circuit, antenne ; le message brownout écarte le code.  ",
        "- **C** : mesure du VCC sous charge (valeur attendue : 3,3 V ± 5 %, mesuré : 2,9 V pendant l'émission WiFi) ; dichotomie : alimenter la carte par une autre source → panne disparue → l'alimentation d'origine est en cause ; cause racine : **câble USB trop long ou de mauvaise qualité (chute de tension)**.  ",
        "- **A** : remplacer le câble par un câble court, ajouter un condensateur de 100 µF près de l'ESP32 ; tests : fonctionnel PASS, I2C PASS, MQTT PASS, aucun reset en 2 min PASS.  ",
        "- **Amélioration préventive** : prévoir un condensateur de découplage et une alimentation dimensionnée pour le courant de pointe WiFi (≈ 250 mA)."], "Exemple de fiche"),
]
