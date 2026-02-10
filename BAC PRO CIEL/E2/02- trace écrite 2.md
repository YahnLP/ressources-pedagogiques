---
title: "E2 - Pack 02 - Fiche de cours élève - Schémas électroniques et plans de câblage"
module: "BAC PRO CIEL - E2"
version: "1.0"
---

# Schémas électroniques et plans de câblage

## 🎯 Objectifs (à atteindre pour l'épreuve E2)
À la fin de cette fiche, je suis capable de :

| Je sais… | Exemple attendu en E2 |
|---|---|
| **Expliquer** ce qu’est un schéma électronique | “Ce n’est pas une photo : c’est une représentation **logique** du circuit.” |
| **Lire** un schéma électronique | “Je repère **Vcc** et **GND**, je suis les connexions, je vérifie les **valeurs** et les **polarités**.” |
| **Différencier** schéma de principe / schéma de câblage / schéma de bloc | “Bloc = fonction / principe = logique / câblage = placement réel.” |
| **Passer** du schéma au montage (breadboard / PCB) | “Une ligne sur le schéma correspond à un **fil** (breadboard) ou une **piste** (PCB).” |
| **Éviter** des erreurs classiques | “Croisement sans point ≠ connexion ; LED/condensateur polarisé dans le bon sens.” |

---

## 🔑 Idée essentielle avant de commencer
Un schéma électronique, c’est comme un **plan** : il sert à **comprendre**, **câbler**, puis **dépanner**.

➡️ Très important : un schéma électronique **n’est pas une photo**.  
C’est une représentation **logique** : elle montre surtout **qui est relié à qui** (les connexions), pas l’apparence réelle du montage.

<p align="center">
  <img src="./images/schema_vs_photo.png" alt="Comparaison entre un schéma électronique (symboles) et un montage réel sur breadboard" width="85%"><br>
  <em>Illustration attendue : comparaison visuelle entre un schéma simple (symboles) et un montage réel sur breadboard.</em>
</p>

---

## I. Schémas électroniques : définition et rôle

Les schémas électroniques sont des représentations graphiques des circuits électroniques. Ils indiquent la disposition des composants (résistances, condensateurs, transistors, etc.) et les connexions électriques entre eux.

On utilise un schéma électronique pour trois raisons principales :

| Rôle du schéma électronique | Ce que ça permet de faire |
|---|---|
| **Comprendre** | Voir rapidement comment le circuit fonctionne (logique des connexions) |
| **Réaliser** | Câbler correctement un montage (transformer le schéma en montage réel) |
| **Diagnostiquer** | Chercher une panne (connexion oubliée, polarité, mauvaise valeur, GND manqué) |

Les composants sont représentés par des **symboles standardisés**. Ces symboles sont “universels” : on peut les lire quel que soit le pays ou le logiciel utilisé.  
Parfois, un même composant peut avoir deux symboles selon les conventions (par exemple une résistance en “zigzag” ou en “rectangle”) : l’idée reste strictement la même.

<p align="center">
  <img src="./images/symboles_de_base.png" alt="Tableau de symboles électroniques de base : R, C, diode, LED, transistor, GND, Vcc" width="90%"><br>
  <em>Illustration attendue : tableau de symboles (R, C, diode, LED, transistor, GND, Vcc).</em>
</p>

En E2, on te demandera souvent la chaîne complète :  
**Lire le schéma → câbler le montage → expliquer une panne (ou justifier un choix).**

---

## II. Les éléments d'un schéma électronique : lecture et compréhension

La lecture d'un schéma électronique repose sur l’identification de plusieurs éléments spécifiques.

### ✅ Méthode simple (à appliquer à chaque fois)
Pour lire un schéma sans te perdre, tu peux suivre cet ordre :

1) **Alimentation** : je repère **Vcc** et **GND**  
2) **Connexions** : je suis les lignes (je vérifie qui est relié à qui)  
3) **Polarités / orientation** : LED, diode, condensateur polarisé… (sens obligatoire)  
4) **Valeurs** : Ω, kΩ, µF, nF… (une mauvaise valeur peut empêcher le fonctionnement)

### ● Composants
Chaque composant a un symbole unique et, souvent, une valeur inscrite à côté (ex : résistance de 220 Ω, condensateur de 100 µF).  
Ces valeurs sont indispensables : une résistance avec une mauvaise valeur peut, par exemple, griller une LED ou empêcher un transistor de commuter.

**Unités à reconnaître rapidement :**
- Ω, kΩ (résistances)
- µF, nF (condensateurs)

### ● Connexions (lignes)
Les lignes relient les composants et montrent le chemin électrique.  
Dans un montage réel :
- une ligne du schéma correspond à un **fil** sur une breadboard,
- ou à une **piste** sur un PCB.

Astuce très simple : tu peux “suivre avec ton doigt” une ligne sur le schéma pour comprendre le trajet.

