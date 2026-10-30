# 🗂️ AIDE-MÉMOIRE ULTIME CCF E2 — À PLASTIFIER
## Examen Blanc · Toutes Formules · Tous Réflexes · BAC PRO CIEL · E2 · S15 · 3ᵉA

---

## ⏱️ Stratégie 2h — CCF

```
0:00-0:08 → Lire TOUT le sujet + repérer les calculs lourds
0:08-0:43 → Partie A : composants (CIRCUIT ÉTEINT !)
0:43-1:13 → Partie B : bilan + thermique + autonomie
1:13-1:33 → Partie C : métrologie DHT22 (6 mesures min)
1:33-1:52 → Partie D : PV complet
1:52-1:55 → SIGNER + vérifier unités
1:55-2:00 → Marge : relire les non-conformités vs décision
```

---

## 🧠 8 Réflexes automatiques

```
① R et C : CIRCUIT ÉTEINT avant toute mesure
② Plage CALCULÉE avant de comparer
③ UNITÉ sur chaque case (Ω/V/mA/W/°C/µF)
④ Métrologie : e̅/σ/u/U DANS CET ORDRE
⑤ |biais|+U vs spécification chiffre vs chiffre
⑥ Calculs avec valeur MESURÉE (pas nominale !)
⑦ PV : décision COHÉRENTE avec les KO trouvés
⑧ SIGNER avant de rendre — toujours
```

---

## ⚡ Bilan puissance — 6 étapes

① I de chaque composant (inclure R_charge !)  
② I_LDO = Σ courants  
③ Pdiss = (Vin − Vout) × I_LDO = 1,7 × I_LDO  
④ Tj = Tamb + Pdiss × 44 · Marge = 105 − Tj  

$$⑤ η = \dfrac{V_{out}}{V_{in}} = \dfrac{3{,}3}{5} = 66\,\mathrm{\%}$$

⑥ Autonomie = Capacité/I_batterie × 0,80  
I_batterie = I_moy / η (si buck-boost)  

---

## 🔋 Autonomie — Ordre de calcul

$$I_moy_ESP32 = \dfrac{I_{\mathrm{actif}} \times t1 + I_{\mathrm{sleep}} \times t2}{t1+t2}$$

$$I_moy_total = I_moy_ESP32 + I_DHT22 + I_{\mathrm{LED}} + I_{\mathrm{charge}}$$

$$I_{\mathrm{batterie}} = I_moy_total / η_convertisseur$$

Autonomie   = Capacité(mAh) / I_batterie(mA) × 0,80  

---

## 📐 Métrologie (6 mesures)

$$x̄ = Σ\dfrac{T°}{n}$$

e̅ = Σei/n     (ei = T°i − T°_réf)  

$$σ = \sqrt{Σ\dfrac{ei^2}{n-1}}$$

u = σ/√n  

$$U = 2u$$

Conformité : |e̅|+U ≤ 0,5°C  

---

## 🔍 Détecter un défaut caché

```
Signal d'alarme : R ou C mesurée > ±5% (ou ±20%) du nominal
→ Calculer impact AVEC la valeur MESURÉE
→ Classifier : mineure / majeure / critique
→ Cause probable + recommandation obligatoires
```

---

## 🖊️ Formulation PV type

```
NON CONFORME :
"X = ___ Ω ∉ [__;__] Ω → NC (+___% d'écart).
 Cause : ___. Impact : ___. Reco : ___."

MÉTROLOGIE :
"|e̅|+U = ___+___ = ___ ≤ 0,5°C → CONFORME."

THERMIQUE :
"Tj = ___°C · Marge = ___°C → satisfaisante."

AUTONOMIE :
"Autonomie = ___ jours · Objectif ___ jours :
 ☐ ATTEINT ☐ NON ATTEINT · Cause principale : ___."
```

---

## 🚨 Erreurs les plus coûteuses

```
❌ Mesure R/C sous tension → valeur fausse → C4 faux
❌ Calculs avec valeur nominale (pas mesurée)
❌ R_charge oubliée → I_LDO et autonomie faux
❌ PV non signé (−2pts automatique)
❌ Décision PV incohérente (−4pts)
❌ Motif PV < 3 lignes → −4pts
❌ Calcul autonomie sans η du convertisseur
```

---

*Aide-Mémoire Ultime CCF E2 — À plastifier · Conserver le jour J*
*BAC PRO CIEL | E2 Systèmes Électroniques | 3ᵉ année S15*
