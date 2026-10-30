# 📖 FICHE COURS – S5 ANNÉE 2 – E2
## Tests & Mesures Avancés : Oscilloscope Mixte, Analyseur Logique, I2C / SPI

**Nom : ________________  Prénom : ________________**

---

## 🎯 OBJECTIFS

- ✅ Configurer un oscilloscope mixte (MSO) pour des signaux numériques + analogiques
- ✅ Connecter et utiliser un analyseur logique USB
- ✅ Décoder une trame I2C et identifier ses champs
- ✅ Décoder une trame SPI et identifier MOSI, MISO, SCLK, CS
- ✅ Diagnostiquer un problème de bus à partir de la capture

---

## 1️⃣ OSCILLOSCOPE : DSO VS MSO

### Types d'oscilloscopes numériques

| **Type** | **Voies** | **Usage** | **Exemple** |
|---|---|---|---|
| **DSO** (Digital Storage Oscilloscope) | 2–4 voies analogiques | Signaux analogiques, formes d'ondes | Rigol DS1054Z |
| **MSO** (Mixed Signal Oscilloscope) | 2–4 voies analogiques **+ 8–16 voies numériques** | Signaux mixtes : analogique + bus numériques | Rigol MSO5072, Keysight MSOX3024T |

### Ce que les voies numériques du MSO apportent

```
Voies analogiques (CH1, CH2…) :
  → Tension réelle (mV à kV), forme d'onde précise
  → Mesures : amplitude, fréquence, phase, overshoot

Voies numériques (D0–D15) :
  → Seulement HIGH (1) ou LOW (0) — pas de valeur précise
  → Affichage en chronogramme sous les voies analogiques
  → Décodage de protocoles intégré (I2C, SPI, UART, CAN…)
```

### Quand utiliser MSO vs Analyseur logique ?

| **Situation** | **Outil recommandé** |
|---|---|
| Mesurer la tension exacte d'un signal I2C | MSO (voie analogique) |
| Décoder un bus I2C avec 16 esclaves | Analyseur logique (plus de voies, meilleure résolution temporelle) |
| Observer un glitch analogique sur SCL + décoder la trame | MSO (les deux en même temps) |
| Débogguer un protocole dans un PC en labo USB | Analyseur logique USB (Saleae, économique) |

---

## 2️⃣ ANALYSEUR LOGIQUE USB

### Principe

> Un **analyseur logique** est un instrument qui capture des signaux numériques (HIGH/LOW) sur plusieurs voies simultanément à très haute fréquence d'échantillonnage, les enregistre dans sa mémoire, et les affiche comme un chronogramme. Les décodeurs de protocoles intégrés permettent de passer automatiquement du niveau binaire au niveau "message" (adresse I2C, données SPI…).

### Connexion physique

```
Analyseur logique USB
   │
   ├── CH0 → Signal 1 (ex: SCL)
   ├── CH1 → Signal 2 (ex: SDA)
   ├── CH2 → Signal 3 (ex: SCLK SPI)
   ├── ...
   └── GND → Masse du circuit (OBLIGATOIRE)

                        ⚠️ GND TOUJOURS CONNECTÉ EN PREMIER
```

### Saleae Logic 2 — Interface

```
┌────────────────────────────────────────────────────────────────┐
│  BARRE D'OUTILS  Start / Stop / Fréquence échantillonnage      │
├─────────────────────────────────────────────────────────────────┤
│  CH0 ────────────────────┐────────────────────────────────────  │
│  (SCL)                   │                                      │
│  CH1 ──────────┐─────────┘────────────────────────────────────  │
│  (SDA)         │                                                 │
│                └──────────── Trame décodée : [0x68 W][ACK]...   │
├─────────────────────────────────────────────────────────────────┤
│  PANNEAU ANALYSEURS   I2C / SPI / UART / 1-Wire / ...          │
└────────────────────────────────────────────────────────────────┘
```

### Fréquence d'échantillonnage — Règle de Nyquist

$$\boxed{f_{éch} \geq 10 \times f_{bus}}$$

