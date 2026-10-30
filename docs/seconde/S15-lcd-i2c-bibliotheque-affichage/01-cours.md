# 📘 FICHE DE COURS ÉLÈVE — S15
## LCD I2C : bibliothèque & affichage · Intégration LM35 · Proto maquette final

---

> **Compétences travaillées** : C2.1 – C3.1 – C3.2 – C4.1
> **Durée de lecture guidée** : ~45 minutes
> **Prérequis** : S9 (capteur LM35, `analogRead`), S14 (HC-05, `SoftwareSerial`)

---

## 🗂️ Sommaire

1. Le protocole I2C — principe et intérêt
2. L'écran LCD 16×2 avec module I2C
3. La bibliothèque LiquidCrystal_I2C — installation et fonctions
4. Rappel : le capteur LM35 (S9)
5. Intégration LM35 → LCD : afficher la température en temps réel
6. Intégration complète : LM35 + LCD + HC-05
7. Structure du proto maquette final
8. Vocabulaire clé à maîtriser

---

## 1. Le protocole I2C — principe et intérêt

### 1.1 Pourquoi I2C ?

Sans I2C, un écran LCD classique (sans module I2C) nécessite **jusqu'à 10 broches** de l'Arduino. C'est énorme sur un projet avec plusieurs composants !

Le protocole **I2C** (Inter-Integrated Circuit, prononcé "I-deux-C" ou "I-carré-C") réduit cette connexion à **seulement 2 fils**, quel que soit le nombre de composants connectés.

```
[ILLUSTRATION 1]
Légende : Comparaison côte à côte entre un câblage LCD classique (10 fils partant de l'Arduino vers le LCD,
représenté encombré et complexe) et un câblage LCD I2C (uniquement 4 fils : VCC, GND, SDA, SCL),
représenté propre et épuré. Les deux montages aboutissent au même écran LCD 16x2.
PROMPT ILLUSTRATION : "Side-by-side comparison diagram: Left side shows 'LCD classique' with Arduino UNO
connected to LCD 16x2 using 10 colored wires (messy, complex). Right side shows 'LCD I2C' with Arduino UNO
connected to LCD+I2C module using only 4 wires (VCC red, GND black, SDA blue, SCL yellow).
Clean flat technical style, labeled in French, white background, emphasis on simplicity of I2C."
```

### 1.2 Les deux fils du bus I2C

| Fil | Nom complet | Rôle |
|---|---|---|
| **SDA** | Serial Data | Transmission des données (bidirectionnel) |
| **SCL** | Serial Clock | Signal d'horloge — synchronise les échanges |

> 💡 **Analogie** : Imagine une grande salle de classe. Le professeur (Arduino = **maître**) pose des questions. Chaque élève a un numéro de siège (son **adresse I2C**). Quand le prof dit "numéro 39, réponds", seul l'élève 39 répond. Tous parlent sur le **même micro** (SDA), mais chacun attend d'être appelé. L'horloge (SCL), c'est le rythme imposé par le prof pour que tout le monde soit synchronisé.

### 1.3 Le bus I2C : maître et esclaves

```
[ILLUSTRATION 2]
Légende : Schéma du bus I2C avec un Arduino UNO (Maître) au centre, relié par deux fils SDA et SCL
à trois périphériques esclaves : LCD I2C (adresse 0x27), capteur de température (0x48) et RTC (0x68).
Chaque esclave est représenté avec son adresse hexadécimale clairement affichée.
PROMPT ILLUSTRATION : "I2C bus architecture diagram: Arduino UNO labeled 'Maître' in center,
connected via two horizontal bus lines (SDA blue, SCL yellow) to three slave devices:
LCD I2C module (address 0x27), temperature sensor (0x48), RTC module (0x68).
Each slave shows address badge. Clean engineering diagram, French labels, white background."
```

| Rôle | Qui ? | Nombre |
|---|---|---|
| **Maître** | Arduino | 1 seul (en général) |
| **Esclave** | LCD, capteurs, modules… | Jusqu'à 127 par bus |

**Broches I2C sur Arduino UNO :**

| Broche Arduino | Fonction I2C |
|---|---|
| **A4** | SDA |
| **A5** | SCL |

> ⚠️ Sur Arduino UNO, **ne pas utiliser A4 et A5 comme entrées analogiques** si tu utilises I2C — elles sont réservées au bus.

---

## 2. L'écran LCD 16×2 avec module I2C

### 2.1 Description du composant

