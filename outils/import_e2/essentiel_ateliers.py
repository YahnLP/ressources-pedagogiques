"""Ateliers guidés et exercices d'application de chaque semaine du parcours « L'essentiel en 1 an ».
Fil rouge : on construit, mesure, valide et dépanne une même carte : le CLIGNOTEUR NE555."""

ATELIER = {}
EXOS = {}

ATELIER[1] = r"""
**Fil rouge** : pendant 10 semaines, tu vas concevoir, fabriquer, tester et dépanner **un clignoteur à LED** (NE555). Cette semaine : la partie LED.

**Matériel** : alimentation 5 V, plaque d'essai, résistance 150 Ω, LED rouge, multimètre.

1. **Calcule** la résistance pour une LED (2 V) à 20 mA sur 5 V.
2. **Trouve ses couleurs** : quelles bagues pour 150 Ω ?
3. **Mesure** la résistance au multimètre (hors tension) et vérifie qu'elle est dans sa tolérance.
4. **Monte** LED + résistance sur la plaque d'essai (patte longue de la LED côté résistance).
5. **Mesure** la tension aux bornes de la LED, puis de la résistance.
6. **Mesure** le courant (multimètre en série, calibre mA).
7. **Remplace** la résistance par 330 Ω et observe : que change-t-il ?

??? success "Résultats attendus"
    1. $R = \dfrac{5 - 2}{0{,}020} = 150\,\Omega$.
    2. **marron – vert – marron – or** (1, 5, × 10, ± 5 %).
    3. Entre 142,5 Ω et 157,5 Ω ($150 \pm 5\,\%$).
    4. La LED s'allume.
    5. Environ 2 V aux bornes de la LED, environ 3 V aux bornes de la résistance (la somme fait 5 V).
    6. Environ 20 mA ($\dfrac{3}{150}$).
    7. $I = \dfrac{5 - 2}{330} \approx 9\,\mathrm{mA}$ : la LED éclaire **moins fort**.
"""
EXOS[1] = [
 ("Une LED verte (2,1 V) doit être traversée par 10 mA sur une alimentation de 9 V. Quelle résistance, et quelle valeur de la série E12 ?", "$R = \\dfrac{9 - 2{,}1}{0{,}010} = 690\\,\\Omega$ → **680 Ω** (E12)."),
 ("On associe 100 Ω et 220 Ω : résistance équivalente en série ? en parallèle ?", "Série : $320\\,\\Omega$ ; parallèle : $\\dfrac{100 \\times 220}{320} \\approx 68{,}8\\,\\Omega$."),
 ("Pont diviseur : 12 V, $R_1 = 10\\,\\mathrm{k\\Omega}$, $R_2 = 4{,}7\\,\\mathrm{k\\Omega}$. Quelle tension de sortie ?", "$V_s = 12 \\times \\dfrac{4{,}7}{14{,}7} \\approx 3{,}84\\,\\mathrm{V}$."),
 ("Une résistance de 330 Ω reçoit 9 V. Quelle puissance dissipe-t-elle ? Une résistance de 0,25 W convient-elle ?", "$P = \\dfrac{9^2}{330} \\approx 0{,}245\\,\\mathrm{W}$ : **à la limite** des 0,25 W : on prend une résistance de 0,5 W."),
]

