---
title: "E2 - Pack 04 - Fiche de cours élève - Mesures électriques"
module: "BAC PRO CIEL - E2"
version: "1.0"
---

# Mesures électriques

## I. Les grandeurs électriques fondamentales et leur unité de mesure

Les mesures électriques reposent sur des grandeurs de base qui permettent de comprendre et de quantifier le comportement d’un circuit. Les principales grandeurs sont :

● La tension (ou différence de potentiel) :
○ La tension représente la force qui pousse les électrons dans un circuit. Elle est mesurée en volts (V).
○ On distingue la tension continue (DC), stable et constante, utilisée dans les circuits à courant continu, et la tension alternative (AC), qui varie périodiquement, typiquement utilisée dans les réseaux domestiques.
○ Exemple : mesurer la tension aux bornes d'une pile pour vérifier si elle est encore utilisable.

✅ **Complément utile :**
- “DC” = pile, USB, alimentation de labo (souvent).
- “AC” = prise secteur (attention : dangereux, on reste en basse tension en atelier).
- En diagnostic, la première mesure est souvent : **U_alimentation** (est-ce que j’ai bien 5V ?).

<p align="center">
  <img src="./images/dc_ac_exemples.png" alt="Tension DC vs AC" width="85%"><br>
  <em>Illustration attendue : schéma simple montrant une pile (DC) et une sinusoïde (AC).</em>
</p>

● Le courant électrique :
○ Le courant est le flux de charges électriques qui circule dans un conducteur, mesuré en ampères (A).
○ En courant continu (DC), le flux est constant, tandis qu’en courant alternatif (AC), il oscille entre deux directions opposées.
○ Exemple : vérifier le courant consommé par un appareil électronique pour s’assurer qu’il est dans les limites prévues par le circuit.

✅ **Complément utile :**
- Le courant dépend de la charge : une LED + résistance consomme peu (mA), un moteur beaucoup plus.
- Mesurer le courant est plus risqué : il faut **ouvrir le circuit** et se mettre **en série**.

● La résistance :
○ La résistance mesure l’opposition d’un matériau au passage du courant, et elle est mesurée en ohms (Ω).
○ Une résistance élevée limite le courant, tandis qu’une résistance faible permet un passage plus facile des charges électriques.
○ Exemple : mesurer la résistance d’un fil chauffant pour s’assurer qu’il dissipera correctement la chaleur.

✅ **Complément utile :**
- Ordres de grandeur : 220Ω, 1kΩ, 10kΩ…
- On mesure une résistance **hors tension** sinon la valeur est fausse et on peut abîmer le multimètre.

● La puissance électrique :
○ La puissance représente le taux de consommation d’énergie par un composant ou un circuit, mesurée en watts (W).
○ Elle est calculée avec la formule P = U × I, où U est la tension et I le courant.
○ Exemple : mesurer la puissance consommée par une ampoule pour calculer l’énergie qu’elle utilisera sur une certaine période.

✅ **Complément utile :**
- Si U augmente ou si I augmente → P augmente.
- P sert à dimensionner (éviter échauffement).

---

## II. Instruments de mesure électrique : fonctionnement et utilisation

Différents outils sont utilisés pour mesurer les grandeurs électriques, chacun ayant une méthode d’utilisation et une précision propres.

● Le multimètre :
○ Il peut mesurer la tension, le courant, la résistance, et parfois d’autres paramètres (fréquence, capacité).
○ Les modes sont sélectionnés en tournant un cadran pour choisir la grandeur à mesurer, et en plaçant les pointes de test sur les points de mesure.
○ Exemple d’utilisation : mesurer la tension aux bornes d’une batterie en plaçant le multimètre en mode « voltmètre » et en posant les sondes sur les bornes de la pile.

✅ **Complément utile :**
- Toujours vérifier les **bornes** : COM (noir) et V/Ω (rouge) ou A/mA (rouge selon mesure).
- Une erreur fréquente : rester branché sur “A” et mesurer une tension → risque.

<p align="center">
  <img src="./images/multimetre_modes_bornes.png" alt="Multimètre : modes et bornes" width="85%"><br>
  <em>Illustration attendue : photo/diagramme d’un multimètre avec repères COM, VΩ, mA/A et modes DC/AC.</em>
</p>