```
[ILLUSTRATION 3]
Légende : Vue annotée de l'ensemble LCD 16x2 + module I2C soudé au dos.
Face avant : 32 emplacements de caractères (16 colonnes × 2 lignes) avec la numérotation des positions
(0,0) en haut à gauche, (15,0) en haut à droite, (0,1) en bas à gauche.
Face arrière (vue de profil) : module I2C PCF8574 avec ses 4 broches (VCC, GND, SDA, SCL) étiquetées
et le potentiomètre de contraste visible.
PROMPT ILLUSTRATION : "Technical diagram of LCD 16x2 with I2C module. Front view shows 32 character cells
(16 columns x 2 rows) with cursor position grid labeled: (0,0) top-left, (15,0) top-right, (0,1) bottom-left.
Back view (side inset) shows I2C PCF8574 module with 4 pins labeled VCC, GND, SDA, SCL and blue contrast
potentiometer. Professional component diagram, French labels, white background."
```

| Caractéristique | Valeur |
|---|---|
| Format d'affichage | 16 colonnes × 2 lignes = 32 caractères |
| Tension d'alimentation | 5V (VCC) |
| Protocole de communication | I2C via module PCF8574 |
| Adresse I2C typique | **0x27** ou **0x3F** (selon le fabricant) |
| Rétroéclairage | Contrôlable via bibliothèque |
| Contraste | Réglable par potentiomètre au dos |

### 2.2 Câblage LCD I2C → Arduino UNO

| Broche LCD I2C | → | Broche Arduino UNO |
|---|---|---|
| **VCC** | Fil rouge | **5V** |
| **GND** | Fil noir | **GND** |
| **SDA** | Fil bleu | **A4** |
| **SCL** | Fil jaune | **A5** |

---

## 3. La bibliothèque LiquidCrystal_I2C

### 3.1 Installation

1. Dans l'IDE Arduino : **Outils → Gérer les bibliothèques**
2. Recherche : `LiquidCrystal I2C`
3. Installer la version de **Frank de Brabander** (la plus répandue)

### 3.2 Initialisation dans le sketch

```cpp
#include <LiquidCrystal_I2C.h>

// LiquidCrystal_I2C(adresse, colonnes, lignes)
LiquidCrystal_I2C lcd(0x27, 16, 2);
//                     ^^^^   ^^  ^
//                     adresse  colonnes  lignes

void setup() {
  lcd.init();         // Initialise le LCD
  lcd.backlight();    // Active le rétroéclairage
}
```

> ⚠️ Si rien ne s'affiche : remplace `0x27` par `0x3F` et retente.

### 3.3 Fonctions essentielles à maîtriser

| Fonction | Syntaxe | Description |
|---|---|---|
| `init()` | `lcd.init();` | Initialise le contrôleur I2C |
| `backlight()` | `lcd.backlight();` | Allume le rétroéclairage |
| `noBacklight()` | `lcd.noBacklight();` | Éteint le rétroéclairage |
| `setCursor()` | `lcd.setCursor(col, ligne);` | Place le curseur à la position donnée (col 0-15, ligne 0-1) |
| `print()` | `lcd.print("Texte");` | Affiche une chaîne de caractères |
| `print()` | `lcd.print(valeur);` | Affiche une valeur numérique |
| `clear()` | `lcd.clear();` | Efface tout l'écran et replace le curseur en (0,0) |
| `home()` | `lcd.home();` | Ramène le curseur en (0,0) sans effacer |

### 3.4 Le système de coordonnées du LCD

```
[ILLUSTRATION 4]
Légende : Grille de positionnement du curseur LCD 16x2. Axe horizontal = colonne (0 à 15),
Axe vertical = ligne (0 = première ligne du haut, 1 = deuxième ligne). Quelques cases sont remplies
avec des exemples de caractères pour montrer où setCursor(0,0), setCursor(8,0) et setCursor(0,1) placent le curseur.
PROMPT ILLUSTRATION : "Grid diagram showing LCD 16x2 cursor coordinate system.
16 columns (0-15 on X axis) and 2 rows (0-1 on Y axis). Grid cells shown.
Highlighted cells: (0,0)=top-left marked red with 'setCursor(0,0)', (8,0)=middle-top in blue, (0,1)=bottom-left in green.
Example text showing 'Temp: 23.4C' on row 0 and 'CIEL  OK' on row 1. 
Clean diagram, French axis labels, professional style."
```

