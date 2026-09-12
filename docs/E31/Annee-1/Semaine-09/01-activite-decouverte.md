# ACTIVITÉ DÉCOUVERTE - U31 Réseaux Informatiques
## Semaine 9 - "Le Serveur Web" : Comprendre HTTP par Simulation

---

## 🎯 OBJECTIFS DE L'ACTIVITÉ

### Objectifs pédagogiques

- **Comprendre intuitivement** le protocole HTTP (requête/réponse)
- **Découvrir** l'architecture client-serveur web
- **Expérimenter** les codes de statut HTTP (200, 404, 403, 500)
- **Identifier** le rôle du DocumentRoot
- **Introduire** la notion de VirtualHost

### Compétences transversales

- Expression orale (jouer un rôle)
- Observation et analyse
- Compréhension du web

---

## ⏱️ DURÉE ET ORGANISATION

| **Élément** | **Détail** |
|-------------|------------|
| **Durée totale** | 20 minutes |
| **Modalité** | Jeu de rôle collectif + observation |
| **Effectif** | 12-16 apprentis |
| **Répartition** | 1 serveur + 4 clients + 10 observateurs |
| **Lieu** | Salle de TP |
| **Moment** | Début de séance (00:00 - 00:20) |

---

## 🛠️ MATÉRIEL NÉCESSAIRE

### Matériel à préparer par le formateur

| **Quantité** | **Matériel** | **Spécifications** |
|--------------|--------------|-------------------|
| 15 | Fiches "Requête HTTP" | Format A5, imprimées (modèle ci-dessous) |
| 10 | Fiches "Page Web" | Représentant les fichiers HTML |
| 1 | Badge "SERVEUR APACHE" | Pour identifier le serveur |
| 4 | Badges "CLIENT" (Firefox, Chrome, Safari, Edge) | Pour les navigateurs |
| 1 | Boîte "DocumentRoot" | Carton représentant /var/www/html |
| 1 | Panneau "Codes HTTP" | Affichage des codes 200, 404, 403, 500 |
| 10 | Fiches d'observation | Pour les apprentis observateurs |

### Préparation des fiches

**Modèle de fiche "Requête HTTP" :**

```
┌─────────────────────────────────────┐
│        REQUÊTE HTTP                 │
├─────────────────────────────────────┤
│ Méthode : GET                       │
│ URL : /index.html                   │
│ Host: example.com                   │
│                                     │
│ [Le client veut la page d'accueil] │
└─────────────────────────────────────┘
```

**Modèle de fiche "Page Web" :**

```
┌─────────────────────────────────────┐
│     📄 index.html                   │
├─────────────────────────────────────┤
│ <html>                              │
│   <h1>Bienvenue !</h1>              │
│   <p>Page d'accueil</p>             │
│ </html>                             │
│                                     │
│ Emplacement : /var/www/html/        │
└─────────────────────────────────────┘
```

---

## 📋 DÉROULÉ DE L'ACTIVITÉ (20 min)

### Phase 1 : Mise en place et présentation (5 min)

#### Attribution des rôles

**Le formateur désigne :**

1. **1 Serveur Apache** (apprenti organisé)
   - Rôle : Recevoir les requêtes, chercher les fichiers, renvoyer les réponses
   - Matériel : Badge "SERVEUR APACHE" + Boîte DocumentRoot + Fiches pages web

2. **4 Clients** (navigateurs)
   - Client 1 : Firefox (badge)
   - Client 2 : Chrome (badge)
   - Client 3 : Safari (badge)
   - Client 4 : Edge (badge)
   - Rôle : Envoyer des requêtes HTTP, recevoir les réponses
   - Matériel : Fiches requêtes HTTP

3. **10 Observateurs** (reste du groupe)
   - Rôle : Observer et noter le processus
   - Matériel : Fiche d'observation + stylo

---

#### Règles du jeu

**Le formateur explique :**

> "Vous allez simuler le fonctionnement d'un serveur web.
>
> **Les clients** veulent consulter des pages web (index.html, about.html, etc.). Ils envoient des **requêtes HTTP** au serveur.
>
> **Le serveur Apache** reçoit les requêtes, cherche les fichiers dans son **DocumentRoot** (la boîte), et renvoie une **réponse HTTP** avec un code de statut.
>
> **Observateurs** : Notez le processus. On fera le lien avec le vrai protocole HTTP après."

---

#### Organisation de l'espace

```
        [SERVEUR APACHE]
        (Centre, avec boîte)
              │
      ┌───────┼───────┐
      │       │       │
   Client  Client  Client  Client
   Firefox Chrome Safari  Edge
```

