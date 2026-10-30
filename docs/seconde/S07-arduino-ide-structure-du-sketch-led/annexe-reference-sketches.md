# 📟 RÉFÉRENCE SKETCHES — S7 / Module E2
## Bibliothèque de code commenté · Arduino Uno · LED & Serial Monitor

---

> **Document élève — À conserver dans le portfolio et à réutiliser en S8, S9, S16**
> BAC Pro CIEL | S7 Module E2 | MFR de Pontonx

---

## 📌 Règles de style de code — À appliquer dès maintenant

Tout sketch remis en portfolio ou en évaluation doit respecter ces règles :

| Règle | Exemple correct | Exemple incorrect |
|---|---|---|
| **En-tête obligatoire** | `/* Titre, auteur, date, description */` | Pas d'en-tête |
| **Constantes nommées** | `const int BROCHE_LED = 13;` | `digitalWrite(13, HIGH);` directement |
| **Commentaire sur chaque bloc** | `// Séquence 1 : 3 flashs rapides` | Bloc sans explication |
| **Indentation cohérente** | 2 espaces ou 1 tabulation partout | Mélange aléatoire d'espaces |
| **Noms de variables explicites** | `int dureeRapide = 100;` | `int d = 100;` |
| **Aucun accent dans le code** | `// Allume la LED` | `// Allumé la LED` *(erreur de compilation)* |

---

## SKETCH 0 — Squelette vide (template de départ)

*Copier-coller ce template au début de chaque nouveau sketch.*

```cpp
/*
 * TITRE   : [Nom du programme]
 * AUTEUR  : [Votre Nom Prénom]
 * DATE    : [jj/mm/aaaa]
 * MODULE  : BAC Pro CIEL - E2 - S7
 * MATÉRIEL: Arduino Uno + [liste des composants]
 *
 * DESCRIPTION :
 * [Décrire en 2-3 phrases ce que fait ce programme]
 */

// ── CONSTANTES & VARIABLES GLOBALES ──────────────────────────────
const int BROCHE_LED = 13;   // Numéro de broche de la LED principale

// ── SETUP — Exécuté une seule fois au démarrage ───────────────────
void setup() {
  pinMode(BROCHE_LED, OUTPUT);  // Configurer la broche LED en sortie
  Serial.begin(9600);           // Démarrer la communication série
  Serial.println("[NOM DU PROGRAMME] démarré");
}

// ── LOOP — Exécuté en boucle infinie ─────────────────────────────
void loop() {
  // [Votre code ici]
}
```

---

## SKETCH 1 — Blink standard commenté

```cpp
/*
 * TITRE   : Blink standard
 * AUTEUR  : Exemple BAC Pro CIEL
 * MODULE  : S7 E2 — TP1
 *
 * DESCRIPTION : Allume et éteint la LED D13 à intervalles réguliers
 *               de 1 seconde. Sketch de base officiel Arduino.
 */

const int BROCHE_LED = 13;     // LED onboard ou LED externe sur D13
const int DUREE_ON   = 1000;   // Durée LED allumée en millisecondes
const int DUREE_OFF  = 1000;   // Durée LED éteinte en millisecondes

void setup() {
  pinMode(BROCHE_LED, OUTPUT);  // D13 en sortie
  Serial.begin(9600);
  Serial.println("Blink démarré — 1 Hz");
}

void loop() {
  // Phase ALLUMÉE
  digitalWrite(BROCHE_LED, HIGH);  // Allumer : mettre la broche à 5V
  Serial.println("LED : ON");
  delay(DUREE_ON);

  // Phase ÉTEINTE
  digitalWrite(BROCHE_LED, LOW);   // Éteindre : mettre la broche à 0V
  Serial.println("LED : OFF");
  delay(DUREE_OFF);
}
```

---

## SKETCH 2 — Blink rapide / lent alterné

