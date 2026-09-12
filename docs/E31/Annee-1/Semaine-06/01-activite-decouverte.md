# 🎮 ACTIVITÉ DE DÉCOUVERTE - U31 RÉSEAUX - SEMAINE 6

## 🎯 JEU DE RÔLE : "LE FACTEUR DU RÉSEAU"

---

## 📋 INFORMATIONS GÉNÉRALES

| **Élément** | **Détail** |
|-------------|------------|
| **Durée** | 35 minutes (5 min préparation + 20 min jeu + 10 min débriefing) |
| **Participants** | Groupes de 6 apprenants |
| **Objectif** | Comprendre le routage IP et la table de routage par la pratique |
| **Matériel** | Fiches de rôle, 3 enveloppes (paquets), tableau, marqueurs |

---

## 🎭 PRINCIPE DU JEU

**Situation :** Vous êtes des **routeurs** dans un réseau informatique. Votre mission est de transmettre des **paquets IP** (représentés par des enveloppes) d'un ordinateur source vers un ordinateur destination.

**Problème :** Chaque routeur ne connaît que les réseaux directement connectés à lui (sa "table de routage"). Comment acheminer les paquets correctement ?

**Mission :** Faire parvenir 3 paquets à leur destination en suivant les règles de routage !

---

## 🗺️ PLAN DU RÉSEAU

Voici le réseau que vous allez simuler :

```
        RÉSEAU A              RÉSEAU B              RÉSEAU C
      (192.168.1.0)        (192.168.2.0)        (192.168.3.0)
            │                    │                    │
            │                    │                    │
    ┌───────────────┐    ┌───────────────┐    ┌───────────────┐
    │   PC SOURCE   │    │  ROUTEUR R2   │    │ PC DESTINATION│
    │ 192.168.1.10  │────│ .1.1  -  .2.1 │────│  192.168.3.10 │
    └───────────────┘    └───────────────┘    └───────────────┘
            │                    │
            │                    │
    ┌───────────────┐            │
    │  ROUTEUR R1   │────────────┘
    │ .1.254 - .2.254│
    └───────────────┘
```

**Légende :**
- **PC Source** : L'ordinateur qui envoie le paquet
- **Routeur R1** : Connecté aux réseaux A et B
- **Routeur R2** : Connecté aux réseaux B et C
- **PC Destination** : L'ordinateur qui doit recevoir le paquet

---

## 👥 DISTRIBUTION DES RÔLES (6 personnes par groupe)

| **Rôle** | **Nombre** | **Mission** |
|----------|------------|------------|
| **PC Source** | 1 | Tu crées les paquets et les envoies sur le réseau |
| **Routeur R1** | 1 | Tu routes les paquets entre les réseaux A et B |
| **Routeur R2** | 1 | Tu routes les paquets entre les réseaux B et C |
| **PC Destination** | 1 | Tu reçois les paquets qui t'sont destinés |
| **Observateur** | 1 | Tu notes les décisions prises par chaque routeur |
| **Chronométreur** | 1 | Tu mesures le temps d'acheminement de chaque paquet |

---

## 📜 FICHES DE RÔLE À DÉCOUPER

---

### 💻 FICHE RÔLE 1 : PC SOURCE (192.168.1.10)

**Qui es-tu ?**  
Tu es l'**ordinateur émetteur** situé sur le **réseau A** (192.168.1.0/24). Tu souhaites envoyer des messages vers d'autres machines.

**Ta configuration réseau :**
- **Adresse IP** : 192.168.1.10
- **Masque** : 255.255.255.0 (réseau local = 192.168.1.0)
- **Passerelle par défaut** : 192.168.1.254 (Routeur R1)

**Ta table de routage (simplifiée) :**

| **Destination** | **Passerelle** | **Décision** |
|----------------|---------------|--------------|
| 192.168.1.0/24 | Direct | Envoyer directement sur le réseau local |
| 0.0.0.0/0 | 192.168.1.254 | Envoyer à la passerelle par défaut (R1) |

