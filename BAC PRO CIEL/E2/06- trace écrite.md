---
title: "E2 - Pack 06 - Fiche de cours élève - Maintenance et réparation"
module: "BAC PRO CIEL - E2"
version: "1.0"
---

# Maintenance et réparation

## I. Principes de la maintenance et de la réparation en électronique

La maintenance et la réparation des équipements électroniques consistent à entretenir, diagnostiquer, et réparer les circuits et les systèmes pour prolonger leur durée de vie et garantir leur bon fonctionnement. La maintenance préventive et corrective permet d’éviter les pannes ou de les corriger rapidement en cas de dysfonctionnement.

✅ Complément utile :
- En entreprise, la maintenance sert à **éviter les arrêts** et à **sécuriser** le matériel.
- En E2, on attend une démarche : **je décris ce que je fais et pourquoi**.

● Maintenance préventive : elle vise à anticiper les pannes par des vérifications régulières, le nettoyage, et la vérification des paramètres clés des composants.

✅ Complément utile :
- Préventif = “je fais avant que ça casse”.
- Exemples simples : nettoyer, resserrer, vérifier tensions.

● Maintenance corrective : elle intervient lorsque le système présente une panne ou un dysfonctionnement. Elle consiste en un diagnostic et une réparation pour rétablir le fonctionnement normal du circuit.

✅ Complément utile :
- Correctif = “je dépanne”.
- On note toujours : symptôme + mesures + réparation.

---

## II. Les types de maintenance et leurs applications

La maintenance en électronique peut être classée en plusieurs types, chacun ayant des objectifs spécifiques :

● Maintenance préventive :
○ Elle consiste à réaliser des contrôles périodiques pour éviter les pannes dues à l’usure, l’accumulation de poussière, ou d’autres facteurs environnementaux.
○ Exemple : vérifier l’état des ventilateurs et des dissipateurs thermiques pour éviter la surchauffe des composants sensibles.

✅ Complément utile :
- Un ventilateur encrassé = surchauffe = panne probable.
- Même sur petites cartes : poussière + humidité peuvent créer des défauts.

● Maintenance prédictive :
○ Basée sur des données de surveillance, elle permet d’anticiper les pannes en détectant des signes de dégradation (bruits, échauffements, signaux anormaux).
○ Exemple : utiliser un capteur de température pour surveiller les variations sur un circuit de puissance, et agir si la température atteint un seuil critique.

✅ Complément utile :
- Prédictif = “je surveille” (capteurs, logs, températures).
- En atelier, on l’illustre avec : température qui monte, signal qui se dégrade.

● Maintenance corrective :
○ Cette forme de maintenance intervient lorsque le circuit ou l’appareil ne fonctionne plus. Elle comprend l’identification de la panne et la réparation des composants défectueux.
○ Exemple : en cas de panne d’alimentation, vérifier et remplacer les composants défectueux (fusibles, régulateurs, condensensateurs).

✅ Complément utile :
- Le diagnostic commence presque toujours par l’alimentation : ai-je la bonne tension ?

---

## III. Les étapes de la maintenance préventive en électronique

La maintenance préventive consiste à effectuer régulièrement des tâches pour maintenir le circuit ou l’appareil en bon état de fonctionnement.

● Inspection visuelle :
○ Observer le circuit pour identifier les signes d’usure, d’accumulation de poussière, de corrosion, ou de composants déformés (condensateurs gonflés, soudures ternies).
○ Exemple : une inspection visuelle d’une carte mère peut révéler des condensateurs bombés, signe de vieillissement.

✅ Complément utile :
- On cherche : traces de chauffe, composants fissurés, fils abîmés, ponts d’étain.
- Condensateur “gonflé” = composant à remplacer (risque de panne).

<p align="center">
  <img src="./images/condensateur_gonfle.png" alt="Condensateur gonflé sur carte" width="70%"><br>
  <em>Illustration attendue : photo d’un condensateur électrolytique bombé/abîmé sur une carte.</em>
</p>

● Nettoyage :
○ La poussière et les débris peuvent altérer la dissipation thermique et créer des courts-circuits. Nettoyer régulièrement les circuits à l’aide de brosses antistatiques ou d’air comprimé.
○ Exemple : dans les ordinateurs, nettoyer les ventilateurs et les grilles de dissipation thermique pour éviter la surchauffe.

✅ Complément utile :
- Nettoyer = meilleure ventilation = composants moins chauds.
- Attention : pas d’objets métalliques sur la carte.