● L’oscilloscope :
○ Utilisé pour observer les signaux variables dans le temps, particulièrement pour la tension alternative.
○ Il affiche les variations de tension en fonction du temps sur un écran, ce qui permet de visualiser des signaux périodiques, comme ceux d’un circuit AC ou d’un signal audio.
○ Exemple : observer le signal de sortie d’un générateur pour vérifier sa fréquence et son amplitude.

✅ **Complément utile :**
- L’oscilloscope “montre la forme” du signal (carré, sinusoïde…).
- Deux réglages essentiels :
  - **Volts/div** (hauteur)
  - **Temps/div** (largeur)

● L’ampèremètre :
○ Spécialisé dans la mesure de courant, il doit être placé en série dans le circuit pour mesurer l’intensité.
○ Les multimètres en mode « ampèremètre » jouent également ce rôle, bien qu’il existe des pinces ampèremétriques qui mesurent le courant sans contact direct.
○ Exemple : mesurer le courant consommé par un moteur en intégrant l’ampèremètre dans le circuit d’alimentation.

✅ **Complément utile :**
- “En série” = dans le chemin du courant.
- On commence sur le calibre le plus grand si on ne sait pas.

● Le mégohmmètre :
○ Utilisé pour mesurer les résistances très élevées, souvent pour vérifier l’isolement dans les câbles électriques.
○ Exemple : mesurer la résistance d’isolement d’un câble haute tension pour s’assurer qu’il n’y a pas de risque de fuite électrique.

✅ **Complément utile :**
- Ce n’est pas l’outil du quotidien en micro-électronique, mais utile en maintenance d’installations.

---

## III. Méthodes de mesure de la tension, du courant et de la résistance

La façon de mesurer chaque grandeur dépend des propriétés du circuit et de la précision souhaitée.

● Mesure de la tension :
○ La tension se mesure toujours en parallèle du composant ou du point de circuit concerné.
○ En courant continu, on sélectionne le mode « tension continue » (DC) sur le multimètre ; en courant alternatif, le mode « tension alternative » (AC).
○ Exemple : pour mesurer la tension aux bornes d’un composant, placer le multimètre en parallèle avec ce composant en respectant la polarité.

✅ **Complément utile :**
- “En parallèle” = une pointe de chaque côté du composant.
- Pour une alimentation : rouge sur Vcc, noir sur GND.

<p align="center">
  <img src="./images/mesure_tension_parallele.png" alt="Mesure de tension en parallèle" width="85%"><br>
  <em>Illustration attendue : schéma d’un composant avec voltmètre branché en parallèle.</em>
</p>

● Mesure du courant :
○ Le courant se mesure en série dans le circuit, ce qui signifie que l’ampèremètre doit faire partie du chemin du courant.
○ Exemple : pour mesurer le courant traversant une lampe, débrancher un fil de la lampe et le relier à l’ampèremètre, puis connecter l’autre borne de l’ampèremètre à la lampe.

✅ **Complément utile :**
- “En série” = on coupe et on insère l’appareil.
- C’est la mesure la plus “à risque” : validation enseignant avant branchement.

<p align="center">
  <img src="./images/mesure_courant_serie.png" alt="Mesure de courant en série" width="85%"><br>
  <em>Illustration attendue : schéma lampe + ampèremètre inséré en série.</em>
</p>

● Mesure de la résistance :
○ La résistance se mesure en plaçant le multimètre directement aux bornes du composant sans alimentation dans le circuit.
○ Cette mesure nécessite que le circuit soit hors tension pour éviter d’endommager l’appareil et d’obtenir des mesures précises.
○ Exemple : pour mesurer la résistance d’une résistance isolée, poser les sondes du multimètre sur chaque extrémité de la résistance en mode « ohmmètre ».

✅ **Complément utile :**
- Règle : **Ω = hors tension**.
- Idéalement, mesurer une résistance **isolée** (sinon le circuit influence).

---

## IV. Interprétation des mesures et erreurs courantes

Les valeurs mesurées doivent être interprétées avec précision, en tenant compte de certaines erreurs et limites des instruments.

● Tolérance des instruments : chaque instrument a une tolérance ou une marge d’erreur qui doit être prise en compte.
○ Exemple : si un multimètre a une précision de ±1%, une mesure de 5 V peut varier de ±0,05 V.

✅ **Complément utile :**
- On compare une mesure à un **ordre de grandeur**, pas au millième.
- Si la mesure est “impossible” (ex : 0V partout), il y a souvent : GND absent, alimentation coupée, mauvais mode.