**Ta mission :**
1. Tu as **3 enveloppes** (paquets) à envoyer avec ces adresses de destination :
   - **Paquet 1** : vers 192.168.1.50 (même réseau que toi)
   - **Paquet 2** : vers 192.168.2.20 (réseau B)
   - **Paquet 3** : vers 192.168.3.10 (réseau C)

2. Pour chaque paquet, consulte ta table de routage et décide :
   - **Destination dans ton réseau local ?** → Livre directement
   - **Destination dans un autre réseau ?** → Envoie à ta passerelle (R1)

3. Remets physiquement l'enveloppe au destinataire ou à ta passerelle

**Règle importante :**  
Tu ne peux envoyer qu'à :
- Un PC de ton réseau local (192.168.1.x)
- Ou à ta passerelle par défaut (192.168.1.254 = R1)

---

### 🔀 FICHE RÔLE 2 : ROUTEUR R1 (192.168.1.254 / 192.168.2.254)

**Qui es-tu ?**  
Tu es le **Routeur R1**, tu interconnectes les **réseaux A et B**. Tu as deux "pattes réseau" (deux interfaces).

**Tes interfaces réseau :**
- **Interface 1** : 192.168.1.254 (connectée au réseau A)
- **Interface 2** : 192.168.2.254 (connectée au réseau B)

**Ta table de routage :**

| **Destination** | **Passerelle** | **Interface** | **Décision** |
|----------------|---------------|---------------|--------------|
| 192.168.1.0/24 | Direct | Interface 1 | Réseau directement connecté |
| 192.168.2.0/24 | Direct | Interface 2 | Réseau directement connecté |
| 0.0.0.0/0 | 192.168.2.1 | Interface 2 | Envoyer vers R2 (passerelle par défaut) |

**Ta mission :**
1. Tu reçois des paquets (enveloppes) de différentes sources
2. Pour chaque paquet, regarde l'**adresse de destination** écrite dessus
3. Consulte ta table de routage :
   - **Destination = 192.168.1.x** → Envoie sur l'interface 1 (réseau A)
   - **Destination = 192.168.2.x** → Envoie sur l'interface 2 (réseau B)
   - **Destination = autre** → Envoie à ta passerelle par défaut (R2 = 192.168.2.1)
4. Remets l'enveloppe au prochain routeur ou au destinataire final

**Règle importante :**  
Tu ne peux envoyer un paquet que vers :
- Un réseau directement connecté à toi (A ou B)
- Ou ta passerelle par défaut (R2)

**Phrase à dire à voix haute à chaque décision :**  
*"Je reçois un paquet pour [adresse]. D'après ma table de routage, je l'envoie à [destinataire]."*

---

### 🔀 FICHE RÔLE 3 : ROUTEUR R2 (192.168.2.1 / 192.168.3.1)

**Qui es-tu ?**  
Tu es le **Routeur R2**, tu interconnectes les **réseaux B et C**. Tu as deux "pattes réseau".

**Tes interfaces réseau :**
- **Interface 1** : 192.168.2.1 (connectée au réseau B)
- **Interface 2** : 192.168.3.1 (connectée au réseau C)

**Ta table de routage :**

| **Destination** | **Passerelle** | **Interface** | **Décision** |
|----------------|---------------|---------------|--------------|
| 192.168.2.0/24 | Direct | Interface 1 | Réseau directement connecté |
| 192.168.3.0/24 | Direct | Interface 2 | Réseau directement connecté |
| 192.168.1.0/24 | 192.168.2.254 | Interface 1 | Route vers réseau A via R1 |

**Ta mission :**
1. Tu reçois des paquets (enveloppes) de différentes sources
2. Pour chaque paquet, regarde l'**adresse de destination** écrite dessus
3. Consulte ta table de routage :
   - **Destination = 192.168.2.x** → Envoie sur l'interface 1 (réseau B)
   - **Destination = 192.168.3.x** → Envoie sur l'interface 2 (réseau C)
   - **Destination = 192.168.1.x** → Envoie vers R1 (192.168.2.254)
