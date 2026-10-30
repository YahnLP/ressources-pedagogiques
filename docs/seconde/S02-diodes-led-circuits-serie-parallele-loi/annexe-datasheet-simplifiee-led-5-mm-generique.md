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
| Tension directe maximale | $V_{F}$ max | 2,5 | 2,8 | 3,8 | V |
| Courant direct continu max | $I_{F}$ max | 30 | 30 | 30 | mA |
| Courant en pointe (pulsé) | $I_{\mathrm{FM}}$ | 100 | 100 | 100 | mA |
| Tension inverse maximale | $V_{R}$ | 5 | 5 | 5 | V |
| Puissance dissipée maximale | $P_{D}$ | 65 | 65 | 80 | mW |
| Température jonction max | $T_{J}$ | 125 | 125 | 125 | °C |

---

## Caractéristiques électro-optiques typiques (T = 25°C, $I_{F}$ = 20 mA)

| Paramètre | Symbole | Rouge | Vert | Bleu | Unité |
|---|---|---|---|---|---|
| **Tension directe typique** | **$V_{F}$ typ** | **2,0** | **2,1** | **3,3** | **V** |
| Longueur d'onde dominante | λ_d | 625 | 565 | 470 | nm |
| Luminosité | $I_{V}$ | 800 | 800 | 400 | mcd |
| Demi-angle d'émission | θ ½ | ±15 | ±15 | ±15 | ° |

---

## Schéma de brochage (Pinout)

---

## Courbe caractéristique $I_{F}$ = f($V_{F}$) — Caractéristique diode

---

## Comment utiliser cette datasheet

### Étape 1 — Identifier la couleur de la LED utilisée

Repère dans le tableau la colonne correspondant à ta LED : Rouge / Vert / Bleu

### Étape 2 — Relever $V_{F}$ et $I_{F}$ typiques

| Ma LED est : | $V_{F}$ à utiliser | $I_{F}$ à utiliser |
|---|---|---|
| Rouge | **2,0 V** | $20\,\mathrm{mA} = 0{,}020\,\mathrm{A}$ |
| Verte | **2,1 V** | $20\,\mathrm{mA} = 0{,}020\,\mathrm{A}$ |
| Bleue | **3,3 V** | $20\,\mathrm{mA} = 0{,}020\,\mathrm{A}$ |

### Étape 3 — Calculer la résistance

$$R = \frac{V_{alim} - V_{F}}{I_F}$$

**Mon calcul :**

| Ma tension d'alimentation | $V_{\mathrm{alim}} = \underline{\hspace{2.5em}} V$ |
|---|---|
| $V_{F}$ de ma LED | $V_{\mathrm{F}} = \underline{\hspace{2.5em}} V$ |
| Tension sur la résistance | $V_{\mathrm{R}} = V_{\mathrm{alim}} - V_{\mathrm{F}} = \underline{\hspace{2.5em}} V$ |
| $I_{\mathrm{F}} = 0{,}020\,\mathrm{A}$ | $I_{\mathrm{F}} = 0{,}020\,\mathrm{A}$ |
| **Résistance calculée** | $R = \dfrac{V_{\mathrm{R}}}{I_{\mathrm{F}}} = \underline{\hspace{2.5em}} \Omega$ |
| **Valeur normalisée choisie** | $R_{\mathrm{choisie}} = \underline{\hspace{2.5em}} \Omega$ |

### Étape 4 — Vérifier la puissance de la résistance

$$P = R \times I_{F}^2$$

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
