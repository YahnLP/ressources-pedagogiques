"""Première S15 : réponses des 4 ateliers différenciés (calculs vérifiés)."""
F = '03-exercices.md'
E = lambda t, l: ('premiere', 'S15', F, t, l)
ENTREES = [
    E('### Exercice A1', [
        "1. Valeur vide → impossible de lire ou commander le composant, BOM incomplète. Correction : renseigner le champ Value (par exemple 330 Ω).  ",
        "2. Pas de PWR_FLAG → l'ERC signale « power pin not driven » : KiCad ne sait pas qu'une source alimente ce net. Correction : poser un PWR_FLAG sur +5V.  ",
        "3. LED inversée → elle ne s'allume jamais. Correction : anode côté +5V (via la résistance), cathode vers GND.  ",
        "4. Raison : la cathode (K) n'est reliée à rien. Correction : la relier à GND (ou poser un No Connect si la broche est volontairement libre)."]),
    E('### Exercice A2', [
        "**Oui**, il y a violation : $0{,}20 - 0{,}12 = 0{,}08\\,\\mathrm{mm}$ de moins que le minimum. Le DRC place un **marqueur d'erreur** sur le PCB à cet endroit ; il ne bloque pas la fabrication, mais la carte n'est pas conforme tant que l'erreur n'est pas corrigée (écarter les pistes)."]),
    E('### Exercice A3', [
        "**Q.A.3a** — F.Cu, B.Cu, F.Mask, B.Mask, F.Silkscreen, Edge.Cuts, plus le fichier de perçage (.drl).  ",
        "**Q.A.3b** — **Ouvrir les fichiers dans un visualiseur** (GerbView ou visualiseur en ligne) pour vérifier ce qui sera réellement fabriqué.  ",
        "**Q.A.3c** — Les zones noires indiquent les **ouvertures du masque de soudure** : le cuivre y reste apparent (pastilles à souder)."]),
    E('### Exercice B1', [
        "1. `Serial.begin(9600)` : sur ESP32, utiliser **115200** (messages de démarrage lisibles).  ",
        "2. `while (WiFi.status() == WL_CONNECTED)` : condition **inversée** ; il faut `!=`.  ",
        "3. `mqtt.connect(\"ESP32\")` : identifiant **non unique** et connexion **non testée** ; utiliser un ID unique et vérifier le retour de `connect`.  ",
        "4. `delay(5000)` + absence de `mqtt.loop()` : le client MQTT n'est jamais entretenu ; appeler `mqtt.loop()` à chaque tour de `loop()` et remplacer `delay` par `millis()`.  ",
        "*(Le repérage exact des 4 erreurs est une proposition à valider par l'enseignant.)*"]),
    E('### Exercice B2', [
        "**Q.B.2a** — Nœud 1 : `mqtt in` → reçoit le message ; nœud 2 : `json` → convertit la chaîne en objet ; nœud 3 : `function` → extrait `msg.payload.temperature` ; nœud 4 : `ui_gauge` → affiche la valeur.  ",
        "**Q.B.2b** — `msg.payload` est de type **chaîne (string)** ; ajouter un nœud **json** puis un nœud function : `msg.payload = msg.payload.temperature;`.  ",
        "**Q.B.2c** — `msg.topic = \"temperature\"`, `msg.topic = \"humidite\"`, `msg.topic = \"co2\"` : un topic **différent** par courbe."]),
    E('### Exercice C1', [
        "a) $TA = 2 + 0{,}5 + 0{,}75 + 3{,}25 + 1{,}5 = 8\\,\\mathrm{h}$.  ",
        "b) $TO = 2 \\times 8760 - 8 = 17\\,512\\,\\mathrm{h}$.  ",
        "c) $MTBF = \\dfrac{17\\,512}{5} = 3\\,502{,}4\\,\\mathrm{h} \\approx 146$ jours.  ",
        "d) $MTTR = \\dfrac{8}{5} = 1{,}6\\,\\mathrm{h}$.  ",
        "e) $D = \\dfrac{3\\,502{,}4}{3\\,502{,}4 + 1{,}6} \\approx 0{,}9995 = 99{,}95\\,\\%$.  ",
        "f) $99{,}95\\,\\% \\geq 99{,}9\\,\\%$ : **conforme**."]),
    E('### Exercice C2', [
        "a) $\\lambda = \\dfrac{1}{50\\,000} = 2 \\times 10^{-5}\\,\\mathrm{h^{-1}}$.  ",
        "b) $\\lambda t = 2 \\times 10^{-5} \\times 8760 = 0{,}1752$ ; $R(8760) = e^{-0{,}1752} \\approx 0{,}839 = 83{,}9\\,\\%$.  ",
        "c) $200 \\times 0{,}839 \\approx 168$ capteurs encore fonctionnels.  ",
        "d) $t \\leq \\dfrac{0{,}105}{2 \\times 10^{-5}} \\approx 5\\,270\\,\\mathrm{h} \\approx 7{,}2$ mois."]),
    E('### Exercice C3', [
        "a) $R_{capteurs} = 1 - (1 - 0{,}85)(1 - 0{,}80) = 1 - 0{,}15 \\times 0{,}20 = 0{,}97$.  ",
        "b) $R_s = 0{,}97 \\times 0{,}95 \\times 0{,}98 \\approx 0{,}903 = 90{,}3\\,\\%$.  ",
        "c) Dans la chaîne en série, le maillon le plus faible est le **CPU** ($R = 0{,}95$) ; le composant individuellement le moins fiable est le capteur B ($R = 0{,}80$), mais la mise en parallèle le compense.  ",
        "d) $R_{B,nouveau} = 1 - 0{,}2 \\times 0{,}2 = 0{,}96$ ; $R_{capteurs,nouveau} = 1 - 0{,}15 \\times 0{,}04 = 0{,}994$ ; $R_{s,nouveau} = 0{,}994 \\times 0{,}95 \\times 0{,}98 \\approx 0{,}925 = 92{,}5\\,\\%$ ; gain : environ **+2,2 points**."]),
    E('### Exercice D1', [
        "- **Situation 1** : couplage **capacitif** (pistes parallèles proches). Solution : éloigner les pistes ou intercaler une piste de garde à la masse.  ",
        "- **Situation 2** : couplage **résistif** (impédance commune de la masse). Solution : masses séparées reliées en un seul point, diode de roue libre sur le relais.  ",
        "- **Situation 3** : couplage **rayonné**. Solution : éloigner le téléphone, blinder le boîtier, filtrer."]),
    E('### Exercice D2', [
        "a) $\\lambda = \\dfrac{3 \\times 10^{8}}{2{,}4 \\times 10^{9}} = 0{,}125\\,\\mathrm{m} = 12{,}5\\,\\mathrm{cm}$ ; fente max $= \\dfrac{\\lambda}{20} = 0{,}625\\,\\mathrm{cm} = 6{,}25\\,\\mathrm{mm}$.  ",
        "b) $C = \\dfrac{1}{2\\pi \\times 50 \\times 33\\,000} \\approx 9{,}6 \\times 10^{-8}\\,\\mathrm{F} \\approx 96\\,\\mathrm{nF}$ ; valeur commerciale : **100 nF**.  ",
        "c) $\\lambda < 20 \\times 0{,}20 = 4\\,\\mathrm{m}$ ; $f > \\dfrac{3 \\times 10^{8}}{4} = 75\\,\\mathrm{MHz}$."]),
    E('### Exercice D3', [
        "1 **F** ; 2 **V** ; 3 **F** ; 4 **V** ; 5 **F** ; 6 **V** ; 7 **V** ; 8 **V**.  ",
        "Corrections : 1 — une fente **dégrade** le blindage (le courant de retour fait un détour : grande boucle) ; 3 — les émissions conduites se propagent **par les câbles**, pas par ondes ; 5 — la masse logique et la terre (PE) sont **deux conducteurs distincts** (reliés en un point si nécessaire)."]),
]
