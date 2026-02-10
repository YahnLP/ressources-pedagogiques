---
title: "E2 - Pack 03 - Fiche de cours élève - Montage et assemblage de circuits"
module: "BAC PRO CIEL - E2"
version: "1.0"
---

# Montage et assemblage de circuits

## I. Compréhension du circuit et préparation au montage

Le montage et l’assemblage d’un circuit nécessitent une compréhension approfondie du schéma électronique et du plan de câblage pour une installation précise et fonctionnelle.

✅ **Complément utile :**
- Schéma = logique (qui est relié à qui).  
- Plan de câblage = placement réel (où je mets les fils/composants).  
- En atelier, une grande partie des pannes vient d’une **mauvaise préparation**.

Avant de commencer, il est essentiel de :

● Analyser le schéma électronique : identifier chaque composant (résistances, diodes, transistors, etc.), comprendre leur rôle dans le circuit et vérifier les connexions.

✅ **Complément utile : méthode simple**
1) repérer **Vcc/GND**  
2) suivre le circuit “du + vers le –”  
3) repérer les **points de jonction**  
4) vérifier les **polarités** (LED, diodes, condensateurs polarisés)

<p align="center">
  <img src="./images/methode_lecture_schema.png" alt="Méthode de lecture d'un schéma avant montage" width="85%"><br>
  <em>Illustration attendue : checklist visuelle en 4 étapes (Vcc/GND → connexions → jonctions → polarités).</em>
</p>

● Étudier le plan de câblage : s’assurer que l’on comprend la disposition physique des composants, leur orientation, et les chemins de connexion.

✅ **Complément utile :**
- Sur breadboard : comprendre quelles rangées/rails sont déjà connectés.
- Sur PCB : repérer l’orientation des composants (encoche du CI, bande “-” du condensateur, sens diode).

● Réunir tous les composants : vérifier les spécifications et la polarité (quand applicable) de chaque composant pour éviter les erreurs au moment de l’assemblage.

✅ **Complément utile :**
- Vérifier la **valeur** (Ω, µF) + la **polarité**.
- Une résistance trop faible peut créer un courant trop fort (ex : LED grillée).

● Préparer l’espace de travail : organiser un espace propre et bien éclairé, avec des outils à portée de main (fer à souder, pinces, multimètre).

✅ **Complément utile :**
- Pro : “j’anticipe” → je gagne du temps et j’évite les erreurs.
- Sécurité : le fer à souder chauffe très fort → zone dédiée.

---

## II. Les techniques de montage sur différents supports

Les composants peuvent être assemblés sur plusieurs types de supports selon les besoins du circuit et les contraintes de l’environnement d’utilisation.

✅ **Complément utile :**
- Il faut choisir le support selon : **rapidité**, **fiabilité**, **modification**, **compacité**.

### ● Montage sur plaque de prototypage (breadboard) :
○ Utilisée principalement pour des tests ou des prototypes, cette plaque permet un montage rapide sans soudure.  
○ Les composants sont insérés dans des trous connectés par des lignes conductrices, ce qui permet des modifications faciles.  
○ Exemple : tester un circuit de capteur de température en reliant simplement les composants pour s’assurer du bon fonctionnement avant le montage définitif.

✅ **Complément utile :**
- Avantage : très rapide, facile à modifier.
- Limite : moins fiable si ça bouge (fils qui se débranchent).

<p align="center">
  <img src="./images/breadboard_connexions.png" alt="Breadboard : rails d'alimentation et rangées connectées" width="90%"><br>
  <em>Illustration attendue : schéma d’une breadboard avec rails +/– et zones de connexions (rangées).</em>
</p>

### ● Montage sur carte de circuit imprimé (PCB) :
○ Requiert des soudures pour fixer les composants aux pistes en cuivre qui relient les différentes parties du circuit.  
○ Les PCB sont conçus spécifiquement pour chaque circuit, offrant une meilleure fiabilité et une compacité accrue.  
○ Exemple : un PCB pour une alimentation régulée avec les composants fixés et les pistes optimisées pour minimiser les pertes de courant.

✅ **Complément utile :**
- Avantage : compact + fiable.
- Limite : difficile à modifier après fabrication, nécessite soudure/compétence.

### ● Montage sur plaque d’expérimentation (stripboard) :
○ Une plaque avec des bandes conductrices en cuivre, permettant un montage semi-permanent.  
○ Les bandes peuvent être coupées pour isoler les sections, et chaque composant est soudé pour plus de solidité.  
○ Exemple : fabriquer un amplificateur audio simple en soudant chaque composant dans des bandes distinctes, avec des coupures pour ajuster les connexions.

