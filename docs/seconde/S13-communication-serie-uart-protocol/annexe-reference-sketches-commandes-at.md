# 📟 RÉFÉRENCE SKETCHES & COMMANDES AT — S13 / Module E2
## Bibliothèque UART · Serial Monitor avancé · HC-05 Bluetooth

---

> **Document élève — À conserver dans le portfolio et réutiliser en S14, S16**

---

## 📌 Règles de style supplémentaires S13

| Règle | Raison |
|---|---|
| **Toujours appeler `.trim()`** après `readStringUntil()` | Élimine les `\r` invisibles sur Windows (CRLF) qui cassent les comparaisons |
| **Toujours vérifier `Serial.available()`** avant de lire | Évite les lectures bloquantes sur tampon vide |
| **Documenter le baud rate en en-tête** | Un sketch sans baud rate documenté est impossible à déboguer à froid |
| **Préfixer les messages Serial** | `[OK]`, `[ERR]`, `[INFO]`, `[DATA]` → lisibilité en débogage |
| **Séparer port matériel et port logiciel** | `Serial` = USB/PC · `btSerial` = HC-05 → ne jamais mélanger |

---

## SKETCH 1 — Écho série (TP1)

```cpp
/*
 * TITRE   : Écho série
 * MODULE  : S13 E2 — TP1
 * BAUD    : 9600
 * CÂBLAGE : Arduino Uno seul (pas de module externe)
 *
 * DESCRIPTION : Renvoie exactement ce qui est reçu depuis le Serial Monitor.
 *               Permet de tester la liaison UART et l'effet du baud rate.
 */

void setup() {
  Serial.begin(9600);
  Serial.println("=== ECHO SERIE démarré — tout ce que tu envoies revient ===");
  Serial.print("Baud rate : ");
  Serial.println(9600);
}

void loop() {
  if (Serial.available() > 0) {
    char c = Serial.read();       // Lire 1 caractère
    Serial.write(c);              // Renvoyer le même caractère (pas print)
  }
}
```

> 📌 `Serial.write(c)` envoie l'octet brut (le caractère lui-même). `Serial.print(c)` affiche aussi le caractère, mais `Serial.print(65)` affiche "65" alors que `Serial.write(65)` envoie le caractère 'A' (code ASCII 65). En écho, toujours utiliser `write()`.

---

## SKETCH 2 — Interpréteur de commandes texte (TP2)

```cpp
/*
 * TITRE   : Interpréteur de commandes texte
 * MODULE  : S13 E2 — TP2
 * BAUD    : 9600
 * NEWLINE : Régler "Newline" dans le Serial Monitor (pas "No line ending")
 *
 * COMMANDES : LED_ON / LED_OFF / STATUS / HELP
 */

const int BROCHE_LED = 13;
String commande      = "";

void setup() {
  pinMode(BROCHE_LED, OUTPUT);
  Serial.begin(9600);
  Serial.println("=== Interpréteur de commandes S13 ===");
  Serial.println("Commandes : LED_ON | LED_OFF | STATUS | HELP");
}

void loop() {
  if (Serial.available() > 0) {
    commande = Serial.readStringUntil('\n');   // Lire jusqu'au saut de ligne
    commande.trim();    // ← ESSENTIEL : supprime \r et espaces résiduels

    // ── Traitement des commandes ──────────────────────────────────
    if (commande == "LED_ON") {
      digitalWrite(BROCHE_LED, HIGH);
      Serial.println("[OK] LED allumée");

    } else if (commande == "LED_OFF") {
      digitalWrite(BROCHE_LED, LOW);
      Serial.println("[OK] LED éteinte");

    } else if (commande == "STATUS") {
      Serial.print("[INFO] LED = ");
      Serial.println(digitalRead(BROCHE_LED) ? "ON" : "OFF");
      Serial.print("[INFO] Uptime = ");
      Serial.print(millis() / 1000);
      Serial.println("s");

    } else if (commande == "HELP") {
      Serial.println("[HELP] Commandes disponibles :");
      Serial.println("  LED_ON   → allumer LED D13");
      Serial.println("  LED_OFF  → éteindre LED D13");
      Serial.println("  STATUS   → état actuel");
      Serial.println("  HELP     → cette aide");

    } else if (commande.length() > 0) {   // Ignorer les lignes vides
      Serial.print("[ERR] Commande inconnue : '");
      Serial.print(commande);
      Serial.println("'");
      Serial.println("[ERR] Taper HELP pour la liste");
    }

    commande = "";  // Réinitialiser
  }
}
```

---

## SKETCH 3 — Parser numérique + contrôle PWM (TP3)

