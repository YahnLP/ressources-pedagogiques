# 📁 DOSSIER RESSOURCES — EXAMEN BLANC E2
## Document Autorisé · Examen Complet 2h · Circuit STATION_E2_FINAL

---

> **⚠️ SEUL DOCUMENT AUTORISÉ PENDANT L'EXAMEN**
> **Aucun Internet · Aucun téléphone · Aucune aide extérieure**

---

## R1 — Schéma du circuit STATION_E2_FINAL

```
                    ┌──────────────────────────────────────────────────────┐
                    │               ESP32 DevKit v1                         │
                    │                                                       │
  3V3 ─[R_pull]──┬─ GPIO4       GPIO2 ─[R_LED]─[LED_R]─ GND               │
                 │                                                          │
                DHT22            GPIO5 ─[R_pot = 10kΩ potentiomètre] ─ GND │
                 │                                                          │
                GND              GPIO34 ─ curseur potentiomètre             │
                    │                                                       │
  USB_5V ─[AMS1117]─ 3V3 ─ [C1] ─ GND                                    │
              │        └─ [R_charge = 68 Ω] ─ GND                         │
              └─────────────────────────────────────────────────────────────┘

Valeurs NOMINALES déclarées dans le cahier des charges :
  R_pull    : 10 kΩ  ±5%
  R_LED     : 220 Ω  ±5%   ← À VÉRIFIER
  C1        : 100 µF ±20%  ← À VÉRIFIER
  R_charge  : 68 Ω   ±5%
```

---

## R2 — Extrait datasheet DHT22 (AM2302)

```
Alimentation     : 3,3 à 5,5 V
Courant mesure   : 1 à 1,5 mA · Courant veille : 40–50 µA
Précision temp.  : ±0,5°C · Résolution : 0,1°C
Précision hum.   : ±2–5%HR · Plage température : −40 à +80°C
Période de mesure: ≥ 2 secondes entre deux lectures
```

---

## R3 — Extrait datasheet AMS1117-3.3 (LDO)

```
Vout fixe        : 3,3 V ± 1%  → Plage : [3,267 ; 3,333] V
Vin min          : 4,6 V (Vout + 1,3 V)  ·  Vin max : 15 V
Courant max      : 1 A
Rθjc             : 5 °C/W  ·  Rθja (SOT-223, PCB std) : 44 °C/W
Tj max           : 125 °C
```

---

## R4 — Extrait datasheet LED rouge standard 5mm

```
Tension directe Vf   : typique 2,0 V  ·  plage : [1,8 ; 2,2] V
Courant direct If    : recommandé 10–20 mA  ·  max : 30 mA
```

---

## R5 — Condensateur électrolytique 100 µF/16V

```
Valeur nominale : 100 µF
Tolérance       : ±20%  → Plage acceptable : [80 ; 120] µF
Tension max     : 16 V (ne pas dépasser)
Polarité        : obligatoire (+ vers VCC, − vers GND)
```

---

## R6 — Formules de référence complètes

━━━ ÉLECTRICITÉ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  

$$U = R \times I (loi d'Ohm)$$

P = U × I                        (puissance)  
R_LED = (Vcc − Vf) / If          (dimensionnement résistance LED)  
I = U / R                        (courant dans une résistance)  

━━━ ALIMENTATION ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  
Pdiss_LDO = (Vin − Vout) × Iout  (dissipation régulateur)  
Iout = Σ(courants @ Vout)        (somme de tous les courants)  
η = Vout / Vin                   (rendement LDO linéaire, approx.)  
Autonomie = Capacité(mAh) / I_moy(mA) × 0,80   (batterie)  
I_moy cycle = (I1×t1 + I2×t2) / (t1 + t2)     (courant moyen)  

━━━ THERMIQUE ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  
Tj = Tamb + Pdiss × Rθja         (température jonction sans radiateur)  
Tj max exploitable = 105°C       (125 − 20 de marge sécurité)  
Marge thermique = 105 − Tj  

━━━ MÉTROLOGIE ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  
Biais e̅  = Σei / n  
Écart-type σ = √(Σei² / (n−1))  
Incertitude type u = σ / √n  
Incertitude élargie U = 2 × u    (k=2, confiance 95%)  
Conformité : |e̅| + U ≤ spécification constructeur  

━━━ TOLÉRANCES ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  
±5%  : [Rnom × 0,95 ; Rnom × 1,05]  
±1%  : [Vnom × 0,99 ; Vnom × 1,01]  
±20% : [Cnom × 0,80 ; Cnom × 1,20]  

---

## R7 — Consommations de référence ESP32

```
Mode                    | Courant (mA) | Remarque
Actif WiFi TX           | 150 à 250    | Pic à 250 mA
Actif sans WiFi (CPU)   | 30 à 80      | Typique 50 mA en mesure
Light sleep             | 0,8          | WiFi maintenu
Deep sleep              | 0,01 à 0,15  | Typique 0,05 mA
```

---

## R8 — Rappel procédures de mesure

```
RÉSISTANCES (circuit obligatoirement éteint) :
  ① Déconnecter l'USB avant toute mesure de résistance
  ② Sélectionner Ω, gamme adaptée
  ③ Effectuer 2 mesures (repositionner les sondes)
  ④ Calculer la plage de tolérance AVANT de conclure

CONDENSATEUR (mode capacimètre) :
  ① Circuit éteint + condensateur déchargé (court-circuiter brièvement)
  ② Sélectionner µF sur le multimètre
  ③ Placer les sondes en respectant la polarité

TENSIONS (circuit sous tension) :
  ① Voltmètre en parallèle (rouge → +, noir → GND)
  ② Lire la valeur stabilisée

COURANT (si shunt disponible) :
  ① Ampèremètre en série (interrompre le circuit)
  ② Ou calculer par I = U/R si résistance connue
```

---

*Dossier Ressources Examen Blanc — BAC PRO CIEL | E2 | 3ᵉ année S15*
*Document autorisé pendant l'examen uniquement*