#### ○ Croisement vs jonction (piège très fréquent)
C’est une des erreurs les plus courantes :

- Si deux lignes se croisent **sans point**, ce n’est **pas connecté**.
- Si un **point** est dessiné, c’est une **connexion électrique**.

<p align="center">
  <img src="./images/croisement_jonction.png" alt="Différence entre un croisement sans point (pas connecté) et une jonction avec point (connecté)" width="80%"><br>
  <em>Illustration attendue : 2 schémas : (1) croisement sans point (pas connecté), (2) croisement avec point (connecté).</em>
</p>

Pour mémoriser, tu peux utiliser ce mini-tableau :

| Situation | Sur le schéma | Résultat |
|---|---|---|
| Croisement **sans point** | lignes qui se croisent | **pas connecté** |
| Jonction **avec point** | point sur la rencontre | **connecté** |

### ● Sources d’alimentation : Vcc et GND
Les sources d’alimentation sont souvent représentées par :
- **Vcc** : tension positive (par exemple +5V)
- **GND** : masse / 0V

Beaucoup de pannes viennent d’un oubli simple : **GND manqué** → le circuit ne se ferme pas → rien ne fonctionne.  
Dans un circuit, le courant “revient” au GND : c’est ce retour qui ferme la boucle.

---

## III. Types de schémas électroniques

Il existe plusieurs types de schémas. Ils ne servent pas au même moment.

### 📌 À retenir (très utile)
- **Schéma de bloc** : on comprend la **fonction** (architecture)
- **Schéma de principe** : on comprend la **logique** (qui est relié à qui)
- **Schéma de câblage / plan de câblage** : on fait le **montage réel** (placement)

| Type | Ce qu’on voit | À quoi ça sert |
|---|---|---|
| **Schéma de principe** (ou schéma fonctionnel) | composants principaux + connexions logiques | comprendre le fonctionnement |
| **Schéma de câblage** (ou plan de câblage) | placement physique + fils/pistes | monter sans se tromper |
| **Schéma de bloc** | blocs “fonction” | comprendre l’architecture globale |

### ● Schéma de principe (ou schéma fonctionnel)
Il présente les composants principaux et leurs connexions de manière simple pour montrer le fonctionnement général du circuit.  
C’est celui qu’on utilise le plus au début pour comprendre “qui est relié à qui”.

Exemple : une alimentation peut montrer une diode (redressement), un condensateur (filtrage) et un régulateur de tension (régulation). On voit l’idée générale : transformer et stabiliser une tension.

### ● Schéma de câblage (ou plan de câblage)
Il montre en détail où chaque fil et composant doit être placé physiquement, souvent sur une plaque de montage ou un PCB.  
C’est celui qu’on suit pour monter **sans se tromper**, car il ressemble à une “carte” du montage.

En maintenance, il est très utile : il permet de repérer où mesurer et où chercher une erreur.

### ● Schéma de bloc
C’est une version simplifiée où les parties complexes du circuit sont représentées par des blocs, indiquant seulement la fonction générale sans entrer dans les détails des composants internes.

<p align="center">
  <img src="./images/schema_de_bloc_exemple.png" alt="Schéma de bloc : capteur → traitement → actionneur" width="90%"><br>
  <em>Illustration attendue : schéma bloc simple : “capteur” → “traitement” → “actionneur”.</em>
</p>

---

## IV. Plan de câblage : principes et réalisation

Le plan de câblage est une représentation qui détaille l’implantation physique des composants et les connexions électriques sur un **PCB** ou une **breadboard**.

### ● PCB et breadboard : ne pas confondre
- **PCB** = circuit imprimé (pistes cuivre) → version “finale” et propre
- **Breadboard** = plaque d’essai → montage rapide sans soudure

Sur breadboard, la difficulté principale est de comprendre quelles lignes sont déjà connectées (rails + rangées).  
Si on ne comprend pas la breadboard, on peut “câbler” sans le savoir des points qui ne sont pas reliés, ou relier ce qu’il ne faut pas.

### ● Organisation des composants
Chaque composant doit être placé selon le plan et relié via des connexions spécifiques (fils, pistes en cuivre).  
Sur PCB, l’orientation et la position sont pensées pour optimiser l’espace et limiter les interférences (éviter que des signaux se parasitent).

### ● Connexions électriques et points de test
Le plan montre les fils de connexion, les soudures et parfois des **points de test**.  
Un point de test, c’est un endroit prévu pour mesurer facilement au multimètre ou à l’oscilloscope.

Sur breadboard, on peut aussi prévoir des “zones” d’alimentation : par exemple relier le rail +5V à plusieurs zones du montage.

### ● Polarité et orientation des composants
Certains composants doivent être placés dans le bon sens :
- diodes, LED
- condensateurs polarisés

Une LED inversée ne s’allumera pas.  
Un condensateur polarisé inversé peut s’abîmer et provoquer une panne (voire un court-circuit).