- Le **serveur** se positionne au centre avec sa boîte "DocumentRoot"
- Les **4 clients** se placent en demi-cercle face au serveur
- Les **observateurs** se placent en périphérie

---

### Phase 2 : Scénario 1 - Requête réussie (200 OK) (5 min)

#### 🎬 Requête 1 : index.html (existe)

**Le formateur donne au Client 1 (Firefox) une fiche requête :**

```
GET /index.html HTTP/1.1
Host: example.com
```

**Client 1** s'approche du serveur et dit :

> "Bonjour serveur ! Je voudrais la page `/index.html`. Peux-tu me la donner ?"

**Le Serveur Apache** :

1. **Reçoit** la requête
2. **Cherche** dans sa boîte DocumentRoot
3. **Trouve** le fichier `index.html` (fiche page web)
4. **Répond** :

> "Requête reçue ! Je cherche... Trouvé ! Voici la page. Code HTTP **200 OK**."

5. **Donne** la fiche page web au Client 1

**Client 1 (Firefox)** :

> "Merci ! J'affiche la page à l'utilisateur."

---

**💡 Formateur explique aux observateurs :**

> "Code **200 OK** = Tout s'est bien passé. La page existe et a été trouvée.
>
> C'est la réponse la plus courante quand vous naviguez sur le web."

---

### Phase 3 : Scénario 2 - Page introuvable (404) (4 min)

#### 🎬 Requête 2 : contact.html (n'existe pas)

**Le formateur donne au Client 2 (Chrome) une fiche requête :**

```
GET /contact.html HTTP/1.1
Host: example.com
```

**Client 2** s'approche du serveur et dit :

> "Bonjour serveur ! Je voudrais la page `/contact.html`."

**Le Serveur Apache** :

1. **Reçoit** la requête
2. **Cherche** dans sa boîte DocumentRoot
3. **NE TROUVE PAS** le fichier `contact.html`
4. **Répond** :

> "Requête reçue ! Je cherche... Désolé, cette page n'existe pas. Code HTTP **404 NOT FOUND**."

**Client 2 (Chrome)** :

> "Zut ! J'affiche un message d'erreur : 'Page introuvable'."

---

**💡 Formateur explique :**

> "Code **404 NOT FOUND** = La page demandée n'existe pas sur le serveur.
>
> Vous avez tous déjà vu cette erreur en naviguant sur Internet !"

---

### Phase 4 : Scénario 3 - Accès interdit (403) (3 min)

#### 🎬 Requête 3 : admin.html (protégé)

**Le formateur place une fiche `admin.html` dans la boîte, mais avec un **cadenas** dessus (représentant les permissions).**

**Le formateur donne au Client 3 (Safari) une fiche requête :**

```
GET /admin.html HTTP/1.1
Host: example.com
```

**Client 3** s'approche du serveur et dit :

> "Bonjour serveur ! Je voudrais la page `/admin.html`."

**Le Serveur Apache** :

1. **Reçoit** la requête
2. **Cherche** dans sa boîte DocumentRoot
3. **Trouve** le fichier `admin.html` mais voit le **cadenas**
4. **Répond** :

> "Requête reçue ! Je cherche... La page existe, mais tu n'as **pas la permission** d'y accéder. Code HTTP **403 FORBIDDEN**."

**Client 3 (Safari)** :

> "Accès refusé ! J'affiche : 'Vous n'avez pas les droits pour voir cette page'."

---

**💡 Formateur explique :**

> "Code **403 FORBIDDEN** = La page existe mais l'accès est interdit.
>
> Causes fréquentes : mauvaises permissions (chmod), authentification requise, IP bloquée."

---

### Phase 5 : Scénario 4 - Erreur serveur (500) (3 min)

#### 🎬 Requête 4 : script.php (bug)

**Le formateur donne au Client 4 (Edge) une fiche requête :**

```
GET /script.php HTTP/1.1
Host: example.com
```

**Client 4** s'approche du serveur et dit :

> "Bonjour serveur ! Je voudrais exécuter `/script.php`."

**Le Serveur Apache** :

1. **Reçoit** la requête
2. **Cherche** le fichier `script.php`
3. **Trouve** le fichier et tente de l'**exécuter**
4. **BUG !** Le script contient une erreur (le formateur simule en faisant tomber des papiers)
5. **Répond** :

> "Requête reçue ! J'essaie d'exécuter le script... ERREUR ! Le script a planté. Code HTTP **500 INTERNAL SERVER ERROR**."

