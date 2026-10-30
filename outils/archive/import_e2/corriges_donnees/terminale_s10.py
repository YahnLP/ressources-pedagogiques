"""Terminale S10 : réponses des 6 ateliers de remédiation (calculs vérifiés)."""
F = '03-exercices.md'
E = lambda t, l: ('terminale', 'S10', F, t, l)
ENTREES = [
    E('### Exercice A1', [
        "a) $I_{moy,ESP32} = \\dfrac{200 \\times 30 + 0{,}02 \\times 570}{600} = \\dfrac{6\\,011{,}4}{600} \\approx 10{,}02\\,\\mathrm{mA}$.  ",
        "b) $I_{GPS,moy} = 50 \\times \\dfrac{30}{600} = 2{,}5\\,\\mathrm{mA}$ ; $I_{LED,moy} = 5 \\times 0{,}5 = 2{,}5\\,\\mathrm{mA}$ ; $I_{moy}$ total $= 10{,}02 + 2{,}5 + 2{,}5 \\approx 15{,}0\\,\\mathrm{mA}$.  ",
        "c) $P_{diss} = (3{,}7 - 3{,}3) \\times 0{,}0150 \\approx 0{,}006\\,\\mathrm{W}$ ; $T_j = 30 + 0{,}006 \\times 44 \\approx 30{,}3\\,°\\mathrm{C}$ → **OK**, pas de radiateur (très loin de 105 °C).  ",
        "d) Le LDO transmet le même courant à la batterie : $t = \\dfrac{2000}{15{,}0} \\times 0{,}80 \\approx 107\\,\\mathrm{h} \\approx 4{,}4$ jours."]),
    E('### Exercice A2', [
        "- **Application 1** : convertisseur **à découpage** (buck) ; $\\eta \\approx 85$ à $90\\,\\%$ ; en linéaire : $P_{diss} = (12 - 5) \\times 3 = 21\\,\\mathrm{W}$ → problème : **échauffement énorme**, radiateur impossible à dimensionner raisonnablement.  ",
        "- **Application 2** : **LDO** (faible chute) ; $V_{drop} = 3{,}7 - 3{,}3 = 0{,}4\\,\\mathrm{V}$ ; $P_{diss} = 0{,}4 \\times 0{,}030 = 0{,}012\\,\\mathrm{W}$ ; $T_j = T_{amb} + 0{,}012 \\times R_{\\theta ja} \\approx T_{amb} + 0{,}6\\,°\\mathrm{C}$ (avec $R_{\\theta ja} \\approx 50\\,°\\mathrm{C/W}$).  ",
        "- **Application 3** : régulateur **linéaire à faible bruit** : un découpage injecterait du **bruit HF** (commutation) qui polluerait le signal audio (lien **CEM**)."]),
    E('### Mini-quiz A', [
        "1. $P_{diss} = (V_{in} - V_{out}) \\times I_{out}$.  ",
        "2. 110 °C dépasse 105 °C : ajouter un **radiateur**, réduire la puissance dissipée ou passer à un **découpage**.  ",
        "3. Un **meilleur rendement** donc une **autonomie plus longue**.  ",
        "4. $t = \\dfrac{\\text{capacité}}{I_{moy}} \\times 0{,}80$.  ",
        "5. Le **LDO** fonctionne avec une très faible chute de tension (≈ 0,3 V) ; le LM78xx demande ≈ 2 V de marge."]),
    E('### Exercice B1', [
        "a) $\\bar{x}_1 = 3{,}995\\,\\mathrm{bar}$ ; $\\sigma_1 \\approx 0{,}0187\\,\\mathrm{bar}$ ; $\\bar{x}_2 = 4{,}055\\,\\mathrm{bar}$ ; $\\sigma_2 \\approx 0{,}0187\\,\\mathrm{bar}$.  ",
        "b) Biais$_1 = 3{,}995 - 4{,}00 = -0{,}005\\,\\mathrm{bar}$ ; Biais$_2 = 4{,}055 - 4{,}00 = +0{,}055\\,\\mathrm{bar}$.  ",
        "c) $\\sigma_{EV} = \\dfrac{0{,}0187 + 0{,}0187}{2} = 0{,}0187$ ; $\\sigma_{AV} \\approx \\dfrac{|3{,}995 - 4{,}055|}{\\sqrt{6}} \\approx 0{,}0245$ ; $\\sigma_{GRR} = \\sqrt{0{,}0187^2 + 0{,}0245^2} \\approx 0{,}0308$ ; $\\%GRR = \\dfrac{5{,}15 \\times 0{,}0308}{0{,}6} \\times 100 \\approx 26{,}5\\,\\%$.  ",
        "d) **Acceptable** (10 à 30 %), sous conditions. Recommandation : **corriger le biais** du capteur 2 (+0,055 bar, soit près de 10 % de la tolérance) par un réglage ou un étalonnage, puis recommencer l'étude.  ",
        "e) $LD \\approx 3 \\times 0{,}0187 \\approx 0{,}056\\,\\mathrm{bar}$ : une variation de 0,02 bar est **inférieure** à la limite de détection → **Non**, le capteur 1 ne la détecte pas.  ",
        "*(Remarque : l'énoncé parle de deux opérateurs, mais le tableau compare deux capteurs ; le calcul ci-dessus suit le tableau.)*"]),
    E('### Mini-quiz B', [
        "1. **un seul opérateur** (même opérateur, même instrument).  ",
        "2. Améliorer le système de mesure (étalonnage, instrument plus précis, formation des opérateurs) avant de l'utiliser.  ",
        "3. $LD \\approx 3 \\times \\sigma_{bruit}$.  ",
        "4. **Non** : une variation de 0,2 bar est inférieure à $LD = 0{,}5\\,\\mathrm{bar}$.  ",
        "5. $NDC \\geq 5$ : l'instrument distingue correctement les pièces."]),
    E('### Exercice C1', [
        "| N° | Violation | Problème CEM / qualité | Correction |", "|---|---|---|---|",
        "| 1 | Condensateur de découplage à 12 mm du CI | Grande boucle de courant, découplage inefficace en HF | Le placer à moins de 2 mm des broches VCC/GND |",
        "| 2 | Plan de masse fendu par une piste 5 V | Le courant de retour fait un détour : grande boucle, fort rayonnement | Router la piste ailleurs ou sur l'autre face, garder le plan continu |",
        "| 3 | Piste de signal de 18 cm | Se comporte en antenne (émet et capte) | Raccourcir la piste, rapprocher les composants |",
        "| 4 | Clearance 0,15 mm au lieu de 0,20 mm | Risque de court-circuit et d'erreur DRC | Écarter les pistes à 0,20 mm ou plus |",
        "| 5 | Sérigraphie « R1 » sur un pad | Gêne la soudure | Déplacer le texte hors des pastilles |",
        "",
        "Sixième défaut (bonus) : la valeur de la résistance de pull-up est vide → BOM incomplète, à renseigner (10 kΩ)."]),
    E('### Exercice C2', [
        "a) $f > \\dfrac{3 \\times 10^{8}}{3{,}6} \\approx 83\\,\\mathrm{MHz}$.  ",
        "b) $\\dfrac{\\lambda}{20} = \\dfrac{0{,}125}{20} = 6{,}25\\,\\mathrm{mm}$ ; toute piste de plus de **6,25 mm** peut rayonner à 2,4 GHz.  ",
        "c) Taille maximale d'une fente : $\\dfrac{\\lambda}{20} = 6{,}25\\,\\mathrm{mm}$."]),
    E('### Mini-quiz C', [
        "1. ERC = vérification **électrique** (du schéma) ; DRC = vérification des **règles de conception** (géométrie du PCB).  ",
        "2. Les zones noires du masque indiquent les **ouvertures du vernis** : le cuivre reste apparent (pastilles à souder).  ",
        "3. Via standard : Ø extérieur **0,8 mm**, perçage **0,4 mm**.  ",
        "4. Moins de **2 mm**.  ",
        "5. B = **remplir les zones** (refill) ; Alt+3 = **vue 3D**."]),
    E('### Exercice D1', [
        "1. `Serial.begin(9600)` : sur ESP32, on utilise **115200** (messages de démarrage), et il manque `pinMode(2, OUTPUT)`.  ",
        "2. `while (WiFi.status() == WL_CONNECTED)` : condition **inversée** ; il faut `!=`.  ",
        "3. `mqtt.connect(\"ESP32\")` : identifiant **non unique** (deux cartes se déconnectent) et connexion **non testée / pas de reconnexion**.  ",
        "4. `setCallback` doit être appelé **avant** `connect` et `subscribe` ; de plus, dans le callback le `payload` n'est pas terminé par `\\0` (copier `l` octets).  ",
        "5. `delay(5000)` **bloque** `mqtt.loop()` (qui n'est d'ailleurs pas appelé) : utiliser `millis()` et appeler `mqtt.loop()` à chaque tour.  ",
        "*(Le repérage exact des 5 erreurs dépend de la lecture du code : à valider par l'enseignant.)*"]),
    E('### Exercice D2', [
        "Nœuds, dans l'ordre : `mqtt-in` (salle/+/data) → `json` → `function` (Parser, 2 sorties).  ",
        "Sortie 1 → `ui_gauge` (0–50 °C), `ui_chart` (30 points) et `switch` (temp > 35) → `ui_notification` + `mqtt-out`.  ",
        "Sortie 2 → `influxdb-out`.  ",
        "Code du Parser : `msgVisu = { payload: data.temp, topic: \"Température\" }` ; `msgDB = { payload: [{ measurement: \"salle_data\", tags: { site: msg.topic.split(\"/\")[1] }, fields: { temp: data.temp, hum: data.hum } }] }`."]),
    E('### Mini-quiz D', [
        "1. **192.168.4.1**.  ",
        "2. **Obligatoire**.  ",
        "3. Le **nom (série)** de la courbe.  ",
        "4. `measurement`.  ",
        "5. Il **bloque `mqtt.loop()`** : la connexion au broker n'est plus entretenue et se coupe."]),
    E('### Exercice E1', [
        "a) $R_{capt} = 1 - 0{,}12 \\times 0{,}18 = 0{,}9784 = 97{,}84\\,\\%$.  ",
        "b) $R_s = 0{,}9784 \\times 0{,}97 \\times 0{,}99 \\approx 0{,}9396 = 93{,}96\\,\\%$.  ",
        "c) $\\lambda_A = \\dfrac{1}{60\\,000} \\approx 1{,}67 \\times 10^{-5}\\,\\mathrm{h^{-1}}$ ; $\\lambda_A t \\approx 0{,}146$ ; $R_A(8\\,760) = e^{-0{,}146} \\approx 0{,}864 = 86{,}4\\,\\%$.  ",
        "d) $0{,}864 \\times 200 \\approx 173$ capteurs.  ",
        "e) $D = \\dfrac{10\\,000}{10\\,004} \\approx 0{,}9996 = 99{,}96\\,\\%$."]),
    E('### Mini-quiz E', [
        "1. **36,8 %** (pas 50 %).  ",
        "2. $R_s < R_{min}$ (la fiabilité d'une série est inférieure à celle du composant le plus faible).  ",
        "3. $1 - 0{,}1^2 = 0{,}99 = 99\\,\\%$.  ",
        "4. $\\lambda = \\dfrac{1}{MTBF}$.  ",
        "5. $D = \\dfrac{MTBF}{MTBF + MTTR}$."]),
    E('### Exercice F1', [
        "- **Scénario 1** : couplage **résistif** (impédance commune de la masse). Le courant du relais traverse la masse commune et fait varier le potentiel de référence de l'ESP32. Solutions : **masses séparées** (reliées en un seul point), alimentation séparée, **diode de roue libre** sur la bobine, découplage, optocoupleur.  ",
        "- **Scénario 2** : couplage **capacitif** (diaphonie entre pistes parallèles). Solutions : **éloigner** les pistes, ne pas les faire courir en parallèle, intercaler une **piste de garde reliée à la masse**, plan de masse continu.  ",
        "- **Scénario 3** : couplage **inductif** (le courant de 2 A crée un champ magnétique). Solutions : **éloigner** les câbles, les faire se croiser à **angle droit**, **torsader** la paire, utiliser un câble **blindé** pour l'UART."]),
    E('### Exercice F2', [
        "a) $\\lambda = \\dfrac{3 \\times 10^{8}}{2{,}4 \\times 10^{9}} = 0{,}125\\,\\mathrm{m}$ ; $\\dfrac{\\lambda}{20} = 6{,}25\\,\\mathrm{mm}$.  ",
        "b) $C = \\dfrac{1}{2\\pi \\times 100 \\times 22\\,000} \\approx 7{,}2 \\times 10^{-8}\\,\\mathrm{F} \\approx 72\\,\\mathrm{nF}$ (valeur normalisée proche : **68 nF** ou **82 nF**).  ",
        "c) $\\lambda < 20 \\times 0{,}22 = 4{,}4\\,\\mathrm{m}$ ; $f > \\dfrac{3 \\times 10^{8}}{4{,}4} \\approx 68\\,\\mathrm{MHz}$.  ",
        "d) 1. **Vrai** ; 2. **Faux** (une ferrite **absorbe** les signaux HF) ; 3. **Faux** (à moins de 2 mm) ; 4. **Faux** (les perturbations conduites se propagent par **les câbles**, pas par l'air) ; 5. **Vrai** ; 6. **Vrai** (pour les hautes fréquences, à valider selon le cours) ; 7. **Vrai** ; 8. **Vrai**."]),
    E('### Mini-quiz F', [
        "1. **Résistif** (impédance commune), **capacitif**, **inductif**, **rayonné**.  ",
        "2. Conduites **< 30 MHz** ; rayonnées **> 30 MHz**.  ",
        "3. Fente **< 6,25 mm**.  ",
        "4. Plan fendu → courant de retour **dévié** → grande **boucle** → fort **rayonnement**.  ",
        "5. $f_c = \\dfrac{1}{2\\pi \\times R \\times C}$."]),
]