| **Protocole** | **Fréquence bus typique** | **Fréquence échantillonnage minimale** |
|---|---|---|
| I2C standard | 100 kHz | 1 MHz |
| I2C fast mode | 400 kHz | 4 MHz (recommandé : 8 MHz) |
| SPI courant | 1–10 MHz | 10–100 MHz |
| UART 115200 baud | 115,2 kHz | 1 MHz |

---

## 3️⃣ DÉCODAGE I2C

### Rappel du protocole I2C

> I2C (Inter-Integrated Circuit) utilise **2 fils** : SCL (horloge) et SDA (données). Toutes les lignes sont en **collecteur ouvert** avec des résistances de pull-up.

### Structure d'une trame I2C

```
Chronogramme :

SCL  ____┐ ┌─┐ ┌─┐ ┌─┐ ┌─┐ ┌─┐ ┌─┐ ┌─┐ ┌─┐ ┌─...
         │ │ │ │ │ │ │ │ │ │ │ │ │ │ │ │ │ │ │
     ────┘ └─┘ └─┘ └─┘ └─┘ └─┘ └─┘ └─┘ └─┘ └─...
          │←──────── 8 bits adresse+RW ────────→│← ACK →│

SDA  ─┐  ┌─────────────────────...─────────────┐ ┌───────
      │  │  A6  A5  A4  A3  A2  A1  A0   R/W   │ │  ACK
      └──┘                                      └─┘
     START                                      ↑ 9ème coup horloge
     condition                             SDA=0 (ACK) ou SDA=1 (NACK)
```

### Champs d'une trame I2C lus dans Saleae

| **Champ** | **Contenu** | **Exemple** |
|---|---|---|
| **START** | Front descendant SDA quand SCL=HIGH | Carré vert `S` dans Saleae |
| **ADRESSE** | 7 bits — identifie l'esclave | `0x68` (MPU-6050) |
| **R/W** | 0 = Write (maître → esclave) ; 1 = Read (esclave → maître) | `W` ou `R` |
| **ACK** | Bit 9 bas (esclave répond) | ✅ ACK |
| **NACK** | Bit 9 haut (pas de réponse) | ❌ NACK = esclave absent ou erreur |
| **DATA** | Octets de données | `0x6B, 0x00` |
| **STOP** | Front montant SDA quand SCL=HIGH | Carré rouge `P` dans Saleae |

---

📷 **[ILLUSTRATION 1]**
*Capture d'écran Saleae Logic 2 annotée montrant une transaction I2C complète. Deux voies : CH0=SCL (horloge régulière) et CH1=SDA (données). Sur la voie CH1, les annotations du décodeur indiquent : "S" (start, flèche rouge), puis "0x68 W" (adresse 7 bits + Write, rectangle vert), puis "ACK" (vert), puis "0x6B" (registre, rectangle bleu), "ACK", "0x00" (données, rectangle bleu), "ACK", "P" (stop, flèche rouge). Style capture d'analyseur logique pédagogique, fond sombre.*

> **Légende :** Transaction I2C décodée dans Saleae Logic 2. Le maître (Arduino) écrit la valeur `0x00` dans le registre `0x6B` de l'esclave à l'adresse `0x68` (MPU-6050). Chaque ACK vert confirme que l'esclave a bien reçu l'octet précédent. Un NACK rouge indiquerait que l'esclave n'a pas répondu — typiquement un problème d'adresse, de câblage ou de pull-up manquant.

### Configurer le décodeur I2C dans Saleae

```
1. Ouvrir Saleae Logic 2
2. Brancher l'analyseur : CH0 → SCL, CH1 → SDA, GND → GND circuit
3. Régler la fréquence d'échantillonnage : 8 MHz (pour I2C 400 kHz)
4. Analyser → Add Analyzer → I2C
5. SCL = CH0, SDA = CH1
6. Lancer une capture (Start + exécuter le code Arduino)
7. Zoom sur la capture → les trames s'affichent décodées
```

### Diagnostic I2C — Les problèmes courants