● Influence de la température : les résistances et autres composants peuvent changer de valeur avec la température.
○ Exemple : une résistance chauffée dans un circuit de puissance peut présenter une valeur différente de celle mesurée à température ambiante.

✅ **Complément utile :**
- En atelier basse tension, l’effet existe mais reste modéré ; on le retient surtout en puissance.

● Effets des champs magnétiques : en présence de champs magnétiques ou de circuits haute fréquence, les valeurs mesurées peuvent être perturbées.
○ Exemple : mesurer le courant dans un circuit de puissance à proximité d’un moteur peut causer des interférences qui faussent les mesures.

✅ **Complément utile :**
- Parasites possibles : on éloigne les fils, on réduit les boucles, on blinde si nécessaire.

---

## V. Les mesures de puissance et d’énergie : calculs et applications

La puissance et l’énergie consommée par un circuit sont des paramètres clés pour dimensionner les composants et optimiser l’efficacité.

● Calcul de la puissance :
○ La puissance (P) se calcule par la formule P = U × I, où U est la tension en volts et I le courant en ampères.
○ Exemple : calculer la puissance d’une ampoule en multipliant la tension à ses bornes par le courant qu’elle consomme.

✅ **Complément utile :**
- Exemple LED : si U=5V et I=0,01A → P = 0,05W.

● Mesure de la puissance en courant alternatif :
○ En courant alternatif, la puissance dépend également du facteur de puissance (cos φ), qui tient compte du déphasage entre le courant et la tension.
○ Exemple : pour un circuit inductif, comme un moteur, le facteur de puissance peut réduire la puissance réelle, ce qui nécessite un wattmètre pour mesurer précisément la puissance active.

✅ **Complément utile :**
- Notion importante mais moins centrale ici : on retient “AC + déphasage = mesure plus complexe”.

● Calcul de l’énergie :
○ L’énergie (en joules ou kilowattheures, kWh) se calcule en multipliant la puissance par le temps.
○ Exemple : pour estimer la consommation d’un appareil de 100 W sur une période de 10 heures, multiplier 100 W par 10 h pour obtenir 1 kWh.

✅ **Complément utile :**
- 1 kWh = 1000 W pendant 1 heure.

---

## VI. Sécurité lors des mesures électriques

La sécurité est primordiale lors de la manipulation de circuits sous tension. Quelques précautions à respecter :

● Utilisation d’instruments isolés : utiliser des multimètres et des pinces de mesure avec une isolation appropriée pour éviter les chocs électriques.  
● Manipulation sous basse tension autant que possible : travailler sous des tensions inférieures à 50 V dans la mesure du possible, car elles sont moins dangereuses.  
● Vérification de l’absence de court-circuit : avant d’effectuer des mesures, s’assurer qu’il n’y a pas de court-circuit potentiel dans le circuit.  
● Maintien des distances de sécurité : particulièrement pour les circuits à haute tension, éviter tout contact accidentel avec des parties conductrices.

✅ **Complément utile :**
- On branche l’alimentation **en dernier**.
- On ne change pas de mode (V ↔ A) sans couper l’alimentation.

---

## VII. Applications concrètes des mesures électriques

Diagnostic de pannes dans des appareils électroniques : utiliser un multimètre pour mesurer la tension et le courant à différents points du circuit permet de repérer des composants défectueux.

Contrôle de consommation énergétique : mesurer régulièrement la consommation d’appareils électriques aide à identifier les équipements énergivores et à optimiser leur usage.

Maintenance des installations électriques : mesurer les résistances d’isolement avec un mégohmmètre pour éviter les fuites de courant dans les câbles et prévenir les risques d’incendie.

✅ **Complément utile :**
- En CIEL : diagnostic = “je mesure au bon endroit, je compare, je conclus”.

---

# Tableau récapitulatif (méthode de mesure)
| Grandeur | Unité | Instrument | Où brancher ? | Erreur fréquente |
|---|---|---|---|---|
| Tension U | V | multimètre | parallèle | mauvais mode AC/DC |
| Courant I | A | multimètre (A) | série | mesurer I en parallèle (danger) |
| Résistance R | Ω | multimètre | hors tension | mesurer sous tension |
| Puissance P | W | calcul | P=U×I | oublier unités |
| Signal | V(t) | oscilloscope | parallèle | mauvais réglage temps/div |

