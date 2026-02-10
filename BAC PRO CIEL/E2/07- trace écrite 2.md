---
title: "E2 - Pack 07 - Fiche de cours élève - Microcontrôleurs & programmation basique (Arduino)"
module: "BAC PRO CIEL - E2"
version: "1.0"
---

# Systèmes microcontrôleurs et programmation basique (Arduino)

## 🎯 Objectifs (niveau E2)
À la fin de cette fiche, je suis capable de :

| Je sais… | Exemple attendu en E2 |
|---|---|
| **Expliquer** ce qu’est un microcontrôleur | “C’est un petit ordinateur dédié : CPU + mémoire + entrées/sorties.” |
| **Nommer** les blocs internes (CPU, Flash, RAM, E/S, bus…) | “Flash = programme, RAM = variables, E/S = broches.” |
| **Configurer** une broche en entrée/sortie | `pinMode(pin, INPUT/OUTPUT/INPUT_PULLUP)` |
| **Lire** un capteur et **agir** sur un actionneur | “Je lis → je décide (if) → j’écris (digitalWrite/analogWrite).” |
| **Reconnaître** analogique / numérique / PWM | “analogRead 0→1023 ; digitalRead LOW/HIGH ; PWM 0→255.” |
| **Déboguer simplement** avec le moniteur série | `Serial.println(valeur)` |

---

## 🔑 Idée essentielle avant de commencer
Un **microcontrôleur**, c’est un **petit ordinateur** dédié à une tâche précise.

Il exécute **un programme** et pilote des **broches (pins)** reliées à des **capteurs** (entrées) et des **actionneurs** (sorties) : LED, relais, moteur, buzzer…

➡️ En pratique, on retrouve toujours la même boucle :
**lire → décider → agir** (en continu tant que la carte est alimentée).

<p align="center">
  <img src="./images/chaine_capteur_decision_actionneur.png" alt="Chaîne classique : capteur → lecture → décision → actionneur" width="90%"><br>
  <em>Illustration attendue : capteur → microcontrôleur (lecture/décision) → actionneur.</em>
</p>

---

## I. Introduction aux systèmes microcontrôleurs : caractéristiques et structure

Les microcontrôleurs sont des circuits intégrés programmables qui contrôlent des systèmes électroniques en exécutant des instructions.  
Ils combinent **un processeur**, **de la mémoire** et des **périphériques d’entrée/sortie** (E/S) dans un seul composant.

👉 Un microcontrôleur = **CPU + mémoire + E/S** (tout-en-un)  
C’est pour cela qu’on le retrouve partout (objets du quotidien, robotique, automobile…).

<p align="center">
  <img src="./images/microcontroleur_blocs.png" alt="Blocs d’un microcontrôleur : CPU, mémoire, E/S, bus interne" width="90%"><br>
  <em>Illustration attendue : schéma en blocs CPU + mémoire + E/S + bus, reliés entre eux.</em>
</p>

### ● Architecture du microcontrôleur

#### ○ Processeur (CPU)
Le CPU exécute les instructions du programme :  
- calculs, comparaisons, décisions (**if/else**),  
- contrôle des broches (allumer/éteindre, lire un bouton, etc.).

#### ○ Mémoire
On distingue plusieurs mémoires (à connaître car elles n’ont pas le même rôle) :

| Type de mémoire | Rôle (simple) | “Elle garde les données quand on coupe l’alim ?” |
|---|---|---|
| **Flash** | stocke le **programme** (ce que tu téléverses) | ✅ Oui |
| **RAM** | stocke les **variables** et données en cours | ❌ Non (elle se vide) |
| **EEPROM** (optionnelle) | stocke des données **modifiables** (réglages) | ✅ Oui |

Exemple concret :
- Flash : ton code Arduino
- RAM : la valeur lue par un capteur, un compteur, une variable
- EEPROM : mémoriser un **seuil** même après coupure

#### ○ Périphériques d’E/S (Entrées/Sorties)
Ils permettent au microcontrôleur de communiquer avec l’extérieur via les **broches**.

➡️ Une broche = un **point de connexion** que tu configures :
- soit en **entrée** (je lis un capteur/bouton),
- soit en **sortie** (je commande une LED/relais…).

#### ○ Bus interne
Le bus est la “route interne” qui transporte les informations entre CPU, mémoire et E/S.

---

### ● Exemples de microcontrôleurs courants
| Famille | Où on les rencontre | Remarque simple |
|---|---|---|
| **AVR (Atmel)** | cartes Arduino classiques | programmation Arduino IDE (C/C++) |
| **PIC (Microchip)** | industrie, cartes dédiées | robuste, très utilisé en automatismes |
| **ESP8266 / ESP32** | projets connectés (IoT) | Wi-Fi (et souvent Bluetooth sur ESP32) |

---

## II. Applications des microcontrôleurs dans les systèmes électroniques

Les microcontrôleurs sont présents dans de nombreux domaines où ils contrôlent des systèmes variés :

