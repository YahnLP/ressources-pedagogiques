# 🗂️ AIDE-MÉMOIRE ENTRAÎNEMENT FINAL — À PLASTIFIER
## Points de Contrôle E2 · Derniers Automatismes · BAC PRO CIEL · E2 · S17 · 3ᵉA

---

## 🔴 Les 3 erreurs qui coûtent le plus

```
1. Mesurer R/C sous tension
   → Valeur fausse → tout faux
   → TOUJOURS éteindre l'USB d'abord

2. Calculs avec valeur nominale
   → Utiliser TOUJOURS la valeur mesurée
   → R_LED=330Ω mesurée → I=1,3/330 (pas 1,3/220)

3. PV non signé
   → −2 à −5 pts automatiques
   → Signer AVANT de rendre, même si incomplet
```

---

## 🧠 8 Réflexes (à réciter)

```
① Éteindre AVANT mesure R ou C
② Plage calculée AVANT comparaison
③ Unité sur CHAQUE case
④ Métrologie : e̅ / σ / u / U
⑤ |e̅|+U ≤ spécif → chiffre vs chiffre
⑥ Valeur MESURÉE dans les calculs
⑦ Décision PV COHÉRENTE avec les KO
⑧ SIGNER avant de rendre
```

---

## ⚡ Formules à sortir en 5 secondes

```
Pdiss = (Vin−Vout) × Iout = 1,7 × I_LDO
Tj = Tamb + Pdiss × 44   (max = 105°C)
I_moy = (I_actif×t1 + I_sleep×t2) / total
I_batt = I_moy / η_convertisseur
Auto = Capacité/I_batt × 0,80
e̅=Σei/n · σ=√(Σei²/(n-1)) · u=σ/√n · U=2u
Conformité : |e̅|+U ≤ 0,5°C
R(MTBF) = 36,8%  ← JAMAIS 50%
Rs_// = 1−(1−R1)(1−R2)
%GRR = 5,15×σ_GRR/Tol×100
```

---

## ⏱️ Séquençage CCF (2h)

```
0:00-0:08 → Lire TOUT le sujet
0:08-0:43 → Partie A : composants CIRCUIT ÉTEINT
0:43-1:13 → Partie B : bilan + Tj + autonomie
1:13-1:33 → Partie C : DHT22 6 mesures + métrologie
1:33-1:52 → Partie D : PV complet
1:52-1:57 → Vérifier unités + cohérence décision
1:57-2:00 → SIGNER + rendre
```

---

## 🔍 Détecter un défaut

```
Si R ou C mesurée > ±5/20% du nominal :
→ Calculer impact avec valeur mesurée
→ Cause + recommandation OBLIGATOIRES
→ Classifier : mineure / majeure / critique
```

---

## 📋 PV en 5 étapes

```
① En-tête (ref, date, T°, Vin)
② Tableau (plages + valeurs + OK/KO)
③ Analyse NC (cause+impact+reco)
④ Synthèse (Tj, autonomie, décision)
⑤ SIGNER
```

---

## 📐 Tolérances rapides

```
±5%  : [Nom×0,95 ; Nom×1,05]
±1%  : [Nom×0,99 ; Nom×1,01]
±20% : [Nom×0,80 ; Nom×1,20]
AMS1117-3.3 : [3,267 ; 3,333] V
```

---

*Aide-Mémoire Final — À plastifier · Conserver pour le jour J*
*BAC PRO CIEL | E2 Systèmes Électroniques | 3ᵉ année S17*