ATELIER[2] = r"""
**Fil rouge** : tu réutilises ton montage LED, et tu apprends à **l'alimenter et le mesurer proprement**.

1. **Alimentation de labo** : règle **5,0 V** et une **limite de courant de 30 mA**, sortie coupée. Mesure la tension à vide au multimètre.
2. **Branche** le montage LED. Lis le courant affiché par l'alimentation, puis **vérifie-le** avec le multimètre en série.
3. **Générateur** : règle un signal **carré, 1 kHz, 3 V crête à crête**. Branche-le à l'oscilloscope (sonde ×10 compensée).
4. **Relève** période, fréquence, $U_{pp}$.
5. Règle un **rapport cyclique de 25 %** et relève $t_{haut}$ sur l'écran.
6. Ajoute un **offset** de 1,5 V, puis passe l'oscilloscope en couplage **AC** : que se passe-t-il ?

??? success "Résultats attendus"
    1. Environ 5,00 V à vide.
    2. Environ 20 mA, mode **CV** (le voyant CC ne s'allume pas).
    3. et 4. $T = 1\,\mathrm{ms}$, $f = 1\,\mathrm{kHz}$, $U_{pp} = 3\,\mathrm{V}$.
    5. $t_{haut} = 0{,}25 \times 1\,\mathrm{ms} = 0{,}25\,\mathrm{ms}$.
    6. L'offset décale tout le signal vers le haut ; en **AC**, le signal **se recentre sur zéro** (la composante continue est supprimée).
"""
EXOS[2] = [
 ("Période de 8 carreaux à 0,5 ms/DIV : quelle fréquence ?", "$T = 4\\,\\mathrm{ms}$ ; $f = 250\\,\\mathrm{Hz}$."),
 ("Une sonde ×10 est utilisée, mais la voie est restée réglée sur ×1. L'écran indique 1,2 V crête à crête : quelle est la vraie valeur ?", "Le signal est atténué 10 fois : la vraie valeur est **12 V**."),
 ("Un signal est à l'état haut 3 ms sur une période de 12 ms. Rapport cyclique ?", "$\\dfrac{3}{12} = 25\\,\\%$."),
 ("Multimètre ±(0,5 % + 2 chiffres), lecture 12,00 V (résolution 0,01 V). Quelle marge ?", "$0{,}5\\,\\% \\times 12 = 0{,}06$ ; 2 chiffres = 0,02 ; marge = **0,08 V** → $(12{,}00 \\pm 0{,}08)\\,\\mathrm{V}$."),
]

ATELIER[3] = r"""
**Fil rouge** : tu choisis les composants du clignoteur **à partir des datasheets**.

1. Ouvre la datasheet du **NE555** et du **7805** (site du fabricant). Remplis : alimentation permise du NE555, tension d'entrée et de sortie du 7805, brochage des deux.
2. **Dimensionne l'oscillateur** pour environ **1 Hz** : prends $C = 10\,\mathrm{\mu F}$, $R_b = 68\,\mathrm{k\Omega}$, $R_a = 10\,\mathrm{k\Omega}$ ; calcule $f$ et le rapport cyclique.
3. **Vérifie le régulateur** : alimentation de 9 V et courant total de 35 mA ; calcule la puissance dissipée par le 7805.
4. **Remplis la fiche composants** : repère, valeur, boîtier.

??? success "Résultats attendus"
    1. NE555 : alimentation d'environ 4,5 V à 16 V. 7805 : entrée jusqu'à 35 V (au moins 7 V pour réguler), sortie 5 V. Brochage NE555 : 1 GND, 2 TRIG, 3 OUT, 4 RESET, 5 CTRL, 6 THR, 7 DIS, 8 VCC. Brochage 7805 : 1 entrée, 2 masse, 3 sortie.
    2. $f = \dfrac{1{,}44}{146\,000 \times 10 \times 10^{-6}} \approx 0{,}99\,\mathrm{Hz}$ ; $DC = \dfrac{78}{146} \approx 53\,\%$.
    3. $P = (9 - 5) \times 0{,}035 = 0{,}14\,\mathrm{W}$ : pas de radiateur.
    4. Par exemple : U1 NE555 (DIP-8), U2 7805 (TO-220), R1 10 kΩ, R2 68 kΩ, R3 150 Ω, C1 100 nF, C2 10 µF (sortie 7805), C3 10 µF (temporisation), C4 100 nF (broche 5), D1 LED 5 mm.
"""
EXOS[3] = [
 ("Un 7805 est alimenté en 7,5 V. Peut-il réguler à 5 V ? Et en 6 V ?", "À 7,5 V : **oui** (7,5 − 5 = 2,5 V ≥ 2 V). À 6 V : **non**, la chute minimale de 2 V n'est pas respectée."),
 ("BC547 de gain minimal 110, courant de collecteur de 30 mA, commande à 5 V. Calcule $R_b$ (règle $I_B = I_C/10$).", "$I_B = 3\\,\\mathrm{mA}$ ; $R_b = \\dfrac{4{,}3}{0{,}003} \\approx 1{,}4\\,\\mathrm{k\\Omega}$ → **1,2 kΩ** (E12 inférieure)."),
 ("NE555 : $R_a = 4{,}7\\,\\mathrm{k\\Omega}$, $R_b = 33\\,\\mathrm{k\\Omega}$, $C = 10\\,\\mathrm{\\mu F}$. Fréquence ?", "$f = \\dfrac{1{,}44}{(4{,}7 + 66) \\times 10^{3} \\times 10^{-5}} \\approx 2{,}04\\,\\mathrm{Hz}$."),
 ("Pourquoi calcule-t-on avec les limites de la datasheet plutôt qu'avec les valeurs typiques ?", "Pour que le montage fonctionne dans le **cas le plus défavorable** (composant le moins favorable, température extrême)."),
]

