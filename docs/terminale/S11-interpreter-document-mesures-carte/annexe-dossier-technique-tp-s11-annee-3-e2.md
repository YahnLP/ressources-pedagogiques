# 📁 DOSSIER TECHNIQUE — TP S11 ANNÉE 3 – E2
## Carte Minuterie LED — AGRITECH Solutions

**À remettre au formateur à la fin de la séance avec votre nom et prénom.**

---

## DOCUMENT 1 — CAHIER DES CHARGES AGRITECH

### Présentation

> **AGRITECH Solutions** commande une carte de démonstration pour ses techniciens terrain. Cette carte, alimentée depuis une batterie 12V, doit faire clignoter une LED rouge pour signaler qu'un équipement est en service.

### Spécifications techniques

| **Paramètre** | **Exigence** |
|---|---|
| Alimentation entrée (Vin) | 12V DC ± 10% (batterie plomb) |
| Tension de sortie régulée | 5V DC ± 5% |
| Fréquence de clignotement | 1 Hz ± 10% |
| Courant LED maximum absolu | 30 mA (ne pas dépasser) |
| Courant LED nominal cible | 20 mA |
| Plage température opérationnelle | 0°C à +60°C |
| Indice de protection | IP00 (usage en boîtier externe) |

---

## DOCUMENT 2 — SCHÉMA ÉLECTRONIQUE (à interpréter)

```
                        +12V (J1 pin1)
                          │
              ┌─── C1 (100nF CMS) ───┐
              │                      │
              └─── Vin (U1:7805) ─── │ ─── GND
                       │             │
                     Vout           GND
                       │
                      +5V ─── C2 (10µF élec.) ─── GND
                       │
                       ├─── R1 (10kΩ) ───┬─── pin7 (DISCHARGE)
                       │                 │
                       │             R2 (68kΩ)
                       │                 │
                       │             pin6 (THRESHOLD) ──┬── pin2 (TRIGGER)
                       │                                │
                       │                            C3 (10µF élec.)
                       │                                │
                       │                               GND
                       │
                       ├─── pin8 (VCC) de U2:NE555
                       │
                      pin4 (RESET) ─── +5V
                      pin5 (CTRL)  ─── C4 (100nF CMS) ─── GND
                       │
                      pin3 (OUTPUT) ─── R3 (100Ω) ─── Anode(LED1) ─── Cathode(LED1) ─── GND
                       │
                      pin1 (GND) ─── GND

Alimentation : 2× PWR_FLAG (sur +5V et GND)
```

> **Note :** Ce schéma est le document de référence pour toutes les parties du TP.

---

## DOCUMENT 3 — EXTRAIT DATASHEET NE555 (Texas Instruments)

### Brochage DIP-8

```
         ┌─────────┐
GND    1 ─┤         ├─ 8  VCC
TRIG   2 ─┤  NE555  ├─ 7  DISCHARGE
OUTPUT 3 ─┤         ├─ 6  THRESHOLD
RESET  4 ─┤         ├─ 5  CONTROL VOLTAGE
         └─────────┘
```

### Mode astable — Formules

```
Fréquence :   f = 1,44 / ((Ra + 2×Rb) × C)        [Hz]
Rapport cyc.: DC = (Ra + Rb) / (Ra + 2×Rb)         [sans unité]
Durée tHigh : tH = 0,693 × (Ra + Rb) × C           [s]
Durée tLow  : tL = 0,693 × Rb × C                  [s]
Période     : T  = tH + tL = 1/f                   [s]
```

### Caractéristiques électriques (extraits)

| **Paramètre** | **Min** | **Typ** | **Max** |
|---|---|---|---|
| VCC | 4,5V | — | 16V |
| Courant de sortie (sink) | — | 200mA | — |
| Fréquence max recommandée | — | — | 300 kHz |

---

## DOCUMENT 4 — EXTRAIT DATASHEET L7805 (STMicroelectronics)

### Brochage TO-220

```
   ┌──────────────┐
   │     7805     │
(1)│  (2)│  (3)   │
  Vin  GND  Vout
```

### Caractéristiques

| **Paramètre** | **Min** | **Typ** | **Max** |
|---|---|---|---|
| Vout | 4,75V | 5,00V | 5,25V |
| Vin min (dropout) | 7V | — | — |
| Vin max absolu | — | — | 35V |
| Courant max | — | — | 1A |
| OTP (protection thermique) | — | 150°C | — |

### Condensateurs recommandés

```
Entrée  : C ≥ 100nF (découplage haute fréquence)
Sortie  : C ≥ 10µF (stabilité en charge variable)
```

---

**Document – BAC PRO CIEL – A3 – E2/U22 – Version 1.0 – 2026**