```cpp
/*
 * TITRE   : Blink rapide/lent alterné
 * MODULE  : S7 E2 — TP2
 *
 * DESCRIPTION : 3 clignotements rapides suivis de 1 clignotement lent.
 *               Introduit la boucle for() et les variables.
 */

const int BROCHE_LED  = 13;
const int NB_RAPIDES  = 3;     // Nombre de flashs rapides par cycle
const int DUREE_RAPIDE = 150;  // ms pour le flash rapide
const int DUREE_LENT  = 1200;  // ms pour le flash lent
const int PAUSE_CYCLE = 500;   // ms de pause entre chaque cycle

int numeroCycle = 0;           // Compteur de cycles (incrémenté dans loop)

void setup() {
  pinMode(BROCHE_LED, OUTPUT);
  Serial.begin(9600);
  Serial.println("Blink rapide/lent - démarré");
}

void loop() {
  numeroCycle++;
  Serial.print("=== Cycle : ");
  Serial.println(numeroCycle);

  // ── Séquence 1 : NB_RAPIDES flashs rapides ──────────────────
  Serial.print("  Flashs rapides x");
  Serial.println(NB_RAPIDES);

  for (int i = 0; i < NB_RAPIDES; i++) {
    digitalWrite(BROCHE_LED, HIGH);
    delay(DUREE_RAPIDE);
    digitalWrite(BROCHE_LED, LOW);
    delay(DUREE_RAPIDE);
  }

  // ── Séquence 2 : 1 flash lent ───────────────────────────────
  Serial.println("  Flash lent x1");
  digitalWrite(BROCHE_LED, HIGH);
  delay(DUREE_LENT);
  digitalWrite(BROCHE_LED, LOW);
  delay(DUREE_LENT);

  // ── Pause inter-cycle ───────────────────────────────────────
  Serial.println("  [pause]");
  delay(PAUSE_CYCLE);
}
```

---

## SKETCH 3 — LED rythmée libre (template TP3)

*Ce sketch sert de base pour le TP3. L'apprenant personnalise les durées et le nombre de séquences.*

```cpp
/*
 * TITRE   : LED Rythmée Personnalisée
 * AUTEUR  : [Votre Nom Prénom]
 * DATE    : [jj/mm/aaaa]
 * MODULE  : BAC Pro CIEL - E2 - S7 - TP3
 *
 * DESCRIPTION : Sketch original avec au moins 3 rythmes différents
 *               et messages Serial Monitor sur chaque état.
 *               Critère : au moins 3 durées de delay() distinctes.
 */

const int BROCHE_LED = 13;

// ── DURÉES PERSONNALISÉES ─────────────────────────────────────────
// CONSIGNE : Modifier ces valeurs pour créer votre propre rythme
const int DUREE_1 = 80;    // [À modifier] Durée séquence 1 (ms)
const int DUREE_2 = 400;   // [À modifier] Durée séquence 2 (ms)
const int DUREE_3 = 1800;  // [À modifier] Durée séquence 3 (ms)
const int PAUSE   = 700;   // [À modifier] Pause entre séquences (ms)

int cycle = 0;

void setup() {
  pinMode(BROCHE_LED, OUTPUT);
  Serial.begin(9600);
  Serial.println("=== LED Rythmée personnalisée ===");
  Serial.print("Durées : ");
  Serial.print(DUREE_1); Serial.print("ms / ");
  Serial.print(DUREE_2); Serial.print("ms / ");
  Serial.print(DUREE_3); Serial.println("ms");
}

void loop() {
  cycle++;
  Serial.print("\n--- Cycle "); Serial.print(cycle); Serial.println(" ---");

  // ── SÉQUENCE 1 ─────────────────────────────────────────────────
  // [Décrire ici ce que cette séquence représente]
  Serial.println("Seq 1 : [votre description]");
  // [Votre code de séquence 1]

  // ── SÉQUENCE 2 ─────────────────────────────────────────────────
  Serial.println("Seq 2 : [votre description]");
  // [Votre code de séquence 2]

  // ── SÉQUENCE 3 ─────────────────────────────────────────────────
  Serial.println("Seq 3 : [votre description]");
  // [Votre code de séquence 3]

  // ── PAUSE INTER-CYCLE ──────────────────────────────────────────
  delay(PAUSE);
}
```

---

## SKETCH 4 — SOS en Morse (défi avancé)

