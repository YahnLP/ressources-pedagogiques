# 🗂️ AIDE-MÉMOIRE MÉTROLOGIE R&R — À PLASTIFIER
## Répétabilité · Reproductibilité · %GRR · Limite Détection · BAC PRO CIEL · E2 · S8 · 3ᵉA

---

## 📐 Formules essentielles

RÉPÉTABILITÉ (EV — même opérateur) :  

$$\sigma _EV = \dfrac{\sigma _A + \sigma _B}{2}$$

→ Bruit de l'instrument  

REPRODUCTIBILITÉ (AV — entre opérateurs) :  
AV_brut = |x̄_A − x̄_B|  
$σ_{\mathrm{AV}}$ ≈ AV_brut / $\sqrt{n}$  

GRR TOTAL :  

$$\sigma _GRR = \sqrt{\sigma _EV^2 + \sigma _AV^2}$$

%GRR = (5,15 × $σ_{\mathrm{GRR}}$ / Tolérance) × 100  

LIMITE DE DÉTECTION :  

$$LDD = 1{,}65 \times \sigma _bruit (95\,\mathrm{\%})$$

LD  = 3,3 × $σ_{\mathrm{bruit}}$    (pratique)  
LD ≈ 3 × $σ_{\mathrm{bruit}}$       (règle 3-sigma)  

---

## 🚦 Interprétation %GRR

```
%GRR < 10%      → ✓✓ EXCELLENT
10% ≤ %GRR ≤ 30%→ ✓  ACCEPTABLE
%GRR > 30%      → ✗  INACCEPTABLE

NDC ≥ 5 → instrument distingue les pièces ✓
```

---

## 🎯 Répétabilité vs Reproductibilité

```
Répétabilité :
  Même opérateur · même instrument · conditions identiques
  Cause : bruit instrument, résolution, contact

Reproductibilité :
  Opérateurs différents · même instrument
  Cause : formation, méthode, interprétation
```

---

## 🔬 Limite de détection

```
Signal détectable si : signal > LD = 3 × σ_bruit

Capteur apte si : σ_bruit ≤ variation_à_détecter / 3

Ex: DHT22 σ=0,15°C → LD=0,45°C
  → Apte pour détecter des variations ≥ 0,45°C
  → Inapte pour 0,1°C de variation
```

---

## ⚠️ Distinctions clés

```
RÉSOLUTION ≠ PRÉCISION ≠ LIMITE DE DÉTECTION

Résolution = plus petit incrément affiché
Précision  = erreur max vs vraie valeur
LD         = plus petite VARIATION détectable
```

---

## 📋 Protocole R&R simplifié

1. k=2 opérateurs · n=8-10 mesures chacun  
2. Même objet, même instrument, séparément  
3. Calculer x̄ et σ de chaque opérateur  

$$4. \sigma _EV = \dfrac{\sigma _A + \sigma _B}{2}$$

5. $σ_{\mathrm{AV}}$ ≈ |x̄_A − x̄_B| / $\sqrt{n}$  

$$6. \sigma _GRR = \sqrt{EV^2 + AV^2}$$

7. %GRR = 5,15 × $σ_{\mathrm{GRR}}$ / Tolérance × 100  

---

## ⚠️ Erreurs à éviter

```
❌ Oublier d'attendre 2s entre lectures DHT22
❌ AV calculé avec les valeurs (pas les moyennes)
❌ Oublier √ dans σ_GRR = √(EV² + AV²)
❌ Confondre étendue R et σ
❌ %GRR avec tolérance unilatérale (±0,5°C → tolérance TOTALE = 1°C)
```

---

*Aide-Mémoire Métrologie R&R — À plastifier*
*BAC PRO CIEL | E2 Systèmes Électroniques | 3ᵉ année S8*
*Compétences S8.1 · S8.2 · S8.3 · S8.4 · C8.1*