| **Symptôme sur la capture** | **Cause probable** | **Solution** |
|---|---|---|
| Pas de START — SDA et SCL toujours HIGH | Code non lancé ou bus bloqué | Vérifier le code Arduino ; reset du bus |
| NACK sur l'adresse | Mauvaise adresse ou esclave absent/non alimenté | Vérifier l'adresse dans le datasheet (souvent configurable via pin AD0) |
| Signal déformé, bords arrondis lents | Pull-up trop élevée ou fréquence trop haute | Diminuer la valeur des pull-up (4,7kΩ → 2,2kΩ) ou réduire la fréquence du bus |
| SDA reste LOW en permanence | Bus bloqué (esclave coincé mi-transaction après reset) | Envoyer 9 coups d'horloge sur SCL pour libérer le bus |

---

## 4️⃣ DÉCODAGE SPI

### Rappel du protocole SPI

> SPI (Serial Peripheral Interface) utilise **4 fils** minimum :
> - **MOSI** : Master Out Slave In — données maître → esclave
> - **MISO** : Master In Slave Out — données esclave → maître
> - **SCLK** : horloge générée par le maître
> - **CS/SS** : Chip Select (actif BAS) — sélectionne un esclave

### Les 4 modes SPI (CPOL / CPHA)

| **Mode** | **CPOL** | **CPHA** | **SCLK repos** | **Capture sur** |
|---|---|---|---|---|
| **Mode 0** | 0 | 0 | Bas | Front montant |
| **Mode 1** | 0 | 1 | Bas | Front descendant |
| **Mode 2** | 1 | 0 | Haut | Front descendant |
| **Mode 3** | 1 | 1 | Haut | Front montant |

> **Mode 0** est le plus courant (Arduino par défaut).

> Pour identifier le mode : regarder l'état de SCLK quand CS est HIGH (repos) → CPOL. Puis voir sur quel front les données changent → CPHA.

### Structure d'une transaction SPI

```
CS    ‾‾‾‾‾‾┐                           ┌‾‾‾‾‾‾‾
            │                           │
            └───────────────────────────┘
            ↑ CS LOW = begin             ↑ CS HIGH = end

SCLK  _____┐_┐_┐_┐_┐_┐_┐_┐_           _
            │ 1 2 3 4 5 6 7 8 coups d'horloge

MOSI  ──────[  b7 b6 b5 b4 b3 b2 b1 b0 ]───
              ← Octet envoyé par le maître →

MISO  ──────[  d7 d6 d5 d4 d3 d2 d1 d0 ]───
              ← Octet reçu de l'esclave →
```

### Champs d'une trame SPI lus dans Saleae

| **Champ** | **Valeur dans Saleae** | **Interprétation** |
|---|---|---|
| CS LOW | Flèche descendante | Début de transaction |
| MOSI | Valeur hex en rectangle | Commande ou données envoyées |
| MISO | Valeur hex en rectangle | Réponse de l'esclave |
| CS HIGH | Flèche montante | Fin de transaction |

### Configurer le décodeur SPI dans Saleae

```
1. Analyser → Add Analyzer → SPI
2. Assigner les voies :
   MOSI = CH0, MISO = CH1, SCLK = CH2, CS = CH3 (si disponible)
3. Configurer le mode (CPOL=0, CPHA=0 pour Mode 0)
4. Bits per word = 8 (standard)
5. CS active: LOW
```

---

📷 **[ILLUSTRATION 2]**
*Capture Saleae annotée d'une transaction SPI 3 octets. Quatre voies visibles : CS (ligne haute puis basse puis haute), SCLK (horloge régulière 8 pulses × 3 fois), MOSI (3 rectangles annotés : "0x9F" commande, "-" pause, "-" pause), MISO (3 rectangles : "-" nul, "0xEF" manufacturer ID, "0x30" device ID). Le décodeur affiche en dessous les octets interprétés. Style capture analyseur logique pédagogique, fond sombre.*

> **Légende :** Transaction SPI décodée — lecture de l'ID JEDEC d'une mémoire flash Winbond W25Q32. Le maître envoie la commande `0x9F` sur MOSI. L'esclave répond sur MISO avec son Manufacturer ID (`0xEF`) puis son Device ID. CS est actif bas — tant qu'il est LOW, l'esclave est sélectionné.

---

## 5️⃣ MSO — UTILISATION DES VOIES NUMÉRIQUES

### Configurer un MSO (ex: Rigol MSO5000)

