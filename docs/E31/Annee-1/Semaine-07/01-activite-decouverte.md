# ACTIVITÉ DÉCOUVERTE - U31 Réseaux Informatiques
## Semaine 7 - "La Poste aux Adresses" : Comprendre le DHCP par le jeu de rôle

---

## 🎯 OBJECTIFS DE L'ACTIVITÉ

### Objectifs pédagogiques

- **Comprendre intuitivement** le rôle du protocole DHCP (distribution automatique d'adresses)
- **Découvrir** le processus DORA (Discover, Offer, Request, Acknowledge) de manière concrète
- **Identifier** les avantages du DHCP vs. attribution manuelle
- **Expérimenter** les notions de bail, release, et renew
- **Anticiper** les problèmes courants (pool saturé, serveur injoignable)

### Compétences transversales

- Expression orale (jouer un rôle)
- Travail collaboratif
- Observation et analyse
- Prise de notes structurée

---

## ⏱️ DURÉE ET ORGANISATION

| **Élément** | **Détail** |
|-------------|------------|
| **Durée totale** | 25 minutes |
| **Modalité** | Jeu de rôle collectif + observation |
| **Effectif** | 12-16 apprentis |
| **Répartition** | 1 serveur + 4 clients + 10 observateurs |
| **Lieu** | Salle de TP avec espace dégagé |
| **Moment** | Début de séance (00:00 - 00:25) |

---

## 🛠️ MATÉRIEL NÉCESSAIRE

### Matériel à préparer par le formateur

| **Quantité** | **Matériel** | **Spécifications** |
|--------------|--------------|-------------------|
| 12 | Cartons "Adresse IP" | Format A5, numérotés 192.168.1.100 à 192.168.1.111 |
| 1 | Registre DHCP (grand cahier ou tableau blanc) | Pour noter les attributions |
| 5 | Badges de rôle | "SERVEUR DHCP", "CLIENT 1", "CLIENT 2", "CLIENT 3", "CLIENT 4" |
| 1 | Chronomètre ou minuteur | Pour mesurer les durées de bail |
| 4 | Badges "Bail expiré" | Cartons rouges à donner quand le temps est écoulé |
| 10 | Fiches d'observation | Pour les apprentis observateurs (modèle ci-dessous) |
| 1 | Panneau "RÉSEAU" | Délimiter la zone du réseau dans la salle |

### Préparation des cartons IP

**Modèle de carton (format A5, à imprimer sur papier coloré) :**

```
┌─────────────────────────────────┐
│                                 │
│      ADRESSE IP                 │
│                                 │
│    192.168.1.100               │
│                                 │
│   Masque : 255.255.255.0       │
│   Passerelle : 192.168.1.1     │
│   DNS : 8.8.8.8                │
│                                 │
│   Bail : 5 minutes             │
│                                 │
└─────────────────────────────────┘
```

**💡 Astuce :** Utiliser une couleur différente par plage (100-103 en bleu, 104-107 en vert, etc.) pour visualiser rapidement les adresses disponibles.

---

## 📋 DÉROULÉ DE L'ACTIVITÉ (25 min)

### Phase 1 : Mise en place et présentation (5 min)

#### Attribution des rôles

**Le formateur désigne :**

1. **1 Serveur DHCP** (apprenti volontaire à l'aise à l'oral)
   - Rôle : Distribuer les adresses IP
   - Matériel : 12 cartons IP + registre + stylo

2. **4 Clients DHCP** (apprentis volontaires)
   - Rôle : Demander et utiliser une adresse IP
   - Matériel : Aucun au départ (ils viendront les chercher)

3. **10 Observateurs** (reste du groupe)
   - Rôle : Observer et noter le processus
   - Matériel : Fiche d'observation + stylo

---

#### Règles du jeu

**Le formateur explique :**

> "Vous êtes dans un réseau informatique. Les **4 clients** veulent se connecter au réseau, mais pour cela ils ont **besoin d'une adresse IP**. Le **serveur DHCP** va leur en distribuer automatiquement.
>
> **Clients** : Vous ne pouvez pas communiquer entre vous tant que vous n'avez pas d'adresse IP !
>
> **Serveur** : Tu as 12 adresses disponibles. Tu dois les distribuer selon les règles DHCP.
>
> **Observateurs** : Notez tout ce qui se passe sur votre fiche. À la fin, on fera le lien avec le vrai protocole DHCP."

---

#### Délimitation de l'espace

**Le formateur place :**

- Un **panneau "RÉSEAU"** au centre de la salle (zone circulaire ou rectangulaire)
- Le **serveur DHCP** se positionne au centre du réseau (table avec ses cartons)
- Les **4 clients** se positionnent aux 4 coins du réseau
- Les **observateurs** restent assis en périphérie avec vue sur la scène

---

### Phase 2 : Scénario 1 - Première attribution (7 min)

#### 🎬 Action 1 : DHCP DISCOVER

**Client 1** entre dans le réseau et crie :

> "Bonjour ! Y a-t-il un serveur DHCP ici ? J'ai besoin d'une adresse IP !"

**💡 Formateur explique aux observateurs :**
> "Le client ne connaît pas l'adresse du serveur, il envoie un message en **broadcast** (à tout le monde)."

---

#### 🎬 Action 2 : DHCP OFFER

**Le serveur DHCP** prend un carton IP (192.168.1.100) et dit :

> "Oui, je suis là ! Je te propose l'adresse IP **192.168.1.100**. Elle est valable pendant **5 minutes**."

Il **tend le carton** au Client 1 (sans le lâcher encore).

**💡 Formateur explique :**
> "Le serveur **propose** une adresse. Le client n'est pas encore autorisé à l'utiliser."

---

#### 🎬 Action 3 : DHCP REQUEST

**Client 1** répond à haute voix (broadcast) :

> "Merci ! J'accepte l'adresse IP **192.168.1.100** du serveur DHCP !"

**💡 Formateur explique :**
> "Le client annonce publiquement qu'il accepte cette IP. Si plusieurs serveurs avaient fait une offre, les autres comprendraient qu'ils n'ont pas été choisis."

---

#### 🎬 Action 4 : DHCP ACKNOWLEDGE

**Le serveur** donne définitivement le carton au Client 1 et note dans son registre :

```
Registre DHCP
─────────────────────────────────────
IP           | Adresse MAC  | Bail expire à
192.168.1.100| Client1-MAC  | 14:35
```

Le serveur dit :

> "C'est confirmé ! Tu peux utiliser l'IP **192.168.1.100** pendant **5 minutes**. Ton bail expire à **14:35**."

**💡 Formateur explique :**
> "L'attribution est validée. Le client peut maintenant communiquer sur le réseau."

---

**Client 1** lève son carton en l'air et dit joyeusement :

> "Super ! Je suis **192.168.1.100** et je peux naviguer sur Internet !"

---

#### Répétition pour les Clients 2, 3 et 4

**Le formateur accélère :**

> "Maintenant, les 3 autres clients vont faire la même chose, mais plus vite. Allez-y !"

**Clients 2, 3, 4** répètent le processus DORA (en 2-3 min) :
- Client 2 obtient 192.168.1.101
- Client 3 obtient 192.168.1.102
- Client 4 obtient 192.168.1.103

**Résultat après 7 minutes :**
- 4 clients ont chacun une adresse IP
- Le serveur a noté les 4 attributions dans son registre
- Il reste 8 adresses disponibles (192.168.1.104 à 111)

---

### Phase 3 : Scénario 2 - Expiration et renouvellement (5 min)

#### 🎬 Situation : Bail expiré

**Le formateur active le chronomètre et annonce :**

> "Attention, 5 minutes sont passées ! Le bail du **Client 1** vient d'**expirer** !"

**Le formateur donne un badge rouge "BAIL EXPIRÉ"** au Client 1.

---

#### 🎬 Action : DHCP RELEASE (Libération volontaire)

**Client 1** rend son carton IP au serveur et dit :

> "Je n'ai plus besoin de cette adresse IP. Je la libère !"

**Le serveur** reprend le carton 192.168.1.100 et barre la ligne dans le registre :

```
Registre DHCP
─────────────────────────────────────
IP           | Adresse MAC  | Bail expire à | Statut
192.168.1.100| Client1-MAC  | 14:35         | LIBÉRÉ ✓
```

**💡 Formateur explique :**
> "Le client a exécuté un **DHCP RELEASE**. L'adresse redevient disponible dans le pool."

---

#### 🎬 Action : DHCP RENEW (Renouvellement)

**Client 1** (qui n'a plus d'IP) lève la main et dit :

> "J'ai à nouveau besoin d'une adresse IP. Je veux renouveler !"

**Le serveur** peut :
- Soit redonner la **même IP** (192.168.1.100) si disponible
- Soit donner une **autre IP** si la précédente a été attribuée

**Dans notre jeu, le serveur redonne 192.168.1.100** car elle est libre :

> "OK, je te redonne l'IP **192.168.1.100**. Nouveau bail de 5 minutes !"

**💡 Formateur explique :**
> "Le client a renouvelé son bail. C'est comme un **DHCP RENEW**."

---

### Phase 4 : Scénario 3 - Problèmes courants (5 min)

#### 🎬 Problème 1 : Pool DHCP saturé

**Le formateur introduit 9 nouveaux clients** (simulés, pas de vrais apprentis) :

> "Maintenant, imaginez que 9 autres postes arrivent sur le réseau. Le serveur distribue toutes les adresses restantes."

**Le serveur mime la distribution des 8 adresses restantes :**
- 192.168.1.104, 105, 106, 107, 108, 109, 110, 111 → Distribuées

**Un 13ème client (simulé) arrive et demande une IP.**

**Le serveur répond :**

> "Désolé, je n'ai plus d'adresses disponibles. Pool DHCP saturé !"

**💡 Formateur explique :**
> "Le client va s'attribuer une **adresse APIPA** (169.254.x.x). Il ne pourra pas communiquer avec le réseau."

**Question aux observateurs :**

> "Que peut faire l'administrateur réseau dans cette situation ?"

**Réponses attendues :**
- Augmenter la taille du pool (ajouter plus d'adresses)
- Réduire la durée des baux
- Libérer les adresses non utilisées

---

#### 🎬 Problème 2 : Serveur DHCP injoignable

**Le formateur fait sortir le serveur DHCP de la salle** (ou lui demande de se boucher les oreilles).

**Un nouveau client arrive et crie :**

> "Y a-t-il un serveur DHCP ? J'ai besoin d'une adresse IP !"

**Silence... Personne ne répond.**

**Le client attend 10 secondes, puis dit :**

> "Pas de réponse... Je vais m'attribuer une adresse APIPA : **169.254.42.57**"

**💡 Formateur explique :**
> "Si le serveur DHCP est éteint ou injoignable, le client ne peut pas obtenir d'IP. Il s'attribue automatiquement une adresse **APIPA** (169.254.x.x) mais **ne peut pas communiquer** avec Internet."

---

### Phase 5 : Débriefing collectif (3 min)

**Le formateur fait revenir tous les apprentis en position assise.**

**Questions posées au groupe :**

1. **"Qu'avez-vous observé pendant ce jeu ?"**
   - Réponses attendues : Distribution automatique, processus en 4 étapes, serveur note tout, baux limités dans le temps

2. **"Quels sont les avantages du DHCP par rapport à une configuration manuelle ?"**
   - Réponses attendues : Rapidité, pas d'erreurs, centralisation, récupération des IP non utilisées

3. **"Que se passe-t-il si le serveur DHCP tombe en panne ?"**
   - Réponse attendue : Les nouveaux clients n'obtiennent pas d'IP (adresse APIPA), mais les clients existants conservent leur IP jusqu'à expiration du bail

4. **"Pourquoi le bail a-t-il une durée limitée ?"**
   - Réponse attendue : Pour récupérer les adresses des postes éteints ou déconnectés, éviter le gaspillage d'adresses

---

## 📄 FICHE D'OBSERVATION (Modèle pour les observateurs)

```
═══════════════════════════════════════════════════════════
        📝 FICHE D'OBSERVATION - JEU DE RÔLE DHCP
═══════════════════════════════════════════════════════════

Nom : _____________________ Prénom : _____________________

Date : ___/___/___


┌─────────────────────────────────────────────────────────┐
│  PROCESSUS D'ATTRIBUTION D'ADRESSE IP                    │
└─────────────────────────────────────────────────────────┘

CLIENT 1 obtient son adresse IP :

Étape 1 - Ce que le client dit :
_________________________________________________________________

Étape 2 - Ce que le serveur répond :
_________________________________________________________________

Étape 3 - Ce que le client accepte :
_________________________________________________________________

Étape 4 - Ce que le serveur confirme :
_________________________________________________________________

Adresse IP attribuée : _______________________

Durée du bail : ____________ minutes


┌─────────────────────────────────────────────────────────┐
│  RENOUVELLEMENT ET LIBÉRATION                            │
└─────────────────────────────────────────────────────────┘

Que se passe-t-il quand le Client 1 libère son adresse ?
_________________________________________________________________
_________________________________________________________________

Que se passe-t-il quand le Client 1 renouvelle ?
_________________________________________________________________
_________________________________________________________________

A-t-il récupéré la même IP ? ☐ Oui ☐ Non


┌─────────────────────────────────────────────────────────┐
│  PROBLÈMES OBSERVÉS                                      │
└─────────────────────────────────────────────────────────┘

Problème 1 : Pool saturé
Que se passe-t-il quand il n'y a plus d'adresses disponibles ?
_________________________________________________________________
_________________________________________________________________

Problème 2 : Serveur injoignable
Que fait un client qui ne trouve pas de serveur DHCP ?
_________________________________________________________________
_________________________________________________________________


┌─────────────────────────────────────────────────────────┐
│  MES RÉFLEXIONS                                          │
└─────────────────────────────────────────────────────────┘

Quels sont les avantages du DHCP selon moi ?
1. ___________________________________________________________
2. ___________________________________________________________
3. ___________________________________________________________

Quels problèmes pourraient survenir en vrai ?
1. ___________________________________________________________
2. ___________________________________________________________

═══════════════════════════════════════════════════════════
```

---

## 🎓 APPRENTISSAGES ATTENDUS

### Ce que les apprentis vont découvrir intuitivement

| **Découverte** | **Lien avec le cours théorique** |
|----------------|----------------------------------|
| "Le client demande publiquement (crie)" | Message DHCP DISCOVER en broadcast |
| "Le serveur propose une adresse" | Message DHCP OFFER |
| "Le client accepte publiquement" | Message DHCP REQUEST en broadcast |
| "Le serveur confirme et note" | Message DHCP ACKNOWLEDGE + enregistrement du bail |
| "L'adresse a une durée limitée (5 min)" | Notion de bail DHCP (lease time) |
| "Le serveur note tout dans un registre" | Base de données DHCP du serveur |
| "On peut rendre l'adresse (Release)" | Commande ipconfig /release |
| "On peut redemander une adresse (Renew)" | Commande ipconfig /renew |
| "Si le serveur ne répond pas, on est bloqué" | Adresse APIPA 169.254.x.x |

---

## 💡 CONSEILS POUR LE FORMATEUR

### Gestion du jeu de rôle

**Si les apprentis sont timides :**
- Le formateur peut jouer le rôle du serveur DHCP lui-même
- Simplifier les dialogues (moins de texte à dire)
- Encourager et valoriser chaque participation

**Si les apprentis sont très à l'aise :**
- Introduire un 2ème serveur DHCP (compétition d'offres)
- Simuler une panne pendant une attribution (serveur s'évanouit)
- Ajouter des paquets "perdus" (un message n'arrive pas)

**Si le temps manque :**
- Réduire à 2 clients au lieu de 4
- Passer directement au débrief après le 1er DORA complet
- Sauter les scénarios de problèmes (ou juste les expliquer oralement)

---

### Variantes pédagogiques

**Version simplifiée (15 min) :**
- 1 serveur + 2 clients
- Processus DORA uniquement (pas de release/renew)
- Débrief rapide

**Version approfondie (35 min) :**
- 2 serveurs DHCP concurrents (choix du client)
- Introduire un routeur (DHCP Relay Agent)
- Simuler une attaque DHCP Starvation (client demande toutes les IP)

**Version théâtralisée :**
- Costumes (le serveur porte une casquette "Facteur")
- Décor (dessiner un réseau au sol avec scotch de couleur)
- Musique d'ambiance (son de modem 56k pour l'immersion)

---

## ✅ CRITÈRES DE RÉUSSITE DE L'ACTIVITÉ

L'activité est réussie si :

| **Indicateur** | **Critère** |
|----------------|-------------|
| **Engagement** | Au moins 80% des apprentis participent activement (rôles ou observations) |
| **Compréhension processus** | Les observateurs identifient les 4 étapes (DORA) |
| **Découverte autonome** | Au moins 3 avantages du DHCP sont cités spontanément |
| **Anticipation problèmes** | Les apprentis devinent que le pool peut être saturé |
| **Questionnement** | Au moins 5 questions pertinentes sont posées au débrief |

---

## 🔗 TRANSITION VERS LE COURS

**Script de transition (à dire aux apprentis après l'activité) :**

> "Bravo pour cette belle simulation ! Vous venez de jouer le rôle d'un **protocole réseau** : le **DHCP** (Dynamic Host Configuration Protocol).
>
> Ce que vous avez découvert :
> - Le processus en **4 étapes** (qu'on appelle **DORA**)
> - La notion de **bail** (durée limitée)
> - Le **registre** du serveur (qui note tout)
> - Les **problèmes** possibles (pool saturé, serveur injoignable)
>
> Maintenant, on va voir comment ça fonctionne **en vrai** :
> - Quels messages réseau sont échangés ?
> - Quelles commandes utiliser sur votre PC ?
> - Comment analyser une capture DHCP avec Wireshark ?
>
> Sortez vos fiches de cours, on plonge dans le monde réel du DHCP !"

---

## 📊 GRILLE D'OBSERVATION FORMATEUR (pendant l'activité)

| **Critère** | **Observations** |
|-------------|------------------|
| **Apprentis très engagés** (noms) | |
| **Apprentis en retrait** (noms) | |
| **Questions intéressantes posées** | |
| **Incompréhensions détectées** | |
| **Points à reprendre dans le cours** | |

---

## 🎯 LIEN AVEC LE PORTFOLIO

Cette activité prépare la compétence C3.1 pour le portfolio :

> "J'ai participé à un jeu de rôle simulant le protocole DHCP. J'ai observé le processus d'attribution automatique d'adresses IP en 4 étapes (Discover, Offer, Request, Acknowledge). J'ai compris l'importance du bail DHCP et les conséquences d'un serveur DHCP injoignable (adresse APIPA). Cette expérience m'a permis de visualiser concrètement un protocole réseau avant de le manipuler techniquement."

---

## 📸 PHOTO-SOUVENIR (optionnel)

**Idée bonus :** Prendre une photo de groupe avec :
- Le serveur DHCP au centre (avec son registre)
- Les 4 clients autour (brandissant leur carton IP)
- Les observateurs en arrière-plan

**Légende :**
> "Promotion 2024-2027 - Simulation DHCP - S7 Réseaux - 24/02/2026"

→ À afficher en salle de TP ou à intégrer dans le portfolio collectif

---

**Document créé le :** 24/02/2026  
**Auteur :** Équipe pédagogique CFA  
**Version :** 1.0  
**Durée de l'activité :** 25 minutes