**Client 4 (Edge)** :

> "Le serveur a un problème ! J'affiche : 'Erreur interne du serveur'."

---

**💡 Formateur explique :**

> "Code **500 INTERNAL SERVER ERROR** = Problème côté serveur (bug PHP, base de données inaccessible, etc.).
>
> Ce n'est PAS la faute du client. C'est le serveur qui a un souci."

---

### Phase 6 : Débriefing collectif (5 min - inclus dans les 20 min)

**Le formateur fait revenir tous les apprentis en position assise.**

**Questions posées au groupe :**

1. **"Quels sont les 4 codes HTTP que vous avez vus ?"**
   - Réponses attendues : 200 OK, 404 Not Found, 403 Forbidden, 500 Internal Server Error

2. **"Que fait le serveur quand il reçoit une requête ?"**
   - Réponse attendue : Il cherche le fichier dans le DocumentRoot, puis renvoie une réponse

3. **"Qu'est-ce que le DocumentRoot ?"**
   - Réponse attendue : Le répertoire où sont stockés les fichiers du site web

4. **"Quelle différence entre 404 et 403 ?"**
   - Réponse attendue :
     - 404 : Le fichier n'existe pas
     - 403 : Le fichier existe mais l'accès est interdit

5. **"Avez-vous déjà vu ces erreurs en naviguant sur Internet ?"**
   - Réponses attendues : Oui, surtout 404 !

---

## 📄 FICHE D'OBSERVATION (Modèle pour les observateurs)

```
═══════════════════════════════════════════════════════════
       📝 FICHE D'OBSERVATION - SERVEUR WEB HTTP
═══════════════════════════════════════════════════════════

Nom : _____________________ Prénom : _____________________

Date : ___/___/___


┌─────────────────────────────────────────────────────────┐
│  REQUÊTE 1 : index.html (200 OK)                         │
└─────────────────────────────────────────────────────────┘

Que demande le client ?
_________________________________________________________________

Que fait le serveur ?
1. _________________________________________________________________
2. _________________________________________________________________
3. _________________________________________________________________

Quelle réponse renvoie le serveur ?
_________________________________________________________________

Code HTTP : __________   Signification : ___________________________


┌─────────────────────────────────────────────────────────┐
│  REQUÊTE 2 : contact.html (404 NOT FOUND)                │
└─────────────────────────────────────────────────────────┘

Pourquoi le serveur ne peut pas renvoyer la page ?
_________________________________________________________________

Code HTTP : __________   Signification : ___________________________


┌─────────────────────────────────────────────────────────┐
│  REQUÊTE 3 : admin.html (403 FORBIDDEN)                  │
└─────────────────────────────────────────────────────────┘

La page existe-t-elle sur le serveur ?  ☐ Oui ☐ Non

Pourquoi le serveur refuse l'accès ?
_________________________________________________________________

Code HTTP : __________   Signification : ___________________________


┌─────────────────────────────────────────────────────────┐
│  REQUÊTE 4 : script.php (500 INTERNAL SERVER ERROR)      │
└─────────────────────────────────────────────────────────┘

Qui est responsable de l'erreur ?  ☐ Le client ☐ Le serveur

Que s'est-il passé ?
_________________________________________________________________

Code HTTP : __________   Signification : ___________________________


┌─────────────────────────────────────────────────────────┐
│  MES RÉFLEXIONS                                          │
└─────────────────────────────────────────────────────────┘

Qu'est-ce que le DocumentRoot selon toi ?
_________________________________________________________________
_________________________________________________________________

Quels sont les rôles du serveur web ?
1. ___________________________________________________________
2. ___________________________________________________________
3. ___________________________________________________________

Quel code HTTP as-tu déjà rencontré en naviguant sur Internet ?
_________________________________________________________________

═══════════════════════════════════════════════════════════
```

---

## 🎓 APPRENTISSAGES ATTENDUS

### Ce que les apprentis vont découvrir intuitivement

| **Découverte** | **Lien avec le cours théorique** |
|----------------|----------------------------------|
| "Le client demande une page" | Requête HTTP GET |
| "Le serveur cherche le fichier" | DocumentRoot, système de fichiers |
| "Le serveur renvoie un code" | Codes de statut HTTP |
| "200 = Tout va bien" | Code HTTP 200 OK |
| "404 = Page pas trouvée" | Code HTTP 404 Not Found |
| "403 = Accès interdit" | Permissions Linux (chmod) |
| "500 = Erreur serveur" | Bug application, crash |

---