ATELIER[4] = r"""
**Fil rouge** : tu dimensionnes l'**alimentation du clignoteur** (12 V → 5 V).

1. **Bilan** : NE555 ≈ 10 mA, LED = 20 mA. Total ?
2. **Régulateur** : puissance dissipée par le 7805 sous 12 V, puis température de jonction ($R_{\theta ja} = 65\,°\mathrm{C/W}$, 25 °C ambiants).
3. Même calcul sous **9 V** (pile) : que gagne-t-on ?
4. **Autonomie** sur une pile 9 V de 500 mAh.
5. Faut-il un **radiateur** ? Justifie.

??? success "Résultats attendus"
    1. $I_{total} = 30\,\mathrm{mA}$ ; avec 25 % de marge : 37,5 mA minimum côté source.
    2. $P = (12 - 5) \times 0{,}03 = 0{,}21\,\mathrm{W}$ ; $T_j = 25 + 0{,}21 \times 65 \approx 38{,}7\,°\mathrm{C}$.
    3. $P = 4 \times 0{,}03 = 0{,}12\,\mathrm{W}$ : moins de chaleur, meilleur rendement.
    4. $t = \dfrac{500}{30} \times 0{,}8 \approx 13\,\mathrm{h}$.
    5. **Non** : 38,7 °C est très inférieur aux 105 °C exploitables.
"""
EXOS[4] = [
 ("Un 7805 alimenté en 24 V débite 100 mA. Que se passe-t-il ?", "$P = 19 \\times 0{,}1 = 1{,}9\\,\\mathrm{W}$ ; $T_j = 25 + 1{,}9 \\times 65 \\approx 148{,}5\\,°\\mathrm{C}$ : **supérieur à 125 °C**, le composant est détruit. Il faut un convertisseur à découpage ou un radiateur."),
 ("Un convertisseur à découpage de rendement 90 % délivre 5 V sous 100 mA. Quelle puissance prélève-t-il ? Quelles pertes ?", "$P_{in} = \\dfrac{5 \\times 0{,}1}{0{,}9} \\approx 0{,}556\\,\\mathrm{W}$ ; pertes ≈ **0,056 W**."),
 ("Pic de consommation de 220 mA : quelle source minimale ?", "$220 \\times 1{,}25 = 275\\,\\mathrm{mA}$."),
 ("Courant moyen d'un système qui consomme 150 mA pendant 5 s puis 0,1 mA pendant 55 s ?", "$\\dfrac{750 + 5{,}5}{60} \\approx 12{,}6\\,\\mathrm{mA}$."),
]