4. Remets l'enveloppe au prochain routeur ou au destinataire final

**Règle importante :**  
Tu ne peux envoyer un paquet que vers :
- Un réseau directement connecté à toi (B ou C)
- Ou vers R1 pour atteindre le réseau A

**Phrase à dire à voix haute à chaque décision :**  
*"Je reçois un paquet pour [adresse]. D'après ma table de routage, je l'envoie à [destinataire]."*

---

### 💻 FICHE RÔLE 4 : PC DESTINATION (192.168.3.10)

**Qui es-tu ?**  
Tu es un **ordinateur récepteur** situé sur le **réseau C** (192.168.3.0/24). Tu attends de recevoir des paquets.

**Ta configuration réseau :**
- **Adresse IP** : 192.168.3.10
- **Masque** : 255.255.255.0 (réseau local = 192.168.3.0)
- **Passerelle par défaut** : 192.168.3.1 (Routeur R2)

**Ta mission :**
1. Attendre de recevoir des paquets (enveloppes)
2. Quand tu reçois une enveloppe, vérifier que l'adresse de destination correspond à ton IP (192.168.3.10)
3. Si oui, crier : *"Paquet reçu ! Je suis bien 192.168.3.10 !"*
4. Si l'adresse ne correspond pas, dire : *"Erreur ! Ce paquet n'est pas pour moi !"*

**Important :**  
Tu ne fais **rien d'autre** que recevoir les paquets. Tu ne routes pas, tu ne transfères pas.

---

### 👁️ FICHE RÔLE 5 : OBSERVATEUR

**Qui es-tu ?**  
Tu es l'**observateur scientifique** de l'expérience. Tu ne participes pas au jeu, mais tu collectes les données.

**Ta mission :**
1. **Note sur une feuille** le parcours de chaque paquet :

| **Paquet** | **Destination** | **Chemin emprunté** | **Réussi ?** |
|-----------|----------------|---------------------|--------------|
| 1 | 192.168.1.50 | PC Source → ? → ? | ☐ Oui ☐ Non |
| 2 | 192.168.2.20 | PC Source → ? → ? | ☐ Oui ☐ Non |
| 3 | 192.168.3.10 | PC Source → ? → ? | ☐ Oui ☐ Non |

2. **Identifie les décisions clés :**
   - Pourquoi le Paquet 1 n'a pas eu besoin de routeur ?
   - Combien de routeurs le Paquet 3 a-t-il traversés ?

3. **Repère les erreurs éventuelles :**
   - Un routeur a-t-il envoyé un paquet au mauvais endroit ?
   - Un paquet est-il arrivé à la mauvaise destination ?

**À la fin du jeu :**
- Présente le parcours de chaque paquet au groupe
- Explique quelle route a été empruntée

---

### ⏱️ FICHE RÔLE 6 : CHRONOMÉTREUR

**Qui es-tu ?**  
Tu es le **chronométreur** de l'expérience. Tu mesures les temps d'acheminement.

**Ta mission :**
1. **Chronomètre chaque paquet** :
   - Démarre le chrono quand le PC Source prend l'enveloppe
   - Arrête le chrono quand le destinataire final reçoit l'enveloppe

2. **Note les temps :**

| **Paquet** | **Destination** | **Temps** |
|-----------|----------------|-----------|
| 1 | 192.168.1.50 | ____ secondes |
| 2 | 192.168.2.20 | ____ secondes |
| 3 | 192.168.3.10 | ____ secondes |

3. **Analyse les résultats :**
   - Quel paquet est arrivé le plus vite ? Pourquoi ?
   - Quel paquet a mis le plus de temps ? Pourquoi ?

**À la fin du jeu :**
- Annonce les temps pour chaque paquet
- Explique pourquoi certains paquets sont plus rapides que d'autres

---

## 🎬 DÉROULEMENT DU JEU (20 MIN)

### Étape 1 : Préparation (5 min)

