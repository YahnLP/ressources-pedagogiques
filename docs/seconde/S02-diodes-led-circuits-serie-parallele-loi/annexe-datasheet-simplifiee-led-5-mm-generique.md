# 📄 DATASHEET SIMPLIFIÉE — LED 5 mm Générique
## Fiche technique élève — Format pédagogique

---

> **Document élève — À conserver dans le portfolio**  
> BAC Pro CIEL | S2 Module E2 | Version simplifiée à partir de datasheet constructeur

---

## Identification du composant

| Champ | Valeur |
|---|---|
| **Référence** | LED-5MM-RGB (générique pédagogique) |
| **Type** | Diode électroluminescente 5 mm |
| **Boîtier** | Through-hole (composant traversant) — 2 broches |
| **Fabricant référence** | Kingbright L-7113 (série équivalente) |

---

## Caractéristiques électriques absolues maximales

> ⚠️ **Ne jamais dépasser ces valeurs — risque de destruction immédiate et irréversible**

| Paramètre | Symbole | Rouge | Vert | Bleu | Unité |
|---|---|---|---|---|---|
| Tension directe maximale | V_F max | 2,5 | 2,8 | 3,8 | V |
| Courant direct continu max | I_F max | 30 | 30 | 30 | mA |
| Courant en pointe (pulsé) | I_FM | 100 | 100 | 100 | mA |
| Tension inverse maximale | V_R | 5 | 5 | 5 | V |
| Puissance dissipée maximale | P_D | 65 | 65 | 80 | mW |
| Température jonction max | T_J | 125 | 125 | 125 | °C |

---

## Caractéristiques électro-optiques typiques (T = 25°C, I_F = 20 mA)

| Paramètre | Symbole | Rouge | Vert | Bleu | Unité |
|---|---|---|---|---|---|
| **Tension directe typique** | **V_F typ** | **2,0** | **2,1** | **3,3** | **V** |
| Longueur d'onde dominante | λ_d | 625 | 565 | 470 | nm |
| Luminosité | I_V | 800 | 800 | 400 | mcd |
| Demi-angle d'émission | θ ½ | ±15 | ±15 | ±15 | ° |

---

## Schéma de brochage (Pinout)

---

## Courbe caractéristique I_F = f(V_F) — Caractéristique diode

---

## Comment utiliser cette datasheet

### Étape 1 — Identifier la couleur de la LED utilisée

Repère dans le tableau la colonne correspondant à ta LED : Rouge / Vert / Bleu

### Étape 2 — Relever V_F et I_F typiques

| Ma LED est : | V_F à utiliser | I_F à utiliser |
|---|---|---|
| Rouge | **2,0 V** | **20 mA = 0,020 A** |
| Verte | **2,1 V** | **20 mA = 0,020 A** |
| Bleue | **3,3 V** | **20 mA = 0,020 A** |

### Étape 3 — Calculer la résistance

$$R = \frac{V_{alim} - V_F}{I_F}$$

**Mon calcul :**

| Ma tension d'alimentation | V_alim = _______ V |
|---|---|
| V_F de ma LED | V_F = _______ V |
| Tension sur la résistance | V_R = V_alim − V_F = _______ V |
| I_F = 0,020 A | I_F = 0,020 A |
| **Résistance calculée** | **R = V_R / I_F = _______ Ω** |
| **Valeur normalisée choisie** | **R_choisie = _______ Ω** |

### Étape 4 — Vérifier la puissance de la résistance

$$P = R \times I_F^2$$

Si P < 250 mW → résistance ¼ W standard (la plus courante)  
Si P > 250 mW → résistance ½ W nécessaire

---

## Série de valeurs normalisées E24 (valeurs disponibles en atelier)

| | | | | | | |
|---|---|---|---|---|---|---|
| 10 | 11 | 12 | 13 | 15 | 16 | 18 |
| 20 | 22 | 24 | 27 | 30 | 33 | 36 |
| 39 | 43 | 47 | 51 | 56 | 62 | 68 |
| 75 | 82 | 91 | 100 | 110 | 120 | 130 |
| 150 | 160 | 180 | 200 | 220 | 240 | 270 |
| 300 | 330 | 360 | 390 | 430 | 470 | 510 |
| 560 | 620 | 680 | 750 | 820 | 910 | 1000 |

> ✅ **Rappel** : On choisit toujours la valeur normalisée **immédiatement supérieure** à la valeur calculée pour protéger la LED.

---

*Fiche datasheet pédagogique simplifiée — BAC Pro CIEL S2 Module E2*  
*Source de référence : Kingbright datasheet L-7113ID/IGD/IBD — simplifiée à des fins pédagogiques*