ATELIER[5] = r"""
**Fil rouge** : tu dessines le **schéma KiCad** du clignoteur.

1. Crée le projet `clignoteur`.
2. Place : connecteur 2 broches (J1, +12 V / GND), **7805** avec ses condensateurs (100 nF entrée, 10 µF sortie), **NE555**, $R_a$, $R_b$, $C_3$ (10 µF), **100 nF** sur la broche 5, $R_3$ (150 Ω) et la LED.
3. Câble : broche 4 et 8 au +5 V, broche 1 à la masse, 2 et 6 reliées entre elles et à $C_3$, 7 entre $R_a$ et $R_b$, sortie 3 vers $R_3$ puis LED vers la masse.
4. Ajoute 2 **PWR_FLAG** (+5 V et GND). **Annote**, renseigne les **valeurs**.
5. Lance l'**ERC** et corrige jusqu'à **0 erreur**.
6. Associe les **empreintes**.

??? success "Résultats attendus"
    - ERC : **0 erreur**.
    - Empreintes : R → `Resistor_THT:R_Axial_DIN0207_L6.3mm_D2.5mm_P10.16mm_Horizontal` ; LED → `LED_THT:LED_D5.0mm` ; NE555 → `Package_DIP:DIP-8_W7.62mm` ; 7805 → `Package_TO_SOT_THT:TO-220-3_Vertical` ; condensateur chimique → `Capacitor_THT:CP_Radial_D5.0mm_P2.50mm` ; connecteur → `Connector_PinHeader_2.54mm:PinHeader_1x02_P2.54mm_Vertical`.
"""
EXOS[5] = [
 ("L'ERC affiche `power_pin_not_driven` sur +5 V. Que faire ?", "Poser un **PWR_FLAG** sur le net +5 V."),
 ("Deux composants portent le repère R1. Quelle erreur et quelle action ?", "`duplicate_reference` : **annoter à nouveau** le schéma."),
 ("La broche 5 du NE555 n'est pas utilisée en astable : doit-elle rester non connectée ?", "On la relie à la masse **par un condensateur de 100 nF** (stabilité) ; si on la laisse en l'air, l'ERC la signale (`pin_not_connected`) et le montage est plus sensible au bruit."),
 ("Quelle est la différence entre un composant THT et CMS ?", "Le THT a des **pattes qui traversent** la carte ; le CMS est **posé en surface** sur les pistes."),
]

ATELIER[6] = r"""
**Fil rouge** : tu transformes le schéma en **carte fabricable**, puis tu la **soudes**.

1. Importe le schéma dans le PCB. Trace le **contour 60 × 40 mm**.
2. **Règles** : clearance 0,25 mm ; pistes 0,25 mm ; alimentation 0,5 mm ; via 0,8 / 0,4 mm.
3. **Place** : J1 au bord, 7805 et ses condensateurs, NE555, passifs près du NE555, LED près du bord.
4. **Route** l'alimentation, puis les signaux. Lance le **DRC** : 0 erreur.
5. **Exporte** Gerber (cuivre, masque, sérigraphie, contour), perçage, BOM. **Ouvre-les** dans un visualiseur.
6. **Soude** dans l'ordre : résistances, support DIP-8, condensateurs, régulateur, connecteur, LED. **Contrôle** les brasures.

??? success "Résultats attendus"
    - DRC : **0 erreur** ; pistes d'alimentation visiblement plus larges.
    - Fichiers : F.Cu (ou B.Cu), masque, sérigraphie, Edge.Cuts, `.drl`, `.csv` de la BOM.
    - Brasures : brillantes, en cône, trou rempli à **75 % au moins** ; aucun pont ni soudure froide.
"""
EXOS[6] = [
 ("Deux pistes sont à 0,18 mm l'une de l'autre, règle 0,25 mm. Violation de combien ?", "$0{,}25 - 0{,}18 = 0{,}07\\,\\mathrm{mm}$ : le DRC signale une erreur."),
 ("Une pastille de 1,8 mm est percée à 1,0 mm. Largeur de l'anneau de cuivre ?", "$\\dfrac{1{,}8 - 1{,}0}{2} = 0{,}4\\,\\mathrm{mm}$."),
 ("Où place-t-on le condensateur de découplage du NE555 ?", "**Au plus près** des broches 8 (VCC) et 1 (GND)."),
 ("Remplissage d'un trou traversant de 70 % : conforme en classe 2 ?", "**Non** : il faut au moins 75 %."),
]

