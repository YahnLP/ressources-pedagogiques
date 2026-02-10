---
title: "E2 - Pack 07 - Fiche de cours élève - Microcontrôleurs & programmation basique (Arduino)"
module: "BAC PRO CIEL - E2"
version: "1.0"
---

# Systèmes microcontrôleurs et programmation basique

## I. Introduction aux systèmes microcontrôleurs : caractéristiques et structure

Les microcontrôleurs sont des circuits intégrés programmables qui contrôlent des systèmes électroniques en exécutant des instructions. Ils combinent un processeur, de la mémoire et des périphériques d’entrée/sortie (E/S) dans un seul composant, ce qui en fait le cœur de nombreux appareils électroniques.

✅ Complément utile :
- Un microcontrôleur = “petit ordinateur” dédié à une tâche.
- Il exécute **un programme** et pilote des broches (pins) reliées à des capteurs/actionneurs. :contentReference[oaicite:5]{index=5}

<p align="center">
  <img src="./images/microcontroleur_blocs.png" alt="Blocs d’un microcontrôleur" width="90%"><br>
  <em>Illustration attendue : schéma en blocs CPU + mémoire + E/S + bus, reliés entre eux.</em>
</p>

● Architecture du microcontrôleur :
○ Processeur (CPU) : il exécute les instructions du programme, effectuant les calculs et prenant des décisions.

✅ Complément utile :
- Le CPU fait : calculs, comparaisons, décisions (if/else) et contrôle des broches.

○ Mémoire :
■ Mémoire Flash : stocke le programme (instructions et données). Elle conserve les données même sans alimentation.

✅ Complément utile :
- Flash = “mémoire du programme” : ce que tu téléverses dans l’Arduino reste après arrêt.

■ RAM : mémoire temporaire pour les données en cours d’utilisation. Elle est volatile et effacée lorsque l’alimentation est coupée.

✅ Complément utile :
- RAM = variables en cours (valeurs lues, calculs). Elle se vide à l’arrêt.

■ EEPROM (optionnelle) : mémoire non volatile pour stocker des données modifiables au fil du temps, même sans alimentation.

✅ Complément utile :
- EEPROM = utile pour mémoriser un réglage (ex : seuil) même si on coupe l’alim.

○ Périphériques d’E/S : permettent de communiquer avec les composants externes (capteurs, LED, moteurs) via des broches d’entrée et de sortie.

✅ Complément utile :
- Une broche = un point de connexion : elle peut être **entrée** ou **sortie** selon configuration.

○ Bus interne : il connecte les différentes parties du microcontrôleur (CPU, mémoire, périphériques) pour assurer le transfert des données.

✅ Complément utile :
- Le bus = “route interne” qui transporte les informations entre blocs.

● Exemples de microcontrôleurs courants :
○ Microcontrôleurs AVR (Atmel) : utilisés dans les cartes Arduino, ils sont souvent programmés en C ou en Arduino IDE.

✅ Complément utile :
- Arduino UNO utilise un AVR classique (selon modèle). On programme via Arduino IDE.

○ Microcontrôleurs PIC (Microchip) : utilisés dans des applications industrielles, avec une architecture robuste.

✅ Complément utile :
- Très présents dans l’industrie (automatismes, cartes dédiées).

○ ESP8266 et ESP32 : microcontrôleurs avec connectivité Wi-Fi, utilisés dans les projets de l’Internet des Objets (IoT).

✅ Complément utile :
- ESP32 = intéressant pour projets connectés (Wi-Fi/Bluetooth) mais plus “riche”.

---

## II. Applications des microcontrôleurs dans les systèmes électroniques

Les microcontrôleurs sont présents dans de nombreux domaines où ils contrôlent des systèmes variés et répondent à des besoins spécifiques.

● Automobile : les microcontrôleurs contrôlent des systèmes tels que l’ABS, les airbags, et les systèmes de gestion du moteur.

✅ Complément utile :
- Ils lisent des capteurs (vitesse, pression) et commandent des actionneurs (pompe ABS…).

● Électroménager : dans les lave-linges, fours, et réfrigérateurs, ils régulent les cycles de fonctionnement.

✅ Complément utile :
- Exemple : mesurer température et ajuster résistance chauffante.

● Robotique : utilisés pour contrôler les moteurs, interpréter les capteurs, et exécuter des algorithmes de déplacement.

✅ Complément utile :
- Capteurs (distance) → décision → moteurs.

● Internet des Objets (IoT) : les microcontrôleurs connectés (comme l’ESP32) permettent de surveiller et contrôler des dispositifs à distance via internet.

