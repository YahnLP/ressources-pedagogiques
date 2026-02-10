---
title: "E2 - Pack 06 - Fiche de cours élève - Maintenance et réparation"
module: "BAC PRO CIEL - E2"
version: "1.0"
---

# Maintenance et réparation

## 🎯 Objectifs (niveau E2)
À la fin de cette fiche, je suis capable de :

| Je sais… | Exemple attendu en E2 |
|---|---|
| **Différencier** préventive / prédictive / corrective | “Préventive = avant la panne ; corrective = je dépanne ; prédictive = je surveille.” |
| **Appliquer une démarche de maintenance** | “Je fais une checklist : inspection → nettoyage → soudures → mesures.” |
| **Diagnostiquer** puis **réparer** | “Je note symptôme → tests → cause → réparation → test final.” |
| **Choisir** l’outil adapté | “Multimètre : U/continuité/test diode ; oscilloscope : signal ; pompe à dessouder : retirer composant.” |
| **Travailler en sécurité** (ESD, alim, courts-circuits) | “Je coupe l’alim avant de modifier, j’évite ponts d’étain, je protège les composants ESD.” |

---

## 🔑 Idée essentielle avant de commencer
En entreprise, la maintenance sert à **éviter les arrêts**, à **sécuriser** le matériel, et à **prolonger la durée de vie** des équipements.

En E2, on attend surtout une chose :  
➡️ **je décris ce que je fais et pourquoi** (avec des preuves : mesures, observations, conclusion).

---

## I. Principes de la maintenance et de la réparation en électronique

La maintenance et la réparation des équipements électroniques consistent à entretenir, diagnostiquer, et réparer les circuits et les systèmes pour prolonger leur durée de vie et garantir leur bon fonctionnement.

Il existe deux grandes logiques :
- **Prévenir** la panne (avant qu’elle arrive)
- **Corriger** la panne (quand elle est là)

### ✅ Vocabulaire à maîtriser (simple et clair)
| Terme | Définition simple | Exemple |
|---|---|---|
| **Maintenance préventive** | je fais **avant que ça casse** | nettoyer, resserrer, contrôler tensions |
| **Maintenance prédictive** | je **surveille** pour anticiper | température qui monte, logs, signal qui se dégrade |
| **Maintenance corrective** | je **dépanne** | diagnostic + remplacement + test final |

---

## II. Les types de maintenance et leurs applications

### ● Maintenance préventive
Elle consiste à réaliser des contrôles périodiques pour éviter les pannes dues à l’usure, l’accumulation de poussière, ou d’autres facteurs environnementaux.

Exemple : vérifier l’état des ventilateurs et des dissipateurs thermiques pour éviter la surchauffe des composants sensibles.

En pratique, une idée très simple :  
➡️ **un ventilateur encrassé = surchauffe = panne probable**  
Même sur de petites cartes, poussière + humidité peuvent provoquer des défauts (mauvais contact, fuite, corrosion).

### ● Maintenance prédictive
Basée sur des données de surveillance, elle permet d’anticiper les pannes en détectant des signes de dégradation (bruits, échauffements, signaux anormaux).

Exemple : utiliser un capteur de température pour surveiller les variations sur un circuit de puissance, et agir si la température atteint un seuil critique.

En atelier, on peut l’illustrer avec :
- une température qui augmente progressivement,
- un signal qui devient bruité,
- une consommation qui monte anormalement.

### ● Maintenance corrective
Cette forme de maintenance intervient lorsque le circuit ou l’appareil ne fonctionne plus. Elle comprend l’identification de la panne et la réparation des composants défectueux.

Exemple : en cas de panne d’alimentation, vérifier et remplacer les composants défectueux (fusibles, régulateurs, condensateurs).

👉 Réflexe très fréquent (et très efficace) :  
**le diagnostic commence presque toujours par l’alimentation : ai-je la bonne tension ?**

---

## III. Les étapes de la maintenance préventive en électronique

La maintenance préventive consiste à effectuer régulièrement des tâches pour maintenir le circuit ou l’appareil en bon état de fonctionnement.

### ✅ Checklist préventive (ordre recommandé)
| Étape | Ce que je fais | Pourquoi |
|---|---|---|
| 1. Inspection visuelle | je cherche signes d’usure/chauffe | rapide, sans risque |
| 2. Nettoyage | poussière / débris / ventilation | évite surchauffe |
| 3. Connexions + soudures | fissures / soudures froides | évite pannes intermittentes |
| 4. Mesures “points clés” | tensions/courants aux bons endroits | détecte dérives avant panne |

---

### ● Inspection visuelle
Observer le circuit pour identifier les signes d’usure, d’accumulation de poussière, de corrosion, ou de composants déformés (condensateurs gonflés, soudures ternies).

Exemple : une inspection visuelle d’une carte mère peut révéler des condensateurs bombés, signe de vieillissement.

On cherche notamment :
- traces de chauffe,
- composants fissurés,
- fils abîmés,
- **ponts d’étain**,
- **condensateur gonflé** (souvent à remplacer).