● Vérification des connexions et des soudures :
○ Contrôler les soudures et les connexions pour détecter les fissures, soudures sèches, ou points de contact lâches qui peuvent entraîner des dysfonctionnements.
○ Exemple : un circuit avec des soudures froides peut générer des coupures intermittentes ou des pannes soudaines.

✅ Complément utile :
- Soudure froide = souvent **panne intermittente**.
- Une bonne soudure : cône propre, pas de pont.

<p align="center">
  <img src="./images/soudures_defauts.png" alt="Soudure correcte vs soudure froide vs pont" width="90%"><br>
  <em>Illustration attendue : 3 exemples : soudure brillante (OK), soudure mate (froide), pont d’étain (court-circuit).</em>
</p>

● Contrôle des valeurs de tension et de courant :
○ Utiliser un multimètre pour vérifier les tensions et les courants aux points clés du circuit afin de s’assurer qu’ils respectent les valeurs spécifiées.
○ Exemple : mesurer les tensions d’alimentation pour s’assurer que chaque section du circuit reçoit une tension correcte.

✅ Complément utile :
- Mesures “points clés” : alimentation, sortie régulateur, entrée capteur…
- Si la tension n’est pas bonne : beaucoup de pannes sont expliquées.

---

## IV. Diagnostic et réparation dans la maintenance corrective

La maintenance corrective est un processus de résolution des pannes qui inclut un diagnostic détaillé et des étapes de réparation précises.

● Étape 1 : Observation des symptômes :
○ Identifier les signes visibles ou audibles du dysfonctionnement, comme des composants chauffants, des bruits anormaux, ou un comportement irrégulier du circuit.
○ Exemple : dans un circuit d’amplification audio, des distorsions peuvent indiquer un problème au niveau des transistors de puissance.

✅ Complément utile :
- Symptôme = ce qu’on constate (ex : “ne s’allume pas”).
- On le note avant de toucher au circuit.

● Étape 2 : Tests de base :
○ Mesurer la tension d’alimentation, vérifier les fusibles, et réaliser des tests de continuité pour détecter les pannes simples.
○ Exemple : en cas d’absence de courant, vérifier le fusible et l’interrupteur d’alimentation avant de procéder à des tests plus poussés.

✅ Complément utile :
- “Tests simples d’abord” = gain de temps.
- Continuité Vcc→circuit et GND→retour, + pas de court-circuit.

● Étape 3 : Vérification des composants individuels :
○ Tester chaque composant pour vérifier sa valeur ou son fonctionnement, en utilisant des outils de mesure comme le multimètre, le capacimètre, ou l’oscilloscope.
○ Exemple : mesurer la résistance d’un composant pour détecter une variation par rapport à sa valeur nominale.

✅ Complément utile :
- Résistance : Ω (hors tension)
- Diode/LED : mode test diode
- Oscilloscope : signal présent/absent/déformé

● Étape 4 : Remplacement des composants défectueux :
○ Une fois la panne localisée, remplacer les composants défaillants en s’assurant qu’ils respectent les caractéristiques spécifiées dans le schéma.
○ Exemple : remplacer un condensateur défectueux par un modèle avec la même capacité et tension nominale.

✅ Complément utile :
- Même capacité + tension nominale ≥ (au moins égale).
- Respect polarité (condensateur électrolytique).

● Étape 5 : Test post-réparation :
○ Après la réparation, tester le circuit sous tension pour s’assurer que la panne a été résolue et que le système fonctionne correctement.
○ Exemple : après avoir remplacé une diode de redressement, mesurer la tension de sortie pour confirmer que le courant est correctement redressé.

✅ Complément utile :
- On refait la checklist : pas de court-circuit, tension OK, fonctionnement OK.

---

## V. Outils et équipements utilisés en maintenance et réparation

La maintenance et la réparation nécessitent l’usage d’outils spécialisés pour diagnostiquer et manipuler les composants du circuit.

● Multimètre : outil de base pour mesurer la tension, le courant et la résistance, essentiel pour diagnostiquer la majorité des pannes.

✅ Complément utile :
- Mode continuité + test diode = très utiles en atelier.

● Oscilloscope : utilisé pour observer les signaux variables en fonction du temps, permettant de diagnostiquer les circuits analogiques et les systèmes de fréquence.

✅ Complément utile :
- Sert à repérer un signal absent, déformé ou bruité.

● Fer à souder et pompe à dessouder : pour retirer et remplacer des composants sur des circuits imprimés, en assurant des soudures propres et solides.

✅ Complément utile :
- La pompe aide à enlever l’étain pour retirer un composant.

