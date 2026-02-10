---
title: "E2 - Pack 04 - Fiche de cours élève - Mesures électriques"
module: "BAC PRO CIEL - E2"
version: "1.0"
---

# Mesures électriques

## 🎯 Objectifs (niveau E2)
À la fin de cette fiche, je suis capable de :

| Je sais… | Exemple attendu en E2 |
|---|---|
| **Nommer** les grandeurs électriques | “U en V, I en A, R en Ω, P en W” |
| **Choisir** le bon instrument | “U → multimètre en V, signal → oscilloscope” |
| **Brancher correctement** pour mesurer | “U en parallèle, I en série, R hors tension” |
| **Éviter les erreurs dangereuses** | “Ne pas mesurer une tension avec la fiche rouge sur A” |
| **Interpréter une mesure** | “Je compare à un ordre de grandeur et je conclus” |

---

## 🔑 Idée essentielle avant de commencer
En diagnostic, la règle la plus simple est souvent la meilleure :

1) **Je vérifie l’alimentation** (ai-je bien la bonne tension ?)  
2) **Je vérifie les connexions** (continuité, GND, court-circuit Vcc↔GND)  
3) **Je vérifie les composants sensibles** (polarités LED/diode/condensateur, valeur des résistances)

Un élève qui suit cette logique gagne beaucoup de temps en atelier.

---

## I. Les grandeurs électriques fondamentales et leur unité de mesure

Les mesures électriques reposent sur des grandeurs de base qui permettent de comprendre et de quantifier le comportement d’un circuit.

### ● La tension (ou différence de potentiel)
- La tension représente la force qui pousse les électrons dans un circuit. Elle est mesurée en **volts (V)**.
- On distingue :
  - la tension continue (**DC**) : stable (pile, USB, alimentation de labo le plus souvent),
  - la tension alternative (**AC**) : varie périodiquement (prise secteur).

Exemple : mesurer la tension aux bornes d'une pile pour vérifier si elle est encore utilisable.

À retenir : en diagnostic, la **première mesure** est très souvent la tension d’alimentation (**U_alimentation**) :  
➡️ “Est-ce que j’ai bien 5 V / 3,3 V / 12 V ?”

<p align="center">
  <img src="./images/dc_ac_exemples.png" alt="Tension DC vs AC : pile (DC) et sinusoïde (AC)" width="85%"><br>
  <em>Illustration attendue : schéma simple montrant une pile (DC) et une sinusoïde (AC).</em>
</p>

⚠️ Sécurité : l’AC du secteur est dangereuse. En atelier, on travaille autant que possible en **basse tension**.

---

### ● Le courant électrique
- Le courant est le flux de charges électriques qui circule dans un conducteur, mesuré en **ampères (A)**.
- En courant continu (DC), le flux est constant, tandis qu’en courant alternatif (AC), il oscille entre deux directions opposées.

Exemple : vérifier le courant consommé par un appareil électronique pour s’assurer qu’il est dans les limites prévues par le circuit.

À retenir :
- le courant dépend de la **charge** : une LED + résistance consomme peu (souvent en **mA**), un moteur consomme beaucoup plus.
- mesurer le courant demande de **couper le circuit** et de brancher l’appareil **en série** : c’est plus “risqué” si on se trompe (voir la méthode plus loin).

---

### ● La résistance
- La résistance mesure l’opposition d’un matériau au passage du courant, mesurée en **ohms (Ω)**.
- Une résistance élevée limite le courant, tandis qu’une résistance faible laisse passer plus facilement les charges électriques.

Exemple : mesurer la résistance d’un fil chauffant pour s’assurer qu’il dissipera correctement la chaleur.

À retenir :
- ordres de grandeur fréquents : **220 Ω**, **1 kΩ**, **10 kΩ**…
- une résistance se mesure **hors tension**. Si le circuit est alimenté, la mesure est fausse et on peut abîmer le multimètre.
- idéalement, on mesure une résistance **isolée** (si elle est dans un circuit, le reste du circuit influence la valeur).

---

### ● La puissance électrique
- La puissance représente le taux de consommation d’énergie par un composant ou un circuit, mesurée en **watts (W)**.
- Elle est calculée avec : **P = U × I**.

Exemple : mesurer la puissance consommée par une ampoule pour calculer l’énergie qu’elle utilisera sur une certaine période.

À retenir :
- si **U** augmente ou si **I** augmente, alors **P** augmente.
- la puissance sert à **dimensionner** : éviter l’échauffement et choisir des composants adaptés (ex : résistance 1/4 W, 1/2 W…).
- on utilise parfois aussi :  
  - **P = U² / R** (utile pour une résistance)  
  - **P = R × I²** (utile si on connaît le courant)

