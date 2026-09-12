# 🎮 ACTIVITÉ DE DÉCOUVERTE - U31 RÉSEAUX - SEMAINE 8

## 🎯 JEU DE RÔLE : "L'ANNUAIRE D'INTERNET"

---

## 📋 INFORMATIONS GÉNÉRALES

| **Élément** | **Détail** |
|-------------|------------|
| **Durée** | 30 minutes (5 min préparation + 15 min jeu + 10 min débriefing) |
| **Participants** | Groupes de 5 apprenants |
| **Objectif** | Comprendre le fonctionnement de la résolution DNS par la pratique |
| **Matériel** | Fiches de rôle (imprimées), chronomètre, tableau pour schématiser |

---

## 🎭 PRINCIPE DU JEU

**Situation :** Vous êtes sur Internet et vous voulez accéder au site `www.amazon.fr`. Mais votre navigateur ne connaît pas l'adresse IP de ce site ! Il doit interroger plusieurs "annuaires" (serveurs DNS) pour la trouver.

**Mission :** Simuler en groupe le parcours d'une requête DNS depuis votre navigateur jusqu'au serveur qui détient l'information.

---

## 👥 DISTRIBUTION DES RÔLES (5 personnes par groupe)

| **Rôle** | **Nombre** | **Mission** |
|----------|------------|------------|
| **Navigateur** | 1 | Tu veux accéder à `www.amazon.fr` mais tu ne connais pas son adresse IP |
| **DNS Local** | 1 | Tu es le premier contact du navigateur (comme un secrétaire) |
| **DNS Racine** | 1 | Tu connais les responsables des extensions `.fr`, `.com`, `.org`... |
| **DNS TLD (.fr)** | 1 | Tu connais les responsables des domaines comme `amazon`, `orange`, `lemonde`... |
| **Observateur** | 1 | Tu chronomètres et tu notes les échanges sur une feuille |

---

## 📜 FICHES DE RÔLE À DÉCOUPER

---

### 🌐 FICHE RÔLE 1 : NAVIGATEUR

**Qui es-tu ?**  
Tu es le **navigateur web** (Chrome, Firefox, Safari...). L'utilisateur vient de taper `www.amazon.fr` dans la barre d'adresse.

**Ton problème :**  
Tu ne connais **QUE** les adresses IP, pas les noms de domaine ! Pour afficher la page web, tu as besoin de l'adresse IP de `www.amazon.fr`.

**Ta mission :**  
1. Adresse-toi d'abord au **DNS Local** et demande-lui : *"Quelle est l'adresse IP de www.amazon.fr ?"*
2. Attends sa réponse
3. Si tu obtiens l'adresse IP, tu as gagné ! Crie : *"J'ai trouvé ! C'est l'IP : [adresse reçue]"*

**Ce que tu ne dois PAS faire :**  
- Ne contacte **jamais directement** le DNS Racine ou le DNS TLD
- Tu passes **toujours** par le DNS Local

---

### 🏠 FICHE RÔLE 2 : DNS LOCAL (Résolveur)

