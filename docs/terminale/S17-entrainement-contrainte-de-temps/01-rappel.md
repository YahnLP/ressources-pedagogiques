# 📖 Rappel essentiel : s'entraîner sous contrainte de temps

> À lire **avant** le sprint. Le but de la séance n'est pas d'apprendre de nouvelles notions mais de **tenir le temps** sans perdre de points.

## 🤔 À ton avis ?

Tu as 40 minutes pour 6 points de mesure. Tu bloques 10 minutes sur un calcul. Que fais-tu ?

??? question "Voir une réponse possible"
    Tu **écris la formule et l'application numérique**, tu passes au point suivant, et tu **reviens** à la fin s'il reste du temps. Un point à moitié traité rapporte des points de **méthode** ; un point laissé vide, aucun.

## 1. Le principe du sprint

Chaque point est **chronométré** : 3 à 5 minutes pour un calcul simple, 15 minutes pour une métrologie, 10 minutes pour le PV. On vise la **régularité**, pas la perfection.

| Type de point | Durée visée | Réflexe |
|---|---|---|
| Mesure circuit **éteint** | 3 à 5 min | Plage calculée avant la mesure |
| Calcul de courant, puissance | 3 min | Formule → application numérique → unité |
| Métrologie (6 mesures) | 15 min | Ordre : $e_i$, $\bar{e}$, $\sigma$, $u$, $U$ |
| Mini-PV | 10 min | 5 éléments obligatoires |

## 2. Les automatismes à réciter

1. Circuit **éteint** avant de mesurer R et C.
2. **Plage** calculée avant de comparer.
3. **Unité** à chaque case.
4. Métrologie **dans l'ordre**.
5. Calculs avec les valeurs **mesurées**.
6. Décision du PV **cohérente** avec les écarts.
7. **Signer**.

## 3. Quelques ordres de grandeur à garder en tête

??? tip "💡 Aide : valeurs pour contrôler tes résultats"
    - Une **LED** reçoit généralement **5 à 20 mA**.
    - Une **résistance de pull-up** courante vaut **4,7 à 10 kΩ**.
    - Un **régulateur LDO 3,3 V** alimenté en 5 V avec quelques dizaines de mA dissipe **moins de 0,3 W**.
    - Pour un **DHT22**, l'incertitude élargie sur 6 mesures est de l'ordre de **0,1 à 0,3 °C**.
    - Un résultat qui sort de ces ordres de grandeur est **suspect** : refais le calcul avant de continuer.

## 4. Après la séance

Compte tes points par catégorie (**oublis**, **calculs**, **manipulations**, **rédaction**). Travaille d'abord celle où tu en perds le plus.

## ✅ Vérifie que tu as compris

**Q1.** Quelle erreur coûte le plus de points dans un TP chronométré ?

??? success "Réponse"
    Laisser le **PV** de côté ou **non signé**, et oublier les **unités**.

**Q2.** Pourquoi ne pas chercher la perfection dès le premier passage ?

??? success "Réponse"
    Parce qu'un travail **complet mais imparfait** rapporte plus qu'un travail **parfait mais incomplet**.
