# 📖 Rappel essentiel : les quatre blocs de la consolidation finale

> À lire **avant** le cahier d'exercices. Chaque bloc a sa méthode : tu les retrouves ici en quelques lignes.

## 🤔 À ton avis ?

Quel est le point commun entre un calcul d'incertitude, une alarme avec hystérésis, une vérification KiCad et une inspection IPC ?

??? question "Voir une réponse possible"
    Dans les quatre cas, on **compare un résultat à un critère chiffré** et on **justifie** la décision : plage de tolérance, seuil haut/bas, règle ERC/DRC, critère de la norme.

## Bloc A : métrologie

**Ordre à respecter** : moyenne $\bar{x}$ → écart-type $s$ → $u_A = \dfrac{s}{\sqrt{n}}$ → $u_{B,rés} = \dfrac{\text{résolution}}{2\sqrt{3}}$ → $u_{B,cl} = \dfrac{\text{classe}\% \times \bar{x}}{100\sqrt{3}}$ → $u_c = \sqrt{u_A^2 + u_{B,rés}^2 + u_{B,cl}^2}$ → $U = 2u_c$ (arrondi par **excès** à 1 chiffre significatif).

> [!WARNING] ⚠️ Pièges
> Utiliser la **pleine échelle** au lieu de la valeur mesurée pour la classe · additionner les incertitudes au lieu de les composer en **racine carrée** · arrondir trop tôt.

## Bloc B : KPI, alarmes et code ESP32

- **Hystérésis** : l'alarme se **déclenche** au seuil haut et ne se **désactive** qu'en dessous du seuil **bas**. Entre les deux, l'état **ne change pas**.
- **Buffer circulaire** : un tableau de *N* valeurs où l'on **écrase la plus ancienne** pour garder les *N* dernières ; la **moyenne glissante** lisse les mesures.
- **Tendance** : $\dfrac{\Delta T}{\Delta t}$ ; positive si la valeur monte.

**Exemple** : seuils 35 °C (haut) et 33 °C (bas). À 34 °C : si l'alarme était **active**, elle **le reste** ; si elle était **inactive**, elle **le reste**.

## Bloc C : KiCad

Ordre : **schéma → ERC (0 erreur) → empreintes → netlist → PCB → DRC (0 erreur)**. Les erreurs fréquentes : **PWR_FLAG** manquant, **broche non connectée**, **empreinte** ne correspondant pas au composant, **broche RESET** du NE555 non reliée.

## Bloc D : normes, IPC et DAT

- **IPC-A-610** : norme de **qualité d'assemblage** ; chaque observation est jugée **conforme**, **acceptable** ou **non conforme** selon la classe (ici classe 2). Dans ce cours : décalage d'un CMS **jusqu'à 50 %** de sa largeur accepté, remplissage d'un trou métallisé **d'au moins 75 %**. Un **court-circuit** ou une **polarité inversée** est **toujours** non conforme.
- **DAT** : dossier qui décrit l'architecture, la configuration, les procédures et les **limites** de responsabilité.

??? tip "💡 Aide : ordres de grandeur pour vérifier tes réponses"
    - **Incertitude élargie** d'une mesure de tension de régulateur : de l'ordre de **0,01 à 0,05 V**.
    - **Composante dominante** : en général la **classe** de l'instrument ($u_{B,cl}$), pas la résolution.
    - **Buffer circulaire** : l'indice se calcule avec `index = (index + 1) % N`.
    - **Hystérésis** : si ton alarme « clignote » dans ton raisonnement, tu as sans doute **mélangé** seuil haut et seuil bas.
    - **IPC** : un résultat « presque à la limite » (par exemple 72 % pour un minimum de 75 %) est **non conforme** : on ne **tolère pas** au jugé.

## ✅ Vérifie que tu as compris

**Q1.** Une alarme a pour seuils 30 °C et 28 °C. La température passe de 31 °C à 29 °C. L'alarme est-elle active ?

??? success "Réponse"
    **Oui** : elle ne se désactive qu'à 28 °C ou moins.

**Q2.** Pourquoi arrondit-on $U$ par excès ?

??? success "Réponse"
    Pour **ne pas sous-estimer** l'incertitude.

**Q3.** Que fait le DRC que l'ERC ne fait pas ?

??? success "Réponse"
    Il vérifie la **géométrie du PCB** (espacements, largeurs, pistes non reliées), alors que l'ERC vérifie la **logique électrique du schéma**.
