# ✏️ FICHE GABARIT — SCHÉMA ÉLECTRONIQUE DU SYSTÈME DOMOTIQUE A1
## À compléter lors du TP · Document officiel du dossier Portfolio E5

---

> **Nom de l'apprenant** : ___________________________
> **Binôme** : ___________________________
> **Date** : ___________________________
> **Version du schéma** : V _____ &nbsp;&nbsp; **Outil utilisé** : ☐ Fritzing &nbsp; ☐ KiCad &nbsp; ☐ Papier/crayon numérisé

---

## 📋 ÉTAPE 1 — Inventaire des composants avant de tracer

Avant de commencer le schéma, liste tous les composants de ton système domotique :

| Réf Schéma | Désignation | Valeur / Type | Rôle dans le système |
|---|---|---|---|
| **U1** | Microcontrôleur | Arduino UNO (ATmega328P) | Unité centrale de traitement |
| **DHT1** | Capteur T°/Humidité | DHT11 | Mesure température et humidité |
| **R1** | Résistance pull-up DHT | 10 kΩ – 1/4W | Maintien niveau logique DATA |
| **LCD1** | Écran LCD I2C | LCD 16×2 + PCF8574 | Affichage local |
| **BT1** | Module Bluetooth | HC-05 | Transmission sans fil |
| **R2** | Résistance pont diviseur | 1 kΩ – 1/4W | Pont div. tension RXD HC-05 |
| **R3** | Résistance pont diviseur | 2 kΩ – 1/4W | Pont div. tension RXD HC-05 |

**Vérification :**
- Nombre total de composants : _____
- Nombre de points GND : _____ (ils doivent tous être reliés)
- Nombre de points +5V : _____ (ils doivent tous être reliés)

---

## ✏️ ÉTAPE 2 — Zone de schéma

> **Instructions** :
> - Si tu utilises **Fritzing ou KiCad** : exporte en PNG/PDF et colle la capture ici (ou joins le fichier)
> - Si tu dessines **à la main** : utilise les conventions ci-dessous, puis numérise ou scanne le schéma

### Conventions de représentation à respecter

| Composant | Représentation | Notes |
|---|---|---|
| **Arduino UNO** | Rectangle avec broches étiquetées | Indiquer le numéro de chaque broche utilisée |
| **DHT11** | Rectangle avec broches VCC/DATA/GND | Indiquer la broche Arduino connectée à DATA |
| **R1 (pull-up)** | Symbole résistance (rectangle IEC) | Entre VCC et DATA du DHT11 |
| **LCD I2C** | Rectangle avec VCC/GND/SDA/SCL | Indiquer A4 et A5 côté Arduino |
| **HC-05** | Rectangle avec VCC/GND/TXD/RXD | Indiquer le pont diviseur sur RXD |
| **R2, R3** | Symboles résistances en série | Valeurs indiquées, point milieu vers RXD |
| **Fils +5V** | Ligne horizontale en haut avec étiquette +5V | Tous les VCC y sont reliés |
| **Fils GND** | Ligne horizontale en bas avec symbole ⏚ | Tous les GND y sont reliés |

---

> [!NOTE] ✏️ À toi de dessiner
> Dessine ton schéma sur ta feuille ou dans ton dossier (zone prévue pour le schéma).

---

## 📏 ÉTAPE 3 — Table de câblage officielle

*(Compléter en parallèle du schéma — doit être cohérente avec le schéma)*

### Liaisons DHT11

| Broche DHT11 | Via | Broche Arduino / Connexion |
|---|---|---|
| VCC (1) | Fil direct | +5V Arduino |
| DATA (2) | Fil direct | Pin ___ Arduino |
| DATA (2) | Via R1 (10kΩ) | +5V (pull-up) |
| NC (3) | — | Non connectée |
| GND (4) | Fil direct | GND Arduino |

### Liaisons LCD I2C

| Broche LCD I2C | Via | Broche Arduino |
|---|---|---|
| VCC | Fil direct | +5V Arduino |
| GND | Fil direct | GND Arduino |
| SDA | Fil direct | **A4** Arduino |
| SCL | Fil direct | **A5** Arduino |

### Liaisons HC-05

| Broche HC-05 | Via | Broche Arduino |
|---|---|---|
| VCC | Fil direct | +5V Arduino |
| GND | Fil direct | GND Arduino |
| TXD | Fil direct | Pin **10** Arduino |
| RXD | Via R2(1kΩ)→nœud→R3(2kΩ)→GND | Pin **11** Arduino |

**Vérification du pont diviseur :**

```
Calcul : V_RXD = 5V × R3 / (R2 + R3) = 5 × 2000 / 3000 = ___ V
Valeur attendue : 3,33 V ✅
```

---

## 🔍 ÉTAPE 4 — Auto-vérification du schéma

Avant de rendre, coche chaque point :

| Critère de vérification | ☐ OK | ☐ À corriger |
|---|---|---|
| Tous les composants ont une référence (U1, DHT1, R1, R2, R3, LCD1, BT1) | | |
| Toutes les résistances ont leur valeur indiquée | | |
| La résistance pull-up R1 est bien entre VCC et DATA du DHT11 | | |
| Le pont diviseur R2+R3 est bien sur la broche RXD du HC-05 | | |
| Les broches SDA (A4) et SCL (A5) sont correctement reliées au LCD | | |
| Toutes les lignes GND sont reliées entre elles | | |
| Toutes les lignes +5V sont reliées entre elles | | |
| Le cartouche est présent et complet | | |
| Le schéma est lisible sans ambiguïté | | |
| La table de câblage est cohérente avec le schéma | | |

**Score de vérification** : ___ / 10 cases cochées ✅

---

## 🗂️ CARTOUCHE OFFICIEL

*(À remplir et reporter sur le schéma)*

| Champ | Valeur |
|---|---|
| **Titre** | Station Domotique Connectée – Projet A1 |
| **Auteur(s)** | |
| **Date** | |
| **Établissement** | |
| **Version** | V 1.0 |
| **Indice de révision** | A |
| **Feuille** | 1 / 1 |

---

## ✅ Validation enseignant

| Critère | Note /5 | Commentaire |
|---|---|---|
| Composants complets et référencés | | |
| Connexions correctes et cohérentes | | |
| Résistances avec valeurs | | |
| Pont diviseur et pull-up présents | | |
| Cartouche complet | | |
| **TOTAL** | **/25** | |

**Signature enseignant** : ___________________________ **Date** : ___________

---

*Fiche Gabarit Schéma Électronique — BAC PRO CIEL | Module E2 | S16*
*Pièce obligatoire du Portfolio E5 — Compétences C4.1 – C1.2*