**Qui es-tu ?**  
Tu es le **serveur DNS local** (souvent celui de ton fournisseur d'accès Internet, ou celui de ton entreprise).

**Ton problème :**  
Le Navigateur te demande l'adresse IP de `www.amazon.fr`, mais tu ne la connais pas encore ! Par contre, tu sais qui pourrait t'aider.

**Ta mission :**  
1. Reçois la demande du **Navigateur** : *"Quelle est l'adresse IP de www.amazon.fr ?"*
2. Réponds-lui : *"Je ne sais pas, mais je vais me renseigner. Patiente."*
3. Demande au **DNS Racine** : *"Qui s'occupe des domaines .fr ?"*
4. Le DNS Racine te répond → Note sa réponse
5. Demande au **DNS TLD (.fr)** : *"Quelle est l'adresse IP de www.amazon.fr ?"*
6. Le DNS TLD te répond → Note la réponse
7. Retourne vers le **Navigateur** et donne-lui l'adresse IP : *"Voici l'adresse IP : [adresse obtenue]"*

**Important :**  
Tu es le **seul lien** entre le Navigateur et les autres serveurs DNS !

---

### 🌍 FICHE RÔLE 3 : DNS RACINE (Root DNS)

**Qui es-tu ?**  
Tu es un **serveur DNS racine**. Tu es au sommet de la hiérarchie DNS sur Internet. Il y en a 13 dans le monde entier (nommés de A à M).

**Ton problème :**  
Tu ne connais **pas** les adresses IP des sites web, mais tu connais les responsables des **extensions** (appelées TLD : Top Level Domains).

**Ta base de données :**  
- `.fr` → DNS TLD France
- `.com` → DNS TLD Commercial
- `.org` → DNS TLD Organisations
- `.uk` → DNS TLD Royaume-Uni
- ...et beaucoup d'autres !

**Ta mission :**  
1. Attends qu'on te contacte (normalement le **DNS Local**)
2. Quelqu'un te demande : *"Qui s'occupe des domaines .fr ?"*
3. Réponds : *"C'est le DNS TLD France qui gère les .fr. Va le voir."*

**Ce que tu ne dois PAS faire :**  
- Ne donne **jamais** directement une adresse IP de site web
- Tu ne connais que les responsables des extensions (TLD)

---

### 🇫🇷 FICHE RÔLE 4 : DNS TLD (.fr)

**Qui es-tu ?**  
Tu es le **serveur DNS TLD (Top Level Domain) France**. Tu gères tous les noms de domaine qui se terminent par `.fr`.

**Ton problème :**  
Tu connais les adresses IP des domaines en `.fr`, mais seulement si on te les demande correctement.

**Ta base de données :**  
- `www.amazon.fr` → **52.95.220.10**
- `www.lemonde.fr` → **195.154.120.50**
- `www.orange.fr` → **80.12.35.60**
- (et des millions d'autres !)

**Ta mission :**  
1. Attends qu'on te contacte (normalement le **DNS Local**, qui a été envoyé par le DNS Racine)
2. Quelqu'un te demande : *"Quelle est l'adresse IP de www.amazon.fr ?"*
3. Consulte ta base de données et réponds : *"L'adresse IP de www.amazon.fr est 52.95.220.10"*

**Important :**  
Tu ne réponds **que** pour les domaines en `.fr` ! Si on te demande un `.com`, réponds : *"Je ne gère pas les .com, demande au DNS Racine de t'orienter vers le DNS TLD .com"*

---

### 👁️ FICHE RÔLE 5 : OBSERVATEUR

**Qui es-tu ?**  
Tu es l'**observateur scientifique** de l'expérience. Tu ne participes pas au jeu, mais tu collectes les données.

**Ta mission :**  
1. **Chronomètre** le temps total entre la question du Navigateur et la réponse finale
2. **Note sur une feuille** les échanges dans l'ordre :
   - Qui parle à qui ?
   - Que dit chaque personne ?
3. **Compte le nombre d'étapes** avant que le Navigateur obtienne l'IP

**Exemple de prise de notes :**

| **Étape** | **De** | **Vers** | **Message** |
|-----------|--------|----------|-------------|
| 1 | Navigateur | DNS Local | "Quelle est l'IP de www.amazon.fr ?" |
| 2 | DNS Local | DNS Racine | "Qui s'occupe des .fr ?" |
| 3 | DNS Racine | DNS Local | "C'est le DNS TLD France" |
| ... | ... | ... | ... |

**À la fin du jeu :**  
- Annonce le temps total
- Lis à voix haute le déroulement des échanges
- Identifie l'étape la plus longue

---

## 🎬 DÉROULEMENT DU JEU (15 MIN)

### Étape 1 : Préparation (5 min)

1. **Formateur** : Constituez des groupes de 5 personnes
2. Distribuez les fiches de rôle (1 par personne)
3. Laissez 2-3 minutes aux apprenants pour lire leur fiche
4. Répondez aux questions de clarification

### Étape 2 : Simulation (10 min)

1. **Formateur** : "Top départ ! Le navigateur souhaite accéder à www.amazon.fr. Action !"
2. Les apprenants jouent leur rôle en s'interpellant oralement
3. L'observateur note tout et chronomètre
4. **Formateur** : Circulez entre les groupes pour observer (sans intervenir sauf blocage total)

### Étape 3 : Arrêt du jeu

- Dès que le Navigateur crie *"J'ai trouvé l'IP !"*, l'observateur arrête le chronomètre
- Si au bout de 10 min, un groupe est bloqué, interrompez et passez au débriefing

---

## 💬 DÉBRIEFING COLLECTIF (10 MIN)

### Questions à poser aux apprenants :

1. **"Que s'est-il passé dans votre groupe ?"**  
   → Laisser un observateur raconter le déroulement

2. **"Combien de temps a pris la résolution DNS ?"**  
   → Comparer les temps entre les groupes

3. **"Pourquoi le Navigateur ne peut-il pas contacter directement le DNS TLD .fr ?"**  
   → Faire émerger la notion de **hiérarchie** et d'**ordre** des requêtes

4. **"Quel était le rôle du DNS Local ?"**  
   → Faire comprendre qu'il est l'**intermédiaire obligatoire**

5. **"Que se passerait-il si le DNS Racine était en panne ?"**  
   → Introduire la notion de **redondance** (13 serveurs racine dans le monde)

### Schématisation au tableau

Le formateur dessine au tableau blanc le schéma suivant **pendant le débriefing** :

```
┌─────────────┐
│ NAVIGATEUR  │  "Je veux www.amazon.fr"
└──────┬──────┘
       │ 1️⃣ Demande
       ▼
┌─────────────┐
│ DNS LOCAL   │  "Je vais me renseigner"
└──────┬──────┘
       │ 2️⃣ Qui gère les .fr ?
       ▼
┌─────────────┐
│ DNS RACINE  │  "C'est le DNS TLD France"
└─────────────┘
       │ 3️⃣ Retour info
       ▼
┌─────────────┐
│ DNS LOCAL   │  "OK, je vais le contacter"
└──────┬──────┘
       │ 4️⃣ IP de www.amazon.fr ?
       ▼
┌──────────────┐
│ DNS TLD .fr  │  "C'est 52.95.220.10"
└──────────────┘
       │ 5️⃣ Retour IP
       ▼
┌─────────────┐
│ DNS LOCAL   │  "Voici l'IP : 52.95.220.10"
└──────┬──────┘
       │ 6️⃣ Transmission IP
       ▼
┌─────────────┐
│ NAVIGATEUR  │  "Merci ! Je peux afficher la page"
└─────────────┘
```

---

## 🎯 OBJECTIFS PÉDAGOGIQUES ATTEINTS

À l'issue de cette activité, les apprenants auront **découvert par eux-mêmes** :

✅ **Le DNS ne stocke pas toutes les adresses IP en un seul endroit**  
✅ **La hiérarchie DNS : Racine → TLD → Domaine**  
✅ **Le rôle central du DNS Local (résolveur)**  
✅ **Le processus en plusieurs étapes d'une résolution DNS**  
✅ **La nécessité d'avoir une organisation structurée pour gérer des millions de domaines**

---

## 💡 VARIANTES POSSIBLES

### Variante 1 : Ajouter le cache DNS

- Le **DNS Local** possède un carnet où il note les réponses
- Si le Navigateur demande une 2e fois `www.amazon.fr`, le DNS Local répond directement **sans interroger les autres**
- **Objectif** : Introduire la notion de **cache DNS** et de **gain de temps**

### Variante 2 : Simuler une panne

- Lors du 2e tour, le **DNS Racine** est "en panne" (il ne répond pas)
- Observer ce qui se passe et introduire la **redondance** (il existe plusieurs DNS Racines)

### Variante 3 : Domaine international

- Demander `www.amazon.com` au lieu de `.fr`
- Le DNS TLD .fr refuse de répondre
- Le DNS Local doit retourner voir le DNS Racine pour obtenir le contact du DNS TLD .com

---

## 🧩 ADAPTATION POUR DIFFÉRENTS PUBLICS

### Public SEGPA / Faible lecteur

- **Simplifier les fiches de rôle** : Réduire le texte, utiliser des pictogrammes
- **Faire un exemple collectif** avant de lancer les groupes
- **Accompagner** un groupe en difficulté en rejouant le rôle du DNS Local

### Public à l'aise

- **Ajouter un rôle supplémentaire** : DNS Autoritaire pour amazon.fr (6e personne)
- **Introduire les sous-domaines** : `www.amazon.fr` vs `images.amazon.fr`
- **Chronométrer** et demander d'optimiser le processus au 2e essai

---

## 📝 GRILLE D'OBSERVATION FORMATEUR

| **Critère** | **Observé** | **Commentaires** |
|-------------|-------------|------------------|
| Les rôles sont-ils bien compris ? | ☐ Oui ☐ Non | |
| Les apprenants respectent-ils la hiérarchie ? | ☐ Oui ☐ Non | |
| Le vocabulaire technique émerge-t-il spontanément ? | ☐ Oui ☐ Non | |
| Les apprenants en difficulté sont-ils aidés par leurs pairs ? | ☐ Oui ☐ Non | |
| Le débriefing permet-il de structurer les connaissances ? | ☐ Oui ☐ Non | |

---

## 🚀 TRANSITION VERS LE COURS MAGISTRAL

**Phrase de transition du formateur :**

> *"Bravo pour cette simulation ! Vous venez de découvrir comment fonctionne le DNS. Maintenant, on va voir les **vraies commandes** que les professionnels utilisent pour interroger ces serveurs DNS : `nslookup` et `dig`. Vous allez devenir des experts de la résolution DNS !"*

---

**📅 Activité conçue le :** 25/02/2026  
**✍️ Auteur :** Équipe pédagogique CFA  
**🎮 Testée avec :** Promo 2024-2027 (retours très positifs !)  
**🔄 Prochaine révision :** Juin 2026

---

**🎉 Amusez-vous bien et apprenez en jouant ! Le DNS n'aura plus de secrets pour vous.**