| Domaine | Ce qu’ils font (simple) |
|---|---|
| **Automobile** | lisent capteurs (vitesse/pression) → commandent actionneurs (ABS, airbags…) |
| **Électroménager** | mesurent (température/eau) → pilotent (moteur, résistance chauffante) |
| **Robotique** | capteurs (distance) → décision → moteurs |
| **IoT** | mesure + envoi vers application (ESP32/ESP8266) |
| **Systèmes embarqués** | petits, fiables, faible consommation (montres, appareils médicaux…) |

---

## III. Fonctions de base et configuration des broches

### ● Broches d’entrée (INPUT)
Elles reçoivent des signaux externes (capteurs, interrupteurs…).

- Exemple : un bouton renvoie LOW/HIGH selon qu’il est appuyé ou non.
- Sur Arduino, on lit une entrée numérique avec : `digitalRead(pin)`.

✅ Option très pratique : `INPUT_PULLUP`  
Cette option active une résistance interne : elle simplifie le câblage (utile avec un bouton).

> Astuce : avec `INPUT_PULLUP`, l’état est souvent **inversé** :  
> - bouton relâché → HIGH  
> - bouton appuyé → LOW

### ● Broches de sortie (OUTPUT)
Elles envoient des signaux pour commander LED, relais, moteurs (via driver), etc.

- Sur Arduino, on commande une sortie avec : `digitalWrite(pin, HIGH/LOW)`.

⚠️ Règle atelier (sécurité matériel) :
- une **LED** doit presque toujours avoir **une résistance** en série.
- un **moteur** ne se branche pas directement sur une broche (il faut un module/driver), car il consomme trop.

---

### ● Broches analogiques et numériques

| Type de broche | Ce qu’elle mesure/commande | Fonction Arduino |
|---|---|---|
| **Numérique** | 2 états : 0/1 (LOW/HIGH) | `digitalRead` / `digitalWrite` |
| **Analogique** | valeur progressive (tension) | `analogRead(A0)` → **0 à 1023** |

Sur Arduino (cas le plus courant), `analogRead(A0)` renvoie un nombre **entre 0 et 1023** (10 bits).  
Cela correspond à une tension comprise entre 0V et la tension de référence (souvent 5V sur Arduino UNO).

<p align="center">
  <img src="./images/analog_read_0_1023.png" alt="analogRead : 0 à 1023 correspond à une tension 0V à 5V" width="90%"><br>
  <em>Illustration attendue : jauge 0→1023 associée à une tension 0V→5V.</em>
</p>

💡 Astuce : convertir une lecture analogique en tension (approximation simple)  
Si référence = 5V :  
`U ≈ valeur * 5 / 1023`

---

### ● Broches spéciales (PWM, I2C, SPI)

#### ○ PWM (modulation de largeur d’impulsion)
Le PWM permet de simuler un “analogique” en sortie (utile pour luminosité LED, vitesse moteur via driver).  
Sur Arduino, on utilise : `analogWrite(pinPWM, valeur)` avec **0→255**.

👉 À retenir :
- `digitalWrite` = ON/OFF (tout-ou-rien)
- `analogWrite` = variation (0→255) sur broche PWM

#### ○ I2C et SPI
Ce sont des liaisons de données pour communiquer avec des capteurs/écrans.  
Ici, on retient surtout : **ce sont des “bus de communication”** (plus tard, on verra en détail).

---

## IV. Langage et environnement de programmation

### ● Arduino IDE
- environnement simple pour programmer Arduino
- langage : C/C++ simplifié
- fonctions de base prêtes à l’emploi :
  - `pinMode(pin, mode)` : configure une broche
  - `digitalWrite(pin, value)` : commande une sortie
  - `digitalRead(pin)` : lit une entrée

✅ Méthode de travail Arduino (simple) :
**écrire → vérifier → téléverser → tester**

💡 Outil très utile : **Serial Monitor**  
Il permet d’afficher des valeurs pour comprendre ce que fait le programme (débogage).

### ● MicroPython
- Python adapté à certains microcontrôleurs (souvent ESP8266/ESP32)
- plus accessible pour débuter, mais pas sur Arduino UNO “classique” (selon carte)

### ● Atmel Studio
IDE plus “expert” pour AVR, plus bas niveau (plus complexe, plus de contrôle).

---

## V. Structure de base d’un programme Arduino

Les programmes Arduino sont organisés autour de deux fonctions :

### ● `setup()`
S’exécute **une seule fois** au démarrage : réglages initiaux.  
Exemples : `pinMode(...)`, `Serial.begin(...)`.

### ● `loop()`
S’exécute **en boucle** tant que l’Arduino est alimenté :  
lire → décider → agir → recommencer.

<p align="center">
  <img src="./images/exemple_blink_setup_loop.png" alt="Exemple Blink : structure setup() et loop()" width="90%"><br>
  <em>Illustration attendue : capture d’écran du code Blink montrant setup() et loop().</em>
</p>

✅ Exemple minimal (structure) :
```cpp
void setup() {
  // réglages initiaux
}

void loop() {
  // programme en continu
}
