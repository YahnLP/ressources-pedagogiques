# 📖 Rappel essentiel : aborder un sujet complet de 2 h

> À lire **avant** le sujet. Il t'aide à lire le dossier de ressources et à enchaîner les calculs dans le bon ordre.

## 🤔 À ton avis ?

Tu as 2 h, un dossier de ressources et un circuit. Dans quel ordre travailles-tu ?

??? question "Voir une réponse possible"
    **Lire tout le sujet** (8 à 10 min), mesurer **circuit éteint** les composants passifs, puis le système actif, puis calculer (bilan, thermique, autonomie, métrologie) avec les **valeurs mesurées**, et enfin rédiger le PV. Le PV se **prépare dès le début**.

## 1. Lire le dossier de ressources

Le dossier contient le **schéma**, des **extraits de datasheet**, les **formules**, les **tolérances** et les **consommations de référence**. Il est **autorisé** : tu n'as **rien à apprendre par cœur**, mais il faut savoir **où chercher**. Avant de commencer, repère : la tension d'alimentation, les tolérances des composants, les courants maximums et les consommations.

## 2. Le bilan de puissance dans l'ordre

1. **Courant de chaque composant** (n'oublie pas la **charge** et la LED).
2. **Courant total** demandé au régulateur.
3. **Puissance dissipée** $P = (V_{in} - V_{out}) \times I$.
4. **Température de jonction** $T_j = T_{amb} + P \times R_{\theta ja}$ et **marge** par rapport au maximum.
5. **Rendement** $\eta = \dfrac{V_{out}}{V_{in}}$.
6. **Autonomie** (si batterie).

## 3. L'autonomie en quatre lignes

**Exemple** (autres valeurs que le sujet) : ESP32 actif 80 mA pendant 2 s, en veille 0,01 mA pendant 58 s ; capteur 0,05 mA ; LED 0,2 mA en moyenne ; batterie 2 000 mAh ; convertisseur de rendement 0,9.

- $I_{moy,ESP32} = \dfrac{80 \times 2 + 0{,}01 \times 58}{60} \approx 2{,}68\,\mathrm{mA}$
- $I_{moy,total} = 2{,}68 + 0{,}05 + 0{,}2 \approx 2{,}93\,\mathrm{mA}$
- $I_{batterie} = \dfrac{2{,}93}{0{,}9} \approx 3{,}25\,\mathrm{mA}$
- Autonomie $= \dfrac{2000}{3{,}25} \times 0{,}8 \approx 492\,\mathrm{h} \approx 20$ jours (le facteur 0,8 tient compte de la capacité réellement utilisable).

## 4. La métrologie sur 6 mesures

Compare chaque mesure à une **référence** : écarts $e_i$ → biais $\bar{e}$ → écart-type $\sigma$ → $u = \dfrac{\sigma}{\sqrt{6}}$ → $U = 2u$ → **conforme si $|\bar{e}| + U \le$ tolérance**.

## 5. Le défaut caché

Un composant **hors tolérance** (par exemple un condensateur mesuré 150 µF pour 100 µF nominal) se **détecte en comparant** chaque mesure à sa plage. On calcule alors l'**impact avec la valeur mesurée**, on **classe** le défaut (mineur, majeur, critique), on donne une **cause probable** et une **recommandation**.

> [!TIP] 💡 Les 5 éléments d'un PV
> **1** Identification (date, opérateur, conditions) · **2** Tableau de résultats (attendu, mesuré, verdict) · **3** Décision (conforme, sous réserve, refusée) · **4** Motif en deux lignes **chiffrées** · **5** **Signature**.

??? tip "💡 Aide : ordres de grandeur pour vérifier tes calculs"
    - **Chaleur d'un LDO** : avec un courant total de **quelques dizaines à une centaine de mA** et une chute de 1,5 à 2 V, la puissance est de l'ordre de **0,1 à 0,3 W** ; $T_j$ reste **sous 60 °C**.
    - **Rendement d'un LDO** : $\dfrac{V_{out}}{V_{in}}$ ; un 5 V → 3,3 V donne **66 %**.
    - **Autonomie** : si tu trouves **quelques heures** pour un capteur en veille profonde, ou **plusieurs années**, **recompte** les courants (la charge oubliée est l'erreur n° 1).
    - **Métrologie** : $U$ est de l'ordre de **0,1 à 0,3 °C** pour 6 mesures d'un DHT22 stable.
    - **Incohérence** : si ton PV conclut « conforme » alors que tu as trouvé un composant hors tolérance, **reprends la décision**.

## ✅ Vérifie que tu as compris

**Q1.** Pourquoi calcule-t-on avec les valeurs **mesurées** plutôt qu'avec les valeurs nominales ?

??? success "Réponse"
    Parce que ce sont celles de **la carte réelle** : un composant dérivé change les courants et les puissances.

**Q2.** Que se passe-t-il pour l'autonomie si on **oublie** le courant de la charge ?

??? success "Réponse"
    Elle est **surestimée** : le courant moyen est trop faible.

**Q3.** Un PV non signé : quelle conséquence ?

??? success "Réponse"
    Il n'a **pas de valeur** ; c'est une perte de points automatique.