---

## II. Instruments de mesure électrique : fonctionnement et utilisation

Différents outils sont utilisés pour mesurer les grandeurs électriques. L’objectif en E2 est de savoir **quel instrument utiliser** et surtout **comment le brancher**.

### ● Le multimètre
- Il peut mesurer la tension, le courant, la résistance, et parfois d’autres paramètres (fréquence, capacité).
- Les modes sont sélectionnés en tournant un cadran (V, A, Ω…) et en plaçant les pointes de test sur les points de mesure.

Exemple : mesurer la tension aux bornes d’une batterie en mode voltmètre (V) et en posant les sondes sur les bornes.

**Repère ultra important (ports du multimètre)**  
- **COM** : noir (toujours)
- **V/Ω** : rouge pour tension et résistance
- **mA/A** : rouge pour courant (selon la valeur)

⚠️ Erreur classique et dangereuse : rester branché sur **A** et vouloir mesurer une tension (V).  
➡️ Risque de court-circuit / fusible grillé / appareil abîmé.

<p align="center">
  <img src="./images/multimetre_modes_bornes.png" alt="Multimètre : modes et bornes (COM, VΩ, mA/A) et sélection DC/AC" width="85%"><br>
  <em>Illustration attendue : multimètre avec repères COM, VΩ, mA/A et modes DC/AC.</em>
</p>

**Astuce de sécurité :**
- si tu ne sais pas, tu demandes validation avant de mesurer un courant.
- tu commences sur le **calibre le plus grand** (et tu diminues ensuite).

---

### ● L’oscilloscope
- Utilisé pour observer des signaux variables dans le temps.
- Il affiche la tension en fonction du temps : on voit la forme du signal (sinusoïde, carré, impulsions…).

Exemple : observer le signal de sortie d’un générateur pour vérifier fréquence et amplitude.

Deux réglages essentiels :
- **Volts/div** (hauteur du signal)
- **Temps/div** (largeur / vitesse)

À retenir : l’oscilloscope ne sert pas seulement à “mesurer une tension”, il sert surtout à **voir la forme** du signal.

---

### ● L’ampèremètre
- Spécialisé dans la mesure de courant, il se place **en série**.
- Un multimètre en mode A joue ce rôle.
- Il existe aussi des pinces ampèremétriques (plutôt en électricité/puissance).

Exemple : mesurer le courant consommé par un moteur en insérant l’ampèremètre dans le circuit d’alimentation.

À retenir :
- “en série” = dans le chemin du courant
- on commence sur le plus grand calibre si on ne connaît pas la valeur

---

### ● Le mégohmmètre
- Mesure des résistances très élevées, surtout pour vérifier l’isolement dans les câbles électriques.
- Utile en maintenance d’installations, moins au quotidien en micro-électronique, mais bon à connaître.

Exemple : mesurer la résistance d’isolement d’un câble pour vérifier qu’il n’y a pas de fuite.

---

## III. Méthodes de mesure de la tension, du courant et de la résistance

### ✅ Règle de base à mémoriser
- **U** se mesure **en parallèle**
- **I** se mesure **en série**
- **R** se mesure **hors tension**

---

### ● Mesure de la tension (U)
- La tension se mesure toujours **en parallèle** du composant ou du point concerné.
- En DC : mode tension continue (DC). En AC : mode tension alternative (AC).

Exemple : mesurer la tension aux bornes d’un composant → une pointe de chaque côté du composant.

Astuce de diagnostic (alimentation) :  
- rouge sur **Vcc**, noir sur **GND**.

<p align="center">
  <img src="./images/mesure_tension_parallele.png" alt="Mesure de tension : voltmètre branché en parallèle sur un composant" width="85%"><br>
  <em>Illustration attendue : schéma d’un composant avec voltmètre branché en parallèle.</em>
</p>

---

### ● Mesure du courant (I)
- Le courant se mesure **en série** : l’ampèremètre doit faire partie du chemin du courant.
- Concrètement, on doit **ouvrir** le circuit et **insérer** l’appareil.

Exemple : pour mesurer le courant dans une lampe : débrancher un fil, insérer l’ampèremètre, puis refermer le circuit.

⚠️ C’est la mesure la plus “à risque” si on se trompe :
- il faut vérifier le bon port (mA/A)
- et le bon calibre
- idéalement, validation enseignant avant le branchement