```cpp
/*
 * TITRE   : Parser numérique + PWM
 * MODULE  : S13 E2 — TP3
 * BAUD    : 9600
 * CÂBLAGE : LED sur D9 (broche PWM ~) avec R=220Ω
 *
 * UTILISATION : Envoyer un nombre 0-255 dans le Serial Monitor
 *               La luminosité de la LED change en proportion.
 */

const int LED_PWM    = 9;     // Broche PWM obligatoirement (~)
int luminosite       = 0;
int derniereValeur   = -1;    // Pour débogage conditionnel

void setup() {
  pinMode(LED_PWM, OUTPUT);
  Serial.begin(9600);
  Serial.println("=== Contrôle PWM via Serial ===");
  Serial.println("Envoyer un entier 0-255 (0=éteint, 255=max)");
}

void loop() {
  if (Serial.available() > 0) {
    luminosite = Serial.parseInt();          // Lire l'entier
    luminosite = constrain(luminosite, 0, 255);   // Borner 0-255
    analogWrite(LED_PWM, luminosite);

    // Affichage conditionnel (seulement si changement)
    if (luminosite != derniereValeur) {
      Serial.print("[PWM] ");
      Serial.print(luminosite);
      Serial.print("/255 → ");
      Serial.print(luminosite * 100 / 255);
      Serial.print("% luminosité");

      // Indicateur visuel texte
      if      (luminosite == 0)   Serial.println("  ○ ÉTEINT");
      else if (luminosite < 85)   Serial.println("  ◔ FAIBLE");
      else if (luminosite < 170)  Serial.println("  ◑ MOYEN");
      else if (luminosite < 255)  Serial.println("  ◕ FORT");
      else                        Serial.println("  ● MAXIMUM");

      derniereValeur = luminosite;
    }

    // Vider le reste du tampon (évite les lectures parasites)
    while (Serial.available()) Serial.read();
  }
}
```

---

## SKETCH 4 — Passerelle Serial ↔ HC-05 (TP4 — mode AT)

```cpp
/*
 * TITRE   : Passerelle Serial Monitor ↔ HC-05 Bluetooth
 * MODULE  : S13 E2 — TP4
 * BAUD SERIE : 9600 (USB ↔ PC)
 * BAUD BT    : 38400 (mode AT du HC-05)
 *
 * CÂBLAGE HC-05 :
 *   VCC  → 5V Arduino
 *   GND  → GND Arduino
 *   TXD  → D10 (RX SoftwareSerial)
 *   RXD  → D11 via diviseur 1kΩ/2kΩ → 3,33V
 *   KEY  → 3,3 V (force le mode AT)
 *
 * UTILISATION :
 *   Ouvrir le Serial Monitor à 9600 bauds + "Both NL & CR"
 *   Taper une commande AT → elle est relayée au HC-05
 *   La réponse du HC-05 s'affiche dans le Serial Monitor
 */

#include <SoftwareSerial.h>

// D10 = RX SoftwareSerial (reçoit depuis TXD du HC-05)
// D11 = TX SoftwareSerial (envoie vers RXD du HC-05 via diviseur)
SoftwareSerial btSerial(10, 11);

void setup() {
  Serial.begin(9600);       // Liaison USB ↔ PC
  btSerial.begin(38400);    // Liaison Arduino ↔ HC-05 en mode AT

  Serial.println("=== Passerelle HC-05 — Mode AT ===");
  Serial.println("Vérifier : KEY du HC-05 est relié au 3,3 V à la mise sous tension");
  Serial.println("Régler Serial Monitor sur 'Both NL & CR'");
  Serial.println("Taper 'AT' et appuyer Entrée → doit répondre 'OK'");
}

void loop() {
  // PC → HC-05 : relayer ce qui vient du Serial Monitor vers le HC-05
  if (Serial.available()) {
    char c = Serial.read();
    btSerial.write(c);
  }

  // HC-05 → PC : relayer la réponse du HC-05 vers le Serial Monitor
  if (btSerial.available()) {
    char c = btSerial.read();
    Serial.write(c);
  }
}
```

---

## SKETCH 5 — Débogage Bluetooth bidirectionnel (préparation S14)

```cpp
/*
 * TITRE   : Communication Bluetooth bidirectionnelle avec débogage
 * MODULE  : S13 E2 — Défi avancé / Préparation S14
 * BAUD SERIE : 9600 (USB ↔ PC)
 * BAUD BT    : 9600 (HC-05 en mode communication normale)
 *
 * DESCRIPTION : Après configuration AT (baud = 9600, nom modifié),
 *               l'Arduino reçoit des commandes via Bluetooth (smartphone)
 *               et les affiche dans le Serial Monitor pour débogage.
 *               Répond également aux commandes.
 */

#include <SoftwareSerial.h>
SoftwareSerial btSerial(10, 11);

String cmdBT  = "";
int compteurRx = 0;

void setup() {
  pinMode(13, OUTPUT);
  Serial.begin(9600);
  btSerial.begin(9600);    // Après configuration AT → baud = 9600

  Serial.println("=== Débogage Bluetooth bidirectionnel ===");
  Serial.println("[SYS] En attente de connexion Bluetooth...");
}

void loop() {
  // ── Réception depuis Bluetooth ─────────────────────────────────
  if (btSerial.available() > 0) {
    cmdBT = btSerial.readStringUntil('\n');
    cmdBT.trim();
    compteurRx++;

    // Débogage : afficher la trame reçue dans le Serial Monitor
    Serial.print("[BT RX #"); Serial.print(compteurRx);
    Serial.print("] Reçu : '"); Serial.print(cmdBT);
    Serial.print("' ("); Serial.print(cmdBT.length());
    Serial.println(" octets)");

    // Traitement de la commande
    if (cmdBT == "ON") {
      digitalWrite(13, HIGH);
      btSerial.println("[OK] LED allumée");
      Serial.println("[BT TX] Réponse envoyée : LED allumée");

    } else if (cmdBT == "OFF") {
      digitalWrite(13, LOW);
      btSerial.println("[OK] LED éteinte");
      Serial.println("[BT TX] Réponse envoyée : LED éteinte");

    } else {
      btSerial.print("[ERR] Inconnu : ");
      btSerial.println(cmdBT);
      Serial.println("[BT TX] Erreur renvoyée");
    }
  }

  // ── Émission depuis le Serial Monitor vers Bluetooth ───────────
  if (Serial.available() > 0) {
    String msgPC = Serial.readStringUntil('\n');
    msgPC.trim();
    btSerial.println(msgPC);
    Serial.print("[PC→BT] Envoyé : '");
    Serial.print(msgPC);
    Serial.println("'");
  }
}
```