## 💡 CONSEILS POUR LE FORMATEUR

### Gestion du jeu de rôle

**Si les apprentis sont timides :**
- Le formateur peut jouer le rôle du serveur lui-même
- Simplifier les requêtes (juste dire "Je veux index.html")
- Réduire à 2-3 requêtes au lieu de 4

**Si les apprentis sont très à l'aise :**
- Introduire les méthodes POST, PUT, DELETE
- Simuler une requête avec cookies (authentification)
- Ajouter un 2ème serveur (load balancing)

**Si le temps manque :**
- Faire uniquement 200 OK et 404 Not Found (les plus courants)
- Expliquer 403 et 500 oralement sans simulation

---

### Variantes pédagogiques

**Version simplifiée (10 min) :**
- 1 serveur + 2 clients
- 2 requêtes (200 et 404 uniquement)
- Pas de fiches, juste oral

**Version approfondie (30 min) :**
- Introduire HTTPS (cadenas, certificat SSL)
- Simuler un cache (le serveur note "Déjà servi récemment")
- Ajouter un proxy inverse (intermédiaire entre client et serveur)

**Version théâtralisée :**
- Costumes (serveur en blouse de "chef", clients avec casquettes navigateurs)
- Décor (dessiner un serveur géant au tableau)
- Son (bip pour chaque requête)

---

## ✅ CRITÈRES DE RÉUSSITE DE L'ACTIVITÉ

L'activité est réussie si :

| **Indicateur** | **Critère** |
|----------------|-------------|
| **Engagement** | Au moins 80% des apprentis participent (rôles ou observations) |
| **Compréhension codes HTTP** | Les observateurs identifient les 4 codes (200, 404, 403, 500) |
| **Découverte DocumentRoot** | Les apprentis comprennent que le serveur cherche dans un répertoire |
| **Lien avec quotidien** | Au moins 3 apprentis citent avoir vu une erreur 404 |
| **Questionnement** | Au moins 3 questions pertinentes posées au débrief |

---

## 🔗 TRANSITION VERS LE COURS

**Script de transition (à dire aux apprentis après l'activité) :**

> "Bravo pour cette simulation ! Vous venez de jouer le rôle d'un **serveur web** Apache et de **clients** (navigateurs).
>
> Ce que vous avez découvert :
> - Le **protocole HTTP** (requête GET, réponse avec code de statut)
> - Le **DocumentRoot** (la boîte où sont les fichiers du site)
> - Les **codes HTTP** : 200 OK, 404 Not Found, 403 Forbidden, 500 Internal Server Error
> - L'**architecture client-serveur** (le navigateur demande, le serveur répond)
>
> Maintenant, on va voir comment ça fonctionne **en vrai** :
> - Installer Apache sur Ubuntu Linux
> - Créer une page HTML et la mettre dans /var/www/html
> - Accéder à votre site depuis un navigateur
> - Configurer plusieurs sites avec des VirtualHosts
>
> Sortez vos fiches de cours, on installe Apache !"

---

## 📊 GRILLE D'OBSERVATION FORMATEUR (pendant l'activité)

| **Critère** | **Observations** |
|-------------|------------------|
| **Apprentis très engagés** (noms) | |
| **Apprentis en retrait** (noms) | |
| **Questions pertinentes posées** | |
| **Incompréhensions détectées** | |
| **Points à reprendre dans le cours** | |

---

## 🎯 LIEN AVEC LE PORTFOLIO

Cette activité prépare la compétence C3.4 pour le portfolio :

> "J'ai participé à une simulation physique du protocole HTTP. J'ai observé les échanges entre un client (navigateur) et un serveur web Apache : requête GET, recherche dans le DocumentRoot, réponse avec code de statut (200, 404, 403, 500). Cette expérience m'a permis de visualiser concrètement le fonctionnement d'un serveur web avant de l'installer techniquement."

---

## 📸 PHOTO-SOUVENIR (optionnel)

**Idée bonus :** Prendre une photo de groupe avec :
- Le serveur Apache au centre (avec sa boîte DocumentRoot)
- Les 4 clients autour (brandissant leurs fiches requêtes)
- Les observateurs en arrière-plan

**Légende :**
> "Promotion 2024-2027 - Simulation HTTP - S9 Réseaux - 24/02/2026"

→ À afficher en salle de TP ou à intégrer dans le portfolio collectif

---

**Document créé le :** 24/02/2026  
**Auteur :** Équipe pédagogique CFA  
**Version :** 1.0  
**Durée de l'activité :** 20 minutes
