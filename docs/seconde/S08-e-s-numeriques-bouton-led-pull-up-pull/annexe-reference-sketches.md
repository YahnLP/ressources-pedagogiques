# 📟 RÉFÉRENCE SKETCHES — S8 / Module E2
## Bibliothèque de code commenté · Bouton & LED · Pull-up/Pull-down · Débogage Serial

---

> **Document élève — À conserver dans le portfolio et réutiliser en S9, S10, S16**
> BAC Pro CIEL | S8 Module E2 | MFR de Pontonx

---

## 📌 Convention de code S8 — Règles supplémentaires à S7

| Règle nouvelle en S8 | Raison |
|---|---|
| **Variables d'état TOUJOURS globales** | Une variable dans `loop()` est réinitialisée à chaque cycle |
| **Nommer les états de façon lisible** | `bool ledAllumee = false` > `bool b = 0` |
| **Documenter la configuration de chaque broche** | Commentaire sur chaque `pinMode()` : mode + raison |
| **Indiquer la configuration pull-up/down dans l'en-tête** | Aide lors du recâblage ou du débogage |
| **Afficher l'état au démarrage dans Serial Monitor** | `Serial.println("Démarrage OK");` en fin de `setup()` |

---

## SKETCH 1 — Bouton → LED (pull-down externe)

```cpp
/*
 * TITRE   : Bouton vers LED — Pull-down externe
 * AUTEUR  : Exemple BAC Pro CIEL
 * MODULE  : S8 E2 — TP1
 * CÂBLAGE : Bouton D4 → 5V · R_PD 10kΩ entre D4 et GND
 *           LED D13 → R 220Ω → GND
 *
 * LOGIQUE : Pull-down → APPUYÉ = HIGH = 1 / RELÂCHÉ = LOW = 0
 */

// ── CONSTANTES ─────────────────────────────────────────────────
const int BROCHE_BTN = 4;   // Bouton avec pull-down externe 10kΩ
const int BROCHE_LED = 13;  // LED avec résistance 220Ω

// ── VARIABLES GLOBALES ─────────────────────────────────────────
int etatPrecedent = -1;     // Pour débogage conditionnel (valeur impossible au départ)

// ── SETUP ──────────────────────────────────────────────────────
void setup() {
  pinMode(BROCHE_BTN, INPUT);   // Entrée simple — pull-down EXTERNE requis
  pinMode(BROCHE_LED, OUTPUT);
  Serial.begin(9600);
  Serial.println("=== Bouton→LED (pull-down) démarré ===");
  Serial.println("RELÂCHÉ = 0  |  APPUYÉ = 1");
}

// ── LOOP ───────────────────────────────────────────────────────
void loop() {
  int etatActuel = digitalRead(BROCHE_BTN);

  // Contrôle de la LED
  if (etatActuel == 1) {              // Bouton appuyé (pull-down → HIGH)
    digitalWrite(BROCHE_LED, HIGH);
  } else {                            // Bouton relâché (pull-down → LOW)
    digitalWrite(BROCHE_LED, LOW);
  }

  // Débogage conditionnel (affiche seulement si changement)
  if (etatActuel != etatPrecedent) {
    Serial.print("Bouton D4 = ");
    Serial.println(etatActuel == 1 ? "APPUYÉ (1)" : "RELÂCHÉ (0)");
    etatPrecedent = etatActuel;
  }
}
```

---

## SKETCH 2 — Bouton → LED (INPUT_PULLUP interne)

```cpp
/*
 * TITRE   : Bouton vers LED — INPUT_PULLUP interne
 * AUTEUR  : Exemple BAC Pro CIEL
 * MODULE  : S8 E2 — TP2
 * CÂBLAGE : Bouton D4 → GND uniquement (pas de résistance externe !)
 *           LED D13 → R 220Ω → GND
 *
 * ⚠️ LOGIQUE INVERSÉE : RELÂCHÉ = HIGH = 1 / APPUYÉ = LOW = 0
 */

const int BROCHE_BTN = 4;
const int BROCHE_LED = 13;

int etatPrecedent = -1;

void setup() {
  pinMode(BROCHE_BTN, INPUT_PULLUP); // Pull-up INTERNE activé — pas de résistance externe !
  pinMode(BROCHE_LED, OUTPUT);
  Serial.begin(9600);
  Serial.println("=== Bouton→LED (INPUT_PULLUP) démarré ===");
  Serial.println("⚠ LOGIQUE INVERSÉE : RELÂCHÉ = 1  |  APPUYÉ = 0");
}

void loop() {
  int etatActuel = digitalRead(BROCHE_BTN);

  // ⚠️ Condition INVERSÉE par rapport au pull-down !
  if (etatActuel == 0) {             // Bouton appuyé (INPUT_PULLUP → LOW = 0)
    digitalWrite(BROCHE_LED, HIGH);
  } else {                           // Bouton relâché (INPUT_PULLUP → HIGH = 1)
    digitalWrite(BROCHE_LED, LOW);
  }

  // Débogage conditionnel
  if (etatActuel != etatPrecedent) {
    Serial.print("Bouton D4 = ");
    if (etatActuel == 0) {
      Serial.println("APPUYÉ (0) → LED allumée");
    } else {
      Serial.println("RELÂCHÉ (1) → LED éteinte");
    }
    etatPrecedent = etatActuel;
  }
}
```