---

## 📋 Table de référence AT complète — HC-05

### Syntaxe des commandes AT

```
Format de commande  : AT+<COMMANDE>[=<valeur>]<CR><LF>
Format de requête   : AT+<COMMANDE>?<CR><LF>
Format de réponse   : +<COMMANDE>:<valeur>\r\n  puis  OK\r\n
```

??? success "Réponse"
    d'erreur    : ERROR:(code)\r\n

### Commandes essentielles

| Commande | Type | Format | Exemple de réponse |
|---|---|---|---|
| `AT` | Test | — | `OK` |
| `AT+VERSION?` | Requête | — | `+VERSION:2.0-20100601` |
| `AT+RESET` | Action | — | `OK` puis redémarrage |
| `AT+NAME?` | Requête | — | `+NAME:HC-05` |
| `AT+NAME=<nom>` | Config | Max 32 chars | `OK` |
| `AT+PSWD?` | Requête | — | `+PSWD:1234` |
| `AT+PSWD=<code>` | Config | 4-8 chiffres | `OK` |
| `AT+ROLE?` | Requête | — | `+ROLE:0` |
| `AT+ROLE=0` | Config | 0=esclave | `OK` |
| `AT+ROLE=1` | Config | 1=maître | `OK` |
| `AT+ADDR?` | Requête | — | `+ADDR:98d3:31:f90xxx` |
| `AT+UART?` | Requête | — | `+UART:9600,0,0` |
| `AT+UART=<baud>,<stop>,<parity>` | Config | ex: `AT+UART=9600,0,0` | `OK` |

### Codes baud rate HC-05

| Code | Baud rate | Usage recommandé |
|---|---|---|
| 1 | 1200 | Très lent, cas spécifiques |
| 2 | 2400 | — |
| 3 | 4800 | — |
| **4** | **9600** | **Standard — utiliser pour S14** |
| 5 | 19200 | — |
| **6** | **38400** | **Mode AT par défaut** |
| 7 | 57600 | — |
| **8** | **115200** | **Haut débit (streaming)** |

### LED de statut HC-05

| Clignotement | Signification |
|---|---|
| Très rapide (∼100ms) | Module sous tension, non appairé |
| Lent (∼2s) | Appairé et connecté |
| Double flash puis pause | En attente de connexion |
| Fixe | Mode AT actif |

---

## 🔌 Schémas de câblage ASCII

### Configuration TP4 — Arduino + HC-05 mode AT

```
Arduino Uno          Breadboard          HC-05
                                         ┌─────────┐
5V ──────────────────────────────────── VCC (3,3-5V)
GND ────────────────────────────────── GND
                                         │
D11 (TX) ── [1kΩ] ─── nœud ─── [2kΩ] ─ RXD (3.3V MAX)
                                 │
                               GND

D10 (RX) ─────────────────────────── TXD
3,3V ──────────────────────────────── KEY  (mode AT)
                                         └─────────┘

         DIVISEUR : V_out = 5V × 2kΩ/(1kΩ+2kΩ) = 3.33V ✓
```

### Configuration S14 — Communication Bluetooth normale

```
Arduino Uno          Breadboard          HC-05
                                         ┌─────────┐
5V ─────────────────────────────────── VCC
GND ───────────────────────────────── GND
                                         │
D11 (TX) ── [1kΩ] ─── nœud ─── [2kΩ] ─ RXD
                                 │
                               GND

D10 (RX) ──────────────────────────── TXD
NC ────────────────────────────────── KEY  (NON relié → mode communication)
                                         └─────────┘

Note : En mode communication normale, KEY doit être LIBRE (non relié au 3,3 V)
       HC-05 baud rate doit correspondre à btSerial.begin(X)
```

---

*Référence Sketches & Commandes AT S13 — BAC Pro CIEL Module E2 | MFR de Pontonx*
