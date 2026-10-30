# 🧠 RÉVISION MENTALE GUIDÉE — S17 · 3ᵉ ANNÉE · E2
## Récitation des Automatismes · Points de Contrôle · Avant le CCF

---

> **Durée** : 20 minutes · **Format** : À voix haute, seul ou en binôme
> **Règle** : Pour chaque item, **fermer la fiche** et essayer de répondre de mémoire.
> Puis rouvrir et vérifier. Cocher ✅ si acquis, ❌ si à revoir.

---

## 🧠 BLOC 1 — Les 8 Réflexes Automatiques (5 min)

> Énoncer à voix haute sans regarder, dans l'ordre.

```
Réflexe ①  : Circuit _______ avant toute mesure de résistance ou condensateur.
Réflexe ②  : Calculer la plage de tolérance _______ de comparer.
Réflexe ③  : Mettre l'_______ sur chaque case du tableau.
Réflexe ④  : Formules métrologie dans l'ordre : _______ / _______ / _______ / _______.
Réflexe ⑤  : Décision de conformité : |_______| + _______ ≤ _______.
Réflexe ⑥  : Dans tous les calculs, utiliser la valeur _______ (pas _______).
Réflexe ⑦  : Décision PV doit être _______ avec les non-conformités trouvées.
Réflexe ⑧  : _______ le PV avant de rendre.

Réponses attendues :
① ÉTEINT · ② AVANT · ③ UNITÉ · ④ e̅ / σ / u / U · ⑤ biais / U / spécification
⑥ MESURÉE / nominale · ⑦ COHÉRENTE · ⑧ SIGNER

Mon score : ___/8  ☐ Tous acquis → continuer · ☐ Manques → revoir S12-3A_02
```

---

## 🧠 BLOC 2 — Formules Alimentation (5 min)

> Fermer la fiche. Écrire les formules sur une feuille de brouillon.

1. Dissipation d'un régulateur linéaire :  
Pdiss = ___________________________  

2. Température de jonction :  
Tj = ___________________________  ·  Tj max exploitable = _____ °C  

3. Courant total LDO :  
I_LDO = ___________________________________________ (liste les composants)  

4. Rendement d'un LDO :  
η = ___________ (approximation) = _____ % pour 3,3V depuis 5V  

5. Autonomie sur batterie avec convertisseur (η_conv = 88%) :  

$$I_{\mathrm{batterie}} = \underline{\hspace{2.5em}}$$

t_réelle   = ___________________________  

Réponses :  
1. (Vin−Vout) × Iout  2. Tamb + Pdiss × Rθja · 105°C  
3. I_ESP32 + I_DHT22 + I_LED + I_charge (ne pas oublier R_charge !)  

$$4. \dfrac{V_{out}}{V_{in}} = \dfrac{3{,}3}{5} = 66\,\mathrm{\%}$$

5. I_moy / η · Capacité(mAh) / I_batterie × 0,80  

Mon score : ___/5  ☐ Tous → continuer · ☐ Revoir → S3-3A_06 + S15-3A_06  

---

## 🧠 BLOC 3 — Formules Métrologie (5 min)

```
Énoncer les formules complètes avec les symboles :

Biais    : _______ = _______ / n
Écart-type : _______ = √( _______ / (n − 1) )
Incert. type : _______ = _______ / √n
Incert. élargie : _______ = 2 × _______  (k = 2 → confiance _______ %)
Conformité : _______ + _______ ≤ _______

À t = MTBF, R = e^(-1) = _______ %   (fiabilité — JAMAIS 50%)
Rs série    : Rs = _______________________
Rs parallèle: Rs = _______________________

Réponses :
e̅=Σei/n · σ=√(Σei²/(n-1)) · u=σ/√n · U=2u · 95%
|e̅|+U ≤ spécif · 36,8% · R1×R2×R3 · 1−(1−R1)(1−R2)

Mon score : ___/8  ☐ Tous → excellent · ☐ Revoir → S11-2A_06 + S8-3A_06
```

---

## 🧠 BLOC 4 — CEM et PCB (3 min)

```
Question flash : sans réfléchir, répondre en 5 secondes chacune.

1. Taille max d'une fente dans un blindage WiFi (2,4 GHz) ?   _______ mm
2. fc d'un filtre RC avec R=10kΩ et C=100nF ?                _______ Hz
3. Plan de masse fendu : ☐ problème ☐ pas de problème         →  ☐ problème
4. Condensateur découplage : distance max au CI ?             _______ mm
5. Commande KiCad pour remplir les zones (plan de masse)?     _______
6. Émissions conduites : fréquences < _______ MHz

Réponses : 1-6,25mm · 2-159Hz · 3-problème · 4-2mm · 5-B · 6-30MHz

Mon score : ___/6  ☐ Tous → continuer · ☐ Revoir → S13-2A_06
```

---

## 📋 POINTS DE CONTRÔLE E2 — Checklist finale

> Pour chaque compétence, évaluer honnêtement : ✅ Maîtrisé / ⚠️ Fragile / ❌ Lacune

```
INSTRUMENTS :
  ☐ Mesurer une résistance hors tension (procédure en 4 étapes)
  ☐ Mesurer un condensateur au capacimètre
  ☐ Mesurer Vf d'une LED aux bornes de la LED seule
  ☐ Lire fréquence + amplitude + rapport cyclique sur oscilloscope
  ☐ Calculer un courant par I = V/R sans ampèremètre

CALCULS ALIMENTATION :
  ☐ Pdiss = (Vin−Vout) × Iout sans hésitation
  ☐ Tj = Tamb + Pdiss × 44 (AMS1117)
  ☐ I_moy cycle (formule avec t_actif et t_sleep)
  ☐ Autonomie avec facteur 0,80 ET facteur η convertisseur
  ☐ Identifier une R_charge "cachée" et l'inclure dans le bilan

MÉTROLOGIE :
  ☐ Tableau 5-6 mesures DHT22 avec colonnes ei et ei²
  ☐ Calculer e̅, σ, u, U dans l'ordre sans erreur
  ☐ Décision de conformité avec |e̅|+U vs 0,5°C

PV DE RECETTAGE :
  ☐ En-tête complet (ref, date, opérateur, conditions, Vin)
  ☐ Tableau de synthèse avec toutes les plages calculées
  ☐ Analyse non-conformité : cause + impact + recommandation
  ☐ Décision cohérente parmi 3 options
  ☐ Motif ≥ 3 lignes avec chiffres
  ☐ Signature AVANT de rendre

DÉFAUTS CACHÉS :
  ☐ Identifier une valeur mesurée > ±5% du nominal
  ☐ Calculer l'impact avec la valeur MESURÉE (pas la nominale)
  ☐ Classifier la non-conformité (mineure/majeure/critique)
```

---

## 🔴 Mon plan d'action ultime

```
Compétences encore ❌ ou ⚠️ :
  1. _________________________  → Revoir : ____________________
  2. _________________________  → Revoir : ____________________

Ce soir avant de dormir (max 30 min) :
  → Relire une seule fois l'aide-mémoire : S15-3A_E2_06

Demain matin (jour J ou veille) :
  → Ne rien réviser de nouveau
  → Vérifier que la calculatrice a des piles
  → Relire les 8 réflexes automatiques une fois
```

---

*Révision Mentale Guidée — BAC PRO CIEL | E2 Systèmes Électroniques | 3ᵉ année S17*
*À faire à voix haute — pas en lecture passive*
