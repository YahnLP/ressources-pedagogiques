# 🔬 ATELIER PRATIQUE — S18 · 3ᵉ ANNÉE · E31
## Produire des schémas professionnels · Évaluer la qualité d'un dossier

---

> **Nom** : ___________________________ **Binôme** : ___________________________
> **Date** : ___________________________
> **Durée** : 95 minutes (atelier schémas 30 min + production DAT 65 min)
> **Outils** : Draw.io (https://app.diagrams.net) · LibreOffice Writer

---

## 📌 Compétences travaillées

| Code | Compétence |
|---|---|
| **C3.1a** | Produire un schéma d'architecture logique professionnel |
| **C3.1b** | Produire un schéma physique annoté |
| **C3.2** | Rédiger des procédures d'exploitation |
| **C2.3** | Documenter les tests de validation |

---

## 🎯 EXERCICE 1 — Évaluer un dossier (10 min)

> Voici deux extraits de plans d'adressage. Lequel est professionnel ?
> Identifie les différences et justifie ton choix.

**Extrait A :**

```
R_SIEGE a plusieurs interfaces. Son IP vers le LAN est 192.168.1.1 avec un masque
en /24 donc 192.168.1.0. L'interface WAN est en 10.0.0.1/30. La loopback est 1.1.1.1.
R_AGENCE a l'IP 192.168.2.1 sur son LAN et 10.0.0.2 sur le WAN.
```

**Extrait B :**

| Équipement | Interface | Adresse IP | CIDR | Masque | Rôle |
|---|---|---|---|---|---|
| R_SIEGE | Gi0/0.10 | 192.168.1.1 | /24 | 255.255.255.0 | Passerelle VLAN 10 |
| R_SIEGE | Gi0/1 | 10.0.0.1 | /30 | 255.255.255.252 | WAN vers R_AGENCE |
| R_SIEGE | Lo0 | 1.1.1.1 | /32 | 255.255.255.255 | Router-ID OSPF |
| R_AGENCE | Gi0/0 | 192.168.2.1 | /24 | 255.255.255.0 | Passerelle LAN Agence |
| R_AGENCE | Gi0/1 | 10.0.0.2 | /30 | 255.255.255.252 | WAN vers R_SIEGE |

```
Extrait professionnel : ___  Raisons (3 minimum) :
1. ____________________________________________________________________________
2. ____________________________________________________________________________
3. ____________________________________________________________________________

Ce qui manque encore dans l'Extrait B pour être parfait :
_______________________________________________________________________________
```

---

## 🖼️ EXERCICE 2 — Produire le schéma logique (30 min)

### Dans Draw.io, crée le schéma logique de NEXALINK

**Éléments obligatoires (cochés = point obtenu) :**

```
☐ Titre du schéma et date
☐ R_LYON avec ses 3 sous-interfaces annotées (Gi0/0.100, .300, .400 avec IPs)
☐ R_MARSEILLE avec ses interfaces annotées
☐ Lien WAN avec le réseau /30 indiqué
☐ SW_CORE_LYON et SW_ACC_LYON avec EtherChannel représenté
☐ VLAN 100 représenté par une zone colorée bleue
☐ VLAN 300 représenté par une zone colorée rouge
☐ VLAN 400 représenté par une zone colorée verte
☐ Area 0 OSPF délimitée (contour pointillé)
☐ Area 1 OSPF délimitée (contour pointillé)
☐ Légende des couleurs/symboles
☐ PC_Direction dans VLAN 100 · IP_Phone dans VLAN 300
```

**Score schéma logique : ___/12**

---

## 🏗️ EXERCICE 3 — Produire le schéma physique (20 min)

> Le schéma physique n'est pas une vue logique — c'est une vue "terrain".
> Il répond à : "Quel câble, dans quel port, entre quels équipements ?"

### Dans Draw.io, crée la vue physique (vue en rack ou vue câblage)

**Éléments obligatoires :**

```
☐ SW_CORE_LYON avec modèle indiqué (ex: Cisco 3560-24PS)
☐ SW_ACC_LYON avec modèle
☐ R_LYON avec modèle
☐ Numéros de ports sur chaque lien :
     SW_CORE Gi0/1 ─────── Gi0/1 SW_ACC  (EtherChannel lien 1)
     SW_CORE Gi0/2 ─────── Gi0/2 SW_ACC  (EtherChannel lien 2)
     SW_CORE Gi0/24 ─────── Gi0/0 R_LYON  (trunk)
☐ Types de câbles indiqués (cuivre CAT6, fibre OM3, câble série...)
☐ Emplacement physique mentionné (Rack A, salle serveurs RDC)
```

**Score schéma physique : ___/5**

---

## 📋 EXERCICE 4 — Rédiger les 2 procédures manquantes (25 min)

> En te basant sur le gabarit DAT (section 6), complète les procédures 6.2 et 6.3.
> Rédige directement dans le gabarit.

### Procédure 6.2 — Modification de configuration en production

```
Éléments obligatoires à inclure :
  ☐ Sauvegarde préalable AVANT toute modification (étape 0)
  ☐ Fenêtre de maintenance indiquée (samedi 22h)
  ☐ Approbation du responsable mentionnée
  ☐ Tests de validation post-modification (au moins 2 tests)
  ☐ Procédure de rollback détaillée avec commandes exactes
  ☐ RTO en cas de rollback estimé (chiffre)

Score procédure 6.2 : ___/6
```

### Procédure 6.3 — Rétablissement après panne WAN

```
Éléments obligatoires à inclure :
  ☐ Symptômes observables décrits (ce que voit l'admin)
  ☐ Commandes de diagnostic listées avec résultats attendus
  ☐ Action si basculement automatique fonctionne
  ☐ Action si intervention manuelle nécessaire
  ☐ Procédure d'escalade vers l'opérateur
  ☐ RTO cible chiffré

Score procédure 6.3 : ___/6
```

---

## ✅ EXERCICE 5 — Relecture croisée (10 min)

> Échange ton dossier avec ton binôme. Utilise cette grille pour évaluer son travail.

### Grille de relecture

| Critère | Oui ✓ | Partiel ~ | Non ✗ | Commentaire |
|---|---|---|---|---|
| Page de garde avec référence, version, date | | | | |
| Table des matières présente | | | | |
| Schéma logique avec VLANs et areas | | | | |
| Plan d'adressage en tableau (pas en texte) | | | | |
| Configs avec commentaires (pas juste brut) | | | | |
| Justifications précises (termes techniques) | | | | |
| Procédures avec rollback | | | | |
| Tableau de tests avec résultats réels | | | | |
| PRA avec 2 scénarios et RTO chiffrés | | | | |
| Document paginé et structuré | | | | |

**Score relecture croisée : ___/10**

**Mon meilleur conseil pour améliorer le dossier de mon binôme :**

```
_______________________________________________________________________________
_______________________________________________________________________________
```

---

## 📊 Score global de l'atelier

| Exercice | /pts | Score |
|---|---|---|
| Ex.1 — Évaluation dossier | /4 | |
| Ex.2 — Schéma logique | /12 | |
| Ex.3 — Schéma physique | /5 | |
| Ex.4 — Procédures 6.2 + 6.3 | /12 | |
| Ex.5 — Relecture croisée | /7 | |
| **TOTAL** | **/40** | |

---

---

# ✅ CORRECTION DE L'ATELIER — Document enseignant uniquement

## Exercice 1 — Évaluation dossier

```
Extrait professionnel : B

Raisons :
  1. Tableau lisible en un coup d'œil (vs texte à analyser)
  2. Informations complètes (masque ET CIDR ET rôle)
  3. Facilement maintenable (modifier 1 ligne = 1 équipement)
  4. Référençable (chaque ligne est unique et précise)
  5. Interopérable (tout technicien peut l'utiliser)

Ce qui manque encore dans B :
  → Wildcard mask (pour OSPF)
  → LAN/VLAN de chaque interface
  → Adresse de broadcast
  → Adresse de réseau (première IP du sous-réseau)
```

## Exercice 2 — Schéma logique

```
Points accordés par élément présent (voir liste).
Critère principal : lisibilité et complétude.

Erreurs fréquentes attendues :
  → Schéma sans légende → -2 pts
  → Areas OSPF non délimitées → -2 pts
  → Adresses IP manquantes sur les interfaces → -1 pt par interface
  → EtherChannel représenté comme un seul lien → -1 pt
```

## Exercice 4 — Procédures

```
Proc. 6.2 éléments critiques :
  L'étape 0 "sauvegarde AVANT modification" est OBLIGATOIRE → -2 pts si absente
  Le rollback doit contenir les commandes exactes :
    erase startup-config / copy tftp: startup-config / reload

Proc. 6.3 éléments critiques :
  RTO doit être chiffré (pas "rapidement") : exemple 30 min pour basculement automatique
  Escalade opérateur : si pas résolu en X min → appel hotline + ouverture ticket
```

---

*Atelier Schémas + Évaluation DAT — BAC PRO CIEL | E31 Infrastructure Réseau | 3ᵉ année S18*
*Compétences : C3.1 · C3.2 · C2.3*