● Pince ampèremétrique : pour mesurer le courant sans déconnexion, utile dans les circuits de puissance ou les câbles inaccessibles.

● Capacimètre et testeur de transistors : pour mesurer la capacité des condensateurs et tester les transistors, vérifiant leur fonctionnement et leur intégrité.

---

## VI. Les pratiques de sécurité lors de la maintenance et de la réparation

Travailler sur des circuits électriques présente des risques ; il est essentiel de respecter certaines précautions pour assurer la sécurité.

● Déconnexion de l’alimentation : toujours débrancher le circuit de l’alimentation avant d’effectuer des opérations de réparation ou de diagnostic.
○ Exemple : ne jamais toucher aux composants d’un circuit haute tension sans être sûr qu’il est hors tension.

✅ Complément utile :
- En atelier, même en basse tension : on coupe avant de changer de mode ou de câblage.

● Utilisation d’équipements de protection : porter des gants isolants, utiliser des outils à isolation renforcée, et travailler sur des surfaces antistatiques pour éviter les chocs électriques.
○ Exemple : utiliser une pince isolée pour manipuler les composants sous tension afin d’éviter tout risque de décharge.

✅ Complément utile :
- Sur surface antistatique : éviter d’abîmer les composants sensibles.

● Précautions contre les décharges électrostatiques (ESD) : utiliser un bracelet antistatique ou une surface de travail antistatique pour protéger les composants sensibles aux décharges électrostatiques.
○ Exemple : lors de la manipulation de circuits intégrés, porter un bracelet antistatique pour éviter de les endommager.

✅ Complément utile :
- L’ESD peut “tuer” un composant sans que ça se voie.

● Éviter les courts-circuits accidentels : ne pas poser d’objets métalliques sur la carte électronique, et utiliser des outils avec des protections isolantes.
○ Exemple : lors de la soudure, s’assurer qu’aucun excès d’étain ne crée de connexion involontaire entre deux pistes.

✅ Complément utile :
- Pont d’étain = court-circuit = panne immédiate.

---

## VII. Exemples pratiques de maintenance et réparation
(Conservés du document)

Maintenance d’un bloc d’alimentation :
● Nettoyer les ventilateurs, vérifier la tension de sortie avec un multimètre, et remplacer les condensateurs électrolytiques vieillissants.
● Exemple : dans une alimentation de PC, vérifier les tensions de 5V et 12V pour garantir la stabilité du système.

Réparation d’un ampli audio :
● En cas de distorsion, tester les transistors de puissance et les condensateurs de couplage. Remplacer les composants défaillants, puis vérifier la sortie avec un oscilloscope.
● Exemple : remplacer un transistor de sortie chauffant anormalement pour corriger la distorsion audio.

Maintenance d’un système de contrôle industriel :
● Réaliser des inspections visuelles, tester les relais et les fusibles, et vérifier l’état des contacts et des câblages.
● Exemple : contrôler le bon fonctionnement des relais de commande d’un moteur pour éviter des interruptions de production.

---

## VIII. Les bonnes pratiques pour prolonger la durée de vie des équipements électroniques

Une maintenance proactive et une utilisation appropriée permettent d’allonger la durée de vie des appareils et circuits électroniques.

● Protection contre les surcharges et les surtensions : utiliser des dispositifs de protection (fusibles, disjoncteurs) pour protéger les composants sensibles des variations de tension.

✅ Complément utile :
- Fusible = “protection” : il saute avant que tout casse.

● Refroidissement adéquat : garantir une ventilation suffisante pour dissiper la chaleur des circuits de puissance ou des systèmes qui consomment beaucoup d’énergie.

✅ Complément utile :
- Ventilation = fiabilité.

● Utilisation d’alimentations stables : utiliser des alimentations filtrées pour éviter les perturbations, particulièrement dans les circuits sensibles (instruments de mesure, ordinateurs).

✅ Complément utile :
- Alim instable = symptômes difficiles à comprendre.

● Remplacement préventif des composants : remplacer les composants qui montrent des signes de vieillissement (condensateurs, relais) pour éviter les pannes soudaines.

✅ Complément utile :
- Remplacer avant panne = éviter immobilisation.

---

# Tableau récapitulatif (méthode E2)
| Objectif | Préventif | Correctif | Preuve à fournir |
|---|---|---|---|
| Éviter panne | inspection, nettoyage, mesures | — | checklist + mesures |
| Dépanner | — | symptôme→tests→réparation→test final | relevé + conclusion |
| Sécuriser | déconnexion, ESD, éviter ponts | idem | règles citées + appliquées |