✅ Complément utile :
- Exemple : capteur de température + envoi vers application.

● Systèmes embarqués : dans les montres intelligentes, appareils médicaux, et téléphones, où ils gèrent les fonctionnalités essentielles avec un faible encombrement.

✅ Complément utile :
- “Embarqué” = petit, fiable, faible consommation.

---

## III. Fonctions de base et configuration des broches d’un microcontrôleur

La configuration des broches du microcontrôleur est cruciale pour interagir avec les composants externes. Chaque broche peut être paramétrée pour une fonction spécifique.

● Broches d’entrée (INPUT) :
○ Elles reçoivent des signaux externes, comme ceux des capteurs ou des interrupteurs.
○ Exemple : une broche en mode entrée peut lire l’état d’un bouton poussoir, retournant une valeur 0 (LOW) ou 1 (HIGH) selon que le bouton est appuyé ou non.

✅ Complément utile :
- Sur Arduino, on lit une entrée numérique avec `digitalRead(pin)`.
- Option pratique : `INPUT_PULLUP` (résistance interne activée) → câblage plus simple.

● Broches de sortie (OUTPUT) :
○ Elles envoient des signaux pour contrôler des dispositifs comme les LED, les relais ou les moteurs.
○ Exemple : une broche en mode sortie peut activer une LED en passant de l’état 0 (LOW) à 1 (HIGH).

✅ Complément utile :
- Sur Arduino, on commande une sortie avec `digitalWrite(pin, HIGH/LOW)`.

● Broches analogiques et numériques :
○ Les broches analogiques mesurent des variations de tension continue, typiquement avec une précision définie (ex. : 10 bits pour Arduino, soit 1024 niveaux).
○ Les broches numériques n’ont que deux états (0 ou 1), pour des signaux de type tout-ou-rien.

✅ Complément utile :
- `analogRead(A0)` renvoie un nombre **entre 0 et 1023**.
- Une entrée analogique sert à lire une valeur “progressive” (potentiomètre, LDR…).

<p align="center">
  <img src="./images/analog_read_0_1023.png" alt="analogRead : 0 à 1023" width="90%"><br>
  <em>Illustration attendue : jauge 0→1023 associée à une tension 0V→5V.</em>
</p>

● Broches spéciales (PWM, I2C, SPI) :
○ PWM (modulation de largeur d’impulsion) : une broche PWM génère des signaux analogiques simulés, souvent pour contrôler la luminosité d’une LED ou la vitesse d’un moteur.
○ I2C et SPI : protocoles de communication pour échanger des données avec des périphériques (écrans, capteurs) sur des broches spécifiques, avec une haute vitesse de transfert.

✅ Complément utile :
- PWM : on utilise `analogWrite(pinPWM, valeur)` (0→255).
- I2C/SPI : utiles pour capteurs/écrans (plus tard). Ici on retient que ce sont des “liaisons de données”.

---

## IV. Langage et environnement de programmation des microcontrôleurs

La plupart des microcontrôleurs sont programmés en langage C ou en C++ pour des raisons de simplicité et d’efficacité. Les environnements de développement spécifiques facilitent la programmation et le débogage des microcontrôleurs.

● Arduino IDE :
○ Un environnement de développement simplifié pour programmer des microcontrôleurs de type Arduino (AVR).
○ Il utilise une version simplifiée du C++, avec des fonctions de base prêtes à l’emploi pour configurer les broches, lire les capteurs, et contrôler les composants.
○ Exemple : l’instruction pinMode(pin, mode) configure une broche en entrée ou sortie, tandis que digitalWrite(pin, value) définit l’état d’une broche en sortie.

✅ Complément utile :
- Étapes Arduino : écrire → vérifier → téléverser → tester.
- Le “Serial Monitor” aide à voir des valeurs (debug simple).

● MicroPython :
○ Un interpréteur Python adapté pour les microcontrôleurs comme l’ESP8266 ou l’ESP32, plus accessible pour les débutants.
○ Exemple : from machine import Pin permet d’utiliser les broches d’E/S et Pin(2, Pin.OUT).on() allume une LED branchée sur la broche 2.

✅ Complément utile :
- MicroPython = très pratique mais pas sur Arduino UNO classique.
- On retient : plusieurs environnements existent selon la carte.

● Atmel Studio :
○ Un IDE avancé pour programmer les microcontrôleurs AVR en C, avec plus de contrôle sur les registres internes et les configurations précises des périphériques.

