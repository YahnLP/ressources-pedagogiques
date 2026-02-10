---
title: "E2 - Pack 03 - Fiche de cours élève - Montage et assemblage de circuits"
module: "BAC PRO CIEL - E2"
version: "1.0"
---

# Montage et assemblage de circuits

## 🎯 Objectifs (Pour examen E2)
À la fin de cette fiche, je suis capable de :

| Je sais… | Exemple attendu en E2 |
|---|---|
| **Préparer** un montage à partir d’un schéma + plan de câblage | “Schéma = logique ; plan de câblage = placement réel.” |
| **Assembler** un circuit sur breadboard / PCB / stripboard | “Je choisis le support selon rapidité, fiabilité, compacité.” |
| **Souder** correctement (aspect + solidité + pas de pont) | “Soudure brillante, cône propre, pas de court-circuit.” |
| **Vérifier** un montage avant alimentation | “Je teste continuité, polarités, et absence de court-circuit Vcc↔GND.” |
| **Diagnostiquer** une panne simple | “LED ne s’allume pas : polarité, résistance, continuité, tension.” |

---

## 🔑 Idée essentielle avant de commencer
En atelier, une grande partie des pannes vient d’une **mauvaise préparation** : on se précipite, on câble “à l’aveugle”, puis on cherche longtemps l’erreur.

➡️ Deux repères à ne jamais confondre :
- **Schéma** = logique (qui est relié à qui).
- **Plan de câblage** = placement réel (où je mets les fils / composants).

---

## I. Compréhension du circuit et préparation au montage

Le montage et l’assemblage d’un circuit nécessitent une compréhension approfondie du schéma électronique et du plan de câblage pour une installation précise et fonctionnelle.

Avant de commencer, il est essentiel de :

### ● Analyser le schéma électronique
Il faut identifier chaque composant (résistances, diodes, transistors, etc.), comprendre leur rôle dans le circuit et vérifier les connexions.

Pour lire un schéma sans se perdre, tu peux appliquer cette méthode simple :

1) repérer **Vcc/GND**  
2) suivre le circuit “du + vers le –”  
3) repérer les **points de jonction** (connexion réelle)  
4) vérifier les **polarités** (LED, diodes, condensateurs polarisés)

<p align="center">
  <img src="./images/methode_lecture_schema.png" alt="Méthode de lecture d'un schéma avant montage : Vcc/GND, suivi du trajet, jonctions, polarités" width="85%"><br>
  <em>Illustration attendue : checklist visuelle en 4 étapes (Vcc/GND → connexions → jonctions → polarités).</em>
</p>

### ● Étudier le plan de câblage
Il faut s’assurer que l’on comprend la disposition physique des composants, leur orientation, et les chemins de connexion.

- Sur **breadboard** : il faut comprendre quelles rangées/rails sont déjà connectés (sinon tu crois relier… mais en réalité non).
- Sur **PCB** : il faut repérer l’orientation des composants (encoche du CI, bande “-” du condensateur, sens diode).

### ● Réunir tous les composants
Il faut vérifier les spécifications et la polarité (quand applicable) de chaque composant pour éviter les erreurs au moment de l’assemblage.

Avant de câbler, fais ce double contrôle :
- **valeur** (Ω, µF, etc.)
- **polarité / sens** (si le composant est polarisé)

Exemple typique : une **résistance trop faible** peut créer un courant trop fort (ex : **LED grillée**).

### ● Préparer l’espace de travail
Organiser un espace propre et bien éclairé, avec des outils à portée de main (fer à souder, pinces, multimètre).

En pratique, anticiper l’organisation fait gagner du temps et évite les erreurs (perte de pièces, mauvais composant pris, fils mal rangés).  
Côté sécurité, le fer à souder chauffe très fort : il faut une zone dédiée, stable, et dégagée.

---

## II. Les techniques de montage sur différents supports

Les composants peuvent être assemblés sur plusieurs types de supports selon les besoins du circuit et les contraintes de l’environnement d’utilisation.

Le choix du support se fait souvent selon : **rapidité**, **fiabilité**, **possibilité de modifier**, **compacité**.

| Support | Quand on l’utilise | Avantage | Limite |
|---|---|---|---|
| Breadboard | test / prototype | rapide, modifiable | moins fiable si ça bouge |
| PCB | version finale | compact, fiable | difficile à modifier |
| Stripboard | semi-permanent | solide, adaptable | risque de court-circuit si coupure oubliée |

### ● Montage sur plaque de prototypage (breadboard)
○ Utilisée principalement pour des tests ou des prototypes, cette plaque permet un montage rapide sans soudure.  
○ Les composants sont insérés dans des trous connectés par des lignes conductrices, ce qui permet des modifications faciles.  
○ Exemple : tester un circuit de capteur de température en reliant simplement les composants pour s’assurer du bon fonctionnement avant le montage définitif.

Sur breadboard :
- c’est très rapide et facile à modifier,
- mais si un fil est mal enfoncé ou si le montage est déplacé, une connexion peut se débrancher (panne “bête” mais fréquente).

