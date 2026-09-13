# PROJET FINAL - U31 Réseaux Informatiques
## Année 1 - Semaine 18 : Déploiement Infrastructure Réseau

---

**Nom Binôme 1 :** _________________________ **Prénom :** _________________________

**Nom Binôme 2 :** _________________________ **Prénom :** _________________________

**Classe :** Bac Pro CIEL - Année 1 **Date :** ___/___/______

**Sujet tiré :** ☐ Sujet 1  ☐ Sujet 2  ☐ Sujet 3  ☐ Sujet 4  ☐ Sujet 5  ☐ Sujet 6  ☐ Sujet 7  ☐ Sujet 8

---

## 🎯 PRÉSENTATION DU PROJET

### Contexte professionnel

Vous êtes **techniciens réseau** dans une **entreprise d'installation et maintenance informatique**. Un client vous confie le déploiement complet de l'infrastructure réseau de sa structure.

**Mission :**

Concevoir, déployer, documenter et présenter une infrastructure réseau complète comprenant :
- Câblage structuré
- Switch avec VLANs
- Serveur DHCP
- Serveur Web
- Tests de validation

**Durée :** 2 jours (8 heures)

---

## 📋 LIVRABLES OBLIGATOIRES

### 1. Infrastructure technique déployée et fonctionnelle

- ✅ **Câblage** : Minimum 6 câbles RJ45 testés
- ✅ **Switch configuré** : 3 VLANs, ports en mode access, config sauvegardée
- ✅ **Serveur DHCP** : 3 pools (1 par VLAN)
- ✅ **Serveur Web** : Site vitrine accessible
- ✅ **Tests validés** : Ping, accès web, logs

### 2. Dossier technique (PDF, 10-15 pages)

- ✅ Schémas réseau (physique + logique)
- ✅ Plan d'adressage complet
- ✅ Configurations (switch, DHCP, web)
- ✅ Procédures de tests
- ✅ Captures d'écran

### 3. Soutenance orale (15 minutes)

- ✅ Présentation (10 min)
- ✅ Démonstration live (dans les 10 min)
- ✅ Questions formateur (5 min)

---

## 📊 CRITÈRES DE RÉUSSITE

| **Critère** | **Validation** |
|-------------|----------------|
| Câblage testé OK | ☐ |
| 3 VLANs configurés | ☐ |
| Connectivité intra-VLAN | ☐ |
| Isolation inter-VLAN | ☐ |
| DHCP fonctionnel | ☐ |
| Site web accessible | ☐ |
| Config sauvegardée | ☐ |
| Documentation complète | ☐ |
| Panne résolue | ☐ |
| Soutenance réussie | ☐ |

**Seuil de validation :** 8/10 critères minimum

---

## 📁 SUJETS DE PROJET (8 contextes clients)

---

## SUJET 1 : PME DE SERVICES (20 postes)

### Présentation du client

**Nom :** Services Plus SARL  
**Activité :** Conseil en management et gestion  
**Effectif :** 20 collaborateurs  
**Locaux :** Open space + 3 bureaux fermés

### Organigramme

```
Direction Générale (2)
├─ Pôle Comptabilité (5)
├─ Pôle Commercial (8)
└─ Pôle Production (5)
```

### Besoin exprimé

Le client souhaite **segmenter son réseau** pour :
- Isoler la comptabilité (données sensibles)
- Prioriser le trafic commercial (VoIP)
- Séparer la production (serveurs internes)

### Spécifications techniques

**3 VLANs à créer :**

| **VLAN** | **Nom** | **Services** | **Nb postes** |
|----------|---------|--------------|--------------|
| VLAN 10 | DIRECTION | Direction + Comptabilité | 7 |
| VLAN 20 | COMMERCIAL | Équipe commerciale + VoIP | 8 |
| VLAN 30 | PRODUCTION | Serveurs + Développement | 5 |

---

**Plan d'adressage suggéré :**