```cpp
/*
 * TITRE   : SOS en code Morse
 * MODULE  : S7 E2 — Défi avancé
 *
 * DESCRIPTION : Émet SOS en morse ( · · · — — — · · · )
 *               avec messages Serial Monitor synchronisés.
 *
 * CODE MORSE :
 *   S = · · ·  (trois points)   — flash court × 3
 *   O = — — —  (trois tirets)   — flash long  × 3
 *   Séparation entre lettres = 3 × durée_point (silence)
 */

const int BROCHE_LED = 13;
const int POINT   = 200;   // Durée d'un point en ms
const int TIRET   = 600;   // Durée d'un tiret = 3 × point
const int GAP_SYM = 200;   // Silence entre symboles = 1 × point
const int GAP_LET = 600;   // Silence entre lettres = 3 × points
const int GAP_MOT = 1400;  // Silence entre mots = 7 × points

// ── Fonctions utilitaires ─────────────────────────────────────────

void flashPoint() {
  Serial.print("·");
  digitalWrite(BROCHE_LED, HIGH); delay(POINT);
  digitalWrite(BROCHE_LED, LOW);  delay(GAP_SYM);
}

void flashTiret() {
  Serial.print("—");
  digitalWrite(BROCHE_LED, HIGH); delay(TIRET);
  digitalWrite(BROCHE_LED, LOW);  delay(GAP_SYM);
}

void lettre(String nom) {
  Serial.print(" "); Serial.print(nom); Serial.print("(");
}

// ── SETUP ─────────────────────────────────────────────────────────
void setup() {
  pinMode(BROCHE_LED, OUTPUT);
  Serial.begin(9600);
  Serial.println("SOS Morse démarré");
}

// ── LOOP ──────────────────────────────────────────────────────────
void loop() {
  Serial.print("Émission : ");

  // S = · · ·
  lettre("S"); flashPoint(); flashPoint(); flashPoint();
  Serial.print(") ");
  delay(GAP_LET);

  // O = — — —
  lettre("O"); flashTiret(); flashTiret(); flashTiret();
  Serial.print(") ");
  delay(GAP_LET);

  // S = · · ·
  lettre("S"); flashPoint(); flashPoint(); flashPoint();
  Serial.println(")");

  // Pause entre les répétitions du mot SOS
  delay(GAP_MOT);
}
```

---

## 📋 Table de référence rapide — Fonctions Arduino S7

| Fonction | Syntaxe complète | Exemple concret |
|---|---|---|
| Configurer broche | `pinMode(n, MODE)` | `pinMode(13, OUTPUT);` |
| Écrire état digital | `digitalWrite(n, ETAT)` | `digitalWrite(13, HIGH);` |
| Attendre | `delay(ms)` | `delay(500);` |
| Initialiser série | `Serial.begin(vitesse)` | `Serial.begin(9600);` |
| Envoyer texte | `Serial.print("texte")` | `Serial.print("LED ON");` |
| Envoyer texte + newline | `Serial.println("texte")` | `Serial.println("OK");` |
| Envoyer nombre | `Serial.println(variable)` | `Serial.println(cycle);` |
| Boucle comptée | `for(int i=0; i<N; i++)` | `for(int i=0; i<3; i++)` |

---

## 🔌 Table de câblage LED externe — Valeurs E24 selon V_alim et V_F

| V_alim Arduino | V_F LED | I_F cible | R calculée | R E24 choisie |
|---|---|---|---|---|
| 5 V | 2,0 V (rouge/jaune) | 20 mA | 150 Ω | **150 Ω** |
| 5 V | 2,0 V (rouge/jaune) | 15 mA | 200 Ω | **220 Ω** *(valeur usuelle)* |
| 5 V | 2,1 V (verte) | 20 mA | 145 Ω | **150 Ω** |
| 5 V | 3,3 V (bleue/blanche) | 20 mA | 85 Ω | **82 Ω** |
| 3,3 V | 2,0 V (rouge) | 20 mA | 65 Ω | **68 Ω** |

> 💡 **En pratique** : Utiliser **220 Ω** pour toute LED rouge/verte sur Arduino 5V est une valeur sûre et universelle dans les kits de formation. Elle donne I_F ≈ 13–15 mA, ce qui est visible et protège la broche.

---

## 🧮 Convertisseur delay() ↔ fréquence

| delay() × 2 (ON+OFF) | Période totale | Fréquence | Perception visuelle |
|---|---|---|---|
| 2 × 25 ms | 50 ms | 20 Hz | Quasi-fixe (fusion) |
| 2 × 50 ms | 100 ms | 10 Hz | Légèrement instable |
| 2 × 100 ms | 200 ms | 5 Hz | Clignotement rapide visible |
| 2 × 250 ms | 500 ms | 2 Hz | Clignotement net |
| 2 × 500 ms | 1000 ms | **1 Hz** | Blink standard (1/sec) |
| 2 × 1000 ms | 2000 ms | 0,5 Hz | Clignotement lent |
| 2 × 2000 ms | 4000 ms | 0,25 Hz | Très lent |

> 📌 `f (Hz) = 1 / T (secondes)` · `T (ms) = 2 × delay()` si durée ON = durée OFF

---

*Référence Sketches S7 — BAC Pro CIEL Module E2 | MFR de Pontonx*
*Fichiers .ino disponibles dans le dossier partagé de classe*
