# DEVOIR PORTFOLIO - U31 Réseaux Informatiques
## Semaine 9 - Serveur Web Apache : Installation et Déploiement

---

**Nom :** _________________________ **Prénom :** _________________________

**Classe :** Bac Pro CIEL - Année 1 **Date :** ___/___/______

---

## 🎯 OBJECTIF DU DEVOIR

Ce devoir constitue une **preuve de compétence** pour votre **portfolio professionnel** (Épreuve E4).

**Vous devez :**
1. Installer et configurer Apache sur Ubuntu Linux
2. Créer et déployer un site web HTML statique
3. Configurer un VirtualHost pour un deuxième site
4. Tester l'accès réseau à vos sites
5. Diagnostiquer et corriger des erreurs courantes
6. Documenter votre travail (captures d'écran, code HTML)

**Compétences évaluées :**
- C3.4 : Installer et configurer un service réseau (serveur web)
- C3.3 : Exploiter un réseau informatique (accès HTTP)
- C1.2 : Gérer un système d'exploitation Linux

---

## 📋 CONSIGNES GÉNÉRALES

### Durée
- **1h50 de pratique** (TP guidé + TP avancé + Diagnostic)

### Travail
- **Individuel** (chacun installe Apache sur son PC)

### Livrables à rendre
1. **Fiche TP complétée** (ce document)
2. **4 captures d'écran** :
   - Capture 1 : `systemctl status apache2` (Apache actif)
   - Capture 2 : Page web site principal dans le navigateur
   - Capture 3 : Page web VirtualHost dans le navigateur
   - Capture 4 : Logs d'accès (`/var/log/apache2/access.log`)
3. **Code HTML** de vos 2 sites (copier-coller dans ce document)
4. **URL d'accès** de vos sites (IP + nom de domaine local)

### Critères de réussite
- ✅ Apache installé et actif
- ✅ Site principal accessible depuis un autre PC
- ✅ VirtualHost configuré et fonctionnel
- ✅ Permissions correctes (www-data, 755/644)
- ✅ Diagnostic d'erreurs résolu

---

## 🔧 EXERCICE 1 : INSTALLATION D'APACHE (25 points)

### Étape 1 : Vérification système (5 points)

**Commandes à exécuter :**

```bash
# Vérifier la distribution
lsb_release -a

# Vérifier l'IP du PC
ip addr show | grep inet
```

**Copier les résultats ci-dessous :**

**Distribution Linux :**
_________________________________________________________________________

**Adresse IP :**
_________________________________________________________________________

**☐ Étape 1 validée** (signature formateur : _______________)

---

### Étape 2 : Installation d'Apache2 (10 points)

**Commandes à exécuter :**

```bash
sudo apt update
sudo apt install apache2 -y
```

**Durée de l'installation :** __________ secondes

**Questions :**

1. **Quels paquets ont été installés ?** (noter au moins 3)
   1. _________________________________________________________________
   2. _________________________________________________________________
   3. _________________________________________________________________

2. **Quelle version d'Apache a été installée ?**
   ```bash
   apache2 -v
   ```
   - Version : _______________________

**☐ Étape 2 validée** (signature formateur : _______________)

---

### Étape 3 : Vérification du service (10 points)

**Commande à exécuter :**

```bash
sudo systemctl status apache2
```

**Copier-coller le résultat (ou faire une capture d'écran) :**

```
[CAPTURE 1 À COLLER ICI]











```

**Questions :**

1. **Apache est-il actif ?** ☐ Oui (active (running)) ☐ Non (inactive)

2. **Apache démarre-t-il automatiquement au boot ?** ☐ Oui (enabled) ☐ Non (disabled)

3. **Sur quel port Apache écoute-t-il ?**
   ```bash
   sudo ss -tlnp | grep apache2
   ```
   - Port : __________

4. **Quel est le PID (identifiant de processus) d'Apache ?** __________

**☐ Étape 3 validée** (signature formateur : _______________)

---

## 🌐 EXERCICE 2 : SITE WEB PRINCIPAL (30 points)

### Étape 1 : Test de la page par défaut (5 points)

**Test dans le navigateur :**

```
http://localhost
```

**Résultat :**
- ☐ Page "Apache2 Ubuntu Default Page" s'affiche
- ☐ Erreur (préciser) : _______________________________________________

**Si erreur, diagnostic :**

```bash
# Vérifier qu'Apache tourne
sudo systemctl status apache2

# Vérifier le pare-feu
sudo ufw status
```

**Solution appliquée :**
_________________________________________________________________________

---

### Étape 2 : Création d'une page HTML personnalisée (15 points)

**Commandes à exécuter :**

```bash
cd /var/www/html
sudo mv index.html index.html.bak
sudo nano index.html
```

**Créer une page HTML avec le contenu suivant (à adapter) :**

```html
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>[VOTRE NOM] - Serveur Apache</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin: 0;
            padding: 0;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
        }
        .container {
            margin-top: 100px;
        }
        h1 {
            font-size: 4em;
            margin-bottom: 20px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }
        .info-box {
            background-color: rgba(255,255,255,0.1);
            padding: 30px;
            border-radius: 15px;
            display: inline-block;
            margin-top: 30px;
            backdrop-filter: blur(10px);
        }
        .info-box p {
            font-size: 1.2em;
            margin: 10px 0;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🚀 Serveur Web de [VOTRE NOM]</h1>
        <div class="info-box">
            <p><strong>Système :</strong> Ubuntu Linux</p>
            <p><strong>Serveur :</strong> Apache 2.4</p>
            <p><strong>IP :</strong> 192.168.50.XX</p>
            <p><strong>Date de déploiement :</strong> 24/02/2026</p>
        </div>
    </div>
</body>
</html>
```

**Copier le code HTML final de votre page :**

```html
[COLLER VOTRE CODE HTML ICI]













```

**☐ Code HTML créé** (signature formateur : _______________)

---

### Étape 3 : Test et validation (10 points)

**Test 1 : Accès local**

```
http://localhost
```

**Résultat :** ☐ Ma page personnalisée s'affiche ✅ ☐ Erreur ❌

---

**Test 2 : Accès depuis un autre PC**

**IP de votre serveur :** 192.168.50.___

**Demander à un voisin de tester :**

```
http://192.168.50.___
```

**Nom du testeur :** _________________________

**Résultat :** ☐ Le voisin voit ma page ✅ ☐ Erreur ❌

**Si erreur, diagnostic :**

| **Problème** | **Vérification** | **Résultat** |
|-------------|----------------|-------------|
| Pare-feu bloque | `sudo ufw status` | ☐ OK ☐ Problème |
| Apache n'écoute que sur localhost | `sudo ss -tlnp \| grep :80` | ☐ OK ☐ Problème |
| Mauvaise IP testée | `ip addr` | ☐ OK ☐ Problème |

**Solution appliquée :**
_________________________________________________________________________

---

**Capture d'écran de votre page :**

```
[CAPTURE 2 : COLLER LA CAPTURE DE VOTRE PAGE WEB]









```

**☐ Étape 3 validée** (signature formateur : _______________)

---

## 🏠 EXERCICE 3 : VIRTUALHOST (30 points)

### Étape 1 : Création du répertoire et de la page (10 points)

**Cahier des charges :**

Créer un deuxième site accessible via `http://portfolio.local` avec le thème de votre choix.

**Commandes à exécuter :**

```bash
# Créer le répertoire
sudo mkdir -p /var/www/portfolio

# Créer la page HTML
sudo nano /var/www/portfolio/index.html
```

**Thèmes suggérés :**
- Portfolio professionnel (CV en ligne)
- Site de présentation d'un projet
- Page d'accueil d'un jeu vidéo
- Site de restaurant fictif

**Copier le code HTML de votre deuxième site :**

```html
[COLLER VOTRE CODE HTML DU PORTFOLIO ICI]













```

**Thème choisi :** _______________________________________________________

**☐ Page créée** (signature formateur : _______________)

---

### Étape 2 : Configuration du VirtualHost (15 points)

**Commande à exécuter :**

```bash
sudo nano /etc/apache2/sites-available/portfolio.conf
```

**Contenu du fichier de configuration :**

```apache
<VirtualHost *:80>
    ServerName portfolio.local
    ServerAlias www.portfolio.local
    
    DocumentRoot /var/www/portfolio
    
    <Directory /var/www/portfolio>
        Options Indexes FollowSymLinks
        AllowOverride None
        Require all granted
    </Directory>
    
    ErrorLog ${APACHE_LOG_DIR}/portfolio_error.log
    CustomLog ${APACHE_LOG_DIR}/portfolio_access.log combined
</VirtualHost>
```

**Questions de compréhension :**

1. **À quoi sert la directive `ServerName` ?**
   _________________________________________________________________

2. **À quoi sert la directive `DocumentRoot` ?**
   _________________________________________________________________

3. **Où seront stockés les logs d'erreur de ce site ?**
   - Chemin complet : _________________________________________________

---

**Commandes d'activation :**

```bash
# Activer le site
sudo a2ensite portfolio.conf

# Recharger Apache
sudo systemctl reload apache2

# Ajouter l'entrée DNS locale
sudo nano /etc/hosts
# Ajouter cette ligne : 127.0.0.1   portfolio.local
```

**Vérifier qu'il n'y a pas d'erreur :**

```bash
sudo apache2ctl configtest
```

**Résultat :** ☐ Syntax OK ✅ ☐ Erreur (préciser) : _____________________

**☐ VirtualHost configuré** (signature formateur : _______________)

---

### Étape 3 : Test du VirtualHost (5 points)

**Test dans le navigateur :**

```
http://portfolio.local
```

**Résultat :** ☐ Mon site portfolio s'affiche ✅ ☐ Erreur ❌

---

**Capture d'écran du site portfolio :**

```
[CAPTURE 3 : COLLER LA CAPTURE DU SITE PORTFOLIO]









```

**Vérifier que les 2 sites cohabitent :**

| **URL** | **Site affiché** | **Fonctionne** |
|---------|-----------------|---------------|
| `http://192.168.50.___` | Site principal | ☐ Oui ☐ Non |
| `http://portfolio.local` | Site portfolio | ☐ Oui ☐ Non |

**☐ Étape 3 validée** (signature formateur : _______________)

---

## 🛠️ EXERCICE 4 : DIAGNOSTIC DE PANNES (25 points)

### Scénario 1 : Erreur 404 - Page introuvable (8 points)

**Contexte :**

Vous créez un fichier `about.html` mais en accédant à `http://192.168.50.XX/about.html`, le navigateur affiche une erreur 404.

**Questions :**

1. **Quelle commande permet de vérifier que le fichier existe ?**
   ```bash
   _______________________________________________________________
   ```

2. **Dans quel répertoire doit se trouver `about.html` ?**
   - Chemin complet : _________________________________________________

3. **Quelle est la cause la plus probable si le fichier existe mais renvoie 404 ?**
   - ☐ Erreur de casse (About.html vs about.html)
   - ☐ Fichier dans le mauvais répertoire
   - ☐ Permissions incorrectes
   - ☐ Apache arrêté

4. **Où consulter les logs pour diagnostiquer ?**
   ```bash
   _______________________________________________________________
   ```

---

### Scénario 2 : Erreur 403 - Accès interdit (9 points)

**Contexte :**

Après avoir créé un fichier `secret.html`, le navigateur affiche "403 Forbidden".

**Questions :**

1. **Vérifier les permissions du fichier :**
   ```bash
   ls -l /var/www/html/secret.html
   ```
   - Permissions actuelles : __________________________________________

2. **Quelles permissions le fichier devrait-il avoir ?**
   - ☐ 644 (rw-r--r--)
   - ☐ 755 (rwxr-xr-x)
   - ☐ 777 (rwxrwxrwx)

3. **Quel utilisateur doit être propriétaire du fichier ?**
   - ☐ root
   - ☐ www-data
   - ☐ Votre nom d'utilisateur

4. **Commandes pour corriger les permissions :**
   ```bash
   # Propriétaire
   _______________________________________________________________
   
   # Permissions
   _______________________________________________________________
   ```

---

### Scénario 3 : Apache ne démarre pas (8 points)

**Contexte :**

Après une modification de configuration, Apache refuse de démarrer :

```bash
sudo systemctl start apache2
Job for apache2.service failed...
```

**Questions :**

1. **Quelle commande permet de tester la configuration Apache ?**
   ```bash
   _______________________________________________________________
   ```

2. **Où consulter les logs pour identifier l'erreur ?**
   - Fichier : ________________________________________________________

3. **Erreur typique trouvée dans les logs :**
   ```
   AH00526: Syntax error on line 5 of /etc/apache2/sites-enabled/portfolio.conf:
   Invalid command 'ServerNam', perhaps misspelled
   ```
   
   **Quelle est l'erreur ?**
   _________________________________________________________________
   
   **Correction à apporter :**
   _________________________________________________________________

4. **Après correction, quelle commande pour redémarrer Apache ?**
   ```bash
   _______________________________________________________________
   ```

---

## 📊 EXERCICE 5 : ANALYSE DES LOGS (10 points)

### Consultation des logs d'accès

**Commande à exécuter :**

```bash
sudo tail -n 20 /var/log/apache2/access.log
```

**Copier-coller les 5 dernières lignes :**

```
[CAPTURE 4 : COLLER LES LOGS D'ACCÈS]







```

**Analyse d'une ligne de log :**

Prendre la première ligne et la décomposer :

```
192.168.50.10 - - [24/Feb/2026:14:30:15 +0100] "GET /index.html HTTP/1.1" 200 1234
```

**Questions :**

1. **Quelle est l'adresse IP du client ?** ______________________________

2. **Quelle page a été demandée ?** _____________________________________

3. **Quel est le code de statut HTTP ?** ____________

4. **Que signifie ce code ?** ___________________________________________

5. **Quelle est la taille de la réponse ?** __________ octets

---

## 📊 BARÈME D'ÉVALUATION (Compatible Qualiopi)

### Partie A : Compétences techniques (60 points)

| **Critère** | **Indicateur observable** | **Points** | **Obtenu** |
|-------------|---------------------------|------------|------------|
| **Installation Apache** | Apache installé, actif, démarre au boot | 10 pts | ___/10 |
| **Vérification service** | systemctl status correct, port 80 écoute | 5 pts | ___/5 |
| **Page HTML principale** | Page personnalisée créée et visible | 15 pts | ___/15 |
| **Accès réseau** | Site accessible depuis un autre PC | 10 pts | ___/10 |
| **VirtualHost** | 2ème site configuré et fonctionnel | 15 pts | ___/15 |
| **Diagnostic pannes** | 3 scénarios résolus correctement | 15 pts | ___/15 |
| **Analyse logs** | Logs consultés et analysés | 5 pts | ___/5 |

**Sous-total Partie A : ___/75 points** (converti sur 60)

---

### Partie B : Documentation et traçabilité (20 points)

| **Critère** | **Indicateur observable** | **Points** | **Obtenu** |
|-------------|---------------------------|------------|------------|
| **Captures d'écran** | 4 captures complètes et exploitables | 8 pts | ___/8 |
| **Code HTML** | Code propre, indenté, fonctionnel | 6 pts | ___/6 |
| **Qualité des explications** | Réponses claires et argumentées | 4 pts | ___/4 |
| **Présentation** | Document soigné, lisible | 2 pts | ___/2 |

**Sous-total Partie B : ___/20 points**

---

### Partie C : Compétences transversales (20 points)

| **Critère** | **Indicateur observable** | **Points** | **Obtenu** |
|-------------|---------------------------|------------|------------|
| **Autonomie** | Réalise les manipulations avec peu d'aide | 6 pts | ___/6 |
| **Rigueur** | Vérifie la configuration avant de valider | 6 pts | ___/6 |
| **Créativité** | Page HTML originale et esthétique | 4 pts | ___/4 |
| **Gestion du temps** | Termine dans le temps imparti (1h50) | 4 pts | ___/4 |

**Sous-total Partie C : ___/20 points**

---

### Note finale

| **Partie** | **Points obtenus** | **Coefficient** | **Note sur 20** |
|------------|--------------------|-----------------|-----------------|
| Partie A - Compétences techniques | ___/75 | ×0,16 | ___/12 |
| Partie B - Documentation | ___/20 | ×1 | ___/4 |
| Partie C - Compétences transversales | ___/20 | ×1 | ___/4 |
| **TOTAL** | | | **___/20** |

**Appréciation formateur :**
_________________________________________________________________________
_________________________________________________________________________
_________________________________________________________________________

**Signature formateur :** ___________________ **Date :** ___/___/______

---

## 🎯 GRILLE D'ANALYSE DE COMPÉTENCES (Portfolio)

**Cette section est à remplir par l'apprenti pour alimenter son portfolio professionnel.**

### Compétence C3.4 : Installer et configurer un service réseau

**Situation professionnelle vécue :**

*"J'ai installé et configuré un serveur web Apache sur Ubuntu Linux. J'ai créé deux sites web HTML statiques accessibles via des VirtualHosts. J'ai géré les permissions des fichiers et diagnostiqué des erreurs courantes (404, 403). J'ai testé l'accès réseau depuis plusieurs postes clients."*

**Ce que j'ai su faire :**
- ☐ Installer Apache avec apt
- ☐ Démarrer/arrêter/recharger le service
- ☐ Créer des pages HTML dans le DocumentRoot
- ☐ Configurer des VirtualHosts
- ☐ Gérer les permissions (chown, chmod)
- ☐ Consulter les logs Apache

**Preuves :**
- ☐ Captures d'écran (systemctl status, sites web)
- ☐ Code HTML créé
- ☐ Fichier de configuration VirtualHost
- ☐ Validation du formateur

---

### Compétence C3.3 : Exploiter un réseau informatique

**Situation professionnelle vécue :**

*"J'ai déployé un service web accessible sur le réseau local. J'ai testé l'accès HTTP depuis plusieurs clients et vérifié la connectivité. J'ai analysé les logs d'accès pour identifier les requêtes reçues."*

**Ce que j'ai su faire :**
- ☐ Tester l'accès à un site web (localhost, IP, nom de domaine)
- ☐ Diagnostiquer les problèmes d'accès réseau
- ☐ Comprendre le protocole HTTP (requête/réponse)
- ☐ Analyser les codes de statut (200, 404, 403, 500)

**Preuves :**
- ☐ Tests d'accès depuis plusieurs PC
- ☐ Logs d'accès analysés
- ☐ Diagnostic de pannes résolu

---

### Compétence C1.2 : Gérer un système d'exploitation

**Situation professionnelle vécue :**

*"J'ai utilisé la ligne de commande Linux pour installer des paquets, gérer des services systemd, éditer des fichiers de configuration, et gérer les permissions du système de fichiers."*

**Ce que j'ai su faire :**
- ☐ Utiliser apt (update, install)
- ☐ Gérer les services avec systemctl
- ☐ Éditer des fichiers avec nano
- ☐ Gérer les permissions (chown, chmod)
- ☐ Consulter les logs système

**Preuves :**
- ☐ Commandes exécutées documentées
- ☐ Fichiers de configuration modifiés
- ☐ Services gérés correctement

---

## ✍️ AUTO-ÉVALUATION

**Réponds honnêtement à ces questions pour progresser :**

1. **As-tu réussi à installer Apache du premier coup ?**
   - ☐ Oui ☐ Non
   - Si non, quelle difficulté ? _______________________________________

2. **Quelle partie as-tu trouvée la plus difficile ?**
   - ☐ Installation Apache
   - ☐ Création page HTML
   - ☐ Configuration VirtualHost
   - ☐ Diagnostic des erreurs
   - ☐ Autre : _____________________________________________________

3. **Te sens-tu capable de déployer un site web en entreprise ?**
   - ☐ Oui, sans aide
   - ☐ Oui, avec un peu d'aide
   - ☐ Non, j'ai besoin de plus d'entraînement

4. **Qu'est-ce que tu as appris de nouveau aujourd'hui ?**
_________________________________________________________________________
_________________________________________________________________________

5. **Quel conseil donnerais-tu à un camarade pour réussir ce TP ?**
_________________________________________________________________________
_________________________________________________________________________

---

## 📝 COMMENTAIRES ET CONSEILS DU FORMATEUR

**Points forts :**
_________________________________________________________________________
_________________________________________________________________________

**Axes d'amélioration :**
_________________________________________________________________________
_________________________________________________________________________

**Conseils pour S10 (Partage fichiers) :**
_________________________________________________________________________
_________________________________________________________________________

---

## ✅ VALIDATION POUR LE PORTFOLIO

☐ **Ce devoir constitue une preuve acceptable pour le portfolio professionnel**

**Niveau de maîtrise atteint :**
- ☐ **Fragile** : L'apprenti a besoin d'un accompagnement renforcé
- ☐ **En cours d'acquisition** : L'apprenti progresse, continuer à pratiquer
- ☐ **Acquis** : L'apprenti maîtrise la compétence
- ☐ **Expert** : L'apprenti peut former d'autres personnes

**Signature formateur :** ___________________ **Date :** ___/___/______

---

**Document à conserver dans le portfolio pour les épreuves E4, E5 et E6**

**Date de création :** 24/02/2026  
**Version :** 1.0  
**Auteur :** Yahn LE PRETTRE