---

## SKETCH 3 — Bascule (toggle) avec anti-rebond

```cpp
/*
 * TITRE   : Bascule LED — Un appui allume / appui suivant éteint
 * AUTEUR  : Exemple BAC Pro CIEL
 * MODULE  : S8 E2 — TP3
 * CÂBLAGE : Bouton D4 → GND (INPUT_PULLUP)
 *           LED D13 → R 220Ω → GND
 *
 * PRINCIPE : Détection du FRONT DESCENDANT (HIGH→LOW avec INPUT_PULLUP)
 *            = moment précis de l'appui sur le bouton.
 */

const int BROCHE_BTN     = 4;
const int BROCHE_LED     = 13;
const int DELAI_DEBOUNCE = 50;  // ms — anti-rebond

// ── VARIABLES GLOBALES (hors de loop() — OBLIGATOIRE) ──────────
bool etatLED      = false;  // État actuel de la LED
bool etatPrec     = HIGH;   // État précédent du bouton (INPUT_PULLUP → commence à HIGH)
int  compteurAppuis = 0;    // Pour le débogage : compte les appuis

void setup() {
  pinMode(BROCHE_BTN, INPUT_PULLUP);
  pinMode(BROCHE_LED, OUTPUT);
  digitalWrite(BROCHE_LED, etatLED);  // État initial de la LED
  Serial.begin(9600);
  Serial.println("=== Bascule LED démarrée ===");
  Serial.println("Chaque appui inverse l'état de la LED");
  Serial.print("État initial LED = ");
  Serial.println(etatLED ? "ALLUMÉE" : "ÉTEINTE");
}

void loop() {
  bool etatActuel = digitalRead(BROCHE_BTN);

  // Détecter le FRONT DESCENDANT : passage de HIGH (relâché) à LOW (appuyé)
  if (etatPrec == HIGH && etatActuel == LOW) {
    // Front détecté → anti-rebond
    delay(DELAI_DEBOUNCE);

    // Vérifier que le bouton est toujours appuyé (pas un faux rebond)
    if (digitalRead(BROCHE_BTN) == LOW) {
      // Basculer l'état de la LED
      etatLED = !etatLED;
      digitalWrite(BROCHE_LED, etatLED);

      compteurAppuis++;
      Serial.print("Appui n°"); Serial.print(compteurAppuis);
      Serial.print(" → LED = ");
      Serial.println(etatLED ? "ALLUMÉE" : "ÉTEINTE");
    }
  }

  etatPrec = etatActuel;  // Mémoriser pour le prochain cycle
}
```

---

## SKETCH 4 — TP4 Bugué (à distribuer aux apprenants)

> **Note formateur** : Distribuer ce sketch pour le TP4. Ne pas révéler les bugs avant que l'apprenant les trouve via le Serial Monitor.

```cpp
/*
 * TITRE   : Sketch TP4 — Trouver et corriger les 3 bugs
 * Ce sketch contient 3 bugs logiques. Utiliser le Serial Monitor
 * pour les identifier un par un.
 * CÂBLAGE : Bouton D4 (INPUT_PULLUP, câblé vers GND)
 *           LED D13 avec R 220Ω
 */

const int BROCHE_BTN = 4;
const int BROCHE_LED = 13;

void setup() {
  pinMode(BROCHE_BTN, INPUT_PULLUP);
  pinMode(BROCHE_LED, OUTPUT);
  Serial.begin(9600);
  Serial.println("Sketch TP4 — Débogage");
}

void loop() {
  // BUG 1 : variable d'état déclarée ICI (dans loop)
  bool etatLED = false;

  int etatBouton = digitalRead(BROCHE_BTN);

  // BUG 2 : condition incorrecte pour INPUT_PULLUP
  if (etatBouton == 1) {   // ← À déboguer avec Serial
    etatLED = !etatLED;
    digitalWrite(BROCHE_LED, etatLED);
    Serial.println("Bascule !");
    delay(50);
  }

  // BUG 3 : affichage permanent (sans condition de changement)
  // → inonde le Serial Monitor
  Serial.print("etat=");
  Serial.println(etatBouton);
}
```