<p align="center">
  <img src="./images/condensateur_gonfle.png" alt="Condensateur gonflé sur carte : signe de vieillissement et risque de panne" width="70%"><br>
  <em>Illustration attendue : photo d’un condensateur électrolytique bombé/abîmé sur une carte.</em>
</p>

### ● Nettoyage
La poussière et les débris peuvent altérer la dissipation thermique et créer des courts-circuits. Nettoyer régulièrement les circuits à l’aide de brosses antistatiques ou d’air comprimé.

Exemple : dans les ordinateurs, nettoyer les ventilateurs et les grilles de dissipation thermique pour éviter la surchauffe.

À retenir :
- nettoyer = meilleure ventilation = composants moins chauds,
- **attention** : pas d’objets métalliques sur la carte (risque court-circuit),
- si possible : outils antistatiques.

### ● Vérification des connexions et des soudures
Contrôler les soudures et les connexions pour détecter les fissures, soudures sèches, ou points de contact lâches qui peuvent entraîner des dysfonctionnements.

Exemple : un circuit avec des soudures froides peut générer des coupures intermittentes ou des pannes soudaines.

À retenir :
- **soudure froide = souvent panne intermittente**
- une bonne soudure : cône propre, brillante, pas de pont

<p align="center">
  <img src="./images/soudures_defauts.png" alt="Soudure correcte vs soudure froide vs pont d'étain : exemples fréquents" width="90%"><br>
  <em>Illustration attendue : 3 exemples : soudure brillante (OK), soudure mate (froide), pont d’étain (court-circuit).</em>
</p>

### ● Contrôle des valeurs de tension et de courant
Utiliser un multimètre pour vérifier les tensions et les courants aux points clés du circuit afin de s’assurer qu’ils respectent les valeurs spécifiées.

Exemple : mesurer les tensions d’alimentation pour s’assurer que chaque section du circuit reçoit une tension correcte.

En pratique, “points clés” = :
- tension d’alimentation principale,
- sortie d’un régulateur,
- entrée/sortie d’un capteur,
- alimentation d’un CI.

👉 Si la tension n’est pas bonne, **beaucoup de pannes sont expliquées**.

---

## IV. Diagnostic et réparation dans la maintenance corrective

La maintenance corrective est un processus de résolution des pannes qui inclut un diagnostic détaillé et des étapes de réparation précises.

### ✅ Méthode corrective (attendue E2)
| Étape | Ce que je note / fais | Preuve attendue |
|---|---|---|
| 1. Symptôme | ce que je constate (avant de toucher) | phrase claire + contexte |
| 2. Tests de base | alim + fusible + continuité | mesures / test continuité |
| 3. Test composants | Ω (hors tension), test diode, signaux | valeurs mesurées |
| 4. Réparation | ressouder / remplacer | justification (même valeur) |
| 5. Test final | sous tension + contrôle | circuit OK + mesures |

---

### ● Étape 1 : Observation des symptômes
Identifier les signes visibles ou audibles du dysfonctionnement, comme des composants chauffants, des bruits anormaux, ou un comportement irrégulier du circuit.

Exemple : dans un circuit d’amplification audio, des distorsions peuvent indiquer un problème au niveau des transistors de puissance.

Point très important :  
➡️ **le symptôme, on le note avant de toucher au circuit** (sinon on “efface” des indices).

### ● Étape 2 : Tests de base
Mesurer la tension d’alimentation, vérifier les fusibles, et réaliser des tests de continuité pour détecter les pannes simples.

Exemple : en cas d’absence de courant, vérifier le fusible et l’interrupteur d’alimentation avant de procéder à des tests plus poussés.

Ici, on applique : **tests simples d’abord** = gain de temps.

Réflexe très utile :
- continuité **Vcc → circuit** et **GND → retour**
- vérifier qu’il n’y a pas de court-circuit **Vcc ↔ GND**

### ● Étape 3 : Vérification des composants individuels
Tester chaque composant pour vérifier sa valeur ou son fonctionnement, en utilisant des outils de mesure comme le multimètre, le capacimètre, ou l’oscilloscope.

Exemple : mesurer la résistance d’un composant pour détecter une variation par rapport à sa valeur nominale.

Rappels opérationnels :
- Résistance : mesure en **Ω (hors tension)**
- Diode/LED : **mode test diode**
- Oscilloscope : signal **présent / absent / déformé**

### ● Étape 4 : Remplacement des composants défectueux
Une fois la panne localisée, remplacer les composants défaillants en s’assurant qu’ils respectent les caractéristiques spécifiées dans le schéma.

Exemple : remplacer un condensateur défectueux par un modèle avec la même capacité et tension nominale.

Règles simples à respecter :
- **même capacité**
- **tension nominale ≥** (au moins égale)
- respecter la **polarité** (condensateur électrolytique)

### ● Étape 5 : Test post-réparation
Après la réparation, tester le circuit sous tension pour s’assurer que la panne a été résolue et que le système fonctionne correctement.

Exemple : après avoir remplacé une diode de redressement, mesurer la tension de sortie pour confirmer que le courant est correctement redressé.

On refait la mini-checklist :
- pas de court-circuit,
- tension OK,
- fonctionnement OK.

