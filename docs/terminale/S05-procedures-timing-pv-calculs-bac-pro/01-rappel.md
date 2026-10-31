# 📖 Rappel essentiel : réussir un TP chronométré

> À lire **avant** de manipuler l'aide-mémoire de cette séance. Il condense tout ce qu'il faut pour un TP de 2 h.

## 🤔 À ton avis ?

Tu as 2 heures, un sujet de 4 parties et un PV à rendre. Par quoi commences-tu ?

??? question "Voir une réponse possible"
    Par **lire tout le sujet** (10 min) pour repérer les calculs longs et les mesures à faire circuit éteint. Le **PV** se prépare **dès le début** (tableau vide) et se remplit au fil de l'eau : le laisser à la fin est l'erreur la plus coûteuse.

## 1. Les quatre parties d'un TP type

| Partie | Contenu | Réflexe |
|---|---|---|
| **A. Composants** | Mesurer R, C, diode | **Circuit éteint** pour R et C |
| **B. Système actif** | Tensions, signaux | Voltmètre en parallèle, masse commune |
| **C. Calculs** | Métrologie, thermique | Calculs avec les **valeurs mesurées** |
| **D. PV** | Tableau, décision, signature | Décision **cohérente** avec les écarts trouvés |

## 2. Les formules à connaître et ce qu'elles veulent dire

| Formule | Sens | Exemple (autres valeurs que le TP) |
|---|---|---|
| $I_{LED} = \dfrac{V_{CC} - V_F}{R}$ | Courant qui traverse la LED | $V_{CC}=5\,\mathrm{V}$, $V_F=2\,\mathrm{V}$, $R=330\,Ω$ → $9{,}1\,\mathrm{mA}$ |
| $P = (U_{in} - U_{out}) \times I$ | Chaleur dissipée par un régulateur linéaire | $(5 - 3{,}3) \times 0{,}12 = 0{,}20\,\mathrm{W}$ |
| $T_j = T_{amb} + P \times R_{\theta ja}$ | Température de la puce | $25 + 0{,}20 \times 44 \approx 34\,°\mathrm{C}$ |
| $\eta = \dfrac{U_{out}}{U_{in}}$ | Rendement du régulateur linéaire | $\dfrac{3{,}3}{5} = 66\,\%$ |

**Métrologie dans l'ordre** : écart $e_i$ de chaque mesure à la référence → biais $\bar{e}$ (moyenne des écarts) → écart-type $\sigma$ → $u = \dfrac{\sigma}{\sqrt{n}}$ → $U = 2u$ → **conforme si $|\bar{e}| + U \le$ tolérance**.

## 3. Ce qui fait perdre des points

> [!WARNING] ⚠️ Les pièges
> - Mesurer une résistance **sous tension**.
> - **Oublier l'unité** dans une case.
> - Calculer la plage de tolérance **après** la mesure.
> - Conclure sans chiffres (« c'est pas bon »).
> - **Oublier de signer** le PV.

> [!TIP] 💡 Les 5 éléments d'un PV
> **1** Identification (date, opérateur, conditions) · **2** Tableau de résultats (attendu, mesuré, verdict) · **3** Décision (conforme, sous réserve, refusée) · **4** Motif en deux lignes **chiffrées** · **5** **Signature**.

??? tip "💡 Aide : gestion du temps"
    - À **1 h 45**, le PV doit **déjà être commencé**.
    - Si un calcul te bloque **plus de 5 minutes**, écris la **formule** et l'application numérique, puis passe à la suite : les points de méthode comptent.
    - Prévois **5 minutes à la fin** pour vérifier les unités et la signature.

## ✅ Vérifie que tu as compris

**Q1.** Une résistance de 220 Ω ± 5 % : quelle est la plage acceptable ?

??? success "Réponse"
    De 209 Ω à 231 Ω.

**Q2.** Un régulateur dissipe 0,5 W avec $R_{\theta ja} = 60\,°\mathrm{C/W}$ à 25 °C ambiants. Quelle est $T_j$ ?

??? success "Réponse"
    $T_j = 25 + 0{,}5 \times 60 = 55\,°\mathrm{C}$.

**Q3.** Pourquoi la décision du PV doit-elle être cohérente avec les écarts relevés ?

??? success "Réponse"
    Un PV qui dit « conforme » alors qu'un composant est hors tolérance est **faux** : la décision est la **conséquence** des mesures.
