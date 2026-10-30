# 🗂️ AIDE-MÉMOIRE SUJET BLANC NV2 — À PLASTIFIER
## Grille Résumée · Stratégie · Formules · BAC PRO CIEL · E2 · S13 · 3ᵉA

---

## 📊 Grille résumée (poids par critère)

```
C1 — Instruments     /20  → Circuit ÉTEINT pour R (4pts d'un coup)
C2 — Dossier ressourc/15  → Plages calculées AVANT comparaison
C3 — Mesures/calculs /25  → Bilan puissance + métrologie complets
C4 — Analyse défaut  /20  → Identifier ≠ valeur nominale + impact
C5 — PV recettage    /20  → 8 lignes + analyse + décision + SIGNATURE
TOTAL               /100
```

---

## ⏱️ Stratégie 2h pour NV2

```
0:00-0:10 → Lire sujet ET grille · repérer poids C3 et C4
0:10-0:45 → Partie A : composants (circuit ÉTEINT!)
0:45-1:20 → Partie B : bilan puissance + thermique
1:20-1:45 → Partie C : DHT22 + analyse défaut
1:45-2:00 → Partie D : PV complet + SIGNER
1:55 → ALERTE : PV commencé ? Signé ?
```

---

## 🔍 Détecter un défaut caché

```
SIGNAL D'ALARME : R_LED mesurée différente de > ±5% du nominal
→ Calculer l'impact CHIFFRÉ avec la vraie valeur
→ Ne pas recalculer avec le nominal dans le bilan de puissance !

Exemple : R_LED = 150Ω (au lieu de 220Ω)
  I_LED = (Vcc − Vf) / 150  ← utiliser LA VALEUR MESURÉE
  Classification : mineure / majeure / critique → justifier
```

---

## ⚡ Bilan puissance — ordre des calculs

① I de chaque composant (tableau)  
② I_LDO = Σ(tous les courants @ 3,3V)  
③ Pdiss = (Vin − Vout) × I_LDO = 1,7 × I_LDO  
④ Tj = Tamb + Pdiss × Rθja (44 °C/W)  
⑤ Marge = 105 − Tj  (OK si > 20°C)  

$$⑥ η = \dfrac{V_{out}}{V_{in}} = \dfrac{3{,}3}{5} = 66\,\mathrm{\%}$$

Composants à ne PAS oublier :  
ESP32 · DHT22 · LED · R_CHARGE (!)  

---

## 📐 Formules NV2 essentielles

```
I_LED = (Vcc − Vf) / R_LED  ← R mesurée !
I_charge = Vcc / R_charge
I_LDO = I_ESP32 + I_DHT22 + I_LED + I_charge
Pdiss = 1,7 × I_LDO (Vin=5V, Vout=3,3V)
Tj = Tamb + Pdiss × 44
e̅ = Σei/n · σ=√(Σei²/(n−1)) · U=2σ/√n
|e̅|+U ≤ 0,5°C → CONFORME
```

---

## ✅ PV en 5 étapes ordonnées

```
① En-tête (opérateur, date, conditions, Vin)
② Tableau 8 paramètres (plages + valeurs)
③ Analyse non-conformités (cause + impact + reco)
④ Bilan puissance résumé (P, Tj, marge)
⑤ Décision + motif 3 lignes + SIGNER
```

---

## 🚨 Erreurs qui coûtent le plus

```
❌ R mesurée sous tension (−4pts C1.1)
❌ Bilan avec valeur nominale (pas mesurée) → C3+C4 faux
❌ R_charge oubliée dans le bilan → I_LDO faux
❌ PV non signé (−2pts C5.7)
❌ Décision PV incohérente avec les KO trouvés
```

---

*Aide-Mémoire Sujet Blanc NV2 — À plastifier*
*BAC PRO CIEL | E2 Systèmes Électroniques | 3ᵉ année S13*
