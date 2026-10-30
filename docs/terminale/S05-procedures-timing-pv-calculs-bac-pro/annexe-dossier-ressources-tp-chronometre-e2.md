# 📁 DOSSIER RESSOURCES — TP CHRONOMÉTRÉ E2
## Documents Autorisés · S5 · 3ᵉ ANNÉE · E2

---

> **⚠️ CE DOCUMENT EST AUTORISÉ PENDANT LE TP**
> Il contient toutes les informations de référence dont vous aurez besoin.
> Vous ne pouvez pas accéder à Internet. Aucune autre aide n'est autorisée.

---

## R1 — Schéma du circuit SONDE_E2_A3

```
                          ┌─────────────────────────────────────┐
                          │           ESP32 DevKit v1            │
                          │                                      │
  3V3 ──[R_pullup]──┬─── GPIO4    GPIO2 ──[R_LED]──[LED]── GND │
                    │                                            │
                   [DHT22]                                       │
                    │                                            │
                   GND                                           │
                          │                                      │
  USB/5V ──[AMS1117]──── 3V3                              GND   │
              │                                                  │
             [C1=100µF]                                         │
              │                                                  │
             GND                                                 │
                          └─────────────────────────────────────┘
```

**Valeurs nominales sur le circuit :**

| Référence | Composant | Valeur nominale | Tolérance |
|---|---|---|---|
| $R_{\mathrm{pullup}}$ | Résistance pull-up DHT22 | 10 kΩ | ± 5% |
| $R_{\mathrm{LED}}$ | Résistance LED | 220 Ω | ± 5% |
| C1 | Condensateur élec. | 100 µF | ± 20% |
| LED | Diode électroluminescente rouge | Vf = 2,0 V typique | — |
| D1 | Diode 1N4007 | Vf = 0,7 V typique | — |

---

## R2 — Extrait datasheet DHT22 (AM2302)

```
SPÉCIFICATIONS ÉLECTRIQUES :
  Alimentation (VCC) : 3,3 V à 5,5 V
  Courant en mesure  : 1 à 1,5 mA
  Courant en veille  : 40 à 50 µA

PERFORMANCES DE MESURE — TEMPÉRATURE :
  Plage               : −40°C à +80°C
  Précision           : ± 0,5°C
  Résolution          : 0,1°C
  Temps de réponse    : < 5 s (63% d'une variation)
  Période de mesure   : ≥ 2 s entre deux lectures

PERFORMANCES DE MESURE — HUMIDITÉ :
  Plage               : 0 à 100 %HR
  Précision           : ± 2 à 5 %HR selon plage
  Résolution          : 0,1 %HR
```

---

## R3 — Extrait datasheet AMS1117-3.3 (LDO)

```
CARACTÉRISTIQUES PRINCIPALES :
  Vout                : 3,3 V fixe (tolérance ± 1%)
  Plage Vout accept.  : 3,267 V à 3,333 V
  Vin min             : Vout + Vdropout = 3,3 + 1,3 = 4,6 V min
  Vin max             : 15 V
  Iout max            : 1 A (courant de sortie maximum)
  
DONNÉES THERMIQUES (boîtier SOT-223) :
  Rθjc                : 5 °C/W
  Rθja                : 44 °C/W (sur PCB FR4, sans radiateur)
  Tj max              : 125 °C
```

---

## R4 — Extrait datasheet LED rouge standard (5mm)

```
CARACTÉRISTIQUES TYPIQUES :
  Couleur             : Rouge (λ = 630 nm)
  Tension directe Vf  : 1,8 à 2,2 V (typique : 2,0 V)
  Courant direct If   : 20 mA (max : 30 mA)
  Courant recommandé  : 10 à 20 mA
```

---

## R5 — Formules de référence

```
LOI D'OHM :           U = R × I
PUISSANCE :           P = U × I
RÉSISTANCE LED :      R = (Vcc − Vf) / If
DISSIPATION LDO :     Pdiss = (Vin − Vout) × Iout
TEMPÉRATURE JCT :     Tj = Tamb + Pdiss × Rθja
BIAIS MÉTROLOGIE :    e̅ = Σei / n
ÉCART-TYPE :          σ = √(Σei² / (n−1))
INCERTITUDE TYPE :    u = σ / √n
INCERTITUDE ÉLARGIE : U = k × u   (k=2 → 95% confiance)
CONFORMITÉ :          |e̅| + U ≤ Spécification constructeur
AUTONOMIE :           t = Capacité(mAh) / I_moy(mA)
```

---

## R6 — Tolérances et critères de conformité

```
RÉSISTANCES :
  Code couleur or (4ème bande)     : ± 5%
  Code couleur argent               : ± 10%
  Ex: 10 kΩ ± 5% → [9 500 Ω ; 10 500 Ω]
  Ex: 220 Ω ± 5% → [209 Ω ; 231 Ω]

TENSIONS :
  AMS1117-3.3 : sortie acceptable dans [3,267 V ; 3,333 V]
  USB 5V nominal : acceptable dans [4,75 V ; 5,25 V]

DÉCISION DE CONFORMITÉ :
  CONFORME      : la valeur mesurée est dans la plage de tolérance
  NON CONFORME  : la valeur mesurée dépasse la tolérance
  HORS SPÉC     : la valeur dépasse la limite absolue (sécurité)
```

---

## R7 — Consommations de référence ESP32

```
Mode de fonctionnement      | Courant (mA) | Tension (V)
----------------------------|--------------|------------
Actif (CPU) sans WiFi       | 30 à 80      | 3,3
Actif WiFi TX               | 150 à 250    | 3,3
Modem sleep (WiFi maintenu) | 15 à 20      | 3,3
Light sleep                 | 0,8          | 3,3
Deep sleep                  | 0,01 à 0,15  | 3,3
```

---

## R8 — Procédure de mesure de résistances (rappel)

```
1. ÉTEINDRE le circuit ou déconnecter la résistance d'au moins une patte
2. Sélectionner la gamme Ohmmètre (Ω) sur le multimètre
3. Placer les sondes aux bornes de la résistance
4. Lire la valeur affichée
5. Vérifier la cohérence avec le code couleur si visible

⚠️ Mesurer une résistance SOUS TENSION donne une valeur FAUSSE
⚠️ Les résistances parallèles du circuit influencent la lecture
```

---

*Dossier Ressources — BAC PRO CIEL | E2 Systèmes Électroniques | 3ᵉ année S5*
*Document apprenant autorisé pendant le TP chronométré*
