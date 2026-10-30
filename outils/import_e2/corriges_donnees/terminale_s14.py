"""Terminale S14 : réponses du cahier d'exercices de consolidation (calculs vérifiés)."""
F = '03-exercices.md'
E = lambda t, l: ('terminale', 'S14', F, t, l)
ENTREES = [
    E('## A1', [
        "**A1.1** — $\\bar{x} = \\dfrac{4680 + 4710 + 4695 + 4725 + 4690}{5} = \\dfrac{23\\,500}{5} = 4\\,700\\,\\Omega$.  ",
        "**A1.2** —", "",
        "| $x_i$ | $x_i - \\bar{x}$ | $(x_i - \\bar{x})^2$ |", "|---|---|---|",
        "| 4 680 | −20 | 400 |", "| 4 710 | +10 | 100 |", "| 4 695 | −5 | 25 |", "| 4 725 | +25 | 625 |", "| 4 690 | −10 | 100 |", "| **Σ** | 0 | 1 250 |", "",
        "$s = \\sqrt{\\dfrac{1250}{4}} \\approx 17{,}7\\,\\Omega$ ; $u_A = \\dfrac{17{,}7}{\\sqrt{5}} \\approx 7{,}9\\,\\Omega$.  ",
        "**A1.3** — $u_{B,rés} = \\dfrac{10}{2\\sqrt{3}} \\approx 2{,}9\\,\\Omega$ ; $u_{B,cl} = \\dfrac{1{,}0 \\times 4700}{173{,}2} \\approx 27{,}1\\,\\Omega$.  ",
        "**A1.4** — $u_c = \\sqrt{7{,}9^2 + 2{,}9^2 + 27{,}1^2} \\approx 28{,}4\\,\\Omega$ ; $U = 2 \\times 28{,}4 \\approx 56{,}8\\,\\Omega$, arrondi par excès à **60 Ω** (1 chiffre significatif). $R = (4\\,700 \\pm 60)\\,\\Omega$ [95 %].  ",
        "**A1.5** — Intervalle mesuré : $[4\\,640\\,;\\,4\\,760]\\,\\Omega$, entièrement dans $[4\\,465\\,;\\,4\\,935]$ : **conforme**."]),
    E('## A2', [
        "**A2.1** — La classe porte sur la **valeur lue**, pas sur la pleine échelle : avec 10 kΩ on obtient $u_{B,cl} \\approx 57{,}7\\,\\Omega$ au lieu de $27{,}1\\,\\Omega$, soit une incertitude **surestimée d'un facteur 2 environ**, donc un résultat trop pessimiste.  ",
        "**A2.2** — Éléments manquants : l'**incertitude** (± U avec le niveau de confiance), l'**instrument** utilisé avec son numéro de série et son étalonnage, la **tolérance / critère** de conformité, la **date**, l'**opérateur**, les **conditions** de mesure.  ",
        "**A2.3** — Un instrument **dérive** avec le temps et les chocs : le certificat n'est valable que pour une durée limitée. Utiliser un instrument hors validité rend les mesures **non garanties**, donc **sans valeur** dans un PV (non-conformité qualité, litige possible).  ",
        "**A2.4** — « Ininterrompue » : chaque instrument est comparé à un étalon plus précis, **sans maillon manquant**, jusqu'à l'étalon national. Si un maillon est rompu, la mesure n'est plus **opposable** (audit, contrat, litige)."]),
    E('## B1', [
        "**B1.1** — Après **5 mesures** (soit 25 s) le buffer est plein ; tant qu'il n'est pas plein, la fonction renvoie la **valeur brute** $v$ et non une moyenne.  ",
        "**B1.2** — Seuils : montée à 38,0 ; descente à 36,0.  ",
        "`OK / CRITIQUE / CRITIQUE / CRITIQUE / CRITIQUE / OK / OK`  ",
        "(37,8 et 36,5 restent critiques : on est entre les deux seuils, l'alarme ne se coupe qu'en dessous de 36,0).  ",
        "**B1.3** — `delay(15000)` **bloque tout le microcontrôleur** pendant 15 s : plus de mesure, de MQTT ni d'alarme. `millis()` mesure le temps sans bloquer.  ",
        "**B1.4** — `static` : la variable **conserve sa valeur entre deux appels** de la fonction. Sans cela, `debord` serait remise à zéro à chaque appel et le chronomètre ne pourrait jamais atteindre 15 s.  ",
        "**B1.5** — `const float SH = 40.0;` et `const float SB = 37.0;` ($40 - 3$)."]),
    E('## B2', [
        "**B2.1** — Tendance $= \\dfrac{30{,}6 - 24{,}2}{40/60} = \\dfrac{6{,}4}{0{,}667} = 9{,}6\\,°\\mathrm{C/h}$.  ",
        "**B2.2** — $\\Delta T = 38 - 30{,}6 = 7{,}4\\,°\\mathrm{C}$ ; durée $= \\dfrac{7{,}4}{9{,}6/60} = \\dfrac{7{,}4}{0{,}16} \\approx 46\\,\\mathrm{min}$ ; heure estimée : 08 h 40 + 46 min ≈ **09 h 26**.  ",
        "**B2.3** — L'alarme prédictive **prévient avant** le dépassement : on a du temps pour agir. Une alarme sur seuil ne réagit qu'**après** le problème.  ",
        "**B2.4** — Exemple : « Sur la dernière heure, l'équipement est resté en alarme critique 15 % du temps (9 mesures sur 60) : une vérification de la ventilation est recommandée. »  ",
        "**B2.5** — Exemple cohérent : `\"t_raw\": 30.9, \"t_moy\": 30.6, \"trend\": 9.6, \"alarme\": \"OK\"`."]),
    E('## C1', [
        "**C1.1** — Erreurs certaines d'après l'énoncé :  ",
        "| # | Erreur | Correction |", "|---|---|---|",
        "| 1 | LED câblée à l'envers (anode vers GND) | Anode côté R2, cathode vers GND |",
        "| 2 | Un seul PWR_FLAG (sur GND) | Ajouter un PWR_FLAG sur +5V |",
        "| 3 et 4 | L'énoncé ne permet pas de les identifier avec certitude | À compléter avec l'enseignant (pistes habituelles : empreintes non associées, références non annotées) |",
        "",
        "**C1.2** — Après correction complète : **0 erreur** ERC.  ",
        "**C1.3** — $f_c = \\dfrac{1}{2\\pi \\times 10\\,000 \\times 100 \\times 10^{-9}} = \\dfrac{1}{2\\pi \\times 10^{-3}} \\approx 159\\,\\mathrm{Hz}$.  ",
        "**C1.4** — $I_f = \\dfrac{4{,}8 - 2}{330} \\approx 8{,}5\\,\\mathrm{mA}$."]),
    E('## C2', [
        "**C2.1** — R1 : `Resistor_SMD:R_0805_2012Metric` ; C1 : `Capacitor_SMD:C_0805_2012Metric` ; LED1 : `LED_THT:LED_D5.0mm` ; J1 : `Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm_Vertical`.  ",
        "**C2.2.1** — **3 nœuds** : `+5V`, `noeud_RC`, `GND` (l'extrait ne montre pas le net entre R2 et l'anode).  ",
        "**C2.2.2** — **Oui** : la cathode d'une LED va côté masse.  ",
        "**C2.2.3** — La pin 2 de R2 resterait **en l'air** (non connectée) et l'anode serait reliée **directement** à `noeud_RC` : la LED n'est plus protégée par la résistance, **courant non limité** et risque de destruction.  ",
        "**C2.3** — Un ratsnest non routé est une **liaison qui existe dans le schéma mais pas encore en piste** sur le PCB. Il faut **tracer la piste manquante** (ou changer de face avec un via), puis relancer le DRC."]),
    E('## D1', [
        "| Observation | Classe 2 | Justification |", "|---|---|---|",
        "| CMS décalé de 28 % | Conforme | Décalage inférieur ou égal à 50 % de la largeur |",
        "| Pont R1-R2 | **Non conforme** | Court-circuit |",
        "| Remplissage PTH 78 % | Conforme | Supérieur ou égal à 75 % |",
        "| Résidu de flux de colophane | Acceptable | Résidu non conducteur (nettoyage selon cahier des charges) |",
        "| Pointe de soudure de 1,2 mm | Non conforme par précaution | Peut réduire l'isolement ; critère exact à confirmer |",
        "| Condensateur C3 inversé | **Non conforme** | Polarité inversée : risque d'explosion |"]),
    E('## D2', [
        "IPC-A-610 → **A** ; IPC-2221 → **D** ; CEI 60068-2 → **B** ; CEI 61010-1 → **C** ; ISO 9001 → **E**.  ",
        "**D2.1** — **IPC-2221** (conception des PCB, classe B industrielle).  ",
        "**D2.2** — **CEI 60068-2** (essai de chaleur humide : 40 °C / 85 % HR, 96 h, série 60068-2-78)."]),
    E('## D3', [
        "**D3.1** —", "",
        "| Section | Titre | Impact de son absence |", "|---|---|---|",
        "| 2 | Description fonctionnelle | On ne comprend pas le rôle de la carte ni ses interfaces |",
        "| 7 | Contraintes de fonctionnement | L'utilisateur peut dépasser les limites (tension, température) et détruire la carte |",
        "| 8 | Résultats de validation | Aucune preuve que la carte respecte les exigences |",
        "",
        "**D3.2** — Exemple : Vin nominale **12 V**, min environ **7 V**, max **35 V** (7805) ; température opérationnelle **0 à 60 °C** ; IP carte nue : **IP00** ; NE555 $V_{CC}$ max **16 V** ; courant LED max **25 mA**."]),
    E('## E1', [
        "**E1.1** — **10 kΩ** (4,7 à 10 kΩ), câblée entre la ligne **DATA** et **VCC**.  ",
        "**E1.2** — C1 : **100 nF** ; C2 : **10 µF** (électrolytique).  ",
        "**E1.3** — Proposition (à valider selon le cours) : **dimensions** de la carte et des trous de fixation ; **position des connecteurs** et accès ; **ventilation** et échauffement du régulateur ; **tolérances d'impression** et jeu ; **matériau adapté à la température** de la serre (le PLA ramollit vers 60 °C)."]),
    E('## E2', [
        "**E2.1** — $\\bar{V} = 4{,}999\\,\\mathrm{V}$ ; $s \\approx 0{,}00265$ ; $u_A \\approx 0{,}00153$ ; $u_{B,rés} \\approx 0{,}00029$ ; $u_{B,cl} = \\dfrac{0{,}5 \\times 4{,}999}{100\\sqrt{3}} \\approx 0{,}01443$ ; $u_c \\approx 0{,}01451$ ; $U \\approx 0{,}0290$ → **0,029 V**. $V_{out} = (4{,}999 \\pm 0{,}029)\\,\\mathrm{V}$ [95 %].  ",
        "**E2.2** — $0{,}978 \\in [0{,}90\\,;\\,1{,}10]$ : **conforme** ; écart $= \\dfrac{0{,}978 - 1}{1} \\times 100 = -2{,}2\\,\\%$.  ",
        "**E2.3** — 72 % est **inférieur à 75 %** : **non conforme** en classe 2. Action : **retoucher** la brasure (refusion avec apport de soudure) puis contrôler à nouveau."]),
    E('## E3', [
        "**E3.1** —", "",
        "| TC# | Exigence | Résultat ± U | Conf. |", "|---|---|---|---|",
        "| TC-01 | $V_{out} = 5\\,\\mathrm{V} \\pm 5\\,\\%$ | $(4{,}999 \\pm 0{,}029)\\,\\mathrm{V}$ | Oui |",
        "| TC-02 | $f = 1\\,\\mathrm{Hz} \\pm 10\\,\\%$ | $0{,}978\\,\\mathrm{Hz}$ (écart −2,2 %) | Oui |",
        "| TC-03 | Assemblage IPC-A-610 Cl. 2 | Remplissage J1 = 72 % | **Non** |",
        "",
        "**E3.2** — **NON CONFORME** tant que J1 n'est pas retouché. Conclusion : « Les mesures électriques sont conformes, mais le remplissage de la brasure de J1 (72 %) est inférieur au minimum de 75 % ; retouche et nouveau contrôle exigés avant livraison. »  ",
        "**E3.3** — **DAT** (décrit la carte, ses calculs et ses contraintes), **PV de validation fonctionnelle** (preuves chiffrées de conformité), **fiche MES** (atteste l'installation et la remise au client)."]),
]