```
1. Connecter les sondes numériques (D0–D15) et le GND commun
2. Activer les voies numériques : bouton "Digital" ou "D0-D7"
3. Régler le seuil logique : Menu Threshold
   → 3,3V system : seuil = 1,65V (VCC/2)
   → 5V system : seuil = 2,5V
4. Activer le décodage : Menu Decode → I2C / SPI / UART
5. Assigner les voies aux signaux (ex: D0=SCL, D1=SDA)
6. La trame décodée s'affiche en bas de l'écran
```

### Avantage du MSO : corrélation analogique + logique

```
CH1 (analogique, voie 1) :  ~~~[signal analogique 3.3V]~~~
D0  (numérique) :           ─────┐ ┌─┐ ┌─┐ ┌─  SCL
D1  (numérique) :           ──┐  └─┘ └─┘ └─┘   SDA

→ On voit simultanément :
  - La forme exacte du signal (tension, temps de montée, overshoot)
  - Le chronogramme logique (hi/low)
  - La trame décodée (adresse, données)
```

---

## 6️⃣ RÉCAPITULATIF COMPARATIF

| **Critère** | **Oscillo seul** | **MSO** | **Analyseur logique** |
|---|---|---|---|
| Mesure tension exacte | ✅ | ✅ | ❌ (seulement HIGH/LOW) |
| Nombre de voies logiques | ❌ | 8–16 | 8–32+ |
| Décodage protocoles | ❌ | ✅ (intégré) | ✅ (logiciel PC) |
| Corrélation analogique + logique | ❌ | ✅ | ❌ |
| Coût | 300–1000€ | 800–3000€ | 10–500€ |
| Usage portable / terrain | Difficile | Difficile | ✅ (USB sur laptop) |

---

## ✅ AUTO-ÉVALUATION

- [ ] Je sais distinguer DSO et MSO — les voies supplémentaires du MSO sont numériques
- [ ] Je sais connecter un analyseur logique (GND en premier, puis les voies)
- [ ] Je sais choisir la bonne fréquence d'échantillonnage (≥ 10 × fbus)
- [ ] Je sais identifier les champs d'une trame I2C : START, ADDR, R/W, ACK/NACK, DATA, STOP
- [ ] Je comprends que ACK = SDA bas au 9ème bit = l'esclave répond ✅
- [ ] Je sais identifier les 4 signaux SPI : MOSI, MISO, SCLK, CS
- [ ] Je sais configurer le mode SPI (CPOL/CPHA) en regardant l'état de SCLK au repos
- [ ] Je sais diagnostiquer un NACK (esclave absent ou mauvaise adresse)

---

## 📚 VOCABULAIRE CLEF

| **Terme** | **Définition** |
|---|---|
| **MSO** | Mixed Signal Oscilloscope — oscillo avec voies analogiques + numériques |
| **DSO** | Digital Storage Oscilloscope — oscillo numérique sans voies logiques |
| **Analyseur logique** | Instrument capturant des signaux numériques et décodant les protocoles |
| **Saleae Logic 2** | Logiciel d'analyse pour analyseurs logiques USB Saleae |
| **PulseView** | Logiciel open-source (sigrok) pour analyseurs logiques génériques |
| **Fréquence d'échantillonnage** | Nombre de mesures par seconde : doit être ≥ 10 × fbus |
| **START condition** | Front descendant SDA quand SCL=HIGH → début trame I2C |
| **STOP condition** | Front montant SDA quand SCL=HIGH → fin trame I2C |
| **ACK** | Acknowledgment — SDA bas au 9ème bit I2C → l'esclave confirme |
| **NACK** | No ACK — SDA haut au 9ème bit → esclave absent ou erreur |
| **MOSI** | Master Out Slave In — données du maître vers l'esclave (SPI) |
| **MISO** | Master In Slave Out — données de l'esclave vers le maître (SPI) |
| **CPOL** | Clock Polarity — niveau de SCLK au repos (0=bas, 1=haut) |
| **CPHA** | Clock Phase — front sur lequel les données sont capturées |
| **Pull-up** | Résistance reliant SCL/SDA au VCC — obligatoire pour I2C |

---

**Document – BAC PRO CIEL – A2 – E2/U21 – Version 1.0 – 2026**