1. **Formateur** : Constituez des groupes de 6 personnes
2. Distribuez les fiches de rôle (1 par personne)
3. Distribuez 3 enveloppes au PC Source avec les adresses de destination écrites dessus :
   - Enveloppe 1 : **Destination : 192.168.1.50**
   - Enveloppe 2 : **Destination : 192.168.2.20**
   - Enveloppe 3 : **Destination : 192.168.3.10**
4. Laissez 2-3 minutes aux apprenants pour lire leur fiche
5. Répondez aux questions de clarification

### Étape 2 : Simulation Paquet 1 (5 min) - LE PLUS FACILE

**Formateur** : *"Top départ pour le Paquet 1 ! Destination : 192.168.1.50"*

**Résultat attendu :**
- Le PC Source consulte sa table de routage
- Il voit que 192.168.1.50 est dans son réseau local (192.168.1.0/24)
- Il livre **directement** l'enveloppe (pas de routeur nécessaire)

**But pédagogique :** Comprendre qu'on ne passe pas par un routeur si la destination est locale.

### Étape 3 : Simulation Paquet 2 (7 min) - DIFFICULTÉ MOYENNE

**Formateur** : *"Top départ pour le Paquet 2 ! Destination : 192.168.2.20"*

**Résultat attendu :**
- Le PC Source consulte sa table de routage
- Il voit que 192.168.2.20 est dans un autre réseau
- Il envoie à sa passerelle par défaut : **R1 (192.168.1.254)**
- R1 consulte sa table de routage
- Il voit que 192.168.2.0/24 est directement connecté (interface 2)
- R1 livre l'enveloppe au destinataire (192.168.2.20)

**But pédagogique :** Comprendre le rôle de la passerelle par défaut et du routage direct.

### Étape 4 : Simulation Paquet 3 (8 min) - LE PLUS COMPLEXE

**Formateur** : *"Top départ pour le Paquet 3 ! Destination : 192.168.3.10 (PC Destination)"*

**Résultat attendu :**
- Le PC Source consulte sa table de routage
- Il envoie à sa passerelle par défaut : **R1**
- R1 consulte sa table de routage
- Il voit que 192.168.3.0 n'est pas directement connecté
- Il envoie à **sa** passerelle par défaut : **R2 (192.168.2.1)**
- R2 consulte sa table de routage
- Il voit que 192.168.3.0/24 est directement connecté (interface 2)
- R2 livre l'enveloppe au **PC Destination (192.168.3.10)**

**But pédagogique :** Comprendre qu'un paquet peut traverser plusieurs routeurs (routage multi-sauts).

---

## 💬 DÉBRIEFING COLLECTIF (10 MIN)

### Questions à poser aux apprenants :

**1. "Pourquoi le Paquet 1 n'a pas eu besoin de routeur ?"**  
→ Réponse attendue : "Parce que la destination était dans le même réseau que la source"

**2. "Qu'est-ce qu'une passerelle par défaut ? À quoi ça sert ?"**  
→ Réponse attendue : "C'est la porte de sortie du réseau local. Quand on ne sait pas où envoyer un paquet, on l'envoie à la passerelle par défaut"

**3. "Combien de routeurs le Paquet 3 a-t-il traversés ?"**  
→ Réponse attendue : "Deux routeurs : R1 et R2"

**4. "Comment un routeur décide-t-il où envoyer un paquet ?"**  
→ Réponse attendue : "Il consulte sa table de routage qui lui dit quel chemin prendre pour chaque destination"

**5. "Que se passerait-il si R1 n'avait pas de passerelle par défaut configurée ?"**  
→ Réponse attendue : "Le paquet serait bloqué, car R1 ne saurait pas où envoyer les paquets pour les réseaux qu'il ne connaît pas"

### Schématisation au tableau

Le formateur dessine au tableau blanc le schéma suivant **pendant le débriefing** :