<p align="center">
  <img src="./images/polarites_led_condo.png" alt="Polarité LED et condensateur : anode/cathode et repère + / bande -" width="90%"><br>
  <em>Illustration attendue : LED avec anode/cathode + condensateur avec bande “-” et repère +.</em>
</p>

---

## V. Les étapes pour réaliser un schéma électronique et un plan de câblage

La conception d'un schéma et d'un plan de câblage passe par plusieurs étapes structurées.  
Tu peux retenir la logique professionnelle : **besoin → schéma → vérification → câblage → test**.

| Étape | Ce que je fais | Ce que je dois vérifier |
|---|---|---|
| 1. Choix des composants et spécifications | Je choisis les composants et leurs valeurs | valeurs (Ω, µF…), compatibilité tension/courant |
| 2. Conception du schéma de principe | Je dessine la logique (connexions) | “qui est relié à qui” |
| 3. Vérification des connexions | Je contrôle le trajet électrique | trajet du Vcc vers le GND, jonctions/points |
| 4. Plan de câblage | Je place physiquement les composants | orientation, distances, fils pas trop longs |
| 5. Réalisation du prototype | Je câble sur breadboard (ou PCB), puis je teste | polarités, valeurs, alimentation en dernier |

Astuce atelier importante : **je branche l’alimentation en dernier**.  
Comme ça, je vérifie d’abord que tout est bien câblé, et j’évite de griller un composant en cas d’erreur.

---

## VI. Exemples d’applications des schémas et plans de câblage

### ● Schéma de câblage pour une alimentation régulée
On peut repérer trois fonctions :
1) **Redresser** (pont de diodes)  
2) **Filtrer** (condensateur de filtrage)  
3) **Réguler** (régulateur de tension)

Le schéma de principe montre les connexions, et le plan de câblage précise la disposition sur une carte, pour minimiser les interférences et dissiper la chaleur (certains composants chauffent, comme un régulateur).

### ● Montage d'un détecteur de lumière (LDR)
Un circuit simple qui utilise une photorésistance (LDR), un transistor et une résistance.  
Très souvent, le principe est :
- LDR + résistance = diviseur de tension
- la tension obtenue sert à commander un transistor (donc un actionneur : LED, relais, etc.)

Le schéma montre les connexions, tandis que le plan de câblage indique la disposition pour une bonne sensibilité lumineuse et une réponse rapide.

---

## VII. Logiciels de conception de schémas et plans de câblage

Les logiciels de conception de circuits facilitent le travail en offrant des outils pour dessiner, tester et organiser les composants.  
En formation, ils permettent souvent de simuler avant de câbler : cela évite des erreurs et fait gagner du temps.

| Logiciel | À quoi il sert | Niveau |
|---|---|---|
| **KiCad** | création de schémas + PCB (open-source) | intermédiaire / avancé |
| **Eagle** | création de PCB et schémas de câblage | professionnel |
| **Tinkercad circuits** | concevoir et tester des circuits en ligne | débutant |

Tinkercad circuits est pratique pour débuter : on “voit” le montage et on peut tester sans risque.

---

## VIII. Les erreurs courantes dans les schémas et plans de câblage et comment les éviter

Les pannes en électronique viennent souvent d’erreurs simples. L’objectif est de les repérer vite.

| Erreur fréquente | Effet typique | Comment l’éviter |
|---|---|---|
| Omission de connexions | le circuit ne fonctionne pas | vérifier que le trajet revient bien au **GND** |
| Croisement mal lu (sans point) | partie du circuit “isolée” | repérer les **points de jonction** |
| Erreurs de polarité (LED, condensateur polarisé) | LED éteinte / composant abîmé | vérifier l’orientation avant d’alimenter |
| Valeur inadéquate | surchauffe, instabilité, LED grillée | relire les unités (Ω, kΩ, µF, nF) |
| Court-circuit / pistes trop proches | alimentation qui chute, chauffe, panne | sur breadboard : éviter fils qui se touchent, rails +/– bien séparés |

---

# Tableau récapitulatif (vocabulaire E2)

| Terme | Définition simple | À quoi ça sert en atelier ? |
|---|---|---|
| Symbole | dessin normalisé d’un composant | reconnaître vite un composant |
| Connexion | liaison électrique entre points | “le courant peut passer” |
| Point de jonction | point qui indique une connexion | éviter l’erreur croisement |
| Vcc | tension positive (ex : +5V) | alimenter le circuit |
| GND | masse / 0V | fermer le circuit |
| Schéma de principe | représentation logique | comprendre le fonctionnement |
| Plan de câblage | représentation physique | monter sans erreur |
| Schéma de bloc | fonctions en blocs | comprendre l’architecture |
| PCB | circuit imprimé | version finale d’un montage |
| Breadboard | plaque d’essai | prototypage rapide |