<p align="center">
  <img src="./images/breadboard_connexions.png" alt="Breadboard : rails d'alimentation et rangées connectées (zones de connexions)" width="90%"><br>
  <em>Illustration attendue : schéma d’une breadboard avec rails +/– et zones de connexions (rangées).</em>
</p>

### ● Montage sur carte de circuit imprimé (PCB)
○ Requiert des soudures pour fixer les composants aux pistes en cuivre qui relient les différentes parties du circuit.  
○ Les PCB sont conçus spécifiquement pour chaque circuit, offrant une meilleure fiabilité et une compacité accrue.  
○ Exemple : un PCB pour une alimentation régulée avec les composants fixés et les pistes optimisées pour minimiser les pertes de courant.

Le PCB est très fiable et compact, mais il demande de la précision :
- soudure plus “propre”,
- modification difficile après fabrication,
- besoin de compétence et d’outillage.

### ● Montage sur plaque d’expérimentation (stripboard)
○ Une plaque avec des bandes conductrices en cuivre, permettant un montage semi-permanent.  
○ Les bandes peuvent être coupées pour isoler les sections, et chaque composant est soudé pour plus de solidité.  
○ Exemple : fabriquer un amplificateur audio simple en soudant chaque composant dans des bandes distinctes, avec des coupures pour ajuster les connexions.

La stripboard est solide, et on peut encore adapter le circuit (en coupant des bandes), mais il faut être très vigilant :
- si une coupure est oubliée, un courant peut passer où il ne faut pas → court-circuit ou fonctionnement étrange.

<p align="center">
  <img src="./images/stripboard_bandes_coupure.png" alt="Stripboard : bandes cuivre et exemple de coupure pour isoler deux zones" width="90%"><br>
  <em>Illustration attendue : vue d’une stripboard + exemple de bande coupée pour isoler deux zones.</em>
</p>

---

## III. Le processus de soudure des composants

La soudure est une étape essentielle dans le montage des circuits permanents. Elle permet de fixer les composants et d’assurer une connexion électrique fiable.

L’objectif d’une bonne soudure est double :
- une liaison **mécaniquement solide** (ça ne bouge pas),
- une liaison **électriquement conductrice** (le courant passe bien).

### ● Choix du matériel de soudure
Il faut un fer à souder, de l’étain (alliage de soudure) et parfois du flux pour faciliter la soudure.  
○ Fer à souder entre 350-400°C pour les composants standards, et une panne fine pour les soudures précises.

Deux erreurs classiques :
- température trop basse → **soudure froide** (mauvaise connexion)
- trop chaud / trop longtemps → composant abîmé (ou piste décollée)

### ● Préparation de la surface
Nettoyer les pistes et les broches des composants pour une meilleure adhérence de l’étain.  
Une surface propre aide à obtenir une soudure plus “propre” et plus fiable (souvent plus brillante).

### ● Réalisation de la soudure
○ Chauffer la jonction entre la broche du composant et la piste en cuivre avec la panne du fer.  
○ Appliquer l’étain pour qu’il fonde et recouvre la jonction ; retirer le fer une fois la soudure réalisée.  
○ Vérifier que la soudure forme un cône propre et brillant, sans excès d’étain ou connexion avec une piste adjacente.

Le bon geste à retenir : **on chauffe la piste + la patte**, puis on dépose l’étain.  
Un “cône” propre est souvent le signe d’une bonne liaison.

<p align="center">
  <img src="./images/soudure_bonne_mauvaise.png" alt="Soudure : bonne (brillante) vs soudure froide (mate/granuleuse) vs pont d'étain (court-circuit)" width="90%"><br>
  <em>Illustration attendue : 3 photos/dessins : soudure brillante (OK), soudure mate/granuleuse (froide), pont d’étain (court-circuit).</em>
</p>

### ● Inspection des soudures
S’assurer qu’il n’y a pas de “soudure froide” (mauvaise connexion) et que toutes les connexions sont solides et bien réalisées.

Une soudure froide peut être trompeuse : elle peut “marcher parfois”, puis lâcher dès qu’on bouge le fil → panne difficile à trouver.  
On inspecte donc :
- l’aspect (brillant / mat),
- l’absence de pont (pas de court-circuit),
- la solidité (ça ne bouge pas).

---

## IV. Assemblage final et vérification des connexions

Après avoir soudé les composants, il est crucial de vérifier le circuit pour garantir sa fiabilité et son bon fonctionnement.

### ● Contrôle des connexions
Vérifier à l’aide d’un multimètre que chaque composant est correctement relié à ceux nécessaires, et qu’il n’y a pas de court-circuit.

Avant toute alimentation, fais le réflexe pro :
- vérifier **Vcc ↔ GND** : il ne doit pas y avoir de court-circuit.

### ● Test de continuité
Utiliser la fonction de continuité du multimètre pour s’assurer que les connexions entre composants sont complètes et sans coupure.