```
PAQUET 1 : Livraison locale (pas de routeur)
─────────────────────────────────────────
PC Source (192.168.1.10) ──► 192.168.1.50
         (même réseau)


PAQUET 2 : 1 routeur
────────────────────────
PC Source (192.168.1.10) ──► R1 ──► 192.168.2.20
         Passerelle         Réseau B


PAQUET 3 : 2 routeurs (multi-sauts)
───────────────────────────────────
PC Source (192.168.1.10) ──► R1 ──► R2 ──► PC Destination (192.168.3.10)
         Passerelle          Passerelle      Réseau C
```

---

## 🎯 OBJECTIFS PÉDAGOGIQUES ATTEINTS

À l'issue de cette activité, les apprenants auront **découvert par eux-mêmes** :

✅ **Un routeur interconnecte des réseaux différents**  
✅ **Chaque routeur possède une table de routage**  
✅ **La passerelle par défaut est la "porte de sortie" d'un réseau**  
✅ **Un paquet peut traverser plusieurs routeurs avant d'arriver à destination**  
✅ **Le routage se fait "de proche en proche" (hop by hop)**  
✅ **Les réseaux directement connectés ne nécessitent pas de routage supplémentaire**  

---

## 💡 VARIANTES POSSIBLES

### Variante 1 : Panne de routeur

- Lors d'un 2e essai, **R1 est en panne** (il ne joue plus)
- Observer ce qui se passe : le paquet ne peut plus être acheminé
- **Objectif** : Comprendre l'importance de la **redondance** (routes alternatives)

### Variante 2 : Route spécifique

- Ajouter une **route spécifique** dans R1 : "Pour aller vers 192.168.3.0, passe directement par R2"
- Comparer avec la route par défaut
- **Objectif** : Différencier route spécifique vs route par défaut

### Variante 3 : Métrique (coût)

- Créer deux chemins possibles vers la même destination
- Donner un "coût" à chaque route (ex : R1→R2 = coût 1, R1→R3→R2 = coût 2)
- Le routeur choisit la route avec le coût le plus faible
- **Objectif** : Introduction à la notion de **métrique**

---

## 🧩 ADAPTATION POUR DIFFÉRENTS PUBLICS

### Public SEGPA / Faible lecteur

- **Simplifier les fiches de rôle** : Moins de texte, plus de schémas visuels
- **Réduire à 2 paquets** au lieu de 3 (supprimer le plus complexe)
- **Accompagner un groupe** en jouant le rôle d'un routeur avec eux

### Public à l'aise

- **Ajouter un 4e réseau** (réseau D) et un 3e routeur (R3)
- **Introduire des routes spécifiques** (pas seulement la route par défaut)
- **Chronométrer et optimiser** : "Comment faire arriver le paquet plus vite ?"

---

## 📝 GRILLE D'OBSERVATION FORMATEUR

| **Critère** | **Observé** | **Commentaires** |
|-------------|-------------|------------------|
| Les routeurs consultent-ils bien leur table de routage ? | ☐ Oui ☐ Non | |
| Le PC Source identifie-t-il correctement sa passerelle ? | ☐ Oui ☐ Non | |
| Les apprenants comprennent-ils la notion de "réseau local" ? | ☐ Oui ☐ Non | |
| Le débriefing permet-il de structurer les connaissances ? | ☐ Oui ☐ Non | |
| Les apprenants en difficulté sont-ils aidés par leurs pairs ? | ☐ Oui ☐ Non | |

---

## 🚀 TRANSITION VERS LE COURS MAGISTRAL

**Phrase de transition du formateur :**

> *"Excellent travail ! Vous venez de simuler le routage IP. Vous avez compris comment les routeurs prennent leurs décisions grâce à leur table de routage. Maintenant, on va voir comment afficher et lire la **vraie** table de routage de votre ordinateur avec les commandes `route print` et `ip route`. Vous allez devenir des experts du routage !"*

---

**📅 Activité conçue le :** 25/02/2026  
**✍️ Auteur :** Équipe pédagogique CFA  
**🎮 Testée avec :** Promo 2023-2026 (retours très positifs !)  
**🔄 Prochaine révision :** Juin 2026

---

**🎉 Amusez-vous bien et apprenez en jouant ! Le routage n'aura plus de secrets pour vous.**