---

## V. Outils et équipements utilisés en maintenance et réparation

La maintenance et la réparation nécessitent l’usage d’outils spécialisés pour diagnostiquer et manipuler les composants du circuit.

| Outil | À quoi il sert | Exemple concret en atelier |
|---|---|---|
| **Multimètre** | U / I / Ω / continuité / test diode | “U_alim = 5V ?”, “diode OK ?” |
| **Oscilloscope** | observer un signal dans le temps | signal absent / bruité / déformé |
| **Fer à souder** | souder / ressouder | reprise soudure froide |
| **Pompe à dessouder** | retirer l’étain | enlever composant pour le remplacer |
| **Pince ampèremétrique** | mesurer courant sans couper | circuits de puissance |
| **Capacimètre** | mesurer capacité | condensateur dégradé |
| **Testeur de transistors** | vérifier transistor | transistor HS / non conforme |

---

## VI. Les pratiques de sécurité lors de la maintenance et de la réparation

Travailler sur des circuits électriques présente des risques ; il est essentiel de respecter certaines précautions pour assurer la sécurité.

### ● Déconnexion de l’alimentation
Toujours débrancher le circuit de l’alimentation avant d’effectuer des opérations de réparation ou de diagnostic.

Exemple : ne jamais toucher aux composants d’un circuit haute tension sans être sûr qu’il est hors tension.

En atelier, même en basse tension :
- on coupe avant de modifier le câblage,
- on coupe avant de changer de mode (V ↔ Ω ↔ A).

### ● Utilisation d’équipements de protection
Porter des gants isolants si nécessaire, utiliser des outils à isolation renforcée, et travailler sur des surfaces antistatiques.

Exemple : utiliser une pince isolée pour manipuler les composants sous tension afin d’éviter tout risque de décharge.

### ● Précautions contre les décharges électrostatiques (ESD)
Utiliser un bracelet antistatique ou une surface de travail antistatique pour protéger les composants sensibles aux décharges électrostatiques.

Exemple : lors de la manipulation de circuits intégrés, porter un bracelet antistatique pour éviter de les endommager.

À retenir : l’ESD peut “tuer” un composant **sans que ça se voie**.

### ● Éviter les courts-circuits accidentels
Ne pas poser d’objets métalliques sur la carte électronique, et utiliser des outils avec des protections isolantes.

Exemple : lors de la soudure, s’assurer qu’aucun excès d’étain ne crée de connexion involontaire entre deux pistes.

Pont d’étain = court-circuit = panne immédiate (ou fusible qui saute).

---

## VII. Exemples pratiques de maintenance et réparation (conservés)

### Maintenance d’un bloc d’alimentation
- Nettoyer les ventilateurs, vérifier la tension de sortie avec un multimètre, et remplacer les condensateurs électrolytiques vieillissants.
- Exemple : dans une alimentation de PC, vérifier les tensions de 5V et 12V pour garantir la stabilité du système.

### Réparation d’un ampli audio
- En cas de distorsion, tester les transistors de puissance et les condensateurs de couplage.
- Remplacer les composants défaillants, puis vérifier la sortie avec un oscilloscope.
- Exemple : remplacer un transistor de sortie chauffant anormalement pour corriger la distorsion audio.

### Maintenance d’un système de contrôle industriel
- Réaliser des inspections visuelles, tester les relais et les fusibles, et vérifier l’état des contacts et des câblages.
- Exemple : contrôler le bon fonctionnement des relais de commande d’un moteur pour éviter des interruptions de production.

---

## VIII. Les bonnes pratiques pour prolonger la durée de vie des équipements électroniques

Une maintenance proactive et une utilisation appropriée permettent d’allonger la durée de vie des appareils et circuits électroniques.

### ● Protection contre les surcharges et les surtensions
Utiliser des dispositifs de protection (fusibles, disjoncteurs) pour protéger les composants sensibles des variations de tension.

Idée simple : **le fusible protège** (il saute avant que tout casse).

### ● Refroidissement adéquat
Garantir une ventilation suffisante pour dissiper la chaleur des circuits de puissance ou des systèmes qui consomment beaucoup d’énergie.

Ventilation = fiabilité.

### ● Utilisation d’alimentations stables
Utiliser des alimentations filtrées pour éviter les perturbations, particulièrement dans les circuits sensibles (instruments de mesure, ordinateurs).

Une alimentation instable peut créer des symptômes difficiles à comprendre (panne “bizarre”).

### ● Remplacement préventif des composants
Remplacer les composants qui montrent des signes de vieillissement (condensateurs, relais) pour éviter les pannes soudaines.

Remplacer avant panne = éviter immobilisation.

---

# Tableau récapitulatif (méthode E2)

| Objectif | Préventif | Correctif | Preuve à fournir (E2) |
|---|---|---|---|
| Éviter la panne | inspection, nettoyage, mesures | — | checklist + mesures |
| Dépanner | — | symptôme → tests → réparation → test final | relevé + conclusion |
| Sécuriser | déconnexion, ESD, éviter ponts | idem | règles citées + appliquées |
