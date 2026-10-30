# 📁 DOSSIER RESSOURCES NIVEAU 2 — S13 · 3ᵉ ANNÉE · E2
## Documents Autorisés · TP Complet 2h · Circuit STATION_E2_NV2

---

> **⚠️ CE DOCUMENT EST AUTORISÉ PENDANT LE TP — LIRE AVANT DE COMMENCER**
> Contient toutes les informations de référence nécessaires.
> Pas d'accès Internet · Pas d'aide extérieure.

---

## R1 — Schéma du circuit STATION_E2_NV2

```
                    ┌────────────────────────────────────────────────┐
                    │              ESP32 DevKit v1                    │
                    │                                                 │
  3V3 ─[R_pullup]─┬─ GPIO4                  GPIO2 ─[R_LED]─[LED]─ GND
                  │                                                   │
                 DHT22                       GPIO5 ─[R_IR]─[LED_IR]─ GND
                  │                                                   │
                 GND                                                  │
                    │                                                 │
  USB_5V ─[AMS1117]─ 3V3 ─[C_dec=100µF]─ GND                       │
              │        └─[R_charge]─ GND                             │
              └──────────────────────────────────────────────────────┘

Valeurs NOMINALES déclarées :
  R_pullup   : 10 kΩ ±5%
  R_LED      : 220 Ω ±5%   ← À vérifier par mesure
  R_charge   : 100 Ω ±1%
  C_dec      : 100 µF ±20%
```

---

## R2 — Extrait datasheet DHT22

```
Alimentation : 3,3 V à 5,5 V · Courant mesure : 1–1,5 mA
Précision température : ±0,5°C · Résolution : 0,1°C
Période de mesure : ≥ 2 s entre lectures
```

---

## R3 — Extrait datasheet AMS1117-3.3

```
Vout : 3,3 V ±1% → plage : [3,267 ; 3,333] V
Vin min : Vout + 1,3 V = 4,6 V · Vin max : 15 V · Iout max : 1 A
Rθjc = 5 °C/W · Rθja = 44 °C/W · Tj max = 125 °C
```

---

## R4 — Extrait datasheet LED verte standard (5mm)

```
Vf typique : 2,0–2,2 V (vert : légèrement plus élevé que rouge)
If recommandé : 10–20 mA · If max : 30 mA
Longueur d'onde : 520–530 nm
```

---

## R5 — Formules complètes

```
LOI D'OHM :               U = R × I
PUISSANCE :               P = U × I
RÉSISTANCE LED :          R = (Vcc − Vf) / If
COURANT DE CHARGE :       I = U / R
BILAN PUISSANCE :         P_totale = Σ(Pi) = Σ(Vi × Ii)
DISSIPATION LDO :         Pdiss = (Vin − Vout) × Iout
COURANT LDO :             Iout = I_ESP32 + I_DHT22 + I_LED + I_charge + ...
TEMPÉRATURE JONCTION :    Tj = Tamb + Pdiss × Rθja
MARGE THERMIQUE :         ΔT_marge = 105 − Tj  (Tj max exploitable = 125−20)
BIAIS MÉTROLOGIE :        e̅ = Σei / n
ÉCART-TYPE :              σ = √(Σei² / (n−1))
INCERTITUDE TYPE :        u = σ / √n
INCERTITUDE ÉLARGIE :     U = 2 × u  (k=2, confiance 95%)
CONFORMITÉ MÉTROLOGIE :   |e̅| + U ≤ spécification
AUTONOMIE BATTERIE :      t = Capacité(mAh) / I_moy × 0,80
```

---

## R6 — Tolérances et critères

```
Résistances :  ±5% → [Rnom×0,95 ; Rnom×1,05]
AMS1117-3.3 :  Vout dans [3,267 ; 3,333] V
USB 5V nominal : [4,75 ; 5,25] V
LED verte If   : [10 ; 30] mA (recommandé : 10–20 mA)
Tj max exploit.: 105 °C (Tj max datasheet 125 − marge sécurité 20)
```

---

## R7 — Consommations de référence ESP32

```
Actif WiFi TX : 150–250 mA · Deep sleep : 0,01–0,15 mA
Actif sans WiFi : 30–80 mA · Light sleep : 0,8 mA
```

---

## R8 — Procédure mesure résistance (rappel)

```
① Circuit ÉTEINT (déconnecter USB) · ② Gamme Ω sélectionnée
③ Sondes aux bornes · ④ Lire + noter · ⑤ Vérifier vs code couleur
⚠️ Mesure sous tension = valeur fausse (résistances en parallèle)
```

---

*Dossier Ressources Niveau 2 — BAC PRO CIEL | E2 Systèmes Électroniques | 3ᵉ année S13*
*Autorisé pendant le TP · Ne pas dépasser les limites du document*