✅ **Complément utile :**
- Avantage : solide, modifiable “un peu” (en coupant les bandes).
- Limite : il faut penser aux bandes (risque de court-circuit si coupure oubliée).

<p align="center">
  <img src="./images/stripboard_bandes_coupure.png" alt="Stripboard : bandes cuivre et coupure" width="90%"><br>
  <em>Illustration attendue : vue d’une stripboard + exemple de bande coupée pour isoler deux zones.</em>
</p>

---

## III. Le processus de soudure des composants

La soudure est une étape essentielle dans le montage des circuits permanents. Elle permet de fixer les composants et d’assurer une connexion électrique fiable.

✅ **Complément utile :**
- Objectif : une soudure **mécaniquement solide** + **électriquement conductrice**.

● Choix du matériel de soudure : il faut un fer à souder, de l’étain (alliage de soudure) et parfois du flux pour faciliter la soudure.  
○ Fer à souder entre 350-400°C pour les composants standards, et une panne fine pour les soudures précises.

✅ **Complément utile :**
- Température trop basse → soudure froide.
- Trop haute / trop longtemps → composant abîmé.

● Préparation de la surface : nettoyer les pistes et les broches des composants pour une meilleure adhérence de l’étain.

✅ **Complément utile :**
- “Propre” = étain accroche mieux, soudure plus brillante.

● Réalisation de la soudure : <br>
○ Chauffer la jonction entre la broche du composant et la piste en cuivre avec la panne du fer.  
○ Appliquer l’étain pour qu’il fonde et recouvre la jonction ; retirer le fer une fois la soudure réalisée.  
○ Vérifier que la soudure forme un cône propre et brillant, sans excès d’étain ou connexion avec une piste adjacente.

✅ **Complément utile :**
- Le bon geste : chauffer **piste + patte** puis déposer l’étain.
- “Cône propre” = signe de bonne liaison.

<p align="center">
  <img src="./images/soudure_bonne_mauvaise.png" alt="Soudure : bonne vs soudure froide vs pont d'étain" width="90%"><br>
  <em>Illustration attendue : 3 photos/dessins : soudure brillante (OK), soudure mate/granuleuse (froide), pont d’étain (court-circuit).</em>
</p>

● Inspection des soudures : s’assurer qu’il n’y a pas de “soudure froide” (mauvaise connexion) et que toutes les connexions sont solides et bien réalisées.

✅ **Complément utile :**
- Une soudure froide peut “marcher parfois” → panne difficile à trouver.
- On inspecte : aspect + absence de pont + solidité.

---

## IV. Assemblage final et vérification des connexions

Après avoir soudé les composants, il est crucial de vérifier le circuit pour garantir sa fiabilité et son bon fonctionnement.

● Contrôle des connexions : vérifier à l’aide d’un multimètre que chaque composant est correctement relié à ceux nécessaires, et qu’il n’y a pas de court-circuit.

✅ **Complément utile :**
- Avant alimentation, on vérifie **Vcc ↔ GND** : pas de court-circuit.

● Test de continuité : utiliser la fonction de continuité du multimètre pour s’assurer que les connexions entre composants sont complètes et sans coupure.

✅ **Complément utile :**
- “Bip” = continuité (liaison).
- Pas de bip = coupure (fil manquant / piste coupée).

● Vérification de la polarité : contrôler les composants polarisés (diodes, condensateurs, transistors) pour confirmer qu’ils sont orientés correctement.

✅ **Complément utile :**
- Diode/LED : sens obligatoire.
- Condensateur polarisé : bande “–” à respecter.

● Mise sous tension progressive : si possible, appliquer une tension inférieure à celle prévue et observer le comportement du circuit avant de l’alimenter complètement.

✅ **Complément utile :**
- Objectif : éviter de “tout griller” en cas d’erreur.
- Indices : échauffement, consommation anormale, LED trop forte.

---

## V. Test et détection de pannes après assemblage

Une fois le circuit assemblé, il peut être nécessaire de procéder à des tests pour s’assurer de son bon fonctionnement et diagnostiquer des éventuelles pannes.

● Test de tension : vérifier la présence des bonnes valeurs de tension aux points clés du circuit (par exemple, sur les broches d’un amplificateur).

✅ **Complément utile :**
- On compare à une valeur attendue (ordre de grandeur).

● Vérification du courant : s’assurer que les courants aux différentes branches du circuit sont dans les valeurs attendues.

✅ **Complément utile :**
- Courant trop fort → échauffement / casse.