ATELIER[7] = r"""
**Fil rouge** : tu **améliores** le clignoteur en lui faisant commander une charge plus puissante (un relais 5 V, 70 mA).

1. **Choisis** le transistor (BC547 ou BC337) et justifie.
2. **Calcule** $R_b$ (commande par la sortie du NE555 à environ 5 V, règle $I_C/10$).
3. **Dessine** le schéma : bobine du relais, diode de roue libre, transistor.
4. **Filtre** : place un filtre RC (10 kΩ, 100 nF) sur une tension bruitée et calcule sa fréquence de coupure.
5. **Logique** : écris la table de vérité d'une alarme « température haute ET porte ouverte ».

??? success "Résultats attendus"
    1. **BC337** (800 mA maximum) : le BC547 serait trop juste à 70 mA.
    2. $I_B = 7\,\mathrm{mA}$ ; $R_b = \dfrac{4{,}3}{0{,}007} \approx 614\,\Omega$ → **560 Ω**.
    3. Diode 1N4007 en parallèle inverse de la bobine.
    4. $f_c = \dfrac{1}{2\pi \times 10^{4} \times 10^{-7}} \approx 159\,\mathrm{Hz}$.
    5. Porte **ET** : la sortie vaut 1 seulement si les deux entrées valent 1.
"""
EXOS[7] = [
 ("$R_f = 22\\,\\mathrm{k\\Omega}$, $R_g = 2{,}2\\,\\mathrm{k\\Omega}$ sur un AOP non inverseur : gain ?", "$G = 1 + 10 = 11$."),
 ("Filtre RC : $R = 4{,}7\\,\\mathrm{k\\Omega}$, $C = 10\\,\\mathrm{nF}$. Fréquence de coupure ?", "$f_c = \\dfrac{1}{2\\pi \\times 4700 \\times 10^{-8}} \\approx 3{,}4\\,\\mathrm{kHz}$."),
 ("MOSFET de $R_{DS(on)} = 22\\,\\mathrm{m\\Omega}$ et courant de 3 A : puissance dissipée ?", "$P = 0{,}022 \\times 9 \\approx 0{,}2\\,\\mathrm{W}$ : pas de radiateur."),
 ("Sortie d'une porte NON-ET avec A = 1 et B = 1 ?", "**0**."),
]

ATELIER[8] = r"""
**Fil rouge** : tu **valides** ta carte clignoteur avec un **procès-verbal**.

1. Alimente en 12 V (limite de courant 100 mA).
2. **TC-01** : tension de sortie du 7805 (attendu 5 V ± 5 %).
3. **TC-02** : fréquence du clignotement (attendu 1 Hz ± 10 %).
4. **TC-03** : courant dans la LED (attendu ≤ 30 mA, cible 20 mA).
5. **TC-04** : rapport cyclique (attendu environ 50 %).
6. Rédige le **PV** : tableau attendu / mesuré / marge / verdict, et conclusion.

??? success "Exemple de PV (valeurs types)"
    | Test | Attendu | Mesuré ± marge | Verdict |
    |---|---|---|---|
    | TC-01 $V_{out}$ | 4,75 à 5,25 V | $(4{,}99 \pm 0{,}03)\,\mathrm{V}$ | Conforme |
    | TC-02 $f$ | 0,90 à 1,10 Hz | $(0{,}99 \pm 0{,}02)\,\mathrm{Hz}$ | Conforme |
    | TC-03 $I_F$ | ≤ 30 mA | $(19{,}3 \pm 0{,}3)\,\mathrm{mA}$ | Conforme |
    | TC-04 $DC$ | ≈ 50 % | 53 % | Observation : cohérent avec la formule |

    **Conclusion** : la carte est **conforme** au cahier des charges ; instruments utilisés et leur étalonnage indiqués ; PV daté et signé.
"""
EXOS[8] = [
 ("Mesure $(5{,}20 \\pm 0{,}08)\\,\\mathrm{V}$ pour 5 V ± 5 % : verdict ?", "Plage 5,12 à 5,28 V, qui **dépasse** 5,25 V : **non garanti**, à justifier ou refaire avec un meilleur instrument."),
 ("Mesure $(0{,}93 \\pm 0{,}02)\\,\\mathrm{Hz}$ pour 1 Hz ± 10 % : verdict ?", "Plage 0,91 à 0,95 Hz, dans [0,90 ; 1,10] : **conforme**."),
 ("Citez 3 éléments obligatoires d'un PV.", "Par exemple : **identification** (carte, date, opérateur), **instruments** avec étalonnage, **résultats** avec verdict, **conclusion**, **signature**."),
 ("Pourquoi un instrument hors étalonnage invalide-t-il un PV ?", "Sa mesure n'est plus **garantie** : elle n'est plus **traçable** jusqu'à une référence."),
]