> 📌 **Règle à retenir** :
> - `setCursor(colonne, ligne)` — **d'abord la colonne**, ensuite la ligne
> - La ligne **0** est en **haut**, la ligne **1** est en **bas**
> - La colonne **0** est à **gauche**, la colonne **15** est à **droite**

### 3.5 Astuce : afficher une valeur avec unité sur le LCD

```cpp
// Problème courant : la valeur et l'unité doivent être envoyées en deux appels
float temperature = 23.4;

lcd.setCursor(0, 0);
lcd.print("Temp: ");      // Affiche le texte fixe
lcd.print(temperature);   // Affiche la valeur numérique
lcd.print(" C");          // Affiche l'unité

// Résultat à l'écran : "Temp: 23.40 C"
```

> ⚠️ **Artefact fréquent** : Si la valeur change de longueur (ex : passe de 23.4 à 9.8), les anciens caractères restent visibles. Solution : appeler `lcd.clear()` avant de réécrire, **ou** forcer un effacement de la ligne avec des espaces.

---

## 4. Rappel — Le capteur LM35 (S9)

```
[ILLUSTRATION 5]
Légende : Vue du capteur LM35 avec ses 3 broches identifiées (de gauche à droite : +Vs = alimentation +5V,
Vout = tension de sortie proportionnelle à la température, GND = masse), et la formule de conversion
encadrée : Température (°C) = (Vout × 100). Rappel visuel du graphique linéaire sortie/température.
PROMPT ILLUSTRATION : "LM35 temperature sensor diagram: front view of TO-92 package with 3 pins labeled:
Pin 1 (+Vs 5V), Pin 2 (Vout → Arduino A0), Pin 3 (GND). 
Inset shows conversion formula 'T(°C) = tension(V) × 100' in a highlighted box.
Small linear graph showing Vout vs Temperature (0°C=0V, 100°C=1V). 
Clean technical diagram, French labels, white background."
```

### Rappel de la formule de conversion

```cpp
int valeurBrute = analogRead(A0);          // Lecture 0-1023

float tension = valeurBrute * (5.0 / 1023.0);  // Conversion en Volts (0 à 5V)

float temperature = tension * 100.0;            // Conversion en °C
// (Le LM35 produit 10 mV par degré Celsius → 1°C = 0.01V → T = V × 100)
```

| Valeur brute | Tension (V) | Température (°C) |
|---|---|---|
| 0 | 0,00 V | 0°C |
| 102 | 0,50 V | 50°C |
| 204 | 1,00 V | 100°C |
| 1023 | 5,00 V | 500°C (hors plage LM35) |

> 📌 Le LM35 mesure entre **−55°C et +150°C**. En usage normal (température ambiante), on obtient des valeurs entre 150 et 250 sur `analogRead()`.

---

## 5. Intégration LM35 → LCD : afficher la température en temps réel

### 5.1 Schéma d'intégration

```
[ILLUSTRATION 6]
Légende : Schéma de câblage Fritzing complet : Arduino UNO au centre, LM35 connecté sur A0 (5V, GND, Vout→A0),
LCD I2C connecté sur A4 (SDA) et A5 (SCL) avec VCC et GND. Les fils sont colorés selon leur fonction.
PROMPT ILLUSTRATION : "Fritzing-style wiring diagram: Arduino UNO center, LM35 sensor on left connected
to A0 (Vout), 5V and GND. LCD 16x2 with I2C module on right connected to A4 (SDA, blue wire),
A5 (SCL, yellow wire), 5V (red) and GND (black). Color-coded wires, component labels, white background,
professional PCB diagram style, French annotations."
```

### 5.2 Sketch d'affichage température sur LCD

```cpp
// ============================================
// S15 – LM35 + LCD I2C
// Affichage de la température en temps réel
// ============================================

#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);   // ← adapter l'adresse si nécessaire

const int BROCHE_LM35 = A0;            // Broche de lecture du LM35

void setup() {
  Serial.begin(9600);
  lcd.init();
  lcd.backlight();

  // Message d'accueil (affiché 2 secondes)
  lcd.setCursor(0, 0);
  lcd.print("BAC PRO CIEL");
  lcd.setCursor(0, 1);
  lcd.print("  Station Meteo");
  delay(2000);
  lcd.clear();
}

void loop() {
  // --- Lecture et conversion LM35 ---
  int valeurBrute   = analogRead(BROCHE_LM35);
  float tension     = valeurBrute * (5.0 / 1023.0);
  float temperature = tension * 100.0;

  // --- Affichage sur LCD ---
  lcd.setCursor(0, 0);
  lcd.print("Temperature :   ");   // Les espaces finaux écrasent les anciens caractères

  lcd.setCursor(0, 1);
  lcd.print(temperature, 1);       // 1 = 1 décimale
  lcd.print(" C          ");       // Espaces pour nettoyer les résidus

  // --- Affichage moniteur série (debug) ---
  Serial.print("Temp brute : ");   Serial.print(valeurBrute);
  Serial.print(" | Tension : ");   Serial.print(tension, 3);
  Serial.print(" V | Temp : ");    Serial.print(temperature, 1);
  Serial.println(" degC");

  delay(1000);    // Rafraîchissement toutes les secondes
}
```