● Observation des signes de défauts : échauffement excessif, absence de signal, ou consommation anormale de courant sont des indices de problème.

✅ **Complément utile :**
- “Je coupe tout de suite” si ça chauffe ou sent mauvais.

● Diagnostic de pannes courantes :
○ Composants mal soudés ou dessoudés, souvent à cause de soudures froides.  
○ Court-circuit entre pistes ou composants mal orientés.  
○ Exemple : si une LED ne s’allume pas, tester le courant dans la branche pour vérifier la continuité et la polarité de la diode.

✅ **Complément utile :**
- Méthode de diagnostic LED :
  1) vérifier polarité LED
  2) vérifier résistance (valeur + connexion)
  3) vérifier continuité
  4) mesurer tension aux bornes LED

---

## VI. Assemblage de circuits avec des composants CMS (Composants Montés en Surface)

Les CMS sont des composants très petits, soudés directement sur les pistes d’un circuit imprimé sans perçage. Leur montage nécessite une technique spécifique.

● Utilisation d’un fer à souder de précision ou d’une station de soudage à air chaud : ces outils permettent de souder les petits composants sans les endommager.

✅ **Complément utile :**
- CMS = précision + outillage adapté.

● Application de pâte à souder : pour les CMS, on utilise souvent une pâte d’étain appliquée sur les pastilles de soudure avant de chauffer.

✅ **Complément utile :**
- Pâte = facilite la fixation pendant le chauffage.

● Placement précis des composants : les CMS sont placés avec une pince à épiler sur la pâte à souder, puis chauffés pour fixer chaque connexion.

✅ **Complément utile :**
- Le placement est critique : très petit, facile à décaler.

● Reflow et four de soudure : dans l’industrie, on utilise un four qui chauffe toute la carte pour fixer les composants CMS en une seule étape.

✅ **Complément utile :**
- Reflow = production en série, très rapide.

---

## VII. Enfermement et protection des circuits assemblés

Une fois le montage terminé, les circuits doivent être protégés des conditions extérieures et des interférences électromagnétiques.

● Boîtiers et enclosures : placer le circuit dans un boîtier adapté pour le protéger des poussières, des chocs et des variations d’humidité.

✅ **Complément utile :**
- Un boîtier = sécurité + durabilité.

● Fixation des composants : s’assurer que les composants et les connexions sont stables et que rien ne risque de se déplacer lors d’une utilisation.

✅ **Complément utile :**
- Éviter que des fils tirent sur les soudures.

● Blindage électromagnétique : utiliser un boîtier métallique ou des rubans de blindage pour éviter les interférences, surtout dans les circuits de haute fréquence ou de précision.

✅ **Complément utile :**
- Blindage = réduire les parasites.

● Application de vernis de protection : un vernis isolant peut être appliqué sur la carte pour la protéger de l’oxydation et des courts-circuits.

✅ **Complément utile :**
- Vernis = utile si humidité/poussière, mais demande prudence en maintenance.

---

## VIII. Exemples pratiques d’assemblage de circuits

● Assemblage d’un circuit d’éclairage LED : les LEDs sont connectées avec des résistances pour contrôler le courant et sont montées sur un PCB ; le tout est protégé dans un boîtier transparent.

✅ **Complément utile :**
- Résistance = protection LED (limite le courant).

● Construction d’un ampli audio : implique des composants polarisés (condensateurs électrolytiques, transistors) montés sur une carte, avec un soin particulier pour les soudures et le blindage pour éviter les parasites.

✅ **Complément utile :**
- Blindage utile en audio (parasites).

● Fabrication d’un capteur de température : le capteur est monté avec un microcontrôleur et un régulateur de tension, le tout dans un boîtier étanche pour protéger le circuit des éléments extérieurs.

✅ **Complément utile :**
- Capteur → traitement → action (logique CIEL).

---

# Tableau récapitulatif (vocabulaire E2)
| Notion | À quoi ça sert | Erreur fréquente |
|---|---|---|
| Breadboard | prototype rapide sans soudure | fils mal enfoncés / mauvais rail |
| PCB | fiable et compact | modification difficile |
| Stripboard | semi-permanent, bandes cuivre | oubli de coupure → court-circuit |
| Soudure froide | mauvaise connexion | panne intermittente |
| Continuité | vérifier une liaison | confondre avec tension |
| Court-circuit | danger Vcc/GND | alimentation branchée trop tôt |
| Polarité | sens diode/LED/condo | composant inversé |
| Mise sous tension progressive | limiter les dégâts | alimenter direct sans contrôle |