✅ Complément utile :
- IDE “expert” : plus complexe, mais plus de contrôle bas niveau.

---

## V. Structure de base d’un programme pour microcontrôleur

Les programmes pour microcontrôleur suivent une structure spécifique, organisée autour de deux fonctions essentielles : setup() et loop().

● Fonction setup() :
○ Elle s’exécute une seule fois au démarrage pour configurer les broches et les paramètres initiaux.
○ Exemple : dans setup(), utiliser pinMode() pour définir une broche en entrée ou en sortie selon son rôle.

✅ Complément utile :
- setup = réglages initiaux : `pinMode`, `Serial.begin(...)`, etc.

● Fonction loop() :
○ Elle s’exécute en boucle continue, réalisant les actions et contrôles en permanence tant que le microcontrôleur est alimenté.
○ Exemple : lire une valeur de capteur à chaque itération et allumer une LED si la valeur dépasse un seuil.

✅ Complément utile :
- loop = “programme en continu” : lire → décider → agir → recommencer.

● Exemple de programme simple :
● Ce programme fait clignoter une LED branchée sur la broche 13 toutes les secondes.

✅ Complément utile :
- La broche 13 est souvent reliée à une LED intégrée sur Arduino.
- Sur la fiche (page 4), l’exemple montre bien la structure setup/loop. :contentReference[oaicite:6]{index=6}

<p align="center">
  <img src="./images/exemple_blink_setup_loop.png" alt="Exemple Blink : setup/loop" width="90%"><br>
  <em>Illustration attendue : capture d’écran du code Blink montrant setup() et loop().</em>
</p>

---

## VI. Les bases de la programmation de capteurs et actionneurs

La programmation de microcontrôleurs implique souvent l’interaction avec des capteurs et des actionneurs. Les capteurs détectent les changements dans l’environnement, tandis que les actionneurs réalisent des actions en réponse aux commandes du microcontrôleur.

● Lecture des capteurs :
○ Les capteurs analogiques (capteurs de lumière, température) envoient une tension proportionnelle à la grandeur mesurée, lue par les broches analogiques avec analogRead().
○ Les capteurs numériques (interrupteurs, détecteurs de mouvement) indiquent un état binaire (0 ou 1) lu avec digitalRead().
○ Exemple : lire la luminosité ambiante avec un capteur LDR et allumer une LED si la lumière est faible.

✅ Complément utile :
- analogRead = 0→1023 (selon tension).
- digitalRead = LOW/HIGH (0/1).

● Contrôle des actionneurs :
○ Les actionneurs comme les moteurs et les LED sont commandés en modifiant l’état des broches de sortie avec digitalWrite() ou analogWrite() pour ajuster l’intensité.
○ Exemple : contrôler la vitesse d’un moteur en envoyant un signal PWM sur une broche de sortie.

✅ Complément utile :
- digitalWrite = ON/OFF.
- analogWrite = variation (0→255) sur broche PWM.

Exemples pratiques de programmes pour microcontrôleur
● Commande de LED en fonction de la lumière ambiante :
○ Un capteur de lumière (LDR) mesure la luminosité, et le microcontrôleur allume ou éteint une LED en fonction de cette valeur.
○ Exemple de code :

✅ Complément utile :
- LDR : souvent en diviseur de tension avec une résistance.
- On fixe un seuil (ex : 300) et on teste.

● Contrôle d’un moteur avec un potentiomètre :
○ Un potentiomètre envoie une tension variable au microcontrôleur, qui utilise cette valeur pour ajuster la vitesse du moteur via PWM.
○ Exemple de code :

✅ Complément utile :
- Le potentiomètre donne 0→1023, le PWM attend 0→255 : on “mappe” (conversion).
- Sur la fiche (page 6), l’exemple illustre analogRead + map + analogWrite. :contentReference[oaicite:7]{index=7}

<p align="center">
  <img src="./images/potentiometre_map_pwm.png" alt="Potentiomètre : analogRead + map + PWM" width="90%"><br>
  <em>Illustration attendue : capture du code montrant analogRead, map, analogWrite.</em>
</p>

---

# Tableau récapitulatif (à mémoriser pour E2)
| Besoin | Entrée (capteur) | Lecture | Décision | Sortie (actionneur) | Action |
|---|---|---|---|---|---|
| Allumer une LED si sombre | LDR | analogRead(A0) | if (val < seuil) | LED | digitalWrite |
| LED variable | potentiomètre | analogRead(A0) | conversion | LED | analogWrite |
| Bouton commande | bouton | digitalRead(pin) | if/else | LED | digitalWrite |