> **Bugs à trouver :**
> 1. `bool etatLED` déclarée dans `loop()` → se réinitialise à `false` à chaque cycle → la bascule ne fonctionne pas
> 2. `etatBouton == 1` avec `INPUT_PULLUP` → la logique est inversée, il faut `== 0`
> 3. `Serial.println()` inconditionnel → inonde le Serial Monitor, masque les vrais messages

---

## SKETCH 5 — Défi avancé : Compteur d'appuis + clignotement conditionnel

```cpp
/*
 * TITRE   : Compteur d'appuis avec comportement LED
 * MODULE  : S8 E2 — Défi avancé
 *
 * COMPORTEMENT :
 *   1-4 appuis   : LED fixe allumée
 *   5-9 appuis   : LED clignote rapidement (200ms)
 *   10+ appuis   : LED clignote lentement (1s) + message "MAX atteint"
 *   Bouton appui LONG (>1s) : remet le compteur à zéro
 */

const int BROCHE_BTN = 4;
const int BROCHE_LED = 13;

int  compteur          = 0;
bool etatPrec          = HIGH;
unsigned long tDebut   = 0;   // Pour mesurer la durée d'appui

void setup() {
  pinMode(BROCHE_BTN, INPUT_PULLUP);
  pinMode(BROCHE_LED, OUTPUT);
  Serial.begin(9600);
  Serial.println("=== Compteur d'appuis ===");
  Serial.println("Appui long (>1s) = reset");
}

void loop() {
  bool etatActuel = digitalRead(BROCHE_BTN);

  // Détecter appui (front descendant)
  if (etatPrec == HIGH && etatActuel == LOW) {
    tDebut = millis();
    delay(50);  // Anti-rebond
  }

  // Détecter relâchement (front montant)
  if (etatPrec == LOW && etatActuel == HIGH) {
    unsigned long duree = millis() - tDebut;

    if (duree > 1000) {
      // Appui long → reset
      compteur = 0;
      Serial.println("RESET — Compteur remis à 0");
    } else {
      // Appui court → incrémenter
      compteur++;
      Serial.print("Compteur = ");
      Serial.println(compteur);
    }
    delay(50);
  }

  // Comportement LED selon le compteur
  if (compteur == 0) {
    digitalWrite(BROCHE_LED, LOW);        // Éteinte
  } else if (compteur < 5) {
    digitalWrite(BROCHE_LED, HIGH);       // Fixe allumée
  } else if (compteur < 10) {
    // Clignotement rapide (non bloquant simplifié)
    digitalWrite(BROCHE_LED, (millis() / 200) % 2);
  } else {
    // Clignotement lent + message
    bool etatCligno = (millis() / 1000) % 2;
    if (digitalRead(BROCHE_LED) != etatCligno) {
      digitalWrite(BROCHE_LED, etatCligno);
      if (etatCligno) Serial.println("MAX atteint — Appui long pour reset");
    }
  }

  etatPrec = etatActuel;
}
```

---

## 📋 Table de référence rapide — Fonctions S8

| Fonction | Syntaxe | Exemple |
|---|---|---|
| Configurer entrée simple | `pinMode(n, INPUT)` | `pinMode(4, INPUT);` |
| Configurer pull-up interne | `pinMode(n, INPUT_PULLUP)` | `pinMode(4, INPUT_PULLUP);` |
| Lire une entrée numérique | `digitalRead(n)` | `int e = digitalRead(4);` |
| Condition si appuyé (pull-down) | `if (digitalRead(n) == 1)` | — |
| Condition si appuyé (PULLUP) | `if (digitalRead(n) == 0)` | — |
| Inverser un booléen | `variable = !variable` | `etatLED = !etatLED;` |
| Temps écoulé depuis démarrage | `millis()` | `unsigned long t = millis();` |
| Débogage conditionnel | `if (etat != precedent)` | voir Sketch 1 |

---

## 🔌 Récapitulatif câblage — Vue d'ensemble

```
CONFIGURATION PULL-DOWN (logique naturelle)
─────────────────────────────────────────────
  D4 ─────────────┬───── [Bouton] ──── 5V
                  │
                [10kΩ]   ← Résistance pull-down
                  │
                 GND

  État relâché : D4 → GND via 10kΩ → digitalRead = 0
  État appuyé  : D4 → 5V via bouton → digitalRead = 1


CONFIGURATION INPUT_PULLUP (économique, logique inversée)
──────────────────────────────────────────────────────────
  D4 ── [~25kΩ interne] ── 5V    (résistance interne activée)
  D4 ──────────────────────────── [Bouton] ──── GND

  État relâché : D4 → 5V via résistance interne → digitalRead = 1
  État appuyé  : D4 → GND via bouton → digitalRead = 0
```

---

*Référence Sketches S8 — BAC Pro CIEL Module E2 | MFR de Pontonx*