---

## 6. Intégration complète : LM35 + LCD + HC-05

### 6.1 Architecture du proto maquette final

```
[ILLUSTRATION 7]
Légende : Schéma bloc de l'architecture complète du proto maquette. Au centre : Arduino UNO.
À gauche : LM35 (entrée analogique A0) avec flèche "donnée de température". En haut : LCD I2C
(bus I2C sur A4/A5) avec flèche "affichage local". À droite : HC-05 (SoftwareSerial broches 10/11)
avec flèche "envoi BT" vers un pictogramme Smartphone. Tous les composants sont reliés à GND/5V.
PROMPT ILLUSTRATION : "System architecture block diagram for Arduino proto-board.
Center: Arduino UNO. Left: LM35 (connected to A0, labeled 'Entrée analogique').
Top: LCD I2C 16x2 (connected to A4/A5, labeled 'Affichage local - Bus I2C').
Right: HC-05 Bluetooth (connected to pins 10/11, labeled 'Envoi sans fil').
Far right: Smartphone icon (labeled 'Affichage déporté - App BT').
Arrows showing data flow. Color-coded connections. Clean flat design, French labels."
```

### 6.2 Sketch du proto maquette final (intégration complète)

```cpp
// ================================================
// S15 – Proto Maquette Final
// LM35 + LCD I2C + HC-05 Bluetooth
// Auteur : [Ton nom]   Date : [Date S15]
// ================================================

#include <LiquidCrystal_I2C.h>
#include <SoftwareSerial.h>

// ---- Déclarations des objets ----
LiquidCrystal_I2C lcd(0x27, 16, 2);     // LCD I2C (adresse à adapter)
SoftwareSerial bluetooth(10, 11);        // HC-05 : RX=10, TX=11

// ---- Constantes ----
const int BROCHE_LM35     = A0;         // Capteur LM35
const int INTERVALLE_MS   = 2000;       // Envoi toutes les 2 secondes

// ---- Variables globales ----
float temperature = 0.0;
unsigned long dernierEnvoi = 0;

// ================================================
void setup() {
  Serial.begin(9600);
  bluetooth.begin(9600);

  // Initialisation LCD
  lcd.init();
  lcd.backlight();
  lcd.setCursor(0, 0);
  lcd.print("Station Meteo");
  lcd.setCursor(0, 1);
  lcd.print("Initialisation..");
  delay(1500);
  lcd.clear();

  // Message de démarrage
  Serial.println("=== Proto Maquette S15 prêt ===");
  bluetooth.println("=== Station Meteo BT ready ===");
}

// ================================================
void loop() {

  // ---- 1. Lecture et calcul de la température ----
  int brut        = analogRead(BROCHE_LM35);
  float tension   = brut * (5.0 / 1023.0);
  temperature     = tension * 100.0;

  // ---- 2. Affichage sur le LCD ----
  lcd.setCursor(0, 0);
  lcd.print("Temp:           ");   // Efface la ligne
  lcd.setCursor(6, 0);
  lcd.print(temperature, 1);
  lcd.print((char)223);            // Caractère degré °
  lcd.print("C");

  lcd.setCursor(0, 1);
  lcd.print("BT: ");
  lcd.print(bluetooth ? "OK  " : "---");   // Indicateur BT (statique ici)

  // ---- 3. Envoi via Bluetooth (toutes les 2 secondes) ----
  if (millis() - dernierEnvoi >= INTERVALLE_MS) {
    bluetooth.print("Temperature: ");
    bluetooth.print(temperature, 1);
    bluetooth.println(" degC");
    dernierEnvoi = millis();
  }

  // ---- 4. Commandes reçues depuis le smartphone ----
  if (bluetooth.available()) {
    String cmd = "";
    while (bluetooth.available()) {
      cmd += (char)bluetooth.read();
      delay(5);
    }
    cmd.trim();

    if (cmd == "TEMP") {
      bluetooth.print("Temp actuelle: ");
      bluetooth.print(temperature, 1);
      bluetooth.println(" degC");
    }
    else if (cmd == "STOP") {
      bluetooth.println("Envoi automatique stoppe.");
      dernierEnvoi = millis() + 999999UL;    // Bloque l'envoi auto
    }
    else if (cmd == "START") {
      dernierEnvoi = 0;
      bluetooth.println("Envoi automatique repris.");
    }
  }

  // ---- 5. Debug moniteur série ----
  Serial.print("T="); Serial.print(temperature, 1); Serial.println("°C");

  delay(500);
}
```