| **VLAN** | **Réseau** | **Plage DHCP** | **Passerelle** |
|----------|-----------|---------------|---------------|
| 10 | 192.168.10.0/24 | .100 - .150 | .1 |
| 20 | 192.168.20.0/24 | .100 - .150 | .1 |
| 30 | 192.168.30.0/24 | .100 - .150 | .1 |

---

**Services à déployer :**

- ✅ Site vitrine : `http://servicesplu.local`
- ✅ DHCP sur les 3 VLANs
- ⭐ **Bonus** : Routage inter-VLAN (VLAN 20 peut joindre VLAN 30 pour accès serveurs)

---

## SUJET 2 : CABINET MÉDICAL (15 postes)

### Présentation du client

**Nom :** Cabinet Médical Saint-Jean  
**Activité :** Médecine générale + Laboratoire d'analyses  
**Effectif :** 15 personnes  
**Locaux :** Accueil + 4 cabinets + Labo

### Organigramme

```
Accueil/Secrétariat (3)
├─ Médecins (5)
├─ Secrétariat médical (4)
└─ Laboratoire (3)
```

### Besoin exprimé

Le client souhaite :
- **Isoler** le laboratoire (données médicales sensibles - RGPD)
- **Séparer** les médecins et le secrétariat
- **Sécuriser** l'accueil (accès public WiFi séparé - optionnel)

### Spécifications techniques

**3 VLANs à créer :**

| **VLAN** | **Nom** | **Services** | **Nb postes** |
|----------|---------|--------------|--------------|
| VLAN 10 | ACCUEIL | Accueil + Secrétariat | 7 |
| VLAN 20 | MEDECINS | Cabinets médicaux | 5 |
| VLAN 30 | LABORATOIRE | Laboratoire d'analyses | 3 |

---

**Plan d'adressage suggéré :**

| **VLAN** | **Réseau** | **Plage DHCP** | **Passerelle** |
|----------|-----------|---------------|---------------|
| 10 | 192.168.10.0/24 | .50 - .100 | .1 |
| 20 | 192.168.20.0/24 | .50 - .100 | .1 |
| 30 | 192.168.30.0/24 | .50 - .80 | .1 |

---

**Services à déployer :**