<p align="center">
  <img src="./images/mesure_courant_serie.png" alt="Mesure de courant : ampèremètre inséré en série avec une lampe" width="85%"><br>
  <em>Illustration attendue : schéma lampe + ampèremètre inséré en série.</em>
</p>

---

### ● Mesure de la résistance (R)
- La résistance se mesure aux bornes du composant **sans alimentation**.
- Le circuit doit être hors tension (sinon mesure fausse et risque appareil).

Exemple : mesurer une résistance isolée → mode Ω, sondes sur les deux extrémités.

À retenir :
- règle simple : **Ω = hors tension**
- si la résistance est dans un circuit, il faut parfois la sortir ou isoler une patte pour ne pas être influencé par le reste du montage.

---

## IV. Interprétation des mesures et erreurs courantes

Les valeurs mesurées doivent être interprétées avec précision, en tenant compte des limites des instruments.

### ● Tolérance des instruments
Chaque instrument a une marge d’erreur.

Exemple : précision ±1% → une mesure de 5 V peut varier de ±0,05 V.

À retenir :
- on compare à un **ordre de grandeur**, pas au millième
- si la mesure est “impossible” (0 V partout, valeur incohérente), la cause est souvent simple :
  - alimentation absente,
  - mauvais mode AC/DC,
  - GND oublié,
  - mauvais branchement sur le multimètre.

---

### ● Influence de la température
Les résistances et certains composants changent de valeur avec la température.

En basse tension atelier, l’effet existe mais reste souvent modéré. On y pense surtout si un composant chauffe : la mesure peut évoluer.

---

### ● Perturbations et parasites
Des champs magnétiques ou des circuits proches peuvent perturber certaines mesures.

À retenir :
- on évite les fils trop longs,
- on évite de faire de grandes boucles,
- on éloigne si possible les sources de parasites (moteurs, alim bruyante).

---

## V. Les mesures de puissance et d’énergie : calculs et applications

### ● Calcul de la puissance (P)
**P = U × I**

Exemple : si U = 5 V et I = 0,01 A, alors P = 0,05 W.

---

### ● Puissance en courant alternatif
En AC, la puissance dépend aussi du facteur de puissance (cos φ), lié au déphasage courant/tension.

À retenir (niveau E2) :
- AC + déphasage = mesure plus complexe
- on retient l’idée sans forcément faire des calculs avancés en atelier basse tension

---

### ● Calcul de l’énergie
L’énergie se calcule en multipliant la puissance par le temps.

- en joules (J) : unité physique
- en kilowattheures (kWh) : unité utilisée sur les factures

Exemple : appareil 100 W pendant 10 h → 100 × 10 = 1000 Wh = **1 kWh**

À retenir : **1 kWh = 1000 W pendant 1 heure**

---

## VI. Sécurité lors des mesures électriques

La sécurité est primordiale lors de la manipulation de circuits sous tension.

- Utiliser des instruments isolés (pointes, pinces adaptées).
- Travailler autant que possible en **basse tension** (inférieure à 50 V).
- Vérifier l’absence de court-circuit potentiel (notamment Vcc ↔ GND).
- Garder des distances de sécurité en haute tension (si applicable).

Réflexes très concrets en atelier :
- on branche l’alimentation **en dernier**
- on ne change pas de mode (V ↔ A ↔ Ω) sans couper l’alimentation
- en doute, on demande validation avant de mesurer un courant

---

## VII. Applications concrètes des mesures électriques

- **Diagnostic de pannes** : mesurer la tension et le courant à différents points d’un circuit permet d’identifier une alimentation absente, une coupure, un court-circuit, un composant mal orienté.
- **Contrôle de consommation** : mesurer la consommation aide à repérer un circuit anormalement gourmand (échauffement possible).
- **Maintenance d’installations** : le mégohmmètre sert à vérifier l’isolement des câbles et à prévenir les fuites de courant.

En CIEL, une bonne démarche de diagnostic est souvent :
**je mesure au bon endroit → je compare à ce qui est attendu → je conclus.**

---

# Tableau récapitulatif (méthode de mesure)

| Grandeur | Unité | Instrument | Où brancher ? | Erreur fréquente |
|---|---|---|---|---|
| Tension U | V | multimètre | parallèle | mauvais mode AC/DC |
| Courant I | A | multimètre (A) | série | mesurer I en parallèle (danger) |
| Résistance R | Ω | multimètre | hors tension | mesurer sous tension |
| Puissance P | W | calcul | P = U × I | oublier unités / mA↔A |
| Signal V(t) | V | oscilloscope | parallèle | mauvais réglage temps/div |