- “Bip” = continuité (liaison OK)
- pas de bip = coupure (fil manquant / piste coupée / patte non soudée)

### ● Vérification de la polarité
Contrôler les composants polarisés (diodes, condensateurs, transistors) pour confirmer qu’ils sont orientés correctement.

- diode/LED : sens obligatoire
- condensateur polarisé : bande “–” à respecter

### ● Mise sous tension progressive
Si possible, appliquer une tension inférieure à celle prévue et observer le comportement du circuit avant de l’alimenter complètement.

Le but est simple : éviter de “tout griller” en cas d’erreur.  
Indices d’alerte :
- échauffement,
- consommation anormale,
- LED trop forte ou comportement bizarre.

---

## V. Test et détection de pannes après assemblage

Une fois le circuit assemblé, il peut être nécessaire de procéder à des tests pour s’assurer de son bon fonctionnement et diagnostiquer des éventuelles pannes.

### ● Test de tension
Vérifier la présence des bonnes valeurs de tension aux points clés du circuit (par exemple, sur les broches d’un amplificateur).  
On compare à une valeur attendue (au moins un ordre de grandeur).

### ● Vérification du courant
S’assurer que les courants aux différentes branches du circuit sont dans les valeurs attendues.  
Un courant trop fort peut provoquer un échauffement ou une casse.

### ● Observation des signes de défauts
Échauffement excessif, absence de signal, ou consommation anormale de courant sont des indices de problème.  
Réflexe sécurité : si ça chauffe ou sent mauvais, **on coupe tout de suite**.

### ● Diagnostic de pannes courantes
○ Composants mal soudés ou dessoudés, souvent à cause de soudures froides.  
○ Court-circuit entre pistes ou composants mal orientés.  
○ Exemple : si une LED ne s’allume pas, tester le courant dans la branche pour vérifier la continuité et la polarité de la diode.

Méthode de diagnostic LED (simple et efficace) :
1) vérifier polarité LED  
2) vérifier résistance (valeur + connexion)  
3) vérifier continuité  
4) mesurer tension aux bornes LED  

---

## VI. Assemblage de circuits avec des composants CMS (Composants Montés en Surface)

Les CMS sont des composants très petits, soudés directement sur les pistes d’un circuit imprimé sans perçage. Leur montage nécessite une technique spécifique.

### ● Utilisation d’un fer à souder de précision ou d’une station de soudage à air chaud
Ces outils permettent de souder les petits composants sans les endommager.  
CMS = précision + outillage adapté.

### ● Application de pâte à souder
Pour les CMS, on utilise souvent une pâte d’étain appliquée sur les pastilles de soudure avant de chauffer.  
La pâte aide à maintenir le composant pendant le chauffage.

### ● Placement précis des composants
Les CMS sont placés avec une pince à épiler sur la pâte à souder, puis chauffés pour fixer chaque connexion.  
Le placement est critique : c’est petit et facile à décaler.

### ● Reflow et four de soudure
Dans l’industrie, on utilise un four qui chauffe toute la carte pour fixer les composants CMS en une seule étape.  
Le reflow est très utilisé pour la production en série.

---

## VII. Enfermement et protection des circuits assemblés

Une fois le montage terminé, les circuits doivent être protégés des conditions extérieures et des interférences électromagnétiques.

### ● Boîtiers et enclosures
Placer le circuit dans un boîtier adapté pour le protéger des poussières, des chocs et des variations d’humidité.  
Un boîtier améliore la sécurité et la durabilité.

### ● Fixation des composants
S’assurer que les composants et les connexions sont stables et que rien ne risque de se déplacer lors d’une utilisation.  
Il faut éviter que des fils tirent sur les soudures (sinon ça finit par casser).

### ● Blindage électromagnétique
Utiliser un boîtier métallique ou des rubans de blindage pour éviter les interférences, surtout dans les circuits de haute fréquence ou de précision.  
Le blindage aide à réduire les parasites.

### ● Application de vernis de protection
Un vernis isolant peut être appliqué sur la carte pour la protéger de l’oxydation et des courts-circuits.  
C’est utile en humidité/poussière, mais il faut garder en tête que cela peut compliquer la maintenance (accès aux soudures).

---

## VIII. Exemples pratiques d’assemblage de circuits

● Assemblage d’un circuit d’éclairage LED : les LEDs sont connectées avec des résistances pour contrôler le courant et sont montées sur un PCB ; le tout est protégé dans un boîtier transparent.  
La résistance protège la LED en limitant le courant.

● Construction d’un ampli audio : implique des composants polarisés (condensateurs électrolytiques, transistors) montés sur une carte, avec un soin particulier pour les soudures et le blindage pour éviter les parasites.  
En audio, le blindage peut être très utile pour limiter les bruits parasites.

● Fabrication d’un capteur de température : le capteur est monté avec un microcontrôleur et un régulateur de tension, le tout dans un boîtier étanche pour protéger le circuit des éléments extérieurs.  
On retrouve ici la logique : capteur → traitement → action (logique CIEL).

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