### 6.3 Tableau de câblage complet du proto maquette

| Composant | Broche composant | → | Broche Arduino |
|---|---|---|---|
| **LM35** | +Vs | → | 5V |
| **LM35** | GND | → | GND |
| **LM35** | Vout | → | A0 |
| **LCD I2C** | VCC | → | 5V |
| **LCD I2C** | GND | → | GND |
| **LCD I2C** | SDA | → | A4 |
| **LCD I2C** | SCL | → | A5 |
| **HC-05** | VCC | → | 5V |
| **HC-05** | GND | → | GND |
| **HC-05** | TXD | → | Pin 10 (direct) |
| **HC-05** | RXD | → | Pin 11 (via pont diviseur 1kΩ+2kΩ) |

---

## 7. Structure du proto maquette final

### Fonctionnalités du proto A1

| N° | Fonctionnalité | Composant | Statut |
|---|---|---|---|
| F1 | Mesure de température en continu | LM35 | À valider |
| F2 | Affichage local temps réel sur LCD | LCD I2C | À valider |
| F3 | Envoi automatique de la température via BT | HC-05 | À valider |
| F4 | Commande manuelle `TEMP` depuis smartphone | HC-05 | À valider |
| F5 | Commandes `START` / `STOP` de l'envoi auto | HC-05 | À valider |
| F6 | Message d'accueil au démarrage | LCD | À valider |

> 📌 Ce tableau sera le point de départ de ton **protocole de tests en S17**.

---

## 8. Vocabulaire clé à maîtriser pour l'examen

| Terme | Définition |
|---|---|
| **I2C** | Inter-Integrated Circuit — protocole série synchrone à 2 fils (SDA + SCL) permettant de connecter plusieurs périphériques sur le même bus |
| **SDA** | Serial Data — fil de transmission des données I2C (bidirectionnel) |
| **SCL** | Serial Clock — fil d'horloge I2C, impose le rythme des échanges |
| **Adresse I2C** | Numéro hexadécimal unique identifiant un périphérique sur le bus (ex : 0x27) |
| **Maître / Esclave** | Le maître (Arduino) initie les communications ; les esclaves (LCD, capteurs) répondent quand ils sont appelés |
| **Bus** | Liaison partagée sur laquelle plusieurs composants communiquent selon des règles d'adressage |
| **LiquidCrystal_I2C** | Bibliothèque Arduino pour piloter un écran LCD via le protocole I2C |
| **`setCursor(col, ligne)`** | Positionne le curseur d'écriture sur le LCD (col = 0 à 15, ligne = 0 ou 1) |
| **Bibliothèque** | Ensemble de fonctions prêtes à l'emploi que l'on inclut dans un sketch pour ne pas tout reprogrammer |
| **LM35** | Capteur de température analogique produisant 10 mV par degré Celsius |
| **`millis()`** | Fonction Arduino retournant le nombre de millisecondes écoulées depuis le démarrage — utilisée pour les temporisations non bloquantes |
| **Proto maquette** | Prototype fonctionnel, souvent sur breadboard, permettant de valider un concept avant la version finale |

---

> 📌 **Retiens l'essentiel en 4 points :**
> 1. I2C connecte de nombreux composants avec seulement **2 fils + alimentation**
> 2. Chaque composant I2C a une **adresse unique** — toujours commencer par un scan
> 3. `setCursor(colonne, ligne)` — **colonne d'abord**, ligne ensuite (0 = haut, 1 = bas)
> 4. Le proto maquette final combine **3 modules** : LM35 (mesure) + LCD (affichage local) + HC-05 (affichage déporté)

---

*Fiche Cours Élève — BAC PRO CIEL | Module E2 | S15*
*Compétences : C2.1 – C3.1 – C3.2 – C4.1*