- ✅ Site web : `http://cabinet-stjean.local` (page d'accueil, horaires)
- ✅ DHCP sur les 3 VLANs
- ⚠️ **Important** : VLAN 30 (labo) **doit être isolé** (pas d'accès depuis autres VLANs)

---

## SUJET 3 : LYCÉE PROFESSIONNEL (18 postes)

### Présentation du client

**Nom :** Lycée Professionnel Jean Moulin  
**Activité :** Enseignement professionnel (BAC PRO CIEL)  
**Effectif :** 18 postes informatiques  
**Locaux :** Administration + Salle des profs + 2 salles élèves

### Organigramme

```
Administration (3)
├─ Enseignants (5)
└─ Élèves (10)
```

### Besoin exprimé

Le lycée souhaite :
- **Séparer** l'administration (données personnelles élèves)
- **Isoler** les élèves (filtrage web - optionnel)
- **Donner accès** aux enseignants à tous les VLANs (routage)

### Spécifications techniques

**3 VLANs à créer :**

| **VLAN** | **Nom** | **Services** | **Nb postes** |
|----------|---------|--------------|--------------|
| VLAN 10 | ADMINISTRATION | Direction + Secrétariat | 3 |
| VLAN 20 | ENSEIGNANTS | Salle des profs | 5 |
| VLAN 30 | ELEVES | Salles informatiques | 10 |

---

**Plan d'adressage suggéré :**

| **VLAN** | **Réseau** | **Plage DHCP** | **Passerelle** |
|----------|-----------|---------------|---------------|
| 10 | 10.10.0.0/24 | .100 - .120 | .1 |
| 20 | 10.20.0.0/24 | .100 - .150 | .1 |
| 30 | 10.30.0.0/24 | .100 - .200 | .1 |

---

**Services à déployer :**

- ✅ Site web : `http://lycee-jmoulin.local` (portail ENT simplifié)
- ✅ DHCP sur les 3 VLANs
- ⭐ **Bonus** : Routage inter-VLAN pour enseignants

---

## SUJET 4 : HÔTEL 3 ÉTOILES (12 postes)

### Présentation du client

**Nom :** Hôtel Le Grand Confort  
**Activité :** Hôtellerie-restauration  
**Effectif :** 12 postes  
**Locaux :** Réception + Direction + Restaurant + Maintenance

### Organigramme

```
Direction (2)
├─ Réception (3)
├─ Restaurant (4)
└─ Maintenance technique (3)
```

### Besoin exprimé

L'hôtel souhaite :
- **Séparer** la réception (système de réservation)
- **Isoler** la direction (comptabilité)
- **Donner accès Internet** au restaurant (commandes en ligne)

### Spécifications techniques

**3 VLANs à créer :**

| **VLAN** | **Nom** | **Services** | **Nb postes** |
|----------|---------|--------------|--------------|
| VLAN 10 | DIRECTION | Direction + Comptabilité | 2 |
| VLAN 20 | RECEPTION | Accueil + Réservations | 3 |
| VLAN 30 | SERVICES | Restaurant + Maintenance | 7 |

---

**Plan d'adressage suggéré :**

| **VLAN** | **Réseau** | **Plage DHCP** | **Passerelle** |
|----------|-----------|---------------|---------------|
| 10 | 172.16.10.0/24 | .50 - .80 | .1 |
| 20 | 172.16.20.0/24 | .50 - .80 | .1 |
| 30 | 172.16.30.0/24 | .50 - .100 | .1 |

---

**Services à déployer :**

- ✅ Site web : `http://hotel-grandconfort.local` (site vitrine de l'hôtel)
- ✅ DHCP sur les 3 VLANs
- ⭐ **Bonus** : Page de réservation (formulaire HTML)

---

## SUJET 5 : START-UP TECH (16 postes)

### Présentation du client

**Nom :** TechInnovate SAS  
**Activité :** Développement logiciels et applications mobiles  
**Effectif :** 16 collaborateurs  
**Locaux :** Open space moderne

### Organigramme

```
Direction/RH (3)
├─ Développement (8)
├─ Marketing (3)
└─ Support Client (2)
```

### Besoin exprimé

La start-up souhaite :
- **Isoler** le développement (serveurs Git, base de données)
- **Séparer** le marketing (accès externe, démonstrations clients)
- **Centraliser** la direction/RH

### Spécifications techniques

**3 VLANs à créer :**

| **VLAN** | **Nom** | **Services** | **Nb postes** |
|----------|---------|--------------|--------------|
| VLAN 10 | DIRECTION | Direction + RH | 3 |
| VLAN 20 | DEV | Développeurs + Serveurs | 8 |
| VLAN 30 | MARKETING | Marketing + Support | 5 |

---

**Plan d'adressage suggéré :**

| **VLAN** | **Réseau** | **Plage DHCP** | **Passerelle** |
|----------|-----------|---------------|---------------|
| 10 | 192.168.100.0/24 | .50 - .80 | .1 |
| 20 | 192.168.200.0/24 | .50 - .100 | .1 |
| 30 | 192.168.300.0/24 | .50 - .80 | .1 |

---

**Services à déployer :**

- ✅ Site web : `http://techinnovate.local` (landing page moderne)
- ✅ DHCP sur les 3 VLANs
- ⭐ **Bonus** : Page "Carrières" avec CSS avancé

---

## SUJET 6 : CABINET D'ARCHITECTES (14 postes)

### Présentation du client

**Nom :** ArchiDesign & Partners  
**Activité :** Architecture et design d'intérieur  
**Effectif :** 14 collaborateurs  
**Locaux :** Bureaux + Salle de dessin

### Organigramme

```
Direction (2)
├─ Architectes (6)
├─ Dessinateurs CAO/DAO (4)
└─ Comptabilité/Accueil (2)
```

### Besoin exprimé

Le cabinet souhaite :
- **Prioriser** les dessinateurs (gros fichiers CAO, bande passante)
- **Séparer** l'administration
- **Centraliser** les architectes

### Spécifications techniques

**3 VLANs à créer :**

| **VLAN** | **Nom** | **Services** | **Nb postes** |
|----------|---------|--------------|--------------|
| VLAN 10 | ADMIN | Direction + Comptabilité | 4 |
| VLAN 20 | ARCHITECTES | Architectes seniors | 6 |
| VLAN 30 | DESSINATEURS | CAO/DAO + Impression | 4 |

---

**Plan d'adressage suggéré :**

| **VLAN** | **Réseau** | **Plage DHCP** | **Passerelle** |
|----------|-----------|---------------|---------------|
| 10 | 10.0.10.0/24 | .10 - .50 | .1 |
| 20 | 10.0.20.0/24 | .10 - .50 | .1 |
| 30 | 10.0.30.0/24 | .10 - .50 | .1 |

---

**Services à déployer :**

- ✅ Site web : `http://archidesign.local` (portfolio projets)
- ✅ DHCP sur les 3 VLANs
- ⭐ **Bonus** : Galerie photos (plusieurs images)

---

## SUJET 7 : AGENCE IMMOBILIÈRE (12 postes)

### Présentation du client

**Nom :** ImmoPlus Transactions  
**Activité :** Vente et location immobilière  
**Effectif :** 12 collaborateurs  
**Locaux :** Agence + Bureaux négociateurs

### Organigramme

```
Direction (2)
├─ Agents immobiliers (6)
├─ Service juridique (2)
└─ Accueil (2)
```

### Besoin exprimé

L'agence souhaite :
- **Isoler** le juridique (contrats sensibles)
- **Centraliser** les agents (accès base de données annonces)
- **Séparer** l'accueil (accès public)

### Spécifications techniques

**3 VLANs à créer :**

| **VLAN** | **Nom** | **Services** | **Nb postes** |
|----------|---------|--------------|--------------|
| VLAN 10 | DIRECTION | Direction + Juridique | 4 |
| VLAN 20 | AGENTS | Agents immobiliers | 6 |
| VLAN 30 | ACCUEIL | Accueil public | 2 |

---

**Plan d'adressage suggéré :**

| **VLAN** | **Réseau** | **Plage DHCP** | **Passerelle** |
|----------|-----------|---------------|---------------|
| 10 | 192.168.1.0/24 | .10 - .50 | .1 |
| 20 | 192.168.2.0/24 | .10 - .50 | .1 |
| 30 | 192.168.3.0/24 | .10 - .20 | .1 |

---

**Services à déployer :**

- ✅ Site web : `http://immoplus.local` (annonces immobilières)
- ✅ DHCP sur les 3 VLANs
- ⭐ **Bonus** : Formulaire contact HTML

---

## SUJET 8 : CENTRE DE FORMATION (18 postes)

### Présentation du client

**Nom :** Centre de Formation Professionnelle CIEL  
**Activité :** Formation continue et apprentissage  
**Effectif :** 18 postes  
**Locaux :** Administration + Formateurs + 3 salles stagiaires

### Organigramme

```
Administration (3)
├─ Formateurs (5)
└─ Stagiaires (10)
```

### Besoin exprimé

Le centre souhaite :
- **Séparer** l'administration (données stagiaires - RGPD)
- **Isoler** les formateurs (préparation cours)
- **Segmenter** les stagiaires (3 groupes = 3 salles)

### Spécifications techniques

**3 (ou 4) VLANs à créer :**

| **VLAN** | **Nom** | **Services** | **Nb postes** |
|----------|---------|--------------|--------------|
| VLAN 10 | ADMIN | Administration | 3 |
| VLAN 20 | FORMATEURS | Espace formateurs | 5 |
| VLAN 30 | STAGIAIRES | Salles de formation | 10 |

---

**Plan d'adressage suggéré :**

| **VLAN** | **Réseau** | **Plage DHCP** | **Passerelle** |
|----------|-----------|---------------|---------------|
| 10 | 10.100.0.0/24 | .10 - .50 | .1 |
| 20 | 10.200.0.0/24 | .10 - .50 | .1 |
| 30 | 10.300.0.0/24 | .10 - .100 | .1 |

---

**Services à déployer :**

- ✅ Site web : `http://cfp-ciel.local` (portail de formation)
- ✅ DHCP sur les 3 VLANs
- ⭐ **Bonus** : Catalogue formations (liste HTML)

---

## 📝 PLANIFICATION DU PROJET

### Répartition des tâches (à compléter)

| **Tâche** | **Responsable** | **Durée estimée** | **Statut** |
|-----------|----------------|-------------------|------------|
| Câblage RJ45 (6 câbles) | _______________ | _____ min | ☐ |
| Configuration switch (VLANs) | _______________ | _____ min | ☐ |
| Configuration DHCP | _______________ | _____ min | ☐ |
| Configuration Apache | _______________ | _____ min | ☐ |
| Création page web | _______________ | _____ min | ☐ |
| Tests de connectivité | _______________ | _____ min | ☐ |
| Documentation (schémas) | _______________ | _____ min | ☐ |
| Préparation soutenance | _______________ | _____ min | ☐ |

---

### Planning prévisionnel

**Jour 1 - Après-midi :**

- 14h00 - 14h45 : _______________________________________________________
- 14h45 - 15h30 : _______________________________________________________
- 15h30 - 16h15 : _______________________________________________________
- 16h15 - 17h00 : _______________________________________________________

**Jour 2 - Matin :**

- 09h00 - 10h00 : _______________________________________________________
- 10h00 - 11h00 : _______________________________________________________
- 11h00 - 12h00 : _______________________________________________________

---

## ✅ CHECKLIST AVANT RECETTAGE

**À vérifier avant l'arrivée du formateur :**

### Infrastructure physique
- ☐ 6 câbles RJ45 minimum fabriqués
- ☐ Tous les câbles testés au testeur (OK)
- ☐ Câbles étiquetés (VLAN 10, VLAN 20, VLAN 30)
- ☐ Connexions physiques réalisées (PC → Switch → Serveur)

### Switch
- ☐ 3 VLANs créés (commande `vlan XX`)
- ☐ Ports affectés aux VLANs (commande `switchport access vlan XX`)
- ☐ Configuration sauvegardée (`write memory`)
- ☐ Test : `show vlan brief` affiche les 3 VLANs

### DHCP
- ☐ Serveur DHCP installé (`isc-dhcp-server`)
- ☐ 3 pools configurés dans `/etc/dhcp/dhcpd.conf`
- ☐ Service démarré (`systemctl status isc-dhcp-server`)
- ☐ Test : PC client obtient une IP automatique

### Serveur Web
- ☐ Apache installé (`apache2`)
- ☐ Page HTML créée dans `/var/www/html/`
- ☐ Permissions correctes (www-data, 644)
- ☐ Test : Site accessible via navigateur

### Tests de connectivité
- ☐ Ping intra-VLAN réussi (2 PC même VLAN)
- ☐ Ping inter-VLAN échoué (2 PC VLANs différents, sans routage)
- ☐ Accès web fonctionnel (navigateur affiche le site)
- ☐ Logs consultés (`/var/log/apache2/access.log`)

### Documentation
- ☐ Schéma physique dessiné
- ☐ Schéma logique avec VLANs
- ☐ Plan d'adressage rempli
- ☐ Captures d'écran prises (au moins 5)
- ☐ Dossier PDF généré

### Soutenance
- ☐ Diaporama préparé (optionnel)
- ☐ Démonstration répétée (tests live)
- ☐ Questions anticipées

---

## 📄 STRUCTURE DU DOSSIER TECHNIQUE

**Modèle de sommaire (à adapter) :**

```
DOSSIER TECHNIQUE - [NOM DU PROJET]

1. Page de garde
   - Nom du projet
   - Binôme
   - Date

2. Sommaire

3. Introduction
   - Contexte client
   - Objectifs du projet

4. Architecture réseau
   4.1. Schéma physique (topologie)
   4.2. Schéma logique (VLANs)
   4.3. Plan d'adressage

5. Configuration switch
   5.1. Création des VLANs
   5.2. Affectation des ports
   5.3. Sauvegarde configuration

6. Configuration DHCP
   6.1. Installation serveur
   6.2. Configuration des pools
   6.3. Tests

7. Configuration serveur web
   7.1. Installation Apache
   7.2. Création page HTML
   7.3. Tests d'accès

8. Tests de validation
   8.1. Connectivité intra-VLAN
   8.2. Isolation inter-VLAN
   8.3. Obtention IP via DHCP
   8.4. Accès site web

9. Procédure de dépannage
   9.1. Méthodologie
   9.2. Outils (ping, traceroute, logs)

10. Difficultés rencontrées
    10.1. Problèmes techniques
    10.2. Solutions apportées

11. Conclusion
    - Bilan du projet
    - Compétences acquises

12. Annexes
    - Captures d'écran
    - Extraits de configurations
    - Logs
```

---

## 🎤 GUIDE DE SOUTENANCE

### Structure de la présentation (10 minutes)

**Minute 0-1 : Introduction**

> "Bonjour, nous sommes [Prénom 1] et [Prénom 2]. Nous avons déployé l'infrastructure réseau de [Nom Client]. Notre mission était de [objectifs]."

---

**Minutes 1-4 : Architecture**

- **Montrer le schéma physique** (topologie, équipements)
- **Montrer le schéma logique** (VLANs, adressage IP)
- **Expliquer les choix** ("Nous avons créé 3 VLANs car...")

---

**Minutes 4-8 : Démonstration live**

- **Test 1** : Ping intra-VLAN → ✅
- **Test 2** : `ipconfig` sur PC → IP DHCP
- **Test 3** : Site web dans navigateur → ✅
- **Test 4** : `show vlan brief` sur switch → VLANs

---

**Minutes 8-10 : Difficultés et conclusion**

- **Difficulté principale** rencontrée
- **Solution** apportée
- **Bilan** : ce qu'on a appris

---

### Questions fréquentes du formateur

**Préparez vos réponses :**

1. "Pourquoi avoir choisi ce plan d'adressage ?"
2. "Combien d'adresses IP disponibles dans VLAN 20 ?"
3. "Comment diagnostiquer si DHCP ne fonctionne pas ?"
4. "Que faire si un PC n'obtient pas d'IP ?"
5. "Quelle commande pour voir les baux DHCP actifs ?"
6. "Pourquoi isoler la comptabilité dans un VLAN séparé ?"

---

## 🏆 CONSEILS POUR RÉUSSIR

### Les erreurs à éviter

❌ **NE PAS** :
- Oublier de sauvegarder la config switch (`write memory`)
- Négliger les tests (tester au dernier moment)
- Bâcler la documentation (schémas illisibles)
- Improviser la soutenance (pas de répétition)
- Travailler chacun dans son coin (pas de communication binôme)

### Les bonnes pratiques

✅ **FAIRE** :
- Tester régulièrement (après chaque étape)
- Documenter au fur et à mesure (pas tout à la fin)
- Communiquer avec son binôme (répartition claire)
- Consulter les logs en cas de problème
- Répéter la soutenance avant le passage
- Anticiper les questions du formateur

---

**Bon courage pour votre projet ! 🚀**

**Date de création :** 24/02/2026  
**Version :** 1.0  
**Auteur :** Yahn LE PRETTRE