ATELIER[9] = r"""
**Fil rouge** : ton enseignant (ou un camarade) a **introduit des pannes** sur la carte clignoteur. Tu les trouves **par la méthode**.

**Tensions attendues (carte en bon état, alimentée en 12 V)** : sortie du 7805 = 5 V ; broche 8 = 5 V ; broche 4 = 5 V ; broche 5 ≈ 3,3 V ; broches 2/6 qui oscillent entre environ 1,7 V et 3,3 V ; broche 3 qui bascule.

Pour chaque panne : **décris**, **mesure** (tableau attendu / mesuré), **conclus**, **répare**, **reteste**.

| Panne | Symptôme |
|---|---|
| A | rien ne s'allume ; sortie du 7805 à 0 V |
| B | LED **toujours éteinte** ; broches 2/6 bloquées à environ 3,3 V |
| C | LED **toujours allumée** ; broches 2/6 à 0 V |

??? success "Diagnostic"
    - **A** : vérifier l'entrée (12 V présent ?) : si oui, **7805 défectueux** ou masse coupée ; si non, câble ou connecteur.
    - **B** : le condensateur **ne peut plus se décharger** : **$R_b$ coupée** (ou mal soudée) : mesurer $R_b$ hors tension.
    - **C** : le condensateur **ne peut plus se charger** : **$R_a$ coupée**. À la mesure de $R_a$, la valeur est infinie.
"""
EXOS[9] = [
 ("La sortie du 7805 est à 0 V, l'entrée à 12 V. Hypothèses ?", "Régulateur défectueux, ou court-circuit en aval qui l'écrase (limite thermique), ou masse du régulateur coupée."),
 ("Pourquoi mesure-t-on une résistance retirée du circuit ?", "Pour ne pas mesurer les autres composants en parallèle."),
 ("Une panne disparaît en touchant la carte. Quelle famille de défauts ?", "Un défaut **intermittent** : soudure froide ou mauvais contact."),
 ("Citez 3 rubriques d'une fiche d'intervention.", "**Symptôme**, **cause**, **action corrective** (et test après réparation)."),
]

ATELIER[10] = r"""
**Épreuve blanche (3 h)** sur une carte **neuve** du même type que le fil rouge (autre valeur de composants).

| Phase | Durée | Travail |
|---|---|---|
| 1 | 30 min | Calculs préalables : fréquence, rapport cyclique, courant LED, plages de tolérance |
| 2 | 1 h 15 | Mesures de la carte (tensions, fréquence, courant) avec les bons instruments |
| 3 | 45 min | Dépannage d'une panne injectée (tableau de tensions) |
| 4 | 30 min | PV : tableau, verdicts, conclusion, signature |

**Barème (20 points)** : calculs (5) · mesures et réglages des instruments (5) · dépannage (5) · PV (5).

??? success "Critères de réussite"
    - Unités présentes partout ; tolérances **chiffrées** ; verdicts **justifiés**.
    - Instruments correctement réglés (calibre, sonde ×10, déclenchement).
    - Panne trouvée **par mesure** (pas par hasard) et réparée par **un seul** changement.
    - PV **daté, signé**, propre.
"""
EXOS[10] = [
 ("Quel est l'ordre logique d'une épreuve de mesure ?", "**Préparer** (calculs attendus) → **mesurer** → **comparer** → **conclure** et rédiger."),
 ("Une mesure te paraît aberrante. Que fais-tu ?", "Je vérifie le **branchement**, le **calibre**, la **sonde**, puis je **refais** la mesure."),
 ("Quelles sont les trois compétences évaluées ?", "**C03** participer à un projet ; **C07** réaliser maquettes et prototypes ; **C11** maintenir un système électronique."),
 ("Que mets-tu dans ton dossier de compétences ?", "Les **preuves** : schéma, fichiers de fabrication, PV, fiches d'intervention."),
]
