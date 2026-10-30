# 🗂️ AIDE-MÉMOIRE ALIMENTATION EMBARQUÉE — À PLASTIFIER
## Bilan de Puissance · Régulateurs · Thermique · Autonomie · BAC PRO CIEL · E2 · S3 · 3ᵉ A

---

## ⚡ Bilan de puissance

Tableau : Composant | Vcc | $I_{\mathrm{pic}}$ | $I_{\mathrm{moy}}$ | $P_{\mathrm{moy}}$  

$I_{\mathrm{moy}}$ sur cycle :  

$$I_{\mathrm{moy}} = \dfrac{I_{1} \times t1 + I_{2} \times t2}{t1+t2}$$

Courant de source :  
≥ I_pic_total × 1,25  (marge 25%)  

---

## 🔌 Régulateurs — Comparatif

```
LINÉAIRE / LDO :
  Pdiss = (Vin − Vout) × Iout
  η ≈ Vout / Vin  (si Vin >> Vout → très inefficace !)
  ✓ Simple · pas de bruit HF · bon pour signal analogique
  ✗ Chaleur · mauvais sur batterie si Vin >> Vout
  → Choisir si Vdrop < 1,5V OU courant < 200mA OU signal sensible

DÉCOUPAGE (Buck/Boost) :
  η = 85-95%  (excellent sur batterie !)
  ✓ Rendement élevé · autonomie × 2 à 3
  ✗ Bruit HF (CEM !) · plus complexe
  → Choisir si Vdrop ≥ 2V ET Iout ≥ 200mA OU sur batterie
```

---

## 🌡️ Calcul thermique

```
Sans radiateur :
  Tj = Tamb + Pdiss × Rθja
  Marge = Tj_max − Tj ≥ 20°C (sécurité)

Avec radiateur :
  Tj = Tamb + Pdiss × (Rθjc + Rθcs + Rθsa)
  Rθcs (graisse thermique) ≈ 0,5°C/W

Valeurs typiques :
  TO-220 sans radiateur : Rθja = 65°C/W
  SOT-223 (LDO)        : Rθja = 44°C/W
  Tj_max courant       : 125°C
  Tj_max exploitable   : 105°C (125−20)
```

---

## 🔋 Autonomie batterie

```
t_brut (h) = Capacité (mAh) / I_moy (mA)
t_réel     = t_brut × 0,80

ESP32 consommations :
  Actif WiFi  : 150-250 mA @ 3,3V
  Veille légère : 10 mA
  Deep sleep  : 0,01-0,15 mA ← × 100 à 1000 d'économie !

Exemple deep sleep (15s actif / 285s sleep sur 300s) :
  I_moy = (200×15 + 0,01×285)/300 = 10 mA
```

---

## 🏗️ Schéma d'alimentation type

```
Source → [C_entrée 10µF] → [Régulateur] → [C_sortie 10µF + 100nF] → Charge

Options protection :
  Diode Schottky série : anti-inversion polarité
  PTC (fusible réarmable) : protection surintensité
```

---

## ⚠️ Pièges courants

```
❌ LM7805 sur 9V pour 3,3V : η = 37% (63% en chaleur !)
❌ Oublier le courant de pointe (WiFi = 250mA) pour dimensionner
❌ Capacité batterie ≠ capacité utilisable (×0,80 en pratique)
❌ Tj calculé à Tamb=25°C OK mais échoue à Tamb=60°C en été
❌ Boost nécessaire si Vin < Vout (batterie Li-ion déchargée 3V → 3,3V)
```

---

*Aide-Mémoire Alimentation Embarquée — À plastifier*
*BAC PRO CIEL | E2 Systèmes Électroniques | 3ᵉ année S3*
*Compétences S2.1 · S2.2 · S2.3 · C2.1*
